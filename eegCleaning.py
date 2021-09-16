import numpy as np
import pandas as pd
import fileCreating


def cleanData(inputData, samplingRate, isArtifactList):
    artifactsCoordinates = fileCreating.markArtifacts(isArtifactList, samplingRate)
    print("Artifact list: " + str(len(artifactsCoordinates)))
    df = pd.DataFrame(inputData)
    print(df)
    toDrop = []
    for coordinates in artifactsCoordinates:
        toDrop += list(range(coordinates[0], coordinates[1]))
    print("toDrop length:")
    print(len(toDrop))
    data = df.drop(toDrop)
    print(data)
    cleanData = data.to_numpy()
    return cleanData





