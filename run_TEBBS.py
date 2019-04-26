from TEBBS import TEBBS_calculate

# example of usage of TEBBS and printing out peak T with its error bounds
start_time = '2013-10-28T01:00:00'
end_time = '2013-10-28T02:30:00'
fluxes, Tarray, EMarray, timing, AFluxMax, AFluxTime, BFluxMax, BFluxTime, T, Tmin, Tmax, Ttime, EM, EMmin, EMmax, EMtime, tmin_test_flag, init_test_flag, rising_phase_bins = TEBBS_calculate(start_time, end_time, plot_key = 0, sys_win = 0, savitzky_golay = 0, extend_50 = 0)
print(T, Tmin, Tmax)