import os
import shutil

# Base path is where this script is located
base_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_path, "example_workflows")
os.makedirs(output_path, exist_ok=True)

for root, dirs, files in os.walk(base_path):
    if "WorkflowJSONs" in root or root.endswith(("F5_TTS", "Video")):
        category = os.path.basename(os.path.dirname(root)) if "WorkflowJSONs" in root else os.path.basename(root)
        image_folder = os.path.join(os.path.dirname(root), "WorkflowImages")
        for f in files:
            if f.endswith(".json"):
                name = os.path.splitext(f)[0]
                json_path = os.path.join(root, f)
                new_json = f"{category}__{f}"
                shutil.copy(json_path, os.path.join(output_path, new_json))

                # Try to find a matching image
                for ext in [".png", ".jpg", ".jpeg"]:
                    image_name = name + ext
                    image_path = os.path.join(image_folder, image_name)
                    if os.path.exists(image_path):
                        new_img = f"{category}__{name}.jpg"  # Must be .jpg
                        shutil.copy(image_path, os.path.join(output_path, new_img))
                        break

print("✅ All templates copied into example_workflows/")
