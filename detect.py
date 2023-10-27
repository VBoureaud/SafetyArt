from ultralytics import YOLO
from ultralytics import settings

# Update setting
settings.update({
	'datasets_dir': './data/',
	'runs_dir': './data/',
	'tensorboard': True,
})

# Load a pretrained YOLO model
model = YOLO('./models/yolov8n_best.onnx')

# Perform object detection on an image using the model
results = model.predict(
	source='data/',
	save=True,
	save_txt=False,
	hide_conf=True,
	classes=[0,1,2,3,4,6]#show only labels0-8, no 5 (Person label)
)