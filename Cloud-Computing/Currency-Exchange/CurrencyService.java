package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

@WebService(serviceName = "CurrencyService")
public class CurrencyService {

    @WebMethod(operationName = "convert")
    public double convert(@WebParam(name = "amount") double amount,
                          @WebParam(name = "from") String from,
                          @WebParam(name = "to") String to) {
        double rate = getConversionRate(from, to);
        return amount * rate;
    }

    private double getConversionRate(String from, String to) {
        if (from.equalsIgnoreCase("USD") && to.equalsIgnoreCase("INR")) return 83.0;
        if (from.equalsIgnoreCase("INR") && to.equalsIgnoreCase("USD")) return 0.012;
        if (from.equalsIgnoreCase("EUR") && to.equalsIgnoreCase("INR")) return 89.0;
        if (from.equalsIgnoreCase("INR") && to.equalsIgnoreCase("EUR")) return 0.011;
        return 1.0; // default fallback
    }
}
