# SNMP MIB module (HUAWEI-PIM-BSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PIM-BSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:30 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetZoneIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwPimBsrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2)
)
hwPimBsrMib.setRevisions(
        ("2007-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMcast_ObjectIdentity = ObjectIdentity
hwMcast = _HwMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149)
)
_HwPimBsrObjects_ObjectIdentity = ObjectIdentity
hwPimBsrObjects = _HwPimBsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1)
)
_HwPimBsrElectedBsrRpSetTable_Object = MibTable
hwPimBsrElectedBsrRpSetTable = _HwPimBsrElectedBsrRpSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetTable.setStatus("current")
_HwPimBsrElectedBsrRpSetEntry_Object = MibTableRow
hwPimBsrElectedBsrRpSetEntry = _HwPimBsrElectedBsrRpSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1)
)
hwPimBsrElectedBsrRpSetEntry.setIndexNames(
    (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingAddrType"),
    (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingGrpAddr"),
    (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingGrpPrefixLen"),
    (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingRPAddr"),
)
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetEntry.setStatus("current")
_HwPimBsrElectedBsrGrpMappingAddrType_Type = InetAddressType
_HwPimBsrElectedBsrGrpMappingAddrType_Object = MibTableColumn
hwPimBsrElectedBsrGrpMappingAddrType = _HwPimBsrElectedBsrGrpMappingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 2),
    _HwPimBsrElectedBsrGrpMappingAddrType_Type()
)
hwPimBsrElectedBsrGrpMappingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrGrpMappingAddrType.setStatus("current")


class _HwPimBsrElectedBsrGrpMappingGrpAddr_Type(InetAddress):
    """Custom type hwPimBsrElectedBsrGrpMappingGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimBsrElectedBsrGrpMappingGrpAddr_Type.__name__ = "InetAddress"
_HwPimBsrElectedBsrGrpMappingGrpAddr_Object = MibTableColumn
hwPimBsrElectedBsrGrpMappingGrpAddr = _HwPimBsrElectedBsrGrpMappingGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 3),
    _HwPimBsrElectedBsrGrpMappingGrpAddr_Type()
)
hwPimBsrElectedBsrGrpMappingGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrGrpMappingGrpAddr.setStatus("current")


class _HwPimBsrElectedBsrGrpMappingGrpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type hwPimBsrElectedBsrGrpMappingGrpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwPimBsrElectedBsrGrpMappingGrpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_HwPimBsrElectedBsrGrpMappingGrpPrefixLen_Object = MibTableColumn
hwPimBsrElectedBsrGrpMappingGrpPrefixLen = _HwPimBsrElectedBsrGrpMappingGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 4),
    _HwPimBsrElectedBsrGrpMappingGrpPrefixLen_Type()
)
hwPimBsrElectedBsrGrpMappingGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrGrpMappingGrpPrefixLen.setStatus("current")


class _HwPimBsrElectedBsrGrpMappingRPAddr_Type(InetAddress):
    """Custom type hwPimBsrElectedBsrGrpMappingRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimBsrElectedBsrGrpMappingRPAddr_Type.__name__ = "InetAddress"
_HwPimBsrElectedBsrGrpMappingRPAddr_Object = MibTableColumn
hwPimBsrElectedBsrGrpMappingRPAddr = _HwPimBsrElectedBsrGrpMappingRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 5),
    _HwPimBsrElectedBsrGrpMappingRPAddr_Type()
)
hwPimBsrElectedBsrGrpMappingRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrGrpMappingRPAddr.setStatus("current")


class _HwPimBsrElectedBsrRpSetPriority_Type(Unsigned32):
    """Custom type hwPimBsrElectedBsrRpSetPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPimBsrElectedBsrRpSetPriority_Type.__name__ = "Unsigned32"
_HwPimBsrElectedBsrRpSetPriority_Object = MibTableColumn
hwPimBsrElectedBsrRpSetPriority = _HwPimBsrElectedBsrRpSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 6),
    _HwPimBsrElectedBsrRpSetPriority_Type()
)
hwPimBsrElectedBsrRpSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetPriority.setStatus("current")


class _HwPimBsrElectedBsrRpSetHoldtime_Type(Unsigned32):
    """Custom type hwPimBsrElectedBsrRpSetHoldtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimBsrElectedBsrRpSetHoldtime_Type.__name__ = "Unsigned32"
_HwPimBsrElectedBsrRpSetHoldtime_Object = MibTableColumn
hwPimBsrElectedBsrRpSetHoldtime = _HwPimBsrElectedBsrRpSetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 7),
    _HwPimBsrElectedBsrRpSetHoldtime_Type()
)
hwPimBsrElectedBsrRpSetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetHoldtime.setUnits("seconds")
_HwPimBsrElectedBsrRpSetExpiryTime_Type = TimeTicks
_HwPimBsrElectedBsrRpSetExpiryTime_Object = MibTableColumn
hwPimBsrElectedBsrRpSetExpiryTime = _HwPimBsrElectedBsrRpSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 8),
    _HwPimBsrElectedBsrRpSetExpiryTime_Type()
)
hwPimBsrElectedBsrRpSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetExpiryTime.setStatus("current")
_HwPimBsrElectedBsrRpSetGrpBidir_Type = TruthValue
_HwPimBsrElectedBsrRpSetGrpBidir_Object = MibTableColumn
hwPimBsrElectedBsrRpSetGrpBidir = _HwPimBsrElectedBsrRpSetGrpBidir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 9),
    _HwPimBsrElectedBsrRpSetGrpBidir_Type()
)
hwPimBsrElectedBsrRpSetGrpBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimBsrElectedBsrRpSetGrpBidir.setStatus("current")
_HwPimBsrConformance_ObjectIdentity = ObjectIdentity
hwPimBsrConformance = _HwPimBsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2)
)
_HwPimBsrCompliances_ObjectIdentity = ObjectIdentity
hwPimBsrCompliances = _HwPimBsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 1)
)
_HwPimBsrGroups_ObjectIdentity = ObjectIdentity
hwPimBsrGroups = _HwPimBsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 2)
)

# Managed Objects groups

hwPimBsrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 2, 1)
)
hwPimBsrObjectGroup.setObjects(
      *(("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetPriority"),
        ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetHoldtime"),
        ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetExpiryTime"),
        ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetGrpBidir"))
)
if mibBuilder.loadTexts:
    hwPimBsrObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPimBsrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwPimBsrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PIM-BSR-MIB",
    **{"hwMcast": hwMcast,
       "hwPimBsrMib": hwPimBsrMib,
       "hwPimBsrObjects": hwPimBsrObjects,
       "hwPimBsrElectedBsrRpSetTable": hwPimBsrElectedBsrRpSetTable,
       "hwPimBsrElectedBsrRpSetEntry": hwPimBsrElectedBsrRpSetEntry,
       "hwPimBsrElectedBsrGrpMappingAddrType": hwPimBsrElectedBsrGrpMappingAddrType,
       "hwPimBsrElectedBsrGrpMappingGrpAddr": hwPimBsrElectedBsrGrpMappingGrpAddr,
       "hwPimBsrElectedBsrGrpMappingGrpPrefixLen": hwPimBsrElectedBsrGrpMappingGrpPrefixLen,
       "hwPimBsrElectedBsrGrpMappingRPAddr": hwPimBsrElectedBsrGrpMappingRPAddr,
       "hwPimBsrElectedBsrRpSetPriority": hwPimBsrElectedBsrRpSetPriority,
       "hwPimBsrElectedBsrRpSetHoldtime": hwPimBsrElectedBsrRpSetHoldtime,
       "hwPimBsrElectedBsrRpSetExpiryTime": hwPimBsrElectedBsrRpSetExpiryTime,
       "hwPimBsrElectedBsrRpSetGrpBidir": hwPimBsrElectedBsrRpSetGrpBidir,
       "hwPimBsrConformance": hwPimBsrConformance,
       "hwPimBsrCompliances": hwPimBsrCompliances,
       "hwPimBsrCompliance": hwPimBsrCompliance,
       "hwPimBsrGroups": hwPimBsrGroups,
       "hwPimBsrObjectGroup": hwPimBsrObjectGroup}
)
