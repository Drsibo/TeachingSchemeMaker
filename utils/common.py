import os
import csv
import shutil
import re
import logging
from datetime import datetime

# 定义常量
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# 定义通用函数
def create_dir_if_not_exists(dir_path):
    """如果目录不存在，则创建目录"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False

def get_files_in_dir(dir_path, extensions=None):
    """获取目录中指定扩展名的文件列表"""
    files = []
    for file in os.listdir(dir_path):
        if extensions is None or file.split('.')[-1].lower() in extensions:
            files.append(os.path.join(dir_path, file))
    return files

def copy_file(src_path, dst_path):
    """复制文件"""
    try:
        shutil.copy2(src_path, dst_path)
        return True
    except Exception as e:
        logging.error(f"复制文件出错: {e}")
        return False

def sanitize_filename(filename):
    """移除文件名中的非法字符，并限制文件名长度"""
    valid_filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
    valid_filename = valid_filename[:255]
    return valid_filename

def read_csv_file(file_path, encodings_to_try=None):
    """尝试用不同的编码读取 CSV 文件"""
    if encodings_to_try is None:
        encodings_to_try = ['utf-8', 'gbk', 'gb18030']
    
    data = None
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as csvfile:
                csvreader = csv.reader(csvfile)
                data = list(csvreader)
            logging.info(f"成功使用编码 {encoding} 读取文件: {file_path}")
            break
        except UnicodeDecodeError:
            continue
    
    if data is None:
        logging.error(f"无法读取文件 {file_path}，尝试了所有编码均失败")
    
    return data