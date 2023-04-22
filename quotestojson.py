import json
import re

quotes_and_authors = [
    "Your time is limited, don't waste it living someone else's life. Don't be trapped by dogma, which is living with the results of other people's thinking. - Steve Jobs",
    "Here's to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes...because the ones who are crazy enough to think that they can change the world, are the ones who do. - Steve Jobs",
    "It is how we choose what we do, and how we approach it, that will determine whether the sum of our days adds up to a formless blur, or to something resembling a work of art - Mihaly Csikszentmihalyi",
    "Self belief is immensely powerful. The most successful people I know believe in themselves almost to the point of delusion. - Sam Altman",
    "Be curious, and however difficult life may seem, there is always something you can do and succeed at. It matters that you don't just give up - Stephen Hawking",
    "Whatever you can do or dream you can, begin it. Boldness has genius, power, and magic in it. - Johann Wolfgang von Goethe",
    "Study hard what interests you the most in the most undisciplined, irreverent and original manner possible - Richard Feynman",
    "What I cannot create, I do not understand. - Richard Feynman",
    "My mother … had a wonderful sense of humor, and I learned from her that the highest forms of understanding we can achieve are laughter and human compassion. - Richard Feynman",
    "As a day well spent makes sleep seem pleasant, so a life well employed makes death pleasant. – Leonardo da Vinci",
    "You can have no dominion greater or less than that over yourself. – Leonardo da Vinci",
    "Life needs to be more than just solving every day problems. You need to wake up and be excited about the future – Elon Musk",
    "If things are not failing, you are not innovating enough. – Elon Musk",
    "When something is important enough, you do it even if the odds are not in your favor. – Elon Musk",
    "Any sufficiently advanced technology is indistinguishable from magic. - Arthur C Clarke",
    "The true delight is in the finding out rather than in the knowing. - Isaac Asimov",
    "I do not fear computers. I fear the lack of them. - Isaac Asimov",
    "One man’s ‘magic’ is another man’s engineering. – Robert Heinlein",
    "Life is trying things to see if they work. – Ray Bradbury",
    "I tell you, we are here on Earth to fart around, and don't let anybody tell you different. – Kurt Vonnegut",
    "When something is such a creative medium as the web, the limits to it are our imagination. – Marvin Minsky",
    "Innovation is serendipity, so you don’t know what people will make. – Marvin Minsky",
    "Computer languages of the future will be more concerned with goals and less with procedures specified by the programmer. – Marvin Minsky",
    "We can only see a short distance ahead, but we can see plenty there that needs to be done. – Alan Turing",
    "Those who can imagine anything, can create the impossible. – Alan Turing",
    "I've always been more interested in the future than in the past. – Grace Hopper",
    "A good scientist is a person with original ideas. A good engineer is a person who makes a design that works with as few original ideas as possible. There are no prima donnas in engineering. – Freeman Dyson",
    "There is a great satisfaction in building good tools for other people to use. – Freeman Dyson",
    "I never did anything worth doing by accident, nor did any of my inventions come indirectly through accident, except the phonograph. No, when I have, fully decided that a result is worth getting, I go about it, and make trial after trial, until it comes. – Thomas Edison",
    "Don't worry about what anybody else is going to do. The best way to predict the future is to invent it. – Alan Kay",
    "The important thing, once you have enough to eat and a nice house, is what you can do for others, what you can contribute to the enterprise as a whole. – Donald Knuth",
    "That as we enjoy great advantages from the inventions of Others, we should be glad of an opportunity to serve others by any invention of ours, and this we should do freely and generously. – Benjamin Franklin",
    "There is nothing like a dream to create the future. - Victor Hugo",
    "Live in the future, then build what's missing - Paul Graham",
    "The way to come up with new ideas is not to try explicitly to, but to try to solve problems and simply not discount weird hunches you have in the process. - Paul Graham",
    "If you aren’t embarrassed by the first version of your product, you shipped too late. – Reid Hoffman",
    "For life in permanent beta, the trick is to never stop starting. – Reid Hoffman",
    "Start a personal blog and begin developing a public reputation and public portfolio of work that’s not tied to your employer. – Reid Hoffman",
    "Until you value yourself, you won’t value your time. Until you value your time, you will not do anything with it. - M. Scott Peck",
    "In a world that’s changing so quickly, the biggest risk you can take is not taking any risk - Peter Thiel",
    "There is a power to obsession and being able to absolutely obsess over something and throw your life’s work. – John Carmack",
    "The programmers of tomorrow are the wizards of the future - Gabe Newell",
    "I've always been more interested in the future than in the past. – Grace Hopper"
    # Add more quotes and authors as separate strings, separated by commas
]

def parse_quote_and_author(quote_and_author):
    split_data = re.split(r'[-–]\s+', quote_and_author.strip(), maxsplit=1)
    if len(split_data) != 2:
        raise ValueError(f"Failed to parse quote and author: {quote_and_author}")
    quote, author = split_data
    return {"quote": quote.strip(), "author": author.strip()}
output = [parse_quote_and_author(item) for item in quotes_and_authors]

with open('quotes.json', 'w') as f:
    json.dump(output, f, indent=2)

print(json.dumps(output, indent=2))
