#####################################
## 미디어파이프.pdf의 12-13페이지
######################################

import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

mp_face_detection=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils


IMAGE_FILES=['./img/short.jpg']

with mp_face_detection.FaceDetection(
    
    ### selection=1은 5m 이내의 전신, 0은 2m 이내의 사진, 기본값은 0
    model_selection=0, min_detection_confidence=0.5) as face_detection:
        
    for idx, file in enumerate(IMAGE_FILES):
        image=cv2.imread(file)
        results=face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
              
        if not results.detections:
            print("Face not found in image")
        else: 
            print(len(results.detections)) # 얼굴인식 갯수 출력
            
            for detection in results.detections:
                    
                    for x in detection.location_data.relative_keypoints:
                        print('-'*50)
                        print(x)
                    