<?php

$to = 'sales@floraextracts.us';
$subject = 'Test Mail';
$message = 'This is a test message';
$headers = 'From: sender@example.com';

if(mail($to, $subject, $message, $headers)) {
    echo "Mail sent successfully.";
} else {
    echo "Mail sending failed.";
}

?>
