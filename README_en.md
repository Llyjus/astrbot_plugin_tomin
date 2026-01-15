# Girls Band Game

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
   - Installation Methods  

3. [Game Modules (In Development)](#game-modules)
   - Currently Developing:
      - Card System
         - Overview
         - ~~Commands~~
      - Performance System
         - Overview
         - ~~Commands~~
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

Girls Band Game is a built-in plugin for AstrBot.  
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
git clone https://github.com/Llyjus/girlsBandGame
```
Place it into AstrBot’s `data/plugins/` directory, then restart AstrBot.
3. Download the ZIP file and extract it into AstrBot’s `data/plugins/` directory, then restart AstrBot.

---

## Game Modules

### Card System

#### Overview

The card system is planned to consist of two parts:

- **Gacha System**
- Three free draws per day.
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

#### ~~Commands~~

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

## Development Roadmap

### Phase 1 – Core Architecture
- [x] Game concept design
- [x] System architecture design
- [ ] Project base structure setup
- [ ] Database schema design

### Phase 2 – Feature Implementation
- [ ] Database creation (SQLite for early versions, upgraded as needed)
- [ ] Basic gacha system
- [ ] Player interaction and data persistence
- [ ] Skill system implementation
- [ ] Character expansion and performance system

### Phase 3 – Usable Version
- [ ] Command implementation
- [ ] API integration
- [ ] UI improvements (image-based gacha results, performance displays, etc.)

---

## Developer Documentation

### Project Structure

```plaintext
girls_band_game/
├── core/
│   ├── assets/
│   ├── card_system/
│   │   └── __init__.py
│   ├── db_connect/
│   │   └── __init__.py
│   ├── gacha/
│   │   └── __init__.py
│   ├── live/
│   │   └── __init__.py
│   ├── skills/
│   │   └── __init__.py
│   └── test/
│       └── __init__.py
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py
├── metadata.yaml
├── README_en.md
└── README.md
```

~~ Detailed overview ~~

---

## Contributing

Feel free to report any issues or suggestions you encounter!

---

## License

MIT License

---

## Support

[About AstrBot](https://astrbot.app)


