# SI507 Project: Yelp Restaurant Search in New York City
SI 507 Intermediate Programming offered by UMSI in 22FA. This repo contains code for final project.



### About & Guideline

This project uses the [Yelp API](https://docs.developer.yelp.com/) to access 1000 restaurant records in the New York City Area. To use this project locally, please follow the steps listed below.

###### Step 1. Install Flask and Clone the Code

If user wants to run this project locally, run the following command to install `flask` and `requests`

```bash
pip install Flask
pip install requests
```

Then, clone the repo to your local directory

```bash
git clone https://github.com/TaikiShuttle/SI507.git
```

###### Step 2. Change the Yelp API Key

This project provides cached information for restaurants in `restaurant_info.json`. 

1. If you want to get those information by yourself, please open the `inform_get.py` and change the `api_key` variable to your own Yelp API Key. 

```python
import requests
import json
api_key = # Your API Key here
```

2. To get a Yelp API Key, please follow the steps [here](https://docs.developer.yelp.com/docs/fusion-authentication).
3. After changing `api_key`, just run the `inform_get.py` using `python inform_get.py`.

###### Step 3. Start the Flask Server

In your command line, run `flask --app restaurant_search run` under the cloned repo. And then go to `http://127.0.0.1:5000` to explore.

##### 1.3 Package Requirements

`Flask`, `requests`, `plotly`.



### How to Interact

Just click the link, and you will enter the corresponding websites.

###### 2.1 View Restaurant in an Interactive Map

Our user can easily get the information for all the restaurants stored in the data set for this project by hovering the mouse on the corresponding point. Also, this map supports zooming into a part of the map. With the help of the map, user can easily find the restaurants in a certain area, as well as their ratings. This can help them make plans for their lunch or dinner. 

###### 2.2 Conduct a Single Condition Precise Search

In this page, user can conduct a single dimension precise search, which means that user need to put exactly the name `key-dimension` pair to find all the related records. As shown in the picture above, after entering the searching condition, all the related records are shown in a list.

###### 2.3 Conduct a Range Search

In this page, user can conduct a range search. A range search means that user can enter a range and the search engine will return all the records that fall in that range. In this page, user can enter ranges for `population`, `rating`, `price`, and `name (sort by ASCII)` to search. For each of the dimension, a maximum and minimum value is required. If they are left blank, the default values will be filled in (0 and `math.inf` respective) to ensure all the possibly useful records are selected.

###### 2.4 Relations between Neighborhood Population and Restaurant Price and Rating

This page uses two interactive line plot to demonstrate the relation between Neighborhood Population and Restaurant Price and Rating.



### Demo Link

https://drive.google.com/file/d/1tE9Hm8zJ5kSl6AhtgW5kEJqyq9C9HD0H/view?usp=sharing

