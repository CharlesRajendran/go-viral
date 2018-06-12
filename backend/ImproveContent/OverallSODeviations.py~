#AVERAGE SO

P_SO = 19.97

NP_SO = 3.65


inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #overall SO
    angerDP = abs(P_SO - d)
    angerDNP = abs(NP_SO - d)
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['so'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['so'] = 1

    if(local_npc>local_pc):
        return 0
    else:
        return 1
