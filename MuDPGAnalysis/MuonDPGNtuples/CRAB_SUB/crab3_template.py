# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferLogs = True
config.General.workArea = '/afs/cern.ch/work/s/skeshri/GEM_efficiency/Ntuple/HI/CMSSW_13_2_5_patch3/src/MuDPGAnalysis/MuonDPGNtuples/CRAB_SUB/'
config.General.transferOutputs = True


config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/s/skeshri/GEM_efficiency/Ntuple/HI/CMSSW_13_2_5_patch3/src/MuDPGAnalysis/MuonDPGNtuples/test/muDpgNtuples_cfg.py'
config.JobType.pyCfgParams = ['isMC=False', 'nEvents=-1', 'globalTag=132X_dataRun3_Prompt_v4']

config.section_('Data')
config.Data.unitsPerJob = 1
config.Data.inputDataset = "/HIPhysicsRawPrime0/HIRun2023A-PbPbEMu-PromptReco-v2/RAW-RECO"
config.Data.inputDBS = 'global'
config.Data.publication = False
config.Data.outLFNDirBase = '/store/group/dpg_gem/comm_gem/P5_Commissioning/2022/GEMCommonNtuples'
config.Data.splitting = 'FileBased'
config.Data.allowNonValidInputDataset = True

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
