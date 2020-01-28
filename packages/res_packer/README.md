# Cocos Creator 微信小游戏内置资源打包插件

插件功能：使用Cocos Creator构建微信小游戏项目时，会自动打包指定必要的内置资源到首包。有效解决启动场景因网络延迟或加载失败而导致的黑屏/卡死问题。

## 原作者
[dylan465@github](https://github.com/dylan465/plugin_internal_res_packer)

## 验证过的支持格式
1. 字体格式（BmFont、LabelAtlas原先就支持，TTF修改后兼容）
2. 粒子
3. 原生资源（若勾选“合并初始场景依赖的所有JSON”时，部分依赖的原生资源无法被找到依赖）
4. 自动图集

## 主要改动
1. 发布时若勾选调试模式依然可以进行分包，方便调试
2. 在wechatgame外建立res文件夹，存放打包后的所有资源
3. 在wechatgame外建立res-temp文件夹，用来做文件剪切工作，以减小子包压缩包大小
4. 对特殊格式资源进行兼容（如TTF格式的资源会生成一个子文件夹"res\\raw-assets\\5b\\5b9cbc23-76b3-41ff-9953-4219fdbea72c\\Fontin-SmallCaps.ttf"）（v2.1.4）

## 解决的具体问题：
1. Cocos Creator初始化引擎时，会先加载内置资源文件夹effects和materials下的资源，因为基础组件cc.Sprite需要对应的material才能显示，如果出现加载失败的情况会导致黑屏卡死。
2. 在玩家首次启动游戏时，加载启动场景/首屏会从远程加载资源，资源在下载过程会出现短暂的黑屏。
3. 其他资源加载问题，比如Cocos Creator 2.2.0华为快游戏播放音频时会出现卡顿，把对应的音频文件夹打包到包里可以解决这个问题。

## 使用方法：
1. 所有项目生效：把插件文件夹拷贝到 用户名/.CocosCreator/packages下；指定项目生效：把插件文件夹拷贝到 项目根目录/packages下。重启Cocos Creator
2. 构建微信小游戏项目，勾选MD5 cache，不勾选调试模式（正式打包才启用该插件功能）
3. 构建完成后，会多出一个res_internal文件夹，这个文件夹就是内置的资源。把原本res文件夹资源上传到服务器后，移除或者删除res文件夹，最后把res_internal重命名为res。

## 修改插件代码打包其他资源
打包文件夹 queryAssets('db://assets/resources/sounds/**/*');
打包具体文件 queryAssets('db://assets/RewardView.prefab');