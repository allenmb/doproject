import numpy as np
import scipy.stats


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h

#values from params.txt
alphat1 = [0.16756793, 0.4710162, -0.02937284]
alphat2 = [1.57540203, 0.30732219, -0.39002928]
alphat3 = [-0.9966547,0.12249597, 0.50551277]
alphat4 = [0.58819534, -0.40837154, 0.02912796]
alphat5 = [0.60332029, -0.21841236, -0.03696413]
alphat6 = [-0.53945947, -0.55825876, -0.42384931]
alphat7 = [ 0.24786555, -0.21534205, 0.23836369]
betat1 = [0,0,0]
betat2 = [0,0,0]
betat3 = [0,0,0]
betat4 = [-0.02652678, -0.02357504, 0.04381682]
betat5 = [0.0745371, -0.04208096, -0.00881286]
betat6 = [ 0.07230737, -0.0623105, -0.00808687]
betat7 = [0,0,0]
gain1 = 1.73901322
gain2 = -2.4276991
gain3 = 6.78629273
gain4 = 3.1006461
gain5 = -5.35550775
gain6 = 9.83744151
gain7 = 2.82578722
K1, tau1, A1, B1 = [ 0.02077936, 0.30082881, 0.00523523, -4.14525173]
K2, tau2, A2, B2 = [ 0.02497473, 0.44387497, 0.01159895, -1.31252334]
K3, tau3, A3, B3 = [ 0.01889417, 0.46886, 0.01190718, -1.18323948]
K4, tau4, A4, B4 = [0.01305491, 3.85785973, 0.00856459, 0.11594656]
K5, tau5, A5, B5 = [0.01132568, 1.9620773, 0.00730827, 0.33600001]
K6, tau6, A6, B6 = [ 0.02807458, 10.55059128, 0.01102206, -0.34109386]
K7, tau7, A7, B7 = [ 0.02131376, 2.36357643, 0.00754481, -1.18999999]

# Put into arrays to run stats
alpha1 = [alphat1[0], alphat2[0],alphat3[0],alphat4[0],alphat5[0],alphat6[0],alphat7[0]]
alpha2 = [alphat1[1], alphat2[1],alphat3[1],alphat4[1],alphat5[1],alphat6[1],alphat7[1]]
alpha3 = [alphat1[2], alphat2[2],alphat3[2],alphat4[2],alphat5[2],alphat6[2],alphat7[2]]
beta1 = [betat1[0], betat2[0],betat3[0],betat4[0],betat5[0],betat6[0],betat7[0]]
beta2 = [betat1[1], betat2[1],betat3[1],betat4[1],betat5[1],betat6[1],betat7[1]]
beta3 = [betat1[2], betat2[2],betat3[2],betat4[2],betat5[2],betat6[2],betat7[2]]
gain = [gain1,gain2,gain3,gain4,gain5,gain6,gain7]
K = [K1,K2,K3,K4,K5,K6,K7]
tau = [tau1,tau2,tau3,tau4,tau5,tau6,tau7]
A = [A1,A2,A3,A4,A5,A6,A7]
B = [B1,B2,B3,B4,B5,B6,B7]

# Run Stats
alpha1_mean = mean_confidence_interval(alpha1)
alpha2_mean = mean_confidence_interval(alpha2)
alpha3_mean = mean_confidence_interval(alpha3)
beta1_mean = mean_confidence_interval(beta1)
beta2_mean = mean_confidence_interval(beta2)
beta3_mean = mean_confidence_interval(beta3)
gain_mean = mean_confidence_interval(gain)
K_mean = mean_confidence_interval(K)
tau_mean = mean_confidence_interval(tau)
A_mean = mean_confidence_interval(A)
B_mean = mean_confidence_interval(B)

# Print Stats
print(alpha1_mean)
print(mean_confidence_interval([alpha1[0],alpha1[1],alpha1[2],alpha1[6]]))
print(mean_confidence_interval([alpha1[3],alpha1[4],alpha1[5]]))
print(alpha2_mean)
print(mean_confidence_interval([alpha2[0],alpha2[1],alpha2[2],alpha2[6]]))
print(mean_confidence_interval([alpha2[3],alpha2[4],alpha2[5]]))
print(alpha3_mean)
print(mean_confidence_interval([alpha3[0],alpha3[1],alpha3[2],alpha3[6]]))
print(mean_confidence_interval([alpha3[3],alpha3[4],alpha3[5]]))
print(beta1_mean)
print(mean_confidence_interval([beta1[0],beta1[1],beta1[2],beta1[6]]))
print(mean_confidence_interval([beta1[3],beta1[4],beta1[5]]))
print(beta2_mean)
print(mean_confidence_interval([beta2[0],beta2[1],beta2[2],beta2[6]]))
print(mean_confidence_interval([beta2[3],beta2[4],beta2[5]]))
print(beta3_mean)
print(mean_confidence_interval([beta3[0],beta3[1],beta3[2],beta3[6]]))
print(mean_confidence_interval([beta3[3],beta3[4],beta3[5]]))
print(gain_mean)
print(mean_confidence_interval([gain[0],gain[1],gain[2],gain[6]]))
print(mean_confidence_interval([gain[3],gain[4],gain[5]]))
print(K_mean)
print(mean_confidence_interval([K[0],K[1],K[2],K[6]]))
print(mean_confidence_interval([K[3],K[4],K[5]]))
print(tau_mean)
print(mean_confidence_interval([tau[0],tau[1],tau[2],tau[6]]))
print(mean_confidence_interval([tau[3],tau[4],tau[5]]))
print(A_mean)
print(mean_confidence_interval([A[0],A[1],A[2],A[6]]))
print(mean_confidence_interval([A[3],A[4],A[5]]))
print(B_mean)
print(mean_confidence_interval([B[0],B[1],B[2],B[6]]))
print(mean_confidence_interval([B[3],B[4],B[5]]))

'''
Output format:
param  = (mean, 95% Confidence +-)

Outputs:
ARX PARAMETERS
alpha1      = (0.23517670999999996, 0.7718037288498272)
alpha1_550  = (0.24854520249999998, 1.6733408437789619)
alpha1_schd = (0.21735205333333332, 1.6282569613548923)
alpha2      = (-0.0713643357142857, 0.35179708470309606)
alpha2_550  = (0.17137307750000003, 0.46862870225529285)
alpha2_schd = (-0.39501421999999997, 0.42308962035596215)
alpha3      = (-0.015315877142857145, 0.3033642084905724)
alpha3_550  = (0.08111858499999999, 0.6087165975053958)
alpha3_schd = (-0.14389516, 0.6078415733109999)
beta1       = (0.01718824142857143, 0.03664489620586028)
beta1_550   = (0.0, 0.0)
beta1_schd  = (0.04010589666666666, 0.14337538457562737)
beta2       = (-0.01828092857142857, 0.023487688422677927)
beta2_550   = (0.0, 0.0)
beta2_schd  = (-0.04265549999999999, 0.048127982878254545)
beta3       = (0.0038452985714285716, 0.016713344642608766)
beta3_550   = (0.0, 0.0)
beta3_schd  = (0.008972363333333334, 0.07496722164064863)
gain        = (2.3579962757142856, 4.762528059434957)
gain_550    = (2.2308485175, 6.027774527547011)
gain_schd   = (2.5275266199999997, 18.91092581168093)

FOPDT + FF PARAMETERS
K           = (0.019773884285714288, 0.005557073932208244)
K_550       = (0.021490505, 0.004048273651452268)
K_schd      = (0.017485056666666665, 0.02288254421312192)
tau         = (2.8496669314285716, 3.362197825449485)
tau_550     = (0.8942850525000001, 1.563091794431025)
tau_schd    = (5.456842770000001, 11.208445643616626)
A           = (0.009025870000000002, 0.002346779207508814)
A_550       = (0.0090715425, 0.005154256018133752)
A_schd      = (0.008964973333333334, 0.00469251519619617)
B           = (-1.1028802614285715, 1.3847103792730167)
B_550       = (-1.957753635, 2.322456901934998)
B_schd      = (0.03695090333333334, 0.8579963617907596)
'''