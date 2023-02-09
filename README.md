## How to install this script on Windows

1. Install python, make sure the python command is available in your PATH
2. Install the required python library:

```
pip install pydicom
pip install filetype
```

3. Put both file dcm-rename.bat and dcm-rename.py script in your PATH
 (I put them in my user folder C:\Users\Lenovo, which is already in my PATH)
4. Check the content of dcm-rename.bat, make sure the path to dcm-rename.py is correct.
4. Go to the folder that you want to batch process. This folder should contain dicom files that you want to be renamed
5. Open Terminal app in the folder
6. Input the command
  
  ```
  dcm-rename "path/to/folder"
  ```

  OR, if inside the target folder:
  
  ``` 
  dcm-rename .
  ```
