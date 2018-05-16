CUDA_VISIBLE_DEVICES=2 ./darknet detector test cfg/dota.data cfg/yolo-dota.cfg dota-backup/yolo-dota.cfg_450000.weights ../dota_data/YOLO/test/images/P0017__1__0___0.jpg -thresh 0.1
