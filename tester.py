import alerter
import configuration
def testing():
     alerter.alert_in_celcius(200)  
     alerter.alert_in_celcius(300)    
     alerter.alert_in_celcius(400)  
     assert(configuration.alert_failure_count==1)
     return "Success!"

      
if __name__ == "__main__":
     testing()
     print("All is well")    
