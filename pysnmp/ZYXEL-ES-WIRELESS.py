# SNMP MIB module (ZYXEL-ES-WIRELESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ES-WIRELESS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:41 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

esWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlanRadioTable_Object = MibTable
wlanRadioTable = _WlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1)
)
if mibBuilder.loadTexts:
    wlanRadioTable.setStatus("current")
_WlanRadioEntry_Object = MibTableRow
wlanRadioEntry = _WlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1)
)
wlanRadioEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanRadioIndex"),
)
if mibBuilder.loadTexts:
    wlanRadioEntry.setStatus("current")


class _WlanCurrentChannel_Type(Integer32):
    """Custom type wlanCurrentChannel based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-10_2457mhz", 10),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-11_2462mhz", 11),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-12_2467mhz", 12),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-13_2472mhz", 13),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("device_is_disable", 0))
    )


_WlanCurrentChannel_Type.__name__ = "Integer32"
_WlanCurrentChannel_Object = MibTableColumn
wlanCurrentChannel = _WlanCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 1),
    _WlanCurrentChannel_Type()
)
wlanCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentChannel.setStatus("current")
_WlanStationCount_Type = Unsigned32
_WlanStationCount_Object = MibTableColumn
wlanStationCount = _WlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 2),
    _WlanStationCount_Type()
)
wlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStationCount.setStatus("current")
_WlanSupportedChannel_Type = OctetString
_WlanSupportedChannel_Object = MibTableColumn
wlanSupportedChannel = _WlanSupportedChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 3),
    _WlanSupportedChannel_Type()
)
wlanSupportedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSupportedChannel.setStatus("current")


class _WlanMode_Type(Integer32):
    """Custom type wlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode_2_4G", 1),
          ("mode_5G", 2))
    )


_WlanMode_Type.__name__ = "Integer32"
_WlanMode_Object = MibTableColumn
wlanMode = _WlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 5),
    _WlanMode_Type()
)
wlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMode.setStatus("current")


class _WlanChannel_Type(Integer32):
    """Custom type wlanChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-10_2457mhz", 10),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-11_2462mhz", 11),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-12_2467mhz", 12),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-13_2472mhz", 13),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64))
    )


_WlanChannel_Type.__name__ = "Integer32"
_WlanChannel_Object = MibTableColumn
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 6),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")


class _WlanRadioIndex_Type(Integer32):
    """Custom type wlanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WlanRadioIndex_Type.__name__ = "Integer32"
_WlanRadioIndex_Object = MibTableColumn
wlanRadioIndex = _WlanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 7),
    _WlanRadioIndex_Type()
)
wlanRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadioIndex.setStatus("current")
_WlanStationTable_Object = MibTable
wlanStationTable = _WlanStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wlanStationTable.setStatus("current")
_WlanStationEntry_Object = MibTableRow
wlanStationEntry = _WlanStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1)
)
wlanStationEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "stationIndex"),
)
if mibBuilder.loadTexts:
    wlanStationEntry.setStatus("current")


class _StationIndex_Type(Integer32):
    """Custom type stationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StationIndex_Type.__name__ = "Integer32"
_StationIndex_Object = MibTableColumn
stationIndex = _StationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 1),
    _StationIndex_Type()
)
stationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stationIndex.setStatus("current")


class _StationMacAddress_Type(MacAddress):
    """Custom type stationMacAddress based on MacAddress"""
    defaultValue = OctetString("public")


_StationMacAddress_Object = MibTableColumn
stationMacAddress = _StationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 2),
    _StationMacAddress_Type()
)
stationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationMacAddress.setStatus("current")
_StationAssociatedTime_Type = DateAndTime
_StationAssociatedTime_Object = MibTableColumn
stationAssociatedTime = _StationAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 3),
    _StationAssociatedTime_Type()
)
stationAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationAssociatedTime.setStatus("current")
_StationSSID_Type = OctetString
_StationSSID_Object = MibTableColumn
stationSSID = _StationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 4),
    _StationSSID_Type()
)
stationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationSSID.setStatus("current")
_WlanStatisticsTable_Object = MibTable
wlanStatisticsTable = _WlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3)
)
if mibBuilder.loadTexts:
    wlanStatisticsTable.setStatus("current")
_WlanStatisticsEntry_Object = MibTableRow
wlanStatisticsEntry = _WlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1)
)
wlanStatisticsEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanStatisticsIndex"),
)
if mibBuilder.loadTexts:
    wlanStatisticsEntry.setStatus("current")
_Dot11FailedCount_Type = Counter64
_Dot11FailedCount_Object = MibTableColumn
dot11FailedCount = _Dot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 1),
    _Dot11FailedCount_Type()
)
dot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedCount.setStatus("current")
_Dot11RetryCount_Type = Counter64
_Dot11RetryCount_Object = MibTableColumn
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 2),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_Dot11ACKFailureCount_Type = Counter64
_Dot11ACKFailureCount_Object = MibTableColumn
dot11ACKFailureCount = _Dot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 3),
    _Dot11ACKFailureCount_Type()
)
dot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ACKFailureCount.setStatus("current")
_Dot11ReceivedFragmentCount_Type = Counter64
_Dot11ReceivedFragmentCount_Object = MibTableColumn
dot11ReceivedFragmentCount = _Dot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 4),
    _Dot11ReceivedFragmentCount_Type()
)
dot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFragmentCount.setStatus("current")
_Dot11TransmittedFrameCount_Type = Counter64
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 5),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("current")
_Dot11ReceivedPktCount_Type = Counter64
_Dot11ReceivedPktCount_Object = MibTableColumn
dot11ReceivedPktCount = _Dot11ReceivedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 6),
    _Dot11ReceivedPktCount_Type()
)
dot11ReceivedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedPktCount.setStatus("current")
_Dot11TransmittedPktCount_Type = Counter64
_Dot11TransmittedPktCount_Object = MibTableColumn
dot11TransmittedPktCount = _Dot11TransmittedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 7),
    _Dot11TransmittedPktCount_Type()
)
dot11TransmittedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedPktCount.setStatus("current")


class _WlanStatisticsIndex_Type(Integer32):
    """Custom type wlanStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WlanStatisticsIndex_Type.__name__ = "Integer32"
_WlanStatisticsIndex_Object = MibTableColumn
wlanStatisticsIndex = _WlanStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 8),
    _WlanStatisticsIndex_Type()
)
wlanStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanStatisticsIndex.setStatus("current")
_WlanTraps_ObjectIdentity = ObjectIdentity
wlanTraps = _WlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4)
)
if mibBuilder.loadTexts:
    wlanTraps.setStatus("current")
_TrapsControl_ObjectIdentity = ObjectIdentity
trapsControl = _TrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    trapsControl.setStatus("current")


class _WlanTrapsControl_Type(Integer32):
    """Custom type wlanTrapsControl based on Integer32"""
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


_WlanTrapsControl_Type.__name__ = "Integer32"
_WlanTrapsControl_Object = MibScalar
wlanTrapsControl = _WlanTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1, 1),
    _WlanTrapsControl_Type()
)
wlanTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanTrapsControl.setStatus("current")
_TrapsFormat_ObjectIdentity = ObjectIdentity
trapsFormat = _TrapsFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    trapsFormat.setStatus("current")
_TrapGenericMessage_Type = DisplayString
_TrapGenericMessage_Object = MibScalar
trapGenericMessage = _TrapGenericMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 1),
    _TrapGenericMessage_Type()
)
trapGenericMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapGenericMessage.setStatus("current")
_TrapMACAddress_Type = MacAddress
_TrapMACAddress_Object = MibScalar
trapMACAddress = _TrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 2),
    _TrapMACAddress_Type()
)
trapMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMACAddress.setStatus("current")
_TrapWlanSSID_Type = DisplayString
_TrapWlanSSID_Object = MibScalar
trapWlanSSID = _TrapWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 3),
    _TrapWlanSSID_Type()
)
trapWlanSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapWlanSSID.setStatus("current")
_TrapsItems_ObjectIdentity = ObjectIdentity
trapsItems = _TrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    trapsItems.setStatus("current")
_WlanTotalStationCount_Type = Integer32
_WlanTotalStationCount_Object = MibScalar
wlanTotalStationCount = _WlanTotalStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 15),
    _WlanTotalStationCount_Type()
)
wlanTotalStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanTotalStationCount.setStatus("current")

# Managed Objects groups


# Notification objects

wlanStaAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wlanStaAssociation.setStatus(
        "current"
    )

wlanStaDisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 2)
)
if mibBuilder.loadTexts:
    wlanStaDisassociation.setStatus(
        "current"
    )

wlanStaAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 3)
)
if mibBuilder.loadTexts:
    wlanStaAuthFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-WIRELESS",
    **{"esWireless": esWireless,
       "wlanRadioTable": wlanRadioTable,
       "wlanRadioEntry": wlanRadioEntry,
       "wlanCurrentChannel": wlanCurrentChannel,
       "wlanStationCount": wlanStationCount,
       "wlanSupportedChannel": wlanSupportedChannel,
       "wlanMode": wlanMode,
       "wlanChannel": wlanChannel,
       "wlanRadioIndex": wlanRadioIndex,
       "wlanStationTable": wlanStationTable,
       "wlanStationEntry": wlanStationEntry,
       "stationIndex": stationIndex,
       "stationMacAddress": stationMacAddress,
       "stationAssociatedTime": stationAssociatedTime,
       "stationSSID": stationSSID,
       "wlanStatisticsTable": wlanStatisticsTable,
       "wlanStatisticsEntry": wlanStatisticsEntry,
       "dot11FailedCount": dot11FailedCount,
       "dot11RetryCount": dot11RetryCount,
       "dot11ACKFailureCount": dot11ACKFailureCount,
       "dot11ReceivedFragmentCount": dot11ReceivedFragmentCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11ReceivedPktCount": dot11ReceivedPktCount,
       "dot11TransmittedPktCount": dot11TransmittedPktCount,
       "wlanStatisticsIndex": wlanStatisticsIndex,
       "wlanTraps": wlanTraps,
       "trapsControl": trapsControl,
       "wlanTrapsControl": wlanTrapsControl,
       "trapsFormat": trapsFormat,
       "trapGenericMessage": trapGenericMessage,
       "trapMACAddress": trapMACAddress,
       "trapWlanSSID": trapWlanSSID,
       "trapsItems": trapsItems,
       "wlanStaAssociation": wlanStaAssociation,
       "wlanStaDisassociation": wlanStaDisassociation,
       "wlanStaAuthFail": wlanStaAuthFail,
       "wlanTotalStationCount": wlanTotalStationCount}
)
