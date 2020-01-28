[toc]
## 概述
对于Cocos Creator的一些梳理，包括架构、插件以及其他常用功能

## 目录划分
* assets
    * resources
        * 按场景划分资源文件夹
    * scripts
        * core -- 核心架构
            * mvc
            * ecs
            * elk -- 日志记录及上报
            * audio -- 背景音乐、音频切分、循环音效
            * screen -- 资源适配及横竖屏切换
            * net -- http和ws
            * touch -- 多点触摸管理
            * memory -- 内存管理
        * tool -- 工具
            * scrollview
            * 
        * sdk -- SDK相关
    * 其他场景文件夹
* packages
    * res-packages -- 资源分包
    * 

## 场景设置
默认开启资源清理、单点触摸、使用mvc
* load -- 加载
* content -- 目录（运用scrollview优化）
* test-screen
* test-touch
* test-net
* test-audio
* test-ecs
