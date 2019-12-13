---
layout: post
cid: 13
title: 用 Workflow 下载网易云音乐 MV
slug: 13
date: 2017/01/19 20:03:00
updated: 2018/09/17 20:02:55
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
excerpt: 
---


网易云音乐平台上有许多不错的音乐 MV，有时候我会想把它们下载下来永久保存，毕竟不知道什么时候就看不到了……这里介绍用 Workflow 实现的方法。


Workflow 链接：[下载网易云音乐 MV](https://workflow.is/workflows/6ae21db094af4d108080dfea674f3fc1)

## 使用的 API

针对 MV，网易云音乐有如下 API（抓包得到的，似乎并不是开放 API）

完整请求 URI：

`GET [http://music.163.com/api/mv/detail?id=ID&type=mp4](http://music.163.com/api/mv/detail?id=ID&type=mp4)`

Header 部分：

`Cookie: appver=1.5.0.75771`

`Referer: [http://music.163.com/](http://music.163.com/)`

## 制作 Workflow

### 获取 MV ID

这部分类似我之前[一篇文章](https://sspai.com/36548)里叙述的过程，配合动作 Match Text 使用简单的正则表达式`\d{4,11}`，并取第一个结果即可。

### 调用 API 获得返回结果

使用 Workflow 内置 Get Contents of URL 动作，Method 就是 GET。但是这里要注意， Headers 里要填上对应的 key 和 value。URL 中的 ID 就是上一步里得到的 MV ID。

![006tLtW4jw1fbvxa83iamj315y112dog.jpg](./assets/5cc2bdf8c824f.jpg)

### 解析返回结果

在上一步的末尾接上一个 Quick Look，可以看出返回的是 JSON 格式的数据块。格式如下：

```
{...    "data": {
    "brs": {
      "720": "http:\/\/v4.music.126.net\/20170119235408\/f3b543ad1bcf39375b34ecabb31ab4f5\/web\/cloudmusic\/ICQkICIgMSFhISA0YDAxMQ==\/mv\/505949\/6200d4cd93ccabb858b11dca70a8fed4.mp4",
      ...
    	},
    ...}
... } 

```

我们想要的视频真实 URL 就包含在 data 下的 brs 里，我们可以使用 Get Dictionary Value 取得这个字段。brs 包含了多个 key 和 value，前面的 "720" 就是指视频的清晰度，后面的 http:\/\/... 就是对应清晰度的视频 URL，但是包含了大量的转义字符 \，用 Replace Text 把这些转义字符去掉就好。为了能够选择清晰度，在获得了 brs 字段之后，可以使用 Get Dictionary Value 里的 Get All Keys 来取得里面提供的所有不同清晰度，用 Choose from List 让用户自行选择，然后从 brs 字段中匹配到对应的 value ，并加以处理，获得真实的视频地址。

### 下载视频

这就不多说了，Get Contents of URL 即可。

## 结语

说点别的。最近在 Twitter 上看到一个玩笑：什么时候能发一篇《如何用 Workflow 高效记录浪费在这玩意儿上的时间》。也有人觉得 Workflow 只是另一个意义上的游戏罢了，制作 Workflow 并获得成就感。提高的那一点效率所节省的时间和学习使用它折腾它用的时间相比是微不足道的。其实我部分同意这个说法。我也不否认我多数时间制作 Workflow 也只是为了好玩。毕竟做一个「快速打开剪贴板链接」的 Workflow，能为我的生活带来多大改善？很有限。

用 Workflow 优化一个本来就有的流程是它的一种用法，但在某些场景下，Workflow 能做的不仅是「提高效率」，它能**做到本来在手机上做不到的事**。我很欣赏 Apple 提出的 “There is an app for that”，但是我很清楚这是不可能实现的美好梦想。这就是 Workflow 的用武之地，在开放的网络世界里配合开放 API，提供定制自动化流程的可能性，Workflow 不是一个吞噬时间的机器，而是一台用来创造的的机床。