<?php

if (!empty($_POST)) {
   $name = $_POST['name'];
   $email = $_POST['email'];
   $message = $_POST['message'];


   $toEmail = 'sales@floraextracts.us';
   $emailSubject = 'Enquiry from website';
   $headers = ['From' => $email, 'Reply-To' => $email, 'Content-type' => 'text/html; charset=utf-8'];
   $bodyParagraphs = ["Name: {$name}", "Email: {$email}", "Message:", $message];
   $body = join(PHP_EOL, $bodyParagraphs);

   if (mail($toEmail, $emailSubject, $body, $headers)) {
       echo '<script>alert("Thank you for reaching out to us. We will be in touch shortly.")</script>';
       header('Location: thank-you.html');
   } else {
       $errorMessage = 'Oops, something went wrong. Please try again later';
   }

}

?>
