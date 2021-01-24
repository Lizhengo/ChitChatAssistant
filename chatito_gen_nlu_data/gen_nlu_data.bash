#!/usr/bin/env bash

npx chatito .\trainClimateBot.chatito --format=rasa
rasa data convert nlu --data .\rasa_dataset_training.json --out .\trip_nlu_augment.md -f md