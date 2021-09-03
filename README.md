# Matrix-py3

Python3 implementation of [cmatrix](https://github.com/abishekvashok/cmatrix) to generate "character falls". 

Matrix-py3 is adapted from [pmatrix](https://github.com/joechrisellis/pmatrix) that is well recommended if you prefer Python2.

It is noteworthy that a timer is added to matrix-py3 for a scheduled stop. 

![screenshot](https://github.com/chunribu/matrix-py3/raw/main/src/matrix.gif)

## Installation

+ with pip

```bash
pip install matrix-py3
```

+ with conda

```bash
conda install matrix-py3 -c conda-forge
```

## Usage

### Run independently

+ run in command line:

```bash
matrix # run until `Ctrl + C`
matrix 3 # run for 3 seconds
```
+ run in python:

```python
from matrix3 import matrix

matrix() # run until `Ctrl + C`
matrix(3) # run for 3 seconds
```
### Parallel with others

```bash
# NOT AVAILABLE YET
```

[TO DO]What's more, ~~matrix-py3 can be regarded as a screensaver parallel with other time-consuming programs.~~