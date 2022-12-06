import alerter
import configuration

def testing():
    alerter.alert_in_celcius(303.6)  
    alerter.alert_in_celcius(392)    
    alerter.alert_in_celcius(400.5)  
    assert(configuration.alert_failure_count==1)
    return "Success!"

     
if __name__ == "__main__":
   print("All is well")
