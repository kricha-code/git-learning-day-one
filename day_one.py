import os
import shutil  # <--- The new "Moving Truck" library

user_home = os.path.expanduser("~")
downloads_path = os.path.join(user_home, "Downloads")

# The Rulebook (Dictionary)
# Key = Extension, Value = Where it should go
extension_map = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".exe": "Installers",
    ".msi": "Installers",
    ".apk": "Installers",
    ".zip": "Archives",
    ".rar": "Archives"
}

if os.path.exists(downloads_path):
    files_found = os.listdir(downloads_path)
    print(f"Starting clean up on {downloads_path}...")
    print("-" * 30) # Just a separator line

    for filename in files_found:
        #1. Split the name
        name, ext = os.path.splitext(filename)

        #2. Normalize the extension to lowercase so ".JPG" matches ".jpg"
        ext = ext.lower()
        #3. The Bouncer Check
        if ext in extension_map:
            target_folder_name = extension_map[ext]
            # 1. Construct the full path to the destination bucket
            # e.g., C:\Users\You\Downloads\Images
            target_path = os.path.join(downloads_path, target_folder_name)
            # 2. Builid the bucket if it doesn't exist yet
            if not os.path.exists(target_path):
                os.makedirs(target_path)
                print(f"🔨 Created new folder: {target_folder_name}")
            # 3. Define the Source (Old) and Destination (New) paths
            old_file_path = os.path.join(downloads_path, filename)
            new_file_path = os.path.join(target_path ,filename)

            # 4. Move it!
            # We use a try/except block just in case the file is open or busy
            try:
                shutil.move(old_file_path, new_file_path)
                print(f"🚚 Moved: {filename} -> {target_folder_name}/")
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")
        else:
            print(f"💤 Skipped: {filename}")
    print("-" * 30)
    print("Clean up complete!")