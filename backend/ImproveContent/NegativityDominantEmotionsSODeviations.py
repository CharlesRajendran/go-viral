#NEGATIVITY - POPULAR - SO OF EACH EMOTIONS

NEGATIVITY_P_ANGER_SO = -9.67
NEGATIVITY_P_ANT_SO = 2.6
NEGATIVITY_P_DISGUST_SO = -8.82
NEGATIVITY_P_FEAR_SO = -11.16
NEGATIVITY_P_JOY_SO = 7.93
NEGATIVITY_P_SADNESS_SO = -9.07
NEGATIVITY_P_SURPRISE_SO = 1.28
NEGATIVITY_P_TRUST_SO = 5.63


#NEGATIVITY - NON POPULAR - SO OF EACH EMOTIONS

NEGATIVITY_NP_ANGER_SO = -9.67
NEGATIVITY_NP_ANT_SO = 2.44
NEGATIVITY_NP_DISGUST_SO = -10.53
NEGATIVITY_NP_FEAR_SO = -9.65
NEGATIVITY_NP_JOY_SO = 4.37
NEGATIVITY_NP_SADNESS_SO = -10.49
NEGATIVITY_NP_SURPRISE_SO = 1.58
NEGATIVITY_NP_TRUST_SO = 3.56

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(NEGATIVITY_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(NEGATIVITY_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(NEGATIVITY_P_ANT_SO - d['antSO'])
    antDNP = abs(NEGATIVITY_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(NEGATIVITY_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(NEGATIVITY_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(NEGATIVITY_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(NEGATIVITY_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(NEGATIVITY_P_JOY_SO - d['joySO'])
    joyDNP = abs(NEGATIVITY_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(NEGATIVITY_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(NEGATIVITY_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(NEGATIVITY_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(NEGATIVITY_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(NEGATIVITY_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(NEGATIVITY_NP_TRUST_SO - d['trustSO'])
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
