# SNMP MIB module (ALVARION-DEVICE-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-DEVICE-WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:36 2024
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "ALVARION-DEVICE-MIB",
    "coDevDisIndex")

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionNotificationEnable,
 AlvarionRadioType,
 AlvarionSSIDOrNone) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionNotificationEnable",
    "AlvarionRadioType",
    "AlvarionSSIDOrNone")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alvarionDeviceWirelessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionDeviceWirelessMIBObjects_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBObjects = _AlvarionDeviceWirelessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1)
)
_CoDeviceWirelessConfigGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessConfigGroup = _CoDeviceWirelessConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 1)
)


class _CoDevWirSNRLevelNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevWirSNRLevelNotificationEnabled based on AlvarionNotificationEnable"""


_CoDevWirSNRLevelNotificationEnabled_Object = MibScalar
coDevWirSNRLevelNotificationEnabled = _CoDevWirSNRLevelNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 1, 1),
    _CoDevWirSNRLevelNotificationEnabled_Type()
)
coDevWirSNRLevelNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirSNRLevelNotificationEnabled.setStatus("current")


class _CoDevWirSNRLevelNotificationInterval_Type(Integer32):
    """Custom type coDevWirSNRLevelNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_CoDevWirSNRLevelNotificationInterval_Type.__name__ = "Integer32"
_CoDevWirSNRLevelNotificationInterval_Object = MibScalar
coDevWirSNRLevelNotificationInterval = _CoDevWirSNRLevelNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 1, 2),
    _CoDevWirSNRLevelNotificationInterval_Type()
)
coDevWirSNRLevelNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirSNRLevelNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirSNRLevelNotificationInterval.setUnits("minutes")


class _CoDevWirMinimumSNRLevel_Type(Integer32):
    """Custom type coDevWirMinimumSNRLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWirMinimumSNRLevel_Type.__name__ = "Integer32"
_CoDevWirMinimumSNRLevel_Object = MibScalar
coDevWirMinimumSNRLevel = _CoDevWirMinimumSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 1, 3),
    _CoDevWirMinimumSNRLevel_Type()
)
coDevWirMinimumSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirMinimumSNRLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirMinimumSNRLevel.setUnits("dBm")


class _CoDevWirAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevWirAssociationNotificationEnabled based on AlvarionNotificationEnable"""


_CoDevWirAssociationNotificationEnabled_Object = MibScalar
coDevWirAssociationNotificationEnabled = _CoDevWirAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 1, 4),
    _CoDevWirAssociationNotificationEnabled_Type()
)
coDevWirAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirAssociationNotificationEnabled.setStatus("current")
_CoDeviceWirelessIfStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfStatusGroup = _CoDeviceWirelessIfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2)
)
_CoDeviceWirelessInterfaceStatusTable_Object = MibTable
coDeviceWirelessInterfaceStatusTable = _CoDeviceWirelessInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatusTable.setStatus("current")
_CoDeviceWirelessInterfaceStatusEntry_Object = MibTableRow
coDeviceWirelessInterfaceStatusEntry = _CoDeviceWirelessInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1)
)
coDeviceWirelessInterfaceStatusEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatusEntry.setStatus("current")


class _CoDevWirIfStaRadioIndex_Type(Integer32):
    """Custom type coDevWirIfStaRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirIfStaRadioIndex_Type.__name__ = "Integer32"
_CoDevWirIfStaRadioIndex_Object = MibTableColumn
coDevWirIfStaRadioIndex = _CoDevWirIfStaRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 1),
    _CoDevWirIfStaRadioIndex_Type()
)
coDevWirIfStaRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioIndex.setStatus("current")


class _CoDevWirIfStaIfIndex_Type(Integer32):
    """Custom type coDevWirIfStaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirIfStaIfIndex_Type.__name__ = "Integer32"
_CoDevWirIfStaIfIndex_Object = MibTableColumn
coDevWirIfStaIfIndex = _CoDevWirIfStaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 2),
    _CoDevWirIfStaIfIndex_Type()
)
coDevWirIfStaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaIfIndex.setStatus("current")


class _CoDevWirIfStaOperatingMode_Type(Integer32):
    """Custom type coDevWirIfStaOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("apAndWds", 2),
          ("apOnly", 3),
          ("monitor", 5),
          ("sensor", 6),
          ("station", 1),
          ("wdsOnly", 4))
    )


_CoDevWirIfStaOperatingMode_Type.__name__ = "Integer32"
_CoDevWirIfStaOperatingMode_Object = MibTableColumn
coDevWirIfStaOperatingMode = _CoDevWirIfStaOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 3),
    _CoDevWirIfStaOperatingMode_Type()
)
coDevWirIfStaOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaOperatingMode.setStatus("current")


class _CoDevWirIfStaTransmitPower_Type(Integer32):
    """Custom type coDevWirIfStaTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CoDevWirIfStaTransmitPower_Type.__name__ = "Integer32"
_CoDevWirIfStaTransmitPower_Object = MibTableColumn
coDevWirIfStaTransmitPower = _CoDevWirIfStaTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 4),
    _CoDevWirIfStaTransmitPower_Type()
)
coDevWirIfStaTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirIfStaTransmitPower.setUnits("dBm")


class _CoDevWirIfStaOperatingChannel_Type(Integer32):
    """Custom type coDevWirIfStaOperatingChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_CoDevWirIfStaOperatingChannel_Type.__name__ = "Integer32"
_CoDevWirIfStaOperatingChannel_Object = MibTableColumn
coDevWirIfStaOperatingChannel = _CoDevWirIfStaOperatingChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 5),
    _CoDevWirIfStaOperatingChannel_Type()
)
coDevWirIfStaOperatingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaOperatingChannel.setStatus("current")


class _CoDevWirIfStaRadioMode_Type(Integer32):
    """Custom type coDevWirIfStaRadioMode based on Integer32"""
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
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11bAndg", 4),
          ("ieee802dot11g", 3))
    )


_CoDevWirIfStaRadioMode_Type.__name__ = "Integer32"
_CoDevWirIfStaRadioMode_Object = MibTableColumn
coDevWirIfStaRadioMode = _CoDevWirIfStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 6),
    _CoDevWirIfStaRadioMode_Type()
)
coDevWirIfStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioMode.setStatus("current")
_CoDevWirIfStaRadioType_Type = AlvarionRadioType
_CoDevWirIfStaRadioType_Object = MibTableColumn
coDevWirIfStaRadioType = _CoDevWirIfStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 7),
    _CoDevWirIfStaRadioType_Type()
)
coDevWirIfStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioType.setStatus("current")
_CoDevWirIfStaRadioOperState_Type = TruthValue
_CoDevWirIfStaRadioOperState_Object = MibTableColumn
coDevWirIfStaRadioOperState = _CoDevWirIfStaRadioOperState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 8),
    _CoDevWirIfStaRadioOperState_Type()
)
coDevWirIfStaRadioOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioOperState.setStatus("current")
_CoDevWirIfStaNumberOfClient_Type = Unsigned32
_CoDevWirIfStaNumberOfClient_Object = MibTableColumn
coDevWirIfStaNumberOfClient = _CoDevWirIfStaNumberOfClient_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 9),
    _CoDevWirIfStaNumberOfClient_Type()
)
coDevWirIfStaNumberOfClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaNumberOfClient.setStatus("current")
_CoDevWirIfStaAutoChannelEnabled_Type = TruthValue
_CoDevWirIfStaAutoChannelEnabled_Object = MibTableColumn
coDevWirIfStaAutoChannelEnabled = _CoDevWirIfStaAutoChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 10),
    _CoDevWirIfStaAutoChannelEnabled_Type()
)
coDevWirIfStaAutoChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaAutoChannelEnabled.setStatus("current")


class _CoDevWirIfStaAutoChannelInterval_Type(Integer32):
    """Custom type coDevWirIfStaAutoChannelInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CoDevWirIfStaAutoChannelInterval_Type.__name__ = "Integer32"
_CoDevWirIfStaAutoChannelInterval_Object = MibTableColumn
coDevWirIfStaAutoChannelInterval = _CoDevWirIfStaAutoChannelInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 11),
    _CoDevWirIfStaAutoChannelInterval_Type()
)
coDevWirIfStaAutoChannelInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaAutoChannelInterval.setStatus("current")
_CoDevWirIfStaAutoPowerEnabled_Type = TruthValue
_CoDevWirIfStaAutoPowerEnabled_Object = MibTableColumn
coDevWirIfStaAutoPowerEnabled = _CoDevWirIfStaAutoPowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 12),
    _CoDevWirIfStaAutoPowerEnabled_Type()
)
coDevWirIfStaAutoPowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaAutoPowerEnabled.setStatus("current")


class _CoDevWirIfStaAutoPowerInterval_Type(Integer32):
    """Custom type coDevWirIfStaAutoPowerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_CoDevWirIfStaAutoPowerInterval_Type.__name__ = "Integer32"
_CoDevWirIfStaAutoPowerInterval_Object = MibTableColumn
coDevWirIfStaAutoPowerInterval = _CoDevWirIfStaAutoPowerInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 13),
    _CoDevWirIfStaAutoPowerInterval_Type()
)
coDevWirIfStaAutoPowerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaAutoPowerInterval.setStatus("current")


class _CoDevWirIfStaResetStats_Type(Integer32):
    """Custom type coDevWirIfStaResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reset", 1))
    )


_CoDevWirIfStaResetStats_Type.__name__ = "Integer32"
_CoDevWirIfStaResetStats_Object = MibTableColumn
coDevWirIfStaResetStats = _CoDevWirIfStaResetStats_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 2, 1, 1, 14),
    _CoDevWirIfStaResetStats_Type()
)
coDevWirIfStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirIfStaResetStats.setStatus("current")
_CoDeviceWirelessIfStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfStatsGroup = _CoDeviceWirelessIfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3)
)
_CoDeviceWirelessInterfaceStatsTable_Object = MibTable
coDeviceWirelessInterfaceStatsTable = _CoDeviceWirelessInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatsTable.setStatus("current")
_CoDeviceWirelessInterfaceStatsEntry_Object = MibTableRow
coDeviceWirelessInterfaceStatsEntry = _CoDeviceWirelessInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatsEntry.setStatus("current")
_CoDevWirIfStsTransmittedFragmentCount_Type = Counter32
_CoDevWirIfStsTransmittedFragmentCount_Object = MibTableColumn
coDevWirIfStsTransmittedFragmentCount = _CoDevWirIfStsTransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 1),
    _CoDevWirIfStsTransmittedFragmentCount_Type()
)
coDevWirIfStsTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsTransmittedFragmentCount.setStatus("current")
_CoDevWirIfStsMulticastTransmittedFrameCount_Type = Counter32
_CoDevWirIfStsMulticastTransmittedFrameCount_Object = MibTableColumn
coDevWirIfStsMulticastTransmittedFrameCount = _CoDevWirIfStsMulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 2),
    _CoDevWirIfStsMulticastTransmittedFrameCount_Type()
)
coDevWirIfStsMulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMulticastTransmittedFrameCount.setStatus("current")
_CoDevWirIfStsFailedCount_Type = Counter32
_CoDevWirIfStsFailedCount_Object = MibTableColumn
coDevWirIfStsFailedCount = _CoDevWirIfStsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 3),
    _CoDevWirIfStsFailedCount_Type()
)
coDevWirIfStsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFailedCount.setStatus("current")
_CoDevWirIfStsRetryCount_Type = Counter32
_CoDevWirIfStsRetryCount_Object = MibTableColumn
coDevWirIfStsRetryCount = _CoDevWirIfStsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 4),
    _CoDevWirIfStsRetryCount_Type()
)
coDevWirIfStsRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirIfStsRetryCount.setUnits("dBm")
_CoDevWirIfStsMultipleRetryCount_Type = Counter32
_CoDevWirIfStsMultipleRetryCount_Object = MibTableColumn
coDevWirIfStsMultipleRetryCount = _CoDevWirIfStsMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 5),
    _CoDevWirIfStsMultipleRetryCount_Type()
)
coDevWirIfStsMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMultipleRetryCount.setStatus("current")
_CoDevWirIfStsFrameDuplicateCount_Type = Counter32
_CoDevWirIfStsFrameDuplicateCount_Object = MibTableColumn
coDevWirIfStsFrameDuplicateCount = _CoDevWirIfStsFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 6),
    _CoDevWirIfStsFrameDuplicateCount_Type()
)
coDevWirIfStsFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFrameDuplicateCount.setStatus("current")
_CoDevWirIfStsRTSSuccessCount_Type = Counter32
_CoDevWirIfStsRTSSuccessCount_Object = MibTableColumn
coDevWirIfStsRTSSuccessCount = _CoDevWirIfStsRTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 7),
    _CoDevWirIfStsRTSSuccessCount_Type()
)
coDevWirIfStsRTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsRTSSuccessCount.setStatus("current")
_CoDevWirIfStsRTSFailureCount_Type = Counter32
_CoDevWirIfStsRTSFailureCount_Object = MibTableColumn
coDevWirIfStsRTSFailureCount = _CoDevWirIfStsRTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 8),
    _CoDevWirIfStsRTSFailureCount_Type()
)
coDevWirIfStsRTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsRTSFailureCount.setStatus("current")
_CoDevWirIfStsACKFailureCount_Type = Counter32
_CoDevWirIfStsACKFailureCount_Object = MibTableColumn
coDevWirIfStsACKFailureCount = _CoDevWirIfStsACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 9),
    _CoDevWirIfStsACKFailureCount_Type()
)
coDevWirIfStsACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsACKFailureCount.setStatus("current")
_CoDevWirIfStsReceivedFragmentCount_Type = Counter32
_CoDevWirIfStsReceivedFragmentCount_Object = MibTableColumn
coDevWirIfStsReceivedFragmentCount = _CoDevWirIfStsReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 10),
    _CoDevWirIfStsReceivedFragmentCount_Type()
)
coDevWirIfStsReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsReceivedFragmentCount.setStatus("current")
_CoDevWirIfStsMulticastReceivedFrameCount_Type = Counter32
_CoDevWirIfStsMulticastReceivedFrameCount_Object = MibTableColumn
coDevWirIfStsMulticastReceivedFrameCount = _CoDevWirIfStsMulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 11),
    _CoDevWirIfStsMulticastReceivedFrameCount_Type()
)
coDevWirIfStsMulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMulticastReceivedFrameCount.setStatus("current")
_CoDevWirIfStsFCSErrorCount_Type = Counter32
_CoDevWirIfStsFCSErrorCount_Object = MibTableColumn
coDevWirIfStsFCSErrorCount = _CoDevWirIfStsFCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 3, 1, 1, 12),
    _CoDevWirIfStsFCSErrorCount_Type()
)
coDevWirIfStsFCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFCSErrorCount.setStatus("current")
_CoDeviceWirelessIfQosGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfQosGroup = _CoDeviceWirelessIfQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 4)
)
_CoDeviceWirelessVscStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessVscStatusGroup = _CoDeviceWirelessVscStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5)
)
_CoDeviceWirelessVscStatusTable_Object = MibTable
coDeviceWirelessVscStatusTable = _CoDeviceWirelessVscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatusTable.setStatus("current")
_CoDeviceWirelessVscStatusEntry_Object = MibTableRow
coDeviceWirelessVscStatusEntry = _CoDeviceWirelessVscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1)
)
coDeviceWirelessVscStatusEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaVscIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatusEntry.setStatus("current")


class _CoDevWirVscStaVscIndex_Type(Integer32):
    """Custom type coDevWirVscStaVscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirVscStaVscIndex_Type.__name__ = "Integer32"
_CoDevWirVscStaVscIndex_Object = MibTableColumn
coDevWirVscStaVscIndex = _CoDevWirVscStaVscIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 1),
    _CoDevWirVscStaVscIndex_Type()
)
coDevWirVscStaVscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirVscStaVscIndex.setStatus("current")


class _CoDevWirVscStaMscVscIndex_Type(Integer32):
    """Custom type coDevWirVscStaMscVscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirVscStaMscVscIndex_Type.__name__ = "Integer32"
_CoDevWirVscStaMscVscIndex_Object = MibTableColumn
coDevWirVscStaMscVscIndex = _CoDevWirVscStaMscVscIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 2),
    _CoDevWirVscStaMscVscIndex_Type()
)
coDevWirVscStaMscVscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaMscVscIndex.setStatus("current")
_CoDevWirVscStaBSSID_Type = MacAddress
_CoDevWirVscStaBSSID_Object = MibTableColumn
coDevWirVscStaBSSID = _CoDevWirVscStaBSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 3),
    _CoDevWirVscStaBSSID_Type()
)
coDevWirVscStaBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaBSSID.setStatus("current")


class _CoDevWirVscStaDefaultVLAN_Type(Integer32):
    """Custom type coDevWirVscStaDefaultVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoDevWirVscStaDefaultVLAN_Type.__name__ = "Integer32"
_CoDevWirVscStaDefaultVLAN_Object = MibTableColumn
coDevWirVscStaDefaultVLAN = _CoDevWirVscStaDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 4),
    _CoDevWirVscStaDefaultVLAN_Type()
)
coDevWirVscStaDefaultVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaDefaultVLAN.setStatus("current")
_CoDevWirVscStaMaximumNumberOfUsers_Type = Unsigned32
_CoDevWirVscStaMaximumNumberOfUsers_Object = MibTableColumn
coDevWirVscStaMaximumNumberOfUsers = _CoDevWirVscStaMaximumNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 5),
    _CoDevWirVscStaMaximumNumberOfUsers_Type()
)
coDevWirVscStaMaximumNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaMaximumNumberOfUsers.setStatus("current")
_CoDevWirVscStaCurrentNumberOfUsers_Type = Unsigned32
_CoDevWirVscStaCurrentNumberOfUsers_Object = MibTableColumn
coDevWirVscStaCurrentNumberOfUsers = _CoDevWirVscStaCurrentNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 6),
    _CoDevWirVscStaCurrentNumberOfUsers_Type()
)
coDevWirVscStaCurrentNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaCurrentNumberOfUsers.setStatus("current")


class _CoDevWirVscStaAverageSNR_Type(Integer32):
    """Custom type coDevWirVscStaAverageSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWirVscStaAverageSNR_Type.__name__ = "Integer32"
_CoDevWirVscStaAverageSNR_Object = MibTableColumn
coDevWirVscStaAverageSNR = _CoDevWirVscStaAverageSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 7),
    _CoDevWirVscStaAverageSNR_Type()
)
coDevWirVscStaAverageSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaAverageSNR.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirVscStaAverageSNR.setUnits("dBm")


class _CoDevWirVscStaResetStats_Type(Integer32):
    """Custom type coDevWirVscStaResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reset", 1))
    )


_CoDevWirVscStaResetStats_Type.__name__ = "Integer32"
_CoDevWirVscStaResetStats_Object = MibTableColumn
coDevWirVscStaResetStats = _CoDevWirVscStaResetStats_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 5, 1, 1, 8),
    _CoDevWirVscStaResetStats_Type()
)
coDevWirVscStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirVscStaResetStats.setStatus("current")
_CoDeviceWirelessVscStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessVscStatsGroup = _CoDeviceWirelessVscStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6)
)
_CoDeviceWirelessVscStatsTable_Object = MibTable
coDeviceWirelessVscStatsTable = _CoDeviceWirelessVscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatsTable.setStatus("current")
_CoDeviceWirelessVscStatsEntry_Object = MibTableRow
coDeviceWirelessVscStatsEntry = _CoDeviceWirelessVscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatsEntry.setStatus("current")
_CoDevWirVscStsTxSecurityFilter_Type = Counter32
_CoDevWirVscStsTxSecurityFilter_Object = MibTableColumn
coDevWirVscStsTxSecurityFilter = _CoDevWirVscStsTxSecurityFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 1),
    _CoDevWirVscStsTxSecurityFilter_Type()
)
coDevWirVscStsTxSecurityFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTxSecurityFilter.setStatus("current")
_CoDevWirVscStsRxSecurityFilter_Type = Counter32
_CoDevWirVscStsRxSecurityFilter_Object = MibTableColumn
coDevWirVscStsRxSecurityFilter = _CoDevWirVscStsRxSecurityFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 2),
    _CoDevWirVscStsRxSecurityFilter_Type()
)
coDevWirVscStsRxSecurityFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsRxSecurityFilter.setStatus("current")
_CoDevWirVscStsWEPICVError_Type = Counter32
_CoDevWirVscStsWEPICVError_Object = MibTableColumn
coDevWirVscStsWEPICVError = _CoDevWirVscStsWEPICVError_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 3),
    _CoDevWirVscStsWEPICVError_Type()
)
coDevWirVscStsWEPICVError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsWEPICVError.setStatus("current")
_CoDevWirVscStsWEPExcluded_Type = Counter32
_CoDevWirVscStsWEPExcluded_Object = MibTableColumn
coDevWirVscStsWEPExcluded = _CoDevWirVscStsWEPExcluded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 4),
    _CoDevWirVscStsWEPExcluded_Type()
)
coDevWirVscStsWEPExcluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsWEPExcluded.setStatus("current")
_CoDevWirVscStsTKIPICVError_Type = Counter32
_CoDevWirVscStsTKIPICVError_Object = MibTableColumn
coDevWirVscStsTKIPICVError = _CoDevWirVscStsTKIPICVError_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 5),
    _CoDevWirVscStsTKIPICVError_Type()
)
coDevWirVscStsTKIPICVError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPICVError.setStatus("current")
_CoDevWirVscStsTKIPMICError_Type = Counter32
_CoDevWirVscStsTKIPMICError_Object = MibTableColumn
coDevWirVscStsTKIPMICError = _CoDevWirVscStsTKIPMICError_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 6),
    _CoDevWirVscStsTKIPMICError_Type()
)
coDevWirVscStsTKIPMICError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPMICError.setStatus("current")
_CoDevWirVscStsTKIPCounterMeasure_Type = Counter32
_CoDevWirVscStsTKIPCounterMeasure_Object = MibTableColumn
coDevWirVscStsTKIPCounterMeasure = _CoDevWirVscStsTKIPCounterMeasure_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 7),
    _CoDevWirVscStsTKIPCounterMeasure_Type()
)
coDevWirVscStsTKIPCounterMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPCounterMeasure.setStatus("current")
_CoDevWirVscStsTKIPReplay_Type = Counter32
_CoDevWirVscStsTKIPReplay_Object = MibTableColumn
coDevWirVscStsTKIPReplay = _CoDevWirVscStsTKIPReplay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 8),
    _CoDevWirVscStsTKIPReplay_Type()
)
coDevWirVscStsTKIPReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPReplay.setStatus("current")
_CoDevWirVscStsAESError_Type = Counter32
_CoDevWirVscStsAESError_Object = MibTableColumn
coDevWirVscStsAESError = _CoDevWirVscStsAESError_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 9),
    _CoDevWirVscStsAESError_Type()
)
coDevWirVscStsAESError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsAESError.setStatus("current")
_CoDevWirVscStsAESReplay_Type = Counter32
_CoDevWirVscStsAESReplay_Object = MibTableColumn
coDevWirVscStsAESReplay = _CoDevWirVscStsAESReplay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 6, 1, 1, 10),
    _CoDevWirVscStsAESReplay_Type()
)
coDevWirVscStsAESReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsAESReplay.setStatus("current")
_CoDeviceWirelessClientStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientStatusGroup = _CoDeviceWirelessClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7)
)
_CoDeviceWirelessClientStatusTable_Object = MibTable
coDeviceWirelessClientStatusTable = _CoDeviceWirelessClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatusTable.setStatus("current")
_CoDeviceWirelessClientStatusEntry_Object = MibTableRow
coDeviceWirelessClientStatusEntry = _CoDeviceWirelessClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1)
)
coDeviceWirelessClientStatusEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatusEntry.setStatus("current")


class _CoDevWirCliStaIndex_Type(Integer32):
    """Custom type coDevWirCliStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirCliStaIndex_Type.__name__ = "Integer32"
_CoDevWirCliStaIndex_Object = MibTableColumn
coDevWirCliStaIndex = _CoDevWirCliStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 1),
    _CoDevWirCliStaIndex_Type()
)
coDevWirCliStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirCliStaIndex.setStatus("current")
_CoDevWirCliStaMACAddress_Type = MacAddress
_CoDevWirCliStaMACAddress_Object = MibTableColumn
coDevWirCliStaMACAddress = _CoDevWirCliStaMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 2),
    _CoDevWirCliStaMACAddress_Type()
)
coDevWirCliStaMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaMACAddress.setStatus("current")
_CoDevWirCliStaVscIndex_Type = Integer32
_CoDevWirCliStaVscIndex_Object = MibTableColumn
coDevWirCliStaVscIndex = _CoDevWirCliStaVscIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 3),
    _CoDevWirCliStaVscIndex_Type()
)
coDevWirCliStaVscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaVscIndex.setStatus("current")
_CoDevWirCliStaConnectTime_Type = Counter32
_CoDevWirCliStaConnectTime_Object = MibTableColumn
coDevWirCliStaConnectTime = _CoDevWirCliStaConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 4),
    _CoDevWirCliStaConnectTime_Type()
)
coDevWirCliStaConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirCliStaConnectTime.setUnits("seconds")
_CoDevWirCliStaSignalLevel_Type = Integer32
_CoDevWirCliStaSignalLevel_Object = MibTableColumn
coDevWirCliStaSignalLevel = _CoDevWirCliStaSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 5),
    _CoDevWirCliStaSignalLevel_Type()
)
coDevWirCliStaSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirCliStaSignalLevel.setUnits("dBm")
_CoDevWirCliStaNoiseLevel_Type = Integer32
_CoDevWirCliStaNoiseLevel_Object = MibTableColumn
coDevWirCliStaNoiseLevel = _CoDevWirCliStaNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 6),
    _CoDevWirCliStaNoiseLevel_Type()
)
coDevWirCliStaNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirCliStaNoiseLevel.setUnits("dBm")
_CoDevWirCliStaSNR_Type = Integer32
_CoDevWirCliStaSNR_Object = MibTableColumn
coDevWirCliStaSNR = _CoDevWirCliStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 7),
    _CoDevWirCliStaSNR_Type()
)
coDevWirCliStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaSNR.setStatus("current")


class _CoDevWirCliStaVLAN_Type(Integer32):
    """Custom type coDevWirCliStaVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoDevWirCliStaVLAN_Type.__name__ = "Integer32"
_CoDevWirCliStaVLAN_Object = MibTableColumn
coDevWirCliStaVLAN = _CoDevWirCliStaVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 8),
    _CoDevWirCliStaVLAN_Type()
)
coDevWirCliStaVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaVLAN.setStatus("current")
_CoDevWirCliStaTransmitRate_Type = Unsigned32
_CoDevWirCliStaTransmitRate_Object = MibTableColumn
coDevWirCliStaTransmitRate = _CoDevWirCliStaTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 9),
    _CoDevWirCliStaTransmitRate_Type()
)
coDevWirCliStaTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaTransmitRate.setStatus("current")
_CoDevWirCliStaReceiveRate_Type = Unsigned32
_CoDevWirCliStaReceiveRate_Object = MibTableColumn
coDevWirCliStaReceiveRate = _CoDevWirCliStaReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 10),
    _CoDevWirCliStaReceiveRate_Type()
)
coDevWirCliStaReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaReceiveRate.setStatus("current")
_CoDevWirCliStaTrafficAuthorized_Type = TruthValue
_CoDevWirCliStaTrafficAuthorized_Object = MibTableColumn
coDevWirCliStaTrafficAuthorized = _CoDevWirCliStaTrafficAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 11),
    _CoDevWirCliStaTrafficAuthorized_Type()
)
coDevWirCliStaTrafficAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaTrafficAuthorized.setStatus("current")
_CoDevWirCliSta8021xAuthenticated_Type = TruthValue
_CoDevWirCliSta8021xAuthenticated_Object = MibTableColumn
coDevWirCliSta8021xAuthenticated = _CoDevWirCliSta8021xAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 12),
    _CoDevWirCliSta8021xAuthenticated_Type()
)
coDevWirCliSta8021xAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliSta8021xAuthenticated.setStatus("current")
_CoDevWirCliStaMACAuthenticated_Type = TruthValue
_CoDevWirCliStaMACAuthenticated_Object = MibTableColumn
coDevWirCliStaMACAuthenticated = _CoDevWirCliStaMACAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 13),
    _CoDevWirCliStaMACAuthenticated_Type()
)
coDevWirCliStaMACAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaMACAuthenticated.setStatus("current")
_CoDevWirCliStaMACFiltered_Type = TruthValue
_CoDevWirCliStaMACFiltered_Object = MibTableColumn
coDevWirCliStaMACFiltered = _CoDevWirCliStaMACFiltered_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 14),
    _CoDevWirCliStaMACFiltered_Type()
)
coDevWirCliStaMACFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaMACFiltered.setStatus("current")


class _CoDevWirCliStaPhyType_Type(Integer32):
    """Custom type coDevWirCliStaPhyType based on Integer32"""
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
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11bAndg", 4),
          ("ieee802dot11g", 3))
    )


_CoDevWirCliStaPhyType_Type.__name__ = "Integer32"
_CoDevWirCliStaPhyType_Object = MibTableColumn
coDevWirCliStaPhyType = _CoDevWirCliStaPhyType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 15),
    _CoDevWirCliStaPhyType_Type()
)
coDevWirCliStaPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaPhyType.setStatus("current")


class _CoDevWirCliStaWPAType_Type(Integer32):
    """Custom type coDevWirCliStaWPAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wpa2Aes", 3),
          ("wpaTkip", 2))
    )


_CoDevWirCliStaWPAType_Type.__name__ = "Integer32"
_CoDevWirCliStaWPAType_Object = MibTableColumn
coDevWirCliStaWPAType = _CoDevWirCliStaWPAType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 16),
    _CoDevWirCliStaWPAType_Type()
)
coDevWirCliStaWPAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaWPAType.setStatus("current")
_CoDevWirCliStaIpAddress_Type = IpAddress
_CoDevWirCliStaIpAddress_Object = MibTableColumn
coDevWirCliStaIpAddress = _CoDevWirCliStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 17),
    _CoDevWirCliStaIpAddress_Type()
)
coDevWirCliStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaIpAddress.setStatus("current")
_CoDevWirCliStaPowerSavingMode_Type = TruthValue
_CoDevWirCliStaPowerSavingMode_Object = MibTableColumn
coDevWirCliStaPowerSavingMode = _CoDevWirCliStaPowerSavingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 18),
    _CoDevWirCliStaPowerSavingMode_Type()
)
coDevWirCliStaPowerSavingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaPowerSavingMode.setStatus("current")
_CoDevWirCliStaWME_Type = TruthValue
_CoDevWirCliStaWME_Object = MibTableColumn
coDevWirCliStaWME = _CoDevWirCliStaWME_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 19),
    _CoDevWirCliStaWME_Type()
)
coDevWirCliStaWME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaWME.setStatus("current")
_CoDevWirCliStaPreviousAPAddress_Type = MacAddress
_CoDevWirCliStaPreviousAPAddress_Object = MibTableColumn
coDevWirCliStaPreviousAPAddress = _CoDevWirCliStaPreviousAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 20),
    _CoDevWirCliStaPreviousAPAddress_Type()
)
coDevWirCliStaPreviousAPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaPreviousAPAddress.setStatus("current")


class _CoDevWirCliStaResetStats_Type(Integer32):
    """Custom type coDevWirCliStaResetStats based on Integer32"""
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
        *(("idle", 0),
          ("resetAll", 3),
          ("resetRates", 2),
          ("resetStats", 1))
    )


_CoDevWirCliStaResetStats_Type.__name__ = "Integer32"
_CoDevWirCliStaResetStats_Object = MibTableColumn
coDevWirCliStaResetStats = _CoDevWirCliStaResetStats_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 7, 1, 1, 21),
    _CoDevWirCliStaResetStats_Type()
)
coDevWirCliStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirCliStaResetStats.setStatus("current")
_CoDeviceWirelessClientStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientStatsGroup = _CoDeviceWirelessClientStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8)
)
_CoDeviceWirelessClientStatsTable_Object = MibTable
coDeviceWirelessClientStatsTable = _CoDeviceWirelessClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsTable.setStatus("current")
_CoDeviceWirelessClientStatsEntry_Object = MibTableRow
coDeviceWirelessClientStatsEntry = _CoDeviceWirelessClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsEntry.setStatus("current")
_CoDevWirCliStsInPkts_Type = Counter32
_CoDevWirCliStsInPkts_Object = MibTableColumn
coDevWirCliStsInPkts = _CoDevWirCliStsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1, 1, 1),
    _CoDevWirCliStsInPkts_Type()
)
coDevWirCliStsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsInPkts.setStatus("current")
_CoDevWirCliStsOutPkts_Type = Counter32
_CoDevWirCliStsOutPkts_Object = MibTableColumn
coDevWirCliStsOutPkts = _CoDevWirCliStsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1, 1, 2),
    _CoDevWirCliStsOutPkts_Type()
)
coDevWirCliStsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsOutPkts.setStatus("current")
_CoDevWirCliStsInOctets_Type = Counter64
_CoDevWirCliStsInOctets_Object = MibTableColumn
coDevWirCliStsInOctets = _CoDevWirCliStsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1, 1, 3),
    _CoDevWirCliStsInOctets_Type()
)
coDevWirCliStsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsInOctets.setStatus("current")
_CoDevWirCliStsOutOctets_Type = Counter64
_CoDevWirCliStsOutOctets_Object = MibTableColumn
coDevWirCliStsOutOctets = _CoDevWirCliStsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 8, 1, 1, 4),
    _CoDevWirCliStsOutOctets_Type()
)
coDevWirCliStsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsOutOctets.setStatus("current")
_CoDeviceWirelessClientRatesGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientRatesGroup = _CoDeviceWirelessClientRatesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9)
)
_CoDeviceWirelessClientStatsRatesTable_Object = MibTable
coDeviceWirelessClientStatsRatesTable = _CoDeviceWirelessClientStatsRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsRatesTable.setStatus("current")
_CoDeviceWirelessClientStatsRatesEntry_Object = MibTableRow
coDeviceWirelessClientStatsRatesEntry = _CoDeviceWirelessClientStatsRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsRatesEntry.setStatus("current")
_CoDevWirCliStsPktsTxRate1_Type = Counter32
_CoDevWirCliStsPktsTxRate1_Object = MibTableColumn
coDevWirCliStsPktsTxRate1 = _CoDevWirCliStsPktsTxRate1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 1),
    _CoDevWirCliStsPktsTxRate1_Type()
)
coDevWirCliStsPktsTxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate1.setStatus("current")
_CoDevWirCliStsPktsTxRate2_Type = Counter32
_CoDevWirCliStsPktsTxRate2_Object = MibTableColumn
coDevWirCliStsPktsTxRate2 = _CoDevWirCliStsPktsTxRate2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 2),
    _CoDevWirCliStsPktsTxRate2_Type()
)
coDevWirCliStsPktsTxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate2.setStatus("current")
_CoDevWirCliStsPktsTxRate5dot5_Type = Counter32
_CoDevWirCliStsPktsTxRate5dot5_Object = MibTableColumn
coDevWirCliStsPktsTxRate5dot5 = _CoDevWirCliStsPktsTxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 3),
    _CoDevWirCliStsPktsTxRate5dot5_Type()
)
coDevWirCliStsPktsTxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate5dot5.setStatus("current")
_CoDevWirCliStsPktsTxRate11_Type = Counter32
_CoDevWirCliStsPktsTxRate11_Object = MibTableColumn
coDevWirCliStsPktsTxRate11 = _CoDevWirCliStsPktsTxRate11_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 4),
    _CoDevWirCliStsPktsTxRate11_Type()
)
coDevWirCliStsPktsTxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate11.setStatus("current")
_CoDevWirCliStsPktsTxRate6_Type = Counter32
_CoDevWirCliStsPktsTxRate6_Object = MibTableColumn
coDevWirCliStsPktsTxRate6 = _CoDevWirCliStsPktsTxRate6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 5),
    _CoDevWirCliStsPktsTxRate6_Type()
)
coDevWirCliStsPktsTxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate6.setStatus("current")
_CoDevWirCliStsPktsTxRate9_Type = Counter32
_CoDevWirCliStsPktsTxRate9_Object = MibTableColumn
coDevWirCliStsPktsTxRate9 = _CoDevWirCliStsPktsTxRate9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 6),
    _CoDevWirCliStsPktsTxRate9_Type()
)
coDevWirCliStsPktsTxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate9.setStatus("current")
_CoDevWirCliStsPktsTxRate12_Type = Counter32
_CoDevWirCliStsPktsTxRate12_Object = MibTableColumn
coDevWirCliStsPktsTxRate12 = _CoDevWirCliStsPktsTxRate12_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 7),
    _CoDevWirCliStsPktsTxRate12_Type()
)
coDevWirCliStsPktsTxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate12.setStatus("current")
_CoDevWirCliStsPktsTxRate18_Type = Counter32
_CoDevWirCliStsPktsTxRate18_Object = MibTableColumn
coDevWirCliStsPktsTxRate18 = _CoDevWirCliStsPktsTxRate18_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 8),
    _CoDevWirCliStsPktsTxRate18_Type()
)
coDevWirCliStsPktsTxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate18.setStatus("current")
_CoDevWirCliStsPktsTxRate24_Type = Counter32
_CoDevWirCliStsPktsTxRate24_Object = MibTableColumn
coDevWirCliStsPktsTxRate24 = _CoDevWirCliStsPktsTxRate24_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 9),
    _CoDevWirCliStsPktsTxRate24_Type()
)
coDevWirCliStsPktsTxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate24.setStatus("current")
_CoDevWirCliStsPktsTxRate36_Type = Counter32
_CoDevWirCliStsPktsTxRate36_Object = MibTableColumn
coDevWirCliStsPktsTxRate36 = _CoDevWirCliStsPktsTxRate36_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 10),
    _CoDevWirCliStsPktsTxRate36_Type()
)
coDevWirCliStsPktsTxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate36.setStatus("current")
_CoDevWirCliStsPktsTxRate48_Type = Counter32
_CoDevWirCliStsPktsTxRate48_Object = MibTableColumn
coDevWirCliStsPktsTxRate48 = _CoDevWirCliStsPktsTxRate48_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 11),
    _CoDevWirCliStsPktsTxRate48_Type()
)
coDevWirCliStsPktsTxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate48.setStatus("current")
_CoDevWirCliStsPktsTxRate54_Type = Counter32
_CoDevWirCliStsPktsTxRate54_Object = MibTableColumn
coDevWirCliStsPktsTxRate54 = _CoDevWirCliStsPktsTxRate54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 12),
    _CoDevWirCliStsPktsTxRate54_Type()
)
coDevWirCliStsPktsTxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate54.setStatus("current")
_CoDevWirCliStsPktsRxRate1_Type = Counter32
_CoDevWirCliStsPktsRxRate1_Object = MibTableColumn
coDevWirCliStsPktsRxRate1 = _CoDevWirCliStsPktsRxRate1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 13),
    _CoDevWirCliStsPktsRxRate1_Type()
)
coDevWirCliStsPktsRxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate1.setStatus("current")
_CoDevWirCliStsPktsRxRate2_Type = Counter32
_CoDevWirCliStsPktsRxRate2_Object = MibTableColumn
coDevWirCliStsPktsRxRate2 = _CoDevWirCliStsPktsRxRate2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 14),
    _CoDevWirCliStsPktsRxRate2_Type()
)
coDevWirCliStsPktsRxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate2.setStatus("current")
_CoDevWirCliStsPktsRxRate5dot5_Type = Counter32
_CoDevWirCliStsPktsRxRate5dot5_Object = MibTableColumn
coDevWirCliStsPktsRxRate5dot5 = _CoDevWirCliStsPktsRxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 15),
    _CoDevWirCliStsPktsRxRate5dot5_Type()
)
coDevWirCliStsPktsRxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate5dot5.setStatus("current")
_CoDevWirCliStsPktsRxRate11_Type = Counter32
_CoDevWirCliStsPktsRxRate11_Object = MibTableColumn
coDevWirCliStsPktsRxRate11 = _CoDevWirCliStsPktsRxRate11_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 16),
    _CoDevWirCliStsPktsRxRate11_Type()
)
coDevWirCliStsPktsRxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate11.setStatus("current")
_CoDevWirCliStsPktsRxRate6_Type = Counter32
_CoDevWirCliStsPktsRxRate6_Object = MibTableColumn
coDevWirCliStsPktsRxRate6 = _CoDevWirCliStsPktsRxRate6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 17),
    _CoDevWirCliStsPktsRxRate6_Type()
)
coDevWirCliStsPktsRxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate6.setStatus("current")
_CoDevWirCliStsPktsRxRate9_Type = Counter32
_CoDevWirCliStsPktsRxRate9_Object = MibTableColumn
coDevWirCliStsPktsRxRate9 = _CoDevWirCliStsPktsRxRate9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 18),
    _CoDevWirCliStsPktsRxRate9_Type()
)
coDevWirCliStsPktsRxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate9.setStatus("current")
_CoDevWirCliStsPktsRxRate12_Type = Counter32
_CoDevWirCliStsPktsRxRate12_Object = MibTableColumn
coDevWirCliStsPktsRxRate12 = _CoDevWirCliStsPktsRxRate12_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 19),
    _CoDevWirCliStsPktsRxRate12_Type()
)
coDevWirCliStsPktsRxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate12.setStatus("current")
_CoDevWirCliStsPktsRxRate18_Type = Counter32
_CoDevWirCliStsPktsRxRate18_Object = MibTableColumn
coDevWirCliStsPktsRxRate18 = _CoDevWirCliStsPktsRxRate18_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 20),
    _CoDevWirCliStsPktsRxRate18_Type()
)
coDevWirCliStsPktsRxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate18.setStatus("current")
_CoDevWirCliStsPktsRxRate24_Type = Counter32
_CoDevWirCliStsPktsRxRate24_Object = MibTableColumn
coDevWirCliStsPktsRxRate24 = _CoDevWirCliStsPktsRxRate24_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 21),
    _CoDevWirCliStsPktsRxRate24_Type()
)
coDevWirCliStsPktsRxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate24.setStatus("current")
_CoDevWirCliStsPktsRxRate36_Type = Counter32
_CoDevWirCliStsPktsRxRate36_Object = MibTableColumn
coDevWirCliStsPktsRxRate36 = _CoDevWirCliStsPktsRxRate36_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 22),
    _CoDevWirCliStsPktsRxRate36_Type()
)
coDevWirCliStsPktsRxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate36.setStatus("current")
_CoDevWirCliStsPktsRxRate48_Type = Counter32
_CoDevWirCliStsPktsRxRate48_Object = MibTableColumn
coDevWirCliStsPktsRxRate48 = _CoDevWirCliStsPktsRxRate48_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 23),
    _CoDevWirCliStsPktsRxRate48_Type()
)
coDevWirCliStsPktsRxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate48.setStatus("current")
_CoDevWirCliStsPktsRxRate54_Type = Counter32
_CoDevWirCliStsPktsRxRate54_Object = MibTableColumn
coDevWirCliStsPktsRxRate54 = _CoDevWirCliStsPktsRxRate54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 9, 1, 1, 24),
    _CoDevWirCliStsPktsRxRate54_Type()
)
coDevWirCliStsPktsRxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate54.setStatus("current")
_CoDeviceWirelessDetectedAPGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessDetectedAPGroup = _CoDeviceWirelessDetectedAPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13)
)
_CoDeviceWirelessDetectedAPTable_Object = MibTable
coDeviceWirelessDetectedAPTable = _CoDeviceWirelessDetectedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessDetectedAPTable.setStatus("current")
_CoDeviceWirelessDetectedAPEntry_Object = MibTableRow
coDeviceWirelessDetectedAPEntry = _CoDeviceWirelessDetectedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1)
)
coDeviceWirelessDetectedAPEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWirelessDetectedAPEntry.setStatus("current")


class _CoDevWirApIndex_Type(Integer32):
    """Custom type coDevWirApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirApIndex_Type.__name__ = "Integer32"
_CoDevWirApIndex_Object = MibTableColumn
coDevWirApIndex = _CoDevWirApIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 1),
    _CoDevWirApIndex_Type()
)
coDevWirApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirApIndex.setStatus("current")
_CoDevWirApBSSID_Type = MacAddress
_CoDevWirApBSSID_Object = MibTableColumn
coDevWirApBSSID = _CoDevWirApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 2),
    _CoDevWirApBSSID_Type()
)
coDevWirApBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApBSSID.setStatus("current")


class _CoDevWirApRadioIndex_Type(Integer32):
    """Custom type coDevWirApRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirApRadioIndex_Type.__name__ = "Integer32"
_CoDevWirApRadioIndex_Object = MibTableColumn
coDevWirApRadioIndex = _CoDevWirApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 3),
    _CoDevWirApRadioIndex_Type()
)
coDevWirApRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApRadioIndex.setStatus("current")
_CoDevWirApSSID_Type = AlvarionSSIDOrNone
_CoDevWirApSSID_Object = MibTableColumn
coDevWirApSSID = _CoDevWirApSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 4),
    _CoDevWirApSSID_Type()
)
coDevWirApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApSSID.setStatus("current")


class _CoDevWirApChannel_Type(Integer32):
    """Custom type coDevWirApChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirApChannel_Type.__name__ = "Integer32"
_CoDevWirApChannel_Object = MibTableColumn
coDevWirApChannel = _CoDevWirApChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 5),
    _CoDevWirApChannel_Type()
)
coDevWirApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApChannel.setStatus("current")
_CoDevWirApSignalLevel_Type = Integer32
_CoDevWirApSignalLevel_Object = MibTableColumn
coDevWirApSignalLevel = _CoDevWirApSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 6),
    _CoDevWirApSignalLevel_Type()
)
coDevWirApSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirApSignalLevel.setUnits("dBm")
_CoDevWirApNoiseLevel_Type = Integer32
_CoDevWirApNoiseLevel_Object = MibTableColumn
coDevWirApNoiseLevel = _CoDevWirApNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 7),
    _CoDevWirApNoiseLevel_Type()
)
coDevWirApNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirApNoiseLevel.setUnits("dBm")
_CoDevWirApSNR_Type = Integer32
_CoDevWirApSNR_Object = MibTableColumn
coDevWirApSNR = _CoDevWirApSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 8),
    _CoDevWirApSNR_Type()
)
coDevWirApSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApSNR.setStatus("current")


class _CoDevWirApPHYType_Type(Integer32):
    """Custom type coDevWirApPHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3))
    )


_CoDevWirApPHYType_Type.__name__ = "Integer32"
_CoDevWirApPHYType_Object = MibTableColumn
coDevWirApPHYType = _CoDevWirApPHYType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 9),
    _CoDevWirApPHYType_Type()
)
coDevWirApPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApPHYType.setStatus("current")


class _CoDevWirApSecurity_Type(Integer32):
    """Custom type coDevWirApSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep", 2),
          ("wpa", 3),
          ("wpa2", 4),
          ("wpaAndWpa2", 5))
    )


_CoDevWirApSecurity_Type.__name__ = "Integer32"
_CoDevWirApSecurity_Object = MibTableColumn
coDevWirApSecurity = _CoDevWirApSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 1, 13, 1, 1, 10),
    _CoDevWirApSecurity_Type()
)
coDevWirApSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApSecurity.setStatus("current")
_AlvarionDeviceWirelessMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBNotificationPrefix = _AlvarionDeviceWirelessMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 2)
)
_AlvarionDeviceWirelessMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBNotifications = _AlvarionDeviceWirelessMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 2, 0)
)
_AlvarionDeviceWirelessMIBConformance_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBConformance = _AlvarionDeviceWirelessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3)
)
_AlvarionDeviceWirelessMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBCompliances = _AlvarionDeviceWirelessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 1)
)
_AlvarionDeviceWirelessMIBGroups_ObjectIdentity = ObjectIdentity
alvarionDeviceWirelessMIBGroups = _AlvarionDeviceWirelessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2)
)
coDeviceWirelessInterfaceStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessInterfaceStatsEntry")
)
coDeviceWirelessInterfaceStatsEntry.setIndexNames(*coDeviceWirelessInterfaceStatusEntry.getIndexNames())
coDeviceWirelessVscStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessVscStatsEntry")
)
coDeviceWirelessVscStatsEntry.setIndexNames(*coDeviceWirelessVscStatusEntry.getIndexNames())
coDeviceWirelessClientStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessClientStatsEntry")
)
coDeviceWirelessClientStatsEntry.setIndexNames(*coDeviceWirelessClientStatusEntry.getIndexNames())
coDeviceWirelessClientStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessClientStatsRatesEntry")
)
coDeviceWirelessClientStatsRatesEntry.setIndexNames(*coDeviceWirelessClientStatusEntry.getIndexNames())

# Managed Objects groups

alvarionDeviceWirelessConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 1)
)
alvarionDeviceWirelessConfigMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirSNRLevelNotificationEnabled"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirSNRLevelNotificationInterval"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirMinimumSNRLevel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirAssociationNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessConfigMIBGroup.setStatus("current")

alvarionDeviceWirelessIfStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 2)
)
alvarionDeviceWirelessIfStatusMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaIfIndex"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaOperatingMode"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaTransmitPower"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaOperatingChannel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioMode"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioType"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioOperState"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaNumberOfClient"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoChannelEnabled"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoChannelInterval"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoPowerEnabled"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoPowerInterval"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStaResetStats"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessIfStatusMIBGroup.setStatus("current")

alvarionDeviceWirelessIfStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 3)
)
alvarionDeviceWirelessIfStatsMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsTransmittedFragmentCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsMulticastTransmittedFrameCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsFailedCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsRetryCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsMultipleRetryCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsFrameDuplicateCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsRTSSuccessCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsRTSFailureCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsACKFailureCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsReceivedFragmentCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsMulticastReceivedFrameCount"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirIfStsFCSErrorCount"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessIfStatsMIBGroup.setStatus("current")

alvarionDeviceVscStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 4)
)
alvarionDeviceVscStatusMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaDefaultVLAN"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaMaximumNumberOfUsers"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaCurrentNumberOfUsers"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaAverageSNR"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaResetStats"))
)
if mibBuilder.loadTexts:
    alvarionDeviceVscStatusMIBGroup.setStatus("current")

alvarionDeviceVscStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 5)
)
alvarionDeviceVscStatsMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsTxSecurityFilter"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsRxSecurityFilter"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsWEPICVError"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsWEPExcluded"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPICVError"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPMICError"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPCounterMeasure"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPReplay"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsAESError"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStsAESReplay"))
)
if mibBuilder.loadTexts:
    alvarionDeviceVscStatsMIBGroup.setStatus("current")

alvarionDeviceWirelessClientStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 6)
)
alvarionDeviceWirelessClientStatusMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAddress"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaVscIndex"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaConnectTime"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaSignalLevel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaNoiseLevel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaSNR"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaVLAN"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaTransmitRate"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaReceiveRate"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaTrafficAuthorized"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliSta8021xAuthenticated"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAuthenticated"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACFiltered"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaPhyType"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaWPAType"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaIpAddress"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaPowerSavingMode"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaWME"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaPreviousAPAddress"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaResetStats"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessClientStatusMIBGroup.setStatus("current")

alvarionDeviceWirelessClientStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 7)
)
alvarionDeviceWirelessClientStatsMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsInPkts"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsOutPkts"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsInOctets"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsOutOctets"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessClientStatsMIBGroup.setStatus("current")

alvarionDeviceWirelessClientStatsRatesMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 8)
)
alvarionDeviceWirelessClientStatsRatesMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate1"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate2"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate5dot5"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate11"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate6"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate9"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate12"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate18"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate24"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate36"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate48"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate54"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate1"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate2"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate5dot5"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate11"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate6"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate9"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate12"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate18"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate24"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate36"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate48"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate54"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessClientStatsRatesMIBGroup.setStatus("current")

alvarionDeviceWirelessDetectedAPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 9)
)
alvarionDeviceWirelessDetectedAPMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApBSSID"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApRadioIndex"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApSSID"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApChannel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApSignalLevel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApNoiseLevel"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApSNR"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApPHYType"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirApSecurity"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessDetectedAPMIBGroup.setStatus("current")


# Notification objects

coDeviceWirelessSNRLevelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 2, 0, 1)
)
coDeviceWirelessSNRLevelNotification.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaAverageSNR"))
)
if mibBuilder.loadTexts:
    coDeviceWirelessSNRLevelNotification.setStatus(
        "current"
    )

coDeviceWirelessAssociationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 2, 0, 2)
)
coDeviceWirelessAssociationNotification.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAddress"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"))
)
if mibBuilder.loadTexts:
    coDeviceWirelessAssociationNotification.setStatus(
        "current"
    )


# Notifications groups

alvarionDeviceWirelessNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 2, 10)
)
alvarionDeviceWirelessNotificationGroup.setObjects(
      *(("ALVARION-DEVICE-WIRELESS-MIB", "coDeviceWirelessSNRLevelNotification"),
        ("ALVARION-DEVICE-WIRELESS-MIB", "coDeviceWirelessAssociationNotification"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionDeviceWirelessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionDeviceWirelessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-DEVICE-WIRELESS-MIB",
    **{"alvarionDeviceWirelessMIB": alvarionDeviceWirelessMIB,
       "alvarionDeviceWirelessMIBObjects": alvarionDeviceWirelessMIBObjects,
       "coDeviceWirelessConfigGroup": coDeviceWirelessConfigGroup,
       "coDevWirSNRLevelNotificationEnabled": coDevWirSNRLevelNotificationEnabled,
       "coDevWirSNRLevelNotificationInterval": coDevWirSNRLevelNotificationInterval,
       "coDevWirMinimumSNRLevel": coDevWirMinimumSNRLevel,
       "coDevWirAssociationNotificationEnabled": coDevWirAssociationNotificationEnabled,
       "coDeviceWirelessIfStatusGroup": coDeviceWirelessIfStatusGroup,
       "coDeviceWirelessInterfaceStatusTable": coDeviceWirelessInterfaceStatusTable,
       "coDeviceWirelessInterfaceStatusEntry": coDeviceWirelessInterfaceStatusEntry,
       "coDevWirIfStaRadioIndex": coDevWirIfStaRadioIndex,
       "coDevWirIfStaIfIndex": coDevWirIfStaIfIndex,
       "coDevWirIfStaOperatingMode": coDevWirIfStaOperatingMode,
       "coDevWirIfStaTransmitPower": coDevWirIfStaTransmitPower,
       "coDevWirIfStaOperatingChannel": coDevWirIfStaOperatingChannel,
       "coDevWirIfStaRadioMode": coDevWirIfStaRadioMode,
       "coDevWirIfStaRadioType": coDevWirIfStaRadioType,
       "coDevWirIfStaRadioOperState": coDevWirIfStaRadioOperState,
       "coDevWirIfStaNumberOfClient": coDevWirIfStaNumberOfClient,
       "coDevWirIfStaAutoChannelEnabled": coDevWirIfStaAutoChannelEnabled,
       "coDevWirIfStaAutoChannelInterval": coDevWirIfStaAutoChannelInterval,
       "coDevWirIfStaAutoPowerEnabled": coDevWirIfStaAutoPowerEnabled,
       "coDevWirIfStaAutoPowerInterval": coDevWirIfStaAutoPowerInterval,
       "coDevWirIfStaResetStats": coDevWirIfStaResetStats,
       "coDeviceWirelessIfStatsGroup": coDeviceWirelessIfStatsGroup,
       "coDeviceWirelessInterfaceStatsTable": coDeviceWirelessInterfaceStatsTable,
       "coDeviceWirelessInterfaceStatsEntry": coDeviceWirelessInterfaceStatsEntry,
       "coDevWirIfStsTransmittedFragmentCount": coDevWirIfStsTransmittedFragmentCount,
       "coDevWirIfStsMulticastTransmittedFrameCount": coDevWirIfStsMulticastTransmittedFrameCount,
       "coDevWirIfStsFailedCount": coDevWirIfStsFailedCount,
       "coDevWirIfStsRetryCount": coDevWirIfStsRetryCount,
       "coDevWirIfStsMultipleRetryCount": coDevWirIfStsMultipleRetryCount,
       "coDevWirIfStsFrameDuplicateCount": coDevWirIfStsFrameDuplicateCount,
       "coDevWirIfStsRTSSuccessCount": coDevWirIfStsRTSSuccessCount,
       "coDevWirIfStsRTSFailureCount": coDevWirIfStsRTSFailureCount,
       "coDevWirIfStsACKFailureCount": coDevWirIfStsACKFailureCount,
       "coDevWirIfStsReceivedFragmentCount": coDevWirIfStsReceivedFragmentCount,
       "coDevWirIfStsMulticastReceivedFrameCount": coDevWirIfStsMulticastReceivedFrameCount,
       "coDevWirIfStsFCSErrorCount": coDevWirIfStsFCSErrorCount,
       "coDeviceWirelessIfQosGroup": coDeviceWirelessIfQosGroup,
       "coDeviceWirelessVscStatusGroup": coDeviceWirelessVscStatusGroup,
       "coDeviceWirelessVscStatusTable": coDeviceWirelessVscStatusTable,
       "coDeviceWirelessVscStatusEntry": coDeviceWirelessVscStatusEntry,
       "coDevWirVscStaVscIndex": coDevWirVscStaVscIndex,
       "coDevWirVscStaMscVscIndex": coDevWirVscStaMscVscIndex,
       "coDevWirVscStaBSSID": coDevWirVscStaBSSID,
       "coDevWirVscStaDefaultVLAN": coDevWirVscStaDefaultVLAN,
       "coDevWirVscStaMaximumNumberOfUsers": coDevWirVscStaMaximumNumberOfUsers,
       "coDevWirVscStaCurrentNumberOfUsers": coDevWirVscStaCurrentNumberOfUsers,
       "coDevWirVscStaAverageSNR": coDevWirVscStaAverageSNR,
       "coDevWirVscStaResetStats": coDevWirVscStaResetStats,
       "coDeviceWirelessVscStatsGroup": coDeviceWirelessVscStatsGroup,
       "coDeviceWirelessVscStatsTable": coDeviceWirelessVscStatsTable,
       "coDeviceWirelessVscStatsEntry": coDeviceWirelessVscStatsEntry,
       "coDevWirVscStsTxSecurityFilter": coDevWirVscStsTxSecurityFilter,
       "coDevWirVscStsRxSecurityFilter": coDevWirVscStsRxSecurityFilter,
       "coDevWirVscStsWEPICVError": coDevWirVscStsWEPICVError,
       "coDevWirVscStsWEPExcluded": coDevWirVscStsWEPExcluded,
       "coDevWirVscStsTKIPICVError": coDevWirVscStsTKIPICVError,
       "coDevWirVscStsTKIPMICError": coDevWirVscStsTKIPMICError,
       "coDevWirVscStsTKIPCounterMeasure": coDevWirVscStsTKIPCounterMeasure,
       "coDevWirVscStsTKIPReplay": coDevWirVscStsTKIPReplay,
       "coDevWirVscStsAESError": coDevWirVscStsAESError,
       "coDevWirVscStsAESReplay": coDevWirVscStsAESReplay,
       "coDeviceWirelessClientStatusGroup": coDeviceWirelessClientStatusGroup,
       "coDeviceWirelessClientStatusTable": coDeviceWirelessClientStatusTable,
       "coDeviceWirelessClientStatusEntry": coDeviceWirelessClientStatusEntry,
       "coDevWirCliStaIndex": coDevWirCliStaIndex,
       "coDevWirCliStaMACAddress": coDevWirCliStaMACAddress,
       "coDevWirCliStaVscIndex": coDevWirCliStaVscIndex,
       "coDevWirCliStaConnectTime": coDevWirCliStaConnectTime,
       "coDevWirCliStaSignalLevel": coDevWirCliStaSignalLevel,
       "coDevWirCliStaNoiseLevel": coDevWirCliStaNoiseLevel,
       "coDevWirCliStaSNR": coDevWirCliStaSNR,
       "coDevWirCliStaVLAN": coDevWirCliStaVLAN,
       "coDevWirCliStaTransmitRate": coDevWirCliStaTransmitRate,
       "coDevWirCliStaReceiveRate": coDevWirCliStaReceiveRate,
       "coDevWirCliStaTrafficAuthorized": coDevWirCliStaTrafficAuthorized,
       "coDevWirCliSta8021xAuthenticated": coDevWirCliSta8021xAuthenticated,
       "coDevWirCliStaMACAuthenticated": coDevWirCliStaMACAuthenticated,
       "coDevWirCliStaMACFiltered": coDevWirCliStaMACFiltered,
       "coDevWirCliStaPhyType": coDevWirCliStaPhyType,
       "coDevWirCliStaWPAType": coDevWirCliStaWPAType,
       "coDevWirCliStaIpAddress": coDevWirCliStaIpAddress,
       "coDevWirCliStaPowerSavingMode": coDevWirCliStaPowerSavingMode,
       "coDevWirCliStaWME": coDevWirCliStaWME,
       "coDevWirCliStaPreviousAPAddress": coDevWirCliStaPreviousAPAddress,
       "coDevWirCliStaResetStats": coDevWirCliStaResetStats,
       "coDeviceWirelessClientStatsGroup": coDeviceWirelessClientStatsGroup,
       "coDeviceWirelessClientStatsTable": coDeviceWirelessClientStatsTable,
       "coDeviceWirelessClientStatsEntry": coDeviceWirelessClientStatsEntry,
       "coDevWirCliStsInPkts": coDevWirCliStsInPkts,
       "coDevWirCliStsOutPkts": coDevWirCliStsOutPkts,
       "coDevWirCliStsInOctets": coDevWirCliStsInOctets,
       "coDevWirCliStsOutOctets": coDevWirCliStsOutOctets,
       "coDeviceWirelessClientRatesGroup": coDeviceWirelessClientRatesGroup,
       "coDeviceWirelessClientStatsRatesTable": coDeviceWirelessClientStatsRatesTable,
       "coDeviceWirelessClientStatsRatesEntry": coDeviceWirelessClientStatsRatesEntry,
       "coDevWirCliStsPktsTxRate1": coDevWirCliStsPktsTxRate1,
       "coDevWirCliStsPktsTxRate2": coDevWirCliStsPktsTxRate2,
       "coDevWirCliStsPktsTxRate5dot5": coDevWirCliStsPktsTxRate5dot5,
       "coDevWirCliStsPktsTxRate11": coDevWirCliStsPktsTxRate11,
       "coDevWirCliStsPktsTxRate6": coDevWirCliStsPktsTxRate6,
       "coDevWirCliStsPktsTxRate9": coDevWirCliStsPktsTxRate9,
       "coDevWirCliStsPktsTxRate12": coDevWirCliStsPktsTxRate12,
       "coDevWirCliStsPktsTxRate18": coDevWirCliStsPktsTxRate18,
       "coDevWirCliStsPktsTxRate24": coDevWirCliStsPktsTxRate24,
       "coDevWirCliStsPktsTxRate36": coDevWirCliStsPktsTxRate36,
       "coDevWirCliStsPktsTxRate48": coDevWirCliStsPktsTxRate48,
       "coDevWirCliStsPktsTxRate54": coDevWirCliStsPktsTxRate54,
       "coDevWirCliStsPktsRxRate1": coDevWirCliStsPktsRxRate1,
       "coDevWirCliStsPktsRxRate2": coDevWirCliStsPktsRxRate2,
       "coDevWirCliStsPktsRxRate5dot5": coDevWirCliStsPktsRxRate5dot5,
       "coDevWirCliStsPktsRxRate11": coDevWirCliStsPktsRxRate11,
       "coDevWirCliStsPktsRxRate6": coDevWirCliStsPktsRxRate6,
       "coDevWirCliStsPktsRxRate9": coDevWirCliStsPktsRxRate9,
       "coDevWirCliStsPktsRxRate12": coDevWirCliStsPktsRxRate12,
       "coDevWirCliStsPktsRxRate18": coDevWirCliStsPktsRxRate18,
       "coDevWirCliStsPktsRxRate24": coDevWirCliStsPktsRxRate24,
       "coDevWirCliStsPktsRxRate36": coDevWirCliStsPktsRxRate36,
       "coDevWirCliStsPktsRxRate48": coDevWirCliStsPktsRxRate48,
       "coDevWirCliStsPktsRxRate54": coDevWirCliStsPktsRxRate54,
       "coDeviceWirelessDetectedAPGroup": coDeviceWirelessDetectedAPGroup,
       "coDeviceWirelessDetectedAPTable": coDeviceWirelessDetectedAPTable,
       "coDeviceWirelessDetectedAPEntry": coDeviceWirelessDetectedAPEntry,
       "coDevWirApIndex": coDevWirApIndex,
       "coDevWirApBSSID": coDevWirApBSSID,
       "coDevWirApRadioIndex": coDevWirApRadioIndex,
       "coDevWirApSSID": coDevWirApSSID,
       "coDevWirApChannel": coDevWirApChannel,
       "coDevWirApSignalLevel": coDevWirApSignalLevel,
       "coDevWirApNoiseLevel": coDevWirApNoiseLevel,
       "coDevWirApSNR": coDevWirApSNR,
       "coDevWirApPHYType": coDevWirApPHYType,
       "coDevWirApSecurity": coDevWirApSecurity,
       "alvarionDeviceWirelessMIBNotificationPrefix": alvarionDeviceWirelessMIBNotificationPrefix,
       "alvarionDeviceWirelessMIBNotifications": alvarionDeviceWirelessMIBNotifications,
       "coDeviceWirelessSNRLevelNotification": coDeviceWirelessSNRLevelNotification,
       "coDeviceWirelessAssociationNotification": coDeviceWirelessAssociationNotification,
       "alvarionDeviceWirelessMIBConformance": alvarionDeviceWirelessMIBConformance,
       "alvarionDeviceWirelessMIBCompliances": alvarionDeviceWirelessMIBCompliances,
       "alvarionDeviceWirelessMIBCompliance": alvarionDeviceWirelessMIBCompliance,
       "alvarionDeviceWirelessMIBGroups": alvarionDeviceWirelessMIBGroups,
       "alvarionDeviceWirelessConfigMIBGroup": alvarionDeviceWirelessConfigMIBGroup,
       "alvarionDeviceWirelessIfStatusMIBGroup": alvarionDeviceWirelessIfStatusMIBGroup,
       "alvarionDeviceWirelessIfStatsMIBGroup": alvarionDeviceWirelessIfStatsMIBGroup,
       "alvarionDeviceVscStatusMIBGroup": alvarionDeviceVscStatusMIBGroup,
       "alvarionDeviceVscStatsMIBGroup": alvarionDeviceVscStatsMIBGroup,
       "alvarionDeviceWirelessClientStatusMIBGroup": alvarionDeviceWirelessClientStatusMIBGroup,
       "alvarionDeviceWirelessClientStatsMIBGroup": alvarionDeviceWirelessClientStatsMIBGroup,
       "alvarionDeviceWirelessClientStatsRatesMIBGroup": alvarionDeviceWirelessClientStatsRatesMIBGroup,
       "alvarionDeviceWirelessDetectedAPMIBGroup": alvarionDeviceWirelessDetectedAPMIBGroup,
       "alvarionDeviceWirelessNotificationGroup": alvarionDeviceWirelessNotificationGroup}
)
