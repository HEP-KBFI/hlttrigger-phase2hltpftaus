#ifndef HLTTrigger_Phase2HLTPFTaus_PFTauPairProducer_h
#define HLTTrigger_Phase2HLTPFTaus_PFTauPairProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/TauReco/interface/PFTau.h"                // reco::PFTau
#include "DataFormats/TauReco/interface/PFTauFwd.h"             // reco::PFTauRef, reco::PFTauCollection
#include "DataFormats/TauReco/interface/PFTauDiscriminator.h"   // reco::PFTauDiscriminator

#include "DataFormats/Phase2HLTPFTaus/interface/PFTauPair.h"    // reco::PFTauPair
#include "DataFormats/Phase2HLTPFTaus/interface/PFTauPairFwd.h" // reco::PFTauPairCollection

class PFTauPairProducer : public edm::EDProducer
{
 public:
  explicit PFTauPairProducer(const edm::ParameterSet& cfg);
  ~PFTauPairProducer();
    
 private:
  void produce(edm::Event& evt, const edm::EventSetup& es);

  std::string moduleLabel_;

  edm::InputTag srcPFTaus_;
  edm::EDGetTokenT<reco::PFTauCollection> tokenPFTaus_;
  edm::InputTag srcPFTauSumChargedIso_;
  edm::EDGetTokenT<reco::PFTauDiscriminator> tokenPFTauSumChargedIso_;

  double min_pfTau_pt_;
  double max_pfTau_pt_;
  double min_pfTau_absEta_;
  double max_pfTau_absEta_;
  double min_pfTau_sumChargedIso_;
  double max_pfTau_sumChargedIso_;
  double min_dR_;
  double max_dR_;
  double min_dz_;
  double max_dz_;
};

#endif  
