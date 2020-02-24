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
'''

footer_addon = r'''
<?php
        $counterFile = "counter.txt";
        function displayCounter($counterFile) {
        $fp = fopen($counterFile,"rw");
        $num = fgets($fp,4096);
        $num += 1;
        print "您是第 " . $num . " 位同学";
        exec( "rm -rf $counterFile");
        exec( "echo $num > $counterFile");
                }
        if (!file_exists($counterFile)) {
            exec( "echo 0 > $counterFile");
            }
        displayCounter($counterFile);
?>
'''

body_addon = r'''
<script src="http://xiaowiba.com/live2d_models/L2Dwidget.min.js"></script>
<script src="http://xiaowiba.com/live2d_models/L2Dwidget.0.min.js"></script>
<script>
    L2Dwidget.init({
        "model":{
            "scale":1,"hHeadPos":0.5,"vHeadPos":0.618,
            "jsonPath":"http://xiaowiba.com/live2d_models/live2d-widget-model-hijiki/assets/hijiki.model.json"
        },
        "display":{
            "superSample":2,"width":100,"height":220,"position":"right","hOffset":20,"vOffset":-20
        },
        "mobile":{
            "show":false,"scale":0.5
        },
        "react":{
            "opacityDefault":0.7,"opacityOnHover":0.2
        }
    });
</script>
<div id="live2d-widget">
    <canvas id="live2dcanvas" width="200" height="440" 
    style="position: fixed; opacity: 1; right: 0px; bottom: 0; z-index: 99999; pointer-events: none;"></canvas>
</div>
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