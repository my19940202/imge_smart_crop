import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_cut_positions(image_path, output_path):
    # 读取图片
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 统计垂直方向边缘像素分布
    vertical_distribution = np.sum(edges, axis=1)

    # 找到可以裁切的 y 轴位置
    threshold = np.max(vertical_distribution) * 0.9  # 自定义阈值
    cut_positions = np.where(vertical_distribution > threshold)[0]

    # 在原图上标记裁切线
    for y in cut_positions:
        cv2.line(img, (0, y), (img.shape[1], y), (0, 0, 255), 2)

    # 保存输出图片
    cv2.imwrite(output_path, img)

    # 显示结果
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.title("Edge Detection")
    plt.imshow(edges, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("Marked Image")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# 示例调用
input_image = "new.jpeg"  # 输入图片路径
output_image = "new-line-09.jpg"  # 输出图片路径
detect_cut_positions(input_image, output_image)

