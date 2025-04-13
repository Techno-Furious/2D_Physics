# 🚀 2D Physics Simulation

A fun and interactive 2D physics engine built with Python and Pygame that simulates realistic ball physics, collisions, and gravity effects.


## 🎮 Demo

Check out the simulation in action:

<img src="https://raw.githubusercontent.com/Techno-Furious/2D_Physics/main/demo/2D_Physics.gif" alt="2D Physics Demo">




## ✨ Features

- Realistic ball physics with proper momentum conservation
- Gravity simulation
- Wall collisions with bounce effects
- Ball-to-ball collision detection and response
- Interactive controls for adding and manipulating balls
- Visual effects for collisions

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Techno-Furious/2D_Physics.git
   cd 2D_physics
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

Run the simulation:
```bash
python main.py
```

### Controls:
- **Left Click**: Add a new ball(small size) at cursor position 
- **Right Click**: Add a new ball(big size) at cursor position 
- **Space**: Turn off gravity
- **G**: Turn on gravity
- **WASD**: Control overall acceleration
- **R**: Reset the simulation


## 🔍 How It Works

This simulation implements core physics principles:
- Conservation of momentum in collisions
- Elastic and inelastic collisions
- Gravitational acceleration
- Friction and drag

This was just a small project for fun, so the physics may not be so accurate😅