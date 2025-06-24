AI Internship Assignment - Player Re-Identification  
Player Re-Identification in a Single Video Feed   
Company: Liat.ai 
Project Overview: 
This project identifies and tracks football players within a 15-second match video using 
YOLOv11. Each player is assigned a unique ID, and when players move out of frame and 
return, the system maintains their identity consistently. 
Tools & Technologies: 
• Python 
• Ultralytics (YOLOv11) 
• OpenCV 
• NumPy 
Approach: 
1. Used YOLOv11 model to detect players in every frame. 
2. Calculated center points of detected players. 
3. Used position matching logic to re-identify players when they re-enter the frame. 
4. Displayed bounding boxes and player IDs on the video. 
5. Saved the output video as `output_with_ids.mp4`. 
Output: 
The output video shows the AI detection system identifying and labeling players 
consistently throughout the video. 
Model Used: 
YOLOv11 provided in the assignment drive link.
