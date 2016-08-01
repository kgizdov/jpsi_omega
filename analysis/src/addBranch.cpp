// Copyright Konstantin Gizdov 2016 Uni Edinburgh

#include <TFile.h>
#include <TTree.h>
#include <TMath.h>
#include <TVector3.h>
#include <TLorentzVector.h>

#include <string>
#include <iostream>

Double_t getCombinedInvMass(Double_t e1, Double_t px1, Double_t py1, Double_t pz1,
                            Double_t e2, Double_t px2, Double_t py2, Double_t pz2) {
    Double_t invMass;
    TLorentzVector comb_v, v1, v2;
    v1.SetPxPyPzE(px1, py1, pz1, e1);
    v2.SetPxPyPzE(px2, py2, pz2, e2);
    comb_v = v1 + v2;
    invMass = comb_v.M();
    return invMass;
}

Double_t getCombinedInvMass(Double_t e1, TVector3 p1, Double_t e2, TVector3 p2) {
    Double_t invMass;
    TLorentzVector comb_v, v1, v2;
    v1.SetPxPyPzE(p1.X(), p1.Y(), p1.Z(), e1);
    v2.SetPxPyPzE(p2.X(), p2.Y(), p2.Z(), e2);
    comb_v = v1 + v2;
    invMass = comb_v.M();
    return invMass;
}

Double_t getCombinedInvMass3(Double_t p1[], Double_t p2[], Double_t p3[]) {
    Double_t invMass;
    TLorentzVector comb_v, v1, v2, v3;
    v1.SetPxPyPzE(p1[1], p1[2], p1[3], p1[0]);
    v2.SetPxPyPzE(p2[1], p2[2], p2[3], p2[0]);
    v3.SetPxPyPzE(p3[1], p3[2], p3[3], p3[0]);
    comb_v = v1 + v2 + v3;
    invMass = comb_v.M();
    return invMass;
}

void addInvMassBranch2(std::string fileIn, std::string treeName, std::string pName,
                       std::string dName1, std::string dName2, std::string fileOut) {
    std::cout << "Opening file " << fileIn << std::endl;
    TFile *fin = TFile::Open(fileIn.c_str());

    std::cout << "Creating output file " << fileOut << std::endl;
    TFile *fout = TFile::Open(fileOut.c_str(), "RECREATE");
    TTree *intree = reinterpret_cast<TTree*>(fin->Get(treeName.c_str()));
    if (intree == NULL) {
        intree = reinterpret_cast<TTree*>(fin->Get(("Tuple/" + treeName).c_str()));
    }
    fout->cd();

    std::cout << "Cloning tree..." << std::endl;
    TTree *outtree = intree->CloneTree(0);
    Double_t invMass = 0.0, invMassErr, pmass, p1[4], p2[4];

    std::cout << "Creating branch..." << std::endl;
    outtree->Branch((pName+"_InvMass").c_str(), &invMass, (pName+"_InvMass/D").c_str());
    outtree->Branch((pName+"_InvMass_ERR").c_str(), &invMassErr, (pName+"_InvMass_ERR/D").c_str());

    intree->SetBranchAddress((pName + "_M").c_str(), &pmass);
    intree->SetBranchAddress((dName1 + "_PE").c_str(), &p1[0]);
    intree->SetBranchAddress((dName1 + "_PX").c_str(), &p1[1]);
    intree->SetBranchAddress((dName1 + "_PY").c_str(), &p1[2]);
    intree->SetBranchAddress((dName1 + "_PZ").c_str(), &p1[3]);
    intree->SetBranchAddress((dName2 + "_PE").c_str(), &p2[0]);
    intree->SetBranchAddress((dName2 + "_PX").c_str(), &p2[1]);
    intree->SetBranchAddress((dName2 + "_PY").c_str(), &p2[2]);
    intree->SetBranchAddress((dName2 + "_PZ").c_str(), &p2[3]);

    std::cout << "Filling tree..." << std::endl;

    Long64_t numEntries = intree->GetEntries();
    for (Long64_t i = 0; i < numEntries; i++) {
        intree->GetEntry(i);
        invMass = getCombinedInvMass(p1[0], p1[1], p1[2], p1[3], p2[0], p2[1], p2[2], p2[3]);
        invMassErr = invMass - pmass;
        outtree->Fill();
    }
    // outtree->Print();
    std::cout << "Writing tree..." << std::endl;

    fout->Write();
    delete fin;
    delete fout;
    std::cout << "Done" << std::endl;
}

void addInvMassBranch3(std::string fileIn, std::string treeName, std::string pName, std::string dName1,
                       std::string dName2, std::string dName3, std::string fileOut) {
    std::cout << "Opening file " << fileIn << std::endl;
    TFile *fin = TFile::Open(fileIn.c_str());

    std::cout << "Creating output file " << fileOut << std::endl;
    TFile *fout = TFile::Open(fileOut.c_str(), "RECREATE");
    TTree *intree = reinterpret_cast<TTree*>(fin->Get(treeName.c_str()));
    if (intree == NULL) {
        intree = reinterpret_cast<TTree*>(fin->Get(("Tuple/" + treeName).c_str()));
    }
    fout->cd();

    std::cout << "Cloning tree..." << std::endl;
    TTree *outtree = intree->CloneTree(0);
    Double_t invMass, invMassErr, pmass, p1[4], p2[4], p3[4];

    std::cout << "Creating branch..." << std::endl;
    outtree->Branch((pName+"_InvMass").c_str(), &invMass, (pName+"_InvMass/D").c_str());
    outtree->Branch((pName+"_InvMass_ERR").c_str(), &invMassErr, (pName+"_InvMass_ERR/D").c_str());

    intree->SetBranchAddress((pName + "_M").c_str(), &pmass);
    intree->SetBranchAddress((dName1 + "_PE").c_str(), &p1[0]);
    intree->SetBranchAddress((dName1 + "_PX").c_str(), &p1[1]);
    intree->SetBranchAddress((dName1 + "_PY").c_str(), &p1[2]);
    intree->SetBranchAddress((dName1 + "_PZ").c_str(), &p1[3]);
    intree->SetBranchAddress((dName2 + "_PE").c_str(), &p2[0]);
    intree->SetBranchAddress((dName2 + "_PX").c_str(), &p2[1]);
    intree->SetBranchAddress((dName2 + "_PY").c_str(), &p2[2]);
    intree->SetBranchAddress((dName2 + "_PZ").c_str(), &p2[3]);
    intree->SetBranchAddress((dName3 + "_PE").c_str(), &p3[0]);
    intree->SetBranchAddress((dName3 + "_PX").c_str(), &p3[1]);
    intree->SetBranchAddress((dName3 + "_PY").c_str(), &p3[2]);
    intree->SetBranchAddress((dName3 + "_PZ").c_str(), &p3[3]);

    std::cout << "Filling tree..." << std::endl;

    Long64_t numEntries = intree->GetEntries();
    for (Long64_t i=0; i < numEntries; i++) {
        intree->GetEntry(i);
        invMass = getCombinedInvMass3(p1, p2, p3);
        invMassErr = invMass - pmass;
        outtree->Fill();
    }
    // outtree->Print();
    std::cout << "Writing tree..." << std::endl;

    fout->Write();
    delete fin;
    delete fout;
    std::cout << "Done" << std::endl;
}

int main(int argc, char const *argv[]) {
    if (argc != 6 && argc != 7) {
        std::cerr << "Usage: " << argv[0] << " <input file> <parentName> <daughterName1> <daughterName2> <output file>" << std::endl;
        std::cerr << "OR" << std::endl;
        std::cerr << "Usage: " << argv[0] << " <input file> <parentName> <daughterName1> <daughterName2> <daughterName3> <output file>" << std::endl;
        return 1;
    }
    if (argc == 6) {
        addInvMassBranch2(std::string(argv[1]), "DecayTree", std::string(argv[2]), std::string(argv[3]),
                          std::string(argv[4]), std::string(argv[5]));
    } else {
        addInvMassBranch3(std::string(argv[1]), "DecayTree", std::string(argv[2]), std::string(argv[3]),
                          std::string(argv[4]), std::string(argv[5]), std::string(argv[6]));
    }
    return 0;
}
