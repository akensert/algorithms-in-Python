import numpy as np
from typing import List, Tuple, Optional, Union, Callable, Any
import warnings

warnings.filterwarnings('ignore')
np.set_printoptions(suppress=True)


class ParticleSwarm():
    """Implementation of a particle swarm optmiization algorithm, that
    takes advantage of Numpy broadcasting"""

    def __init__(self,
                 num_particles: int = 100,
                 w: float = 1.0,
                 c1: float = 0.5,
                 c2: float = 0.5,
                 bounds: Optional[Tuple[Optional[float]]] = None,
                 patience: int = 200,
                 max_iter: Optional[int] = None,
                 verbose: Union[bool, int] = 1) -> None:

        self.num_particles = num_particles
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.bounds = bounds or [None, None]
        self.patience = patience
        self.max_iter = (max_iter or float('inf'))
        self.verbose = verbose


    def _initialize_particles(self,
                              p0: List[Tuple[float]],
                              v0: List[Tuple[float]]
                              ) -> Tuple[np.ndarray, np.ndarray]:
        dim = (self.num_particles, len(p0))
        p_pos = np.random.uniform(
            low=[p[0] for p in p0], high=[p[1] for p in p0], size=dim)
        p_vel = np.random.uniform(
            low=[v[0] for v in v0], high=[v[1] for v in v0], size=dim)
        return p_pos, p_vel

    def _update_velocity(self,
                         p_vel: np.ndarray,
                         p_pos: np.ndarray,
                         p_best_pos: np.ndarray,
                         g_best_pos: np.ndarray
                         ) -> np.ndarray:
        r1, r2 = np.random.uniform(0, 1, size=(2))
        cog_acc = self.c1 * r1 * (p_best_pos - p_pos)
        soc_acc = self.c2 * r2 * (g_best_pos - p_pos)
        return (self.w * p_vel) + cog_acc + soc_acc

    def _update_position(self,
                         p_pos: np.ndarray,
                         p_vel: np.ndarray
                         ) -> np.ndarray:
        p_pos_updated = p_pos + p_vel
        p_pos_updated = p_pos_updated.reshape(-1)
        p_vel = p_vel.reshape(-1)

        if self.bounds[0] is not None:
            # update new position, with upper bounds
            p_pos_updated = np.where(
                p_pos_updated > self.bounds[0], p_pos_updated-(2*p_vel), p_pos_updated)

        if self.bounds[1] is not None:
            # update new position, with lower bounds
            p_pos_updated = np.where(
                p_pos_updated < self.bounds[1], p_pos_updated-(2*p_vel), p_pos_updated)

        p_pos_updated = p_pos_updated.reshape((self.num_particles, -1))

        return p_pos_updated

    def fit(self,
            obj_fn: Callable,
            p0: List[Tuple[float]],
            v0: List[Tuple[float]],
            args: Union[List[Any], Tuple[Any]] = ()
            ) -> np.ndarray:

        self.p_pos, self.p_vel = self._initialize_particles(p0, v0)

        self.p_best_pos = np.zeros(self.p_pos.shape)
        self.p_best_obj_val = np.full((self.p_pos.shape[0],), np.inf)
        self.g_best_pos = np.zeros((self.p_pos.shape[1]))
        self.g_best_obj_val = np.inf

        k = 1
        iters_with_no_improvement = 0
        while (self.patience - iters_with_no_improvement) and k <= self.max_iter:

            obj_val = obj_fn(self.p_pos, *args)
            obj_val_improved = obj_val < obj_fn(self.p_best_pos, *args)

            self.p_best_pos[obj_val_improved] = self.p_pos[obj_val_improved]
            self.p_best_obj_val[obj_val_improved] = obj_val[obj_val_improved]

            self.iter_best = self.p_best_obj_val.min()
            if self.iter_best < self.g_best_obj_val:
                self.g_best_pos = self.p_best_pos[np.argmin(self.p_best_obj_val)]
                self.g_best_obj_val = self.iter_best
                iters_with_no_improvement = 0
            else:
                iters_with_no_improvement += 1

            if self.verbose:
                template = "Iter {:05d} : Best particle MAE {:.7f} : "
                template += "Params [" + "{:.3f} " * len(self.g_best_pos) + "]"
                print(template.format(k, self.g_best_obj_val, *self.g_best_pos), end='\r')

            self.p_vel = self._update_velocity(
                self.p_vel, self.p_pos, self.p_best_pos, self.g_best_pos)

            self.p_pos = self._update_position(
                self.p_pos, self.p_vel)

            if self.max_iter and k >= self.max_iter:
                break

            k += 1

        return self.g_best_pos


if __name__ == '__main__':

    X, y = np.random.multivariate_normal(
        mean=[5, 0], cov=[[1.0, 0.9], [0.9, 1.0]], size=1000).T

    ps = ParticleSwarm(
        num_particles=1000,
        w=1.0,
        c1=0.5,
        c2=0.5,
        bounds=None,
        patience=100,
        max_iter=None,
        verbose=1
    )

    def obj_fn(params, X, y):
        # params.T[..., np.newaxis].shape = (num_params, num_particles, 1)
        theta1, theta0 = params.T[..., np.newaxis]
        y_hat = X * theta1 + theta0
        return np.mean(np.square(y - y_hat), axis=1)

    params = ps.fit(
        obj_fn=obj_fn,
        p0=[(-1, 1), (-1, 1)],
        v0=[(0, 0), (0, 0)],
        args=(X, y)
    )


    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('TkAgg')

        plt.scatter(X, y)
        linspace = np.linspace(X.min(), X.max(), 1000)
        plt.plot(linspace, params[0] * linspace + params[1], color='red',
                 label="y = x * {:.4f} + {:.4f}".format(params[0], params[1]))
        plt.legend(fontsize=14)
        plt.show(block=True);
    except:
        print("\ny = x * {:.4f} + {:.4f}".format(params[0], params[1]))
