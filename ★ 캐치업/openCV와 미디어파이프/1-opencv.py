####################################
## keyword: 이미지읽기모드, bgr2rgb
####################################
import cv2

# 오픈CV는 폴더명과 파일명이 영문이어야 함.
# 읽으면 무조건 array 읽어주는데, rgb가 아니라 bgr로 읽음
# cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE
# cv2.IMREAD_UNCHANGED : png에서 투명도가 있는 자료일떄 그 4채널을 모두 읽음

img=cv2.imread('b.png',cv2.IMREAD_COLOR) # rgb값으로 읽음, 0으로 지정해도 됨.
print(img)
cv2.imshow('test',img)    # bgr을 rgb로 알아서 변경해서 출력함.
inputKeyValue=cv2.waitKey(0)  # 사용자가 화면을 닫을때까지 열려있음, 함수 매개 변수로 넣는 키 입력 대기 시간은 ms 단위이고 0이면 무한대기이다.

# 키보드 a가 들어온다면
if inputKeyValue==ord('a'): 
    print('a키를 누르셨습니다. 종료하겠습니다')
    cv2.destroyWindow('color img') # 'color img'  창닫기
print(inputKeyValue)




##############################
## 만약에 matplotlib에서 출력하고자 한다면
## rgb로 변환해야함
##############################
import matplotlib.pyplot as plt
imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()


