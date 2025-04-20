<!DOCTYPE html>
<html>
<head>
    <title>Currency Converter</title>
</head>
<body>
    <h2>Currency Converter</h2>
    <form action="output.jsp" method="post">
        Amount: <input type="text" name="amount" required><br><br>
        From: <input type="text" name="from" placeholder="e.g. USD"><br><br>
        To: <input type="text" name="to" placeholder="e.g. INR"><br><br>
        <input type="submit" value="Convert">
    </form>
</body>
</html>
