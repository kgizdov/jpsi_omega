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
#include "TLegend.h"
// RooFit headers
#include "RooDataSet.h"
#include "RooHist.h"
#include "RooPlot.h"
#include "RooRealVar.h"
// Custom headers
#include "plotmaker.h"
#include "GetTree.h"

// Just sum bin contents for a RooHist 
inline double integrate(RooHist* hist)
{
  double integral = 0;
  for(int i = 0; i < hist->GetN(); i++)
  {
    integral+=hist->GetY()[i];
  }
  return integral;
}
void CompareBranch(string MCfilename, string REfilename, string branchname, string xtitle, string unit, string plotname, string cuts, string MCweight, string REweight, double xlow, double xup, int nbins)
{
  // Open the files and get the trees
  TFile* MCfile = new TFile(MCfilename.c_str());
  TFile* REfile = new TFile(REfilename.c_str());
  TTree* MCtree = GetTree(MCfile,cuts);
  TTree* MCtree_s = GetTree(MCfile,cuts+"&& B_BKGCAT == 0");
  TTree* MCtree_b = GetTree(MCfile,cuts+"&& B_BKGCAT == 100");
  TTree* REtree = GetTree(REfile,cuts);
  // RooFit variables
  using namespace RooFit;
  RooRealVar* x = new RooRealVar(branchname.c_str(),xtitle.c_str(),xlow,xup);
  RooRealVar* MCw,* REw;
  RooDataSet* MCdata,* MCdata_b,* MCdata_s,* REdata;
  // Store the values of each bin because the GetMaximum() method isn't implemented properly in RooHist
  vector<double> bincontent;
  // Get the data out of the file and optionally weight it
  std::cout << "Importing first tree" << endl;
  if(MCweight!="")
  {
    MCw = new RooRealVar(MCweight.c_str(),"",-0.5,1.5);
    MCdata = new RooDataSet("MCdata","",RooArgSet(*x,*MCw),WeightVar(*MCw),Import(*MCtree));
    MCdata_s = new RooDataSet("MCdata_s","",RooArgSet(*x,*MCw),WeightVar(*MCw),Import(*MCtree_s));
    MCdata_b = new RooDataSet("MCdata_b","",RooArgSet(*x,*MCw),WeightVar(*MCw),Import(*MCtree_b));
  }
  else
  {
    MCdata = new RooDataSet("MCdata","",RooArgSet(*x),Import(*MCtree));
    MCdata_s = new RooDataSet("MCdata_s","",RooArgSet(*x),Import(*MCtree_s));
    MCdata_b = new RooDataSet("MCdata_b","",RooArgSet(*x),Import(*MCtree_b));
  }
  std::cout << "Importing second tree" << endl;
  if(REweight!="")
  {
    REw = new RooRealVar(REweight.c_str(),"",-0.5,1.5);
    REdata = new RooDataSet("REdata","",RooArgSet(*x,*REw),WeightVar(*REw),Import(*REtree));
  }
  else
  {
    REdata = new RooDataSet("REdata","",RooArgSet(*x),Import(*REtree));
  }
  // Create a RooPlot and add the data points
  RooPlot* frame = x->frame();
  std::cout << "Plotting" << endl;
  MCdata->plotOn(frame,Binning(nbins),DrawOption("B1"),FillColor(kOrange));
  MCdata_b->plotOn(frame,Binning(nbins),DrawOption("B1"),FillColor(kRed-7),FillStyle(3144));
  MCdata_s->plotOn(frame,Binning(nbins),DrawOption("B1"),FillColor(kBlue-7),FillStyle(3244));
  // MCdata_b->plotOn(frame,Binning(nbins),DrawOption("B1"),FillColor(kBlue));
  // MCdata_b->plotOn(frame,Binning(nbins),DrawOption("B1"),FillColor(kBlue),FillColorAlpha(0.35));
  // MCdata_b->plotOn(frame,Binning(nbins),DrawOption("B1"));
  // frame->getHist("h_MCdata_b")->SetFillColorAlpha(kBlue, 0.35);
  // MCdata_b->SetFillColorAlpha(kBlue, 0.35);
  // MCdata_b->plotOn(frame,Binning(nbins),DrawOption("B1"));
  REdata->plotOn(frame,Binning(nbins));

  // Get the histograms out of the RooPlot
  RooHist* h_MCdata = frame->getHist("h_MCdata");
  RooHist* h_MCdata_s = frame->getHist("h_MCdata_s");
  RooHist* h_MCdata_b = frame->getHist("h_MCdata_b");
  RooHist* h_REdata = frame->getHist("h_REdata");

  // Put a legend
  TLegend *leg1;
  leg1 = new TLegend(0.2,0.8,0.4,0.92);
  leg1->SetFillColor(kWhite);
  leg1->SetLineColor(kWhite);
  // leg1->AddEntry(frame->getObject(3),"Data", "P");
  // leg1->AddEntry(frame->findObject("h_REdata"),"Data", "P");
  leg1->AddEntry(frame->findObject("h_REdata"),"Data", "LP");
  leg1->AddEntry(frame->findObject("h_MCdata"),"MC Signal + background","F");
  leg1->AddEntry(frame->findObject("h_MCdata_b"),"MC Background only", "F");
  leg1->AddEntry(frame->findObject("h_MCdata_s"),"MC Signal only", "F");
  // leg1->Draw();
  // Integrate the histograms
  double MCint = integrate(h_MCdata);
  double MCint_s = integrate(h_MCdata_s);
  double MCint_b = integrate(h_MCdata_b);
  double REint = integrate(h_REdata);
  double ratio = MCint/REint;
  cout << "First integral \t" << MCint << endl;
  cout << "Second integral\t" << REint << endl;
  cout << "Scale factor   \t" << ratio << endl;
  // Get rid of MC datapoint error bars and normalise to unity
  for(int i = 0; i < h_MCdata->GetN(); i++)
  {
    h_MCdata->SetPointError(i,0,0,0,0);
    h_MCdata_s->SetPointError(i,0,0,0,0);
    h_MCdata_b->SetPointError(i,0,0,0,0);
    h_MCdata->GetY()[i] /= MCint;
    h_MCdata_s->GetY()[i] /= MCint;
    h_MCdata_b->GetY()[i] /= MCint;
    bincontent.push_back(h_MCdata->GetY()[i]);
    bincontent.push_back(h_MCdata_b->GetY()[i]);
    bincontent.push_back(h_MCdata_s->GetY()[i]);
  }
  // Normalise to unity
  for(int i = 0; i < h_REdata->GetN(); i++)
  {
    h_REdata->GetY(     )[i] /= REint;
    h_REdata->GetEYhigh()[i] /= REint;
    h_REdata->GetEYlow( )[i] /= REint;
    bincontent.push_back(h_REdata->GetY()[i]);
  }
  // Set a sensible maximum so the blurb doesn't sit on top of data points
  double max = *max_element(bincontent.begin(),bincontent.end());
  cout << "The maximum is\t" << max << endl;
  frame->SetMaximum(max*1.3);
  frame->SetMinimum(0);
  // Draw everything
  plotmaker plotter(frame);
  plotter.SetTitle(xtitle, unit);
  TCanvas* canvas = plotter.Draw();
  leg1->Draw();
  canvas->SetLogy();
  canvas->SaveAs((plotname+".pdf").c_str());
}

int main(int argc, char* argv[])
{
  using namespace boost::program_options;
  options_description desc("Allowed options",(unsigned)120);
  std::string MCfile, REfile, branch, cuts, xtitle, unit, plot, MCweight, REweight;
  double xlow, xup;
  int nbins;
  desc.add_options()
    ("help,H"    ,                                                                                        "produce help message"                      )
    ("MCfile,M"  , value<std::string>(&MCfile  )->default_value("ntuples/DVTuples_mc.root"          ), "set Monte Carlo file"                      )
    ("REfile,R"  , value<std::string>(&REfile  )->default_value("ntuples/DVTuples_data.root"        ), "set collision data file"                   )
    ("branch,B"  , value<std::string>(&branch  )->default_value("Tuple/DecayTree/B_MM"                       ), "set branch to plot"                        )
    ("MCweight,w", value<std::string>(&MCweight)->default_value(""                                     ), "set Monte Carlo weighting variable"        )
    ("REweight,W", value<std::string>(&REweight)->default_value(""                                     ), "set collision data weighting variable"     )
    ("cuts,C"    , value<std::string>(&cuts    )->default_value(""                                     ), "set optional cuts (UNIMPLEMENTED)"         )
    ("title,T"   , value<std::string>(&xtitle  )->default_value("#it{m}(#it{#phi K^{#plus}K^{#minus}})"), "set x-axis title (takes ROOT LaTeX format)")
    ("unit,U"    , value<std::string>(&unit    )->default_value("MeV/#it{c}^{2}"                       ), "set unit (takes ROOT LaTeX format)"        )
    ("plot,O"    , value<std::string>(&plot    )->default_value("comparison"                           ), "set output plot filename"                  )
    ("upper,u"   , value<double     >(&xup     )->default_value(5600                                   ), "set branch upper limit"                    )
    ("lower,l"   , value<double     >(&xlow    )->default_value(5000                                   ), "set branch lower limit"                    )
    ("bins,b"    , value<int        >(&nbins   )->default_value(20                                     ), "set number of bins"                        )
  ;
  variables_map vmap;
  store(parse_command_line(argc, argv, desc), vmap);
  notify(vmap);
  if (vmap.count("help"))
  {
    std::cout << desc << endl;
    return 1;
  }
  cout << "Entering main function" << endl;
  CompareBranch(MCfile,REfile,branch,xtitle,unit,plot,cuts,MCweight,REweight,xlow,xup,nbins);
  return 0;
}
