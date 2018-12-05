from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client

class FDFSStorage(Storage):
    """fast dfs文件存储类"""

    def _open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def _save(self, name, content):
        """保存文件时使用"""
        # name:你选择上传文件的名字
        # content:包含你上传文件内容的File对象

        # 创建一个Fdfs_client对象
        client = Fdfs_client('./utils/fdfs/client.conf')

        # 上传文件到fast dfs文件系统中
        res = client.upload_by_buffer(content.read())

        # res = 返回的字典
        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast DFS失败')