import cv2

# 加载预训练的人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取图片
img = cv2.imread('face.jpg')

# 将图片转为灰度图，这是因为opencv的人脸检测需要灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 打印出每张人脸的坐标
for (x, y, w, h) in faces:
    print(f"Face found at x={x}, y={y}, width={w}, height={h}")

# 在原图上画出人脸的矩形框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示图片，按任意键关闭窗口
cv2.imwrite('new_face.jpg', img)
