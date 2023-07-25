import os

import supervisely as sly
from dotenv import load_dotenv

# to show error message to user with dialog window
from supervisely.app import DialogWindowError

# widgets that we will use in GUI
from supervisely.app.widgets import (
    Button,
    Card,
    Field,
    Checkbox,
    Container,
    Input,
    ProjectThumbnail,
    SelectWorkspace,
    SlyTqdm,
    TeamFilesSelector,
    Text,
    Flexbox,
    FileStorageUpload,
    Stepper
)

import ds_manager
import src.globals as g

class MyApp:

    def __init__(self):
        self.data = None

    def run(self):
        # Step 1: Select and scan dataset w/ dragndrop
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

        # Step 2: Convert local to Supervisely
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

        # Step 3: Create Project
        ws_selector = SelectWorkspace(default_id=g.WORKSPACE_ID, team_id=g.TEAM_ID)
        output_project_name = Input(value="My Project")
        project_creator = Container(widgets=[ws_selector, output_project_name])
        project_card = Card(
            title="Create Project",
            description="Select destination team, workspace and enter project name",
            content=project_creator,
        )

        # Step 4: Output
        start_import_btn = Button(text="Start Import")
        output_project_thumbnail = ProjectThumbnail()
        output_project_thumbnail.hide()
        output_text = Text()
        output_text.hide()
        output_progress = SlyTqdm()
        output_progress.hide()
        output_container = Container(
            widgets=[output_project_thumbnail, output_text, output_progress, start_import_btn]
        )
        output_card = Card(
            title="Output", description="Press button to start import", content=output_container
        )
        convert_card.lock()
        project_card.lock()
        output_card.lock()

        stepper = Stepper(widgets=[card_info, card_success, card_warning],
                          titles=["Text step", "Success step", "Warning step"],
                          )

        # Create app
        layout = Container(widgets=[card,convert_card, project_card, output_card])
        app = sly.Application(layout=layout)

        @button_select.click
        def take_root():
            paths = file_upload.get_uploaded_paths()
            common_path = os.path.commonpath(paths)
            if common_path.startswith('\\'):
                common_path = common_path.lstrip('\\')
            self.data = ds_manager.Dataset(data=common_path)
            self.data = ds_manager.scan(self.data)
            ds_class = str(self.data.__class__.__name__)
            text.set(
                            text=f'\n{ds_class} format detected. {len(self.data.root)} objects in Root collected.', status="success"
                        )
            text.show()
            # text.status = "text"
            # text.text = f'\n{ds_class} format detected. {len(self.data.root)} objects in Root collected.'
            card.lock()
            convert_card.unlock()
            
        @convert_btn.click
        def convert():
            try:
                self.data.dump_sly()
                convert_text.set(
                            text="Convertation success!'", status="success"
                        )
                convert_text.show()
                # text.text = f'\n Convertation success!'
            except Exception as e:
                convert_text.status = "error"
                convert_text.set(
                            text="Please, specify path to folder in Supervisely Team Files", status="error"
                        )
                convert_text.show()

            convert_card.lock()
            project_card.unlock()
            output_card.unlock()

        @start_import_btn.click
        def start_import():
            try:
                card.lock()
                project_card.lock()
                output_text.hide()
                project_name = output_project_name.get_value()
                if project_name is None or project_name == "":
                    output_text.set(text="Please, enter project name", status="error")
                    output_text.show()
                    return
                self.data.upload(
                    api=g.api,
                    WORKSPACE_ID=g.WORKSPACE_ID,
                    proj_name=output_project_name.get_value()
                    )
                output_text.set(text="Import success!", status="success")
                output_text.show()
                output_card.lock()
                print('OK')
            except Exception as e:
                card.unlock()
                project_card.unlock()
                raise DialogWindowError(title="Import error", description=f"Error: {e}")
            
        return app
      
a = MyApp()
app = a.run()

