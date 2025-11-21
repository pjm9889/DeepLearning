import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection,\
    mp_pose.Pose(
      min_detection_confidence = 0.5,
      min_tracking_confidence = 0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # result = image에서 얼굴을 인식한 bbox + point 계산
    result1 = face_detection.process(image)
    result2 = pose.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    mp_drawing.draw_landmarks(
        image,
        result2.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    # detection 내부에 bbox 좌표와 point 들의 좌표값이 x,y, score로 설정되어 있음
    if result1.detections:
      for detection in result1.detections:
        mp_drawing.draw_detection(image, detection)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break
