## 初始化git
git config --global user.name "<用户名>"
git config --global user.email "<电子邮件>"

## 彩色显示
git config --global color.ui auto


## 当前目录创建本地git数据库
git init

## 在目标目录创建本地git数据库
mkdir <目录>
cd <目录>
git init

## 确认工作树和索引的状态
git status

## 将文件或目录加入到索引
git add <file>..

## 将从索引中删除文件或目录
git rm <file>..

## 指定参数「.」，可以把当前目录下所有的文件加入到索引
git add .

## 提交文件
git commit -m "<索引备注>"

## 查看日志
git log

## 连接你的仓库到某个远程服务器（github）上
git remote add origin https://github.com/<your_user_name>/<repository.git>

## 推送改动
git push origin master
可以把 master 换成你想要推送的任何分支

## 分支
分支是用来将特性开发绝缘开来的。在你创建仓库的时候，master 是“默认的”分支。在其他分支上进行开发，完成后再将它们合并到主分支上。

## 创建一个叫做“feature_x”的分支，并切换过去：
git checkout -b feature_x
切换回主分支：
git checkout master
再把新建的分支删掉：
git branch -d feature_x
除非你将分支推送到远端仓库，不然该分支就是 不为他人所见的：
git push origin <branch>
