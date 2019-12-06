default_carbon_intensity_factor = 519
kWh_per_byte_data_center = 7.20e-11

kWh_per_byte_network_wired = 4.29e-10
kWh_per_byte_network_wireless = 1.52e-10
kWh_per_byte_network_mobile = 8.84e-10

kWh_per_minute_laptop = 3.2e-04
kWh_per_minute_mobile = 1.1e-04

def carbon_intensity_factor(location):
    return default_carbon_intensity_factor

def kWh_per_byte_network(network_type):
    if network_type == "wireless":
        return kWh_per_byte_network_wireless
    elif network_type == "wired":
        return kWh_per_byte_network_wired
    elif network_type == "mobile":
        return kWh_per_byte_network_mobile

    # By default, return wireless
    return kWh_per_byte_wireless

def kWh_per_minute(device_type):
    if network_type == "laptop":
        return kWh_per_minute_laptop
    elif network_type == "mobile":
        return kWh_per_minute_mobile

    # By default, return laptop
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
