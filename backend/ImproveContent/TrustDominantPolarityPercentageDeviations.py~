#TRUST - POPULAR - PERCENTAGES OF EACH POLARITY

TRUST_P_POSITIVITY_PERCENTAGE = 77.19
TRUST_P_NEGATIVITY_PERCENTAGE = 22.81


#TRUST - NON POPULAR - PERCENTAGES OF EACH POLARITY

TRUST_NP_POSITIVITY_PERCENTAGE = 76.1
TRUST_NP_NEGATIVITY_PERCENTAGE = 23.9

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(TRUST_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(TRUST_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(TRUST_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(TRUST_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
