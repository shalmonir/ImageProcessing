import json

from flask import Blueprint, request

from FaceRecognition.processing.FaceRecognition import FaceRecognition
from FaceRecognition.validation.ImageProcessingRequestValidator import ImageProcessingRequestValidator

recognition = Blueprint('recognition', import_name=__name__)


@recognition.route('/detect_faces', methods=['POST'])
def face_recognition():
    request_payload = json.loads(request.data.decode())
    validation_result = ImageProcessingRequestValidator.validate_face_recognition(request_payload)
    if validation_result.validity is not True:
        return {'result': None, 'Error': 'Illegal request content'}
    image = request_payload['picture']
    inst = FaceRecognition()
    return {'result': inst.recognize(image)}

