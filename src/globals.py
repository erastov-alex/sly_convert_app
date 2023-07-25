import os

import supervisely as sly
from dotenv import load_dotenv

IS_PRODUCTION = sly.is_production()
if IS_PRODUCTION is True:
    load_dotenv("advanced.env")
    STORAGE_DIR = sly.app.get_data_dir()
else:
    load_dotenv("local.env")

load_dotenv(os.path.expanduser("~/supervisely.env"))

# Get ENV variables
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()
PATH_TO_FOLDER = sly.env.folder(raise_not_found=False)

api: sly.Api = sly.Api.from_env()




# if sly.is_development():
#     load_dotenv("local.env")
#     load_dotenv(os.path.expanduser("~/supervisely.env"))

# api: sly.Api = sly.Api.from_env()

# TEAM_ID = sly.env.team_id()
# WORKSPACE_ID = sly.env.workspace_id()
# PROJECT_ID = sly.env.project_id()
# DATASET_ID = sly.env.dataset_id(raise_not_found=False)

# PROJECT_INFO = api.project.get_info_by_id(id=PROJECT_ID)
# PROJECT_META = sly.ProjectMeta.from_json(data=api.project.get_meta(PROJECT_ID))