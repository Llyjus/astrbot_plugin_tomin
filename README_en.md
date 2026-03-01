![CI](https://github.com/Llyjus/astrbot_plugin_tomin/actions/workflows/main.yml/badge.svg)

# Tomin - Girls Band Game

This plugin is a **built-in plugin for AstrBot**, designed as a casual idol girls band game.  
It includes features such as card gacha and performances.  
Additional systems (such as a roguelike mini-game and event system) will be developed in future updates — stay tuned!

🌐 **Languages / 语言**:  
[中文](README.md) | [English](README_en.md)

***Tips:***

***The current version only contains the core game logic. The interface layer is still under step-by-step development. The plugin is NOT usable at the moment and is for reference only.***
***The English README file is almost translated by AI from the zh. version. ***
---




## Table of Contents
1. [Project Overview](#project-overview)
   - Introduction  
   - Current Status  

2. [Installation](#installation)
   - Version Requirements  
   - Installation Methods(Linux/MacOS User Must Read!!!)

3. [Game Modules (In Development)](#game-modules)
   - Currently Developing:
      - Card System
         - Overview
         - Commands
      - Performance System
         - Overview
         - Commands
      - Others
   - Future Plans

4. [Development Roadmap](#development-roadmap)

5. [Developer Documentation](#developer-documentation)
   - Project Structure
   - Overview Details

6. [Contributing](#contributing)

7. [License](#license)

8. [Support](#support)

---

## Installation

1. Install from the AstrBot plugin marketplace by searching for **“少女乐队游戏”**.

2. Install via Git (clone into AstrBot’s `data/plugins/` directory):

```bash
git clone https://github.com/Llyjus/astrbot_plugin_Tomin
```

Restart AstrBot after installation.

3. Alternatively, download the project ZIP and extract it into AstrBot’s `data/plugins/` directory.

Restart AstrBot after extraction.

---

## Dependencies and Deployment

This plugin uses **Playwright + Chromium** for local HTML-to-image rendering.

### Local Deployment

After installing Python dependencies from `requirements.txt`, you must also install the Chromium browser for rendering support:

```bash
python -m playwright install chromium
```

Currently, only the QQ platform is supported. However, when other platforms are supported, the adapter platform can be changed by modifying the default value.
```python
platform = str(os.getenv("PLATFORM", "qq"))
```

The rendering system defaults to a maximum concurrency of **2** and a render timeout of **15 seconds**.
If needed, these defaults can be adjusted by modifying the values in the `TominPlugin` initialization:

```python
max_renderer = int(os.getenv("RENDER_MAX_CONCURRENCY", "2"))
timeout_s = float(os.getenv("RENDER_TIMEOUT_S", "15"))
```

Changing the `2` and `15` parameters adjusts rendering concurrency and timeout.
Since browser rendering is CPU-intensive, a typical recommendation is:

> concurrency ≈ CPU cores × 0.6–0.8

For example, an 8-core CPU is typically suited for **4–6 concurrent renders**.

---

### Docker / docker-compose Deployment

If AstrBot is deployed using Docker, Chromium must be installed during the image build stage (copy directly):

```dockerfile
FROM soulter/astrbot:latest

RUN python -m pip install --no-cache-dir playwright
RUN python -m playwright install --with-deps chromium
```

It is also recommended to allocate sufficient shared memory to the container; otherwise, Chromium rendering may become slow or unstable:

```yaml
shm_size: 1g
```

The image rendering uses a browser engine (Chromium) and is CPU- and memory-intensive.
To avoid resource competition and system instability, the rendering system enforces default limits on concurrency and timeout:

* Default maximum render concurrency: **2**
* Default render timeout: **15 seconds**

These values can be configured via environment variables in `docker-compose`:

```yaml
- RENDER_MAX_CONCURRENCY=2
- RENDER_TIMEOUT_S=15
```

Currently, only the QQ platform is supported. However, when other platforms are supported, the adapter platform can be changed by modifying the default value.
```yaml
- PLATFORM="qq"
```
To use the forwarded paragraph messaging feature for QQ, you can add the following to the environment configuration:  
```yaml
- BOT_ID=xxx (your bot's QQ number)
- BOT_NAME=xxx (your bot's nickname; if an ID is provided but the name is not filled in, it defaults to Tomin)
```

Below is a complete, copyable example `docker-compose.yml` configuration:

```yaml
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
      - PLATFORM='qq'
      - RENDER_MAX_CONCURRENCY=6
      - RENDER_TIMEOUT_S=15
    volumes:
      - ./data:/AstrBot/data
      - /etc/localtime:/etc/localtime:ro
```

---

## Game Modules

### Card System

#### Overview

The card system consists of two parts:

- **Gacha System**
- 5 free draws per day.
- Resource-based draws.
- Resource-based draws allow increased consumption to raise the probability of obtaining high-rarity characters.

Planned rarity tiers (6 levels) with default probabilities:

| Rarity | Probability |
|------|------------|
| 1 | 29% |
| 2 | 35% |
| 3 | 19% |
| 4 | 10% |
| 5 | 6% |
| 6 | 1% |

- **Cards**
- Each card has 7 attributes:
   - Character
   - Band affiliation
   - Position
   - Rarity
   - Overall Power
   - Speed
   - Resistance

- Higher rarity increases overall power, skills, and resistance. Overall power, speed, and resistance are randomly generated within a range and follow a normal distribution. Resistance has a probability to activate when opposing cards attempt to interfere using skills.

- Commands

  1. `帮助` / `help` / `hp` / `bz`  
     Show the command help system.  
     This bot supports commands and parameters without spaces.

     You can use:

     ```
     帮助 [command]
     ```

     to view the detailed help of a specific command.  
     For example:

     ```
     帮助 zm
     ```

  2. `打卡` / `dk` / `qd` / `签到`  
     Perform a free daily recruitment.  
     Cooldown is 4 hours, up to 5 times per day.  
     The cooldown is reset on the next day.

  3. Recruitment commands:

     - `招募` or `zm`  
       Perform one recruitment with default settings  
       (costs 10 funds, 1 time).

     - `招募 [funds] [times]`  
       or  
       `zm[funds][x or space][times]`

       Examples:

       ```
       招募
       zm 20 3
       zm20x3
       ```

       This means spending 20 funds per draw, and performing 3 draws.

       The maximum number of draws per command is 10.

       Without any bonus, the base probabilities for rarity 1–6 are:

       - 40%, 30%, 25%, 5%, 0%, 0%

     - `招募 x` (x is the amount of funds)

       A single recruitment can use up to 50 funds.  
       For every additional 5 funds, the appearance rate of characters
       with rarity higher than 2 will be increased.

       5-star characters start appearing when the cost is above 25 funds,  
       and reach the maximum probability at 40 funds (no longer increases).  
       6-star characters start appearing when the cost is above 40 funds.

       Probability increase for every 5 funds:

       | Rarity | Increase per 5 funds |
       |------|---------------------|
       | 1    | 0%                  |
       | 2    | 12.5%               |
       | 3    | 10%                 |
       | 4    | 7.5%                |
       | 5    | 5%                  |
       | 6    | 5%                  |

       When using 50 funds for one recruitment, the probabilities for
       rarity 1–6 are:

       | Rarity | Probability |
       |------|-------------|
       | 1    | 0%          |
       | 2    | 0%          |
       | 3    | 35%         |
       | 4    | 40%         |
       | 5    | 15%         |
       | 6    | 10%         |

  4. Card query commands:

     - `查卡牌[id]` or `ckp[id]`  
       View a specific card by its ID.

     - `查卡牌集` or `ckpj`  
       View all cards you own.

     - Using:

       ```
       查卡牌 band_name rarity
       ```

       You can filter cards by band name and/or rarity.  
       Both band name and rarity are optional, and spaces can be omitted.

       Examples:

       ```
       查卡牌 roselia 4
       查卡牌4
       ```

  5. Sell commands:

     - `出售 card_id` or `cs card_id`  
       Sell a single card.

     - `稀有度出售` / `x出售` / `xcs rarity`  
       Sell all cards whose rarity is equal to or lower than the given rarity.

       Sell prices by rarity:

       | Rarity | Price |
       |------|-------|
       | 1    | 1     |
       | 2    | 3     |
       | 3    | 8     |
       | 4    | 40    |
       | 5    | 100   |
       | 6    | 150   |

       Example:

       ```
       xcs 3
       ```

       This will sell all cards with rarity 1, 2 and 3.

  6. `资金` or `zj`  
     Check your current funds.

  7. Gift command:

     ```
     zs @xxx card_id
     赠送 @xxx card_id
     ```

     Or gift by using a QQ number:

     ```
     zs qq_number card_id
     ```

     When using a QQ number, you must separate the QQ number and the card ID
     with a space, `c`, or `C`.

   8. Work Command

   `work [card_id] [location] [duration]` or `wk [card_id] [location] [duration]` allows cards to start working.

   - Location keywords are as follows:
   | Store Name | Target ID | Aliases |
   |---------|--------|------|
   | Ramen Shop | wutagawa_laamen | wtgw, wutagawa, ramen, ramen_shop, lm, lmg |
   | Hot Spring Inn | rokka_onsenryokan | hot_spring, hot_spring_inn, wq, wqlg, rokka, six_flowers, lock |
   | Amusement Park | Tsurumaki_amusement_park | tsurumaki, trmk, amusement_park, yly, tsurumaki |
   | Yoshinoya | Yoshinoya | yoshinoya, ysny, jyj |
   | STARRY | STARRY | starry |

   Examples:
   
   `work 123 bakery 3`
   `wk123bkr3`
   `wk 123 ymbk`

   - If no duration is specified, the default work duration is 3 hours. After work ends, it needs to be manually concluded.

   - Base wage is 2 funds per hour, with a maximum of 3 cards working simultaneously;
   Each member receives wage bonuses based on work location and rarity;
   Wages are halved after working continuously for more than 3 hours.
   Cards with rarity 4, 5, and 6 receive 1.5x, 2x, and 3x wage bonuses respectively.
   Specific work location bonuses are as follows:

   | Store Name | popipa | afterglow | roselia | hello_happy_world | pastel_palettes | morfonica | RAS | mygo | ave mujica | toge | kessoku band |
   |---------|--------|-----------|---------|-------------------|-----------------|-----------|-----|------|------------|------|--------------|
   | SPACE | 1.5 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | - | - |
   | CiRCLE | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | - | - |
   | RiNG | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.5 | 1.5 | - | - |
   | Yamabuki_Bakery | 1.5 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | - | - |
   | wutagawa_laamen | 1.2 | 1.5 | 1.5 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | - | - |
   | rokka_onsenryokan | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.5 | 1.2 | 1.2 | - | - |
   | Tsurumaki_amusement_park | 1.2 | 1.2 | 1.2 | 1.5 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | - | - |
   | Yoshinoya | - | - | - | - | - | - | - | - | - | 1.5 | - |
   | STARRY | - | - | - | - | - | - | - | - | - | - | 1.5 |

   9. Off Work Command

   - Command `offwork` or `ow` allows cards that have finished working to return to rest status.

   10. Work Status Command

   - Command `work status`/`wkst` or `wst` allows users to query their currently working and resting cards.

   11. Card Work Status Command

   - Command `card work status [card_id]`/`cdwkst[card_id]` or `cwst[card_id]`
   allows viewing the work status of a user's specific card ID.

   - Examples:

   `card work status 123`
   `cwst123`


### Performance System

#### Overview

- Players can participate in **daily solo performances** to earn resources based on performance scores (no manual operation required).
- Earned resources can be used for card gacha.
- Players can also compete against other players’ bands in **band battles**, comparing scores to obtain gacha resources.

#### ~~Commands~~

---

### Others

~~None at the moment~~

---

### Future Plans

After completing the basic version, a **roguelike system** and **event system** are planned for future updates. Stay tuned!

---

## Development Plan

### Phase 1: Foundation Architecture Implementation
- [x] Game concept design
- [x] System architecture
- [x] Project foundation architecture setup
- [x] Database structure setup

### Phase 2: Feature Implementation
- [x] Database creation (using SQLite for local storage in this small game; upgradeable based on requirements)
- [x] Basic gacha system implementation
- [x] Player interaction and data storage

### Phase 3: Usable Version Implementation
- [x] Command method implementation
- [x] Interface integration

### Future Development Plan
- [x] Character expansion and performance feature implementation
- [x] Working system
- [x] UI enhancement (using images to display gacha results etc.)
- [ ] performance system
- [ ] Roguelike system
- [ ] Event system

---

## Developer Documentation

### Project Structure

```plaintext
.
├── app
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
├── LICENSE
├── main.py
├── metadata.yaml
├── pytest.ini
├── README_en.md
├── README.md
├── requirements.txt
└── tests
    ├── test_intergration
    │   ├── conftest.py
    │   ├── test_card_io.py
    │   └── test_database.py
    └── test_unit
        ├── test_cleaner.py
        ├── test_db_init.py
        ├── test_gacha.py
        └── test_interface.py





```



## Developer Documentation


> Note  
> The system architecture, business rules, and all implementations of this project were designed and developed by the author.  
> Parts of this README were refined with the assistance of AI for wording and formatting, based strictly on the existing design and actual implementation of the project.  
> AI was only used as a documentation and language polishing tool, and was not involved in system design or feature implementation.



### I. Overall Architecture Design

This project adopts a layered architecture and strictly controls dependency directions.  
The core goal is to build a backend system that is portable, testable, and evolvable under the AstrBot plugin environment.

The system is divided into four layers:

```

Interface Layer
↓
Application Layer (Use Case)
↓
Domain / Service Layer
↓
Repository / Storage Layer

```

#### 1. Interface Layer

Located in `main.py`.

Responsibilities:

- Command parsing (regular expressions / command routing)
- Input validation (Pydantic)
- Exception handling and user-facing messages

This layer contains no business logic and does not access the database directly.

The interface layer can be regarded as an adapter.  
AstrBot is only one of the possible integration targets.

---

#### 2. Application Layer

Located in `app/application`.

Each function represents a complete use case:

- `normal_gacha`: paid gacha
- `free_gacha`: sign-in and free gacha

Responsibilities:

- Orchestrating business workflows
- Defining and controlling transaction boundaries
- Coordinating multiple Services and Repositories

The application layer is the single entry point of system behaviors.  
The interface layer must not bypass it to directly access Services or Repositories.

---

#### 3. Domain / Service Layer

Located in `app/services`.

Includes:

- `Fund_service`: fund validation and deduction rules
- `Card_service`: card numbering, slot reuse, card lookup and transfer rules
- `Sign_in_service`: sign-in count and cooldown rules

Characteristics:

- Independent of any interface or transport layer
- Does not manage transactions
- Only expresses business rules

This layer can be reused by Web APIs, scheduled jobs, or other game backends.

---

#### 4. Repository Layer

Located in `app/data_management`.

The current implementation uses SQLite, and is decoupled through Repository abstractions and Protocols (ports).

Characteristics:

- Repositories are responsible only for data access and contain no business semantics
- Transactions are centrally controlled by the outer `connection()` context
- All database exceptions are converted into domain or infrastructure-level exceptions

The storage backend can be migrated to PostgreSQL or MySQL without intrusive changes.

---

### II. Key Mechanisms

#### 1. Idempotency Design (No Retry Even on Failure)

The system adopts a strong idempotency strategy based on event pre-insertion:

- Each user message uses `message_id` as the idempotency key
- Before any business logic is executed, a record is inserted into the `events` table
- `event_id` is the primary key, and duplicate requests are rejected by a unique constraint violation

Design trade-offs:

- The current strategy does not allow retries, even when failures occur
- This is suitable for chatbot scenarios to prevent duplicated charges and rewards
- If retry-on-failure is required in the future, event submission can be delayed or split into separate transactions

---

#### 2. Transaction Boundary Design

- Database connections are wrapped using a `contextmanager`
- Each use case explicitly defines its transaction scope at the application layer
- Any exception triggers a rollback to avoid partial success
- Write operations and read-back queries are isolated, ensuring that failures in result queries do not affect data mutations

---

#### 3. Decoupling of Gacha Logic and Balancing System

- Gacha logic is implemented in `app/gacha`
- Numerical calculations and probability distributions are centralized in `util`

The gacha module has the following properties:

- Does not depend on the database
- Does not depend on AstrBot
- Can be independently tested, reused, or replaced

---

#### 4. Decoupling Between Application Output and Integration Layer

The application layer exposes a unified result structure and does not depend on AstrBot message objects or output formats.

All data exchanged between the application layer and the interface layer is represented as dictionaries (`dict`).  
The interface layer is responsible for converting the results into AstrBot-specific output formats.

Design goals:

- The application layer preserves pure business semantics and remains platform-agnostic
- The interface layer acts purely as an adapter (text formatting, image rendering, rich messages, etc.)
- When integrating with other platforms (such as Web APIs or other bot frameworks), only the interface layer needs to be modified

This design establishes a stable boundary between the application layer and the integration layer, improving portability and extensibility.

---

#### 5. Image Rendering and Output Format Extension

The system supports local image rendering at the interface layer for presenting card lists and result views, improving user experience and readability.

Design highlights:

- Rendering logic is completely decoupled from business logic and depends only on the data returned by the application layer
- The same business result can be rendered as:
  - plain text
  - images

To improve robustness and fault tolerance:

- Image rendering is protected by a timeout mechanism
- When rendering fails or times out, the system automatically falls back to text output

This ensures that failures in the presentation layer do not affect core business workflows.

---

### III. Testability Design

Testability is considered from the early design stage:

- `pytest` is used as the test framework
- The repository layer is tested in isolation using in-memory SQLite
- The gacha module and the AstrBot interface layer are tested through dependency injection (fake gacha / fake rarity) to achieve deterministic behavior

The test coverage includes:

- database CRUD operations
- idempotency logic
- transaction rollbacks
- fund boundary conditions
- cooldown and usage limits

- The image rendering module is only used for presentation purposes, does not participate in business decisions or transactions, and is currently excluded from automated testing.

---

### IV. Known Limitations and Future Evolution

- SQLite has limited concurrency capability and is suitable for small group scenarios
- The Cleaner runs as an in-process periodic task and is not a distributed job
- Some internal implementations currently depend on an absolute `db_path`; in the future, this can be refactored to use path injection from the interface layer to improve portability

---

### (Structure Change Notes)

- Developer documentation has been consolidated
- New sections such as “Key Mechanisms”, “Testability”, and “Limitations and Evolution” have been added
- Player-facing content is not affected; this documentation is intended for developers only



## Contributing

Feel free to report any issues or suggestions you encounter!

---

## License

MIT License

---

## Support

[About AstrBot](https://astrbot.app)


