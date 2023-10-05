class Procedure:

    def __init__(self, proced_name, proced_date, practit_name, proced_charges, pat_id):
        self.__proced_name = proced_name
        self.__proced_date = proced_date
        self.__practit_name = practit_name
        self.__proced_charges = proced_charges
        self.__pat_id = pat_id

    def get_proced_name(self):
        return self.__proced_name
    
    def get_proced_date(self):
        return self.__proced_date
    
    def get_practit_name(self):
        return self.__practit_name
    
    def get_proced_charges(self):
        return self.__proced_charges
    
    def get_pat_id(self):
        return self.__pat_id