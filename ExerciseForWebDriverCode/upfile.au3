;必须打开AutoItWindow Info
ControlFocus("文件上传","","Edit1")
WinWait("[CLASS:#32770]", "" ,10)
ControlSetText("文件上传", "", "Edit1","D:\code\python\FormalSpecificationAndSTest\C4.12_C4.20\upload_file.txt" )
Sleep(2000)
ControlClick("文件上传", "","Button1" )