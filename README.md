# rainkmc_feeder

**Introduction项目介绍**：雨中小町rss生成器，抓取网页内容并生成.xml的rss2.0文件以供订阅。

**Prerequisite必要前提**：

1. RSS(Really Simple Syndication)的常识
2. tt-rss(tiny tiny rss)阅读器或者其他主流rss阅读器
3. 配置好的Huginn环境(推荐使用docker配置)。[Huginn项目地址](https://github.com/huginn/huginn)

**Specification详细介绍：**

1. 使用python直接抓取页面，需要提供您的**账户**和**密码**登录以抓取页面(rainkmc.py)。

2. 在页面抓取完后使用Huginn生成rss订阅源。

   Huginn生成订阅源分为**4**个步骤：

   1. 通过Xpath获取发帖内容。(rainkmc_spider.json)

      使用Website Agent

   2. 根据URL属性对获取到的Event进行去重。(rainkmc_dedup.json)

      使用De Duplication Agent

   3. 通过选择器选择自己感兴趣的内容，通过javascript实现，可自定义规则。(rainkmc_selector.json)

      使用Java Script Agent 

   4. 生成.xml页面。(rainkmc_out.json)

      使用Data Output Agent 

最终生成的页面只包含URL，标题和日期，不含正文。要阅读正文可通过embeded html模式阅读。