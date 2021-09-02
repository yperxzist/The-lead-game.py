t = int(input("enter the round: "))
play1_score_list = []
play2_score_list = []
for i in range (t):
    play1 = int(input("enter the play1 score: "))
    play2 = int(input("enter the play2 score: "))
    if play1 > play2:
        play1_score = play1 - play2
        play1_score_list.append(play1_score)
        print("play1 is lead.")
    elif play1 < play2:
        play2_score = play2 - play1
        play2_score_list.append(play2_score)
        print("play2 is lead")
def addList(play1_score_list,play2_score_list):
    play1_score_list.sort()
    play2_score_list.sort() 
    add_list1 = sum(play1_score_list)
    add_list2 = sum(play2_score_list)
    if add_list1 > add_list2:
        print("play1 is win")
    else:
        print("play2 is win")
addList(play1_score_list,play2_score_list) 