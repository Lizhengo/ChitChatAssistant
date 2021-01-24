## happy path
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_trip_jiaoban
    - action_trip_hotel_recommend
    - action_trip_flight_recommend
    - action_restart
    
## happy path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_trip_jiaoban
    - action_trip_hotel_recommend
    - action_trip_flight_recommend
    - action_restart
* thanks
    - utter_noworries

## stop but continue path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
* stop
    - utter_ask_continue
* affirm
    - trip_form
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_trip_jiaoban
    - action_trip_hotel_recommend
    - action_trip_flight_recommend
    - action_restart
* thanks
    - utter_noworries

## stop and really stop path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
* stop
    - utter_ask_continue
* deny
    - utter_answer_abandon
    - action_deactivate_form
    - form{"name": null}
    - action_restart
