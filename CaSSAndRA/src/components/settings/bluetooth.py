from dash import clientside_callback, ClientsideFunction, Input, Output, html, dcc, callback
import dash_bootstrap_components as dbc
from .. import ids

addbluetoothdevicebutton = dbc.Button('Select Device', color='primary', className='m-1', id=ids.BUTTONADDBLUETOOTHDEVICE, n_clicks=0)

connected_bt_devices_list = html.Div([html.Div(id="connected-bt-devices"),
                                    dcc.Store(id="connected-bt-devices-store",
                                              storage_type='local')
                                          ]
                                          )

clientside_callback(
    ClientsideFunction(
        namespace='bluetooth',
        function_name='add_new_device'
    ),
    Output('connected-bt-devices-store', 'data'),
    Input(ids.BUTTONADDBLUETOOTHDEVICE, 'n_clicks')
)

@callback(
    Output('connected-bt-devices', 'children'),
    Input('connected-bt-devices-store', 'data')
)
def update_connected_bt_devices(data):
    print(data)
    print(len(data))
    items = []
    for device in data:
        if 'name' in device:
            items.append(html.P(device['name']))
    return items