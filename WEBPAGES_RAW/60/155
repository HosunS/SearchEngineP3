<?php
  //Get the requested url from our proxy url
  $url = $_SERVER['QUERY_STRING'];

  // initialize curl with given url
  $ch = curl_init($url);

  //Tell curl to write the response to a variable
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

  //Tell curl to follow any redirects
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);

  $response = curl_exec($ch);

  $cType = curl_getinfo($ch,CURLINFO_CONTENT_TYPE);

  //Output the right mime/type
  header('Content-type: '.$cType);

  //Pass through the data 
  print $response;

  curl_close($ch);
?>

