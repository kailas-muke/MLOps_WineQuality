import os

dirs = [
    os.path.join("data", "raw"),       # os.path.join is used to give path to folder in any os
    os.path.join("data", "processed"),
    "notebooks",                        # experimenting using jupyter notebook
    "saved_models",                     # all the saved ML models
    "src"
]
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)    # exist_ok=True is used to to check the folder/repository name if it already present
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")

]
for file_ in files:
    with open(file_, "w") as f:
        pass
