#SURPRISE - POPULAR - PERCENTAGE OF EACH EMOTIONS

SURPRISE_P_ANGER_PERCENTAGE = 9.21
SURPRISE_P_ANT_PERCENTAGE = 13.31
SURPRISE_P_DISGUST_PERCENTAGE = 7.02
SURPRISE_P_FEAR_PERCENTAGE = 9.05
SURPRISE_P_JOY_PERCENTAGE = 16.68
SURPRISE_P_SADNESS_PERCENTAGE = 9.1
SURPRISE_P_SURPRISE_PERCENTAGE = 21.53
SURPRISE_P_TRUST_PERCENTAGE = 14.1


#SURPRISE - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

SURPRISE_NP_ANGER_PERCENTAGE = 4.48
SURPRISE_NP_ANT_PERCENTAGE = 19.54
SURPRISE_NP_DISGUST_PERCENTAGE = 3.86
SURPRISE_NP_FEAR_PERCENTAGE = 5.04
SURPRISE_NP_JOY_PERCENTAGE = 23.14
SURPRISE_NP_SADNESS_PERCENTAGE = 5.05
SURPRISE_NP_SURPRISE_PERCENTAGE = 25.78
SURPRISE_NP_TRUST_PERCENTAGE = 13.11

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(SURPRISE_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(SURPRISE_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(SURPRISE_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(SURPRISE_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(SURPRISE_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(SURPRISE_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(SURPRISE_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(SURPRISE_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(SURPRISE_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(SURPRISE_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(SURPRISE_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(SURPRISE_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(SURPRISE_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(SURPRISE_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(SURPRISE_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(SURPRISE_NP_TRUST_PERCENTAGE - d['trustPer'])
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
