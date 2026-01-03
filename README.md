# Bank Marketing Automation (Capstone 1 ML Zoomcamp)

## Problem Statement

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed ([Kaggle](https://www.kaggle.com/competitions/marketing-data/overview))

### Data Dictionary

|Field          | Description                               | Group     |
|---------------|-------------------------------------------|-----------|
|age            |age                                        | Features  |
|job	        |job                                        | Features  |
|marital        |marital status                             | Features  |
|education      |education group                            | Features  |
|default        |has credit default?                        | Features  |
|housing        |has housing loan?                          | Features  |
|loan           |has personal loan?                         | Features  |
|contact        |contact communication type('cellular','telephone') | Features  |
|month          |last contact month of year                 | Features  |
|day_of_week    |last contact day of the week               | Features  |
|duration       |last contact duration, in seconds          | Features  |
|campaign       |number of contacts performed during this campaign and for this client | Features  |
|pdays          |number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted) | Features  |
|previous       |number of contacts performed before this campaign and for this client (numeric) | Features  |
|poutcome       |outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success') | Features  |
|emp.var.rate   |employment variation rate - quarterly indicator (numeric) | Features  |
|cons.price.idx |consumer price index - monthly indicator (numeric) | Features  |
|cons.conf.idx  |consumer confidence index - monthly indicator (numeric) | Features  |
|euribor3m      |euribor 3 month rate - daily indicator (numeric) | Features  |
|nr.employed    |number of employees - quarterly indicator (numeric) | Features  |
|y              |has the client subscribed a term deposit? (binary: 'yes','no') | Label     |


## Environment Setup