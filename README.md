# rainkmc_feeder

雨中小町rss生成器，生成.xml文件以供订阅。

使用python直接抓取页面，需要账户和密码登录。

在页面抓取完后使用Huginn生成rss。

Huginn生成分为3个步骤：

1. 通过Xpath获取每一条发帖
2. 通过选择器选择自己感兴趣的内容[通过javascript实现]
3. 生成.xml页面

最终生成的页面只包含URL，标题和日期，不含正文。要阅读正文可通过embeded html模式阅读。