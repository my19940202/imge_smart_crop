# 基于OpenCV和NumPy的Python脚本，用于扫描图像中的纯色或渐变区域
import cv2
import numpy as np
import argparse

def is_solid_or_gradient_region(column, threshold):
    # 计算列的标准差
    std_dev = np.std(column)
    return std_dev < threshold

def find_closest_pair(arr):
    left = 0
    right = len(arr) - 1
    closest_pair = [None, None]
    closest_diff = float('inf')
    # 更新最接近宽高比3:4的差值,图片宽度800
    gap = 800 * 1.33

    while left < right:
        diff = arr[right] - arr[left]

        if abs(diff - gap) < closest_diff:
            closest_diff = abs(diff - gap)
            closest_pair = [arr[left], arr[right]]

        # 根据差值调整指针
        if diff < gap:
            left += 1
        else:
            right -= 1

    return closest_pair

def scan_image_for_solid_or_gradient(image_path, threshold):
    # 读取图像并转换为灰度图-减少颜色通道，降低计算复杂度
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    yList = []

    for y in range(height):
        # 提取当前y轴的列
        column = gray_image[y, :]

        # 检查当前列是否为纯色或渐变色区域
        if is_solid_or_gradient_region(column, threshold):
            # 在当前y轴画一条线
            # cv2.line(image, (0, y), (width, y), (0, 0, 0), 1)
            yList.append(y)

    bestRange = find_closest_pair(yList)
    print(image_path, bestRange)
    if bestRange[0] is not None and bestRange[1] is not None:
        # 裁剪部分灰色 提现出裁剪效果
        for y in range(height):
            if y > bestRange[1] or y < bestRange[0]:
                # 将整行像素设置为灰色
                # gray_value = [128, 128, 128]  # 灰色
                # image[y, :] = gray_value

                # 亮度减弱处理
                image[y, :] = (image[y, :] * 0.1).astype(np.uint8)

                # 反色处理
                # image[y, :] = 255 - image[y, :]  # 反色处理

        # cv2.line(image, (0, bestRange[0]), (width, bestRange[0]), (0, 255, 0), 1)
        # cv2.line(image, (0, bestRange[1]), (width, bestRange[1]), (0, 255, 0), 1)

    # 显示结果图像
    cv2.imwrite(image_path.replace('.', '-' + str(bestRange[1] - bestRange[0]) + '-range.'), image)

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='Scan an image for solid or gradient regions.')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    parser.add_argument('--threshold', type=float, default=10, help='Threshold for detecting solid/gradient regions')

    args = parser.parse_args()

    # 执行扫描
    scan_image_for_solid_or_gradient(args.image_path, args.threshold)
