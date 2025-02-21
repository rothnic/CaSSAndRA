from dash import html, dcc, Input, Output, State, callback, ctx
import dash_bootstrap_components as dbc
import time

from src.components import ids
from . import buttons
from src.backend.data.mapdata import current_map, current_task, tasks

tasksorder = dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Tasks'),
                        dbc.CardBody([
                            dcc.Dropdown(
                                id=ids.DROPDOWNTASKSORDER, 
                                className='m-1', 
                                multi=True, 
                            ),
                            dbc.Container([
                                    buttons.starttasksorder,
                                    buttons.loadtasksorder,
                                    buttons.renametask,
                                    buttons.savenewtask, 
                                    buttons.removetask, 
                                    buttons.copytask,
                            ], fluid=True),                       
                        ]), 
                    ], className='text-center m-1 w-90')
                ])

@callback(Output(ids.DROPDOWNTASKSORDER, 'options'),
          [Input(ids.OKBUTTONSRRENAMETASK, 'n_clicks'),
           Input(ids.OKBUTTONSAVECURRENTTASK, 'n_clicks'),
           Input(ids.OKBUTTONSREMOVETASK, 'n_clicks'),
           Input(ids.OKBUTTONCOPYTASK, 'n_clicks'),
           Input(ids.URLUPDATE, 'pathname'),
           State(ids.DROPDOWNTASKSORDER, 'options')])
def update_dropdown_tasksorder(bokrt_nclicks: int, bokst_nclicks: int, bokdt_nclicks: int, 
                               bokct_nclicks: int, pathname: str, dropdown_opt_state: list()) -> list():
    time.sleep(0.5)
    context = ctx.triggered_id
    try:
        filtered_tasks = tasks.saved[tasks.saved['map name'] == current_map.name]
        options = filtered_tasks.name.unique() 
    except:
        options = []
    if options == []:
        current_task.create()
    return options