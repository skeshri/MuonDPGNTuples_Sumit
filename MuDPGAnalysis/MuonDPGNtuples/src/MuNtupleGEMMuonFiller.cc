
#include "MuDPGAnalysis/MuonDPGNtuples/src/MuNtupleGEMMuonFiller.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Ref.h"
#include "Geometry/GEMGeometry/interface/GEMGeometry.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include "DataFormats/MuonDetId/interface/DTChamberId.h"
#include "DataFormats/MuonReco/interface/MuonChamberMatch.h"
#include "DataFormats/MuonReco/interface/MuonSegmentMatch.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/GEMRecHit/interface/GEMRecHitCollection.h"
#include "DataFormats/GEMRecHit/interface/GEMSegment.h"
#include "DataFormats/GEMRecHit/interface/GEMSegmentCollection.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "DataFormats/MuonDetId/interface/GEMDetId.h"
#include "DataFormats/CSCRecHit/interface/CSCSegment.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"

#include "DataFormats/GeometryCommonDetAlgo/interface/ErrorFrameTransformer.h"
#include "TrackPropagation/SteppingHelixPropagator/interface/SteppingHelixStateInfo.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"

#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>

#include "TVectorF.h"
#include "TFile.h"

MuNtupleGEMMuonFiller::MuNtupleGEMMuonFiller(edm::ConsumesCollector && collector,
					     const std::shared_ptr<MuNtupleConfig> config, 
					     std::shared_ptr<TTree> tree, const std::string & label) : 
MuNtupleBaseFiller(config, tree, label), m_nullVecF()
{

  edm::InputTag & muonTag = m_config->m_inputTags["muonTag"];
  if (muonTag.label() != "none") m_muToken = collector.consumes<reco::MuonCollection>(muonTag);

  edm::InputTag & primaryVerticesTag = m_config->m_inputTags["primaryVerticesTag"];
  if (primaryVerticesTag.label() != "none") m_primaryVerticesToken = collector.consumes<std::vector<reco::Vertex>>(primaryVerticesTag);

  edm::InputTag & gemSegmentTag = m_config->m_inputTags["gemSegmentTag"];
  if (gemSegmentTag.label() != "none") m_gemSegmentToken = collector.consumes<GEMSegmentCollection>(gemSegmentTag);
  
  edm::InputTag & cscSegmentTag = m_config->m_inputTags["cscSegmentTag"];
  if(cscSegmentTag.label() != "none") m_cscSegmentToken = collector.consumes<CSCSegmentCollection>(cscSegmentTag);

//  edm::InputTag & trigResultsTag = m_config->m_inputTags["trigResultsTag"];
//  if (trigResultsTag.label() != "none") m_trigResultsToken = collector.consumes<edm::TriggerResults>(trigResultsTag);

//  edm::InputTag & trigEventTag = m_config->m_inputTags["trigEventTag"];
//  if (trigEventTag.label() != "none") m_trigEventToken = collector.consumes<trigger::TriggerEvent>(trigEventTag);

  edm::InputTag & gemRecHitTag = m_config->m_inputTags["gemRecHitTag"];
  if (gemRecHitTag.label() != "none") m_gemRecHitToken = collector.consumes<GEMRecHitCollection>(gemRecHitTag);
 
//  edm::InputTag & trigTag = m_config->m_inputTags["trigTag"];
//  if (trigTag.label() != "none") m_trigToken = collector.consumes<edm::TriggerResults>(trigTag);

}

MuNtupleGEMMuonFiller::~MuNtupleGEMMuonFiller() 
{ 

}

void MuNtupleGEMMuonFiller::initialize()
{

  m_tree->Branch((m_label + "_nMuons").c_str(), &m_nMuons);
  
  m_tree->Branch((m_label + "_pt").c_str(), &m_pt);
  m_tree->Branch((m_label + "_phi").c_str(), &m_phi);
  m_tree->Branch((m_label + "_eta").c_str(), &m_eta);
  m_tree->Branch((m_label + "_charge").c_str(), &m_charge);

  m_tree->Branch((m_label + "_isGlobal").c_str(), &m_isGlobal);
  m_tree->Branch((m_label + "_isStandalone").c_str(), &m_isStandalone);
  m_tree->Branch((m_label + "_isTracker").c_str(), &m_isTracker);
  m_tree->Branch((m_label + "_isGEM").c_str(), &m_isGEM);
  m_tree->Branch((m_label + "_isCSC").c_str(), &m_isCSC);
  m_tree->Branch((m_label + "_isME11").c_str(), &m_isME11);
  m_tree->Branch((m_label + "_isME21").c_str(), &m_isME21);
  
  m_tree->Branch((m_label + "_isLoose").c_str(), &m_isLoose);
  m_tree->Branch((m_label + "_isMedium").c_str(), &m_isMedium);
  m_tree->Branch((m_label + "_isTight").c_str(), &m_isTight);
  
  m_tree->Branch((m_label + "_isPFMuon").c_str(), &m_isPFMuon);
  m_tree->Branch((m_label + "_validFraction").c_str(), &m_validFraction);
  m_tree->Branch((m_label + "_normChi2").c_str(), &m_normChi2);
  m_tree->Branch((m_label + "_chi2LocalPosition").c_str(), &m_chi2LocalPosition);
  m_tree->Branch((m_label + "_trkKink").c_str(), &m_trkKink);
  m_tree->Branch((m_label + "_segCompatibility").c_str(), &m_segCompatibility);
  m_tree->Branch((m_label + "_numValidMuonHits").c_str(), &m_numValidMuonHits);
  m_tree->Branch((m_label + "_numMatchedStation").c_str(), &m_numMatchedStation);
  m_tree->Branch((m_label + "_dxy").c_str(), &m_dxy);
  m_tree->Branch((m_label + "_dz").c_str(), &m_dz);
  m_tree->Branch((m_label + "_numValidPixelHits").c_str(), &m_numValidPixelHits);
  m_tree->Branch((m_label + "_numTrackerLayers").c_str(), &m_numTrackerLayers);
  
  m_tree->Branch((m_label + "_GlobalTrackHits").c_str(), &m_GlobalTrackHits);
  m_tree->Branch((m_label + "_OuterTrackHits").c_str(), &m_OuterTrackHits);

  m_tree->Branch((m_label + "_propagated_isME11").c_str(), &m_propagated_isME11);
  m_tree->Branch((m_label + "_propagated_isME21").c_str(), &m_propagated_isME21);

  m_tree->Branch((m_label + "_propagated_TrackNormChi2").c_str(), &m_propagated_TrackNormChi2);

  m_tree->Branch((m_label + "_propagated_numberOfValidPixelHits").c_str(), &m_propagated_numberOfValidPixelHits);
  m_tree->Branch((m_label + "_propagated_innerTracker_ValidFraction").c_str(), &m_propagated_innerTracker_ValidFraction);
  m_tree->Branch((m_label + "_propagated_numberOfValidTrackerHits").c_str(), &m_propagated_numberOfValidTrackerHits);
  
  m_tree->Branch((m_label + "_path_length").c_str(), &m_path_length);

  m_tree->Branch((m_label + "_isinsideout").c_str(), &m_isinsideout);
  m_tree->Branch((m_label + "_isincoming").c_str(), &m_isincoming);

  m_tree->Branch((m_label + "_propagated_region").c_str(), &m_propagated_region);
  m_tree->Branch((m_label + "_propagated_station").c_str(), &m_propagated_station);
  m_tree->Branch((m_label + "_propagated_layer").c_str(), &m_propagated_layer);
  m_tree->Branch((m_label + "_propagated_chamber").c_str(), &m_propagated_chamber);
  m_tree->Branch((m_label + "_propagated_etaP").c_str(), &m_propagated_etaP);

  m_tree->Branch((m_label + "_propagated_pt").c_str(), &m_propagated_pt);
  m_tree->Branch((m_label + "_propagated_isLoose").c_str(), &m_propagated_isLoose);
  m_tree->Branch((m_label + "_propagated_isMedium").c_str(), &m_propagated_isMedium);
  m_tree->Branch((m_label + "_propagated_isTight").c_str(), &m_propagated_isTight);
  m_tree->Branch((m_label + "_propagated_phi").c_str(), &m_propagated_phi);
  m_tree->Branch((m_label + "_propagated_eta").c_str(), &m_propagated_eta);
  m_tree->Branch((m_label + "_propagated_charge").c_str(), &m_propagated_charge);
  m_tree->Branch((m_label + "_propagated_isGlobal").c_str(), &m_propagated_isGlobal);
  m_tree->Branch((m_label + "_propagated_isStandalone").c_str(), &m_propagated_isStandalone);
  m_tree->Branch((m_label + "_propagated_isTracker").c_str(), &m_propagated_isTracker);

  m_tree->Branch((m_label + "_propagatedLoc_x").c_str(), &m_propagatedLoc_x);
  m_tree->Branch((m_label + "_propagatedLoc_y").c_str(), &m_propagatedLoc_y);
  m_tree->Branch((m_label + "_propagatedLoc_z").c_str(), &m_propagatedLoc_z);
  m_tree->Branch((m_label + "_propagatedLoc_r").c_str(), &m_propagatedLoc_r);
  m_tree->Branch((m_label + "_propagated_isGEM").c_str(), &m_propagated_isGEM);
  m_tree->Branch((m_label + "_propagatedLoc_phi").c_str(), &m_propagatedLoc_phi);
  m_tree->Branch((m_label + "_propagatedLoc_errX").c_str(), &m_propagatedLoc_errX);
  m_tree->Branch((m_label + "_propagatedLoc_errY").c_str(), &m_propagatedLoc_errY);
  m_tree->Branch((m_label + "_propagatedLoc_dirX").c_str(), &m_propagatedLoc_dirX);
  m_tree->Branch((m_label + "_propagatedLoc_dirY").c_str(), &m_propagatedLoc_dirY);
  m_tree->Branch((m_label + "_propagatedLoc_dirZ").c_str(), &m_propagatedLoc_dirZ);

  m_tree->Branch((m_label + "_propagated_isPFMuon").c_str(), &m_propagated_isPFMuon);
  m_tree->Branch((m_label + "_propagated_validFraction").c_str(), &m_propagated_validFraction);
  m_tree->Branch((m_label + "_propagated_normChi2").c_str(), &m_propagated_normChi2);
  m_tree->Branch((m_label + "_propagated_chi2LocalPosition").c_str(), &m_propagated_chi2LocalPosition);
  m_tree->Branch((m_label + "_propagated_trkKink").c_str(), &m_propagated_trkKink);
  m_tree->Branch((m_label + "_propagated_segCompatibility").c_str(), &m_propagated_segCompatibility);
  m_tree->Branch((m_label + "_propagated_numValidMuonHits").c_str(), &m_propagated_numValidMuonHits);
  m_tree->Branch((m_label + "_propagated_numMatchedStation").c_str(), &m_propagated_numMatchedStation);
  m_tree->Branch((m_label + "_propagated_dxy").c_str(), &m_propagated_dxy);
  m_tree->Branch((m_label + "_propagated_dz").c_str(), &m_propagated_dz);
  m_tree->Branch((m_label + "_propagated_numValidPixelHits").c_str(), &m_propagated_numValidPixelHits);
  m_tree->Branch((m_label + "_propagated_numTrackerLayers").c_str(), &m_propagated_numTrackerLayers);

  m_tree->Branch((m_label + "_propagatedGlb_x").c_str(), &m_propagatedGlb_x);
  m_tree->Branch((m_label + "_propagatedGlb_y").c_str(), &m_propagatedGlb_y);
  m_tree->Branch((m_label + "_propagatedGlb_z").c_str(), &m_propagatedGlb_z);
  m_tree->Branch((m_label + "_propagatedGlb_r").c_str(), &m_propagatedGlb_r);
  m_tree->Branch((m_label + "_propagatedGlb_phi").c_str(), &m_propagatedGlb_phi);
  m_tree->Branch((m_label + "_propagatedGlb_errX").c_str(), &m_propagatedGlb_errX);
  m_tree->Branch((m_label + "_propagatedGlb_errY").c_str(), &m_propagatedGlb_errY);
  m_tree->Branch((m_label + "_propagatedGlb_errR").c_str(), &m_propagatedGlb_rerr);
  m_tree->Branch((m_label + "_propagatedGlb_errPhi").c_str(), &m_propagatedGlb_phierr);

  m_tree->Branch((m_label + "_propagated_EtaPartition_centerX").c_str(), &m_propagated_EtaPartition_centerX);
  m_tree->Branch((m_label + "_propagated_EtaPartition_centerY").c_str(), &m_propagated_EtaPartition_centerY);
  m_tree->Branch((m_label + "_propagated_EtaPartition_rMax").c_str(), &m_propagated_EtaPartition_rMax);
  m_tree->Branch((m_label + "_propagated_EtaPartition_rMin").c_str(), &m_propagated_EtaPartition_rMin);
  m_tree->Branch((m_label + "_propagated_EtaPartition_phiMax").c_str(), &m_propagated_EtaPartition_phiMax);
  m_tree->Branch((m_label + "_propagated_EtaPartition_phiMin").c_str(), &m_propagated_EtaPartition_phiMin);
  
  m_tree->Branch((m_label + "_propagated_EtaPartition_xMax").c_str(), &m_propagated_EtaPartition_xMax);
  m_tree->Branch((m_label + "_propagated_EtaPartition_xMin").c_str(), &m_propagated_EtaPartition_xMin);
  m_tree->Branch((m_label + "_propagated_EtaPartition_yMax").c_str(), &m_propagated_EtaPartition_yMax);
  m_tree->Branch((m_label + "_propagated_EtaPartition_yMin").c_str(), &m_propagated_EtaPartition_yMin);

  m_tree->Branch((m_label + "_propagated_nME1hits").c_str(), &m_propagated_nME1hits);
  m_tree->Branch((m_label + "_propagated_nME2hits").c_str(), &m_propagated_nME2hits);
  m_tree->Branch((m_label + "_propagated_nME3hits").c_str(), &m_propagated_nME3hits);
  m_tree->Branch((m_label + "_propagated_nME4hits").c_str(), &m_propagated_nME4hits);



  m_tree->Branch((m_label + "_propagated_Innermost_x").c_str(), &m_propagated_Innermost_x);
  m_tree->Branch((m_label + "_propagated_Innermost_y").c_str(), &m_propagated_Innermost_y);
  m_tree->Branch((m_label + "_propagated_Innermost_z").c_str(), &m_propagated_Innermost_z);
  m_tree->Branch((m_label + "_propagated_Outermost_x").c_str(), &m_propagated_Outermost_x);
  m_tree->Branch((m_label + "_propagated_Outermost_y").c_str(), &m_propagated_Outermost_y);
  m_tree->Branch((m_label + "_propagated_Outermost_z").c_str(), &m_propagated_Outermost_z);

//  m_tree->Branch((m_label + "_triggerMap").c_str(), &m_triggerMap, (m_label + "_triggerMap").c_str());  

}

void MuNtupleGEMMuonFiller::clear()
{

  m_nMuons = 0;

  m_pt.clear();
  m_phi.clear();
  m_eta.clear();
  m_charge.clear();

  m_isGlobal.clear();
  m_isStandalone.clear();
  m_isTracker.clear();
  m_isGEM.clear();
  m_isCSC.clear();
  m_isME11.clear();
  m_isME21.clear();

m_GlobalTrackHits.clear();
m_OuterTrackHits.clear();

  m_propagated_TrackNormChi2.clear();

  m_propagated_numberOfValidPixelHits.clear();
  m_propagated_innerTracker_ValidFraction.clear();
  m_propagated_numberOfValidTrackerHits.clear();

  m_isLoose.clear();
  m_isMedium.clear();
  m_isTight.clear();

  m_isPFMuon.clear();
  m_validFraction.clear();
  m_normChi2.clear();
  m_chi2LocalPosition.clear();
  m_trkKink.clear();
  m_segCompatibility.clear();
  m_numValidMuonHits.clear();
  m_numMatchedStation.clear();
  m_dxy.clear();
  m_dz.clear();
  m_numValidPixelHits.clear();
  m_numTrackerLayers.clear();

 
  m_path_length = 0;
  
  m_isinsideout.clear();
  m_isincoming.clear();

  m_propagated_region.clear();
  m_propagated_station.clear();
  m_propagated_layer.clear();
  m_propagated_chamber.clear();
  m_propagated_etaP.clear();
  m_propagated_isME11.clear();
  m_propagated_isME21.clear();
  
  m_propagated_isLoose.clear();
  m_propagated_isMedium.clear();
  m_propagated_isTight.clear();
  m_propagated_pt.clear();
  m_propagated_phi.clear();
  m_propagated_eta.clear();
  m_propagated_charge.clear();
  m_propagated_isGlobal.clear();
  m_propagated_isStandalone.clear();
  m_propagated_isTracker.clear();


  m_propagated_isPFMuon.clear();
  m_propagated_validFraction.clear();
  m_propagated_normChi2.clear();
  m_propagated_chi2LocalPosition.clear();
  m_propagated_trkKink.clear();
  m_propagated_segCompatibility.clear();
  m_propagated_numValidMuonHits.clear();
  m_propagated_numMatchedStation.clear();
  m_propagated_dxy.clear();
  m_propagated_dz.clear();
  m_propagated_numValidPixelHits.clear();
  m_propagated_numTrackerLayers.clear();

  m_propagatedLoc_x.clear();
  m_propagatedLoc_y.clear();
  m_propagatedLoc_z.clear();
  m_propagatedLoc_r.clear();
  m_propagated_isGEM.clear();
  m_propagatedLoc_phi.clear();
  m_propagatedLoc_errX.clear();
  m_propagatedLoc_errY.clear();
  m_propagatedLoc_dirX.clear();
  m_propagatedLoc_dirY.clear();
  m_propagatedLoc_dirZ.clear();

  m_propagatedGlb_errX.clear();
  m_propagatedGlb_errY.clear();
  m_propagatedGlb_rerr.clear();
  m_propagatedGlb_phierr.clear();
  m_propagatedGlb_x.clear();
  m_propagatedGlb_y.clear();
  m_propagatedGlb_z.clear();
  m_propagatedGlb_r.clear();
  m_propagatedGlb_phi.clear();

  m_propagated_nME1hits.clear();
  m_propagated_nME2hits.clear();
  m_propagated_nME3hits.clear();
  m_propagated_nME4hits.clear();


  m_propagated_Innermost_x.clear();
  m_propagated_Innermost_y.clear();
  m_propagated_Innermost_z.clear();

  m_propagated_Outermost_x.clear();
  m_propagated_Outermost_y.clear();
  m_propagated_Outermost_z.clear();

  m_propagated_EtaPartition_centerX.clear();
  m_propagated_EtaPartition_centerY.clear();
  m_propagated_EtaPartition_rMax.clear();
  m_propagated_EtaPartition_rMin.clear();
  m_propagated_EtaPartition_phiMax.clear();
  m_propagated_EtaPartition_phiMin.clear();
  
  m_propagated_EtaPartition_xMax.clear();
  m_propagated_EtaPartition_xMin.clear();
  m_propagated_EtaPartition_yMax.clear();
  m_propagated_EtaPartition_yMin.clear();

//  m_triggerMap.clear();
      
}

void MuNtupleGEMMuonFiller::fill(const edm::Event & ev)
{

  clear();

  auto muons = conditionalGet<reco::MuonCollection>(ev, m_muToken, "MuonCollection");
  auto gem_segments = conditionalGet<GEMSegmentCollection>(ev,m_gemSegmentToken, "GEMSegmentCollection");
  auto csc_segments = conditionalGet<CSCSegmentCollection>(ev,m_cscSegmentToken, "CSCSegmentCollection" );
  auto vtxs = conditionalGet<std::vector<reco::Vertex>>(ev, m_primaryVerticesToken, "std::vector<reco::Vertex>");

  //if (vtxs->empty()) return; // skip the event if no PV found
  //const reco::Vertex &pv = vtxs->front();

  bool isCSC = false;
  bool isME11 = false;
  bool isME21 = false;
  
  edm::Handle<GEMRecHitCollection> rechit_collection;
  ev.getByToken(m_gemRecHitToken, rechit_collection);

 
  edm::ESHandle<Propagator>&& propagator_any = m_config->m_muonSP->propagator("SteppingHelixPropagatorAny");
  if (not propagator_any.isValid()) {
    std::cout<< "Any Propagator is invalid" << std::endl;
    return;
  }

  edm::ESHandle<Propagator>&& propagator_along = m_config->m_muonSP->propagator("SteppingHelixPropagatorAlong");
  if (not propagator_along.isValid()) {
    std::cout<< "Along Propagator is invalid" << std::endl;
    return;
  }

  edm::ESHandle<Propagator>&& propagator_opposite = m_config->m_muonSP->propagator("SteppingHelixPropagatorOpposite");
  if (not propagator_opposite.isValid()) {
    std::cout<< "Opposite Propagator is invalid" << std::endl;
    return;
  }

    
  edm::ESHandle<GEMGeometry> gem = m_config->m_gemGeometry;
  if (not gem.isValid()) {
    std::cout << "GEMGeometry is invalid" << std::endl;
    return;
  }

  edm::ESHandle<CSCGeometry> csc = m_config->m_cscGeometry;
  if (not csc.isValid()) {
    std::cout << "CSCGeometry is invalid" << std::endl;
    return;
  }
    
  edm::ESHandle<TransientTrackBuilder> transient_track_builder = m_config->m_transientTrackBuilder;
  if (not transient_track_builder.isValid()) {
    std::cout << "TransientTrack is invalid" << std::endl;
    return;
  }

/*  auto triggerResults = conditionalGet<edm::TriggerResults>(ev, m_trigToken,"edm::TriggerResults");

  const edm::TriggerNames &names = ev.triggerNames(*triggerResults);
    size_t j;
    for (j=0; j < triggerResults->size(); j++) {
       if (triggerResults->accept(j)) {
           m_triggerMap[names.triggerName(j)] = 1;
       }
       else
       {
           m_triggerMap[names.triggerName(j)] = 0;
       }
     }
*/

  if (muons.isValid()) // && csc_segments.isValid() && vtxs.isValid()) 
    {
      //loop on recoMuons  
      for (const auto & muon : (*muons))
	{

          //if (!(muon.passed(reco::Muon::CutBasedIdTight) && muon.isGlobalMuon()))
          //{ continue;}

	  m_pt.push_back(muon.pt());
	  m_eta.push_back(muon.eta());
	  m_phi.push_back(muon.phi());
	  m_charge.push_back(muon.charge());

	  m_isGlobal.push_back(muon.isGlobalMuon());
	  m_isStandalone.push_back(muon.isStandAloneMuon());
	  m_isTracker.push_back(muon.isTrackerMuon());
	  m_isGEM.push_back(muon.isGEMMuon());

	  m_isLoose.push_back(muon.passed(reco::Muon::CutBasedIdLoose));
	  m_isMedium.push_back(muon.passed(reco::Muon::CutBasedIdMedium));
	  m_isTight.push_back(muon.passed(reco::Muon::CutBasedIdTight));
    
          // Adding ID variables Sumit
	  m_isPFMuon.push_back(muon.isPFMuon());
          bool validFractionThreshold=((272728 >= ev.run() && ev.run() >= 278808)? 0.49 : 0.8);
          m_validFraction.push_back(int(validFractionThreshold));
          
          if(!muon.globalTrack().isNull()){
          m_normChi2.push_back(muon.globalTrack()->normalizedChi2());
          m_numValidMuonHits.push_back(muon.globalTrack()->hitPattern().numberOfValidMuonHits());
          }
          m_chi2LocalPosition.push_back(muon.combinedQuality().chi2LocalPosition);
          m_trkKink.push_back(muon.combinedQuality().trkKink);
          m_segCompatibility.push_back(muon::segmentCompatibility(muon));
          m_numMatchedStation.push_back(muon.numberOfMatchedStations());
          if (! vtxs->empty())
          {
          const reco::Vertex &pv = vtxs->front();
          m_dxy.push_back(fabs(muon.muonBestTrack()->dxy(pv.position())));
          m_dz.push_back(fabs(muon.muonBestTrack()->dz(pv.position())));
          }
          if (!muon.innerTrack().isNull()){
          m_numValidPixelHits.push_back(muon.innerTrack()->hitPattern().numberOfValidPixelHits());
          m_numTrackerLayers.push_back(muon.innerTrack()->hitPattern().trackerLayersWithMeasurement());
          }

	  m_nMuons++;
      
      isCSC = false;
      isME11 = false;
      isME21 = false;

          if (muon.isGlobalMuon()){
              m_GlobalTrackHits.push_back(muon.globalTrack().get()->recHitsSize());
              //m_GlobalTrackCSCSegments.push_back(muon.num)
          }

          //if (muon.isStandAloneMuon()) m_OuterTrackHits.push_back(muon.outerTrack().get()->recHitsSize());

          if (!(muon.isGlobalMuon() and muon.isStandAloneMuon() and muon.passed(reco::Muon::CutBasedIdTight))) continue;

	  //if(!muon.globalTrack().isNull())  //GLB muon
	  //if(!muon.innerTrack().isNull() && muon.innerTrack().isAvailable())   //tracker muon	  
	  if(!muon.outerTrack().isNull())   //STA muon

	    {
	      

	  //    const reco::Track* track = muon.globalTrack().get();   //GLB muon
          //const reco::Track* track = muon.innerTrack().get();    //tracker muon
          const reco::Track* track = muon.outerTrack().get();    //STA muon
	      
	      if (track == nullptr) {
		std::cout << "failed to get muon track" << std::endl;
                continue;
              }

	      //const reco::TrackRef trackRef = muon.globalTrack();       //GLB muon              
	      //const reco::TrackRef innerTrackRef = muon.innerTrack();   //tracker muon
	      const reco::TrackRef outerTrackRef = muon.outerTrack();   //STA muon 
              //if(innerTrackRef.isNull()){
              //    std::cout<<"failed to get inner muon track reference."<<std::endl;
              //   continue;
              //} 

	    

	      float p2_in = track->innerMomentum().mag2();
	      float p2_out = track->outerMomentum().mag2();
	      float pos_out = track->outerPosition().mag2();
	      float pos_in = track->innerPosition().mag2();

	      bool is_insideout = pos_in > pos_out;

	      if(is_insideout)
		{
		  std::swap(pos_in, pos_out);
		  std::swap(p2_in, p2_out);
		}
	            
	      bool is_incoming = p2_out > p2_in;

	      const reco::TransientTrack&& transient_track = transient_track_builder->build(track);
	      if (not transient_track.isValid()) 
		{
		  std::cout<<"failed to build TransientTrack" << std::endl;
		  continue;
		}

	     	      
	      const auto&& start_state = is_insideout ? transient_track.outermostMeasurementState() : transient_track.innermostMeasurementState();
	      auto& propagator = is_incoming ? propagator_along : propagator_opposite;
	     
	      //auto recHitMu = trackRef->recHitsBegin();           //GLB muon
	      //auto recHitMuEnd = trackRef->recHitsEnd();           //GLB muon
	      //auto recHitMu = innerTrackRef->recHitsBegin();      //tracker muon
	      auto recHitMuEnd = outerTrackRef ->recHitsEnd();      //STA muon

	     // auto recHitMuEnd = innerTrackRef->recHitsEnd();     //tracker muon
	      auto recHitMu = outerTrackRef->recHitsBegin();      //STA muon
	      // auto recHitMuEnd = innerTrackerRef->recHitsEnd();     //STA muon

          const reco::HitPattern& htp = transient_track.hitPattern();

	      for(; recHitMu != recHitMuEnd; ++recHitMu)
              {
                  DetId detId = (*recHitMu)->geographicalId();
                  if(detId.det() == DetId::Muon && detId.subdetId() == MuonSubdetId::GEM)
                      {
                          // std::cout<<"InnermostZ = " << transient_track.innermostMeasurementState().globalPosition().z()<<std::endl;
                          // std::cout<<"GEM found in STA track"<<std::endl;
                      }
                  if(detId.det() == DetId::Muon && detId.subdetId() == MuonSubdetId::CSC)
                      {
                          isCSC = true;
                          const CSCDetId csc_id{detId};
                          // ME11 chambers are composed by 2 subchambers: ME11a, ME11b. In CMSSW they are referred as Stat. 1 Ring 1, Stat. 1 Ring. 4 respectively
                          if(csc_id.station() == 1 && ((csc_id.ring() == 1) || (csc_id.ring() == 4)) ) 
                              {
                                  isME11 = true;
                              }
                          if(csc_id.station() == 2 && csc_id.ring() == 1)
                              {
                                  isME21 = true;
                              }

                      }
              } //loop on recHits to find if muon has MEX1 hits
          
                            
	      m_isCSC.push_back(isCSC);
	      m_isME11.push_back(isME11);
	      m_isME21.push_back(isME21);
	      
          //if at least one CSC hit is found, perform propagation 
	      if(isCSC)
              { 
                  //std::cout<<"Track HITS"<<std::endl;
                  //htp.print(reco::HitPattern::TRACK_HITS);

                  // CSC Hits
                  int nME1_hits = 0;
                  int nME2_hits = 0;
                  int nME3_hits = 0;
                  int nME4_hits = 0;

                  for (int i = 0; i < htp.numberOfAllHits(htp.TRACK_HITS); i++) {
                      uint32_t hit = htp.getHitPattern(htp.TRACK_HITS, i);
                      int substructure = htp.getSubStructure(hit);
                      int hittype = htp.getHitType(hit);

                      
                      if ( substructure == 2 && hittype == 0) // CSC Hits
                          {
                              int CSC_station = htp.getMuonStation(hit);
                              
                              switch(CSC_station) {
                              case 1 :
                                  nME1_hits++;
                                  break;
                              case 2 :
                                  nME2_hits++;
                                  break;
                              case 3 :
                                  nME3_hits++;
                                  break;
                              case 4 :
                                  nME4_hits++;
                                  break;
                              default: 
                                  std::cout<<"Invalid station " <<std::endl;
                              }
                              
                          }
                  }
                      

                  for (const GEMRegion* gem_region : gem->regions())
                      {
                          bool is_opposite_region = muon.eta() * gem_region->region() < 0;
                          if (is_incoming xor is_opposite_region) continue;
                          
                          for (const GEMStation* station : gem_region->stations())
                              {//if (station->station()!=1) continue; // Skipping GE21 station
                                  for (const GEMSuperChamber* super_chamber : station->superChambers())
                                      {
                                          for (const GEMChamber* chamber : super_chamber->chambers())
                                              {
                                                  for (const GEMEtaPartition* eta_partition : chamber->etaPartitions())
                                                      {
                                                          const BoundPlane& bound_plane = eta_partition->surface();

                                                          // PROPAGATION ON ETAP SURFACE
                                                          // The Z of the dest_state is fixed one the boundplane. x,y are actually evaluated by the propagator at that Z
                                                          const auto& dest_state = propagator_any->propagate(start_state,bound_plane);
                                                          //END PROPAGATION ON ETAP SURFACE

                                                          // // PROPAGATION IN THE DRIFT GAP
                                                          // BoundPlane& etaPSur_translated_to_drift = const_cast<BoundPlane&>(bound_plane);

                                                          // int ch = eta_partition->id().chamber();
                                                          // int re = eta_partition->id().region();
                                                          // double displacement = 0;
                                                              
                                                          // if (ch % 2 == 0)
                                                          //     {
                                                          //         displacement = -0.55*re;
                                                          //     }
                                                          // if (ch % 2 == 1)
                                                          //     {
                                                          //         displacement = 0.55*re;
                                                          //     }
                                                          
                                                          // etaPSur_translated_to_drift.move(GlobalVector(0.,0.,displacement));
                                                          // const auto& dest_state = propagator_any->propagate(start_state,etaPSur_translated_to_drift);
                                                          // etaPSur_translated_to_drift.move(GlobalVector(0.,0.,-displacement));
                                                          // // END PROPAGATION IN THE DRIFT GAP


                                                          if (not dest_state.isValid())
                                                              {
                                                                  std::cout << "failed to propagate" << std::endl;
                                                                  continue;
                                                              }
                                                        //std::cout<<"(x,y): ("<<cartesian.x()<<","<<cartesian.y()<<")"<<std::endl;

                                                          const GlobalPoint&& dest_global_pos = dest_state.globalPosition();
                                                          const LocalPoint&& local_point = eta_partition->toLocal(dest_global_pos);
                                                          const LocalPoint local_point_2d(local_point.x(), local_point.y(), 0.0f);

                                                          if (eta_partition->surface().bounds().inside(local_point_2d)) 
                                                              {

                                                                  const GEMDetId&& gem_id = eta_partition->id();
                                                                  Geom::Polar2Cartesian<float> cartesian_min(bound_plane.rSpan().first,bound_plane.phiSpan().first);
                                                                  Geom::Polar2Cartesian<float> cartesian_max(bound_plane.rSpan().second,bound_plane.phiSpan().second);

                                                                  //// PROPAGATED HIT ERROR EVALUATION
                                                                  // X,Y FROM QC8 Code
                                                                  double xx = dest_state.curvilinearError().matrix()(3,3);
                                                                  double yy = dest_state.curvilinearError().matrix()(4,4);
                                                                  double xy = dest_state.curvilinearError().matrix()(4,3);
                                                                  double dest_glob_error_x = sqrt(0.5*(xx+yy-sqrt((xx-yy)*(xx-yy)+4*xy*xy)));
                                                                  double dest_glob_error_y = sqrt(0.5*(xx+yy+sqrt((xx-yy)*(xx-yy)+4*xy*xy)));
                                                                  // R,Phi From https://github.com/cms-sw/cmssw/blob/f77e926a1e98b3d9f1144caf3b83cb3667e23786/DQMOffline/Muon/src/GEMEfficiencyAnalyzer.cc
                                                                  const LocalPoint&& dest_local_pos = chamber->toLocal(dest_global_pos);
                                                                  const LocalError&& dest_local_err = dest_state.localError().positionError();
                                                                  const GlobalError& dest_global_err = ErrorFrameTransformer().transform(dest_local_err, eta_partition->surface());
                                                                  const double dest_global_r_err = std::sqrt(dest_global_err.rerr(dest_global_pos));
                                                                  const double dest_global_phi_err = std::sqrt(dest_global_err.phierr(dest_global_pos));
                                                                  
                                                                  m_propagated_isME11.push_back(isME11);
                                                                  m_propagated_isME21.push_back(isME21);

                                                                  m_propagated_nME1hits.push_back(nME1_hits);
                                                                  m_propagated_nME2hits.push_back(nME2_hits);
                                                                  m_propagated_nME3hits.push_back(nME3_hits);
                                                                  m_propagated_nME4hits.push_back(nME4_hits);
                                                                  
                                                                  m_propagated_Innermost_x.push_back(transient_track.innermostMeasurementState().globalPosition().x());
                                                                  m_propagated_Innermost_y.push_back(transient_track.innermostMeasurementState().globalPosition().y());
                                                                  m_propagated_Innermost_z.push_back(transient_track.innermostMeasurementState().globalPosition().z());
                                                                  m_propagated_Outermost_x.push_back(transient_track.outermostMeasurementState().globalPosition().x());
                                                                  m_propagated_Outermost_y.push_back(transient_track.outermostMeasurementState().globalPosition().y());
                                                                  m_propagated_Outermost_z.push_back(transient_track.outermostMeasurementState().globalPosition().z());
                                                                  
                                                                  m_propagated_EtaPartition_centerX.push_back(eta_partition->position().x());
                                                                  m_propagated_EtaPartition_centerY.push_back(eta_partition->position().y());
                                                                  m_propagated_EtaPartition_rMin.push_back(eta_partition->surface().rSpan().first);
                                                                  m_propagated_EtaPartition_rMax.push_back(eta_partition->surface().rSpan().second);
                                                                  m_propagated_EtaPartition_phiMin.push_back(eta_partition->surface().phiSpan().first);
                                                                  m_propagated_EtaPartition_phiMax.push_back(eta_partition->surface().phiSpan().second);
                                                                  
                                                                  m_propagated_EtaPartition_xMin.push_back(cartesian_min.x());
                                                                  m_propagated_EtaPartition_xMax.push_back(cartesian_max.x());
                                                                  m_propagated_EtaPartition_yMin.push_back(cartesian_min.y());
                                                                  m_propagated_EtaPartition_yMax.push_back(cartesian_max.y());
                                                                  
                                                                  m_propagatedGlb_x.push_back(dest_global_pos.x());
                                                                  m_propagatedGlb_y.push_back(dest_global_pos.y());
                                                                  m_propagatedGlb_z.push_back(dest_global_pos.z());
                                                                  m_propagatedGlb_r.push_back(dest_global_pos.perp());
                                                                  m_propagatedGlb_phi.push_back(dest_global_pos.phi());
                                                                  
                                                                  m_propagated_pt.push_back(muon.pt());
                                                                  m_propagated_isLoose.push_back(muon.passed(reco::Muon::CutBasedIdLoose));
                                                                  m_propagated_isMedium.push_back(muon.passed(reco::Muon::CutBasedIdMedium));
                                                                  m_propagated_isTight.push_back(muon.passed(reco::Muon::CutBasedIdTight));
	                                                          m_propagated_isGlobal.push_back(muon.isGlobalMuon());
	                                                          m_propagated_isStandalone.push_back(muon.isStandAloneMuon());
	                                                          m_propagated_isTracker.push_back(muon.isTrackerMuon());
	                                                          m_propagated_isPFMuon.push_back(muon.isPFMuon());
	                                                          m_propagated_validFraction.push_back(int(validFractionThreshold));
	                                                          if (!muon.globalTrack().isNull()){
                                                                      m_propagated_normChi2.push_back(muon.globalTrack()->normalizedChi2());
                                                                      m_propagated_numValidMuonHits.push_back(muon.globalTrack()->hitPattern().numberOfValidMuonHits());
                                                                      }
	                                                          m_propagated_chi2LocalPosition.push_back(muon.combinedQuality().chi2LocalPosition);
	                                                          m_propagated_trkKink.push_back(muon.combinedQuality().trkKink);
                                                                  
	                                                          m_propagated_segCompatibility.push_back(muon::segmentCompatibility(muon));
	                                                          m_propagated_numMatchedStation.push_back(muon.numberOfMatchedStations());
                                                                  if(!vtxs->empty())
                                                                  {
                                                                      const reco::Vertex &pv = vtxs->front();
	                                                          m_propagated_dxy.push_back(fabs(muon.muonBestTrack()->dxy(pv.position())));
	                                                          m_propagated_dz.push_back(fabs(muon.muonBestTrack()->dz(pv.position())));
                                                                  }
                                                                  
                                                                  
                                                                  m_propagated_phi.push_back(muon.phi());
                                                                  m_propagated_eta.push_back(muon.eta());
                                                                  m_propagated_charge.push_back(muon.charge());
                                                                  m_propagated_TrackNormChi2.push_back(transient_track.normalizedChi2());
                                                                  
                                                                  m_propagatedLoc_x.push_back(dest_local_pos.x());
                                                                  m_propagatedLoc_phi.push_back(dest_local_pos.phi());
                                                                  m_propagatedLoc_r.push_back(dest_local_pos.perp());
                                                                  m_propagatedLoc_y.push_back(dest_local_pos.y());
                                                                  m_propagatedLoc_dirX.push_back(dest_state.localDirection().x());
                                                                  m_propagatedLoc_dirY.push_back(dest_state.localDirection().y());
                                                                  m_propagatedLoc_dirZ.push_back(dest_state.localDirection().z());
                                                                  
                                                                  m_propagatedLoc_errX.push_back(dest_local_err.xx());
                                                                  m_propagatedLoc_errY.push_back(dest_local_err.yy());
                                                                  m_propagated_isGEM.push_back(muon.isGEMMuon());

                                                                  m_propagatedGlb_errX.push_back(dest_glob_error_x);
                                                                  m_propagatedGlb_errY.push_back(dest_glob_error_y);
                                                                  m_propagatedGlb_rerr.push_back(dest_global_r_err);
                                                                  m_propagatedGlb_phierr.push_back(dest_global_phi_err);
                                                                  
                                                                  m_propagated_region.push_back(gem_id.region());
                                                                  m_propagated_station.push_back(gem_id.station());
                                                                  m_propagated_layer.push_back(gem_id.layer());
                                                                  m_propagated_chamber.push_back(gem_id.chamber());
                                                                  m_propagated_etaP.push_back(gem_id.roll());
                                                                  
                                                                  m_isinsideout.push_back(is_insideout);
                                                                  m_isincoming.push_back(is_incoming);

                                                                  if(!muon.innerTrack().isNull())
                                                                      {
                                                                          m_propagated_numberOfValidPixelHits.push_back(muon.innerTrack()->hitPattern().numberOfValidPixelHits());
                                                                          m_propagated_innerTracker_ValidFraction.push_back(muon.innerTrack()->validFraction());
                                                                          m_propagated_numTrackerLayers.push_back(muon.innerTrack()->hitPattern().trackerLayersWithMeasurement());
                                                                          m_propagated_numberOfValidTrackerHits.push_back(muon.innerTrack()->hitPattern().numberOfValidTrackerHits());
                                                                      }

                                                              }// Propagation is inside EtaPartition
                                                      }//Loop over Eta Partition
                                              }//Loop over chambers
                                      }//Loop over SuperChambers
                              }//Loop over stations
                      }//Loop over regions
              }//isCSC therefore perform propagation
	    }//!muon.outerTrack().isNull()
	
	}//loop on reco muons
    }//muons.isValid()
  
  return;
  
}


const GEMEtaPartition* MuNtupleGEMMuonFiller::findEtaPartition(const GEMChamber* chamber, const GlobalPoint& global_point) {

  for (const GEMEtaPartition* eta_partition : chamber->etaPartitions()) {
    const LocalPoint&& local_point = eta_partition->toLocal(global_point);
    const LocalPoint local_point_2d(local_point.x(), local_point.y(), 0.0f);
    if (eta_partition->surface().bounds().inside(local_point_2d)) 
      return eta_partition;
  }

  return nullptr;
}

