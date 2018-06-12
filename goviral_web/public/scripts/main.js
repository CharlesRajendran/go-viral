$(document).ready(function(){

	$('#market-button').click(function(){
		$.post('http://localhost/goviral_web/curl/postReview.php',JSON.stringify({
			'movie':document.getElementById('movie_name').value,
			'content': document.getElementById('content-textarea').value 
		}),function(response1){
			console.log(response1);
			var review_url = response1.reviewUrl;

			$.get('http://localhost/goviral_web/curl/getTweets.php',JSON.stringify({
				'movie':response1.movie_name
			}),function(response2){
				console.log("Response 2");
				console.log(response2);
				window.location = "./tweets.php";
			});	
		});		
	});

	$('#messure_popularity').click(function(){
		$.post('http://localhost/goviral_web/curl/postRawReviewText.php',JSON.stringify({
			'movie':document.getElementById('movie_name').value,
			'content': document.getElementById('content-textarea').value
		}),function(response3){
			$.post('http://localhost/goviral_web/curl/postReviewPopularity.php',JSON.stringify({
				'movie':response3.movie
			}),function(response4){
				// console.log(response4);

				$.get('http://localhost/goviral_web/curl/getVisualise.php',function(response5){
					// console.log(response5);
					// console.log(response5.popular_words);
					// console.log(response5.non_popular_words);
					positive_words = "<h2><u>Popular Words</u></h2>";
					for(var p_words=0;p_words<response5.popular_words.length;p_words++){
						positive_words+='<h4 class="pos_words">'+response5.popular_words[p_words]+'<//h4>';
					}

					negative_words = "<h2><u>Negative Popular Words</u></h2>";
					for(var n_words=0;n_words<response5.non_popular_words.length;n_words++){
						negative_words+='<h4 class="non_pos_words">'+response5.non_popular_words[n_words]+'</h4>';
					}

					// console.log(positive_words);
					// console.log(negative_words);

					document.getElementById('positive-rules').innerHTML = positive_words;
					document.getElementById('negative-rules').innerHTML = negative_words;

					document.getElementById('popularity_percentage_span').innerHTML = response4.p_percentage+"%";
					document.getElementById('popularity_alert').style.display="block";
				});
			});
		});
	});
});