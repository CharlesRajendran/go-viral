import content_posting as copo
import crawl_imdb_for_stars as cifs
import movie_tweets as mt

def post_review_backend(movie,content):
	print('movie"',movie)
	print('content:',content)

	re_url = copo.writeReviewPHP(movie,content)
	print('review_url:',re_url)

	keys_words = cifs.returnMovieCelebratiesWithPopularity(movie)
	print('keywords',keys_words)

	print(mt.getTweets(keys_words))

	return re_url

if __name__ == "__main__":
	post_review_backend('Cars3','''If #TheMummy is supposed to be the beginning of Universal's ambitious Dark Universe that showcases their classic monsters in one big shared cinematic crossover, then they're off to a terrible start.

There's probably only a couple of sequences that somewhat thrill, the rest are just a continuous string of one poorly written, poorly acted and poorly executed scene after another. It feels more like sitting in a dentist's waiting room as opposed to rockin' on a roller coaster ride. And Tom Cruise is just wrong for this role, a huge case of miscast. Perhaps they should just press the reboot button again.

Sofia Boutella plays an evil ancient princess imprisoned in a tomb deep beneath the unforgiving desert. When a couple of treasure hunters and an archaeologist awaken her in our present day, she returns to life to reclaim her destiny while at the same time unleashing unimaginable terrors in this new take that ushers in a new world of gods and monsters. Co-starring Tom Cruise, Annabelle Wallis, Russell Crowe and Jake Johnson, directed by Alex Kurtzman.

The concept of what the writers and director Alex Kurtzman is trying to present to us with "The Mummy" is nothing new, in fact it's quite predictable, but the biggest problem about it is that along the way from point A to point B, they fill it in with moments that just don't work. And it gets even more frustrating when they bring it up again the second, third and fourth time as if shoving it down our throats would make it better. The jokes fall flat so much so you kinda feel sorry for Jake Johnson who clearly wants to make some effort as this film's comic relief. There are also parts that are just absolutely pointless and unnecessary. The characters including Dr. Jekyll frequently draw conclusions out of their butts. I do think "The Mummy" is what happens when the story is forced to serve the visual spectacle instead of the other way around. That said, rising star Sofia Boutella is a marvelous choice, she exudes that thirst for power effortlessly in addition to being incredibly seductive.

But of course, just as expected, instead of it being a movie about Sofia Boutella's The Mummy, it becomes all about Tom Cruise, who as I said earlier is just awfully wrong for this role. I understand that the studios probably think that banking on a A-lister would translate into box office results, but fact of the matter is outside "Mission: Impossible" franchise, Cruise just doesn't fit anywhere else anymore. The character that he plays here is is a thieving treasure hunter, much like Nathan Drake from "Uncharted" games, but all you see on the screen instead is special agent Ethan Hunt desperately trying to be someone he's not. By the end of "The Mummy" you're going to have second thoughts about anticipating the next installment of this Dark Universe, and you're going to want to wish Brendan Fraser had still been around.
		''')
