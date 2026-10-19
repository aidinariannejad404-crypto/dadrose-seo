<?php
/**
 * Plugin Name: DADROSE llms.txt
 * Description: Serves the hand-curated /llms.txt (file dadrose-llms.txt next to this plugin) as text/plain; charset=utf-8, ahead of any other plugin.
 * Version: 1.0.0
 *
 * Only needed if a physical /llms.txt is NOT present in the web root (a physical file is served by the
 * web server before PHP runs, so this plugin never fires while it exists). Install: upload this file and
 * dadrose-llms.txt (the curated llms.txt, renamed) to wp-content/mu-plugins/.
 */

if (! defined('ABSPATH')) {
    exit;
}

/**
 * Output the curated llms.txt for the exact path /llms.txt and stop.
 */
function dadrose_llms_serve(): void
{
    $path = parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH);

    if ($path !== '/llms.txt') {
        return;
    }

    $file = __DIR__ . '/dadrose-llms.txt';

    if (! is_readable($file)) {
        return;
    }

    status_header(200);
    header('Content-Type: text/plain; charset=utf-8');
    header('Cache-Control: public, max-age=3600');
    header('X-Robots-Tag: noindex');
    readfile($file);
    exit;
}

add_action('plugins_loaded', 'dadrose_llms_serve', 0);
