import cv2

cap = cv2.VideoCapture('test3.mp4')

# 재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("재생할 파일 넓이, 높이 : %d, %d" % (width, height))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output3.mp4', fourcc, 30.0, (int(width), int(height)))

while True:
    ok, img = cap.read()
    if not ok:
        print("저장 완료")
        break

     # 1) BGR -> GRAY 영상으로 색 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2) 이미지 내 노이즈를 완화시키기 위해 blur 효과 적용
    blur_img = cv2.GaussianBlur(gray_img, (7, 7), 0)

    # 3) 캐니 엣지 검출을 사용하여 엣지 영상 검출
    edge_img = cv2.Canny(blur_img, 70, 140)

    img = cv2.cvtColor(edge_img, cv2.COLOR_RGB2BGR)

    cv2.imshow('result', img)
    key = cv2.waitKey(1)  # -1

    out.write(img)
    if key == ord('x'):
        break
cap.release()