## happy path
* meeting_book
    - meeting_form
    - form{"name": "meeting_form"}
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_meeting_jiaoban
    - action_restart
    
## happy path
* greet
    - utter_answer_greet
* meeting_book
    - meeting_form
    - form{"name": "meeting_form"}
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_meeting_jiaoban
    - action_restart
* thanks
    - utter_noworries

## stop but continue path
* greet
    - utter_answer_greet
* meeting_book
    - meeting_form
    - form{"name": "meeting_form"}
* stop
    - utter_ask_continue
* affirm
    - meeting_form
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_meeting_jiaoban
    - action_restart
* thanks
    - utter_noworries

## stop and really stop path
* greet
    - utter_answer_greet
* meeting_book
    - meeting_form
    - form{"name": "meeting_form"}
* stop
    - utter_ask_continue
* deny
    - utter_answer_abandon
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## unhappy path
* meeting_book
    - meeting_form
    - form{"name": "meeting_form"}
* request_trip
    - utter_answer_other_intent
    - meeting_form
    - form{"name": null}
    - affirm_form
    - form{"name": "affirm_form"}
    - form{"name": null}
    - action_meeting_jiaoban
    - action_restart
