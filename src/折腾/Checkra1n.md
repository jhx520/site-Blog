---
layout: post
title: Checkra1n 越狱指南
slug: Checkra1n
date: 2020-02-11 20:34
status: publish
author: Anony
categories: 
  - 折腾
tags: 
  - iOS
  - 越狱
excerpt: 疑难解惑，不是教程！
---
### 起因

首先来说一下我的设备情况，18年9月买的 iPhone 8P，本来是准备留在 iOS 12.4 养老，但是由于去年买了耳机（AirPods Pro），所有功能起步适配 iOS 13.2，所以没办法，考虑再三，最终还是选择升级系统。

### 计划

- **原本：**<u>U盘 + macOS 10.14</u>
- **现在：**<u>Windows + 虚拟机</u>

### 准备

- **环境：**Windows

- **虚拟机：**VMware 15.5 Pro （已上传至云盘 [点击下载](https://pukobaggstuacnz-my.sharepoint.com/personal/jhx520_qqu_me/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fjhx520%5Fqqu%5Fme%2FDocuments%2FVMware%20MacOS%2Fvmware%2Dpro15%2Ezip)）

- **镜像：**ubuntu 18.03 （推荐使用网易开源镜像站 [点击下载](http://mirrors.163.com/ubuntu-releases/18.04/ubuntu-18.04.3-desktop-amd64.iso)）
- **越狱工具：**Checkra1n （[点击跳转](https://checkra.in/)）

### 疑难

- VMware 在装载系统时，**不能全屏显示**，不建议使用 VMware Tools，解决办法：

  ```shell
  sudo apt-get install open-vm-tools
  sudo apt-get install open-vm*
  reboot
  ```

- 密钥无法导入，出现 “ **gpgkeys: protocol `https' not supported** ” 错误，解决办法：

  ```shell
  sudo apt install gnupg-curl
  ```

- 执行 sudo apt-get update 时出现 ” **无法获得锁 /var/lib/apt/lists/lock - open （11: 资源暂时不可用）**“ 错误，解决办法：

  ```shell
  sudo rm /var/lib/apt/lists/lock
  ```

### 小结

其实两者并没有什么效率可言，纯属个人习惯，且不随身携带 U盘，所以还是喜欢直接进入 Windows，这样操作起来也方便些，截至写稿前，Checkra1n Win 并没有发布。