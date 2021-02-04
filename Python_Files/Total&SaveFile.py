#This function is used to get judge scores and returns them as an array
import os

def get_judge_scores():
    scores = []
    for i in range(0,5):
        in_range = False

        #This checks that the score is between 0 and 10 to prevent accidental mistakes
        while in_range == False:

            score = int(input("Judge "+str(i+1)+" : "))

            if score >= 0 and score <= 10:
                in_range = True
                scores.append(score)

    return scores

#This function discards of the minimum and maximum values of the scores and returns the total
def total(scores):

    local_scores = scores
    
    true_min = min(scores)
    true_max = max(scores)

    min_found = False
    max_found = False

    counter = 0

    #Removes the minimum and maximum values of the scores just once
    for i in local_scores:
        if local_scores[counter] == true_min and min_found == False:
            local_scores.pop(counter)
            min_found = True
            
        if local_scores[counter] == true_max and max_found == False:
            local_scores.pop(counter)
            max_found = True

        counter = counter + 1

    total = 0

    #Calculates the total scores 
    for i in local_scores:
        total = total + i

    return total

#This part saves the scores and total in a file
def file_write(scores, total, couple_name, round_name):

    #This gets the location of where the file is currently running from
    path = os.path.abspath(os.getcwd())

    try:
        new_file = open(path+'\\'+couple_name+'\\'+round_name+'.txt', 'w')

    except IOError:
        os.mkdir(path+'\\'+couple_name)
        new_file = open(path+'\\'+couple_name+'\\'+round_name+'.txt', 'w')
        
    score_holder = scores

#This part saves the results in a file, with * as a separator between them
    for i in score_holder:
        new_file.write(str(i)+'*')

#This part saves the total in the file
    new_file.write(str(total))
    new_file.close()
