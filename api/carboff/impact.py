estimates = {
    "carbon_intensity_factor": {
        "default": 519,
        "us": 493,
        "cn": 681,
        "fr": 35
    },
    "kWh_per_byte": {
        "data_center": 7.20e-11,
        "network": {
            "wired": 4.29e-10,
            "wireless": 1.52e-10,
            "mobile": 8.84e-10
        }
    },
    "kWh_per_minute": {
        "laptop": 3.2e-04,
        "mobile": 1.1e-04
    }
}

# Different locations have different carbon intensities
def carbon_intensity_factor(location):
    data = estimates["carbon_intensity_factor"]
    if location in data:
        return data[location]
    
    return data["default"]

# Different network types use different amounts of electricity when sending a byte
def kWh_per_byte_network(network_type):
    data = estimates["kWh_per_byte"]["network"]
    if network_type in data:
        return data[network_type]

    # By default, return wireless
    return data["wireless"]

# Different devices consume electricity at different rates
def kWh_per_minute(device_type):
    data = estimates["kWh_per_minute"]
    if device_type in data:
        return data[device_type]

    # By default, return laptop
    return data["laptop"]

# Given all the data as parameter, do the calculations here
def action(*, duration=0, data=0, location=None, device_type=None, network_type=None):
    kWh_data_center = data * estimates["kWh_per_byte"]["data_center"]
    gCO2_data_center = kWh_data_center * carbon_intensity_factor(None)

    kWh_network = data * kWh_per_byte_network(network_type)
    gCO2_network = kWh_network * carbon_intensity_factor(None)

    kWh_device = duration * kWh_per_minute(device_type)
    gCO2_device = kWh_device * carbon_intensity_factor(location)
    
    return {
        "kWh_total": kWh_data_center + kWh_network + kWh_device,
        "gCO2_total": gCO2_data_center + gCO2_network + gCO2_device
    }
