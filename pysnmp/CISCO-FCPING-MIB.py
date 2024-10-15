# SNMP MIB module (CISCO-FCPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:25 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddress,
 FcAddressType,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddress",
    "FcAddressType",
    "VsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295)
)
ciscoFcPingMIB.setRevisions(
        ("2002-10-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcStartOper(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcPingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcPingMIBObjects = _CiscoFcPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1)
)
_FcPingConfiguration_ObjectIdentity = ObjectIdentity
fcPingConfiguration = _FcPingConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1)
)
_FcPingTable_Object = MibTable
fcPingTable = _FcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fcPingTable.setStatus("current")
_FcPingEntry_Object = MibTableRow
fcPingEntry = _FcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1)
)
fcPingEntry.setIndexNames(
    (0, "CISCO-FCPING-MIB", "fcPingIndex"),
)
if mibBuilder.loadTexts:
    fcPingEntry.setStatus("current")


class _FcPingIndex_Type(Integer32):
    """Custom type fcPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcPingIndex_Type.__name__ = "Integer32"
_FcPingIndex_Object = MibTableColumn
fcPingIndex = _FcPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 1),
    _FcPingIndex_Type()
)
fcPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcPingIndex.setStatus("current")


class _FcPingVsanIndex_Type(VsanIndex):
    """Custom type fcPingVsanIndex based on VsanIndex"""
    defaultValue = 1


_FcPingVsanIndex_Object = MibTableColumn
fcPingVsanIndex = _FcPingVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 2),
    _FcPingVsanIndex_Type()
)
fcPingVsanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingVsanIndex.setStatus("current")


class _FcPingAddressType_Type(FcAddressType):
    """Custom type fcPingAddressType based on FcAddressType"""


_FcPingAddressType_Object = MibTableColumn
fcPingAddressType = _FcPingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 3),
    _FcPingAddressType_Type()
)
fcPingAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingAddressType.setStatus("current")
_FcPingAddress_Type = FcAddress
_FcPingAddress_Object = MibTableColumn
fcPingAddress = _FcPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 4),
    _FcPingAddress_Type()
)
fcPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingAddress.setStatus("current")


class _FcPingPacketCount_Type(Unsigned32):
    """Custom type fcPingPacketCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcPingPacketCount_Type.__name__ = "Unsigned32"
_FcPingPacketCount_Object = MibTableColumn
fcPingPacketCount = _FcPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 5),
    _FcPingPacketCount_Type()
)
fcPingPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingPacketCount.setStatus("current")


class _FcPingPayloadSize_Type(Unsigned32):
    """Custom type fcPingPayloadSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1884),
    )


_FcPingPayloadSize_Type.__name__ = "Unsigned32"
_FcPingPayloadSize_Object = MibTableColumn
fcPingPayloadSize = _FcPingPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 6),
    _FcPingPayloadSize_Type()
)
fcPingPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingPayloadSize.setStatus("current")


class _FcPingPacketTimeout_Type(Unsigned32):
    """Custom type fcPingPacketTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FcPingPacketTimeout_Type.__name__ = "Unsigned32"
_FcPingPacketTimeout_Object = MibTableColumn
fcPingPacketTimeout = _FcPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 7),
    _FcPingPacketTimeout_Type()
)
fcPingPacketTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingPacketTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fcPingPacketTimeout.setUnits("seconds")


class _FcPingDelay_Type(Unsigned32):
    """Custom type fcPingDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FcPingDelay_Type.__name__ = "Unsigned32"
_FcPingDelay_Object = MibTableColumn
fcPingDelay = _FcPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 8),
    _FcPingDelay_Type()
)
fcPingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    fcPingDelay.setUnits("milliseconds")


class _FcPingAgeInterval_Type(Unsigned32):
    """Custom type fcPingAgeInterval based on Unsigned32"""
    defaultValue = 500000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500000, 900000),
    )


_FcPingAgeInterval_Type.__name__ = "Unsigned32"
_FcPingAgeInterval_Object = MibTableColumn
fcPingAgeInterval = _FcPingAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 9),
    _FcPingAgeInterval_Type()
)
fcPingAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    fcPingAgeInterval.setUnits("milliseconds")


class _FcPingUsrPriority_Type(Integer32):
    """Custom type fcPingUsrPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_FcPingUsrPriority_Type.__name__ = "Integer32"
_FcPingUsrPriority_Object = MibTableColumn
fcPingUsrPriority = _FcPingUsrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 10),
    _FcPingUsrPriority_Type()
)
fcPingUsrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingUsrPriority.setStatus("current")


class _FcPingAdminStatus_Type(FcStartOper):
    """Custom type fcPingAdminStatus based on FcStartOper"""


_FcPingAdminStatus_Object = MibTableColumn
fcPingAdminStatus = _FcPingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 11),
    _FcPingAdminStatus_Type()
)
fcPingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingAdminStatus.setStatus("current")


class _FcPingOperStatus_Type(Integer32):
    """Custom type fcPingOperStatus based on Integer32"""
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
          ("failure", 4),
          ("inProgress", 1))
    )


_FcPingOperStatus_Type.__name__ = "Integer32"
_FcPingOperStatus_Object = MibTableColumn
fcPingOperStatus = _FcPingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 12),
    _FcPingOperStatus_Type()
)
fcPingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingOperStatus.setStatus("current")


class _FcPingTrapOnCompletion_Type(TruthValue):
    """Custom type fcPingTrapOnCompletion based on TruthValue"""


_FcPingTrapOnCompletion_Object = MibTableColumn
fcPingTrapOnCompletion = _FcPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 13),
    _FcPingTrapOnCompletion_Type()
)
fcPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingTrapOnCompletion.setStatus("current")
_FcPingRowStatus_Type = RowStatus
_FcPingRowStatus_Object = MibTableColumn
fcPingRowStatus = _FcPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 1, 1, 1, 14),
    _FcPingRowStatus_Type()
)
fcPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcPingRowStatus.setStatus("current")
_FcPingStats_ObjectIdentity = ObjectIdentity
fcPingStats = _FcPingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2)
)
_FcPingStatsTable_Object = MibTable
fcPingStatsTable = _FcPingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcPingStatsTable.setStatus("current")
_FcPingStatsEntry_Object = MibTableRow
fcPingStatsEntry = _FcPingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1)
)
fcPingStatsEntry.setIndexNames(
    (0, "CISCO-FCPING-MIB", "fcPingIndex"),
)
if mibBuilder.loadTexts:
    fcPingStatsEntry.setStatus("current")
_FcPingTxPackets_Type = Gauge32
_FcPingTxPackets_Object = MibTableColumn
fcPingTxPackets = _FcPingTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 1),
    _FcPingTxPackets_Type()
)
fcPingTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingTxPackets.setStatus("current")
_FcPingRxPackets_Type = Gauge32
_FcPingRxPackets_Object = MibTableColumn
fcPingRxPackets = _FcPingRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 2),
    _FcPingRxPackets_Type()
)
fcPingRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingRxPackets.setStatus("current")


class _FcPingMinRtt_Type(Integer32):
    """Custom type fcPingMinRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FcPingMinRtt_Type.__name__ = "Integer32"
_FcPingMinRtt_Object = MibTableColumn
fcPingMinRtt = _FcPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 3),
    _FcPingMinRtt_Type()
)
fcPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    fcPingMinRtt.setUnits("microseconds")


class _FcPingAvgRtt_Type(Integer32):
    """Custom type fcPingAvgRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FcPingAvgRtt_Type.__name__ = "Integer32"
_FcPingAvgRtt_Object = MibTableColumn
fcPingAvgRtt = _FcPingAvgRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 4),
    _FcPingAvgRtt_Type()
)
fcPingAvgRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingAvgRtt.setStatus("current")
if mibBuilder.loadTexts:
    fcPingAvgRtt.setUnits("microseconds")


class _FcPingMaxRtt_Type(Integer32):
    """Custom type fcPingMaxRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FcPingMaxRtt_Type.__name__ = "Integer32"
_FcPingMaxRtt_Object = MibTableColumn
fcPingMaxRtt = _FcPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 5),
    _FcPingMaxRtt_Type()
)
fcPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    fcPingMaxRtt.setUnits("microseconds")
_FcPingNumTimeouts_Type = Gauge32
_FcPingNumTimeouts_Object = MibTableColumn
fcPingNumTimeouts = _FcPingNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 2, 1, 1, 6),
    _FcPingNumTimeouts_Type()
)
fcPingNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPingNumTimeouts.setStatus("current")
_FcPingNotification_ObjectIdentity = ObjectIdentity
fcPingNotification = _FcPingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 3)
)
_FcPingNotifications_ObjectIdentity = ObjectIdentity
fcPingNotifications = _FcPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 3, 0)
)
_FcPingMIBConformance_ObjectIdentity = ObjectIdentity
fcPingMIBConformance = _FcPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2)
)
_FcPingMIBCompliances_ObjectIdentity = ObjectIdentity
fcPingMIBCompliances = _FcPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 1)
)
_FcPingMIBGroups_ObjectIdentity = ObjectIdentity
fcPingMIBGroups = _FcPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 2)
)

# Managed Objects groups

fcPingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 2, 1)
)
fcPingConfigGroup.setObjects(
      *(("CISCO-FCPING-MIB", "fcPingVsanIndex"),
        ("CISCO-FCPING-MIB", "fcPingAddressType"),
        ("CISCO-FCPING-MIB", "fcPingAddress"),
        ("CISCO-FCPING-MIB", "fcPingPacketCount"),
        ("CISCO-FCPING-MIB", "fcPingPayloadSize"),
        ("CISCO-FCPING-MIB", "fcPingPacketTimeout"),
        ("CISCO-FCPING-MIB", "fcPingDelay"),
        ("CISCO-FCPING-MIB", "fcPingAgeInterval"),
        ("CISCO-FCPING-MIB", "fcPingUsrPriority"),
        ("CISCO-FCPING-MIB", "fcPingAdminStatus"),
        ("CISCO-FCPING-MIB", "fcPingOperStatus"),
        ("CISCO-FCPING-MIB", "fcPingTrapOnCompletion"),
        ("CISCO-FCPING-MIB", "fcPingRowStatus"))
)
if mibBuilder.loadTexts:
    fcPingConfigGroup.setStatus("current")

fcPingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 2, 2)
)
fcPingStatsGroup.setObjects(
      *(("CISCO-FCPING-MIB", "fcPingTxPackets"),
        ("CISCO-FCPING-MIB", "fcPingRxPackets"),
        ("CISCO-FCPING-MIB", "fcPingMinRtt"),
        ("CISCO-FCPING-MIB", "fcPingAvgRtt"),
        ("CISCO-FCPING-MIB", "fcPingMaxRtt"),
        ("CISCO-FCPING-MIB", "fcPingNumTimeouts"))
)
if mibBuilder.loadTexts:
    fcPingStatsGroup.setStatus("current")


# Notification objects

fcPingCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 1, 3, 0, 1)
)
fcPingCompletionNotify.setObjects(
      *(("CISCO-FCPING-MIB", "fcPingAddress"),
        ("CISCO-FCPING-MIB", "fcPingTxPackets"),
        ("CISCO-FCPING-MIB", "fcPingRxPackets"))
)
if mibBuilder.loadTexts:
    fcPingCompletionNotify.setStatus(
        "current"
    )


# Notifications groups

fcPingNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 2, 3)
)
fcPingNotifyGroup.setObjects(
    ("CISCO-FCPING-MIB", "fcPingCompletionNotify")
)
if mibBuilder.loadTexts:
    fcPingNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fcPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 295, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcPingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCPING-MIB",
    **{"FcStartOper": FcStartOper,
       "ciscoFcPingMIB": ciscoFcPingMIB,
       "ciscoFcPingMIBObjects": ciscoFcPingMIBObjects,
       "fcPingConfiguration": fcPingConfiguration,
       "fcPingTable": fcPingTable,
       "fcPingEntry": fcPingEntry,
       "fcPingIndex": fcPingIndex,
       "fcPingVsanIndex": fcPingVsanIndex,
       "fcPingAddressType": fcPingAddressType,
       "fcPingAddress": fcPingAddress,
       "fcPingPacketCount": fcPingPacketCount,
       "fcPingPayloadSize": fcPingPayloadSize,
       "fcPingPacketTimeout": fcPingPacketTimeout,
       "fcPingDelay": fcPingDelay,
       "fcPingAgeInterval": fcPingAgeInterval,
       "fcPingUsrPriority": fcPingUsrPriority,
       "fcPingAdminStatus": fcPingAdminStatus,
       "fcPingOperStatus": fcPingOperStatus,
       "fcPingTrapOnCompletion": fcPingTrapOnCompletion,
       "fcPingRowStatus": fcPingRowStatus,
       "fcPingStats": fcPingStats,
       "fcPingStatsTable": fcPingStatsTable,
       "fcPingStatsEntry": fcPingStatsEntry,
       "fcPingTxPackets": fcPingTxPackets,
       "fcPingRxPackets": fcPingRxPackets,
       "fcPingMinRtt": fcPingMinRtt,
       "fcPingAvgRtt": fcPingAvgRtt,
       "fcPingMaxRtt": fcPingMaxRtt,
       "fcPingNumTimeouts": fcPingNumTimeouts,
       "fcPingNotification": fcPingNotification,
       "fcPingNotifications": fcPingNotifications,
       "fcPingCompletionNotify": fcPingCompletionNotify,
       "fcPingMIBConformance": fcPingMIBConformance,
       "fcPingMIBCompliances": fcPingMIBCompliances,
       "fcPingMIBCompliance": fcPingMIBCompliance,
       "fcPingMIBGroups": fcPingMIBGroups,
       "fcPingConfigGroup": fcPingConfigGroup,
       "fcPingStatsGroup": fcPingStatsGroup,
       "fcPingNotifyGroup": fcPingNotifyGroup}
)
