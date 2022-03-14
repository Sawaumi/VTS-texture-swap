#VtextureSwap

用于一键切换刷新live2d模型纹理集的vts插件

##使用说明：

###安装运行库<br/>
写给不熟悉python脚本的朋友：<br/>
请先运行运行库安装脚本，如遇网络问题，请使用镜像源安装。<br/>

###模型设置<br/>
textureSwap.exp3.json需要放置在模型motion目录下，在vts中绑定按键事件（绑定的键位将成为切换贴图所用的快捷键），并设置“0.1秒后关闭”。<br/>

目标模型的VTS按键列表中需要有一项名为“ReloadModelTexture”的按键事件，事件动作为重载模型材质，可不设置快捷键。<br/>

请确保目标模型的纹理集文件夹内已有原始贴图与替换贴图，其名称默认为texture_00.png与texture_00_swap.png，可以在example.py中更改。<br/>

###插件设置<br/>
当前测试版本需要您进入example.py中填写贴图文件夹的路径。
需要填写的内容与部分已注释在example.py中。
如果您不熟悉编辑方法，可以更改后缀名.py至.txt，使用txt编辑器编辑。编辑好后改回.py后缀名。<br/>

###一切就绪？<br/>
在启动VtubeStudio（VTS）后，双击 启动插件.bat 启动本插件。
VTS将弹出是否接受插件连接的对话框，请选择“接受”。<br/>

详情摸了就写这些<br/>
联系作者：带牛角包去公交车站等蒜头鹦鹉来吃，或，sawaumi@foxmail.com
