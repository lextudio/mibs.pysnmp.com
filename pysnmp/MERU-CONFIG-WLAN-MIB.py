# SNMP MIB module (MERU-CONFIG-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:11 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAntennaLinkType,
 MwlAntennaSet,
 MwlAntennaSetLocation,
 MwlAntennaType,
 MwlApHwType,
 MwlApIfConfigModeType,
 MwlApIfModeType,
 MwlApMode,
 MwlApRfType,
 MwlArrayDataTypeAction,
 MwlAvailabilityStatus,
 MwlBandSteeringMode,
 MwlBgProtectionModeType,
 MwlChannelWidth,
 MwlDataplaneMode,
 MwlEnableDisableOption,
 MwlEssApAdminMode,
 MwlHtProtectionModeType,
 MwlIfAdministrativeState,
 MwlL2BridgingsBits,
 MwlMimoMode,
 MwlOnOffSwitch,
 MwlOperationalState,
 MwlPapBroadcastSsidMode,
 MwlProfileOwner,
 MwlPublishEssId,
 MwlTransmitRateAGBits,
 MwlTransmitRateBGBits,
 MwlTransmitRateBits,
 MwlTransmitRateHTBits,
 MwlUplinkType,
 MwlVcellType,
 MwlVlanType) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAntennaLinkType",
    "MwlAntennaSet",
    "MwlAntennaSetLocation",
    "MwlAntennaType",
    "MwlApHwType",
    "MwlApIfConfigModeType",
    "MwlApIfModeType",
    "MwlApMode",
    "MwlApRfType",
    "MwlArrayDataTypeAction",
    "MwlAvailabilityStatus",
    "MwlBandSteeringMode",
    "MwlBgProtectionModeType",
    "MwlChannelWidth",
    "MwlDataplaneMode",
    "MwlEnableDisableOption",
    "MwlEssApAdminMode",
    "MwlHtProtectionModeType",
    "MwlIfAdministrativeState",
    "MwlL2BridgingsBits",
    "MwlMimoMode",
    "MwlOnOffSwitch",
    "MwlOperationalState",
    "MwlPapBroadcastSsidMode",
    "MwlProfileOwner",
    "MwlPublishEssId",
    "MwlTransmitRateAGBits",
    "MwlTransmitRateBGBits",
    "MwlTransmitRateBits",
    "MwlTransmitRateHTBits",
    "MwlUplinkType",
    "MwlVcellType",
    "MwlVlanType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigWlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwIf80211CapabilityTable_Object = MibTable
mwIf80211CapabilityTable = _MwIf80211CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mwIf80211CapabilityTable.setStatus("current")
_MwIf80211CapabilityEntry_Object = MibTableRow
mwIf80211CapabilityEntry = _MwIf80211CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1)
)
mwIf80211CapabilityEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwIf80211CapabilityTableIndex"),
)
if mibBuilder.loadTexts:
    mwIf80211CapabilityEntry.setStatus("current")
_MwIf80211CapabilityTableIndex_Type = Integer32
_MwIf80211CapabilityTableIndex_Object = MibTableColumn
mwIf80211CapabilityTableIndex = _MwIf80211CapabilityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 1),
    _MwIf80211CapabilityTableIndex_Type()
)
mwIf80211CapabilityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIf80211CapabilityTableIndex.setStatus("current")
_MwIf80211CapabilityIfAGain_Type = Unsigned32
_MwIf80211CapabilityIfAGain_Object = MibTableColumn
mwIf80211CapabilityIfAGain = _MwIf80211CapabilityIfAGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 2),
    _MwIf80211CapabilityIfAGain_Type()
)
mwIf80211CapabilityIfAGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAGain.setStatus("current")
_MwIf80211CapabilityIfBgGain_Type = Unsigned32
_MwIf80211CapabilityIfBgGain_Object = MibTableColumn
mwIf80211CapabilityIfBgGain = _MwIf80211CapabilityIfBgGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 3),
    _MwIf80211CapabilityIfBgGain_Type()
)
mwIf80211CapabilityIfBgGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfBgGain.setStatus("current")
_MwIf80211CapabilityIfLinkType_Type = MwlAntennaLinkType
_MwIf80211CapabilityIfLinkType_Object = MibTableColumn
mwIf80211CapabilityIfLinkType = _MwIf80211CapabilityIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 4),
    _MwIf80211CapabilityIfLinkType_Type()
)
mwIf80211CapabilityIfLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfLinkType.setStatus("current")
_MwIf80211CapabilityIfAntennaSet_Type = MwlAntennaSet
_MwIf80211CapabilityIfAntennaSet_Object = MibTableColumn
mwIf80211CapabilityIfAntennaSet = _MwIf80211CapabilityIfAntennaSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 5),
    _MwIf80211CapabilityIfAntennaSet_Type()
)
mwIf80211CapabilityIfAntennaSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaSet.setStatus("current")
_MwIf80211CapabilityIfConnectorType_Type = MwlAntennaType
_MwIf80211CapabilityIfConnectorType_Object = MibTableColumn
mwIf80211CapabilityIfConnectorType = _MwIf80211CapabilityIfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 6),
    _MwIf80211CapabilityIfConnectorType_Type()
)
mwIf80211CapabilityIfConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfConnectorType.setStatus("current")
_MwIf80211CapabilityIfIndex_Type = Integer32
_MwIf80211CapabilityIfIndex_Object = MibTableColumn
mwIf80211CapabilityIfIndex = _MwIf80211CapabilityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 7),
    _MwIf80211CapabilityIfIndex_Type()
)
mwIf80211CapabilityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfIndex.setStatus("current")
_MwIf80211CapabilityApHwType_Type = MwlApHwType
_MwIf80211CapabilityApHwType_Object = MibTableColumn
mwIf80211CapabilityApHwType = _MwIf80211CapabilityApHwType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 8),
    _MwIf80211CapabilityApHwType_Type()
)
mwIf80211CapabilityApHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityApHwType.setStatus("current")
_MwIf80211CapabilityIfNmsNodeId_Type = Integer32
_MwIf80211CapabilityIfNmsNodeId_Object = MibTableColumn
mwIf80211CapabilityIfNmsNodeId = _MwIf80211CapabilityIfNmsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 9),
    _MwIf80211CapabilityIfNmsNodeId_Type()
)
mwIf80211CapabilityIfNmsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfNmsNodeId.setStatus("current")
_MwIf80211CapabilityIfConnectorGain_Type = Unsigned32
_MwIf80211CapabilityIfConnectorGain_Object = MibTableColumn
mwIf80211CapabilityIfConnectorGain = _MwIf80211CapabilityIfConnectorGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 10),
    _MwIf80211CapabilityIfConnectorGain_Type()
)
mwIf80211CapabilityIfConnectorGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfConnectorGain.setStatus("current")
_MwIf80211CapabilityIfAntennaLocation_Type = MwlAntennaSetLocation
_MwIf80211CapabilityIfAntennaLocation_Object = MibTableColumn
mwIf80211CapabilityIfAntennaLocation = _MwIf80211CapabilityIfAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 11),
    _MwIf80211CapabilityIfAntennaLocation_Type()
)
mwIf80211CapabilityIfAntennaLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaLocation.setStatus("current")
_MwIf80211CapabilityIfAntennaConnector_Type = Integer32
_MwIf80211CapabilityIfAntennaConnector_Object = MibTableColumn
mwIf80211CapabilityIfAntennaConnector = _MwIf80211CapabilityIfAntennaConnector_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 12),
    _MwIf80211CapabilityIfAntennaConnector_Type()
)
mwIf80211CapabilityIfAntennaConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaConnector.setStatus("current")
_MwEssTable_Object = MibTable
mwEssTable = _MwEssTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    mwEssTable.setStatus("current")
_MwEssEntry_Object = MibTableRow
mwEssEntry = _MwEssEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1)
)
mwEssEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwEssTableIndex"),
)
if mibBuilder.loadTexts:
    mwEssEntry.setStatus("current")
_MwEssTableIndex_Type = Integer32
_MwEssTableIndex_Object = MibTableColumn
mwEssTableIndex = _MwEssTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 1),
    _MwEssTableIndex_Type()
)
mwEssTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEssTableIndex.setStatus("current")


class _MwEssSsId_Type(DisplayString):
    """Custom type mwEssSsId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssSsId_Type.__name__ = "DisplayString"
_MwEssSsId_Object = MibTableColumn
mwEssSsId = _MwEssSsId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 2),
    _MwEssSsId_Type()
)
mwEssSsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSsId.setStatus("current")


class _MwEssId_Type(DisplayString):
    """Custom type mwEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwEssId_Type.__name__ = "DisplayString"
_MwEssId_Object = MibTableColumn
mwEssId = _MwEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 3),
    _MwEssId_Type()
)
mwEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssId.setStatus("current")


class _MwEssGreName_Type(DisplayString):
    """Custom type mwEssGreName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssGreName_Type.__name__ = "DisplayString"
_MwEssGreName_Object = MibTableColumn
mwEssGreName = _MwEssGreName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 4),
    _MwEssGreName_Type()
)
mwEssGreName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGreName.setStatus("current")


class _MwEssVlanName_Type(DisplayString):
    """Custom type mwEssVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssVlanName_Type.__name__ = "DisplayString"
_MwEssVlanName_Object = MibTableColumn
mwEssVlanName = _MwEssVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 5),
    _MwEssVlanName_Type()
)
mwEssVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVlanName.setStatus("current")
_MwEssVcellType_Type = MwlVcellType
_MwEssVcellType_Object = MibTableColumn
mwEssVcellType = _MwEssVcellType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 7),
    _MwEssVcellType_Type()
)
mwEssVcellType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVcellType.setStatus("current")
_MwEssL2Bridging_Type = MwlL2BridgingsBits
_MwEssL2Bridging_Object = MibTableColumn
mwEssL2Bridging = _MwEssL2Bridging_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 8),
    _MwEssL2Bridging_Type()
)
mwEssL2Bridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssL2Bridging.setStatus("current")


class _MwEssDTIMPeriod_Type(Integer32):
    """Custom type mwEssDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MwEssDTIMPeriod_Type.__name__ = "Integer32"
_MwEssDTIMPeriod_Object = MibTableColumn
mwEssDTIMPeriod = _MwEssDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 9),
    _MwEssDTIMPeriod_Type()
)
mwEssDTIMPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssDTIMPeriod.setStatus("current")
_MwEssVlanSupport_Type = MwlVlanType
_MwEssVlanSupport_Object = MibTableColumn
mwEssVlanSupport = _MwEssVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 10),
    _MwEssVlanSupport_Type()
)
mwEssVlanSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVlanSupport.setStatus("current")
_MwEssBaseTxRates_Type = MwlTransmitRateBits
_MwEssBaseTxRates_Object = MibTableColumn
mwEssBaseTxRates = _MwEssBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 11),
    _MwEssBaseTxRates_Type()
)
mwEssBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBaseTxRates.setStatus("current")
_MwPublishEssId_Type = MwlPublishEssId
_MwPublishEssId_Object = MibTableColumn
mwPublishEssId = _MwPublishEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 12),
    _MwPublishEssId_Type()
)
mwPublishEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPublishEssId.setStatus("current")
_MwEssABaseTxRates_Type = MwlTransmitRateAGBits
_MwEssABaseTxRates_Object = MibTableColumn
mwEssABaseTxRates = _MwEssABaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 13),
    _MwEssABaseTxRates_Type()
)
mwEssABaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssABaseTxRates.setStatus("current")
_MwEssGBaseTxRates_Type = MwlTransmitRateAGBits
_MwEssGBaseTxRates_Object = MibTableColumn
mwEssGBaseTxRates = _MwEssGBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 14),
    _MwEssGBaseTxRates_Type()
)
mwEssGBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGBaseTxRates.setStatus("current")
_MwEssDataplaneMode_Type = MwlDataplaneMode
_MwEssDataplaneMode_Object = MibTableColumn
mwEssDataplaneMode = _MwEssDataplaneMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 15),
    _MwEssDataplaneMode_Type()
)
mwEssDataplaneMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssDataplaneMode.setStatus("current")
_MwEssBGBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssBGBaseTxRates_Object = MibTableColumn
mwEssBGBaseTxRates = _MwEssBGBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 16),
    _MwEssBGBaseTxRates_Type()
)
mwEssBGBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGBaseTxRates.setStatus("current")
_MwEssANBaseTxRates_Type = MwlTransmitRateAGBits
_MwEssANBaseTxRates_Object = MibTableColumn
mwEssANBaseTxRates = _MwEssANBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 17),
    _MwEssANBaseTxRates_Type()
)
mwEssANBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANBaseTxRates.setStatus("current")
_MwEssBeaconInterval_Type = Unsigned32
_MwEssBeaconInterval_Object = MibTableColumn
mwEssBeaconInterval = _MwEssBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 18),
    _MwEssBeaconInterval_Type()
)
mwEssBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBeaconInterval.setStatus("current")
_MwEssAllowMulticast_Type = MwlOnOffSwitch
_MwEssAllowMulticast_Object = MibTableColumn
mwEssAllowMulticast = _MwEssAllowMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 19),
    _MwEssAllowMulticast_Type()
)
mwEssAllowMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssAllowMulticast.setStatus("current")
_MwEssBGNBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssBGNBaseTxRates_Object = MibTableColumn
mwEssBGNBaseTxRates = _MwEssBGNBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 20),
    _MwEssBGNBaseTxRates_Type()
)
mwEssBGNBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNBaseTxRates.setStatus("current")
_MwEssCountermeasure_Type = MwlOnOffSwitch
_MwEssCountermeasure_Object = MibTableColumn
mwEssCountermeasure = _MwEssCountermeasure_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 21),
    _MwEssCountermeasure_Type()
)
mwEssCountermeasure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssCountermeasure.setStatus("current")
_MwEssJoinOnDiscovery_Type = MwlOnOffSwitch
_MwEssJoinOnDiscovery_Object = MibTableColumn
mwEssJoinOnDiscovery = _MwEssJoinOnDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 22),
    _MwEssJoinOnDiscovery_Type()
)
mwEssJoinOnDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssJoinOnDiscovery.setStatus("current")
_MwEssANBaseHTTxRates_Type = MwlTransmitRateHTBits
_MwEssANBaseHTTxRates_Object = MibTableColumn
mwEssANBaseHTTxRates = _MwEssANBaseHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 23),
    _MwEssANBaseHTTxRates_Type()
)
mwEssANBaseHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANBaseHTTxRates.setStatus("current")
_MwEssSupportedTxRates_Type = MwlTransmitRateBits
_MwEssSupportedTxRates_Object = MibTableColumn
mwEssSupportedTxRates = _MwEssSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 24),
    _MwEssSupportedTxRates_Type()
)
mwEssSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSupportedTxRates.setStatus("current")
_MwEssBGNBaseHTTxRates_Type = MwlTransmitRateHTBits
_MwEssBGNBaseHTTxRates_Object = MibTableColumn
mwEssBGNBaseHTTxRates = _MwEssBGNBaseHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 25),
    _MwEssBGNBaseHTTxRates_Type()
)
mwEssBGNBaseHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNBaseHTTxRates.setStatus("current")
_MwEssASupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssASupportedTxRates_Object = MibTableColumn
mwEssASupportedTxRates = _MwEssASupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 26),
    _MwEssASupportedTxRates_Type()
)
mwEssASupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssASupportedTxRates.setStatus("current")
_MwEssGSupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssGSupportedTxRates_Object = MibTableColumn
mwEssGSupportedTxRates = _MwEssGSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 27),
    _MwEssGSupportedTxRates_Type()
)
mwEssGSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGSupportedTxRates.setStatus("current")
_MwEssBGSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssBGSupportedTxRates_Object = MibTableColumn
mwEssBGSupportedTxRates = _MwEssBGSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 29),
    _MwEssBGSupportedTxRates_Type()
)
mwEssBGSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGSupportedTxRates.setStatus("current")
_MwEssANSupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssANSupportedTxRates_Object = MibTableColumn
mwEssANSupportedTxRates = _MwEssANSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 30),
    _MwEssANSupportedTxRates_Type()
)
mwEssANSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANSupportedTxRates.setStatus("current")
_MwEssSecurityProfileName_Type = DisplayString
_MwEssSecurityProfileName_Object = MibTableColumn
mwEssSecurityProfileName = _MwEssSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 31),
    _MwEssSecurityProfileName_Type()
)
mwEssSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSecurityProfileName.setStatus("current")
_MwEssBGNSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssBGNSupportedTxRates_Object = MibTableColumn
mwEssBGNSupportedTxRates = _MwEssBGNSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 32),
    _MwEssBGNSupportedTxRates_Type()
)
mwEssBGNSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNSupportedTxRates.setStatus("current")
_MwEssANSupportedHTTxRates_Type = MwlTransmitRateHTBits
_MwEssANSupportedHTTxRates_Object = MibTableColumn
mwEssANSupportedHTTxRates = _MwEssANSupportedHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 33),
    _MwEssANSupportedHTTxRates_Type()
)
mwEssANSupportedHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANSupportedHTTxRates.setStatus("current")
_MwEssBGNSupportedHTTxRates_Type = MwlTransmitRateHTBits
_MwEssBGNSupportedHTTxRates_Object = MibTableColumn
mwEssBGNSupportedHTTxRates = _MwEssBGNSupportedHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 34),
    _MwEssBGNSupportedHTTxRates_Type()
)
mwEssBGNSupportedHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNSupportedHTTxRates.setStatus("current")
_MwEssAPsShareChannelAndBssId_Type = MwlOnOffSwitch
_MwEssAPsShareChannelAndBssId_Object = MibTableColumn
mwEssAPsShareChannelAndBssId = _MwEssAPsShareChannelAndBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 35),
    _MwEssAPsShareChannelAndBssId_Type()
)
mwEssAPsShareChannelAndBssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssAPsShareChannelAndBssId.setStatus("current")
_MwEssAccountingInterimInterval_Type = Unsigned32
_MwEssAccountingInterimInterval_Object = MibTableColumn
mwEssAccountingInterimInterval = _MwEssAccountingInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 36),
    _MwEssAccountingInterimInterval_Type()
)
mwEssAccountingInterimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssAccountingInterimInterval.setStatus("current")
_MwEssPrimaryAccountingRadiusName_Type = DisplayString
_MwEssPrimaryAccountingRadiusName_Object = MibTableColumn
mwEssPrimaryAccountingRadiusName = _MwEssPrimaryAccountingRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 37),
    _MwEssPrimaryAccountingRadiusName_Type()
)
mwEssPrimaryAccountingRadiusName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssPrimaryAccountingRadiusName.setStatus("current")
_MwEssSecondaryAccountingRadiusName_Type = DisplayString
_MwEssSecondaryAccountingRadiusName_Object = MibTableColumn
mwEssSecondaryAccountingRadiusName = _MwEssSecondaryAccountingRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 38),
    _MwEssSecondaryAccountingRadiusName_Type()
)
mwEssSecondaryAccountingRadiusName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSecondaryAccountingRadiusName.setStatus("current")
_MwEssMulticastMACTransparency_Type = MwlOnOffSwitch
_MwEssMulticastMACTransparency_Object = MibTableColumn
mwEssMulticastMACTransparency = _MwEssMulticastMACTransparency_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 39),
    _MwEssMulticastMACTransparency_Type()
)
mwEssMulticastMACTransparency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMulticastMACTransparency.setStatus("current")
_MwEssBandSteering_Type = MwlBandSteeringMode
_MwEssBandSteering_Object = MibTableColumn
mwEssBandSteering = _MwEssBandSteering_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 43),
    _MwEssBandSteering_Type()
)
mwEssBandSteering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBandSteering.setStatus("current")
_MwEssBandSteeringTimeout_Type = Unsigned32
_MwEssBandSteeringTimeout_Object = MibTableColumn
mwEssBandSteeringTimeout = _MwEssBandSteeringTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 44),
    _MwEssBandSteeringTimeout_Type()
)
mwEssBandSteeringTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBandSteeringTimeout.setStatus("current")
_MwEssApVlanTag_Type = Unsigned32
_MwEssApVlanTag_Object = MibTableColumn
mwEssApVlanTag = _MwEssApVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 45),
    _MwEssApVlanTag_Type()
)
mwEssApVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApVlanTag.setStatus("current")
_MwEssEnableApVlanPriority_Type = MwlOnOffSwitch
_MwEssEnableApVlanPriority_Object = MibTableColumn
mwEssEnableApVlanPriority = _MwEssEnableApVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 46),
    _MwEssEnableApVlanPriority_Type()
)
mwEssEnableApVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEnableApVlanPriority.setStatus("current")
_MwEssOwner_Type = MwlProfileOwner
_MwEssOwner_Object = MibTableColumn
mwEssOwner = _MwEssOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 47),
    _MwEssOwner_Type()
)
mwEssOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssOwner.setStatus("current")


class _MwEssIDOverflowFrom_Type(DisplayString):
    """Custom type mwEssIDOverflowFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssIDOverflowFrom_Type.__name__ = "DisplayString"
_MwEssIDOverflowFrom_Object = MibTableColumn
mwEssIDOverflowFrom = _MwEssIDOverflowFrom_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 48),
    _MwEssIDOverflowFrom_Type()
)
mwEssIDOverflowFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssIDOverflowFrom.setStatus("current")
_MwEssEnableAPSD_Type = MwlOnOffSwitch
_MwEssEnableAPSD_Object = MibTableColumn
mwEssEnableAPSD = _MwEssEnableAPSD_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 49),
    _MwEssEnableAPSD_Type()
)
mwEssEnableAPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEnableAPSD.setStatus("current")
_MwEssState_Type = MwlEnableDisableOption
_MwEssState_Object = MibTableColumn
mwEssState = _MwEssState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 50),
    _MwEssState_Type()
)
mwEssState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssState.setStatus("current")
_MwEssMultipleIpPerStation_Type = MwlOnOffSwitch
_MwEssMultipleIpPerStation_Object = MibTableColumn
mwEssMultipleIpPerStation = _MwEssMultipleIpPerStation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 51),
    _MwEssMultipleIpPerStation_Type()
)
mwEssMultipleIpPerStation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMultipleIpPerStation.setStatus("current")
_MwEssMulticastToUnicastConversion_Type = MwlOnOffSwitch
_MwEssMulticastToUnicastConversion_Object = MibTableColumn
mwEssMulticastToUnicastConversion = _MwEssMulticastToUnicastConversion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 52),
    _MwEssMulticastToUnicastConversion_Type()
)
mwEssMulticastToUnicastConversion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMulticastToUnicastConversion.setStatus("current")
_MwEssEfOverride_Type = MwlOnOffSwitch
_MwEssEfOverride_Object = MibTableColumn
mwEssEfOverride = _MwEssEfOverride_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 53),
    _MwEssEfOverride_Type()
)
mwEssEfOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEfOverride.setStatus("current")
_MwEssPapBroadcastSsid_Type = MwlPapBroadcastSsidMode
_MwEssPapBroadcastSsid_Object = MibTableColumn
mwEssPapBroadcastSsid = _MwEssPapBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 54),
    _MwEssPapBroadcastSsid_Type()
)
mwEssPapBroadcastSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssPapBroadcastSsid.setStatus("current")


class _MwEssVirtualInterfaceProfileName_Type(DisplayString):
    """Custom type mwEssVirtualInterfaceProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssVirtualInterfaceProfileName_Type.__name__ = "DisplayString"
_MwEssVirtualInterfaceProfileName_Object = MibTableColumn
mwEssVirtualInterfaceProfileName = _MwEssVirtualInterfaceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 56),
    _MwEssVirtualInterfaceProfileName_Type()
)
mwEssVirtualInterfaceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVirtualInterfaceProfileName.setStatus("current")
_MwEssWirelessToWirelessIsolation_Type = MwlOnOffSwitch
_MwEssWirelessToWirelessIsolation_Object = MibTableColumn
mwEssWirelessToWirelessIsolation = _MwEssWirelessToWirelessIsolation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 58),
    _MwEssWirelessToWirelessIsolation_Type()
)
mwEssWirelessToWirelessIsolation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssWirelessToWirelessIsolation.setStatus("current")
_MwEssRowStatus_Type = RowStatus
_MwEssRowStatus_Object = MibTableColumn
mwEssRowStatus = _MwEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 67),
    _MwEssRowStatus_Type()
)
mwEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssRowStatus.setStatus("current")
_MwIf80211Table_Object = MibTable
mwIf80211Table = _MwIf80211Table_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    mwIf80211Table.setStatus("current")
_MwIf80211Entry_Object = MibTableRow
mwIf80211Entry = _MwIf80211Entry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1)
)
mwIf80211Entry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwIf80211TableIndex"),
)
if mibBuilder.loadTexts:
    mwIf80211Entry.setStatus("current")
_MwIf80211TableIndex_Type = Integer32
_MwIf80211TableIndex_Object = MibTableColumn
mwIf80211TableIndex = _MwIf80211TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 1),
    _MwIf80211TableIndex_Type()
)
mwIf80211TableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIf80211TableIndex.setStatus("current")
_MwIf80211IfMode_Type = MwlApIfConfigModeType
_MwIf80211IfMode_Object = MibTableColumn
mwIf80211IfMode = _MwIf80211IfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 2),
    _MwIf80211IfMode_Type()
)
mwIf80211IfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMode.setStatus("current")


class _MwIf80211IfDescr_Type(DisplayString):
    """Custom type mwIf80211IfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MwIf80211IfDescr_Type.__name__ = "DisplayString"
_MwIf80211IfDescr_Object = MibTableColumn
mwIf80211IfDescr = _MwIf80211IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 3),
    _MwIf80211IfDescr_Type()
)
mwIf80211IfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfDescr.setStatus("current")
_MwIf80211IfApMode_Type = MwlApMode
_MwIf80211IfApMode_Object = MibTableColumn
mwIf80211IfApMode = _MwIf80211IfApMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 4),
    _MwIf80211IfApMode_Type()
)
mwIf80211IfApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfApMode.setStatus("current")
_MwIf80211IfChannel_Type = Integer32
_MwIf80211IfChannel_Object = MibTableColumn
mwIf80211IfChannel = _MwIf80211IfChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 5),
    _MwIf80211IfChannel_Type()
)
mwIf80211IfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfChannel.setStatus("current")
_MwIf80211NOnlyMode_Type = MwlOnOffSwitch
_MwIf80211NOnlyMode_Object = MibTableColumn
mwIf80211NOnlyMode = _MwIf80211NOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 7),
    _MwIf80211NOnlyMode_Type()
)
mwIf80211NOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211NOnlyMode.setStatus("current")
_MwIf80211IfMimoMode_Type = MwlMimoMode
_MwIf80211IfMimoMode_Object = MibTableColumn
mwIf80211IfMimoMode = _MwIf80211IfMimoMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 11),
    _MwIf80211IfMimoMode_Type()
)
mwIf80211IfMimoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMimoMode.setStatus("current")
_MwIf80211channelWidth_Type = MwlChannelWidth
_MwIf80211channelWidth_Object = MibTableColumn
mwIf80211channelWidth = _MwIf80211channelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 13),
    _MwIf80211channelWidth_Type()
)
mwIf80211channelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211channelWidth.setStatus("current")
_MwIf80211IfAdminStatus_Type = MwlIfAdministrativeState
_MwIf80211IfAdminStatus_Object = MibTableColumn
mwIf80211IfAdminStatus = _MwIf80211IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 17),
    _MwIf80211IfAdminStatus_Type()
)
mwIf80211IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfAdminStatus.setStatus("current")
_MwIf80211IfTxPowerHigh_Type = Integer32
_MwIf80211IfTxPowerHigh_Object = MibTableColumn
mwIf80211IfTxPowerHigh = _MwIf80211IfTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 18),
    _MwIf80211IfTxPowerHigh_Type()
)
mwIf80211IfTxPowerHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfTxPowerHigh.setStatus("current")
_MwIf80211IfBgProtectionMode_Type = MwlBgProtectionModeType
_MwIf80211IfBgProtectionMode_Object = MibTableColumn
mwIf80211IfBgProtectionMode = _MwIf80211IfBgProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 19),
    _MwIf80211IfBgProtectionMode_Type()
)
mwIf80211IfBgProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfBgProtectionMode.setStatus("current")
_MwIf80211IfShortPreambleFlag_Type = MwlOnOffSwitch
_MwIf80211IfShortPreambleFlag_Object = MibTableColumn
mwIf80211IfShortPreambleFlag = _MwIf80211IfShortPreambleFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 20),
    _MwIf80211IfShortPreambleFlag_Type()
)
mwIf80211IfShortPreambleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfShortPreambleFlag.setStatus("current")
_MwIf80211IfMtu_Type = Unsigned32
_MwIf80211IfMtu_Object = MibTableColumn
mwIf80211IfMtu = _MwIf80211IfMtu_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 21),
    _MwIf80211IfMtu_Type()
)
mwIf80211IfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfMtu.setStatus("current")
_MwIf80211IfType_Type = MwlApRfType
_MwIf80211IfType_Object = MibTableColumn
mwIf80211IfType = _MwIf80211IfType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 22),
    _MwIf80211IfType_Type()
)
mwIf80211IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfType.setStatus("current")
_MwIf80211IfIndex_Type = Integer32
_MwIf80211IfIndex_Object = MibTableColumn
mwIf80211IfIndex = _MwIf80211IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 23),
    _MwIf80211IfIndex_Type()
)
mwIf80211IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfIndex.setStatus("current")
_MwIf80211IfNodeId_Type = Unsigned32
_MwIf80211IfNodeId_Object = MibTableColumn
mwIf80211IfNodeId = _MwIf80211IfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 24),
    _MwIf80211IfNodeId_Type()
)
mwIf80211IfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNodeId.setStatus("current")
_MwIf80211ApHwType_Type = MwlApHwType
_MwIf80211ApHwType_Object = MibTableColumn
mwIf80211ApHwType = _MwIf80211ApHwType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 25),
    _MwIf80211ApHwType_Type()
)
mwIf80211ApHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211ApHwType.setStatus("current")
_MwIf80211IfNodeName_Type = DisplayString
_MwIf80211IfNodeName_Object = MibTableColumn
mwIf80211IfNodeName = _MwIf80211IfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 26),
    _MwIf80211IfNodeName_Type()
)
mwIf80211IfNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNodeName.setStatus("current")
_MwIf80211IfOperStatus_Type = MwlOperationalState
_MwIf80211IfOperStatus_Object = MibTableColumn
mwIf80211IfOperStatus = _MwIf80211IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 27),
    _MwIf80211IfOperStatus_Type()
)
mwIf80211IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfOperStatus.setStatus("current")
_MwIf80211IfLastChange_Type = DateAndTime
_MwIf80211IfLastChange_Object = MibTableColumn
mwIf80211IfLastChange = _MwIf80211IfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 28),
    _MwIf80211IfLastChange_Type()
)
mwIf80211IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfLastChange.setStatus("current")
_MwIf80211IfOperChannel_Type = Integer32
_MwIf80211IfOperChannel_Object = MibTableColumn
mwIf80211IfOperChannel = _MwIf80211IfOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 29),
    _MwIf80211IfOperChannel_Type()
)
mwIf80211IfOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfOperChannel.setStatus("current")
_MwIf80211IfBandSupport_Type = MwlApIfModeType
_MwIf80211IfBandSupport_Object = MibTableColumn
mwIf80211IfBandSupport = _MwIf80211IfBandSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 30),
    _MwIf80211IfBandSupport_Type()
)
mwIf80211IfBandSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfBandSupport.setStatus("current")
_MwIf80211DualabgSupport_Type = MwlOnOffSwitch
_MwIf80211DualabgSupport_Object = MibTableColumn
mwIf80211DualabgSupport = _MwIf80211DualabgSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 33),
    _MwIf80211DualabgSupport_Type()
)
mwIf80211DualabgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211DualabgSupport.setStatus("current")
_MwIf80211IfNumAntennas_Type = Integer32
_MwIf80211IfNumAntennas_Object = MibTableColumn
mwIf80211IfNumAntennas = _MwIf80211IfNumAntennas_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 40),
    _MwIf80211IfNumAntennas_Type()
)
mwIf80211IfNumAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNumAntennas.setStatus("current")
_MwIf80211Rf6Rf7VcellMode_Type = MwlOnOffSwitch
_MwIf80211Rf6Rf7VcellMode_Object = MibTableColumn
mwIf80211Rf6Rf7VcellMode = _MwIf80211Rf6Rf7VcellMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 41),
    _MwIf80211Rf6Rf7VcellMode_Type()
)
mwIf80211Rf6Rf7VcellMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211Rf6Rf7VcellMode.setStatus("current")
_MwIf80211ProbeResponseThreshold_Type = Unsigned32
_MwIf80211ProbeResponseThreshold_Object = MibTableColumn
mwIf80211ProbeResponseThreshold = _MwIf80211ProbeResponseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 42),
    _MwIf80211ProbeResponseThreshold_Type()
)
mwIf80211ProbeResponseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211ProbeResponseThreshold.setStatus("current")
_MwIf80211IfMeshStatus_Type = MwlEnableDisableOption
_MwIf80211IfMeshStatus_Object = MibTableColumn
mwIf80211IfMeshStatus = _MwIf80211IfMeshStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 44),
    _MwIf80211IfMeshStatus_Type()
)
mwIf80211IfMeshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMeshStatus.setStatus("current")
_MwIf80211UplinkType_Type = MwlUplinkType
_MwIf80211UplinkType_Object = MibTableColumn
mwIf80211UplinkType = _MwIf80211UplinkType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 45),
    _MwIf80211UplinkType_Type()
)
mwIf80211UplinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211UplinkType.setStatus("current")
_MwIf80211IfHtProtectionMode_Type = MwlHtProtectionModeType
_MwIf80211IfHtProtectionMode_Object = MibTableColumn
mwIf80211IfHtProtectionMode = _MwIf80211IfHtProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 46),
    _MwIf80211IfHtProtectionMode_Type()
)
mwIf80211IfHtProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfHtProtectionMode.setStatus("current")
_MwEssApTable_Object = MibTable
mwEssApTable = _MwEssApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    mwEssApTable.setStatus("current")
_MwEssApEntry_Object = MibTableRow
mwEssApEntry = _MwEssApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1)
)
mwEssApEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwEssApTableIndex"),
)
if mibBuilder.loadTexts:
    mwEssApEntry.setStatus("current")
_MwEssApTableIndex_Type = Integer32
_MwEssApTableIndex_Object = MibTableColumn
mwEssApTableIndex = _MwEssApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 1),
    _MwEssApTableIndex_Type()
)
mwEssApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEssApTableIndex.setStatus("current")
_MwEssApEssId_Type = DisplayString
_MwEssApEssId_Object = MibTableColumn
mwEssApEssId = _MwEssApEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 2),
    _MwEssApEssId_Type()
)
mwEssApEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApEssId.setStatus("current")
_MwEssApIfIndex_Type = Integer32
_MwEssApIfIndex_Object = MibTableColumn
mwEssApIfIndex = _MwEssApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 3),
    _MwEssApIfIndex_Type()
)
mwEssApIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApIfIndex.setStatus("current")
_MwEssApMaxCalls_Type = Unsigned32
_MwEssApMaxCalls_Object = MibTableColumn
mwEssApMaxCalls = _MwEssApMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 4),
    _MwEssApMaxCalls_Type()
)
mwEssApMaxCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApMaxCalls.setStatus("current")


class _MwEssApApNodeId_Type(Integer32):
    """Custom type mwEssApApNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MwEssApApNodeId_Type.__name__ = "Integer32"
_MwEssApApNodeId_Object = MibTableColumn
mwEssApApNodeId = _MwEssApApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 5),
    _MwEssApApNodeId_Type()
)
mwEssApApNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApApNodeId.setStatus("current")
_MwEssApBssId_Type = MacAddress
_MwEssApBssId_Object = MibTableColumn
mwEssApBssId = _MwEssApBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 6),
    _MwEssApBssId_Type()
)
mwEssApBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApBssId.setStatus("current")
_MwEssApIfMode_Type = MwlApIfConfigModeType
_MwEssApIfMode_Object = MibTableColumn
mwEssApIfMode = _MwEssApIfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 7),
    _MwEssApIfMode_Type()
)
mwEssApIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApIfMode.setStatus("current")
_MwEssApApNodeName_Type = DisplayString
_MwEssApApNodeName_Object = MibTableColumn
mwEssApApNodeName = _MwEssApApNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 8),
    _MwEssApApNodeName_Type()
)
mwEssApApNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApApNodeName.setStatus("current")
_MwEssApBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssApBaseTxRates_Object = MibTableColumn
mwEssApBaseTxRates = _MwEssApBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 9),
    _MwEssApBaseTxRates_Type()
)
mwEssApBaseTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApBaseTxRates.setStatus("current")
_MwEssApChannelNumber_Type = Integer32
_MwEssApChannelNumber_Object = MibTableColumn
mwEssApChannelNumber = _MwEssApChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 10),
    _MwEssApChannelNumber_Type()
)
mwEssApChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApChannelNumber.setStatus("current")
_MwEssApIfOperChannel_Type = Integer32
_MwEssApIfOperChannel_Object = MibTableColumn
mwEssApIfOperChannel = _MwEssApIfOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 11),
    _MwEssApIfOperChannel_Type()
)
mwEssApIfOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApIfOperChannel.setStatus("current")
_MwEssApSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssApSupportedTxRates_Object = MibTableColumn
mwEssApSupportedTxRates = _MwEssApSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 12),
    _MwEssApSupportedTxRates_Type()
)
mwEssApSupportedTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApSupportedTxRates.setStatus("current")
_MwEssApAdminMode_Type = MwlEssApAdminMode
_MwEssApAdminMode_Object = MibTableColumn
mwEssApAdminMode = _MwEssApAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 13),
    _MwEssApAdminMode_Type()
)
mwEssApAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApAdminMode.setStatus("current")
_MwEssApRowStatus_Type = RowStatus
_MwEssApRowStatus_Object = MibTableColumn
mwEssApRowStatus = _MwEssApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 14),
    _MwEssApRowStatus_Type()
)
mwEssApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApRowStatus.setStatus("current")
_MwMeshProfileTable_Object = MibTable
mwMeshProfileTable = _MwMeshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    mwMeshProfileTable.setStatus("current")
_MwMeshProfileEntry_Object = MibTableRow
mwMeshProfileEntry = _MwMeshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1)
)
mwMeshProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwMeshProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwMeshProfileEntry.setStatus("current")
_MwMeshProfileTableIndex_Type = Integer32
_MwMeshProfileTableIndex_Object = MibTableColumn
mwMeshProfileTableIndex = _MwMeshProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 1),
    _MwMeshProfileTableIndex_Type()
)
mwMeshProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwMeshProfileTableIndex.setStatus("current")


class _MwMeshProfileName_Type(DisplayString):
    """Custom type mwMeshProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwMeshProfileName_Type.__name__ = "DisplayString"
_MwMeshProfileName_Object = MibTableColumn
mwMeshProfileName = _MwMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 2),
    _MwMeshProfileName_Type()
)
mwMeshProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileName.setStatus("current")


class _MwMeshProfileDescr_Type(DisplayString):
    """Custom type mwMeshProfileDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MwMeshProfileDescr_Type.__name__ = "DisplayString"
_MwMeshProfileDescr_Object = MibTableColumn
mwMeshProfileDescr = _MwMeshProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 3),
    _MwMeshProfileDescr_Type()
)
mwMeshProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileDescr.setStatus("current")


class _MwMeshProfilePSK_Type(DisplayString):
    """Custom type mwMeshProfilePSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_MwMeshProfilePSK_Type.__name__ = "DisplayString"
_MwMeshProfilePSK_Object = MibTableColumn
mwMeshProfilePSK = _MwMeshProfilePSK_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 4),
    _MwMeshProfilePSK_Type()
)
mwMeshProfilePSK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfilePSK.setStatus("current")
_MwMeshProfileAdminMode_Type = MwlEnableDisableOption
_MwMeshProfileAdminMode_Object = MibTableColumn
mwMeshProfileAdminMode = _MwMeshProfileAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 5),
    _MwMeshProfileAdminMode_Type()
)
mwMeshProfileAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileAdminMode.setStatus("current")
_MwMeshProfilePlugNPlayStatus_Type = MwlEnableDisableOption
_MwMeshProfilePlugNPlayStatus_Object = MibTableColumn
mwMeshProfilePlugNPlayStatus = _MwMeshProfilePlugNPlayStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 6),
    _MwMeshProfilePlugNPlayStatus_Type()
)
mwMeshProfilePlugNPlayStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfilePlugNPlayStatus.setStatus("current")
_MwMeshProfileRowStatus_Type = RowStatus
_MwMeshProfileRowStatus_Object = MibTableColumn
mwMeshProfileRowStatus = _MwMeshProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 24),
    _MwMeshProfileRowStatus_Type()
)
mwMeshProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileRowStatus.setStatus("current")
_MwMeshApTable_Object = MibTable
mwMeshApTable = _MwMeshApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8)
)
if mibBuilder.loadTexts:
    mwMeshApTable.setStatus("current")
_MwMeshApEntry_Object = MibTableRow
mwMeshApEntry = _MwMeshApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1)
)
mwMeshApEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwMeshApTableIndex"),
)
if mibBuilder.loadTexts:
    mwMeshApEntry.setStatus("current")
_MwMeshApTableIndex_Type = Integer32
_MwMeshApTableIndex_Object = MibTableColumn
mwMeshApTableIndex = _MwMeshApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 1),
    _MwMeshApTableIndex_Type()
)
mwMeshApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwMeshApTableIndex.setStatus("current")


class _MwMeshApName_Type(DisplayString):
    """Custom type mwMeshApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwMeshApName_Type.__name__ = "DisplayString"
_MwMeshApName_Object = MibTableColumn
mwMeshApName = _MwMeshApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 2),
    _MwMeshApName_Type()
)
mwMeshApName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApName.setStatus("current")
_MwMeshApAPId_Type = Integer32
_MwMeshApAPId_Object = MibTableColumn
mwMeshApAPId = _MwMeshApAPId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 3),
    _MwMeshApAPId_Type()
)
mwMeshApAPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApAPId.setStatus("current")
_MwMeshApAPMac_Type = MacAddress
_MwMeshApAPMac_Object = MibTableColumn
mwMeshApAPMac = _MwMeshApAPMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 4),
    _MwMeshApAPMac_Type()
)
mwMeshApAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApAPMac.setStatus("current")
_MwMeshApAvailState_Type = MwlAvailabilityStatus
_MwMeshApAvailState_Object = MibTableColumn
mwMeshApAvailState = _MwMeshApAvailState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 5),
    _MwMeshApAvailState_Type()
)
mwMeshApAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApAvailState.setStatus("current")
_MwMeshApParentAPId_Type = Integer32
_MwMeshApParentAPId_Object = MibTableColumn
mwMeshApParentAPId = _MwMeshApParentAPId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 6),
    _MwMeshApParentAPId_Type()
)
mwMeshApParentAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApParentAPId.setStatus("current")
_MwMeshApParentAPMac_Type = MacAddress
_MwMeshApParentAPMac_Object = MibTableColumn
mwMeshApParentAPMac = _MwMeshApParentAPMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 7),
    _MwMeshApParentAPMac_Type()
)
mwMeshApParentAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApParentAPMac.setStatus("current")
_MwMeshApUpIfIndex_Type = Integer32
_MwMeshApUpIfIndex_Object = MibTableColumn
mwMeshApUpIfIndex = _MwMeshApUpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 8),
    _MwMeshApUpIfIndex_Type()
)
mwMeshApUpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApUpIfIndex.setStatus("current")
_MwMeshApUpChannel_Type = Integer32
_MwMeshApUpChannel_Object = MibTableColumn
mwMeshApUpChannel = _MwMeshApUpChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 9),
    _MwMeshApUpChannel_Type()
)
mwMeshApUpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApUpChannel.setStatus("current")
_MwMeshApDownIfIndex_Type = Integer32
_MwMeshApDownIfIndex_Object = MibTableColumn
mwMeshApDownIfIndex = _MwMeshApDownIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 10),
    _MwMeshApDownIfIndex_Type()
)
mwMeshApDownIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDownIfIndex.setStatus("current")
_MwMeshApDownChannel_Type = Integer32
_MwMeshApDownChannel_Object = MibTableColumn
mwMeshApDownChannel = _MwMeshApDownChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 11),
    _MwMeshApDownChannel_Type()
)
mwMeshApDownChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDownChannel.setStatus("current")


class _MwMeshApDescr_Type(DisplayString):
    """Custom type mwMeshApDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_MwMeshApDescr_Type.__name__ = "DisplayString"
_MwMeshApDescr_Object = MibTableColumn
mwMeshApDescr = _MwMeshApDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 12),
    _MwMeshApDescr_Type()
)
mwMeshApDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDescr.setStatus("current")
_MwMeshApRowStatus_Type = RowStatus
_MwMeshApRowStatus_Object = MibTableColumn
mwMeshApRowStatus = _MwMeshApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 13),
    _MwMeshApRowStatus_Type()
)
mwMeshApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApRowStatus.setStatus("current")
_MwDefaultIf80211SettingsTable_Object = MibTable
mwDefaultIf80211SettingsTable = _MwDefaultIf80211SettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9)
)
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsTable.setStatus("current")
_MwDefaultIf80211SettingsEntry_Object = MibTableRow
mwDefaultIf80211SettingsEntry = _MwDefaultIf80211SettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1)
)
mwDefaultIf80211SettingsEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwDefaultIf80211SettingsTableIndex"),
)
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsEntry.setStatus("current")
_MwDefaultIf80211SettingsTableIndex_Type = Integer32
_MwDefaultIf80211SettingsTableIndex_Object = MibTableColumn
mwDefaultIf80211SettingsTableIndex = _MwDefaultIf80211SettingsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 1),
    _MwDefaultIf80211SettingsTableIndex_Type()
)
mwDefaultIf80211SettingsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsTableIndex.setStatus("current")
_MwDefaultIf80211SettingsIfIndex_Type = Integer32
_MwDefaultIf80211SettingsIfIndex_Object = MibTableColumn
mwDefaultIf80211SettingsIfIndex = _MwDefaultIf80211SettingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 2),
    _MwDefaultIf80211SettingsIfIndex_Type()
)
mwDefaultIf80211SettingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfIndex.setStatus("current")
_MwDefaultIf80211SettingsIfMode_Type = MwlApIfConfigModeType
_MwDefaultIf80211SettingsIfMode_Object = MibTableColumn
mwDefaultIf80211SettingsIfMode = _MwDefaultIf80211SettingsIfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 3),
    _MwDefaultIf80211SettingsIfMode_Type()
)
mwDefaultIf80211SettingsIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfMode.setStatus("current")
_MwDefaultIf80211SettingsIfChannel_Type = Integer32
_MwDefaultIf80211SettingsIfChannel_Object = MibTableColumn
mwDefaultIf80211SettingsIfChannel = _MwDefaultIf80211SettingsIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 4),
    _MwDefaultIf80211SettingsIfChannel_Type()
)
mwDefaultIf80211SettingsIfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfChannel.setStatus("current")
_MwDefaultIf80211SettingsIfChannelWidth_Type = MwlChannelWidth
_MwDefaultIf80211SettingsIfChannelWidth_Object = MibTableColumn
mwDefaultIf80211SettingsIfChannelWidth = _MwDefaultIf80211SettingsIfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 5),
    _MwDefaultIf80211SettingsIfChannelWidth_Type()
)
mwDefaultIf80211SettingsIfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfChannelWidth.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-WLAN-MIB",
    **{"mwConfigWlan": mwConfigWlan,
       "mwIf80211CapabilityTable": mwIf80211CapabilityTable,
       "mwIf80211CapabilityEntry": mwIf80211CapabilityEntry,
       "mwIf80211CapabilityTableIndex": mwIf80211CapabilityTableIndex,
       "mwIf80211CapabilityIfAGain": mwIf80211CapabilityIfAGain,
       "mwIf80211CapabilityIfBgGain": mwIf80211CapabilityIfBgGain,
       "mwIf80211CapabilityIfLinkType": mwIf80211CapabilityIfLinkType,
       "mwIf80211CapabilityIfAntennaSet": mwIf80211CapabilityIfAntennaSet,
       "mwIf80211CapabilityIfConnectorType": mwIf80211CapabilityIfConnectorType,
       "mwIf80211CapabilityIfIndex": mwIf80211CapabilityIfIndex,
       "mwIf80211CapabilityApHwType": mwIf80211CapabilityApHwType,
       "mwIf80211CapabilityIfNmsNodeId": mwIf80211CapabilityIfNmsNodeId,
       "mwIf80211CapabilityIfConnectorGain": mwIf80211CapabilityIfConnectorGain,
       "mwIf80211CapabilityIfAntennaLocation": mwIf80211CapabilityIfAntennaLocation,
       "mwIf80211CapabilityIfAntennaConnector": mwIf80211CapabilityIfAntennaConnector,
       "mwEssTable": mwEssTable,
       "mwEssEntry": mwEssEntry,
       "mwEssTableIndex": mwEssTableIndex,
       "mwEssSsId": mwEssSsId,
       "mwEssId": mwEssId,
       "mwEssGreName": mwEssGreName,
       "mwEssVlanName": mwEssVlanName,
       "mwEssVcellType": mwEssVcellType,
       "mwEssL2Bridging": mwEssL2Bridging,
       "mwEssDTIMPeriod": mwEssDTIMPeriod,
       "mwEssVlanSupport": mwEssVlanSupport,
       "mwEssBaseTxRates": mwEssBaseTxRates,
       "mwPublishEssId": mwPublishEssId,
       "mwEssABaseTxRates": mwEssABaseTxRates,
       "mwEssGBaseTxRates": mwEssGBaseTxRates,
       "mwEssDataplaneMode": mwEssDataplaneMode,
       "mwEssBGBaseTxRates": mwEssBGBaseTxRates,
       "mwEssANBaseTxRates": mwEssANBaseTxRates,
       "mwEssBeaconInterval": mwEssBeaconInterval,
       "mwEssAllowMulticast": mwEssAllowMulticast,
       "mwEssBGNBaseTxRates": mwEssBGNBaseTxRates,
       "mwEssCountermeasure": mwEssCountermeasure,
       "mwEssJoinOnDiscovery": mwEssJoinOnDiscovery,
       "mwEssANBaseHTTxRates": mwEssANBaseHTTxRates,
       "mwEssSupportedTxRates": mwEssSupportedTxRates,
       "mwEssBGNBaseHTTxRates": mwEssBGNBaseHTTxRates,
       "mwEssASupportedTxRates": mwEssASupportedTxRates,
       "mwEssGSupportedTxRates": mwEssGSupportedTxRates,
       "mwEssBGSupportedTxRates": mwEssBGSupportedTxRates,
       "mwEssANSupportedTxRates": mwEssANSupportedTxRates,
       "mwEssSecurityProfileName": mwEssSecurityProfileName,
       "mwEssBGNSupportedTxRates": mwEssBGNSupportedTxRates,
       "mwEssANSupportedHTTxRates": mwEssANSupportedHTTxRates,
       "mwEssBGNSupportedHTTxRates": mwEssBGNSupportedHTTxRates,
       "mwEssAPsShareChannelAndBssId": mwEssAPsShareChannelAndBssId,
       "mwEssAccountingInterimInterval": mwEssAccountingInterimInterval,
       "mwEssPrimaryAccountingRadiusName": mwEssPrimaryAccountingRadiusName,
       "mwEssSecondaryAccountingRadiusName": mwEssSecondaryAccountingRadiusName,
       "mwEssMulticastMACTransparency": mwEssMulticastMACTransparency,
       "mwEssBandSteering": mwEssBandSteering,
       "mwEssBandSteeringTimeout": mwEssBandSteeringTimeout,
       "mwEssApVlanTag": mwEssApVlanTag,
       "mwEssEnableApVlanPriority": mwEssEnableApVlanPriority,
       "mwEssOwner": mwEssOwner,
       "mwEssIDOverflowFrom": mwEssIDOverflowFrom,
       "mwEssEnableAPSD": mwEssEnableAPSD,
       "mwEssState": mwEssState,
       "mwEssMultipleIpPerStation": mwEssMultipleIpPerStation,
       "mwEssMulticastToUnicastConversion": mwEssMulticastToUnicastConversion,
       "mwEssEfOverride": mwEssEfOverride,
       "mwEssPapBroadcastSsid": mwEssPapBroadcastSsid,
       "mwEssVirtualInterfaceProfileName": mwEssVirtualInterfaceProfileName,
       "mwEssWirelessToWirelessIsolation": mwEssWirelessToWirelessIsolation,
       "mwEssRowStatus": mwEssRowStatus,
       "mwIf80211Table": mwIf80211Table,
       "mwIf80211Entry": mwIf80211Entry,
       "mwIf80211TableIndex": mwIf80211TableIndex,
       "mwIf80211IfMode": mwIf80211IfMode,
       "mwIf80211IfDescr": mwIf80211IfDescr,
       "mwIf80211IfApMode": mwIf80211IfApMode,
       "mwIf80211IfChannel": mwIf80211IfChannel,
       "mwIf80211NOnlyMode": mwIf80211NOnlyMode,
       "mwIf80211IfMimoMode": mwIf80211IfMimoMode,
       "mwIf80211channelWidth": mwIf80211channelWidth,
       "mwIf80211IfAdminStatus": mwIf80211IfAdminStatus,
       "mwIf80211IfTxPowerHigh": mwIf80211IfTxPowerHigh,
       "mwIf80211IfBgProtectionMode": mwIf80211IfBgProtectionMode,
       "mwIf80211IfShortPreambleFlag": mwIf80211IfShortPreambleFlag,
       "mwIf80211IfMtu": mwIf80211IfMtu,
       "mwIf80211IfType": mwIf80211IfType,
       "mwIf80211IfIndex": mwIf80211IfIndex,
       "mwIf80211IfNodeId": mwIf80211IfNodeId,
       "mwIf80211ApHwType": mwIf80211ApHwType,
       "mwIf80211IfNodeName": mwIf80211IfNodeName,
       "mwIf80211IfOperStatus": mwIf80211IfOperStatus,
       "mwIf80211IfLastChange": mwIf80211IfLastChange,
       "mwIf80211IfOperChannel": mwIf80211IfOperChannel,
       "mwIf80211IfBandSupport": mwIf80211IfBandSupport,
       "mwIf80211DualabgSupport": mwIf80211DualabgSupport,
       "mwIf80211IfNumAntennas": mwIf80211IfNumAntennas,
       "mwIf80211Rf6Rf7VcellMode": mwIf80211Rf6Rf7VcellMode,
       "mwIf80211ProbeResponseThreshold": mwIf80211ProbeResponseThreshold,
       "mwIf80211IfMeshStatus": mwIf80211IfMeshStatus,
       "mwIf80211UplinkType": mwIf80211UplinkType,
       "mwIf80211IfHtProtectionMode": mwIf80211IfHtProtectionMode,
       "mwEssApTable": mwEssApTable,
       "mwEssApEntry": mwEssApEntry,
       "mwEssApTableIndex": mwEssApTableIndex,
       "mwEssApEssId": mwEssApEssId,
       "mwEssApIfIndex": mwEssApIfIndex,
       "mwEssApMaxCalls": mwEssApMaxCalls,
       "mwEssApApNodeId": mwEssApApNodeId,
       "mwEssApBssId": mwEssApBssId,
       "mwEssApIfMode": mwEssApIfMode,
       "mwEssApApNodeName": mwEssApApNodeName,
       "mwEssApBaseTxRates": mwEssApBaseTxRates,
       "mwEssApChannelNumber": mwEssApChannelNumber,
       "mwEssApIfOperChannel": mwEssApIfOperChannel,
       "mwEssApSupportedTxRates": mwEssApSupportedTxRates,
       "mwEssApAdminMode": mwEssApAdminMode,
       "mwEssApRowStatus": mwEssApRowStatus,
       "mwMeshProfileTable": mwMeshProfileTable,
       "mwMeshProfileEntry": mwMeshProfileEntry,
       "mwMeshProfileTableIndex": mwMeshProfileTableIndex,
       "mwMeshProfileName": mwMeshProfileName,
       "mwMeshProfileDescr": mwMeshProfileDescr,
       "mwMeshProfilePSK": mwMeshProfilePSK,
       "mwMeshProfileAdminMode": mwMeshProfileAdminMode,
       "mwMeshProfilePlugNPlayStatus": mwMeshProfilePlugNPlayStatus,
       "mwMeshProfileRowStatus": mwMeshProfileRowStatus,
       "mwMeshApTable": mwMeshApTable,
       "mwMeshApEntry": mwMeshApEntry,
       "mwMeshApTableIndex": mwMeshApTableIndex,
       "mwMeshApName": mwMeshApName,
       "mwMeshApAPId": mwMeshApAPId,
       "mwMeshApAPMac": mwMeshApAPMac,
       "mwMeshApAvailState": mwMeshApAvailState,
       "mwMeshApParentAPId": mwMeshApParentAPId,
       "mwMeshApParentAPMac": mwMeshApParentAPMac,
       "mwMeshApUpIfIndex": mwMeshApUpIfIndex,
       "mwMeshApUpChannel": mwMeshApUpChannel,
       "mwMeshApDownIfIndex": mwMeshApDownIfIndex,
       "mwMeshApDownChannel": mwMeshApDownChannel,
       "mwMeshApDescr": mwMeshApDescr,
       "mwMeshApRowStatus": mwMeshApRowStatus,
       "mwDefaultIf80211SettingsTable": mwDefaultIf80211SettingsTable,
       "mwDefaultIf80211SettingsEntry": mwDefaultIf80211SettingsEntry,
       "mwDefaultIf80211SettingsTableIndex": mwDefaultIf80211SettingsTableIndex,
       "mwDefaultIf80211SettingsIfIndex": mwDefaultIf80211SettingsIfIndex,
       "mwDefaultIf80211SettingsIfMode": mwDefaultIf80211SettingsIfMode,
       "mwDefaultIf80211SettingsIfChannel": mwDefaultIf80211SettingsIfChannel,
       "mwDefaultIf80211SettingsIfChannelWidth": mwDefaultIf80211SettingsIfChannelWidth}
)
