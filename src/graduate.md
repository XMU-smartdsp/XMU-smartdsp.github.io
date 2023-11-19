---
article: false
icon: circle-info
# cover: /assets/images/cover3.jpg
editLink: false
---

# 桃李天下
<div class="row">
    <div class="team">
        <template v-for="(students, year, i) in graduates" :key="year">
          <div class="team-item" v-for="(item, index) in students" :key="index">
              <img :src="`${avatarBaseUrl}${item.avatar}`" alt="" />
              <div class="name" v-if="item.link"><a :href="item.link" target="_blank" >{{ item.name }}</a></div>
              <div v-else>{{ item.name }}</div>
              <div class="year">毕业年份：{{ year}}</div>
              <div class="goto">{{ item.title }}</div>
          </div>
        </template>
    </div>
</div>

<script>
export default {
  // data() 返回的属性将会成为响应式的状态
  // 并且暴露在 `this` 上
  data() {
    return {
      avatarBaseUrl: "assets/images/memberimage/",
      graduates: {
        2013: [
          {
            name: "糜增元",
            avatar: "mizengyuan.jpg",
            title: "国家专利审查局",
            link: "",
          },
          {
            name: "谢进",
            avatar: "xiejin.jpg",
            title: "部队",
            link: "",
          },
          {
            name: "金文博",
            avatar: "jinwenbo.jpg",
            title: "中国建设银行总行",
            link: "",
          },
          {
            name: "易才钦",
            avatar: "dabai.jpg",
            title: "广州专利局",
            link: "",
          },
          {
            name: "于一淼",
            avatar: "dabai.jpg",
            title: "百度",
            link: "",
          },
          {
            name: "吴笑天",
            avatar: "dabai.jpg",
            title: "长春光机所",
            link: "",
          },
        ],
        2014: [
          {
            name: "林溱",
            avatar: "linqin.jpg",
            title: "福州电信",
            link: "",
          },
          {
            name: "傅雪阳",
            avatar: "fuxueyang.jpg",
            title: "读博",
            link: "",
          },
          {
            name: "张君",
            avatar: "zhangjun.jpg",
            title: "华为技术有限公司",
            link: "",
          },
          {
            name: "郑贤辉",
            avatar: "zhengxianhui.jpg",
            title: "华为技术有限公司",
            link: "",
          },
          {
            name: "张晓龙",
            avatar: "zhangxiaolong.jpg",
            title: "网宿科技有限公司",
            link: "",
          },
          {
            name: "张冬映",
            avatar: "zhangdongying.jpg",
            title: "厦门大学马克思学院行政人员",
            link: "",
          },
          {
            name: "郭伟",
            avatar: "guowei.jpg",
            title: "广州联通",
            link: "",
          },
        ],
        2015: [
          {
            name: "孙晔",
            avatar: "sunye.jpg",
            title: "阿里巴巴集团",
            link: "",
          },
          {
            name: "蒋怡勇",
            avatar: "jiangyiyong.jpg",
            title: "福州锐捷网络",
            link: "",
          },
          {
            name: "陈金楚",
            avatar: "chenjinchu.jpg",
            title: "中信银行",
            link: "",
          },
          {
            name: "陈欣",
            avatar: "chenxin.jpg",
            title: "厦门招商银行",
            link: "",
          },
          {
            name: "刘伟骏",
            avatar: "liuweijun.jpg",
            title: "国家无限电监测中心",
            link: "",
          },
        ],
        2016: [
          {
            name: "陈丽琴",
            avatar: "chenliqin.jpg",
            title: "长城国瑞",
            link: "",
          },
          {
            name: "陈人楷",
            avatar: "chenrenkai.jpg",
            title: "国家电网",
            link: "",
          },
          {
            name: "王家坤",
            avatar: "wangjiakun.jpg",
            title: "厦门网宿科技",
            link: "",
          },
          {
            name: "李王明卉",
            avatar: "liwangminghui.jpg",
            title: "直博",
            link: "",
          },
          {
            name: "王薇",
            avatar: "wangwei.jpg",
            title: "唯品会",
            link: "",
          },
          {
            name: "吴锐文",
            avatar: "wuruiwen.jpg",
            title: "上海招商银行信用卡中心",
            link: "",
          },
          {
            name: "张征",
            avatar: "zhangzheng.jpg",
            title: "福州联迪商用",
            link: "",
          },
          {
            name: "赵彤",
            avatar: "zhaotong.jpg",
            title: "华为",
            link: "",
          },
          {
            name: "周赛亚",
            avatar: "zhousaiya.JPG",
            title: "华为",
            link: "",
          },
          {
            name: "陈伟涛",
            avatar: "chenweitao.jpg",
            title: "腾讯",
            link: "",
          },
        ],
        2017: [
          {
            name: "陈曦",
            avatar: "chenxi.jpg",
            title: "部队",
            link: "",
          },
          {
            name: "胡宇雯",
            avatar: "huyuwen.jpg",
            title: "华为(special offer)",
            link: "",
          },
          {
            name: "林炜",
            avatar: "linwei.jpg",
            title: "美图秀秀",
            link: "",
          },
          {
            name: "刘新",
            avatar: "liuxin.jpg",
            title: "华为(special offer)",
            link: "",
          },
          {
            name: "丘琴秀",
            avatar: "qiuqinxiu.jpg",
            title: "网宿科技",
            link: "",
          },
          {
            name: "王秋红",
            avatar: "wangqiuhong.jpg",
            title: "厦航",
            link: "",
          },
          {
            name: "吴凡",
            avatar: "wufan.JPG",
            title: "厦航",
            link: "",
          },
          {
            name: "吴佳雯",
            avatar: "wujiawen.jpg",
            title: "厦门大学信息学院",
            link: "",
          },
          {
            name: "吴文磊",
            avatar: "wuwenlei.jpg",
            title: "腾讯(special offer)",
            link: "",
          },
          {
            name: "曾益清",
            avatar: "zengyiqing.jpg",
            title: "福州瑞芯微有限公司",
            link: "",
          },
          {
            name: "朱攀",
            avatar: "zhupan.jpg",
            title: "华为(special offer)",
            link: "",
          },
        ],
        2018: [
          {
            name: "蔡淑莲",
            avatar: "caishulian.JPG",
            title: "建行厦门开发中心",
            link: "",
          },
          {
            name: "杜宝林",
            avatar: "dubaolin.jpg",
            title: "上汽大众",
            link: "",
          },
          {
            name: "黄佳斌",
            avatar: "huangjiabin.jpg",
            title: "字节跳动",
            link: "",
          },
          {
            name: "林质锐",
            avatar: "linzhirui.jpg",
            title: "美图",
            link: "",
          },
          {
            name: "凌梅",
            avatar: "lingmei.jpg",
            title: "网宿科技",
            link: "",
          },
          {
            name: "孟俊彪",
            avatar: "mengjunbiao.jpg",
            title: "TCL",
            link: "",
          },
          {
            name: "王超",
            avatar: "wangchao.jpg",
            title: "科大讯飞",
            link: "",
          },
          {
            name: "杨骏峰",
            avatar: "yangjunfeng.jpg",
            title: "旷视Face++",
            link: "",
          },
          {
            name: "赵彦杰",
            avatar: "zhaoyanjie.jpg",
            title: "招银网络科技",
            link: "",
          },
          {
            name: "郑翰",
            avatar: "zhenghan.jpg",
            title: "腾讯（SSP）",
            link: "",
          },
        ],
        2019: [
          {
            name: "陈浩鹏",
            avatar: "chenghaopen.jpg",
            title: " ",
            link: "",
          },
          {
            name: "陈云舒",
            avatar: "chengyunshu.JPG",
            title: " ",
            link: "",
          },
          {
            name: "樊志文",
            avatar: "fanzhiwen.JPG",
            title: " ",
            link: "https://zhiwenfan.github.io/",
          },
          {
            name: "何福金",
            avatar: "hefujin.JPG",
            title: " ",
            link: "",
          },
          {
            name: "梁伯荣",
            avatar: "liangborong.jpg",
            title: " ",
            link: "",
          },
          {
            name: "舒炳林",
            avatar: "shubinglin.jpg",
            title: " ",
            link: "",
          },
          {
            name: "唐圳",
            avatar: "tangzhen.jpg",
            title: " ",
            link: "",
          },
          {
            name: "王继天",
            avatar: "wangjitian.jpg",
            title: " ",
            link: "",
          },
          {
            name: "吴华峰",
            avatar: "wuhuafeng.jpg",
            title: " ",
            link: "",
          },
          {
            name: "余宪",
            avatar: "yuxian.JPG",
            title: " ",
            link: "",
          },
        ],
        2020: [
          {
            name: "陈超奇",
            avatar: "chenchaoqi.jpg",
            title: "",
            link: "",
          },
          {
            name: "董成威",
            avatar: "dcw.jpg",
            title: "",
            link: "",
          },
          {
            name: "江明辉",
            avatar: "jmh.jpg",
            title: "",
            link: "",
          },
          {
            name: "李斐",
            avatar: "lifei.jpg",
            title: "",
            link: "",
          },
          {
            name: "罗琰",
            avatar: "ly.jpg",
            title: "",
            link: "",
          },
          {
            name: "林子煌",
            avatar: "lzh.jpg",
            title: "",
            link: "",
          },
          {
            name: "刘振卫",
            avatar: "lzw.jpg",
            title: "",
            link: "",
          },
          {
            name: "马文骜",
            avatar: "mwa.JPG",
            title: "",
            link: "",
          },
          {
            name: "孙琦",
            avatar: "sq.jpg",
            title: "",
            link: "",
          },
          {
            name: "王杰祥",
            avatar: "wangjiexiang.jpg",
            title: "",
            link: "",
          },
          {
            name: "吴亚文",
            avatar: "wyw.jpg",
            title: "",
            link: "",
          },
          {
            name: "谢伟平",
            avatar: "xwp.jpg",
            title: "",
            link: "",
          },
          {
            name: "邢翔瑞",
            avatar: "xxr.jpg",
            title: "",
            link: "",
          },
          {
            name: "庄铭泳",
            avatar: "zhuangmingyong.JPG",
            title: "",
            link: "",
          },
        ],
        2021: [
          {
            name: "陈旭恒",
            avatar: "chenxuheng.jpg",
            title: "",
            link: "",
          },
          {
            name: "郭慧敏",
            avatar: "guohuimin.jpg",
            title: "",
            link: "",
          },
          {
            name: "黄鸿宇",
            avatar: "huanghongyu.jpg",
            title: "",
            link: "",
          },
          {
            name: "李彦龙",
            avatar: "liyanlong.jpg",
            title: "",
            link: "",
          },
          {
            name: "潘婕",
            avatar: "panjie.jpg",
            title: "",
            link: "",
          },
          {
            name: "齐琦",
            avatar: "qiqi.jpg",
            title: "",
            link: "",
          },
          {
            name: "文艺",
            avatar: "wenyi.jpg",
            title: "",
            link: "",
          },
          {
            name: "章云龙",
            avatar: "zhangyunlong.jpg",
            title: "",
            link: "",
          },
          {
            name: "周融",
            avatar: "zhourong.jpg",
            title: "",
            link: "",
          },
          {
            name: "曾伟宏",
            avatar: "zengweihong.jpg",
            title: "",
            link: "",
          },
        ],
        2022: [
          {
            name: "成欣",
            avatar: "chengxin.jpg",
            title: "",
            link: "",
          },
          {
            name: "董琦",
            avatar: "dongqi.jpg",
            title: "",
            link: "",
          },
          {
            name: "李宸鑫",
            avatar: "lichenxin.jpg",
            title: "",
            link: "",
          },
          {
            name: "梁哲涵",
            avatar: "liangzhehan.jpg",
            title: "",
            link: "",
          },
          {
            name: "林鑫",
            avatar: "linxin.jpg",
            title: "",
            link: "",
          },
          {
            name: "刘小煜",
            avatar: "liuxiaoyu.jpg",
            title: "",
            link: "",
          },
          {
            name: "伍健雄",
            avatar: "wujianxiong.png",
            title: "",
            link: "",
          },
          {
            name: "史良超",
            avatar: "dabai.jpg",
            title: "",
            link: "",
          },
          {
            name: "郑泽镖",
            avatar: "zhengzebiao.jpg",
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
  /* 自动换行并自动平均分配宽度 */
  gap: 15px;
  /* 可以添加适当的间距 */
  text-align: center;
}

.name {
  font-size: 15px;
}

.year,
.title {
  font-size: 12px;
}
</style>
