from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chronicles of Eloria</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #0d0d0d;
            color: #fff;
            line-height: 1.6;
        }

        header {
            background-color: #111;
            padding: 20px 0;
            text-align: center;
            border-bottom: 5px solid #c77e36;
        }

        header h1 {
            font-size: 3rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        nav {
            background-color: #111;
            padding: 10px 0;
            text-align: center;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 20px;
            transition: all 0.3s ease;
        }

        nav a:hover {
            color: #c77e36;
        }

        section {
            padding: 50px 20px;
            text-align: center;
        }

        footer {
            background-color: #111;
            color: #ccc;
            text-align: center;
            padding: 20px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Chronicles of Eloria</h1>
    </header>
    
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Story</a>
        <a href="#">Characters</a>
        <a href="#">Gallery</a>
        <a href="#">Download</a>
    </nav>
    
    <section>
        <h2>Welcome to the Adventure</h2>
        <p>"Chronicles of Eloria" is a gripping and immersive action-adventure RPG set in a world torn apart by betrayal and ancient secrets. Players embark on a quest to uncover the truth behind the Sundering and confront the lingering darkness that threatens to consume Eloria once more.

Themes of redemption, sacrifice, and the consequences of power weave throughout the narrative, challenging players to confront their own choices and forge their own path in a world on the brink of oblivion. As they journey through the fractured landscapes of Eloria, players will encounter allies and adversaries alike, each with their own motivations and agendas.

With its immersive storytelling, dynamic gameplay mechanics, and stunning visuals, "Chronicles of Eloria" offers players an unforgettable gaming experience that will test their courage, cunning, and resolve. In a world where nothing is as it seems, players must navigate the treacherous waters of politics, magic, and ancient lore to uncover the truth and shape the fate of Eloria for generations to come.</p>
        <a href="#" style="padding: 10px 20px; background-color: #c77e36; color: #fff; text-decoration: none; border-radius: 5px; font-size: 1.2rem;">Play Now</a>
    </section>
    
    <section>
        <h2>About the Game</h2>
        <p>In the ancient realm of Eloria, magic was once a gift bestowed upon the land by the mythical beings known as the Eldritch Guardians. Under their watchful gaze, the people of Eloria flourished, building great cities and harnessing the power of magic to advance society.

But as time passed, whispers of discontent spread among the people. Some believed that the Eldritch Guardians were holding back the true potential of magic, while others feared their influence was waning and chaos would soon consume the land.

Amidst this growing unrest, a charismatic leader named Ardyn rallied a faction of rebels, promising to unlock the full potential of magic and usher in a new era of prosperity. Unbeknownst to his followers, Ardyn had made a pact with dark forces, trading his humanity for unimaginable power.

In a cataclysmic event known as the Sundering, Ardyn unleashed a devastating spell that shattered the realm, tearing a rift between the mortal world and the abyss. The Eldritch Guardians, horrified by Ardyn's betrayal, sacrificed themselves to seal the breach, but not before fragments of their essence scattered across Eloria.

Now, centuries later, the land of Eloria lies in ruin, scarred by the aftermath of the Sundering. Magic, once a source of wonder and awe, has become a volatile force that twists and corrupts everything it touches. In the shadows, whispers of Ardyn's return echo, fueling rumors of a dark prophecy that threatens to plunge Eloria into eternal darkness.</p>
    </section>
    
    <footer>
        &copy; 2024 Chronicles of Eloria. All rights reserved.
    </footer>
</body>
</html>

    """
    return page

@app.route('/random')
def random():
    return 'This is my first enpoint here'


if __name__ == '__main__':
    app.run(debug=True)