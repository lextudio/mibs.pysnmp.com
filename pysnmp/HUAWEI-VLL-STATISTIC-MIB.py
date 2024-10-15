# SNMP MIB module (HUAWEI-VLL-STATISTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VLL-STATISTIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:26 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwL2VpnVllStatistic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwVllMIBObjects_ObjectIdentity = ObjectIdentity
hwVllMIBObjects = _HwVllMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1)
)
_HwVllStatisticTable_Object = MibTable
hwVllStatisticTable = _HwVllStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwVllStatisticTable.setStatus("current")
_HwVllStatisticEntry_Object = MibTableRow
hwVllStatisticEntry = _HwVllStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1)
)
hwVllStatisticEntry.setIndexNames(
    (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticIfIndex"),
    (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPwType"),
)
if mibBuilder.loadTexts:
    hwVllStatisticEntry.setStatus("current")
_HwVllStatisticIfIndex_Type = InterfaceIndex
_HwVllStatisticIfIndex_Object = MibTableColumn
hwVllStatisticIfIndex = _HwVllStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 1),
    _HwVllStatisticIfIndex_Type()
)
hwVllStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVllStatisticIfIndex.setStatus("current")


class _HwVllStatisticPwType_Type(Integer32):
    """Custom type hwVllStatisticPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HwVllStatisticPwType_Type.__name__ = "Integer32"
_HwVllStatisticPwType_Object = MibTableColumn
hwVllStatisticPwType = _HwVllStatisticPwType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 2),
    _HwVllStatisticPwType_Type()
)
hwVllStatisticPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVllStatisticPwType.setStatus("current")
_HwVllStatisticEnable_Type = EnabledStatus
_HwVllStatisticEnable_Object = MibTableColumn
hwVllStatisticEnable = _HwVllStatisticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 3),
    _HwVllStatisticEnable_Type()
)
hwVllStatisticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVllStatisticEnable.setStatus("current")


class _HwVllStatisticResetTraffic_Type(Integer32):
    """Custom type hwVllStatisticResetTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unknownStatus", 2))
    )


_HwVllStatisticResetTraffic_Type.__name__ = "Integer32"
_HwVllStatisticResetTraffic_Object = MibTableColumn
hwVllStatisticResetTraffic = _HwVllStatisticResetTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 4),
    _HwVllStatisticResetTraffic_Type()
)
hwVllStatisticResetTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVllStatisticResetTraffic.setStatus("current")
_HwVllStatisticResetTime_Type = TimeTicks
_HwVllStatisticResetTime_Object = MibTableColumn
hwVllStatisticResetTime = _HwVllStatisticResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 5),
    _HwVllStatisticResetTime_Type()
)
hwVllStatisticResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllStatisticResetTime.setStatus("current")
_HwVllStatisticPackets_Type = Counter64
_HwVllStatisticPackets_Object = MibTableColumn
hwVllStatisticPackets = _HwVllStatisticPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 6),
    _HwVllStatisticPackets_Type()
)
hwVllStatisticPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllStatisticPackets.setStatus("current")
_HwVllStatisticBytes_Type = Counter64
_HwVllStatisticBytes_Object = MibTableColumn
hwVllStatisticBytes = _HwVllStatisticBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 7),
    _HwVllStatisticBytes_Type()
)
hwVllStatisticBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllStatisticBytes.setStatus("current")
_HwVllStatisticPacketsRate_Type = Counter64
_HwVllStatisticPacketsRate_Object = MibTableColumn
hwVllStatisticPacketsRate = _HwVllStatisticPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 8),
    _HwVllStatisticPacketsRate_Type()
)
hwVllStatisticPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllStatisticPacketsRate.setStatus("current")
_HwVllStatisticBytesRate_Type = Counter64
_HwVllStatisticBytesRate_Object = MibTableColumn
hwVllStatisticBytesRate = _HwVllStatisticBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 9),
    _HwVllStatisticBytesRate_Type()
)
hwVllStatisticBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllStatisticBytesRate.setStatus("current")
_HwVllQosStatisticTable_Object = MibTable
hwVllQosStatisticTable = _HwVllQosStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hwVllQosStatisticTable.setStatus("current")
_HwVllQosStatisticEntry_Object = MibTableRow
hwVllQosStatisticEntry = _HwVllQosStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1)
)
hwVllQosStatisticEntry.setIndexNames(
    (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticIfIndex"),
    (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPwType"),
    (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticQueueId"),
)
if mibBuilder.loadTexts:
    hwVllQosStatisticEntry.setStatus("current")
_HwVllQosStatisticIfIndex_Type = InterfaceIndex
_HwVllQosStatisticIfIndex_Object = MibTableColumn
hwVllQosStatisticIfIndex = _HwVllQosStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 1),
    _HwVllQosStatisticIfIndex_Type()
)
hwVllQosStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVllQosStatisticIfIndex.setStatus("current")


class _HwVllQosStatisticPwType_Type(Integer32):
    """Custom type hwVllQosStatisticPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HwVllQosStatisticPwType_Type.__name__ = "Integer32"
_HwVllQosStatisticPwType_Object = MibTableColumn
hwVllQosStatisticPwType = _HwVllQosStatisticPwType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 2),
    _HwVllQosStatisticPwType_Type()
)
hwVllQosStatisticPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVllQosStatisticPwType.setStatus("current")


class _HwVllQosStatisticQueueId_Type(Integer32):
    """Custom type hwVllQosStatisticQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwVllQosStatisticQueueId_Type.__name__ = "Integer32"
_HwVllQosStatisticQueueId_Object = MibTableColumn
hwVllQosStatisticQueueId = _HwVllQosStatisticQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 3),
    _HwVllQosStatisticQueueId_Type()
)
hwVllQosStatisticQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVllQosStatisticQueueId.setStatus("current")
_HwVllQosStatisticPassPacket_Type = Counter64
_HwVllQosStatisticPassPacket_Object = MibTableColumn
hwVllQosStatisticPassPacket = _HwVllQosStatisticPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 4),
    _HwVllQosStatisticPassPacket_Type()
)
hwVllQosStatisticPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticPassPacket.setStatus("current")
_HwVllQosStatisticPassByte_Type = Counter64
_HwVllQosStatisticPassByte_Object = MibTableColumn
hwVllQosStatisticPassByte = _HwVllQosStatisticPassByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 5),
    _HwVllQosStatisticPassByte_Type()
)
hwVllQosStatisticPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticPassByte.setStatus("current")
_HwVllQosStatisticDiscardPacket_Type = Counter64
_HwVllQosStatisticDiscardPacket_Object = MibTableColumn
hwVllQosStatisticDiscardPacket = _HwVllQosStatisticDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 6),
    _HwVllQosStatisticDiscardPacket_Type()
)
hwVllQosStatisticDiscardPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticDiscardPacket.setStatus("current")
_HwVllQosStatisticDiscardByte_Type = Counter64
_HwVllQosStatisticDiscardByte_Object = MibTableColumn
hwVllQosStatisticDiscardByte = _HwVllQosStatisticDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 7),
    _HwVllQosStatisticDiscardByte_Type()
)
hwVllQosStatisticDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticDiscardByte.setStatus("current")
_HwVllQosStatisticPassPacketRate_Type = Counter64
_HwVllQosStatisticPassPacketRate_Object = MibTableColumn
hwVllQosStatisticPassPacketRate = _HwVllQosStatisticPassPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 8),
    _HwVllQosStatisticPassPacketRate_Type()
)
hwVllQosStatisticPassPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticPassPacketRate.setStatus("current")
_HwVllQosStatisticPassByteRate_Type = Counter64
_HwVllQosStatisticPassByteRate_Object = MibTableColumn
hwVllQosStatisticPassByteRate = _HwVllQosStatisticPassByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 9),
    _HwVllQosStatisticPassByteRate_Type()
)
hwVllQosStatisticPassByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticPassByteRate.setStatus("current")
_HwVllQosStatisticDiscardPacketRate_Type = Counter64
_HwVllQosStatisticDiscardPacketRate_Object = MibTableColumn
hwVllQosStatisticDiscardPacketRate = _HwVllQosStatisticDiscardPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 10),
    _HwVllQosStatisticDiscardPacketRate_Type()
)
hwVllQosStatisticDiscardPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticDiscardPacketRate.setStatus("current")
_HwVllQosStatisticDiscardByteRate_Type = Counter64
_HwVllQosStatisticDiscardByteRate_Object = MibTableColumn
hwVllQosStatisticDiscardByteRate = _HwVllQosStatisticDiscardByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 11),
    _HwVllQosStatisticDiscardByteRate_Type()
)
hwVllQosStatisticDiscardByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVllQosStatisticDiscardByteRate.setStatus("current")
_HwVllMIBTraps_ObjectIdentity = ObjectIdentity
hwVllMIBTraps = _HwVllMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 2)
)
_HwVllMIBConformance_ObjectIdentity = ObjectIdentity
hwVllMIBConformance = _HwVllMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3)
)
_HwVllMIBCompliances_ObjectIdentity = ObjectIdentity
hwVllMIBCompliances = _HwVllMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1)
)
_HwVllMIBGroups_ObjectIdentity = ObjectIdentity
hwVllMIBGroups = _HwVllMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2)
)

# Managed Objects groups

hwVllStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 1)
)
hwVllStatisticGroup.setObjects(
      *(("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticEnable"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticResetTraffic"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticResetTime"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPackets"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticBytes"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPacketsRate"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticBytesRate"))
)
if mibBuilder.loadTexts:
    hwVllStatisticGroup.setStatus("current")

hwVllQosStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 2)
)
hwVllQosStatisticGroup.setObjects(
      *(("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassPacket"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassByte"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardPacket"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardByte"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassPacketRate"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassByteRate"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardPacketRate"),
        ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardByteRate"))
)
if mibBuilder.loadTexts:
    hwVllQosStatisticGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwVllMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVllMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VLL-STATISTIC-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2VpnVllStatistic": hwL2VpnVllStatistic,
       "hwVllMIBObjects": hwVllMIBObjects,
       "hwVllStatisticTable": hwVllStatisticTable,
       "hwVllStatisticEntry": hwVllStatisticEntry,
       "hwVllStatisticIfIndex": hwVllStatisticIfIndex,
       "hwVllStatisticPwType": hwVllStatisticPwType,
       "hwVllStatisticEnable": hwVllStatisticEnable,
       "hwVllStatisticResetTraffic": hwVllStatisticResetTraffic,
       "hwVllStatisticResetTime": hwVllStatisticResetTime,
       "hwVllStatisticPackets": hwVllStatisticPackets,
       "hwVllStatisticBytes": hwVllStatisticBytes,
       "hwVllStatisticPacketsRate": hwVllStatisticPacketsRate,
       "hwVllStatisticBytesRate": hwVllStatisticBytesRate,
       "hwVllQosStatisticTable": hwVllQosStatisticTable,
       "hwVllQosStatisticEntry": hwVllQosStatisticEntry,
       "hwVllQosStatisticIfIndex": hwVllQosStatisticIfIndex,
       "hwVllQosStatisticPwType": hwVllQosStatisticPwType,
       "hwVllQosStatisticQueueId": hwVllQosStatisticQueueId,
       "hwVllQosStatisticPassPacket": hwVllQosStatisticPassPacket,
       "hwVllQosStatisticPassByte": hwVllQosStatisticPassByte,
       "hwVllQosStatisticDiscardPacket": hwVllQosStatisticDiscardPacket,
       "hwVllQosStatisticDiscardByte": hwVllQosStatisticDiscardByte,
       "hwVllQosStatisticPassPacketRate": hwVllQosStatisticPassPacketRate,
       "hwVllQosStatisticPassByteRate": hwVllQosStatisticPassByteRate,
       "hwVllQosStatisticDiscardPacketRate": hwVllQosStatisticDiscardPacketRate,
       "hwVllQosStatisticDiscardByteRate": hwVllQosStatisticDiscardByteRate,
       "hwVllMIBTraps": hwVllMIBTraps,
       "hwVllMIBConformance": hwVllMIBConformance,
       "hwVllMIBCompliances": hwVllMIBCompliances,
       "hwVllMIBCompliance": hwVllMIBCompliance,
       "hwVllMIBGroups": hwVllMIBGroups,
       "hwVllStatisticGroup": hwVllStatisticGroup,
       "hwVllQosStatisticGroup": hwVllQosStatisticGroup}
)
