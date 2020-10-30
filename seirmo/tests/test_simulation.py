#
# This file is part of seirmo (https://github.com/SABS-R3-Epidemiology/seirmo/)
# which is released under the BSD 3-clause license. See accompanying LICENSE.md
# for copyright notice and full license details.
#

import numpy as np

import unittest
import seirmo as se


class TestSimulationController(unittest.TestCase):
    """
    Test the 'SimulationController' class.
    """
    def test__init__(self):
        start = 0
        end = 10
        n_times = 10
        with self.assertRaises(TypeError):
            se.SimulationController('ForwardModel', start, end, n_times)

    def test_run(self):

        n_outputs = 4

        start = 0
        end = 10
        n_times = 10
        model = se.SEIRModel()
        simulation = se.SimulationController(model, start, end, n_times)

        initial_values = [0.9, 0, 0.1, 0]
        constants = [1, 1, 1]
        test_parameters = initial_values + constants
        output = simulation.run(test_parameters)

        # Check output shape
        self.assertEqual(output.shape, (n_times, n_outputs))

        # Check that sum of states is one at all times
        total = np.sum(output, axis=1)
        expected = np.ones(shape=n_times)
        np.testing.assert_almost_equal(total, expected)


if __name__ == '__main__':
    unittest.main()