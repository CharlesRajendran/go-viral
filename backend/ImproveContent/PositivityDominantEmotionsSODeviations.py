#POSITIVITY - POPULAR - SO OF EACH EMOTIONS

POSITIVITY_P_ANGER_SO = -2.93
POSITIVITY_P_ANT_SO = 7.19
POSITIVITY_P_DISGUST_SO = -2.85
POSITIVITY_P_FEAR_SO = -3.59
POSITIVITY_P_JOY_SO = 13.91
POSITIVITY_P_SADNESS_SO = -3.13
POSITIVITY_P_SURPRISE_SO = 4.78
POSITIVITY_P_TRUST_SO = 10.03

#POSITIVITY - NON POPULAR - SO OF EACH EMOTIONS

POSITIVITY_NP_ANGER_SO = -2.76
POSITIVITY_NP_ANT_SO = 5.41
POSITIVITY_NP_DISGUST_SO = -2.8
POSITIVITY_NP_FEAR_SO = -3.02
POSITIVITY_NP_JOY_SO = 8.24
POSITIVITY_NP_SADNESS_SO = -2.96
POSITIVITY_NP_SURPRISE_SO = 3.43
POSITIVITY_NP_TRUST_SO = 6.02

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(POSITIVITY_P_ANGER_SO - d['angerSO'])
    angerDNP = abs(POSITIVITY_NP_ANGER_SO - d['angerSO'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(POSITIVITY_P_ANT_SO - d['antSO'])
    antDNP = abs(POSITIVITY_NP_ANT_SO - d['antSO'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(POSITIVITY_P_DISGUST_SO - d['disgustSO'])
    disgustDNP = abs(POSITIVITY_NP_DISGUST_SO - d['disgustSO'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(POSITIVITY_P_FEAR_SO - d['fearSO'])
    fearDNP = abs(POSITIVITY_NP_FEAR_SO - d['fearSO'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(POSITIVITY_P_JOY_SO - d['joySO'])
    joyDNP = abs(POSITIVITY_NP_JOY_SO - d['joySO'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(POSITIVITY_P_SADNESS_SO - d['sadnessSO'])
    sadnessDNP = abs(POSITIVITY_NP_SADNESS_SO - d['sadnessSO'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(POSITIVITY_P_SURPRISE_SO - d['surpriseSO'])
    surpriseDNP = abs(POSITIVITY_NP_SURPRISE_SO - d['surpriseSO'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(POSITIVITY_P_TRUST_SO - d['trustSO'])
    trustDNP = abs(POSITIVITY_NP_TRUST_SO - d['trustSO'])
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
