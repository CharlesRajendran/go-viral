#ANT - POPULAR - PERCENTAGE OF EACH EMOTIONS 

ANT_P_ANGER_PERCENTAGE  = 5.58
ANT_P_ANT_PERCENTAGE  = 27.23
ANT_P_DISGUST_PERCENTAGE = 3.79
ANT_P_FEAR_PERCENTAGE = 8.76
ANT_P_JOY_PERCENTAGE = 22.66
ANT_P_SADNESS_PERCENTAGE = 6.75
ANT_P_SURPRISE_PERCENTAGE = 10.83
ANT_P_TRUST_PERCENTAGE = 14.4


#ANT - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

ANT_NP_ANGER_PERCENTAGE = 4.4
ANT_NP_ANT_PERCENTAGE = 27.63
ANT_NP_DISGUST_PERCENTAGE = 4.01
ANT_NP_FEAR_PERCENTAGE = 6.58
ANT_NP_JOY_PERCENTAGE = 23.4
ANT_NP_SADNESS_PERCENTAGE = 6.28
ANT_NP_SURPRISE_PERCENTAGE = 12.65
ANT_NP_TRUST_PERCENTAGE = 15.04

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(ANT_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(ANT_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(ANT_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(ANT_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(ANT_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(ANT_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(ANT_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(ANT_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(ANT_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(ANT_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(ANT_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(ANT_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(ANT_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(ANT_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(ANT_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(ANT_NP_TRUST_PERCENTAGE - d['trustPer'])
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
