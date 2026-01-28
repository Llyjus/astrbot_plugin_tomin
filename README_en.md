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

## Project Overview

### Introduction

Tomin - Girls Band Game is a built-in plugin for AstrBot.  
Players can collect cards and form their own bands to participate in performances.

### Current Status

***The current version only contains core game logic. The interface layer is still under development.  
It is currently NOT usable and is for reference only.***

---

## Installation

### Version Requirements

```plaintext
 astrbot >= 4.10.3 
python >= 3.12.0 
```


### Installation Methods

1. Search for **Girls Band Game** in the AstrBot plugin marketplace and install it.
2. Clone directly via:
```bash
git clone https://github.com/Llyjus/astrbot_plugin_Tomin
```
Place it into AstrBot’s `data/plugins/` directory, then restart AstrBot.
3. Download the ZIP file and extract it into AstrBot’s `data/plugins/` directory, then restart AstrBot.

- Tips
If your system is Linux, you may be missing system-level dependencies required by numpy. For proper plugin functionality:

Linux users, please enter in terminal (copy directly):
```bash
sudo apt-get update
sudo apt-get install -y python3-dev build-essential
sudo apt-get install -y libblas-dev liblapack-dev gfortran
```
If you are a macOS user, please enter:
```bash
brew install openblas
export OPENBLAS=$(brew --prefix openblas)
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

#### Commands

1. Use ```help``` to view the command system.
2. Use ```check-in```, ```dk```, ```sign in```, or ```qd``` to perform daily free recruitment. Cooldown: 4 hours, maximum 5 times per day, resets daily.
3. 
   - Use ```recruit``` or ```zm``` to spend a minimum of 10 funds for recruitment.
   - ```recruit x``` (where x is the amount of funds) allows spending up to 100 funds per recruitment. Each additional fund increases the appearance rate of characters with rarity ≥2 by a fixed percentage, as shown below:

   | Rarity | Probability Increase per 10 Funds |
   |--------|----------------------------------|
   | 1      | 0%                               |
   | 2      | 3%                               |
   | 3      | 3%                               |
   | 4      | 2%                               |
   | 5      | 2%                               |
   | 6      | 1%                               |

   For example, spending 100 funds on one recruitment gives the following probabilities:

   | Rarity | Probability |
   |--------|-------------|
   | 1      | 0%          |
   | 2      | 2%          |
   | 3      | 37%         |
   | 4      | 28%         |
   | 5      | 24%         |
   | 6      | 10%         |

   - ```recruit x n``` (where n is the number of attempts) allows multiple recruitments in one command.

---

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
- [ ] Character expansion and performance feature implementation
- [ ] Skill system implementation
- [ ] UI enhancement (using images to display gacha results, performance processes, etc.)
- [ ] Roguelike system
- [ ] Event system

---

## Developer Documentation

### Project Structure

```plaintext
.
├── app
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
├── LICENSE
├── main.py
├── metadata.yaml
├── pytest.ini
├── README_en.md
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_intergration
    │   ├── conftest.py
    │   ├── test_database.py
    │   └── test_gacha_in.py
    └── test_unit
        ├── test_cleaner.py
        ├── test_db_init.py
        ├── test_gacha.py
        └── test_interface.py





```



## Developer Documentation

### 1. Overall Architecture Design

This project adopts a layered architecture with strict dependency direction control. The core goal is to:
In the form of an AstrBot plugin, implement a backend system that is migratable, testable, and evolvable.

The architecture is divided into four layers:

```

Interface Layer (Interface)
↓
Application Layer (Application / Use Case)
↓
Logic Layer (Domain / Service)
↓
Data Layer (Repository / Storage)

```

#### 1. Interface Layer

Located in `main.py`.

Responsibilities only include:
- Command parsing (regular expressions / command routing)
- Input validation (Pydantic)
- Exception handling and user feedback

Contains no business rules and does not directly access the database.

The interface layer can be viewed as an Adapter, with AstrBot being just one of many possible access methods.

---

#### 2. Application Layer

Located in `app/application`.

Each function corresponds to a complete use case:
- `normal_gacha`: Paid gacha
- `free_gacha`: Check-in + free gacha

Responsibilities:
- Orchestrating business processes
- Controlling transaction boundaries
- Coordinating multiple Services and Repositories

The application layer is the sole entry point for system behavior; the interface layer cannot bypass it to directly call Services or Repositories.

---

#### 3. Logic Layer (Domain / Service Layer)

Located in `app/services`.

Includes:
- `Fund_service`: Fund validation and deduction rules
- `Card_service`: Card numbering and slot reuse rules
- `Sign_in_service`: Check-in count / cooldown logic

Characteristics:
- Unaware of interface forms
- Does not manage transactions
- Only expresses business rules

This layer can be reused for Web APIs, scheduled tasks, or other game interfaces.

---

#### 4. Data Layer (Repository Layer)

Located in `app/data_management`.

Implemented using SQLite, but decoupled via Repository + Protocol (ports).

Characteristics:
- Repository only handles data access, no business semantics
- Transactions are uniformly controlled by the outer `connection()`
- All database exceptions are converted to domain / infrastructure exceptions

Can be migrated to PostgreSQL / MySQL non-intrusively in the future.

---

### 2. Key Mechanism Explanations

#### 1. Idempotence Design (No Retry on Failure)

The system adopts a **strong idempotence strategy with event-first persistence**:
- Each user message uses `message_id` as the idempotency key
- Before any business processing, the event is written to the `events` table first
- `event_id` is the primary key; duplicate requests directly trigger unique key conflicts

Design trade-off explanation:
- Current strategy: **No retry allowed even on failure**
- Suitable for chatbot scenarios to avoid duplicate deductions and rewards
- If "retry on failure" is needed in the future, event submission can be delayed or transactions can be split

---

#### 2. Transaction Boundary Design

- Uses `contextmanager` to encapsulate database connections
- Each use case explicitly controls transaction scope at the application layer
- Any exception triggers rollback to avoid partial success states

---

#### 3. Decoupling Gacha and Numerical Systems

- Gacha logic is located in `app/gacha`
- Numerical calculations and probability distributions are centralized in `util`

The gacha module has the following characteristics:
- No database dependency
- No AstrBot dependency
- Can be tested, reused, or replaced independently

---

### 3. Testability Design

This project is designed with testability in mind from the start:

- Uses `pytest` as the testing framework
- Repository layer uses in-memory SQLite for isolated testing
- Gacha module achieves deterministic testing via dependency injection (fake gacha / fake rarity)

Test coverage includes:
- Database CRUD
- Idempotence logic
- Transaction rollback
- Fund boundary conditions
- Cooldown and count limits

---

### 4. Known Limitations and Future Evolution

- SQLite has limited concurrency, suitable for small group scenarios
- Cleaner is an in-process periodic cleanup, not a distributed task
- Gacha probability uses a threshold model, not a weight table
- `numpy` is a numerical dependency, which can be replaced with a lightweight implementation in the future

---

### (Structural Change Notes)

- Merged the original "Project Architecture / Detailed Outline" into a unified "Developer Documentation"
- Added new sections: "Key Mechanisms", "Testability", "Limitations and Evolution"
- No impact on player-facing content, only for developers


## Contributing

Feel free to report any issues or suggestions you encounter!

---

## License

MIT License

---

## Support

[About AstrBot](https://astrbot.app)


