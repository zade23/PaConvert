# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.backends.cudnn.benchmark")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        torch.backends.cudnn.benchmark = True
        """
    )
    obj.run(
        pytorch_code, ["result"], unsupport=True, reason="Now can only delete ast.Expr"
    )


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        torch.backends.cudnn.benchmark = False
        """
    )
    obj.run(
        pytorch_code, ["result"], unsupport=True, reason="Now can only delete ast.Expr"
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        print(torch.backends.cudnn.benchmark)
        """
    )
    obj.run(
        pytorch_code, ["result"], unsupport=True, reason="Now can only delete ast.Expr"
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        torch.backends.cudnn.benchmark
        """
    )
    obj.run(pytorch_code, expect_paddle_code="import paddle\n")