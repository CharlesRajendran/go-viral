#NEGATIVITY - POPULAR - PERCENTAGE OF EACH EMOTIONS

NEGATIVITY_P_ANGER_PERCENTAGE = 16.9
NEGATIVITY_P_ANT_PERCENTAGE = 7.02
NEGATIVITY_P_DISGUST_PERCENTAGE = 12.44
NEGATIVITY_P_FEAR_PERCENTAGE = 20.73
NEGATIVITY_P_JOY_PERCENTAGE = 8.53
NEGATIVITY_P_SADNESS_PERCENTAGE = 15.56
NEGATIVITY_P_SURPRISE_PERCENTAGE = 9.21
NEGATIVITY_P_TRUST_PERCENTAGE = 9.6


#NEGATIVITY - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

NEGATIVITY_NP_ANGER_PERCENTAGE = 17.66
NEGATIVITY_NP_ANT_PERCENTAGE = 6.98
NEGATIVITY_NP_DISGUST_PERCENTAGE = 17.22
NEGATIVITY_NP_FEAR_PERCENTAGE = 16.42
NEGATIVITY_NP_JOY_PERCENTAGE = 8.77
NEGATIVITY_NP_SADNESS_PERCENTAGE = 18.76
NEGATIVITY_NP_SURPRISE_PERCENTAGE = 6.16
NEGATIVITY_NP_TRUST_PERCENTAGE = 6.28

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(NEGATIVITY_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(NEGATIVITY_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(NEGATIVITY_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(NEGATIVITY_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(NEGATIVITY_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(NEGATIVITY_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(NEGATIVITY_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(NEGATIVITY_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(NEGATIVITY_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(NEGATIVITY_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(NEGATIVITY_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(NEGATIVITY_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(NEGATIVITY_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(NEGATIVITY_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(NEGATIVITY_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(NEGATIVITY_NP_TRUST_PERCENTAGE - d['trustPer'])
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
