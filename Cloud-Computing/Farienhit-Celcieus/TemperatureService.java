package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

@WebService(serviceName = "TemperatureService")
public class TemperatureService {

    @WebMethod(operationName = "fahrenheitToCelsius")
    public double fahrenheitToCelsius(@WebParam(name = "f") double f) {
        return (f - 32) * 5 / 9;
    }

    @WebMethod(operationName = "celsiusToFahrenheit")
    public double celsiusToFahrenheit(@WebParam(name = "c") double c) {
        return (c * 9 / 5) + 32;
    }
}
