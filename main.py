from flask import Flask, render_template, request 
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        # Handle file upload and reel creation logic here
        print(request.files.keys())
        recv_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            print(key, value)
            # Upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], recv_id)):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], recv_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], recv_id, filename))
                input_files.append(file.filename)
            # Capture the description that the user entered and save it to a text file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], recv_id, "desc.txt"), "w") as f:
                f.write(desc)
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], recv_id, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n") # Assuming each image is shown for 1 second

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)