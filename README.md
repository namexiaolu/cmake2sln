# cmake2sln
## 介绍
在windows上用cmake编译开源项目的时候，编译成的sln只能在自己电脑运行
如果将该sln文件目录分享给别人，别人无法使用。
因为sln中充满了各种绝对路径。
本脚本就是将这些绝对路径改为相对路径。
## 使用方法Cancel changes
先用cmake正常编译，
然后把py中的路径修改一下。执行即可。
