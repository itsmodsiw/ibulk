from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename
import os
import zipfile
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')
        output_format = request.form.get('output_format')
        width = request.form.get('width')
        height = request.form.get('height')

        # If width or height is not provided, use None to keep original size
        width = int(width) if width else None
        height = int(height) if height else None

        file_paths = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                img = Image.open(file_path)
                img = img.convert('RGB')

                # If width and height are provided, resize the image
                if width and height:
                    img.thumbnail((width, height))

                base_filename, _ = os.path.splitext(filename)
                output_filename = base_filename + '.' + output_format
                output_filepath = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
                img.save(output_filepath)
                file_paths.append(output_filepath)

        # Create a zip file containing all the output files
        zip_filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
        zip_path = os.path.join(app.config['OUTPUT_FOLDER'], zip_filename)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_path in file_paths:
                zipf.write(file_path, arcname=os.path.basename(file_path))

        return send_from_directory(app.config['OUTPUT_FOLDER'], zip_filename, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
