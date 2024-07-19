import cv2
from deepface import DeepFace
from response import get_response
from recognizeSpeech import record_audio, recognize_speech
from voiceOut import Voice_out


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


def detect_emotions(callback):
    detect_emotion_flag = True
    
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = rgb_frame[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

  
            callback(x, y)

 
            if detect_emotion_flag:
                result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']
                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                # Start conversation based on the detected emotion
                response = get_response(emotion)
                print(response)
                Voice_out(response)

                for i in range(0, 2, 1):
                    audio = record_audio()
                    text = recognize_speech(audio)
                    conversation = get_response(text)
                    Voice_out(conversation)


        cv2.imshow('Real-time Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()