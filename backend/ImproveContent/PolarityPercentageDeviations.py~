#EACH POLARITY PERCENTAGES OF POPULAR POSTS

P_POSITIVE_PERCENTAGE = 74.15

P_NEGATIVE_PERCENTAGE = 25.85


#EACH POLARITY PERCENTAGES OF NON POPULAR POSTS

NP_POSITIVE_PERCENTAGE = 68.39

NP_NEGATIVE_PERCENTAGE = 31.61


inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(P_POSITIVE_PERCENTAGE - d['positivePer'])
    angerDNP = abs(NP_POSITIVE_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(P_NEGATIVE_PERCENTAGE - d['negativePer'])
    antDNP = abs(NP_NEGATIVE_PERCENTAGE - d['negativePer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['negativity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['negativity'] = 1

    if(local_npc>local_pc):
        return 0
    else:
        return 1



    
    
























    
