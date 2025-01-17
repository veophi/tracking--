import sys
import cv2
import os
from motion_detect import motion_detector as motd
import gui.util.cv_rectutil as cvrect
import gui.util.cv_drawline as cvline
import gui.backend_gui_bridge as bridge


def main():
    assert len(sys.argv) == 2;
    assert os.path.isfile(sys.argv[1])
    cap = cv2.VideoCapture(sys.argv[1])
    ret, frame = cap.read()
    rois = cv2.selectROIs("Select Areas", frame)
    cv2.destroyWindow("Select Areas")
    lines = cvline.selectLines("Select Lines", frame)
    cap.release()
    b = bridge.BackendGuiBridge(sys.argv[1], lines, rois)
    succ, frame = b.get_frame()
    while succ:
        if (cv2.waitKey(100) & 0xFF == ord('q')):
            break
        cv2.imshow("Tracking", frame)
        succ, frame = b.get_frame()


# 用法： python cli_main.py <视频文件路径>
if __name__ == '__main__':
    main()
