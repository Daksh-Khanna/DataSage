import face_recognition

class FaceAuthenticator:
    def verify(self, captured_image_bytes, known_image_path):
        try:
            unknown_image = face_recognition.load_image_file(captured_image_bytes)
            known_image = face_recognition.load_image_file(known_image_path)

            unknown_encodings = face_recognition.face_encodings(unknown_image)
            known_encodings = face_recognition.face_encodings(known_image)

            if not unknown_encodings or not known_encodings:
                return False

            result = face_recognition.compare_faces([known_encodings[0]], unknown_encodings[0])
            return result[0]
        except Exception as e:
            print(f"[Face Verification Error]: {e}")
            return False
