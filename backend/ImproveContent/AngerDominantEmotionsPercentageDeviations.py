#ANGER - POPULAR - PERCENTAGE OF EACH EMOTIONS 

ANGER_P_ANGER_PERCENTAGE = 22.57
ANGER_P_ANT_PERCENTAGE = 9
ANGER_P_DISGUST_PERCENTAGE = 13.16
ANGER_P_FEAR_PERCENTAGE = 13.42
ANGER_P_JOY_PERCENTAGE = 9.82
ANGER_P_SADNESS_PERCENTAGE = 13.27
ANGER_P_SURPRISE_PERCENTAGE = 7.01
ANGER_P_TRUST_PERCENTAGE = 11.74

#ANGER - NON POPULAR - PERCENTAGE OF EACH EMOTIONS 

ANGER_NP_ANGER_PERCENTAGE = 25.65
ANGER_NP_ANT_PERCENTAGE = 6.6
ANGER_NP_DISGUST_PERCENTAGE = 15.05
ANGER_NP_FEAR_PERCENTAGE = 17.45
ANGER_NP_JOY_PERCENTAGE = 6.36
ANGER_NP_SADNESS_PERCENTAGE = 16.61
ANGER_NP_SURPRISE_PERCENTAGE = 5.54
ANGER_NP_TRUST_PERCENTAGE = 6.74

inner_rule_dict = {}

def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(ANGER_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(ANGER_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(ANGER_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(ANGER_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(ANGER_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(ANGER_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(ANGER_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(ANGER_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(ANGER_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(ANGER_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(ANGER_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(ANGER_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(ANGER_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(ANGER_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(ANGER_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(ANGER_NP_TRUST_PERCENTAGE - d['trustPer'])
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
