# A Bayesian Approach to a Batter's Pitch Mix

This repository contains code to predict the percentage of Fastballs, Breaking Balls, and Off-speed pitches that batters will see in 2024 based on pitch data from the 2021-2023 MLB seasons. Using Multinomial likelihoods, Dirichlet priors, and boostrap sampling, I have created bootstrap distributions predicting a batter's pitch mix in 2024.

## Project Files
- Data Folder
  - Contains all the data files to run the notebooks and Streamlit app
  - To run the notebooks, first unzip the Archive.zip file. This contains the original data file as well as a smaller file with data to train the model
- DataManipulation.ipynb
  - This notebook contains basic data exploration and manipulation for model creation
- Model.ipynb
  - This notebook contains the code to create the model and it's associated probability distributions
- app.py
  - The interactive Streamlit application. This app is available at [this site](https://batter-pitch-mix.streamlit.app/).
- Technical_Report.pdf
  - A brief technical description of the methodologies used for this model.
