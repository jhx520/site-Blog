---
layout: post
cid: 277
title: Sticky：CSS 粘性布局
slug: 277
date: 2019/03/03 10:02:00
updated: 2019/03/03 10:17:37
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
  - 前端
excerpt: 一个相当方便的属性，用于解决随滚动固定的布局问题。
---


最近发现了一个不错的 CSS 属性：`position:sticky`，这个尚处于实验阶段的属性可以很好的解决网页中边栏随滚动固定的问题。

先看一个 Demo，在上下滚动过程中注意右侧红色块的行为：

<iframe height="450" style="width: 100%;" scrolling="no" title="position: sticky Demo" src="//codepen.io/AlanDecode/embed/gErQqq/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/AlanDecode/pen/gErQqq/'>position: sticky Demo</a> by AlanDecode
  (<a href='https://codepen.io/AlanDecode'>@AlanDecode</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

这就是 `position: sticky` 的作用。以下部分摘选自 [MDN Position](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)：

> 盒位置根据正常流计算（这称为正常流动中的位置），然后相对于该元素在流中的 flow root（BFC）和 containing block（最近的块级祖先元素）定位。在所有情况下（即便被定位元素为 `table 时`），该元素定位均不对后续元素造成影响。当元素 B 被粘性定位时，后续元素的位置仍按照 B 未定位时的位置来确定。`position: sticky ` 对 `table` 元素的效果与 `position: relative `相同。

因此，应用这个属性并不会破坏网页原有布局，super cool。

应用时，除了指定 `position: sticky` 外还必须指定 `top`、`bottom`、`right`、`left` 中至少一个作为阈值，当元素距离 viewport 边缘的距离达到这个阈值时就会触发黏性布局。

兼容性：

![兼容性，2019-03-03](./assets/4200253595.png)

emmm，如果不是生产环境，还是可以玩玩的。另外有开源库可以稍稍提升一下这个属性的兼容性：[filamentgroup/fixed-sticky](https://github.com/filamentgroup/fixed-sticky)，但是这个项目已经 Archive 了。