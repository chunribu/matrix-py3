# Matrix-py3

Matrix-py3 is a python3 implementation of cmatrix to ganerate "character falls". Besides, a timer is added to matrix-py3 for a scheduled stop.

![screenshot](src/matrix.gif)

## Installation

`conda install matrix-py3 -c conda-forge`

or

`pip install matrix-py3`

## Usage

+ run in command line:

  ```bash
  matrix # run until `Ctrl + C`
  matrix 3 # run for 3 seconds
  ```
+ run in python:

  ```python
  from matrix3 import matrix

  matrix # run until `Ctrl + C`
  matrix(3) # run for 3 seconds
  ```
