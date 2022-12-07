import alerter
import configuration
def testing():
     alerter.alert_in_celcius(350.5)  
     alerter.alert_in_celcius(393.6)    
     alerter.alert_in_celcius(400.6)   
     assert(configuration.alert_failure_count==1)
     return "Success!"

      
if __name__ == "__main__":
     testing()
     print("All is well")    
