#EACH EMOTION PERCENTAGES OF POPULAR POSTS

P_ANGER_PERCENTAGE = 8.29

P_ANT_PERCENTAGE = 14.09

P_DISGUST_PERCENTAGE = 6.14

P_FEAR_PERCENTAGE = 9.67

P_JOY_PERCENTAGE = 22.63

P_SADNESS_PERCENTAGE = 9.27

P_SURPRISE_PERCENTAGE = 9.98

P_TRUST_PERCENTAGE = 18.97

#EACH EMOTION PERCENTAGES OF NON POPULAR POSTS

NP_ANGER_PERCENTAGE = 9.53

NP_ANT_PERCENTAGE = 12.82

NP_DISGUST_PERCENTAGE = 9.22

NP_FEAR_PERCENTAGE = 9.58

NP_JOY_PERCENTAGE = 18.2

NP_SADNESS_PERCENTAGE = 11.77

NP_SURPRISE_PERCENTAGE = 8.65

NP_TRUST_PERCENTAGE = 14.47

inner_rule_dict = {}


def deviations(d):
    local_pc = 0
    local_npc = 0
    
    #anger
    angerDP = abs(P_ANGER_PERCENTAGE - d['angerPer'])
    angerDNP = abs(NP_ANGER_PERCENTAGE - d['angerPer'])
    if(angerDP>angerDNP):
        local_npc = local_npc + 1
        inner_rule_dict['anger'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['anger'] = 1

    #ant
    antDP = abs(P_ANT_PERCENTAGE - d['antPer'])
    antDNP = abs(NP_ANT_PERCENTAGE - d['antPer'])
    if(antDP>antDNP):
        local_npc = local_npc + 1
        inner_rule_dict['ant'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['ant'] = 1

    #disgust
    disgustDP = abs(P_DISGUST_PERCENTAGE - d['disgustPer'])
    disgustDNP = abs(NP_DISGUST_PERCENTAGE - d['disgustPer'])
    if(disgustDP>disgustDNP):
        local_npc = local_npc + 1
        inner_rule_dict['disgust'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['disgust'] = 1

    #fear
    fearDP = abs(P_FEAR_PERCENTAGE - d['fearPer'])
    fearDNP = abs(NP_FEAR_PERCENTAGE - d['fearPer'])
    if(fearDP>fearDNP):
        local_npc = local_npc + 1
        inner_rule_dict['fear'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['fear'] = 1

    #joy
    joyDP = abs(P_JOY_PERCENTAGE - d['joyPer'])
    joyDNP = abs(NP_JOY_PERCENTAGE - d['joyPer'])
    if(joyDP>joyDNP):
        local_npc = local_npc + 1
        inner_rule_dict['joy'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['joy'] = 1

    #sadness
    sadnessDP = abs(P_SADNESS_PERCENTAGE - d['sadnessPer'])
    sadnessDNP = abs(NP_SADNESS_PERCENTAGE - d['sadnessPer'])
    if(sadnessDP>sadnessDNP):
        local_npc = local_npc + 1
        inner_rule_dict['sadness'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['sadness'] = 1

    #surprise
    surpriseDP = abs(P_SURPRISE_PERCENTAGE - d['surprisePer'])
    surpriseDNP = abs(NP_SURPRISE_PERCENTAGE - d['surprisePer'])
    if(surpriseDP>surpriseDNP):
        local_npc = local_npc + 1
        inner_rule_dict['surprise'] = 0
    else:
        local_pc = local_pc + 1
        inner_rule_dict['surprise'] = 1

    #trust
    trustDP = abs(P_TRUST_PERCENTAGE - d['trustPer'])
    trustDNP = abs(NP_TRUST_PERCENTAGE - d['trustPer'])
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



    
    
























    
