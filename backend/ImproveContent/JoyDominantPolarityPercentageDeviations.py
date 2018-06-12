#JOY - POPULAR - PERCENTAGES OF EACH POLARITY

JOY_P_POSITIVITY_PERCENTAGE = 81.2
JOY_P_NEGATIVITY_PERCENTAGE = 18.8


#JOY - NON POPULAR - PERCENTAGES OF EACH POLARITY

JOY_NP_POSITIVITY_PERCENTAGE = 79.32
JOY_NP_NEGATIVITY_PERCENTAGE = 20.68

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #positive
    angerDP = abs(JOY_P_POSITIVITY_PERCENTAGE - d['positivePer'])
    angerDNP = abs(JOY_NP_POSITIVITY_PERCENTAGE - d['positivePer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['positivity'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['positivity'] = 1

    #negative
    antDP = abs(JOY_P_NEGATIVITY_PERCENTAGE - d['negativePer'])
    antDNP = abs(JOY_NP_NEGATIVITY_PERCENTAGE - d['negativePer'])
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
