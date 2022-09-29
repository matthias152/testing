Login, buy, sell.
| TestCaseID  | Description | Steps | Data | Expected Result | 
| ------- | -------- | --------------- | ---------- | ----------- |
| T01  | Check user login with valid data  | 1. Go to login page <br /> 2. Enter Data <br /> 3. Press Login | user=matt, psw=1526 | User get logged in succesful, redirected to main page |
| T02  | Check user login with invalid data  | 1. Go to login page <br /> 2. Enter Data <br /> 3. Press Login | user=justauser, psw=1231231 | User receives an error, not logged in |
| T03 | Check if user can add balance properly | 1. Log in as an valid user with data <br /> 2. Click 'Add more funds!' button on Main Page <br /> 3. Type valid number and click 'Deposit' | user=test, psw=test1, balance=100 | Money gets added properly |
| T04 | Check if user can add balance properly | 1. Log in as an valid user with data <br /> 2. Click 'Add more funds!' button on Main Page <br /> 3. Type 'balance' in data and click 'Deposit' | user=test, psw=test1, balance='test' | Error, money does not get added |
| T05 | Check if user can buy cryptocurrencies with enough amount of money" | 1. Log in as an valid user with data <br /> 2. Go to 'Buy Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='ripple' amount=1 | Cryptocurrency purchased succesfully |
| T06 | Check if user can not buy cryptocurrencies without enough amount of money" | 1. Log in as an valid user with data <br /> 2. Go to 'Buy Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='bitcoin' amount=1000 | Error, Cryptocurrency not purchased succesfully |
| T07 | Check if user can sell his cryptocurrencies. | 1. Log in as an valid user with data <br /> 2. Go to 'Sell Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='ripple' amount=1 | Cryptocurrency sold succesfully, money added, crypto subtracted |
| T08 | Check if user can not sell cryptocurrencies he doesn't posses. | 1. Log in as an valid user with data <br /> 2. Go to 'Sell Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='ethereum' amount=1000 | Error, money and cryptos stays the same |

Sending.
| TestCaseID  | Description | Steps | Data | Expected Result | 
| ------- | -------- | --------------- | ---------- | ----------- |
| S01 | Send cryptocurrencies to existing WalletID | 1. Log in as an valid user with data <br /> 2. Go to 'Send Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='ripple', quantity=1, WalletID='ZSBmxHOEwSSy92tYI66LkcX89' | Send succesful, cryptos subtracted |
| S02 | Send cryptocurrencies to not existing WalletID | 1. Log in as an valid user with data <br /> 2. Go to 'Send Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='ripple', quantity=1, WalletID='test' | Error - WalletID does not exist |
| S03 | Send cryptocurrencies user does not possess | 1. Log in as an valid user with data <br /> 2. Go to 'Send Cryptos' section. <br /> 3. Fill in according to data | user=test, psw=test2 <br /> / CryptoName='bitcoin', quantity=15000, WalletID='ZSBmxHOEwSSy92tYI66LkcX89' | Error - Not enough cryptocurrencies in Wallet |

Attachments.
| TestCaseID  | Description | Steps | Data | Expected Result | 
| ------- | -------- | --------------- | ---------- | ----------- |
| A01 | Checks if User can download his transactions history as PDF file. | 1. Log in as an valid user with data <br /> 2. Go to 'Transactions' section. <br /> 3. Click 'Download' | user=test, psw=test3 | PDF file downloaded succesfully |
| A02 | Check if User can send his transactions history to E-Mail as PDF file. | 1. Log in as an valid user with data <br /> 2. Go to 'Transactions' section. <br /> 3. Click 'Send attachment' | user=test, psw=test3 | PDF file sent succesfully to user's E-Mail|
