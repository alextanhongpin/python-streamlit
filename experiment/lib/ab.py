import math
import statsmodels.stats.api as sm
import statsmodels.stats.power as sp


def sample_size_for_mean_difference(delta, std, power=0.8, alpha=0.05, sides=1):
    return math.ceil(
        sp.normal_sample_size_one_tail(
            delta, power, alpha / sides, std_null=std, std_alternative=None
        )
    )


def sample_size_for_proportions(
    p1, p2, alpha=0.05, power=0.8, alternative="two-sided", ratio=1
):
    return math.ceil(
        sm.samplesize_proportions_2indep_onetail(
            p2 - p1, p1, power=power, alpha=alpha, alternative=alternative, ratio=ratio
        )
    )


def analyze(count1, count2, nobs1, nobs2, alternative="two-sided"):
    stat, p_value = sm.test_proportions_2indep(
        count1, nobs1, count2, nobs2, return_results=False, alternative=alternative
    )
    return stat, p_value
