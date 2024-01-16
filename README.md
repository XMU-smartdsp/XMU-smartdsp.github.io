# XMU-SmartDSP Website V2

## Introduction

This project is for the website of LAB OF SMART DATA AND SIGNAL PROCESSING, XIAMEN UNIVERSITY, FUJIAN CHINA (SmartDSP).

The first html version is built in 2018 and this V2 is built in 2023.

This project is drived by [VuePress](https://v2.vuepress.vuejs.org/zh/) and [VuePress Theme Hope](https://theme-hope.vuejs.press/)

It's builded by [HUII](https://github.com/huiiz).
Refounded Date: 2023.10.31

## Run it

You can start with:

```sh
git  clone -b v2 https://github.com/XMU-smartdsp/XMU-smartdsp.github.io.git
cd XMU-smartdsp.github.io
pnpm install
```
Then you can run it with
```sh
npm run docs:dev
```
and build it with
```sh
npm run docs:build
```
## Attenetion

- Although there are some image files that have an uppercase suffix (e.g. IMG_8752.JPG), you need to change them to **lowercase** (e.g. IMG_8752.jpg) and reference them correctly in markdown. Please make sure that the images with the **correct filenames have been updated in GitHub**, otherwise the build may **fail** in GitHub.

- You can get some help about the website config from [here](https://theme-hope.vuejs.press/zh/config/intro.html)

## How to update the website? 如何更新网站？

### News 新闻

新闻文件位于```src\news```文件夹下，命名按照```news日期.md```格式，参考文件夹下文件。如果一天内有多篇，可在后面加```_序号```，如```news20160308_2.md```表示2016年3月8日的第二篇。

新闻内容使用markdown格式，头部是新闻的基本信息：
```markdown
date: 日期，如：2022-07-18
category:
  - 分类
editLink: false（默认，无需更改）
cover: 封面图，如：/news/newsimage0718/IMG_8752.jpg，可不填
```

注意：
- 静态文件根目录为```src\.vuepress\public```,新闻图片统一放在```src\.vuepress\public\news```下。
- 图像文件后缀名以小写为宜，如```.jpg```,```.png```(大写后缀名可能导致报错)

### 学术团队和毕业生资料维护
分别对应```src\team.md```和```src\graduate.md```文件，硕博与毕业生数据存放格式均为
```js
{
    入学/毕业年份: [
          {
            name: "姓名",
            avatar: "头像地址，这里只要填文件名即可，如fanzhiwen.jpg",
            title: "毕业去向",
            link: "个人主页",
          },
    ]
}
```
头像文件夹位于```src\.vuepress\public\assets\images\memberimage```

### 网站基础信息

网站相关配置位于```src\.vuepress```文件夹下的四个```.ts```文件中。
其他信息可以自行了解。

---

Welcome to our website: [https://xmu-smartdsp.github.io/](https://xmu-smartdsp.github.io/)

All rights received by SmartDSP.
