# Matrix-py3

Python3 implementation of [cmatrix](https://github.com/abishekvashok/cmatrix) to generate "character falls". 

Matrix-py3 is adapted from [pmatrix](https://github.com/joechrisellis/pmatrix) that is well recommended if you prefer Python2.

It is also noteworthy that a timer is added to matrix-py3 for a scheduled stop. What's more, matrix-py3 can be regarded as a screensaver that runs parallel to other time-consuming programs.

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

+ in command line

```bash
matrix    # run until `Ctrl + C`
matrix 3  # run for 3 seconds
```
+ in python

```python
from matrix3 import matrix

matrix()  # run until `Ctrl + C`
matrix(3) # run for 3 seconds
```
### Run parallel to other programs

Add `coolmatrix` to the head of your commands. For example, `ping` is a command for testing a network connection. Assuming you want to run `ping 8.8.8.8 -c 10` , then run:

```bash
coolmatrix ping 8.8.8.8 -c 10
```

All the outputs can be recorded automatically in the file `cool.out` .

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=110 time=75.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=110 time=81.8 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=110 time=82.3 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=110 time=75.0 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 75.055/78.655/82.345/3.449 ms
```
