import alerter
import configuration

def testing():
    alerter.alert_in_celcius(303.6)  
    alerter.alert_in_celcius(231)    
    alerter.alert_in_celcius(500)  
    assert(configuration.alert_failure_count==1)
    return "Success!"

     
if __name__ == "__main__":
    testing()
    print("All is well")
