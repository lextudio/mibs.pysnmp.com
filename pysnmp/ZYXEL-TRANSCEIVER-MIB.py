# SNMP MIB module (ZYXEL-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-TRANSCEIVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:58 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelTransceiverStatus_ObjectIdentity = ObjectIdentity
zyxelTransceiverStatus = _ZyxelTransceiverStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1)
)
_ZyxelTransceiverSerialTable_Object = MibTable
zyxelTransceiverSerialTable = _ZyxelTransceiverSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelTransceiverSerialTable.setStatus("current")
_ZyxelTransceiverSerialEntry_Object = MibTableRow
zyxelTransceiverSerialEntry = _ZyxelTransceiverSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1)
)
zyxelTransceiverSerialEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelTransceiverSerialEntry.setStatus("current")


class _ZyTransceiverSerialModuleType_Type(Integer32):
    """Custom type zyTransceiverSerialModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonoperational", 3),
          ("okWithDdm", 1),
          ("okWithoutDdm", 2))
    )


_ZyTransceiverSerialModuleType_Type.__name__ = "Integer32"
_ZyTransceiverSerialModuleType_Object = MibTableColumn
zyTransceiverSerialModuleType = _ZyTransceiverSerialModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 1),
    _ZyTransceiverSerialModuleType_Type()
)
zyTransceiverSerialModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialModuleType.setStatus("current")
_ZyTransceiverSerialVendor_Type = DisplayString
_ZyTransceiverSerialVendor_Object = MibTableColumn
zyTransceiverSerialVendor = _ZyTransceiverSerialVendor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 2),
    _ZyTransceiverSerialVendor_Type()
)
zyTransceiverSerialVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialVendor.setStatus("current")
_ZyTransceiverSerialPartNumber_Type = DisplayString
_ZyTransceiverSerialPartNumber_Object = MibTableColumn
zyTransceiverSerialPartNumber = _ZyTransceiverSerialPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 3),
    _ZyTransceiverSerialPartNumber_Type()
)
zyTransceiverSerialPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialPartNumber.setStatus("current")
_ZyTransceiverSerialSerialNumber_Type = DisplayString
_ZyTransceiverSerialSerialNumber_Object = MibTableColumn
zyTransceiverSerialSerialNumber = _ZyTransceiverSerialSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 4),
    _ZyTransceiverSerialSerialNumber_Type()
)
zyTransceiverSerialSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialSerialNumber.setStatus("current")
_ZyTransceiverSerialRevision_Type = DisplayString
_ZyTransceiverSerialRevision_Object = MibTableColumn
zyTransceiverSerialRevision = _ZyTransceiverSerialRevision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 5),
    _ZyTransceiverSerialRevision_Type()
)
zyTransceiverSerialRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialRevision.setStatus("current")
_ZyTransceiverSerialDateCode_Type = DisplayString
_ZyTransceiverSerialDateCode_Object = MibTableColumn
zyTransceiverSerialDateCode = _ZyTransceiverSerialDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 6),
    _ZyTransceiverSerialDateCode_Type()
)
zyTransceiverSerialDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialDateCode.setStatus("current")
_ZyTransceiverSerialTransceiver_Type = DisplayString
_ZyTransceiverSerialTransceiver_Object = MibTableColumn
zyTransceiverSerialTransceiver = _ZyTransceiverSerialTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 1, 1, 7),
    _ZyTransceiverSerialTransceiver_Type()
)
zyTransceiverSerialTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverSerialTransceiver.setStatus("current")
_ZyxelTransceiverDdmiTable_Object = MibTable
zyxelTransceiverDdmiTable = _ZyxelTransceiverDdmiTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelTransceiverDdmiTable.setStatus("current")
_ZyxelTransceiverDdmiEntry_Object = MibTableRow
zyxelTransceiverDdmiEntry = _ZyxelTransceiverDdmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1)
)
zyxelTransceiverDdmiEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-TRANSCEIVER-MIB", "zyTransceiverDdmiType"),
)
if mibBuilder.loadTexts:
    zyxelTransceiverDdmiEntry.setStatus("current")
_ZyTransceiverDdmiType_Type = Integer32
_ZyTransceiverDdmiType_Object = MibTableColumn
zyTransceiverDdmiType = _ZyTransceiverDdmiType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 1),
    _ZyTransceiverDdmiType_Type()
)
zyTransceiverDdmiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiType.setStatus("current")
_ZyTransceiverDdmiAlarmMax_Type = Integer32
_ZyTransceiverDdmiAlarmMax_Object = MibTableColumn
zyTransceiverDdmiAlarmMax = _ZyTransceiverDdmiAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 2),
    _ZyTransceiverDdmiAlarmMax_Type()
)
zyTransceiverDdmiAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiAlarmMax.setStatus("current")
_ZyTransceiverDdmiAlarmMin_Type = Integer32
_ZyTransceiverDdmiAlarmMin_Object = MibTableColumn
zyTransceiverDdmiAlarmMin = _ZyTransceiverDdmiAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 3),
    _ZyTransceiverDdmiAlarmMin_Type()
)
zyTransceiverDdmiAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiAlarmMin.setStatus("current")
_ZyTransceiverDdmiWarnMax_Type = Integer32
_ZyTransceiverDdmiWarnMax_Object = MibTableColumn
zyTransceiverDdmiWarnMax = _ZyTransceiverDdmiWarnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 4),
    _ZyTransceiverDdmiWarnMax_Type()
)
zyTransceiverDdmiWarnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiWarnMax.setStatus("current")
_ZyTransceiverDdmiWarnMin_Type = Integer32
_ZyTransceiverDdmiWarnMin_Object = MibTableColumn
zyTransceiverDdmiWarnMin = _ZyTransceiverDdmiWarnMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 5),
    _ZyTransceiverDdmiWarnMin_Type()
)
zyTransceiverDdmiWarnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiWarnMin.setStatus("current")
_ZyTransceiverDdmiCurrent_Type = Integer32
_ZyTransceiverDdmiCurrent_Object = MibTableColumn
zyTransceiverDdmiCurrent = _ZyTransceiverDdmiCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 6),
    _ZyTransceiverDdmiCurrent_Type()
)
zyTransceiverDdmiCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiCurrent.setStatus("current")
_ZyTransceiverDdmiDescription_Type = DisplayString
_ZyTransceiverDdmiDescription_Object = MibTableColumn
zyTransceiverDdmiDescription = _ZyTransceiverDdmiDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 1, 2, 1, 7),
    _ZyTransceiverDdmiDescription_Type()
)
zyTransceiverDdmiDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTransceiverDdmiDescription.setStatus("current")
_ZyxelTransceiverTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelTransceiverTrapInfoObject = _ZyxelTransceiverTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 2)
)


class _ZyTransceiverTrapOutOfRangeType_Type(Integer32):
    """Custom type zyTransceiverTrapOutOfRangeType based on Integer32"""
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
        *(("alarmHigh", 0),
          ("alarmLow", 2),
          ("warnHigh", 1),
          ("warnLow", 3))
    )


_ZyTransceiverTrapOutOfRangeType_Type.__name__ = "Integer32"
_ZyTransceiverTrapOutOfRangeType_Object = MibScalar
zyTransceiverTrapOutOfRangeType = _ZyTransceiverTrapOutOfRangeType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 2, 1),
    _ZyTransceiverTrapOutOfRangeType_Type()
)
zyTransceiverTrapOutOfRangeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTransceiverTrapOutOfRangeType.setStatus("current")
_ZyTransceiverTrapOutOfRangeValue_Type = Integer32
_ZyTransceiverTrapOutOfRangeValue_Object = MibScalar
zyTransceiverTrapOutOfRangeValue = _ZyTransceiverTrapOutOfRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 2, 2),
    _ZyTransceiverTrapOutOfRangeValue_Type()
)
zyTransceiverTrapOutOfRangeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTransceiverTrapOutOfRangeValue.setStatus("current")
_ZyxelTransceiverNotifications_ObjectIdentity = ObjectIdentity
zyxelTransceiverNotifications = _ZyxelTransceiverNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3)
)

# Managed Objects groups


# Notification objects

zyTransceiverDdmiTemperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 1)
)
zyTransceiverDdmiTemperatureOutOfRange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTemperatureOutOfRange.setStatus(
        "current"
    )

zyTransceiverDdmiTxPowerOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 2)
)
zyTransceiverDdmiTxPowerOutOfRange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTxPowerOutOfRange.setStatus(
        "current"
    )

zyTransceiverDdmiRxPowerOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 3)
)
zyTransceiverDdmiRxPowerOutOfRange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiRxPowerOutOfRange.setStatus(
        "current"
    )

zyTransceiverDdmiVoltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 4)
)
zyTransceiverDdmiVoltageOutOfRange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiVoltageOutOfRange.setStatus(
        "current"
    )

zyTransceiverDdmiTxBiasOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 5)
)
zyTransceiverDdmiTxBiasOutOfRange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTxBiasOutOfRange.setStatus(
        "current"
    )

zyTransceiverDdmiTemperatureOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 6)
)
zyTransceiverDdmiTemperatureOutOfRangeRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTemperatureOutOfRangeRecovered.setStatus(
        "current"
    )

zyTransceiverDdmiTxPowerOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 7)
)
zyTransceiverDdmiTxPowerOutOfRangeRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTxPowerOutOfRangeRecovered.setStatus(
        "current"
    )

zyTransceiverDdmiRxPowerOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 8)
)
zyTransceiverDdmiRxPowerOutOfRangeRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiRxPowerOutOfRangeRecovered.setStatus(
        "current"
    )

zyTransceiverDdmiVoltageOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 9)
)
zyTransceiverDdmiVoltageOutOfRangeRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiVoltageOutOfRangeRecovered.setStatus(
        "current"
    )

zyTransceiverDdmiTxBiasOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 84, 3, 10)
)
zyTransceiverDdmiTxBiasOutOfRangeRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-TRANSCEIVER-MIB", "zyTransceiverTrapOutOfRangeType"))
)
if mibBuilder.loadTexts:
    zyTransceiverDdmiTxBiasOutOfRangeRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-TRANSCEIVER-MIB",
    **{"zyxelTransceiver": zyxelTransceiver,
       "zyxelTransceiverStatus": zyxelTransceiverStatus,
       "zyxelTransceiverSerialTable": zyxelTransceiverSerialTable,
       "zyxelTransceiverSerialEntry": zyxelTransceiverSerialEntry,
       "zyTransceiverSerialModuleType": zyTransceiverSerialModuleType,
       "zyTransceiverSerialVendor": zyTransceiverSerialVendor,
       "zyTransceiverSerialPartNumber": zyTransceiverSerialPartNumber,
       "zyTransceiverSerialSerialNumber": zyTransceiverSerialSerialNumber,
       "zyTransceiverSerialRevision": zyTransceiverSerialRevision,
       "zyTransceiverSerialDateCode": zyTransceiverSerialDateCode,
       "zyTransceiverSerialTransceiver": zyTransceiverSerialTransceiver,
       "zyxelTransceiverDdmiTable": zyxelTransceiverDdmiTable,
       "zyxelTransceiverDdmiEntry": zyxelTransceiverDdmiEntry,
       "zyTransceiverDdmiType": zyTransceiverDdmiType,
       "zyTransceiverDdmiAlarmMax": zyTransceiverDdmiAlarmMax,
       "zyTransceiverDdmiAlarmMin": zyTransceiverDdmiAlarmMin,
       "zyTransceiverDdmiWarnMax": zyTransceiverDdmiWarnMax,
       "zyTransceiverDdmiWarnMin": zyTransceiverDdmiWarnMin,
       "zyTransceiverDdmiCurrent": zyTransceiverDdmiCurrent,
       "zyTransceiverDdmiDescription": zyTransceiverDdmiDescription,
       "zyxelTransceiverTrapInfoObject": zyxelTransceiverTrapInfoObject,
       "zyTransceiverTrapOutOfRangeType": zyTransceiverTrapOutOfRangeType,
       "zyTransceiverTrapOutOfRangeValue": zyTransceiverTrapOutOfRangeValue,
       "zyxelTransceiverNotifications": zyxelTransceiverNotifications,
       "zyTransceiverDdmiTemperatureOutOfRange": zyTransceiverDdmiTemperatureOutOfRange,
       "zyTransceiverDdmiTxPowerOutOfRange": zyTransceiverDdmiTxPowerOutOfRange,
       "zyTransceiverDdmiRxPowerOutOfRange": zyTransceiverDdmiRxPowerOutOfRange,
       "zyTransceiverDdmiVoltageOutOfRange": zyTransceiverDdmiVoltageOutOfRange,
       "zyTransceiverDdmiTxBiasOutOfRange": zyTransceiverDdmiTxBiasOutOfRange,
       "zyTransceiverDdmiTemperatureOutOfRangeRecovered": zyTransceiverDdmiTemperatureOutOfRangeRecovered,
       "zyTransceiverDdmiTxPowerOutOfRangeRecovered": zyTransceiverDdmiTxPowerOutOfRangeRecovered,
       "zyTransceiverDdmiRxPowerOutOfRangeRecovered": zyTransceiverDdmiRxPowerOutOfRangeRecovered,
       "zyTransceiverDdmiVoltageOutOfRangeRecovered": zyTransceiverDdmiVoltageOutOfRangeRecovered,
       "zyTransceiverDdmiTxBiasOutOfRangeRecovered": zyTransceiverDdmiTxBiasOutOfRangeRecovered}
)
