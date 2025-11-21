######################################
##   img  폴더안의 모든 사진을 읽어서,
## 얼굴을 인식하면 박스를 그림
## 미디어파이프.pdf의 9페이지
######################################
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from glob import glob

mp_face_detection=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils


IMAGE_FILES=glob('./img/*.*')

with mp_face_detection.FaceDetection(
    
    ### selection=1은 5m 이내의 전신, 0은 2m 이내의 사진, 기본값은 0
    model_selection=0, min_detection_confidence=0.5) as face_detection:
        
    for idx, file in enumerate(IMAGE_FILES):
        image=cv2.imread(file)
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results=face_detection.process(image)
       
              
        if not results.detections:

            print(str(idx) + '-->'+ file + ':Face not found in image')
            
        else: 
            print(str(idx) + '-->'+  file + ':'+ str(len(results.detections)) + 'count')
            annotated_image = image.copy()
            for detection in results.detections:
                mp_drawing.draw_detection(annotated_image, detection, 
                                          bbox_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=7))
        
            plt.figure(figsize=(8,20))
            plt.subplot(1,2,1);plt.imshow(image)
            plt.subplot(1,2,2);plt.imshow(annotated_image)
            plt.show()