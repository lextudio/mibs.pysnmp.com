# SNMP MIB module (TUBS-NFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-NFS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:00 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

nfsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NfsServer_ObjectIdentity = ObjectIdentity
nfsServer = _NfsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1)
)
_NfsServerCalls_Type = Counter32
_NfsServerCalls_Object = MibScalar
nfsServerCalls = _NfsServerCalls_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 1),
    _NfsServerCalls_Type()
)
nfsServerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerCalls.setStatus("current")
_NfsServerBad_Type = Counter32
_NfsServerBad_Object = MibScalar
nfsServerBad = _NfsServerBad_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 2),
    _NfsServerBad_Type()
)
nfsServerBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerBad.setStatus("current")
_NfsServerNull_Type = Counter32
_NfsServerNull_Object = MibScalar
nfsServerNull = _NfsServerNull_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 3),
    _NfsServerNull_Type()
)
nfsServerNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerNull.setStatus("current")
_NfsServerGetattr_Type = Counter32
_NfsServerGetattr_Object = MibScalar
nfsServerGetattr = _NfsServerGetattr_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 4),
    _NfsServerGetattr_Type()
)
nfsServerGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerGetattr.setStatus("current")
_NfsServerSetattr_Type = Counter32
_NfsServerSetattr_Object = MibScalar
nfsServerSetattr = _NfsServerSetattr_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 5),
    _NfsServerSetattr_Type()
)
nfsServerSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerSetattr.setStatus("current")
_NfsServerRoot_Type = Counter32
_NfsServerRoot_Object = MibScalar
nfsServerRoot = _NfsServerRoot_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 6),
    _NfsServerRoot_Type()
)
nfsServerRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerRoot.setStatus("current")
_NfsServerLookup_Type = Counter32
_NfsServerLookup_Object = MibScalar
nfsServerLookup = _NfsServerLookup_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 7),
    _NfsServerLookup_Type()
)
nfsServerLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerLookup.setStatus("current")
_NfsServerReadlink_Type = Counter32
_NfsServerReadlink_Object = MibScalar
nfsServerReadlink = _NfsServerReadlink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 8),
    _NfsServerReadlink_Type()
)
nfsServerReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerReadlink.setStatus("current")
_NfsServerRead_Type = Counter32
_NfsServerRead_Object = MibScalar
nfsServerRead = _NfsServerRead_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 9),
    _NfsServerRead_Type()
)
nfsServerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerRead.setStatus("current")
_NfsServerWrcache_Type = Counter32
_NfsServerWrcache_Object = MibScalar
nfsServerWrcache = _NfsServerWrcache_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 10),
    _NfsServerWrcache_Type()
)
nfsServerWrcache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerWrcache.setStatus("current")
_NfsServerWrite_Type = Counter32
_NfsServerWrite_Object = MibScalar
nfsServerWrite = _NfsServerWrite_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 11),
    _NfsServerWrite_Type()
)
nfsServerWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerWrite.setStatus("current")
_NfsServerCreate_Type = Counter32
_NfsServerCreate_Object = MibScalar
nfsServerCreate = _NfsServerCreate_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 12),
    _NfsServerCreate_Type()
)
nfsServerCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerCreate.setStatus("current")
_NfsServerRemove_Type = Counter32
_NfsServerRemove_Object = MibScalar
nfsServerRemove = _NfsServerRemove_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 13),
    _NfsServerRemove_Type()
)
nfsServerRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerRemove.setStatus("current")
_NfsServerRename_Type = Counter32
_NfsServerRename_Object = MibScalar
nfsServerRename = _NfsServerRename_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 14),
    _NfsServerRename_Type()
)
nfsServerRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerRename.setStatus("current")
_NfsServerLink_Type = Counter32
_NfsServerLink_Object = MibScalar
nfsServerLink = _NfsServerLink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 15),
    _NfsServerLink_Type()
)
nfsServerLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerLink.setStatus("current")
_NfsServerSymlink_Type = Counter32
_NfsServerSymlink_Object = MibScalar
nfsServerSymlink = _NfsServerSymlink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 16),
    _NfsServerSymlink_Type()
)
nfsServerSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerSymlink.setStatus("current")
_NfsServerMkdir_Type = Counter32
_NfsServerMkdir_Object = MibScalar
nfsServerMkdir = _NfsServerMkdir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 17),
    _NfsServerMkdir_Type()
)
nfsServerMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerMkdir.setStatus("current")
_NfsServerRmdir_Type = Counter32
_NfsServerRmdir_Object = MibScalar
nfsServerRmdir = _NfsServerRmdir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 18),
    _NfsServerRmdir_Type()
)
nfsServerRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerRmdir.setStatus("current")
_NfsServerReaddir_Type = Counter32
_NfsServerReaddir_Object = MibScalar
nfsServerReaddir = _NfsServerReaddir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 19),
    _NfsServerReaddir_Type()
)
nfsServerReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerReaddir.setStatus("current")
_NfsServerFsstat_Type = Counter32
_NfsServerFsstat_Object = MibScalar
nfsServerFsstat = _NfsServerFsstat_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 1, 20),
    _NfsServerFsstat_Type()
)
nfsServerFsstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServerFsstat.setStatus("current")
_NfsClient_ObjectIdentity = ObjectIdentity
nfsClient = _NfsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2)
)
_NfsClientCalls_Type = Counter32
_NfsClientCalls_Object = MibScalar
nfsClientCalls = _NfsClientCalls_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 1),
    _NfsClientCalls_Type()
)
nfsClientCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientCalls.setStatus("current")
_NfsClientBad_Type = Counter32
_NfsClientBad_Object = MibScalar
nfsClientBad = _NfsClientBad_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 2),
    _NfsClientBad_Type()
)
nfsClientBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientBad.setStatus("current")
_NfsClientNull_Type = Counter32
_NfsClientNull_Object = MibScalar
nfsClientNull = _NfsClientNull_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 3),
    _NfsClientNull_Type()
)
nfsClientNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientNull.setStatus("current")
_NfsClientGetattr_Type = Counter32
_NfsClientGetattr_Object = MibScalar
nfsClientGetattr = _NfsClientGetattr_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 4),
    _NfsClientGetattr_Type()
)
nfsClientGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientGetattr.setStatus("current")
_NfsClientSetattr_Type = Counter32
_NfsClientSetattr_Object = MibScalar
nfsClientSetattr = _NfsClientSetattr_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 5),
    _NfsClientSetattr_Type()
)
nfsClientSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientSetattr.setStatus("current")
_NfsClientRoot_Type = Counter32
_NfsClientRoot_Object = MibScalar
nfsClientRoot = _NfsClientRoot_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 6),
    _NfsClientRoot_Type()
)
nfsClientRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientRoot.setStatus("current")
_NfsClientLookup_Type = Counter32
_NfsClientLookup_Object = MibScalar
nfsClientLookup = _NfsClientLookup_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 7),
    _NfsClientLookup_Type()
)
nfsClientLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientLookup.setStatus("current")
_NfsClientReadlink_Type = Counter32
_NfsClientReadlink_Object = MibScalar
nfsClientReadlink = _NfsClientReadlink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 8),
    _NfsClientReadlink_Type()
)
nfsClientReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientReadlink.setStatus("current")
_NfsClientRead_Type = Counter32
_NfsClientRead_Object = MibScalar
nfsClientRead = _NfsClientRead_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 9),
    _NfsClientRead_Type()
)
nfsClientRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientRead.setStatus("current")
_NfsClientWrcache_Type = Counter32
_NfsClientWrcache_Object = MibScalar
nfsClientWrcache = _NfsClientWrcache_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 10),
    _NfsClientWrcache_Type()
)
nfsClientWrcache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientWrcache.setStatus("current")
_NfsClientWrite_Type = Counter32
_NfsClientWrite_Object = MibScalar
nfsClientWrite = _NfsClientWrite_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 11),
    _NfsClientWrite_Type()
)
nfsClientWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientWrite.setStatus("current")
_NfsClientCreate_Type = Counter32
_NfsClientCreate_Object = MibScalar
nfsClientCreate = _NfsClientCreate_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 12),
    _NfsClientCreate_Type()
)
nfsClientCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientCreate.setStatus("current")
_NfsClientRemove_Type = Counter32
_NfsClientRemove_Object = MibScalar
nfsClientRemove = _NfsClientRemove_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 13),
    _NfsClientRemove_Type()
)
nfsClientRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientRemove.setStatus("current")
_NfsClientRename_Type = Counter32
_NfsClientRename_Object = MibScalar
nfsClientRename = _NfsClientRename_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 14),
    _NfsClientRename_Type()
)
nfsClientRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientRename.setStatus("current")
_NfsClientLink_Type = Counter32
_NfsClientLink_Object = MibScalar
nfsClientLink = _NfsClientLink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 15),
    _NfsClientLink_Type()
)
nfsClientLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientLink.setStatus("current")
_NfsClientSymlink_Type = Counter32
_NfsClientSymlink_Object = MibScalar
nfsClientSymlink = _NfsClientSymlink_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 16),
    _NfsClientSymlink_Type()
)
nfsClientSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientSymlink.setStatus("current")
_NfsClientMkdir_Type = Counter32
_NfsClientMkdir_Object = MibScalar
nfsClientMkdir = _NfsClientMkdir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 17),
    _NfsClientMkdir_Type()
)
nfsClientMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientMkdir.setStatus("current")
_NfsClientRmdir_Type = Counter32
_NfsClientRmdir_Object = MibScalar
nfsClientRmdir = _NfsClientRmdir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 18),
    _NfsClientRmdir_Type()
)
nfsClientRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientRmdir.setStatus("current")
_NfsClientReaddir_Type = Counter32
_NfsClientReaddir_Object = MibScalar
nfsClientReaddir = _NfsClientReaddir_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 19),
    _NfsClientReaddir_Type()
)
nfsClientReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientReaddir.setStatus("current")
_NfsClientFsstat_Type = Counter32
_NfsClientFsstat_Object = MibScalar
nfsClientFsstat = _NfsClientFsstat_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 2, 2, 20),
    _NfsClientFsstat_Type()
)
nfsClientFsstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientFsstat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-NFS-MIB",
    **{"nfsMIB": nfsMIB,
       "nfsServer": nfsServer,
       "nfsServerCalls": nfsServerCalls,
       "nfsServerBad": nfsServerBad,
       "nfsServerNull": nfsServerNull,
       "nfsServerGetattr": nfsServerGetattr,
       "nfsServerSetattr": nfsServerSetattr,
       "nfsServerRoot": nfsServerRoot,
       "nfsServerLookup": nfsServerLookup,
       "nfsServerReadlink": nfsServerReadlink,
       "nfsServerRead": nfsServerRead,
       "nfsServerWrcache": nfsServerWrcache,
       "nfsServerWrite": nfsServerWrite,
       "nfsServerCreate": nfsServerCreate,
       "nfsServerRemove": nfsServerRemove,
       "nfsServerRename": nfsServerRename,
       "nfsServerLink": nfsServerLink,
       "nfsServerSymlink": nfsServerSymlink,
       "nfsServerMkdir": nfsServerMkdir,
       "nfsServerRmdir": nfsServerRmdir,
       "nfsServerReaddir": nfsServerReaddir,
       "nfsServerFsstat": nfsServerFsstat,
       "nfsClient": nfsClient,
       "nfsClientCalls": nfsClientCalls,
       "nfsClientBad": nfsClientBad,
       "nfsClientNull": nfsClientNull,
       "nfsClientGetattr": nfsClientGetattr,
       "nfsClientSetattr": nfsClientSetattr,
       "nfsClientRoot": nfsClientRoot,
       "nfsClientLookup": nfsClientLookup,
       "nfsClientReadlink": nfsClientReadlink,
       "nfsClientRead": nfsClientRead,
       "nfsClientWrcache": nfsClientWrcache,
       "nfsClientWrite": nfsClientWrite,
       "nfsClientCreate": nfsClientCreate,
       "nfsClientRemove": nfsClientRemove,
       "nfsClientRename": nfsClientRename,
       "nfsClientLink": nfsClientLink,
       "nfsClientSymlink": nfsClientSymlink,
       "nfsClientMkdir": nfsClientMkdir,
       "nfsClientRmdir": nfsClientRmdir,
       "nfsClientReaddir": nfsClientReaddir,
       "nfsClientFsstat": nfsClientFsstat}
)
