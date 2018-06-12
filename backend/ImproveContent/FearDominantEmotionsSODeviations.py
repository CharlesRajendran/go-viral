#FEAR - POPULAR - SO OF EACH EMOTIONS

FEAR_P_ANGER_SO = -6.77
FEAR_P_ANT_SO = 2.31
FEAR_P_DISGUST_SO = -6.42
FEAR_P_FEAR_SO = -9
FEAR_P_JOY_SO = 6.75
FEAR_P_SADNESS_SO = -6.93
FEAR_P_SURPRISE_SO = 1.22
FEAR_P_TRUST_SO = 4.14


#FEAR - NON POPULAR - SO OF EACH EMOTIONS

FEAR_NP_ANGER_SO = -7
FEAR_NP_ANT_SO = 1.47
FEAR_NP_DISGUST_SO = -6.66
FEAR_NP_FEAR_SO = -9
FEAR_NP_JOY_SO = 2.56
FEAR_NP_SADNESS_SO = -7.28
FEAR_NP_SURPRISE_SO = 0.97
FEAR_NP_TRUST_SO = 2.91

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(FEAR_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(FEAR_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(FEAR_P_ANT_SO - d['antSO'])
    antDNP = abs(FEAR_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(FEAR_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(FEAR_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(FEAR_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(FEAR_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(FEAR_P_JOY_SO - d['joySO'])
    joyDNP = abs(FEAR_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(FEAR_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(FEAR_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(FEAR_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(FEAR_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(FEAR_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(FEAR_NP_TRUST_SO - d['trustSO'])
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
