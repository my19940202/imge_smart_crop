# 项目调研记录opencv代码
采用了opencv做图片裁剪处理

## ❌方案1: 采用opencv的边缘检测
边缘检测可以识别比较明显的边界，但是无法识别颜色相近的区域,示例如下
<table style="text-align:center">
    <thead>
        <tr>
        <td>原图</td><td>Canny裁剪</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <img src="./preview/edge_detection_origin.jpeg" width="200" />
            </td>
            <td>
                <img src="./preview/edge_detection_0.3.jpeg" width="200" />
            </td>
        </tr>
    </tbody>
</table>

## ✅方案2: 考虑使用opencv分析Y轴方向的颜色，如果是纯色就允许裁剪
- 实际业务中的图片，Y轴存在比较多的纯色区域和渐变色的区域 用来裁剪比较合适
- 实际裁剪的时候，采用双指定去移动判断最佳的裁剪区域
<table style="text-align:center">
    <thead>
        <tr>
        <td>原图</td><td>统计Y轴颜色变化方差</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <img src="./preview/car-origin.jpeg" width="200" />
            </td>
            <td>
                <img src="./preview/car-30.jpeg" width="200" />
            </td>
        </tr>
        <tr>
            <td>
                <img src="./preview/tooth-origin.jpeg" width="200" />
            </td>
            <td>
                <img src="./preview/tooth-color30.jpeg" width="200" />
            </td>
        </tr>
    </tbody>
</table>

