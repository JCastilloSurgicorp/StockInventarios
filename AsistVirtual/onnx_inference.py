from StockInventarioB.serializers import *
from StockInventarioB.filters import *
from StockInventarioB.models import *
from django.db.models import Sum
import ollama
import json

def generate_suggestion(user_prompt, max_length=50):
    # Tell the AI about our function
    tools = [
        {
            "type": "function",
            "function": {
                "name": "check_stock",
                "description": "Obtiene la cantidad(stock) que se tiene en el almacen del producto a consultar. Usa esta función cuando el usuario pida saber la cantidad que existe de un producto especifico del inventario.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "prod": {
                            "type": "string",
                            "description": "Nombre del producto a consultar en la tabla de inventario",
                        },
                    },
                    "required": ["prod"],
                    "additionalProperties": False,
                },
            },
        }
    ]
    messages = [
        {
            "role": "system",
            "content": "Eres un asistente de almacen que ayuda a los usuarios a saber si se tiene o no stock de ciertos productos y cuantos hay en el almacen. El usuario te entregará el nombre comercial del producto y tienes que entregarle la cantidad de producto que existe por cada producto que en su descripcion contenga el nombre brindado (Normalmente el nombre del producto empieza con Mayúscula). Si no entendiste la pregunta o no lograste determinar cual era el producto a consultar, pide al usuario que ingrese el nombre del producto o que reformule su pregunta",
        },
        {
            "role": "user",
            "content": f"{user_prompt}",
        },
    ]
    response = ollama.chat(
        model="tripolskypetr/gemma3-tools:4b",
        messages=messages,
        tools=tools,
    )
    # return response.message
    # Get the name the AI wants to use a tool to say hello to
    try:
        tool_call = response.message.tool_calls[0]
        arguments = tool_call.function.arguments
        producto = arguments.get("prod")
        # Call the function
        stock = check_stock(producto)
        response.message.content = stock
        return response.message
    except Exception as e:
        return response.message

# Define a simple function
def check_stock(prod):
    try:
        productos = StocksInventario.objects.values('descr_prod').annotate(stock_total=Sum('stock')).filter(descr_prod__contains=prod, stock__gt=0).order_by('descr_prod')
        stock_string = ""
        for item in productos:
            stock_string = stock_string + f"{item['descr_prod']}:  \t{item['stock_total']} unidades,\n"
        stock_string = stock_string[:-2]
        if stock_string == "":
            return f"No tenemos stock de {prod} Actualmente.\nDesea consultar sobre otro producto?"
        return f"Tenemos los siguiente productos {prod} en stock: \n\n{stock_string}\n\nDesea consultar sobre algún otro producto?"
    except Exception as e:
        return f"Error:{e}"
