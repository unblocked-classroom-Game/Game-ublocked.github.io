import { renderFooter } from './Footer.js';
import { renderHeader } from './Header.js';

export function renderLayout(parentElement) {
    // Container
    const container = document.createElement('div');
    container.className = 'layout-container';

    // Header (Top Navigation)
    const header = renderHeader();
    container.appendChild(header);

    // Main Content
    const main = document.createElement('main');
    main.id = 'main-content';
    main.className = 'main-content';
    container.appendChild(main);

    // Footer
    const footer = renderFooter();
    container.appendChild(footer);

    // Mount to #app
    parentElement.appendChild(container);
}

