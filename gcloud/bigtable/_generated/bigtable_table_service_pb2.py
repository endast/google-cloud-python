# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/admin/table/v1/bigtable_table_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from gcloud.bigtable._generated import bigtable_table_data_pb2 as google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2
from gcloud.bigtable._generated import bigtable_table_service_messages_pb2 as google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/admin/table/v1/bigtable_table_service.proto',
  package='google.bigtable.admin.table.v1',
  syntax='proto3',
  serialized_pb=b'\n;google/bigtable/admin/table/v1/bigtable_table_service.proto\x12\x1egoogle.bigtable.admin.table.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x38google/bigtable/admin/table/v1/bigtable_table_data.proto\x1a\x44google/bigtable/admin/table/v1/bigtable_table_service_messages.proto\x1a\x1bgoogle/protobuf/empty.proto2\x89\x0b\n\x14\x42igtableTableService\x12\xa4\x01\n\x0b\x43reateTable\x12\x32.google.bigtable.admin.table.v1.CreateTableRequest\x1a%.google.bigtable.admin.table.v1.Table\":\x82\xd3\xe4\x93\x02\x34\"//v1/{name=projects/*/zones/*/clusters/*}/tables:\x01*\x12\xac\x01\n\nListTables\x12\x31.google.bigtable.admin.table.v1.ListTablesRequest\x1a\x32.google.bigtable.admin.table.v1.ListTablesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//v1/{name=projects/*/zones/*/clusters/*}/tables\x12\x9d\x01\n\x08GetTable\x12/.google.bigtable.admin.table.v1.GetTableRequest\x1a%.google.bigtable.admin.table.v1.Table\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/{name=projects/*/zones/*/clusters/*/tables/*}\x12\x94\x01\n\x0b\x44\x65leteTable\x12\x32.google.bigtable.admin.table.v1.DeleteTableRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v1/{name=projects/*/zones/*/clusters/*/tables/*}\x12\x9e\x01\n\x0bRenameTable\x12\x32.google.bigtable.admin.table.v1.RenameTableRequest\x1a\x16.google.protobuf.Empty\"C\x82\xd3\xe4\x93\x02=\"8/v1/{name=projects/*/zones/*/clusters/*/tables/*}:rename:\x01*\x12\xca\x01\n\x12\x43reateColumnFamily\x12\x39.google.bigtable.admin.table.v1.CreateColumnFamilyRequest\x1a,.google.bigtable.admin.table.v1.ColumnFamily\"K\x82\xd3\xe4\x93\x02\x45\"@/v1/{name=projects/*/zones/*/clusters/*/tables/*}/columnFamilies:\x01*\x12\xbf\x01\n\x12UpdateColumnFamily\x12,.google.bigtable.admin.table.v1.ColumnFamily\x1a,.google.bigtable.admin.table.v1.ColumnFamily\"M\x82\xd3\xe4\x93\x02G\x1a\x42/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}:\x01*\x12\xb3\x01\n\x12\x44\x65leteColumnFamily\x12\x39.google.bigtable.admin.table.v1.DeleteColumnFamilyRequest\x1a\x16.google.protobuf.Empty\"J\x82\xd3\xe4\x93\x02\x44*B/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}BB\n\"com.google.bigtable.admin.table.v1B\x1a\x42igtableTableServicesProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2.DESCRIPTOR,google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\"com.google.bigtable.admin.table.v1B\032BigtableTableServicesProtoP\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterBigtableTableServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def CreateTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ListTables(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RenameTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CreateColumnFamily(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def UpdateColumnFamily(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteColumnFamily(self, request, context):
    raise NotImplementedError()
class EarlyAdopterBigtableTableServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterBigtableTableServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def CreateTable(self, request):
    raise NotImplementedError()
  CreateTable.async = None
  @abc.abstractmethod
  def ListTables(self, request):
    raise NotImplementedError()
  ListTables.async = None
  @abc.abstractmethod
  def GetTable(self, request):
    raise NotImplementedError()
  GetTable.async = None
  @abc.abstractmethod
  def DeleteTable(self, request):
    raise NotImplementedError()
  DeleteTable.async = None
  @abc.abstractmethod
  def RenameTable(self, request):
    raise NotImplementedError()
  RenameTable.async = None
  @abc.abstractmethod
  def CreateColumnFamily(self, request):
    raise NotImplementedError()
  CreateColumnFamily.async = None
  @abc.abstractmethod
  def UpdateColumnFamily(self, request):
    raise NotImplementedError()
  UpdateColumnFamily.async = None
  @abc.abstractmethod
  def DeleteColumnFamily(self, request):
    raise NotImplementedError()
  DeleteColumnFamily.async = None
def early_adopter_create_BigtableTableService_server(servicer, port, private_key=None, certificate_chain=None):
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  method_service_descriptions = {
    "CreateColumnFamily": alpha_utilities.unary_unary_service_description(
      servicer.CreateColumnFamily,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateColumnFamilyRequest.FromString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
    ),
    "CreateTable": alpha_utilities.unary_unary_service_description(
      servicer.CreateTable,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateTableRequest.FromString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.Table.SerializeToString,
    ),
    "DeleteColumnFamily": alpha_utilities.unary_unary_service_description(
      servicer.DeleteColumnFamily,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteColumnFamilyRequest.FromString,
      google.protobuf.empty_pb2.Empty.SerializeToString,
    ),
    "DeleteTable": alpha_utilities.unary_unary_service_description(
      servicer.DeleteTable,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteTableRequest.FromString,
      google.protobuf.empty_pb2.Empty.SerializeToString,
    ),
    "GetTable": alpha_utilities.unary_unary_service_description(
      servicer.GetTable,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.GetTableRequest.FromString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.Table.SerializeToString,
    ),
    "ListTables": alpha_utilities.unary_unary_service_description(
      servicer.ListTables,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesRequest.FromString,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesResponse.SerializeToString,
    ),
    "RenameTable": alpha_utilities.unary_unary_service_description(
      servicer.RenameTable,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.RenameTableRequest.FromString,
      google.protobuf.empty_pb2.Empty.SerializeToString,
    ),
    "UpdateColumnFamily": alpha_utilities.unary_unary_service_description(
      servicer.UpdateColumnFamily,
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("google.bigtable.admin.table.v1.BigtableTableService", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_BigtableTableService_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  method_invocation_descriptions = {
    "CreateColumnFamily": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateColumnFamilyRequest.SerializeToString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
    ),
    "CreateTable": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateTableRequest.SerializeToString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.Table.FromString,
    ),
    "DeleteColumnFamily": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteColumnFamilyRequest.SerializeToString,
      google.protobuf.empty_pb2.Empty.FromString,
    ),
    "DeleteTable": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteTableRequest.SerializeToString,
      google.protobuf.empty_pb2.Empty.FromString,
    ),
    "GetTable": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.GetTableRequest.SerializeToString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.Table.FromString,
    ),
    "ListTables": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesRequest.SerializeToString,
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesResponse.FromString,
    ),
    "RenameTable": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_service_messages_pb2.RenameTableRequest.SerializeToString,
      google.protobuf.empty_pb2.Empty.FromString,
    ),
    "UpdateColumnFamily": alpha_utilities.unary_unary_invocation_description(
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
      gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
    ),
  }
  return early_adopter_implementations.stub("google.bigtable.admin.table.v1.BigtableTableService", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaBigtableTableServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def CreateTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ListTables(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RenameTable(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CreateColumnFamily(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def UpdateColumnFamily(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteColumnFamily(self, request, context):
    raise NotImplementedError()

class BetaBigtableTableServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def CreateTable(self, request, timeout):
    raise NotImplementedError()
  CreateTable.future = None
  @abc.abstractmethod
  def ListTables(self, request, timeout):
    raise NotImplementedError()
  ListTables.future = None
  @abc.abstractmethod
  def GetTable(self, request, timeout):
    raise NotImplementedError()
  GetTable.future = None
  @abc.abstractmethod
  def DeleteTable(self, request, timeout):
    raise NotImplementedError()
  DeleteTable.future = None
  @abc.abstractmethod
  def RenameTable(self, request, timeout):
    raise NotImplementedError()
  RenameTable.future = None
  @abc.abstractmethod
  def CreateColumnFamily(self, request, timeout):
    raise NotImplementedError()
  CreateColumnFamily.future = None
  @abc.abstractmethod
  def UpdateColumnFamily(self, request, timeout):
    raise NotImplementedError()
  UpdateColumnFamily.future = None
  @abc.abstractmethod
  def DeleteColumnFamily(self, request, timeout):
    raise NotImplementedError()
  DeleteColumnFamily.future = None

def beta_create_BigtableTableService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  request_deserializers = {
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateColumnFamily'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateColumnFamilyRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateTableRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteColumnFamily'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteColumnFamilyRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteTableRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'GetTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.GetTableRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'ListTables'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'RenameTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.RenameTableRequest.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'UpdateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
  }
  response_serializers = {
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateTable'): gcloud.bigtable._generated.bigtable_table_data_pb2.Table.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteColumnFamily'): google.protobuf.empty_pb2.Empty.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteTable'): google.protobuf.empty_pb2.Empty.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'GetTable'): gcloud.bigtable._generated.bigtable_table_data_pb2.Table.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'ListTables'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesResponse.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'RenameTable'): google.protobuf.empty_pb2.Empty.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'UpdateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
  }
  method_implementations = {
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateColumnFamily'): face_utilities.unary_unary_inline(servicer.CreateColumnFamily),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateTable'): face_utilities.unary_unary_inline(servicer.CreateTable),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteColumnFamily'): face_utilities.unary_unary_inline(servicer.DeleteColumnFamily),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteTable'): face_utilities.unary_unary_inline(servicer.DeleteTable),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'GetTable'): face_utilities.unary_unary_inline(servicer.GetTable),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'ListTables'): face_utilities.unary_unary_inline(servicer.ListTables),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'RenameTable'): face_utilities.unary_unary_inline(servicer.RenameTable),
    ('google.bigtable.admin.table.v1.BigtableTableService', 'UpdateColumnFamily'): face_utilities.unary_unary_inline(servicer.UpdateColumnFamily),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BigtableTableService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_data_pb2
  import gcloud.bigtable._generated.bigtable_table_service_messages_pb2
  import google.protobuf.empty_pb2
  request_serializers = {
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateColumnFamily'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateColumnFamilyRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.CreateTableRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteColumnFamily'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteColumnFamilyRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.DeleteTableRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'GetTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.GetTableRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'ListTables'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'RenameTable'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.RenameTableRequest.SerializeToString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'UpdateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.SerializeToString,
  }
  response_deserializers = {
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'CreateTable'): gcloud.bigtable._generated.bigtable_table_data_pb2.Table.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteColumnFamily'): google.protobuf.empty_pb2.Empty.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'DeleteTable'): google.protobuf.empty_pb2.Empty.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'GetTable'): gcloud.bigtable._generated.bigtable_table_data_pb2.Table.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'ListTables'): gcloud.bigtable._generated.bigtable_table_service_messages_pb2.ListTablesResponse.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'RenameTable'): google.protobuf.empty_pb2.Empty.FromString,
    ('google.bigtable.admin.table.v1.BigtableTableService', 'UpdateColumnFamily'): gcloud.bigtable._generated.bigtable_table_data_pb2.ColumnFamily.FromString,
  }
  cardinalities = {
    'CreateColumnFamily': cardinality.Cardinality.UNARY_UNARY,
    'CreateTable': cardinality.Cardinality.UNARY_UNARY,
    'DeleteColumnFamily': cardinality.Cardinality.UNARY_UNARY,
    'DeleteTable': cardinality.Cardinality.UNARY_UNARY,
    'GetTable': cardinality.Cardinality.UNARY_UNARY,
    'ListTables': cardinality.Cardinality.UNARY_UNARY,
    'RenameTable': cardinality.Cardinality.UNARY_UNARY,
    'UpdateColumnFamily': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'google.bigtable.admin.table.v1.BigtableTableService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
