
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import cv2

### add the eye-recognizing model from haarcascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

if eye_cascade.empty():
    st.error("Failed to load eye cascade model.")

if "cx" not in st.session_state:
    st.session_state.cx, st.session_state.cy = 20.0, 20.0
    st.session_state.vx, st.session_state.vy = 0.0, 0.0

if "score" not in st.session_state:
    st.session_state["score"] = 0

st.title(f"Webcam Dodger")

class EyeDodger(VideoProcessorBase):
    def __init__(self):
        self.eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
        self.cx, self.cy = 20.0, 20.0
        self.vx, self.vy = 0.0, 0.0
        self.score = 0  # ← use local score

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, 1.1, 5)

        for i, (x, y, w, h) in enumerate(eyes):
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0 if i == 0 else 255, 0), 2)

        if len(eyes) > 0:
            x, y, w, h = eyes[0]
            tx, ty = x + w // 2, y + h // 2
            dx = tx - self.cx
            dy = ty - self.cy
            self.vx += dx * 0.05
            self.vy += dy * 0.05
            self.vx *= 0.9
            self.vy *= 0.9
            self.cx += self.vx
            self.cy += self.vy

            # Collision detection
            if not (x <= self.cx <= x + w and y <= self.cy <= y + h):
                self.score += 1

        # Draw red dot and score
        cv2.circle(img, (int(self.cx), int(self.cy)), 10, (0, 0, 255), -1)
        cv2.putText(img, f"Score: {self.score}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="dodger", video_processor_factory=EyeDodger)