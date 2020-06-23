import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.Config as cms

process = cms.Process("skimEvents")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
)

#--------------------------------------------------------------------------------
# set input files

import os
import re

inputFile_regex = r"[a-zA-Z0-9_/:.-]*[a-zA-Z0-9-_]+.root"

inputFilePaths_miniaod = [
    '/hdfs/cms/store/mc/Phase2HLTTDRWinter20RECOMiniAOD/MinBias_TuneCP5_14TeV-pythia8/MINIAODSIM/PU200_110X_mcRun4_realistic_v3-v1/110000/'
]

inputFilePaths_raw = [
    '/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110000/',
    '/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110001/',
    '/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/',
]

# check if name of inputFile matches regular expression
def getFiles(inputFilePaths, inputFile_regex):
    inputFileNames = []
    for inputFilePath in inputFilePaths:
        files = [ os.path.join("file:%s" % inputFilePath, file) for file in os.listdir(inputFilePath) ]
        for file in files:
            inputFile_matcher = re.compile(inputFile_regex)
            if inputFile_matcher.match(file):
                inputFileNames.append(file)
    return inputFileNames

# get list of files with MINIAODSIM event content
inputFileNames_miniaod = getFiles(inputFilePaths_miniaod, inputFile_regex)
print("inputFileNames_miniaod = %s" % inputFileNames_miniaod)
process.source.fileNames = cms.untracked.vstring(inputFileNames_miniaod)

# get list of files with RAW event content
inputFileNames_raw = getFiles(inputFilePaths_raw, inputFile_regex)
print("inputFileNames_raw = %s" % inputFileNames_raw)
process.source.secondaryFileNames = cms.untracked.vstring(inputFileNames_raw)
#--------------------------------------------------------------------------------

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.skimSequence = cms.Sequence()

process.runLumiSectionEventNumberFilter = cms.EDFilter("RunLumiSectionEventNumberFilter",
    runLumiSectionEventNumberFileName = cms.string("/home/veelken/Phase2HLT/CMSSW_11_1_0_pre6/src/HLTTrigger/Phase2HLTPFTaus/test/selEvents_debugRate.txt"),
    separator = cms.string(":")
)
process.skimSequence += process.runLumiSectionEventNumberFilter

process.skim_path = cms.Path(process.skimSequence)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Output definition
process.RECOoutput = cms.OutputModule("PoolOutputModule",
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('selEvents_debugRate_MINIAODSIM-RAW.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('skim_path')
    ),
    outputCommands = cms.untracked.vstring(
        'keep *',
    )
)

process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.endjob_step = cms.EndPath(process.endOfProcess)

