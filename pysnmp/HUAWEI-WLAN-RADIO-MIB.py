# SNMP MIB module (HUAWEI-WLAN-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-RADIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:42 2024
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

(hwApIndex,
 hwApMac,
 hwApRegionIndex) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-DEVICE-MIB",
    "hwApIndex",
    "hwApMac",
    "hwApRegionIndex")

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwRadio = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3)
)
hwRadio.setRevisions(
        ("2014-12-17 11:45",
         "2014-12-16 16:00",
         "2014-12-16 10:15",
         "2014-11-27 14:45",
         "2014-09-28 10:27",
         "2014-09-16 10:08",
         "2014-07-17 14:27",
         "2014-07-11 14:27",
         "2014-07-07 14:49",
         "2014-05-26 18:56",
         "2014-05-06 11:30",
         "2014-02-13 13:30",
         "2014-01-26 13:30",
         "2014-01-13 10:30",
         "2013-10-23 11:41",
         "2013-09-06 15:14",
         "2013-08-21 15:14",
         "2013-05-21 15:14",
         "2010-11-11 10:00",
         "2010-05-25 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRadioProfileTable_Object = MibTable
hwRadioProfileTable = _HwRadioProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1)
)
if mibBuilder.loadTexts:
    hwRadioProfileTable.setStatus("current")
_HwRadioProfileEntry_Object = MibTableRow
hwRadioProfileEntry = _HwRadioProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1)
)
hwRadioProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioProfileName"),
)
if mibBuilder.loadTexts:
    hwRadioProfileEntry.setStatus("current")


class _HwRadioProfileName_Type(OctetString):
    """Custom type hwRadioProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadioProfileName_Type.__name__ = "OctetString"
_HwRadioProfileName_Object = MibTableColumn
hwRadioProfileName = _HwRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 1),
    _HwRadioProfileName_Type()
)
hwRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRadioProfileName.setStatus("current")


class _HwRadioType_Type(Integer32):
    """Custom type hwRadioType based on Integer32"""
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
        *(("auto", 1),
          ("dot11a", 3),
          ("dot11ac", 10),
          ("dot11an", 7),
          ("dot11b", 2),
          ("dot11bg", 6),
          ("dot11bgn", 8),
          ("dot11g", 4),
          ("dot11gn", 9),
          ("dot11n", 5))
    )


_HwRadioType_Type.__name__ = "Integer32"
_HwRadioType_Object = MibTableColumn
hwRadioType = _HwRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 2),
    _HwRadioType_Type()
)
hwRadioType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioType.setStatus("current")


class _HwRadioRateMode_Type(Integer32):
    """Custom type hwRadioRateMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("designate", 2),
          ("unknown", -1))
    )


_HwRadioRateMode_Type.__name__ = "Integer32"
_HwRadioRateMode_Object = MibTableColumn
hwRadioRateMode = _HwRadioRateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 3),
    _HwRadioRateMode_Type()
)
hwRadioRateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRateMode.setStatus("current")


class _HwRadioRateValue_Type(Integer32):
    """Custom type hwRadioRateValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 1),
          ("rate11", 6),
          ("rate12", 7),
          ("rate18", 8),
          ("rate2", 2),
          ("rate22", 9),
          ("rate24", 10),
          ("rate33", 11),
          ("rate36", 12),
          ("rate48", 13),
          ("rate54", 14),
          ("rate55", 3),
          ("rate6", 4),
          ("rate9", 5),
          ("unknown", -1))
    )


_HwRadioRateValue_Type.__name__ = "Integer32"
_HwRadioRateValue_Object = MibTableColumn
hwRadioRateValue = _HwRadioRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 4),
    _HwRadioRateValue_Type()
)
hwRadioRateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioRateValue.setStatus("current")


class _HwRadioChannelMode_Type(Integer32):
    """Custom type hwRadioChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_HwRadioChannelMode_Type.__name__ = "Integer32"
_HwRadioChannelMode_Object = MibTableColumn
hwRadioChannelMode = _HwRadioChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 5),
    _HwRadioChannelMode_Type()
)
hwRadioChannelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioChannelMode.setStatus("current")


class _HwRadioPowerMode_Type(Integer32):
    """Custom type hwRadioPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_HwRadioPowerMode_Type.__name__ = "Integer32"
_HwRadioPowerMode_Object = MibTableColumn
hwRadioPowerMode = _HwRadioPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 6),
    _HwRadioPowerMode_Type()
)
hwRadioPowerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioPowerMode.setStatus("current")
_HwRadioCalibrateInterval_Type = Unsigned32
_HwRadioCalibrateInterval_Object = MibTableColumn
hwRadioCalibrateInterval = _HwRadioCalibrateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 7),
    _HwRadioCalibrateInterval_Type()
)
hwRadioCalibrateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioCalibrateInterval.setStatus("current")
_HwRadioPERThreshold_Type = Unsigned32
_HwRadioPERThreshold_Object = MibTableColumn
hwRadioPERThreshold = _HwRadioPERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 8),
    _HwRadioPERThreshold_Type()
)
hwRadioPERThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioPERThreshold.setStatus("current")
_HwRadioConfictRateThreshold_Type = Unsigned32
_HwRadioConfictRateThreshold_Object = MibTableColumn
hwRadioConfictRateThreshold = _HwRadioConfictRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 9),
    _HwRadioConfictRateThreshold_Type()
)
hwRadioConfictRateThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioConfictRateThreshold.setStatus("current")
_HwRadioRTSThreshold_Type = Unsigned32
_HwRadioRTSThreshold_Object = MibTableColumn
hwRadioRTSThreshold = _HwRadioRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 10),
    _HwRadioRTSThreshold_Type()
)
hwRadioRTSThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioRTSThreshold.setStatus("current")
_HwRadioFragmentThreshold_Type = Unsigned32
_HwRadioFragmentThreshold_Object = MibTableColumn
hwRadioFragmentThreshold = _HwRadioFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 11),
    _HwRadioFragmentThreshold_Type()
)
hwRadioFragmentThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioFragmentThreshold.setStatus("current")
_HwRadioShortFrameRetryTimes_Type = Unsigned32
_HwRadioShortFrameRetryTimes_Object = MibTableColumn
hwRadioShortFrameRetryTimes = _HwRadioShortFrameRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 12),
    _HwRadioShortFrameRetryTimes_Type()
)
hwRadioShortFrameRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioShortFrameRetryTimes.setStatus("current")
_HwRadioLongFrameRetryTimes_Type = Unsigned32
_HwRadioLongFrameRetryTimes_Object = MibTableColumn
hwRadioLongFrameRetryTimes = _HwRadioLongFrameRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 13),
    _HwRadioLongFrameRetryTimes_Type()
)
hwRadioLongFrameRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioLongFrameRetryTimes.setStatus("current")


class _HwRadioSupportShortPreamble_Type(Integer32):
    """Custom type hwRadioSupportShortPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioSupportShortPreamble_Type.__name__ = "Integer32"
_HwRadioSupportShortPreamble_Object = MibTableColumn
hwRadioSupportShortPreamble = _HwRadioSupportShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 14),
    _HwRadioSupportShortPreamble_Type()
)
hwRadioSupportShortPreamble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioSupportShortPreamble.setStatus("current")
_HwRadioDTIMInterval_Type = Unsigned32
_HwRadioDTIMInterval_Object = MibTableColumn
hwRadioDTIMInterval = _HwRadioDTIMInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 15),
    _HwRadioDTIMInterval_Type()
)
hwRadioDTIMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioDTIMInterval.setStatus("current")
_HwRadioBeaconInterval_Type = Unsigned32
_HwRadioBeaconInterval_Object = MibTableColumn
hwRadioBeaconInterval = _HwRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 16),
    _HwRadioBeaconInterval_Type()
)
hwRadioBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioBeaconInterval.setStatus("current")


class _HwRadioWMMProfileName_Type(OctetString):
    """Custom type hwRadioWMMProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadioWMMProfileName_Type.__name__ = "OctetString"
_HwRadioWMMProfileName_Object = MibTableColumn
hwRadioWMMProfileName = _HwRadioWMMProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 17),
    _HwRadioWMMProfileName_Type()
)
hwRadioWMMProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioWMMProfileName.setStatus("current")
_HwRadioProfileRowStatus_Type = RowStatus
_HwRadioProfileRowStatus_Object = MibTableColumn
hwRadioProfileRowStatus = _HwRadioProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 18),
    _HwRadioProfileRowStatus_Type()
)
hwRadioProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioProfileRowStatus.setStatus("current")


class _HwRadio80211nGuardIntervalMode_Type(Integer32):
    """Custom type hwRadio80211nGuardIntervalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("short", 2),
          ("unknown", -1))
    )


_HwRadio80211nGuardIntervalMode_Type.__name__ = "Integer32"
_HwRadio80211nGuardIntervalMode_Object = MibTableColumn
hwRadio80211nGuardIntervalMode = _HwRadio80211nGuardIntervalMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 19),
    _HwRadio80211nGuardIntervalMode_Type()
)
hwRadio80211nGuardIntervalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadio80211nGuardIntervalMode.setStatus("current")


class _HwRadio80211nAMPDUMaxLengthExponent_Type(Integer32):
    """Custom type hwRadio80211nAMPDUMaxLengthExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3),
    )


_HwRadio80211nAMPDUMaxLengthExponent_Type.__name__ = "Integer32"
_HwRadio80211nAMPDUMaxLengthExponent_Object = MibTableColumn
hwRadio80211nAMPDUMaxLengthExponent = _HwRadio80211nAMPDUMaxLengthExponent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 20),
    _HwRadio80211nAMPDUMaxLengthExponent_Type()
)
hwRadio80211nAMPDUMaxLengthExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadio80211nAMPDUMaxLengthExponent.setStatus("current")


class _HwRadioCalibrateEnable_Type(Integer32):
    """Custom type hwRadioCalibrateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HwRadioCalibrateEnable_Type.__name__ = "Integer32"
_HwRadioCalibrateEnable_Object = MibTableColumn
hwRadioCalibrateEnable = _HwRadioCalibrateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 21),
    _HwRadioCalibrateEnable_Type()
)
hwRadioCalibrateEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioCalibrateEnable.setStatus("current")
_HwRadioInterfDetDevice_Type = Integer32
_HwRadioInterfDetDevice_Object = MibTableColumn
hwRadioInterfDetDevice = _HwRadioInterfDetDevice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 22),
    _HwRadioInterfDetDevice_Type()
)
hwRadioInterfDetDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioInterfDetDevice.setStatus("current")
_HwRadioApComInterfThreshold_Type = Integer32
_HwRadioApComInterfThreshold_Object = MibTableColumn
hwRadioApComInterfThreshold = _HwRadioApComInterfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 23),
    _HwRadioApComInterfThreshold_Type()
)
hwRadioApComInterfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioApComInterfThreshold.setStatus("current")
_HwRadioApAdjInterfThreshold_Type = Integer32
_HwRadioApAdjInterfThreshold_Object = MibTableColumn
hwRadioApAdjInterfThreshold = _HwRadioApAdjInterfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 24),
    _HwRadioApAdjInterfThreshold_Type()
)
hwRadioApAdjInterfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioApAdjInterfThreshold.setStatus("current")
_HwRadioStaInterfThreshold_Type = Integer32
_HwRadioStaInterfThreshold_Object = MibTableColumn
hwRadioStaInterfThreshold = _HwRadioStaInterfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 25),
    _HwRadioStaInterfThreshold_Type()
)
hwRadioStaInterfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioStaInterfThreshold.setStatus("current")


class _HwRadioDeviceReportDuration_Type(Integer32):
    """Custom type hwRadioDeviceReportDuration based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_HwRadioDeviceReportDuration_Type.__name__ = "Integer32"
_HwRadioDeviceReportDuration_Object = MibTableColumn
hwRadioDeviceReportDuration = _HwRadioDeviceReportDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 26),
    _HwRadioDeviceReportDuration_Type()
)
hwRadioDeviceReportDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioDeviceReportDuration.setStatus("current")
if mibBuilder.loadTexts:
    hwRadioDeviceReportDuration.setUnits("second")


class _HwRadioRTSMode_Type(Integer32):
    """Custom type hwRadioRTSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsToSelf", 2),
          ("disable", 1),
          ("rtsCts", 3))
    )


_HwRadioRTSMode_Type.__name__ = "Integer32"
_HwRadioRTSMode_Object = MibTableColumn
hwRadioRTSMode = _HwRadioRTSMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 27),
    _HwRadioRTSMode_Type()
)
hwRadioRTSMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioRTSMode.setStatus("current")


class _HwRadioWifiLight_Type(Integer32):
    """Custom type hwRadioWifiLight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signalStrength", 1),
          ("traffic", 2))
    )


_HwRadioWifiLight_Type.__name__ = "Integer32"
_HwRadioWifiLight_Object = MibTableColumn
hwRadioWifiLight = _HwRadioWifiLight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 28),
    _HwRadioWifiLight_Type()
)
hwRadioWifiLight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioWifiLight.setStatus("current")


class _HwRadioBeamformingSwitch_Type(Integer32):
    """Custom type hwRadioBeamformingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioBeamformingSwitch_Type.__name__ = "Integer32"
_HwRadioBeamformingSwitch_Object = MibTableColumn
hwRadioBeamformingSwitch = _HwRadioBeamformingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 29),
    _HwRadioBeamformingSwitch_Type()
)
hwRadioBeamformingSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioBeamformingSwitch.setStatus("current")
_HwRadioWidsDevSynchronizationInt_Type = Integer32
_HwRadioWidsDevSynchronizationInt_Object = MibTableColumn
hwRadioWidsDevSynchronizationInt = _HwRadioWidsDevSynchronizationInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 30),
    _HwRadioWidsDevSynchronizationInt_Type()
)
hwRadioWidsDevSynchronizationInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioWidsDevSynchronizationInt.setStatus("current")


class _HwRadioChannelSwitchAnnouncement_Type(Integer32):
    """Custom type hwRadioChannelSwitchAnnouncement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioChannelSwitchAnnouncement_Type.__name__ = "Integer32"
_HwRadioChannelSwitchAnnouncement_Object = MibTableColumn
hwRadioChannelSwitchAnnouncement = _HwRadioChannelSwitchAnnouncement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 31),
    _HwRadioChannelSwitchAnnouncement_Type()
)
hwRadioChannelSwitchAnnouncement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioChannelSwitchAnnouncement.setStatus("current")


class _HwRadioChannelSwitchMode_Type(Integer32):
    """Custom type hwRadioChannelSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continueTransmitting", 1),
          ("stopTransmitting", 2))
    )


_HwRadioChannelSwitchMode_Type.__name__ = "Integer32"
_HwRadioChannelSwitchMode_Object = MibTableColumn
hwRadioChannelSwitchMode = _HwRadioChannelSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 32),
    _HwRadioChannelSwitchMode_Type()
)
hwRadioChannelSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioChannelSwitchMode.setStatus("current")


class _HwRadioStaAccessSignalStrengthSwitch_Type(Integer32):
    """Custom type hwRadioStaAccessSignalStrengthSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioStaAccessSignalStrengthSwitch_Type.__name__ = "Integer32"
_HwRadioStaAccessSignalStrengthSwitch_Object = MibTableColumn
hwRadioStaAccessSignalStrengthSwitch = _HwRadioStaAccessSignalStrengthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 33),
    _HwRadioStaAccessSignalStrengthSwitch_Type()
)
hwRadioStaAccessSignalStrengthSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioStaAccessSignalStrengthSwitch.setStatus("current")
_HwRadioStaAccessSignalStrengthThreshold_Type = Integer32
_HwRadioStaAccessSignalStrengthThreshold_Object = MibTableColumn
hwRadioStaAccessSignalStrengthThreshold = _HwRadioStaAccessSignalStrengthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 34),
    _HwRadioStaAccessSignalStrengthThreshold_Type()
)
hwRadioStaAccessSignalStrengthThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioStaAccessSignalStrengthThreshold.setStatus("current")


class _HwRadioBackgroundListenNeighborSwitch_Type(Integer32):
    """Custom type hwRadioBackgroundListenNeighborSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioBackgroundListenNeighborSwitch_Type.__name__ = "Integer32"
_HwRadioBackgroundListenNeighborSwitch_Object = MibTableColumn
hwRadioBackgroundListenNeighborSwitch = _HwRadioBackgroundListenNeighborSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 35),
    _HwRadioBackgroundListenNeighborSwitch_Type()
)
hwRadioBackgroundListenNeighborSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioBackgroundListenNeighborSwitch.setStatus("current")
_HwRadioBackgroundScanningServiceThreshold_Type = Integer32
_HwRadioBackgroundScanningServiceThreshold_Object = MibTableColumn
hwRadioBackgroundScanningServiceThreshold = _HwRadioBackgroundScanningServiceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 36),
    _HwRadioBackgroundScanningServiceThreshold_Type()
)
hwRadioBackgroundScanningServiceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBackgroundScanningServiceThreshold.setStatus("current")
_HwRadioBackgroundScanningClientThreshold_Type = Integer32
_HwRadioBackgroundScanningClientThreshold_Object = MibTableColumn
hwRadioBackgroundScanningClientThreshold = _HwRadioBackgroundScanningClientThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 37),
    _HwRadioBackgroundScanningClientThreshold_Type()
)
hwRadioBackgroundScanningClientThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBackgroundScanningClientThreshold.setStatus("current")


class _HwRadioStaAccessRateLimitSwitch_Type(Integer32):
    """Custom type hwRadioStaAccessRateLimitSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("unknown", -1))
    )


_HwRadioStaAccessRateLimitSwitch_Type.__name__ = "Integer32"
_HwRadioStaAccessRateLimitSwitch_Object = MibTableColumn
hwRadioStaAccessRateLimitSwitch = _HwRadioStaAccessRateLimitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 38),
    _HwRadioStaAccessRateLimitSwitch_Type()
)
hwRadioStaAccessRateLimitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaAccessRateLimitSwitch.setStatus("current")


class _HwRadioStaAccessRateLimitThreshold_Type(Integer32):
    """Custom type hwRadioStaAccessRateLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 1),
          ("rate11", 6),
          ("rate12", 7),
          ("rate18", 8),
          ("rate2", 2),
          ("rate22", 9),
          ("rate24", 10),
          ("rate33", 11),
          ("rate36", 12),
          ("rate48", 13),
          ("rate54", 14),
          ("rate55", 3),
          ("rate6", 4),
          ("rate9", 5),
          ("unknown", -1))
    )


_HwRadioStaAccessRateLimitThreshold_Type.__name__ = "Integer32"
_HwRadioStaAccessRateLimitThreshold_Object = MibTableColumn
hwRadioStaAccessRateLimitThreshold = _HwRadioStaAccessRateLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 39),
    _HwRadioStaAccessRateLimitThreshold_Type()
)
hwRadioStaAccessRateLimitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaAccessRateLimitThreshold.setStatus("current")
_HwRadioSpectrumAnalysisScanPeriod_Type = Integer32
_HwRadioSpectrumAnalysisScanPeriod_Object = MibTableColumn
hwRadioSpectrumAnalysisScanPeriod = _HwRadioSpectrumAnalysisScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 40),
    _HwRadioSpectrumAnalysisScanPeriod_Type()
)
hwRadioSpectrumAnalysisScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioSpectrumAnalysisScanPeriod.setStatus("current")
_HwRadioSpectrumAnalysisScanInterval_Type = Integer32
_HwRadioSpectrumAnalysisScanInterval_Object = MibTableColumn
hwRadioSpectrumAnalysisScanInterval = _HwRadioSpectrumAnalysisScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 41),
    _HwRadioSpectrumAnalysisScanInterval_Type()
)
hwRadioSpectrumAnalysisScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioSpectrumAnalysisScanInterval.setStatus("current")


class _HwRadioHighDenseSwitch_Type(Integer32):
    """Custom type hwRadioHighDenseSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioHighDenseSwitch_Type.__name__ = "Integer32"
_HwRadioHighDenseSwitch_Object = MibTableColumn
hwRadioHighDenseSwitch = _HwRadioHighDenseSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 42),
    _HwRadioHighDenseSwitch_Type()
)
hwRadioHighDenseSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioHighDenseSwitch.setStatus("current")
_HwRadioHighDenseMode_Type = Integer32
_HwRadioHighDenseMode_Object = MibTableColumn
hwRadioHighDenseMode = _HwRadioHighDenseMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 43),
    _HwRadioHighDenseMode_Type()
)
hwRadioHighDenseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioHighDenseMode.setStatus("current")


class _HwRadioStaOfflineSignalStrengthSwitch_Type(Integer32):
    """Custom type hwRadioStaOfflineSignalStrengthSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioStaOfflineSignalStrengthSwitch_Type.__name__ = "Integer32"
_HwRadioStaOfflineSignalStrengthSwitch_Object = MibTableColumn
hwRadioStaOfflineSignalStrengthSwitch = _HwRadioStaOfflineSignalStrengthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 44),
    _HwRadioStaOfflineSignalStrengthSwitch_Type()
)
hwRadioStaOfflineSignalStrengthSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaOfflineSignalStrengthSwitch.setStatus("current")


class _HwRadioStaOfflineSignalStrengthThreshold_Type(Integer32):
    """Custom type hwRadioStaOfflineSignalStrengthThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_HwRadioStaOfflineSignalStrengthThreshold_Type.__name__ = "Integer32"
_HwRadioStaOfflineSignalStrengthThreshold_Object = MibTableColumn
hwRadioStaOfflineSignalStrengthThreshold = _HwRadioStaOfflineSignalStrengthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 45),
    _HwRadioStaOfflineSignalStrengthThreshold_Type()
)
hwRadioStaOfflineSignalStrengthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaOfflineSignalStrengthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwRadioStaOfflineSignalStrengthThreshold.setUnits("dbm")


class _HwRadioStaOfflineRateLimitSwitch_Type(Integer32):
    """Custom type hwRadioStaOfflineRateLimitSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioStaOfflineRateLimitSwitch_Type.__name__ = "Integer32"
_HwRadioStaOfflineRateLimitSwitch_Object = MibTableColumn
hwRadioStaOfflineRateLimitSwitch = _HwRadioStaOfflineRateLimitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 46),
    _HwRadioStaOfflineRateLimitSwitch_Type()
)
hwRadioStaOfflineRateLimitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaOfflineRateLimitSwitch.setStatus("current")


class _HwRadioStaOfflineRateThreshold_Type(Integer32):
    """Custom type hwRadioStaOfflineRateThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwRadioStaOfflineRateThreshold_Type.__name__ = "Integer32"
_HwRadioStaOfflineRateThreshold_Object = MibTableColumn
hwRadioStaOfflineRateThreshold = _HwRadioStaOfflineRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 47),
    _HwRadioStaOfflineRateThreshold_Type()
)
hwRadioStaOfflineRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioStaOfflineRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwRadioStaOfflineRateThreshold.setUnits("%")


class _HwRadioDynamicAdjustPowerSwitch_Type(Integer32):
    """Custom type hwRadioDynamicAdjustPowerSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioDynamicAdjustPowerSwitch_Type.__name__ = "Integer32"
_HwRadioDynamicAdjustPowerSwitch_Object = MibTableColumn
hwRadioDynamicAdjustPowerSwitch = _HwRadioDynamicAdjustPowerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 48),
    _HwRadioDynamicAdjustPowerSwitch_Type()
)
hwRadioDynamicAdjustPowerSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioDynamicAdjustPowerSwitch.setStatus("current")
_HwRadioLocationReportTime_Type = Integer32
_HwRadioLocationReportTime_Object = MibTableColumn
hwRadioLocationReportTime = _HwRadioLocationReportTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 49),
    _HwRadioLocationReportTime_Type()
)
hwRadioLocationReportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationReportTime.setStatus("current")
_HwRadioLocationScanInterval_Type = Integer32
_HwRadioLocationScanInterval_Object = MibTableColumn
hwRadioLocationScanInterval = _HwRadioLocationScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 50),
    _HwRadioLocationScanInterval_Type()
)
hwRadioLocationScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationScanInterval.setStatus("current")
_HwRadioLocationScanPeriod_Type = Integer32
_HwRadioLocationScanPeriod_Object = MibTableColumn
hwRadioLocationScanPeriod = _HwRadioLocationScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 51),
    _HwRadioLocationScanPeriod_Type()
)
hwRadioLocationScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationScanPeriod.setStatus("current")


class _HwRadioAirTimeScheduleSwitch_Type(Integer32):
    """Custom type hwRadioAirTimeScheduleSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioAirTimeScheduleSwitch_Type.__name__ = "Integer32"
_HwRadioAirTimeScheduleSwitch_Object = MibTableColumn
hwRadioAirTimeScheduleSwitch = _HwRadioAirTimeScheduleSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 52),
    _HwRadioAirTimeScheduleSwitch_Type()
)
hwRadioAirTimeScheduleSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAirTimeScheduleSwitch.setStatus("current")
_HwRadioCalibrateScanCycle_Type = Unsigned32
_HwRadioCalibrateScanCycle_Object = MibTableColumn
hwRadioCalibrateScanCycle = _HwRadioCalibrateScanCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 53),
    _HwRadioCalibrateScanCycle_Type()
)
hwRadioCalibrateScanCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateScanCycle.setStatus("current")


class _HwRadioUacPolicyType_Type(Integer32):
    """Custom type hwRadioUacPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelUtilization", 2),
          ("users", 1))
    )


_HwRadioUacPolicyType_Type.__name__ = "Integer32"
_HwRadioUacPolicyType_Object = MibTableColumn
hwRadioUacPolicyType = _HwRadioUacPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 54),
    _HwRadioUacPolicyType_Type()
)
hwRadioUacPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUacPolicyType.setStatus("current")


class _HwRadioUacPolicySwitch_Type(Integer32):
    """Custom type hwRadioUacPolicySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioUacPolicySwitch_Type.__name__ = "Integer32"
_HwRadioUacPolicySwitch_Object = MibTableColumn
hwRadioUacPolicySwitch = _HwRadioUacPolicySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 55),
    _HwRadioUacPolicySwitch_Type()
)
hwRadioUacPolicySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUacPolicySwitch.setStatus("current")
_HwRadioUacAccessThreshold_Type = Integer32
_HwRadioUacAccessThreshold_Object = MibTableColumn
hwRadioUacAccessThreshold = _HwRadioUacAccessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 56),
    _HwRadioUacAccessThreshold_Type()
)
hwRadioUacAccessThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUacAccessThreshold.setStatus("current")
_HwRadioUacRoamThreshold_Type = Integer32
_HwRadioUacRoamThreshold_Object = MibTableColumn
hwRadioUacRoamThreshold = _HwRadioUacRoamThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 57),
    _HwRadioUacRoamThreshold_Type()
)
hwRadioUacRoamThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUacRoamThreshold.setStatus("current")


class _HwRadioUacHideSSIDSwitch_Type(Integer32):
    """Custom type hwRadioUacHideSSIDSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioUacHideSSIDSwitch_Type.__name__ = "Integer32"
_HwRadioUacHideSSIDSwitch_Object = MibTableColumn
hwRadioUacHideSSIDSwitch = _HwRadioUacHideSSIDSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 58),
    _HwRadioUacHideSSIDSwitch_Type()
)
hwRadioUacHideSSIDSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUacHideSSIDSwitch.setStatus("current")


class _HwRadio80211acGuardIntervalMode_Type(Integer32):
    """Custom type hwRadio80211acGuardIntervalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("short", 2),
          ("unknown", -1))
    )


_HwRadio80211acGuardIntervalMode_Type.__name__ = "Integer32"
_HwRadio80211acGuardIntervalMode_Object = MibTableColumn
hwRadio80211acGuardIntervalMode = _HwRadio80211acGuardIntervalMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 59),
    _HwRadio80211acGuardIntervalMode_Type()
)
hwRadio80211acGuardIntervalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadio80211acGuardIntervalMode.setStatus("current")


class _HwRadio80211acAMPDUMaxLengthExponent_Type(Integer32):
    """Custom type hwRadio80211acAMPDUMaxLengthExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_HwRadio80211acAMPDUMaxLengthExponent_Type.__name__ = "Integer32"
_HwRadio80211acAMPDUMaxLengthExponent_Object = MibTableColumn
hwRadio80211acAMPDUMaxLengthExponent = _HwRadio80211acAMPDUMaxLengthExponent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 60),
    _HwRadio80211acAMPDUMaxLengthExponent_Type()
)
hwRadio80211acAMPDUMaxLengthExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadio80211acAMPDUMaxLengthExponent.setStatus("current")


class _HwRadio80211bgBasicRateSet_Type(OctetString):
    """Custom type hwRadio80211bgBasicRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwRadio80211bgBasicRateSet_Type.__name__ = "OctetString"
_HwRadio80211bgBasicRateSet_Object = MibTableColumn
hwRadio80211bgBasicRateSet = _HwRadio80211bgBasicRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 61),
    _HwRadio80211bgBasicRateSet_Type()
)
hwRadio80211bgBasicRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211bgBasicRateSet.setStatus("current")


class _HwRadio80211bgSupportRateSet_Type(OctetString):
    """Custom type hwRadio80211bgSupportRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwRadio80211bgSupportRateSet_Type.__name__ = "OctetString"
_HwRadio80211bgSupportRateSet_Object = MibTableColumn
hwRadio80211bgSupportRateSet = _HwRadio80211bgSupportRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 62),
    _HwRadio80211bgSupportRateSet_Type()
)
hwRadio80211bgSupportRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211bgSupportRateSet.setStatus("current")


class _HwRadio80211aBasicRateSet_Type(OctetString):
    """Custom type hwRadio80211aBasicRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwRadio80211aBasicRateSet_Type.__name__ = "OctetString"
_HwRadio80211aBasicRateSet_Object = MibTableColumn
hwRadio80211aBasicRateSet = _HwRadio80211aBasicRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 63),
    _HwRadio80211aBasicRateSet_Type()
)
hwRadio80211aBasicRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211aBasicRateSet.setStatus("current")


class _HwRadio80211aSupportRateSet_Type(OctetString):
    """Custom type hwRadio80211aSupportRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwRadio80211aSupportRateSet_Type.__name__ = "OctetString"
_HwRadio80211aSupportRateSet_Object = MibTableColumn
hwRadio80211aSupportRateSet = _HwRadio80211aSupportRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 64),
    _HwRadio80211aSupportRateSet_Type()
)
hwRadio80211aSupportRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211aSupportRateSet.setStatus("current")


class _HwRadio80211nSupportMCS_Type(OctetString):
    """Custom type hwRadio80211nSupportMCS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwRadio80211nSupportMCS_Type.__name__ = "OctetString"
_HwRadio80211nSupportMCS_Object = MibTableColumn
hwRadio80211nSupportMCS = _HwRadio80211nSupportMCS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 65),
    _HwRadio80211nSupportMCS_Type()
)
hwRadio80211nSupportMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211nSupportMCS.setStatus("current")


class _HwRadio80211acSupportMcsMapMcs_Type(OctetString):
    """Custom type hwRadio80211acSupportMcsMapMcs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwRadio80211acSupportMcsMapMcs_Type.__name__ = "OctetString"
_HwRadio80211acSupportMcsMapMcs_Object = MibTableColumn
hwRadio80211acSupportMcsMapMcs = _HwRadio80211acSupportMcsMapMcs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 67),
    _HwRadio80211acSupportMcsMapMcs_Type()
)
hwRadio80211acSupportMcsMapMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211acSupportMcsMapMcs.setStatus("current")


class _HwRadioMulticastRate2G_Type(Integer32):
    """Custom type hwRadioMulticastRate2G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(18, 18),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(54, 54),
    )


_HwRadioMulticastRate2G_Type.__name__ = "Integer32"
_HwRadioMulticastRate2G_Object = MibTableColumn
hwRadioMulticastRate2G = _HwRadioMulticastRate2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 68),
    _HwRadioMulticastRate2G_Type()
)
hwRadioMulticastRate2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMulticastRate2G.setStatus("current")


class _HwRadioMulticastRate5G_Type(Integer32):
    """Custom type hwRadioMulticastRate5G based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(18, 18),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(54, 54),
    )


_HwRadioMulticastRate5G_Type.__name__ = "Integer32"
_HwRadioMulticastRate5G_Object = MibTableColumn
hwRadioMulticastRate5G = _HwRadioMulticastRate5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 69),
    _HwRadioMulticastRate5G_Type()
)
hwRadioMulticastRate5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMulticastRate5G.setStatus("current")


class _HwRadioLegacyStationEnable_Type(Integer32):
    """Custom type hwRadioLegacyStationEnable based on Integer32"""
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


_HwRadioLegacyStationEnable_Type.__name__ = "Integer32"
_HwRadioLegacyStationEnable_Object = MibTableColumn
hwRadioLegacyStationEnable = _HwRadioLegacyStationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 70),
    _HwRadioLegacyStationEnable_Type()
)
hwRadioLegacyStationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioLegacyStationEnable.setStatus("current")


class _HwRadioLocationScanChannel2G_Type(Integer32):
    """Custom type hwRadioLocationScanChannel2G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("countrychannel", 1),
          ("dcachannel", 2))
    )


_HwRadioLocationScanChannel2G_Type.__name__ = "Integer32"
_HwRadioLocationScanChannel2G_Object = MibTableColumn
hwRadioLocationScanChannel2G = _HwRadioLocationScanChannel2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 71),
    _HwRadioLocationScanChannel2G_Type()
)
hwRadioLocationScanChannel2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationScanChannel2G.setStatus("current")


class _HwRadioLocationScanChannel5G_Type(Integer32):
    """Custom type hwRadioLocationScanChannel5G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("countrychannel", 1),
          ("dcachannel", 2))
    )


_HwRadioLocationScanChannel5G_Type.__name__ = "Integer32"
_HwRadioLocationScanChannel5G_Object = MibTableColumn
hwRadioLocationScanChannel5G = _HwRadioLocationScanChannel5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 72),
    _HwRadioLocationScanChannel5G_Type()
)
hwRadioLocationScanChannel5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationScanChannel5G.setStatus("current")


class _HwRadioAMSDUTxEnable_Type(Integer32):
    """Custom type hwRadioAMSDUTxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioAMSDUTxEnable_Type.__name__ = "Integer32"
_HwRadioAMSDUTxEnable_Object = MibTableColumn
hwRadioAMSDUTxEnable = _HwRadioAMSDUTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 73),
    _HwRadioAMSDUTxEnable_Type()
)
hwRadioAMSDUTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioAMSDUTxEnable.setStatus("current")


class _HwRadioAMSDUTxMaxSubFrames_Type(Integer32):
    """Custom type hwRadioAMSDUTxMaxSubFrames based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_HwRadioAMSDUTxMaxSubFrames_Type.__name__ = "Integer32"
_HwRadioAMSDUTxMaxSubFrames_Object = MibTableColumn
hwRadioAMSDUTxMaxSubFrames = _HwRadioAMSDUTxMaxSubFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 1, 1, 74),
    _HwRadioAMSDUTxMaxSubFrames_Type()
)
hwRadioAMSDUTxMaxSubFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioAMSDUTxMaxSubFrames.setStatus("current")
_HwRadioManageTable_Object = MibTable
hwRadioManageTable = _HwRadioManageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2)
)
if mibBuilder.loadTexts:
    hwRadioManageTable.setStatus("current")
_HwRadioManageEntry_Object = MibTableRow
hwRadioManageEntry = _HwRadioManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1)
)
hwRadioManageEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioManageEntry.setStatus("current")
_HwRadioID_Type = Unsigned32
_HwRadioID_Object = MibTableColumn
hwRadioID = _HwRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 1),
    _HwRadioID_Type()
)
hwRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRadioID.setStatus("current")
_HwRadioMngBaseBssID_Type = MacAddress
_HwRadioMngBaseBssID_Object = MibTableColumn
hwRadioMngBaseBssID = _HwRadioMngBaseBssID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 2),
    _HwRadioMngBaseBssID_Type()
)
hwRadioMngBaseBssID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioMngBaseBssID.setStatus("current")


class _HwRadioMngRadioProfileName_Type(OctetString):
    """Custom type hwRadioMngRadioProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadioMngRadioProfileName_Type.__name__ = "OctetString"
_HwRadioMngRadioProfileName_Object = MibTableColumn
hwRadioMngRadioProfileName = _HwRadioMngRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 3),
    _HwRadioMngRadioProfileName_Type()
)
hwRadioMngRadioProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngRadioProfileName.setStatus("current")


class _HwRadioMngState_Type(Integer32):
    """Custom type hwRadioMngState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioMngState_Type.__name__ = "Integer32"
_HwRadioMngState_Object = MibTableColumn
hwRadioMngState = _HwRadioMngState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 4),
    _HwRadioMngState_Type()
)
hwRadioMngState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngState.setStatus("current")
_HwRadioMngChannel_Type = Unsigned32
_HwRadioMngChannel_Object = MibTableColumn
hwRadioMngChannel = _HwRadioMngChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 5),
    _HwRadioMngChannel_Type()
)
hwRadioMngChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngChannel.setStatus("current")
_HwRadioMngPowerLevel_Type = Unsigned32
_HwRadioMngPowerLevel_Object = MibTableColumn
hwRadioMngPowerLevel = _HwRadioMngPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 6),
    _HwRadioMngPowerLevel_Type()
)
hwRadioMngPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngPowerLevel.setStatus("current")
_HwRadioMngPower_Type = Integer32
_HwRadioMngPower_Object = MibTableColumn
hwRadioMngPower = _HwRadioMngPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 7),
    _HwRadioMngPower_Type()
)
hwRadioMngPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngPower.setStatus("current")


class _HwRadioAvailableSntennaNumber_Type(Integer32):
    """Custom type hwRadioAvailableSntennaNumber based on Integer32"""
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
        *(("all", 1),
          ("num0", 2),
          ("num1", 3),
          ("num2", 4),
          ("num3", 5),
          ("num4", 6),
          ("num5", 7))
    )


_HwRadioAvailableSntennaNumber_Type.__name__ = "Integer32"
_HwRadioAvailableSntennaNumber_Object = MibTableColumn
hwRadioAvailableSntennaNumber = _HwRadioAvailableSntennaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 8),
    _HwRadioAvailableSntennaNumber_Type()
)
hwRadioAvailableSntennaNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadioAvailableSntennaNumber.setStatus("current")
_HwRadioWorkingChannel_Type = Unsigned32
_HwRadioWorkingChannel_Object = MibTableColumn
hwRadioWorkingChannel = _HwRadioWorkingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 9),
    _HwRadioWorkingChannel_Type()
)
hwRadioWorkingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioWorkingChannel.setStatus("current")
_HwRadioWorkingPowerLevel_Type = Unsigned32
_HwRadioWorkingPowerLevel_Object = MibTableColumn
hwRadioWorkingPowerLevel = _HwRadioWorkingPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 10),
    _HwRadioWorkingPowerLevel_Type()
)
hwRadioWorkingPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioWorkingPowerLevel.setStatus("current")
_HwRadioWorkingPower_Type = Unsigned32
_HwRadioWorkingPower_Object = MibTableColumn
hwRadioWorkingPower = _HwRadioWorkingPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 11),
    _HwRadioWorkingPower_Type()
)
hwRadioWorkingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioWorkingPower.setStatus("current")


class _HwRadioMngChannelBandwidth_Type(Integer32):
    """Custom type hwRadioMngChannelBandwidth based on Integer32"""
    defaultValue = 1

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
        *(("ht20", 1),
          ("ht40Minus", 3),
          ("ht40Plus", 2),
          ("ht80", 4))
    )


_HwRadioMngChannelBandwidth_Type.__name__ = "Integer32"
_HwRadioMngChannelBandwidth_Object = MibTableColumn
hwRadioMngChannelBandwidth = _HwRadioMngChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 12),
    _HwRadioMngChannelBandwidth_Type()
)
hwRadioMngChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngChannelBandwidth.setStatus("current")


class _HwRadioWorkingChannelBandwidth_Type(Integer32):
    """Custom type hwRadioWorkingChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40Minus", 3),
          ("ht40Plus", 2),
          ("ht80", 4),
          ("unknown", -1))
    )


_HwRadioWorkingChannelBandwidth_Type.__name__ = "Integer32"
_HwRadioWorkingChannelBandwidth_Object = MibTableColumn
hwRadioWorkingChannelBandwidth = _HwRadioWorkingChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 13),
    _HwRadioWorkingChannelBandwidth_Type()
)
hwRadioWorkingChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioWorkingChannelBandwidth.setStatus("current")


class _HwRadio80211nMCSValue_Type(Integer32):
    """Custom type hwRadio80211nMCSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_HwRadio80211nMCSValue_Type.__name__ = "Integer32"
_HwRadio80211nMCSValue_Object = MibTableColumn
hwRadio80211nMCSValue = _HwRadio80211nMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 14),
    _HwRadio80211nMCSValue_Type()
)
hwRadio80211nMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211nMCSValue.setStatus("current")


class _HwRadioWidsWorkMode_Type(Integer32):
    """Custom type hwRadioWidsWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HwRadioWidsWorkMode_Type.__name__ = "Integer32"
_HwRadioWidsWorkMode_Object = MibTableColumn
hwRadioWidsWorkMode = _HwRadioWidsWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 15),
    _HwRadioWidsWorkMode_Type()
)
hwRadioWidsWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioWidsWorkMode.setStatus("current")


class _HwRadioMngBinded_Type(Integer32):
    """Custom type hwRadioMngBinded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", -1))
    )


_HwRadioMngBinded_Type.__name__ = "Integer32"
_HwRadioMngBinded_Object = MibTableColumn
hwRadioMngBinded = _HwRadioMngBinded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 16),
    _HwRadioMngBinded_Type()
)
hwRadioMngBinded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMngBinded.setStatus("current")


class _HwRadioDeviceDetectEnable_Type(Integer32):
    """Custom type hwRadioDeviceDetectEnable based on Integer32"""
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


_HwRadioDeviceDetectEnable_Type.__name__ = "Integer32"
_HwRadioDeviceDetectEnable_Object = MibTableColumn
hwRadioDeviceDetectEnable = _HwRadioDeviceDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 17),
    _HwRadioDeviceDetectEnable_Type()
)
hwRadioDeviceDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioDeviceDetectEnable.setStatus("current")
_HwRadioMaxTxPwrLvl_Type = Integer32
_HwRadioMaxTxPwrLvl_Object = MibTableColumn
hwRadioMaxTxPwrLvl = _HwRadioMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 18),
    _HwRadioMaxTxPwrLvl_Type()
)
hwRadioMaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioMaxTxPwrLvl.setStatus("current")
_HwRadioPwrAttRange_Type = Integer32
_HwRadioPwrAttRange_Object = MibTableColumn
hwRadioPwrAttRange = _HwRadioPwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 19),
    _HwRadioPwrAttRange_Type()
)
hwRadioPwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPwrAttRange.setStatus("current")
_HwRadioPwrAttValue_Type = Integer32
_HwRadioPwrAttValue_Object = MibTableColumn
hwRadioPwrAttValue = _HwRadioPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 20),
    _HwRadioPwrAttValue_Type()
)
hwRadioPwrAttValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPwrAttValue.setStatus("current")
_HwRadioAntennaGain_Type = Integer32
_HwRadioAntennaGain_Object = MibTableColumn
hwRadioAntennaGain = _HwRadioAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 21),
    _HwRadioAntennaGain_Type()
)
hwRadioAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAntennaGain.setStatus("current")


class _HwRadioBridgeWhitelistEnable_Type(Integer32):
    """Custom type hwRadioBridgeWhitelistEnable based on Integer32"""
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


_HwRadioBridgeWhitelistEnable_Type.__name__ = "Integer32"
_HwRadioBridgeWhitelistEnable_Object = MibTableColumn
hwRadioBridgeWhitelistEnable = _HwRadioBridgeWhitelistEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 22),
    _HwRadioBridgeWhitelistEnable_Type()
)
hwRadioBridgeWhitelistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBridgeWhitelistEnable.setStatus("current")


class _HwRadioBridgeWhitelistName_Type(OctetString):
    """Custom type hwRadioBridgeWhitelistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwRadioBridgeWhitelistName_Type.__name__ = "OctetString"
_HwRadioBridgeWhitelistName_Object = MibTableColumn
hwRadioBridgeWhitelistName = _HwRadioBridgeWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 23),
    _HwRadioBridgeWhitelistName_Type()
)
hwRadioBridgeWhitelistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBridgeWhitelistName.setStatus("current")


class _HwRadioBridgeStpSwitch_Type(Integer32):
    """Custom type hwRadioBridgeStpSwitch based on Integer32"""
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


_HwRadioBridgeStpSwitch_Type.__name__ = "Integer32"
_HwRadioBridgeStpSwitch_Object = MibTableColumn
hwRadioBridgeStpSwitch = _HwRadioBridgeStpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 24),
    _HwRadioBridgeStpSwitch_Type()
)
hwRadioBridgeStpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBridgeStpSwitch.setStatus("current")


class _HwRadioBridgeSwitch_Type(Integer32):
    """Custom type hwRadioBridgeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioBridgeSwitch_Type.__name__ = "Integer32"
_HwRadioBridgeSwitch_Object = MibTableColumn
hwRadioBridgeSwitch = _HwRadioBridgeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 25),
    _HwRadioBridgeSwitch_Type()
)
hwRadioBridgeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBridgeSwitch.setStatus("current")


class _HwRadioBridgeMode_Type(Integer32):
    """Custom type hwRadioBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 3),
          ("middle", 1),
          ("root", 2))
    )


_HwRadioBridgeMode_Type.__name__ = "Integer32"
_HwRadioBridgeMode_Object = MibTableColumn
hwRadioBridgeMode = _HwRadioBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 26),
    _HwRadioBridgeMode_Type()
)
hwRadioBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioBridgeMode.setStatus("current")
_HwRadioUndoBridgeWhitelist_Type = Integer32
_HwRadioUndoBridgeWhitelist_Object = MibTableColumn
hwRadioUndoBridgeWhitelist = _HwRadioUndoBridgeWhitelist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 27),
    _HwRadioUndoBridgeWhitelist_Type()
)
hwRadioUndoBridgeWhitelist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUndoBridgeWhitelist.setStatus("current")


class _HwRadioUserTrafficScheduler_Type(Integer32):
    """Custom type hwRadioUserTrafficScheduler based on Integer32"""
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


_HwRadioUserTrafficScheduler_Type.__name__ = "Integer32"
_HwRadioUserTrafficScheduler_Object = MibTableColumn
hwRadioUserTrafficScheduler = _HwRadioUserTrafficScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 28),
    _HwRadioUserTrafficScheduler_Type()
)
hwRadioUserTrafficScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUserTrafficScheduler.setStatus("obsolete")


class _HwRadioCountermeasuresMode_Type(Unsigned32):
    """Custom type hwRadioCountermeasuresMode based on Unsigned32"""
    defaultValue = 0


_HwRadioCountermeasuresMode_Object = MibTableColumn
hwRadioCountermeasuresMode = _HwRadioCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 29),
    _HwRadioCountermeasuresMode_Type()
)
hwRadioCountermeasuresMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCountermeasuresMode.setStatus("current")


class _HwRadioFrequency_Type(Integer32):
    """Custom type hwRadioFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frequency2G", 1),
          ("frequency5G", 2))
    )


_HwRadioFrequency_Type.__name__ = "Integer32"
_HwRadioFrequency_Object = MibTableColumn
hwRadioFrequency = _HwRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 30),
    _HwRadioFrequency_Type()
)
hwRadioFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioFrequency.setStatus("current")


class _HwRadioCountermeasuresSwitch_Type(Integer32):
    """Custom type hwRadioCountermeasuresSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioCountermeasuresSwitch_Type.__name__ = "Integer32"
_HwRadioCountermeasuresSwitch_Object = MibTableColumn
hwRadioCountermeasuresSwitch = _HwRadioCountermeasuresSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 31),
    _HwRadioCountermeasuresSwitch_Type()
)
hwRadioCountermeasuresSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCountermeasuresSwitch.setStatus("current")
_HwRadioSpectrumAnalysisEnable_Type = Integer32
_HwRadioSpectrumAnalysisEnable_Object = MibTableColumn
hwRadioSpectrumAnalysisEnable = _HwRadioSpectrumAnalysisEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 32),
    _HwRadioSpectrumAnalysisEnable_Type()
)
hwRadioSpectrumAnalysisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioSpectrumAnalysisEnable.setStatus("current")
_HwRadioWidsAttackDetEnable_Type = Integer32
_HwRadioWidsAttackDetEnable_Object = MibTableColumn
hwRadioWidsAttackDetEnable = _HwRadioWidsAttackDetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 33),
    _HwRadioWidsAttackDetEnable_Type()
)
hwRadioWidsAttackDetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioWidsAttackDetEnable.setStatus("current")
_HwRadioMeshWhitelistName_Type = OctetString
_HwRadioMeshWhitelistName_Object = MibTableColumn
hwRadioMeshWhitelistName = _HwRadioMeshWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 34),
    _HwRadioMeshWhitelistName_Type()
)
hwRadioMeshWhitelistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMeshWhitelistName.setStatus("current")
_HwRadioUndoMeshWhitelist_Type = Integer32
_HwRadioUndoMeshWhitelist_Object = MibTableColumn
hwRadioUndoMeshWhitelist = _HwRadioUndoMeshWhitelist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 35),
    _HwRadioUndoMeshWhitelist_Type()
)
hwRadioUndoMeshWhitelist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioUndoMeshWhitelist.setStatus("current")


class _HwRadioMeshRole_Type(Integer32):
    """Custom type hwRadioMeshRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meshNode", 1),
          ("meshPortal", 2))
    )


_HwRadioMeshRole_Type.__name__ = "Integer32"
_HwRadioMeshRole_Object = MibTableColumn
hwRadioMeshRole = _HwRadioMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 36),
    _HwRadioMeshRole_Type()
)
hwRadioMeshRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMeshRole.setStatus("current")


class _HwRadioLocationEnable_Type(Integer32):
    """Custom type hwRadioLocationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioLocationEnable_Type.__name__ = "Integer32"
_HwRadioLocationEnable_Object = MibTableColumn
hwRadioLocationEnable = _HwRadioLocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 37),
    _HwRadioLocationEnable_Type()
)
hwRadioLocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationEnable.setStatus("current")


class _HwRadioLocationScanChannelEnable_Type(Integer32):
    """Custom type hwRadioLocationScanChannelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioLocationScanChannelEnable_Type.__name__ = "Integer32"
_HwRadioLocationScanChannelEnable_Object = MibTableColumn
hwRadioLocationScanChannelEnable = _HwRadioLocationScanChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 38),
    _HwRadioLocationScanChannelEnable_Type()
)
hwRadioLocationScanChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioLocationScanChannelEnable.setStatus("current")


class _HwRadio80211nMulticastMCSValue_Type(Integer32):
    """Custom type hwRadio80211nMulticastMCSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_HwRadio80211nMulticastMCSValue_Type.__name__ = "Integer32"
_HwRadio80211nMulticastMCSValue_Object = MibTableColumn
hwRadio80211nMulticastMCSValue = _HwRadio80211nMulticastMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 39),
    _HwRadio80211nMulticastMCSValue_Type()
)
hwRadio80211nMulticastMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio80211nMulticastMCSValue.setStatus("current")


class _HwRadioSpectrogramServerReportEnable_Type(Integer32):
    """Custom type hwRadioSpectrogramServerReportEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRadioSpectrogramServerReportEnable_Type.__name__ = "Integer32"
_HwRadioSpectrogramServerReportEnable_Object = MibTableColumn
hwRadioSpectrogramServerReportEnable = _HwRadioSpectrogramServerReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 40),
    _HwRadioSpectrogramServerReportEnable_Type()
)
hwRadioSpectrogramServerReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioSpectrogramServerReportEnable.setStatus("current")


class _HwRadioRadioMulticastRateValue_Type(Integer32):
    """Custom type hwRadioRadioMulticastRateValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 1),
          ("rate11", 6),
          ("rate12", 7),
          ("rate18", 8),
          ("rate2", 2),
          ("rate24", 10),
          ("rate36", 12),
          ("rate48", 13),
          ("rate54", 14),
          ("rate55", 3),
          ("rate6", 4),
          ("rate9", 5),
          ("unknown", -1))
    )


_HwRadioRadioMulticastRateValue_Type.__name__ = "Integer32"
_HwRadioRadioMulticastRateValue_Object = MibTableColumn
hwRadioRadioMulticastRateValue = _HwRadioRadioMulticastRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 41),
    _HwRadioRadioMulticastRateValue_Type()
)
hwRadioRadioMulticastRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioRadioMulticastRateValue.setStatus("current")


class _HwRadio11acSpatialStream_Type(Integer32):
    """Custom type hwRadio11acSpatialStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 3),
    )


_HwRadio11acSpatialStream_Type.__name__ = "Integer32"
_HwRadio11acSpatialStream_Object = MibTableColumn
hwRadio11acSpatialStream = _HwRadio11acSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 42),
    _HwRadio11acSpatialStream_Type()
)
hwRadio11acSpatialStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio11acSpatialStream.setStatus("current")


class _HwRadio11acMCSValue_Type(Integer32):
    """Custom type hwRadio11acMCSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 9),
    )


_HwRadio11acMCSValue_Type.__name__ = "Integer32"
_HwRadio11acMCSValue_Object = MibTableColumn
hwRadio11acMCSValue = _HwRadio11acMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 43),
    _HwRadio11acMCSValue_Type()
)
hwRadio11acMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadio11acMCSValue.setStatus("current")


class _HwRadioActiveSwitch_Type(Integer32):
    """Custom type hwRadioActiveSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("dormancy", 1))
    )


_HwRadioActiveSwitch_Type.__name__ = "Integer32"
_HwRadioActiveSwitch_Object = MibTableColumn
hwRadioActiveSwitch = _HwRadioActiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 2, 1, 44),
    _HwRadioActiveSwitch_Type()
)
hwRadioActiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioActiveSwitch.setStatus("current")
_HwRadioCalibrateStatisicsTable_Object = MibTable
hwRadioCalibrateStatisicsTable = _HwRadioCalibrateStatisicsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3)
)
if mibBuilder.loadTexts:
    hwRadioCalibrateStatisicsTable.setStatus("current")
_HwRadioCalibrateStatisicsEntry_Object = MibTableRow
hwRadioCalibrateStatisicsEntry = _HwRadioCalibrateStatisicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3, 1)
)
hwRadioCalibrateStatisicsEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioCalibrateStatisicsEntry.setStatus("current")
_HwRadioCalStatisSignalBadCount_Type = Unsigned32
_HwRadioCalStatisSignalBadCount_Object = MibTableColumn
hwRadioCalStatisSignalBadCount = _HwRadioCalStatisSignalBadCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3, 1, 1),
    _HwRadioCalStatisSignalBadCount_Type()
)
hwRadioCalStatisSignalBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioCalStatisSignalBadCount.setStatus("current")
_HwRadioCalStatisCalibratePowerCount_Type = Unsigned32
_HwRadioCalStatisCalibratePowerCount_Object = MibTableColumn
hwRadioCalStatisCalibratePowerCount = _HwRadioCalStatisCalibratePowerCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3, 1, 2),
    _HwRadioCalStatisCalibratePowerCount_Type()
)
hwRadioCalStatisCalibratePowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioCalStatisCalibratePowerCount.setStatus("current")
_HwRadioCalStatisCalibrateChannelCount_Type = Unsigned32
_HwRadioCalStatisCalibrateChannelCount_Object = MibTableColumn
hwRadioCalStatisCalibrateChannelCount = _HwRadioCalStatisCalibrateChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3, 1, 3),
    _HwRadioCalStatisCalibrateChannelCount_Type()
)
hwRadioCalStatisCalibrateChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioCalStatisCalibrateChannelCount.setStatus("current")


class _HwRadioCalibrateStatisicsOperMode_Type(Integer32):
    """Custom type hwRadioCalibrateStatisicsOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearstatistic", 1),
          ("invalid", -1))
    )


_HwRadioCalibrateStatisicsOperMode_Type.__name__ = "Integer32"
_HwRadioCalibrateStatisicsOperMode_Object = MibTableColumn
hwRadioCalibrateStatisicsOperMode = _HwRadioCalibrateStatisicsOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 3, 1, 4),
    _HwRadioCalibrateStatisicsOperMode_Type()
)
hwRadioCalibrateStatisicsOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateStatisicsOperMode.setStatus("current")
_HwRadioAuthNeighborInfTable_Object = MibTable
hwRadioAuthNeighborInfTable = _HwRadioAuthNeighborInfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4)
)
if mibBuilder.loadTexts:
    hwRadioAuthNeighborInfTable.setStatus("current")
_HwRadioAuthNeighborInfEntry_Object = MibTableRow
hwRadioAuthNeighborInfEntry = _HwRadioAuthNeighborInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1)
)
hwRadioAuthNeighborInfEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioAuthNeighborInfEntry.setStatus("current")
_HwAuthenticRadioNeighborAPID_Type = OctetString
_HwAuthenticRadioNeighborAPID_Object = MibTableColumn
hwAuthenticRadioNeighborAPID = _HwAuthenticRadioNeighborAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1, 1),
    _HwAuthenticRadioNeighborAPID_Type()
)
hwAuthenticRadioNeighborAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticRadioNeighborAPID.setStatus("current")
_HwAuthenticRadioNeighborChannel_Type = OctetString
_HwAuthenticRadioNeighborChannel_Object = MibTableColumn
hwAuthenticRadioNeighborChannel = _HwAuthenticRadioNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1, 2),
    _HwAuthenticRadioNeighborChannel_Type()
)
hwAuthenticRadioNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticRadioNeighborChannel.setStatus("current")
_HwAuthenticRadioNeighborFrontAttenu_Type = OctetString
_HwAuthenticRadioNeighborFrontAttenu_Object = MibTableColumn
hwAuthenticRadioNeighborFrontAttenu = _HwAuthenticRadioNeighborFrontAttenu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1, 3),
    _HwAuthenticRadioNeighborFrontAttenu_Type()
)
hwAuthenticRadioNeighborFrontAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticRadioNeighborFrontAttenu.setStatus("current")
_HwAuthenticRadioNeighborBackAttenu_Type = OctetString
_HwAuthenticRadioNeighborBackAttenu_Object = MibTableColumn
hwAuthenticRadioNeighborBackAttenu = _HwAuthenticRadioNeighborBackAttenu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1, 4),
    _HwAuthenticRadioNeighborBackAttenu_Type()
)
hwAuthenticRadioNeighborBackAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticRadioNeighborBackAttenu.setStatus("current")
_HwAuthenticRadioNeighborSSID_Type = OctetString
_HwAuthenticRadioNeighborSSID_Object = MibTableColumn
hwAuthenticRadioNeighborSSID = _HwAuthenticRadioNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 4, 1, 5),
    _HwAuthenticRadioNeighborSSID_Type()
)
hwAuthenticRadioNeighborSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticRadioNeighborSSID.setStatus("current")
_HwRadioLoadBalanceGroupTable_Object = MibTable
hwRadioLoadBalanceGroupTable = _HwRadioLoadBalanceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5)
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupTable.setStatus("current")
_HwRadioLoadBalanceGroupEntry_Object = MibTableRow
hwRadioLoadBalanceGroupEntry = _HwRadioLoadBalanceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1)
)
hwRadioLoadBalanceGroupEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwLBGroupName"),
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupEntry.setStatus("current")
_HwLBGroupName_Type = OctetString
_HwLBGroupName_Object = MibTableColumn
hwLBGroupName = _HwLBGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 1),
    _HwLBGroupName_Type()
)
hwLBGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLBGroupName.setStatus("current")


class _HwLBGroupMode_Type(Integer32):
    """Custom type hwLBGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("session", 1),
          ("traffic", 2))
    )


_HwLBGroupMode_Type.__name__ = "Integer32"
_HwLBGroupMode_Object = MibTableColumn
hwLBGroupMode = _HwLBGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 2),
    _HwLBGroupMode_Type()
)
hwLBGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLBGroupMode.setStatus("current")
_HwLBGapThreshold_Type = Integer32
_HwLBGapThreshold_Object = MibTableColumn
hwLBGapThreshold = _HwLBGapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 3),
    _HwLBGapThreshold_Type()
)
hwLBGapThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLBGapThreshold.setStatus("current")
_HwLBAssociateThreshold_Type = Unsigned32
_HwLBAssociateThreshold_Object = MibTableColumn
hwLBAssociateThreshold = _HwLBAssociateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 4),
    _HwLBAssociateThreshold_Type()
)
hwLBAssociateThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLBAssociateThreshold.setStatus("current")


class _HwLBGroupStatus_Type(Integer32):
    """Custom type hwLBGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 2),
          ("unbalanced", 1))
    )


_HwLBGroupStatus_Type.__name__ = "Integer32"
_HwLBGroupStatus_Object = MibTableColumn
hwLBGroupStatus = _HwLBGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 5),
    _HwLBGroupStatus_Type()
)
hwLBGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBGroupStatus.setStatus("current")
_HwLBGroupRowStatus_Type = RowStatus
_HwLBGroupRowStatus_Object = MibTableColumn
hwLBGroupRowStatus = _HwLBGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 5, 1, 6),
    _HwLBGroupRowStatus_Type()
)
hwLBGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLBGroupRowStatus.setStatus("current")
_HwRadioLoadBalanceGroupMemberTable_Object = MibTable
hwRadioLoadBalanceGroupMemberTable = _HwRadioLoadBalanceGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6)
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupMemberTable.setStatus("current")
_HwRadioLoadBalanceGroupMemberEntry_Object = MibTableRow
hwRadioLoadBalanceGroupMemberEntry = _HwRadioLoadBalanceGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1)
)
hwRadioLoadBalanceGroupMemberEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwLBGroupName"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupMemberEntry.setStatus("current")
_HwLBMemberRadioChannel_Type = Unsigned32
_HwLBMemberRadioChannel_Object = MibTableColumn
hwLBMemberRadioChannel = _HwLBMemberRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 1),
    _HwLBMemberRadioChannel_Type()
)
hwLBMemberRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBMemberRadioChannel.setStatus("current")
_HwLBMemberRadioPowerLevel_Type = Unsigned32
_HwLBMemberRadioPowerLevel_Object = MibTableColumn
hwLBMemberRadioPowerLevel = _HwLBMemberRadioPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 2),
    _HwLBMemberRadioPowerLevel_Type()
)
hwLBMemberRadioPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBMemberRadioPowerLevel.setStatus("current")
_HwLBMemberRadioPower_Type = Unsigned32
_HwLBMemberRadioPower_Object = MibTableColumn
hwLBMemberRadioPower = _HwLBMemberRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 3),
    _HwLBMemberRadioPower_Type()
)
hwLBMemberRadioPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBMemberRadioPower.setStatus("current")
_HwLBMemberRadioSeesionNum_Type = Unsigned32
_HwLBMemberRadioSeesionNum_Object = MibTableColumn
hwLBMemberRadioSeesionNum = _HwLBMemberRadioSeesionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 4),
    _HwLBMemberRadioSeesionNum_Type()
)
hwLBMemberRadioSeesionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBMemberRadioSeesionNum.setStatus("current")
_HwLBMemberRadioTraffic_Type = Unsigned32
_HwLBMemberRadioTraffic_Object = MibTableColumn
hwLBMemberRadioTraffic = _HwLBMemberRadioTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 5),
    _HwLBMemberRadioTraffic_Type()
)
hwLBMemberRadioTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLBMemberRadioTraffic.setStatus("current")
_HwLBMemberRowStatus_Type = RowStatus
_HwLBMemberRowStatus_Object = MibTableColumn
hwLBMemberRowStatus = _HwLBMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 6, 1, 6),
    _HwLBMemberRowStatus_Type()
)
hwLBMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLBMemberRowStatus.setStatus("current")
_HwRadioUncontrolAPInfTable_Object = MibTable
hwRadioUncontrolAPInfTable = _HwRadioUncontrolAPInfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7)
)
if mibBuilder.loadTexts:
    hwRadioUncontrolAPInfTable.setStatus("current")
_HwRadioUncontrolAPInfEntry_Object = MibTableRow
hwRadioUncontrolAPInfEntry = _HwRadioUncontrolAPInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1)
)
hwRadioUncontrolAPInfEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwUncontrolAPIndex"),
)
if mibBuilder.loadTexts:
    hwRadioUncontrolAPInfEntry.setStatus("current")
_HwUncontrolAPIndex_Type = Integer32
_HwUncontrolAPIndex_Object = MibTableColumn
hwUncontrolAPIndex = _HwUncontrolAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 1),
    _HwUncontrolAPIndex_Type()
)
hwUncontrolAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUncontrolAPIndex.setStatus("current")
_HwUncontrolAPBSSID_Type = MacAddress
_HwUncontrolAPBSSID_Object = MibTableColumn
hwUncontrolAPBSSID = _HwUncontrolAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 2),
    _HwUncontrolAPBSSID_Type()
)
hwUncontrolAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUncontrolAPBSSID.setStatus("current")
_HwAuthAPIndex_Type = Integer32
_HwAuthAPIndex_Object = MibTableColumn
hwAuthAPIndex = _HwAuthAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 3),
    _HwAuthAPIndex_Type()
)
hwAuthAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthAPIndex.setStatus("current")
_HwUncontrolAPChannel_Type = Unsigned32
_HwUncontrolAPChannel_Object = MibTableColumn
hwUncontrolAPChannel = _HwUncontrolAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 4),
    _HwUncontrolAPChannel_Type()
)
hwUncontrolAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUncontrolAPChannel.setStatus("current")
_HwUncontrolAPRSSI_Type = Integer32
_HwUncontrolAPRSSI_Object = MibTableColumn
hwUncontrolAPRSSI = _HwUncontrolAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 5),
    _HwUncontrolAPRSSI_Type()
)
hwUncontrolAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUncontrolAPRSSI.setStatus("current")
_HwUncontrolAPSSID_Type = OctetString
_HwUncontrolAPSSID_Object = MibTableColumn
hwUncontrolAPSSID = _HwUncontrolAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 7, 1, 6),
    _HwUncontrolAPSSID_Type()
)
hwUncontrolAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUncontrolAPSSID.setStatus("current")
_HwRadioPerformanceStatTable_Object = MibTable
hwRadioPerformanceStatTable = _HwRadioPerformanceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8)
)
if mibBuilder.loadTexts:
    hwRadioPerformanceStatTable.setStatus("current")
_HwRadioPerformanceStatEntry_Object = MibTableRow
hwRadioPerformanceStatEntry = _HwRadioPerformanceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1)
)
hwRadioPerformanceStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioPerformanceStatEntry.setStatus("current")
_HwRadioRcvFrames_Type = Unsigned32
_HwRadioRcvFrames_Object = MibTableColumn
hwRadioRcvFrames = _HwRadioRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 1),
    _HwRadioRcvFrames_Type()
)
hwRadioRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvFrames.setStatus("current")
_HwRadioRcvBytes_Type = Unsigned32
_HwRadioRcvBytes_Object = MibTableColumn
hwRadioRcvBytes = _HwRadioRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 2),
    _HwRadioRcvBytes_Type()
)
hwRadioRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvBytes.setStatus("current")
_HwRadioSendFrames_Type = Unsigned32
_HwRadioSendFrames_Object = MibTableColumn
hwRadioSendFrames = _HwRadioSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 3),
    _HwRadioSendFrames_Type()
)
hwRadioSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendFrames.setStatus("current")
_HwRadioSendBytes_Type = Unsigned32
_HwRadioSendBytes_Object = MibTableColumn
hwRadioSendBytes = _HwRadioSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 4),
    _HwRadioSendBytes_Type()
)
hwRadioSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendBytes.setStatus("current")
_HwRadioSendRtsSuccess_Type = Unsigned32
_HwRadioSendRtsSuccess_Object = MibTableColumn
hwRadioSendRtsSuccess = _HwRadioSendRtsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 5),
    _HwRadioSendRtsSuccess_Type()
)
hwRadioSendRtsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendRtsSuccess.setStatus("current")
_HwRadioSendUnicast_Type = Unsigned32
_HwRadioSendUnicast_Object = MibTableColumn
hwRadioSendUnicast = _HwRadioSendUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 6),
    _HwRadioSendUnicast_Type()
)
hwRadioSendUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendUnicast.setStatus("current")
_HwRadioSendBroadcast_Type = Unsigned32
_HwRadioSendBroadcast_Object = MibTableColumn
hwRadioSendBroadcast = _HwRadioSendBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 7),
    _HwRadioSendBroadcast_Type()
)
hwRadioSendBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendBroadcast.setStatus("current")
_HwRadioSendFailFrames_Type = Unsigned32
_HwRadioSendFailFrames_Object = MibTableColumn
hwRadioSendFailFrames = _HwRadioSendFailFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 8),
    _HwRadioSendFailFrames_Type()
)
hwRadioSendFailFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendFailFrames.setStatus("current")
_HwRadioRcvErrFrames_Type = Unsigned32
_HwRadioRcvErrFrames_Object = MibTableColumn
hwRadioRcvErrFrames = _HwRadioRcvErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 9),
    _HwRadioRcvErrFrames_Type()
)
hwRadioRcvErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvErrFrames.setStatus("current")
_HwRadioRcvPhyErrFrames_Type = Unsigned32
_HwRadioRcvPhyErrFrames_Object = MibTableColumn
hwRadioRcvPhyErrFrames = _HwRadioRcvPhyErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 10),
    _HwRadioRcvPhyErrFrames_Type()
)
hwRadioRcvPhyErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvPhyErrFrames.setStatus("current")
_HwRadioRcvCrcErrFrames_Type = Unsigned32
_HwRadioRcvCrcErrFrames_Object = MibTableColumn
hwRadioRcvCrcErrFrames = _HwRadioRcvCrcErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 11),
    _HwRadioRcvCrcErrFrames_Type()
)
hwRadioRcvCrcErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvCrcErrFrames.setStatus("current")
_HwRadioRcvMicErrFrames_Type = Unsigned32
_HwRadioRcvMicErrFrames_Object = MibTableColumn
hwRadioRcvMicErrFrames = _HwRadioRcvMicErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 12),
    _HwRadioRcvMicErrFrames_Type()
)
hwRadioRcvMicErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvMicErrFrames.setStatus("current")
_HwRadioRcvKeyDecryptErrFrames_Type = Unsigned32
_HwRadioRcvKeyDecryptErrFrames_Object = MibTableColumn
hwRadioRcvKeyDecryptErrFrames = _HwRadioRcvKeyDecryptErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 13),
    _HwRadioRcvKeyDecryptErrFrames_Type()
)
hwRadioRcvKeyDecryptErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvKeyDecryptErrFrames.setStatus("current")
_HwRadioRetryFrames_Type = Unsigned32
_HwRadioRetryFrames_Object = MibTableColumn
hwRadioRetryFrames = _HwRadioRetryFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 14),
    _HwRadioRetryFrames_Type()
)
hwRadioRetryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRetryFrames.setStatus("current")
_HwRadioPER_Type = Unsigned32
_HwRadioPER_Object = MibTableColumn
hwRadioPER = _HwRadioPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 15),
    _HwRadioPER_Type()
)
hwRadioPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPER.setStatus("current")
_HwRadioChUtilizationRate_Type = Unsigned32
_HwRadioChUtilizationRate_Object = MibTableColumn
hwRadioChUtilizationRate = _HwRadioChUtilizationRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 16),
    _HwRadioChUtilizationRate_Type()
)
hwRadioChUtilizationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioChUtilizationRate.setStatus("current")


class _HwRadioPerformanceStatOperMode_Type(Integer32):
    """Custom type hwRadioPerformanceStatOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearstatistic", 1),
          ("invalid", -1))
    )


_HwRadioPerformanceStatOperMode_Type.__name__ = "Integer32"
_HwRadioPerformanceStatOperMode_Object = MibTableColumn
hwRadioPerformanceStatOperMode = _HwRadioPerformanceStatOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 17),
    _HwRadioPerformanceStatOperMode_Type()
)
hwRadioPerformanceStatOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioPerformanceStatOperMode.setStatus("current")
_HwRadioPEROfLastPeriod_Type = Unsigned32
_HwRadioPEROfLastPeriod_Object = MibTableColumn
hwRadioPEROfLastPeriod = _HwRadioPEROfLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 18),
    _HwRadioPEROfLastPeriod_Type()
)
hwRadioPEROfLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPEROfLastPeriod.setStatus("current")
_HwRadioRcvSignalStrength_Type = Integer32
_HwRadioRcvSignalStrength_Object = MibTableColumn
hwRadioRcvSignalStrength = _HwRadioRcvSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 19),
    _HwRadioRcvSignalStrength_Type()
)
hwRadioRcvSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvSignalStrength.setStatus("current")
_HwRadioDownMacErrFrames_Type = Unsigned32
_HwRadioDownMacErrFrames_Object = MibTableColumn
hwRadioDownMacErrFrames = _HwRadioDownMacErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 20),
    _HwRadioDownMacErrFrames_Type()
)
hwRadioDownMacErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDownMacErrFrames.setStatus("obsolete")
_HwRadioRcvPower_Type = Integer32
_HwRadioRcvPower_Object = MibTableColumn
hwRadioRcvPower = _HwRadioRcvPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 21),
    _HwRadioRcvPower_Type()
)
hwRadioRcvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvPower.setStatus("current")
_HwRadioRcvUnicastFrames_Type = Counter64
_HwRadioRcvUnicastFrames_Object = MibTableColumn
hwRadioRcvUnicastFrames = _HwRadioRcvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 22),
    _HwRadioRcvUnicastFrames_Type()
)
hwRadioRcvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvUnicastFrames.setStatus("current")
_HwRadioRcvMngFrames_Type = Counter64
_HwRadioRcvMngFrames_Object = MibTableColumn
hwRadioRcvMngFrames = _HwRadioRcvMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 23),
    _HwRadioRcvMngFrames_Type()
)
hwRadioRcvMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvMngFrames.setStatus("current")
_HwRadioRcvCtrlFrames_Type = Counter64
_HwRadioRcvCtrlFrames_Object = MibTableColumn
hwRadioRcvCtrlFrames = _HwRadioRcvCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 24),
    _HwRadioRcvCtrlFrames_Type()
)
hwRadioRcvCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvCtrlFrames.setStatus("current")
_HwRadioRcvDataFrames_Type = Counter64
_HwRadioRcvDataFrames_Object = MibTableColumn
hwRadioRcvDataFrames = _HwRadioRcvDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 25),
    _HwRadioRcvDataFrames_Type()
)
hwRadioRcvDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvDataFrames.setStatus("current")
_HwRadioSendMngFrames_Type = Counter64
_HwRadioSendMngFrames_Object = MibTableColumn
hwRadioSendMngFrames = _HwRadioSendMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 26),
    _HwRadioSendMngFrames_Type()
)
hwRadioSendMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendMngFrames.setStatus("current")
_HwRadioSendCtrlFrames_Type = Counter64
_HwRadioSendCtrlFrames_Object = MibTableColumn
hwRadioSendCtrlFrames = _HwRadioSendCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 27),
    _HwRadioSendCtrlFrames_Type()
)
hwRadioSendCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendCtrlFrames.setStatus("current")
_HwRadioSendDataFrames_Type = Counter64
_HwRadioSendDataFrames_Object = MibTableColumn
hwRadioSendDataFrames = _HwRadioSendDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 28),
    _HwRadioSendDataFrames_Type()
)
hwRadioSendDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendDataFrames.setStatus("current")
_HwRadioStaMaxSignalStrength_Type = Integer32
_HwRadioStaMaxSignalStrength_Object = MibTableColumn
hwRadioStaMaxSignalStrength = _HwRadioStaMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 29),
    _HwRadioStaMaxSignalStrength_Type()
)
hwRadioStaMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaMaxSignalStrength.setStatus("current")
_HwRadioStaMinSignalStrength_Type = Integer32
_HwRadioStaMinSignalStrength_Object = MibTableColumn
hwRadioStaMinSignalStrength = _HwRadioStaMinSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 30),
    _HwRadioStaMinSignalStrength_Type()
)
hwRadioStaMinSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaMinSignalStrength.setStatus("current")
_HwRadioStaAvgSignalStrength_Type = Integer32
_HwRadioStaAvgSignalStrength_Object = MibTableColumn
hwRadioStaAvgSignalStrength = _HwRadioStaAvgSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 31),
    _HwRadioStaAvgSignalStrength_Type()
)
hwRadioStaAvgSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaAvgSignalStrength.setStatus("current")
_HwRadioSendRate_Type = Unsigned32
_HwRadioSendRate_Object = MibTableColumn
hwRadioSendRate = _HwRadioSendRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 32),
    _HwRadioSendRate_Type()
)
hwRadioSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendRate.setStatus("current")
_HwRadioRecvRate_Type = Unsigned32
_HwRadioRecvRate_Object = MibTableColumn
hwRadioRecvRate = _HwRadioRecvRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 33),
    _HwRadioRecvRate_Type()
)
hwRadioRecvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRecvRate.setStatus("current")
_HwRadioDropRate_Type = Unsigned32
_HwRadioDropRate_Object = MibTableColumn
hwRadioDropRate = _HwRadioDropRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 34),
    _HwRadioDropRate_Type()
)
hwRadioDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDropRate.setStatus("current")
_HwRadioAirPortDhcpFrames_Type = Counter64
_HwRadioAirPortDhcpFrames_Object = MibTableColumn
hwRadioAirPortDhcpFrames = _HwRadioAirPortDhcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 35),
    _HwRadioAirPortDhcpFrames_Type()
)
hwRadioAirPortDhcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioAirPortDhcpFrames.setStatus("current")
_HwRadioAirPortEapolFrames_Type = Counter64
_HwRadioAirPortEapolFrames_Object = MibTableColumn
hwRadioAirPortEapolFrames = _HwRadioAirPortEapolFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 36),
    _HwRadioAirPortEapolFrames_Type()
)
hwRadioAirPortEapolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioAirPortEapolFrames.setStatus("current")
_HwRadioAirPortPsPollFrames_Type = Counter64
_HwRadioAirPortPsPollFrames_Object = MibTableColumn
hwRadioAirPortPsPollFrames = _HwRadioAirPortPsPollFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 37),
    _HwRadioAirPortPsPollFrames_Type()
)
hwRadioAirPortPsPollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioAirPortPsPollFrames.setStatus("current")
_HwRadioAssocRequestFrames_Type = Counter64
_HwRadioAssocRequestFrames_Object = MibTableColumn
hwRadioAssocRequestFrames = _HwRadioAssocRequestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 38),
    _HwRadioAssocRequestFrames_Type()
)
hwRadioAssocRequestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioAssocRequestFrames.setStatus("current")
_HwRadioAssocResponseFrames_Type = Counter64
_HwRadioAssocResponseFrames_Object = MibTableColumn
hwRadioAssocResponseFrames = _HwRadioAssocResponseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 39),
    _HwRadioAssocResponseFrames_Type()
)
hwRadioAssocResponseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioAssocResponseFrames.setStatus("current")
_HwRadioReassocRequestFrames_Type = Counter64
_HwRadioReassocRequestFrames_Object = MibTableColumn
hwRadioReassocRequestFrames = _HwRadioReassocRequestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 40),
    _HwRadioReassocRequestFrames_Type()
)
hwRadioReassocRequestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioReassocRequestFrames.setStatus("current")
_HwRadioReassocResponseFrames_Type = Counter64
_HwRadioReassocResponseFrames_Object = MibTableColumn
hwRadioReassocResponseFrames = _HwRadioReassocResponseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 41),
    _HwRadioReassocResponseFrames_Type()
)
hwRadioReassocResponseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioReassocResponseFrames.setStatus("current")
_HwRadioDisassocFrames_Type = Counter64
_HwRadioDisassocFrames_Object = MibTableColumn
hwRadioDisassocFrames = _HwRadioDisassocFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 42),
    _HwRadioDisassocFrames_Type()
)
hwRadioDisassocFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDisassocFrames.setStatus("current")
_HwRadioDisauthFrames_Type = Counter64
_HwRadioDisauthFrames_Object = MibTableColumn
hwRadioDisauthFrames = _HwRadioDisauthFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 43),
    _HwRadioDisauthFrames_Type()
)
hwRadioDisauthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDisauthFrames.setStatus("current")
_HwRadioRcvFrames64Bits_Type = Counter64
_HwRadioRcvFrames64Bits_Object = MibTableColumn
hwRadioRcvFrames64Bits = _HwRadioRcvFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 44),
    _HwRadioRcvFrames64Bits_Type()
)
hwRadioRcvFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvFrames64Bits.setStatus("current")
_HwRadioRcvBytes64Bits_Type = Counter64
_HwRadioRcvBytes64Bits_Object = MibTableColumn
hwRadioRcvBytes64Bits = _HwRadioRcvBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 45),
    _HwRadioRcvBytes64Bits_Type()
)
hwRadioRcvBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvBytes64Bits.setStatus("current")
_HwRadioSendFrames64Bits_Type = Counter64
_HwRadioSendFrames64Bits_Object = MibTableColumn
hwRadioSendFrames64Bits = _HwRadioSendFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 46),
    _HwRadioSendFrames64Bits_Type()
)
hwRadioSendFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendFrames64Bits.setStatus("current")
_HwRadioSendBytes64Bits_Type = Counter64
_HwRadioSendBytes64Bits_Object = MibTableColumn
hwRadioSendBytes64Bits = _HwRadioSendBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 47),
    _HwRadioSendBytes64Bits_Type()
)
hwRadioSendBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendBytes64Bits.setStatus("current")
_HwRadioSendRtsSuccess64Bits_Type = Counter64
_HwRadioSendRtsSuccess64Bits_Object = MibTableColumn
hwRadioSendRtsSuccess64Bits = _HwRadioSendRtsSuccess64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 48),
    _HwRadioSendRtsSuccess64Bits_Type()
)
hwRadioSendRtsSuccess64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendRtsSuccess64Bits.setStatus("current")
_HwRadioSendUnicast64Bits_Type = Counter64
_HwRadioSendUnicast64Bits_Object = MibTableColumn
hwRadioSendUnicast64Bits = _HwRadioSendUnicast64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 49),
    _HwRadioSendUnicast64Bits_Type()
)
hwRadioSendUnicast64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendUnicast64Bits.setStatus("current")
_HwRadioSendBroadcast64Bits_Type = Counter64
_HwRadioSendBroadcast64Bits_Object = MibTableColumn
hwRadioSendBroadcast64Bits = _HwRadioSendBroadcast64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 50),
    _HwRadioSendBroadcast64Bits_Type()
)
hwRadioSendBroadcast64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendBroadcast64Bits.setStatus("current")
_HwRadioSendFailFrames64Bits_Type = Counter64
_HwRadioSendFailFrames64Bits_Object = MibTableColumn
hwRadioSendFailFrames64Bits = _HwRadioSendFailFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 51),
    _HwRadioSendFailFrames64Bits_Type()
)
hwRadioSendFailFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendFailFrames64Bits.setStatus("current")
_HwRadioRcvErrFrames64Bits_Type = Counter64
_HwRadioRcvErrFrames64Bits_Object = MibTableColumn
hwRadioRcvErrFrames64Bits = _HwRadioRcvErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 52),
    _HwRadioRcvErrFrames64Bits_Type()
)
hwRadioRcvErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvErrFrames64Bits.setStatus("current")
_HwRadioRcvPhyErrFrames64Bits_Type = Counter64
_HwRadioRcvPhyErrFrames64Bits_Object = MibTableColumn
hwRadioRcvPhyErrFrames64Bits = _HwRadioRcvPhyErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 53),
    _HwRadioRcvPhyErrFrames64Bits_Type()
)
hwRadioRcvPhyErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvPhyErrFrames64Bits.setStatus("current")
_HwRadioRcvCrcErrFrames64Bits_Type = Counter64
_HwRadioRcvCrcErrFrames64Bits_Object = MibTableColumn
hwRadioRcvCrcErrFrames64Bits = _HwRadioRcvCrcErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 54),
    _HwRadioRcvCrcErrFrames64Bits_Type()
)
hwRadioRcvCrcErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvCrcErrFrames64Bits.setStatus("current")
_HwRadioRcvMicErrFrames64Bits_Type = Counter64
_HwRadioRcvMicErrFrames64Bits_Object = MibTableColumn
hwRadioRcvMicErrFrames64Bits = _HwRadioRcvMicErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 55),
    _HwRadioRcvMicErrFrames64Bits_Type()
)
hwRadioRcvMicErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvMicErrFrames64Bits.setStatus("current")
_HwRadioRcvKeyDecryptErrFrames64Bits_Type = Counter64
_HwRadioRcvKeyDecryptErrFrames64Bits_Object = MibTableColumn
hwRadioRcvKeyDecryptErrFrames64Bits = _HwRadioRcvKeyDecryptErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 56),
    _HwRadioRcvKeyDecryptErrFrames64Bits_Type()
)
hwRadioRcvKeyDecryptErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvKeyDecryptErrFrames64Bits.setStatus("current")
_HwRadioRetryFrames64Bits_Type = Counter64
_HwRadioRetryFrames64Bits_Object = MibTableColumn
hwRadioRetryFrames64Bits = _HwRadioRetryFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 57),
    _HwRadioRetryFrames64Bits_Type()
)
hwRadioRetryFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRetryFrames64Bits.setStatus("current")
_HwRadioDownMacErrFrames64Bits_Type = Counter64
_HwRadioDownMacErrFrames64Bits_Object = MibTableColumn
hwRadioDownMacErrFrames64Bits = _HwRadioDownMacErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 58),
    _HwRadioDownMacErrFrames64Bits_Type()
)
hwRadioDownMacErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDownMacErrFrames64Bits.setStatus("obsolete")
_HwRadioNoise_Type = Integer32
_HwRadioNoise_Object = MibTableColumn
hwRadioNoise = _HwRadioNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 59),
    _HwRadioNoise_Type()
)
hwRadioNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioNoise.setStatus("current")
_HwRadioActualBandwidth_Type = Unsigned32
_HwRadioActualBandwidth_Object = MibTableColumn
hwRadioActualBandwidth = _HwRadioActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 60),
    _HwRadioActualBandwidth_Type()
)
hwRadioActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioActualBandwidth.setStatus("current")
_HwRadioFrames_Type = Counter64
_HwRadioFrames_Object = MibTableColumn
hwRadioFrames = _HwRadioFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 61),
    _HwRadioFrames_Type()
)
hwRadioFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioFrames.setStatus("current")
_HwRadioSendDropFrames64Bits_Type = Counter64
_HwRadioSendDropFrames64Bits_Object = MibTableColumn
hwRadioSendDropFrames64Bits = _HwRadioSendDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 62),
    _HwRadioSendDropFrames64Bits_Type()
)
hwRadioSendDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioSendDropFrames64Bits.setStatus("current")
_HwRadioRcvDropFrames64Bits_Type = Counter64
_HwRadioRcvDropFrames64Bits_Object = MibTableColumn
hwRadioRcvDropFrames64Bits = _HwRadioRcvDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 63),
    _HwRadioRcvDropFrames64Bits_Type()
)
hwRadioRcvDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRcvDropFrames64Bits.setStatus("current")
_HwRadioChannelFreeRate_Type = Unsigned32
_HwRadioChannelFreeRate_Object = MibTableColumn
hwRadioChannelFreeRate = _HwRadioChannelFreeRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 64),
    _HwRadioChannelFreeRate_Type()
)
hwRadioChannelFreeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioChannelFreeRate.setStatus("current")
_HwRadioTxRate_Type = Unsigned32
_HwRadioTxRate_Object = MibTableColumn
hwRadioTxRate = _HwRadioTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 65),
    _HwRadioTxRate_Type()
)
hwRadioTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioTxRate.setStatus("current")
_HwRadioRxRate_Type = Unsigned32
_HwRadioRxRate_Object = MibTableColumn
hwRadioRxRate = _HwRadioRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 66),
    _HwRadioRxRate_Type()
)
hwRadioRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioRxRate.setStatus("current")
_HwRadioChInterferenceRate_Type = Unsigned32
_HwRadioChInterferenceRate_Object = MibTableColumn
hwRadioChInterferenceRate = _HwRadioChInterferenceRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 8, 1, 67),
    _HwRadioChInterferenceRate_Type()
)
hwRadioChInterferenceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioChInterferenceRate.setStatus("current")
_HwRadioUnauthenticNeighborInfoTable_Object = MibTable
hwRadioUnauthenticNeighborInfoTable = _HwRadioUnauthenticNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9)
)
if mibBuilder.loadTexts:
    hwRadioUnauthenticNeighborInfoTable.setStatus("current")
_HwRadioUnauthenticNeighborInfoEntry_Object = MibTableRow
hwRadioUnauthenticNeighborInfoEntry = _HwRadioUnauthenticNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9, 1)
)
hwRadioUnauthenticNeighborInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioUnauthenticNeighborInfoEntry.setStatus("current")
_HwUnauthenticRadioNeighborBSSID_Type = OctetString
_HwUnauthenticRadioNeighborBSSID_Object = MibTableColumn
hwUnauthenticRadioNeighborBSSID = _HwUnauthenticRadioNeighborBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9, 1, 1),
    _HwUnauthenticRadioNeighborBSSID_Type()
)
hwUnauthenticRadioNeighborBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUnauthenticRadioNeighborBSSID.setStatus("current")
_HwUnauthenticRadioNeighborRSSI_Type = OctetString
_HwUnauthenticRadioNeighborRSSI_Object = MibTableColumn
hwUnauthenticRadioNeighborRSSI = _HwUnauthenticRadioNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9, 1, 2),
    _HwUnauthenticRadioNeighborRSSI_Type()
)
hwUnauthenticRadioNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUnauthenticRadioNeighborRSSI.setStatus("current")
_HwunauthenticRadioNeighborChannel_Type = OctetString
_HwunauthenticRadioNeighborChannel_Object = MibTableColumn
hwunauthenticRadioNeighborChannel = _HwunauthenticRadioNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9, 1, 3),
    _HwunauthenticRadioNeighborChannel_Type()
)
hwunauthenticRadioNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwunauthenticRadioNeighborChannel.setStatus("current")
_HwUnauthenticRadioNeighborSSID_Type = OctetString
_HwUnauthenticRadioNeighborSSID_Object = MibTableColumn
hwUnauthenticRadioNeighborSSID = _HwUnauthenticRadioNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 9, 1, 4),
    _HwUnauthenticRadioNeighborSSID_Type()
)
hwUnauthenticRadioNeighborSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUnauthenticRadioNeighborSSID.setStatus("current")
_HwRadioRegionCalibrateTable_Object = MibTable
hwRadioRegionCalibrateTable = _HwRadioRegionCalibrateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10)
)
if mibBuilder.loadTexts:
    hwRadioRegionCalibrateTable.setStatus("current")
_HwRadioRegionCalibrateEntry_Object = MibTableRow
hwRadioRegionCalibrateEntry = _HwRadioRegionCalibrateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10, 1)
)
hwRadioRegionCalibrateEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApRegionIndex"),
)
if mibBuilder.loadTexts:
    hwRadioRegionCalibrateEntry.setStatus("current")


class _HwRegionCalibrateStartupMode_Type(Integer32):
    """Custom type hwRegionCalibrateStartupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancelPeriodic", 3),
          ("immediate", 1),
          ("periodic", 2))
    )


_HwRegionCalibrateStartupMode_Type.__name__ = "Integer32"
_HwRegionCalibrateStartupMode_Object = MibTableColumn
hwRegionCalibrateStartupMode = _HwRegionCalibrateStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10, 1, 1),
    _HwRegionCalibrateStartupMode_Type()
)
hwRegionCalibrateStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRegionCalibrateStartupMode.setStatus("current")
_HwRegionCalibrateAutoTime_Type = DateAndTime
_HwRegionCalibrateAutoTime_Object = MibTableColumn
hwRegionCalibrateAutoTime = _HwRegionCalibrateAutoTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10, 1, 2),
    _HwRegionCalibrateAutoTime_Type()
)
hwRegionCalibrateAutoTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRegionCalibrateAutoTime.setStatus("current")


class _HwRegionCalibrateListenMode_Type(Integer32):
    """Custom type hwRegionCalibrateListenMode based on Integer32"""
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


_HwRegionCalibrateListenMode_Type.__name__ = "Integer32"
_HwRegionCalibrateListenMode_Object = MibTableColumn
hwRegionCalibrateListenMode = _HwRegionCalibrateListenMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10, 1, 3),
    _HwRegionCalibrateListenMode_Type()
)
hwRegionCalibrateListenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRegionCalibrateListenMode.setStatus("current")


class _HwRegionCalibrateStatus_Type(Integer32):
    """Custom type hwRegionCalibrateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stop", 2))
    )


_HwRegionCalibrateStatus_Type.__name__ = "Integer32"
_HwRegionCalibrateStatus_Object = MibTableColumn
hwRegionCalibrateStatus = _HwRegionCalibrateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 10, 1, 4),
    _HwRegionCalibrateStatus_Type()
)
hwRegionCalibrateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRegionCalibrateStatus.setStatus("current")
_HwBatchRadioProfileStartNumber_Type = Integer32
_HwBatchRadioProfileStartNumber_Object = MibScalar
hwBatchRadioProfileStartNumber = _HwBatchRadioProfileStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 11),
    _HwBatchRadioProfileStartNumber_Type()
)
hwBatchRadioProfileStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchRadioProfileStartNumber.setStatus("current")
_HwBatchRadioProfileNumber_Type = Integer32
_HwBatchRadioProfileNumber_Object = MibScalar
hwBatchRadioProfileNumber = _HwBatchRadioProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 12),
    _HwBatchRadioProfileNumber_Type()
)
hwBatchRadioProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchRadioProfileNumber.setStatus("current")
_HwBatchRadioProfileReturnNumber_Type = Integer32
_HwBatchRadioProfileReturnNumber_Object = MibScalar
hwBatchRadioProfileReturnNumber = _HwBatchRadioProfileReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 13),
    _HwBatchRadioProfileReturnNumber_Type()
)
hwBatchRadioProfileReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchRadioProfileReturnNumber.setStatus("current")
_HwBatchRadioProfileName_Type = OctetString
_HwBatchRadioProfileName_Object = MibScalar
hwBatchRadioProfileName = _HwBatchRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 14),
    _HwBatchRadioProfileName_Type()
)
hwBatchRadioProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchRadioProfileName.setStatus("current")
_HwBatchLoadBalanceGroupStartNumber_Type = Integer32
_HwBatchLoadBalanceGroupStartNumber_Object = MibScalar
hwBatchLoadBalanceGroupStartNumber = _HwBatchLoadBalanceGroupStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 15),
    _HwBatchLoadBalanceGroupStartNumber_Type()
)
hwBatchLoadBalanceGroupStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchLoadBalanceGroupStartNumber.setStatus("current")
_HwBatchLoadBalanceGroupNumber_Type = Integer32
_HwBatchLoadBalanceGroupNumber_Object = MibScalar
hwBatchLoadBalanceGroupNumber = _HwBatchLoadBalanceGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 16),
    _HwBatchLoadBalanceGroupNumber_Type()
)
hwBatchLoadBalanceGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchLoadBalanceGroupNumber.setStatus("current")
_HwBatchLoadBalanceGroupReturnNumber_Type = Integer32
_HwBatchLoadBalanceGroupReturnNumber_Object = MibScalar
hwBatchLoadBalanceGroupReturnNumber = _HwBatchLoadBalanceGroupReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 17),
    _HwBatchLoadBalanceGroupReturnNumber_Type()
)
hwBatchLoadBalanceGroupReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchLoadBalanceGroupReturnNumber.setStatus("current")
_HwBatchLoadBalanceGroupName_Type = OctetString
_HwBatchLoadBalanceGroupName_Object = MibScalar
hwBatchLoadBalanceGroupName = _HwBatchLoadBalanceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 18),
    _HwBatchLoadBalanceGroupName_Type()
)
hwBatchLoadBalanceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchLoadBalanceGroupName.setStatus("current")
_HwBatchUncontrolAPStartNumber_Type = Integer32
_HwBatchUncontrolAPStartNumber_Object = MibScalar
hwBatchUncontrolAPStartNumber = _HwBatchUncontrolAPStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 19),
    _HwBatchUncontrolAPStartNumber_Type()
)
hwBatchUncontrolAPStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchUncontrolAPStartNumber.setStatus("current")
_HwBatchUncontrolAPNumber_Type = Integer32
_HwBatchUncontrolAPNumber_Object = MibScalar
hwBatchUncontrolAPNumber = _HwBatchUncontrolAPNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 20),
    _HwBatchUncontrolAPNumber_Type()
)
hwBatchUncontrolAPNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBatchUncontrolAPNumber.setStatus("current")
_HwBatchUncontrolAPReturnNumber_Type = Integer32
_HwBatchUncontrolAPReturnNumber_Object = MibScalar
hwBatchUncontrolAPReturnNumber = _HwBatchUncontrolAPReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 21),
    _HwBatchUncontrolAPReturnNumber_Type()
)
hwBatchUncontrolAPReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchUncontrolAPReturnNumber.setStatus("current")
_HwBatchUncontrolAPBssid_Type = OctetString
_HwBatchUncontrolAPBssid_Object = MibScalar
hwBatchUncontrolAPBssid = _HwBatchUncontrolAPBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 22),
    _HwBatchUncontrolAPBssid_Type()
)
hwBatchUncontrolAPBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchUncontrolAPBssid.setStatus("current")
_HwBatchUncontrolAPAuthNeighborIndex_Type = OctetString
_HwBatchUncontrolAPAuthNeighborIndex_Object = MibScalar
hwBatchUncontrolAPAuthNeighborIndex = _HwBatchUncontrolAPAuthNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 23),
    _HwBatchUncontrolAPAuthNeighborIndex_Type()
)
hwBatchUncontrolAPAuthNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBatchUncontrolAPAuthNeighborIndex.setStatus("current")
_HwRadioNotifications_ObjectIdentity = ObjectIdentity
hwRadioNotifications = _HwRadioNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24)
)
_HwRadioNotify_ObjectIdentity = ObjectIdentity
hwRadioNotify = _HwRadioNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1)
)
_HwRadioNotifyObjects_ObjectIdentity = ObjectIdentity
hwRadioNotifyObjects = _HwRadioNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3)
)
_HwRadioActualChannel_Type = Unsigned32
_HwRadioActualChannel_Object = MibScalar
hwRadioActualChannel = _HwRadioActualChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 1),
    _HwRadioActualChannel_Type()
)
hwRadioActualChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioActualChannel.setStatus("current")
_HwRadioConflictRate_Type = Unsigned32
_HwRadioConflictRate_Object = MibScalar
hwRadioConflictRate = _HwRadioConflictRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 2),
    _HwRadioConflictRate_Type()
)
hwRadioConflictRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioConflictRate.setStatus("current")
_HwApMonitorMode_Type = Integer32
_HwApMonitorMode_Object = MibScalar
hwApMonitorMode = _HwApMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 3),
    _HwApMonitorMode_Type()
)
hwApMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMonitorMode.setStatus("current")
_HwApPreMonitorMode_Type = Integer32
_HwApPreMonitorMode_Object = MibScalar
hwApPreMonitorMode = _HwApPreMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 4),
    _HwApPreMonitorMode_Type()
)
hwApPreMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPreMonitorMode.setStatus("current")
_HwApChannel_Type = Integer32
_HwApChannel_Object = MibScalar
hwApChannel = _HwApChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 5),
    _HwApChannel_Type()
)
hwApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApChannel.setStatus("current")
_HwApInterfBssid_Type = MacAddress
_HwApInterfBssid_Object = MibScalar
hwApInterfBssid = _HwApInterfBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 6),
    _HwApInterfBssid_Type()
)
hwApInterfBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApInterfBssid.setStatus("current")
_HwInterfStaMac_Type = OctetString
_HwInterfStaMac_Object = MibScalar
hwInterfStaMac = _HwInterfStaMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 7),
    _HwInterfStaMac_Type()
)
hwInterfStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfStaMac.setStatus("current")
_HwRadioDownCause_Type = Integer32
_HwRadioDownCause_Object = MibScalar
hwRadioDownCause = _HwRadioDownCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 8),
    _HwRadioDownCause_Type()
)
hwRadioDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDownCause.setStatus("current")
_HwInterfApChannel_Type = Integer32
_HwInterfApChannel_Object = MibScalar
hwInterfApChannel = _HwInterfApChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 9),
    _HwInterfApChannel_Type()
)
hwInterfApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfApChannel.setStatus("current")
_HwInterfRSSI_Type = Integer32
_HwInterfRSSI_Object = MibScalar
hwInterfRSSI = _HwInterfRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 10),
    _HwInterfRSSI_Type()
)
hwInterfRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfRSSI.setStatus("current")
_HwWIDSTrapInfoAPID_Type = Integer32
_HwWIDSTrapInfoAPID_Object = MibScalar
hwWIDSTrapInfoAPID = _HwWIDSTrapInfoAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 11),
    _HwWIDSTrapInfoAPID_Type()
)
hwWIDSTrapInfoAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoAPID.setStatus("current")
_HwWIDSTrapInfoRadioId_Type = Integer32
_HwWIDSTrapInfoRadioId_Object = MibScalar
hwWIDSTrapInfoRadioId = _HwWIDSTrapInfoRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 12),
    _HwWIDSTrapInfoRadioId_Type()
)
hwWIDSTrapInfoRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRadioId.setStatus("current")
_HwWIDSTrapInfoAPMAC_Type = MacAddress
_HwWIDSTrapInfoAPMAC_Object = MibScalar
hwWIDSTrapInfoAPMAC = _HwWIDSTrapInfoAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 13),
    _HwWIDSTrapInfoAPMAC_Type()
)
hwWIDSTrapInfoAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoAPMAC.setStatus("current")
_HwWIDSTrapInfoRogueMAC_Type = MacAddress
_HwWIDSTrapInfoRogueMAC_Object = MibScalar
hwWIDSTrapInfoRogueMAC = _HwWIDSTrapInfoRogueMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 14),
    _HwWIDSTrapInfoRogueMAC_Type()
)
hwWIDSTrapInfoRogueMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRogueMAC.setStatus("current")


class _HwWIDSTrapInfoRogueSSId_Type(OctetString):
    """Custom type hwWIDSTrapInfoRogueSSId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWIDSTrapInfoRogueSSId_Type.__name__ = "OctetString"
_HwWIDSTrapInfoRogueSSId_Object = MibScalar
hwWIDSTrapInfoRogueSSId = _HwWIDSTrapInfoRogueSSId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 15),
    _HwWIDSTrapInfoRogueSSId_Type()
)
hwWIDSTrapInfoRogueSSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRogueSSId.setStatus("current")
_HwWIDSTrapInfoRogueType_Type = Integer32
_HwWIDSTrapInfoRogueType_Object = MibScalar
hwWIDSTrapInfoRogueType = _HwWIDSTrapInfoRogueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 16),
    _HwWIDSTrapInfoRogueType_Type()
)
hwWIDSTrapInfoRogueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRogueType.setStatus("current")
_HwWIDSTrapInfoRogueRSSI_Type = Integer32
_HwWIDSTrapInfoRogueRSSI_Object = MibScalar
hwWIDSTrapInfoRogueRSSI = _HwWIDSTrapInfoRogueRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 17),
    _HwWIDSTrapInfoRogueRSSI_Type()
)
hwWIDSTrapInfoRogueRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRogueRSSI.setStatus("current")
_HwWIDSTrapInfoRogueChanID_Type = Integer32
_HwWIDSTrapInfoRogueChanID_Object = MibScalar
hwWIDSTrapInfoRogueChanID = _HwWIDSTrapInfoRogueChanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 18),
    _HwWIDSTrapInfoRogueChanID_Type()
)
hwWIDSTrapInfoRogueChanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWIDSTrapInfoRogueChanID.setStatus("current")


class _HwRadioActualChannelBandwidth_Type(Integer32):
    """Custom type hwRadioActualChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40Minus", 3),
          ("ht40Plus", 2))
    )


_HwRadioActualChannelBandwidth_Type.__name__ = "Integer32"
_HwRadioActualChannelBandwidth_Object = MibScalar
hwRadioActualChannelBandwidth = _HwRadioActualChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 19),
    _HwRadioActualChannelBandwidth_Type()
)
hwRadioActualChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioActualChannelBandwidth.setStatus("current")
_HwRadioActualPowerLevel_Type = Integer32
_HwRadioActualPowerLevel_Object = MibScalar
hwRadioActualPowerLevel = _HwRadioActualPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 20),
    _HwRadioActualPowerLevel_Type()
)
hwRadioActualPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioActualPowerLevel.setStatus("current")
_HwRadioActualAntennaGain_Type = Integer32
_HwRadioActualAntennaGain_Object = MibScalar
hwRadioActualAntennaGain = _HwRadioActualAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 21),
    _HwRadioActualAntennaGain_Type()
)
hwRadioActualAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioActualAntennaGain.setStatus("current")
_HwRadioLegitimateAntennaGain_Type = Integer32
_HwRadioLegitimateAntennaGain_Object = MibScalar
hwRadioLegitimateAntennaGain = _HwRadioLegitimateAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 22),
    _HwRadioLegitimateAntennaGain_Type()
)
hwRadioLegitimateAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioLegitimateAntennaGain.setStatus("current")


class _HwRadioChannelChangedReason_Type(Integer32):
    """Custom type hwRadioChannelChangedReason based on Integer32"""
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
        *(("calibrate", 5),
          ("config", 4),
          ("dfs", 2),
          ("mesh", 6),
          ("unknown", 1),
          ("wds", 3))
    )


_HwRadioChannelChangedReason_Type.__name__ = "Integer32"
_HwRadioChannelChangedReason_Object = MibScalar
hwRadioChannelChangedReason = _HwRadioChannelChangedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 23),
    _HwRadioChannelChangedReason_Type()
)
hwRadioChannelChangedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioChannelChangedReason.setStatus("current")
_HwRadioChannelChangedReasonStr_Type = OctetString
_HwRadioChannelChangedReasonStr_Object = MibScalar
hwRadioChannelChangedReasonStr = _HwRadioChannelChangedReasonStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 24),
    _HwRadioChannelChangedReasonStr_Type()
)
hwRadioChannelChangedReasonStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioChannelChangedReasonStr.setStatus("current")
_HwRadioDownCauseStr_Type = OctetString
_HwRadioDownCauseStr_Object = MibScalar
hwRadioDownCauseStr = _HwRadioDownCauseStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 25),
    _HwRadioDownCauseStr_Type()
)
hwRadioDownCauseStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDownCauseStr.setStatus("current")
_HwRadioUacUserNum_Type = Integer32
_HwRadioUacUserNum_Object = MibScalar
hwRadioUacUserNum = _HwRadioUacUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 26),
    _HwRadioUacUserNum_Type()
)
hwRadioUacUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioUacUserNum.setStatus("current")
_HwRadioPreActualChannel_Type = Integer32
_HwRadioPreActualChannel_Object = MibScalar
hwRadioPreActualChannel = _HwRadioPreActualChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 27),
    _HwRadioPreActualChannel_Type()
)
hwRadioPreActualChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPreActualChannel.setStatus("current")
_HwRadioPowerChangedReasonStr_Type = OctetString
_HwRadioPowerChangedReasonStr_Object = MibScalar
hwRadioPowerChangedReasonStr = _HwRadioPowerChangedReasonStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 3, 28),
    _HwRadioPowerChangedReasonStr_Type()
)
hwRadioPowerChangedReasonStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPowerChangedReasonStr.setStatus("current")
_HwRadioParaStatisticTable_Object = MibTable
hwRadioParaStatisticTable = _HwRadioParaStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 25)
)
if mibBuilder.loadTexts:
    hwRadioParaStatisticTable.setStatus("current")
_HwRadioParaStatisticEntry_Object = MibTableRow
hwRadioParaStatisticEntry = _HwRadioParaStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 25, 1)
)
hwRadioParaStatisticEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioParaStatisticEntry.setStatus("current")
_HwRadioStaAveSignalStrength_Type = Integer32
_HwRadioStaAveSignalStrength_Object = MibTableColumn
hwRadioStaAveSignalStrength = _HwRadioStaAveSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 25, 1, 1),
    _HwRadioStaAveSignalStrength_Type()
)
hwRadioStaAveSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaAveSignalStrength.setStatus("current")
_HwMacRadioManageTable_Object = MibTable
hwMacRadioManageTable = _HwMacRadioManageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26)
)
if mibBuilder.loadTexts:
    hwMacRadioManageTable.setStatus("current")
_HwMacRadioManageEntry_Object = MibTableRow
hwMacRadioManageEntry = _HwMacRadioManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1)
)
hwMacRadioManageEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwMacRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioManageEntry.setStatus("current")
_HwMacRadioID_Type = Unsigned32
_HwMacRadioID_Object = MibTableColumn
hwMacRadioID = _HwMacRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 1),
    _HwMacRadioID_Type()
)
hwMacRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacRadioID.setStatus("current")
_HwMacRadioMngBaseBssID_Type = MacAddress
_HwMacRadioMngBaseBssID_Object = MibTableColumn
hwMacRadioMngBaseBssID = _HwMacRadioMngBaseBssID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 2),
    _HwMacRadioMngBaseBssID_Type()
)
hwMacRadioMngBaseBssID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioMngBaseBssID.setStatus("current")
_HwMacRadioMngRadioProfileName_Type = OctetString
_HwMacRadioMngRadioProfileName_Object = MibTableColumn
hwMacRadioMngRadioProfileName = _HwMacRadioMngRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 3),
    _HwMacRadioMngRadioProfileName_Type()
)
hwMacRadioMngRadioProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngRadioProfileName.setStatus("current")


class _HwMacRadioMngState_Type(Integer32):
    """Custom type hwMacRadioMngState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMacRadioMngState_Type.__name__ = "Integer32"
_HwMacRadioMngState_Object = MibTableColumn
hwMacRadioMngState = _HwMacRadioMngState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 4),
    _HwMacRadioMngState_Type()
)
hwMacRadioMngState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngState.setStatus("current")
_HwMacRadioMngChannel_Type = Unsigned32
_HwMacRadioMngChannel_Object = MibTableColumn
hwMacRadioMngChannel = _HwMacRadioMngChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 5),
    _HwMacRadioMngChannel_Type()
)
hwMacRadioMngChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngChannel.setStatus("current")
_HwMacRadioMngPowerLevel_Type = Unsigned32
_HwMacRadioMngPowerLevel_Object = MibTableColumn
hwMacRadioMngPowerLevel = _HwMacRadioMngPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 6),
    _HwMacRadioMngPowerLevel_Type()
)
hwMacRadioMngPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngPowerLevel.setStatus("current")
_HwMacRadioMngPower_Type = Integer32
_HwMacRadioMngPower_Object = MibTableColumn
hwMacRadioMngPower = _HwMacRadioMngPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 7),
    _HwMacRadioMngPower_Type()
)
hwMacRadioMngPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngPower.setStatus("current")
if mibBuilder.loadTexts:
    hwMacRadioMngPower.setUnits("dBm")


class _HwMacRadioAvailableSntennaNumber_Type(Integer32):
    """Custom type hwMacRadioAvailableSntennaNumber based on Integer32"""
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
        *(("all", 1),
          ("num0", 2),
          ("num1", 3),
          ("num2", 4),
          ("num3", 5),
          ("num4", 6),
          ("num5", 7))
    )


_HwMacRadioAvailableSntennaNumber_Type.__name__ = "Integer32"
_HwMacRadioAvailableSntennaNumber_Object = MibTableColumn
hwMacRadioAvailableSntennaNumber = _HwMacRadioAvailableSntennaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 8),
    _HwMacRadioAvailableSntennaNumber_Type()
)
hwMacRadioAvailableSntennaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAvailableSntennaNumber.setStatus("current")
_HwMacRadioWorkingChannel_Type = Unsigned32
_HwMacRadioWorkingChannel_Object = MibTableColumn
hwMacRadioWorkingChannel = _HwMacRadioWorkingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 9),
    _HwMacRadioWorkingChannel_Type()
)
hwMacRadioWorkingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioWorkingChannel.setStatus("current")
_HwMacRadioWorkingPowerLevel_Type = Unsigned32
_HwMacRadioWorkingPowerLevel_Object = MibTableColumn
hwMacRadioWorkingPowerLevel = _HwMacRadioWorkingPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 10),
    _HwMacRadioWorkingPowerLevel_Type()
)
hwMacRadioWorkingPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioWorkingPowerLevel.setStatus("current")
_HwMacRadioWorkingPower_Type = Unsigned32
_HwMacRadioWorkingPower_Object = MibTableColumn
hwMacRadioWorkingPower = _HwMacRadioWorkingPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 11),
    _HwMacRadioWorkingPower_Type()
)
hwMacRadioWorkingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioWorkingPower.setStatus("current")


class _HwMacRadioMngChannelBandwidth_Type(Integer32):
    """Custom type hwMacRadioMngChannelBandwidth based on Integer32"""
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
        *(("ht20", 1),
          ("ht40Minus", 3),
          ("ht40Plus", 2),
          ("ht80", 4))
    )


_HwMacRadioMngChannelBandwidth_Type.__name__ = "Integer32"
_HwMacRadioMngChannelBandwidth_Object = MibTableColumn
hwMacRadioMngChannelBandwidth = _HwMacRadioMngChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 12),
    _HwMacRadioMngChannelBandwidth_Type()
)
hwMacRadioMngChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngChannelBandwidth.setStatus("current")


class _HwMacRadioWorkingChannelBandwidth_Type(Integer32):
    """Custom type hwMacRadioWorkingChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40Minus", 3),
          ("ht40Plus", 2),
          ("ht80", 4),
          ("unknown", -1))
    )


_HwMacRadioWorkingChannelBandwidth_Type.__name__ = "Integer32"
_HwMacRadioWorkingChannelBandwidth_Object = MibTableColumn
hwMacRadioWorkingChannelBandwidth = _HwMacRadioWorkingChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 13),
    _HwMacRadioWorkingChannelBandwidth_Type()
)
hwMacRadioWorkingChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioWorkingChannelBandwidth.setStatus("current")
_HwMacRadio80211nMCSValue_Type = Integer32
_HwMacRadio80211nMCSValue_Object = MibTableColumn
hwMacRadio80211nMCSValue = _HwMacRadio80211nMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 14),
    _HwMacRadio80211nMCSValue_Type()
)
hwMacRadio80211nMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadio80211nMCSValue.setStatus("current")


class _HwMacRadioWidsWorkMode_Type(Integer32):
    """Custom type hwMacRadioWidsWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HwMacRadioWidsWorkMode_Type.__name__ = "Integer32"
_HwMacRadioWidsWorkMode_Object = MibTableColumn
hwMacRadioWidsWorkMode = _HwMacRadioWidsWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 15),
    _HwMacRadioWidsWorkMode_Type()
)
hwMacRadioWidsWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioWidsWorkMode.setStatus("current")


class _HwMacRadioMngBinded_Type(Integer32):
    """Custom type hwMacRadioMngBinded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", -1))
    )


_HwMacRadioMngBinded_Type.__name__ = "Integer32"
_HwMacRadioMngBinded_Object = MibTableColumn
hwMacRadioMngBinded = _HwMacRadioMngBinded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 16),
    _HwMacRadioMngBinded_Type()
)
hwMacRadioMngBinded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMngBinded.setStatus("current")
_HwMacRadioMaxTxPwrLvl_Type = Integer32
_HwMacRadioMaxTxPwrLvl_Object = MibTableColumn
hwMacRadioMaxTxPwrLvl = _HwMacRadioMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 18),
    _HwMacRadioMaxTxPwrLvl_Type()
)
hwMacRadioMaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioMaxTxPwrLvl.setStatus("current")
_HwMacRadioPwrAttRange_Type = Integer32
_HwMacRadioPwrAttRange_Object = MibTableColumn
hwMacRadioPwrAttRange = _HwMacRadioPwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 19),
    _HwMacRadioPwrAttRange_Type()
)
hwMacRadioPwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioPwrAttRange.setStatus("current")
_HwMacRadioPwrAttValue_Type = Integer32
_HwMacRadioPwrAttValue_Object = MibTableColumn
hwMacRadioPwrAttValue = _HwMacRadioPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 20),
    _HwMacRadioPwrAttValue_Type()
)
hwMacRadioPwrAttValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioPwrAttValue.setStatus("current")
_HwMacRadioAntennaGain_Type = Integer32
_HwMacRadioAntennaGain_Object = MibTableColumn
hwMacRadioAntennaGain = _HwMacRadioAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 21),
    _HwMacRadioAntennaGain_Type()
)
hwMacRadioAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAntennaGain.setStatus("current")


class _HwMacRadioBridgeWhitelistEnable_Type(Integer32):
    """Custom type hwMacRadioBridgeWhitelistEnable based on Integer32"""
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


_HwMacRadioBridgeWhitelistEnable_Type.__name__ = "Integer32"
_HwMacRadioBridgeWhitelistEnable_Object = MibTableColumn
hwMacRadioBridgeWhitelistEnable = _HwMacRadioBridgeWhitelistEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 22),
    _HwMacRadioBridgeWhitelistEnable_Type()
)
hwMacRadioBridgeWhitelistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioBridgeWhitelistEnable.setStatus("current")


class _HwMacRadioBridgeWhitelistName_Type(OctetString):
    """Custom type hwMacRadioBridgeWhitelistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMacRadioBridgeWhitelistName_Type.__name__ = "OctetString"
_HwMacRadioBridgeWhitelistName_Object = MibTableColumn
hwMacRadioBridgeWhitelistName = _HwMacRadioBridgeWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 23),
    _HwMacRadioBridgeWhitelistName_Type()
)
hwMacRadioBridgeWhitelistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioBridgeWhitelistName.setStatus("current")


class _HwMacRadioBridgeStpSwitch_Type(Integer32):
    """Custom type hwMacRadioBridgeStpSwitch based on Integer32"""
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


_HwMacRadioBridgeStpSwitch_Type.__name__ = "Integer32"
_HwMacRadioBridgeStpSwitch_Object = MibTableColumn
hwMacRadioBridgeStpSwitch = _HwMacRadioBridgeStpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 24),
    _HwMacRadioBridgeStpSwitch_Type()
)
hwMacRadioBridgeStpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioBridgeStpSwitch.setStatus("current")


class _HwMacRadioBridgeSwitch_Type(Integer32):
    """Custom type hwMacRadioBridgeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMacRadioBridgeSwitch_Type.__name__ = "Integer32"
_HwMacRadioBridgeSwitch_Object = MibTableColumn
hwMacRadioBridgeSwitch = _HwMacRadioBridgeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 25),
    _HwMacRadioBridgeSwitch_Type()
)
hwMacRadioBridgeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioBridgeSwitch.setStatus("current")


class _HwMacRadioBridgeMode_Type(Integer32):
    """Custom type hwMacRadioBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 3),
          ("middle", 1),
          ("root", 2))
    )


_HwMacRadioBridgeMode_Type.__name__ = "Integer32"
_HwMacRadioBridgeMode_Object = MibTableColumn
hwMacRadioBridgeMode = _HwMacRadioBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 26),
    _HwMacRadioBridgeMode_Type()
)
hwMacRadioBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioBridgeMode.setStatus("current")
_HwMacRadioUndoBridgeWhitelist_Type = Integer32
_HwMacRadioUndoBridgeWhitelist_Object = MibTableColumn
hwMacRadioUndoBridgeWhitelist = _HwMacRadioUndoBridgeWhitelist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 27),
    _HwMacRadioUndoBridgeWhitelist_Type()
)
hwMacRadioUndoBridgeWhitelist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioUndoBridgeWhitelist.setStatus("current")


class _HwMacRadioUserTrafficScheduler_Type(Integer32):
    """Custom type hwMacRadioUserTrafficScheduler based on Integer32"""
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


_HwMacRadioUserTrafficScheduler_Type.__name__ = "Integer32"
_HwMacRadioUserTrafficScheduler_Object = MibTableColumn
hwMacRadioUserTrafficScheduler = _HwMacRadioUserTrafficScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 28),
    _HwMacRadioUserTrafficScheduler_Type()
)
hwMacRadioUserTrafficScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioUserTrafficScheduler.setStatus("obsolete")


class _HwMacRadioCountermeasuresMode_Type(Unsigned32):
    """Custom type hwMacRadioCountermeasuresMode based on Unsigned32"""
    defaultValue = 0


_HwMacRadioCountermeasuresMode_Object = MibTableColumn
hwMacRadioCountermeasuresMode = _HwMacRadioCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 29),
    _HwMacRadioCountermeasuresMode_Type()
)
hwMacRadioCountermeasuresMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioCountermeasuresMode.setStatus("current")


class _HwMacRadioFrequency_Type(Integer32):
    """Custom type hwMacRadioFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frequency2G", 1),
          ("frequency5G", 2))
    )


_HwMacRadioFrequency_Type.__name__ = "Integer32"
_HwMacRadioFrequency_Object = MibTableColumn
hwMacRadioFrequency = _HwMacRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 30),
    _HwMacRadioFrequency_Type()
)
hwMacRadioFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioFrequency.setStatus("current")


class _HwMacRadioCountermeasuresSwitch_Type(Integer32):
    """Custom type hwMacRadioCountermeasuresSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMacRadioCountermeasuresSwitch_Type.__name__ = "Integer32"
_HwMacRadioCountermeasuresSwitch_Object = MibTableColumn
hwMacRadioCountermeasuresSwitch = _HwMacRadioCountermeasuresSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 31),
    _HwMacRadioCountermeasuresSwitch_Type()
)
hwMacRadioCountermeasuresSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioCountermeasuresSwitch.setStatus("current")
_HwMacRadioSpectrumAnalysisEnable_Type = Integer32
_HwMacRadioSpectrumAnalysisEnable_Object = MibTableColumn
hwMacRadioSpectrumAnalysisEnable = _HwMacRadioSpectrumAnalysisEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 32),
    _HwMacRadioSpectrumAnalysisEnable_Type()
)
hwMacRadioSpectrumAnalysisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioSpectrumAnalysisEnable.setStatus("current")
_HwMACRadioWidsAttackDetEnable_Type = Integer32
_HwMACRadioWidsAttackDetEnable_Object = MibTableColumn
hwMACRadioWidsAttackDetEnable = _HwMACRadioWidsAttackDetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 33),
    _HwMACRadioWidsAttackDetEnable_Type()
)
hwMACRadioWidsAttackDetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMACRadioWidsAttackDetEnable.setStatus("current")
_HwMacRadioMeshWhitelistName_Type = OctetString
_HwMacRadioMeshWhitelistName_Object = MibTableColumn
hwMacRadioMeshWhitelistName = _HwMacRadioMeshWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 34),
    _HwMacRadioMeshWhitelistName_Type()
)
hwMacRadioMeshWhitelistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMeshWhitelistName.setStatus("current")
_HwMacUndoMeshWhitelist_Type = Integer32
_HwMacUndoMeshWhitelist_Object = MibTableColumn
hwMacUndoMeshWhitelist = _HwMacUndoMeshWhitelist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 35),
    _HwMacUndoMeshWhitelist_Type()
)
hwMacUndoMeshWhitelist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacUndoMeshWhitelist.setStatus("current")


class _HwMacRadioMeshRole_Type(Integer32):
    """Custom type hwMacRadioMeshRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meshNode", 1),
          ("meshPortal", 2))
    )


_HwMacRadioMeshRole_Type.__name__ = "Integer32"
_HwMacRadioMeshRole_Object = MibTableColumn
hwMacRadioMeshRole = _HwMacRadioMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 36),
    _HwMacRadioMeshRole_Type()
)
hwMacRadioMeshRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMeshRole.setStatus("current")


class _HwMacRadioLocationEnable_Type(Integer32):
    """Custom type hwMacRadioLocationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacRadioLocationEnable_Type.__name__ = "Integer32"
_HwMacRadioLocationEnable_Object = MibTableColumn
hwMacRadioLocationEnable = _HwMacRadioLocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 37),
    _HwMacRadioLocationEnable_Type()
)
hwMacRadioLocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioLocationEnable.setStatus("current")


class _HwMacRadioLocationScanChannelEnable_Type(Integer32):
    """Custom type hwMacRadioLocationScanChannelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacRadioLocationScanChannelEnable_Type.__name__ = "Integer32"
_HwMacRadioLocationScanChannelEnable_Object = MibTableColumn
hwMacRadioLocationScanChannelEnable = _HwMacRadioLocationScanChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 38),
    _HwMacRadioLocationScanChannelEnable_Type()
)
hwMacRadioLocationScanChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioLocationScanChannelEnable.setStatus("current")
_HwMacRadio80211nMulticastMCSValue_Type = Integer32
_HwMacRadio80211nMulticastMCSValue_Object = MibTableColumn
hwMacRadio80211nMulticastMCSValue = _HwMacRadio80211nMulticastMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 39),
    _HwMacRadio80211nMulticastMCSValue_Type()
)
hwMacRadio80211nMulticastMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadio80211nMulticastMCSValue.setStatus("current")


class _HwMacRadioSpectrogramServerReportEnable_Type(Integer32):
    """Custom type hwMacRadioSpectrogramServerReportEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacRadioSpectrogramServerReportEnable_Type.__name__ = "Integer32"
_HwMacRadioSpectrogramServerReportEnable_Object = MibTableColumn
hwMacRadioSpectrogramServerReportEnable = _HwMacRadioSpectrogramServerReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 40),
    _HwMacRadioSpectrogramServerReportEnable_Type()
)
hwMacRadioSpectrogramServerReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioSpectrogramServerReportEnable.setStatus("current")


class _HwMacRadioMulticastRateValue_Type(Integer32):
    """Custom type hwMacRadioMulticastRateValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 1),
          ("rate11", 6),
          ("rate12", 7),
          ("rate18", 8),
          ("rate2", 2),
          ("rate24", 10),
          ("rate36", 12),
          ("rate48", 13),
          ("rate54", 14),
          ("rate55", 3),
          ("rate6", 4),
          ("rate9", 5),
          ("unknow", -1))
    )


_HwMacRadioMulticastRateValue_Type.__name__ = "Integer32"
_HwMacRadioMulticastRateValue_Object = MibTableColumn
hwMacRadioMulticastRateValue = _HwMacRadioMulticastRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 41),
    _HwMacRadioMulticastRateValue_Type()
)
hwMacRadioMulticastRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioMulticastRateValue.setStatus("current")


class _HwMacRadio11acSpatialStream_Type(Integer32):
    """Custom type hwMacRadio11acSpatialStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 3),
    )


_HwMacRadio11acSpatialStream_Type.__name__ = "Integer32"
_HwMacRadio11acSpatialStream_Object = MibTableColumn
hwMacRadio11acSpatialStream = _HwMacRadio11acSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 42),
    _HwMacRadio11acSpatialStream_Type()
)
hwMacRadio11acSpatialStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadio11acSpatialStream.setStatus("current")


class _HwMacRadio11acMCSValue_Type(Integer32):
    """Custom type hwMacRadio11acMCSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 9),
    )


_HwMacRadio11acMCSValue_Type.__name__ = "Integer32"
_HwMacRadio11acMCSValue_Object = MibTableColumn
hwMacRadio11acMCSValue = _HwMacRadio11acMCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 43),
    _HwMacRadio11acMCSValue_Type()
)
hwMacRadio11acMCSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadio11acMCSValue.setStatus("current")


class _HwMacRadioActiveSwitch_Type(Integer32):
    """Custom type hwMacRadioActiveSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("dormancy", 1))
    )


_HwMacRadioActiveSwitch_Type.__name__ = "Integer32"
_HwMacRadioActiveSwitch_Object = MibTableColumn
hwMacRadioActiveSwitch = _HwMacRadioActiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 26, 1, 44),
    _HwMacRadioActiveSwitch_Type()
)
hwMacRadioActiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioActiveSwitch.setStatus("current")
_HwMacRadioCalibrateStatisicsTable_Object = MibTable
hwMacRadioCalibrateStatisicsTable = _HwMacRadioCalibrateStatisicsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27)
)
if mibBuilder.loadTexts:
    hwMacRadioCalibrateStatisicsTable.setStatus("current")
_HwMacRadioCalibrateStatisicsEntry_Object = MibTableRow
hwMacRadioCalibrateStatisicsEntry = _HwMacRadioCalibrateStatisicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27, 1)
)
hwMacRadioCalibrateStatisicsEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioCalibrateStatisicsEntry.setStatus("current")
_HwMacRadioCalStatisSignalBadCount_Type = Unsigned32
_HwMacRadioCalStatisSignalBadCount_Object = MibTableColumn
hwMacRadioCalStatisSignalBadCount = _HwMacRadioCalStatisSignalBadCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27, 1, 1),
    _HwMacRadioCalStatisSignalBadCount_Type()
)
hwMacRadioCalStatisSignalBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioCalStatisSignalBadCount.setStatus("current")
_HwMacRadioCalStatisCalibratePowerCount_Type = Unsigned32
_HwMacRadioCalStatisCalibratePowerCount_Object = MibTableColumn
hwMacRadioCalStatisCalibratePowerCount = _HwMacRadioCalStatisCalibratePowerCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27, 1, 2),
    _HwMacRadioCalStatisCalibratePowerCount_Type()
)
hwMacRadioCalStatisCalibratePowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioCalStatisCalibratePowerCount.setStatus("current")
_HwMacRadioCalStatisCalibrateChannelCount_Type = Unsigned32
_HwMacRadioCalStatisCalibrateChannelCount_Object = MibTableColumn
hwMacRadioCalStatisCalibrateChannelCount = _HwMacRadioCalStatisCalibrateChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27, 1, 3),
    _HwMacRadioCalStatisCalibrateChannelCount_Type()
)
hwMacRadioCalStatisCalibrateChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioCalStatisCalibrateChannelCount.setStatus("current")


class _HwMacRadioCalibrateStatisicsOperMode_Type(Integer32):
    """Custom type hwMacRadioCalibrateStatisicsOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearstatistic", 1),
          ("invalid", -1))
    )


_HwMacRadioCalibrateStatisicsOperMode_Type.__name__ = "Integer32"
_HwMacRadioCalibrateStatisicsOperMode_Object = MibTableColumn
hwMacRadioCalibrateStatisicsOperMode = _HwMacRadioCalibrateStatisicsOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 27, 1, 4),
    _HwMacRadioCalibrateStatisicsOperMode_Type()
)
hwMacRadioCalibrateStatisicsOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioCalibrateStatisicsOperMode.setStatus("current")
_HwMacRadioAuthNeighborInfTable_Object = MibTable
hwMacRadioAuthNeighborInfTable = _HwMacRadioAuthNeighborInfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28)
)
if mibBuilder.loadTexts:
    hwMacRadioAuthNeighborInfTable.setStatus("current")
_HwMacRadioAuthNeighborInfEntry_Object = MibTableRow
hwMacRadioAuthNeighborInfEntry = _HwMacRadioAuthNeighborInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1)
)
hwMacRadioAuthNeighborInfEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioAuthNeighborInfEntry.setStatus("current")
_HwMacAuthenticRadioNeighborAPID_Type = OctetString
_HwMacAuthenticRadioNeighborAPID_Object = MibTableColumn
hwMacAuthenticRadioNeighborAPID = _HwMacAuthenticRadioNeighborAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 1),
    _HwMacAuthenticRadioNeighborAPID_Type()
)
hwMacAuthenticRadioNeighborAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborAPID.setStatus("current")
_HwMacAuthenticRadioNeighborChannel_Type = OctetString
_HwMacAuthenticRadioNeighborChannel_Object = MibTableColumn
hwMacAuthenticRadioNeighborChannel = _HwMacAuthenticRadioNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 2),
    _HwMacAuthenticRadioNeighborChannel_Type()
)
hwMacAuthenticRadioNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborChannel.setStatus("current")
_HwMacAuthenticRadioNeighborFrontAttenu_Type = OctetString
_HwMacAuthenticRadioNeighborFrontAttenu_Object = MibTableColumn
hwMacAuthenticRadioNeighborFrontAttenu = _HwMacAuthenticRadioNeighborFrontAttenu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 3),
    _HwMacAuthenticRadioNeighborFrontAttenu_Type()
)
hwMacAuthenticRadioNeighborFrontAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborFrontAttenu.setStatus("current")
_HwMacAuthenticRadioNeighborBackAttenu_Type = OctetString
_HwMacAuthenticRadioNeighborBackAttenu_Object = MibTableColumn
hwMacAuthenticRadioNeighborBackAttenu = _HwMacAuthenticRadioNeighborBackAttenu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 4),
    _HwMacAuthenticRadioNeighborBackAttenu_Type()
)
hwMacAuthenticRadioNeighborBackAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborBackAttenu.setStatus("current")
_HwMacAuthenticRadioNeighborAPMac_Type = OctetString
_HwMacAuthenticRadioNeighborAPMac_Object = MibTableColumn
hwMacAuthenticRadioNeighborAPMac = _HwMacAuthenticRadioNeighborAPMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 5),
    _HwMacAuthenticRadioNeighborAPMac_Type()
)
hwMacAuthenticRadioNeighborAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborAPMac.setStatus("current")
_HwMacAuthenticRadioNeighborSSID_Type = OctetString
_HwMacAuthenticRadioNeighborSSID_Object = MibTableColumn
hwMacAuthenticRadioNeighborSSID = _HwMacAuthenticRadioNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 28, 1, 6),
    _HwMacAuthenticRadioNeighborSSID_Type()
)
hwMacAuthenticRadioNeighborSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAuthenticRadioNeighborSSID.setStatus("current")
_HwMacRadioLoadBalanceGroupMemberTable_Object = MibTable
hwMacRadioLoadBalanceGroupMemberTable = _HwMacRadioLoadBalanceGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29)
)
if mibBuilder.loadTexts:
    hwMacRadioLoadBalanceGroupMemberTable.setStatus("current")
_HwMacRadioLoadBalanceGroupMemberEntry_Object = MibTableRow
hwMacRadioLoadBalanceGroupMemberEntry = _HwMacRadioLoadBalanceGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1)
)
hwMacRadioLoadBalanceGroupMemberEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwLBGroupName"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioLoadBalanceGroupMemberEntry.setStatus("current")
_HwMacLBMemberRadioChannel_Type = Unsigned32
_HwMacLBMemberRadioChannel_Object = MibTableColumn
hwMacLBMemberRadioChannel = _HwMacLBMemberRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 1),
    _HwMacLBMemberRadioChannel_Type()
)
hwMacLBMemberRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacLBMemberRadioChannel.setStatus("current")
_HwMacLBMemberRadioPowerLevel_Type = Unsigned32
_HwMacLBMemberRadioPowerLevel_Object = MibTableColumn
hwMacLBMemberRadioPowerLevel = _HwMacLBMemberRadioPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 2),
    _HwMacLBMemberRadioPowerLevel_Type()
)
hwMacLBMemberRadioPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacLBMemberRadioPowerLevel.setStatus("current")
_HwMacLBMemberRadioPower_Type = Unsigned32
_HwMacLBMemberRadioPower_Object = MibTableColumn
hwMacLBMemberRadioPower = _HwMacLBMemberRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 3),
    _HwMacLBMemberRadioPower_Type()
)
hwMacLBMemberRadioPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacLBMemberRadioPower.setStatus("current")
_HwMacLBMemberRadioSeesionNum_Type = Unsigned32
_HwMacLBMemberRadioSeesionNum_Object = MibTableColumn
hwMacLBMemberRadioSeesionNum = _HwMacLBMemberRadioSeesionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 4),
    _HwMacLBMemberRadioSeesionNum_Type()
)
hwMacLBMemberRadioSeesionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacLBMemberRadioSeesionNum.setStatus("current")
_HwMacLBMemberRadioTraffic_Type = Unsigned32
_HwMacLBMemberRadioTraffic_Object = MibTableColumn
hwMacLBMemberRadioTraffic = _HwMacLBMemberRadioTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 5),
    _HwMacLBMemberRadioTraffic_Type()
)
hwMacLBMemberRadioTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacLBMemberRadioTraffic.setStatus("current")
_HwMacLBMemberRowStatus_Type = RowStatus
_HwMacLBMemberRowStatus_Object = MibTableColumn
hwMacLBMemberRowStatus = _HwMacLBMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 29, 1, 6),
    _HwMacLBMemberRowStatus_Type()
)
hwMacLBMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLBMemberRowStatus.setStatus("current")
_HwMacRadioPerformanceStatTable_Object = MibTable
hwMacRadioPerformanceStatTable = _HwMacRadioPerformanceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30)
)
if mibBuilder.loadTexts:
    hwMacRadioPerformanceStatTable.setStatus("current")
_HwMacRadioPerformanceStatEntry_Object = MibTableRow
hwMacRadioPerformanceStatEntry = _HwMacRadioPerformanceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1)
)
hwMacRadioPerformanceStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioPerformanceStatEntry.setStatus("current")
_HwMacRadioRcvFrames_Type = Unsigned32
_HwMacRadioRcvFrames_Object = MibTableColumn
hwMacRadioRcvFrames = _HwMacRadioRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 1),
    _HwMacRadioRcvFrames_Type()
)
hwMacRadioRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvFrames.setStatus("current")
_HwMacRadioRcvBytes_Type = Unsigned32
_HwMacRadioRcvBytes_Object = MibTableColumn
hwMacRadioRcvBytes = _HwMacRadioRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 2),
    _HwMacRadioRcvBytes_Type()
)
hwMacRadioRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvBytes.setStatus("current")
_HwMacRadioSendFrames_Type = Unsigned32
_HwMacRadioSendFrames_Object = MibTableColumn
hwMacRadioSendFrames = _HwMacRadioSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 3),
    _HwMacRadioSendFrames_Type()
)
hwMacRadioSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendFrames.setStatus("current")
_HwMacRadioSendBytes_Type = Unsigned32
_HwMacRadioSendBytes_Object = MibTableColumn
hwMacRadioSendBytes = _HwMacRadioSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 4),
    _HwMacRadioSendBytes_Type()
)
hwMacRadioSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendBytes.setStatus("current")
_HwMacRadioSendRtsSuccess_Type = Unsigned32
_HwMacRadioSendRtsSuccess_Object = MibTableColumn
hwMacRadioSendRtsSuccess = _HwMacRadioSendRtsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 5),
    _HwMacRadioSendRtsSuccess_Type()
)
hwMacRadioSendRtsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendRtsSuccess.setStatus("current")
_HwMacRadioSendUnicast_Type = Unsigned32
_HwMacRadioSendUnicast_Object = MibTableColumn
hwMacRadioSendUnicast = _HwMacRadioSendUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 6),
    _HwMacRadioSendUnicast_Type()
)
hwMacRadioSendUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendUnicast.setStatus("current")
_HwMacRadioSendBroadcast_Type = Unsigned32
_HwMacRadioSendBroadcast_Object = MibTableColumn
hwMacRadioSendBroadcast = _HwMacRadioSendBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 7),
    _HwMacRadioSendBroadcast_Type()
)
hwMacRadioSendBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendBroadcast.setStatus("current")
_HwMacRadioSendFailFrames_Type = Unsigned32
_HwMacRadioSendFailFrames_Object = MibTableColumn
hwMacRadioSendFailFrames = _HwMacRadioSendFailFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 8),
    _HwMacRadioSendFailFrames_Type()
)
hwMacRadioSendFailFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendFailFrames.setStatus("current")
_HwMacRadioRcvErrFrames_Type = Unsigned32
_HwMacRadioRcvErrFrames_Object = MibTableColumn
hwMacRadioRcvErrFrames = _HwMacRadioRcvErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 9),
    _HwMacRadioRcvErrFrames_Type()
)
hwMacRadioRcvErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvErrFrames.setStatus("current")
_HwMacRadioRcvPhyErrFrames_Type = Unsigned32
_HwMacRadioRcvPhyErrFrames_Object = MibTableColumn
hwMacRadioRcvPhyErrFrames = _HwMacRadioRcvPhyErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 10),
    _HwMacRadioRcvPhyErrFrames_Type()
)
hwMacRadioRcvPhyErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvPhyErrFrames.setStatus("current")
_HwMacRadioRcvCrcErrFrames_Type = Unsigned32
_HwMacRadioRcvCrcErrFrames_Object = MibTableColumn
hwMacRadioRcvCrcErrFrames = _HwMacRadioRcvCrcErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 11),
    _HwMacRadioRcvCrcErrFrames_Type()
)
hwMacRadioRcvCrcErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvCrcErrFrames.setStatus("current")
_HwMacRadioRcvMicErrFrames_Type = Unsigned32
_HwMacRadioRcvMicErrFrames_Object = MibTableColumn
hwMacRadioRcvMicErrFrames = _HwMacRadioRcvMicErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 12),
    _HwMacRadioRcvMicErrFrames_Type()
)
hwMacRadioRcvMicErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvMicErrFrames.setStatus("current")
_HwMacRadioRcvKeyDecryptErrFrames_Type = Unsigned32
_HwMacRadioRcvKeyDecryptErrFrames_Object = MibTableColumn
hwMacRadioRcvKeyDecryptErrFrames = _HwMacRadioRcvKeyDecryptErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 13),
    _HwMacRadioRcvKeyDecryptErrFrames_Type()
)
hwMacRadioRcvKeyDecryptErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvKeyDecryptErrFrames.setStatus("current")
_HwMacRadioRetryFrames_Type = Unsigned32
_HwMacRadioRetryFrames_Object = MibTableColumn
hwMacRadioRetryFrames = _HwMacRadioRetryFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 14),
    _HwMacRadioRetryFrames_Type()
)
hwMacRadioRetryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRetryFrames.setStatus("current")
_HwMacRadioPER_Type = Unsigned32
_HwMacRadioPER_Object = MibTableColumn
hwMacRadioPER = _HwMacRadioPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 15),
    _HwMacRadioPER_Type()
)
hwMacRadioPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioPER.setStatus("current")
_HwMacRadioChUtilizationRate_Type = Unsigned32
_HwMacRadioChUtilizationRate_Object = MibTableColumn
hwMacRadioChUtilizationRate = _HwMacRadioChUtilizationRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 16),
    _HwMacRadioChUtilizationRate_Type()
)
hwMacRadioChUtilizationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioChUtilizationRate.setStatus("current")


class _HwMacRadioPerformanceStatOperMode_Type(Integer32):
    """Custom type hwMacRadioPerformanceStatOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearstatistic", 1),
          ("invalid", -1))
    )


_HwMacRadioPerformanceStatOperMode_Type.__name__ = "Integer32"
_HwMacRadioPerformanceStatOperMode_Object = MibTableColumn
hwMacRadioPerformanceStatOperMode = _HwMacRadioPerformanceStatOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 17),
    _HwMacRadioPerformanceStatOperMode_Type()
)
hwMacRadioPerformanceStatOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioPerformanceStatOperMode.setStatus("current")
_HwMacRadioPEROfLastPeriod_Type = Unsigned32
_HwMacRadioPEROfLastPeriod_Object = MibTableColumn
hwMacRadioPEROfLastPeriod = _HwMacRadioPEROfLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 18),
    _HwMacRadioPEROfLastPeriod_Type()
)
hwMacRadioPEROfLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioPEROfLastPeriod.setStatus("current")
_HwMacRadioRcvSignalStrength_Type = Integer32
_HwMacRadioRcvSignalStrength_Object = MibTableColumn
hwMacRadioRcvSignalStrength = _HwMacRadioRcvSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 19),
    _HwMacRadioRcvSignalStrength_Type()
)
hwMacRadioRcvSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvSignalStrength.setStatus("current")
_HwMacRadioDownMacErrFrames_Type = Unsigned32
_HwMacRadioDownMacErrFrames_Object = MibTableColumn
hwMacRadioDownMacErrFrames = _HwMacRadioDownMacErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 20),
    _HwMacRadioDownMacErrFrames_Type()
)
hwMacRadioDownMacErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDownMacErrFrames.setStatus("current")
_HwMacRadioRcvPower_Type = Integer32
_HwMacRadioRcvPower_Object = MibTableColumn
hwMacRadioRcvPower = _HwMacRadioRcvPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 21),
    _HwMacRadioRcvPower_Type()
)
hwMacRadioRcvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvPower.setStatus("current")
_HwMacRadioRcvUnicastFrames_Type = Counter64
_HwMacRadioRcvUnicastFrames_Object = MibTableColumn
hwMacRadioRcvUnicastFrames = _HwMacRadioRcvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 22),
    _HwMacRadioRcvUnicastFrames_Type()
)
hwMacRadioRcvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvUnicastFrames.setStatus("current")
_HwMacRadioRcvMngFrames_Type = Counter64
_HwMacRadioRcvMngFrames_Object = MibTableColumn
hwMacRadioRcvMngFrames = _HwMacRadioRcvMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 23),
    _HwMacRadioRcvMngFrames_Type()
)
hwMacRadioRcvMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvMngFrames.setStatus("current")
_HwMacRadioRcvCtrlFrames_Type = Counter64
_HwMacRadioRcvCtrlFrames_Object = MibTableColumn
hwMacRadioRcvCtrlFrames = _HwMacRadioRcvCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 24),
    _HwMacRadioRcvCtrlFrames_Type()
)
hwMacRadioRcvCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvCtrlFrames.setStatus("current")
_HwMacRadioRcvDataFrames_Type = Counter64
_HwMacRadioRcvDataFrames_Object = MibTableColumn
hwMacRadioRcvDataFrames = _HwMacRadioRcvDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 25),
    _HwMacRadioRcvDataFrames_Type()
)
hwMacRadioRcvDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvDataFrames.setStatus("current")
_HwMacRadioSendMngFrames_Type = Counter64
_HwMacRadioSendMngFrames_Object = MibTableColumn
hwMacRadioSendMngFrames = _HwMacRadioSendMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 26),
    _HwMacRadioSendMngFrames_Type()
)
hwMacRadioSendMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendMngFrames.setStatus("current")
_HwMacRadioSendCtrlFrames_Type = Counter64
_HwMacRadioSendCtrlFrames_Object = MibTableColumn
hwMacRadioSendCtrlFrames = _HwMacRadioSendCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 27),
    _HwMacRadioSendCtrlFrames_Type()
)
hwMacRadioSendCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendCtrlFrames.setStatus("current")
_HwMacRadioSendDataFrames_Type = Counter64
_HwMacRadioSendDataFrames_Object = MibTableColumn
hwMacRadioSendDataFrames = _HwMacRadioSendDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 28),
    _HwMacRadioSendDataFrames_Type()
)
hwMacRadioSendDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendDataFrames.setStatus("current")
_HwMacRadioStaMaxSignalStrength_Type = Integer32
_HwMacRadioStaMaxSignalStrength_Object = MibTableColumn
hwMacRadioStaMaxSignalStrength = _HwMacRadioStaMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 29),
    _HwMacRadioStaMaxSignalStrength_Type()
)
hwMacRadioStaMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaMaxSignalStrength.setStatus("current")
_HwMacRadioStaMinSignalStrength_Type = Integer32
_HwMacRadioStaMinSignalStrength_Object = MibTableColumn
hwMacRadioStaMinSignalStrength = _HwMacRadioStaMinSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 30),
    _HwMacRadioStaMinSignalStrength_Type()
)
hwMacRadioStaMinSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaMinSignalStrength.setStatus("current")
_HwMacRadioStaAvgSignalStrength_Type = Integer32
_HwMacRadioStaAvgSignalStrength_Object = MibTableColumn
hwMacRadioStaAvgSignalStrength = _HwMacRadioStaAvgSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 31),
    _HwMacRadioStaAvgSignalStrength_Type()
)
hwMacRadioStaAvgSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaAvgSignalStrength.setStatus("current")
_HwMacRadioSendRate_Type = Unsigned32
_HwMacRadioSendRate_Object = MibTableColumn
hwMacRadioSendRate = _HwMacRadioSendRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 32),
    _HwMacRadioSendRate_Type()
)
hwMacRadioSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendRate.setStatus("current")
_HwMacRadioRecvRate_Type = Unsigned32
_HwMacRadioRecvRate_Object = MibTableColumn
hwMacRadioRecvRate = _HwMacRadioRecvRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 33),
    _HwMacRadioRecvRate_Type()
)
hwMacRadioRecvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRecvRate.setStatus("current")
_HwMacRadioDropRate_Type = Unsigned32
_HwMacRadioDropRate_Object = MibTableColumn
hwMacRadioDropRate = _HwMacRadioDropRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 34),
    _HwMacRadioDropRate_Type()
)
hwMacRadioDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDropRate.setStatus("current")
_HwMacRadioAirPortDhcpFrames_Type = Counter64
_HwMacRadioAirPortDhcpFrames_Object = MibTableColumn
hwMacRadioAirPortDhcpFrames = _HwMacRadioAirPortDhcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 35),
    _HwMacRadioAirPortDhcpFrames_Type()
)
hwMacRadioAirPortDhcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioAirPortDhcpFrames.setStatus("current")
_HwMacRadioAirPortEapolFrames_Type = Counter64
_HwMacRadioAirPortEapolFrames_Object = MibTableColumn
hwMacRadioAirPortEapolFrames = _HwMacRadioAirPortEapolFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 36),
    _HwMacRadioAirPortEapolFrames_Type()
)
hwMacRadioAirPortEapolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioAirPortEapolFrames.setStatus("current")
_HwMacRadioAirPortPsPollFrames_Type = Counter64
_HwMacRadioAirPortPsPollFrames_Object = MibTableColumn
hwMacRadioAirPortPsPollFrames = _HwMacRadioAirPortPsPollFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 37),
    _HwMacRadioAirPortPsPollFrames_Type()
)
hwMacRadioAirPortPsPollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioAirPortPsPollFrames.setStatus("current")
_HwMacRadioAssocRequestFrames_Type = Counter64
_HwMacRadioAssocRequestFrames_Object = MibTableColumn
hwMacRadioAssocRequestFrames = _HwMacRadioAssocRequestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 38),
    _HwMacRadioAssocRequestFrames_Type()
)
hwMacRadioAssocRequestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioAssocRequestFrames.setStatus("current")
_HwMacRadioAssocResponseFrames_Type = Counter64
_HwMacRadioAssocResponseFrames_Object = MibTableColumn
hwMacRadioAssocResponseFrames = _HwMacRadioAssocResponseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 39),
    _HwMacRadioAssocResponseFrames_Type()
)
hwMacRadioAssocResponseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioAssocResponseFrames.setStatus("current")
_HwMacRadioReassocRequestFrames_Type = Counter64
_HwMacRadioReassocRequestFrames_Object = MibTableColumn
hwMacRadioReassocRequestFrames = _HwMacRadioReassocRequestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 40),
    _HwMacRadioReassocRequestFrames_Type()
)
hwMacRadioReassocRequestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioReassocRequestFrames.setStatus("current")
_HwMacRadioReassocResponseFrames_Type = Counter64
_HwMacRadioReassocResponseFrames_Object = MibTableColumn
hwMacRadioReassocResponseFrames = _HwMacRadioReassocResponseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 41),
    _HwMacRadioReassocResponseFrames_Type()
)
hwMacRadioReassocResponseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioReassocResponseFrames.setStatus("current")
_HwMacRadioDisassocFrames_Type = Counter64
_HwMacRadioDisassocFrames_Object = MibTableColumn
hwMacRadioDisassocFrames = _HwMacRadioDisassocFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 42),
    _HwMacRadioDisassocFrames_Type()
)
hwMacRadioDisassocFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDisassocFrames.setStatus("current")
_HwMacRadioDisauthFrames_Type = Counter64
_HwMacRadioDisauthFrames_Object = MibTableColumn
hwMacRadioDisauthFrames = _HwMacRadioDisauthFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 43),
    _HwMacRadioDisauthFrames_Type()
)
hwMacRadioDisauthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDisauthFrames.setStatus("current")
_HwMacRadioRcvFrames64Bits_Type = Counter64
_HwMacRadioRcvFrames64Bits_Object = MibTableColumn
hwMacRadioRcvFrames64Bits = _HwMacRadioRcvFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 44),
    _HwMacRadioRcvFrames64Bits_Type()
)
hwMacRadioRcvFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvFrames64Bits.setStatus("current")
_HwMacRadioRcvBytes64Bits_Type = Counter64
_HwMacRadioRcvBytes64Bits_Object = MibTableColumn
hwMacRadioRcvBytes64Bits = _HwMacRadioRcvBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 45),
    _HwMacRadioRcvBytes64Bits_Type()
)
hwMacRadioRcvBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvBytes64Bits.setStatus("current")
_HwMacRadioSendFrames64Bits_Type = Counter64
_HwMacRadioSendFrames64Bits_Object = MibTableColumn
hwMacRadioSendFrames64Bits = _HwMacRadioSendFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 46),
    _HwMacRadioSendFrames64Bits_Type()
)
hwMacRadioSendFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendFrames64Bits.setStatus("current")
_HwMacRadioSendBytes64Bits_Type = Counter64
_HwMacRadioSendBytes64Bits_Object = MibTableColumn
hwMacRadioSendBytes64Bits = _HwMacRadioSendBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 47),
    _HwMacRadioSendBytes64Bits_Type()
)
hwMacRadioSendBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendBytes64Bits.setStatus("current")
_HwMacRadioSendRtsSuccess64Bits_Type = Counter64
_HwMacRadioSendRtsSuccess64Bits_Object = MibTableColumn
hwMacRadioSendRtsSuccess64Bits = _HwMacRadioSendRtsSuccess64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 48),
    _HwMacRadioSendRtsSuccess64Bits_Type()
)
hwMacRadioSendRtsSuccess64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendRtsSuccess64Bits.setStatus("current")
_HwMacRadioSendUnicast64Bits_Type = Counter64
_HwMacRadioSendUnicast64Bits_Object = MibTableColumn
hwMacRadioSendUnicast64Bits = _HwMacRadioSendUnicast64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 49),
    _HwMacRadioSendUnicast64Bits_Type()
)
hwMacRadioSendUnicast64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendUnicast64Bits.setStatus("current")
_HwMacRadioSendBroadcast64Bits_Type = Counter64
_HwMacRadioSendBroadcast64Bits_Object = MibTableColumn
hwMacRadioSendBroadcast64Bits = _HwMacRadioSendBroadcast64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 50),
    _HwMacRadioSendBroadcast64Bits_Type()
)
hwMacRadioSendBroadcast64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendBroadcast64Bits.setStatus("current")
_HwMacRadioSendFailFrames64Bits_Type = Counter64
_HwMacRadioSendFailFrames64Bits_Object = MibTableColumn
hwMacRadioSendFailFrames64Bits = _HwMacRadioSendFailFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 51),
    _HwMacRadioSendFailFrames64Bits_Type()
)
hwMacRadioSendFailFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendFailFrames64Bits.setStatus("current")
_HwMacRadioRcvErrFrames64Bits_Type = Counter64
_HwMacRadioRcvErrFrames64Bits_Object = MibTableColumn
hwMacRadioRcvErrFrames64Bits = _HwMacRadioRcvErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 52),
    _HwMacRadioRcvErrFrames64Bits_Type()
)
hwMacRadioRcvErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvErrFrames64Bits.setStatus("current")
_HwMacRadioRcvPhyErrFrames64Bits_Type = Counter64
_HwMacRadioRcvPhyErrFrames64Bits_Object = MibTableColumn
hwMacRadioRcvPhyErrFrames64Bits = _HwMacRadioRcvPhyErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 53),
    _HwMacRadioRcvPhyErrFrames64Bits_Type()
)
hwMacRadioRcvPhyErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvPhyErrFrames64Bits.setStatus("current")
_HwMacRadioRcvCrcErrFrames64Bits_Type = Counter64
_HwMacRadioRcvCrcErrFrames64Bits_Object = MibTableColumn
hwMacRadioRcvCrcErrFrames64Bits = _HwMacRadioRcvCrcErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 54),
    _HwMacRadioRcvCrcErrFrames64Bits_Type()
)
hwMacRadioRcvCrcErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvCrcErrFrames64Bits.setStatus("current")
_HwMacRadioRcvMicErrFrames64Bits_Type = Counter64
_HwMacRadioRcvMicErrFrames64Bits_Object = MibTableColumn
hwMacRadioRcvMicErrFrames64Bits = _HwMacRadioRcvMicErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 55),
    _HwMacRadioRcvMicErrFrames64Bits_Type()
)
hwMacRadioRcvMicErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvMicErrFrames64Bits.setStatus("current")
_HwMacRadioRcvKeyDecryptErrFrames64Bits_Type = Counter64
_HwMacRadioRcvKeyDecryptErrFrames64Bits_Object = MibTableColumn
hwMacRadioRcvKeyDecryptErrFrames64Bits = _HwMacRadioRcvKeyDecryptErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 56),
    _HwMacRadioRcvKeyDecryptErrFrames64Bits_Type()
)
hwMacRadioRcvKeyDecryptErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvKeyDecryptErrFrames64Bits.setStatus("current")
_HwMacRadioRetryFrames64Bits_Type = Counter64
_HwMacRadioRetryFrames64Bits_Object = MibTableColumn
hwMacRadioRetryFrames64Bits = _HwMacRadioRetryFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 57),
    _HwMacRadioRetryFrames64Bits_Type()
)
hwMacRadioRetryFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRetryFrames64Bits.setStatus("current")
_HwMacRadioDownMacErrFrames64Bits_Type = Counter64
_HwMacRadioDownMacErrFrames64Bits_Object = MibTableColumn
hwMacRadioDownMacErrFrames64Bits = _HwMacRadioDownMacErrFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 58),
    _HwMacRadioDownMacErrFrames64Bits_Type()
)
hwMacRadioDownMacErrFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDownMacErrFrames64Bits.setStatus("current")
_HwMacRadioNoise_Type = Integer32
_HwMacRadioNoise_Object = MibTableColumn
hwMacRadioNoise = _HwMacRadioNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 59),
    _HwMacRadioNoise_Type()
)
hwMacRadioNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioNoise.setStatus("current")
_HwMacRadioActualBandwidth_Type = Unsigned32
_HwMacRadioActualBandwidth_Object = MibTableColumn
hwMacRadioActualBandwidth = _HwMacRadioActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 60),
    _HwMacRadioActualBandwidth_Type()
)
hwMacRadioActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioActualBandwidth.setStatus("current")
_HwMacRadioFrames_Type = Counter64
_HwMacRadioFrames_Object = MibTableColumn
hwMacRadioFrames = _HwMacRadioFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 61),
    _HwMacRadioFrames_Type()
)
hwMacRadioFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioFrames.setStatus("current")
_HwMacRadioSendDropFrames64Bits_Type = Counter64
_HwMacRadioSendDropFrames64Bits_Object = MibTableColumn
hwMacRadioSendDropFrames64Bits = _HwMacRadioSendDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 62),
    _HwMacRadioSendDropFrames64Bits_Type()
)
hwMacRadioSendDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioSendDropFrames64Bits.setStatus("current")
_HwMacRadioRcvDropFrames64Bits_Type = Counter64
_HwMacRadioRcvDropFrames64Bits_Object = MibTableColumn
hwMacRadioRcvDropFrames64Bits = _HwMacRadioRcvDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 63),
    _HwMacRadioRcvDropFrames64Bits_Type()
)
hwMacRadioRcvDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRcvDropFrames64Bits.setStatus("current")
_HwMacRadioChannelFreeRate_Type = Unsigned32
_HwMacRadioChannelFreeRate_Object = MibTableColumn
hwMacRadioChannelFreeRate = _HwMacRadioChannelFreeRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 64),
    _HwMacRadioChannelFreeRate_Type()
)
hwMacRadioChannelFreeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioChannelFreeRate.setStatus("current")
_HwMacRadioTxRate_Type = Unsigned32
_HwMacRadioTxRate_Object = MibTableColumn
hwMacRadioTxRate = _HwMacRadioTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 65),
    _HwMacRadioTxRate_Type()
)
hwMacRadioTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioTxRate.setStatus("current")
_HwMacRadioRxRate_Type = Unsigned32
_HwMacRadioRxRate_Object = MibTableColumn
hwMacRadioRxRate = _HwMacRadioRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 66),
    _HwMacRadioRxRate_Type()
)
hwMacRadioRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioRxRate.setStatus("current")
_HwMacRadioChInterferenceRate_Type = Unsigned32
_HwMacRadioChInterferenceRate_Object = MibTableColumn
hwMacRadioChInterferenceRate = _HwMacRadioChInterferenceRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 30, 1, 67),
    _HwMacRadioChInterferenceRate_Type()
)
hwMacRadioChInterferenceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioChInterferenceRate.setStatus("current")
_HwMacRadioUnauthenticNeighborInfoTable_Object = MibTable
hwMacRadioUnauthenticNeighborInfoTable = _HwMacRadioUnauthenticNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31)
)
if mibBuilder.loadTexts:
    hwMacRadioUnauthenticNeighborInfoTable.setStatus("current")
_HwMacRadioUnauthenticNeighborInfoEntry_Object = MibTableRow
hwMacRadioUnauthenticNeighborInfoEntry = _HwMacRadioUnauthenticNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31, 1)
)
hwMacRadioUnauthenticNeighborInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioUnauthenticNeighborInfoEntry.setStatus("current")
_HwMacUnauthenticRadioNeighborBSSID_Type = OctetString
_HwMacUnauthenticRadioNeighborBSSID_Object = MibTableColumn
hwMacUnauthenticRadioNeighborBSSID = _HwMacUnauthenticRadioNeighborBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31, 1, 1),
    _HwMacUnauthenticRadioNeighborBSSID_Type()
)
hwMacUnauthenticRadioNeighborBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacUnauthenticRadioNeighborBSSID.setStatus("current")
_HwMacUnauthenticRadioNeighborRSSI_Type = OctetString
_HwMacUnauthenticRadioNeighborRSSI_Object = MibTableColumn
hwMacUnauthenticRadioNeighborRSSI = _HwMacUnauthenticRadioNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31, 1, 2),
    _HwMacUnauthenticRadioNeighborRSSI_Type()
)
hwMacUnauthenticRadioNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacUnauthenticRadioNeighborRSSI.setStatus("current")
_HwMacunauthenticRadioNeighborChannel_Type = OctetString
_HwMacunauthenticRadioNeighborChannel_Object = MibTableColumn
hwMacunauthenticRadioNeighborChannel = _HwMacunauthenticRadioNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31, 1, 3),
    _HwMacunauthenticRadioNeighborChannel_Type()
)
hwMacunauthenticRadioNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacunauthenticRadioNeighborChannel.setStatus("current")
_HwMacUnauthenticRadioNeighborSSID_Type = OctetString
_HwMacUnauthenticRadioNeighborSSID_Object = MibTableColumn
hwMacUnauthenticRadioNeighborSSID = _HwMacUnauthenticRadioNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 31, 1, 4),
    _HwMacUnauthenticRadioNeighborSSID_Type()
)
hwMacUnauthenticRadioNeighborSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacUnauthenticRadioNeighborSSID.setStatus("current")
_HwRadioInfoTable_Object = MibTable
hwRadioInfoTable = _HwRadioInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32)
)
if mibBuilder.loadTexts:
    hwRadioInfoTable.setStatus("current")
_HwRadioInfoEntry_Object = MibTableRow
hwRadioInfoEntry = _HwRadioInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1)
)
hwRadioInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioInfoEntry.setStatus("current")
_HwRadioDecsption_Type = OctetString
_HwRadioDecsption_Object = MibTableColumn
hwRadioDecsption = _HwRadioDecsption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 1),
    _HwRadioDecsption_Type()
)
hwRadioDecsption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioDecsption.setStatus("current")
_HwRadioPortType_Type = OctetString
_HwRadioPortType_Object = MibTableColumn
hwRadioPortType = _HwRadioPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 2),
    _HwRadioPortType_Type()
)
hwRadioPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioPortType.setStatus("current")
_HwRadioMaxMtu_Type = Integer32
_HwRadioMaxMtu_Object = MibTableColumn
hwRadioMaxMtu = _HwRadioMaxMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 3),
    _HwRadioMaxMtu_Type()
)
hwRadioMaxMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioMaxMtu.setStatus("current")
if mibBuilder.loadTexts:
    hwRadioMaxMtu.setUnits("byte")
_HwRadioBandwidth_Type = Integer32
_HwRadioBandwidth_Object = MibTableColumn
hwRadioBandwidth = _HwRadioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 4),
    _HwRadioBandwidth_Type()
)
hwRadioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwRadioBandwidth.setUnits("Mbps")
_HwRadioMac_Type = MacAddress
_HwRadioMac_Object = MibTableColumn
hwRadioMac = _HwRadioMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 5),
    _HwRadioMac_Type()
)
hwRadioMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioMac.setStatus("current")


class _HwRadioAdminStatus_Type(Integer32):
    """Custom type hwRadioAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 2),
          ("up", 1))
    )


_HwRadioAdminStatus_Type.__name__ = "Integer32"
_HwRadioAdminStatus_Object = MibTableColumn
hwRadioAdminStatus = _HwRadioAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 6),
    _HwRadioAdminStatus_Type()
)
hwRadioAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAdminStatus.setStatus("current")


class _HwRadioOperStatus_Type(Integer32):
    """Custom type hwRadioOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 3),
          ("down", 2),
          ("up", 1))
    )


_HwRadioOperStatus_Type.__name__ = "Integer32"
_HwRadioOperStatus_Object = MibTableColumn
hwRadioOperStatus = _HwRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 7),
    _HwRadioOperStatus_Type()
)
hwRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioOperStatus.setStatus("current")
_HwRadioLastChange_Type = Integer32
_HwRadioLastChange_Object = MibTableColumn
hwRadioLastChange = _HwRadioLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 8),
    _HwRadioLastChange_Type()
)
hwRadioLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioLastChange.setStatus("current")
_HwRadioInfoUpDownTimes_Type = Integer32
_HwRadioInfoUpDownTimes_Object = MibTableColumn
hwRadioInfoUpDownTimes = _HwRadioInfoUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 9),
    _HwRadioInfoUpDownTimes_Type()
)
hwRadioInfoUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioInfoUpDownTimes.setStatus("current")


class _HwRadioAutoOffSwitch_Type(Integer32):
    """Custom type hwRadioAutoOffSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwRadioAutoOffSwitch_Type.__name__ = "Integer32"
_HwRadioAutoOffSwitch_Object = MibTableColumn
hwRadioAutoOffSwitch = _HwRadioAutoOffSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 10),
    _HwRadioAutoOffSwitch_Type()
)
hwRadioAutoOffSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAutoOffSwitch.setStatus("current")


class _HwRadioAutoOffStartTime_Type(OctetString):
    """Custom type hwRadioAutoOffStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwRadioAutoOffStartTime_Type.__name__ = "OctetString"
_HwRadioAutoOffStartTime_Object = MibTableColumn
hwRadioAutoOffStartTime = _HwRadioAutoOffStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 11),
    _HwRadioAutoOffStartTime_Type()
)
hwRadioAutoOffStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAutoOffStartTime.setStatus("current")


class _HwRadioAutoOffEndTime_Type(OctetString):
    """Custom type hwRadioAutoOffEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwRadioAutoOffEndTime_Type.__name__ = "OctetString"
_HwRadioAutoOffEndTime_Object = MibTableColumn
hwRadioAutoOffEndTime = _HwRadioAutoOffEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 32, 1, 12),
    _HwRadioAutoOffEndTime_Type()
)
hwRadioAutoOffEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioAutoOffEndTime.setStatus("current")
_HwMacRadioInfoTable_Object = MibTable
hwMacRadioInfoTable = _HwMacRadioInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33)
)
if mibBuilder.loadTexts:
    hwMacRadioInfoTable.setStatus("current")
_HwMacRadioInfoEntry_Object = MibTableRow
hwMacRadioInfoEntry = _HwMacRadioInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1)
)
hwMacRadioInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
)
if mibBuilder.loadTexts:
    hwMacRadioInfoEntry.setStatus("current")
_HwMacRadioDecsption_Type = OctetString
_HwMacRadioDecsption_Object = MibTableColumn
hwMacRadioDecsption = _HwMacRadioDecsption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 1),
    _HwMacRadioDecsption_Type()
)
hwMacRadioDecsption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioDecsption.setStatus("current")
_HwMacRadioPortType_Type = OctetString
_HwMacRadioPortType_Object = MibTableColumn
hwMacRadioPortType = _HwMacRadioPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 2),
    _HwMacRadioPortType_Type()
)
hwMacRadioPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioPortType.setStatus("current")
_HwMacRadioMaxMtu_Type = Integer32
_HwMacRadioMaxMtu_Object = MibTableColumn
hwMacRadioMaxMtu = _HwMacRadioMaxMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 3),
    _HwMacRadioMaxMtu_Type()
)
hwMacRadioMaxMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioMaxMtu.setStatus("current")
_HwMacRadioBandwidth_Type = Integer32
_HwMacRadioBandwidth_Object = MibTableColumn
hwMacRadioBandwidth = _HwMacRadioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 4),
    _HwMacRadioBandwidth_Type()
)
hwMacRadioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioBandwidth.setStatus("current")
_HwMacRadioMac_Type = MacAddress
_HwMacRadioMac_Object = MibTableColumn
hwMacRadioMac = _HwMacRadioMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 5),
    _HwMacRadioMac_Type()
)
hwMacRadioMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioMac.setStatus("current")


class _HwMacRadioAdminStatus_Type(Integer32):
    """Custom type hwMacRadioAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 2),
          ("up", 1))
    )


_HwMacRadioAdminStatus_Type.__name__ = "Integer32"
_HwMacRadioAdminStatus_Object = MibTableColumn
hwMacRadioAdminStatus = _HwMacRadioAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 6),
    _HwMacRadioAdminStatus_Type()
)
hwMacRadioAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAdminStatus.setStatus("current")


class _HwMacRadioOperStatus_Type(Integer32):
    """Custom type hwMacRadioOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 3),
          ("down", 2),
          ("up", 1))
    )


_HwMacRadioOperStatus_Type.__name__ = "Integer32"
_HwMacRadioOperStatus_Object = MibTableColumn
hwMacRadioOperStatus = _HwMacRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 7),
    _HwMacRadioOperStatus_Type()
)
hwMacRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioOperStatus.setStatus("current")
_HwMacRadioLastChange_Type = Integer32
_HwMacRadioLastChange_Object = MibTableColumn
hwMacRadioLastChange = _HwMacRadioLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 8),
    _HwMacRadioLastChange_Type()
)
hwMacRadioLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioLastChange.setStatus("current")
_HwMacRadioInfoUpDownTimes_Type = Integer32
_HwMacRadioInfoUpDownTimes_Object = MibTableColumn
hwMacRadioInfoUpDownTimes = _HwMacRadioInfoUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 9),
    _HwMacRadioInfoUpDownTimes_Type()
)
hwMacRadioInfoUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioInfoUpDownTimes.setStatus("current")


class _HwMacRadioAutoOffSwitch_Type(Integer32):
    """Custom type hwMacRadioAutoOffSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMacRadioAutoOffSwitch_Type.__name__ = "Integer32"
_HwMacRadioAutoOffSwitch_Object = MibTableColumn
hwMacRadioAutoOffSwitch = _HwMacRadioAutoOffSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 10),
    _HwMacRadioAutoOffSwitch_Type()
)
hwMacRadioAutoOffSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAutoOffSwitch.setStatus("current")


class _HwMacRadioAutoOffStartTime_Type(OctetString):
    """Custom type hwMacRadioAutoOffStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwMacRadioAutoOffStartTime_Type.__name__ = "OctetString"
_HwMacRadioAutoOffStartTime_Object = MibTableColumn
hwMacRadioAutoOffStartTime = _HwMacRadioAutoOffStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 11),
    _HwMacRadioAutoOffStartTime_Type()
)
hwMacRadioAutoOffStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAutoOffStartTime.setStatus("current")


class _HwMacRadioAutoOffEndTime_Type(OctetString):
    """Custom type hwMacRadioAutoOffEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwMacRadioAutoOffEndTime_Type.__name__ = "OctetString"
_HwMacRadioAutoOffEndTime_Object = MibTableColumn
hwMacRadioAutoOffEndTime = _HwMacRadioAutoOffEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 33, 1, 12),
    _HwMacRadioAutoOffEndTime_Type()
)
hwMacRadioAutoOffEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRadioAutoOffEndTime.setStatus("current")
_HwRadioObjects_ObjectIdentity = ObjectIdentity
hwRadioObjects = _HwRadioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34)
)
_HwRadioCalibrateTable_ObjectIdentity = ObjectIdentity
hwRadioCalibrateTable = _HwRadioCalibrateTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1)
)
_HwRadioCalibrateMode_Type = Integer32
_HwRadioCalibrateMode_Object = MibScalar
hwRadioCalibrateMode = _HwRadioCalibrateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 1),
    _HwRadioCalibrateMode_Type()
)
hwRadioCalibrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateMode.setStatus("current")
_HwRadioCalibrateTime_Type = OctetString
_HwRadioCalibrateTime_Object = MibScalar
hwRadioCalibrateTime = _HwRadioCalibrateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 2),
    _HwRadioCalibrateTime_Type()
)
hwRadioCalibrateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateTime.setStatus("current")
_HwRadioCalibrateManualStartup_Type = Integer32
_HwRadioCalibrateManualStartup_Object = MibScalar
hwRadioCalibrateManualStartup = _HwRadioCalibrateManualStartup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 3),
    _HwRadioCalibrateManualStartup_Type()
)
hwRadioCalibrateManualStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateManualStartup.setStatus("current")
_HwRadioCalibrateCycle_Type = Integer32
_HwRadioCalibrateCycle_Object = MibScalar
hwRadioCalibrateCycle = _HwRadioCalibrateCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 4),
    _HwRadioCalibrateCycle_Type()
)
hwRadioCalibrateCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateCycle.setStatus("current")
_HwRadioCalibratePolicy_Type = Unsigned32
_HwRadioCalibratePolicy_Object = MibScalar
hwRadioCalibratePolicy = _HwRadioCalibratePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 5),
    _HwRadioCalibratePolicy_Type()
)
hwRadioCalibratePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibratePolicy.setStatus("current")
_HwRadioCalibratesensitivity_Type = Unsigned32
_HwRadioCalibratesensitivity_Object = MibScalar
hwRadioCalibratesensitivity = _HwRadioCalibratesensitivity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 6),
    _HwRadioCalibratesensitivity_Type()
)
hwRadioCalibratesensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibratesensitivity.setStatus("current")
_HwRadioGlobalCalibrateChannel2G_Type = OctetString
_HwRadioGlobalCalibrateChannel2G_Object = MibScalar
hwRadioGlobalCalibrateChannel2G = _HwRadioGlobalCalibrateChannel2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 7),
    _HwRadioGlobalCalibrateChannel2G_Type()
)
hwRadioGlobalCalibrateChannel2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioGlobalCalibrateChannel2G.setStatus("current")
_HwRadioGlobalCalibrateChannel5G_Type = OctetString
_HwRadioGlobalCalibrateChannel5G_Object = MibScalar
hwRadioGlobalCalibrateChannel5G = _HwRadioGlobalCalibrateChannel5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 8),
    _HwRadioGlobalCalibrateChannel5G_Type()
)
hwRadioGlobalCalibrateChannel5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioGlobalCalibrateChannel5G.setStatus("current")
_HwRadioGlobalScanChannel2G_Type = OctetString
_HwRadioGlobalScanChannel2G_Object = MibScalar
hwRadioGlobalScanChannel2G = _HwRadioGlobalScanChannel2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 9),
    _HwRadioGlobalScanChannel2G_Type()
)
hwRadioGlobalScanChannel2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioGlobalScanChannel2G.setStatus("current")
_HwRadioGlobalScanChannel5G_Type = OctetString
_HwRadioGlobalScanChannel5G_Object = MibScalar
hwRadioGlobalScanChannel5G = _HwRadioGlobalScanChannel5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 10),
    _HwRadioGlobalScanChannel5G_Type()
)
hwRadioGlobalScanChannel5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioGlobalScanChannel5G.setStatus("current")


class _HwRadioGlobalCalibrate5gBandWidth_Type(Integer32):
    """Custom type hwRadioGlobalCalibrate5gBandWidth based on Integer32"""
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
        *(("ht20", 1),
          ("ht40", 2),
          ("ht80", 3))
    )


_HwRadioGlobalCalibrate5gBandWidth_Type.__name__ = "Integer32"
_HwRadioGlobalCalibrate5gBandWidth_Object = MibScalar
hwRadioGlobalCalibrate5gBandWidth = _HwRadioGlobalCalibrate5gBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 11),
    _HwRadioGlobalCalibrate5gBandWidth_Type()
)
hwRadioGlobalCalibrate5gBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioGlobalCalibrate5gBandWidth.setStatus("current")
_HwRadioCalibrateAutoStartTime_Type = OctetString
_HwRadioCalibrateAutoStartTime_Object = MibScalar
hwRadioCalibrateAutoStartTime = _HwRadioCalibrateAutoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 1, 12),
    _HwRadioCalibrateAutoStartTime_Type()
)
hwRadioCalibrateAutoStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioCalibrateAutoStartTime.setStatus("current")
_HwConnectProfileTable_Object = MibTable
hwConnectProfileTable = _HwConnectProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2)
)
if mibBuilder.loadTexts:
    hwConnectProfileTable.setStatus("current")
_HwConnectProfileEntry_Object = MibTableRow
hwConnectProfileEntry = _HwConnectProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1)
)
hwConnectProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectProfileName"),
)
if mibBuilder.loadTexts:
    hwConnectProfileEntry.setStatus("current")


class _HwConnectProfileName_Type(OctetString):
    """Custom type hwConnectProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwConnectProfileName_Type.__name__ = "OctetString"
_HwConnectProfileName_Object = MibTableColumn
hwConnectProfileName = _HwConnectProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 1),
    _HwConnectProfileName_Type()
)
hwConnectProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectProfileName.setStatus("current")


class _HwConnectSsid_Type(OctetString):
    """Custom type hwConnectSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwConnectSsid_Type.__name__ = "OctetString"
_HwConnectSsid_Object = MibTableColumn
hwConnectSsid = _HwConnectSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 2),
    _HwConnectSsid_Type()
)
hwConnectSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectSsid.setStatus("current")
_HwConnectPeerMac_Type = MacAddress
_HwConnectPeerMac_Object = MibTableColumn
hwConnectPeerMac = _HwConnectPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 3),
    _HwConnectPeerMac_Type()
)
hwConnectPeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectPeerMac.setStatus("current")
_HwConnectPskPassPhase_Type = OctetString
_HwConnectPskPassPhase_Object = MibTableColumn
hwConnectPskPassPhase = _HwConnectPskPassPhase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 4),
    _HwConnectPskPassPhase_Type()
)
hwConnectPskPassPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectPskPassPhase.setStatus("current")


class _HwConnectProfileActived_Type(Integer32):
    """Custom type hwConnectProfileActived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwConnectProfileActived_Type.__name__ = "Integer32"
_HwConnectProfileActived_Object = MibTableColumn
hwConnectProfileActived = _HwConnectProfileActived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 5),
    _HwConnectProfileActived_Type()
)
hwConnectProfileActived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectProfileActived.setStatus("current")
_HwConnectProfileRowStatus_Type = RowStatus
_HwConnectProfileRowStatus_Object = MibTableColumn
hwConnectProfileRowStatus = _HwConnectProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 2, 1, 6),
    _HwConnectProfileRowStatus_Type()
)
hwConnectProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectProfileRowStatus.setStatus("current")
_HwRadioBasicSettingTable_Object = MibTable
hwRadioBasicSettingTable = _HwRadioBasicSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 3)
)
if mibBuilder.loadTexts:
    hwRadioBasicSettingTable.setStatus("current")
_HwRadioBasicSettingEntry_Object = MibTableRow
hwRadioBasicSettingEntry = _HwRadioBasicSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 3, 1)
)
hwRadioBasicSettingEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwApRadioID"),
)
if mibBuilder.loadTexts:
    hwRadioBasicSettingEntry.setStatus("current")
_HwApRadioID_Type = Integer32
_HwApRadioID_Object = MibTableColumn
hwApRadioID = _HwApRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 3, 1, 1),
    _HwApRadioID_Type()
)
hwApRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApRadioID.setStatus("current")


class _HwApRadioTxPower_Type(Integer32):
    """Custom type hwApRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 36),
    )


_HwApRadioTxPower_Type.__name__ = "Integer32"
_HwApRadioTxPower_Object = MibTableColumn
hwApRadioTxPower = _HwApRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 3, 1, 2),
    _HwApRadioTxPower_Type()
)
hwApRadioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRadioTxPower.setStatus("current")


class _HwApRadioRtsThreshold_Type(Integer32):
    """Custom type hwApRadioRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2347),
    )


_HwApRadioRtsThreshold_Type.__name__ = "Integer32"
_HwApRadioRtsThreshold_Object = MibTableColumn
hwApRadioRtsThreshold = _HwApRadioRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 3, 1, 3),
    _HwApRadioRtsThreshold_Type()
)
hwApRadioRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRadioRtsThreshold.setStatus("current")
_HwConnectStatusTable_Object = MibTable
hwConnectStatusTable = _HwConnectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4)
)
if mibBuilder.loadTexts:
    hwConnectStatusTable.setStatus("current")
_HwConnectStatusEntry_Object = MibTableRow
hwConnectStatusEntry = _HwConnectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1)
)
hwConnectStatusEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusPeerMac"),
)
if mibBuilder.loadTexts:
    hwConnectStatusEntry.setStatus("current")
_HwConnectStatusPeerMac_Type = MacAddress
_HwConnectStatusPeerMac_Object = MibTableColumn
hwConnectStatusPeerMac = _HwConnectStatusPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 1),
    _HwConnectStatusPeerMac_Type()
)
hwConnectStatusPeerMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectStatusPeerMac.setStatus("current")


class _HwConnectStatusSsid_Type(OctetString):
    """Custom type hwConnectStatusSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwConnectStatusSsid_Type.__name__ = "OctetString"
_HwConnectStatusSsid_Object = MibTableColumn
hwConnectStatusSsid = _HwConnectStatusSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 2),
    _HwConnectStatusSsid_Type()
)
hwConnectStatusSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusSsid.setStatus("current")


class _HwConnectStatus_Type(Integer32):
    """Custom type hwConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 2),
          ("disconnect", 1))
    )


_HwConnectStatus_Type.__name__ = "Integer32"
_HwConnectStatus_Object = MibTableColumn
hwConnectStatus = _HwConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 3),
    _HwConnectStatus_Type()
)
hwConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatus.setStatus("current")
_HwConnectStatusSNR_Type = Integer32
_HwConnectStatusSNR_Object = MibTableColumn
hwConnectStatusSNR = _HwConnectStatusSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 4),
    _HwConnectStatusSNR_Type()
)
hwConnectStatusSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusSNR.setStatus("current")
_HwConnectStatusNoiseFloor_Type = Integer32
_HwConnectStatusNoiseFloor_Object = MibTableColumn
hwConnectStatusNoiseFloor = _HwConnectStatusNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 5),
    _HwConnectStatusNoiseFloor_Type()
)
hwConnectStatusNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusNoiseFloor.setStatus("current")
_HwConnectStatusChannel_Type = Integer32
_HwConnectStatusChannel_Object = MibTableColumn
hwConnectStatusChannel = _HwConnectStatusChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 6),
    _HwConnectStatusChannel_Type()
)
hwConnectStatusChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusChannel.setStatus("current")
_HwConnectStatusActualTxPower_Type = Integer32
_HwConnectStatusActualTxPower_Object = MibTableColumn
hwConnectStatusActualTxPower = _HwConnectStatusActualTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 7),
    _HwConnectStatusActualTxPower_Type()
)
hwConnectStatusActualTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusActualTxPower.setStatus("current")
_HwConnectStatusBeaconInterval_Type = Integer32
_HwConnectStatusBeaconInterval_Object = MibTableColumn
hwConnectStatusBeaconInterval = _HwConnectStatusBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 8),
    _HwConnectStatusBeaconInterval_Type()
)
hwConnectStatusBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusBeaconInterval.setStatus("current")
_HwConnectStatusCurrentRate_Type = Integer32
_HwConnectStatusCurrentRate_Object = MibTableColumn
hwConnectStatusCurrentRate = _HwConnectStatusCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 9),
    _HwConnectStatusCurrentRate_Type()
)
hwConnectStatusCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusCurrentRate.setStatus("current")
_HwConnectStatusTxBeamforming_Type = Integer32
_HwConnectStatusTxBeamforming_Object = MibTableColumn
hwConnectStatusTxBeamforming = _HwConnectStatusTxBeamforming_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 10),
    _HwConnectStatusTxBeamforming_Type()
)
hwConnectStatusTxBeamforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusTxBeamforming.setStatus("current")
_HwConnectStatusActualCountryCode_Type = Integer32
_HwConnectStatusActualCountryCode_Object = MibTableColumn
hwConnectStatusActualCountryCode = _HwConnectStatusActualCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 11),
    _HwConnectStatusActualCountryCode_Type()
)
hwConnectStatusActualCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusActualCountryCode.setStatus("current")
_HwConnectStatusDistance_Type = Integer32
_HwConnectStatusDistance_Object = MibTableColumn
hwConnectStatusDistance = _HwConnectStatusDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 12),
    _HwConnectStatusDistance_Type()
)
hwConnectStatusDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusDistance.setStatus("current")
_HwConnectStatusCurrentRateKbps_Type = Integer32
_HwConnectStatusCurrentRateKbps_Object = MibTableColumn
hwConnectStatusCurrentRateKbps = _HwConnectStatusCurrentRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 13),
    _HwConnectStatusCurrentRateKbps_Type()
)
hwConnectStatusCurrentRateKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusCurrentRateKbps.setStatus("current")


class _HwConnectStatusHtMode_Type(Integer32):
    """Custom type hwConnectStatusHtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40", 2))
    )


_HwConnectStatusHtMode_Type.__name__ = "Integer32"
_HwConnectStatusHtMode_Object = MibTableColumn
hwConnectStatusHtMode = _HwConnectStatusHtMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 14),
    _HwConnectStatusHtMode_Type()
)
hwConnectStatusHtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusHtMode.setStatus("current")


class _HwConnectStatusGIMode_Type(Integer32):
    """Custom type hwConnectStatusGIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("short", 2))
    )


_HwConnectStatusGIMode_Type.__name__ = "Integer32"
_HwConnectStatusGIMode_Object = MibTableColumn
hwConnectStatusGIMode = _HwConnectStatusGIMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 4, 1, 15),
    _HwConnectStatusGIMode_Type()
)
hwConnectStatusGIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectStatusGIMode.setStatus("current")
_HwConnectStatisticsTable_Object = MibTable
hwConnectStatisticsTable = _HwConnectStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5)
)
if mibBuilder.loadTexts:
    hwConnectStatisticsTable.setStatus("current")
_HwConnectStatisticsEntry_Object = MibTableRow
hwConnectStatisticsEntry = _HwConnectStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1)
)
hwConnectStatisticsEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectStatisticsPeerMac"),
)
if mibBuilder.loadTexts:
    hwConnectStatisticsEntry.setStatus("current")
_HwConnectStatisticsPeerMac_Type = MacAddress
_HwConnectStatisticsPeerMac_Object = MibTableColumn
hwConnectStatisticsPeerMac = _HwConnectStatisticsPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 1),
    _HwConnectStatisticsPeerMac_Type()
)
hwConnectStatisticsPeerMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectStatisticsPeerMac.setStatus("current")
_HwConnectRxOkUcastDataFrames_Type = Counter64
_HwConnectRxOkUcastDataFrames_Object = MibTableColumn
hwConnectRxOkUcastDataFrames = _HwConnectRxOkUcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 2),
    _HwConnectRxOkUcastDataFrames_Type()
)
hwConnectRxOkUcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectRxOkUcastDataFrames.setStatus("current")
_HwConnectRxOkUcastDataBytes_Type = Counter64
_HwConnectRxOkUcastDataBytes_Object = MibTableColumn
hwConnectRxOkUcastDataBytes = _HwConnectRxOkUcastDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 3),
    _HwConnectRxOkUcastDataBytes_Type()
)
hwConnectRxOkUcastDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectRxOkUcastDataBytes.setStatus("current")
_HwConnectTxOkUcastDataFrames_Type = Counter64
_HwConnectTxOkUcastDataFrames_Object = MibTableColumn
hwConnectTxOkUcastDataFrames = _HwConnectTxOkUcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 4),
    _HwConnectTxOkUcastDataFrames_Type()
)
hwConnectTxOkUcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectTxOkUcastDataFrames.setStatus("current")
_HwConnectTxOkUcastDataBytes_Type = Counter64
_HwConnectTxOkUcastDataBytes_Object = MibTableColumn
hwConnectTxOkUcastDataBytes = _HwConnectTxOkUcastDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 5),
    _HwConnectTxOkUcastDataBytes_Type()
)
hwConnectTxOkUcastDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectTxOkUcastDataBytes.setStatus("current")
_HwConnectRxThroughput_Type = Unsigned32
_HwConnectRxThroughput_Object = MibTableColumn
hwConnectRxThroughput = _HwConnectRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 6),
    _HwConnectRxThroughput_Type()
)
hwConnectRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectRxThroughput.setStatus("current")
_HwConnectTxThroughput_Type = Unsigned32
_HwConnectTxThroughput_Object = MibTableColumn
hwConnectTxThroughput = _HwConnectTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 7),
    _HwConnectTxThroughput_Type()
)
hwConnectTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectTxThroughput.setStatus("current")
_HwConnectRxErrFrames_Type = Counter64
_HwConnectRxErrFrames_Object = MibTableColumn
hwConnectRxErrFrames = _HwConnectRxErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 8),
    _HwConnectRxErrFrames_Type()
)
hwConnectRxErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectRxErrFrames.setStatus("current")
_HwConnectTxErrUcastDataFrames_Type = Counter64
_HwConnectTxErrUcastDataFrames_Object = MibTableColumn
hwConnectTxErrUcastDataFrames = _HwConnectTxErrUcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 9),
    _HwConnectTxErrUcastDataFrames_Type()
)
hwConnectTxErrUcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectTxErrUcastDataFrames.setStatus("current")
_HwConnectUcastDataFrameTxRetryRatio_Type = Unsigned32
_HwConnectUcastDataFrameTxRetryRatio_Object = MibTableColumn
hwConnectUcastDataFrameTxRetryRatio = _HwConnectUcastDataFrameTxRetryRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 10),
    _HwConnectUcastDataFrameTxRetryRatio_Type()
)
hwConnectUcastDataFrameTxRetryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectUcastDataFrameTxRetryRatio.setStatus("current")
_HwConnectOnlineTime_Type = Unsigned32
_HwConnectOnlineTime_Object = MibTableColumn
hwConnectOnlineTime = _HwConnectOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 11),
    _HwConnectOnlineTime_Type()
)
hwConnectOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectOnlineTime.setStatus("current")


class _HwConnectStatisticsReset_Type(Integer32):
    """Custom type hwConnectStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_HwConnectStatisticsReset_Type.__name__ = "Integer32"
_HwConnectStatisticsReset_Object = MibTableColumn
hwConnectStatisticsReset = _HwConnectStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 5, 1, 12),
    _HwConnectStatisticsReset_Type()
)
hwConnectStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectStatisticsReset.setStatus("current")
_HwConnectRateHistogramTable_Object = MibTable
hwConnectRateHistogramTable = _HwConnectRateHistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 6)
)
if mibBuilder.loadTexts:
    hwConnectRateHistogramTable.setStatus("current")
_HwConnectRateHistogramEntry_Object = MibTableRow
hwConnectRateHistogramEntry = _HwConnectRateHistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 6, 1)
)
hwConnectRateHistogramEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectRateStatDirection"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectRateStatRange"),
)
if mibBuilder.loadTexts:
    hwConnectRateHistogramEntry.setStatus("current")


class _HwConnectRateStatDirection_Type(Integer32):
    """Custom type hwConnectRateStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxRate", 2),
          ("txRate", 1))
    )


_HwConnectRateStatDirection_Type.__name__ = "Integer32"
_HwConnectRateStatDirection_Object = MibTableColumn
hwConnectRateStatDirection = _HwConnectRateStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 6, 1, 1),
    _HwConnectRateStatDirection_Type()
)
hwConnectRateStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectRateStatDirection.setStatus("current")
_HwConnectRateStatRange_Type = Integer32
_HwConnectRateStatRange_Object = MibTableColumn
hwConnectRateStatRange = _HwConnectRateStatRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 6, 1, 2),
    _HwConnectRateStatRange_Type()
)
hwConnectRateStatRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectRateStatRange.setStatus("current")
_HwConnectRateStatUcastDataFrames_Type = Counter64
_HwConnectRateStatUcastDataFrames_Object = MibTableColumn
hwConnectRateStatUcastDataFrames = _HwConnectRateStatUcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 6, 1, 3),
    _HwConnectRateStatUcastDataFrames_Type()
)
hwConnectRateStatUcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectRateStatUcastDataFrames.setStatus("current")
_HwConnectAMPDUHistogramTable_Object = MibTable
hwConnectAMPDUHistogramTable = _HwConnectAMPDUHistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 7)
)
if mibBuilder.loadTexts:
    hwConnectAMPDUHistogramTable.setStatus("current")
_HwConnectAMPDUHistogramEntry_Object = MibTableRow
hwConnectAMPDUHistogramEntry = _HwConnectAMPDUHistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 7, 1)
)
hwConnectAMPDUHistogramEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectAMPDUStatDirection"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectAMPDUStatRange"),
)
if mibBuilder.loadTexts:
    hwConnectAMPDUHistogramEntry.setStatus("current")


class _HwConnectAMPDUStatDirection_Type(Integer32):
    """Custom type hwConnectAMPDUStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxAMPDU", 2),
          ("txAMPDU", 1))
    )


_HwConnectAMPDUStatDirection_Type.__name__ = "Integer32"
_HwConnectAMPDUStatDirection_Object = MibTableColumn
hwConnectAMPDUStatDirection = _HwConnectAMPDUStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 7, 1, 1),
    _HwConnectAMPDUStatDirection_Type()
)
hwConnectAMPDUStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectAMPDUStatDirection.setStatus("current")
_HwConnectAMPDUStatRange_Type = Integer32
_HwConnectAMPDUStatRange_Object = MibTableColumn
hwConnectAMPDUStatRange = _HwConnectAMPDUStatRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 7, 1, 2),
    _HwConnectAMPDUStatRange_Type()
)
hwConnectAMPDUStatRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectAMPDUStatRange.setStatus("current")
_HwConnectAMPDUStatUcastDataFrames_Type = Counter64
_HwConnectAMPDUStatUcastDataFrames_Object = MibTableColumn
hwConnectAMPDUStatUcastDataFrames = _HwConnectAMPDUStatUcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 7, 1, 3),
    _HwConnectAMPDUStatUcastDataFrames_Type()
)
hwConnectAMPDUStatUcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectAMPDUStatUcastDataFrames.setStatus("current")
_HwConnectLenHistogramTable_Object = MibTable
hwConnectLenHistogramTable = _HwConnectLenHistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 8)
)
if mibBuilder.loadTexts:
    hwConnectLenHistogramTable.setStatus("current")
_HwConnectLenHistogramEntry_Object = MibTableRow
hwConnectLenHistogramEntry = _HwConnectLenHistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 8, 1)
)
hwConnectLenHistogramEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectDataLenStatDirection"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectDataLenStatLength"),
)
if mibBuilder.loadTexts:
    hwConnectLenHistogramEntry.setStatus("current")


class _HwConnectDataLenStatDirection_Type(Integer32):
    """Custom type hwConnectDataLenStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxLen", 2),
          ("txLen", 1))
    )


_HwConnectDataLenStatDirection_Type.__name__ = "Integer32"
_HwConnectDataLenStatDirection_Object = MibTableColumn
hwConnectDataLenStatDirection = _HwConnectDataLenStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 8, 1, 1),
    _HwConnectDataLenStatDirection_Type()
)
hwConnectDataLenStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectDataLenStatDirection.setStatus("current")
_HwConnectDataLenStatLength_Type = Integer32
_HwConnectDataLenStatLength_Object = MibTableColumn
hwConnectDataLenStatLength = _HwConnectDataLenStatLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 8, 1, 2),
    _HwConnectDataLenStatLength_Type()
)
hwConnectDataLenStatLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectDataLenStatLength.setStatus("current")
_HwConnectDataLenStatFrameCounts_Type = Counter64
_HwConnectDataLenStatFrameCounts_Object = MibTableColumn
hwConnectDataLenStatFrameCounts = _HwConnectDataLenStatFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 8, 1, 3),
    _HwConnectDataLenStatFrameCounts_Type()
)
hwConnectDataLenStatFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectDataLenStatFrameCounts.setStatus("current")
_HwConnectMaxSnrTable_Object = MibTable
hwConnectMaxSnrTable = _HwConnectMaxSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9)
)
if mibBuilder.loadTexts:
    hwConnectMaxSnrTable.setStatus("current")
_HwConnectMaxSnrEntry_Object = MibTableRow
hwConnectMaxSnrEntry = _HwConnectMaxSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1)
)
hwConnectMaxSnrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrPeerMAC"),
)
if mibBuilder.loadTexts:
    hwConnectMaxSnrEntry.setStatus("current")
_HwConnectMaxSnrPeerMAC_Type = MacAddress
_HwConnectMaxSnrPeerMAC_Object = MibTableColumn
hwConnectMaxSnrPeerMAC = _HwConnectMaxSnrPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1, 1),
    _HwConnectMaxSnrPeerMAC_Type()
)
hwConnectMaxSnrPeerMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConnectMaxSnrPeerMAC.setStatus("current")
_HwConnectMaxSnrValue_Type = Integer32
_HwConnectMaxSnrValue_Object = MibTableColumn
hwConnectMaxSnrValue = _HwConnectMaxSnrValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1, 2),
    _HwConnectMaxSnrValue_Type()
)
hwConnectMaxSnrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectMaxSnrValue.setStatus("current")
_HwConnectMaxSnrNoiseFloor_Type = Integer32
_HwConnectMaxSnrNoiseFloor_Object = MibTableColumn
hwConnectMaxSnrNoiseFloor = _HwConnectMaxSnrNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1, 3),
    _HwConnectMaxSnrNoiseFloor_Type()
)
hwConnectMaxSnrNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectMaxSnrNoiseFloor.setStatus("current")
_HwConnectMaxSnrSSID_Type = OctetString
_HwConnectMaxSnrSSID_Object = MibTableColumn
hwConnectMaxSnrSSID = _HwConnectMaxSnrSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1, 4),
    _HwConnectMaxSnrSSID_Type()
)
hwConnectMaxSnrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectMaxSnrSSID.setStatus("current")
_HwConnectMaxSnrTime_Type = DateAndTime
_HwConnectMaxSnrTime_Object = MibTableColumn
hwConnectMaxSnrTime = _HwConnectMaxSnrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 9, 1, 5),
    _HwConnectMaxSnrTime_Type()
)
hwConnectMaxSnrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConnectMaxSnrTime.setStatus("current")
_HwRadioQueryPowerlevelTable_Object = MibTable
hwRadioQueryPowerlevelTable = _HwRadioQueryPowerlevelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 10)
)
if mibBuilder.loadTexts:
    hwRadioQueryPowerlevelTable.setStatus("current")
_HwRadioQueryPowerlevelEntry_Object = MibTableRow
hwRadioQueryPowerlevelEntry = _HwRadioQueryPowerlevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 10, 1)
)
hwRadioQueryPowerlevelEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioQueryPowerlevelChannel"),
    (0, "HUAWEI-WLAN-RADIO-MIB", "hwRadioQueryPowerlevelBandwidth"),
)
if mibBuilder.loadTexts:
    hwRadioQueryPowerlevelEntry.setStatus("current")
_HwRadioQueryPowerlevelChannel_Type = Integer32
_HwRadioQueryPowerlevelChannel_Object = MibTableColumn
hwRadioQueryPowerlevelChannel = _HwRadioQueryPowerlevelChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 10, 1, 1),
    _HwRadioQueryPowerlevelChannel_Type()
)
hwRadioQueryPowerlevelChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRadioQueryPowerlevelChannel.setStatus("current")
_HwRadioQueryPowerlevelBandwidth_Type = Integer32
_HwRadioQueryPowerlevelBandwidth_Object = MibTableColumn
hwRadioQueryPowerlevelBandwidth = _HwRadioQueryPowerlevelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 10, 1, 2),
    _HwRadioQueryPowerlevelBandwidth_Type()
)
hwRadioQueryPowerlevelBandwidth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRadioQueryPowerlevelBandwidth.setStatus("current")
_HwRadioQueryPowerlevelMax_Type = Integer32
_HwRadioQueryPowerlevelMax_Object = MibTableColumn
hwRadioQueryPowerlevelMax = _HwRadioQueryPowerlevelMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 34, 10, 1, 3),
    _HwRadioQueryPowerlevelMax_Type()
)
hwRadioQueryPowerlevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioQueryPowerlevelMax.setStatus("current")
_HwRadioConformance_ObjectIdentity = ObjectIdentity
hwRadioConformance = _HwRadioConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35)
)
_HwRadioCompliances_ObjectIdentity = ObjectIdentity
hwRadioCompliances = _HwRadioCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 1)
)
_HwRadioObjectGroups_ObjectIdentity = ObjectIdentity
hwRadioObjectGroups = _HwRadioObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2)
)

# Managed Objects groups

hwRadioProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 1)
)
hwRadioProfileGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRateMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRateValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPowerMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPERThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioConfictRateThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRTSThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioFragmentThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioShortFrameRetryTimes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLongFrameRetryTimes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSupportShortPreamble"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDTIMInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBeaconInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWMMProfileName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioProfileRowStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211nGuardIntervalMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211nAMPDUMaxLengthExponent"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioInterfDetDevice"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioApComInterfThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioApAdjInterfThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaInterfThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDeviceReportDuration"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRTSMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWifiLight"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBeamformingSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWidsDevSynchronizationInt"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelSwitchAnnouncement"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelSwitchMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAccessSignalStrengthSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAccessSignalStrengthThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBackgroundListenNeighborSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBackgroundScanningServiceThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBackgroundScanningClientThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAccessRateLimitSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAccessRateLimitThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSpectrumAnalysisScanPeriod"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSpectrumAnalysisScanInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioHighDenseSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioHighDenseMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaOfflineSignalStrengthSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaOfflineSignalStrengthThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaOfflineRateLimitSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaOfflineRateThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDynamicAdjustPowerSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationReportTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationScanInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationScanPeriod"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAirTimeScheduleSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateScanCycle"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacPolicyType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacPolicySwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacAccessThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacRoamThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacHideSSIDSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211acGuardIntervalMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211acAMPDUMaxLengthExponent"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211bgBasicRateSet"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211bgSupportRateSet"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211aBasicRateSet"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211aSupportRateSet"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211nSupportMCS"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211acSupportMcsMapMcs"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMulticastRate2G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMulticastRate5G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLegacyStationEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationScanChannel2G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationScanChannel5G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAMSDUTxEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAMSDUTxMaxSubFrames"))
)
if mibBuilder.loadTexts:
    hwRadioProfileGroup.setStatus("current")

hwRadioManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 2)
)
hwRadioManageGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngBaseBssID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngRadioProfileName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngState"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAvailableSntennaNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWorkingChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWorkingPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWorkingPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWorkingChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211nMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWidsWorkMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngBinded"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDeviceDetectEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMaxTxPwrLvl"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPwrAttRange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPwrAttValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAntennaGain"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBridgeWhitelistEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBridgeWhitelistName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBridgeStpSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBridgeSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBridgeMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUndoBridgeWhitelist"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUserTrafficScheduler"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCountermeasuresMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioFrequency"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCountermeasuresSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSpectrumAnalysisEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWidsAttackDetEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMeshWhitelistName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUndoMeshWhitelist"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMeshRole"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLocationScanChannelEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio80211nMulticastMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSpectrogramServerReportEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRadioMulticastRateValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio11acSpatialStream"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadio11acMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActiveSwitch"))
)
if mibBuilder.loadTexts:
    hwRadioManageGroup.setStatus("current")

hwRadioCalibrateStatisicsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 3)
)
hwRadioCalibrateStatisicsGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalStatisSignalBadCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalStatisCalibratePowerCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalStatisCalibrateChannelCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateStatisicsOperMode"))
)
if mibBuilder.loadTexts:
    hwRadioCalibrateStatisicsGroup.setStatus("current")

hwRadioAuthNeighborInfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 4)
)
hwRadioAuthNeighborInfGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwAuthenticRadioNeighborAPID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAuthenticRadioNeighborChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAuthenticRadioNeighborFrontAttenu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAuthenticRadioNeighborBackAttenu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAuthenticRadioNeighborSSID"))
)
if mibBuilder.loadTexts:
    hwRadioAuthNeighborInfGroup.setStatus("current")

hwRadioLoadBalanceGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 5)
)
hwRadioLoadBalanceGroupGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwLBGroupMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBGapThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBAssociateThreshold"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBGroupStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupGroup.setStatus("current")

hwRadioLoadBalanceGroupMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 6)
)
hwRadioLoadBalanceGroupMemberGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRadioChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRadioPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRadioPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRadioSeesionNum"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRadioTraffic"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwLBMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwRadioLoadBalanceGroupMemberGroup.setStatus("current")

hwRadioUncontrolAPInfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 7)
)
hwRadioUncontrolAPInfGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwUncontrolAPBSSID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAuthAPIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwUncontrolAPChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwUncontrolAPRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwUncontrolAPSSID"))
)
if mibBuilder.loadTexts:
    hwRadioUncontrolAPInfGroup.setStatus("current")

hwRadioPerformanceStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 8)
)
hwRadioPerformanceStatGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendRtsSuccess"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendUnicast"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendBroadcast"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendFailFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvPhyErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvCrcErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvMicErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvKeyDecryptErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRetryFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPER"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChUtilizationRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPerformanceStatOperMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPEROfLastPeriod"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownMacErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvUnicastFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvMngFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvCtrlFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendMngFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendCtrlFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaMaxSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaMinSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAvgSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRecvRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDropRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAirPortDhcpFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAirPortEapolFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAirPortPsPollFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAssocRequestFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAssocResponseFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioReassocRequestFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioReassocResponseFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDisassocFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDisauthFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvBytes64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendBytes64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendRtsSuccess64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendUnicast64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendBroadcast64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendFailFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvPhyErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvCrcErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvMicErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvKeyDecryptErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRetryFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownMacErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioNoise"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSendDropFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRcvDropFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelFreeRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioTxRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioRxRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChInterferenceRate"))
)
if mibBuilder.loadTexts:
    hwRadioPerformanceStatGroup.setStatus("current")

hwRadioUnauthenticNeighborInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 9)
)
hwRadioUnauthenticNeighborInfoGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwUnauthenticRadioNeighborBSSID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwUnauthenticRadioNeighborRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwunauthenticRadioNeighborChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwUnauthenticRadioNeighborSSID"))
)
if mibBuilder.loadTexts:
    hwRadioUnauthenticNeighborInfoGroup.setStatus("current")

hwRadioRegionCalibrateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 10)
)
hwRadioRegionCalibrateGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRegionCalibrateStartupMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRegionCalibrateAutoTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRegionCalibrateListenMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRegionCalibrateStatus"))
)
if mibBuilder.loadTexts:
    hwRadioRegionCalibrateGroup.setStatus("current")

hwRadioGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 11)
)
hwRadioGlobalGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwBatchRadioProfileStartNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchRadioProfileNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchRadioProfileReturnNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchRadioProfileName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchLoadBalanceGroupStartNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchLoadBalanceGroupNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchLoadBalanceGroupReturnNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchLoadBalanceGroupName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchUncontrolAPStartNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchUncontrolAPNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchUncontrolAPReturnNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchUncontrolAPBssid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwBatchUncontrolAPAuthNeighborIndex"))
)
if mibBuilder.loadTexts:
    hwRadioGlobalGroup.setStatus("current")

hwRadioNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 13)
)
hwRadioNotifyObjectGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioConflictRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApMonitorMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApPreMonitorMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApInterfBssid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfStaMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCause"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoAPID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRadioId"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoAPMAC"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueMAC"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueSSId"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueChanID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualAntennaGain"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLegitimateAntennaGain"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelChangedReason"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelChangedReasonStr"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCauseStr"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPreActualChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPowerChangedReasonStr"))
)
if mibBuilder.loadTexts:
    hwRadioNotifyObjectGroup.setStatus("current")

hwRadioParaStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 14)
)
hwRadioParaStatisticGroup.setObjects(
    ("HUAWEI-WLAN-RADIO-MIB", "hwRadioStaAveSignalStrength")
)
if mibBuilder.loadTexts:
    hwRadioParaStatisticGroup.setStatus("current")

hwMacRadioManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 15)
)
hwMacRadioManageGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngBaseBssID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngRadioProfileName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngState"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAvailableSntennaNumber"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioWorkingChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioWorkingPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioWorkingPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioWorkingChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadio80211nMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioWidsWorkMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMngBinded"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMaxTxPwrLvl"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPwrAttRange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPwrAttValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAntennaGain"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBridgeWhitelistEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBridgeWhitelistName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBridgeStpSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBridgeSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBridgeMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioUndoBridgeWhitelist"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioUserTrafficScheduler"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCountermeasuresMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioFrequency"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCountermeasuresSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSpectrumAnalysisEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMACRadioWidsAttackDetEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMeshWhitelistName"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacUndoMeshWhitelist"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMeshRole"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioLocationEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioLocationScanChannelEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadio80211nMulticastMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSpectrogramServerReportEnable"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMulticastRateValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadio11acSpatialStream"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadio11acMCSValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioActiveSwitch"))
)
if mibBuilder.loadTexts:
    hwMacRadioManageGroup.setStatus("current")

hwMacRadioCalibrateStatisicsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 16)
)
hwMacRadioCalibrateStatisicsGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCalStatisSignalBadCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCalStatisCalibratePowerCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCalStatisCalibrateChannelCount"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioCalibrateStatisicsOperMode"))
)
if mibBuilder.loadTexts:
    hwMacRadioCalibrateStatisicsGroup.setStatus("current")

hwMacRadioAuthNeighborInfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 17)
)
hwMacRadioAuthNeighborInfGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborFrontAttenu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborBackAttenu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborAPMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborSSID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacAuthenticRadioNeighborAPID"))
)
if mibBuilder.loadTexts:
    hwMacRadioAuthNeighborInfGroup.setStatus("current")

hwMacRadioLoadBalanceGroupMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 18)
)
hwMacRadioLoadBalanceGroupMemberGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRadioChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRadioPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRadioPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRadioSeesionNum"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRadioTraffic"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacLBMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwMacRadioLoadBalanceGroupMemberGroup.setStatus("current")

hwMacRadioPerformanceStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 19)
)
hwMacRadioPerformanceStatGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendRtsSuccess"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendUnicast"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendBroadcast"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendFailFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvPhyErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvCrcErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvMicErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvKeyDecryptErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRetryFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPER"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioChUtilizationRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPerformanceStatOperMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPEROfLastPeriod"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDownMacErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvUnicastFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvMngFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvCtrlFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendMngFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendCtrlFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioStaMaxSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioStaMinSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioStaAvgSignalStrength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRecvRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDropRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAirPortDhcpFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAirPortEapolFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAirPortPsPollFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAssocRequestFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAssocResponseFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioReassocRequestFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioReassocResponseFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDisassocFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDisauthFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvBytes64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendBytes64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendRtsSuccess64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendUnicast64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendBroadcast64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendFailFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvPhyErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvCrcErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvMicErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvKeyDecryptErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRetryFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDownMacErrFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioNoise"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioActualBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioSendDropFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRcvDropFrames64Bits"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioChannelFreeRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioTxRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioRxRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioChInterferenceRate"))
)
if mibBuilder.loadTexts:
    hwMacRadioPerformanceStatGroup.setStatus("current")

hwMacRadioUnauthenticNeighborInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 20)
)
hwMacRadioUnauthenticNeighborInfoGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacUnauthenticRadioNeighborBSSID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacUnauthenticRadioNeighborRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacunauthenticRadioNeighborChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacUnauthenticRadioNeighborSSID"))
)
if mibBuilder.loadTexts:
    hwMacRadioUnauthenticNeighborInfoGroup.setStatus("current")

hwRadioInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 21)
)
hwRadioInfoGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioDecsption"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPortType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMaxMtu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAdminStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioOperStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLastChange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioInfoUpDownTimes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAutoOffSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAutoOffStartTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAutoOffEndTime"))
)
if mibBuilder.loadTexts:
    hwRadioInfoGroup.setStatus("current")

hwMacRadioInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 22)
)
hwMacRadioInfoGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioDecsption"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioPortType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMaxMtu"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAdminStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioOperStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioLastChange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioInfoUpDownTimes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAutoOffSwitch"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAutoOffStartTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwMacRadioAutoOffEndTime"))
)
if mibBuilder.loadTexts:
    hwMacRadioInfoGroup.setStatus("current")

hwRadioCalibrateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 23)
)
hwRadioCalibrateGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateManualStartup"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateCycle"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibratePolicy"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibratesensitivity"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioGlobalCalibrateChannel5G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioGlobalScanChannel5G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioGlobalCalibrateChannel2G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioGlobalScanChannel2G"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioGlobalCalibrate5gBandWidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioCalibrateAutoStartTime"))
)
if mibBuilder.loadTexts:
    hwRadioCalibrateGroup.setStatus("current")

hwConnectStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 24)
)
hwConnectStatusGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusPeerMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusSsid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatus"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusSNR"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusNoiseFloor"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusActualTxPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusBeaconInterval"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusCurrentRate"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusTxBeamforming"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusActualCountryCode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatusDistance"))
)
if mibBuilder.loadTexts:
    hwConnectStatusGroup.setStatus("current")

hwConnectStatisticsGruop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 25)
)
hwConnectStatisticsGruop.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatisticsPeerMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRxOkUcastDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRxOkUcastDataBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectTxOkUcastDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectTxOkUcastDataBytes"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRxThroughput"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectTxThroughput"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRxErrFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectTxErrUcastDataFrames"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectUcastDataFrameTxRetryRatio"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectOnlineTime"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectStatisticsReset"))
)
if mibBuilder.loadTexts:
    hwConnectStatisticsGruop.setStatus("current")

hwConnectRateHistogramGruop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 26)
)
hwConnectRateHistogramGruop.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectRateStatDirection"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRateStatRange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectRateStatUcastDataFrames"))
)
if mibBuilder.loadTexts:
    hwConnectRateHistogramGruop.setStatus("current")

hwConnectAMPDUHistogramGruop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 27)
)
hwConnectAMPDUHistogramGruop.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectAMPDUStatDirection"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectAMPDUStatRange"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectAMPDUStatUcastDataFrames"))
)
if mibBuilder.loadTexts:
    hwConnectAMPDUHistogramGruop.setStatus("current")

hwConnectLenHistogramGruop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 28)
)
hwConnectLenHistogramGruop.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectDataLenStatDirection"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectDataLenStatLength"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectDataLenStatFrameCounts"))
)
if mibBuilder.loadTexts:
    hwConnectLenHistogramGruop.setStatus("current")

hwConnectMaxSnrGruop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 29)
)
hwConnectMaxSnrGruop.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrPeerMAC"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrValue"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrNoiseFloor"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrSSID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwConnectMaxSnrTime"))
)
if mibBuilder.loadTexts:
    hwConnectMaxSnrGruop.setStatus("current")


# Notification objects

hwRadioChannelChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 1)
)
hwRadioChannelChangedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualChannel"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelChangedReason"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelChangedReasonStr"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPreActualChannel"))
)
if mibBuilder.loadTexts:
    hwRadioChannelChangedNotify.setStatus(
        "current"
    )

hwRadioSignalEnvDeteriorationNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 2)
)
hwRadioSignalEnvDeteriorationNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPER"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioConflictRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwRadioSignalEnvDeteriorationNotify.setStatus(
        "current"
    )

hwRadioSignalEnvResumeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 3)
)
hwRadioSignalEnvResumeNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwRadioSignalEnvResumeNotify.setStatus(
        "current"
    )

hwApMonitorModeChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 4)
)
hwApMonitorModeChangedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApMonitorMode"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApPreMonitorMode"))
)
if mibBuilder.loadTexts:
    hwApMonitorModeChangedNotify.setStatus(
        "current"
    )

hwAPCoInterfDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 5)
)
hwAPCoInterfDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApInterfBssid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfRSSI"))
)
if mibBuilder.loadTexts:
    hwAPCoInterfDetectedNotify.setStatus(
        "current"
    )

hwAPCoInterfClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 6)
)
hwAPCoInterfClearNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApInterfBssid"))
)
if mibBuilder.loadTexts:
    hwAPCoInterfClearNotify.setStatus(
        "current"
    )

hwNerborInterfDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 7)
)
hwNerborInterfDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApInterfBssid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfRSSI"))
)
if mibBuilder.loadTexts:
    hwNerborInterfDetectedNotify.setStatus(
        "current"
    )

hwNeiborInterfClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 8)
)
hwNeiborInterfClearNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApInterfBssid"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfApChannel"))
)
if mibBuilder.loadTexts:
    hwNeiborInterfClearNotify.setStatus(
        "current"
    )

hwStaInterfDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 9)
)
hwStaInterfDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfStaMac"))
)
if mibBuilder.loadTexts:
    hwStaInterfDetectedNotify.setStatus(
        "current"
    )

hwStaInterfClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 10)
)
hwStaInterfClearNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwInterfStaMac"))
)
if mibBuilder.loadTexts:
    hwStaInterfClearNotify.setStatus(
        "current"
    )

hwOtherDeviceInterfDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 11)
)
hwOtherDeviceInterfDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"))
)
if mibBuilder.loadTexts:
    hwOtherDeviceInterfDetectedNotify.setStatus(
        "current"
    )

hwOtherDeviceInterfClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 12)
)
hwOtherDeviceInterfClearNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApChannel"))
)
if mibBuilder.loadTexts:
    hwOtherDeviceInterfClearNotify.setStatus(
        "current"
    )

hwRadioDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 13)
)
hwRadioDownNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCause"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCauseStr"))
)
if mibBuilder.loadTexts:
    hwRadioDownNotify.setStatus(
        "current"
    )

hwRadioDownRecovNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 14)
)
hwRadioDownRecovNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCause"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownCauseStr"))
)
if mibBuilder.loadTexts:
    hwRadioDownRecovNotify.setStatus(
        "current"
    )

hwWIDSDetectRogueNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 15)
)
hwWIDSDetectRogueNotify.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoAPID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRadioId"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoAPMAC"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueMAC"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueSSId"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueType"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueRSSI"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSTrapInfoRogueChanID"))
)
if mibBuilder.loadTexts:
    hwWIDSDetectRogueNotify.setStatus(
        "current"
    )

hwRadioNotSupportChannelNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 16)
)
hwRadioNotSupportChannelNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngChannel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualChannelBandwidth"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualChannel"))
)
if mibBuilder.loadTexts:
    hwRadioNotSupportChannelNotify.setStatus(
        "current"
    )

hwRadioNotSupportPowerLevelNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 17)
)
hwRadioNotSupportPowerLevelNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioMngPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualPowerLevel"))
)
if mibBuilder.loadTexts:
    hwRadioNotSupportPowerLevelNotify.setStatus(
        "current"
    )

hwRadioAntennaGainIsUnlawfulNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 18)
)
hwRadioAntennaGainIsUnlawfulNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualAntennaGain"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioLegitimateAntennaGain"))
)
if mibBuilder.loadTexts:
    hwRadioAntennaGainIsUnlawfulNotify.setStatus(
        "current"
    )

hwRadioPowerChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 19)
)
hwRadioPowerChangedNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioActualPowerLevel"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioWorkingPower"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPowerChangedReasonStr"))
)
if mibBuilder.loadTexts:
    hwRadioPowerChangedNotify.setStatus(
        "current"
    )

hwApAccessUserNumExceedThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 20)
)
hwApAccessUserNumExceedThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApAccessUserNumExceedThresholdNotify.setStatus(
        "current"
    )

hwApAccessUserNumExceedThresholdRecovNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 21)
)
hwApAccessUserNumExceedThresholdRecovNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApAccessUserNumExceedThresholdRecovNotify.setStatus(
        "current"
    )

hwApRoamUserNumExceedThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 22)
)
hwApRoamUserNumExceedThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApRoamUserNumExceedThresholdNotify.setStatus(
        "current"
    )

hwApRoamUserNumExceedThresholdRecovNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 23)
)
hwApRoamUserNumExceedThresholdRecovNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApRoamUserNumExceedThresholdRecovNotify.setStatus(
        "current"
    )

hwApAccessChannelUtilExceedThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 24)
)
hwApAccessChannelUtilExceedThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApAccessChannelUtilExceedThresholdNotify.setStatus(
        "current"
    )

hwApAccessChannelUtilExceedThresholdRecovNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 25)
)
hwApAccessChannelUtilExceedThresholdRecovNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApAccessChannelUtilExceedThresholdRecovNotify.setStatus(
        "current"
    )

hwApRoamChannelUtilExceedThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 26)
)
hwApRoamChannelUtilExceedThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApRoamChannelUtilExceedThresholdNotify.setStatus(
        "current"
    )

hwApRoamChannelUtilExceedThresholdRecovNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 27)
)
hwApRoamChannelUtilExceedThresholdRecovNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUacUserNum"))
)
if mibBuilder.loadTexts:
    hwApRoamChannelUtilExceedThresholdRecovNotify.setStatus(
        "current"
    )

hwRadioUploadRemoteCaptureFileNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 24, 1, 28)
)
hwRadioUploadRemoteCaptureFileNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"))
)
if mibBuilder.loadTexts:
    hwRadioUploadRemoteCaptureFileNotify.setStatus(
        "current"
    )


# Notifications groups

hwRadioNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 2, 12)
)
hwRadioNotifyGroup.setObjects(
      *(("HUAWEI-WLAN-RADIO-MIB", "hwRadioChannelChangedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSignalEnvDeteriorationNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioSignalEnvResumeNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApMonitorModeChangedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAPCoInterfDetectedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwAPCoInterfClearNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwNerborInterfDetectedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwNeiborInterfClearNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwStaInterfDetectedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwStaInterfClearNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwOtherDeviceInterfDetectedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwOtherDeviceInterfClearNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioDownRecovNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwWIDSDetectRogueNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioNotSupportChannelNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioNotSupportPowerLevelNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioAntennaGainIsUnlawfulNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioPowerChangedNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApAccessUserNumExceedThresholdNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApAccessUserNumExceedThresholdRecovNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApRoamUserNumExceedThresholdNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApRoamUserNumExceedThresholdRecovNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApAccessChannelUtilExceedThresholdNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApAccessChannelUtilExceedThresholdRecovNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApRoamChannelUtilExceedThresholdNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwApRoamChannelUtilExceedThresholdRecovNotify"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioUploadRemoteCaptureFileNotify"))
)
if mibBuilder.loadTexts:
    hwRadioNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRadioCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 3, 35, 1, 1)
)
if mibBuilder.loadTexts:
    hwRadioCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-RADIO-MIB",
    **{"hwRadio": hwRadio,
       "hwRadioProfileTable": hwRadioProfileTable,
       "hwRadioProfileEntry": hwRadioProfileEntry,
       "hwRadioProfileName": hwRadioProfileName,
       "hwRadioType": hwRadioType,
       "hwRadioRateMode": hwRadioRateMode,
       "hwRadioRateValue": hwRadioRateValue,
       "hwRadioChannelMode": hwRadioChannelMode,
       "hwRadioPowerMode": hwRadioPowerMode,
       "hwRadioCalibrateInterval": hwRadioCalibrateInterval,
       "hwRadioPERThreshold": hwRadioPERThreshold,
       "hwRadioConfictRateThreshold": hwRadioConfictRateThreshold,
       "hwRadioRTSThreshold": hwRadioRTSThreshold,
       "hwRadioFragmentThreshold": hwRadioFragmentThreshold,
       "hwRadioShortFrameRetryTimes": hwRadioShortFrameRetryTimes,
       "hwRadioLongFrameRetryTimes": hwRadioLongFrameRetryTimes,
       "hwRadioSupportShortPreamble": hwRadioSupportShortPreamble,
       "hwRadioDTIMInterval": hwRadioDTIMInterval,
       "hwRadioBeaconInterval": hwRadioBeaconInterval,
       "hwRadioWMMProfileName": hwRadioWMMProfileName,
       "hwRadioProfileRowStatus": hwRadioProfileRowStatus,
       "hwRadio80211nGuardIntervalMode": hwRadio80211nGuardIntervalMode,
       "hwRadio80211nAMPDUMaxLengthExponent": hwRadio80211nAMPDUMaxLengthExponent,
       "hwRadioCalibrateEnable": hwRadioCalibrateEnable,
       "hwRadioInterfDetDevice": hwRadioInterfDetDevice,
       "hwRadioApComInterfThreshold": hwRadioApComInterfThreshold,
       "hwRadioApAdjInterfThreshold": hwRadioApAdjInterfThreshold,
       "hwRadioStaInterfThreshold": hwRadioStaInterfThreshold,
       "hwRadioDeviceReportDuration": hwRadioDeviceReportDuration,
       "hwRadioRTSMode": hwRadioRTSMode,
       "hwRadioWifiLight": hwRadioWifiLight,
       "hwRadioBeamformingSwitch": hwRadioBeamformingSwitch,
       "hwRadioWidsDevSynchronizationInt": hwRadioWidsDevSynchronizationInt,
       "hwRadioChannelSwitchAnnouncement": hwRadioChannelSwitchAnnouncement,
       "hwRadioChannelSwitchMode": hwRadioChannelSwitchMode,
       "hwRadioStaAccessSignalStrengthSwitch": hwRadioStaAccessSignalStrengthSwitch,
       "hwRadioStaAccessSignalStrengthThreshold": hwRadioStaAccessSignalStrengthThreshold,
       "hwRadioBackgroundListenNeighborSwitch": hwRadioBackgroundListenNeighborSwitch,
       "hwRadioBackgroundScanningServiceThreshold": hwRadioBackgroundScanningServiceThreshold,
       "hwRadioBackgroundScanningClientThreshold": hwRadioBackgroundScanningClientThreshold,
       "hwRadioStaAccessRateLimitSwitch": hwRadioStaAccessRateLimitSwitch,
       "hwRadioStaAccessRateLimitThreshold": hwRadioStaAccessRateLimitThreshold,
       "hwRadioSpectrumAnalysisScanPeriod": hwRadioSpectrumAnalysisScanPeriod,
       "hwRadioSpectrumAnalysisScanInterval": hwRadioSpectrumAnalysisScanInterval,
       "hwRadioHighDenseSwitch": hwRadioHighDenseSwitch,
       "hwRadioHighDenseMode": hwRadioHighDenseMode,
       "hwRadioStaOfflineSignalStrengthSwitch": hwRadioStaOfflineSignalStrengthSwitch,
       "hwRadioStaOfflineSignalStrengthThreshold": hwRadioStaOfflineSignalStrengthThreshold,
       "hwRadioStaOfflineRateLimitSwitch": hwRadioStaOfflineRateLimitSwitch,
       "hwRadioStaOfflineRateThreshold": hwRadioStaOfflineRateThreshold,
       "hwRadioDynamicAdjustPowerSwitch": hwRadioDynamicAdjustPowerSwitch,
       "hwRadioLocationReportTime": hwRadioLocationReportTime,
       "hwRadioLocationScanInterval": hwRadioLocationScanInterval,
       "hwRadioLocationScanPeriod": hwRadioLocationScanPeriod,
       "hwRadioAirTimeScheduleSwitch": hwRadioAirTimeScheduleSwitch,
       "hwRadioCalibrateScanCycle": hwRadioCalibrateScanCycle,
       "hwRadioUacPolicyType": hwRadioUacPolicyType,
       "hwRadioUacPolicySwitch": hwRadioUacPolicySwitch,
       "hwRadioUacAccessThreshold": hwRadioUacAccessThreshold,
       "hwRadioUacRoamThreshold": hwRadioUacRoamThreshold,
       "hwRadioUacHideSSIDSwitch": hwRadioUacHideSSIDSwitch,
       "hwRadio80211acGuardIntervalMode": hwRadio80211acGuardIntervalMode,
       "hwRadio80211acAMPDUMaxLengthExponent": hwRadio80211acAMPDUMaxLengthExponent,
       "hwRadio80211bgBasicRateSet": hwRadio80211bgBasicRateSet,
       "hwRadio80211bgSupportRateSet": hwRadio80211bgSupportRateSet,
       "hwRadio80211aBasicRateSet": hwRadio80211aBasicRateSet,
       "hwRadio80211aSupportRateSet": hwRadio80211aSupportRateSet,
       "hwRadio80211nSupportMCS": hwRadio80211nSupportMCS,
       "hwRadio80211acSupportMcsMapMcs": hwRadio80211acSupportMcsMapMcs,
       "hwRadioMulticastRate2G": hwRadioMulticastRate2G,
       "hwRadioMulticastRate5G": hwRadioMulticastRate5G,
       "hwRadioLegacyStationEnable": hwRadioLegacyStationEnable,
       "hwRadioLocationScanChannel2G": hwRadioLocationScanChannel2G,
       "hwRadioLocationScanChannel5G": hwRadioLocationScanChannel5G,
       "hwRadioAMSDUTxEnable": hwRadioAMSDUTxEnable,
       "hwRadioAMSDUTxMaxSubFrames": hwRadioAMSDUTxMaxSubFrames,
       "hwRadioManageTable": hwRadioManageTable,
       "hwRadioManageEntry": hwRadioManageEntry,
       "hwRadioID": hwRadioID,
       "hwRadioMngBaseBssID": hwRadioMngBaseBssID,
       "hwRadioMngRadioProfileName": hwRadioMngRadioProfileName,
       "hwRadioMngState": hwRadioMngState,
       "hwRadioMngChannel": hwRadioMngChannel,
       "hwRadioMngPowerLevel": hwRadioMngPowerLevel,
       "hwRadioMngPower": hwRadioMngPower,
       "hwRadioAvailableSntennaNumber": hwRadioAvailableSntennaNumber,
       "hwRadioWorkingChannel": hwRadioWorkingChannel,
       "hwRadioWorkingPowerLevel": hwRadioWorkingPowerLevel,
       "hwRadioWorkingPower": hwRadioWorkingPower,
       "hwRadioMngChannelBandwidth": hwRadioMngChannelBandwidth,
       "hwRadioWorkingChannelBandwidth": hwRadioWorkingChannelBandwidth,
       "hwRadio80211nMCSValue": hwRadio80211nMCSValue,
       "hwRadioWidsWorkMode": hwRadioWidsWorkMode,
       "hwRadioMngBinded": hwRadioMngBinded,
       "hwRadioDeviceDetectEnable": hwRadioDeviceDetectEnable,
       "hwRadioMaxTxPwrLvl": hwRadioMaxTxPwrLvl,
       "hwRadioPwrAttRange": hwRadioPwrAttRange,
       "hwRadioPwrAttValue": hwRadioPwrAttValue,
       "hwRadioAntennaGain": hwRadioAntennaGain,
       "hwRadioBridgeWhitelistEnable": hwRadioBridgeWhitelistEnable,
       "hwRadioBridgeWhitelistName": hwRadioBridgeWhitelistName,
       "hwRadioBridgeStpSwitch": hwRadioBridgeStpSwitch,
       "hwRadioBridgeSwitch": hwRadioBridgeSwitch,
       "hwRadioBridgeMode": hwRadioBridgeMode,
       "hwRadioUndoBridgeWhitelist": hwRadioUndoBridgeWhitelist,
       "hwRadioUserTrafficScheduler": hwRadioUserTrafficScheduler,
       "hwRadioCountermeasuresMode": hwRadioCountermeasuresMode,
       "hwRadioFrequency": hwRadioFrequency,
       "hwRadioCountermeasuresSwitch": hwRadioCountermeasuresSwitch,
       "hwRadioSpectrumAnalysisEnable": hwRadioSpectrumAnalysisEnable,
       "hwRadioWidsAttackDetEnable": hwRadioWidsAttackDetEnable,
       "hwRadioMeshWhitelistName": hwRadioMeshWhitelistName,
       "hwRadioUndoMeshWhitelist": hwRadioUndoMeshWhitelist,
       "hwRadioMeshRole": hwRadioMeshRole,
       "hwRadioLocationEnable": hwRadioLocationEnable,
       "hwRadioLocationScanChannelEnable": hwRadioLocationScanChannelEnable,
       "hwRadio80211nMulticastMCSValue": hwRadio80211nMulticastMCSValue,
       "hwRadioSpectrogramServerReportEnable": hwRadioSpectrogramServerReportEnable,
       "hwRadioRadioMulticastRateValue": hwRadioRadioMulticastRateValue,
       "hwRadio11acSpatialStream": hwRadio11acSpatialStream,
       "hwRadio11acMCSValue": hwRadio11acMCSValue,
       "hwRadioActiveSwitch": hwRadioActiveSwitch,
       "hwRadioCalibrateStatisicsTable": hwRadioCalibrateStatisicsTable,
       "hwRadioCalibrateStatisicsEntry": hwRadioCalibrateStatisicsEntry,
       "hwRadioCalStatisSignalBadCount": hwRadioCalStatisSignalBadCount,
       "hwRadioCalStatisCalibratePowerCount": hwRadioCalStatisCalibratePowerCount,
       "hwRadioCalStatisCalibrateChannelCount": hwRadioCalStatisCalibrateChannelCount,
       "hwRadioCalibrateStatisicsOperMode": hwRadioCalibrateStatisicsOperMode,
       "hwRadioAuthNeighborInfTable": hwRadioAuthNeighborInfTable,
       "hwRadioAuthNeighborInfEntry": hwRadioAuthNeighborInfEntry,
       "hwAuthenticRadioNeighborAPID": hwAuthenticRadioNeighborAPID,
       "hwAuthenticRadioNeighborChannel": hwAuthenticRadioNeighborChannel,
       "hwAuthenticRadioNeighborFrontAttenu": hwAuthenticRadioNeighborFrontAttenu,
       "hwAuthenticRadioNeighborBackAttenu": hwAuthenticRadioNeighborBackAttenu,
       "hwAuthenticRadioNeighborSSID": hwAuthenticRadioNeighborSSID,
       "hwRadioLoadBalanceGroupTable": hwRadioLoadBalanceGroupTable,
       "hwRadioLoadBalanceGroupEntry": hwRadioLoadBalanceGroupEntry,
       "hwLBGroupName": hwLBGroupName,
       "hwLBGroupMode": hwLBGroupMode,
       "hwLBGapThreshold": hwLBGapThreshold,
       "hwLBAssociateThreshold": hwLBAssociateThreshold,
       "hwLBGroupStatus": hwLBGroupStatus,
       "hwLBGroupRowStatus": hwLBGroupRowStatus,
       "hwRadioLoadBalanceGroupMemberTable": hwRadioLoadBalanceGroupMemberTable,
       "hwRadioLoadBalanceGroupMemberEntry": hwRadioLoadBalanceGroupMemberEntry,
       "hwLBMemberRadioChannel": hwLBMemberRadioChannel,
       "hwLBMemberRadioPowerLevel": hwLBMemberRadioPowerLevel,
       "hwLBMemberRadioPower": hwLBMemberRadioPower,
       "hwLBMemberRadioSeesionNum": hwLBMemberRadioSeesionNum,
       "hwLBMemberRadioTraffic": hwLBMemberRadioTraffic,
       "hwLBMemberRowStatus": hwLBMemberRowStatus,
       "hwRadioUncontrolAPInfTable": hwRadioUncontrolAPInfTable,
       "hwRadioUncontrolAPInfEntry": hwRadioUncontrolAPInfEntry,
       "hwUncontrolAPIndex": hwUncontrolAPIndex,
       "hwUncontrolAPBSSID": hwUncontrolAPBSSID,
       "hwAuthAPIndex": hwAuthAPIndex,
       "hwUncontrolAPChannel": hwUncontrolAPChannel,
       "hwUncontrolAPRSSI": hwUncontrolAPRSSI,
       "hwUncontrolAPSSID": hwUncontrolAPSSID,
       "hwRadioPerformanceStatTable": hwRadioPerformanceStatTable,
       "hwRadioPerformanceStatEntry": hwRadioPerformanceStatEntry,
       "hwRadioRcvFrames": hwRadioRcvFrames,
       "hwRadioRcvBytes": hwRadioRcvBytes,
       "hwRadioSendFrames": hwRadioSendFrames,
       "hwRadioSendBytes": hwRadioSendBytes,
       "hwRadioSendRtsSuccess": hwRadioSendRtsSuccess,
       "hwRadioSendUnicast": hwRadioSendUnicast,
       "hwRadioSendBroadcast": hwRadioSendBroadcast,
       "hwRadioSendFailFrames": hwRadioSendFailFrames,
       "hwRadioRcvErrFrames": hwRadioRcvErrFrames,
       "hwRadioRcvPhyErrFrames": hwRadioRcvPhyErrFrames,
       "hwRadioRcvCrcErrFrames": hwRadioRcvCrcErrFrames,
       "hwRadioRcvMicErrFrames": hwRadioRcvMicErrFrames,
       "hwRadioRcvKeyDecryptErrFrames": hwRadioRcvKeyDecryptErrFrames,
       "hwRadioRetryFrames": hwRadioRetryFrames,
       "hwRadioPER": hwRadioPER,
       "hwRadioChUtilizationRate": hwRadioChUtilizationRate,
       "hwRadioPerformanceStatOperMode": hwRadioPerformanceStatOperMode,
       "hwRadioPEROfLastPeriod": hwRadioPEROfLastPeriod,
       "hwRadioRcvSignalStrength": hwRadioRcvSignalStrength,
       "hwRadioDownMacErrFrames": hwRadioDownMacErrFrames,
       "hwRadioRcvPower": hwRadioRcvPower,
       "hwRadioRcvUnicastFrames": hwRadioRcvUnicastFrames,
       "hwRadioRcvMngFrames": hwRadioRcvMngFrames,
       "hwRadioRcvCtrlFrames": hwRadioRcvCtrlFrames,
       "hwRadioRcvDataFrames": hwRadioRcvDataFrames,
       "hwRadioSendMngFrames": hwRadioSendMngFrames,
       "hwRadioSendCtrlFrames": hwRadioSendCtrlFrames,
       "hwRadioSendDataFrames": hwRadioSendDataFrames,
       "hwRadioStaMaxSignalStrength": hwRadioStaMaxSignalStrength,
       "hwRadioStaMinSignalStrength": hwRadioStaMinSignalStrength,
       "hwRadioStaAvgSignalStrength": hwRadioStaAvgSignalStrength,
       "hwRadioSendRate": hwRadioSendRate,
       "hwRadioRecvRate": hwRadioRecvRate,
       "hwRadioDropRate": hwRadioDropRate,
       "hwRadioAirPortDhcpFrames": hwRadioAirPortDhcpFrames,
       "hwRadioAirPortEapolFrames": hwRadioAirPortEapolFrames,
       "hwRadioAirPortPsPollFrames": hwRadioAirPortPsPollFrames,
       "hwRadioAssocRequestFrames": hwRadioAssocRequestFrames,
       "hwRadioAssocResponseFrames": hwRadioAssocResponseFrames,
       "hwRadioReassocRequestFrames": hwRadioReassocRequestFrames,
       "hwRadioReassocResponseFrames": hwRadioReassocResponseFrames,
       "hwRadioDisassocFrames": hwRadioDisassocFrames,
       "hwRadioDisauthFrames": hwRadioDisauthFrames,
       "hwRadioRcvFrames64Bits": hwRadioRcvFrames64Bits,
       "hwRadioRcvBytes64Bits": hwRadioRcvBytes64Bits,
       "hwRadioSendFrames64Bits": hwRadioSendFrames64Bits,
       "hwRadioSendBytes64Bits": hwRadioSendBytes64Bits,
       "hwRadioSendRtsSuccess64Bits": hwRadioSendRtsSuccess64Bits,
       "hwRadioSendUnicast64Bits": hwRadioSendUnicast64Bits,
       "hwRadioSendBroadcast64Bits": hwRadioSendBroadcast64Bits,
       "hwRadioSendFailFrames64Bits": hwRadioSendFailFrames64Bits,
       "hwRadioRcvErrFrames64Bits": hwRadioRcvErrFrames64Bits,
       "hwRadioRcvPhyErrFrames64Bits": hwRadioRcvPhyErrFrames64Bits,
       "hwRadioRcvCrcErrFrames64Bits": hwRadioRcvCrcErrFrames64Bits,
       "hwRadioRcvMicErrFrames64Bits": hwRadioRcvMicErrFrames64Bits,
       "hwRadioRcvKeyDecryptErrFrames64Bits": hwRadioRcvKeyDecryptErrFrames64Bits,
       "hwRadioRetryFrames64Bits": hwRadioRetryFrames64Bits,
       "hwRadioDownMacErrFrames64Bits": hwRadioDownMacErrFrames64Bits,
       "hwRadioNoise": hwRadioNoise,
       "hwRadioActualBandwidth": hwRadioActualBandwidth,
       "hwRadioFrames": hwRadioFrames,
       "hwRadioSendDropFrames64Bits": hwRadioSendDropFrames64Bits,
       "hwRadioRcvDropFrames64Bits": hwRadioRcvDropFrames64Bits,
       "hwRadioChannelFreeRate": hwRadioChannelFreeRate,
       "hwRadioTxRate": hwRadioTxRate,
       "hwRadioRxRate": hwRadioRxRate,
       "hwRadioChInterferenceRate": hwRadioChInterferenceRate,
       "hwRadioUnauthenticNeighborInfoTable": hwRadioUnauthenticNeighborInfoTable,
       "hwRadioUnauthenticNeighborInfoEntry": hwRadioUnauthenticNeighborInfoEntry,
       "hwUnauthenticRadioNeighborBSSID": hwUnauthenticRadioNeighborBSSID,
       "hwUnauthenticRadioNeighborRSSI": hwUnauthenticRadioNeighborRSSI,
       "hwunauthenticRadioNeighborChannel": hwunauthenticRadioNeighborChannel,
       "hwUnauthenticRadioNeighborSSID": hwUnauthenticRadioNeighborSSID,
       "hwRadioRegionCalibrateTable": hwRadioRegionCalibrateTable,
       "hwRadioRegionCalibrateEntry": hwRadioRegionCalibrateEntry,
       "hwRegionCalibrateStartupMode": hwRegionCalibrateStartupMode,
       "hwRegionCalibrateAutoTime": hwRegionCalibrateAutoTime,
       "hwRegionCalibrateListenMode": hwRegionCalibrateListenMode,
       "hwRegionCalibrateStatus": hwRegionCalibrateStatus,
       "hwBatchRadioProfileStartNumber": hwBatchRadioProfileStartNumber,
       "hwBatchRadioProfileNumber": hwBatchRadioProfileNumber,
       "hwBatchRadioProfileReturnNumber": hwBatchRadioProfileReturnNumber,
       "hwBatchRadioProfileName": hwBatchRadioProfileName,
       "hwBatchLoadBalanceGroupStartNumber": hwBatchLoadBalanceGroupStartNumber,
       "hwBatchLoadBalanceGroupNumber": hwBatchLoadBalanceGroupNumber,
       "hwBatchLoadBalanceGroupReturnNumber": hwBatchLoadBalanceGroupReturnNumber,
       "hwBatchLoadBalanceGroupName": hwBatchLoadBalanceGroupName,
       "hwBatchUncontrolAPStartNumber": hwBatchUncontrolAPStartNumber,
       "hwBatchUncontrolAPNumber": hwBatchUncontrolAPNumber,
       "hwBatchUncontrolAPReturnNumber": hwBatchUncontrolAPReturnNumber,
       "hwBatchUncontrolAPBssid": hwBatchUncontrolAPBssid,
       "hwBatchUncontrolAPAuthNeighborIndex": hwBatchUncontrolAPAuthNeighborIndex,
       "hwRadioNotifications": hwRadioNotifications,
       "hwRadioNotify": hwRadioNotify,
       "hwRadioChannelChangedNotify": hwRadioChannelChangedNotify,
       "hwRadioSignalEnvDeteriorationNotify": hwRadioSignalEnvDeteriorationNotify,
       "hwRadioSignalEnvResumeNotify": hwRadioSignalEnvResumeNotify,
       "hwApMonitorModeChangedNotify": hwApMonitorModeChangedNotify,
       "hwAPCoInterfDetectedNotify": hwAPCoInterfDetectedNotify,
       "hwAPCoInterfClearNotify": hwAPCoInterfClearNotify,
       "hwNerborInterfDetectedNotify": hwNerborInterfDetectedNotify,
       "hwNeiborInterfClearNotify": hwNeiborInterfClearNotify,
       "hwStaInterfDetectedNotify": hwStaInterfDetectedNotify,
       "hwStaInterfClearNotify": hwStaInterfClearNotify,
       "hwOtherDeviceInterfDetectedNotify": hwOtherDeviceInterfDetectedNotify,
       "hwOtherDeviceInterfClearNotify": hwOtherDeviceInterfClearNotify,
       "hwRadioDownNotify": hwRadioDownNotify,
       "hwRadioDownRecovNotify": hwRadioDownRecovNotify,
       "hwWIDSDetectRogueNotify": hwWIDSDetectRogueNotify,
       "hwRadioNotSupportChannelNotify": hwRadioNotSupportChannelNotify,
       "hwRadioNotSupportPowerLevelNotify": hwRadioNotSupportPowerLevelNotify,
       "hwRadioAntennaGainIsUnlawfulNotify": hwRadioAntennaGainIsUnlawfulNotify,
       "hwRadioPowerChangedNotify": hwRadioPowerChangedNotify,
       "hwApAccessUserNumExceedThresholdNotify": hwApAccessUserNumExceedThresholdNotify,
       "hwApAccessUserNumExceedThresholdRecovNotify": hwApAccessUserNumExceedThresholdRecovNotify,
       "hwApRoamUserNumExceedThresholdNotify": hwApRoamUserNumExceedThresholdNotify,
       "hwApRoamUserNumExceedThresholdRecovNotify": hwApRoamUserNumExceedThresholdRecovNotify,
       "hwApAccessChannelUtilExceedThresholdNotify": hwApAccessChannelUtilExceedThresholdNotify,
       "hwApAccessChannelUtilExceedThresholdRecovNotify": hwApAccessChannelUtilExceedThresholdRecovNotify,
       "hwApRoamChannelUtilExceedThresholdNotify": hwApRoamChannelUtilExceedThresholdNotify,
       "hwApRoamChannelUtilExceedThresholdRecovNotify": hwApRoamChannelUtilExceedThresholdRecovNotify,
       "hwRadioUploadRemoteCaptureFileNotify": hwRadioUploadRemoteCaptureFileNotify,
       "hwRadioNotifyObjects": hwRadioNotifyObjects,
       "hwRadioActualChannel": hwRadioActualChannel,
       "hwRadioConflictRate": hwRadioConflictRate,
       "hwApMonitorMode": hwApMonitorMode,
       "hwApPreMonitorMode": hwApPreMonitorMode,
       "hwApChannel": hwApChannel,
       "hwApInterfBssid": hwApInterfBssid,
       "hwInterfStaMac": hwInterfStaMac,
       "hwRadioDownCause": hwRadioDownCause,
       "hwInterfApChannel": hwInterfApChannel,
       "hwInterfRSSI": hwInterfRSSI,
       "hwWIDSTrapInfoAPID": hwWIDSTrapInfoAPID,
       "hwWIDSTrapInfoRadioId": hwWIDSTrapInfoRadioId,
       "hwWIDSTrapInfoAPMAC": hwWIDSTrapInfoAPMAC,
       "hwWIDSTrapInfoRogueMAC": hwWIDSTrapInfoRogueMAC,
       "hwWIDSTrapInfoRogueSSId": hwWIDSTrapInfoRogueSSId,
       "hwWIDSTrapInfoRogueType": hwWIDSTrapInfoRogueType,
       "hwWIDSTrapInfoRogueRSSI": hwWIDSTrapInfoRogueRSSI,
       "hwWIDSTrapInfoRogueChanID": hwWIDSTrapInfoRogueChanID,
       "hwRadioActualChannelBandwidth": hwRadioActualChannelBandwidth,
       "hwRadioActualPowerLevel": hwRadioActualPowerLevel,
       "hwRadioActualAntennaGain": hwRadioActualAntennaGain,
       "hwRadioLegitimateAntennaGain": hwRadioLegitimateAntennaGain,
       "hwRadioChannelChangedReason": hwRadioChannelChangedReason,
       "hwRadioChannelChangedReasonStr": hwRadioChannelChangedReasonStr,
       "hwRadioDownCauseStr": hwRadioDownCauseStr,
       "hwRadioUacUserNum": hwRadioUacUserNum,
       "hwRadioPreActualChannel": hwRadioPreActualChannel,
       "hwRadioPowerChangedReasonStr": hwRadioPowerChangedReasonStr,
       "hwRadioParaStatisticTable": hwRadioParaStatisticTable,
       "hwRadioParaStatisticEntry": hwRadioParaStatisticEntry,
       "hwRadioStaAveSignalStrength": hwRadioStaAveSignalStrength,
       "hwMacRadioManageTable": hwMacRadioManageTable,
       "hwMacRadioManageEntry": hwMacRadioManageEntry,
       "hwMacRadioID": hwMacRadioID,
       "hwMacRadioMngBaseBssID": hwMacRadioMngBaseBssID,
       "hwMacRadioMngRadioProfileName": hwMacRadioMngRadioProfileName,
       "hwMacRadioMngState": hwMacRadioMngState,
       "hwMacRadioMngChannel": hwMacRadioMngChannel,
       "hwMacRadioMngPowerLevel": hwMacRadioMngPowerLevel,
       "hwMacRadioMngPower": hwMacRadioMngPower,
       "hwMacRadioAvailableSntennaNumber": hwMacRadioAvailableSntennaNumber,
       "hwMacRadioWorkingChannel": hwMacRadioWorkingChannel,
       "hwMacRadioWorkingPowerLevel": hwMacRadioWorkingPowerLevel,
       "hwMacRadioWorkingPower": hwMacRadioWorkingPower,
       "hwMacRadioMngChannelBandwidth": hwMacRadioMngChannelBandwidth,
       "hwMacRadioWorkingChannelBandwidth": hwMacRadioWorkingChannelBandwidth,
       "hwMacRadio80211nMCSValue": hwMacRadio80211nMCSValue,
       "hwMacRadioWidsWorkMode": hwMacRadioWidsWorkMode,
       "hwMacRadioMngBinded": hwMacRadioMngBinded,
       "hwMacRadioMaxTxPwrLvl": hwMacRadioMaxTxPwrLvl,
       "hwMacRadioPwrAttRange": hwMacRadioPwrAttRange,
       "hwMacRadioPwrAttValue": hwMacRadioPwrAttValue,
       "hwMacRadioAntennaGain": hwMacRadioAntennaGain,
       "hwMacRadioBridgeWhitelistEnable": hwMacRadioBridgeWhitelistEnable,
       "hwMacRadioBridgeWhitelistName": hwMacRadioBridgeWhitelistName,
       "hwMacRadioBridgeStpSwitch": hwMacRadioBridgeStpSwitch,
       "hwMacRadioBridgeSwitch": hwMacRadioBridgeSwitch,
       "hwMacRadioBridgeMode": hwMacRadioBridgeMode,
       "hwMacRadioUndoBridgeWhitelist": hwMacRadioUndoBridgeWhitelist,
       "hwMacRadioUserTrafficScheduler": hwMacRadioUserTrafficScheduler,
       "hwMacRadioCountermeasuresMode": hwMacRadioCountermeasuresMode,
       "hwMacRadioFrequency": hwMacRadioFrequency,
       "hwMacRadioCountermeasuresSwitch": hwMacRadioCountermeasuresSwitch,
       "hwMacRadioSpectrumAnalysisEnable": hwMacRadioSpectrumAnalysisEnable,
       "hwMACRadioWidsAttackDetEnable": hwMACRadioWidsAttackDetEnable,
       "hwMacRadioMeshWhitelistName": hwMacRadioMeshWhitelistName,
       "hwMacUndoMeshWhitelist": hwMacUndoMeshWhitelist,
       "hwMacRadioMeshRole": hwMacRadioMeshRole,
       "hwMacRadioLocationEnable": hwMacRadioLocationEnable,
       "hwMacRadioLocationScanChannelEnable": hwMacRadioLocationScanChannelEnable,
       "hwMacRadio80211nMulticastMCSValue": hwMacRadio80211nMulticastMCSValue,
       "hwMacRadioSpectrogramServerReportEnable": hwMacRadioSpectrogramServerReportEnable,
       "hwMacRadioMulticastRateValue": hwMacRadioMulticastRateValue,
       "hwMacRadio11acSpatialStream": hwMacRadio11acSpatialStream,
       "hwMacRadio11acMCSValue": hwMacRadio11acMCSValue,
       "hwMacRadioActiveSwitch": hwMacRadioActiveSwitch,
       "hwMacRadioCalibrateStatisicsTable": hwMacRadioCalibrateStatisicsTable,
       "hwMacRadioCalibrateStatisicsEntry": hwMacRadioCalibrateStatisicsEntry,
       "hwMacRadioCalStatisSignalBadCount": hwMacRadioCalStatisSignalBadCount,
       "hwMacRadioCalStatisCalibratePowerCount": hwMacRadioCalStatisCalibratePowerCount,
       "hwMacRadioCalStatisCalibrateChannelCount": hwMacRadioCalStatisCalibrateChannelCount,
       "hwMacRadioCalibrateStatisicsOperMode": hwMacRadioCalibrateStatisicsOperMode,
       "hwMacRadioAuthNeighborInfTable": hwMacRadioAuthNeighborInfTable,
       "hwMacRadioAuthNeighborInfEntry": hwMacRadioAuthNeighborInfEntry,
       "hwMacAuthenticRadioNeighborAPID": hwMacAuthenticRadioNeighborAPID,
       "hwMacAuthenticRadioNeighborChannel": hwMacAuthenticRadioNeighborChannel,
       "hwMacAuthenticRadioNeighborFrontAttenu": hwMacAuthenticRadioNeighborFrontAttenu,
       "hwMacAuthenticRadioNeighborBackAttenu": hwMacAuthenticRadioNeighborBackAttenu,
       "hwMacAuthenticRadioNeighborAPMac": hwMacAuthenticRadioNeighborAPMac,
       "hwMacAuthenticRadioNeighborSSID": hwMacAuthenticRadioNeighborSSID,
       "hwMacRadioLoadBalanceGroupMemberTable": hwMacRadioLoadBalanceGroupMemberTable,
       "hwMacRadioLoadBalanceGroupMemberEntry": hwMacRadioLoadBalanceGroupMemberEntry,
       "hwMacLBMemberRadioChannel": hwMacLBMemberRadioChannel,
       "hwMacLBMemberRadioPowerLevel": hwMacLBMemberRadioPowerLevel,
       "hwMacLBMemberRadioPower": hwMacLBMemberRadioPower,
       "hwMacLBMemberRadioSeesionNum": hwMacLBMemberRadioSeesionNum,
       "hwMacLBMemberRadioTraffic": hwMacLBMemberRadioTraffic,
       "hwMacLBMemberRowStatus": hwMacLBMemberRowStatus,
       "hwMacRadioPerformanceStatTable": hwMacRadioPerformanceStatTable,
       "hwMacRadioPerformanceStatEntry": hwMacRadioPerformanceStatEntry,
       "hwMacRadioRcvFrames": hwMacRadioRcvFrames,
       "hwMacRadioRcvBytes": hwMacRadioRcvBytes,
       "hwMacRadioSendFrames": hwMacRadioSendFrames,
       "hwMacRadioSendBytes": hwMacRadioSendBytes,
       "hwMacRadioSendRtsSuccess": hwMacRadioSendRtsSuccess,
       "hwMacRadioSendUnicast": hwMacRadioSendUnicast,
       "hwMacRadioSendBroadcast": hwMacRadioSendBroadcast,
       "hwMacRadioSendFailFrames": hwMacRadioSendFailFrames,
       "hwMacRadioRcvErrFrames": hwMacRadioRcvErrFrames,
       "hwMacRadioRcvPhyErrFrames": hwMacRadioRcvPhyErrFrames,
       "hwMacRadioRcvCrcErrFrames": hwMacRadioRcvCrcErrFrames,
       "hwMacRadioRcvMicErrFrames": hwMacRadioRcvMicErrFrames,
       "hwMacRadioRcvKeyDecryptErrFrames": hwMacRadioRcvKeyDecryptErrFrames,
       "hwMacRadioRetryFrames": hwMacRadioRetryFrames,
       "hwMacRadioPER": hwMacRadioPER,
       "hwMacRadioChUtilizationRate": hwMacRadioChUtilizationRate,
       "hwMacRadioPerformanceStatOperMode": hwMacRadioPerformanceStatOperMode,
       "hwMacRadioPEROfLastPeriod": hwMacRadioPEROfLastPeriod,
       "hwMacRadioRcvSignalStrength": hwMacRadioRcvSignalStrength,
       "hwMacRadioDownMacErrFrames": hwMacRadioDownMacErrFrames,
       "hwMacRadioRcvPower": hwMacRadioRcvPower,
       "hwMacRadioRcvUnicastFrames": hwMacRadioRcvUnicastFrames,
       "hwMacRadioRcvMngFrames": hwMacRadioRcvMngFrames,
       "hwMacRadioRcvCtrlFrames": hwMacRadioRcvCtrlFrames,
       "hwMacRadioRcvDataFrames": hwMacRadioRcvDataFrames,
       "hwMacRadioSendMngFrames": hwMacRadioSendMngFrames,
       "hwMacRadioSendCtrlFrames": hwMacRadioSendCtrlFrames,
       "hwMacRadioSendDataFrames": hwMacRadioSendDataFrames,
       "hwMacRadioStaMaxSignalStrength": hwMacRadioStaMaxSignalStrength,
       "hwMacRadioStaMinSignalStrength": hwMacRadioStaMinSignalStrength,
       "hwMacRadioStaAvgSignalStrength": hwMacRadioStaAvgSignalStrength,
       "hwMacRadioSendRate": hwMacRadioSendRate,
       "hwMacRadioRecvRate": hwMacRadioRecvRate,
       "hwMacRadioDropRate": hwMacRadioDropRate,
       "hwMacRadioAirPortDhcpFrames": hwMacRadioAirPortDhcpFrames,
       "hwMacRadioAirPortEapolFrames": hwMacRadioAirPortEapolFrames,
       "hwMacRadioAirPortPsPollFrames": hwMacRadioAirPortPsPollFrames,
       "hwMacRadioAssocRequestFrames": hwMacRadioAssocRequestFrames,
       "hwMacRadioAssocResponseFrames": hwMacRadioAssocResponseFrames,
       "hwMacRadioReassocRequestFrames": hwMacRadioReassocRequestFrames,
       "hwMacRadioReassocResponseFrames": hwMacRadioReassocResponseFrames,
       "hwMacRadioDisassocFrames": hwMacRadioDisassocFrames,
       "hwMacRadioDisauthFrames": hwMacRadioDisauthFrames,
       "hwMacRadioRcvFrames64Bits": hwMacRadioRcvFrames64Bits,
       "hwMacRadioRcvBytes64Bits": hwMacRadioRcvBytes64Bits,
       "hwMacRadioSendFrames64Bits": hwMacRadioSendFrames64Bits,
       "hwMacRadioSendBytes64Bits": hwMacRadioSendBytes64Bits,
       "hwMacRadioSendRtsSuccess64Bits": hwMacRadioSendRtsSuccess64Bits,
       "hwMacRadioSendUnicast64Bits": hwMacRadioSendUnicast64Bits,
       "hwMacRadioSendBroadcast64Bits": hwMacRadioSendBroadcast64Bits,
       "hwMacRadioSendFailFrames64Bits": hwMacRadioSendFailFrames64Bits,
       "hwMacRadioRcvErrFrames64Bits": hwMacRadioRcvErrFrames64Bits,
       "hwMacRadioRcvPhyErrFrames64Bits": hwMacRadioRcvPhyErrFrames64Bits,
       "hwMacRadioRcvCrcErrFrames64Bits": hwMacRadioRcvCrcErrFrames64Bits,
       "hwMacRadioRcvMicErrFrames64Bits": hwMacRadioRcvMicErrFrames64Bits,
       "hwMacRadioRcvKeyDecryptErrFrames64Bits": hwMacRadioRcvKeyDecryptErrFrames64Bits,
       "hwMacRadioRetryFrames64Bits": hwMacRadioRetryFrames64Bits,
       "hwMacRadioDownMacErrFrames64Bits": hwMacRadioDownMacErrFrames64Bits,
       "hwMacRadioNoise": hwMacRadioNoise,
       "hwMacRadioActualBandwidth": hwMacRadioActualBandwidth,
       "hwMacRadioFrames": hwMacRadioFrames,
       "hwMacRadioSendDropFrames64Bits": hwMacRadioSendDropFrames64Bits,
       "hwMacRadioRcvDropFrames64Bits": hwMacRadioRcvDropFrames64Bits,
       "hwMacRadioChannelFreeRate": hwMacRadioChannelFreeRate,
       "hwMacRadioTxRate": hwMacRadioTxRate,
       "hwMacRadioRxRate": hwMacRadioRxRate,
       "hwMacRadioChInterferenceRate": hwMacRadioChInterferenceRate,
       "hwMacRadioUnauthenticNeighborInfoTable": hwMacRadioUnauthenticNeighborInfoTable,
       "hwMacRadioUnauthenticNeighborInfoEntry": hwMacRadioUnauthenticNeighborInfoEntry,
       "hwMacUnauthenticRadioNeighborBSSID": hwMacUnauthenticRadioNeighborBSSID,
       "hwMacUnauthenticRadioNeighborRSSI": hwMacUnauthenticRadioNeighborRSSI,
       "hwMacunauthenticRadioNeighborChannel": hwMacunauthenticRadioNeighborChannel,
       "hwMacUnauthenticRadioNeighborSSID": hwMacUnauthenticRadioNeighborSSID,
       "hwRadioInfoTable": hwRadioInfoTable,
       "hwRadioInfoEntry": hwRadioInfoEntry,
       "hwRadioDecsption": hwRadioDecsption,
       "hwRadioPortType": hwRadioPortType,
       "hwRadioMaxMtu": hwRadioMaxMtu,
       "hwRadioBandwidth": hwRadioBandwidth,
       "hwRadioMac": hwRadioMac,
       "hwRadioAdminStatus": hwRadioAdminStatus,
       "hwRadioOperStatus": hwRadioOperStatus,
       "hwRadioLastChange": hwRadioLastChange,
       "hwRadioInfoUpDownTimes": hwRadioInfoUpDownTimes,
       "hwRadioAutoOffSwitch": hwRadioAutoOffSwitch,
       "hwRadioAutoOffStartTime": hwRadioAutoOffStartTime,
       "hwRadioAutoOffEndTime": hwRadioAutoOffEndTime,
       "hwMacRadioInfoTable": hwMacRadioInfoTable,
       "hwMacRadioInfoEntry": hwMacRadioInfoEntry,
       "hwMacRadioDecsption": hwMacRadioDecsption,
       "hwMacRadioPortType": hwMacRadioPortType,
       "hwMacRadioMaxMtu": hwMacRadioMaxMtu,
       "hwMacRadioBandwidth": hwMacRadioBandwidth,
       "hwMacRadioMac": hwMacRadioMac,
       "hwMacRadioAdminStatus": hwMacRadioAdminStatus,
       "hwMacRadioOperStatus": hwMacRadioOperStatus,
       "hwMacRadioLastChange": hwMacRadioLastChange,
       "hwMacRadioInfoUpDownTimes": hwMacRadioInfoUpDownTimes,
       "hwMacRadioAutoOffSwitch": hwMacRadioAutoOffSwitch,
       "hwMacRadioAutoOffStartTime": hwMacRadioAutoOffStartTime,
       "hwMacRadioAutoOffEndTime": hwMacRadioAutoOffEndTime,
       "hwRadioObjects": hwRadioObjects,
       "hwRadioCalibrateTable": hwRadioCalibrateTable,
       "hwRadioCalibrateMode": hwRadioCalibrateMode,
       "hwRadioCalibrateTime": hwRadioCalibrateTime,
       "hwRadioCalibrateManualStartup": hwRadioCalibrateManualStartup,
       "hwRadioCalibrateCycle": hwRadioCalibrateCycle,
       "hwRadioCalibratePolicy": hwRadioCalibratePolicy,
       "hwRadioCalibratesensitivity": hwRadioCalibratesensitivity,
       "hwRadioGlobalCalibrateChannel2G": hwRadioGlobalCalibrateChannel2G,
       "hwRadioGlobalCalibrateChannel5G": hwRadioGlobalCalibrateChannel5G,
       "hwRadioGlobalScanChannel2G": hwRadioGlobalScanChannel2G,
       "hwRadioGlobalScanChannel5G": hwRadioGlobalScanChannel5G,
       "hwRadioGlobalCalibrate5gBandWidth": hwRadioGlobalCalibrate5gBandWidth,
       "hwRadioCalibrateAutoStartTime": hwRadioCalibrateAutoStartTime,
       "hwConnectProfileTable": hwConnectProfileTable,
       "hwConnectProfileEntry": hwConnectProfileEntry,
       "hwConnectProfileName": hwConnectProfileName,
       "hwConnectSsid": hwConnectSsid,
       "hwConnectPeerMac": hwConnectPeerMac,
       "hwConnectPskPassPhase": hwConnectPskPassPhase,
       "hwConnectProfileActived": hwConnectProfileActived,
       "hwConnectProfileRowStatus": hwConnectProfileRowStatus,
       "hwRadioBasicSettingTable": hwRadioBasicSettingTable,
       "hwRadioBasicSettingEntry": hwRadioBasicSettingEntry,
       "hwApRadioID": hwApRadioID,
       "hwApRadioTxPower": hwApRadioTxPower,
       "hwApRadioRtsThreshold": hwApRadioRtsThreshold,
       "hwConnectStatusTable": hwConnectStatusTable,
       "hwConnectStatusEntry": hwConnectStatusEntry,
       "hwConnectStatusPeerMac": hwConnectStatusPeerMac,
       "hwConnectStatusSsid": hwConnectStatusSsid,
       "hwConnectStatus": hwConnectStatus,
       "hwConnectStatusSNR": hwConnectStatusSNR,
       "hwConnectStatusNoiseFloor": hwConnectStatusNoiseFloor,
       "hwConnectStatusChannel": hwConnectStatusChannel,
       "hwConnectStatusActualTxPower": hwConnectStatusActualTxPower,
       "hwConnectStatusBeaconInterval": hwConnectStatusBeaconInterval,
       "hwConnectStatusCurrentRate": hwConnectStatusCurrentRate,
       "hwConnectStatusTxBeamforming": hwConnectStatusTxBeamforming,
       "hwConnectStatusActualCountryCode": hwConnectStatusActualCountryCode,
       "hwConnectStatusDistance": hwConnectStatusDistance,
       "hwConnectStatusCurrentRateKbps": hwConnectStatusCurrentRateKbps,
       "hwConnectStatusHtMode": hwConnectStatusHtMode,
       "hwConnectStatusGIMode": hwConnectStatusGIMode,
       "hwConnectStatisticsTable": hwConnectStatisticsTable,
       "hwConnectStatisticsEntry": hwConnectStatisticsEntry,
       "hwConnectStatisticsPeerMac": hwConnectStatisticsPeerMac,
       "hwConnectRxOkUcastDataFrames": hwConnectRxOkUcastDataFrames,
       "hwConnectRxOkUcastDataBytes": hwConnectRxOkUcastDataBytes,
       "hwConnectTxOkUcastDataFrames": hwConnectTxOkUcastDataFrames,
       "hwConnectTxOkUcastDataBytes": hwConnectTxOkUcastDataBytes,
       "hwConnectRxThroughput": hwConnectRxThroughput,
       "hwConnectTxThroughput": hwConnectTxThroughput,
       "hwConnectRxErrFrames": hwConnectRxErrFrames,
       "hwConnectTxErrUcastDataFrames": hwConnectTxErrUcastDataFrames,
       "hwConnectUcastDataFrameTxRetryRatio": hwConnectUcastDataFrameTxRetryRatio,
       "hwConnectOnlineTime": hwConnectOnlineTime,
       "hwConnectStatisticsReset": hwConnectStatisticsReset,
       "hwConnectRateHistogramTable": hwConnectRateHistogramTable,
       "hwConnectRateHistogramEntry": hwConnectRateHistogramEntry,
       "hwConnectRateStatDirection": hwConnectRateStatDirection,
       "hwConnectRateStatRange": hwConnectRateStatRange,
       "hwConnectRateStatUcastDataFrames": hwConnectRateStatUcastDataFrames,
       "hwConnectAMPDUHistogramTable": hwConnectAMPDUHistogramTable,
       "hwConnectAMPDUHistogramEntry": hwConnectAMPDUHistogramEntry,
       "hwConnectAMPDUStatDirection": hwConnectAMPDUStatDirection,
       "hwConnectAMPDUStatRange": hwConnectAMPDUStatRange,
       "hwConnectAMPDUStatUcastDataFrames": hwConnectAMPDUStatUcastDataFrames,
       "hwConnectLenHistogramTable": hwConnectLenHistogramTable,
       "hwConnectLenHistogramEntry": hwConnectLenHistogramEntry,
       "hwConnectDataLenStatDirection": hwConnectDataLenStatDirection,
       "hwConnectDataLenStatLength": hwConnectDataLenStatLength,
       "hwConnectDataLenStatFrameCounts": hwConnectDataLenStatFrameCounts,
       "hwConnectMaxSnrTable": hwConnectMaxSnrTable,
       "hwConnectMaxSnrEntry": hwConnectMaxSnrEntry,
       "hwConnectMaxSnrPeerMAC": hwConnectMaxSnrPeerMAC,
       "hwConnectMaxSnrValue": hwConnectMaxSnrValue,
       "hwConnectMaxSnrNoiseFloor": hwConnectMaxSnrNoiseFloor,
       "hwConnectMaxSnrSSID": hwConnectMaxSnrSSID,
       "hwConnectMaxSnrTime": hwConnectMaxSnrTime,
       "hwRadioQueryPowerlevelTable": hwRadioQueryPowerlevelTable,
       "hwRadioQueryPowerlevelEntry": hwRadioQueryPowerlevelEntry,
       "hwRadioQueryPowerlevelChannel": hwRadioQueryPowerlevelChannel,
       "hwRadioQueryPowerlevelBandwidth": hwRadioQueryPowerlevelBandwidth,
       "hwRadioQueryPowerlevelMax": hwRadioQueryPowerlevelMax,
       "hwRadioConformance": hwRadioConformance,
       "hwRadioCompliances": hwRadioCompliances,
       "hwRadioCompliance": hwRadioCompliance,
       "hwRadioObjectGroups": hwRadioObjectGroups,
       "hwRadioProfileGroup": hwRadioProfileGroup,
       "hwRadioManageGroup": hwRadioManageGroup,
       "hwRadioCalibrateStatisicsGroup": hwRadioCalibrateStatisicsGroup,
       "hwRadioAuthNeighborInfGroup": hwRadioAuthNeighborInfGroup,
       "hwRadioLoadBalanceGroupGroup": hwRadioLoadBalanceGroupGroup,
       "hwRadioLoadBalanceGroupMemberGroup": hwRadioLoadBalanceGroupMemberGroup,
       "hwRadioUncontrolAPInfGroup": hwRadioUncontrolAPInfGroup,
       "hwRadioPerformanceStatGroup": hwRadioPerformanceStatGroup,
       "hwRadioUnauthenticNeighborInfoGroup": hwRadioUnauthenticNeighborInfoGroup,
       "hwRadioRegionCalibrateGroup": hwRadioRegionCalibrateGroup,
       "hwRadioGlobalGroup": hwRadioGlobalGroup,
       "hwRadioNotifyGroup": hwRadioNotifyGroup,
       "hwRadioNotifyObjectGroup": hwRadioNotifyObjectGroup,
       "hwRadioParaStatisticGroup": hwRadioParaStatisticGroup,
       "hwMacRadioManageGroup": hwMacRadioManageGroup,
       "hwMacRadioCalibrateStatisicsGroup": hwMacRadioCalibrateStatisicsGroup,
       "hwMacRadioAuthNeighborInfGroup": hwMacRadioAuthNeighborInfGroup,
       "hwMacRadioLoadBalanceGroupMemberGroup": hwMacRadioLoadBalanceGroupMemberGroup,
       "hwMacRadioPerformanceStatGroup": hwMacRadioPerformanceStatGroup,
       "hwMacRadioUnauthenticNeighborInfoGroup": hwMacRadioUnauthenticNeighborInfoGroup,
       "hwRadioInfoGroup": hwRadioInfoGroup,
       "hwMacRadioInfoGroup": hwMacRadioInfoGroup,
       "hwRadioCalibrateGroup": hwRadioCalibrateGroup,
       "hwConnectStatusGroup": hwConnectStatusGroup,
       "hwConnectStatisticsGruop": hwConnectStatisticsGruop,
       "hwConnectRateHistogramGruop": hwConnectRateHistogramGruop,
       "hwConnectAMPDUHistogramGruop": hwConnectAMPDUHistogramGruop,
       "hwConnectLenHistogramGruop": hwConnectLenHistogramGruop,
       "hwConnectMaxSnrGruop": hwConnectMaxSnrGruop}
)
