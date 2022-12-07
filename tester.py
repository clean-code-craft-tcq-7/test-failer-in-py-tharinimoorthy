from alerter import *
import configuration
def testing():
     alert_in_celcius(100.5)  
     alert_in_celcius(303)    
     alert_in_celcius(400)  
     assert(configuration.alert_failure_count==1)
     return "Success!"

      
if __name__ == "__main__":
     testing()
     print("All is well")    

