import os
import shutil

from supervisely.app.widgets import (
    Button,
    Card,
    Field,
    Container,
    Text,
    Flexbox,
    FileStorageUpload,
    Checkbox,
    Input
)

import ds_manager
import src.globals as g
from ds_manager.tools.dumping_sly import dump_sly


def selector():
    '''
    Step 1: Select and scan dataset w/ dragndrop
    '''

    file_upload = FileStorageUpload(
        team_id=g.TEAM_ID,
        path="input",
    )
    upload_1 = Field(
        title="Upload folder with Coco/Pascal/Yolo/Cityscapes format dataset",
        description="Make sure that annotaions and photos are separated",
        content=file_upload,
    )
    mask_in_project = Checkbox("Project includes PNG masks", checked=False)
    button_select = Button('Scan dataset')
    text = Text()
    upload_container = Container([upload_1])
    btns_box = Flexbox([button_select])
    input_console = Input(value="If images in project have PNG ext, pls input image folder")
    controls_container = Container([mask_in_project,input_console, btns_box, text])
    # g.input_text = Text()
    # input_select = Button('Input command')
    # input_container =  Container([g.input_console, g.input_text, input_select])
    card = Card(
        title="File Storage Upload",
        content=Container([upload_container, controls_container]),
    )

    @button_select.click
    def take_root():
        try:
            paths = file_upload.get_uploaded_paths()
            common_path = os.path.commonpath(paths)
            g.api.file.download_directory(g.TEAM_ID, common_path, 'input') #Works only with Unix/WSL
            if common_path.startswith('\\'):
                common_path = common_path.lstrip('\\')
            elif common_path.startswith('/'):
                common_path = common_path.lstrip('/')
            img_path = 'input'
            if mask_in_project.is_checked():
                img_path = input_console.get_value()
            g.DATA = ds_manager.Dataset(data='input', mask = mask_in_project.is_checked(), img_path=img_path)
            g.DATA = ds_manager.scan(g.DATA)
            ds_class = str(g.DATA.__class__.__name__)
            text.set(
                    text=f'\n{ds_class} format detected. {len(g.DATA.root)} objects in Root collected.',
                    status="success"
                    )
            text.show()
            card.lock()
            curr_step = g.stepper.get_active_step()
            curr_step += 1
            g.stepper.set_active_step(curr_step)
        except Exception as e:
            shutil.rmtree('input')
        try:
            dump_sly(g.DATA.root)
            text.set(
                        text="Convertation success!'", status="success"
                    )
            text.show()
            curr_step = g.stepper.get_active_step()
            curr_step += 1
            g.stepper.set_active_step(curr_step)
            # text.text = f'\n Convertation success!'
        except Exception as e:
            text.status = "error"
            text.set(
                        text="Please, specify path to folder in Supervisely Team Files", status="error"
                    )
            text.show()
    return card
