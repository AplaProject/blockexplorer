""" Clear blocks @ auxliliary DB """

from ...app import create_lean_app as create_app
from ...models.genesis.aux.block.filler import BlockFiller
from ...models.genesis.aux.session import AuxSessionManager

from .base import Base

class AuxBlocksClear(Base):
    def run(self):
        seq_num = self.options.get("<seq-num>")
        app = create_app(config_path=self.config_path)
        app.app_context().push()
        sm = AuxSessionManager(app=app)
        session = sm.get_session(seq_num)
        bf = BlockFiller(app=app, seq_num=seq_num)
        bf.clear()
