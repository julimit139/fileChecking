import dataExtractionModified
import artifactDetection


# dataPath = "D:\Data\PD_512\PD144.txt"
dataPath = "D:\PD_512Hz from 1_06_2020 to 31_03_2021\PD167.txt"
data = dataExtractionModified.extractData(dataPath)
inputData = data[0]
examinationTime = data[1]
samplingRate = data[2]
eegChannelNumber = data[4]

resultEEP = artifactDetection.performEEPDetection(inputData, eegChannelNumber, examinationTime, samplingRate)
listResultEEP = resultEEP[0]
print("List length: " + str(len(listResultEEP)))
print("True elements number: " + str(listResultEEP.count(True)))

resultLFP = artifactDetection.performLFPDetection(inputData, eegChannelNumber, examinationTime, samplingRate, 0.625,
                                                  samplingRate/2, 50)
listResultLFP = resultLFP[0]
print("List length: " + str(len(listResultLFP)))
print("True elements number: " + str(listResultLFP.count(True)))