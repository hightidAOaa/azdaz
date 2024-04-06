<?php
$to = 'laja966@yahoo.com';
$subject = 'Test Email';
$message = 'This is a test email sent from a PHP script.';
$headers = 'From: sender@whoevaaa.com' . "\r\n" .
    'Reply-To: sender@whoevaaa.com' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

if (mail($to, $subject, $message, $headers)) {
    echo 'Email sent successfully.';
} else {
    echo 'Error sending email.';
}
?>