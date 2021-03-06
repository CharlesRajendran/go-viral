#ANGER - POPULAR - PERCENTAGES OF EACH POLARITY

ANGER_P_POSITIVITY_PERCENTAGE = 61.9
ANGER_P_NEGATIVITY_PERCENTAGE = 38.1

#ANGER - NON POPULAR - PERCENTAGES OF EACH POLARITY

ANGER_NP_POSITIVITY_PERCENTAGE = 51.71
ANGER_NP_NEGATIVITY_PERCENTAGE = 48.29

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(ANGER_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(ANGER_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(ANGER_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(ANGER_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
