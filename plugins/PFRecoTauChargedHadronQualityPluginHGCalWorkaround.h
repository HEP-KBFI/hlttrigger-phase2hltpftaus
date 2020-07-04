#ifndef HLTTrigger_Phase2HLTPFTaus_PFRecoTauChargedHadronQualityPluginHGCalWorkaround_h
#define HLTTrigger_Phase2HLTPFTaus_PFRecoTauChargedHadronQualityPluginHGCalWorkaround_h

#include "RecoTauTag/RecoTau/interface/PFRecoTauChargedHadronPlugins.h"
#include "DataFormats/TauReco/interface/PFRecoTauChargedHadron.h"

class PFRecoTauChargedHadronQualityPluginHGCalWorkaround : public reco::tau::PFRecoTauChargedHadronQualityPlugin 
{
 public:
  explicit PFRecoTauChargedHadronQualityPluginHGCalWorkaround(const edm::ParameterSet& cfg);
  ~PFRecoTauChargedHadronQualityPluginHGCalWorkaround() override {}
  
  double operator()(const reco::PFRecoTauChargedHadron& pfTauChargedHadron) const override;
};

#endif
