from setuptools import (setup,find_packages)

setup(
    # 包名
    name="Lidar_Upload",
    # 版本
    version="0.1",
    # github地址[我学习的样例地址]
    url='https://github.com/ningwenxu/lidar_upload.git',
    # 包的解释地址
    long_description=open('README.md', encoding='utf-8').read(),
    # 需要包含的子包列表
    packages=find_packages()
)