############# GT: 140X_dataRun3_HLT_Candidate_2024_06_04_11_54_43
import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.AlpakaCore.ProcessAcceleratorAlpaka import ProcessAcceleratorAlpaka
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA
from HeterogeneousCore.ROCmCore.ProcessAcceleratorROCm import ProcessAcceleratorROCm

process = cms.Process("MUNTUPLES")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2024D/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/380/567/00000/09e1f948-c1d2-4ba9-abf0-3606a5a5b982.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.CSCTimingExtractorBlock = cms.PSet(
    CSCTimingParameters = cms.PSet(
        CSCStripError = cms.double(7.0),
        CSCStripTimeOffset = cms.double(0.0),
        CSCWireError = cms.double(8.6),
        CSCWireTimeOffset = cms.double(0.0),
        PruneCut = cms.double(9.0),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite'
            ),
            RPCLayers = cms.bool(True)
        ),
        UseStripTime = cms.bool(True),
        UseWireTime = cms.bool(True),
        debug = cms.bool(False)
    )
)

process.ChargeSignificanceTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ChargeSignificanceTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0)
)

process.CkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.CompositeTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet()
)

process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.DTTimingExtractorBlock = cms.PSet(
    DTTimingParameters = cms.PSet(
        DTTimeOffset = cms.double(0.0),
        DoWireCorr = cms.bool(True),
        DropTheta = cms.bool(True),
        HitError = cms.double(2.8),
        HitsMin = cms.int32(3),
        PruneCut = cms.double(5.0),
        RequireBothProjections = cms.bool(False),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite'
            ),
            RPCLayers = cms.bool(True)
        ),
        UseSegmentT0 = cms.bool(False),
        debug = cms.bool(False)
    )
)

process.GlobalMuonRefitter = cms.PSet(
    CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
    Chi2CutCSC = cms.double(1.0),
    Chi2CutDT = cms.double(30.0),
    Chi2CutGEM = cms.double(1.0),
    Chi2CutME0 = cms.double(1.0),
    Chi2CutRPC = cms.double(1.0),
    Chi2ProbabilityCut = cms.double(30.0),
    DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
    DYTselector = cms.int32(1),
    DYTthrs = cms.vint32(10, 10),
    DYTthrsParameters = cms.PSet(
        eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
        eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
        eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
        eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
        eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
    ),
    DYTupdator = cms.bool(True),
    DYTuseAPE = cms.bool(False),
    DYTuseThrsParametrization = cms.bool(True),
    DoPredictionsOnly = cms.bool(False),
    Fitter = cms.string('KFFitterForRefitInsideOut'),
    GEMRecHitLabel = cms.InputTag("gemRecHits"),
    HitThreshold = cms.int32(1),
    ME0RecHitLabel = cms.InputTag("me0Segments"),
    MuonHitsOption = cms.int32(1),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    PropDirForCosmics = cms.bool(False),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    PtCut = cms.double(1.0),
    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
    RefitDirection = cms.string('insideOut'),
    RefitFlag = cms.bool(True),
    RefitRPCHits = cms.bool(True),
    SkipStation = cms.int32(-1),
    Smoother = cms.string('KFSmootherForRefitInsideOut'),
    TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
    TrackerSkipSection = cms.int32(-1),
    TrackerSkipSystem = cms.int32(-1)
)

process.GlobalMuonTrackMatcher = cms.PSet(
    GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_1 = cms.double(50.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaDCut_2 = cms.double(10.0),
        DeltaDCut_3 = cms.double(15.0),
        DeltaRCut_1 = cms.double(0.1),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        Eta_threshold = cms.double(1.2),
        LocChi2Cut = cms.double(20.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Pt_threshold1 = cms.double(0.0),
        Pt_threshold2 = cms.double(999999999.0),
        Quality_1 = cms.double(20.0),
        Quality_2 = cms.double(15.0),
        Quality_3 = cms.double(7.0)
    )
)

process.GlobalTrajectoryBuilderCommon = cms.PSet(
    GlbRefitterParameters = cms.PSet(
        CSCRecSegmentLabel = cms.InputTag("cscSegments"),
        Chi2CutCSC = cms.double(150.0),
        Chi2CutDT = cms.double(10.0),
        Chi2CutGEM = cms.double(1.0),
        Chi2CutME0 = cms.double(1.0),
        Chi2CutRPC = cms.double(1.0),
        Chi2ProbabilityCut = cms.double(30.0),
        DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
        DYTselector = cms.int32(1),
        DYTthrs = cms.vint32(20, 30),
        DYTthrsParameters = cms.PSet(
            eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
            eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
            eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
            eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
            eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
        ),
        DYTupdator = cms.bool(False),
        DYTuseAPE = cms.bool(False),
        DYTuseThrsParametrization = cms.bool(True),
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('GlbMuKFFitter'),
        GEMRecHitLabel = cms.InputTag("gemRecHits"),
        HitThreshold = cms.int32(1),
        ME0RecHitLabel = cms.InputTag("me0Segments"),
        MuonHitsOption = cms.int32(1),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        PropDirForCosmics = cms.bool(False),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        PtCut = cms.double(1.0),
        RefitDirection = cms.string('insideOut'),
        RefitFlag = cms.bool(True),
        RefitRPCHits = cms.bool(True),
        SkipStation = cms.int32(-1),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        TrackerSkipSection = cms.int32(-1),
        TrackerSkipSystem = cms.int32(-1)
    ),
    GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_1 = cms.double(50.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaDCut_2 = cms.double(10.0),
        DeltaDCut_3 = cms.double(15.0),
        DeltaRCut_1 = cms.double(0.1),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        Eta_threshold = cms.double(1.2),
        LocChi2Cut = cms.double(20.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Pt_threshold1 = cms.double(0.0),
        Pt_threshold2 = cms.double(999999999.0),
        Quality_1 = cms.double(20.0),
        Quality_2 = cms.double(15.0),
        Quality_3 = cms.double(7.0)
    ),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    MuonTrackingRegionBuilder = cms.PSet(
        DeltaEta = cms.double(0.2),
        DeltaPhi = cms.double(0.2),
        DeltaR = cms.double(0.2),
        DeltaZ = cms.double(15.9),
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        Eta_fixed = cms.bool(False),
        Eta_min = cms.double(0.1),
        MeasurementTrackerName = cms.InputTag(""),
        OnDemand = cms.int32(-1),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        Phi_fixed = cms.bool(False),
        Phi_min = cms.double(0.1),
        Pt_fixed = cms.bool(False),
        Pt_min = cms.double(1.5),
        Rescale_Dz = cms.double(3.0),
        Rescale_eta = cms.double(3.0),
        Rescale_phi = cms.double(3.0),
        UseVertex = cms.bool(False),
        Z_fixed = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        input = cms.InputTag(""),
        maxRegions = cms.int32(1),
        precise = cms.bool(True),
        vertexCollection = cms.InputTag("")
    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    RefitRPCHits = cms.bool(True),
    ScaleTECxFactor = cms.double(-1.0),
    ScaleTECyFactor = cms.double(-1.0),
    TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
    ),
    TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
    TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
)

process.GroupedCkfTrajectoryBuilderP5 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2MeasurementEstimatorForP5'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('ckfBaseTrajectoryFilterP5')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.MIdIsoExtractorPSetBlock = cms.PSet(
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    ecalDepositName = cms.string('ecal'),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    jetDepositName = cms.string('jets'),
    trackDepositName = cms.string('tracker')
)

process.MIsoCaloExtractorByAssociatorHitsBlock = cms.PSet(
    CenterConeOnCalIntersection = cms.bool(False),
    ComponentName = cms.string('CaloExtractorByAssociator'),
    DR_Max = cms.double(0.5),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_H = cms.double(0.1),
    DR_Veto_HO = cms.double(0.1),
    DepositInstanceLabels = cms.vstring(
        'ecal',
        'hcal',
        'ho'
    ),
    DepositLabel = cms.untracked.string('Cal'),
    NoiseTow_EB = cms.double(0.04),
    NoiseTow_EE = cms.double(0.15),
    Noise_EB = cms.double(0.025),
    Noise_EE = cms.double(0.1),
    Noise_HB = cms.double(0.2),
    Noise_HE = cms.double(0.2),
    Noise_HO = cms.double(0.2),
    PrintTimeReport = cms.untracked.bool(False),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    Threshold_E = cms.double(0.025),
    Threshold_H = cms.double(0.1),
    Threshold_HO = cms.double(0.1),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        dRHcal = cms.double(1.0),
        dRHcalPreselection = cms.double(1.0),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(False),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    ),
    UseRecHitsFlag = cms.bool(True)
)

process.MIsoCaloExtractorByAssociatorTowersBlock = cms.PSet(
    CenterConeOnCalIntersection = cms.bool(False),
    ComponentName = cms.string('CaloExtractorByAssociator'),
    DR_Max = cms.double(0.5),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_H = cms.double(0.1),
    DR_Veto_HO = cms.double(0.1),
    DepositInstanceLabels = cms.vstring(
        'ecal',
        'hcal',
        'ho'
    ),
    DepositLabel = cms.untracked.string('Cal'),
    NoiseTow_EB = cms.double(0.04),
    NoiseTow_EE = cms.double(0.15),
    Noise_EB = cms.double(0.025),
    Noise_EE = cms.double(0.1),
    Noise_HB = cms.double(0.2),
    Noise_HE = cms.double(0.2),
    Noise_HO = cms.double(0.2),
    PrintTimeReport = cms.untracked.bool(False),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    Threshold_E = cms.double(0.2),
    Threshold_H = cms.double(0.5),
    Threshold_HO = cms.double(0.5),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        dRHcal = cms.double(1.0),
        dRHcalPreselection = cms.double(1.0),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(True),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    ),
    UseRecHitsFlag = cms.bool(False)
)

process.MIsoCaloExtractorEcalBlock = cms.PSet(
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    ComponentName = cms.string('CaloExtractor'),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_H = cms.double(0.1),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    Threshold_E = cms.double(0.2),
    Threshold_H = cms.double(0.5),
    Vertex_Constraint_XY = cms.bool(False),
    Vertex_Constraint_Z = cms.bool(False),
    Weight_E = cms.double(1.0),
    Weight_H = cms.double(0.0)
)

process.MIsoCaloExtractorHLTBlock = cms.PSet(
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    ComponentName = cms.string('CaloExtractor'),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_H = cms.double(0.1),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    Threshold_E = cms.double(0.2),
    Threshold_H = cms.double(0.5),
    Vertex_Constraint_XY = cms.bool(False),
    Vertex_Constraint_Z = cms.bool(False),
    Weight_E = cms.double(1.5),
    Weight_H = cms.double(1.0)
)

process.MIsoCaloExtractorHcalBlock = cms.PSet(
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    ComponentName = cms.string('CaloExtractor'),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_H = cms.double(0.1),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    Threshold_E = cms.double(0.2),
    Threshold_H = cms.double(0.5),
    Vertex_Constraint_XY = cms.bool(False),
    Vertex_Constraint_Z = cms.bool(False),
    Weight_E = cms.double(0.0),
    Weight_H = cms.double(1.0)
)

process.MIsoDepositGlobalIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('TrackCollection'),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('track'),
    inputMuonCollection = cms.InputTag("globalMuons")
)

process.MIsoDepositGlobalMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('TrackCollection'),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('track'),
    inputMuonCollection = cms.InputTag("globalMuons")
)

process.MIsoDepositParamGlobalIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('track'),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
)

process.MIsoDepositParamGlobalMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('track'),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
)

process.MIsoDepositParamGlobalViewIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('bestTrkSta'),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
)

process.MIsoDepositParamGlobalViewMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('bestTrkSta'),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
)

process.MIsoDepositViewIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('bestTrkSta'),
    inputMuonCollection = cms.InputTag("muons1stStep")
)

process.MIsoDepositViewMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    InputType = cms.string('MuonCollection'),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('bestTrkSta'),
    inputMuonCollection = cms.InputTag("muons1stStep")
)

process.MIsoJetExtractorBlock = cms.PSet(
    ComponentName = cms.string('JetExtractor'),
    DR_Max = cms.double(1.0),
    DR_Veto = cms.double(0.1),
    ExcludeMuonVeto = cms.bool(True),
    JetCollectionLabel = cms.InputTag("ak4CaloJets"),
    PrintTimeReport = cms.untracked.bool(False),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    Threshold = cms.double(5.0),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(0.5),
        dREcalPreselection = cms.double(0.5),
        dRHcal = cms.double(0.5),
        dRHcalPreselection = cms.double(0.5),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(True),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    )
)

process.MIsoTrackAssociatorDefault = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        dRHcal = cms.double(1.0),
        dRHcalPreselection = cms.double(1.0),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(True),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    )
)

process.MIsoTrackAssociatorHits = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        dRHcal = cms.double(1.0),
        dRHcalPreselection = cms.double(1.0),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(False),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    )
)

process.MIsoTrackAssociatorJets = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(0.5),
        dREcalPreselection = cms.double(0.5),
        dRHcal = cms.double(0.5),
        dRHcalPreselection = cms.double(0.5),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(True),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    )
)

process.MIsoTrackAssociatorTowers = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        dRHcal = cms.double(1.0),
        dRHcalPreselection = cms.double(1.0),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(False),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(True),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(False),
        usePreshower = cms.bool(False)
    )
)

process.MIsoTrackExtractorBlock = cms.PSet(
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    BeamlineOption = cms.string('BeamSpotFromEvent'),
    Chi2Ndof_Max = cms.double(1e+64),
    Chi2Prob_Min = cms.double(-1.0),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(0.5),
    DR_Veto = cms.double(0.01),
    DepositLabel = cms.untracked.string(''),
    Diff_r = cms.double(0.1),
    Diff_z = cms.double(0.2),
    NHits_Min = cms.uint32(0),
    Pt_Min = cms.double(-1.0),
    inputTrackCollection = cms.InputTag("generalTracks")
)

process.MIsoTrackExtractorCtfBlock = cms.PSet(
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    BeamlineOption = cms.string('BeamSpotFromEvent'),
    Chi2Ndof_Max = cms.double(1e+64),
    Chi2Prob_Min = cms.double(-1.0),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(0.5),
    DR_Veto = cms.double(0.01),
    DepositLabel = cms.untracked.string(''),
    Diff_r = cms.double(0.1),
    Diff_z = cms.double(0.2),
    NHits_Min = cms.uint32(0),
    Pt_Min = cms.double(-1.0),
    inputTrackCollection = cms.InputTag("generalTracks")
)

process.MIsoTrackExtractorGsBlock = cms.PSet(
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    BeamlineOption = cms.string('BeamSpotFromEvent'),
    Chi2Ndof_Max = cms.double(1e+64),
    Chi2Prob_Min = cms.double(-1.0),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(0.5),
    DR_Veto = cms.double(0.01),
    DepositLabel = cms.untracked.string(''),
    Diff_r = cms.double(0.1),
    Diff_z = cms.double(0.2),
    NHits_Min = cms.uint32(0),
    Pt_Min = cms.double(-1.0),
    inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks")
)

process.MaxCCCLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxCCCLostHitsTrajectoryFilter'),
    maxCCCLostHits = cms.int32(3),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    )
)

process.MaxConsecLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxConsecLostHitsTrajectoryFilter'),
    maxConsecLostHits = cms.int32(1)
)

process.MaxHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxHitsTrajectoryFilter'),
    maxNumberOfHits = cms.int32(100)
)

process.MaxLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxLostHitsTrajectoryFilter'),
    maxLostHits = cms.int32(2)
)

process.MinHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinHitsTrajectoryFilter'),
    highEtaSwitch = cms.double(5.0),
    minHitsAtHighEta = cms.int32(5),
    minimumNumberOfHits = cms.int32(5)
)

process.MinPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinPtTrajectoryFilter'),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0),
    nSigmaMinPt = cms.double(5.0)
)

process.MuonCaloCompatibilityBlock = cms.PSet(
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    )
)

process.MuonCosmicCompatibilityParameters = cms.PSet(
    CosmicCompFillerParameters = cms.PSet(
        InputCosmicMuonCollection = cms.InputTag("muonsFromCosmics1Leg"),
        InputMuonCollections = cms.VInputTag(cms.InputTag("globalMuons"), cms.InputTag("muons1stStep")),
        InputTrackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks")),
        InputVertexCollection = cms.InputTag("offlinePrimaryVertices"),
        ServiceParameters = cms.PSet(
            CSCLayers = cms.untracked.bool(True),
            GEMLayers = cms.untracked.bool(True),
            ME0Layers = cms.bool(False),
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'SteppingHelixPropagatorAlong',
                'SteppingHelixPropagatorOpposite',
                'SteppingHelixPropagatorL2Any',
                'SteppingHelixPropagatorL2Along',
                'SteppingHelixPropagatorL2Opposite',
                'SteppingHelixPropagatorAnyNoError',
                'SteppingHelixPropagatorAlongNoError',
                'SteppingHelixPropagatorOppositeNoError',
                'SteppingHelixPropagatorL2AnyNoError',
                'SteppingHelixPropagatorL2AlongNoError',
                'SteppingHelixPropagatorL2OppositeNoError',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite',
                'SmartPropagator',
                'SmartPropagatorOpposite',
                'SmartPropagatorAnyOpposite',
                'SmartPropagatorAny',
                'SmartPropagatorRK',
                'SmartPropagatorAnyRK',
                'StraightLinePropagator'
            ),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        angleCut = cms.double(0.1),
        corrTimeNeg = cms.double(-10),
        corrTimePos = cms.double(5),
        deltaPt = cms.double(0.1),
        hIpTrdxy = cms.double(0.02),
        hIpTrvProb = cms.double(0.5),
        ipCut = cms.double(0.02),
        largedxy = cms.double(2.0),
        largedxyMult = cms.double(3.0),
        maxdxyLoose = cms.double(0.01),
        maxdxyLooseMult = cms.double(0.01),
        maxdxyTight = cms.double(1.0),
        maxdxyTightMult = cms.double(1.0),
        maxdzLoose = cms.double(0.1),
        maxdzLooseMult = cms.double(0.1),
        maxdzTight = cms.double(10.0),
        maxdzTightMult = cms.double(10.0),
        maxvertRho = cms.double(5),
        maxvertZ = cms.double(20),
        minvProb = cms.double(0.001),
        nChamberMatches = cms.int32(1),
        nTrackThreshold = cms.int32(3),
        offTimeNegLoose = cms.double(-15.0),
        offTimeNegLooseMult = cms.double(-15.0),
        offTimeNegTight = cms.double(-20.0),
        offTimeNegTightMult = cms.double(-20.0),
        offTimePosLoose = cms.double(15.0),
        offTimePosLooseMult = cms.double(15.0),
        offTimePosTight = cms.double(25.0),
        offTimePosTightMult = cms.double(25.0),
        segmentComp = cms.double(0.4),
        sharedFrac = cms.double(0.75),
        sharedHits = cms.int32(5)
    )
)

process.MuonSegmentMatcher = cms.PSet(
    MatchParameters = cms.PSet(
        CSCsegments = cms.InputTag("cscSegments"),
        DTradius = cms.double(0.01),
        DTsegments = cms.InputTag("dt4DSegments"),
        RPChits = cms.InputTag("rpcRecHits"),
        TightMatchCSC = cms.bool(True),
        TightMatchDT = cms.bool(False)
    )
)

process.MuonServiceProxy = cms.PSet(
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    )
)

process.MuonShowerDigiFillerBlock = cms.PSet(
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    )
)

process.MuonShowerParameters = cms.PSet(
    MuonShowerInformationFillerParameters = cms.PSet(
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        CSCSegmentLabel = cms.InputTag("cscSegments"),
        DT4DRecSegmentLabel = cms.InputTag("dt4DSegments"),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        ServiceParameters = cms.PSet(
            CSCLayers = cms.untracked.bool(True),
            GEMLayers = cms.untracked.bool(True),
            ME0Layers = cms.bool(False),
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'SteppingHelixPropagatorAlong',
                'SteppingHelixPropagatorOpposite',
                'SteppingHelixPropagatorL2Any',
                'SteppingHelixPropagatorL2Along',
                'SteppingHelixPropagatorL2Opposite',
                'SteppingHelixPropagatorAnyNoError',
                'SteppingHelixPropagatorAlongNoError',
                'SteppingHelixPropagatorOppositeNoError',
                'SteppingHelixPropagatorL2AnyNoError',
                'SteppingHelixPropagatorL2AlongNoError',
                'SteppingHelixPropagatorL2OppositeNoError',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite',
                'SmartPropagator',
                'SmartPropagatorOpposite',
                'SmartPropagatorAnyOpposite',
                'SmartPropagatorAny',
                'SmartPropagatorRK',
                'SmartPropagatorAnyRK',
                'StraightLinePropagator'
            ),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        TrackerRecHitBuilder = cms.string('WithTrackAngle')
    )
)

process.MuonTrackLoaderForCosmic = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        AllowNoVertex = cms.untracked.bool(True),
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny')
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)

process.MuonTrackLoaderForGLB = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)

process.MuonTrackLoaderForL2 = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("hltOfflineBeamSpot")
    )
)

process.MuonTrackLoaderForL3 = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(True),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('KFSmootherForMuonTrackLoaderL3'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOfflineBeamSpot")
    )
)

process.MuonTrackLoaderForSTA = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)

process.MuonTrackingRegionCommon = cms.PSet(
    MuonTrackingRegionBuilder = cms.PSet(
        DeltaEta = cms.double(0.2),
        DeltaPhi = cms.double(0.2),
        DeltaR = cms.double(0.2),
        DeltaZ = cms.double(15.9),
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        Eta_fixed = cms.bool(False),
        Eta_min = cms.double(0.1),
        MeasurementTrackerName = cms.InputTag(""),
        OnDemand = cms.int32(-1),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        Phi_fixed = cms.bool(False),
        Phi_min = cms.double(0.1),
        Pt_fixed = cms.bool(False),
        Pt_min = cms.double(1.5),
        Rescale_Dz = cms.double(3.0),
        Rescale_eta = cms.double(3.0),
        Rescale_phi = cms.double(3.0),
        UseVertex = cms.bool(False),
        Z_fixed = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        input = cms.InputTag(""),
        maxRegions = cms.int32(1),
        precise = cms.bool(True),
        vertexCollection = cms.InputTag("")
    )
)

process.MuonUpdatorAtVertex = cms.PSet(
    MuonUpdatorAtVertexParameters = cms.PSet(
        BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
        MaxChi2 = cms.double(1000000.0),
        Propagator = cms.string('SteppingHelixPropagatorOpposite')
    )
)

process.MuonUpdatorAtVertexAnyDirection = cms.PSet(
    MuonUpdatorAtVertexParameters = cms.PSet(
        BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
        MaxChi2 = cms.double(1000000.0),
        Propagator = cms.string('SteppingHelixPropagatorAny')
    )
)

process.SiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.SiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.SiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.SiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.ThresholdPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ThresholdPtTrajectoryFilter'),
    minHitsThresholdPt = cms.int32(3),
    nSigmaThresholdPt = cms.double(5.0),
    thresholdPt = cms.double(10.0)
)

process.TimingFillerBlock = cms.PSet(
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    )
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(True),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(False),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    )
)

process.TrackAssociatorParameters = cms.PSet(
    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
    GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
    HORecHitCollectionLabel = cms.InputTag("horeco"),
    ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
    ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
    RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
    accountForTrajectoryChangeCalo = cms.bool(False),
    dREcal = cms.double(9999.0),
    dREcalPreselection = cms.double(0.05),
    dRHcal = cms.double(9999.0),
    dRHcalPreselection = cms.double(0.2),
    dRMuon = cms.double(9999.0),
    dRMuonPreselection = cms.double(0.2),
    muonMaxDistanceSigmaX = cms.double(0.0),
    muonMaxDistanceSigmaY = cms.double(0.0),
    muonMaxDistanceX = cms.double(5.0),
    muonMaxDistanceY = cms.double(5.0),
    preselectMuonTracks = cms.bool(False),
    propagateAllDirections = cms.bool(True),
    trajectoryUncertaintyTolerance = cms.double(-1.0),
    truthMatch = cms.bool(False),
    useCalo = cms.bool(False),
    useEcal = cms.bool(True),
    useGEM = cms.bool(False),
    useHO = cms.bool(True),
    useHcal = cms.bool(True),
    useME0 = cms.bool(False),
    useMuon = cms.bool(True),
    usePreshower = cms.bool(False)
)

process.TrackerKinkFinderParametersBlock = cms.PSet(
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    )
)

process.ckfBaseTrajectoryFilterP5 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(4),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.dphiScale = cms.PSet(
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.muonSeededTrajectoryBuilderForOutInDisplaced = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('muonSeededMeasurementEstimatorForOutInDisplaced'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForOutInDisplaced')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForOutInDisplaced')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.muonSeededTrajectoryFilterForOutInDisplaced = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.ptSeedParameterization = cms.PSet(
    CSC_01 = cms.vdouble(
        0.155906, -0.000406, 0.0, 0.194022, -0.010181,
        0.0
    ),
    CSC_02 = cms.vdouble(
        0.600235, -0.205683, 0.001113, 0.655625, -0.682129,
        0.253916
    ),
    CSC_03 = cms.vdouble(
        0.498992, -0.086235, -0.025772, 2.761006, -2.667607,
        0.72802
    ),
    CSC_12 = cms.vdouble(
        -0.363549, 0.569552, -0.173186, 7.777069, -10.203618,
        3.478874
    ),
    CSC_13 = cms.vdouble(
        1.22495, -1.792358, 0.711378, 5.271848, -6.280625,
        2.0142
    ),
    CSC_14 = cms.vdouble(
        0.952517, -0.532733, 0.084601, 1.615881, -1.630744,
        0.514139
    ),
    CSC_23 = cms.vdouble(
        -0.095236, 0.122061, -0.029852, -11.396689, 15.933598,
        -4.267065
    ),
    CSC_24 = cms.vdouble(
        -0.049769, 0.063087, -0.011029, -13.765978, 16.296143,
        -4.241835
    ),
    CSC_34 = cms.vdouble(
        0.144321, -0.142283, 0.035636, 190.260708, -180.888643,
        43.430395
    ),
    DT_12 = cms.vdouble(
        0.176182, 0.058535, -0.090549, 0.202363, -0.203126,
        0.222219
    ),
    DT_13 = cms.vdouble(
        0.298842, 0.076531, -0.14293, 0.219923, -0.145026,
        0.155638
    ),
    DT_14 = cms.vdouble(
        0.388423, 0.068698, -0.145925, 0.159515, 0.124299,
        -0.133269
    ),
    DT_23 = cms.vdouble(
        0.120647, 0.034743, -0.070855, 0.302427, -0.21417,
        0.261012
    ),
    DT_24 = cms.vdouble(
        0.189527, 0.037328, -0.088523, 0.251936, 0.032411,
        0.010984
    ),
    DT_34 = cms.vdouble(
        0.049146, -0.003494, -0.010099, 0.672095, 0.36459,
        -0.304346
    ),
    OL_1213 = cms.vdouble(
        0.960544, -0.75644, 0.0, 0.1636, 0.114178,
        0.0
    ),
    OL_1222 = cms.vdouble(
        0.215915, 0.002556, 0.0, 0.313596, -0.021465,
        0.0
    ),
    OL_1232 = cms.vdouble(
        0.162626, 0.000843, 0.0, 0.396271, 0.002791,
        0.0
    ),
    OL_2213 = cms.vdouble(
        0.563218, -0.493991, 0.0, 0.943776, -0.591751,
        0.0
    ),
    OL_2222 = cms.vdouble(
        0.087587, 0.005729, 0.0, 0.535169, -0.087675,
        0.0
    ),
    SMB_10 = cms.vdouble(
        1.160532, 0.148991, 0.0, 0.182785, -0.093776,
        0.0
    ),
    SMB_11 = cms.vdouble(
        1.289468, -0.139653, 0.0, 0.137191, 0.01217,
        0.0
    ),
    SMB_12 = cms.vdouble(
        1.923091, -0.913204, 0.0, 0.161556, 0.020215,
        0.0
    ),
    SMB_20 = cms.vdouble(
        0.861314, -0.16233, 0.0, 0.248879, -0.113879,
        0.0
    ),
    SMB_21 = cms.vdouble(
        0.918425, -0.141199, 0.0, 0.254515, -0.111848,
        0.0
    ),
    SMB_22 = cms.vdouble(
        1.308565, -0.701634, 0.0, -0.302861, 0.675785,
        0.0
    ),
    SMB_30 = cms.vdouble(
        0.399628, 0.014922, 0.0, 0.665622, 0.358439,
        0.0
    ),
    SMB_31 = cms.vdouble(
        0.398661, -0.024853, 0.0, 0.863324, -0.413048,
        0.0
    ),
    SMB_32 = cms.vdouble(
        0.421649, -0.111654, 0.0, -0.044613, 1.134858,
        0.0
    ),
    SME_11 = cms.vdouble(
        2.39479, -0.888663, 0.0, -4.604546, 3.623464,
        0.0
    ),
    SME_12 = cms.vdouble(
        -0.277294, 0.7616, 0.0, -0.243326, 1.446792,
        0.0
    ),
    SME_13 = cms.vdouble(
        0.398851, 0.028176, 0.0, 0.567015, 2.623232,
        0.0
    ),
    SME_21 = cms.vdouble(
        0.64895, -0.148762, 0.0, -5.07676, 6.284227,
        0.0
    ),
    SME_22 = cms.vdouble(
        -0.624708, 0.641043, 0.0, 32.581295, -19.604264,
        0.0
    ),
    SME_31 = cms.vdouble(
        -0.588188, 0.316961, 0.0, -95.261732, 45.444051,
        0.0
    ),
    SME_32 = cms.vdouble(
        -0.021912, -0.008995, 0.0, -49.779764, 30.780972,
        0.0
    ),
    SME_41 = cms.vdouble(
        -0.187116, 0.076415, 0.0, -58.552583, 27.933864,
        0.0
    ),
    SME_42 = cms.vdouble(
        -0.021912, -0.008995, 0.0, -49.779764, 30.780972,
        0.0
    )
)

process.CosmicMuonSeed = cms.EDProducer("CosmicMuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    ForcePointDown = cms.bool(True),
    MaxCSCChi2 = cms.double(300.0),
    MaxDTChi2 = cms.double(300.0),
    MaxSeeds = cms.int32(1000)
)


process.DuplicateListMerger = cms.EDProducer("DuplicateListMerger",
    candidateComponents = cms.InputTag(""),
    candidateSource = cms.InputTag(""),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag(""),
    mergedSource = cms.InputTag(""),
    mightGet = cms.optional.untracked.vstring,
    originalMVAVals = cms.InputTag(""),
    originalSource = cms.InputTag(""),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)


process.DuplicateTrackMerger = cms.EDProducer("DuplicateTrackMerger",
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('DuplicateTrackMergerChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    mightGet = cms.optional.untracked.vstring,
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag(""),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)


process.MuonSeed = cms.EDProducer("MuonSeedProducer",
    CSCSegmentLabel = cms.InputTag("cscSegments"),
    CSC_01 = cms.vdouble(
        0.166, 0.0, 0.0, 0.031, 0.0,
        0.0
    ),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_02 = cms.vdouble(
        0.612, -0.207, -0.0, 0.067, -0.001,
        0.0
    ),
    CSC_03 = cms.vdouble(
        0.787, -0.338, 0.029, 0.101, -0.008,
        0.0
    ),
    CSC_12 = cms.vdouble(
        -0.161, 0.254, -0.047, 0.042, -0.007,
        0.0
    ),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13 = cms.vdouble(
        0.901, -1.302, 0.533, 0.045, 0.005,
        0.0
    ),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14 = cms.vdouble(
        0.606, -0.181, -0.002, 0.111, -0.003,
        0.0
    ),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23 = cms.vdouble(
        -0.081, 0.113, -0.029, 0.015, 0.008,
        0.0
    ),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24 = cms.vdouble(
        0.004, 0.021, -0.002, 0.053, 0.0,
        0.0
    ),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34 = cms.vdouble(
        0.062, -0.067, 0.019, 0.021, 0.003,
        0.0
    ),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DTSegmentLabel = cms.InputTag("dt4DSegments"),
    DT_12 = cms.vdouble(
        0.183, 0.054, -0.087, 0.028, 0.002,
        0.0
    ),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13 = cms.vdouble(
        0.315, 0.068, -0.127, 0.051, -0.002,
        0.0
    ),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14 = cms.vdouble(
        0.359, 0.052, -0.107, 0.072, -0.004,
        0.0
    ),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23 = cms.vdouble(
        0.13, 0.023, -0.057, 0.028, 0.004,
        0.0
    ),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24 = cms.vdouble(
        0.176, 0.014, -0.051, 0.051, 0.003,
        0.0
    ),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(
        0.044, 0.004, -0.013, 0.029, 0.003,
        0.0
    ),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    DebugMuonSeed = cms.bool(False),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    OL_1213 = cms.vdouble(
        0.96, -0.737, 0.0, 0.052, 0.0,
        0.0
    ),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222 = cms.vdouble(
        0.848, -0.591, 0.0, 0.062, 0.0,
        0.0
    ),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232 = cms.vdouble(
        0.184, 0.0, 0.0, 0.066, 0.0,
        0.0
    ),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213 = cms.vdouble(
        0.117, 0.0, 0.0, 0.044, 0.0,
        0.0
    ),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222 = cms.vdouble(
        0.107, 0.0, 0.0, 0.04, 0.0,
        0.0
    ),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10 = cms.vdouble(
        1.387, -0.038, 0.0, 0.19, 0.0,
        0.0
    ),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11 = cms.vdouble(
        1.247, 0.72, -0.802, 0.229, -0.075,
        0.0
    ),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12 = cms.vdouble(
        2.128, -0.956, 0.0, 0.199, 0.0,
        0.0
    ),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20 = cms.vdouble(
        1.011, -0.052, 0.0, 0.188, 0.0,
        0.0
    ),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21 = cms.vdouble(
        1.043, -0.124, 0.0, 0.183, 0.0,
        0.0
    ),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22 = cms.vdouble(
        1.474, -0.758, 0.0, 0.185, 0.0,
        0.0
    ),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30 = cms.vdouble(
        0.505, -0.022, 0.0, 0.215, 0.0,
        0.0
    ),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31 = cms.vdouble(
        0.549, -0.145, 0.0, 0.207, 0.0,
        0.0
    ),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32 = cms.vdouble(
        0.67, -0.327, 0.0, 0.22, 0.0,
        0.0
    ),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11 = cms.vdouble(
        3.295, -1.527, 0.112, 0.378, 0.02,
        0.0
    ),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12 = cms.vdouble(
        0.102, 0.599, 0.0, 0.38, 0.0,
        0.0
    ),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13 = cms.vdouble(
        -1.286, 1.711, 0.0, 0.356, 0.0,
        0.0
    ),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21 = cms.vdouble(
        -0.529, 1.194, -0.358, 0.472, 0.086,
        0.0
    ),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22 = cms.vdouble(
        -1.207, 1.491, -0.251, 0.189, 0.243,
        0.0
    ),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SME_31 = cms.vdouble(
        -1.594, 1.482, -0.317, 0.487, 0.097,
        0.0
    ),
    SME_32 = cms.vdouble(
        -0.901, 1.333, -0.47, 0.41, 0.073,
        0.0
    ),
    SME_41 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    SME_42 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    SeedPtSystematics = cms.double(0.1),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    defaultSeedPt = cms.double(25.0),
    maxDeltaEtaCSC = cms.double(0.2),
    maxDeltaEtaDT = cms.double(0.3),
    maxDeltaEtaOverlap = cms.double(0.08),
    maxDeltaPhiCSC = cms.double(0.5),
    maxDeltaPhiDT = cms.double(0.3),
    maxDeltaPhiOverlap = cms.double(0.25),
    maxEtaResolutionCSC = cms.double(0.06),
    maxEtaResolutionDT = cms.double(0.02),
    maxPhiResolutionCSC = cms.double(0.03),
    maxPhiResolutionDT = cms.double(0.03),
    maximumSeedPt = cms.double(3000.0),
    minCSCHitsPerSegment = cms.int32(4),
    minDTHitsPerSegment = cms.int32(2),
    minimumSeedPt = cms.double(5.0)
)


process.SETMuonSeed = cms.EDProducer("SETMuonSeedProducer",
    SETTrajBuilderParameters = cms.PSet(
        Apply_prePruning = cms.bool(True),
        CSC_01 = cms.vdouble(
            0.155906, -0.000406, 0.0, 0.194022, -0.010181,
            0.0
        ),
        CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
        CSC_02 = cms.vdouble(
            0.600235, -0.205683, 0.001113, 0.655625, -0.682129,
            0.253916
        ),
        CSC_03 = cms.vdouble(
            0.498992, -0.086235, -0.025772, 2.761006, -2.667607,
            0.72802
        ),
        CSC_12 = cms.vdouble(
            -0.363549, 0.569552, -0.173186, 7.777069, -10.203618,
            3.478874
        ),
        CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
        CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
        CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
        CSC_13 = cms.vdouble(
            1.22495, -1.792358, 0.711378, 5.271848, -6.280625,
            2.0142
        ),
        CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
        CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
        CSC_14 = cms.vdouble(
            0.952517, -0.532733, 0.084601, 1.615881, -1.630744,
            0.514139
        ),
        CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
        CSC_23 = cms.vdouble(
            -0.095236, 0.122061, -0.029852, -11.396689, 15.933598,
            -4.267065
        ),
        CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
        CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
        CSC_24 = cms.vdouble(
            -0.049769, 0.063087, -0.011029, -13.765978, 16.296143,
            -4.241835
        ),
        CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
        CSC_34 = cms.vdouble(
            0.144321, -0.142283, 0.035636, 190.260708, -180.888643,
            43.430395
        ),
        CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
        DT_12 = cms.vdouble(
            0.176182, 0.058535, -0.090549, 0.202363, -0.203126,
            0.222219
        ),
        DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
        DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
        DT_13 = cms.vdouble(
            0.298842, 0.076531, -0.14293, 0.219923, -0.145026,
            0.155638
        ),
        DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
        DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
        DT_14 = cms.vdouble(
            0.388423, 0.068698, -0.145925, 0.159515, 0.124299,
            -0.133269
        ),
        DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
        DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
        DT_23 = cms.vdouble(
            0.120647, 0.034743, -0.070855, 0.302427, -0.21417,
            0.261012
        ),
        DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
        DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
        DT_24 = cms.vdouble(
            0.189527, 0.037328, -0.088523, 0.251936, 0.032411,
            0.010984
        ),
        DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
        DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
        DT_34 = cms.vdouble(
            0.049146, -0.003494, -0.010099, 0.672095, 0.36459,
            -0.304346
        ),
        DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
        DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            MinLocalSegmentAngle = cms.double(0.09),
            OutsideChamberErrorScale = cms.double(1.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            maxActiveChambers = cms.int32(100)
        ),
        OL_1213 = cms.vdouble(
            0.960544, -0.75644, 0.0, 0.1636, 0.114178,
            0.0
        ),
        OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
        OL_1222 = cms.vdouble(
            0.215915, 0.002556, 0.0, 0.313596, -0.021465,
            0.0
        ),
        OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
        OL_1232 = cms.vdouble(
            0.162626, 0.000843, 0.0, 0.396271, 0.002791,
            0.0
        ),
        OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
        OL_2213 = cms.vdouble(
            0.563218, -0.493991, 0.0, 0.943776, -0.591751,
            0.0
        ),
        OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
        OL_2222 = cms.vdouble(
            0.087587, 0.005729, 0.0, 0.535169, -0.087675,
            0.0
        ),
        OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
        SMB_10 = cms.vdouble(
            1.160532, 0.148991, 0.0, 0.182785, -0.093776,
            0.0
        ),
        SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
        SMB_11 = cms.vdouble(
            1.289468, -0.139653, 0.0, 0.137191, 0.01217,
            0.0
        ),
        SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
        SMB_12 = cms.vdouble(
            1.923091, -0.913204, 0.0, 0.161556, 0.020215,
            0.0
        ),
        SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
        SMB_20 = cms.vdouble(
            0.861314, -0.16233, 0.0, 0.248879, -0.113879,
            0.0
        ),
        SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
        SMB_21 = cms.vdouble(
            0.918425, -0.141199, 0.0, 0.254515, -0.111848,
            0.0
        ),
        SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
        SMB_22 = cms.vdouble(
            1.308565, -0.701634, 0.0, -0.302861, 0.675785,
            0.0
        ),
        SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
        SMB_30 = cms.vdouble(
            0.399628, 0.014922, 0.0, 0.665622, 0.358439,
            0.0
        ),
        SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
        SMB_31 = cms.vdouble(
            0.398661, -0.024853, 0.0, 0.863324, -0.413048,
            0.0
        ),
        SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
        SMB_32 = cms.vdouble(
            0.421649, -0.111654, 0.0, -0.044613, 1.134858,
            0.0
        ),
        SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
        SME_11 = cms.vdouble(
            2.39479, -0.888663, 0.0, -4.604546, 3.623464,
            0.0
        ),
        SME_11_0_scale = cms.vdouble(1.325085, 0.0),
        SME_12 = cms.vdouble(
            -0.277294, 0.7616, 0.0, -0.243326, 1.446792,
            0.0
        ),
        SME_12_0_scale = cms.vdouble(2.279181, 0.0),
        SME_13 = cms.vdouble(
            0.398851, 0.028176, 0.0, 0.567015, 2.623232,
            0.0
        ),
        SME_13_0_scale = cms.vdouble(0.104905, 0.0),
        SME_21 = cms.vdouble(
            0.64895, -0.148762, 0.0, -5.07676, 6.284227,
            0.0
        ),
        SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
        SME_22 = cms.vdouble(
            -0.624708, 0.641043, 0.0, 32.581295, -19.604264,
            0.0
        ),
        SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
        SME_31 = cms.vdouble(
            -0.588188, 0.316961, 0.0, -95.261732, 45.444051,
            0.0
        ),
        SME_32 = cms.vdouble(
            -0.021912, -0.008995, 0.0, -49.779764, 30.780972,
            0.0
        ),
        SME_41 = cms.vdouble(
            -0.187116, 0.076415, 0.0, -58.552583, 27.933864,
            0.0
        ),
        SME_42 = cms.vdouble(
            -0.021912, -0.008995, 0.0, -49.779764, 30.780972,
            0.0
        ),
        UseSegmentsInTrajectory = cms.bool(False),
        scaleDT = cms.bool(True)
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot")
)


process.TrackCollectionMerger = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(10),
    inputClassifiers = cms.vstring(),
    lostHitPenalty = cms.double(5),
    mightGet = cms.optional.untracked.vstring,
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag()
)


process.TrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999, 25, 16),
        maxChi2n = cms.vdouble(9999, 1, 0.4),
        maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 3, 3),
        maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        min3DLayers = cms.vint32(1, 2, 3),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 4, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 1)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag(""),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.ancientMuonSeed = cms.EDProducer("MuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    CSC_01 = cms.vdouble(
        0.166, 0.0, 0.0, 0.031, 0.0,
        0.0
    ),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_02 = cms.vdouble(
        0.612, -0.207, -0.0, 0.067, -0.001,
        0.0
    ),
    CSC_03 = cms.vdouble(
        0.787, -0.338, 0.029, 0.101, -0.008,
        0.0
    ),
    CSC_12 = cms.vdouble(
        -0.161, 0.254, -0.047, 0.042, -0.007,
        0.0
    ),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13 = cms.vdouble(
        0.901, -1.302, 0.533, 0.045, 0.005,
        0.0
    ),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14 = cms.vdouble(
        0.606, -0.181, -0.002, 0.111, -0.003,
        0.0
    ),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23 = cms.vdouble(
        -0.081, 0.113, -0.029, 0.015, 0.008,
        0.0
    ),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24 = cms.vdouble(
        0.004, 0.021, -0.002, 0.053, 0.0,
        0.0
    ),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34 = cms.vdouble(
        0.062, -0.067, 0.019, 0.021, 0.003,
        0.0
    ),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
    DT_12 = cms.vdouble(
        0.183, 0.054, -0.087, 0.028, 0.002,
        0.0
    ),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13 = cms.vdouble(
        0.315, 0.068, -0.127, 0.051, -0.002,
        0.0
    ),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14 = cms.vdouble(
        0.359, 0.052, -0.107, 0.072, -0.004,
        0.0
    ),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23 = cms.vdouble(
        0.13, 0.023, -0.057, 0.028, 0.004,
        0.0
    ),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24 = cms.vdouble(
        0.176, 0.014, -0.051, 0.051, 0.003,
        0.0
    ),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(
        0.044, 0.004, -0.013, 0.029, 0.003,
        0.0
    ),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(False),
    EnableME0Measurement = cms.bool(False),
    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
    OL_1213 = cms.vdouble(
        0.96, -0.737, 0.0, 0.052, 0.0,
        0.0
    ),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222 = cms.vdouble(
        0.848, -0.591, 0.0, 0.062, 0.0,
        0.0
    ),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232 = cms.vdouble(
        0.184, 0.0, 0.0, 0.066, 0.0,
        0.0
    ),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213 = cms.vdouble(
        0.117, 0.0, 0.0, 0.044, 0.0,
        0.0
    ),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222 = cms.vdouble(
        0.107, 0.0, 0.0, 0.04, 0.0,
        0.0
    ),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10 = cms.vdouble(
        1.387, -0.038, 0.0, 0.19, 0.0,
        0.0
    ),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11 = cms.vdouble(
        1.247, 0.72, -0.802, 0.229, -0.075,
        0.0
    ),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12 = cms.vdouble(
        2.128, -0.956, 0.0, 0.199, 0.0,
        0.0
    ),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20 = cms.vdouble(
        1.011, -0.052, 0.0, 0.188, 0.0,
        0.0
    ),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21 = cms.vdouble(
        1.043, -0.124, 0.0, 0.183, 0.0,
        0.0
    ),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22 = cms.vdouble(
        1.474, -0.758, 0.0, 0.185, 0.0,
        0.0
    ),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30 = cms.vdouble(
        0.505, -0.022, 0.0, 0.215, 0.0,
        0.0
    ),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31 = cms.vdouble(
        0.549, -0.145, 0.0, 0.207, 0.0,
        0.0
    ),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32 = cms.vdouble(
        0.67, -0.327, 0.0, 0.22, 0.0,
        0.0
    ),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11 = cms.vdouble(
        3.295, -1.527, 0.112, 0.378, 0.02,
        0.0
    ),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12 = cms.vdouble(
        0.102, 0.599, 0.0, 0.38, 0.0,
        0.0
    ),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13 = cms.vdouble(
        -1.286, 1.711, 0.0, 0.356, 0.0,
        0.0
    ),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21 = cms.vdouble(
        -0.529, 1.194, -0.358, 0.472, 0.086,
        0.0
    ),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22 = cms.vdouble(
        -1.207, 1.491, -0.251, 0.189, 0.243,
        0.0
    ),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SME_31 = cms.vdouble(
        -1.594, 1.482, -0.317, 0.487, 0.097,
        0.0
    ),
    SME_32 = cms.vdouble(
        -0.901, 1.333, -0.47, 0.41, 0.073,
        0.0
    ),
    SME_41 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    SME_42 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    crackWindow = cms.double(0.04),
    deltaEtaCrackSearchWindow = cms.double(0.25),
    deltaEtaSearchWindow = cms.double(0.2),
    deltaPhiSearchWindow = cms.double(0.25),
    mightGet = cms.optional.untracked.vstring,
    scaleDT = cms.bool(True)
)


process.bmtfDigis = cms.EDProducer("L1TRawToDigi",
    FWId = cms.uint32(2500002144),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1376, 1377),
    InputLabel = cms.InputTag("rawDataCollector"),
    Setup = cms.string('stage2::BMTFSetup'),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.caloLayer1Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(True),
    FWId = cms.uint32(305419896),
    FedIds = cms.vint32(1354, 1356, 1358),
    InputLabel = cms.InputTag("rawDataCollector"),
    Setup = cms.string('stage2::CaloLayer1Setup'),
    debug = cms.untracked.bool(False)
)


process.caloStage1Digis = cms.EDProducer("L1TRawToDigi",
    FedIds = cms.vint32(1352),
    InputLabel = cms.InputTag("rawDataCollector"),
    Setup = cms.string('stage1::CaloSetup')
)


process.caloStage1FinalDigis = cms.EDProducer("L1TPhysicalEtAdder",
    InputCollection = cms.InputTag("caloStage1Digis"),
    InputHFCountsCollection = cms.InputTag("caloStage1Digis","HFBitCounts"),
    InputHFSumsCollection = cms.InputTag("caloStage1Digis","HFRingSums"),
    InputIsoTauCollection = cms.InputTag("caloStage1Digis","isoTaus"),
    InputPreGtJetCollection = cms.InputTag("caloStage1Digis"),
    InputRlxTauCollection = cms.InputTag("caloStage1Digis","rlxTaus")
)


process.caloStage1LegacyFormatDigis = cms.EDProducer("L1TCaloUpgradeToGCTConverter",
    InputCollection = cms.InputTag("caloStage1Digis"),
    InputHFCountsCollection = cms.InputTag("caloStage1Digis","HFBitCounts"),
    InputHFSumsCollection = cms.InputTag("caloStage1Digis","HFRingSums"),
    InputIsoTauCollection = cms.InputTag("caloStage1Digis","isoTaus"),
    InputRlxTauCollection = cms.InputTag("caloStage1Digis","rlxTaus")
)


process.caloStage2Digis = cms.EDProducer("L1TRawToDigi",
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1360, 1366),
    InputLabel = cms.InputTag("rawDataCollector"),
    MinFeds = cms.uint32(1),
    Setup = cms.string('stage2::CaloSetup'),
    TMTCheck = cms.bool(True)
)


process.castorDigis = cms.EDProducer("CastorRawToDigi",
    CastorCtdc = cms.bool(False),
    CastorFirstFED = cms.int32(690),
    ComplainEmptyData = cms.untracked.bool(False),
    ExceptionEmptyData = cms.untracked.bool(False),
    ExpectedOrbitMessageTime = cms.int32(-1),
    FEDs = cms.untracked.vint32(690, 691, 692, 693, 722),
    FilterDataQuality = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackTTP = cms.bool(True),
    UnpackZDC = cms.bool(True),
    UseNominalOrbitMessageTime = cms.bool(True),
    ZDCFirstFED = cms.int32(693),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    silent = cms.untracked.bool(False)
)


process.ckfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring,
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalMixedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesIterativeDefault = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderIterativeDefault')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring,
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalMixedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesP5 = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring,
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("combinatorialcosmicseedfinderP5"),
    useHitsSplitting = cms.bool(True)
)


process.conversionStepTracks = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("convStepTracks"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(True),
    hasSelector = cms.vint32(1),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("convStepSelector:convStep"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(1)
    )),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.cosmicsVeto = cms.EDProducer("CosmicsMuonIdProducer",
    CosmicCompFillerParameters = cms.PSet(
        InputCosmicMuonCollection = cms.InputTag("muonsFromCosmics1Leg"),
        InputMuonCollections = cms.VInputTag(cms.InputTag("globalMuons"), cms.InputTag("muons1stStep")),
        InputTrackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks")),
        InputVertexCollection = cms.InputTag("offlinePrimaryVertices"),
        ServiceParameters = cms.PSet(
            CSCLayers = cms.untracked.bool(True),
            GEMLayers = cms.untracked.bool(True),
            ME0Layers = cms.bool(False),
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'SteppingHelixPropagatorAlong',
                'SteppingHelixPropagatorOpposite',
                'SteppingHelixPropagatorL2Any',
                'SteppingHelixPropagatorL2Along',
                'SteppingHelixPropagatorL2Opposite',
                'SteppingHelixPropagatorAnyNoError',
                'SteppingHelixPropagatorAlongNoError',
                'SteppingHelixPropagatorOppositeNoError',
                'SteppingHelixPropagatorL2AnyNoError',
                'SteppingHelixPropagatorL2AlongNoError',
                'SteppingHelixPropagatorL2OppositeNoError',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite',
                'SmartPropagator',
                'SmartPropagatorOpposite',
                'SmartPropagatorAnyOpposite',
                'SmartPropagatorAny',
                'SmartPropagatorRK',
                'SmartPropagatorAnyRK',
                'StraightLinePropagator'
            ),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        angleCut = cms.double(0.1),
        corrTimeNeg = cms.double(-10),
        corrTimePos = cms.double(5),
        deltaPt = cms.double(0.1),
        hIpTrdxy = cms.double(0.02),
        hIpTrvProb = cms.double(0.5),
        ipCut = cms.double(0.02),
        largedxy = cms.double(2.0),
        largedxyMult = cms.double(3.0),
        maxdxyLoose = cms.double(0.01),
        maxdxyLooseMult = cms.double(0.01),
        maxdxyTight = cms.double(1.0),
        maxdxyTightMult = cms.double(1.0),
        maxdzLoose = cms.double(0.1),
        maxdzLooseMult = cms.double(0.1),
        maxdzTight = cms.double(10.0),
        maxdzTightMult = cms.double(10.0),
        maxvertRho = cms.double(5),
        maxvertZ = cms.double(20),
        minvProb = cms.double(0.001),
        nChamberMatches = cms.int32(1),
        nTrackThreshold = cms.int32(3),
        offTimeNegLoose = cms.double(-15.0),
        offTimeNegLooseMult = cms.double(-15.0),
        offTimeNegTight = cms.double(-20.0),
        offTimeNegTightMult = cms.double(-20.0),
        offTimePosLoose = cms.double(15.0),
        offTimePosLooseMult = cms.double(15.0),
        offTimePosTight = cms.double(25.0),
        offTimePosTightMult = cms.double(25.0),
        segmentComp = cms.double(0.4),
        sharedFrac = cms.double(0.75),
        sharedHits = cms.int32(5)
    ),
    muonCollection = cms.InputTag("muons1stStep"),
    trackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks"))
)


process.cosmicsVetoSeeds = cms.EDProducer("TrajectorySeedFromMuonProducer",
    muonCollectionTag = cms.InputTag("muons1stStep"),
    skipMatchedMuons = cms.bool(False),
    trackCollectionTag = cms.InputTag("generalTracks")
)


process.cosmicsVetoTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('none'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring,
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("cosmicsVetoSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicsVetoTracks = cms.EDProducer("CosmicTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    chi2n_par = cms.double(10.0),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    max_eta = cms.double(2.0),
    max_z0 = cms.double(300.0),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(0),
    min_nHit = cms.uint32(5),
    min_nPixelHit = cms.uint32(0),
    min_pt = cms.double(1.0),
    qualityBit = cms.string(''),
    src = cms.InputTag("cosmicsVetoTracksRaw")
)


process.cosmicsVetoTracksRaw = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("cosmicsVetoTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.cosmictrackSelector = cms.EDProducer("CosmicTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    chi2n_par = cms.double(10.0),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    max_eta = cms.double(2.0),
    max_z0 = cms.double(300.0),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(0),
    min_nHit = cms.uint32(5),
    min_nPixelHit = cms.uint32(0),
    min_pt = cms.double(1.0),
    qualityBit = cms.string(''),
    src = cms.InputTag("ctfWithMaterialTracksCosmics")
)


process.csctfDigis = cms.EDProducer("CSCTFUnpacker",
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    mappingFile = cms.string(''),
    producer = cms.InputTag("rawDataCollector"),
    slot2sector = cms.vint32(
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0
    ),
    swapME1strips = cms.bool(False)
)


process.ctfWithMaterialTracksCosmics = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesP5"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctppsDiamondRawToDigi = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.bool(False),
        printUnknownFrameSummary = cms.untracked.bool(False),
        testBCMostFrequent = cms.uint32(2),
        testCRC = cms.uint32(0),
        testECMostFrequent = cms.uint32(0),
        testFootprint = cms.uint32(2),
        testID = cms.uint32(2),
        useOlderT2TestFile = cms.bool(False),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(
        verbosity = cms.untracked.uint32(0)
    ),
    fedIds = cms.vuint32(
        579, 581, 582, 583, 588,
        589
    ),
    mightGet = cms.optional.untracked.vstring,
    rawDataTag = cms.InputTag("rawDataCollector"),
    subSystem = cms.string('TimingDiamond')
)


process.ctppsPixelDigis = cms.EDProducer("CTPPSPixelRawToDigi",
    includeErrors = cms.bool(True),
    inputLabel = cms.InputTag("rawDataCollector"),
    isRun3 = cms.bool(True),
    mappingLabel = cms.string('RPix'),
    mightGet = cms.optional.untracked.vstring
)


process.displacedGlobalMuons = cms.EDProducer("GlobalMuonProducer",
    GLBTrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutME0 = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            Chi2ProbabilityCut = cms.double(30.0),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            DYTselector = cms.int32(1),
            DYTthrs = cms.vint32(20, 30),
            DYTthrsParameters = cms.PSet(
                eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
                eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
                eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
                eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
                eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
            ),
            DYTupdator = cms.bool(False),
            DYTuseAPE = cms.bool(False),
            DYTuseThrsParametrization = cms.bool(True),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('GlbMuKFFitter'),
            GEMRecHitLabel = cms.InputTag("gemRecHits"),
            HitThreshold = cms.int32(1),
            ME0RecHitLabel = cms.InputTag("me0Segments"),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            PtCut = cms.double(1.0),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(20.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('SmartPropagatorRK'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.2),
            DeltaPhi = cms.double(0.2),
            DeltaR = cms.double(0.2),
            DeltaZ = cms.double(15.9),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(False),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag(""),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(False),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(False),
            Pt_min = cms.double(1.5),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            input = cms.InputTag(""),
            maxRegions = cms.int32(1),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
    ),
    MuonCollectionLabel = cms.InputTag("displacedStandAloneMuons"),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    ),
    TrackerCollectionLabel = cms.InputTag("displacedTracks"),
    VertexCollectionLabel = cms.InputTag("offlinePrimaryVertices"),
    selectHighPurity = cms.bool(False)
)


process.displacedMuonSeeds = cms.EDProducer("CosmicMuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    ForcePointDown = cms.bool(False),
    MaxCSCChi2 = cms.double(300.0),
    MaxDTChi2 = cms.double(300.0),
    MaxSeeds = cms.int32(1000)
)


process.displacedMuons1stStep = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(True),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.2),
        Diff_z = cms.double(0.5),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(True),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(True),
    fillTrackerKink = cms.bool(True),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("displacedTracks", "displacedGlobalMuons", "displacedStandAloneMuons"),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'links',
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(3.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(2.5),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(0.5),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(True),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(True),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(True)
)


process.displacedStandAloneMuons = cms.EDProducer("StandAloneMuonProducer",
    InputObjects = cms.InputTag("displacedMuonSeeds"),
    MuonTrajectoryBuilder = cms.string('StandAloneMuonTrajectoryBuilder'),
    STATrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            ForceAllIterations = cms.bool(False),
            MaxFractionOfLostHits = cms.double(0.05),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        ),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)


process.displacedTracks = cms.EDProducer("DuplicateListMerger",
    candidateComponents = cms.InputTag("duplicateDisplacedTrackCandidates","candidateMap"),
    candidateSource = cms.InputTag("duplicateDisplacedTrackCandidates","candidates"),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag("duplicateDisplacedTrackClassifier","MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateDisplacedTracks"),
    mightGet = cms.optional.untracked.vstring,
    originalMVAVals = cms.InputTag("preDuplicateMergingDisplacedTracks","MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingDisplacedTracks"),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)


process.dttfDigis = cms.EDProducer("DTTFFEDReader",
    DTTF_FED_Source = cms.InputTag("rawDataCollector"),
    verbose = cms.untracked.bool(False)
)


process.duplicateDisplacedTrackCandidates = cms.EDProducer("DuplicateTrackMerger",
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('duplicateDisplacedTrackCandidatesChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    mightGet = cms.optional.untracked.vstring,
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag("preDuplicateMergingDisplacedTracks"),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)


process.duplicateDisplacedTrackClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 99, 99),
        maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        min3DLayers = cms.vint32(0, 0, 0),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(0, 0, 0),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("mergedDuplicateDisplacedTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.duplicateTrackCandidates = cms.EDProducer("DuplicateTrackMerger",
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('duplicateTrackCandidatesChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    mightGet = cms.optional.untracked.vstring,
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag("preDuplicateMergingGeneralTracks"),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)


process.duplicateTrackClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 99, 99),
        maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        min3DLayers = cms.vint32(0, 0, 0),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(0, 0, 0),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("mergedDuplicateTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.earlyDisplacedMuons = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(True),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(False),
        useGEM = cms.bool(True),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(False),
    fillEnergy = cms.bool(False),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(False),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(True),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("earlyGeneralTracks", "displacedStandAloneMuons:"),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(3.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(3.0),
    minPCaloMuon = cms.double(3.0),
    minPt = cms.double(2.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(True),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(True),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(True)
)


process.ecalDigisCPU = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.ecalDigisGPU = cms.EDProducer("EcalRawToDigiGPU",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648),
    mightGet = cms.optional.untracked.vstring
)


process.ecalDigisPortable = cms.EDProducer("EcalRawToDigiPortable@alpaka",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648),
    mightGet = cms.optional.untracked.vstring
)


process.ecalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    sourceTag = cms.InputTag("rawDataCollector")
)


process.emtfStage2Digis = cms.EDProducer("L1TRawToDigi",
    FWId = cms.uint32(0),
    FedIds = cms.vint32(1384, 1385),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(True),
    Setup = cms.string('stage2::EMTFSetup'),
    debug = cms.untracked.bool(False)
)


process.gctDigis = cms.EDProducer("GctRawToDigi",
    checkHeaders = cms.untracked.bool(False),
    gctFedId = cms.untracked.int32(745),
    hltMode = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring,
    numberOfGctSamplesToUnpack = cms.uint32(1),
    numberOfRctSamplesToUnpack = cms.uint32(1),
    unpackSharedRegions = cms.bool(False),
    unpackerVersion = cms.uint32(0),
    verbose = cms.untracked.bool(False)
)


process.gemRecHits = cms.EDProducer("GEMRecHitProducer",
    applyMasking = cms.bool(False),
    deadFile = cms.optional.FileInPath,
    ge21Off = cms.bool(False),
    gemDigiLabel = cms.InputTag("muonGEMDigis"),
    maskFile = cms.optional.FileInPath,
    mightGet = cms.optional.untracked.vstring,
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)


process.gemRecHitsDef = cms.EDProducer("GEMRecHitProducer",
    applyMasking = cms.bool(False),
    deadFile = cms.optional.FileInPath,
    ge21Off = cms.bool(False),
    gemDigiLabel = cms.InputTag("muonGEMDigis"),
    maskFile = cms.optional.FileInPath,
    mightGet = cms.optional.untracked.vstring,
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)


process.generalTracks = cms.EDProducer("DuplicateListMerger",
    candidateComponents = cms.InputTag("duplicateTrackCandidates","candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates","candidates"),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier","MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"),
    mightGet = cms.optional.untracked.vstring,
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks","MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)


process.glbTrackQual = cms.EDProducer("GlobalTrackQualityProducer",
    BaseLabel = cms.string('GLB'),
    GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_1 = cms.double(50.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaDCut_2 = cms.double(10.0),
        DeltaDCut_3 = cms.double(15.0),
        DeltaRCut_1 = cms.double(0.1),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        Eta_threshold = cms.double(1.2),
        LocChi2Cut = cms.double(20.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Pt_threshold1 = cms.double(0.0),
        Pt_threshold2 = cms.double(999999999.0),
        Quality_1 = cms.double(20.0),
        Quality_2 = cms.double(15.0),
        Quality_3 = cms.double(7.0)
    ),
    InputCollection = cms.InputTag("globalMuons"),
    InputLinksCollection = cms.InputTag("globalMuons"),
    MaxChi2 = cms.double(100000.0),
    RefitterParameters = cms.PSet(
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        Chi2CutCSC = cms.double(1.0),
        Chi2CutDT = cms.double(30.0),
        Chi2CutGEM = cms.double(1.0),
        Chi2CutME0 = cms.double(1.0),
        Chi2CutRPC = cms.double(1.0),
        Chi2ProbabilityCut = cms.double(30.0),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        DYTselector = cms.int32(1),
        DYTthrs = cms.vint32(10, 10),
        DYTthrsParameters = cms.PSet(
            eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
            eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
            eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
            eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
            eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
        ),
        DYTupdator = cms.bool(True),
        DYTuseAPE = cms.bool(False),
        DYTuseThrsParametrization = cms.bool(True),
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        GEMRecHitLabel = cms.InputTag("gemRecHits"),
        HitThreshold = cms.int32(1),
        ME0RecHitLabel = cms.InputTag("me0Segments"),
        MuonHitsOption = cms.int32(1),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        PropDirForCosmics = cms.bool(False),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        PtCut = cms.double(1.0),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        RefitDirection = cms.string('insideOut'),
        RefitFlag = cms.bool(True),
        RefitRPCHits = cms.bool(True),
        SkipStation = cms.int32(-1),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        TrackerSkipSection = cms.int32(-1),
        TrackerSkipSystem = cms.int32(-1)
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    nSigma = cms.double(3.0)
)


process.globalMuons = cms.EDProducer("GlobalMuonProducer",
    GLBTrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutME0 = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            Chi2ProbabilityCut = cms.double(30.0),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            DYTselector = cms.int32(1),
            DYTthrs = cms.vint32(20, 30),
            DYTthrsParameters = cms.PSet(
                eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
                eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
                eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
                eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
                eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
            ),
            DYTupdator = cms.bool(False),
            DYTuseAPE = cms.bool(False),
            DYTuseThrsParametrization = cms.bool(True),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('GlbMuKFFitter'),
            GEMRecHitLabel = cms.InputTag("gemRecHits"),
            HitThreshold = cms.int32(1),
            ME0RecHitLabel = cms.InputTag("me0Segments"),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            PtCut = cms.double(1.0),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(20.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('SmartPropagatorRK'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.2),
            DeltaPhi = cms.double(0.2),
            DeltaR = cms.double(0.2),
            DeltaZ = cms.double(15.9),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(False),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag(""),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(False),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(False),
            Pt_min = cms.double(1.5),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            input = cms.InputTag(""),
            maxRegions = cms.int32(1),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
    ),
    MuonCollectionLabel = cms.InputTag("standAloneMuons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    ),
    TrackerCollectionLabel = cms.InputTag("generalTracks"),
    VertexCollectionLabel = cms.InputTag("offlinePrimaryVertices"),
    selectHighPurity = cms.bool(False)
)


process.globalSETMuons = cms.EDProducer("GlobalMuonProducer",
    GLBTrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutME0 = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            Chi2ProbabilityCut = cms.double(30.0),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            DYTselector = cms.int32(1),
            DYTthrs = cms.vint32(20, 30),
            DYTthrsParameters = cms.PSet(
                eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
                eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
                eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
                eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
                eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
            ),
            DYTupdator = cms.bool(False),
            DYTuseAPE = cms.bool(False),
            DYTuseThrsParametrization = cms.bool(True),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('GlbMuKFFitter'),
            GEMRecHitLabel = cms.InputTag("gemRecHits"),
            HitThreshold = cms.int32(1),
            ME0RecHitLabel = cms.InputTag("me0Segments"),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            PtCut = cms.double(1.0),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(20.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('SmartPropagatorRK'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.2),
            DeltaPhi = cms.double(0.2),
            DeltaR = cms.double(0.2),
            DeltaZ = cms.double(15.9),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(False),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag(""),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(False),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(False),
            Pt_min = cms.double(1.5),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            input = cms.InputTag(""),
            maxRegions = cms.int32(1),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate')
    ),
    MuonCollectionLabel = cms.InputTag("standAloneSETMuons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    ),
    TrackerCollectionLabel = cms.InputTag("generalTracks"),
    VertexCollectionLabel = cms.InputTag("offlinePrimaryVertices"),
    selectHighPurity = cms.bool(False)
)


process.gmtStage2Digis = cms.EDProducer("L1TRawToDigi",
    FedIds = cms.vint32(1402),
    InputLabel = cms.InputTag("rawDataCollector"),
    MinFeds = cms.uint32(1),
    Setup = cms.string('stage2::GMTSetup')
)


process.gtDigis = cms.EDProducer("L1GlobalTriggerRawToDigi",
    ActiveBoardsMask = cms.uint32(65535),
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(-1),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
)


process.gtEvmDigis = cms.EDProducer("L1GlobalTriggerEvmRawToDigi",
    ActiveBoardsMask = cms.uint32(65535),
    BstLengthBytes = cms.int32(-1),
    EvmGtFedId = cms.untracked.int32(812),
    EvmGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(-1)
)


process.gtStage2Digis = cms.EDProducer("L1TRawToDigi",
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MinFeds = cms.uint32(1),
    Setup = cms.string('stage2::GTSetup')
)


process.gtTestcrateStage2Digis = cms.EDProducer("L1TRawToDigi",
    FedIds = cms.vint32(1405),
    InputLabel = cms.InputTag("rawDataCollector"),
    Setup = cms.string('stage2::GTSetup')
)


process.hcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    mightGet = cms.optional.untracked.vstring,
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.hfnoseDigis = cms.EDProducer("HFNoseRawToDigiFake",
    hfnoseDigis = cms.InputTag("simHFNoseUnsuppressedDigis","HFNose"),
    mightGet = cms.optional.untracked.vstring
)


process.hgcalDigis = cms.EDProducer("HGCalRawToDigiFake",
    bhDigis = cms.InputTag("simHGCalUnsuppressedDigis","HEback"),
    eeDigis = cms.InputTag("simHGCalUnsuppressedDigis","EE"),
    fhDigis = cms.InputTag("simHGCalUnsuppressedDigis","HEfront"),
    mightGet = cms.optional.untracked.vstring
)


process.mergedDuplicateDisplacedTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("duplicateDisplacedTrackCandidates","candidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.mergedDuplicateTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("duplicateTrackCandidates","candidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.mergedStandAloneMuonSeeds = cms.EDProducer("MuonSeedMerger",
    SeedCollections = cms.VInputTag(cms.InputTag("ancientMuonSeed"), cms.InputTag("MuonSeed"))
)


process.muIsoDepositCalByAssociatorHits = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.025),
        Threshold_H = cms.double(0.1),
        Threshold_HO = cms.double(0.1),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(False),
            useEcal = cms.bool(True),
            useGEM = cms.bool(False),
            useHO = cms.bool(True),
            useHcal = cms.bool(True),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(True)
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        inputMuonCollection = cms.InputTag("muons1stStep")
    )
)


process.muIsoDepositCalByAssociatorTowers = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(
        'ecal',
        'hcal',
        'ho'
    ),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","ecal"), cms.InputTag("muons1stStep","hcal"), cms.InputTag("muons1stStep","ho"))
)


process.muIsoDepositCalByAssociatorTowersDisplaced = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(
        'ecal',
        'hcal',
        'ho'
    ),
    inputTags = cms.VInputTag(cms.InputTag("displacedMuons1stStep","ecal"), cms.InputTag("displacedMuons1stStep","hcal"), cms.InputTag("displacedMuons1stStep","ho"))
)


process.muIsoDepositJets = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","jets"))
)


process.muIsoDepositJetsDisplaced = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("displacedMuons1stStep","jets"))
)


process.muIsoDepositTk = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","tracker"))
)


process.muIsoDepositTkDisplaced = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("displacedMuons1stStep","tracker"))
)


process.muParamGlobalIsoDepositCalByAssociatorHits = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.025),
        Threshold_H = cms.double(0.1),
        Threshold_HO = cms.double(0.1),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(False),
            useEcal = cms.bool(True),
            useGEM = cms.bool(False),
            useHO = cms.bool(True),
            useHcal = cms.bool(True),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(True)
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositCalByAssociatorTowers = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositCalEcal = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        ComponentName = cms.string('CaloExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Vertex_Constraint_XY = cms.bool(False),
        Vertex_Constraint_Z = cms.bool(False),
        Weight_E = cms.double(1.0),
        Weight_H = cms.double(0.0)
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositCalHcal = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        ComponentName = cms.string('CaloExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Vertex_Constraint_XY = cms.bool(False),
        Vertex_Constraint_Z = cms.bool(False),
        Weight_E = cms.double(0.0),
        Weight_H = cms.double(1.0)
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositCtfTk = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks")
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('bestTrkSta'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositGsTk = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks")
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositJets = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('bestTrkSta'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muParamGlobalIsoDepositTk = cms.EDProducer("MuIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        InputType = cms.string('MuonCollection'),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons")
    )
)


process.muidAllArbitrated = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('AllArbitrated')
)


process.muidGMStaChiCompatibility = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMStaChiCompatibility')
)


process.muidGMTkChiCompatibility = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMTkChiCompatibility')
)


process.muidGMTkKinkTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMTkKinkTight')
)


process.muidGlobalMuonPromptTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GlobalMuonPromptTight')
)


process.muidRPCMuLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('RPCMuLoose')
)


process.muidTM2DCompatibilityLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TM2DCompatibilityLoose')
)


process.muidTM2DCompatibilityTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TM2DCompatibilityTight')
)


process.muidTMLastStationAngLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationAngLoose')
)


process.muidTMLastStationAngTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationAngTight')
)


process.muidTMLastStationLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationLoose')
)


process.muidTMLastStationOptimizedLowPtLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationOptimizedLowPtLoose')
)


process.muidTMLastStationOptimizedLowPtTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationOptimizedLowPtTight')
)


process.muidTMLastStationTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationTight')
)


process.muidTMOneStationAngLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationAngLoose')
)


process.muidTMOneStationAngTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationAngTight')
)


process.muidTMOneStationLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationLoose')
)


process.muidTMOneStationTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationTight')
)


process.muidTrackerMuonArbitrated = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TrackerMuonArbitrated')
)


process.muonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    B904Setup = cms.untracked.bool(False),
    B904dmb = cms.untracked.int32(3),
    B904vmecrate = cms.untracked.int32(1),
    Debug = cms.untracked.bool(False),
    DisableMappingCheck = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    runDQM = cms.untracked.bool(False),
    useCSCShowers = cms.bool(True),
    useGEMs = cms.bool(True),
    useRPCs = cms.bool(False)
)


process.muonDTDigis = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector")
)


process.muonEcalDetIds = cms.EDProducer("InterestingEcalDetIdProducer",
    inputCollection = cms.InputTag("muons1stStep")
)


process.muonGEMDigis = cms.EDProducer("GEMRawToDigiModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    fedIdEnd = cms.uint32(1478),
    fedIdStart = cms.uint32(1467),
    ge21Off = cms.bool(False),
    keepDAQStatus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    readMultiBX = cms.bool(False),
    useDBEMap = cms.bool(True)
)


process.muonRPCDigis = cms.EDProducer("RPCDigiMerger",
    InputLabel = cms.InputTag("rawDataCollector"),
    bxMaxCPPF = cms.int32(2),
    bxMaxOMTF = cms.int32(4),
    bxMaxTwinMux = cms.int32(2),
    bxMinCPPF = cms.int32(-2),
    bxMinOMTF = cms.int32(-3),
    bxMinTwinMux = cms.int32(-2),
    inputTagCPPFDigis = cms.InputTag("rpcCPPFRawToDigi"),
    inputTagOMTFDigis = cms.InputTag("omtfStage2Digis"),
    inputTagSimRPCDigis = cms.InputTag("simMuonRPCDigis"),
    inputTagTwinMuxDigis = cms.InputTag("rpcTwinMuxRawToDigi"),
    mightGet = cms.optional.untracked.vstring
)


process.muonSeededSeedsOutInDisplaced = cms.EDProducer("OutsideInMuonSeeder",
    cut = cms.string('pt > 10 && outerTrack.hitPattern.muonStationsWithValidHits >= 2'),
    debug = cms.untracked.bool(False),
    errorRescaleFactor = cms.double(2.0),
    fromVertex = cms.bool(False),
    hitCollector = cms.string('hitCollectorForOutInMuonSeeds'),
    hitsToTry = cms.int32(3),
    layersToTry = cms.int32(3),
    maxEtaForTOB = cms.double(1.8),
    minEtaForTEC = cms.double(0.7),
    muonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    src = cms.InputTag("earlyDisplacedMuons"),
    trackerPropagator = cms.string('PropagatorWithMaterial')
)


process.muonSeededSeedsOutInDisplacedAsTracks = cms.EDProducer("FakeTrackProducerFromSeed",
    src = cms.InputTag("muonSeededSeedsOutInDisplaced")
)


process.muonSeededTrackCandidatesOutInDisplaced = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryBuilderForOutInDisplaced')
    ),
    TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring,
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("muonSeededSeedsOutInDisplaced"),
    useHitsSplitting = cms.bool(True)
)


process.muonSeededTrackCandidatesOutInDisplacedAsTracks = cms.EDProducer("FakeTrackProducerFromCandidate",
    src = cms.InputTag("muonSeededTrackCandidatesOutInDisplaced")
)


process.muonSeededTracksOutInDisplaced = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('muonSeededStepOutIn'),
    Fitter = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("muonSeededTrackCandidatesOutInDisplaced"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.muonSeededTracksOutInDisplacedClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
            dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
        maxLostLayers = cms.vint32(4, 3, 2),
        maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
        min3DLayers = cms.vint32(1, 2, 2),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 5, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("muonSeededTracksOutInDisplaced"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.muonSelectionTypeValueMapProducer = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('All')
)


process.muonShowerInformation = cms.EDProducer("MuonShowerInformationProducer",
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    ShowerInformationFillerParameters = cms.PSet(
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        CSCSegmentLabel = cms.InputTag("cscSegments"),
        DT4DRecSegmentLabel = cms.InputTag("dt4DSegments"),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        ServiceParameters = cms.PSet(
            CSCLayers = cms.untracked.bool(True),
            GEMLayers = cms.untracked.bool(True),
            ME0Layers = cms.bool(False),
            Propagators = cms.untracked.vstring(
                'SteppingHelixPropagatorAny',
                'SteppingHelixPropagatorAlong',
                'SteppingHelixPropagatorOpposite',
                'SteppingHelixPropagatorL2Any',
                'SteppingHelixPropagatorL2Along',
                'SteppingHelixPropagatorL2Opposite',
                'SteppingHelixPropagatorAnyNoError',
                'SteppingHelixPropagatorAlongNoError',
                'SteppingHelixPropagatorOppositeNoError',
                'SteppingHelixPropagatorL2AnyNoError',
                'SteppingHelixPropagatorL2AlongNoError',
                'SteppingHelixPropagatorL2OppositeNoError',
                'PropagatorWithMaterial',
                'PropagatorWithMaterialOpposite',
                'SmartPropagator',
                'SmartPropagatorOpposite',
                'SmartPropagatorAnyOpposite',
                'SmartPropagatorAny',
                'SmartPropagatorRK',
                'SmartPropagatorAnyRK',
                'StraightLinePropagator'
            ),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        TrackerRecHitBuilder = cms.string('WithTrackAngle')
    ),
    muonCollection = cms.InputTag("muons1stStep"),
    trackCollection = cms.InputTag("generalTracks")
)


process.muons1stStep = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(True),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(True),
    fillGlobalTrackRefits = cms.bool(True),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(True),
    fillTrackerKink = cms.bool(True),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag(
        cms.InputTag("generalTracks"), cms.InputTag("globalMuons"), cms.InputTag("standAloneMuons","UpdatedAtVtx"), cms.InputTag("standAloneMuons"), cms.InputTag("tevMuons","firstHit"),
        cms.InputTag("tevMuons","picky"), cms.InputTag("tevMuons","dyt")
    ),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'links',
        'outer tracks',
        'outer tracks',
        'tev firstHit',
        'tev picky',
        'tev dyt'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(3.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(2.5),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(0.5),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(True),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(True),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(True)
)


process.muonsWithSET = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            preselectMuonTracks = cms.bool(False),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMHitCollectionLabel = cms.InputTag("gemRecHits"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0HitCollectionLabel = cms.InputTag("me0RecHits"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        RPCHitCollectionLabel = cms.InputTag("rpcRecHits"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        preselectMuonTracks = cms.bool(True),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(True),
    fillGlobalTrackRefits = cms.bool(True),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(True),
    fillTrackerKink = cms.bool(True),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("generalTracks", "globalSETMuons", "standAloneSETMuons:UpdatedAtVtx"),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'links',
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(3.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(2.5),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(0.5),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(True),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(True),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(True)
)


process.muontiming = cms.EDProducer("MuonTimingProducer",
    MuonCollection = cms.InputTag("muons"),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    )
)


process.offlineBeamSpot = cms.EDProducer("BeamSpotProducer")


process.offlineBeamSpotDevice = cms.EDProducer("BeamSpotDeviceProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("offlineBeamSpot")
)


process.offlineBeamSpotToCUDA = cms.EDProducer("BeamSpotToCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("offlineBeamSpot")
)


process.omtfStage2Digis = cms.EDProducer("OmtfUnpacker",
    inputLabel = cms.InputTag("rawDataCollector"),
    skipRpc = cms.bool(False)
)


process.onlineMetaDataDigis = cms.EDProducer("OnlineMetaDataRawToDigi",
    mightGet = cms.optional.untracked.vstring,
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.onlineMetaDataRawToDigi = cms.EDProducer("OnlineMetaDataRawToDigi",
    mightGet = cms.optional.untracked.vstring,
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.preDuplicateMergingDisplacedTracks = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(100.0),
    inputClassifiers = cms.vstring(
        'muonSeededTracksInOutClassifier',
        'muonSeededTracksOutInDisplacedClassifier'
    ),
    lostHitPenalty = cms.double(1.0),
    mightGet = cms.optional.untracked.vstring,
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag("muonSeededTracksInOut", "muonSeededTracksOutInDisplaced")
)


process.refittedStandAloneMuons = cms.EDProducer("StandAloneMuonProducer",
    InputObjects = cms.InputTag("ancientMuonSeed"),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    STATrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(True),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            ForceAllIterations = cms.bool(False),
            MaxFractionOfLostHits = cms.double(0.05),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        ),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)


process.rpcCPPFRawToDigi = cms.EDProducer("RPCAMCRawToDigi",
    RPCAMCUnpacker = cms.string('RPCCPPFUnpacker'),
    RPCAMCUnpackerSettings = cms.PSet(
        bxMax = cms.int32(2),
        bxMin = cms.int32(-2),
        cppfDaqDelay = cms.int32(2),
        fillAMCCounters = cms.bool(True)
    ),
    calculateCRC = cms.bool(True),
    fillCounters = cms.bool(True),
    inputTag = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring
)


process.rpcTwinMuxRawToDigi = cms.EDProducer("RPCTwinMuxRawToDigi",
    bxMax = cms.int32(2),
    bxMin = cms.int32(-2),
    calculateCRC = cms.bool(True),
    fillCounters = cms.bool(True),
    inputTag = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring
)


process.rpcunpacker = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
)


process.scalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    mightGet = cms.optional.untracked.vstring,
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.siPixelDigiErrors = cms.EDProducer("SiPixelDigiErrorsFromSoA",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    UsePhase1 = cms.bool(True),
    UserErrorList = cms.vint32(40),
    digiErrorSoASrc = cms.InputTag("siPixelDigiErrorsSoA"),
    mightGet = cms.optional.untracked.vstring
)


process.siPixelDigiErrorsSoA = cms.EDProducer("SiPixelDigiErrorsSoAFromCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplittingCUDA")
)


process.siPixelDigisSoA = cms.EDProducer("SiPixelDigisSoAFromCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplittingCUDA")
)


process.siStripDigis = cms.EDProducer("SiStripRawToDigiModule",
    AppendedBytes = cms.int32(0),
    DoAPVEmulatorCheck = cms.bool(False),
    DoAllCorruptBufferChecks = cms.bool(False),
    ErrorThreshold = cms.uint32(7174),
    LegacyUnpacker = cms.bool(False),
    MarkModulesOnMissingFeds = cms.bool(True),
    ProductLabel = cms.InputTag("rawDataCollector"),
    TriggerFedId = cms.int32(0),
    UnpackBadChannels = cms.bool(False),
    UnpackCommonModeValues = cms.bool(False),
    UseDaqRegister = cms.bool(False),
    UseFedKey = cms.bool(False)
)


process.simEcalTriggerPrimitiveDigis = cms.EDProducer("EcalTrigPrimProducer",
    BarrelOnly = cms.bool(False),
    Debug = cms.bool(False),
    Famos = cms.bool(False),
    InstanceEB = cms.string(''),
    InstanceEE = cms.string(''),
    Label = cms.string('simEcalUnsuppressedDigis'),
    TcpOutput = cms.bool(False),
    binOfMaximum = cms.int32(6)
)


process.standAloneMuons = cms.EDProducer("StandAloneMuonProducer",
    InputObjects = cms.InputTag("ancientMuonSeed"),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    STATrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(False),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(False),
            EnableME0Measurement = cms.bool(False),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            ForceAllIterations = cms.bool(False),
            MaxFractionOfLostHits = cms.double(0.05),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        ),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)


process.standAloneSETMuons = cms.EDProducer("StandAloneMuonProducer",
    InputObjects = cms.InputTag("SETMuonSeed"),
    MuonTrajectoryBuilder = cms.string('DirectMuonTrajectoryBuilder'),
    STATrajBuilderParameters = cms.PSet(
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            RescaleError = cms.double(1.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)


process.tcdsDigis = cms.EDProducer("TcdsRawToDigi",
    InputLabel = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring
)


process.tcdsRawToDigi = cms.EDProducer("TcdsRawToDigi",
    InputLabel = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring
)


process.tevMuons = cms.EDProducer("TevMuonProducer",
    MuonCollectionLabel = cms.InputTag("globalMuons"),
    RefitIndex = cms.vint32(1, 2, 3, 4),
    Refits = cms.vstring(
        'default',
        'firstHit',
        'picky',
        'dyt'
    ),
    RefitterParameters = cms.PSet(
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        Chi2CutCSC = cms.double(1.0),
        Chi2CutDT = cms.double(30.0),
        Chi2CutGEM = cms.double(1.0),
        Chi2CutME0 = cms.double(1.0),
        Chi2CutRPC = cms.double(1.0),
        Chi2ProbabilityCut = cms.double(30.0),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        DYTselector = cms.int32(1),
        DYTthrs = cms.vint32(10, 10),
        DYTthrsParameters = cms.PSet(
            eta0p8 = cms.vdouble(1, -0.919853, 0.990742),
            eta1p2 = cms.vdouble(1, -0.897354, 0.987738),
            eta2p0 = cms.vdouble(4, -0.986855, 0.998516),
            eta2p2 = cms.vdouble(1, -0.940342, 0.992955),
            eta2p4 = cms.vdouble(1, -0.947633, 0.993762)
        ),
        DYTupdator = cms.bool(True),
        DYTuseAPE = cms.bool(False),
        DYTuseThrsParametrization = cms.bool(True),
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        GEMRecHitLabel = cms.InputTag("gemRecHits"),
        HitThreshold = cms.int32(1),
        ME0RecHitLabel = cms.InputTag("me0Segments"),
        MuonHitsOption = cms.int32(1),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        PropDirForCosmics = cms.bool(False),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        PtCut = cms.double(1.0),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        RefitDirection = cms.string('insideOut'),
        RefitFlag = cms.bool(True),
        RefitRPCHits = cms.bool(True),
        SkipStation = cms.int32(-1),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        TrackerSkipSection = cms.int32(-1),
        TrackerSkipSystem = cms.int32(-1)
    ),
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)


process.totemRPRawToDigi = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.bool(False),
        printUnknownFrameSummary = cms.untracked.bool(False),
        testBCMostFrequent = cms.uint32(2),
        testCRC = cms.uint32(2),
        testECMostFrequent = cms.uint32(2),
        testFootprint = cms.uint32(2),
        testID = cms.uint32(2),
        useOlderT2TestFile = cms.bool(False),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(
        verbosity = cms.untracked.uint32(0)
    ),
    fedIds = cms.vuint32(578, 580, 584, 585),
    mightGet = cms.optional.untracked.vstring,
    rawDataTag = cms.InputTag("rawDataCollector"),
    subSystem = cms.string('TrackingStrip')
)


process.totemT2Digis = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.bool(False),
        printUnknownFrameSummary = cms.untracked.bool(False),
        testBCMostFrequent = cms.uint32(0),
        testCRC = cms.uint32(0),
        testECMostFrequent = cms.uint32(0),
        testFootprint = cms.uint32(2),
        testID = cms.uint32(0),
        useOlderT2TestFile = cms.bool(False),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(
        verbosity = cms.untracked.uint32(0)
    ),
    fedIds = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring,
    rawDataTag = cms.InputTag("rawDataCollector"),
    subSystem = cms.string('TotemT2')
)


process.totemTimingRawToDigi = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.bool(False),
        printUnknownFrameSummary = cms.untracked.bool(False),
        testBCMostFrequent = cms.uint32(0),
        testCRC = cms.uint32(0),
        testECMostFrequent = cms.uint32(0),
        testFootprint = cms.uint32(0),
        testID = cms.uint32(0),
        useOlderT2TestFile = cms.bool(False),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(
        verbosity = cms.untracked.uint32(0)
    ),
    fedIds = cms.vuint32(586, 587),
    mightGet = cms.optional.untracked.vstring,
    rawDataTag = cms.InputTag("rawDataCollector"),
    subSystem = cms.string('TotemTiming')
)


process.twinMuxStage2Digis = cms.EDProducer("L1TTwinMuxRawToDigi",
    DTTM7_FED_Source = cms.InputTag("rawDataCollector"),
    amcsecmap = cms.untracked.vint64(20015998343868, 20015998343868, 20015998343868, 20015998343868, 20015998343868),
    debug = cms.untracked.bool(False),
    feds = cms.untracked.vint32(1395, 1391, 1390, 1393, 1394),
    wheels = cms.untracked.vint32(-2, -1, 0, 1, 2)
)


process.ecalDigis = SwitchProducerCUDA(
    cpu = cms.EDProducer("EcalRawToDigi",
        DoRegional = cms.bool(False),
        FEDs = cms.vint32(
            601, 602, 603, 604, 605,
            606, 607, 608, 609, 610,
            611, 612, 613, 614, 615,
            616, 617, 618, 619, 620,
            621, 622, 623, 624, 625,
            626, 627, 628, 629, 630,
            631, 632, 633, 634, 635,
            636, 637, 638, 639, 640,
            641, 642, 643, 644, 645,
            646, 647, 648, 649, 650,
            651, 652, 653, 654
        ),
        FedLabel = cms.InputTag("listfeds"),
        InputLabel = cms.InputTag("rawDataCollector"),
        eventPut = cms.bool(True),
        feIdCheck = cms.bool(True),
        feUnpacking = cms.bool(True),
        forceToKeepFRData = cms.bool(False),
        headerUnpacking = cms.bool(True),
        memUnpacking = cms.bool(True),
        mightGet = cms.optional.untracked.vstring,
        numbTriggerTSamples = cms.int32(1),
        numbXtalTSamples = cms.int32(10),
        orderedDCCIdList = cms.vint32(
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,
            16, 17, 18, 19, 20,
            21, 22, 23, 24, 25,
            26, 27, 28, 29, 30,
            31, 32, 33, 34, 35,
            36, 37, 38, 39, 40,
            41, 42, 43, 44, 45,
            46, 47, 48, 49, 50,
            51, 52, 53, 54
        ),
        orderedFedList = cms.vint32(
            601, 602, 603, 604, 605,
            606, 607, 608, 609, 610,
            611, 612, 613, 614, 615,
            616, 617, 618, 619, 620,
            621, 622, 623, 624, 625,
            626, 627, 628, 629, 630,
            631, 632, 633, 634, 635,
            636, 637, 638, 639, 640,
            641, 642, 643, 644, 645,
            646, 647, 648, 649, 650,
            651, 652, 653, 654
        ),
        silentMode = cms.untracked.bool(True),
        srpUnpacking = cms.bool(True),
        syncCheck = cms.bool(True),
        tccUnpacking = cms.bool(True)
    )
)


process.siPixelDigis = SwitchProducerCUDA(
    cpu = cms.EDProducer("SiPixelRawToDigi",
        CablingMapLabel = cms.string(''),
        ErrorList = cms.vint32(29),
        IncludeErrors = cms.bool(True),
        InputLabel = cms.InputTag("rawDataCollector"),
        Regions = cms.PSet(
            beamSpot = cms.optional.InputTag,
            deltaPhi = cms.optional.vdouble,
            inputs = cms.optional.VInputTag,
            maxZ = cms.optional.vdouble
        ),
        SiPixelQualityLabel = cms.string(''),
        UsePhase1 = cms.bool(True),
        UsePilotBlade = cms.bool(False),
        UseQualityInfo = cms.bool(False),
        UserErrorList = cms.vint32(40),
        mightGet = cms.optional.untracked.vstring
    )
)


process.muNtupleProducer = cms.EDAnalyzer("MuNtupleProducer",
    ServiceParameters = cms.PSet(
        CSCLayers = cms.untracked.bool(True),
        GEMLayers = cms.untracked.bool(True),
        ME0Layers = cms.bool(False),
        Propagators = cms.untracked.vstring(
            'SteppingHelixPropagatorAny',
            'SteppingHelixPropagatorAlong',
            'SteppingHelixPropagatorOpposite',
            'SteppingHelixPropagatorL2Any',
            'SteppingHelixPropagatorL2Along',
            'SteppingHelixPropagatorL2Opposite',
            'SteppingHelixPropagatorAnyNoError',
            'SteppingHelixPropagatorAlongNoError',
            'SteppingHelixPropagatorOppositeNoError',
            'SteppingHelixPropagatorL2AnyNoError',
            'SteppingHelixPropagatorL2AlongNoError',
            'SteppingHelixPropagatorL2OppositeNoError',
            'PropagatorWithMaterial',
            'PropagatorWithMaterialOpposite',
            'SmartPropagator',
            'SmartPropagatorOpposite',
            'SmartPropagatorAnyOpposite',
            'SmartPropagatorAny',
            'SmartPropagatorRK',
            'SmartPropagatorAnyRK',
            'StraightLinePropagator'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    cscSegmentTag = cms.untracked.InputTag("cscSegments"),
    gemDigiTag = cms.untracked.InputTag("muonGEMDigis"),
    gemOHStatusTag = cms.untracked.InputTag("muonGEMDigis","OHStatus"),
    gemRecHitTag = cms.untracked.InputTag("gemRecHits"),
    gemSegmentTag = cms.untracked.InputTag("gemSegments"),
    gemSimHitTag = cms.untracked.InputTag("g4SimHits","MuonGEMHits"),
    genParticlesTag = cms.untracked.InputTag("genParticles"),
    isMC = cms.bool(False),
    muonSimTag = cms.untracked.InputTag("muons"),
    muonTag = cms.untracked.InputTag("muons"),
    ph1DTtTrigMode = cms.untracked.string('DTTTrigSyncFromDB'),
    ph1DTtTrigModeConfig = cms.untracked.PSet(
        debug = cms.untracked.bool(False),
        doT0Correction = cms.bool(True),
        doTOFCorrection = cms.bool(False),
        doWirePropCorrection = cms.bool(False),
        t0Label = cms.string(''),
        tTrigLabel = cms.string(''),
        tofCorrType = cms.int32(2),
        vPropWire = cms.double(24.4),
        wirePropCorrType = cms.int32(0)
    ),
    ph1DtDigiTag = cms.untracked.InputTag("muonDTDigis"),
    ph1DtSegmentTag = cms.untracked.InputTag("dt4DSegments"),
    ph2DtDigiTag = cms.untracked.InputTag("none"),
    ph2DtSegmentTag = cms.untracked.InputTag("none"),
    primaryVerticesTag = cms.untracked.InputTag("offlinePrimaryVertices"),
    storeAMCStatus = cms.bool(True),
    storeOHStatus = cms.bool(True),
    tcdsTag = cms.untracked.InputTag("tcdsDigis","tcdsRecord","RECO"),
    trigTag = cms.untracked.InputTag("TriggerResults","","HLT")
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('MuDPGNtuple.root')
)


process.ProcessAcceleratorAlpaka = ProcessAcceleratorAlpaka()


process.ProcessAcceleratorCUDA = ProcessAcceleratorCUDA()


process.ProcessAcceleratorROCm = ProcessAcceleratorROCm()


process.AnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.AnalyticalPropagatorParabolicMF = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorParabolicMf'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.Chi2EstimatorForMuRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2EstimatorForMuRefit'),
    MaxChi2 = cms.double(100000.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.Chi2EstimatorForMuonTrackLoader = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2EstimatorForMuonTrackLoader'),
    MaxChi2 = cms.double(100000.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.Chi2EstimatorForRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2EstimatorForRefit'),
    MaxChi2 = cms.double(100000.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.Chi2MeasurementEstimatorForP5 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2MeasurementEstimatorForP5'),
    MaxChi2 = cms.double(100.0),
    MaxDisplacement = cms.double(100),
    MaxSagitta = cms.double(-1),
    MinPtForHitRecoveryInGluedDet = cms.double(100000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('DummyDetLayerGeometry')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.EstimatorForSTA = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2STA'),
    MaxChi2 = cms.double(1000.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.FittingSmootherRKP5 = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('FittingSmootherRKP5'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(4),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.FlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('LooperFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK')
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlbMuKFFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('GlbMuKFFitter'),
    Estimator = cms.string('Chi2EstimatorForMuRefit'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.KFFitterForRefitInsideOut = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitterForRefitInsideOut'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFFitterForRefitOutsideIn = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitterForRefitOutsideIn'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFFittingSmootheForSTA = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFitterSmootherSTA'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('KFFitterSTA'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('KFSmootherSTA'),
    appendToDataLabel = cms.string('')
)


process.KFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('KFFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('KFSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFSmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherForMuonTrackLoader'),
    Estimator = cms.string('Chi2EstimatorForMuonTrackLoader'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.KFSmootherForMuonTrackLoaderL3 = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherForMuonTrackLoaderL3'),
    Estimator = cms.string('Chi2EstimatorForMuonTrackLoader'),
    Propagator = cms.string('SmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.KFSmootherForRefitInsideOut = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherForRefitInsideOut'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFSmootherForRefitOutsideIn = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherForRefitOutsideIn'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitterForSTA = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitterSTA'),
    Estimator = cms.string('Chi2STA'),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFTrajectorySmootherForSTA = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherSTA'),
    Estimator = cms.string('Chi2STA'),
    Propagator = cms.string('SteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.LooperFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('LooperFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('LooperFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('LooperSmoother'),
    appendToDataLabel = cms.string('')
)


process.LooperTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('LooperFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.LooperTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('LooperSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.MRHChi2MeasurementEstimator = cms.ESProducer("MRHChi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('MRHChi2'),
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0)
)


process.MRHFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('MRHFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('MRHFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('MRHSmoother'),
    appendToDataLabel = cms.string('')
)


process.MRHTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('MRHFitter'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.MRHTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('MRHSmoother'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.MTDTransientTrackingRecHitBuilder = cms.ESProducer("MTDTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('MTDRecHitBuilder')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonTransientTrackingRecHitBuilderESProducer = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('MuonRecHitBuilder')
)


process.OppositeAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorOpposite'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.OppositeAnalyticalPropagatorParabolicMF = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorParabolicMfOpposite'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50),
    EdgeClusterErrorY = cms.double(85),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1),
    eff_charge_cut_highY = cms.double(1),
    eff_charge_cut_lowX = cms.double(0),
    eff_charge_cut_lowY = cms.double(0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    isPhase2 = cms.bool(False),
    lAOffset = cms.double(0),
    lAWidthBPix = cms.double(0),
    lAWidthFPix = cms.double(0),
    size_cutX = cms.double(3),
    size_cutY = cms.double(3),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1),
    useOldAnalPropLogic = cms.bool(False),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForLoopersOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopersOpposite'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1),
    useOldAnalPropLogic = cms.bool(False),
    useRungeKutta = cms.bool(False)
)


process.RK1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RK1DFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RK1DFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RK1DTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RK1DFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RK1DTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RK1DSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RKFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKOutliers1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKOutliers1DFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RK1DFitter'),
    HighEtaSwitch = cms.double(5),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.RungeKuttaTrackerPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('RungeKuttaTrackerPropagatorOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.SiPixelTemplateStoreESProducer = cms.ESProducer("SiPixelTemplateStoreESProducer",
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.SmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.SmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.SmartPropagatorAnyRK = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorAnyRK'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagator')
)


process.SmartPropagatorAnyRKOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorAnyRKOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagatorOpposite')
)


process.SmartPropagatorOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.SmartPropagatorRK = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorRK'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagator')
)


process.SmartPropagatorRKOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('SmartPropagatorRKOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagatorOpposite')
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorAlongNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlongNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorAnyNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAnyNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorL2Along = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2Along'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorL2AlongNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2AlongNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorL2Any = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2Any'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorL2AnyNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2AnyNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorL2Opposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2Opposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorL2OppositeNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorL2OppositeNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.SteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorOppositeNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOppositeNoError'),
    NoErrorPropagation = cms.bool(True),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StraightLinePropagator = cms.ESProducer("StraightLinePropagatorESProducer",
    ComponentName = cms.string('StraightLinePropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TTRHBuilderFast = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithoutAngleFast'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('PixelCPEFast'),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("DD4hep_VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.beamHaloNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('BeamHaloNavigationSchool'),
    PluginName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("SkippingLayerCosmicNavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    allSelf = cms.bool(True),
    noPXB = cms.bool(False),
    noPXF = cms.bool(False),
    noTEC = cms.bool(False),
    noTIB = cms.bool(False),
    noTID = cms.bool(False),
    noTOB = cms.bool(False),
    selfSearch = cms.bool(True)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True)
)


process.duplicateDisplaceTrackCandidatesChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('duplicateDisplacedTrackCandidatesChi2Est'),
    MaxChi2 = cms.double(100),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.duplicateTrackCandidatesChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('duplicateTrackCandidatesChi2Est'),
    MaxChi2 = cms.double(100),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalElectronicsMappingGPUESProducer = cms.ESProducer("EcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalElectronicsMappingHostESProducer = cms.ESProducer("EcalElectronicsMappingHostESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    includeBadChambers = cms.bool(True),
    includeGEM = cms.bool(True),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(True)
)


process.muonSeededMeasurementEstimatorForOutInDisplaced = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('muonSeededMeasurementEstimatorForOutInDisplaced'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    PluginName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.navigationSchoolESProducerParabolicMf = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchoolParabolicMf'),
    PluginName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityFromDbLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.tkTransientTrackingRecHitBuilderESProducer = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('Fake'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('Fake'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('Fake'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.trackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('trackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep',
        'lowPtQuadStep',
        'highPtTripletStep',
        'lowPtTripletStep',
        'detachedQuadStep',
        'detachedTripletStep',
        'pixelPairStep',
        'mixedTripletStep',
        'pixelLessStep',
        'tobTecStep',
        'jetCoreRegionalStep',
        'muonSeededStepInOut',
        'muonSeededStepOutIn',
        'displacedRegionalStep'
    ),
    appendToDataLabel = cms.string('')
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.ttrhbwor = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithoutRefit'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('Fake'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('Fake'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('140X_dataRun3_HLT_Candidate_2024_06_04_11_54_43'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(100.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(100.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(True),
    useHEUpgrade = cms.bool(True),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.prefer("es_hardcode")

process.cosmicsMuonIdTask = cms.Task(process.cosmicsVeto, process.cosmicsVetoSeeds, process.cosmicsVetoTrackCandidates, process.cosmicsVetoTracks, process.cosmicsVetoTracksRaw)


process.displacedMuonIdProducerTask = cms.Task(process.displacedMuons1stStep)


process.displacedTracksTask = cms.Task(process.displacedTracks, process.duplicateDisplacedTrackCandidates, process.duplicateDisplacedTrackClassifier, process.mergedDuplicateDisplacedTracks)


process.generalTracksTask = cms.Task(process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.generalTracks, process.mergedDuplicateTracks)


process.muIsoDeposits_ParamGlobalMuonsOldTask = cms.Task(process.muParamGlobalIsoDepositCalEcal, process.muParamGlobalIsoDepositCalHcal, process.muParamGlobalIsoDepositGsTk)


process.muIsoDeposits_ParamGlobalMuonsTask = cms.Task(process.muParamGlobalIsoDepositCalByAssociatorTowers, process.muParamGlobalIsoDepositJets, process.muParamGlobalIsoDepositTk)


process.muIsoDeposits_displacedMuonsTask = cms.Task(process.muIsoDepositCalByAssociatorTowersDisplaced, process.muIsoDepositJetsDisplaced, process.muIsoDepositTkDisplaced)


process.muIsoDeposits_muonsTask = cms.Task(process.muIsoDepositCalByAssociatorTowers, process.muIsoDepositJets, process.muIsoDepositTk)


process.muIsolation_ParamGlobalMuonsOldTask = cms.Task(process.muIsoDeposits_ParamGlobalMuonsOldTask)


process.muIsolation_ParamGlobalMuonsTask = cms.Task(process.muIsoDeposits_ParamGlobalMuonsTask)


process.muIsolation_displacedMuonsTask = cms.Task(process.muIsoDeposits_displacedMuonsTask)


process.muIsolation_muonsTask = cms.Task(process.muIsoDeposits_muonsTask)


process.muonIdProducerTask = cms.Task(process.glbTrackQual, process.muonEcalDetIds, process.muonShowerInformation, process.muons1stStep)


process.muonSeededStepCoreDisplacedTask = cms.Task(cms.TaskPlaceholder("muonSeededStepCoreInOutTask"), process.muonSeededSeedsOutInDisplaced, process.muonSeededTrackCandidatesOutInDisplaced, process.muonSeededTracksOutInDisplaced)


process.muonSeededStepDebugDisplacedTask = cms.Task(cms.TaskPlaceholder("muonSeededStepDebugInOutTask"), process.muonSeededSeedsOutInDisplacedAsTracks, process.muonSeededTrackCandidatesOutInDisplacedAsTracks)


process.muonSeededStepExtraDisplacedTask = cms.Task(cms.TaskPlaceholder("muonSeededStepExtraInOutTask"), process.muonSeededTracksOutInDisplacedClassifier)


process.muonSelectionTypeTask = cms.Task(process.muidAllArbitrated, process.muidGMStaChiCompatibility, process.muidGMTkChiCompatibility, process.muidGMTkKinkTight, process.muidGlobalMuonPromptTight, process.muidRPCMuLoose, process.muidTM2DCompatibilityLoose, process.muidTM2DCompatibilityTight, process.muidTMLastStationAngLoose, process.muidTMLastStationAngTight, process.muidTMLastStationLoose, process.muidTMLastStationOptimizedLowPtLoose, process.muidTMLastStationOptimizedLowPtTight, process.muidTMLastStationTight, process.muidTMOneStationAngLoose, process.muidTMOneStationAngTight, process.muidTMOneStationLoose, process.muidTMOneStationTight, process.muidTrackerMuonArbitrated)


process.muonreco_with_standAloneSET_Task = cms.Task(process.SETMuonSeed, process.standAloneSETMuons)


process.muontracking_with_SET_Task = cms.Task(process.SETMuonSeed, process.globalSETMuons, process.standAloneSETMuons)


process.standAloneMuonSeedsTask = cms.Task(process.ancientMuonSeed)


process.standalonemuontrackingTask = cms.Task(process.displacedMuonSeeds, process.displacedStandAloneMuons, process.refittedStandAloneMuons, process.standAloneMuonSeedsTask, process.standAloneMuons)


process.L1TRawToDigi_Legacy = cms.Task(process.csctfDigis, process.dttfDigis, process.gctDigis, process.gtDigis, process.gtEvmDigis)


process.L1TRawToDigi_Stage1 = cms.Task(process.caloStage1Digis, process.caloStage1FinalDigis, process.caloStage1LegacyFormatDigis, process.csctfDigis, process.dttfDigis, process.gctDigis, process.gtDigis)


process.L1TRawToDigi_Stage2 = cms.Task(process.bmtfDigis, process.caloLayer1Digis, process.caloStage2Digis, process.emtfStage2Digis, process.gmtStage2Digis, process.gtStage2Digis, process.gtTestcrateStage2Digis, process.omtfStage2Digis, process.rpcCPPFRawToDigi, process.rpcTwinMuxRawToDigi, process.rpcunpacker, process.twinMuxStage2Digis)


process.RawToDigiTask_hcalOnly = cms.Task(process.hcalDigis)


process.ctppsRawToDigiTask = cms.Task(process.ctppsDiamondRawToDigi, process.ctppsPixelDigis, process.totemRPRawToDigi, process.totemT2Digis, process.totemTimingRawToDigi)


process.ecalDigisTask = cms.Task(process.ecalDigis)


process.siPixelDigisTask = cms.Task(process.siPixelDigis)


process.offlineBeamSpotTask = cms.Task(process.offlineBeamSpot)


process.muIsolationDisplacedTask = cms.Task(process.muIsolation_displacedMuonsTask)


process.muIsolationTask = cms.Task(process.muIsolation_muonsTask)


process.muonSeededStepDisplacedTask = cms.Task(process.earlyDisplacedMuons, process.muonSeededStepCoreDisplacedTask, process.muonSeededStepExtraDisplacedTask)


process.muonreco_with_SET_Task = cms.Task(process.muontracking_with_SET_Task)


process.L1TRawToDigiTask = cms.Task(process.L1TRawToDigi_Stage1, process.L1TRawToDigi_Stage2)


process.RawToDigiTask = cms.Task(process.L1TRawToDigiTask, process.ctppsRawToDigiTask, process.ecalDigisTask, process.ecalPreshowerDigis, process.hcalDigis, process.muonCSCDigis, process.muonDTDigis, process.muonGEMDigis, process.muonRPCDigis, process.onlineMetaDataDigis, process.scalersRawToDigi, process.siPixelDigisTask, process.siStripDigis, process.tcdsDigis)


process.RawToDigiTask_ecalOnly = cms.Task(process.ecalDigisTask, process.ecalPreshowerDigis, process.scalersRawToDigi)


process.RawToDigiTask_noTk = cms.Task(process.L1TRawToDigiTask, process.castorDigis, process.ctppsRawToDigiTask, process.ecalDigisTask, process.ecalPreshowerDigis, process.hcalDigis, process.muonCSCDigis, process.muonDTDigis, process.muonRPCDigis, process.onlineMetaDataDigis, process.scalersRawToDigi, process.tcdsDigis)


process.RawToDigiTask_pixelOnly = cms.Task(process.scalersRawToDigi, process.siPixelDigisTask)


process.iterDisplcedTrackingTask = cms.Task(process.displacedTracksTask, process.muonSeededStepDisplacedTask, process.preDuplicateMergingDisplacedTracks)


process.displacedGlobalMuonTrackingTask = cms.Task(process.displacedGlobalMuons, process.iterDisplcedTrackingTask)


process.globalmuontrackingTask = cms.Task(process.displacedGlobalMuonTrackingTask, process.globalMuons, process.tevMuons)


process.muonGlobalRecoTask = cms.Task(process.displacedMuonIdProducerTask, process.globalmuontrackingTask, process.muIsolationDisplacedTask, process.muIsolationTask, process.muonIdProducerTask, process.muonSelectionTypeTask)


process.muonrecoTask = cms.Task(process.displacedMuonIdProducerTask, process.displacedMuonSeeds, process.displacedStandAloneMuons, process.globalmuontrackingTask, process.muonIdProducerTask, process.refittedStandAloneMuons, process.standAloneMuonSeedsTask, process.standAloneMuons)


process.muonreco_plus_isolationTask = cms.Task(process.muIsolationTask, process.muonrecoTask)


process.muontrackingTask = cms.Task(process.displacedMuonSeeds, process.displacedStandAloneMuons, process.globalmuontrackingTask, process.refittedStandAloneMuons, process.standAloneMuonSeedsTask, process.standAloneMuons)


process.cosmicsMuonIdSequence = cms.Sequence(process.cosmicsMuonIdTask)


process.displacedGlobalMuonTracking = cms.Sequence(process.displacedGlobalMuonTrackingTask)


process.displacedTracksSequence = cms.Sequence(process.displacedTracksTask)


process.generalTracksSequence = cms.Sequence(process.generalTracksTask)


process.globalmuontracking = cms.Sequence(process.globalmuontrackingTask)


process.iterDisplcedTracking = cms.Sequence(process.iterDisplcedTrackingTask)


process.muIsoDeposits_ParamGlobalMuons = cms.Sequence(process.muIsoDeposits_ParamGlobalMuonsTask)


process.muIsoDeposits_ParamGlobalMuonsOld = cms.Sequence(process.muIsoDeposits_ParamGlobalMuonsOldTask)


process.muIsoDeposits_displacedMuons = cms.Sequence(process.muIsoDeposits_displacedMuonsTask)


process.muIsoDeposits_muons = cms.Sequence(process.muIsoDeposits_muonsTask)


process.muIsolation = cms.Sequence(process.muIsolationTask)


process.muIsolationDisplaced = cms.Sequence(process.muIsolationDisplacedTask)


process.muIsolation_ParamGlobalMuons = cms.Sequence(process.muIsolation_ParamGlobalMuonsTask)


process.muIsolation_ParamGlobalMuonsOld = cms.Sequence(process.muIsolation_ParamGlobalMuonsOldTask)


process.muIsolation_displacedMuons = cms.Sequence(process.muIsolation_displacedMuonsTask)


process.muIsolation_muons = cms.Sequence(process.muIsolation_muonsTask)


process.muonGlobalReco = cms.Sequence(process.muonGlobalRecoTask)


process.muonIdProducerSequence = cms.Sequence(process.muonIdProducerTask)


process.muonSeededStepCoreDisplaced = cms.Sequence(process.muonSeededStepCoreDisplacedTask)


process.muonSeededStepDebugDisplaced = cms.Sequence(process.muonSeededStepDebugDisplacedTask)


process.muonSeededStepDisplaced = cms.Sequence(process.muonSeededStepDisplacedTask)


process.muonSeededStepExtraDisplaced = cms.Sequence(process.muonSeededStepExtraDisplacedTask)


process.muonSelectionTypeSequence = cms.Sequence(process.muonSelectionTypeTask)


process.muonreco = cms.Sequence(process.muonrecoTask)


process.muonrecoComplete = cms.Sequence(process.muonSelectionTypeTask, process.muonreco_plus_isolationTask)


process.muonreco_plus_isolation = cms.Sequence(process.muonreco_plus_isolationTask)


process.muonreco_with_SET = cms.Sequence(process.muonreco_with_SET_Task)


process.muonreco_with_standAloneSET = cms.Sequence(process.muonreco_with_standAloneSET_Task)


process.muontracking = cms.Sequence(process.muontrackingTask)


process.muontracking_with_SET = cms.Sequence(process.muontracking_with_SET_Task)


process.standAloneMuonSeeds = cms.Sequence(process.standAloneMuonSeedsTask)


process.standalonemuontracking = cms.Sequence(process.standalonemuontrackingTask)


process.L1TRawToDigi = cms.Sequence(process.L1TRawToDigiTask)


process.RawToDigi = cms.Sequence(process.RawToDigiTask)


process.RawToDigi_ecalOnly = cms.Sequence(process.RawToDigiTask_ecalOnly)


process.RawToDigi_hcalOnly = cms.Sequence(process.RawToDigiTask_hcalOnly)


process.RawToDigi_noTk = cms.Sequence(process.RawToDigiTask_noTk)


process.RawToDigi_pixelOnly = cms.Sequence(process.RawToDigiTask_pixelOnly)


process.ctppsRawToDigi = cms.Sequence(process.ctppsRawToDigiTask)


process.p = cms.Path(process.muonGEMDigis+process.gemRecHits+(process.offlineBeamSpot+process.standAloneMuonSeeds+process.standAloneMuons)+process.muNtupleProducer)



