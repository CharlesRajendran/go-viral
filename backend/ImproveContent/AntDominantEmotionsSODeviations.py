#ANT - POPULAR - SO OF EACH EMOTIONS

ANT_P_ANGER_SO = -1.48
ANT_P_ANT_SO = 9.35
ANT_P_DISGUST_SO = -1.68
ANT_P_FEAR_SO = -2.15
ANT_P_JOY_SO = 10.51
ANT_P_SADNESS_SO = -1.69
ANT_P_SURPRISE_SO = 4.55
ANT_P_TRUST_SO = 7.17


#ANT - NON POPULAR - SO OF EACH EMOTIONS

ANT_NP_ANGER_SO = -1.8
ANT_NP_ANT_SO = 7.45
ANT_NP_DISGUST_SO = -1.92
ANT_NP_FEAR_SO = -2
ANT_NP_JOY_SO = 8.8
ANT_NP_SADNESS_SO = -2
ANT_NP_SURPRISE_SO = 4.37
ANT_NP_TRUST_SO = 6.08

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(ANT_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(ANT_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(ANT_P_ANT_SO - d['antSO'])
    antDNP = abs(ANT_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(ANT_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(ANT_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(ANT_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(ANT_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(ANT_P_JOY_SO - d['joySO'])
    joyDNP = abs(ANT_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(ANT_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(ANT_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(ANT_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(ANT_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(ANT_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(ANT_NP_TRUST_SO - d['trustSO'])
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
