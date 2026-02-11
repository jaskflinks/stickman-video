from manim import *
import numpy as np
import struct

class StickmanFight(Scene):
    # Colors at class level - accessible to all methods
    BLUE_COLOR = "#4A90E2"
    YELLOW_COLOR = "#F5A623"
    
    def construct(self):
        # Set 16 FPS
        self.camera.frame_rate = 16
        
        # ---------- SOUND EFFECTS ----------
        deflect_sound = self.create_sound_wave([500, 600, 700], 0.15)
        arrow_sound = self.create_sound_wave([400, 300], 0.1)
        thwip_sound = self.create_sound_wave([200, 150, 100], 0.08)
        struggle_sound = self.create_sound_wave([100, 120, 80], 0.2)
        walk_sound = self.create_sound_wave([60, 50], 0.3)
        shutter_sound = self.create_sound_wave([800, 600], 0.05)
        
        # Create stick figures
        blue = self.create_stickman(self.BLUE_COLOR, LEFT * 3)
        yellow = self.create_stickman(self.YELLOW_COLOR, RIGHT * 3)
        
        # Add glow stick to Blue
        glow_stick = Line(
            blue.get_top() + RIGHT * 0.5,
            blue.get_top() + RIGHT * 0.5 + UP * 1.5,
            color=self.BLUE_COLOR,
            stroke_width=8
        )
        glow_stick.add_updater(lambda x: x.become(
            Line(
                blue.get_top() + RIGHT * 0.5,
                blue.get_top() + RIGHT * 0.5 + UP * 1.5,
                color=self.BLUE_COLOR,
                stroke_width=8
            ).set_opacity(0.8)
        ))
        
        # Add bow to Yellow
        bow = self.create_bow(yellow)
        
        # Dust effect
        dust = VGroup(*[
            Dot(
                np.array([np.random.uniform(-1, 1), -2, 0]),
                radius=0.03,
                color=GRAY
            ) for _ in range(20)
        ])
        
        # Setup scene
        self.add(blue, yellow, glow_stick, bow, dust)
        self.wait(0.5)
        
        # Dialogue
        blue_text = Text("This ends now.", color=self.BLUE_COLOR, font_size=30).next_to(blue, UP, buff=0.8)
        self.play(Write(blue_text), run_time=1)
        self.wait(0.5)
        self.remove(blue_text)
        
        yellow_text = Text("Agreed.", color=self.YELLOW_COLOR, font_size=30).next_to(yellow, UP, buff=0.8)
        self.play(Write(yellow_text), run_time=0.8)
        self.wait(0.5)
        self.remove(yellow_text)
        
        # ---------- SCENE 2 ----------
        arrow = self.create_arrow(self.YELLOW_COLOR)
        arrow.move_to(yellow.get_right() + RIGHT * 0.5 + UP * 0.3)
        
        self.add_sound(arrow_sound, time_offset=0)
        self.play(
            arrow.animate.move_to(blue.get_center() + UP * 0.3),
            run_time=0.3
        )
        
        self.add_sound(deflect_sound, time_offset=0)
        self.play(
            glow_stick.animate.rotate(90 * DEGREES),
            FadeOut(arrow),
            run_time=0.2
        )
        
        blue_text = Text("Too slow.", color=self.BLUE_COLOR, font_size=30).next_to(blue, UP, buff=0.8)
        self.play(Write(blue_text), run_time=0.5)
        self.wait(0.3)
        self.remove(blue_text)
        
        # ---------- SCENE 3 ----------
        self.play(
            blue.animate.move_to(RIGHT * 1),
            glow_stick.animate.move_to(RIGHT * 1.5 + UP * 1),
            run_time=0.8
        )
        
        for i in range(3):
            arrow = self.create_arrow(self.YELLOW_COLOR)
            arrow.move_to(yellow.get_right() + RIGHT * 0.5 + UP * (0.3 + i * 0.2))
            self.add(arrow)
            self.add_sound(arrow_sound, time_offset=0)
            self.play(
                arrow.animate.move_to(blue.get_center() + UP * (0.3 + i * 0.1)),
                run_time=0.2
            )
            self.add_sound(deflect_sound, time_offset=0)
            self.play(
                glow_stick.animate.rotate(-60 * DEGREES),
                FadeOut(arrow),
                run_time=0.1
            )
        
        yellow_text = Text("...Okay.", color=self.YELLOW_COLOR, font_size=30).next_to(yellow, UP, buff=0.8)
        self.play(Write(yellow_text), run_time=0.3)
        self.wait(0.3)
        self.remove(yellow_text)
        
        # ---------- SCENE 4 ----------
        self.play(
            glow_stick.animate.scale(1.2),
            blue.animate.shift(UP * 0.3),
            run_time=0.5
        )
        
        blue_text = Text("Any last words?", color=self.BLUE_COLOR, font_size=30).next_to(blue, UP, buff=0.8)
        self.play(Write(blue_text), run_time=0.8)
        self.wait(0.3)
        self.remove(blue_text)
        
        # ---------- SCENE 5 ----------
        suction_arrow = self.create_arrow(self.YELLOW_COLOR, tip_radius=0.3)
        suction_arrow.move_to(yellow.get_right() + RIGHT * 0.5 + UP * 0.3)
        
        yellow_text = Text("One.", color=self.YELLOW_COLOR, font_size=30, weight=BOLD).next_to(yellow, UP, buff=0.8)
        self.play(Write(yellow_text), run_time=0.5)
        self.wait(0.5)
        self.remove(yellow_text)
        
        # ---------- SCENE 6 ----------
        self.add_sound(arrow_sound, time_offset=0)
        self.play(
            suction_arrow.animate.move_to(blue.get_top() + UP * 0.5),
            run_time=0.3
        )
        
        self.add_sound(thwip_sound, time_offset=0)
        self.play(
            suction_arrow.animate.move_to(blue.get_top() + UP * 0.2),
            run_time=0.1
        )
        
        blue_text = Text("...What.", color=self.BLUE_COLOR, font_size=30).next_to(blue, UP, buff=1.2)
        self.play(Write(blue_text), run_time=0.3)
        self.wait(0.5)
        self.remove(blue_text)
        
        for _ in range(3):
            self.add_sound(struggle_sound, time_offset=0)
            self.play(
                blue.animate.shift(UP * 0.1),
                suction_arrow.animate.shift(UP * 0.1),
                run_time=0.1
            )
            self.play(
                blue.animate.shift(DOWN * 0.1),
                suction_arrow.animate.shift(DOWN * 0.1),
                run_time=0.1
            )
        
        # ---------- SCENE 7 ----------
        self.play(
            FadeOut(glow_stick),
            run_time=0.3
        )
        
        self.add_sound(walk_sound, time_offset=0)
        self.play(
            yellow.animate.move_to(RIGHT * 5 + DOWN * 0.5),
            bow.animate.move_to(RIGHT * 5 + DOWN * 0.5),
            run_time=1
        )
        
        yellow_text = Text("Suction cup. Non-lethal. Very effective.", 
                          color=self.YELLOW_COLOR, font_size=28).next_to(yellow, UP, buff=0.5)
        self.play(Write(yellow_text), run_time=1)
        self.wait(1)
        self.remove(yellow_text)
        
        # ---------- SCENE 8 ----------
        self.play(
            blue.animate.shift(DOWN * 0.2),
            run_time=0.5
        )
        
        for _ in range(2):
            self.add_sound(struggle_sound, time_offset=0)
            self.play(
                suction_arrow.animate.shift(UP * 0.1),
                run_time=0.1
            )
            self.play(
                suction_arrow.animate.shift(DOWN * 0.1),
                run_time=0.1
            )
        
        blue_text = Text("...I can work with this.", 
                        color=self.BLUE_COLOR, font_size=30).next_to(blue, UP, buff=1.2)
        self.play(Write(blue_text), run_time=0.8)
        self.wait(1)
        
        # ---------- FINAL FRAME ----------
        self.clear()
        
        title = Text("New aesthetic unlocked.", 
                    color=self.BLUE_COLOR, font_size=48, weight=BOLD)
        title.move_to(ORIGIN)
        
        self.play(Write(title), run_time=1)
        self.wait(1)
        
        # ---------- BONUS: SELFIE ----------
        self.clear()
        
        blue_selfie = self.create_stickman(self.BLUE_COLOR, ORIGIN + DOWN * 1)
        suction_arrow_selfie = self.create_arrow(self.YELLOW_COLOR, tip_radius=0.3)
        suction_arrow_selfie.move_to(blue_selfie.get_top() + UP * 0.2)
        
        phone_frame = Rectangle(height=6, width=3.5, color=WHITE)
        camera_flash = Dot(phone_frame.get_top() + RIGHT * 1.2 + DOWN * 0.3, 
                          radius=0.1, color=self.YELLOW_COLOR)
        
        self.add(phone_frame, blue_selfie, suction_arrow_selfie, camera_flash)
        
        self.add_sound(shutter_sound, time_offset=0)
        flash = FullScreenRectangle(color=WHITE, fill_opacity=0.8)
        self.play(FadeIn(flash), run_time=0.05)
        self.remove(flash)
        self.wait(2)
    
    def create_sound_wave(self, frequencies, duration):
        """Generate a simple sine wave sound"""
        sample_rate = 44100
        samples = []
        
        for freq in frequencies:
            t = np.linspace(0, duration/len(frequencies), 
                          int(sample_rate * duration/len(frequencies)))
            wave = np.sin(2 * np.pi * freq * t) * 0.3
            samples.extend(wave)
        
        samples = np.array(samples, dtype=np.float32)
        byte_data = b''.join(struct.pack('<f', s) for s in samples)
        return byte_data
    
    def create_stickman(self, color, position):
        """Create a stick figure"""
        head = Circle(radius=0.3, color=color, stroke_width=4).move_to(position + UP * 1.5)
        body = Line(position + UP * 1.2, position + DOWN * 0.5, color=color, stroke_width=4)
        
        left_arm = Line(position + UP * 0.8, position + LEFT * 0.5 + UP * 0.8, 
                       color=color, stroke_width=4)
        right_arm = Line(position + UP * 0.8, position + RIGHT * 0.5 + UP * 0.8, 
                        color=color, stroke_width=4)
        
        left_leg = Line(position + DOWN * 0.5, position + LEFT * 0.4 + DOWN * 1.2, 
                       color=color, stroke_width=4)
        right_leg = Line(position + DOWN * 0.5, position + RIGHT * 0.4 + DOWN * 1.2, 
                        color=color, stroke_width=4)
        
        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
    
    def create_bow(self, stickman):
        """Create a bow for Yellow"""
        bow = Arc(radius=0.8, angle=PI/2, color=self.YELLOW_COLOR, stroke_width=6)
        bow.rotate(-PI/4)
        bow.move_to(stickman.get_right() + RIGHT * 0.3 + UP * 0.5)
        return bow
    
    def create_arrow(self, arrow_color, tip_radius=0.1):
        """Create an arrow - FIXED: renamed parameter to avoid shadowing"""
        shaft = Line(LEFT * 0.3, RIGHT * 0.7, color=arrow_color, stroke_width=3)
        tip = Dot(radius=tip_radius, color=arrow_color).move_to(RIGHT * 0.7)
        return VGroup(shaft, tip)
