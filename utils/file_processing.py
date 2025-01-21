import os
from werkzeug.utils import secure_filename
from config import Config

def save_file(file, file_type):
    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, file_type, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    file.save(filepath)
    return filepath
