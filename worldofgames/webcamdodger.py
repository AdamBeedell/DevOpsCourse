

import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Webcam Dodger")


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    # ... process with OpenCV here ...
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

### add the eye-recognizing model from haarcascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


### broke below here


## find eyes
# if img:
#     ret, frame = cap.read()
#     if not ret:
        

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     # Draw rectangles around detected eyes
#     second = 0 # Colour 2nd eye differently (and any other which wont be tracked)

#     for (x, y, w, h) in eyes:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, second, 0), 2)
#         second = 255

#     # Update position if eye found
#     if len(eyes) > 0:
#         x, y, w, h = eyes[0]
#         tx, ty = x + w // 2, y + h // 2

#         dx = tx - cx
#         dy = ty - cy

#         ax = dx * 0.05
#         ay = dy * 0.05

#         vx += ax
#         vy += ay

#         vx *= 0.9
#         vy *= 0.9

#         cx += vx
#         cy += vy

#     # Draw moving circle
#     cv2.circle(frame, (int(cx), int(cy)), 10, (0, 0, 255), -1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

