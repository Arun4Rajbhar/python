class IRCTC:
    def __init__(self):
        user_input=input("""
        here are the options choose accordingly

        *. Enter 1 to  check train live status
        *. Enter 2 to  check train PNR status
        *. Enter 3 to  check train schedule
        """)

        if user_input=='1':
            print('live train status')

        elif user_input=='2':
            print('pnr status')

        else:
            self.train_schedule()
            
                
