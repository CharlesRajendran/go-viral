#SADNESS - POPULAR - PERCENTAGES OF EACH POLARITY

SADNESS_P_POSITIVITY_PERCENTAGE = 63.25
SADNESS_P_NEGATIVITY_PERCENTAGE = 36.75


#SADNESS - NON POPULAR - PERCENTAGES OF EACH POLARITY

SADNESS_NP_POSITIVITY_PERCENTAGE = 52.59
SADNESS_NP_NEGATIVITY_PERCENTAGE = 47.41

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(SADNESS_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(SADNESS_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(SADNESS_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(SADNESS_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
