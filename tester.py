from alerter import *
import configuration
class Alerter:
    def testing():
        alert_in_celcius(200)  
        alert_in_celcius(300)    
        alert_in_celcius(400)  
        assert(configuration.alert_failure_count==1)
        return "Success!"

         
    if __name__ == "__main__":
        alerter = testing()
        print("All is well") 
