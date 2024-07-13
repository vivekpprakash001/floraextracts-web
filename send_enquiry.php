<?php

$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$toEmail = 'sales@floraextracts.us';
$emailSubject = 'Enquiry from website';
$headers = ['From' => $email, 'Reply-To' => $email, 'Content-type' => 'text/html; charset=utf-8'];
$bodyParagraphs = ["Name: {$name}", "Email: {$email}", "Message:", $message];
$body = join(PHP_EOL, $bodyParagraphs);

echo "<script>alert(' .$body. ')</script>";

?>
