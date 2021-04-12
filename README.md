1. ##### Common API use-cases:

   1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. 

   ```
   http://127.0.0.1:8000/api/?date__lte=2017-06-01&group_by=country&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks
   ```

   2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

   ```
   http://127.0.0.1:8000/api/?date__range=2017-05-01,2017-05-31&ordering=date&os=ios&group_by=date&limit=installs
   ```

   3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

   ```
   http://127.0.0.1:8000/api/?date__lte=2017-06-01&country=US&group_by=os&ordering=-revenue&limit=revenue
   ```

   4) Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

   ```
   http://127.0.0.1:8000/api/?country=CA&group_by=channel&cpi=cpi&limit=spend&ordering=-cpi
   ```

   

