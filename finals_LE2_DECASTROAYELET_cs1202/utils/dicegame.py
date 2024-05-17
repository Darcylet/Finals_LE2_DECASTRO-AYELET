from utils.user import User
from utils.usermanager import UserManager
from utils.scores import Score
from datetime import datetime
import os
import random

class Dicegame(Score):
    def __init__(self, username):
        self.users = 'user'
        self.score_file = os.path.join(self.users, 'scores.txt')
        super().__init__(self.score_file)
        self.users = 'user'
        
        
    
    def menu(self, username):
        os.system('cls')
        print("""
-----------------------------------------
   __  __ __ ___    __   _  _   _____
  /  \/ ,'_// _/  ,'_/ .' \/ \,' / _/
 / o / / /_/ _/  / /_n/ o / \,' / _/ 
/__,/_/|__/___/  |__,/_n_/_/ /_/___/ 
                                                                                                                                          
-----------------------------------------
    """)
        print("1. Play game")
        print("2. View top scores")
        print("3. Log out")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.playgame(username)
        elif choice == 2:
            self.top_scores()
        elif choice == 3:
            os.system('cls')
            return
            
            
    def playgame(self, username):
        totalscore = 0
        rounds = 3
        stage = 0
        finalstageswon = 0

        while True:
            os.system('cls')
            
            while True:
                stage += 1
                print(f'-------------- Stage {stage} --------------')
                userscore = 0
                userroundswon = 0
                cpuroundswon = 0
                
                for i in range(rounds):    
                    usernum = random.randint(1,6)
                    cpunum = random.randint(1,6)
                    
                    print(f'{username} rolled: {usernum}\nCPU rolled: {cpunum}')
                   
                    if usernum == cpunum:
                        print("TIE!\n")
                   
                    if usernum > cpunum:
                        print(f'{username} won this round!\n')
                        userroundswon += 1
                        userscore += 1
                  
                    elif cpunum > usernum:
                        print("CPU won this round!\n")
                        cpuroundswon += 1
                break
            
            
            stageswon = 0
            
            while userroundswon == cpuroundswon:
                
                print("It's a Tie! roll again\n")
                usernum = random.randint(1,6)
                cpunum = random.randint(1,6)
                print(f'{username} rolled: {usernum}\nCPU rolled: {cpunum}')
                   
                if usernum == cpunum:
                    print("TIE!\n")
                
                if usernum > cpunum:
                    print(f'{username} won this round!\n')
                    userroundswon += 1
                    userscore += 1
                
                elif cpunum > usernum:
                    print("CPU won this round!\n")
                    cpuroundswon += 1
            
            
            if userroundswon > cpuroundswon:
                print(f'-------------- {username} Won this stage! --------------')
                userscore += 3
                totalscore += userscore
                stageswon += 1
                finalstageswon += stageswon
                print(f'Total points: {totalscore}       Stages won: {finalstageswon}\n')
            
                    
            elif cpuroundswon > userroundswon:
                print("CPU Won this stage!")
                save_score = Score(username)
                now = datetime.now()
                date = now.strftime("%Y-%m-%d %H:%M:%S")
                save_score.save_scores(username, totalscore, finalstageswon, date)
                
                totalscore = 0
                stageswon = 0
                finalstageswon = 0
           
            choice = input("play another stage?(y/n): ")
            while choice not in ('y', 'n'):
                print("Invalid input. try again")
                choice = input("play another stage?(y/n): ")
            
            if choice.lower() == 'n':
                self.menu(username)
                break
            
        
        
            
    def top_scores(self):
        score = Score(self.score_file)
        scores = score.load_scores()

        _scores_ = []
        for score_entry in scores:
            parts = score_entry.strip().split('  |  ')
            username = parts[0].split(': ')[1].strip()
            totalscore = int(parts[1].split(': ')[1].strip())
            stageswon = int(parts[2].split(': ')[1].strip())
            date = parts[3].split(': ')[1].strip()
            _scores_.append((username, totalscore, stageswon, date))
            
        _scores_.sort(key=lambda x: x[1], reverse=True)
        
        print("------------------TOP SCORES------------------")
        for i, (username, totalscore, stageswon, date) in enumerate(_scores_[:10], 1):
            print(f"{i}. {username} | Total Score: {totalscore} | Stages Won: {stageswon} | Achieved on: {date}")
            
        
        
        
        
        input("\n\nPRESS ENTER TO GO BACK TO MENU")
        self.menu(username)
            
        
            
            
            
            