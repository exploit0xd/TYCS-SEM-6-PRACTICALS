<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
</head>
<body>
    <h2>Temperature Converter</h2>
    <form action="output.jsp" method="post">
        Enter Value: <input type="text" name="value" required><br><br>
        Convert: 
        <select name="type">
            <option value="toCelsius">Fahrenheit to Celsius</option>
            <option value="toFahrenheit">Celsius to Fahrenheit</option>
        </select><br><br>
        <input type="submit" value="Convert">
    </form>
</body>
</html>
