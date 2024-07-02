import os
import requests

def download_images(urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            
            # Extract the image name from the URL
            image_name = os.path.basename(url)
            image_path = os.path.join(save_dir, image_name)
            
            with open(image_path, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded {url} to {image_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")

# 读取json文件，获取json数据
import json
with open('./send_request/static/ai_list.json', 'r') as file:
    image_urls_json_data = json.load(file)

# 处理json数据，获取图片url
image_urls = []
for urls in image_urls_json_data['ai_list']:
    # 首先把urls['img']的https换成http
    urls['img'] = urls['img'].replace('https', 'http')
    # 读取图片url
    image_urls.append(urls['img'])

# 保存路径
save_directory = './downloads/ai_images/'

# 下载图片
download_images(image_urls, save_directory)
