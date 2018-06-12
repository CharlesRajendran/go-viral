#SADNESS - POPULAR - PERCENTAGE OF EACH EMOTIONS

SADNESS_P_ANGER_PERCENTAGE = 13.18
SADNESS_P_ANT_PERCENTAGE = 7.46
SADNESS_P_DISGUST_PERCENTAGE = 10.42
SADNESS_P_FEAR_PERCENTAGE = 15.69
SADNESS_P_JOY_PERCENTAGE = 11.55
SADNESS_P_SADNESS_PERCENTAGE = 23.8
SADNESS_P_SURPRISE_PERCENTAGE = 6.41
SADNESS_P_TRUST_PERCENTAGE = 11.48


#SADNESS - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

SADNESS_NP_ANGER_PERCENTAGE = 13.74
SADNESS_NP_ANT_PERCENTAGE = 6.45
SADNESS_NP_DISGUST_PERCENTAGE = 17.58
SADNESS_NP_FEAR_PERCENTAGE = 15.61
SADNESS_NP_JOY_PERCENTAGE = 8.22
SADNESS_NP_SADNESS_PERCENTAGE = 26.01
SADNESS_NP_SURPRISE_PERCENTAGE = 5.4
SADNESS_NP_TRUST_PERCENTAGE = 6.99

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(SADNESS_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(SADNESS_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(SADNESS_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(SADNESS_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(SADNESS_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(SADNESS_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(SADNESS_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(SADNESS_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(SADNESS_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(SADNESS_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(SADNESS_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(SADNESS_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(SADNESS_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(SADNESS_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(SADNESS_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(SADNESS_NP_TRUST_PERCENTAGE - d['trustPer'])
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

