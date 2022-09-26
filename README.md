# Rock Paper & Sissors  

### Developer: Asma Aamir 

## About
A traditional game that I played with my sibling to decide who would watch Tv first. Here, I've created it for computer play with user. Where the user make a choice to choose from Rock, Paper and Sissors. The computer makes the decison simultaneously. Who wins will depned on the choices they make. You must make an effort to forsee you adversary's futuer action if you to outwit them. 


## Table of Content
1. [Project Goals](#projects-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experiencer)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#users-requirment-and-expectations)
    3. [User manual]()
3. [Technical Design](#technical-design)
    1. 
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks--tools)
    3. [Libraries](#libraries)
5. [Features](#features)
6. [Testing](#validation) 
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

# Projects Goals
### User Goals:
* Paly a simple, enjoable gam
* Having access to your existing account 
* Before playing the game, read the rules.


### Site Owner Goals:
* Make a game that is simple and intuitive to play.
* Make sure that players comprehend the game's goal.


## User Experience 
### Target Audience
The game's doesn't have a target audience. However, in accordance with the traditional game, I would advise that participants be at least 4 year & above and be computer literate.  

### User Requirements and Expectations

### User Manual
#### Home Page
On the home page users are first shown a welcome page, with header ROCK, PAPER & SISSORS running diaginally. The user can choose from a few option below the welcome and header. Operation: Enter the entry key after entering a numeric value. 

- Game rules 
- log in 
- Play game  <br />

If a player enters a number that does not match an option that is accessible at any time during the game, they will be prompted to try again. 

#### Game Rules
User can read a brief description of the game rules by selecting the first option to examine the game rules, after which they can return to the main menu or login page, simply by chossing the option. 

#### Play 
The Play Game option prompts users to indicate whether they have already played the game or not. If they have, they will be directed to the login page; if not they will be directed to the registration page. 

#### Log in 
User are prompted to providde thie perivous login detail when chossing option 1. 
There is a validation mechamismm used for the username and password. The user has the choice to try again or register if they enter a username or password that havn't been registered. Operation: Press the enter key after entering a numeric value:
- Try again 
- Register <br />

Until the username and password entered by the user match the one that had already been registered, they can try again. If it does, then they would be greeted with a message. 
Alternativly, they can register by choosing the second choice.  

#### Registration for new players
Users can register to creat a new user by choosing the option from the login menu. 
The user will be prompted for their username and password in that order. The validation process involves both values. 
- Username must only contaon the leters a-z and can be no longer then 10 characters. 
- Password can be anywhere from 6 to 10 charaters. It can also inculde a capital letter and the digits 0-9. <br />

once registration is complete, the user is greeted with a notice that they have successfully registered and gives the choice to play or go the home page. 

#### Game and Plat again
The user makes the first move by selecting rock, paper or sissors by tyoing it on the keybaord. Then computer makes its move and the game's outcome is displayed to the user. 
If the users enter anthying other then rock ,paper and sissord  in the consol, the application will keep presenting the same option. 
When the user wins, lose or ties a notice stating that they can play agian will appear. If they select yes the game will restart. if not, it offers the user below optiom:
- Play again 
- Home page 
- Quit 

#### Quit game 
The application display a goodbye message whne the user exits. 


## User Stories
### Users
* 
* 
* 

### Site Owner
* 
* 
* 

## Technical Design 
* Flowchart 
The application's structure and logic are summarised in th diagram below. 
<details><summary>Flowchart</summary><img src="docs/flowchart.png"></details>

## Technologies Used
* Language
    - The logic of the programme was created using the Python programming language. 
* Frameworks & Tools 
    - GitHub
    - Google Cloud Platform
    - Google Sheets 
    - Heroku Platform 
    - Diagrams.net 
* Libraries
    * Python Libararies: 
        - Random: Used in Rock Paper & Scissors game to the user can play againt the computer. 
    * Third Party Libraries:
        - gspread: 
        - google.oauth2.service_account:
        
## Festures
1. Main Menu
2. Game Rules 
3. Play Option
4. Log-in 
5. Register 
6. Game 
7. Play again option 
8. Quit game option

## Validation

## Testing 

## Bugs

## Deployment
### Heroku 
I used Heroky to deploye this application through GitGub. below are the step I took to deploye the appliction:
    1. Create an account on herkou.com or sign in. 
    2. Creat a new app, add your project name and choose your region. 
    3. Click on create app
    4. Go to Setting 
    5. 


## Credits 
* Code Institute - for Git template ide and "Love Sandwiches - Essentials Project" which helped me with connecting the Google Spreadsheet to my project.

## Acknowledgements 
I would like to take this opportunit to thank you :
* My mentor Mo Shami for his feedback , advise and guidance
* tutor Ger for helping me fix registeration issue
* My mum Farida Liaqat for looking after my daughter and my daughter Zainab Rana for being very patient with me. 