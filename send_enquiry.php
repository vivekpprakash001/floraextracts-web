<?php

$to = 'sales@floraextracts.us';
$subject = 'Enquiry from website';

$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$bodyParagraphs = ["Name: {$name}", "Email: {$email}", "Message:", $message];
$body = join(PHP_EOL, $bodyParagraphs);

$headers = "From: $email";

if(mail($to, $subject, $body, $headers)) {
    echo '<script>alert("Thank you for reaching out to us. We will be in touch shortly.")</script>';
    header('Location: contact.html');
} else {
    echo "Mail sending failed.";
}

?>
