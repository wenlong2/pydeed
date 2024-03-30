## pydeed

A Python tool for retrieving Indeed job postings and filtering custom keywords.

## Key Features

- Query indeed.com with keywords and location.
- Save job meta information to a local file.
- Retrieve detailed information for each job and save it to a local text file.
- Filter jobs by excluding postings containing specific keywords.

## Installing

### Python 3.8 or higher is required

```
pip install git+https://github.com/wenlong2/pydeed
pip install --index-url https://test.pypi.org/simple/ pydeed
pip install -r requirements.txt
```

### Quick example

``` bash
python3 -m pydeed -j get -k Python -l California -n 5
python3 -m pydeed -j filter -e 'TS/SCI,US citizen,security clearance'
```
