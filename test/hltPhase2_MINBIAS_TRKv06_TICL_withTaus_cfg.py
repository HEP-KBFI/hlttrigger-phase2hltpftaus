# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --geometry Extended2026D49 --era Phase2C9 --conditions auto:phase2_realistic_T15 --processName RECO2 --step RAW2DIGI,RECO --eventcontent RECO --datatier RECO --filein /store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/8A31EE8B-FC0F-A949-8340-58E2ABD2F30F.root --mc --nThreads 4 --nStreams 4 --no_exec -n 10 --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --customise JMETriggerAnalysis/Common/hltPhase2_TRKv06.customize_hltPhase2_TRKv06 --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_JME --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_TICL --customise_commands process.schedule.remove(process.RECOoutput_step)\ndel process.RECOoutput\ndel process.RECOoutput_step\n --python_filename hltPhase2_MINBIAS_TRKv06_TICL_NoskimmedTracks_cfg.py
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('RECO2',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#--------------------------------------------------------------------------------
# CV: switch between offline-like and Pixel vertices

vertices = "OfflineVertices"
#vertices = "OnlineVertices"
#vertices = "OnlineVerticesTrimmed"

srcVertices = None
if vertices == "OfflineVertices":
    srcVertices = "offlinePrimaryVertices"
elif vertices == "OnlineVertices":
    srcVertices = "hltPhase2PixelVertices"
elif vertices == "OnlineVerticesTrimmed":
    srcVertices = "hltPhase2TrimmedPixelVertices"
else:
    raise ValueError("Invalid configuration parameter vertices = '%s' !!" % vertices)
#--------------------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt_120to170_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/20000/EABECFB8-B05F-1F40-98A2-B174A99FD5C2.root')
    #fileNames = cms.untracked.vstring('file:/hdfs/cms/store/mc/Run3Winter20DRPremixMiniAOD/WJetsToLNu_TuneCP5_14TeV-amcatnloFXFX-pythia8/GEN-SIM-RAW/110X_mcRun3_2021_realistic_v6-v1/20000/778690DC-AB99-1849-9E7D-36FB30A546F7.root')
    fileNames = cms.untracked.vstring('file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/10000/FF49837E-DFAA-F247-B065-0D3A2FDCFD02.root')
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(8),
    numberOfThreads = cms.untracked.uint32(8),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)

# Output definition
process.RECOoutput = cms.OutputModule("PoolOutputModule",
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('step3_RAW2DIGI_RECO.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('reconstruction_step')
    ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ak4GenJets*_*_*',                   ## PRESENT ONLY IN RAW
        'keep *_hltGtStage2Digis*_*_*',             ## PRESENT ONLY IN RAW
        'keep *_hltTriggerSummaryRAW*_*_*',         ## PRESENT ONLY IN RAW
        'keep *_ak4PFJetsCorrected*_*_*',           ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_hlt*Tau*_*_*',                      ## PRODUCED BY addHLTPFTaus FUNCTION BELOW
        'keep *_particleFlowTmp_*_*',               ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_muons1stStep_*_*',                  ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_electronGsfTracks_*_*',             ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_generalTracks_*_*',                 ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_offlinePrimaryVertices_*_*',        ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_hltPhase2PixelVertices_*_*',        ## PRODUCED BELOW
        'keep *_hltPhase2TrimmedPixelVertices_*_*', ## PRODUCED BELOW
        'keep *_hltKT6PFJets_*_*',                  ## PRODUCED BELOW
        'keep *_hltPFMET*_*_*',                     ## PRODUCED BELOW
        'keep *_hltPuppiMET*_*_*',                  ## PRODUCED BELOW
        'keep *_prunedGenParticles_*_*',            ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_ak4GenJets_*_*',                    ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_ak8GenJets_*_*',                    ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedGenJets__*',                 ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedTaus_*_*',                   ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedJets_*_*',                   ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_packedPFCandidates_*_*',            ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedAddPileupInfo_*_*',          ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_offlineSlimmedPrimaryVertices_*_*', ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_generatorSmeared_*_*',              ## CV: ALLOWS TO PRODUCE FULL COLLECTION OF genParticles FOR DEBUGGING PURPOSES 
        'keep *_generator_*_*',                     ## CV: NEEDED TO MAKE PTHAT PLOTS FOR QCD MULTIJET MC SAMPLES
    )
)

process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.hltPhase2_TRKv06
from JMETriggerAnalysis.Common.hltPhase2_TRKv06 import customize_hltPhase2_TRKv06 

#call to customisation function customize_hltPhase2_TRKv06 imported from JMETriggerAnalysis.Common.hltPhase2_TRKv06
process = customize_hltPhase2_TRKv06(process)

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.hltPhase2_JME
from JMETriggerAnalysis.Common.hltPhase2_JME import customize_hltPhase2_JME,customize_hltPhase2_TICL 

#call to customisation function customize_hltPhase2_JME imported from JMETriggerAnalysis.Common.hltPhase2_JME
process = customize_hltPhase2_JME(process)

#call to customisation function customize_hltPhase2_TICL imported from JMETriggerAnalysis.Common.hltPhase2_JME
process = customize_hltPhase2_TICL(process)

#--------------------------------------------------------------------------------
# CV: run HLT Pixel vertex reconstruction
process.load("HLTTrigger.Phase2HLTPFTaus.hltPixelVertices_cff")
process.reconstruction_step.replace(process.offlinePrimaryVertices, process.offlinePrimaryVertices + process.hltPhase2PixelTracksSequence + process.hltPhase2PixelVerticesSequence)

# CV: switch vertex collection in particle-flow algorithm
if srcVertices != "offlinePrimaryVertices":
    print("Switching all vertex-related InputTags in 'reconstruction_step' path from '%s' to '%s'..." % ('offlinePrimaryVertices', srcVertices))
    from FWCore.ParameterSet.MassReplace import massSearchReplaceAnyInputTag
    massSearchReplaceAnyInputTag(process.reconstruction_step, 'offlinePrimaryVertices', srcVertices)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# CV: add HLT tau reconstruction
process.taucustomreco = cms.Sequence()

# run HLT tau reconstruction
from HLTTrigger.Phase2HLTPFTaus.tools.addHLTPFTaus import addHLTPFTaus
srcPFCandidates = "particleFlowTmp"
for algorithm in [ "hps", "shrinking-cone" ]:
  for isolation_maxDeltaZOption in [ "primaryVertex", "leadTrack" ]:
    for isolation_minTrackHits in [ 3, 5, 8 ]:  

      suffix = "%iHits" % isolation_minTrackHits
      isolation_maxDeltaZ            = None
      isolation_maxDeltaZToLeadTrack = None
      if isolation_maxDeltaZOption == "primaryVertex":
        isolation_maxDeltaZ            =  0.15 # value optimized for offline tau reconstruction at higher pileup expected during LHC Phase-2
        isolation_maxDeltaZToLeadTrack = -1.   # disabled
        suffix += "MaxDeltaZ"
      elif isolation_maxDeltaZOption == "leadTrack":
        isolation_maxDeltaZ            = -1.   # disabled
        isolation_maxDeltaZToLeadTrack =  0.15 # value optimized for offline tau reconstruction at higher pileup expected during LHC Phase-2
        suffix += "MaxDeltaZToLeadTrack"
      else:
        raise ValueError("Invalid parameter isolation_maxDeltaZOption = '%s' !!" % isolation_maxDeltaZOption)
      if srcVertices == "offlinePrimaryVertices":
        suffix += "WithOfflineVertices"
      elif srcVertices == "hltPhase2PixelVertices":
        suffix += "WithOnlineVertices"
      elif srcVertices == "hltPhase2TrimmedPixelVertices":
        suffix += "WithOnlineVerticesTrimmed"
      else:
        raise ValueError("Invalid parameter srcVertices = '%s' !!" % srcVertices)        
        
      pftauSequence = addHLTPFTaus(process, algorithm, srcPFCandidates, srcVertices, 
        isolation_maxDeltaZ, isolation_maxDeltaZToLeadTrack, isolation_minTrackHits, 
        suffix)
      process.taucustomreco += pftauSequence

process.reconstruction_step += process.taucustomreco

# CV: add kt6PFJets for rho computation
from RecoJets.JetProducers.kt6PFJets_cfi import kt6PFJets
process.hltKT6PFJets = kt6PFJets.clone(
    src = cms.InputTag("particleFlowTmp"),
    doRhoFastjet = cms.bool(True)
)
process.reconstruction_step += process.hltKT6PFJets

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#--------------------------------------------------------------------------------

# End of customisation functions

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

##dump_file = open('dump.py','w')
##dump_file.write(process.dumpPython())

#Setup FWK for multithreaded
process.options.numberOfThreads = cms.untracked.uint32(8)
process.options.numberOfStreams = cms.untracked.uint32(8)
process.options.numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1)









