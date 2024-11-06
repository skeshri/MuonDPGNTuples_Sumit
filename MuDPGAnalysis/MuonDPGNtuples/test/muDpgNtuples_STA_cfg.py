import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from Configuration.StandardSequences.Eras import eras
from Configuration.AlCa.GlobalTag import GlobalTag

import os
import subprocess
import sys

options = VarParsing.VarParsing()

options.register('globalTag',
                '140X_dataRun3_HLT_Candidate_2024_06_04_11_54_43',
                 #'130X_dataRun3_Prompt_v4',
                 #'132X_dataRun3_Prompt_v4',
                 #'140X_dataRun3_Prompt_v2',
                 #'130X_dataRun3_Prompt_v3',#Run3
                 #'125X_mcRun4_realistic_v5', #Phase-2
                 #'124X_dataRun3_Prompt_v4',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Global Tag")

options.register('nEvents',
                 #10, #to run on a sub-sample
                 -1, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum number of processed events")

options.register('isMC',
                 False, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Dataset is MC")

options.register('reUnpack',
                 True, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "enables reprocessing of digis: i.e OHStatus is not stored in RECO datesets, but can be extracted by re-unpacking data from a RAW dataset.")

options.register('storeOHStatus',
                 True, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Save OH status info from unpacker")

options.register('storeAMCStatus',
                 True, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Save AMC status info from unpacker")

options.register('GE21',
                 True, #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "enables storing of GE21 rechits, disabled by default in CMSSW: i.e when running on a RAW dataset it's possible to reprocess digi and build GE21 rechits and save them in the ntuples")

options.register('inputFolder',
                 #/eos/cms/store/
                 #"/eos/cms/store/data/Run2022D/Muon/RAW-RECO/ZMu-PromptReco-v2/000/357/734/00000/",
                 "/eos/cms/store/group/dpg_gem/comm_gem/reRECO/Muon/crab_gemReReco_hv_re3/230213_023322/0000/",
                 #"/eos/cms/store/group/dpg_gem/comm_gem/reRECO/SingleMuon/GEM-reRECO-GEM-only__Run2022B-ZMu-PromptReco-v1__RAW-RECO/220721_151149/0000/",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "EOS folder with input files")

options.register('secondaryInputFolder',
                 '', #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "EOS folder with input files for secondary files")

# options.register('fileNumber',
#                  "1", #default value
#                  VarParsing.VarParsing.multiplicity.singleton,
#                  VarParsing.VarParsing.varType.string,
#                  "FileNumber to be processed")

options.register('ntupleName',
                 'MuDPGNtuple', #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Name for output ntuple")

options.parseArguments()

process = cms.Process("MUNTUPLES",eras.Run3)#Run2_2018)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load("FWCore.PrescaleService.PrescaleService_cfi")
process.load('FWCore.MessageService.MessageLogger_cfi')
#SkipEvent = cms.untracked.vstring('ProductNotFound')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.nEvents))

print("############# GT:",options.globalTag )
process.GlobalTag.globaltag = cms.string(options.globalTag)
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(),
        secondaryFileNames = cms.untracked.vstring()
)
#process.source.fileNames = ['/store/data/Run2024D/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/380/306/00000/00c30283-19ba-4e50-9ac1-dceff63c8b20.root'] # v1 Run4 noPU
process.source.fileNames = ['/store/data/Run2024D/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/380/567/00000/09e1f948-c1d2-4ba9-abf0-3606a5a5b982.root']
"""
process.source.fileNames = ['/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/611f4885-6906-43e8-86c7-7573055153e7.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/f0046433-2772-42f6-9841-c91f94d92d3f.root']

"""
process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string(options.ntupleName+".root")
    )


process.load('Configuration/StandardSequences/GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('RecoLocalMuon.GEMRecHit.gemRecHits_cfi')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('RecoMuon.StandAloneMuonProducer.standAloneMuons_cfi')
process.load('RecoMuon.Configuration.RecoMuonPPonly_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")


## for global muons
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from RecoMuon.TrackingTools.MuonTrackLoader_cff import *
from RecoMuon.GlobalTrackingTools.GlobalTrajectoryBuilderCommon_cff import *



# add TrackDetectorAssociator lookup maps to the EventSetup
process.load("TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff")

process.load('MuDPGAnalysis.MuonDPGNtuples.muNtupleProducer_cfi')


process.standAloneMuons = process.standAloneMuons.clone()
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableGEMMeasurement = cms.bool(False)
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableGEMMeasurement = cms.bool(False)

process.standAloneMuons.STATrajBuilderParameters.FilterParameters.CSCRecSegmentLabel = cms.InputTag("cscSegments")
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.DTRecSegmentLabel = cms.InputTag("dt4DSegments")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.CSCRecSegmentLabel = cms.InputTag("cscSegments")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.DTRecSegmentLabel = cms.InputTag("dt4DSegments")
process.ancientMuonSeed.EnableDTMeasurement = False
process.ancientMuonSeed.CSCRecSegmentLabel = "cscSegments"

process.globalMuons = process.globalMuons.clone()

muonstandalonereco = cms.Sequence(process.offlineBeamSpot + process.standAloneMuonSeeds * process.standAloneMuons)
#muonstandalonereco = cms.Sequence(process.offlineBeamSpot + process.standAloneMuonSeeds * process.standAloneMuons + process.globalMuons)
#muonstandalonereco = cms.Sequence(process.offlineBeamSpot + process.standAloneMuons)


process.muNtupleProducer.isMC = cms.bool(options.isMC)
process.muNtupleProducer.storeOHStatus = cms.bool(options.storeOHStatus)
process.muNtupleProducer.storeAMCStatus = cms.bool(options.storeAMCStatus)

#print(process.dumpPython())

if options.reUnpack and options.GE21:
    process.gemRecHits.ge21Off = cms.bool(not options.GE21) ## user selection GE21 = True means "store GE21 rechits"
    process.p = cms.Path(
        process.muonGEMDigis *
        process.gemRecHits *
        muonstandalonereco *
        process.muNtupleProducer)
elif options.reUnpack:
    process.p = cms.Path(
        #process.muonGEMDigis *
        process.muNtupleProducer)
else:
    process.p = cms.Path(
        process.muNtupleProducer)
