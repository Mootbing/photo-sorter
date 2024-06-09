import os
from datetime import datetime
import shutil

dir = "./photos/"

for photo in os.listdir(dir):
    photo_path = os.path.join(dir, photo)
    if os.path.isfile(photo_path):
        # Get the creation time of the file
        creation_time = os.path.getctime(photo_path)
        
        # Convert creation time to a datetime object
        creation_datetime = datetime.fromtimestamp(creation_time)
        
        # Extract year and month
        year = creation_datetime.strftime("%Y")
        month = creation_datetime.strftime("%m")
        
        # Create directory if it doesn't exist
        new_dir = os.path.join(dir, year, month)
        os.makedirs(new_dir, exist_ok=True)
        
        # Move the photo to the new directory
        new_photo_path = os.path.join(new_dir, photo)
        shutil.move(photo_path, new_photo_path)
