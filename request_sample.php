<?php

$to = 'sales@floraextracts.us';
$subject = 'Request For Free Sample from website';

$name = $_POST['name'];
$email = $_POST['email'];
$products = $_POST['products'];
$message = $_POST['message'];

$bodyParagraphs = ["Name: {$name}", "Email: {$email}", "Product: {$products}", "Message:", $message];
$body = join(PHP_EOL, $bodyParagraphs);

$headers = "From: $email";

if(mail($to, $subject, $body, $headers)) {
    echo '<script>alert("Thank you for reaching out to us. We will be in touch shortly.")</script>';
    header('Location: request_sample.html');
} else {
    echo "Mail sending failed.";
}

?>
