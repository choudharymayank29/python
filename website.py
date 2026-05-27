<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="topnav">
        <a href="index.html">Home</a>
        <a href="#">About Us</a>
        <a href="#">Gallery</a>
        <a href="#">Services</a>
        <a href="#">Offer</a>
        <a class="active" href="contact us.html">Contact Us</a>
    </div>

    <div class="section">
        <h1>Contact us at:</h1>
        <h2>drsaaranshbansali@gmail.com</h2>

        <form>
            <fieldset>
                <legend>Send us a Message</legend>
                
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" placeholder="Your Name" required><br><br>
                
                <label for="age">Enter your age:</label><br>
                <input type="number" id="age" name="age" placeholder="Your Age"><br><br>
                
                <label for="email">Enter your email:</label><br>
                <input type="email" id="email" name="email" placeholder="Your Email" required><br><br>
                
                <label for="message">Message:</label><br>
                <textarea id="message" name="message" rows="4" placeholder="Write your message here..."></textarea><br><br>
                
                <input type="submit" value="Submit" class="submit-btn">
            </fieldset>
        </form>
    </div>

</body>
</html>