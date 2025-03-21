import cv2 as cv
import numpy as np

img_path = input("변환할 파일명을 입력하세요: ")
img = cv.imread("input/" + img_path)

levels = 8
div = 256 // levels

def quantize_color(value):
    return (value // div) * div + div // 2

quantized_img = np.zeros_like(img)
for i in range(3):
    quantized_img[:, :, i] = quantize_color(img[:, :, i])

gray = cv.cvtColor(quantized_img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

edges_thick = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 12
)
edges_thin = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 10
)
combined_edges = cv.bitwise_and(edges_thick, edges_thin)

cartoon = cv.bitwise_and(quantized_img, quantized_img, mask=combined_edges)

# 원본 이미지와 변환된 이미지 합성
combined_image = np.hstack((img, cartoon))
cv.imshow("Original | Cartoon", combined_image)

output_path = "output/cartoon_" + img_path  # 저장할 파일명 설정
cv.imwrite(output_path, cartoon)  # 이미지 저장
print(f"이미지가 '{'cartoon_' + img_path}'로 저장되었습니다.")

cv.waitKey(0)
cv.destroyAllWindows()