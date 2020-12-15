#
# This file is part of seirmo (https://github.com/SABS-R3-Epidemiology/seirmo/)
# which is released under the BSD 3-clause license. See accompanying LICENSE.md
# for copyright notice and full license details.
#

"""This is an app which shows forward simulation of the SEIR model
with fixed example data. To run the app, use ``python dash_app.py``.
"""

import numpy as np
import pandas as pd
import random
from dash.dependencies import Input, Output

import seirmo as se
from seirmo.apps import SimulationApp

app = SimulationApp()
data = pd.DataFrame({
            'Time': range(50),
            'Incidence Number': [random.randint(0, 100) for i in range(50)]
        })

model = se.SEIRModel()
parameter_name = ['Initial S', 'Initial E', 'Initial I', 'Initial R', 
                  'Infection Rate', 'Incubation Rate', 'Recovery Rate']
app.add_model(model, parameter_name)
app.add_data(data)

sliders = app.get_sliders_ids()

@app.app.callback(
        Output('fig', 'figure'),
        [Input(s, 'value') for s in sliders])
def update_simulation(*args):
    """
    Simulates the model for the current slider values and updates the
    plot in the figure.
    """
    parameters = args
    fig = app.update_simulation(*parameters)

    return fig


if __name__ == "__main__":
    app.app.run_server(debug=True)