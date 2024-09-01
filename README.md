# U.S. States Game

This Python game challenges players to name all 50 U.S. states. It uses the `turtle` graphics library for visual output and `pandas` for data handling.

## Overview

The game displays a map of the U.S. with blank states. Players input state names one by one. Correctly guessed states appear on the map, while incorrect or missing guesses are tracked. The game ends when all states are guessed or when the player chooses to exit.

## Features

- **Interactive Map**: Displays a U.S. map where correctly guessed states are labeled.
- **State Tracking**: Keeps track of correctly guessed states and shows the number of correct answers.
- **Missing States**: Generates a CSV file listing states that were not guessed.

## Prerequisites

- Python 3.x
- `turtle` module (comes pre-installed with Python)
- `pandas` library

You can install `pandas` using pip if it's not already installed:

    ```bash
    pip install pandas


## Files
- **blank_states_img.gif**: An image file representing the U.S. map with blank states. Place this file in the same directory as your script.
- **50_states.csv**: A CSV file containing state names and their coordinates. Make sure this file is in the same directory as your script.

## Code Description
### Setup:
- Initializes the Turtle graphics screen.
- Sets up the map image as the turtle shape.

### Game Loop:
- Prompts the player to guess a state.
- Checks if the guessed state is correct and not already guessed.
- Displays the state on the map if correct.
- Keeps track of the number of correct guesses.
- Allows the player to exit the game by typing 'exit'.

### End of Game:
- Identifies and saves states that were not guessed to a CSV file (missing_states.csv).
