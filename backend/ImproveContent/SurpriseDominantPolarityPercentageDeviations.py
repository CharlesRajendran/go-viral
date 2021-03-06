#SURPRISE - POPULAR - PERCENTAGES OF EACH POLARITY

SURPRISE_P_POSITIVITY_PERCENTAGE = 70.02
SURPRISE_P_NEGATIVITY_PERCENTAGE = 29.98


#SURPRISE - NON POPULAR - PERCENTAGES OF EACH POLARITY

SURPRISE_NP_POSITIVITY_PERCENTAGE = 83.28
SURPRISE_NP_NEGATIVITY_PERCENTAGE = 16.72

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(SURPRISE_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(SURPRISE_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(SURPRISE_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(SURPRISE_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
