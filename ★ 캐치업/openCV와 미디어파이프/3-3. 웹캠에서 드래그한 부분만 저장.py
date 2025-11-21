import cv2

# 변수 초기화
drawing = False  # 마우스가 클릭된 상태 확인
start_x, start_y = -1, -1  # 시작 좌표

# 마우스 콜백 함수
def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(frame, (start_x, start_y), (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(frame, (start_x, start_y), (x, y), (0, 255, 0), 2)
        # 선택한 영역을 파일로 저장
        roi = frame[min(start_y, y):max(start_y, y), min(start_x, x):max(start_x, x)]
        cv2.imwrite('a.jpg', roi)
        print('a.jpg로 저장 완료')

# 웹캠 열기
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print('카메라를 찾을 수 없습니다.')
else:
    print('카메라 활성화 완료')

cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', draw_rectangle)

while webcam.isOpened():
    ret, frame = webcam.read()  # 웹캠에서 프레임 읽기

    if not ret:
        break

    cv2.imshow('Webcam', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 정리 작업
webcam.release()
cv2.destroyAllWindows()
