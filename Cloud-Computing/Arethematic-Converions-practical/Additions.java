package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

@WebService(serviceName = "Addition")
public class Addition {

    @WebMethod(operationName = "add")
    public double add(@WebParam(name = "a") double a, @WebParam(name = "b") double b) {
        return a + b;
    }

    @WebMethod(operationName = "subtract")
    public int subtract(@WebParam(name = "a") int a, @WebParam(name = "b") int b) {
        return a - b;
    }

    @WebMethod(operationName = "multiply")
    public int multiply(@WebParam(name = "a") int a, @WebParam(name = "b") int b) {
        return a * b;
    }

    @WebMethod(operationName = "divide")
    public double divide(@WebParam(name = "a") int a, @WebParam(name = "b") int b) {
        if (b == 0) throw new IllegalArgumentException("Division by zero is not allowed.");
        return (double) a / b;
    }
}
