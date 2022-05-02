# Chess_Tournament_Manager
P4_Sylvain_GAUTHIER_github

Chess Tournamanet manager is a programm to manage chess tournament written in Python
***
***
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Script Execution](#script-execution)
5. [Génération des rapport flake8-html](#flake8-html-report)
6. [FAQs](#faqs)
***
***
## General Info
***
This program is in version 1.0 and aimed the purpose why it has been created.
I wait hte result of the meeting with the askers to see if there was some modifications to brign to this version.

***
## Technologies
***
List of technologies used within this project : 
* [Windows 10](https://www.microsoft.com/fr-fr/software-download/windows10): version 21H2
* [Python](https://www.python.org/downloads/release/python-3100/):  version 3.10.0
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/): version 2021.2.3
* [git](https://git-scm.com/download/win): version 2.35.1.windows.2
* [flake8](https://pypi.org/project/flake8/): Version 4.0.1
* [flake8-html](https://pypi.org/project/flake8-html/): version 0.4.2
* [Tinydb](https://tinydb.readthedocs.io/en/latest/): version 4.7.0

***
## Installation
***
This process suggests that you have admin priviledges on you computer
### Python 3.10.0 installation
***
For installing Python 3.10.0 on your computer go to those adress following the OS you use :

For MacOS :

  Package :
    [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0post2-macos11.pkg)
    
  Installation guide :
    [Installing Python 3 on MacOS](https://docs.python-guide.org/starting/install3/osx/)

For Linux :

  Package :
    [Python 3.10.0](https://www.python.org/downloads/release/python-3100/)
    [Gzipped source tarball](https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz)
    [XZ compressed source tarball](https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz)
    
 Installation guide :
    [Installing Python 3.10.0 on Linux](https://docs.python-guide.org/starting/install3/linux/)

For Windows :

  Package : 
    [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
    
  Installation guide :
    [installing Python 3.1.0 on Windows](https://docs.python.org/fr/3/using/windows.html)

***
### Git 2.35.1 installation
***
For installing Git on your computer go to this adress (all OS contents):

[Git installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

***
#### Git configuration 
***
(Even if you did not have done before, create an account on Github at the adress : https://github.com)

1. In order to configure your git IDs , see the following process in GitBash console :
   Type the following command
  
  ``` 
       $ git config --global user.name "your_github_username"
       $ git config --global user.email your_email@your_provider.com
  ```
2. Type the following command to configure the GitBash console interface (optional) :
  
  ```
       $ git config --global color.diff auto
       $ git config --global color.status auto 
       $ git config --global color.branch auto
  ```
***
### Clone the distant repository with Gitbash
***
You have now to clone the distant repository on your computer.
1. type the following command in Gitbash console :
  
  ```
        $ git clone https://github.com/SGauthier2Pro/Chess_Tournament_Manager.git
  ```
2. Verify that you got the source directory opening an explorator and verifying that all files are in:

![directory_clone_CTM](https://user-images.githubusercontent.com/99419487/164944934-0c714e14-1366-47c7-83a1-106c249e626f.png)

![directory_content_CTM](https://user-images.githubusercontent.com/99419487/164945094-85b81809-0a5d-455a-a473-1233d2294fd8.png)

![CTM_controlers](https://user-images.githubusercontent.com/99419487/164945313-79ac3e82-2549-477a-ae54-c0b1f364e000.png)

![CTM_Flake8-rapport](https://user-images.githubusercontent.com/99419487/164945317-93f001d7-3bc8-47e5-bb30-273042a7a0f6.png)

![CTM_models](https://user-images.githubusercontent.com/99419487/164945320-8358a0c1-5782-4975-b0ae-abd783ec81bc.png)

![CTM_Views](https://user-images.githubusercontent.com/99419487/164945323-fa13e831-f0dc-45cd-aad3-68a6f5696983.png)

***
### configure the python environment for application
***
 1. open a Terminal
 2. go to program directory where you clone the distant repository in the precedent step : 
   /path_where_you_put_the clone_repo/Chess_Tournament_Manager
 3. create the virtual environment with the following command :
 
 ```
    python -m venv env
    
    sous Windows :
    env/Scripts/activate.bat
    
    sous linux ou MacOS :
    source env/bin/activate
 ```
4. Verify that the virtual environment is activate checking the presence of (env) before the prompt
5. Type the following command to implement all necessary modules in your environment :
 
 ```
      pip install -r requirements.txt
 ``` 
 6. verify that all packages are installed typing "pip freeze" command. You should get this result :
![pip_freeze_result_CTM](https://user-images.githubusercontent.com/99419487/164945928-56e3bc22-a333-4653-8fe4-c9d723dca993.png)
 7. now your environement is ready to execute the program. 
 
***
## Script Execution
***
to execute the program type :

```
    Python Chess_Tournament_Manager.py
```

***
### Main Menu
***

![Chess_Tournament_Manager_Main_Menu py](https://user-images.githubusercontent.com/99419487/164946120-bf5a3c38-79c9-459b-af3b-18d445a78a2e.png)


From this menu you can acces to 4 sub menus :

#### 1. Tournament Menu

![Chess_Tournament_Manager_1_Tournament_menu py](https://user-images.githubusercontent.com/99419487/164946151-d480c97a-5eea-49d0-8aa5-9242c9a84633.png)

From there you can chose 4 options :

1.1 Create a tournament :

Entering :
* the name of tournament
* the situation (city)
* one or more date
* the number of turns in tournament (4 by default)
* a description for the tournament
* the kind of time control (Bullet (by default), Blitz or Speed)

![Chess_Tournament_Manager_1 1_Create_Tournament py](https://user-images.githubusercontent.com/99419487/164946739-2fc4f07f-224e-40b9-98a0-113c503e2cac.png)

Then, it asks you to select the player in the data base list of player and show you witch player is select until you reach the number max of player (8):

![Chess_Tournament_Manager_1 1_add_players_in_tournament py](https://user-images.githubusercontent.com/99419487/164946747-dc6e4af3-40e1-4bc0-96b3-bc3662e6f9c8.png)

1.2 Load a tournament :

From there, you can load an existing tournament by choosing his number:

![Chess_Tournament_Manager_1 2_load_tournament py](https://user-images.githubusercontent.com/99419487/164946753-1a86009e-8a09-4cf0-a842-6c885ce63417.png)

When a tournament is loaded, it appears just under the main title

![Chess_Tournament_Manager_1 2_tournamanet_loaded py](https://user-images.githubusercontent.com/99419487/164946757-af709561-144a-4ef7-bb2d-0fccc2de91aa.png)

1.3 Enter the tournament results :

This menu display the tournament and the list of all players of this tournamanet.

First it asks you if you want to start a round ( if the tournament was allready in progress it asks you to start the last non started round)

![Chess_Tournament_Manager_1 3_start_round](https://user-images.githubusercontent.com/99419487/164946968-24a227f3-262f-48e7-8af4-79c44ab4435c.png)

Then, if you answer "n"("non") you back to the tournament menu, if you answer "o"("oui"), it display that the round is started 
and asks you if you want to enter the result of the round, 

![Chess_Tournament_Manager_1 3_enter_results](https://user-images.githubusercontent.com/99419487/164947060-8cc7e8c6-d4ca-49d3-a226-8d36e9814d98.png)

If you enter "o"("oui"), it displays each match with the name of players and asks you to enter the result (3 is null and is the default value) :

![Chess_Tournament_Manager_1 3_enter_match_result](https://user-images.githubusercontent.com/99419487/164947472-c1fea3a0-1ecc-494e-9627-27335213595e.png)

Finaly, it asks you if you wat to start the next round and so on, until the and of the tournament.

when the tournament is terminated, it displays the result of tournament

![Chess_Tournament_Manager_1 3_Final_result](https://user-images.githubusercontent.com/99419487/164948026-1e5fccd9-5803-463f-a703-086c755664ac.png)


NOTA : if you choose to enter result about a terminated tournament, this message appears :

![Chess_Tournament_Manager_1 3_tournament terminated](https://user-images.githubusercontent.com/99419487/164948153-e4587224-47e8-4c51-90a5-63e0d757b7d1.png)

The option 4 bring you back to the main menu

***
#### 2. Player management
***

![Chess_Tournament_Manager_2_player_menu](https://user-images.githubusercontent.com/99419487/164948219-c3cbd009-f7e1-4107-974b-6ca2488e15ea.png)

From there you got 2 options :

2.1 Enter a new player :

Entering :
* the family name
* the surname
* birthday date
* the ranking

![Chess_Tournament_Manager_2 1_enter_new_player](https://user-images.githubusercontent.com/99419487/164948348-ac1cbdbd-5c34-4833-9edf-6d9b4af0c2a0.png)

when all informations are entered, it asks you if you want to enter another player

![Chess_Tournament_Manager_2 1_enter_another_player](https://user-images.githubusercontent.com/99419487/164948352-ff397c62-4a83-42f0-9e7f-43e829014d37.png)

2.2 Update player informations :

From this menu you can update player informations including the ranking :

fisrt you choose the player to update entering his number :

![Chess_Tournament_Manager_2 2_choose_player](https://user-images.githubusercontent.com/99419487/164948428-4a30551e-9aac-42a0-b765-73605008e7ac.png)

then you select the item to update by his number or 6 to back to the player menu :

![Chess_Tournament_Manager_2 2_choose_player_item_to_update](https://user-images.githubusercontent.com/99419487/164948532-048906b6-733a-46ba-93d7-42c4fbd1c5cd.png)

and enter the new value :

![Chess_Tournament_Manager_2 2_new_item_value](https://user-images.githubusercontent.com/99419487/164948539-baf2ee1d-4f0b-4a6e-9a06-a7fabe783f3f.png)

After that it ask you if you want to change another information for this player, if no, if you want to change information about another player.

Option 3 bring you back to the main menu

***
#### 3 Report menu
***

![Chess_Tournament_Manager_3_Report_menu](https://user-images.githubusercontent.com/99419487/164948644-d73114ad-b4a2-4568-9cec-04a546fa7740.png)

From this menu you can choose to diplay 5 kind of report :

3.1 List of all player in data base :

![Chess_Tournament_Manager_3 1_sort_question](https://user-images.githubusercontent.com/99419487/164948700-7980557d-2289-42d5-b21d-15014be254f8.png)

2 kinds of sorting :
  
1. alphabetical
     
![Chess_Tournament_Manager_3 1_alphabetical](https://user-images.githubusercontent.com/99419487/164948860-38db4cf5-4d78-459d-85a2-4e0334a459cf.png)
     
2. by ranking
     
![Chess_Tournament_Manager_3 1_by_ranking](https://user-images.githubusercontent.com/99419487/164948869-b5581dcf-aca6-4d0d-91c2-68bf57830aaa.png)
     
3.2 List of tournament players

first you choose the tournament and then the sorting method (alphabetical or by ranking)

![Chess_Tournament_Manager_3 2_list_of_tournament_players](https://user-images.githubusercontent.com/99419487/164948937-4a0962ed-986c-4a44-ace5-b44c309bf50b.png)

3.3 list of tournaments in data base :

![Chess_Tournament_Manager_3 3_list_of_tournaments](https://user-images.githubusercontent.com/99419487/164948964-aaa75b37-3c9a-4b3c-809b-d3561334675c.png)

3.4 List of tournament turns :

![Chess_Tournament_Manager_3 4_list_of_tournament_turns](https://user-images.githubusercontent.com/99419487/164948995-a5e92064-12df-48bc-a6f3-b70ed673c343.png)

3.5 list of tournaments matches :

![Chess_Tournament_Manager_3 5_list_of_tournament_matches](https://user-images.githubusercontent.com/99419487/164949028-68a59933-60ac-445c-9711-631f9727414e.png)


option 6 to back to the main menu.

***
#### 4. Exit menu
***

![Chess_Tournament_Manager_4_Exit_menu](https://user-images.githubusercontent.com/99419487/164949071-2816474d-8812-4384-b2b3-0d93c0b9d87b.png)

choose 1 to close the program or 2 to back to the main menu

***
## Flake8-html reports
***

In order to generate the flake8-html report, type the following command from the program folder :

```
    flake8 --format=html --htmldir=flake8-report --max-line-length=119 --exclude env ../Chess_Tournament_Manager
```

***
## FAQs
***

N/A
