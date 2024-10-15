# SNMP MIB module (MARVELL-PBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-PBR-MIB
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

(rlRouteMapPbrRouteMapName,
 rlRouteMapPbrRouteMapSectionId) = mibBuilder.importSymbols(
    "MARVELL-ROUTEMAP-MIB",
    "rlRouteMapPbrRouteMapName",
    "rlRouteMapPbrRouteMapSectionId")

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

rlPolicyBasedRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 228)
)
rlPolicyBasedRouting.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPBRInetType(Integer32, TextualConvention):
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



class RlPBRStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("interfaceDown", 3),
          ("noIp", 2))
    )



class RlPBRNexthopStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notDirect", 3),
          ("notReachable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlPBRTable_Object = MibTable
rlPBRTable = _RlPBRTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1)
)
if mibBuilder.loadTexts:
    rlPBRTable.setStatus("current")
_RlPBREntry_Object = MibTableRow
rlPBREntry = _RlPBREntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1)
)
rlPBREntry.setIndexNames(
    (0, "MARVELL-PBR-MIB", "rlPBRIfIndex"),
    (0, "MARVELL-PBR-MIB", "rlPBRInetType"),
)
if mibBuilder.loadTexts:
    rlPBREntry.setStatus("current")
_RlPBRIfIndex_Type = InterfaceIndex
_RlPBRIfIndex_Object = MibTableColumn
rlPBRIfIndex = _RlPBRIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 1),
    _RlPBRIfIndex_Type()
)
rlPBRIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPBRIfIndex.setStatus("current")
_RlPBRInetType_Type = RlPBRInetType
_RlPBRInetType_Object = MibTableColumn
rlPBRInetType = _RlPBRInetType_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 2),
    _RlPBRInetType_Type()
)
rlPBRInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPBRInetType.setStatus("current")


class _RlPBRRouteMapName_Type(DisplayString):
    """Custom type rlPBRRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlPBRRouteMapName_Type.__name__ = "DisplayString"
_RlPBRRouteMapName_Object = MibTableColumn
rlPBRRouteMapName = _RlPBRRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 3),
    _RlPBRRouteMapName_Type()
)
rlPBRRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPBRRouteMapName.setStatus("current")
_RlPBRStatus_Type = RlPBRStatusType
_RlPBRStatus_Object = MibTableColumn
rlPBRStatus = _RlPBRStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 4),
    _RlPBRStatus_Type()
)
rlPBRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRStatus.setStatus("current")
_RlPBRRowStatus_Type = RowStatus
_RlPBRRowStatus_Object = MibTableColumn
rlPBRRowStatus = _RlPBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 5),
    _RlPBRRowStatus_Type()
)
rlPBRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPBRRowStatus.setStatus("current")
_RlPBRInfoTable_Object = MibTable
rlPBRInfoTable = _RlPBRInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2)
)
if mibBuilder.loadTexts:
    rlPBRInfoTable.setStatus("current")
_RlPBRInfoEntry_Object = MibTableRow
rlPBRInfoEntry = _RlPBRInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1)
)
rlPBRInfoEntry.setIndexNames(
    (0, "MARVELL-PBR-MIB", "rlPBRInetType"),
    (0, "MARVELL-PBR-MIB", "rlPBRIfIndex"),
    (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"),
    (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"),
)
if mibBuilder.loadTexts:
    rlPBRInfoEntry.setStatus("current")


class _RlPBRInfoAccessListName_Type(DisplayString):
    """Custom type rlPBRInfoAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlPBRInfoAccessListName_Type.__name__ = "DisplayString"
_RlPBRInfoAccessListName_Object = MibTableColumn
rlPBRInfoAccessListName = _RlPBRInfoAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 1),
    _RlPBRInfoAccessListName_Type()
)
rlPBRInfoAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRInfoAccessListName.setStatus("current")
_RlPBRInfoNexthopInetAddressType_Type = InetAddressType
_RlPBRInfoNexthopInetAddressType_Object = MibTableColumn
rlPBRInfoNexthopInetAddressType = _RlPBRInfoNexthopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 2),
    _RlPBRInfoNexthopInetAddressType_Type()
)
rlPBRInfoNexthopInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRInfoNexthopInetAddressType.setStatus("current")
_RlPBRInfoNexthopInetAddress_Type = InetAddress
_RlPBRInfoNexthopInetAddress_Object = MibTableColumn
rlPBRInfoNexthopInetAddress = _RlPBRInfoNexthopInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 3),
    _RlPBRInfoNexthopInetAddress_Type()
)
rlPBRInfoNexthopInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRInfoNexthopInetAddress.setStatus("current")
_RlPBRInfoNexthopIfIndex_Type = InterfaceIndexOrZero
_RlPBRInfoNexthopIfIndex_Object = MibTableColumn
rlPBRInfoNexthopIfIndex = _RlPBRInfoNexthopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 4),
    _RlPBRInfoNexthopIfIndex_Type()
)
rlPBRInfoNexthopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRInfoNexthopIfIndex.setStatus("current")
_RlPBRInfoNexthopStatus_Type = RlPBRNexthopStatusType
_RlPBRInfoNexthopStatus_Object = MibTableColumn
rlPBRInfoNexthopStatus = _RlPBRInfoNexthopStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 5),
    _RlPBRInfoNexthopStatus_Type()
)
rlPBRInfoNexthopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPBRInfoNexthopStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-PBR-MIB",
    **{"RlPBRInetType": RlPBRInetType,
       "RlPBRStatusType": RlPBRStatusType,
       "RlPBRNexthopStatusType": RlPBRNexthopStatusType,
       "rlPolicyBasedRouting": rlPolicyBasedRouting,
       "rlPBRTable": rlPBRTable,
       "rlPBREntry": rlPBREntry,
       "rlPBRIfIndex": rlPBRIfIndex,
       "rlPBRInetType": rlPBRInetType,
       "rlPBRRouteMapName": rlPBRRouteMapName,
       "rlPBRStatus": rlPBRStatus,
       "rlPBRRowStatus": rlPBRRowStatus,
       "rlPBRInfoTable": rlPBRInfoTable,
       "rlPBRInfoEntry": rlPBRInfoEntry,
       "rlPBRInfoAccessListName": rlPBRInfoAccessListName,
       "rlPBRInfoNexthopInetAddressType": rlPBRInfoNexthopInetAddressType,
       "rlPBRInfoNexthopInetAddress": rlPBRInfoNexthopInetAddress,
       "rlPBRInfoNexthopIfIndex": rlPBRInfoNexthopIfIndex,
       "rlPBRInfoNexthopStatus": rlPBRInfoNexthopStatus}
)
