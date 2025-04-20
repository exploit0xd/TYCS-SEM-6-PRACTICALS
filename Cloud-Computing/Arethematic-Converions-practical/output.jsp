<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="client.Addition_Service"%>
<%@page import="client.Addition"%>
<!DOCTYPE html>
<html>
<head>
    <title>Output Page</title>
</head>
<body>
<h2>Arithmetic Operation Results</h2>

<%
    try {
        double a = Double.parseDouble(request.getParameter("num1"));
        double b = Double.parseDouble(request.getParameter("num2"));

        Addition_Service service = new Addition_Service();
        Addition port = service.getAdditionPort();

        double sum = port.add(a, b);
        double difference = port.subtract((int)a, (int)b);
        double product = port.multiply((int)a, (int)b);
        double quotient = (b != 0) ? port.divide((int)a, (int)b) : Double.NaN;

        out.println("<p>Addition Result: " + a + " + " + b + " = " + sum + "</p>");
        out.println("<p>Subtraction Result: " + a + " - " + b + " = " + difference + "</p>");
        out.println("<p>Multiplication Result: " + a + " * " + b + " = " + product + "</p>");
        out.println("<p>Division Result: " + a + " / " + b + " = " + (b != 0 ? quotient : "Cannot divide by zero") + "</p>");

    } catch (Exception ex) {
        out.println("<p style='color:red;'>Error: " + ex.getMessage() + "</p>");
    }
%>
</body>
</html>
