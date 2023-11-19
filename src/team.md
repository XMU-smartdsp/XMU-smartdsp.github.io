---
article: false
icon: circle-info
editLink: false
pageInfo: false
breadcrumb: false
---

# 学术团队

## 教师团队

<div class="row">
    <div class="team">
        <div class="team-item" v-for="(item, index) in teachers" :key="index">
          <img :src="`${avatarBaseUrl}${item.avatar}`" alt="" />
          <div class="name">{{ item.name }}</div>
          <div class="title">{{ item.title }}</div>
          <a :href="item.link" target="_blank"><img src="/assets/images/home.gif"></a>
      </div>
    </div>
</div>

## 博士生

<div class="row">
    <div class="team">
        <template v-for="(students, year, i) in phds" :key="year">
            <div class="team-item" v-for="(item, index) in students" :key="index">
              <img :src="`${avatarBaseUrl}${item.avatar}`" alt="" />
              <div class="name">{{ item.name }}</div>
              <div class="title">{{ year }}级</div>
              <a :href="item.link" target="_blank"><img src="/assets/images/home.gif"></a>
            </div>
        </template>
    </div>
</div>

## 硕士研究生

<template v-for="(students, year, i) in masters" :key="year">

  <h3 :id="'_'+year+'级'" tabindex="-1"><a class="header-anchor" :href="'#_'+year+'级'" aria-hidden="true">#</a> {{year}} 级</h3>
  <div class="row">
      <div class="team">
          <div class="team-item" v-for="(item, index) in students" :key="index">
            <img :src="`${avatarBaseUrl}${item.avatar}`" alt="" />
            <div class="name">{{ item.name }}</div>
            <div class="title">{{year}} 级</div>
            <a :href="item.link" target="_blank"><img src="/assets/images/home.gif"></a>
        </div>
      </div>
  </div>
</template>


<script>
export default {
    // data() 返回的属性将会成为响应式的状态
    // 并且暴露在 `this` 上
    data() {
        return {
            avatarBaseUrl: "assets/images/memberimage/",
            teachers: [
                {
                    name: "丁兴号",
                    avatar: "dingxinghao.jpg",
                    title: "教授，博导",
                    link: "teamindex/xhding.html",
                },
                {
                    name: "黄悦",
                    avatar: "huangyue.jpg",
                    title: "教授，硕导",
                    link: "teamindex/yhuang.html",
                },
                {
                    name: "肖珍龙",
                    avatar: "xiaozhenlong.jpg",
                    title: "副教授，硕导",
                    link: "teamindex/zlxiao.html",
                },
                {
                    name: "涂晓彤",
                    avatar: "tuxiaotong.jpg",
                    title: "助理教授，硕导",
                    link: "teamindex/xttu.html",
                },
                {
                    name: "John Paisely",
                    avatar: "john.jpg",
                    title: "客座教授",
                    link: "http://www.columbia.edu/~jwp2128/",
                },
                {
                    name: "Mingyuan Zhou",
                    avatar: "zhoumingyuan.png",
                    title: "客座教授",
                    link: "http://mingyuanzhou.github.io/",
                },
            ],
            phds: {
                2014: [{
                    name: "傅雪阳",
                    avatar: "fuxueyang.jpg",
                    title: "",
                    link: "https://xueyangfu.github.io",
                },],
                2015: [{
                    name: "王宇",
                    avatar: "wangyu.jpg",
                    title: "",
                    link: "teamindex/ywang.html",
                },],
                2016: [{
                    name: "孙立言",
                    avatar: "sunliyan.jpg",
                    title: "",
                    link: "https://lynnsunxmu.github.io",
                },],
                2017: [{
                    name: "王武",
                    avatar: "wangwu.jpg",
                    title: "",
                    link: "#"
                },],
                2018: [{
                    name: "林煌星",
                    avatar: "linhuangxing.jpg",
                    title: "",
                    link: "#",
                },
                {
                    name: "井长兴",
                    avatar: "jingchangxing.jpg",
                    title: "",
                    link: "#",
                },],
                2019: [{
                    name: "富振奇",
                    avatar: "fuzhenqi.jpg",
                    title: "",
                    link: "https://zhenqifu.github.io/",
                },
                {
                    name: "马超",
                    avatar: "machao.jpg",
                    title: "",
                    link: "#"
                },],
                2020: [{
                    name: "徐浩特",
                    avatar: "xuhaote.jpg",
                    title: "",
                    link: "#"
                },
                {
                    name: "匡振宇",
                    avatar: "kuangzhenyu.jpg",
                    title: "",
                    link: "#",
                },],
                2021: [{
                    name: "孟戈",
                    avatar: "mengge.jpg",
                    title: "",
                    link: "#"
                },
                {
                    name: "黄飞成",
                    avatar: "huangfeicheng.jpg",
                    title: "",
                    link: "#",
                },],
                2022: [{
                    name: "林溦",
                    avatar: "linwei.png",
                    title: "",
                    link: "#"
                },
                {
                    name: "黄海靓",
                    avatar: "huanghailiang.jpg",
                    title: "",
                    link: "#",
                },
                {
                    name: "王莹莹",
                    avatar: "wangyingying.jpg",
                    title: "",
                    link: "#",
                },]
            },
            masters: {
                2020: [
                    {
                        name: "蔡森林",
                        avatar: "caisenlin.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "柴舒",
                        avatar: "chaishu.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "陈睿哲",
                        avatar: "chenruizhe.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "丁之元",
                        avatar: "dingzhiyuan.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "何楚楚",
                        avatar: "hechuchu.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "黄乐兴",
                        avatar: "huanglexing.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "李炯承",
                        avatar: "lijiongcheng.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "梁浩",
                        avatar: "lianghao.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "林晓鹏",
                        avatar: "linxiaopeng.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "饶智杰",
                        avatar: "raozhijie.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "王天浚",
                        avatar: "dabai.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "王蔚瑜",
                        avatar: "wangweiyu.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "余少聪",
                        avatar: "yushaocong.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "张弛",
                        avatar: "zhangchi.png",
                        title: "",
                        link: ""
                    },
                    {
                        name: "周观星",
                        avatar: "zhouguanxing.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "庄易鸿",
                        avatar: "zhuangyihong.jpg",
                        title: "",
                        link: "",
                    },
                ],
                2021: [
                    {
                        name: "褚学业",
                        avatar: "chuxueye.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "丁海舟",
                        avatar: "dinghaizhou.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "胡郁明",
                        avatar: "huyuming.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "赖灿兴",
                        avatar: "laicanxing.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "林初阳",
                        avatar: "linchuyang.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "刘奕阳",
                        avatar: "liuyiyang.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "吕正芃",
                        avatar: "dabai.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "毛怡瑾",
                        avatar: "maoyijin.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "魏海艳",
                        avatar: "weihaiyan.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "徐迎",
                        avatar: "xuying.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "杨刚",
                        avatar: "yanggang.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "张勇华",
                        avatar: "zhangyonghua.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "郑国庆",
                        avatar: "zhengguoqing.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "钟杰",
                        avatar: "zhongjie.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "钟亦劲",
                        avatar: "zhongyijin.jpg",
                        title: "",
                        link: "",
                    },
                    {
                        name: "周文波",
                        avatar: "zhouwenbo.jpg",
                        title: "",
                        link: "",
                    },
                ],
                2022: [
                    {
                        name: "陈晓璐",
                        avatar: "陈晓璐.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "程利东",
                        avatar: "程利东.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "邓成浩",
                        avatar: "邓成浩.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "董於航",
                        avatar: "董於航.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "范琳钰",
                        avatar: "范琳钰.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "黄婧嘉",
                        avatar: "黄婧嘉.png",
                        title: "",
                        link: ""
                    },
                    {
                        name: "李晨",
                        avatar: "李晨.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "林鸿",
                        avatar: "林鸿.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "马晨雨",
                        avatar: "马晨雨.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "彭家傲",
                        avatar: "彭家傲.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "唐路垚",
                        avatar: "唐路垚.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "吴庆垚",
                        avatar: "吴庆垚.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "夏周翔",
                        avatar: "夏周翔.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "余河灯",
                        avatar: "余河灯.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "袁与炫",
                        avatar: "袁与炫.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "章弘阳",
                        avatar: "章弘阳.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "庄荣晋",
                        avatar: "庄荣晋.jpg",
                        title: "",
                        link: ""
                    },
                    {
                        name: "王珺玮",
                        avatar: "wangjunwei.jpg",
                        title: "",
                        link: "",
                    },
                ],
            },

        };
    },
};
</script>

<style>
.team {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    /*自动换行并自动平均分配宽度 */
    gap: 15px;
    /* 可以添加适当的间距*/
    text-align: center;
}

.name {
    font-size: 15px;
}

.title {
    font-size: 12px;
}
</style>
