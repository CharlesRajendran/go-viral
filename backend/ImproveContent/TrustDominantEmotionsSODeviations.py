#TRUST - POPULAR - SO OF EACH EMOTIONS

TRUST_P_ANGER_SO = -2.56
TRUST_P_ANT_SO = 5.99
TRUST_P_DISGUST_SO = -2.73
TRUST_P_FEAR_SO = -3.17
TRUST_P_JOY_SO = 11.89
TRUST_P_SADNESS_SO = -2.59
TRUST_P_SURPRISE_SO = 5.16
TRUST_P_TRUST_SO = 12.23


#TRUST - NON POPULAR - SO OF EACH EMOTIONS

TRUST_NP_ANGER_SO = -2.17
TRUST_NP_ANT_SO = 4.77
TRUST_NP_DISGUST_SO = -2.19
TRUST_NP_FEAR_SO = -2.2
TRUST_NP_JOY_SO = 7.44
TRUST_NP_SADNESS_SO = -1.98
TRUST_NP_SURPRISE_SO = 3.03
TRUST_NP_TRUST_SO = 7.77

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(TRUST_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(TRUST_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(TRUST_P_ANT_SO - d['antSO'])
    antDNP = abs(TRUST_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(TRUST_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(TRUST_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(TRUST_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(TRUST_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(TRUST_P_JOY_SO - d['joySO'])
    joyDNP = abs(TRUST_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(TRUST_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(TRUST_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(TRUST_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(TRUST_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(TRUST_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(TRUST_NP_TRUST_SO - d['trustSO'])
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
