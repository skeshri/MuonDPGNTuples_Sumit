#include "MuDPGAnalysis/MuonDPGNtuples/src/MuNtupleEventFiller.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "TString.h"

MuNtupleEventFiller::MuNtupleEventFiller(edm::ConsumesCollector && collector,
					 const std::shared_ptr<MuNtupleConfig> config, 
					 std::shared_ptr<TTree> tree, const std::string & label) : 
  MuNtupleBaseFiller(config, tree, label)
{
  edm::InputTag & tcdsTag = m_config->m_inputTags["tcdsTag"];
  if (tcdsTag.label() != "none") m_TCDStoken = collector.consumes<TCDSRecord>(tcdsTag);

  edm::InputTag & primaryVerticesTag = m_config->m_inputTags["primaryVerticesTag"];
  if (primaryVerticesTag.label() != "none") m_primaryVerticesToken = collector.consumes<std::vector<reco::Vertex>>(primaryVerticesTag);

  edm::InputTag & trigTag = m_config->m_inputTags["trigTag"];
  if (trigTag.label() != "none") m_trigToken = collector.consumes<edm::TriggerResults>(trigTag);
}


MuNtupleEventFiller::~MuNtupleEventFiller() 
{

};

void MuNtupleEventFiller::initialize()
{
  
  m_tree->Branch((m_label + "_runNumber").c_str(), &m_runNumber, (m_label + "_runNumber/I").c_str());
  m_tree->Branch((m_label + "_nVtx").c_str(), &m_nVtx, (m_label + "_nVtx/I").c_str());
  m_tree->Branch((m_label + "_lumiBlock").c_str(), &m_lumiBlock, (m_label + "_lumiBlock/I").c_str());
  m_tree->Branch((m_label + "_eventNumber").c_str(), &m_eventNumber, (m_label + "_eventNumber/L").c_str());
  m_tree->Branch((m_label + "_bunchCrossing").c_str(), &m_bunchCrossing, (m_label + "_bunchCrossing/I").c_str());
  m_tree->Branch((m_label + "_orbitNumber").c_str(), &m_orbitNumber, (m_label + "_orbitNumber/I").c_str());
  m_tree->Branch((m_label + "_1stLast_L1A").c_str(), &m_L1A_1_Diff, (m_label + "_1stLast_L1A/I").c_str());
  m_tree->Branch((m_label + "_2ndLast_L1A").c_str(), &m_L1A_2_Diff, (m_label + "_2ndLast_L1A/I").c_str());
  m_tree->Branch((m_label + "_3rdLast_L1A").c_str(), &m_L1A_3_Diff, (m_label + "_3rdLast_L1A/I").c_str());
  m_tree->Branch((m_label + "_4thLast_L1A").c_str(), &m_L1A_4_Diff, (m_label + "_4thLast_L1A/I").c_str());
  m_tree->Branch((m_label + "_trigName").c_str(), &m_trigName);
  m_tree->Branch((m_label + "_trigDecision").c_str(), &m_trigDecision);
  m_tree->Branch((m_label + "_trigPS").c_str(), &m_trigPS);
  //m_tree->Branch((m_label + "_trigMap").c_str(), &m_trigMap, (m_label + "_trigMap").c_str());
  //m_tree->Branch((m_label + "_trigName").c_str(), &m_trigName);
  //m_tree->Branch((m_label + "_trigDecision").c_str(), &m_trigDecision);
  //m_tree->Branch((m_label + "_trigMap").c_str(), &m_trigMap);
      
}

void MuNtupleEventFiller::clear()
{

  m_runNumber   = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_nVtx   = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_lumiBlock   = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_eventNumber = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_bunchCrossing = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_orbitNumber = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_L1A_1_Diff = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_L1A_2_Diff = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_L1A_3_Diff = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
  m_L1A_4_Diff = MuNtupleBaseFiller::DEFAULT_INT_VAL_POS;
    //m_trigMap.clear();
  m_trigName.clear();
  m_trigDecision.clear();
  m_trigPS.clear();
    
}

void MuNtupleEventFiller::fill(const edm::Event & ev)
{

  clear();
  

  auto tcdsData = conditionalGet<TCDSRecord>(ev, m_TCDStoken, "tcdsRecord");
  auto vtxs = conditionalGet<std::vector<reco::Vertex>>(ev, m_primaryVerticesToken, "std::vector<reco::Vertex>");

  auto triggerResults = conditionalGet<edm::TriggerResults>(ev, m_trigToken,"edm::TriggerResults"); 


  m_runNumber   = ev.run();
  m_lumiBlock   = ev.getLuminosityBlock().luminosityBlock();
  m_eventNumber = ev.eventAuxiliary().event();
  m_bunchCrossing = ev.bunchCrossing();
  m_orbitNumber = ev.orbitNumber();

  if(tcdsData.isValid()){
  m_L1A_1_Diff = 3564 * (tcdsData->getOrbitNr() - tcdsData->getL1aHistoryEntry(0).getOrbitNr()) + tcdsData->getBXID() - tcdsData->getL1aHistoryEntry(0).getBXID();
  
  m_L1A_2_Diff = 3564 * (tcdsData->getOrbitNr() - tcdsData->getL1aHistoryEntry(1).getOrbitNr()) + tcdsData->getBXID() - tcdsData->getL1aHistoryEntry(1).getBXID();
  
  m_L1A_3_Diff = 3564 * (tcdsData->getOrbitNr() - tcdsData->getL1aHistoryEntry(2).getOrbitNr()) + tcdsData->getBXID() - tcdsData->getL1aHistoryEntry(2).getBXID();
  
  m_L1A_4_Diff = 3564 * (tcdsData->getOrbitNr() - tcdsData->getL1aHistoryEntry(3).getOrbitNr()) + tcdsData->getBXID() - tcdsData->getL1aHistoryEntry(3).getBXID();
  }

  if(vtxs.isValid()){
      m_nVtx = vtxs->size();
  
  }


    
  const edm::TriggerNames &names = ev.triggerNames(*triggerResults);
    for (size_t j=0; j < triggerResults->size(); j++) {
        
        std::string trig_ = names.triggerName(j);
        TString T_trig_(trig_);
        if(! (T_trig_.Contains("HLT_Mu") or (T_trig_.Contains("HLT_IsoMu"))) ) continue;
       if (triggerResults->accept(j)) {
        //std::cout<<trig_<<"\n";
        float ps_value=1.0;
        const unsigned int prescaleSize = hltConfig_.prescaleSize();
        for (unsigned int ps = 0; ps < prescaleSize; ps++) {
            auto const prescaleValue = hltConfig_.prescaleValue<double>(ps, trig_);
            if (prescaleValue != 1) {
                ps_value = prescaleValue;
            }
        }

        //std::cout<<trig_<<"\t"<<ps_value<<"\t"<<std::endl;
            m_trigName.push_back(trig_);
            m_trigPS.push_back(ps_value);
            m_trigDecision.push_back(1);
       }
     }


  return;

}
