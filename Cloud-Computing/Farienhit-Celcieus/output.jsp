<%@page import="client.TemperatureService"%>
<%@page import="client.TemperatureService_Service"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Conversion Result</title>
</head>
<body>
    <h2>Result</h2>

<%
    try {
        double value = Double.parseDouble(request.getParameter("value"));
        String type = request.getParameter("type");

        client.TemperatureService_Service service = new client.TemperatureService_Service();
        client.TemperatureService port = service.getTemperatureServicePort();

        double result;
        if (type.equals("toCelsius")) {
            result = port.fahrenheitToCelsius(value);
            out.println("<p>" + value + "°F = " + result + "°C</p>");
        } else {
            result = port.celsiusToFahrenheit(value);
            out.println("<p>" + value + "°C = " + result + "°F</p>");
        }
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
    }
%>

</body>
</html>
