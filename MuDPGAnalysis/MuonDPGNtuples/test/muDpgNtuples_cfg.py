import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from Configuration.StandardSequences.Eras import eras
from Configuration.AlCa.GlobalTag import GlobalTag

import os
import subprocess
import sys

options = VarParsing.VarParsing()

options.register('globalTag',
                 #'132X_dataRun3_Prompt_v4',
                 '124X_dataRun3_Prompt_v10',
                 #'130X_dataRun3_Prompt_v3',#Run3
                 #'125X_mcRun4_realistic_v5', #Phase-2
                 #'124X_dataRun3_Prompt_v4',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Global Tag")

options.register('nEvents',
                 100, #to run on a sub-sample
                 #-1, #default value
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
#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/125X_mcRun3_2022_realistic_v5-v2/2590000/402b16ef-be13-49c2-88f3-401adcda3d00.root']
process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/data/Run2022G/Muon/RAW-RECO/ZMu-PromptReco-v1/000/362/433/00000/092d015c-b786-4834-a4f5-d10d793432d4.root'] # v1 Run4 noPU
#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v5_2026D88PU200-v1/2590000/0193d62c-aaa9-4add-86f3-8dffb3e8abc7.root'] # v1 Run4 PU-200

#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-RECO/PU_125X_mcRun3_2022_realistic_v5-v1/2590000/086b0ef9-d0c4-4ac0-a281-51cd69e15aaf.root'] # v1 Run3


#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-RECO/125X_mcRun3_2022_realistic_v5-v2/2590000/3869aa52-c4b8-4b81-8f5d-8a6f53199d23.root']
#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_125X_mcRun4_realistic_v5_2026D88PU200-v1/2590000/0352a6bf-2ea5-4adf-a12e-072a2aa400df.root']
#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/relval/CMSSW_12_6_0_pre5/RelValZMM_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v5_2026D88PU200-v1/2590000/18a3becf-da3a-4e27-9353-2880edadf250.root']#"file:/eos/cms/store/group/dpg_gem/comm_gem/reRECO/Muon/crab_gemReReco_hv_re3/230213_023322/0000/step3_35.root"]#@["root://xrootd-cms.infn.it//store/data/Run2022E/Muon/RAW-RECO/ZMu-PromptReco-v1/000/360/019/00001/4933b7ab-622b-4b80-87ee-8165f976a332.root"]
#process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/data/Run2023B/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/366/451/00000/30ddccc4-b48e-4d6e-b213-1686fad74be4.root']#"file:/eos/cms/store/group/dpg_gem/comm_gem/reRECO/Muon/crab_gemReReco_hv_re3/230213_023322/0000/step3_35.root"]#@["root://xrootd-cms.infn.it//store/data/Run2022E/Muon/RAW-RECO/ZMu-PromptReco-v1/000/360/019/00001/4933b7ab-622b-4b80-87ee-8165f976a332.root"]
'''
if "eos/cms" in options.inputFolder:
    #files = subprocess.check_output(['xrdfs', 'root://eoscms.cern.ch/', 'ls', options.inputFolder]) ## Did work with CMSSW 11XX, not anymore w CMSSW 12
    files = os.listdir(options.inputFolder)
    #process.source.fileNames = ["file:"+options.inputFolder + f for f in files if "07a64f0e-25eb-40b6-b2a6-e8971a4e0ce8.root" in f]
    #process.source.fileNames = ['file:/eos/cms/store/data/Run2022E/Muon/RAW-RECO/ZMu-10Dec2022-v2/330000/159d8e9d-7887-4543-a637-203f4c874c48.root']#"file:/eos/cms/store/group/dpg_gem/comm_gem/reRECO/Muon/crab_gemReReco_hv_re3/230213_023322/0000/step3_35.root"]#@["root://xrootd-cms.infn.it//store/data/Run2022E/Muon/RAW-RECO/ZMu-PromptReco-v1/000/360/019/00001/4933b7ab-622b-4b80-87ee-8165f976a332.root"]
    process.source.fileNames = ['root://cms-xrd-global.cern.ch//store/data/Run2023B/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/366/451/00000/30ddccc4-b48e-4d6e-b213-1686fad74be4.root']#"file:/eos/cms/store/group/dpg_gem/comm_gem/reRECO/Muon/crab_gemReReco_hv_re3/230213_023322/0000/step3_35.root"]#@["root://xrootd-cms.infn.it//store/data/Run2022E/Muon/RAW-RECO/ZMu-PromptReco-v1/000/360/019/00001/4933b7ab-622b-4b80-87ee-8165f976a332.root"]

elif "/xrd/" in options.inputFolder:
    files = subprocess.check_output(['xrdfs', 'root://cms-xrdr.sdfarm.kr/', 'ls', options.inputFolder])
    process.source.fileNames = ["root://cms-xrdr.sdfarm.kr//" +f for f in files.split()]

else:
    files = subprocess.check_output(['ls', options.inputFolder])
    process.source.fileNames = ["file://" + options.inputFolder + "/" + f for f in files.split()]

if options.secondaryInputFolder != "" :
    files = subprocess.check_output(["ls", options.secondaryInputFolder])
    process.source.secondaryFileNames = ["file://" + options.secondaryInputFolder + "/" + f for f in files.split()]
'''

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



process.load('Configuration.StandardSequences.RawToDigi_Data_cff')

# add TrackDetectorAssociator lookup maps to the EventSetup
process.load("TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff")

process.load('MuDPGAnalysis.MuonDPGNtuples.muNtupleProducer_cfi')

process.muNtupleProducer.isMC = cms.bool(options.isMC)
process.muNtupleProducer.storeOHStatus = cms.bool(options.storeOHStatus)
process.muNtupleProducer.storeAMCStatus = cms.bool(options.storeAMCStatus)

if options.reUnpack and options.GE21:
    process.gemRecHits.ge21Off = cms.bool(not options.GE21) ## user selection GE21 = True means "store GE21 rechits"
    process.p = cms.Path(
        process.muonGEMDigis *
        process.gemRecHits *
        process.muNtupleProducer)
elif options.reUnpack:
    process.p = cms.Path(
        #process.muonGEMDigis *
        process.muNtupleProducer)
else:
    process.p = cms.Path(
        process.muNtupleProducer)
