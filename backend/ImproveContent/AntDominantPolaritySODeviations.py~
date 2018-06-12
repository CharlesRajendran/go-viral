#ANT - POPULAR - SO OF EACH POLARITY

ANT_P_POSITIVITY_SO = 18.88
ANT_P_NEGATIVITY_SO = -4.73


#ANT - NON POPULAR - SO OF EACH POLARITY

ANT_NP_POSITIVITY_SO = 15.82
ANT_NP_NEGATIVITY_SO = -4.55

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(ANT_P_POSITIVITY_SO - d['semanticOrientationPos'])
    angerDNP = abs(ANT_NP_POSITIVITY_SO - d['semanticOrientationPos'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(ANT_P_NEGATIVITY_SO - d['semanticOrientationNeg'])
    antDNP = abs(ANT_NP_NEGATIVITY_SO - d['semanticOrientationNeg'])
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
