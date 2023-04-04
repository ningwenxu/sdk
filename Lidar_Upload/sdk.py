import os
from pymdi import pymdi

def lidar_list_upload(files:list,Token:str,endpoint:str,url_pre:str,storage_name:str,asset_group:str,type:str,is_small_datas):

    client=pymdi.Client(token=Token,endpoint=endpoint)
    if is_small_datas:
        ids=client.upload(files,storage_name=storage_name,asset_group=asset_group)
    else:
        ids=list()
        for file in files:
            with open(file,"rb") as f:
                id=client.async_upload(f,type,storage_name=storage_name,asset_group=asset_group)
                ids.append(id)

    return [url_pre+id for id in ids]
def lidar_single_upload(file:str,Token:str,endpoint:str,url_pre:str,storage_name:str,asset_group:str,is_small_datas):
    client = pymdi.Client(token=Token, endpoint=endpoint)
    md5=client.upload([file],storage_name=storage_name,asset_group=asset_group,is_small_datas=is_small_datas)
    return url_pre+md5[0]
url=lidar_single_upload(r"C:\Users\nio.ning\Downloads\test.pcd","3b9d9284-53c5-4503-aafc-851b7202b7ff",
                 "http://data.cla-dev.mmtdev.com",
             "https://cla.momenta.works/cdi/data/","cla-mdi-test-obs",
"CDI",True)
