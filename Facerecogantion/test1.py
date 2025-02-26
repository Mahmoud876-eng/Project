import cv2
import face_recognition
import pyttsx3

# Load known face and encode it
known_image = face_recognition.load_image_file("mahmoud.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize camera
video_capture = cv2.VideoCapture(0)
engine = pyttsx3.init()

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

    # Detect face locations and encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        
        if True in matches:
            print("Mahmoud detected! Time to take medicine.")
            engine.say("Hello Mahmoud, it's time to take your medicine.")
            engine.runAndWait()
    
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
