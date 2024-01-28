# python-speedup
Python speedup references

## Pre-reqs

Python >= 3.10
virtualenv


## Instalation

 Inside your project directory do as following: 

 * Download the code(zip, `git clone`) - [https://github.com/bang/python-speedup](https://github.com/bang/python-speedup)
 
 * Setup `virtualenv` using the command: `python -mvirtualenv venv`
 
 * Activate `virtualenv` by the command:

   * Linux/Unix: `source venv/bin/activate`
   
   * Windows: `.\venv\Scripts\activate`

## Boilerplate examples

### [async_boilerplate.py](https://github.com/bang/python-speedup/blob/master/async_boilerplate.py)

Uses `asyncio` ecosystem to simulate multiple processings runnging in
concurrence.

### [joblib_boilerplate.py](https://github.com/bang/python-speedup/blob/master/joblib_boilerplate.py)

Uses `joblib` library to simulate multiple processing using
concurrence.

### [multiprocessing_bilerplate.py](https://github.com/bang/python-speedup/blob/master/multiprocessing_boilerplate.py)

Uses `multiprocessing` library to simulate multiple processing
using parallelism.

## HTTP request examples

### [asyncio_http_requests.py](https://github.com/bang/python-speedup/blob/master/asyncio_http_request.py)

Uses `asyncio` + `requests` to perform simple HTTP GET operations
in multiple URLs

### [joblib_http_requests.py](https://github.com/bang/python-speedup/blob/master/joblib_http_request.py)

Uses `joblib` + `requests` to perform simple HTTP GET operations
in multiple URLs

### [multiprocess_http_requests.py](https://github.com/bang/python-speedup/blob/master/multiprocessing_http_requests.py)

Uses `multiprocess` + `requests` to perform simple HTTP GET operations
in multiple URLs
