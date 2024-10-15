# SNMP MIB module (MARVELL-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-ROUTEMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:13 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlRouteMap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 227)
)
rlRouteMap.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlRouteMapInetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlRouteMapPbrTable_Object = MibTable
rlRouteMapPbrTable = _RlRouteMapPbrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1)
)
if mibBuilder.loadTexts:
    rlRouteMapPbrTable.setStatus("current")
_RlRouteMapPbrEntry_Object = MibTableRow
rlRouteMapPbrEntry = _RlRouteMapPbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1)
)
rlRouteMapPbrEntry.setIndexNames(
    (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"),
    (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"),
    (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrInetType"),
)
if mibBuilder.loadTexts:
    rlRouteMapPbrEntry.setStatus("current")


class _RlRouteMapPbrRouteMapName_Type(DisplayString):
    """Custom type rlRouteMapPbrRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRouteMapPbrRouteMapName_Type.__name__ = "DisplayString"
_RlRouteMapPbrRouteMapName_Object = MibTableColumn
rlRouteMapPbrRouteMapName = _RlRouteMapPbrRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 1),
    _RlRouteMapPbrRouteMapName_Type()
)
rlRouteMapPbrRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRouteMapPbrRouteMapName.setStatus("current")


class _RlRouteMapPbrRouteMapSectionId_Type(Unsigned32):
    """Custom type rlRouteMapPbrRouteMapSectionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlRouteMapPbrRouteMapSectionId_Type.__name__ = "Unsigned32"
_RlRouteMapPbrRouteMapSectionId_Object = MibTableColumn
rlRouteMapPbrRouteMapSectionId = _RlRouteMapPbrRouteMapSectionId_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 2),
    _RlRouteMapPbrRouteMapSectionId_Type()
)
rlRouteMapPbrRouteMapSectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRouteMapPbrRouteMapSectionId.setStatus("current")
_RlRouteMapPbrInetType_Type = RlRouteMapInetType
_RlRouteMapPbrInetType_Object = MibTableColumn
rlRouteMapPbrInetType = _RlRouteMapPbrInetType_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 3),
    _RlRouteMapPbrInetType_Type()
)
rlRouteMapPbrInetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrInetType.setStatus("current")
_RlRouteMapPbrMatchAccessListName_Type = DisplayString
_RlRouteMapPbrMatchAccessListName_Object = MibTableColumn
rlRouteMapPbrMatchAccessListName = _RlRouteMapPbrMatchAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 4),
    _RlRouteMapPbrMatchAccessListName_Type()
)
rlRouteMapPbrMatchAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrMatchAccessListName.setStatus("current")
_RlRouteMapPbrActionNexthopInetAddressType_Type = InetAddressType
_RlRouteMapPbrActionNexthopInetAddressType_Object = MibTableColumn
rlRouteMapPbrActionNexthopInetAddressType = _RlRouteMapPbrActionNexthopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 5),
    _RlRouteMapPbrActionNexthopInetAddressType_Type()
)
rlRouteMapPbrActionNexthopInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopInetAddressType.setStatus("current")
_RlRouteMapPbrActionNexthopInetAddress_Type = InetAddress
_RlRouteMapPbrActionNexthopInetAddress_Object = MibTableColumn
rlRouteMapPbrActionNexthopInetAddress = _RlRouteMapPbrActionNexthopInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 6),
    _RlRouteMapPbrActionNexthopInetAddress_Type()
)
rlRouteMapPbrActionNexthopInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopInetAddress.setStatus("current")
_RlRouteMapPbrActionNexthopIfIndex_Type = InterfaceIndexOrZero
_RlRouteMapPbrActionNexthopIfIndex_Object = MibTableColumn
rlRouteMapPbrActionNexthopIfIndex = _RlRouteMapPbrActionNexthopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 7),
    _RlRouteMapPbrActionNexthopIfIndex_Type()
)
rlRouteMapPbrActionNexthopIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopIfIndex.setStatus("current")
_RlRouteMapPbrRowStatus_Type = RowStatus
_RlRouteMapPbrRowStatus_Object = MibTableColumn
rlRouteMapPbrRowStatus = _RlRouteMapPbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 8),
    _RlRouteMapPbrRowStatus_Type()
)
rlRouteMapPbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-ROUTEMAP-MIB",
    **{"RlRouteMapInetType": RlRouteMapInetType,
       "rlRouteMap": rlRouteMap,
       "rlRouteMapPbrTable": rlRouteMapPbrTable,
       "rlRouteMapPbrEntry": rlRouteMapPbrEntry,
       "rlRouteMapPbrRouteMapName": rlRouteMapPbrRouteMapName,
       "rlRouteMapPbrRouteMapSectionId": rlRouteMapPbrRouteMapSectionId,
       "rlRouteMapPbrInetType": rlRouteMapPbrInetType,
       "rlRouteMapPbrMatchAccessListName": rlRouteMapPbrMatchAccessListName,
       "rlRouteMapPbrActionNexthopInetAddressType": rlRouteMapPbrActionNexthopInetAddressType,
       "rlRouteMapPbrActionNexthopInetAddress": rlRouteMapPbrActionNexthopInetAddress,
       "rlRouteMapPbrActionNexthopIfIndex": rlRouteMapPbrActionNexthopIfIndex,
       "rlRouteMapPbrRowStatus": rlRouteMapPbrRowStatus}
)
