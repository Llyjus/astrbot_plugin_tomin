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




1. Use ````help```` or ````help```` to view the command system.
2. Use ````check-in````, ````dk````, ````sign-in```` or ````qd```` for daily free recruitment. Cooldown time is 4 hours, maximum 5 times per day, cooldown resets the next day.
3. 
   - Use ````recruit```` or ````zm```` to recruit characters with the default minimum of 10 funds;
   - Use ````recruit x```` (where x is the fund amount) to recruit with up to 100 funds at once. Each additional fund increases the fixed probability of characters with rarity over 2 appearing;
   - Use ````recruit x n```` (where n is the number of times) to perform multiple recruitments in a single command. For example, spending 100 funds for one recruitment, the probabilities are:

      | Rarity | Probability |
      |--------|-------------|
      | 1      | 0%          |
      | 2      | 2%          |
      | 3      | 37%         |
      | 4      | 28%         |
      | 5      | 24%         |
      | 6      | 10%         |

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


- Detailed Overview

      1. **Architecture**: This project adopts a layered architecture design. Except for the interface layer, it does not depend on astrbot, achieving a migratable system with good portability and reusability. The overall architecture consists of 4 layers: Interface Layer, Application Layer, Logic Layer, and Data Layer.
      2. **Data Layer**: The data layer uses SQLite3 for local lightweight data storage. The database is encapsulated through a unified interface, making it easy to migrate later if the user base grows or based on development requirements.
      3. **Logic Layer**: The logic layer interacts with both the data layer and application layer, responsible for implementing specific individual tasks, such as accessing user data, generating cards, etc. Each logic component is not coupled with others and is only invoked through explicit interfaces.
      4. **Application Layer**: The application layer receives standardized input from the interface layer and calls the logic layer to indirectly perform database operations and execute logic (e.g., generating cards), then returns results to the interface layer. Currently, the application layer only supports structured data input. In the future, if support for multi-language or cross-process interface interaction is needed, universal data formats like JSON can be further introduced.
      5. **Interface Layer**: Receives frontend information and performs basic validation (such as data types, formats, and required fields). Upon validation, it calls the application layer for processing and returns the result to the caller.

---

## Contributing

Feel free to report any issues or suggestions you encounter!

---

## License

MIT License

---

## Support

[About AstrBot](https://astrbot.app)


