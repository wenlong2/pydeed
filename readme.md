## pydeed

A python tool to retrieve indeed job postings for keyword filtering.

## Key Features

- query indeed.com with keywords and location
- save job meta information to a local file
- retrieve detailed information for each job and save it into local text file

## installing

### Python 3.8 or higher is required

```
pip install git+https://github.com/wenlong2/pydeed
pip install --index-url https://test.pypi.org/simple/ pydeed
pip install -r requirements.txt
```

### Quick example

``` bash
p3 -m pydeed -j get -k Python -l California -n 5
p3 -m pydeed -j filter -e 'TS/SCI,US citizen,security clearance'
```
