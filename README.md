# Facebook Expats Data

## 1. Introduction
This depository is used to build the code and download Facebook data which serves as an input for the analysis and visualization of Serbian emigration. This account will be handed over to the UNDP team upon the completion of the project. The purpose of using the Facebook estimations is not to reproduce migration statistics, but rather to generate snapshots of the estimates of expatriates that could be used to measure emigration trends. Using social media in this regard can be a timely and low-cost source of information.  Our model will fetch new data every two months, which, we hope, will give a glimpse into the cross-border movement of the Serbian population. However, there are important methodological and data integrity issues with using social media data sources that we will discuss and address.  

## 2. Facebook API and data

We use data from the Facebook API to estimate the number of Serbian “expats” in countries around the world. "Expat" is Facebook's definition of a person who lived in one country ("home country"), but moved to another country. "Home country" in our case is Serbia, and host countries are all coutries recognized by Facebook's API. Additionally, we added additional parameters, such as age group, education, marriage status and gender. The API returns the estimates of the number of monthly active users of the FB platforms, which includes Facebook, Instagram, and Messenger. The estimates present a subset of the total population and need to be calibrated based on the official numbers. 


### 2.1 Fetching the data

To connect with the API, we used python library [pySocialWatcher](https://github.com/maraujo/pySocialWatcher/blob/master/README.md).

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
**License:** MIT


##### Facebook Marketing API Refereces page:
Targeting Specs: https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.8

Ad Targeting Search API: https://developers.facebook.com/docs/marketing-api/targeting-search/v2.8

#### Install
    git clone https://github.com/maraujo/pySocialWatcher.git
    cd pySocialWatcher
    pip install -r requirements.txt
    python setup.py install
    
#### Quick Start
You should have a .csv file with your Facebook tokens and accountIDs.
Example: pySocialWatcher/pysocialwatcher/facebook_tokens_example.csv
  
    >>> from pysocialwatcher import watcherAPI 
    >>> watcher = watcherAPI() 
    >>> watcher.load_credentials_file("pysocialwatcher/credentials.csv")
    >>> watcher.run_data_collection("pysocialwatcher/input_examples/quick_example.json")


#### Limitations:
Current supported API fields are listed below:
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

More information on the definition of the categories can be found here https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting/.


### 2.2. Downloaded data

The query returned a total of 595 thousand monthly users who are identified as Serbian expats. The map below presents per-country breakdown of that number. Note that 

![Map](data/Map.png)

We analysed the characteristics of Facebook Network statistics to develop a robust model for correcting the bias given by the fact that Facebook Network users may over or under-
represent a country’s population at large. As shown in Figure 2, Facebook Network users’ representativeness varies based on the country under consideration, as well as
demographic characteristics of the population, namely gender and age. When the number of Facebook Network users in a country and a given age group is higher than the actual
number of residents in that age group (based on official statistics), it means that users have multiple unlinked Facebook Network accounts, for instance on Facebook, Instagram
and Messenger. We assume that there are two main drivers of Facebook Network platforms’ usage.

![Pyramid](data/Structure.png)

### 2.2. Calibrating the raw data

Official statistics on international migrant stocks disaggregated by age, sex, country of birth and destination were used to a) identify the degree to which a migrant assimilates to the Facebook Network usage patterns of the destination country and b) evaluate and compare the results of the model proposed. Migration statistics at this level of disaggregation are available from UNDESA (2008), the OECD in collaboration with the World Bank (2010) and Eurostat (2017a). We used Eurostat statistics since they were more
updated. We additionally used updated population statistics from UNDESA (2017a) for calibrating the Facebook Network data.

## 3. Methodology

Our methodology is based on the following three papers:
[Monitoring of the Venezuelan exodus through
Facebook’s advertising platform](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229175)
[Quantifying international human mobility
patterns using Facebook Network data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0224134)
[Migration Data using Social Media](https://ec.europa.eu/jrc/en/publication/migration-data-using-social-media-european-perspective)

The goal is to estimate the number of expats based on non-representative raw Facebook data. We propose a three-step method:

1. Analyze Facebook data limitations, 
2. Clean the data.
3. Develop a model. 
