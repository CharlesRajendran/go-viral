#TRUST - POPULAR - SO OF EACH POLARITY

TRUST_P_POSITIVITY_SO = 23.3
TRUST_P_NEGATIVITY_SO = -6.44

#TRUST - NON POPULAR - SO OF EACH POLARITY

TRUST_NP_POSITIVITY_SO = 16.08
TRUST_NP_NEGATIVITY_SO = -5.66

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(TRUST_P_POSITIVITY_SO - d['semanticOrientationPos'])
    angerDNP = abs(TRUST_NP_POSITIVITY_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(TRUST_P_NEGATIVITY_SO - d['semanticOrientationNeg'])
    antDNP = abs(TRUST_NP_NEGATIVITY_SO - d['semanticOrientationNeg'])
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
