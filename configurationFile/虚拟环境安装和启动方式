# 虚拟环境
[virtualenv官方文档](https://pypi.org/project/virtualenv/)  
 
安装同一个包的不同版本，后安装的包会把原来安装的包覆盖掉。这样，如同一台机器上两个项目依赖于相同包的不同版本，则会导致一些项目运行失败。
解决的方案就是：虚拟环境* 

__虚拟环境是真实python环境的复制版本。__
  
- ### 安装虚拟环境的命令
    1. 安装虚拟环境  
        `sudo pip install virtualenv`
        
    2. 安装虚拟环境扩展包  
        `sudo pip install virtualenvwrapper`
        
    3. 编辑家目录下面的`.bashrc`文件,添加下面两行  
        ```
        export WORKON_HOME=$HOME/.virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh
        ```
    4. 使用 `source .bashrc` 使其生效
- ### 安装中可能遇到的错误
    ```
    /usr/bin/python: No module named virtualenvwrapper
    ```
    错误原因：Ubuntu安装了2.7和3.x两个版本的python,在安装时使用的是`sudo pip3 install virtualenvwrapper`
在运行的时候默认使用的是python2.x,但在python2.x中不存在对应的模块  
    解决方法：在`.bashrc`文件里面加入如下命令即可
    ```
    VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    ----
    
    VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    ```
- ### virtualenv操作命令
    ```
    创建虚拟环境命令:
        mkvirtualenv 虚拟环境名
    
    创建Python3虚拟环境:
        mkvirtualenv -p python3 虚拟环境名
       
    进入虚拟环境工作:
        workon 虚拟环境名
        
    查看机器上有多少个虚拟环境：
        workon
        
    退出虚拟环境：
        deactivate
        
    删除虚拟环境：
        rmvirtualenv 虚拟环境名
    ```