# 少女乐队游戏

该插件是一个**AstrBot**的内置插件，是一个少女偶像乐队休闲游戏插件，包含抽卡、演出等功能，其它功能（比如肉鸽小游戏，活动系统）会在后续的开发中继续跟进，敬请期待。

🌐 **Languages / 语言**:  
[中文](README.md) | [English](README_en.md)

***Tips：***

***当前版本核心游戏逻辑，接口层正在按按步骤开发中；目前暂时无法使用，仅供参考。***

## 目录
1. [项目简介](#项目简介)
   - 介绍
   - 当前状态
      
2. [安装](#安装)
   - 版本需求
   - 安装方法(Linux/MacOS用户必读！！！)

3. [功能模块（开发中）](#功能模块)
   - 正在开发：
      - 卡牌系统
         - 概要
         - 指令
      - 演出系统
         - 概要
         - 指令
      - 其它
   - 后续开发规划

4. [开发规划](#开发规划)

5. [开发者文档](#开发者文档)
   - 项目架构
   - 细节概要


6. [贡献](#贡献)

7. [许可证](#许可证)

8. [支持](#支持)


## 项目简介

- 介绍

少女乐队游戏是 AstrBot的一个内置插件，玩家可以收集卡牌，组建自己的乐队进行演出。

- 项目状态

***当前版本核心游戏逻辑，接口层正在按按步骤开发中；目前暂时无法使用，仅供参考。***

## 安装

- 版本需求

```plaintext
astrbot >= 4.10.3
python >= 3.12.0
```

- 安装方法

1. 在astrbot插件市场
搜索少女乐队游戏并安装。
2. 直接通过
```bash
git clone https://github.com/Llyjus/girlsBandGame
```
安装到AstrBot的```data/plugins/```目录。
重启astrbot。
3. 下载zip压缩包到AstrBot的```data/plugins/```目录。
重启astrbot。

- Tips
如果您的系统是linux系统可能缺少numpy相关系统级依赖，为了正常使用该插件:
Linux用户请在终端输入（直接复制）：
```bash
sudo apt-get update
sudo apt-get install -y python3-dev build-essential
sudo apt-get install -y libblas-dev liblapack-dev gfortran
```
如果是MacOS用户请输入：
```bash
brew install openblas
export OPENBLAS=$(brew --prefix openblas)
```


## 功能模块

### 卡牌系统

- 概要

    本游戏卡牌系统分为两个部分：

   - 抽卡
      - 一个为免费的每日3次抽卡机会，还有一个为使用资源抽卡；
      - 使用资源抽卡可以增加消耗资源来增加获得高级角色的概率。

      - 对于角色，目前角色拟定为6个等级，在无加成的情况下抽取概率为：
| 稀有度 | 概率 |
|--------|------|
| 1      | 29%  |
| 2      | 35%  |
| 3      | 19%  |
| 4      | 10%  |
| 5      | 6%   |
| 6      | 1%   |
   - 卡牌
      - 卡牌一共有7个属性（角色，所属乐队，位置，稀有度，综合力，速度以及抵抗值）。
      -  稀有度的增加会增强卡牌的综合力，技能以及抵抗值。但是卡牌的综合力，速度和抵抗值是在一定范围内随机的，符合正态分布。
      -  抵抗在对手的卡牌释放技能干扰自身的时候按概率可能会生效。


    - ~~指令~~

### 演出系统

- 概要
    - 玩家可以通过每日单人演出，根据评分来获得资源（不需要玩家来操作）。该资源可以用于抽卡。
    - 同时玩家也可以和其它玩家的乐队进行对邦，比较分数高低，获得抽卡资源。

- ~~指令~~

###  其它

~~ 暂时没有 ~~

### 后续开发规划

在基础版本开发完毕后预计会增加肉鸽系统和活动系统，敬请期待~

## 开发规划

### 阶段1 基础架构实现
- [x] 游戏概念设计
- [x] 系统架构
- [x] 搭建项目基础架构
- [x] 搭建数据库结构

### 阶段2 功能实现
- [x] 数据库创建（基于本地存储数据的小游戏故使用sqlite，根据需求升级）
- [ ] 简单抽卡系统实现
- [ ] 玩家交互，数据存储
- [ ] 技能类实现
- [ ] 角色拓展，演出功能实现

### 阶段3 实现可用版本
- [ ] 实现指令方法
- [ ] 接口对接
- [ ] 完善UI(使用图片等展示抽卡结果，演出过程等等)

## 开发者文档
   - 项目架构
```plaintext

girls_band_game/
├── app
│   ├── application
│   │   └── __init__.py
│   ├── assets
│   │   └── images
│   │       ├── backgrounds
│   │       └── cards
│   ├── card_system
│   │   ├── cards.py
│   │   └── __init__.py
│   ├── data_management
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── init.py
│   │   ├── ports.py
│   │   └── services
│   │       ├── connection.py
│   │       ├── repository.py
│   │       └── sql.py
│   ├── gacha
│   │   └── __init__.py
│   ├── __init__.py
│   ├── live
│   │   └── __init__.py
│   └── skills
│       └── __init__.py
├── LICENSE
├── main.py
├── metadata.yaml
├── README_en.md
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_intergration
    │   ├── conftest.py
    │   └── test_database.py
    └── test_unit



```


   ~~- 细节概要~~


## 贡献

欢迎提出你遇到的任何问题！


## 许可证

MIT License


# 支持

[关于AstrBot](https://astrbot.app)

