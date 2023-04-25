
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap
from tests.apibase import APIBase


obj = APIBase('torch.nn.AvgPool2d')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        import torch.nn as nn
        input = torch.tensor([[[[-0.5743,  0.4889, -0.0878,  0.4210, -0.0844],
            [ 0.3614,  0.8458, -0.6152,  0.6894,  0.2927],
            [-0.0087,  0.1098,  0.1783, -0.6953,  0.5519],
            [ 0.3789, -0.0560, -0.4090, -0.1070, -1.0139],
            [ 0.9204,  1.0817, -2.6126,  0.4244,  0.3272]]]])
        pool = torch.nn.AvgPool2d(3, stride=2)
        result = pool(input)
        '''
    )
    obj.run(pytorch_code,['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        import torch.nn as nn
        input = torch.tensor([[[[ 0.6430,  0.4511, -1.6757,  1.7116],
            [-0.2288, -0.4111, -1.3602,  0.2685],
            [ 0.2363,  1.9341,  0.8522, -0.1846],
            [ 1.6496, -0.0675, -0.7208, -1.0018]],

            [[-0.3183,  0.8029, -0.4993,  1.0598],
            [-0.4952, -0.9536,  0.1954,  0.0551],
            [ 1.2257,  0.7517,  0.4063, -1.2151],
            [-1.3562,  0.3547,  1.1147,  1.2898]],

            [[ 0.1205, -0.1889,  0.5086, -0.8080],
            [ 0.3156, -0.8298,  2.0242, -0.9184],
            [-0.4005,  1.3586,  0.6205, -0.7487],
            [ 1.6239,  0.2900,  0.9671,  1.2961]],

            [[-1.1996, -0.2201, -0.9466, -0.7264],
            [-0.0313,  0.8284, -0.3588,  1.3522],
            [-0.0991, -0.5112, -0.1785,  2.0903],
            [-1.3286, -0.9333, -0.1404,  1.2582]]]])
        pool = torch.nn.AvgPool2d(4, stride=2, padding=2)
        result = pool(input)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        import torch.nn as nn
        input = torch.tensor([[[[-0.5743,  0.4889, -0.0878,  0.4210, -0.0844],
            [ 0.3614,  0.8458, -0.6152,  0.6894,  0.2927],
            [-0.0087,  0.1098,  0.1783, -0.6953,  0.5519],
            [ 0.3789, -0.0560, -0.4090, -0.1070, -1.0139],
            [ 0.9204,  1.0817, -2.6126,  0.4244,  0.3272]]]])
        pool = torch.nn.AvgPool2d(3, stride=2, ceil_mode=True)
        result = pool(input)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        import torch.nn as nn
        input = torch.tensor([[[[-0.5743,  0.4889, -0.0878,  0.4210, -0.0844],
            [ 0.3614,  0.8458, -0.6152,  0.6894,  0.2927],
            [-0.0087,  0.1098,  0.1783, -0.6953,  0.5519],
            [ 0.3789, -0.0560, -0.4090, -0.1070, -1.0139],
            [ 0.9204,  1.0817, -2.6126,  0.4244,  0.3272]]]])
        pool = torch.nn.AvgPool2d(3, stride=2, ceil_mode=True, count_include_pad=False)
        result = pool(input)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        import torch.nn as nn
        input = torch.tensor([[[[ 0.6430,  0.4511, -1.6757,  1.7116],
            [-0.2288, -0.4111, -1.3602,  0.2685],
            [ 0.2363,  1.9341,  0.8522, -0.1846],
            [ 1.6496, -0.0675, -0.7208, -1.0018]],

            [[-0.3183,  0.8029, -0.4993,  1.0598],
            [-0.4952, -0.9536,  0.1954,  0.0551],
            [ 1.2257,  0.7517,  0.4063, -1.2151],
            [-1.3562,  0.3547,  1.1147,  1.2898]],

            [[ 0.1205, -0.1889,  0.5086, -0.8080],
            [ 0.3156, -0.8298,  2.0242, -0.9184],
            [-0.4005,  1.3586,  0.6205, -0.7487],
            [ 1.6239,  0.2900,  0.9671,  1.2961]],

            [[-1.1996, -0.2201, -0.9466, -0.7264],
            [-0.0313,  0.8284, -0.3588,  1.3522],
            [-0.0991, -0.5112, -0.1785,  2.0903],
            [-1.3286, -0.9333, -0.1404,  1.2582]]]])
        pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=1, ceil_mode=True, count_include_pad=False)
        result = pool(input)
        '''
    )
    obj.run(pytorch_code, ['result'])