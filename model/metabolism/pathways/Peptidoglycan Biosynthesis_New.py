from CellScribe import *
from model.metabolites import phosphate, atp, adp
from model.genes import SP_1081, SP_1966, SP_1390, SP_1521, SP_0688, SP_1589, SP_1530, SP_1671, SP_1670, SP_0337, SP_0689, SP_0615, SP_0616, SP_0457

#minors
phosphate = Metabolite("phosphate", kegg="C00009")
PEP = Metabolite("phosphoenolpyruvate", kegg="C00074")
NADP = Metabolite("NADP+", kegg="C00006")
NADPH = Metabolite("NADPH", kegg="C00005")
H = Metabolite("H+", kegg="C00080")
ATP = Metabolite("ATP", kegg="C00002")
ADP = Metabolite("ADP", kegg="C00008")
L_alanine = Metabolite("L-alanine", kegg="C00041")
UDP = Metabolite("UDP", kegg="C00015")
L_Lysine = Metabolite("L-lysine", kegg="C00047")
undecaprenyl_phosphate = Metabolite("undecaprenyl phosphate", kegg="C17556")
L_Alanyl_tRNA = Metabolite("L_Alanyl_tRNA", kegg="C00886")
tRNA_Ala = Metabolite("tRNA_Ala", kegg="C01635")
undecaprenyl_diphosphate = Metabolite("Undecaprenyl diphosphate", kegg="C04574")
H2O = Metabolite("H2O", kegg="C00001")



#major metabolites
UDP_N_acetyl_alpha_D_glucosamine = Metabolite("UDP-N-acetyl-alpha-D-glucosamine", kegg="C00043")
UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine = Metabolite("UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine", kegg="C04631")
UDP_N_acetylmuramate = Metabolite("UDP-N-acetylmuramate", kegg="C01050")
UDP_N_acetylmuramoyl_L_alanine = Metabolite("UDP-N-acetylmuramoyl-L-alanine", kegg="C01212")
UDP_N_acetylmuramoyl_L_alanyl_D_glutamate = Metabolite("UDP-N-acetylmuramoyl-L-alanyl-D-glutamate", kegg="C00692")
D_glutamate = Metabolite("D-glutamate", kegg="C00217")
meso_2_6_diaminoheptanedioate = Metabolite("meso_2,6_diaminoheptanedioate", kegg="C00680")
UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2_6_diaminopimelate = Metabolite("UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2,6", kegg="C04877")
D_alanyl_D_alanine = Metabolite("D_alanyl_D_alanine", kegg="C00993")
D_alanine = Metabolite("D_alanine", kegg="C00133")
UMP = Metabolite("UMP", kegg="C00105")
Undecaprenyl_phosphate = Metabolite("Undecaprenyl_phosphate", kegg="C17556")
Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine", kegg="C04851")
Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl_diphospho_N_acetylmuramoyl_(N_acetylglucosamine)_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine", kegg="C05893")
UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("UDP_N_acetylmuramoyl_L_alanyl_gamma__D_glutamyl_L_lysyl_D_alanyl_D_alanine", kegg="C04702")
UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine = Metabolite("UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2,6_diaminopimelyl_D_alanyl_D_alanine", kegg="C04882")
UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine = Metabolite("UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine", kegg="C05892")
N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenol = Metabolite("N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine-diphosphoundecaprenol", kegg="C05897")
N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenyl_N_acetylglucosamine = Metabolite("N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine-diphosphoundecaprenyl-N-acetylglucosamine", kegg="C05898")
Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D-alanyl_D_alanine", kegg="C17550")
Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_L_alanyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_L_alanyl_D_alanyl_D_alanine", kegg="C17549")


MurA = Reaction(name="MurA",
                reactants=PEP + UDP_N_acetyl_alpha_D_glucosamine,
                products=phosphate + UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine,
                pairs=[(UDP_N_acetyl_alpha_D_glucosamine, UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine)],
                minors=[PEP, phosphate])

SP_1081 = Gene("SP_1081")
SP_1966 = Gene("SP_1966")
MurA_GA = GeneAssociation(MurA, SP_1081 | SP_1966)

##############################################################################

MurB = Reaction(name="MurB",
                reactants=NADPH + H + UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine,
                products=NADP + UDP_N_acetylmuramate,
                pairs=[(UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine, UDP_N_acetylmuramate)],
                minors=[NADPH, NADP, H])


SP_1390 = Gene("SP_1390")
MurB_GA = GeneAssociation(MurB, SP_1390)

###Make sure minors are going in the right direction

##############################################################################

MurC = Reaction(name="MurC",
                reactants=ATP + UDP_N_acetylmuramate + L_alanine,
                products=ADP + UDP_N_acetylmuramoyl_L_alanine + phosphate + H,
                pairs=[(UDP_N_acetylmuramate, UDP_N_acetylmuramoyl_L_alanine)],
                minors=[ATP, ADP, phosphate, L_alanine, H])


SP_1521 = Gene("SP_1521")
MurC_GA = GeneAssociation(MurC, SP_1521)

##############################################################################

MurD = Reaction(name="MurD",
                reactants=UDP_N_acetylmuramoyl_L_alanine + ATP + D_glutamate,
                products=UDP_N_acetylmuramoyl_L_alanyl_D_glutamate + ADP + phosphate + H,
                pairs=[(UDP_N_acetylmuramoyl_L_alanine, UDP_N_acetylmuramoyl_L_alanyl_D_glutamate)],
                minors=[ATP, ADP, phosphate, H])

SP_0688 = Gene("SP_0688")
MurD_GA = GeneAssociation(MurD, SP_0688)

##############################################################################

Diaminopimelate_Ligase = Reaction(name="Diaminopimelate_Ligase",
                                  reactants=ATP + UDP_N_acetylmuramoyl_L_alanyl_D_glutamate + meso_2_6_diaminoheptanedioate,
                                  products=ADP + phosphate + UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2_6_diaminopimelate,
                                  pairs=[(UDP_N_acetylmuramoyl_L_alanyl_D_glutamate, UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2_6_diaminopimelate)],
                                  minors=[ATP, ADP, phosphate])

SP_1589 = Gene("SP_1589")
Diaminopimelate_Ligase_GA = GeneAssociation(Diaminopimelate_Ligase, SP_1589)

#Right side of the peptidoglycan biosynthesis pathway

###Does this have a hydrogen?????

##############################################################################

MurE = Reaction(name="MurE",
                reactants=UDP_N_acetylmuramoyl_L_alanyl_D_glutamate + ATP + L_Lysine,
                products=ADP + phosphate + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine + H,
                pairs=[(UDP_N_acetylmuramoyl_L_alanyl_D_glutamate, UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine)],
                minors=[ATP, ADP, phosphate, L_Lysine, H])

SP_1530 = Gene("SP_1530")
MurE_GA = GeneAssociation(MurE, SP_1530)

# Left side of the peptidoglycan biosynthesis pathway

##############################################################################

ddl = Reaction(name="ddl",
               reactants=ATP + 2*(D_alanine),
               products=ADP + phosphate + D_alanyl_D_alanine + H,
               pairs=[(2*(D_alanine), D_alanyl_D_alanine)],
               minors=[ATP, ADP, phosphate, H])

SP_1671 = Gene("SP_1671")
ddl_GA = GeneAssociation(ddl, SP_1671)

##############################################################################

MurF_Homolog_1 = Reaction(name="MurF_Homolog_1",
                        reactants=ATP + D_alanyl_D_alanine + UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2_6_diaminopimelate,
                        products=ADP + phosphate + UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine + H,
                        pairs=[(UDP_N_acetylmuramoyl_L_alanyl_D_gamma_glutamyl_meso_2_6_diaminopimelate, UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine)],
                        minors=[ATP, ADP, phosphate, H])

SP_1670 = Gene("SP_1670")
MurF_Homolog_1_GA = GeneAssociation(MurF_Homolog_1, SP_1670)

#Right side of the peptidoglycan biosynthesis pathway

##############################################################################

MurF_Homolog_2 = Reaction(name="MurF_Homolog_2",
                          reactants=ATP + D_alanyl_D_alanine + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine,
                          products=ADP + phosphate + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + H,
                          pairs=[(UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine, UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)],
                          minors=[ATP, ADP, phosphate, H])

SP_1670 = Gene("SP_1670")
MurF_Homolog_2_GA = GeneAssociation(MurF_Homolog_2, SP_1670)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MraY_1 = Reaction(name="MraY_1",
                  reactants=UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine + undecaprenyl_phosphate,
                  products=UMP + N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenol,
                  pairs=[(UDP_N_acetylmuramoyl__L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine, N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenol)])

SP_0337 = Gene("SP0337")
MraY_1_GA = GeneAssociation(MraY_1, SP_0337)

#Right side of the peptidoglycan biosynthesis pathway

##############################################################################

MraY_2 = Reaction(name="MraY_2",
                reactants=UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + Undecaprenyl_phosphate,
                products=UMP + Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine,
                pairs=[(UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)])

SP_0337 = Gene("SP_0337")
MraY_2_GA = GeneAssociation(MraY_2, SP_0337)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MurG_1 = Reaction("MurG_1",
                  reactants=N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenol + UDP_N_acetyl_alpha_D_glucosamine,
                  products=N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenyl_N_acetylglucosamine + UDP,
                  pairs=[N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenol, N_acetylmuramoyl_L_alanyl_D_glutamyl_meso_2_6_diaminopimelyl_D_alanyl_D_alanine_diphosphoundecaprenyl_N_acetylglucosamine],
                  minors=[UDP_N_acetyl_alpha_D_glucosamine, UDP])

SP_0689 = Gene("SP_0689")
MurG_1_GA = GeneAssociation(MurG_1, SP_0689)

#Right side of the peptidoglycan biosynthesis pathway

##############################################################################

MurG_2 = Reaction("MurG_2",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + UDP_N_acetyl_alpha_D_glucosamine,
                products=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + UDP,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)],
                minors=[UDP_N_acetyl_alpha_D_glucosamine, UDP])

SP_0689 = Gene("SP_0689")
MurG_2_GA = GeneAssociation(MurG_2, SP_0689)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MurM = Reaction("MurM",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + L_Alanyl_tRNA,
                products=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine + tRNA_Ala,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine)],
                minors=[L_Alanyl_tRNA, tRNA_Ala])

SP_0615 = Gene("SP_0615")
MurM_GA = GeneAssociation(MurM, SP_0615)

##############################################################################

MurN = Reaction("MurN",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine + L_Alanyl_tRNA,
                products=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_L_alanyl_D_alanyl_D_alanine + tRNA_Ala,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_L_alanyl_D_alanyl_D_alanine)],
                minors=[L_Alanyl_tRNA, tRNA_Ala])

SP_0616 = Gene("SP_0616")
MurN_GA = GeneAssociation(MurN, SP_0616)

##############################################################################

uppP = Reaction("uppP",
                reactants=undecaprenyl_diphosphate + H2O,
                products=undecaprenyl_phosphate + phosphate + H,
                pairs=[(undecaprenyl_diphosphate, undecaprenyl_phosphate)],
                minors=[H2O, H])

SP_0457 = Gene("SP_0457")
uppP_GA = GeneAssociation(uppP, SP_0457)

##############################################################################

#glycosyltransferase : elongation of uncross-linked glycans (either N-acetylmuramic acid or N-acetylglucosamine)
#transpeptidase : peptide cross-linking between two adjacent glycans
#DD-carboxypeptidase : hydrolyzes peptide bonds (in this case, between D-ala-D-alanine) to help control the extent of PG cross-linking

##Class A PBPs: N-terminal has a glycosyltransferase activity and the C-terminal has a transpeptidase activity
###pbp1a = SP_0369
###pbp1b = SP_2099
###pbp2a = SP_2010

##Class B PBPs: C-terminal has a transpeptidase activity; other functions not characterized but plays a role in cell division; has PASTA domains which are thought to bind unlinked peptidoglycans
###pbp2x = SP_0336 (cell division)--"Growth and Division of "Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet, pg. 846
###pbp2b = SP_1673 (functions during growth phase)--"Growth and Division of "Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet, pg. 846

##Class C PBPs: DD-carboxypeptidases
###SP_0872 (EC 3.4.16.4)

#Peptidoglycans consist of two alternating sugars N-acetylmuramic acid or N-acetylglucosamine
#N-acetylmuramic acid has a pentapeptide chain attached to it. Third amino acid is the cross-linking site and is, in the case of S. pneumoniae, a L-Lys
#Cross bridge consists of two L-Ala

#S. pneumoniae may not use the right side of this reaction: this creates a product (two sugars + pentapeptide) that has the meso-2,6-diaminopimeloyl in the third spot for cross-linking
###This is found primarily in gram negative bacteria and leads to direct linking with another peptidoglycan -- no cross-bridge ("Bacterial Cell Wall Synthesis..." Scheffers and Pinho, pg. 586)

#Average length of peptidogylcan chains in S. aureus is 3-10 with maximum being 23 to 26

#Expression/regulation information

#Class A: None is found to be essential in the sense that single mutants showed no obvious phenotype ("Growth and Division of "Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet, pg. 846)
### mutation of [pbp1b and (pbp1a or pbp2a)] = defects in septum position but not lethal
### mutation of [pbp1a and pbp2a] = possibly lethal
#Class B: Likely to be essential as attempts to isolate deletion mutants failed ("Growth and Division of "Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet, pg. 846)
#Class C (SP_0872): No apparent phenotype associated with its inactivation in S. aureus ("The penicillin binding proteins..." Kerff, Terrak, and Charlier, pg. 244-245)










