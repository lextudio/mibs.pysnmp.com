# SNMP MIB module (IEEE8021-TPMR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-TPMR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:45 2024
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

(ieee8021BridgeBasePortComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePortComponentId")

(IEEE8021BridgePortNumber,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "ieee802dot1mibs")

(ifCounterDiscontinuityGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifCounterDiscontinuityGroup")

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
 MacAddress,
 StorageType,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ieee8021TpmrMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14)
)
ieee8021TpmrMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2009-09-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021TpmrFrameDiscardErrorReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("txSduSizeExceeded", 1)
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021TpmrNotifications_ObjectIdentity = ObjectIdentity
ieee8021TpmrNotifications = _Ieee8021TpmrNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14, 0)
)
_Ieee8021TpmrObjects_ObjectIdentity = ObjectIdentity
ieee8021TpmrObjects = _Ieee8021TpmrObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14, 1)
)
_Ieee8021TpmrPortTable_Object = MibTable
ieee8021TpmrPortTable = _Ieee8021TpmrPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortTable.setStatus("current")
_Ieee8021TpmrPortEntry_Object = MibTableRow
ieee8021TpmrPortEntry = _Ieee8021TpmrPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1)
)
ieee8021TpmrPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortEntry.setStatus("current")


class _Ieee8021TpmrPortNumber_Type(IEEE8021BridgePortNumber):
    """Custom type ieee8021TpmrPortNumber based on IEEE8021BridgePortNumber"""
    subtypeSpec = IEEE8021BridgePortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ieee8021TpmrPortNumber_Type.__name__ = "IEEE8021BridgePortNumber"
_Ieee8021TpmrPortNumber_Object = MibTableColumn
ieee8021TpmrPortNumber = _Ieee8021TpmrPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 1),
    _Ieee8021TpmrPortNumber_Type()
)
ieee8021TpmrPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TpmrPortNumber.setStatus("current")
_Ieee8021TpmrPortMgmtAddr_Type = TruthValue
_Ieee8021TpmrPortMgmtAddr_Object = MibTableColumn
ieee8021TpmrPortMgmtAddr = _Ieee8021TpmrPortMgmtAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 2),
    _Ieee8021TpmrPortMgmtAddr_Type()
)
ieee8021TpmrPortMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortMgmtAddr.setStatus("current")
_Ieee8021TpmrPortMgmtAddrForwarding_Type = TruthValue
_Ieee8021TpmrPortMgmtAddrForwarding_Object = MibTableColumn
ieee8021TpmrPortMgmtAddrForwarding = _Ieee8021TpmrPortMgmtAddrForwarding_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 3),
    _Ieee8021TpmrPortMgmtAddrForwarding_Type()
)
ieee8021TpmrPortMgmtAddrForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortMgmtAddrForwarding.setStatus("current")
_Ieee8021TpmrPortStatsTable_Object = MibTable
ieee8021TpmrPortStatsTable = _Ieee8021TpmrPortStatsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsTable.setStatus("current")
_Ieee8021TpmrPortStatsEntry_Object = MibTableRow
ieee8021TpmrPortStatsEntry = _Ieee8021TpmrPortStatsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsEntry.setStatus("current")
_Ieee8021TpmrPortStatsRxFrames_Type = Counter64
_Ieee8021TpmrPortStatsRxFrames_Object = MibTableColumn
ieee8021TpmrPortStatsRxFrames = _Ieee8021TpmrPortStatsRxFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 1),
    _Ieee8021TpmrPortStatsRxFrames_Type()
)
ieee8021TpmrPortStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsRxFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsRxFrames.setUnits("frames")
_Ieee8021TpmrPortStatsRxOctets_Type = Counter64
_Ieee8021TpmrPortStatsRxOctets_Object = MibTableColumn
ieee8021TpmrPortStatsRxOctets = _Ieee8021TpmrPortStatsRxOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 2),
    _Ieee8021TpmrPortStatsRxOctets_Type()
)
ieee8021TpmrPortStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsRxOctets.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsRxOctets.setUnits("octets")
_Ieee8021TpmrPortStatsFramesForwarded_Type = Counter64
_Ieee8021TpmrPortStatsFramesForwarded_Object = MibTableColumn
ieee8021TpmrPortStatsFramesForwarded = _Ieee8021TpmrPortStatsFramesForwarded_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 3),
    _Ieee8021TpmrPortStatsFramesForwarded_Type()
)
ieee8021TpmrPortStatsFramesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesForwarded.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesForwarded.setUnits("frames")
_Ieee8021TpmrPortStatsFramesDiscarded_Type = Counter64
_Ieee8021TpmrPortStatsFramesDiscarded_Object = MibTableColumn
ieee8021TpmrPortStatsFramesDiscarded = _Ieee8021TpmrPortStatsFramesDiscarded_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 4),
    _Ieee8021TpmrPortStatsFramesDiscarded_Type()
)
ieee8021TpmrPortStatsFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscarded.setUnits("frames")
_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Type = Counter64
_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Object = MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedQueueFull = _Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 5),
    _Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Type()
)
ieee8021TpmrPortStatsFramesDiscardedQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedQueueFull.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedQueueFull.setUnits("frames")
_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Type = Counter64
_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Object = MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedLifetime = _Ieee8021TpmrPortStatsFramesDiscardedLifetime_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 6),
    _Ieee8021TpmrPortStatsFramesDiscardedLifetime_Type()
)
ieee8021TpmrPortStatsFramesDiscardedLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedLifetime.setUnits("frames")
_Ieee8021TpmrPortStatsFramesDiscardedError_Type = Counter64
_Ieee8021TpmrPortStatsFramesDiscardedError_Object = MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedError = _Ieee8021TpmrPortStatsFramesDiscardedError_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 7),
    _Ieee8021TpmrPortStatsFramesDiscardedError_Type()
)
ieee8021TpmrPortStatsFramesDiscardedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedError.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsFramesDiscardedError.setUnits("frames")
_Ieee8021TpmrPortDiscardDetailsTable_Object = MibTable
ieee8021TpmrPortDiscardDetailsTable = _Ieee8021TpmrPortDiscardDetailsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsTable.setStatus("current")
_Ieee8021TpmrPortDiscardDetailsEntry_Object = MibTableRow
ieee8021TpmrPortDiscardDetailsEntry = _Ieee8021TpmrPortDiscardDetailsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1)
)
ieee8021TpmrPortDiscardDetailsEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortNumber"),
    (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsEntry.setStatus("current")


class _Ieee8021TpmrPortDiscardDetailsIndex_Type(Unsigned32):
    """Custom type ieee8021TpmrPortDiscardDetailsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ieee8021TpmrPortDiscardDetailsIndex_Type.__name__ = "Unsigned32"
_Ieee8021TpmrPortDiscardDetailsIndex_Object = MibTableColumn
ieee8021TpmrPortDiscardDetailsIndex = _Ieee8021TpmrPortDiscardDetailsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 1),
    _Ieee8021TpmrPortDiscardDetailsIndex_Type()
)
ieee8021TpmrPortDiscardDetailsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsIndex.setStatus("current")
_Ieee8021TpmrPortDiscardDetailsSource_Type = MacAddress
_Ieee8021TpmrPortDiscardDetailsSource_Object = MibTableColumn
ieee8021TpmrPortDiscardDetailsSource = _Ieee8021TpmrPortDiscardDetailsSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 2),
    _Ieee8021TpmrPortDiscardDetailsSource_Type()
)
ieee8021TpmrPortDiscardDetailsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsSource.setStatus("current")
_Ieee8021TpmrPortDiscardDetailsReason_Type = IEEE8021TpmrFrameDiscardErrorReason
_Ieee8021TpmrPortDiscardDetailsReason_Object = MibTableColumn
ieee8021TpmrPortDiscardDetailsReason = _Ieee8021TpmrPortDiscardDetailsReason_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 3),
    _Ieee8021TpmrPortDiscardDetailsReason_Type()
)
ieee8021TpmrPortDiscardDetailsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsReason.setStatus("current")
_Ieee8021TpmrMspTable_Object = MibTable
ieee8021TpmrMspTable = _Ieee8021TpmrMspTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspTable.setStatus("current")
_Ieee8021TpmrMspEntry_Object = MibTableRow
ieee8021TpmrMspEntry = _Ieee8021TpmrMspEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspEntry.setStatus("current")


class _Ieee8021TpmrMspLinkNotify_Type(TruthValue):
    """Custom type ieee8021TpmrMspLinkNotify based on TruthValue"""


_Ieee8021TpmrMspLinkNotify_Object = MibTableColumn
ieee8021TpmrMspLinkNotify = _Ieee8021TpmrMspLinkNotify_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 1),
    _Ieee8021TpmrMspLinkNotify_Type()
)
ieee8021TpmrMspLinkNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspLinkNotify.setStatus("current")


class _Ieee8021TpmrMspLinkNotifyWait_Type(TimeInterval):
    """Custom type ieee8021TpmrMspLinkNotifyWait based on TimeInterval"""
    defaultValue = 40

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Ieee8021TpmrMspLinkNotifyWait_Type.__name__ = "TimeInterval"
_Ieee8021TpmrMspLinkNotifyWait_Object = MibTableColumn
ieee8021TpmrMspLinkNotifyWait = _Ieee8021TpmrMspLinkNotifyWait_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 2),
    _Ieee8021TpmrMspLinkNotifyWait_Type()
)
ieee8021TpmrMspLinkNotifyWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspLinkNotifyWait.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspLinkNotifyWait.setUnits("centiseconds")


class _Ieee8021TpmrMspLinkNotifyRetry_Type(TimeInterval):
    """Custom type ieee8021TpmrMspLinkNotifyRetry based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Ieee8021TpmrMspLinkNotifyRetry_Type.__name__ = "TimeInterval"
_Ieee8021TpmrMspLinkNotifyRetry_Object = MibTableColumn
ieee8021TpmrMspLinkNotifyRetry = _Ieee8021TpmrMspLinkNotifyRetry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 3),
    _Ieee8021TpmrMspLinkNotifyRetry_Type()
)
ieee8021TpmrMspLinkNotifyRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspLinkNotifyRetry.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspLinkNotifyRetry.setUnits("centiseconds")


class _Ieee8021TpmrMspMacNotify_Type(TruthValue):
    """Custom type ieee8021TpmrMspMacNotify based on TruthValue"""


_Ieee8021TpmrMspMacNotify_Object = MibTableColumn
ieee8021TpmrMspMacNotify = _Ieee8021TpmrMspMacNotify_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 4),
    _Ieee8021TpmrMspMacNotify_Type()
)
ieee8021TpmrMspMacNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspMacNotify.setStatus("current")


class _Ieee8021TpmrMspMacNotifyTime_Type(TimeInterval):
    """Custom type ieee8021TpmrMspMacNotifyTime based on TimeInterval"""
    defaultValue = 20

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ieee8021TpmrMspMacNotifyTime_Type.__name__ = "TimeInterval"
_Ieee8021TpmrMspMacNotifyTime_Object = MibTableColumn
ieee8021TpmrMspMacNotifyTime = _Ieee8021TpmrMspMacNotifyTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 5),
    _Ieee8021TpmrMspMacNotifyTime_Type()
)
ieee8021TpmrMspMacNotifyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspMacNotifyTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspMacNotifyTime.setUnits("centiseconds")


class _Ieee8021TpmrMspMacRecoverTime_Type(TimeInterval):
    """Custom type ieee8021TpmrMspMacRecoverTime based on TimeInterval"""
    defaultValue = 10

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_Ieee8021TpmrMspMacRecoverTime_Type.__name__ = "TimeInterval"
_Ieee8021TpmrMspMacRecoverTime_Object = MibTableColumn
ieee8021TpmrMspMacRecoverTime = _Ieee8021TpmrMspMacRecoverTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 6),
    _Ieee8021TpmrMspMacRecoverTime_Type()
)
ieee8021TpmrMspMacRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspMacRecoverTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspMacRecoverTime.setUnits("centiseconds")


class _Ieee8021TpmrMspStorageType_Type(StorageType):
    """Custom type ieee8021TpmrMspStorageType based on StorageType"""


_Ieee8021TpmrMspStorageType_Object = MibTableColumn
ieee8021TpmrMspStorageType = _Ieee8021TpmrMspStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 7),
    _Ieee8021TpmrMspStorageType_Type()
)
ieee8021TpmrMspStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStorageType.setStatus("current")
_Ieee8021TpmrMspStatsTable_Object = MibTable
ieee8021TpmrMspStatsTable = _Ieee8021TpmrMspStatsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTable.setStatus("current")
_Ieee8021TpmrMspStatsEntry_Object = MibTableRow
ieee8021TpmrMspStatsEntry = _Ieee8021TpmrMspStatsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsEntry.setStatus("current")
_Ieee8021TpmrMspStatsTxAcks_Type = Counter32
_Ieee8021TpmrMspStatsTxAcks_Object = MibTableColumn
ieee8021TpmrMspStatsTxAcks = _Ieee8021TpmrMspStatsTxAcks_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 1),
    _Ieee8021TpmrMspStatsTxAcks_Type()
)
ieee8021TpmrMspStatsTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAcks.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAcks.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsTxAddNotifications_Type = Counter32
_Ieee8021TpmrMspStatsTxAddNotifications_Object = MibTableColumn
ieee8021TpmrMspStatsTxAddNotifications = _Ieee8021TpmrMspStatsTxAddNotifications_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 2),
    _Ieee8021TpmrMspStatsTxAddNotifications_Type()
)
ieee8021TpmrMspStatsTxAddNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAddNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAddNotifications.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsTxAddConfirmations_Type = Counter32
_Ieee8021TpmrMspStatsTxAddConfirmations_Object = MibTableColumn
ieee8021TpmrMspStatsTxAddConfirmations = _Ieee8021TpmrMspStatsTxAddConfirmations_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 3),
    _Ieee8021TpmrMspStatsTxAddConfirmations_Type()
)
ieee8021TpmrMspStatsTxAddConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAddConfirmations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxAddConfirmations.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsTxLossNotifications_Type = Counter32
_Ieee8021TpmrMspStatsTxLossNotifications_Object = MibTableColumn
ieee8021TpmrMspStatsTxLossNotifications = _Ieee8021TpmrMspStatsTxLossNotifications_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 4),
    _Ieee8021TpmrMspStatsTxLossNotifications_Type()
)
ieee8021TpmrMspStatsTxLossNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxLossNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxLossNotifications.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsTxLossConfirmations_Type = Counter32
_Ieee8021TpmrMspStatsTxLossConfirmations_Object = MibTableColumn
ieee8021TpmrMspStatsTxLossConfirmations = _Ieee8021TpmrMspStatsTxLossConfirmations_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 5),
    _Ieee8021TpmrMspStatsTxLossConfirmations_Type()
)
ieee8021TpmrMspStatsTxLossConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxLossConfirmations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsTxLossConfirmations.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsRxAcks_Type = Counter32
_Ieee8021TpmrMspStatsRxAcks_Object = MibTableColumn
ieee8021TpmrMspStatsRxAcks = _Ieee8021TpmrMspStatsRxAcks_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 6),
    _Ieee8021TpmrMspStatsRxAcks_Type()
)
ieee8021TpmrMspStatsRxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAcks.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAcks.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsRxAddNotifications_Type = Counter32
_Ieee8021TpmrMspStatsRxAddNotifications_Object = MibTableColumn
ieee8021TpmrMspStatsRxAddNotifications = _Ieee8021TpmrMspStatsRxAddNotifications_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 7),
    _Ieee8021TpmrMspStatsRxAddNotifications_Type()
)
ieee8021TpmrMspStatsRxAddNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAddNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAddNotifications.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsRxAddConfirmations_Type = Counter32
_Ieee8021TpmrMspStatsRxAddConfirmations_Object = MibTableColumn
ieee8021TpmrMspStatsRxAddConfirmations = _Ieee8021TpmrMspStatsRxAddConfirmations_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 8),
    _Ieee8021TpmrMspStatsRxAddConfirmations_Type()
)
ieee8021TpmrMspStatsRxAddConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAddConfirmations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxAddConfirmations.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsRxLossNotifications_Type = Counter32
_Ieee8021TpmrMspStatsRxLossNotifications_Object = MibTableColumn
ieee8021TpmrMspStatsRxLossNotifications = _Ieee8021TpmrMspStatsRxLossNotifications_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 9),
    _Ieee8021TpmrMspStatsRxLossNotifications_Type()
)
ieee8021TpmrMspStatsRxLossNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxLossNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxLossNotifications.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsRxLossConfirmations_Type = Counter32
_Ieee8021TpmrMspStatsRxLossConfirmations_Object = MibTableColumn
ieee8021TpmrMspStatsRxLossConfirmations = _Ieee8021TpmrMspStatsRxLossConfirmations_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 10),
    _Ieee8021TpmrMspStatsRxLossConfirmations_Type()
)
ieee8021TpmrMspStatsRxLossConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxLossConfirmations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsRxLossConfirmations.setUnits("MSPDUs")
_Ieee8021TpmrMspStatsAddEvents_Type = Counter32
_Ieee8021TpmrMspStatsAddEvents_Object = MibTableColumn
ieee8021TpmrMspStatsAddEvents = _Ieee8021TpmrMspStatsAddEvents_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 11),
    _Ieee8021TpmrMspStatsAddEvents_Type()
)
ieee8021TpmrMspStatsAddEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsAddEvents.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsAddEvents.setUnits("MSP transitions")
_Ieee8021TpmrMspStatsLossEvents_Type = Counter32
_Ieee8021TpmrMspStatsLossEvents_Object = MibTableColumn
ieee8021TpmrMspStatsLossEvents = _Ieee8021TpmrMspStatsLossEvents_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 12),
    _Ieee8021TpmrMspStatsLossEvents_Type()
)
ieee8021TpmrMspStatsLossEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsLossEvents.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsLossEvents.setUnits("MSP transitions")
_Ieee8021TpmrMspStatsMacStatusNotifications_Type = Counter32
_Ieee8021TpmrMspStatsMacStatusNotifications_Object = MibTableColumn
ieee8021TpmrMspStatsMacStatusNotifications = _Ieee8021TpmrMspStatsMacStatusNotifications_Object(
    (1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 13),
    _Ieee8021TpmrMspStatsMacStatusNotifications_Type()
)
ieee8021TpmrMspStatsMacStatusNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsMacStatusNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsMacStatusNotifications.setUnits("MSP transitions")
_Ieee8021TpmrConformance_ObjectIdentity = ObjectIdentity
ieee8021TpmrConformance = _Ieee8021TpmrConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14, 2)
)
_Ieee8021TpmrCompliances_ObjectIdentity = ObjectIdentity
ieee8021TpmrCompliances = _Ieee8021TpmrCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 1)
)
_Ieee8021TpmrGroups_ObjectIdentity = ObjectIdentity
ieee8021TpmrGroups = _Ieee8021TpmrGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2)
)
ieee8021TpmrPortEntry.registerAugmentions(
    ("IEEE8021-TPMR-MIB",
     "ieee8021TpmrPortStatsEntry")
)
ieee8021TpmrPortStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
ieee8021TpmrPortEntry.registerAugmentions(
    ("IEEE8021-TPMR-MIB",
     "ieee8021TpmrMspEntry")
)
ieee8021TpmrMspEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
ieee8021TpmrPortEntry.registerAugmentions(
    ("IEEE8021-TPMR-MIB",
     "ieee8021TpmrMspStatsEntry")
)
ieee8021TpmrMspStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())

# Managed Objects groups

ieee8021TpmrPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 1)
)
ieee8021TpmrPortGroup.setObjects(
      *(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortMgmtAddr"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortMgmtAddrForwarding"))
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortGroup.setStatus("current")

ieee8021TpmrPortStatsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 2)
)
ieee8021TpmrPortStatsGroup.setObjects(
      *(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsRxFrames"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsRxOctets"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesForwarded"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscarded"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedQueueFull"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedLifetime"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedError"))
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortStatsGroup.setStatus("current")

ieee8021TpmrPortDiscardDetailsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 3)
)
ieee8021TpmrPortDiscardDetailsGroup.setObjects(
      *(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsSource"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsReason"))
)
if mibBuilder.loadTexts:
    ieee8021TpmrPortDiscardDetailsGroup.setStatus("current")

ieee8021TpmrMspGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 4)
)
ieee8021TpmrMspGroup.setObjects(
      *(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotify"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotifyWait"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotifyRetry"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacNotify"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacNotifyTime"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacRecoverTime"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStorageType"))
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspGroup.setStatus("current")

ieee8021TpmrMspStatsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 5)
)
ieee8021TpmrMspStatsGroup.setObjects(
      *(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAcks"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAddNotifications"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAddConfirmations"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxLossNotifications"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxLossConfirmations"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAcks"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAddNotifications"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAddConfirmations"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxLossNotifications"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxLossConfirmations"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsAddEvents"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsLossEvents"),
        ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsMacStatusNotifications"))
)
if mibBuilder.loadTexts:
    ieee8021TpmrMspStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021TpmrCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TpmrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TPMR-MIB",
    **{"IEEE8021TpmrFrameDiscardErrorReason": IEEE8021TpmrFrameDiscardErrorReason,
       "ieee8021TpmrMib": ieee8021TpmrMib,
       "ieee8021TpmrNotifications": ieee8021TpmrNotifications,
       "ieee8021TpmrObjects": ieee8021TpmrObjects,
       "ieee8021TpmrPortTable": ieee8021TpmrPortTable,
       "ieee8021TpmrPortEntry": ieee8021TpmrPortEntry,
       "ieee8021TpmrPortNumber": ieee8021TpmrPortNumber,
       "ieee8021TpmrPortMgmtAddr": ieee8021TpmrPortMgmtAddr,
       "ieee8021TpmrPortMgmtAddrForwarding": ieee8021TpmrPortMgmtAddrForwarding,
       "ieee8021TpmrPortStatsTable": ieee8021TpmrPortStatsTable,
       "ieee8021TpmrPortStatsEntry": ieee8021TpmrPortStatsEntry,
       "ieee8021TpmrPortStatsRxFrames": ieee8021TpmrPortStatsRxFrames,
       "ieee8021TpmrPortStatsRxOctets": ieee8021TpmrPortStatsRxOctets,
       "ieee8021TpmrPortStatsFramesForwarded": ieee8021TpmrPortStatsFramesForwarded,
       "ieee8021TpmrPortStatsFramesDiscarded": ieee8021TpmrPortStatsFramesDiscarded,
       "ieee8021TpmrPortStatsFramesDiscardedQueueFull": ieee8021TpmrPortStatsFramesDiscardedQueueFull,
       "ieee8021TpmrPortStatsFramesDiscardedLifetime": ieee8021TpmrPortStatsFramesDiscardedLifetime,
       "ieee8021TpmrPortStatsFramesDiscardedError": ieee8021TpmrPortStatsFramesDiscardedError,
       "ieee8021TpmrPortDiscardDetailsTable": ieee8021TpmrPortDiscardDetailsTable,
       "ieee8021TpmrPortDiscardDetailsEntry": ieee8021TpmrPortDiscardDetailsEntry,
       "ieee8021TpmrPortDiscardDetailsIndex": ieee8021TpmrPortDiscardDetailsIndex,
       "ieee8021TpmrPortDiscardDetailsSource": ieee8021TpmrPortDiscardDetailsSource,
       "ieee8021TpmrPortDiscardDetailsReason": ieee8021TpmrPortDiscardDetailsReason,
       "ieee8021TpmrMspTable": ieee8021TpmrMspTable,
       "ieee8021TpmrMspEntry": ieee8021TpmrMspEntry,
       "ieee8021TpmrMspLinkNotify": ieee8021TpmrMspLinkNotify,
       "ieee8021TpmrMspLinkNotifyWait": ieee8021TpmrMspLinkNotifyWait,
       "ieee8021TpmrMspLinkNotifyRetry": ieee8021TpmrMspLinkNotifyRetry,
       "ieee8021TpmrMspMacNotify": ieee8021TpmrMspMacNotify,
       "ieee8021TpmrMspMacNotifyTime": ieee8021TpmrMspMacNotifyTime,
       "ieee8021TpmrMspMacRecoverTime": ieee8021TpmrMspMacRecoverTime,
       "ieee8021TpmrMspStorageType": ieee8021TpmrMspStorageType,
       "ieee8021TpmrMspStatsTable": ieee8021TpmrMspStatsTable,
       "ieee8021TpmrMspStatsEntry": ieee8021TpmrMspStatsEntry,
       "ieee8021TpmrMspStatsTxAcks": ieee8021TpmrMspStatsTxAcks,
       "ieee8021TpmrMspStatsTxAddNotifications": ieee8021TpmrMspStatsTxAddNotifications,
       "ieee8021TpmrMspStatsTxAddConfirmations": ieee8021TpmrMspStatsTxAddConfirmations,
       "ieee8021TpmrMspStatsTxLossNotifications": ieee8021TpmrMspStatsTxLossNotifications,
       "ieee8021TpmrMspStatsTxLossConfirmations": ieee8021TpmrMspStatsTxLossConfirmations,
       "ieee8021TpmrMspStatsRxAcks": ieee8021TpmrMspStatsRxAcks,
       "ieee8021TpmrMspStatsRxAddNotifications": ieee8021TpmrMspStatsRxAddNotifications,
       "ieee8021TpmrMspStatsRxAddConfirmations": ieee8021TpmrMspStatsRxAddConfirmations,
       "ieee8021TpmrMspStatsRxLossNotifications": ieee8021TpmrMspStatsRxLossNotifications,
       "ieee8021TpmrMspStatsRxLossConfirmations": ieee8021TpmrMspStatsRxLossConfirmations,
       "ieee8021TpmrMspStatsAddEvents": ieee8021TpmrMspStatsAddEvents,
       "ieee8021TpmrMspStatsLossEvents": ieee8021TpmrMspStatsLossEvents,
       "ieee8021TpmrMspStatsMacStatusNotifications": ieee8021TpmrMspStatsMacStatusNotifications,
       "ieee8021TpmrConformance": ieee8021TpmrConformance,
       "ieee8021TpmrCompliances": ieee8021TpmrCompliances,
       "ieee8021TpmrCompliance": ieee8021TpmrCompliance,
       "ieee8021TpmrGroups": ieee8021TpmrGroups,
       "ieee8021TpmrPortGroup": ieee8021TpmrPortGroup,
       "ieee8021TpmrPortStatsGroup": ieee8021TpmrPortStatsGroup,
       "ieee8021TpmrPortDiscardDetailsGroup": ieee8021TpmrPortDiscardDetailsGroup,
       "ieee8021TpmrMspGroup": ieee8021TpmrMspGroup,
       "ieee8021TpmrMspStatsGroup": ieee8021TpmrMspStatsGroup}
)
