export function renderGameCard(game) {
  const a = document.createElement('a');
  a.href = `#/game/${game.slug}`; // Hash navigation
  a.className = 'game-card';

  // Use 'public' path for images. 
  // Original path: /cache/data/image/...
  // We mirrored this in public/cache, so the paths in JSON (starting with /cache) should work as-is
  // relative to the root.

  let imgUrl = game.image;
  if (imgUrl.startsWith('/cache')) {
    // Relative path to public folder
    imgUrl = './public' + imgUrl;
  } else if (imgUrl.startsWith('/')) {
    imgUrl = '.' + imgUrl;
  }

  a.innerHTML = `
    <div class="card-image">
      <img src="${imgUrl}" alt="${game.name}" loading="lazy" />
      <div class="card-overlay">
        <span class="play-button">▶</span>
      </div>
    </div>
    <div class="card-info">
      <h3>${game.name}</h3>
    </div>
  `;

  return a;
}
