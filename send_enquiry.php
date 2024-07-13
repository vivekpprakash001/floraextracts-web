<?php
if(isset($_POST["submit"])){
echo '<script type="text/javascript">
             alert("'.$email.'");
             window.location.href = "'.$goto_after_mail.'";
          </script>';

// Checking For Blank Fields..
if($_POST["name"]==""||$_POST["email"]==""||$_POST["message"]==""){
echo "Fill All Fields..";
}else{
// Check if the "Sender's Email" input field is filled out
$email=$_POST['eemail'];
// Sanitize E-mail Address
$email =filter_var($email, FILTER_SANITIZE_EMAIL);
// Validate E-mail Address
$email= filter_var($email, FILTER_VALIDATE_EMAIL);

if (!$email){
echo "Invalid Sender's Email";
}
else{
$subject = $_POST['ename']." Enquiry to Church";

$name = $_POST['ename'];
$email = $_POST['eemail'];
$message = $_POST['emessage'];

$email_message = "Enquiry details below.\n\n";
$email_message .= "Name : ".$name."\n";
$email_message .= "Email : ".$email."\n";
$email_message .= "Message : ".$message."\n";

$headers = 'From:'. $email; // Sender's Email

// Message lines should not exceed 150 characters (PHP rule), so wrap it
$message = wordwrap($message, 150);

$goto_after_mail="https://floraextracts.us/contact.html";

$reply_msg = "Enquiry Accepted";

mail("info@floraextracts.us", $subject, $email_message, $headers);

echo '<script type="text/javascript">
             alert("'.$reply_msg.'");
             window.location.href = "'.$goto_after_mail.'";
          </script>';

// header("Location: ".$goto_after_mail);

}
}
}
?>
