#FEAR - POPULAR - PERCENTAGES OF EACH POLARITY

FEAR_P_POSITIVITY_PERCENTAGE = 56.34
FEAR_P_NEGATIVITY_PERCENTAGE = 43.66


#FEAR - NON POPULAR - PERCENTAGES OF EACH POLARITY

FEAR_NP_POSITIVITY_PERCENTAGE = 54.76
FEAR_NP_NEGATIVITY_PERCENTAGE = 45.24

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(FEAR_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(FEAR_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(FEAR_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(FEAR_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
