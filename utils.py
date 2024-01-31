import os, requests
import numpy as np

def retrieve_data_orientation() -> np.array:
    """
    Retrieve Stringer et al. (2019) orientation data from OSF repository.

    Returns:
        dat (np.array): array of orientation data
    """
    fpath = "./data/stringer_orientations.npy"
    url = "https://osf.io/ny4ut/download"

    if not os.path.exists(fpath):
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            print("!!! Failed to download data !!!")
        else:
            if r.status_code != requests.codes.ok:
                print("!!! Failed to download data !!!")
            else:
                with open(fpath, "wb") as fid:
                    fid.write(r.content)

    dat = np.load('./data/stringer_orientations.npy', allow_pickle=True).item()
    return dat

def circular_encoding(angle: np.array) -> tuple[np.array, np.array]:
    """
    Encode an angle into a pair of coordinates using sine and cosine functions.
    Angle should be in radians.

    Args:
        angle (float): angle in radians

    Returns:
        x, y (float): coordinates
    """
    x = np.cos(angle)
    y = np.sin(angle)
    return x, y
