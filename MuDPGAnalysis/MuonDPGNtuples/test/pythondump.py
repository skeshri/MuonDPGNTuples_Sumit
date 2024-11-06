############# GT: 140X_dataRun3_HLT_Candidate_2024_06_04_11_54_43
----- Begin Fatal Exception 11-Oct-2024 13:46:12 CEST-----------------------
An exception of category 'ConfigFileReadError' occurred while
   [0] Processing the python configuration file named muDpgNtuples_STA_cfg.py
Exception Message:
 unknown python problem occurred.
KeyboardInterrupt: <EMPTY MESSAGE>

At:
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/external/python3/3.9.14-8e02587b42992e07ed46b00eca9dfc3a/lib/python3.9/inspect.py(746): getmodule
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/external/python3/3.9.14-8e02587b42992e07ed46b00eca9dfc3a/lib/python3.9/inspect.py(829): findsource
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/external/python3/3.9.14-8e02587b42992e07ed46b00eca9dfc3a/lib/python3.9/inspect.py(1507): getframeinfo
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/FWCore/ParameterSet/python/Mixins.py(709): saveOrigin
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/FWCore/ParameterSet/python/Mixins.py(440): clone
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/EventFilter/CTPPSRawToDigi/python/ctppsDiamondRawToDigi_cfi.py(11): <module>
  <frozen importlib._bootstrap>(228): _call_with_frames_removed
  <frozen importlib._bootstrap_external>(850): exec_module
  <frozen importlib._bootstrap>(695): _load_unlocked
  <frozen importlib._bootstrap>(986): _find_and_load_unlocked
  <frozen importlib._bootstrap>(1007): _find_and_load
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/EventFilter/CTPPSRawToDigi/python/ctppsRawToDigi_cff.py(14): <module>
  <frozen importlib._bootstrap>(228): _call_with_frames_removed
  <frozen importlib._bootstrap_external>(850): exec_module
  <frozen importlib._bootstrap>(695): _load_unlocked
  <frozen importlib._bootstrap>(986): _find_and_load_unlocked
  <frozen importlib._bootstrap>(1007): _find_and_load
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/Configuration/StandardSequences/python/RawToDigi_cff.py(46): <module>
  <frozen importlib._bootstrap>(228): _call_with_frames_removed
  <frozen importlib._bootstrap_external>(850): exec_module
  <frozen importlib._bootstrap>(695): _load_unlocked
  <frozen importlib._bootstrap>(986): _find_and_load_unlocked
  <frozen importlib._bootstrap>(1007): _find_and_load
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/Configuration/StandardSequences/python/RawToDigi_Data_cff.py(3): <module>
  <frozen importlib._bootstrap>(228): _call_with_frames_removed
  <frozen importlib._bootstrap_external>(850): exec_module
  <frozen importlib._bootstrap>(695): _load_unlocked
  <frozen importlib._bootstrap>(986): _find_and_load_unlocked
  <frozen importlib._bootstrap>(1007): _find_and_load
  /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_11/src/FWCore/ParameterSet/python/Config.py(761): load
  muDpgNtuples_STA_cfg.py(128): <module>

----- End Fatal Exception -------------------------------------------------
