---
layout: post
cid: 168
title: Typecho-Plugin-DoubanBoard 发布
slug: 168
date: 2018/10/14 01:23:00
updated: 2019/10/12 17:22:58
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
excerpt: 在博客上展示你的豆瓣书单、豆瓣影单 & MORE！
---


之前我写过一篇文章，介绍如何把豆瓣读书和豆瓣电影的个人收藏数据拉取过来在博客上展示：[把豆瓣读书和电影收藏数据扒过来展示](https://blog.imalan.cn/archives/150/)。但是写代码的方式对大多数人来说还是不太友好，而且相当于需要自己搭建 API 服务，于是现在我把代码整合一下，并加上了单独插入某一书籍、电影的功能，制作成了这个插件：DoubanBoard。

## 介绍

豆瓣书单与豆瓣影单的抓取方法有所不同。书单有接口可以获取，影单没有，只能通过访问豆瓣的网页来解析。具体实现就不多说了。

示例页面见：[电影 - 熊猫小A的博客](https://blog.imalan.cn/movie) | [读书 - 熊猫小A的博客](https://blog.imalan.cn/book)

除此之外，也有单独展示某一部电影或书籍的功能，喜欢写影评和书评的博主可能会喜欢这个功能。示例：

**单部电影**

<div class="douban-single" data-type="movie" data-id="26685451" data-rating="8.6"></div>

**单部书籍**

<div class="douban-single" data-type="book" data-id="30226856" data-rating="8.3"></div>

理论上，也支持剧集，只要按照单部电影的方式添加就好：

<div class="douban-single" data-type="movie" data-id="1393859" data-rating="10"></div>

## 食用方式

去 GitHub 上下载或者 Clone 这个 repo：[Typecho-Plugin-DoubanBoard](https://github.com/AlanDecode/Typecho-Plugin-DoubanBoard)，**将解压后的文件夹改名为 DoubanBoard**，上传至站点插件目录启用，并在插件设置面板进行必要的设置。设置项有：

- 豆瓣 ID：你的豆瓣 ID，一般可以从你的个人主页的 URL 里找到。
- 每次加载的数量：从速度和节省流量的考虑，书单和影单不会一次全部加载。你可以填写每次加载的数量。不填默认为 10。
- 缓存过期时间：插件对数据做了本地缓存以提高访问速度，你可以在这里填写缓存过期时间，单位为秒。两次访问时间间隔超过该时间则会重新拉取数据，不填默认 24 小时。注意，不建议设置得过短，否则豆瓣可能判定你的 IP 存在异常流量。
- 是否加载 JQuery：如果你的主题没有引入则勾选它来引入，否则取消勾选。

**注意：要保证 `插件目录/cache` 这个文件夹可写！**

### 插入书单与影单

想读清单：

```
<div data-status="wish" class="douban-book-list doubanboard-list"></div>
```

已读清单：

```
<div data-status="read" class="douban-book-list doubanboard-list"></div>
```

在读清单：

```
<div data-status="reading" class="douban-book-list doubanboard-list"></div>
```

电影想看清单：

```
<div data-status="wish" class="douban-movie-list doubanboard-list"></div>
```

电影已看清单：

```
<div data-status="watched" class="douban-movie-list doubanboard-list"></div>
```

电影在看清单：

```
<div data-status="watching" class="douban-movie-list doubanboard-list"></div>
```

注意，在某些 Typecho 版本中你可能需要使用 `!!!` 来包裹住 HTML 代码。

### 插入单部电影、书籍

**插入单部电影**：

```
<div class="douban-single" data-type="movie" data-id="电影 ID" data-rating="你的评分"></div>
```

其中`电影 ID`可以在豆瓣电影页面的 URL 中找到。`你的评分`修改为你自己的评分，10 分制，可带小数。

**插入单部书籍**

```
<div class="douban-single" data-type="book" data-id="书籍 ID" data-rating="你的评分"></div>
```

其中`书籍 ID`可以在豆瓣书籍页面的 URL 中找到。`你的评分`修改为你自己的评分，10 分制，可带小数。

注意，在某些 Typecho 版本中你可能需要使用 `!!!` 来包裹住 HTML 代码。

Enjoy.

**如果本项目对你有所帮助，请考虑捐助我 ↓↓↓**