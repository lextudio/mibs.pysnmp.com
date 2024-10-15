# SNMP MIB module (PROXIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROXIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:54 2024
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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

proxim = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 841)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString20(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class DisplayString32(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DisplayString55(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 55),
    )



class DisplayString80(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class InterfaceBitmask(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ObjStatus(Integer32, TextualConvention):
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
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 0))
    )



class ObjStatusActive(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deleted", 3),
          ("inactive", 2))
    )



class Password(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )



class V3Password(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )



class WEPKeyType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1)
)
_DeviceConfig_ObjectIdentity = ObjectIdentity
deviceConfig = _DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1)
)
_WirelessIf_ObjectIdentity = ObjectIdentity
wirelessIf = _WirelessIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1)
)
_WirelessIfPropertiesTable_Object = MibTable
wirelessIfPropertiesTable = _WirelessIfPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wirelessIfPropertiesTable.setStatus("current")
_WirelessIfPropertiesTableEntry_Object = MibTableRow
wirelessIfPropertiesTableEntry = _WirelessIfPropertiesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1)
)
wirelessIfPropertiesTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfPropertiesTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfPropertiesTableEntry.setStatus("current")


class _WirelessIfPropertiesTableIndex_Type(Unsigned32):
    """Custom type wirelessIfPropertiesTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIfPropertiesTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfPropertiesTableIndex_Object = MibTableColumn
wirelessIfPropertiesTableIndex = _WirelessIfPropertiesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 1),
    _WirelessIfPropertiesTableIndex_Type()
)
wirelessIfPropertiesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfPropertiesTableIndex.setStatus("current")


class _WirelessIfPropertiesRadioStatus_Type(Integer32):
    """Custom type wirelessIfPropertiesRadioStatus based on Integer32"""
    defaultValue = 1

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


_WirelessIfPropertiesRadioStatus_Type.__name__ = "Integer32"
_WirelessIfPropertiesRadioStatus_Object = MibTableColumn
wirelessIfPropertiesRadioStatus = _WirelessIfPropertiesRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 2),
    _WirelessIfPropertiesRadioStatus_Type()
)
wirelessIfPropertiesRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfPropertiesRadioStatus.setStatus("current")


class _WirelessIfOperationalMode_Type(DisplayString):
    """Custom type wirelessIfOperationalMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WirelessIfOperationalMode_Type.__name__ = "DisplayString"
_WirelessIfOperationalMode_Object = MibTableColumn
wirelessIfOperationalMode = _WirelessIfOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 3),
    _WirelessIfOperationalMode_Type()
)
wirelessIfOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfOperationalMode.setStatus("current")
_WirelessIfSupportedOperationalMode_Type = DisplayString
_WirelessIfSupportedOperationalMode_Object = MibTableColumn
wirelessIfSupportedOperationalMode = _WirelessIfSupportedOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 4),
    _WirelessIfSupportedOperationalMode_Type()
)
wirelessIfSupportedOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfSupportedOperationalMode.setStatus("current")
_WirelessIfCurrentChannelBandwidth_Type = Unsigned32
_WirelessIfCurrentChannelBandwidth_Object = MibTableColumn
wirelessIfCurrentChannelBandwidth = _WirelessIfCurrentChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 5),
    _WirelessIfCurrentChannelBandwidth_Type()
)
wirelessIfCurrentChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfCurrentChannelBandwidth.setStatus("current")
_WirelessIfSupportedChannelBandwidth_Type = DisplayString
_WirelessIfSupportedChannelBandwidth_Object = MibTableColumn
wirelessIfSupportedChannelBandwidth = _WirelessIfSupportedChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 6),
    _WirelessIfSupportedChannelBandwidth_Type()
)
wirelessIfSupportedChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfSupportedChannelBandwidth.setStatus("current")


class _WirelessIfAutoChannelSelection_Type(Integer32):
    """Custom type wirelessIfAutoChannelSelection based on Integer32"""
    defaultValue = 1

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


_WirelessIfAutoChannelSelection_Type.__name__ = "Integer32"
_WirelessIfAutoChannelSelection_Object = MibTableColumn
wirelessIfAutoChannelSelection = _WirelessIfAutoChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 7),
    _WirelessIfAutoChannelSelection_Type()
)
wirelessIfAutoChannelSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfAutoChannelSelection.setStatus("current")
_WirelessIfCurrentOperatingChannel_Type = Unsigned32
_WirelessIfCurrentOperatingChannel_Object = MibTableColumn
wirelessIfCurrentOperatingChannel = _WirelessIfCurrentOperatingChannel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 8),
    _WirelessIfCurrentOperatingChannel_Type()
)
wirelessIfCurrentOperatingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfCurrentOperatingChannel.setStatus("current")


class _WirelessIfSupportedChannels_Type(OctetString):
    """Custom type wirelessIfSupportedChannels based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_WirelessIfSupportedChannels_Type.__name__ = "OctetString"
_WirelessIfSupportedChannels_Object = MibTableColumn
wirelessIfSupportedChannels = _WirelessIfSupportedChannels_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 9),
    _WirelessIfSupportedChannels_Type()
)
wirelessIfSupportedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfSupportedChannels.setStatus("current")


class _WirelessIfAutoRateSelection_Type(Integer32):
    """Custom type wirelessIfAutoRateSelection based on Integer32"""
    defaultValue = 1

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


_WirelessIfAutoRateSelection_Type.__name__ = "Integer32"
_WirelessIfAutoRateSelection_Object = MibTableColumn
wirelessIfAutoRateSelection = _WirelessIfAutoRateSelection_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 10),
    _WirelessIfAutoRateSelection_Type()
)
wirelessIfAutoRateSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfAutoRateSelection.setStatus("current")


class _WirelessIfTransmittedRate_Type(Unsigned32):
    """Custom type wirelessIfTransmittedRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WirelessIfTransmittedRate_Type.__name__ = "Unsigned32"
_WirelessIfTransmittedRate_Object = MibTableColumn
wirelessIfTransmittedRate = _WirelessIfTransmittedRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 11),
    _WirelessIfTransmittedRate_Type()
)
wirelessIfTransmittedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfTransmittedRate.setStatus("current")
_WirelessIfSupportedRate_Type = DisplayString
_WirelessIfSupportedRate_Object = MibTableColumn
wirelessIfSupportedRate = _WirelessIfSupportedRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 12),
    _WirelessIfSupportedRate_Type()
)
wirelessIfSupportedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfSupportedRate.setStatus("current")


class _WirelessIfVAPRTSThreshold_Type(Unsigned32):
    """Custom type wirelessIfVAPRTSThreshold based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2346),
    )


_WirelessIfVAPRTSThreshold_Type.__name__ = "Unsigned32"
_WirelessIfVAPRTSThreshold_Object = MibTableColumn
wirelessIfVAPRTSThreshold = _WirelessIfVAPRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 13),
    _WirelessIfVAPRTSThreshold_Type()
)
wirelessIfVAPRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPRTSThreshold.setStatus("current")


class _WirelessIfVAPBeaconInterval_Type(Unsigned32):
    """Custom type wirelessIfVAPBeaconInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WirelessIfVAPBeaconInterval_Type.__name__ = "Unsigned32"
_WirelessIfVAPBeaconInterval_Object = MibTableColumn
wirelessIfVAPBeaconInterval = _WirelessIfVAPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 14),
    _WirelessIfVAPBeaconInterval_Type()
)
wirelessIfVAPBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPBeaconInterval.setStatus("current")


class _WirelessIfTPC_Type(Unsigned32):
    """Custom type wirelessIfTPC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_WirelessIfTPC_Type.__name__ = "Unsigned32"
_WirelessIfTPC_Object = MibTableColumn
wirelessIfTPC = _WirelessIfTPC_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 15),
    _WirelessIfTPC_Type()
)
wirelessIfTPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfTPC.setStatus("current")


class _WirelessIfCellSize_Type(Integer32):
    """Custom type wirelessIfCellSize based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 3),
          ("medium", 2),
          ("small", 1))
    )


_WirelessIfCellSize_Type.__name__ = "Integer32"
_WirelessIfCellSize_Object = MibTableColumn
wirelessIfCellSize = _WirelessIfCellSize_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 16),
    _WirelessIfCellSize_Type()
)
wirelessIfCellSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfCellSize.setStatus("current")


class _WirelessIfDTIM_Type(Unsigned32):
    """Custom type wirelessIfDTIM based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WirelessIfDTIM_Type.__name__ = "Unsigned32"
_WirelessIfDTIM_Object = MibTableColumn
wirelessIfDTIM = _WirelessIfDTIM_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 17),
    _WirelessIfDTIM_Type()
)
wirelessIfDTIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDTIM.setStatus("current")


class _WirelessIfAntennaGain_Type(Unsigned32):
    """Custom type wirelessIfAntennaGain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_WirelessIfAntennaGain_Type.__name__ = "Unsigned32"
_WirelessIfAntennaGain_Object = MibTableColumn
wirelessIfAntennaGain = _WirelessIfAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 18),
    _WirelessIfAntennaGain_Type()
)
wirelessIfAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfAntennaGain.setStatus("current")
_WirelessIfCurrentActiveChannel_Type = Unsigned32
_WirelessIfCurrentActiveChannel_Object = MibTableColumn
wirelessIfCurrentActiveChannel = _WirelessIfCurrentActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 19),
    _WirelessIfCurrentActiveChannel_Type()
)
wirelessIfCurrentActiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfCurrentActiveChannel.setStatus("current")


class _WirelessIfSatelliteDensity_Type(Integer32):
    """Custom type wirelessIfSatelliteDensity based on Integer32"""
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
        *(("disable", 1),
          ("large", 2),
          ("medium", 3),
          ("micro", 6),
          ("mini", 5),
          ("small", 4))
    )


_WirelessIfSatelliteDensity_Type.__name__ = "Integer32"
_WirelessIfSatelliteDensity_Object = MibTableColumn
wirelessIfSatelliteDensity = _WirelessIfSatelliteDensity_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 20),
    _WirelessIfSatelliteDensity_Type()
)
wirelessIfSatelliteDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfSatelliteDensity.setStatus("current")


class _WirelessIfMPOperationalMode_Type(Integer32):
    """Custom type wirelessIfMPOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highThroughput", 1),
          ("legacy", 2))
    )


_WirelessIfMPOperationalMode_Type.__name__ = "Integer32"
_WirelessIfMPOperationalMode_Object = MibTableColumn
wirelessIfMPOperationalMode = _WirelessIfMPOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 21),
    _WirelessIfMPOperationalMode_Type()
)
wirelessIfMPOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfMPOperationalMode.setStatus("current")


class _WirelessIfChannelWaitTime_Type(Unsigned32):
    """Custom type wirelessIfChannelWaitTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WirelessIfChannelWaitTime_Type.__name__ = "Unsigned32"
_WirelessIfChannelWaitTime_Object = MibTableColumn
wirelessIfChannelWaitTime = _WirelessIfChannelWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 22),
    _WirelessIfChannelWaitTime_Type()
)
wirelessIfChannelWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfChannelWaitTime.setStatus("current")


class _WirelessIfActiveTPC_Type(Unsigned32):
    """Custom type wirelessIfActiveTPC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_WirelessIfActiveTPC_Type.__name__ = "Unsigned32"
_WirelessIfActiveTPC_Object = MibTableColumn
wirelessIfActiveTPC = _WirelessIfActiveTPC_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 23),
    _WirelessIfActiveTPC_Type()
)
wirelessIfActiveTPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfActiveTPC.setStatus("current")


class _WirelessIfDfsNumSatWithRadarForFreqSwitch_Type(Unsigned32):
    """Custom type wirelessIfDfsNumSatWithRadarForFreqSwitch based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WirelessIfDfsNumSatWithRadarForFreqSwitch_Type.__name__ = "Unsigned32"
_WirelessIfDfsNumSatWithRadarForFreqSwitch_Object = MibTableColumn
wirelessIfDfsNumSatWithRadarForFreqSwitch = _WirelessIfDfsNumSatWithRadarForFreqSwitch_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 24),
    _WirelessIfDfsNumSatWithRadarForFreqSwitch_Type()
)
wirelessIfDfsNumSatWithRadarForFreqSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDfsNumSatWithRadarForFreqSwitch.setStatus("current")


class _WirelessIfDfsStatus_Type(Integer32):
    """Custom type wirelessIfDfsStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfDfsStatus_Type.__name__ = "Integer32"
_WirelessIfDfsStatus_Object = MibTableColumn
wirelessIfDfsStatus = _WirelessIfDfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 1, 1, 25),
    _WirelessIfDfsStatus_Type()
)
wirelessIfDfsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDfsStatus.setStatus("current")
_WirelessIf11nPropertiesTable_Object = MibTable
wirelessIf11nPropertiesTable = _WirelessIf11nPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesTable.setStatus("current")
_WirelessIf11nPropertiesTableEntry_Object = MibTableRow
wirelessIf11nPropertiesTableEntry = _WirelessIf11nPropertiesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1)
)
wirelessIf11nPropertiesTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIf11nPropertiesTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesTableEntry.setStatus("current")


class _WirelessIf11nPropertiesTableIndex_Type(Unsigned32):
    """Custom type wirelessIf11nPropertiesTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIf11nPropertiesTableIndex_Type.__name__ = "Unsigned32"
_WirelessIf11nPropertiesTableIndex_Object = MibTableColumn
wirelessIf11nPropertiesTableIndex = _WirelessIf11nPropertiesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 1),
    _WirelessIf11nPropertiesTableIndex_Type()
)
wirelessIf11nPropertiesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesTableIndex.setStatus("current")


class _WirelessIf11nPropertiesAMPDUStatus_Type(Integer32):
    """Custom type wirelessIf11nPropertiesAMPDUStatus based on Integer32"""
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


_WirelessIf11nPropertiesAMPDUStatus_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesAMPDUStatus_Object = MibTableColumn
wirelessIf11nPropertiesAMPDUStatus = _WirelessIf11nPropertiesAMPDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 2),
    _WirelessIf11nPropertiesAMPDUStatus_Type()
)
wirelessIf11nPropertiesAMPDUStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesAMPDUStatus.setStatus("current")


class _WirelessIf11nPropertiesAMPDUMaxNumFrames_Type(Unsigned32):
    """Custom type wirelessIf11nPropertiesAMPDUMaxNumFrames based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WirelessIf11nPropertiesAMPDUMaxNumFrames_Type.__name__ = "Unsigned32"
_WirelessIf11nPropertiesAMPDUMaxNumFrames_Object = MibTableColumn
wirelessIf11nPropertiesAMPDUMaxNumFrames = _WirelessIf11nPropertiesAMPDUMaxNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 3),
    _WirelessIf11nPropertiesAMPDUMaxNumFrames_Type()
)
wirelessIf11nPropertiesAMPDUMaxNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesAMPDUMaxNumFrames.setStatus("current")


class _WirelessIf11nPropertiesAMPDUMaxFrameSize_Type(Unsigned32):
    """Custom type wirelessIf11nPropertiesAMPDUMaxFrameSize based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_WirelessIf11nPropertiesAMPDUMaxFrameSize_Type.__name__ = "Unsigned32"
_WirelessIf11nPropertiesAMPDUMaxFrameSize_Object = MibTableColumn
wirelessIf11nPropertiesAMPDUMaxFrameSize = _WirelessIf11nPropertiesAMPDUMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 4),
    _WirelessIf11nPropertiesAMPDUMaxFrameSize_Type()
)
wirelessIf11nPropertiesAMPDUMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesAMPDUMaxFrameSize.setStatus("current")


class _WirelessIf11nPropertiesAMSDUStatus_Type(Integer32):
    """Custom type wirelessIf11nPropertiesAMSDUStatus based on Integer32"""
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


_WirelessIf11nPropertiesAMSDUStatus_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesAMSDUStatus_Object = MibTableColumn
wirelessIf11nPropertiesAMSDUStatus = _WirelessIf11nPropertiesAMSDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 5),
    _WirelessIf11nPropertiesAMSDUStatus_Type()
)
wirelessIf11nPropertiesAMSDUStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesAMSDUStatus.setStatus("current")


class _WirelessIf11nPropertiesAMSDUMaxFrameSize_Type(Unsigned32):
    """Custom type wirelessIf11nPropertiesAMSDUMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 4096),
    )


_WirelessIf11nPropertiesAMSDUMaxFrameSize_Type.__name__ = "Unsigned32"
_WirelessIf11nPropertiesAMSDUMaxFrameSize_Object = MibTableColumn
wirelessIf11nPropertiesAMSDUMaxFrameSize = _WirelessIf11nPropertiesAMSDUMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 6),
    _WirelessIf11nPropertiesAMSDUMaxFrameSize_Type()
)
wirelessIf11nPropertiesAMSDUMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesAMSDUMaxFrameSize.setStatus("current")


class _WirelessIf11nPropertiesFrequencyExtension_Type(Integer32):
    """Custom type wirelessIf11nPropertiesFrequencyExtension based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerExtensionChannel", 2),
          ("upperExtensionChannel", 1))
    )


_WirelessIf11nPropertiesFrequencyExtension_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesFrequencyExtension_Object = MibTableColumn
wirelessIf11nPropertiesFrequencyExtension = _WirelessIf11nPropertiesFrequencyExtension_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 7),
    _WirelessIf11nPropertiesFrequencyExtension_Type()
)
wirelessIf11nPropertiesFrequencyExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesFrequencyExtension.setStatus("current")


class _WirelessIf11nPropertiesGuardInterval_Type(Integer32):
    """Custom type wirelessIf11nPropertiesGuardInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullGI-800nSec", 2),
          ("shortGI-400nSec", 1))
    )


_WirelessIf11nPropertiesGuardInterval_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesGuardInterval_Object = MibTableColumn
wirelessIf11nPropertiesGuardInterval = _WirelessIf11nPropertiesGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 8),
    _WirelessIf11nPropertiesGuardInterval_Type()
)
wirelessIf11nPropertiesGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesGuardInterval.setStatus("current")


class _WirelessIf11nPropertiesTxAntennas_Type(Integer32):
    """Custom type wirelessIf11nPropertiesTxAntennas based on Integer32"""
    defaultValue = 7

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
        *(("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WirelessIf11nPropertiesTxAntennas_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesTxAntennas_Object = MibTableColumn
wirelessIf11nPropertiesTxAntennas = _WirelessIf11nPropertiesTxAntennas_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 9),
    _WirelessIf11nPropertiesTxAntennas_Type()
)
wirelessIf11nPropertiesTxAntennas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesTxAntennas.setStatus("current")


class _WirelessIf11nPropertiesRxAntennas_Type(Integer32):
    """Custom type wirelessIf11nPropertiesRxAntennas based on Integer32"""
    defaultValue = 7

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
        *(("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WirelessIf11nPropertiesRxAntennas_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesRxAntennas_Object = MibTableColumn
wirelessIf11nPropertiesRxAntennas = _WirelessIf11nPropertiesRxAntennas_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 10),
    _WirelessIf11nPropertiesRxAntennas_Type()
)
wirelessIf11nPropertiesRxAntennas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesRxAntennas.setStatus("current")


class _WirelessIf11nPropertiesNumOfSpatialStreams_Type(Integer32):
    """Custom type wirelessIf11nPropertiesNumOfSpatialStreams based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("dual", 2),
          ("single", 1))
    )


_WirelessIf11nPropertiesNumOfSpatialStreams_Type.__name__ = "Integer32"
_WirelessIf11nPropertiesNumOfSpatialStreams_Object = MibTableColumn
wirelessIf11nPropertiesNumOfSpatialStreams = _WirelessIf11nPropertiesNumOfSpatialStreams_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 11),
    _WirelessIf11nPropertiesNumOfSpatialStreams_Type()
)
wirelessIf11nPropertiesNumOfSpatialStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesNumOfSpatialStreams.setStatus("current")


class _WirelessIf11nPropertiesSupportedTxAntennas_Type(DisplayString):
    """Custom type wirelessIf11nPropertiesSupportedTxAntennas based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WirelessIf11nPropertiesSupportedTxAntennas_Type.__name__ = "DisplayString"
_WirelessIf11nPropertiesSupportedTxAntennas_Object = MibTableColumn
wirelessIf11nPropertiesSupportedTxAntennas = _WirelessIf11nPropertiesSupportedTxAntennas_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 12),
    _WirelessIf11nPropertiesSupportedTxAntennas_Type()
)
wirelessIf11nPropertiesSupportedTxAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesSupportedTxAntennas.setStatus("current")


class _WirelessIf11nPropertiesSupportedRxAntennas_Type(DisplayString):
    """Custom type wirelessIf11nPropertiesSupportedRxAntennas based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WirelessIf11nPropertiesSupportedRxAntennas_Type.__name__ = "DisplayString"
_WirelessIf11nPropertiesSupportedRxAntennas_Object = MibTableColumn
wirelessIf11nPropertiesSupportedRxAntennas = _WirelessIf11nPropertiesSupportedRxAntennas_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 2, 1, 13),
    _WirelessIf11nPropertiesSupportedRxAntennas_Type()
)
wirelessIf11nPropertiesSupportedRxAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIf11nPropertiesSupportedRxAntennas.setStatus("current")
_WirelessIfVAPTable_Object = MibTable
wirelessIfVAPTable = _WirelessIfVAPTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wirelessIfVAPTable.setStatus("current")
_WirelessIfVAPTableEntry_Object = MibTableRow
wirelessIfVAPTableEntry = _WirelessIfVAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1)
)
wirelessIfVAPTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfVAPTableIndex"),
    (0, "PROXIM-MIB", "wirelessIfVAPTableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfVAPTableEntry.setStatus("current")


class _WirelessIfVAPTableIndex_Type(Unsigned32):
    """Custom type wirelessIfVAPTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIfVAPTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfVAPTableIndex_Object = MibTableColumn
wirelessIfVAPTableIndex = _WirelessIfVAPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 1),
    _WirelessIfVAPTableIndex_Type()
)
wirelessIfVAPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfVAPTableIndex.setStatus("current")


class _WirelessIfVAPTableSecIndex_Type(Unsigned32):
    """Custom type wirelessIfVAPTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WirelessIfVAPTableSecIndex_Type.__name__ = "Unsigned32"
_WirelessIfVAPTableSecIndex_Object = MibTableColumn
wirelessIfVAPTableSecIndex = _WirelessIfVAPTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 2),
    _WirelessIfVAPTableSecIndex_Type()
)
wirelessIfVAPTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfVAPTableSecIndex.setStatus("current")


class _WirelessIfVAPType_Type(Integer32):
    """Custom type wirelessIfVAPType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ap", 1)
    )


_WirelessIfVAPType_Type.__name__ = "Integer32"
_WirelessIfVAPType_Object = MibTableColumn
wirelessIfVAPType = _WirelessIfVAPType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 3),
    _WirelessIfVAPType_Type()
)
wirelessIfVAPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPType.setStatus("current")


class _WirelessIfVAPSSID_Type(DisplayString):
    """Custom type wirelessIfVAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessIfVAPSSID_Type.__name__ = "DisplayString"
_WirelessIfVAPSSID_Object = MibTableColumn
wirelessIfVAPSSID = _WirelessIfVAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 4),
    _WirelessIfVAPSSID_Type()
)
wirelessIfVAPSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPSSID.setStatus("current")
_WirelessIfVAPBSSID_Type = MacAddress
_WirelessIfVAPBSSID_Object = MibTableColumn
wirelessIfVAPBSSID = _WirelessIfVAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 5),
    _WirelessIfVAPBSSID_Type()
)
wirelessIfVAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfVAPBSSID.setStatus("current")


class _WirelessIfVAPBroadcastSSID_Type(Integer32):
    """Custom type wirelessIfVAPBroadcastSSID based on Integer32"""
    defaultValue = 1

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


_WirelessIfVAPBroadcastSSID_Type.__name__ = "Integer32"
_WirelessIfVAPBroadcastSSID_Object = MibTableColumn
wirelessIfVAPBroadcastSSID = _WirelessIfVAPBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 6),
    _WirelessIfVAPBroadcastSSID_Type()
)
wirelessIfVAPBroadcastSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPBroadcastSSID.setStatus("current")


class _WirelessIfVAPFragmentationThreshold_Type(Unsigned32):
    """Custom type wirelessIfVAPFragmentationThreshold based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WirelessIfVAPFragmentationThreshold_Type.__name__ = "Unsigned32"
_WirelessIfVAPFragmentationThreshold_Object = MibTableColumn
wirelessIfVAPFragmentationThreshold = _WirelessIfVAPFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 7),
    _WirelessIfVAPFragmentationThreshold_Type()
)
wirelessIfVAPFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPFragmentationThreshold.setStatus("current")


class _WirelessIfVAPSecurityProfileName_Type(DisplayString):
    """Custom type wirelessIfVAPSecurityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessIfVAPSecurityProfileName_Type.__name__ = "DisplayString"
_WirelessIfVAPSecurityProfileName_Object = MibTableColumn
wirelessIfVAPSecurityProfileName = _WirelessIfVAPSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 8),
    _WirelessIfVAPSecurityProfileName_Type()
)
wirelessIfVAPSecurityProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPSecurityProfileName.setStatus("current")


class _WirelessIfVAPRadiusProfileName_Type(DisplayString):
    """Custom type wirelessIfVAPRadiusProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessIfVAPRadiusProfileName_Type.__name__ = "DisplayString"
_WirelessIfVAPRadiusProfileName_Object = MibTableColumn
wirelessIfVAPRadiusProfileName = _WirelessIfVAPRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 9),
    _WirelessIfVAPRadiusProfileName_Type()
)
wirelessIfVAPRadiusProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPRadiusProfileName.setStatus("current")


class _WirelessIfVAPVLANID_Type(VlanId):
    """Custom type wirelessIfVAPVLANID based on VlanId"""
    defaultValue = -1


_WirelessIfVAPVLANID_Object = MibTableColumn
wirelessIfVAPVLANID = _WirelessIfVAPVLANID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 10),
    _WirelessIfVAPVLANID_Type()
)
wirelessIfVAPVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPVLANID.setStatus("current")


class _WirelessIfVAPVLANPriority_Type(Unsigned32):
    """Custom type wirelessIfVAPVLANPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WirelessIfVAPVLANPriority_Type.__name__ = "Unsigned32"
_WirelessIfVAPVLANPriority_Object = MibTableColumn
wirelessIfVAPVLANPriority = _WirelessIfVAPVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 11),
    _WirelessIfVAPVLANPriority_Type()
)
wirelessIfVAPVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPVLANPriority.setStatus("current")


class _WirelessIfVAPQoSProfileName_Type(DisplayString):
    """Custom type wirelessIfVAPQoSProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessIfVAPQoSProfileName_Type.__name__ = "DisplayString"
_WirelessIfVAPQoSProfileName_Object = MibTableColumn
wirelessIfVAPQoSProfileName = _WirelessIfVAPQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 12),
    _WirelessIfVAPQoSProfileName_Type()
)
wirelessIfVAPQoSProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPQoSProfileName.setStatus("current")


class _WirelessIfVAPMACACLStatus_Type(Integer32):
    """Custom type wirelessIfVAPMACACLStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfVAPMACACLStatus_Type.__name__ = "Integer32"
_WirelessIfVAPMACACLStatus_Object = MibTableColumn
wirelessIfVAPMACACLStatus = _WirelessIfVAPMACACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 13),
    _WirelessIfVAPMACACLStatus_Type()
)
wirelessIfVAPMACACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPMACACLStatus.setStatus("current")


class _WirelessIfVAPRadiusMACACLStatus_Type(Integer32):
    """Custom type wirelessIfVAPRadiusMACACLStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfVAPRadiusMACACLStatus_Type.__name__ = "Integer32"
_WirelessIfVAPRadiusMACACLStatus_Object = MibTableColumn
wirelessIfVAPRadiusMACACLStatus = _WirelessIfVAPRadiusMACACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 14),
    _WirelessIfVAPRadiusMACACLStatus_Type()
)
wirelessIfVAPRadiusMACACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPRadiusMACACLStatus.setStatus("current")


class _WirelessIfVAPRadiusAccStatus_Type(Integer32):
    """Custom type wirelessIfVAPRadiusAccStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfVAPRadiusAccStatus_Type.__name__ = "Integer32"
_WirelessIfVAPRadiusAccStatus_Object = MibTableColumn
wirelessIfVAPRadiusAccStatus = _WirelessIfVAPRadiusAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 15),
    _WirelessIfVAPRadiusAccStatus_Type()
)
wirelessIfVAPRadiusAccStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPRadiusAccStatus.setStatus("current")


class _WirelessIfVAPStatus_Type(Integer32):
    """Custom type wirelessIfVAPStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_WirelessIfVAPStatus_Type.__name__ = "Integer32"
_WirelessIfVAPStatus_Object = MibTableColumn
wirelessIfVAPStatus = _WirelessIfVAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 3, 1, 16),
    _WirelessIfVAPStatus_Type()
)
wirelessIfVAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfVAPStatus.setStatus("current")
_WirelessIfWORPTable_Object = MibTable
wirelessIfWORPTable = _WirelessIfWORPTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wirelessIfWORPTable.setStatus("current")
_WirelessIfWORPTableEntry_Object = MibTableRow
wirelessIfWORPTableEntry = _WirelessIfWORPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1)
)
wirelessIfWORPTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfWORPTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfWORPTableEntry.setStatus("current")


class _WirelessIfWORPTableIndex_Type(Unsigned32):
    """Custom type wirelessIfWORPTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIfWORPTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfWORPTableIndex_Object = MibTableColumn
wirelessIfWORPTableIndex = _WirelessIfWORPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 1),
    _WirelessIfWORPTableIndex_Type()
)
wirelessIfWORPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPTableIndex.setStatus("current")
_WirelessIfWORPMode_Type = DisplayString
_WirelessIfWORPMode_Object = MibTableColumn
wirelessIfWORPMode = _WirelessIfWORPMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 2),
    _WirelessIfWORPMode_Type()
)
wirelessIfWORPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPMode.setStatus("current")


class _WirelessIfWORPBaseStationName_Type(DisplayString):
    """Custom type wirelessIfWORPBaseStationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessIfWORPBaseStationName_Type.__name__ = "DisplayString"
_WirelessIfWORPBaseStationName_Object = MibTableColumn
wirelessIfWORPBaseStationName = _WirelessIfWORPBaseStationName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 3),
    _WirelessIfWORPBaseStationName_Type()
)
wirelessIfWORPBaseStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPBaseStationName.setStatus("current")


class _WirelessIfWORPNetworkName_Type(DisplayString):
    """Custom type wirelessIfWORPNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessIfWORPNetworkName_Type.__name__ = "DisplayString"
_WirelessIfWORPNetworkName_Object = MibTableColumn
wirelessIfWORPNetworkName = _WirelessIfWORPNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 4),
    _WirelessIfWORPNetworkName_Type()
)
wirelessIfWORPNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPNetworkName.setStatus("current")


class _WirelessIfWORPMaxSatellites_Type(Unsigned32):
    """Custom type wirelessIfWORPMaxSatellites based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_WirelessIfWORPMaxSatellites_Type.__name__ = "Unsigned32"
_WirelessIfWORPMaxSatellites_Object = MibTableColumn
wirelessIfWORPMaxSatellites = _WirelessIfWORPMaxSatellites_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 5),
    _WirelessIfWORPMaxSatellites_Type()
)
wirelessIfWORPMaxSatellites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPMaxSatellites.setStatus("current")


class _WirelessIfWORPMTU_Type(Unsigned32):
    """Custom type wirelessIfWORPMTU based on Unsigned32"""
    defaultValue = 3808

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 3808),
    )


_WirelessIfWORPMTU_Type.__name__ = "Unsigned32"
_WirelessIfWORPMTU_Object = MibTableColumn
wirelessIfWORPMTU = _WirelessIfWORPMTU_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 6),
    _WirelessIfWORPMTU_Type()
)
wirelessIfWORPMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPMTU.setStatus("current")


class _WirelessIfWORPSuperPacketing_Type(Integer32):
    """Custom type wirelessIfWORPSuperPacketing based on Integer32"""
    defaultValue = 1

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


_WirelessIfWORPSuperPacketing_Type.__name__ = "Integer32"
_WirelessIfWORPSuperPacketing_Object = MibTableColumn
wirelessIfWORPSuperPacketing = _WirelessIfWORPSuperPacketing_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 7),
    _WirelessIfWORPSuperPacketing_Type()
)
wirelessIfWORPSuperPacketing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPSuperPacketing.setStatus("current")


class _WirelessIfWORPSleepMode_Type(Integer32):
    """Custom type wirelessIfWORPSleepMode based on Integer32"""
    defaultValue = 1

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


_WirelessIfWORPSleepMode_Type.__name__ = "Integer32"
_WirelessIfWORPSleepMode_Object = MibTableColumn
wirelessIfWORPSleepMode = _WirelessIfWORPSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 8),
    _WirelessIfWORPSleepMode_Type()
)
wirelessIfWORPSleepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPSleepMode.setStatus("current")


class _WirelessIfWORPMultiFrameBursting_Type(Integer32):
    """Custom type wirelessIfWORPMultiFrameBursting based on Integer32"""
    defaultValue = 1

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


_WirelessIfWORPMultiFrameBursting_Type.__name__ = "Integer32"
_WirelessIfWORPMultiFrameBursting_Object = MibTableColumn
wirelessIfWORPMultiFrameBursting = _WirelessIfWORPMultiFrameBursting_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 9),
    _WirelessIfWORPMultiFrameBursting_Type()
)
wirelessIfWORPMultiFrameBursting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPMultiFrameBursting.setStatus("current")


class _WirelessIfWORPRegistrationTimeout_Type(Unsigned32):
    """Custom type wirelessIfWORPRegistrationTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WirelessIfWORPRegistrationTimeout_Type.__name__ = "Unsigned32"
_WirelessIfWORPRegistrationTimeout_Object = MibTableColumn
wirelessIfWORPRegistrationTimeout = _WirelessIfWORPRegistrationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 11),
    _WirelessIfWORPRegistrationTimeout_Type()
)
wirelessIfWORPRegistrationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPRegistrationTimeout.setStatus("current")


class _WirelessIfWORPRetries_Type(Unsigned32):
    """Custom type wirelessIfWORPRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WirelessIfWORPRetries_Type.__name__ = "Unsigned32"
_WirelessIfWORPRetries_Object = MibTableColumn
wirelessIfWORPRetries = _WirelessIfWORPRetries_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 12),
    _WirelessIfWORPRetries_Type()
)
wirelessIfWORPRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPRetries.setStatus("current")
_WirelessIfWORPTxRate_Type = Unsigned32
_WirelessIfWORPTxRate_Object = MibTableColumn
wirelessIfWORPTxRate = _WirelessIfWORPTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 13),
    _WirelessIfWORPTxRate_Type()
)
wirelessIfWORPTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPTxRate.setStatus("current")
_WirelessIfWORPSupportedTxRate_Type = DisplayString
_WirelessIfWORPSupportedTxRate_Object = MibTableColumn
wirelessIfWORPSupportedTxRate = _WirelessIfWORPSupportedTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 14),
    _WirelessIfWORPSupportedTxRate_Type()
)
wirelessIfWORPSupportedTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPSupportedTxRate.setStatus("current")


class _WirelessIfWORPInputBandwidthLimit_Type(Unsigned32):
    """Custom type wirelessIfWORPInputBandwidthLimit based on Unsigned32"""
    defaultValue = 3072000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 307200),
    )


_WirelessIfWORPInputBandwidthLimit_Type.__name__ = "Unsigned32"
_WirelessIfWORPInputBandwidthLimit_Object = MibTableColumn
wirelessIfWORPInputBandwidthLimit = _WirelessIfWORPInputBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 15),
    _WirelessIfWORPInputBandwidthLimit_Type()
)
wirelessIfWORPInputBandwidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPInputBandwidthLimit.setStatus("current")


class _WirelessIfWORPOutputBandwidthLimit_Type(Unsigned32):
    """Custom type wirelessIfWORPOutputBandwidthLimit based on Unsigned32"""
    defaultValue = 307200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 307200),
    )


_WirelessIfWORPOutputBandwidthLimit_Type.__name__ = "Unsigned32"
_WirelessIfWORPOutputBandwidthLimit_Object = MibTableColumn
wirelessIfWORPOutputBandwidthLimit = _WirelessIfWORPOutputBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 16),
    _WirelessIfWORPOutputBandwidthLimit_Type()
)
wirelessIfWORPOutputBandwidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPOutputBandwidthLimit.setStatus("current")


class _WirelessIfWORPBandwidthLimitType_Type(Integer32):
    """Custom type wirelessIfWORPBandwidthLimitType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("policing", 1),
          ("shaping", 2))
    )


_WirelessIfWORPBandwidthLimitType_Type.__name__ = "Integer32"
_WirelessIfWORPBandwidthLimitType_Object = MibTableColumn
wirelessIfWORPBandwidthLimitType = _WirelessIfWORPBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 17),
    _WirelessIfWORPBandwidthLimitType_Type()
)
wirelessIfWORPBandwidthLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPBandwidthLimitType.setStatus("current")


class _WirelessIfWORPSecurityProfileIndex_Type(Integer32):
    """Custom type wirelessIfWORPSecurityProfileIndex based on Integer32"""
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
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WirelessIfWORPSecurityProfileIndex_Type.__name__ = "Integer32"
_WirelessIfWORPSecurityProfileIndex_Object = MibTableColumn
wirelessIfWORPSecurityProfileIndex = _WirelessIfWORPSecurityProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 18),
    _WirelessIfWORPSecurityProfileIndex_Type()
)
wirelessIfWORPSecurityProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPSecurityProfileIndex.setStatus("current")


class _WirelessIfWORPRadiusProfileIndex_Type(Integer32):
    """Custom type wirelessIfWORPRadiusProfileIndex based on Integer32"""
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
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WirelessIfWORPRadiusProfileIndex_Type.__name__ = "Integer32"
_WirelessIfWORPRadiusProfileIndex_Object = MibTableColumn
wirelessIfWORPRadiusProfileIndex = _WirelessIfWORPRadiusProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 19),
    _WirelessIfWORPRadiusProfileIndex_Type()
)
wirelessIfWORPRadiusProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPRadiusProfileIndex.setStatus("current")


class _WirelessIfWORPMACACLStatus_Type(Integer32):
    """Custom type wirelessIfWORPMACACLStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfWORPMACACLStatus_Type.__name__ = "Integer32"
_WirelessIfWORPMACACLStatus_Object = MibTableColumn
wirelessIfWORPMACACLStatus = _WirelessIfWORPMACACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 20),
    _WirelessIfWORPMACACLStatus_Type()
)
wirelessIfWORPMACACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPMACACLStatus.setStatus("current")


class _WirelessIfWORPRadiusMACACLStatus_Type(Integer32):
    """Custom type wirelessIfWORPRadiusMACACLStatus based on Integer32"""
    defaultValue = 2

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


_WirelessIfWORPRadiusMACACLStatus_Type.__name__ = "Integer32"
_WirelessIfWORPRadiusMACACLStatus_Object = MibTableColumn
wirelessIfWORPRadiusMACACLStatus = _WirelessIfWORPRadiusMACACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 21),
    _WirelessIfWORPRadiusMACACLStatus_Type()
)
wirelessIfWORPRadiusMACACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPRadiusMACACLStatus.setStatus("current")


class _WirelessIfWORPRadiusAccStatus_Type(Integer32):
    """Custom type wirelessIfWORPRadiusAccStatus based on Integer32"""
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


_WirelessIfWORPRadiusAccStatus_Type.__name__ = "Integer32"
_WirelessIfWORPRadiusAccStatus_Object = MibTableColumn
wirelessIfWORPRadiusAccStatus = _WirelessIfWORPRadiusAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 22),
    _WirelessIfWORPRadiusAccStatus_Type()
)
wirelessIfWORPRadiusAccStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wirelessIfWORPRadiusAccStatus.setStatus("current")
_WirelessIfWORPIntfMacAddress_Type = MacAddress
_WirelessIfWORPIntfMacAddress_Object = MibTableColumn
wirelessIfWORPIntfMacAddress = _WirelessIfWORPIntfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 23),
    _WirelessIfWORPIntfMacAddress_Type()
)
wirelessIfWORPIntfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPIntfMacAddress.setStatus("current")


class _WirelessIfWORPAutoMultiFrameBursting_Type(Integer32):
    """Custom type wirelessIfWORPAutoMultiFrameBursting based on Integer32"""
    defaultValue = 1

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


_WirelessIfWORPAutoMultiFrameBursting_Type.__name__ = "Integer32"
_WirelessIfWORPAutoMultiFrameBursting_Object = MibTableColumn
wirelessIfWORPAutoMultiFrameBursting = _WirelessIfWORPAutoMultiFrameBursting_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 4, 1, 24),
    _WirelessIfWORPAutoMultiFrameBursting_Type()
)
wirelessIfWORPAutoMultiFrameBursting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPAutoMultiFrameBursting.setStatus("current")
_WirelessIfDDRSTable_Object = MibTable
wirelessIfDDRSTable = _WirelessIfDDRSTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wirelessIfDDRSTable.setStatus("current")
_WirelessIfDDRSTableEntry_Object = MibTableRow
wirelessIfDDRSTableEntry = _WirelessIfDDRSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1)
)
wirelessIfDDRSTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfDDRSTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfDDRSTableEntry.setStatus("current")
_WirelessIfDDRSTableIndex_Type = Unsigned32
_WirelessIfDDRSTableIndex_Object = MibTableColumn
wirelessIfDDRSTableIndex = _WirelessIfDDRSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 1),
    _WirelessIfDDRSTableIndex_Type()
)
wirelessIfDDRSTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfDDRSTableIndex.setStatus("current")


class _WirelessIfDDRSStatus_Type(Integer32):
    """Custom type wirelessIfDDRSStatus based on Integer32"""
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


_WirelessIfDDRSStatus_Type.__name__ = "Integer32"
_WirelessIfDDRSStatus_Object = MibTableColumn
wirelessIfDDRSStatus = _WirelessIfDDRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 2),
    _WirelessIfDDRSStatus_Type()
)
wirelessIfDDRSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSStatus.setStatus("current")
_WirelessIfDDRSDefDataRate_Type = Unsigned32
_WirelessIfDDRSDefDataRate_Object = MibTableColumn
wirelessIfDDRSDefDataRate = _WirelessIfDDRSDefDataRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 3),
    _WirelessIfDDRSDefDataRate_Type()
)
wirelessIfDDRSDefDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSDefDataRate.setStatus("current")
_WirelessIfDDRSMaxDataRate_Type = Unsigned32
_WirelessIfDDRSMaxDataRate_Object = MibTableColumn
wirelessIfDDRSMaxDataRate = _WirelessIfDDRSMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 4),
    _WirelessIfDDRSMaxDataRate_Type()
)
wirelessIfDDRSMaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSMaxDataRate.setStatus("current")


class _WirelessIfDDRSIncrAvgSNRThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSIncrAvgSNRThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WirelessIfDDRSIncrAvgSNRThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSIncrAvgSNRThrld_Object = MibTableColumn
wirelessIfDDRSIncrAvgSNRThrld = _WirelessIfDDRSIncrAvgSNRThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 5),
    _WirelessIfDDRSIncrAvgSNRThrld_Type()
)
wirelessIfDDRSIncrAvgSNRThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSIncrAvgSNRThrld.setStatus("current")


class _WirelessIfDDRSIncrReqSNRThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSIncrReqSNRThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WirelessIfDDRSIncrReqSNRThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSIncrReqSNRThrld_Object = MibTableColumn
wirelessIfDDRSIncrReqSNRThrld = _WirelessIfDDRSIncrReqSNRThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 6),
    _WirelessIfDDRSIncrReqSNRThrld_Type()
)
wirelessIfDDRSIncrReqSNRThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSIncrReqSNRThrld.setStatus("current")


class _WirelessIfDDRSDecrReqSNRThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSDecrReqSNRThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WirelessIfDDRSDecrReqSNRThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSDecrReqSNRThrld_Object = MibTableColumn
wirelessIfDDRSDecrReqSNRThrld = _WirelessIfDDRSDecrReqSNRThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 7),
    _WirelessIfDDRSDecrReqSNRThrld_Type()
)
wirelessIfDDRSDecrReqSNRThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSDecrReqSNRThrld.setStatus("current")


class _WirelessIfDDRSIncrReTxPercentThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSIncrReTxPercentThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WirelessIfDDRSIncrReTxPercentThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSIncrReTxPercentThrld_Object = MibTableColumn
wirelessIfDDRSIncrReTxPercentThrld = _WirelessIfDDRSIncrReTxPercentThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 8),
    _WirelessIfDDRSIncrReTxPercentThrld_Type()
)
wirelessIfDDRSIncrReTxPercentThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSIncrReTxPercentThrld.setStatus("current")


class _WirelessIfDDRSDecrReTxPercentThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSDecrReTxPercentThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WirelessIfDDRSDecrReTxPercentThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSDecrReTxPercentThrld_Object = MibTableColumn
wirelessIfDDRSDecrReTxPercentThrld = _WirelessIfDDRSDecrReTxPercentThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 9),
    _WirelessIfDDRSDecrReTxPercentThrld_Type()
)
wirelessIfDDRSDecrReTxPercentThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSDecrReTxPercentThrld.setStatus("current")


class _WirelessIfDDRSAggressiveIndex_Type(Unsigned32):
    """Custom type wirelessIfDDRSAggressiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WirelessIfDDRSAggressiveIndex_Type.__name__ = "Unsigned32"
_WirelessIfDDRSAggressiveIndex_Object = MibTableColumn
wirelessIfDDRSAggressiveIndex = _WirelessIfDDRSAggressiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 10),
    _WirelessIfDDRSAggressiveIndex_Type()
)
wirelessIfDDRSAggressiveIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSAggressiveIndex.setStatus("current")


class _WirelessIfDDRSChainBalThrld_Type(Unsigned32):
    """Custom type wirelessIfDDRSChainBalThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_WirelessIfDDRSChainBalThrld_Type.__name__ = "Unsigned32"
_WirelessIfDDRSChainBalThrld_Object = MibTableColumn
wirelessIfDDRSChainBalThrld = _WirelessIfDDRSChainBalThrld_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 11),
    _WirelessIfDDRSChainBalThrld_Type()
)
wirelessIfDDRSChainBalThrld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSChainBalThrld.setStatus("current")


class _WirelessIfDDRSRateBackOffInt_Type(Unsigned32):
    """Custom type wirelessIfDDRSRateBackOffInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_WirelessIfDDRSRateBackOffInt_Type.__name__ = "Unsigned32"
_WirelessIfDDRSRateBackOffInt_Object = MibTableColumn
wirelessIfDDRSRateBackOffInt = _WirelessIfDDRSRateBackOffInt_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 12),
    _WirelessIfDDRSRateBackOffInt_Type()
)
wirelessIfDDRSRateBackOffInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSRateBackOffInt.setStatus("current")


class _WirelessIfDDRSRateBlackListInt_Type(Unsigned32):
    """Custom type wirelessIfDDRSRateBlackListInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_WirelessIfDDRSRateBlackListInt_Type.__name__ = "Unsigned32"
_WirelessIfDDRSRateBlackListInt_Object = MibTableColumn
wirelessIfDDRSRateBlackListInt = _WirelessIfDDRSRateBlackListInt_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 5, 1, 13),
    _WirelessIfDDRSRateBlackListInt_Type()
)
wirelessIfDDRSRateBlackListInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSRateBlackListInt.setStatus("current")
_WirelessIfDDRSMinReqSNRTable_Object = MibTable
wirelessIfDDRSMinReqSNRTable = _WirelessIfDDRSMinReqSNRTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wirelessIfDDRSMinReqSNRTable.setStatus("current")
_WirelessIfDDRSMinReqSNRTableEntry_Object = MibTableRow
wirelessIfDDRSMinReqSNRTableEntry = _WirelessIfDDRSMinReqSNRTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1)
)
wirelessIfDDRSMinReqSNRTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfDDRSMinReqSNRTableIndex"),
    (0, "PROXIM-MIB", "wirelessIfDDRSMinReqSNRTableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfDDRSMinReqSNRTableEntry.setStatus("current")
_WirelessIfDDRSMinReqSNRTableIndex_Type = Unsigned32
_WirelessIfDDRSMinReqSNRTableIndex_Object = MibTableColumn
wirelessIfDDRSMinReqSNRTableIndex = _WirelessIfDDRSMinReqSNRTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1, 1),
    _WirelessIfDDRSMinReqSNRTableIndex_Type()
)
wirelessIfDDRSMinReqSNRTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfDDRSMinReqSNRTableIndex.setStatus("current")
_WirelessIfDDRSMinReqSNRTableSecIndex_Type = Unsigned32
_WirelessIfDDRSMinReqSNRTableSecIndex_Object = MibTableColumn
wirelessIfDDRSMinReqSNRTableSecIndex = _WirelessIfDDRSMinReqSNRTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1, 2),
    _WirelessIfDDRSMinReqSNRTableSecIndex_Type()
)
wirelessIfDDRSMinReqSNRTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfDDRSMinReqSNRTableSecIndex.setStatus("current")
_WirelessIfDDRSPhyModulation_Type = DisplayString
_WirelessIfDDRSPhyModulation_Object = MibTableColumn
wirelessIfDDRSPhyModulation = _WirelessIfDDRSPhyModulation_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1, 3),
    _WirelessIfDDRSPhyModulation_Type()
)
wirelessIfDDRSPhyModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfDDRSPhyModulation.setStatus("current")
_WirelessIfDDRSDataRate_Type = DisplayString
_WirelessIfDDRSDataRate_Object = MibTableColumn
wirelessIfDDRSDataRate = _WirelessIfDDRSDataRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1, 4),
    _WirelessIfDDRSDataRate_Type()
)
wirelessIfDDRSDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfDDRSDataRate.setStatus("current")


class _WirelessIfDDRSMinReqSNR_Type(Unsigned32):
    """Custom type wirelessIfDDRSMinReqSNR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WirelessIfDDRSMinReqSNR_Type.__name__ = "Unsigned32"
_WirelessIfDDRSMinReqSNR_Object = MibTableColumn
wirelessIfDDRSMinReqSNR = _WirelessIfDDRSMinReqSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 1, 6, 1, 5),
    _WirelessIfDDRSMinReqSNR_Type()
)
wirelessIfDDRSMinReqSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfDDRSMinReqSNR.setStatus("current")
_EthernetIf_ObjectIdentity = ObjectIdentity
ethernetIf = _EthernetIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2)
)
_EthernetIfPropertiesTable_Object = MibTable
ethernetIfPropertiesTable = _EthernetIfPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ethernetIfPropertiesTable.setStatus("current")
_EthernetIfPropertiesTableEntry_Object = MibTableRow
ethernetIfPropertiesTableEntry = _EthernetIfPropertiesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1)
)
ethernetIfPropertiesTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "ethernetIfPropertiesTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetIfPropertiesTableEntry.setStatus("current")


class _EthernetIfPropertiesTableIndex_Type(Unsigned32):
    """Custom type ethernetIfPropertiesTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_EthernetIfPropertiesTableIndex_Type.__name__ = "Unsigned32"
_EthernetIfPropertiesTableIndex_Object = MibTableColumn
ethernetIfPropertiesTableIndex = _EthernetIfPropertiesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 1),
    _EthernetIfPropertiesTableIndex_Type()
)
ethernetIfPropertiesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfPropertiesTableIndex.setStatus("current")
_EthernetIfMACAddress_Type = MacAddress
_EthernetIfMACAddress_Object = MibTableColumn
ethernetIfMACAddress = _EthernetIfMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 2),
    _EthernetIfMACAddress_Type()
)
ethernetIfMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfMACAddress.setStatus("current")


class _EthernetIfSupportedSpeed_Type(Integer32):
    """Custom type ethernetIfSupportedSpeed based on Integer32"""
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
        *(("auto", 1),
          ("hundredMbit", 4),
          ("oneGbps", 2),
          ("tenMbps", 3),
          ("unknown", 5))
    )


_EthernetIfSupportedSpeed_Type.__name__ = "Integer32"
_EthernetIfSupportedSpeed_Object = MibTableColumn
ethernetIfSupportedSpeed = _EthernetIfSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 3),
    _EthernetIfSupportedSpeed_Type()
)
ethernetIfSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfSupportedSpeed.setStatus("current")


class _EthernetIfSupportedTxMode_Type(Integer32):
    """Custom type ethernetIfSupportedTxMode based on Integer32"""
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
        *(("auto", 3),
          ("fullDuplex", 2),
          ("halfDuplex", 1),
          ("unknown", 4))
    )


_EthernetIfSupportedTxMode_Type.__name__ = "Integer32"
_EthernetIfSupportedTxMode_Object = MibTableColumn
ethernetIfSupportedTxMode = _EthernetIfSupportedTxMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 4),
    _EthernetIfSupportedTxMode_Type()
)
ethernetIfSupportedTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfSupportedTxMode.setStatus("current")


class _EthernetIfTxModeAndSpeed_Type(Integer32):
    """Custom type ethernetIfTxModeAndSpeed based on Integer32"""
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
        *(("auto", 1),
          ("hundredMbps-fullDuplex", 5),
          ("hundredMbps-halfDuplex", 4),
          ("oneGbps-fullDuplex", 6),
          ("tenMbps-fullDuplex", 3),
          ("tenMbps-halfDuplex", 2))
    )


_EthernetIfTxModeAndSpeed_Type.__name__ = "Integer32"
_EthernetIfTxModeAndSpeed_Object = MibTableColumn
ethernetIfTxModeAndSpeed = _EthernetIfTxModeAndSpeed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 5),
    _EthernetIfTxModeAndSpeed_Type()
)
ethernetIfTxModeAndSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfTxModeAndSpeed.setStatus("current")
_EthernetIfSupportedModes_Type = DisplayString
_EthernetIfSupportedModes_Object = MibTableColumn
ethernetIfSupportedModes = _EthernetIfSupportedModes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 6),
    _EthernetIfSupportedModes_Type()
)
ethernetIfSupportedModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfSupportedModes.setStatus("current")


class _EthernetIfAdminStatus_Type(Integer32):
    """Custom type ethernetIfAdminStatus based on Integer32"""
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


_EthernetIfAdminStatus_Type.__name__ = "Integer32"
_EthernetIfAdminStatus_Object = MibTableColumn
ethernetIfAdminStatus = _EthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 7),
    _EthernetIfAdminStatus_Type()
)
ethernetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfAdminStatus.setStatus("current")


class _EthernetIfAutoShutDown_Type(Integer32):
    """Custom type ethernetIfAutoShutDown based on Integer32"""
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


_EthernetIfAutoShutDown_Type.__name__ = "Integer32"
_EthernetIfAutoShutDown_Object = MibTableColumn
ethernetIfAutoShutDown = _EthernetIfAutoShutDown_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 1, 2, 1, 1, 8),
    _EthernetIfAutoShutDown_Type()
)
ethernetIfAutoShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfAutoShutDown.setStatus("current")
_ApSecurity_ObjectIdentity = ObjectIdentity
apSecurity = _ApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2)
)
_WirelessSecurity_ObjectIdentity = ObjectIdentity
wirelessSecurity = _WirelessSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1)
)
_WirelessSecurityCfgTable_Object = MibTable
wirelessSecurityCfgTable = _WirelessSecurityCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wirelessSecurityCfgTable.setStatus("current")
_WirelessSecurityCfgTableEntry_Object = MibTableRow
wirelessSecurityCfgTableEntry = _WirelessSecurityCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1)
)
wirelessSecurityCfgTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessSecurityCfgTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessSecurityCfgTableEntry.setStatus("current")


class _WirelessSecurityCfgTableIndex_Type(Unsigned32):
    """Custom type wirelessSecurityCfgTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WirelessSecurityCfgTableIndex_Type.__name__ = "Unsigned32"
_WirelessSecurityCfgTableIndex_Object = MibTableColumn
wirelessSecurityCfgTableIndex = _WirelessSecurityCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 1),
    _WirelessSecurityCfgTableIndex_Type()
)
wirelessSecurityCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessSecurityCfgTableIndex.setStatus("current")


class _WirelessSecurityCfgprofileName_Type(DisplayString):
    """Custom type wirelessSecurityCfgprofileName based on DisplayString"""
    defaultValue = OctetString("DEFAULT SECURITY")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessSecurityCfgprofileName_Type.__name__ = "DisplayString"
_WirelessSecurityCfgprofileName_Object = MibTableColumn
wirelessSecurityCfgprofileName = _WirelessSecurityCfgprofileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 2),
    _WirelessSecurityCfgprofileName_Type()
)
wirelessSecurityCfgprofileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgprofileName.setStatus("current")


class _WirelessSecurityCfgAuthenticationMode_Type(Integer32):
    """Custom type wirelessSecurityCfgAuthenticationMode based on Integer32"""
    defaultValue = 1

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
        *(("dot1x", 4),
          ("none", 1),
          ("psk", 3),
          ("wep", 2),
          ("worp", 5))
    )


_WirelessSecurityCfgAuthenticationMode_Type.__name__ = "Integer32"
_WirelessSecurityCfgAuthenticationMode_Object = MibTableColumn
wirelessSecurityCfgAuthenticationMode = _WirelessSecurityCfgAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 3),
    _WirelessSecurityCfgAuthenticationMode_Type()
)
wirelessSecurityCfgAuthenticationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wirelessSecurityCfgAuthenticationMode.setStatus("current")


class _WirelessSecurityCfgKeyIndex_Type(Integer32):
    """Custom type wirelessSecurityCfgKeyIndex based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WirelessSecurityCfgKeyIndex_Type.__name__ = "Integer32"
_WirelessSecurityCfgKeyIndex_Object = MibTableColumn
wirelessSecurityCfgKeyIndex = _WirelessSecurityCfgKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 4),
    _WirelessSecurityCfgKeyIndex_Type()
)
wirelessSecurityCfgKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgKeyIndex.setStatus("current")
_WirelessSecurityCfgKey1_Type = WEPKeyType
_WirelessSecurityCfgKey1_Object = MibTableColumn
wirelessSecurityCfgKey1 = _WirelessSecurityCfgKey1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 5),
    _WirelessSecurityCfgKey1_Type()
)
wirelessSecurityCfgKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgKey1.setStatus("current")


class _WirelessSecurityCfgdot1xWepKeyLength_Type(Integer32):
    """Custom type wirelessSecurityCfgdot1xWepKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wep128", 2),
          ("wep64", 1))
    )


_WirelessSecurityCfgdot1xWepKeyLength_Type.__name__ = "Integer32"
_WirelessSecurityCfgdot1xWepKeyLength_Object = MibTableColumn
wirelessSecurityCfgdot1xWepKeyLength = _WirelessSecurityCfgdot1xWepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 6),
    _WirelessSecurityCfgdot1xWepKeyLength_Type()
)
wirelessSecurityCfgdot1xWepKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgdot1xWepKeyLength.setStatus("current")


class _WirelessSecurityCfgEncryptionType_Type(Integer32):
    """Custom type wirelessSecurityCfgEncryptionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aes-ccm", 7),
          ("none", 0),
          ("tkip", 6),
          ("wep", 1),
          ("wpa-tkip", 2),
          ("wpa-wpa2aes-tkip", 4),
          ("wpa2-aes", 3),
          ("wpa2-aes-ccm", 5))
    )


_WirelessSecurityCfgEncryptionType_Type.__name__ = "Integer32"
_WirelessSecurityCfgEncryptionType_Object = MibTableColumn
wirelessSecurityCfgEncryptionType = _WirelessSecurityCfgEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 7),
    _WirelessSecurityCfgEncryptionType_Type()
)
wirelessSecurityCfgEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgEncryptionType.setStatus("current")


class _WirelessSecurityCfgPSK_Type(DisplayString):
    """Custom type wirelessSecurityCfgPSK based on DisplayString"""
    defaultValue = OctetString("123456789")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessSecurityCfgPSK_Type.__name__ = "DisplayString"
_WirelessSecurityCfgPSK_Object = MibTableColumn
wirelessSecurityCfgPSK = _WirelessSecurityCfgPSK_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 8),
    _WirelessSecurityCfgPSK_Type()
)
wirelessSecurityCfgPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgPSK.setStatus("current")


class _WirelessSecurityCfgRekeyingInterval_Type(Unsigned32):
    """Custom type wirelessSecurityCfgRekeyingInterval based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 65535),
    )


_WirelessSecurityCfgRekeyingInterval_Type.__name__ = "Unsigned32"
_WirelessSecurityCfgRekeyingInterval_Object = MibTableColumn
wirelessSecurityCfgRekeyingInterval = _WirelessSecurityCfgRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 9),
    _WirelessSecurityCfgRekeyingInterval_Type()
)
wirelessSecurityCfgRekeyingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgRekeyingInterval.setStatus("current")


class _WirelessSecurityCfgEntryStatus_Type(RowStatus):
    """Custom type wirelessSecurityCfgEntryStatus based on RowStatus"""


_WirelessSecurityCfgEntryStatus_Object = MibTableColumn
wirelessSecurityCfgEntryStatus = _WirelessSecurityCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 10),
    _WirelessSecurityCfgEntryStatus_Type()
)
wirelessSecurityCfgEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgEntryStatus.setStatus("current")


class _WirelessSecurityCfgNetworkSecret_Type(DisplayString):
    """Custom type wirelessSecurityCfgNetworkSecret based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_WirelessSecurityCfgNetworkSecret_Type.__name__ = "DisplayString"
_WirelessSecurityCfgNetworkSecret_Object = MibTableColumn
wirelessSecurityCfgNetworkSecret = _WirelessSecurityCfgNetworkSecret_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 11),
    _WirelessSecurityCfgNetworkSecret_Type()
)
wirelessSecurityCfgNetworkSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgNetworkSecret.setStatus("current")
_WirelessSecurityCfgKey2_Type = WEPKeyType
_WirelessSecurityCfgKey2_Object = MibTableColumn
wirelessSecurityCfgKey2 = _WirelessSecurityCfgKey2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 12),
    _WirelessSecurityCfgKey2_Type()
)
wirelessSecurityCfgKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgKey2.setStatus("current")
_WirelessSecurityCfgKey3_Type = WEPKeyType
_WirelessSecurityCfgKey3_Object = MibTableColumn
wirelessSecurityCfgKey3 = _WirelessSecurityCfgKey3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 13),
    _WirelessSecurityCfgKey3_Type()
)
wirelessSecurityCfgKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgKey3.setStatus("current")
_WirelessSecurityCfgKey4_Type = WEPKeyType
_WirelessSecurityCfgKey4_Object = MibTableColumn
wirelessSecurityCfgKey4 = _WirelessSecurityCfgKey4_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 1, 1, 1, 14),
    _WirelessSecurityCfgKey4_Type()
)
wirelessSecurityCfgKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityCfgKey4.setStatus("current")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2)
)
_RadiusSrvProfileTable_Object = MibTable
radiusSrvProfileTable = _RadiusSrvProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    radiusSrvProfileTable.setStatus("current")
_RadiusSrvProfileTableEntry_Object = MibTableRow
radiusSrvProfileTableEntry = _RadiusSrvProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1)
)
radiusSrvProfileTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "radiusSrvProfileTableIndex"),
    (0, "PROXIM-MIB", "radiusSrvProfileTableSecIndex"),
)
if mibBuilder.loadTexts:
    radiusSrvProfileTableEntry.setStatus("current")


class _RadiusSrvProfileTableIndex_Type(Unsigned32):
    """Custom type radiusSrvProfileTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadiusSrvProfileTableIndex_Type.__name__ = "Unsigned32"
_RadiusSrvProfileTableIndex_Object = MibTableColumn
radiusSrvProfileTableIndex = _RadiusSrvProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 1),
    _RadiusSrvProfileTableIndex_Type()
)
radiusSrvProfileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvProfileTableIndex.setStatus("current")


class _RadiusSrvProfileTableSecIndex_Type(Unsigned32):
    """Custom type radiusSrvProfileTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RadiusSrvProfileTableSecIndex_Type.__name__ = "Unsigned32"
_RadiusSrvProfileTableSecIndex_Object = MibTableColumn
radiusSrvProfileTableSecIndex = _RadiusSrvProfileTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 2),
    _RadiusSrvProfileTableSecIndex_Type()
)
radiusSrvProfileTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvProfileTableSecIndex.setStatus("current")


class _RadiusSrvProfileType_Type(Integer32):
    """Custom type radiusSrvProfileType based on Integer32"""
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
        *(("primaryAccountingServer", 3),
          ("primaryAuthticationServer", 1),
          ("secondaryAccountingServer", 4),
          ("secondaryAuthenticationServer", 2))
    )


_RadiusSrvProfileType_Type.__name__ = "Integer32"
_RadiusSrvProfileType_Object = MibTableColumn
radiusSrvProfileType = _RadiusSrvProfileType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 3),
    _RadiusSrvProfileType_Type()
)
radiusSrvProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvProfileType.setStatus("current")


class _RadiusSrvIPADDR_Type(IpAddress):
    """Custom type radiusSrvIPADDR based on IpAddress"""
    defaultHexValue = "a9fe8085"


_RadiusSrvIPADDR_Object = MibTableColumn
radiusSrvIPADDR = _RadiusSrvIPADDR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 4),
    _RadiusSrvIPADDR_Type()
)
radiusSrvIPADDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvIPADDR.setStatus("current")


class _RadiusSrvServerPort_Type(Unsigned32):
    """Custom type radiusSrvServerPort based on Unsigned32"""
    defaultValue = 1812


_RadiusSrvServerPort_Object = MibTableColumn
radiusSrvServerPort = _RadiusSrvServerPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 5),
    _RadiusSrvServerPort_Type()
)
radiusSrvServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvServerPort.setStatus("current")


class _RadiusSrvProfileServerSharedSecret_Type(DisplayString):
    """Custom type radiusSrvProfileServerSharedSecret based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RadiusSrvProfileServerSharedSecret_Type.__name__ = "DisplayString"
_RadiusSrvProfileServerSharedSecret_Object = MibTableColumn
radiusSrvProfileServerSharedSecret = _RadiusSrvProfileServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 6),
    _RadiusSrvProfileServerSharedSecret_Type()
)
radiusSrvProfileServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvProfileServerSharedSecret.setStatus("current")


class _RadiusSrvProfileTableEntryStatus_Type(RowStatus):
    """Custom type radiusSrvProfileTableEntryStatus based on RowStatus"""


_RadiusSrvProfileTableEntryStatus_Object = MibTableColumn
radiusSrvProfileTableEntryStatus = _RadiusSrvProfileTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 1, 1, 7),
    _RadiusSrvProfileTableEntryStatus_Type()
)
radiusSrvProfileTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvProfileTableEntryStatus.setStatus("current")
_RadiusSupProfileTable_Object = MibTable
radiusSupProfileTable = _RadiusSupProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    radiusSupProfileTable.setStatus("current")
_RadiusSupProfileTableEntry_Object = MibTableRow
radiusSupProfileTableEntry = _RadiusSupProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1)
)
radiusSupProfileTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "radiusSupProfileTableIndex"),
)
if mibBuilder.loadTexts:
    radiusSupProfileTableEntry.setStatus("current")


class _RadiusSupProfileTableIndex_Type(Unsigned32):
    """Custom type radiusSupProfileTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RadiusSupProfileTableIndex_Type.__name__ = "Unsigned32"
_RadiusSupProfileTableIndex_Object = MibTableColumn
radiusSupProfileTableIndex = _RadiusSupProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 1),
    _RadiusSupProfileTableIndex_Type()
)
radiusSupProfileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSupProfileTableIndex.setStatus("current")


class _RadiusSupProfileName_Type(DisplayString):
    """Custom type radiusSupProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RadiusSupProfileName_Type.__name__ = "DisplayString"
_RadiusSupProfileName_Object = MibTableColumn
radiusSupProfileName = _RadiusSupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 2),
    _RadiusSupProfileName_Type()
)
radiusSupProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSupProfileName.setStatus("current")


class _RadiusSupProfileMaxReTransmissions_Type(Unsigned32):
    """Custom type radiusSupProfileMaxReTransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RadiusSupProfileMaxReTransmissions_Type.__name__ = "Unsigned32"
_RadiusSupProfileMaxReTransmissions_Object = MibTableColumn
radiusSupProfileMaxReTransmissions = _RadiusSupProfileMaxReTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 3),
    _RadiusSupProfileMaxReTransmissions_Type()
)
radiusSupProfileMaxReTransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSupProfileMaxReTransmissions.setStatus("current")


class _RadiusSupProfileMsgResponseTime_Type(Unsigned32):
    """Custom type radiusSupProfileMsgResponseTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 12),
    )


_RadiusSupProfileMsgResponseTime_Type.__name__ = "Unsigned32"
_RadiusSupProfileMsgResponseTime_Object = MibTableColumn
radiusSupProfileMsgResponseTime = _RadiusSupProfileMsgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 4),
    _RadiusSupProfileMsgResponseTime_Type()
)
radiusSupProfileMsgResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSupProfileMsgResponseTime.setStatus("current")


class _RadiusSupProfileReAuthenticationPeriod_Type(Unsigned32):
    """Custom type radiusSupProfileReAuthenticationPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 65535),
    )


_RadiusSupProfileReAuthenticationPeriod_Type.__name__ = "Unsigned32"
_RadiusSupProfileReAuthenticationPeriod_Object = MibTableColumn
radiusSupProfileReAuthenticationPeriod = _RadiusSupProfileReAuthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 5),
    _RadiusSupProfileReAuthenticationPeriod_Type()
)
radiusSupProfileReAuthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSupProfileReAuthenticationPeriod.setStatus("current")


class _RadiusSupProfileTableEntryStatus_Type(RowStatus):
    """Custom type radiusSupProfileTableEntryStatus based on RowStatus"""


_RadiusSupProfileTableEntryStatus_Object = MibTableColumn
radiusSupProfileTableEntryStatus = _RadiusSupProfileTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 2, 2, 1, 6),
    _RadiusSupProfileTableEntryStatus_Type()
)
radiusSupProfileTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSupProfileTableEntryStatus.setStatus("current")
_Macacl_ObjectIdentity = ObjectIdentity
macacl = _Macacl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3)
)
_MacaclProfileTable_Object = MibTable
macaclProfileTable = _MacaclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    macaclProfileTable.setStatus("current")
_MacaclProfileTableEntry_Object = MibTableRow
macaclProfileTableEntry = _MacaclProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1, 1)
)
macaclProfileTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "macaclProfileTableIndex"),
)
if mibBuilder.loadTexts:
    macaclProfileTableEntry.setStatus("current")


class _MacaclProfileTableIndex_Type(Unsigned32):
    """Custom type macaclProfileTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MacaclProfileTableIndex_Type.__name__ = "Unsigned32"
_MacaclProfileTableIndex_Object = MibTableColumn
macaclProfileTableIndex = _MacaclProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1, 1, 1),
    _MacaclProfileTableIndex_Type()
)
macaclProfileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macaclProfileTableIndex.setStatus("current")


class _MacaclProfileName_Type(DisplayString):
    """Custom type macaclProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MacaclProfileName_Type.__name__ = "DisplayString"
_MacaclProfileName_Object = MibTableColumn
macaclProfileName = _MacaclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1, 1, 2),
    _MacaclProfileName_Type()
)
macaclProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaclProfileName.setStatus("current")


class _MacaclOperationType_Type(Integer32):
    """Custom type macaclOperationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_MacaclOperationType_Type.__name__ = "Integer32"
_MacaclOperationType_Object = MibTableColumn
macaclOperationType = _MacaclOperationType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1, 1, 3),
    _MacaclOperationType_Type()
)
macaclOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaclOperationType.setStatus("current")


class _MacaclTableEntryStatus_Type(RowStatus):
    """Custom type macaclTableEntryStatus based on RowStatus"""


_MacaclTableEntryStatus_Object = MibTableColumn
macaclTableEntryStatus = _MacaclTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 1, 1, 4),
    _MacaclTableEntryStatus_Type()
)
macaclTableEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaclTableEntryStatus.setStatus("current")
_MacaclAddrTable_Object = MibTable
macaclAddrTable = _MacaclAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    macaclAddrTable.setStatus("current")
_MacaclAddrTableEntry_Object = MibTableRow
macaclAddrTableEntry = _MacaclAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1)
)
macaclAddrTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "macaclAddrTableIndex"),
    (0, "PROXIM-MIB", "macaclAddrTableSecIndex"),
)
if mibBuilder.loadTexts:
    macaclAddrTableEntry.setStatus("current")


class _MacaclAddrTableIndex_Type(Unsigned32):
    """Custom type macaclAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MacaclAddrTableIndex_Type.__name__ = "Unsigned32"
_MacaclAddrTableIndex_Object = MibTableColumn
macaclAddrTableIndex = _MacaclAddrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1, 1),
    _MacaclAddrTableIndex_Type()
)
macaclAddrTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macaclAddrTableIndex.setStatus("current")


class _MacaclAddrTableSecIndex_Type(Unsigned32):
    """Custom type macaclAddrTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MacaclAddrTableSecIndex_Type.__name__ = "Unsigned32"
_MacaclAddrTableSecIndex_Object = MibTableColumn
macaclAddrTableSecIndex = _MacaclAddrTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1, 2),
    _MacaclAddrTableSecIndex_Type()
)
macaclAddrTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macaclAddrTableSecIndex.setStatus("current")
_MacaclAddrTableMACAddress_Type = MacAddress
_MacaclAddrTableMACAddress_Object = MibTableColumn
macaclAddrTableMACAddress = _MacaclAddrTableMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1, 3),
    _MacaclAddrTableMACAddress_Type()
)
macaclAddrTableMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaclAddrTableMACAddress.setStatus("current")


class _MacaclAddrComment_Type(DisplayString):
    """Custom type macaclAddrComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MacaclAddrComment_Type.__name__ = "DisplayString"
_MacaclAddrComment_Object = MibTableColumn
macaclAddrComment = _MacaclAddrComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1, 4),
    _MacaclAddrComment_Type()
)
macaclAddrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaclAddrComment.setStatus("current")


class _MacaclAddrTableEntryStatus_Type(RowStatus):
    """Custom type macaclAddrTableEntryStatus based on RowStatus"""


_MacaclAddrTableEntryStatus_Object = MibTableColumn
macaclAddrTableEntryStatus = _MacaclAddrTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 2, 3, 2, 1, 5),
    _MacaclAddrTableEntryStatus_Type()
)
macaclAddrTableEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaclAddrTableEntryStatus.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3)
)
_QosProfileTable_Object = MibTable
qosProfileTable = _QosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qosProfileTable.setStatus("current")
_QosProfileTableEntry_Object = MibTableRow
qosProfileTableEntry = _QosProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1)
)
qosProfileTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "qosProfileTableIndex"),
)
if mibBuilder.loadTexts:
    qosProfileTableEntry.setStatus("current")


class _QosProfileTableIndex_Type(Unsigned32):
    """Custom type qosProfileTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_QosProfileTableIndex_Type.__name__ = "Unsigned32"
_QosProfileTableIndex_Object = MibTableColumn
qosProfileTableIndex = _QosProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1, 1),
    _QosProfileTableIndex_Type()
)
qosProfileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosProfileTableIndex.setStatus("current")


class _QosProfileName_Type(DisplayString):
    """Custom type qosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QosProfileName_Type.__name__ = "DisplayString"
_QosProfileName_Object = MibTableColumn
qosProfileName = _QosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1, 2),
    _QosProfileName_Type()
)
qosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfileName.setStatus("current")


class _QosProfileTablePolicyName_Type(DisplayString):
    """Custom type qosProfileTablePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QosProfileTablePolicyName_Type.__name__ = "DisplayString"
_QosProfileTablePolicyName_Object = MibTableColumn
qosProfileTablePolicyName = _QosProfileTablePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1, 3),
    _QosProfileTablePolicyName_Type()
)
qosProfileTablePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfileTablePolicyName.setStatus("current")


class _QosProfileEDCAProfileName_Type(DisplayString):
    """Custom type qosProfileEDCAProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QosProfileEDCAProfileName_Type.__name__ = "DisplayString"
_QosProfileEDCAProfileName_Object = MibTableColumn
qosProfileEDCAProfileName = _QosProfileEDCAProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1, 4),
    _QosProfileEDCAProfileName_Type()
)
qosProfileEDCAProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfileEDCAProfileName.setStatus("current")


class _QosProfileTableQoSNACKStatus_Type(Integer32):
    """Custom type qosProfileTableQoSNACKStatus based on Integer32"""
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


_QosProfileTableQoSNACKStatus_Type.__name__ = "Integer32"
_QosProfileTableQoSNACKStatus_Object = MibTableColumn
qosProfileTableQoSNACKStatus = _QosProfileTableQoSNACKStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 1, 1, 5),
    _QosProfileTableQoSNACKStatus_Type()
)
qosProfileTableQoSNACKStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfileTableQoSNACKStatus.setStatus("current")
_QoSPolicyTable_Object = MibTable
qoSPolicyTable = _QoSPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qoSPolicyTable.setStatus("current")
_QoSPolicyTableEntry_Object = MibTableRow
qoSPolicyTableEntry = _QoSPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1)
)
qoSPolicyTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "qoSPolicyTableIndex"),
    (0, "PROXIM-MIB", "qoSPolicyTableSecIndex"),
)
if mibBuilder.loadTexts:
    qoSPolicyTableEntry.setStatus("current")


class _QoSPolicyTableIndex_Type(Unsigned32):
    """Custom type qoSPolicyTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_QoSPolicyTableIndex_Type.__name__ = "Unsigned32"
_QoSPolicyTableIndex_Object = MibTableColumn
qoSPolicyTableIndex = _QoSPolicyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 1),
    _QoSPolicyTableIndex_Type()
)
qoSPolicyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoSPolicyTableIndex.setStatus("current")


class _QoSPolicyTableSecIndex_Type(Unsigned32):
    """Custom type qoSPolicyTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QoSPolicyTableSecIndex_Type.__name__ = "Unsigned32"
_QoSPolicyTableSecIndex_Object = MibTableColumn
qoSPolicyTableSecIndex = _QoSPolicyTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 2),
    _QoSPolicyTableSecIndex_Type()
)
qoSPolicyTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoSPolicyTableSecIndex.setStatus("current")
_QoSPolicyTablePolicyName_Type = DisplayString
_QoSPolicyTablePolicyName_Object = MibTableColumn
qoSPolicyTablePolicyName = _QoSPolicyTablePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 3),
    _QoSPolicyTablePolicyName_Type()
)
qoSPolicyTablePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoSPolicyTablePolicyName.setStatus("current")


class _QoSPolicyType_Type(Integer32):
    """Custom type qoSPolicyType based on Integer32"""
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
        *(("inboundLayer2", 1),
          ("inboundLayer3", 2),
          ("outboundLayer2", 3),
          ("outboundLayer3", 4))
    )


_QoSPolicyType_Type.__name__ = "Integer32"
_QoSPolicyType_Object = MibTableColumn
qoSPolicyType = _QoSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 4),
    _QoSPolicyType_Type()
)
qoSPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoSPolicyType.setStatus("current")


class _QoSPolicyPriorityMapping_Type(Unsigned32):
    """Custom type qoSPolicyPriorityMapping based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QoSPolicyPriorityMapping_Type.__name__ = "Unsigned32"
_QoSPolicyPriorityMapping_Object = MibTableColumn
qoSPolicyPriorityMapping = _QoSPolicyPriorityMapping_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 5),
    _QoSPolicyPriorityMapping_Type()
)
qoSPolicyPriorityMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoSPolicyPriorityMapping.setStatus("current")


class _QoSPolicyMarkingStatus_Type(Integer32):
    """Custom type qoSPolicyMarkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 3))
    )


_QoSPolicyMarkingStatus_Type.__name__ = "Integer32"
_QoSPolicyMarkingStatus_Object = MibTableColumn
qoSPolicyMarkingStatus = _QoSPolicyMarkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 6),
    _QoSPolicyMarkingStatus_Type()
)
qoSPolicyMarkingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoSPolicyMarkingStatus.setStatus("current")
_QoSPolicyTableEntryStatus_Type = RowStatus
_QoSPolicyTableEntryStatus_Object = MibTableColumn
qoSPolicyTableEntryStatus = _QoSPolicyTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 2, 1, 7),
    _QoSPolicyTableEntryStatus_Type()
)
qoSPolicyTableEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qoSPolicyTableEntryStatus.setStatus("current")
_WirelessQoS_ObjectIdentity = ObjectIdentity
wirelessQoS = _WirelessQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3)
)
_WirelessQoSEDCATable_Object = MibTable
wirelessQoSEDCATable = _WirelessQoSEDCATable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    wirelessQoSEDCATable.setStatus("current")
_WirelessQoSEDCATableEntry_Object = MibTableRow
wirelessQoSEDCATableEntry = _WirelessQoSEDCATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1)
)
wirelessQoSEDCATableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessQoSEDCATableIndex"),
    (0, "PROXIM-MIB", "wirelessQoSEDCATableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessQoSEDCATableEntry.setStatus("current")


class _WirelessQoSEDCATableIndex_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WirelessQoSEDCATableIndex_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableIndex_Object = MibTableColumn
wirelessQoSEDCATableIndex = _WirelessQoSEDCATableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 1),
    _WirelessQoSEDCATableIndex_Type()
)
wirelessQoSEDCATableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableIndex.setStatus("current")


class _WirelessQoSEDCATableSecIndex_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WirelessQoSEDCATableSecIndex_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableSecIndex_Object = MibTableColumn
wirelessQoSEDCATableSecIndex = _WirelessQoSEDCATableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 2),
    _WirelessQoSEDCATableSecIndex_Type()
)
wirelessQoSEDCATableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableSecIndex.setStatus("current")


class _WirelessQoSEDCATableProfileName_Type(DisplayString):
    """Custom type wirelessQoSEDCATableProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessQoSEDCATableProfileName_Type.__name__ = "DisplayString"
_WirelessQoSEDCATableProfileName_Object = MibTableColumn
wirelessQoSEDCATableProfileName = _WirelessQoSEDCATableProfileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 3),
    _WirelessQoSEDCATableProfileName_Type()
)
wirelessQoSEDCATableProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableProfileName.setStatus("current")


class _WirelessQoSEDCATableCWmin_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableCWmin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WirelessQoSEDCATableCWmin_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableCWmin_Object = MibTableColumn
wirelessQoSEDCATableCWmin = _WirelessQoSEDCATableCWmin_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 4),
    _WirelessQoSEDCATableCWmin_Type()
)
wirelessQoSEDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableCWmin.setStatus("current")


class _WirelessQoSEDCATableCWmax_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableCWmax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WirelessQoSEDCATableCWmax_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableCWmax_Object = MibTableColumn
wirelessQoSEDCATableCWmax = _WirelessQoSEDCATableCWmax_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 5),
    _WirelessQoSEDCATableCWmax_Type()
)
wirelessQoSEDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableCWmax.setStatus("current")


class _WirelessQoSEDCATableAIFSN_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableAIFSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_WirelessQoSEDCATableAIFSN_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableAIFSN_Object = MibTableColumn
wirelessQoSEDCATableAIFSN = _WirelessQoSEDCATableAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 6),
    _WirelessQoSEDCATableAIFSN_Type()
)
wirelessQoSEDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAIFSN.setStatus("current")


class _WirelessQoSEDCATableTXOP_Type(DisplayString):
    """Custom type wirelessQoSEDCATableTXOP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessQoSEDCATableTXOP_Type.__name__ = "DisplayString"
_WirelessQoSEDCATableTXOP_Object = MibTableColumn
wirelessQoSEDCATableTXOP = _WirelessQoSEDCATableTXOP_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 7),
    _WirelessQoSEDCATableTXOP_Type()
)
wirelessQoSEDCATableTXOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableTXOP.setStatus("current")


class _WirelessQoSEDCATableACM_Type(Integer32):
    """Custom type wirelessQoSEDCATableACM based on Integer32"""
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


_WirelessQoSEDCATableACM_Type.__name__ = "Integer32"
_WirelessQoSEDCATableACM_Object = MibTableColumn
wirelessQoSEDCATableACM = _WirelessQoSEDCATableACM_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 8),
    _WirelessQoSEDCATableACM_Type()
)
wirelessQoSEDCATableACM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableACM.setStatus("current")


class _WirelessQoSEDCATableAPCWmin_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableAPCWmin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WirelessQoSEDCATableAPCWmin_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableAPCWmin_Object = MibTableColumn
wirelessQoSEDCATableAPCWmin = _WirelessQoSEDCATableAPCWmin_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 9),
    _WirelessQoSEDCATableAPCWmin_Type()
)
wirelessQoSEDCATableAPCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAPCWmin.setStatus("current")


class _WirelessQoSEDCATableAPCWmax_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableAPCWmax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WirelessQoSEDCATableAPCWmax_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableAPCWmax_Object = MibTableColumn
wirelessQoSEDCATableAPCWmax = _WirelessQoSEDCATableAPCWmax_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 10),
    _WirelessQoSEDCATableAPCWmax_Type()
)
wirelessQoSEDCATableAPCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAPCWmax.setStatus("current")


class _WirelessQoSEDCATableAPAIFSN_Type(Unsigned32):
    """Custom type wirelessQoSEDCATableAPAIFSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WirelessQoSEDCATableAPAIFSN_Type.__name__ = "Unsigned32"
_WirelessQoSEDCATableAPAIFSN_Object = MibTableColumn
wirelessQoSEDCATableAPAIFSN = _WirelessQoSEDCATableAPAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 11),
    _WirelessQoSEDCATableAPAIFSN_Type()
)
wirelessQoSEDCATableAPAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAPAIFSN.setStatus("current")


class _WirelessQoSEDCATableAPTXOP_Type(DisplayString):
    """Custom type wirelessQoSEDCATableAPTXOP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessQoSEDCATableAPTXOP_Type.__name__ = "DisplayString"
_WirelessQoSEDCATableAPTXOP_Object = MibTableColumn
wirelessQoSEDCATableAPTXOP = _WirelessQoSEDCATableAPTXOP_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 12),
    _WirelessQoSEDCATableAPTXOP_Type()
)
wirelessQoSEDCATableAPTXOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAPTXOP.setStatus("current")


class _WirelessQoSEDCATableAPACM_Type(Integer32):
    """Custom type wirelessQoSEDCATableAPACM based on Integer32"""
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


_WirelessQoSEDCATableAPACM_Type.__name__ = "Integer32"
_WirelessQoSEDCATableAPACM_Object = MibTableColumn
wirelessQoSEDCATableAPACM = _WirelessQoSEDCATableAPACM_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 3, 1, 1, 13),
    _WirelessQoSEDCATableAPACM_Type()
)
wirelessQoSEDCATableAPACM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessQoSEDCATableAPACM.setStatus("current")
_L2l3QoS_ObjectIdentity = ObjectIdentity
l2l3QoS = _L2l3QoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4)
)
_L2l3QoSDot1DToDot1pMappingTable_Object = MibTable
l2l3QoSDot1DToDot1pMappingTable = _L2l3QoSDot1DToDot1pMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    l2l3QoSDot1DToDot1pMappingTable.setStatus("current")
_L2l3QoSDot1DToDot1pMappingTableEntry_Object = MibTableRow
l2l3QoSDot1DToDot1pMappingTableEntry = _L2l3QoSDot1DToDot1pMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 1, 1)
)
l2l3QoSDot1DToDot1pMappingTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "l2l3QoSDot1DToDot1pMappingTableIndex"),
    (0, "PROXIM-MIB", "l2l3QoSDot1dPriority"),
)
if mibBuilder.loadTexts:
    l2l3QoSDot1DToDot1pMappingTableEntry.setStatus("current")


class _L2l3QoSDot1DToDot1pMappingTableIndex_Type(Unsigned32):
    """Custom type l2l3QoSDot1DToDot1pMappingTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_L2l3QoSDot1DToDot1pMappingTableIndex_Type.__name__ = "Unsigned32"
_L2l3QoSDot1DToDot1pMappingTableIndex_Object = MibTableColumn
l2l3QoSDot1DToDot1pMappingTableIndex = _L2l3QoSDot1DToDot1pMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 1, 1, 1),
    _L2l3QoSDot1DToDot1pMappingTableIndex_Type()
)
l2l3QoSDot1DToDot1pMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2l3QoSDot1DToDot1pMappingTableIndex.setStatus("current")


class _L2l3QoSDot1dPriority_Type(Unsigned32):
    """Custom type l2l3QoSDot1dPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_L2l3QoSDot1dPriority_Type.__name__ = "Unsigned32"
_L2l3QoSDot1dPriority_Object = MibTableColumn
l2l3QoSDot1dPriority = _L2l3QoSDot1dPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 1, 1, 2),
    _L2l3QoSDot1dPriority_Type()
)
l2l3QoSDot1dPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2l3QoSDot1dPriority.setStatus("current")


class _L2l3QoSDot1pPriority_Type(Unsigned32):
    """Custom type l2l3QoSDot1pPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L2l3QoSDot1pPriority_Type.__name__ = "Unsigned32"
_L2l3QoSDot1pPriority_Object = MibTableColumn
l2l3QoSDot1pPriority = _L2l3QoSDot1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 1, 1, 3),
    _L2l3QoSDot1pPriority_Type()
)
l2l3QoSDot1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2l3QoSDot1pPriority.setStatus("current")
_L2l3QoSDot1DToIPDSCPMappingTable_Object = MibTable
l2l3QoSDot1DToIPDSCPMappingTable = _L2l3QoSDot1DToIPDSCPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    l2l3QoSDot1DToIPDSCPMappingTable.setStatus("current")
_L2l3QoSDot1DToIPDSCPMappingTableEntry_Object = MibTableRow
l2l3QoSDot1DToIPDSCPMappingTableEntry = _L2l3QoSDot1DToIPDSCPMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2, 1)
)
l2l3QoSDot1DToIPDSCPMappingTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "l2l3QoSDot1DToIPDSCPMappingTableIndex"),
    (0, "PROXIM-MIB", "l2l3QoSDot1dPriorityIPDSCP"),
)
if mibBuilder.loadTexts:
    l2l3QoSDot1DToIPDSCPMappingTableEntry.setStatus("current")


class _L2l3QoSDot1DToIPDSCPMappingTableIndex_Type(Unsigned32):
    """Custom type l2l3QoSDot1DToIPDSCPMappingTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_L2l3QoSDot1DToIPDSCPMappingTableIndex_Type.__name__ = "Unsigned32"
_L2l3QoSDot1DToIPDSCPMappingTableIndex_Object = MibTableColumn
l2l3QoSDot1DToIPDSCPMappingTableIndex = _L2l3QoSDot1DToIPDSCPMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2, 1, 1),
    _L2l3QoSDot1DToIPDSCPMappingTableIndex_Type()
)
l2l3QoSDot1DToIPDSCPMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2l3QoSDot1DToIPDSCPMappingTableIndex.setStatus("current")


class _L2l3QoSDot1dPriorityIPDSCP_Type(Unsigned32):
    """Custom type l2l3QoSDot1dPriorityIPDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L2l3QoSDot1dPriorityIPDSCP_Type.__name__ = "Unsigned32"
_L2l3QoSDot1dPriorityIPDSCP_Object = MibTableColumn
l2l3QoSDot1dPriorityIPDSCP = _L2l3QoSDot1dPriorityIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2, 1, 2),
    _L2l3QoSDot1dPriorityIPDSCP_Type()
)
l2l3QoSDot1dPriorityIPDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2l3QoSDot1dPriorityIPDSCP.setStatus("current")


class _L2l3QoSDSCPPriorityLowerLimit_Type(Unsigned32):
    """Custom type l2l3QoSDSCPPriorityLowerLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_L2l3QoSDSCPPriorityLowerLimit_Type.__name__ = "Unsigned32"
_L2l3QoSDSCPPriorityLowerLimit_Object = MibTableColumn
l2l3QoSDSCPPriorityLowerLimit = _L2l3QoSDSCPPriorityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2, 1, 3),
    _L2l3QoSDSCPPriorityLowerLimit_Type()
)
l2l3QoSDSCPPriorityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2l3QoSDSCPPriorityLowerLimit.setStatus("current")


class _L2l3QoSDSCPPriorityUpperLimit_Type(Unsigned32):
    """Custom type l2l3QoSDSCPPriorityUpperLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_L2l3QoSDSCPPriorityUpperLimit_Type.__name__ = "Unsigned32"
_L2l3QoSDSCPPriorityUpperLimit_Object = MibTableColumn
l2l3QoSDSCPPriorityUpperLimit = _L2l3QoSDSCPPriorityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 4, 2, 1, 4),
    _L2l3QoSDSCPPriorityUpperLimit_Type()
)
l2l3QoSDSCPPriorityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2l3QoSDSCPPriorityUpperLimit.setStatus("current")
_WorpQoS_ObjectIdentity = ObjectIdentity
worpQoS = _WorpQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5)
)
_WorpQoSPIRMacTable_Object = MibTable
worpQoSPIRMacTable = _WorpQoSPIRMacTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    worpQoSPIRMacTable.setStatus("current")
_WorpQoSPIRMacTableEntry_Object = MibTableRow
worpQoSPIRMacTableEntry = _WorpQoSPIRMacTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1)
)
worpQoSPIRMacTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSPIRMacTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSPIRMacTableEntry.setStatus("current")


class _WorpQoSPIRMacTableIndex_Type(Unsigned32):
    """Custom type worpQoSPIRMacTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WorpQoSPIRMacTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSPIRMacTableIndex_Object = MibTableColumn
worpQoSPIRMacTableIndex = _WorpQoSPIRMacTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1, 1),
    _WorpQoSPIRMacTableIndex_Type()
)
worpQoSPIRMacTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRMacTableIndex.setStatus("current")
_WorpQoSPIRMacAddr_Type = MacAddress
_WorpQoSPIRMacAddr_Object = MibTableColumn
worpQoSPIRMacAddr = _WorpQoSPIRMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1, 2),
    _WorpQoSPIRMacAddr_Type()
)
worpQoSPIRMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMacAddr.setStatus("current")
_WorpQoSPIRMacMask_Type = MacAddress
_WorpQoSPIRMacMask_Object = MibTableColumn
worpQoSPIRMacMask = _WorpQoSPIRMacMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1, 3),
    _WorpQoSPIRMacMask_Type()
)
worpQoSPIRMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMacMask.setStatus("current")


class _WorpQoSPIRMacComment_Type(DisplayString):
    """Custom type worpQoSPIRMacComment based on DisplayString"""
    defaultValue = OctetString("default-mac")


_WorpQoSPIRMacComment_Object = MibTableColumn
worpQoSPIRMacComment = _WorpQoSPIRMacComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1, 4),
    _WorpQoSPIRMacComment_Type()
)
worpQoSPIRMacComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMacComment.setStatus("current")


class _WorpQoSPIRMacTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSPIRMacTableEntryStatus based on RowStatus"""


_WorpQoSPIRMacTableEntryStatus_Object = MibTableColumn
worpQoSPIRMacTableEntryStatus = _WorpQoSPIRMacTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 1, 1, 5),
    _WorpQoSPIRMacTableEntryStatus_Type()
)
worpQoSPIRMacTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMacTableEntryStatus.setStatus("current")
_WorpQoSPIRIPTable_Object = MibTable
worpQoSPIRIPTable = _WorpQoSPIRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    worpQoSPIRIPTable.setStatus("current")
_WorpQoSPIRIPTableEntry_Object = MibTableRow
worpQoSPIRIPTableEntry = _WorpQoSPIRIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1)
)
worpQoSPIRIPTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSPIRIPTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSPIRIPTableEntry.setStatus("current")


class _WorpQoSPIRIPTableIndex_Type(Unsigned32):
    """Custom type worpQoSPIRIPTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WorpQoSPIRIPTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSPIRIPTableIndex_Object = MibTableColumn
worpQoSPIRIPTableIndex = _WorpQoSPIRIPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1, 1),
    _WorpQoSPIRIPTableIndex_Type()
)
worpQoSPIRIPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRIPTableIndex.setStatus("current")
_WorpQoSPIRIPAddr_Type = IpAddress
_WorpQoSPIRIPAddr_Object = MibTableColumn
worpQoSPIRIPAddr = _WorpQoSPIRIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1, 2),
    _WorpQoSPIRIPAddr_Type()
)
worpQoSPIRIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPAddr.setStatus("current")


class _WorpQoSPIRIPSubMask_Type(IpAddress):
    """Custom type worpQoSPIRIPSubMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_WorpQoSPIRIPSubMask_Object = MibTableColumn
worpQoSPIRIPSubMask = _WorpQoSPIRIPSubMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1, 3),
    _WorpQoSPIRIPSubMask_Type()
)
worpQoSPIRIPSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPSubMask.setStatus("current")


class _WorpQoSPIRIPComment_Type(DisplayString):
    """Custom type worpQoSPIRIPComment based on DisplayString"""
    defaultValue = OctetString("default-ip")


_WorpQoSPIRIPComment_Object = MibTableColumn
worpQoSPIRIPComment = _WorpQoSPIRIPComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1, 4),
    _WorpQoSPIRIPComment_Type()
)
worpQoSPIRIPComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPComment.setStatus("current")


class _WorpQoSPIRIPTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSPIRIPTableEntryStatus based on RowStatus"""


_WorpQoSPIRIPTableEntryStatus_Object = MibTableColumn
worpQoSPIRIPTableEntryStatus = _WorpQoSPIRIPTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 2, 1, 5),
    _WorpQoSPIRIPTableEntryStatus_Type()
)
worpQoSPIRIPTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPTableEntryStatus.setStatus("current")
_WorpQoSPIRPortTable_Object = MibTable
worpQoSPIRPortTable = _WorpQoSPIRPortTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    worpQoSPIRPortTable.setStatus("current")
_WorpQoSPIRPortTableEntry_Object = MibTableRow
worpQoSPIRPortTableEntry = _WorpQoSPIRPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1)
)
worpQoSPIRPortTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSPIRPortTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSPIRPortTableEntry.setStatus("current")


class _WorpQoSPIRPortTableIndex_Type(Unsigned32):
    """Custom type worpQoSPIRPortTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WorpQoSPIRPortTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSPIRPortTableIndex_Object = MibTableColumn
worpQoSPIRPortTableIndex = _WorpQoSPIRPortTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1, 1),
    _WorpQoSPIRPortTableIndex_Type()
)
worpQoSPIRPortTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRPortTableIndex.setStatus("current")


class _WorpQoSPIRStartPort_Type(Unsigned32):
    """Custom type worpQoSPIRStartPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WorpQoSPIRStartPort_Type.__name__ = "Unsigned32"
_WorpQoSPIRStartPort_Object = MibTableColumn
worpQoSPIRStartPort = _WorpQoSPIRStartPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1, 2),
    _WorpQoSPIRStartPort_Type()
)
worpQoSPIRStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRStartPort.setStatus("current")


class _WorpQoSPIREndPort_Type(Unsigned32):
    """Custom type worpQoSPIREndPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WorpQoSPIREndPort_Type.__name__ = "Unsigned32"
_WorpQoSPIREndPort_Object = MibTableColumn
worpQoSPIREndPort = _WorpQoSPIREndPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1, 3),
    _WorpQoSPIREndPort_Type()
)
worpQoSPIREndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIREndPort.setStatus("current")


class _WorpQoSPIRPortComment_Type(DisplayString):
    """Custom type worpQoSPIRPortComment based on DisplayString"""
    defaultValue = OctetString("default-port")


_WorpQoSPIRPortComment_Object = MibTableColumn
worpQoSPIRPortComment = _WorpQoSPIRPortComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1, 4),
    _WorpQoSPIRPortComment_Type()
)
worpQoSPIRPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRPortComment.setStatus("current")


class _WorpQoSPIRPortTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSPIRPortTableEntryStatus based on RowStatus"""


_WorpQoSPIRPortTableEntryStatus_Object = MibTableColumn
worpQoSPIRPortTableEntryStatus = _WorpQoSPIRPortTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 3, 1, 5),
    _WorpQoSPIRPortTableEntryStatus_Type()
)
worpQoSPIRPortTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRPortTableEntryStatus.setStatus("current")
_WorpQoSPIRMapTable_Object = MibTable
worpQoSPIRMapTable = _WorpQoSPIRMapTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    worpQoSPIRMapTable.setStatus("current")
_WorpQoSPIRMapTableEntry_Object = MibTableRow
worpQoSPIRMapTableEntry = _WorpQoSPIRMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1)
)
worpQoSPIRMapTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSPIRMapTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSPIRMapTableEntry.setStatus("current")


class _WorpQoSPIRMapTableIndex_Type(Unsigned32):
    """Custom type worpQoSPIRMapTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WorpQoSPIRMapTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSPIRMapTableIndex_Object = MibTableColumn
worpQoSPIRMapTableIndex = _WorpQoSPIRMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 1),
    _WorpQoSPIRMapTableIndex_Type()
)
worpQoSPIRMapTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRMapTableIndex.setStatus("current")
_WorpQoSPIRMapRuleName_Type = DisplayString
_WorpQoSPIRMapRuleName_Object = MibTableColumn
worpQoSPIRMapRuleName = _WorpQoSPIRMapRuleName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 2),
    _WorpQoSPIRMapRuleName_Type()
)
worpQoSPIRMapRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRMapRuleName.setStatus("current")


class _WorpQoSPIRMapSrcMacIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapSrcMacIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapSrcMacIndexList_Object = MibTableColumn
worpQoSPIRMapSrcMacIndexList = _WorpQoSPIRMapSrcMacIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 3),
    _WorpQoSPIRMapSrcMacIndexList_Type()
)
worpQoSPIRMapSrcMacIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapSrcMacIndexList.setStatus("current")


class _WorpQoSPIRMapDstMacIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapDstMacIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapDstMacIndexList_Object = MibTableColumn
worpQoSPIRMapDstMacIndexList = _WorpQoSPIRMapDstMacIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 4),
    _WorpQoSPIRMapDstMacIndexList_Type()
)
worpQoSPIRMapDstMacIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapDstMacIndexList.setStatus("current")


class _WorpQoSPIRMapSrcIpAddrIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapSrcIpAddrIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapSrcIpAddrIndexList_Object = MibTableColumn
worpQoSPIRMapSrcIpAddrIndexList = _WorpQoSPIRMapSrcIpAddrIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 5),
    _WorpQoSPIRMapSrcIpAddrIndexList_Type()
)
worpQoSPIRMapSrcIpAddrIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapSrcIpAddrIndexList.setStatus("current")


class _WorpQoSPIRMapDstIpAddrIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapDstIpAddrIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapDstIpAddrIndexList_Object = MibTableColumn
worpQoSPIRMapDstIpAddrIndexList = _WorpQoSPIRMapDstIpAddrIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 6),
    _WorpQoSPIRMapDstIpAddrIndexList_Type()
)
worpQoSPIRMapDstIpAddrIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapDstIpAddrIndexList.setStatus("current")


class _WorpQoSPIRMapSrcPortIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapSrcPortIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapSrcPortIndexList_Object = MibTableColumn
worpQoSPIRMapSrcPortIndexList = _WorpQoSPIRMapSrcPortIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 7),
    _WorpQoSPIRMapSrcPortIndexList_Type()
)
worpQoSPIRMapSrcPortIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapSrcPortIndexList.setStatus("current")


class _WorpQoSPIRMapDstPortIndexList_Type(DisplayString):
    """Custom type worpQoSPIRMapDstPortIndexList based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRMapDstPortIndexList_Object = MibTableColumn
worpQoSPIRMapDstPortIndexList = _WorpQoSPIRMapDstPortIndexList_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 4, 1, 8),
    _WorpQoSPIRMapDstPortIndexList_Type()
)
worpQoSPIRMapDstPortIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRMapDstPortIndexList.setStatus("current")
_WorpQoSPIRTable_Object = MibTable
worpQoSPIRTable = _WorpQoSPIRTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5)
)
if mibBuilder.loadTexts:
    worpQoSPIRTable.setStatus("current")
_WorpQoSPIRTableEntry_Object = MibTableRow
worpQoSPIRTableEntry = _WorpQoSPIRTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1)
)
worpQoSPIRTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSPIRTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSPIRTableEntry.setStatus("current")


class _WorpQoSPIRTableIndex_Type(Unsigned32):
    """Custom type worpQoSPIRTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WorpQoSPIRTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSPIRTableIndex_Object = MibTableColumn
worpQoSPIRTableIndex = _WorpQoSPIRTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 1),
    _WorpQoSPIRTableIndex_Type()
)
worpQoSPIRTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRTableIndex.setStatus("current")


class _WorpQoSPIRRuleName_Type(DisplayString):
    """Custom type worpQoSPIRRuleName based on DisplayString"""
    defaultValue = OctetString("default-pir")


_WorpQoSPIRRuleName_Object = MibTableColumn
worpQoSPIRRuleName = _WorpQoSPIRRuleName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 2),
    _WorpQoSPIRRuleName_Type()
)
worpQoSPIRRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRRuleName.setStatus("current")


class _WorpQoSPIRRuleBitMask_Type(Unsigned32):
    """Custom type worpQoSPIRRuleBitMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WorpQoSPIRRuleBitMask_Type.__name__ = "Unsigned32"
_WorpQoSPIRRuleBitMask_Object = MibTableColumn
worpQoSPIRRuleBitMask = _WorpQoSPIRRuleBitMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 3),
    _WorpQoSPIRRuleBitMask_Type()
)
worpQoSPIRRuleBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRRuleBitMask.setStatus("current")


class _WorpQoSPIRIPToSLow_Type(Unsigned32):
    """Custom type worpQoSPIRIPToSLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WorpQoSPIRIPToSLow_Type.__name__ = "Unsigned32"
_WorpQoSPIRIPToSLow_Object = MibTableColumn
worpQoSPIRIPToSLow = _WorpQoSPIRIPToSLow_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 4),
    _WorpQoSPIRIPToSLow_Type()
)
worpQoSPIRIPToSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPToSLow.setStatus("current")


class _WorpQoSPIRIPToSHigh_Type(Unsigned32):
    """Custom type worpQoSPIRIPToSHigh based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WorpQoSPIRIPToSHigh_Type.__name__ = "Unsigned32"
_WorpQoSPIRIPToSHigh_Object = MibTableColumn
worpQoSPIRIPToSHigh = _WorpQoSPIRIPToSHigh_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 5),
    _WorpQoSPIRIPToSHigh_Type()
)
worpQoSPIRIPToSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPToSHigh.setStatus("current")


class _WorpQoSPIRIPToSMask_Type(Unsigned32):
    """Custom type worpQoSPIRIPToSMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WorpQoSPIRIPToSMask_Type.__name__ = "Unsigned32"
_WorpQoSPIRIPToSMask_Object = MibTableColumn
worpQoSPIRIPToSMask = _WorpQoSPIRIPToSMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 6),
    _WorpQoSPIRIPToSMask_Type()
)
worpQoSPIRIPToSMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPToSMask.setStatus("current")


class _WorpQoSPIRIPProtocolIds_Type(DisplayString):
    """Custom type worpQoSPIRIPProtocolIds based on DisplayString"""
    defaultValue = OctetString("0")


_WorpQoSPIRIPProtocolIds_Object = MibTableColumn
worpQoSPIRIPProtocolIds = _WorpQoSPIRIPProtocolIds_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 7),
    _WorpQoSPIRIPProtocolIds_Type()
)
worpQoSPIRIPProtocolIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRIPProtocolIds.setStatus("current")


class _WorpQoSPIREtherPriorityLow_Type(Unsigned32):
    """Custom type worpQoSPIREtherPriorityLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WorpQoSPIREtherPriorityLow_Type.__name__ = "Unsigned32"
_WorpQoSPIREtherPriorityLow_Object = MibTableColumn
worpQoSPIREtherPriorityLow = _WorpQoSPIREtherPriorityLow_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 8),
    _WorpQoSPIREtherPriorityLow_Type()
)
worpQoSPIREtherPriorityLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIREtherPriorityLow.setStatus("current")


class _WorpQoSPIREtherPriorityHigh_Type(Unsigned32):
    """Custom type worpQoSPIREtherPriorityHigh based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WorpQoSPIREtherPriorityHigh_Type.__name__ = "Unsigned32"
_WorpQoSPIREtherPriorityHigh_Object = MibTableColumn
worpQoSPIREtherPriorityHigh = _WorpQoSPIREtherPriorityHigh_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 9),
    _WorpQoSPIREtherPriorityHigh_Type()
)
worpQoSPIREtherPriorityHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIREtherPriorityHigh.setStatus("current")


class _WorpQoSPIRVlanId_Type(VlanId):
    """Custom type worpQoSPIRVlanId based on VlanId"""
    defaultValue = 1


_WorpQoSPIRVlanId_Object = MibTableColumn
worpQoSPIRVlanId = _WorpQoSPIRVlanId_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 10),
    _WorpQoSPIRVlanId_Type()
)
worpQoSPIRVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRVlanId.setStatus("current")


class _WorpQoSPIREtherType_Type(Integer32):
    """Custom type worpQoSPIREtherType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dix-snap", 1),
          ("dsap", 2))
    )


_WorpQoSPIREtherType_Type.__name__ = "Integer32"
_WorpQoSPIREtherType_Object = MibTableColumn
worpQoSPIREtherType = _WorpQoSPIREtherType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 11),
    _WorpQoSPIREtherType_Type()
)
worpQoSPIREtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIREtherType.setStatus("current")


class _WorpQoSPIREtherValue_Type(OctetString):
    """Custom type worpQoSPIREtherValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WorpQoSPIREtherValue_Type.__name__ = "OctetString"
_WorpQoSPIREtherValue_Object = MibTableColumn
worpQoSPIREtherValue = _WorpQoSPIREtherValue_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 12),
    _WorpQoSPIREtherValue_Type()
)
worpQoSPIREtherValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIREtherValue.setStatus("current")


class _WorpQoSPIRPPPoEEncapsulation_Type(Integer32):
    """Custom type worpQoSPIRPPPoEEncapsulation based on Integer32"""
    defaultValue = 2

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


_WorpQoSPIRPPPoEEncapsulation_Type.__name__ = "Integer32"
_WorpQoSPIRPPPoEEncapsulation_Object = MibTableColumn
worpQoSPIRPPPoEEncapsulation = _WorpQoSPIRPPPoEEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 13),
    _WorpQoSPIRPPPoEEncapsulation_Type()
)
worpQoSPIRPPPoEEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRPPPoEEncapsulation.setStatus("current")


class _WorpQoSPIRPPPoEProtocolId_Type(OctetString):
    """Custom type worpQoSPIRPPPoEProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WorpQoSPIRPPPoEProtocolId_Type.__name__ = "OctetString"
_WorpQoSPIRPPPoEProtocolId_Object = MibTableColumn
worpQoSPIRPPPoEProtocolId = _WorpQoSPIRPPPoEProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 14),
    _WorpQoSPIRPPPoEProtocolId_Type()
)
worpQoSPIRPPPoEProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRPPPoEProtocolId.setStatus("current")


class _WorpQoSPIRMapTableIndexVal_Type(Unsigned32):
    """Custom type worpQoSPIRMapTableIndexVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WorpQoSPIRMapTableIndexVal_Type.__name__ = "Unsigned32"
_WorpQoSPIRMapTableIndexVal_Object = MibTableColumn
worpQoSPIRMapTableIndexVal = _WorpQoSPIRMapTableIndexVal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 15),
    _WorpQoSPIRMapTableIndexVal_Type()
)
worpQoSPIRMapTableIndexVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSPIRMapTableIndexVal.setStatus("current")


class _WorpQoSPIRTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSPIRTableEntryStatus based on RowStatus"""


_WorpQoSPIRTableEntryStatus_Object = MibTableColumn
worpQoSPIRTableEntryStatus = _WorpQoSPIRTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 5, 1, 16),
    _WorpQoSPIRTableEntryStatus_Type()
)
worpQoSPIRTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSPIRTableEntryStatus.setStatus("current")
_WorpQoSSFClassTable_Object = MibTable
worpQoSSFClassTable = _WorpQoSSFClassTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6)
)
if mibBuilder.loadTexts:
    worpQoSSFClassTable.setStatus("current")
_WorpQoSSFClassTableEntry_Object = MibTableRow
worpQoSSFClassTableEntry = _WorpQoSSFClassTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1)
)
worpQoSSFClassTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSSFClassTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSSFClassTableEntry.setStatus("current")


class _WorpQoSSFClassTableIndex_Type(Unsigned32):
    """Custom type worpQoSSFClassTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WorpQoSSFClassTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSSFClassTableIndex_Object = MibTableColumn
worpQoSSFClassTableIndex = _WorpQoSSFClassTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 1),
    _WorpQoSSFClassTableIndex_Type()
)
worpQoSSFClassTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSSFClassTableIndex.setStatus("current")


class _WorpQoSSFClassName_Type(DisplayString):
    """Custom type worpQoSSFClassName based on DisplayString"""
    defaultValue = OctetString("default-sfc")


_WorpQoSSFClassName_Object = MibTableColumn
worpQoSSFClassName = _WorpQoSSFClassName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 2),
    _WorpQoSSFClassName_Type()
)
worpQoSSFClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassName.setStatus("current")


class _WorpQoSSFClassSchedularType_Type(Integer32):
    """Custom type worpQoSSFClassSchedularType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("be", 2),
          ("rtpS", 1))
    )


_WorpQoSSFClassSchedularType_Type.__name__ = "Integer32"
_WorpQoSSFClassSchedularType_Object = MibTableColumn
worpQoSSFClassSchedularType = _WorpQoSSFClassSchedularType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 3),
    _WorpQoSSFClassSchedularType_Type()
)
worpQoSSFClassSchedularType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassSchedularType.setStatus("current")


class _WorpQoSSFClassDirection_Type(Integer32):
    """Custom type worpQoSSFClassDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("uplink", 1))
    )


_WorpQoSSFClassDirection_Type.__name__ = "Integer32"
_WorpQoSSFClassDirection_Object = MibTableColumn
worpQoSSFClassDirection = _WorpQoSSFClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 4),
    _WorpQoSSFClassDirection_Type()
)
worpQoSSFClassDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassDirection.setStatus("current")


class _WorpQoSSFClassStatus_Type(Integer32):
    """Custom type worpQoSSFClassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("in-active", 2))
    )


_WorpQoSSFClassStatus_Type.__name__ = "Integer32"
_WorpQoSSFClassStatus_Object = MibTableColumn
worpQoSSFClassStatus = _WorpQoSSFClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 5),
    _WorpQoSSFClassStatus_Type()
)
worpQoSSFClassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSSFClassStatus.setStatus("current")


class _WorpQoSSFClassMIR_Type(Unsigned32):
    """Custom type worpQoSSFClassMIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 307200),
    )


_WorpQoSSFClassMIR_Type.__name__ = "Unsigned32"
_WorpQoSSFClassMIR_Object = MibTableColumn
worpQoSSFClassMIR = _WorpQoSSFClassMIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 6),
    _WorpQoSSFClassMIR_Type()
)
worpQoSSFClassMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassMIR.setStatus("current")


class _WorpQoSSFClassCIR_Type(Unsigned32):
    """Custom type worpQoSSFClassCIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 307200),
    )


_WorpQoSSFClassCIR_Type.__name__ = "Unsigned32"
_WorpQoSSFClassCIR_Object = MibTableColumn
worpQoSSFClassCIR = _WorpQoSSFClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 7),
    _WorpQoSSFClassCIR_Type()
)
worpQoSSFClassCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassCIR.setStatus("current")


class _WorpQoSSFClassMaxLatency_Type(Unsigned32):
    """Custom type worpQoSSFClassMaxLatency based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_WorpQoSSFClassMaxLatency_Type.__name__ = "Unsigned32"
_WorpQoSSFClassMaxLatency_Object = MibTableColumn
worpQoSSFClassMaxLatency = _WorpQoSSFClassMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 8),
    _WorpQoSSFClassMaxLatency_Type()
)
worpQoSSFClassMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassMaxLatency.setStatus("current")


class _WorpQoSSFClassTolerableJitter_Type(Unsigned32):
    """Custom type worpQoSSFClassTolerableJitter based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WorpQoSSFClassTolerableJitter_Type.__name__ = "Unsigned32"
_WorpQoSSFClassTolerableJitter_Object = MibTableColumn
worpQoSSFClassTolerableJitter = _WorpQoSSFClassTolerableJitter_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 9),
    _WorpQoSSFClassTolerableJitter_Type()
)
worpQoSSFClassTolerableJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassTolerableJitter.setStatus("current")


class _WorpQoSSFClassTrafficPriority_Type(Unsigned32):
    """Custom type worpQoSSFClassTrafficPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WorpQoSSFClassTrafficPriority_Type.__name__ = "Unsigned32"
_WorpQoSSFClassTrafficPriority_Object = MibTableColumn
worpQoSSFClassTrafficPriority = _WorpQoSSFClassTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 10),
    _WorpQoSSFClassTrafficPriority_Type()
)
worpQoSSFClassTrafficPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassTrafficPriority.setStatus("current")


class _WorpQoSSFClassNumOfMesgInBurst_Type(Unsigned32):
    """Custom type worpQoSSFClassNumOfMesgInBurst based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WorpQoSSFClassNumOfMesgInBurst_Type.__name__ = "Unsigned32"
_WorpQoSSFClassNumOfMesgInBurst_Object = MibTableColumn
worpQoSSFClassNumOfMesgInBurst = _WorpQoSSFClassNumOfMesgInBurst_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 11),
    _WorpQoSSFClassNumOfMesgInBurst_Type()
)
worpQoSSFClassNumOfMesgInBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassNumOfMesgInBurst.setStatus("current")


class _WorpQoSSFClassTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSSFClassTableEntryStatus based on RowStatus"""


_WorpQoSSFClassTableEntryStatus_Object = MibTableColumn
worpQoSSFClassTableEntryStatus = _WorpQoSSFClassTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 6, 1, 12),
    _WorpQoSSFClassTableEntryStatus_Type()
)
worpQoSSFClassTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSFClassTableEntryStatus.setStatus("current")
_WorpQoSClassTable_Object = MibTable
worpQoSClassTable = _WorpQoSClassTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7)
)
if mibBuilder.loadTexts:
    worpQoSClassTable.setStatus("current")
_WorpQoSClassTableEntry_Object = MibTableRow
worpQoSClassTableEntry = _WorpQoSClassTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1)
)
worpQoSClassTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSClassTableIndex"),
    (0, "PROXIM-MIB", "worpQoSSFClassTableIndex"),
    (0, "PROXIM-MIB", "worpQoSPIRTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSClassTableEntry.setStatus("current")


class _WorpQoSClassTableIndex_Type(Unsigned32):
    """Custom type worpQoSClassTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WorpQoSClassTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSClassTableIndex_Object = MibTableColumn
worpQoSClassTableIndex = _WorpQoSClassTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 1),
    _WorpQoSClassTableIndex_Type()
)
worpQoSClassTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSClassTableIndex.setStatus("current")


class _WorpQoSClassSFCTableIndex_Type(Unsigned32):
    """Custom type worpQoSClassSFCTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WorpQoSClassSFCTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSClassSFCTableIndex_Object = MibTableColumn
worpQoSClassSFCTableIndex = _WorpQoSClassSFCTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 2),
    _WorpQoSClassSFCTableIndex_Type()
)
worpQoSClassSFCTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSClassSFCTableIndex.setStatus("current")


class _WorpQoSClassPIRTableIndex_Type(Unsigned32):
    """Custom type worpQoSClassPIRTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WorpQoSClassPIRTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSClassPIRTableIndex_Object = MibTableColumn
worpQoSClassPIRTableIndex = _WorpQoSClassPIRTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 3),
    _WorpQoSClassPIRTableIndex_Type()
)
worpQoSClassPIRTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSClassPIRTableIndex.setStatus("current")


class _WorpQoSClassSFCValue_Type(Unsigned32):
    """Custom type worpQoSClassSFCValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WorpQoSClassSFCValue_Type.__name__ = "Unsigned32"
_WorpQoSClassSFCValue_Object = MibTableColumn
worpQoSClassSFCValue = _WorpQoSClassSFCValue_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 4),
    _WorpQoSClassSFCValue_Type()
)
worpQoSClassSFCValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSClassSFCValue.setStatus("current")


class _WorpQoSClassPIRValue_Type(Unsigned32):
    """Custom type worpQoSClassPIRValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WorpQoSClassPIRValue_Type.__name__ = "Unsigned32"
_WorpQoSClassPIRValue_Object = MibTableColumn
worpQoSClassPIRValue = _WorpQoSClassPIRValue_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 5),
    _WorpQoSClassPIRValue_Type()
)
worpQoSClassPIRValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSClassPIRValue.setStatus("current")


class _WorpQoSClassName_Type(DisplayString):
    """Custom type worpQoSClassName based on DisplayString"""
    defaultValue = OctetString("default-class")


_WorpQoSClassName_Object = MibTableColumn
worpQoSClassName = _WorpQoSClassName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 6),
    _WorpQoSClassName_Type()
)
worpQoSClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSClassName.setStatus("current")


class _WorpQoSClassPriority_Type(Unsigned32):
    """Custom type worpQoSClassPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WorpQoSClassPriority_Type.__name__ = "Unsigned32"
_WorpQoSClassPriority_Object = MibTableColumn
worpQoSClassPriority = _WorpQoSClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 7),
    _WorpQoSClassPriority_Type()
)
worpQoSClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSClassPriority.setStatus("current")


class _WorpQoSClassTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSClassTableEntryStatus based on RowStatus"""


_WorpQoSClassTableEntryStatus_Object = MibTableColumn
worpQoSClassTableEntryStatus = _WorpQoSClassTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 7, 1, 8),
    _WorpQoSClassTableEntryStatus_Type()
)
worpQoSClassTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSClassTableEntryStatus.setStatus("current")
_WorpQoSSUTable_Object = MibTable
worpQoSSUTable = _WorpQoSSUTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8)
)
if mibBuilder.loadTexts:
    worpQoSSUTable.setStatus("current")
_WorpQoSSUTableEntry_Object = MibTableRow
worpQoSSUTableEntry = _WorpQoSSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1)
)
worpQoSSUTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpQoSSUTableIndex"),
)
if mibBuilder.loadTexts:
    worpQoSSUTableEntry.setStatus("current")


class _WorpQoSSUTableIndex_Type(Unsigned32):
    """Custom type worpQoSSUTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_WorpQoSSUTableIndex_Type.__name__ = "Unsigned32"
_WorpQoSSUTableIndex_Object = MibTableColumn
worpQoSSUTableIndex = _WorpQoSSUTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1, 1),
    _WorpQoSSUTableIndex_Type()
)
worpQoSSUTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpQoSSUTableIndex.setStatus("current")
_WorpQoSSUMACAddress_Type = MacAddress
_WorpQoSSUMACAddress_Object = MibTableColumn
worpQoSSUMACAddress = _WorpQoSSUMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1, 2),
    _WorpQoSSUMACAddress_Type()
)
worpQoSSUMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSUMACAddress.setStatus("current")


class _WorpQoSSUQoSClassIndex_Type(Unsigned32):
    """Custom type worpQoSSUQoSClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WorpQoSSUQoSClassIndex_Type.__name__ = "Unsigned32"
_WorpQoSSUQoSClassIndex_Object = MibTableColumn
worpQoSSUQoSClassIndex = _WorpQoSSUQoSClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1, 3),
    _WorpQoSSUQoSClassIndex_Type()
)
worpQoSSUQoSClassIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSUQoSClassIndex.setStatus("current")


class _WorpQoSSUComment_Type(DisplayString):
    """Custom type worpQoSSUComment based on DisplayString"""
    defaultValue = OctetString("default-su")


_WorpQoSSUComment_Object = MibTableColumn
worpQoSSUComment = _WorpQoSSUComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1, 4),
    _WorpQoSSUComment_Type()
)
worpQoSSUComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSUComment.setStatus("current")


class _WorpQoSSUTableEntryStatus_Type(RowStatus):
    """Custom type worpQoSSUTableEntryStatus based on RowStatus"""


_WorpQoSSUTableEntryStatus_Object = MibTableColumn
worpQoSSUTableEntryStatus = _WorpQoSSUTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 8, 1, 5),
    _WorpQoSSUTableEntryStatus_Type()
)
worpQoSSUTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSSUTableEntryStatus.setStatus("current")


class _WorpQoSDefaultClass_Type(Unsigned32):
    """Custom type worpQoSDefaultClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WorpQoSDefaultClass_Type.__name__ = "Unsigned32"
_WorpQoSDefaultClass_Object = MibScalar
worpQoSDefaultClass = _WorpQoSDefaultClass_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 9),
    _WorpQoSDefaultClass_Type()
)
worpQoSDefaultClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSDefaultClass.setStatus("current")


class _WorpQoSL2BroadcastClass_Type(Unsigned32):
    """Custom type worpQoSL2BroadcastClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WorpQoSL2BroadcastClass_Type.__name__ = "Unsigned32"
_WorpQoSL2BroadcastClass_Object = MibScalar
worpQoSL2BroadcastClass = _WorpQoSL2BroadcastClass_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 3, 5, 10),
    _WorpQoSL2BroadcastClass_Type()
)
worpQoSL2BroadcastClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpQoSL2BroadcastClass.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4)
)
_NetIp_ObjectIdentity = ObjectIdentity
netIp = _NetIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1)
)
_NetIpCfgTable_Object = MibTable
netIpCfgTable = _NetIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    netIpCfgTable.setStatus("current")
_NetIpCfgTableEntry_Object = MibTableRow
netIpCfgTableEntry = _NetIpCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1)
)
netIpCfgTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "netIpCfgTableIndex"),
)
if mibBuilder.loadTexts:
    netIpCfgTableEntry.setStatus("current")
_NetIpCfgTableIndex_Type = Unsigned32
_NetIpCfgTableIndex_Object = MibTableColumn
netIpCfgTableIndex = _NetIpCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1, 1),
    _NetIpCfgTableIndex_Type()
)
netIpCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIpCfgTableIndex.setStatus("current")


class _NetIpCfgIPAddress_Type(IpAddress):
    """Custom type netIpCfgIPAddress based on IpAddress"""
    defaultHexValue = "a9fe8084"


_NetIpCfgIPAddress_Object = MibTableColumn
netIpCfgIPAddress = _NetIpCfgIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1, 2),
    _NetIpCfgIPAddress_Type()
)
netIpCfgIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpCfgIPAddress.setStatus("current")


class _NetIpCfgSubnetMask_Type(IpAddress):
    """Custom type netIpCfgSubnetMask based on IpAddress"""
    defaultHexValue = "ffff0000"


_NetIpCfgSubnetMask_Object = MibTableColumn
netIpCfgSubnetMask = _NetIpCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1, 3),
    _NetIpCfgSubnetMask_Type()
)
netIpCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpCfgSubnetMask.setStatus("current")
_NetIpCfgDefaultRouterIPAddress_Type = IpAddress
_NetIpCfgDefaultRouterIPAddress_Object = MibTableColumn
netIpCfgDefaultRouterIPAddress = _NetIpCfgDefaultRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1, 4),
    _NetIpCfgDefaultRouterIPAddress_Type()
)
netIpCfgDefaultRouterIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpCfgDefaultRouterIPAddress.setStatus("deprecated")


class _NetIpCfgAddressType_Type(Integer32):
    """Custom type netIpCfgAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_NetIpCfgAddressType_Type.__name__ = "Integer32"
_NetIpCfgAddressType_Object = MibTableColumn
netIpCfgAddressType = _NetIpCfgAddressType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 1, 1, 5),
    _NetIpCfgAddressType_Type()
)
netIpCfgAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpCfgAddressType.setStatus("current")
_NetIpWirelessCfgTable_Object = MibTable
netIpWirelessCfgTable = _NetIpWirelessCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    netIpWirelessCfgTable.setStatus("current")
_NetIpWirelessCfgTableEntry_Object = MibTableRow
netIpWirelessCfgTableEntry = _NetIpWirelessCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 2, 1)
)
netIpWirelessCfgTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "netIpWirelessCfgTableIndex"),
)
if mibBuilder.loadTexts:
    netIpWirelessCfgTableEntry.setStatus("current")
_NetIpWirelessCfgTableIndex_Type = Unsigned32
_NetIpWirelessCfgTableIndex_Object = MibTableColumn
netIpWirelessCfgTableIndex = _NetIpWirelessCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 2, 1, 1),
    _NetIpWirelessCfgTableIndex_Type()
)
netIpWirelessCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIpWirelessCfgTableIndex.setStatus("current")
_NetIpWirelessCfgIPAddress_Type = IpAddress
_NetIpWirelessCfgIPAddress_Object = MibTableColumn
netIpWirelessCfgIPAddress = _NetIpWirelessCfgIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 2, 1, 2),
    _NetIpWirelessCfgIPAddress_Type()
)
netIpWirelessCfgIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpWirelessCfgIPAddress.setStatus("current")
_NetIpWirelessCfgSubnetMask_Type = IpAddress
_NetIpWirelessCfgSubnetMask_Object = MibTableColumn
netIpWirelessCfgSubnetMask = _NetIpWirelessCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 2, 1, 3),
    _NetIpWirelessCfgSubnetMask_Type()
)
netIpWirelessCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpWirelessCfgSubnetMask.setStatus("current")
_NetIpStaticRouteTable_Object = MibTable
netIpStaticRouteTable = _NetIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    netIpStaticRouteTable.setStatus("current")
_NetIpStaticRouteTableEntry_Object = MibTableRow
netIpStaticRouteTableEntry = _NetIpStaticRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1)
)
netIpStaticRouteTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "netIpStaticRouteTableIndex"),
)
if mibBuilder.loadTexts:
    netIpStaticRouteTableEntry.setStatus("current")


class _NetIpStaticRouteTableIndex_Type(Unsigned32):
    """Custom type netIpStaticRouteTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NetIpStaticRouteTableIndex_Type.__name__ = "Unsigned32"
_NetIpStaticRouteTableIndex_Object = MibTableColumn
netIpStaticRouteTableIndex = _NetIpStaticRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 1),
    _NetIpStaticRouteTableIndex_Type()
)
netIpStaticRouteTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIpStaticRouteTableIndex.setStatus("current")
_NetIpStaticRouteDestAddr_Type = IpAddress
_NetIpStaticRouteDestAddr_Object = MibTableColumn
netIpStaticRouteDestAddr = _NetIpStaticRouteDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 2),
    _NetIpStaticRouteDestAddr_Type()
)
netIpStaticRouteDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpStaticRouteDestAddr.setStatus("current")
_NetIpStaticRouteMask_Type = IpAddress
_NetIpStaticRouteMask_Object = MibTableColumn
netIpStaticRouteMask = _NetIpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 3),
    _NetIpStaticRouteMask_Type()
)
netIpStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpStaticRouteMask.setStatus("current")
_NetIpStaticRouteNextHop_Type = IpAddress
_NetIpStaticRouteNextHop_Object = MibTableColumn
netIpStaticRouteNextHop = _NetIpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 4),
    _NetIpStaticRouteNextHop_Type()
)
netIpStaticRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpStaticRouteNextHop.setStatus("current")


class _NetIpStaticRouteMetric_Type(Unsigned32):
    """Custom type netIpStaticRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NetIpStaticRouteMetric_Type.__name__ = "Unsigned32"
_NetIpStaticRouteMetric_Object = MibTableColumn
netIpStaticRouteMetric = _NetIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 5),
    _NetIpStaticRouteMetric_Type()
)
netIpStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpStaticRouteMetric.setStatus("current")
_NetIpStaticRouteTableEntryStatus_Type = RowStatus
_NetIpStaticRouteTableEntryStatus_Object = MibTableColumn
netIpStaticRouteTableEntryStatus = _NetIpStaticRouteTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 1, 3, 1, 6),
    _NetIpStaticRouteTableEntryStatus_Type()
)
netIpStaticRouteTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIpStaticRouteTableEntryStatus.setStatus("current")
_NetCfg_ObjectIdentity = ObjectIdentity
netCfg = _NetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2)
)


class _NetCfgClearIntfStats_Type(Integer32):
    """Custom type netCfgClearIntfStats based on Integer32"""
    defaultValue = 1

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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("arpTable", 5),
          ("bridgeStats", 4),
          ("ethernetIntf1", 2),
          ("ethernetIntf2", 3),
          ("learnTable", 10),
          ("none", 1),
          ("wirelessIntf1", 6),
          ("wirelessIntf2", 7),
          ("worpIntf1", 8),
          ("worpIntf2", 9))
    )


_NetCfgClearIntfStats_Type.__name__ = "Integer32"
_NetCfgClearIntfStats_Object = MibScalar
netCfgClearIntfStats = _NetCfgClearIntfStats_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 1),
    _NetCfgClearIntfStats_Type()
)
netCfgClearIntfStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCfgClearIntfStats.setStatus("current")
_NetCfgAllIntfDefaultRouterAddr_Type = IpAddress
_NetCfgAllIntfDefaultRouterAddr_Object = MibScalar
netCfgAllIntfDefaultRouterAddr = _NetCfgAllIntfDefaultRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 2),
    _NetCfgAllIntfDefaultRouterAddr_Type()
)
netCfgAllIntfDefaultRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCfgAllIntfDefaultRouterAddr.setStatus("current")


class _NetCfgSupportedInterfaces_Type(DisplayString):
    """Custom type netCfgSupportedInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NetCfgSupportedInterfaces_Type.__name__ = "DisplayString"
_NetCfgSupportedInterfaces_Object = MibScalar
netCfgSupportedInterfaces = _NetCfgSupportedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 3),
    _NetCfgSupportedInterfaces_Type()
)
netCfgSupportedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCfgSupportedInterfaces.setStatus("current")


class _NetCfgStaticRouteStatus_Type(Integer32):
    """Custom type netCfgStaticRouteStatus based on Integer32"""
    defaultValue = 2

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


_NetCfgStaticRouteStatus_Type.__name__ = "Integer32"
_NetCfgStaticRouteStatus_Object = MibScalar
netCfgStaticRouteStatus = _NetCfgStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 4),
    _NetCfgStaticRouteStatus_Type()
)
netCfgStaticRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCfgStaticRouteStatus.setStatus("current")


class _WirelessInActivityTimer_Type(Unsigned32):
    """Custom type wirelessInActivityTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WirelessInActivityTimer_Type.__name__ = "Unsigned32"
_WirelessInActivityTimer_Object = MibScalar
wirelessInActivityTimer = _WirelessInActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 5),
    _WirelessInActivityTimer_Type()
)
wirelessInActivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInActivityTimer.setStatus("deprecated")


class _EthernetInActivityTimer_Type(Unsigned32):
    """Custom type ethernetInActivityTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_EthernetInActivityTimer_Type.__name__ = "Unsigned32"
_EthernetInActivityTimer_Object = MibScalar
ethernetInActivityTimer = _EthernetInActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 6),
    _EthernetInActivityTimer_Type()
)
ethernetInActivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInActivityTimer.setStatus("current")
_NetCfgPrimaryDNSIpAddress_Type = IpAddress
_NetCfgPrimaryDNSIpAddress_Object = MibScalar
netCfgPrimaryDNSIpAddress = _NetCfgPrimaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 7),
    _NetCfgPrimaryDNSIpAddress_Type()
)
netCfgPrimaryDNSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCfgPrimaryDNSIpAddress.setStatus("current")
_NetCfgSecondaryDNSIpAddress_Type = IpAddress
_NetCfgSecondaryDNSIpAddress_Object = MibScalar
netCfgSecondaryDNSIpAddress = _NetCfgSecondaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 8),
    _NetCfgSecondaryDNSIpAddress_Type()
)
netCfgSecondaryDNSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCfgSecondaryDNSIpAddress.setStatus("current")


class _WirelessInActivityTimerInSecs_Type(Unsigned32):
    """Custom type wirelessInActivityTimerInSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WirelessInActivityTimerInSecs_Type.__name__ = "Unsigned32"
_WirelessInActivityTimerInSecs_Object = MibScalar
wirelessInActivityTimerInSecs = _WirelessInActivityTimerInSecs_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 2, 9),
    _WirelessInActivityTimerInSecs_Type()
)
wirelessInActivityTimerInSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInActivityTimerInSecs.setStatus("current")
_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3)
)


class _NatStatus_Type(Integer32):
    """Custom type natStatus based on Integer32"""
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


_NatStatus_Type.__name__ = "Integer32"
_NatStatus_Object = MibScalar
natStatus = _NatStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 1),
    _NatStatus_Type()
)
natStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStatus.setStatus("current")


class _NatPortBindingStatus_Type(Integer32):
    """Custom type natPortBindingStatus based on Integer32"""
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


_NatPortBindingStatus_Type.__name__ = "Integer32"
_NatPortBindingStatus_Object = MibScalar
natPortBindingStatus = _NatPortBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 2),
    _NatPortBindingStatus_Type()
)
natPortBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortBindingStatus.setStatus("current")
_NatStaticPortBindTable_Object = MibTable
natStaticPortBindTable = _NatStaticPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    natStaticPortBindTable.setStatus("current")
_NatStaticPortBindTableEntry_Object = MibTableRow
natStaticPortBindTableEntry = _NatStaticPortBindTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1)
)
natStaticPortBindTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "natStaticPortBindTableIndex"),
)
if mibBuilder.loadTexts:
    natStaticPortBindTableEntry.setStatus("current")


class _NatStaticPortBindTableIndex_Type(Unsigned32):
    """Custom type natStaticPortBindTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NatStaticPortBindTableIndex_Type.__name__ = "Unsigned32"
_NatStaticPortBindTableIndex_Object = MibTableColumn
natStaticPortBindTableIndex = _NatStaticPortBindTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 1),
    _NatStaticPortBindTableIndex_Type()
)
natStaticPortBindTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStaticPortBindTableIndex.setStatus("current")
_NatStaticPortBindLocalAddr_Type = IpAddress
_NatStaticPortBindLocalAddr_Object = MibTableColumn
natStaticPortBindLocalAddr = _NatStaticPortBindLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 2),
    _NatStaticPortBindLocalAddr_Type()
)
natStaticPortBindLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticPortBindLocalAddr.setStatus("current")


class _NatStaticPortBindPortType_Type(Integer32):
    """Custom type natStaticPortBindPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_NatStaticPortBindPortType_Type.__name__ = "Integer32"
_NatStaticPortBindPortType_Object = MibTableColumn
natStaticPortBindPortType = _NatStaticPortBindPortType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 3),
    _NatStaticPortBindPortType_Type()
)
natStaticPortBindPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticPortBindPortType.setStatus("current")


class _NatStaticPortBindStartPortNum_Type(Unsigned32):
    """Custom type natStaticPortBindStartPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatStaticPortBindStartPortNum_Type.__name__ = "Unsigned32"
_NatStaticPortBindStartPortNum_Object = MibTableColumn
natStaticPortBindStartPortNum = _NatStaticPortBindStartPortNum_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 4),
    _NatStaticPortBindStartPortNum_Type()
)
natStaticPortBindStartPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticPortBindStartPortNum.setStatus("current")


class _NatStaticPortBindEndPortNum_Type(Unsigned32):
    """Custom type natStaticPortBindEndPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatStaticPortBindEndPortNum_Type.__name__ = "Unsigned32"
_NatStaticPortBindEndPortNum_Object = MibTableColumn
natStaticPortBindEndPortNum = _NatStaticPortBindEndPortNum_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 5),
    _NatStaticPortBindEndPortNum_Type()
)
natStaticPortBindEndPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticPortBindEndPortNum.setStatus("current")
_NatStaticPortBindTableEntryStatus_Type = RowStatus
_NatStaticPortBindTableEntryStatus_Object = MibTableColumn
natStaticPortBindTableEntryStatus = _NatStaticPortBindTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 3, 3, 1, 6),
    _NatStaticPortBindTableEntryStatus_Type()
)
natStaticPortBindTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticPortBindTableEntryStatus.setStatus("current")
_Rip_ObjectIdentity = ObjectIdentity
rip = _Rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4)
)


class _RipConfigStatus_Type(Integer32):
    """Custom type ripConfigStatus based on Integer32"""
    defaultValue = 2

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


_RipConfigStatus_Type.__name__ = "Integer32"
_RipConfigStatus_Object = MibScalar
ripConfigStatus = _RipConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 1),
    _RipConfigStatus_Type()
)
ripConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigStatus.setStatus("current")
_RipConfigTable_Object = MibTable
ripConfigTable = _RipConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ripConfigTable.setStatus("current")
_RipConfigTableEntry_Object = MibTableRow
ripConfigTableEntry = _RipConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1)
)
ripConfigTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "ripConfigTableIndex"),
)
if mibBuilder.loadTexts:
    ripConfigTableEntry.setStatus("current")
_RipConfigTableIndex_Type = Unsigned32
_RipConfigTableIndex_Object = MibTableColumn
ripConfigTableIndex = _RipConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 1),
    _RipConfigTableIndex_Type()
)
ripConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripConfigTableIndex.setStatus("current")
_RipInterfaceName_Type = DisplayString
_RipInterfaceName_Object = MibTableColumn
ripInterfaceName = _RipInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 2),
    _RipInterfaceName_Type()
)
ripInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInterfaceName.setStatus("current")


class _RipInterfaceStatus_Type(Integer32):
    """Custom type ripInterfaceStatus based on Integer32"""
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


_RipInterfaceStatus_Type.__name__ = "Integer32"
_RipInterfaceStatus_Object = MibTableColumn
ripInterfaceStatus = _RipInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 3),
    _RipInterfaceStatus_Type()
)
ripInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceStatus.setStatus("current")


class _RipInterfaceAuthType_Type(Integer32):
    """Custom type ripInterfaceAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 3),
          ("simple", 1))
    )


_RipInterfaceAuthType_Type.__name__ = "Integer32"
_RipInterfaceAuthType_Object = MibTableColumn
ripInterfaceAuthType = _RipInterfaceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 4),
    _RipInterfaceAuthType_Type()
)
ripInterfaceAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceAuthType.setStatus("current")


class _RipInterfaceAuthKey_Type(DisplayString):
    """Custom type ripInterfaceAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RipInterfaceAuthKey_Type.__name__ = "DisplayString"
_RipInterfaceAuthKey_Object = MibTableColumn
ripInterfaceAuthKey = _RipInterfaceAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 5),
    _RipInterfaceAuthKey_Type()
)
ripInterfaceAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceAuthKey.setStatus("current")


class _RipInterfaceVersionNum_Type(Integer32):
    """Custom type ripInterfaceVersionNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("v1", 1),
          ("v2", 2))
    )


_RipInterfaceVersionNum_Type.__name__ = "Integer32"
_RipInterfaceVersionNum_Object = MibTableColumn
ripInterfaceVersionNum = _RipInterfaceVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 6),
    _RipInterfaceVersionNum_Type()
)
ripInterfaceVersionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceVersionNum.setStatus("current")


class _RipReceiveOnly_Type(Integer32):
    """Custom type ripReceiveOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_RipReceiveOnly_Type.__name__ = "Integer32"
_RipReceiveOnly_Object = MibTableColumn
ripReceiveOnly = _RipReceiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 4, 4, 2, 1, 7),
    _RipReceiveOnly_Type()
)
ripReceiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReceiveOnly.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5)
)


class _VlanStatus_Type(Integer32):
    """Custom type vlanStatus based on Integer32"""
    defaultValue = 2

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


_VlanStatus_Type.__name__ = "Integer32"
_VlanStatus_Object = MibScalar
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 1),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")


class _MgmtVLANIdentifier_Type(VlanId):
    """Custom type mgmtVLANIdentifier based on VlanId"""
    defaultValue = -1


_MgmtVLANIdentifier_Object = MibScalar
mgmtVLANIdentifier = _MgmtVLANIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 2),
    _MgmtVLANIdentifier_Type()
)
mgmtVLANIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANIdentifier.setStatus("current")


class _MgmtVLANPriority_Type(Unsigned32):
    """Custom type mgmtVLANPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtVLANPriority_Type.__name__ = "Unsigned32"
_MgmtVLANPriority_Object = MibScalar
mgmtVLANPriority = _MgmtVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 3),
    _MgmtVLANPriority_Type()
)
mgmtVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANPriority.setStatus("current")
_VlanEthCfgTable_Object = MibTable
vlanEthCfgTable = _VlanEthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    vlanEthCfgTable.setStatus("current")
_VlanEthCfgTableEntry_Object = MibTableRow
vlanEthCfgTableEntry = _VlanEthCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1)
)
vlanEthCfgTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "vlanEthCfgTableIndex"),
)
if mibBuilder.loadTexts:
    vlanEthCfgTableEntry.setStatus("current")


class _VlanEthCfgTableIndex_Type(Unsigned32):
    """Custom type vlanEthCfgTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_VlanEthCfgTableIndex_Type.__name__ = "Unsigned32"
_VlanEthCfgTableIndex_Object = MibTableColumn
vlanEthCfgTableIndex = _VlanEthCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1, 1),
    _VlanEthCfgTableIndex_Type()
)
vlanEthCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanEthCfgTableIndex.setStatus("current")


class _VlanMode_Type(Integer32):
    """Custom type vlanMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("transparent", 1),
          ("trunk", 3))
    )


_VlanMode_Type.__name__ = "Integer32"
_VlanMode_Object = MibTableColumn
vlanMode = _VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1, 2),
    _VlanMode_Type()
)
vlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMode.setStatus("current")


class _AccessVLANId_Type(VlanId):
    """Custom type accessVLANId based on VlanId"""
    defaultValue = -1


_AccessVLANId_Object = MibTableColumn
accessVLANId = _AccessVLANId_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1, 3),
    _AccessVLANId_Type()
)
accessVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessVLANId.setStatus("current")


class _AccessVLANPriority_Type(Unsigned32):
    """Custom type accessVLANPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AccessVLANPriority_Type.__name__ = "Unsigned32"
_AccessVLANPriority_Object = MibTableColumn
accessVLANPriority = _AccessVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1, 4),
    _AccessVLANPriority_Type()
)
accessVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessVLANPriority.setStatus("current")


class _UntaggedFrames_Type(Integer32):
    """Custom type untaggedFrames based on Integer32"""
    defaultValue = 2

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


_UntaggedFrames_Type.__name__ = "Integer32"
_UntaggedFrames_Object = MibTableColumn
untaggedFrames = _UntaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 4, 1, 5),
    _UntaggedFrames_Type()
)
untaggedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    untaggedFrames.setStatus("current")
_VlanEthTrunkTable_Object = MibTable
vlanEthTrunkTable = _VlanEthTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    vlanEthTrunkTable.setStatus("current")
_VlanEthTrunkTableEntry_Object = MibTableRow
vlanEthTrunkTableEntry = _VlanEthTrunkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5, 1)
)
vlanEthTrunkTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "vlanEthTrunkTableIndex"),
    (0, "PROXIM-MIB", "vlanEthTrunkTableSecIndex"),
)
if mibBuilder.loadTexts:
    vlanEthTrunkTableEntry.setStatus("current")


class _VlanEthTrunkTableIndex_Type(Unsigned32):
    """Custom type vlanEthTrunkTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VlanEthTrunkTableIndex_Type.__name__ = "Unsigned32"
_VlanEthTrunkTableIndex_Object = MibTableColumn
vlanEthTrunkTableIndex = _VlanEthTrunkTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5, 1, 1),
    _VlanEthTrunkTableIndex_Type()
)
vlanEthTrunkTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanEthTrunkTableIndex.setStatus("current")


class _VlanEthTrunkTableSecIndex_Type(Unsigned32):
    """Custom type vlanEthTrunkTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VlanEthTrunkTableSecIndex_Type.__name__ = "Unsigned32"
_VlanEthTrunkTableSecIndex_Object = MibTableColumn
vlanEthTrunkTableSecIndex = _VlanEthTrunkTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5, 1, 2),
    _VlanEthTrunkTableSecIndex_Type()
)
vlanEthTrunkTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanEthTrunkTableSecIndex.setStatus("current")
_EthVLANTrunkId_Type = VlanId
_EthVLANTrunkId_Object = MibTableColumn
ethVLANTrunkId = _EthVLANTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5, 1, 3),
    _EthVLANTrunkId_Type()
)
ethVLANTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethVLANTrunkId.setStatus("current")
_VlanEthTrunkTableEntryStatus_Type = RowStatus
_VlanEthTrunkTableEntryStatus_Object = MibTableColumn
vlanEthTrunkTableEntryStatus = _VlanEthTrunkTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 5, 5, 1, 4),
    _VlanEthTrunkTableEntryStatus_Type()
)
vlanEthTrunkTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEthTrunkTableEntryStatus.setStatus("current")
_Filtering_ObjectIdentity = ObjectIdentity
filtering = _Filtering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6)
)


class _FilteringCtrl_Type(Integer32):
    """Custom type filteringCtrl based on Integer32"""
    defaultValue = 2

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


_FilteringCtrl_Type.__name__ = "Integer32"
_FilteringCtrl_Object = MibScalar
filteringCtrl = _FilteringCtrl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 1),
    _FilteringCtrl_Type()
)
filteringCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringCtrl.setStatus("current")


class _IntraBSSFiltering_Type(Integer32):
    """Custom type intraBSSFiltering based on Integer32"""
    defaultValue = 2

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


_IntraBSSFiltering_Type.__name__ = "Integer32"
_IntraBSSFiltering_Object = MibScalar
intraBSSFiltering = _IntraBSSFiltering_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 2),
    _IntraBSSFiltering_Type()
)
intraBSSFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intraBSSFiltering.setStatus("current")
_ProtocolFilter_ObjectIdentity = ObjectIdentity
protocolFilter = _ProtocolFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3)
)


class _EtherProtocolFilteringCtrl_Type(Integer32):
    """Custom type etherProtocolFilteringCtrl based on Integer32"""
    defaultValue = 4

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
        *(("allInterfaces", 3),
          ("disable", 4),
          ("ethernet", 1),
          ("wireless", 2))
    )


_EtherProtocolFilteringCtrl_Type.__name__ = "Integer32"
_EtherProtocolFilteringCtrl_Object = MibScalar
etherProtocolFilteringCtrl = _EtherProtocolFilteringCtrl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 1),
    _EtherProtocolFilteringCtrl_Type()
)
etherProtocolFilteringCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherProtocolFilteringCtrl.setStatus("current")


class _EtherProtocolFilteringType_Type(Integer32):
    """Custom type etherProtocolFilteringType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("passthru", 1))
    )


_EtherProtocolFilteringType_Type.__name__ = "Integer32"
_EtherProtocolFilteringType_Object = MibScalar
etherProtocolFilteringType = _EtherProtocolFilteringType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 2),
    _EtherProtocolFilteringType_Type()
)
etherProtocolFilteringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherProtocolFilteringType.setStatus("current")
_EtherProtocolFilterTable_Object = MibTable
etherProtocolFilterTable = _EtherProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    etherProtocolFilterTable.setStatus("current")
_EtherProtocolFilterTableEntry_Object = MibTableRow
etherProtocolFilterTableEntry = _EtherProtocolFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1)
)
etherProtocolFilterTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "etherProtocolFilterTableIndex"),
)
if mibBuilder.loadTexts:
    etherProtocolFilterTableEntry.setStatus("current")


class _EtherProtocolFilterTableIndex_Type(Unsigned32):
    """Custom type etherProtocolFilterTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EtherProtocolFilterTableIndex_Type.__name__ = "Unsigned32"
_EtherProtocolFilterTableIndex_Object = MibTableColumn
etherProtocolFilterTableIndex = _EtherProtocolFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1, 1),
    _EtherProtocolFilterTableIndex_Type()
)
etherProtocolFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherProtocolFilterTableIndex.setStatus("current")


class _EtherProtocolFilterProtocolName_Type(DisplayString):
    """Custom type etherProtocolFilterProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtherProtocolFilterProtocolName_Type.__name__ = "DisplayString"
_EtherProtocolFilterProtocolName_Object = MibTableColumn
etherProtocolFilterProtocolName = _EtherProtocolFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1, 2),
    _EtherProtocolFilterProtocolName_Type()
)
etherProtocolFilterProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherProtocolFilterProtocolName.setStatus("current")
_EtherProtocolFilterProtocolNumber_Type = OctetString
_EtherProtocolFilterProtocolNumber_Object = MibTableColumn
etherProtocolFilterProtocolNumber = _EtherProtocolFilterProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1, 3),
    _EtherProtocolFilterProtocolNumber_Type()
)
etherProtocolFilterProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherProtocolFilterProtocolNumber.setStatus("current")


class _EtherprotocolFilterStatus_Type(Integer32):
    """Custom type etherprotocolFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("passthru", 2))
    )


_EtherprotocolFilterStatus_Type.__name__ = "Integer32"
_EtherprotocolFilterStatus_Object = MibTableColumn
etherprotocolFilterStatus = _EtherprotocolFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1, 4),
    _EtherprotocolFilterStatus_Type()
)
etherprotocolFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherprotocolFilterStatus.setStatus("current")


class _EtherProtocolFilterTableStatus_Type(RowStatus):
    """Custom type etherProtocolFilterTableStatus based on RowStatus"""


_EtherProtocolFilterTableStatus_Object = MibTableColumn
etherProtocolFilterTableStatus = _EtherProtocolFilterTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 3, 3, 1, 5),
    _EtherProtocolFilterTableStatus_Type()
)
etherProtocolFilterTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherProtocolFilterTableStatus.setStatus("current")
_StaticMACAddrFilter_ObjectIdentity = ObjectIdentity
staticMACAddrFilter = _StaticMACAddrFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4)
)
_StaticMACAddrFilterTable_Object = MibTable
staticMACAddrFilterTable = _StaticMACAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    staticMACAddrFilterTable.setStatus("current")
_StaticMACAddrFilterTableEntry_Object = MibTableRow
staticMACAddrFilterTableEntry = _StaticMACAddrFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1)
)
staticMACAddrFilterTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "staticMACAddrFilterTableIndex"),
)
if mibBuilder.loadTexts:
    staticMACAddrFilterTableEntry.setStatus("current")


class _StaticMACAddrFilterTableIndex_Type(Unsigned32):
    """Custom type staticMACAddrFilterTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_StaticMACAddrFilterTableIndex_Type.__name__ = "Unsigned32"
_StaticMACAddrFilterTableIndex_Object = MibTableColumn
staticMACAddrFilterTableIndex = _StaticMACAddrFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 1),
    _StaticMACAddrFilterTableIndex_Type()
)
staticMACAddrFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMACAddrFilterTableIndex.setStatus("current")
_StaticMACAddrFilterWiredMACAddress_Type = MacAddress
_StaticMACAddrFilterWiredMACAddress_Object = MibTableColumn
staticMACAddrFilterWiredMACAddress = _StaticMACAddrFilterWiredMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 2),
    _StaticMACAddrFilterWiredMACAddress_Type()
)
staticMACAddrFilterWiredMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMACAddrFilterWiredMACAddress.setStatus("current")
_StaticMACAddrFilterWiredMACMask_Type = MacAddress
_StaticMACAddrFilterWiredMACMask_Object = MibTableColumn
staticMACAddrFilterWiredMACMask = _StaticMACAddrFilterWiredMACMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 3),
    _StaticMACAddrFilterWiredMACMask_Type()
)
staticMACAddrFilterWiredMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMACAddrFilterWiredMACMask.setStatus("current")
_StaticMACAddrFilterWirelessMACAddress_Type = MacAddress
_StaticMACAddrFilterWirelessMACAddress_Object = MibTableColumn
staticMACAddrFilterWirelessMACAddress = _StaticMACAddrFilterWirelessMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 4),
    _StaticMACAddrFilterWirelessMACAddress_Type()
)
staticMACAddrFilterWirelessMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMACAddrFilterWirelessMACAddress.setStatus("current")
_StaticMACAddrFilterWirelessMACMask_Type = MacAddress
_StaticMACAddrFilterWirelessMACMask_Object = MibTableColumn
staticMACAddrFilterWirelessMACMask = _StaticMACAddrFilterWirelessMACMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 5),
    _StaticMACAddrFilterWirelessMACMask_Type()
)
staticMACAddrFilterWirelessMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMACAddrFilterWirelessMACMask.setStatus("current")


class _StaticMACAddrFilterComment_Type(DisplayString):
    """Custom type staticMACAddrFilterComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaticMACAddrFilterComment_Type.__name__ = "DisplayString"
_StaticMACAddrFilterComment_Object = MibTableColumn
staticMACAddrFilterComment = _StaticMACAddrFilterComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 6),
    _StaticMACAddrFilterComment_Type()
)
staticMACAddrFilterComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMACAddrFilterComment.setStatus("current")


class _StaticMACAddrFilterTableEntryStatus_Type(RowStatus):
    """Custom type staticMACAddrFilterTableEntryStatus based on RowStatus"""


_StaticMACAddrFilterTableEntryStatus_Object = MibTableColumn
staticMACAddrFilterTableEntryStatus = _StaticMACAddrFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 4, 1, 1, 7),
    _StaticMACAddrFilterTableEntryStatus_Type()
)
staticMACAddrFilterTableEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMACAddrFilterTableEntryStatus.setStatus("current")
_AdvancedFiltering_ObjectIdentity = ObjectIdentity
advancedFiltering = _AdvancedFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5)
)
_AdvancedFilterTable_Object = MibTable
advancedFilterTable = _AdvancedFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    advancedFilterTable.setStatus("current")
_AdvancedFilterTableEntry_Object = MibTableRow
advancedFilterTableEntry = _AdvancedFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1, 1)
)
advancedFilterTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "advancedFilterTableIndex"),
)
if mibBuilder.loadTexts:
    advancedFilterTableEntry.setStatus("current")


class _AdvancedFilterTableIndex_Type(Unsigned32):
    """Custom type advancedFilterTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AdvancedFilterTableIndex_Type.__name__ = "Unsigned32"
_AdvancedFilterTableIndex_Object = MibTableColumn
advancedFilterTableIndex = _AdvancedFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1, 1, 1),
    _AdvancedFilterTableIndex_Type()
)
advancedFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedFilterTableIndex.setStatus("current")
_AdvancedFilterProtocolName_Type = DisplayString
_AdvancedFilterProtocolName_Object = MibTableColumn
advancedFilterProtocolName = _AdvancedFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1, 1, 2),
    _AdvancedFilterProtocolName_Type()
)
advancedFilterProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedFilterProtocolName.setStatus("current")


class _AdvancedFilterDirection_Type(Integer32):
    """Custom type advancedFilterDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet2wireless", 1),
          ("wireless2ethernet", 2))
    )


_AdvancedFilterDirection_Type.__name__ = "Integer32"
_AdvancedFilterDirection_Object = MibTableColumn
advancedFilterDirection = _AdvancedFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1, 1, 3),
    _AdvancedFilterDirection_Type()
)
advancedFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedFilterDirection.setStatus("current")


class _AdvancedFilterTableEntryStatus_Type(RowStatus):
    """Custom type advancedFilterTableEntryStatus based on RowStatus"""


_AdvancedFilterTableEntryStatus_Object = MibTableColumn
advancedFilterTableEntryStatus = _AdvancedFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 5, 1, 1, 4),
    _AdvancedFilterTableEntryStatus_Type()
)
advancedFilterTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedFilterTableEntryStatus.setStatus("current")
_TcpudpPortFilter_ObjectIdentity = ObjectIdentity
tcpudpPortFilter = _TcpudpPortFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6)
)


class _TcpudpPortFilterCtrl_Type(Integer32):
    """Custom type tcpudpPortFilterCtrl based on Integer32"""
    defaultValue = 2

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


_TcpudpPortFilterCtrl_Type.__name__ = "Integer32"
_TcpudpPortFilterCtrl_Object = MibScalar
tcpudpPortFilterCtrl = _TcpudpPortFilterCtrl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 1),
    _TcpudpPortFilterCtrl_Type()
)
tcpudpPortFilterCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpudpPortFilterCtrl.setStatus("current")
_TcpudpPortFilterTable_Object = MibTable
tcpudpPortFilterTable = _TcpudpPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    tcpudpPortFilterTable.setStatus("current")
_TcpudpPortFilterTableEntry_Object = MibTableRow
tcpudpPortFilterTableEntry = _TcpudpPortFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1)
)
tcpudpPortFilterTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "tcpudpPortFilterTableIndex"),
)
if mibBuilder.loadTexts:
    tcpudpPortFilterTableEntry.setStatus("current")


class _TcpudpPortFilterTableIndex_Type(Unsigned32):
    """Custom type tcpudpPortFilterTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TcpudpPortFilterTableIndex_Type.__name__ = "Unsigned32"
_TcpudpPortFilterTableIndex_Object = MibTableColumn
tcpudpPortFilterTableIndex = _TcpudpPortFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 1),
    _TcpudpPortFilterTableIndex_Type()
)
tcpudpPortFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpudpPortFilterTableIndex.setStatus("current")


class _TcpudpPortFilterProtocolName_Type(DisplayString):
    """Custom type tcpudpPortFilterProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TcpudpPortFilterProtocolName_Type.__name__ = "DisplayString"
_TcpudpPortFilterProtocolName_Object = MibTableColumn
tcpudpPortFilterProtocolName = _TcpudpPortFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 2),
    _TcpudpPortFilterProtocolName_Type()
)
tcpudpPortFilterProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpudpPortFilterProtocolName.setStatus("current")
_TcpudpPortFilterPortNumber_Type = Unsigned32
_TcpudpPortFilterPortNumber_Object = MibTableColumn
tcpudpPortFilterPortNumber = _TcpudpPortFilterPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 3),
    _TcpudpPortFilterPortNumber_Type()
)
tcpudpPortFilterPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpudpPortFilterPortNumber.setStatus("current")


class _TcpudpPortFilterPortType_Type(Integer32):
    """Custom type tcpudpPortFilterPortType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_TcpudpPortFilterPortType_Type.__name__ = "Integer32"
_TcpudpPortFilterPortType_Object = MibTableColumn
tcpudpPortFilterPortType = _TcpudpPortFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 4),
    _TcpudpPortFilterPortType_Type()
)
tcpudpPortFilterPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpudpPortFilterPortType.setStatus("current")


class _TcpudpPortFilterInterface_Type(Integer32):
    """Custom type tcpudpPortFilterInterface based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allInterfaces", 3),
          ("onlyEthernet", 1),
          ("onlyWireless", 2))
    )


_TcpudpPortFilterInterface_Type.__name__ = "Integer32"
_TcpudpPortFilterInterface_Object = MibTableColumn
tcpudpPortFilterInterface = _TcpudpPortFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 5),
    _TcpudpPortFilterInterface_Type()
)
tcpudpPortFilterInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpudpPortFilterInterface.setStatus("current")
_TcpudpPortFilterTableEntryStatus_Type = RowStatus
_TcpudpPortFilterTableEntryStatus_Object = MibTableColumn
tcpudpPortFilterTableEntryStatus = _TcpudpPortFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 6, 2, 1, 6),
    _TcpudpPortFilterTableEntryStatus_Type()
)
tcpudpPortFilterTableEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tcpudpPortFilterTableEntryStatus.setStatus("current")
_WorpIntraCellBlocking_ObjectIdentity = ObjectIdentity
worpIntraCellBlocking = _WorpIntraCellBlocking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7)
)


class _WorpIntraCellBlockingStatus_Type(Integer32):
    """Custom type worpIntraCellBlockingStatus based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingStatus_Type.__name__ = "Integer32"
_WorpIntraCellBlockingStatus_Object = MibScalar
worpIntraCellBlockingStatus = _WorpIntraCellBlockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 1),
    _WorpIntraCellBlockingStatus_Type()
)
worpIntraCellBlockingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingStatus.setStatus("current")
_WorpIntraCellBlockingMACTable_Object = MibTable
worpIntraCellBlockingMACTable = _WorpIntraCellBlockingMACTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    worpIntraCellBlockingMACTable.setStatus("current")
_WorpIntraCellBlockingMACTableEntry_Object = MibTableRow
worpIntraCellBlockingMACTableEntry = _WorpIntraCellBlockingMACTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1)
)
worpIntraCellBlockingMACTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpIntraCellBlockingMACTableIndex"),
)
if mibBuilder.loadTexts:
    worpIntraCellBlockingMACTableEntry.setStatus("current")


class _WorpIntraCellBlockingMACTableIndex_Type(Unsigned32):
    """Custom type worpIntraCellBlockingMACTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_WorpIntraCellBlockingMACTableIndex_Type.__name__ = "Unsigned32"
_WorpIntraCellBlockingMACTableIndex_Object = MibTableColumn
worpIntraCellBlockingMACTableIndex = _WorpIntraCellBlockingMACTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 1),
    _WorpIntraCellBlockingMACTableIndex_Type()
)
worpIntraCellBlockingMACTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpIntraCellBlockingMACTableIndex.setStatus("current")
_WorpIntraCellBlockingMACAddress_Type = MacAddress
_WorpIntraCellBlockingMACAddress_Object = MibTableColumn
worpIntraCellBlockingMACAddress = _WorpIntraCellBlockingMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 2),
    _WorpIntraCellBlockingMACAddress_Type()
)
worpIntraCellBlockingMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingMACAddress.setStatus("current")


class _WorpIntraCellBlockingGroupID1_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID1 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID1_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID1_Object = MibTableColumn
worpIntraCellBlockingGroupID1 = _WorpIntraCellBlockingGroupID1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 3),
    _WorpIntraCellBlockingGroupID1_Type()
)
worpIntraCellBlockingGroupID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID1.setStatus("current")


class _WorpIntraCellBlockingGroupID2_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID2 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID2_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID2_Object = MibTableColumn
worpIntraCellBlockingGroupID2 = _WorpIntraCellBlockingGroupID2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 4),
    _WorpIntraCellBlockingGroupID2_Type()
)
worpIntraCellBlockingGroupID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID2.setStatus("current")


class _WorpIntraCellBlockingGroupID3_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID3 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID3_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID3_Object = MibTableColumn
worpIntraCellBlockingGroupID3 = _WorpIntraCellBlockingGroupID3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 5),
    _WorpIntraCellBlockingGroupID3_Type()
)
worpIntraCellBlockingGroupID3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID3.setStatus("current")


class _WorpIntraCellBlockingGroupID4_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID4 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID4_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID4_Object = MibTableColumn
worpIntraCellBlockingGroupID4 = _WorpIntraCellBlockingGroupID4_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 6),
    _WorpIntraCellBlockingGroupID4_Type()
)
worpIntraCellBlockingGroupID4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID4.setStatus("current")


class _WorpIntraCellBlockingGroupID5_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID5 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID5_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID5_Object = MibTableColumn
worpIntraCellBlockingGroupID5 = _WorpIntraCellBlockingGroupID5_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 7),
    _WorpIntraCellBlockingGroupID5_Type()
)
worpIntraCellBlockingGroupID5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID5.setStatus("current")


class _WorpIntraCellBlockingGroupID6_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID6 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID6_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID6_Object = MibTableColumn
worpIntraCellBlockingGroupID6 = _WorpIntraCellBlockingGroupID6_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 8),
    _WorpIntraCellBlockingGroupID6_Type()
)
worpIntraCellBlockingGroupID6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID6.setStatus("current")


class _WorpIntraCellBlockingGroupID7_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID7 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID7_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID7_Object = MibTableColumn
worpIntraCellBlockingGroupID7 = _WorpIntraCellBlockingGroupID7_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 9),
    _WorpIntraCellBlockingGroupID7_Type()
)
worpIntraCellBlockingGroupID7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID7.setStatus("current")


class _WorpIntraCellBlockingGroupID8_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID8 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID8_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID8_Object = MibTableColumn
worpIntraCellBlockingGroupID8 = _WorpIntraCellBlockingGroupID8_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 10),
    _WorpIntraCellBlockingGroupID8_Type()
)
worpIntraCellBlockingGroupID8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID8.setStatus("current")


class _WorpIntraCellBlockingGroupID9_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID9 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID9_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID9_Object = MibTableColumn
worpIntraCellBlockingGroupID9 = _WorpIntraCellBlockingGroupID9_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 11),
    _WorpIntraCellBlockingGroupID9_Type()
)
worpIntraCellBlockingGroupID9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID9.setStatus("current")


class _WorpIntraCellBlockingGroupID10_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID10 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID10_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID10_Object = MibTableColumn
worpIntraCellBlockingGroupID10 = _WorpIntraCellBlockingGroupID10_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 12),
    _WorpIntraCellBlockingGroupID10_Type()
)
worpIntraCellBlockingGroupID10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID10.setStatus("current")


class _WorpIntraCellBlockingGroupID11_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID11 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID11_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID11_Object = MibTableColumn
worpIntraCellBlockingGroupID11 = _WorpIntraCellBlockingGroupID11_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 13),
    _WorpIntraCellBlockingGroupID11_Type()
)
worpIntraCellBlockingGroupID11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID11.setStatus("current")


class _WorpIntraCellBlockingGroupID12_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID12 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID12_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID12_Object = MibTableColumn
worpIntraCellBlockingGroupID12 = _WorpIntraCellBlockingGroupID12_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 14),
    _WorpIntraCellBlockingGroupID12_Type()
)
worpIntraCellBlockingGroupID12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID12.setStatus("current")


class _WorpIntraCellBlockingGroupID13_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID13 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID13_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID13_Object = MibTableColumn
worpIntraCellBlockingGroupID13 = _WorpIntraCellBlockingGroupID13_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 15),
    _WorpIntraCellBlockingGroupID13_Type()
)
worpIntraCellBlockingGroupID13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID13.setStatus("current")


class _WorpIntraCellBlockingGroupID14_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID14 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID14_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID14_Object = MibTableColumn
worpIntraCellBlockingGroupID14 = _WorpIntraCellBlockingGroupID14_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 16),
    _WorpIntraCellBlockingGroupID14_Type()
)
worpIntraCellBlockingGroupID14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID14.setStatus("current")


class _WorpIntraCellBlockingGroupID15_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID15 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID15_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID15_Object = MibTableColumn
worpIntraCellBlockingGroupID15 = _WorpIntraCellBlockingGroupID15_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 17),
    _WorpIntraCellBlockingGroupID15_Type()
)
worpIntraCellBlockingGroupID15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID15.setStatus("current")


class _WorpIntraCellBlockingGroupID16_Type(Integer32):
    """Custom type worpIntraCellBlockingGroupID16 based on Integer32"""
    defaultValue = 2

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


_WorpIntraCellBlockingGroupID16_Type.__name__ = "Integer32"
_WorpIntraCellBlockingGroupID16_Object = MibTableColumn
worpIntraCellBlockingGroupID16 = _WorpIntraCellBlockingGroupID16_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 18),
    _WorpIntraCellBlockingGroupID16_Type()
)
worpIntraCellBlockingGroupID16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupID16.setStatus("current")


class _WorpIntraCellBlockingMACTableEntryStatus_Type(RowStatus):
    """Custom type worpIntraCellBlockingMACTableEntryStatus based on RowStatus"""


_WorpIntraCellBlockingMACTableEntryStatus_Object = MibTableColumn
worpIntraCellBlockingMACTableEntryStatus = _WorpIntraCellBlockingMACTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 2, 1, 19),
    _WorpIntraCellBlockingMACTableEntryStatus_Type()
)
worpIntraCellBlockingMACTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingMACTableEntryStatus.setStatus("current")
_WorpIntraCellBlockingGroupTable_Object = MibTable
worpIntraCellBlockingGroupTable = _WorpIntraCellBlockingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 3)
)
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupTable.setStatus("current")
_WorpIntraCellBlockingGroupTableEntry_Object = MibTableRow
worpIntraCellBlockingGroupTableEntry = _WorpIntraCellBlockingGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 3, 1)
)
worpIntraCellBlockingGroupTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpIntraCellBlockingGroupTableIndex"),
)
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupTableEntry.setStatus("current")


class _WorpIntraCellBlockingGroupTableIndex_Type(Unsigned32):
    """Custom type worpIntraCellBlockingGroupTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WorpIntraCellBlockingGroupTableIndex_Type.__name__ = "Unsigned32"
_WorpIntraCellBlockingGroupTableIndex_Object = MibTableColumn
worpIntraCellBlockingGroupTableIndex = _WorpIntraCellBlockingGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 3, 1, 1),
    _WorpIntraCellBlockingGroupTableIndex_Type()
)
worpIntraCellBlockingGroupTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupTableIndex.setStatus("current")


class _WorpIntraCellBlockingGroupName_Type(DisplayString):
    """Custom type worpIntraCellBlockingGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WorpIntraCellBlockingGroupName_Type.__name__ = "DisplayString"
_WorpIntraCellBlockingGroupName_Object = MibTableColumn
worpIntraCellBlockingGroupName = _WorpIntraCellBlockingGroupName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 3, 1, 2),
    _WorpIntraCellBlockingGroupName_Type()
)
worpIntraCellBlockingGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupName.setStatus("current")


class _WorpIntraCellBlockingGroupTableEntryStatus_Type(RowStatus):
    """Custom type worpIntraCellBlockingGroupTableEntryStatus based on RowStatus"""


_WorpIntraCellBlockingGroupTableEntryStatus_Object = MibTableColumn
worpIntraCellBlockingGroupTableEntryStatus = _WorpIntraCellBlockingGroupTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 7, 3, 1, 3),
    _WorpIntraCellBlockingGroupTableEntryStatus_Type()
)
worpIntraCellBlockingGroupTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpIntraCellBlockingGroupTableEntryStatus.setStatus("current")
_SecurityGateway_ObjectIdentity = ObjectIdentity
securityGateway = _SecurityGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 8)
)


class _SecurityGatewayStatus_Type(Integer32):
    """Custom type securityGatewayStatus based on Integer32"""
    defaultValue = 2

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


_SecurityGatewayStatus_Type.__name__ = "Integer32"
_SecurityGatewayStatus_Object = MibScalar
securityGatewayStatus = _SecurityGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 8, 1),
    _SecurityGatewayStatus_Type()
)
securityGatewayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityGatewayStatus.setStatus("current")
_SecurityGatewayMacAddress_Type = MacAddress
_SecurityGatewayMacAddress_Object = MibScalar
securityGatewayMacAddress = _SecurityGatewayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 8, 2),
    _SecurityGatewayMacAddress_Type()
)
securityGatewayMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityGatewayMacAddress.setStatus("current")


class _StpFrameForwardStatus_Type(Integer32):
    """Custom type stpFrameForwardStatus based on Integer32"""
    defaultValue = 2

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


_StpFrameForwardStatus_Type.__name__ = "Integer32"
_StpFrameForwardStatus_Object = MibScalar
stpFrameForwardStatus = _StpFrameForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 9),
    _StpFrameForwardStatus_Type()
)
stpFrameForwardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpFrameForwardStatus.setStatus("current")
_StormThreshold_ObjectIdentity = ObjectIdentity
stormThreshold = _StormThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10)
)
_StormThresholdTable_Object = MibTable
stormThresholdTable = _StormThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    stormThresholdTable.setStatus("current")
_StormThresholdTableEntry_Object = MibTableRow
stormThresholdTableEntry = _StormThresholdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1, 1)
)
stormThresholdTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "stormThresholdTableIndex"),
)
if mibBuilder.loadTexts:
    stormThresholdTableEntry.setStatus("current")
_StormThresholdTableIndex_Type = Unsigned32
_StormThresholdTableIndex_Object = MibTableColumn
stormThresholdTableIndex = _StormThresholdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1, 1, 1),
    _StormThresholdTableIndex_Type()
)
stormThresholdTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormThresholdTableIndex.setStatus("current")


class _StormFilterInterface_Type(Integer32):
    """Custom type stormFilterInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("wireless", 2))
    )


_StormFilterInterface_Type.__name__ = "Integer32"
_StormFilterInterface_Object = MibTableColumn
stormFilterInterface = _StormFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1, 1, 2),
    _StormFilterInterface_Type()
)
stormFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormFilterInterface.setStatus("current")


class _StormMulticastThreshold_Type(Integer32):
    """Custom type stormMulticastThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_StormMulticastThreshold_Type.__name__ = "Integer32"
_StormMulticastThreshold_Object = MibTableColumn
stormMulticastThreshold = _StormMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1, 1, 3),
    _StormMulticastThreshold_Type()
)
stormMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormMulticastThreshold.setStatus("current")


class _StormBroadcastThreshold_Type(Integer32):
    """Custom type stormBroadcastThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_StormBroadcastThreshold_Type.__name__ = "Integer32"
_StormBroadcastThreshold_Object = MibTableColumn
stormBroadcastThreshold = _StormBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 6, 10, 1, 1, 4),
    _StormBroadcastThreshold_Type()
)
stormBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormBroadcastThreshold.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7)
)
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1)
)


class _DhcpServerStatus_Type(Integer32):
    """Custom type dhcpServerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcpRelayAgent", 3),
          ("dhcpServer", 2),
          ("disable", 1))
    )


_DhcpServerStatus_Type.__name__ = "Integer32"
_DhcpServerStatus_Object = MibScalar
dhcpServerStatus = _DhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 1),
    _DhcpServerStatus_Type()
)
dhcpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStatus.setStatus("current")


class _DhcpMaxLeaseTime_Type(TimeTicks):
    """Custom type dhcpMaxLeaseTime based on TimeTicks"""
    defaultValue = 8640000

    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360000, 17280000),
    )


_DhcpMaxLeaseTime_Type.__name__ = "TimeTicks"
_DhcpMaxLeaseTime_Object = MibScalar
dhcpMaxLeaseTime = _DhcpMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 2),
    _DhcpMaxLeaseTime_Type()
)
dhcpMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpMaxLeaseTime.setStatus("current")
_DhcpServerIfTable_Object = MibTable
dhcpServerIfTable = _DhcpServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    dhcpServerIfTable.setStatus("current")
_DhcpServerIfTableEntry_Object = MibTableRow
dhcpServerIfTableEntry = _DhcpServerIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1)
)
dhcpServerIfTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "dhcpServerIfTableIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerIfTableEntry.setStatus("current")


class _DhcpServerIfTableIndex_Type(Unsigned32):
    """Custom type dhcpServerIfTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpServerIfTableIndex_Type.__name__ = "Unsigned32"
_DhcpServerIfTableIndex_Object = MibTableColumn
dhcpServerIfTableIndex = _DhcpServerIfTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 1),
    _DhcpServerIfTableIndex_Type()
)
dhcpServerIfTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerIfTableIndex.setStatus("current")


class _DhcpServerInterfaceType_Type(Integer32):
    """Custom type dhcpServerInterfaceType based on Integer32"""
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
        *(("bridge", 1),
          ("ethernet1", 2),
          ("ethernet2", 3),
          ("wireless1", 4))
    )


_DhcpServerInterfaceType_Type.__name__ = "Integer32"
_DhcpServerInterfaceType_Object = MibTableColumn
dhcpServerInterfaceType = _DhcpServerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 2),
    _DhcpServerInterfaceType_Type()
)
dhcpServerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerInterfaceType.setStatus("current")
_DhcpServerNetMask_Type = IpAddress
_DhcpServerNetMask_Object = MibTableColumn
dhcpServerNetMask = _DhcpServerNetMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 3),
    _DhcpServerNetMask_Type()
)
dhcpServerNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerNetMask.setStatus("current")
_DhcpServerDefaultGateway_Type = IpAddress
_DhcpServerDefaultGateway_Object = MibTableColumn
dhcpServerDefaultGateway = _DhcpServerDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 4),
    _DhcpServerDefaultGateway_Type()
)
dhcpServerDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultGateway.setStatus("current")
_DhcpServerPrimaryDNS_Type = IpAddress
_DhcpServerPrimaryDNS_Object = MibTableColumn
dhcpServerPrimaryDNS = _DhcpServerPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 5),
    _DhcpServerPrimaryDNS_Type()
)
dhcpServerPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPrimaryDNS.setStatus("current")
_DhcpServerSecondaryDNS_Type = IpAddress
_DhcpServerSecondaryDNS_Object = MibTableColumn
dhcpServerSecondaryDNS = _DhcpServerSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 6),
    _DhcpServerSecondaryDNS_Type()
)
dhcpServerSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerSecondaryDNS.setStatus("current")


class _DhcpServerDefaultLeaseTime_Type(TimeTicks):
    """Custom type dhcpServerDefaultLeaseTime based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360000, 17280000),
    )


_DhcpServerDefaultLeaseTime_Type.__name__ = "TimeTicks"
_DhcpServerDefaultLeaseTime_Object = MibTableColumn
dhcpServerDefaultLeaseTime = _DhcpServerDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 7),
    _DhcpServerDefaultLeaseTime_Type()
)
dhcpServerDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultLeaseTime.setStatus("current")
_DhcpServerIfTableComment_Type = DisplayString
_DhcpServerIfTableComment_Object = MibTableColumn
dhcpServerIfTableComment = _DhcpServerIfTableComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 8),
    _DhcpServerIfTableComment_Type()
)
dhcpServerIfTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIfTableComment.setStatus("current")
_DhcpServerIfTableEntryStatus_Type = RowStatus
_DhcpServerIfTableEntryStatus_Object = MibTableColumn
dhcpServerIfTableEntryStatus = _DhcpServerIfTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 3, 1, 9),
    _DhcpServerIfTableEntryStatus_Type()
)
dhcpServerIfTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIfTableEntryStatus.setStatus("current")
_DhcpServerIpPoolTable_Object = MibTable
dhcpServerIpPoolTable = _DhcpServerIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    dhcpServerIpPoolTable.setStatus("current")
_DhcpServerIpPoolTableEntry_Object = MibTableRow
dhcpServerIpPoolTableEntry = _DhcpServerIpPoolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1)
)
dhcpServerIpPoolTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "dhcpServerIpPoolTableIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerIpPoolTableEntry.setStatus("current")


class _DhcpServerIpPoolTableIndex_Type(Unsigned32):
    """Custom type dhcpServerIpPoolTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpServerIpPoolTableIndex_Type.__name__ = "Unsigned32"
_DhcpServerIpPoolTableIndex_Object = MibTableColumn
dhcpServerIpPoolTableIndex = _DhcpServerIpPoolTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1, 1),
    _DhcpServerIpPoolTableIndex_Type()
)
dhcpServerIpPoolTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerIpPoolTableIndex.setStatus("current")


class _DhcpServerIpPoolInterface_Type(Integer32):
    """Custom type dhcpServerIpPoolInterface based on Integer32"""
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
        *(("bridge", 1),
          ("ethernet1", 2),
          ("ethernet2", 3),
          ("wireless1", 4))
    )


_DhcpServerIpPoolInterface_Type.__name__ = "Integer32"
_DhcpServerIpPoolInterface_Object = MibTableColumn
dhcpServerIpPoolInterface = _DhcpServerIpPoolInterface_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1, 2),
    _DhcpServerIpPoolInterface_Type()
)
dhcpServerIpPoolInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIpPoolInterface.setStatus("current")
_DhcpServerIpPoolStartIpAddress_Type = IpAddress
_DhcpServerIpPoolStartIpAddress_Object = MibTableColumn
dhcpServerIpPoolStartIpAddress = _DhcpServerIpPoolStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1, 3),
    _DhcpServerIpPoolStartIpAddress_Type()
)
dhcpServerIpPoolStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIpPoolStartIpAddress.setStatus("current")
_DhcpServerIpPoolEndIpAddress_Type = IpAddress
_DhcpServerIpPoolEndIpAddress_Object = MibTableColumn
dhcpServerIpPoolEndIpAddress = _DhcpServerIpPoolEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1, 4),
    _DhcpServerIpPoolEndIpAddress_Type()
)
dhcpServerIpPoolEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIpPoolEndIpAddress.setStatus("current")
_DhcpServerIpPoolTableEntryStatus_Type = RowStatus
_DhcpServerIpPoolTableEntryStatus_Object = MibTableColumn
dhcpServerIpPoolTableEntryStatus = _DhcpServerIpPoolTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 1, 4, 1, 5),
    _DhcpServerIpPoolTableEntryStatus_Type()
)
dhcpServerIpPoolTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIpPoolTableEntryStatus.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2)
)
_DhcpRelayServerTable_Object = MibTable
dhcpRelayServerTable = _DhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayServerTable.setStatus("current")
_DhcpRelayServerTableEntry_Object = MibTableRow
dhcpRelayServerTableEntry = _DhcpRelayServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2, 1, 1)
)
dhcpRelayServerTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "dhcpRelayServerTableIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerTableEntry.setStatus("current")
_DhcpRelayServerTableIndex_Type = Unsigned32
_DhcpRelayServerTableIndex_Object = MibTableColumn
dhcpRelayServerTableIndex = _DhcpRelayServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2, 1, 1, 1),
    _DhcpRelayServerTableIndex_Type()
)
dhcpRelayServerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerTableIndex.setStatus("current")
_DhcpRelayServerIpAddress_Type = IpAddress
_DhcpRelayServerIpAddress_Object = MibTableColumn
dhcpRelayServerIpAddress = _DhcpRelayServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2, 1, 1, 2),
    _DhcpRelayServerIpAddress_Type()
)
dhcpRelayServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerIpAddress.setStatus("current")
_DhcpRelayServerTableEntryStatus_Type = RowStatus
_DhcpRelayServerTableEntryStatus_Object = MibTableColumn
dhcpRelayServerTableEntryStatus = _DhcpRelayServerTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 7, 2, 1, 1, 3),
    _DhcpRelayServerTableEntryStatus_Type()
)
dhcpRelayServerTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerTableEntryStatus.setStatus("current")
_SysConf_ObjectIdentity = ObjectIdentity
sysConf = _SysConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8)
)
_SysTypeTable_Object = MibTable
sysTypeTable = _SysTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    sysTypeTable.setStatus("current")
_SysTypeTableEntry_Object = MibTableRow
sysTypeTableEntry = _SysTypeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1)
)
sysTypeTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "sysTypeRadioIfIndex"),
)
if mibBuilder.loadTexts:
    sysTypeTableEntry.setStatus("current")
_SysTypeRadioIfIndex_Type = Unsigned32
_SysTypeRadioIfIndex_Object = MibTableColumn
sysTypeRadioIfIndex = _SysTypeRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 1),
    _SysTypeRadioIfIndex_Type()
)
sysTypeRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTypeRadioIfIndex.setStatus("current")


class _SysTypeMode_Type(Unsigned32):
    """Custom type sysTypeMode based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysTypeMode_Type.__name__ = "Unsigned32"
_SysTypeMode_Object = MibTableColumn
sysTypeMode = _SysTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 2),
    _SysTypeMode_Type()
)
sysTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTypeMode.setStatus("current")


class _SysTypeActiveMode_Type(Unsigned32):
    """Custom type sysTypeActiveMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysTypeActiveMode_Type.__name__ = "Unsigned32"
_SysTypeActiveMode_Object = MibTableColumn
sysTypeActiveMode = _SysTypeActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 3),
    _SysTypeActiveMode_Type()
)
sysTypeActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTypeActiveMode.setStatus("current")
_SysTypeSupportedMode_Type = DisplayString
_SysTypeSupportedMode_Object = MibTableColumn
sysTypeSupportedMode = _SysTypeSupportedMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 4),
    _SysTypeSupportedMode_Type()
)
sysTypeSupportedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTypeSupportedMode.setStatus("current")
_SysTypeSupportedFreqDomains_Type = DisplayString
_SysTypeSupportedFreqDomains_Object = MibTableColumn
sysTypeSupportedFreqDomains = _SysTypeSupportedFreqDomains_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 5),
    _SysTypeSupportedFreqDomains_Type()
)
sysTypeSupportedFreqDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTypeSupportedFreqDomains.setStatus("current")


class _SysTypeFreqDomain_Type(Integer32):
    """Custom type sysTypeFreqDomain based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("australia5p4GHz", 26),
          ("australia5p8GHz", 27),
          ("brazil5p4GHz", 24),
          ("brazil5p8GHz", 25),
          ("canada5GHz", 9),
          ("canada5p8GHz", 16),
          ("europe2p4GHz", 12),
          ("europe5p4GHz", 11),
          ("europe5p8GHz", 10),
          ("india5p8GHz", 23),
          ("japan2p4", 18),
          ("japan4p9", 19),
          ("russia5GHz", 13),
          ("russiaFC", 17),
          ("taiwan5GHz", 14),
          ("uk5p8GHz", 20),
          ("unitedStates2p4", 3),
          ("unitedStates5GHz", 15),
          ("unitedStates5p3And5p8GHz", 22),
          ("unitedStatesAdhoc", 2),
          ("unitedStatesAll", 1),
          ("world2p3GHz", 7),
          ("world2p4GHz", 6),
          ("world2p5GHz", 8),
          ("world4p9GHz", 5),
          ("world5p9GHz", 21),
          ("worldAll", 4))
    )


_SysTypeFreqDomain_Type.__name__ = "Integer32"
_SysTypeFreqDomain_Object = MibTableColumn
sysTypeFreqDomain = _SysTypeFreqDomain_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 6),
    _SysTypeFreqDomain_Type()
)
sysTypeFreqDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTypeFreqDomain.setStatus("current")


class _SysTypeActiveFreqDomain_Type(Integer32):
    """Custom type sysTypeActiveFreqDomain based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("australia5p4GHz", 26),
          ("australia5p8GHz", 27),
          ("brazil5p4GHz", 24),
          ("brazil5p8GHz", 25),
          ("canada5GHz", 9),
          ("canada5p8GHz", 16),
          ("europe2p4GHz", 12),
          ("europe5p4GHz", 11),
          ("europe5p8GHz", 10),
          ("india5p8GHz", 23),
          ("japan2p4", 18),
          ("japan4p9", 19),
          ("russia5GHz", 13),
          ("russiaFC", 17),
          ("taiwan5GHz", 14),
          ("uk5p8GHz", 20),
          ("unitedStates2p4", 3),
          ("unitedStates5GHz", 15),
          ("unitedStates5p3And5p8GHz", 22),
          ("unitedStatesAdhoc", 2),
          ("unitedStatesAll", 1),
          ("world2p3GHz", 7),
          ("world2p4GHz", 6),
          ("world2p5GHz", 8),
          ("world4p9GHz", 5),
          ("world5p9GHz", 21),
          ("worldAll", 4))
    )


_SysTypeActiveFreqDomain_Type.__name__ = "Integer32"
_SysTypeActiveFreqDomain_Object = MibTableColumn
sysTypeActiveFreqDomain = _SysTypeActiveFreqDomain_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 1, 1, 7),
    _SysTypeActiveFreqDomain_Type()
)
sysTypeActiveFreqDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTypeActiveFreqDomain.setStatus("current")


class _SysNetworkMode_Type(Integer32):
    """Custom type sysNetworkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("route", 2))
    )


_SysNetworkMode_Type.__name__ = "Integer32"
_SysNetworkMode_Object = MibScalar
sysNetworkMode = _SysNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 2),
    _SysNetworkMode_Type()
)
sysNetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetworkMode.setStatus("current")


class _SysActiveNetworkMode_Type(Integer32):
    """Custom type sysActiveNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("route", 2))
    )


_SysActiveNetworkMode_Type.__name__ = "Integer32"
_SysActiveNetworkMode_Object = MibScalar
sysActiveNetworkMode = _SysActiveNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 3),
    _SysActiveNetworkMode_Type()
)
sysActiveNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysActiveNetworkMode.setStatus("current")


class _SysConfCountryCode_Type(DisplayString):
    """Custom type sysConfCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysConfCountryCode_Type.__name__ = "DisplayString"
_SysConfCountryCode_Object = MibScalar
sysConfCountryCode = _SysConfCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 8, 4),
    _SysConfCountryCode_Type()
)
sysConfCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfCountryCode.setStatus("current")
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 10)
)


class _IgmpSnoopingGlobalStatus_Type(Integer32):
    """Custom type igmpSnoopingGlobalStatus based on Integer32"""
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


_IgmpSnoopingGlobalStatus_Type.__name__ = "Integer32"
_IgmpSnoopingGlobalStatus_Object = MibScalar
igmpSnoopingGlobalStatus = _IgmpSnoopingGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 10, 1),
    _IgmpSnoopingGlobalStatus_Type()
)
igmpSnoopingGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingGlobalStatus.setStatus("current")
_IgmpMembershipAgingTimer_Type = Unsigned32
_IgmpMembershipAgingTimer_Object = MibScalar
igmpMembershipAgingTimer = _IgmpMembershipAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 10, 2),
    _IgmpMembershipAgingTimer_Type()
)
igmpMembershipAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMembershipAgingTimer.setStatus("current")
_IgmpRouterPortAgingTimer_Type = Unsigned32
_IgmpRouterPortAgingTimer_Object = MibScalar
igmpRouterPortAgingTimer = _IgmpRouterPortAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 10, 3),
    _IgmpRouterPortAgingTimer_Type()
)
igmpRouterPortAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpRouterPortAgingTimer.setStatus("current")


class _IgmpForcedFlood_Type(Integer32):
    """Custom type igmpForcedFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IgmpForcedFlood_Type.__name__ = "Integer32"
_IgmpForcedFlood_Object = MibScalar
igmpForcedFlood = _IgmpForcedFlood_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 1, 10, 4),
    _IgmpForcedFlood_Type()
)
igmpForcedFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpForcedFlood.setStatus("current")
_DeviceMgmt_ObjectIdentity = ObjectIdentity
deviceMgmt = _DeviceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1)
)


class _SysCountryCode_Type(DisplayString):
    """Custom type sysCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysCountryCode_Type.__name__ = "DisplayString"
_SysCountryCode_Object = MibScalar
sysCountryCode = _SysCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 1),
    _SysCountryCode_Type()
)
sysCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCountryCode.setStatus("deprecated")
_SysInvMgmt_ObjectIdentity = ObjectIdentity
sysInvMgmt = _SysInvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2)
)
_SysInvMgmtComponentTable_Object = MibTable
sysInvMgmtComponentTable = _SysInvMgmtComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysInvMgmtComponentTable.setStatus("current")
_SysInvMgmtComponentTableEntry_Object = MibTableRow
sysInvMgmtComponentTableEntry = _SysInvMgmtComponentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1)
)
sysInvMgmtComponentTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "sysInvMgmtCompTableIndex"),
)
if mibBuilder.loadTexts:
    sysInvMgmtComponentTableEntry.setStatus("current")
_SysInvMgmtCompTableIndex_Type = Unsigned32
_SysInvMgmtCompTableIndex_Object = MibTableColumn
sysInvMgmtCompTableIndex = _SysInvMgmtCompTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 1),
    _SysInvMgmtCompTableIndex_Type()
)
sysInvMgmtCompTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompTableIndex.setStatus("current")
_SysInvMgmtCompSerialNumber_Type = DisplayString
_SysInvMgmtCompSerialNumber_Object = MibTableColumn
sysInvMgmtCompSerialNumber = _SysInvMgmtCompSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 2),
    _SysInvMgmtCompSerialNumber_Type()
)
sysInvMgmtCompSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompSerialNumber.setStatus("current")
_SysInvMgmtCompName_Type = DisplayString
_SysInvMgmtCompName_Object = MibTableColumn
sysInvMgmtCompName = _SysInvMgmtCompName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 3),
    _SysInvMgmtCompName_Type()
)
sysInvMgmtCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompName.setStatus("current")
_SysInvMgmtCompId_Type = Unsigned32
_SysInvMgmtCompId_Object = MibTableColumn
sysInvMgmtCompId = _SysInvMgmtCompId_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 4),
    _SysInvMgmtCompId_Type()
)
sysInvMgmtCompId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompId.setStatus("current")
_SysInvMgmtCompVariant_Type = Unsigned32
_SysInvMgmtCompVariant_Object = MibTableColumn
sysInvMgmtCompVariant = _SysInvMgmtCompVariant_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 5),
    _SysInvMgmtCompVariant_Type()
)
sysInvMgmtCompVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompVariant.setStatus("current")
_SysInvMgmtCompReleaseVersion_Type = Unsigned32
_SysInvMgmtCompReleaseVersion_Object = MibTableColumn
sysInvMgmtCompReleaseVersion = _SysInvMgmtCompReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 6),
    _SysInvMgmtCompReleaseVersion_Type()
)
sysInvMgmtCompReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompReleaseVersion.setStatus("current")
_SysInvMgmtCompMajorVersion_Type = Unsigned32
_SysInvMgmtCompMajorVersion_Object = MibTableColumn
sysInvMgmtCompMajorVersion = _SysInvMgmtCompMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 7),
    _SysInvMgmtCompMajorVersion_Type()
)
sysInvMgmtCompMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompMajorVersion.setStatus("current")
_SysInvMgmtCompMinorVersion_Type = Unsigned32
_SysInvMgmtCompMinorVersion_Object = MibTableColumn
sysInvMgmtCompMinorVersion = _SysInvMgmtCompMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 1, 1, 8),
    _SysInvMgmtCompMinorVersion_Type()
)
sysInvMgmtCompMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtCompMinorVersion.setStatus("current")
_SysInvMgmtSecurityID_Type = DisplayString
_SysInvMgmtSecurityID_Object = MibScalar
sysInvMgmtSecurityID = _SysInvMgmtSecurityID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 2),
    _SysInvMgmtSecurityID_Type()
)
sysInvMgmtSecurityID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtSecurityID.setStatus("current")


class _SysInvMgmtDaughterCardAvailability_Type(Integer32):
    """Custom type sysInvMgmtDaughterCardAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SysInvMgmtDaughterCardAvailability_Type.__name__ = "Integer32"
_SysInvMgmtDaughterCardAvailability_Object = MibScalar
sysInvMgmtDaughterCardAvailability = _SysInvMgmtDaughterCardAvailability_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 2, 3),
    _SysInvMgmtDaughterCardAvailability_Type()
)
sysInvMgmtDaughterCardAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInvMgmtDaughterCardAvailability.setStatus("current")
_SysFeature_ObjectIdentity = ObjectIdentity
sysFeature = _SysFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3)
)
_SysFeatureCtrlID_Type = Unsigned32
_SysFeatureCtrlID_Object = MibScalar
sysFeatureCtrlID = _SysFeatureCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 1),
    _SysFeatureCtrlID_Type()
)
sysFeatureCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureCtrlID.setStatus("current")
_SysFeatureNumRadios_Type = Unsigned32
_SysFeatureNumRadios_Object = MibScalar
sysFeatureNumRadios = _SysFeatureNumRadios_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 2),
    _SysFeatureNumRadios_Type()
)
sysFeatureNumRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureNumRadios.setStatus("current")
_SysFeatureFreqBand_Type = DisplayString
_SysFeatureFreqBand_Object = MibScalar
sysFeatureFreqBand = _SysFeatureFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 3),
    _SysFeatureFreqBand_Type()
)
sysFeatureFreqBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureFreqBand.setStatus("current")
_SysFeatureOutBandwidth_Type = Unsigned32
_SysFeatureOutBandwidth_Object = MibScalar
sysFeatureOutBandwidth = _SysFeatureOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 4),
    _SysFeatureOutBandwidth_Type()
)
sysFeatureOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureOutBandwidth.setStatus("current")
_SysFeatureInBandwidth_Type = Unsigned32
_SysFeatureInBandwidth_Object = MibScalar
sysFeatureInBandwidth = _SysFeatureInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 5),
    _SysFeatureInBandwidth_Type()
)
sysFeatureInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureInBandwidth.setStatus("current")
_SysFeatureOpMode_Type = DisplayString
_SysFeatureOpMode_Object = MibScalar
sysFeatureOpMode = _SysFeatureOpMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 6),
    _SysFeatureOpMode_Type()
)
sysFeatureOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureOpMode.setStatus("current")
_SysLicFeatureTable_Object = MibTable
sysLicFeatureTable = _SysLicFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    sysLicFeatureTable.setStatus("current")
_SysLicFeatureTableEntry_Object = MibTableRow
sysLicFeatureTableEntry = _SysLicFeatureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 7, 1)
)
sysLicFeatureTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "sysLicFeatureTableIndex"),
)
if mibBuilder.loadTexts:
    sysLicFeatureTableEntry.setStatus("current")
_SysLicFeatureTableIndex_Type = Unsigned32
_SysLicFeatureTableIndex_Object = MibTableColumn
sysLicFeatureTableIndex = _SysLicFeatureTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 7, 1, 1),
    _SysLicFeatureTableIndex_Type()
)
sysLicFeatureTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicFeatureTableIndex.setStatus("current")
_SysLicFeatureType_Type = Unsigned32
_SysLicFeatureType_Object = MibTableColumn
sysLicFeatureType = _SysLicFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 7, 1, 2),
    _SysLicFeatureType_Type()
)
sysLicFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicFeatureType.setStatus("current")
_SysLicFeatureValue_Type = Unsigned32
_SysLicFeatureValue_Object = MibTableColumn
sysLicFeatureValue = _SysLicFeatureValue_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 7, 1, 3),
    _SysLicFeatureValue_Type()
)
sysLicFeatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicFeatureValue.setStatus("current")
_SysFeatureCumulativeBandwidth_Type = Unsigned32
_SysFeatureCumulativeBandwidth_Object = MibScalar
sysFeatureCumulativeBandwidth = _SysFeatureCumulativeBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 8),
    _SysFeatureCumulativeBandwidth_Type()
)
sysFeatureCumulativeBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureCumulativeBandwidth.setStatus("current")
_SysFeatureNumEtherIf_Type = Unsigned32
_SysFeatureNumEtherIf_Object = MibScalar
sysFeatureNumEtherIf = _SysFeatureNumEtherIf_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 9),
    _SysFeatureNumEtherIf_Type()
)
sysFeatureNumEtherIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureNumEtherIf.setStatus("current")
_SysFeatureBitmap_Type = Unsigned32
_SysFeatureBitmap_Object = MibScalar
sysFeatureBitmap = _SysFeatureBitmap_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 10),
    _SysFeatureBitmap_Type()
)
sysFeatureBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureBitmap.setStatus("current")
_SysFeatureNumOfSatellitesAllowed_Type = Unsigned32
_SysFeatureNumOfSatellitesAllowed_Object = MibScalar
sysFeatureNumOfSatellitesAllowed = _SysFeatureNumOfSatellitesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 11),
    _SysFeatureNumOfSatellitesAllowed_Type()
)
sysFeatureNumOfSatellitesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureNumOfSatellitesAllowed.setStatus("current")


class _SysFeatureProductFamily_Type(Integer32):
    """Custom type sysFeatureProductFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("orinocoAP", 2),
          ("tsunamiMP", 1),
          ("tsunamiQuickBridge", 3))
    )


_SysFeatureProductFamily_Type.__name__ = "Integer32"
_SysFeatureProductFamily_Object = MibScalar
sysFeatureProductFamily = _SysFeatureProductFamily_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 12),
    _SysFeatureProductFamily_Type()
)
sysFeatureProductFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureProductFamily.setStatus("current")


class _SysFeatureProductClass_Type(Integer32):
    """Custom type sysFeatureProductClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 0),
          ("outdoor", 1))
    )


_SysFeatureProductClass_Type.__name__ = "Integer32"
_SysFeatureProductClass_Object = MibScalar
sysFeatureProductClass = _SysFeatureProductClass_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 13),
    _SysFeatureProductClass_Type()
)
sysFeatureProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureProductClass.setStatus("current")
_SysLicRadioInfoTable_Object = MibTable
sysLicRadioInfoTable = _SysLicRadioInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14)
)
if mibBuilder.loadTexts:
    sysLicRadioInfoTable.setStatus("current")
_SysLicRadioInfoTableEntry_Object = MibTableRow
sysLicRadioInfoTableEntry = _SysLicRadioInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1)
)
sysLicRadioInfoTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "sysLicRadioInfoTableIndex"),
)
if mibBuilder.loadTexts:
    sysLicRadioInfoTableEntry.setStatus("current")
_SysLicRadioInfoTableIndex_Type = Unsigned32
_SysLicRadioInfoTableIndex_Object = MibTableColumn
sysLicRadioInfoTableIndex = _SysLicRadioInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1, 1),
    _SysLicRadioInfoTableIndex_Type()
)
sysLicRadioInfoTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicRadioInfoTableIndex.setStatus("current")
_SysLicRadioCompID_Type = Unsigned32
_SysLicRadioCompID_Object = MibTableColumn
sysLicRadioCompID = _SysLicRadioCompID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1, 2),
    _SysLicRadioCompID_Type()
)
sysLicRadioCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicRadioCompID.setStatus("current")
_SysLicRadiovariantID_Type = Unsigned32
_SysLicRadiovariantID_Object = MibTableColumn
sysLicRadiovariantID = _SysLicRadiovariantID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1, 3),
    _SysLicRadiovariantID_Type()
)
sysLicRadiovariantID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicRadiovariantID.setStatus("current")


class _SysLicRadioAntennaType_Type(Integer32):
    """Custom type sysLicRadioAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectorized", 1),
          ("integrated", 2),
          ("invalid", 0))
    )


_SysLicRadioAntennaType_Type.__name__ = "Integer32"
_SysLicRadioAntennaType_Object = MibTableColumn
sysLicRadioAntennaType = _SysLicRadioAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1, 4),
    _SysLicRadioAntennaType_Type()
)
sysLicRadioAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicRadioAntennaType.setStatus("current")


class _SysLicRadioAntennaMimoType_Type(Integer32):
    """Custom type sysLicRadioAntennaMimoType based on Integer32"""
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
        *(("invalid", 0),
          ("oneCrossOneAntenna", 1),
          ("threeCrossThreeAntenna", 3),
          ("twoCrossTwoAntenna", 2))
    )


_SysLicRadioAntennaMimoType_Type.__name__ = "Integer32"
_SysLicRadioAntennaMimoType_Object = MibTableColumn
sysLicRadioAntennaMimoType = _SysLicRadioAntennaMimoType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 3, 14, 1, 5),
    _SysLicRadioAntennaMimoType_Type()
)
sysLicRadioAntennaMimoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicRadioAntennaMimoType.setStatus("current")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4)
)
_SysMgmtCfgChangeCnt_Type = Counter32
_SysMgmtCfgChangeCnt_Object = MibScalar
sysMgmtCfgChangeCnt = _SysMgmtCfgChangeCnt_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 1),
    _SysMgmtCfgChangeCnt_Type()
)
sysMgmtCfgChangeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCfgChangeCnt.setStatus("current")
_SysMgmtCfgCommit_Type = Unsigned32
_SysMgmtCfgCommit_Object = MibScalar
sysMgmtCfgCommit = _SysMgmtCfgCommit_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 2),
    _SysMgmtCfgCommit_Type()
)
sysMgmtCfgCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCfgCommit.setStatus("current")


class _SysMgmtCfgRestore_Type(Integer32):
    """Custom type sysMgmtCfgRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SysMgmtCfgRestore_Type.__name__ = "Integer32"
_SysMgmtCfgRestore_Object = MibScalar
sysMgmtCfgRestore = _SysMgmtCfgRestore_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 3),
    _SysMgmtCfgRestore_Type()
)
sysMgmtCfgRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCfgRestore.setStatus("current")
_SysMgmtCfgErrorMsg_Type = DisplayString
_SysMgmtCfgErrorMsg_Object = MibScalar
sysMgmtCfgErrorMsg = _SysMgmtCfgErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 4),
    _SysMgmtCfgErrorMsg_Type()
)
sysMgmtCfgErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCfgErrorMsg.setStatus("current")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 5),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("current")


class _SysMgmtFactoryReset_Type(Integer32):
    """Custom type sysMgmtFactoryReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SysMgmtFactoryReset_Type.__name__ = "Integer32"
_SysMgmtFactoryReset_Object = MibScalar
sysMgmtFactoryReset = _SysMgmtFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 6),
    _SysMgmtFactoryReset_Type()
)
sysMgmtFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtFactoryReset.setStatus("current")


class _SysMgmtLoadTextConfig_Type(Integer32):
    """Custom type sysMgmtLoadTextConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SysMgmtLoadTextConfig_Type.__name__ = "Integer32"
_SysMgmtLoadTextConfig_Object = MibScalar
sysMgmtLoadTextConfig = _SysMgmtLoadTextConfig_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 4, 7),
    _SysMgmtLoadTextConfig_Type()
)
sysMgmtLoadTextConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtLoadTextConfig.setStatus("current")
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5)
)


class _SysContactEmail_Type(DisplayString):
    """Custom type sysContactEmail based on DisplayString"""
    defaultValue = OctetString("user@domain.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_SysContactEmail_Type.__name__ = "DisplayString"
_SysContactEmail_Object = MibScalar
sysContactEmail = _SysContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 1),
    _SysContactEmail_Type()
)
sysContactEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContactEmail.setStatus("current")


class _SysContactPhoneNumber_Type(DisplayString):
    """Custom type sysContactPhoneNumber based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_SysContactPhoneNumber_Type.__name__ = "DisplayString"
_SysContactPhoneNumber_Object = MibScalar
sysContactPhoneNumber = _SysContactPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 2),
    _SysContactPhoneNumber_Type()
)
sysContactPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContactPhoneNumber.setStatus("current")


class _SysLocationName_Type(DisplayString):
    """Custom type sysLocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocationName_Type.__name__ = "DisplayString"
_SysLocationName_Object = MibScalar
sysLocationName = _SysLocationName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 3),
    _SysLocationName_Type()
)
sysLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationName.setStatus("current")


class _SysGPSLongitude_Type(DisplayString):
    """Custom type sysGPSLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysGPSLongitude_Type.__name__ = "DisplayString"
_SysGPSLongitude_Object = MibScalar
sysGPSLongitude = _SysGPSLongitude_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 4),
    _SysGPSLongitude_Type()
)
sysGPSLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGPSLongitude.setStatus("current")


class _SysGPSLatitude_Type(DisplayString):
    """Custom type sysGPSLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysGPSLatitude_Type.__name__ = "DisplayString"
_SysGPSLatitude_Object = MibScalar
sysGPSLatitude = _SysGPSLatitude_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 5),
    _SysGPSLatitude_Type()
)
sysGPSLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGPSLatitude.setStatus("current")


class _SysGPSAltitude_Type(DisplayString):
    """Custom type sysGPSAltitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysGPSAltitude_Type.__name__ = "DisplayString"
_SysGPSAltitude_Object = MibScalar
sysGPSAltitude = _SysGPSAltitude_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 6),
    _SysGPSAltitude_Type()
)
sysGPSAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGPSAltitude.setStatus("current")
_ProductDescr_Type = DisplayString
_ProductDescr_Object = MibScalar
productDescr = _ProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 7),
    _ProductDescr_Type()
)
productDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDescr.setStatus("current")


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 1, 5, 8),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_MgmtSnmp_ObjectIdentity = ObjectIdentity
mgmtSnmp = _MgmtSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2)
)
_MgmtSnmpReadPassword_Type = Password
_MgmtSnmpReadPassword_Object = MibScalar
mgmtSnmpReadPassword = _MgmtSnmpReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 1),
    _MgmtSnmpReadPassword_Type()
)
mgmtSnmpReadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpReadPassword.setStatus("current")
_MgmtSnmpReadWritePassword_Type = Password
_MgmtSnmpReadWritePassword_Object = MibScalar
mgmtSnmpReadWritePassword = _MgmtSnmpReadWritePassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 2),
    _MgmtSnmpReadWritePassword_Type()
)
mgmtSnmpReadWritePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpReadWritePassword.setStatus("current")
_MgmtSnmpAccessTable_Object = MibTable
mgmtSnmpAccessTable = _MgmtSnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    mgmtSnmpAccessTable.setStatus("current")
_MgmtSnmpAccessTableEntry_Object = MibTableRow
mgmtSnmpAccessTableEntry = _MgmtSnmpAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 3, 1)
)
mgmtSnmpAccessTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "mgmtSnmpAccessTableIndex"),
)
if mibBuilder.loadTexts:
    mgmtSnmpAccessTableEntry.setStatus("current")


class _MgmtSnmpAccessTableIndex_Type(Unsigned32):
    """Custom type mgmtSnmpAccessTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MgmtSnmpAccessTableIndex_Type.__name__ = "Unsigned32"
_MgmtSnmpAccessTableIndex_Object = MibTableColumn
mgmtSnmpAccessTableIndex = _MgmtSnmpAccessTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 3, 1, 1),
    _MgmtSnmpAccessTableIndex_Type()
)
mgmtSnmpAccessTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtSnmpAccessTableIndex.setStatus("current")
_MgmtSnmpTrapHostTable_Object = MibTable
mgmtSnmpTrapHostTable = _MgmtSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTable.setStatus("current")
_MgmtSnmpTrapHostTableEntry_Object = MibTableRow
mgmtSnmpTrapHostTableEntry = _MgmtSnmpTrapHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1)
)
mgmtSnmpTrapHostTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "mgmtSnmpTrapHostTableIndex"),
)
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTableEntry.setStatus("current")


class _MgmtSnmpTrapHostTableIndex_Type(Unsigned32):
    """Custom type mgmtSnmpTrapHostTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MgmtSnmpTrapHostTableIndex_Type.__name__ = "Unsigned32"
_MgmtSnmpTrapHostTableIndex_Object = MibTableColumn
mgmtSnmpTrapHostTableIndex = _MgmtSnmpTrapHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1, 1),
    _MgmtSnmpTrapHostTableIndex_Type()
)
mgmtSnmpTrapHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTableIndex.setStatus("current")
_MgmtSnmpTrapHostTableIPAddress_Type = IpAddress
_MgmtSnmpTrapHostTableIPAddress_Object = MibTableColumn
mgmtSnmpTrapHostTableIPAddress = _MgmtSnmpTrapHostTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1, 2),
    _MgmtSnmpTrapHostTableIPAddress_Type()
)
mgmtSnmpTrapHostTableIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTableIPAddress.setStatus("current")
_MgmtSnmpTrapHostTablePassword_Type = Password
_MgmtSnmpTrapHostTablePassword_Object = MibTableColumn
mgmtSnmpTrapHostTablePassword = _MgmtSnmpTrapHostTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1, 3),
    _MgmtSnmpTrapHostTablePassword_Type()
)
mgmtSnmpTrapHostTablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTablePassword.setStatus("current")


class _MgmtSnmpTrapHostTableComment_Type(DisplayString):
    """Custom type mgmtSnmpTrapHostTableComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MgmtSnmpTrapHostTableComment_Type.__name__ = "DisplayString"
_MgmtSnmpTrapHostTableComment_Object = MibTableColumn
mgmtSnmpTrapHostTableComment = _MgmtSnmpTrapHostTableComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1, 4),
    _MgmtSnmpTrapHostTableComment_Type()
)
mgmtSnmpTrapHostTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTableComment.setStatus("current")
_MgmtSnmpTrapHostTableEntryStatus_Type = RowStatus
_MgmtSnmpTrapHostTableEntryStatus_Object = MibTableColumn
mgmtSnmpTrapHostTableEntryStatus = _MgmtSnmpTrapHostTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 4, 1, 5),
    _MgmtSnmpTrapHostTableEntryStatus_Type()
)
mgmtSnmpTrapHostTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpTrapHostTableEntryStatus.setStatus("current")


class _MgmtSnmpVersion_Type(Integer32):
    """Custom type mgmtSnmpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-v2c", 1),
          ("snmpv3", 2))
    )


_MgmtSnmpVersion_Type.__name__ = "Integer32"
_MgmtSnmpVersion_Object = MibScalar
mgmtSnmpVersion = _MgmtSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 5),
    _MgmtSnmpVersion_Type()
)
mgmtSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpVersion.setStatus("current")


class _MgmtSnmpV3SecurityLevel_Type(Integer32):
    """Custom type mgmtSnmpV3SecurityLevel based on Integer32"""
    defaultValue = 4

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
        *(("authNoPriv", 3),
          ("authPriv", 4),
          ("noAuthNoPriv", 2),
          ("none", 1))
    )


_MgmtSnmpV3SecurityLevel_Type.__name__ = "Integer32"
_MgmtSnmpV3SecurityLevel_Object = MibScalar
mgmtSnmpV3SecurityLevel = _MgmtSnmpV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 6),
    _MgmtSnmpV3SecurityLevel_Type()
)
mgmtSnmpV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpV3SecurityLevel.setStatus("current")


class _MgmtSnmpV3AuthProtocol_Type(Integer32):
    """Custom type mgmtSnmpV3AuthProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )


_MgmtSnmpV3AuthProtocol_Type.__name__ = "Integer32"
_MgmtSnmpV3AuthProtocol_Object = MibScalar
mgmtSnmpV3AuthProtocol = _MgmtSnmpV3AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 7),
    _MgmtSnmpV3AuthProtocol_Type()
)
mgmtSnmpV3AuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpV3AuthProtocol.setStatus("current")
_MgmtSnmpV3AuthPassword_Type = V3Password
_MgmtSnmpV3AuthPassword_Object = MibScalar
mgmtSnmpV3AuthPassword = _MgmtSnmpV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 8),
    _MgmtSnmpV3AuthPassword_Type()
)
mgmtSnmpV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpV3AuthPassword.setStatus("current")


class _MgmtSnmpV3PrivProtocol_Type(Integer32):
    """Custom type mgmtSnmpV3PrivProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes-128", 3),
          ("des", 2),
          ("none", 1))
    )


_MgmtSnmpV3PrivProtocol_Type.__name__ = "Integer32"
_MgmtSnmpV3PrivProtocol_Object = MibScalar
mgmtSnmpV3PrivProtocol = _MgmtSnmpV3PrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 9),
    _MgmtSnmpV3PrivProtocol_Type()
)
mgmtSnmpV3PrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpV3PrivProtocol.setStatus("current")
_MgmtSnmpV3PrivPassword_Type = V3Password
_MgmtSnmpV3PrivPassword_Object = MibScalar
mgmtSnmpV3PrivPassword = _MgmtSnmpV3PrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 2, 10),
    _MgmtSnmpV3PrivPassword_Type()
)
mgmtSnmpV3PrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtSnmpV3PrivPassword.setStatus("current")
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 3)
)


class _HttpPassword_Type(Password):
    """Custom type httpPassword based on Password"""
    defaultValue = OctetString("public")


_HttpPassword_Object = MibScalar
httpPassword = _HttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 3, 1),
    _HttpPassword_Type()
)
httpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPassword.setStatus("current")


class _HttpPort_Type(Unsigned32):
    """Custom type httpPort based on Unsigned32"""
    defaultValue = 80


_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 3, 2),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_Telnet_ObjectIdentity = ObjectIdentity
telnet = _Telnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 4)
)
_TelnetPassword_Type = Password
_TelnetPassword_Object = MibScalar
telnetPassword = _TelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 4, 1),
    _TelnetPassword_Type()
)
telnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPassword.setStatus("current")


class _TelnetPort_Type(Unsigned32):
    """Custom type telnetPort based on Unsigned32"""
    defaultValue = 23


_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 4, 2),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")
_TelnetSessions_Type = Unsigned32
_TelnetSessions_Object = MibScalar
telnetSessions = _TelnetSessions_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 4, 3),
    _TelnetSessions_Type()
)
telnetSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSessions.setStatus("current")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5)
)


class _TftpSrvIpAddress_Type(IpAddress):
    """Custom type tftpSrvIpAddress based on IpAddress"""
    defaultHexValue = "0a00000a"


_TftpSrvIpAddress_Object = MibScalar
tftpSrvIpAddress = _TftpSrvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5, 1),
    _TftpSrvIpAddress_Type()
)
tftpSrvIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSrvIpAddress.setStatus("current")


class _TftpFileName_Type(DisplayString):
    """Custom type tftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TftpFileName_Type.__name__ = "DisplayString"
_TftpFileName_Object = MibScalar
tftpFileName = _TftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5, 2),
    _TftpFileName_Type()
)
tftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileName.setStatus("current")


class _TftpFileType_Type(Integer32):
    """Custom type tftpFileType based on Integer32"""
    defaultValue = 2

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
        *(("config", 1),
          ("debuglog", 6),
          ("eventlog", 3),
          ("image", 2),
          ("templog", 4),
          ("textConfigFile", 5))
    )


_TftpFileType_Type.__name__ = "Integer32"
_TftpFileType_Object = MibScalar
tftpFileType = _TftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5, 3),
    _TftpFileType_Type()
)
tftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileType.setStatus("current")


class _TftpOpType_Type(Integer32):
    """Custom type tftpOpType based on Integer32"""
    defaultValue = 4

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
        *(("download", 2),
          ("downloadandReboot", 3),
          ("none", 4),
          ("upload", 1))
    )


_TftpOpType_Type.__name__ = "Integer32"
_TftpOpType_Object = MibScalar
tftpOpType = _TftpOpType_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5, 4),
    _TftpOpType_Type()
)
tftpOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpOpType.setStatus("current")


class _TftpOpStatus_Type(Integer32):
    """Custom type tftpOpStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailure", 4),
          ("downloadInProgress", 2),
          ("downloadSuccess", 3),
          ("idle", 1),
          ("signatureCheckFailed", 6),
          ("signatureCheckInProgress", 5),
          ("uploadFailure", 11),
          ("uploadInProgress", 9),
          ("uploadSuccess", 10),
          ("writeOnFlashFailed", 8),
          ("writeOnFlashInProgress", 7))
    )


_TftpOpStatus_Type.__name__ = "Integer32"
_TftpOpStatus_Object = MibScalar
tftpOpStatus = _TftpOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 5, 5),
    _TftpOpStatus_Type()
)
tftpOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpOpStatus.setStatus("current")
_TrapControl_ObjectIdentity = ObjectIdentity
trapControl = _TrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 6)
)
_GenericTrap_Type = DisplayString
_GenericTrap_Object = MibScalar
genericTrap = _GenericTrap_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 6, 1),
    _GenericTrap_Type()
)
genericTrap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericTrap.setStatus("current")


class _GlobalTrapStatus_Type(Integer32):
    """Custom type globalTrapStatus based on Integer32"""
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


_GlobalTrapStatus_Type.__name__ = "Integer32"
_GlobalTrapStatus_Object = MibScalar
globalTrapStatus = _GlobalTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 6, 2),
    _GlobalTrapStatus_Type()
)
globalTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalTrapStatus.setStatus("current")
_MgmtAccessControl_ObjectIdentity = ObjectIdentity
mgmtAccessControl = _MgmtAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7)
)


class _AllIntAccessControl_Type(Integer32):
    """Custom type allIntAccessControl based on Integer32"""
    defaultValue = 1

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


_AllIntAccessControl_Type.__name__ = "Integer32"
_AllIntAccessControl_Object = MibScalar
allIntAccessControl = _AllIntAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 1),
    _AllIntAccessControl_Type()
)
allIntAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allIntAccessControl.setStatus("current")


class _HttpAccessControl_Type(Integer32):
    """Custom type httpAccessControl based on Integer32"""
    defaultValue = 1

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


_HttpAccessControl_Type.__name__ = "Integer32"
_HttpAccessControl_Object = MibScalar
httpAccessControl = _HttpAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 2),
    _HttpAccessControl_Type()
)
httpAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAccessControl.setStatus("current")


class _HttpsAccessControl_Type(Integer32):
    """Custom type httpsAccessControl based on Integer32"""
    defaultValue = 1

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


_HttpsAccessControl_Type.__name__ = "Integer32"
_HttpsAccessControl_Object = MibScalar
httpsAccessControl = _HttpsAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 3),
    _HttpsAccessControl_Type()
)
httpsAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsAccessControl.setStatus("current")


class _SnmpAccessControl_Type(Integer32):
    """Custom type snmpAccessControl based on Integer32"""
    defaultValue = 1

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


_SnmpAccessControl_Type.__name__ = "Integer32"
_SnmpAccessControl_Object = MibScalar
snmpAccessControl = _SnmpAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 4),
    _SnmpAccessControl_Type()
)
snmpAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessControl.setStatus("current")


class _TelnetAccessControl_Type(Integer32):
    """Custom type telnetAccessControl based on Integer32"""
    defaultValue = 1

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


_TelnetAccessControl_Type.__name__ = "Integer32"
_TelnetAccessControl_Object = MibScalar
telnetAccessControl = _TelnetAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 5),
    _TelnetAccessControl_Type()
)
telnetAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAccessControl.setStatus("current")


class _SshAccessControl_Type(Integer32):
    """Custom type sshAccessControl based on Integer32"""
    defaultValue = 1

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


_SshAccessControl_Type.__name__ = "Integer32"
_SshAccessControl_Object = MibScalar
sshAccessControl = _SshAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 6),
    _SshAccessControl_Type()
)
sshAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessControl.setStatus("current")


class _MgmtAccessTableStatus_Type(Integer32):
    """Custom type mgmtAccessTableStatus based on Integer32"""
    defaultValue = 2

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


_MgmtAccessTableStatus_Type.__name__ = "Integer32"
_MgmtAccessTableStatus_Object = MibScalar
mgmtAccessTableStatus = _MgmtAccessTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 7),
    _MgmtAccessTableStatus_Type()
)
mgmtAccessTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtAccessTableStatus.setStatus("current")
_MgmtAccessTable_Object = MibTable
mgmtAccessTable = _MgmtAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 8)
)
if mibBuilder.loadTexts:
    mgmtAccessTable.setStatus("current")
_MgmtAccessTableEntry_Object = MibTableRow
mgmtAccessTableEntry = _MgmtAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 8, 1)
)
mgmtAccessTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "mgmtAccessTableIndex"),
)
if mibBuilder.loadTexts:
    mgmtAccessTableEntry.setStatus("current")
_MgmtAccessTableIndex_Type = Unsigned32
_MgmtAccessTableIndex_Object = MibTableColumn
mgmtAccessTableIndex = _MgmtAccessTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 8, 1, 1),
    _MgmtAccessTableIndex_Type()
)
mgmtAccessTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtAccessTableIndex.setStatus("current")
_MgmtAccessTableIpAddress_Type = IpAddress
_MgmtAccessTableIpAddress_Object = MibTableColumn
mgmtAccessTableIpAddress = _MgmtAccessTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 8, 1, 2),
    _MgmtAccessTableIpAddress_Type()
)
mgmtAccessTableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtAccessTableIpAddress.setStatus("current")
_MgmtAccessTableEntryStatus_Type = RowStatus
_MgmtAccessTableEntryStatus_Object = MibTableColumn
mgmtAccessTableEntryStatus = _MgmtAccessTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 7, 8, 1, 3),
    _MgmtAccessTableEntryStatus_Type()
)
mgmtAccessTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtAccessTableEntryStatus.setStatus("current")
_Ssh_ObjectIdentity = ObjectIdentity
ssh = _Ssh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 8)
)


class _SshPort_Type(Unsigned32):
    """Custom type sshPort based on Unsigned32"""
    defaultValue = 22


_SshPort_Object = MibScalar
sshPort = _SshPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 8, 1),
    _SshPort_Type()
)
sshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPort.setStatus("current")
_SshSessions_Type = Unsigned32
_SshSessions_Object = MibScalar
sshSessions = _SshSessions_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 2, 8, 2),
    _SshSessions_Type()
)
sshSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSessions.setStatus("current")
_DeviceMon_ObjectIdentity = ObjectIdentity
deviceMon = _DeviceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3)
)
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1)
)


class _SyslogStatus_Type(Integer32):
    """Custom type syslogStatus based on Integer32"""
    defaultValue = 1

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


_SyslogStatus_Type.__name__ = "Integer32"
_SyslogStatus_Object = MibScalar
syslogStatus = _SyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 1),
    _SyslogStatus_Type()
)
syslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStatus.setStatus("current")


class _SyslogPriority_Type(Integer32):
    """Custom type syslogPriority based on Integer32"""
    defaultValue = 5

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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_SyslogPriority_Type.__name__ = "Integer32"
_SyslogPriority_Object = MibScalar
syslogPriority = _SyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 2),
    _SyslogPriority_Type()
)
syslogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogPriority.setStatus("current")


class _SyslogReset_Type(Integer32):
    """Custom type syslogReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SyslogReset_Type.__name__ = "Integer32"
_SyslogReset_Object = MibScalar
syslogReset = _SyslogReset_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 3),
    _SyslogReset_Type()
)
syslogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogReset.setStatus("current")
_SyslogHostTable_Object = MibTable
syslogHostTable = _SyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    syslogHostTable.setStatus("current")
_SyslogHostTableEntry_Object = MibTableRow
syslogHostTableEntry = _SyslogHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1)
)
syslogHostTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "syslogHostTableIndex"),
)
if mibBuilder.loadTexts:
    syslogHostTableEntry.setStatus("current")
_SyslogHostTableIndex_Type = Unsigned32
_SyslogHostTableIndex_Object = MibTableColumn
syslogHostTableIndex = _SyslogHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1, 1),
    _SyslogHostTableIndex_Type()
)
syslogHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogHostTableIndex.setStatus("current")
_SyslogHostIpAddress_Type = IpAddress
_SyslogHostIpAddress_Object = MibTableColumn
syslogHostIpAddress = _SyslogHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1, 2),
    _SyslogHostIpAddress_Type()
)
syslogHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogHostIpAddress.setStatus("current")
_SyslogHostPort_Type = Unsigned32
_SyslogHostPort_Object = MibTableColumn
syslogHostPort = _SyslogHostPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1, 3),
    _SyslogHostPort_Type()
)
syslogHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogHostPort.setStatus("current")


class _SyslogHostComment_Type(DisplayString):
    """Custom type syslogHostComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SyslogHostComment_Type.__name__ = "DisplayString"
_SyslogHostComment_Object = MibTableColumn
syslogHostComment = _SyslogHostComment_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1, 4),
    _SyslogHostComment_Type()
)
syslogHostComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogHostComment.setStatus("current")
_SyslogHostTableEntryStatus_Type = RowStatus
_SyslogHostTableEntryStatus_Object = MibTableColumn
syslogHostTableEntryStatus = _SyslogHostTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 1, 4, 1, 5),
    _SyslogHostTableEntryStatus_Type()
)
syslogHostTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogHostTableEntryStatus.setStatus("current")
_Eventlog_ObjectIdentity = ObjectIdentity
eventlog = _Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 2)
)


class _EventLogPriority_Type(Integer32):
    """Custom type eventLogPriority based on Integer32"""
    defaultValue = 5

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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_EventLogPriority_Type.__name__ = "Integer32"
_EventLogPriority_Object = MibScalar
eventLogPriority = _EventLogPriority_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 2, 1),
    _EventLogPriority_Type()
)
eventLogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogPriority.setStatus("current")


class _EventLogReset_Type(Integer32):
    """Custom type eventLogReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EventLogReset_Type.__name__ = "Integer32"
_EventLogReset_Object = MibScalar
eventLogReset = _EventLogReset_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 2, 2),
    _EventLogReset_Type()
)
eventLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogReset.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3)
)


class _SntpStatus_Type(Integer32):
    """Custom type sntpStatus based on Integer32"""
    defaultValue = 2

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


_SntpStatus_Type.__name__ = "Integer32"
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpPrimaryServerName_Type(DisplayString):
    """Custom type sntpPrimaryServerName based on DisplayString"""
    defaultValue = OctetString("time.nist.gov")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SntpPrimaryServerName_Type.__name__ = "DisplayString"
_SntpPrimaryServerName_Object = MibScalar
sntpPrimaryServerName = _SntpPrimaryServerName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 2),
    _SntpPrimaryServerName_Type()
)
sntpPrimaryServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPrimaryServerName.setStatus("current")


class _SntpSecondaryServerName_Type(DisplayString):
    """Custom type sntpSecondaryServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SntpSecondaryServerName_Type.__name__ = "DisplayString"
_SntpSecondaryServerName_Object = MibScalar
sntpSecondaryServerName = _SntpSecondaryServerName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 3),
    _SntpSecondaryServerName_Type()
)
sntpSecondaryServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSecondaryServerName.setStatus("current")


class _SntpTimeZone_Type(Integer32):
    """Custom type sntpTimeZone based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("afghanistan", 26),
          ("alaska", 4),
          ("arabian", 25),
          ("arizona", 7),
          ("atlantic-canada", 12),
          ("australia-ct", 36),
          ("australia-et", 37),
          ("australia-wt", 32),
          ("azores", 18),
          ("bangkok", 31),
          ("bangladesh", 29),
          ("beijing", 34),
          ("brasilia", 15),
          ("buenos-aires", 16),
          ("burma", 30),
          ("cairo", 22),
          ("central-pacific", 38),
          ("central-us", 8),
          ("dateline", 1),
          ("eastern-europe", 21),
          ("eastern-us", 10),
          ("ewfoundland", 14),
          ("hawaii", 3),
          ("hong-kong", 33),
          ("india", 28),
          ("indiana", 11),
          ("iran", 24),
          ("japan-korea", 35),
          ("london", 19),
          ("mexico-city", 9),
          ("mid-atlantic", 17),
          ("mountain-us", 6),
          ("new-zealand", 39),
          ("pacific-us", 5),
          ("pakistan", 27),
          ("russia-iraq", 23),
          ("samoa", 2),
          ("santiago", 13),
          ("tonga", 40),
          ("western-europe", 20),
          ("western-samoa", 41))
    )


_SntpTimeZone_Type.__name__ = "Integer32"
_SntpTimeZone_Object = MibScalar
sntpTimeZone = _SntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 4),
    _SntpTimeZone_Type()
)
sntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeZone.setStatus("current")


class _SntpDayLightSavingTime_Type(Integer32):
    """Custom type sntpDayLightSavingTime based on Integer32"""
    defaultValue = 3

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
        *(("minus-one", 4),
          ("minus-two", 5),
          ("plus-one", 2),
          ("plus-two", 1),
          ("unchanged", 3))
    )


_SntpDayLightSavingTime_Type.__name__ = "Integer32"
_SntpDayLightSavingTime_Object = MibScalar
sntpDayLightSavingTime = _SntpDayLightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 5),
    _SntpDayLightSavingTime_Type()
)
sntpDayLightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDayLightSavingTime.setStatus("current")
_SntpShowCurrentTime_Type = DisplayString
_SntpShowCurrentTime_Object = MibScalar
sntpShowCurrentTime = _SntpShowCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 3, 6),
    _SntpShowCurrentTime_Type()
)
sntpShowCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpShowCurrentTime.setStatus("current")
_WirelessIfMon_ObjectIdentity = ObjectIdentity
wirelessIfMon = _WirelessIfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4)
)
_WirelessIfStaStats_ObjectIdentity = ObjectIdentity
wirelessIfStaStats = _WirelessIfStaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1)
)
_WirelessIfStaStatsTable_Object = MibTable
wirelessIfStaStatsTable = _WirelessIfStaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wirelessIfStaStatsTable.setStatus("current")
_WirelessIfStaStatsTableEntry_Object = MibTableRow
wirelessIfStaStatsTableEntry = _WirelessIfStaStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1)
)
wirelessIfStaStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfStaStatsTableIndex"),
    (0, "PROXIM-MIB", "wirelessIfStaStatsTableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfStaStatsTableEntry.setStatus("current")


class _WirelessIfStaStatsTableIndex_Type(Unsigned32):
    """Custom type wirelessIfStaStatsTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WirelessIfStaStatsTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfStaStatsTableIndex_Object = MibTableColumn
wirelessIfStaStatsTableIndex = _WirelessIfStaStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 1),
    _WirelessIfStaStatsTableIndex_Type()
)
wirelessIfStaStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTableIndex.setStatus("current")


class _WirelessIfStaStatsTableSecIndex_Type(Unsigned32):
    """Custom type wirelessIfStaStatsTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WirelessIfStaStatsTableSecIndex_Type.__name__ = "Unsigned32"
_WirelessIfStaStatsTableSecIndex_Object = MibTableColumn
wirelessIfStaStatsTableSecIndex = _WirelessIfStaStatsTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 2),
    _WirelessIfStaStatsTableSecIndex_Type()
)
wirelessIfStaStatsTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTableSecIndex.setStatus("current")


class _WirelessIfStaStatsIfNumber_Type(Unsigned32):
    """Custom type wirelessIfStaStatsIfNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIfStaStatsIfNumber_Type.__name__ = "Unsigned32"
_WirelessIfStaStatsIfNumber_Object = MibTableColumn
wirelessIfStaStatsIfNumber = _WirelessIfStaStatsIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 3),
    _WirelessIfStaStatsIfNumber_Type()
)
wirelessIfStaStatsIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsIfNumber.setStatus("current")


class _WirelessIfStaStatsVAPNumber_Type(Unsigned32):
    """Custom type wirelessIfStaStatsVAPNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WirelessIfStaStatsVAPNumber_Type.__name__ = "Unsigned32"
_WirelessIfStaStatsVAPNumber_Object = MibTableColumn
wirelessIfStaStatsVAPNumber = _WirelessIfStaStatsVAPNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 4),
    _WirelessIfStaStatsVAPNumber_Type()
)
wirelessIfStaStatsVAPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsVAPNumber.setStatus("current")
_WirelessIfStaStatsMACAddress_Type = MacAddress
_WirelessIfStaStatsMACAddress_Object = MibTableColumn
wirelessIfStaStatsMACAddress = _WirelessIfStaStatsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 5),
    _WirelessIfStaStatsMACAddress_Type()
)
wirelessIfStaStatsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsMACAddress.setStatus("current")
_WirelessIfStaStatsRxMgmtFrames_Type = Counter32
_WirelessIfStaStatsRxMgmtFrames_Object = MibTableColumn
wirelessIfStaStatsRxMgmtFrames = _WirelessIfStaStatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 6),
    _WirelessIfStaStatsRxMgmtFrames_Type()
)
wirelessIfStaStatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxMgmtFrames.setStatus("current")
_WirelessIfStaStatsRxControlFrames_Type = Counter32
_WirelessIfStaStatsRxControlFrames_Object = MibTableColumn
wirelessIfStaStatsRxControlFrames = _WirelessIfStaStatsRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 7),
    _WirelessIfStaStatsRxControlFrames_Type()
)
wirelessIfStaStatsRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxControlFrames.setStatus("current")
_WirelessIfStaStatsRxUnicastFrames_Type = Counter32
_WirelessIfStaStatsRxUnicastFrames_Object = MibTableColumn
wirelessIfStaStatsRxUnicastFrames = _WirelessIfStaStatsRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 8),
    _WirelessIfStaStatsRxUnicastFrames_Type()
)
wirelessIfStaStatsRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxUnicastFrames.setStatus("current")
_WirelessIfStaStatsRxMulticastFrames_Type = Counter32
_WirelessIfStaStatsRxMulticastFrames_Object = MibTableColumn
wirelessIfStaStatsRxMulticastFrames = _WirelessIfStaStatsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 9),
    _WirelessIfStaStatsRxMulticastFrames_Type()
)
wirelessIfStaStatsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxMulticastFrames.setStatus("current")
_WirelessIfStaStatsRxBytes_Type = Counter32
_WirelessIfStaStatsRxBytes_Object = MibTableColumn
wirelessIfStaStatsRxBytes = _WirelessIfStaStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 10),
    _WirelessIfStaStatsRxBytes_Type()
)
wirelessIfStaStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxBytes.setStatus("current")
_WirelessIfStaStatsRxBeacons_Type = Counter32
_WirelessIfStaStatsRxBeacons_Object = MibTableColumn
wirelessIfStaStatsRxBeacons = _WirelessIfStaStatsRxBeacons_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 11),
    _WirelessIfStaStatsRxBeacons_Type()
)
wirelessIfStaStatsRxBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxBeacons.setStatus("current")
_WirelessIfStaStatsRxProbeResp_Type = Counter32
_WirelessIfStaStatsRxProbeResp_Object = MibTableColumn
wirelessIfStaStatsRxProbeResp = _WirelessIfStaStatsRxProbeResp_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 12),
    _WirelessIfStaStatsRxProbeResp_Type()
)
wirelessIfStaStatsRxProbeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxProbeResp.setStatus("current")
_WirelessIfStaStatsRxDupFrames_Type = Counter32
_WirelessIfStaStatsRxDupFrames_Object = MibTableColumn
wirelessIfStaStatsRxDupFrames = _WirelessIfStaStatsRxDupFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 13),
    _WirelessIfStaStatsRxDupFrames_Type()
)
wirelessIfStaStatsRxDupFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDupFrames.setStatus("current")
_WirelessIfStaStatsRxNoPrivacy_Type = Counter32
_WirelessIfStaStatsRxNoPrivacy_Object = MibTableColumn
wirelessIfStaStatsRxNoPrivacy = _WirelessIfStaStatsRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 14),
    _WirelessIfStaStatsRxNoPrivacy_Type()
)
wirelessIfStaStatsRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxNoPrivacy.setStatus("current")
_WirelessIfStaStatsRxWepFail_Type = Counter32
_WirelessIfStaStatsRxWepFail_Object = MibTableColumn
wirelessIfStaStatsRxWepFail = _WirelessIfStaStatsRxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 15),
    _WirelessIfStaStatsRxWepFail_Type()
)
wirelessIfStaStatsRxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxWepFail.setStatus("current")
_WirelessIfStaStatsRxDeMicFail_Type = Counter32
_WirelessIfStaStatsRxDeMicFail_Object = MibTableColumn
wirelessIfStaStatsRxDeMicFail = _WirelessIfStaStatsRxDeMicFail_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 16),
    _WirelessIfStaStatsRxDeMicFail_Type()
)
wirelessIfStaStatsRxDeMicFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDeMicFail.setStatus("current")
_WirelessIfStaStatsRxDecapFailed_Type = Counter32
_WirelessIfStaStatsRxDecapFailed_Object = MibTableColumn
wirelessIfStaStatsRxDecapFailed = _WirelessIfStaStatsRxDecapFailed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 17),
    _WirelessIfStaStatsRxDecapFailed_Type()
)
wirelessIfStaStatsRxDecapFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDecapFailed.setStatus("current")
_WirelessIfStaStatsRxDefragFailed_Type = Counter32
_WirelessIfStaStatsRxDefragFailed_Object = MibTableColumn
wirelessIfStaStatsRxDefragFailed = _WirelessIfStaStatsRxDefragFailed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 18),
    _WirelessIfStaStatsRxDefragFailed_Type()
)
wirelessIfStaStatsRxDefragFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDefragFailed.setStatus("current")
_WirelessIfStaStatsRxDisassociationFrames_Type = Counter32
_WirelessIfStaStatsRxDisassociationFrames_Object = MibTableColumn
wirelessIfStaStatsRxDisassociationFrames = _WirelessIfStaStatsRxDisassociationFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 19),
    _WirelessIfStaStatsRxDisassociationFrames_Type()
)
wirelessIfStaStatsRxDisassociationFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDisassociationFrames.setStatus("current")
_WirelessIfStaStatsRxDeauthenticationFrames_Type = Counter32
_WirelessIfStaStatsRxDeauthenticationFrames_Object = MibTableColumn
wirelessIfStaStatsRxDeauthenticationFrames = _WirelessIfStaStatsRxDeauthenticationFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 20),
    _WirelessIfStaStatsRxDeauthenticationFrames_Type()
)
wirelessIfStaStatsRxDeauthenticationFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDeauthenticationFrames.setStatus("current")
_WirelessIfStaStatsRxDecryptFailedOnCRC_Type = Counter32
_WirelessIfStaStatsRxDecryptFailedOnCRC_Object = MibTableColumn
wirelessIfStaStatsRxDecryptFailedOnCRC = _WirelessIfStaStatsRxDecryptFailedOnCRC_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 21),
    _WirelessIfStaStatsRxDecryptFailedOnCRC_Type()
)
wirelessIfStaStatsRxDecryptFailedOnCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxDecryptFailedOnCRC.setStatus("current")
_WirelessIfStaStatsRxUnauthPort_Type = Counter32
_WirelessIfStaStatsRxUnauthPort_Object = MibTableColumn
wirelessIfStaStatsRxUnauthPort = _WirelessIfStaStatsRxUnauthPort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 22),
    _WirelessIfStaStatsRxUnauthPort_Type()
)
wirelessIfStaStatsRxUnauthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxUnauthPort.setStatus("current")
_WirelessIfStaStatsRxUnencrypted_Type = Counter32
_WirelessIfStaStatsRxUnencrypted_Object = MibTableColumn
wirelessIfStaStatsRxUnencrypted = _WirelessIfStaStatsRxUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 23),
    _WirelessIfStaStatsRxUnencrypted_Type()
)
wirelessIfStaStatsRxUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRxUnencrypted.setStatus("current")
_WirelessIfStaStatsTxDataFrames_Type = Counter32
_WirelessIfStaStatsTxDataFrames_Object = MibTableColumn
wirelessIfStaStatsTxDataFrames = _WirelessIfStaStatsTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 24),
    _WirelessIfStaStatsTxDataFrames_Type()
)
wirelessIfStaStatsTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxDataFrames.setStatus("current")
_WirelessIfStaStatsTxMgmtFrames_Type = Counter32
_WirelessIfStaStatsTxMgmtFrames_Object = MibTableColumn
wirelessIfStaStatsTxMgmtFrames = _WirelessIfStaStatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 25),
    _WirelessIfStaStatsTxMgmtFrames_Type()
)
wirelessIfStaStatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxMgmtFrames.setStatus("current")
_WirelessIfStaStatsTxUnicastFrames_Type = Counter32
_WirelessIfStaStatsTxUnicastFrames_Object = MibTableColumn
wirelessIfStaStatsTxUnicastFrames = _WirelessIfStaStatsTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 26),
    _WirelessIfStaStatsTxUnicastFrames_Type()
)
wirelessIfStaStatsTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxUnicastFrames.setStatus("current")
_WirelessIfStaStatsTxMulticastFrames_Type = Counter32
_WirelessIfStaStatsTxMulticastFrames_Object = MibTableColumn
wirelessIfStaStatsTxMulticastFrames = _WirelessIfStaStatsTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 27),
    _WirelessIfStaStatsTxMulticastFrames_Type()
)
wirelessIfStaStatsTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxMulticastFrames.setStatus("current")
_WirelessIfStaStatsTxBytes_Type = Counter32
_WirelessIfStaStatsTxBytes_Object = MibTableColumn
wirelessIfStaStatsTxBytes = _WirelessIfStaStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 28),
    _WirelessIfStaStatsTxBytes_Type()
)
wirelessIfStaStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxBytes.setStatus("current")
_WirelessIfStaStatsTxProbeReq_Type = Counter32
_WirelessIfStaStatsTxProbeReq_Object = MibTableColumn
wirelessIfStaStatsTxProbeReq = _WirelessIfStaStatsTxProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 29),
    _WirelessIfStaStatsTxProbeReq_Type()
)
wirelessIfStaStatsTxProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxProbeReq.setStatus("current")
_WirelessIfStaStatsTxEospLost_Type = Counter32
_WirelessIfStaStatsTxEospLost_Object = MibTableColumn
wirelessIfStaStatsTxEospLost = _WirelessIfStaStatsTxEospLost_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 30),
    _WirelessIfStaStatsTxEospLost_Type()
)
wirelessIfStaStatsTxEospLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxEospLost.setStatus("current")
_WirelessIfStaStatsTxPSDiscard_Type = Counter32
_WirelessIfStaStatsTxPSDiscard_Object = MibTableColumn
wirelessIfStaStatsTxPSDiscard = _WirelessIfStaStatsTxPSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 31),
    _WirelessIfStaStatsTxPSDiscard_Type()
)
wirelessIfStaStatsTxPSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxPSDiscard.setStatus("current")
_WirelessIfStaStatsTxAssociationFrames_Type = Counter32
_WirelessIfStaStatsTxAssociationFrames_Object = MibTableColumn
wirelessIfStaStatsTxAssociationFrames = _WirelessIfStaStatsTxAssociationFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 32),
    _WirelessIfStaStatsTxAssociationFrames_Type()
)
wirelessIfStaStatsTxAssociationFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxAssociationFrames.setStatus("current")
_WirelessIfStaStatsTxAssociationFailedFrames_Type = Counter32
_WirelessIfStaStatsTxAssociationFailedFrames_Object = MibTableColumn
wirelessIfStaStatsTxAssociationFailedFrames = _WirelessIfStaStatsTxAssociationFailedFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 33),
    _WirelessIfStaStatsTxAssociationFailedFrames_Type()
)
wirelessIfStaStatsTxAssociationFailedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxAssociationFailedFrames.setStatus("current")
_WirelessIfStaStatsTxAuthenticationFrames_Type = Counter32
_WirelessIfStaStatsTxAuthenticationFrames_Object = MibTableColumn
wirelessIfStaStatsTxAuthenticationFrames = _WirelessIfStaStatsTxAuthenticationFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 34),
    _WirelessIfStaStatsTxAuthenticationFrames_Type()
)
wirelessIfStaStatsTxAuthenticationFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxAuthenticationFrames.setStatus("current")
_WirelessIfStaStatsTxAuthenticationFailed_Type = Counter32
_WirelessIfStaStatsTxAuthenticationFailed_Object = MibTableColumn
wirelessIfStaStatsTxAuthenticationFailed = _WirelessIfStaStatsTxAuthenticationFailed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 35),
    _WirelessIfStaStatsTxAuthenticationFailed_Type()
)
wirelessIfStaStatsTxAuthenticationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxAuthenticationFailed.setStatus("current")
_WirelessIfStaStatsTxDeAuthFrames_Type = Counter32
_WirelessIfStaStatsTxDeAuthFrames_Object = MibTableColumn
wirelessIfStaStatsTxDeAuthFrames = _WirelessIfStaStatsTxDeAuthFrames_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 36),
    _WirelessIfStaStatsTxDeAuthFrames_Type()
)
wirelessIfStaStatsTxDeAuthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxDeAuthFrames.setStatus("current")
_WirelessIfStaStatsTxDeAuthCode_Type = Counter32
_WirelessIfStaStatsTxDeAuthCode_Object = MibTableColumn
wirelessIfStaStatsTxDeAuthCode = _WirelessIfStaStatsTxDeAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 37),
    _WirelessIfStaStatsTxDeAuthCode_Type()
)
wirelessIfStaStatsTxDeAuthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxDeAuthCode.setStatus("current")
_WirelessIfStaStatsTxDisassociation_Type = Counter32
_WirelessIfStaStatsTxDisassociation_Object = MibTableColumn
wirelessIfStaStatsTxDisassociation = _WirelessIfStaStatsTxDisassociation_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 38),
    _WirelessIfStaStatsTxDisassociation_Type()
)
wirelessIfStaStatsTxDisassociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxDisassociation.setStatus("current")
_WirelessIfStaStatsTxDisassociationCode_Type = Unsigned32
_WirelessIfStaStatsTxDisassociationCode_Object = MibTableColumn
wirelessIfStaStatsTxDisassociationCode = _WirelessIfStaStatsTxDisassociationCode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 39),
    _WirelessIfStaStatsTxDisassociationCode_Type()
)
wirelessIfStaStatsTxDisassociationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxDisassociationCode.setStatus("current")
_WirelessIfStaStatsFrequency_Type = Unsigned32
_WirelessIfStaStatsFrequency_Object = MibTableColumn
wirelessIfStaStatsFrequency = _WirelessIfStaStatsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 40),
    _WirelessIfStaStatsFrequency_Type()
)
wirelessIfStaStatsFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsFrequency.setStatus("current")
_WirelessIfStaStatsState_Type = Unsigned32
_WirelessIfStaStatsState_Object = MibTableColumn
wirelessIfStaStatsState = _WirelessIfStaStatsState_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 41),
    _WirelessIfStaStatsState_Type()
)
wirelessIfStaStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsState.setStatus("current")
_WirelessIfStaStatsRSSI_Type = Unsigned32
_WirelessIfStaStatsRSSI_Object = MibTableColumn
wirelessIfStaStatsRSSI = _WirelessIfStaStatsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 42),
    _WirelessIfStaStatsRSSI_Type()
)
wirelessIfStaStatsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsRSSI.setStatus("current")
_WirelessIfStaStatsTxRate_Type = Unsigned32
_WirelessIfStaStatsTxRate_Object = MibTableColumn
wirelessIfStaStatsTxRate = _WirelessIfStaStatsTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 43),
    _WirelessIfStaStatsTxRate_Type()
)
wirelessIfStaStatsTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxRate.setStatus("current")
_WirelessIfStaStatsAuthenAlgorithm_Type = Unsigned32
_WirelessIfStaStatsAuthenAlgorithm_Object = MibTableColumn
wirelessIfStaStatsAuthenAlgorithm = _WirelessIfStaStatsAuthenAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 44),
    _WirelessIfStaStatsAuthenAlgorithm_Type()
)
wirelessIfStaStatsAuthenAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsAuthenAlgorithm.setStatus("current")
_WirelessIfStaStatsAssociationID_Type = Unsigned32
_WirelessIfStaStatsAssociationID_Object = MibTableColumn
wirelessIfStaStatsAssociationID = _WirelessIfStaStatsAssociationID_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 45),
    _WirelessIfStaStatsAssociationID_Type()
)
wirelessIfStaStatsAssociationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsAssociationID.setStatus("current")
_WirelessIfStaStatsVlanTag_Type = Unsigned32
_WirelessIfStaStatsVlanTag_Object = MibTableColumn
wirelessIfStaStatsVlanTag = _WirelessIfStaStatsVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 46),
    _WirelessIfStaStatsVlanTag_Type()
)
wirelessIfStaStatsVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsVlanTag.setStatus("current")
_WirelessIfStaStatsAssocationTime_Type = Unsigned32
_WirelessIfStaStatsAssocationTime_Object = MibTableColumn
wirelessIfStaStatsAssocationTime = _WirelessIfStaStatsAssocationTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 47),
    _WirelessIfStaStatsAssocationTime_Type()
)
wirelessIfStaStatsAssocationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsAssocationTime.setStatus("current")
_WirelessIfStaStatsTxPower_Type = Unsigned32
_WirelessIfStaStatsTxPower_Object = MibTableColumn
wirelessIfStaStatsTxPower = _WirelessIfStaStatsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 48),
    _WirelessIfStaStatsTxPower_Type()
)
wirelessIfStaStatsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsTxPower.setStatus("current")
_WirelessIfStaStatsInactivityTimer_Type = Unsigned32
_WirelessIfStaStatsInactivityTimer_Object = MibTableColumn
wirelessIfStaStatsInactivityTimer = _WirelessIfStaStatsInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 49),
    _WirelessIfStaStatsInactivityTimer_Type()
)
wirelessIfStaStatsInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsInactivityTimer.setStatus("current")
_WirelessIfStaStatsStationOperatingMode_Type = Unsigned32
_WirelessIfStaStatsStationOperatingMode_Object = MibTableColumn
wirelessIfStaStatsStationOperatingMode = _WirelessIfStaStatsStationOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 50),
    _WirelessIfStaStatsStationOperatingMode_Type()
)
wirelessIfStaStatsStationOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsStationOperatingMode.setStatus("current")
_WirelessIfStaStatsHTCapability_Type = Unsigned32
_WirelessIfStaStatsHTCapability_Object = MibTableColumn
wirelessIfStaStatsHTCapability = _WirelessIfStaStatsHTCapability_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 1, 1, 51),
    _WirelessIfStaStatsHTCapability_Type()
)
wirelessIfStaStatsHTCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStaStatsHTCapability.setStatus("current")
_WirelessIfWORPStaStatsTable_Object = MibTable
wirelessIfWORPStaStatsTable = _WirelessIfWORPStaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsTable.setStatus("current")
_WirelessIfWORPStaStatsTableEntry_Object = MibTableRow
wirelessIfWORPStaStatsTableEntry = _WirelessIfWORPStaStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1)
)
wirelessIfWORPStaStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfWORPStaStatsTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsTableEntry.setStatus("current")
_WirelessIfWORPStaStatsTableIndex_Type = Unsigned32
_WirelessIfWORPStaStatsTableIndex_Object = MibTableColumn
wirelessIfWORPStaStatsTableIndex = _WirelessIfWORPStaStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 1),
    _WirelessIfWORPStaStatsTableIndex_Type()
)
wirelessIfWORPStaStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsTableIndex.setStatus("current")
_WirelessIfWORPStaStatsMacAddress_Type = MacAddress
_WirelessIfWORPStaStatsMacAddress_Object = MibTableColumn
wirelessIfWORPStaStatsMacAddress = _WirelessIfWORPStaStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 2),
    _WirelessIfWORPStaStatsMacAddress_Type()
)
wirelessIfWORPStaStatsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsMacAddress.setStatus("current")
_WirelessIfWORPStaStatsSatelliteName_Type = DisplayString
_WirelessIfWORPStaStatsSatelliteName_Object = MibTableColumn
wirelessIfWORPStaStatsSatelliteName = _WirelessIfWORPStaStatsSatelliteName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 3),
    _WirelessIfWORPStaStatsSatelliteName_Type()
)
wirelessIfWORPStaStatsSatelliteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsSatelliteName.setStatus("current")


class _WirelessIfWORPStaStatsAverageLocalSignal_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsAverageLocalSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStaStatsAverageLocalSignal_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsAverageLocalSignal_Object = MibTableColumn
wirelessIfWORPStaStatsAverageLocalSignal = _WirelessIfWORPStaStatsAverageLocalSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 4),
    _WirelessIfWORPStaStatsAverageLocalSignal_Type()
)
wirelessIfWORPStaStatsAverageLocalSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageLocalSignal.setStatus("current")


class _WirelessIfWORPStaStatsAverageLocalNoise_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsAverageLocalNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStaStatsAverageLocalNoise_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsAverageLocalNoise_Object = MibTableColumn
wirelessIfWORPStaStatsAverageLocalNoise = _WirelessIfWORPStaStatsAverageLocalNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 5),
    _WirelessIfWORPStaStatsAverageLocalNoise_Type()
)
wirelessIfWORPStaStatsAverageLocalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageLocalNoise.setStatus("current")


class _WirelessIfWORPStaStatsAverageRemoteSignal_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsAverageRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStaStatsAverageRemoteSignal_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsAverageRemoteSignal_Object = MibTableColumn
wirelessIfWORPStaStatsAverageRemoteSignal = _WirelessIfWORPStaStatsAverageRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 6),
    _WirelessIfWORPStaStatsAverageRemoteSignal_Type()
)
wirelessIfWORPStaStatsAverageRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageRemoteSignal.setStatus("current")


class _WirelessIfWORPStaStatsAverageRemoteNoise_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsAverageRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStaStatsAverageRemoteNoise_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsAverageRemoteNoise_Object = MibTableColumn
wirelessIfWORPStaStatsAverageRemoteNoise = _WirelessIfWORPStaStatsAverageRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 7),
    _WirelessIfWORPStaStatsAverageRemoteNoise_Type()
)
wirelessIfWORPStaStatsAverageRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageRemoteNoise.setStatus("current")
_WirelessIfWORPStaStatsRequestForService_Type = Counter32
_WirelessIfWORPStaStatsRequestForService_Object = MibTableColumn
wirelessIfWORPStaStatsRequestForService = _WirelessIfWORPStaStatsRequestForService_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 8),
    _WirelessIfWORPStaStatsRequestForService_Type()
)
wirelessIfWORPStaStatsRequestForService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRequestForService.setStatus("current")
_WirelessIfWORPStaStatsPollData_Type = Counter32
_WirelessIfWORPStaStatsPollData_Object = MibTableColumn
wirelessIfWORPStaStatsPollData = _WirelessIfWORPStaStatsPollData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 9),
    _WirelessIfWORPStaStatsPollData_Type()
)
wirelessIfWORPStaStatsPollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsPollData.setStatus("current")
_WirelessIfWORPStaStatsPollNoData_Type = Counter32
_WirelessIfWORPStaStatsPollNoData_Object = MibTableColumn
wirelessIfWORPStaStatsPollNoData = _WirelessIfWORPStaStatsPollNoData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 10),
    _WirelessIfWORPStaStatsPollNoData_Type()
)
wirelessIfWORPStaStatsPollNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsPollNoData.setStatus("current")
_WirelessIfWORPStaStatsReplyData_Type = Counter32
_WirelessIfWORPStaStatsReplyData_Object = MibTableColumn
wirelessIfWORPStaStatsReplyData = _WirelessIfWORPStaStatsReplyData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 11),
    _WirelessIfWORPStaStatsReplyData_Type()
)
wirelessIfWORPStaStatsReplyData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsReplyData.setStatus("current")
_WirelessIfWORPStaStatsReplyNoData_Type = Counter32
_WirelessIfWORPStaStatsReplyNoData_Object = MibTableColumn
wirelessIfWORPStaStatsReplyNoData = _WirelessIfWORPStaStatsReplyNoData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 12),
    _WirelessIfWORPStaStatsReplyNoData_Type()
)
wirelessIfWORPStaStatsReplyNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsReplyNoData.setStatus("current")
_WirelessIfWORPStaStatsSendSuccess_Type = Counter32
_WirelessIfWORPStaStatsSendSuccess_Object = MibTableColumn
wirelessIfWORPStaStatsSendSuccess = _WirelessIfWORPStaStatsSendSuccess_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 13),
    _WirelessIfWORPStaStatsSendSuccess_Type()
)
wirelessIfWORPStaStatsSendSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsSendSuccess.setStatus("current")
_WirelessIfWORPStaStatsSendRetries_Type = Counter32
_WirelessIfWORPStaStatsSendRetries_Object = MibTableColumn
wirelessIfWORPStaStatsSendRetries = _WirelessIfWORPStaStatsSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 14),
    _WirelessIfWORPStaStatsSendRetries_Type()
)
wirelessIfWORPStaStatsSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsSendRetries.setStatus("current")
_WirelessIfWORPStaStatsSendFailures_Type = Counter32
_WirelessIfWORPStaStatsSendFailures_Object = MibTableColumn
wirelessIfWORPStaStatsSendFailures = _WirelessIfWORPStaStatsSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 15),
    _WirelessIfWORPStaStatsSendFailures_Type()
)
wirelessIfWORPStaStatsSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsSendFailures.setStatus("current")
_WirelessIfWORPStaStatsReceiveSuccess_Type = Counter32
_WirelessIfWORPStaStatsReceiveSuccess_Object = MibTableColumn
wirelessIfWORPStaStatsReceiveSuccess = _WirelessIfWORPStaStatsReceiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 16),
    _WirelessIfWORPStaStatsReceiveSuccess_Type()
)
wirelessIfWORPStaStatsReceiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsReceiveSuccess.setStatus("current")
_WirelessIfWORPStaStatsReceiveRetries_Type = Counter32
_WirelessIfWORPStaStatsReceiveRetries_Object = MibTableColumn
wirelessIfWORPStaStatsReceiveRetries = _WirelessIfWORPStaStatsReceiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 17),
    _WirelessIfWORPStaStatsReceiveRetries_Type()
)
wirelessIfWORPStaStatsReceiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsReceiveRetries.setStatus("current")
_WirelessIfWORPStaStatsReceiveFailures_Type = Counter32
_WirelessIfWORPStaStatsReceiveFailures_Object = MibTableColumn
wirelessIfWORPStaStatsReceiveFailures = _WirelessIfWORPStaStatsReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 18),
    _WirelessIfWORPStaStatsReceiveFailures_Type()
)
wirelessIfWORPStaStatsReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsReceiveFailures.setStatus("current")
_WirelessIfWORPStaStatsPollNoReplies_Type = Counter32
_WirelessIfWORPStaStatsPollNoReplies_Object = MibTableColumn
wirelessIfWORPStaStatsPollNoReplies = _WirelessIfWORPStaStatsPollNoReplies_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 19),
    _WirelessIfWORPStaStatsPollNoReplies_Type()
)
wirelessIfWORPStaStatsPollNoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsPollNoReplies.setStatus("current")
_WirelessIfWORPStaStatsLocalTxRate_Type = Unsigned32
_WirelessIfWORPStaStatsLocalTxRate_Object = MibTableColumn
wirelessIfWORPStaStatsLocalTxRate = _WirelessIfWORPStaStatsLocalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 20),
    _WirelessIfWORPStaStatsLocalTxRate_Type()
)
wirelessIfWORPStaStatsLocalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalTxRate.setStatus("current")
_WirelessIfWORPStaStatsRemoteTxRate_Type = Unsigned32
_WirelessIfWORPStaStatsRemoteTxRate_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteTxRate = _WirelessIfWORPStaStatsRemoteTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 21),
    _WirelessIfWORPStaStatsRemoteTxRate_Type()
)
wirelessIfWORPStaStatsRemoteTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteTxRate.setStatus("current")
_WirelessIfWORPStaBridgePort_Type = Unsigned32
_WirelessIfWORPStaBridgePort_Object = MibTableColumn
wirelessIfWORPStaBridgePort = _WirelessIfWORPStaBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 22),
    _WirelessIfWORPStaBridgePort_Type()
)
wirelessIfWORPStaBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaBridgePort.setStatus("current")
_WirelessIfWORPStaStatsAverageLocalSNR_Type = Unsigned32
_WirelessIfWORPStaStatsAverageLocalSNR_Object = MibTableColumn
wirelessIfWORPStaStatsAverageLocalSNR = _WirelessIfWORPStaStatsAverageLocalSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 23),
    _WirelessIfWORPStaStatsAverageLocalSNR_Type()
)
wirelessIfWORPStaStatsAverageLocalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageLocalSNR.setStatus("current")
_WirelessIfWORPStaStatsAverageRemoteSNR_Type = Unsigned32
_WirelessIfWORPStaStatsAverageRemoteSNR_Object = MibTableColumn
wirelessIfWORPStaStatsAverageRemoteSNR = _WirelessIfWORPStaStatsAverageRemoteSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 24),
    _WirelessIfWORPStaStatsAverageRemoteSNR_Type()
)
wirelessIfWORPStaStatsAverageRemoteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsAverageRemoteSNR.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSig1_Type = Integer32
_WirelessIfWORPStaStatsLocalMimoCtrlSig1_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSig1 = _WirelessIfWORPStaStatsLocalMimoCtrlSig1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 25),
    _WirelessIfWORPStaStatsLocalMimoCtrlSig1_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSig1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSig1.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSig2_Type = Integer32
_WirelessIfWORPStaStatsLocalMimoCtrlSig2_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSig2 = _WirelessIfWORPStaStatsLocalMimoCtrlSig2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 26),
    _WirelessIfWORPStaStatsLocalMimoCtrlSig2_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSig2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSig2.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSig3_Type = Integer32
_WirelessIfWORPStaStatsLocalMimoCtrlSig3_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSig3 = _WirelessIfWORPStaStatsLocalMimoCtrlSig3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 27),
    _WirelessIfWORPStaStatsLocalMimoCtrlSig3_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSig3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSig3.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoNoise_Type = Integer32
_WirelessIfWORPStaStatsLocalMimoNoise_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoNoise = _WirelessIfWORPStaStatsLocalMimoNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 28),
    _WirelessIfWORPStaStatsLocalMimoNoise_Type()
)
wirelessIfWORPStaStatsLocalMimoNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoNoise.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSNR1_Type = Unsigned32
_WirelessIfWORPStaStatsLocalMimoCtrlSNR1_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSNR1 = _WirelessIfWORPStaStatsLocalMimoCtrlSNR1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 29),
    _WirelessIfWORPStaStatsLocalMimoCtrlSNR1_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSNR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSNR1.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSNR2_Type = Unsigned32
_WirelessIfWORPStaStatsLocalMimoCtrlSNR2_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSNR2 = _WirelessIfWORPStaStatsLocalMimoCtrlSNR2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 30),
    _WirelessIfWORPStaStatsLocalMimoCtrlSNR2_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSNR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSNR2.setStatus("current")
_WirelessIfWORPStaStatsLocalMimoCtrlSNR3_Type = Unsigned32
_WirelessIfWORPStaStatsLocalMimoCtrlSNR3_Object = MibTableColumn
wirelessIfWORPStaStatsLocalMimoCtrlSNR3 = _WirelessIfWORPStaStatsLocalMimoCtrlSNR3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 31),
    _WirelessIfWORPStaStatsLocalMimoCtrlSNR3_Type()
)
wirelessIfWORPStaStatsLocalMimoCtrlSNR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalMimoCtrlSNR3.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSig1_Type = Integer32
_WirelessIfWORPStaStatsRemoteMimoCtrlSig1_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSig1 = _WirelessIfWORPStaStatsRemoteMimoCtrlSig1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 32),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSig1_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSig1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSig1.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSig2_Type = Integer32
_WirelessIfWORPStaStatsRemoteMimoCtrlSig2_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSig2 = _WirelessIfWORPStaStatsRemoteMimoCtrlSig2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 33),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSig2_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSig2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSig2.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSig3_Type = Integer32
_WirelessIfWORPStaStatsRemoteMimoCtrlSig3_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSig3 = _WirelessIfWORPStaStatsRemoteMimoCtrlSig3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 34),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSig3_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSig3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSig3.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoNoise_Type = Integer32
_WirelessIfWORPStaStatsRemoteMimoNoise_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoNoise = _WirelessIfWORPStaStatsRemoteMimoNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 35),
    _WirelessIfWORPStaStatsRemoteMimoNoise_Type()
)
wirelessIfWORPStaStatsRemoteMimoNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoNoise.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR1_Type = Unsigned32
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR1_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSNR1 = _WirelessIfWORPStaStatsRemoteMimoCtrlSNR1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 36),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSNR1_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSNR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSNR1.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR2_Type = Unsigned32
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR2_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSNR2 = _WirelessIfWORPStaStatsRemoteMimoCtrlSNR2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 37),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSNR2_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSNR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSNR2.setStatus("current")
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR3_Type = Unsigned32
_WirelessIfWORPStaStatsRemoteMimoCtrlSNR3_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteMimoCtrlSNR3 = _WirelessIfWORPStaStatsRemoteMimoCtrlSNR3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 38),
    _WirelessIfWORPStaStatsRemoteMimoCtrlSNR3_Type()
)
wirelessIfWORPStaStatsRemoteMimoCtrlSNR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteMimoCtrlSNR3.setStatus("current")


class _WirelessIfWORPStaStatsLocalChainBalStatus_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsLocalChainBalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 2),
          ("notApplicable", 1),
          ("notBalanced", 3))
    )


_WirelessIfWORPStaStatsLocalChainBalStatus_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsLocalChainBalStatus_Object = MibTableColumn
wirelessIfWORPStaStatsLocalChainBalStatus = _WirelessIfWORPStaStatsLocalChainBalStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 39),
    _WirelessIfWORPStaStatsLocalChainBalStatus_Type()
)
wirelessIfWORPStaStatsLocalChainBalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsLocalChainBalStatus.setStatus("current")


class _WirelessIfWORPStaStatsRemoteChainBalStatus_Type(Integer32):
    """Custom type wirelessIfWORPStaStatsRemoteChainBalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 2),
          ("notApplicable", 1),
          ("notBalanced", 3))
    )


_WirelessIfWORPStaStatsRemoteChainBalStatus_Type.__name__ = "Integer32"
_WirelessIfWORPStaStatsRemoteChainBalStatus_Object = MibTableColumn
wirelessIfWORPStaStatsRemoteChainBalStatus = _WirelessIfWORPStaStatsRemoteChainBalStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 2, 1, 40),
    _WirelessIfWORPStaStatsRemoteChainBalStatus_Type()
)
wirelessIfWORPStaStatsRemoteChainBalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStaStatsRemoteChainBalStatus.setStatus("current")
_WirelessIfMonNumOfStaConnected_Type = Unsigned32
_WirelessIfMonNumOfStaConnected_Object = MibScalar
wirelessIfMonNumOfStaConnected = _WirelessIfMonNumOfStaConnected_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 1, 3),
    _WirelessIfMonNumOfStaConnected_Type()
)
wirelessIfMonNumOfStaConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfMonNumOfStaConnected.setStatus("current")
_WirelessIfWORPStats_ObjectIdentity = ObjectIdentity
wirelessIfWORPStats = _WirelessIfWORPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2)
)
_WirelessIfWORPStatsTable_Object = MibTable
wirelessIfWORPStatsTable = _WirelessIfWORPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wirelessIfWORPStatsTable.setStatus("current")
_WirelessIfWORPStatsTableEntry_Object = MibTableRow
wirelessIfWORPStatsTableEntry = _WirelessIfWORPStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1)
)
wirelessIfWORPStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfWORPStatsTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfWORPStatsTableEntry.setStatus("current")
_WirelessIfWORPStatsTableIndex_Type = Unsigned32
_WirelessIfWORPStatsTableIndex_Object = MibTableColumn
wirelessIfWORPStatsTableIndex = _WirelessIfWORPStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 1),
    _WirelessIfWORPStatsTableIndex_Type()
)
wirelessIfWORPStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsTableIndex.setStatus("current")


class _WirelessIfWORPStatsAverageLocalSignal_Type(Integer32):
    """Custom type wirelessIfWORPStatsAverageLocalSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStatsAverageLocalSignal_Type.__name__ = "Integer32"
_WirelessIfWORPStatsAverageLocalSignal_Object = MibTableColumn
wirelessIfWORPStatsAverageLocalSignal = _WirelessIfWORPStatsAverageLocalSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 2),
    _WirelessIfWORPStatsAverageLocalSignal_Type()
)
wirelessIfWORPStatsAverageLocalSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAverageLocalSignal.setStatus("current")


class _WirelessIfWORPStatsAverageLocalNoise_Type(Integer32):
    """Custom type wirelessIfWORPStatsAverageLocalNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStatsAverageLocalNoise_Type.__name__ = "Integer32"
_WirelessIfWORPStatsAverageLocalNoise_Object = MibTableColumn
wirelessIfWORPStatsAverageLocalNoise = _WirelessIfWORPStatsAverageLocalNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 3),
    _WirelessIfWORPStatsAverageLocalNoise_Type()
)
wirelessIfWORPStatsAverageLocalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAverageLocalNoise.setStatus("current")


class _WirelessIfWORPStatsAverageRemoteSignal_Type(Integer32):
    """Custom type wirelessIfWORPStatsAverageRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStatsAverageRemoteSignal_Type.__name__ = "Integer32"
_WirelessIfWORPStatsAverageRemoteSignal_Object = MibTableColumn
wirelessIfWORPStatsAverageRemoteSignal = _WirelessIfWORPStatsAverageRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 4),
    _WirelessIfWORPStatsAverageRemoteSignal_Type()
)
wirelessIfWORPStatsAverageRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAverageRemoteSignal.setStatus("current")


class _WirelessIfWORPStatsAverageRemoteNoise_Type(Integer32):
    """Custom type wirelessIfWORPStatsAverageRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_WirelessIfWORPStatsAverageRemoteNoise_Type.__name__ = "Integer32"
_WirelessIfWORPStatsAverageRemoteNoise_Object = MibTableColumn
wirelessIfWORPStatsAverageRemoteNoise = _WirelessIfWORPStatsAverageRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 5),
    _WirelessIfWORPStatsAverageRemoteNoise_Type()
)
wirelessIfWORPStatsAverageRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAverageRemoteNoise.setStatus("current")
_WirelessIfWORPStatsRemotePartners_Type = Unsigned32
_WirelessIfWORPStatsRemotePartners_Object = MibTableColumn
wirelessIfWORPStatsRemotePartners = _WirelessIfWORPStatsRemotePartners_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 6),
    _WirelessIfWORPStatsRemotePartners_Type()
)
wirelessIfWORPStatsRemotePartners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRemotePartners.setStatus("current")
_WirelessIfWORPStatsBaseStationAnnounces_Type = Counter32
_WirelessIfWORPStatsBaseStationAnnounces_Object = MibTableColumn
wirelessIfWORPStatsBaseStationAnnounces = _WirelessIfWORPStatsBaseStationAnnounces_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 7),
    _WirelessIfWORPStatsBaseStationAnnounces_Type()
)
wirelessIfWORPStatsBaseStationAnnounces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsBaseStationAnnounces.setStatus("current")
_WirelessIfWORPStatsRequestForService_Type = Counter32
_WirelessIfWORPStatsRequestForService_Object = MibTableColumn
wirelessIfWORPStatsRequestForService = _WirelessIfWORPStatsRequestForService_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 8),
    _WirelessIfWORPStatsRequestForService_Type()
)
wirelessIfWORPStatsRequestForService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRequestForService.setStatus("current")
_WirelessIfWORPStatsRegistrationRequests_Type = Counter32
_WirelessIfWORPStatsRegistrationRequests_Object = MibTableColumn
wirelessIfWORPStatsRegistrationRequests = _WirelessIfWORPStatsRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 9),
    _WirelessIfWORPStatsRegistrationRequests_Type()
)
wirelessIfWORPStatsRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationRequests.setStatus("current")
_WirelessIfWORPStatsRegistrationRejects_Type = Counter32
_WirelessIfWORPStatsRegistrationRejects_Object = MibTableColumn
wirelessIfWORPStatsRegistrationRejects = _WirelessIfWORPStatsRegistrationRejects_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 10),
    _WirelessIfWORPStatsRegistrationRejects_Type()
)
wirelessIfWORPStatsRegistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationRejects.setStatus("current")
_WirelessIfWORPStatsAuthenticationRequests_Type = Counter32
_WirelessIfWORPStatsAuthenticationRequests_Object = MibTableColumn
wirelessIfWORPStatsAuthenticationRequests = _WirelessIfWORPStatsAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 11),
    _WirelessIfWORPStatsAuthenticationRequests_Type()
)
wirelessIfWORPStatsAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAuthenticationRequests.setStatus("current")
_WirelessIfWORPStatsAuthenticationConfirms_Type = Counter32
_WirelessIfWORPStatsAuthenticationConfirms_Object = MibTableColumn
wirelessIfWORPStatsAuthenticationConfirms = _WirelessIfWORPStatsAuthenticationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 12),
    _WirelessIfWORPStatsAuthenticationConfirms_Type()
)
wirelessIfWORPStatsAuthenticationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsAuthenticationConfirms.setStatus("current")
_WirelessIfWORPStatsRegistrationAttempts_Type = Counter32
_WirelessIfWORPStatsRegistrationAttempts_Object = MibTableColumn
wirelessIfWORPStatsRegistrationAttempts = _WirelessIfWORPStatsRegistrationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 13),
    _WirelessIfWORPStatsRegistrationAttempts_Type()
)
wirelessIfWORPStatsRegistrationAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationAttempts.setStatus("current")
_WirelessIfWORPStatsRegistrationIncompletes_Type = Counter32
_WirelessIfWORPStatsRegistrationIncompletes_Object = MibTableColumn
wirelessIfWORPStatsRegistrationIncompletes = _WirelessIfWORPStatsRegistrationIncompletes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 14),
    _WirelessIfWORPStatsRegistrationIncompletes_Type()
)
wirelessIfWORPStatsRegistrationIncompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationIncompletes.setStatus("current")
_WirelessIfWORPStatsRegistrationTimeouts_Type = Counter32
_WirelessIfWORPStatsRegistrationTimeouts_Object = MibTableColumn
wirelessIfWORPStatsRegistrationTimeouts = _WirelessIfWORPStatsRegistrationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 15),
    _WirelessIfWORPStatsRegistrationTimeouts_Type()
)
wirelessIfWORPStatsRegistrationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationTimeouts.setStatus("current")


class _WirelessIfWORPStatsRegistrationLastReason_Type(Integer32):
    """Custom type wirelessIfWORPStatsRegistrationLastReason based on Integer32"""
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
        *(("incorrectParameter", 3),
          ("lowQuality", 6),
          ("noMoreAllowed", 2),
          ("none", 1),
          ("roaming", 4),
          ("timeout", 5))
    )


_WirelessIfWORPStatsRegistrationLastReason_Type.__name__ = "Integer32"
_WirelessIfWORPStatsRegistrationLastReason_Object = MibTableColumn
wirelessIfWORPStatsRegistrationLastReason = _WirelessIfWORPStatsRegistrationLastReason_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 16),
    _WirelessIfWORPStatsRegistrationLastReason_Type()
)
wirelessIfWORPStatsRegistrationLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsRegistrationLastReason.setStatus("current")
_WirelessIfWORPStatsPollData_Type = Counter32
_WirelessIfWORPStatsPollData_Object = MibTableColumn
wirelessIfWORPStatsPollData = _WirelessIfWORPStatsPollData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 17),
    _WirelessIfWORPStatsPollData_Type()
)
wirelessIfWORPStatsPollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsPollData.setStatus("current")
_WirelessIfWORPStatsPollNoData_Type = Counter32
_WirelessIfWORPStatsPollNoData_Object = MibTableColumn
wirelessIfWORPStatsPollNoData = _WirelessIfWORPStatsPollNoData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 18),
    _WirelessIfWORPStatsPollNoData_Type()
)
wirelessIfWORPStatsPollNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsPollNoData.setStatus("current")
_WirelessIfWORPStatsReplyData_Type = Counter32
_WirelessIfWORPStatsReplyData_Object = MibTableColumn
wirelessIfWORPStatsReplyData = _WirelessIfWORPStatsReplyData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 19),
    _WirelessIfWORPStatsReplyData_Type()
)
wirelessIfWORPStatsReplyData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReplyData.setStatus("current")
_WirelessIfWORPStatsReplyMoreData_Type = Counter32
_WirelessIfWORPStatsReplyMoreData_Object = MibTableColumn
wirelessIfWORPStatsReplyMoreData = _WirelessIfWORPStatsReplyMoreData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 20),
    _WirelessIfWORPStatsReplyMoreData_Type()
)
wirelessIfWORPStatsReplyMoreData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReplyMoreData.setStatus("current")
_WirelessIfWORPStatsReplyNoData_Type = Counter32
_WirelessIfWORPStatsReplyNoData_Object = MibTableColumn
wirelessIfWORPStatsReplyNoData = _WirelessIfWORPStatsReplyNoData_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 21),
    _WirelessIfWORPStatsReplyNoData_Type()
)
wirelessIfWORPStatsReplyNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReplyNoData.setStatus("current")
_WirelessIfWORPStatsPollNoReplies_Type = Counter32
_WirelessIfWORPStatsPollNoReplies_Object = MibTableColumn
wirelessIfWORPStatsPollNoReplies = _WirelessIfWORPStatsPollNoReplies_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 22),
    _WirelessIfWORPStatsPollNoReplies_Type()
)
wirelessIfWORPStatsPollNoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsPollNoReplies.setStatus("current")
_WirelessIfWORPStatsSendSuccess_Type = Counter32
_WirelessIfWORPStatsSendSuccess_Object = MibTableColumn
wirelessIfWORPStatsSendSuccess = _WirelessIfWORPStatsSendSuccess_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 23),
    _WirelessIfWORPStatsSendSuccess_Type()
)
wirelessIfWORPStatsSendSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsSendSuccess.setStatus("current")
_WirelessIfWORPStatsSendRetries_Type = Counter32
_WirelessIfWORPStatsSendRetries_Object = MibTableColumn
wirelessIfWORPStatsSendRetries = _WirelessIfWORPStatsSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 24),
    _WirelessIfWORPStatsSendRetries_Type()
)
wirelessIfWORPStatsSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsSendRetries.setStatus("current")
_WirelessIfWORPStatsSendFailures_Type = Counter32
_WirelessIfWORPStatsSendFailures_Object = MibTableColumn
wirelessIfWORPStatsSendFailures = _WirelessIfWORPStatsSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 25),
    _WirelessIfWORPStatsSendFailures_Type()
)
wirelessIfWORPStatsSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsSendFailures.setStatus("current")
_WirelessIfWORPStatsReceiveSuccess_Type = Counter32
_WirelessIfWORPStatsReceiveSuccess_Object = MibTableColumn
wirelessIfWORPStatsReceiveSuccess = _WirelessIfWORPStatsReceiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 26),
    _WirelessIfWORPStatsReceiveSuccess_Type()
)
wirelessIfWORPStatsReceiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReceiveSuccess.setStatus("current")
_WirelessIfWORPStatsReceiveRetries_Type = Counter32
_WirelessIfWORPStatsReceiveRetries_Object = MibTableColumn
wirelessIfWORPStatsReceiveRetries = _WirelessIfWORPStatsReceiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 27),
    _WirelessIfWORPStatsReceiveRetries_Type()
)
wirelessIfWORPStatsReceiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReceiveRetries.setStatus("current")
_WirelessIfWORPStatsReceiveFailures_Type = Counter32
_WirelessIfWORPStatsReceiveFailures_Object = MibTableColumn
wirelessIfWORPStatsReceiveFailures = _WirelessIfWORPStatsReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 28),
    _WirelessIfWORPStatsReceiveFailures_Type()
)
wirelessIfWORPStatsReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsReceiveFailures.setStatus("current")
_WirelessIfWORPStatsProvisionedUplinkCIR_Type = Unsigned32
_WirelessIfWORPStatsProvisionedUplinkCIR_Object = MibTableColumn
wirelessIfWORPStatsProvisionedUplinkCIR = _WirelessIfWORPStatsProvisionedUplinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 29),
    _WirelessIfWORPStatsProvisionedUplinkCIR_Type()
)
wirelessIfWORPStatsProvisionedUplinkCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsProvisionedUplinkCIR.setStatus("current")
_WirelessIfWORPStatsProvisionedDownlinkCIR_Type = Unsigned32
_WirelessIfWORPStatsProvisionedDownlinkCIR_Object = MibTableColumn
wirelessIfWORPStatsProvisionedDownlinkCIR = _WirelessIfWORPStatsProvisionedDownlinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 30),
    _WirelessIfWORPStatsProvisionedDownlinkCIR_Type()
)
wirelessIfWORPStatsProvisionedDownlinkCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsProvisionedDownlinkCIR.setStatus("current")
_WirelessIfWORPStatsProvisionedUplinkMIR_Type = Unsigned32
_WirelessIfWORPStatsProvisionedUplinkMIR_Object = MibTableColumn
wirelessIfWORPStatsProvisionedUplinkMIR = _WirelessIfWORPStatsProvisionedUplinkMIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 31),
    _WirelessIfWORPStatsProvisionedUplinkMIR_Type()
)
wirelessIfWORPStatsProvisionedUplinkMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsProvisionedUplinkMIR.setStatus("current")
_WirelessIfWORPStatsProvisionedDownlinkMIR_Type = Unsigned32
_WirelessIfWORPStatsProvisionedDownlinkMIR_Object = MibTableColumn
wirelessIfWORPStatsProvisionedDownlinkMIR = _WirelessIfWORPStatsProvisionedDownlinkMIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 32),
    _WirelessIfWORPStatsProvisionedDownlinkMIR_Type()
)
wirelessIfWORPStatsProvisionedDownlinkMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsProvisionedDownlinkMIR.setStatus("current")
_WirelessIfWORPStatsActiveUplinkCIR_Type = Unsigned32
_WirelessIfWORPStatsActiveUplinkCIR_Object = MibTableColumn
wirelessIfWORPStatsActiveUplinkCIR = _WirelessIfWORPStatsActiveUplinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 33),
    _WirelessIfWORPStatsActiveUplinkCIR_Type()
)
wirelessIfWORPStatsActiveUplinkCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsActiveUplinkCIR.setStatus("current")
_WirelessIfWORPStatsActiveDownlinkCIR_Type = Unsigned32
_WirelessIfWORPStatsActiveDownlinkCIR_Object = MibTableColumn
wirelessIfWORPStatsActiveDownlinkCIR = _WirelessIfWORPStatsActiveDownlinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 34),
    _WirelessIfWORPStatsActiveDownlinkCIR_Type()
)
wirelessIfWORPStatsActiveDownlinkCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsActiveDownlinkCIR.setStatus("current")
_WirelessIfWORPStatsActiveUplinkMIR_Type = Unsigned32
_WirelessIfWORPStatsActiveUplinkMIR_Object = MibTableColumn
wirelessIfWORPStatsActiveUplinkMIR = _WirelessIfWORPStatsActiveUplinkMIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 35),
    _WirelessIfWORPStatsActiveUplinkMIR_Type()
)
wirelessIfWORPStatsActiveUplinkMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsActiveUplinkMIR.setStatus("current")
_WirelessIfWORPStatsActiveDownlinkMIR_Type = Unsigned32
_WirelessIfWORPStatsActiveDownlinkMIR_Object = MibTableColumn
wirelessIfWORPStatsActiveDownlinkMIR = _WirelessIfWORPStatsActiveDownlinkMIR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 36),
    _WirelessIfWORPStatsActiveDownlinkMIR_Type()
)
wirelessIfWORPStatsActiveDownlinkMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsActiveDownlinkMIR.setStatus("current")
_WirelessIfWORPStatsCurrentUplinkBandwidth_Type = Unsigned32
_WirelessIfWORPStatsCurrentUplinkBandwidth_Object = MibTableColumn
wirelessIfWORPStatsCurrentUplinkBandwidth = _WirelessIfWORPStatsCurrentUplinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 37),
    _WirelessIfWORPStatsCurrentUplinkBandwidth_Type()
)
wirelessIfWORPStatsCurrentUplinkBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsCurrentUplinkBandwidth.setStatus("current")
_WirelessIfWORPStatsCurrentDownlinkBandwidth_Type = Unsigned32
_WirelessIfWORPStatsCurrentDownlinkBandwidth_Object = MibTableColumn
wirelessIfWORPStatsCurrentDownlinkBandwidth = _WirelessIfWORPStatsCurrentDownlinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 2, 1, 1, 38),
    _WirelessIfWORPStatsCurrentDownlinkBandwidth_Type()
)
wirelessIfWORPStatsCurrentDownlinkBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPStatsCurrentDownlinkBandwidth.setStatus("current")
_WirelessIfBlacklistInfo_ObjectIdentity = ObjectIdentity
wirelessIfBlacklistInfo = _WirelessIfBlacklistInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3)
)
_WirelessIfBlacklistInfoTable_Object = MibTable
wirelessIfBlacklistInfoTable = _WirelessIfBlacklistInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wirelessIfBlacklistInfoTable.setStatus("current")
_WirelessIfBlacklistInfoTableEntry_Object = MibTableRow
wirelessIfBlacklistInfoTableEntry = _WirelessIfBlacklistInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1)
)
wirelessIfBlacklistInfoTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfBlacklistInfoTableIndex"),
    (0, "PROXIM-MIB", "wirelessIfBlacklistInfoTableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfBlacklistInfoTableEntry.setStatus("current")


class _WirelessIfBlacklistInfoTableIndex_Type(Unsigned32):
    """Custom type wirelessIfBlacklistInfoTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessIfBlacklistInfoTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfBlacklistInfoTableIndex_Object = MibTableColumn
wirelessIfBlacklistInfoTableIndex = _WirelessIfBlacklistInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1, 1),
    _WirelessIfBlacklistInfoTableIndex_Type()
)
wirelessIfBlacklistInfoTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfBlacklistInfoTableIndex.setStatus("current")
_WirelessIfBlacklistInfoTableSecIndex_Type = Unsigned32
_WirelessIfBlacklistInfoTableSecIndex_Object = MibTableColumn
wirelessIfBlacklistInfoTableSecIndex = _WirelessIfBlacklistInfoTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1, 2),
    _WirelessIfBlacklistInfoTableSecIndex_Type()
)
wirelessIfBlacklistInfoTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfBlacklistInfoTableSecIndex.setStatus("current")
_WirelessIfBlacklistedChannelNum_Type = Unsigned32
_WirelessIfBlacklistedChannelNum_Object = MibTableColumn
wirelessIfBlacklistedChannelNum = _WirelessIfBlacklistedChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1, 3),
    _WirelessIfBlacklistedChannelNum_Type()
)
wirelessIfBlacklistedChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfBlacklistedChannelNum.setStatus("current")
_WirelessIfBlacklistReason_Type = DisplayString
_WirelessIfBlacklistReason_Object = MibTableColumn
wirelessIfBlacklistReason = _WirelessIfBlacklistReason_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1, 4),
    _WirelessIfBlacklistReason_Type()
)
wirelessIfBlacklistReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfBlacklistReason.setStatus("current")
_WirelessIfBlacklistTimeElapsed_Type = Unsigned32
_WirelessIfBlacklistTimeElapsed_Object = MibTableColumn
wirelessIfBlacklistTimeElapsed = _WirelessIfBlacklistTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 3, 1, 1, 5),
    _WirelessIfBlacklistTimeElapsed_Type()
)
wirelessIfBlacklistTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfBlacklistTimeElapsed.setStatus("current")
_WirelessIfWORPLinkTest_ObjectIdentity = ObjectIdentity
wirelessIfWORPLinkTest = _WirelessIfWORPLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4)
)
_WirelessIfWORPLinkTestConfTable_Object = MibTable
wirelessIfWORPLinkTestConfTable = _WirelessIfWORPLinkTestConfTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestConfTable.setStatus("current")
_WirelessIfWORPLinkTestConfTableEntry_Object = MibTableRow
wirelessIfWORPLinkTestConfTableEntry = _WirelessIfWORPLinkTestConfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1, 1)
)
wirelessIfWORPLinkTestConfTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfWORPLinkTestConfTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestConfTableEntry.setStatus("current")


class _WirelessIfWORPLinkTestConfTableIndex_Type(Unsigned32):
    """Custom type wirelessIfWORPLinkTestConfTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WirelessIfWORPLinkTestConfTableIndex_Type.__name__ = "Unsigned32"
_WirelessIfWORPLinkTestConfTableIndex_Object = MibTableColumn
wirelessIfWORPLinkTestConfTableIndex = _WirelessIfWORPLinkTestConfTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1, 1, 1),
    _WirelessIfWORPLinkTestConfTableIndex_Type()
)
wirelessIfWORPLinkTestConfTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestConfTableIndex.setStatus("current")


class _WirelessIfWORPLinkTestExploreStatus_Type(Integer32):
    """Custom type wirelessIfWORPLinkTestExploreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_WirelessIfWORPLinkTestExploreStatus_Type.__name__ = "Integer32"
_WirelessIfWORPLinkTestExploreStatus_Object = MibTableColumn
wirelessIfWORPLinkTestExploreStatus = _WirelessIfWORPLinkTestExploreStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1, 1, 2),
    _WirelessIfWORPLinkTestExploreStatus_Type()
)
wirelessIfWORPLinkTestExploreStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestExploreStatus.setStatus("current")


class _WirelessIfWORPLinkTestProgressStatus_Type(Integer32):
    """Custom type wirelessIfWORPLinkTestProgressStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("stopped", 3),
          ("timeOut", 4))
    )


_WirelessIfWORPLinkTestProgressStatus_Type.__name__ = "Integer32"
_WirelessIfWORPLinkTestProgressStatus_Object = MibTableColumn
wirelessIfWORPLinkTestProgressStatus = _WirelessIfWORPLinkTestProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1, 1, 3),
    _WirelessIfWORPLinkTestProgressStatus_Type()
)
wirelessIfWORPLinkTestProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestProgressStatus.setStatus("current")


class _WirelessIfWORPLinkTestIdleTimeout_Type(Unsigned32):
    """Custom type wirelessIfWORPLinkTestIdleTimeout based on Unsigned32"""
    defaultValue = 300


_WirelessIfWORPLinkTestIdleTimeout_Object = MibTableColumn
wirelessIfWORPLinkTestIdleTimeout = _WirelessIfWORPLinkTestIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 1, 1, 4),
    _WirelessIfWORPLinkTestIdleTimeout_Type()
)
wirelessIfWORPLinkTestIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestIdleTimeout.setStatus("current")
_WirelessIfWORPLinkTestStatsTable_Object = MibTable
wirelessIfWORPLinkTestStatsTable = _WirelessIfWORPLinkTestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5)
)
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStatsTable.setStatus("current")
_WirelessIfWORPLinkTestStatsTableEntry_Object = MibTableRow
wirelessIfWORPLinkTestStatsTableEntry = _WirelessIfWORPLinkTestStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1)
)
wirelessIfWORPLinkTestStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfWORPLinkTestStatsTableIndex"),
    (0, "PROXIM-MIB", "wirelessIfWORPLinkTestStatsTableSecIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStatsTableEntry.setStatus("current")
_WirelessIfWORPLinkTestStatsTableIndex_Type = Unsigned32
_WirelessIfWORPLinkTestStatsTableIndex_Object = MibTableColumn
wirelessIfWORPLinkTestStatsTableIndex = _WirelessIfWORPLinkTestStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 1),
    _WirelessIfWORPLinkTestStatsTableIndex_Type()
)
wirelessIfWORPLinkTestStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStatsTableIndex.setStatus("current")
_WirelessIfWORPLinkTestStatsTableSecIndex_Type = Unsigned32
_WirelessIfWORPLinkTestStatsTableSecIndex_Object = MibTableColumn
wirelessIfWORPLinkTestStatsTableSecIndex = _WirelessIfWORPLinkTestStatsTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 2),
    _WirelessIfWORPLinkTestStatsTableSecIndex_Type()
)
wirelessIfWORPLinkTestStatsTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStatsTableSecIndex.setStatus("current")


class _WirelessIfWORPLinkTestStatus_Type(Integer32):
    """Custom type wirelessIfWORPLinkTestStatus based on Integer32"""
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


_WirelessIfWORPLinkTestStatus_Type.__name__ = "Integer32"
_WirelessIfWORPLinkTestStatus_Object = MibTableColumn
wirelessIfWORPLinkTestStatus = _WirelessIfWORPLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 3),
    _WirelessIfWORPLinkTestStatus_Type()
)
wirelessIfWORPLinkTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStatus.setStatus("current")
_WirelessIfWORPLinkTestStationName_Type = DisplayString
_WirelessIfWORPLinkTestStationName_Object = MibTableColumn
wirelessIfWORPLinkTestStationName = _WirelessIfWORPLinkTestStationName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 4),
    _WirelessIfWORPLinkTestStationName_Type()
)
wirelessIfWORPLinkTestStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestStationName.setStatus("current")
_WirelessIfWORPLinkTestMACAddress_Type = MacAddress
_WirelessIfWORPLinkTestMACAddress_Object = MibTableColumn
wirelessIfWORPLinkTestMACAddress = _WirelessIfWORPLinkTestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 5),
    _WirelessIfWORPLinkTestMACAddress_Type()
)
wirelessIfWORPLinkTestMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestMACAddress.setStatus("current")


class _WirelessIfWORPLinkTestWORPLinkStatus_Type(Integer32):
    """Custom type wirelessIfWORPLinkTestWORPLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WirelessIfWORPLinkTestWORPLinkStatus_Type.__name__ = "Integer32"
_WirelessIfWORPLinkTestWORPLinkStatus_Object = MibTableColumn
wirelessIfWORPLinkTestWORPLinkStatus = _WirelessIfWORPLinkTestWORPLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 6),
    _WirelessIfWORPLinkTestWORPLinkStatus_Type()
)
wirelessIfWORPLinkTestWORPLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestWORPLinkStatus.setStatus("current")
_WirelessIfWORPLinkTestLocalCurSignal_Type = Integer32
_WirelessIfWORPLinkTestLocalCurSignal_Object = MibTableColumn
wirelessIfWORPLinkTestLocalCurSignal = _WirelessIfWORPLinkTestLocalCurSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 7),
    _WirelessIfWORPLinkTestLocalCurSignal_Type()
)
wirelessIfWORPLinkTestLocalCurSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalCurSignal.setStatus("current")
_WirelessIfWORPLinkTestLocalCurNoise_Type = Integer32
_WirelessIfWORPLinkTestLocalCurNoise_Object = MibTableColumn
wirelessIfWORPLinkTestLocalCurNoise = _WirelessIfWORPLinkTestLocalCurNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 8),
    _WirelessIfWORPLinkTestLocalCurNoise_Type()
)
wirelessIfWORPLinkTestLocalCurNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalCurNoise.setStatus("current")
_WirelessIfWORPLinkTestLocalCurSNR_Type = Integer32
_WirelessIfWORPLinkTestLocalCurSNR_Object = MibTableColumn
wirelessIfWORPLinkTestLocalCurSNR = _WirelessIfWORPLinkTestLocalCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 9),
    _WirelessIfWORPLinkTestLocalCurSNR_Type()
)
wirelessIfWORPLinkTestLocalCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalCurSNR.setStatus("current")
_WirelessIfWORPLinkTestLocalMinSignal_Type = Integer32
_WirelessIfWORPLinkTestLocalMinSignal_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMinSignal = _WirelessIfWORPLinkTestLocalMinSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 10),
    _WirelessIfWORPLinkTestLocalMinSignal_Type()
)
wirelessIfWORPLinkTestLocalMinSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMinSignal.setStatus("current")
_WirelessIfWORPLinkTestLocalMinNoise_Type = Integer32
_WirelessIfWORPLinkTestLocalMinNoise_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMinNoise = _WirelessIfWORPLinkTestLocalMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 11),
    _WirelessIfWORPLinkTestLocalMinNoise_Type()
)
wirelessIfWORPLinkTestLocalMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMinNoise.setStatus("current")
_WirelessIfWORPLinkTestLocalMinSNR_Type = Integer32
_WirelessIfWORPLinkTestLocalMinSNR_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMinSNR = _WirelessIfWORPLinkTestLocalMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 12),
    _WirelessIfWORPLinkTestLocalMinSNR_Type()
)
wirelessIfWORPLinkTestLocalMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMinSNR.setStatus("current")
_WirelessIfWORPLinkTestLocalMaxSignal_Type = Integer32
_WirelessIfWORPLinkTestLocalMaxSignal_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMaxSignal = _WirelessIfWORPLinkTestLocalMaxSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 13),
    _WirelessIfWORPLinkTestLocalMaxSignal_Type()
)
wirelessIfWORPLinkTestLocalMaxSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMaxSignal.setStatus("current")
_WirelessIfWORPLinkTestLocalMaxNoise_Type = Integer32
_WirelessIfWORPLinkTestLocalMaxNoise_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMaxNoise = _WirelessIfWORPLinkTestLocalMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 14),
    _WirelessIfWORPLinkTestLocalMaxNoise_Type()
)
wirelessIfWORPLinkTestLocalMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMaxNoise.setStatus("current")
_WirelessIfWORPLinkTestLocalMaxSNR_Type = Integer32
_WirelessIfWORPLinkTestLocalMaxSNR_Object = MibTableColumn
wirelessIfWORPLinkTestLocalMaxSNR = _WirelessIfWORPLinkTestLocalMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 15),
    _WirelessIfWORPLinkTestLocalMaxSNR_Type()
)
wirelessIfWORPLinkTestLocalMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestLocalMaxSNR.setStatus("current")
_WirelessIfWORPLinkTestRemoteCurSignal_Type = Integer32
_WirelessIfWORPLinkTestRemoteCurSignal_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteCurSignal = _WirelessIfWORPLinkTestRemoteCurSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 16),
    _WirelessIfWORPLinkTestRemoteCurSignal_Type()
)
wirelessIfWORPLinkTestRemoteCurSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteCurSignal.setStatus("current")
_WirelessIfWORPLinkTestRemoteCurNoise_Type = Integer32
_WirelessIfWORPLinkTestRemoteCurNoise_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteCurNoise = _WirelessIfWORPLinkTestRemoteCurNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 17),
    _WirelessIfWORPLinkTestRemoteCurNoise_Type()
)
wirelessIfWORPLinkTestRemoteCurNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteCurNoise.setStatus("current")
_WirelessIfWORPLinkTestRemoteCurSNR_Type = Integer32
_WirelessIfWORPLinkTestRemoteCurSNR_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteCurSNR = _WirelessIfWORPLinkTestRemoteCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 18),
    _WirelessIfWORPLinkTestRemoteCurSNR_Type()
)
wirelessIfWORPLinkTestRemoteCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteCurSNR.setStatus("current")
_WirelessIfWORPLinkTestRemoteMinSignal_Type = Integer32
_WirelessIfWORPLinkTestRemoteMinSignal_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMinSignal = _WirelessIfWORPLinkTestRemoteMinSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 19),
    _WirelessIfWORPLinkTestRemoteMinSignal_Type()
)
wirelessIfWORPLinkTestRemoteMinSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMinSignal.setStatus("current")
_WirelessIfWORPLinkTestRemoteMinNoise_Type = Integer32
_WirelessIfWORPLinkTestRemoteMinNoise_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMinNoise = _WirelessIfWORPLinkTestRemoteMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 20),
    _WirelessIfWORPLinkTestRemoteMinNoise_Type()
)
wirelessIfWORPLinkTestRemoteMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMinNoise.setStatus("current")
_WirelessIfWORPLinkTestRemoteMinSNR_Type = Integer32
_WirelessIfWORPLinkTestRemoteMinSNR_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMinSNR = _WirelessIfWORPLinkTestRemoteMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 21),
    _WirelessIfWORPLinkTestRemoteMinSNR_Type()
)
wirelessIfWORPLinkTestRemoteMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMinSNR.setStatus("current")
_WirelessIfWORPLinkTestRemoteMaxSignal_Type = Integer32
_WirelessIfWORPLinkTestRemoteMaxSignal_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMaxSignal = _WirelessIfWORPLinkTestRemoteMaxSignal_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 22),
    _WirelessIfWORPLinkTestRemoteMaxSignal_Type()
)
wirelessIfWORPLinkTestRemoteMaxSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMaxSignal.setStatus("current")
_WirelessIfWORPLinkTestRemoteMaxNoise_Type = Integer32
_WirelessIfWORPLinkTestRemoteMaxNoise_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMaxNoise = _WirelessIfWORPLinkTestRemoteMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 23),
    _WirelessIfWORPLinkTestRemoteMaxNoise_Type()
)
wirelessIfWORPLinkTestRemoteMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMaxNoise.setStatus("current")
_WirelessIfWORPLinkTestRemoteMaxSNR_Type = Integer32
_WirelessIfWORPLinkTestRemoteMaxSNR_Object = MibTableColumn
wirelessIfWORPLinkTestRemoteMaxSNR = _WirelessIfWORPLinkTestRemoteMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 4, 5, 1, 24),
    _WirelessIfWORPLinkTestRemoteMaxSNR_Type()
)
wirelessIfWORPLinkTestRemoteMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfWORPLinkTestRemoteMaxSNR.setStatus("current")
_WirelessIfStats_ObjectIdentity = ObjectIdentity
wirelessIfStats = _WirelessIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5)
)
_WirelessIfStatsTable_Object = MibTable
wirelessIfStatsTable = _WirelessIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    wirelessIfStatsTable.setStatus("current")
_WirelessIfStatsTableEntry_Object = MibTableRow
wirelessIfStatsTableEntry = _WirelessIfStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1)
)
wirelessIfStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "wirelessIfStatsTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessIfStatsTableEntry.setStatus("current")
_WirelessIfStatsTableIndex_Type = Unsigned32
_WirelessIfStatsTableIndex_Object = MibTableColumn
wirelessIfStatsTableIndex = _WirelessIfStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 1),
    _WirelessIfStatsTableIndex_Type()
)
wirelessIfStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsTableIndex.setStatus("current")
_WirelessIfStatsTxPkts_Type = Counter32
_WirelessIfStatsTxPkts_Object = MibTableColumn
wirelessIfStatsTxPkts = _WirelessIfStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 2),
    _WirelessIfStatsTxPkts_Type()
)
wirelessIfStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsTxPkts.setStatus("current")
_WirelessIfStatsTxBytes_Type = Counter64
_WirelessIfStatsTxBytes_Object = MibTableColumn
wirelessIfStatsTxBytes = _WirelessIfStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 3),
    _WirelessIfStatsTxBytes_Type()
)
wirelessIfStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsTxBytes.setStatus("current")
_WirelessIfStatsRxPkts_Type = Counter32
_WirelessIfStatsRxPkts_Object = MibTableColumn
wirelessIfStatsRxPkts = _WirelessIfStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 4),
    _WirelessIfStatsRxPkts_Type()
)
wirelessIfStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsRxPkts.setStatus("current")
_WirelessIfStatsRxBytes_Type = Counter64
_WirelessIfStatsRxBytes_Object = MibTableColumn
wirelessIfStatsRxBytes = _WirelessIfStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 5),
    _WirelessIfStatsRxBytes_Type()
)
wirelessIfStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsRxBytes.setStatus("current")
_WirelessIfStatsRxDecryptErrors_Type = Counter64
_WirelessIfStatsRxDecryptErrors_Object = MibTableColumn
wirelessIfStatsRxDecryptErrors = _WirelessIfStatsRxDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 6),
    _WirelessIfStatsRxDecryptErrors_Type()
)
wirelessIfStatsRxDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsRxDecryptErrors.setStatus("current")
_WirelessIfStatsRxCRCErrors_Type = Counter64
_WirelessIfStatsRxCRCErrors_Object = MibTableColumn
wirelessIfStatsRxCRCErrors = _WirelessIfStatsRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 7),
    _WirelessIfStatsRxCRCErrors_Type()
)
wirelessIfStatsRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsRxCRCErrors.setStatus("current")
_WirelessIfStatsChain0CtlRSSI_Type = Integer32
_WirelessIfStatsChain0CtlRSSI_Object = MibTableColumn
wirelessIfStatsChain0CtlRSSI = _WirelessIfStatsChain0CtlRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 8),
    _WirelessIfStatsChain0CtlRSSI_Type()
)
wirelessIfStatsChain0CtlRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain0CtlRSSI.setStatus("current")
_WirelessIfStatsChain1CtlRSSI_Type = Integer32
_WirelessIfStatsChain1CtlRSSI_Object = MibTableColumn
wirelessIfStatsChain1CtlRSSI = _WirelessIfStatsChain1CtlRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 9),
    _WirelessIfStatsChain1CtlRSSI_Type()
)
wirelessIfStatsChain1CtlRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain1CtlRSSI.setStatus("current")
_WirelessIfStatsChain2CtlRSSI_Type = Integer32
_WirelessIfStatsChain2CtlRSSI_Object = MibTableColumn
wirelessIfStatsChain2CtlRSSI = _WirelessIfStatsChain2CtlRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 10),
    _WirelessIfStatsChain2CtlRSSI_Type()
)
wirelessIfStatsChain2CtlRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain2CtlRSSI.setStatus("current")
_WirelessIfStatsChain0ExtRSSI_Type = Integer32
_WirelessIfStatsChain0ExtRSSI_Object = MibTableColumn
wirelessIfStatsChain0ExtRSSI = _WirelessIfStatsChain0ExtRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 11),
    _WirelessIfStatsChain0ExtRSSI_Type()
)
wirelessIfStatsChain0ExtRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain0ExtRSSI.setStatus("current")
_WirelessIfStatsChain1ExtRSSI_Type = Integer32
_WirelessIfStatsChain1ExtRSSI_Object = MibTableColumn
wirelessIfStatsChain1ExtRSSI = _WirelessIfStatsChain1ExtRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 12),
    _WirelessIfStatsChain1ExtRSSI_Type()
)
wirelessIfStatsChain1ExtRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain1ExtRSSI.setStatus("current")
_WirelessIfStatsChain2ExtRSSI_Type = Integer32
_WirelessIfStatsChain2ExtRSSI_Object = MibTableColumn
wirelessIfStatsChain2ExtRSSI = _WirelessIfStatsChain2ExtRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 13),
    _WirelessIfStatsChain2ExtRSSI_Type()
)
wirelessIfStatsChain2ExtRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsChain2ExtRSSI.setStatus("current")
_WirelessIfStatsCombinedRSSI_Type = Integer32
_WirelessIfStatsCombinedRSSI_Object = MibTableColumn
wirelessIfStatsCombinedRSSI = _WirelessIfStatsCombinedRSSI_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 14),
    _WirelessIfStatsCombinedRSSI_Type()
)
wirelessIfStatsCombinedRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsCombinedRSSI.setStatus("current")
_WirelessIfStatsPhyErrors_Type = Integer32
_WirelessIfStatsPhyErrors_Object = MibTableColumn
wirelessIfStatsPhyErrors = _WirelessIfStatsPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 15),
    _WirelessIfStatsPhyErrors_Type()
)
wirelessIfStatsPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsPhyErrors.setStatus("current")
_WirelessIfStatsRadioReTunes_Type = Integer32
_WirelessIfStatsRadioReTunes_Object = MibTableColumn
wirelessIfStatsRadioReTunes = _WirelessIfStatsRadioReTunes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 4, 5, 1, 1, 16),
    _WirelessIfStatsRadioReTunes_Type()
)
wirelessIfStatsRadioReTunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIfStatsRadioReTunes.setStatus("current")
_RadiusMon_ObjectIdentity = ObjectIdentity
radiusMon = _RadiusMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5)
)
_RadiusClientStats_ObjectIdentity = ObjectIdentity
radiusClientStats = _RadiusClientStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1)
)
_RadiusClientAuthStatsTable_Object = MibTable
radiusClientAuthStatsTable = _RadiusClientAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    radiusClientAuthStatsTable.setStatus("current")
_RadiusClientAuthStatsTableEntry_Object = MibTableRow
radiusClientAuthStatsTableEntry = _RadiusClientAuthStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1)
)
radiusClientAuthStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "radiusClientAuthStatsTableIndex"),
    (0, "PROXIM-MIB", "radiusClientAuthStatsTableSecIndex"),
)
if mibBuilder.loadTexts:
    radiusClientAuthStatsTableEntry.setStatus("current")


class _RadiusClientAuthStatsTableIndex_Type(Unsigned32):
    """Custom type radiusClientAuthStatsTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadiusClientAuthStatsTableIndex_Type.__name__ = "Unsigned32"
_RadiusClientAuthStatsTableIndex_Object = MibTableColumn
radiusClientAuthStatsTableIndex = _RadiusClientAuthStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 1),
    _RadiusClientAuthStatsTableIndex_Type()
)
radiusClientAuthStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsTableIndex.setStatus("current")


class _RadiusClientAuthStatsTableSecIndex_Type(Unsigned32):
    """Custom type radiusClientAuthStatsTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RadiusClientAuthStatsTableSecIndex_Type.__name__ = "Unsigned32"
_RadiusClientAuthStatsTableSecIndex_Object = MibTableColumn
radiusClientAuthStatsTableSecIndex = _RadiusClientAuthStatsTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 2),
    _RadiusClientAuthStatsTableSecIndex_Type()
)
radiusClientAuthStatsTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsTableSecIndex.setStatus("current")
_RadiusClientAuthStatsRoundTripTime_Type = TimeTicks
_RadiusClientAuthStatsRoundTripTime_Object = MibTableColumn
radiusClientAuthStatsRoundTripTime = _RadiusClientAuthStatsRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 3),
    _RadiusClientAuthStatsRoundTripTime_Type()
)
radiusClientAuthStatsRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsRoundTripTime.setStatus("current")
_RadiusClientAuthStatsRequests_Type = Counter32
_RadiusClientAuthStatsRequests_Object = MibTableColumn
radiusClientAuthStatsRequests = _RadiusClientAuthStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 4),
    _RadiusClientAuthStatsRequests_Type()
)
radiusClientAuthStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsRequests.setStatus("current")
_RadiusClientAuthStatsRetransmissions_Type = Counter32
_RadiusClientAuthStatsRetransmissions_Object = MibTableColumn
radiusClientAuthStatsRetransmissions = _RadiusClientAuthStatsRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 5),
    _RadiusClientAuthStatsRetransmissions_Type()
)
radiusClientAuthStatsRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsRetransmissions.setStatus("current")
_RadiusClientAuthStatsAccessAccepts_Type = Counter32
_RadiusClientAuthStatsAccessAccepts_Object = MibTableColumn
radiusClientAuthStatsAccessAccepts = _RadiusClientAuthStatsAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 6),
    _RadiusClientAuthStatsAccessAccepts_Type()
)
radiusClientAuthStatsAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsAccessAccepts.setStatus("current")
_RadiusClientAuthStatsAccessRejects_Type = Counter32
_RadiusClientAuthStatsAccessRejects_Object = MibTableColumn
radiusClientAuthStatsAccessRejects = _RadiusClientAuthStatsAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 7),
    _RadiusClientAuthStatsAccessRejects_Type()
)
radiusClientAuthStatsAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsAccessRejects.setStatus("current")
_RadiusClientAuthStatsAccessChallenges_Type = Counter32
_RadiusClientAuthStatsAccessChallenges_Object = MibTableColumn
radiusClientAuthStatsAccessChallenges = _RadiusClientAuthStatsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 8),
    _RadiusClientAuthStatsAccessChallenges_Type()
)
radiusClientAuthStatsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsAccessChallenges.setStatus("current")
_RadiusClientAuthStatsResponses_Type = Counter32
_RadiusClientAuthStatsResponses_Object = MibTableColumn
radiusClientAuthStatsResponses = _RadiusClientAuthStatsResponses_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 9),
    _RadiusClientAuthStatsResponses_Type()
)
radiusClientAuthStatsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsResponses.setStatus("current")
_RadiusClientAuthStatsMalformedResponses_Type = Counter32
_RadiusClientAuthStatsMalformedResponses_Object = MibTableColumn
radiusClientAuthStatsMalformedResponses = _RadiusClientAuthStatsMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 10),
    _RadiusClientAuthStatsMalformedResponses_Type()
)
radiusClientAuthStatsMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsMalformedResponses.setStatus("current")
_RadiusClientAuthStatsBadAuthenticators_Type = Counter32
_RadiusClientAuthStatsBadAuthenticators_Object = MibTableColumn
radiusClientAuthStatsBadAuthenticators = _RadiusClientAuthStatsBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 11),
    _RadiusClientAuthStatsBadAuthenticators_Type()
)
radiusClientAuthStatsBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsBadAuthenticators.setStatus("current")
_RadiusClientAuthStatsTimeouts_Type = Counter32
_RadiusClientAuthStatsTimeouts_Object = MibTableColumn
radiusClientAuthStatsTimeouts = _RadiusClientAuthStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 12),
    _RadiusClientAuthStatsTimeouts_Type()
)
radiusClientAuthStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsTimeouts.setStatus("current")
_RadiusClientAuthStatsUnknownTypes_Type = Counter32
_RadiusClientAuthStatsUnknownTypes_Object = MibTableColumn
radiusClientAuthStatsUnknownTypes = _RadiusClientAuthStatsUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 13),
    _RadiusClientAuthStatsUnknownTypes_Type()
)
radiusClientAuthStatsUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsUnknownTypes.setStatus("current")
_RadiusClientAuthStatsPacketsDropped_Type = Counter32
_RadiusClientAuthStatsPacketsDropped_Object = MibTableColumn
radiusClientAuthStatsPacketsDropped = _RadiusClientAuthStatsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 1, 1, 14),
    _RadiusClientAuthStatsPacketsDropped_Type()
)
radiusClientAuthStatsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthStatsPacketsDropped.setStatus("current")
_RadiusClientAccStatsTable_Object = MibTable
radiusClientAccStatsTable = _RadiusClientAccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    radiusClientAccStatsTable.setStatus("current")
_RadiusClientAccStatsTableEntry_Object = MibTableRow
radiusClientAccStatsTableEntry = _RadiusClientAccStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1)
)
radiusClientAccStatsTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "radiusClientAccStatsTableIndex"),
    (0, "PROXIM-MIB", "radiusClientAccStatsTableSecIndex"),
)
if mibBuilder.loadTexts:
    radiusClientAccStatsTableEntry.setStatus("current")


class _RadiusClientAccStatsTableIndex_Type(Unsigned32):
    """Custom type radiusClientAccStatsTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadiusClientAccStatsTableIndex_Type.__name__ = "Unsigned32"
_RadiusClientAccStatsTableIndex_Object = MibTableColumn
radiusClientAccStatsTableIndex = _RadiusClientAccStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 1),
    _RadiusClientAccStatsTableIndex_Type()
)
radiusClientAccStatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsTableIndex.setStatus("current")


class _RadiusClientAccStatsTableSecIndex_Type(Unsigned32):
    """Custom type radiusClientAccStatsTableSecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RadiusClientAccStatsTableSecIndex_Type.__name__ = "Unsigned32"
_RadiusClientAccStatsTableSecIndex_Object = MibTableColumn
radiusClientAccStatsTableSecIndex = _RadiusClientAccStatsTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 2),
    _RadiusClientAccStatsTableSecIndex_Type()
)
radiusClientAccStatsTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsTableSecIndex.setStatus("current")
_RadiusClientAccStatsRoundTripTime_Type = TimeTicks
_RadiusClientAccStatsRoundTripTime_Object = MibTableColumn
radiusClientAccStatsRoundTripTime = _RadiusClientAccStatsRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 3),
    _RadiusClientAccStatsRoundTripTime_Type()
)
radiusClientAccStatsRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsRoundTripTime.setStatus("current")
_RadiusClientAccStatsRequests_Type = Counter32
_RadiusClientAccStatsRequests_Object = MibTableColumn
radiusClientAccStatsRequests = _RadiusClientAccStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 4),
    _RadiusClientAccStatsRequests_Type()
)
radiusClientAccStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsRequests.setStatus("current")
_RadiusClientAccStatsRetransmissions_Type = Counter32
_RadiusClientAccStatsRetransmissions_Object = MibTableColumn
radiusClientAccStatsRetransmissions = _RadiusClientAccStatsRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 5),
    _RadiusClientAccStatsRetransmissions_Type()
)
radiusClientAccStatsRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsRetransmissions.setStatus("current")
_RadiusClientAccStatsResponses_Type = Counter32
_RadiusClientAccStatsResponses_Object = MibTableColumn
radiusClientAccStatsResponses = _RadiusClientAccStatsResponses_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 6),
    _RadiusClientAccStatsResponses_Type()
)
radiusClientAccStatsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsResponses.setStatus("current")
_RadiusClientAccStatsMalformedResponses_Type = Counter32
_RadiusClientAccStatsMalformedResponses_Object = MibTableColumn
radiusClientAccStatsMalformedResponses = _RadiusClientAccStatsMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 7),
    _RadiusClientAccStatsMalformedResponses_Type()
)
radiusClientAccStatsMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsMalformedResponses.setStatus("current")
_RadiusClientAccStatsTimeouts_Type = Counter32
_RadiusClientAccStatsTimeouts_Object = MibTableColumn
radiusClientAccStatsTimeouts = _RadiusClientAccStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 8),
    _RadiusClientAccStatsTimeouts_Type()
)
radiusClientAccStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsTimeouts.setStatus("current")
_RadiusClientAccStatsUnknownTypes_Type = Counter32
_RadiusClientAccStatsUnknownTypes_Object = MibTableColumn
radiusClientAccStatsUnknownTypes = _RadiusClientAccStatsUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 9),
    _RadiusClientAccStatsUnknownTypes_Type()
)
radiusClientAccStatsUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsUnknownTypes.setStatus("current")
_RadiusClientAccStatsPacketsDropped_Type = Counter32
_RadiusClientAccStatsPacketsDropped_Object = MibTableColumn
radiusClientAccStatsPacketsDropped = _RadiusClientAccStatsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 5, 1, 2, 1, 10),
    _RadiusClientAccStatsPacketsDropped_Type()
)
radiusClientAccStatsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccStatsPacketsDropped.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6)
)
_InterfaceTraps_ObjectIdentity = ObjectIdentity
interfaceTraps = _InterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1)
)
_SecurityTraps_ObjectIdentity = ObjectIdentity
securityTraps = _SecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 2)
)
_OperationalTraps_ObjectIdentity = ObjectIdentity
operationalTraps = _OperationalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 3)
)
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4)
)
_SntpTraps_ObjectIdentity = ObjectIdentity
sntpTraps = _SntpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 5)
)
_ImageTraps_ObjectIdentity = ObjectIdentity
imageTraps = _ImageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 6)
)
_SiteSurvey_ObjectIdentity = ObjectIdentity
siteSurvey = _SiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7)
)
_WorpSiteSurvey_ObjectIdentity = ObjectIdentity
worpSiteSurvey = _WorpSiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1)
)
_WorpSiteSurveyOperationTable_Object = MibTable
worpSiteSurveyOperationTable = _WorpSiteSurveyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    worpSiteSurveyOperationTable.setStatus("current")
_WorpSiteSurveyOperationTableEntry_Object = MibTableRow
worpSiteSurveyOperationTableEntry = _WorpSiteSurveyOperationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 1, 1)
)
worpSiteSurveyOperationTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpSiteSurveyOperationTableIndex"),
)
if mibBuilder.loadTexts:
    worpSiteSurveyOperationTableEntry.setStatus("current")
_WorpSiteSurveyOperationTableIndex_Type = Unsigned32
_WorpSiteSurveyOperationTableIndex_Object = MibTableColumn
worpSiteSurveyOperationTableIndex = _WorpSiteSurveyOperationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 1, 1, 1),
    _WorpSiteSurveyOperationTableIndex_Type()
)
worpSiteSurveyOperationTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyOperationTableIndex.setStatus("current")


class _WorpSiteSurveyOperationIfName_Type(DisplayString):
    """Custom type worpSiteSurveyOperationIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WorpSiteSurveyOperationIfName_Type.__name__ = "DisplayString"
_WorpSiteSurveyOperationIfName_Object = MibTableColumn
worpSiteSurveyOperationIfName = _WorpSiteSurveyOperationIfName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 1, 1, 2),
    _WorpSiteSurveyOperationIfName_Type()
)
worpSiteSurveyOperationIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyOperationIfName.setStatus("current")


class _WorpSiteSurveyOperationStatus_Type(Integer32):
    """Custom type worpSiteSurveyOperationStatus based on Integer32"""
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


_WorpSiteSurveyOperationStatus_Type.__name__ = "Integer32"
_WorpSiteSurveyOperationStatus_Object = MibTableColumn
worpSiteSurveyOperationStatus = _WorpSiteSurveyOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 1, 1, 3),
    _WorpSiteSurveyOperationStatus_Type()
)
worpSiteSurveyOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    worpSiteSurveyOperationStatus.setStatus("current")
_WorpSiteSurveyTable_Object = MibTable
worpSiteSurveyTable = _WorpSiteSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    worpSiteSurveyTable.setStatus("current")
_WorpSiteSurveyTableEntry_Object = MibTableRow
worpSiteSurveyTableEntry = _WorpSiteSurveyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1)
)
worpSiteSurveyTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "worpSiteSurveyTableIndex"),
    (0, "PROXIM-MIB", "worpSiteSurveyTableSecIndex"),
)
if mibBuilder.loadTexts:
    worpSiteSurveyTableEntry.setStatus("current")
_WorpSiteSurveyTableIndex_Type = Unsigned32
_WorpSiteSurveyTableIndex_Object = MibTableColumn
worpSiteSurveyTableIndex = _WorpSiteSurveyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 1),
    _WorpSiteSurveyTableIndex_Type()
)
worpSiteSurveyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyTableIndex.setStatus("current")
_WorpSiteSurveyTableSecIndex_Type = Unsigned32
_WorpSiteSurveyTableSecIndex_Object = MibTableColumn
worpSiteSurveyTableSecIndex = _WorpSiteSurveyTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 2),
    _WorpSiteSurveyTableSecIndex_Type()
)
worpSiteSurveyTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyTableSecIndex.setStatus("current")
_WorpSiteSurveyBaseMACAddress_Type = PhysAddress
_WorpSiteSurveyBaseMACAddress_Object = MibTableColumn
worpSiteSurveyBaseMACAddress = _WorpSiteSurveyBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 3),
    _WorpSiteSurveyBaseMACAddress_Type()
)
worpSiteSurveyBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyBaseMACAddress.setStatus("current")
_WorpSiteSurveyBaseName_Type = DisplayString
_WorpSiteSurveyBaseName_Object = MibTableColumn
worpSiteSurveyBaseName = _WorpSiteSurveyBaseName_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 4),
    _WorpSiteSurveyBaseName_Type()
)
worpSiteSurveyBaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyBaseName.setStatus("current")
_WorpSiteSurveyMaxSatellitesAllowed_Type = Unsigned32
_WorpSiteSurveyMaxSatellitesAllowed_Object = MibTableColumn
worpSiteSurveyMaxSatellitesAllowed = _WorpSiteSurveyMaxSatellitesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 5),
    _WorpSiteSurveyMaxSatellitesAllowed_Type()
)
worpSiteSurveyMaxSatellitesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyMaxSatellitesAllowed.setStatus("current")
_WorpSiteSurveyNumSatellitesRegistered_Type = Unsigned32
_WorpSiteSurveyNumSatellitesRegistered_Object = MibTableColumn
worpSiteSurveyNumSatellitesRegistered = _WorpSiteSurveyNumSatellitesRegistered_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 6),
    _WorpSiteSurveyNumSatellitesRegistered_Type()
)
worpSiteSurveyNumSatellitesRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyNumSatellitesRegistered.setStatus("current")


class _WorpSiteSurveySatelliteRegisteredStatus_Type(Integer32):
    """Custom type worpSiteSurveySatelliteRegisteredStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-Registered", 2),
          ("registered", 1))
    )


_WorpSiteSurveySatelliteRegisteredStatus_Type.__name__ = "Integer32"
_WorpSiteSurveySatelliteRegisteredStatus_Object = MibTableColumn
worpSiteSurveySatelliteRegisteredStatus = _WorpSiteSurveySatelliteRegisteredStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 7),
    _WorpSiteSurveySatelliteRegisteredStatus_Type()
)
worpSiteSurveySatelliteRegisteredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveySatelliteRegisteredStatus.setStatus("current")
_WorpSiteSurveyLocalTxRate_Type = Unsigned32
_WorpSiteSurveyLocalTxRate_Object = MibTableColumn
worpSiteSurveyLocalTxRate = _WorpSiteSurveyLocalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 8),
    _WorpSiteSurveyLocalTxRate_Type()
)
worpSiteSurveyLocalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalTxRate.setStatus("current")
_WorpSiteSurveyRemoteTxRate_Type = Unsigned32
_WorpSiteSurveyRemoteTxRate_Object = MibTableColumn
worpSiteSurveyRemoteTxRate = _WorpSiteSurveyRemoteTxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 9),
    _WorpSiteSurveyRemoteTxRate_Type()
)
worpSiteSurveyRemoteTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteTxRate.setStatus("current")
_WorpSiteSurveyLocalSignalLevel_Type = Integer32
_WorpSiteSurveyLocalSignalLevel_Object = MibTableColumn
worpSiteSurveyLocalSignalLevel = _WorpSiteSurveyLocalSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 10),
    _WorpSiteSurveyLocalSignalLevel_Type()
)
worpSiteSurveyLocalSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalSignalLevel.setStatus("current")
_WorpSiteSurveyLocalNoiseLevel_Type = Integer32
_WorpSiteSurveyLocalNoiseLevel_Object = MibTableColumn
worpSiteSurveyLocalNoiseLevel = _WorpSiteSurveyLocalNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 11),
    _WorpSiteSurveyLocalNoiseLevel_Type()
)
worpSiteSurveyLocalNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalNoiseLevel.setStatus("current")
_WorpSiteSurveyLocalSNR_Type = Unsigned32
_WorpSiteSurveyLocalSNR_Object = MibTableColumn
worpSiteSurveyLocalSNR = _WorpSiteSurveyLocalSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 12),
    _WorpSiteSurveyLocalSNR_Type()
)
worpSiteSurveyLocalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalSNR.setStatus("current")
_WorpSiteSurveyRemoteSignalLevel_Type = Integer32
_WorpSiteSurveyRemoteSignalLevel_Object = MibTableColumn
worpSiteSurveyRemoteSignalLevel = _WorpSiteSurveyRemoteSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 13),
    _WorpSiteSurveyRemoteSignalLevel_Type()
)
worpSiteSurveyRemoteSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteSignalLevel.setStatus("current")
_WorpSiteSurveyRemoteNoiseLevel_Type = Integer32
_WorpSiteSurveyRemoteNoiseLevel_Object = MibTableColumn
worpSiteSurveyRemoteNoiseLevel = _WorpSiteSurveyRemoteNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 14),
    _WorpSiteSurveyRemoteNoiseLevel_Type()
)
worpSiteSurveyRemoteNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteNoiseLevel.setStatus("current")
_WorpSiteSurveyRemoteSNR_Type = Unsigned32
_WorpSiteSurveyRemoteSNR_Object = MibTableColumn
worpSiteSurveyRemoteSNR = _WorpSiteSurveyRemoteSNR_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 15),
    _WorpSiteSurveyRemoteSNR_Type()
)
worpSiteSurveyRemoteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteSNR.setStatus("current")
_WorpSiteSurveyChannel_Type = Unsigned32
_WorpSiteSurveyChannel_Object = MibTableColumn
worpSiteSurveyChannel = _WorpSiteSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 16),
    _WorpSiteSurveyChannel_Type()
)
worpSiteSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyChannel.setStatus("current")
_WorpSiteSurveyChannelBandwidth_Type = Unsigned32
_WorpSiteSurveyChannelBandwidth_Object = MibTableColumn
worpSiteSurveyChannelBandwidth = _WorpSiteSurveyChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 17),
    _WorpSiteSurveyChannelBandwidth_Type()
)
worpSiteSurveyChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyChannelBandwidth.setStatus("current")
_WorpSiteSurveyChannelRxRate_Type = Unsigned32
_WorpSiteSurveyChannelRxRate_Object = MibTableColumn
worpSiteSurveyChannelRxRate = _WorpSiteSurveyChannelRxRate_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 18),
    _WorpSiteSurveyChannelRxRate_Type()
)
worpSiteSurveyChannelRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyChannelRxRate.setStatus("current")
_WorpSiteSurveyBaseBridgePort_Type = Unsigned32
_WorpSiteSurveyBaseBridgePort_Object = MibTableColumn
worpSiteSurveyBaseBridgePort = _WorpSiteSurveyBaseBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 19),
    _WorpSiteSurveyBaseBridgePort_Type()
)
worpSiteSurveyBaseBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyBaseBridgePort.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSig1_Type = Integer32
_WorpSiteSurveyLocalMimoCtrlSig1_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSig1 = _WorpSiteSurveyLocalMimoCtrlSig1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 20),
    _WorpSiteSurveyLocalMimoCtrlSig1_Type()
)
worpSiteSurveyLocalMimoCtrlSig1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSig1.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSig2_Type = Integer32
_WorpSiteSurveyLocalMimoCtrlSig2_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSig2 = _WorpSiteSurveyLocalMimoCtrlSig2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 21),
    _WorpSiteSurveyLocalMimoCtrlSig2_Type()
)
worpSiteSurveyLocalMimoCtrlSig2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSig2.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSig3_Type = Integer32
_WorpSiteSurveyLocalMimoCtrlSig3_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSig3 = _WorpSiteSurveyLocalMimoCtrlSig3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 22),
    _WorpSiteSurveyLocalMimoCtrlSig3_Type()
)
worpSiteSurveyLocalMimoCtrlSig3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSig3.setStatus("current")
_WorpSiteSurveyLocalMimoNoise_Type = Integer32
_WorpSiteSurveyLocalMimoNoise_Object = MibTableColumn
worpSiteSurveyLocalMimoNoise = _WorpSiteSurveyLocalMimoNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 23),
    _WorpSiteSurveyLocalMimoNoise_Type()
)
worpSiteSurveyLocalMimoNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoNoise.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSNR1_Type = Unsigned32
_WorpSiteSurveyLocalMimoCtrlSNR1_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSNR1 = _WorpSiteSurveyLocalMimoCtrlSNR1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 24),
    _WorpSiteSurveyLocalMimoCtrlSNR1_Type()
)
worpSiteSurveyLocalMimoCtrlSNR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSNR1.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSNR2_Type = Unsigned32
_WorpSiteSurveyLocalMimoCtrlSNR2_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSNR2 = _WorpSiteSurveyLocalMimoCtrlSNR2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 25),
    _WorpSiteSurveyLocalMimoCtrlSNR2_Type()
)
worpSiteSurveyLocalMimoCtrlSNR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSNR2.setStatus("current")
_WorpSiteSurveyLocalMimoCtrlSNR3_Type = Unsigned32
_WorpSiteSurveyLocalMimoCtrlSNR3_Object = MibTableColumn
worpSiteSurveyLocalMimoCtrlSNR3 = _WorpSiteSurveyLocalMimoCtrlSNR3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 26),
    _WorpSiteSurveyLocalMimoCtrlSNR3_Type()
)
worpSiteSurveyLocalMimoCtrlSNR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalMimoCtrlSNR3.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSig1_Type = Integer32
_WorpSiteSurveyRemoteMimoCtrlSig1_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSig1 = _WorpSiteSurveyRemoteMimoCtrlSig1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 27),
    _WorpSiteSurveyRemoteMimoCtrlSig1_Type()
)
worpSiteSurveyRemoteMimoCtrlSig1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSig1.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSig2_Type = Integer32
_WorpSiteSurveyRemoteMimoCtrlSig2_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSig2 = _WorpSiteSurveyRemoteMimoCtrlSig2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 28),
    _WorpSiteSurveyRemoteMimoCtrlSig2_Type()
)
worpSiteSurveyRemoteMimoCtrlSig2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSig2.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSig3_Type = Integer32
_WorpSiteSurveyRemoteMimoCtrlSig3_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSig3 = _WorpSiteSurveyRemoteMimoCtrlSig3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 29),
    _WorpSiteSurveyRemoteMimoCtrlSig3_Type()
)
worpSiteSurveyRemoteMimoCtrlSig3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSig3.setStatus("current")
_WorpSiteSurveyRemoteMimoNoise_Type = Integer32
_WorpSiteSurveyRemoteMimoNoise_Object = MibTableColumn
worpSiteSurveyRemoteMimoNoise = _WorpSiteSurveyRemoteMimoNoise_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 30),
    _WorpSiteSurveyRemoteMimoNoise_Type()
)
worpSiteSurveyRemoteMimoNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoNoise.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSNR1_Type = Unsigned32
_WorpSiteSurveyRemoteMimoCtrlSNR1_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSNR1 = _WorpSiteSurveyRemoteMimoCtrlSNR1_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 31),
    _WorpSiteSurveyRemoteMimoCtrlSNR1_Type()
)
worpSiteSurveyRemoteMimoCtrlSNR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSNR1.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSNR2_Type = Unsigned32
_WorpSiteSurveyRemoteMimoCtrlSNR2_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSNR2 = _WorpSiteSurveyRemoteMimoCtrlSNR2_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 32),
    _WorpSiteSurveyRemoteMimoCtrlSNR2_Type()
)
worpSiteSurveyRemoteMimoCtrlSNR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSNR2.setStatus("current")
_WorpSiteSurveyRemoteMimoCtrlSNR3_Type = Unsigned32
_WorpSiteSurveyRemoteMimoCtrlSNR3_Object = MibTableColumn
worpSiteSurveyRemoteMimoCtrlSNR3 = _WorpSiteSurveyRemoteMimoCtrlSNR3_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 33),
    _WorpSiteSurveyRemoteMimoCtrlSNR3_Type()
)
worpSiteSurveyRemoteMimoCtrlSNR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteMimoCtrlSNR3.setStatus("current")


class _WorpSiteSurveyLocalChainBalStatus_Type(Integer32):
    """Custom type worpSiteSurveyLocalChainBalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 2),
          ("notApplicable", 1),
          ("notBalanced", 3))
    )


_WorpSiteSurveyLocalChainBalStatus_Type.__name__ = "Integer32"
_WorpSiteSurveyLocalChainBalStatus_Object = MibTableColumn
worpSiteSurveyLocalChainBalStatus = _WorpSiteSurveyLocalChainBalStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 34),
    _WorpSiteSurveyLocalChainBalStatus_Type()
)
worpSiteSurveyLocalChainBalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyLocalChainBalStatus.setStatus("current")


class _WorpSiteSurveyRemoteChainBalStatus_Type(Integer32):
    """Custom type worpSiteSurveyRemoteChainBalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 2),
          ("notApplicable", 1),
          ("notBalanced", 3))
    )


_WorpSiteSurveyRemoteChainBalStatus_Type.__name__ = "Integer32"
_WorpSiteSurveyRemoteChainBalStatus_Object = MibTableColumn
worpSiteSurveyRemoteChainBalStatus = _WorpSiteSurveyRemoteChainBalStatus_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 7, 1, 2, 1, 35),
    _WorpSiteSurveyRemoteChainBalStatus_Type()
)
worpSiteSurveyRemoteChainBalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worpSiteSurveyRemoteChainBalStatus.setStatus("current")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8)
)


class _CurrentUnitTemp_Type(Integer32):
    """Custom type currentUnitTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_CurrentUnitTemp_Type.__name__ = "Integer32"
_CurrentUnitTemp_Object = MibScalar
currentUnitTemp = _CurrentUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8, 1),
    _CurrentUnitTemp_Type()
)
currentUnitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUnitTemp.setStatus("current")


class _HighTempThreshold_Type(Integer32):
    """Custom type highTempThreshold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_HighTempThreshold_Type.__name__ = "Integer32"
_HighTempThreshold_Object = MibScalar
highTempThreshold = _HighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8, 2),
    _HighTempThreshold_Type()
)
highTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTempThreshold.setStatus("current")


class _LowTempThreshold_Type(Integer32):
    """Custom type lowTempThreshold based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_LowTempThreshold_Type.__name__ = "Integer32"
_LowTempThreshold_Object = MibScalar
lowTempThreshold = _LowTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8, 3),
    _LowTempThreshold_Type()
)
lowTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTempThreshold.setStatus("current")


class _TempLoggingInterval_Type(Integer32):
    """Custom type tempLoggingInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TempLoggingInterval_Type.__name__ = "Integer32"
_TempLoggingInterval_Object = MibScalar
tempLoggingInterval = _TempLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8, 4),
    _TempLoggingInterval_Type()
)
tempLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLoggingInterval.setStatus("current")


class _TempLogReset_Type(Integer32):
    """Custom type tempLogReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TempLogReset_Type.__name__ = "Integer32"
_TempLogReset_Object = MibScalar
tempLogReset = _TempLogReset_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 8, 5),
    _TempLogReset_Type()
)
tempLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLogReset.setStatus("current")
_SysMonitor_ObjectIdentity = ObjectIdentity
sysMonitor = _SysMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 9)
)


class _SysMonitorCPUUsage_Type(DisplayString):
    """Custom type sysMonitorCPUUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysMonitorCPUUsage_Type.__name__ = "DisplayString"
_SysMonitorCPUUsage_Object = MibScalar
sysMonitorCPUUsage = _SysMonitorCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 9, 1),
    _SysMonitorCPUUsage_Type()
)
sysMonitorCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMonitorCPUUsage.setStatus("current")


class _SysMonitorRAMUsage_Type(DisplayString):
    """Custom type sysMonitorRAMUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysMonitorRAMUsage_Type.__name__ = "DisplayString"
_SysMonitorRAMUsage_Object = MibScalar
sysMonitorRAMUsage = _SysMonitorRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 9, 2),
    _SysMonitorRAMUsage_Type()
)
sysMonitorRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMonitorRAMUsage.setStatus("current")
_IgmpStats_ObjectIdentity = ObjectIdentity
igmpStats = _IgmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10)
)
_IgmpEthernetSnoopingStats_ObjectIdentity = ObjectIdentity
igmpEthernetSnoopingStats = _IgmpEthernetSnoopingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1)
)
_IgmpEth1MCastTable_Object = MibTable
igmpEth1MCastTable = _IgmpEth1MCastTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    igmpEth1MCastTable.setStatus("current")
_IgmpEth1MCastTableEntry_Object = MibTableRow
igmpEth1MCastTableEntry = _IgmpEth1MCastTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1, 1)
)
igmpEth1MCastTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "igmpEth1MCastTableIndex"),
)
if mibBuilder.loadTexts:
    igmpEth1MCastTableEntry.setStatus("current")
_IgmpEth1MCastTableIndex_Type = Unsigned32
_IgmpEth1MCastTableIndex_Object = MibTableColumn
igmpEth1MCastTableIndex = _IgmpEth1MCastTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1, 1, 1),
    _IgmpEth1MCastTableIndex_Type()
)
igmpEth1MCastTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth1MCastTableIndex.setStatus("current")
_IgmpEth1MCastGrpIp_Type = IpAddress
_IgmpEth1MCastGrpIp_Object = MibTableColumn
igmpEth1MCastGrpIp = _IgmpEth1MCastGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1, 1, 2),
    _IgmpEth1MCastGrpIp_Type()
)
igmpEth1MCastGrpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth1MCastGrpIp.setStatus("current")
_IgmpEth1MCastGrpMACAddr_Type = MacAddress
_IgmpEth1MCastGrpMACAddr_Object = MibTableColumn
igmpEth1MCastGrpMACAddr = _IgmpEth1MCastGrpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1, 1, 3),
    _IgmpEth1MCastGrpMACAddr_Type()
)
igmpEth1MCastGrpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth1MCastGrpMACAddr.setStatus("current")
_IgmpEth1MCastGrpAgingTimeElapsed_Type = TimeTicks
_IgmpEth1MCastGrpAgingTimeElapsed_Object = MibTableColumn
igmpEth1MCastGrpAgingTimeElapsed = _IgmpEth1MCastGrpAgingTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 1, 1, 4),
    _IgmpEth1MCastGrpAgingTimeElapsed_Type()
)
igmpEth1MCastGrpAgingTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth1MCastGrpAgingTimeElapsed.setStatus("current")
_IgmpEth2MCastTable_Object = MibTable
igmpEth2MCastTable = _IgmpEth2MCastTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2)
)
if mibBuilder.loadTexts:
    igmpEth2MCastTable.setStatus("current")
_IgmpEth2MCastTableEntry_Object = MibTableRow
igmpEth2MCastTableEntry = _IgmpEth2MCastTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2, 1)
)
igmpEth2MCastTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "igmpEth2MCastTableIndex"),
)
if mibBuilder.loadTexts:
    igmpEth2MCastTableEntry.setStatus("current")
_IgmpEth2MCastTableIndex_Type = Unsigned32
_IgmpEth2MCastTableIndex_Object = MibTableColumn
igmpEth2MCastTableIndex = _IgmpEth2MCastTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2, 1, 1),
    _IgmpEth2MCastTableIndex_Type()
)
igmpEth2MCastTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth2MCastTableIndex.setStatus("current")
_IgmpEth2MCastGrpIp_Type = IpAddress
_IgmpEth2MCastGrpIp_Object = MibTableColumn
igmpEth2MCastGrpIp = _IgmpEth2MCastGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2, 1, 2),
    _IgmpEth2MCastGrpIp_Type()
)
igmpEth2MCastGrpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth2MCastGrpIp.setStatus("current")
_IgmpEth2MCastGrpMACAddr_Type = MacAddress
_IgmpEth2MCastGrpMACAddr_Object = MibTableColumn
igmpEth2MCastGrpMACAddr = _IgmpEth2MCastGrpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2, 1, 3),
    _IgmpEth2MCastGrpMACAddr_Type()
)
igmpEth2MCastGrpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth2MCastGrpMACAddr.setStatus("current")
_IgmpEth2MCastGrpAgingTimeElapsed_Type = TimeTicks
_IgmpEth2MCastGrpAgingTimeElapsed_Object = MibTableColumn
igmpEth2MCastGrpAgingTimeElapsed = _IgmpEth2MCastGrpAgingTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 1, 2, 1, 4),
    _IgmpEth2MCastGrpAgingTimeElapsed_Type()
)
igmpEth2MCastGrpAgingTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEth2MCastGrpAgingTimeElapsed.setStatus("current")
_IgmpWirelessSnoopingStats_ObjectIdentity = ObjectIdentity
igmpWirelessSnoopingStats = _IgmpWirelessSnoopingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2)
)
_IgmpWireless1MCastTable_Object = MibTable
igmpWireless1MCastTable = _IgmpWireless1MCastTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    igmpWireless1MCastTable.setStatus("current")
_IgmpWireless1MCastTableEntry_Object = MibTableRow
igmpWireless1MCastTableEntry = _IgmpWireless1MCastTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1, 1)
)
igmpWireless1MCastTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "igmpWireless1MCastTableIndex"),
)
if mibBuilder.loadTexts:
    igmpWireless1MCastTableEntry.setStatus("current")
_IgmpWireless1MCastTableIndex_Type = Unsigned32
_IgmpWireless1MCastTableIndex_Object = MibTableColumn
igmpWireless1MCastTableIndex = _IgmpWireless1MCastTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1, 1, 1),
    _IgmpWireless1MCastTableIndex_Type()
)
igmpWireless1MCastTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpWireless1MCastTableIndex.setStatus("current")
_IgmpWireless1MCastGrpIp_Type = IpAddress
_IgmpWireless1MCastGrpIp_Object = MibTableColumn
igmpWireless1MCastGrpIp = _IgmpWireless1MCastGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1, 1, 2),
    _IgmpWireless1MCastGrpIp_Type()
)
igmpWireless1MCastGrpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpWireless1MCastGrpIp.setStatus("current")
_IgmpWireless1MCastGrpMACAddr_Type = MacAddress
_IgmpWireless1MCastGrpMACAddr_Object = MibTableColumn
igmpWireless1MCastGrpMACAddr = _IgmpWireless1MCastGrpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1, 1, 3),
    _IgmpWireless1MCastGrpMACAddr_Type()
)
igmpWireless1MCastGrpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpWireless1MCastGrpMACAddr.setStatus("current")
_IgmpWireless1MCastGrpAgingTimeElapsed_Type = TimeTicks
_IgmpWireless1MCastGrpAgingTimeElapsed_Object = MibTableColumn
igmpWireless1MCastGrpAgingTimeElapsed = _IgmpWireless1MCastGrpAgingTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 2, 1, 1, 4),
    _IgmpWireless1MCastGrpAgingTimeElapsed_Type()
)
igmpWireless1MCastGrpAgingTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpWireless1MCastGrpAgingTimeElapsed.setStatus("current")
_IgmpRouterPortListTable_Object = MibTable
igmpRouterPortListTable = _IgmpRouterPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 3)
)
if mibBuilder.loadTexts:
    igmpRouterPortListTable.setStatus("current")
_IgmpRouterPortListTableEntry_Object = MibTableRow
igmpRouterPortListTableEntry = _IgmpRouterPortListTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 3, 1)
)
igmpRouterPortListTableEntry.setIndexNames(
    (0, "PROXIM-MIB", "igmpRouterPortListTableIndex"),
)
if mibBuilder.loadTexts:
    igmpRouterPortListTableEntry.setStatus("current")
_IgmpRouterPortListTableIndex_Type = Unsigned32
_IgmpRouterPortListTableIndex_Object = MibTableColumn
igmpRouterPortListTableIndex = _IgmpRouterPortListTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 3, 1, 1),
    _IgmpRouterPortListTableIndex_Type()
)
igmpRouterPortListTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortListTableIndex.setStatus("current")
_IgmpRouterPortNumber_Type = Unsigned32
_IgmpRouterPortNumber_Object = MibTableColumn
igmpRouterPortNumber = _IgmpRouterPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 3, 1, 2),
    _IgmpRouterPortNumber_Type()
)
igmpRouterPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPortNumber.setStatus("current")
_IgmpRouterAgingTimeElapsed_Type = TimeTicks
_IgmpRouterAgingTimeElapsed_Object = MibTableColumn
igmpRouterAgingTimeElapsed = _IgmpRouterAgingTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 10, 3, 1, 3),
    _IgmpRouterAgingTimeElapsed_Type()
)
igmpRouterAgingTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterAgingTimeElapsed.setStatus("current")
_DebugLog_ObjectIdentity = ObjectIdentity
debugLog = _DebugLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 11)
)
_DebugLogBitMask_Type = Unsigned32
_DebugLogBitMask_Object = MibScalar
debugLogBitMask = _DebugLogBitMask_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 11, 1),
    _DebugLogBitMask_Type()
)
debugLogBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugLogBitMask.setStatus("current")


class _DebugLogReset_Type(Integer32):
    """Custom type debugLogReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_DebugLogReset_Type.__name__ = "Integer32"
_DebugLogReset_Object = MibScalar
debugLogReset = _DebugLogReset_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 11, 2),
    _DebugLogReset_Type()
)
debugLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugLogReset.setStatus("current")
_DebugLogSize_Type = Unsigned32
_DebugLogSize_Object = MibScalar
debugLogSize = _DebugLogSize_Object(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 11, 3),
    _DebugLogSize_Type()
)
debugLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLogSize.setStatus("current")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2)
)
_Ap_800_ObjectIdentity = ObjectIdentity
ap_800 = _Ap_800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2, 1)
)
_Ap_8000_ObjectIdentity = ObjectIdentity
ap_8000 = _Ap_8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2, 2)
)
_Qb_8100_ObjectIdentity = ObjectIdentity
qb_8100 = _Qb_8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2, 11)
)
_Mp_8100_ObjectIdentity = ObjectIdentity
mp_8100 = _Mp_8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2, 21)
)
_Mp_8100_cpe_ObjectIdentity = ObjectIdentity
mp_8100_cpe = _Mp_8100_cpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 841, 2, 22)
)

# Managed Objects groups


# Notification objects

wirelessInterfaceCardInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1, 1)
)
wirelessInterfaceCardInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wirelessInterfaceCardInitFailure.setStatus(
        "current"
    )

wirelessInterfaceCardRadarInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1, 2)
)
wirelessInterfaceCardRadarInterferenceDetected.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wirelessInterfaceCardRadarInterferenceDetected.setStatus(
        "current"
    )

wirelessInterfaceInvalidRegDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1, 3)
)
wirelessInterfaceInvalidRegDomain.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wirelessInterfaceInvalidRegDomain.setStatus(
        "current"
    )

wirelessInterfaceWorldModeCCNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1, 4)
)
wirelessInterfaceWorldModeCCNotSet.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wirelessInterfaceWorldModeCCNotSet.setStatus(
        "current"
    )

wirelessInterfaceChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 1, 5)
)
wirelessInterfaceChannelChanged.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wirelessInterfaceChannelChanged.setStatus(
        "current"
    )

radiusSrvNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 2, 1)
)
radiusSrvNotResponding.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    radiusSrvNotResponding.setStatus(
        "current"
    )

masterAgentExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 3, 1)
)
masterAgentExited.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    masterAgentExited.setStatus(
        "current"
    )

imageDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 3, 2)
)
imageDownloadFailed.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    imageDownloadFailed.setStatus(
        "current"
    )

signatureCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 3, 3)
)
signatureCheckFailed.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    signatureCheckFailed.setStatus(
        "current"
    )

configurationAppliedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 3, 4)
)
configurationAppliedSuccessfully.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    configurationAppliedSuccessfully.setStatus(
        "current"
    )

invalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 1)
)
invalidConfigFile.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    invalidConfigFile.setStatus(
        "current"
    )

cpuUsageThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 2)
)
cpuUsageThresholdExceeded.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    cpuUsageThresholdExceeded.setStatus(
        "current"
    )

flashMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 3)
)
flashMemoryThresholdExceeded.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    flashMemoryThresholdExceeded.setStatus(
        "current"
    )

ramMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 4)
)
ramMemoryThresholdExceeded.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    ramMemoryThresholdExceeded.setStatus(
        "current"
    )

invalidLicenseFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 5)
)
invalidLicenseFile.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    invalidLicenseFile.setStatus(
        "current"
    )

pxmModulesInitSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 6)
)
pxmModulesInitSuccess.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    pxmModulesInitSuccess.setStatus(
        "current"
    )

sysMgmtModulesInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 7)
)
sysMgmtModulesInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    sysMgmtModulesInitFailure.setStatus(
        "current"
    )

vlanModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 8)
)
vlanModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    vlanModuleInitFailure.setStatus(
        "current"
    )

filteringModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 9)
)
filteringModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    filteringModuleInitFailure.setStatus(
        "current"
    )

sysutilsModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 10)
)
sysutilsModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    sysutilsModuleInitFailure.setStatus(
        "current"
    )

tftpModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 11)
)
tftpModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    tftpModuleInitFailure.setStatus(
        "current"
    )

sntpModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 12)
)
sntpModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    sntpModuleInitFailure.setStatus(
        "current"
    )

syslogModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 13)
)
syslogModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    syslogModuleInitFailure.setStatus(
        "current"
    )

wlanModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 14)
)
wlanModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    wlanModuleInitFailure.setStatus(
        "current"
    )

flashModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 15)
)
flashModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    flashModuleInitFailure.setStatus(
        "current"
    )

snmpModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 16)
)
snmpModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    snmpModuleInitFailure.setStatus(
        "current"
    )

systemTempReachedLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 17)
)
systemTempReachedLimits.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    systemTempReachedLimits.setStatus(
        "current"
    )

dhcpRelayModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 18)
)
dhcpRelayModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    dhcpRelayModuleInitFailure.setStatus(
        "current"
    )

dhcpServerModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 19)
)
dhcpServerModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    dhcpServerModuleInitFailure.setStatus(
        "current"
    )

staticNATModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 20)
)
staticNATModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    staticNATModuleInitFailure.setStatus(
        "current"
    )

licenseModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 21)
)
licenseModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    licenseModuleInitFailure.setStatus(
        "current"
    )

systemFeatureModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 22)
)
systemFeatureModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    systemFeatureModuleInitFailure.setStatus(
        "current"
    )

mgmtAccessModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 23)
)
mgmtAccessModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    mgmtAccessModuleInitFailure.setStatus(
        "current"
    )

routingModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 4, 24)
)
routingModuleInitFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    routingModuleInitFailure.setStatus(
        "current"
    )

sntpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 5, 1)
)
sntpFailure.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    sntpFailure.setStatus(
        "current"
    )

invalidImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 841, 1, 1, 3, 6, 6, 1)
)
invalidImage.setObjects(
    ("PROXIM-MIB", "genericTrap")
)
if mibBuilder.loadTexts:
    invalidImage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROXIM-MIB",
    **{"DisplayString20": DisplayString20,
       "DisplayString32": DisplayString32,
       "DisplayString55": DisplayString55,
       "DisplayString80": DisplayString80,
       "InterfaceBitmask": InterfaceBitmask,
       "ObjStatus": ObjStatus,
       "ObjStatusActive": ObjStatusActive,
       "Password": Password,
       "V3Password": V3Password,
       "VlanId": VlanId,
       "WEPKeyType": WEPKeyType,
       "proxim": proxim,
       "wireless": wireless,
       "objects": objects,
       "deviceConfig": deviceConfig,
       "interface": interface,
       "wirelessIf": wirelessIf,
       "wirelessIfPropertiesTable": wirelessIfPropertiesTable,
       "wirelessIfPropertiesTableEntry": wirelessIfPropertiesTableEntry,
       "wirelessIfPropertiesTableIndex": wirelessIfPropertiesTableIndex,
       "wirelessIfPropertiesRadioStatus": wirelessIfPropertiesRadioStatus,
       "wirelessIfOperationalMode": wirelessIfOperationalMode,
       "wirelessIfSupportedOperationalMode": wirelessIfSupportedOperationalMode,
       "wirelessIfCurrentChannelBandwidth": wirelessIfCurrentChannelBandwidth,
       "wirelessIfSupportedChannelBandwidth": wirelessIfSupportedChannelBandwidth,
       "wirelessIfAutoChannelSelection": wirelessIfAutoChannelSelection,
       "wirelessIfCurrentOperatingChannel": wirelessIfCurrentOperatingChannel,
       "wirelessIfSupportedChannels": wirelessIfSupportedChannels,
       "wirelessIfAutoRateSelection": wirelessIfAutoRateSelection,
       "wirelessIfTransmittedRate": wirelessIfTransmittedRate,
       "wirelessIfSupportedRate": wirelessIfSupportedRate,
       "wirelessIfVAPRTSThreshold": wirelessIfVAPRTSThreshold,
       "wirelessIfVAPBeaconInterval": wirelessIfVAPBeaconInterval,
       "wirelessIfTPC": wirelessIfTPC,
       "wirelessIfCellSize": wirelessIfCellSize,
       "wirelessIfDTIM": wirelessIfDTIM,
       "wirelessIfAntennaGain": wirelessIfAntennaGain,
       "wirelessIfCurrentActiveChannel": wirelessIfCurrentActiveChannel,
       "wirelessIfSatelliteDensity": wirelessIfSatelliteDensity,
       "wirelessIfMPOperationalMode": wirelessIfMPOperationalMode,
       "wirelessIfChannelWaitTime": wirelessIfChannelWaitTime,
       "wirelessIfActiveTPC": wirelessIfActiveTPC,
       "wirelessIfDfsNumSatWithRadarForFreqSwitch": wirelessIfDfsNumSatWithRadarForFreqSwitch,
       "wirelessIfDfsStatus": wirelessIfDfsStatus,
       "wirelessIf11nPropertiesTable": wirelessIf11nPropertiesTable,
       "wirelessIf11nPropertiesTableEntry": wirelessIf11nPropertiesTableEntry,
       "wirelessIf11nPropertiesTableIndex": wirelessIf11nPropertiesTableIndex,
       "wirelessIf11nPropertiesAMPDUStatus": wirelessIf11nPropertiesAMPDUStatus,
       "wirelessIf11nPropertiesAMPDUMaxNumFrames": wirelessIf11nPropertiesAMPDUMaxNumFrames,
       "wirelessIf11nPropertiesAMPDUMaxFrameSize": wirelessIf11nPropertiesAMPDUMaxFrameSize,
       "wirelessIf11nPropertiesAMSDUStatus": wirelessIf11nPropertiesAMSDUStatus,
       "wirelessIf11nPropertiesAMSDUMaxFrameSize": wirelessIf11nPropertiesAMSDUMaxFrameSize,
       "wirelessIf11nPropertiesFrequencyExtension": wirelessIf11nPropertiesFrequencyExtension,
       "wirelessIf11nPropertiesGuardInterval": wirelessIf11nPropertiesGuardInterval,
       "wirelessIf11nPropertiesTxAntennas": wirelessIf11nPropertiesTxAntennas,
       "wirelessIf11nPropertiesRxAntennas": wirelessIf11nPropertiesRxAntennas,
       "wirelessIf11nPropertiesNumOfSpatialStreams": wirelessIf11nPropertiesNumOfSpatialStreams,
       "wirelessIf11nPropertiesSupportedTxAntennas": wirelessIf11nPropertiesSupportedTxAntennas,
       "wirelessIf11nPropertiesSupportedRxAntennas": wirelessIf11nPropertiesSupportedRxAntennas,
       "wirelessIfVAPTable": wirelessIfVAPTable,
       "wirelessIfVAPTableEntry": wirelessIfVAPTableEntry,
       "wirelessIfVAPTableIndex": wirelessIfVAPTableIndex,
       "wirelessIfVAPTableSecIndex": wirelessIfVAPTableSecIndex,
       "wirelessIfVAPType": wirelessIfVAPType,
       "wirelessIfVAPSSID": wirelessIfVAPSSID,
       "wirelessIfVAPBSSID": wirelessIfVAPBSSID,
       "wirelessIfVAPBroadcastSSID": wirelessIfVAPBroadcastSSID,
       "wirelessIfVAPFragmentationThreshold": wirelessIfVAPFragmentationThreshold,
       "wirelessIfVAPSecurityProfileName": wirelessIfVAPSecurityProfileName,
       "wirelessIfVAPRadiusProfileName": wirelessIfVAPRadiusProfileName,
       "wirelessIfVAPVLANID": wirelessIfVAPVLANID,
       "wirelessIfVAPVLANPriority": wirelessIfVAPVLANPriority,
       "wirelessIfVAPQoSProfileName": wirelessIfVAPQoSProfileName,
       "wirelessIfVAPMACACLStatus": wirelessIfVAPMACACLStatus,
       "wirelessIfVAPRadiusMACACLStatus": wirelessIfVAPRadiusMACACLStatus,
       "wirelessIfVAPRadiusAccStatus": wirelessIfVAPRadiusAccStatus,
       "wirelessIfVAPStatus": wirelessIfVAPStatus,
       "wirelessIfWORPTable": wirelessIfWORPTable,
       "wirelessIfWORPTableEntry": wirelessIfWORPTableEntry,
       "wirelessIfWORPTableIndex": wirelessIfWORPTableIndex,
       "wirelessIfWORPMode": wirelessIfWORPMode,
       "wirelessIfWORPBaseStationName": wirelessIfWORPBaseStationName,
       "wirelessIfWORPNetworkName": wirelessIfWORPNetworkName,
       "wirelessIfWORPMaxSatellites": wirelessIfWORPMaxSatellites,
       "wirelessIfWORPMTU": wirelessIfWORPMTU,
       "wirelessIfWORPSuperPacketing": wirelessIfWORPSuperPacketing,
       "wirelessIfWORPSleepMode": wirelessIfWORPSleepMode,
       "wirelessIfWORPMultiFrameBursting": wirelessIfWORPMultiFrameBursting,
       "wirelessIfWORPRegistrationTimeout": wirelessIfWORPRegistrationTimeout,
       "wirelessIfWORPRetries": wirelessIfWORPRetries,
       "wirelessIfWORPTxRate": wirelessIfWORPTxRate,
       "wirelessIfWORPSupportedTxRate": wirelessIfWORPSupportedTxRate,
       "wirelessIfWORPInputBandwidthLimit": wirelessIfWORPInputBandwidthLimit,
       "wirelessIfWORPOutputBandwidthLimit": wirelessIfWORPOutputBandwidthLimit,
       "wirelessIfWORPBandwidthLimitType": wirelessIfWORPBandwidthLimitType,
       "wirelessIfWORPSecurityProfileIndex": wirelessIfWORPSecurityProfileIndex,
       "wirelessIfWORPRadiusProfileIndex": wirelessIfWORPRadiusProfileIndex,
       "wirelessIfWORPMACACLStatus": wirelessIfWORPMACACLStatus,
       "wirelessIfWORPRadiusMACACLStatus": wirelessIfWORPRadiusMACACLStatus,
       "wirelessIfWORPRadiusAccStatus": wirelessIfWORPRadiusAccStatus,
       "wirelessIfWORPIntfMacAddress": wirelessIfWORPIntfMacAddress,
       "wirelessIfWORPAutoMultiFrameBursting": wirelessIfWORPAutoMultiFrameBursting,
       "wirelessIfDDRSTable": wirelessIfDDRSTable,
       "wirelessIfDDRSTableEntry": wirelessIfDDRSTableEntry,
       "wirelessIfDDRSTableIndex": wirelessIfDDRSTableIndex,
       "wirelessIfDDRSStatus": wirelessIfDDRSStatus,
       "wirelessIfDDRSDefDataRate": wirelessIfDDRSDefDataRate,
       "wirelessIfDDRSMaxDataRate": wirelessIfDDRSMaxDataRate,
       "wirelessIfDDRSIncrAvgSNRThrld": wirelessIfDDRSIncrAvgSNRThrld,
       "wirelessIfDDRSIncrReqSNRThrld": wirelessIfDDRSIncrReqSNRThrld,
       "wirelessIfDDRSDecrReqSNRThrld": wirelessIfDDRSDecrReqSNRThrld,
       "wirelessIfDDRSIncrReTxPercentThrld": wirelessIfDDRSIncrReTxPercentThrld,
       "wirelessIfDDRSDecrReTxPercentThrld": wirelessIfDDRSDecrReTxPercentThrld,
       "wirelessIfDDRSAggressiveIndex": wirelessIfDDRSAggressiveIndex,
       "wirelessIfDDRSChainBalThrld": wirelessIfDDRSChainBalThrld,
       "wirelessIfDDRSRateBackOffInt": wirelessIfDDRSRateBackOffInt,
       "wirelessIfDDRSRateBlackListInt": wirelessIfDDRSRateBlackListInt,
       "wirelessIfDDRSMinReqSNRTable": wirelessIfDDRSMinReqSNRTable,
       "wirelessIfDDRSMinReqSNRTableEntry": wirelessIfDDRSMinReqSNRTableEntry,
       "wirelessIfDDRSMinReqSNRTableIndex": wirelessIfDDRSMinReqSNRTableIndex,
       "wirelessIfDDRSMinReqSNRTableSecIndex": wirelessIfDDRSMinReqSNRTableSecIndex,
       "wirelessIfDDRSPhyModulation": wirelessIfDDRSPhyModulation,
       "wirelessIfDDRSDataRate": wirelessIfDDRSDataRate,
       "wirelessIfDDRSMinReqSNR": wirelessIfDDRSMinReqSNR,
       "ethernetIf": ethernetIf,
       "ethernetIfPropertiesTable": ethernetIfPropertiesTable,
       "ethernetIfPropertiesTableEntry": ethernetIfPropertiesTableEntry,
       "ethernetIfPropertiesTableIndex": ethernetIfPropertiesTableIndex,
       "ethernetIfMACAddress": ethernetIfMACAddress,
       "ethernetIfSupportedSpeed": ethernetIfSupportedSpeed,
       "ethernetIfSupportedTxMode": ethernetIfSupportedTxMode,
       "ethernetIfTxModeAndSpeed": ethernetIfTxModeAndSpeed,
       "ethernetIfSupportedModes": ethernetIfSupportedModes,
       "ethernetIfAdminStatus": ethernetIfAdminStatus,
       "ethernetIfAutoShutDown": ethernetIfAutoShutDown,
       "apSecurity": apSecurity,
       "wirelessSecurity": wirelessSecurity,
       "wirelessSecurityCfgTable": wirelessSecurityCfgTable,
       "wirelessSecurityCfgTableEntry": wirelessSecurityCfgTableEntry,
       "wirelessSecurityCfgTableIndex": wirelessSecurityCfgTableIndex,
       "wirelessSecurityCfgprofileName": wirelessSecurityCfgprofileName,
       "wirelessSecurityCfgAuthenticationMode": wirelessSecurityCfgAuthenticationMode,
       "wirelessSecurityCfgKeyIndex": wirelessSecurityCfgKeyIndex,
       "wirelessSecurityCfgKey1": wirelessSecurityCfgKey1,
       "wirelessSecurityCfgdot1xWepKeyLength": wirelessSecurityCfgdot1xWepKeyLength,
       "wirelessSecurityCfgEncryptionType": wirelessSecurityCfgEncryptionType,
       "wirelessSecurityCfgPSK": wirelessSecurityCfgPSK,
       "wirelessSecurityCfgRekeyingInterval": wirelessSecurityCfgRekeyingInterval,
       "wirelessSecurityCfgEntryStatus": wirelessSecurityCfgEntryStatus,
       "wirelessSecurityCfgNetworkSecret": wirelessSecurityCfgNetworkSecret,
       "wirelessSecurityCfgKey2": wirelessSecurityCfgKey2,
       "wirelessSecurityCfgKey3": wirelessSecurityCfgKey3,
       "wirelessSecurityCfgKey4": wirelessSecurityCfgKey4,
       "radius": radius,
       "radiusSrvProfileTable": radiusSrvProfileTable,
       "radiusSrvProfileTableEntry": radiusSrvProfileTableEntry,
       "radiusSrvProfileTableIndex": radiusSrvProfileTableIndex,
       "radiusSrvProfileTableSecIndex": radiusSrvProfileTableSecIndex,
       "radiusSrvProfileType": radiusSrvProfileType,
       "radiusSrvIPADDR": radiusSrvIPADDR,
       "radiusSrvServerPort": radiusSrvServerPort,
       "radiusSrvProfileServerSharedSecret": radiusSrvProfileServerSharedSecret,
       "radiusSrvProfileTableEntryStatus": radiusSrvProfileTableEntryStatus,
       "radiusSupProfileTable": radiusSupProfileTable,
       "radiusSupProfileTableEntry": radiusSupProfileTableEntry,
       "radiusSupProfileTableIndex": radiusSupProfileTableIndex,
       "radiusSupProfileName": radiusSupProfileName,
       "radiusSupProfileMaxReTransmissions": radiusSupProfileMaxReTransmissions,
       "radiusSupProfileMsgResponseTime": radiusSupProfileMsgResponseTime,
       "radiusSupProfileReAuthenticationPeriod": radiusSupProfileReAuthenticationPeriod,
       "radiusSupProfileTableEntryStatus": radiusSupProfileTableEntryStatus,
       "macacl": macacl,
       "macaclProfileTable": macaclProfileTable,
       "macaclProfileTableEntry": macaclProfileTableEntry,
       "macaclProfileTableIndex": macaclProfileTableIndex,
       "macaclProfileName": macaclProfileName,
       "macaclOperationType": macaclOperationType,
       "macaclTableEntryStatus": macaclTableEntryStatus,
       "macaclAddrTable": macaclAddrTable,
       "macaclAddrTableEntry": macaclAddrTableEntry,
       "macaclAddrTableIndex": macaclAddrTableIndex,
       "macaclAddrTableSecIndex": macaclAddrTableSecIndex,
       "macaclAddrTableMACAddress": macaclAddrTableMACAddress,
       "macaclAddrComment": macaclAddrComment,
       "macaclAddrTableEntryStatus": macaclAddrTableEntryStatus,
       "qos": qos,
       "qosProfileTable": qosProfileTable,
       "qosProfileTableEntry": qosProfileTableEntry,
       "qosProfileTableIndex": qosProfileTableIndex,
       "qosProfileName": qosProfileName,
       "qosProfileTablePolicyName": qosProfileTablePolicyName,
       "qosProfileEDCAProfileName": qosProfileEDCAProfileName,
       "qosProfileTableQoSNACKStatus": qosProfileTableQoSNACKStatus,
       "qoSPolicyTable": qoSPolicyTable,
       "qoSPolicyTableEntry": qoSPolicyTableEntry,
       "qoSPolicyTableIndex": qoSPolicyTableIndex,
       "qoSPolicyTableSecIndex": qoSPolicyTableSecIndex,
       "qoSPolicyTablePolicyName": qoSPolicyTablePolicyName,
       "qoSPolicyType": qoSPolicyType,
       "qoSPolicyPriorityMapping": qoSPolicyPriorityMapping,
       "qoSPolicyMarkingStatus": qoSPolicyMarkingStatus,
       "qoSPolicyTableEntryStatus": qoSPolicyTableEntryStatus,
       "wirelessQoS": wirelessQoS,
       "wirelessQoSEDCATable": wirelessQoSEDCATable,
       "wirelessQoSEDCATableEntry": wirelessQoSEDCATableEntry,
       "wirelessQoSEDCATableIndex": wirelessQoSEDCATableIndex,
       "wirelessQoSEDCATableSecIndex": wirelessQoSEDCATableSecIndex,
       "wirelessQoSEDCATableProfileName": wirelessQoSEDCATableProfileName,
       "wirelessQoSEDCATableCWmin": wirelessQoSEDCATableCWmin,
       "wirelessQoSEDCATableCWmax": wirelessQoSEDCATableCWmax,
       "wirelessQoSEDCATableAIFSN": wirelessQoSEDCATableAIFSN,
       "wirelessQoSEDCATableTXOP": wirelessQoSEDCATableTXOP,
       "wirelessQoSEDCATableACM": wirelessQoSEDCATableACM,
       "wirelessQoSEDCATableAPCWmin": wirelessQoSEDCATableAPCWmin,
       "wirelessQoSEDCATableAPCWmax": wirelessQoSEDCATableAPCWmax,
       "wirelessQoSEDCATableAPAIFSN": wirelessQoSEDCATableAPAIFSN,
       "wirelessQoSEDCATableAPTXOP": wirelessQoSEDCATableAPTXOP,
       "wirelessQoSEDCATableAPACM": wirelessQoSEDCATableAPACM,
       "l2l3QoS": l2l3QoS,
       "l2l3QoSDot1DToDot1pMappingTable": l2l3QoSDot1DToDot1pMappingTable,
       "l2l3QoSDot1DToDot1pMappingTableEntry": l2l3QoSDot1DToDot1pMappingTableEntry,
       "l2l3QoSDot1DToDot1pMappingTableIndex": l2l3QoSDot1DToDot1pMappingTableIndex,
       "l2l3QoSDot1dPriority": l2l3QoSDot1dPriority,
       "l2l3QoSDot1pPriority": l2l3QoSDot1pPriority,
       "l2l3QoSDot1DToIPDSCPMappingTable": l2l3QoSDot1DToIPDSCPMappingTable,
       "l2l3QoSDot1DToIPDSCPMappingTableEntry": l2l3QoSDot1DToIPDSCPMappingTableEntry,
       "l2l3QoSDot1DToIPDSCPMappingTableIndex": l2l3QoSDot1DToIPDSCPMappingTableIndex,
       "l2l3QoSDot1dPriorityIPDSCP": l2l3QoSDot1dPriorityIPDSCP,
       "l2l3QoSDSCPPriorityLowerLimit": l2l3QoSDSCPPriorityLowerLimit,
       "l2l3QoSDSCPPriorityUpperLimit": l2l3QoSDSCPPriorityUpperLimit,
       "worpQoS": worpQoS,
       "worpQoSPIRMacTable": worpQoSPIRMacTable,
       "worpQoSPIRMacTableEntry": worpQoSPIRMacTableEntry,
       "worpQoSPIRMacTableIndex": worpQoSPIRMacTableIndex,
       "worpQoSPIRMacAddr": worpQoSPIRMacAddr,
       "worpQoSPIRMacMask": worpQoSPIRMacMask,
       "worpQoSPIRMacComment": worpQoSPIRMacComment,
       "worpQoSPIRMacTableEntryStatus": worpQoSPIRMacTableEntryStatus,
       "worpQoSPIRIPTable": worpQoSPIRIPTable,
       "worpQoSPIRIPTableEntry": worpQoSPIRIPTableEntry,
       "worpQoSPIRIPTableIndex": worpQoSPIRIPTableIndex,
       "worpQoSPIRIPAddr": worpQoSPIRIPAddr,
       "worpQoSPIRIPSubMask": worpQoSPIRIPSubMask,
       "worpQoSPIRIPComment": worpQoSPIRIPComment,
       "worpQoSPIRIPTableEntryStatus": worpQoSPIRIPTableEntryStatus,
       "worpQoSPIRPortTable": worpQoSPIRPortTable,
       "worpQoSPIRPortTableEntry": worpQoSPIRPortTableEntry,
       "worpQoSPIRPortTableIndex": worpQoSPIRPortTableIndex,
       "worpQoSPIRStartPort": worpQoSPIRStartPort,
       "worpQoSPIREndPort": worpQoSPIREndPort,
       "worpQoSPIRPortComment": worpQoSPIRPortComment,
       "worpQoSPIRPortTableEntryStatus": worpQoSPIRPortTableEntryStatus,
       "worpQoSPIRMapTable": worpQoSPIRMapTable,
       "worpQoSPIRMapTableEntry": worpQoSPIRMapTableEntry,
       "worpQoSPIRMapTableIndex": worpQoSPIRMapTableIndex,
       "worpQoSPIRMapRuleName": worpQoSPIRMapRuleName,
       "worpQoSPIRMapSrcMacIndexList": worpQoSPIRMapSrcMacIndexList,
       "worpQoSPIRMapDstMacIndexList": worpQoSPIRMapDstMacIndexList,
       "worpQoSPIRMapSrcIpAddrIndexList": worpQoSPIRMapSrcIpAddrIndexList,
       "worpQoSPIRMapDstIpAddrIndexList": worpQoSPIRMapDstIpAddrIndexList,
       "worpQoSPIRMapSrcPortIndexList": worpQoSPIRMapSrcPortIndexList,
       "worpQoSPIRMapDstPortIndexList": worpQoSPIRMapDstPortIndexList,
       "worpQoSPIRTable": worpQoSPIRTable,
       "worpQoSPIRTableEntry": worpQoSPIRTableEntry,
       "worpQoSPIRTableIndex": worpQoSPIRTableIndex,
       "worpQoSPIRRuleName": worpQoSPIRRuleName,
       "worpQoSPIRRuleBitMask": worpQoSPIRRuleBitMask,
       "worpQoSPIRIPToSLow": worpQoSPIRIPToSLow,
       "worpQoSPIRIPToSHigh": worpQoSPIRIPToSHigh,
       "worpQoSPIRIPToSMask": worpQoSPIRIPToSMask,
       "worpQoSPIRIPProtocolIds": worpQoSPIRIPProtocolIds,
       "worpQoSPIREtherPriorityLow": worpQoSPIREtherPriorityLow,
       "worpQoSPIREtherPriorityHigh": worpQoSPIREtherPriorityHigh,
       "worpQoSPIRVlanId": worpQoSPIRVlanId,
       "worpQoSPIREtherType": worpQoSPIREtherType,
       "worpQoSPIREtherValue": worpQoSPIREtherValue,
       "worpQoSPIRPPPoEEncapsulation": worpQoSPIRPPPoEEncapsulation,
       "worpQoSPIRPPPoEProtocolId": worpQoSPIRPPPoEProtocolId,
       "worpQoSPIRMapTableIndexVal": worpQoSPIRMapTableIndexVal,
       "worpQoSPIRTableEntryStatus": worpQoSPIRTableEntryStatus,
       "worpQoSSFClassTable": worpQoSSFClassTable,
       "worpQoSSFClassTableEntry": worpQoSSFClassTableEntry,
       "worpQoSSFClassTableIndex": worpQoSSFClassTableIndex,
       "worpQoSSFClassName": worpQoSSFClassName,
       "worpQoSSFClassSchedularType": worpQoSSFClassSchedularType,
       "worpQoSSFClassDirection": worpQoSSFClassDirection,
       "worpQoSSFClassStatus": worpQoSSFClassStatus,
       "worpQoSSFClassMIR": worpQoSSFClassMIR,
       "worpQoSSFClassCIR": worpQoSSFClassCIR,
       "worpQoSSFClassMaxLatency": worpQoSSFClassMaxLatency,
       "worpQoSSFClassTolerableJitter": worpQoSSFClassTolerableJitter,
       "worpQoSSFClassTrafficPriority": worpQoSSFClassTrafficPriority,
       "worpQoSSFClassNumOfMesgInBurst": worpQoSSFClassNumOfMesgInBurst,
       "worpQoSSFClassTableEntryStatus": worpQoSSFClassTableEntryStatus,
       "worpQoSClassTable": worpQoSClassTable,
       "worpQoSClassTableEntry": worpQoSClassTableEntry,
       "worpQoSClassTableIndex": worpQoSClassTableIndex,
       "worpQoSClassSFCTableIndex": worpQoSClassSFCTableIndex,
       "worpQoSClassPIRTableIndex": worpQoSClassPIRTableIndex,
       "worpQoSClassSFCValue": worpQoSClassSFCValue,
       "worpQoSClassPIRValue": worpQoSClassPIRValue,
       "worpQoSClassName": worpQoSClassName,
       "worpQoSClassPriority": worpQoSClassPriority,
       "worpQoSClassTableEntryStatus": worpQoSClassTableEntryStatus,
       "worpQoSSUTable": worpQoSSUTable,
       "worpQoSSUTableEntry": worpQoSSUTableEntry,
       "worpQoSSUTableIndex": worpQoSSUTableIndex,
       "worpQoSSUMACAddress": worpQoSSUMACAddress,
       "worpQoSSUQoSClassIndex": worpQoSSUQoSClassIndex,
       "worpQoSSUComment": worpQoSSUComment,
       "worpQoSSUTableEntryStatus": worpQoSSUTableEntryStatus,
       "worpQoSDefaultClass": worpQoSDefaultClass,
       "worpQoSL2BroadcastClass": worpQoSL2BroadcastClass,
       "network": network,
       "netIp": netIp,
       "netIpCfgTable": netIpCfgTable,
       "netIpCfgTableEntry": netIpCfgTableEntry,
       "netIpCfgTableIndex": netIpCfgTableIndex,
       "netIpCfgIPAddress": netIpCfgIPAddress,
       "netIpCfgSubnetMask": netIpCfgSubnetMask,
       "netIpCfgDefaultRouterIPAddress": netIpCfgDefaultRouterIPAddress,
       "netIpCfgAddressType": netIpCfgAddressType,
       "netIpWirelessCfgTable": netIpWirelessCfgTable,
       "netIpWirelessCfgTableEntry": netIpWirelessCfgTableEntry,
       "netIpWirelessCfgTableIndex": netIpWirelessCfgTableIndex,
       "netIpWirelessCfgIPAddress": netIpWirelessCfgIPAddress,
       "netIpWirelessCfgSubnetMask": netIpWirelessCfgSubnetMask,
       "netIpStaticRouteTable": netIpStaticRouteTable,
       "netIpStaticRouteTableEntry": netIpStaticRouteTableEntry,
       "netIpStaticRouteTableIndex": netIpStaticRouteTableIndex,
       "netIpStaticRouteDestAddr": netIpStaticRouteDestAddr,
       "netIpStaticRouteMask": netIpStaticRouteMask,
       "netIpStaticRouteNextHop": netIpStaticRouteNextHop,
       "netIpStaticRouteMetric": netIpStaticRouteMetric,
       "netIpStaticRouteTableEntryStatus": netIpStaticRouteTableEntryStatus,
       "netCfg": netCfg,
       "netCfgClearIntfStats": netCfgClearIntfStats,
       "netCfgAllIntfDefaultRouterAddr": netCfgAllIntfDefaultRouterAddr,
       "netCfgSupportedInterfaces": netCfgSupportedInterfaces,
       "netCfgStaticRouteStatus": netCfgStaticRouteStatus,
       "wirelessInActivityTimer": wirelessInActivityTimer,
       "ethernetInActivityTimer": ethernetInActivityTimer,
       "netCfgPrimaryDNSIpAddress": netCfgPrimaryDNSIpAddress,
       "netCfgSecondaryDNSIpAddress": netCfgSecondaryDNSIpAddress,
       "wirelessInActivityTimerInSecs": wirelessInActivityTimerInSecs,
       "nat": nat,
       "natStatus": natStatus,
       "natPortBindingStatus": natPortBindingStatus,
       "natStaticPortBindTable": natStaticPortBindTable,
       "natStaticPortBindTableEntry": natStaticPortBindTableEntry,
       "natStaticPortBindTableIndex": natStaticPortBindTableIndex,
       "natStaticPortBindLocalAddr": natStaticPortBindLocalAddr,
       "natStaticPortBindPortType": natStaticPortBindPortType,
       "natStaticPortBindStartPortNum": natStaticPortBindStartPortNum,
       "natStaticPortBindEndPortNum": natStaticPortBindEndPortNum,
       "natStaticPortBindTableEntryStatus": natStaticPortBindTableEntryStatus,
       "rip": rip,
       "ripConfigStatus": ripConfigStatus,
       "ripConfigTable": ripConfigTable,
       "ripConfigTableEntry": ripConfigTableEntry,
       "ripConfigTableIndex": ripConfigTableIndex,
       "ripInterfaceName": ripInterfaceName,
       "ripInterfaceStatus": ripInterfaceStatus,
       "ripInterfaceAuthType": ripInterfaceAuthType,
       "ripInterfaceAuthKey": ripInterfaceAuthKey,
       "ripInterfaceVersionNum": ripInterfaceVersionNum,
       "ripReceiveOnly": ripReceiveOnly,
       "vlan": vlan,
       "vlanStatus": vlanStatus,
       "mgmtVLANIdentifier": mgmtVLANIdentifier,
       "mgmtVLANPriority": mgmtVLANPriority,
       "vlanEthCfgTable": vlanEthCfgTable,
       "vlanEthCfgTableEntry": vlanEthCfgTableEntry,
       "vlanEthCfgTableIndex": vlanEthCfgTableIndex,
       "vlanMode": vlanMode,
       "accessVLANId": accessVLANId,
       "accessVLANPriority": accessVLANPriority,
       "untaggedFrames": untaggedFrames,
       "vlanEthTrunkTable": vlanEthTrunkTable,
       "vlanEthTrunkTableEntry": vlanEthTrunkTableEntry,
       "vlanEthTrunkTableIndex": vlanEthTrunkTableIndex,
       "vlanEthTrunkTableSecIndex": vlanEthTrunkTableSecIndex,
       "ethVLANTrunkId": ethVLANTrunkId,
       "vlanEthTrunkTableEntryStatus": vlanEthTrunkTableEntryStatus,
       "filtering": filtering,
       "filteringCtrl": filteringCtrl,
       "intraBSSFiltering": intraBSSFiltering,
       "protocolFilter": protocolFilter,
       "etherProtocolFilteringCtrl": etherProtocolFilteringCtrl,
       "etherProtocolFilteringType": etherProtocolFilteringType,
       "etherProtocolFilterTable": etherProtocolFilterTable,
       "etherProtocolFilterTableEntry": etherProtocolFilterTableEntry,
       "etherProtocolFilterTableIndex": etherProtocolFilterTableIndex,
       "etherProtocolFilterProtocolName": etherProtocolFilterProtocolName,
       "etherProtocolFilterProtocolNumber": etherProtocolFilterProtocolNumber,
       "etherprotocolFilterStatus": etherprotocolFilterStatus,
       "etherProtocolFilterTableStatus": etherProtocolFilterTableStatus,
       "staticMACAddrFilter": staticMACAddrFilter,
       "staticMACAddrFilterTable": staticMACAddrFilterTable,
       "staticMACAddrFilterTableEntry": staticMACAddrFilterTableEntry,
       "staticMACAddrFilterTableIndex": staticMACAddrFilterTableIndex,
       "staticMACAddrFilterWiredMACAddress": staticMACAddrFilterWiredMACAddress,
       "staticMACAddrFilterWiredMACMask": staticMACAddrFilterWiredMACMask,
       "staticMACAddrFilterWirelessMACAddress": staticMACAddrFilterWirelessMACAddress,
       "staticMACAddrFilterWirelessMACMask": staticMACAddrFilterWirelessMACMask,
       "staticMACAddrFilterComment": staticMACAddrFilterComment,
       "staticMACAddrFilterTableEntryStatus": staticMACAddrFilterTableEntryStatus,
       "advancedFiltering": advancedFiltering,
       "advancedFilterTable": advancedFilterTable,
       "advancedFilterTableEntry": advancedFilterTableEntry,
       "advancedFilterTableIndex": advancedFilterTableIndex,
       "advancedFilterProtocolName": advancedFilterProtocolName,
       "advancedFilterDirection": advancedFilterDirection,
       "advancedFilterTableEntryStatus": advancedFilterTableEntryStatus,
       "tcpudpPortFilter": tcpudpPortFilter,
       "tcpudpPortFilterCtrl": tcpudpPortFilterCtrl,
       "tcpudpPortFilterTable": tcpudpPortFilterTable,
       "tcpudpPortFilterTableEntry": tcpudpPortFilterTableEntry,
       "tcpudpPortFilterTableIndex": tcpudpPortFilterTableIndex,
       "tcpudpPortFilterProtocolName": tcpudpPortFilterProtocolName,
       "tcpudpPortFilterPortNumber": tcpudpPortFilterPortNumber,
       "tcpudpPortFilterPortType": tcpudpPortFilterPortType,
       "tcpudpPortFilterInterface": tcpudpPortFilterInterface,
       "tcpudpPortFilterTableEntryStatus": tcpudpPortFilterTableEntryStatus,
       "worpIntraCellBlocking": worpIntraCellBlocking,
       "worpIntraCellBlockingStatus": worpIntraCellBlockingStatus,
       "worpIntraCellBlockingMACTable": worpIntraCellBlockingMACTable,
       "worpIntraCellBlockingMACTableEntry": worpIntraCellBlockingMACTableEntry,
       "worpIntraCellBlockingMACTableIndex": worpIntraCellBlockingMACTableIndex,
       "worpIntraCellBlockingMACAddress": worpIntraCellBlockingMACAddress,
       "worpIntraCellBlockingGroupID1": worpIntraCellBlockingGroupID1,
       "worpIntraCellBlockingGroupID2": worpIntraCellBlockingGroupID2,
       "worpIntraCellBlockingGroupID3": worpIntraCellBlockingGroupID3,
       "worpIntraCellBlockingGroupID4": worpIntraCellBlockingGroupID4,
       "worpIntraCellBlockingGroupID5": worpIntraCellBlockingGroupID5,
       "worpIntraCellBlockingGroupID6": worpIntraCellBlockingGroupID6,
       "worpIntraCellBlockingGroupID7": worpIntraCellBlockingGroupID7,
       "worpIntraCellBlockingGroupID8": worpIntraCellBlockingGroupID8,
       "worpIntraCellBlockingGroupID9": worpIntraCellBlockingGroupID9,
       "worpIntraCellBlockingGroupID10": worpIntraCellBlockingGroupID10,
       "worpIntraCellBlockingGroupID11": worpIntraCellBlockingGroupID11,
       "worpIntraCellBlockingGroupID12": worpIntraCellBlockingGroupID12,
       "worpIntraCellBlockingGroupID13": worpIntraCellBlockingGroupID13,
       "worpIntraCellBlockingGroupID14": worpIntraCellBlockingGroupID14,
       "worpIntraCellBlockingGroupID15": worpIntraCellBlockingGroupID15,
       "worpIntraCellBlockingGroupID16": worpIntraCellBlockingGroupID16,
       "worpIntraCellBlockingMACTableEntryStatus": worpIntraCellBlockingMACTableEntryStatus,
       "worpIntraCellBlockingGroupTable": worpIntraCellBlockingGroupTable,
       "worpIntraCellBlockingGroupTableEntry": worpIntraCellBlockingGroupTableEntry,
       "worpIntraCellBlockingGroupTableIndex": worpIntraCellBlockingGroupTableIndex,
       "worpIntraCellBlockingGroupName": worpIntraCellBlockingGroupName,
       "worpIntraCellBlockingGroupTableEntryStatus": worpIntraCellBlockingGroupTableEntryStatus,
       "securityGateway": securityGateway,
       "securityGatewayStatus": securityGatewayStatus,
       "securityGatewayMacAddress": securityGatewayMacAddress,
       "stpFrameForwardStatus": stpFrameForwardStatus,
       "stormThreshold": stormThreshold,
       "stormThresholdTable": stormThresholdTable,
       "stormThresholdTableEntry": stormThresholdTableEntry,
       "stormThresholdTableIndex": stormThresholdTableIndex,
       "stormFilterInterface": stormFilterInterface,
       "stormMulticastThreshold": stormMulticastThreshold,
       "stormBroadcastThreshold": stormBroadcastThreshold,
       "dhcp": dhcp,
       "dhcpServer": dhcpServer,
       "dhcpServerStatus": dhcpServerStatus,
       "dhcpMaxLeaseTime": dhcpMaxLeaseTime,
       "dhcpServerIfTable": dhcpServerIfTable,
       "dhcpServerIfTableEntry": dhcpServerIfTableEntry,
       "dhcpServerIfTableIndex": dhcpServerIfTableIndex,
       "dhcpServerInterfaceType": dhcpServerInterfaceType,
       "dhcpServerNetMask": dhcpServerNetMask,
       "dhcpServerDefaultGateway": dhcpServerDefaultGateway,
       "dhcpServerPrimaryDNS": dhcpServerPrimaryDNS,
       "dhcpServerSecondaryDNS": dhcpServerSecondaryDNS,
       "dhcpServerDefaultLeaseTime": dhcpServerDefaultLeaseTime,
       "dhcpServerIfTableComment": dhcpServerIfTableComment,
       "dhcpServerIfTableEntryStatus": dhcpServerIfTableEntryStatus,
       "dhcpServerIpPoolTable": dhcpServerIpPoolTable,
       "dhcpServerIpPoolTableEntry": dhcpServerIpPoolTableEntry,
       "dhcpServerIpPoolTableIndex": dhcpServerIpPoolTableIndex,
       "dhcpServerIpPoolInterface": dhcpServerIpPoolInterface,
       "dhcpServerIpPoolStartIpAddress": dhcpServerIpPoolStartIpAddress,
       "dhcpServerIpPoolEndIpAddress": dhcpServerIpPoolEndIpAddress,
       "dhcpServerIpPoolTableEntryStatus": dhcpServerIpPoolTableEntryStatus,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayServerTable": dhcpRelayServerTable,
       "dhcpRelayServerTableEntry": dhcpRelayServerTableEntry,
       "dhcpRelayServerTableIndex": dhcpRelayServerTableIndex,
       "dhcpRelayServerIpAddress": dhcpRelayServerIpAddress,
       "dhcpRelayServerTableEntryStatus": dhcpRelayServerTableEntryStatus,
       "sysConf": sysConf,
       "sysTypeTable": sysTypeTable,
       "sysTypeTableEntry": sysTypeTableEntry,
       "sysTypeRadioIfIndex": sysTypeRadioIfIndex,
       "sysTypeMode": sysTypeMode,
       "sysTypeActiveMode": sysTypeActiveMode,
       "sysTypeSupportedMode": sysTypeSupportedMode,
       "sysTypeSupportedFreqDomains": sysTypeSupportedFreqDomains,
       "sysTypeFreqDomain": sysTypeFreqDomain,
       "sysTypeActiveFreqDomain": sysTypeActiveFreqDomain,
       "sysNetworkMode": sysNetworkMode,
       "sysActiveNetworkMode": sysActiveNetworkMode,
       "sysConfCountryCode": sysConfCountryCode,
       "igmp": igmp,
       "igmpSnoopingGlobalStatus": igmpSnoopingGlobalStatus,
       "igmpMembershipAgingTimer": igmpMembershipAgingTimer,
       "igmpRouterPortAgingTimer": igmpRouterPortAgingTimer,
       "igmpForcedFlood": igmpForcedFlood,
       "deviceMgmt": deviceMgmt,
       "sys": sys,
       "sysCountryCode": sysCountryCode,
       "sysInvMgmt": sysInvMgmt,
       "sysInvMgmtComponentTable": sysInvMgmtComponentTable,
       "sysInvMgmtComponentTableEntry": sysInvMgmtComponentTableEntry,
       "sysInvMgmtCompTableIndex": sysInvMgmtCompTableIndex,
       "sysInvMgmtCompSerialNumber": sysInvMgmtCompSerialNumber,
       "sysInvMgmtCompName": sysInvMgmtCompName,
       "sysInvMgmtCompId": sysInvMgmtCompId,
       "sysInvMgmtCompVariant": sysInvMgmtCompVariant,
       "sysInvMgmtCompReleaseVersion": sysInvMgmtCompReleaseVersion,
       "sysInvMgmtCompMajorVersion": sysInvMgmtCompMajorVersion,
       "sysInvMgmtCompMinorVersion": sysInvMgmtCompMinorVersion,
       "sysInvMgmtSecurityID": sysInvMgmtSecurityID,
       "sysInvMgmtDaughterCardAvailability": sysInvMgmtDaughterCardAvailability,
       "sysFeature": sysFeature,
       "sysFeatureCtrlID": sysFeatureCtrlID,
       "sysFeatureNumRadios": sysFeatureNumRadios,
       "sysFeatureFreqBand": sysFeatureFreqBand,
       "sysFeatureOutBandwidth": sysFeatureOutBandwidth,
       "sysFeatureInBandwidth": sysFeatureInBandwidth,
       "sysFeatureOpMode": sysFeatureOpMode,
       "sysLicFeatureTable": sysLicFeatureTable,
       "sysLicFeatureTableEntry": sysLicFeatureTableEntry,
       "sysLicFeatureTableIndex": sysLicFeatureTableIndex,
       "sysLicFeatureType": sysLicFeatureType,
       "sysLicFeatureValue": sysLicFeatureValue,
       "sysFeatureCumulativeBandwidth": sysFeatureCumulativeBandwidth,
       "sysFeatureNumEtherIf": sysFeatureNumEtherIf,
       "sysFeatureBitmap": sysFeatureBitmap,
       "sysFeatureNumOfSatellitesAllowed": sysFeatureNumOfSatellitesAllowed,
       "sysFeatureProductFamily": sysFeatureProductFamily,
       "sysFeatureProductClass": sysFeatureProductClass,
       "sysLicRadioInfoTable": sysLicRadioInfoTable,
       "sysLicRadioInfoTableEntry": sysLicRadioInfoTableEntry,
       "sysLicRadioInfoTableIndex": sysLicRadioInfoTableIndex,
       "sysLicRadioCompID": sysLicRadioCompID,
       "sysLicRadiovariantID": sysLicRadiovariantID,
       "sysLicRadioAntennaType": sysLicRadioAntennaType,
       "sysLicRadioAntennaMimoType": sysLicRadioAntennaMimoType,
       "sysMgmt": sysMgmt,
       "sysMgmtCfgChangeCnt": sysMgmtCfgChangeCnt,
       "sysMgmtCfgCommit": sysMgmtCfgCommit,
       "sysMgmtCfgRestore": sysMgmtCfgRestore,
       "sysMgmtCfgErrorMsg": sysMgmtCfgErrorMsg,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtFactoryReset": sysMgmtFactoryReset,
       "sysMgmtLoadTextConfig": sysMgmtLoadTextConfig,
       "sysInfo": sysInfo,
       "sysContactEmail": sysContactEmail,
       "sysContactPhoneNumber": sysContactPhoneNumber,
       "sysLocationName": sysLocationName,
       "sysGPSLongitude": sysGPSLongitude,
       "sysGPSLatitude": sysGPSLatitude,
       "sysGPSAltitude": sysGPSAltitude,
       "productDescr": productDescr,
       "systemName": systemName,
       "mgmtSnmp": mgmtSnmp,
       "mgmtSnmpReadPassword": mgmtSnmpReadPassword,
       "mgmtSnmpReadWritePassword": mgmtSnmpReadWritePassword,
       "mgmtSnmpAccessTable": mgmtSnmpAccessTable,
       "mgmtSnmpAccessTableEntry": mgmtSnmpAccessTableEntry,
       "mgmtSnmpAccessTableIndex": mgmtSnmpAccessTableIndex,
       "mgmtSnmpTrapHostTable": mgmtSnmpTrapHostTable,
       "mgmtSnmpTrapHostTableEntry": mgmtSnmpTrapHostTableEntry,
       "mgmtSnmpTrapHostTableIndex": mgmtSnmpTrapHostTableIndex,
       "mgmtSnmpTrapHostTableIPAddress": mgmtSnmpTrapHostTableIPAddress,
       "mgmtSnmpTrapHostTablePassword": mgmtSnmpTrapHostTablePassword,
       "mgmtSnmpTrapHostTableComment": mgmtSnmpTrapHostTableComment,
       "mgmtSnmpTrapHostTableEntryStatus": mgmtSnmpTrapHostTableEntryStatus,
       "mgmtSnmpVersion": mgmtSnmpVersion,
       "mgmtSnmpV3SecurityLevel": mgmtSnmpV3SecurityLevel,
       "mgmtSnmpV3AuthProtocol": mgmtSnmpV3AuthProtocol,
       "mgmtSnmpV3AuthPassword": mgmtSnmpV3AuthPassword,
       "mgmtSnmpV3PrivProtocol": mgmtSnmpV3PrivProtocol,
       "mgmtSnmpV3PrivPassword": mgmtSnmpV3PrivPassword,
       "http": http,
       "httpPassword": httpPassword,
       "httpPort": httpPort,
       "telnet": telnet,
       "telnetPassword": telnetPassword,
       "telnetPort": telnetPort,
       "telnetSessions": telnetSessions,
       "tftp": tftp,
       "tftpSrvIpAddress": tftpSrvIpAddress,
       "tftpFileName": tftpFileName,
       "tftpFileType": tftpFileType,
       "tftpOpType": tftpOpType,
       "tftpOpStatus": tftpOpStatus,
       "trapControl": trapControl,
       "genericTrap": genericTrap,
       "globalTrapStatus": globalTrapStatus,
       "mgmtAccessControl": mgmtAccessControl,
       "allIntAccessControl": allIntAccessControl,
       "httpAccessControl": httpAccessControl,
       "httpsAccessControl": httpsAccessControl,
       "snmpAccessControl": snmpAccessControl,
       "telnetAccessControl": telnetAccessControl,
       "sshAccessControl": sshAccessControl,
       "mgmtAccessTableStatus": mgmtAccessTableStatus,
       "mgmtAccessTable": mgmtAccessTable,
       "mgmtAccessTableEntry": mgmtAccessTableEntry,
       "mgmtAccessTableIndex": mgmtAccessTableIndex,
       "mgmtAccessTableIpAddress": mgmtAccessTableIpAddress,
       "mgmtAccessTableEntryStatus": mgmtAccessTableEntryStatus,
       "ssh": ssh,
       "sshPort": sshPort,
       "sshSessions": sshSessions,
       "deviceMon": deviceMon,
       "syslog": syslog,
       "syslogStatus": syslogStatus,
       "syslogPriority": syslogPriority,
       "syslogReset": syslogReset,
       "syslogHostTable": syslogHostTable,
       "syslogHostTableEntry": syslogHostTableEntry,
       "syslogHostTableIndex": syslogHostTableIndex,
       "syslogHostIpAddress": syslogHostIpAddress,
       "syslogHostPort": syslogHostPort,
       "syslogHostComment": syslogHostComment,
       "syslogHostTableEntryStatus": syslogHostTableEntryStatus,
       "eventlog": eventlog,
       "eventLogPriority": eventLogPriority,
       "eventLogReset": eventLogReset,
       "sntp": sntp,
       "sntpStatus": sntpStatus,
       "sntpPrimaryServerName": sntpPrimaryServerName,
       "sntpSecondaryServerName": sntpSecondaryServerName,
       "sntpTimeZone": sntpTimeZone,
       "sntpDayLightSavingTime": sntpDayLightSavingTime,
       "sntpShowCurrentTime": sntpShowCurrentTime,
       "wirelessIfMon": wirelessIfMon,
       "wirelessIfStaStats": wirelessIfStaStats,
       "wirelessIfStaStatsTable": wirelessIfStaStatsTable,
       "wirelessIfStaStatsTableEntry": wirelessIfStaStatsTableEntry,
       "wirelessIfStaStatsTableIndex": wirelessIfStaStatsTableIndex,
       "wirelessIfStaStatsTableSecIndex": wirelessIfStaStatsTableSecIndex,
       "wirelessIfStaStatsIfNumber": wirelessIfStaStatsIfNumber,
       "wirelessIfStaStatsVAPNumber": wirelessIfStaStatsVAPNumber,
       "wirelessIfStaStatsMACAddress": wirelessIfStaStatsMACAddress,
       "wirelessIfStaStatsRxMgmtFrames": wirelessIfStaStatsRxMgmtFrames,
       "wirelessIfStaStatsRxControlFrames": wirelessIfStaStatsRxControlFrames,
       "wirelessIfStaStatsRxUnicastFrames": wirelessIfStaStatsRxUnicastFrames,
       "wirelessIfStaStatsRxMulticastFrames": wirelessIfStaStatsRxMulticastFrames,
       "wirelessIfStaStatsRxBytes": wirelessIfStaStatsRxBytes,
       "wirelessIfStaStatsRxBeacons": wirelessIfStaStatsRxBeacons,
       "wirelessIfStaStatsRxProbeResp": wirelessIfStaStatsRxProbeResp,
       "wirelessIfStaStatsRxDupFrames": wirelessIfStaStatsRxDupFrames,
       "wirelessIfStaStatsRxNoPrivacy": wirelessIfStaStatsRxNoPrivacy,
       "wirelessIfStaStatsRxWepFail": wirelessIfStaStatsRxWepFail,
       "wirelessIfStaStatsRxDeMicFail": wirelessIfStaStatsRxDeMicFail,
       "wirelessIfStaStatsRxDecapFailed": wirelessIfStaStatsRxDecapFailed,
       "wirelessIfStaStatsRxDefragFailed": wirelessIfStaStatsRxDefragFailed,
       "wirelessIfStaStatsRxDisassociationFrames": wirelessIfStaStatsRxDisassociationFrames,
       "wirelessIfStaStatsRxDeauthenticationFrames": wirelessIfStaStatsRxDeauthenticationFrames,
       "wirelessIfStaStatsRxDecryptFailedOnCRC": wirelessIfStaStatsRxDecryptFailedOnCRC,
       "wirelessIfStaStatsRxUnauthPort": wirelessIfStaStatsRxUnauthPort,
       "wirelessIfStaStatsRxUnencrypted": wirelessIfStaStatsRxUnencrypted,
       "wirelessIfStaStatsTxDataFrames": wirelessIfStaStatsTxDataFrames,
       "wirelessIfStaStatsTxMgmtFrames": wirelessIfStaStatsTxMgmtFrames,
       "wirelessIfStaStatsTxUnicastFrames": wirelessIfStaStatsTxUnicastFrames,
       "wirelessIfStaStatsTxMulticastFrames": wirelessIfStaStatsTxMulticastFrames,
       "wirelessIfStaStatsTxBytes": wirelessIfStaStatsTxBytes,
       "wirelessIfStaStatsTxProbeReq": wirelessIfStaStatsTxProbeReq,
       "wirelessIfStaStatsTxEospLost": wirelessIfStaStatsTxEospLost,
       "wirelessIfStaStatsTxPSDiscard": wirelessIfStaStatsTxPSDiscard,
       "wirelessIfStaStatsTxAssociationFrames": wirelessIfStaStatsTxAssociationFrames,
       "wirelessIfStaStatsTxAssociationFailedFrames": wirelessIfStaStatsTxAssociationFailedFrames,
       "wirelessIfStaStatsTxAuthenticationFrames": wirelessIfStaStatsTxAuthenticationFrames,
       "wirelessIfStaStatsTxAuthenticationFailed": wirelessIfStaStatsTxAuthenticationFailed,
       "wirelessIfStaStatsTxDeAuthFrames": wirelessIfStaStatsTxDeAuthFrames,
       "wirelessIfStaStatsTxDeAuthCode": wirelessIfStaStatsTxDeAuthCode,
       "wirelessIfStaStatsTxDisassociation": wirelessIfStaStatsTxDisassociation,
       "wirelessIfStaStatsTxDisassociationCode": wirelessIfStaStatsTxDisassociationCode,
       "wirelessIfStaStatsFrequency": wirelessIfStaStatsFrequency,
       "wirelessIfStaStatsState": wirelessIfStaStatsState,
       "wirelessIfStaStatsRSSI": wirelessIfStaStatsRSSI,
       "wirelessIfStaStatsTxRate": wirelessIfStaStatsTxRate,
       "wirelessIfStaStatsAuthenAlgorithm": wirelessIfStaStatsAuthenAlgorithm,
       "wirelessIfStaStatsAssociationID": wirelessIfStaStatsAssociationID,
       "wirelessIfStaStatsVlanTag": wirelessIfStaStatsVlanTag,
       "wirelessIfStaStatsAssocationTime": wirelessIfStaStatsAssocationTime,
       "wirelessIfStaStatsTxPower": wirelessIfStaStatsTxPower,
       "wirelessIfStaStatsInactivityTimer": wirelessIfStaStatsInactivityTimer,
       "wirelessIfStaStatsStationOperatingMode": wirelessIfStaStatsStationOperatingMode,
       "wirelessIfStaStatsHTCapability": wirelessIfStaStatsHTCapability,
       "wirelessIfWORPStaStatsTable": wirelessIfWORPStaStatsTable,
       "wirelessIfWORPStaStatsTableEntry": wirelessIfWORPStaStatsTableEntry,
       "wirelessIfWORPStaStatsTableIndex": wirelessIfWORPStaStatsTableIndex,
       "wirelessIfWORPStaStatsMacAddress": wirelessIfWORPStaStatsMacAddress,
       "wirelessIfWORPStaStatsSatelliteName": wirelessIfWORPStaStatsSatelliteName,
       "wirelessIfWORPStaStatsAverageLocalSignal": wirelessIfWORPStaStatsAverageLocalSignal,
       "wirelessIfWORPStaStatsAverageLocalNoise": wirelessIfWORPStaStatsAverageLocalNoise,
       "wirelessIfWORPStaStatsAverageRemoteSignal": wirelessIfWORPStaStatsAverageRemoteSignal,
       "wirelessIfWORPStaStatsAverageRemoteNoise": wirelessIfWORPStaStatsAverageRemoteNoise,
       "wirelessIfWORPStaStatsRequestForService": wirelessIfWORPStaStatsRequestForService,
       "wirelessIfWORPStaStatsPollData": wirelessIfWORPStaStatsPollData,
       "wirelessIfWORPStaStatsPollNoData": wirelessIfWORPStaStatsPollNoData,
       "wirelessIfWORPStaStatsReplyData": wirelessIfWORPStaStatsReplyData,
       "wirelessIfWORPStaStatsReplyNoData": wirelessIfWORPStaStatsReplyNoData,
       "wirelessIfWORPStaStatsSendSuccess": wirelessIfWORPStaStatsSendSuccess,
       "wirelessIfWORPStaStatsSendRetries": wirelessIfWORPStaStatsSendRetries,
       "wirelessIfWORPStaStatsSendFailures": wirelessIfWORPStaStatsSendFailures,
       "wirelessIfWORPStaStatsReceiveSuccess": wirelessIfWORPStaStatsReceiveSuccess,
       "wirelessIfWORPStaStatsReceiveRetries": wirelessIfWORPStaStatsReceiveRetries,
       "wirelessIfWORPStaStatsReceiveFailures": wirelessIfWORPStaStatsReceiveFailures,
       "wirelessIfWORPStaStatsPollNoReplies": wirelessIfWORPStaStatsPollNoReplies,
       "wirelessIfWORPStaStatsLocalTxRate": wirelessIfWORPStaStatsLocalTxRate,
       "wirelessIfWORPStaStatsRemoteTxRate": wirelessIfWORPStaStatsRemoteTxRate,
       "wirelessIfWORPStaBridgePort": wirelessIfWORPStaBridgePort,
       "wirelessIfWORPStaStatsAverageLocalSNR": wirelessIfWORPStaStatsAverageLocalSNR,
       "wirelessIfWORPStaStatsAverageRemoteSNR": wirelessIfWORPStaStatsAverageRemoteSNR,
       "wirelessIfWORPStaStatsLocalMimoCtrlSig1": wirelessIfWORPStaStatsLocalMimoCtrlSig1,
       "wirelessIfWORPStaStatsLocalMimoCtrlSig2": wirelessIfWORPStaStatsLocalMimoCtrlSig2,
       "wirelessIfWORPStaStatsLocalMimoCtrlSig3": wirelessIfWORPStaStatsLocalMimoCtrlSig3,
       "wirelessIfWORPStaStatsLocalMimoNoise": wirelessIfWORPStaStatsLocalMimoNoise,
       "wirelessIfWORPStaStatsLocalMimoCtrlSNR1": wirelessIfWORPStaStatsLocalMimoCtrlSNR1,
       "wirelessIfWORPStaStatsLocalMimoCtrlSNR2": wirelessIfWORPStaStatsLocalMimoCtrlSNR2,
       "wirelessIfWORPStaStatsLocalMimoCtrlSNR3": wirelessIfWORPStaStatsLocalMimoCtrlSNR3,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSig1": wirelessIfWORPStaStatsRemoteMimoCtrlSig1,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSig2": wirelessIfWORPStaStatsRemoteMimoCtrlSig2,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSig3": wirelessIfWORPStaStatsRemoteMimoCtrlSig3,
       "wirelessIfWORPStaStatsRemoteMimoNoise": wirelessIfWORPStaStatsRemoteMimoNoise,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSNR1": wirelessIfWORPStaStatsRemoteMimoCtrlSNR1,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSNR2": wirelessIfWORPStaStatsRemoteMimoCtrlSNR2,
       "wirelessIfWORPStaStatsRemoteMimoCtrlSNR3": wirelessIfWORPStaStatsRemoteMimoCtrlSNR3,
       "wirelessIfWORPStaStatsLocalChainBalStatus": wirelessIfWORPStaStatsLocalChainBalStatus,
       "wirelessIfWORPStaStatsRemoteChainBalStatus": wirelessIfWORPStaStatsRemoteChainBalStatus,
       "wirelessIfMonNumOfStaConnected": wirelessIfMonNumOfStaConnected,
       "wirelessIfWORPStats": wirelessIfWORPStats,
       "wirelessIfWORPStatsTable": wirelessIfWORPStatsTable,
       "wirelessIfWORPStatsTableEntry": wirelessIfWORPStatsTableEntry,
       "wirelessIfWORPStatsTableIndex": wirelessIfWORPStatsTableIndex,
       "wirelessIfWORPStatsAverageLocalSignal": wirelessIfWORPStatsAverageLocalSignal,
       "wirelessIfWORPStatsAverageLocalNoise": wirelessIfWORPStatsAverageLocalNoise,
       "wirelessIfWORPStatsAverageRemoteSignal": wirelessIfWORPStatsAverageRemoteSignal,
       "wirelessIfWORPStatsAverageRemoteNoise": wirelessIfWORPStatsAverageRemoteNoise,
       "wirelessIfWORPStatsRemotePartners": wirelessIfWORPStatsRemotePartners,
       "wirelessIfWORPStatsBaseStationAnnounces": wirelessIfWORPStatsBaseStationAnnounces,
       "wirelessIfWORPStatsRequestForService": wirelessIfWORPStatsRequestForService,
       "wirelessIfWORPStatsRegistrationRequests": wirelessIfWORPStatsRegistrationRequests,
       "wirelessIfWORPStatsRegistrationRejects": wirelessIfWORPStatsRegistrationRejects,
       "wirelessIfWORPStatsAuthenticationRequests": wirelessIfWORPStatsAuthenticationRequests,
       "wirelessIfWORPStatsAuthenticationConfirms": wirelessIfWORPStatsAuthenticationConfirms,
       "wirelessIfWORPStatsRegistrationAttempts": wirelessIfWORPStatsRegistrationAttempts,
       "wirelessIfWORPStatsRegistrationIncompletes": wirelessIfWORPStatsRegistrationIncompletes,
       "wirelessIfWORPStatsRegistrationTimeouts": wirelessIfWORPStatsRegistrationTimeouts,
       "wirelessIfWORPStatsRegistrationLastReason": wirelessIfWORPStatsRegistrationLastReason,
       "wirelessIfWORPStatsPollData": wirelessIfWORPStatsPollData,
       "wirelessIfWORPStatsPollNoData": wirelessIfWORPStatsPollNoData,
       "wirelessIfWORPStatsReplyData": wirelessIfWORPStatsReplyData,
       "wirelessIfWORPStatsReplyMoreData": wirelessIfWORPStatsReplyMoreData,
       "wirelessIfWORPStatsReplyNoData": wirelessIfWORPStatsReplyNoData,
       "wirelessIfWORPStatsPollNoReplies": wirelessIfWORPStatsPollNoReplies,
       "wirelessIfWORPStatsSendSuccess": wirelessIfWORPStatsSendSuccess,
       "wirelessIfWORPStatsSendRetries": wirelessIfWORPStatsSendRetries,
       "wirelessIfWORPStatsSendFailures": wirelessIfWORPStatsSendFailures,
       "wirelessIfWORPStatsReceiveSuccess": wirelessIfWORPStatsReceiveSuccess,
       "wirelessIfWORPStatsReceiveRetries": wirelessIfWORPStatsReceiveRetries,
       "wirelessIfWORPStatsReceiveFailures": wirelessIfWORPStatsReceiveFailures,
       "wirelessIfWORPStatsProvisionedUplinkCIR": wirelessIfWORPStatsProvisionedUplinkCIR,
       "wirelessIfWORPStatsProvisionedDownlinkCIR": wirelessIfWORPStatsProvisionedDownlinkCIR,
       "wirelessIfWORPStatsProvisionedUplinkMIR": wirelessIfWORPStatsProvisionedUplinkMIR,
       "wirelessIfWORPStatsProvisionedDownlinkMIR": wirelessIfWORPStatsProvisionedDownlinkMIR,
       "wirelessIfWORPStatsActiveUplinkCIR": wirelessIfWORPStatsActiveUplinkCIR,
       "wirelessIfWORPStatsActiveDownlinkCIR": wirelessIfWORPStatsActiveDownlinkCIR,
       "wirelessIfWORPStatsActiveUplinkMIR": wirelessIfWORPStatsActiveUplinkMIR,
       "wirelessIfWORPStatsActiveDownlinkMIR": wirelessIfWORPStatsActiveDownlinkMIR,
       "wirelessIfWORPStatsCurrentUplinkBandwidth": wirelessIfWORPStatsCurrentUplinkBandwidth,
       "wirelessIfWORPStatsCurrentDownlinkBandwidth": wirelessIfWORPStatsCurrentDownlinkBandwidth,
       "wirelessIfBlacklistInfo": wirelessIfBlacklistInfo,
       "wirelessIfBlacklistInfoTable": wirelessIfBlacklistInfoTable,
       "wirelessIfBlacklistInfoTableEntry": wirelessIfBlacklistInfoTableEntry,
       "wirelessIfBlacklistInfoTableIndex": wirelessIfBlacklistInfoTableIndex,
       "wirelessIfBlacklistInfoTableSecIndex": wirelessIfBlacklistInfoTableSecIndex,
       "wirelessIfBlacklistedChannelNum": wirelessIfBlacklistedChannelNum,
       "wirelessIfBlacklistReason": wirelessIfBlacklistReason,
       "wirelessIfBlacklistTimeElapsed": wirelessIfBlacklistTimeElapsed,
       "wirelessIfWORPLinkTest": wirelessIfWORPLinkTest,
       "wirelessIfWORPLinkTestConfTable": wirelessIfWORPLinkTestConfTable,
       "wirelessIfWORPLinkTestConfTableEntry": wirelessIfWORPLinkTestConfTableEntry,
       "wirelessIfWORPLinkTestConfTableIndex": wirelessIfWORPLinkTestConfTableIndex,
       "wirelessIfWORPLinkTestExploreStatus": wirelessIfWORPLinkTestExploreStatus,
       "wirelessIfWORPLinkTestProgressStatus": wirelessIfWORPLinkTestProgressStatus,
       "wirelessIfWORPLinkTestIdleTimeout": wirelessIfWORPLinkTestIdleTimeout,
       "wirelessIfWORPLinkTestStatsTable": wirelessIfWORPLinkTestStatsTable,
       "wirelessIfWORPLinkTestStatsTableEntry": wirelessIfWORPLinkTestStatsTableEntry,
       "wirelessIfWORPLinkTestStatsTableIndex": wirelessIfWORPLinkTestStatsTableIndex,
       "wirelessIfWORPLinkTestStatsTableSecIndex": wirelessIfWORPLinkTestStatsTableSecIndex,
       "wirelessIfWORPLinkTestStatus": wirelessIfWORPLinkTestStatus,
       "wirelessIfWORPLinkTestStationName": wirelessIfWORPLinkTestStationName,
       "wirelessIfWORPLinkTestMACAddress": wirelessIfWORPLinkTestMACAddress,
       "wirelessIfWORPLinkTestWORPLinkStatus": wirelessIfWORPLinkTestWORPLinkStatus,
       "wirelessIfWORPLinkTestLocalCurSignal": wirelessIfWORPLinkTestLocalCurSignal,
       "wirelessIfWORPLinkTestLocalCurNoise": wirelessIfWORPLinkTestLocalCurNoise,
       "wirelessIfWORPLinkTestLocalCurSNR": wirelessIfWORPLinkTestLocalCurSNR,
       "wirelessIfWORPLinkTestLocalMinSignal": wirelessIfWORPLinkTestLocalMinSignal,
       "wirelessIfWORPLinkTestLocalMinNoise": wirelessIfWORPLinkTestLocalMinNoise,
       "wirelessIfWORPLinkTestLocalMinSNR": wirelessIfWORPLinkTestLocalMinSNR,
       "wirelessIfWORPLinkTestLocalMaxSignal": wirelessIfWORPLinkTestLocalMaxSignal,
       "wirelessIfWORPLinkTestLocalMaxNoise": wirelessIfWORPLinkTestLocalMaxNoise,
       "wirelessIfWORPLinkTestLocalMaxSNR": wirelessIfWORPLinkTestLocalMaxSNR,
       "wirelessIfWORPLinkTestRemoteCurSignal": wirelessIfWORPLinkTestRemoteCurSignal,
       "wirelessIfWORPLinkTestRemoteCurNoise": wirelessIfWORPLinkTestRemoteCurNoise,
       "wirelessIfWORPLinkTestRemoteCurSNR": wirelessIfWORPLinkTestRemoteCurSNR,
       "wirelessIfWORPLinkTestRemoteMinSignal": wirelessIfWORPLinkTestRemoteMinSignal,
       "wirelessIfWORPLinkTestRemoteMinNoise": wirelessIfWORPLinkTestRemoteMinNoise,
       "wirelessIfWORPLinkTestRemoteMinSNR": wirelessIfWORPLinkTestRemoteMinSNR,
       "wirelessIfWORPLinkTestRemoteMaxSignal": wirelessIfWORPLinkTestRemoteMaxSignal,
       "wirelessIfWORPLinkTestRemoteMaxNoise": wirelessIfWORPLinkTestRemoteMaxNoise,
       "wirelessIfWORPLinkTestRemoteMaxSNR": wirelessIfWORPLinkTestRemoteMaxSNR,
       "wirelessIfStats": wirelessIfStats,
       "wirelessIfStatsTable": wirelessIfStatsTable,
       "wirelessIfStatsTableEntry": wirelessIfStatsTableEntry,
       "wirelessIfStatsTableIndex": wirelessIfStatsTableIndex,
       "wirelessIfStatsTxPkts": wirelessIfStatsTxPkts,
       "wirelessIfStatsTxBytes": wirelessIfStatsTxBytes,
       "wirelessIfStatsRxPkts": wirelessIfStatsRxPkts,
       "wirelessIfStatsRxBytes": wirelessIfStatsRxBytes,
       "wirelessIfStatsRxDecryptErrors": wirelessIfStatsRxDecryptErrors,
       "wirelessIfStatsRxCRCErrors": wirelessIfStatsRxCRCErrors,
       "wirelessIfStatsChain0CtlRSSI": wirelessIfStatsChain0CtlRSSI,
       "wirelessIfStatsChain1CtlRSSI": wirelessIfStatsChain1CtlRSSI,
       "wirelessIfStatsChain2CtlRSSI": wirelessIfStatsChain2CtlRSSI,
       "wirelessIfStatsChain0ExtRSSI": wirelessIfStatsChain0ExtRSSI,
       "wirelessIfStatsChain1ExtRSSI": wirelessIfStatsChain1ExtRSSI,
       "wirelessIfStatsChain2ExtRSSI": wirelessIfStatsChain2ExtRSSI,
       "wirelessIfStatsCombinedRSSI": wirelessIfStatsCombinedRSSI,
       "wirelessIfStatsPhyErrors": wirelessIfStatsPhyErrors,
       "wirelessIfStatsRadioReTunes": wirelessIfStatsRadioReTunes,
       "radiusMon": radiusMon,
       "radiusClientStats": radiusClientStats,
       "radiusClientAuthStatsTable": radiusClientAuthStatsTable,
       "radiusClientAuthStatsTableEntry": radiusClientAuthStatsTableEntry,
       "radiusClientAuthStatsTableIndex": radiusClientAuthStatsTableIndex,
       "radiusClientAuthStatsTableSecIndex": radiusClientAuthStatsTableSecIndex,
       "radiusClientAuthStatsRoundTripTime": radiusClientAuthStatsRoundTripTime,
       "radiusClientAuthStatsRequests": radiusClientAuthStatsRequests,
       "radiusClientAuthStatsRetransmissions": radiusClientAuthStatsRetransmissions,
       "radiusClientAuthStatsAccessAccepts": radiusClientAuthStatsAccessAccepts,
       "radiusClientAuthStatsAccessRejects": radiusClientAuthStatsAccessRejects,
       "radiusClientAuthStatsAccessChallenges": radiusClientAuthStatsAccessChallenges,
       "radiusClientAuthStatsResponses": radiusClientAuthStatsResponses,
       "radiusClientAuthStatsMalformedResponses": radiusClientAuthStatsMalformedResponses,
       "radiusClientAuthStatsBadAuthenticators": radiusClientAuthStatsBadAuthenticators,
       "radiusClientAuthStatsTimeouts": radiusClientAuthStatsTimeouts,
       "radiusClientAuthStatsUnknownTypes": radiusClientAuthStatsUnknownTypes,
       "radiusClientAuthStatsPacketsDropped": radiusClientAuthStatsPacketsDropped,
       "radiusClientAccStatsTable": radiusClientAccStatsTable,
       "radiusClientAccStatsTableEntry": radiusClientAccStatsTableEntry,
       "radiusClientAccStatsTableIndex": radiusClientAccStatsTableIndex,
       "radiusClientAccStatsTableSecIndex": radiusClientAccStatsTableSecIndex,
       "radiusClientAccStatsRoundTripTime": radiusClientAccStatsRoundTripTime,
       "radiusClientAccStatsRequests": radiusClientAccStatsRequests,
       "radiusClientAccStatsRetransmissions": radiusClientAccStatsRetransmissions,
       "radiusClientAccStatsResponses": radiusClientAccStatsResponses,
       "radiusClientAccStatsMalformedResponses": radiusClientAccStatsMalformedResponses,
       "radiusClientAccStatsTimeouts": radiusClientAccStatsTimeouts,
       "radiusClientAccStatsUnknownTypes": radiusClientAccStatsUnknownTypes,
       "radiusClientAccStatsPacketsDropped": radiusClientAccStatsPacketsDropped,
       "traps": traps,
       "interfaceTraps": interfaceTraps,
       "wirelessInterfaceCardInitFailure": wirelessInterfaceCardInitFailure,
       "wirelessInterfaceCardRadarInterferenceDetected": wirelessInterfaceCardRadarInterferenceDetected,
       "wirelessInterfaceInvalidRegDomain": wirelessInterfaceInvalidRegDomain,
       "wirelessInterfaceWorldModeCCNotSet": wirelessInterfaceWorldModeCCNotSet,
       "wirelessInterfaceChannelChanged": wirelessInterfaceChannelChanged,
       "securityTraps": securityTraps,
       "radiusSrvNotResponding": radiusSrvNotResponding,
       "operationalTraps": operationalTraps,
       "masterAgentExited": masterAgentExited,
       "imageDownloadFailed": imageDownloadFailed,
       "signatureCheckFailed": signatureCheckFailed,
       "configurationAppliedSuccessfully": configurationAppliedSuccessfully,
       "systemTraps": systemTraps,
       "invalidConfigFile": invalidConfigFile,
       "cpuUsageThresholdExceeded": cpuUsageThresholdExceeded,
       "flashMemoryThresholdExceeded": flashMemoryThresholdExceeded,
       "ramMemoryThresholdExceeded": ramMemoryThresholdExceeded,
       "invalidLicenseFile": invalidLicenseFile,
       "pxmModulesInitSuccess": pxmModulesInitSuccess,
       "sysMgmtModulesInitFailure": sysMgmtModulesInitFailure,
       "vlanModuleInitFailure": vlanModuleInitFailure,
       "filteringModuleInitFailure": filteringModuleInitFailure,
       "sysutilsModuleInitFailure": sysutilsModuleInitFailure,
       "tftpModuleInitFailure": tftpModuleInitFailure,
       "sntpModuleInitFailure": sntpModuleInitFailure,
       "syslogModuleInitFailure": syslogModuleInitFailure,
       "wlanModuleInitFailure": wlanModuleInitFailure,
       "flashModuleInitFailure": flashModuleInitFailure,
       "snmpModuleInitFailure": snmpModuleInitFailure,
       "systemTempReachedLimits": systemTempReachedLimits,
       "dhcpRelayModuleInitFailure": dhcpRelayModuleInitFailure,
       "dhcpServerModuleInitFailure": dhcpServerModuleInitFailure,
       "staticNATModuleInitFailure": staticNATModuleInitFailure,
       "licenseModuleInitFailure": licenseModuleInitFailure,
       "systemFeatureModuleInitFailure": systemFeatureModuleInitFailure,
       "mgmtAccessModuleInitFailure": mgmtAccessModuleInitFailure,
       "routingModuleInitFailure": routingModuleInitFailure,
       "sntpTraps": sntpTraps,
       "sntpFailure": sntpFailure,
       "imageTraps": imageTraps,
       "invalidImage": invalidImage,
       "siteSurvey": siteSurvey,
       "worpSiteSurvey": worpSiteSurvey,
       "worpSiteSurveyOperationTable": worpSiteSurveyOperationTable,
       "worpSiteSurveyOperationTableEntry": worpSiteSurveyOperationTableEntry,
       "worpSiteSurveyOperationTableIndex": worpSiteSurveyOperationTableIndex,
       "worpSiteSurveyOperationIfName": worpSiteSurveyOperationIfName,
       "worpSiteSurveyOperationStatus": worpSiteSurveyOperationStatus,
       "worpSiteSurveyTable": worpSiteSurveyTable,
       "worpSiteSurveyTableEntry": worpSiteSurveyTableEntry,
       "worpSiteSurveyTableIndex": worpSiteSurveyTableIndex,
       "worpSiteSurveyTableSecIndex": worpSiteSurveyTableSecIndex,
       "worpSiteSurveyBaseMACAddress": worpSiteSurveyBaseMACAddress,
       "worpSiteSurveyBaseName": worpSiteSurveyBaseName,
       "worpSiteSurveyMaxSatellitesAllowed": worpSiteSurveyMaxSatellitesAllowed,
       "worpSiteSurveyNumSatellitesRegistered": worpSiteSurveyNumSatellitesRegistered,
       "worpSiteSurveySatelliteRegisteredStatus": worpSiteSurveySatelliteRegisteredStatus,
       "worpSiteSurveyLocalTxRate": worpSiteSurveyLocalTxRate,
       "worpSiteSurveyRemoteTxRate": worpSiteSurveyRemoteTxRate,
       "worpSiteSurveyLocalSignalLevel": worpSiteSurveyLocalSignalLevel,
       "worpSiteSurveyLocalNoiseLevel": worpSiteSurveyLocalNoiseLevel,
       "worpSiteSurveyLocalSNR": worpSiteSurveyLocalSNR,
       "worpSiteSurveyRemoteSignalLevel": worpSiteSurveyRemoteSignalLevel,
       "worpSiteSurveyRemoteNoiseLevel": worpSiteSurveyRemoteNoiseLevel,
       "worpSiteSurveyRemoteSNR": worpSiteSurveyRemoteSNR,
       "worpSiteSurveyChannel": worpSiteSurveyChannel,
       "worpSiteSurveyChannelBandwidth": worpSiteSurveyChannelBandwidth,
       "worpSiteSurveyChannelRxRate": worpSiteSurveyChannelRxRate,
       "worpSiteSurveyBaseBridgePort": worpSiteSurveyBaseBridgePort,
       "worpSiteSurveyLocalMimoCtrlSig1": worpSiteSurveyLocalMimoCtrlSig1,
       "worpSiteSurveyLocalMimoCtrlSig2": worpSiteSurveyLocalMimoCtrlSig2,
       "worpSiteSurveyLocalMimoCtrlSig3": worpSiteSurveyLocalMimoCtrlSig3,
       "worpSiteSurveyLocalMimoNoise": worpSiteSurveyLocalMimoNoise,
       "worpSiteSurveyLocalMimoCtrlSNR1": worpSiteSurveyLocalMimoCtrlSNR1,
       "worpSiteSurveyLocalMimoCtrlSNR2": worpSiteSurveyLocalMimoCtrlSNR2,
       "worpSiteSurveyLocalMimoCtrlSNR3": worpSiteSurveyLocalMimoCtrlSNR3,
       "worpSiteSurveyRemoteMimoCtrlSig1": worpSiteSurveyRemoteMimoCtrlSig1,
       "worpSiteSurveyRemoteMimoCtrlSig2": worpSiteSurveyRemoteMimoCtrlSig2,
       "worpSiteSurveyRemoteMimoCtrlSig3": worpSiteSurveyRemoteMimoCtrlSig3,
       "worpSiteSurveyRemoteMimoNoise": worpSiteSurveyRemoteMimoNoise,
       "worpSiteSurveyRemoteMimoCtrlSNR1": worpSiteSurveyRemoteMimoCtrlSNR1,
       "worpSiteSurveyRemoteMimoCtrlSNR2": worpSiteSurveyRemoteMimoCtrlSNR2,
       "worpSiteSurveyRemoteMimoCtrlSNR3": worpSiteSurveyRemoteMimoCtrlSNR3,
       "worpSiteSurveyLocalChainBalStatus": worpSiteSurveyLocalChainBalStatus,
       "worpSiteSurveyRemoteChainBalStatus": worpSiteSurveyRemoteChainBalStatus,
       "temperature": temperature,
       "currentUnitTemp": currentUnitTemp,
       "highTempThreshold": highTempThreshold,
       "lowTempThreshold": lowTempThreshold,
       "tempLoggingInterval": tempLoggingInterval,
       "tempLogReset": tempLogReset,
       "sysMonitor": sysMonitor,
       "sysMonitorCPUUsage": sysMonitorCPUUsage,
       "sysMonitorRAMUsage": sysMonitorRAMUsage,
       "igmpStats": igmpStats,
       "igmpEthernetSnoopingStats": igmpEthernetSnoopingStats,
       "igmpEth1MCastTable": igmpEth1MCastTable,
       "igmpEth1MCastTableEntry": igmpEth1MCastTableEntry,
       "igmpEth1MCastTableIndex": igmpEth1MCastTableIndex,
       "igmpEth1MCastGrpIp": igmpEth1MCastGrpIp,
       "igmpEth1MCastGrpMACAddr": igmpEth1MCastGrpMACAddr,
       "igmpEth1MCastGrpAgingTimeElapsed": igmpEth1MCastGrpAgingTimeElapsed,
       "igmpEth2MCastTable": igmpEth2MCastTable,
       "igmpEth2MCastTableEntry": igmpEth2MCastTableEntry,
       "igmpEth2MCastTableIndex": igmpEth2MCastTableIndex,
       "igmpEth2MCastGrpIp": igmpEth2MCastGrpIp,
       "igmpEth2MCastGrpMACAddr": igmpEth2MCastGrpMACAddr,
       "igmpEth2MCastGrpAgingTimeElapsed": igmpEth2MCastGrpAgingTimeElapsed,
       "igmpWirelessSnoopingStats": igmpWirelessSnoopingStats,
       "igmpWireless1MCastTable": igmpWireless1MCastTable,
       "igmpWireless1MCastTableEntry": igmpWireless1MCastTableEntry,
       "igmpWireless1MCastTableIndex": igmpWireless1MCastTableIndex,
       "igmpWireless1MCastGrpIp": igmpWireless1MCastGrpIp,
       "igmpWireless1MCastGrpMACAddr": igmpWireless1MCastGrpMACAddr,
       "igmpWireless1MCastGrpAgingTimeElapsed": igmpWireless1MCastGrpAgingTimeElapsed,
       "igmpRouterPortListTable": igmpRouterPortListTable,
       "igmpRouterPortListTableEntry": igmpRouterPortListTableEntry,
       "igmpRouterPortListTableIndex": igmpRouterPortListTableIndex,
       "igmpRouterPortNumber": igmpRouterPortNumber,
       "igmpRouterAgingTimeElapsed": igmpRouterAgingTimeElapsed,
       "debugLog": debugLog,
       "debugLogBitMask": debugLogBitMask,
       "debugLogReset": debugLogReset,
       "debugLogSize": debugLogSize,
       "products": products,
       "ap-800": ap_800,
       "ap-8000": ap_8000,
       "qb-8100": qb_8100,
       "mp-8100": mp_8100,
       "mp-8100-cpe": mp_8100_cpe}
)
