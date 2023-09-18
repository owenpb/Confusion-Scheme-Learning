# Confusion-Scheme-Learning
## Detecting phase transition from Quantum Monte Carlo datasets using Convolutional Neural Networks

**Learning By Confusion** (LBC) is a machine learning technique for detecting phase transitions, first introduced by van Nieuwenberg <i>et. al.</i> in <i>"Learning phase transitions by confusion",</i> [Nature Physics 13, 435-439 (2017)](https://www.nature.com/articles/nphys4037). In recent years this method has been used to detect phase transitions in a variety of classical models in condensed matter physics such as the XY-model and the q-state Potts model, however its application to <i>Quantum</i> Monte Carlo datasets has not yet been fully explored. 

Here we explore the efficacy of various types of Quantum Monte Carlo datasets for discovering the phase transition in the Holstein model (a model of the electron-phonon interaction) via the LBC approach. We will implement confusion scheme learning by training Convolutional Neural Networks (CNNs) implemented in PyTorch.

This repository contains two main notebooks:

## [Methodology_and_Results.ipynb](https://github.com/owenpb/Confusion-Scheme-Learning/blob/main/Methodology_and_Results.ipynb) 
This notebook contains an overview of the model and the learning by confusion technique, and presents a summary of the main results.

## [Confusion-Scheme-CNN-PyTorch.ipynb](https://github.com/owenpb/Confusion-Scheme-Learning/blob/main/Confusion-Scheme-CNN-PyTorch.ipynb) 
This notebook contains an implementation of learning by confusion in PyTorch, for one particular set of training data (phonon field configurations).

Additionally, example output data from our Hybrid Monte Carlo simulations is provided in the **data** directory. Several useful functions for processing this data (to be used as input for our CNN classifier) are also provided in the **analysis_functions** directory.  
