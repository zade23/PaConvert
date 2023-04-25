
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap

from tests.apibase import APIBase


class IntTensorAPI(APIBase):

    def __init__(self, pytorch_api) -> None:
        super().__init__(pytorch_api)

    def check(self, pytorch_result, paddle_result):
        if pytorch_result.requires_grad == paddle_result.stop_gradient:
            return False
        if str(pytorch_result.dtype)[6:] != str(paddle_result.dtype)[7:]:
            return False
        return True

obj = IntTensorAPI('torch.IntTensor')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.IntTensor(2, 3)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        shape = [2, 3]
        result = torch.IntTensor(*shape)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        dim1, dim2 = 2, 3
        result = torch.IntTensor(dim1, dim2)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        def fun(x: torch.IntTensor):
            return x * 2

        a = torch.IntTensor(3, 4)
        result = fun(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.IntTensor([[3, 4], [5, 8]])
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_6():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.tensor([[3, 4], [5, 8]], dtype=torch.int)
        result = torch.IntTensor(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_7():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.IntTensor((1, 2, 3))
        '''
    )
    obj.run(pytorch_code, ['result'])

def _test_case_8():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.IntTensor()
        '''
    )
    obj.run(pytorch_code, ['result'])