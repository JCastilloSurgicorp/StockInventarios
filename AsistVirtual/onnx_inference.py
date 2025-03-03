from StockInventarioB.serializers import *
from StockInventarioB.filters import *
from StockInventarioB.models import *
import ollama
import json

def generate_suggestion(user_prompt, max_length=50):
    # Tell the AI about our function
    tools = [
        {
            "type": "function",
            "function": {
                "name": "check_stock",
                "description": "Obtiene la cantidad que se tiene en el almacen del producto a consultar. Usa esta función cuando el usuario pida saber la cantidad que existe de un producto especifico del inventario. Ejemplo: ¿Cuanto tenemos de UM-4?",
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
            "content": "Eres un asistente de almacen que ayuda a los usuarios a saber si se tiene o no stock de ciertos productos y cuantos hay en el almacen. El usuario te entregará el nombre del producto. Ejemplo: UM-4",
        },
        {
            "role": "user",
            "content": f"{user_prompt}",
        },
    ]
    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=messages,
        tools=tools,
    )
    # return response.message
    # Get the name the AI wants to use a tool to say hello to
    try:
        tool_call = response.message.tool_calls[0]
        #return tool_call.function.arguments.get("prod")
        arguments = tool_call.function.arguments
        producto = arguments.get("prod")
        # Call the get_delivery_date function with the extracted order_id
        stock = check_stock(producto)
        # Create tool call request
        assistant_tool_call_request_message = {
            "role": "assistant",
            "tool_calls": [
                {
                    "function": response.message.tool_calls[0].function,
                }
            ],
        }
        # Create a message containing the result of the function call
        function_call_result_message = {
            "role": "tool",
            "content": json.dumps(
                {
                    "prod": producto,
                    "stock": stock,
                }
            )
        }
        # Prepare the chat completion call payload
        completion_messages_payload = [
            messages[0],
            messages[1],
            assistant_tool_call_request_message,
            function_call_result_message,
        ]
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=completion_messages_payload,
            tools=tools,
        )
        return response.message
    except Exception as e:
        return f"Error:{e}"

# Define a simple function
def check_stock(prod):
    try:
        sum = 0
        productos = StocksInventario.objects.filter(producto=prod).order_by('-stock')
        for stock in productos:
            sum = sum + stock.stock
        return f"{sum}"
    except Exception as e:
        return f"Error:{e}"
