from manim import *
import numpy as np
import random

class StickmanFight(Scene):
    def construct(self):
        # 16 FPS for that smooth TikTok/YouTube feel
        self.camera.frame_rate = 16
        self.camera.background_color = "#F0F0F0"  # Paper white background
        
        # ---------- HAND-DRAWN STYLE SETTINGS ----------
        # Slight wiggle for that "drawn" feel
        wiggle = 0.02
        
        # ---------- SCENE 1: STANDOFF ----------
        # Create Blue - confident stance
        blue = self.draw_stickman(
            color="#4169E1",  # Royal blue
            position=LEFT * 3.5 + DOWN * 0.5,
            pose="ready",
            name="Blue"
        )
        
        # Create Yellow - calm, ready
        yellow = self.draw_stickman(
            color="#FFA500",  # Orange
            position=RIGHT * 3.5 + DOWN * 0.5,
            pose="calm",
            name="Yellow"
        )
        
        # Ground line
        ground = Line(LEFT * 7, RIGHT * 7, color="#888888", stroke_width=3)
        ground.shift(DOWN * 1.8)
        
        # Dust/sketch marks
        dust = self.draw_dust(LEFT * 2)
        
        # Add everything
        self.add(ground, dust, blue, yellow)
        self.wait(0.5)
        
        # Blue ignites light stick - ACTION LINE!
        light_stick = self.draw_light_stick(blue)
        self.play(
            Create(light_stick),
            run_time=0.2
        )
        
        # Dialogue with hand-drawn bubbles
        blue_text = self.speech_bubble(
            "This ends now.", 
            blue, 
            color="#4169E1"
        )
        self.play(Write(blue_text), run_time=0.5)
        self.wait(0.8)
        self.remove(blue_text)
        
        yellow_text = self.speech_bubble(
            "Agreed.", 
            yellow,
            color="#FFA500"
        )
        self.play(Write(yellow_text), run_time=0.4)
        self.wait(0.5)
        self.remove(yellow_text)
        
        # ---------- SCENE 2: FIRST SHOT ----------
        # Yellow draws arrow
        arrow = self.draw_arrow(color="#FFA500")
        arrow.move_to(yellow.get_center() + RIGHT * 0.8 + UP * 0.3)
        self.add(arrow)
        
        # Fire! - with motion lines
        self.play(
            arrow.animate.move_to(blue.get_center() + UP * 0.3),
            run_time=0.15
        )
        
        # Deflect - IMPACT LINES!
        impact = self.draw_impact(arrow.get_center())
        self.play(
            light_stick.animate.rotate(90 * DEGREES),
            FadeOut(arrow),
            Create(impact),
            run_time=0.1
        )
        self.remove(impact)
        
        blue_text = self.thought_bubble("Too slow.", blue, color="#4169E1")
        self.play(Write(blue_text), run_time=0.3)
        self.wait(0.3)
        self.remove(blue_text)
        
        # ---------- SCENE 3: RAPID FIRE + CHARGE ----------
        # Blue charges - RUNNING LINES!
        run_lines = self.draw_motion_lines(blue, direction=RIGHT)
        self.play(
            blue.animate.move_to(RIGHT * 0.5 + DOWN * 0.5),
            run_time=0.4
        )
        self.remove(run_lines)
        
        # Three arrows rapid fire
        for i in range(3):
            arrow = self.draw_arrow(color="#FFA500")
            arrow.move_to(yellow.get_center() + RIGHT * 0.8 + UP * (0.2 + i * 0.15))
            self.add(arrow)
            
            self.play(
                arrow.animate.move_to(blue.get_center() + UP * (0.2 + i * 0.15)),
                run_time=0.1
            )
            
            impact = self.draw_impact(arrow.get_center())
            self.play(
                light_stick.animate.rotate(-60 * DEGREES),
                FadeOut(arrow),
                Create(impact),
                run_time=0.08
            )
            self.remove(impact)
        
        # Yellow steps back - SURPRISE!
        self.play(
            yellow.animate.shift(LEFT * 0.3),
            run_time=0.15
        )
        
        yellow_text = self.thought_bubble("...Okay.", yellow, color="#FFA500")
        self.play(Write(yellow_text), run_time=0.2)
        self.wait(0.3)
        self.remove(yellow_text)
        
        # ---------- SCENE 4: FINAL STANCE ----------
        # Blue raises weapon - DRAMATIC!
        self.play(
            blue.animate.shift(UP * 0.2),
            light_stick.animate.scale(1.2),
            run_time=0.3
        )
        
        blue_text = self.speech_bubble("Any last words?", blue, color="#4169E1")
        self.play(Write(blue_text), run_time=0.4)
        self.wait(0.5)
        self.remove(blue_text)
        
        # ---------- SCENE 5: THE SUCTION ARROW ----------
        # Yellow reaches back SLOWLY
        self.play(
            yellow.animate.rotate(-10 * DEGREES, about_point=yellow.get_center()),
            run_time=0.5
        )
        
        # Pull out special arrow - COMIC REVEAL!
        suction_arrow = self.draw_suction_arrow()
        suction_arrow.move_to(yellow.get_center() + RIGHT * 0.6 + UP * 0.2)
        self.play(
            Create(suction_arrow),
            run_time=0.2
        )
        
        yellow_text = self.speech_bubble("One.", yellow, color="#FFA500", bold=True)
        self.play(Write(yellow_text), run_time=0.3)
        self.wait(0.4)
        self.remove(yellow_text)
        
        # ---------- SCENE 6: THWIP! ----------
        # Fire - but different sound/feel
        self.play(
            suction_arrow.animate.move_to(blue.get_top() + UP * 0.3),
            run_time=0.15
        )
        
        # STICK! - comedy impact
        self.play(
            suction_arrow.animate.move_to(blue.get_top() + UP * 0.1),
            blue.animate.shift(DOWN * 0.1),
            run_time=0.08
        )
        
        # Blue confusion
        blue_text = self.thought_bubble("...What.", blue, color="#4169E1")
        self.play(Write(blue_text), run_time=0.2)
        self.wait(0.4)
        self.remove(blue_text)
        
        # DESPERATE PULLING - COMEDY GOLD
        for _ in range(4):
            self.play(
                blue.animate.shift(UP * 0.15),
                suction_arrow.animate.shift(UP * 0.15),
                run_time=0.08
            )
            self.play(
                blue.animate.shift(DOWN * 0.15),
                suction_arrow.animate.shift(DOWN * 0.15),
                run_time=0.08
            )
        
        # ---------- SCENE 7: DEFEAT ----------
        # Drop light stick - *clatter*
        self.play(
            light_stick.animate.scale(0.5).shift(DOWN * 0.5),
            FadeOut(light_stick, scale=0.5),
            run_time=0.2
        )
        
        # Yellow walks away - COOL!
        walk_lines = self.draw_motion_lines(yellow, direction=RIGHT)
        self.play(
            yellow.animate.move_to(RIGHT * 6 + DOWN * 0.5),
            walk_lines.animate.move_to(RIGHT * 6 + DOWN * 0.5),
            run_time=1
        )
        self.remove(walk_lines)
        
        # Victory speech
        yellow_text = self.speech_bubble(
            "Suction cup.\nNon-lethal.\nVery effective.", 
            yellow, 
            color="#FFA500",
            font_size=24
        )
        self.play(Write(yellow_text), run_time=0.8)
        self.wait(0.8)
        self.remove(yellow_text)
        
        # ---------- SCENE 8: ACCEPTANCE ----------
        # Blue alone - defeated pose
        self.play(
            blue.animate.shift(DOWN * 0.1),
            blue.animate.rotate(-5 * DEGREES, about_point=blue.get_center()),
            run_time=0.3
        )
        
        # One last pull attempt
        self.play(
            suction_arrow.animate.shift(UP * 0.1),
            run_time=0.08
        )
        self.play(
            suction_arrow.animate.shift(DOWN * 0.1),
            run_time=0.08
        )
        
        # ACCEPTANCE - character growth!
        blue_text = self.thought_bubble("...I can work with this.", blue, color="#4169E1")
        self.play(Write(blue_text), run_time=0.5)
        self.wait(0.8)
        self.remove(blue_text)
        
        # ---------- FINAL FRAME ----------
        self.clear()
        
        # Title card - COMIC STYLE!
        title = Text(
            "NEW AESTHETIC UNLOCKED",
            color="#4169E1",
            font_size=48,
            weight=BOLD,
            font="Comic Sans MS"
        )
        title.move_to(ORIGIN)
        
        # Sketchy underline
        underline = Line(
            title.get_left() + DOWN * 0.3,
            title.get_right() + DOWN * 0.3,
            color="#FFA500",
            stroke_width=8
        )
        underline.add_updater(lambda x: x.become(
            Line(
                title.get_left() + DOWN * 0.3 + LEFT * random.uniform(-0.02, 0.02),
                title.get_right() + DOWN * 0.3 + RIGHT * random.uniform(-0.02, 0.02),
                color="#FFA500",
                stroke_width=8
            )
        ))
        
        self.play(
            Write(title),
            Create(underline),
            run_time=0.8
        )
        self.wait(1)
        
        # ---------- BONUS: SELFIE ----------
        self.clear()
        
        # Simple phone frame
        phone = RoundedRectangle(
            height=6, 
            width=3, 
            corner_radius=0.3,
            color="#333333",
            stroke_width=6
        )
        phone.move_to(ORIGIN)
        
        # Blue with arrow still on head - COMMITMENT TO THE BIT
        blue_selfie = self.draw_stickman(
            color="#4169E1",
            position=ORIGIN + DOWN * 0.5,
            pose="selfie"
        )
        
        arrow_selfie = self.draw_suction_arrow()
        arrow_selfie.move_to(blue_selfie.get_top() + UP * 0.1)
        
        # Peace sign!
        peace = VGroup(
            Line(ORIGIN + RIGHT * 0.2 + UP * 0.3, ORIGIN + RIGHT * 0.2 + UP * 0.6),
            Line(ORIGIN + RIGHT * 0.4 + UP * 0.3, ORIGIN + RIGHT * 0.4 + UP * 0.6),
        )
        peace.set_color("#4169E1")
        peace.move_to(blue_selfie.get_center() + RIGHT * 0.5 + UP * 0.2)
        
        # Caption
        caption = Text(
            "#newaesthetic #worthit",
            color="#666666",
            font_size=20,
            font="Comic Sans MS"
        )
        caption.next_to(phone, DOWN, buff=0.3)
        
        self.add(phone, blue_selfie, arrow_selfie, peace, caption)
        self.wait(1.5)
    
    def draw_stickman(self, color, position, pose="neutral", name=""):
        """Draw a proper HAND-DRAWN style stickman"""
        group = VGroup()
        
        # Slight random offset for hand-drawn feel
        wiggle = 0.02
        
        # Head - slightly imperfect circle
        head = Circle(
            radius=0.28,
            color=color,
            stroke_width=6
        )
        head.move_to(position + UP * 1.2)
        head.apply_function(
            lambda p: p + np.array([random.uniform(-wiggle, wiggle) for _ in range(3)])
        )
        
        # Body - slightly wobbly line
        body = Line(
            position + UP * 0.9,
            position + DOWN * 0.3,
            color=color,
            stroke_width=6
        )
        body.apply_function(
            lambda p: p + np.array([random.uniform(-wiggle, wiggle) for _ in range(3)])
        )
        
        # Arms based on pose
        if pose == "ready":  # Blue fighting stance
            left_arm = Line(
                position + UP * 0.7,
                position + LEFT * 0.6 + UP * 0.4,
                color=color,
                stroke_width=5
            )
            right_arm = Line(
                position + UP * 0.7,
                position + RIGHT * 0.8 + UP * 0.2,  # Holding weapon
                color=color,
                stroke_width=5
            )
        elif pose == "calm":  # Yellow relaxed
            left_arm = Line(
                position + UP * 0.7,
                position + LEFT * 0.4 + UP * 0.3,
                color=color,
                stroke_width=5
            )
            right_arm = Line(
                position + UP * 0.7,
                position + RIGHT * 0.4 + UP * 0.3,
                color=color,
                stroke_width=5
            )
        elif pose == "selfie":  # Peace sign pose
            left_arm = Line(
                position + UP * 0.7,
                position + LEFT * 0.5 + DOWN * 0.1,
                color=color,
                stroke_width=5
            )
            right_arm = Line(
                position + UP * 0.7,
                position + RIGHT * 0.6 + UP * 0.1,
                color=color,
                stroke_width=5
            )
        else:  # Neutral/defeated
            left_arm = Line(
                position + UP * 0.7,
                position + LEFT * 0.5 + DOWN * 0.1,
                color=color,
                stroke_width=5
            )
            right_arm = Line(
                position + UP * 0.7,
                position + RIGHT * 0.5 + DOWN * 0.1,
                color=color,
                stroke_width=5
            )
        
        # Legs
        left_leg = Line(
            position + DOWN * 0.3,
            position + LEFT * 0.3 + DOWN * 0.9,
            color=color,
            stroke_width=5
        )
        right_leg = Line(
            position + DOWN * 0.3,
            position + RIGHT * 0.3 + DOWN * 0.9,
            color=color,
            stroke_width=5
        )
        
        # Add wiggle to all limbs
        for limb in [head, body, left_arm, right_arm, left_leg, right_leg]:
            limb.apply_function(
                lambda p: p + np.array([random.uniform(-wiggle, wiggle) for _ in range(3)])
            )
        
        group.add(head, body, left_arm, right_arm, left_leg, right_leg)
        return group
    
    def draw_light_stick(self, stickman):
        """Simple glowing stick - like a lightsaber but sketchy"""
        stick = Line(
            stickman.get_center() + RIGHT * 0.3 + UP * 0.5,
            stickman.get_center() + RIGHT * 0.3 + UP * 1.3,
            color="#00FFFF",
            stroke_width=12
        )
        # Slight wobble
        stick.apply_function(
            lambda p: p + np.array([random.uniform(-0.01, 0.01) for _ in range(3)])
        )
        return stick
    
    def draw_arrow(self, color):
        """Simple comic-style arrow"""
        shaft = Line(LEFT * 0.2, RIGHT * 0.6, color=color, stroke_width=4)
        tip = Polygon(
            [0.6, 0.05, 0],
            [0.7, 0, 0],
            [0.6, -0.05, 0],
            color=color,
            fill_opacity=1
        )
        return VGroup(shaft, tip)
    
    def draw_suction_arrow(self):
        """Comedy suction cup arrow"""
        shaft = Line(LEFT * 0.2, RIGHT * 0.5, color="#FFA500", stroke_width=4)
        cup = Arc(radius=0.2, angle=PI, color="#FF4444", stroke_width=6)
        cup.rotate(-90 * DEGREES)
        cup.move_to(RIGHT * 0.5)
        return VGroup(shaft, cup)
    
    def draw_impact(self, position):
        """Comic book impact lines"""
        lines = VGroup()
        for i in range(8):
            angle = i * 45 * DEGREES
            line = Line(
                position,
                position + np.array([np.cos(angle), np.sin(angle), 0]) * 0.2,
                color="#FFAA00",
                stroke_width=3
            )
            lines.add(line)
        return lines
    
    def draw_motion_lines(self, object, direction=RIGHT):
        """Speed lines for movement"""
        lines = VGroup()
        for i in range(5):
            line = Line(
                object.get_left() + LEFT * (i * 0.1),
                object.get_left() + LEFT * (i * 0.1 + 0.3),
                color="#CCCCCC",
                stroke_width=2
            )
            lines.add(line)
        return lines
    
    def draw_dust(self, position):
        """Sketchy dust marks"""
        dots = VGroup()
        for _ in range(10):
            dot = Dot(
                position + np.array([random.uniform(-0.5, 0.5), random.uniform(-0.3, 0.3), 0]),
                radius=random.uniform(0.01, 0.03),
                color="#AAAAAA"
            )
            dots.add(dot)
        return dots
    
    def speech_bubble(self, text, speaker, color="#000000", font_size=28, bold=False):
        """Comic style speech bubble"""
        txt = Text(
            text,
            color=color,
            font_size=font_size,
            font="Comic Sans MS",
            weight=BOLD if bold else NORMAL
        )
        txt.next_to(speaker, UP, buff=0.8)
        
        # Simple bubble background
        bubble = RoundedRectangle(
            width=txt.width + 0.6,
            height=txt.height + 0.4,
            corner_radius=0.2,
            color=color,
            fill_color="#FFFFFF",
            fill_opacity=0.9,
            stroke_width=3
        )
        bubble.move_to(txt.get_center())
        
        # Tail
        tail = Polygon(
            bubble.get_bottom() + LEFT * 0.1,
            bubble.get_bottom() + RIGHT * 0.1,
            speaker.get_top() + UP * 0.1,
            color=color,
            fill_color="#FFFFFF",
            fill_opacity=0.9,
            stroke_width=3
        )
        
        return VGroup(bubble, tail, txt)
    
    def thought_bubble(self, text, thinker, color="#666666", font_size=26):
        """Thought bubble (cloud style)"""
        txt = Text(
            text,
            color=color,
            font_size=font_size,
            font="Comic Sans MS"
        )
        txt.next_to(thinker, UP, buff=0.8)
        
        # Cloud bubble
        bubble = RoundedRectangle(
            width=txt.width + 0.6,
            height=txt.height + 0.4,
            corner_radius=0.4,
            color=color,
            fill_color="#FFFFFF",
            fill_opacity=0.9,
            stroke_width=2,
            stroke_opacity=0.8
        )
        bubble.move_to(txt.get_center())
        
        # Thought circles
        circle1 = Circle(radius=0.08, color=color, stroke_width=2)
        circle1.next_to(bubble, DOWN, buff=0.1)
        circle2 = Circle(radius=0.06, color=color, stroke_width=2)
        circle2.next_to(circle1, DOWN, buff=0.05)
        circle3 = Circle(radius=0.04, color=color, stroke_width=2)
        circle3.next_to(circle2, DOWN, buff=0.03)
        
        return VGroup(bubble, circle1, circle2, circle3, txt)
