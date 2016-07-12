EOS = "root://eoslhcb.cern.ch/"
EOSDIR = "/eos/lhcb/user/k/kgizdov/jpsi_omega/"
FILE = "cut_tuples.root"


SBMASSPLOTS = ["plots/comparison/%s_comparison.pdf" % (i) for i in ["B_M_SB", "JPsi_M_SB", "Omega_M_SB", "Pi0_M_SB"]]
SBPTMASSPLOTS = ["plots/comparison/%s_HighPTcut_comparison.pdf" % (i) for i in ["B_M_SB", "JPsi_M_SB", "Omega_M_SB", "Pi0_M_SB"]]

# B0 comparison plots params
B_VARS =     ["%s" % (i) for i in ["B_M", "B_DTF_MASS_constr1", "B_PT", "B_DTF_CTAU", "B_DTF_CHI2NDOF", "B_ETA", "B_IPCHI2_OWNPV", "B_VCHI2NDOF"]]
B_WRANGE =   ["%s" % (i) for i in ["-l 5100 -u 5600", "-l 5100 -u 5600", "-l 0 -u 20000", "-l 0.150 -u 1", "-l 0 -u 5", "-l 2 -u 6", "-l 0 -u 10", "-l 0 -u 5",]]
B_NRANGE =   ["%s" % (i) for i in ["-l 5100 -u 5600", "-l 5100 -u 5600", "-l 0 -u 10000", "-l 0.150 -u 1", "-l 0 -u 5", "-l 2 -u 6", "-l 0 -u 10", "-l 0 -u 5",]]
B_TITLE =    ["%s" % (i) for i in ["#it{{m}}(#it{{J#psi#omega}})", "#it{{m}}(#it{{J#psi#omega}})", "#it{P_{{T}}}(#it{{J#psi#omega}})", "#it{{c}}#tau(#it{{J#psi#omega}})"
                                  ,"#it{{#chi^{{2}}/ndf}}(#it{{J#psi#omega}})", "#it{{#eta}}(#it{{J#psi#omega}})", "#it{{IP#chi^{{2}}}}(#it{{J#psi#omega}})", "#it{{VX#chi^{{2}}/ndf}}(#it{{J#psi#omega}})"]]
B_UNIT =     ["%s" % (i) for i in ["MeV/#it{{c}}^{{2}}", "MeV/#it{{c}}^{{2}}", "MeV/#it{{c}}", "#it{{mm}}", " ", " ", " ", " "]]
B_PLOTS =    ["plots/comparison/B/%s_comparison.pdf" % (i) for i in B_VARS]
B_PT_PLOTS = ["plots/comparison/B/%s_HighPTcut_comparison.pdf" % (i) for i in B_VARS]

# J/psi comparison plots params
JP_VARS =     ["%s" % (i) for i in ["Jpsi_M", "Jpsi_PT", "Jpsi_OWNPV_CHI2", "Jpsi_IPCHI2_OWNPV"]]
JP_WRANGE =   ["%s" % (i) for i in ["-l 3050 -u 3150", "-l 0 -u 10000", "-l 0 -u 100", "-l 0 -u 1000"]]
JP_NRANGE =   ["%s" % (i) for i in ["-l 3050 -u 3150", "-l 0 -u 6000", "-l 0 -u 60" "-l 0 -u 300"]]
JP_TITLE =    ["%s" % (i) for i in ["#it{m}(#it{J#psi})", "#it{P_{T}}(#it{J#psi})","#it{PV#chi^{2}}(#it{J#psi})", "#it{IP#chi^{2}}(#it{J#psi})"]]
JP_UNIT =     ["%s" % (i) for i in ["MeV/#it{c}^{2}", "MeV/#it{c}", " ", " "]]
JP_PLOTS =    ["plots/comparison/JP/%s_comparison.pdf" % (i) for i in JP_VARS]
JP_PT_PLOTS = ["plots/comparison/JP/%s_HighPTcut_comparison.pdf" % (i) for i in JP_VARS]

# Omega comparison plots params
OM_VARS =     ["%s" % (i) for i in ["omega_M", "omega_PT", "omega_OWNPV_CHI2", "omega_IPCHI2_OWNPV"]]
OM_WRANGE =   ["%s" % (i) for i in ["-l 732 -u 832", "-l 3000 -u 10000", "-l 0 -u 100", "-l 0 -u 1000"]]
OM_NRANGE =   ["%s" % (i) for i in ["-l 732 -u 832", "-l 3000 -u 6000", "-l 0 -u 60" "-l 0 -u 300"]]
OM_TITLE =    ["%s" % (i) for i in ["#it{m}(#it{#omega})", "#it{P_{T}}(#it{#omega})","#it{PV#chi^{2}}(#it{#omega})", "#it{IP#chi^{2}}(#it{#omega})"]]
OM_UNIT =     ["%s" % (i) for i in ["MeV/#it{c}^{2}", "MeV/#it{c}", " ", " "]]
OM_PLOTS =    ["plots/comparison/OM/%s_comparison.pdf" % (i) for i in OM_VARS]
OM_PT_PLOTS = ["plots/comparison/OM/%s_HighPTcut_comparison.pdf" % (i) for i in OM_VARS]

# PiZero comparison plots params
PZ_VARS =     ["%s" % (i) for i in ["pizero_M", "pizero_PT"]]
PZ_WRANGE =   ["%s" % (i) for i in ["-l 109 -u 159", "-l 500 -u 4000"]]
PZ_NRANGE =   ["%s" % (i) for i in ["-l 109 -u 159", "-l 500 -u 1500"]]
OM_TITLE =    ["%s" % (i) for i in ["#it{m}(#it{#pi^{0}})", "#it{P_{T}}(#it{#pi^{0}})"]]
OM_UNIT =     ["%s" % (i) for i in ["MeV/#it{c}^{2}", "MeV/#it{c}"]]
PZ_PLOTS =    ["plots/comparison/PZ/%s_comparison.pdf" % (i) for i in PZ_VARS]
PZ_PT_PLOTS = ["plots/comparison/PZ/%s_HighPTcut_comparison.pdf" % (i) for i in PZ_VARS]

MASSRANGE = ["%s" % (i) for i in ["-l 5100 -u 5600", "-l 3050 -u 3150", "-l 732 -u 832", "-l 109 -u 159"]]
PTWRANGE = ["%s" % (i) for i in ["-l 0 -u 20000", "-l 0 -u 10000", "-l 3000 -u 10000", "-l 450 -u 4000"]]
PTNRANGE = ["%s" % (i) for i in ["-l 0 -u 10000", "-l 0 -u 6000", "-l 3000 -u 6000", "-l 450 -u 2000"]]

# COMPBIN = ["analysis/bin/%s" % (i) for i in ["CompareBranch", "CompareBranchSB"]]
COMPBIN = ["analysis/bin/%s" % (i) for i in ["CompareBranchSB"]]
COMMONLIBS = ["common/lib/lib%s.so" % (i) for i in ["CloneInfo", "CloneTagger", "GetTree", "plotmaker", "progbar"]]

rule all:
    input:
        B_PLOTS, B_PT_PLOTS

rule bplots:
    input:
        COMPBIN
    output:
        B_PLOTS
    threads: 4
    shell:
        # expand("""./{bin}   -M {e}{dir}/mc/{file}
        #                     -R {e}{dir}/data/{file}
        #                     -B {br}
        #                     -T {title}
        #                     -U {unit}
        #                     -O {pdf}
        #                     {range}""".split()
        #                     , zip
        #                     , bin=COMPBIN, br=B_VARS, title=B_TITLE, unit=B_UNIT, range=B_NRANGE, pdf=B_PLOTS, e=EOS, dir=EOSDIR, file=FILE)
        shell("""./{bin}   -M {e}{dir}/mc/{file}
                            -R {e}{dir}/data/{file}
                            -B {br}
                            -T {title}
                            -U {unit}
                            -O {pdf}
                            {range}""".format(
                            # , zip
                            bin=COMPBIN, br=B_VARS, title=B_TITLE, unit=B_UNIT, range=B_NRANGE, pdf=B_PLOTS, e=EOS, dir=EOSDIR, file=FILE))
        # shell("./{bin} -R {e}{dir}/data/{file} -O {sb}".format(bin=COMPBIN, sb=SBMASSPLOTS, e=EOS, dir=EOSDIR, file=FILE))

rule bptplots:
    input:
        COMPBIN
    output:
        B_PT_PLOTS
    threads: 4
    shell:
        # expand("""./{bin}   -M {e}{dir}/mc/{file}
        #                     -R {e}{dir}/data/{file}
        #                     -B {br}
        #                     -C omega_PT>8000
        #                     -T {title}
        #                     -U {unit}
        #                     -O {pdf}
        #                     {range}""".split()
        #                     , zip
        #                     , bin=COMPBIN, br=B_VARS, title=B_TITLE, unit=B_UNIT, range=B_NRANGE, pdf=B_PT_PLOTS, e=EOS, dir=EOSDIR, file=FILE)
        shell("""./{bin}   -M {e}{dir}/mc/{file}
                            -R {e}{dir}/data/{file}
                            -B {br}
                            -C omega_PT>8000
                            -T {title}
                            -U {unit}
                            -O {pdf}
                            {range}""".format(
                            # , zip
                            bin=COMPBIN, br=B_VARS, title=B_TITLE, unit=B_UNIT, range=B_NRANGE, pdf=B_PT_PLOTS, e=EOS, dir=EOSDIR, file=FILE))
        # shell("./{bin} -R {e}{dir}/data/{file} -O {sb}".format(bin=COMPBIN, sb=SBMASSPLOTS, e=EOS, dir=EOSDIR, file=FILE))

rule compbin:
    output:
        COMPBIN, COMMONLIBS
    shell:
        "make -j$(nproc)"
