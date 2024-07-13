<?php

$to = 'sales@floraextracts.us';
$subject = 'Test Mail';

$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$headers = "From: $email";

if(mail($to, $subject, $message, $headers)) {
    echo "Mail sent successfully.";
} else {
    echo "Mail sending failed.";
}

?>
