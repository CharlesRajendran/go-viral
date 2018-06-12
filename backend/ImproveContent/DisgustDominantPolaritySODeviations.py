#DISGUST - POPULAR - SO OF EACH POLARITY

DISGUST_P_POSITIVITY_SO = 13.56
DISGUST_P_NEGATIVITY_SO = -10.46


#DISGUST - NON POPULAR - SO OF EACH POLARITY

DISGUST_NP_POSITIVITY_SO = 9.39
DISGUST_NP_NEGATIVITY_SO = -13.42

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(DISGUST_P_POSITIVITY_SO - d['semanticOrientationPos'])
    angerDNP = abs(DISGUST_NP_POSITIVITY_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(DISGUST_P_NEGATIVITY_SO - d['semanticOrientationNeg'])
    antDNP = abs(DISGUST_NP_NEGATIVITY_SO - d['semanticOrientationNeg'])
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
