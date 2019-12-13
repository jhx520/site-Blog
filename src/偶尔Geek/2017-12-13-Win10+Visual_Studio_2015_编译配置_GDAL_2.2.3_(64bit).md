---
layout: post
cid: 67
title: Win10+Visual Studio 2015 编译配置 GDAL 2.2.3 (64bit)
slug: 67
date: 2017/12/13 20:51:00
updated: 2019/08/21 10:51:04
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
excerpt: 
---


这里介绍如何在 Win10 + VS2015 环境下编译并配置 64 位 GDAL 库。

## 从源代码编译 GDAL

首先下载 GDAL 源代码：[http://trac.osgeo.org/gdal/wiki/DownloadSource](http://trac.osgeo.org/gdal/wiki/DownloadSource)。下载后解压，得到源代码。

在源代码路径中找到 `nmake.opt` 文件，用文本编辑器打开，搜索 `GDAL_HOME` ，把后面的路径 `"C:\warmerda\bld"` 改为你希望最终存储 GDAL 库文件的目录，比如 `C:\GDAL` ，并在对应位置创建目录。那么在编译安装完成后将会将包含文件、库文件、可执行文件都提取到这个目录。

在开始菜单中打开 VS2015 x64 本机工具命令提示符，并 cd 到 GDAL 的源码目录，即包含了`makefile.vc` 的路径，这里假设是 `C:\GDALSOURCE` 。

```
cd C:\GDALSOURCE
```

依次执行以下命令：

```
nmake -f makefile.vc MSVC_VER=1900 WIN64=1
nmake /f makefile.vc install MSVC_VER=1900 WIN64=1
nmake /f makefile.vc devinstall MSVC_VER=1900 WIN64=1
```

待完成后，对应的文件将出现在 `GDAL_HOME` 指定的路径下，包含 `bin` 、`data` 、`html` 、`include` 、`lib` 这几个文件夹。

这里解释以下这几行命令都是什么意思：

* 第一行命令将编译 GDAL。
* 第二行命令将提取可执行文件和 data 文件到 `nmake.opt` 文件中 `BINDIR` 、 `DATADIR` 指定的路径下，如果没有特别设置，就是 `GDAL_HOME` 下的对应目录。
* 第三行命令将提取包含文件和库文件到 `nmake.opt` 文件中 `INCDIR` 、 `LIBDIR` 指定的路径下，如果没有特别设置，就是 `GDAL_HOME` 下的对应目录。
* 默认情况下编译生成的是 Release 版本，如果需要 Debug 版本的库，请在以上命令后面加上 `DEBUG=1` 。
* 另外 `WIN64=1` 指定是 64 位版本，`MSVC_VER=1900` 指定编译环境是 VS2015，即 `vc14` 。如果不声明这个参数，由于 VS2015 一些内部的改动，编译将会报错：

```
Creating library gdal_i.lib and object gdal_i.exp
odbccp32.lib(dllload.obj) : error LNK2019: unresolved external symbol _vsnwprintf_s referenced in function StringCchPrintfW
gdal201.dll : fatal error LNK1120: 1 unresolved externals
NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\amd64\link.EXE"' : return code '0x460' Stop.
```

以上内容参见 GDAL 官方说明：[http://trac.osgeo.org/gdal/wiki/BuildingOnWindows](http://trac.osgeo.org/gdal/wiki/BuildingOnWindows) 。

## 配置 VS2015

类似 OpenCV 的配置，打开 VS2015，新建新的空 Win32 控制台程序。在视图—其他窗口—属性管理器中选中`Debug | x64` ，双击打开 `Microsoft.Cpp.x64.user` ，在 VC++ 目录中的包含目录、库目录中分别添加上一步骤获得的目录，比如 `C:\GDAL\include` 、`C:\GDAL\lib` ，点击应用。在链接器-输出中添加附加依赖项 `gdal_i.lib` ，点击应用，然后点击确认保存。

## 测试

在上面新建的工程里添加源文件 `mian.cpp` ，键入代码：

```cpp
#include <iostream>
#include "gdal.h"
#include "gdal_priv.h"

using namespace std;

int main() {
	GDALDataset *p;
	GDALAllRegister();
	p = (GDALDataset*)GDALOpen("1.tif", GA_ReadOnly);
	if (p == NULL)
		cout << "Failed!"<<endl;
	else
		cout << "Success!"<<endl;
	return 0;
}
```

找一张`.tif` 格式的图片放在 `mian.cpp` 同一目录下，重命名为 `1.tif`，按 Ctrl+F5 编译并运行，如果配置没有问题控制台将输出 `Success!` 。如果提示“找不到 gdal202.dll”，是因为 GDAL 是动态编译的，运行需要对应的动态链接库。两种方法：

1. 去上面得到的 `bin` 目录下将 `gdal202.dll` 拷贝过来和 `main.cpp` 放在一起即可；
2. 将上面得到的 `bin` 目录的路径添加到系统环境变量 Path 中，重启电脑即可。

我更推荐第二种方式，这样以免以后每次都去拷贝 `gdal202.dll` ，一劳永逸。桌面右键此电脑-属性-高级系统设置-环境变量-系统变量，双击 Path 变量，新建，将 `bin` 目录的路径复制进去点击确定保存。重启计算机。



以上。