<?php 
	include_once("templates/header.php");  
	include_once("templates/style.php"); 
    include_once("templates/logo.php");
?>

<script type="text/javascript">
    function sendTweet(screen_name,review_url,movie_name){
        var content = "Check our review on "+movie_name+" in this link "+review_url;


        console.log("screen name is "+screen_name+" url "+content);
        $.post('http://localhost/goviral_web/curl/sentTweet.php',JSON.stringify({
            'screen_name':screen_name,
            'message':content
        }),function(res){
            console.log(res);
            document.getElementById('id_'+screen_name).value = 'Sent';
            document.getElementById('id_'+screen_name).disabled = true;
        });
    }
</script>


<div id="twitter_container">

<?php
        
    $url = 'http://localhost:8080/tweets';
        
    $ch = curl_init(); 
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    
    $result=curl_exec($ch);
    curl_close($ch);
    $data  = array();
    $data = json_decode($result);
    $tweets = array();
    $tweets = $data->tweets;
    $review_url = $data->review_url;

    $movie_name = $data->movie_name;
    
    for($x=0;$x<count($tweets);$x++){
    	$tweet = $tweets[$x]->tweet;
    	$screen_name = $tweets[$x]->screen_name;
    	$date_post = $tweets[$x]->created_at;
        $status_url = $tweets[$x]->status_url;

?>
		<div class="row well tweet-container">
			<blockquote class="twitter-tweet col-md-10" data-lang="en">
				<p lang="en" dir="ltr"><?php echo $tweet ?></p>&mdash; <?php echo $screen_name ?> <a href="<?php echo $status_url; ?>"><?php echo $date_post ?></a>
			</blockquote>
			<button class="btn btn-danger btn-lg col=-md-2 recommend-button" id="id_<?php echo $screen_name; ?>" onclick="sendTweet('<?php echo $screen_name; ?>','<?php echo $review_url; ?>','<?php echo $movie_name; ?>');">Recommend</button>
		</div>

<?php 
	}
?>

</div>


<?php 
	 include_once("templates/script.php");  
	 include_once("templates/footer.php");  
?>
