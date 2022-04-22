from scipy.ndimage import filters as scifil
import numpy as np
from matplotlib import pyplot as plt

def compute_harris_response(im:np.ndarray,sigma:float=3)->np.ndarray:
    """
    Compute the Harris corner detector response function for each pixel in a graylevel image.
    """

    # derivatives:
    imx = np.zeros(im.shape)
    scifil.gaussian_filter(im, (sigma,sigma), (0,1), imx)
    imy = np.zeros(im.shape)
    scifil.gaussian_filter(im, (sigma,sigma), (1,0), imy)

    # compute components of the Harris matrix
    Wxx = scifil.gaussian_filter(imx*imx,sigma)
    Wxy = scifil.gaussian_filter(imx*imy,sigma)
    Wyy = scifil.gaussian_filter(imy*imy,sigma)

    # determinant and trace
    Wdet = Wxx*Wyy - Wxy * 2
    Wtr = Wxx + Wyy

    return Wdet / Wtr

def get_harris_points(harrisim:np.ndarray, min_dist:int=10, threshold:float=0.1)->list[np.ndarray]:
    """
    Return corners from a Harris response image
    `min_dist` is the minimum number of pixels separating corners and image boundary.
    """

    # find top corner candidates above a threshold
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1

    # get cordinates of candidates
    coords = np.array(harrisim_t.nonzero()).T

    # ... and their values
    candidate_values = [harrisim[c[0], c[1]] for c in coords]

    # sort candidates
    index = np.argsort(candidate_values)

    # store allowed point locations in np.array
    allowed_locations = np.zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1

    # select the best points taking min_dist into acount
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0], coords[i,1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[
                    (coords[i,0]-min_dist):(coords[i,0]+min_dist),
                    (coords[i,1]-min_dist):(coords[i,1]+min_dist)
                ] = 0
    return filtered_coords

def plot_harris_points(image:np.ndarray, filtered_coords:np.ndarray)->plt.Figure:
    """Plots corners found in image.

    Args:
        image (_type_): _description_
        filtered_coords (_type_): _description_
    """

    fig = plt.figure()
    plt.gray()
    plt.imshow(image)
    plt.plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords], '*')
    plt.axis('off')
    plt.show()

    return fig

'''
def get_descriptors(image:np.ndarray, filtered_coords:np.ndarray, wid:int=5)->list[np.ndarray]:
    """For each point return, pixel values around the point
    using a neighbourhood of width `2*wid+1`. (Assume points are
    extracted with `min_distance > wid`)

    Args:
        image (np.ndarray): _description_
        filtered_coords (np.ndarray): _description_
        wid (int, optional): _description_. Defaults to 5.
    """

    desc = []
    for coords in filtered_coords:
        patch = image[coords[0]-wid:coords[0]+wid+1, coords[1]-wid:coords[1]+wid+1].flatten()
    desc.append(patch)

    return desc

def match(desc1, desc2, threshold=0.5):
    """For each corner point descriptor in the first image,
    select its match to second image using normalized cross-correlation.

    Args:
        desc1 (_type_): _description_
        desc2 (_type_): _description_
        threshold (float, optional): _description_. Defaults to 0.5.

    Returns:
        _type_: _description_
    """

    n = len(desc1[0])

    # pair-wise distances

    return matchscores

def match_threshold(desc1, desc2, threshold=0.5):
    return matches_12

'''