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
        convert_card = convert()
        upload_card = upload_2sly()
        stepper = Stepper(
                        widgets=[card, convert_card, upload_card],
                        titles=["Select and scan dataset", "Convert local to Supervisely", "Create Project and import data"],
                        )
        card = Card(
                    title="Stepper",
                    content=stepper,
                )
        button_increase = Button(text="Increase step")
        button_decrease = Button(text="Decrease step")
        buttons_container = Container(widgets=[button_increase, button_decrease])
        buttons_card = Card(content=buttons_container)
        layout = Container(widgets=[card, buttons_card])


        # layout = Container(widgets=[card,convert_card, upload_card])
        app = sly.Application(layout=layout)

        @button_increase.click
        def click_button():
            curr_step = stepper.get_active_step()
            curr_step += 1
            stepper.set_active_step(curr_step)


        @button_decrease.click
        def click_button():
            curr_step = stepper.get_active_step()
            curr_step -= 1
            stepper.set_active_step(curr_step)
        
        return app

a = MyApp()
app = a.run()

