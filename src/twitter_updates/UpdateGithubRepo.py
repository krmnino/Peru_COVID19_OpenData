import datetime
import sys

from TwitterUpdate import check_date
from TwitterUpdate import update_git_repo_win32
from TwitterUpdate import update_git_repo_linux

def update_git(opt_date=datetime.date.today().strftime('%Y-%m-%d')):
    check_date(opt_date)
    if(sys.platform == 'win32'):
        update_git_repo_win32(opt_date)
    else:
        update_git_repo_linux(opt_date)

if(len(sys.argv)):
    update_git()
else:
    update_git(opt_date=sys.argv[0])