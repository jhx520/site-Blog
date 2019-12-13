---
layout: post
cid: 137
title: Vintage Web
slug: 137
date: 2018/07/17 20:21:00
updated: 2019/05/18 10:04:57
status: publish
author: 熊猫小A
categories: 
  - 胡说八道
tags: 
  - 博客
  - 主题
excerpt: 没错，就是要多折腾。
---


今天干活摸鱼，读到了一篇文章：[How the Blog Broke the Web](https://stackingthebricks.com/how-blogs-broke-the-web/) ，正巧，我最近正在思考一些相关的问题，于是就着不成熟的想法写这么一篇短文。

读到的这篇文章讲了一件事：面向大众的博客系统如何让 Web 变得千篇一律，变得不「Cool」了。作者谈到，早年间他{{网上冲浪:Surfing the Net}}时，还没有{{博客:blog}}的说法，大家有的是{{主页:homepage}}。那时候一个人要发布一篇内容，步骤何其繁杂：

> We built every new page *by hand*. When we had more than one web *page*, we built the navigation *by hand*. We managed our Table of Contents *by hand*. We broke out our calculators to code boundaries for our image maps. We talked unironically about “hyperlinks.” 

以及：

> Diarying was *a helluva lot of work*. First you had to have something to say, then write, edit it, format it, add clip art, edit your index.html, edit any prev/next links, check those links, and lastly, upload the files. 

门槛不低，就连我读到这里都吃了一惊。

最近我有回到静态博客的想法，因为毕竟动态博客系统依赖数据库，而在中国租用 VPS 可不是件便宜的事情，静态博客则有简单的[解决方法](https://pages.github.com/)。手写 HTML 与 CSS，以及需要的 JS 代码是终极的解决方案，但我随即自我否定：每一个页面都自己写一遍 head 标签里的各种 meta 吗？不能愚蠢至此啊，即使是刚发明万维网时也不可能连这等自动化程度都没有。事实证明我错了，依照上面的片段，我们的前辈们是真的在**手写每一个页面**。

后来我在 [Hexo](https://hexo.io/) 上犹豫不定，Hexo 是一个静态博客生成器，它把输入的 Markdown 文件转换为各个 index.html。这种解决方案与文章中提到的「Movable Type 」同出一辙。「Movable Type 」不是什么大不了的系统，只是一系列的脚本而已，比起 Hexo 尚要落后许多，更不提 Wordpress、Typecho 这些带有数据库的动态博客系统了。然而正是这个东西，被作者认为是 Web 死掉的开端。

这是个简单的道理：东西越是简单，用的人越多。

![][1]

上面是「Movable Type 」新建文章的界面，这与如今的 WordPress、Typecho 没什么大的不同。你只要在每个框里输入对应的内容，工具就能帮你生成需要的 HTML 文件。有了这样简单的工具，内容生产者大可把心思放在要写的内容上，而不必忙碌于学习 HTML。坏处是：**网站们变得千篇一律，当年自己写页面、百家争鸣的好日子不在了**。

听上去又是那一套「Golden Ages」的论调，我们很容易在脑袋里构思出一个上了年纪的大叔嘟嘟囔囔地说着“当年可不是这样的……”，不无顽固的感觉，但就这件事上，作者说对了。

虽然用着 Hexo、WordPress、Typecho 默认主题的不多，但即使是使用自定义的主题也是大面积地撞车。比如我正在使用的「handsome」主题，在 Typecho 世界是十足的明星主题，使用的人何其多。个人博客的个人特质只能通过「魔改」来实现，但这门槛可不低。即使是 Hexo 也不可谓不复杂，Typecho、Wordpress 可不是简单的静态博客生成器，它们是动态博客。在 2018 年一个人想要自己定制博客，除了 HTML、CSS、JS 外，还要掌握服务端的语言，比如 PHP、NodeJS 等。若使用这些博客系统有一个难度曲线的话，从「使用一切默认功能」到「做出自己的改变」之间有陡峭的难度提升，绝大多数人难以越过。结果就是，**[Cool but difficult] VS [Ordinary but simple]，**绝大多数人会选择，也只能选择后者。

这就是为什么[How the Blog Broke the Web](https://stackingthebricks.com/how-blogs-broke-the-web/) 这篇文章的作者说“Blog broked the Web”。虽然这个说法显得过于斩钉截铁，忽略了简单的工具带来的好处，但我们可以接受作者的这一点说法：博客系统的出现让网络世界不再丰富多彩了。

「要和别人不一样」听上去更像一个 15 岁少年想要标新立异时的想法，很可能会被一些实用主义者嘲笑。但仔细想想其实历来如此，如果你总是与别人做一样的事，you are never cool。网络世界可从来没有因为「整洁划一」或者「井井有条」被人们称道。The online world is destined to be diverse. 

我不是在倡导大家回去过原始生活，去“手写 index.html”。这谁也倡导不了，历史有它前进的方向。有一件事我们得明确，不是“手写 index.html”造就了人们怀念的 **「Vintage Web」**，而是那种纯粹、创造力、多样性造就了**「Vintage Web」**。

**我要倡导的是：去折腾，去玩，去创造，去用尽你的想象力做出真正有趣的东西。Live like a 16 year old boy, forever.**


  [1]: ./assets/movabletype_interface_new_entry.gif