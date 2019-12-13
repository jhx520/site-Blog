---
layout: post
cid: 259
title: Semantic Web：结构化数据
slug: 259
date: 2019/02/01 16:31:00
updated: 2019/03/30 17:50:51
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
  - 前端
  - VOID笔记
excerpt: 谈谈诸如微格式、微数据等概念与应用。
---


文章标题是几个故弄玄虚的词，但本文要聊的是更具体与实用的东西：从某些愿景出发，谈诸如 Microdata、Microformat、JSON-LD 等概念与其实践。


<!--more-->


## 0X01: Semantic Web

{{语义网:Semantic Web}}是由 Tim Berners-Lee 于 1998 年提出的概念，它的核心是给万维网上的文档（例如 HTML）添加可以被机器理解的语义作为文档的{{元数据:metadata}}，使整个互联网成为一个通用的信息交换媒介[^摘自维基百科]。

说得更简单些，语义网的宗旨是帮助计算机理解网络上各种资源到底是什么，以此来使信息的集合、分发、分析效率更高，并且有的放矢。

语义网的实现途径有很多，例如 HTML 中的各种语义化标签就是一例。我们常常推荐使用诸如 `<nav>`、`<header>`、`<aside>` 等标签代替单纯的 `<div>`，背后的目的之一就是使 HTML 文档具有更好的语义：对机器而言，更容易理解页面上具体是什么。[HTML Accessibility](https://www.w3schools.com/html/html_accessibility.asp)  就相当依赖这些语义数据，读屏软件[^一类读出屏幕内容的软件，一般为视觉障碍的用户服务]可以很清楚地知道 `<nav>` 标签中的链接代表着页面导航，`<figure>` 标签中的内容代表着文章配图与图题，使用 `<div>` 与 `<img>` 标签在视觉展示效果上也许能达到相同的效果，但是它背后蕴含的信息量却是截然不同的。不过 Accessibility 是一个大议题，不是本文重点。

语义网通过使用标准、标记语言以及相关的工具作为技术实现手段，本文要聊的就是其中一种：{{结构化数据:Structured Data }}。

## 0X02: Structured Data

结构化数据一个大概念，它指一切以某种特定结构组织的数据，例如一个数据库、一张数据表。实际上我们常用的词 SQL — Structured Query Language 就蕴含着结构化数据的思想。

在 Web 语境下说结构化数据，主要说的是以某种特定的数据结构呈现页面的内容。例如一个介绍了一张菜谱的网页，视觉上的效果各有不同，但其中的重要信息是一致的：菜名、原料与用量、烹制顺序、烹制时间等。结构化数据通过某种标准，帮助各个网站对其内容做好标记，方便第三方服务抓取、分析与展示。

结构化数据是一种思想，具体实现途径有多种，例如[{{微数据:Microdata}}](https://www.w3.org/TR/microdata/)，[{{微格式:Microformat}}](http://microformats.org)，[JSON-LD](https://json-ld.org/)，RDFa 等。但不论使用哪种途径，都需要一个统一的标准为{{事物:Thing}}制定必须的属性集合，例如一辆汽车的结构化属性（价格、排量等），一本书的结构化属性（书名、作者、出版时间等）。

互联网上，{{事实上的:de-facto}}结构化数据标准是 [Schema.org](https://schema.org)，它制定了许多标准，并且仍然在添加更多的标准，例如下图是 Schema.org 制定的一张菜谱需要的结构内容：

![Scheme.org - Recipe][1]

可以想象，如果需要一个网页展示的菜谱更容易被机器理解，就需要在网页中显式地指明上图中列出的数据，而且还是以某种开放的、大家都接受的格式。

需要特别说明的是，虽然结构化数据经常和 SEO 一块儿讨论，但结构化数据的作用绝不只是 SEO，它是“讲究的 HTML”所必备的。

现在，我们来聊聊技术细节。对技术不敏感的读者可以止步于此了。

## 0X03: Microdata

Microdata，或者微数据，是 HTML 5 引入的。它扩展了 HTML 的属性集，通过 `itemscope`、`itemtype`、`itemprop` 加上 `itemid` 与 `itemref` 来界定结构化数据的类型与数据来源。

给标签加上 `itemscope` 属性，代表这是一个事物（item）：

```html
<div itemscope>
    ...
</div>
```

标记了 `itemscope` 的 DOM 树中就应该包含这个事物的信息。这个事物到底是什么？我们可以使用 Scheme.org 所定义的格式：

```html
<div itemscope itemtype="https://schema.org/Book">
    <div>书名：<span itemprop="name">挪威的森林</span></div>
    <div>作者：<span itemprop="author">村上春树</span></div>
    ...
</div>
```

带有 `itemscope` 的元素下面的子元素通过 `itemprop` 指定数据名称，标签的内容就是这个属性的值。当然 `itemprop` 也应该在文档中查询对应的事物得到。

 `itemid` 与 `itemref` 用于无法在同一个 `itemscope` 中指定所有结构化数据的情况。例如：

```html
<div itemscope itemref="book-1-attr-1 book-1-attr-2" itemtype="https://schema.org/Book">
    <div>书名：<span itemprop="name">挪威的森林</span></div>
    ...
</div>

<!-- 在 itemscope 外声明 -->
<div id="book-1-attr-1">书名：<span itemprop="author">村上春树</span></div>
<div id="book-1-attr-2">价格：<span itemprop="price">$20</span></div>
```

VOID 1.2 版本添加了 Microdata 支持，你可以在检查元素中查看一下。你看到的这个页面使用的是 http://schema.org/Article 这个 `itemtype`，完整的属性集：

```html
<article itemscope="" itemtype="http://schema.org/Article">
    <h1 itemprop="name">Semantic Web：结构化数据</h1>
    <p hidden itemprop="headline">...</p>
    <time datetime="2019-02-01T16:31:14Z" itemprop="datePublished">2019-02-01</time>
    <div itemprop="articleBody">...</div>
    <meta itemprop="dateModified" content="2019-02-01T16:31:14Z">
    <span itemprop="author">熊猫小A</span>
    <div hidden itemprop="image" itemscope="" itemtype="https://schema.org/ImageObject">
        <meta itemprop="url" content="https://blog.imalan.cn/usr/uploads/2019/02/1792839130.png">
    </div>
    <div hidden itemprop="publisher" itemscope="" itemtype="https://schema.org/Organization">
        <meta itemprop="name" content="熊猫小A的博客">
        <div itemprop="logo" itemscope="" itemtype="https://schema.org/ImageObject">
            <meta itemprop="url" content="https://secure.gravatar.com/avatar/1741a6eef5c824899e347e4afcbaa75d?s=256&amp;r=&amp;d=">
        </div>
    </div>
    <meta itemscope="" itemprop="mainEntityOfPage" itemtype="https://schema.org/WebPage" itemid="https://blog.imalan.cn/archives/259/">
</article>
```

## 0X04: Microformat

Microformat（也叫 μF） 诞生已经 14 年了。它相对 Microdata 而言要更简单一些：使用 class 与 rel 来指定数据类型与数据名。

虽说互联网上有事实上的标准 Schema.org，但你实际上是可以自定义任何 itemtype 作为 Microdata 的。Microformat 则与此不同，你基本上只能使用 [Wiki](http://microformats.org/wiki/Main_Page) 上列出来的东西，要想使用新的则需要经过冗长的流程。Microformat 基本上已经是过去时了，所以并不十分推荐。

以一篇文章为例，最适合的类型是 [hentry](http://microformats.org/wiki/hentry)：

![Microformat - hentry][2]

在原有的结构上添加一些 class 名即可完成 Microformat 标注：

```html
<article class="h-entry">
  <h1 class="p-name">Semantic Web: 结构化数据</h1>
  <p>Published by <a class="p-author h-card" href="https://blog.imalan.cn">熊猫小A</a>
     on <time class="dt-published" datetime="2019-02-01T16:31:14Z">2019-02-01</time></p>
  <p class="p-summary">...</p>
  <div class="e-content">
    ...
  </div>
</article>
```

Microformat 的好处是相对简单，在原始的页面上应用少量的更改即可。并且由于它使用类名作为标志，可以在一定程度上指导页面开发。

不过值得一提的是，Google 的[结构化数据接入指导](https://developers.google.com/search/docs/guides/intro-structured-data)中并没有提及它是否支持 Microformat，因此综合考虑下我并没有为本站添加 Microformat 支持。

## 0X05: JSON-LD

JSON-LD 是 JSON for Linking Data 的缩写。我挺喜欢它官网的 slogan：

> Data is messy and disconnected. JSON-LD organizes and connects it, creating a better Web.

当然，每一种结构化数据手段都是为了“creating a better Web”。JSON-LD 是相对较新的东西，它采用 JSON 格式在页面中展示页面信息，例如：

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Recipe",
  "name": "Grandma's Holiday Apple Pie",
  "author": "Elaine Smith",
  "image": "http://......",
  "description": "A classic apple pie."
}
</script>
```

这段代码可以放在页面的 head 中，也可以放在页面内。Google 明确说明了它支持动态注入的 JSON-LD 数据，也就是说可以放心地在页面中使用 AJAX 等技术：

> Google can read JSON-LD data when it is dynamically injected into the page's contents, such as by JavaScript code or embedded widgets in your content management system.

使用 JSON-LD 的好处是完全不用更改原 HTML 结构，只需要在页面中添加这部分数据即可。坏处是它使用独立的一块 JSON 来展示数据，使页面数据有一部分冗余。

注意，JSON-LD 是 Google 推荐的结构化数据标注方式。另还有 RDFa 等标注方式，现在用得较少了，就不单独说明了。

## 0X06: In real world

虽然 Google 在「尝试搞明白网页上都在说什么」这件事上做得已经相当不错了，但充分地使用结构化数据为网页做好标记仍然是有意义的。一个明显的优势是做好了标注的网页在 Google 的搜索结果中**可能**会有更好的展示。

![一个菜单搜索结果][3]

Google 在[这里](https://developers.google.com/search/docs/guides/mark-up-content)列举了它所支持的部分类型，截止本文写作（2019-02-01），支持的类型与可能的结果展示方式如下：

![Google 支持的标注类型][4]

对每种数据类型，在提供了所有{{必须:required}}信息的前提下，Google 提倡提供尽量多的{{可用:optional}}信息。但是值得注意的是，Google 有他自己的一套要求，与 Scheme.org 的要求并不一定一致。

Google 提供了一个[结构化数据检查工具](https://search.google.com/structured-data/testing-tool)，你可以输入网址或者粘贴代码来查看网页标记是否合规，例如你正在看到的这个页面检测结果如下：

![测试结果][5]

至于是否需要在页面中同时应用多种标记，例如同时使用 JSON-LD 与 Microdata，这个视情况而定。只要多个标记的标记内容都是一致的，Google 是可以接受的，但是若标记内容不同，则可能被判定为重复的内容，这不利于 SEO。以我自己的实践来说，考虑到浏览器与搜索引擎支持，目前在博客中支持了 Microdata。JSON-LD 稍后支持。

除了对网页数据进行语义化标注，Google 还对 GMail [做了支持](https://developers.google.com/gmail/markup/getting-started)。如果你曾经使用过 Google 出品的 Index 这个产品，会发现 Google 对邮件的内容分析做得相当好，这一部分是机器学习的功劳，一部分仰赖各个厂商对邮件的标记。例如机票、酒店预订等通知邮件，通过良好的标记都可以帮助 Google 在产品中更直观地展示邮件中的重要信息，甚至帮助用户订车、安排日程等。

------

参考：

- https://ahrefs.com/blog/what-is-structured-data/
- https://www.wikiwand.com/en/Semantic_Web
- https://www.w3.org/TR/microdata/
- https://lepture.com/zh/2015/fe-microdata
- http://microformats.org/
- https://json-ld.org/


  [1]: ./assets/4195820294.png
  [2]: ./assets/2420525554.png
  [3]: ./assets/2240800113.png
  [4]: ./assets/1745795788.png
  [5]: ./assets/2599722711.png