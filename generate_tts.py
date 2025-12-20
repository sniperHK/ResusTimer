#!/usr/bin/env python3
"""
Generate MP3 files from text-to-speech for CPR voice prompts
Uses macOS 'say' command with Tingting voice
"""

import pandas as pd
import subprocess
import os
import re

# Configuration
EXCEL_FILE = '音效腳本(傳送).xlsx'
OUTPUT_DIR = 'voice_mp3'
VOICE = 'Tingting'  # 婷婷 - Chinese TTS voice
RATE = 180  # Speech rate (words per minute)

def clean_filename(text, max_len=50):
    """Create a safe filename from text"""
    # Remove special characters
    clean = re.sub(r'[\\/:*?"<>|\n\r]', '_', text)
    clean = re.sub(r'\s+', '_', clean)
    clean = clean.strip('_')
    return clean[:max_len] if len(clean) > max_len else clean

def clean_text_for_speech(text):
    """Clean text for better TTS output"""
    if pd.isna(text):
        return None
    # Remove parenthetical notes for cleaner speech
    text = str(text)
    # Keep the main content but clean up formatting
    text = text.replace('\n', '，')
    text = text.replace('\\n', '，')
    text = re.sub(r'（[^）]*）', '', text)  # Remove Chinese parentheses content
    text = re.sub(r'\([^)]*\)', '', text)   # Remove English parentheses content
    text = text.strip()
    return text if text else None

def generate_mp3(text, output_path, voice=VOICE, rate=RATE):
    """Generate MP3 from text using macOS say command"""
    # First generate AIFF
    aiff_path = output_path.replace('.mp3', '.aiff')

    # Use say command to generate audio
    say_cmd = ['say', '-v', voice, '-r', str(rate), '-o', aiff_path, text]
    subprocess.run(say_cmd, check=True)

    # Convert to MP3 using ffmpeg
    ffmpeg_cmd = [
        'ffmpeg', '-y', '-i', aiff_path,
        '-codec:a', 'libmp3lame', '-qscale:a', '2',
        output_path
    ]
    subprocess.run(ffmpeg_cmd, check=True, capture_output=True)

    # Remove intermediate AIFF file
    os.remove(aiff_path)

    return output_path

def main():
    # Read Excel file
    df = pd.read_excel(EXCEL_FILE)
    print(f"Found {len(df)} rows in Excel file")
    print(f"Columns: {list(df.columns)}")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process each row
    generated_files = []
    for idx, row in df.iterrows():
        time_str = str(row.iloc[0]).strip()
        voice_content = row.iloc[1]

        # Skip rows with no content or placeholder content
        if pd.isna(voice_content) or str(voice_content).strip() == '...':
            print(f"Skipping row {idx}: no content")
            continue

        # Clean text for speech
        speech_text = clean_text_for_speech(voice_content)
        if not speech_text:
            print(f"Skipping row {idx}: empty after cleaning")
            continue

        # Create filename
        time_clean = time_str.replace(':', '-').replace(' ', '_')
        content_preview = clean_filename(speech_text, 30)
        filename = f"{idx+1:02d}_{time_clean}_{content_preview}.mp3"
        output_path = os.path.join(OUTPUT_DIR, filename)

        print(f"\nProcessing row {idx+1}:")
        print(f"  Time: {time_str}")
        print(f"  Text: {speech_text[:50]}...")
        print(f"  Output: {filename}")

        try:
            generate_mp3(speech_text, output_path)
            generated_files.append(output_path)
            print(f"  ✓ Generated successfully")
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print(f"\n{'='*50}")
    print(f"Generated {len(generated_files)} MP3 files in '{OUTPUT_DIR}/'")

    return generated_files

if __name__ == '__main__':
    main()
