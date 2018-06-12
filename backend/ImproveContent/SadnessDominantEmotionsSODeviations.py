#SADNESS - POPULAR - SO OF EACH EMOTIONS

SADNESS_P_ANGER_SO = -4.48
SADNESS_P_ANT_SO = 2.32
SADNESS_P_DISGUST_SO = -4.69
SADNESS_P_FEAR_SO = -5.39
SADNESS_P_JOY_SO = 5.97
SADNESS_P_SADNESS_SO = -6.01
SADNESS_P_SURPRISE_SO = 1.45
SADNESS_P_TRUST_SO = 3.58


#SADNESS - NON POPULAR - SO OF EACH EMOTIONS

SADNESS_NP_ANGER_SO = -6.85
SADNESS_NP_ANT_SO = 1.77
SADNESS_NP_DISGUST_SO = -8.65
SADNESS_NP_FEAR_SO = -7.92
SADNESS_NP_JOY_SO = 3.69
SADNESS_NP_SADNESS_SO = -9.48
SADNESS_NP_SURPRISE_SO = 1.4
SADNESS_NP_TRUST_SO = 2.81

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(SADNESS_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(SADNESS_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(SADNESS_P_ANT_SO - d['antSO'])
    antDNP = abs(SADNESS_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(SADNESS_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(SADNESS_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(SADNESS_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(SADNESS_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(SADNESS_P_JOY_SO - d['joySO'])
    joyDNP = abs(SADNESS_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(SADNESS_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(SADNESS_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(SADNESS_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(SADNESS_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(SADNESS_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(SADNESS_NP_TRUST_SO - d['trustSO'])
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
