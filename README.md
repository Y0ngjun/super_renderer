# super_renderer
super useful renderer using OpenCV

## how to rendering
1. put the file path.
2. rendering img is created.

## screen shots
Original  
![Image](https://github.com/user-attachments/assets/193e6e74-8cdf-4029-8856-20427868413b)  
Cartoon  
![Image](https://github.com/user-attachments/assets/3446342d-237e-492f-a831-be69c3abe525)  
Original  
![Image](https://github.com/user-attachments/assets/601d30ac-8118-4078-b7ea-551c985c7bf9)  
Cartoon  
![Image](https://github.com/user-attachments/assets/e53b4672-dcf2-4f73-922c-cb8f2f3b847f)  
Original  
![Image](https://github.com/user-attachments/assets/1a3fbd53-55fa-41dc-b563-81522833032d)  
Cartoon  
![Image](https://github.com/user-attachments/assets/66b389db-3030-40fc-b4a6-d32ab98c4430)  
Original  
![Image](https://github.com/user-attachments/assets/85b1cf72-f802-464d-a20e-30d66836bae0)  
Cartoon  
![Image](https://github.com/user-attachments/assets/93136bf7-d0f8-4f88-a233-273c6a06e248)  
## limit
2번과 4번 예시는 만화 같은 느낌이 잘 표현되었다. 나는 색을 양자화하는 알고리즘을 사용하였는데 이 때 색의 조합이 잘 양자화 되어 만화같은 느낌이 더욱 살아나게 되었다.  
하지만 1번의 경우 색의 양자화 결과가 조화롭지 못했고 그림이 세부적인 요소가 많아서 블러 과정에서 이러한 요소들이 조금 뭉게지게 되어 만화같은 느낌이 약하게 표현되었다.
## algorithm
나의 알고리즘은 다음의 과정을 따른다.  
1. 이미지를 입력받는다.
2. 색을 양자화 한다.
3. 그레이 이미지로 변환하여 노이즈를 제거한다.
4. 그레이 이미지로부터 외곽선을 추출한다. 이때 굵은 외곽선과 얇은 외곽선을 각각 추출한다.
5. 양자화된 색깔 이미지와 외곽선을 합성하여 출력한다.

카툰느낌을 위해 색을 양자화 하기 때문에 무지개 처럼 색깔이 매우 다양하거나 광원이 강한 경우 잘 표현되지 않는다. 또한 데이터에 따라 다르지만 외곽선을 2번 나눠서 추출함에도 불구하고 외곽선이 매우 복잡한 이미지의 경우 정확한 외곽선을 추출하지 못한다.