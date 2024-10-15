# SNMP MIB module (HUAWEI-BRAS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:01 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

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

hwMulticastVirtualAdjust = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMulticastVirtualAdjustMibObjects_ObjectIdentity = ObjectIdentity
hwMulticastVirtualAdjustMibObjects = _HwMulticastVirtualAdjustMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1)
)
_HwMulticastVirtualAdjustSetBandTable_Object = MibTable
hwMulticastVirtualAdjustSetBandTable = _HwMulticastVirtualAdjustSetBandTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1)
)
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandTable.setStatus("current")
_HwMulticastVirtualAdjustSetBandEntry_Object = MibTableRow
hwMulticastVirtualAdjustSetBandEntry = _HwMulticastVirtualAdjustSetBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1)
)
hwMulticastVirtualAdjustSetBandEntry.setIndexNames(
    (0, "HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandListIndex"),
)
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandEntry.setStatus("current")


class _HwMulticastVirtualAdjustSetBandListIndex_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustSetBandListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwMulticastVirtualAdjustSetBandListIndex_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustSetBandListIndex_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandListIndex = _HwMulticastVirtualAdjustSetBandListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 1),
    _HwMulticastVirtualAdjustSetBandListIndex_Type()
)
hwMulticastVirtualAdjustSetBandListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandListIndex.setStatus("current")


class _HwMulticastVirtualAdjustSetBandType_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustSetBandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_HwMulticastVirtualAdjustSetBandType_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustSetBandType_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandType = _HwMulticastVirtualAdjustSetBandType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 2),
    _HwMulticastVirtualAdjustSetBandType_Type()
)
hwMulticastVirtualAdjustSetBandType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandType.setStatus("current")


class _HwMulticastVirtualAdjustSetBandValue_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustSetBandValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400000),
    )


_HwMulticastVirtualAdjustSetBandValue_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustSetBandValue_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandValue = _HwMulticastVirtualAdjustSetBandValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 3),
    _HwMulticastVirtualAdjustSetBandValue_Type()
)
hwMulticastVirtualAdjustSetBandValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandValue.setStatus("current")


class _HwMulticastVirtualAdjustSetBandDetectInterval_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustSetBandDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_HwMulticastVirtualAdjustSetBandDetectInterval_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustSetBandDetectInterval_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandDetectInterval = _HwMulticastVirtualAdjustSetBandDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 4),
    _HwMulticastVirtualAdjustSetBandDetectInterval_Type()
)
hwMulticastVirtualAdjustSetBandDetectInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandDetectInterval.setStatus("current")


class _HwMulticastVirtualAdjustSetBandThreshold_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustSetBandThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMulticastVirtualAdjustSetBandThreshold_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustSetBandThreshold_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandThreshold = _HwMulticastVirtualAdjustSetBandThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 5),
    _HwMulticastVirtualAdjustSetBandThreshold_Type()
)
hwMulticastVirtualAdjustSetBandThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandThreshold.setStatus("current")
_HwMulticastVirtualAdjustSetBandRowStatus_Type = RowStatus
_HwMulticastVirtualAdjustSetBandRowStatus_Object = MibTableColumn
hwMulticastVirtualAdjustSetBandRowStatus = _HwMulticastVirtualAdjustSetBandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 1, 1, 6),
    _HwMulticastVirtualAdjustSetBandRowStatus_Type()
)
hwMulticastVirtualAdjustSetBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustSetBandRowStatus.setStatus("current")
_HwMulticastVirtualAdjustShowBandTable_Object = MibTable
hwMulticastVirtualAdjustShowBandTable = _HwMulticastVirtualAdjustShowBandTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2)
)
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandTable.setStatus("current")
_HwMulticastVirtualAdjustShowBandEntry_Object = MibTableRow
hwMulticastVirtualAdjustShowBandEntry = _HwMulticastVirtualAdjustShowBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2, 1)
)
hwMulticastVirtualAdjustShowBandEntry.setIndexNames(
    (0, "HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustShowBandListIndex"),
    (0, "HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustShowBandSourceIp"),
    (0, "HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustShowBandGroupIp"),
)
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandEntry.setStatus("current")


class _HwMulticastVirtualAdjustShowBandListIndex_Type(Integer32):
    """Custom type hwMulticastVirtualAdjustShowBandListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwMulticastVirtualAdjustShowBandListIndex_Type.__name__ = "Integer32"
_HwMulticastVirtualAdjustShowBandListIndex_Object = MibTableColumn
hwMulticastVirtualAdjustShowBandListIndex = _HwMulticastVirtualAdjustShowBandListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2, 1, 1),
    _HwMulticastVirtualAdjustShowBandListIndex_Type()
)
hwMulticastVirtualAdjustShowBandListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandListIndex.setStatus("current")
_HwMulticastVirtualAdjustShowBandSourceIp_Type = IpAddress
_HwMulticastVirtualAdjustShowBandSourceIp_Object = MibTableColumn
hwMulticastVirtualAdjustShowBandSourceIp = _HwMulticastVirtualAdjustShowBandSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2, 1, 2),
    _HwMulticastVirtualAdjustShowBandSourceIp_Type()
)
hwMulticastVirtualAdjustShowBandSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandSourceIp.setStatus("current")
_HwMulticastVirtualAdjustShowBandGroupIp_Type = IpAddress
_HwMulticastVirtualAdjustShowBandGroupIp_Object = MibTableColumn
hwMulticastVirtualAdjustShowBandGroupIp = _HwMulticastVirtualAdjustShowBandGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2, 1, 3),
    _HwMulticastVirtualAdjustShowBandGroupIp_Type()
)
hwMulticastVirtualAdjustShowBandGroupIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandGroupIp.setStatus("current")
_HwMulticastVirtualAdjustShowBandwidth_Type = Integer32
_HwMulticastVirtualAdjustShowBandwidth_Object = MibTableColumn
hwMulticastVirtualAdjustShowBandwidth = _HwMulticastVirtualAdjustShowBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 1, 2, 1, 4),
    _HwMulticastVirtualAdjustShowBandwidth_Type()
)
hwMulticastVirtualAdjustShowBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMulticastVirtualAdjustShowBandwidth.setStatus("current")
_HwMulticastMIBConformance_ObjectIdentity = ObjectIdentity
hwMulticastMIBConformance = _HwMulticastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 2)
)
_HwMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
hwMulticastMIBCompliances = _HwMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 2, 1)
)
_HwMulticastMIBGroups_ObjectIdentity = ObjectIdentity
hwMulticastMIBGroups = _HwMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 2, 2)
)

# Managed Objects groups

hwMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 2, 2, 1)
)
hwMulticastGroup.setObjects(
      *(("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandType"),
        ("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandValue"),
        ("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandDetectInterval"),
        ("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandThreshold"),
        ("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustSetBandRowStatus"),
        ("HUAWEI-BRAS-MULTICAST-MIB", "hwMulticastVirtualAdjustShowBandwidth"))
)
if mibBuilder.loadTexts:
    hwMulticastGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-MULTICAST-MIB",
    **{"hwMulticastVirtualAdjust": hwMulticastVirtualAdjust,
       "hwMulticastVirtualAdjustMibObjects": hwMulticastVirtualAdjustMibObjects,
       "hwMulticastVirtualAdjustSetBandTable": hwMulticastVirtualAdjustSetBandTable,
       "hwMulticastVirtualAdjustSetBandEntry": hwMulticastVirtualAdjustSetBandEntry,
       "hwMulticastVirtualAdjustSetBandListIndex": hwMulticastVirtualAdjustSetBandListIndex,
       "hwMulticastVirtualAdjustSetBandType": hwMulticastVirtualAdjustSetBandType,
       "hwMulticastVirtualAdjustSetBandValue": hwMulticastVirtualAdjustSetBandValue,
       "hwMulticastVirtualAdjustSetBandDetectInterval": hwMulticastVirtualAdjustSetBandDetectInterval,
       "hwMulticastVirtualAdjustSetBandThreshold": hwMulticastVirtualAdjustSetBandThreshold,
       "hwMulticastVirtualAdjustSetBandRowStatus": hwMulticastVirtualAdjustSetBandRowStatus,
       "hwMulticastVirtualAdjustShowBandTable": hwMulticastVirtualAdjustShowBandTable,
       "hwMulticastVirtualAdjustShowBandEntry": hwMulticastVirtualAdjustShowBandEntry,
       "hwMulticastVirtualAdjustShowBandListIndex": hwMulticastVirtualAdjustShowBandListIndex,
       "hwMulticastVirtualAdjustShowBandSourceIp": hwMulticastVirtualAdjustShowBandSourceIp,
       "hwMulticastVirtualAdjustShowBandGroupIp": hwMulticastVirtualAdjustShowBandGroupIp,
       "hwMulticastVirtualAdjustShowBandwidth": hwMulticastVirtualAdjustShowBandwidth,
       "hwMulticastMIBConformance": hwMulticastMIBConformance,
       "hwMulticastMIBCompliances": hwMulticastMIBCompliances,
       "hwMulticastMIBCompliance": hwMulticastMIBCompliance,
       "hwMulticastMIBGroups": hwMulticastMIBGroups,
       "hwMulticastGroup": hwMulticastGroup}
)
