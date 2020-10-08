# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --geometry Extended2026D49 --era Phase2C9 --conditions auto:phase2_realistic_T15 --processName RECO2 --step RAW2DIGI,RECO --eventcontent RECO --datatier RECO --filein /store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/003ACFBC-23B2-EA45-9A12-BECFF07760FC.root --mc --nThreads 4 --nStreams 4 --no_exec -n 10 --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000, Configuration/DataProcessing/Utils.addMonitoring --customise CMS_HLT_Phase2_Tracking/Configs/phase2_tracking.customise_hltPhase2_TRKv06_1 --no_exec --python_filename hlt_phase2_tracking_v6p1.py
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
srcBeamSpot = None
if vertices == "OfflineVertices":
    srcVertices = 'offlinePrimaryVertices'
    srcBeamSpot = 'offlineBeamSpot'
elif vertices == "OnlineVertices":
    srcVertices = 'hltPhase2PixelVertices'
    srcBeamSpot = 'hltOnlineBeamSpot'
elif vertices == "OnlineVerticesTrimmed":
    srcVertices = 'hltPhase2TrimmedPixelVertices'
    srcBeamSpot = 'hltOnlineBeamSpot'
else:
    raise ValueError("Invalid configuration parameter vertices = '%s' !!" % vertices)

# CV: enable/disable L1 emulator
#runL1Emulator = False
runL1Emulator = True
#--------------------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/003ACFBC-23B2-EA45-9A12-BECFF07760FC.root'
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20RECOMiniAOD/MinBias_TuneCP5_14TeV-pythia8/MINIAODSIM/PU200_110X_mcRun4_realistic_v3-v1/110000/054D8F53-89B2-E143-B106-FD85AC2F1F4B.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/534D3139-A254-E24B-A125-3C176575E2DB.root',
    )
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
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    #fileName = cms.untracked.string('step3_RAW2DIGI_RECO.root'),
    #outputCommands = process.RECOEventContent.outputCommands,
    #splitLevel = cms.untracked.int32(0)

    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('NTuple_produce_HLT_Taus_and_L1Taus.root'),
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
        'keep *_muons1stStep_*_*',                  ## KEEP REFERENCE TO reco::Track COLLECTIONS FOR ALL TYPES OF MUONS USED AS INPUT TO PARTICLE-FLOW ALGORITHM
        'keep *_globalMuons_*_*',                   ## KEEP REFERENCE TO reco::Track COLLECTIONS FOR ALL TYPES OF MUONS USED AS INPUT TO PARTICLE-FLOW ALGORITHM
        'keep *_standAloneMuons_*_*',               ## KEEP REFERENCE TO reco::Track COLLECTIONS FOR ALL TYPES OF MUONS USED AS INPUT TO PARTICLE-FLOW ALGORITHM
        'keep *_tevMuons_*_*',                      ## KEEP REFERENCE TO reco::Track COLLECTIONS FOR ALL TYPES OF MUONS USED AS INPUT TO PARTICLE-FLOW ALGORITHM
        'keep *_electronGsfTracks_*_*',             ## KEEP REFERENCE TO reco::GsfTrack COLLECTION FOR ELECTRONS USED AS INPUT TO PARTICLE-FLOW ALGORITHM
        'keep *_generalTracks_*_*',                 ## KEEP REFERENCE TO reco::Track COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_offlinePrimaryVertices_*_*',        ## KEEP REFERENCE TO reco::Vertex COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION 
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
        'keep *_addPileupInfo_*_*',                 ## PRESENT ONLY IN RAW
        'keep *_offlineSlimmedPrimaryVertices_*_*', ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_generatorSmeared_*_*',              ## CV: ALLOWS TO PRODUCE FULL COLLECTION OF genParticles FOR DEBUGGING PURPOSES 
        'keep *_generator_*_*',                     ## CV: NEEDED TO MAKE PTHAT PLOTS FOR QCD MULTIJET MC SAMPLES
        'keep *_L1HPSPFTauProducer*PF_*_*',         ## ADDED BY L1 EMULATOR
        'keep *_l1pfCandidates_PF_*',               ## ADDED BY L1 EMULATOR
        'keep *_l1pfProducer*_z0_*',                ## ADDED BY L1 EMULATOR
        'keep *_pfTracksFromL1Tracks*_*_*',         ## ADDED BY L1 EMULATOR
        'keep *_pfClustersFrom*_*_*',               ## ADDED BY L1 EMULATOR
        'keep *_TTTracksFromTracklet_*_*',          ## ADDED BY L1 EMULATOR
        'keep *_VertexProducer_*_*',                ## ADDED BY L1 EMULATOR
        'keep *_ak4PFL1PF_*_*',                     ## ADDED BY L1 EMULATOR
        'keep *_ak4PFL1PFCorrected_*_*',            ## ADDED BY L1 EMULATOR
        'keep *_kt6L1PFJetsPF_rho_*',               ## ADDED BY L1 EMULATOR
        'keep *_kt6L1PFJetsNeutralsPF_rho_*',       ## ADDED BY L1 EMULATOR
        'keep *_l1pfCandidates_PF_*',               ## ADDED BY L1 EMULATOR
        'keep *_l1pfCandidates_Puppi_*',            ## ADDED BY L1 EMULATOR
        'keep *_L1TkPrimaryVertex_*_*',             ## ADDED BY L1 EMULATOR
        'keep *_L1HPSPFTauProducer*PF_*_*',         ## ADDED BY L1 EMULATOR
        'keep *_L1HPSPFTauProducer*Puppi_*_*',      ## ADDED BY L1 EMULATOR
    )

)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
#process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(4)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from CMS_HLT_Phase2_Tracking.Configs.phase2_tracking
from CMS_HLT_Phase2_Tracking.Configs.phase2_tracking import customise_hltPhase2_TRKv06_1 

#call to customisation function customise_hltPhase2_TRKv06_1 imported from CMS_HLT_Phase2_Tracking.Configs.phase2_tracking
process = customise_hltPhase2_TRKv06_1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.hltPhase2_JME
from JMETriggerAnalysis.Common.hltPhase2_JME import customise_hltPhase2_JME

#call to customisation function customise_hltPhase2_JME imported from JMETriggerAnalysis.Common.hltPhase2_JME
process = customise_hltPhase2_JME(process)

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.customiseHLTForPhase2 
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_enableTICLInHGCalReconstruction

#call to customisation function customise_hltPhase2_enableTICLInHGCalReconstruction imported from JMETriggerAnalysis.Common.customiseHLTForPhase2 
process = customise_hltPhase2_enableTICLInHGCalReconstruction(process) 

#--------------------------------------------------------------------------------
# CV: run HLT Pixel vertex reconstruction
#process.load("HLTrigger.Phase2HLTPFTaus.hltPixelVertices_cff")
#process.reconstruction_step.replace(process.offlinePrimaryVertices, process.offlinePrimaryVertices + process.hltPhase2PixelTracksSequence + process.hltPhase2PixelVerticesSequence)
#process.reconstruction_step += process.offlinePrimaryVertices
#process.reconstruction_step += process.hltPhase2PixelTracksSequence
#process.reconstruction_step += process.hltPhase2PixelVerticesSequence

# CV: switch vertex collection in particle-flow algorithm
if srcVertices != "offlinePrimaryVertices":
    print("Switching all vertex-related InputTags in 'reconstruction_step' path from '%s' to '%s'..." % ('offlinePrimaryVertices', srcVertices))
    from FWCore.ParameterSet.MassReplace import massSearchReplaceAnyInputTag
    massSearchReplaceAnyInputTag(process.reconstruction_step, 'offlinePrimaryVertices', srcVertices)
#--------------------------------------------------------------------------------


#-------------------------------------------------------------------------------- 
# CV: run L1 trigger emulator and produce L1 HPS PF Tau objects
if runL1Emulator:
    process.load('L1Trigger.Phase2L1Taus.l1emulator_cff')
    process.l1emulatorSequence = cms.Sequence(process.l1emulator)

    # SB: produce L1 HPS PF Tau objects                                                                                                                                                                                                                                         
    from L1Trigger.Phase2L1Taus.L1HPSPFTauProducerPF_cfi import L1HPSPFTauProducerPF
    from L1Trigger.Phase2L1Taus.L1HPSPFTauProducerPuppi_cfi import L1HPSPFTauProducerPuppi
    for useStrips in [ True, False ]:
        moduleNameBase = "L1HPSPFTauProducer"
        if useStrips:
            moduleNameBase += "WithStrips"
        else:
            moduleNameBase += "WithoutStrips"

        moduleNamePF = moduleNameBase + "PF"
        modulePF = L1HPSPFTauProducerPF.clone(
            useStrips = cms.bool(useStrips),
            applyPreselection = cms.bool(False),
            debug = cms.untracked.bool(False)
        )
        setattr(process, moduleNamePF, modulePF)
        process.l1emulatorSequence += getattr(process, moduleNamePF)

    process.reconstruction_step += process.l1emulatorSequence
#-------------------------------------------------------------------------------- 



#--------------------------------------------------------------------------------
# CV: add HLT tau reconstruction
process.taucustomreco = cms.Sequence()

# run HLT tau reconstruction
from HLTrigger.Phase2HLTPFTaus.tools.addHLTPFTaus import addHLTPFTaus
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

      pftauSequence = addHLTPFTaus(process, algorithm,
        srcPFCandidates, srcVertices, srcBeamSpot,
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
#--------------------------------------------------------------------------------

##process.dumpEventContent = cms.EDAnalyzer('EventContentAnalyzer')
##process.reconstruction_step += process.dumpEventContent

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#--------------------------------------------------------------------------------

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


dump_file = open('dump.py','w')
dump_file.write(process.dumpPython())

#Setup FWK for multithreaded
process.options.numberOfThreads = cms.untracked.uint32(8)
process.options.numberOfStreams = cms.untracked.uint32(8)
process.options.numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1)



