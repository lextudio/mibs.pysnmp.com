# SNMP MIB module (HPN-ICF-FC-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:17 2024
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

(HpnicfFcAddress,
 HpnicfFcAddressType,
 HpnicfFcStartOper,
 HpnicfFcVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcAddress",
    "HpnicfFcAddressType",
    "HpnicfFcStartOper",
    "HpnicfFcVsanIndex")

(hpnicfSan,) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfFcPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5)
)
hpnicfFcPing.setRevisions(
        ("2013-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFcPingObjects_ObjectIdentity = ObjectIdentity
hpnicfFcPingObjects = _HpnicfFcPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1)
)
_HpnicfFcPingConfigurations_ObjectIdentity = ObjectIdentity
hpnicfFcPingConfigurations = _HpnicfFcPingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1)
)
_HpnicfFcPingTable_Object = MibTable
hpnicfFcPingTable = _HpnicfFcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcPingTable.setStatus("current")
_HpnicfFcPingEntry_Object = MibTableRow
hpnicfFcPingEntry = _HpnicfFcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1)
)
hpnicfFcPingEntry.setIndexNames(
    (0, "HPN-ICF-FC-PING-MIB", "hpnicfFcPingIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPingEntry.setStatus("current")


class _HpnicfFcPingIndex_Type(Unsigned32):
    """Custom type hpnicfFcPingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfFcPingIndex_Type.__name__ = "Unsigned32"
_HpnicfFcPingIndex_Object = MibTableColumn
hpnicfFcPingIndex = _HpnicfFcPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 1),
    _HpnicfFcPingIndex_Type()
)
hpnicfFcPingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcPingIndex.setStatus("current")
_HpnicfFcPingVsan_Type = HpnicfFcVsanIndex
_HpnicfFcPingVsan_Object = MibTableColumn
hpnicfFcPingVsan = _HpnicfFcPingVsan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 2),
    _HpnicfFcPingVsan_Type()
)
hpnicfFcPingVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingVsan.setStatus("current")


class _HpnicfFcPingAddressType_Type(HpnicfFcAddressType):
    """Custom type hpnicfFcPingAddressType based on HpnicfFcAddressType"""


_HpnicfFcPingAddressType_Object = MibTableColumn
hpnicfFcPingAddressType = _HpnicfFcPingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 3),
    _HpnicfFcPingAddressType_Type()
)
hpnicfFcPingAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingAddressType.setStatus("current")
_HpnicfFcPingAddress_Type = HpnicfFcAddress
_HpnicfFcPingAddress_Object = MibTableColumn
hpnicfFcPingAddress = _HpnicfFcPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 4),
    _HpnicfFcPingAddress_Type()
)
hpnicfFcPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingAddress.setStatus("current")


class _HpnicfFcPingPacketCount_Type(Unsigned32):
    """Custom type hpnicfFcPingPacketCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfFcPingPacketCount_Type.__name__ = "Unsigned32"
_HpnicfFcPingPacketCount_Object = MibTableColumn
hpnicfFcPingPacketCount = _HpnicfFcPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 5),
    _HpnicfFcPingPacketCount_Type()
)
hpnicfFcPingPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingPacketCount.setStatus("current")
_HpnicfFcPingPayloadSize_Type = Unsigned32
_HpnicfFcPingPayloadSize_Object = MibTableColumn
hpnicfFcPingPayloadSize = _HpnicfFcPingPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 6),
    _HpnicfFcPingPayloadSize_Type()
)
hpnicfFcPingPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingPayloadSize.setStatus("current")


class _HpnicfFcPingTimeout_Type(Unsigned32):
    """Custom type hpnicfFcPingTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfFcPingTimeout_Type.__name__ = "Unsigned32"
_HpnicfFcPingTimeout_Object = MibTableColumn
hpnicfFcPingTimeout = _HpnicfFcPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 7),
    _HpnicfFcPingTimeout_Type()
)
hpnicfFcPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingTimeout.setUnits("seconds")
_HpnicfFcPingDelay_Type = Unsigned32
_HpnicfFcPingDelay_Object = MibTableColumn
hpnicfFcPingDelay = _HpnicfFcPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 8),
    _HpnicfFcPingDelay_Type()
)
hpnicfFcPingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingDelay.setUnits("seconds")


class _HpnicfFcPingAgeInterval_Type(Unsigned32):
    """Custom type hpnicfFcPingAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_HpnicfFcPingAgeInterval_Type.__name__ = "Unsigned32"
_HpnicfFcPingAgeInterval_Object = MibTableColumn
hpnicfFcPingAgeInterval = _HpnicfFcPingAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 9),
    _HpnicfFcPingAgeInterval_Type()
)
hpnicfFcPingAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingAgeInterval.setUnits("seconds")


class _HpnicfFcPingAdminStatus_Type(HpnicfFcStartOper):
    """Custom type hpnicfFcPingAdminStatus based on HpnicfFcStartOper"""


_HpnicfFcPingAdminStatus_Object = MibTableColumn
hpnicfFcPingAdminStatus = _HpnicfFcPingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 10),
    _HpnicfFcPingAdminStatus_Type()
)
hpnicfFcPingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingAdminStatus.setStatus("current")


class _HpnicfFcPingOperStatus_Type(Integer32):
    """Custom type hpnicfFcPingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("disabled", 3),
          ("failed", 4),
          ("inProgress", 1))
    )


_HpnicfFcPingOperStatus_Type.__name__ = "Integer32"
_HpnicfFcPingOperStatus_Object = MibTableColumn
hpnicfFcPingOperStatus = _HpnicfFcPingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 11),
    _HpnicfFcPingOperStatus_Type()
)
hpnicfFcPingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingOperStatus.setStatus("current")


class _HpnicfFcPingTrapOnCompletion_Type(TruthValue):
    """Custom type hpnicfFcPingTrapOnCompletion based on TruthValue"""


_HpnicfFcPingTrapOnCompletion_Object = MibTableColumn
hpnicfFcPingTrapOnCompletion = _HpnicfFcPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 12),
    _HpnicfFcPingTrapOnCompletion_Type()
)
hpnicfFcPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingTrapOnCompletion.setStatus("current")
_HpnicfFcPingRowStatus_Type = RowStatus
_HpnicfFcPingRowStatus_Object = MibTableColumn
hpnicfFcPingRowStatus = _HpnicfFcPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 1, 1, 1, 13),
    _HpnicfFcPingRowStatus_Type()
)
hpnicfFcPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPingRowStatus.setStatus("current")
_HpnicfFcPingStatistics_ObjectIdentity = ObjectIdentity
hpnicfFcPingStatistics = _HpnicfFcPingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2)
)
_HpnicfFcPingStatTable_Object = MibTable
hpnicfFcPingStatTable = _HpnicfFcPingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcPingStatTable.setStatus("current")
_HpnicfFcPingStatEntry_Object = MibTableRow
hpnicfFcPingStatEntry = _HpnicfFcPingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1)
)
hpnicfFcPingStatEntry.setIndexNames(
    (0, "HPN-ICF-FC-PING-MIB", "hpnicfFcPingIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPingStatEntry.setStatus("current")
_HpnicfFcPingReqPackets_Type = Unsigned32
_HpnicfFcPingReqPackets_Object = MibTableColumn
hpnicfFcPingReqPackets = _HpnicfFcPingReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 1),
    _HpnicfFcPingReqPackets_Type()
)
hpnicfFcPingReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingReqPackets.setStatus("current")
_HpnicfFcPingResPackets_Type = Unsigned32
_HpnicfFcPingResPackets_Object = MibTableColumn
hpnicfFcPingResPackets = _HpnicfFcPingResPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 2),
    _HpnicfFcPingResPackets_Type()
)
hpnicfFcPingResPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingResPackets.setStatus("current")
_HpnicfFcPingMinTime_Type = Integer32
_HpnicfFcPingMinTime_Object = MibTableColumn
hpnicfFcPingMinTime = _HpnicfFcPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 3),
    _HpnicfFcPingMinTime_Type()
)
hpnicfFcPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingMinTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingMinTime.setUnits("microseconds")
_HpnicfFcPingAverageTime_Type = Integer32
_HpnicfFcPingAverageTime_Object = MibTableColumn
hpnicfFcPingAverageTime = _HpnicfFcPingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 4),
    _HpnicfFcPingAverageTime_Type()
)
hpnicfFcPingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingAverageTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingAverageTime.setUnits("microseconds")
_HpnicfFcPingMaxTime_Type = Integer32
_HpnicfFcPingMaxTime_Object = MibTableColumn
hpnicfFcPingMaxTime = _HpnicfFcPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 5),
    _HpnicfFcPingMaxTime_Type()
)
hpnicfFcPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcPingMaxTime.setUnits("microseconds")
_HpnicfFcPingTimeoutNum_Type = Unsigned32
_HpnicfFcPingTimeoutNum_Object = MibTableColumn
hpnicfFcPingTimeoutNum = _HpnicfFcPingTimeoutNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 2, 1, 1, 6),
    _HpnicfFcPingTimeoutNum_Type()
)
hpnicfFcPingTimeoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPingTimeoutNum.setStatus("current")
_HpnicfFcPingNotifications_ObjectIdentity = ObjectIdentity
hpnicfFcPingNotifications = _HpnicfFcPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 3)
)
_HpnicfFcPingNotifyPrefix_ObjectIdentity = ObjectIdentity
hpnicfFcPingNotifyPrefix = _HpnicfFcPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfFcPingCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 5, 1, 3, 0, 1)
)
hpnicfFcPingCompletionNotify.setObjects(
      *(("HPN-ICF-FC-PING-MIB", "hpnicfFcPingIndex"),
        ("HPN-ICF-FC-PING-MIB", "hpnicfFcPingVsan"),
        ("HPN-ICF-FC-PING-MIB", "hpnicfFcPingAddressType"),
        ("HPN-ICF-FC-PING-MIB", "hpnicfFcPingAddress"),
        ("HPN-ICF-FC-PING-MIB", "hpnicfFcPingReqPackets"),
        ("HPN-ICF-FC-PING-MIB", "hpnicfFcPingResPackets"))
)
if mibBuilder.loadTexts:
    hpnicfFcPingCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-PING-MIB",
    **{"hpnicfFcPing": hpnicfFcPing,
       "hpnicfFcPingObjects": hpnicfFcPingObjects,
       "hpnicfFcPingConfigurations": hpnicfFcPingConfigurations,
       "hpnicfFcPingTable": hpnicfFcPingTable,
       "hpnicfFcPingEntry": hpnicfFcPingEntry,
       "hpnicfFcPingIndex": hpnicfFcPingIndex,
       "hpnicfFcPingVsan": hpnicfFcPingVsan,
       "hpnicfFcPingAddressType": hpnicfFcPingAddressType,
       "hpnicfFcPingAddress": hpnicfFcPingAddress,
       "hpnicfFcPingPacketCount": hpnicfFcPingPacketCount,
       "hpnicfFcPingPayloadSize": hpnicfFcPingPayloadSize,
       "hpnicfFcPingTimeout": hpnicfFcPingTimeout,
       "hpnicfFcPingDelay": hpnicfFcPingDelay,
       "hpnicfFcPingAgeInterval": hpnicfFcPingAgeInterval,
       "hpnicfFcPingAdminStatus": hpnicfFcPingAdminStatus,
       "hpnicfFcPingOperStatus": hpnicfFcPingOperStatus,
       "hpnicfFcPingTrapOnCompletion": hpnicfFcPingTrapOnCompletion,
       "hpnicfFcPingRowStatus": hpnicfFcPingRowStatus,
       "hpnicfFcPingStatistics": hpnicfFcPingStatistics,
       "hpnicfFcPingStatTable": hpnicfFcPingStatTable,
       "hpnicfFcPingStatEntry": hpnicfFcPingStatEntry,
       "hpnicfFcPingReqPackets": hpnicfFcPingReqPackets,
       "hpnicfFcPingResPackets": hpnicfFcPingResPackets,
       "hpnicfFcPingMinTime": hpnicfFcPingMinTime,
       "hpnicfFcPingAverageTime": hpnicfFcPingAverageTime,
       "hpnicfFcPingMaxTime": hpnicfFcPingMaxTime,
       "hpnicfFcPingTimeoutNum": hpnicfFcPingTimeoutNum,
       "hpnicfFcPingNotifications": hpnicfFcPingNotifications,
       "hpnicfFcPingNotifyPrefix": hpnicfFcPingNotifyPrefix,
       "hpnicfFcPingCompletionNotify": hpnicfFcPingCompletionNotify}
)
