
    import numpy as np
    from scipy import stats

    O = np.array([52.09,54.46,52.68,51.68,53.83,47.21,44.36])
    Pr = 1/7
    n = O.sum()
    E = n * Pr
    df = len(O)-1

    chi2, p = stats.chisquare(O,E)
    print (" Chi-squared test for given probabilities",
            "\n","\n",
            "Chi-Squared :", round(chi2,4),"\n",
            "df :",df,"\n",
            "P-Value :",round(p,4))



    import numpy as np
    from scipy import stats

    O = np.array([19,32,22,7])
    Pr0 = stats.binom.pmf(0,3,0.4)
    Pr1 = stats.binom.pmf(1,3,0.4)
    Pr2 = stats.binom.pmf(2,3,0.4)
    Pr3 = stats.binom.pmf(3,3,0.4)
    Pr = np.array([Pr0,Pr1,Pr2,Pr3])
    Pr
    n = O.sum()
    E = n * Pr

    chisq = sum(( O - E )**2 / E )
    chisq
    1-stats.chi2.cdf(chisq, df = 2)



    import numpy as np
    from scipy import stats

    bone = np.array([[38,15,7],[22,32,16],[15,30,25]])
    row_names    = ['Nothing', 'Phisical','Excercise']
    column_names = ['loss', 'little', 'increase']

    chi22, p2, dof, expected = stats.chi2_contingency(bone)
    print (" Pearson's Chi-squared test","\n","\n",
            "Chi-Squared :",round(chi22,4),"\n",
            "df :",dof,"\n",
            "P-Value :", round(p2, 4))



    import numpy as np
    from scipy import stats

    control = np.array([[9, 9], [8, 12], [3, 14]])
    row_names = ['good', 'normal', 'poor']
    column_names = ['continue', 'stop']

    chi22, p2, dof, expected = stats.chi2_contingency(control)
    print(" Pearson's Chi-squared test", "\n", "\n",
          "Chi-Squared :", round(chi22, 4), "\n",
          "df :", dof, "\n",
          "P-Value :", round(p2, 4))
