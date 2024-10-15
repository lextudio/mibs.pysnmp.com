# SNMP MIB module (MRV-IR-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IR-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:49 2024
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

(irCharPortIndex,
 irHumidityThresholdHigh,
 irHumidityThresholdLow,
 irHumidityTrapSeverity,
 irHumidityValue,
 irLdAlarmContactState,
 irLdAlarmCount,
 irLdAlarmDescription,
 irLdAlarmName,
 irLdAlarmPointIndex,
 irLdAlarmPortIndex,
 irLdAlarmTrapSeverity,
 irTempThresholdHigh,
 irTempThresholdLow,
 irTempTrapSeverity,
 irTempValue) = mibBuilder.importSymbols(
    "MRV-IR-CHAR-MIB",
    "irCharPortIndex",
    "irHumidityThresholdHigh",
    "irHumidityThresholdLow",
    "irHumidityTrapSeverity",
    "irHumidityValue",
    "irLdAlarmContactState",
    "irLdAlarmCount",
    "irLdAlarmDescription",
    "irLdAlarmName",
    "irLdAlarmPointIndex",
    "irLdAlarmPortIndex",
    "irLdAlarmTrapSeverity",
    "irTempThresholdHigh",
    "irTempThresholdLow",
    "irTempTrapSeverity",
    "irTempValue")

(irAlarmContactState,
 irAlarmCount,
 irAlarmDescription,
 irAlarmName,
 irAlarmPointIndex,
 irAlarmPortIndex,
 irAlarmSlotIndex,
 irAlarmTrapSeverity,
 irAnalogCalValue,
 irAnalogDescription,
 irAnalogName,
 irAnalogPointIndex,
 irAnalogPortIndex,
 irAnalogSlotIndex,
 irAnalogThresholdHighAlarmCount,
 irAnalogThresholdLowAlarmCount,
 irAnalogThresholdSeverity,
 irHdamPortIndex,
 irHdamPowerIndex,
 irHdamPowerPortIndex,
 irHdamPowerStatus) = mibBuilder.importSymbols(
    "MRV-IR-HDAM-MIB",
    "irAlarmContactState",
    "irAlarmCount",
    "irAlarmDescription",
    "irAlarmName",
    "irAlarmPointIndex",
    "irAlarmPortIndex",
    "irAlarmSlotIndex",
    "irAlarmTrapSeverity",
    "irAnalogCalValue",
    "irAnalogDescription",
    "irAnalogName",
    "irAnalogPointIndex",
    "irAnalogPortIndex",
    "irAnalogSlotIndex",
    "irAnalogThresholdHighAlarmCount",
    "irAnalogThresholdLowAlarmCount",
    "irAnalogThresholdSeverity",
    "irHdamPortIndex",
    "irHdamPowerIndex",
    "irHdamPowerPortIndex",
    "irHdamPowerStatus")

(ipmiDiscreteOffset,
 ipmiDiscreteSensorName,
 ipmiThresholdAssert,
 ipmiThresholdDirection,
 ipmiThresholdSensorName,
 ipmiThresholdType,
 irEnetPortIndex,
 irEnetPortLinkStatus,
 irPowerIndex,
 irPowerStatus,
 irSysCurrentTemp,
 irSysTempHysteresis,
 irSysTempThresholdHigh,
 irSysTempThresholdLow,
 mrvLx) = mibBuilder.importSymbols(
    "MRV-IR-SYSTEM-MIB",
    "ipmiDiscreteOffset",
    "ipmiDiscreteSensorName",
    "ipmiThresholdAssert",
    "ipmiThresholdDirection",
    "ipmiThresholdSensorName",
    "ipmiThresholdType",
    "irEnetPortIndex",
    "irEnetPortLinkStatus",
    "irPowerIndex",
    "irPowerStatus",
    "irSysCurrentTemp",
    "irSysTempHysteresis",
    "irSysTempThresholdHigh",
    "irSysTempThresholdLow",
    "mrvLx")

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


# MODULE-IDENTITY

irTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IrTrapObjects_ObjectIdentity = ObjectIdentity
irTrapObjects = _IrTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 1)
)
_IrTextString_Type = DisplayString
_IrTextString_Object = MibScalar
irTextString = _IrTextString_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 1, 1),
    _IrTextString_Type()
)
irTextString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    irTextString.setStatus("current")
_IrTimeStamp_Type = DisplayString
_IrTimeStamp_Object = MibScalar
irTimeStamp = _IrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 1, 2),
    _IrTimeStamp_Type()
)
irTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    irTimeStamp.setStatus("current")
_IrUserName_Type = DisplayString
_IrUserName_Object = MibScalar
irUserName = _IrUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 1, 3),
    _IrUserName_Type()
)
irUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    irUserName.setStatus("current")
_IrIpAddress_Type = DisplayString
_IrIpAddress_Object = MibScalar
irIpAddress = _IrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 1, 4),
    _IrIpAddress_Type()
)
irIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    irIpAddress.setStatus("current")
_IrTraps_ObjectIdentity = ObjectIdentity
irTraps = _IrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2)
)

# Managed Objects groups


# Notification objects

irNotifyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 1)
)
irNotifyEvent.setObjects(
    ("MRV-IR-TRAP-MIB", "irTextString")
)
if mibBuilder.loadTexts:
    irNotifyEvent.setStatus(
        "current"
    )

irTempHighTholdAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 2)
)
irTempHighTholdAlarmRaised.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irTempValue"),
        ("MRV-IR-CHAR-MIB", "irTempThresholdHigh"),
        ("MRV-IR-CHAR-MIB", "irTempTrapSeverity"))
)
if mibBuilder.loadTexts:
    irTempHighTholdAlarmRaised.setStatus(
        "current"
    )

irTempHighTholdAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 3)
)
irTempHighTholdAlarmCleared.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irTempValue"),
        ("MRV-IR-CHAR-MIB", "irTempThresholdHigh"),
        ("MRV-IR-CHAR-MIB", "irTempTrapSeverity"))
)
if mibBuilder.loadTexts:
    irTempHighTholdAlarmCleared.setStatus(
        "current"
    )

irTempLowTholdAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 4)
)
irTempLowTholdAlarmRaised.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irTempValue"),
        ("MRV-IR-CHAR-MIB", "irTempThresholdLow"),
        ("MRV-IR-CHAR-MIB", "irTempTrapSeverity"))
)
if mibBuilder.loadTexts:
    irTempLowTholdAlarmRaised.setStatus(
        "current"
    )

irTempLowTholdAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 5)
)
irTempLowTholdAlarmCleared.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irTempValue"),
        ("MRV-IR-CHAR-MIB", "irTempThresholdLow"),
        ("MRV-IR-CHAR-MIB", "irTempTrapSeverity"))
)
if mibBuilder.loadTexts:
    irTempLowTholdAlarmCleared.setStatus(
        "current"
    )

irHumidityHighTholdAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 6)
)
irHumidityHighTholdAlarmRaised.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irHumidityValue"),
        ("MRV-IR-CHAR-MIB", "irHumidityThresholdHigh"),
        ("MRV-IR-CHAR-MIB", "irHumidityTrapSeverity"))
)
if mibBuilder.loadTexts:
    irHumidityHighTholdAlarmRaised.setStatus(
        "current"
    )

irHumidityHighTholdAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 7)
)
irHumidityHighTholdAlarmCleared.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irHumidityValue"),
        ("MRV-IR-CHAR-MIB", "irHumidityThresholdHigh"),
        ("MRV-IR-CHAR-MIB", "irHumidityTrapSeverity"))
)
if mibBuilder.loadTexts:
    irHumidityHighTholdAlarmCleared.setStatus(
        "current"
    )

irHumidityLowTholdAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 8)
)
irHumidityLowTholdAlarmRaised.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irHumidityValue"),
        ("MRV-IR-CHAR-MIB", "irHumidityThresholdLow"),
        ("MRV-IR-CHAR-MIB", "irHumidityTrapSeverity"))
)
if mibBuilder.loadTexts:
    irHumidityLowTholdAlarmRaised.setStatus(
        "current"
    )

irHumidityLowTholdAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 9)
)
irHumidityLowTholdAlarmCleared.setObjects(
      *(("MRV-IR-CHAR-MIB", "irCharPortIndex"),
        ("MRV-IR-CHAR-MIB", "irHumidityValue"),
        ("MRV-IR-CHAR-MIB", "irHumidityThresholdLow"),
        ("MRV-IR-CHAR-MIB", "irHumidityTrapSeverity"))
)
if mibBuilder.loadTexts:
    irHumidityLowTholdAlarmCleared.setStatus(
        "current"
    )

irClusterSyncStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 10)
)
irClusterSyncStarted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterSyncStarted.setStatus(
        "current"
    )

irClusterSyncCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 11)
)
irClusterSyncCompleted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterSyncCompleted.setStatus(
        "current"
    )

irClusterSoftwareUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 12)
)
irClusterSoftwareUpdateStarted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterSoftwareUpdateStarted.setStatus(
        "current"
    )

irClusterSoftwareUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 13)
)
irClusterSoftwareUpdateCompleted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterSoftwareUpdateCompleted.setStatus(
        "current"
    )

irClusterBootloaderUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 14)
)
irClusterBootloaderUpdateStarted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterBootloaderUpdateStarted.setStatus(
        "current"
    )

irClusterBootloaderUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 15)
)
irClusterBootloaderUpdateCompleted.setObjects(
    ("MRV-IR-TRAP-MIB", "irTimeStamp")
)
if mibBuilder.loadTexts:
    irClusterBootloaderUpdateCompleted.setStatus(
        "current"
    )

irPowerSupplyStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 16)
)
irPowerSupplyStatusChanged.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irPowerIndex"),
        ("MRV-IR-SYSTEM-MIB", "irPowerStatus"))
)
if mibBuilder.loadTexts:
    irPowerSupplyStatusChanged.setStatus(
        "current"
    )

irLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 17)
)
irLoginFailed.setObjects(
      *(("MRV-IR-TRAP-MIB", "irUserName"),
        ("MRV-IR-TRAP-MIB", "irIpAddress"),
        ("MRV-IR-CHAR-MIB", "irCharPortIndex"))
)
if mibBuilder.loadTexts:
    irLoginFailed.setStatus(
        "current"
    )

irHdamAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 18)
)
irHdamAlarmRaised.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAlarmPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmName"),
        ("MRV-IR-HDAM-MIB", "irAlarmContactState"),
        ("MRV-IR-HDAM-MIB", "irAlarmTrapSeverity"),
        ("MRV-IR-HDAM-MIB", "irAlarmCount"),
        ("MRV-IR-HDAM-MIB", "irAlarmDescription"))
)
if mibBuilder.loadTexts:
    irHdamAlarmRaised.setStatus(
        "current"
    )

irHdamAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 19)
)
irHdamAlarmCleared.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAlarmPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAlarmName"),
        ("MRV-IR-HDAM-MIB", "irAlarmContactState"),
        ("MRV-IR-HDAM-MIB", "irAlarmTrapSeverity"),
        ("MRV-IR-HDAM-MIB", "irAlarmCount"),
        ("MRV-IR-HDAM-MIB", "irAlarmDescription"))
)
if mibBuilder.loadTexts:
    irHdamAlarmCleared.setStatus(
        "current"
    )

irHdamContactLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 20)
)
irHdamContactLost.setObjects(
    ("MRV-IR-HDAM-MIB", "irHdamPortIndex")
)
if mibBuilder.loadTexts:
    irHdamContactLost.setStatus(
        "current"
    )

irHdamContactRegained = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 21)
)
irHdamContactRegained.setObjects(
    ("MRV-IR-HDAM-MIB", "irHdamPortIndex")
)
if mibBuilder.loadTexts:
    irHdamContactRegained.setStatus(
        "current"
    )

irHdamPowerStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 22)
)
irHdamPowerStatusChanged.setObjects(
      *(("MRV-IR-HDAM-MIB", "irHdamPowerPortIndex"),
        ("MRV-IR-HDAM-MIB", "irHdamPowerIndex"),
        ("MRV-IR-HDAM-MIB", "irHdamPowerStatus"))
)
if mibBuilder.loadTexts:
    irHdamPowerStatusChanged.setStatus(
        "current"
    )

irOnBoardLowTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 24)
)
irOnBoardLowTempExceeded.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irSysCurrentTemp"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempThresholdLow"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempHysteresis"))
)
if mibBuilder.loadTexts:
    irOnBoardLowTempExceeded.setStatus(
        "current"
    )

irOnBoardLowTempCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 25)
)
irOnBoardLowTempCleared.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irSysCurrentTemp"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempThresholdLow"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempHysteresis"))
)
if mibBuilder.loadTexts:
    irOnBoardLowTempCleared.setStatus(
        "current"
    )

irOnBoardHighTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 26)
)
irOnBoardHighTempExceeded.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irSysCurrentTemp"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempThresholdHigh"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempHysteresis"))
)
if mibBuilder.loadTexts:
    irOnBoardHighTempExceeded.setStatus(
        "current"
    )

irOnBoardHighTempCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 27)
)
irOnBoardHighTempCleared.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irSysCurrentTemp"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempThresholdHigh"),
        ("MRV-IR-SYSTEM-MIB", "irSysTempHysteresis"))
)
if mibBuilder.loadTexts:
    irOnBoardHighTempCleared.setStatus(
        "current"
    )

irAdminLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 28)
)
irAdminLoginFailed.setObjects(
      *(("MRV-IR-TRAP-MIB", "irUserName"),
        ("MRV-IR-CHAR-MIB", "irCharPortIndex"))
)
if mibBuilder.loadTexts:
    irAdminLoginFailed.setStatus(
        "current"
    )

irEnetPortBondLinkStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 29)
)
irEnetPortBondLinkStatusChanged.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "irEnetPortIndex"),
        ("MRV-IR-SYSTEM-MIB", "irEnetPortLinkStatus"))
)
if mibBuilder.loadTexts:
    irEnetPortBondLinkStatusChanged.setStatus(
        "current"
    )

irHdamAnalogHighAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 30)
)
irHdamAnalogHighAlarmRaised.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAnalogPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogName"),
        ("MRV-IR-HDAM-MIB", "irAnalogDescription"),
        ("MRV-IR-HDAM-MIB", "irAnalogCalValue"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdSeverity"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdHighAlarmCount"))
)
if mibBuilder.loadTexts:
    irHdamAnalogHighAlarmRaised.setStatus(
        "current"
    )

irHdamAnalogHighAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 31)
)
irHdamAnalogHighAlarmCleared.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAnalogPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogName"),
        ("MRV-IR-HDAM-MIB", "irAnalogDescription"),
        ("MRV-IR-HDAM-MIB", "irAnalogCalValue"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdSeverity"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdHighAlarmCount"))
)
if mibBuilder.loadTexts:
    irHdamAnalogHighAlarmCleared.setStatus(
        "current"
    )

irHdamAnalogLowAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 32)
)
irHdamAnalogLowAlarmRaised.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAnalogPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogName"),
        ("MRV-IR-HDAM-MIB", "irAnalogDescription"),
        ("MRV-IR-HDAM-MIB", "irAnalogCalValue"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdSeverity"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdLowAlarmCount"))
)
if mibBuilder.loadTexts:
    irHdamAnalogLowAlarmRaised.setStatus(
        "current"
    )

irHdamAnalogLowAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 33)
)
irHdamAnalogLowAlarmCleared.setObjects(
      *(("MRV-IR-HDAM-MIB", "irAnalogPortIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogSlotIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogPointIndex"),
        ("MRV-IR-HDAM-MIB", "irAnalogName"),
        ("MRV-IR-HDAM-MIB", "irAnalogDescription"),
        ("MRV-IR-HDAM-MIB", "irAnalogCalValue"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdSeverity"),
        ("MRV-IR-HDAM-MIB", "irAnalogThresholdLowAlarmCount"))
)
if mibBuilder.loadTexts:
    irHdamAnalogLowAlarmCleared.setStatus(
        "current"
    )

irLdamAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 34)
)
irLdamAlarmRaised.setObjects(
      *(("MRV-IR-CHAR-MIB", "irLdAlarmPortIndex"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmPointIndex"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmName"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmDescription"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmContactState"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmTrapSeverity"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmCount"))
)
if mibBuilder.loadTexts:
    irLdamAlarmRaised.setStatus(
        "current"
    )

irLdamAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 35)
)
irLdamAlarmCleared.setObjects(
      *(("MRV-IR-CHAR-MIB", "irLdAlarmPortIndex"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmPointIndex"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmName"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmDescription"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmContactState"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmTrapSeverity"),
        ("MRV-IR-CHAR-MIB", "irLdAlarmCount"))
)
if mibBuilder.loadTexts:
    irLdamAlarmCleared.setStatus(
        "current"
    )

irIpmiDiscreteDeassertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 36)
)
irIpmiDiscreteDeassertEvent.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "ipmiDiscreteOffset"),
        ("MRV-IR-SYSTEM-MIB", "ipmiDiscreteSensorName"))
)
if mibBuilder.loadTexts:
    irIpmiDiscreteDeassertEvent.setStatus(
        "current"
    )

irIpmiDiscreteAssertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 37)
)
irIpmiDiscreteAssertEvent.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "ipmiDiscreteOffset"),
        ("MRV-IR-SYSTEM-MIB", "ipmiDiscreteSensorName"))
)
if mibBuilder.loadTexts:
    irIpmiDiscreteAssertEvent.setStatus(
        "current"
    )

irIpmiThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 100, 3, 2, 38)
)
irIpmiThresholdEvent.setObjects(
      *(("MRV-IR-SYSTEM-MIB", "ipmiThresholdType"),
        ("MRV-IR-SYSTEM-MIB", "ipmiThresholdSensorName"),
        ("MRV-IR-SYSTEM-MIB", "ipmiThresholdDirection"),
        ("MRV-IR-SYSTEM-MIB", "ipmiThresholdAssert"))
)
if mibBuilder.loadTexts:
    irIpmiThresholdEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IR-TRAP-MIB",
    **{"irTrapMib": irTrapMib,
       "irTrapObjects": irTrapObjects,
       "irTextString": irTextString,
       "irTimeStamp": irTimeStamp,
       "irUserName": irUserName,
       "irIpAddress": irIpAddress,
       "irTraps": irTraps,
       "irNotifyEvent": irNotifyEvent,
       "irTempHighTholdAlarmRaised": irTempHighTholdAlarmRaised,
       "irTempHighTholdAlarmCleared": irTempHighTholdAlarmCleared,
       "irTempLowTholdAlarmRaised": irTempLowTholdAlarmRaised,
       "irTempLowTholdAlarmCleared": irTempLowTholdAlarmCleared,
       "irHumidityHighTholdAlarmRaised": irHumidityHighTholdAlarmRaised,
       "irHumidityHighTholdAlarmCleared": irHumidityHighTholdAlarmCleared,
       "irHumidityLowTholdAlarmRaised": irHumidityLowTholdAlarmRaised,
       "irHumidityLowTholdAlarmCleared": irHumidityLowTholdAlarmCleared,
       "irClusterSyncStarted": irClusterSyncStarted,
       "irClusterSyncCompleted": irClusterSyncCompleted,
       "irClusterSoftwareUpdateStarted": irClusterSoftwareUpdateStarted,
       "irClusterSoftwareUpdateCompleted": irClusterSoftwareUpdateCompleted,
       "irClusterBootloaderUpdateStarted": irClusterBootloaderUpdateStarted,
       "irClusterBootloaderUpdateCompleted": irClusterBootloaderUpdateCompleted,
       "irPowerSupplyStatusChanged": irPowerSupplyStatusChanged,
       "irLoginFailed": irLoginFailed,
       "irHdamAlarmRaised": irHdamAlarmRaised,
       "irHdamAlarmCleared": irHdamAlarmCleared,
       "irHdamContactLost": irHdamContactLost,
       "irHdamContactRegained": irHdamContactRegained,
       "irHdamPowerStatusChanged": irHdamPowerStatusChanged,
       "irOnBoardLowTempExceeded": irOnBoardLowTempExceeded,
       "irOnBoardLowTempCleared": irOnBoardLowTempCleared,
       "irOnBoardHighTempExceeded": irOnBoardHighTempExceeded,
       "irOnBoardHighTempCleared": irOnBoardHighTempCleared,
       "irAdminLoginFailed": irAdminLoginFailed,
       "irEnetPortBondLinkStatusChanged": irEnetPortBondLinkStatusChanged,
       "irHdamAnalogHighAlarmRaised": irHdamAnalogHighAlarmRaised,
       "irHdamAnalogHighAlarmCleared": irHdamAnalogHighAlarmCleared,
       "irHdamAnalogLowAlarmRaised": irHdamAnalogLowAlarmRaised,
       "irHdamAnalogLowAlarmCleared": irHdamAnalogLowAlarmCleared,
       "irLdamAlarmRaised": irLdamAlarmRaised,
       "irLdamAlarmCleared": irLdamAlarmCleared,
       "irIpmiDiscreteDeassertEvent": irIpmiDiscreteDeassertEvent,
       "irIpmiDiscreteAssertEvent": irIpmiDiscreteAssertEvent,
       "irIpmiThresholdEvent": irIpmiThresholdEvent}
)
