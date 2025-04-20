<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Prime/Factorial Result</title>
</head>
<body>

<h2>Prime and Factorial Results</h2>

<%
    try {
        // Get the input number
        int num = Integer.parseInt(request.getParameter("num"));

        // Create a web service client
        client.MathService_Service service = new client.MathService_Service();
        client.MathService port = service.getMathServicePort();

        // Get results from the web service
        boolean isPrime = port.isPrime(num);
        long factorial = port.factorial(num);

        // Display the results
        out.println("<p>Number: " + num + "</p>");
        out.println("<p>Is Prime: " + (isPrime ? "Yes" : "No") + "</p>");
        out.println("<p>Factorial: " + factorial + "</p>");
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
    }
%>

</body>
</html>
