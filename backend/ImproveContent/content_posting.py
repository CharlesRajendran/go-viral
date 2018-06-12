from os.path import expanduser

def writeReviewPHP(movie_name,content):
    # the symbol is not hyphen, it is intelide
    user_system = expanduser('~')
    filename = "{0}/GoViral/goviral_web/reviews/review-{1}.php".format(user_system,movie_name)

    content_paras = content.split("\n")
    final_content = ""

    for paras in content_paras:
        final_content += (paras+"<br>")

    page_template = '''<?php 
	include_once("../template-review/header.php");  
	include_once("../template-review/style.php"); 
    include_once("../template-review/logo.php");
?>
<div class="well">
<h3 class="page-header"> {0} Review</h3>
{1}
<?php 
	include_once("../template-review/script.php");  
	include_once("../template-review/footer.php");  
?>'''.format(movie_name,final_content)

    open(filename,'w').write(page_template)
    
    print('done')
    review_url = "http://localhost/"+"/".join(filename.split('/')[filename.split('/').index('goviral_web'):])

    return review_url

if __name__ == "__main__":
    writeReviewPHP('WonderWoman','''Apart from directing good commercial Tamil films, AR Murugadoss is known for producing some quality flicks majorly featuring debut directors. Through Rangoon, he introduces another promising young filmmaker, Rajkumar Periyasamy who happens to be his former associate.

Rangoon is a crime thriller with the core being smuggling. Over the years, we have come across a lot of films that talk about illegal trading but where Rangoon scores is when it gives another dimension to the overall concept. This one is more real and in depth than most of the Tamil movies that dealt with similar concepts.

Though the core concept is so raw, the treatment is largely commercial. That is where Rajkumar Periasamy had made use of the guessing game, leaving the audience to keep thinking about what would happen next. Some may find the story to be predictable while some would say it lost track midway and deviated post interval point but that is the nature of the script and the director has done whatever he could do to tell that in an engaging manner.

The kind of research that has gone behind the project is commendable and at no point, Rajkumar has bombarded his exploration onto the floor and has only used them as a guiding force. Screenplay in the first half look really tight but some might feel that the second half is a little draggy. The emotions look real in most places; however, scenes could have been enacted better. But still, for a debutant to have extracted the kind of work from a bunch of lesser known stars is meritorious.

Probably Rangoon is Gautham Karthik’s best work till date and it could very well give his career a much-needed break. Adequate concentration has been given to make Gautham look like a real slum boy. The overall setup is indigenous right from the set designs, characters involved, their slang and also the dialogues. Another worthy mention is Lallu, the boy from KTVI and 8 Thottakkal. Apart from Gautham Karthik, his role connects well with the audience.

The love portion seems unnecessary. Is it a compulsion to have a love track that does not fit into the script? Sana Makbul looks pleasing but should add few more expressions to her gallery. You get pretty much the same expressions for all the situations from her.

RH Vikram makes an impressive debut as a music director, his songs work well with the visuals. Particularly ‘Foreign Return’ track works well with the masses and ‘Yathriga’ song lingers in your heart well after you leave the theatre.''')
