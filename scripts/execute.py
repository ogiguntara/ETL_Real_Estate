import extract
import transform
import load
from common.base import Base,engine

if __name__=="__main__":
    extract.main()
    Base.metadata.create_all(engine)
    transform.main()
    load.main()