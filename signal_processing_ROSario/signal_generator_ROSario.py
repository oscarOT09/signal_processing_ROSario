import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np

# Clase encargada de generar y publicar una señal senoidal junto con su correspondiente valor de tiempo.
class SignalGenerator(Node):
    # Constructores de publicadores y timer, y definición de variables
    def __init__(self):
        super().__init__('signal_generator_ROSario')
        self.publisher0 = self.create_publisher(Float32, 'time_ROSario', 10)
        self.publisher1 = self.create_publisher(Float32, 'signal_ROSario', 10)
        timer_period = 0.1 # 10 Hz
        self.timer = self.create_timer(timer_period, self.timer_cb)
        self.t = 0.0
        self.y = 0.0

    # Función encargada de publicar los datos correspondientes a los diferentes tópicos
    def timer_cb(self):
        msg0 = Float32()
        msg0.data = self.t
        self.publisher0.publish(msg0)
        self.get_logger().info('Publishing in /time_ROSario: "%f"' % msg0.data)

        msg1 = Float32()
        self.y = np.sin(self.t)
        msg1.data = self.y
        self.publisher1.publish(msg1)
        self.get_logger().info('Publishing in /signal_ROSario: "%f"' % msg1.data)

        self.t = self.t + 0.1

def main(args=None):
    rclpy.init(args=args)

    signal_generator = SignalGenerator()

    try:
        rclpy.spin(signal_generator)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()
        signal_generator.destroy_node()
    
if __name__ == '__main__':
    main()