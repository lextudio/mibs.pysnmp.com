# SNMP MIB module (ZHONE-FS-ALARM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-FS-ALARM
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:29 2024
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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneTrapVersion,
 zhoneTrapsSequenceNumber,
 zhoneTrapsSeverity) = mibBuilder.importSymbols(
    "ZHONE-SYSTEM-MIB",
    "zhoneTrapVersion",
    "zhoneTrapsSequenceNumber",
    "zhoneTrapsSeverity")

(zhoneZmsProduct,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneZmsProduct")


# MODULE-IDENTITY

faultServiceAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1)
)
faultServiceAlarm.setRevisions(
        ("2013-04-21 16:29",
         "2009-04-29 13:47",
         "2001-07-27 16:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FaultServiceDefinitions_ObjectIdentity = ObjectIdentity
faultServiceDefinitions = _FaultServiceDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    faultServiceDefinitions.setStatus("current")


class _AlarmName_Type(OctetString):
    """Custom type alarmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_AlarmName_Type.__name__ = "OctetString"
_AlarmName_Object = MibScalar
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 1),
    _AlarmName_Type()
)
alarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmDescription_Type(OctetString):
    """Custom type alarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AlarmDescription_Type.__name__ = "OctetString"
_AlarmDescription_Object = MibScalar
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 2),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")


class _AlarmType_Type(OctetString):
    """Custom type alarmType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmType_Type.__name__ = "OctetString"
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 3),
    _AlarmType_Type()
)
alarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("informational", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmTimestamp_Type = OctetString
_AlarmTimestamp_Object = MibScalar
alarmTimestamp = _AlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 5),
    _AlarmTimestamp_Type()
)
alarmTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTimestamp.setStatus("current")
_AlarmDevice_Type = IpAddress
_AlarmDevice_Object = MibScalar
alarmDevice = _AlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 6),
    _AlarmDevice_Type()
)
alarmDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmDevice.setStatus("current")


class _AlarmShelf_Type(Integer32):
    """Custom type alarmShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_AlarmShelf_Type.__name__ = "Integer32"
_AlarmShelf_Object = MibScalar
alarmShelf = _AlarmShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 7),
    _AlarmShelf_Type()
)
alarmShelf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmShelf.setStatus("current")


class _AlarmSlot_Type(Integer32):
    """Custom type alarmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AlarmSlot_Type.__name__ = "Integer32"
_AlarmSlot_Object = MibScalar
alarmSlot = _AlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 8),
    _AlarmSlot_Type()
)
alarmSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSlot.setStatus("current")
_AlarmPort_Type = Integer32
_AlarmPort_Object = MibScalar
alarmPort = _AlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 9),
    _AlarmPort_Type()
)
alarmPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmPort.setStatus("current")
_AlarmSubPort_Type = Integer32
_AlarmSubPort_Object = MibScalar
alarmSubPort = _AlarmSubPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 10),
    _AlarmSubPort_Type()
)
alarmSubPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubPort.setStatus("current")


class _AlarmDeviceName_Type(OctetString):
    """Custom type alarmDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmDeviceName_Type.__name__ = "OctetString"
_AlarmDeviceName_Object = MibScalar
alarmDeviceName = _AlarmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 11),
    _AlarmDeviceName_Type()
)
alarmDeviceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmDeviceName.setStatus("current")
_AlarmCpeInternal_Type = TruthValue
_AlarmCpeInternal_Object = MibScalar
alarmCpeInternal = _AlarmCpeInternal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 12),
    _AlarmCpeInternal_Type()
)
alarmCpeInternal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmCpeInternal.setStatus("current")
_AlarmCpePortType_Type = Integer32
_AlarmCpePortType_Object = MibScalar
alarmCpePortType = _AlarmCpePortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 13),
    _AlarmCpePortType_Type()
)
alarmCpePortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmCpePortType.setStatus("current")
_AlarmCpePortId_Type = Integer32
_AlarmCpePortId_Object = MibScalar
alarmCpePortId = _AlarmCpePortId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 14),
    _AlarmCpePortId_Type()
)
alarmCpePortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmCpePortId.setStatus("current")
_FaultServiceTraps_ObjectIdentity = ObjectIdentity
faultServiceTraps = _FaultServiceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    faultServiceTraps.setStatus("current")
_FaultServiceV2Traps_ObjectIdentity = ObjectIdentity
faultServiceV2Traps = _FaultServiceV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0)
)
if mibBuilder.loadTexts:
    faultServiceV2Traps.setStatus("current")
_FaultServiceCompliances_ObjectIdentity = ObjectIdentity
faultServiceCompliances = _FaultServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    faultServiceCompliances.setStatus("current")
_FaultServiceGroups_ObjectIdentity = ObjectIdentity
faultServiceGroups = _FaultServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    faultServiceGroups.setStatus("current")
_FaultServiceImports_ObjectIdentity = ObjectIdentity
faultServiceImports = _FaultServiceImports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    faultServiceImports.setStatus("current")

# Managed Objects groups

faultServiceAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1, 1)
)
faultServiceAlarmGroup.setObjects(
      *(("ZHONE-FS-ALARM", "alarmName"),
        ("ZHONE-FS-ALARM", "alarmDescription"),
        ("ZHONE-FS-ALARM", "alarmType"),
        ("ZHONE-FS-ALARM", "alarmSeverity"),
        ("ZHONE-FS-ALARM", "alarmTimestamp"),
        ("ZHONE-FS-ALARM", "alarmDevice"),
        ("ZHONE-FS-ALARM", "alarmShelf"),
        ("ZHONE-FS-ALARM", "alarmSlot"),
        ("ZHONE-FS-ALARM", "alarmPort"),
        ("ZHONE-FS-ALARM", "alarmSubPort"),
        ("ZHONE-FS-ALARM", "alarmDeviceName"),
        ("ZHONE-FS-ALARM", "alarmCpeInternal"),
        ("ZHONE-FS-ALARM", "alarmCpePortType"),
        ("ZHONE-FS-ALARM", "alarmCpePortId"))
)
if mibBuilder.loadTexts:
    faultServiceAlarmGroup.setStatus("current")


# Notification objects

alarmReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0, 1)
)
alarmReceived.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneTrapVersion"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSeverity"),
        ("ZHONE-FS-ALARM", "alarmName"),
        ("ZHONE-FS-ALARM", "alarmDescription"),
        ("ZHONE-FS-ALARM", "alarmType"),
        ("ZHONE-FS-ALARM", "alarmSeverity"),
        ("ZHONE-FS-ALARM", "alarmTimestamp"),
        ("ZHONE-FS-ALARM", "alarmDevice"),
        ("ZHONE-FS-ALARM", "alarmShelf"),
        ("ZHONE-FS-ALARM", "alarmSlot"),
        ("ZHONE-FS-ALARM", "alarmPort"),
        ("ZHONE-FS-ALARM", "alarmSubPort"),
        ("ZHONE-FS-ALARM", "alarmDeviceName"),
        ("ZHONE-FS-ALARM", "alarmCpeInternal"),
        ("ZHONE-FS-ALARM", "alarmCpePortType"),
        ("ZHONE-FS-ALARM", "alarmCpePortId"))
)
if mibBuilder.loadTexts:
    alarmReceived.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0, 2)
)
alarmCleared.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneTrapVersion"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSeverity"),
        ("ZHONE-FS-ALARM", "alarmName"),
        ("ZHONE-FS-ALARM", "alarmDescription"),
        ("ZHONE-FS-ALARM", "alarmType"),
        ("ZHONE-FS-ALARM", "alarmSeverity"),
        ("ZHONE-FS-ALARM", "alarmTimestamp"),
        ("ZHONE-FS-ALARM", "alarmDevice"),
        ("ZHONE-FS-ALARM", "alarmShelf"),
        ("ZHONE-FS-ALARM", "alarmSlot"),
        ("ZHONE-FS-ALARM", "alarmPort"),
        ("ZHONE-FS-ALARM", "alarmSubPort"),
        ("ZHONE-FS-ALARM", "alarmDeviceName"),
        ("ZHONE-FS-ALARM", "alarmCpeInternal"),
        ("ZHONE-FS-ALARM", "alarmCpePortType"),
        ("ZHONE-FS-ALARM", "alarmCpePortId"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )


# Notifications groups

faultServiceTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1, 2)
)
faultServiceTrapGroup.setObjects(
      *(("ZHONE-FS-ALARM", "alarmReceived"),
        ("ZHONE-FS-ALARM", "alarmCleared"))
)
if mibBuilder.loadTexts:
    faultServiceTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-FS-ALARM",
    **{"faultServiceAlarm": faultServiceAlarm,
       "faultServiceDefinitions": faultServiceDefinitions,
       "alarmName": alarmName,
       "alarmDescription": alarmDescription,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmTimestamp": alarmTimestamp,
       "alarmDevice": alarmDevice,
       "alarmShelf": alarmShelf,
       "alarmSlot": alarmSlot,
       "alarmPort": alarmPort,
       "alarmSubPort": alarmSubPort,
       "alarmDeviceName": alarmDeviceName,
       "alarmCpeInternal": alarmCpeInternal,
       "alarmCpePortType": alarmCpePortType,
       "alarmCpePortId": alarmCpePortId,
       "faultServiceTraps": faultServiceTraps,
       "faultServiceV2Traps": faultServiceV2Traps,
       "alarmReceived": alarmReceived,
       "alarmCleared": alarmCleared,
       "faultServiceCompliances": faultServiceCompliances,
       "faultServiceGroups": faultServiceGroups,
       "faultServiceAlarmGroup": faultServiceAlarmGroup,
       "faultServiceTrapGroup": faultServiceTrapGroup,
       "faultServiceImports": faultServiceImports}
)
