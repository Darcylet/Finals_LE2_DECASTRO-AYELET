import os

class Score:
    def __init__(self, scores_file):
        self.scores_file = scores_file
    
    def load_scores(self):
        scores_file = os.path.join('users', 'scores.txt')
        if os.path.exists(scores_file):
            with open(scores_file, 'r') as file:
                return file.readlines()
            
            return []
            
            
    def save_scores(self, username, totalscore, stageswon, date):
        score_folder = 'users'
        score_filepath = os.path.join(score_folder, 'scores.txt')
        if not os.path.exists(score_folder):
            os.makedirs(score_folder)
            
        with open(score_filepath, 'a') as file:
            file.write(f'user: {username}     |    Total score: {totalscore}     |      Stages won: {stageswon}       |     Achieved on: {date}\n')
            