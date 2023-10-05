class Patient:

    def __init__(self, pat_id, pat_name, pat_address, pat_phone, pat_vet_status):
        self.__pat_id = pat_id
        self.__pat_name = pat_name
        self.__pat_address = pat_address
        self.__pat_phone = pat_phone
        self.__pat_vet_status = pat_vet_status

    def get_pat_id(self):
        return self.__pat_id
    
    def get_pat_name(self):
        return self.__pat_name
    
    def get_pat_address(self):
        return self.__pat_address
    
    def get_pat_phone(self):
        return self.__pat_phone
    
    def get_pat_vet_status(self):
        return self.__pat_vet_status