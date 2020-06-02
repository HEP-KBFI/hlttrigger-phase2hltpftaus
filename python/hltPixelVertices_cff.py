import FWCore.ParameterSet.Config as cms

hltPixelTracksTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet( 
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      ptMin = cms.double( 0.9 ), # previous 0.8
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True )
    )
)

pixelTracksHitDoubletsPPV = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32(50000000), # 0 ),
    seedingLayers = cms.InputTag( "pixelTracksSeedLayers" )
)

pixelTracksHitQuadrupletsPPV = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double( 0.0 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCachePreSplitting" ) ## hltSiPixelClustersCache
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "pixelTracksHitDoubletsPPV" ), 
    fitFastCircle = cms.bool( True ),
    CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )#,
)

pixelTracksPPV = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('pixelTrackCleanerBySharedHits'),
    passLabel = cms.string('pixelTracks'),
    Filter = cms.InputTag("pixelTrackFilterByKinematics"),
    Fitter = cms.InputTag("pixelFitterByHelixProjections"),
    SeedingHitSets = cms.InputTag("pixelTracksHitQuadrupletsPPV"),
    mightGet = cms.untracked.vstring("")#'RegionsSeedingHitSets_pixelTracksHitQuadruplets__RECO')
)

process.hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "pixelTracksPPV" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)

process.hltPixelVertexSequence = cms.Sequence(
    process.hltPixelTracksTrackingRegions
  + process.pixelTracksHitDoubletsPPV
  + pixelTracksHitQuadrupletsPPV
  + pixelTracksPPV
  + hltPixelVertices
)
