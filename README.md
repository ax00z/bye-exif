# ByeExif

ByeExif is a simple yet effective Flask web application that allows users to remove EXIF metadata from their image files. It accepts a variety of file formats and provides an easy-to-use interface for uploading, processing, and downloading cleaned images.

## Features

- Supports multiple image file formats, including PNG, JPG, JPEG, and GIF
- Utilizes the `exifread` library to extract and remove EXIF metadata from images
- Provides a clean and straightforward user interface for file uploads and downloads
- Securely handles file uploads and storage using `werkzeug` utilities

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ````
   pip install Flask exifread
   ```
3. Set the `SECRET_KEY` environment variable for your Flask app or replace the placeholder in the code.
4. Create an `uploads` directory in the project root folder to store uploaded files.
5. Run the Flask app:
   ````
   export FLASK_APP=your_app_file.py
   export FLASK_ENV=development
   flask run
   ```

Access the application at http://localhost:5000 and start removing EXIF metadata from your images.

## Live Demo

You can also try the live demo of ByeExif at [https://61e0z6.deta.dev/](https://61e0z6.deta.dev/).
