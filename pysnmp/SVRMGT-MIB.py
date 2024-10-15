# SNMP MIB module (SVRMGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SVRMGT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:44 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class SnmpErrors(Integer32):
    """Custom type SnmpErrors based on Integer32"""
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
        *(("badValue", 6),
          ("genericError", 4),
          ("noError", 1),
          ("noSuchName", 5),
          ("readonly", 3),
          ("tooBig", 2))
    )





class Severity(Integer32):
    """Custom type Severity based on Integer32"""
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
        *(("high", 1),
          ("informational", 4),
          ("low", 3),
          ("medium", 2))
    )





class AlarmCategory(Integer32):
    """Custom type AlarmCategory based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("clusterGroupStatus", 27),
          ("cpuUsage", 12),
          ("diskStatus", 4),
          ("fanStatus", 5),
          ("fileUsage", 10),
          ("memoryStatus", 9),
          ("networkInboundDiscards", 17),
          ("networkInboundErrors", 13),
          ("networkInboundNonUnicastPackets", 21),
          ("networkInboundOctets", 23),
          ("networkInboundPackets", 15),
          ("networkInboundUnicastPackets", 19),
          ("networkOutboundDiscards", 18),
          ("networkOutboundErrors", 14),
          ("networkOutboundNonUnicastPackets", 22),
          ("networkOutboundOctets", 24),
          ("networkOutboundPackets", 16),
          ("networkOutboundUnicastPackets", 20),
          ("networkUnknownProtocol", 25),
          ("other", 2),
          ("powerSupplyStatus", 7),
          ("processorStatus", 3),
          ("secureBoxBreakInCount", 29),
          ("secureBoxStatus", 28),
          ("temperatureReading", 11),
          ("temperatureStatus", 8),
          ("unknown", 1),
          ("voltageReading", 26),
          ("voltageStatus", 6))
    )





class ResetRelationalOperators(Integer32):
    """Custom type ResetRelationalOperators based on Integer32"""
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
        *(("equalTo", 3),
          ("greaterThan", 1),
          ("greaterThanOrEqualTo", 2),
          ("lessThan", 5),
          ("lessThanOrEqualTo", 4),
          ("notEqualTo", 6))
    )





class ThresholdOwner(Integer32):
    """Custom type ThresholdOwner based on Integer32"""
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
        *(("bmcPatrol", 9),
          ("distributedMonitor", 8),
          ("eminate", 10),
          ("netView", 5),
          ("openView", 6),
          ("other", 2),
          ("serverWorks", 3),
          ("serverWorksMinimalHealth", 4),
          ("uniCenter", 7),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_SvrSystem_ObjectIdentity = ObjectIdentity
svrSystem = _SvrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22)
)
_SvrMgt_ObjectIdentity = ObjectIdentity
svrMgt = _SvrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2)
)
_SvrMgtMibInfo_ObjectIdentity = ObjectIdentity
svrMgtMibInfo = _SvrMgtMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 1)
)
_SvrMgtMibMajorRev_Type = Integer32
_SvrMgtMibMajorRev_Object = MibScalar
svrMgtMibMajorRev = _SvrMgtMibMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 1, 1),
    _SvrMgtMibMajorRev_Type()
)
svrMgtMibMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMgtMibMajorRev.setStatus("mandatory")
_SvrMgtMibMinorRev_Type = Integer32
_SvrMgtMibMinorRev_Object = MibScalar
svrMgtMibMinorRev = _SvrMgtMibMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 1, 2),
    _SvrMgtMibMinorRev_Type()
)
svrMgtMibMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMgtMibMinorRev.setStatus("mandatory")
_SvrAlarms_ObjectIdentity = ObjectIdentity
svrAlarms = _SvrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2)
)
_SvrAlarmNextThrIndex_Type = Integer32
_SvrAlarmNextThrIndex_Object = MibScalar
svrAlarmNextThrIndex = _SvrAlarmNextThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 1),
    _SvrAlarmNextThrIndex_Type()
)
svrAlarmNextThrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrAlarmNextThrIndex.setStatus("mandatory")
_SvrAlarmEnableTraps_Type = Boolean
_SvrAlarmEnableTraps_Object = MibScalar
svrAlarmEnableTraps = _SvrAlarmEnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 2),
    _SvrAlarmEnableTraps_Type()
)
svrAlarmEnableTraps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svrAlarmEnableTraps.setStatus("obsolete")
_SvrThresholdTable_Object = MibTable
svrThresholdTable = _SvrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3)
)
if mibBuilder.loadTexts:
    svrThresholdTable.setStatus("mandatory")
_SvrThresholdEntry_Object = MibTableRow
svrThresholdEntry = _SvrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1)
)
svrThresholdEntry.setIndexNames(
    (0, "SVRMGT-MIB", "svrThrIndex"),
)
if mibBuilder.loadTexts:
    svrThresholdEntry.setStatus("mandatory")
_SvrThrIndex_Type = Integer32
_SvrThrIndex_Object = MibTableColumn
svrThrIndex = _SvrThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 1),
    _SvrThrIndex_Type()
)
svrThrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThrIndex.setStatus("mandatory")


class _SvrThrStatus_Type(Integer32):
    """Custom type svrThrStatus based on Integer32"""
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
        *(("rowDisabled", 4),
          ("rowEnabled", 3),
          ("rowError", 5),
          ("rowInvalid", 2),
          ("underCreation", 1))
    )


_SvrThrStatus_Type.__name__ = "Integer32"
_SvrThrStatus_Object = MibTableColumn
svrThrStatus = _SvrThrStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 2),
    _SvrThrStatus_Type()
)
svrThrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrStatus.setStatus("mandatory")
_SvrThrVariableName_Type = ObjectIdentifier
_SvrThrVariableName_Object = MibTableColumn
svrThrVariableName = _SvrThrVariableName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 3),
    _SvrThrVariableName_Type()
)
svrThrVariableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrVariableName.setStatus("mandatory")


class _SvrThrValueType_Type(Integer32):
    """Custom type svrThrValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_SvrThrValueType_Type.__name__ = "Integer32"
_SvrThrValueType_Object = MibTableColumn
svrThrValueType = _SvrThrValueType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 4),
    _SvrThrValueType_Type()
)
svrThrValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrValueType.setStatus("mandatory")


class _SvrThrAlarmType_Type(Integer32):
    """Custom type svrThrAlarmType based on Integer32"""
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
        *(("equalTo", 3),
          ("greaterThan", 1),
          ("greaterThanOrEqualTo", 2),
          ("lessThan", 5),
          ("lessThanOrEqualTo", 4))
    )


_SvrThrAlarmType_Type.__name__ = "Integer32"
_SvrThrAlarmType_Object = MibTableColumn
svrThrAlarmType = _SvrThrAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 5),
    _SvrThrAlarmType_Type()
)
svrThrAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrAlarmType.setStatus("mandatory")
_SvrThrSampleInterval_Type = Integer32
_SvrThrSampleInterval_Object = MibTableColumn
svrThrSampleInterval = _SvrThrSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 6),
    _SvrThrSampleInterval_Type()
)
svrThrSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrSampleInterval.setStatus("mandatory")
_SvrThrPersistent_Type = Boolean
_SvrThrPersistent_Object = MibTableColumn
svrThrPersistent = _SvrThrPersistent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 7),
    _SvrThrPersistent_Type()
)
svrThrPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrPersistent.setStatus("mandatory")
_SvrThrThresholdValue_Type = Integer32
_SvrThrThresholdValue_Object = MibTableColumn
svrThrThresholdValue = _SvrThrThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 8),
    _SvrThrThresholdValue_Type()
)
svrThrThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrThresholdValue.setStatus("mandatory")
_SvrThrResetValue_Type = Integer32
_SvrThrResetValue_Object = MibTableColumn
svrThrResetValue = _SvrThrResetValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 9),
    _SvrThrResetValue_Type()
)
svrThrResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrResetValue.setStatus("mandatory")
_SvrThrLastValue_Type = Integer32
_SvrThrLastValue_Object = MibTableColumn
svrThrLastValue = _SvrThrLastValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 10),
    _SvrThrLastValue_Type()
)
svrThrLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThrLastValue.setStatus("mandatory")


class _SvrThrAlarmState_Type(Integer32):
    """Custom type svrThrAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("set", 1))
    )


_SvrThrAlarmState_Type.__name__ = "Integer32"
_SvrThrAlarmState_Object = MibTableColumn
svrThrAlarmState = _SvrThrAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 11),
    _SvrThrAlarmState_Type()
)
svrThrAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThrAlarmState.setStatus("mandatory")
_SvrThrLogEvent_Type = Boolean
_SvrThrLogEvent_Object = MibTableColumn
svrThrLogEvent = _SvrThrLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 12),
    _SvrThrLogEvent_Type()
)
svrThrLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLogEvent.setStatus("mandatory")
_SvrThrInvokeLocalHandler_Type = Boolean
_SvrThrInvokeLocalHandler_Object = MibTableColumn
svrThrInvokeLocalHandler = _SvrThrInvokeLocalHandler_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 13),
    _SvrThrInvokeLocalHandler_Type()
)
svrThrInvokeLocalHandler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrInvokeLocalHandler.setStatus("mandatory")
_SvrThrLocalHandlerPath_Type = DisplayString
_SvrThrLocalHandlerPath_Object = MibTableColumn
svrThrLocalHandlerPath = _SvrThrLocalHandlerPath_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 14),
    _SvrThrLocalHandlerPath_Type()
)
svrThrLocalHandlerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLocalHandlerPath.setStatus("mandatory")
_SvrThrDescr_Type = DisplayString
_SvrThrDescr_Object = MibTableColumn
svrThrDescr = _SvrThrDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 15),
    _SvrThrDescr_Type()
)
svrThrDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrDescr.setStatus("mandatory")
_SvrThrErrorValue_Type = SnmpErrors
_SvrThrErrorValue_Object = MibTableColumn
svrThrErrorValue = _SvrThrErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 16),
    _SvrThrErrorValue_Type()
)
svrThrErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThrErrorValue.setStatus("mandatory")
_SvrThrComparisonName_Type = ObjectIdentifier
_SvrThrComparisonName_Object = MibTableColumn
svrThrComparisonName = _SvrThrComparisonName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 17),
    _SvrThrComparisonName_Type()
)
svrThrComparisonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrComparisonName.setStatus("mandatory")
_SvrThrComparisonValue_Type = DisplayString
_SvrThrComparisonValue_Object = MibTableColumn
svrThrComparisonValue = _SvrThrComparisonValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 18),
    _SvrThrComparisonValue_Type()
)
svrThrComparisonValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrComparisonValue.setStatus("mandatory")
_SvrThrSeverity_Type = Severity
_SvrThrSeverity_Object = MibTableColumn
svrThrSeverity = _SvrThrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 19),
    _SvrThrSeverity_Type()
)
svrThrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrSeverity.setStatus("mandatory")
_SvrThrTrapEnabler_Type = Boolean
_SvrThrTrapEnabler_Object = MibTableColumn
svrThrTrapEnabler = _SvrThrTrapEnabler_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 20),
    _SvrThrTrapEnabler_Type()
)
svrThrTrapEnabler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrTrapEnabler.setStatus("mandatory")
_SvrThrLocalHandlerArguments1_Type = DisplayString
_SvrThrLocalHandlerArguments1_Object = MibTableColumn
svrThrLocalHandlerArguments1 = _SvrThrLocalHandlerArguments1_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 21),
    _SvrThrLocalHandlerArguments1_Type()
)
svrThrLocalHandlerArguments1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLocalHandlerArguments1.setStatus("mandatory")
_SvrThrLocalHandlerArguments2_Type = DisplayString
_SvrThrLocalHandlerArguments2_Object = MibTableColumn
svrThrLocalHandlerArguments2 = _SvrThrLocalHandlerArguments2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 22),
    _SvrThrLocalHandlerArguments2_Type()
)
svrThrLocalHandlerArguments2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLocalHandlerArguments2.setStatus("mandatory")
_SvrThrLocalHandlerArguments3_Type = DisplayString
_SvrThrLocalHandlerArguments3_Object = MibTableColumn
svrThrLocalHandlerArguments3 = _SvrThrLocalHandlerArguments3_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 23),
    _SvrThrLocalHandlerArguments3_Type()
)
svrThrLocalHandlerArguments3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLocalHandlerArguments3.setStatus("mandatory")
_SvrThrLocalHandlerArguments4_Type = DisplayString
_SvrThrLocalHandlerArguments4_Object = MibTableColumn
svrThrLocalHandlerArguments4 = _SvrThrLocalHandlerArguments4_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 24),
    _SvrThrLocalHandlerArguments4_Type()
)
svrThrLocalHandlerArguments4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrLocalHandlerArguments4.setStatus("mandatory")
_SvrThrTrapsSendingInterval_Type = Integer32
_SvrThrTrapsSendingInterval_Object = MibTableColumn
svrThrTrapsSendingInterval = _SvrThrTrapsSendingInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 25),
    _SvrThrTrapsSendingInterval_Type()
)
svrThrTrapsSendingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrTrapsSendingInterval.setStatus("mandatory")
_SvrThrManagerDefinedTrapData_Type = DisplayString
_SvrThrManagerDefinedTrapData_Object = MibTableColumn
svrThrManagerDefinedTrapData = _SvrThrManagerDefinedTrapData_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 26),
    _SvrThrManagerDefinedTrapData_Type()
)
svrThrManagerDefinedTrapData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrManagerDefinedTrapData.setStatus("mandatory")
_SvrThrUserDefinedTrapData_Type = DisplayString
_SvrThrUserDefinedTrapData_Object = MibTableColumn
svrThrUserDefinedTrapData = _SvrThrUserDefinedTrapData_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 27),
    _SvrThrUserDefinedTrapData_Type()
)
svrThrUserDefinedTrapData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrUserDefinedTrapData.setStatus("mandatory")
_SvrThrRetryCount_Type = Integer32
_SvrThrRetryCount_Object = MibTableColumn
svrThrRetryCount = _SvrThrRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 28),
    _SvrThrRetryCount_Type()
)
svrThrRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrRetryCount.setStatus("mandatory")
_SvrThrResetType_Type = ResetRelationalOperators
_SvrThrResetType_Object = MibTableColumn
svrThrResetType = _SvrThrResetType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 29),
    _SvrThrResetType_Type()
)
svrThrResetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrResetType.setStatus("mandatory")
_SvrThrAlarmCategory_Type = AlarmCategory
_SvrThrAlarmCategory_Object = MibTableColumn
svrThrAlarmCategory = _SvrThrAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 30),
    _SvrThrAlarmCategory_Type()
)
svrThrAlarmCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrAlarmCategory.setStatus("mandatory")
_SvrThrTrapOid_Type = ObjectIdentifier
_SvrThrTrapOid_Object = MibTableColumn
svrThrTrapOid = _SvrThrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 31),
    _SvrThrTrapOid_Type()
)
svrThrTrapOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrTrapOid.setStatus("mandatory")
_SvrThrCreatedBy_Type = ThresholdOwner
_SvrThrCreatedBy_Object = MibTableColumn
svrThrCreatedBy = _SvrThrCreatedBy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 32),
    _SvrThrCreatedBy_Type()
)
svrThrCreatedBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrCreatedBy.setStatus("mandatory")
_SvrThrModifiable_Type = Boolean
_SvrThrModifiable_Object = MibTableColumn
svrThrModifiable = _SvrThrModifiable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 2, 3, 1, 33),
    _SvrThrModifiable_Type()
)
svrThrModifiable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThrModifiable.setStatus("mandatory")
_SvrControl_ObjectIdentity = ObjectIdentity
svrControl = _SvrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 3)
)
_SvrControlEnableTraps_Type = Boolean
_SvrControlEnableTraps_Object = MibScalar
svrControlEnableTraps = _SvrControlEnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 3, 1),
    _SvrControlEnableTraps_Type()
)
svrControlEnableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrControlEnableTraps.setStatus("mandatory")
_SvrControlEnableModifyTraps_Type = Boolean
_SvrControlEnableModifyTraps_Object = MibScalar
svrControlEnableModifyTraps = _SvrControlEnableModifyTraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 3, 2),
    _SvrControlEnableModifyTraps_Type()
)
svrControlEnableModifyTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrControlEnableModifyTraps.setStatus("mandatory")
_SvrControlEnableResetTraps_Type = Boolean
_SvrControlEnableResetTraps_Object = MibScalar
svrControlEnableResetTraps = _SvrControlEnableResetTraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 3, 3),
    _SvrControlEnableResetTraps_Type()
)
svrControlEnableResetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrControlEnableResetTraps.setStatus("mandatory")
_SvrControlModifyOID_Type = ObjectIdentifier
_SvrControlModifyOID_Object = MibScalar
svrControlModifyOID = _SvrControlModifyOID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 3, 4),
    _SvrControlModifyOID_Type()
)
svrControlModifyOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svrControlModifyOID.setStatus("mandatory")
_SvrTrap_ObjectIdentity = ObjectIdentity
svrTrap = _SvrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4)
)


class _SvrTrapReconfigureEvent_Type(Integer32):
    """Custom type svrTrapReconfigureEvent based on Integer32"""
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


_SvrTrapReconfigureEvent_Type.__name__ = "Integer32"
_SvrTrapReconfigureEvent_Object = MibScalar
svrTrapReconfigureEvent = _SvrTrapReconfigureEvent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 1),
    _SvrTrapReconfigureEvent_Type()
)
svrTrapReconfigureEvent.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    svrTrapReconfigureEvent.setStatus("mandatory")
_SvrTrapCommunityNextIndex_Type = Integer32
_SvrTrapCommunityNextIndex_Object = MibScalar
svrTrapCommunityNextIndex = _SvrTrapCommunityNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 2),
    _SvrTrapCommunityNextIndex_Type()
)
svrTrapCommunityNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrTrapCommunityNextIndex.setStatus("mandatory")
_SvrTrapCommunityTable_Object = MibTable
svrTrapCommunityTable = _SvrTrapCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 6)
)
if mibBuilder.loadTexts:
    svrTrapCommunityTable.setStatus("mandatory")
_SvrTrapCommunityEntry_Object = MibTableRow
svrTrapCommunityEntry = _SvrTrapCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 6, 1)
)
svrTrapCommunityEntry.setIndexNames(
    (0, "SVRMGT-MIB", "svrTrapCommunityIndex"),
)
if mibBuilder.loadTexts:
    svrTrapCommunityEntry.setStatus("mandatory")
_SvrTrapCommunityIndex_Type = Integer32
_SvrTrapCommunityIndex_Object = MibTableColumn
svrTrapCommunityIndex = _SvrTrapCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 6, 1, 1),
    _SvrTrapCommunityIndex_Type()
)
svrTrapCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrTrapCommunityIndex.setStatus("mandatory")
_SvrTrapCommunityName_Type = DisplayString
_SvrTrapCommunityName_Object = MibTableColumn
svrTrapCommunityName = _SvrTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 6, 1, 2),
    _SvrTrapCommunityName_Type()
)
svrTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrTrapCommunityName.setStatus("mandatory")
_SvrTrapDestinationNextIndex_Type = Integer32
_SvrTrapDestinationNextIndex_Object = MibTableColumn
svrTrapDestinationNextIndex = _SvrTrapDestinationNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 6, 1, 3),
    _SvrTrapDestinationNextIndex_Type()
)
svrTrapDestinationNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrTrapDestinationNextIndex.setStatus("mandatory")
_SvrTrapDestinationTable_Object = MibTable
svrTrapDestinationTable = _SvrTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 7)
)
if mibBuilder.loadTexts:
    svrTrapDestinationTable.setStatus("mandatory")
_SvrTrapDestinationEntry_Object = MibTableRow
svrTrapDestinationEntry = _SvrTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 7, 1)
)
svrTrapDestinationEntry.setIndexNames(
    (0, "SVRMGT-MIB", "svrTrapCommunityIndex"),
    (0, "SVRMGT-MIB", "svrTrapDestinationIndex"),
)
if mibBuilder.loadTexts:
    svrTrapDestinationEntry.setStatus("mandatory")
_SvrTrapDestinationIndex_Type = Integer32
_SvrTrapDestinationIndex_Object = MibTableColumn
svrTrapDestinationIndex = _SvrTrapDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 7, 1, 1),
    _SvrTrapDestinationIndex_Type()
)
svrTrapDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrTrapDestinationIndex.setStatus("mandatory")
_SvrTrapDestination_Type = DisplayString
_SvrTrapDestination_Object = MibTableColumn
svrTrapDestination = _SvrTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 4, 7, 1, 2),
    _SvrTrapDestination_Type()
)
svrTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrTrapDestination.setStatus("mandatory")
_SvrMinimalHealth_ObjectIdentity = ObjectIdentity
svrMinimalHealth = _SvrMinimalHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5)
)
_SvrMinimalHealthMajorRev_Type = Integer32
_SvrMinimalHealthMajorRev_Object = MibScalar
svrMinimalHealthMajorRev = _SvrMinimalHealthMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 1),
    _SvrMinimalHealthMajorRev_Type()
)
svrMinimalHealthMajorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthMajorRev.setStatus("mandatory")
_SvrMinimalHealthMinorRev_Type = Integer32
_SvrMinimalHealthMinorRev_Object = MibScalar
svrMinimalHealthMinorRev = _SvrMinimalHealthMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 2),
    _SvrMinimalHealthMinorRev_Type()
)
svrMinimalHealthMinorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthMinorRev.setStatus("mandatory")
_SvrMinimalHealthEnable_Type = Boolean
_SvrMinimalHealthEnable_Object = MibScalar
svrMinimalHealthEnable = _SvrMinimalHealthEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 3),
    _SvrMinimalHealthEnable_Type()
)
svrMinimalHealthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthEnable.setStatus("mandatory")
_SvrMinimalHealthDesiredTemplateName_Type = DisplayString
_SvrMinimalHealthDesiredTemplateName_Object = MibScalar
svrMinimalHealthDesiredTemplateName = _SvrMinimalHealthDesiredTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 4),
    _SvrMinimalHealthDesiredTemplateName_Type()
)
svrMinimalHealthDesiredTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthDesiredTemplateName.setStatus("mandatory")
_SvrMinimalHealthDesiredTemplateRevision_Type = DisplayString
_SvrMinimalHealthDesiredTemplateRevision_Object = MibScalar
svrMinimalHealthDesiredTemplateRevision = _SvrMinimalHealthDesiredTemplateRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 5),
    _SvrMinimalHealthDesiredTemplateRevision_Type()
)
svrMinimalHealthDesiredTemplateRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthDesiredTemplateRevision.setStatus("mandatory")
_SvrMinimalHealthDesiredTemplateRevisionDate_Type = DisplayString
_SvrMinimalHealthDesiredTemplateRevisionDate_Object = MibScalar
svrMinimalHealthDesiredTemplateRevisionDate = _SvrMinimalHealthDesiredTemplateRevisionDate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 6),
    _SvrMinimalHealthDesiredTemplateRevisionDate_Type()
)
svrMinimalHealthDesiredTemplateRevisionDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthDesiredTemplateRevisionDate.setStatus("mandatory")
_SvrMinimalHealthActualTemplateName_Type = DisplayString
_SvrMinimalHealthActualTemplateName_Object = MibScalar
svrMinimalHealthActualTemplateName = _SvrMinimalHealthActualTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 7),
    _SvrMinimalHealthActualTemplateName_Type()
)
svrMinimalHealthActualTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthActualTemplateName.setStatus("mandatory")
_SvrMinimalHealthActualTemplateRevision_Type = DisplayString
_SvrMinimalHealthActualTemplateRevision_Object = MibScalar
svrMinimalHealthActualTemplateRevision = _SvrMinimalHealthActualTemplateRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 8),
    _SvrMinimalHealthActualTemplateRevision_Type()
)
svrMinimalHealthActualTemplateRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthActualTemplateRevision.setStatus("mandatory")
_SvrMinimalHealthActualTemplateRevisionDate_Type = DisplayString
_SvrMinimalHealthActualTemplateRevisionDate_Object = MibScalar
svrMinimalHealthActualTemplateRevisionDate = _SvrMinimalHealthActualTemplateRevisionDate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 5, 9),
    _SvrMinimalHealthActualTemplateRevisionDate_Type()
)
svrMinimalHealthActualTemplateRevisionDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrMinimalHealthActualTemplateRevisionDate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

svrThrModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 99)
)
svrThrModifyTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrControlModifyOID"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrModifyTrap.setStatus(
        ""
    )

svrThrResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 100)
)
svrThrResetTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrResetValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrResetTrap.setStatus(
        ""
    )

svrThrHighExceptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 101)
)
svrThrHighExceptTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrHighExceptTrap.setStatus(
        ""
    )

svrThrMediumExceptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 102)
)
svrThrMediumExceptTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrMediumExceptTrap.setStatus(
        ""
    )

svrThrLowExceptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 103)
)
svrThrLowExceptTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrLowExceptTrap.setStatus(
        ""
    )

svrThrInformationalExceptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 104)
)
svrThrInformationalExceptTrap.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrInformationalExceptTrap.setStatus(
        ""
    )

svrThrDiskDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 105)
)
svrThrDiskDown.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrDiskDown.setStatus(
        ""
    )

svrThrDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 106)
)
svrThrDiskWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrDiskWarning.setStatus(
        ""
    )

svrThrDiskOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 107)
)
svrThrDiskOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrDiskOk.setStatus(
        ""
    )

svrThrFileSystemUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 108)
)
svrThrFileSystemUsage.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrFileSystemUsage.setStatus(
        ""
    )

svrThrTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 109)
)
svrThrTemperatureOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrTemperatureOk.setStatus(
        ""
    )

svrThrTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 110)
)
svrThrTemperatureCritical.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrTemperatureCritical.setStatus(
        ""
    )

svrThrTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 111)
)
svrThrTemperatureWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrTemperatureWarning.setStatus(
        ""
    )

svrThrFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 112)
)
svrThrFanFailed.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrFanFailed.setStatus(
        ""
    )

svrThrFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 113)
)
svrThrFanOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrFanOk.setStatus(
        ""
    )

svrThrFanBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 114)
)
svrThrFanBackup.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrFanBackup.setStatus(
        ""
    )

svrThrVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 115)
)
svrThrVoltageOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrVoltageOk.setStatus(
        ""
    )

svrThrVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 116)
)
svrThrVoltageCritical.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrVoltageCritical.setStatus(
        ""
    )

svrThrVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 117)
)
svrThrVoltageWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrVoltageWarning.setStatus(
        ""
    )

svrThrPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 118)
)
svrThrPowerSupplyFailed.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrPowerSupplyFailed.setStatus(
        ""
    )

svrThrPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 119)
)
svrThrPowerSupplyWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrPowerSupplyWarning.setStatus(
        ""
    )

svrThrPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 120)
)
svrThrPowerSupplyOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrPowerSupplyOk.setStatus(
        ""
    )

svrThrPowerSupplyBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 121)
)
svrThrPowerSupplyBackup.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrPowerSupplyBackup.setStatus(
        ""
    )

svrThrMemoryEltFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 122)
)
svrThrMemoryEltFailed.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrMemoryEltFailed.setStatus(
        ""
    )

svrThrMemoryEltWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 123)
)
svrThrMemoryEltWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrMemoryEltWarning.setStatus(
        ""
    )

svrThrMemoryEltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 124)
)
svrThrMemoryEltOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrMemoryEltOk.setStatus(
        ""
    )

svrThrNetworkIfInErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 125)
)
svrThrNetworkIfInErrors.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfInErrors.setStatus(
        ""
    )

svrThrNetworkIfInOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 126)
)
svrThrNetworkIfInOctets.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfInOctets.setStatus(
        ""
    )

svrThrNetworkIfOutOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 127)
)
svrThrNetworkIfOutOctets.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfOutOctets.setStatus(
        ""
    )

svrThrNetworkIfInPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 128)
)
svrThrNetworkIfInPkts.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfInPkts.setStatus(
        ""
    )

svrThrNetworkIfOutPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 129)
)
svrThrNetworkIfOutPkts.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfOutPkts.setStatus(
        ""
    )

svrThrNetworkIfOutErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 130)
)
svrThrNetworkIfOutErrors.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfOutErrors.setStatus(
        ""
    )

svrThrNetworkIfInDiscards = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 131)
)
svrThrNetworkIfInDiscards.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrNetworkIfInDiscards.setStatus(
        ""
    )

svrThrProcessorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 132)
)
svrThrProcessorDown.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrProcessorDown.setStatus(
        ""
    )

svrThrProcessorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 133)
)
svrThrProcessorWarning.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrProcessorWarning.setStatus(
        ""
    )

svrThrProcessorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 134)
)
svrThrProcessorOk.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrProcessorOk.setStatus(
        ""
    )

svrThrCpuUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 135)
)
svrThrCpuUsage.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrCpuUsage.setStatus(
        ""
    )

svrThrClusterFailOverOwner = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 136)
)
svrThrClusterFailOverOwner.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrClusterFailOverOwner.setStatus(
        ""
    )

svrThrClusterFailOverNotOwner = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 2, 0, 137)
)
svrThrClusterFailOverNotOwner.setObjects(
      *(("SVRMGT-MIB", "svrThrVariableName"),
        ("SVRMGT-MIB", "svrThrValueType"),
        ("SVRMGT-MIB", "svrThrThresholdValue"),
        ("SVRMGT-MIB", "svrThrLastValue"),
        ("SVRMGT-MIB", "svrThrDescr"),
        ("SVRMGT-MIB", "svrThrManagerDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrUserDefinedTrapData"),
        ("SVRMGT-MIB", "svrThrAlarmCategory"),
        ("SVRMGT-MIB", "svrThrCreatedBy"),
        ("SVRMGT-MIB", "svrThrSeverity"))
)
if mibBuilder.loadTexts:
    svrThrClusterFailOverNotOwner.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SVRMGT-MIB",
    **{"Boolean": Boolean,
       "SnmpErrors": SnmpErrors,
       "Severity": Severity,
       "AlarmCategory": AlarmCategory,
       "ResetRelationalOperators": ResetRelationalOperators,
       "ThresholdOwner": ThresholdOwner,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "svrSystem": svrSystem,
       "svrMgt": svrMgt,
       "svrThrModifyTrap": svrThrModifyTrap,
       "svrThrResetTrap": svrThrResetTrap,
       "svrThrHighExceptTrap": svrThrHighExceptTrap,
       "svrThrMediumExceptTrap": svrThrMediumExceptTrap,
       "svrThrLowExceptTrap": svrThrLowExceptTrap,
       "svrThrInformationalExceptTrap": svrThrInformationalExceptTrap,
       "svrThrDiskDown": svrThrDiskDown,
       "svrThrDiskWarning": svrThrDiskWarning,
       "svrThrDiskOk": svrThrDiskOk,
       "svrThrFileSystemUsage": svrThrFileSystemUsage,
       "svrThrTemperatureOk": svrThrTemperatureOk,
       "svrThrTemperatureCritical": svrThrTemperatureCritical,
       "svrThrTemperatureWarning": svrThrTemperatureWarning,
       "svrThrFanFailed": svrThrFanFailed,
       "svrThrFanOk": svrThrFanOk,
       "svrThrFanBackup": svrThrFanBackup,
       "svrThrVoltageOk": svrThrVoltageOk,
       "svrThrVoltageCritical": svrThrVoltageCritical,
       "svrThrVoltageWarning": svrThrVoltageWarning,
       "svrThrPowerSupplyFailed": svrThrPowerSupplyFailed,
       "svrThrPowerSupplyWarning": svrThrPowerSupplyWarning,
       "svrThrPowerSupplyOk": svrThrPowerSupplyOk,
       "svrThrPowerSupplyBackup": svrThrPowerSupplyBackup,
       "svrThrMemoryEltFailed": svrThrMemoryEltFailed,
       "svrThrMemoryEltWarning": svrThrMemoryEltWarning,
       "svrThrMemoryEltOk": svrThrMemoryEltOk,
       "svrThrNetworkIfInErrors": svrThrNetworkIfInErrors,
       "svrThrNetworkIfInOctets": svrThrNetworkIfInOctets,
       "svrThrNetworkIfOutOctets": svrThrNetworkIfOutOctets,
       "svrThrNetworkIfInPkts": svrThrNetworkIfInPkts,
       "svrThrNetworkIfOutPkts": svrThrNetworkIfOutPkts,
       "svrThrNetworkIfOutErrors": svrThrNetworkIfOutErrors,
       "svrThrNetworkIfInDiscards": svrThrNetworkIfInDiscards,
       "svrThrProcessorDown": svrThrProcessorDown,
       "svrThrProcessorWarning": svrThrProcessorWarning,
       "svrThrProcessorOk": svrThrProcessorOk,
       "svrThrCpuUsage": svrThrCpuUsage,
       "svrThrClusterFailOverOwner": svrThrClusterFailOverOwner,
       "svrThrClusterFailOverNotOwner": svrThrClusterFailOverNotOwner,
       "svrMgtMibInfo": svrMgtMibInfo,
       "svrMgtMibMajorRev": svrMgtMibMajorRev,
       "svrMgtMibMinorRev": svrMgtMibMinorRev,
       "svrAlarms": svrAlarms,
       "svrAlarmNextThrIndex": svrAlarmNextThrIndex,
       "svrAlarmEnableTraps": svrAlarmEnableTraps,
       "svrThresholdTable": svrThresholdTable,
       "svrThresholdEntry": svrThresholdEntry,
       "svrThrIndex": svrThrIndex,
       "svrThrStatus": svrThrStatus,
       "svrThrVariableName": svrThrVariableName,
       "svrThrValueType": svrThrValueType,
       "svrThrAlarmType": svrThrAlarmType,
       "svrThrSampleInterval": svrThrSampleInterval,
       "svrThrPersistent": svrThrPersistent,
       "svrThrThresholdValue": svrThrThresholdValue,
       "svrThrResetValue": svrThrResetValue,
       "svrThrLastValue": svrThrLastValue,
       "svrThrAlarmState": svrThrAlarmState,
       "svrThrLogEvent": svrThrLogEvent,
       "svrThrInvokeLocalHandler": svrThrInvokeLocalHandler,
       "svrThrLocalHandlerPath": svrThrLocalHandlerPath,
       "svrThrDescr": svrThrDescr,
       "svrThrErrorValue": svrThrErrorValue,
       "svrThrComparisonName": svrThrComparisonName,
       "svrThrComparisonValue": svrThrComparisonValue,
       "svrThrSeverity": svrThrSeverity,
       "svrThrTrapEnabler": svrThrTrapEnabler,
       "svrThrLocalHandlerArguments1": svrThrLocalHandlerArguments1,
       "svrThrLocalHandlerArguments2": svrThrLocalHandlerArguments2,
       "svrThrLocalHandlerArguments3": svrThrLocalHandlerArguments3,
       "svrThrLocalHandlerArguments4": svrThrLocalHandlerArguments4,
       "svrThrTrapsSendingInterval": svrThrTrapsSendingInterval,
       "svrThrManagerDefinedTrapData": svrThrManagerDefinedTrapData,
       "svrThrUserDefinedTrapData": svrThrUserDefinedTrapData,
       "svrThrRetryCount": svrThrRetryCount,
       "svrThrResetType": svrThrResetType,
       "svrThrAlarmCategory": svrThrAlarmCategory,
       "svrThrTrapOid": svrThrTrapOid,
       "svrThrCreatedBy": svrThrCreatedBy,
       "svrThrModifiable": svrThrModifiable,
       "svrControl": svrControl,
       "svrControlEnableTraps": svrControlEnableTraps,
       "svrControlEnableModifyTraps": svrControlEnableModifyTraps,
       "svrControlEnableResetTraps": svrControlEnableResetTraps,
       "svrControlModifyOID": svrControlModifyOID,
       "svrTrap": svrTrap,
       "svrTrapReconfigureEvent": svrTrapReconfigureEvent,
       "svrTrapCommunityNextIndex": svrTrapCommunityNextIndex,
       "svrTrapCommunityTable": svrTrapCommunityTable,
       "svrTrapCommunityEntry": svrTrapCommunityEntry,
       "svrTrapCommunityIndex": svrTrapCommunityIndex,
       "svrTrapCommunityName": svrTrapCommunityName,
       "svrTrapDestinationNextIndex": svrTrapDestinationNextIndex,
       "svrTrapDestinationTable": svrTrapDestinationTable,
       "svrTrapDestinationEntry": svrTrapDestinationEntry,
       "svrTrapDestinationIndex": svrTrapDestinationIndex,
       "svrTrapDestination": svrTrapDestination,
       "svrMinimalHealth": svrMinimalHealth,
       "svrMinimalHealthMajorRev": svrMinimalHealthMajorRev,
       "svrMinimalHealthMinorRev": svrMinimalHealthMinorRev,
       "svrMinimalHealthEnable": svrMinimalHealthEnable,
       "svrMinimalHealthDesiredTemplateName": svrMinimalHealthDesiredTemplateName,
       "svrMinimalHealthDesiredTemplateRevision": svrMinimalHealthDesiredTemplateRevision,
       "svrMinimalHealthDesiredTemplateRevisionDate": svrMinimalHealthDesiredTemplateRevisionDate,
       "svrMinimalHealthActualTemplateName": svrMinimalHealthActualTemplateName,
       "svrMinimalHealthActualTemplateRevision": svrMinimalHealthActualTemplateRevision,
       "svrMinimalHealthActualTemplateRevisionDate": svrMinimalHealthActualTemplateRevisionDate}
)
