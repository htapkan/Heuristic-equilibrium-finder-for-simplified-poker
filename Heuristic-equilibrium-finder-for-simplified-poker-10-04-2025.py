
class card():
    
    ranks_dictionary={2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":11,"Q":12,"K":13,"A":14}
    def __init__(self,suit,rank):        
        self.suit=suit
        self.rank=rank
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def attributes(self):
        return (self.suit,self.rank)
    def rank_value(self):
        return card.ranks_dictionary[self.rank]
    def __repr__(self):
        return "({}, {})".format(self.suit,self.rank)

class card_set(list):
    def get_card(self,n):
        return self[n-1]
    def add_cards(self,other):
        for i in self:
            for j in other:
                if i.suit==j.suit and i.rank==j.rank:
                    return "one card is already in the set"
        else:
            return self+other


class player():
    def __init__(self,cash,card):
        self.cash=cash
        self.card=card
    





#Initialize the deck of all cards:

suits=["d","c","s","h"]
ranks=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
ranks_dictionary={2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":11,"Q":12,"K":13,"A":14}



deck=card_set([])
for suit in suits:
    for rank in ranks:
        deck += [card(suit,rank)]


import random 


def subsetwithsize(lst,k):
    # a function to find the subsets of a list with given size k
    superlist=[]
    
    consider={}
    for i in range(1,len(lst)+1):
        consider[i]=[]

    consider[1]=[[lst[0]],[]]
    for u in range(1,len(lst)):
        for j in consider[u]:
            if () in j:
                j.remove(())
            
            if len(j)==k:
                superlist.append(j)
            else:
                
                consider[u+1].append(j+[lst[u]])
                consider[u+1].append(j)
            
    for i in consider[len(lst)]:
        if len(i)==k: 
            superlist.append(i)                       
    return superlist


def potential_cards(community,holding):
    # a function that finds the list of the potential cards of the other player given the community cards and own-holding.
    superlist=[]
    to_consider=deck[:]
    for i in community:
        for j in to_consider:
            if j.get_rank()==i.get_rank() and j.get_suit()==i.get_suit():
                to_consider.remove(j)
    for n in holding:
        for j in to_consider:
            if j.get_rank()==i.get_rank() and j.get_suit()==i.get_suit():
                to_consider.remove(j)
    for j in subsetwithsize(to_consider,2):
        superlist.append(j)
    return superlist
    
    
def potential_combos(community,holding):
    # Find all potential 7 card combinations of the other player (including the community cards)
    superlist=[]
    for i in potential_cards(community,holding):
        a=community+i
        superlist.append(a)
    return superlist



def flushtest(cards):
    for suit in suits:
        counter=0
        for i in cards:
            if i.get_suit()==suit:
                counter=counter+1
            if counter==5:
                return True
    return False

def flushset(cards):
    #find the cards that belong to a flush
    for suit in suits:
        counter=0
        flushset=[]
        for i in cards:
            if i.get_suit()==suit:
                counter=counter+1
        if counter>=5:
            for i in cards:
                if i.get_suit()==suit:
                    flushset.append(i)
            return flushset
    return []
            
   

def straighttest(cards):
    #checks whether there is a straight.
    ranks=[]
    for i in cards:
        ranks.append(i.rank_value())
    to_consider=sorted(ranks,reverse=True)
    already_considered=[]
    for j in to_consider:
        word=[]
        a=j
        while a in to_consider:
            if a in already_considered:
                a=a+1
            if a not in already_considered:
                word.append(a)
                a=a+1   
        if len(word)>=5:
            return True
        if len(word)==4 and 2 in word and 14 in to_consider:
            return True
    return False


def beststraightrank(cards):
    #calculates the highest rank card of a straight
    ranks=[]
    for i in cards:
        ranks.append(i.rank_value())
    to_consider=sorted(ranks,reverse=True)
    already_considered=[]
    bestrank=0
    for j in to_consider:
        word=[]
        a=j
        while a in to_consider:
            if a in already_considered:
                a=a+1
            if a not in already_considered:
                word.append(a)
                a=a+1
        if len(word)==4 and 2 in word and 14 in to_consider:
            bestrank=5       
        if len(word)>=5:
            bestrank=word[-1]
    return bestrank    

            
        
def straightflushtest(cards):
    if straighttest(cards) and flushtest(cards):
        return True
    return False

 
 
                       
def cardrankcomposer(cards):
    #Records the card composition in terms of the rank and the number of cards with that rank.
    Dict={}
    Compositionlist=[]
    for i in cards:
        if i.get_rank() in Dict.keys():
            Dict[i.get_rank()]=Dict[i.get_rank()]+1
        else:
            Dict[i.get_rank()]=1

    for i in Dict.items():
        Compositionlist.append(i)
    Compositionlist=sorted(Compositionlist,key=lambda x: (x[1],card.ranks_dictionary[x[0]]),reverse=True)
    return Compositionlist

def rankcomparator(cards1,cards2):
    #Compares the composed ranks of two sets of cards. This function does not do flush and straight-related comparisons. 
    if cardrankcomposer(cards1)[0:5]==cardrankcomposer(cards2)[0:5]:
        return "equal"
    cardranks1=cardrankcomposer(cards1)[0:5]
    cardranks2=cardrankcomposer(cards2)[0:5]
    
    effective_range= min(len(cardranks1),len(cardranks2))
               
    for i in range(effective_range):
        if cardranks1[i][1]==cardranks2[i][1]:
            if ranks_dictionary[cardranks1[i][0]]==ranks_dictionary[cardranks2[i][0]]: #here seems to be the issue.
                pass
            else:
                if ranks_dictionary[cardranks1[i][0]]>ranks_dictionary[cardranks2[i][0]]:
                    return "first"
                if ranks_dictionary[cardranks1[i][0]]<ranks_dictionary[cardranks2[i][0]]:
                    return "second"
        else:
            if cardranks1[i][1]>cardranks2[i][1]:
                return "first"
            else:
                return "second"
            

def cardscomparator(cards1,cards2):
    # Based on above it compares two sets of cards combinations.
    if straightflushtest(cards1):
        if straightflushtest(cards2):
            return rankcomparator(cards1,cards2)
        else:
            return "first"
    if straightflushtest(cards2):
        return "second"
    for i in (cardrankcomposer(cards1),cardrankcomposer(cards2)):
        if i[0][1]==4 or i[0][1]==3 and i[1][1]==2:
            return rankcomparator(cards1,cards2)
    if flushset(cards1)!=[]:
        if flushset(cards2)!=[] :
            return rankcomparator(flushset(cards1),flushset(cards2))
    else:
        if flushset(cards2)!=[]:
            return "second"
    return rankcomparator(cards1,cards2)
        

# To order many cards at once and obtain the potential strength of a card combination we do not use the exact rankcomparators. 
# This would have required obtaining a sorted list based on only binary comparisons. I have refrained from trying to solve that problem directly which might be computation-intesive.
# Instead, I decided to classify card combinations into segments based on their strength using most of the available information.
# I give them scores based on these segments and finally compare them according those scores.


def combinationscorer(cards):
    #This classifies card combinations and records the strength of some of the included cards relevant for comparison.
    if flushtest(cards):           
        if straighttest(flushset(cards)):
            superlist=["sf"]
            for x in card.ranks_dictionary.keys():
                if card.ranks_dictionary[x]==beststraightrank(flushset(cards)):
                    superlist.append(x)                  
            return superlist
    a=cardrankcomposer(cards)[:]
    if a[0][1]==4:
        
        return ["quads", a[0][0],max(a[0][1:])]
    
    if a[0][1]==3 and a[1][1]>=2 :
        return ["fh", a[0][0],a[1][0]]

    if flushtest(cards):
        d=flushset(cards)[0].get_suit()
        superlist=["flush"]
       
        addition=sorted([i for i in cards if i.get_suit()==d],key=lambda x: card.ranks_dictionary[x.get_rank()],reverse=True)[0:2]
        for i in addition:
            superlist.append(i.get_rank())
        
        return superlist
                                   
    if straighttest(cards):
        
            superlist=["st"]
            for x in card.ranks_dictionary.keys():
                if ranks_dictionary[x]==beststraightrank(cards):
                    superlist.append(x)                  
            return superlist
    
    if  a[0][1]==3 and a[1][1]==1 :
        return ["trips", a[0][0],a[1][0],a[2][0]]
    if  a[0][1]==2 and a[1][1]==2 :
        return ["tp", a[0][0],a[1][0],a[2][0]]
    if a[0][1]==2 and a[1][1]==1 :
        return ["op", a[0][0],a[1][0],a[2][0],a[3][0]]
    if a[0][1]==1: #and len(a)>4: (this is commented out- 03/04/2025)
        return ["np", a[0][0],a[1][0],a[2][0],a[3][0],a[4][0]]

#The following function gives scores based on the above classification.

def scorecompar(cards):
    q=combinationscorer(cards)[:]    
    x_1=card.ranks_dictionary[q[1]]
    if len(q)>2:        
        x_2=card.ranks_dictionary[q[2]]
    if combinationscorer(cards)[0]=="sf":
        return 10000+x_1
    if combinationscorer(cards)[0]=="quads":
        return 8000+x_1*20+x_2
    if combinationscorer(cards)[0]=="fh":
        return 7000+x_1*20+x_2
    if combinationscorer(cards)[0]=="flush":
        return 6000+x_1*20+x_2
    if combinationscorer(cards)[0]=="st":
        return 5000+x_1*20
    if combinationscorer(cards)[0]=="trips":
        return 4000+x_1*20+x_2
    if combinationscorer(cards)[0]=="tp":
        return 3000+x_1*20+x_2
    if combinationscorer(cards)[0]=="op":
        return 2000+x_1*20+x_2
    if combinationscorer(cards)[0]=="np":
        return 1000+x_1*20+x_2



def cardordererscore(cards):
    #Orders a set of cards based on the scores.
    for i in cards:
        i.append(scorecompar(i))        
    a=sorted(cards,key=lambda x: x[-1],reverse=True)
    return a


def percentile_calculator(community, holding):
    # Calculates the strength percentile (using cardorderscore) of a card combination based on the community cards.
    potential_com=potential_combos(community,holding)
    lst=cardordererscore(potential_com)
    own_cards=community+holding
    score=scorecompar(own_cards)
    a=len(lst)
    if score>lst[0][-1]:
        return 100
    if score<lst[a-1][-1]:
        return 0
    count=0
    for i in lst:
        if i[-1]>score:
            count+=1
    effective_order=a-count
    return (effective_order/a)*100



# The follong function describes a one-round simplified poker with two players and only river (all 5 community cards are open).
# The program takes strategies of the players which describe fully what a player would do in the game and distributes cards randomly.
# Based on the cards and strategies, it redistributes cash and records the game information in memory-tuples.
# Specifics: Each player has a cash amount of 9, the pot is set at 9 and each player can only bet or raise 3 euros at once.
# The strategies of the players are strength-percentile dependent- meaning that they take the form of dictionaries. 
# That is we assume the players would play the same strategy if two different card combinations belong to the same percentile interval.
# The strategy relevant intervals are 0-1pcn, 1-10pcn, 10-25pcn, 25-50pcn, 50-75pcn, 75-90pcn, 90-99pcn.
# Since the first action of the second player depends on what she observes first, her strategy dictionary depends on the first move of the first player.



def game(strategy1,strategy2):
    random.shuffle(deck)
    cards1=deck[0:2]
    cards2=deck[2:4]
    community_cards=deck[4:9]
    result=cardscomparator(cards1+community_cards,cards2+community_cards)   
    player1_percentile=percentile_calculator(community_cards,cards1)
    player2_percentile=percentile_calculator(community_cards,cards2)
    percentiles_list=[1,10,25,50,75,90,99]
    count=0
    for i in [1,10,25,50,75,90]:
        if i<=player1_percentile:
            count+=1
    
    effectivepercentile_1= percentiles_list[count]
    count=0
    for i in [1,10,25,50,75,90]:
        if i<=player2_percentile:
            count+=1
   
    effectivepercentile_2= percentiles_list[count]

    effectivestrategy1=strategy1[effectivepercentile_1]
    w=strategy2[effectivestrategy1[0]]
    effectivestrategy2= w[effectivepercentile_2]
    
    round=1
    last_move="a"
    pot=6
    cash_1,cash_2=9,9
    memory_player1=[]
    memory_player2=[]
    x="d"
    while x!="f" and x!="c":
        if round%2==1:
            Acting_last=1
            if effectivestrategy1[round//2]=="r":
                pot=pot+3
                cash_1=cash_1-3
                last_move="r"
                round=round+1
            elif  effectivestrategy1[round//2]=="ch":
                last_move="ch"
                round=round+1
            elif  effectivestrategy1[round//2]=="f":
                
                cash_2=cash_2+pot
                last_move="f"
            elif  effectivestrategy1[round//2]=="c":
                
                if result=="first":
                    cash_1=cash_1+pot
                if result=="second":
                    cash_2=cash_2+pot
                if result=="equal":
                    cash_1=pot/2+cash_1
                    cash_2=pot/2+cash_2
                last_move="c"
            memory_player1.append((last_move))
            x=last_move


        if round%2==0:
            Acting_last=2
            if effectivestrategy2[(round//2)-1]=="r":
                pot=pot+3
                cash_2=cash_2-3
                last_move="r"
                round=round+1
            elif  effectivestrategy2[(round//2)-1]=="ch":
                last_move="ch"
                round=round+1
            elif  effectivestrategy2[(round//2)-1]=="f":
                
                cash_1=cash_1+pot
                last_move="f"
            elif  effectivestrategy2[(round//2)-1]=="c":
                
                if result=="first":
                    cash_1=cash_1+pot
                if result=="second":
                    cash_2=cash_2+pot
                if result=="equal":
                    cash_1=pot/2+cash_2
                    cash_2=pot/2+cash_2
                last_move="c"
            memory_player2.append(last_move)
            x=last_move
    if len(memory_player1)==1:
        memo1=(memory_player1[0],)
    else:
        memo1=tuple(memory_player1)
    if len(memory_player2)==1:
        memo2=(memory_player2[0],)
    else:
        memo2=tuple(memory_player2)
    
    memotuple_1=(effectivepercentile_1,memo1)
    
    memotuple_2=(effectivepercentile_2,memo2)  

    return (cash_1,cash_2,memotuple_1,memotuple_2)


# The following generates a strategy for both players based on the memory that would come from the previous rounds.
# The strategy is generated in a random but structured process. 
# Simply, if a set of strategies are not tested (as indicated in the memory) for a given percentile, then the function makes a random choice out of these elements for the respective percentile.
# If for a given percentile, all options are tested, then the program orders the strategies based on the average cash return indicated in the memory.
# Based on this ordering, it chooses the best alternative with 80% probability, the second best with 10% probability. The last 10% is distributed within the remaining alternatives. 


def strategy_generator(memory1,memory2):
    import random   
    strategy_1={}
    strategy_2={}
    strategy_2["ch"]={}
    strategy_2["r"]={}
    untested_1={}
    untested_2={}
    for i in [1,10,25,50,75,90,99]:
        untested_1[i]=[]
        
        for j in memory1[i].keys():
            if memory1[i][j]==["untested"]:
                untested_1[i].append(j)
        if len(untested_1[i])>0:
            random.shuffle(untested_1[i])
            strategy_1[i]=untested_1[i][0]
        else:
            a=[x for x in memory1[i].keys()]
            
            d=sorted(a,key= lambda y: memory1[i][y][0],reverse= True)
            weig=[]
            b=len(a)-2

            weig.append(8*b)
            weig.append(b)
            weig=weig+[1]*b
        
            select=random.choices(d, weights = weig, k = 1)
            strategy_1[i]=select[0]

        
    for j in ["ch","r"]:
        untested_2[j]={}
        for i in [1,10,25,50,75,90,99]:
            untested_2[j][i]=[]
            for k in memory2[j][i]:
                if memory2[j][i][k]==["untested"]:
                    untested_2[j][i].append(k)
            if len(untested_2[j][i])>0:
                random.shuffle(untested_2[j][i])
                strategy_2[j][i]=untested_2[j][i][0]
            else:
                a=[x for x in memory2[j][i].keys()]
                z=sorted(a,key= lambda y: memory2[j][i][y][0],reverse= True)
                weig=[]
                b=len(a)-2

                weig.append(8*b)
                weig.append(b)
                weig=weig+[1]*b
        
                select=random.choices(z, weights = weig, k = 1)
                strategy_2[j][i]=select[0]

    return strategy_1,strategy_2



# The repeated game starts by using totally random strategies and untested- "no-memory" and iterates the one-round game multiple times based on the updated memories and strategies of the players.
# It includes a memory recording dictionary where the average cash return of a strategy and the actions of players are stored.



def repeated_game(n):
    strategy_set_p1=[("ch","c"),("ch","f"),("ch","r","f"),("ch","r","c"),("r","f"),("r","r"),("r","c")]
    strategy_set_p2={}
    strategy_set_p2["ch"]=[("c",),("r","r"),("r","f"),("r","c")]
    strategy_set_p2["r"]=[("c",),("r","c"),("r","f")]
    memory_player1={}
    memory_player2={}
    
    for i in [1,10,25,50,75,90,99]:
        memory_player1[i]={}
        for j in strategy_set_p1:
            memory_player1[i][j]=["untested"]
    for k in ["ch","r"]:
        memory_player2[k]={}        
        for i in [1,10,25,50,75,90,99]:
            memory_player2[k][i]={}
            for j in strategy_set_p2[k]:
                memory_player2[k][i][j]=["untested"]   
    cache_dict_1={}
    cache_dict_2={}
    cache_dict_2["ch"]={}
    cache_dict_2["r"]={}
    i=0
    
    while i<n:
        
        strategy1,strategy2= strategy_generator(memory_player1,memory_player2)
        cash_1,cash_2,memory1,memory2=game(strategy1,strategy2)
        
        percentile_1,percentile_2=memory1[0],memory2[0]
        
        action_1,action_2=memory1[1],memory2[1]
        
        if action_1 in cache_dict_1.keys():
            for strategy in cache_dict_1[action_1]:        
                if "untested" in memory_player1[percentile_1][strategy]:
                    memory_player1[percentile_1][strategy]=[cash_1,1]
                else:
                    old_average= memory_player1[percentile_1][strategy][0]
                    frequency=memory_player1[percentile_1][strategy][1]
                    new_average= (cash_1+frequency*old_average)/(frequency+1)
                    new_list=[new_average,frequency+1]
                    memory_player1[percentile_1][strategy]=new_list
        else:
            for strategy in strategy_set_p1:
                if len(strategy)>=len(action_1) and action_1==strategy[:len(action_1)]:        
                    if action_1 in cache_dict_1.keys():
                        cache_dict_1[action_1].append(strategy)
                    else:
                        cache_dict_1[action_1]=[strategy]
                    if "untested" in memory_player1[percentile_1][strategy]:             
                        memory_player1[percentile_1][strategy]=[cash_1,1]
                    else:
                        old_average= memory_player1[percentile_1][strategy][0]
                        frequency=memory_player1[percentile_1][strategy][1]
                        new_average= (cash_1+frequency*old_average)/(frequency+1)
                        new_list=[new_average,frequency+1]
                        memory_player1[percentile_1][strategy]=new_list

        if action_2 in cache_dict_2[action_1[0]].keys():
            for strategy in cache_dict_2[action_1[0]][action_2]:                           
                if "untested" in memory_player2[action_1[0]][percentile_2][strategy]:                    
                    new_list=[cash_2,1]
                    memory_player2[action_1[0]][percentile_2][strategy]=new_list
                else:
                    old_average= memory_player2[action_1[0]][percentile_2][strategy][0]
                    frequency=memory_player2[action_1[0]][percentile_2][strategy][1]
                    new_average= (cash_2+frequency*old_average)/(frequency+1)
                    new_list=[new_average,frequency+1]
                    memory_player2[action_1[0]][percentile_2][strategy]=new_list        
        else:
            
            for strategy in strategy_set_p2[action_1[0]]:
                if len(strategy)>=len(action_2) and action_2==strategy[:len(action_2)]:                                                                                            
                    if action_2 in cache_dict_2[action_1[0]].keys():
                        cache_dict_2[action_1[0]][action_2].append(strategy)
                    else:
                        cache_dict_2[action_1[0]][action_2]=[strategy]
                    if "untested" in memory_player2[action_1[0]][percentile_2][strategy]:                            
                        new_list=[cash_2,1]
                        memory_player2[action_1[0]][percentile_2][strategy]=new_list
                    else:
                        old_average= memory_player2[action_1[0]][percentile_2][strategy][0]
                        frequency=memory_player2[action_1[0]][percentile_2][strategy][1]
                        new_average= (cash_2+frequency*old_average)/(frequency+1)
                        new_list=[new_average,frequency+1]
                        memory_player2[action_1[0]][percentile_2][strategy]=new_list   
                                        
                         
            
        i+=1
    
    return memory_player1,memory_player2



# Testing the time of execution and printing the memory.


# The following function recommends a strategy based on the memory. This function in contrast to the previous strategy generator does not randomize and chooses the best alternative given the available information.

def strategy_recommender(memory_tuple):
    recommended_strategy_1={}
    for i in [1,10,25,50,75,90,99]:
        recommended_strategy_1[i]={}

    recommended_strategy_2={}
    for k in ["ch","r"]:
        recommended_strategy_2[k]={}
        for i in [1,10,25,50,75,90,99]:
            recommended_strategy_2[k][i]={}
               
    for i in [1,10,25,50,75,90,99]:
        for j in list(memory_tuple[0][i]):
            if memory_tuple[0][i][j]==["untested"]:
                memory_tuple[0][i].pop(j)
            
        a=[x for x in memory_tuple[0][i].keys()]
        if len(a)==0:
            recommended_strategy_1[i]="not enough information"   
        else:
            d=sorted(a,key= lambda y: sum(memory_tuple[0][i][y])/len(memory_tuple[0][i][y]),reverse= True)
            recommended_strategy_1[i]=d[0]
    
    for k in ["ch","r"]:
        for i in [1,10,25,50,75,90,99]:
            for j in list(memory_tuple[1][k][i]):
                if memory_tuple[1][k][i][j]==["untested"]:
                    memory_tuple[1][k][i].pop(j)
            
            a=[x for x in memory_tuple[1][k][i].keys()]
            if len(a)==0:
                recommended_strategy_2[k][i]="not enough information"
            else:
                d=sorted(a,key= lambda y: sum(memory_tuple[1][k][i][y])/len(memory_tuple[1][k][i][y]),reverse= True)
                recommended_strategy_2[k][i]=d[0]
    
    return (recommended_strategy_1,recommended_strategy_2)



# To compare the relative convergence of the recommended strategies out of two different simulations, we write a simple dictionary comparator.
def dict_comp(dict_1,dict_2):
    comp=0
    count=0
    for i in dict_1.keys():
         if dict_1[i]==dict_2[i]:
             comp+=1
    return comp/len(dict_1.keys())

             


# The function compares the similarity of two given strategy recommendations.
def compare(strategy_1,strategy_2):
    
    closeness_p1=dict_comp(strategy_1[0],strategy_2[0])
    closeness_p2=(1/2)*(dict_comp(strategy_1[1]["r"],strategy_2[1]["r"])+dict_comp(strategy_1[1]["ch"],strategy_2[1]["ch"]))
    return closeness_p1,closeness_p2
    


#Testing the execution time of two simulations and similarity of the recommended strategies.

import time

start = time.time()
f=repeated_game(250)
g=repeated_game(250)
print(strategy_recommender(f))
print(strategy_recommender(g))

print(compare(strategy_recommender(f),strategy_recommender(g)))

end = time.time()
print(end - start)
