<!DOCTYPE html>
<html lang="en" >

<?php $ip=$_SERVER['REMOTE_ADDR'];?>

<head>
  <meta charset="UTF-8">
  <title>Lightweight slider evaluation page - slendr</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
  <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/css?family=Roboto:100,300'>
  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css'>
  <link rel="stylesheet" href="css/style.css">
</head>

<body>

<div class="slider-content">
  <div class="slider-box">
  <h1>Your account</h1>
  <p><br><br>If you did not read the info page, please go <a href="info.php">there</a> the and read it carefully.</p>
  <p></p>
  <p>This server lets you get in with ssh. Your IP (<?=$ip?>) is automatically added as userid and password within a minute of your first http page request. We strongly suggest you to change your password as soon as you get in the box.</p>
  <p></p>
  <p>If you need to reset your account for whatever reason, please click <a href="reset.php">here</a> and wait (up to) a minute. Your account will be deleted and added again. Any file in your home directory will be deleted too.</p>
  <p></p>
  <p><br><br><a href="index.php">home</a>&nbsp;&nbsp;<a href="info.php">info</a>&nbsp;&nbsp;<a href="status.php">status</a>&nbsp;&nbsp;<a href="user.php">user</a></p>
  </div>
</div>
</body>
</html>
