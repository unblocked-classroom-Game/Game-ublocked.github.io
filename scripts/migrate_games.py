import json
import os
import shutil
import re

# Paths
EXTRACTED_DATA_DIR = "extracted_data"
SOURCE_JSON = os.path.join(EXTRACTED_DATA_DIR, "games.json")
DEST_JSON = "src/data/games.json"
GAMES_DIR = "games"
IMAGES_DIR = "public/cache/data/image/game"

# Template derived from vex3.html
# We replace:
# {{TITLE}} -> Game Title
# {{SLUG}} -> Game Slug
# {{DESCRIPTION}} -> Game Description
# {{IMAGE}} -> Image Path
# {{IFRAME_URL}} -> Source URL

GAME_TEMPLATE = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/x-icon" href="../public/cache/data/image/options/geometry_dash.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{{TITLE}} - Play Online for Free</title>
  <meta name="description" content="{{DESCRIPTION}}" />
  <meta name="keywords" content="play {{TITLE}}, {{TITLE}} game, free online games, Arcade games" />
  <link rel="canonical" href="https://pingwin-w.github.io/GameBLOCK.github.io/games/{{SLUG}}.html" />
  <meta name="robots" content="index, follow" />

  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5520409989170076"
    crossorigin="anonymous"></script>

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://pingwin-w.github.io/GameBLOCK.github.io/games/{{SLUG}}.html" />
  <meta property="og:title" content="{{TITLE}} - Play Online for Free" />
  <meta property="og:description" content="{{DESCRIPTION}}" />
  <meta property="og:image" content="https://pingwin-w.github.io/GameBLOCK.github.io/{{IMAGE_REL}}" />

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:site" content="@ModernUblocked" />
  <meta property="twitter:url" content="https://pingwin-w.github.io/GameBLOCK.github.io/games/{{SLUG}}.html" />
  <meta property="twitter:title" content="{{TITLE}} - Play Online for Free" />
  <meta property="twitter:description" content="{{DESCRIPTION}}" />
  <meta property="twitter:image" content="https://pingwin-w.github.io/GameBLOCK.github.io/{{IMAGE_REL}}" />
  <link rel="stylesheet" href="../src/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>

<body>
  <div id="app">
    <div class="layout-container">
      <header class="nav-header">
        <div class="header-content">
          <div class="logo-area">
            <h1>ublocked games</h1>
          </div>
          <nav class="nav-menu">
            <a href="../index.html" class="nav-item">
              <span class="icon">🏠</span>
              <span>Home</span>
            </a>
            <a href="../popular.html" class="nav-item">
              <span class="icon">🔥</span>
              <span>Popular</span>
            </a>
            <a href="../new.html" class="nav-item">
              <span class="icon">✨</span>
              <span>New</span>
            </a>
            <a href="./about.html" class="nav-item">
              <span class="icon">ℹ️</span>
              <span>About</span>
            </a>
            <a href="./contact.html" class="nav-item">
              <span class="icon">📧</span>
              <span>Contact</span>
            </a>
          </nav>
        </div>
      </header>

      <main id="main-content" class="main-content">
  <section class="player-layout">
      <div class="player-main">
        <div class="player-header">
          <a href="../index.html" class="btn-back">
            <span class="icon">arrow_back</span> Back
          </a>
          <h2>{{TITLE}}</h2>
        </div>
        
        <div class="game-wrapper">
          <div class="iframe-container">
             <iframe 
               src="{{IFRAME_URL}}" 
               id="game-frame" 
               frameborder="0" 
               scrolling="no" 
               allowfullscreen 
               referrerpolicy="no-referrer" 
               style="width: 100%; height: 100%; background: white;"
               sandbox="allow-scripts allow-same-origin allow-popups allow-forms allow-pointer-lock allow-top-navigation-by-user-activation"
               allow="autoplay; fullscreen; monetization; clipboard-write; web-share; accelerometer; magnetometer; gyroscope; display-capture">
            </iframe>
          </div>
          <div class="game-controls">
            <button id="btn-fullscreen" class="control-btn" onclick="const iframe = document.getElementById('game-frame'); if(iframe.requestFullscreen) iframe.requestFullscreen();">
              <span class="icon">fullscreen</span> Fullscreen
            </button>
             <div class="rating">
                <span class="icon">❤️</span> 95%
             </div>
          </div>
        </div>

        <div class="game-info">
          <h3>About {{TITLE}}</h3>
          <p>{{DESCRIPTION}}</p>
          
          <div class="instructions">
             <h3>How to Play</h3>
             <ul>
               <li>Click "Play" to start.</li>
               <li>Use Mouse or Keyboard to control.</li>
               <li>Complete objectives and earn high scores!</li>
             </ul>
          </div>
        </div>
      </div>

      <aside class="player-sidebar">
        <h3>You May Also Like</h3>
        <div class="related-games-list">
          
            <a href="../games/vex4.html" class="related-card">
              <img src="../public/cache/data/image/game/vex4/vex4.jpg" alt="Vex4" loading="lazy" />
              <div class="info">
                <h4>Vex4</h4>
                <span>Arcade</span>
              </div>
            </a>
        
            <a href="../games/vex6.html" class="related-card">
              <img src="../public/cache/data/image/game/vex6/vex6.jpeg" alt="Vex6" loading="lazy" />
              <div class="info">
                <h4>Vex6</h4>
                <span>Arcade</span>
              </div>
            </a>
        
            <a href="../games/uphill-rush-13.html" class="related-card">
              <img src="../public/cache/data/image/game/uphill-rush-13/uphill-rush-13.jpg" alt="Uphill Rush 13" loading="lazy" />
              <div class="info">
                <h4>Uphill Rush 13</h4>
                <span>Arcade</span>
              </div>
            </a>
        
            <a href="../games/physics-balls.html" class="related-card">
              <img src="../public/cache/data/image/game/physics-balls/physics-balls.jpg" alt="Physics Balls" loading="lazy" />
              <div class="info">
                <h4>Physics Balls</h4>
                <span>Arcade</span>
              </div>
            </a>
        
            <a href="../games/zen-master-3-tiles.html" class="related-card">
              <img src="../public/cache/data/image/game/zen-master-3-tiles/zen-master-3-tiles.jpg" alt="Zen Master - 3 tiles" loading="lazy" />
              <div class="info">
                <h4>Zen Master - 3 tiles</h4>
                <span>Arcade</span>
              </div>
            </a>
        
            <a href="../games/granny.html" class="related-card">
              <img src="../public/cache/data/image/game/granny/granny.png" alt="Granny" loading="lazy" />
              <div class="info">
                <h4>Granny</h4>
                <span>Arcade</span>
              </div>
            </a>
        
        </div>
      </aside>
    </section>
</main>

      <footer class="site-footer"
        style="background: var(--surface); border-top: 1px solid var(--glass-border); padding: 4rem 2rem 2rem; margin-top: 2rem;">
        <div
          style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem;">

          <!-- Column 1: Site Links -->
          <div class="footer-col">
            <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Site Links</h4>
            <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="../index.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Home</a>
              <a href="../index.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">All Games</a>
              <a href="./about.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">About Us</a>
              <a href="./contact.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Contact Us</a>
            </nav>
          </div>

          <!-- Column 2: Game Categories -->
          <div class="footer-col">
            <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Game Categories</h4>
            <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="./action.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Action</a>
              <a href="./arcade.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Arcade</a>
              <a href="./puzzle.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Puzzle</a>
              <a href="./racing.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Racing</a>
              <a href="./sports.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Sports</a>
            </nav>
          </div>

          <!-- Column 3: Popular Games -->
          <div class="footer-col">
            <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Popular Games</h4>
            <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="./games/tunnel-road.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Tunnel Road</a>
              <a href="./games/2048-classic.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">2048 Classic</a>
              <a href="./games/bubble-game-3d.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Bubble Game
                3D</a>
              <a href="./games/merge-flowers.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Merge Flowers</a>
            </nav>
          </div>

          <!-- Column 4: Legal -->
          <div class="footer-col">
            <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Legal</h4>
            <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="./privacy.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Privacy
                Policy</a>
              <a href="./terms.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Terms of
                Service</a>
              <a href="./contact.html"
                style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Contact</a>
            </nav>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div
          style="max-width: 1200px; margin: 3rem auto 0; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; color: var(--color-text-dim); font-size: 0.9em;">
          <p>&copy; 2025 Modern ublocked games. All rights reserved.</p>
        </div>
      </footer>
    </div>
  </div>
  <script type="module" src="../src/main.js"></script>
</body>

</html>
"""

# Load existing data first
try:
    with open(DEST_JSON, 'r') as f:
        existing_games = json.load(f)
except FileNotFoundError:
    existing_games = []

existing_slugs = {g['slug'] for g in existing_games}

# Load source data
try:
    with open(SOURCE_JSON, 'r') as f:
        new_games = json.load(f)
except FileNotFoundError:
    print(f"Error: {SOURCE_JSON} not found.")
    exit(1)

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

added_count = 0

for game in new_games:
    title = game['title']
    slug = slugify(title)
    
    if slug in existing_slugs:
        # print(f"Skipping {title}, already exists.")
        continue
        
    print(f"Processing {title}...")
    
    # Image handling
    # new_games json has "extracted_data/game_icons/..."
    # We are in root, so relative path is valid.
    source_icon = game['icon_url'].replace("\\", "/") # standardize slashes
    if not os.path.exists(source_icon):
        # Trying to guess if path is different
        # Sometimes source might be just "game_icons/..."? No, I saw "extracted_data/game_icons"
        # Let's try simple join
        pass

    dest_dir = os.path.join(IMAGES_DIR, slug)
    os.makedirs(dest_dir, exist_ok=True)
    
    ext = os.path.splitext(source_icon)[1]
    if not ext: ext = ".png"
    
    dest_filename = f"{slug}{ext}"
    dest_path = os.path.join(dest_dir, dest_filename)
    
    final_image_path = f"./public/cache/data/image/game/{slug}/{dest_filename}"
    image_rel = f"public/cache/data/image/game/{slug}/{dest_filename}" # For OG tags
    
    if os.path.exists(source_icon):
        shutil.copy(source_icon, dest_path)
    else:
        print(f"  Warning: Icon not found: {source_icon}, using default.")
        final_image_path = "./public/cache/data/image/options/no_image.png"
        image_rel = "public/cache/data/image/options/no_image.png"

    # Add to existing_games
    new_entry = {
        "id": slug,
        "name": title,
        "slug": slug,
        "description": f"Play {title} unblocked.",
        "category": "Arcade",
        "image": final_image_path
    }
    existing_games.append(new_entry)
    existing_slugs.add(slug)
    
    # Generate HTML
    html_content = GAME_TEMPLATE.replace("{{TITLE}}", title) \
                                .replace("{{SLUG}}", slug) \
                                .replace("{{DESCRIPTION}}", f"Play {title} unblocked.") \
                                .replace("{{IMAGE}}", final_image_path) \
                                .replace("{{IMAGE_REL}}", image_rel) \
                                .replace("{{IFRAME_URL}}", game['iframe_url'])
                                
    with open(os.path.join(GAMES_DIR, f"{slug}.html"), "w") as f:
        f.write(html_content)
        
    added_count += 1

# Save JSON
with open(DEST_JSON, 'w') as f:
    json.dump(existing_games, f, indent=2)
    
print(f"Migration complete. Added {added_count} games.")
