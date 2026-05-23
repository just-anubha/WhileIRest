import os
import shutil

path = r"C:\Users\KIIT\Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".java", ".js", ".html", ".css"],
    "Others": []
}

for file in os.listdir(path):
    full_path = os.path.join(path, file)
    
    if os.path.isfile(full_path):
        extension = os.path.splitext(file)[1].lower()
        destination_folder = "Others"
        
        for folder_name, extensions in folders.items():
            if extension in extensions:
                destination_folder = folder_name
                break
        
        folder_path = os.path.join(path, destination_folder)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        shutil.move(full_path, os.path.join(folder_path, file))
        
        print(f"Moved {file} → {destination_folder}")