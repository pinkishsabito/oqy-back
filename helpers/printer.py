import os

current_path = os.path.dirname(os.path.abspath(__file__))
folder_path = ".."
output_file = os.path.join(current_path, "output.txt")

print("Current script path:", current_path)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"Current script path: {current_path}\n\n")

    for root, dirs, files in os.walk(folder_path):
        if "venv" in dirs:
            dirs.remove("venv")
        if ".git" in dirs:
            dirs.remove(".git")
        if ".idea" in dirs:
            dirs.remove(".idea")
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        for file_name in files:
            file_path = os.path.join(root, file_name)

            file.write(f"File path: {file_path}\n")
            file.write("Content:\n")

            with open(file_path, "r", encoding="utf-8-sig") as inner_file:
                try:
                    content = inner_file.read()
                    file.write(content)
                except UnicodeDecodeError:
                    file.write("<Cannot decode content>\n")

            file.write("\n----------------------\n")

            print(file_path)
            print("Content:")
            print(content)
            print("----------------------")
