from FaceRecognition.validation.ValidationResult import ValidationResult


class ImageProcessingRequestValidator:
    @staticmethod
    def validate_face_recognition(request):
        return ValidationResult(True)
