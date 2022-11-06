import sys, os
import shutil
import pydicom
import filetype

def main():

    print("Renaming Dicom files... in directory")

    current_folder = "."

    if len(sys.argv) > 1:
        current_folder = sys.argv[1]

    working_dir = os.path.abspath(current_folder)

    print(working_dir)

    for foldername, subfolders, filenames in os.walk(working_dir):

        for filename in filenames:

            print("Processing", filename)

            ds_filename = os.path.join(working_dir, filename)

            kind = filetype.guess_mime(ds_filename)

            if kind == 'application/dicom':

                ds = pydicom.dcmread(ds_filename)

                patient_id = str(ds.PatientID)
                patient_id = patient_id.replace("/", " ")

                patient_name = str(ds.PatientName)
                patient_name = patient_name.replace("/", " ")

                srs_time = str(ds.SeriesTime)

                patient_filename = patient_id + " " + patient_name + " " + srs_time + ".dcm"
                new_filename = os.path.join(working_dir, patient_filename)

                print(f'==> Renaming "{ds_filename}" to "{new_filename}"...')
                shutil.move(ds_filename, new_filename)

            else:
                print ("==> Not a Dicom file")

        break

    print("Finished!")

if __name__ == '__main__':
    main()
