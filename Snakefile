SBCOMPPLOTS = ["plots/comparison/%s_comparison.pdf" % (i) for i in ["B_M_SB", "JPsi_M_SB", "Omega_M_SB", "Pi0_M_SB"]]
SBPTCOMPPLOTS = ["plots/comparison/%s_HighPTcut_comparison.pdf" % (i) for i in ["B_M_SB", "JPsi_M_SB", "Omega_M_SB", "Pi0_M_SB"]]

# COMPBIN = ["analysis/bin/%s" % (i) for i in ["CompareBranch", "CompareBranchSB"]]
COMPBIN = ["analysis/bin/%s" % (i) for i in ["CompareBranchSB"]]
COMMONLIBS = ["common/lib/lib%s.so" % (i) for i in ["CloneInfo", "CloneTagger", "GetTree", "plotmaker", "progbar"]]

rule all:
    input:
        SBCOMPPLOTS, SBPTCOMPPLOTS

rule sbplots:
    input:
        COMPBIN
    output:
        SBCOMPPLOTS
    threads: 4
    shell:
        # expand("./{bin} -O {sb}", bin=COMPBIN, sb=SBCOMPPLOTS)
        shell("./{bin} -O {sb}".format(bin=COMPBIN, sb=SBCOMPPLOTS))

rule sbptplots:
    input:
        COMPBIN
    output:
        SBPTCOMPPLOTS
    threads: 4
    shell:
        # expand("./{bin} -O {sbpt}", bin=COMPBIN, sbpt=SBPTCOMPPLOTS)
        shell("./{bin} -O {sbpt}".format(bin=COMPBIN, sbpt=SBPTCOMPPLOTS))

rule compbin:
    output:
        COMPBIN, COMMONLIBS
    shell:
        "make -j$(nproc)"