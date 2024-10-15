# SNMP MIB module (ZHONE-PHY-WTN-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-PHY-WTN-RADIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:40 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(SkyZhoneRadioChannelNumber,
 SkyZhoneScientificNotation) = mibBuilder.importSymbols(
    "ZHONE-RADIO-TC-MIB",
    "SkyZhoneRadioChannelNumber",
    "SkyZhoneScientificNotation")

(zhoneModules,
 zhoneRadio) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneRadio")

(ZhoneAdminString,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString")


# MODULE-IDENTITY

zhonePhyWtnRadio = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 106)
)
zhonePhyWtnRadio.setRevisions(
        ("2001-07-11 13:00",
         "2001-06-07 14:14",
         "2001-05-18 10:02",
         "2000-11-24 08:18",
         "2000-11-21 15:35",
         "2000-11-03 09:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WtnConfigTable_Object = MibTable
wtnConfigTable = _WtnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1)
)
if mibBuilder.loadTexts:
    wtnConfigTable.setStatus("current")
_WtnConfigEntry_Object = MibTableRow
wtnConfigEntry = _WtnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1)
)
wtnConfigEntry.setIndexNames(
    (0, "ZHONE-PHY-WTN-RADIO-MIB", "wtnRadioIfIndex"),
)
if mibBuilder.loadTexts:
    wtnConfigEntry.setStatus("current")
_WtnRadioIfIndex_Type = InterfaceIndex
_WtnRadioIfIndex_Object = MibTableColumn
wtnRadioIfIndex = _WtnRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 1),
    _WtnRadioIfIndex_Type()
)
wtnRadioIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wtnRadioIfIndex.setStatus("current")
_WtnActiveChannelNumber_Type = SkyZhoneRadioChannelNumber
_WtnActiveChannelNumber_Object = MibTableColumn
wtnActiveChannelNumber = _WtnActiveChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 2),
    _WtnActiveChannelNumber_Type()
)
wtnActiveChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnActiveChannelNumber.setStatus("current")
_WtnActiveTransmitFrequency_Type = SkyZhoneScientificNotation
_WtnActiveTransmitFrequency_Object = MibTableColumn
wtnActiveTransmitFrequency = _WtnActiveTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 3),
    _WtnActiveTransmitFrequency_Type()
)
wtnActiveTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnActiveTransmitFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wtnActiveTransmitFrequency.setUnits("Hz")
_WtnStandbyChannelNumber_Type = SkyZhoneRadioChannelNumber
_WtnStandbyChannelNumber_Object = MibTableColumn
wtnStandbyChannelNumber = _WtnStandbyChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 4),
    _WtnStandbyChannelNumber_Type()
)
wtnStandbyChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnStandbyChannelNumber.setStatus("current")
_WtnStandbyTransmitFrequency_Type = SkyZhoneScientificNotation
_WtnStandbyTransmitFrequency_Object = MibTableColumn
wtnStandbyTransmitFrequency = _WtnStandbyTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 5),
    _WtnStandbyTransmitFrequency_Type()
)
wtnStandbyTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnStandbyTransmitFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wtnStandbyTransmitFrequency.setUnits("Hz")
_WtnAutoChannelSwitchEnable_Type = TruthValue
_WtnAutoChannelSwitchEnable_Object = MibTableColumn
wtnAutoChannelSwitchEnable = _WtnAutoChannelSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 6),
    _WtnAutoChannelSwitchEnable_Type()
)
wtnAutoChannelSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnAutoChannelSwitchEnable.setStatus("current")


class _WtnChannelSeparation_Type(Integer32):
    """Custom type wtnChannelSeparation based on Integer32"""
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
        *(("na", 0),
          ("s1008MHz", 3),
          ("s1200MHz", 2),
          ("s1232MHz", 1))
    )


_WtnChannelSeparation_Type.__name__ = "Integer32"
_WtnChannelSeparation_Object = MibTableColumn
wtnChannelSeparation = _WtnChannelSeparation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 7),
    _WtnChannelSeparation_Type()
)
wtnChannelSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnChannelSeparation.setStatus("current")
_WtnRadioAmplifiersEnable_Type = TruthValue
_WtnRadioAmplifiersEnable_Object = MibTableColumn
wtnRadioAmplifiersEnable = _WtnRadioAmplifiersEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 8),
    _WtnRadioAmplifiersEnable_Type()
)
wtnRadioAmplifiersEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnRadioAmplifiersEnable.setStatus("current")
_WtnRxBERThresh_Type = SkyZhoneScientificNotation
_WtnRxBERThresh_Object = MibTableColumn
wtnRxBERThresh = _WtnRxBERThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 9),
    _WtnRxBERThresh_Type()
)
wtnRxBERThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnRxBERThresh.setStatus("current")
_WtnRxBERHysteresisWindow_Type = SkyZhoneScientificNotation
_WtnRxBERHysteresisWindow_Object = MibTableColumn
wtnRxBERHysteresisWindow = _WtnRxBERHysteresisWindow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 10),
    _WtnRxBERHysteresisWindow_Type()
)
wtnRxBERHysteresisWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnRxBERHysteresisWindow.setStatus("current")


class _WtnAntennaSize_Type(Integer32):
    """Custom type wtnAntennaSize based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fourFeet", 4),
          ("oneFoot", 1),
          ("sixFeet", 6),
          ("twoFeet", 2))
    )


_WtnAntennaSize_Type.__name__ = "Integer32"
_WtnAntennaSize_Object = MibTableColumn
wtnAntennaSize = _WtnAntennaSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 11),
    _WtnAntennaSize_Type()
)
wtnAntennaSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnAntennaSize.setStatus("current")
if mibBuilder.loadTexts:
    wtnAntennaSize.setUnits("feet")


class _WtnIduOduCableLength_Type(Integer32):
    """Custom type wtnIduOduCableLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WtnIduOduCableLength_Type.__name__ = "Integer32"
_WtnIduOduCableLength_Object = MibTableColumn
wtnIduOduCableLength = _WtnIduOduCableLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 12),
    _WtnIduOduCableLength_Type()
)
wtnIduOduCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnIduOduCableLength.setStatus("current")
if mibBuilder.loadTexts:
    wtnIduOduCableLength.setUnits("feet")


class _WtnRssiThresh_Type(Integer32):
    """Custom type wtnRssiThresh based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
    )


_WtnRssiThresh_Type.__name__ = "Integer32"
_WtnRssiThresh_Object = MibTableColumn
wtnRssiThresh = _WtnRssiThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 13),
    _WtnRssiThresh_Type()
)
wtnRssiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnRssiThresh.setStatus("current")
if mibBuilder.loadTexts:
    wtnRssiThresh.setUnits("dB")


class _WtnRssiHysteresisWindow_Type(Integer32):
    """Custom type wtnRssiHysteresisWindow based on Integer32"""
    defaultValue = 10


_WtnRssiHysteresisWindow_Object = MibTableColumn
wtnRssiHysteresisWindow = _WtnRssiHysteresisWindow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 14),
    _WtnRssiHysteresisWindow_Type()
)
wtnRssiHysteresisWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnRssiHysteresisWindow.setStatus("current")
if mibBuilder.loadTexts:
    wtnRssiHysteresisWindow.setUnits("dB")
_WtnTrapsEnable_Type = TruthValue
_WtnTrapsEnable_Object = MibTableColumn
wtnTrapsEnable = _WtnTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 15),
    _WtnTrapsEnable_Type()
)
wtnTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnTrapsEnable.setStatus("current")


class _WtnOduLoopback_Type(Integer32):
    """Custom type wtnOduLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopbackOff", 2),
          ("loopbackOn", 1))
    )


_WtnOduLoopback_Type.__name__ = "Integer32"
_WtnOduLoopback_Object = MibTableColumn
wtnOduLoopback = _WtnOduLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 16),
    _WtnOduLoopback_Type()
)
wtnOduLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnOduLoopback.setStatus("current")
_WtnOduIdentifier_Type = SnmpAdminString
_WtnOduIdentifier_Object = MibTableColumn
wtnOduIdentifier = _WtnOduIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 17),
    _WtnOduIdentifier_Type()
)
wtnOduIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnOduIdentifier.setStatus("current")


class _WtnTxLevel_Type(Integer32):
    """Custom type wtnTxLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_WtnTxLevel_Type.__name__ = "Integer32"
_WtnTxLevel_Object = MibTableColumn
wtnTxLevel = _WtnTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 1, 1, 18),
    _WtnTxLevel_Type()
)
wtnTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnTxLevel.setStatus("current")
if mibBuilder.loadTexts:
    wtnTxLevel.setUnits("dB")
_WtnStatusTable_Object = MibTable
wtnStatusTable = _WtnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2)
)
if mibBuilder.loadTexts:
    wtnStatusTable.setStatus("current")
_WtnStatusEntry_Object = MibTableRow
wtnStatusEntry = _WtnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1)
)
if mibBuilder.loadTexts:
    wtnStatusEntry.setStatus("current")


class _WtnCriticalAlarmStatus_Type(Bits):
    """Custom type wtnCriticalAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("iduEquipFail", 8),
          ("iduOOL", 1),
          ("iduOduLinkFail", 10),
          ("mcChannelFail", 11),
          ("oduEquipFail", 9),
          ("oduTempAlert", 2),
          ("rssiDeviation", 0),
          ("rxBerAlarm", 3),
          ("rxEbnoAlarm", 4),
          ("serviceAffected", 15),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused5", 5),
          ("unused6", 6),
          ("unused7", 7))
    )

_WtnCriticalAlarmStatus_Type.__name__ = "Bits"
_WtnCriticalAlarmStatus_Object = MibTableColumn
wtnCriticalAlarmStatus = _WtnCriticalAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 1),
    _WtnCriticalAlarmStatus_Type()
)
wtnCriticalAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnCriticalAlarmStatus.setStatus("current")
_WtnCriticalAlarmStatusLastChange_Type = TimeStamp
_WtnCriticalAlarmStatusLastChange_Object = MibTableColumn
wtnCriticalAlarmStatusLastChange = _WtnCriticalAlarmStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 2),
    _WtnCriticalAlarmStatusLastChange_Type()
)
wtnCriticalAlarmStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnCriticalAlarmStatusLastChange.setStatus("current")


class _WtnMinorAlarmStatus_Type(Bits):
    """Custom type wtnMinorAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("iduEquipFail", 8),
          ("iduOOL", 1),
          ("iduOduLinkFail", 10),
          ("mcChannelFail", 11),
          ("oduEquipFail", 9),
          ("oduTempAlert", 2),
          ("rssiDeviation", 0),
          ("rxBerAlarm", 3),
          ("rxEbnoAlarm", 4),
          ("serviceAffected", 15),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused5", 5),
          ("unused6", 6),
          ("unused7", 7))
    )

_WtnMinorAlarmStatus_Type.__name__ = "Bits"
_WtnMinorAlarmStatus_Object = MibTableColumn
wtnMinorAlarmStatus = _WtnMinorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 3),
    _WtnMinorAlarmStatus_Type()
)
wtnMinorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnMinorAlarmStatus.setStatus("current")
_WtnMinorAlarmStatusLastChange_Type = TimeStamp
_WtnMinorAlarmStatusLastChange_Object = MibTableColumn
wtnMinorAlarmStatusLastChange = _WtnMinorAlarmStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 4),
    _WtnMinorAlarmStatusLastChange_Type()
)
wtnMinorAlarmStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnMinorAlarmStatusLastChange.setStatus("current")
_WtnOduTemperature_Type = Integer32
_WtnOduTemperature_Object = MibTableColumn
wtnOduTemperature = _WtnOduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 5),
    _WtnOduTemperature_Type()
)
wtnOduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnOduTemperature.setStatus("current")
_WtnReceiveFrequency_Type = SkyZhoneScientificNotation
_WtnReceiveFrequency_Object = MibTableColumn
wtnReceiveFrequency = _WtnReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 2, 1, 6),
    _WtnReceiveFrequency_Type()
)
wtnReceiveFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnReceiveFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wtnReceiveFrequency.setUnits("Hz")
_WtnInfoTable_Object = MibTable
wtnInfoTable = _WtnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 3)
)
if mibBuilder.loadTexts:
    wtnInfoTable.setStatus("current")
_WtnInfoEntry_Object = MibTableRow
wtnInfoEntry = _WtnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 3, 1)
)
if mibBuilder.loadTexts:
    wtnInfoEntry.setStatus("current")
_WtnOduSerialNumber_Type = ZhoneAdminString
_WtnOduSerialNumber_Object = MibTableColumn
wtnOduSerialNumber = _WtnOduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 3, 1, 1),
    _WtnOduSerialNumber_Type()
)
wtnOduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnOduSerialNumber.setStatus("current")
_WtnOduMfgCLEICode_Type = ZhoneAdminString
_WtnOduMfgCLEICode_Object = MibTableColumn
wtnOduMfgCLEICode = _WtnOduMfgCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 3, 1, 2),
    _WtnOduMfgCLEICode_Type()
)
wtnOduMfgCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnOduMfgCLEICode.setStatus("current")
_WtnSnapshotTable_Object = MibTable
wtnSnapshotTable = _WtnSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4)
)
if mibBuilder.loadTexts:
    wtnSnapshotTable.setStatus("current")
_WtnSnapshotEntry_Object = MibTableRow
wtnSnapshotEntry = _WtnSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4, 1)
)
if mibBuilder.loadTexts:
    wtnSnapshotEntry.setStatus("current")


class _WtnRSSI_Type(Integer32):
    """Custom type wtnRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_WtnRSSI_Type.__name__ = "Integer32"
_WtnRSSI_Object = MibTableColumn
wtnRSSI = _WtnRSSI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4, 1, 1),
    _WtnRSSI_Type()
)
wtnRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnRSSI.setStatus("current")
if mibBuilder.loadTexts:
    wtnRSSI.setUnits("dBm")


class _WtnTSSI_Type(Integer32):
    """Custom type wtnTSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_WtnTSSI_Type.__name__ = "Integer32"
_WtnTSSI_Object = MibTableColumn
wtnTSSI = _WtnTSSI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4, 1, 2),
    _WtnTSSI_Type()
)
wtnTSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnTSSI.setStatus("current")
if mibBuilder.loadTexts:
    wtnTSSI.setUnits("dBm")
_WtnRxBerFloat_Type = SkyZhoneScientificNotation
_WtnRxBerFloat_Object = MibTableColumn
wtnRxBerFloat = _WtnRxBerFloat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4, 1, 3),
    _WtnRxBerFloat_Type()
)
wtnRxBerFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnRxBerFloat.setStatus("current")
_WtnRcvEbNoFloat_Type = SkyZhoneScientificNotation
_WtnRcvEbNoFloat_Object = MibTableColumn
wtnRcvEbNoFloat = _WtnRcvEbNoFloat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 4, 1, 4),
    _WtnRcvEbNoFloat_Type()
)
wtnRcvEbNoFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnRcvEbNoFloat.setStatus("current")
_WtnTrapData_ObjectIdentity = ObjectIdentity
wtnTrapData = _WtnTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5)
)
_WtnTraps_ObjectIdentity = ObjectIdentity
wtnTraps = _WtnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0)
)


class _WtnTrapCondition_Type(Integer32):
    """Custom type wtnTrapCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conditionCleared", 2),
          ("conditionPresent", 1))
    )


_WtnTrapCondition_Type.__name__ = "Integer32"
_WtnTrapCondition_Object = MibScalar
wtnTrapCondition = _WtnTrapCondition_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 1),
    _WtnTrapCondition_Type()
)
wtnTrapCondition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wtnTrapCondition.setStatus("current")


class _WtnServiceAffected_Type(Integer32):
    """Custom type wtnServiceAffected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceAffected", 1),
          ("serviceNotAffected", 2))
    )


_WtnServiceAffected_Type.__name__ = "Integer32"
_WtnServiceAffected_Object = MibScalar
wtnServiceAffected = _WtnServiceAffected_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 2),
    _WtnServiceAffected_Type()
)
wtnServiceAffected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wtnServiceAffected.setStatus("current")
_RadioTotalTable_Object = MibTable
radioTotalTable = _RadioTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 6)
)
if mibBuilder.loadTexts:
    radioTotalTable.setStatus("current")
_RadioTotalEntry_Object = MibTableRow
radioTotalEntry = _RadioTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 6, 1)
)
if mibBuilder.loadTexts:
    radioTotalEntry.setStatus("current")
_RadioTotalES_Type = Gauge32
_RadioTotalES_Object = MibTableColumn
radioTotalES = _RadioTotalES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 6, 1, 1),
    _RadioTotalES_Type()
)
radioTotalES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTotalES.setStatus("current")
_RadioTotalSES_Type = Gauge32
_RadioTotalSES_Object = MibTableColumn
radioTotalSES = _RadioTotalSES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 6, 1, 2),
    _RadioTotalSES_Type()
)
radioTotalSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTotalSES.setStatus("current")
_RadioTotalUAS_Type = Gauge32
_RadioTotalUAS_Object = MibTableColumn
radioTotalUAS = _RadioTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 6, 1, 3),
    _RadioTotalUAS_Type()
)
radioTotalUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTotalUAS.setStatus("current")
wtnConfigEntry.registerAugmentions(
    ("ZHONE-PHY-WTN-RADIO-MIB",
     "wtnStatusEntry")
)
wtnStatusEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions(
    ("ZHONE-PHY-WTN-RADIO-MIB",
     "wtnInfoEntry")
)
wtnInfoEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions(
    ("ZHONE-PHY-WTN-RADIO-MIB",
     "wtnSnapshotEntry")
)
wtnSnapshotEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions(
    ("ZHONE-PHY-WTN-RADIO-MIB",
     "radioTotalEntry")
)
radioTotalEntry.setIndexNames(*wtnConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

wtnIduEquipFailCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 1)
)
wtnIduEquipFailCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduEquipFailCritical.setStatus(
        "current"
    )

wtnIduEquipFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 2)
)
wtnIduEquipFail.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduEquipFail.setStatus(
        "current"
    )

wtnIduOduLinkFailCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 3)
)
wtnIduOduLinkFailCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduOduLinkFailCritical.setStatus(
        "current"
    )

wtnIduOduLinkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 4)
)
wtnIduOduLinkFail.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduOduLinkFail.setStatus(
        "current"
    )

wtnIduOutOfLockCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 5)
)
wtnIduOutOfLockCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduOutOfLockCritical.setStatus(
        "current"
    )

wtnIduOutOfLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 6)
)
wtnIduOutOfLock.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnIduOutOfLock.setStatus(
        "current"
    )

wtnMcChannelFailCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 7)
)
wtnMcChannelFailCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnMcChannelFailCritical.setStatus(
        "current"
    )

wtnMcChannelFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 8)
)
wtnMcChannelFail.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnMcChannelFail.setStatus(
        "current"
    )

wtnOduEquipFailCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 9)
)
wtnOduEquipFailCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnOduEquipFailCritical.setStatus(
        "current"
    )

wtnOduEquipFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 10)
)
wtnOduEquipFail.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnOduEquipFail.setStatus(
        "current"
    )

wtnOduTempAlertCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 11)
)
wtnOduTempAlertCritical.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnOduTempAlertCritical.setStatus(
        "current"
    )

wtnOduTempAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 12)
)
wtnOduTempAlert.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnOduTempAlert.setStatus(
        "current"
    )

wtnRSSIDeviation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 13)
)
wtnRSSIDeviation.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnRSSIDeviation.setStatus(
        "current"
    )

wtnBerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 14)
)
wtnBerAlarm.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnBerAlarm.setStatus(
        "current"
    )

wtnEbNoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 8, 5, 0, 15)
)
wtnEbNoAlarm.setObjects(
      *(("ZHONE-PHY-WTN-RADIO-MIB", "wtnTrapCondition"),
        ("ZHONE-PHY-WTN-RADIO-MIB", "wtnServiceAffected"))
)
if mibBuilder.loadTexts:
    wtnEbNoAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-PHY-WTN-RADIO-MIB",
    **{"wtnConfigTable": wtnConfigTable,
       "wtnConfigEntry": wtnConfigEntry,
       "wtnRadioIfIndex": wtnRadioIfIndex,
       "wtnActiveChannelNumber": wtnActiveChannelNumber,
       "wtnActiveTransmitFrequency": wtnActiveTransmitFrequency,
       "wtnStandbyChannelNumber": wtnStandbyChannelNumber,
       "wtnStandbyTransmitFrequency": wtnStandbyTransmitFrequency,
       "wtnAutoChannelSwitchEnable": wtnAutoChannelSwitchEnable,
       "wtnChannelSeparation": wtnChannelSeparation,
       "wtnRadioAmplifiersEnable": wtnRadioAmplifiersEnable,
       "wtnRxBERThresh": wtnRxBERThresh,
       "wtnRxBERHysteresisWindow": wtnRxBERHysteresisWindow,
       "wtnAntennaSize": wtnAntennaSize,
       "wtnIduOduCableLength": wtnIduOduCableLength,
       "wtnRssiThresh": wtnRssiThresh,
       "wtnRssiHysteresisWindow": wtnRssiHysteresisWindow,
       "wtnTrapsEnable": wtnTrapsEnable,
       "wtnOduLoopback": wtnOduLoopback,
       "wtnOduIdentifier": wtnOduIdentifier,
       "wtnTxLevel": wtnTxLevel,
       "wtnStatusTable": wtnStatusTable,
       "wtnStatusEntry": wtnStatusEntry,
       "wtnCriticalAlarmStatus": wtnCriticalAlarmStatus,
       "wtnCriticalAlarmStatusLastChange": wtnCriticalAlarmStatusLastChange,
       "wtnMinorAlarmStatus": wtnMinorAlarmStatus,
       "wtnMinorAlarmStatusLastChange": wtnMinorAlarmStatusLastChange,
       "wtnOduTemperature": wtnOduTemperature,
       "wtnReceiveFrequency": wtnReceiveFrequency,
       "wtnInfoTable": wtnInfoTable,
       "wtnInfoEntry": wtnInfoEntry,
       "wtnOduSerialNumber": wtnOduSerialNumber,
       "wtnOduMfgCLEICode": wtnOduMfgCLEICode,
       "wtnSnapshotTable": wtnSnapshotTable,
       "wtnSnapshotEntry": wtnSnapshotEntry,
       "wtnRSSI": wtnRSSI,
       "wtnTSSI": wtnTSSI,
       "wtnRxBerFloat": wtnRxBerFloat,
       "wtnRcvEbNoFloat": wtnRcvEbNoFloat,
       "wtnTrapData": wtnTrapData,
       "wtnTraps": wtnTraps,
       "wtnIduEquipFailCritical": wtnIduEquipFailCritical,
       "wtnIduEquipFail": wtnIduEquipFail,
       "wtnIduOduLinkFailCritical": wtnIduOduLinkFailCritical,
       "wtnIduOduLinkFail": wtnIduOduLinkFail,
       "wtnIduOutOfLockCritical": wtnIduOutOfLockCritical,
       "wtnIduOutOfLock": wtnIduOutOfLock,
       "wtnMcChannelFailCritical": wtnMcChannelFailCritical,
       "wtnMcChannelFail": wtnMcChannelFail,
       "wtnOduEquipFailCritical": wtnOduEquipFailCritical,
       "wtnOduEquipFail": wtnOduEquipFail,
       "wtnOduTempAlertCritical": wtnOduTempAlertCritical,
       "wtnOduTempAlert": wtnOduTempAlert,
       "wtnRSSIDeviation": wtnRSSIDeviation,
       "wtnBerAlarm": wtnBerAlarm,
       "wtnEbNoAlarm": wtnEbNoAlarm,
       "wtnTrapCondition": wtnTrapCondition,
       "wtnServiceAffected": wtnServiceAffected,
       "radioTotalTable": radioTotalTable,
       "radioTotalEntry": radioTotalEntry,
       "radioTotalES": radioTotalES,
       "radioTotalSES": radioTotalSES,
       "radioTotalUAS": radioTotalUAS,
       "zhonePhyWtnRadio": zhonePhyWtnRadio}
)
