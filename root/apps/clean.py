import exifread
#from flask import Flask, flash, request, redirect, url_for
#from werkzeug.utils import secure_filename


#UPLOAD_FOLDER = '/path/to/the/uploads'


""" app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
 """


f = open('C:/Users/Amir/Documents/glasses.jpg','rb')


exif = exifread.process_file(f, details=True, stop_tag='Model')


print(exif)



""" def clean_file(filename):
    helper = exif.Image(file)
    metadata = helper.get_all()
    

    return((metadata))




print(clean_file(file))
 """

""" @app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']

		filename = clean_file(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash(filename)
		return
 """
