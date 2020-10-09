# Duplicate File Finder

Python script to find duplicate files in given path.

## Usage

```bash
python dupsfinder.py <path_to_directory>
```

A file with name `duplicates.txt` will be created containing list of duplicate files.

# Benchmarks

## Test system specs:
- Ryzen 5 2500U @2 Ghz(base) and 3.6 Ghz(boost), 4 cores
- 8 GB DDR4 Ram
- 1 TB 5400 RPM HDD of western digital

### Test Directory : 4157 files taking 2 GB

#### Duplicates: 173 files taking 47.40 MB

* Average of 10 consecutive tests
  - User: 0.52s
  - Sys: 1.24s
  - Total: 3.046s

## Miscellaneous
- A very fast version of this script written in C can be found [here](https://github.com/yogeshsingh101200/dupsfinder).
- **Fun Fact**: This script took me weeks to write in C while it took only few hours in python.