import os
import json
import shutil
import re

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')
GAMES_DIR = os.path.join(BASE_DIR, 'games')
DATA_FILE = os.path.join(SRC_DIR, 'data', 'games.json')
TEMPLATE_FILE = os.path.join(BASE_DIR, 'template.html')

print('Starting static site generation (Root Mode)...')

# Ensure games directory exists and is clean
if os.path.exists(GAMES_DIR):
    shutil.rmtree(GAMES_DIR)
os.makedirs(GAMES_DIR)

# 1. Read Data
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    games = json.load(f)

with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template = f.read()

# 2. No need to copy assets (we are in root)

# 3. Helper to Generate Grid Pages
def generate_grid_page(games_list, page_title, output_filename, active_nav='', seo_title='', seo_desc=''):
    print(f'Generating {output_filename}...')
    
    # Defaults
    if not seo_title:
        seo_title = f"{page_title} - Modern Game Portal"
    if not seo_desc:
        seo_desc = "Play the best free online games at Modern Game Portal. Discover arcade, puzzle, and action games in a premium, ad-free environment."
    seo_image = "https://pingwin-w.github.io/GameBLOCK.github.io/public/cache/data/image/options/geometry_dash.png"
    seo_url = f"https://pingwin-w.github.io/GameBLOCK.github.io/{output_filename}"
    seo_keywords = "online games, free games, arcade games, puzzle games, browser games, html5 games"
    
    games_html_list = []
    for game in games_list:
        category = game.get('category', 'Arcade')
        name = game.get('name', 'Unknown')
        slug = game.get('slug', 'unknown')
        image = game.get('image', '')
        
        card_html = f'''
      <a href="./games/{slug}.html" class="game-card" style="animation: fadeIn 0.5s ease;">
        <div class="card-image">
          <img src="{image}" alt="{name}" loading="lazy" />
          <div class="card-overlay">
            <span class="play-icon">▶</span>
          </div>
        </div>
        <div class="card-info">
          <h3>{name}</h3>
          <span class="category">{category}</span>
        </div>
      </a>
    '''
        games_html_list.append(card_html)

    games_grid_html = ''.join(games_html_list)

    page_html = f'''
      <section class="home-page">
        <header class="page-header">
          <h2>{page_title}</h2>
          <div class="search-bar">
            <input type="text" placeholder="Search games..." />
          </div>
        </header>
        <div class="games-grid">
          {games_grid_html}
        </div>
      </section>
    '''

    page_content = template.replace(
        '<main id="main-content" class="main-content">\n        <!-- Content will be injected here -->\n      </main>',
        f'<main id="main-content" class="main-content">{page_html}</main>'
    )
    
    # Set Active Nav State
    # Note: This is simple string replacement, might be brittle if classes change
    if active_nav == 'home':
         page_content = page_content.replace('href="./index.html" class="nav-item"', 'href="./index.html" class="nav-item active"')
    elif active_nav == 'popular':
         page_content = page_content.replace('href="./popular.html" class="nav-item"', 'href="./popular.html" class="nav-item active"')
    elif active_nav == 'new':
         page_content = page_content.replace('href="./new.html" class="nav-item"', 'href="./new.html" class="nav-item active"')

    # Inject SEO
    page_content = page_content.replace('%TITLE%', seo_title)
    page_content = page_content.replace('%DESCRIPTION%', seo_desc)
    page_content = page_content.replace('%IMAGE%', seo_image)
    page_content = page_content.replace('%URL%', seo_url)
    page_content = page_content.replace('%KEYWORDS%', seo_keywords)

    with open(os.path.join(BASE_DIR, output_filename), 'w', encoding='utf-8') as f:
        f.write(page_content)

# Generate Home (Default Order)
generate_grid_page(games, 'All Games', 'index.html', active_nav='home', 
                   seo_title="Modern Game Portal - Play Best Free Online Games",
                   seo_desc="Play the best free online games at Modern Game Portal. Discover arcade, puzzle, and action games in a premium, ad-free environment. Play now without downloads!")

# Generate Popular (Shuffle)
import random
popular_games = games.copy()
random.shuffle(popular_games)
generate_grid_page(popular_games, 'Popular Games', 'popular.html', active_nav='popular')

# Generate New (Reverse Order)
new_games = games.copy()
new_games.reverse()
generate_grid_page(new_games, 'New Games', 'new.html', active_nav='new')


# 4. Generate Game Pages
print('Generating game pages...')

for game in games:
    game_id = game.get('id', '')
    name = game.get('name', 'Unknown')
    slug = game.get('slug', 'unknown')
    
    if not game_id:
        print(f"Skipping {name} - no ID")
        continue

    game_url = f"https://html5.gamedistribution.com/{game_id}/"

    # Select 6 random other games for sidebar
    import random
    other_games = [g for g in games if g.get('slug') != slug]
    random.shuffle(other_games)
    sidebar_games = other_games[:6]
    
    sidebar_html_list = []
    for bg in sidebar_games:
        bg_name = bg.get('name', 'Game')
        bg_slug = bg.get('slug', '')
        bg_cat = bg.get('category', 'Game')
        bg_img = bg.get('image', '')
        # Fix relative image path for subplot
        if bg_img.startswith('./'):
             bg_img = '.' + bg_img 
        
        sidebar_html_list.append(f'''
            <a href="../games/{bg_slug}.html" class="related-card">
              <img src="{bg_img}" alt="{bg_name}" loading="lazy" />
              <div class="info">
                <h4>{bg_name}</h4>
                <span>{bg_cat}</span>
              </div>
            </a>
        ''')
    sidebar_html = ''.join(sidebar_html_list)

    # Game Description
    g_desc_text = game.get('description', '')
    if not g_desc_text:
        g_desc_text = f"Play {name} online for free. This is a popular {game.get('category','Arcade')} game."

    player_html = f'''
  <section class="player-layout">
      <div class="player-main">
        <div class="player-header">
          <a href="../index.html" class="btn-back">
            <span class="icon">arrow_back</span> Back
          </a>
          <h2>{name}</h2>
        </div>
        
        <div class="game-wrapper">
          <div class="iframe-container">
             <iframe 
               src="{game_url}" 
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
          <h3>About {name}</h3>
          <p>{g_desc_text}</p>
          
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
          {sidebar_html}
        </div>
      </aside>
    </section>
'''

    page_content = template.replace(
        '<main id="main-content" class="main-content">\n        <!-- Content will be injected here -->\n      </main>',
        f'<main id="main-content" class="main-content">{player_html}</main>'
    )
    
    # Game SEO Data
    g_title = f"{name} - Play Online for Free"
    g_desc = game.get('description', '')
    if not g_desc:
        g_desc = f"Play {name} online for free. One of the best {game.get('category','Arcade')} games. No downloads required!"
    
    # Fix image path for SEO (make absolute if possible, or at least relative correctly)
    # The image path is like /cache/... or ./public/...
    # Ideally use absolute URL for OG tags
    g_image = game.get('image', '')
    if g_image.startswith('./'):
        g_image = g_image[1:] # remove dot, keep /public...
    
    full_image_url = f"https://pingwin-w.github.io/GameBLOCK.github.io{g_image}"
    full_page_url = f"https://pingwin-w.github.io/GameBLOCK.github.io/games/{slug}.html"
    
    page_content = page_content.replace('%TITLE%', g_title)
    page_content = page_content.replace('%DESCRIPTION%', g_desc)
    page_content = page_content.replace('%IMAGE%', full_image_url)
    page_content = page_content.replace('%URL%', full_page_url)
    page_content = page_content.replace('%KEYWORDS%', f"play {name}, {name} game, free online games, {game.get('category','Arcade')} games")

    # Fix resource paths for subdirectory
    # We need to change ./src/ -> ../src/ and ./public/ -> ../public/
    page_content = page_content.replace('href="./src/', 'href="../src/')
    page_content = page_content.replace('src="./src/', 'src="../src/')
    page_content = page_content.replace('href="./public/', 'href="../public/')
    page_content = page_content.replace('src="./public/', 'src="../public/')
    
    # Fix Sidebar Links for subdirectory
    page_content = page_content.replace('href="./index.html"', 'href="../index.html"')
    page_content = page_content.replace('href="./popular.html"', 'href="../popular.html"')
    page_content = page_content.replace('href="./new.html"', 'href="../new.html"')

    with open(os.path.join(GAMES_DIR, f'{slug}.html'), 'w', encoding='utf-8') as f:
        f.write(page_content)

print('Build complete! Output in root.')
