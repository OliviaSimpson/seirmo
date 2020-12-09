#
# This file is part of seirmo (https://github.com/SABS-R3-Epidemiology/seirmo/)
# which is released under the BSD 3-clause license. See accompanying LICENSE.md
# for copyright notice and full license details.
#

import unittest
import seirmo as se


class TestSliderComponent(unittest.TestCase):
    """
    Test the '_SliderComponent' class.
    """
    def test__init__(self):
        se._SliderComponent()

    def test_add_slider(self):

        slider = se._SliderComponent()

        # Check input type
        with self.assertRaises(TypeError):
            slider.add_slider(1, 0, 1)

    def test_group_sliders(self):

        slider = se._SliderComponent()
        slider.add_slider('slider1', 0, 1)
        slider.add_slider('slider2', 0, 2)
        slider.add_slider('slider3', 0, 1)

        # Check group slider input
        with self.assertRaises(AssertionError):
            slider.group_sliders('3', '2')

        # Check slider group dictionary
        slider.group_sliders('slider1', 'group1')
        slider.group_sliders('slider2', 'group1')
        slider.group_sliders('slider3', 'group2')

        self.assertEqual(slider._group_ids['group1'], ['slider1', 'slider2'])
        self.assertEqual(slider._group_ids['group2'], ['slider3'])

    def test_slider_ids(self):

        slider = se._SliderComponent()
        slider.add_slider('1', 0, 1)
        slider.add_slider('2', 0, 2)

        self.assertEqual(slider.slider_ids(), ['1', '2'])

    def test_sliders_in_group(self):

        slider = se._SliderComponent()
        slider.add_slider('slider1', 0, 1)
        slider.add_slider('slider2', 0, 2)

        slider.group_sliders('slider1', 'group1')
        slider.group_sliders('slider2', 'group1')

        self.assertEqual(slider.sliders_in_group('group1'), ['slider1', 'slider2']) # noqa  


if __name__ == '__main__':
    unittest.main()
