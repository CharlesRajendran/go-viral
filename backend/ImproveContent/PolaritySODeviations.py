#EACH POLARITY SO OF POPULAR POSTS

P_POSITIVE_SO = 23.35

P_NEGATIVE_SO = -7.26


#EACH POLARITY SO OF NON POPULAR POSTS

NP_POSITIVE_SO = 14.49

NP_NEGATIVE_SO = -8.77


inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(P_POSITIVE_SO - d['semanticOrientationPos'])
    angerDNP = abs(NP_POSITIVE_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(P_NEGATIVE_SO - d['semanticOrientationNeg'])
    antDNP = abs(NP_NEGATIVE_SO - d['semanticOrientationNeg'])
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



    
    
























    
