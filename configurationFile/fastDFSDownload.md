# FastDFS
- [安装包下载](https://pan.baidu.com/s/1NkK7VbeNBrbTPUeTxcYD6A)
- [参考文档](https://blog.csdn.net/MissEel/article/details/80856194)
- [tracker.conf文件](./conf/tracker.conf)
- [storage.conf文件](./conf/storage.conf)
- [client.conf文件](./conf/client.conf)
- ### FastDFS下载安装
    1. #### 安装fastDFS依赖包
        1. 解压缩libfastcommon-master.zip  
        2. 进入到libfastcommon-master的目录中
        3. 执行 `sudo ./make.sh`
        4. 执行 `sudo ./make.sh install`
        
    2. #### 安装fastDFS
        1. 解压缩fastdfs-master.zip
        2. 进入到 fastdfs-master目录中
        3. 执行 `./make.sh`
        4. 执行 `sudo ./make.sh install`
    3. #### 配置跟踪服务器tracker [tracker conf文件](./conf/tracker.conf)
        1. `sudo cp /etc/fdfs/tracker.conf.sample /etc/fdfs/tracker.conf`
        2. 在/home/python/目录中创建目录 fastdfs/tracker      
        `mkdir –p /home/python/fastdfs/tracker`
        3. 编辑/etc/fdfs/tracker.conf配置文件    
        `sudo vim /etc/fdfs/tracker.conf`
        修改 
        `base_path=/home/python/fastdfs/tracker`
    4. #### 配置存储服务器storage [storage conf文件](./conf/storage.conf)
        1. `sudo cp /etc/fdfs/storage.conf.sample /etc/fdfs/storage.conf`
        2. 在/home/python/fastdfs/ 目录中创建目录 storage  
            `mkdir –p /home/python/fastdfs/storage`
        3. 编辑/etc/fdfs/storage.conf配置文件  sudo vim /etc/fdfs/storage.conf
        修改内容：
        `base_path=/home/python/fastdfs/storage`  
        `store_path0=/home/python/fastdfs/storage`  
        `tracker_server=自己ubuntu虚拟机的ip地址:22122`  
    5. #### 启动tracker和storage
        Trackerd服务  
        `sudo /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf start`  
        storge服务  
        `sudo /usr/bin/fdfs_storaged /etc/fdfs/storage.conf start`
    6. #### 测试是否安装成功 [client.conf文件](./conf/client.conf)
        1. `sudo cp /etc/fdfs/client.conf.sample /etc/fdfs/client.conf`
        2. 编辑/etc/fdfs/client.conf配置文件  
        `sudo vim /etc/fdfs/client.conf`  
        修改内容：  
        `base_path=/home/python/fastdfs/tracker`  
        `tracker_server=自己ubuntu虚拟机的ip地址:22122`
        3. 上传文件测试：  
        `fdfs_upload_file /etc/fdfs/client.conf 要上传的图片文件`  
        如果返回类似group1/M00/00/00/rBIK6VcaP0aARXXvAAHrUgHEviQ394.jpg的文件id则说明文件上传成功
