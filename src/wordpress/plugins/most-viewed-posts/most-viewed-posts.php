<?php
/*
Plugin Name: Most Viewed Posts
Plugin URI:  https://medxmedia.net/
Description: A plugin to track and display the most viewed posts with optional thumbnails.
Version:     1.3
Author:      MedX Media Team
Author URI:  https://medxmedia.net/
License:     GPL2
*/

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

// Track post views
add_action('wp_head', 'mvp_track_post_views');

function mvp_track_post_views() {
    if ( !is_single() ) return;
    global $post;
    if ( !isset($post->ID) ) return;
    $post_id = $post->ID;
    mvp_set_post_views($post_id);
}

function mvp_set_post_views($post_id) {
    $count_key = 'mvp_post_views_count';
    $count = get_post_meta($post_id, $count_key, true);
    if ($count === '') {
        $count = 0;
    }
    $count++;
    update_post_meta($post_id, $count_key, $count);
}

function mvp_get_post_views($post_id){
    $count_key = 'mvp_post_views_count';
    $count = get_post_meta($post_id, $count_key, true);
    if ($count === '') {
        return "0 Views";
    }
    return $count . ' Views';
}

// Create shortcode to display most viewed posts with thumbnails if available
function mvp_most_viewed_posts_shortcode($atts) {
    $atts = shortcode_atts(array(
        'posts' => 5,
        'post_type' => 'post',
    ), $atts, 'most_viewed_posts');

    $args = array(
        'posts_per_page' => intval($atts['posts']),
        'meta_key' => 'mvp_post_views_count',
        'orderby' => 'meta_value_num',
        'order' => 'DESC',
        'post_type' => sanitize_text_field($atts['post_type']),
        'post_status' => 'publish',
    );

    $query = new WP_Query($args);

    if ($query->have_posts()) {
        $output = '<ul class="most-viewed-posts">';
        while ($query->have_posts()) {
            $query->the_post();

            $output .= '<li>';
            if (has_post_thumbnail()) {
                $output .= '<a href="' . esc_url(get_permalink()) . '" class="post-view-image">' . get_the_post_thumbnail(get_the_ID(), 'thumbnail') . '</a> ';
            }
            $output .= '<a href="' . esc_url(get_permalink()) . '" class="post-view-title">' . get_the_title() . '</a>';
            $output .= '<br><span class="post-view-meta">' . get_the_author() . ' | ' . get_the_date() . '</span>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = 'No posts found';
    }

    return $output;
}
add_shortcode('most_viewed_posts', 'mvp_most_viewed_posts_shortcode');
