from dateutil.tz import UTC
import importlib
import pkgutil


def write_datetime_to_message(message, dt):
    # value is a datetime
    datetime_utc = dt.astimezone(UTC)
    datetime_naive = datetime_utc.replace(tzinfo=None)
    message.FromDatetime(datetime_naive)


def create_message_proto_map(protobuf_modules=None, package_paths=None):
    """
    Create a dictionary of proto message name to the message class
    """
    assert protobuf_modules or package_paths

    protobuf_modules = protobuf_modules or get_protobuf_modules(package_paths)

    message_proto_map = {}
    for module in protobuf_modules:
        for message_name in module.DESCRIPTOR.message_types_by_name:
            message_proto = getattr(module, message_name)
            message_full_name = message_proto.DESCRIPTOR.full_name
            # remove the google testing messages
            if 'unittest' in message_full_name:   # pragma: no cover
                continue
            message_proto_map[message_full_name] = getattr(module, message_name)
    return message_proto_map


def get_protobuf_modules(package_paths):
    """
    - package_paths: list of importable paths to protobuf packages

    Example:
    package_paths = [
        'val_client.api.grpc.protobuf',
        'google.protobuf',
    ]
    """

    modules = []

    for package_path in package_paths:
        package = importlib.import_module(package_path)
        modnames = []
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            if modname.endswith('pb2'):
                modnames.append(modname)
        for modname in modnames:
            mod_path = f'{package_path}.{modname}'
            module = importlib.import_module(mod_path)
            modules.append(module)

    return modules
