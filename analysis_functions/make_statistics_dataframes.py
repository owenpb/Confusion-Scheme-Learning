import pandas as pd

def make_stats_csv(folder, save_csv=True):
    
    
    """
    Returns two separate dataframes of position-space data and momentum-space data. Each contains data for density-density correlation,
    two-point Green's function, pair Green's function, phonon Green's function, and spin-spin correlation, along with the standard error
    for these measurements. Optionally save dataframes in .csv format.
    
    
    Parameters
    ----------
    
    folder :
        Directory of output files produced by HMC simulation (at some particular fixed temperature).
    save_csv : bool
        If True, saves dataframes in .csv format.
        
        
    Returns
    -------
    
    position_stats_data : DataFrame
        pandas DataFrame of position-space measurements and their errors.
        
    momentum_stats_data : DataFrame
        pandas DataFrame of momentum-space measurements and their errors.
        
    
    """
    
    
    beta = folder.split('_')[2][1:]
    
    # Position space stats files:
    
    DenDen_position_stats_file = folder + "/DenDen_position_stats.out"
    Greens_position_stats_file = folder + "/Greens_position_stats.out"
    PairGreens_position_stats_file = folder + "/PairGreens_position_stats.out"
    PhononGreens_position_stats_file = folder + "/PhononGreens_position_stats.out"
    SpinSpin_position_stats_file = folder + "/SpinSpin_position_stats.out"
    
    
    # Momentum space stats files:
    
    DenDen_momentum_stats_file = folder + "/DenDen_momentum_stats.out"
    Greens_momentum_stats_file = folder + "/Greens_momentum_stats.out"
    PairGreens_momentum_stats_file = folder + "/PairGreens_momentum_stats.out"
    PhononGreens_momentum_stats_file = folder + "/PhononGreens_momentum_stats.out"
    SpinSpin_momentum_stats_file = folder + "/SpinSpin_momentum_stats.out"
    
    
    # Make individual position space dataframes:
    
    DenDen_position_stats_data = pd.read_csv(DenDen_position_stats_file, sep=' ')
    Greens_position_stats_data = pd.read_csv(Greens_position_stats_file, sep=' ')
    PairGreens_position_stats_data = pd.read_csv(PairGreens_position_stats_file, sep=' ')
    PhononGreens_position_stats_data = pd.read_csv(PhononGreens_position_stats_file, sep=' ')
    SpinSpin_position_stats_data = pd.read_csv(SpinSpin_position_stats_file, sep=' ')
    
    
    # Make individual momentum space dataframes:

    DenDen_momentum_stats_data = pd.read_csv(DenDen_momentum_stats_file, sep=' ')
    Greens_momentum_stats_data = pd.read_csv(Greens_momentum_stats_file, sep=' ')
    PairGreens_momentum_stats_data = pd.read_csv(PairGreens_momentum_stats_file, sep=' ')
    PhononGreens_momentum_stats_data = pd.read_csv(PhononGreens_momentum_stats_file, sep=' ')
    SpinSpin_momentum_stats_data = pd.read_csv(SpinSpin_momentum_stats_file, sep=' ')
    
    
    # Rename error columns:
    
    DenDen_position_stats_data.rename(columns={"error":"DenDen_error"}, inplace=True)
    Greens_position_stats_data.rename(columns={"error":"Greens_error"}, inplace=True)
    PairGreens_position_stats_data.rename(columns={"error":"PairGreens_error"}, inplace=True)
    PhononGreens_position_stats_data.rename(columns={"error":"PhononGreens_error"}, inplace=True)
    SpinSpin_position_stats_data.rename(columns={"error":"SpinSpin_error"}, inplace=True)
    
    
    # Rename error columns:
    
    DenDen_momentum_stats_data.rename(columns={"error":"DenDen_error"}, inplace=True)
    Greens_momentum_stats_data.rename(columns={"error":"Greens_error"}, inplace=True)
    PairGreens_momentum_stats_data.rename(columns={"error":"PairGreens_error"}, inplace=True)
    PhononGreens_momentum_stats_data.rename(columns={"error":"PhononGreens_error"}, inplace=True)
    SpinSpin_momentum_stats_data.rename(columns={"error":"SpinSpin_error"}, inplace=True)
    
    
    # Concatenate dataframes (position space data):
    
    position_stats_data = pd.concat([DenDen_position_stats_data, 
                  Greens_position_stats_data["Greens"],
                  Greens_position_stats_data["Greens_error"],
                  PairGreens_position_stats_data["PairGreens"],
                  PairGreens_position_stats_data["PairGreens_error"],
                  PhononGreens_position_stats_data["PhononGreens"],
                  PhononGreens_position_stats_data["PhononGreens_error"],
                  SpinSpin_position_stats_data["SpinSpin"],
                  SpinSpin_position_stats_data["SpinSpin_error"]
                 ], axis=1)
    
    
    # Concatenate dataframes (momentum space data):

    momentum_stats_data = pd.concat([DenDen_momentum_stats_data, 
                  Greens_momentum_stats_data["Greens"],
                  Greens_momentum_stats_data["Greens_error"],
                  PairGreens_momentum_stats_data["PairGreens"],
                  PairGreens_momentum_stats_data["PairGreens_error"],
                  PhononGreens_momentum_stats_data["PhononGreens"],
                  PhononGreens_momentum_stats_data["PhononGreens_error"],
                  SpinSpin_momentum_stats_data["SpinSpin"],
                  SpinSpin_momentum_stats_data["SpinSpin_error"]
                 ], axis=1)
    
    
    # Save dataframes to csv:
    
    if save_csv:
    
        position_stats_data.to_csv('square_L12_beta'+beta+'_w1_ld025_position_stats_data.csv')
        momentum_stats_data.to_csv('square_L12_beta'+beta+'_w1_ld025_momentum_stats_data.csv')
    
    return position_stats_data, momentum_stats_data