# SNMP MIB module (VEC-MIBv5-5) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VEC-MIBv5-5
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:07 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

vecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 885, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmersonESNA_ObjectIdentity = ObjectIdentity
emersonESNA = _EmersonESNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885)
)
_Vec_ObjectIdentity = ObjectIdentity
vec = _Vec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3)
)
_VecInformation_ObjectIdentity = ObjectIdentity
vecInformation = _VecInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 1)
)
_VecFirmwareVersion_Type = DisplayString
_VecFirmwareVersion_Object = MibScalar
vecFirmwareVersion = _VecFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 1),
    _VecFirmwareVersion_Type()
)
vecFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecFirmwareVersion.setStatus("mandatory")
_VecMessageStats_ObjectIdentity = ObjectIdentity
vecMessageStats = _VecMessageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2)
)
_VecMessageRequests_Type = Integer32
_VecMessageRequests_Object = MibScalar
vecMessageRequests = _VecMessageRequests_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 1),
    _VecMessageRequests_Type()
)
vecMessageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageRequests.setStatus("mandatory")
_VecMessageTransmissions_Type = Integer32
_VecMessageTransmissions_Object = MibScalar
vecMessageTransmissions = _VecMessageTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 2),
    _VecMessageTransmissions_Type()
)
vecMessageTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageTransmissions.setStatus("mandatory")
_VecMessageNoResponses_Type = Integer32
_VecMessageNoResponses_Object = MibScalar
vecMessageNoResponses = _VecMessageNoResponses_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 3),
    _VecMessageNoResponses_Type()
)
vecMessageNoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageNoResponses.setStatus("mandatory")
_VecMessageBadCRCs_Type = Integer32
_VecMessageBadCRCs_Object = MibScalar
vecMessageBadCRCs = _VecMessageBadCRCs_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 4),
    _VecMessageBadCRCs_Type()
)
vecMessageBadCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageBadCRCs.setStatus("mandatory")
_VecMessageLinkErrors_Type = Integer32
_VecMessageLinkErrors_Object = MibScalar
vecMessageLinkErrors = _VecMessageLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 5),
    _VecMessageLinkErrors_Type()
)
vecMessageLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageLinkErrors.setStatus("mandatory")
_VecMessagePartialResponses_Type = Integer32
_VecMessagePartialResponses_Object = MibScalar
vecMessagePartialResponses = _VecMessagePartialResponses_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 6),
    _VecMessagePartialResponses_Type()
)
vecMessagePartialResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessagePartialResponses.setStatus("mandatory")
_VecMessageWrongPackets_Type = Integer32
_VecMessageWrongPackets_Object = MibScalar
vecMessageWrongPackets = _VecMessageWrongPackets_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 7),
    _VecMessageWrongPackets_Type()
)
vecMessageWrongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageWrongPackets.setStatus("mandatory")
_VecMessageErrorReplies_Type = Integer32
_VecMessageErrorReplies_Object = MibScalar
vecMessageErrorReplies = _VecMessageErrorReplies_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 1, 2, 8),
    _VecMessageErrorReplies_Type()
)
vecMessageErrorReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vecMessageErrorReplies.setStatus("mandatory")
_PsStatus_ObjectIdentity = ObjectIdentity
psStatus = _PsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 2)
)
_PsMeasurement_ObjectIdentity = ObjectIdentity
psMeasurement = _PsMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1)
)
_PsSystemVoltage_Type = DisplayString
_PsSystemVoltage_Object = MibScalar
psSystemVoltage = _PsSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 1),
    _PsSystemVoltage_Type()
)
psSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSystemVoltage.setStatus("mandatory")
_PsSystemCurrent_Type = Integer32
_PsSystemCurrent_Object = MibScalar
psSystemCurrent = _PsSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 2),
    _PsSystemCurrent_Type()
)
psSystemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSystemCurrent.setStatus("mandatory")
_PsSubsystemVoltage_Type = DisplayString
_PsSubsystemVoltage_Object = MibScalar
psSubsystemVoltage = _PsSubsystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 3),
    _PsSubsystemVoltage_Type()
)
psSubsystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSubsystemVoltage.setStatus("mandatory")
_PsSubsystemCurrent_Type = Integer32
_PsSubsystemCurrent_Object = MibScalar
psSubsystemCurrent = _PsSubsystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 4),
    _PsSubsystemCurrent_Type()
)
psSubsystemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSubsystemCurrent.setStatus("mandatory")
_PsSenseVoltage_Type = DisplayString
_PsSenseVoltage_Object = MibScalar
psSenseVoltage = _PsSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 5),
    _PsSenseVoltage_Type()
)
psSenseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSenseVoltage.setStatus("mandatory")
_PsPCUTotalCurrent_Type = DisplayString
_PsPCUTotalCurrent_Object = MibScalar
psPCUTotalCurrent = _PsPCUTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 6),
    _PsPCUTotalCurrent_Type()
)
psPCUTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPCUTotalCurrent.setStatus("mandatory")
_PsBatteryCurrent_Type = DisplayString
_PsBatteryCurrent_Object = MibScalar
psBatteryCurrent = _PsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 7),
    _PsBatteryCurrent_Type()
)
psBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCurrent.setStatus("mandatory")
_PsBatteryReserveHours_Type = DisplayString
_PsBatteryReserveHours_Object = MibScalar
psBatteryReserveHours = _PsBatteryReserveHours_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 1, 8),
    _PsBatteryReserveHours_Type()
)
psBatteryReserveHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryReserveHours.setStatus("mandatory")
_PsTemperatureTable_Object = MibTable
psTemperatureTable = _PsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 2)
)
if mibBuilder.loadTexts:
    psTemperatureTable.setStatus("mandatory")
_PsTemperatureEntry_Object = MibTableRow
psTemperatureEntry = _PsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 2, 1)
)
psTemperatureEntry.setIndexNames(
    (0, "VEC-MIBv5-5", "psTemperatureIndex"),
)
if mibBuilder.loadTexts:
    psTemperatureEntry.setStatus("mandatory")
_PsTemperatureIndex_Type = Integer32
_PsTemperatureIndex_Object = MibTableColumn
psTemperatureIndex = _PsTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 2, 1, 1),
    _PsTemperatureIndex_Type()
)
psTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureIndex.setStatus("mandatory")
_PsTemperatureMeasurement_Type = DisplayString
_PsTemperatureMeasurement_Object = MibTableColumn
psTemperatureMeasurement = _PsTemperatureMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 2, 1, 2),
    _PsTemperatureMeasurement_Type()
)
psTemperatureMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureMeasurement.setStatus("mandatory")
_PsLVDTable_Object = MibTable
psLVDTable = _PsLVDTable_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 3)
)
if mibBuilder.loadTexts:
    psLVDTable.setStatus("mandatory")
_PsLVDEntry_Object = MibTableRow
psLVDEntry = _PsLVDEntry_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 3, 1)
)
psLVDEntry.setIndexNames(
    (0, "VEC-MIBv5-5", "psLVDIndex"),
)
if mibBuilder.loadTexts:
    psLVDEntry.setStatus("mandatory")
_PsLVDIndex_Type = Integer32
_PsLVDIndex_Object = MibTableColumn
psLVDIndex = _PsLVDIndex_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 3, 1, 1),
    _PsLVDIndex_Type()
)
psLVDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psLVDIndex.setStatus("mandatory")
_PsLVDCircuitA_Type = DisplayString
_PsLVDCircuitA_Object = MibTableColumn
psLVDCircuitA = _PsLVDCircuitA_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 3, 1, 2),
    _PsLVDCircuitA_Type()
)
psLVDCircuitA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psLVDCircuitA.setStatus("mandatory")
_PsLVDCircuitB_Type = DisplayString
_PsLVDCircuitB_Object = MibTableColumn
psLVDCircuitB = _PsLVDCircuitB_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 3, 1, 3),
    _PsLVDCircuitB_Type()
)
psLVDCircuitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psLVDCircuitB.setStatus("mandatory")
_PsDistributionTable_Object = MibTable
psDistributionTable = _PsDistributionTable_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 4)
)
if mibBuilder.loadTexts:
    psDistributionTable.setStatus("mandatory")
_PsShuntEntry_Object = MibTableRow
psShuntEntry = _PsShuntEntry_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 4, 1)
)
psShuntEntry.setIndexNames(
    (0, "VEC-MIBv5-5", "psShuntIndex"),
)
if mibBuilder.loadTexts:
    psShuntEntry.setStatus("mandatory")
_PsShuntIndex_Type = Integer32
_PsShuntIndex_Object = MibTableColumn
psShuntIndex = _PsShuntIndex_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 4, 1, 1),
    _PsShuntIndex_Type()
)
psShuntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psShuntIndex.setStatus("mandatory")
_PsShuntCurrent_Type = DisplayString
_PsShuntCurrent_Object = MibTableColumn
psShuntCurrent = _PsShuntCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 4, 1, 2),
    _PsShuntCurrent_Type()
)
psShuntCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psShuntCurrent.setStatus("mandatory")
_PsPCUTable_Object = MibTable
psPCUTable = _PsPCUTable_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5)
)
if mibBuilder.loadTexts:
    psPCUTable.setStatus("mandatory")
_PsPCUEntry_Object = MibTableRow
psPCUEntry = _PsPCUEntry_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5, 1)
)
psPCUEntry.setIndexNames(
    (0, "VEC-MIBv5-5", "psPCUIndex"),
)
if mibBuilder.loadTexts:
    psPCUEntry.setStatus("mandatory")
_PsPCUIndex_Type = Integer32
_PsPCUIndex_Object = MibTableColumn
psPCUIndex = _PsPCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5, 1, 1),
    _PsPCUIndex_Type()
)
psPCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPCUIndex.setStatus("mandatory")


class _PsPCUFail_Type(Integer32):
    """Custom type psPCUFail based on Integer32"""
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


_PsPCUFail_Type.__name__ = "Integer32"
_PsPCUFail_Object = MibTableColumn
psPCUFail = _PsPCUFail_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5, 1, 2),
    _PsPCUFail_Type()
)
psPCUFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPCUFail.setStatus("mandatory")
_PsPCUCurrent_Type = Integer32
_PsPCUCurrent_Object = MibTableColumn
psPCUCurrent = _PsPCUCurrent_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5, 1, 3),
    _PsPCUCurrent_Type()
)
psPCUCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPCUCurrent.setStatus("mandatory")


class _PsPCUFerroGateway_Type(Integer32):
    """Custom type psPCUFerroGateway based on Integer32"""
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


_PsPCUFerroGateway_Type.__name__ = "Integer32"
_PsPCUFerroGateway_Object = MibTableColumn
psPCUFerroGateway = _PsPCUFerroGateway_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 2, 5, 1, 4),
    _PsPCUFerroGateway_Type()
)
psPCUFerroGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPCUFerroGateway.setStatus("mandatory")
_PsTraps_ObjectIdentity = ObjectIdentity
psTraps = _PsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3)
)
_PsAlarmsGeneral1_ObjectIdentity = ObjectIdentity
psAlarmsGeneral1 = _PsAlarmsGeneral1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1)
)
_PsAlarmsGeneral2_ObjectIdentity = ObjectIdentity
psAlarmsGeneral2 = _PsAlarmsGeneral2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2)
)
_PsAlarmsBattery_ObjectIdentity = ObjectIdentity
psAlarmsBattery = _PsAlarmsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 3)
)
_PsPCUSummaryTypeTraps_ObjectIdentity = ObjectIdentity
psPCUSummaryTypeTraps = _PsPCUSummaryTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 4)
)
_PsPCUSummaryTraps_ObjectIdentity = ObjectIdentity
psPCUSummaryTraps = _PsPCUSummaryTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 4, 1)
)
_PsPCUNodeTypeTraps_ObjectIdentity = ObjectIdentity
psPCUNodeTypeTraps = _PsPCUNodeTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5)
)
_PsPCUTraps_ObjectIdentity = ObjectIdentity
psPCUTraps = _PsPCUTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1)
)
_PsAlarmPCUId_Type = Integer32
_PsAlarmPCUId_Object = MibScalar
psAlarmPCUId = _PsAlarmPCUId_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 1),
    _PsAlarmPCUId_Type()
)
psAlarmPCUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmPCUId.setStatus("mandatory")
_PsShuntTypeTraps_ObjectIdentity = ObjectIdentity
psShuntTypeTraps = _PsShuntTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 6)
)
_PsShuntTraps_ObjectIdentity = ObjectIdentity
psShuntTraps = _PsShuntTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 6, 1)
)
_PsAlarmShuntId_Type = Integer32
_PsAlarmShuntId_Object = MibScalar
psAlarmShuntId = _PsAlarmShuntId_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 6, 1, 1),
    _PsAlarmShuntId_Type()
)
psAlarmShuntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmShuntId.setStatus("mandatory")
_PsLVDTypeTraps_ObjectIdentity = ObjectIdentity
psLVDTypeTraps = _PsLVDTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7)
)
_PsLVDTraps_ObjectIdentity = ObjectIdentity
psLVDTraps = _PsLVDTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1)
)
_PsAlarmLVDId_Type = Integer32
_PsAlarmLVDId_Object = MibScalar
psAlarmLVDId = _PsAlarmLVDId_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 1),
    _PsAlarmLVDId_Type()
)
psAlarmLVDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmLVDId.setStatus("mandatory")
_PsTemperatureTypeTraps_ObjectIdentity = ObjectIdentity
psTemperatureTypeTraps = _PsTemperatureTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8)
)
_PsTemperatureTraps_ObjectIdentity = ObjectIdentity
psTemperatureTraps = _PsTemperatureTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8, 1)
)
_PsAlarmTemperatureId_Type = Integer32
_PsAlarmTemperatureId_Object = MibScalar
psAlarmTemperatureId = _PsAlarmTemperatureId_Object(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8, 1, 1),
    _PsAlarmTemperatureId_Type()
)
psAlarmTemperatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmTemperatureId.setStatus("mandatory")
_PsSysInfoTypeTraps_ObjectIdentity = ObjectIdentity
psSysInfoTypeTraps = _PsSysInfoTypeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9)
)
_PsSysInfoTraps_ObjectIdentity = ObjectIdentity
psSysInfoTraps = _PsSysInfoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1)
)

# Managed Objects groups


# Notification objects

psEmergencyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    psEmergencyStop.setStatus(
        "current"
    )

psAlarmVeryLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmVeryLowVoltage.setStatus(
        "current"
    )

psAlarmLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmLowVoltage.setStatus(
        "current"
    )

psAlarmSystemHighVoltage1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    psAlarmSystemHighVoltage1.setStatus(
        "current"
    )

psAlarmSystemHighVoltage2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    psAlarmSystemHighVoltage2.setStatus(
        "current"
    )

psAlarmSubsystemLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemLowVoltage.setStatus(
        "current"
    )

psAlarmSubsystemHighVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 7)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemHighVoltage.setStatus(
        "current"
    )

psAlarmSystemFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 8)
)
if mibBuilder.loadTexts:
    psAlarmSystemFuse.setStatus(
        "current"
    )

psAlarmSubsystemFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 9)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemFuse.setStatus(
        "current"
    )

psAlarmAllACOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 10)
)
if mibBuilder.loadTexts:
    psAlarmAllACOff.setStatus(
        "current"
    )

psAlarmSystemOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 11)
)
if mibBuilder.loadTexts:
    psAlarmSystemOverCurrent.setStatus(
        "current"
    )

psAlarmSubsystemOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 12)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemOverCurrent.setStatus(
        "current"
    )

psAlarmLVDsAreInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 13)
)
if mibBuilder.loadTexts:
    psAlarmLVDsAreInhibited.setStatus(
        "current"
    )

psAlarmTestEqualizeMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 14)
)
if mibBuilder.loadTexts:
    psAlarmTestEqualizeMode.setStatus(
        "current"
    )

psAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 15)
)
if mibBuilder.loadTexts:
    psAlarmMinor.setStatus(
        "current"
    )

psAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 16)
)
if mibBuilder.loadTexts:
    psAlarmMajor.setStatus(
        "current"
    )

psAlarmSenseVoltageFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 17)
)
if mibBuilder.loadTexts:
    psAlarmSenseVoltageFuse.setStatus(
        "current"
    )

psAlarmSystemVoltageFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 18)
)
if mibBuilder.loadTexts:
    psAlarmSystemVoltageFuse.setStatus(
        "current"
    )

psAlarmNoSystemVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 19)
)
if mibBuilder.loadTexts:
    psAlarmNoSystemVoltage.setStatus(
        "current"
    )

psAlarmNoSubsystemVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 20)
)
if mibBuilder.loadTexts:
    psAlarmNoSubsystemVoltage.setStatus(
        "current"
    )

psAlarmNoSenseVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 21)
)
if mibBuilder.loadTexts:
    psAlarmNoSenseVoltage.setStatus(
        "current"
    )

psAlarmDisplayNoReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 22)
)
if mibBuilder.loadTexts:
    psAlarmDisplayNoReply.setStatus(
        "current"
    )

psAlarmSubsystemMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 23)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemMajor.setStatus(
        "current"
    )

psAlarmSubsystemMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 24)
)
if mibBuilder.loadTexts:
    psAlarmSubsystemMinor.setStatus(
        "current"
    )

psAlarmHighACLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 25)
)
if mibBuilder.loadTexts:
    psAlarmHighACLine.setStatus(
        "current"
    )

psAlarmSenseVoltageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 1, 26)
)
if mibBuilder.loadTexts:
    psAlarmSenseVoltageError.setStatus(
        "current"
    )

psTestEqualizeHardwareInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    psTestEqualizeHardwareInput.setStatus(
        "current"
    )

psPCUFailMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    psPCUFailMajor.setStatus(
        "current"
    )

psPCUFailMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    psPCUFailMinor.setStatus(
        "current"
    )

psLVDAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    psLVDAlarmMajor.setStatus(
        "current"
    )

psLVDAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    psLVDAlarmMinor.setStatus(
        "current"
    )

psPCULoadShare = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    psPCULoadShare.setStatus(
        "current"
    )

psACFailMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 7)
)
if mibBuilder.loadTexts:
    psACFailMajor.setStatus(
        "current"
    )

psACFailMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 8)
)
if mibBuilder.loadTexts:
    psACFailMinor.setStatus(
        "current"
    )

psMCACommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 9)
)
if mibBuilder.loadTexts:
    psMCACommFail.setStatus(
        "current"
    )

psHVSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    psHVSActive.setStatus(
        "current"
    )

psRemoteHVSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    psRemoteHVSActive.setStatus(
        "current"
    )

psRemoteEstopActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 2, 12)
)
if mibBuilder.loadTexts:
    psRemoteEstopActive.setStatus(
        "current"
    )

psAlarmBatteryChargeOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    psAlarmBatteryChargeOverCurrent.setStatus(
        "current"
    )

psBatteryCurrentLimitInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    psBatteryCurrentLimitInhibited.setStatus(
        "current"
    )

psAlarmBatteryPoorHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    psAlarmBatteryPoorHealth.setStatus(
        "current"
    )

psAlarmBatteryReserveLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    psAlarmBatteryReserveLow.setStatus(
        "current"
    )

psAlarmPCUSummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmPCUSummary.setStatus(
        "current"
    )

psAlarmPCUHighACLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmPCUHighACLine.setStatus(
        "current"
    )

psAlarmPCUControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmPCUControllerFailure.setStatus(
        "current"
    )

psAlarmPCUFanSlowOrStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    psAlarmPCUFanSlowOrStopped.setStatus(
        "current"
    )

psAlarmPCUTurnedOffByMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    psAlarmPCUTurnedOffByMca.setStatus(
        "current"
    )

psAlarmPCUCircuitBreakerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 6)
)
if mibBuilder.loadTexts:
    psAlarmPCUCircuitBreakerOff.setStatus(
        "current"
    )

psAlarmPCUDCorACConvertFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 7)
)
if mibBuilder.loadTexts:
    psAlarmPCUDCorACConvertFail.setStatus(
        "current"
    )

psAlarmPCUThermalAlarmorCurrentLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    psAlarmPCUThermalAlarmorCurrentLimit.setStatus(
        "current"
    )

psAlarmPCUEmergencyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 9)
)
if mibBuilder.loadTexts:
    psAlarmPCUEmergencyStop.setStatus(
        "current"
    )

psAlarmPCUInputSwitchOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 10)
)
if mibBuilder.loadTexts:
    psAlarmPCUInputSwitchOff.setStatus(
        "current"
    )

psAlarmPCUHighVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 11)
)
if mibBuilder.loadTexts:
    psAlarmPCUHighVoltageShutdown.setStatus(
        "current"
    )

psAlarmPCUACInputIsOffOrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 12)
)
if mibBuilder.loadTexts:
    psAlarmPCUACInputIsOffOrLow.setStatus(
        "current"
    )

psAlarmPCUCommunicationFailureWithMCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 13)
)
if mibBuilder.loadTexts:
    psAlarmPCUCommunicationFailureWithMCA.setStatus(
        "current"
    )

psAlarmPCUSenseLeadOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 5, 1, 14)
)
if mibBuilder.loadTexts:
    psAlarmPCUSenseLeadOpen.setStatus(
        "current"
    )

psAlarmShuntType = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmShuntType.setStatus(
        "current"
    )

psAlarmShuntNoReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmShuntNoReply.setStatus(
        "current"
    )

psAlarmLVDDisconnectedA = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmLVDDisconnectedA.setStatus(
        "current"
    )

psAlarmLVDNoReplyA = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmLVDNoReplyA.setStatus(
        "current"
    )

psAlarmLVDBoardFailA = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 4)
)
if mibBuilder.loadTexts:
    psAlarmLVDBoardFailA.setStatus(
        "current"
    )

psAlarmLVDDisconnectedB = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 5)
)
if mibBuilder.loadTexts:
    psAlarmLVDDisconnectedB.setStatus(
        "current"
    )

psAlarmLVDNoReplyB = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 6)
)
if mibBuilder.loadTexts:
    psAlarmLVDNoReplyB.setStatus(
        "current"
    )

psAlarmLVDBoardFailB = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 7, 1, 7)
)
if mibBuilder.loadTexts:
    psAlarmLVDBoardFailB.setStatus(
        "current"
    )

psAlarmTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmTemperatureHigh.setStatus(
        "current"
    )

psAlarmTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmTemperatureLow.setStatus(
        "current"
    )

psAlarmTemperatureNoReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 8, 1, 4)
)
if mibBuilder.loadTexts:
    psAlarmTemperatureNoReply.setStatus(
        "current"
    )

psAlarmSysInfoError1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoError1.setStatus(
        "current"
    )

psAlarmSysInfoError2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoError2.setStatus(
        "current"
    )

psAlarmSysInfoString1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 3)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString1.setStatus(
        "current"
    )

psAlarmSysInfoString2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 4)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString2.setStatus(
        "current"
    )

psAlarmSysInfoString3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 5)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString3.setStatus(
        "current"
    )

psAlarmSysInfoString4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 6)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString4.setStatus(
        "current"
    )

psAlarmSysInfoString5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 7)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString5.setStatus(
        "current"
    )

psAlarmSysInfoString6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 8)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString6.setStatus(
        "current"
    )

psAlarmSysInfoString7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 9)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString7.setStatus(
        "current"
    )

psAlarmSysInfoString8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 10)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString8.setStatus(
        "current"
    )

psAlarmSysInfoString9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 11)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString9.setStatus(
        "current"
    )

psAlarmSysInfoString10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 885, 3, 3, 9, 1, 12)
)
if mibBuilder.loadTexts:
    psAlarmSysInfoString10.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VEC-MIBv5-5",
    **{"emersonESNA": emersonESNA,
       "vecMIB": vecMIB,
       "vec": vec,
       "vecInformation": vecInformation,
       "vecFirmwareVersion": vecFirmwareVersion,
       "vecMessageStats": vecMessageStats,
       "vecMessageRequests": vecMessageRequests,
       "vecMessageTransmissions": vecMessageTransmissions,
       "vecMessageNoResponses": vecMessageNoResponses,
       "vecMessageBadCRCs": vecMessageBadCRCs,
       "vecMessageLinkErrors": vecMessageLinkErrors,
       "vecMessagePartialResponses": vecMessagePartialResponses,
       "vecMessageWrongPackets": vecMessageWrongPackets,
       "vecMessageErrorReplies": vecMessageErrorReplies,
       "psStatus": psStatus,
       "psMeasurement": psMeasurement,
       "psSystemVoltage": psSystemVoltage,
       "psSystemCurrent": psSystemCurrent,
       "psSubsystemVoltage": psSubsystemVoltage,
       "psSubsystemCurrent": psSubsystemCurrent,
       "psSenseVoltage": psSenseVoltage,
       "psPCUTotalCurrent": psPCUTotalCurrent,
       "psBatteryCurrent": psBatteryCurrent,
       "psBatteryReserveHours": psBatteryReserveHours,
       "psTemperatureTable": psTemperatureTable,
       "psTemperatureEntry": psTemperatureEntry,
       "psTemperatureIndex": psTemperatureIndex,
       "psTemperatureMeasurement": psTemperatureMeasurement,
       "psLVDTable": psLVDTable,
       "psLVDEntry": psLVDEntry,
       "psLVDIndex": psLVDIndex,
       "psLVDCircuitA": psLVDCircuitA,
       "psLVDCircuitB": psLVDCircuitB,
       "psDistributionTable": psDistributionTable,
       "psShuntEntry": psShuntEntry,
       "psShuntIndex": psShuntIndex,
       "psShuntCurrent": psShuntCurrent,
       "psPCUTable": psPCUTable,
       "psPCUEntry": psPCUEntry,
       "psPCUIndex": psPCUIndex,
       "psPCUFail": psPCUFail,
       "psPCUCurrent": psPCUCurrent,
       "psPCUFerroGateway": psPCUFerroGateway,
       "psTraps": psTraps,
       "psAlarmsGeneral1": psAlarmsGeneral1,
       "psEmergencyStop": psEmergencyStop,
       "psAlarmVeryLowVoltage": psAlarmVeryLowVoltage,
       "psAlarmLowVoltage": psAlarmLowVoltage,
       "psAlarmSystemHighVoltage1": psAlarmSystemHighVoltage1,
       "psAlarmSystemHighVoltage2": psAlarmSystemHighVoltage2,
       "psAlarmSubsystemLowVoltage": psAlarmSubsystemLowVoltage,
       "psAlarmSubsystemHighVoltage": psAlarmSubsystemHighVoltage,
       "psAlarmSystemFuse": psAlarmSystemFuse,
       "psAlarmSubsystemFuse": psAlarmSubsystemFuse,
       "psAlarmAllACOff": psAlarmAllACOff,
       "psAlarmSystemOverCurrent": psAlarmSystemOverCurrent,
       "psAlarmSubsystemOverCurrent": psAlarmSubsystemOverCurrent,
       "psAlarmLVDsAreInhibited": psAlarmLVDsAreInhibited,
       "psAlarmTestEqualizeMode": psAlarmTestEqualizeMode,
       "psAlarmMinor": psAlarmMinor,
       "psAlarmMajor": psAlarmMajor,
       "psAlarmSenseVoltageFuse": psAlarmSenseVoltageFuse,
       "psAlarmSystemVoltageFuse": psAlarmSystemVoltageFuse,
       "psAlarmNoSystemVoltage": psAlarmNoSystemVoltage,
       "psAlarmNoSubsystemVoltage": psAlarmNoSubsystemVoltage,
       "psAlarmNoSenseVoltage": psAlarmNoSenseVoltage,
       "psAlarmDisplayNoReply": psAlarmDisplayNoReply,
       "psAlarmSubsystemMajor": psAlarmSubsystemMajor,
       "psAlarmSubsystemMinor": psAlarmSubsystemMinor,
       "psAlarmHighACLine": psAlarmHighACLine,
       "psAlarmSenseVoltageError": psAlarmSenseVoltageError,
       "psAlarmsGeneral2": psAlarmsGeneral2,
       "psTestEqualizeHardwareInput": psTestEqualizeHardwareInput,
       "psPCUFailMajor": psPCUFailMajor,
       "psPCUFailMinor": psPCUFailMinor,
       "psLVDAlarmMajor": psLVDAlarmMajor,
       "psLVDAlarmMinor": psLVDAlarmMinor,
       "psPCULoadShare": psPCULoadShare,
       "psACFailMajor": psACFailMajor,
       "psACFailMinor": psACFailMinor,
       "psMCACommFail": psMCACommFail,
       "psHVSActive": psHVSActive,
       "psRemoteHVSActive": psRemoteHVSActive,
       "psRemoteEstopActive": psRemoteEstopActive,
       "psAlarmsBattery": psAlarmsBattery,
       "psAlarmBatteryChargeOverCurrent": psAlarmBatteryChargeOverCurrent,
       "psBatteryCurrentLimitInhibited": psBatteryCurrentLimitInhibited,
       "psAlarmBatteryPoorHealth": psAlarmBatteryPoorHealth,
       "psAlarmBatteryReserveLow": psAlarmBatteryReserveLow,
       "psPCUSummaryTypeTraps": psPCUSummaryTypeTraps,
       "psPCUSummaryTraps": psPCUSummaryTraps,
       "psAlarmPCUSummary": psAlarmPCUSummary,
       "psPCUNodeTypeTraps": psPCUNodeTypeTraps,
       "psPCUTraps": psPCUTraps,
       "psAlarmPCUId": psAlarmPCUId,
       "psAlarmPCUHighACLine": psAlarmPCUHighACLine,
       "psAlarmPCUControllerFailure": psAlarmPCUControllerFailure,
       "psAlarmPCUFanSlowOrStopped": psAlarmPCUFanSlowOrStopped,
       "psAlarmPCUTurnedOffByMca": psAlarmPCUTurnedOffByMca,
       "psAlarmPCUCircuitBreakerOff": psAlarmPCUCircuitBreakerOff,
       "psAlarmPCUDCorACConvertFail": psAlarmPCUDCorACConvertFail,
       "psAlarmPCUThermalAlarmorCurrentLimit": psAlarmPCUThermalAlarmorCurrentLimit,
       "psAlarmPCUEmergencyStop": psAlarmPCUEmergencyStop,
       "psAlarmPCUInputSwitchOff": psAlarmPCUInputSwitchOff,
       "psAlarmPCUHighVoltageShutdown": psAlarmPCUHighVoltageShutdown,
       "psAlarmPCUACInputIsOffOrLow": psAlarmPCUACInputIsOffOrLow,
       "psAlarmPCUCommunicationFailureWithMCA": psAlarmPCUCommunicationFailureWithMCA,
       "psAlarmPCUSenseLeadOpen": psAlarmPCUSenseLeadOpen,
       "psShuntTypeTraps": psShuntTypeTraps,
       "psShuntTraps": psShuntTraps,
       "psAlarmShuntId": psAlarmShuntId,
       "psAlarmShuntType": psAlarmShuntType,
       "psAlarmShuntNoReply": psAlarmShuntNoReply,
       "psLVDTypeTraps": psLVDTypeTraps,
       "psLVDTraps": psLVDTraps,
       "psAlarmLVDId": psAlarmLVDId,
       "psAlarmLVDDisconnectedA": psAlarmLVDDisconnectedA,
       "psAlarmLVDNoReplyA": psAlarmLVDNoReplyA,
       "psAlarmLVDBoardFailA": psAlarmLVDBoardFailA,
       "psAlarmLVDDisconnectedB": psAlarmLVDDisconnectedB,
       "psAlarmLVDNoReplyB": psAlarmLVDNoReplyB,
       "psAlarmLVDBoardFailB": psAlarmLVDBoardFailB,
       "psTemperatureTypeTraps": psTemperatureTypeTraps,
       "psTemperatureTraps": psTemperatureTraps,
       "psAlarmTemperatureId": psAlarmTemperatureId,
       "psAlarmTemperatureHigh": psAlarmTemperatureHigh,
       "psAlarmTemperatureLow": psAlarmTemperatureLow,
       "psAlarmTemperatureNoReply": psAlarmTemperatureNoReply,
       "psSysInfoTypeTraps": psSysInfoTypeTraps,
       "psSysInfoTraps": psSysInfoTraps,
       "psAlarmSysInfoError1": psAlarmSysInfoError1,
       "psAlarmSysInfoError2": psAlarmSysInfoError2,
       "psAlarmSysInfoString1": psAlarmSysInfoString1,
       "psAlarmSysInfoString2": psAlarmSysInfoString2,
       "psAlarmSysInfoString3": psAlarmSysInfoString3,
       "psAlarmSysInfoString4": psAlarmSysInfoString4,
       "psAlarmSysInfoString5": psAlarmSysInfoString5,
       "psAlarmSysInfoString6": psAlarmSysInfoString6,
       "psAlarmSysInfoString7": psAlarmSysInfoString7,
       "psAlarmSysInfoString8": psAlarmSysInfoString8,
       "psAlarmSysInfoString9": psAlarmSysInfoString9,
       "psAlarmSysInfoString10": psAlarmSysInfoString10}
)
