# yysScript
基于物体检测识别的自动点击脚本，python开发，不仅仅能用到阴阳师，可以用到一切需要按照标记点击的游戏。封号不负责啊。

### 如何安装

确保有anaconda的环境。

- 新建环境并启动

```shell
conda create -name yys python=3.8
conda activate yys
```

- 安装依赖

此过程可能很慢，国内的同学自行寻找镜像代理

```shell
pip install -r requirements.txt
```

### 如何使用

自己将想要图片放到`picture`文件下，确保寻找的到。

重写`YYS`类下的`script`方法。构建自己的脚本模板。(当前默认的脚本是yys五周年活动本)。

最后执行`YYS`下的`run`方法，开始脚本。

脚本内有很多细节参数请查看代码。另外`drawPictureWhenFound`函数可以进行一张图片是否找的到目标并画出目标位置，可以用来测试这个好不好用。

配合使用向日葵，远程操控电脑更加舒服。

**效果图:**

![](https://pic.imgdb.cn/item/61552d772ab3f51d91460357.png)



