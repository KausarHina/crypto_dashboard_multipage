## Code Flow - Notifications

# Main API storage of live data
1. `def api-timer()` runs continuous scheduler ever(x) minutes
    --calls function `get_live_data()` api call every (x)minues with all 10 coins
        --calls `clean_coin_data(all_coiN_info.df)` which returns all_coin_info.df
        --calls `save_coin_data(all_coin_info.df)` which creates sql database table "coin_info"

# Notifications page maybe rename Indicators
currently `test_indicators`.ipynb
1. asks user for coin choice via widget from top 10 coin list
    -api call with that coin for data past 90 days
    - creates db of price
    -currently slices 90 days of data  to create new df (because I got api call from jan1,2022- can be changed)
    -plots price for 90 days
    -computes simple moving average (SMA)for 7,12,30 days, and plots
        --explains significance and plot
    -computes weighted moving average (WMA)for 7 days
    -plots price vs. SMA-7 & WMA -7
        --explains significance and plot
    -computes bollinger bands
    -plots price vs bollinger bands
        --explains significance and plot
    
#Email Notifications
1. `verify notification(coin_list)` 
    -questionary: if wants email notifications, gets email
    -runs function `coin_choice'(coin_list)
    -returns new_email and coin choice to be saved in variables of same name

2. `add_email_and_coin(new_email, coin_choice)` 
    -adds parameters to lists and creates database
    -saves to sql database called "member emails and coins"

3. `notification_body(Marissa parameters)`
    - creates body of email notification to be sent
    -returns variable notification body str saved as global variable email_msg
    

3. email_send.py **this needs refining to grabs right emails and coin preference fromsql database)**
    -takes in global variable email_msg
    -takes email and coin preferance from sql database lists
    -sends emails
    -

