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
process.load('FWCore.MessageService.MessageLogger_cfi')
#SkipEvent = cms.untracked.vstring('ProductNotFound')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 100
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
        '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/c25dcb4b-95c3-480f-ab66-fec3f98eee19.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/842df1f2-510e-41ec-b5a0-94d313ff7bf7.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/8f78a0d1-0ade-4d6c-b59b-55b50a19342f.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/7e946b96-de67-48d5-9ee7-a925741f085e.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/329c8f70-0a72-442b-a385-f198928c5812.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/d768aeac-7e21-4fe6-92be-68c21f59ae95.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/fa5ee2c1-8bf7-4831-a9ce-99f2cda709a6.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/8212cc51-c382-4b7e-8c73-0e7bacb1a20e.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/fd39d9e3-15ef-4949-b50b-868b6295917b.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/5c163fd1-de21-4113-9206-91449a5eb1d5.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/3d0677df-4a52-4db2-a6c7-28736295fabe.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/00183f47-abee-4b7f-91e5-dbedad120f29.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/44a0e278-2987-4da7-941c-06b1cf6007e7.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/daee8aee-8a31-4f99-9097-94b1bcf20e1b.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/6382350b-42a8-4b5b-bf00-afbeb1f1c929.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/ca062f75-d819-4d6d-b1e6-1c6602b027fd.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/3a3f3bf3-0550-485e-907a-16f53e985306.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/78fae939-5a78-467e-8366-a5ee55d21905.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/aca67996-088f-48ce-9098-b812b68996e6.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/fdbf7f5d-cd24-4398-a25c-552cdd3792b8.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/6dade8f5-e44d-44d9-9547-e2a4433ac936.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/69bab46f-02ce-4219-9448-340d4c3c4c61.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/fb5c4dd0-0f1f-441d-8022-c1ea51706114.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/7b9f8a84-bb14-4c3d-8d6b-7ba00d0c4198.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/2d7bf715-6315-48d1-bdba-fc09a36739c0.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/ad82a0ef-f783-448d-9463-5efaca16c08d.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/47e5d4fa-c0bc-4660-a730-f6aece26dda3.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/0f88c731-aa38-41eb-becf-97ae1ab7cf30.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/36843fbc-4914-4a47-99be-d14208e8288a.root',
       '/store/data/Run2023D/Muon1/RAW-RECO/ZMu-PromptReco-v2/000/370/772/00000/c11b63be-6f60-4129-a16c-c081fdbb845a.root',
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

process.load("RecoMuon.GlobalMuonProducer.globalMuons_cfi")
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
muonstandalonereco = cms.Sequence(process.offlineBeamSpot + process.standAloneMuonSeeds * process.standAloneMuons * process.globalMuons)

#process.globalMuons = process.globalMuons.clone()
#process.globalMuons.MuonCollectionLabel = cms.InputTag("standAloneMuons","UpdatedAtVtx")
#process.globalMuons.GLBTrajBuilderParameters.GlobalMuonTrackMatcher.Propagator = 'SmartPropagatorRK'
#process.globalMuons.GLBTrajBuilderParameters.TrackTransformer.Propagator = cms.string('SmartPropagatorAnyRK')


#muonstandalonereco = cms.Sequence(process.offlineBeamSpot + process.standAloneMuons)


process.muNtupleProducer.isMC = cms.bool(options.isMC)
process.muNtupleProducer.storeOHStatus = cms.bool(options.storeOHStatus)
process.muNtupleProducer.storeAMCStatus = cms.bool(options.storeAMCStatus)

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
