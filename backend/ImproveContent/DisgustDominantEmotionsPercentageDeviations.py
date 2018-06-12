#DISGUST - POPULAR - PERCENTAGE OF EACH EMOTIONS

DISGUST_P_ANGER_PERCENTAGE = 14.98
DISGUST_P_ANT_PERCENTAGE = 6.02
DISGUST_P_DISGUST_PERCENTAGE = 21.23
DISGUST_P_FEAR_PERCENTAGE = 16.75
DISGUST_P_JOY_PERCENTAGE = 10.14
DISGUST_P_SADNESS_PERCENTAGE = 15.01
DISGUST_P_SURPRISE_PERCENTAGE = 8.39
DISGUST_P_TRUST_PERCENTAGE = 7.48


#DISGUST - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

DISGUST_NP_ANGER_PERCENTAGE = 13.61
DISGUST_NP_ANT_PERCENTAGE = 5.84
DISGUST_NP_DISGUST_PERCENTAGE = 29.28
DISGUST_NP_FEAR_PERCENTAGE = 13.72
DISGUST_NP_JOY_PERCENTAGE = 6.96
DISGUST_NP_SADNESS_PERCENTAGE = 20.9
DISGUST_NP_SURPRISE_PERCENTAGE = 3.61
DISGUST_NP_TRUST_PERCENTAGE = 6.08

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(DISGUST_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(DISGUST_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(DISGUST_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(DISGUST_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(DISGUST_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(DISGUST_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(DISGUST_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(DISGUST_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(DISGUST_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(DISGUST_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(DISGUST_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(DISGUST_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(DISGUST_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(DISGUST_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(DISGUST_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(DISGUST_NP_TRUST_PERCENTAGE - d['trustPer'])
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
