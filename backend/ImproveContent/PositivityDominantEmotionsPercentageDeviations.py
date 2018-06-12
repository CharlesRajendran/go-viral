#POSITIVITY - POPULAR - PERCENTAGE OF EACH EMOTIONS

POSITIVITY_P_ANGER_PERCENTAGE = 7.58
POSITIVITY_P_ANT_PERCENTAGE = 14.58
POSITIVITY_P_DISGUST_PERCENTAGE = 5.67
POSITIVITY_P_FEAR_PERCENTAGE = 8.78
POSITIVITY_P_JOY_PERCENTAGE = 23.74
POSITIVITY_P_SADNESS_PERCENTAGE = 8.81
POSITIVITY_P_SURPRISE_PERCENTAGE = 10.12
POSITIVITY_P_TRUST_PERCENTAGE = 19.69

#POSITIVITY - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

POSITIVITY_NP_ANGER_PERCENTAGE = 7.72
POSITIVITY_NP_ANT_PERCENTAGE = 13.85
POSITIVITY_NP_DISGUST_PERCENTAGE = 7.27
POSITIVITY_NP_FEAR_PERCENTAGE = 8.26
POSITIVITY_NP_JOY_PERCENTAGE = 20.39
POSITIVITY_NP_SADNESS_PERCENTAGE = 10.2
POSITIVITY_NP_SURPRISE_PERCENTAGE = 9.28
POSITIVITY_NP_TRUST_PERCENTAGE = 16.22

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(POSITIVITY_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(POSITIVITY_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(POSITIVITY_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(POSITIVITY_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(POSITIVITY_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(POSITIVITY_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(POSITIVITY_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(POSITIVITY_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(POSITIVITY_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(POSITIVITY_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(POSITIVITY_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(POSITIVITY_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(POSITIVITY_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(POSITIVITY_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(POSITIVITY_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(POSITIVITY_NP_TRUST_PERCENTAGE - d['trustPer'])
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
