import os
from PIL import Image
from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def file_upload():
    if request.method == "POST":
        print("method is post")
        if request.files:
            for file_to_upload in request.files.getlist("uploaded_file"):
                file_to_upload.seek(0, os.SEEK_END)
                filename = (file_to_upload.filename)
                file_to_upload.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))
                return render_template('index.html', succ="Your file(s) are now being processed.")
        else:  # If no files request, redirect to index.
            return redirect(request.url)
    else:  # If not a POST request, load page as normal.
        return render_template('index.html', is_home='yes')


