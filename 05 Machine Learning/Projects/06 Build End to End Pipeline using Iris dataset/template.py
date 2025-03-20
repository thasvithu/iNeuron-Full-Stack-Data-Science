from pathlib import Path

project_name = "iris-project"

folders = [
    f"src/{project_name}",
    f"src/{project_name}/components",
    f"src/{project_name}/utils",
    f"src/{project_name}/config",
    f"src/{project_name}/pipeline",
    f"src/{project_name}/pipeline/train",
    f"src/{project_name}/pipeline/predict",
]

files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train/train_model.py",
    f"src/{project_name}/pipeline/predict/predict_model.py",
    "main.py",
    "requirements.txt",
    "test.py"
]

# Create the folders
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

# Create the files
for file in files:
    Path(file).touch()

print("Project structure created successfully!")