from dash import html, Input, Output, State, callback, ctx
import dash_bootstrap_components as dbc

from src.backend.data.mapdata import mapping_maps
from .. import ids

#import map area
uploadsunrayfile = dbc.Button(class_name='mt-1 me-1 bi bi-filetype-txt', title='upload sunray file')
saveimportedperimeter = dbc.Button(id=ids.BUTTONSAVEIMPORTEDPERIMETER, class_name='mt-1 me-1 bi bi-cloud-plus', n_clicks=0, title='save imported perimeter')
okbuttonoverwriteperimter= dbc.Button('OK', id=ids.OKBUTTONOVERWRITEPERIMTER, class_name='ms-auto', n_clicks=0)

#select map area
selectperimeter = dbc.Button(id=ids.BUTTONSELECTPERIMETER, class_name='mt-1 me-1 bi bi-cloud-download', n_clicks=0, title='use selected perimeter')
removeperimeter = dbc.Button(id=ids.BUTTONREMOVEPERIMETER, class_name='mt-1 me-1 bi bi-cloud-minus', n_clicks=0, title='remove selected perimeter')
addnewperimeter = dbc.Button(id=ids.BUTTONADDNEWPERIMETER, class_name='mt-1 me-1 bi-file-earmark-plus', n_clicks=0, title='add new perimeter')
copyperimeter = dbc.Button(id=ids.BUTTONCOPYPERIMETER, class_name='mt-1 me-1 bi bi-clouds', n_clicks=0, title='copy perimeter')
finishfigure = dbc.Button(id=ids.BUTTONFINISHFIGURE, class_name='mt-1 me-1 bi bi-cloud-plus', disabled=False, title='finish and save')
okbuttonselectedperimeter = dbc.Button('OK', id=ids.OKBUTTONSELECTEDPERIMETER, class_name='ms-auto', n_clicks=0)

okbuttonnewperimeter = dbc.Button('OK', id=ids.OKBUTTONNEWPERIMETER, class_name='ms-auto', n_clicks=0)
okbuttoncopyperimeter = dbc.Button('OK', id=ids.OKBUTTONCOPYPERIMETER, class_name='ms-auto', n_clicks=0)
okbuttonremoveperimeter = dbc.Button('OK', id=ids.OKBUTTONREMOVEPERIMETER, class_name='ms-auto', n_clicks=0)
okbuttonfinishmapping = dbc.Button('OK', id=ids.OKBUTTONFINISHMAPPING, class_name='ms-auto', n_clicks=0)
okbuttonnofixsolution = dbc.Button('OK', id=ids.OKBUTTONNOFIXSOLUTION, class_name='ms-auto', n_clicks=0)

@callback(Output(ids.BUTTONSELECTPERIMETER, 'disabled'),
          Output(ids.BUTTONREMOVEPERIMETER, 'disabled'),
          Output(ids.BUTTONCOPYPERIMETER, 'disabled'),
          [Input(ids.DROPDOWNCHOOSEPERIMETER, 'value')])
def update_perimeter_select_buttons_disabled(dropdown: str()) -> list():
    if dropdown == None:
        return True, True, True
    else:
        return False, False, False

@callback(Output(ids.BUTTONMOVEPOINTS, 'disabled'),
          [Input(ids.MAPPINGMAP, 'figure')])
def update_button_move_points_disabled(figure: dict):
    if mapping_maps.build.empty and not 'shapes' in figure['layout']:
        return True
    elif mapping_maps.build[mapping_maps.build['type'] == 'edit'].empty and not 'shapes' in figure['layout']:
        return True
    else:
        return False

@callback(Output(ids.BUTTONMOVEPOINTS, 'active'),
          [Input(ids.BUTTONMOVEPOINTS, 'n_clicks'),
           State(ids.BUTTONMOVEPOINTS, 'active')])
def update_button_move_points(bmp_nclicks: int, bmp_state: bool):
    context = ctx.triggered_id
    if context == ids.BUTTONMOVEPOINTS and not bmp_state:
        return True
    else:
        False
