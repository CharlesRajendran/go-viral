#DISGUST - POPULAR - SO OF EACH EMOTIONS 

DISGUST_P_ANGER_SO = -7.09
DISGUST_P_ANT_SO = 1.26
DISGUST_P_DISGUST_SO = -8.28
DISGUST_P_FEAR_SO = -7.01
DISGUST_P_JOY_SO = 6.65
DISGUST_P_SADNESS_SO = -6.93
DISGUST_P_SURPRISE_SO = 0.91
DISGUST_P_TRUST_SO = 3.19


#DISGUST - NON POPULAR - SO OF EACH EMOTIONS

DISGUST_NP_ANGER_SO = -6.06
DISGUST_NP_ANT_SO = 1.35
DISGUST_NP_DISGUST_SO = -9.48
DISGUST_NP_FEAR_SO = -5.94
DISGUST_NP_JOY_SO = 3.58
DISGUST_NP_SADNESS_SO = -6.87
DISGUST_NP_SURPRISE_SO = 0.65
DISGUST_NP_TRUST_SO = 2.55

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(DISGUST_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(DISGUST_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(DISGUST_P_ANT_SO - d['antSO'])
    antDNP = abs(DISGUST_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(DISGUST_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(DISGUST_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(DISGUST_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(DISGUST_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(DISGUST_P_JOY_SO - d['joySO'])
    joyDNP = abs(DISGUST_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(DISGUST_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(DISGUST_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(DISGUST_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(DISGUST_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(DISGUST_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(DISGUST_NP_TRUST_SO - d['trustSO'])
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
