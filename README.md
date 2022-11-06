# crypto_dashboard_multipage


This project will create a dashboard for cryptocurrency data. It is meant to be simple and straight-forward for users new to crypto.  

Timely data on the top 10 coins is collected and displayed on the front page of the dashboard. The Portfolio page shows the results of monte carlo simulations to help users evaluate the best coins to include in their portfolio. There is also notifications that can be sent to user's emails when coins reach criteria for users to consider when buying and selling. 


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


## Usage

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

StreamIt/Panel - for Dashboard
```
---
## Project Tasks
```python
 - Kausar - main dashboard page construction with graph of at least 10 coins

 - Melissa & Edith - development of the portfolio construction outline of functions

 - Jodi - API data analysis and notifications sent as email alerts 
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

