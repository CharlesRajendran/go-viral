import operator
import FindPostSO, FindPostEmotionSO, FindPostEmotionPercentage, FindPostPolarityPercentage, FindPostPolaritySO
import EmotionsPercentageDeviations, EmotionsSODeviations, PolarityPercentageDeviations, PolaritySODeviations, OverallSODeviations

import AngerDominantEmotionsPercentageDeviations, AngerDominantEmotionsSODeviations, AngerDominantPolarityPercentageDeviations, AngerDominantPolaritySODeviations
import AntDominantEmotionsPercentageDeviations, AntDominantEmotionsSODeviations, AntDominantPolarityPercentageDeviations, AntDominantPolaritySODeviations
import DisgustDominantEmotionsPercentageDeviations, DisgustDominantEmotionsSODeviations, DisgustDominantPolarityPercentageDeviations, DisgustDominantPolaritySODeviations
import FearDominantEmotionsPercentageDeviations, FearDominantEmotionsSODeviations, FearDominantPolarityPercentageDeviations, FearDominantPolaritySODeviations
import JoyDominantEmotionsPercentageDeviations, JoyDominantEmotionsSODeviations, JoyDominantPolarityPercentageDeviations, JoyDominantPolaritySODeviations
import SadnessDominantEmotionsPercentageDeviations, SadnessDominantEmotionsSODeviations, SadnessDominantPolarityPercentageDeviations, SadnessDominantPolaritySODeviations
import SurpriseDominantEmotionsPercentageDeviations, SurpriseDominantEmotionsSODeviations, SurpriseDominantPolarityPercentageDeviations, SurpriseDominantPolaritySODeviations
import TrustDominantEmotionsPercentageDeviations, TrustDominantEmotionsSODeviations, TrustDominantPolarityPercentageDeviations, TrustDominantPolaritySODeviations

import PositivityDominantEmotionsPercentageDeviations, PositivityDominantEmotionsSODeviations
import NegativityDominantEmotionsPercentageDeviations, NegativityDominantEmotionsSODeviations

import Rules

#to be passed to Recommendation
rules = {}

#to be passed to Visualization
e_visualization = []
s_visualization = []



def dictCreatorPos(d):
    temp = {}
    for k,v in d.items():
        if(v == 1):
            temp[k] = v
    return temp

def dictCreatorNeg(d):
    temp = {}
    for k,v in d.items():
        if(v == 0):
            temp[k] = v
    return temp



def measurePopularity(file_name):
    file_handler = open(file_name,"r").read()
    pc = 0
    npc = 0

    #finding values from post
    so = FindPostSO.FindSO(file_handler)

    eso = FindPostEmotionSO.FindEmotionsSO(file_handler)

    eper = FindPostEmotionPercentage.FindEmotionsPer(file_handler)

    pso = FindPostPolaritySO.FindPolaritySO(file_handler)

    pper = FindPostPolarityPercentage.FindPolarityPer(file_handler)
   
    

    #finding deviations from emotions percentage - rule 1
    epd = EmotionsPercentageDeviations.deviations(eper)
    if(epd == 1):
        pc = pc + 1
    else:
        npc = npc + 1
        rules['rule1'] = EmotionsPercentageDeviations.inner_rule_dict
    

    #finding deviations from emotions so - rule 2
    esod = EmotionsSODeviations.deviations(eso)
    if(esod == 1):
        pc = pc + 1
        e_visualization.append(dictCreatorPos(EmotionsSODeviations.inner_rule_dict))
    else:
        npc = npc + 1
        rules['rule2'] = EmotionsSODeviations.inner_rule_dict
        e_visualization.append(dictCreatorNeg(EmotionsSODeviations.inner_rule_dict))
        


    #finding deviations from polarity percentage - rule 3
    ppd = PolarityPercentageDeviations.deviations(pper)
    if(ppd == 1):
        pc = pc + 1
    else:
        npc = npc + 1
        rules['rule3'] = PolarityPercentageDeviations.inner_rule_dict


    #finding deviations from polarity so - rule 4
    psod = PolaritySODeviations.deviations(pso)
    if(psod == 1):
        pc = pc + 1
        s_visualization.append(dictCreatorPos(PolaritySODeviations.inner_rule_dict))
    else:
        npc = npc + 1
        rules['rule4'] = PolaritySODeviations.inner_rule_dict
        s_visualization.append(dictCreatorNeg(PolaritySODeviations.inner_rule_dict))


    #finding deviations from overall so - rule 5
    sod = OverallSODeviations.deviations(so)
    if(sod == 1):
        pc = pc + 1
        s_visualization.append(dictCreatorPos(OverallSODeviations.inner_rule_dict))
    else:
        npc = npc + 1
        rules['rule5'] = OverallSODeviations.inner_rule_dict
        s_visualization.append(dictCreatorNeg(OverallSODeviations.inner_rule_dict))


    #finding dominant emotion
    maxEm = max(eper, key=eper.get)

    #if the dominant emotion is anger
    if(maxEm == 'angerPer'):
        #anger - finding deviations from emotions percentage - rule 6
        epd = AngerDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule6'] = AngerDominantEmotionsPercentageDeviations.inner_rule_dict


        #anger - finding deviations from emotions so - rule 7
        esod = AngerDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(AngerDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule7'] = AngerDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(AngerDominantEmotionsSODeviations.inner_rule_dict))


        #anger - finding deviations from polarity percentage - rule 8
        ppd = AngerDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule8'] = AngerDominantPolarityPercentageDeviations.inner_rule_dict


        #anger - finding deviations from polarity so - rule 9
        psod = AngerDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(AngerDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule9'] = AngerDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(AngerDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is anticipation
    if(maxEm == 'antPer'):
        #ant - finding deviations from emotions percentage - rule 10
        epd = AntDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule10'] = AntDominantEmotionsPercentageDeviations.inner_rule_dict


        #ant - finding deviations from emotions so - rule 11
        esod = AntDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(AntDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule11'] = AntDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(AntDominantEmotionsSODeviations.inner_rule_dict))


        #ant - finding deviations from polarity percentage - rule 12
        ppd = AntDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule12'] = AntDominantPolarityPercentageDeviations.inner_rule_dict


        #ant - finding deviations from polarity so - rule 13
        psod = AntDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(AntDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule13'] = AntDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(AntDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is disgust
    if(maxEm == 'disgustPer'):
        #disgust - finding deviations from emotions percentage - rule 14
        epd = DisgustDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule14'] = DisgustDominantEmotionsPercentageDeviations.inner_rule_dict


        #disgust - finding deviations from emotions so - rule 15
        esod = DisgustDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(DisgustDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule15'] = DisgustDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(DisgustDominantEmotionsSODeviations.inner_rule_dict))


        #disgust - finding deviations from polarity percentage - rule 16
        ppd = DisgustDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule16'] = DisgustDominantPolarityPercentageDeviations.inner_rule_dict


        #disgust - finding deviations from polarity so - rule 17
        psod = DisgustDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(DisgustDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule17'] = DisgustDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(DisgustDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is fear
    if(maxEm == 'fearPer'):
        #fear - finding deviations from emotions percentage - rule 18
        epd = FearDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule18'] = FearDominantEmotionsPercentageDeviations.inner_rule_dict


        #fear - finding deviations from emotions so - rule 19
        esod = FearDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(FearDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule19'] = FearDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(FearDominantEmotionsSODeviations.inner_rule_dict))


        #fear - finding deviations from polarity percentage - rule 20
        ppd = FearDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule20'] = FearDominantPolarityPercentageDeviations.inner_rule_dict


        #fear - finding deviations from polarity so - rule 21
        psod = FearDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(FearDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule21'] = FearDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(FearDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is joy
    if(maxEm == 'joyPer'):
        #joy - finding deviations from emotions percentage - rule 22
        epd = JoyDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule22'] = JoyDominantEmotionsPercentageDeviations.inner_rule_dict


        #joy - finding deviations from emotions so - rule 23
        esod = JoyDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(JoyDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule23'] = JoyDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(JoyDominantEmotionsSODeviations.inner_rule_dict))


        #joy - finding deviations from polarity percentage - rule 24
        ppd = JoyDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule24'] = JoyDominantPolarityPercentageDeviations.inner_rule_dict


        #joy - finding deviations from polarity so - rule 25
        psod = JoyDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(JoyDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule25'] = JoyDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(JoyDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is sadness
    if(maxEm == 'sadnessPer'):
        #sadness - finding deviations from emotions percentage - rule 26
        epd = SadnessDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule26'] = SadnessDominantEmotionsPercentageDeviations.inner_rule_dict


        #sadness - finding deviations from emotions so - rule 27
        esod = SadnessDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(SadnessDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule27'] = SadnessDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(SadnessDominantEmotionsSODeviations.inner_rule_dict))


        #sadness - finding deviations from polarity percentage - rule 28
        ppd = SadnessDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule28'] = SadnessDominantPolarityPercentageDeviations.inner_rule_dict


        #sadness - finding deviations from polarity so - rule 29
        psod = SadnessDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(SadnessDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule29'] = SadnessDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(SadnessDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is surprise
    if(maxEm == 'surprisePer'):
        #surprise - finding deviations from emotions percentage - rule 30
        epd = SurpriseDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule30'] = SurpriseDominantEmotionsPercentageDeviations.inner_rule_dict


        #Surprise - finding deviations from emotions so - rule 31
        esod = SurpriseDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(SurpriseDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule31'] = SurpriseDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(SurpriseDominantEmotionsSODeviations.inner_rule_dict))


        #Surprise - finding deviations from polarity percentage - rule 32
        ppd = SurpriseDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule32'] = SurpriseDominantPolarityPercentageDeviations.inner_rule_dict


        #Surprise - finding deviations from polarity so - rule 33
        psod = SurpriseDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(SurpriseDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule33'] = SurpriseDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(SurpriseDominantPolaritySODeviations.inner_rule_dict))


    #if the dominant emotion is trust
    if(maxEm == 'trustPer'):
        #trust - finding deviations from emotions percentage - rule 34
        epd = TrustDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule34'] = TrustDominantEmotionsPercentageDeviations.inner_rule_dict


        #trust - finding deviations from emotions so - rule 35
        esod = TrustDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(TrustDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule35'] = TrustDominantEmotionsSODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(TrustDominantEmotionsSODeviations.inner_rule_dict))


        #trust - finding deviations from polarity percentage - rule 36
        ppd = TrustDominantPolarityPercentageDeviations.deviations(pper)
        if(ppd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule36'] = TrustDominantPolarityPercentageDeviations.inner_rule_dict


        #trust - finding deviations from polarity so - rule 37
        psod = TrustDominantPolaritySODeviations.deviations(pso)
        if(psod == 1):
            pc = pc + 1
            e_visualization.append(dictCreatorPos(TrustDominantPolaritySODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule37'] = TrustDominantPolaritySODeviations.inner_rule_dict
            e_visualization.append(dictCreatorNeg(TrustDominantPolaritySODeviations.inner_rule_dict))
    


    #finding dominant polarity
    maxPolarity = max(pper, key=pper.get)

    #if dominant polarity is positive
    if(maxPolarity == 'positivePer'):
        #Positivity - finding deviations from emotions percentage - rule 38
        epd = PositivityDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule38'] = PositivityDominantEmotionsPercentageDeviations.inner_rule_dict


        #Positivity - finding deviations from emotions so - rule 39
        esod = PositivityDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            s_visualization.append(dictCreatorPos(PositivityDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule39'] = PositivityDominantEmotionsSODeviations.inner_rule_dict
            s_visualization.append(dictCreatorNeg(PositivityDominantEmotionsSODeviations.inner_rule_dict))

            
    #if dominant polarity is negative
    if(maxPolarity == 'negativePer'):
        #Negativity - finding deviations from emotions percentage - rule 40
        epd = NegativityDominantEmotionsPercentageDeviations.deviations(eper)
        if(epd == 1):
            pc = pc + 1
        else:
            npc = npc + 1
            rules['rule40'] = NegativityDominantEmotionsPercentageDeviations.inner_rule_dict


        #negativity - finding deviations from emotions so - rule 41
        esod = NegativityDominantEmotionsSODeviations.deviations(eso)
        if(esod == 1):
            pc = pc + 1
            s_visualization.append(dictCreatorPos(NegativityDominantEmotionsSODeviations.inner_rule_dict))
        else:
            npc = npc + 1
            rules['rule41'] = NegativityDominantEmotionsSODeviations.inner_rule_dict
        s_visualization.append(dictCreatorNeg(NegativityDominantEmotionsSODeviations.inner_rule_dict))



    popularity_measure = (pc/11)-(npc/11)
    return popularity_measure


def getRules():
    return rules


if __name__ == "__main__":

    print(measurePopularity("89.txt"))
    print()
    print(getRules())
    print()
    print(e_visualization)
    print()
    print(s_visualization)



