import cv2
from datetime import datetime

webcam = cv2.VideoCapture(0)  # 웹캠을 사용합니다.

if not webcam.isOpened():
    print('카메라를 찾을 수 없습니다.')
else:
    print('카메라 활성화 완료')

while webcam.isOpened():
    ret, frame = webcam.read()  # 웹캠에서 프레임을 읽어옵니다.

    if ret:
        # 프레임에 'Python'이라는 텍스트를 추가합니다.
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cv2.putText(frame, current_time, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Webcam', frame)  # 수정된 프레임을 화면에 표시합니다.
    else:
        break  # ret이 False인 경우 반복문을 종료합니다.

    # 'q' 키를 누르면 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 반복문을 빠져나오면 웹캠을 해제합니다.
webcam.release()
cv2.destroyAllWindows()  # 모든 창을 닫습니다.
