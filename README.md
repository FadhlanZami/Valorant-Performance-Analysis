# Franchise Valorant Player Champions Tour 2023-2024 Performance Analysis

# Valorant Player Performance Analysis

This repository contains a set of scripts for analyzing and predicting the performance of Valorant players based on their statistics. The project includes data preprocessing, filtering, and machine learning model creation using Python.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

The goal of this project is to analyze player performance in Valorant using data from multiple matches and tournaments. By classifying player performance into categories such as "Best Perform", "Normal Perform", and "Under Perform", the project aims to predict player performance based on various match statistics. The dataset used for this project is sourced from [Valorant Champion Tour 2021-2023 Data on Kaggle](https://www.kaggle.com/datasets/ryanluong1/valorant-champion-tour-2021-2023-data). The data contains detailed player statistics across multiple tournaments and match types.


## Installation

To get started, you'll need to install the required libraries. The following command will install all the necessary dependencies:
- pandas
- scikit-learn
- sqlite3
- joblib

## Usage

### 1. **Data Preprocessing**

- **File**: `data_preprocessing.py`
- **Functionality**: This script reads the raw dataset, handles missing values in both numerical and categorical columns, and saves the preprocessed data to a new file.

### 2. **Data Filtering**

- **File**: `Filtered_data.py`
- **Functionality**: This script filters the dataset based on match type and saves the filtered data.

### 3. **Performance Classification**

- **File**: `performance_classification.py`
- **Functionality**: This script classifies players' performance into categories based on their rating. It then builds a Random Forest model for predicting player performance using match statistics.

- ### 4. **Model Evaluation**

- **File**: `model_evaluation.py`
- **Functionality**: This script evaluates the Random Forest model using test data and outputs a classification report.
