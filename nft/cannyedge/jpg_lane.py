import cv2
import pipeline

img = cv2.imread('puskas.jpg')

result = pipeline.run(img)

cv2.imshow('result', result)
cv2.waitKey(0)

cv2.imwrite('image.jpg', result)

cv2.destroyAllWindows()
