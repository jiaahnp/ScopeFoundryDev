from ScopeFoundry import BaseMicroscopeApp  
from ScopeFoundry.examples.hardware.dummy_xy_stage import DummyXYStage
from base_cartesian_scan import TestCartesian2DSlowScan

class TestCartesian2DSlowScanApp(BaseMicroscopeApp):
    
    name = 'app'

    def setup(self):
        
        stage = self.add_hardware_component(DummyXYStage(self))
        stage.connect()
        self.test_cart_2d_slow_scan = self.add_measurement_component(TestCartesian2DSlowScan(self))
        
        self.ui.show()
        
        self.ui.mdiArea.addSubWindow(self.test_cart_2d_slow_scan.ui)
        
        


if __name__ == '__main__':
    import sys
    app = TestCartesian2DSlowScanApp([])
    sys.exit(app.exec_())    

