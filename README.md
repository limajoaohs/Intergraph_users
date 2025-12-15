# Yelp Graph Intersection

This project implements a graph analysis tool using NetworkX to identify and map interactions across different Yelp datasets. The core functionality merges two distinct graphs by isolating users present in both datasets and reconstructing their connections to reviewed businesses.

## Overview

The main algorithm, `intergraph_users`, accepts two NetworkX graph objects. It filters for users active in both source graphs and generates a new graph containing:
1. The common users.
2. All businesses associated with these users from both original datasets.
3. The edges representing the reviews/interactions.

This approach allows for the analysis of user behavior across different geographic locations or data subsets without merging the entire dataset.

## Project Structure

* `intergraph_users.py`: Contains the core logic for the graph intersection.
* `main.py`: A script to run the analysis and visualize the resulting graph using Matplotlib.
* `setup_graphs.py`: A utility script to generate the necessary `.graphml` data files for testing (mocks the structure of Yelp data).
* `requirements.txt`: List of dependencies.

## Setup and Usage

### 1. Install Dependencies
Ensure you have Python 3 installed, then run:

```bash
pip install -r requirements.txt