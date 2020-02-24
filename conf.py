# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "jhx520/site-Blog@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 2

# 站点设置
site_name = "三刀魚"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-02-08T12:00+08:00"
author = "Anony"
email = "1046880355@qq.com"
author_homepage = "http://139931.xyz"
description = "我欲乘风向北行，雪落轩辕大如席"
key_words = ['三刀魚', '科技', 'Anony', '学习', 'Blog']
language = 'zh-CN'
external_links = [ 
 { 
 "name": "三刀魚", 
 "url": "http://anony.pp.ua", 
 "brief": "🏄‍ Go My Own Way." 
 }, 
 { 
 "name": "小游戏", 
 "url": "https://weigame.pp.ua", 
 "brief": "放松小游戏" 
 }, 
 { 
 "name": "云盘", 
 "url": "https://onedrive.pp.ua", 
 "brief": "Anony的云盘" 
 } 
 ] 
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "友链",
        "url": "${site_prefix}links/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "相册",
        "url": "${site_prefix}gallery/",
        "target": "_self"
    }
]

social_links = [ 
 { 
 "name": "Twitter", 
 "url": "https://twitter.com/Cv2Ln", 
 "icon": "gi gi-twitter" 
 }, 
 { 
 "name": "GitHub", 
 "url": "https://github.com/jhx520", 
 "icon": "gi gi-github" 
 }, 
 { 
 "name": "Weibo", 
 "url": "https://weibo.com/2975939221/", 
 "icon": "gi gi-weibo" 
 } 
 ] 

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}logo.png">
<link rel="shortcut icon" href="${static_prefix}favicon.ico">
<link rel="stylesheet" href="${static_prefix}1.css" />
'''

footer_addon = r'''
<div class="shaky">欢迎各位同学୧(๑•̀⌄•́๑)૭</div>
'''

body_addon = r'''
<!-- 点击烟花特效 -->
<canvas class="fireworks" 
        style="position: fixed; left: 0px; top: 0px; z-index: 99999999; pointer-events: none; width: 1158px; height: 916px;" 
        width="2316" 
        height="1832">
</canvas>
<script type="text/javascript" src="${static_prefix}anime.min.js"></script>
<script type="text/javascript" src="${static_prefix}fireworks.js"></script>
<!-- 点击烟花特效 -->
<!-- 评论输入特效 -->
<script src="${static_prefix}activate-power-mode.js"></script>
<script>
    POWERMODE.colorful = true; // ture 为启用礼花特效
    POWERMODE.shake = false; // false 为禁用震动特效
    document.body.addEventListener('input', POWERMODE);
</script>
<!-- 评论输入特效 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?9f55f0ad8d1ef06dd6141095e6c14611";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "uM4TdSOqBxnHFm3gcy0VRcVC-gzGzoHsz",
    "appKey": "S8PiDx66GTKdtjwmQ5dMnCK6",
    "visitor": True,
    "recordIP": True,
    "placeholder": "请不吝赐教"
}