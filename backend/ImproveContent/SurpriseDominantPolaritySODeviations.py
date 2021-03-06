#SURPRISE - POPULAR - SO OF EACH POLARITY

SURPRISE_P_POSITIVITY_SO = 16.14
SURPRISE_P_NEGATIVITY_SO = -5.32


#SURPRISE - NON POPULAR - SO OF EACH POLARITY

SURPRISE_NP_POSITIVITY_SO = 11.1
SURPRISE_NP_NEGATIVITY_SO = -3.1

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(SURPRISE_P_POSITIVITY_SO - d['semanticOrientationPos'])
    angerDNP = abs(SURPRISE_NP_POSITIVITY_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(SURPRISE_P_NEGATIVITY_SO - d['semanticOrientationNeg'])
    antDNP = abs(SURPRISE_NP_NEGATIVITY_SO - d['semanticOrientationNeg'])
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
