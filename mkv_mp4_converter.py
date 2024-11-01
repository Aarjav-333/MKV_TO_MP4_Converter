from moviepy.editor import VideoFileClip

def convert_mkv_to_mp4(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', 
                                    remove_temp=True, threads=4, fps=24)
        print(f"Conversion successful: '{output_file}' created.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        video_clip.close()

def main():
    input_file = r"Your_File_Path"
    output_file = r"Your_File_Path"  
    
    convert_mkv_to_mp4(input_file, output_file)

if __name__ == "__main__":
    main()
