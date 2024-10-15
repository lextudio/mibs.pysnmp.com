# SNMP MIB module (PDN-SOCKET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SOCKET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:07 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(pdn_socket,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-socket")

(SocketFamily,
 SocketState,
 SocketType) = mibBuilder.importSymbols(
    "PDN-TC",
    "SocketFamily",
    "SocketState",
    "SocketType")

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
    "iso")

(DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevSocketStatsMIBObjects_ObjectIdentity = ObjectIdentity
devSocketStatsMIBObjects = _DevSocketStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1)
)
_DevSocketStatsTable_Object = MibTable
devSocketStatsTable = _DevSocketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    devSocketStatsTable.setStatus("mandatory")
_DevSocketStatsEntry_Object = MibTableRow
devSocketStatsEntry = _DevSocketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1)
)
devSocketStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-SOCKET-MIB", "devSocketNumber"),
)
if mibBuilder.loadTexts:
    devSocketStatsEntry.setStatus("mandatory")
_DevSocketNumber_Type = Integer32
_DevSocketNumber_Object = MibTableColumn
devSocketNumber = _DevSocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 1),
    _DevSocketNumber_Type()
)
devSocketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketNumber.setStatus("mandatory")
_DevSocketName_Type = DisplayString
_DevSocketName_Object = MibTableColumn
devSocketName = _DevSocketName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 2),
    _DevSocketName_Type()
)
devSocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketName.setStatus("mandatory")
_DevSocketFamily_Type = SocketFamily
_DevSocketFamily_Object = MibTableColumn
devSocketFamily = _DevSocketFamily_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 3),
    _DevSocketFamily_Type()
)
devSocketFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketFamily.setStatus("mandatory")
_DevSocketType_Type = SocketType
_DevSocketType_Object = MibTableColumn
devSocketType = _DevSocketType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 4),
    _DevSocketType_Type()
)
devSocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketType.setStatus("mandatory")
_DevSocketLocalAddress_Type = TAddress
_DevSocketLocalAddress_Object = MibTableColumn
devSocketLocalAddress = _DevSocketLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 5),
    _DevSocketLocalAddress_Type()
)
devSocketLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketLocalAddress.setStatus("mandatory")
_DevSocketRemoteAddress_Type = TAddress
_DevSocketRemoteAddress_Object = MibTableColumn
devSocketRemoteAddress = _DevSocketRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 6),
    _DevSocketRemoteAddress_Type()
)
devSocketRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketRemoteAddress.setStatus("mandatory")
_DevSocketState_Type = SocketState
_DevSocketState_Object = MibTableColumn
devSocketState = _DevSocketState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 7),
    _DevSocketState_Type()
)
devSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketState.setStatus("mandatory")
_DevSocketInputBytes_Type = Integer32
_DevSocketInputBytes_Object = MibTableColumn
devSocketInputBytes = _DevSocketInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 8),
    _DevSocketInputBytes_Type()
)
devSocketInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketInputBytes.setStatus("mandatory")
_DevSocketOutputBytes_Type = Integer32
_DevSocketOutputBytes_Object = MibTableColumn
devSocketOutputBytes = _DevSocketOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 9),
    _DevSocketOutputBytes_Type()
)
devSocketOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketOutputBytes.setStatus("mandatory")
_DevSocketPDUDrops_Type = Integer32
_DevSocketPDUDrops_Object = MibTableColumn
devSocketPDUDrops = _DevSocketPDUDrops_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 10),
    _DevSocketPDUDrops_Type()
)
devSocketPDUDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketPDUDrops.setStatus("mandatory")
_DevSocketByteDrops_Type = Integer32
_DevSocketByteDrops_Object = MibTableColumn
devSocketByteDrops = _DevSocketByteDrops_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 11),
    _DevSocketByteDrops_Type()
)
devSocketByteDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSocketByteDrops.setStatus("mandatory")
_DevSocketStatsMIBTraps_ObjectIdentity = ObjectIdentity
devSocketStatsMIBTraps = _DevSocketStatsMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SOCKET-MIB",
    **{"devSocketStatsMIBObjects": devSocketStatsMIBObjects,
       "devSocketStatsTable": devSocketStatsTable,
       "devSocketStatsEntry": devSocketStatsEntry,
       "devSocketNumber": devSocketNumber,
       "devSocketName": devSocketName,
       "devSocketFamily": devSocketFamily,
       "devSocketType": devSocketType,
       "devSocketLocalAddress": devSocketLocalAddress,
       "devSocketRemoteAddress": devSocketRemoteAddress,
       "devSocketState": devSocketState,
       "devSocketInputBytes": devSocketInputBytes,
       "devSocketOutputBytes": devSocketOutputBytes,
       "devSocketPDUDrops": devSocketPDUDrops,
       "devSocketByteDrops": devSocketByteDrops,
       "devSocketStatsMIBTraps": devSocketStatsMIBTraps}
)
