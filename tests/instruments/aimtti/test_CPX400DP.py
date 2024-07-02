#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2024 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import pytest

from pymeasure.test import expected_protocol
from pymeasure.instruments.aimtti.aimttiCPX import AimttiCPX400DP


def test_voltage_setpoint():
    with expected_protocol(
        AimttiCPX400DP,
        [("V1V 0.1", None),
         ("V1?", "V1 0.1")
         ],
    ) as inst:
        inst.ch_1.voltage_setpoint = 0.1
        assert inst.ch_1.voltage_setpoint == 0.1


def test_current_limit():
    with expected_protocol(
        AimttiCPX400DP,
        [("I2 5", None),
         ("I2?", "I2 5")
         ],
    ) as inst:
        inst.ch_2.current_limit = 5
        assert inst.ch_2.current_limit == 5
