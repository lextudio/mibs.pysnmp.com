# SNMP MIB module (HH3C-FC-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FC-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:17 2024
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

(Hh3cFcAddress,
 Hh3cFcAddressType,
 Hh3cFcStartOper,
 Hh3cFcVsanIndex) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcAddress",
    "Hh3cFcAddressType",
    "Hh3cFcStartOper",
    "Hh3cFcVsanIndex")

(hh3cSan,) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan")

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

hh3cFcPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5)
)
hh3cFcPing.setRevisions(
        ("2013-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcPingObjects_ObjectIdentity = ObjectIdentity
hh3cFcPingObjects = _Hh3cFcPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1)
)
_Hh3cFcPingConfigurations_ObjectIdentity = ObjectIdentity
hh3cFcPingConfigurations = _Hh3cFcPingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1)
)
_Hh3cFcPingTable_Object = MibTable
hh3cFcPingTable = _Hh3cFcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFcPingTable.setStatus("current")
_Hh3cFcPingEntry_Object = MibTableRow
hh3cFcPingEntry = _Hh3cFcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1)
)
hh3cFcPingEntry.setIndexNames(
    (0, "HH3C-FC-PING-MIB", "hh3cFcPingIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPingEntry.setStatus("current")


class _Hh3cFcPingIndex_Type(Unsigned32):
    """Custom type hh3cFcPingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cFcPingIndex_Type.__name__ = "Unsigned32"
_Hh3cFcPingIndex_Object = MibTableColumn
hh3cFcPingIndex = _Hh3cFcPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 1),
    _Hh3cFcPingIndex_Type()
)
hh3cFcPingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcPingIndex.setStatus("current")
_Hh3cFcPingVsan_Type = Hh3cFcVsanIndex
_Hh3cFcPingVsan_Object = MibTableColumn
hh3cFcPingVsan = _Hh3cFcPingVsan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 2),
    _Hh3cFcPingVsan_Type()
)
hh3cFcPingVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingVsan.setStatus("current")


class _Hh3cFcPingAddressType_Type(Hh3cFcAddressType):
    """Custom type hh3cFcPingAddressType based on Hh3cFcAddressType"""


_Hh3cFcPingAddressType_Object = MibTableColumn
hh3cFcPingAddressType = _Hh3cFcPingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 3),
    _Hh3cFcPingAddressType_Type()
)
hh3cFcPingAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingAddressType.setStatus("current")
_Hh3cFcPingAddress_Type = Hh3cFcAddress
_Hh3cFcPingAddress_Object = MibTableColumn
hh3cFcPingAddress = _Hh3cFcPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 4),
    _Hh3cFcPingAddress_Type()
)
hh3cFcPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingAddress.setStatus("current")


class _Hh3cFcPingPacketCount_Type(Unsigned32):
    """Custom type hh3cFcPingPacketCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cFcPingPacketCount_Type.__name__ = "Unsigned32"
_Hh3cFcPingPacketCount_Object = MibTableColumn
hh3cFcPingPacketCount = _Hh3cFcPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 5),
    _Hh3cFcPingPacketCount_Type()
)
hh3cFcPingPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingPacketCount.setStatus("current")
_Hh3cFcPingPayloadSize_Type = Unsigned32
_Hh3cFcPingPayloadSize_Object = MibTableColumn
hh3cFcPingPayloadSize = _Hh3cFcPingPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 6),
    _Hh3cFcPingPayloadSize_Type()
)
hh3cFcPingPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingPayloadSize.setStatus("current")


class _Hh3cFcPingTimeout_Type(Unsigned32):
    """Custom type hh3cFcPingTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cFcPingTimeout_Type.__name__ = "Unsigned32"
_Hh3cFcPingTimeout_Object = MibTableColumn
hh3cFcPingTimeout = _Hh3cFcPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 7),
    _Hh3cFcPingTimeout_Type()
)
hh3cFcPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingTimeout.setUnits("seconds")
_Hh3cFcPingDelay_Type = Unsigned32
_Hh3cFcPingDelay_Object = MibTableColumn
hh3cFcPingDelay = _Hh3cFcPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 8),
    _Hh3cFcPingDelay_Type()
)
hh3cFcPingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingDelay.setUnits("seconds")


class _Hh3cFcPingAgeInterval_Type(Unsigned32):
    """Custom type hh3cFcPingAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_Hh3cFcPingAgeInterval_Type.__name__ = "Unsigned32"
_Hh3cFcPingAgeInterval_Object = MibTableColumn
hh3cFcPingAgeInterval = _Hh3cFcPingAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 9),
    _Hh3cFcPingAgeInterval_Type()
)
hh3cFcPingAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingAgeInterval.setUnits("seconds")


class _Hh3cFcPingAdminStatus_Type(Hh3cFcStartOper):
    """Custom type hh3cFcPingAdminStatus based on Hh3cFcStartOper"""


_Hh3cFcPingAdminStatus_Object = MibTableColumn
hh3cFcPingAdminStatus = _Hh3cFcPingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 10),
    _Hh3cFcPingAdminStatus_Type()
)
hh3cFcPingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingAdminStatus.setStatus("current")


class _Hh3cFcPingOperStatus_Type(Integer32):
    """Custom type hh3cFcPingOperStatus based on Integer32"""
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


_Hh3cFcPingOperStatus_Type.__name__ = "Integer32"
_Hh3cFcPingOperStatus_Object = MibTableColumn
hh3cFcPingOperStatus = _Hh3cFcPingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 11),
    _Hh3cFcPingOperStatus_Type()
)
hh3cFcPingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingOperStatus.setStatus("current")


class _Hh3cFcPingTrapOnCompletion_Type(TruthValue):
    """Custom type hh3cFcPingTrapOnCompletion based on TruthValue"""


_Hh3cFcPingTrapOnCompletion_Object = MibTableColumn
hh3cFcPingTrapOnCompletion = _Hh3cFcPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 12),
    _Hh3cFcPingTrapOnCompletion_Type()
)
hh3cFcPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingTrapOnCompletion.setStatus("current")
_Hh3cFcPingRowStatus_Type = RowStatus
_Hh3cFcPingRowStatus_Object = MibTableColumn
hh3cFcPingRowStatus = _Hh3cFcPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 13),
    _Hh3cFcPingRowStatus_Type()
)
hh3cFcPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPingRowStatus.setStatus("current")
_Hh3cFcPingStatistics_ObjectIdentity = ObjectIdentity
hh3cFcPingStatistics = _Hh3cFcPingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2)
)
_Hh3cFcPingStatTable_Object = MibTable
hh3cFcPingStatTable = _Hh3cFcPingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFcPingStatTable.setStatus("current")
_Hh3cFcPingStatEntry_Object = MibTableRow
hh3cFcPingStatEntry = _Hh3cFcPingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1)
)
hh3cFcPingStatEntry.setIndexNames(
    (0, "HH3C-FC-PING-MIB", "hh3cFcPingIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPingStatEntry.setStatus("current")
_Hh3cFcPingReqPackets_Type = Unsigned32
_Hh3cFcPingReqPackets_Object = MibTableColumn
hh3cFcPingReqPackets = _Hh3cFcPingReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 1),
    _Hh3cFcPingReqPackets_Type()
)
hh3cFcPingReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingReqPackets.setStatus("current")
_Hh3cFcPingResPackets_Type = Unsigned32
_Hh3cFcPingResPackets_Object = MibTableColumn
hh3cFcPingResPackets = _Hh3cFcPingResPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 2),
    _Hh3cFcPingResPackets_Type()
)
hh3cFcPingResPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingResPackets.setStatus("current")
_Hh3cFcPingMinTime_Type = Integer32
_Hh3cFcPingMinTime_Object = MibTableColumn
hh3cFcPingMinTime = _Hh3cFcPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 3),
    _Hh3cFcPingMinTime_Type()
)
hh3cFcPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingMinTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingMinTime.setUnits("microseconds")
_Hh3cFcPingAverageTime_Type = Integer32
_Hh3cFcPingAverageTime_Object = MibTableColumn
hh3cFcPingAverageTime = _Hh3cFcPingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 4),
    _Hh3cFcPingAverageTime_Type()
)
hh3cFcPingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingAverageTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingAverageTime.setUnits("microseconds")
_Hh3cFcPingMaxTime_Type = Integer32
_Hh3cFcPingMaxTime_Object = MibTableColumn
hh3cFcPingMaxTime = _Hh3cFcPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 5),
    _Hh3cFcPingMaxTime_Type()
)
hh3cFcPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcPingMaxTime.setUnits("microseconds")
_Hh3cFcPingTimeoutNum_Type = Unsigned32
_Hh3cFcPingTimeoutNum_Object = MibTableColumn
hh3cFcPingTimeoutNum = _Hh3cFcPingTimeoutNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 6),
    _Hh3cFcPingTimeoutNum_Type()
)
hh3cFcPingTimeoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPingTimeoutNum.setStatus("current")
_Hh3cFcPingNotifications_ObjectIdentity = ObjectIdentity
hh3cFcPingNotifications = _Hh3cFcPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3)
)
_Hh3cFcPingNotifyPrefix_ObjectIdentity = ObjectIdentity
hh3cFcPingNotifyPrefix = _Hh3cFcPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cFcPingCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3, 0, 1)
)
hh3cFcPingCompletionNotify.setObjects(
      *(("HH3C-FC-PING-MIB", "hh3cFcPingIndex"),
        ("HH3C-FC-PING-MIB", "hh3cFcPingVsan"),
        ("HH3C-FC-PING-MIB", "hh3cFcPingAddressType"),
        ("HH3C-FC-PING-MIB", "hh3cFcPingAddress"),
        ("HH3C-FC-PING-MIB", "hh3cFcPingReqPackets"),
        ("HH3C-FC-PING-MIB", "hh3cFcPingResPackets"))
)
if mibBuilder.loadTexts:
    hh3cFcPingCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-PING-MIB",
    **{"hh3cFcPing": hh3cFcPing,
       "hh3cFcPingObjects": hh3cFcPingObjects,
       "hh3cFcPingConfigurations": hh3cFcPingConfigurations,
       "hh3cFcPingTable": hh3cFcPingTable,
       "hh3cFcPingEntry": hh3cFcPingEntry,
       "hh3cFcPingIndex": hh3cFcPingIndex,
       "hh3cFcPingVsan": hh3cFcPingVsan,
       "hh3cFcPingAddressType": hh3cFcPingAddressType,
       "hh3cFcPingAddress": hh3cFcPingAddress,
       "hh3cFcPingPacketCount": hh3cFcPingPacketCount,
       "hh3cFcPingPayloadSize": hh3cFcPingPayloadSize,
       "hh3cFcPingTimeout": hh3cFcPingTimeout,
       "hh3cFcPingDelay": hh3cFcPingDelay,
       "hh3cFcPingAgeInterval": hh3cFcPingAgeInterval,
       "hh3cFcPingAdminStatus": hh3cFcPingAdminStatus,
       "hh3cFcPingOperStatus": hh3cFcPingOperStatus,
       "hh3cFcPingTrapOnCompletion": hh3cFcPingTrapOnCompletion,
       "hh3cFcPingRowStatus": hh3cFcPingRowStatus,
       "hh3cFcPingStatistics": hh3cFcPingStatistics,
       "hh3cFcPingStatTable": hh3cFcPingStatTable,
       "hh3cFcPingStatEntry": hh3cFcPingStatEntry,
       "hh3cFcPingReqPackets": hh3cFcPingReqPackets,
       "hh3cFcPingResPackets": hh3cFcPingResPackets,
       "hh3cFcPingMinTime": hh3cFcPingMinTime,
       "hh3cFcPingAverageTime": hh3cFcPingAverageTime,
       "hh3cFcPingMaxTime": hh3cFcPingMaxTime,
       "hh3cFcPingTimeoutNum": hh3cFcPingTimeoutNum,
       "hh3cFcPingNotifications": hh3cFcPingNotifications,
       "hh3cFcPingNotifyPrefix": hh3cFcPingNotifyPrefix,
       "hh3cFcPingCompletionNotify": hh3cFcPingCompletionNotify}
)
