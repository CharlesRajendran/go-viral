<?php

    header('Content-Type:application/json');
    
    $data = array();
    $data = json_decode(file_get_contents('php://input'), true);

    $json = json_encode($data);
    
    $url = 'http://localhost:8080/visualise_terms';
        
    $ch = curl_init(); 
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    
    $result=curl_exec($ch);
    curl_close($ch);
    
    echo $result;