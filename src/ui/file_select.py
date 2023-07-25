import os

from supervisely.app.widgets import (
    Button,
    Card,
    Field,
    Container,
    Text,
    Flexbox,
    FileStorageUpload
)

import ds_manager
import src.globals as g

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
    button_select = Button('Scan dataset')
    text = Text()
    upload_container = Container([upload_1])
    btns_box = Flexbox([button_select])
    controls_container = Container([btns_box, text])
    card = Card(
        title="File Storage Upload",
        content=Container([upload_container, controls_container]),
    )

    @button_select.click
    def take_root():
        paths = file_upload.get_uploaded_paths()
        common_path = os.path.commonpath(paths)
        if common_path.startswith('\\'):
            common_path = common_path.lstrip('\\')
        elif common_path.startswith('/'):
            common_path = common_path.lstrip('/')
        g.DATA = ds_manager.Dataset(data=common_path)
        g.DATA = ds_manager.scan(g.DATA)
        ds_class = str(g.DATA.__class__.__name__)
        text.set(
                        text=f'\n{ds_class} format detected. {len(g.DATA.root)} objects in Root collected.', status="success"
                    )
        text.show()
        return g.DATA
    
    return card
