---
layout: post
cid: 102
title: 春天=过敏，以及用 Apple Script 调整 Mac 屏幕亮度
slug: 102
date: 2018/03/30 21:38:00
updated: 2018/08/27 11:44:39
status: publish
author: 熊猫小A
categories: 
  - 摸鱼日常
tags: 
excerpt: 大概这就是闲得慌的人才会干的事吧~
---


都说北京四季不分明，每年都在夏天和冬天之间轮替，我说这是瞎扯。每年只要发现自己眼睛痒、鼻子堵、打喷嚏，我就知道不是春天就是秋天又到了。这几天被过敏折腾得不行，随时保持眼泪汪汪的状态，卫生纸消耗速度惊人，赶紧去医院看病开了些抗过敏的药才好转一点。

### 又来折腾 Hackintosh

去年末把笔记本从惠普 Probook 440 G3 换成了联想 R720，于是之前一直在用的黑苹果也木有了，新电脑没抽出时间来折腾它。前两天临时起意，就随便搜索了一下这个机型有没有成功的例子，找到了一个类似的：[【教程】联想拯救者R720 安装MacOS 10.12.6 双系统教程](http://tieba.baidu.com/p/5521219636?pv=1&red_tag=a1580648294) 。虽然帖子里的机型是 i5-7300 的版本，我的是 i7-7700HQ 的版本，据我估计差别不会太大，而且楼主封装的镜像和引导以及驱动**非常全面** ，弄得我顿时手痒起来。回头一看自己的固态，500G 就用了 200 多 G，闲着也是闲着，分了 100G 出来装 Hackintosh。

版本是 10.12.6，主要是一般来说，上一版本的驱动会更稳定一些，而且可以找的资料也多一点。过程很顺利，果然联想爆款一向装黑苹果都不难，回头写个过程记录当备忘。总之结果是：

* 核显 Intel HD Graphics 630，独立显卡无解。亮度调节 OK
* 有线网卡 OK，无线无解
* 声卡 OK（扬声器以及耳机）
* 电池状态显示 OK
* 蓝牙 OK，但没有 AirDrop 和 Handoff
* iMessage、iCloud、App Store 这些内置程序都正常。
* 睡眠一睡就死
* 触控板依然很垃圾（当然这是硬件的锅）

算是比较标准的黑苹果状态。就差无线网卡比较蛋疼，家里有一块 BCM94352Z，但不在手边，回头把无线网卡换一个试试能不能把 WiFi 修好。其实我装黑苹果也不是要做什么 iOS 开发啥的，就是很喜欢 macOS 的那种顺畅和人性化的感觉，外观设计和字体渲染也很棒，最最重要的还是 Mac 平台的一些很精致的独占应用。既然没钱买一台真 Mac，暂时就这么曲线救国吧~

### 用 Apple Script 调整 Mac 屏幕亮度

一个很烦人的点，跟黑苹果无关，就是 Mac 外接显示器时是没办法（方便地）在不合盖的情况下关闭内建显示器的。我平时主要是用外接显示器的，很少的情况下才会镜像显示器或者扩展显示器。这个问题可以用两种方法解决。

#### 糊弄电脑

说白了就是让电脑觉得已经盒盖了。方法就是拿一块小磁铁在笔记本 C 面试探，找到一个位置，当磁铁在这个位置时笔记本感应器接收到信号，觉得盖子合上了，于是关闭内建显示器。对我的联想 R720 而言，这个位置在左侧耳机孔附近。

这个方法的好处是可以真正关闭内建显示器；坏处就是必须有个磁铁一直放在那个位置。

#### 糊弄自己

原理就是把亮度开到最低，骗自己已经关闭了显示器……

虽然有点自欺欺人，但是并不是不能接受的做法。不过每次都要用功能键（何况 Hackintosh 很多时候功能键并不奏效）或者去偏好设置里调节多少有些不便，我找了个用 Apple Script 的方法。

首先打开系统内置的脚本编辑器，新建文稿，输入以下代码：

```
tell application "System Preferences"
	activate
	reveal anchor "displaysDisplayTab" of pane id "com.apple.preference.displays"
	tell application "System Events"
		set now to value of slider 1 of group 1 of tab group 1 of window "内建显示器" of process "System Preferences"
		if now > 0 then
			set value of slider 1 of group 1 of tab group 1 of window "内建显示器" of process "System Preferences" to 0
		else if now = 0 then
			set value of slider 1 of group 1 of tab group 1 of window "内建显示器" of process "System Preferences" to 1
		end if
	end tell
	quit
end tell
```

然后点击文件-导出，文件格式选择应用程序，勾选仅运行，然后起一个好听的名字，比如“嗯嗯这样的话我就可以随便开关屏幕了呢.app”，然后保存。打开系统偏好设置-安全性与隐私，隐私选项卡里，在“辅助功能”这一项里点“+”，添加上面保存的“嗯嗯这样的话我就可以随便开关屏幕了呢.app”。

以后点击“嗯嗯这样的话我就可以随便开关屏幕了呢.app”就会把内建显示器亮度调成 0，再点就会调成 1，再点就调成 0……

<div class="scode">注意：以上代码适用于中文系统，如果不是中文系统，那要把代码里的“内建显示器”换成对应的窗口名，比如（我猜）"Built-in Display" 啥的。</div>

如果借用 Alfred 这类可以运行 Apple Script 的软件，那么可以更加方便，设置触发短语直接运行上面的代码即可。置的亮度值可以自己设定，不一定非得是 0 和 1。这段代码可以给我们许多启示：代表着我们还能用 Apple Script 调整更多的系统偏好设置，exciting！
