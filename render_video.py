import os
import sys

def render_video():
    """Render the animation without requiring shell access"""
    try:
        from manim import config, tempconfig
        
        # Configure for phone/render.com
        with tempconfig({
            "quality": "low_quality",
            "frame_rate": 16,
            "pixel_width": 720,
            "pixel_height": 1280,
            "output_file": "stickman_fight",
            "disable_caching": True,
            "save_last_frame": False,
            "save_pngs": False
        }):
            # Import and render
            from main import StickmanFight
            scene = StickmanFight()
            scene.render()
            
        print("✅ Video rendered successfully!")
        print("📁 Output file: media/videos/main/720p16/StickmanFight.mp4")
        
        # Create download page
        with open("index.html", "w") as f:
            f.write("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Download Stickman Video</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding: 20px;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        min-height: 100vh;
                        margin: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    .container {
                        background: rgba(255,255,255,0.1);
                        backdrop-filter: blur(10px);
                        padding: 40px;
                        border-radius: 20px;
                        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                        max-width: 600px;
                    }
                    h1 {
                        margin-bottom: 20px;
                        font-size: 2em;
                    }
                    .download-btn {
                        background: #4A90E2;
                        color: white;
                        padding: 15px 40px;
                        text-decoration: none;
                        border-radius: 50px;
                        font-size: 20px;
                        font-weight: bold;
                        display: inline-block;
                        margin: 20px 0;
                        transition: transform 0.3s, box-shadow 0.3s;
                        border: none;
                        cursor: pointer;
                    }
                    .download-btn:hover {
                        transform: translateY(-2px);
                        box-shadow: 0 10px 30px rgba(74,144,226,0.5);
                    }
                    .info {
                        margin-top: 30px;
                        color: rgba(255,255,255,0.8);
                        font-size: 14px;
                    }
                    .success {
                        color: #4CAF50;
                        font-size: 48px;
                        margin-bottom: 20px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="success">✅</div>
                    <h1>Your Stickman Video is Ready!</h1>
                    <p style="font-size: 18px; margin-bottom: 30px;">
                        "The Light Stick vs. The Bow"<br>
                        <span style="font-size: 14px;">16 FPS | 30 Seconds | With Sound Effects</span>
                    </p>
                    <a href="/media/videos/main/720p16/StickmanFight.mp4" 
                       download="stickman_fight.mp4" 
                       class="download-btn">
                        📥 Download Video
                    </a>
                    <div class="info">
                        ⚡ Video includes sound effects<br>
                        🎬 8 scenes + bonus selfie frame<br>
                        😂 "New aesthetic unlocked."
                    </div>
                </div>
            </body>
            </html>
            """)
        
        print("✅ Download page created: index.html")
        print("🌐 Visit your Render URL to download the video")
        
    except Exception as e:
        print(f"❌ Error rendering video: {e}")
        sys.exit(1)

if __name__ == "__main__":
    render_video()
