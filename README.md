# CA-lottery-simulation

# Description
- This program will scape the current drawings on the [CA Lottery](https://www.calottery.com/) for the 3 main tickets ```Powerball, SuperLotto, Mega Millions```
- It will also get the current prize money for each ticket respectively (Refer to [draw details](https://www.calottery.com/draw-games/powerball#section-content-1-3) for the prize money)
- User will be able to choose the ticket they want to ```simulate```, and have 2 ```simulation``` types


# Simulation Types
- ```Infinite simulation``` which means that the simulation will run until a ```jackpot``` occurs (5 numbers matching + special)
- ```Finite simulation``` where the user will be able to simulate only ```n``` tickets

# Getting Started

# Prerequisites
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
- In this ```simulation```, we have actually gained $4,656,370.00 hence the - sign

![image](https://user-images.githubusercontent.com/60799172/161394869-1f79e639-17f5-49ca-8c6b-b96c6a3a0ac9.png)
![image](https://user-images.githubusercontent.com/60799172/161394879-5d62dd69-0f51-43a0-aaa1-80647bf0ad3f.png)


