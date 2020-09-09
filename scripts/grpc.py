import glob
import re
from distutils.cmd import Command

class GrpcCommand(Command):
    description = 'Generate gRPC classes from Protobuf definitions'

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from grpc_tools import protoc

        protoc.main([
            'grpc_tools.protoc',
            '--proto_path=api/proto',
            '--python_out=api/grpc',
            '--grpc_python_out=api/grpc'
        ] + [proto for proto in glob.iglob('./api/proto/*.proto')])

        # https://github.com/protocolbuffers/protobuf/issues/1491
        for script in glob.iglob('./api/grpc/*.py'):
            with open(script, 'r+') as file:
                code = file.read()
                file.seek(0)
                file.write(re.sub(r'(import .+_pb2.*)', 'from . \\1', code))
                file.truncate()
