default_carbon_intensity_factor = 519
kWh_per_byte_data_center = 7.20E-11
kWh_per_byte_network_wireless = 1.52E-07
kWh_per_minute_laptop = 3.2E-04

def carbon_intensity_factor(location):
    return default_carbon_intensity_factor

def kWh_per_byte_network(network_type):
    return kWh_per_byte_network_wireless

def kWh_per_minute(device_type):
    return kWh_per_minute_laptop

def action(*, duration=0, data=0, location=None, device_type=None, network_type=None):
    kWh_data_center = data * kWh_per_byte_data_center
    gCO2_data_center = kWh_data_center * default_carbon_intensity_factor

    kWh_network = data * kWh_per_byte_network(network_type)
    gCO2_network = kWh_network * default_carbon_intensity_factor

    kWh_device = duration * kWh_per_minute(device_type)
    gCO2_device = kWh_device * carbon_intensity_factor(location)
    
    return {
        "kWh_total": kWh_data_center + kWh_network + kWh_device,
        "gCO2_total": gCO2_data_center + gCO2_network + gCO2_device
    }
