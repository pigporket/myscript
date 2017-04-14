import os
import traceback
from datetime import datetime

home_path = os.path.expanduser("~") + "/"
mysqldump_output_file_name = home_path + "mysql_backup/"


def mysqldump(host, user, password, database_name, port=3306, skipdata=False):
    try:
        skipdata_string = ''
        if skipdata:
            skipdata_string = '-d'
        output_file = mysqldump_output_file_name + database_name + str(datetime.now().strftime("%Y-%m-%d")) + '.sql'
        mysqldump_string = "mysqldump --lock-tables=false -C -P{0}  -h{1} -u{2} -p{3} {4} {5} > {6}".format(port,
                                                                                                              host,
                                                                                                              user,
                                                                                                              password,
                                                                                                              skipdata_string,
                                                                                                              database_name,
                                                                                                              output_file
                                                                                                              )
        os.system(mysqldump_string)
    except:
        traceback.print_exc()


def backup_data():
    shell_str = 'find /root/mysql_backup -name "*.zip" -mtime -700 | xargs -I {} scp {} /data/mysql_backup/'
    os.system(shell_str)


def run():
    backup_data()
    mysqldump("192.168.100.162", "root", "123qwe", "oldboydb")

if __name__ == '__main__':
	run()
