<?php
       header('Content-Type:application/json');

       $data = array();
       $data = json_decode(file_get_contents('php://input'), true);

       $json = json_encode($data);

       $url = 'http://localhost:8080/post_review';
       $header = array("Content-Type: application/json");

       $ch = curl_init();
       curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
       curl_setopt($ch, CURLOPT_URL, $url);
       curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
       curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
       curl_setopt($ch, CURLOPT_TIMEOUT, 75);
       curl_setopt($ch, CURLOPT_POST, 1);
       curl_setopt($ch, CURLOPT_POSTFIELDS, $json);

       $result = curl_exec($ch);
       curl_close($ch);
       
       echo $result;
