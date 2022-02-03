import cv2
import pipeline

# img = cv2.imread('./test_images/solidWhiteRight.jpg')
#
# result = pipeline.run(img)
#
# cv2.imshow('result', result)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

# 동영상 테스트
cap = cv2.VideoCapture('./test.mp4')

while True:
    ok, frame = cap.read()
    if not ok:
        break

    result = pipeline.run(frame)

    cv2.imshow('result', result)
    key = cv2.waitKey(1)  # -1
    if key == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

