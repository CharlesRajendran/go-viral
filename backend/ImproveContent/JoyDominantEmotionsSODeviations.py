#JOY - POPULAR - SO OF EACH EMOTIONS

JOY_P_ANGER_SO = -2.28
JOY_P_ANT_SO = 8.64
JOY_P_DISGUST_SO = -2.35
JOY_P_FEAR_SO = -3.06
JOY_P_JOY_SO = 17.53
JOY_P_SADNESS_SO = -2.4
JOY_P_SURPRISE_SO = 5.99
JOY_P_TRUST_SO = 10.9


#JOY - NON POPULAR - SO OF EACH EMOTIONS

JOY_NP_ANGER_SO = -1.76
JOY_NP_ANT_SO = 7.53
JOY_NP_DISGUST_SO = -1.85
JOY_NP_FEAR_SO = -2.01
JOY_NP_JOY_SO = 11.59
JOY_NP_SADNESS_SO = -2.12
JOY_NP_SURPRISE_SO = 4.66
JOY_NP_TRUST_SO = 6.72

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(JOY_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(JOY_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(JOY_P_ANT_SO - d['antSO'])
    antDNP = abs(JOY_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(JOY_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(JOY_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(JOY_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(JOY_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(JOY_P_JOY_SO - d['joySO'])
    joyDNP = abs(JOY_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(JOY_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(JOY_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(JOY_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(JOY_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(JOY_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(JOY_NP_TRUST_SO - d['trustSO'])
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
