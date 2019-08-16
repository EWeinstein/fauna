from update import update
from dengue_upload import dengue_upload
from update import parser

class dengue_update(update, dengue_upload):
    def __init__(self, **kwargs):
        update.__init__(self, **kwargs)
        dengue_upload.__init__(self, **kwargs)

if __name__=="__main__":
    args = parser.parse_args()
    connVDB = dengue_update(**args.__dict__)
    connVDB.update(**args.__dict__)
