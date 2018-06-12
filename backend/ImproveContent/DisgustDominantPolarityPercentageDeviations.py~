#DISGUST - POPULAR - PERCENTAGES OF EACH POLARITY

DISGUST_P_POSITIVITY_PERCENTAGE = 58.65
DISGUST_P_NEGATIVITY_PERCENTAGE = 41.35

#DISGUST - NON POPULAR - PERCENTAGES OF EACH POLARITY

DISGUST_NP_POSITIVITY_PERCENTAGE = 52.92
DISGUST_NP_NEGATIVITY_PERCENTAGE = 47.08

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(DISGUST_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(DISGUST_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(DISGUST_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(DISGUST_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
