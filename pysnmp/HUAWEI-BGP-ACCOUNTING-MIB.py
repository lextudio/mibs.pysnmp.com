# SNMP MIB module (HUAWEI-BGP-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BGP-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:53 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hwBgpAcctMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("invalid", 0),
          ("source", 1))
    )



class DirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inboundAndOutbound", 3),
          ("invalid", 0),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwBgpAcctMIBObjects_ObjectIdentity = ObjectIdentity
hwBgpAcctMIBObjects = _HwBgpAcctMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1)
)
_HwBgpAcctCfgTable_Object = MibTable
hwBgpAcctCfgTable = _HwBgpAcctCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpAcctCfgTable.setStatus("current")
_HwBgpAcctCfgEntry_Object = MibTableRow
hwBgpAcctCfgEntry = _HwBgpAcctCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1)
)
hwBgpAcctCfgEntry.setIndexNames(
    (0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwBgpAcctCfgEntry.setStatus("current")
_HwbgpAcctCfgIfIndex_Type = Integer32
_HwbgpAcctCfgIfIndex_Object = MibTableColumn
hwbgpAcctCfgIfIndex = _HwbgpAcctCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 1),
    _HwbgpAcctCfgIfIndex_Type()
)
hwbgpAcctCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctCfgIfIndex.setStatus("current")


class _HwbgpAcctSrcOrDest_Type(AddressType):
    """Custom type hwbgpAcctSrcOrDest based on AddressType"""
    defaultValue = 2


_HwbgpAcctSrcOrDest_Object = MibTableColumn
hwbgpAcctSrcOrDest = _HwbgpAcctSrcOrDest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 2),
    _HwbgpAcctSrcOrDest_Type()
)
hwbgpAcctSrcOrDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwbgpAcctSrcOrDest.setStatus("current")


class _HwbgpAcctDirection_Type(DirectionType):
    """Custom type hwbgpAcctDirection based on DirectionType"""
    defaultValue = 1


_HwbgpAcctDirection_Object = MibTableColumn
hwbgpAcctDirection = _HwbgpAcctDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 3),
    _HwbgpAcctDirection_Type()
)
hwbgpAcctDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwbgpAcctDirection.setStatus("current")
_HwbgpAcctCfgRowStatus_Type = RowStatus
_HwbgpAcctCfgRowStatus_Object = MibTableColumn
hwbgpAcctCfgRowStatus = _HwbgpAcctCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 4),
    _HwbgpAcctCfgRowStatus_Type()
)
hwbgpAcctCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwbgpAcctCfgRowStatus.setStatus("current")
_HwBgpAcctStatTable_Object = MibTable
hwBgpAcctStatTable = _HwBgpAcctStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2)
)
if mibBuilder.loadTexts:
    hwBgpAcctStatTable.setStatus("current")
_HwBgpAcctStatEntry_Object = MibTableRow
hwBgpAcctStatEntry = _HwBgpAcctStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1)
)
hwBgpAcctStatEntry.setIndexNames(
    (0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctStatIfIndex"),
    (0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctTrafficIndex"),
)
if mibBuilder.loadTexts:
    hwBgpAcctStatEntry.setStatus("current")
_HwbgpAcctStatIfIndex_Type = Integer32
_HwbgpAcctStatIfIndex_Object = MibTableColumn
hwbgpAcctStatIfIndex = _HwbgpAcctStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 1),
    _HwbgpAcctStatIfIndex_Type()
)
hwbgpAcctStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctStatIfIndex.setStatus("current")


class _HwbgpAcctTrafficIndex_Type(Integer32):
    """Custom type hwbgpAcctTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwbgpAcctTrafficIndex_Type.__name__ = "Integer32"
_HwbgpAcctTrafficIndex_Object = MibTableColumn
hwbgpAcctTrafficIndex = _HwbgpAcctTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 2),
    _HwbgpAcctTrafficIndex_Type()
)
hwbgpAcctTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctTrafficIndex.setStatus("current")
_HwbgpAcctInPacketCount_Type = Counter64
_HwbgpAcctInPacketCount_Object = MibTableColumn
hwbgpAcctInPacketCount = _HwbgpAcctInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 3),
    _HwbgpAcctInPacketCount_Type()
)
hwbgpAcctInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctInPacketCount.setStatus("current")
_HwbgpAcctInOctetCount_Type = Counter64
_HwbgpAcctInOctetCount_Object = MibTableColumn
hwbgpAcctInOctetCount = _HwbgpAcctInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 4),
    _HwbgpAcctInOctetCount_Type()
)
hwbgpAcctInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctInOctetCount.setStatus("current")
_HwbgpAcctOutPacketCount_Type = Counter64
_HwbgpAcctOutPacketCount_Object = MibTableColumn
hwbgpAcctOutPacketCount = _HwbgpAcctOutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 5),
    _HwbgpAcctOutPacketCount_Type()
)
hwbgpAcctOutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctOutPacketCount.setStatus("current")
_HwbgpAcctOutOctetCount_Type = Counter64
_HwbgpAcctOutOctetCount_Object = MibTableColumn
hwbgpAcctOutOctetCount = _HwbgpAcctOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 6),
    _HwbgpAcctOutOctetCount_Type()
)
hwbgpAcctOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwbgpAcctOutOctetCount.setStatus("current")
_HwBgpAcctConformance_ObjectIdentity = ObjectIdentity
hwBgpAcctConformance = _HwBgpAcctConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2)
)
_HwBgpAcctCompliances_ObjectIdentity = ObjectIdentity
hwBgpAcctCompliances = _HwBgpAcctCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 1)
)
_HwBgpAcctStatGroups_ObjectIdentity = ObjectIdentity
hwBgpAcctStatGroups = _HwBgpAcctStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2)
)

# Managed Objects groups

hwBgpAcctCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2, 1)
)
hwBgpAcctCfgGroup.setObjects(
      *(("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctCfgIfIndex"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctSrcOrDest"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctDirection"))
)
if mibBuilder.loadTexts:
    hwBgpAcctCfgGroup.setStatus("current")

hwBgpAcctStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2, 2)
)
hwBgpAcctStatGroup.setObjects(
      *(("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctStatIfIndex"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctTrafficIndex"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctInPacketCount"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctInOctetCount"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctOutPacketCount"),
        ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctOutOctetCount"))
)
if mibBuilder.loadTexts:
    hwBgpAcctStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwBgpAcctCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpAcctCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BGP-ACCOUNTING-MIB",
    **{"AddressType": AddressType,
       "DirectionType": DirectionType,
       "hwBgpAcctMIB": hwBgpAcctMIB,
       "hwBgpAcctMIBObjects": hwBgpAcctMIBObjects,
       "hwBgpAcctCfgTable": hwBgpAcctCfgTable,
       "hwBgpAcctCfgEntry": hwBgpAcctCfgEntry,
       "hwbgpAcctCfgIfIndex": hwbgpAcctCfgIfIndex,
       "hwbgpAcctSrcOrDest": hwbgpAcctSrcOrDest,
       "hwbgpAcctDirection": hwbgpAcctDirection,
       "hwbgpAcctCfgRowStatus": hwbgpAcctCfgRowStatus,
       "hwBgpAcctStatTable": hwBgpAcctStatTable,
       "hwBgpAcctStatEntry": hwBgpAcctStatEntry,
       "hwbgpAcctStatIfIndex": hwbgpAcctStatIfIndex,
       "hwbgpAcctTrafficIndex": hwbgpAcctTrafficIndex,
       "hwbgpAcctInPacketCount": hwbgpAcctInPacketCount,
       "hwbgpAcctInOctetCount": hwbgpAcctInOctetCount,
       "hwbgpAcctOutPacketCount": hwbgpAcctOutPacketCount,
       "hwbgpAcctOutOctetCount": hwbgpAcctOutOctetCount,
       "hwBgpAcctConformance": hwBgpAcctConformance,
       "hwBgpAcctCompliances": hwBgpAcctCompliances,
       "hwBgpAcctCompliance": hwBgpAcctCompliance,
       "hwBgpAcctStatGroups": hwBgpAcctStatGroups,
       "hwBgpAcctCfgGroup": hwBgpAcctCfgGroup,
       "hwBgpAcctStatGroup": hwBgpAcctStatGroup}
)
