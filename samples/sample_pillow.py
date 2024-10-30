from PIL import Image

def get_image_info(image_path):
    with Image.open(image_path) as img:
        info = {
            "format": img.format,
            "mode": img.mode,
            "size": img.size,
            "info": img.info,
            "frames": []
        }

        # 检查是否有多个帧
        try:
            while True:
                info["frames"].append({
                    "frame_number": img.tell(),
                    "size": img.size,
                    "mode": img.mode,
                    "info": img.info
                })
                img.seek(img.tell() + 1)
        except EOFError:
            pass  # 已到达最后一帧c

        return info

# 读取两张ICO图像的详细信息
image1_path = './assets/images/doubao.ico'
image2_path = './assets/images/uitab.ico'

image1_info = get_image_info(image1_path)
image2_info = get_image_info(image2_path)

# 打印图像信息
print("Image 1 Info:")
for key, value in image1_info.items():
    print(f"{key}: {value}")

print("\nImage 2 Info:")
for key, value in image2_info.items():
    print(f"{key}: {value}")
