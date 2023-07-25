from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    Input,
    ProjectThumbnail,
    SelectWorkspace,
    SlyTqdm,
    Text,
    Checkbox
)
from supervisely.app import DialogWindowError

import src.globals as g
from ds_manager.tools.uploading import upload

def upload_2sly():
    """
    Step 3: Create Project and import data
    """

    ws_selector = SelectWorkspace(default_id=g.WORKSPACE_ID, team_id=g.TEAM_ID)
    output_project_name = Input(value="My Project")
    # project_creator = Container(widgets=[ws_selector, output_project_name])
    # project_card = Card(
    #     title="Create Project",
    #     description="Select destination team, workspace and enter project name",
    #     content=project_creator,
    # )

    start_import_btn = Button(text="Start Import")
    output_project_thumbnail = ProjectThumbnail()
    output_project_thumbnail.hide()
    output_text = Text()
    output_text.hide()
    output_progress = SlyTqdm()
    output_progress.hide()
    remove_source_files = Checkbox("Remove source files after successful import", checked=True)
    output_container = Container(
        widgets=[ws_selector, output_project_name, output_project_thumbnail, output_text, output_progress, start_import_btn, remove_source_files]
    )
    output_card = Card(
        title="Create Project and Import Data",
        description="Select destination team, workspace and enter project name", content=output_container
    )


    @start_import_btn.click
    def start_import():
        try:
            project_name = output_project_name.get_value()
            if project_name is None or project_name == "":
                output_text.set(text="Please, enter project name", status="error")
                output_text.show()
                return
            upload(
                api=g.api,
                WORKSPACE_ID=g.WORKSPACE_ID,
                proj_name=output_project_name.get_value(),
                delete=remove_source_files
                )
            output_text.set(text="Import success!", status="success")
            output_text.show()
            print('OK')
        except Exception as e:
            raise DialogWindowError(title="Import error", description=f"Error: {e}")
    return output_card
    