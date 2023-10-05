import PatientClass as pat
import ProcedureClass as proc

def main():

    pat_id = int(input('Patient ID?: '))
    pat_name = input('Patient name?: ')
    pat_address = input('Patient address?: ')
    pat_phone = input("Patient phone?: ")
    pat_vet_status = input("Patient veteran staus? (type 'TRUE' or 'FALSE'): ").upper()

    patient = pat.Patient(pat_id, pat_name, pat_address, pat_phone, pat_vet_status)

    physical_exam = proc.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1)
    mri = proc.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
    ct_scan = proc.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)

    
    #Patient Report
    print('\n*** Patient Bill ***')
    print(f'Name: {patient.get_pat_name()}')
    print(f'Address: {patient.get_pat_address()}')
    print(f'Phone: {patient.get_pat_phone()}\n')

    total_charges = 0

    for procedure in [physical_exam, mri, ct_scan]:
        if procedure.get_pat_id() == patient.get_pat_id():
            print(f'Procedure: {procedure.get_proced_name()}')
            print(f'Date: {procedure.get_proced_date()}')
            print(f'Practitioner: {procedure.get_practit_name()}')
            print(f'Charge: ${procedure.get_proced_charges():,.2f}\n')
            total_charges += procedure.get_proced_charges()

    if patient.get_pat_vet_status() == 'TRUE':
        total_charges *= 0.6

    print(f'Total Charges: ${total_charges:,.2f}')

main()