from flask import Flask

from FaceRecognition.API.recognition import recognition

app = Flask(__name__)
app.register_blueprint(recognition)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
