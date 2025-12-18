export function renderFooter() {
  const footer = document.createElement('footer');
  footer.className = 'site-footer';
  footer.style.cssText = 'background: var(--surface); border-top: 1px solid var(--glass-border); padding: 4rem 2rem 2rem; margin-top: 2rem;';

  const template = `
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem;">
      
      <!-- Column 1: Site Links -->
      <div class="footer-col">
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Site Links</h4>
        <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
          <a href="./index.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Home</a>
          <a href="./index.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">All Games</a>
          <a href="./about.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">About Us</a>
          <a href="./contact.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Contact Us</a>
        </nav>
      </div>

      <!-- Column 2: Game Categories -->
      <div class="footer-col">
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Game Categories</h4>
        <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
          <a href="./action.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Action</a>
          <a href="./arcade.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Arcade</a>
          <a href="./puzzle.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Puzzle</a>
          <a href="./racing.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Racing</a>
          <a href="./sports.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Sports</a>
        </nav>
      </div>

      <!-- Column 3: Popular Games -->
      <div class="footer-col">
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Popular Games</h4>
        <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
          <a href="./games/tunnel-road.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Tunnel Road</a>
          <a href="./games/2048-classic.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">2048 Classic</a>
          <a href="./games/bubble-game-3d.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Bubble Game 3D</a>
          <a href="./games/merge-flowers.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Merge Flowers</a>
        </nav>
      </div>

      <!-- Column 4: Legal -->
      <div class="footer-col">
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.1em;">Legal</h4>
        <nav style="display: flex; flex-direction: column; gap: 0.8rem;">
          <a href="./privacy.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Privacy Policy</a>
          <a href="./terms.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Terms of Service</a>
          <a href="./contact.html" style="color: var(--color-text-dim); text-decoration: none; transition: color 0.2s;">Contact</a>
        </nav>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div style="max-width: 1200px; margin: 3rem auto 0; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; color: var(--color-text-dim); font-size: 0.9em;">
      <p>&copy; 2025 Modern Game Portal. All rights reserved.</p>
    </div>
  `;

  footer.innerHTML = template;
  return footer;
}
