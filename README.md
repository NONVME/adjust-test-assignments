[![CI](https://github.com/NONVME/adjust-test-assignments/actions/workflows/CI.yml/badge.svg)](https://github.com/NONVME/adjust-test-assignments/actions/workflows/CI.yml)

# AdjustHomeTask

Sample dataset: https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.
Dataset is expected to be stored and processed in a relational database.

Client of this API should be able to:

1. filter by time range (date_from+date_to is enough), channels, countries, operating systems
2. group by one or more columns: date, channel, country, operating system
3. sort by any column in ascending or descending order
4. see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

## Installation

**required dependencies**: [Poetry](https://github.com/python-poetry/poetry)

```bash
git clone git@github.com:NONVME/adjust-test-assignments.git
cd adjust-test-assignments
make install
```

## Usage

##### Localy

1. For local use, we need to create a .env  file in root project, with the *secret_key* and *debug* variables. After which we can start the server locally.

```bash
echo -e 'SECRET_KEY="rdh@tnbi+oz*5*92nze\#)ww_&l@y1+4^z0leoi&s44sh6_ygca"\nDEBUG=True' > .env
make migrate
make run-dev
```

2. Upload DB.

```bash
curl -X POST -d "https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv" --header 'Content-Type: application/json' http://127.0.0.1:8000/upload
```

   

##### Heroku

**[Preview on Heroku](https://adjust-dataset-api.herokuapp.com/api/)**

1. ##### Common API use-cases:

   1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. 

   Locally

   ```
   http://127.0.0.1:8000/api/?date__lte=2017-06-01&group_by=country&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks
   ```

   In Heroku:

   ```
   https://adjust-dataset-api.herokuapp.com/api/?date__lte=2017-06-01&group_by=country&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks
   ```

   2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

   Locally

   ```
   http://127.0.0.1:8000/api/?date__range=2017-05-01,2017-05-31&ordering=date&os=ios&group_by=date&limit=installs
   ```

   In Heroku:

   ```
   https://adjust-dataset-api.herokuapp.com/api/?date__range=2017-05-01,2017-05-31&ordering=date&os=ios&group_by=date&limit=installs
   ```

   3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

   Locally

   ```
   http://127.0.0.1:8000/api/?date__lte=2017-06-01&country=US&group_by=os&ordering=-revenue&limit=revenue
   ```

   In Heroku:

   ```
   https://adjust-dataset-api.herokuapp.com/api/?date__lte=2017-06-01&country=US&group_by=os&ordering=-revenue&limit=revenue
   ```

   4) Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

   Locally

   ```
   http://127.0.0.1:8000/api/?country=CA&group_by=channel&cpi=cpi&limit=spend&ordering=-cpi
   ```

   In Heroku:

   ```
   https://adjust-dataset-api.herokuapp.com/api/?country=CA&group_by=channel&cpi=cpi&limit=spend&ordering=-cpi
   ```

## Tests

Just:

```bash
make test
```

