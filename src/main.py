import os

import supervisely as sly

from supervisely.app.widgets import (
    Container,
    Card,
    Button,
    Stepper
)

import src.globals as g
from src.ui.file_select import selector
from src.ui.converting import convert
from src.ui.uploading import upload_2sly

class MyApp:

    def __init__(self):
        self.data = None

    def run(self):
        card = selector()
        upload_card = upload_2sly()
        g.stepper = Stepper(
                        widgets=[card, upload_card],
                        titles=["Select and scan dataset", "Convert local to Supervisely", "Create Project and import data"],
                        )
        card = Card(
                    title="Stepper",
                    content=g.stepper,
                )
        layout = Container(widgets=[card])

        # layout = Container(widgets=[card,convert_card, upload_card])
        app = sly.Application(layout=layout)
        
        return app

a = MyApp()
app = a.run()

