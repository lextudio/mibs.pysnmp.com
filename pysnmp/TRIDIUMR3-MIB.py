# SNMP MIB module (TRIDIUMR3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRIDIUMR3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:43 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tridium_ObjectIdentity = ObjectIdentity
tridium = _Tridium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4131)
)
_TridiumStation_ObjectIdentity = ObjectIdentity
tridiumStation = _TridiumStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4131, 1)
)
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")


class _Action_Type(Integer32):
    """Custom type action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ackAll", 1),
          ("noAction", 0))
    )


_Action_Type.__name__ = "Integer32"
_Action_Object = MibScalar
action = _Action_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 2),
    _Action_Type()
)
action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    action.setStatus("mandatory")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmTableEntry_Object = MibTableRow
alarmTableEntry = _AlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1)
)
alarmTableEntry.setIndexNames(
    (1, "TRIDIUMR3-MIB", "uuid"),
)
if mibBuilder.loadTexts:
    alarmTableEntry.setStatus("mandatory")
_Timestamp_Type = DisplayString
_Timestamp_Object = MibTableColumn
timestamp = _Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 1),
    _Timestamp_Type()
)
timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timestamp.setStatus("mandatory")


class _Uuid_Type(OctetString):
    """Custom type uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Uuid_Type.__name__ = "OctetString"
_Uuid_Object = MibTableColumn
uuid = _Uuid_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 2),
    _Uuid_Type()
)
uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uuid.setStatus("mandatory")


class _SourceState_Type(Integer32):
    """Custom type sourceState based on Integer32"""
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
        *(("alert", 3),
          ("fault", 2),
          ("normal", 0),
          ("offnormal", 1))
    )


_SourceState_Type.__name__ = "Integer32"
_SourceState_Object = MibTableColumn
sourceState = _SourceState_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 3),
    _SourceState_Type()
)
sourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceState.setStatus("mandatory")


class _AckState_Type(Integer32):
    """Custom type ackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ackPending", 2),
          ("acked", 0),
          ("unacked", 1))
    )


_AckState_Type.__name__ = "Integer32"
_AckState_Object = MibTableColumn
ackState = _AckState_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 4),
    _AckState_Type()
)
ackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ackState.setStatus("mandatory")


class _AckRequired_Type(Integer32):
    """Custom type ackRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AckRequired_Type.__name__ = "Integer32"
_AckRequired_Object = MibTableColumn
ackRequired = _AckRequired_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 5),
    _AckRequired_Type()
)
ackRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ackRequired.setStatus("mandatory")
_Source_Type = DisplayString
_Source_Object = MibTableColumn
source = _Source_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 6),
    _Source_Type()
)
source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source.setStatus("mandatory")
_AlarmClass_Type = DisplayString
_AlarmClass_Object = MibTableColumn
alarmClass = _AlarmClass_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 7),
    _AlarmClass_Type()
)
alarmClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClass.setStatus("mandatory")


class _Priority_Type(Integer32):
    """Custom type priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Priority_Type.__name__ = "Integer32"
_Priority_Object = MibTableColumn
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 8),
    _Priority_Type()
)
priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priority.setStatus("mandatory")
_NormalTime_Type = DisplayString
_NormalTime_Object = MibTableColumn
normalTime = _NormalTime_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 9),
    _NormalTime_Type()
)
normalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    normalTime.setStatus("mandatory")
_AckTime_Type = DisplayString
_AckTime_Object = MibTableColumn
ackTime = _AckTime_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 10),
    _AckTime_Type()
)
ackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ackTime.setStatus("mandatory")
_User_Type = DisplayString
_User_Object = MibTableColumn
user = _User_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 11),
    _User_Type()
)
user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user.setStatus("mandatory")
_AlarmData_Type = DisplayString
_AlarmData_Object = MibTableColumn
alarmData = _AlarmData_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 12),
    _AlarmData_Type()
)
alarmData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmData.setStatus("mandatory")


class _AlarmTransition_Type(Integer32):
    """Custom type alarmTransition based on Integer32"""
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
        *(("alert", 3),
          ("fault", 2),
          ("normal", 0),
          ("offnormal", 1))
    )


_AlarmTransition_Type.__name__ = "Integer32"
_AlarmTransition_Object = MibTableColumn
alarmTransition = _AlarmTransition_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 13),
    _AlarmTransition_Type()
)
alarmTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTransition.setStatus("mandatory")
_LastUpdate_Type = DisplayString
_LastUpdate_Object = MibTableColumn
lastUpdate = _LastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 3, 1, 14),
    _LastUpdate_Type()
)
lastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastUpdate.setStatus("mandatory")
_InputTable_Object = MibTable
inputTable = _InputTable_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 4)
)
if mibBuilder.loadTexts:
    inputTable.setStatus("mandatory")
_InputTableEntry_Object = MibTableRow
inputTableEntry = _InputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 4, 1)
)
inputTableEntry.setIndexNames(
    (0, "TRIDIUMR3-MIB", "inputIndex"),
)
if mibBuilder.loadTexts:
    inputTableEntry.setStatus("mandatory")


class _InputIndex_Type(Integer32):
    """Custom type inputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InputIndex_Type.__name__ = "Integer32"
_InputIndex_Object = MibTableColumn
inputIndex = _InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 4, 1, 1),
    _InputIndex_Type()
)
inputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIndex.setStatus("mandatory")
_InputName_Type = DisplayString
_InputName_Object = MibTableColumn
inputName = _InputName_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 4, 1, 2),
    _InputName_Type()
)
inputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputName.setStatus("mandatory")
_InputValue_Type = DisplayString
_InputValue_Object = MibTableColumn
inputValue = _InputValue_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 4, 1, 3),
    _InputValue_Type()
)
inputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputValue.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 5)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputTableEntry_Object = MibTableRow
outputTableEntry = _OutputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 5, 1)
)
outputTableEntry.setIndexNames(
    (0, "TRIDIUMR3-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputTableEntry.setStatus("mandatory")


class _OutputIndex_Type(Integer32):
    """Custom type outputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OutputIndex_Type.__name__ = "Integer32"
_OutputIndex_Object = MibTableColumn
outputIndex = _OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 5, 1, 1),
    _OutputIndex_Type()
)
outputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIndex.setStatus("mandatory")
_OutputName_Type = DisplayString
_OutputName_Object = MibTableColumn
outputName = _OutputName_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 5, 1, 2),
    _OutputName_Type()
)
outputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputName.setStatus("mandatory")
_OutputValue_Type = DisplayString
_OutputValue_Object = MibTableColumn
outputValue = _OutputValue_Object(
    (1, 3, 6, 1, 4, 1, 4131, 1, 5, 1, 3),
    _OutputValue_Type()
)
outputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

stationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4131, 1, 0, 1)
)
stationAlarm.setObjects(
      *(("TRIDIUMR3-MIB", "timestamp"),
        ("TRIDIUMR3-MIB", "uuid"),
        ("TRIDIUMR3-MIB", "sourceState"),
        ("TRIDIUMR3-MIB", "ackState"),
        ("TRIDIUMR3-MIB", "ackRequired"),
        ("TRIDIUMR3-MIB", "source"),
        ("TRIDIUMR3-MIB", "alarmClass"),
        ("TRIDIUMR3-MIB", "priority"),
        ("TRIDIUMR3-MIB", "normalTime"),
        ("TRIDIUMR3-MIB", "ackTime"),
        ("TRIDIUMR3-MIB", "user"),
        ("TRIDIUMR3-MIB", "alarmData"),
        ("TRIDIUMR3-MIB", "alarmTransition"),
        ("TRIDIUMR3-MIB", "lastUpdate"))
)
if mibBuilder.loadTexts:
    stationAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIDIUMR3-MIB",
    **{"tridium": tridium,
       "tridiumStation": tridiumStation,
       "stationAlarm": stationAlarm,
       "version": version,
       "action": action,
       "alarmTable": alarmTable,
       "alarmTableEntry": alarmTableEntry,
       "timestamp": timestamp,
       "uuid": uuid,
       "sourceState": sourceState,
       "ackState": ackState,
       "ackRequired": ackRequired,
       "source": source,
       "alarmClass": alarmClass,
       "priority": priority,
       "normalTime": normalTime,
       "ackTime": ackTime,
       "user": user,
       "alarmData": alarmData,
       "alarmTransition": alarmTransition,
       "lastUpdate": lastUpdate,
       "inputTable": inputTable,
       "inputTableEntry": inputTableEntry,
       "inputIndex": inputIndex,
       "inputName": inputName,
       "inputValue": inputValue,
       "outputTable": outputTable,
       "outputTableEntry": outputTableEntry,
       "outputIndex": outputIndex,
       "outputName": outputName,
       "outputValue": outputValue}
)
