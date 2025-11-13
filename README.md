# DeepLearning
## 강의진행에 요청사항폼 https://forms.gle/xf7ajtvgrGdn8K1Z9
## 구글드라이브 https://drive.google.com/drive/folders/1zdbT8ELimUixLKOXOhBnrhT1sZCm5E9g?usp=drive_link

- 이미지데이터 이해도 : https://forms.gle/3hqYQhdHuL5a2XRz6
- 딥러닝 이해도:  https://forms.gle/HY7dBBmbRLGbbgsk8
- 전이학습 이해도: https://forms.gle/sTGaJ1CsWu2BkkRv7


*11월13일(금) 정리되어야 할 개념
   - 인공신경망에서 나오는 용어만 알기
   - train, val, test의 역할, 과적합의 개념
   - pytorch에서는 transforms모듈을 통해, 전처리 및 증강을 함. 이때 훈련데이터를 증강한다면 val,test는 증강하지 않아야 하기 때문에
     train용, val과test의 transform을 별도로 두어야함.
   - 추론은 train환경과 같게 해야한다. (중요)
   - 모델을 저장하면 모델의 파라미터(w,b, feature map)값이 저장됨을 의미
      (모델 save 방법에 따라 파라미터값만 저장할수도 있고, 모델의 Layer층도 저장할수 있음)
   - 사전학습모델에서 마지막의 out 갯수만 변경하는걸 Feature extraction 방식이라함.
   - Fine-tuning은 모델층에서 일부층을 다시 미분에 (grad)에 참여함)

## 11월14일(금) 전이학습 실습 
  - 오전 9시~10시: 이해도 문제 풀이
  - 오전 10시~11시: 병충해 나뭇잎 자료에 대한 개요
  - 11시~12시: 데이터로더기 및 전이학습 코드로 돌리면서, 값들 확인하는 절차 & 개인작업
  - 1시~4시: 조별작업 (병충해 나뭇잎 또는 개인미션 , 추후bakpak@empas.com 으로 제줄하세요. _ 과정기록한 내용으로(블로그, git, ipynb의 코드설명 다 괜찮습니다. _ )
                                                - 날짜마감없음
