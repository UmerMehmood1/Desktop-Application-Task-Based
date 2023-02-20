import pymysql as sql
class DB_Data:
        def __init__(self, email, password):
                self.email = email
                self.password = password
                self.getdatafrom()
        def getdatafrom(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_Email = %s and writer_Password = %s",(self.email,self.password))
                record = cur.fetchone()
                self.writer_id = record[0]
                self.writer_fullname = record[1]+" "+record[2]
                self.writer_evaluation_points = record[3]
                self.writer_daily_word_count = record[4]
                self.writer_monthly_word_count = record[5]
                self.writer_total_leaves = record[6]
                self.writer_leaves_deduction_type = record[7]
                self.writer_email = record[8]
                self.writer_phone = record[9]
                self.writer_gender = record[10]
                self.writer_description = record[11]
                self.writer_jobe_role = record[12]
                self.writer_image = record[13]
                self.writer_team_leader = record[14]
                self.writer_password = record[15]
                self.writer_team_name = record[18]
                self.writer_total_assignments = record[20]
                self.writer_new_members = record[21]
                self.write_file(r".\Images\writer_image.png",self.writer_image)
                con.commit()
                con.close()
        def write_file(self, directory, image):
                self.directory = directory
                self.image = image
                with open(directory, 'wb') as file:
                        file.write(image)