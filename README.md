# Clinical Automation

## Model

* Patient

    * Patient
        * name
        * family
        * national_code
        * birthday
        * gender

    [Patient] example

    | name | family | national_code |
    |:-----:|:-----:|:-----:|
    | Mahdi | Imani | 1451 |

    * Contact
        * patient_id
        * key
        * value

    [Contact] god example

    | patient_id | key | value |
    |:-----:|:-----:|:-----:|
    | 1 | address | tehran, ekbatan |
    | 2 | address | karaj, golshahr |
    | 2 | address | tehran, gisha |
    | 2 | address | tehran, satarkhan |
    | 1 | postal_code | 12541 |
    | 1 | postal_code | 13265464 |

    [Contact] bas example

    | patient_id | address1 | address2 | address3 |
    |:-----:|:-----:|:-----:|:-----:|:-----:|
    | 1 | tehran, ekbatan | * | * |
    | 1 | tehran, ekbatan |  karaj, golshahr | tehran, satarkhan |

    * Refrence
        * patient_id
        * name
        * phone

    * Record
        * patient_id
        * key
        * value
        * time
        * start_date
        * end_date

[Record] example

| patient_id | key | value |
|:-----:|:-----:|:-----:|
| 1 | last operation | nadarad |

* Clinical

    * Clinical_record
        * patient_id
        * description
        * physician_id
        * type (telorder, visit, tele-medecine)
        * date

    * medecine_order
        * Clinical_record_id
        * medecine_id
        * patient_id
        * dose
        * qty
        * description

    * treatment_order
        * Clinical_record_id
        * patient_id
        * key
        * value
        * description

* ParaClininical

    * Operation_record
        * title
        * date
        * patient_id
        * physician_id

    * service_list
        * Operation_record_id
        * service_id
        * qty
        * descripton

    * medecine_order
        * Operation_record_id
        * medecine_id
        * dose
        * qty
        * description

    * treatment_order
        * Operation_record_id
        * key
        * value
        * description

    * consumable_order
        * Operation_record_id
        * consumable_id
        * description
        * qty

    * device_order
        * Operation_record_id
        * title
        * description
        * qty

    * hoteling
        * Operation_record_id
        * title (1-2, 2-4)
        * description
        * qty

* Physician

    * physician
        * name
        * degree

* Accounting

    * Invoice
        * Operation_record_id
        * ... 

* Services
    * Services    
        * type (laser, disk, RF, epidoroscopy, endoscopy)
