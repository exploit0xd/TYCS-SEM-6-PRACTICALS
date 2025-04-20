package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

@WebService(serviceName = "MathService")
public class MathService {

    /**
     * Web service operation to check if a number is prime
     */
    @WebMethod(operationName = "isPrime")
    public boolean isPrime(@WebParam(name = "number") int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    /**
     * Web service operation to calculate the factorial of a number
     */
    @WebMethod(operationName = "factorial")
    public long factorial(@WebParam(name = "number") int number) {
        if (number < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }
        long result = 1;
        for (int i = 1; i <= number; i++) {
            result *= i;
        }
        return result;
    }
}
