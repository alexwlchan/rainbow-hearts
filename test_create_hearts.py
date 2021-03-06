#!/usr/bin/env python

import pytest

from create_hearts import inner_stripes, outer_stripes, middle_stripes


def test_stripe_filters():
    assert inner_stripes([1, 2, 3, 4, 5]) == [4, 5]
    assert outer_stripes([1, 2, 3, 4, 5]) == [1, 2]
    assert middle_stripes([1, 2, 3, 4, 5]) == [3]

    assert inner_stripes([1, 2, 3, 4]) == [3, 4]
    assert outer_stripes([1, 2, 3, 4]) == [1, 2]
    assert middle_stripes([1, 2, 3, 4]) == []
