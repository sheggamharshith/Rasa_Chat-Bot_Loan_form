## bot challenge
* bot_challenge
  - utter_iamabot

## loan+form1+proceed+form2+success
* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
	- utter_accept_go
    - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null}    
    - utter_loan_from_accepted_proced_next
* proceed
	- loan_form2           
    - form{"name":"loan_form2"}
    - form{"name": null} 
    - utter_submit_success

## loan+convence+form2+success
* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* deny
	- utter_convence
    - utter_greet_ask_loan_premission
* affirm
	- utter_accept_go
     - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null}    
    - utter_loan_from_accepted_proced_next
* proceed
	- loan_form2           
    - form{"name":"loan_form2"}
    - form{"name": null} 
    - utter_submit_success
* thanks
    - utter_thanks

## loan+form1+submitform+accepted
* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
	- utter_accept_go
     - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null}    
    - utter_loan_from_accepted_proced_next
* submitform
	- utter_submit_deny

## end story

* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* deny
    - utter_convence
    - utter_greet_ask_loan_premission
* deny
    - utter_canthelp

## loan+form1+deny+accepted
* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
	- utter_accept_go
     - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null}    
    - utter_loan_from_accepted_proced_next
* deny
	- utter_submit_deny

## loan+form1+affirm+form2+suceese
* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
	- utter_accept_go
    - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null}    
    - utter_loan_from_accepted_proced_next
* affirm
	- loan_form2           
    - form{"name":"loan_form2"}
    - form{"name": null} 
    - utter_submit_success

## loan+form1+deny_in_middle+submitform1

* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
    - utter_accept_go
    - loan_form
    - form{"name":"loan_form"}
    - slot{"requested_slot":"person_name"}
* deny
    - utter_canthelp
* proceed
    - action_hello_world
    - utter_greet_ask_loan_premission
* affirm
    - utter_accept_go
   	- loan_form
    - form{"name":"loan_form"}
* submitform
    - utter_submit_deny

## loan+form1+deny_in_middle+form2+accepted

* greet
    - utter_greet
    - utter_greet_2
    - utter_greet_ask_loan_premission
* affirm
    - utter_accept_go
    - loan_form
    - form{"name":"loan_form"}
    - slot{"requested_slot":"person_name"}
* deny
    - utter_canthelp
* proceed
    - action_hello_world
    - utter_greet_ask_loan_premission
* affirm
    - utter_accept_go
   	- loan_form
    - form{"name":"loan_form"}
* proceed
	- loan_form2           
    - form{"name":"loan_form2"}
    - form{"name": null} 
    - utter_submit_success



## unknow
* unknow
- utter_default


## chatrestart
* slotreset
- action_hello_world
- action_chat_restart



## loan explain and continue
* loan
    - loan_form
    - form{"name":"loan_form"}
    - slot{"requested_slot":"person_name"}
* explain
    - utter_explain_why_name
    - loan_form           
    - form{"name":"loan_form"}
    - slot{"requested_slot":"email_id"}
* explain
    - utter_explain_why_email_id
    - loan_form           
    - form{"name":"loan_form"}
    - slot{"requested_slot":"phone_number"}
* explain
    - utter_explain_why_phone_number
    - loan_form           
    - form{"name":"loan_form"}
    - form{"name": null} 
    - utter_loan_from_accepted_proced_next
* affirm
    - loan_form2           
    - form{"name":"loan_form2"}
    - form{"name": null} 
    - utter_submit_success


## just sales, continue
* loan
    - loan_form
    - form{"name": "loan_form"}
* faq
    - respond_faq
    - loan_form
    - form{"name": null}

## Some question from FAQ
* faq
    - respond_faq

## thankyou
* thankyou
    - utter_thanks


## bye
* bye
    - utter_bye