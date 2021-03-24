# py_imgur_bruteforcer

A simple utility to find and download randomly found imgur images

## Features 
- CLI user interface
- Blazingly fast

## TODO
- Saving images to local filesystem
- Saving urls to .csv file

## Requirements
- requests library

## Command line syntax

```
bruteforcer.py [workers] [ext] [len] [type]

[workers] -> int, no. of workers
[ext] -> string,  filename extention - png, jpg, jpeg, gif
[len] -> int, lenght of imgur_id - 5 or 7
[type] -> int, type of id's to scan - 1: letters 2: digits 3: mixed

bruteforcer.py h, for help
```
