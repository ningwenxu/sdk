# 主要功能  
### 1.提供访问DSS的函数，上传pcd，获取访问的url<br>
### 2.目前写有两个函数:<br>
#### a.lidar_single_upload(),只用于接收单个pcd文件，并给出url，需要提供:
file:文件路径、Token:用于创建client、endpoint:数据平台上线环境,url_pre:访问前缀、storage_name:存储桶名称、asset_group:数据业务归属、is_small_datas：是否属于小文件。  
#### b.lidar_list_upload() 用于接受批量pcd文件，文件以列表传递。其他参数与上一个函数相同

