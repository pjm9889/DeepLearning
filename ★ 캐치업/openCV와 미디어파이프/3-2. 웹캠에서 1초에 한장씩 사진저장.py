import cv2
import os
from datetime import datetime
import time

# 저장할 폴더와 파일 이름 초기화
output_folder = 'face'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 변수 초기화
count = 1  # 파일 번호 초기화
start_time = time.time()  # 시작 시간 초기화

# 웹캠 열기
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print('카메라를 찾을 수 없습니다.')
else:
    print('카메라 활성화 완료')

while webcam.isOpened():
    ret, frame = webcam.read()  # 웹캠에서 프레임 읽기

    if not ret:
        break

    # 현재 시간과 경과 시간 계산
    current_time = time.time()
    elapsed_time = current_time - start_time

    # 1초에 한 번씩 사진을 저장
    if elapsed_time >= 1.0:
        # 파일 이름 설정
        filename = os.path.join(output_folder, f'face-{count:02d}.jpg')
        
        # 사진 저장
        cv2.imwrite(filename, frame)
        print(f'{filename} 저장 완료')

        # 다음 파일 번호 증가 및 시작 시간 업데이트
        count += 1
        start_time = time.time()

    cv2.imshow('Webcam', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 정리 작업
webcam.release()
cv2.destroyAllWindows()
