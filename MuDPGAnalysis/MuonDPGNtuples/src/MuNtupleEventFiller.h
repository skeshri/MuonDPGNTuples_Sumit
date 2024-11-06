#ifndef MuNTuple_EventFiller_h
#define MuNTuple_EventFiller_h

#include "MuDPGAnalysis/MuonDPGNtuples/src/MuNtupleBaseFiller.h"
#include "DataFormats/TCDS/interface/TCDSRecord.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/PrescaleService/interface/PrescaleService.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include <vector>
#include <cstdint>
#include <map>

class MuNtupleEventFiller : public MuNtupleBaseFiller
{

 public:

  /// Constructor
  MuNtupleEventFiller(edm::ConsumesCollector && collector,
		      const std::shared_ptr<MuNtupleConfig> config, 
		      std::shared_ptr<TTree> tree, const std::string & label);

  ///Destructor
  virtual ~MuNtupleEventFiller();
 
  /// Intialize function : setup tree branches etc ... 
  virtual void initialize() final;
  
  /// Clear branches before event filling 
  virtual void clear() final;

  /// Fill tree branches for a given events
  virtual void fill(const edm::Event & ev) final;    

 private :
  edm::EDGetTokenT<TCDSRecord> m_TCDStoken;
  edm::EDGetTokenT<edm::TriggerResults> m_trigToken;
  edm::EDGetTokenT<std::vector<reco::Vertex>> m_primaryVerticesToken;

  int m_runNumber;
  int m_nVtx;
  int  m_lumiBlock;
  int64_t m_eventNumber;
  int m_bunchCrossing;
  int m_orbitNumber;
  int m_L1A_1_Diff;
  int m_L1A_2_Diff;
  int m_L1A_3_Diff;
  int m_L1A_4_Diff;
  std::vector<std::string> m_trigName;
  std::vector<float> m_trigDecision;
  std::vector<float> m_trigPS;
  
  HLTConfigProvider hltConfig_;

};
  
#endif
