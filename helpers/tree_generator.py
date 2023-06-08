import os


def generate_project_tree(root_path, exclude_folders=None):
    if exclude_folders is None:
        exclude_folders = []

    def generate_tree(folder, indent=""):
        folder_name = os.path.basename(folder)

        if folder_name in exclude_folders:
            return

        print(indent + folder_name)

        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)

            if item in exclude_folders or item_path in exclude_folders:
                continue

            if os.path.isfile(item_path):
                print(indent + "├── " + item)
            elif os.path.isdir(item_path):
                print(indent + "├── " + item + "/")
                generate_tree(item_path, indent + "│   ")

    generate_tree(root_path)


project_path = "."
excluded_folders = ["venv", ".git", ".idea", "__pycache__"]

generate_project_tree(project_path, excluded_folders)
