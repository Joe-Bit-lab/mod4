# mod4
Flatiron Mod4 repo

### Team Members
Joe McHugh and Joe Buzzelli

### Items in Repository

- /data: includes the processed and raw data.  Some data was too large for a free Github account and thus, S3 storage was used.
- /github_lfs_setup: includes a jupyter notebook outlining how to setup git large file storage
- /kickoff_docs: includes documents outlining this Flatiron School assigment
- /Presentation_Materials: holds the final presentation and supporting images and notebooks
- README.md: this document outlining the repository
-/Step01_Data_Cleaning: includes notebooks executing the EDA and cleaning of Zillowing housing value data
- /Step02_Zip_Code_Selection: includes notebooks used to select zip codes with the least real estate volatility
- /Step03_Model: Includes the first draft of the ARIMA model
- /Step04_Reckoning: Includes the second wave of modeling
- /viz: folder cointaining project visualizaitons


### Prompt

Given a database of Zillow home values for 15,000 zip codes from 1996 to 2018, what are the best zip codes?  For this repository, Joe McHugh and Joe Buzzelli aim to answer this question.  Prior to providing answers, the term "best" must be defined.  In this project, we applied a fictious scenario.  We imigined that we were starting a business (J&J Real Estate) with the business strategy of identifying real estate markets in the U.S. that exhibit the lowest volatility for initial investment.  After defining "best", we applied ARIMA models to the top three zip codes in order to forecast real estate prices over the next year.  Our model applied to our portfolio perfromed 2.5% better (at roughly 8.5%) than the real estate market at large (roughly 6%).


### Goal

Identify three zip codes in order to invest in residential real estate.  These locations minimize risk and maximize returns based off of their performance from 2011 through 2018 (accounts for trends after the 2006 housing crisis).


### Results

With the exception of a small dip in our most volatile market, our forecatss were within the 95% confidence threshold for all three markets over the next year.

############################################################################################### Break
Template from Mod 3


### Methodology:

1. Clean and transform data
2. Conduct EDA
3. Develop and apply methodology for selecing the "best" zip codes
4. Create ARIMA models for each location
5. Analyze forecasts and apply to business problem

#### Data description: 

https://github.com/jaybee202/mod4

Zillow data set included 3.9 million rows (in long format) for 15,000 zip codes from 1996 to 2018.


### Recommendations:

Integrate access to credit data per zip code to better assess zip code suitability with the strategy of borrowing money for real estate investments.

### Next Steps:

Continue to update the model for date from 2018 through 2020 with additional analysis on the effect of the Covid-19 virus.



