# SNMP MIB module (COLUBRIS-DEVICE-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-DEVICE-WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:18 2024
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
    "COLUBRIS-DEVICE-MIB",
    "coDevDisIndex")

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,
 ColubrisRadioType,
 ColubrisSSID,
 ColubrisSSIDOrNone) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable",
    "ColubrisRadioType",
    "ColubrisSSID",
    "ColubrisSSIDOrNone")

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

colubrisDeviceWirelessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisDeviceWirelessMIBObjects_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBObjects = _ColubrisDeviceWirelessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1)
)
_CoDeviceWirelessConfigGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessConfigGroup = _CoDeviceWirelessConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 1)
)


class _CoDevWirSNRLevelNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDevWirSNRLevelNotificationEnabled based on ColubrisNotificationEnable"""


_CoDevWirSNRLevelNotificationEnabled_Object = MibScalar
coDevWirSNRLevelNotificationEnabled = _CoDevWirSNRLevelNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 1, 3),
    _CoDevWirMinimumSNRLevel_Type()
)
coDevWirMinimumSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirMinimumSNRLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirMinimumSNRLevel.setUnits("dBm")


class _CoDevWirAssociationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDevWirAssociationNotificationEnabled based on ColubrisNotificationEnable"""


_CoDevWirAssociationNotificationEnabled_Object = MibScalar
coDevWirAssociationNotificationEnabled = _CoDevWirAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 1, 4),
    _CoDevWirAssociationNotificationEnabled_Type()
)
coDevWirAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirAssociationNotificationEnabled.setStatus("current")
_CoDeviceWirelessIfStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfStatusGroup = _CoDeviceWirelessIfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2)
)
_CoDeviceWirelessInterfaceStatusTable_Object = MibTable
coDeviceWirelessInterfaceStatusTable = _CoDeviceWirelessInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatusTable.setStatus("current")
_CoDeviceWirelessInterfaceStatusEntry_Object = MibTableRow
coDeviceWirelessInterfaceStatusEntry = _CoDeviceWirelessInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1)
)
coDeviceWirelessInterfaceStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 5),
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
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11aTurbo", 5),
          ("ieee802dot11b", 2),
          ("ieee802dot11bAndg", 4),
          ("ieee802dot11g", 3),
          ("ieee802dot11na", 6),
          ("ieee802dot11ng", 7))
    )


_CoDevWirIfStaRadioMode_Type.__name__ = "Integer32"
_CoDevWirIfStaRadioMode_Object = MibTableColumn
coDevWirIfStaRadioMode = _CoDevWirIfStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 6),
    _CoDevWirIfStaRadioMode_Type()
)
coDevWirIfStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioMode.setStatus("current")
_CoDevWirIfStaRadioType_Type = ColubrisRadioType
_CoDevWirIfStaRadioType_Object = MibTableColumn
coDevWirIfStaRadioType = _CoDevWirIfStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 7),
    _CoDevWirIfStaRadioType_Type()
)
coDevWirIfStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioType.setStatus("current")
_CoDevWirIfStaRadioOperState_Type = TruthValue
_CoDevWirIfStaRadioOperState_Object = MibTableColumn
coDevWirIfStaRadioOperState = _CoDevWirIfStaRadioOperState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 8),
    _CoDevWirIfStaRadioOperState_Type()
)
coDevWirIfStaRadioOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaRadioOperState.setStatus("current")
_CoDevWirIfStaNumberOfClient_Type = Unsigned32
_CoDevWirIfStaNumberOfClient_Object = MibTableColumn
coDevWirIfStaNumberOfClient = _CoDevWirIfStaNumberOfClient_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 9),
    _CoDevWirIfStaNumberOfClient_Type()
)
coDevWirIfStaNumberOfClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaNumberOfClient.setStatus("current")
_CoDevWirIfStaAutoChannelEnabled_Type = TruthValue
_CoDevWirIfStaAutoChannelEnabled_Object = MibTableColumn
coDevWirIfStaAutoChannelEnabled = _CoDevWirIfStaAutoChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 11),
    _CoDevWirIfStaAutoChannelInterval_Type()
)
coDevWirIfStaAutoChannelInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaAutoChannelInterval.setStatus("current")
_CoDevWirIfStaAutoPowerEnabled_Type = TruthValue
_CoDevWirIfStaAutoPowerEnabled_Object = MibTableColumn
coDevWirIfStaAutoPowerEnabled = _CoDevWirIfStaAutoPowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 14),
    _CoDevWirIfStaResetStats_Type()
)
coDevWirIfStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirIfStaResetStats.setStatus("current")
_CoDevWirIfStaGreenfieldOptionEnabled_Type = TruthValue
_CoDevWirIfStaGreenfieldOptionEnabled_Object = MibTableColumn
coDevWirIfStaGreenfieldOptionEnabled = _CoDevWirIfStaGreenfieldOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 15),
    _CoDevWirIfStaGreenfieldOptionEnabled_Type()
)
coDevWirIfStaGreenfieldOptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaGreenfieldOptionEnabled.setStatus("current")
_CoDevWirIfStaNbDetectedStation_Type = Unsigned32
_CoDevWirIfStaNbDetectedStation_Object = MibTableColumn
coDevWirIfStaNbDetectedStation = _CoDevWirIfStaNbDetectedStation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 2, 1, 1, 16),
    _CoDevWirIfStaNbDetectedStation_Type()
)
coDevWirIfStaNbDetectedStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStaNbDetectedStation.setStatus("current")
_CoDeviceWirelessIfStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfStatsGroup = _CoDeviceWirelessIfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3)
)
_CoDeviceWirelessInterfaceStatsTable_Object = MibTable
coDeviceWirelessInterfaceStatsTable = _CoDeviceWirelessInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatsTable.setStatus("current")
_CoDeviceWirelessInterfaceStatsEntry_Object = MibTableRow
coDeviceWirelessInterfaceStatsEntry = _CoDeviceWirelessInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessInterfaceStatsEntry.setStatus("current")
_CoDevWirIfStsTransmittedFragmentCount_Type = Counter32
_CoDevWirIfStsTransmittedFragmentCount_Object = MibTableColumn
coDevWirIfStsTransmittedFragmentCount = _CoDevWirIfStsTransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 1),
    _CoDevWirIfStsTransmittedFragmentCount_Type()
)
coDevWirIfStsTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsTransmittedFragmentCount.setStatus("current")
_CoDevWirIfStsMulticastTransmittedFrameCount_Type = Counter32
_CoDevWirIfStsMulticastTransmittedFrameCount_Object = MibTableColumn
coDevWirIfStsMulticastTransmittedFrameCount = _CoDevWirIfStsMulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 2),
    _CoDevWirIfStsMulticastTransmittedFrameCount_Type()
)
coDevWirIfStsMulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMulticastTransmittedFrameCount.setStatus("current")
_CoDevWirIfStsFailedCount_Type = Counter32
_CoDevWirIfStsFailedCount_Object = MibTableColumn
coDevWirIfStsFailedCount = _CoDevWirIfStsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 3),
    _CoDevWirIfStsFailedCount_Type()
)
coDevWirIfStsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFailedCount.setStatus("current")
_CoDevWirIfStsRetryCount_Type = Counter32
_CoDevWirIfStsRetryCount_Object = MibTableColumn
coDevWirIfStsRetryCount = _CoDevWirIfStsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 5),
    _CoDevWirIfStsMultipleRetryCount_Type()
)
coDevWirIfStsMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMultipleRetryCount.setStatus("current")
_CoDevWirIfStsFrameDuplicateCount_Type = Counter32
_CoDevWirIfStsFrameDuplicateCount_Object = MibTableColumn
coDevWirIfStsFrameDuplicateCount = _CoDevWirIfStsFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 6),
    _CoDevWirIfStsFrameDuplicateCount_Type()
)
coDevWirIfStsFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFrameDuplicateCount.setStatus("current")
_CoDevWirIfStsRTSSuccessCount_Type = Counter32
_CoDevWirIfStsRTSSuccessCount_Object = MibTableColumn
coDevWirIfStsRTSSuccessCount = _CoDevWirIfStsRTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 7),
    _CoDevWirIfStsRTSSuccessCount_Type()
)
coDevWirIfStsRTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsRTSSuccessCount.setStatus("current")
_CoDevWirIfStsRTSFailureCount_Type = Counter32
_CoDevWirIfStsRTSFailureCount_Object = MibTableColumn
coDevWirIfStsRTSFailureCount = _CoDevWirIfStsRTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 8),
    _CoDevWirIfStsRTSFailureCount_Type()
)
coDevWirIfStsRTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsRTSFailureCount.setStatus("current")
_CoDevWirIfStsACKFailureCount_Type = Counter32
_CoDevWirIfStsACKFailureCount_Object = MibTableColumn
coDevWirIfStsACKFailureCount = _CoDevWirIfStsACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 9),
    _CoDevWirIfStsACKFailureCount_Type()
)
coDevWirIfStsACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsACKFailureCount.setStatus("current")
_CoDevWirIfStsReceivedFragmentCount_Type = Counter32
_CoDevWirIfStsReceivedFragmentCount_Object = MibTableColumn
coDevWirIfStsReceivedFragmentCount = _CoDevWirIfStsReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 10),
    _CoDevWirIfStsReceivedFragmentCount_Type()
)
coDevWirIfStsReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsReceivedFragmentCount.setStatus("current")
_CoDevWirIfStsMulticastReceivedFrameCount_Type = Counter32
_CoDevWirIfStsMulticastReceivedFrameCount_Object = MibTableColumn
coDevWirIfStsMulticastReceivedFrameCount = _CoDevWirIfStsMulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 11),
    _CoDevWirIfStsMulticastReceivedFrameCount_Type()
)
coDevWirIfStsMulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsMulticastReceivedFrameCount.setStatus("current")
_CoDevWirIfStsFCSErrorCount_Type = Counter32
_CoDevWirIfStsFCSErrorCount_Object = MibTableColumn
coDevWirIfStsFCSErrorCount = _CoDevWirIfStsFCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 12),
    _CoDevWirIfStsFCSErrorCount_Type()
)
coDevWirIfStsFCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsFCSErrorCount.setStatus("current")
_CoDevWirIfStsTransmittedFrameCount_Type = Counter32
_CoDevWirIfStsTransmittedFrameCount_Object = MibTableColumn
coDevWirIfStsTransmittedFrameCount = _CoDevWirIfStsTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 13),
    _CoDevWirIfStsTransmittedFrameCount_Type()
)
coDevWirIfStsTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsTransmittedFrameCount.setStatus("current")
_CoDevWirIfStsReceivedFrameCount_Type = Counter32
_CoDevWirIfStsReceivedFrameCount_Object = MibTableColumn
coDevWirIfStsReceivedFrameCount = _CoDevWirIfStsReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 3, 1, 1, 14),
    _CoDevWirIfStsReceivedFrameCount_Type()
)
coDevWirIfStsReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirIfStsReceivedFrameCount.setStatus("current")
_CoDeviceWirelessIfQosGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessIfQosGroup = _CoDeviceWirelessIfQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 4)
)
_CoDeviceWirelessVscStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessVscStatusGroup = _CoDeviceWirelessVscStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5)
)
_CoDeviceWirelessVscStatusTable_Object = MibTable
coDeviceWirelessVscStatusTable = _CoDeviceWirelessVscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatusTable.setStatus("current")
_CoDeviceWirelessVscStatusEntry_Object = MibTableRow
coDeviceWirelessVscStatusEntry = _CoDeviceWirelessVscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1)
)
coDeviceWirelessVscStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaVscIndex"),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 2),
    _CoDevWirVscStaMscVscIndex_Type()
)
coDevWirVscStaMscVscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaMscVscIndex.setStatus("current")
_CoDevWirVscStaBSSID_Type = MacAddress
_CoDevWirVscStaBSSID_Object = MibTableColumn
coDevWirVscStaBSSID = _CoDevWirVscStaBSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 4),
    _CoDevWirVscStaDefaultVLAN_Type()
)
coDevWirVscStaDefaultVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaDefaultVLAN.setStatus("current")
_CoDevWirVscStaMaximumNumberOfUsers_Type = Unsigned32
_CoDevWirVscStaMaximumNumberOfUsers_Object = MibTableColumn
coDevWirVscStaMaximumNumberOfUsers = _CoDevWirVscStaMaximumNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 5),
    _CoDevWirVscStaMaximumNumberOfUsers_Type()
)
coDevWirVscStaMaximumNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStaMaximumNumberOfUsers.setStatus("current")
_CoDevWirVscStaCurrentNumberOfUsers_Type = Unsigned32
_CoDevWirVscStaCurrentNumberOfUsers_Object = MibTableColumn
coDevWirVscStaCurrentNumberOfUsers = _CoDevWirVscStaCurrentNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 5, 1, 1, 8),
    _CoDevWirVscStaResetStats_Type()
)
coDevWirVscStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirVscStaResetStats.setStatus("current")
_CoDeviceWirelessVscStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessVscStatsGroup = _CoDeviceWirelessVscStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6)
)
_CoDeviceWirelessVscStatsTable_Object = MibTable
coDeviceWirelessVscStatsTable = _CoDeviceWirelessVscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatsTable.setStatus("current")
_CoDeviceWirelessVscStatsEntry_Object = MibTableRow
coDeviceWirelessVscStatsEntry = _CoDeviceWirelessVscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessVscStatsEntry.setStatus("current")
_CoDevWirVscStsTxSecurityFilter_Type = Counter32
_CoDevWirVscStsTxSecurityFilter_Object = MibTableColumn
coDevWirVscStsTxSecurityFilter = _CoDevWirVscStsTxSecurityFilter_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 1),
    _CoDevWirVscStsTxSecurityFilter_Type()
)
coDevWirVscStsTxSecurityFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTxSecurityFilter.setStatus("current")
_CoDevWirVscStsRxSecurityFilter_Type = Counter32
_CoDevWirVscStsRxSecurityFilter_Object = MibTableColumn
coDevWirVscStsRxSecurityFilter = _CoDevWirVscStsRxSecurityFilter_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 2),
    _CoDevWirVscStsRxSecurityFilter_Type()
)
coDevWirVscStsRxSecurityFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsRxSecurityFilter.setStatus("current")
_CoDevWirVscStsWEPICVError_Type = Counter32
_CoDevWirVscStsWEPICVError_Object = MibTableColumn
coDevWirVscStsWEPICVError = _CoDevWirVscStsWEPICVError_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 3),
    _CoDevWirVscStsWEPICVError_Type()
)
coDevWirVscStsWEPICVError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsWEPICVError.setStatus("current")
_CoDevWirVscStsWEPExcluded_Type = Counter32
_CoDevWirVscStsWEPExcluded_Object = MibTableColumn
coDevWirVscStsWEPExcluded = _CoDevWirVscStsWEPExcluded_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 4),
    _CoDevWirVscStsWEPExcluded_Type()
)
coDevWirVscStsWEPExcluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsWEPExcluded.setStatus("current")
_CoDevWirVscStsTKIPICVError_Type = Counter32
_CoDevWirVscStsTKIPICVError_Object = MibTableColumn
coDevWirVscStsTKIPICVError = _CoDevWirVscStsTKIPICVError_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 5),
    _CoDevWirVscStsTKIPICVError_Type()
)
coDevWirVscStsTKIPICVError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPICVError.setStatus("current")
_CoDevWirVscStsTKIPMICError_Type = Counter32
_CoDevWirVscStsTKIPMICError_Object = MibTableColumn
coDevWirVscStsTKIPMICError = _CoDevWirVscStsTKIPMICError_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 6),
    _CoDevWirVscStsTKIPMICError_Type()
)
coDevWirVscStsTKIPMICError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPMICError.setStatus("current")
_CoDevWirVscStsTKIPCounterMeasure_Type = Counter32
_CoDevWirVscStsTKIPCounterMeasure_Object = MibTableColumn
coDevWirVscStsTKIPCounterMeasure = _CoDevWirVscStsTKIPCounterMeasure_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 7),
    _CoDevWirVscStsTKIPCounterMeasure_Type()
)
coDevWirVscStsTKIPCounterMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPCounterMeasure.setStatus("current")
_CoDevWirVscStsTKIPReplay_Type = Counter32
_CoDevWirVscStsTKIPReplay_Object = MibTableColumn
coDevWirVscStsTKIPReplay = _CoDevWirVscStsTKIPReplay_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 8),
    _CoDevWirVscStsTKIPReplay_Type()
)
coDevWirVscStsTKIPReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsTKIPReplay.setStatus("current")
_CoDevWirVscStsAESError_Type = Counter32
_CoDevWirVscStsAESError_Object = MibTableColumn
coDevWirVscStsAESError = _CoDevWirVscStsAESError_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 9),
    _CoDevWirVscStsAESError_Type()
)
coDevWirVscStsAESError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsAESError.setStatus("current")
_CoDevWirVscStsAESReplay_Type = Counter32
_CoDevWirVscStsAESReplay_Object = MibTableColumn
coDevWirVscStsAESReplay = _CoDevWirVscStsAESReplay_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 6, 1, 1, 10),
    _CoDevWirVscStsAESReplay_Type()
)
coDevWirVscStsAESReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirVscStsAESReplay.setStatus("current")
_CoDeviceWirelessClientStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientStatusGroup = _CoDeviceWirelessClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7)
)
_CoDeviceWirelessClientStatusTable_Object = MibTable
coDeviceWirelessClientStatusTable = _CoDeviceWirelessClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatusTable.setStatus("current")
_CoDeviceWirelessClientStatusEntry_Object = MibTableRow
coDeviceWirelessClientStatusEntry = _CoDeviceWirelessClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1)
)
coDeviceWirelessClientStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaIndex"),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 1),
    _CoDevWirCliStaIndex_Type()
)
coDevWirCliStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirCliStaIndex.setStatus("current")
_CoDevWirCliStaMACAddress_Type = MacAddress
_CoDevWirCliStaMACAddress_Object = MibTableColumn
coDevWirCliStaMACAddress = _CoDevWirCliStaMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 2),
    _CoDevWirCliStaMACAddress_Type()
)
coDevWirCliStaMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaMACAddress.setStatus("current")
_CoDevWirCliStaVscIndex_Type = Integer32
_CoDevWirCliStaVscIndex_Object = MibTableColumn
coDevWirCliStaVscIndex = _CoDevWirCliStaVscIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 3),
    _CoDevWirCliStaVscIndex_Type()
)
coDevWirCliStaVscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaVscIndex.setStatus("current")
_CoDevWirCliStaConnectTime_Type = Counter32
_CoDevWirCliStaConnectTime_Object = MibTableColumn
coDevWirCliStaConnectTime = _CoDevWirCliStaConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 8),
    _CoDevWirCliStaVLAN_Type()
)
coDevWirCliStaVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaVLAN.setStatus("current")
_CoDevWirCliStaTransmitRate_Type = Unsigned32
_CoDevWirCliStaTransmitRate_Object = MibTableColumn
coDevWirCliStaTransmitRate = _CoDevWirCliStaTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 9),
    _CoDevWirCliStaTransmitRate_Type()
)
coDevWirCliStaTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaTransmitRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirCliStaTransmitRate.setUnits("500Kb/s")
_CoDevWirCliStaReceiveRate_Type = Unsigned32
_CoDevWirCliStaReceiveRate_Object = MibTableColumn
coDevWirCliStaReceiveRate = _CoDevWirCliStaReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 10),
    _CoDevWirCliStaReceiveRate_Type()
)
coDevWirCliStaReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirCliStaReceiveRate.setUnits("500Kb/s")
_CoDevWirCliStaTrafficAuthorized_Type = TruthValue
_CoDevWirCliStaTrafficAuthorized_Object = MibTableColumn
coDevWirCliStaTrafficAuthorized = _CoDevWirCliStaTrafficAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 11),
    _CoDevWirCliStaTrafficAuthorized_Type()
)
coDevWirCliStaTrafficAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaTrafficAuthorized.setStatus("current")
_CoDevWirCliSta8021xAuthenticated_Type = TruthValue
_CoDevWirCliSta8021xAuthenticated_Object = MibTableColumn
coDevWirCliSta8021xAuthenticated = _CoDevWirCliSta8021xAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 12),
    _CoDevWirCliSta8021xAuthenticated_Type()
)
coDevWirCliSta8021xAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliSta8021xAuthenticated.setStatus("current")
_CoDevWirCliStaMACAuthenticated_Type = TruthValue
_CoDevWirCliStaMACAuthenticated_Object = MibTableColumn
coDevWirCliStaMACAuthenticated = _CoDevWirCliStaMACAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 13),
    _CoDevWirCliStaMACAuthenticated_Type()
)
coDevWirCliStaMACAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaMACAuthenticated.setStatus("current")
_CoDevWirCliStaMACFiltered_Type = TruthValue
_CoDevWirCliStaMACFiltered_Object = MibTableColumn
coDevWirCliStaMACFiltered = _CoDevWirCliStaMACFiltered_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 14),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11bAndg", 4),
          ("ieee802dot11g", 3),
          ("ieee802dot11n", 5))
    )


_CoDevWirCliStaPhyType_Type.__name__ = "Integer32"
_CoDevWirCliStaPhyType_Object = MibTableColumn
coDevWirCliStaPhyType = _CoDevWirCliStaPhyType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 16),
    _CoDevWirCliStaWPAType_Type()
)
coDevWirCliStaWPAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaWPAType.setStatus("current")
_CoDevWirCliStaIpAddress_Type = IpAddress
_CoDevWirCliStaIpAddress_Object = MibTableColumn
coDevWirCliStaIpAddress = _CoDevWirCliStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 17),
    _CoDevWirCliStaIpAddress_Type()
)
coDevWirCliStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaIpAddress.setStatus("current")
_CoDevWirCliStaPowerSavingMode_Type = TruthValue
_CoDevWirCliStaPowerSavingMode_Object = MibTableColumn
coDevWirCliStaPowerSavingMode = _CoDevWirCliStaPowerSavingMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 18),
    _CoDevWirCliStaPowerSavingMode_Type()
)
coDevWirCliStaPowerSavingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaPowerSavingMode.setStatus("current")
_CoDevWirCliStaWME_Type = TruthValue
_CoDevWirCliStaWME_Object = MibTableColumn
coDevWirCliStaWME = _CoDevWirCliStaWME_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 19),
    _CoDevWirCliStaWME_Type()
)
coDevWirCliStaWME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaWME.setStatus("current")
_CoDevWirCliStaPreviousAPAddress_Type = MacAddress
_CoDevWirCliStaPreviousAPAddress_Object = MibTableColumn
coDevWirCliStaPreviousAPAddress = _CoDevWirCliStaPreviousAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 21),
    _CoDevWirCliStaResetStats_Type()
)
coDevWirCliStaResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirCliStaResetStats.setStatus("current")
_CoDevWirCliStaHT_Type = TruthValue
_CoDevWirCliStaHT_Object = MibTableColumn
coDevWirCliStaHT = _CoDevWirCliStaHT_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 22),
    _CoDevWirCliStaHT_Type()
)
coDevWirCliStaHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaHT.setStatus("current")
_CoDevWirCliStaTransmitMCS_Type = Unsigned32
_CoDevWirCliStaTransmitMCS_Object = MibTableColumn
coDevWirCliStaTransmitMCS = _CoDevWirCliStaTransmitMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 23),
    _CoDevWirCliStaTransmitMCS_Type()
)
coDevWirCliStaTransmitMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaTransmitMCS.setStatus("current")
_CoDevWirCliStaReceiveMCS_Type = Unsigned32
_CoDevWirCliStaReceiveMCS_Object = MibTableColumn
coDevWirCliStaReceiveMCS = _CoDevWirCliStaReceiveMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 24),
    _CoDevWirCliStaReceiveMCS_Type()
)
coDevWirCliStaReceiveMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaReceiveMCS.setStatus("current")


class _CoDevWirCliStaChannelWidth_Type(Integer32):
    """Custom type coDevWirCliStaChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw20MHz", 1),
          ("cw40MHz", 2))
    )


_CoDevWirCliStaChannelWidth_Type.__name__ = "Integer32"
_CoDevWirCliStaChannelWidth_Object = MibTableColumn
coDevWirCliStaChannelWidth = _CoDevWirCliStaChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 25),
    _CoDevWirCliStaChannelWidth_Type()
)
coDevWirCliStaChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaChannelWidth.setStatus("current")
_CoDevWirCliStaShortGI_Type = TruthValue
_CoDevWirCliStaShortGI_Object = MibTableColumn
coDevWirCliStaShortGI = _CoDevWirCliStaShortGI_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 26),
    _CoDevWirCliStaShortGI_Type()
)
coDevWirCliStaShortGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStaShortGI.setStatus("current")


class _CoDevWirCliDisassociate_Type(Integer32):
    """Custom type coDevWirCliDisassociate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disassociate", 1),
          ("idle", 0))
    )


_CoDevWirCliDisassociate_Type.__name__ = "Integer32"
_CoDevWirCliDisassociate_Object = MibTableColumn
coDevWirCliDisassociate = _CoDevWirCliDisassociate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 1, 1, 27),
    _CoDevWirCliDisassociate_Type()
)
coDevWirCliDisassociate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevWirCliDisassociate.setStatus("current")
_CoDevWirNbAssociatedStation_Type = Unsigned32
_CoDevWirNbAssociatedStation_Object = MibScalar
coDevWirNbAssociatedStation = _CoDevWirNbAssociatedStation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 7, 2),
    _CoDevWirNbAssociatedStation_Type()
)
coDevWirNbAssociatedStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirNbAssociatedStation.setStatus("current")
_CoDeviceWirelessClientStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientStatsGroup = _CoDeviceWirelessClientStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8)
)
_CoDeviceWirelessClientStatsTable_Object = MibTable
coDeviceWirelessClientStatsTable = _CoDeviceWirelessClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsTable.setStatus("current")
_CoDeviceWirelessClientStatsEntry_Object = MibTableRow
coDeviceWirelessClientStatsEntry = _CoDeviceWirelessClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsEntry.setStatus("current")
_CoDevWirCliStsInPkts_Type = Counter32
_CoDevWirCliStsInPkts_Object = MibTableColumn
coDevWirCliStsInPkts = _CoDevWirCliStsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1, 1, 1),
    _CoDevWirCliStsInPkts_Type()
)
coDevWirCliStsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsInPkts.setStatus("current")
_CoDevWirCliStsOutPkts_Type = Counter32
_CoDevWirCliStsOutPkts_Object = MibTableColumn
coDevWirCliStsOutPkts = _CoDevWirCliStsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1, 1, 2),
    _CoDevWirCliStsOutPkts_Type()
)
coDevWirCliStsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsOutPkts.setStatus("current")
_CoDevWirCliStsInOctets_Type = Counter64
_CoDevWirCliStsInOctets_Object = MibTableColumn
coDevWirCliStsInOctets = _CoDevWirCliStsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1, 1, 3),
    _CoDevWirCliStsInOctets_Type()
)
coDevWirCliStsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsInOctets.setStatus("current")
_CoDevWirCliStsOutOctets_Type = Counter64
_CoDevWirCliStsOutOctets_Object = MibTableColumn
coDevWirCliStsOutOctets = _CoDevWirCliStsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 8, 1, 1, 4),
    _CoDevWirCliStsOutOctets_Type()
)
coDevWirCliStsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsOutOctets.setStatus("current")
_CoDeviceWirelessClientRatesGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientRatesGroup = _CoDeviceWirelessClientRatesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9)
)
_CoDeviceWirelessClientStatsRatesTable_Object = MibTable
coDeviceWirelessClientStatsRatesTable = _CoDeviceWirelessClientStatsRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsRatesTable.setStatus("current")
_CoDeviceWirelessClientStatsRatesEntry_Object = MibTableRow
coDeviceWirelessClientStatsRatesEntry = _CoDeviceWirelessClientStatsRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsRatesEntry.setStatus("current")
_CoDevWirCliStsPktsTxRate1_Type = Counter32
_CoDevWirCliStsPktsTxRate1_Object = MibTableColumn
coDevWirCliStsPktsTxRate1 = _CoDevWirCliStsPktsTxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 1),
    _CoDevWirCliStsPktsTxRate1_Type()
)
coDevWirCliStsPktsTxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate1.setStatus("current")
_CoDevWirCliStsPktsTxRate2_Type = Counter32
_CoDevWirCliStsPktsTxRate2_Object = MibTableColumn
coDevWirCliStsPktsTxRate2 = _CoDevWirCliStsPktsTxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 2),
    _CoDevWirCliStsPktsTxRate2_Type()
)
coDevWirCliStsPktsTxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate2.setStatus("current")
_CoDevWirCliStsPktsTxRate5dot5_Type = Counter32
_CoDevWirCliStsPktsTxRate5dot5_Object = MibTableColumn
coDevWirCliStsPktsTxRate5dot5 = _CoDevWirCliStsPktsTxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 3),
    _CoDevWirCliStsPktsTxRate5dot5_Type()
)
coDevWirCliStsPktsTxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate5dot5.setStatus("current")
_CoDevWirCliStsPktsTxRate11_Type = Counter32
_CoDevWirCliStsPktsTxRate11_Object = MibTableColumn
coDevWirCliStsPktsTxRate11 = _CoDevWirCliStsPktsTxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 4),
    _CoDevWirCliStsPktsTxRate11_Type()
)
coDevWirCliStsPktsTxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate11.setStatus("current")
_CoDevWirCliStsPktsTxRate6_Type = Counter32
_CoDevWirCliStsPktsTxRate6_Object = MibTableColumn
coDevWirCliStsPktsTxRate6 = _CoDevWirCliStsPktsTxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 5),
    _CoDevWirCliStsPktsTxRate6_Type()
)
coDevWirCliStsPktsTxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate6.setStatus("current")
_CoDevWirCliStsPktsTxRate9_Type = Counter32
_CoDevWirCliStsPktsTxRate9_Object = MibTableColumn
coDevWirCliStsPktsTxRate9 = _CoDevWirCliStsPktsTxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 6),
    _CoDevWirCliStsPktsTxRate9_Type()
)
coDevWirCliStsPktsTxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate9.setStatus("current")
_CoDevWirCliStsPktsTxRate12_Type = Counter32
_CoDevWirCliStsPktsTxRate12_Object = MibTableColumn
coDevWirCliStsPktsTxRate12 = _CoDevWirCliStsPktsTxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 7),
    _CoDevWirCliStsPktsTxRate12_Type()
)
coDevWirCliStsPktsTxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate12.setStatus("current")
_CoDevWirCliStsPktsTxRate18_Type = Counter32
_CoDevWirCliStsPktsTxRate18_Object = MibTableColumn
coDevWirCliStsPktsTxRate18 = _CoDevWirCliStsPktsTxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 8),
    _CoDevWirCliStsPktsTxRate18_Type()
)
coDevWirCliStsPktsTxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate18.setStatus("current")
_CoDevWirCliStsPktsTxRate24_Type = Counter32
_CoDevWirCliStsPktsTxRate24_Object = MibTableColumn
coDevWirCliStsPktsTxRate24 = _CoDevWirCliStsPktsTxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 9),
    _CoDevWirCliStsPktsTxRate24_Type()
)
coDevWirCliStsPktsTxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate24.setStatus("current")
_CoDevWirCliStsPktsTxRate36_Type = Counter32
_CoDevWirCliStsPktsTxRate36_Object = MibTableColumn
coDevWirCliStsPktsTxRate36 = _CoDevWirCliStsPktsTxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 10),
    _CoDevWirCliStsPktsTxRate36_Type()
)
coDevWirCliStsPktsTxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate36.setStatus("current")
_CoDevWirCliStsPktsTxRate48_Type = Counter32
_CoDevWirCliStsPktsTxRate48_Object = MibTableColumn
coDevWirCliStsPktsTxRate48 = _CoDevWirCliStsPktsTxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 11),
    _CoDevWirCliStsPktsTxRate48_Type()
)
coDevWirCliStsPktsTxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate48.setStatus("current")
_CoDevWirCliStsPktsTxRate54_Type = Counter32
_CoDevWirCliStsPktsTxRate54_Object = MibTableColumn
coDevWirCliStsPktsTxRate54 = _CoDevWirCliStsPktsTxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 12),
    _CoDevWirCliStsPktsTxRate54_Type()
)
coDevWirCliStsPktsTxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxRate54.setStatus("current")
_CoDevWirCliStsPktsRxRate1_Type = Counter32
_CoDevWirCliStsPktsRxRate1_Object = MibTableColumn
coDevWirCliStsPktsRxRate1 = _CoDevWirCliStsPktsRxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 13),
    _CoDevWirCliStsPktsRxRate1_Type()
)
coDevWirCliStsPktsRxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate1.setStatus("current")
_CoDevWirCliStsPktsRxRate2_Type = Counter32
_CoDevWirCliStsPktsRxRate2_Object = MibTableColumn
coDevWirCliStsPktsRxRate2 = _CoDevWirCliStsPktsRxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 14),
    _CoDevWirCliStsPktsRxRate2_Type()
)
coDevWirCliStsPktsRxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate2.setStatus("current")
_CoDevWirCliStsPktsRxRate5dot5_Type = Counter32
_CoDevWirCliStsPktsRxRate5dot5_Object = MibTableColumn
coDevWirCliStsPktsRxRate5dot5 = _CoDevWirCliStsPktsRxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 15),
    _CoDevWirCliStsPktsRxRate5dot5_Type()
)
coDevWirCliStsPktsRxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate5dot5.setStatus("current")
_CoDevWirCliStsPktsRxRate11_Type = Counter32
_CoDevWirCliStsPktsRxRate11_Object = MibTableColumn
coDevWirCliStsPktsRxRate11 = _CoDevWirCliStsPktsRxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 16),
    _CoDevWirCliStsPktsRxRate11_Type()
)
coDevWirCliStsPktsRxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate11.setStatus("current")
_CoDevWirCliStsPktsRxRate6_Type = Counter32
_CoDevWirCliStsPktsRxRate6_Object = MibTableColumn
coDevWirCliStsPktsRxRate6 = _CoDevWirCliStsPktsRxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 17),
    _CoDevWirCliStsPktsRxRate6_Type()
)
coDevWirCliStsPktsRxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate6.setStatus("current")
_CoDevWirCliStsPktsRxRate9_Type = Counter32
_CoDevWirCliStsPktsRxRate9_Object = MibTableColumn
coDevWirCliStsPktsRxRate9 = _CoDevWirCliStsPktsRxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 18),
    _CoDevWirCliStsPktsRxRate9_Type()
)
coDevWirCliStsPktsRxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate9.setStatus("current")
_CoDevWirCliStsPktsRxRate12_Type = Counter32
_CoDevWirCliStsPktsRxRate12_Object = MibTableColumn
coDevWirCliStsPktsRxRate12 = _CoDevWirCliStsPktsRxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 19),
    _CoDevWirCliStsPktsRxRate12_Type()
)
coDevWirCliStsPktsRxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate12.setStatus("current")
_CoDevWirCliStsPktsRxRate18_Type = Counter32
_CoDevWirCliStsPktsRxRate18_Object = MibTableColumn
coDevWirCliStsPktsRxRate18 = _CoDevWirCliStsPktsRxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 20),
    _CoDevWirCliStsPktsRxRate18_Type()
)
coDevWirCliStsPktsRxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate18.setStatus("current")
_CoDevWirCliStsPktsRxRate24_Type = Counter32
_CoDevWirCliStsPktsRxRate24_Object = MibTableColumn
coDevWirCliStsPktsRxRate24 = _CoDevWirCliStsPktsRxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 21),
    _CoDevWirCliStsPktsRxRate24_Type()
)
coDevWirCliStsPktsRxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate24.setStatus("current")
_CoDevWirCliStsPktsRxRate36_Type = Counter32
_CoDevWirCliStsPktsRxRate36_Object = MibTableColumn
coDevWirCliStsPktsRxRate36 = _CoDevWirCliStsPktsRxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 22),
    _CoDevWirCliStsPktsRxRate36_Type()
)
coDevWirCliStsPktsRxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate36.setStatus("current")
_CoDevWirCliStsPktsRxRate48_Type = Counter32
_CoDevWirCliStsPktsRxRate48_Object = MibTableColumn
coDevWirCliStsPktsRxRate48 = _CoDevWirCliStsPktsRxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 23),
    _CoDevWirCliStsPktsRxRate48_Type()
)
coDevWirCliStsPktsRxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate48.setStatus("current")
_CoDevWirCliStsPktsRxRate54_Type = Counter32
_CoDevWirCliStsPktsRxRate54_Object = MibTableColumn
coDevWirCliStsPktsRxRate54 = _CoDevWirCliStsPktsRxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 9, 1, 1, 24),
    _CoDevWirCliStsPktsRxRate54_Type()
)
coDevWirCliStsPktsRxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxRate54.setStatus("current")
_CoDeviceWirelessClientHTRatesGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessClientHTRatesGroup = _CoDeviceWirelessClientHTRatesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10)
)
_CoDeviceWirelessClientStatsHTRatesTable_Object = MibTable
coDeviceWirelessClientStatsHTRatesTable = _CoDeviceWirelessClientStatsHTRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsHTRatesTable.setStatus("current")
_CoDeviceWirelessClientStatsHTRatesEntry_Object = MibTableRow
coDeviceWirelessClientStatsHTRatesEntry = _CoDeviceWirelessClientStatsHTRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessClientStatsHTRatesEntry.setStatus("current")
_CoDevWirCliStsPktsTxMCS0_Type = Counter32
_CoDevWirCliStsPktsTxMCS0_Object = MibTableColumn
coDevWirCliStsPktsTxMCS0 = _CoDevWirCliStsPktsTxMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 1),
    _CoDevWirCliStsPktsTxMCS0_Type()
)
coDevWirCliStsPktsTxMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS0.setStatus("current")
_CoDevWirCliStsPktsTxMCS1_Type = Counter32
_CoDevWirCliStsPktsTxMCS1_Object = MibTableColumn
coDevWirCliStsPktsTxMCS1 = _CoDevWirCliStsPktsTxMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 2),
    _CoDevWirCliStsPktsTxMCS1_Type()
)
coDevWirCliStsPktsTxMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS1.setStatus("current")
_CoDevWirCliStsPktsTxMCS2_Type = Counter32
_CoDevWirCliStsPktsTxMCS2_Object = MibTableColumn
coDevWirCliStsPktsTxMCS2 = _CoDevWirCliStsPktsTxMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 3),
    _CoDevWirCliStsPktsTxMCS2_Type()
)
coDevWirCliStsPktsTxMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS2.setStatus("current")
_CoDevWirCliStsPktsTxMCS3_Type = Counter32
_CoDevWirCliStsPktsTxMCS3_Object = MibTableColumn
coDevWirCliStsPktsTxMCS3 = _CoDevWirCliStsPktsTxMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 4),
    _CoDevWirCliStsPktsTxMCS3_Type()
)
coDevWirCliStsPktsTxMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS3.setStatus("current")
_CoDevWirCliStsPktsTxMCS4_Type = Counter32
_CoDevWirCliStsPktsTxMCS4_Object = MibTableColumn
coDevWirCliStsPktsTxMCS4 = _CoDevWirCliStsPktsTxMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 5),
    _CoDevWirCliStsPktsTxMCS4_Type()
)
coDevWirCliStsPktsTxMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS4.setStatus("current")
_CoDevWirCliStsPktsTxMCS5_Type = Counter32
_CoDevWirCliStsPktsTxMCS5_Object = MibTableColumn
coDevWirCliStsPktsTxMCS5 = _CoDevWirCliStsPktsTxMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 6),
    _CoDevWirCliStsPktsTxMCS5_Type()
)
coDevWirCliStsPktsTxMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS5.setStatus("current")
_CoDevWirCliStsPktsTxMCS6_Type = Counter32
_CoDevWirCliStsPktsTxMCS6_Object = MibTableColumn
coDevWirCliStsPktsTxMCS6 = _CoDevWirCliStsPktsTxMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 7),
    _CoDevWirCliStsPktsTxMCS6_Type()
)
coDevWirCliStsPktsTxMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS6.setStatus("current")
_CoDevWirCliStsPktsTxMCS7_Type = Counter32
_CoDevWirCliStsPktsTxMCS7_Object = MibTableColumn
coDevWirCliStsPktsTxMCS7 = _CoDevWirCliStsPktsTxMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 8),
    _CoDevWirCliStsPktsTxMCS7_Type()
)
coDevWirCliStsPktsTxMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS7.setStatus("current")
_CoDevWirCliStsPktsTxMCS8_Type = Counter32
_CoDevWirCliStsPktsTxMCS8_Object = MibTableColumn
coDevWirCliStsPktsTxMCS8 = _CoDevWirCliStsPktsTxMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 9),
    _CoDevWirCliStsPktsTxMCS8_Type()
)
coDevWirCliStsPktsTxMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS8.setStatus("current")
_CoDevWirCliStsPktsTxMCS9_Type = Counter32
_CoDevWirCliStsPktsTxMCS9_Object = MibTableColumn
coDevWirCliStsPktsTxMCS9 = _CoDevWirCliStsPktsTxMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 10),
    _CoDevWirCliStsPktsTxMCS9_Type()
)
coDevWirCliStsPktsTxMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS9.setStatus("current")
_CoDevWirCliStsPktsTxMCS10_Type = Counter32
_CoDevWirCliStsPktsTxMCS10_Object = MibTableColumn
coDevWirCliStsPktsTxMCS10 = _CoDevWirCliStsPktsTxMCS10_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 11),
    _CoDevWirCliStsPktsTxMCS10_Type()
)
coDevWirCliStsPktsTxMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS10.setStatus("current")
_CoDevWirCliStsPktsTxMCS11_Type = Counter32
_CoDevWirCliStsPktsTxMCS11_Object = MibTableColumn
coDevWirCliStsPktsTxMCS11 = _CoDevWirCliStsPktsTxMCS11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 12),
    _CoDevWirCliStsPktsTxMCS11_Type()
)
coDevWirCliStsPktsTxMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS11.setStatus("current")
_CoDevWirCliStsPktsTxMCS12_Type = Counter32
_CoDevWirCliStsPktsTxMCS12_Object = MibTableColumn
coDevWirCliStsPktsTxMCS12 = _CoDevWirCliStsPktsTxMCS12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 13),
    _CoDevWirCliStsPktsTxMCS12_Type()
)
coDevWirCliStsPktsTxMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS12.setStatus("current")
_CoDevWirCliStsPktsTxMCS13_Type = Counter32
_CoDevWirCliStsPktsTxMCS13_Object = MibTableColumn
coDevWirCliStsPktsTxMCS13 = _CoDevWirCliStsPktsTxMCS13_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 14),
    _CoDevWirCliStsPktsTxMCS13_Type()
)
coDevWirCliStsPktsTxMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS13.setStatus("current")
_CoDevWirCliStsPktsTxMCS14_Type = Counter32
_CoDevWirCliStsPktsTxMCS14_Object = MibTableColumn
coDevWirCliStsPktsTxMCS14 = _CoDevWirCliStsPktsTxMCS14_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 15),
    _CoDevWirCliStsPktsTxMCS14_Type()
)
coDevWirCliStsPktsTxMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS14.setStatus("current")
_CoDevWirCliStsPktsTxMCS15_Type = Counter32
_CoDevWirCliStsPktsTxMCS15_Object = MibTableColumn
coDevWirCliStsPktsTxMCS15 = _CoDevWirCliStsPktsTxMCS15_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 16),
    _CoDevWirCliStsPktsTxMCS15_Type()
)
coDevWirCliStsPktsTxMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsTxMCS15.setStatus("current")
_CoDevWirCliStsPktsRxMCS0_Type = Counter32
_CoDevWirCliStsPktsRxMCS0_Object = MibTableColumn
coDevWirCliStsPktsRxMCS0 = _CoDevWirCliStsPktsRxMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 17),
    _CoDevWirCliStsPktsRxMCS0_Type()
)
coDevWirCliStsPktsRxMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS0.setStatus("current")
_CoDevWirCliStsPktsRxMCS1_Type = Counter32
_CoDevWirCliStsPktsRxMCS1_Object = MibTableColumn
coDevWirCliStsPktsRxMCS1 = _CoDevWirCliStsPktsRxMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 18),
    _CoDevWirCliStsPktsRxMCS1_Type()
)
coDevWirCliStsPktsRxMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS1.setStatus("current")
_CoDevWirCliStsPktsRxMCS2_Type = Counter32
_CoDevWirCliStsPktsRxMCS2_Object = MibTableColumn
coDevWirCliStsPktsRxMCS2 = _CoDevWirCliStsPktsRxMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 19),
    _CoDevWirCliStsPktsRxMCS2_Type()
)
coDevWirCliStsPktsRxMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS2.setStatus("current")
_CoDevWirCliStsPktsRxMCS3_Type = Counter32
_CoDevWirCliStsPktsRxMCS3_Object = MibTableColumn
coDevWirCliStsPktsRxMCS3 = _CoDevWirCliStsPktsRxMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 20),
    _CoDevWirCliStsPktsRxMCS3_Type()
)
coDevWirCliStsPktsRxMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS3.setStatus("current")
_CoDevWirCliStsPktsRxMCS4_Type = Counter32
_CoDevWirCliStsPktsRxMCS4_Object = MibTableColumn
coDevWirCliStsPktsRxMCS4 = _CoDevWirCliStsPktsRxMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 21),
    _CoDevWirCliStsPktsRxMCS4_Type()
)
coDevWirCliStsPktsRxMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS4.setStatus("current")
_CoDevWirCliStsPktsRxMCS5_Type = Counter32
_CoDevWirCliStsPktsRxMCS5_Object = MibTableColumn
coDevWirCliStsPktsRxMCS5 = _CoDevWirCliStsPktsRxMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 22),
    _CoDevWirCliStsPktsRxMCS5_Type()
)
coDevWirCliStsPktsRxMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS5.setStatus("current")
_CoDevWirCliStsPktsRxMCS6_Type = Counter32
_CoDevWirCliStsPktsRxMCS6_Object = MibTableColumn
coDevWirCliStsPktsRxMCS6 = _CoDevWirCliStsPktsRxMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 23),
    _CoDevWirCliStsPktsRxMCS6_Type()
)
coDevWirCliStsPktsRxMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS6.setStatus("current")
_CoDevWirCliStsPktsRxMCS7_Type = Counter32
_CoDevWirCliStsPktsRxMCS7_Object = MibTableColumn
coDevWirCliStsPktsRxMCS7 = _CoDevWirCliStsPktsRxMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 24),
    _CoDevWirCliStsPktsRxMCS7_Type()
)
coDevWirCliStsPktsRxMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS7.setStatus("current")
_CoDevWirCliStsPktsRxMCS8_Type = Counter32
_CoDevWirCliStsPktsRxMCS8_Object = MibTableColumn
coDevWirCliStsPktsRxMCS8 = _CoDevWirCliStsPktsRxMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 25),
    _CoDevWirCliStsPktsRxMCS8_Type()
)
coDevWirCliStsPktsRxMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS8.setStatus("current")
_CoDevWirCliStsPktsRxMCS9_Type = Counter32
_CoDevWirCliStsPktsRxMCS9_Object = MibTableColumn
coDevWirCliStsPktsRxMCS9 = _CoDevWirCliStsPktsRxMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 26),
    _CoDevWirCliStsPktsRxMCS9_Type()
)
coDevWirCliStsPktsRxMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS9.setStatus("current")
_CoDevWirCliStsPktsRxMCS10_Type = Counter32
_CoDevWirCliStsPktsRxMCS10_Object = MibTableColumn
coDevWirCliStsPktsRxMCS10 = _CoDevWirCliStsPktsRxMCS10_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 27),
    _CoDevWirCliStsPktsRxMCS10_Type()
)
coDevWirCliStsPktsRxMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS10.setStatus("current")
_CoDevWirCliStsPktsRxMCS11_Type = Counter32
_CoDevWirCliStsPktsRxMCS11_Object = MibTableColumn
coDevWirCliStsPktsRxMCS11 = _CoDevWirCliStsPktsRxMCS11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 28),
    _CoDevWirCliStsPktsRxMCS11_Type()
)
coDevWirCliStsPktsRxMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS11.setStatus("current")
_CoDevWirCliStsPktsRxMCS12_Type = Counter32
_CoDevWirCliStsPktsRxMCS12_Object = MibTableColumn
coDevWirCliStsPktsRxMCS12 = _CoDevWirCliStsPktsRxMCS12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 29),
    _CoDevWirCliStsPktsRxMCS12_Type()
)
coDevWirCliStsPktsRxMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS12.setStatus("current")
_CoDevWirCliStsPktsRxMCS13_Type = Counter32
_CoDevWirCliStsPktsRxMCS13_Object = MibTableColumn
coDevWirCliStsPktsRxMCS13 = _CoDevWirCliStsPktsRxMCS13_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 30),
    _CoDevWirCliStsPktsRxMCS13_Type()
)
coDevWirCliStsPktsRxMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS13.setStatus("current")
_CoDevWirCliStsPktsRxMCS14_Type = Counter32
_CoDevWirCliStsPktsRxMCS14_Object = MibTableColumn
coDevWirCliStsPktsRxMCS14 = _CoDevWirCliStsPktsRxMCS14_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 31),
    _CoDevWirCliStsPktsRxMCS14_Type()
)
coDevWirCliStsPktsRxMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS14.setStatus("current")
_CoDevWirCliStsPktsRxMCS15_Type = Counter32
_CoDevWirCliStsPktsRxMCS15_Object = MibTableColumn
coDevWirCliStsPktsRxMCS15 = _CoDevWirCliStsPktsRxMCS15_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 10, 1, 1, 32),
    _CoDevWirCliStsPktsRxMCS15_Type()
)
coDevWirCliStsPktsRxMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirCliStsPktsRxMCS15.setStatus("current")
_CoDeviceWirelessDetectedAPGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessDetectedAPGroup = _CoDeviceWirelessDetectedAPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13)
)
_CoDeviceWirelessDetectedAPTable_Object = MibTable
coDeviceWirelessDetectedAPTable = _CoDeviceWirelessDetectedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1)
)
if mibBuilder.loadTexts:
    coDeviceWirelessDetectedAPTable.setStatus("current")
_CoDeviceWirelessDetectedAPEntry_Object = MibTableRow
coDeviceWirelessDetectedAPEntry = _CoDeviceWirelessDetectedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1)
)
coDeviceWirelessDetectedAPEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApIndex"),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 1),
    _CoDevWirApIndex_Type()
)
coDevWirApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirApIndex.setStatus("current")
_CoDevWirApBSSID_Type = MacAddress
_CoDevWirApBSSID_Object = MibTableColumn
coDevWirApBSSID = _CoDevWirApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 3),
    _CoDevWirApRadioIndex_Type()
)
coDevWirApRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApRadioIndex.setStatus("current")
_CoDevWirApSSID_Type = ColubrisSSIDOrNone
_CoDevWirApSSID_Object = MibTableColumn
coDevWirApSSID = _CoDevWirApSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 5),
    _CoDevWirApChannel_Type()
)
coDevWirApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApChannel.setStatus("current")
_CoDevWirApSignalLevel_Type = Integer32
_CoDevWirApSignalLevel_Object = MibTableColumn
coDevWirApSignalLevel = _CoDevWirApSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 8),
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
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3),
          ("ieee802dot11na", 4),
          ("ieee802dot11ng", 5))
    )


_CoDevWirApPHYType_Type.__name__ = "Integer32"
_CoDevWirApPHYType_Object = MibTableColumn
coDevWirApPHYType = _CoDevWirApPHYType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 10),
    _CoDevWirApSecurity_Type()
)
coDevWirApSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApSecurity.setStatus("current")


class _CoDevWirApNetworkType_Type(Integer32):
    """Custom type coDevWirApNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ess", 1),
          ("ibss", 2))
    )


_CoDevWirApNetworkType_Type.__name__ = "Integer32"
_CoDevWirApNetworkType_Object = MibTableColumn
coDevWirApNetworkType = _CoDevWirApNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 13, 1, 1, 11),
    _CoDevWirApNetworkType_Type()
)
coDevWirApNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirApNetworkType.setStatus("current")
_CoDeviceWirelessDetectedStationGroup_ObjectIdentity = ObjectIdentity
coDeviceWirelessDetectedStationGroup = _CoDeviceWirelessDetectedStationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14)
)
_CoDevWirNbDetectedStation_Type = Unsigned32
_CoDevWirNbDetectedStation_Object = MibScalar
coDevWirNbDetectedStation = _CoDevWirNbDetectedStation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 1),
    _CoDevWirNbDetectedStation_Type()
)
coDevWirNbDetectedStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirNbDetectedStation.setStatus("current")
_CoDeviceWirelessDetectedStationTable_Object = MibTable
coDeviceWirelessDetectedStationTable = _CoDeviceWirelessDetectedStationTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2)
)
if mibBuilder.loadTexts:
    coDeviceWirelessDetectedStationTable.setStatus("current")
_CoDeviceWirelessDetectedStationEntry_Object = MibTableRow
coDeviceWirelessDetectedStationEntry = _CoDeviceWirelessDetectedStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1)
)
coDeviceWirelessDetectedStationEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirSDetRadioIndex"),
    (0, "COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWirelessDetectedStationEntry.setStatus("current")


class _CoDevWirSDetRadioIndex_Type(Integer32):
    """Custom type coDevWirSDetRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirSDetRadioIndex_Type.__name__ = "Integer32"
_CoDevWirSDetRadioIndex_Object = MibTableColumn
coDevWirSDetRadioIndex = _CoDevWirSDetRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 1),
    _CoDevWirSDetRadioIndex_Type()
)
coDevWirSDetRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirSDetRadioIndex.setStatus("current")


class _CoDevWirDetStaIndex_Type(Integer32):
    """Custom type coDevWirDetStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirDetStaIndex_Type.__name__ = "Integer32"
_CoDevWirDetStaIndex_Object = MibTableColumn
coDevWirDetStaIndex = _CoDevWirDetStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 2),
    _CoDevWirDetStaIndex_Type()
)
coDevWirDetStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWirDetStaIndex.setStatus("current")
_CoDevWirDetStaMacAddress_Type = MacAddress
_CoDevWirDetStaMacAddress_Object = MibTableColumn
coDevWirDetStaMacAddress = _CoDevWirDetStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 3),
    _CoDevWirDetStaMacAddress_Type()
)
coDevWirDetStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaMacAddress.setStatus("current")


class _CoDevWirDetStaChannel_Type(Integer32):
    """Custom type coDevWirDetStaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWirDetStaChannel_Type.__name__ = "Integer32"
_CoDevWirDetStaChannel_Object = MibTableColumn
coDevWirDetStaChannel = _CoDevWirDetStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 4),
    _CoDevWirDetStaChannel_Type()
)
coDevWirDetStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaChannel.setStatus("current")
_CoDevWirDetStaSignalLevel_Type = Integer32
_CoDevWirDetStaSignalLevel_Object = MibTableColumn
coDevWirDetStaSignalLevel = _CoDevWirDetStaSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 5),
    _CoDevWirDetStaSignalLevel_Type()
)
coDevWirDetStaSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirDetStaSignalLevel.setUnits("dBm")
_CoDevWirDetStaNoiseLevel_Type = Integer32
_CoDevWirDetStaNoiseLevel_Object = MibTableColumn
coDevWirDetStaNoiseLevel = _CoDevWirDetStaNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 6),
    _CoDevWirDetStaNoiseLevel_Type()
)
coDevWirDetStaNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirDetStaNoiseLevel.setUnits("dBm")
_CoDevWirDetStaNbProbeReq_Type = Counter32
_CoDevWirDetStaNbProbeReq_Object = MibTableColumn
coDevWirDetStaNbProbeReq = _CoDevWirDetStaNbProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 7),
    _CoDevWirDetStaNbProbeReq_Type()
)
coDevWirDetStaNbProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaNbProbeReq.setStatus("current")
_CoDevWirDetStaRate_Type = Unsigned32
_CoDevWirDetStaRate_Object = MibTableColumn
coDevWirDetStaRate = _CoDevWirDetStaRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 8),
    _CoDevWirDetStaRate_Type()
)
coDevWirDetStaRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirDetStaRate.setUnits("500Kb/s")
_CoDevWirDetStaSSID_Type = ColubrisSSID
_CoDevWirDetStaSSID_Object = MibTableColumn
coDevWirDetStaSSID = _CoDevWirDetStaSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 9),
    _CoDevWirDetStaSSID_Type()
)
coDevWirDetStaSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaSSID.setStatus("current")
_CoDevWirDetStaTimeDiscovered_Type = Counter32
_CoDevWirDetStaTimeDiscovered_Object = MibTableColumn
coDevWirDetStaTimeDiscovered = _CoDevWirDetStaTimeDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 10),
    _CoDevWirDetStaTimeDiscovered_Type()
)
coDevWirDetStaTimeDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaTimeDiscovered.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirDetStaTimeDiscovered.setUnits("seconds")
_CoDevWirDetStaTimeLastSeen_Type = Unsigned32
_CoDevWirDetStaTimeLastSeen_Object = MibTableColumn
coDevWirDetStaTimeLastSeen = _CoDevWirDetStaTimeLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 1, 14, 2, 1, 11),
    _CoDevWirDetStaTimeLastSeen_Type()
)
coDevWirDetStaTimeLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWirDetStaTimeLastSeen.setStatus("current")
if mibBuilder.loadTexts:
    coDevWirDetStaTimeLastSeen.setUnits("seconds")
_ColubrisDeviceWirelessMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBNotificationPrefix = _ColubrisDeviceWirelessMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 2)
)
_ColubrisDeviceWirelessMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBNotifications = _ColubrisDeviceWirelessMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 2, 0)
)
_ColubrisDeviceWirelessMIBConformance_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBConformance = _ColubrisDeviceWirelessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3)
)
_ColubrisDeviceWirelessMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBCompliances = _ColubrisDeviceWirelessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 1)
)
_ColubrisDeviceWirelessMIBGroups_ObjectIdentity = ObjectIdentity
colubrisDeviceWirelessMIBGroups = _ColubrisDeviceWirelessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2)
)
coDeviceWirelessInterfaceStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessInterfaceStatsEntry")
)
coDeviceWirelessInterfaceStatsEntry.setIndexNames(*coDeviceWirelessInterfaceStatusEntry.getIndexNames())
coDeviceWirelessVscStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessVscStatsEntry")
)
coDeviceWirelessVscStatsEntry.setIndexNames(*coDeviceWirelessVscStatusEntry.getIndexNames())
coDeviceWirelessClientStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessClientStatsEntry")
)
coDeviceWirelessClientStatsEntry.setIndexNames(*coDeviceWirelessClientStatusEntry.getIndexNames())
coDeviceWirelessClientStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessClientStatsRatesEntry")
)
coDeviceWirelessClientStatsRatesEntry.setIndexNames(*coDeviceWirelessClientStatusEntry.getIndexNames())
coDeviceWirelessClientStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WIRELESS-MIB",
     "coDeviceWirelessClientStatsHTRatesEntry")
)
coDeviceWirelessClientStatsHTRatesEntry.setIndexNames(*coDeviceWirelessClientStatusEntry.getIndexNames())

# Managed Objects groups

colubrisDeviceWirelessConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 1)
)
colubrisDeviceWirelessConfigMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirSNRLevelNotificationEnabled"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirSNRLevelNotificationInterval"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirMinimumSNRLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirAssociationNotificationEnabled"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessConfigMIBGroup.setStatus("current")

colubrisDeviceWirelessIfStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 2)
)
colubrisDeviceWirelessIfStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaIfIndex"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaOperatingMode"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaTransmitPower"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaOperatingChannel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioMode"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioType"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaRadioOperState"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaNumberOfClient"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoChannelEnabled"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoChannelInterval"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoPowerEnabled"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaAutoPowerInterval"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaResetStats"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaGreenfieldOptionEnabled"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStaNbDetectedStation"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessIfStatusMIBGroup.setStatus("current")

colubrisDeviceWirelessIfStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 3)
)
colubrisDeviceWirelessIfStatsMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsTransmittedFragmentCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsMulticastTransmittedFrameCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsFailedCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsRetryCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsMultipleRetryCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsFrameDuplicateCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsRTSSuccessCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsRTSFailureCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsACKFailureCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsReceivedFragmentCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsMulticastReceivedFrameCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsFCSErrorCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsTransmittedFrameCount"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirIfStsReceivedFrameCount"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessIfStatsMIBGroup.setStatus("current")

colubrisDeviceVscStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 4)
)
colubrisDeviceVscStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaDefaultVLAN"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaMaximumNumberOfUsers"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaCurrentNumberOfUsers"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaAverageSNR"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaResetStats"))
)
if mibBuilder.loadTexts:
    colubrisDeviceVscStatusMIBGroup.setStatus("current")

colubrisDeviceVscStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 5)
)
colubrisDeviceVscStatsMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsTxSecurityFilter"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsRxSecurityFilter"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsWEPICVError"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsWEPExcluded"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPICVError"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPMICError"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPCounterMeasure"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsTKIPReplay"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsAESError"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStsAESReplay"))
)
if mibBuilder.loadTexts:
    colubrisDeviceVscStatsMIBGroup.setStatus("current")

colubrisDeviceWirelessClientStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 6)
)
colubrisDeviceWirelessClientStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAddress"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaVscIndex"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaConnectTime"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaSignalLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaNoiseLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaSNR"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaVLAN"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaTransmitRate"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaReceiveRate"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaTrafficAuthorized"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliSta8021xAuthenticated"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAuthenticated"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACFiltered"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaPhyType"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaWPAType"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaIpAddress"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaPowerSavingMode"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaWME"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaPreviousAPAddress"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaResetStats"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaHT"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaTransmitMCS"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaReceiveMCS"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaChannelWidth"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaShortGI"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliDisassociate"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirNbAssociatedStation"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessClientStatusMIBGroup.setStatus("current")

colubrisDeviceWirelessClientStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 7)
)
colubrisDeviceWirelessClientStatsMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsInPkts"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsOutPkts"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsInOctets"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsOutOctets"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessClientStatsMIBGroup.setStatus("current")

colubrisDeviceWirelessClientStatsRatesMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 8)
)
colubrisDeviceWirelessClientStatsRatesMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate1"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate2"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate5dot5"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate11"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate6"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate9"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate12"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate18"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate24"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate36"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate48"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxRate54"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate1"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate2"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate5dot5"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate11"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate6"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate9"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate12"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate18"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate24"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate36"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate48"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxRate54"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessClientStatsRatesMIBGroup.setStatus("current")

colubrisDeviceWirelessDetectedAPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 9)
)
colubrisDeviceWirelessDetectedAPMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApBSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApRadioIndex"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApChannel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApSignalLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApNoiseLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApSNR"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApPHYType"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApSecurity"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirApNetworkType"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessDetectedAPMIBGroup.setStatus("current")

colubrisDeviceWirelessClientStatsHTRatesMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 11)
)
colubrisDeviceWirelessClientStatsHTRatesMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS0"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS1"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS2"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS3"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS4"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS5"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS6"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS7"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS8"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS9"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS10"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS11"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS12"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS13"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS14"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsTxMCS15"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS0"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS1"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS2"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS3"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS4"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS5"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS6"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS7"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS8"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS9"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS10"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS11"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS12"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS13"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS14"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStsPktsRxMCS15"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessClientStatsHTRatesMIBGroup.setStatus("current")

colubrisDeviceWirelessDetectedStationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 12)
)
colubrisDeviceWirelessDetectedStationMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirNbDetectedStation"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaMacAddress"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaChannel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaSignalLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaNoiseLevel"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaNbProbeReq"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaRate"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaTimeDiscovered"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirDetStaTimeLastSeen"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessDetectedStationMIBGroup.setStatus("current")


# Notification objects

coDeviceWirelessSNRLevelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 2, 0, 1)
)
coDeviceWirelessSNRLevelNotification.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaAverageSNR"))
)
if mibBuilder.loadTexts:
    coDeviceWirelessSNRLevelNotification.setStatus(
        "current"
    )

coDeviceWirelessAssociationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 2, 0, 2)
)
coDeviceWirelessAssociationNotification.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirCliStaMACAddress"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaBSSID"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDevWirVscStaMscVscIndex"))
)
if mibBuilder.loadTexts:
    coDeviceWirelessAssociationNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisDeviceWirelessNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 2, 10)
)
colubrisDeviceWirelessNotificationGroup.setObjects(
      *(("COLUBRIS-DEVICE-WIRELESS-MIB", "coDeviceWirelessSNRLevelNotification"),
        ("COLUBRIS-DEVICE-WIRELESS-MIB", "coDeviceWirelessAssociationNotification"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisDeviceWirelessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisDeviceWirelessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-DEVICE-WIRELESS-MIB",
    **{"colubrisDeviceWirelessMIB": colubrisDeviceWirelessMIB,
       "colubrisDeviceWirelessMIBObjects": colubrisDeviceWirelessMIBObjects,
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
       "coDevWirIfStaGreenfieldOptionEnabled": coDevWirIfStaGreenfieldOptionEnabled,
       "coDevWirIfStaNbDetectedStation": coDevWirIfStaNbDetectedStation,
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
       "coDevWirIfStsTransmittedFrameCount": coDevWirIfStsTransmittedFrameCount,
       "coDevWirIfStsReceivedFrameCount": coDevWirIfStsReceivedFrameCount,
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
       "coDevWirCliStaHT": coDevWirCliStaHT,
       "coDevWirCliStaTransmitMCS": coDevWirCliStaTransmitMCS,
       "coDevWirCliStaReceiveMCS": coDevWirCliStaReceiveMCS,
       "coDevWirCliStaChannelWidth": coDevWirCliStaChannelWidth,
       "coDevWirCliStaShortGI": coDevWirCliStaShortGI,
       "coDevWirCliDisassociate": coDevWirCliDisassociate,
       "coDevWirNbAssociatedStation": coDevWirNbAssociatedStation,
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
       "coDeviceWirelessClientHTRatesGroup": coDeviceWirelessClientHTRatesGroup,
       "coDeviceWirelessClientStatsHTRatesTable": coDeviceWirelessClientStatsHTRatesTable,
       "coDeviceWirelessClientStatsHTRatesEntry": coDeviceWirelessClientStatsHTRatesEntry,
       "coDevWirCliStsPktsTxMCS0": coDevWirCliStsPktsTxMCS0,
       "coDevWirCliStsPktsTxMCS1": coDevWirCliStsPktsTxMCS1,
       "coDevWirCliStsPktsTxMCS2": coDevWirCliStsPktsTxMCS2,
       "coDevWirCliStsPktsTxMCS3": coDevWirCliStsPktsTxMCS3,
       "coDevWirCliStsPktsTxMCS4": coDevWirCliStsPktsTxMCS4,
       "coDevWirCliStsPktsTxMCS5": coDevWirCliStsPktsTxMCS5,
       "coDevWirCliStsPktsTxMCS6": coDevWirCliStsPktsTxMCS6,
       "coDevWirCliStsPktsTxMCS7": coDevWirCliStsPktsTxMCS7,
       "coDevWirCliStsPktsTxMCS8": coDevWirCliStsPktsTxMCS8,
       "coDevWirCliStsPktsTxMCS9": coDevWirCliStsPktsTxMCS9,
       "coDevWirCliStsPktsTxMCS10": coDevWirCliStsPktsTxMCS10,
       "coDevWirCliStsPktsTxMCS11": coDevWirCliStsPktsTxMCS11,
       "coDevWirCliStsPktsTxMCS12": coDevWirCliStsPktsTxMCS12,
       "coDevWirCliStsPktsTxMCS13": coDevWirCliStsPktsTxMCS13,
       "coDevWirCliStsPktsTxMCS14": coDevWirCliStsPktsTxMCS14,
       "coDevWirCliStsPktsTxMCS15": coDevWirCliStsPktsTxMCS15,
       "coDevWirCliStsPktsRxMCS0": coDevWirCliStsPktsRxMCS0,
       "coDevWirCliStsPktsRxMCS1": coDevWirCliStsPktsRxMCS1,
       "coDevWirCliStsPktsRxMCS2": coDevWirCliStsPktsRxMCS2,
       "coDevWirCliStsPktsRxMCS3": coDevWirCliStsPktsRxMCS3,
       "coDevWirCliStsPktsRxMCS4": coDevWirCliStsPktsRxMCS4,
       "coDevWirCliStsPktsRxMCS5": coDevWirCliStsPktsRxMCS5,
       "coDevWirCliStsPktsRxMCS6": coDevWirCliStsPktsRxMCS6,
       "coDevWirCliStsPktsRxMCS7": coDevWirCliStsPktsRxMCS7,
       "coDevWirCliStsPktsRxMCS8": coDevWirCliStsPktsRxMCS8,
       "coDevWirCliStsPktsRxMCS9": coDevWirCliStsPktsRxMCS9,
       "coDevWirCliStsPktsRxMCS10": coDevWirCliStsPktsRxMCS10,
       "coDevWirCliStsPktsRxMCS11": coDevWirCliStsPktsRxMCS11,
       "coDevWirCliStsPktsRxMCS12": coDevWirCliStsPktsRxMCS12,
       "coDevWirCliStsPktsRxMCS13": coDevWirCliStsPktsRxMCS13,
       "coDevWirCliStsPktsRxMCS14": coDevWirCliStsPktsRxMCS14,
       "coDevWirCliStsPktsRxMCS15": coDevWirCliStsPktsRxMCS15,
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
       "coDevWirApNetworkType": coDevWirApNetworkType,
       "coDeviceWirelessDetectedStationGroup": coDeviceWirelessDetectedStationGroup,
       "coDevWirNbDetectedStation": coDevWirNbDetectedStation,
       "coDeviceWirelessDetectedStationTable": coDeviceWirelessDetectedStationTable,
       "coDeviceWirelessDetectedStationEntry": coDeviceWirelessDetectedStationEntry,
       "coDevWirSDetRadioIndex": coDevWirSDetRadioIndex,
       "coDevWirDetStaIndex": coDevWirDetStaIndex,
       "coDevWirDetStaMacAddress": coDevWirDetStaMacAddress,
       "coDevWirDetStaChannel": coDevWirDetStaChannel,
       "coDevWirDetStaSignalLevel": coDevWirDetStaSignalLevel,
       "coDevWirDetStaNoiseLevel": coDevWirDetStaNoiseLevel,
       "coDevWirDetStaNbProbeReq": coDevWirDetStaNbProbeReq,
       "coDevWirDetStaRate": coDevWirDetStaRate,
       "coDevWirDetStaSSID": coDevWirDetStaSSID,
       "coDevWirDetStaTimeDiscovered": coDevWirDetStaTimeDiscovered,
       "coDevWirDetStaTimeLastSeen": coDevWirDetStaTimeLastSeen,
       "colubrisDeviceWirelessMIBNotificationPrefix": colubrisDeviceWirelessMIBNotificationPrefix,
       "colubrisDeviceWirelessMIBNotifications": colubrisDeviceWirelessMIBNotifications,
       "coDeviceWirelessSNRLevelNotification": coDeviceWirelessSNRLevelNotification,
       "coDeviceWirelessAssociationNotification": coDeviceWirelessAssociationNotification,
       "colubrisDeviceWirelessMIBConformance": colubrisDeviceWirelessMIBConformance,
       "colubrisDeviceWirelessMIBCompliances": colubrisDeviceWirelessMIBCompliances,
       "colubrisDeviceWirelessMIBCompliance": colubrisDeviceWirelessMIBCompliance,
       "colubrisDeviceWirelessMIBGroups": colubrisDeviceWirelessMIBGroups,
       "colubrisDeviceWirelessConfigMIBGroup": colubrisDeviceWirelessConfigMIBGroup,
       "colubrisDeviceWirelessIfStatusMIBGroup": colubrisDeviceWirelessIfStatusMIBGroup,
       "colubrisDeviceWirelessIfStatsMIBGroup": colubrisDeviceWirelessIfStatsMIBGroup,
       "colubrisDeviceVscStatusMIBGroup": colubrisDeviceVscStatusMIBGroup,
       "colubrisDeviceVscStatsMIBGroup": colubrisDeviceVscStatsMIBGroup,
       "colubrisDeviceWirelessClientStatusMIBGroup": colubrisDeviceWirelessClientStatusMIBGroup,
       "colubrisDeviceWirelessClientStatsMIBGroup": colubrisDeviceWirelessClientStatsMIBGroup,
       "colubrisDeviceWirelessClientStatsRatesMIBGroup": colubrisDeviceWirelessClientStatsRatesMIBGroup,
       "colubrisDeviceWirelessDetectedAPMIBGroup": colubrisDeviceWirelessDetectedAPMIBGroup,
       "colubrisDeviceWirelessNotificationGroup": colubrisDeviceWirelessNotificationGroup,
       "colubrisDeviceWirelessClientStatsHTRatesMIBGroup": colubrisDeviceWirelessClientStatsHTRatesMIBGroup,
       "colubrisDeviceWirelessDetectedStationMIBGroup": colubrisDeviceWirelessDetectedStationMIBGroup}
)
