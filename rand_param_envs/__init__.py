from rand_param_envs.base import MetaEnv
from rand_param_envs.gym.envs.registration import register

register(
    id='WalkerRandParams-v0',
    entry_point='rand_param_envs.walker_rand_params:Walker2DRandParamsEnv',
)