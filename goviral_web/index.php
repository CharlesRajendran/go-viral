<?php 
	include_once("templates/header.php");  
	include_once("templates/style.php"); 
    include_once("templates/logo.php");
?>

	<div class="row">
		<div class="col-md-4">
			<input id="movie_name" class="form-control" placeholder="Type Movie Name..." />
		</div>
    </div>
    <div class="row">
        <div class="col-md-6" id="content-section">
            <textarea id="content-textarea" class="full-width form-control" spellcheck="false" placeholder="paste your content here..."></textarea>
        </div>

        <div class="col-md-6" id="rules-section">
            
            <div id="positive-rules" class="well rules-div"> 
                                               
            </div>

            <div id="negative-rules" class="well rules-div">
                
            </div>
        </div>
    </div> 


    <div id="popularity_alert" class="alert alert-info alert-dismissible" role="alert">
      <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
      <div id="alert_message" align="center">
        Your content have <span id="popularity_percentage_span">83%</span> popularity elements. 
      </div>
    </div>

    <div class="row" id="button-section">
        <div class="col-md-4">
            <button class="btn btn-success full-button" id="messure_popularity">Measure Popularity</button>
        </div>
        <div class="col-md-4">
            <button class="btn btn-success full-button" onclick="window.location='./content-edit.php'">Improve</button>
        </div>
        <div class="col-md-4">
            <button id="market-button" class="btn btn-success full-button">Market</button>
        </div>
     </div>

<?php 
	include_once("templates/script.php");  
?>

<script src="./public/scripts/main.js"></script>
<?php
	include_once("templates/footer.php");  
?>
