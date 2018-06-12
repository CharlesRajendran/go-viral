#SURPRISE - POPULAR - SO OF EACH EMOTIONS

SURPRISE_P_ANGER_SO = -3.23
SURPRISE_P_ANT_SO = 4.45
SURPRISE_P_DISGUST_SO = -2.63
SURPRISE_P_FEAR_SO = -3.65
SURPRISE_P_JOY_SO = 8.79
SURPRISE_P_SADNESS_SO = -3.32
SURPRISE_P_SURPRISE_SO = 4.12
SURPRISE_P_TRUST_SO = 6.84


#SURPRISE - NON POPULAR - SO OF EACH EMOTIONS 

SURPRISE_NP_ANGER_SO = -0.9
SURPRISE_NP_ANT_SO = 4.05
SURPRISE_NP_DISGUST_SO = -1
SURPRISE_NP_FEAR_SO = -1.4
SURPRISE_NP_JOY_SO = 6.15
SURPRISE_NP_SADNESS_SO = -1
SURPRISE_NP_SURPRISE_SO = 4.85
SURPRISE_NP_TRUST_SO = 4

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(SURPRISE_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(SURPRISE_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(SURPRISE_P_ANT_SO - d['antSO'])
    antDNP = abs(SURPRISE_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(SURPRISE_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(SURPRISE_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(SURPRISE_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(SURPRISE_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(SURPRISE_P_JOY_SO - d['joySO'])
    joyDNP = abs(SURPRISE_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(SURPRISE_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(SURPRISE_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(SURPRISE_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(SURPRISE_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(SURPRISE_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(SURPRISE_NP_TRUST_SO - d['trustSO'])
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
