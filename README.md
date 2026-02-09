# Tomin - 少女乐队游戏

Tomin是一个**AstrBot**的内置插件，是一个少女偶像乐队休闲游戏插件，包含抽卡、演出等功能，其它功能（比如肉鸽小游戏，活动系统）会在后续的开发中继续跟进，敬请期待。

🌐 **Languages / 语言**:  
[中文](README.md) | [English](README_en.md)

***Tips：***

<<<<<<< HEAD
=======
***当前版本核心游戏逻辑，接口层正在按按步骤开发中；目前暂时无法使用，仅供参考。***

>>>>>>> origin/develop
## 目录
1. [项目简介](#项目简介)
   - 介绍
   - 当前状态
      
2. [安装](#安装)
   - 版本需求
   - 安装方法

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

Tomin - 少女乐队游戏是 AstrBot的一个内置插件，玩家可以收集卡牌，组建自己的乐队进行演出。

<<<<<<< HEAD
=======
- 项目状态

***当前版本核心游戏逻辑，接口层正在按按步骤开发中；目前暂时无法使用，仅供参考。***
>>>>>>> origin/develop

## 安装

- 版本需求

```plaintext
astrbot >= 4.10.3
python >= 3.8.0
<<<<<<< HEAD
playwright>=1.41.0
```



## 安装方法

1. 在 AstrBot 插件市场中搜索「少女乐队游戏」并安装。

2. 通过 Git 克隆安装到 AstrBot 的 `data/plugins/` 目录：

```bash
git clone https://github.com/Llyjus/astrbot_plugin_Tomin
````

重启 AstrBot。

3. 下载本项目的 zip 压缩包并解压到 AstrBot 的 `data/plugins/` 目录。

重启 AstrBot。

---

## 依赖说明（Playwright / Chromium）

本插件使用 Playwright + Chromium 进行本地渲染截图。

安装 Python 依赖后，需要额外安装浏览器：

```bash
python -m playwright install chromium


---

## Docker / docker-compose 部署注意事项

如果使用 Docker 部署 AstrBot，必须在镜像构建阶段安装 Chromium（直接复制）：

```dockerfile
FROM soulter/astrbot:latest

RUN python -m pip install --no-cache-dir playwright
RUN python -m playwright install --with-deps chromium

```

同时建议为容器开启较大的共享内存，否则 Chromium 截图容易变慢或异常：

```yaml
shm_size: 1g
```

完整版可复制的docker compose yml内容：
```yaml
version: "3.8"

services:
  astrbot:
    build: .
    image: astrbot-playwright:latest
    shm_size: 1g
    container_name: astrbot
    restart: always
    ports:
      - "6185:6185"
      - "6199:6199"
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - ./data:/AstrBot/data
      - /etc/localtime:/etc/localtime:ro

```


---

## 说明

* 已移除原版本中的重量级依赖 `numpy`。




=======
```

- 安装方法

1. 在astrbot插件市场
搜索少女乐队游戏并安装。
2. 直接通过
```bash
git clone https://github.com/Llyjus/astrbot_plugin_Tomin
```
安装到AstrBot的```data/plugins/```目录。
重启astrbot。
3. 下载zip压缩包到AstrBot的```data/plugins/```目录。
重启astrbot。

- tips:原版本使用重量级依赖numpy，现已移除。
>>>>>>> origin/develop

## 功能模块

### 卡牌系统

- 概要

    本游戏卡牌系统分为两个部分：

<<<<<<< HEAD
   - 招募
      - 一个为免费的每日5次招募机会，还有一个为使用资金招募；
      - 使用资金抽卡可以增加消耗资金来增加获得高级角色的概率。
=======
   - 抽卡
      - 一个为免费的每日5次抽卡机会，还有一个为使用资源抽卡；
      - 使用资源抽卡可以增加消耗资源来增加获得高级角色的概率。
>>>>>>> origin/develop

      - 对于角色，目前角色拟定为6个等级，在无加成的情况下抽取概率为：

         | 稀有度  | 概率           |
         |--------|---------------|
<<<<<<< HEAD
         | 1      | 40%           |
         | 2      | 30%           |
         | 3      | 25%           |
         | 4      | 5%            |
         | 5      | 0%            |
         | 6      | 0%            |
=======
         | 1      | 29%           |
         | 2      | 35%           |
         | 3      | 19%           |
         | 4      | 10%           |
         | 5      | 6%            |
         | 6      | 1%            |
>>>>>>> origin/develop

   - 卡牌
      - 卡牌一共有7个属性（角色，所属乐队，位置，稀有度，综合力，速度以及抵抗值）。
      -  稀有度的增加会增强卡牌的综合力，技能以及抵抗值。但是卡牌的综合力，速度和抵抗值是在一定范围内随机的，符合正态分布。
<<<<<<< HEAD
      -  抵抗在负面效果下按概率生效。



- 指令

  1. `帮助` / `help` / `hp` / `bz`  
     查看指令系统。  
     支持不使用空格分隔指令和参数。  
     可以使用：

     ```
     帮助 [指令名称]
     ```

     查看某条指令的详细说明，例如：

     ```
     帮助 zm
     ```

  2. `打卡` / `dk` / `qd` / `签到`  
     进行每日免费招募。  
     冷却时间为 4 小时，每日最多 5 次，隔天重置冷却时间。

  3. 招募指令：

     - `招募` 或 `zm`  
       进行一次默认招募（默认花费 10 资金，次数 1）。

     - `招募 [资金] [次数]`  
       或  
       `zm[资金][x或空格][次数]`  

       例如：

       ```plaintext
       招募
       zm 20 3
       zm20x3
       ```

       表示每次花费 20 资金，进行 3 次招募。

       次数最多为 10 次。

       在无加成情况下，稀有度 1～6 的基础概率为：

       - 40%、30%、25%、5%、0%、0%

     - `招募 x`（x 为资金数量）

       单次招募最高可使用 50 资金。  
       每增加 5 资金，可提升稀有度大于 2 的角色出现概率。

       五星角色在 25 资金以上的招募中出现，  
       并在 40 资金时达到最大概率，不再增长；  
       六星角色在 40 资金以上的招募中出现。

       每 5 资金的概率提升为：

       | 稀有度 | 概率提升 / 5资金 |
       |------|----------------|
       | 1    | 0%             |
       | 2    | 12.5%          |
       | 3    | 10%            |
       | 4    | 7.5%           |
       | 5    | 5%             |
       | 6    | 5%             |

       当使用 50 资金进行一次招募时，稀有度 1～6 的概率为：

       | 稀有度 | 概率 |
       |------|----|
       | 1    | 0% |
       | 2    | 0% |
       | 3    | 35%|
       | 4    | 40%|
       | 5    | 15%|
       | 6    | 10%|

  4. 卡牌查询指令：

     - `查卡牌[id]` 或 `ckp[id]`  
       查看指定 id 的卡牌。

     - `查卡牌集` 或 `ckpj`  
       查看你拥有的所有卡牌。

     - 使用：

       ```
       查卡牌 乐队名称 稀有度
       ```

       可以筛选指定乐队或指定稀有度的卡牌。  
       乐队名称和稀有度均可以省略，也可以不使用空格。

       例如：

       ```
       查卡牌 roselia 4
       查卡牌4
       ```

  5. 出售指令：

     - `出售 卡牌id` 或 `cs 卡牌id`  
       出售单张卡牌。

     - `稀有度出售` / `x出售` / `xcs 稀有度`  
       批量出售指定稀有度及更低稀有度的所有卡牌。

       各稀有度出售价格如下：

       | 稀有度 | 价格 |
       |-------|-----|
       | 1     |  1  |
       | 2     |  3  |
       | 3     |  8  |
       | 4     |  40 |
       | 5     | 100 |
       | 6     | 150 |

       例如：

       ```
       xcs 3
       ```

       将出售所有稀有度 1、2、3 的卡牌。

  6. `资金` 或 `zj`  
     查询当前拥有的资金。

  7. 赠送指令：

     ```
     zs @xxx 卡牌id
     赠送 @xxx 卡牌id
     ```

     或使用 QQ 号进行赠送：

     ```
     zs qq号 卡牌id
     ```

     如果使用 QQ 号，中间需要用空格、`c` 或 `C` 进行分隔。


=======
      -  抵抗在对手的卡牌释放技能干扰自身的时候按概率可能会生效。


    - 指令
    
      1.  `帮助`或`help`来查看指令系统。
      2. `打卡`，`dk`，`签到`或`qd`来进行每日免费招募。冷却时间为4小时，每日最多5次，隔天重置冷却时间。
      3. 
         - `招募`或`zm`来花费默认最低10资金招募角色；
         - `招募 x`（x为资金数量）最高可一次使用50资金招募，每增加一点资金可提升固定比例的稀有度超过2的角色出现,具体为：

         | 稀有度  | 概率提升/5资金  |
         |--------|---------------|
         | 1      | 0%            |
         | 2      | 3%            |
         | 3      | 3%            |
         | 4      | 2%            |
         | 5      | 2%            |
         | 6      | 1%            |

         如若花费50资金进行一次招募，概率为：

         | 稀有度  | 概率  |
         |--------|------|
         | 1      | 0%   |
         | 2      | 5%   |
         | 3      | 34%  |
         | 4      | 26%  |
         | 5      | 22%  |
         | 6      | 9 %  |

         - `招募 x n`(n为次数)可在一次指令中进行多次抽取。
      4. 
         - `查卡牌`或`ckp`来查找拥有的所有卡牌；
         - `查卡牌 [乐队] [稀有度]`来筛选特定稀有度和乐队卡牌。可以省略空格和不填写任意一项。

      5. 
         - `出售 [卡牌id]`或`cs [卡牌id]`来出售卡牌。
         - `稀有度出售/x出售/xcs [稀有度]`来批量出售指定稀有度以及更低的所有卡牌。各稀有度卡牌价格为：
         | 稀有度  | 概率  |
         |--------|------|
         | 1      | 3    |
         | 2      | 5    |
         | 3      | 15   |
         | 4      | 40   |
         | 5      | 80   |
         | 6      | 200  |
      6. 
         `资金`或`zj`来查询自己拥有多少资金。
>>>>>>> origin/develop


### 演出系统(预实现)

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
- [x] 简单抽卡系统实现
- [x] 玩家交互，数据存储



### 阶段3 实现可用版本
- [x] 实现指令方法
- [x] 接口对接

### 后续开发规划
- [x] 角色拓展，演出功能实现
<<<<<<< HEAD
- [x] 完善UI(使用图片等展示抽卡结果)
- [ ] 打工系统
- [ ] 技能类实现
=======
- [ ] 技能类实现
- [ ] 完善UI(使用图片等展示抽卡结果，演出过程等等)
>>>>>>> origin/develop
- [ ] 肉鸽系统
- [ ] 活动系统

## 开发者文档
<<<<<<< HEAD

   > 文档说明
   > 本项目的系统架构设计、业务规则与代码实现为作者本人架构与实现， README 中的部分说明文字，基于本项目已有的系统设计与实现逻辑由作者整理项目特色与要点并在必要时借助 AI 进行语言润色与格式统一。  
   > AI 仅参与文档表达优化与中英文一致性处理，不参与系统设计与功能实现。

=======
>>>>>>> origin/develop
   - 项目架构:
```plaintext
.
├── app
<<<<<<< HEAD
│   ├── application
│   │   ├── cards_app.py
│   │   ├── funds_app.py
│   │   ├── gacha_app.py
│   │   └── __init__.py
│   ├── card_system
│   │   ├── cards.py
│   │   └── __init__.py
│   ├── data_management
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── init.py
│   │   ├── ports.py
│   │   └── repository
│   │       ├── connection.py
│   │       ├── repository.py
│   │       └── sql.py
│   ├── gacha
│   │   ├── characters.py
│   │   ├── gacha.py
│   │   ├── __init__.py
│   │   └── util.py
│   ├── infrastuctures
│   │   ├── images
│   │   │   ├── backgrounds
│   │   │   │   ├── background1.jpg
│   │   │   │   ├── background2.jpg
│   │   │   │   └── background3.jpg
│   │   │   └── cards
│   │   ├── __init__.py
│   │   ├── renderer
│   │   │   └── html_to_image.py
│   │   └── template
│   │       ├── templates
│   │       │   ├── base.css
│   │       │   ├── base.html
│   │       │   ├── cards.css
│   │       │   └── cards.html
│   │       └── templates_gen.py
│   ├── __init__.py
│   ├── interface
│   │   ├── app_interface.py
│   │   └── __init__.py
│   ├── live
│   │   └── __init__.py
│   ├── maintenance
│   │   ├── cleaner.py
│   │   ├── event.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── errors.py
│   │   ├── __init__.py
│   │   ├── inter_util
│   │   │   └── text_dict.py
│   │   └── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service.py
│   └── skills
│       └── __init__.py
├── __init__.py
=======
│   ├── application
│   │   ├── cards_app.py
│   │   ├── gacha_app.py
│   │   ├── __init__.py
│   │   └── init.py
│   ├── assets
│   │   └── images
│   │       ├── backgrounds
│   │       └── cards
│   ├── card_system
│   │   ├── cards.py
│   │   └── __init__.py
│   ├── data_management
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── init.py
│   │   ├── ports.py
│   │   └── repository
│   │       ├── connection.py
│   │       ├── repository.py
│   │       └── sql.py
│   ├── gacha
│   │   ├── characters.py
│   │   ├── gacha.py
│   │   ├── __init__.py
│   │   └── util.py
│   ├── __init__.py
│   ├── live
│   │   └── __init__.py
│   ├── maintenance
│   │   ├── cleaner.py
│   │   ├── event.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── errors.py
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service.py
│   └── skills
│       └── __init__.py
>>>>>>> origin/develop
├── LICENSE
├── main.py
├── metadata.yaml
├── pytest.ini
├── README_en.md
├── README.md
├── requirements.txt
└── tests
<<<<<<< HEAD
    ├── test_intergration
    │   ├── conftest.py
    │   ├── test_card_io.py
    │   └── test_database.py
=======
    ├── __init__.py
    ├── test_intergration
    │   ├── conftest.py
    │   ├── test_database.py
    │   └── test_gacha_in.py
>>>>>>> origin/develop
    └── test_unit
        ├── test_cleaner.py
        ├── test_db_init.py
        ├── test_gacha.py
        └── test_interface.py

<<<<<<< HEAD

=======
>>>>>>> origin/develop
```


### 一、整体架构设计

本项目采用分层架构（Layered Architecture），并严格控制依赖方向，核心目标是：  
在 AstrBot 插件形态下，实现一个可迁移、可测试、可演进的后端系统。

整体分为四层：

```

接口层（Interface）
↓
应用层（Application / Use Case）
↓
逻辑层（Domain / Service）
↓
数据层（Repository / Storage）

```

#### 1. 接口层（Interface Layer）

位于 `main.py`。

仅负责：

- 指令解析（正则 / 命令路由）
- 输入校验（Pydantic）
- 异常捕获与用户提示

不包含任何业务规则，不直接访问数据库。

接口层可以被视为一个 Adapter，AstrBot 只是其中一种接入方式。

---

#### 2. 应用层（Application Layer）

位于 `app/application`。

每个函数对应一个完整用例（Use Case）：

- `normal_gacha`：付费抽卡
- `free_gacha`：签到 + 免费抽卡

职责：

- 编排业务流程
- 控制事务边界
- 协调多个 Service 与 Repository

应用层是系统行为的唯一入口，接口层不能绕过它直接调用 Service 或 Repository。

---

#### 3. 逻辑层（Domain / Service Layer）

位于 `app/services`。

包含：

- `Fund_service`：资金校验与扣减规则
<<<<<<< HEAD
- `Card_service`：卡牌编号、槽位复用、检索与转让卡牌规则
=======
- `Card_service`：卡牌编号、槽位复用规则
>>>>>>> origin/develop
- `Sign_in_service`：签到次数 / 冷却逻辑

特点：

- 不感知接口形态
- 不管理事务
- 只表达业务规则

该层可被复用于 Web API / 定时任务 / 其它游戏接口。

---

#### 4. 数据层（Repository Layer）

位于 `app/data_management`。

使用 SQLite 实现，但通过 Repository + Protocol（ports）解耦。

特点：

- Repository 只负责数据访问，不包含业务语义
- 事务由外层 `connection()` 统一控制
- 所有数据库异常被转换为领域 / 基础设施异常

后续可无侵入迁移到 PostgreSQL / MySQL。

---

### 二、关键机制说明

#### 1. 幂等设计（失败也不允许重试）

系统采用**事件先落库的强幂等策略**：

- 每条用户消息使用 `message_id` 作为幂等键
- 在任何业务处理前，先写入 `events` 表
- `event_id` 为主键，重复请求直接触发唯一键冲突

设计取舍说明：

- 当前策略为：**失败也不允许重试**
- 适用于聊天机器人场景，避免重复扣费、重复发奖
- 若未来需要支持“失败可重试”，可将事件提交延后或拆分事务

---

#### 2. 事务边界设计

- 使用 `contextmanager` 封装数据库连接
- 每个用例在应用层显式控制事务范围
- 任一异常触发 rollback，避免部分成功状态
<<<<<<< HEAD
- 操作与查询返回结果隔离，保证不因查询返回结果失败而影响数据操作本身
=======

>>>>>>> origin/develop
---

#### 3. 抽卡与数值系统解耦

- 抽卡逻辑位于 `app/gacha`
- 数值计算、概率分布集中在 `util` 中

抽卡模块具有以下特性：

- 不依赖数据库
- 不依赖 AstrBot
- 可单独测试、复用或替换

<<<<<<< HEAD

#### 4. 应用层输出接口与接入层解耦

应用层对外仅暴露统一的结果结构，不直接依赖 AstrBot 的消息对象或返回格式。

应用层与接口层之间，统一使用字典（`dict`）作为数据交换格式，由接口层负责将结果转换为 AstrBot 所需的输出形式。

设计目的：

- 应用层保持纯业务语义，不感知任何平台协议
- 接口层仅承担适配职责（格式化文本、图片、富消息等）
- 当接入其它平台（如 Web API / 其它机器人框架）时，仅需替换接口层的结果渲染与输出格式，无需修改应用层与业务逻辑

该设计保证了从应用层到接口层的稳定边界，使系统具备较好的可移植性与可扩展性。


#### 5. 图片渲染与输出格式扩展机制

系统支持在接口层对业务结果进行本地图片渲染，用于展示卡牌列表与结果界面，提升用户可读性与交互体验。

设计要点：

- 渲染逻辑与业务逻辑完全解耦，仅依赖应用层返回的数据结构
- 同一业务结果可输出为：
  - 纯文本格式
  - 图片格式

为提高系统稳定性与容错能力：

- 图片渲染设有超时控制
- 当图片渲染失败或超时时，自动降级返回文本结果

该机制保证了展示层的失败不会影响核心业务流程，从而避免因渲染异常导致用户操作失败。


=======
>>>>>>> origin/develop
---

### 三、可测试性设计

本项目在设计阶段即考虑测试友好性：

- 使用 `pytest` 作为测试框架
- Repository 层使用 in-memory SQLite 进行隔离测试
<<<<<<< HEAD
- Gacha 模块与astrbot接口层通过依赖注入（fake gacha / fake rarity）实现确定性测试
=======
- Gacha 模块通过依赖注入（fake gacha / fake rarity）实现确定性测试
>>>>>>> origin/develop

覆盖内容包括：

- 数据库 CRUD
- 幂等逻辑
- 事务回滚
- 资金边界条件
- 冷却与次数限制

<<<<<<< HEAD
- 图片渲染模块仅用于展示层输出，不参与业务决策与事务流程，当前未纳入自动化测试范围


=======
>>>>>>> origin/develop
---

### 四、已知限制与后续演进

- SQLite 并发能力有限，适合当前小群场景
- Cleaner 为进程内定期清理，非分布式任务
<<<<<<< HEAD
- 内部实现取决于db_path的绝对路径，后续如有迁移需求则更改为外部接口层注入路径来优化可迁移属性
=======
- 抽卡概率采用阈值模型，非权重表
>>>>>>> origin/develop

---

### （结构变更说明）

- 合并开发者文档
<<<<<<< HEAD
- 新增「关键机制」「可测试性」「限制与演进」等章节
=======
- 新增「关键机制」「可测试性」「限制与演进」章节
>>>>>>> origin/develop
- 不影响玩家内容，仅面向开发者



## 贡献

欢迎提出你遇到的任何问题！


## 许可证

MIT License


# 支持

[关于AstrBot](https://astrbot.app)

