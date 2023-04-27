# Genetic and Ant Colony Optimization: Some applications in transport engineering

This project is a review of the ant colony optimization algorithm and the genetic algorithm and their applications on transportation engineering.

Here you are going to find a brief review of the theoretical framework of these metaheuristic together with a deployment in python code. In addition, we are going to be talking about some of the application of these framework in the transportation engineering context
  
## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so genetic_algorithm_vehicle_routing can be imported.
    │
    ├── slides.pptx        <- Power Point presentation
    |
    └── genetic_algorithm_vehicle_routing  <- Source code for vehicle routing problem with genetic algorithm.
        ├── __init__.py    <- Makes genetic_algorithm_vehicle_routing a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts of different features of the models 
        │
        ├── tests          <- tests.
        |
        ├── utils          <- Scripts to help with common tasks.
        |    └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py
            
    └──ant_colony_salesman_problem <- Source code for Travelling salesman problem with ant colony optimization.
        ├── __init__.py    <- Makes ant_colony_salesman_problem a Python module.
        |
        ├── models         <- Scripts of different features of the models
        |
        └── tests          <- tests.
        


---
