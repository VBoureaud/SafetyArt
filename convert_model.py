from ultralytics import YOLO

model = YOLO('yolov8n_best.pt')
success = model.export(format='onnx')
