import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np

# Clase encargada de recibir, procesar y publicar la señal modificada.
class SignalProcessor(Node):
    # Constructores de suscriptores, publicador y timer, y definición de variables
    def __init__(self):
        super().__init__('process_ROSario')
        
        self.subscription0 = self.create_subscription(Float32, 'signal_ROSario', self.listener_callback,10)
        self.subscription0 #No unusedvariable warning
        self.subscription1 = self.create_subscription(Float32, 'time_ROSario', self.empty_callback , 10)
        self.subscription1 #No unusedvariable warning
        
        self.publisher2 = self.create_publisher(Float32, 'proc_signal_ROSario', 10)
        timer_period = 0.25 # 4 Hz
        self.timer = self.create_timer(timer_period, self.talker_callback)

        self.y = 0
        self.g = 0

    # Función encargada del procesamiento de la señal recibida en el tópico "/signal_ROSario"
    def listener_callback(self, msg2):
        self.get_logger().info('I heard from /signal_ROSario: "%s"' % msg2.data)

        self.y = msg2.data
        self.g = -0.5 * self.y + 0.5     

    # Función encargada de publicar la señal procesada anteriormente
    def talker_callback(self):
        msg3 = Float32()
        msg3.data = self.g
        self.publisher2.publish(msg3)
        self.get_logger().info('Publishing in /proc_signal_ROSario: "%f"' % msg3.data)

    # Función asociada a la suscripción del tópico "/time_ROSario"
    def empty_callback(self, msg4):
        pass



#Main
def main(args=None):
    rclpy.init(args=args)

    process_signal  = SignalProcessor()

    try:
        rclpy.spin(process_signal)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():  # Ensure shutdown is only called once
            rclpy.shutdown()
        process_signal.destroy_node()


#Execute Node
if __name__ == '__main__':
    main()