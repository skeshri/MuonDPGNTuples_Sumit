import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import MuonServiceProxy
# add TrackDetectorAssociator lookup maps to the EventSetup
#process.load("TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff") 
# from TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff import *  
from TrackingTools.TrackAssociator.default_cfi import *


muNtupleProducer = cms.EDAnalyzer("MuNtupleProducer",
                                  MuonServiceProxy,
                                  TrackAssociatorParameterBlock,
                                  ph1DtDigiTag = cms.untracked.InputTag("muonDTDigis"),
                                  ph2DtDigiTag = cms.untracked.InputTag("none"),

                                  ph1DtSegmentTag = cms.untracked.InputTag("dt4DSegments"),        
                                  ph2DtSegmentTag = cms.untracked.InputTag("none"),
                                  trigResultsTag     = cms.untracked.InputTag("TriggerResults","","HLT"),
                                  trigEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","","HLT"),
                                  ph1DTtTrigMode = cms.untracked.string('DTTTrigSyncFromDB'),
                                  isMC = cms.bool(False),
                                  gemDigiTag = cms.untracked.InputTag("muonGEMDigis"),
                                  gemOHStatusTag = cms.untracked.InputTag("muonGEMDigis", "OHStatus"),
                                  #gemDigiTag = cms.untracked.InputTag("simMuonGEMDigis"),
                                  gemRecHitTag = cms.untracked.InputTag("gemRecHits"),
                                  gemSegmentTag = cms.untracked.InputTag("gemSegments"),
                                  cscSegmentTag = cms.untracked.InputTag("cscSegments"),
                                  muonTag = cms.untracked.InputTag("muons"),
                                  tcdsTag = cms.untracked.InputTag("tcdsDigis","tcdsRecord","RECO"),
                                  
                                  gemSimHitTag = cms.untracked.InputTag("g4SimHits","MuonGEMHits"),
                                  muonSimTag = cms.untracked.InputTag("muons"),
                                  genParticlesTag = cms.untracked.InputTag("genParticles"),
                                  primaryVerticesTag = cms.untracked.InputTag("offlinePrimaryVertices"),
                                  ph1DTtTrigModeConfig = cms.untracked.PSet(vPropWire = cms.double(24.4),
                                                                            doTOFCorrection = cms.bool(False),
                                                                            tofCorrType = cms.int32(2),
                                                                            wirePropCorrType = cms.int32(0),
                                                                            doWirePropCorrection = cms.bool(False),
                                                                            doT0Correction = cms.bool(True),
                                                                            tTrigLabel = cms.string(''),
                                                                            t0Label = cms.string(''),
                                                                            debug = cms.untracked.bool(False)
                                                                        )
)

