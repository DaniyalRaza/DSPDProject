from flask import Flask, render_template, Response, request
from model import FacialExpressionModel
from werkzeug.utils import secure_filename
import keras.preprocessing.image as image
import numpy as np
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = FacialExpressionModel("model.json", "model_weights.h5")

@app.route('/')
def index():
    return 'Hello world'

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        img_width, img_height = 56, 56
        img = image.load_img(file_path, target_size = (img_width, img_height), grayscale = True)
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis = 0)/255
        result = model.predict_emotion(img)

        return result

def random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
