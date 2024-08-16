### Most Viewed Posts Plugin

Most Viewed Posts is a WordPress plugin that tracks and displays the most viewed posts on your site. It supports optional thumbnails and a customizable shortcode.

# Features
- Track Post Views: tracks and updates the number of views for each post.
- Display Most Viewed Posts: Shows the most viewed posts with optional post thumbnails.
- Customizable Shortcode: Use a shortcode to display the most viewed posts with configurable options.
# Installation
- Download the Plugin: Download the latest release from the GitHub repository.
- Upload the Plugin: Upload the plugin folder to your WordPress site via FTP to wp-content/plugins/.
- Activate the Plugin: Go to the WordPress admin dashboard, navigate to Plugins, find Most Viewed Posts, and click Activate.
# Usage
Shortcode
Use the [most_viewed_posts] shortcode to display the most viewed posts on your site. The shortcode has the following optional attributes:
- posts: Number of posts to display (default is 5).
- post_type: Post type to query (default is post).
Example:
plaintext
Copy code
[most_viewed_posts posts="10" post_type="post"]
This shortcode will display the top 10 most viewed posts.

# Template Tags
For developers, you can use the following functions in your theme:

- mvp_track_post_views(): Call this function to track post views (should be used in wp_head action).
- mvp_set_post_views($post_id): Manually set the view count for a post.
- mvp_get_post_views($post_id): Get the view count of a post.

# Customization
You can style the shortcode output by adding custom CSS to your theme. The default class names used are:
- .most-viewed-posts: Container for the list of posts.
- .post-view-image: Image link for the post thumbnail.
- .post-view-title: Title link for the post.
- .post-view-meta: Meta information (author and date) for the post.

# Changelog
Version 1.3
- Added support for custom post types.
- Improved shortcode functionality and output formatting.
Version 1.2
- Fixed minor bugs and improved performance.
Version 1.1
- Initial release with basic functionality.

# Contributing
Contributions are welcome! Please fork the repository and submit pull requests. For bug reports and feature requests, please open an issue on GitHub.

# License
This plugin is licensed under the GPL2 license.

# Author
MedX Media Team
https://medxmedia.net/
