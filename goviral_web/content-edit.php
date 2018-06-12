<?php 
	include_once("templates/header.php");  
	include_once("templates/style.php"); 
    include_once("templates/logo.php");
?>


<?php

    // header('Content-Type:application/json');
    
    $data = array();
    $data = json_decode(file_get_contents('php://input'), true);

    $json = json_encode($data);
    
    $url = 'http://localhost:8080/recommendations';
        
    $ch = curl_init(); 
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    
    $result=curl_exec($ch);
    curl_close($ch);
    
    $resultArray = json_decode($result)->recommendation_list;
    $raw_content = json_decode($result)->raw_content;

    $sentence_array = explode('.',$raw_content);

    // print_r($sentence_array[0]);

    $string_recommendations = $resultArray->string_recommendations;
    $list_recommendations = $resultArray->list_recommendations;

    // print_r($raw_content);
    // print_r($string_recommendations);
    // print_r($list_recommendations);
?>

<h2 style="color:#333;text-decoration: underline;"> Word Suggestions</h2>

<?php 
    for($x=0;$x< count($sentence_array);$x++) {
        for($y=0;$y< count($list_recommendations);$y++){
            if(strpos($sentence_array[$x],$list_recommendations[$y]->original_word)){
?>
<div class="well content-editing-container">
    <div class="row">
        <div class="col-md-offset-1 col-md-1 classified-type" align="center"><?php echo $list_recommendations[$y]->rulenum ?></div>
        <div class="col-md-offset-1 col-md-4 original-editable"><?php echo str_replace($list_recommendations[$y]->original_word,'<strong><strike>'.$list_recommendations[$y]->original_word.'</strong></strike>', $sentence_array[$x]); ?></div>

        <div class="col-md-5 modified-content">
            
            <?php for($z=0;$z < count($list_recommendations[$y]->sugessions);$z++){ ?>    
            <div class="row">
                <div class="col-md-9">
                <?php echo str_replace($list_recommendations[$y]->original_word,'<span class="changed_words">'.$list_recommendations[$y]->sugessions[$z].'</span>', $sentence_array[$x]).'<br><br>'; ?>
                </div>
            </div>
            <?php } ?>
            
        </div>
    </div>
</div>

<?php
        } 
    }
}
?>

<div class="well content-editing-container">
<h2 style="color:#333;text-decoration: underline;"> General Tips</h2><br>

<?php for($ss=0;$ss<count($string_recommendations);$ss++){ ?>

    <div class="row">
        <div class="col-md-offset-1 col-md-1 classified-type" align="center"><?php echo $string_recommendations[$ss]->rulenum ?></div>
        <div class="col-md-offeset-1 col-md-8 general-rules">
                <h4 style="color: #445566;"><?php echo $string_recommendations[$ss]->message;  ?></h4><br>
        </div>
    </div>
<?php } ?>
</div>

    <div class="row" id="button-section">
        <div class="col-md-offset-8 col-md-4">
            <button class="btn btn-success full-button" onclick="window.location='./index.php'">Back</button>
        </div>
     </div>

<?php 
	include_once("templates/script.php");  
	include_once("templates/footer.php");  
?>