#EACH EMOTION SO OF POPULAR POSTS

P_ANGER_SO = -3.5

P_ANT_SO = 6.9

P_DISGUST_SO = -3.39

P_FEAR_SO = -4.22

P_JOY_SO = 13.48

P_SADNESS_SO = -3.65

P_SURPRISE_SO = 4.58

P_TRUST_SO = 9.77


#EACH EMOTION SO OF NON POPULAR POSTS

NP_ANGER_SO = -4.08

NP_ANT_SO = 4.83

NP_DISGUST_SO = -4.38

NP_FEAR_SO = -4.31

NP_JOY_SO = 7.54

NP_SADNESS_SO = -4.41

NP_SURPRISE_SO = 2.93

NP_TRUST_SO = 5.53


inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(P_ANGER_SO - d['angerSO'])
    angerDNP = abs(NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(P_ANT_SO - d['antSO'])
    antDNP = abs(NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(P_FEAR_SO - d['fearSO'])
    fearDNP = abs(NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(P_JOY_SO - d['joySO'])
    joyDNP = abs(NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(P_TRUST_SO - d['trustSO'])
    trustDNP = abs(NP_TRUST_SO - d['trustSO'])
    if(trustDP>trustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['trust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['trust'] = 1


    if(local_npc>local_pc):
        return 0
    else:
        return 1



    
    
























    
