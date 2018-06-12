#JOY - POPULAR - PERCENTAGE OF EACH EMOTIONS

JOY_P_ANGER_PERCENTAGE = 5.41
JOY_P_ANT_PERCENTAGE = 16.54
JOY_P_DISGUST_PERCENTAGE = 4.43
JOY_P_FEAR_PERCENTAGE = 6.78
JOY_P_JOY_PERCENTAGE = 31.04
JOY_P_SADNESS_PERCENTAGE = 6.39
JOY_P_SURPRISE_PERCENTAGE = 10.6
JOY_P_TRUST_PERCENTAGE = 18.81


#JOY - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

JOY_NP_ANGER_PERCENTAGE = 4.88
JOY_NP_ANT_PERCENTAGE = 18.95
JOY_NP_DISGUST_PERCENTAGE = 3.35
JOY_NP_FEAR_PERCENTAGE = 5.39
JOY_NP_JOY_PERCENTAGE = 31.35
JOY_NP_SADNESS_PERCENTAGE = 6.59
JOY_NP_SURPRISE_PERCENTAGE = 12.52
JOY_NP_TRUST_PERCENTAGE = 16.97

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(JOY_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(JOY_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(JOY_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(JOY_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(JOY_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(JOY_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(JOY_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(JOY_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(JOY_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(JOY_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(JOY_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(JOY_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(JOY_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(JOY_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(JOY_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(JOY_NP_TRUST_PERCENTAGE - d['trustPer'])
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
