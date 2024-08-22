import os
import json
import sqlite3

def ensure_directory(path):
    """确保目录存在，如果不存在，则创建它。"""
    if not os.path.exists(path):
        os.makedirs(path)

def manage_runtime_cache(runtime_dir):
    """处理运行时缓存目录的创建和写入操作。"""
    ensure_directory(runtime_dir)
    cache_file = os.path.join(runtime_dir, 'cache.txt')
    with open(cache_file, 'w') as f:
        f.write('Cache data')
    print(f'Cache written to {cache_file}')

def setup_database(data_dir):
    """检查数据库存在，不存在则创建，并执行一个简单的数据库操作。"""
    ensure_directory(data_dir)
    db_path = os.path.join(data_dir, 'app.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value TEXT)')
    cursor.execute('INSERT INTO test (value) VALUES ("Hello, World!")')
    conn.commit()
    print(f'Database set up at {db_path}')
    cursor.execute('SELECT * FROM test')
    print('Data from database:', cursor.fetchall())
    cursor.close()
    conn.close()

def read_config(config_path):
    """读取配置文件。"""
    with open(config_path, 'r') as f:
        config = json.load(f)
    print(f'Config read from {config_path}:', json.dumps(config, indent=2))

def read_images(banner_path):
    """读取图像文件。"""
    with open(banner_path, 'rb') as f:
        data = f.read()
    print(f'Image read from {banner_path}: {len(data)} bytes')

def main():
    # 运行时目录
    runtime_dir = 'runtime'
    manage_runtime_cache(runtime_dir)

    # 数据库目录
    data_dir = 'data'
    setup_database(data_dir)

    # 配置文件路径
    config_path = 'app/config/settings.json'
    read_config(config_path)

    # 资源文件路径
    banner_path = 'app/sources/images/python.png'
    read_images(banner_path)

if __name__ == '__main__':
    print(os.getenv('APPDATA'))
    # main()
