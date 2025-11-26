# FIFA Players Data Visualization

A Python-based data analysis and visualization project for FIFA player statistics.

## Overview

This project analyzes FIFA player data to visualize key metrics including age distribution, nationality representation, playing preferences, and performance ratings.

## Features

* Data cleaning and preprocessing of FIFA player statistics
* Age distribution analysis with histogram visualization
* Top 10 nationalities by player count (bar chart)
* Preferred foot distribution (pie chart)
* Age vs overall rating correlation (2D density heatmap)
* Scatterplot: Height (cm) vs Heading Accuracy
* Stripplot: Weight (kg) vs Acceleration
* Regression plot: Overall Rating vs Player Value (Euro)
* Joint plot combining Overall Rating, Value (Euro), and Preferred Foot

## Requirements

* Python 3.x
* pandas
* numpy
* matplotlib
* seaborn

## Installation

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

```bash
python main.py
```

## Data

The project uses `fifa_players.csv` containing player attributes and statistics.

## Visualizations

1. **Age Distribution**: Histogram showing player age frequency
2. **Top Nationalities**: Bar chart of countries with most players
3. **Preferred Foot**: Pie chart showing left vs right foot preference
4. **Age vs Rating**: 2D heatmap correlating player age with overall rating
5. **Height vs Heading Accuracy**: Scatterplot
6. **Weight vs Acceleration**: Stripplot
7. **Overall Rating vs Value**: Regression plot
8. **Joint Plot**: Rating, Value, and Preferred Foot relationships
