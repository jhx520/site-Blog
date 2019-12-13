---
layout: post
cid: 465
title: 查看 GitHub Release 下载量
slug: view-download-count-of-github-release
date: 2019/10/27 17:40:00
updated: 2019/10/27 18:07:57
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
  - LifeHack
excerpt: 少得可怜，令人伤心。
---


有时候也会好奇某个仓库到底被下载了多少次呢……所以写了个 PHP 脚本从 GitHub API 请求数据，然后输出到终端上，大概效果如下：

![][1]

使用方法：去 [AlanDecode/getDownloadInfo.php](https://gist.github.com/AlanDecode/29f3e5b876d9ea03b1dc5c2fba8ef808) 获取代码保存为 getDownloadInfo.php，并修改里面的 `$UserName` 和 `$RepoName` 两项为你感兴趣的值，然后在命令行中运行 `php getDownloadInfo.php` 即可。PHP 需要启用 curl 扩展。

受 API 限制，Source ​code 和直接下载仓库的无法统计，只能统计 Release 中自己添加的附件。看看 VOID 主题发布版的下载量吧：

![][2]

啊，还真是少得可怜啊……  


[1]: ./assets/1754349277.png
[2]: ./assets/4224242303.png