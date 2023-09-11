async function getDevices(){
    try {
        const devices = await navigator.bluetooth.getDevices();
        return devices;
    } catch(error){
        console.log(error)
        return [];
    }
}

async function addNewDevice(n_clicks) {
  try {
    console.log("Requesting any Bluetooth device...");
    if (n_clicks > 0){
        const device = await navigator.bluetooth.requestDevice({
        // filters: [...] <- Prefer filters to save energy & show relevant devices.
        acceptAllDevices: true,
        });
    }   

    // return JSON.stringify({
    //     id: device.id,
    //     name: device.name,
    // })
    console.log(device);
    const devices = await getDevices();
    //const devices = [device];
    // console.log(devices);
    const json_devices = devices.map(function(device){
        return {name: device.name, id: device.id}
    })
    return json_devices;
  } catch (error) {
    console.log("No device selected")
  }
}

window.dash_clientside = Object.assign({}, window.dash_clientside, {
  bluetooth: {
    add_new_device: async function(n_clicks){
        return await addNewDevice(n_clicks)
    }
  },
});
