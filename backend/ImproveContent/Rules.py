import IncreaseAnger
import IncreaseAnt
import IncreaseDisgust
import IncreaseFear
import IncreaseJoy
import IncreaseSadness
import IncreaseSurprise
import IncreaseTrust
import IncreasePositivity
import IncreaseNegativity
import IncreaseSO
import DecreaseAnger
import DecreaseAnt
import DecreaseDisgust
import DecreaseFear
import DecreaseJoy
import DecreaseSadness
import DecreaseSurprise
import DecreaseTrust
import DecreasePositivity
import DecreaseNegativity
import DecreaseSO

#each emotions percentage
def rule1(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to lessen Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
        

    return recommendations

#each emotions SO
def rule2(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(IncreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        

    return recommendations


#each polarity percentages
def rule3(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#each polarity SO
def rule4(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(IncreaseNegativity.increaseAnger(file_name))

    return recommendations


#overall SO
def rule5(d, file_name):
    recommendations = []
    
    if(d['so'] == 0):
        recommendations.append(IncreaseSO.increaseAnger(file_name))

    return recommendations

#===================================================================================
#anger dominant - emotions percentages
def rule6(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to lessen Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to lessen Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#anger dominant - emotions so
def rule7(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(IncreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(IncreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#anger dominant - polarity percentages
def rule8(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#anger dominant - polarity so
def rule9(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(IncreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#ant dominant - emotions percentages
def rule10(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to lessen Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to lessen Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to increase Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to lessen Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to lessen Trust!')
     
    return recommendations

#ant dominant - emotions so
def rule11(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(IncreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#anger dominant - polarity percentages
def rule12(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Decrease Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Increase Negativity')

    return recommendations


#anger dominant - polarity so
def rule13(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(DecreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#disgust dominant - emotions percentages
def rule14(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#disgust dominant - emotions so
def rule15(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(DecreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(DecreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(DecreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#disgust dominant - polarity percentages
def rule16(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#disgust dominant - polarity so
def rule17(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(IncreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#fear dominant - emotions percentages
def rule18(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to lessen Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to lessen Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#fear dominant - emotions so
def rule19(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(IncreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append("Fear content seems ok!")

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#fear dominant - polarity percentages
def rule20(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#fear dominant - polarity so
def rule21(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(IncreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#joy dominant - emotions percentages
def rule22(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to lessen Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to increase Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to lessen Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to lessen Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#joy dominant - emotions so
def rule23(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(DecreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(DecreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(DecreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#joy dominant - polarity percentages
def rule24(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#joy dominant - polarity so
def rule25(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(DecreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#sadness dominant - emotions percentages
def rule26(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to lessen Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#sadness dominant - emotions so
def rule27(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(IncreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(IncreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#sadness dominant - polarity percentages
def rule28(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#sadness dominant - polarity so
def rule29(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(IncreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#surprise dominant - emotions percentages
def rule30(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to lessen Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to increase Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to lessen Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to increase Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to lessen Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#surprise dominant - emotions so
def rule31(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(DecreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(DecreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(DecreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(DecreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#surprise dominant - polarity percentages
def rule32(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Decrease Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Increase Negativity')

    return recommendations


#surprise dominant - polarity so
def rule33(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(DecreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#trust dominant - emotions percentages
def rule34(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to lessen Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to increase Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to lessen Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to increase Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to lessen Trust!')
     
    return recommendations

#trust dominant - emotions so
def rule35(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(DecreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(DecreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(DecreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations


#trust dominant - polarity percentages
def rule36(d):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append('Increase Positivity')

    if(d['negativity'] == 0):
        recommendations.append('Decrease Negativity')

    return recommendations


#trust dominant - polarity so
def rule37(d, file_name):
    recommendations = []
    
    if(d['positivity'] == 0):
        recommendations.append(IncreasePositivity.increaseAnger(file_name))

    if(d['negativity'] == 0):
        recommendations.append(DecreaseNegativity.increaseAnger(file_name))

    return recommendations

#========================================================================================

#positivity dominant - emotions percentages
def rule38(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to increase Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to increase Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#positivity dominant - emotions so
def rule39(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append(DecreaseAnger.increaseAnger(file_name))

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(DecreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(DecreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(IncreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations

#================================================================================

#negativity dominant - emotions percentages
def rule40(d):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Need to lessen Anger!')

    if(d['ant'] == 0):
        recommendations.append('Need to increase Anticipation!')

    if(d['disgust'] == 0):
        recommendations.append('Need to lessen Disgust!')

    if(d['fear'] == 0):
        recommendations.append('Need to increase Fear!')

    if(d['joy'] == 0):
        recommendations.append('Need to lessen Joy!')

    if(d['sadness'] == 0):
        recommendations.append('Need to lessen Sadness!')

    if(d['surprise'] == 0):
        recommendations.append('Need to increase Surprise!')

    if(d['trust'] == 0):
        recommendations.append('Need to increase Trust!')
     
    return recommendations

#negativity dominant - emotions so
def rule41(d, file_name):
    recommendations = []

    if(d['anger'] == 0):
        recommendations.append('Anger content is ok!')

    if(d['ant'] == 0):
        recommendations.append(IncreaseAnt.increaseAnger(file_name))

    if(d['disgust'] == 0):
        recommendations.append(IncreaseDisgust.increaseAnger(file_name))

    if(d['fear'] == 0):
        recommendations.append(DecreaseFear.increaseAnger(file_name))

    if(d['joy'] == 0):
        recommendations.append(IncreaseJoy.increaseAnger(file_name))

    if(d['sadness'] == 0):
        recommendations.append(IncreaseSadness.increaseAnger(file_name))

    if(d['surprise'] == 0):
        recommendations.append(DecreaseSurprise.increaseAnger(file_name))

    if(d['trust'] == 0):
        recommendations.append(IncreaseTrust.increaseAnger(file_name))
        
    return recommendations

#================================================================================












