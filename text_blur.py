import cv2
import numpy as np
import json
import os

def text_blur_main(file_name, json_file_name):
    cap = None
    out = None
    try:
        # Reading the json file into a variable
        final_time = {}
        with open(f'text_json/{json_file_name}', 'r') as file:
            final_time = json.load(file)        
        
        # Load video
        cap = cv2.VideoCapture(f'inputs/{file_name}')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # Get the frame width and height
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_rate = cap.get(cv2.CAP_PROP_FPS)

        out = cv2.VideoWriter(f'final/{file_name}', fourcc, frame_rate, (frame_width, frame_height))

        print('frame_width => ', frame_width)
        print('frame_height => ', frame_height)
        print('frame_rate => ', frame_rate)

        total_frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # Process video
        frame_counter = 0
        while cap.isOpened():
            ret, frame = cap.read()
            frame_counter += 1
            if frame_counter%100 == 0:
                print('processing frame => ', frame_counter)

            if not ret:
                break
            
            for t in final_time:
                vertices = final_time.get(t, [])
                # print('vertices len => ', len(vertices))
                lower_bound = int(int(t)  * frame_rate)
                upper_bound = int(int(t) * frame_rate + frame_rate / 1) + 1
                if len(vertices) > 0 and (frame_counter >= lower_bound) and (frame_counter <= upper_bound):
                    for v in vertices:
                        # print('v => ', v)
                        draw_bounding_box(frame, v)

            out.write(frame)
        return True
    except Exception as e:
        print('Error in text_blur main')
        print(e)
        return False
    finally:
        # Release resources
        if cap != None:
            try:
                cap.release()
            except Exception as e:
                print('Error releasing resource')

        if out != None:
            try:
                out.release()
            except Exception as e:
                print('Error releasing resource')

        # Remove the files
        try:
            os.remove(f'inputs/{file_name}')
        except Exception as e:
            print('Error while removing file')

        try:
            os.remove(f'text_json/{json_file_name}')
        except Exception as e:
            print('Error while removing file')



def anonymize_face_pixelate(image, blocks=30):
    """
    Computes a pixelated blur with OpenCV
    Args:
        image (ndarray): The image to be blurred
        blocks (int): Number of pixel blocks (default is 10)
    Returns:
        image (ndarray): The blurred image
    """
    # divide the input image into NxN blocks
    (h, w) = image.shape[:2]
    x_coordinates, y_coordinates = np.linspace(0, w, blocks + 1, dtype="int"), np.linspace(0, h, blocks + 1, dtype="int")
    
    # loop over the blocks along x and y axis
    for i in range(1, len(y_coordinates)):
        for j in range(1, len(x_coordinates)):
            # compute the first and last (x, y)-coordinates for the current block
            first_x, last_x = x_coordinates[j - 1], x_coordinates[j]
            first_y, last_y = y_coordinates[i - 1], y_coordinates[i]
            # extract the ROI
            roi = image[first_y:last_y, first_x:last_x]
            # compute the mean of the ROI 
            (b, g, r) = [int(x) for x in cv2.mean(roi)[:3]]
            # draw a rectangle with the mean RGB values over the ROI in the original image
            cv2.rectangle(image, (first_x, first_y), (last_x, last_y), (b, g, r), -1)

    # return the pixelated blurred image
    return image


def draw_bounding_box(frame, vertices):
    # Convert normalized coordinates to pixel coordinates
    height, width, _ = frame.shape

    # for v in vertices:
    #     print('v.get => ', v.get('x', 0.0))

    points = [(int(v.get('x', 0.0) * width), int(v.get('y', 0.0) * height)) for v in vertices]

    # Draw the bounding box
    # points = np.array(points, dtype=np.int32)
    # cv2.polylines(frame, [points], isClosed=True, color=(255, 0, 0), thickness=2)
    
    # Blur the above part
    x1 = points[0][0]
    y1 = points[0][1]

    x2 = points[2][0]
    y2 = points[2][1]

    to_blur = frame[y1:y2, x1:x2]
    # blurred = anonymize_face_pixelate(to_blur, blocks=10)
    # print('to_blur => ', to_blur)
    if len(to_blur) > 0:
        # print('in here -- ', to_blur, ' --- ', len(to_blur))
        try:
            blurred = cv2.GaussianBlur(to_blur, (99, 99), 30)
            frame[y1:y2, x1:x2] = blurred
        except Exception as e:
            print(e)