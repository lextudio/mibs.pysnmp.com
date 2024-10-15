# SNMP MIB module (SL81-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SL81-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:53:49 2024
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
 ObjectName,
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
    "ObjectName",
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

_Omnitronix_ObjectIdentity = ObjectIdentity
omnitronix = _Omnitronix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052)
)
_Sl81_ObjectIdentity = ObjectIdentity
sl81 = _Sl81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("mandatory")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "SL81-STD-MIB", "esIndexES"),
    (0, "SL81-STD-MIB", "esIndexPC"),
    (0, "SL81-STD-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("mandatory")
_EsIndexES_Type = Integer32
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("mandatory")
_EsIndexPC_Type = Integer32
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("mandatory")
_EsIndexPoint_Type = Integer32
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("mandatory")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("mandatory")
_EsPointInEventState_Type = Integer32
_EsPointInEventState_Object = MibTableColumn
esPointInEventState = _EsPointInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 5),
    _EsPointInEventState_Type()
)
esPointInEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointInEventState.setStatus("mandatory")


class _EsPointValueInt_Type(Integer32):
    """Custom type esPointValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_EsPointValueInt_Type.__name__ = "Integer32"
_EsPointValueInt_Object = MibTableColumn
esPointValueInt = _EsPointValueInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 6),
    _EsPointValueInt_Type()
)
esPointValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointValueInt.setStatus("mandatory")
_EsPointValueStr_Type = DisplayString
_EsPointValueStr_Object = MibTableColumn
esPointValueStr = _EsPointValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 7),
    _EsPointValueStr_Type()
)
esPointValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointValueStr.setStatus("mandatory")
_EsPointTimeLastChange_Type = DisplayString
_EsPointTimeLastChange_Object = MibTableColumn
esPointTimeLastChange = _EsPointTimeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 8),
    _EsPointTimeLastChange_Type()
)
esPointTimeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimeLastChange.setStatus("mandatory")
_EsPointTimetickLastChange_Type = TimeTicks
_EsPointTimetickLastChange_Object = MibTableColumn
esPointTimetickLastChange = _EsPointTimetickLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 1, 1, 1, 9),
    _EsPointTimetickLastChange_Type()
)
esPointTimetickLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimetickLastChange.setStatus("mandatory")
_DataEventStatus_ObjectIdentity = ObjectIdentity
dataEventStatus = _DataEventStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2)
)
_DeStatusTable_Object = MibTable
deStatusTable = _DeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deStatusTable.setStatus("mandatory")
_DeStatusEntry_Object = MibTableRow
deStatusEntry = _DeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1)
)
deStatusEntry.setIndexNames(
    (0, "SL81-STD-MIB", "deStatusIndex"),
)
if mibBuilder.loadTexts:
    deStatusEntry.setStatus("mandatory")
_DeStatusIndex_Type = Integer32
_DeStatusIndex_Object = MibTableColumn
deStatusIndex = _DeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 1),
    _DeStatusIndex_Type()
)
deStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusIndex.setStatus("mandatory")
_DeStatusName_Type = DisplayString
_DeStatusName_Object = MibTableColumn
deStatusName = _DeStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 2),
    _DeStatusName_Type()
)
deStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusName.setStatus("mandatory")
_DeStatusCounter_Type = Integer32
_DeStatusCounter_Object = MibTableColumn
deStatusCounter = _DeStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 3),
    _DeStatusCounter_Type()
)
deStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusCounter.setStatus("mandatory")
_DeStatusThreshold_Type = Integer32
_DeStatusThreshold_Object = MibTableColumn
deStatusThreshold = _DeStatusThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 4),
    _DeStatusThreshold_Type()
)
deStatusThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusThreshold.setStatus("mandatory")
_DeStatusLastTriggerTime_Type = DisplayString
_DeStatusLastTriggerTime_Object = MibTableColumn
deStatusLastTriggerTime = _DeStatusLastTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 5),
    _DeStatusLastTriggerTime_Type()
)
deStatusLastTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusLastTriggerTime.setStatus("mandatory")
_DeStatusLastTriggerData_Type = DisplayString
_DeStatusLastTriggerData_Object = MibTableColumn
deStatusLastTriggerData = _DeStatusLastTriggerData_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 1, 2, 1, 1, 6),
    _DeStatusLastTriggerData_Type()
)
deStatusLastTriggerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusLastTriggerData.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2)
)
_EventSensorBasics_ObjectIdentity = ObjectIdentity
eventSensorBasics = _EventSensorBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("mandatory")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1)
)
esEntry.setIndexNames(
    (0, "SL81-STD-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("mandatory")
_EsIndex_Type = Integer32
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("mandatory")
_EsName_Type = DisplayString
_EsName_Object = MibTableColumn
esName = _EsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 2),
    _EsName_Type()
)
esName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esName.setStatus("mandatory")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 3),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("mandatory")
_EsNumberTempSensors_Type = Integer32
_EsNumberTempSensors_Object = MibTableColumn
esNumberTempSensors = _EsNumberTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 4),
    _EsNumberTempSensors_Type()
)
esNumberTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberTempSensors.setStatus("mandatory")
_EsTempReportingMode_Type = DisplayString
_EsTempReportingMode_Object = MibTableColumn
esTempReportingMode = _EsTempReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 5),
    _EsTempReportingMode_Type()
)
esTempReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempReportingMode.setStatus("mandatory")
_EsNumberCCs_Type = Integer32
_EsNumberCCs_Object = MibTableColumn
esNumberCCs = _EsNumberCCs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 6),
    _EsNumberCCs_Type()
)
esNumberCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberCCs.setStatus("mandatory")
_EsCCReportingMode_Type = DisplayString
_EsCCReportingMode_Object = MibTableColumn
esCCReportingMode = _EsCCReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 7),
    _EsCCReportingMode_Type()
)
esCCReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCReportingMode.setStatus("mandatory")
_EsNumberHumidSensors_Type = Integer32
_EsNumberHumidSensors_Object = MibTableColumn
esNumberHumidSensors = _EsNumberHumidSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 8),
    _EsNumberHumidSensors_Type()
)
esNumberHumidSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberHumidSensors.setStatus("mandatory")
_EsHumidReportingMode_Type = DisplayString
_EsHumidReportingMode_Object = MibTableColumn
esHumidReportingMode = _EsHumidReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 9),
    _EsHumidReportingMode_Type()
)
esHumidReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidReportingMode.setStatus("mandatory")
_EsNumberNoiseSensors_Type = Integer32
_EsNumberNoiseSensors_Object = MibTableColumn
esNumberNoiseSensors = _EsNumberNoiseSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 10),
    _EsNumberNoiseSensors_Type()
)
esNumberNoiseSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberNoiseSensors.setStatus("mandatory")
_EsNoiseReportingMode_Type = DisplayString
_EsNoiseReportingMode_Object = MibTableColumn
esNoiseReportingMode = _EsNoiseReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 11),
    _EsNoiseReportingMode_Type()
)
esNoiseReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNoiseReportingMode.setStatus("mandatory")
_EsNumberAirflowSensors_Type = Integer32
_EsNumberAirflowSensors_Object = MibTableColumn
esNumberAirflowSensors = _EsNumberAirflowSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 12),
    _EsNumberAirflowSensors_Type()
)
esNumberAirflowSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAirflowSensors.setStatus("mandatory")
_EsAirflowReportingMode_Type = DisplayString
_EsAirflowReportingMode_Object = MibTableColumn
esAirflowReportingMode = _EsAirflowReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 13),
    _EsAirflowReportingMode_Type()
)
esAirflowReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAirflowReportingMode.setStatus("mandatory")
_EsNumberAnalog_Type = Integer32
_EsNumberAnalog_Object = MibTableColumn
esNumberAnalog = _EsNumberAnalog_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 14),
    _EsNumberAnalog_Type()
)
esNumberAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAnalog.setStatus("mandatory")
_EsAnalogReportingMode_Type = DisplayString
_EsAnalogReportingMode_Object = MibTableColumn
esAnalogReportingMode = _EsAnalogReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 15),
    _EsAnalogReportingMode_Type()
)
esAnalogReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogReportingMode.setStatus("mandatory")
_EsNumberRelayOutputs_Type = Integer32
_EsNumberRelayOutputs_Object = MibTableColumn
esNumberRelayOutputs = _EsNumberRelayOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 16),
    _EsNumberRelayOutputs_Type()
)
esNumberRelayOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberRelayOutputs.setStatus("mandatory")
_EsRelayReportingMode_Type = DisplayString
_EsRelayReportingMode_Object = MibTableColumn
esRelayReportingMode = _EsRelayReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 1, 2, 1, 17),
    _EsRelayReportingMode_Type()
)
esRelayReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esRelayReportingMode.setStatus("mandatory")
_DataEventConfig_ObjectIdentity = ObjectIdentity
dataEventConfig = _DataEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2)
)
_DeFieldTable_Object = MibTable
deFieldTable = _DeFieldTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    deFieldTable.setStatus("mandatory")
_DeFieldEntry_Object = MibTableRow
deFieldEntry = _DeFieldEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1, 1)
)
deFieldEntry.setIndexNames(
    (0, "SL81-STD-MIB", "deFieldIndex"),
)
if mibBuilder.loadTexts:
    deFieldEntry.setStatus("mandatory")
_DeFieldIndex_Type = Integer32
_DeFieldIndex_Object = MibTableColumn
deFieldIndex = _DeFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1, 1, 1),
    _DeFieldIndex_Type()
)
deFieldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deFieldIndex.setStatus("mandatory")
_DeFieldStart_Type = Integer32
_DeFieldStart_Object = MibTableColumn
deFieldStart = _DeFieldStart_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1, 1, 2),
    _DeFieldStart_Type()
)
deFieldStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deFieldStart.setStatus("mandatory")
_DeFieldLength_Type = Integer32
_DeFieldLength_Object = MibTableColumn
deFieldLength = _DeFieldLength_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1, 1, 3),
    _DeFieldLength_Type()
)
deFieldLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deFieldLength.setStatus("mandatory")
_DeFieldName_Type = DisplayString
_DeFieldName_Object = MibTableColumn
deFieldName = _DeFieldName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 1, 1, 4),
    _DeFieldName_Type()
)
deFieldName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deFieldName.setStatus("mandatory")
_DeConfigTable_Object = MibTable
deConfigTable = _DeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    deConfigTable.setStatus("mandatory")
_DeConfigEntry_Object = MibTableRow
deConfigEntry = _DeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1)
)
deConfigEntry.setIndexNames(
    (0, "SL81-STD-MIB", "deConfigIndex"),
)
if mibBuilder.loadTexts:
    deConfigEntry.setStatus("mandatory")
_DeConfigIndex_Type = Integer32
_DeConfigIndex_Object = MibTableColumn
deConfigIndex = _DeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 1),
    _DeConfigIndex_Type()
)
deConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deConfigIndex.setStatus("mandatory")
_DeConfigEnabled_Type = Integer32
_DeConfigEnabled_Object = MibTableColumn
deConfigEnabled = _DeConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 2),
    _DeConfigEnabled_Type()
)
deConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigEnabled.setStatus("mandatory")
_DeConfigName_Type = DisplayString
_DeConfigName_Object = MibTableColumn
deConfigName = _DeConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 3),
    _DeConfigName_Type()
)
deConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigName.setStatus("mandatory")
_DeConfigEquation_Type = DisplayString
_DeConfigEquation_Object = MibTableColumn
deConfigEquation = _DeConfigEquation_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 4),
    _DeConfigEquation_Type()
)
deConfigEquation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigEquation.setStatus("mandatory")
_DeConfigThreshold_Type = Integer32
_DeConfigThreshold_Object = MibTableColumn
deConfigThreshold = _DeConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 5),
    _DeConfigThreshold_Type()
)
deConfigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigThreshold.setStatus("mandatory")
_DeConfigClearMode_Type = Integer32
_DeConfigClearMode_Object = MibTableColumn
deConfigClearMode = _DeConfigClearMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 6),
    _DeConfigClearMode_Type()
)
deConfigClearMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigClearMode.setStatus("mandatory")
_DeConfigClearTime_Type = DisplayString
_DeConfigClearTime_Object = MibTableColumn
deConfigClearTime = _DeConfigClearTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 7),
    _DeConfigClearTime_Type()
)
deConfigClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigClearTime.setStatus("mandatory")
_DeConfigAutoClear_Type = Integer32
_DeConfigAutoClear_Object = MibTableColumn
deConfigAutoClear = _DeConfigAutoClear_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 8),
    _DeConfigAutoClear_Type()
)
deConfigAutoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigAutoClear.setStatus("mandatory")
_DeConfigActions_Type = DisplayString
_DeConfigActions_Object = MibTableColumn
deConfigActions = _DeConfigActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 9),
    _DeConfigActions_Type()
)
deConfigActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigActions.setStatus("mandatory")
_DeConfigTrapNumber_Type = Integer32
_DeConfigTrapNumber_Object = MibTableColumn
deConfigTrapNumber = _DeConfigTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 10),
    _DeConfigTrapNumber_Type()
)
deConfigTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigTrapNumber.setStatus("mandatory")
_DeConfigClass_Type = Integer32
_DeConfigClass_Object = MibTableColumn
deConfigClass = _DeConfigClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 2, 2, 1, 11),
    _DeConfigClass_Type()
)
deConfigClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deConfigClass.setStatus("mandatory")
_SerialPorts_ObjectIdentity = ObjectIdentity
serialPorts = _SerialPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3)
)
_NumberPorts_Type = Integer32
_NumberPorts_Object = MibScalar
numberPorts = _NumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 1),
    _NumberPorts_Type()
)
numberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberPorts.setStatus("mandatory")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("mandatory")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1)
)
portConfigEntry.setIndexNames(
    (0, "SL81-STD-MIB", "portConfigIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("mandatory")
_PortConfigIndex_Type = Integer32
_PortConfigIndex_Object = MibTableColumn
portConfigIndex = _PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 1),
    _PortConfigIndex_Type()
)
portConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigIndex.setStatus("mandatory")
_PortConfigBaud_Type = Integer32
_PortConfigBaud_Object = MibTableColumn
portConfigBaud = _PortConfigBaud_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 2),
    _PortConfigBaud_Type()
)
portConfigBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBaud.setStatus("mandatory")
_PortConfigDataFormat_Type = Integer32
_PortConfigDataFormat_Object = MibTableColumn
portConfigDataFormat = _PortConfigDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 3),
    _PortConfigDataFormat_Type()
)
portConfigDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDataFormat.setStatus("mandatory")
_PortConfigStripPtOutputLfs_Type = Integer32
_PortConfigStripPtOutputLfs_Object = MibTableColumn
portConfigStripPtOutputLfs = _PortConfigStripPtOutputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 4),
    _PortConfigStripPtOutputLfs_Type()
)
portConfigStripPtOutputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtOutputLfs.setStatus("mandatory")
_PortConfigStripPtInputLfs_Type = Integer32
_PortConfigStripPtInputLfs_Object = MibTableColumn
portConfigStripPtInputLfs = _PortConfigStripPtInputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 5),
    _PortConfigStripPtInputLfs_Type()
)
portConfigStripPtInputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtInputLfs.setStatus("mandatory")
_PortConfigDTRLowIdle_Type = Integer32
_PortConfigDTRLowIdle_Object = MibTableColumn
portConfigDTRLowIdle = _PortConfigDTRLowIdle_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 6),
    _PortConfigDTRLowIdle_Type()
)
portConfigDTRLowIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDTRLowIdle.setStatus("mandatory")
_PortConfigMaskEnable_Type = Integer32
_PortConfigMaskEnable_Object = MibTableColumn
portConfigMaskEnable = _PortConfigMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 7),
    _PortConfigMaskEnable_Type()
)
portConfigMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMaskEnable.setStatus("mandatory")
_PortConfigDAEnable_Type = Integer32
_PortConfigDAEnable_Object = MibTableColumn
portConfigDAEnable = _PortConfigDAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 3, 2, 1, 8),
    _PortConfigDAEnable_Type()
)
portConfigDAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDAEnable.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4)
)
_IpConfigStatic_Type = Integer32
_IpConfigStatic_Object = MibScalar
ipConfigStatic = _IpConfigStatic_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 1),
    _IpConfigStatic_Type()
)
ipConfigStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipConfigStatic.setStatus("mandatory")
_IpConfigAddress_Type = IpAddress
_IpConfigAddress_Object = MibScalar
ipConfigAddress = _IpConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 2),
    _IpConfigAddress_Type()
)
ipConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigAddress.setStatus("mandatory")
_IpConfigSubnetMask_Type = IpAddress
_IpConfigSubnetMask_Object = MibScalar
ipConfigSubnetMask = _IpConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 3),
    _IpConfigSubnetMask_Type()
)
ipConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigSubnetMask.setStatus("mandatory")
_IpConfigDefaultRouter_Type = IpAddress
_IpConfigDefaultRouter_Object = MibScalar
ipConfigDefaultRouter = _IpConfigDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 4),
    _IpConfigDefaultRouter_Type()
)
ipConfigDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigDefaultRouter.setStatus("mandatory")
_IpConfigEngage_Type = Integer32
_IpConfigEngage_Object = MibScalar
ipConfigEngage = _IpConfigEngage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 5),
    _IpConfigEngage_Type()
)
ipConfigEngage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigEngage.setStatus("mandatory")
_TelnetDuplex_Type = Integer32
_TelnetDuplex_Object = MibScalar
telnetDuplex = _TelnetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 4, 6),
    _TelnetDuplex_Type()
)
telnetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetDuplex.setStatus("mandatory")
_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 5)
)
_ModemDataFormat_Type = Integer32
_ModemDataFormat_Object = MibScalar
modemDataFormat = _ModemDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 5, 1),
    _ModemDataFormat_Type()
)
modemDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemDataFormat.setStatus("mandatory")
_ModemUserSetup_Type = DisplayString
_ModemUserSetup_Object = MibScalar
modemUserSetup = _ModemUserSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 5, 2),
    _ModemUserSetup_Type()
)
modemUserSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemUserSetup.setStatus("mandatory")
_ModemTAPSetup_Type = DisplayString
_ModemTAPSetup_Object = MibScalar
modemTAPSetup = _ModemTAPSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 5, 3),
    _ModemTAPSetup_Type()
)
modemTAPSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTAPSetup.setStatus("mandatory")
_ModemTimeBetweenOutbound_Type = Integer32
_ModemTimeBetweenOutbound_Object = MibScalar
modemTimeBetweenOutbound = _ModemTimeBetweenOutbound_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 5, 5),
    _ModemTimeBetweenOutbound_Type()
)
modemTimeBetweenOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTimeBetweenOutbound.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 6)
)
_SmTable_Object = MibTable
smTable = _SmTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    smTable.setStatus("mandatory")
_SmEntry_Object = MibTableRow
smEntry = _SmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 6, 1, 1)
)
smEntry.setIndexNames(
    (0, "SL81-STD-MIB", "smIndex"),
)
if mibBuilder.loadTexts:
    smEntry.setStatus("mandatory")
_SmIndex_Type = Integer32
_SmIndex_Object = MibTableColumn
smIndex = _SmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 6, 1, 1, 1),
    _SmIndex_Type()
)
smIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smIndex.setStatus("mandatory")
_SmAddress_Type = IpAddress
_SmAddress_Object = MibTableColumn
smAddress = _SmAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 6, 1, 1, 2),
    _SmAddress_Type()
)
smAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smAddress.setStatus("mandatory")
_Pagers_ObjectIdentity = ObjectIdentity
pagers = _Pagers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7)
)
_PagerRetries_Type = Integer32
_PagerRetries_Object = MibScalar
pagerRetries = _PagerRetries_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 1),
    _PagerRetries_Type()
)
pagerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerRetries.setStatus("mandatory")
_PagerTable_Object = MibTable
pagerTable = _PagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    pagerTable.setStatus("mandatory")
_PagerEntry_Object = MibTableRow
pagerEntry = _PagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1)
)
pagerEntry.setIndexNames(
    (0, "SL81-STD-MIB", "pagerIndex"),
)
if mibBuilder.loadTexts:
    pagerEntry.setStatus("mandatory")
_PagerIndex_Type = Integer32
_PagerIndex_Object = MibTableColumn
pagerIndex = _PagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 1),
    _PagerIndex_Type()
)
pagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagerIndex.setStatus("mandatory")
_PagerType_Type = Integer32
_PagerType_Object = MibTableColumn
pagerType = _PagerType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 2),
    _PagerType_Type()
)
pagerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerType.setStatus("mandatory")
_PagerPhoneNumber_Type = DisplayString
_PagerPhoneNumber_Object = MibTableColumn
pagerPhoneNumber = _PagerPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 3),
    _PagerPhoneNumber_Type()
)
pagerPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerPhoneNumber.setStatus("mandatory")
_PagerID_Type = DisplayString
_PagerID_Object = MibTableColumn
pagerID = _PagerID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 4),
    _PagerID_Type()
)
pagerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerID.setStatus("mandatory")
_PagerPostCalloutDelay_Type = Integer32
_PagerPostCalloutDelay_Object = MibTableColumn
pagerPostCalloutDelay = _PagerPostCalloutDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 5),
    _PagerPostCalloutDelay_Type()
)
pagerPostCalloutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerPostCalloutDelay.setStatus("mandatory")
_PagerIDDelay_Type = Integer32
_PagerIDDelay_Object = MibTableColumn
pagerIDDelay = _PagerIDDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 7, 2, 1, 6),
    _PagerIDDelay_Type()
)
pagerIDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerIDDelay.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 8)
)
_Clock_Type = DisplayString
_Clock_Object = MibScalar
clock = _Clock_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 8, 1),
    _Clock_Type()
)
clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clock.setStatus("mandatory")
_AutoDSTAdjust_Type = Integer32
_AutoDSTAdjust_Object = MibScalar
autoDSTAdjust = _AutoDSTAdjust_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 8, 2),
    _AutoDSTAdjust_Type()
)
autoDSTAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDSTAdjust.setStatus("mandatory")
_Timeouts_ObjectIdentity = ObjectIdentity
timeouts = _Timeouts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 9)
)
_CommandTimeout_Type = Integer32
_CommandTimeout_Object = MibScalar
commandTimeout = _CommandTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 9, 1),
    _CommandTimeout_Type()
)
commandTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandTimeout.setStatus("mandatory")
_PassthroughTimeout_Type = Integer32
_PassthroughTimeout_Object = MibScalar
passthroughTimeout = _PassthroughTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 2, 9, 2),
    _PassthroughTimeout_Type()
)
passthroughTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passthroughTimeout.setStatus("mandatory")
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3)
)
_SiteID_Type = DisplayString
_SiteID_Object = MibScalar
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 1),
    _SiteID_Type()
)
siteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
_ThisProduct_Type = DisplayString
_ThisProduct_Object = MibScalar
thisProduct = _ThisProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 2),
    _ThisProduct_Type()
)
thisProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thisProduct.setStatus("mandatory")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("mandatory")
_TrapEventTypeNumber_Type = Integer32
_TrapEventTypeNumber_Object = MibScalar
trapEventTypeNumber = _TrapEventTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 4),
    _TrapEventTypeNumber_Type()
)
trapEventTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeNumber.setStatus("mandatory")
_TrapEventTypeName_Type = DisplayString
_TrapEventTypeName_Object = MibScalar
trapEventTypeName = _TrapEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 5),
    _TrapEventTypeName_Type()
)
trapEventTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeName.setStatus("mandatory")


class _TrapIncludedValue_Type(Integer32):
    """Custom type trapIncludedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_TrapIncludedValue_Type.__name__ = "Integer32"
_TrapIncludedValue_Object = MibScalar
trapIncludedValue = _TrapIncludedValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 6),
    _TrapIncludedValue_Type()
)
trapIncludedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedValue.setStatus("mandatory")
_TrapIncludedString_Type = DisplayString
_TrapIncludedString_Object = MibScalar
trapIncludedString = _TrapIncludedString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 7),
    _TrapIncludedString_Type()
)
trapIncludedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedString.setStatus("mandatory")
_TrapEventClassNumber_Type = Integer32
_TrapEventClassNumber_Object = MibScalar
trapEventClassNumber = _TrapEventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 9),
    _TrapEventClassNumber_Type()
)
trapEventClassNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventClassNumber.setStatus("mandatory")
_TrapEventClassName_Type = Integer32
_TrapEventClassName_Object = MibScalar
trapEventClassName = _TrapEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 3, 10),
    _TrapEventClassName_Type()
)
trapEventClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventClassName.setStatus("mandatory")
_TechSupport_ObjectIdentity = ObjectIdentity
techSupport = _TechSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99)
)
_TechSupport1_Type = Integer32
_TechSupport1_Object = MibScalar
techSupport1 = _TechSupport1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 1),
    _TechSupport1_Type()
)
techSupport1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport1.setStatus("mandatory")
_TechSupport2_ObjectIdentity = ObjectIdentity
techSupport2 = _TechSupport2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 2)
)
_TechSupport2n1_Type = Integer32
_TechSupport2n1_Object = MibScalar
techSupport2n1 = _TechSupport2n1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 2, 1),
    _TechSupport2n1_Type()
)
techSupport2n1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport2n1.setStatus("mandatory")
_TechSupport2n2_Type = Integer32
_TechSupport2n2_Object = MibScalar
techSupport2n2 = _TechSupport2n2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 2, 2),
    _TechSupport2n2_Type()
)
techSupport2n2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport2n2.setStatus("mandatory")
_TechSupport3_ObjectIdentity = ObjectIdentity
techSupport3 = _TechSupport3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3)
)
_TechSupport3n1_Type = Integer32
_TechSupport3n1_Object = MibScalar
techSupport3n1 = _TechSupport3n1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3, 1),
    _TechSupport3n1_Type()
)
techSupport3n1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport3n1.setStatus("mandatory")
_TechSupport3n2_Type = Integer32
_TechSupport3n2_Object = MibScalar
techSupport3n2 = _TechSupport3n2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3, 2),
    _TechSupport3n2_Type()
)
techSupport3n2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport3n2.setStatus("mandatory")
_TechSupport3n3_Type = Integer32
_TechSupport3n3_Object = MibScalar
techSupport3n3 = _TechSupport3n3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3, 3),
    _TechSupport3n3_Type()
)
techSupport3n3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport3n3.setStatus("mandatory")
_TechSupport3n4_Type = Integer32
_TechSupport3n4_Object = MibScalar
techSupport3n4 = _TechSupport3n4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3, 4),
    _TechSupport3n4_Type()
)
techSupport3n4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport3n4.setStatus("mandatory")
_TechSupport3n5_Type = Integer32
_TechSupport3n5_Object = MibScalar
techSupport3n5 = _TechSupport3n5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 3, 5),
    _TechSupport3n5_Type()
)
techSupport3n5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport3n5.setStatus("mandatory")
_TechSupport4_Type = Integer32
_TechSupport4_Object = MibScalar
techSupport4 = _TechSupport4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 4),
    _TechSupport4_Type()
)
techSupport4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport4.setStatus("mandatory")
_TechSupport7_Type = Integer32
_TechSupport7_Object = MibScalar
techSupport7 = _TechSupport7_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 7),
    _TechSupport7_Type()
)
techSupport7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport7.setStatus("mandatory")
_TechSupport9_Type = Integer32
_TechSupport9_Object = MibScalar
techSupport9 = _TechSupport9_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 9),
    _TechSupport9_Type()
)
techSupport9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport9.setStatus("mandatory")
_TechSupport10_Type = DisplayString
_TechSupport10_Object = MibScalar
techSupport10 = _TechSupport10_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 10),
    _TechSupport10_Type()
)
techSupport10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport10.setStatus("mandatory")
_TechSupport11_Type = Integer32
_TechSupport11_Object = MibScalar
techSupport11 = _TechSupport11_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 11),
    _TechSupport11_Type()
)
techSupport11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport11.setStatus("mandatory")
_TechSupport16_Type = Integer32
_TechSupport16_Object = MibScalar
techSupport16 = _TechSupport16_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 16),
    _TechSupport16_Type()
)
techSupport16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport16.setStatus("mandatory")
_TechSupport17_Type = Integer32
_TechSupport17_Object = MibScalar
techSupport17 = _TechSupport17_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 17),
    _TechSupport17_Type()
)
techSupport17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport17.setStatus("mandatory")
_TechSupport18_Type = Integer32
_TechSupport18_Object = MibScalar
techSupport18 = _TechSupport18_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 18),
    _TechSupport18_Type()
)
techSupport18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport18.setStatus("mandatory")
_TechSupport19_Type = DisplayString
_TechSupport19_Object = MibScalar
techSupport19 = _TechSupport19_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 19),
    _TechSupport19_Type()
)
techSupport19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport19.setStatus("mandatory")
_TechSupport20Table_Object = MibTable
techSupport20Table = _TechSupport20Table_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 20)
)
if mibBuilder.loadTexts:
    techSupport20Table.setStatus("mandatory")
_TechSupport20Entry_Object = MibTableRow
techSupport20Entry = _TechSupport20Entry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 20, 1)
)
techSupport20Entry.setIndexNames(
    (0, "SL81-STD-MIB", "techSupport20Index"),
)
if mibBuilder.loadTexts:
    techSupport20Entry.setStatus("mandatory")
_TechSupport20Index_Type = Integer32
_TechSupport20Index_Object = MibTableColumn
techSupport20Index = _TechSupport20Index_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 20, 1, 1),
    _TechSupport20Index_Type()
)
techSupport20Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    techSupport20Index.setStatus("mandatory")
_TechSupport20_Type = DisplayString
_TechSupport20_Object = MibTableColumn
techSupport20 = _TechSupport20_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 20, 1, 2),
    _TechSupport20_Type()
)
techSupport20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport20.setStatus("mandatory")
_TechSupport21Table_Object = MibTable
techSupport21Table = _TechSupport21Table_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 21)
)
if mibBuilder.loadTexts:
    techSupport21Table.setStatus("mandatory")
_TechSupport21Entry_Object = MibTableRow
techSupport21Entry = _TechSupport21Entry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 21, 1)
)
techSupport21Entry.setIndexNames(
    (0, "SL81-STD-MIB", "techSupport21Index"),
)
if mibBuilder.loadTexts:
    techSupport21Entry.setStatus("mandatory")
_TechSupport21Index_Type = Integer32
_TechSupport21Index_Object = MibTableColumn
techSupport21Index = _TechSupport21Index_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 21, 1, 1),
    _TechSupport21Index_Type()
)
techSupport21Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    techSupport21Index.setStatus("mandatory")
_TechSupport21_Type = Integer32
_TechSupport21_Object = MibTableColumn
techSupport21 = _TechSupport21_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 21, 1, 2),
    _TechSupport21_Type()
)
techSupport21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    techSupport21.setStatus("mandatory")
_TechSupport22_Type = Integer32
_TechSupport22_Object = MibScalar
techSupport22 = _TechSupport22_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 22),
    _TechSupport22_Type()
)
techSupport22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport22.setStatus("mandatory")
_TechSupport24_Type = DisplayString
_TechSupport24_Object = MibScalar
techSupport24 = _TechSupport24_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 24),
    _TechSupport24_Type()
)
techSupport24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport24.setStatus("mandatory")
_TechSupport25_Type = DisplayString
_TechSupport25_Object = MibScalar
techSupport25 = _TechSupport25_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 25),
    _TechSupport25_Type()
)
techSupport25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport25.setStatus("mandatory")
_TechSupport26_Type = DisplayString
_TechSupport26_Object = MibScalar
techSupport26 = _TechSupport26_Object(
    (1, 3, 6, 1, 4, 1, 3052, 5, 99, 26),
    _TechSupport26_Type()
)
techSupport26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techSupport26.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sl81TestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1)
)
sl81TestTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81TestTrap.setStatus(
        ""
    )

sl81StockESDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 50)
)
sl81StockESDisconnectTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockESDisconnectTrap.setStatus(
        ""
    )

sl81StockDataEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 100)
)
sl81StockDataEventTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockDataEventTrap.setStatus(
        ""
    )

sl81StockContactClosureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 110)
)
sl81StockContactClosureTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockContactClosureTrap.setStatus(
        ""
    )

sl81StockTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 120)
)
sl81StockTempTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockTempTrap.setStatus(
        ""
    )

sl81StockHumidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 130)
)
sl81StockHumidityTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockHumidityTrap.setStatus(
        ""
    )

sl81StockAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 140)
)
sl81StockAnalogTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockAnalogTrap.setStatus(
        ""
    )

sl81StockCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 160)
)
sl81StockCTSTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockCTSTrap.setStatus(
        ""
    )

sl81StockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 170)
)
sl81StockSchedTrap.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    sl81StockSchedTrap.setStatus(
        ""
    )

sl81UserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1000)
)
sl81UserTrap1000.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1000.setStatus(
        ""
    )

sl81UserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1001)
)
sl81UserTrap1001.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1001.setStatus(
        ""
    )

sl81UserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1002)
)
sl81UserTrap1002.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1002.setStatus(
        ""
    )

sl81UserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1003)
)
sl81UserTrap1003.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1003.setStatus(
        ""
    )

sl81UserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1004)
)
sl81UserTrap1004.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1004.setStatus(
        ""
    )

sl81UserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1005)
)
sl81UserTrap1005.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1005.setStatus(
        ""
    )

sl81UserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1006)
)
sl81UserTrap1006.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1006.setStatus(
        ""
    )

sl81UserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1007)
)
sl81UserTrap1007.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1007.setStatus(
        ""
    )

sl81UserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1008)
)
sl81UserTrap1008.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1008.setStatus(
        ""
    )

sl81UserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1009)
)
sl81UserTrap1009.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1009.setStatus(
        ""
    )

sl81UserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1010)
)
sl81UserTrap1010.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1010.setStatus(
        ""
    )

sl81UserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1011)
)
sl81UserTrap1011.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1011.setStatus(
        ""
    )

sl81UserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1012)
)
sl81UserTrap1012.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1012.setStatus(
        ""
    )

sl81UserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1013)
)
sl81UserTrap1013.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1013.setStatus(
        ""
    )

sl81UserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1014)
)
sl81UserTrap1014.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1014.setStatus(
        ""
    )

sl81UserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1015)
)
sl81UserTrap1015.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1015.setStatus(
        ""
    )

sl81UserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1016)
)
sl81UserTrap1016.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1016.setStatus(
        ""
    )

sl81UserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1017)
)
sl81UserTrap1017.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1017.setStatus(
        ""
    )

sl81UserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1018)
)
sl81UserTrap1018.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1018.setStatus(
        ""
    )

sl81UserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1019)
)
sl81UserTrap1019.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1019.setStatus(
        ""
    )

sl81UserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1020)
)
sl81UserTrap1020.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1020.setStatus(
        ""
    )

sl81UserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1021)
)
sl81UserTrap1021.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1021.setStatus(
        ""
    )

sl81UserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1022)
)
sl81UserTrap1022.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1022.setStatus(
        ""
    )

sl81UserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1023)
)
sl81UserTrap1023.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1023.setStatus(
        ""
    )

sl81UserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1024)
)
sl81UserTrap1024.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1024.setStatus(
        ""
    )

sl81UserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1025)
)
sl81UserTrap1025.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1025.setStatus(
        ""
    )

sl81UserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1026)
)
sl81UserTrap1026.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1026.setStatus(
        ""
    )

sl81UserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1027)
)
sl81UserTrap1027.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1027.setStatus(
        ""
    )

sl81UserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1028)
)
sl81UserTrap1028.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1028.setStatus(
        ""
    )

sl81UserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1029)
)
sl81UserTrap1029.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1029.setStatus(
        ""
    )

sl81UserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1030)
)
sl81UserTrap1030.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1030.setStatus(
        ""
    )

sl81UserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1031)
)
sl81UserTrap1031.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1031.setStatus(
        ""
    )

sl81UserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1032)
)
sl81UserTrap1032.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1032.setStatus(
        ""
    )

sl81UserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1033)
)
sl81UserTrap1033.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1033.setStatus(
        ""
    )

sl81UserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1034)
)
sl81UserTrap1034.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1034.setStatus(
        ""
    )

sl81UserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1035)
)
sl81UserTrap1035.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1035.setStatus(
        ""
    )

sl81UserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1036)
)
sl81UserTrap1036.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1036.setStatus(
        ""
    )

sl81UserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1037)
)
sl81UserTrap1037.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1037.setStatus(
        ""
    )

sl81UserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1038)
)
sl81UserTrap1038.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1038.setStatus(
        ""
    )

sl81UserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1039)
)
sl81UserTrap1039.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1039.setStatus(
        ""
    )

sl81UserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1040)
)
sl81UserTrap1040.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1040.setStatus(
        ""
    )

sl81UserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1041)
)
sl81UserTrap1041.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1041.setStatus(
        ""
    )

sl81UserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1042)
)
sl81UserTrap1042.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1042.setStatus(
        ""
    )

sl81UserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1043)
)
sl81UserTrap1043.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1043.setStatus(
        ""
    )

sl81UserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1044)
)
sl81UserTrap1044.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1044.setStatus(
        ""
    )

sl81UserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1045)
)
sl81UserTrap1045.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1045.setStatus(
        ""
    )

sl81UserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1046)
)
sl81UserTrap1046.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1046.setStatus(
        ""
    )

sl81UserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1047)
)
sl81UserTrap1047.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1047.setStatus(
        ""
    )

sl81UserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1048)
)
sl81UserTrap1048.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1048.setStatus(
        ""
    )

sl81UserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1049)
)
sl81UserTrap1049.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1049.setStatus(
        ""
    )

sl81UserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1050)
)
sl81UserTrap1050.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1050.setStatus(
        ""
    )

sl81UserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1051)
)
sl81UserTrap1051.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1051.setStatus(
        ""
    )

sl81UserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1052)
)
sl81UserTrap1052.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1052.setStatus(
        ""
    )

sl81UserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1053)
)
sl81UserTrap1053.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1053.setStatus(
        ""
    )

sl81UserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1054)
)
sl81UserTrap1054.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1054.setStatus(
        ""
    )

sl81UserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1055)
)
sl81UserTrap1055.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1055.setStatus(
        ""
    )

sl81UserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1056)
)
sl81UserTrap1056.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1056.setStatus(
        ""
    )

sl81UserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1057)
)
sl81UserTrap1057.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1057.setStatus(
        ""
    )

sl81UserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1058)
)
sl81UserTrap1058.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1058.setStatus(
        ""
    )

sl81UserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1059)
)
sl81UserTrap1059.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1059.setStatus(
        ""
    )

sl81UserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1060)
)
sl81UserTrap1060.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1060.setStatus(
        ""
    )

sl81UserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1061)
)
sl81UserTrap1061.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1061.setStatus(
        ""
    )

sl81UserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1062)
)
sl81UserTrap1062.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1062.setStatus(
        ""
    )

sl81UserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1063)
)
sl81UserTrap1063.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1063.setStatus(
        ""
    )

sl81UserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1064)
)
sl81UserTrap1064.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1064.setStatus(
        ""
    )

sl81UserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1065)
)
sl81UserTrap1065.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1065.setStatus(
        ""
    )

sl81UserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1066)
)
sl81UserTrap1066.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1066.setStatus(
        ""
    )

sl81UserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1067)
)
sl81UserTrap1067.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1067.setStatus(
        ""
    )

sl81UserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1068)
)
sl81UserTrap1068.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1068.setStatus(
        ""
    )

sl81UserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1069)
)
sl81UserTrap1069.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1069.setStatus(
        ""
    )

sl81UserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1070)
)
sl81UserTrap1070.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1070.setStatus(
        ""
    )

sl81UserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1071)
)
sl81UserTrap1071.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1071.setStatus(
        ""
    )

sl81UserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1072)
)
sl81UserTrap1072.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1072.setStatus(
        ""
    )

sl81UserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1073)
)
sl81UserTrap1073.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1073.setStatus(
        ""
    )

sl81UserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1074)
)
sl81UserTrap1074.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1074.setStatus(
        ""
    )

sl81UserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1075)
)
sl81UserTrap1075.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1075.setStatus(
        ""
    )

sl81UserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1076)
)
sl81UserTrap1076.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1076.setStatus(
        ""
    )

sl81UserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1077)
)
sl81UserTrap1077.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1077.setStatus(
        ""
    )

sl81UserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1078)
)
sl81UserTrap1078.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1078.setStatus(
        ""
    )

sl81UserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1079)
)
sl81UserTrap1079.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1079.setStatus(
        ""
    )

sl81UserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1080)
)
sl81UserTrap1080.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1080.setStatus(
        ""
    )

sl81UserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1081)
)
sl81UserTrap1081.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1081.setStatus(
        ""
    )

sl81UserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1082)
)
sl81UserTrap1082.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1082.setStatus(
        ""
    )

sl81UserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1083)
)
sl81UserTrap1083.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1083.setStatus(
        ""
    )

sl81UserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1084)
)
sl81UserTrap1084.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1084.setStatus(
        ""
    )

sl81UserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1085)
)
sl81UserTrap1085.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1085.setStatus(
        ""
    )

sl81UserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1086)
)
sl81UserTrap1086.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1086.setStatus(
        ""
    )

sl81UserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1087)
)
sl81UserTrap1087.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1087.setStatus(
        ""
    )

sl81UserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1088)
)
sl81UserTrap1088.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1088.setStatus(
        ""
    )

sl81UserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1089)
)
sl81UserTrap1089.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1089.setStatus(
        ""
    )

sl81UserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1090)
)
sl81UserTrap1090.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1090.setStatus(
        ""
    )

sl81UserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1091)
)
sl81UserTrap1091.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1091.setStatus(
        ""
    )

sl81UserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1092)
)
sl81UserTrap1092.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1092.setStatus(
        ""
    )

sl81UserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1093)
)
sl81UserTrap1093.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1093.setStatus(
        ""
    )

sl81UserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1094)
)
sl81UserTrap1094.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1094.setStatus(
        ""
    )

sl81UserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1095)
)
sl81UserTrap1095.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1095.setStatus(
        ""
    )

sl81UserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1096)
)
sl81UserTrap1096.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1096.setStatus(
        ""
    )

sl81UserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1097)
)
sl81UserTrap1097.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1097.setStatus(
        ""
    )

sl81UserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1098)
)
sl81UserTrap1098.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1098.setStatus(
        ""
    )

sl81UserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1099)
)
sl81UserTrap1099.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1099.setStatus(
        ""
    )

sl81UserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1100)
)
sl81UserTrap1100.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1100.setStatus(
        ""
    )

sl81UserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1101)
)
sl81UserTrap1101.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1101.setStatus(
        ""
    )

sl81UserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1102)
)
sl81UserTrap1102.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1102.setStatus(
        ""
    )

sl81UserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1103)
)
sl81UserTrap1103.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1103.setStatus(
        ""
    )

sl81UserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1104)
)
sl81UserTrap1104.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1104.setStatus(
        ""
    )

sl81UserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1105)
)
sl81UserTrap1105.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1105.setStatus(
        ""
    )

sl81UserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1106)
)
sl81UserTrap1106.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1106.setStatus(
        ""
    )

sl81UserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1107)
)
sl81UserTrap1107.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1107.setStatus(
        ""
    )

sl81UserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1108)
)
sl81UserTrap1108.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1108.setStatus(
        ""
    )

sl81UserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1109)
)
sl81UserTrap1109.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1109.setStatus(
        ""
    )

sl81UserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1110)
)
sl81UserTrap1110.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1110.setStatus(
        ""
    )

sl81UserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1111)
)
sl81UserTrap1111.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1111.setStatus(
        ""
    )

sl81UserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1112)
)
sl81UserTrap1112.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1112.setStatus(
        ""
    )

sl81UserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1113)
)
sl81UserTrap1113.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1113.setStatus(
        ""
    )

sl81UserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1114)
)
sl81UserTrap1114.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1114.setStatus(
        ""
    )

sl81UserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1115)
)
sl81UserTrap1115.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1115.setStatus(
        ""
    )

sl81UserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1116)
)
sl81UserTrap1116.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1116.setStatus(
        ""
    )

sl81UserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1117)
)
sl81UserTrap1117.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1117.setStatus(
        ""
    )

sl81UserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1118)
)
sl81UserTrap1118.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1118.setStatus(
        ""
    )

sl81UserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1119)
)
sl81UserTrap1119.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1119.setStatus(
        ""
    )

sl81UserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1120)
)
sl81UserTrap1120.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1120.setStatus(
        ""
    )

sl81UserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1121)
)
sl81UserTrap1121.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1121.setStatus(
        ""
    )

sl81UserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1122)
)
sl81UserTrap1122.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1122.setStatus(
        ""
    )

sl81UserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1123)
)
sl81UserTrap1123.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1123.setStatus(
        ""
    )

sl81UserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1124)
)
sl81UserTrap1124.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1124.setStatus(
        ""
    )

sl81UserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1125)
)
sl81UserTrap1125.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1125.setStatus(
        ""
    )

sl81UserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1126)
)
sl81UserTrap1126.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1126.setStatus(
        ""
    )

sl81UserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1127)
)
sl81UserTrap1127.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1127.setStatus(
        ""
    )

sl81UserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1128)
)
sl81UserTrap1128.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1128.setStatus(
        ""
    )

sl81UserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1129)
)
sl81UserTrap1129.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1129.setStatus(
        ""
    )

sl81UserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1130)
)
sl81UserTrap1130.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1130.setStatus(
        ""
    )

sl81UserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1131)
)
sl81UserTrap1131.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1131.setStatus(
        ""
    )

sl81UserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1132)
)
sl81UserTrap1132.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1132.setStatus(
        ""
    )

sl81UserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1133)
)
sl81UserTrap1133.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1133.setStatus(
        ""
    )

sl81UserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1134)
)
sl81UserTrap1134.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1134.setStatus(
        ""
    )

sl81UserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1135)
)
sl81UserTrap1135.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1135.setStatus(
        ""
    )

sl81UserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1136)
)
sl81UserTrap1136.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1136.setStatus(
        ""
    )

sl81UserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1137)
)
sl81UserTrap1137.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1137.setStatus(
        ""
    )

sl81UserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1138)
)
sl81UserTrap1138.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1138.setStatus(
        ""
    )

sl81UserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1139)
)
sl81UserTrap1139.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1139.setStatus(
        ""
    )

sl81UserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1140)
)
sl81UserTrap1140.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1140.setStatus(
        ""
    )

sl81UserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1141)
)
sl81UserTrap1141.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1141.setStatus(
        ""
    )

sl81UserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1142)
)
sl81UserTrap1142.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1142.setStatus(
        ""
    )

sl81UserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1143)
)
sl81UserTrap1143.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1143.setStatus(
        ""
    )

sl81UserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1144)
)
sl81UserTrap1144.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1144.setStatus(
        ""
    )

sl81UserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1145)
)
sl81UserTrap1145.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1145.setStatus(
        ""
    )

sl81UserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1146)
)
sl81UserTrap1146.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1146.setStatus(
        ""
    )

sl81UserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1147)
)
sl81UserTrap1147.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1147.setStatus(
        ""
    )

sl81UserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1148)
)
sl81UserTrap1148.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1148.setStatus(
        ""
    )

sl81UserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1149)
)
sl81UserTrap1149.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1149.setStatus(
        ""
    )

sl81UserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1150)
)
sl81UserTrap1150.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1150.setStatus(
        ""
    )

sl81UserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1151)
)
sl81UserTrap1151.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1151.setStatus(
        ""
    )

sl81UserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1152)
)
sl81UserTrap1152.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1152.setStatus(
        ""
    )

sl81UserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1153)
)
sl81UserTrap1153.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1153.setStatus(
        ""
    )

sl81UserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1154)
)
sl81UserTrap1154.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1154.setStatus(
        ""
    )

sl81UserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1155)
)
sl81UserTrap1155.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1155.setStatus(
        ""
    )

sl81UserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1156)
)
sl81UserTrap1156.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1156.setStatus(
        ""
    )

sl81UserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1157)
)
sl81UserTrap1157.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1157.setStatus(
        ""
    )

sl81UserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1158)
)
sl81UserTrap1158.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1158.setStatus(
        ""
    )

sl81UserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1159)
)
sl81UserTrap1159.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1159.setStatus(
        ""
    )

sl81UserTrap1160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1160)
)
sl81UserTrap1160.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1160.setStatus(
        ""
    )

sl81UserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1161)
)
sl81UserTrap1161.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1161.setStatus(
        ""
    )

sl81UserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1162)
)
sl81UserTrap1162.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1162.setStatus(
        ""
    )

sl81UserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1163)
)
sl81UserTrap1163.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1163.setStatus(
        ""
    )

sl81UserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1164)
)
sl81UserTrap1164.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1164.setStatus(
        ""
    )

sl81UserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1165)
)
sl81UserTrap1165.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1165.setStatus(
        ""
    )

sl81UserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1166)
)
sl81UserTrap1166.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1166.setStatus(
        ""
    )

sl81UserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1167)
)
sl81UserTrap1167.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1167.setStatus(
        ""
    )

sl81UserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1168)
)
sl81UserTrap1168.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1168.setStatus(
        ""
    )

sl81UserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1169)
)
sl81UserTrap1169.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1169.setStatus(
        ""
    )

sl81UserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1170)
)
sl81UserTrap1170.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1170.setStatus(
        ""
    )

sl81UserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1171)
)
sl81UserTrap1171.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1171.setStatus(
        ""
    )

sl81UserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1172)
)
sl81UserTrap1172.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1172.setStatus(
        ""
    )

sl81UserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1173)
)
sl81UserTrap1173.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1173.setStatus(
        ""
    )

sl81UserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1174)
)
sl81UserTrap1174.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1174.setStatus(
        ""
    )

sl81UserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1175)
)
sl81UserTrap1175.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1175.setStatus(
        ""
    )

sl81UserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1176)
)
sl81UserTrap1176.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1176.setStatus(
        ""
    )

sl81UserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1177)
)
sl81UserTrap1177.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1177.setStatus(
        ""
    )

sl81UserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1178)
)
sl81UserTrap1178.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1178.setStatus(
        ""
    )

sl81UserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1179)
)
sl81UserTrap1179.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1179.setStatus(
        ""
    )

sl81UserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1180)
)
sl81UserTrap1180.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1180.setStatus(
        ""
    )

sl81UserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1181)
)
sl81UserTrap1181.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1181.setStatus(
        ""
    )

sl81UserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1182)
)
sl81UserTrap1182.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1182.setStatus(
        ""
    )

sl81UserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1183)
)
sl81UserTrap1183.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1183.setStatus(
        ""
    )

sl81UserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1184)
)
sl81UserTrap1184.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1184.setStatus(
        ""
    )

sl81UserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1185)
)
sl81UserTrap1185.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1185.setStatus(
        ""
    )

sl81UserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1186)
)
sl81UserTrap1186.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1186.setStatus(
        ""
    )

sl81UserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1187)
)
sl81UserTrap1187.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1187.setStatus(
        ""
    )

sl81UserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1188)
)
sl81UserTrap1188.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1188.setStatus(
        ""
    )

sl81UserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1189)
)
sl81UserTrap1189.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1189.setStatus(
        ""
    )

sl81UserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1190)
)
sl81UserTrap1190.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1190.setStatus(
        ""
    )

sl81UserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1191)
)
sl81UserTrap1191.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1191.setStatus(
        ""
    )

sl81UserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1192)
)
sl81UserTrap1192.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1192.setStatus(
        ""
    )

sl81UserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1193)
)
sl81UserTrap1193.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1193.setStatus(
        ""
    )

sl81UserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1194)
)
sl81UserTrap1194.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1194.setStatus(
        ""
    )

sl81UserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1195)
)
sl81UserTrap1195.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1195.setStatus(
        ""
    )

sl81UserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1196)
)
sl81UserTrap1196.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1196.setStatus(
        ""
    )

sl81UserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1197)
)
sl81UserTrap1197.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1197.setStatus(
        ""
    )

sl81UserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1198)
)
sl81UserTrap1198.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1198.setStatus(
        ""
    )

sl81UserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 5, 0, 1199)
)
sl81UserTrap1199.setObjects(
      *(("SL81-STD-MIB", "siteID"),
        ("SL81-STD-MIB", "esIndex"),
        ("SL81-STD-MIB", "esName"),
        ("SL81-STD-MIB", "trapEventTypeNumber"),
        ("SL81-STD-MIB", "trapEventTypeName"),
        ("SL81-STD-MIB", "esIndexPoint"),
        ("SL81-STD-MIB", "esPointName"),
        ("SL81-STD-MIB", "esID"),
        ("SL81-STD-MIB", "clock"),
        ("SL81-STD-MIB", "trapIncludedValue"),
        ("SL81-STD-MIB", "trapIncludedString"),
        ("SL81-STD-MIB", "trapEventClassNumber"),
        ("SL81-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    sl81UserTrap1199.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL81-STD-MIB",
    **{"omnitronix": omnitronix,
       "sl81": sl81,
       "sl81TestTrap": sl81TestTrap,
       "sl81StockESDisconnectTrap": sl81StockESDisconnectTrap,
       "sl81StockDataEventTrap": sl81StockDataEventTrap,
       "sl81StockContactClosureTrap": sl81StockContactClosureTrap,
       "sl81StockTempTrap": sl81StockTempTrap,
       "sl81StockHumidityTrap": sl81StockHumidityTrap,
       "sl81StockAnalogTrap": sl81StockAnalogTrap,
       "sl81StockCTSTrap": sl81StockCTSTrap,
       "sl81StockSchedTrap": sl81StockSchedTrap,
       "sl81UserTrap1000": sl81UserTrap1000,
       "sl81UserTrap1001": sl81UserTrap1001,
       "sl81UserTrap1002": sl81UserTrap1002,
       "sl81UserTrap1003": sl81UserTrap1003,
       "sl81UserTrap1004": sl81UserTrap1004,
       "sl81UserTrap1005": sl81UserTrap1005,
       "sl81UserTrap1006": sl81UserTrap1006,
       "sl81UserTrap1007": sl81UserTrap1007,
       "sl81UserTrap1008": sl81UserTrap1008,
       "sl81UserTrap1009": sl81UserTrap1009,
       "sl81UserTrap1010": sl81UserTrap1010,
       "sl81UserTrap1011": sl81UserTrap1011,
       "sl81UserTrap1012": sl81UserTrap1012,
       "sl81UserTrap1013": sl81UserTrap1013,
       "sl81UserTrap1014": sl81UserTrap1014,
       "sl81UserTrap1015": sl81UserTrap1015,
       "sl81UserTrap1016": sl81UserTrap1016,
       "sl81UserTrap1017": sl81UserTrap1017,
       "sl81UserTrap1018": sl81UserTrap1018,
       "sl81UserTrap1019": sl81UserTrap1019,
       "sl81UserTrap1020": sl81UserTrap1020,
       "sl81UserTrap1021": sl81UserTrap1021,
       "sl81UserTrap1022": sl81UserTrap1022,
       "sl81UserTrap1023": sl81UserTrap1023,
       "sl81UserTrap1024": sl81UserTrap1024,
       "sl81UserTrap1025": sl81UserTrap1025,
       "sl81UserTrap1026": sl81UserTrap1026,
       "sl81UserTrap1027": sl81UserTrap1027,
       "sl81UserTrap1028": sl81UserTrap1028,
       "sl81UserTrap1029": sl81UserTrap1029,
       "sl81UserTrap1030": sl81UserTrap1030,
       "sl81UserTrap1031": sl81UserTrap1031,
       "sl81UserTrap1032": sl81UserTrap1032,
       "sl81UserTrap1033": sl81UserTrap1033,
       "sl81UserTrap1034": sl81UserTrap1034,
       "sl81UserTrap1035": sl81UserTrap1035,
       "sl81UserTrap1036": sl81UserTrap1036,
       "sl81UserTrap1037": sl81UserTrap1037,
       "sl81UserTrap1038": sl81UserTrap1038,
       "sl81UserTrap1039": sl81UserTrap1039,
       "sl81UserTrap1040": sl81UserTrap1040,
       "sl81UserTrap1041": sl81UserTrap1041,
       "sl81UserTrap1042": sl81UserTrap1042,
       "sl81UserTrap1043": sl81UserTrap1043,
       "sl81UserTrap1044": sl81UserTrap1044,
       "sl81UserTrap1045": sl81UserTrap1045,
       "sl81UserTrap1046": sl81UserTrap1046,
       "sl81UserTrap1047": sl81UserTrap1047,
       "sl81UserTrap1048": sl81UserTrap1048,
       "sl81UserTrap1049": sl81UserTrap1049,
       "sl81UserTrap1050": sl81UserTrap1050,
       "sl81UserTrap1051": sl81UserTrap1051,
       "sl81UserTrap1052": sl81UserTrap1052,
       "sl81UserTrap1053": sl81UserTrap1053,
       "sl81UserTrap1054": sl81UserTrap1054,
       "sl81UserTrap1055": sl81UserTrap1055,
       "sl81UserTrap1056": sl81UserTrap1056,
       "sl81UserTrap1057": sl81UserTrap1057,
       "sl81UserTrap1058": sl81UserTrap1058,
       "sl81UserTrap1059": sl81UserTrap1059,
       "sl81UserTrap1060": sl81UserTrap1060,
       "sl81UserTrap1061": sl81UserTrap1061,
       "sl81UserTrap1062": sl81UserTrap1062,
       "sl81UserTrap1063": sl81UserTrap1063,
       "sl81UserTrap1064": sl81UserTrap1064,
       "sl81UserTrap1065": sl81UserTrap1065,
       "sl81UserTrap1066": sl81UserTrap1066,
       "sl81UserTrap1067": sl81UserTrap1067,
       "sl81UserTrap1068": sl81UserTrap1068,
       "sl81UserTrap1069": sl81UserTrap1069,
       "sl81UserTrap1070": sl81UserTrap1070,
       "sl81UserTrap1071": sl81UserTrap1071,
       "sl81UserTrap1072": sl81UserTrap1072,
       "sl81UserTrap1073": sl81UserTrap1073,
       "sl81UserTrap1074": sl81UserTrap1074,
       "sl81UserTrap1075": sl81UserTrap1075,
       "sl81UserTrap1076": sl81UserTrap1076,
       "sl81UserTrap1077": sl81UserTrap1077,
       "sl81UserTrap1078": sl81UserTrap1078,
       "sl81UserTrap1079": sl81UserTrap1079,
       "sl81UserTrap1080": sl81UserTrap1080,
       "sl81UserTrap1081": sl81UserTrap1081,
       "sl81UserTrap1082": sl81UserTrap1082,
       "sl81UserTrap1083": sl81UserTrap1083,
       "sl81UserTrap1084": sl81UserTrap1084,
       "sl81UserTrap1085": sl81UserTrap1085,
       "sl81UserTrap1086": sl81UserTrap1086,
       "sl81UserTrap1087": sl81UserTrap1087,
       "sl81UserTrap1088": sl81UserTrap1088,
       "sl81UserTrap1089": sl81UserTrap1089,
       "sl81UserTrap1090": sl81UserTrap1090,
       "sl81UserTrap1091": sl81UserTrap1091,
       "sl81UserTrap1092": sl81UserTrap1092,
       "sl81UserTrap1093": sl81UserTrap1093,
       "sl81UserTrap1094": sl81UserTrap1094,
       "sl81UserTrap1095": sl81UserTrap1095,
       "sl81UserTrap1096": sl81UserTrap1096,
       "sl81UserTrap1097": sl81UserTrap1097,
       "sl81UserTrap1098": sl81UserTrap1098,
       "sl81UserTrap1099": sl81UserTrap1099,
       "sl81UserTrap1100": sl81UserTrap1100,
       "sl81UserTrap1101": sl81UserTrap1101,
       "sl81UserTrap1102": sl81UserTrap1102,
       "sl81UserTrap1103": sl81UserTrap1103,
       "sl81UserTrap1104": sl81UserTrap1104,
       "sl81UserTrap1105": sl81UserTrap1105,
       "sl81UserTrap1106": sl81UserTrap1106,
       "sl81UserTrap1107": sl81UserTrap1107,
       "sl81UserTrap1108": sl81UserTrap1108,
       "sl81UserTrap1109": sl81UserTrap1109,
       "sl81UserTrap1110": sl81UserTrap1110,
       "sl81UserTrap1111": sl81UserTrap1111,
       "sl81UserTrap1112": sl81UserTrap1112,
       "sl81UserTrap1113": sl81UserTrap1113,
       "sl81UserTrap1114": sl81UserTrap1114,
       "sl81UserTrap1115": sl81UserTrap1115,
       "sl81UserTrap1116": sl81UserTrap1116,
       "sl81UserTrap1117": sl81UserTrap1117,
       "sl81UserTrap1118": sl81UserTrap1118,
       "sl81UserTrap1119": sl81UserTrap1119,
       "sl81UserTrap1120": sl81UserTrap1120,
       "sl81UserTrap1121": sl81UserTrap1121,
       "sl81UserTrap1122": sl81UserTrap1122,
       "sl81UserTrap1123": sl81UserTrap1123,
       "sl81UserTrap1124": sl81UserTrap1124,
       "sl81UserTrap1125": sl81UserTrap1125,
       "sl81UserTrap1126": sl81UserTrap1126,
       "sl81UserTrap1127": sl81UserTrap1127,
       "sl81UserTrap1128": sl81UserTrap1128,
       "sl81UserTrap1129": sl81UserTrap1129,
       "sl81UserTrap1130": sl81UserTrap1130,
       "sl81UserTrap1131": sl81UserTrap1131,
       "sl81UserTrap1132": sl81UserTrap1132,
       "sl81UserTrap1133": sl81UserTrap1133,
       "sl81UserTrap1134": sl81UserTrap1134,
       "sl81UserTrap1135": sl81UserTrap1135,
       "sl81UserTrap1136": sl81UserTrap1136,
       "sl81UserTrap1137": sl81UserTrap1137,
       "sl81UserTrap1138": sl81UserTrap1138,
       "sl81UserTrap1139": sl81UserTrap1139,
       "sl81UserTrap1140": sl81UserTrap1140,
       "sl81UserTrap1141": sl81UserTrap1141,
       "sl81UserTrap1142": sl81UserTrap1142,
       "sl81UserTrap1143": sl81UserTrap1143,
       "sl81UserTrap1144": sl81UserTrap1144,
       "sl81UserTrap1145": sl81UserTrap1145,
       "sl81UserTrap1146": sl81UserTrap1146,
       "sl81UserTrap1147": sl81UserTrap1147,
       "sl81UserTrap1148": sl81UserTrap1148,
       "sl81UserTrap1149": sl81UserTrap1149,
       "sl81UserTrap1150": sl81UserTrap1150,
       "sl81UserTrap1151": sl81UserTrap1151,
       "sl81UserTrap1152": sl81UserTrap1152,
       "sl81UserTrap1153": sl81UserTrap1153,
       "sl81UserTrap1154": sl81UserTrap1154,
       "sl81UserTrap1155": sl81UserTrap1155,
       "sl81UserTrap1156": sl81UserTrap1156,
       "sl81UserTrap1157": sl81UserTrap1157,
       "sl81UserTrap1158": sl81UserTrap1158,
       "sl81UserTrap1159": sl81UserTrap1159,
       "sl81UserTrap1160": sl81UserTrap1160,
       "sl81UserTrap1161": sl81UserTrap1161,
       "sl81UserTrap1162": sl81UserTrap1162,
       "sl81UserTrap1163": sl81UserTrap1163,
       "sl81UserTrap1164": sl81UserTrap1164,
       "sl81UserTrap1165": sl81UserTrap1165,
       "sl81UserTrap1166": sl81UserTrap1166,
       "sl81UserTrap1167": sl81UserTrap1167,
       "sl81UserTrap1168": sl81UserTrap1168,
       "sl81UserTrap1169": sl81UserTrap1169,
       "sl81UserTrap1170": sl81UserTrap1170,
       "sl81UserTrap1171": sl81UserTrap1171,
       "sl81UserTrap1172": sl81UserTrap1172,
       "sl81UserTrap1173": sl81UserTrap1173,
       "sl81UserTrap1174": sl81UserTrap1174,
       "sl81UserTrap1175": sl81UserTrap1175,
       "sl81UserTrap1176": sl81UserTrap1176,
       "sl81UserTrap1177": sl81UserTrap1177,
       "sl81UserTrap1178": sl81UserTrap1178,
       "sl81UserTrap1179": sl81UserTrap1179,
       "sl81UserTrap1180": sl81UserTrap1180,
       "sl81UserTrap1181": sl81UserTrap1181,
       "sl81UserTrap1182": sl81UserTrap1182,
       "sl81UserTrap1183": sl81UserTrap1183,
       "sl81UserTrap1184": sl81UserTrap1184,
       "sl81UserTrap1185": sl81UserTrap1185,
       "sl81UserTrap1186": sl81UserTrap1186,
       "sl81UserTrap1187": sl81UserTrap1187,
       "sl81UserTrap1188": sl81UserTrap1188,
       "sl81UserTrap1189": sl81UserTrap1189,
       "sl81UserTrap1190": sl81UserTrap1190,
       "sl81UserTrap1191": sl81UserTrap1191,
       "sl81UserTrap1192": sl81UserTrap1192,
       "sl81UserTrap1193": sl81UserTrap1193,
       "sl81UserTrap1194": sl81UserTrap1194,
       "sl81UserTrap1195": sl81UserTrap1195,
       "sl81UserTrap1196": sl81UserTrap1196,
       "sl81UserTrap1197": sl81UserTrap1197,
       "sl81UserTrap1198": sl81UserTrap1198,
       "sl81UserTrap1199": sl81UserTrap1199,
       "status": status,
       "eventSensorStatus": eventSensorStatus,
       "esPointTable": esPointTable,
       "esPointEntry": esPointEntry,
       "esIndexES": esIndexES,
       "esIndexPC": esIndexPC,
       "esIndexPoint": esIndexPoint,
       "esPointName": esPointName,
       "esPointInEventState": esPointInEventState,
       "esPointValueInt": esPointValueInt,
       "esPointValueStr": esPointValueStr,
       "esPointTimeLastChange": esPointTimeLastChange,
       "esPointTimetickLastChange": esPointTimetickLastChange,
       "dataEventStatus": dataEventStatus,
       "deStatusTable": deStatusTable,
       "deStatusEntry": deStatusEntry,
       "deStatusIndex": deStatusIndex,
       "deStatusName": deStatusName,
       "deStatusCounter": deStatusCounter,
       "deStatusThreshold": deStatusThreshold,
       "deStatusLastTriggerTime": deStatusLastTriggerTime,
       "deStatusLastTriggerData": deStatusLastTriggerData,
       "config": config,
       "eventSensorBasics": eventSensorBasics,
       "esNumberEventSensors": esNumberEventSensors,
       "esTable": esTable,
       "esEntry": esEntry,
       "esIndex": esIndex,
       "esName": esName,
       "esID": esID,
       "esNumberTempSensors": esNumberTempSensors,
       "esTempReportingMode": esTempReportingMode,
       "esNumberCCs": esNumberCCs,
       "esCCReportingMode": esCCReportingMode,
       "esNumberHumidSensors": esNumberHumidSensors,
       "esHumidReportingMode": esHumidReportingMode,
       "esNumberNoiseSensors": esNumberNoiseSensors,
       "esNoiseReportingMode": esNoiseReportingMode,
       "esNumberAirflowSensors": esNumberAirflowSensors,
       "esAirflowReportingMode": esAirflowReportingMode,
       "esNumberAnalog": esNumberAnalog,
       "esAnalogReportingMode": esAnalogReportingMode,
       "esNumberRelayOutputs": esNumberRelayOutputs,
       "esRelayReportingMode": esRelayReportingMode,
       "dataEventConfig": dataEventConfig,
       "deFieldTable": deFieldTable,
       "deFieldEntry": deFieldEntry,
       "deFieldIndex": deFieldIndex,
       "deFieldStart": deFieldStart,
       "deFieldLength": deFieldLength,
       "deFieldName": deFieldName,
       "deConfigTable": deConfigTable,
       "deConfigEntry": deConfigEntry,
       "deConfigIndex": deConfigIndex,
       "deConfigEnabled": deConfigEnabled,
       "deConfigName": deConfigName,
       "deConfigEquation": deConfigEquation,
       "deConfigThreshold": deConfigThreshold,
       "deConfigClearMode": deConfigClearMode,
       "deConfigClearTime": deConfigClearTime,
       "deConfigAutoClear": deConfigAutoClear,
       "deConfigActions": deConfigActions,
       "deConfigTrapNumber": deConfigTrapNumber,
       "deConfigClass": deConfigClass,
       "serialPorts": serialPorts,
       "numberPorts": numberPorts,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigIndex": portConfigIndex,
       "portConfigBaud": portConfigBaud,
       "portConfigDataFormat": portConfigDataFormat,
       "portConfigStripPtOutputLfs": portConfigStripPtOutputLfs,
       "portConfigStripPtInputLfs": portConfigStripPtInputLfs,
       "portConfigDTRLowIdle": portConfigDTRLowIdle,
       "portConfigMaskEnable": portConfigMaskEnable,
       "portConfigDAEnable": portConfigDAEnable,
       "network": network,
       "ipConfigStatic": ipConfigStatic,
       "ipConfigAddress": ipConfigAddress,
       "ipConfigSubnetMask": ipConfigSubnetMask,
       "ipConfigDefaultRouter": ipConfigDefaultRouter,
       "ipConfigEngage": ipConfigEngage,
       "telnetDuplex": telnetDuplex,
       "modem": modem,
       "modemDataFormat": modemDataFormat,
       "modemUserSetup": modemUserSetup,
       "modemTAPSetup": modemTAPSetup,
       "modemTimeBetweenOutbound": modemTimeBetweenOutbound,
       "snmp": snmp,
       "smTable": smTable,
       "smEntry": smEntry,
       "smIndex": smIndex,
       "smAddress": smAddress,
       "pagers": pagers,
       "pagerRetries": pagerRetries,
       "pagerTable": pagerTable,
       "pagerEntry": pagerEntry,
       "pagerIndex": pagerIndex,
       "pagerType": pagerType,
       "pagerPhoneNumber": pagerPhoneNumber,
       "pagerID": pagerID,
       "pagerPostCalloutDelay": pagerPostCalloutDelay,
       "pagerIDDelay": pagerIDDelay,
       "time": time,
       "clock": clock,
       "autoDSTAdjust": autoDSTAdjust,
       "timeouts": timeouts,
       "commandTimeout": commandTimeout,
       "passthroughTimeout": passthroughTimeout,
       "productIds": productIds,
       "siteID": siteID,
       "thisProduct": thisProduct,
       "stockTrapString": stockTrapString,
       "trapEventTypeNumber": trapEventTypeNumber,
       "trapEventTypeName": trapEventTypeName,
       "trapIncludedValue": trapIncludedValue,
       "trapIncludedString": trapIncludedString,
       "trapEventClassNumber": trapEventClassNumber,
       "trapEventClassName": trapEventClassName,
       "techSupport": techSupport,
       "techSupport1": techSupport1,
       "techSupport2": techSupport2,
       "techSupport2n1": techSupport2n1,
       "techSupport2n2": techSupport2n2,
       "techSupport3": techSupport3,
       "techSupport3n1": techSupport3n1,
       "techSupport3n2": techSupport3n2,
       "techSupport3n3": techSupport3n3,
       "techSupport3n4": techSupport3n4,
       "techSupport3n5": techSupport3n5,
       "techSupport4": techSupport4,
       "techSupport7": techSupport7,
       "techSupport9": techSupport9,
       "techSupport10": techSupport10,
       "techSupport11": techSupport11,
       "techSupport16": techSupport16,
       "techSupport17": techSupport17,
       "techSupport18": techSupport18,
       "techSupport19": techSupport19,
       "techSupport20Table": techSupport20Table,
       "techSupport20Entry": techSupport20Entry,
       "techSupport20Index": techSupport20Index,
       "techSupport20": techSupport20,
       "techSupport21Table": techSupport21Table,
       "techSupport21Entry": techSupport21Entry,
       "techSupport21Index": techSupport21Index,
       "techSupport21": techSupport21,
       "techSupport22": techSupport22,
       "techSupport24": techSupport24,
       "techSupport25": techSupport25,
       "techSupport26": techSupport26}
)
