---
layout: post
title: Maverick - Go My Own Way.
slug: blog-now-powered-by-maverick
date: 2019-12-13 11:27
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
  - 博客
  - Maverick
excerpt: 关于 Maverick 及其设计思想的一些分享。
---

首先是在少数派上写一些折腾经验，然后是自己基于 WordPress、Typecho 建站，我在各种网络平台上涂鸦也快三年了。这期间尝试了许多写作、建站工具，深感该领域百花齐放，令人眼花缭乱。很长的一段时间里，我沉浸于给博客程序写主题写插件、使用诸如 CDN 等方式优化网站速度、研究 SEO 玄学，不亦乐乎。

但终究有些厌倦了。Typecho 这类动态博客程序固然方便，然而自己管理一个服务器确实是负担，而且对图片、内容的管理不甚自由，一旦需要迁移就是噩梦一场；若只是在第三方平台上发表东西，就总觉得互联网上少了属于自己的一亩三分地。

因此我曾几次把目光转向静态博客。诸如 Hexo、Jekyll 这类静态博客生成器让用户在本地编写 Markdown 文本，再由生成器完成从原始文件到博客网页的转换。某种程度上，这类程序让写作者从维护网站的繁琐中解脱出来，而专注创作本身。MWeb、Gridea 作为博客写作工具时也属于此类。

然而实践下来，仍然有两个问题没能得到解决：

1. 博客源文件的管理问题。想要达到真正的内容与展示分离，就不应该限制源文件的存储方式。现在的生成器要么要求把内容存储到自己的库中，要么要求放在生成器目录下的特定位置，某些甚至对目录结构都有要求。这并不是我想要的；
2. 图片等静态资源的处理问题。Markdown 对图片的处理一直都是痛点。我不希望把图片放在任何第三方图床，且不提上传图片-获得外链-插入外链这个过程多么不便，远程图床还有随时跑路的风险；而现在的生成器又不能很好地处理本地图片，至少处理起来并不优雅。

Alan Key 的一句名言，被 Steve Jobs 引用后众人皆知：

> People who are really serious about software should make their own hardware.

拿来活用，则「任何认真对待博客的人都应该自己写博客系统」。这话说起来固然偏执，但确实为吹毛求疵的人指了一条明路。既然现在的轮子都不满意，那就应该造自己的轮子。本着学习与探索的目的，我使用 Python 自己写了一个静态博客生成器，取名 **Maverick**，开源于 GitHub。它现在正驱动着我的[个人博客](https://blog.imalan.cn/)与我的[个人 Wiki](https://wiki.imalan.cn/)。

![](./assets/Maverick-Banner-1.png)

[**项目主页**](https://github.com/AlanDecode/Maverick) | [**个人博客**](https://blog.imalan.cn/) | [**演示站点**](https://alandecode.github.io/Maverick/) | **欢迎反馈与Star**

现在可以说说 Maverick 本身。大致上，它与 Hexo 等相似，都是通过解析 Markdown 文件生成网页。不过我在设计它时考虑到了上文所述的系列问题，并做了针对性的改进。

首先是 Maverick 对源文件的处理。Maverick **不限制**源文件的存储位置，你可以把文章目录放在电脑上的任何路径下，例如 Dropbox、iCloud Drive，以便备份、同步、版本管理，以及在任何设备上用任何编辑器写作。Maverick 也**不限制**源文件的组织结构，你可以按照你喜欢的方式组织它们，按时间、按类别都可以。

为了达到这一点，Maverick 通过叫做 `source_dir` 的选项在指定路径下搜索所有 Markdown 文件，并根据里面提供的信息将它们分门别类，生成日期标签等等。这些内容被称作 `frontmatter`，也就是使用 Hexo 等写文章时顶部的使用 `---` 包裹起来的那部分东西。这样的设计让以前的内容可以被复用，也便于以后的迁移。

此外是对图片的处理。Maverick 允许在 Markdown 文件中引用**任何位置**的图片，并且都能在生成网站时合适地处理它们。若你在原始文本中通过绝对路径或者相对路径引用本地图片，Maverick 会在生成网站时自动寻找它们，并把它们复制到统一的位置，同时修改文章里的引用链接；若通过 URL 引用了远程图片，则（可选地）将它们下载到本地缓存，按本地图片对待。这样处理的好处很多。

* Typora、VS Code 等软件都支持插入与预览本地图片。尤其是 Typora，本身还提供了插入图片时自动将图片复制到相对文章的某个目录的功能，这与 Maverick 的处理方式十分契合；
* 通过本地缓存，减小了图片丢失的风险。若图床跑路，你还可以在本地找到一份备份，不会影响你发布的内容；
* 虽然目前还没有实现这个功能，但通过本地化以及统一的发布流程，可以实现自动图片处理（例如压缩）；
* 可以提前获知图片的大小尺寸等信息，并在网页展示时提供优化的体验（比如图片排版与点击放大）。

而这一切都发生在生成站点时，不会对原本的文章有任何影响，不需要在文章里多加什么标注或者声明。只需要用标准的 Markdown 语法引入图片就好。此外，不论是缓存还是尺寸信息，Maverick 都会在生成时缓存下来，不会反反复复地请求与解析。

---

除了以上两点改进，Maverick 还自带了一些博客的常用功能，例如 RSS 源生成、**实时搜索**、Sitemap 等。这一切你都可以在[我的博客](https://blog.imalan.cn)以及[示例站点](https://alandecode.github.io/Maverick/)上体验到。目前，Maverick 没有插件机制，但以我自己的体验而言，应该具备了个人博客应有的功能。

我在 Lepture 开发的 Markdown 解析器 [mistune](https://github.com/lepture/mistune) 基础上进行扩展，添加了一些 Markdown 语法，使之能够良好地支持代码高亮、行内脚注、数学公式、图片排版等。

网页端的展示方面，Maverick 使用自带的主题 Galileo。这是一个比较简洁的主题，以文字阅读体验为重心开发，样式上借鉴了[安妮薇日报](https://anyway.fm/post/)与 [hexo-theme-cactus](https://github.com/probberechts/hexo-theme-cactus) 的设计。文字排版效果请参见 [Typography - Maverick](https://alandecode.github.io/Maverick/archives/typography/)。

---

总之，我从自己的观察与需求出发，自己写了一款静态博客生成器。本文只覆盖了关于 Maverick 的很小的一部分，欢迎各位移步 [项目主页](https://github.com/AlanDecode/Maverick) 阅读完整的说明。

这是我用 Python 写的第一个像点样的东西，因此不免有些遗漏与错误，任何建议与反馈都十分欢迎。当然 Star 则是特别欢迎😜。

那么，就这样，感谢各位阅读。周末愉快~
