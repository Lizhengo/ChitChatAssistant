## happy path
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* affirm
    - action_trip_jiaoban

## happy path
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* deny
    - action_deactivate_form
    
## happy path
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* deny
    - action_deactivate_form
    
## happy path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* affirm
    - action_trip_jiaoban
* thanks
    - utter_noworries
    
## happy path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* deny
    - action_deactivate_form
* thanks
    - utter_noworries
    
## happy path
* greet
    - utter_answer_greet
* request_trip
    - trip_form
    - form{"name": "trip_form"}
    - form{"name": null}
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* deny
    - action_deactivate_form
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
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* affirm
    - action_trip_jiaoban
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
* deny
    - action_deactivate_form
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
* affirm
    - jiaoban_form
    - form{"name": "jiaoban_form"}
    - form{"name": null}
* deny
    - action_deactivate_form
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
    - action_deactivate_form
    - form{"name": null}
