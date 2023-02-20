from WriterMain import WriterUI
from TDLMain import TDL_UI
from Login import LoginUI
from Reg import RegisterationUI
from Data_Extractor import DB_Data
from PyQt5 import QtWidgets
import sys
# For Writer UI Testing "Umer's Account"
if __name__ == "__main__":
    GetData = DB_Data("umer.fiesta2762", "1")
    app = QtWidgets.QApplication(sys.argv)
    ui = WriterUI(
                str(GetData.writer_id),
                False,
                str(GetData.writer_evaluation_points),
                str(GetData.writer_fullname),
                str(GetData.writer_daily_word_count),
                str(GetData.writer_monthly_word_count),
                r"./Images/writer_image.png",
                str(GetData.writer_email),
                str(GetData.writer_phone),
                str(GetData.writer_gender),
                "20",
                str(GetData.writer_description),
                str(GetData.writer_jobe_role),
                str(GetData.writer_team_name),
                str(GetData.writer_team_leader))
    sys.exit(app.exec_())
# For TDL UI Testing "Abe's Account"
if __name__ == "__main__":
    GetData = DB_Data("abe.fiesta", "1")
    ui = TDL_UI(
        False,
        str(GetData.writer_team_name),
        "5",
        '15',
        str(GetData.writer_evaluation_points),
        str(GetData.writer_fullname),
        f"F:\\Visual Code Stuff\\Design_For_FCS_Portal\\Images\\writer_image.png",
        str(GetData.writer_email),
        str(GetData.writer_phone),
        str(GetData.writer_gender),
        '24',
        str(GetData.writer_description),
        str(GetData.writer_jobe_role),
        str(GetData.writer_team_leader)
        )
# For Login UI Testing "Null Account"
if __name__ == "__main__":
        ui = LoginUI()
# For Registeration UI Testing "Any Account"
if __name__ == "__main__":
    ui = RegisterationUI()