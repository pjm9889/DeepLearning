#################################
### ROI: 관심영역으로, 이미지의 높이,너비의 일정부분을 지정하는것을 의미함
##################################

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('a.png',cv2.IMREAD_COLOR)   # rgb 3채널로 읽음
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    # plt.imshow로 보기 위하여서 bgr를 rgb로 변환

plt.rcParams['font.family'] ='Malgun Gothic'  #한글깨짐해결
plt.rcParams['axes.unicode_minus'] =False  # 마이너스 기호 깨짐 방지

plt.figure(figsize=(10,3))
plt.subplot(1,4,1)
plt.imshow(img)
plt.title('원본이미지')

plt.subplot(1,4,2)
roi=img[0:100, 100:200]  # 높이0~100, 너비위치 100:200
plt.imshow(roi)
plt.title('행(0:100), 열(100:200)')

plt.subplot(1,4,3)
img[0:100, 100:200]=255
plt.imshow(img)
plt.title('행:0~100, 열:100~200은 흰색으로')


plt.subplot(1,4,4)
roi=img[300:, 150:]
plt.imshow(roi)
plt.title('행(300이후), 열(150이후)')
plt.show()