from voximplant.apiclient import VoximplantAPI, VoximplantException

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    # Create SIP registration.

    SIP_USERNAME = "test"
    PROXY = "localhost"
    
    try:
        res = voxapi.create_sip_registration(SIP_USERNAME, PROXY)
    except VoximplantException as e:
        print("Error: {}".format(e.message))
    print(res)
