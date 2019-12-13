---
layout: post
cid: 261
title: Typecho 搜索增强：ExSearch
slug: 261
date: 2019/02/19 20:30:00
updated: 2019/11/01 23:38:11
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
  - 前端
excerpt: 🔍 为 Typecho 带来实时搜索体验。
---


Typecho 中没有单独的搜索页，绝大多数主题的所谓「搜索页」只是为搜索框单独写了一个样式，具体的搜索还是靠页面跳转。我对 Typecho 的搜索从来没有满意过，因此这次我想办法将其增强。

------

> 🔍 为 Typecho 带来实时搜索体验

项目地址：[ExSearch](https://github.com/AlanDecode/Typecho-Plugin-ExSearch)，使用方法见：[README.md](https://github.com/AlanDecode/Typecho-Plugin-ExSearch/blob/master/README.md)。

对于 [VOID](https://blog.imalan.cn/archives/247/) 主题，只需要下载启用插件，并建立缓存即可,主题已针对插件做了适配。

我需要为 Typecho 添加搜索实时响应、高亮与预览功能。[泽泽](https://qqdie.com/)的搜索插件通过 hack Typecho 的内部方法实现了高亮与过滤功能，但是仍然不能实现实时响应。其实也能理解，如果跟随输入实时响应的话，数据库的压力大大增加，而且网络压力也大大增加。必须另辟蹊径。

我在[为什么每个人都应该有自己的 Wiki](https://blog.imalan.cn/archives/108/)中提到自己启用了 [Wikitten](https://github.com/zthxxx/hexo-theme-Wikitten) 这个 Hexo 主题作为自己的 Wiki 站点主题。其中很重要的一个原因就是它舒服到无以复加的搜索体验。Hexo 这样无后端的博客为我提供了新的思路：将内容静态化，使搜索在前端进行。这样不仅降低了数据库压力，节省了网络请求数，同时也不用与 Typecho 的内部方法作斗争。唯一的缺点是对内容过多的站点来说需要传输一定数量的内容到前端，但这通过缓存静态化与前端长缓存也能缓解。

最终的结果便是这个插件。

**如果这个项目对你有所帮助，请考虑向我我捐助 ↓↓↓**