def generate_css_theme(brand_name, slug, author):
    css_template = f"""
    /*
    Theme Name: {brand_name}
    Theme URI: https://wordpress.org/themes/{slug}/
    Author: {author}
    Author URI: https://wordpress.org/
    Description: 
    Requires at least: 
    Tested up to: 
    Requires PHP: 
    Version: 1
    License: GNU General Public License v2 or later
    License URI: http://www.gnu.org/licenses/gpl-2.0.html
    Text Domain: {slug}
    Tags: 

    {brand_name} WordPress Theme, (C) 2021 WordPress.org
    {brand_name} is distributed under the terms of the GNU GPL.
    */
    """

    return css_template