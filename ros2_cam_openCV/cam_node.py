import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class UvcCameraNode(Node):
    def __init__(self):
        super().__init__('uvc_camera_node')
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(Image, 'camera/image', 10)
        self.timer = self.create_timer(1/30, self.timer_callback)  # Adjust the interval as needed --> here should be 30 Hz for usb webcam (30fps)

        # Initialize the UVC camera capture
        self.cap = cv2.VideoCapture(0)  # Modify the index if needed

        # Set the desired resolution
        width = 640
        height = 480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform any necessary image processing or hardware acceleration here
            # Example: Apply a grayscale filter using the GPU-accelerated function
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Flip the image
            frame_flipped = cv2.flip(frame_gray, 0)

            # Convert the processed frame to a ROS Image message
            # img_msg = self.bridge.cv2_to_imgmsg(frame_gray, 'mono8') # or 'bgr8' for colored image
            img_msg = self.bridge.cv2_to_imgmsg(frame_flipped, 'mono8')

            # Publish the processed image
            self.publisher.publish(img_msg)

def main(args=None):
    rclpy.init(args=args)
    node = UvcCameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
