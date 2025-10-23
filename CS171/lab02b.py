import math

def yarnRequired(skeinWeight, swatchLength, swatchWidth, swatchWeight, projectLength, projectWidth):
    swatchSize = swatchLength * swatchWidth
    projectSize = projectLength * projectWidth
    swatchYarn = swatchWeight / swatchSize
    yarnRequired = swatchYarn * projectSize * 1.1
    skeinsRequired = math.ceil(yarnRequired / skeinWeight)
    
    return skeinsRequired


    
    
