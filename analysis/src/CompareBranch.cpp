// Copyright 2016 Adam Morris
// Copyright 2016 Konstantin Gizdov
// Standard headers
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
// BOOST headers
#include "boost/program_options.hpp"
// ROOT headers
#include "TFile.h"
#include "TTree.h"
#include "TH1.h"
#include "TMath.h"
// RooFit headers
#include "RooDataSet.h"
#include "RooHist.h"
#include "RooPlot.h"
#include "RooRealVar.h"
// Custom headers
#include "../../common/include/plotmaker.h"
#include "../../common/include/GetTree.h"

// Just sum bin contents for a RooHist
inline double integrate(RooHist* hist) {
    double integral = 0;
    for (int i = 0; i < hist->GetN(); i++) {
        integral+=hist->GetY()[i];
    }
    return integral;
}
void CompareBranch(string MCfilename, string REfilename, string branchname,
                    string xtitle, string unit, string plotname, string cuts,
                    string MCweight, string REweight, double xlow, double xup, int nbins) {
    // Open the files and get the trees
    // TFile* MCfile = new TFile(MCfilename.c_str());
    TFile* MCfile = TFile::Open(MCfilename.c_str());
    // TFile* REfile = new TFile(REfilename.c_str());
    TFile* REfile = TFile::Open(REfilename.c_str());
    TTree* MCtree = GetTree(MCfile, cuts);
    TTree* REtree = GetTree(REfile, cuts);
    // RooFit variables
    // using namespace RooFit;
    namespace rf = RooFit;
    RooRealVar* x = new RooRealVar(branchname.c_str(), xtitle.c_str(), xlow, xup);
    RooDataSet* MCdata, * REdata;
    // Store the values of each bin because the GetMaximum() method isn't implemented properly in RooHist
    vector<double> bincontent;
    // Get the data out of the file and optionally weight it
    std::cout << "Importing first tree" << endl;
    if (MCweight != "") {
        RooRealVar * MCw;
        MCw = new RooRealVar(MCweight.c_str(), "", -0.5, 1.5);
        MCdata = new RooDataSet("MCdata", "", RooArgSet(*x, *MCw), rf::WeightVar(*MCw), rf::Import(*MCtree));
    } else {
        MCdata = new RooDataSet("MCdata", "", RooArgSet(*x), rf::Import(*MCtree));
    }
    std::cout << "Importing second tree" << endl;
    if (REweight != "") {
        RooRealVar * REw;
        REw = new RooRealVar(REweight.c_str(), "", -0.5, 1.5);
        REdata = new RooDataSet("REdata", "", RooArgSet(*x, *REw), rf::WeightVar(*REw), rf::Import(*REtree));
    } else {
        REdata = new RooDataSet("REdata", "", RooArgSet(*x), rf::Import(*REtree));
    }
    // Create a RooPlot and add the data points
    RooPlot* frame = x->frame();
    std::cout << "Plotting" << endl;
    MCdata->plotOn(frame, rf::Binning(nbins), rf::DrawOption("B1"), rf::FillColor(kOrange));
    REdata->plotOn(frame, rf::Binning(nbins));
    // Get the histograms out of the RooPlot
    RooHist* h_MCdata = frame->getHist("h_MCdata");
    RooHist* h_REdata = frame->getHist("h_REdata");
    // Integrate the histograms
    double MCint = integrate(h_MCdata);
    double REint = integrate(h_REdata);
    double ratio = MCint/REint;
    cout << "First integral \t" << MCint << endl;
    cout << "Second integral\t" << REint << endl;
    cout << "Scale factor   \t" << ratio << endl;
    // Get rid of MC datapoint error bars and normalise to unity
    for (int i = 0; i < h_MCdata->GetN(); i++) {
        h_MCdata->SetPointError(i, 0, 0, 0, 0);
        h_MCdata->GetY()[i] /= MCint;
        bincontent.push_back(h_MCdata->GetY()[i]);
    }
    // Normalise to unity
    for (int i = 0; i < h_REdata->GetN(); i++) {
        h_REdata->GetY()[i]      /= REint;
        h_REdata->GetEYhigh()[i] /= REint;
        h_REdata->GetEYlow()[i]  /= REint;
        bincontent.push_back(h_REdata->GetY()[i]);
    }
    // Set a sensible maximum so the blurb doesn't sit on top of data points
    double max = *max_element(bincontent.begin(), bincontent.end());
    cout << "The maximum is\t" << max << endl;
    frame->SetMaximum(max*1.3);
    frame->SetMinimum(0);
    // Draw everything
    plotmaker plotter(frame);
    plotter.SetTitle(xtitle, unit);
    plotter.Draw()->SaveAs((plotname+".pdf").c_str());
}

int main(int argc, char* argv[]) {
    // using namespace boost::program_options;
    namespace po = boost::program_options;
    po::options_description desc("Allowed options", (unsigned)120);
    std::string MCfile, REfile, branch, cuts, xtitle, unit, plot, MCweight, REweight;
    double xlow = 0, xup = 0;
    int nbins = 0;
    desc.add_options()
        ("help,H"    ,                                                                                 "produce help message"                      )
        ("MCfile,M"  , po::value<std::string>(&MCfile  )->default_value("ntuples/DVTuples_mc.root"  ), "set Monte Carlo file"                      )
        ("REfile,R"  , po::value<std::string>(&REfile  )->default_value("ntuples/DVTuples_data.root"), "set collision data file"                   )
        ("branch,B"  , po::value<std::string>(&branch  )->default_value("B_DTF_MASS_constr1"        ), "set branch to plot"                        )
        ("MCweight,w", po::value<std::string>(&MCweight)->default_value(""                          ), "set Monte Carlo weighting variable"        )
        ("REweight,W", po::value<std::string>(&REweight)->default_value(""                          ), "set collision data weighting variable"     )
        ("cuts,C"    , po::value<std::string>(&cuts    )->default_value(""                          ), "set optional cuts (UNIMPLEMENTED)"         )
        ("title,T"   , po::value<std::string>(&xtitle  )->default_value("#it{m}(#it{J/#psi #omega})"), "set x-axis title (takes ROOT LaTeX format)")
        ("unit,U"    , po::value<std::string>(&unit    )->default_value("MeV/#it{c}^{2}"            ), "set unit (takes ROOT LaTeX format)"        )
        ("plot,O"    , po::value<std::string>(&plot    )->default_value("B_M_comparison"            ), "set output plot filename"                  )
        ("lower,l"   , po::value<double     >(&xlow    )->default_value(5100                        ), "set branch lower limit"                    )
        ("upper,u"   , po::value<double     >(&xup     )->default_value(5600                        ), "set branch upper limit"                    )
        ("bins,b"    , po::value<int        >(&nbins   )->default_value(20                          ), "set number of bins"                        )
    ;
    po::variables_map vmap;
    po::store(po::parse_command_line(argc, argv, desc), vmap);
    po::notify(vmap);
    if (vmap.count("help")) {
        std::cout << desc << endl;
        return 1;
    }
    cout << "Entering main function" << endl;
    CompareBranch(MCfile, REfile, branch, xtitle, unit, plot, cuts, MCweight, REweight, xlow, xup, nbins);
    return 0;
}
