#ANGER - POPULAR - SO OF EACH POLARITY

ANGER_P_POSITIVITY_SO = 14.75
ANGER_P_NEGATIVITY_SO = -9.27

#ANGER - NON POPULAR - SO OF EACH POLARITY

ANGER_NP_POSITIVITY_SO = 8.03
ANGER_NP_NEGATIVITY_SO = -10.95

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(ANGER_P_POSITIVITY_SO - d['semanticOrientationPos'])
    angerDNP = abs(ANGER_NP_POSITIVITY_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(ANGER_P_NEGATIVITY_SO - d['semanticOrientationNeg'])
    antDNP = abs(ANGER_NP_NEGATIVITY_SO - d['semanticOrientationNeg'])
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
