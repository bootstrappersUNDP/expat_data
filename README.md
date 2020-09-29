# pySocialWatcher
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
### A Social Data Collector from Facebook Marketing API
#### I'm more than pleased that many teams used this library. But I need your help to support it. Please feel free to pull requests that solve issues. Unfortunatelly, my time is very very limited to keep updating this repository.
#### If this package helps your research somehow, reference this paper:

```
@inproceedings{araujo2017facebook,
 author = {Araujo, Matheus and Mejova, Yelena and Weber, Ingmar and Benevenuto, Fabricio},
 title = {Using Facebook Ads Audiences for Global Lifestyle Disease Surveillance: Promises and Limitations},
 series = {WebSci '17},
 year = {2017},
 location = {Troy, USA},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {Facebook, Advertising, Epidemihology, Social Media, Health},
} 
```

 
[![Build Status](https://travis-ci.org/maraujo/pySocialWatcher.svg?branch=master)](https://travis-ci.org/maraujo/pySocialWatcher)
[![codecov](https://codecov.io/gh/maraujo/pySocialWatcher/branch/dev/graph/badge.svg)](https://codecov.io/gh/maraujo/pySocialWatcher)

**Package Name:** pysocialwatcher

**Facebook Ads API version supported:** 8.0

**License:** MIT

**Python Version:** 3.8


### What is this for
This package tries to get the full potencial of the Facebook Marketing API for Social Analysis research.
Recent works show that online social media has a huge potencial to provide interesting insights on trends of across demographic groups.

Examples of research question that it can answer:
* For each european country, get how many people are interested in Science?
* Get how many people in each GCC country who is Graduated AND is interested in Football, and how many is not interested in Football breakdown by: gender, age range, scholarity, language and citizenship.


##### Facebook Marketing API Refereces page:
Targeting Specs: https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.8

Ad Targeting Search API: https://developers.facebook.com/docs/marketing-api/targeting-search/v2.8
### Limitations:
* Current supported API fields are listed below:
    ```
    "interests",
    "behaviors",
    "education_statuses",
    "family_statuses",
    "relationship_statuses",
    "locales",
    "genders",
    "age_min",
    "age_max",
    "geo_locations"
    ```

### Install
    git clone https://github.com/maraujo/pySocialWatcher.git
    cd pySocialWatcher
    pip install -r requirements.txt
    python3 setup.py install
    
### Tips added by Tica
Create a separate virtual environment before installing all the pakcages.
    
    python3 -m venv env
    . env/bin/activate

### Quick Start
You should have a .csv file with your Facebook tokens and accountIDs.
Example: pySocialWatcher/pysocialwatcher/facebook_credentials_example.csv
  
    python3 pysocialwatcher/test_windows.py

or

    >>> from pysocialwatcher import watcherAPI 
    >>> watcher = watcherAPI() 
    >>> watcher.load_credentials_file("pysocialwatcher/credentials.csv")
    >>> watcher.run_data_collection("pysocialwatcher/input_examples/quick_example.json")

### How it works (slides):
Check the slides: https://goo.gl/WzE9ic

### Features
1. Static input json format to make you experiments easily reproducible.
2. Support multiple Facebook tokens.
3. Multiple tokens are processed in parallel to speedup data collection.
3. Complex logic queries in the Facebook Marketing API with 'or', 'and', 'not', for example:.
```
      "interests": [{
            "not": [6003442346642],
            "and": [6004115167424, 6003277229371],
            "name": "Not interested in Football, but interest in some physical activity"
        }
```
4. Automatically save the state every constants.SAVE_EVERY requests. If any problem happens you can load the incomplete file and continue the data collection (```load_data_and_continue_collection```)

