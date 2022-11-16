# crypto_dashboard_multipage


This project creates a dashboard for cryptocurrency data. It is meant to be simple and straight-forward for users new to crypto. The data provided gives them basic information to help them evaluate coin performance and develop a starting point for evaluating buy/sell opportunities.

1. Timely data on the top 10 coins is collected and displayed on the front page of the dashboard. 
2. The Coins page allows the user to choose a top-ten coin and a timeframe. With their parmaters choosen, numerical and graphical price trends are displayed. 
3. The Indicators page follows the users interest further by allowing them again to choose a coin and see common trade indictor statistics, used to help evaluate the coin's past performance.  These statistics are followed with information expaining their significance to the new crypto enthusiast. 
4. The XXX page, evaluates coin prices and trading fees across 5 different trading exchanges to find the best price for each coin. The user can elect to receive notifications via email to tell them the "best value" exchange for their top 3 prefered coins. 



## Technologies

This project leverages python 3.7.13 with the following packages:

* [pandas](https://pandas.pydata.org/) - For data analysis
* [streamlit](https://streamlit.io/) - For creating web apps from python script

---

## Installation Guide

Before running the application first install the dependencies in conda dev environment.

```python

    conda create -n dev python=3.7 anaconda

    python -m ipykernel install --user --name dev

    conda activate dev

    pip install -r requirements.txt

    conda deactivate 
  
```

---


##  Usage

To use the **crypto_dashboard_multipage** simply clone the repository and run the **main.py** with streamlit:

```python
    conda activate dev

    streamlit run main.py

    conda deactivate 
```

Here are the three pages :

![Coins Page ](Images/Coins.png)

![Portfolio Page ](Images/Portfolio.png)

![Notification Page ](Images/Notification.png)


---
## Questions to Answer

```python
    Which cryptocurrency coins would make the best investment in my portfolio?

    Has the price changed drastically or buy/sell criteria been met over the past few minutes?
```

---
## Research Resources/Datasets
```python
    coingecko API - for coin data

    streamlit - for Dashboard
```
---
## Project Tasks
```python
    Kausar - main dashboard page construction with graph of at least 10 coins

    Melissa & Edith - development of the portfolio construction outline of functions

    Jodi - API data analysis and notifications sent as email alerts 
```
---

## Contributors

Kausar Hina

Marissa Gonzalas

Edith Chou

Jodi Artman

---

## License

MIT

#testing branch Edith