<?php 
	include_once("templates/header.php");  
	include_once("templates/style.php"); 
    include_once("templates/logo.php");
?>

<div class="col-md-offset-2 col-md-8">
    <div class="form-group">
        <label for="film-name">Movie Name : </label>
        <input type="text" id="film-name" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="directed-by">Directed by : </label>
        <input type="text" id="directed-by" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="produced-by">Produced by : </label>
        <input type="text" id="produced-by" class="form-control market-form-text-field" />
    </div>

    
    <div class="form-group">
        <label for="written-by">Written by : </label>
        <input type="text" id="written-by" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="starring">Starring (comma separated) (jacky, bruce lee, arnold,...) : </label>
        <input type="text" id="starring" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="music-by">Music by : </label>
        <input type="text" id="music-by" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="cinematography">Cinematography : </label>
        <input type="text" id="cinematography" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="release-date">Release Date : </label>
        <input type="text" id="release-date" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="country">Country : </label>
        <input type="text" id="country" class="form-control market-form-text-field" />
    </div>
    
    <div class="form-group">
        <label for="review-author">Review Author : </label>
        <input type="text" id="review-author" class="form-control market-form-text-field" />
    </div>
</div>

<div class="col-md-offset-7 col-md-3" style="margin-bottom:2%;">
    <button class="btn btn-success full-button">Save & Find</button>
</div>
<?php 
	include_once("templates/script.php");  
	include_once("templates/footer.php");  
?>
