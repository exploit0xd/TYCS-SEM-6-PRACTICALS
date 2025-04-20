<%@page import="client.CurrencyService_Service"%>
<%@page import="client.CurrencyService"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Converted Result</title>
</head>
<body>
<%
    try {
        double amount = Double.parseDouble(request.getParameter("amount"));
        String from = request.getParameter("from");
        String to = request.getParameter("to");

        CurrencyService_Service service = new CurrencyService_Service();
        CurrencyService port = service.getCurrencyServicePort();

        double result = port.convert(amount, from, to);

        out.println("<h2>Converted Amount: " + result + " " + to.toUpperCase() + "</h2>");
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
    }
%>
</body>
</html>
