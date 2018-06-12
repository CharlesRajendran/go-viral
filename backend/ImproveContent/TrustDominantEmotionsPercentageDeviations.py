#TRUST - POPULAR - PERCENTAGE OF EACH EMOTIONS

TRUST_P_ANGER_PERCENTAGE = 7.11
TRUST_P_ANT_PERCENTAGE = 11.55
TRUST_P_DISGUST_PERCENTAGE = 5.15
TRUST_P_FEAR_PERCENTAGE = 7.61
TRUST_P_JOY_PERCENTAGE = 20.65
TRUST_P_SADNESS_PERCENTAGE = 8.64
TRUST_P_SURPRISE_PERCENTAGE = 10.58
TRUST_P_TRUST_PERCENTAGE = 28.71


#TRUST - NON POPULAR - PERCENTAGE OF EACH EMOTIONS

TRUST_NP_ANGER_PERCENTAGE = 6.42
TRUST_NP_ANT_PERCENTAGE = 13.36
TRUST_NP_DISGUST_PERCENTAGE = 5.12
TRUST_NP_FEAR_PERCENTAGE = 7.11
TRUST_NP_JOY_PERCENTAGE = 21.1
TRUST_NP_SADNESS_PERCENTAGE = 8.02
TRUST_NP_SURPRISE_PERCENTAGE = 8.86
TRUST_NP_TRUST_PERCENTAGE = 30.02

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(TRUST_P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(TRUST_NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(TRUST_P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(TRUST_NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(TRUST_P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(TRUST_NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(TRUST_P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(TRUST_NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(TRUST_P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(TRUST_NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(TRUST_P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(TRUST_NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(TRUST_P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(TRUST_NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(TRUST_P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(TRUST_NP_TRUST_PERCENTAGE - d['trustPer'])
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
