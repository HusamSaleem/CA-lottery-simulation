# CA-lottery-simulation

# Description
- This program will scape the current drawings on the [CA Lottery](https://www.calottery.com/) for the 3 main tickets ```Powerball, SuperLotto, Mega Millions```
- It will also get the current prize money for each ticket respectively (Refer to [draw details](https://www.calottery.com/draw-games/powerball#section-content-1-3) for the prize money)
- User will be able to choose the ticket they want to ```simulate```, and have 2 ```simulation``` types
- The purpose is to showcase just how rare it is to win the jackpot prize


# Simulation Types
- ```Infinite simulation``` which means that the simulation will run until a ```jackpot``` occurs (5 numbers matching + special)
- ```Finite simulation``` where the user will be able to simulate only ```n``` tickets

# Getting Started

# Prerequisites
- [Python](https://www.python.org/downloads/)
- ```pip install columnar```
- ```pip install requests_html```
- [VSCode](https://code.visualstudio.com/) or any other IDE is fine

# Running the program
- Clone this repo
- Run the main.py file

# Example

- Program begins with showing the current drawings and prize money

![image](https://user-images.githubusercontent.com/60799172/161394783-87e07f85-672e-44c4-80b2-1393744ebbbc.png)

- Choosing option ```2``` for the ```SuperLotto simulation```

![image](https://user-images.githubusercontent.com/60799172/161394820-a8108896-ea26-4259-9464-c7cb2529dabc.png)

- Choosing the ```infinite simulation``` with the ```verbose``` option turned off

![image](https://user-images.githubusercontent.com/60799172/161394832-b8ab60fc-107d-4737-b901-7587884aff17.png)

- The final report and general statistics is outputted to the console after the ```simulation``` completes
- In this ```simulation```, we have actually gained $14,819,606.00 hence the - sign which is pretty rare to see

![image](https://user-images.githubusercontent.com/60799172/161395243-89636581-c28c-4914-a8cd-73ca9cf41ba7.png)
![image](https://user-images.githubusercontent.com/60799172/161395267-cdb8cc77-391c-41aa-905c-0efcf7049c93.png)

# Conclusion
- The example I showed above was very lucky
- The program's final report when excluding outliers like in the example shows odds are very close to the game odds that the [CA Lottery](https://www.calottery.com/) specifies on their website
