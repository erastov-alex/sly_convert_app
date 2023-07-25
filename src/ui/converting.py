from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    Text,
    SlyTqdm,
    ProjectThumbnail
)    

import src.globals as g
from ds_manager.tools.dumping_sly import dump_sly

def convert():
    '''
    # Step 2: Convert local to Supervisely
    '''

    convert_btn = Button(text="Convert")
    convert_project_thumbnail = ProjectThumbnail()
    convert_project_thumbnail.hide()
    convert_text = Text()
    convert_text.hide()
    convert_progress = SlyTqdm()
    convert_progress.hide()
    convert_container = Container(
        widgets=[convert_project_thumbnail, convert_text, convert_progress, convert_btn]
    )
    convert_card = Card(
        title="Convert", description="Press button to convert to Supervisely format", content=convert_container
    )
    
    @convert_btn.click
    def convert():
        try:
            dump_sly(g.DATA.root)
            convert_text.set(
                        text="Convertation success!'", status="success"
                    )
            convert_text.show()
            curr_step = g.stepper.get_active_step()
            curr_step += 1
            g.stepper.set_active_step(curr_step)
            # text.text = f'\n Convertation success!'
            convert_card.lock()
        except Exception as e:
            convert_text.status = "error"
            convert_text.set(
                        text="Please, specify path to folder in Supervisely Team Files", status="error"
                    )
            convert_text.show()

    return convert_card
