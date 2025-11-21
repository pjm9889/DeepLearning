##  좌표이동 https://diytube.tistory.com/21

import cv2
img_color=cv2.imread('a.png', cv2.IMREAD_COLOR)  

x, y = 200, 200
title = 'KeyBoard Control'
img=img_color.copy()

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력 대기, 8비트 마스크 처리
    print(key, chr(key))        # 키보드 입력 값, 문자 값 출력
    if key == ord('a'):
        x -= 10                 # a가 입력되면 왼쪽으로 이동
    
    elif key == ord('s'):
        y += 10                 # s가 입력되면 아래로 이동
    
    elif key == ord('w'):
        y -= 10                 # d가 입력되면 위로 이동
        
    elif key == ord('d'):
        x += 10                 # w가 입력되면 오른쪽으로 이동
    
    elif key == ord('q') or key == 27:
                 
        cv2.destroyWindow(title) # q이거나 esc이면 종료.
        break   
    cv2.moveWindow(title, x, y) # 새로운 좌표로 창 이동