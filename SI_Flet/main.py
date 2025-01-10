import flet as fl


def main(page: fl.Page):
    page.title = "Calc App"
    result = fl.Text(value="0")

    # def button_clicked(self, e):
    #     if e.control.data == "AC":
    #         self.result.value = "0"

    page.add(
        fl.Container(
            width=350,
            bgcolor=fl.colors.BLACK,
            border_radius=fl.border_radius.all(20),
            padding=20,
            content=fl.Column(
                controls=[
                    fl.Row(controls=[result], alignment="end"),
                    fl.Row(
                        controls=[
                            ExtraActionButton(text="AC"),
                            ExtraActionButton(text="+/-"),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),
                        ]
                    ),
                    fl.Row(
                        controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*"),
                        ]
                    ),
                    fl.Row(
                        controls=[
                            DigitButton(text="4"),
                            DigitButton(text="5"),
                            DigitButton(text="6"),
                            ActionButton(text="-"),
                        ]
                    ),
                    fl.Row(
                        controls=[
                            DigitButton(text="1"),
                            DigitButton(text="2"),
                            DigitButton(text="3"),
                            ActionButton(text="+"),
                        ]
                    ),
                    fl.Row(
                        controls=[
                            DigitButton(text="0", expand=2),
                            DigitButton(text="."),
                            ActionButton(text="="),
                        ]
                    ),
                ]
            ),
        )
    )

class CalcButton(fl.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        #self.on_click = button_clicked
        self.data = text

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = fl.colors.WHITE24
        self.color = fl.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = fl.colors.ORANGE
        self.color = fl.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = fl.colors.BLUE_GREY_100
        self.color = fl.colors.BLACK

fl.app(main)