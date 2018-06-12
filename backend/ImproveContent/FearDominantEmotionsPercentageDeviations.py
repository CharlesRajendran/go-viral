#FEAR - POPULAR - PERCENTAGE OF EACH EMOTIONS

FEAR_P_ANGER_PERCENTAGE = 12.86
FEAR_P_ANT_PERCENTAGE = 8.28
FEAR_P_DISGUST_PERCENTAGE = 11.48
FEAR_P_FEAR_PERCENTAGE = 24.07
FEAR_P_JOY_PERCENTAGE = 10.78
FEAR_P_SADNESS_PERCENTAGE = 14.74
FEAR_P_SURPRISE_PERCENTAGE = 8.02
FEAR_P_TRUST_PERCENTAGE = 9.76


#FEAR - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

FEAR_NP_ANGER_PERCENTAGE = 17.43
FEAR_NP_ANT_PERCENTAGE = 5.09
FEAR_NP_DISGUST_PERCENTAGE = 13.3
FEAR_NP_FEAR_PERCENTAGE = 25.33
FEAR_NP_JOY_PERCENTAGE = 6.25
FEAR_NP_SADNESS_PERCENTAGE = 19.06
FEAR_NP_SURPRISE_PERCENTAGE = 5.86
FEAR_NP_TRUST_PERCENTAGE = 7.68

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(FEAR_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(FEAR_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(FEAR_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(FEAR_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(FEAR_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(FEAR_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(FEAR_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(FEAR_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(FEAR_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(FEAR_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(FEAR_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(FEAR_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(FEAR_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(FEAR_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(FEAR_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(FEAR_NP_TRUST_PERCENTAGE - d['trustPer'])
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
