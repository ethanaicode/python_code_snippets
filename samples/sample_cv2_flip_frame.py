import cv2

"""
目前测试这个方法是没有声音的
而且视频会非常大，并不推荐，可以使用 moviepy 实现
"""

# 打开视频文件
cap = cv2.VideoCapture('./data/input_video.mp4')

# 获取视频的基本信息
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 设置视频编码器和输出文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./data/output_video.mp4', fourcc, fps, (frame_width, frame_height))

# 读取视频的每一帧，进行处理
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 水平翻转帧
        flipped_frame = cv2.flip(frame, 1)
        # 写入翻转的帧到输出文件
        out.write(flipped_frame)
        # 显示帧（如果需要的话）
        # cv2.imshow('Flipped Frame', flipped_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
