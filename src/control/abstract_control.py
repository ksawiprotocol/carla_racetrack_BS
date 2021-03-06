from abc import ABCMeta, abstractmethod
import numpy as np

class Controller(metaclass=ABCMeta):
    @abstractmethod
    def control(self, state, **kwargs):
        pass

    @staticmethod
    def _calc_closest_dists_and_location(actor_location_3D:np.array, pts_3D:np.array):
        dists = np.linalg.norm(pts_3D - actor_location_3D, axis=1)
        which_closest = np.argmin(dists)

        return which_closest, dists, actor_location_3D

