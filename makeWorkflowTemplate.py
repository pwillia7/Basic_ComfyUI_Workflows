import os
import shutil

base_path = "/home/ptkwilliams/repos/Basic_ComfyUI_Workflows" 
output_path = os.path.join(base_path, "example_workflows")
os.makedirs(output_path, exist_ok=True)

for root, dirs, files in os.walk(base_path):
    if "WorkflowJSONs" in root or any(f.endswith(".json") for f in files):
        category = root.split(os.sep)[-2] if "WorkflowJSONs" in root else os.path.basename(root)
        images = {}
        for f in files:
            if f.endswith(".png") or f.endswith(".jpg"):
                images[os.path.splitext(f)[0]] = f
        for f in files:
            if f.endswith(".json"):
                name = os.path.splitext(f)[0]
                new_json = f"{category}__{f}"
                shutil.copy(os.path.join(root, f), os.path.join(output_path, new_json))
                if name in images:
                    img_ext = os.path.splitext(images[name])[1]
                    new_img = f"{category}__{name}{img_ext}"
                    shutil.copy(os.path.join(root, images[name]), os.path.join(output_path, new_img))
