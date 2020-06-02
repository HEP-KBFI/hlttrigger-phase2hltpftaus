import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets 

from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import PFTauQualityCuts
from RecoTauTag.RecoTau.RecoTauJetRegionProducer_cfi import RecoTauJetRegionProducer
from RecoTauTag.RecoTau.PFRecoTauChargedHadronProducer_cff import ak4PFJetsRecoTauChargedHadrons
import RecoTauTag.RecoTau.PFRecoTauChargedHadronBuilderPlugins_cfi as builders
import RecoTauTag.RecoTau.PFRecoTauChargedHadronQualityPlugins_cfi as ranking
from RecoTauTag.RecoTau.RecoTauPiZeroProducer_cff import ak4PFJetsLegacyHPSPiZeros
from RecoTauTag.RecoTau.PFRecoTauProducer_cfi.py import pfRecoTauProducer
from RecoTauTag.RecoTau.RecoTauCombinatoricProducer_cfi import *
from RecoTauTag.RecoTau.PFRecoTauProducer_cfi.py import pfRecoTauProducer
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByHPSSelection_cfi import *
from RecoTauTag.RecoTau.RecoTauCleaner_cfi import RecoTauCleaner
import RecoTauTag.RecoTau.RecoTauCleanerPlugins as cleaners
from RecoTauTag.RecoTau.RecoTauPiZeroUnembedder_cfi import RecoTauPiZeroUnembedder
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingObjectPtCut_cfi import pfRecoTauDiscriminationByLeadingObjectPtCut
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByIsolation_cfi import pfRecoTauDiscriminationByIsolation
from RecoTauTag.RecoTau.PFTauSelector_cfi import pfTauSelector

#--------------------------------------------------------------------------------
# Define parameters of "hadron-plus-strips" (HPS) and shrinking-cone (SC) tau reconstruction algorithms

# CV: pT thresholds for charged PFCandidates to be considered when building tau candidate (minSignalTrackPt) 
#     and when computing the isolation of the tau candidate (minIsolationTrackPt)
#     Both thresholds are set to pT > 0.9 by default, motivated by this presentation
#       https://indico.cern.ch/event/921383/contributions/3879407/attachments/2044996/3426284/200526_hltupg_jme.pdf
#    (cf. "TRK v6" and "TRK v6 + skimTrk" on slides 3 and 5)
minSignalTrackPt      = 0.9
minIsolationTrackPt   = 0.9

signalConeSize_hps    = "min(max(3.6/pt(), 0.08), 0.12)"
signalConeSize_sc     = "min(max(3.6/pt(), 0.08), 0.12)"

isolationConeSize_hps = 0.5
isolationConeSize_sc  = 0.5
#--------------------------------------------------------------------------------

def addPFTauDiscriminator(process, discriminatorName, discriminator, pftauDiscriminators, pftauSequence):
    setattr(process, discriminatorName, discriminator)
    pftauSequence += discriminator
    pftauDiscriminators.append(discriminatorName)
    return discriminator

def addPFTauSelector(process, selectorName, srcPFTaus, pftauDiscriminators, pftauSequence):
    selector = pfTauSelector.clone(
        src = cms.InputTag(srcPFTaus),
        cut = cms.string("pt > 15.0 & abs(eta) < 2.1"),  
        discriminators = cms.VPSet([ cms.PSet( 
            discriminator = cms.InputTag(pftauDiscriminator), 
            selectionCut = cms.double(0.5) 
        ) for pftauDiscriminator in pftauDiscriminators ])
    )
    setattr(process, selectorName, selector)
    pftauSequence += selector
    return selector

def addHLTPFTaus(process, algorithm, srcPFCandidates, srcPixelVertices):
    pfTauLabel = None
    if algorithm == "shrinking-cone":
        pfTauLabel = "PFTau"
    elif algorithm == "hps":
        pfTauLabel = "HpsPFTau"
    else:
        raise ValueError("Invalid parameter algorithm = '%s' !!" % algorithm)

    pftauSequence = cms.Sequence()

    hltQualityCuts = PFTauQualityCuts.clone()
    hltQualityCuts.signalQualityCuts.minTrackPt = cms.double(minSignalTrackPt)
    hltQualityCuts.isolationQualityCuts.minTrackPt = cms.double(minIsolationTrackPt)
    hltQualityCuts.primaryVertexSrc = cms.InputTag(srcPixelVertices)

    from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets 
    hltPFTauAK4PFJets = ak4PFJets.clone(
        src = cms.InputTag(srcPFCandidates),
        srcPVs = cms.InputTag(srcPixelVertices)
    )
    srcPFTauAK4PFJets = "hlt%sAK4PFJets" % pfTauLabel
    setattr(process, srcPFTauAK4PFJets, hltPFTauAK4PFJets)
    pftauSequence += hltPFTauAK4PFJets

    hltPFTau08Region = RecoTauJetRegionProducer.clone(
        src = cms.InputTag(srcPFTauAK4PFJets),
        pfCandSrc = cms.InputTag(srcPFCandidates)
    )
    srcPFTau08Region = "hlt%sPFJets08Region" % pfTauLabel
    setattr(process, srcPFTau08Region, hltPFTau08Region)
    pftauSequence += hltPFTau08Region

    hltPFTauPFJetsRecoTauChargedHadrons = ak4PFJetsRecoTauChargedHadrons.clone(
        jetSrc = cms.InputTag(srcPFTauAK4PFJets),
        minJetPt = cms.double(15.0),
        maxJetAbsEta = cms.double(2.5),
        outputSelection = cms.string('pt > %1.2f' % minSignalTrackPt),
        builders = cms.VPSet(
            builders.chargedPFCandidates
        ),
        ranking = cms.VPSet(
            ranking.isChargedPFCandidate
        )
    )
    srcPFTauPFJetsRecoTauChargedHadrons = "hlt%sPFJetsRecoTauChargedHadrons" % pfTauLabel
    setattr(process, srcPFTauPFJetsRecoTauChargedHadrons, hltPFTauPFJetsRecoTauChargedHadrons)
    pftauSequence += hltPFTauPFJetsRecoTauChargedHadrons

    hltPFTauPiZeros = ak4PFJetsLegacyHPSPiZeros.clone(
        jetSrc = cms.InputTag(srcPFTauAK4PFJets)
    )
    hltPFTauPiZeros.builders[0].qualityCuts = hltQualityCuts
    srcPFTauPiZeros = "hlt%sPiZeros" % pfTauLabel
    setattr(process, srcPFTauPiZeros, hltPFTauPiZeros)
    pftauSequence += hltPFTauPiZeros

    srcPFTausTmp = None
    if algorithm == "shrinking-cone":
        hltPFTausSansRef = combinatoricRecoTaus.clone(      
            jetSrc = cms.InputTag(srcPFTauAK4PFJets),
            minJetPt = cms.doube(15.0),
            maxJetAbsEta = cms.doube(2.5),
            jetRegionSrc = cms.InputTag(srcPFTau08Region),
            chargedHadronSrc = cms.InputTag(srcPFTauPFJetsRecoTauChargedHadrons),
            piZeroSrc = cms.InputTag(srcPFTauPiZeros),
            builders = cms.VPSet(cms.PSet( 
                plugin = cms.string("RecoTauBuilderConePlugin"),
                name = cms.string("shrinkingConeTau"),
                matchingCone = cms.string("0.3"),
                pfCandSrc = cms.InputTag(srcPFCandidates),
                usePFLeptons = cms.bool(True),
                leadObjectPt = cms.double(minSignalTrackPt),
                signalConeChargedHadrons = cms.string(signalConeSize_shrinking_cone),
                maxSignalConeChargedHadrons = cms.int32(3),
                signalConeNeutralHadrons = cms.string("0.1"),
                signalConePiZeros = cms.string(signalConeSize_shrinking_cone),                
                minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
                minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
                isoConeChargedHadrons = cms.string("%1.2f" % isolationConeSize_sc),
                isoConeNeutralHadrons = cms.string("%1.2f" % isolationConeSize_sc),
                isoConePiZeros = cms.string("%1.2f" % isolationConeSize_sc),
                qualityCuts = hltQualityCuts,
            )),
            modifiers = cms.VPSet()
        )
        srcPFTausSansRef = "hlt%ssSansRef" % pfTauLabel
        setattr(process, srcPFTausSansRef, hltPFTausSansRef)
        pftauSequence += hltPFTausSansRef
        srcPFTausTmp = srcPFTausSansRef 
    elif algorithm == "hps":
        hltCombinatoricRecoTaus = combinatoricRecoTaus.clone(      
            jetSrc = cms.InputTag(srcPFTauAK4PFJets),
            minJetPt = cms.doube(15.0),
            maxJetAbsEta = cms.doube(2.5),
            jetRegionSrc = cms.InputTag(srcPFTau08Region),
            chargedHadronSrc = cms.InputTag(srcPFTauPFJetsRecoTauChargedHadrons),
            piZeroSrc = cms.InputTag(srcPFTauPiZeros),
            builders = cms.VPSet(cms.PSet(
                name = cms.string("combinatoric"),
                plugin = cms.string("RecoTauBuilderCombinatoricPlugin"),
                pfCandSrc = cms.InputTag(srcPFCandidates),
                isolationConeSize = cms.double(isolationConeSize_hps),
                qualityCuts = hltQualityCuts,
                decayModes = cms.VPSet(
                    combinatoricDecayModeConfigs.config1prong0pi0,
                    combinatoricDecayModeConfigs.config1prong1pi0,
                    combinatoricDecayModeConfigs.config1prong2pi0,
                    ##combinatoricDecayModeConfigs.config2prong0pi0,
                    ##combinatoricDecayModeConfigs.config2prong1pi0,
                    combinatoricDecayModeConfigs.config3prong0pi0,
       	            ##combinatoricDecayModeConfigs.config3prong1pi0
                ),
                signalConeSize = cms.string(signalConeSize_hps),
                minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
                minRelPhotonSumPt_insideSignalCone = cms.double(0.10),
                minAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
                minRelPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
                verbosity = cms.int32(0)
            )),
            modifiers = cms.VPSet(cms.PSet(  
                name = cms.string("tau_mass"),
                plugin = cms.string("PFRecoTauMassPlugin"),
                verbosity = cms.int32(0)
            ))
        )
        srcCombinatoricRecoTaus = "hlt%sCombinatoricProducer"
        setattr(process, srcCombinatoricRecoTaus, hltCombinatoricRecoTaus)
        pftauSequence += hltCombinatoricRecoTaus

        hltPFTauSelectionDiscriminator = hpsSelectionDiscriminator.clone(
            PFTauProducer = cms.InputTag(srcCombinatoricRecoTaus),
            # CV: mass-window cuts taken from configuation used for HLT tau trigger during LHC Run 2
            decayModes = cms.VPSet(
                decayMode_1Prong0Pi0.clone(
                    maxMass = cms.string("1.")
                ),
                decayMode_1Prong1Pi0.clone(
                    maxMass = cms.string("max(1.72, min(1.72*sqrt(pt/100.), 4.2))")
                ),
                decayMode_1Prong2Pi0.clone(
                    maxMass = cms.string("max(1.72, min(1.72*sqrt(pt/100.), 4.0))")
                ),
                ##decayMode_2Prong0Pi0.clone(
                ##    maxMass = cms.string("1.2")
                ##),
                ##decayMode_2Prong1Pi0.clone(
                ##    maxMass = cms.string("max(1.6, min(1.6*sqrt(pt/100.), 4.0))")
                ##),
                decayMode_3Prong0Pi0.clone(
                    maxMass = cms.string("1.6")
                ),
                ##decayMode_3Prong1Pi0.clone(
                ##    maxMass = cms.string("1.6")
                ##)
            ),
            requireTauChargedHadronsToBeChargedPFCands = cms.bool(True)
        )
        srcPFTauSelectionDiscriminatorByHPS = "hlt%sSelectionDiscriminatorByHPS" % pfTauLabel
        setattr(process, srcPFTauSelectionDiscriminatorByHPS, hltPFTauSelectionDiscriminator)
        pftauSequence += hltPFTauSelectionDiscriminator

        hltPFTauCleaner = RecoTauCleaner.clone(
            src = cms.InputTag(hltCombinatoricRecoTaus),
            cleaners = cms.VPSet(
                cms.PSet(  
                    name = cms.string("HPS_Select"),
                    plugin = cms.string("RecoTauDiscriminantCleanerPlugin"),
                    src = cms.InputTag(srcPFTauSelectionDiscriminatorByHPS)
                ),
                cleaners.killSoftTwoProngTaus,
                cleaners.chargedHadronMultiplicity,
                cleaners.stripMultiplicity,
                cleaners.chargeIsolation
            )
        )
        srcPFTauCleaner = "hlt%sCleaner" % pfTauLabel
        setattr(process, srcPFTauCleaner, hltPFTauCleaner)
        pftauSequence += hltPFTauCleaner
        srcPFTausTmp = srcPFTauCleaner
    else:
        raise ValueError("Invalid parameter algorithm = '%s' !!" % algorithm)

    hltPFTaus = RecoTauPiZeroUnembedder.clone(
        src = cms.InputTag(srcPFTausTmp)
    )
    srcPFTaus = "hlt%ss" % pfTauLabel
    setattr(process, srcPFTaus, hltPFTaus)
    pftauSequence += srcPFTaus

    pftauDiscriminators = []

    hltPFTauDiscriminatorByTrackFinding = addPFTauDiscriminator(process, "hlt%sDiscriminatorByTrackFinding" % pfTauLabel,
        pfRecoTauDiscriminationByLeadingObjectPtCut.clone(
            PFTauProducer = cms.InputTag(srcPFTaus_passingLastDiscriminator),
            UseOnlyChargedHadrons = cms.bool(True),
            MinPtLeadingObject = cms.double(0.0)
        ),
        pftauDiscriminators, pftauSequence)
    hltPFTausPassingTrackFinding = addPFTauSelector(process, "hlt%ssPassingTrackFinding" % pfTauLabel,
        pftauDiscriminators, pftauSequence)

    hltPFTauDiscriminatorByTrackPtGt5 = addPFTauDiscriminator(process, "hlt%sDiscriminatorByTrackPtGt5" % pfTauLabel,
        pfRecoTauDiscriminationByLeadingObjectPtCut.clone(
            PFTauProducer = cms.InputTag(srcPFTaus),
            UseOnlyChargedHadrons = cms.bool(True),
            MinPtLeadingObject = cms.double(5.0)
        ),
        pftauDiscriminators, pftauSequence)
    hltPFTausPassingTrackPtGt5 = addPFTauSelector(process, "hlt%ssPassingTrackPtGt5" % pfTauLabel,
        pftauDiscriminators, pftauSequence)
       
    hltSelectedPFTaus = addPFTauSelector(process, "hltSelected%ss" % pfTauLabel,
        pftauDiscriminators, pftauSequence)
    srcSelectedPFTaus = hltSelectedPFTaus.label()

    # CV: do not cut on charged isolation, but store charged isolation pT-sum in output file instead
    hltPFTauChargedIsolation = addPFTauDiscriminator(process, "hlt%sChargedIsolation" % pfTauLabel,
        pfRecoTauDiscriminationByIsolation.clone( 
            PFTauProducer = cms.InputTag(srcSelectedPFTaus),
            particleFlowSrc = cms.InputTag(srcPFCandidates),
            vertexSrc = cms.InputTag(srcPixelVertices),
            qualityCuts = hltQualityCuts,
            ApplyDiscriminationByECALIsolation = cms.bool(False),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
            applyOccupancyCut = cms.bool(False),
            applySumPtCut = cms.bool(False),
            applyRelativeSumPtCut = cms.bool(False),
            applyFootprintCorrection = cms.bool(False),
            storeRawOccupancy = cms.bool(False),
            storeRawSumPt = cms.bool(True),
            storeRawPUsumPt = cms.bool(False),
            storeRawFootprintCorrection = cms.bool(False),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(False)
        ),
        pftauDiscriminators, pftauSequence)

    pftauSequenceName = "HLT%sSequence" % pfTauLabel
    setattr(process, pftauSequenceName, pftauSequence)
    return pftauSequence
