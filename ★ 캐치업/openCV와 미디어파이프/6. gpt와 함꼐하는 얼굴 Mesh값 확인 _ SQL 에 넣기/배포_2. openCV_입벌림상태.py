#####################################
## 미디어파이프 mesh에서 13,14번의 y값의 차이를 화면상단에 출력하는 웹캠 프로그램
#####################################
import cv2
import mediapipe as mp

# MediaPipe와 OpenCV 객체 초기화
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# 얼굴 메쉬 모델 초기화
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지 전처리
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # 랜드마크를 그리기
            for landmark in landmarks.landmark:
                h, w, _ = frame.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            
            # 랜드마크 13번과 14번의 y값 추출
            landmark_13 = landmarks.landmark[13]
            landmark_14 = landmarks.landmark[14]
            y_diff = landmark_14.y - landmark_13.y

            # y값 차이를 화면에 출력
            cv2.putText(frame, f'Y difference (13-14): {y_diff:.3f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 화면에 이미지 출력
    cv2.imshow('MediaPipe Face Mesh', frame)

    # 'q' 키를 눌러 프로그램 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
