import configuration
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius <= configuration.alert_threshold):
        return 200
    else:
        return 500
def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    temperature = network_alert_stub(celcius)
    if temperature != 200:
        configuration.alert_failure_count += 1
