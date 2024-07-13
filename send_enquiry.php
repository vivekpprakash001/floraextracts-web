<?php

$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$toEmail = 'sales@floraextracts.us';
$emailSubject = 'Enquiry from website';
$headers = ['From' => $email, 'Reply-To' => $email, 'Content-type' => 'text/html; charset=utf-8'];

echo "<script>alert(' .$emailSubject. ')</script>";

?>
