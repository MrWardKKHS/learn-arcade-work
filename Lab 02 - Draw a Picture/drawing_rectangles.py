import arcade

arcade.open_window(600, 400, 'drawing example')

arcade.set_background_color(arcade.color.TIMBERWOLF)

arcade.start_render()

# To Print physicals - all 2D primitives 
arcade.draw_rectangle_outline(250,140, 100, 100, arcade.color.RED_PURPLE)
arcade.draw_lrtb_rectangle_filled(20, 50, 300, 10, arcade.color.MEDIUM_RUBY)

arcade.finish_render()

arcade.run()

# USE AS MANY OF THESE AS POSSIBLE
# draw_arc_filled
# draw_arc_outline
# draw_circle_filled
# draw_circle_outline
# draw_ellipse_filled
# draw_ellipse_outline
# draw_line
# draw_line_strip
# draw_lines
# draw_lrtb_rectangle_filled
# draw_lrtb_rectangle_outline
# draw_lrwh_rectangle_textured
# draw_parabola_filled
# draw_parabola_outline
# draw_point
# draw_points
# draw_polygon_filled
# draw_polygon_outline
# draw_rectangle_filled
# draw_rectangle_outline
# draw_scaled_texture_rectangle
# draw_texture_rectangle
# draw_triangle_filled
# draw_triangle_outline
# draw_xywh_rectangle_filled
# draw_xywh_rectangle_outline