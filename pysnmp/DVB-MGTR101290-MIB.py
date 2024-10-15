# SNMP MIB module (DVB-MGTR101290-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVB-MGTR101290-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:53 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tr101290 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ActiveTime(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class Availability(Integer32, TextualConvention):
    status = "current"
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
        *(("measurementAndTestAvailable", 4),
          ("measurementAvailable", 3),
          ("notAvailable", 1),
          ("testAvailable", 2))
    )



class BERMeasurementMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iqCombined", 2),
          ("iqSeparate", 1))
    )



class BitRateElement(Integer32, TextualConvention):
    status = "current"
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
        *(("bit", 1),
          ("byte", 2),
          ("other", 4),
          ("packet", 3))
    )



class DeliverySystemType(Integer32, TextualConvention):
    status = "current"
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
        *(("cable", 2),
          ("satellite", 3),
          ("terrestrial", 4),
          ("unknown", 1))
    )



class Enable(Bits, TextualConvention):
    status = "current"


class FloatingPoint(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class GroupAvailability(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completeSupport", 3),
          ("noSupport", 1),
          ("selectiveSupport", 2))
    )



class GuardInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("interval1d16", 3),
          ("interval1d32", 4),
          ("interval1d4", 1),
          ("interval1d8", 2))
    )



class Hierarchy(Integer32, TextualConvention):
    status = "current"
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
        *(("hierarchicalAlphaFour", 4),
          ("hierarchicalAlphaOne", 2),
          ("hierarchicalAphaTwo", 3),
          ("nonHierarchical", 1))
    )



class IndexConsistencyTest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tsIdCheck", 1)
    )



class IndexMIPSyntaxTest(Integer32, TextualConvention):
    status = "current"
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
        *(("mipPeriodicityError", 5),
          ("mipPointerError", 4),
          ("mipPresenceError", 3),
          ("mipStructureError", 2),
          ("mipTimingError", 1),
          ("mipTsRateError", 6))
    )



class IndexPCRMeasurement(Integer32, TextualConvention):
    status = "current"
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
        *(("pcrAC", 4),
          ("pcrDR", 2),
          ("pcrFO", 1),
          ("pcrOJ", 3))
    )



class IndexServicePerformance(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serviceAvailability", 1),
          ("serviceDegradation", 2),
          ("serviceImpairments", 3))
    )



class IndexTransportStreamTest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1010,
              1020,
              1031,
              1040,
              1051,
              1060,
              2010,
              2020,
              2031,
              2032,
              2040,
              2050,
              2060,
              3011,
              3012,
              3020,
              3030,
              3041,
              3051,
              3052,
              3061,
              3062,
              3063,
              3070,
              3080,
              3090,
              3100)
        )
    )
    namedValues = NamedValues(
        *(("bufferError", 3030),
          ("catError", 2060),
          ("continuityCountError", 1040),
          ("crcError", 2020),
          ("dataDelayError", 3100),
          ("eitActualError", 3061),
          ("eitOtherError", 3062),
          ("eitPfError", 3063),
          ("emptyBufferError", 3090),
          ("nitActualError", 3011),
          ("nitOtherError", 3012),
          ("patError2", 1031),
          ("pcrAccuracyError", 2040),
          ("pcrDiscontinuityError", 2032),
          ("pcrRepetitionError", 2031),
          ("pidError", 1060),
          ("pmtError2", 1051),
          ("ptsError", 2050),
          ("rstError", 3070),
          ("sdtActualError", 3051),
          ("sdtOtherError", 3052),
          ("siRepetitionError", 3020),
          ("syncByteError", 1020),
          ("tdtError", 3080),
          ("transportError", 2010),
          ("tsSyncLoss", 1010),
          ("unreferencedPID", 3041))
    )



class InputNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MeasurementState(Integer32, TextualConvention):
    status = "current"
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
        *(("abnormal", 4),
          ("disabled", 1),
          ("normal", 3),
          ("unknown", 2))
    )



class Modulation(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bpsk", 1),
          ("psk8", 3),
          ("qam128", 7),
          ("qam16", 4),
          ("qam16Alpha2", 9),
          ("qam16Alpha4", 11),
          ("qam256", 8),
          ("qam32", 5),
          ("qam64", 6),
          ("qam64Alpha2", 10),
          ("qam64Alpha4", 12),
          ("qpsk", 2))
    )



class PIDPlusOne(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )



class PollingInterval(Integer32, TextualConvention):
    status = "current"


class RateStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledThrottled", 3))
    )



class ServiceId(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TerrestrialTransmissionMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode2k", 1),
          ("mode8k", 2))
    )



class TestState(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 1),
          ("fail", 4),
          ("pass", 3),
          ("unknown", 2))
    )



class TestSummary(Bits, TextualConvention):
    status = "current"


class TransportStreamID(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UATMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nConsecutive", 1),
          ("rollingWindow", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Dvb_ObjectIdentity = ObjectIdentity
dvb = _Dvb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696)
)
_Mg_ObjectIdentity = ObjectIdentity
mg = _Mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3)
)
_Tr101290Objects_ObjectIdentity = ObjectIdentity
tr101290Objects = _Tr101290Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1)
)
_Tr101290Control_ObjectIdentity = ObjectIdentity
tr101290Control = _Tr101290Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1)
)
_ControlNow_Type = DateAndTime
_ControlNow_Object = MibScalar
controlNow = _ControlNow_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 1),
    _ControlNow_Type()
)
controlNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlNow.setStatus("current")


class _ControlEventPersistence_Type(FloatingPoint):
    """Custom type controlEventPersistence based on FloatingPoint"""
    defaultValue = OctetString("2")


_ControlEventPersistence_Object = MibScalar
controlEventPersistence = _ControlEventPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 2),
    _ControlEventPersistence_Type()
)
controlEventPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlEventPersistence.setStatus("current")
if mibBuilder.loadTexts:
    controlEventPersistence.setUnits("second")
_ControlRFSystemTable_Object = MibTable
controlRFSystemTable = _ControlRFSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    controlRFSystemTable.setStatus("current")
_ControlRFSystemEntry_Object = MibTableRow
controlRFSystemEntry = _ControlRFSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 3, 1)
)
controlRFSystemEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfSystemInputNumber"),
)
if mibBuilder.loadTexts:
    controlRFSystemEntry.setStatus("current")
_RfSystemInputNumber_Type = InputNumber
_RfSystemInputNumber_Object = MibTableColumn
rfSystemInputNumber = _RfSystemInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 3, 1, 1),
    _RfSystemInputNumber_Type()
)
rfSystemInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfSystemInputNumber.setStatus("current")
_RfSystemDelivery_Type = DeliverySystemType
_RfSystemDelivery_Object = MibTableColumn
rfSystemDelivery = _RfSystemDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 3, 1, 2),
    _RfSystemDelivery_Type()
)
rfSystemDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfSystemDelivery.setStatus("current")
_ControlSynchronizationTable_Object = MibTable
controlSynchronizationTable = _ControlSynchronizationTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    controlSynchronizationTable.setStatus("current")
_ControlSynchronizationEntry_Object = MibTableRow
controlSynchronizationEntry = _ControlSynchronizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 4, 1)
)
controlSynchronizationEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "controlSynchronizationInputNumber"),
)
if mibBuilder.loadTexts:
    controlSynchronizationEntry.setStatus("current")
_ControlSynchronizationInputNumber_Type = InputNumber
_ControlSynchronizationInputNumber_Object = MibTableColumn
controlSynchronizationInputNumber = _ControlSynchronizationInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 4, 1, 1),
    _ControlSynchronizationInputNumber_Type()
)
controlSynchronizationInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSynchronizationInputNumber.setStatus("current")
_ControlSynchronizedTime_Type = FloatingPoint
_ControlSynchronizedTime_Object = MibTableColumn
controlSynchronizedTime = _ControlSynchronizedTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 1, 4, 1, 2),
    _ControlSynchronizedTime_Type()
)
controlSynchronizedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSynchronizedTime.setStatus("current")
_Tr101290Trap_ObjectIdentity = ObjectIdentity
tr101290Trap = _Tr101290Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 0)
)
_TrapControlTable_Object = MibTable
trapControlTable = _TrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    trapControlTable.setStatus("current")
_TrapControlEntry_Object = MibTableRow
trapControlEntry = _TrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1)
)
trapControlEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "trapControlInputNumber"),
)
if mibBuilder.loadTexts:
    trapControlEntry.setStatus("current")
_TrapControlInputNumber_Type = InputNumber
_TrapControlInputNumber_Object = MibTableColumn
trapControlInputNumber = _TrapControlInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 1),
    _TrapControlInputNumber_Type()
)
trapControlInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapControlInputNumber.setStatus("current")
_TrapControlOID_Type = ObjectIdentifier
_TrapControlOID_Object = MibTableColumn
trapControlOID = _TrapControlOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 2),
    _TrapControlOID_Type()
)
trapControlOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapControlOID.setStatus("current")
_TrapControlGenerationTime_Type = DateAndTime
_TrapControlGenerationTime_Object = MibTableColumn
trapControlGenerationTime = _TrapControlGenerationTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 3),
    _TrapControlGenerationTime_Type()
)
trapControlGenerationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapControlGenerationTime.setStatus("current")
_TrapControlMeasurementValue_Type = FloatingPoint
_TrapControlMeasurementValue_Object = MibTableColumn
trapControlMeasurementValue = _TrapControlMeasurementValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 4),
    _TrapControlMeasurementValue_Type()
)
trapControlMeasurementValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapControlMeasurementValue.setStatus("current")
_TrapControlRateStatus_Type = RateStatus
_TrapControlRateStatus_Object = MibTableColumn
trapControlRateStatus = _TrapControlRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 5),
    _TrapControlRateStatus_Type()
)
trapControlRateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapControlRateStatus.setStatus("current")


class _TrapControlPeriod_Type(Unsigned32):
    """Custom type trapControlPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_TrapControlPeriod_Type.__name__ = "Unsigned32"
_TrapControlPeriod_Object = MibTableColumn
trapControlPeriod = _TrapControlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 6),
    _TrapControlPeriod_Type()
)
trapControlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapControlPeriod.setStatus("current")
if mibBuilder.loadTexts:
    trapControlPeriod.setUnits("millisecond")
_TrapControlFailureSummary_Type = TestSummary
_TrapControlFailureSummary_Object = MibTableColumn
trapControlFailureSummary = _TrapControlFailureSummary_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 1, 1, 7),
    _TrapControlFailureSummary_Type()
)
trapControlFailureSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapControlFailureSummary.setStatus("current")
_TrapInput_Type = InputNumber
_TrapInput_Object = MibScalar
trapInput = _TrapInput_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 2),
    _TrapInput_Type()
)
trapInput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapInput.setStatus("current")
_Tr101290Capability_ObjectIdentity = ObjectIdentity
tr101290Capability = _Tr101290Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3)
)
_CapabilityMIBRevision_Type = DateAndTime
_CapabilityMIBRevision_Object = MibScalar
capabilityMIBRevision = _CapabilityMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 1),
    _CapabilityMIBRevision_Type()
)
capabilityMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityMIBRevision.setStatus("current")
_CapabilityTS_ObjectIdentity = ObjectIdentity
capabilityTS = _CapabilityTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5)
)
_CapabilityTSGroup_Type = GroupAvailability
_CapabilityTSGroup_Object = MibScalar
capabilityTSGroup = _CapabilityTSGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 1),
    _CapabilityTSGroup_Type()
)
capabilityTSGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTSGroup.setStatus("current")
_CapabilityTSTable_Object = MibTable
capabilityTSTable = _CapabilityTSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    capabilityTSTable.setStatus("current")
_CapabilityTSEntry_Object = MibTableRow
capabilityTSEntry = _CapabilityTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 2, 1)
)
capabilityTSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "capabilityTSOID"),
)
if mibBuilder.loadTexts:
    capabilityTSEntry.setStatus("current")
_CapabilityTSOID_Type = ObjectIdentifier
_CapabilityTSOID_Object = MibTableColumn
capabilityTSOID = _CapabilityTSOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 2, 1, 1),
    _CapabilityTSOID_Type()
)
capabilityTSOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capabilityTSOID.setStatus("current")
_CapabilityTSAvailability_Type = Availability
_CapabilityTSAvailability_Object = MibTableColumn
capabilityTSAvailability = _CapabilityTSAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 2, 1, 2),
    _CapabilityTSAvailability_Type()
)
capabilityTSAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTSAvailability.setStatus("current")
_CapabilityTSPollInterval_Type = PollingInterval
_CapabilityTSPollInterval_Object = MibTableColumn
capabilityTSPollInterval = _CapabilityTSPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 5, 2, 1, 3),
    _CapabilityTSPollInterval_Type()
)
capabilityTSPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTSPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    capabilityTSPollInterval.setUnits("millisecond")
_CapabilityCableSat_ObjectIdentity = ObjectIdentity
capabilityCableSat = _CapabilityCableSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6)
)
_CapabilityCableSatGroup_Type = GroupAvailability
_CapabilityCableSatGroup_Object = MibScalar
capabilityCableSatGroup = _CapabilityCableSatGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 1),
    _CapabilityCableSatGroup_Type()
)
capabilityCableSatGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCableSatGroup.setStatus("current")
_CapabilityCableSatTable_Object = MibTable
capabilityCableSatTable = _CapabilityCableSatTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    capabilityCableSatTable.setStatus("current")
_CapabilityCableSatEntry_Object = MibTableRow
capabilityCableSatEntry = _CapabilityCableSatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 2, 1)
)
capabilityCableSatEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "capabilityCableSatOID"),
)
if mibBuilder.loadTexts:
    capabilityCableSatEntry.setStatus("current")
_CapabilityCableSatOID_Type = ObjectIdentifier
_CapabilityCableSatOID_Object = MibTableColumn
capabilityCableSatOID = _CapabilityCableSatOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 2, 1, 1),
    _CapabilityCableSatOID_Type()
)
capabilityCableSatOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capabilityCableSatOID.setStatus("current")
_CapabilityCableSatAvailability_Type = Availability
_CapabilityCableSatAvailability_Object = MibTableColumn
capabilityCableSatAvailability = _CapabilityCableSatAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 2, 1, 2),
    _CapabilityCableSatAvailability_Type()
)
capabilityCableSatAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCableSatAvailability.setStatus("current")
_CapabilityCableSatPollInterval_Type = PollingInterval
_CapabilityCableSatPollInterval_Object = MibTableColumn
capabilityCableSatPollInterval = _CapabilityCableSatPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 6, 2, 1, 3),
    _CapabilityCableSatPollInterval_Type()
)
capabilityCableSatPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCableSatPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    capabilityCableSatPollInterval.setUnits("millisecond")
_CapabilityCable_ObjectIdentity = ObjectIdentity
capabilityCable = _CapabilityCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7)
)
_CapabilityCableGroup_Type = GroupAvailability
_CapabilityCableGroup_Object = MibScalar
capabilityCableGroup = _CapabilityCableGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 1),
    _CapabilityCableGroup_Type()
)
capabilityCableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCableGroup.setStatus("current")
_CapabilityCableTable_Object = MibTable
capabilityCableTable = _CapabilityCableTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    capabilityCableTable.setStatus("current")
_CapabilityCableEntry_Object = MibTableRow
capabilityCableEntry = _CapabilityCableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 2, 1)
)
capabilityCableEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "capabilityCableOID"),
)
if mibBuilder.loadTexts:
    capabilityCableEntry.setStatus("current")
_CapabilityCableOID_Type = ObjectIdentifier
_CapabilityCableOID_Object = MibTableColumn
capabilityCableOID = _CapabilityCableOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 2, 1, 1),
    _CapabilityCableOID_Type()
)
capabilityCableOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capabilityCableOID.setStatus("current")
_CapabilityCableAvailability_Type = Availability
_CapabilityCableAvailability_Object = MibTableColumn
capabilityCableAvailability = _CapabilityCableAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 2, 1, 2),
    _CapabilityCableAvailability_Type()
)
capabilityCableAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCableAvailability.setStatus("current")
_CapabilityCablePollInterval_Type = PollingInterval
_CapabilityCablePollInterval_Object = MibTableColumn
capabilityCablePollInterval = _CapabilityCablePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 7, 2, 1, 3),
    _CapabilityCablePollInterval_Type()
)
capabilityCablePollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityCablePollInterval.setStatus("current")
if mibBuilder.loadTexts:
    capabilityCablePollInterval.setUnits("millisecond")
_CapabilitySatellite_ObjectIdentity = ObjectIdentity
capabilitySatellite = _CapabilitySatellite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8)
)
_CapabilitySatelliteGroup_Type = GroupAvailability
_CapabilitySatelliteGroup_Object = MibScalar
capabilitySatelliteGroup = _CapabilitySatelliteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 1),
    _CapabilitySatelliteGroup_Type()
)
capabilitySatelliteGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilitySatelliteGroup.setStatus("current")
_CapabilitySatelliteTable_Object = MibTable
capabilitySatelliteTable = _CapabilitySatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    capabilitySatelliteTable.setStatus("current")
_CapabilitySatelliteEntry_Object = MibTableRow
capabilitySatelliteEntry = _CapabilitySatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 2, 1)
)
capabilitySatelliteEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "capabilitySatelliteOID"),
)
if mibBuilder.loadTexts:
    capabilitySatelliteEntry.setStatus("current")
_CapabilitySatelliteOID_Type = ObjectIdentifier
_CapabilitySatelliteOID_Object = MibTableColumn
capabilitySatelliteOID = _CapabilitySatelliteOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 2, 1, 1),
    _CapabilitySatelliteOID_Type()
)
capabilitySatelliteOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capabilitySatelliteOID.setStatus("current")
_CapabilitySatelliteAvailability_Type = Availability
_CapabilitySatelliteAvailability_Object = MibTableColumn
capabilitySatelliteAvailability = _CapabilitySatelliteAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 2, 1, 2),
    _CapabilitySatelliteAvailability_Type()
)
capabilitySatelliteAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilitySatelliteAvailability.setStatus("current")
_CapabilitySatellitePollInterval_Type = PollingInterval
_CapabilitySatellitePollInterval_Object = MibTableColumn
capabilitySatellitePollInterval = _CapabilitySatellitePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 8, 2, 1, 3),
    _CapabilitySatellitePollInterval_Type()
)
capabilitySatellitePollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilitySatellitePollInterval.setStatus("current")
if mibBuilder.loadTexts:
    capabilitySatellitePollInterval.setUnits("millisecond")
_CapabilityTerrestrial_ObjectIdentity = ObjectIdentity
capabilityTerrestrial = _CapabilityTerrestrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9)
)
_CapabilityTerrestrialGroup_Type = GroupAvailability
_CapabilityTerrestrialGroup_Object = MibScalar
capabilityTerrestrialGroup = _CapabilityTerrestrialGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 1),
    _CapabilityTerrestrialGroup_Type()
)
capabilityTerrestrialGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTerrestrialGroup.setStatus("current")
_CapabilityTerrestrialTable_Object = MibTable
capabilityTerrestrialTable = _CapabilityTerrestrialTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    capabilityTerrestrialTable.setStatus("current")
_CapabilityTerrestrialEntry_Object = MibTableRow
capabilityTerrestrialEntry = _CapabilityTerrestrialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 2, 1)
)
capabilityTerrestrialEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "capabilityTerrestrialOID"),
)
if mibBuilder.loadTexts:
    capabilityTerrestrialEntry.setStatus("current")
_CapabilityTerrestrialOID_Type = ObjectIdentifier
_CapabilityTerrestrialOID_Object = MibTableColumn
capabilityTerrestrialOID = _CapabilityTerrestrialOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 2, 1, 1),
    _CapabilityTerrestrialOID_Type()
)
capabilityTerrestrialOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capabilityTerrestrialOID.setStatus("current")
_CapabilityTerrestrialAvailability_Type = Availability
_CapabilityTerrestrialAvailability_Object = MibTableColumn
capabilityTerrestrialAvailability = _CapabilityTerrestrialAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 2, 1, 2),
    _CapabilityTerrestrialAvailability_Type()
)
capabilityTerrestrialAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTerrestrialAvailability.setStatus("current")
_CapabilityTerrestrialPollInterval_Type = PollingInterval
_CapabilityTerrestrialPollInterval_Object = MibTableColumn
capabilityTerrestrialPollInterval = _CapabilityTerrestrialPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 3, 9, 2, 1, 3),
    _CapabilityTerrestrialPollInterval_Type()
)
capabilityTerrestrialPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityTerrestrialPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    capabilityTerrestrialPollInterval.setUnits("millisecond")
_Tr101290TS_ObjectIdentity = ObjectIdentity
tr101290TS = _Tr101290TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5)
)
_TsTests_ObjectIdentity = ObjectIdentity
tsTests = _TsTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2)
)
_TsTestsSummaryTable_Object = MibTable
tsTestsSummaryTable = _TsTestsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    tsTestsSummaryTable.setStatus("current")
_TsTestsSummaryEntry_Object = MibTableRow
tsTestsSummaryEntry = _TsTestsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1)
)
tsTestsSummaryEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsTestsSummaryTestNumber"),
    (0, "DVB-MGTR101290-MIB", "tsTestsSummaryInputNumber"),
)
if mibBuilder.loadTexts:
    tsTestsSummaryEntry.setStatus("current")
_TsTestsSummaryInputNumber_Type = InputNumber
_TsTestsSummaryInputNumber_Object = MibTableColumn
tsTestsSummaryInputNumber = _TsTestsSummaryInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 1),
    _TsTestsSummaryInputNumber_Type()
)
tsTestsSummaryInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsSummaryInputNumber.setStatus("current")
_TsTestsSummaryTestNumber_Type = IndexTransportStreamTest
_TsTestsSummaryTestNumber_Object = MibTableColumn
tsTestsSummaryTestNumber = _TsTestsSummaryTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 2),
    _TsTestsSummaryTestNumber_Type()
)
tsTestsSummaryTestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsSummaryTestNumber.setStatus("current")
_TsTestsSummaryState_Type = TestState
_TsTestsSummaryState_Object = MibTableColumn
tsTestsSummaryState = _TsTestsSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 3),
    _TsTestsSummaryState_Type()
)
tsTestsSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsSummaryState.setStatus("current")


class _TsTestsSummaryEnable_Type(Enable):
    """Custom type tsTestsSummaryEnable based on Enable"""
    defaultBinValue = "1"


_TsTestsSummaryEnable_Object = MibTableColumn
tsTestsSummaryEnable = _TsTestsSummaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 4),
    _TsTestsSummaryEnable_Type()
)
tsTestsSummaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsSummaryEnable.setStatus("current")
_TsTestsSummaryCounter_Type = Counter32
_TsTestsSummaryCounter_Object = MibTableColumn
tsTestsSummaryCounter = _TsTestsSummaryCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 5),
    _TsTestsSummaryCounter_Type()
)
tsTestsSummaryCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsSummaryCounter.setStatus("current")
_TsTestsSummaryCounterDiscontinuity_Type = DateAndTime
_TsTestsSummaryCounterDiscontinuity_Object = MibTableColumn
tsTestsSummaryCounterDiscontinuity = _TsTestsSummaryCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 6),
    _TsTestsSummaryCounterDiscontinuity_Type()
)
tsTestsSummaryCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsSummaryCounterDiscontinuity.setStatus("current")
_TsTestsSummaryCounterReset_Type = TruthValue
_TsTestsSummaryCounterReset_Object = MibTableColumn
tsTestsSummaryCounterReset = _TsTestsSummaryCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 7),
    _TsTestsSummaryCounterReset_Type()
)
tsTestsSummaryCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsSummaryCounterReset.setStatus("current")
_TsTestsSummaryLatestError_Type = DateAndTime
_TsTestsSummaryLatestError_Object = MibTableColumn
tsTestsSummaryLatestError = _TsTestsSummaryLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 8),
    _TsTestsSummaryLatestError_Type()
)
tsTestsSummaryLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsSummaryLatestError.setStatus("current")
_TsTestsSummaryActiveTime_Type = ActiveTime
_TsTestsSummaryActiveTime_Object = MibTableColumn
tsTestsSummaryActiveTime = _TsTestsSummaryActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 2, 1, 9),
    _TsTestsSummaryActiveTime_Type()
)
tsTestsSummaryActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsSummaryActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsSummaryActiveTime.setUnits("second")
_TsTestsPIDTable_Object = MibTable
tsTestsPIDTable = _TsTestsPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    tsTestsPIDTable.setStatus("current")
_TsTestsPIDEntry_Object = MibTableRow
tsTestsPIDEntry = _TsTestsPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1)
)
tsTestsPIDEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsTestsPIDPID"),
    (0, "DVB-MGTR101290-MIB", "tsTestsPIDTestNumber"),
    (0, "DVB-MGTR101290-MIB", "tsTestsPIDInputNumber"),
)
if mibBuilder.loadTexts:
    tsTestsPIDEntry.setStatus("current")
_TsTestsPIDInputNumber_Type = InputNumber
_TsTestsPIDInputNumber_Object = MibTableColumn
tsTestsPIDInputNumber = _TsTestsPIDInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 1),
    _TsTestsPIDInputNumber_Type()
)
tsTestsPIDInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPIDInputNumber.setStatus("current")
_TsTestsPIDPID_Type = PIDPlusOne
_TsTestsPIDPID_Object = MibTableColumn
tsTestsPIDPID = _TsTestsPIDPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 2),
    _TsTestsPIDPID_Type()
)
tsTestsPIDPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPIDPID.setStatus("current")
_TsTestsPIDTestNumber_Type = IndexTransportStreamTest
_TsTestsPIDTestNumber_Object = MibTableColumn
tsTestsPIDTestNumber = _TsTestsPIDTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 3),
    _TsTestsPIDTestNumber_Type()
)
tsTestsPIDTestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPIDTestNumber.setStatus("current")


class _TsTestsPIDRowStatus_Type(RowStatus):
    """Custom type tsTestsPIDRowStatus based on RowStatus"""


_TsTestsPIDRowStatus_Object = MibTableColumn
tsTestsPIDRowStatus = _TsTestsPIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 4),
    _TsTestsPIDRowStatus_Type()
)
tsTestsPIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsTestsPIDRowStatus.setStatus("current")
_TsTestsPIDState_Type = TestState
_TsTestsPIDState_Object = MibTableColumn
tsTestsPIDState = _TsTestsPIDState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 5),
    _TsTestsPIDState_Type()
)
tsTestsPIDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsPIDState.setStatus("current")


class _TsTestsPIDEnable_Type(Enable):
    """Custom type tsTestsPIDEnable based on Enable"""
    defaultBinValue = "1"


_TsTestsPIDEnable_Object = MibTableColumn
tsTestsPIDEnable = _TsTestsPIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 6),
    _TsTestsPIDEnable_Type()
)
tsTestsPIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsTestsPIDEnable.setStatus("current")
_TsTestsPIDCounter_Type = Counter32
_TsTestsPIDCounter_Object = MibTableColumn
tsTestsPIDCounter = _TsTestsPIDCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 7),
    _TsTestsPIDCounter_Type()
)
tsTestsPIDCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsPIDCounter.setStatus("current")
_TsTestsPIDCounterDiscontinuity_Type = DateAndTime
_TsTestsPIDCounterDiscontinuity_Object = MibTableColumn
tsTestsPIDCounterDiscontinuity = _TsTestsPIDCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 8),
    _TsTestsPIDCounterDiscontinuity_Type()
)
tsTestsPIDCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsPIDCounterDiscontinuity.setStatus("current")


class _TsTestsPIDCounterReset_Type(TruthValue):
    """Custom type tsTestsPIDCounterReset based on TruthValue"""


_TsTestsPIDCounterReset_Object = MibTableColumn
tsTestsPIDCounterReset = _TsTestsPIDCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 9),
    _TsTestsPIDCounterReset_Type()
)
tsTestsPIDCounterReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsTestsPIDCounterReset.setStatus("current")
_TsTestsPIDLatestError_Type = DateAndTime
_TsTestsPIDLatestError_Object = MibTableColumn
tsTestsPIDLatestError = _TsTestsPIDLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 10),
    _TsTestsPIDLatestError_Type()
)
tsTestsPIDLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsPIDLatestError.setStatus("current")
_TsTestsPIDActiveTime_Type = ActiveTime
_TsTestsPIDActiveTime_Object = MibTableColumn
tsTestsPIDActiveTime = _TsTestsPIDActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 3, 1, 11),
    _TsTestsPIDActiveTime_Type()
)
tsTestsPIDActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTestsPIDActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPIDActiveTime.setUnits("second")
_TsTestsPreferences_ObjectIdentity = ObjectIdentity
tsTestsPreferences = _TsTestsPreferences_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100)
)
_TsTestsPreferencesTable_Object = MibTable
tsTestsPreferencesTable = _TsTestsPreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1)
)
if mibBuilder.loadTexts:
    tsTestsPreferencesTable.setStatus("current")
_TsTestsPreferencesEntry_Object = MibTableRow
tsTestsPreferencesEntry = _TsTestsPreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1)
)
tsTestsPreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsTestsPrefInputNumber"),
)
if mibBuilder.loadTexts:
    tsTestsPreferencesEntry.setStatus("current")
_TsTestsPrefInputNumber_Type = InputNumber
_TsTestsPrefInputNumber_Object = MibTableColumn
tsTestsPrefInputNumber = _TsTestsPrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 1),
    _TsTestsPrefInputNumber_Type()
)
tsTestsPrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPrefInputNumber.setStatus("current")


class _TsTestsPrefTransitionDuration_Type(FloatingPoint):
    """Custom type tsTestsPrefTransitionDuration based on FloatingPoint"""
    defaultValue = OctetString("0.5")


_TsTestsPrefTransitionDuration_Object = MibTableColumn
tsTestsPrefTransitionDuration = _TsTestsPrefTransitionDuration_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 2),
    _TsTestsPrefTransitionDuration_Type()
)
tsTestsPrefTransitionDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefTransitionDuration.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefTransitionDuration.setUnits("second")


class _TsTestsPrefPATSectionIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPATSectionIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("0.5")


_TsTestsPrefPATSectionIntervalMax_Object = MibTableColumn
tsTestsPrefPATSectionIntervalMax = _TsTestsPrefPATSectionIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 3),
    _TsTestsPrefPATSectionIntervalMax_Type()
)
tsTestsPrefPATSectionIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPATSectionIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPATSectionIntervalMax.setUnits("second")


class _TsTestsPrefPMTSectionIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPMTSectionIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("0.5")


_TsTestsPrefPMTSectionIntervalMax_Object = MibTableColumn
tsTestsPrefPMTSectionIntervalMax = _TsTestsPrefPMTSectionIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 4),
    _TsTestsPrefPMTSectionIntervalMax_Type()
)
tsTestsPrefPMTSectionIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPMTSectionIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPMTSectionIntervalMax.setUnits("second")


class _TsTestsPrefReferredIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefReferredIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("5")


_TsTestsPrefReferredIntervalMax_Object = MibTableColumn
tsTestsPrefReferredIntervalMax = _TsTestsPrefReferredIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 5),
    _TsTestsPrefReferredIntervalMax_Type()
)
tsTestsPrefReferredIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefReferredIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefReferredIntervalMax.setUnits("s")


class _TsTestsPrefPCRIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPCRIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("0.04")


_TsTestsPrefPCRIntervalMax_Object = MibTableColumn
tsTestsPrefPCRIntervalMax = _TsTestsPrefPCRIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 6),
    _TsTestsPrefPCRIntervalMax_Type()
)
tsTestsPrefPCRIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPCRIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPCRIntervalMax.setUnits("second")


class _TsTestsPrefPCRDiscontinuityMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPCRDiscontinuityMax based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsTestsPrefPCRDiscontinuityMax_Object = MibTableColumn
tsTestsPrefPCRDiscontinuityMax = _TsTestsPrefPCRDiscontinuityMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 7),
    _TsTestsPrefPCRDiscontinuityMax_Type()
)
tsTestsPrefPCRDiscontinuityMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPCRDiscontinuityMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPCRDiscontinuityMax.setUnits("second")


class _TsTestsPrefPCRInaccuracyMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPCRInaccuracyMax based on FloatingPoint"""
    defaultValue = OctetString("500E-9")


_TsTestsPrefPCRInaccuracyMax_Object = MibTableColumn
tsTestsPrefPCRInaccuracyMax = _TsTestsPrefPCRInaccuracyMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 8),
    _TsTestsPrefPCRInaccuracyMax_Type()
)
tsTestsPrefPCRInaccuracyMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPCRInaccuracyMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPCRInaccuracyMax.setUnits("second")


class _TsTestsPrefPTSIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefPTSIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("0.7")


_TsTestsPrefPTSIntervalMax_Object = MibTableColumn
tsTestsPrefPTSIntervalMax = _TsTestsPrefPTSIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 9),
    _TsTestsPrefPTSIntervalMax_Type()
)
tsTestsPrefPTSIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPTSIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPTSIntervalMax.setUnits("second")


class _TsTestsPrefNITActualIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefNITActualIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefNITActualIntervalMax_Object = MibTableColumn
tsTestsPrefNITActualIntervalMax = _TsTestsPrefNITActualIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 10),
    _TsTestsPrefNITActualIntervalMax_Type()
)
tsTestsPrefNITActualIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefNITActualIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefNITActualIntervalMax.setUnits("second")


class _TsTestsPrefNITActualIntervalMin_Type(FloatingPoint):
    """Custom type tsTestsPrefNITActualIntervalMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefNITActualIntervalMin_Object = MibTableColumn
tsTestsPrefNITActualIntervalMin = _TsTestsPrefNITActualIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 11),
    _TsTestsPrefNITActualIntervalMin_Type()
)
tsTestsPrefNITActualIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefNITActualIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefNITActualIntervalMin.setUnits("second")


class _TsTestsPrefNITOtherIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefNITOtherIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefNITOtherIntervalMax_Object = MibTableColumn
tsTestsPrefNITOtherIntervalMax = _TsTestsPrefNITOtherIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 12),
    _TsTestsPrefNITOtherIntervalMax_Type()
)
tsTestsPrefNITOtherIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefNITOtherIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefNITOtherIntervalMax.setUnits("second")


class _TsTestsPrefSIGapMin_Type(FloatingPoint):
    """Custom type tsTestsPrefSIGapMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefSIGapMin_Object = MibTableColumn
tsTestsPrefSIGapMin = _TsTestsPrefSIGapMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 13),
    _TsTestsPrefSIGapMin_Type()
)
tsTestsPrefSIGapMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSIGapMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSIGapMin.setUnits("second")


class _TsTestsPrefNITTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefNITTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefNITTableIntervalMax_Object = MibTableColumn
tsTestsPrefNITTableIntervalMax = _TsTestsPrefNITTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 14),
    _TsTestsPrefNITTableIntervalMax_Type()
)
tsTestsPrefNITTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefNITTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefNITTableIntervalMax.setUnits("second")


class _TsTestsPrefBATTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefBATTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefBATTableIntervalMax_Object = MibTableColumn
tsTestsPrefBATTableIntervalMax = _TsTestsPrefBATTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 15),
    _TsTestsPrefBATTableIntervalMax_Type()
)
tsTestsPrefBATTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefBATTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefBATTableIntervalMax.setUnits("second")


class _TsTestsPrefSDTActualTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefSDTActualTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("2")


_TsTestsPrefSDTActualTableIntervalMax_Object = MibTableColumn
tsTestsPrefSDTActualTableIntervalMax = _TsTestsPrefSDTActualTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 16),
    _TsTestsPrefSDTActualTableIntervalMax_Type()
)
tsTestsPrefSDTActualTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualTableIntervalMax.setUnits("second")


class _TsTestsPrefSDTOtherTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefSDTOtherTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefSDTOtherTableIntervalMax_Object = MibTableColumn
tsTestsPrefSDTOtherTableIntervalMax = _TsTestsPrefSDTOtherTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 17),
    _TsTestsPrefSDTOtherTableIntervalMax_Type()
)
tsTestsPrefSDTOtherTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSDTOtherTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSDTOtherTableIntervalMax.setUnits("second")


class _TsTestsPrefEITPFActualTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITPFActualTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("2")


_TsTestsPrefEITPFActualTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITPFActualTableIntervalMax = _TsTestsPrefEITPFActualTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 18),
    _TsTestsPrefEITPFActualTableIntervalMax_Type()
)
tsTestsPrefEITPFActualTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITPFActualTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITPFActualTableIntervalMax.setUnits("second")


class _TsTestsPrefEITPFOtherTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITPFOtherTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefEITPFOtherTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITPFOtherTableIntervalMax = _TsTestsPrefEITPFOtherTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 19),
    _TsTestsPrefEITPFOtherTableIntervalMax_Type()
)
tsTestsPrefEITPFOtherTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITPFOtherTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITPFOtherTableIntervalMax.setUnits("second")


class _TsTestsPrefEITSActualNearTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITSActualNearTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefEITSActualNearTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITSActualNearTableIntervalMax = _TsTestsPrefEITSActualNearTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 20),
    _TsTestsPrefEITSActualNearTableIntervalMax_Type()
)
tsTestsPrefEITSActualNearTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITSActualNearTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITSActualNearTableIntervalMax.setUnits("second")


class _TsTestsPrefEITSActualFarTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITSActualFarTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefEITSActualFarTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITSActualFarTableIntervalMax = _TsTestsPrefEITSActualFarTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 21),
    _TsTestsPrefEITSActualFarTableIntervalMax_Type()
)
tsTestsPrefEITSActualFarTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITSActualFarTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITSActualFarTableIntervalMax.setUnits("second")


class _TsTestsPrefEITSOtherNearTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITSOtherNearTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefEITSOtherNearTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITSOtherNearTableIntervalMax = _TsTestsPrefEITSOtherNearTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 22),
    _TsTestsPrefEITSOtherNearTableIntervalMax_Type()
)
tsTestsPrefEITSOtherNearTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITSOtherNearTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITSOtherNearTableIntervalMax.setUnits("second")


class _TsTestsPrefEITSOtherFarTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITSOtherFarTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("30")


_TsTestsPrefEITSOtherFarTableIntervalMax_Object = MibTableColumn
tsTestsPrefEITSOtherFarTableIntervalMax = _TsTestsPrefEITSOtherFarTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 23),
    _TsTestsPrefEITSOtherFarTableIntervalMax_Type()
)
tsTestsPrefEITSOtherFarTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITSOtherFarTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITSOtherFarTableIntervalMax.setUnits("second")


class _TsTestsPrefTxTTableIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefTxTTableIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("30")


_TsTestsPrefTxTTableIntervalMax_Object = MibTableColumn
tsTestsPrefTxTTableIntervalMax = _TsTestsPrefTxTTableIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 24),
    _TsTestsPrefTxTTableIntervalMax_Type()
)
tsTestsPrefTxTTableIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefTxTTableIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefTxTTableIntervalMax.setUnits("second")


class _TsTestsPrefSDTActualIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefSDTActualIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("2")


_TsTestsPrefSDTActualIntervalMax_Object = MibTableColumn
tsTestsPrefSDTActualIntervalMax = _TsTestsPrefSDTActualIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 25),
    _TsTestsPrefSDTActualIntervalMax_Type()
)
tsTestsPrefSDTActualIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualIntervalMax.setUnits("second")


class _TsTestsPrefSDTActualIntervalMin_Type(FloatingPoint):
    """Custom type tsTestsPrefSDTActualIntervalMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefSDTActualIntervalMin_Object = MibTableColumn
tsTestsPrefSDTActualIntervalMin = _TsTestsPrefSDTActualIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 26),
    _TsTestsPrefSDTActualIntervalMin_Type()
)
tsTestsPrefSDTActualIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSDTActualIntervalMin.setUnits("second")


class _TsTestsPrefSDTOtherIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefSDTOtherIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefSDTOtherIntervalMax_Object = MibTableColumn
tsTestsPrefSDTOtherIntervalMax = _TsTestsPrefSDTOtherIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 27),
    _TsTestsPrefSDTOtherIntervalMax_Type()
)
tsTestsPrefSDTOtherIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefSDTOtherIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefSDTOtherIntervalMax.setUnits("second")


class _TsTestsPrefEITActualIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITActualIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("2")


_TsTestsPrefEITActualIntervalMax_Object = MibTableColumn
tsTestsPrefEITActualIntervalMax = _TsTestsPrefEITActualIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 28),
    _TsTestsPrefEITActualIntervalMax_Type()
)
tsTestsPrefEITActualIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITActualIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITActualIntervalMax.setUnits("second")


class _TsTestsPrefEITActualIntervalMin_Type(FloatingPoint):
    """Custom type tsTestsPrefEITActualIntervalMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefEITActualIntervalMin_Object = MibTableColumn
tsTestsPrefEITActualIntervalMin = _TsTestsPrefEITActualIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 29),
    _TsTestsPrefEITActualIntervalMin_Type()
)
tsTestsPrefEITActualIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITActualIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITActualIntervalMin.setUnits("second")


class _TsTestsPrefEITOtherIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefEITOtherIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefEITOtherIntervalMax_Object = MibTableColumn
tsTestsPrefEITOtherIntervalMax = _TsTestsPrefEITOtherIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 30),
    _TsTestsPrefEITOtherIntervalMax_Type()
)
tsTestsPrefEITOtherIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefEITOtherIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefEITOtherIntervalMax.setUnits("second")


class _TsTestsPrefRSTIntervalMin_Type(FloatingPoint):
    """Custom type tsTestsPrefRSTIntervalMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefRSTIntervalMin_Object = MibTableColumn
tsTestsPrefRSTIntervalMin = _TsTestsPrefRSTIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 31),
    _TsTestsPrefRSTIntervalMin_Type()
)
tsTestsPrefRSTIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefRSTIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefRSTIntervalMin.setUnits("second")


class _TsTestsPrefTDTIntervalMax_Type(FloatingPoint):
    """Custom type tsTestsPrefTDTIntervalMax based on FloatingPoint"""
    defaultValue = OctetString("10")


_TsTestsPrefTDTIntervalMax_Object = MibTableColumn
tsTestsPrefTDTIntervalMax = _TsTestsPrefTDTIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 32),
    _TsTestsPrefTDTIntervalMax_Type()
)
tsTestsPrefTDTIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefTDTIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefTDTIntervalMax.setUnits("second")


class _TsTestsPrefTDTIntervalMin_Type(FloatingPoint):
    """Custom type tsTestsPrefTDTIntervalMin based on FloatingPoint"""
    defaultValue = OctetString("0.025")


_TsTestsPrefTDTIntervalMin_Object = MibTableColumn
tsTestsPrefTDTIntervalMin = _TsTestsPrefTDTIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 1, 1, 33),
    _TsTestsPrefTDTIntervalMin_Type()
)
tsTestsPrefTDTIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefTDTIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefTDTIntervalMin.setUnits("second")
_TsTestsPreferencesPIDTable_Object = MibTable
tsTestsPreferencesPIDTable = _TsTestsPreferencesPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2)
)
if mibBuilder.loadTexts:
    tsTestsPreferencesPIDTable.setStatus("current")
_TsTestsPreferencesPIDEntry_Object = MibTableRow
tsTestsPreferencesPIDEntry = _TsTestsPreferencesPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2, 1)
)
tsTestsPreferencesPIDEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsTestsPrefPIDInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsTestsPrefPIDPID"),
)
if mibBuilder.loadTexts:
    tsTestsPreferencesPIDEntry.setStatus("current")
_TsTestsPrefPIDInputNumber_Type = InputNumber
_TsTestsPrefPIDInputNumber_Object = MibTableColumn
tsTestsPrefPIDInputNumber = _TsTestsPrefPIDInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2, 1, 1),
    _TsTestsPrefPIDInputNumber_Type()
)
tsTestsPrefPIDInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPrefPIDInputNumber.setStatus("current")
_TsTestsPrefPIDPID_Type = PIDPlusOne
_TsTestsPrefPIDPID_Object = MibTableColumn
tsTestsPrefPIDPID = _TsTestsPrefPIDPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2, 1, 2),
    _TsTestsPrefPIDPID_Type()
)
tsTestsPrefPIDPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTestsPrefPIDPID.setStatus("current")
_TsTestsPrefPIDRowStatus_Type = RowStatus
_TsTestsPrefPIDRowStatus_Object = MibTableColumn
tsTestsPrefPIDRowStatus = _TsTestsPrefPIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2, 1, 3),
    _TsTestsPrefPIDRowStatus_Type()
)
tsTestsPrefPIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsTestsPrefPIDRowStatus.setStatus("current")
_TsTestsPrefPIDReferredIntervalMax_Type = FloatingPoint
_TsTestsPrefPIDReferredIntervalMax_Object = MibTableColumn
tsTestsPrefPIDReferredIntervalMax = _TsTestsPrefPIDReferredIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 2, 100, 2, 1, 4),
    _TsTestsPrefPIDReferredIntervalMax_Type()
)
tsTestsPrefPIDReferredIntervalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTestsPrefPIDReferredIntervalMax.setStatus("current")
if mibBuilder.loadTexts:
    tsTestsPrefPIDReferredIntervalMax.setUnits("second")
_TsMeasurements_ObjectIdentity = ObjectIdentity
tsMeasurements = _TsMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4)
)
_TsPcrMeasurementTable_Object = MibTable
tsPcrMeasurementTable = _TsPcrMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tsPcrMeasurementTable.setStatus("current")
_TsPcrMeasurementEntry_Object = MibTableRow
tsPcrMeasurementEntry = _TsPcrMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1)
)
tsPcrMeasurementEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsPcrMeasurementPID"),
    (0, "DVB-MGTR101290-MIB", "tsPcrMeasurementNumber"),
    (0, "DVB-MGTR101290-MIB", "tsPcrMeasurementInputNumber"),
)
if mibBuilder.loadTexts:
    tsPcrMeasurementEntry.setStatus("current")
_TsPcrMeasurementInputNumber_Type = InputNumber
_TsPcrMeasurementInputNumber_Object = MibTableColumn
tsPcrMeasurementInputNumber = _TsPcrMeasurementInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 1),
    _TsPcrMeasurementInputNumber_Type()
)
tsPcrMeasurementInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsPcrMeasurementInputNumber.setStatus("current")
_TsPcrMeasurementPID_Type = PIDPlusOne
_TsPcrMeasurementPID_Object = MibTableColumn
tsPcrMeasurementPID = _TsPcrMeasurementPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 2),
    _TsPcrMeasurementPID_Type()
)
tsPcrMeasurementPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsPcrMeasurementPID.setStatus("current")
_TsPcrMeasurementNumber_Type = IndexPCRMeasurement
_TsPcrMeasurementNumber_Object = MibTableColumn
tsPcrMeasurementNumber = _TsPcrMeasurementNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 3),
    _TsPcrMeasurementNumber_Type()
)
tsPcrMeasurementNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsPcrMeasurementNumber.setStatus("current")


class _TsPcrMeasurementRowStatus_Type(RowStatus):
    """Custom type tsPcrMeasurementRowStatus based on RowStatus"""


_TsPcrMeasurementRowStatus_Object = MibTableColumn
tsPcrMeasurementRowStatus = _TsPcrMeasurementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 4),
    _TsPcrMeasurementRowStatus_Type()
)
tsPcrMeasurementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPcrMeasurementRowStatus.setStatus("current")
_TsPcrMeasurementState_Type = TestState
_TsPcrMeasurementState_Object = MibTableColumn
tsPcrMeasurementState = _TsPcrMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 5),
    _TsPcrMeasurementState_Type()
)
tsPcrMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementState.setStatus("current")


class _TsPcrMeasurementEnable_Type(Enable):
    """Custom type tsPcrMeasurementEnable based on Enable"""
    defaultBinValue = "1"


_TsPcrMeasurementEnable_Object = MibTableColumn
tsPcrMeasurementEnable = _TsPcrMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 6),
    _TsPcrMeasurementEnable_Type()
)
tsPcrMeasurementEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPcrMeasurementEnable.setStatus("current")
_TsPcrMeasurementCounter_Type = Counter32
_TsPcrMeasurementCounter_Object = MibTableColumn
tsPcrMeasurementCounter = _TsPcrMeasurementCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 7),
    _TsPcrMeasurementCounter_Type()
)
tsPcrMeasurementCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementCounter.setStatus("current")
_TsPcrMeasurementCounterDiscontinuity_Type = DateAndTime
_TsPcrMeasurementCounterDiscontinuity_Object = MibTableColumn
tsPcrMeasurementCounterDiscontinuity = _TsPcrMeasurementCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 8),
    _TsPcrMeasurementCounterDiscontinuity_Type()
)
tsPcrMeasurementCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementCounterDiscontinuity.setStatus("current")


class _TsPcrMeasurementCounterReset_Type(TruthValue):
    """Custom type tsPcrMeasurementCounterReset based on TruthValue"""


_TsPcrMeasurementCounterReset_Object = MibTableColumn
tsPcrMeasurementCounterReset = _TsPcrMeasurementCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 9),
    _TsPcrMeasurementCounterReset_Type()
)
tsPcrMeasurementCounterReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPcrMeasurementCounterReset.setStatus("current")
_TsPcrMeasurementLatestError_Type = DateAndTime
_TsPcrMeasurementLatestError_Object = MibTableColumn
tsPcrMeasurementLatestError = _TsPcrMeasurementLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 10),
    _TsPcrMeasurementLatestError_Type()
)
tsPcrMeasurementLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementLatestError.setStatus("current")
_TsPcrMeasurementActiveTime_Type = ActiveTime
_TsPcrMeasurementActiveTime_Object = MibTableColumn
tsPcrMeasurementActiveTime = _TsPcrMeasurementActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 11),
    _TsPcrMeasurementActiveTime_Type()
)
tsPcrMeasurementActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsPcrMeasurementActiveTime.setUnits("second")
_TsPcrMeasurementMeasurementState_Type = MeasurementState
_TsPcrMeasurementMeasurementState_Object = MibTableColumn
tsPcrMeasurementMeasurementState = _TsPcrMeasurementMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 12),
    _TsPcrMeasurementMeasurementState_Type()
)
tsPcrMeasurementMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementMeasurementState.setStatus("current")
_TsPcrMeasurementValue_Type = FloatingPoint
_TsPcrMeasurementValue_Object = MibTableColumn
tsPcrMeasurementValue = _TsPcrMeasurementValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 1, 1, 13),
    _TsPcrMeasurementValue_Type()
)
tsPcrMeasurementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPcrMeasurementValue.setStatus("current")
_BitRate_ObjectIdentity = ObjectIdentity
bitRate = _BitRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2)
)
_TsTransportStreamBitRateTable_Object = MibTable
tsTransportStreamBitRateTable = _TsTransportStreamBitRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tsTransportStreamBitRateTable.setStatus("current")
_TsTransportStreamBitRateEntry_Object = MibTableRow
tsTransportStreamBitRateEntry = _TsTransportStreamBitRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1)
)
tsTransportStreamBitRateEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsTransportStreamBitRateInputNumber"),
)
if mibBuilder.loadTexts:
    tsTransportStreamBitRateEntry.setStatus("current")
_TsTransportStreamBitRateInputNumber_Type = InputNumber
_TsTransportStreamBitRateInputNumber_Object = MibTableColumn
tsTransportStreamBitRateInputNumber = _TsTransportStreamBitRateInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 1),
    _TsTransportStreamBitRateInputNumber_Type()
)
tsTransportStreamBitRateInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateInputNumber.setStatus("current")
_TsTransportStreamBitRateState_Type = TestState
_TsTransportStreamBitRateState_Object = MibTableColumn
tsTransportStreamBitRateState = _TsTransportStreamBitRateState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 2),
    _TsTransportStreamBitRateState_Type()
)
tsTransportStreamBitRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateState.setStatus("current")
_TsTransportStreamBitRateEnable_Type = Enable
_TsTransportStreamBitRateEnable_Object = MibTableColumn
tsTransportStreamBitRateEnable = _TsTransportStreamBitRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 3),
    _TsTransportStreamBitRateEnable_Type()
)
tsTransportStreamBitRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateEnable.setStatus("current")
_TsTransportStreamBitRateCounter_Type = Counter32
_TsTransportStreamBitRateCounter_Object = MibTableColumn
tsTransportStreamBitRateCounter = _TsTransportStreamBitRateCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 4),
    _TsTransportStreamBitRateCounter_Type()
)
tsTransportStreamBitRateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateCounter.setStatus("current")
_TsTransportStreamBitRateCounterDiscontinuity_Type = DateAndTime
_TsTransportStreamBitRateCounterDiscontinuity_Object = MibTableColumn
tsTransportStreamBitRateCounterDiscontinuity = _TsTransportStreamBitRateCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 5),
    _TsTransportStreamBitRateCounterDiscontinuity_Type()
)
tsTransportStreamBitRateCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateCounterDiscontinuity.setStatus("current")


class _TsTransportStreamBitRateCounterReset_Type(TruthValue):
    """Custom type tsTransportStreamBitRateCounterReset based on TruthValue"""


_TsTransportStreamBitRateCounterReset_Object = MibTableColumn
tsTransportStreamBitRateCounterReset = _TsTransportStreamBitRateCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 6),
    _TsTransportStreamBitRateCounterReset_Type()
)
tsTransportStreamBitRateCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateCounterReset.setStatus("current")
_TsTransportStreamBitRateLatestError_Type = DateAndTime
_TsTransportStreamBitRateLatestError_Object = MibTableColumn
tsTransportStreamBitRateLatestError = _TsTransportStreamBitRateLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 7),
    _TsTransportStreamBitRateLatestError_Type()
)
tsTransportStreamBitRateLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateLatestError.setStatus("current")
_TsTransportStreamBitRateActiveTime_Type = ActiveTime
_TsTransportStreamBitRateActiveTime_Object = MibTableColumn
tsTransportStreamBitRateActiveTime = _TsTransportStreamBitRateActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 8),
    _TsTransportStreamBitRateActiveTime_Type()
)
tsTransportStreamBitRateActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateActiveTime.setUnits("second")
_TsTransportStreamBitRateMeasurementState_Type = MeasurementState
_TsTransportStreamBitRateMeasurementState_Object = MibTableColumn
tsTransportStreamBitRateMeasurementState = _TsTransportStreamBitRateMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 9),
    _TsTransportStreamBitRateMeasurementState_Type()
)
tsTransportStreamBitRateMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateMeasurementState.setStatus("current")
_TsTransportStreamBitRateValue_Type = FloatingPoint
_TsTransportStreamBitRateValue_Object = MibTableColumn
tsTransportStreamBitRateValue = _TsTransportStreamBitRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 10),
    _TsTransportStreamBitRateValue_Type()
)
tsTransportStreamBitRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateValue.setStatus("current")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateValue.setUnits("bit/s")
_TsTransportStreamBitRateNomenclature_Type = DisplayString
_TsTransportStreamBitRateNomenclature_Object = MibTableColumn
tsTransportStreamBitRateNomenclature = _TsTransportStreamBitRateNomenclature_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 1, 1, 11),
    _TsTransportStreamBitRateNomenclature_Type()
)
tsTransportStreamBitRateNomenclature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTransportStreamBitRateNomenclature.setStatus("current")
_TsServiceBitRateTable_Object = MibTable
tsServiceBitRateTable = _TsServiceBitRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    tsServiceBitRateTable.setStatus("current")
_TsServiceBitRateEntry_Object = MibTableRow
tsServiceBitRateEntry = _TsServiceBitRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1)
)
tsServiceBitRateEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsServiceBitRateService"),
    (0, "DVB-MGTR101290-MIB", "tsServiceBitRateInputNumber"),
)
if mibBuilder.loadTexts:
    tsServiceBitRateEntry.setStatus("current")
_TsServiceBitRateInputNumber_Type = InputNumber
_TsServiceBitRateInputNumber_Object = MibTableColumn
tsServiceBitRateInputNumber = _TsServiceBitRateInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 1),
    _TsServiceBitRateInputNumber_Type()
)
tsServiceBitRateInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsServiceBitRateInputNumber.setStatus("current")
_TsServiceBitRateService_Type = ServiceId
_TsServiceBitRateService_Object = MibTableColumn
tsServiceBitRateService = _TsServiceBitRateService_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 2),
    _TsServiceBitRateService_Type()
)
tsServiceBitRateService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsServiceBitRateService.setStatus("current")


class _TsServiceBitRateRowStatus_Type(RowStatus):
    """Custom type tsServiceBitRateRowStatus based on RowStatus"""


_TsServiceBitRateRowStatus_Object = MibTableColumn
tsServiceBitRateRowStatus = _TsServiceBitRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 3),
    _TsServiceBitRateRowStatus_Type()
)
tsServiceBitRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsServiceBitRateRowStatus.setStatus("current")
_TsServiceBitRateState_Type = TestState
_TsServiceBitRateState_Object = MibTableColumn
tsServiceBitRateState = _TsServiceBitRateState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 4),
    _TsServiceBitRateState_Type()
)
tsServiceBitRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateState.setStatus("current")


class _TsServiceBitRateEnable_Type(Enable):
    """Custom type tsServiceBitRateEnable based on Enable"""
    defaultBinValue = "1"


_TsServiceBitRateEnable_Object = MibTableColumn
tsServiceBitRateEnable = _TsServiceBitRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 5),
    _TsServiceBitRateEnable_Type()
)
tsServiceBitRateEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsServiceBitRateEnable.setStatus("current")
_TsServiceBitRateCounter_Type = Counter32
_TsServiceBitRateCounter_Object = MibTableColumn
tsServiceBitRateCounter = _TsServiceBitRateCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 6),
    _TsServiceBitRateCounter_Type()
)
tsServiceBitRateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateCounter.setStatus("current")
_TsServiceBitRateCounterDiscontinuity_Type = DateAndTime
_TsServiceBitRateCounterDiscontinuity_Object = MibTableColumn
tsServiceBitRateCounterDiscontinuity = _TsServiceBitRateCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 7),
    _TsServiceBitRateCounterDiscontinuity_Type()
)
tsServiceBitRateCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateCounterDiscontinuity.setStatus("current")


class _TsServiceBitRateCounterReset_Type(TruthValue):
    """Custom type tsServiceBitRateCounterReset based on TruthValue"""


_TsServiceBitRateCounterReset_Object = MibTableColumn
tsServiceBitRateCounterReset = _TsServiceBitRateCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 8),
    _TsServiceBitRateCounterReset_Type()
)
tsServiceBitRateCounterReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsServiceBitRateCounterReset.setStatus("current")
_TsServiceBitRateLatestError_Type = DateAndTime
_TsServiceBitRateLatestError_Object = MibTableColumn
tsServiceBitRateLatestError = _TsServiceBitRateLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 9),
    _TsServiceBitRateLatestError_Type()
)
tsServiceBitRateLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateLatestError.setStatus("current")
_TsServiceBitRateActiveTime_Type = ActiveTime
_TsServiceBitRateActiveTime_Object = MibTableColumn
tsServiceBitRateActiveTime = _TsServiceBitRateActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 10),
    _TsServiceBitRateActiveTime_Type()
)
tsServiceBitRateActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsServiceBitRateActiveTime.setUnits("second")
_TsServiceBitRateMeasurementState_Type = MeasurementState
_TsServiceBitRateMeasurementState_Object = MibTableColumn
tsServiceBitRateMeasurementState = _TsServiceBitRateMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 11),
    _TsServiceBitRateMeasurementState_Type()
)
tsServiceBitRateMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateMeasurementState.setStatus("current")
_TsServiceBitRateValue_Type = FloatingPoint
_TsServiceBitRateValue_Object = MibTableColumn
tsServiceBitRateValue = _TsServiceBitRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 12),
    _TsServiceBitRateValue_Type()
)
tsServiceBitRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateValue.setStatus("current")
if mibBuilder.loadTexts:
    tsServiceBitRateValue.setUnits("bit/s")
_TsServiceBitRateNomenclature_Type = DisplayString
_TsServiceBitRateNomenclature_Object = MibTableColumn
tsServiceBitRateNomenclature = _TsServiceBitRateNomenclature_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 2, 1, 13),
    _TsServiceBitRateNomenclature_Type()
)
tsServiceBitRateNomenclature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServiceBitRateNomenclature.setStatus("current")
_TsPIDBitRateTable_Object = MibTable
tsPIDBitRateTable = _TsPIDBitRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    tsPIDBitRateTable.setStatus("current")
_TsPIDBitRateEntry_Object = MibTableRow
tsPIDBitRateEntry = _TsPIDBitRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1)
)
tsPIDBitRateEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsPIDBitRateInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsPIDBitRatePID"),
)
if mibBuilder.loadTexts:
    tsPIDBitRateEntry.setStatus("current")
_TsPIDBitRateInputNumber_Type = InputNumber
_TsPIDBitRateInputNumber_Object = MibTableColumn
tsPIDBitRateInputNumber = _TsPIDBitRateInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 1),
    _TsPIDBitRateInputNumber_Type()
)
tsPIDBitRateInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsPIDBitRateInputNumber.setStatus("current")
_TsPIDBitRatePID_Type = PIDPlusOne
_TsPIDBitRatePID_Object = MibTableColumn
tsPIDBitRatePID = _TsPIDBitRatePID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 2),
    _TsPIDBitRatePID_Type()
)
tsPIDBitRatePID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsPIDBitRatePID.setStatus("current")


class _TsPIDBitRateRowStatus_Type(RowStatus):
    """Custom type tsPIDBitRateRowStatus based on RowStatus"""


_TsPIDBitRateRowStatus_Object = MibTableColumn
tsPIDBitRateRowStatus = _TsPIDBitRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 3),
    _TsPIDBitRateRowStatus_Type()
)
tsPIDBitRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPIDBitRateRowStatus.setStatus("current")
_TsPIDBitRateState_Type = TestState
_TsPIDBitRateState_Object = MibTableColumn
tsPIDBitRateState = _TsPIDBitRateState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 4),
    _TsPIDBitRateState_Type()
)
tsPIDBitRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateState.setStatus("current")


class _TsPIDBitRateEnable_Type(Enable):
    """Custom type tsPIDBitRateEnable based on Enable"""
    defaultBinValue = "1"


_TsPIDBitRateEnable_Object = MibTableColumn
tsPIDBitRateEnable = _TsPIDBitRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 5),
    _TsPIDBitRateEnable_Type()
)
tsPIDBitRateEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPIDBitRateEnable.setStatus("current")
_TsPIDBitRateCounter_Type = Counter32
_TsPIDBitRateCounter_Object = MibTableColumn
tsPIDBitRateCounter = _TsPIDBitRateCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 6),
    _TsPIDBitRateCounter_Type()
)
tsPIDBitRateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateCounter.setStatus("current")
_TsPIDBitRateCounterDiscontinuity_Type = DateAndTime
_TsPIDBitRateCounterDiscontinuity_Object = MibTableColumn
tsPIDBitRateCounterDiscontinuity = _TsPIDBitRateCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 7),
    _TsPIDBitRateCounterDiscontinuity_Type()
)
tsPIDBitRateCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateCounterDiscontinuity.setStatus("current")


class _TsPIDBitRateCounterReset_Type(TruthValue):
    """Custom type tsPIDBitRateCounterReset based on TruthValue"""


_TsPIDBitRateCounterReset_Object = MibTableColumn
tsPIDBitRateCounterReset = _TsPIDBitRateCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 8),
    _TsPIDBitRateCounterReset_Type()
)
tsPIDBitRateCounterReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsPIDBitRateCounterReset.setStatus("current")
_TsPIDBitRateLatestError_Type = DateAndTime
_TsPIDBitRateLatestError_Object = MibTableColumn
tsPIDBitRateLatestError = _TsPIDBitRateLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 9),
    _TsPIDBitRateLatestError_Type()
)
tsPIDBitRateLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateLatestError.setStatus("current")
_TsPIDBitRateActiveTime_Type = ActiveTime
_TsPIDBitRateActiveTime_Object = MibTableColumn
tsPIDBitRateActiveTime = _TsPIDBitRateActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 10),
    _TsPIDBitRateActiveTime_Type()
)
tsPIDBitRateActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsPIDBitRateActiveTime.setUnits("second")
_TsPIDBitRateMeasurementState_Type = MeasurementState
_TsPIDBitRateMeasurementState_Object = MibTableColumn
tsPIDBitRateMeasurementState = _TsPIDBitRateMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 11),
    _TsPIDBitRateMeasurementState_Type()
)
tsPIDBitRateMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateMeasurementState.setStatus("current")
_TsPIDBitRateValue_Type = FloatingPoint
_TsPIDBitRateValue_Object = MibTableColumn
tsPIDBitRateValue = _TsPIDBitRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 12),
    _TsPIDBitRateValue_Type()
)
tsPIDBitRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateValue.setStatus("current")
if mibBuilder.loadTexts:
    tsPIDBitRateValue.setUnits("bit/s")
_TsPIDBitRateNomenclature_Type = DisplayString
_TsPIDBitRateNomenclature_Object = MibTableColumn
tsPIDBitRateNomenclature = _TsPIDBitRateNomenclature_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 2, 3, 1, 13),
    _TsPIDBitRateNomenclature_Type()
)
tsPIDBitRateNomenclature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPIDBitRateNomenclature.setStatus("current")
_TsConsistencyTable_Object = MibTable
tsConsistencyTable = _TsConsistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    tsConsistencyTable.setStatus("current")
_TsConsistencyEntry_Object = MibTableRow
tsConsistencyEntry = _TsConsistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1)
)
tsConsistencyEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsConsistencyInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsConsistencyTestNumber"),
)
if mibBuilder.loadTexts:
    tsConsistencyEntry.setStatus("current")
_TsConsistencyInputNumber_Type = InputNumber
_TsConsistencyInputNumber_Object = MibTableColumn
tsConsistencyInputNumber = _TsConsistencyInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 1),
    _TsConsistencyInputNumber_Type()
)
tsConsistencyInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsConsistencyInputNumber.setStatus("current")
_TsConsistencyTestNumber_Type = IndexConsistencyTest
_TsConsistencyTestNumber_Object = MibTableColumn
tsConsistencyTestNumber = _TsConsistencyTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 2),
    _TsConsistencyTestNumber_Type()
)
tsConsistencyTestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsConsistencyTestNumber.setStatus("current")
_TsConsistencyState_Type = TestState
_TsConsistencyState_Object = MibTableColumn
tsConsistencyState = _TsConsistencyState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 3),
    _TsConsistencyState_Type()
)
tsConsistencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsConsistencyState.setStatus("current")


class _TsConsistencyEnable_Type(Enable):
    """Custom type tsConsistencyEnable based on Enable"""
    defaultBinValue = "1"


_TsConsistencyEnable_Object = MibTableColumn
tsConsistencyEnable = _TsConsistencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 4),
    _TsConsistencyEnable_Type()
)
tsConsistencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsConsistencyEnable.setStatus("current")
_TsConsistencyCounter_Type = Counter32
_TsConsistencyCounter_Object = MibTableColumn
tsConsistencyCounter = _TsConsistencyCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 5),
    _TsConsistencyCounter_Type()
)
tsConsistencyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsConsistencyCounter.setStatus("current")
_TsConsistencyCounterDiscontinuity_Type = DateAndTime
_TsConsistencyCounterDiscontinuity_Object = MibTableColumn
tsConsistencyCounterDiscontinuity = _TsConsistencyCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 6),
    _TsConsistencyCounterDiscontinuity_Type()
)
tsConsistencyCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsConsistencyCounterDiscontinuity.setStatus("current")
_TsConsistencyCounterReset_Type = TruthValue
_TsConsistencyCounterReset_Object = MibTableColumn
tsConsistencyCounterReset = _TsConsistencyCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 7),
    _TsConsistencyCounterReset_Type()
)
tsConsistencyCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsConsistencyCounterReset.setStatus("current")
_TsConsistencyLatestError_Type = DateAndTime
_TsConsistencyLatestError_Object = MibTableColumn
tsConsistencyLatestError = _TsConsistencyLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 8),
    _TsConsistencyLatestError_Type()
)
tsConsistencyLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsConsistencyLatestError.setStatus("current")
_TsConsistencyActiveTime_Type = ActiveTime
_TsConsistencyActiveTime_Object = MibTableColumn
tsConsistencyActiveTime = _TsConsistencyActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 3, 1, 9),
    _TsConsistencyActiveTime_Type()
)
tsConsistencyActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsConsistencyActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsConsistencyActiveTime.setUnits("second")
_TsMeasurePreferences_ObjectIdentity = ObjectIdentity
tsMeasurePreferences = _TsMeasurePreferences_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100)
)
_TsMeasurePreferencesTable_Object = MibTable
tsMeasurePreferencesTable = _TsMeasurePreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1)
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesTable.setStatus("current")
_TsMeasurePreferencesEntry_Object = MibTableRow
tsMeasurePreferencesEntry = _TsMeasurePreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1)
)
tsMeasurePreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsMeasurePrefInputNumber"),
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesEntry.setStatus("current")
_TsMeasurePrefInputNumber_Type = InputNumber
_TsMeasurePrefInputNumber_Object = MibTableColumn
tsMeasurePrefInputNumber = _TsMeasurePrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 1),
    _TsMeasurePrefInputNumber_Type()
)
tsMeasurePrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsMeasurePrefInputNumber.setStatus("current")


class _TsMeasurePrefPCRDemarcationFrequency_Type(FloatingPoint):
    """Custom type tsMeasurePrefPCRDemarcationFrequency based on FloatingPoint"""
    defaultValue = OctetString("0.01")


_TsMeasurePrefPCRDemarcationFrequency_Object = MibTableColumn
tsMeasurePrefPCRDemarcationFrequency = _TsMeasurePrefPCRDemarcationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 2),
    _TsMeasurePrefPCRDemarcationFrequency_Type()
)
tsMeasurePrefPCRDemarcationFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefPCRDemarcationFrequency.setStatus("current")


class _TsMeasurePrefPCRFOMax_Type(FloatingPoint):
    """Custom type tsMeasurePrefPCRFOMax based on FloatingPoint"""
    defaultValue = OctetString("810")


_TsMeasurePrefPCRFOMax_Object = MibTableColumn
tsMeasurePrefPCRFOMax = _TsMeasurePrefPCRFOMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 3),
    _TsMeasurePrefPCRFOMax_Type()
)
tsMeasurePrefPCRFOMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefPCRFOMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPCRFOMax.setUnits("Hz")


class _TsMeasurePrefPCRDRMax_Type(FloatingPoint):
    """Custom type tsMeasurePrefPCRDRMax based on FloatingPoint"""
    defaultValue = OctetString("0.075")


_TsMeasurePrefPCRDRMax_Object = MibTableColumn
tsMeasurePrefPCRDRMax = _TsMeasurePrefPCRDRMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 4),
    _TsMeasurePrefPCRDRMax_Type()
)
tsMeasurePrefPCRDRMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefPCRDRMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPCRDRMax.setUnits("Hz/s")


class _TsMeasurePrefPCROJMax_Type(FloatingPoint):
    """Custom type tsMeasurePrefPCROJMax based on FloatingPoint"""
    defaultValue = OctetString("25E-06")


_TsMeasurePrefPCROJMax_Object = MibTableColumn
tsMeasurePrefPCROJMax = _TsMeasurePrefPCROJMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 5),
    _TsMeasurePrefPCROJMax_Type()
)
tsMeasurePrefPCROJMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefPCROJMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPCROJMax.setUnits("second")


class _TsMeasurePrefTSBitRateTau_Type(FloatingPoint):
    """Custom type tsMeasurePrefTSBitRateTau based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsMeasurePrefTSBitRateTau_Object = MibTableColumn
tsMeasurePrefTSBitRateTau = _TsMeasurePrefTSBitRateTau_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 6),
    _TsMeasurePrefTSBitRateTau_Type()
)
tsMeasurePrefTSBitRateTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateTau.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateTau.setUnits("second")


class _TsMeasurePrefTSBitRateN_Type(Unsigned32):
    """Custom type tsMeasurePrefTSBitRateN based on Unsigned32"""
    defaultValue = 10


_TsMeasurePrefTSBitRateN_Object = MibTableColumn
tsMeasurePrefTSBitRateN = _TsMeasurePrefTSBitRateN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 7),
    _TsMeasurePrefTSBitRateN_Type()
)
tsMeasurePrefTSBitRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateN.setStatus("current")


class _TsMeasurePrefTSBitRateElement_Type(BitRateElement):
    """Custom type tsMeasurePrefTSBitRateElement based on BitRateElement"""


_TsMeasurePrefTSBitRateElement_Object = MibTableColumn
tsMeasurePrefTSBitRateElement = _TsMeasurePrefTSBitRateElement_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 8),
    _TsMeasurePrefTSBitRateElement_Type()
)
tsMeasurePrefTSBitRateElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateElement.setStatus("current")
_TsMeasurePrefTSBitRateMin_Type = FloatingPoint
_TsMeasurePrefTSBitRateMin_Object = MibTableColumn
tsMeasurePrefTSBitRateMin = _TsMeasurePrefTSBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 9),
    _TsMeasurePrefTSBitRateMin_Type()
)
tsMeasurePrefTSBitRateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateMin.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateMin.setUnits("bit/s")
_TsMeasurePrefTSBitRateMax_Type = FloatingPoint
_TsMeasurePrefTSBitRateMax_Object = MibTableColumn
tsMeasurePrefTSBitRateMax = _TsMeasurePrefTSBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 10),
    _TsMeasurePrefTSBitRateMax_Type()
)
tsMeasurePrefTSBitRateMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefTSBitRateMax.setUnits("bit/s")


class _TsMeasurePrefAllServiceBitRateTau_Type(FloatingPoint):
    """Custom type tsMeasurePrefAllServiceBitRateTau based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsMeasurePrefAllServiceBitRateTau_Object = MibTableColumn
tsMeasurePrefAllServiceBitRateTau = _TsMeasurePrefAllServiceBitRateTau_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 11),
    _TsMeasurePrefAllServiceBitRateTau_Type()
)
tsMeasurePrefAllServiceBitRateTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllServiceBitRateTau.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefAllServiceBitRateTau.setUnits("second")


class _TsMeasurePrefAllServiceBitRateN_Type(Unsigned32):
    """Custom type tsMeasurePrefAllServiceBitRateN based on Unsigned32"""
    defaultValue = 10


_TsMeasurePrefAllServiceBitRateN_Object = MibTableColumn
tsMeasurePrefAllServiceBitRateN = _TsMeasurePrefAllServiceBitRateN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 12),
    _TsMeasurePrefAllServiceBitRateN_Type()
)
tsMeasurePrefAllServiceBitRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllServiceBitRateN.setStatus("current")


class _TsMeasurePrefAllServiceBitRateElement_Type(BitRateElement):
    """Custom type tsMeasurePrefAllServiceBitRateElement based on BitRateElement"""


_TsMeasurePrefAllServiceBitRateElement_Object = MibTableColumn
tsMeasurePrefAllServiceBitRateElement = _TsMeasurePrefAllServiceBitRateElement_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 13),
    _TsMeasurePrefAllServiceBitRateElement_Type()
)
tsMeasurePrefAllServiceBitRateElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllServiceBitRateElement.setStatus("current")


class _TsMeasurePrefAllPIDBitRateTau_Type(FloatingPoint):
    """Custom type tsMeasurePrefAllPIDBitRateTau based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsMeasurePrefAllPIDBitRateTau_Object = MibTableColumn
tsMeasurePrefAllPIDBitRateTau = _TsMeasurePrefAllPIDBitRateTau_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 14),
    _TsMeasurePrefAllPIDBitRateTau_Type()
)
tsMeasurePrefAllPIDBitRateTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllPIDBitRateTau.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefAllPIDBitRateTau.setUnits("second")


class _TsMeasurePrefAllPIDBitRateN_Type(Unsigned32):
    """Custom type tsMeasurePrefAllPIDBitRateN based on Unsigned32"""
    defaultValue = 10


_TsMeasurePrefAllPIDBitRateN_Object = MibTableColumn
tsMeasurePrefAllPIDBitRateN = _TsMeasurePrefAllPIDBitRateN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 15),
    _TsMeasurePrefAllPIDBitRateN_Type()
)
tsMeasurePrefAllPIDBitRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllPIDBitRateN.setStatus("current")


class _TsMeasurePrefAllPIDBitRateElement_Type(BitRateElement):
    """Custom type tsMeasurePrefAllPIDBitRateElement based on BitRateElement"""


_TsMeasurePrefAllPIDBitRateElement_Object = MibTableColumn
tsMeasurePrefAllPIDBitRateElement = _TsMeasurePrefAllPIDBitRateElement_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 16),
    _TsMeasurePrefAllPIDBitRateElement_Type()
)
tsMeasurePrefAllPIDBitRateElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefAllPIDBitRateElement.setStatus("current")
_TsMeasurePrefExpectedTSID_Type = TransportStreamID
_TsMeasurePrefExpectedTSID_Object = MibTableColumn
tsMeasurePrefExpectedTSID = _TsMeasurePrefExpectedTSID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 1, 1, 17),
    _TsMeasurePrefExpectedTSID_Type()
)
tsMeasurePrefExpectedTSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMeasurePrefExpectedTSID.setStatus("current")
_TsMeasurePreferencesServiceTable_Object = MibTable
tsMeasurePreferencesServiceTable = _TsMeasurePreferencesServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2)
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesServiceTable.setStatus("current")
_TsMeasurePreferencesServiceEntry_Object = MibTableRow
tsMeasurePreferencesServiceEntry = _TsMeasurePreferencesServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1)
)
tsMeasurePreferencesServiceEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsMeasurePrefServiceInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsMeasurePrefServiceService"),
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesServiceEntry.setStatus("current")
_TsMeasurePrefServiceInputNumber_Type = InputNumber
_TsMeasurePrefServiceInputNumber_Object = MibTableColumn
tsMeasurePrefServiceInputNumber = _TsMeasurePrefServiceInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 1),
    _TsMeasurePrefServiceInputNumber_Type()
)
tsMeasurePrefServiceInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceInputNumber.setStatus("current")
_TsMeasurePrefServiceService_Type = ServiceId
_TsMeasurePrefServiceService_Object = MibTableColumn
tsMeasurePrefServiceService = _TsMeasurePrefServiceService_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 2),
    _TsMeasurePrefServiceService_Type()
)
tsMeasurePrefServiceService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceService.setStatus("current")


class _TsMeasurePrefServiceRowStatus_Type(RowStatus):
    """Custom type tsMeasurePrefServiceRowStatus based on RowStatus"""


_TsMeasurePrefServiceRowStatus_Object = MibTableColumn
tsMeasurePrefServiceRowStatus = _TsMeasurePrefServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 3),
    _TsMeasurePrefServiceRowStatus_Type()
)
tsMeasurePrefServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceRowStatus.setStatus("current")


class _TsMeasurePrefServiceBitRateTau_Type(FloatingPoint):
    """Custom type tsMeasurePrefServiceBitRateTau based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsMeasurePrefServiceBitRateTau_Object = MibTableColumn
tsMeasurePrefServiceBitRateTau = _TsMeasurePrefServiceBitRateTau_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 4),
    _TsMeasurePrefServiceBitRateTau_Type()
)
tsMeasurePrefServiceBitRateTau.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateTau.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateTau.setUnits("second")


class _TsMeasurePrefServiceBitRateN_Type(Unsigned32):
    """Custom type tsMeasurePrefServiceBitRateN based on Unsigned32"""
    defaultValue = 10


_TsMeasurePrefServiceBitRateN_Object = MibTableColumn
tsMeasurePrefServiceBitRateN = _TsMeasurePrefServiceBitRateN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 5),
    _TsMeasurePrefServiceBitRateN_Type()
)
tsMeasurePrefServiceBitRateN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateN.setStatus("current")


class _TsMeasurePrefServiceBitRateElement_Type(BitRateElement):
    """Custom type tsMeasurePrefServiceBitRateElement based on BitRateElement"""


_TsMeasurePrefServiceBitRateElement_Object = MibTableColumn
tsMeasurePrefServiceBitRateElement = _TsMeasurePrefServiceBitRateElement_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 6),
    _TsMeasurePrefServiceBitRateElement_Type()
)
tsMeasurePrefServiceBitRateElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateElement.setStatus("current")
_TsMeasurePrefServiceBitRateMin_Type = FloatingPoint
_TsMeasurePrefServiceBitRateMin_Object = MibTableColumn
tsMeasurePrefServiceBitRateMin = _TsMeasurePrefServiceBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 7),
    _TsMeasurePrefServiceBitRateMin_Type()
)
tsMeasurePrefServiceBitRateMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateMin.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateMin.setUnits("bit/s")
_TsMeasurePrefServiceBitRateMax_Type = FloatingPoint
_TsMeasurePrefServiceBitRateMax_Object = MibTableColumn
tsMeasurePrefServiceBitRateMax = _TsMeasurePrefServiceBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 2, 1, 8),
    _TsMeasurePrefServiceBitRateMax_Type()
)
tsMeasurePrefServiceBitRateMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefServiceBitRateMax.setUnits("bit/s")
_TsMeasurePreferencesPIDTable_Object = MibTable
tsMeasurePreferencesPIDTable = _TsMeasurePreferencesPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3)
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesPIDTable.setStatus("current")
_TsMeasurePreferencesPIDEntry_Object = MibTableRow
tsMeasurePreferencesPIDEntry = _TsMeasurePreferencesPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1)
)
tsMeasurePreferencesPIDEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsMeasurePrefPIDInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsMeasurePrefPIDPID"),
)
if mibBuilder.loadTexts:
    tsMeasurePreferencesPIDEntry.setStatus("current")
_TsMeasurePrefPIDInputNumber_Type = InputNumber
_TsMeasurePrefPIDInputNumber_Object = MibTableColumn
tsMeasurePrefPIDInputNumber = _TsMeasurePrefPIDInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 1),
    _TsMeasurePrefPIDInputNumber_Type()
)
tsMeasurePrefPIDInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDInputNumber.setStatus("current")
_TsMeasurePrefPIDPID_Type = PIDPlusOne
_TsMeasurePrefPIDPID_Object = MibTableColumn
tsMeasurePrefPIDPID = _TsMeasurePrefPIDPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 2),
    _TsMeasurePrefPIDPID_Type()
)
tsMeasurePrefPIDPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDPID.setStatus("current")


class _TsMeasurePrefPIDRowStatus_Type(RowStatus):
    """Custom type tsMeasurePrefPIDRowStatus based on RowStatus"""


_TsMeasurePrefPIDRowStatus_Object = MibTableColumn
tsMeasurePrefPIDRowStatus = _TsMeasurePrefPIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 3),
    _TsMeasurePrefPIDRowStatus_Type()
)
tsMeasurePrefPIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDRowStatus.setStatus("current")


class _TsMeasurePrefPIDBitRateTau_Type(FloatingPoint):
    """Custom type tsMeasurePrefPIDBitRateTau based on FloatingPoint"""
    defaultValue = OctetString("0.1")


_TsMeasurePrefPIDBitRateTau_Object = MibTableColumn
tsMeasurePrefPIDBitRateTau = _TsMeasurePrefPIDBitRateTau_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 4),
    _TsMeasurePrefPIDBitRateTau_Type()
)
tsMeasurePrefPIDBitRateTau.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateTau.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateTau.setUnits("second")


class _TsMeasurePrefPIDBitRateN_Type(Unsigned32):
    """Custom type tsMeasurePrefPIDBitRateN based on Unsigned32"""
    defaultValue = 10


_TsMeasurePrefPIDBitRateN_Object = MibTableColumn
tsMeasurePrefPIDBitRateN = _TsMeasurePrefPIDBitRateN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 5),
    _TsMeasurePrefPIDBitRateN_Type()
)
tsMeasurePrefPIDBitRateN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateN.setStatus("current")


class _TsMeasurePrefPIDBitRateElement_Type(BitRateElement):
    """Custom type tsMeasurePrefPIDBitRateElement based on BitRateElement"""


_TsMeasurePrefPIDBitRateElement_Object = MibTableColumn
tsMeasurePrefPIDBitRateElement = _TsMeasurePrefPIDBitRateElement_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 6),
    _TsMeasurePrefPIDBitRateElement_Type()
)
tsMeasurePrefPIDBitRateElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateElement.setStatus("current")
_TsMeasurePrefPIDBitRateMin_Type = FloatingPoint
_TsMeasurePrefPIDBitRateMin_Object = MibTableColumn
tsMeasurePrefPIDBitRateMin = _TsMeasurePrefPIDBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 7),
    _TsMeasurePrefPIDBitRateMin_Type()
)
tsMeasurePrefPIDBitRateMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateMin.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateMin.setUnits("bit/s")
_TsMeasurePrefPIDBitRateMax_Type = FloatingPoint
_TsMeasurePrefPIDBitRateMax_Object = MibTableColumn
tsMeasurePrefPIDBitRateMax = _TsMeasurePrefPIDBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 4, 100, 3, 1, 8),
    _TsMeasurePrefPIDBitRateMax_Type()
)
tsMeasurePrefPIDBitRateMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateMax.setStatus("current")
if mibBuilder.loadTexts:
    tsMeasurePrefPIDBitRateMax.setUnits("bit/s")
_TsServicePerformance_ObjectIdentity = ObjectIdentity
tsServicePerformance = _TsServicePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5)
)
_TsServicePerformanceTable_Object = MibTable
tsServicePerformanceTable = _TsServicePerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    tsServicePerformanceTable.setStatus("current")
_TsServicePerformanceEntry_Object = MibTableRow
tsServicePerformanceEntry = _TsServicePerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1)
)
tsServicePerformanceEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsServicePerformanceNumber"),
    (0, "DVB-MGTR101290-MIB", "tsServicePerformanceInputNumber"),
)
if mibBuilder.loadTexts:
    tsServicePerformanceEntry.setStatus("current")
_TsServicePerformanceInputNumber_Type = InputNumber
_TsServicePerformanceInputNumber_Object = MibTableColumn
tsServicePerformanceInputNumber = _TsServicePerformanceInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 1),
    _TsServicePerformanceInputNumber_Type()
)
tsServicePerformanceInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsServicePerformanceInputNumber.setStatus("current")
_TsServicePerformanceNumber_Type = IndexServicePerformance
_TsServicePerformanceNumber_Object = MibTableColumn
tsServicePerformanceNumber = _TsServicePerformanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 2),
    _TsServicePerformanceNumber_Type()
)
tsServicePerformanceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsServicePerformanceNumber.setStatus("current")
_TsServicePerformanceState_Type = TestState
_TsServicePerformanceState_Object = MibTableColumn
tsServicePerformanceState = _TsServicePerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 3),
    _TsServicePerformanceState_Type()
)
tsServicePerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceState.setStatus("current")


class _TsServicePerformanceEnable_Type(Enable):
    """Custom type tsServicePerformanceEnable based on Enable"""
    defaultBinValue = "1"


_TsServicePerformanceEnable_Object = MibTableColumn
tsServicePerformanceEnable = _TsServicePerformanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 4),
    _TsServicePerformanceEnable_Type()
)
tsServicePerformanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsServicePerformanceEnable.setStatus("current")
_TsServicePerformanceCounter_Type = Counter32
_TsServicePerformanceCounter_Object = MibTableColumn
tsServicePerformanceCounter = _TsServicePerformanceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 5),
    _TsServicePerformanceCounter_Type()
)
tsServicePerformanceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceCounter.setStatus("current")
_TsServicePerformanceCounterDiscontinuity_Type = DateAndTime
_TsServicePerformanceCounterDiscontinuity_Object = MibTableColumn
tsServicePerformanceCounterDiscontinuity = _TsServicePerformanceCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 6),
    _TsServicePerformanceCounterDiscontinuity_Type()
)
tsServicePerformanceCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceCounterDiscontinuity.setStatus("current")


class _TsServicePerformanceCounterReset_Type(TruthValue):
    """Custom type tsServicePerformanceCounterReset based on TruthValue"""


_TsServicePerformanceCounterReset_Object = MibTableColumn
tsServicePerformanceCounterReset = _TsServicePerformanceCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 7),
    _TsServicePerformanceCounterReset_Type()
)
tsServicePerformanceCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsServicePerformanceCounterReset.setStatus("current")
_TsServicePerformanceLatestError_Type = DateAndTime
_TsServicePerformanceLatestError_Object = MibTableColumn
tsServicePerformanceLatestError = _TsServicePerformanceLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 8),
    _TsServicePerformanceLatestError_Type()
)
tsServicePerformanceLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceLatestError.setStatus("current")
_TsServicePerformanceActiveTime_Type = ActiveTime
_TsServicePerformanceActiveTime_Object = MibTableColumn
tsServicePerformanceActiveTime = _TsServicePerformanceActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 9),
    _TsServicePerformanceActiveTime_Type()
)
tsServicePerformanceActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    tsServicePerformanceActiveTime.setUnits("second")
_TsServicePerformanceMeasurementState_Type = MeasurementState
_TsServicePerformanceMeasurementState_Object = MibTableColumn
tsServicePerformanceMeasurementState = _TsServicePerformanceMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 10),
    _TsServicePerformanceMeasurementState_Type()
)
tsServicePerformanceMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceMeasurementState.setStatus("current")
_TsServicePerformanceError_Type = Unsigned32
_TsServicePerformanceError_Object = MibTableColumn
tsServicePerformanceError = _TsServicePerformanceError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 11),
    _TsServicePerformanceError_Type()
)
tsServicePerformanceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceError.setStatus("current")
_TsServicePerformanceErrorRatio_Type = FloatingPoint
_TsServicePerformanceErrorRatio_Object = MibTableColumn
tsServicePerformanceErrorRatio = _TsServicePerformanceErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 2, 1, 12),
    _TsServicePerformanceErrorRatio_Type()
)
tsServicePerformanceErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServicePerformanceErrorRatio.setStatus("current")
_TsServicePerformancePreferencesTable_Object = MibTable
tsServicePerformancePreferencesTable = _TsServicePerformancePreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100)
)
if mibBuilder.loadTexts:
    tsServicePerformancePreferencesTable.setStatus("current")
_TsServicePerformancePreferencesEntry_Object = MibTableRow
tsServicePerformancePreferencesEntry = _TsServicePerformancePreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1)
)
tsServicePerformancePreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "tsSPPrefInputNumber"),
    (0, "DVB-MGTR101290-MIB", "tsSPPrefNumber"),
)
if mibBuilder.loadTexts:
    tsServicePerformancePreferencesEntry.setStatus("current")
_TsSPPrefInputNumber_Type = InputNumber
_TsSPPrefInputNumber_Object = MibTableColumn
tsSPPrefInputNumber = _TsSPPrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1, 1),
    _TsSPPrefInputNumber_Type()
)
tsSPPrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsSPPrefInputNumber.setStatus("current")
_TsSPPrefNumber_Type = IndexServicePerformance
_TsSPPrefNumber_Object = MibTableColumn
tsSPPrefNumber = _TsSPPrefNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1, 2),
    _TsSPPrefNumber_Type()
)
tsSPPrefNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsSPPrefNumber.setStatus("current")
_TsSPPrefDeltaT_Type = FloatingPoint
_TsSPPrefDeltaT_Object = MibTableColumn
tsSPPrefDeltaT = _TsSPPrefDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1, 3),
    _TsSPPrefDeltaT_Type()
)
tsSPPrefDeltaT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsSPPrefDeltaT.setStatus("current")
if mibBuilder.loadTexts:
    tsSPPrefDeltaT.setUnits("second")
_TsSPPrefEvaluationTime_Type = FloatingPoint
_TsSPPrefEvaluationTime_Object = MibTableColumn
tsSPPrefEvaluationTime = _TsSPPrefEvaluationTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1, 4),
    _TsSPPrefEvaluationTime_Type()
)
tsSPPrefEvaluationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsSPPrefEvaluationTime.setStatus("current")
if mibBuilder.loadTexts:
    tsSPPrefEvaluationTime.setUnits("second")
_TsSPPrefThreshold_Type = FloatingPoint
_TsSPPrefThreshold_Object = MibTableColumn
tsSPPrefThreshold = _TsSPPrefThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 5, 5, 100, 1, 5),
    _TsSPPrefThreshold_Type()
)
tsSPPrefThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsSPPrefThreshold.setStatus("current")
_Tr101290CableSat_ObjectIdentity = ObjectIdentity
tr101290CableSat = _Tr101290CableSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6)
)
_SysAvailabilityTable_Object = MibTable
sysAvailabilityTable = _SysAvailabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sysAvailabilityTable.setStatus("current")
_SysAvailabilityEntry_Object = MibTableRow
sysAvailabilityEntry = _SysAvailabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1)
)
sysAvailabilityEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "sysAvailabilityInputNumber"),
)
if mibBuilder.loadTexts:
    sysAvailabilityEntry.setStatus("current")
_SysAvailabilityInputNumber_Type = InputNumber
_SysAvailabilityInputNumber_Object = MibTableColumn
sysAvailabilityInputNumber = _SysAvailabilityInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 1),
    _SysAvailabilityInputNumber_Type()
)
sysAvailabilityInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysAvailabilityInputNumber.setStatus("current")
_SysAvailabilityTestState_Type = TestState
_SysAvailabilityTestState_Object = MibTableColumn
sysAvailabilityTestState = _SysAvailabilityTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 2),
    _SysAvailabilityTestState_Type()
)
sysAvailabilityTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityTestState.setStatus("current")


class _SysAvailabilityEnable_Type(Enable):
    """Custom type sysAvailabilityEnable based on Enable"""
    defaultBinValue = "1"


_SysAvailabilityEnable_Object = MibTableColumn
sysAvailabilityEnable = _SysAvailabilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 3),
    _SysAvailabilityEnable_Type()
)
sysAvailabilityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAvailabilityEnable.setStatus("current")
_SysAvailabilityCounter_Type = Counter32
_SysAvailabilityCounter_Object = MibTableColumn
sysAvailabilityCounter = _SysAvailabilityCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 4),
    _SysAvailabilityCounter_Type()
)
sysAvailabilityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityCounter.setStatus("current")
_SysAvailabilityCounterDiscontinuity_Type = DateAndTime
_SysAvailabilityCounterDiscontinuity_Object = MibTableColumn
sysAvailabilityCounterDiscontinuity = _SysAvailabilityCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 5),
    _SysAvailabilityCounterDiscontinuity_Type()
)
sysAvailabilityCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityCounterDiscontinuity.setStatus("current")
_SysAvailabilityCounterReset_Type = TruthValue
_SysAvailabilityCounterReset_Object = MibTableColumn
sysAvailabilityCounterReset = _SysAvailabilityCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 6),
    _SysAvailabilityCounterReset_Type()
)
sysAvailabilityCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAvailabilityCounterReset.setStatus("current")
_SysAvailabilityLatestError_Type = DateAndTime
_SysAvailabilityLatestError_Object = MibTableColumn
sysAvailabilityLatestError = _SysAvailabilityLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 7),
    _SysAvailabilityLatestError_Type()
)
sysAvailabilityLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityLatestError.setStatus("current")
_SysAvailabilityActiveTime_Type = ActiveTime
_SysAvailabilityActiveTime_Object = MibTableColumn
sysAvailabilityActiveTime = _SysAvailabilityActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 8),
    _SysAvailabilityActiveTime_Type()
)
sysAvailabilityActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    sysAvailabilityActiveTime.setUnits("second")
_SysAvailabilityMeasurementState_Type = MeasurementState
_SysAvailabilityMeasurementState_Object = MibTableColumn
sysAvailabilityMeasurementState = _SysAvailabilityMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 9),
    _SysAvailabilityMeasurementState_Type()
)
sysAvailabilityMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityMeasurementState.setStatus("current")
_SysAvailabilityUnavailableTime_Type = Unsigned32
_SysAvailabilityUnavailableTime_Object = MibTableColumn
sysAvailabilityUnavailableTime = _SysAvailabilityUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 10),
    _SysAvailabilityUnavailableTime_Type()
)
sysAvailabilityUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityUnavailableTime.setStatus("current")
if mibBuilder.loadTexts:
    sysAvailabilityUnavailableTime.setUnits("second")
_SysAvailabilityRatio_Type = FloatingPoint
_SysAvailabilityRatio_Object = MibTableColumn
sysAvailabilityRatio = _SysAvailabilityRatio_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 11),
    _SysAvailabilityRatio_Type()
)
sysAvailabilityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityRatio.setStatus("current")
_SysAvailabilityInSETI_Type = TruthValue
_SysAvailabilityInSETI_Object = MibTableColumn
sysAvailabilityInSETI = _SysAvailabilityInSETI_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 1, 1, 12),
    _SysAvailabilityInSETI_Type()
)
sysAvailabilityInSETI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAvailabilityInSETI.setStatus("current")
_LinkAvailabilityTable_Object = MibTable
linkAvailabilityTable = _LinkAvailabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    linkAvailabilityTable.setStatus("current")
_LinkAvailabilityEntry_Object = MibTableRow
linkAvailabilityEntry = _LinkAvailabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1)
)
linkAvailabilityEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "linkAvailabilityInputNumber"),
)
if mibBuilder.loadTexts:
    linkAvailabilityEntry.setStatus("current")
_LinkAvailabilityInputNumber_Type = InputNumber
_LinkAvailabilityInputNumber_Object = MibTableColumn
linkAvailabilityInputNumber = _LinkAvailabilityInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 1),
    _LinkAvailabilityInputNumber_Type()
)
linkAvailabilityInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkAvailabilityInputNumber.setStatus("current")
_LinkAvailabilityTestState_Type = TestState
_LinkAvailabilityTestState_Object = MibTableColumn
linkAvailabilityTestState = _LinkAvailabilityTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 2),
    _LinkAvailabilityTestState_Type()
)
linkAvailabilityTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityTestState.setStatus("current")


class _LinkAvailabilityEnable_Type(Enable):
    """Custom type linkAvailabilityEnable based on Enable"""
    defaultBinValue = "1"


_LinkAvailabilityEnable_Object = MibTableColumn
linkAvailabilityEnable = _LinkAvailabilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 3),
    _LinkAvailabilityEnable_Type()
)
linkAvailabilityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkAvailabilityEnable.setStatus("current")
_LinkAvailabilityCounter_Type = Counter32
_LinkAvailabilityCounter_Object = MibTableColumn
linkAvailabilityCounter = _LinkAvailabilityCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 4),
    _LinkAvailabilityCounter_Type()
)
linkAvailabilityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityCounter.setStatus("current")
_LinkAvailabilityCounterDiscontinuity_Type = DateAndTime
_LinkAvailabilityCounterDiscontinuity_Object = MibTableColumn
linkAvailabilityCounterDiscontinuity = _LinkAvailabilityCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 5),
    _LinkAvailabilityCounterDiscontinuity_Type()
)
linkAvailabilityCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityCounterDiscontinuity.setStatus("current")


class _LinkAvailabilityCounterReset_Type(TruthValue):
    """Custom type linkAvailabilityCounterReset based on TruthValue"""


_LinkAvailabilityCounterReset_Object = MibTableColumn
linkAvailabilityCounterReset = _LinkAvailabilityCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 6),
    _LinkAvailabilityCounterReset_Type()
)
linkAvailabilityCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkAvailabilityCounterReset.setStatus("current")
_LinkAvailabilityLatestError_Type = DateAndTime
_LinkAvailabilityLatestError_Object = MibTableColumn
linkAvailabilityLatestError = _LinkAvailabilityLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 7),
    _LinkAvailabilityLatestError_Type()
)
linkAvailabilityLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityLatestError.setStatus("current")
_LinkAvailabilityActiveTime_Type = ActiveTime
_LinkAvailabilityActiveTime_Object = MibTableColumn
linkAvailabilityActiveTime = _LinkAvailabilityActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 8),
    _LinkAvailabilityActiveTime_Type()
)
linkAvailabilityActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    linkAvailabilityActiveTime.setUnits("second")
_LinkAvailabilityMeasurementState_Type = MeasurementState
_LinkAvailabilityMeasurementState_Object = MibTableColumn
linkAvailabilityMeasurementState = _LinkAvailabilityMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 9),
    _LinkAvailabilityMeasurementState_Type()
)
linkAvailabilityMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityMeasurementState.setStatus("current")
_LinkAvailabilityUnavailableTime_Type = Unsigned32
_LinkAvailabilityUnavailableTime_Object = MibTableColumn
linkAvailabilityUnavailableTime = _LinkAvailabilityUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 10),
    _LinkAvailabilityUnavailableTime_Type()
)
linkAvailabilityUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityUnavailableTime.setStatus("current")
if mibBuilder.loadTexts:
    linkAvailabilityUnavailableTime.setUnits("second")
_LinkAvailabilityRatio_Type = FloatingPoint
_LinkAvailabilityRatio_Object = MibTableColumn
linkAvailabilityRatio = _LinkAvailabilityRatio_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 11),
    _LinkAvailabilityRatio_Type()
)
linkAvailabilityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityRatio.setStatus("current")
_LinkAvailabilityInSUTI_Type = TruthValue
_LinkAvailabilityInSUTI_Object = MibTableColumn
linkAvailabilityInSUTI = _LinkAvailabilityInSUTI_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 2, 1, 12),
    _LinkAvailabilityInSUTI_Type()
)
linkAvailabilityInSUTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailabilityInSUTI.setStatus("current")
_BerRSinServiceTable_Object = MibTable
berRSinServiceTable = _BerRSinServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    berRSinServiceTable.setStatus("current")
_BerRSinServiceEntry_Object = MibTableRow
berRSinServiceEntry = _BerRSinServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1)
)
berRSinServiceEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berRSinServiceInputNumber"),
)
if mibBuilder.loadTexts:
    berRSinServiceEntry.setStatus("current")
_BerRSinServiceInputNumber_Type = InputNumber
_BerRSinServiceInputNumber_Object = MibTableColumn
berRSinServiceInputNumber = _BerRSinServiceInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 1),
    _BerRSinServiceInputNumber_Type()
)
berRSinServiceInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berRSinServiceInputNumber.setStatus("current")
_BerRSinServiceTestState_Type = TestState
_BerRSinServiceTestState_Object = MibTableColumn
berRSinServiceTestState = _BerRSinServiceTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 2),
    _BerRSinServiceTestState_Type()
)
berRSinServiceTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceTestState.setStatus("current")


class _BerRSinServiceEnable_Type(Enable):
    """Custom type berRSinServiceEnable based on Enable"""
    defaultBinValue = "1"


_BerRSinServiceEnable_Object = MibTableColumn
berRSinServiceEnable = _BerRSinServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 3),
    _BerRSinServiceEnable_Type()
)
berRSinServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSinServiceEnable.setStatus("current")
_BerRSinServiceCounter_Type = Counter32
_BerRSinServiceCounter_Object = MibTableColumn
berRSinServiceCounter = _BerRSinServiceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 4),
    _BerRSinServiceCounter_Type()
)
berRSinServiceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceCounter.setStatus("current")
_BerRSinServiceCounterDiscontinuity_Type = DateAndTime
_BerRSinServiceCounterDiscontinuity_Object = MibTableColumn
berRSinServiceCounterDiscontinuity = _BerRSinServiceCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 5),
    _BerRSinServiceCounterDiscontinuity_Type()
)
berRSinServiceCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceCounterDiscontinuity.setStatus("current")


class _BerRSinServiceCounterReset_Type(TruthValue):
    """Custom type berRSinServiceCounterReset based on TruthValue"""


_BerRSinServiceCounterReset_Object = MibTableColumn
berRSinServiceCounterReset = _BerRSinServiceCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 6),
    _BerRSinServiceCounterReset_Type()
)
berRSinServiceCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSinServiceCounterReset.setStatus("current")
_BerRSinServiceLatestError_Type = DateAndTime
_BerRSinServiceLatestError_Object = MibTableColumn
berRSinServiceLatestError = _BerRSinServiceLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 7),
    _BerRSinServiceLatestError_Type()
)
berRSinServiceLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceLatestError.setStatus("current")
_BerRSinServiceActiveTime_Type = ActiveTime
_BerRSinServiceActiveTime_Object = MibTableColumn
berRSinServiceActiveTime = _BerRSinServiceActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 8),
    _BerRSinServiceActiveTime_Type()
)
berRSinServiceActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    berRSinServiceActiveTime.setUnits("second")
_BerRSinServiceMeasurementState_Type = MeasurementState
_BerRSinServiceMeasurementState_Object = MibTableColumn
berRSinServiceMeasurementState = _BerRSinServiceMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 9),
    _BerRSinServiceMeasurementState_Type()
)
berRSinServiceMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceMeasurementState.setStatus("current")
_BerRSinServiceValue_Type = FloatingPoint
_BerRSinServiceValue_Object = MibTableColumn
berRSinServiceValue = _BerRSinServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 3, 1, 10),
    _BerRSinServiceValue_Type()
)
berRSinServiceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSinServiceValue.setStatus("current")
_RfIFsignalPowerTable_Object = MibTable
rfIFsignalPowerTable = _RfIFsignalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6)
)
if mibBuilder.loadTexts:
    rfIFsignalPowerTable.setStatus("current")
_RfIFsignalPowerEntry_Object = MibTableRow
rfIFsignalPowerEntry = _RfIFsignalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1)
)
rfIFsignalPowerEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfIFsignalPowerInputNumber"),
)
if mibBuilder.loadTexts:
    rfIFsignalPowerEntry.setStatus("current")
_RfIFsignalPowerInputNumber_Type = InputNumber
_RfIFsignalPowerInputNumber_Object = MibTableColumn
rfIFsignalPowerInputNumber = _RfIFsignalPowerInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 1),
    _RfIFsignalPowerInputNumber_Type()
)
rfIFsignalPowerInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIFsignalPowerInputNumber.setStatus("current")
_RfIFsignalPowerTestState_Type = TestState
_RfIFsignalPowerTestState_Object = MibTableColumn
rfIFsignalPowerTestState = _RfIFsignalPowerTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 2),
    _RfIFsignalPowerTestState_Type()
)
rfIFsignalPowerTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerTestState.setStatus("current")


class _RfIFsignalPowerEnable_Type(Enable):
    """Custom type rfIFsignalPowerEnable based on Enable"""
    defaultBinValue = "1"


_RfIFsignalPowerEnable_Object = MibTableColumn
rfIFsignalPowerEnable = _RfIFsignalPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 3),
    _RfIFsignalPowerEnable_Type()
)
rfIFsignalPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIFsignalPowerEnable.setStatus("current")
_RfIFsignalPowerCounter_Type = Counter32
_RfIFsignalPowerCounter_Object = MibTableColumn
rfIFsignalPowerCounter = _RfIFsignalPowerCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 4),
    _RfIFsignalPowerCounter_Type()
)
rfIFsignalPowerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerCounter.setStatus("current")
_RfIFsignalPowerCounterDiscontinuity_Type = DateAndTime
_RfIFsignalPowerCounterDiscontinuity_Object = MibTableColumn
rfIFsignalPowerCounterDiscontinuity = _RfIFsignalPowerCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 5),
    _RfIFsignalPowerCounterDiscontinuity_Type()
)
rfIFsignalPowerCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerCounterDiscontinuity.setStatus("current")


class _RfIFsignalPowerCounterReset_Type(TruthValue):
    """Custom type rfIFsignalPowerCounterReset based on TruthValue"""


_RfIFsignalPowerCounterReset_Object = MibTableColumn
rfIFsignalPowerCounterReset = _RfIFsignalPowerCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 6),
    _RfIFsignalPowerCounterReset_Type()
)
rfIFsignalPowerCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIFsignalPowerCounterReset.setStatus("current")
_RfIFsignalPowerLatestError_Type = DateAndTime
_RfIFsignalPowerLatestError_Object = MibTableColumn
rfIFsignalPowerLatestError = _RfIFsignalPowerLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 7),
    _RfIFsignalPowerLatestError_Type()
)
rfIFsignalPowerLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerLatestError.setStatus("current")
_RfIFsignalPowerActiveTime_Type = ActiveTime
_RfIFsignalPowerActiveTime_Object = MibTableColumn
rfIFsignalPowerActiveTime = _RfIFsignalPowerActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 8),
    _RfIFsignalPowerActiveTime_Type()
)
rfIFsignalPowerActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rfIFsignalPowerActiveTime.setUnits("second")
_RfIFsignalPowerMeasurementState_Type = MeasurementState
_RfIFsignalPowerMeasurementState_Object = MibTableColumn
rfIFsignalPowerMeasurementState = _RfIFsignalPowerMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 9),
    _RfIFsignalPowerMeasurementState_Type()
)
rfIFsignalPowerMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerMeasurementState.setStatus("current")
_RfIFsignalPowerValue_Type = FloatingPoint
_RfIFsignalPowerValue_Object = MibTableColumn
rfIFsignalPowerValue = _RfIFsignalPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 6, 1, 10),
    _RfIFsignalPowerValue_Type()
)
rfIFsignalPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIFsignalPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    rfIFsignalPowerValue.setUnits("dBm")
_NoisePowerTable_Object = MibTable
noisePowerTable = _NoisePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7)
)
if mibBuilder.loadTexts:
    noisePowerTable.setStatus("current")
_NoisePowerEntry_Object = MibTableRow
noisePowerEntry = _NoisePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1)
)
noisePowerEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "noisePowerInputNumber"),
)
if mibBuilder.loadTexts:
    noisePowerEntry.setStatus("current")
_NoisePowerInputNumber_Type = InputNumber
_NoisePowerInputNumber_Object = MibTableColumn
noisePowerInputNumber = _NoisePowerInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 1),
    _NoisePowerInputNumber_Type()
)
noisePowerInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    noisePowerInputNumber.setStatus("current")
_NoisePowerTestState_Type = TestState
_NoisePowerTestState_Object = MibTableColumn
noisePowerTestState = _NoisePowerTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 2),
    _NoisePowerTestState_Type()
)
noisePowerTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerTestState.setStatus("current")


class _NoisePowerEnable_Type(Enable):
    """Custom type noisePowerEnable based on Enable"""
    defaultBinValue = "1"


_NoisePowerEnable_Object = MibTableColumn
noisePowerEnable = _NoisePowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 3),
    _NoisePowerEnable_Type()
)
noisePowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noisePowerEnable.setStatus("current")
_NoisePowerCounter_Type = Counter32
_NoisePowerCounter_Object = MibTableColumn
noisePowerCounter = _NoisePowerCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 4),
    _NoisePowerCounter_Type()
)
noisePowerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerCounter.setStatus("current")
_NoisePowerCounterDiscontinuity_Type = DateAndTime
_NoisePowerCounterDiscontinuity_Object = MibTableColumn
noisePowerCounterDiscontinuity = _NoisePowerCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 5),
    _NoisePowerCounterDiscontinuity_Type()
)
noisePowerCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerCounterDiscontinuity.setStatus("current")
_NoisePowerCounterReset_Type = TruthValue
_NoisePowerCounterReset_Object = MibTableColumn
noisePowerCounterReset = _NoisePowerCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 6),
    _NoisePowerCounterReset_Type()
)
noisePowerCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noisePowerCounterReset.setStatus("current")
_NoisePowerLatestError_Type = DateAndTime
_NoisePowerLatestError_Object = MibTableColumn
noisePowerLatestError = _NoisePowerLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 7),
    _NoisePowerLatestError_Type()
)
noisePowerLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerLatestError.setStatus("current")
_NoisePowerActiveTime_Type = ActiveTime
_NoisePowerActiveTime_Object = MibTableColumn
noisePowerActiveTime = _NoisePowerActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 8),
    _NoisePowerActiveTime_Type()
)
noisePowerActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    noisePowerActiveTime.setUnits("second")
_NoisePowerMeasurementState_Type = MeasurementState
_NoisePowerMeasurementState_Object = MibTableColumn
noisePowerMeasurementState = _NoisePowerMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 9),
    _NoisePowerMeasurementState_Type()
)
noisePowerMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerMeasurementState.setStatus("current")
_NoisePowerValue_Type = FloatingPoint
_NoisePowerValue_Object = MibTableColumn
noisePowerValue = _NoisePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 7, 1, 10),
    _NoisePowerValue_Type()
)
noisePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisePowerValue.setStatus("current")
if mibBuilder.loadTexts:
    noisePowerValue.setUnits("dBm")
_IqAnalysisCS_ObjectIdentity = ObjectIdentity
iqAnalysisCS = _IqAnalysisCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9)
)
_MerCSTable_Object = MibTable
merCSTable = _MerCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2)
)
if mibBuilder.loadTexts:
    merCSTable.setStatus("current")
_MerCSEntry_Object = MibTableRow
merCSEntry = _MerCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1)
)
merCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "merCSInputNumber"),
)
if mibBuilder.loadTexts:
    merCSEntry.setStatus("current")
_MerCSInputNumber_Type = InputNumber
_MerCSInputNumber_Object = MibTableColumn
merCSInputNumber = _MerCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 1),
    _MerCSInputNumber_Type()
)
merCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    merCSInputNumber.setStatus("current")
_MerCSTestState_Type = TestState
_MerCSTestState_Object = MibTableColumn
merCSTestState = _MerCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 2),
    _MerCSTestState_Type()
)
merCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSTestState.setStatus("current")


class _MerCSEnable_Type(Enable):
    """Custom type merCSEnable based on Enable"""
    defaultBinValue = "1"


_MerCSEnable_Object = MibTableColumn
merCSEnable = _MerCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 3),
    _MerCSEnable_Type()
)
merCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    merCSEnable.setStatus("current")
_MerCSCounter_Type = Counter32
_MerCSCounter_Object = MibTableColumn
merCSCounter = _MerCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 4),
    _MerCSCounter_Type()
)
merCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSCounter.setStatus("current")
_MerCSCounterDiscontinuity_Type = DateAndTime
_MerCSCounterDiscontinuity_Object = MibTableColumn
merCSCounterDiscontinuity = _MerCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 5),
    _MerCSCounterDiscontinuity_Type()
)
merCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSCounterDiscontinuity.setStatus("current")


class _MerCSCounterReset_Type(TruthValue):
    """Custom type merCSCounterReset based on TruthValue"""


_MerCSCounterReset_Object = MibTableColumn
merCSCounterReset = _MerCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 6),
    _MerCSCounterReset_Type()
)
merCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    merCSCounterReset.setStatus("current")
_MerCSLatestError_Type = DateAndTime
_MerCSLatestError_Object = MibTableColumn
merCSLatestError = _MerCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 7),
    _MerCSLatestError_Type()
)
merCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSLatestError.setStatus("current")
_MerCSActiveTime_Type = ActiveTime
_MerCSActiveTime_Object = MibTableColumn
merCSActiveTime = _MerCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 8),
    _MerCSActiveTime_Type()
)
merCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    merCSActiveTime.setUnits("second")
_MerCSMeasurementState_Type = MeasurementState
_MerCSMeasurementState_Object = MibTableColumn
merCSMeasurementState = _MerCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 9),
    _MerCSMeasurementState_Type()
)
merCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSMeasurementState.setStatus("current")
_MerCSValue_Type = FloatingPoint
_MerCSValue_Object = MibTableColumn
merCSValue = _MerCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 2, 1, 10),
    _MerCSValue_Type()
)
merCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merCSValue.setStatus("current")
if mibBuilder.loadTexts:
    merCSValue.setUnits("dB")
_SteCS_ObjectIdentity = ObjectIdentity
steCS = _SteCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3)
)
_SteMeanCSTable_Object = MibTable
steMeanCSTable = _SteMeanCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1)
)
if mibBuilder.loadTexts:
    steMeanCSTable.setStatus("current")
_SteMeanCSEntry_Object = MibTableRow
steMeanCSEntry = _SteMeanCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1)
)
steMeanCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "steMeanCSInputNumber"),
)
if mibBuilder.loadTexts:
    steMeanCSEntry.setStatus("current")
_SteMeanCSInputNumber_Type = InputNumber
_SteMeanCSInputNumber_Object = MibTableColumn
steMeanCSInputNumber = _SteMeanCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 1),
    _SteMeanCSInputNumber_Type()
)
steMeanCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    steMeanCSInputNumber.setStatus("current")
_SteMeanCSTestState_Type = TestState
_SteMeanCSTestState_Object = MibTableColumn
steMeanCSTestState = _SteMeanCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 2),
    _SteMeanCSTestState_Type()
)
steMeanCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSTestState.setStatus("current")


class _SteMeanCSEnable_Type(Enable):
    """Custom type steMeanCSEnable based on Enable"""
    defaultBinValue = "1"


_SteMeanCSEnable_Object = MibTableColumn
steMeanCSEnable = _SteMeanCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 3),
    _SteMeanCSEnable_Type()
)
steMeanCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steMeanCSEnable.setStatus("current")
_SteMeanCSCounter_Type = Counter32
_SteMeanCSCounter_Object = MibTableColumn
steMeanCSCounter = _SteMeanCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 4),
    _SteMeanCSCounter_Type()
)
steMeanCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSCounter.setStatus("current")
_SteMeanCSCounterDiscontinuity_Type = DateAndTime
_SteMeanCSCounterDiscontinuity_Object = MibTableColumn
steMeanCSCounterDiscontinuity = _SteMeanCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 5),
    _SteMeanCSCounterDiscontinuity_Type()
)
steMeanCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSCounterDiscontinuity.setStatus("current")
_SteMeanCSCounterReset_Type = TruthValue
_SteMeanCSCounterReset_Object = MibTableColumn
steMeanCSCounterReset = _SteMeanCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 6),
    _SteMeanCSCounterReset_Type()
)
steMeanCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steMeanCSCounterReset.setStatus("current")
_SteMeanCSLatestError_Type = DateAndTime
_SteMeanCSLatestError_Object = MibTableColumn
steMeanCSLatestError = _SteMeanCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 7),
    _SteMeanCSLatestError_Type()
)
steMeanCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSLatestError.setStatus("current")
_SteMeanCSActiveTime_Type = ActiveTime
_SteMeanCSActiveTime_Object = MibTableColumn
steMeanCSActiveTime = _SteMeanCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 8),
    _SteMeanCSActiveTime_Type()
)
steMeanCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    steMeanCSActiveTime.setUnits("second")
_SteMeanCSMeasurementState_Type = MeasurementState
_SteMeanCSMeasurementState_Object = MibTableColumn
steMeanCSMeasurementState = _SteMeanCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 9),
    _SteMeanCSMeasurementState_Type()
)
steMeanCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSMeasurementState.setStatus("current")
_SteMeanCSValue_Type = FloatingPoint
_SteMeanCSValue_Object = MibTableColumn
steMeanCSValue = _SteMeanCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 1, 1, 10),
    _SteMeanCSValue_Type()
)
steMeanCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanCSValue.setStatus("current")
_SteDeviationCSTable_Object = MibTable
steDeviationCSTable = _SteDeviationCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2)
)
if mibBuilder.loadTexts:
    steDeviationCSTable.setStatus("current")
_SteDeviationCSEntry_Object = MibTableRow
steDeviationCSEntry = _SteDeviationCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1)
)
steDeviationCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "steDeviationCSInputNumber"),
)
if mibBuilder.loadTexts:
    steDeviationCSEntry.setStatus("current")
_SteDeviationCSInputNumber_Type = InputNumber
_SteDeviationCSInputNumber_Object = MibTableColumn
steDeviationCSInputNumber = _SteDeviationCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 1),
    _SteDeviationCSInputNumber_Type()
)
steDeviationCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    steDeviationCSInputNumber.setStatus("current")
_SteDeviationCSTestState_Type = TestState
_SteDeviationCSTestState_Object = MibTableColumn
steDeviationCSTestState = _SteDeviationCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 2),
    _SteDeviationCSTestState_Type()
)
steDeviationCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSTestState.setStatus("current")


class _SteDeviationCSEnable_Type(Enable):
    """Custom type steDeviationCSEnable based on Enable"""
    defaultBinValue = "1"


_SteDeviationCSEnable_Object = MibTableColumn
steDeviationCSEnable = _SteDeviationCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 3),
    _SteDeviationCSEnable_Type()
)
steDeviationCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steDeviationCSEnable.setStatus("current")
_SteDeviationCSCounter_Type = Counter32
_SteDeviationCSCounter_Object = MibTableColumn
steDeviationCSCounter = _SteDeviationCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 4),
    _SteDeviationCSCounter_Type()
)
steDeviationCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSCounter.setStatus("current")
_SteDeviationCSCounterDiscontinuity_Type = DateAndTime
_SteDeviationCSCounterDiscontinuity_Object = MibTableColumn
steDeviationCSCounterDiscontinuity = _SteDeviationCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 5),
    _SteDeviationCSCounterDiscontinuity_Type()
)
steDeviationCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSCounterDiscontinuity.setStatus("current")


class _SteDeviationCSCounterReset_Type(TruthValue):
    """Custom type steDeviationCSCounterReset based on TruthValue"""


_SteDeviationCSCounterReset_Object = MibTableColumn
steDeviationCSCounterReset = _SteDeviationCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 6),
    _SteDeviationCSCounterReset_Type()
)
steDeviationCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steDeviationCSCounterReset.setStatus("current")
_SteDeviationCSLatestError_Type = DateAndTime
_SteDeviationCSLatestError_Object = MibTableColumn
steDeviationCSLatestError = _SteDeviationCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 7),
    _SteDeviationCSLatestError_Type()
)
steDeviationCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSLatestError.setStatus("current")
_SteDeviationCSActiveTime_Type = ActiveTime
_SteDeviationCSActiveTime_Object = MibTableColumn
steDeviationCSActiveTime = _SteDeviationCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 8),
    _SteDeviationCSActiveTime_Type()
)
steDeviationCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    steDeviationCSActiveTime.setUnits("second")
_SteDeviationCSMeasurementState_Type = MeasurementState
_SteDeviationCSMeasurementState_Object = MibTableColumn
steDeviationCSMeasurementState = _SteDeviationCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 9),
    _SteDeviationCSMeasurementState_Type()
)
steDeviationCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSMeasurementState.setStatus("current")
_SteDeviationCSValue_Type = FloatingPoint
_SteDeviationCSValue_Object = MibTableColumn
steDeviationCSValue = _SteDeviationCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 3, 2, 1, 10),
    _SteDeviationCSValue_Type()
)
steDeviationCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationCSValue.setStatus("current")
_CsCSTable_Object = MibTable
csCSTable = _CsCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4)
)
if mibBuilder.loadTexts:
    csCSTable.setStatus("current")
_CsCSEntry_Object = MibTableRow
csCSEntry = _CsCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1)
)
csCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "csCSInputNumber"),
)
if mibBuilder.loadTexts:
    csCSEntry.setStatus("current")
_CsCSInputNumber_Type = InputNumber
_CsCSInputNumber_Object = MibTableColumn
csCSInputNumber = _CsCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 1),
    _CsCSInputNumber_Type()
)
csCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csCSInputNumber.setStatus("current")
_CsCSTestState_Type = TestState
_CsCSTestState_Object = MibTableColumn
csCSTestState = _CsCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 2),
    _CsCSTestState_Type()
)
csCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSTestState.setStatus("current")


class _CsCSEnable_Type(Enable):
    """Custom type csCSEnable based on Enable"""
    defaultBinValue = "1"


_CsCSEnable_Object = MibTableColumn
csCSEnable = _CsCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 3),
    _CsCSEnable_Type()
)
csCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csCSEnable.setStatus("current")
_CsCSCounter_Type = Counter32
_CsCSCounter_Object = MibTableColumn
csCSCounter = _CsCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 4),
    _CsCSCounter_Type()
)
csCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSCounter.setStatus("current")
_CsCSCounterDiscontinuity_Type = DateAndTime
_CsCSCounterDiscontinuity_Object = MibTableColumn
csCSCounterDiscontinuity = _CsCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 5),
    _CsCSCounterDiscontinuity_Type()
)
csCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSCounterDiscontinuity.setStatus("current")


class _CsCSCounterReset_Type(TruthValue):
    """Custom type csCSCounterReset based on TruthValue"""


_CsCSCounterReset_Object = MibTableColumn
csCSCounterReset = _CsCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 6),
    _CsCSCounterReset_Type()
)
csCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csCSCounterReset.setStatus("current")
_CsCSLatestError_Type = DateAndTime
_CsCSLatestError_Object = MibTableColumn
csCSLatestError = _CsCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 7),
    _CsCSLatestError_Type()
)
csCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSLatestError.setStatus("current")
_CsCSActiveTime_Type = ActiveTime
_CsCSActiveTime_Object = MibTableColumn
csCSActiveTime = _CsCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 8),
    _CsCSActiveTime_Type()
)
csCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    csCSActiveTime.setUnits("second")
_CsCSMeasurementState_Type = MeasurementState
_CsCSMeasurementState_Object = MibTableColumn
csCSMeasurementState = _CsCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 9),
    _CsCSMeasurementState_Type()
)
csCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSMeasurementState.setStatus("current")
_CsCSValue_Type = FloatingPoint
_CsCSValue_Object = MibTableColumn
csCSValue = _CsCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 4, 1, 10),
    _CsCSValue_Type()
)
csCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCSValue.setStatus("current")
if mibBuilder.loadTexts:
    csCSValue.setUnits("dB")
_AiCSTable_Object = MibTable
aiCSTable = _AiCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5)
)
if mibBuilder.loadTexts:
    aiCSTable.setStatus("current")
_AiCSEntry_Object = MibTableRow
aiCSEntry = _AiCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1)
)
aiCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "aiCSInputNumber"),
)
if mibBuilder.loadTexts:
    aiCSEntry.setStatus("current")
_AiCSInputNumber_Type = InputNumber
_AiCSInputNumber_Object = MibTableColumn
aiCSInputNumber = _AiCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 1),
    _AiCSInputNumber_Type()
)
aiCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aiCSInputNumber.setStatus("current")
_AiCSTestState_Type = TestState
_AiCSTestState_Object = MibTableColumn
aiCSTestState = _AiCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 2),
    _AiCSTestState_Type()
)
aiCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSTestState.setStatus("current")


class _AiCSEnable_Type(Enable):
    """Custom type aiCSEnable based on Enable"""
    defaultBinValue = "1"


_AiCSEnable_Object = MibTableColumn
aiCSEnable = _AiCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 3),
    _AiCSEnable_Type()
)
aiCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCSEnable.setStatus("current")
_AiCSCounter_Type = Counter32
_AiCSCounter_Object = MibTableColumn
aiCSCounter = _AiCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 4),
    _AiCSCounter_Type()
)
aiCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSCounter.setStatus("current")
_AiCSCounterDiscontinuity_Type = DateAndTime
_AiCSCounterDiscontinuity_Object = MibTableColumn
aiCSCounterDiscontinuity = _AiCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 5),
    _AiCSCounterDiscontinuity_Type()
)
aiCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSCounterDiscontinuity.setStatus("current")


class _AiCSCounterReset_Type(TruthValue):
    """Custom type aiCSCounterReset based on TruthValue"""


_AiCSCounterReset_Object = MibTableColumn
aiCSCounterReset = _AiCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 6),
    _AiCSCounterReset_Type()
)
aiCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCSCounterReset.setStatus("current")
_AiCSLatestError_Type = DateAndTime
_AiCSLatestError_Object = MibTableColumn
aiCSLatestError = _AiCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 7),
    _AiCSLatestError_Type()
)
aiCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSLatestError.setStatus("current")
_AiCSActiveTime_Type = ActiveTime
_AiCSActiveTime_Object = MibTableColumn
aiCSActiveTime = _AiCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 8),
    _AiCSActiveTime_Type()
)
aiCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    aiCSActiveTime.setUnits("second")
_AiCSMeasurementState_Type = MeasurementState
_AiCSMeasurementState_Object = MibTableColumn
aiCSMeasurementState = _AiCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 9),
    _AiCSMeasurementState_Type()
)
aiCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSMeasurementState.setStatus("current")
_AiCSValue_Type = FloatingPoint
_AiCSValue_Object = MibTableColumn
aiCSValue = _AiCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 5, 1, 10),
    _AiCSValue_Type()
)
aiCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCSValue.setStatus("current")
_QeCSTable_Object = MibTable
qeCSTable = _QeCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6)
)
if mibBuilder.loadTexts:
    qeCSTable.setStatus("current")
_QeCSEntry_Object = MibTableRow
qeCSEntry = _QeCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1)
)
qeCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "qeCSInputNumber"),
)
if mibBuilder.loadTexts:
    qeCSEntry.setStatus("current")
_QeCSInputNumber_Type = InputNumber
_QeCSInputNumber_Object = MibTableColumn
qeCSInputNumber = _QeCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 1),
    _QeCSInputNumber_Type()
)
qeCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qeCSInputNumber.setStatus("current")
_QeCSTestState_Type = TestState
_QeCSTestState_Object = MibTableColumn
qeCSTestState = _QeCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 2),
    _QeCSTestState_Type()
)
qeCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSTestState.setStatus("current")


class _QeCSEnable_Type(Enable):
    """Custom type qeCSEnable based on Enable"""
    defaultBinValue = "1"


_QeCSEnable_Object = MibTableColumn
qeCSEnable = _QeCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 3),
    _QeCSEnable_Type()
)
qeCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qeCSEnable.setStatus("current")
_QeCSCounter_Type = Counter32
_QeCSCounter_Object = MibTableColumn
qeCSCounter = _QeCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 4),
    _QeCSCounter_Type()
)
qeCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSCounter.setStatus("current")
_QeCSCounterDiscontinuity_Type = DateAndTime
_QeCSCounterDiscontinuity_Object = MibTableColumn
qeCSCounterDiscontinuity = _QeCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 5),
    _QeCSCounterDiscontinuity_Type()
)
qeCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSCounterDiscontinuity.setStatus("current")


class _QeCSCounterReset_Type(TruthValue):
    """Custom type qeCSCounterReset based on TruthValue"""


_QeCSCounterReset_Object = MibTableColumn
qeCSCounterReset = _QeCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 6),
    _QeCSCounterReset_Type()
)
qeCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qeCSCounterReset.setStatus("current")
_QeCSLatestError_Type = DateAndTime
_QeCSLatestError_Object = MibTableColumn
qeCSLatestError = _QeCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 7),
    _QeCSLatestError_Type()
)
qeCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSLatestError.setStatus("current")
_QeCSActiveTime_Type = ActiveTime
_QeCSActiveTime_Object = MibTableColumn
qeCSActiveTime = _QeCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 8),
    _QeCSActiveTime_Type()
)
qeCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    qeCSActiveTime.setUnits("second")
_QeCSMeasurementState_Type = MeasurementState
_QeCSMeasurementState_Object = MibTableColumn
qeCSMeasurementState = _QeCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 9),
    _QeCSMeasurementState_Type()
)
qeCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSMeasurementState.setStatus("current")
_QeCSValue_Type = FloatingPoint
_QeCSValue_Object = MibTableColumn
qeCSValue = _QeCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 6, 1, 10),
    _QeCSValue_Type()
)
qeCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeCSValue.setStatus("current")
if mibBuilder.loadTexts:
    qeCSValue.setUnits("degree")
_RteCSTable_Object = MibTable
rteCSTable = _RteCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7)
)
if mibBuilder.loadTexts:
    rteCSTable.setStatus("current")
_RteCSEntry_Object = MibTableRow
rteCSEntry = _RteCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1)
)
rteCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rteCSInputNumber"),
)
if mibBuilder.loadTexts:
    rteCSEntry.setStatus("current")
_RteCSInputNumber_Type = InputNumber
_RteCSInputNumber_Object = MibTableColumn
rteCSInputNumber = _RteCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 1),
    _RteCSInputNumber_Type()
)
rteCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rteCSInputNumber.setStatus("current")
_RteCSTestState_Type = TestState
_RteCSTestState_Object = MibTableColumn
rteCSTestState = _RteCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 2),
    _RteCSTestState_Type()
)
rteCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSTestState.setStatus("current")


class _RteCSEnable_Type(Enable):
    """Custom type rteCSEnable based on Enable"""
    defaultBinValue = "1"


_RteCSEnable_Object = MibTableColumn
rteCSEnable = _RteCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 3),
    _RteCSEnable_Type()
)
rteCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rteCSEnable.setStatus("current")
_RteCSCounter_Type = Counter32
_RteCSCounter_Object = MibTableColumn
rteCSCounter = _RteCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 4),
    _RteCSCounter_Type()
)
rteCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSCounter.setStatus("current")
_RteCSCounterDiscontinuity_Type = DateAndTime
_RteCSCounterDiscontinuity_Object = MibTableColumn
rteCSCounterDiscontinuity = _RteCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 5),
    _RteCSCounterDiscontinuity_Type()
)
rteCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSCounterDiscontinuity.setStatus("current")


class _RteCSCounterReset_Type(TruthValue):
    """Custom type rteCSCounterReset based on TruthValue"""


_RteCSCounterReset_Object = MibTableColumn
rteCSCounterReset = _RteCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 6),
    _RteCSCounterReset_Type()
)
rteCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rteCSCounterReset.setStatus("current")
_RteCSLatestError_Type = DateAndTime
_RteCSLatestError_Object = MibTableColumn
rteCSLatestError = _RteCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 7),
    _RteCSLatestError_Type()
)
rteCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSLatestError.setStatus("current")
_RteCSActiveTime_Type = ActiveTime
_RteCSActiveTime_Object = MibTableColumn
rteCSActiveTime = _RteCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 8),
    _RteCSActiveTime_Type()
)
rteCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rteCSActiveTime.setUnits("second")
_RteCSMeasurementState_Type = MeasurementState
_RteCSMeasurementState_Object = MibTableColumn
rteCSMeasurementState = _RteCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 9),
    _RteCSMeasurementState_Type()
)
rteCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSMeasurementState.setStatus("current")
_RteCSValue_Type = FloatingPoint
_RteCSValue_Object = MibTableColumn
rteCSValue = _RteCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 7, 1, 10),
    _RteCSValue_Type()
)
rteCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rteCSValue.setStatus("current")
_CiCSTable_Object = MibTable
ciCSTable = _CiCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8)
)
if mibBuilder.loadTexts:
    ciCSTable.setStatus("current")
_CiCSEntry_Object = MibTableRow
ciCSEntry = _CiCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1)
)
ciCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "ciCSInputNumber"),
)
if mibBuilder.loadTexts:
    ciCSEntry.setStatus("current")
_CiCSInputNumber_Type = InputNumber
_CiCSInputNumber_Object = MibTableColumn
ciCSInputNumber = _CiCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 1),
    _CiCSInputNumber_Type()
)
ciCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciCSInputNumber.setStatus("current")
_CiCSTestState_Type = TestState
_CiCSTestState_Object = MibTableColumn
ciCSTestState = _CiCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 2),
    _CiCSTestState_Type()
)
ciCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSTestState.setStatus("current")


class _CiCSEnable_Type(Enable):
    """Custom type ciCSEnable based on Enable"""
    defaultBinValue = "1"


_CiCSEnable_Object = MibTableColumn
ciCSEnable = _CiCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 3),
    _CiCSEnable_Type()
)
ciCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciCSEnable.setStatus("current")
_CiCSCounter_Type = Counter32
_CiCSCounter_Object = MibTableColumn
ciCSCounter = _CiCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 4),
    _CiCSCounter_Type()
)
ciCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSCounter.setStatus("current")
_CiCSCounterDiscontinuity_Type = DateAndTime
_CiCSCounterDiscontinuity_Object = MibTableColumn
ciCSCounterDiscontinuity = _CiCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 5),
    _CiCSCounterDiscontinuity_Type()
)
ciCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSCounterDiscontinuity.setStatus("current")


class _CiCSCounterReset_Type(TruthValue):
    """Custom type ciCSCounterReset based on TruthValue"""


_CiCSCounterReset_Object = MibTableColumn
ciCSCounterReset = _CiCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 6),
    _CiCSCounterReset_Type()
)
ciCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciCSCounterReset.setStatus("current")
_CiCSLatestError_Type = DateAndTime
_CiCSLatestError_Object = MibTableColumn
ciCSLatestError = _CiCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 7),
    _CiCSLatestError_Type()
)
ciCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSLatestError.setStatus("current")
_CiCSActiveTime_Type = ActiveTime
_CiCSActiveTime_Object = MibTableColumn
ciCSActiveTime = _CiCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 8),
    _CiCSActiveTime_Type()
)
ciCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    ciCSActiveTime.setUnits("second")
_CiCSMeasurementState_Type = MeasurementState
_CiCSMeasurementState_Object = MibTableColumn
ciCSMeasurementState = _CiCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 9),
    _CiCSMeasurementState_Type()
)
ciCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSMeasurementState.setStatus("current")
_CiCSValue_Type = FloatingPoint
_CiCSValue_Object = MibTableColumn
ciCSValue = _CiCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 8, 1, 10),
    _CiCSValue_Type()
)
ciCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCSValue.setStatus("current")
if mibBuilder.loadTexts:
    ciCSValue.setUnits("dB")
_PjCSTable_Object = MibTable
pjCSTable = _PjCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9)
)
if mibBuilder.loadTexts:
    pjCSTable.setStatus("current")
_PjCSEntry_Object = MibTableRow
pjCSEntry = _PjCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1)
)
pjCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "pjCSInputNumber"),
)
if mibBuilder.loadTexts:
    pjCSEntry.setStatus("current")
_PjCSInputNumber_Type = InputNumber
_PjCSInputNumber_Object = MibTableColumn
pjCSInputNumber = _PjCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 1),
    _PjCSInputNumber_Type()
)
pjCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pjCSInputNumber.setStatus("current")
_PjCSTestState_Type = TestState
_PjCSTestState_Object = MibTableColumn
pjCSTestState = _PjCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 2),
    _PjCSTestState_Type()
)
pjCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSTestState.setStatus("current")


class _PjCSEnable_Type(Enable):
    """Custom type pjCSEnable based on Enable"""
    defaultBinValue = "1"


_PjCSEnable_Object = MibTableColumn
pjCSEnable = _PjCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 3),
    _PjCSEnable_Type()
)
pjCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pjCSEnable.setStatus("current")
_PjCSCounter_Type = Counter32
_PjCSCounter_Object = MibTableColumn
pjCSCounter = _PjCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 4),
    _PjCSCounter_Type()
)
pjCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSCounter.setStatus("current")
_PjCSCounterDiscontinuity_Type = DateAndTime
_PjCSCounterDiscontinuity_Object = MibTableColumn
pjCSCounterDiscontinuity = _PjCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 5),
    _PjCSCounterDiscontinuity_Type()
)
pjCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSCounterDiscontinuity.setStatus("current")


class _PjCSCounterReset_Type(TruthValue):
    """Custom type pjCSCounterReset based on TruthValue"""


_PjCSCounterReset_Object = MibTableColumn
pjCSCounterReset = _PjCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 6),
    _PjCSCounterReset_Type()
)
pjCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pjCSCounterReset.setStatus("current")
_PjCSLatestError_Type = DateAndTime
_PjCSLatestError_Object = MibTableColumn
pjCSLatestError = _PjCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 7),
    _PjCSLatestError_Type()
)
pjCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSLatestError.setStatus("current")
_PjCSActiveTime_Type = ActiveTime
_PjCSActiveTime_Object = MibTableColumn
pjCSActiveTime = _PjCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 8),
    _PjCSActiveTime_Type()
)
pjCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    pjCSActiveTime.setUnits("second")
_PjCSMeasurementState_Type = MeasurementState
_PjCSMeasurementState_Object = MibTableColumn
pjCSMeasurementState = _PjCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 9),
    _PjCSMeasurementState_Type()
)
pjCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSMeasurementState.setStatus("current")
_PjCSValue_Type = FloatingPoint
_PjCSValue_Object = MibTableColumn
pjCSValue = _PjCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 9, 1, 10),
    _PjCSValue_Type()
)
pjCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjCSValue.setStatus("current")
if mibBuilder.loadTexts:
    pjCSValue.setUnits("degree")
_SnrCSTable_Object = MibTable
snrCSTable = _SnrCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10)
)
if mibBuilder.loadTexts:
    snrCSTable.setStatus("current")
_SnrCSEntry_Object = MibTableRow
snrCSEntry = _SnrCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1)
)
snrCSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "snrCSInputNumber"),
)
if mibBuilder.loadTexts:
    snrCSEntry.setStatus("current")
_SnrCSInputNumber_Type = InputNumber
_SnrCSInputNumber_Object = MibTableColumn
snrCSInputNumber = _SnrCSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 1),
    _SnrCSInputNumber_Type()
)
snrCSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snrCSInputNumber.setStatus("current")
_SnrCSTestState_Type = TestState
_SnrCSTestState_Object = MibTableColumn
snrCSTestState = _SnrCSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 2),
    _SnrCSTestState_Type()
)
snrCSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSTestState.setStatus("current")


class _SnrCSEnable_Type(Enable):
    """Custom type snrCSEnable based on Enable"""
    defaultBinValue = "1"


_SnrCSEnable_Object = MibTableColumn
snrCSEnable = _SnrCSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 3),
    _SnrCSEnable_Type()
)
snrCSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrCSEnable.setStatus("current")
_SnrCSCounter_Type = Counter32
_SnrCSCounter_Object = MibTableColumn
snrCSCounter = _SnrCSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 4),
    _SnrCSCounter_Type()
)
snrCSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSCounter.setStatus("current")
_SnrCSCounterDiscontinuity_Type = DateAndTime
_SnrCSCounterDiscontinuity_Object = MibTableColumn
snrCSCounterDiscontinuity = _SnrCSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 5),
    _SnrCSCounterDiscontinuity_Type()
)
snrCSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSCounterDiscontinuity.setStatus("current")


class _SnrCSCounterReset_Type(TruthValue):
    """Custom type snrCSCounterReset based on TruthValue"""


_SnrCSCounterReset_Object = MibTableColumn
snrCSCounterReset = _SnrCSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 6),
    _SnrCSCounterReset_Type()
)
snrCSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrCSCounterReset.setStatus("current")
_SnrCSLatestError_Type = DateAndTime
_SnrCSLatestError_Object = MibTableColumn
snrCSLatestError = _SnrCSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 7),
    _SnrCSLatestError_Type()
)
snrCSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSLatestError.setStatus("current")
_SnrCSActiveTime_Type = ActiveTime
_SnrCSActiveTime_Object = MibTableColumn
snrCSActiveTime = _SnrCSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 8),
    _SnrCSActiveTime_Type()
)
snrCSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    snrCSActiveTime.setUnits("second")
_SnrCSMeasurementState_Type = MeasurementState
_SnrCSMeasurementState_Object = MibTableColumn
snrCSMeasurementState = _SnrCSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 9),
    _SnrCSMeasurementState_Type()
)
snrCSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSMeasurementState.setStatus("current")
_SnrCSValue_Type = FloatingPoint
_SnrCSValue_Object = MibTableColumn
snrCSValue = _SnrCSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 9, 10, 1, 10),
    _SnrCSValue_Type()
)
snrCSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrCSValue.setStatus("current")
if mibBuilder.loadTexts:
    snrCSValue.setUnits("dB")
_CableSatPreferencesTable_Object = MibTable
cableSatPreferencesTable = _CableSatPreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100)
)
if mibBuilder.loadTexts:
    cableSatPreferencesTable.setStatus("current")
_CableSatPreferencesEntry_Object = MibTableRow
cableSatPreferencesEntry = _CableSatPreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1)
)
cableSatPreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "cableSatPrefInputNumber"),
)
if mibBuilder.loadTexts:
    cableSatPreferencesEntry.setStatus("current")
_CableSatPrefInputNumber_Type = InputNumber
_CableSatPrefInputNumber_Object = MibTableColumn
cableSatPrefInputNumber = _CableSatPrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 1),
    _CableSatPrefInputNumber_Type()
)
cableSatPrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableSatPrefInputNumber.setStatus("current")
_CableSatPrefCentreFrequency_Type = FloatingPoint
_CableSatPrefCentreFrequency_Object = MibTableColumn
cableSatPrefCentreFrequency = _CableSatPrefCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 2),
    _CableSatPrefCentreFrequency_Type()
)
cableSatPrefCentreFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefCentreFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefCentreFrequency.setUnits("MHz")
_CableSatPrefModulation_Type = Modulation
_CableSatPrefModulation_Object = MibTableColumn
cableSatPrefModulation = _CableSatPrefModulation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 3),
    _CableSatPrefModulation_Type()
)
cableSatPrefModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefModulation.setStatus("current")
_CableSatPrefSysAvailUATMode_Type = UATMode
_CableSatPrefSysAvailUATMode_Object = MibTableColumn
cableSatPrefSysAvailUATMode = _CableSatPrefSysAvailUATMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 4),
    _CableSatPrefSysAvailUATMode_Type()
)
cableSatPrefSysAvailUATMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailUATMode.setStatus("current")
_CableSatPrefSysAvailN_Type = Unsigned32
_CableSatPrefSysAvailN_Object = MibTableColumn
cableSatPrefSysAvailN = _CableSatPrefSysAvailN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 5),
    _CableSatPrefSysAvailN_Type()
)
cableSatPrefSysAvailN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailN.setStatus("current")
_CableSatPrefSysAvailT_Type = FloatingPoint
_CableSatPrefSysAvailT_Object = MibTableColumn
cableSatPrefSysAvailT = _CableSatPrefSysAvailT_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 6),
    _CableSatPrefSysAvailT_Type()
)
cableSatPrefSysAvailT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailT.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailT.setUnits("second")
_CableSatPrefSysAvailM_Type = Unsigned32
_CableSatPrefSysAvailM_Object = MibTableColumn
cableSatPrefSysAvailM = _CableSatPrefSysAvailM_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 7),
    _CableSatPrefSysAvailM_Type()
)
cableSatPrefSysAvailM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailM.setStatus("current")
_CableSatPrefSysAvailTI_Type = FloatingPoint
_CableSatPrefSysAvailTI_Object = MibTableColumn
cableSatPrefSysAvailTI = _CableSatPrefSysAvailTI_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 8),
    _CableSatPrefSysAvailTI_Type()
)
cableSatPrefSysAvailTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailTI.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailTI.setUnits("second")
_CableSatPrefSysAvailEBPerCent_Type = FloatingPoint
_CableSatPrefSysAvailEBPerCent_Object = MibTableColumn
cableSatPrefSysAvailEBPerCent = _CableSatPrefSysAvailEBPerCent_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 9),
    _CableSatPrefSysAvailEBPerCent_Type()
)
cableSatPrefSysAvailEBPerCent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailEBPerCent.setStatus("current")
_CableSatPrefSysAvailTotalTime_Type = FloatingPoint
_CableSatPrefSysAvailTotalTime_Object = MibTableColumn
cableSatPrefSysAvailTotalTime = _CableSatPrefSysAvailTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 10),
    _CableSatPrefSysAvailTotalTime_Type()
)
cableSatPrefSysAvailTotalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailTotalTime.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSysAvailTotalTime.setUnits("second")
_CableSatPrefLinkAvailUATMode_Type = UATMode
_CableSatPrefLinkAvailUATMode_Object = MibTableColumn
cableSatPrefLinkAvailUATMode = _CableSatPrefLinkAvailUATMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 11),
    _CableSatPrefLinkAvailUATMode_Type()
)
cableSatPrefLinkAvailUATMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailUATMode.setStatus("current")
_CableSatPrefLinkAvailN_Type = Unsigned32
_CableSatPrefLinkAvailN_Object = MibTableColumn
cableSatPrefLinkAvailN = _CableSatPrefLinkAvailN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 12),
    _CableSatPrefLinkAvailN_Type()
)
cableSatPrefLinkAvailN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailN.setStatus("current")
_CableSatPrefLinkAvailT_Type = FloatingPoint
_CableSatPrefLinkAvailT_Object = MibTableColumn
cableSatPrefLinkAvailT = _CableSatPrefLinkAvailT_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 13),
    _CableSatPrefLinkAvailT_Type()
)
cableSatPrefLinkAvailT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailT.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailT.setUnits("second")
_CableSatPrefLinkAvailM_Type = Unsigned32
_CableSatPrefLinkAvailM_Object = MibTableColumn
cableSatPrefLinkAvailM = _CableSatPrefLinkAvailM_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 14),
    _CableSatPrefLinkAvailM_Type()
)
cableSatPrefLinkAvailM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailM.setStatus("current")
_CableSatPrefLinkAvailTI_Type = FloatingPoint
_CableSatPrefLinkAvailTI_Object = MibTableColumn
cableSatPrefLinkAvailTI = _CableSatPrefLinkAvailTI_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 15),
    _CableSatPrefLinkAvailTI_Type()
)
cableSatPrefLinkAvailTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailTI.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailTI.setUnits("second")
_CableSatPrefLinkAvailUPPerCent_Type = FloatingPoint
_CableSatPrefLinkAvailUPPerCent_Object = MibTableColumn
cableSatPrefLinkAvailUPPerCent = _CableSatPrefLinkAvailUPPerCent_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 16),
    _CableSatPrefLinkAvailUPPerCent_Type()
)
cableSatPrefLinkAvailUPPerCent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailUPPerCent.setStatus("current")
_CableSatPrefLinkAvailTotalTime_Type = FloatingPoint
_CableSatPrefLinkAvailTotalTime_Object = MibTableColumn
cableSatPrefLinkAvailTotalTime = _CableSatPrefLinkAvailTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 17),
    _CableSatPrefLinkAvailTotalTime_Type()
)
cableSatPrefLinkAvailTotalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailTotalTime.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefLinkAvailTotalTime.setUnits("second")
_CableSatPrefBERMax_Type = FloatingPoint
_CableSatPrefBERMax_Object = MibTableColumn
cableSatPrefBERMax = _CableSatPrefBERMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 18),
    _CableSatPrefBERMax_Type()
)
cableSatPrefBERMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefBERMax.setStatus("current")
_CableSatPrefSignalPowerMin_Type = FloatingPoint
_CableSatPrefSignalPowerMin_Object = MibTableColumn
cableSatPrefSignalPowerMin = _CableSatPrefSignalPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 19),
    _CableSatPrefSignalPowerMin_Type()
)
cableSatPrefSignalPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSignalPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSignalPowerMin.setUnits("dBm")
_CableSatPrefSignalPowerMax_Type = FloatingPoint
_CableSatPrefSignalPowerMax_Object = MibTableColumn
cableSatPrefSignalPowerMax = _CableSatPrefSignalPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 20),
    _CableSatPrefSignalPowerMax_Type()
)
cableSatPrefSignalPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSignalPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSignalPowerMax.setUnits("dBm")
_CableSatPrefNoisePowerMax_Type = FloatingPoint
_CableSatPrefNoisePowerMax_Object = MibTableColumn
cableSatPrefNoisePowerMax = _CableSatPrefNoisePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 21),
    _CableSatPrefNoisePowerMax_Type()
)
cableSatPrefNoisePowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefNoisePowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefNoisePowerMax.setUnits("dBm")
_CableSatPrefMerCSMin_Type = FloatingPoint
_CableSatPrefMerCSMin_Object = MibTableColumn
cableSatPrefMerCSMin = _CableSatPrefMerCSMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 22),
    _CableSatPrefMerCSMin_Type()
)
cableSatPrefMerCSMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefMerCSMin.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefMerCSMin.setUnits("dB")
_CableSatPrefSteMeanCSMax_Type = FloatingPoint
_CableSatPrefSteMeanCSMax_Object = MibTableColumn
cableSatPrefSteMeanCSMax = _CableSatPrefSteMeanCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 23),
    _CableSatPrefSteMeanCSMax_Type()
)
cableSatPrefSteMeanCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSteMeanCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSteMeanCSMax.setUnits("dB")
_CableSatPrefSteDeviationCSMax_Type = FloatingPoint
_CableSatPrefSteDeviationCSMax_Object = MibTableColumn
cableSatPrefSteDeviationCSMax = _CableSatPrefSteDeviationCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 24),
    _CableSatPrefSteDeviationCSMax_Type()
)
cableSatPrefSteDeviationCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSteDeviationCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSteDeviationCSMax.setUnits("dB")
_CableSatPrefCsCSMin_Type = FloatingPoint
_CableSatPrefCsCSMin_Object = MibTableColumn
cableSatPrefCsCSMin = _CableSatPrefCsCSMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 25),
    _CableSatPrefCsCSMin_Type()
)
cableSatPrefCsCSMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefCsCSMin.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefCsCSMin.setUnits("dB")
_CableSatPrefAiCSMax_Type = FloatingPoint
_CableSatPrefAiCSMax_Object = MibTableColumn
cableSatPrefAiCSMax = _CableSatPrefAiCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 26),
    _CableSatPrefAiCSMax_Type()
)
cableSatPrefAiCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefAiCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefAiCSMax.setUnits("dB")
_CableSatPrefQeCSMax_Type = FloatingPoint
_CableSatPrefQeCSMax_Object = MibTableColumn
cableSatPrefQeCSMax = _CableSatPrefQeCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 27),
    _CableSatPrefQeCSMax_Type()
)
cableSatPrefQeCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefQeCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefQeCSMax.setUnits("dB")
_CableSatPrefRteCSMax_Type = FloatingPoint
_CableSatPrefRteCSMax_Object = MibTableColumn
cableSatPrefRteCSMax = _CableSatPrefRteCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 28),
    _CableSatPrefRteCSMax_Type()
)
cableSatPrefRteCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefRteCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefRteCSMax.setUnits("dB")
_CableSatPrefCiCSMin_Type = FloatingPoint
_CableSatPrefCiCSMin_Object = MibTableColumn
cableSatPrefCiCSMin = _CableSatPrefCiCSMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 29),
    _CableSatPrefCiCSMin_Type()
)
cableSatPrefCiCSMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefCiCSMin.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefCiCSMin.setUnits("dB")
_CableSatPrefPjCSMax_Type = FloatingPoint
_CableSatPrefPjCSMax_Object = MibTableColumn
cableSatPrefPjCSMax = _CableSatPrefPjCSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 30),
    _CableSatPrefPjCSMax_Type()
)
cableSatPrefPjCSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefPjCSMax.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefPjCSMax.setUnits("dB")
_CableSatPrefSnrCSMin_Type = FloatingPoint
_CableSatPrefSnrCSMin_Object = MibTableColumn
cableSatPrefSnrCSMin = _CableSatPrefSnrCSMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 6, 100, 1, 31),
    _CableSatPrefSnrCSMin_Type()
)
cableSatPrefSnrCSMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableSatPrefSnrCSMin.setStatus("current")
if mibBuilder.loadTexts:
    cableSatPrefSnrCSMin.setUnits("dB")
_Tr101290Cable_ObjectIdentity = ObjectIdentity
tr101290Cable = _Tr101290Cable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7)
)
_NoiseMarginTable_Object = MibTable
noiseMarginTable = _NoiseMarginTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    noiseMarginTable.setStatus("current")
_NoiseMarginEntry_Object = MibTableRow
noiseMarginEntry = _NoiseMarginEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1)
)
noiseMarginEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "noiseMarginInputNumber"),
)
if mibBuilder.loadTexts:
    noiseMarginEntry.setStatus("current")
_NoiseMarginInputNumber_Type = InputNumber
_NoiseMarginInputNumber_Object = MibTableColumn
noiseMarginInputNumber = _NoiseMarginInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 1),
    _NoiseMarginInputNumber_Type()
)
noiseMarginInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    noiseMarginInputNumber.setStatus("current")
_NoiseMarginTestState_Type = TestState
_NoiseMarginTestState_Object = MibTableColumn
noiseMarginTestState = _NoiseMarginTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 2),
    _NoiseMarginTestState_Type()
)
noiseMarginTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginTestState.setStatus("current")


class _NoiseMarginEnable_Type(Enable):
    """Custom type noiseMarginEnable based on Enable"""
    defaultBinValue = "1"


_NoiseMarginEnable_Object = MibTableColumn
noiseMarginEnable = _NoiseMarginEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 3),
    _NoiseMarginEnable_Type()
)
noiseMarginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiseMarginEnable.setStatus("current")
_NoiseMarginCounter_Type = Counter32
_NoiseMarginCounter_Object = MibTableColumn
noiseMarginCounter = _NoiseMarginCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 4),
    _NoiseMarginCounter_Type()
)
noiseMarginCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginCounter.setStatus("current")
_NoiseMarginCounterDiscontinuity_Type = DateAndTime
_NoiseMarginCounterDiscontinuity_Object = MibTableColumn
noiseMarginCounterDiscontinuity = _NoiseMarginCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 5),
    _NoiseMarginCounterDiscontinuity_Type()
)
noiseMarginCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginCounterDiscontinuity.setStatus("current")


class _NoiseMarginCounterReset_Type(TruthValue):
    """Custom type noiseMarginCounterReset based on TruthValue"""


_NoiseMarginCounterReset_Object = MibTableColumn
noiseMarginCounterReset = _NoiseMarginCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 6),
    _NoiseMarginCounterReset_Type()
)
noiseMarginCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiseMarginCounterReset.setStatus("current")
_NoiseMarginLatestError_Type = DateAndTime
_NoiseMarginLatestError_Object = MibTableColumn
noiseMarginLatestError = _NoiseMarginLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 7),
    _NoiseMarginLatestError_Type()
)
noiseMarginLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginLatestError.setStatus("current")
_NoiseMarginActiveTime_Type = ActiveTime
_NoiseMarginActiveTime_Object = MibTableColumn
noiseMarginActiveTime = _NoiseMarginActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 8),
    _NoiseMarginActiveTime_Type()
)
noiseMarginActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    noiseMarginActiveTime.setUnits("second")
_NoiseMarginMeasurementState_Type = MeasurementState
_NoiseMarginMeasurementState_Object = MibTableColumn
noiseMarginMeasurementState = _NoiseMarginMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 9),
    _NoiseMarginMeasurementState_Type()
)
noiseMarginMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginMeasurementState.setStatus("current")
_NoiseMarginValue_Type = FloatingPoint
_NoiseMarginValue_Object = MibTableColumn
noiseMarginValue = _NoiseMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 1, 1, 10),
    _NoiseMarginValue_Type()
)
noiseMarginValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseMarginValue.setStatus("current")
if mibBuilder.loadTexts:
    noiseMarginValue.setUnits("dB")
_EstNoiseMarginTable_Object = MibTable
estNoiseMarginTable = _EstNoiseMarginTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    estNoiseMarginTable.setStatus("current")
_EstNoiseMarginEntry_Object = MibTableRow
estNoiseMarginEntry = _EstNoiseMarginEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1)
)
estNoiseMarginEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "estNoiseMarginInputNumber"),
)
if mibBuilder.loadTexts:
    estNoiseMarginEntry.setStatus("current")
_EstNoiseMarginInputNumber_Type = InputNumber
_EstNoiseMarginInputNumber_Object = MibTableColumn
estNoiseMarginInputNumber = _EstNoiseMarginInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 1),
    _EstNoiseMarginInputNumber_Type()
)
estNoiseMarginInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    estNoiseMarginInputNumber.setStatus("current")
_EstNoiseMarginTestState_Type = TestState
_EstNoiseMarginTestState_Object = MibTableColumn
estNoiseMarginTestState = _EstNoiseMarginTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 2),
    _EstNoiseMarginTestState_Type()
)
estNoiseMarginTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginTestState.setStatus("current")


class _EstNoiseMarginEnable_Type(Enable):
    """Custom type estNoiseMarginEnable based on Enable"""
    defaultBinValue = "1"


_EstNoiseMarginEnable_Object = MibTableColumn
estNoiseMarginEnable = _EstNoiseMarginEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 3),
    _EstNoiseMarginEnable_Type()
)
estNoiseMarginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    estNoiseMarginEnable.setStatus("current")
_EstNoiseMarginCounter_Type = Counter32
_EstNoiseMarginCounter_Object = MibTableColumn
estNoiseMarginCounter = _EstNoiseMarginCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 4),
    _EstNoiseMarginCounter_Type()
)
estNoiseMarginCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginCounter.setStatus("current")
_EstNoiseMarginCounterDiscontinuity_Type = DateAndTime
_EstNoiseMarginCounterDiscontinuity_Object = MibTableColumn
estNoiseMarginCounterDiscontinuity = _EstNoiseMarginCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 5),
    _EstNoiseMarginCounterDiscontinuity_Type()
)
estNoiseMarginCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginCounterDiscontinuity.setStatus("current")


class _EstNoiseMarginCounterReset_Type(TruthValue):
    """Custom type estNoiseMarginCounterReset based on TruthValue"""


_EstNoiseMarginCounterReset_Object = MibTableColumn
estNoiseMarginCounterReset = _EstNoiseMarginCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 6),
    _EstNoiseMarginCounterReset_Type()
)
estNoiseMarginCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    estNoiseMarginCounterReset.setStatus("current")
_EstNoiseMarginLatestError_Type = DateAndTime
_EstNoiseMarginLatestError_Object = MibTableColumn
estNoiseMarginLatestError = _EstNoiseMarginLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 7),
    _EstNoiseMarginLatestError_Type()
)
estNoiseMarginLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginLatestError.setStatus("current")
_EstNoiseMarginActiveTime_Type = ActiveTime
_EstNoiseMarginActiveTime_Object = MibTableColumn
estNoiseMarginActiveTime = _EstNoiseMarginActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 8),
    _EstNoiseMarginActiveTime_Type()
)
estNoiseMarginActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    estNoiseMarginActiveTime.setUnits("second")
_EstNoiseMarginMeasurementState_Type = MeasurementState
_EstNoiseMarginMeasurementState_Object = MibTableColumn
estNoiseMarginMeasurementState = _EstNoiseMarginMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 9),
    _EstNoiseMarginMeasurementState_Type()
)
estNoiseMarginMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginMeasurementState.setStatus("current")
_EstNoiseMarginValue_Type = FloatingPoint
_EstNoiseMarginValue_Object = MibTableColumn
estNoiseMarginValue = _EstNoiseMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 2, 1, 10),
    _EstNoiseMarginValue_Type()
)
estNoiseMarginValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estNoiseMarginValue.setStatus("current")
if mibBuilder.loadTexts:
    estNoiseMarginValue.setUnits("dB")
_SignQualMarTTable_Object = MibTable
signQualMarTTable = _SignQualMarTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    signQualMarTTable.setStatus("current")
_SignQualMarTEntry_Object = MibTableRow
signQualMarTEntry = _SignQualMarTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1)
)
signQualMarTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "signQualMarTInputNumber"),
)
if mibBuilder.loadTexts:
    signQualMarTEntry.setStatus("current")
_SignQualMarTInputNumber_Type = InputNumber
_SignQualMarTInputNumber_Object = MibTableColumn
signQualMarTInputNumber = _SignQualMarTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 1),
    _SignQualMarTInputNumber_Type()
)
signQualMarTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    signQualMarTInputNumber.setStatus("current")
_SignQualMarTTestState_Type = TestState
_SignQualMarTTestState_Object = MibTableColumn
signQualMarTTestState = _SignQualMarTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 2),
    _SignQualMarTTestState_Type()
)
signQualMarTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signQualMarTTestState.setStatus("current")


class _SignQualMarTEnable_Type(Enable):
    """Custom type signQualMarTEnable based on Enable"""
    defaultBinValue = "1"


_SignQualMarTEnable_Object = MibTableColumn
signQualMarTEnable = _SignQualMarTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 3),
    _SignQualMarTEnable_Type()
)
signQualMarTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signQualMarTEnable.setStatus("current")
_SignQualMarTCounter_Type = Counter32
_SignQualMarTCounter_Object = MibTableColumn
signQualMarTCounter = _SignQualMarTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 4),
    _SignQualMarTCounter_Type()
)
signQualMarTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signQualMarTCounter.setStatus("current")
_SignQualMarTCounterDiscontinuity_Type = DateAndTime
_SignQualMarTCounterDiscontinuity_Object = MibTableColumn
signQualMarTCounterDiscontinuity = _SignQualMarTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 5),
    _SignQualMarTCounterDiscontinuity_Type()
)
signQualMarTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signQualMarTCounterDiscontinuity.setStatus("current")
_SignQualMarTCounterReset_Type = TruthValue
_SignQualMarTCounterReset_Object = MibTableColumn
signQualMarTCounterReset = _SignQualMarTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 6),
    _SignQualMarTCounterReset_Type()
)
signQualMarTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signQualMarTCounterReset.setStatus("current")
_SignQualMarTLatestError_Type = DateAndTime
_SignQualMarTLatestError_Object = MibTableColumn
signQualMarTLatestError = _SignQualMarTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 7),
    _SignQualMarTLatestError_Type()
)
signQualMarTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signQualMarTLatestError.setStatus("current")
_SignQualMarTActiveTime_Type = ActiveTime
_SignQualMarTActiveTime_Object = MibTableColumn
signQualMarTActiveTime = _SignQualMarTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 3, 1, 8),
    _SignQualMarTActiveTime_Type()
)
signQualMarTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signQualMarTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    signQualMarTActiveTime.setUnits("second")
_ENDCTable_Object = MibTable
eNDCTable = _ENDCTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    eNDCTable.setStatus("current")
_ENDCEntry_Object = MibTableRow
eNDCEntry = _ENDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1)
)
eNDCEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "eNDCInputNumber"),
)
if mibBuilder.loadTexts:
    eNDCEntry.setStatus("current")
_ENDCInputNumber_Type = InputNumber
_ENDCInputNumber_Object = MibTableColumn
eNDCInputNumber = _ENDCInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 1),
    _ENDCInputNumber_Type()
)
eNDCInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eNDCInputNumber.setStatus("current")
_ENDCTestState_Type = TestState
_ENDCTestState_Object = MibTableColumn
eNDCTestState = _ENDCTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 2),
    _ENDCTestState_Type()
)
eNDCTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCTestState.setStatus("current")


class _ENDCEnable_Type(Enable):
    """Custom type eNDCEnable based on Enable"""
    defaultBinValue = "1"


_ENDCEnable_Object = MibTableColumn
eNDCEnable = _ENDCEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 3),
    _ENDCEnable_Type()
)
eNDCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDCEnable.setStatus("current")
_ENDCCounter_Type = Counter32
_ENDCCounter_Object = MibTableColumn
eNDCCounter = _ENDCCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 4),
    _ENDCCounter_Type()
)
eNDCCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCCounter.setStatus("current")
_ENDCCounterDiscontinuity_Type = DateAndTime
_ENDCCounterDiscontinuity_Object = MibTableColumn
eNDCCounterDiscontinuity = _ENDCCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 5),
    _ENDCCounterDiscontinuity_Type()
)
eNDCCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCCounterDiscontinuity.setStatus("current")


class _ENDCCounterReset_Type(TruthValue):
    """Custom type eNDCCounterReset based on TruthValue"""


_ENDCCounterReset_Object = MibTableColumn
eNDCCounterReset = _ENDCCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 6),
    _ENDCCounterReset_Type()
)
eNDCCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDCCounterReset.setStatus("current")
_ENDCLatestError_Type = DateAndTime
_ENDCLatestError_Object = MibTableColumn
eNDCLatestError = _ENDCLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 7),
    _ENDCLatestError_Type()
)
eNDCLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCLatestError.setStatus("current")
_ENDCActiveTime_Type = ActiveTime
_ENDCActiveTime_Object = MibTableColumn
eNDCActiveTime = _ENDCActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 8),
    _ENDCActiveTime_Type()
)
eNDCActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    eNDCActiveTime.setUnits("second")
_ENDCMeasurementState_Type = MeasurementState
_ENDCMeasurementState_Object = MibTableColumn
eNDCMeasurementState = _ENDCMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 9),
    _ENDCMeasurementState_Type()
)
eNDCMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCMeasurementState.setStatus("current")
_ENDCValue_Type = FloatingPoint
_ENDCValue_Object = MibTableColumn
eNDCValue = _ENDCValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 4, 1, 10),
    _ENDCValue_Type()
)
eNDCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDCValue.setStatus("current")
if mibBuilder.loadTexts:
    eNDCValue.setUnits("dB")
_OutBandEmissTable_Object = MibTable
outBandEmissTable = _OutBandEmissTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    outBandEmissTable.setStatus("current")
_OutBandEmissEntry_Object = MibTableRow
outBandEmissEntry = _OutBandEmissEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1)
)
outBandEmissEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "outBandEmissInputNumber"),
)
if mibBuilder.loadTexts:
    outBandEmissEntry.setStatus("current")
_OutBandEmissInputNumber_Type = InputNumber
_OutBandEmissInputNumber_Object = MibTableColumn
outBandEmissInputNumber = _OutBandEmissInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 1),
    _OutBandEmissInputNumber_Type()
)
outBandEmissInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outBandEmissInputNumber.setStatus("current")
_OutBandEmissTestState_Type = TestState
_OutBandEmissTestState_Object = MibTableColumn
outBandEmissTestState = _OutBandEmissTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 2),
    _OutBandEmissTestState_Type()
)
outBandEmissTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandEmissTestState.setStatus("current")


class _OutBandEmissEnable_Type(Enable):
    """Custom type outBandEmissEnable based on Enable"""
    defaultBinValue = "1"


_OutBandEmissEnable_Object = MibTableColumn
outBandEmissEnable = _OutBandEmissEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 3),
    _OutBandEmissEnable_Type()
)
outBandEmissEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outBandEmissEnable.setStatus("current")
_OutBandEmissCounter_Type = Counter32
_OutBandEmissCounter_Object = MibTableColumn
outBandEmissCounter = _OutBandEmissCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 4),
    _OutBandEmissCounter_Type()
)
outBandEmissCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandEmissCounter.setStatus("current")
_OutBandEmissCounterDiscontinuity_Type = DateAndTime
_OutBandEmissCounterDiscontinuity_Object = MibTableColumn
outBandEmissCounterDiscontinuity = _OutBandEmissCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 5),
    _OutBandEmissCounterDiscontinuity_Type()
)
outBandEmissCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandEmissCounterDiscontinuity.setStatus("current")
_OutBandEmissCounterReset_Type = TruthValue
_OutBandEmissCounterReset_Object = MibTableColumn
outBandEmissCounterReset = _OutBandEmissCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 6),
    _OutBandEmissCounterReset_Type()
)
outBandEmissCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outBandEmissCounterReset.setStatus("current")
_OutBandEmissLatestError_Type = DateAndTime
_OutBandEmissLatestError_Object = MibTableColumn
outBandEmissLatestError = _OutBandEmissLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 7),
    _OutBandEmissLatestError_Type()
)
outBandEmissLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandEmissLatestError.setStatus("current")
_OutBandEmissActiveTime_Type = ActiveTime
_OutBandEmissActiveTime_Object = MibTableColumn
outBandEmissActiveTime = _OutBandEmissActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 5, 1, 8),
    _OutBandEmissActiveTime_Type()
)
outBandEmissActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandEmissActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    outBandEmissActiveTime.setUnits("second")
_CablePreferencesTable_Object = MibTable
cablePreferencesTable = _CablePreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100)
)
if mibBuilder.loadTexts:
    cablePreferencesTable.setStatus("current")
_CablePreferencesEntry_Object = MibTableRow
cablePreferencesEntry = _CablePreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1)
)
cablePreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "cablePrefInputNumber"),
)
if mibBuilder.loadTexts:
    cablePreferencesEntry.setStatus("current")
_CablePrefInputNumber_Type = InputNumber
_CablePrefInputNumber_Object = MibTableColumn
cablePrefInputNumber = _CablePrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 1),
    _CablePrefInputNumber_Type()
)
cablePrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cablePrefInputNumber.setStatus("current")
_CablePrefNoiseMarginMin_Type = FloatingPoint
_CablePrefNoiseMarginMin_Object = MibTableColumn
cablePrefNoiseMarginMin = _CablePrefNoiseMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 2),
    _CablePrefNoiseMarginMin_Type()
)
cablePrefNoiseMarginMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefNoiseMarginMin.setStatus("current")
if mibBuilder.loadTexts:
    cablePrefNoiseMarginMin.setUnits("dB")
_CablePrefEstNoiseMarginMin_Type = FloatingPoint
_CablePrefEstNoiseMarginMin_Object = MibTableColumn
cablePrefEstNoiseMarginMin = _CablePrefEstNoiseMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 3),
    _CablePrefEstNoiseMarginMin_Type()
)
cablePrefEstNoiseMarginMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefEstNoiseMarginMin.setStatus("current")
if mibBuilder.loadTexts:
    cablePrefEstNoiseMarginMin.setUnits("dB")
_CablePrefSignQualBoxSize_Type = FloatingPoint
_CablePrefSignQualBoxSize_Object = MibTableColumn
cablePrefSignQualBoxSize = _CablePrefSignQualBoxSize_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 4),
    _CablePrefSignQualBoxSize_Type()
)
cablePrefSignQualBoxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefSignQualBoxSize.setStatus("current")
_CablePrefSignQualPercentMax_Type = Integer32
_CablePrefSignQualPercentMax_Object = MibTableColumn
cablePrefSignQualPercentMax = _CablePrefSignQualPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 5),
    _CablePrefSignQualPercentMax_Type()
)
cablePrefSignQualPercentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefSignQualPercentMax.setStatus("current")


class _CablePrefENDBER_Type(FloatingPoint):
    """Custom type cablePrefENDBER based on FloatingPoint"""
    defaultValue = OctetString("1E-04")


_CablePrefENDBER_Object = MibTableColumn
cablePrefENDBER = _CablePrefENDBER_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 6),
    _CablePrefENDBER_Type()
)
cablePrefENDBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefENDBER.setStatus("current")
_CablePrefENDCtoNSpecified_Type = TruthValue
_CablePrefENDCtoNSpecified_Object = MibTableColumn
cablePrefENDCtoNSpecified = _CablePrefENDCtoNSpecified_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 7),
    _CablePrefENDCtoNSpecified_Type()
)
cablePrefENDCtoNSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefENDCtoNSpecified.setStatus("current")
_CablePrefENDIdeal_Type = FloatingPoint
_CablePrefENDIdeal_Object = MibTableColumn
cablePrefENDIdeal = _CablePrefENDIdeal_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 8),
    _CablePrefENDIdeal_Type()
)
cablePrefENDIdeal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefENDIdeal.setStatus("current")
if mibBuilder.loadTexts:
    cablePrefENDIdeal.setUnits("dB")
_CablePrefENDMax_Type = FloatingPoint
_CablePrefENDMax_Object = MibTableColumn
cablePrefENDMax = _CablePrefENDMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 7, 100, 1, 9),
    _CablePrefENDMax_Type()
)
cablePrefENDMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cablePrefENDMax.setStatus("current")
if mibBuilder.loadTexts:
    cablePrefENDMax.setUnits("dB")
_Tr101290Satellite_ObjectIdentity = ObjectIdentity
tr101290Satellite = _Tr101290Satellite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8)
)
_BerViterbiSTable_Object = MibTable
berViterbiSTable = _BerViterbiSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    berViterbiSTable.setStatus("current")
_BerViterbiSEntry_Object = MibTableRow
berViterbiSEntry = _BerViterbiSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1)
)
berViterbiSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berViterbiSInputNumber"),
)
if mibBuilder.loadTexts:
    berViterbiSEntry.setStatus("current")
_BerViterbiSInputNumber_Type = InputNumber
_BerViterbiSInputNumber_Object = MibTableColumn
berViterbiSInputNumber = _BerViterbiSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 1),
    _BerViterbiSInputNumber_Type()
)
berViterbiSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berViterbiSInputNumber.setStatus("current")
_BerViterbiSTestState_Type = TestState
_BerViterbiSTestState_Object = MibTableColumn
berViterbiSTestState = _BerViterbiSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 2),
    _BerViterbiSTestState_Type()
)
berViterbiSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSTestState.setStatus("current")


class _BerViterbiSEnable_Type(Enable):
    """Custom type berViterbiSEnable based on Enable"""
    defaultBinValue = "1"


_BerViterbiSEnable_Object = MibTableColumn
berViterbiSEnable = _BerViterbiSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 3),
    _BerViterbiSEnable_Type()
)
berViterbiSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiSEnable.setStatus("current")
_BerViterbiSCounter_Type = Counter32
_BerViterbiSCounter_Object = MibTableColumn
berViterbiSCounter = _BerViterbiSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 4),
    _BerViterbiSCounter_Type()
)
berViterbiSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSCounter.setStatus("current")
_BerViterbiSCounterDiscontinuity_Type = DateAndTime
_BerViterbiSCounterDiscontinuity_Object = MibTableColumn
berViterbiSCounterDiscontinuity = _BerViterbiSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 5),
    _BerViterbiSCounterDiscontinuity_Type()
)
berViterbiSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSCounterDiscontinuity.setStatus("current")


class _BerViterbiSCounterReset_Type(TruthValue):
    """Custom type berViterbiSCounterReset based on TruthValue"""


_BerViterbiSCounterReset_Object = MibTableColumn
berViterbiSCounterReset = _BerViterbiSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 6),
    _BerViterbiSCounterReset_Type()
)
berViterbiSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiSCounterReset.setStatus("current")
_BerViterbiSLatestError_Type = DateAndTime
_BerViterbiSLatestError_Object = MibTableColumn
berViterbiSLatestError = _BerViterbiSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 7),
    _BerViterbiSLatestError_Type()
)
berViterbiSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSLatestError.setStatus("current")
_BerViterbiSActiveTime_Type = ActiveTime
_BerViterbiSActiveTime_Object = MibTableColumn
berViterbiSActiveTime = _BerViterbiSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 8),
    _BerViterbiSActiveTime_Type()
)
berViterbiSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    berViterbiSActiveTime.setUnits("second")
_BerViterbiSMeasurementState_Type = MeasurementState
_BerViterbiSMeasurementState_Object = MibTableColumn
berViterbiSMeasurementState = _BerViterbiSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 9),
    _BerViterbiSMeasurementState_Type()
)
berViterbiSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSMeasurementState.setStatus("current")
_BerViterbiSIValue_Type = FloatingPoint
_BerViterbiSIValue_Object = MibTableColumn
berViterbiSIValue = _BerViterbiSIValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 10),
    _BerViterbiSIValue_Type()
)
berViterbiSIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSIValue.setStatus("current")
_BerViterbiSQValue_Type = FloatingPoint
_BerViterbiSQValue_Object = MibTableColumn
berViterbiSQValue = _BerViterbiSQValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 11),
    _BerViterbiSQValue_Type()
)
berViterbiSQValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSQValue.setStatus("current")
_BerViterbiSMeasurementMethod_Type = BERMeasurementMethod
_BerViterbiSMeasurementMethod_Object = MibTableColumn
berViterbiSMeasurementMethod = _BerViterbiSMeasurementMethod_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 1, 1, 12),
    _BerViterbiSMeasurementMethod_Type()
)
berViterbiSMeasurementMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiSMeasurementMethod.setStatus("current")
_IfSpectrumTable_Object = MibTable
ifSpectrumTable = _IfSpectrumTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ifSpectrumTable.setStatus("current")
_IfSpectrumEntry_Object = MibTableRow
ifSpectrumEntry = _IfSpectrumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1)
)
ifSpectrumEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "ifSpectrumInputNumber"),
)
if mibBuilder.loadTexts:
    ifSpectrumEntry.setStatus("current")
_IfSpectrumInputNumber_Type = InputNumber
_IfSpectrumInputNumber_Object = MibTableColumn
ifSpectrumInputNumber = _IfSpectrumInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 1),
    _IfSpectrumInputNumber_Type()
)
ifSpectrumInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifSpectrumInputNumber.setStatus("current")
_IfSpectrumTestState_Type = TestState
_IfSpectrumTestState_Object = MibTableColumn
ifSpectrumTestState = _IfSpectrumTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 2),
    _IfSpectrumTestState_Type()
)
ifSpectrumTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpectrumTestState.setStatus("current")


class _IfSpectrumEnable_Type(Enable):
    """Custom type ifSpectrumEnable based on Enable"""
    defaultBinValue = "1"


_IfSpectrumEnable_Object = MibTableColumn
ifSpectrumEnable = _IfSpectrumEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 3),
    _IfSpectrumEnable_Type()
)
ifSpectrumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSpectrumEnable.setStatus("current")
_IfSpectrumCounter_Type = Counter32
_IfSpectrumCounter_Object = MibTableColumn
ifSpectrumCounter = _IfSpectrumCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 4),
    _IfSpectrumCounter_Type()
)
ifSpectrumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpectrumCounter.setStatus("current")
_IfSpectrumCounterDiscontinuity_Type = DateAndTime
_IfSpectrumCounterDiscontinuity_Object = MibTableColumn
ifSpectrumCounterDiscontinuity = _IfSpectrumCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 5),
    _IfSpectrumCounterDiscontinuity_Type()
)
ifSpectrumCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpectrumCounterDiscontinuity.setStatus("current")


class _IfSpectrumCounterReset_Type(TruthValue):
    """Custom type ifSpectrumCounterReset based on TruthValue"""


_IfSpectrumCounterReset_Object = MibTableColumn
ifSpectrumCounterReset = _IfSpectrumCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 6),
    _IfSpectrumCounterReset_Type()
)
ifSpectrumCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSpectrumCounterReset.setStatus("current")
_IfSpectrumLatestError_Type = DateAndTime
_IfSpectrumLatestError_Object = MibTableColumn
ifSpectrumLatestError = _IfSpectrumLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 7),
    _IfSpectrumLatestError_Type()
)
ifSpectrumLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpectrumLatestError.setStatus("current")
_IfSpectrumActiveTime_Type = ActiveTime
_IfSpectrumActiveTime_Object = MibTableColumn
ifSpectrumActiveTime = _IfSpectrumActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 2, 1, 8),
    _IfSpectrumActiveTime_Type()
)
ifSpectrumActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpectrumActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    ifSpectrumActiveTime.setUnits("second")
_SatellitePreferencesTable_Object = MibTable
satellitePreferencesTable = _SatellitePreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 100)
)
if mibBuilder.loadTexts:
    satellitePreferencesTable.setStatus("current")
_SatellitePreferencesEntry_Object = MibTableRow
satellitePreferencesEntry = _SatellitePreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 100, 1)
)
satellitePreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "satellitePrefInputNumber"),
)
if mibBuilder.loadTexts:
    satellitePreferencesEntry.setStatus("current")
_SatellitePrefInputNumber_Type = InputNumber
_SatellitePrefInputNumber_Object = MibTableColumn
satellitePrefInputNumber = _SatellitePrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 100, 1, 1),
    _SatellitePrefInputNumber_Type()
)
satellitePrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satellitePrefInputNumber.setStatus("current")
_SatellitePrefBERMax_Type = FloatingPoint
_SatellitePrefBERMax_Object = MibTableColumn
satellitePrefBERMax = _SatellitePrefBERMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 8, 100, 1, 2),
    _SatellitePrefBERMax_Type()
)
satellitePrefBERMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satellitePrefBERMax.setStatus("current")
_Tr101290Terrestrial_ObjectIdentity = ObjectIdentity
tr101290Terrestrial = _Tr101290Terrestrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9)
)
_RfTerr_ObjectIdentity = ObjectIdentity
rfTerr = _RfTerr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1)
)
_RfAccuracyTable_Object = MibTable
rfAccuracyTable = _RfAccuracyTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rfAccuracyTable.setStatus("current")
_RfAccuracyEntry_Object = MibTableRow
rfAccuracyEntry = _RfAccuracyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1)
)
rfAccuracyEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfAccuracyInputNumber"),
)
if mibBuilder.loadTexts:
    rfAccuracyEntry.setStatus("current")
_RfAccuracyInputNumber_Type = InputNumber
_RfAccuracyInputNumber_Object = MibTableColumn
rfAccuracyInputNumber = _RfAccuracyInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 1),
    _RfAccuracyInputNumber_Type()
)
rfAccuracyInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfAccuracyInputNumber.setStatus("current")
_RfAccuracyTestState_Type = TestState
_RfAccuracyTestState_Object = MibTableColumn
rfAccuracyTestState = _RfAccuracyTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 2),
    _RfAccuracyTestState_Type()
)
rfAccuracyTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyTestState.setStatus("current")


class _RfAccuracyEnable_Type(Enable):
    """Custom type rfAccuracyEnable based on Enable"""
    defaultBinValue = "1"


_RfAccuracyEnable_Object = MibTableColumn
rfAccuracyEnable = _RfAccuracyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 3),
    _RfAccuracyEnable_Type()
)
rfAccuracyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfAccuracyEnable.setStatus("current")
_RfAccuracyCounter_Type = Counter32
_RfAccuracyCounter_Object = MibTableColumn
rfAccuracyCounter = _RfAccuracyCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 4),
    _RfAccuracyCounter_Type()
)
rfAccuracyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyCounter.setStatus("current")
_RfAccuracyCounterDiscontinuity_Type = DateAndTime
_RfAccuracyCounterDiscontinuity_Object = MibTableColumn
rfAccuracyCounterDiscontinuity = _RfAccuracyCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 5),
    _RfAccuracyCounterDiscontinuity_Type()
)
rfAccuracyCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyCounterDiscontinuity.setStatus("current")


class _RfAccuracyCounterReset_Type(TruthValue):
    """Custom type rfAccuracyCounterReset based on TruthValue"""


_RfAccuracyCounterReset_Object = MibTableColumn
rfAccuracyCounterReset = _RfAccuracyCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 6),
    _RfAccuracyCounterReset_Type()
)
rfAccuracyCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfAccuracyCounterReset.setStatus("current")
_RfAccuracyLatestError_Type = DateAndTime
_RfAccuracyLatestError_Object = MibTableColumn
rfAccuracyLatestError = _RfAccuracyLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 7),
    _RfAccuracyLatestError_Type()
)
rfAccuracyLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyLatestError.setStatus("current")
_RfAccuracyActiveTime_Type = ActiveTime
_RfAccuracyActiveTime_Object = MibTableColumn
rfAccuracyActiveTime = _RfAccuracyActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 8),
    _RfAccuracyActiveTime_Type()
)
rfAccuracyActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rfAccuracyActiveTime.setUnits("second")
_RfAccuracyMeasurementState_Type = MeasurementState
_RfAccuracyMeasurementState_Object = MibTableColumn
rfAccuracyMeasurementState = _RfAccuracyMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 9),
    _RfAccuracyMeasurementState_Type()
)
rfAccuracyMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyMeasurementState.setStatus("current")
_RfAccuracyValue_Type = FloatingPoint
_RfAccuracyValue_Object = MibTableColumn
rfAccuracyValue = _RfAccuracyValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 1, 1, 10),
    _RfAccuracyValue_Type()
)
rfAccuracyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAccuracyValue.setStatus("current")
if mibBuilder.loadTexts:
    rfAccuracyValue.setUnits("Hz")
_RfChannelWidthTable_Object = MibTable
rfChannelWidthTable = _RfChannelWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    rfChannelWidthTable.setStatus("current")
_RfChannelWidthEntry_Object = MibTableRow
rfChannelWidthEntry = _RfChannelWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1)
)
rfChannelWidthEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfChannelWidthInputNumber"),
)
if mibBuilder.loadTexts:
    rfChannelWidthEntry.setStatus("current")
_RfChannelWidthInputNumber_Type = InputNumber
_RfChannelWidthInputNumber_Object = MibTableColumn
rfChannelWidthInputNumber = _RfChannelWidthInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 1),
    _RfChannelWidthInputNumber_Type()
)
rfChannelWidthInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfChannelWidthInputNumber.setStatus("current")
_RfChannelWidthTestState_Type = TestState
_RfChannelWidthTestState_Object = MibTableColumn
rfChannelWidthTestState = _RfChannelWidthTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 2),
    _RfChannelWidthTestState_Type()
)
rfChannelWidthTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthTestState.setStatus("current")


class _RfChannelWidthEnable_Type(Enable):
    """Custom type rfChannelWidthEnable based on Enable"""
    defaultBinValue = "1"


_RfChannelWidthEnable_Object = MibTableColumn
rfChannelWidthEnable = _RfChannelWidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 3),
    _RfChannelWidthEnable_Type()
)
rfChannelWidthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfChannelWidthEnable.setStatus("current")
_RfChannelWidthCounter_Type = Counter32
_RfChannelWidthCounter_Object = MibTableColumn
rfChannelWidthCounter = _RfChannelWidthCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 4),
    _RfChannelWidthCounter_Type()
)
rfChannelWidthCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthCounter.setStatus("current")
_RfChannelWidthCounterDiscontinuity_Type = DateAndTime
_RfChannelWidthCounterDiscontinuity_Object = MibTableColumn
rfChannelWidthCounterDiscontinuity = _RfChannelWidthCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 5),
    _RfChannelWidthCounterDiscontinuity_Type()
)
rfChannelWidthCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthCounterDiscontinuity.setStatus("current")


class _RfChannelWidthCounterReset_Type(TruthValue):
    """Custom type rfChannelWidthCounterReset based on TruthValue"""


_RfChannelWidthCounterReset_Object = MibTableColumn
rfChannelWidthCounterReset = _RfChannelWidthCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 6),
    _RfChannelWidthCounterReset_Type()
)
rfChannelWidthCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfChannelWidthCounterReset.setStatus("current")
_RfChannelWidthLatestError_Type = DateAndTime
_RfChannelWidthLatestError_Object = MibTableColumn
rfChannelWidthLatestError = _RfChannelWidthLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 7),
    _RfChannelWidthLatestError_Type()
)
rfChannelWidthLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthLatestError.setStatus("current")
_RfChannelWidthActiveTime_Type = ActiveTime
_RfChannelWidthActiveTime_Object = MibTableColumn
rfChannelWidthActiveTime = _RfChannelWidthActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 8),
    _RfChannelWidthActiveTime_Type()
)
rfChannelWidthActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rfChannelWidthActiveTime.setUnits("second")
_RfChannelWidthMeasurementState_Type = MeasurementState
_RfChannelWidthMeasurementState_Object = MibTableColumn
rfChannelWidthMeasurementState = _RfChannelWidthMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 9),
    _RfChannelWidthMeasurementState_Type()
)
rfChannelWidthMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthMeasurementState.setStatus("current")
_RfChannelWidthValue_Type = FloatingPoint
_RfChannelWidthValue_Object = MibTableColumn
rfChannelWidthValue = _RfChannelWidthValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 2, 1, 10),
    _RfChannelWidthValue_Type()
)
rfChannelWidthValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfChannelWidthValue.setStatus("current")
if mibBuilder.loadTexts:
    rfChannelWidthValue.setUnits("Hz")
_SymbolLengthTable_Object = MibTable
symbolLengthTable = _SymbolLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    symbolLengthTable.setStatus("current")
_SymbolLengthEntry_Object = MibTableRow
symbolLengthEntry = _SymbolLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1)
)
symbolLengthEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "symbolLengthInputNumber"),
)
if mibBuilder.loadTexts:
    symbolLengthEntry.setStatus("current")
_SymbolLengthInputNumber_Type = InputNumber
_SymbolLengthInputNumber_Object = MibTableColumn
symbolLengthInputNumber = _SymbolLengthInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 1),
    _SymbolLengthInputNumber_Type()
)
symbolLengthInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    symbolLengthInputNumber.setStatus("current")
_SymbolLengthTestState_Type = TestState
_SymbolLengthTestState_Object = MibTableColumn
symbolLengthTestState = _SymbolLengthTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 2),
    _SymbolLengthTestState_Type()
)
symbolLengthTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthTestState.setStatus("current")


class _SymbolLengthEnable_Type(Enable):
    """Custom type symbolLengthEnable based on Enable"""
    defaultBinValue = "1"


_SymbolLengthEnable_Object = MibTableColumn
symbolLengthEnable = _SymbolLengthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 3),
    _SymbolLengthEnable_Type()
)
symbolLengthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symbolLengthEnable.setStatus("current")
_SymbolLengthCounter_Type = Counter32
_SymbolLengthCounter_Object = MibTableColumn
symbolLengthCounter = _SymbolLengthCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 4),
    _SymbolLengthCounter_Type()
)
symbolLengthCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthCounter.setStatus("current")
_SymbolLengthCounterDiscontinuity_Type = DateAndTime
_SymbolLengthCounterDiscontinuity_Object = MibTableColumn
symbolLengthCounterDiscontinuity = _SymbolLengthCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 5),
    _SymbolLengthCounterDiscontinuity_Type()
)
symbolLengthCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthCounterDiscontinuity.setStatus("current")


class _SymbolLengthCounterReset_Type(TruthValue):
    """Custom type symbolLengthCounterReset based on TruthValue"""


_SymbolLengthCounterReset_Object = MibTableColumn
symbolLengthCounterReset = _SymbolLengthCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 6),
    _SymbolLengthCounterReset_Type()
)
symbolLengthCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symbolLengthCounterReset.setStatus("current")
_SymbolLengthLatestError_Type = DateAndTime
_SymbolLengthLatestError_Object = MibTableColumn
symbolLengthLatestError = _SymbolLengthLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 7),
    _SymbolLengthLatestError_Type()
)
symbolLengthLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthLatestError.setStatus("current")
_SymbolLengthActiveTime_Type = ActiveTime
_SymbolLengthActiveTime_Object = MibTableColumn
symbolLengthActiveTime = _SymbolLengthActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 8),
    _SymbolLengthActiveTime_Type()
)
symbolLengthActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    symbolLengthActiveTime.setUnits("second")
_SymbolLengthMeasurementState_Type = MeasurementState
_SymbolLengthMeasurementState_Object = MibTableColumn
symbolLengthMeasurementState = _SymbolLengthMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 9),
    _SymbolLengthMeasurementState_Type()
)
symbolLengthMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthMeasurementState.setStatus("current")
_SymbolLengthValue_Type = FloatingPoint
_SymbolLengthValue_Object = MibTableColumn
symbolLengthValue = _SymbolLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 1, 3, 1, 10),
    _SymbolLengthValue_Type()
)
symbolLengthValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolLengthValue.setStatus("current")
if mibBuilder.loadTexts:
    symbolLengthValue.setUnits("microsecond")
_RfIfPowerTable_Object = MibTable
rfIfPowerTable = _RfIfPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5)
)
if mibBuilder.loadTexts:
    rfIfPowerTable.setStatus("current")
_RfIfPowerEntry_Object = MibTableRow
rfIfPowerEntry = _RfIfPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1)
)
rfIfPowerEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfIfPowerInputNumber"),
)
if mibBuilder.loadTexts:
    rfIfPowerEntry.setStatus("current")
_RfIfPowerInputNumber_Type = InputNumber
_RfIfPowerInputNumber_Object = MibTableColumn
rfIfPowerInputNumber = _RfIfPowerInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 1),
    _RfIfPowerInputNumber_Type()
)
rfIfPowerInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIfPowerInputNumber.setStatus("current")
_RfIfPowerTestState_Type = TestState
_RfIfPowerTestState_Object = MibTableColumn
rfIfPowerTestState = _RfIfPowerTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 2),
    _RfIfPowerTestState_Type()
)
rfIfPowerTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerTestState.setStatus("current")


class _RfIfPowerEnable_Type(Enable):
    """Custom type rfIfPowerEnable based on Enable"""
    defaultBinValue = "1"


_RfIfPowerEnable_Object = MibTableColumn
rfIfPowerEnable = _RfIfPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 3),
    _RfIfPowerEnable_Type()
)
rfIfPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIfPowerEnable.setStatus("current")
_RfIfPowerCounter_Type = Counter32
_RfIfPowerCounter_Object = MibTableColumn
rfIfPowerCounter = _RfIfPowerCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 4),
    _RfIfPowerCounter_Type()
)
rfIfPowerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerCounter.setStatus("current")
_RfIfPowerCounterDiscontinuity_Type = DateAndTime
_RfIfPowerCounterDiscontinuity_Object = MibTableColumn
rfIfPowerCounterDiscontinuity = _RfIfPowerCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 5),
    _RfIfPowerCounterDiscontinuity_Type()
)
rfIfPowerCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerCounterDiscontinuity.setStatus("current")


class _RfIfPowerCounterReset_Type(TruthValue):
    """Custom type rfIfPowerCounterReset based on TruthValue"""


_RfIfPowerCounterReset_Object = MibTableColumn
rfIfPowerCounterReset = _RfIfPowerCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 6),
    _RfIfPowerCounterReset_Type()
)
rfIfPowerCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIfPowerCounterReset.setStatus("current")
_RfIfPowerLatestError_Type = DateAndTime
_RfIfPowerLatestError_Object = MibTableColumn
rfIfPowerLatestError = _RfIfPowerLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 7),
    _RfIfPowerLatestError_Type()
)
rfIfPowerLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerLatestError.setStatus("current")
_RfIfPowerActiveTime_Type = ActiveTime
_RfIfPowerActiveTime_Object = MibTableColumn
rfIfPowerActiveTime = _RfIfPowerActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 8),
    _RfIfPowerActiveTime_Type()
)
rfIfPowerActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rfIfPowerActiveTime.setUnits("second")
_RfIfPowerMeasurementState_Type = MeasurementState
_RfIfPowerMeasurementState_Object = MibTableColumn
rfIfPowerMeasurementState = _RfIfPowerMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 9),
    _RfIfPowerMeasurementState_Type()
)
rfIfPowerMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerMeasurementState.setStatus("current")
_RfIfPowerValue_Type = FloatingPoint
_RfIfPowerValue_Object = MibTableColumn
rfIfPowerValue = _RfIfPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 5, 1, 10),
    _RfIfPowerValue_Type()
)
rfIfPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    rfIfPowerValue.setUnits("dBm")
_RfIfSpectrumTable_Object = MibTable
rfIfSpectrumTable = _RfIfSpectrumTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7)
)
if mibBuilder.loadTexts:
    rfIfSpectrumTable.setStatus("current")
_RfIfSpectrumEntry_Object = MibTableRow
rfIfSpectrumEntry = _RfIfSpectrumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1)
)
rfIfSpectrumEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "rfIfSpectrumInputNumber"),
)
if mibBuilder.loadTexts:
    rfIfSpectrumEntry.setStatus("current")
_RfIfSpectrumInputNumber_Type = InputNumber
_RfIfSpectrumInputNumber_Object = MibTableColumn
rfIfSpectrumInputNumber = _RfIfSpectrumInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 1),
    _RfIfSpectrumInputNumber_Type()
)
rfIfSpectrumInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIfSpectrumInputNumber.setStatus("current")
_RfIfSpectrumTestState_Type = TestState
_RfIfSpectrumTestState_Object = MibTableColumn
rfIfSpectrumTestState = _RfIfSpectrumTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 2),
    _RfIfSpectrumTestState_Type()
)
rfIfSpectrumTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfSpectrumTestState.setStatus("current")


class _RfIfSpectrumEnable_Type(Enable):
    """Custom type rfIfSpectrumEnable based on Enable"""
    defaultBinValue = "1"


_RfIfSpectrumEnable_Object = MibTableColumn
rfIfSpectrumEnable = _RfIfSpectrumEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 3),
    _RfIfSpectrumEnable_Type()
)
rfIfSpectrumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIfSpectrumEnable.setStatus("current")
_RfIfSpectrumCounter_Type = Counter32
_RfIfSpectrumCounter_Object = MibTableColumn
rfIfSpectrumCounter = _RfIfSpectrumCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 4),
    _RfIfSpectrumCounter_Type()
)
rfIfSpectrumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfSpectrumCounter.setStatus("current")
_RfIfSpectrumCounterDiscontinuity_Type = DateAndTime
_RfIfSpectrumCounterDiscontinuity_Object = MibTableColumn
rfIfSpectrumCounterDiscontinuity = _RfIfSpectrumCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 5),
    _RfIfSpectrumCounterDiscontinuity_Type()
)
rfIfSpectrumCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfSpectrumCounterDiscontinuity.setStatus("current")


class _RfIfSpectrumCounterReset_Type(TruthValue):
    """Custom type rfIfSpectrumCounterReset based on TruthValue"""


_RfIfSpectrumCounterReset_Object = MibTableColumn
rfIfSpectrumCounterReset = _RfIfSpectrumCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 6),
    _RfIfSpectrumCounterReset_Type()
)
rfIfSpectrumCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfIfSpectrumCounterReset.setStatus("current")
_RfIfSpectrumLatestError_Type = DateAndTime
_RfIfSpectrumLatestError_Object = MibTableColumn
rfIfSpectrumLatestError = _RfIfSpectrumLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 7),
    _RfIfSpectrumLatestError_Type()
)
rfIfSpectrumLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfSpectrumLatestError.setStatus("current")
_RfIfSpectrumActiveTime_Type = ActiveTime
_RfIfSpectrumActiveTime_Object = MibTableColumn
rfIfSpectrumActiveTime = _RfIfSpectrumActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 7, 1, 8),
    _RfIfSpectrumActiveTime_Type()
)
rfIfSpectrumActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfIfSpectrumActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    rfIfSpectrumActiveTime.setUnits("second")
_ENDT_ObjectIdentity = ObjectIdentity
eNDT = _ENDT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9)
)
_ENDTTable_Object = MibTable
eNDTTable = _ENDTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1)
)
if mibBuilder.loadTexts:
    eNDTTable.setStatus("current")
_ENDTEntry_Object = MibTableRow
eNDTEntry = _ENDTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1)
)
eNDTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "eNDTInputNumber"),
)
if mibBuilder.loadTexts:
    eNDTEntry.setStatus("current")
_ENDTInputNumber_Type = InputNumber
_ENDTInputNumber_Object = MibTableColumn
eNDTInputNumber = _ENDTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 1),
    _ENDTInputNumber_Type()
)
eNDTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eNDTInputNumber.setStatus("current")
_ENDTTestState_Type = TestState
_ENDTTestState_Object = MibTableColumn
eNDTTestState = _ENDTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 2),
    _ENDTTestState_Type()
)
eNDTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTTestState.setStatus("current")


class _ENDTEnable_Type(Enable):
    """Custom type eNDTEnable based on Enable"""
    defaultBinValue = "1"


_ENDTEnable_Object = MibTableColumn
eNDTEnable = _ENDTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 3),
    _ENDTEnable_Type()
)
eNDTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDTEnable.setStatus("current")
_ENDTCounter_Type = Counter32
_ENDTCounter_Object = MibTableColumn
eNDTCounter = _ENDTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 4),
    _ENDTCounter_Type()
)
eNDTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTCounter.setStatus("current")
_ENDTCounterDiscontinuity_Type = DateAndTime
_ENDTCounterDiscontinuity_Object = MibTableColumn
eNDTCounterDiscontinuity = _ENDTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 5),
    _ENDTCounterDiscontinuity_Type()
)
eNDTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTCounterDiscontinuity.setStatus("current")


class _ENDTCounterReset_Type(TruthValue):
    """Custom type eNDTCounterReset based on TruthValue"""


_ENDTCounterReset_Object = MibTableColumn
eNDTCounterReset = _ENDTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 6),
    _ENDTCounterReset_Type()
)
eNDTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDTCounterReset.setStatus("current")
_ENDTLatestError_Type = DateAndTime
_ENDTLatestError_Object = MibTableColumn
eNDTLatestError = _ENDTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 7),
    _ENDTLatestError_Type()
)
eNDTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLatestError.setStatus("current")
_ENDTActiveTime_Type = ActiveTime
_ENDTActiveTime_Object = MibTableColumn
eNDTActiveTime = _ENDTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 8),
    _ENDTActiveTime_Type()
)
eNDTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    eNDTActiveTime.setUnits("second")
_ENDTMeasurementState_Type = MeasurementState
_ENDTMeasurementState_Object = MibTableColumn
eNDTMeasurementState = _ENDTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 9),
    _ENDTMeasurementState_Type()
)
eNDTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTMeasurementState.setStatus("current")
_ENDTValue_Type = FloatingPoint
_ENDTValue_Object = MibTableColumn
eNDTValue = _ENDTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 1, 1, 10),
    _ENDTValue_Type()
)
eNDTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTValue.setStatus("current")
if mibBuilder.loadTexts:
    eNDTValue.setUnits("dB")
_ENFTTable_Object = MibTable
eNFTTable = _ENFTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2)
)
if mibBuilder.loadTexts:
    eNFTTable.setStatus("current")
_ENFTEntry_Object = MibTableRow
eNFTEntry = _ENFTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1)
)
eNFTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "eNFTInputNumber"),
)
if mibBuilder.loadTexts:
    eNFTEntry.setStatus("current")
_ENFTInputNumber_Type = InputNumber
_ENFTInputNumber_Object = MibTableColumn
eNFTInputNumber = _ENFTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 1),
    _ENFTInputNumber_Type()
)
eNFTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eNFTInputNumber.setStatus("current")
_ENFTTestState_Type = TestState
_ENFTTestState_Object = MibTableColumn
eNFTTestState = _ENFTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 2),
    _ENFTTestState_Type()
)
eNFTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTTestState.setStatus("current")


class _ENFTEnable_Type(Enable):
    """Custom type eNFTEnable based on Enable"""
    defaultBinValue = "1"


_ENFTEnable_Object = MibTableColumn
eNFTEnable = _ENFTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 3),
    _ENFTEnable_Type()
)
eNFTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNFTEnable.setStatus("current")
_ENFTCounter_Type = Counter32
_ENFTCounter_Object = MibTableColumn
eNFTCounter = _ENFTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 4),
    _ENFTCounter_Type()
)
eNFTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTCounter.setStatus("current")
_ENFTCounterDiscontinuity_Type = DateAndTime
_ENFTCounterDiscontinuity_Object = MibTableColumn
eNFTCounterDiscontinuity = _ENFTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 5),
    _ENFTCounterDiscontinuity_Type()
)
eNFTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTCounterDiscontinuity.setStatus("current")


class _ENFTCounterReset_Type(TruthValue):
    """Custom type eNFTCounterReset based on TruthValue"""


_ENFTCounterReset_Object = MibTableColumn
eNFTCounterReset = _ENFTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 6),
    _ENFTCounterReset_Type()
)
eNFTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNFTCounterReset.setStatus("current")
_ENFTLatestError_Type = DateAndTime
_ENFTLatestError_Object = MibTableColumn
eNFTLatestError = _ENFTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 7),
    _ENFTLatestError_Type()
)
eNFTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLatestError.setStatus("current")
_ENFTActiveTime_Type = ActiveTime
_ENFTActiveTime_Object = MibTableColumn
eNFTActiveTime = _ENFTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 8),
    _ENFTActiveTime_Type()
)
eNFTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    eNFTActiveTime.setUnits("second")
_ENFTMeasurementState_Type = MeasurementState
_ENFTMeasurementState_Object = MibTableColumn
eNFTMeasurementState = _ENFTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 9),
    _ENFTMeasurementState_Type()
)
eNFTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTMeasurementState.setStatus("current")
_ENFTValue_Type = FloatingPoint
_ENFTValue_Object = MibTableColumn
eNFTValue = _ENFTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 2, 1, 10),
    _ENFTValue_Type()
)
eNFTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTValue.setStatus("current")
if mibBuilder.loadTexts:
    eNFTValue.setUnits("dB")
_ENDTLPTable_Object = MibTable
eNDTLPTable = _ENDTLPTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3)
)
if mibBuilder.loadTexts:
    eNDTLPTable.setStatus("current")
_ENDTLPEntry_Object = MibTableRow
eNDTLPEntry = _ENDTLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1)
)
eNDTLPEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "eNDTLPInputNumber"),
)
if mibBuilder.loadTexts:
    eNDTLPEntry.setStatus("current")
_ENDTLPInputNumber_Type = InputNumber
_ENDTLPInputNumber_Object = MibTableColumn
eNDTLPInputNumber = _ENDTLPInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 1),
    _ENDTLPInputNumber_Type()
)
eNDTLPInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eNDTLPInputNumber.setStatus("current")
_ENDTLPTestState_Type = TestState
_ENDTLPTestState_Object = MibTableColumn
eNDTLPTestState = _ENDTLPTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 2),
    _ENDTLPTestState_Type()
)
eNDTLPTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPTestState.setStatus("current")


class _ENDTLPEnable_Type(Enable):
    """Custom type eNDTLPEnable based on Enable"""
    defaultBinValue = "1"


_ENDTLPEnable_Object = MibTableColumn
eNDTLPEnable = _ENDTLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 3),
    _ENDTLPEnable_Type()
)
eNDTLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDTLPEnable.setStatus("current")
_ENDTLPCounter_Type = Counter32
_ENDTLPCounter_Object = MibTableColumn
eNDTLPCounter = _ENDTLPCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 4),
    _ENDTLPCounter_Type()
)
eNDTLPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPCounter.setStatus("current")
_ENDTLPCounterDiscontinuity_Type = DateAndTime
_ENDTLPCounterDiscontinuity_Object = MibTableColumn
eNDTLPCounterDiscontinuity = _ENDTLPCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 5),
    _ENDTLPCounterDiscontinuity_Type()
)
eNDTLPCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPCounterDiscontinuity.setStatus("current")
_ENDTLPCounterReset_Type = TruthValue
_ENDTLPCounterReset_Object = MibTableColumn
eNDTLPCounterReset = _ENDTLPCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 6),
    _ENDTLPCounterReset_Type()
)
eNDTLPCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNDTLPCounterReset.setStatus("current")
_ENDTLPLatestError_Type = DateAndTime
_ENDTLPLatestError_Object = MibTableColumn
eNDTLPLatestError = _ENDTLPLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 7),
    _ENDTLPLatestError_Type()
)
eNDTLPLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPLatestError.setStatus("current")
_ENDTLPActiveTime_Type = ActiveTime
_ENDTLPActiveTime_Object = MibTableColumn
eNDTLPActiveTime = _ENDTLPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 8),
    _ENDTLPActiveTime_Type()
)
eNDTLPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPActiveTime.setStatus("current")
_ENDTLPMeasurementState_Type = MeasurementState
_ENDTLPMeasurementState_Object = MibTableColumn
eNDTLPMeasurementState = _ENDTLPMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 9),
    _ENDTLPMeasurementState_Type()
)
eNDTLPMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPMeasurementState.setStatus("current")
_ENDTLPValue_Type = FloatingPoint
_ENDTLPValue_Object = MibTableColumn
eNDTLPValue = _ENDTLPValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 3, 1, 10),
    _ENDTLPValue_Type()
)
eNDTLPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNDTLPValue.setStatus("current")
if mibBuilder.loadTexts:
    eNDTLPValue.setUnits("dB")
_ENFTLPTable_Object = MibTable
eNFTLPTable = _ENFTLPTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4)
)
if mibBuilder.loadTexts:
    eNFTLPTable.setStatus("current")
_ENFTLPEntry_Object = MibTableRow
eNFTLPEntry = _ENFTLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1)
)
eNFTLPEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "eNDTLPInputNumber"),
)
if mibBuilder.loadTexts:
    eNFTLPEntry.setStatus("current")
_ENFTLPInputNumber_Type = InputNumber
_ENFTLPInputNumber_Object = MibTableColumn
eNFTLPInputNumber = _ENFTLPInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 1),
    _ENFTLPInputNumber_Type()
)
eNFTLPInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eNFTLPInputNumber.setStatus("current")
_ENFTLPTestState_Type = TestState
_ENFTLPTestState_Object = MibTableColumn
eNFTLPTestState = _ENFTLPTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 2),
    _ENFTLPTestState_Type()
)
eNFTLPTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPTestState.setStatus("current")


class _ENFTLPEnable_Type(Enable):
    """Custom type eNFTLPEnable based on Enable"""
    defaultBinValue = "1"


_ENFTLPEnable_Object = MibTableColumn
eNFTLPEnable = _ENFTLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 3),
    _ENFTLPEnable_Type()
)
eNFTLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNFTLPEnable.setStatus("current")
_ENFTLPCounter_Type = Counter32
_ENFTLPCounter_Object = MibTableColumn
eNFTLPCounter = _ENFTLPCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 4),
    _ENFTLPCounter_Type()
)
eNFTLPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPCounter.setStatus("current")
_ENFTLPCounterDiscontinuity_Type = DateAndTime
_ENFTLPCounterDiscontinuity_Object = MibTableColumn
eNFTLPCounterDiscontinuity = _ENFTLPCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 5),
    _ENFTLPCounterDiscontinuity_Type()
)
eNFTLPCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPCounterDiscontinuity.setStatus("current")
_ENFTLPCounterReset_Type = TruthValue
_ENFTLPCounterReset_Object = MibTableColumn
eNFTLPCounterReset = _ENFTLPCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 6),
    _ENFTLPCounterReset_Type()
)
eNFTLPCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNFTLPCounterReset.setStatus("current")
_ENFTLPLatestError_Type = DateAndTime
_ENFTLPLatestError_Object = MibTableColumn
eNFTLPLatestError = _ENFTLPLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 7),
    _ENFTLPLatestError_Type()
)
eNFTLPLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPLatestError.setStatus("current")
_ENFTLPActiveTime_Type = ActiveTime
_ENFTLPActiveTime_Object = MibTableColumn
eNFTLPActiveTime = _ENFTLPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 8),
    _ENFTLPActiveTime_Type()
)
eNFTLPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPActiveTime.setStatus("current")
_ENFTLPMeasurementState_Type = MeasurementState
_ENFTLPMeasurementState_Object = MibTableColumn
eNFTLPMeasurementState = _ENFTLPMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 9),
    _ENFTLPMeasurementState_Type()
)
eNFTLPMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPMeasurementState.setStatus("current")
_ENFTLPValue_Type = FloatingPoint
_ENFTLPValue_Object = MibTableColumn
eNFTLPValue = _ENFTLPValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 9, 4, 1, 10),
    _ENFTLPValue_Type()
)
eNFTLPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNFTLPValue.setStatus("current")
if mibBuilder.loadTexts:
    eNFTLPValue.setUnits("dB")
_LinearityTable_Object = MibTable
linearityTable = _LinearityTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10)
)
if mibBuilder.loadTexts:
    linearityTable.setStatus("current")
_LinearityEntry_Object = MibTableRow
linearityEntry = _LinearityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1)
)
linearityEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "linearityInputNumber"),
)
if mibBuilder.loadTexts:
    linearityEntry.setStatus("current")
_LinearityInputNumber_Type = InputNumber
_LinearityInputNumber_Object = MibTableColumn
linearityInputNumber = _LinearityInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 1),
    _LinearityInputNumber_Type()
)
linearityInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linearityInputNumber.setStatus("current")
_LinearityTestState_Type = TestState
_LinearityTestState_Object = MibTableColumn
linearityTestState = _LinearityTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 2),
    _LinearityTestState_Type()
)
linearityTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityTestState.setStatus("current")


class _LinearityEnable_Type(Enable):
    """Custom type linearityEnable based on Enable"""
    defaultBinValue = "1"


_LinearityEnable_Object = MibTableColumn
linearityEnable = _LinearityEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 3),
    _LinearityEnable_Type()
)
linearityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linearityEnable.setStatus("current")
_LinearityCounter_Type = Counter32
_LinearityCounter_Object = MibTableColumn
linearityCounter = _LinearityCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 4),
    _LinearityCounter_Type()
)
linearityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityCounter.setStatus("current")
_LinearityCounterDiscontinuity_Type = DateAndTime
_LinearityCounterDiscontinuity_Object = MibTableColumn
linearityCounterDiscontinuity = _LinearityCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 5),
    _LinearityCounterDiscontinuity_Type()
)
linearityCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityCounterDiscontinuity.setStatus("current")
_LinearityCounterReset_Type = TruthValue
_LinearityCounterReset_Object = MibTableColumn
linearityCounterReset = _LinearityCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 6),
    _LinearityCounterReset_Type()
)
linearityCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linearityCounterReset.setStatus("current")
_LinearityLatestError_Type = DateAndTime
_LinearityLatestError_Object = MibTableColumn
linearityLatestError = _LinearityLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 7),
    _LinearityLatestError_Type()
)
linearityLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityLatestError.setStatus("current")
_LinearityActiveTime_Type = ActiveTime
_LinearityActiveTime_Object = MibTableColumn
linearityActiveTime = _LinearityActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 8),
    _LinearityActiveTime_Type()
)
linearityActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    linearityActiveTime.setUnits("second")
_LinearityMeasurementState_Type = MeasurementState
_LinearityMeasurementState_Object = MibTableColumn
linearityMeasurementState = _LinearityMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 9),
    _LinearityMeasurementState_Type()
)
linearityMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityMeasurementState.setStatus("current")
_LinearityValue_Type = FloatingPoint
_LinearityValue_Object = MibTableColumn
linearityValue = _LinearityValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 10, 1, 10),
    _LinearityValue_Type()
)
linearityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linearityValue.setStatus("current")
if mibBuilder.loadTexts:
    linearityValue.setUnits("dB")
_BerViterbiT_ObjectIdentity = ObjectIdentity
berViterbiT = _BerViterbiT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15)
)
_BerViterbiTTable_Object = MibTable
berViterbiTTable = _BerViterbiTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1)
)
if mibBuilder.loadTexts:
    berViterbiTTable.setStatus("current")
_BerViterbiTEntry_Object = MibTableRow
berViterbiTEntry = _BerViterbiTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1)
)
berViterbiTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berViterbiTInputNumber"),
)
if mibBuilder.loadTexts:
    berViterbiTEntry.setStatus("current")
_BerViterbiTInputNumber_Type = InputNumber
_BerViterbiTInputNumber_Object = MibTableColumn
berViterbiTInputNumber = _BerViterbiTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 1),
    _BerViterbiTInputNumber_Type()
)
berViterbiTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berViterbiTInputNumber.setStatus("current")
_BerViterbiTTestState_Type = TestState
_BerViterbiTTestState_Object = MibTableColumn
berViterbiTTestState = _BerViterbiTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 2),
    _BerViterbiTTestState_Type()
)
berViterbiTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTTestState.setStatus("current")


class _BerViterbiTEnable_Type(Enable):
    """Custom type berViterbiTEnable based on Enable"""
    defaultBinValue = "1"


_BerViterbiTEnable_Object = MibTableColumn
berViterbiTEnable = _BerViterbiTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 3),
    _BerViterbiTEnable_Type()
)
berViterbiTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiTEnable.setStatus("current")
_BerViterbiTCounter_Type = Counter32
_BerViterbiTCounter_Object = MibTableColumn
berViterbiTCounter = _BerViterbiTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 4),
    _BerViterbiTCounter_Type()
)
berViterbiTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTCounter.setStatus("current")
_BerViterbiTCounterDiscontinuity_Type = DateAndTime
_BerViterbiTCounterDiscontinuity_Object = MibTableColumn
berViterbiTCounterDiscontinuity = _BerViterbiTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 5),
    _BerViterbiTCounterDiscontinuity_Type()
)
berViterbiTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTCounterDiscontinuity.setStatus("current")
_BerViterbiTCounterReset_Type = TruthValue
_BerViterbiTCounterReset_Object = MibTableColumn
berViterbiTCounterReset = _BerViterbiTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 6),
    _BerViterbiTCounterReset_Type()
)
berViterbiTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiTCounterReset.setStatus("current")
_BerViterbiTLatestError_Type = DateAndTime
_BerViterbiTLatestError_Object = MibTableColumn
berViterbiTLatestError = _BerViterbiTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 7),
    _BerViterbiTLatestError_Type()
)
berViterbiTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLatestError.setStatus("current")
_BerViterbiTActiveTime_Type = ActiveTime
_BerViterbiTActiveTime_Object = MibTableColumn
berViterbiTActiveTime = _BerViterbiTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 8),
    _BerViterbiTActiveTime_Type()
)
berViterbiTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTActiveTime.setStatus("current")
_BerViterbiTMeasurementState_Type = MeasurementState
_BerViterbiTMeasurementState_Object = MibTableColumn
berViterbiTMeasurementState = _BerViterbiTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 9),
    _BerViterbiTMeasurementState_Type()
)
berViterbiTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTMeasurementState.setStatus("current")
_BerViterbiTValue_Type = FloatingPoint
_BerViterbiTValue_Object = MibTableColumn
berViterbiTValue = _BerViterbiTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 1, 1, 10),
    _BerViterbiTValue_Type()
)
berViterbiTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTValue.setStatus("current")
_BerViterbiTLPTable_Object = MibTable
berViterbiTLPTable = _BerViterbiTLPTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2)
)
if mibBuilder.loadTexts:
    berViterbiTLPTable.setStatus("current")
_BerViterbiTLPEntry_Object = MibTableRow
berViterbiTLPEntry = _BerViterbiTLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1)
)
berViterbiTLPEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berViterbiTLPInputNumber"),
)
if mibBuilder.loadTexts:
    berViterbiTLPEntry.setStatus("current")
_BerViterbiTLPInputNumber_Type = InputNumber
_BerViterbiTLPInputNumber_Object = MibTableColumn
berViterbiTLPInputNumber = _BerViterbiTLPInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 1),
    _BerViterbiTLPInputNumber_Type()
)
berViterbiTLPInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berViterbiTLPInputNumber.setStatus("current")
_BerViterbiTLPTestState_Type = TestState
_BerViterbiTLPTestState_Object = MibTableColumn
berViterbiTLPTestState = _BerViterbiTLPTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 2),
    _BerViterbiTLPTestState_Type()
)
berViterbiTLPTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPTestState.setStatus("current")


class _BerViterbiTLPEnable_Type(Enable):
    """Custom type berViterbiTLPEnable based on Enable"""
    defaultBinValue = "1"


_BerViterbiTLPEnable_Object = MibTableColumn
berViterbiTLPEnable = _BerViterbiTLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 3),
    _BerViterbiTLPEnable_Type()
)
berViterbiTLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiTLPEnable.setStatus("current")
_BerViterbiTLPCounter_Type = Counter32
_BerViterbiTLPCounter_Object = MibTableColumn
berViterbiTLPCounter = _BerViterbiTLPCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 4),
    _BerViterbiTLPCounter_Type()
)
berViterbiTLPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPCounter.setStatus("current")
_BerViterbiTLPCounterDiscontinuity_Type = DateAndTime
_BerViterbiTLPCounterDiscontinuity_Object = MibTableColumn
berViterbiTLPCounterDiscontinuity = _BerViterbiTLPCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 5),
    _BerViterbiTLPCounterDiscontinuity_Type()
)
berViterbiTLPCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPCounterDiscontinuity.setStatus("current")
_BerViterbiTLPCounterReset_Type = TruthValue
_BerViterbiTLPCounterReset_Object = MibTableColumn
berViterbiTLPCounterReset = _BerViterbiTLPCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 6),
    _BerViterbiTLPCounterReset_Type()
)
berViterbiTLPCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berViterbiTLPCounterReset.setStatus("current")
_BerViterbiTLPLatestError_Type = DateAndTime
_BerViterbiTLPLatestError_Object = MibTableColumn
berViterbiTLPLatestError = _BerViterbiTLPLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 7),
    _BerViterbiTLPLatestError_Type()
)
berViterbiTLPLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPLatestError.setStatus("current")
_BerViterbiTLPActiveTime_Type = ActiveTime
_BerViterbiTLPActiveTime_Object = MibTableColumn
berViterbiTLPActiveTime = _BerViterbiTLPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 8),
    _BerViterbiTLPActiveTime_Type()
)
berViterbiTLPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPActiveTime.setStatus("current")
_BerViterbiTLPMeasurementState_Type = MeasurementState
_BerViterbiTLPMeasurementState_Object = MibTableColumn
berViterbiTLPMeasurementState = _BerViterbiTLPMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 9),
    _BerViterbiTLPMeasurementState_Type()
)
berViterbiTLPMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPMeasurementState.setStatus("current")
_BerViterbiTLPValue_Type = FloatingPoint
_BerViterbiTLPValue_Object = MibTableColumn
berViterbiTLPValue = _BerViterbiTLPValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 15, 2, 1, 10),
    _BerViterbiTLPValue_Type()
)
berViterbiTLPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berViterbiTLPValue.setStatus("current")
if mibBuilder.loadTexts:
    berViterbiTLPValue.setUnits("dB")
_BerRS_ObjectIdentity = ObjectIdentity
berRS = _BerRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16)
)
_BerRSTable_Object = MibTable
berRSTable = _BerRSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1)
)
if mibBuilder.loadTexts:
    berRSTable.setStatus("current")
_BerRSEntry_Object = MibTableRow
berRSEntry = _BerRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1)
)
berRSEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berRSInputNumber"),
)
if mibBuilder.loadTexts:
    berRSEntry.setStatus("current")
_BerRSInputNumber_Type = InputNumber
_BerRSInputNumber_Object = MibTableColumn
berRSInputNumber = _BerRSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 1),
    _BerRSInputNumber_Type()
)
berRSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berRSInputNumber.setStatus("current")
_BerRSTestState_Type = TestState
_BerRSTestState_Object = MibTableColumn
berRSTestState = _BerRSTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 2),
    _BerRSTestState_Type()
)
berRSTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSTestState.setStatus("current")


class _BerRSEnable_Type(Enable):
    """Custom type berRSEnable based on Enable"""
    defaultBinValue = "1"


_BerRSEnable_Object = MibTableColumn
berRSEnable = _BerRSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 3),
    _BerRSEnable_Type()
)
berRSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSEnable.setStatus("current")
_BerRSCounter_Type = Counter32
_BerRSCounter_Object = MibTableColumn
berRSCounter = _BerRSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 4),
    _BerRSCounter_Type()
)
berRSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSCounter.setStatus("current")
_BerRSCounterDiscontinuity_Type = DateAndTime
_BerRSCounterDiscontinuity_Object = MibTableColumn
berRSCounterDiscontinuity = _BerRSCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 5),
    _BerRSCounterDiscontinuity_Type()
)
berRSCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSCounterDiscontinuity.setStatus("current")
_BerRSCounterReset_Type = TruthValue
_BerRSCounterReset_Object = MibTableColumn
berRSCounterReset = _BerRSCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 6),
    _BerRSCounterReset_Type()
)
berRSCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSCounterReset.setStatus("current")
_BerRSLatestError_Type = DateAndTime
_BerRSLatestError_Object = MibTableColumn
berRSLatestError = _BerRSLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 7),
    _BerRSLatestError_Type()
)
berRSLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLatestError.setStatus("current")
_BerRSActiveTime_Type = ActiveTime
_BerRSActiveTime_Object = MibTableColumn
berRSActiveTime = _BerRSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 8),
    _BerRSActiveTime_Type()
)
berRSActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSActiveTime.setStatus("current")
_BerRSMeasurementState_Type = MeasurementState
_BerRSMeasurementState_Object = MibTableColumn
berRSMeasurementState = _BerRSMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 9),
    _BerRSMeasurementState_Type()
)
berRSMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSMeasurementState.setStatus("current")
_BerRSValue_Type = FloatingPoint
_BerRSValue_Object = MibTableColumn
berRSValue = _BerRSValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 1, 1, 10),
    _BerRSValue_Type()
)
berRSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSValue.setStatus("current")
_BerRSLPTable_Object = MibTable
berRSLPTable = _BerRSLPTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2)
)
if mibBuilder.loadTexts:
    berRSLPTable.setStatus("current")
_BerRSLPEntry_Object = MibTableRow
berRSLPEntry = _BerRSLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1)
)
berRSLPEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "berRSLPInputNumber"),
)
if mibBuilder.loadTexts:
    berRSLPEntry.setStatus("current")
_BerRSLPInputNumber_Type = InputNumber
_BerRSLPInputNumber_Object = MibTableColumn
berRSLPInputNumber = _BerRSLPInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 1),
    _BerRSLPInputNumber_Type()
)
berRSLPInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    berRSLPInputNumber.setStatus("current")
_BerRSLPTestState_Type = TestState
_BerRSLPTestState_Object = MibTableColumn
berRSLPTestState = _BerRSLPTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 2),
    _BerRSLPTestState_Type()
)
berRSLPTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPTestState.setStatus("current")


class _BerRSLPEnable_Type(Enable):
    """Custom type berRSLPEnable based on Enable"""
    defaultBinValue = "1"


_BerRSLPEnable_Object = MibTableColumn
berRSLPEnable = _BerRSLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 3),
    _BerRSLPEnable_Type()
)
berRSLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSLPEnable.setStatus("current")
_BerRSLPCounter_Type = Counter32
_BerRSLPCounter_Object = MibTableColumn
berRSLPCounter = _BerRSLPCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 4),
    _BerRSLPCounter_Type()
)
berRSLPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPCounter.setStatus("current")
_BerRSLPCounterDiscontinuity_Type = DateAndTime
_BerRSLPCounterDiscontinuity_Object = MibTableColumn
berRSLPCounterDiscontinuity = _BerRSLPCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 5),
    _BerRSLPCounterDiscontinuity_Type()
)
berRSLPCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPCounterDiscontinuity.setStatus("current")
_BerRSLPCounterReset_Type = TruthValue
_BerRSLPCounterReset_Object = MibTableColumn
berRSLPCounterReset = _BerRSLPCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 6),
    _BerRSLPCounterReset_Type()
)
berRSLPCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berRSLPCounterReset.setStatus("current")
_BerRSLPLatestError_Type = DateAndTime
_BerRSLPLatestError_Object = MibTableColumn
berRSLPLatestError = _BerRSLPLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 7),
    _BerRSLPLatestError_Type()
)
berRSLPLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPLatestError.setStatus("current")
_BerRSLPActiveTime_Type = ActiveTime
_BerRSLPActiveTime_Object = MibTableColumn
berRSLPActiveTime = _BerRSLPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 8),
    _BerRSLPActiveTime_Type()
)
berRSLPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPActiveTime.setStatus("current")
_BerRSLPMeasurementState_Type = MeasurementState
_BerRSLPMeasurementState_Object = MibTableColumn
berRSLPMeasurementState = _BerRSLPMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 9),
    _BerRSLPMeasurementState_Type()
)
berRSLPMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPMeasurementState.setStatus("current")
_BerRSLPValue_Type = FloatingPoint
_BerRSLPValue_Object = MibTableColumn
berRSLPValue = _BerRSLPValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 16, 2, 1, 10),
    _BerRSLPValue_Type()
)
berRSLPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berRSLPValue.setStatus("current")
_IqAnalysisT_ObjectIdentity = ObjectIdentity
iqAnalysisT = _IqAnalysisT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18)
)
_MerTTable_Object = MibTable
merTTable = _MerTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2)
)
if mibBuilder.loadTexts:
    merTTable.setStatus("current")
_MerTEntry_Object = MibTableRow
merTEntry = _MerTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1)
)
merTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "merTInputNumber"),
)
if mibBuilder.loadTexts:
    merTEntry.setStatus("current")
_MerTInputNumber_Type = InputNumber
_MerTInputNumber_Object = MibTableColumn
merTInputNumber = _MerTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 1),
    _MerTInputNumber_Type()
)
merTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    merTInputNumber.setStatus("current")
_MerTTestState_Type = TestState
_MerTTestState_Object = MibTableColumn
merTTestState = _MerTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 2),
    _MerTTestState_Type()
)
merTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTTestState.setStatus("current")


class _MerTEnable_Type(Enable):
    """Custom type merTEnable based on Enable"""
    defaultBinValue = "1"


_MerTEnable_Object = MibTableColumn
merTEnable = _MerTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 3),
    _MerTEnable_Type()
)
merTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    merTEnable.setStatus("current")
_MerTCounter_Type = Counter32
_MerTCounter_Object = MibTableColumn
merTCounter = _MerTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 4),
    _MerTCounter_Type()
)
merTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTCounter.setStatus("current")
_MerTCounterDiscontinuity_Type = DateAndTime
_MerTCounterDiscontinuity_Object = MibTableColumn
merTCounterDiscontinuity = _MerTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 5),
    _MerTCounterDiscontinuity_Type()
)
merTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTCounterDiscontinuity.setStatus("current")


class _MerTCounterReset_Type(TruthValue):
    """Custom type merTCounterReset based on TruthValue"""


_MerTCounterReset_Object = MibTableColumn
merTCounterReset = _MerTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 6),
    _MerTCounterReset_Type()
)
merTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    merTCounterReset.setStatus("current")
_MerTLatestError_Type = DateAndTime
_MerTLatestError_Object = MibTableColumn
merTLatestError = _MerTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 7),
    _MerTLatestError_Type()
)
merTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTLatestError.setStatus("current")
_MerTActiveTime_Type = ActiveTime
_MerTActiveTime_Object = MibTableColumn
merTActiveTime = _MerTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 8),
    _MerTActiveTime_Type()
)
merTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    merTActiveTime.setUnits("second")
_MerTMeasurementState_Type = MeasurementState
_MerTMeasurementState_Object = MibTableColumn
merTMeasurementState = _MerTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 9),
    _MerTMeasurementState_Type()
)
merTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTMeasurementState.setStatus("current")
_MerTValue_Type = FloatingPoint
_MerTValue_Object = MibTableColumn
merTValue = _MerTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 2, 1, 10),
    _MerTValue_Type()
)
merTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    merTValue.setStatus("current")
if mibBuilder.loadTexts:
    merTValue.setUnits("dB")
_SteT_ObjectIdentity = ObjectIdentity
steT = _SteT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3)
)
_SteMeanTTable_Object = MibTable
steMeanTTable = _SteMeanTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1)
)
if mibBuilder.loadTexts:
    steMeanTTable.setStatus("current")
_SteMeanTEntry_Object = MibTableRow
steMeanTEntry = _SteMeanTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1)
)
steMeanTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "steMeanTInputNumber"),
)
if mibBuilder.loadTexts:
    steMeanTEntry.setStatus("current")
_SteMeanTInputNumber_Type = InputNumber
_SteMeanTInputNumber_Object = MibTableColumn
steMeanTInputNumber = _SteMeanTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 1),
    _SteMeanTInputNumber_Type()
)
steMeanTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    steMeanTInputNumber.setStatus("current")
_SteMeanTTestState_Type = TestState
_SteMeanTTestState_Object = MibTableColumn
steMeanTTestState = _SteMeanTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 2),
    _SteMeanTTestState_Type()
)
steMeanTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTTestState.setStatus("current")


class _SteMeanTEnable_Type(Enable):
    """Custom type steMeanTEnable based on Enable"""
    defaultBinValue = "1"


_SteMeanTEnable_Object = MibTableColumn
steMeanTEnable = _SteMeanTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 3),
    _SteMeanTEnable_Type()
)
steMeanTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steMeanTEnable.setStatus("current")
_SteMeanTCounter_Type = Counter32
_SteMeanTCounter_Object = MibTableColumn
steMeanTCounter = _SteMeanTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 4),
    _SteMeanTCounter_Type()
)
steMeanTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTCounter.setStatus("current")
_SteMeanTCounterDiscontinuity_Type = DateAndTime
_SteMeanTCounterDiscontinuity_Object = MibTableColumn
steMeanTCounterDiscontinuity = _SteMeanTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 5),
    _SteMeanTCounterDiscontinuity_Type()
)
steMeanTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTCounterDiscontinuity.setStatus("current")


class _SteMeanTCounterReset_Type(TruthValue):
    """Custom type steMeanTCounterReset based on TruthValue"""


_SteMeanTCounterReset_Object = MibTableColumn
steMeanTCounterReset = _SteMeanTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 6),
    _SteMeanTCounterReset_Type()
)
steMeanTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steMeanTCounterReset.setStatus("current")
_SteMeanTLatestError_Type = DateAndTime
_SteMeanTLatestError_Object = MibTableColumn
steMeanTLatestError = _SteMeanTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 7),
    _SteMeanTLatestError_Type()
)
steMeanTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTLatestError.setStatus("current")
_SteMeanTActiveTime_Type = ActiveTime
_SteMeanTActiveTime_Object = MibTableColumn
steMeanTActiveTime = _SteMeanTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 8),
    _SteMeanTActiveTime_Type()
)
steMeanTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    steMeanTActiveTime.setUnits("second")
_SteMeanTMeasurementState_Type = MeasurementState
_SteMeanTMeasurementState_Object = MibTableColumn
steMeanTMeasurementState = _SteMeanTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 9),
    _SteMeanTMeasurementState_Type()
)
steMeanTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTMeasurementState.setStatus("current")
_SteMeanTValue_Type = FloatingPoint
_SteMeanTValue_Object = MibTableColumn
steMeanTValue = _SteMeanTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 1, 1, 10),
    _SteMeanTValue_Type()
)
steMeanTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steMeanTValue.setStatus("current")
_SteDeviationTTable_Object = MibTable
steDeviationTTable = _SteDeviationTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2)
)
if mibBuilder.loadTexts:
    steDeviationTTable.setStatus("current")
_SteDeviationTEntry_Object = MibTableRow
steDeviationTEntry = _SteDeviationTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1)
)
steDeviationTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "steDeviationTInputNumber"),
)
if mibBuilder.loadTexts:
    steDeviationTEntry.setStatus("current")
_SteDeviationTInputNumber_Type = InputNumber
_SteDeviationTInputNumber_Object = MibTableColumn
steDeviationTInputNumber = _SteDeviationTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 1),
    _SteDeviationTInputNumber_Type()
)
steDeviationTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    steDeviationTInputNumber.setStatus("current")
_SteDeviationTTestState_Type = TestState
_SteDeviationTTestState_Object = MibTableColumn
steDeviationTTestState = _SteDeviationTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 2),
    _SteDeviationTTestState_Type()
)
steDeviationTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTTestState.setStatus("current")


class _SteDeviationTEnable_Type(Enable):
    """Custom type steDeviationTEnable based on Enable"""
    defaultBinValue = "1"


_SteDeviationTEnable_Object = MibTableColumn
steDeviationTEnable = _SteDeviationTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 3),
    _SteDeviationTEnable_Type()
)
steDeviationTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steDeviationTEnable.setStatus("current")
_SteDeviationTCounter_Type = Counter32
_SteDeviationTCounter_Object = MibTableColumn
steDeviationTCounter = _SteDeviationTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 4),
    _SteDeviationTCounter_Type()
)
steDeviationTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTCounter.setStatus("current")
_SteDeviationTCounterDiscontinuity_Type = DateAndTime
_SteDeviationTCounterDiscontinuity_Object = MibTableColumn
steDeviationTCounterDiscontinuity = _SteDeviationTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 5),
    _SteDeviationTCounterDiscontinuity_Type()
)
steDeviationTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTCounterDiscontinuity.setStatus("current")
_SteDeviationTCounterReset_Type = TruthValue
_SteDeviationTCounterReset_Object = MibTableColumn
steDeviationTCounterReset = _SteDeviationTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 6),
    _SteDeviationTCounterReset_Type()
)
steDeviationTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    steDeviationTCounterReset.setStatus("current")
_SteDeviationTLatestError_Type = DateAndTime
_SteDeviationTLatestError_Object = MibTableColumn
steDeviationTLatestError = _SteDeviationTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 7),
    _SteDeviationTLatestError_Type()
)
steDeviationTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTLatestError.setStatus("current")
_SteDeviationTActiveTime_Type = ActiveTime
_SteDeviationTActiveTime_Object = MibTableColumn
steDeviationTActiveTime = _SteDeviationTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 8),
    _SteDeviationTActiveTime_Type()
)
steDeviationTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    steDeviationTActiveTime.setUnits("second")
_SteDeviationTMeasurementState_Type = MeasurementState
_SteDeviationTMeasurementState_Object = MibTableColumn
steDeviationTMeasurementState = _SteDeviationTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 9),
    _SteDeviationTMeasurementState_Type()
)
steDeviationTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTMeasurementState.setStatus("current")
_SteDeviationTValue_Type = FloatingPoint
_SteDeviationTValue_Object = MibTableColumn
steDeviationTValue = _SteDeviationTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 3, 2, 1, 10),
    _SteDeviationTValue_Type()
)
steDeviationTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steDeviationTValue.setStatus("current")
_CsTTable_Object = MibTable
csTTable = _CsTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4)
)
if mibBuilder.loadTexts:
    csTTable.setStatus("current")
_CsTEntry_Object = MibTableRow
csTEntry = _CsTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1)
)
csTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "csTInputNumber"),
)
if mibBuilder.loadTexts:
    csTEntry.setStatus("current")
_CsTInputNumber_Type = InputNumber
_CsTInputNumber_Object = MibTableColumn
csTInputNumber = _CsTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 1),
    _CsTInputNumber_Type()
)
csTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csTInputNumber.setStatus("current")
_CsTTestState_Type = TestState
_CsTTestState_Object = MibTableColumn
csTTestState = _CsTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 2),
    _CsTTestState_Type()
)
csTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTTestState.setStatus("current")


class _CsTEnable_Type(Enable):
    """Custom type csTEnable based on Enable"""
    defaultBinValue = "1"


_CsTEnable_Object = MibTableColumn
csTEnable = _CsTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 3),
    _CsTEnable_Type()
)
csTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTEnable.setStatus("current")
_CsTCounter_Type = Counter32
_CsTCounter_Object = MibTableColumn
csTCounter = _CsTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 4),
    _CsTCounter_Type()
)
csTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTCounter.setStatus("current")
_CsTCounterDiscontinuity_Type = DateAndTime
_CsTCounterDiscontinuity_Object = MibTableColumn
csTCounterDiscontinuity = _CsTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 5),
    _CsTCounterDiscontinuity_Type()
)
csTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTCounterDiscontinuity.setStatus("current")
_CsTCounterReset_Type = TruthValue
_CsTCounterReset_Object = MibTableColumn
csTCounterReset = _CsTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 6),
    _CsTCounterReset_Type()
)
csTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTCounterReset.setStatus("current")
_CsTLatestError_Type = DateAndTime
_CsTLatestError_Object = MibTableColumn
csTLatestError = _CsTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 7),
    _CsTLatestError_Type()
)
csTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTLatestError.setStatus("current")
_CsTActiveTime_Type = ActiveTime
_CsTActiveTime_Object = MibTableColumn
csTActiveTime = _CsTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 8),
    _CsTActiveTime_Type()
)
csTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    csTActiveTime.setUnits("second")
_CsTMeasurementState_Type = MeasurementState
_CsTMeasurementState_Object = MibTableColumn
csTMeasurementState = _CsTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 9),
    _CsTMeasurementState_Type()
)
csTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTMeasurementState.setStatus("current")
_CsTValue_Type = FloatingPoint
_CsTValue_Object = MibTableColumn
csTValue = _CsTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 4, 1, 10),
    _CsTValue_Type()
)
csTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csTValue.setStatus("current")
if mibBuilder.loadTexts:
    csTValue.setUnits("dB")
_AiTTable_Object = MibTable
aiTTable = _AiTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5)
)
if mibBuilder.loadTexts:
    aiTTable.setStatus("current")
_AiTEntry_Object = MibTableRow
aiTEntry = _AiTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1)
)
aiTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "aiTInputNumber"),
)
if mibBuilder.loadTexts:
    aiTEntry.setStatus("current")
_AiTInputNumber_Type = InputNumber
_AiTInputNumber_Object = MibTableColumn
aiTInputNumber = _AiTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 1),
    _AiTInputNumber_Type()
)
aiTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aiTInputNumber.setStatus("current")
_AiTTestState_Type = TestState
_AiTTestState_Object = MibTableColumn
aiTTestState = _AiTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 2),
    _AiTTestState_Type()
)
aiTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTTestState.setStatus("current")


class _AiTEnable_Type(Enable):
    """Custom type aiTEnable based on Enable"""
    defaultBinValue = "1"


_AiTEnable_Object = MibTableColumn
aiTEnable = _AiTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 3),
    _AiTEnable_Type()
)
aiTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiTEnable.setStatus("current")
_AiTCounter_Type = Counter32
_AiTCounter_Object = MibTableColumn
aiTCounter = _AiTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 4),
    _AiTCounter_Type()
)
aiTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTCounter.setStatus("current")
_AiTCounterDiscontinuity_Type = DateAndTime
_AiTCounterDiscontinuity_Object = MibTableColumn
aiTCounterDiscontinuity = _AiTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 5),
    _AiTCounterDiscontinuity_Type()
)
aiTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTCounterDiscontinuity.setStatus("current")


class _AiTCounterReset_Type(TruthValue):
    """Custom type aiTCounterReset based on TruthValue"""


_AiTCounterReset_Object = MibTableColumn
aiTCounterReset = _AiTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 6),
    _AiTCounterReset_Type()
)
aiTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiTCounterReset.setStatus("current")
_AiTLatestError_Type = DateAndTime
_AiTLatestError_Object = MibTableColumn
aiTLatestError = _AiTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 7),
    _AiTLatestError_Type()
)
aiTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTLatestError.setStatus("current")
_AiTActiveTime_Type = ActiveTime
_AiTActiveTime_Object = MibTableColumn
aiTActiveTime = _AiTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 8),
    _AiTActiveTime_Type()
)
aiTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    aiTActiveTime.setUnits("second")
_AiTMeasurementState_Type = MeasurementState
_AiTMeasurementState_Object = MibTableColumn
aiTMeasurementState = _AiTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 9),
    _AiTMeasurementState_Type()
)
aiTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTMeasurementState.setStatus("current")
_AiTValue_Type = FloatingPoint
_AiTValue_Object = MibTableColumn
aiTValue = _AiTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 5, 1, 10),
    _AiTValue_Type()
)
aiTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTValue.setStatus("current")
_QeTTable_Object = MibTable
qeTTable = _QeTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6)
)
if mibBuilder.loadTexts:
    qeTTable.setStatus("current")
_QeTEntry_Object = MibTableRow
qeTEntry = _QeTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1)
)
qeTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "qeTInputNumber"),
)
if mibBuilder.loadTexts:
    qeTEntry.setStatus("current")
_QeTInputNumber_Type = InputNumber
_QeTInputNumber_Object = MibTableColumn
qeTInputNumber = _QeTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 1),
    _QeTInputNumber_Type()
)
qeTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qeTInputNumber.setStatus("current")
_QeTTestState_Type = TestState
_QeTTestState_Object = MibTableColumn
qeTTestState = _QeTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 2),
    _QeTTestState_Type()
)
qeTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTTestState.setStatus("current")


class _QeTEnable_Type(Enable):
    """Custom type qeTEnable based on Enable"""
    defaultBinValue = "1"


_QeTEnable_Object = MibTableColumn
qeTEnable = _QeTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 3),
    _QeTEnable_Type()
)
qeTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qeTEnable.setStatus("current")
_QeTCounter_Type = Counter32
_QeTCounter_Object = MibTableColumn
qeTCounter = _QeTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 4),
    _QeTCounter_Type()
)
qeTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTCounter.setStatus("current")
_QeTCounterDiscontinuity_Type = DateAndTime
_QeTCounterDiscontinuity_Object = MibTableColumn
qeTCounterDiscontinuity = _QeTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 5),
    _QeTCounterDiscontinuity_Type()
)
qeTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTCounterDiscontinuity.setStatus("current")


class _QeTCounterReset_Type(TruthValue):
    """Custom type qeTCounterReset based on TruthValue"""


_QeTCounterReset_Object = MibTableColumn
qeTCounterReset = _QeTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 6),
    _QeTCounterReset_Type()
)
qeTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qeTCounterReset.setStatus("current")
_QeTLatestError_Type = DateAndTime
_QeTLatestError_Object = MibTableColumn
qeTLatestError = _QeTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 7),
    _QeTLatestError_Type()
)
qeTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTLatestError.setStatus("current")
_QeTActiveTime_Type = ActiveTime
_QeTActiveTime_Object = MibTableColumn
qeTActiveTime = _QeTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 8),
    _QeTActiveTime_Type()
)
qeTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    qeTActiveTime.setUnits("second")
_QeTMeasurementState_Type = MeasurementState
_QeTMeasurementState_Object = MibTableColumn
qeTMeasurementState = _QeTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 9),
    _QeTMeasurementState_Type()
)
qeTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTMeasurementState.setStatus("current")
_QeTValue_Type = FloatingPoint
_QeTValue_Object = MibTableColumn
qeTValue = _QeTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 6, 1, 10),
    _QeTValue_Type()
)
qeTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeTValue.setStatus("current")
if mibBuilder.loadTexts:
    qeTValue.setUnits("degree")
_PjTTable_Object = MibTable
pjTTable = _PjTTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7)
)
if mibBuilder.loadTexts:
    pjTTable.setStatus("current")
_PjTEntry_Object = MibTableRow
pjTEntry = _PjTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1)
)
pjTEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "pjTInputNumber"),
)
if mibBuilder.loadTexts:
    pjTEntry.setStatus("current")
_PjTInputNumber_Type = InputNumber
_PjTInputNumber_Object = MibTableColumn
pjTInputNumber = _PjTInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 1),
    _PjTInputNumber_Type()
)
pjTInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pjTInputNumber.setStatus("current")
_PjTTestState_Type = TestState
_PjTTestState_Object = MibTableColumn
pjTTestState = _PjTTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 2),
    _PjTTestState_Type()
)
pjTTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTTestState.setStatus("current")


class _PjTEnable_Type(Enable):
    """Custom type pjTEnable based on Enable"""
    defaultBinValue = "1"


_PjTEnable_Object = MibTableColumn
pjTEnable = _PjTEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 3),
    _PjTEnable_Type()
)
pjTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pjTEnable.setStatus("current")
_PjTCounter_Type = Counter32
_PjTCounter_Object = MibTableColumn
pjTCounter = _PjTCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 4),
    _PjTCounter_Type()
)
pjTCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTCounter.setStatus("current")
_PjTCounterDiscontinuity_Type = DateAndTime
_PjTCounterDiscontinuity_Object = MibTableColumn
pjTCounterDiscontinuity = _PjTCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 5),
    _PjTCounterDiscontinuity_Type()
)
pjTCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTCounterDiscontinuity.setStatus("current")


class _PjTCounterReset_Type(TruthValue):
    """Custom type pjTCounterReset based on TruthValue"""


_PjTCounterReset_Object = MibTableColumn
pjTCounterReset = _PjTCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 6),
    _PjTCounterReset_Type()
)
pjTCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pjTCounterReset.setStatus("current")
_PjTLatestError_Type = DateAndTime
_PjTLatestError_Object = MibTableColumn
pjTLatestError = _PjTLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 7),
    _PjTLatestError_Type()
)
pjTLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTLatestError.setStatus("current")
_PjTActiveTime_Type = ActiveTime
_PjTActiveTime_Object = MibTableColumn
pjTActiveTime = _PjTActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 8),
    _PjTActiveTime_Type()
)
pjTActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    pjTActiveTime.setUnits("second")
_PjTMeasurementState_Type = MeasurementState
_PjTMeasurementState_Object = MibTableColumn
pjTMeasurementState = _PjTMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 9),
    _PjTMeasurementState_Type()
)
pjTMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTMeasurementState.setStatus("current")
_PjTValue_Type = FloatingPoint
_PjTValue_Object = MibTableColumn
pjTValue = _PjTValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 18, 7, 1, 10),
    _PjTValue_Type()
)
pjTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjTValue.setStatus("current")
if mibBuilder.loadTexts:
    pjTValue.setUnits("degree")
_MipSyntaxTable_Object = MibTable
mipSyntaxTable = _MipSyntaxTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20)
)
if mibBuilder.loadTexts:
    mipSyntaxTable.setStatus("current")
_MipSyntaxEntry_Object = MibTableRow
mipSyntaxEntry = _MipSyntaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1)
)
mipSyntaxEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "mipSyntaxTestNumber"),
    (0, "DVB-MGTR101290-MIB", "mipSyntaxInputNumber"),
)
if mibBuilder.loadTexts:
    mipSyntaxEntry.setStatus("current")
_MipSyntaxInputNumber_Type = InputNumber
_MipSyntaxInputNumber_Object = MibTableColumn
mipSyntaxInputNumber = _MipSyntaxInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 1),
    _MipSyntaxInputNumber_Type()
)
mipSyntaxInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mipSyntaxInputNumber.setStatus("current")
_MipSyntaxTestNumber_Type = IndexMIPSyntaxTest
_MipSyntaxTestNumber_Object = MibTableColumn
mipSyntaxTestNumber = _MipSyntaxTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 2),
    _MipSyntaxTestNumber_Type()
)
mipSyntaxTestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mipSyntaxTestNumber.setStatus("current")
_MipSyntaxState_Type = TestState
_MipSyntaxState_Object = MibTableColumn
mipSyntaxState = _MipSyntaxState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 3),
    _MipSyntaxState_Type()
)
mipSyntaxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSyntaxState.setStatus("current")


class _MipSyntaxEnable_Type(Enable):
    """Custom type mipSyntaxEnable based on Enable"""
    defaultBinValue = "1"


_MipSyntaxEnable_Object = MibTableColumn
mipSyntaxEnable = _MipSyntaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 4),
    _MipSyntaxEnable_Type()
)
mipSyntaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mipSyntaxEnable.setStatus("current")
_MipSyntaxCounter_Type = Counter32
_MipSyntaxCounter_Object = MibTableColumn
mipSyntaxCounter = _MipSyntaxCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 5),
    _MipSyntaxCounter_Type()
)
mipSyntaxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSyntaxCounter.setStatus("current")
_MipSyntaxCounterDiscontinuity_Type = DateAndTime
_MipSyntaxCounterDiscontinuity_Object = MibTableColumn
mipSyntaxCounterDiscontinuity = _MipSyntaxCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 6),
    _MipSyntaxCounterDiscontinuity_Type()
)
mipSyntaxCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSyntaxCounterDiscontinuity.setStatus("current")
_MipSyntaxCounterReset_Type = TruthValue
_MipSyntaxCounterReset_Object = MibTableColumn
mipSyntaxCounterReset = _MipSyntaxCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 7),
    _MipSyntaxCounterReset_Type()
)
mipSyntaxCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mipSyntaxCounterReset.setStatus("current")
_MipSyntaxLatestError_Type = DateAndTime
_MipSyntaxLatestError_Object = MibTableColumn
mipSyntaxLatestError = _MipSyntaxLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 8),
    _MipSyntaxLatestError_Type()
)
mipSyntaxLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSyntaxLatestError.setStatus("current")
_MipSyntaxActiveTime_Type = ActiveTime
_MipSyntaxActiveTime_Object = MibTableColumn
mipSyntaxActiveTime = _MipSyntaxActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 20, 1, 9),
    _MipSyntaxActiveTime_Type()
)
mipSyntaxActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSyntaxActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    mipSyntaxActiveTime.setUnits("second")
_SystemErrorPerformance_ObjectIdentity = ObjectIdentity
systemErrorPerformance = _SystemErrorPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21)
)
_SepEtiTable_Object = MibTable
sepEtiTable = _SepEtiTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1)
)
if mibBuilder.loadTexts:
    sepEtiTable.setStatus("current")
_SepEtiEntry_Object = MibTableRow
sepEtiEntry = _SepEtiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1)
)
sepEtiEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "sepEtiInputNumber"),
)
if mibBuilder.loadTexts:
    sepEtiEntry.setStatus("current")
_SepEtiInputNumber_Type = InputNumber
_SepEtiInputNumber_Object = MibTableColumn
sepEtiInputNumber = _SepEtiInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 1),
    _SepEtiInputNumber_Type()
)
sepEtiInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sepEtiInputNumber.setStatus("current")
_SepEtiTestState_Type = TestState
_SepEtiTestState_Object = MibTableColumn
sepEtiTestState = _SepEtiTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 2),
    _SepEtiTestState_Type()
)
sepEtiTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiTestState.setStatus("current")


class _SepEtiEnable_Type(Enable):
    """Custom type sepEtiEnable based on Enable"""
    defaultBinValue = "1"


_SepEtiEnable_Object = MibTableColumn
sepEtiEnable = _SepEtiEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 3),
    _SepEtiEnable_Type()
)
sepEtiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sepEtiEnable.setStatus("current")
_SepEtiCounter_Type = Counter32
_SepEtiCounter_Object = MibTableColumn
sepEtiCounter = _SepEtiCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 4),
    _SepEtiCounter_Type()
)
sepEtiCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiCounter.setStatus("current")
_SepEtiCounterDiscontinuity_Type = DateAndTime
_SepEtiCounterDiscontinuity_Object = MibTableColumn
sepEtiCounterDiscontinuity = _SepEtiCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 5),
    _SepEtiCounterDiscontinuity_Type()
)
sepEtiCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiCounterDiscontinuity.setStatus("current")
_SepEtiCounterReset_Type = TruthValue
_SepEtiCounterReset_Object = MibTableColumn
sepEtiCounterReset = _SepEtiCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 6),
    _SepEtiCounterReset_Type()
)
sepEtiCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sepEtiCounterReset.setStatus("current")
_SepEtiLatestError_Type = DateAndTime
_SepEtiLatestError_Object = MibTableColumn
sepEtiLatestError = _SepEtiLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 7),
    _SepEtiLatestError_Type()
)
sepEtiLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiLatestError.setStatus("current")
_SepEtiActiveTime_Type = ActiveTime
_SepEtiActiveTime_Object = MibTableColumn
sepEtiActiveTime = _SepEtiActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 8),
    _SepEtiActiveTime_Type()
)
sepEtiActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    sepEtiActiveTime.setUnits("second")
_SepEtiMeasurementState_Type = MeasurementState
_SepEtiMeasurementState_Object = MibTableColumn
sepEtiMeasurementState = _SepEtiMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 9),
    _SepEtiMeasurementState_Type()
)
sepEtiMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiMeasurementState.setStatus("current")
_SepEtiValue_Type = FloatingPoint
_SepEtiValue_Object = MibTableColumn
sepEtiValue = _SepEtiValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 1, 1, 10),
    _SepEtiValue_Type()
)
sepEtiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepEtiValue.setStatus("current")
_SepSetiTable_Object = MibTable
sepSetiTable = _SepSetiTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2)
)
if mibBuilder.loadTexts:
    sepSetiTable.setStatus("current")
_SepSetiEntry_Object = MibTableRow
sepSetiEntry = _SepSetiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1)
)
sepSetiEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "sepSetiInputNumber"),
)
if mibBuilder.loadTexts:
    sepSetiEntry.setStatus("current")
_SepSetiInputNumber_Type = InputNumber
_SepSetiInputNumber_Object = MibTableColumn
sepSetiInputNumber = _SepSetiInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 1),
    _SepSetiInputNumber_Type()
)
sepSetiInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sepSetiInputNumber.setStatus("current")
_SepSetiTestState_Type = TestState
_SepSetiTestState_Object = MibTableColumn
sepSetiTestState = _SepSetiTestState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 2),
    _SepSetiTestState_Type()
)
sepSetiTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiTestState.setStatus("current")


class _SepSetiEnable_Type(Enable):
    """Custom type sepSetiEnable based on Enable"""
    defaultBinValue = "1"


_SepSetiEnable_Object = MibTableColumn
sepSetiEnable = _SepSetiEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 3),
    _SepSetiEnable_Type()
)
sepSetiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sepSetiEnable.setStatus("current")
_SepSetiCounter_Type = Counter32
_SepSetiCounter_Object = MibTableColumn
sepSetiCounter = _SepSetiCounter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 4),
    _SepSetiCounter_Type()
)
sepSetiCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiCounter.setStatus("current")
_SepSetiCounterDiscontinuity_Type = DateAndTime
_SepSetiCounterDiscontinuity_Object = MibTableColumn
sepSetiCounterDiscontinuity = _SepSetiCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 5),
    _SepSetiCounterDiscontinuity_Type()
)
sepSetiCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiCounterDiscontinuity.setStatus("current")
_SepSetiCounterReset_Type = TruthValue
_SepSetiCounterReset_Object = MibTableColumn
sepSetiCounterReset = _SepSetiCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 6),
    _SepSetiCounterReset_Type()
)
sepSetiCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sepSetiCounterReset.setStatus("current")
_SepSetiLatestError_Type = DateAndTime
_SepSetiLatestError_Object = MibTableColumn
sepSetiLatestError = _SepSetiLatestError_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 7),
    _SepSetiLatestError_Type()
)
sepSetiLatestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiLatestError.setStatus("current")
_SepSetiActiveTime_Type = ActiveTime
_SepSetiActiveTime_Object = MibTableColumn
sepSetiActiveTime = _SepSetiActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 8),
    _SepSetiActiveTime_Type()
)
sepSetiActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    sepSetiActiveTime.setUnits("second")
_SepSetiMeasurementState_Type = MeasurementState
_SepSetiMeasurementState_Object = MibTableColumn
sepSetiMeasurementState = _SepSetiMeasurementState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 9),
    _SepSetiMeasurementState_Type()
)
sepSetiMeasurementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiMeasurementState.setStatus("current")
_SepSetiValue_Type = FloatingPoint
_SepSetiValue_Object = MibTableColumn
sepSetiValue = _SepSetiValue_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 21, 2, 1, 10),
    _SepSetiValue_Type()
)
sepSetiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sepSetiValue.setStatus("current")
_TerrestrialPreferencesTable_Object = MibTable
terrestrialPreferencesTable = _TerrestrialPreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100)
)
if mibBuilder.loadTexts:
    terrestrialPreferencesTable.setStatus("current")
_TerrestrialPreferencesEntry_Object = MibTableRow
terrestrialPreferencesEntry = _TerrestrialPreferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1)
)
terrestrialPreferencesEntry.setIndexNames(
    (0, "DVB-MGTR101290-MIB", "terrestrialPrefInputNumber"),
)
if mibBuilder.loadTexts:
    terrestrialPreferencesEntry.setStatus("current")
_TerrestrialPrefInputNumber_Type = InputNumber
_TerrestrialPrefInputNumber_Object = MibTableColumn
terrestrialPrefInputNumber = _TerrestrialPrefInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 1),
    _TerrestrialPrefInputNumber_Type()
)
terrestrialPrefInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    terrestrialPrefInputNumber.setStatus("current")
_TerrestrialPrefCentreFrequency_Type = FloatingPoint
_TerrestrialPrefCentreFrequency_Object = MibTableColumn
terrestrialPrefCentreFrequency = _TerrestrialPrefCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 2),
    _TerrestrialPrefCentreFrequency_Type()
)
terrestrialPrefCentreFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFrequency.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFrequency.setUnits("MHz")
_TerrestrialPrefBandwidth_Type = FloatingPoint
_TerrestrialPrefBandwidth_Object = MibTableColumn
terrestrialPrefBandwidth = _TerrestrialPrefBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 3),
    _TerrestrialPrefBandwidth_Type()
)
terrestrialPrefBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefBandwidth.setUnits("MHz")
_TerrestrialPrefModulation_Type = Modulation
_TerrestrialPrefModulation_Object = MibTableColumn
terrestrialPrefModulation = _TerrestrialPrefModulation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 4),
    _TerrestrialPrefModulation_Type()
)
terrestrialPrefModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefModulation.setStatus("current")
_TerrestrialPrefTransmissionMode_Type = TerrestrialTransmissionMode
_TerrestrialPrefTransmissionMode_Object = MibTableColumn
terrestrialPrefTransmissionMode = _TerrestrialPrefTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 5),
    _TerrestrialPrefTransmissionMode_Type()
)
terrestrialPrefTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefTransmissionMode.setStatus("current")
_TerrestrialPrefGuardInterval_Type = GuardInterval
_TerrestrialPrefGuardInterval_Object = MibTableColumn
terrestrialPrefGuardInterval = _TerrestrialPrefGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 6),
    _TerrestrialPrefGuardInterval_Type()
)
terrestrialPrefGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefGuardInterval.setStatus("current")
_TerrestrialPrefHierarchical_Type = Hierarchy
_TerrestrialPrefHierarchical_Object = MibTableColumn
terrestrialPrefHierarchical = _TerrestrialPrefHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 7),
    _TerrestrialPrefHierarchical_Type()
)
terrestrialPrefHierarchical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefHierarchical.setStatus("current")
_TerrestrialPrefCentreFreqExpected_Type = FloatingPoint
_TerrestrialPrefCentreFreqExpected_Object = MibTableColumn
terrestrialPrefCentreFreqExpected = _TerrestrialPrefCentreFreqExpected_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 8),
    _TerrestrialPrefCentreFreqExpected_Type()
)
terrestrialPrefCentreFreqExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFreqExpected.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFreqExpected.setUnits("Hz")
_TerrestrialPrefCentreFreqLimit_Type = FloatingPoint
_TerrestrialPrefCentreFreqLimit_Object = MibTableColumn
terrestrialPrefCentreFreqLimit = _TerrestrialPrefCentreFreqLimit_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 9),
    _TerrestrialPrefCentreFreqLimit_Type()
)
terrestrialPrefCentreFreqLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFreqLimit.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefCentreFreqLimit.setUnits("Hz")
_TerrestrialPrefChannelWidthLimit_Type = FloatingPoint
_TerrestrialPrefChannelWidthLimit_Object = MibTableColumn
terrestrialPrefChannelWidthLimit = _TerrestrialPrefChannelWidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 10),
    _TerrestrialPrefChannelWidthLimit_Type()
)
terrestrialPrefChannelWidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefChannelWidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefChannelWidthLimit.setUnits("Hz")
_TerrestrialPrefSymbolLengthLimit_Type = FloatingPoint
_TerrestrialPrefSymbolLengthLimit_Object = MibTableColumn
terrestrialPrefSymbolLengthLimit = _TerrestrialPrefSymbolLengthLimit_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 11),
    _TerrestrialPrefSymbolLengthLimit_Type()
)
terrestrialPrefSymbolLengthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSymbolLengthLimit.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSymbolLengthLimit.setUnits("s")
_TerrestrialPrefPowerMin_Type = FloatingPoint
_TerrestrialPrefPowerMin_Object = MibTableColumn
terrestrialPrefPowerMin = _TerrestrialPrefPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 12),
    _TerrestrialPrefPowerMin_Type()
)
terrestrialPrefPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefPowerMin.setUnits("dBm")
_TerrestrialPrefPowerMax_Type = FloatingPoint
_TerrestrialPrefPowerMax_Object = MibTableColumn
terrestrialPrefPowerMax = _TerrestrialPrefPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 13),
    _TerrestrialPrefPowerMax_Type()
)
terrestrialPrefPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefPowerMax.setUnits("dBm")


class _TerrestrialPrefENDBER_Type(FloatingPoint):
    """Custom type terrestrialPrefENDBER based on FloatingPoint"""
    defaultValue = OctetString("2E-04")


_TerrestrialPrefENDBER_Object = MibTableColumn
terrestrialPrefENDBER = _TerrestrialPrefENDBER_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 14),
    _TerrestrialPrefENDBER_Type()
)
terrestrialPrefENDBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENDBER.setStatus("current")
_TerrestrialPrefENDIdeal_Type = FloatingPoint
_TerrestrialPrefENDIdeal_Object = MibTableColumn
terrestrialPrefENDIdeal = _TerrestrialPrefENDIdeal_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 15),
    _TerrestrialPrefENDIdeal_Type()
)
terrestrialPrefENDIdeal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENDIdeal.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENDIdeal.setUnits("dB")
_TerrestrialPrefENDMax_Type = FloatingPoint
_TerrestrialPrefENDMax_Object = MibTableColumn
terrestrialPrefENDMax = _TerrestrialPrefENDMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 16),
    _TerrestrialPrefENDMax_Type()
)
terrestrialPrefENDMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENDMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENDMax.setUnits("dB")
_TerrestrialPrefENFIdeal_Type = FloatingPoint
_TerrestrialPrefENFIdeal_Object = MibTableColumn
terrestrialPrefENFIdeal = _TerrestrialPrefENFIdeal_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 17),
    _TerrestrialPrefENFIdeal_Type()
)
terrestrialPrefENFIdeal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENFIdeal.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENFIdeal.setUnits("dB")
_TerrestrialPrefENFMax_Type = FloatingPoint
_TerrestrialPrefENFMax_Object = MibTableColumn
terrestrialPrefENFMax = _TerrestrialPrefENFMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 18),
    _TerrestrialPrefENFMax_Type()
)
terrestrialPrefENFMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENFMax.setStatus("current")
_TerrestrialPrefENDLPIdeal_Type = FloatingPoint
_TerrestrialPrefENDLPIdeal_Object = MibTableColumn
terrestrialPrefENDLPIdeal = _TerrestrialPrefENDLPIdeal_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 19),
    _TerrestrialPrefENDLPIdeal_Type()
)
terrestrialPrefENDLPIdeal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENDLPIdeal.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENDLPIdeal.setUnits("dB")
_TerrestrialPrefENDLPMax_Type = FloatingPoint
_TerrestrialPrefENDLPMax_Object = MibTableColumn
terrestrialPrefENDLPMax = _TerrestrialPrefENDLPMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 20),
    _TerrestrialPrefENDLPMax_Type()
)
terrestrialPrefENDLPMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENDLPMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENDLPMax.setUnits("dB")
_TerrestrialPrefENFLPIdeal_Type = FloatingPoint
_TerrestrialPrefENFLPIdeal_Object = MibTableColumn
terrestrialPrefENFLPIdeal = _TerrestrialPrefENFLPIdeal_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 21),
    _TerrestrialPrefENFLPIdeal_Type()
)
terrestrialPrefENFLPIdeal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENFLPIdeal.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENFLPIdeal.setUnits("dB")
_TerrestrialPrefENFLPMax_Type = FloatingPoint
_TerrestrialPrefENFLPMax_Object = MibTableColumn
terrestrialPrefENFLPMax = _TerrestrialPrefENFLPMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 22),
    _TerrestrialPrefENFLPMax_Type()
)
terrestrialPrefENFLPMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefENFLPMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefENFLPMax.setUnits("dB")
_TerrestrialPrefLinearityMin_Type = FloatingPoint
_TerrestrialPrefLinearityMin_Object = MibTableColumn
terrestrialPrefLinearityMin = _TerrestrialPrefLinearityMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 23),
    _TerrestrialPrefLinearityMin_Type()
)
terrestrialPrefLinearityMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefLinearityMin.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefLinearityMin.setUnits("dB")
_TerrestrialPrefBERViterbiMax_Type = FloatingPoint
_TerrestrialPrefBERViterbiMax_Object = MibTableColumn
terrestrialPrefBERViterbiMax = _TerrestrialPrefBERViterbiMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 24),
    _TerrestrialPrefBERViterbiMax_Type()
)
terrestrialPrefBERViterbiMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefBERViterbiMax.setStatus("current")
_TerrestrialPrefBERViterbiLPMax_Type = FloatingPoint
_TerrestrialPrefBERViterbiLPMax_Object = MibTableColumn
terrestrialPrefBERViterbiLPMax = _TerrestrialPrefBERViterbiLPMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 25),
    _TerrestrialPrefBERViterbiLPMax_Type()
)
terrestrialPrefBERViterbiLPMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefBERViterbiLPMax.setStatus("current")
_TerrestrialPrefBERRSMax_Type = FloatingPoint
_TerrestrialPrefBERRSMax_Object = MibTableColumn
terrestrialPrefBERRSMax = _TerrestrialPrefBERRSMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 26),
    _TerrestrialPrefBERRSMax_Type()
)
terrestrialPrefBERRSMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefBERRSMax.setStatus("current")
_TerrestrialPrefBERRSLPMax_Type = FloatingPoint
_TerrestrialPrefBERRSLPMax_Object = MibTableColumn
terrestrialPrefBERRSLPMax = _TerrestrialPrefBERRSLPMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 27),
    _TerrestrialPrefBERRSLPMax_Type()
)
terrestrialPrefBERRSLPMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefBERRSLPMax.setStatus("current")
_TerrestrialPrefMerTMin_Type = FloatingPoint
_TerrestrialPrefMerTMin_Object = MibTableColumn
terrestrialPrefMerTMin = _TerrestrialPrefMerTMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 28),
    _TerrestrialPrefMerTMin_Type()
)
terrestrialPrefMerTMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefMerTMin.setStatus("current")
_TerrestrialPrefSteMeanMax_Type = FloatingPoint
_TerrestrialPrefSteMeanMax_Object = MibTableColumn
terrestrialPrefSteMeanMax = _TerrestrialPrefSteMeanMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 29),
    _TerrestrialPrefSteMeanMax_Type()
)
terrestrialPrefSteMeanMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSteMeanMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSteMeanMax.setUnits("dB")
_TerrestrialPrefSteDeviationMax_Type = FloatingPoint
_TerrestrialPrefSteDeviationMax_Object = MibTableColumn
terrestrialPrefSteDeviationMax = _TerrestrialPrefSteDeviationMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 30),
    _TerrestrialPrefSteDeviationMax_Type()
)
terrestrialPrefSteDeviationMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSteDeviationMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSteDeviationMax.setUnits("dB")
_TerrestrialPrefCsMin_Type = FloatingPoint
_TerrestrialPrefCsMin_Object = MibTableColumn
terrestrialPrefCsMin = _TerrestrialPrefCsMin_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 31),
    _TerrestrialPrefCsMin_Type()
)
terrestrialPrefCsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefCsMin.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefCsMin.setUnits("dB")
_TerrestrialPrefAiMax_Type = FloatingPoint
_TerrestrialPrefAiMax_Object = MibTableColumn
terrestrialPrefAiMax = _TerrestrialPrefAiMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 32),
    _TerrestrialPrefAiMax_Type()
)
terrestrialPrefAiMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefAiMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefAiMax.setUnits("dB")
_TerrestrialPrefQeMax_Type = FloatingPoint
_TerrestrialPrefQeMax_Object = MibTableColumn
terrestrialPrefQeMax = _TerrestrialPrefQeMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 33),
    _TerrestrialPrefQeMax_Type()
)
terrestrialPrefQeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefQeMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefQeMax.setUnits("dB")
_TerrestrialPrefPjMax_Type = FloatingPoint
_TerrestrialPrefPjMax_Object = MibTableColumn
terrestrialPrefPjMax = _TerrestrialPrefPjMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 34),
    _TerrestrialPrefPjMax_Type()
)
terrestrialPrefPjMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefPjMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefPjMax.setUnits("dB")
_TerrestrialPrefMIPTimingLimit_Type = FloatingPoint
_TerrestrialPrefMIPTimingLimit_Object = MibTableColumn
terrestrialPrefMIPTimingLimit = _TerrestrialPrefMIPTimingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 35),
    _TerrestrialPrefMIPTimingLimit_Type()
)
terrestrialPrefMIPTimingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefMIPTimingLimit.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefMIPTimingLimit.setUnits("second")
_TerrestrialPrefMIPDeviationMax_Type = FloatingPoint
_TerrestrialPrefMIPDeviationMax_Object = MibTableColumn
terrestrialPrefMIPDeviationMax = _TerrestrialPrefMIPDeviationMax_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 36),
    _TerrestrialPrefMIPDeviationMax_Type()
)
terrestrialPrefMIPDeviationMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefMIPDeviationMax.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefMIPDeviationMax.setUnits("bit/s")
_TerrestrialPrefSEPUATMode_Type = UATMode
_TerrestrialPrefSEPUATMode_Object = MibTableColumn
terrestrialPrefSEPUATMode = _TerrestrialPrefSEPUATMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 37),
    _TerrestrialPrefSEPUATMode_Type()
)
terrestrialPrefSEPUATMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPUATMode.setStatus("current")
_TerrestrialPrefSEPN_Type = Unsigned32
_TerrestrialPrefSEPN_Object = MibTableColumn
terrestrialPrefSEPN = _TerrestrialPrefSEPN_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 38),
    _TerrestrialPrefSEPN_Type()
)
terrestrialPrefSEPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPN.setStatus("current")
_TerrestrialPrefSEPT_Type = FloatingPoint
_TerrestrialPrefSEPT_Object = MibTableColumn
terrestrialPrefSEPT = _TerrestrialPrefSEPT_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 39),
    _TerrestrialPrefSEPT_Type()
)
terrestrialPrefSEPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPT.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSEPT.setUnits("second")
_TerrestrialPrefSEPM_Type = Unsigned32
_TerrestrialPrefSEPM_Object = MibTableColumn
terrestrialPrefSEPM = _TerrestrialPrefSEPM_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 40),
    _TerrestrialPrefSEPM_Type()
)
terrestrialPrefSEPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPM.setStatus("current")
_TerrestrialPrefSEPTI_Type = FloatingPoint
_TerrestrialPrefSEPTI_Object = MibTableColumn
terrestrialPrefSEPTI = _TerrestrialPrefSEPTI_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 41),
    _TerrestrialPrefSEPTI_Type()
)
terrestrialPrefSEPTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPTI.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSEPTI.setUnits("second")
_TerrestrialPrefSEPEBPerCent_Type = FloatingPoint
_TerrestrialPrefSEPEBPerCent_Object = MibTableColumn
terrestrialPrefSEPEBPerCent = _TerrestrialPrefSEPEBPerCent_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 42),
    _TerrestrialPrefSEPEBPerCent_Type()
)
terrestrialPrefSEPEBPerCent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPEBPerCent.setStatus("current")
_TerrestrialPrefSEPMeasurementInterval_Type = FloatingPoint
_TerrestrialPrefSEPMeasurementInterval_Object = MibTableColumn
terrestrialPrefSEPMeasurementInterval = _TerrestrialPrefSEPMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 9, 100, 1, 43),
    _TerrestrialPrefSEPMeasurementInterval_Type()
)
terrestrialPrefSEPMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terrestrialPrefSEPMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    terrestrialPrefSEPMeasurementInterval.setUnits("second")
_Tr101290Conformance_ObjectIdentity = ObjectIdentity
tr101290Conformance = _Tr101290Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3)
)
_Tr101290Compliances_ObjectIdentity = ObjectIdentity
tr101290Compliances = _Tr101290Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 1)
)
_Tr101290ObjectGroups_ObjectIdentity = ObjectIdentity
tr101290ObjectGroups = _Tr101290ObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2)
)

# Managed Objects groups

groupControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 1)
)
groupControl.setObjects(
      *(("DVB-MGTR101290-MIB", "controlNow"),
        ("DVB-MGTR101290-MIB", "controlEventPersistence"),
        ("DVB-MGTR101290-MIB", "rfSystemDelivery"),
        ("DVB-MGTR101290-MIB", "controlSynchronizedTime"))
)
if mibBuilder.loadTexts:
    groupControl.setStatus("current")

groupTrapControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 2)
)
groupTrapControl.setObjects(
      *(("DVB-MGTR101290-MIB", "trapControlOID"),
        ("DVB-MGTR101290-MIB", "trapControlGenerationTime"),
        ("DVB-MGTR101290-MIB", "trapControlMeasurementValue"),
        ("DVB-MGTR101290-MIB", "trapControlRateStatus"),
        ("DVB-MGTR101290-MIB", "trapControlPeriod"),
        ("DVB-MGTR101290-MIB", "trapControlFailureSummary"),
        ("DVB-MGTR101290-MIB", "trapInput"))
)
if mibBuilder.loadTexts:
    groupTrapControl.setStatus("current")

groupCapability = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 4)
)
groupCapability.setObjects(
      *(("DVB-MGTR101290-MIB", "capabilityMIBRevision"),
        ("DVB-MGTR101290-MIB", "capabilityTSGroup"),
        ("DVB-MGTR101290-MIB", "capabilityTSAvailability"),
        ("DVB-MGTR101290-MIB", "capabilityTSPollInterval"),
        ("DVB-MGTR101290-MIB", "capabilityCableSatGroup"),
        ("DVB-MGTR101290-MIB", "capabilityCableSatAvailability"),
        ("DVB-MGTR101290-MIB", "capabilityCableSatPollInterval"),
        ("DVB-MGTR101290-MIB", "capabilityCableGroup"),
        ("DVB-MGTR101290-MIB", "capabilityCableAvailability"),
        ("DVB-MGTR101290-MIB", "capabilityCablePollInterval"),
        ("DVB-MGTR101290-MIB", "capabilitySatelliteGroup"),
        ("DVB-MGTR101290-MIB", "capabilitySatelliteAvailability"),
        ("DVB-MGTR101290-MIB", "capabilitySatellitePollInterval"),
        ("DVB-MGTR101290-MIB", "capabilityTerrestrialGroup"),
        ("DVB-MGTR101290-MIB", "capabilityTerrestrialAvailability"),
        ("DVB-MGTR101290-MIB", "capabilityTerrestrialPollInterval"))
)
if mibBuilder.loadTexts:
    groupCapability.setStatus("current")

groupTransportStream = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 5)
)
groupTransportStream.setObjects(
      *(("DVB-MGTR101290-MIB", "tsTestsSummaryState"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryEnable"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryCounter"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryCounterReset"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryLatestError"),
        ("DVB-MGTR101290-MIB", "tsTestsSummaryActiveTime"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDRowStatus"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDState"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDEnable"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDCounter"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDCounterReset"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDLatestError"),
        ("DVB-MGTR101290-MIB", "tsTestsPIDActiveTime"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefTransitionDuration"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPATSectionIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPMTSectionIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefReferredIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPCRIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPCRDiscontinuityMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPCRInaccuracyMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPTSIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefNITActualIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefNITActualIntervalMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefNITOtherIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSIGapMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefNITTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefBATTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSDTActualTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSDTOtherTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITPFActualTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITPFOtherTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITSActualNearTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITSActualFarTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITSOtherNearTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITSOtherFarTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefTxTTableIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSDTActualIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSDTActualIntervalMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefSDTOtherIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITActualIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITActualIntervalMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefEITOtherIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefRSTIntervalMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefTDTIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefTDTIntervalMin"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPIDRowStatus"),
        ("DVB-MGTR101290-MIB", "tsTestsPrefPIDReferredIntervalMax"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementRowStatus"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementEnable"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementCounter"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementCounterReset"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementLatestError"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementActiveTime"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsPcrMeasurementValue"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateState"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateEnable"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateCounter"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateCounterReset"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateLatestError"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateActiveTime"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateValue"),
        ("DVB-MGTR101290-MIB", "tsTransportStreamBitRateNomenclature"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateRowStatus"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateState"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateEnable"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateCounter"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateCounterReset"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateLatestError"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateActiveTime"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateValue"),
        ("DVB-MGTR101290-MIB", "tsServiceBitRateNomenclature"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateRowStatus"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateState"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateEnable"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateCounter"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateCounterReset"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateLatestError"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateActiveTime"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateValue"),
        ("DVB-MGTR101290-MIB", "tsPIDBitRateNomenclature"),
        ("DVB-MGTR101290-MIB", "tsConsistencyState"),
        ("DVB-MGTR101290-MIB", "tsConsistencyEnable"),
        ("DVB-MGTR101290-MIB", "tsConsistencyCounter"),
        ("DVB-MGTR101290-MIB", "tsConsistencyCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsConsistencyCounterReset"),
        ("DVB-MGTR101290-MIB", "tsConsistencyLatestError"),
        ("DVB-MGTR101290-MIB", "tsConsistencyActiveTime"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPCRDemarcationFrequency"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPCRFOMax"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPCRDRMax"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPCROJMax"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefTSBitRateTau"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefTSBitRateN"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefTSBitRateElement"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefTSBitRateMin"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefTSBitRateMax"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllServiceBitRateTau"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllServiceBitRateN"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllServiceBitRateElement"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllPIDBitRateTau"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllPIDBitRateN"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefAllPIDBitRateElement"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefExpectedTSID"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceRowStatus"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceBitRateTau"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceBitRateN"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceBitRateElement"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceBitRateMin"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefServiceBitRateMax"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDRowStatus"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDBitRateTau"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDBitRateN"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDBitRateElement"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDBitRateMin"),
        ("DVB-MGTR101290-MIB", "tsMeasurePrefPIDBitRateMax"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceState"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceEnable"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceCounter"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceCounterReset"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceLatestError"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceActiveTime"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceMeasurementState"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceError"),
        ("DVB-MGTR101290-MIB", "tsServicePerformanceErrorRatio"),
        ("DVB-MGTR101290-MIB", "tsSPPrefDeltaT"),
        ("DVB-MGTR101290-MIB", "tsSPPrefEvaluationTime"),
        ("DVB-MGTR101290-MIB", "tsSPPrefThreshold"))
)
if mibBuilder.loadTexts:
    groupTransportStream.setStatus("current")

groupCable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 6)
)
groupCable.setObjects(
      *(("DVB-MGTR101290-MIB", "sysAvailabilityTestState"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityEnable"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounter"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounterReset"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityLatestError"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityActiveTime"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityMeasurementState"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityUnavailableTime"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityRatio"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityInSETI"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityTestState"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityEnable"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounter"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounterReset"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityLatestError"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityActiveTime"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityMeasurementState"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityUnavailableTime"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityRatio"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityInSUTI"),
        ("DVB-MGTR101290-MIB", "berRSinServiceTestState"),
        ("DVB-MGTR101290-MIB", "berRSinServiceEnable"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounter"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounterReset"),
        ("DVB-MGTR101290-MIB", "berRSinServiceLatestError"),
        ("DVB-MGTR101290-MIB", "berRSinServiceActiveTime"),
        ("DVB-MGTR101290-MIB", "berRSinServiceMeasurementState"),
        ("DVB-MGTR101290-MIB", "berRSinServiceValue"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerTestState"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerEnable"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounter"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounterReset"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerLatestError"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerActiveTime"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerMeasurementState"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerValue"),
        ("DVB-MGTR101290-MIB", "noisePowerTestState"),
        ("DVB-MGTR101290-MIB", "noisePowerEnable"),
        ("DVB-MGTR101290-MIB", "noisePowerCounter"),
        ("DVB-MGTR101290-MIB", "noisePowerCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "noisePowerCounterReset"),
        ("DVB-MGTR101290-MIB", "noisePowerLatestError"),
        ("DVB-MGTR101290-MIB", "noisePowerActiveTime"),
        ("DVB-MGTR101290-MIB", "noisePowerMeasurementState"),
        ("DVB-MGTR101290-MIB", "noisePowerValue"),
        ("DVB-MGTR101290-MIB", "merCSTestState"),
        ("DVB-MGTR101290-MIB", "merCSEnable"),
        ("DVB-MGTR101290-MIB", "merCSCounter"),
        ("DVB-MGTR101290-MIB", "merCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "merCSCounterReset"),
        ("DVB-MGTR101290-MIB", "merCSLatestError"),
        ("DVB-MGTR101290-MIB", "merCSActiveTime"),
        ("DVB-MGTR101290-MIB", "merCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "merCSValue"),
        ("DVB-MGTR101290-MIB", "steMeanCSTestState"),
        ("DVB-MGTR101290-MIB", "steMeanCSEnable"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounter"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounterReset"),
        ("DVB-MGTR101290-MIB", "steMeanCSLatestError"),
        ("DVB-MGTR101290-MIB", "steMeanCSActiveTime"),
        ("DVB-MGTR101290-MIB", "steMeanCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "steMeanCSValue"),
        ("DVB-MGTR101290-MIB", "steDeviationCSTestState"),
        ("DVB-MGTR101290-MIB", "steDeviationCSEnable"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounter"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounterReset"),
        ("DVB-MGTR101290-MIB", "steDeviationCSLatestError"),
        ("DVB-MGTR101290-MIB", "steDeviationCSActiveTime"),
        ("DVB-MGTR101290-MIB", "steDeviationCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "steDeviationCSValue"),
        ("DVB-MGTR101290-MIB", "csCSTestState"),
        ("DVB-MGTR101290-MIB", "csCSEnable"),
        ("DVB-MGTR101290-MIB", "csCSCounter"),
        ("DVB-MGTR101290-MIB", "csCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "csCSCounterReset"),
        ("DVB-MGTR101290-MIB", "csCSLatestError"),
        ("DVB-MGTR101290-MIB", "csCSActiveTime"),
        ("DVB-MGTR101290-MIB", "csCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "csCSValue"),
        ("DVB-MGTR101290-MIB", "aiCSTestState"),
        ("DVB-MGTR101290-MIB", "aiCSEnable"),
        ("DVB-MGTR101290-MIB", "aiCSCounter"),
        ("DVB-MGTR101290-MIB", "aiCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "aiCSCounterReset"),
        ("DVB-MGTR101290-MIB", "aiCSLatestError"),
        ("DVB-MGTR101290-MIB", "aiCSActiveTime"),
        ("DVB-MGTR101290-MIB", "aiCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "aiCSValue"),
        ("DVB-MGTR101290-MIB", "qeCSTestState"),
        ("DVB-MGTR101290-MIB", "qeCSEnable"),
        ("DVB-MGTR101290-MIB", "qeCSCounter"),
        ("DVB-MGTR101290-MIB", "qeCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "qeCSCounterReset"),
        ("DVB-MGTR101290-MIB", "qeCSLatestError"),
        ("DVB-MGTR101290-MIB", "qeCSActiveTime"),
        ("DVB-MGTR101290-MIB", "qeCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "qeCSValue"),
        ("DVB-MGTR101290-MIB", "rteCSTestState"),
        ("DVB-MGTR101290-MIB", "rteCSEnable"),
        ("DVB-MGTR101290-MIB", "rteCSCounter"),
        ("DVB-MGTR101290-MIB", "rteCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rteCSCounterReset"),
        ("DVB-MGTR101290-MIB", "rteCSLatestError"),
        ("DVB-MGTR101290-MIB", "rteCSActiveTime"),
        ("DVB-MGTR101290-MIB", "rteCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "rteCSValue"),
        ("DVB-MGTR101290-MIB", "ciCSTestState"),
        ("DVB-MGTR101290-MIB", "ciCSEnable"),
        ("DVB-MGTR101290-MIB", "ciCSCounter"),
        ("DVB-MGTR101290-MIB", "ciCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "ciCSCounterReset"),
        ("DVB-MGTR101290-MIB", "ciCSLatestError"),
        ("DVB-MGTR101290-MIB", "ciCSActiveTime"),
        ("DVB-MGTR101290-MIB", "ciCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "ciCSValue"),
        ("DVB-MGTR101290-MIB", "pjCSTestState"),
        ("DVB-MGTR101290-MIB", "pjCSEnable"),
        ("DVB-MGTR101290-MIB", "pjCSCounter"),
        ("DVB-MGTR101290-MIB", "pjCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "pjCSCounterReset"),
        ("DVB-MGTR101290-MIB", "pjCSLatestError"),
        ("DVB-MGTR101290-MIB", "pjCSActiveTime"),
        ("DVB-MGTR101290-MIB", "pjCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "pjCSValue"),
        ("DVB-MGTR101290-MIB", "snrCSTestState"),
        ("DVB-MGTR101290-MIB", "snrCSEnable"),
        ("DVB-MGTR101290-MIB", "snrCSCounter"),
        ("DVB-MGTR101290-MIB", "snrCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "snrCSCounterReset"),
        ("DVB-MGTR101290-MIB", "snrCSLatestError"),
        ("DVB-MGTR101290-MIB", "snrCSActiveTime"),
        ("DVB-MGTR101290-MIB", "snrCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "snrCSValue"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCentreFrequency"),
        ("DVB-MGTR101290-MIB", "cableSatPrefModulation"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailUATMode"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailN"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailT"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailM"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailTI"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailEBPerCent"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailTotalTime"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailUATMode"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailN"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailT"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailM"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailTI"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailUPPerCent"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailTotalTime"),
        ("DVB-MGTR101290-MIB", "cableSatPrefBERMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSignalPowerMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSignalPowerMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefNoisePowerMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefMerCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSteMeanCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSteDeviationCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCsCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefAiCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefQeCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefRteCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCiCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefPjCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSnrCSMin"),
        ("DVB-MGTR101290-MIB", "noiseMarginTestState"),
        ("DVB-MGTR101290-MIB", "noiseMarginEnable"),
        ("DVB-MGTR101290-MIB", "noiseMarginCounter"),
        ("DVB-MGTR101290-MIB", "noiseMarginCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "noiseMarginCounterReset"),
        ("DVB-MGTR101290-MIB", "noiseMarginLatestError"),
        ("DVB-MGTR101290-MIB", "noiseMarginActiveTime"),
        ("DVB-MGTR101290-MIB", "noiseMarginMeasurementState"),
        ("DVB-MGTR101290-MIB", "noiseMarginValue"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginTestState"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginEnable"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginCounter"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginCounterReset"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginLatestError"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginActiveTime"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginMeasurementState"),
        ("DVB-MGTR101290-MIB", "estNoiseMarginValue"),
        ("DVB-MGTR101290-MIB", "signQualMarTTestState"),
        ("DVB-MGTR101290-MIB", "signQualMarTEnable"),
        ("DVB-MGTR101290-MIB", "signQualMarTCounter"),
        ("DVB-MGTR101290-MIB", "signQualMarTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "signQualMarTCounterReset"),
        ("DVB-MGTR101290-MIB", "signQualMarTLatestError"),
        ("DVB-MGTR101290-MIB", "signQualMarTActiveTime"),
        ("DVB-MGTR101290-MIB", "eNDCTestState"),
        ("DVB-MGTR101290-MIB", "eNDCEnable"),
        ("DVB-MGTR101290-MIB", "eNDCCounter"),
        ("DVB-MGTR101290-MIB", "eNDCCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "eNDCCounterReset"),
        ("DVB-MGTR101290-MIB", "eNDCLatestError"),
        ("DVB-MGTR101290-MIB", "eNDCActiveTime"),
        ("DVB-MGTR101290-MIB", "eNDCMeasurementState"),
        ("DVB-MGTR101290-MIB", "eNDCValue"),
        ("DVB-MGTR101290-MIB", "outBandEmissTestState"),
        ("DVB-MGTR101290-MIB", "outBandEmissEnable"),
        ("DVB-MGTR101290-MIB", "outBandEmissCounter"),
        ("DVB-MGTR101290-MIB", "outBandEmissCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "outBandEmissCounterReset"),
        ("DVB-MGTR101290-MIB", "outBandEmissLatestError"),
        ("DVB-MGTR101290-MIB", "outBandEmissActiveTime"),
        ("DVB-MGTR101290-MIB", "cablePrefNoiseMarginMin"),
        ("DVB-MGTR101290-MIB", "cablePrefEstNoiseMarginMin"),
        ("DVB-MGTR101290-MIB", "cablePrefSignQualBoxSize"),
        ("DVB-MGTR101290-MIB", "cablePrefSignQualPercentMax"),
        ("DVB-MGTR101290-MIB", "cablePrefENDBER"),
        ("DVB-MGTR101290-MIB", "cablePrefENDCtoNSpecified"),
        ("DVB-MGTR101290-MIB", "cablePrefENDIdeal"),
        ("DVB-MGTR101290-MIB", "cablePrefENDMax"))
)
if mibBuilder.loadTexts:
    groupCable.setStatus("current")

groupSatellite = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 7)
)
groupSatellite.setObjects(
      *(("DVB-MGTR101290-MIB", "sysAvailabilityTestState"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityEnable"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounter"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityCounterReset"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityLatestError"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityActiveTime"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityMeasurementState"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityUnavailableTime"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityRatio"),
        ("DVB-MGTR101290-MIB", "sysAvailabilityInSETI"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityTestState"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityEnable"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounter"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityCounterReset"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityLatestError"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityActiveTime"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityMeasurementState"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityUnavailableTime"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityRatio"),
        ("DVB-MGTR101290-MIB", "linkAvailabilityInSUTI"),
        ("DVB-MGTR101290-MIB", "berRSinServiceTestState"),
        ("DVB-MGTR101290-MIB", "berRSinServiceEnable"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounter"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berRSinServiceCounterReset"),
        ("DVB-MGTR101290-MIB", "berRSinServiceLatestError"),
        ("DVB-MGTR101290-MIB", "berRSinServiceActiveTime"),
        ("DVB-MGTR101290-MIB", "berRSinServiceMeasurementState"),
        ("DVB-MGTR101290-MIB", "berRSinServiceValue"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerTestState"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerEnable"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounter"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerCounterReset"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerLatestError"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerActiveTime"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerMeasurementState"),
        ("DVB-MGTR101290-MIB", "rfIFsignalPowerValue"),
        ("DVB-MGTR101290-MIB", "noisePowerTestState"),
        ("DVB-MGTR101290-MIB", "noisePowerEnable"),
        ("DVB-MGTR101290-MIB", "noisePowerCounter"),
        ("DVB-MGTR101290-MIB", "noisePowerCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "noisePowerCounterReset"),
        ("DVB-MGTR101290-MIB", "noisePowerLatestError"),
        ("DVB-MGTR101290-MIB", "noisePowerActiveTime"),
        ("DVB-MGTR101290-MIB", "noisePowerMeasurementState"),
        ("DVB-MGTR101290-MIB", "noisePowerValue"),
        ("DVB-MGTR101290-MIB", "merCSTestState"),
        ("DVB-MGTR101290-MIB", "merCSEnable"),
        ("DVB-MGTR101290-MIB", "merCSCounter"),
        ("DVB-MGTR101290-MIB", "merCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "merCSCounterReset"),
        ("DVB-MGTR101290-MIB", "merCSLatestError"),
        ("DVB-MGTR101290-MIB", "merCSActiveTime"),
        ("DVB-MGTR101290-MIB", "merCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "merCSValue"),
        ("DVB-MGTR101290-MIB", "steMeanCSTestState"),
        ("DVB-MGTR101290-MIB", "steMeanCSEnable"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounter"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steMeanCSCounterReset"),
        ("DVB-MGTR101290-MIB", "steMeanCSLatestError"),
        ("DVB-MGTR101290-MIB", "steMeanCSActiveTime"),
        ("DVB-MGTR101290-MIB", "steMeanCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "steMeanCSValue"),
        ("DVB-MGTR101290-MIB", "steDeviationCSTestState"),
        ("DVB-MGTR101290-MIB", "steDeviationCSEnable"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounter"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steDeviationCSCounterReset"),
        ("DVB-MGTR101290-MIB", "steDeviationCSLatestError"),
        ("DVB-MGTR101290-MIB", "steDeviationCSActiveTime"),
        ("DVB-MGTR101290-MIB", "steDeviationCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "steDeviationCSValue"),
        ("DVB-MGTR101290-MIB", "csCSTestState"),
        ("DVB-MGTR101290-MIB", "csCSEnable"),
        ("DVB-MGTR101290-MIB", "csCSCounter"),
        ("DVB-MGTR101290-MIB", "csCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "csCSCounterReset"),
        ("DVB-MGTR101290-MIB", "csCSLatestError"),
        ("DVB-MGTR101290-MIB", "csCSActiveTime"),
        ("DVB-MGTR101290-MIB", "csCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "csCSValue"),
        ("DVB-MGTR101290-MIB", "aiCSTestState"),
        ("DVB-MGTR101290-MIB", "aiCSEnable"),
        ("DVB-MGTR101290-MIB", "aiCSCounter"),
        ("DVB-MGTR101290-MIB", "aiCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "aiCSCounterReset"),
        ("DVB-MGTR101290-MIB", "aiCSLatestError"),
        ("DVB-MGTR101290-MIB", "aiCSActiveTime"),
        ("DVB-MGTR101290-MIB", "aiCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "aiCSValue"),
        ("DVB-MGTR101290-MIB", "qeCSTestState"),
        ("DVB-MGTR101290-MIB", "qeCSEnable"),
        ("DVB-MGTR101290-MIB", "qeCSCounter"),
        ("DVB-MGTR101290-MIB", "qeCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "qeCSCounterReset"),
        ("DVB-MGTR101290-MIB", "qeCSLatestError"),
        ("DVB-MGTR101290-MIB", "qeCSActiveTime"),
        ("DVB-MGTR101290-MIB", "qeCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "qeCSValue"),
        ("DVB-MGTR101290-MIB", "rteCSTestState"),
        ("DVB-MGTR101290-MIB", "rteCSEnable"),
        ("DVB-MGTR101290-MIB", "rteCSCounter"),
        ("DVB-MGTR101290-MIB", "rteCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rteCSCounterReset"),
        ("DVB-MGTR101290-MIB", "rteCSLatestError"),
        ("DVB-MGTR101290-MIB", "rteCSActiveTime"),
        ("DVB-MGTR101290-MIB", "rteCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "rteCSValue"),
        ("DVB-MGTR101290-MIB", "ciCSTestState"),
        ("DVB-MGTR101290-MIB", "ciCSEnable"),
        ("DVB-MGTR101290-MIB", "ciCSCounter"),
        ("DVB-MGTR101290-MIB", "ciCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "ciCSCounterReset"),
        ("DVB-MGTR101290-MIB", "ciCSLatestError"),
        ("DVB-MGTR101290-MIB", "ciCSActiveTime"),
        ("DVB-MGTR101290-MIB", "ciCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "ciCSValue"),
        ("DVB-MGTR101290-MIB", "pjCSTestState"),
        ("DVB-MGTR101290-MIB", "pjCSEnable"),
        ("DVB-MGTR101290-MIB", "pjCSCounter"),
        ("DVB-MGTR101290-MIB", "pjCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "pjCSCounterReset"),
        ("DVB-MGTR101290-MIB", "pjCSLatestError"),
        ("DVB-MGTR101290-MIB", "pjCSActiveTime"),
        ("DVB-MGTR101290-MIB", "pjCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "pjCSValue"),
        ("DVB-MGTR101290-MIB", "snrCSTestState"),
        ("DVB-MGTR101290-MIB", "snrCSEnable"),
        ("DVB-MGTR101290-MIB", "snrCSCounter"),
        ("DVB-MGTR101290-MIB", "snrCSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "snrCSCounterReset"),
        ("DVB-MGTR101290-MIB", "snrCSLatestError"),
        ("DVB-MGTR101290-MIB", "snrCSActiveTime"),
        ("DVB-MGTR101290-MIB", "snrCSMeasurementState"),
        ("DVB-MGTR101290-MIB", "snrCSValue"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCentreFrequency"),
        ("DVB-MGTR101290-MIB", "cableSatPrefModulation"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailUATMode"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailN"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailT"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailM"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailTI"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailEBPerCent"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSysAvailTotalTime"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailUATMode"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailN"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailT"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailM"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailTI"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailUPPerCent"),
        ("DVB-MGTR101290-MIB", "cableSatPrefLinkAvailTotalTime"),
        ("DVB-MGTR101290-MIB", "cableSatPrefBERMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSignalPowerMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSignalPowerMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefNoisePowerMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefMerCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSteMeanCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSteDeviationCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCsCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefAiCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefQeCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefRteCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefCiCSMin"),
        ("DVB-MGTR101290-MIB", "cableSatPrefPjCSMax"),
        ("DVB-MGTR101290-MIB", "cableSatPrefSnrCSMin"),
        ("DVB-MGTR101290-MIB", "berViterbiSTestState"),
        ("DVB-MGTR101290-MIB", "berViterbiSEnable"),
        ("DVB-MGTR101290-MIB", "berViterbiSCounter"),
        ("DVB-MGTR101290-MIB", "berViterbiSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berViterbiSCounterReset"),
        ("DVB-MGTR101290-MIB", "berViterbiSLatestError"),
        ("DVB-MGTR101290-MIB", "berViterbiSActiveTime"),
        ("DVB-MGTR101290-MIB", "berViterbiSMeasurementState"),
        ("DVB-MGTR101290-MIB", "berViterbiSIValue"),
        ("DVB-MGTR101290-MIB", "berViterbiSQValue"),
        ("DVB-MGTR101290-MIB", "berViterbiSMeasurementMethod"),
        ("DVB-MGTR101290-MIB", "ifSpectrumTestState"),
        ("DVB-MGTR101290-MIB", "ifSpectrumEnable"),
        ("DVB-MGTR101290-MIB", "ifSpectrumCounter"),
        ("DVB-MGTR101290-MIB", "ifSpectrumCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "ifSpectrumCounterReset"),
        ("DVB-MGTR101290-MIB", "ifSpectrumLatestError"),
        ("DVB-MGTR101290-MIB", "ifSpectrumActiveTime"),
        ("DVB-MGTR101290-MIB", "satellitePrefBERMax"))
)
if mibBuilder.loadTexts:
    groupSatellite.setStatus("current")

groupTerrestrial = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 8)
)
groupTerrestrial.setObjects(
      *(("DVB-MGTR101290-MIB", "rfAccuracyTestState"),
        ("DVB-MGTR101290-MIB", "rfAccuracyEnable"),
        ("DVB-MGTR101290-MIB", "rfAccuracyCounter"),
        ("DVB-MGTR101290-MIB", "rfAccuracyCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfAccuracyCounterReset"),
        ("DVB-MGTR101290-MIB", "rfAccuracyLatestError"),
        ("DVB-MGTR101290-MIB", "rfAccuracyActiveTime"),
        ("DVB-MGTR101290-MIB", "rfAccuracyMeasurementState"),
        ("DVB-MGTR101290-MIB", "rfAccuracyValue"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthTestState"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthEnable"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthCounter"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthCounterReset"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthLatestError"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthActiveTime"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthMeasurementState"),
        ("DVB-MGTR101290-MIB", "rfChannelWidthValue"),
        ("DVB-MGTR101290-MIB", "symbolLengthTestState"),
        ("DVB-MGTR101290-MIB", "symbolLengthEnable"),
        ("DVB-MGTR101290-MIB", "symbolLengthCounter"),
        ("DVB-MGTR101290-MIB", "symbolLengthCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "symbolLengthCounterReset"),
        ("DVB-MGTR101290-MIB", "symbolLengthLatestError"),
        ("DVB-MGTR101290-MIB", "symbolLengthActiveTime"),
        ("DVB-MGTR101290-MIB", "symbolLengthMeasurementState"),
        ("DVB-MGTR101290-MIB", "symbolLengthValue"),
        ("DVB-MGTR101290-MIB", "rfIfPowerTestState"),
        ("DVB-MGTR101290-MIB", "rfIfPowerEnable"),
        ("DVB-MGTR101290-MIB", "rfIfPowerCounter"),
        ("DVB-MGTR101290-MIB", "rfIfPowerCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfIfPowerCounterReset"),
        ("DVB-MGTR101290-MIB", "rfIfPowerLatestError"),
        ("DVB-MGTR101290-MIB", "rfIfPowerActiveTime"),
        ("DVB-MGTR101290-MIB", "rfIfPowerMeasurementState"),
        ("DVB-MGTR101290-MIB", "rfIfPowerValue"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumTestState"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumEnable"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumCounter"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumCounterReset"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumLatestError"),
        ("DVB-MGTR101290-MIB", "rfIfSpectrumActiveTime"),
        ("DVB-MGTR101290-MIB", "eNDTTestState"),
        ("DVB-MGTR101290-MIB", "eNDTEnable"),
        ("DVB-MGTR101290-MIB", "eNDTCounter"),
        ("DVB-MGTR101290-MIB", "eNDTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "eNDTCounterReset"),
        ("DVB-MGTR101290-MIB", "eNDTLatestError"),
        ("DVB-MGTR101290-MIB", "eNDTActiveTime"),
        ("DVB-MGTR101290-MIB", "eNDTMeasurementState"),
        ("DVB-MGTR101290-MIB", "eNDTValue"),
        ("DVB-MGTR101290-MIB", "eNFTTestState"),
        ("DVB-MGTR101290-MIB", "eNFTEnable"),
        ("DVB-MGTR101290-MIB", "eNFTCounter"),
        ("DVB-MGTR101290-MIB", "eNFTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "eNFTCounterReset"),
        ("DVB-MGTR101290-MIB", "eNFTLatestError"),
        ("DVB-MGTR101290-MIB", "eNFTActiveTime"),
        ("DVB-MGTR101290-MIB", "eNFTMeasurementState"),
        ("DVB-MGTR101290-MIB", "eNFTValue"),
        ("DVB-MGTR101290-MIB", "eNDTLPTestState"),
        ("DVB-MGTR101290-MIB", "eNDTLPEnable"),
        ("DVB-MGTR101290-MIB", "eNDTLPCounter"),
        ("DVB-MGTR101290-MIB", "eNDTLPCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "eNDTLPCounterReset"),
        ("DVB-MGTR101290-MIB", "eNDTLPLatestError"),
        ("DVB-MGTR101290-MIB", "eNDTLPActiveTime"),
        ("DVB-MGTR101290-MIB", "eNDTLPMeasurementState"),
        ("DVB-MGTR101290-MIB", "eNDTLPValue"),
        ("DVB-MGTR101290-MIB", "eNFTLPTestState"),
        ("DVB-MGTR101290-MIB", "eNFTLPEnable"),
        ("DVB-MGTR101290-MIB", "eNFTLPCounter"),
        ("DVB-MGTR101290-MIB", "eNFTLPCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "eNFTLPCounterReset"),
        ("DVB-MGTR101290-MIB", "eNFTLPLatestError"),
        ("DVB-MGTR101290-MIB", "eNFTLPActiveTime"),
        ("DVB-MGTR101290-MIB", "eNFTLPMeasurementState"),
        ("DVB-MGTR101290-MIB", "eNFTLPValue"),
        ("DVB-MGTR101290-MIB", "linearityTestState"),
        ("DVB-MGTR101290-MIB", "linearityEnable"),
        ("DVB-MGTR101290-MIB", "linearityCounter"),
        ("DVB-MGTR101290-MIB", "linearityCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "linearityCounterReset"),
        ("DVB-MGTR101290-MIB", "linearityLatestError"),
        ("DVB-MGTR101290-MIB", "linearityActiveTime"),
        ("DVB-MGTR101290-MIB", "linearityMeasurementState"),
        ("DVB-MGTR101290-MIB", "linearityValue"),
        ("DVB-MGTR101290-MIB", "berViterbiTTestState"),
        ("DVB-MGTR101290-MIB", "berViterbiTEnable"),
        ("DVB-MGTR101290-MIB", "berViterbiTCounter"),
        ("DVB-MGTR101290-MIB", "berViterbiTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berViterbiTCounterReset"),
        ("DVB-MGTR101290-MIB", "berViterbiTLatestError"),
        ("DVB-MGTR101290-MIB", "berViterbiTActiveTime"),
        ("DVB-MGTR101290-MIB", "berViterbiTMeasurementState"),
        ("DVB-MGTR101290-MIB", "berViterbiTValue"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPTestState"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPEnable"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPCounter"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPCounterReset"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPLatestError"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPActiveTime"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPMeasurementState"),
        ("DVB-MGTR101290-MIB", "berViterbiTLPValue"),
        ("DVB-MGTR101290-MIB", "berRSTestState"),
        ("DVB-MGTR101290-MIB", "berRSEnable"),
        ("DVB-MGTR101290-MIB", "berRSCounter"),
        ("DVB-MGTR101290-MIB", "berRSCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berRSCounterReset"),
        ("DVB-MGTR101290-MIB", "berRSLatestError"),
        ("DVB-MGTR101290-MIB", "berRSActiveTime"),
        ("DVB-MGTR101290-MIB", "berRSMeasurementState"),
        ("DVB-MGTR101290-MIB", "berRSValue"),
        ("DVB-MGTR101290-MIB", "berRSLPTestState"),
        ("DVB-MGTR101290-MIB", "berRSLPEnable"),
        ("DVB-MGTR101290-MIB", "berRSLPCounter"),
        ("DVB-MGTR101290-MIB", "berRSLPCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "berRSLPCounterReset"),
        ("DVB-MGTR101290-MIB", "berRSLPLatestError"),
        ("DVB-MGTR101290-MIB", "berRSLPActiveTime"),
        ("DVB-MGTR101290-MIB", "berRSLPMeasurementState"),
        ("DVB-MGTR101290-MIB", "berRSLPValue"),
        ("DVB-MGTR101290-MIB", "merTTestState"),
        ("DVB-MGTR101290-MIB", "merTEnable"),
        ("DVB-MGTR101290-MIB", "merTCounter"),
        ("DVB-MGTR101290-MIB", "merTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "merTCounterReset"),
        ("DVB-MGTR101290-MIB", "merTLatestError"),
        ("DVB-MGTR101290-MIB", "merTActiveTime"),
        ("DVB-MGTR101290-MIB", "merTMeasurementState"),
        ("DVB-MGTR101290-MIB", "merTValue"),
        ("DVB-MGTR101290-MIB", "steMeanTTestState"),
        ("DVB-MGTR101290-MIB", "steMeanTEnable"),
        ("DVB-MGTR101290-MIB", "steMeanTCounter"),
        ("DVB-MGTR101290-MIB", "steMeanTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steMeanTCounterReset"),
        ("DVB-MGTR101290-MIB", "steMeanTLatestError"),
        ("DVB-MGTR101290-MIB", "steMeanTActiveTime"),
        ("DVB-MGTR101290-MIB", "steMeanTMeasurementState"),
        ("DVB-MGTR101290-MIB", "steMeanTValue"),
        ("DVB-MGTR101290-MIB", "steDeviationTTestState"),
        ("DVB-MGTR101290-MIB", "steDeviationTEnable"),
        ("DVB-MGTR101290-MIB", "steDeviationTCounter"),
        ("DVB-MGTR101290-MIB", "steDeviationTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "steDeviationTCounterReset"),
        ("DVB-MGTR101290-MIB", "steDeviationTLatestError"),
        ("DVB-MGTR101290-MIB", "steDeviationTActiveTime"),
        ("DVB-MGTR101290-MIB", "steDeviationTMeasurementState"),
        ("DVB-MGTR101290-MIB", "steDeviationTValue"),
        ("DVB-MGTR101290-MIB", "csTTestState"),
        ("DVB-MGTR101290-MIB", "csTEnable"),
        ("DVB-MGTR101290-MIB", "csTCounter"),
        ("DVB-MGTR101290-MIB", "csTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "csTCounterReset"),
        ("DVB-MGTR101290-MIB", "csTLatestError"),
        ("DVB-MGTR101290-MIB", "csTActiveTime"),
        ("DVB-MGTR101290-MIB", "csTMeasurementState"),
        ("DVB-MGTR101290-MIB", "csTValue"),
        ("DVB-MGTR101290-MIB", "aiTTestState"),
        ("DVB-MGTR101290-MIB", "aiTEnable"),
        ("DVB-MGTR101290-MIB", "aiTCounter"),
        ("DVB-MGTR101290-MIB", "aiTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "aiTCounterReset"),
        ("DVB-MGTR101290-MIB", "aiTLatestError"),
        ("DVB-MGTR101290-MIB", "aiTActiveTime"),
        ("DVB-MGTR101290-MIB", "aiTMeasurementState"),
        ("DVB-MGTR101290-MIB", "aiTValue"),
        ("DVB-MGTR101290-MIB", "qeTTestState"),
        ("DVB-MGTR101290-MIB", "qeTEnable"),
        ("DVB-MGTR101290-MIB", "qeTCounter"),
        ("DVB-MGTR101290-MIB", "qeTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "qeTCounterReset"),
        ("DVB-MGTR101290-MIB", "qeTLatestError"),
        ("DVB-MGTR101290-MIB", "qeTActiveTime"),
        ("DVB-MGTR101290-MIB", "qeTMeasurementState"),
        ("DVB-MGTR101290-MIB", "qeTValue"),
        ("DVB-MGTR101290-MIB", "pjTTestState"),
        ("DVB-MGTR101290-MIB", "pjTEnable"),
        ("DVB-MGTR101290-MIB", "pjTCounter"),
        ("DVB-MGTR101290-MIB", "pjTCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "pjTCounterReset"),
        ("DVB-MGTR101290-MIB", "pjTLatestError"),
        ("DVB-MGTR101290-MIB", "pjTActiveTime"),
        ("DVB-MGTR101290-MIB", "pjTMeasurementState"),
        ("DVB-MGTR101290-MIB", "pjTValue"),
        ("DVB-MGTR101290-MIB", "mipSyntaxState"),
        ("DVB-MGTR101290-MIB", "mipSyntaxEnable"),
        ("DVB-MGTR101290-MIB", "mipSyntaxCounter"),
        ("DVB-MGTR101290-MIB", "mipSyntaxCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "mipSyntaxCounterReset"),
        ("DVB-MGTR101290-MIB", "mipSyntaxLatestError"),
        ("DVB-MGTR101290-MIB", "mipSyntaxActiveTime"),
        ("DVB-MGTR101290-MIB", "sepEtiTestState"),
        ("DVB-MGTR101290-MIB", "sepEtiEnable"),
        ("DVB-MGTR101290-MIB", "sepEtiCounter"),
        ("DVB-MGTR101290-MIB", "sepEtiCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "sepEtiCounterReset"),
        ("DVB-MGTR101290-MIB", "sepEtiLatestError"),
        ("DVB-MGTR101290-MIB", "sepEtiActiveTime"),
        ("DVB-MGTR101290-MIB", "sepEtiMeasurementState"),
        ("DVB-MGTR101290-MIB", "sepEtiValue"),
        ("DVB-MGTR101290-MIB", "sepSetiTestState"),
        ("DVB-MGTR101290-MIB", "sepSetiEnable"),
        ("DVB-MGTR101290-MIB", "sepSetiCounter"),
        ("DVB-MGTR101290-MIB", "sepSetiCounterDiscontinuity"),
        ("DVB-MGTR101290-MIB", "sepSetiCounterReset"),
        ("DVB-MGTR101290-MIB", "sepSetiLatestError"),
        ("DVB-MGTR101290-MIB", "sepSetiActiveTime"),
        ("DVB-MGTR101290-MIB", "sepSetiMeasurementState"),
        ("DVB-MGTR101290-MIB", "sepSetiValue"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefCentreFrequency"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefBandwidth"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefModulation"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefTransmissionMode"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefGuardInterval"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefHierarchical"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefCentreFreqExpected"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefCentreFreqLimit"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefChannelWidthLimit"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSymbolLengthLimit"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefPowerMin"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefPowerMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENDBER"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENDIdeal"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENDMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENFIdeal"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENFMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENDLPIdeal"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENDLPMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENFLPIdeal"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefENFLPMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefLinearityMin"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefBERViterbiMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefBERViterbiLPMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefBERRSMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefBERRSLPMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefMerTMin"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSteMeanMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSteDeviationMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefCsMin"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefAiMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefQeMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefPjMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefMIPTimingLimit"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefMIPDeviationMax"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPUATMode"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPN"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPT"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPM"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPTI"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPEBPerCent"),
        ("DVB-MGTR101290-MIB", "terrestrialPrefSEPMeasurementInterval"))
)
if mibBuilder.loadTexts:
    groupTerrestrial.setStatus("current")


# Notification objects

testFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 0, 1)
)
testFailTrap.setObjects(
      *(("DVB-MGTR101290-MIB", "trapControlOID"),
        ("DVB-MGTR101290-MIB", "trapControlGenerationTime"),
        ("DVB-MGTR101290-MIB", "trapControlFailureSummary"),
        ("DVB-MGTR101290-MIB", "trapInput"))
)
if mibBuilder.loadTexts:
    testFailTrap.setStatus(
        "current"
    )

measurementFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 0, 2)
)
measurementFailTrap.setObjects(
      *(("DVB-MGTR101290-MIB", "trapControlOID"),
        ("DVB-MGTR101290-MIB", "trapControlGenerationTime"),
        ("DVB-MGTR101290-MIB", "trapControlMeasurementValue"),
        ("DVB-MGTR101290-MIB", "trapControlFailureSummary"),
        ("DVB-MGTR101290-MIB", "trapInput"))
)
if mibBuilder.loadTexts:
    measurementFailTrap.setStatus(
        "current"
    )

measurementUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 1, 2, 0, 3)
)
measurementUnknownTrap.setObjects(
      *(("DVB-MGTR101290-MIB", "trapControlOID"),
        ("DVB-MGTR101290-MIB", "trapControlGenerationTime"),
        ("DVB-MGTR101290-MIB", "trapControlFailureSummary"),
        ("DVB-MGTR101290-MIB", "trapInput"))
)
if mibBuilder.loadTexts:
    measurementUnknownTrap.setStatus(
        "current"
    )


# Notifications groups

groupTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 2, 3)
)
groupTraps.setObjects(
      *(("DVB-MGTR101290-MIB", "testFailTrap"),
        ("DVB-MGTR101290-MIB", "measurementFailTrap"),
        ("DVB-MGTR101290-MIB", "measurementUnknownTrap"))
)
if mibBuilder.loadTexts:
    groupTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

complianceTransportStream = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    complianceTransportStream.setStatus(
        "current"
    )

complianceCable = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    complianceCable.setStatus(
        "current"
    )

complianceSatellite = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    complianceSatellite.setStatus(
        "current"
    )

complianceTerrestrial = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    complianceTerrestrial.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVB-MGTR101290-MIB",
    **{"ActiveTime": ActiveTime,
       "Availability": Availability,
       "BERMeasurementMethod": BERMeasurementMethod,
       "BitRateElement": BitRateElement,
       "DeliverySystemType": DeliverySystemType,
       "Enable": Enable,
       "FloatingPoint": FloatingPoint,
       "GroupAvailability": GroupAvailability,
       "GuardInterval": GuardInterval,
       "Hierarchy": Hierarchy,
       "IndexConsistencyTest": IndexConsistencyTest,
       "IndexMIPSyntaxTest": IndexMIPSyntaxTest,
       "IndexPCRMeasurement": IndexPCRMeasurement,
       "IndexServicePerformance": IndexServicePerformance,
       "IndexTransportStreamTest": IndexTransportStreamTest,
       "InputNumber": InputNumber,
       "MeasurementState": MeasurementState,
       "Modulation": Modulation,
       "PIDPlusOne": PIDPlusOne,
       "PollingInterval": PollingInterval,
       "RateStatus": RateStatus,
       "ServiceId": ServiceId,
       "TerrestrialTransmissionMode": TerrestrialTransmissionMode,
       "TestState": TestState,
       "TestSummary": TestSummary,
       "TransportStreamID": TransportStreamID,
       "UATMode": UATMode,
       "dvb": dvb,
       "mg": mg,
       "tr101290": tr101290,
       "tr101290Objects": tr101290Objects,
       "tr101290Control": tr101290Control,
       "controlNow": controlNow,
       "controlEventPersistence": controlEventPersistence,
       "controlRFSystemTable": controlRFSystemTable,
       "controlRFSystemEntry": controlRFSystemEntry,
       "rfSystemInputNumber": rfSystemInputNumber,
       "rfSystemDelivery": rfSystemDelivery,
       "controlSynchronizationTable": controlSynchronizationTable,
       "controlSynchronizationEntry": controlSynchronizationEntry,
       "controlSynchronizationInputNumber": controlSynchronizationInputNumber,
       "controlSynchronizedTime": controlSynchronizedTime,
       "tr101290Trap": tr101290Trap,
       "trapPrefix": trapPrefix,
       "testFailTrap": testFailTrap,
       "measurementFailTrap": measurementFailTrap,
       "measurementUnknownTrap": measurementUnknownTrap,
       "trapControlTable": trapControlTable,
       "trapControlEntry": trapControlEntry,
       "trapControlInputNumber": trapControlInputNumber,
       "trapControlOID": trapControlOID,
       "trapControlGenerationTime": trapControlGenerationTime,
       "trapControlMeasurementValue": trapControlMeasurementValue,
       "trapControlRateStatus": trapControlRateStatus,
       "trapControlPeriod": trapControlPeriod,
       "trapControlFailureSummary": trapControlFailureSummary,
       "trapInput": trapInput,
       "tr101290Capability": tr101290Capability,
       "capabilityMIBRevision": capabilityMIBRevision,
       "capabilityTS": capabilityTS,
       "capabilityTSGroup": capabilityTSGroup,
       "capabilityTSTable": capabilityTSTable,
       "capabilityTSEntry": capabilityTSEntry,
       "capabilityTSOID": capabilityTSOID,
       "capabilityTSAvailability": capabilityTSAvailability,
       "capabilityTSPollInterval": capabilityTSPollInterval,
       "capabilityCableSat": capabilityCableSat,
       "capabilityCableSatGroup": capabilityCableSatGroup,
       "capabilityCableSatTable": capabilityCableSatTable,
       "capabilityCableSatEntry": capabilityCableSatEntry,
       "capabilityCableSatOID": capabilityCableSatOID,
       "capabilityCableSatAvailability": capabilityCableSatAvailability,
       "capabilityCableSatPollInterval": capabilityCableSatPollInterval,
       "capabilityCable": capabilityCable,
       "capabilityCableGroup": capabilityCableGroup,
       "capabilityCableTable": capabilityCableTable,
       "capabilityCableEntry": capabilityCableEntry,
       "capabilityCableOID": capabilityCableOID,
       "capabilityCableAvailability": capabilityCableAvailability,
       "capabilityCablePollInterval": capabilityCablePollInterval,
       "capabilitySatellite": capabilitySatellite,
       "capabilitySatelliteGroup": capabilitySatelliteGroup,
       "capabilitySatelliteTable": capabilitySatelliteTable,
       "capabilitySatelliteEntry": capabilitySatelliteEntry,
       "capabilitySatelliteOID": capabilitySatelliteOID,
       "capabilitySatelliteAvailability": capabilitySatelliteAvailability,
       "capabilitySatellitePollInterval": capabilitySatellitePollInterval,
       "capabilityTerrestrial": capabilityTerrestrial,
       "capabilityTerrestrialGroup": capabilityTerrestrialGroup,
       "capabilityTerrestrialTable": capabilityTerrestrialTable,
       "capabilityTerrestrialEntry": capabilityTerrestrialEntry,
       "capabilityTerrestrialOID": capabilityTerrestrialOID,
       "capabilityTerrestrialAvailability": capabilityTerrestrialAvailability,
       "capabilityTerrestrialPollInterval": capabilityTerrestrialPollInterval,
       "tr101290TS": tr101290TS,
       "tsTests": tsTests,
       "tsTestsSummaryTable": tsTestsSummaryTable,
       "tsTestsSummaryEntry": tsTestsSummaryEntry,
       "tsTestsSummaryInputNumber": tsTestsSummaryInputNumber,
       "tsTestsSummaryTestNumber": tsTestsSummaryTestNumber,
       "tsTestsSummaryState": tsTestsSummaryState,
       "tsTestsSummaryEnable": tsTestsSummaryEnable,
       "tsTestsSummaryCounter": tsTestsSummaryCounter,
       "tsTestsSummaryCounterDiscontinuity": tsTestsSummaryCounterDiscontinuity,
       "tsTestsSummaryCounterReset": tsTestsSummaryCounterReset,
       "tsTestsSummaryLatestError": tsTestsSummaryLatestError,
       "tsTestsSummaryActiveTime": tsTestsSummaryActiveTime,
       "tsTestsPIDTable": tsTestsPIDTable,
       "tsTestsPIDEntry": tsTestsPIDEntry,
       "tsTestsPIDInputNumber": tsTestsPIDInputNumber,
       "tsTestsPIDPID": tsTestsPIDPID,
       "tsTestsPIDTestNumber": tsTestsPIDTestNumber,
       "tsTestsPIDRowStatus": tsTestsPIDRowStatus,
       "tsTestsPIDState": tsTestsPIDState,
       "tsTestsPIDEnable": tsTestsPIDEnable,
       "tsTestsPIDCounter": tsTestsPIDCounter,
       "tsTestsPIDCounterDiscontinuity": tsTestsPIDCounterDiscontinuity,
       "tsTestsPIDCounterReset": tsTestsPIDCounterReset,
       "tsTestsPIDLatestError": tsTestsPIDLatestError,
       "tsTestsPIDActiveTime": tsTestsPIDActiveTime,
       "tsTestsPreferences": tsTestsPreferences,
       "tsTestsPreferencesTable": tsTestsPreferencesTable,
       "tsTestsPreferencesEntry": tsTestsPreferencesEntry,
       "tsTestsPrefInputNumber": tsTestsPrefInputNumber,
       "tsTestsPrefTransitionDuration": tsTestsPrefTransitionDuration,
       "tsTestsPrefPATSectionIntervalMax": tsTestsPrefPATSectionIntervalMax,
       "tsTestsPrefPMTSectionIntervalMax": tsTestsPrefPMTSectionIntervalMax,
       "tsTestsPrefReferredIntervalMax": tsTestsPrefReferredIntervalMax,
       "tsTestsPrefPCRIntervalMax": tsTestsPrefPCRIntervalMax,
       "tsTestsPrefPCRDiscontinuityMax": tsTestsPrefPCRDiscontinuityMax,
       "tsTestsPrefPCRInaccuracyMax": tsTestsPrefPCRInaccuracyMax,
       "tsTestsPrefPTSIntervalMax": tsTestsPrefPTSIntervalMax,
       "tsTestsPrefNITActualIntervalMax": tsTestsPrefNITActualIntervalMax,
       "tsTestsPrefNITActualIntervalMin": tsTestsPrefNITActualIntervalMin,
       "tsTestsPrefNITOtherIntervalMax": tsTestsPrefNITOtherIntervalMax,
       "tsTestsPrefSIGapMin": tsTestsPrefSIGapMin,
       "tsTestsPrefNITTableIntervalMax": tsTestsPrefNITTableIntervalMax,
       "tsTestsPrefBATTableIntervalMax": tsTestsPrefBATTableIntervalMax,
       "tsTestsPrefSDTActualTableIntervalMax": tsTestsPrefSDTActualTableIntervalMax,
       "tsTestsPrefSDTOtherTableIntervalMax": tsTestsPrefSDTOtherTableIntervalMax,
       "tsTestsPrefEITPFActualTableIntervalMax": tsTestsPrefEITPFActualTableIntervalMax,
       "tsTestsPrefEITPFOtherTableIntervalMax": tsTestsPrefEITPFOtherTableIntervalMax,
       "tsTestsPrefEITSActualNearTableIntervalMax": tsTestsPrefEITSActualNearTableIntervalMax,
       "tsTestsPrefEITSActualFarTableIntervalMax": tsTestsPrefEITSActualFarTableIntervalMax,
       "tsTestsPrefEITSOtherNearTableIntervalMax": tsTestsPrefEITSOtherNearTableIntervalMax,
       "tsTestsPrefEITSOtherFarTableIntervalMax": tsTestsPrefEITSOtherFarTableIntervalMax,
       "tsTestsPrefTxTTableIntervalMax": tsTestsPrefTxTTableIntervalMax,
       "tsTestsPrefSDTActualIntervalMax": tsTestsPrefSDTActualIntervalMax,
       "tsTestsPrefSDTActualIntervalMin": tsTestsPrefSDTActualIntervalMin,
       "tsTestsPrefSDTOtherIntervalMax": tsTestsPrefSDTOtherIntervalMax,
       "tsTestsPrefEITActualIntervalMax": tsTestsPrefEITActualIntervalMax,
       "tsTestsPrefEITActualIntervalMin": tsTestsPrefEITActualIntervalMin,
       "tsTestsPrefEITOtherIntervalMax": tsTestsPrefEITOtherIntervalMax,
       "tsTestsPrefRSTIntervalMin": tsTestsPrefRSTIntervalMin,
       "tsTestsPrefTDTIntervalMax": tsTestsPrefTDTIntervalMax,
       "tsTestsPrefTDTIntervalMin": tsTestsPrefTDTIntervalMin,
       "tsTestsPreferencesPIDTable": tsTestsPreferencesPIDTable,
       "tsTestsPreferencesPIDEntry": tsTestsPreferencesPIDEntry,
       "tsTestsPrefPIDInputNumber": tsTestsPrefPIDInputNumber,
       "tsTestsPrefPIDPID": tsTestsPrefPIDPID,
       "tsTestsPrefPIDRowStatus": tsTestsPrefPIDRowStatus,
       "tsTestsPrefPIDReferredIntervalMax": tsTestsPrefPIDReferredIntervalMax,
       "tsMeasurements": tsMeasurements,
       "tsPcrMeasurementTable": tsPcrMeasurementTable,
       "tsPcrMeasurementEntry": tsPcrMeasurementEntry,
       "tsPcrMeasurementInputNumber": tsPcrMeasurementInputNumber,
       "tsPcrMeasurementPID": tsPcrMeasurementPID,
       "tsPcrMeasurementNumber": tsPcrMeasurementNumber,
       "tsPcrMeasurementRowStatus": tsPcrMeasurementRowStatus,
       "tsPcrMeasurementState": tsPcrMeasurementState,
       "tsPcrMeasurementEnable": tsPcrMeasurementEnable,
       "tsPcrMeasurementCounter": tsPcrMeasurementCounter,
       "tsPcrMeasurementCounterDiscontinuity": tsPcrMeasurementCounterDiscontinuity,
       "tsPcrMeasurementCounterReset": tsPcrMeasurementCounterReset,
       "tsPcrMeasurementLatestError": tsPcrMeasurementLatestError,
       "tsPcrMeasurementActiveTime": tsPcrMeasurementActiveTime,
       "tsPcrMeasurementMeasurementState": tsPcrMeasurementMeasurementState,
       "tsPcrMeasurementValue": tsPcrMeasurementValue,
       "bitRate": bitRate,
       "tsTransportStreamBitRateTable": tsTransportStreamBitRateTable,
       "tsTransportStreamBitRateEntry": tsTransportStreamBitRateEntry,
       "tsTransportStreamBitRateInputNumber": tsTransportStreamBitRateInputNumber,
       "tsTransportStreamBitRateState": tsTransportStreamBitRateState,
       "tsTransportStreamBitRateEnable": tsTransportStreamBitRateEnable,
       "tsTransportStreamBitRateCounter": tsTransportStreamBitRateCounter,
       "tsTransportStreamBitRateCounterDiscontinuity": tsTransportStreamBitRateCounterDiscontinuity,
       "tsTransportStreamBitRateCounterReset": tsTransportStreamBitRateCounterReset,
       "tsTransportStreamBitRateLatestError": tsTransportStreamBitRateLatestError,
       "tsTransportStreamBitRateActiveTime": tsTransportStreamBitRateActiveTime,
       "tsTransportStreamBitRateMeasurementState": tsTransportStreamBitRateMeasurementState,
       "tsTransportStreamBitRateValue": tsTransportStreamBitRateValue,
       "tsTransportStreamBitRateNomenclature": tsTransportStreamBitRateNomenclature,
       "tsServiceBitRateTable": tsServiceBitRateTable,
       "tsServiceBitRateEntry": tsServiceBitRateEntry,
       "tsServiceBitRateInputNumber": tsServiceBitRateInputNumber,
       "tsServiceBitRateService": tsServiceBitRateService,
       "tsServiceBitRateRowStatus": tsServiceBitRateRowStatus,
       "tsServiceBitRateState": tsServiceBitRateState,
       "tsServiceBitRateEnable": tsServiceBitRateEnable,
       "tsServiceBitRateCounter": tsServiceBitRateCounter,
       "tsServiceBitRateCounterDiscontinuity": tsServiceBitRateCounterDiscontinuity,
       "tsServiceBitRateCounterReset": tsServiceBitRateCounterReset,
       "tsServiceBitRateLatestError": tsServiceBitRateLatestError,
       "tsServiceBitRateActiveTime": tsServiceBitRateActiveTime,
       "tsServiceBitRateMeasurementState": tsServiceBitRateMeasurementState,
       "tsServiceBitRateValue": tsServiceBitRateValue,
       "tsServiceBitRateNomenclature": tsServiceBitRateNomenclature,
       "tsPIDBitRateTable": tsPIDBitRateTable,
       "tsPIDBitRateEntry": tsPIDBitRateEntry,
       "tsPIDBitRateInputNumber": tsPIDBitRateInputNumber,
       "tsPIDBitRatePID": tsPIDBitRatePID,
       "tsPIDBitRateRowStatus": tsPIDBitRateRowStatus,
       "tsPIDBitRateState": tsPIDBitRateState,
       "tsPIDBitRateEnable": tsPIDBitRateEnable,
       "tsPIDBitRateCounter": tsPIDBitRateCounter,
       "tsPIDBitRateCounterDiscontinuity": tsPIDBitRateCounterDiscontinuity,
       "tsPIDBitRateCounterReset": tsPIDBitRateCounterReset,
       "tsPIDBitRateLatestError": tsPIDBitRateLatestError,
       "tsPIDBitRateActiveTime": tsPIDBitRateActiveTime,
       "tsPIDBitRateMeasurementState": tsPIDBitRateMeasurementState,
       "tsPIDBitRateValue": tsPIDBitRateValue,
       "tsPIDBitRateNomenclature": tsPIDBitRateNomenclature,
       "tsConsistencyTable": tsConsistencyTable,
       "tsConsistencyEntry": tsConsistencyEntry,
       "tsConsistencyInputNumber": tsConsistencyInputNumber,
       "tsConsistencyTestNumber": tsConsistencyTestNumber,
       "tsConsistencyState": tsConsistencyState,
       "tsConsistencyEnable": tsConsistencyEnable,
       "tsConsistencyCounter": tsConsistencyCounter,
       "tsConsistencyCounterDiscontinuity": tsConsistencyCounterDiscontinuity,
       "tsConsistencyCounterReset": tsConsistencyCounterReset,
       "tsConsistencyLatestError": tsConsistencyLatestError,
       "tsConsistencyActiveTime": tsConsistencyActiveTime,
       "tsMeasurePreferences": tsMeasurePreferences,
       "tsMeasurePreferencesTable": tsMeasurePreferencesTable,
       "tsMeasurePreferencesEntry": tsMeasurePreferencesEntry,
       "tsMeasurePrefInputNumber": tsMeasurePrefInputNumber,
       "tsMeasurePrefPCRDemarcationFrequency": tsMeasurePrefPCRDemarcationFrequency,
       "tsMeasurePrefPCRFOMax": tsMeasurePrefPCRFOMax,
       "tsMeasurePrefPCRDRMax": tsMeasurePrefPCRDRMax,
       "tsMeasurePrefPCROJMax": tsMeasurePrefPCROJMax,
       "tsMeasurePrefTSBitRateTau": tsMeasurePrefTSBitRateTau,
       "tsMeasurePrefTSBitRateN": tsMeasurePrefTSBitRateN,
       "tsMeasurePrefTSBitRateElement": tsMeasurePrefTSBitRateElement,
       "tsMeasurePrefTSBitRateMin": tsMeasurePrefTSBitRateMin,
       "tsMeasurePrefTSBitRateMax": tsMeasurePrefTSBitRateMax,
       "tsMeasurePrefAllServiceBitRateTau": tsMeasurePrefAllServiceBitRateTau,
       "tsMeasurePrefAllServiceBitRateN": tsMeasurePrefAllServiceBitRateN,
       "tsMeasurePrefAllServiceBitRateElement": tsMeasurePrefAllServiceBitRateElement,
       "tsMeasurePrefAllPIDBitRateTau": tsMeasurePrefAllPIDBitRateTau,
       "tsMeasurePrefAllPIDBitRateN": tsMeasurePrefAllPIDBitRateN,
       "tsMeasurePrefAllPIDBitRateElement": tsMeasurePrefAllPIDBitRateElement,
       "tsMeasurePrefExpectedTSID": tsMeasurePrefExpectedTSID,
       "tsMeasurePreferencesServiceTable": tsMeasurePreferencesServiceTable,
       "tsMeasurePreferencesServiceEntry": tsMeasurePreferencesServiceEntry,
       "tsMeasurePrefServiceInputNumber": tsMeasurePrefServiceInputNumber,
       "tsMeasurePrefServiceService": tsMeasurePrefServiceService,
       "tsMeasurePrefServiceRowStatus": tsMeasurePrefServiceRowStatus,
       "tsMeasurePrefServiceBitRateTau": tsMeasurePrefServiceBitRateTau,
       "tsMeasurePrefServiceBitRateN": tsMeasurePrefServiceBitRateN,
       "tsMeasurePrefServiceBitRateElement": tsMeasurePrefServiceBitRateElement,
       "tsMeasurePrefServiceBitRateMin": tsMeasurePrefServiceBitRateMin,
       "tsMeasurePrefServiceBitRateMax": tsMeasurePrefServiceBitRateMax,
       "tsMeasurePreferencesPIDTable": tsMeasurePreferencesPIDTable,
       "tsMeasurePreferencesPIDEntry": tsMeasurePreferencesPIDEntry,
       "tsMeasurePrefPIDInputNumber": tsMeasurePrefPIDInputNumber,
       "tsMeasurePrefPIDPID": tsMeasurePrefPIDPID,
       "tsMeasurePrefPIDRowStatus": tsMeasurePrefPIDRowStatus,
       "tsMeasurePrefPIDBitRateTau": tsMeasurePrefPIDBitRateTau,
       "tsMeasurePrefPIDBitRateN": tsMeasurePrefPIDBitRateN,
       "tsMeasurePrefPIDBitRateElement": tsMeasurePrefPIDBitRateElement,
       "tsMeasurePrefPIDBitRateMin": tsMeasurePrefPIDBitRateMin,
       "tsMeasurePrefPIDBitRateMax": tsMeasurePrefPIDBitRateMax,
       "tsServicePerformance": tsServicePerformance,
       "tsServicePerformanceTable": tsServicePerformanceTable,
       "tsServicePerformanceEntry": tsServicePerformanceEntry,
       "tsServicePerformanceInputNumber": tsServicePerformanceInputNumber,
       "tsServicePerformanceNumber": tsServicePerformanceNumber,
       "tsServicePerformanceState": tsServicePerformanceState,
       "tsServicePerformanceEnable": tsServicePerformanceEnable,
       "tsServicePerformanceCounter": tsServicePerformanceCounter,
       "tsServicePerformanceCounterDiscontinuity": tsServicePerformanceCounterDiscontinuity,
       "tsServicePerformanceCounterReset": tsServicePerformanceCounterReset,
       "tsServicePerformanceLatestError": tsServicePerformanceLatestError,
       "tsServicePerformanceActiveTime": tsServicePerformanceActiveTime,
       "tsServicePerformanceMeasurementState": tsServicePerformanceMeasurementState,
       "tsServicePerformanceError": tsServicePerformanceError,
       "tsServicePerformanceErrorRatio": tsServicePerformanceErrorRatio,
       "tsServicePerformancePreferencesTable": tsServicePerformancePreferencesTable,
       "tsServicePerformancePreferencesEntry": tsServicePerformancePreferencesEntry,
       "tsSPPrefInputNumber": tsSPPrefInputNumber,
       "tsSPPrefNumber": tsSPPrefNumber,
       "tsSPPrefDeltaT": tsSPPrefDeltaT,
       "tsSPPrefEvaluationTime": tsSPPrefEvaluationTime,
       "tsSPPrefThreshold": tsSPPrefThreshold,
       "tr101290CableSat": tr101290CableSat,
       "sysAvailabilityTable": sysAvailabilityTable,
       "sysAvailabilityEntry": sysAvailabilityEntry,
       "sysAvailabilityInputNumber": sysAvailabilityInputNumber,
       "sysAvailabilityTestState": sysAvailabilityTestState,
       "sysAvailabilityEnable": sysAvailabilityEnable,
       "sysAvailabilityCounter": sysAvailabilityCounter,
       "sysAvailabilityCounterDiscontinuity": sysAvailabilityCounterDiscontinuity,
       "sysAvailabilityCounterReset": sysAvailabilityCounterReset,
       "sysAvailabilityLatestError": sysAvailabilityLatestError,
       "sysAvailabilityActiveTime": sysAvailabilityActiveTime,
       "sysAvailabilityMeasurementState": sysAvailabilityMeasurementState,
       "sysAvailabilityUnavailableTime": sysAvailabilityUnavailableTime,
       "sysAvailabilityRatio": sysAvailabilityRatio,
       "sysAvailabilityInSETI": sysAvailabilityInSETI,
       "linkAvailabilityTable": linkAvailabilityTable,
       "linkAvailabilityEntry": linkAvailabilityEntry,
       "linkAvailabilityInputNumber": linkAvailabilityInputNumber,
       "linkAvailabilityTestState": linkAvailabilityTestState,
       "linkAvailabilityEnable": linkAvailabilityEnable,
       "linkAvailabilityCounter": linkAvailabilityCounter,
       "linkAvailabilityCounterDiscontinuity": linkAvailabilityCounterDiscontinuity,
       "linkAvailabilityCounterReset": linkAvailabilityCounterReset,
       "linkAvailabilityLatestError": linkAvailabilityLatestError,
       "linkAvailabilityActiveTime": linkAvailabilityActiveTime,
       "linkAvailabilityMeasurementState": linkAvailabilityMeasurementState,
       "linkAvailabilityUnavailableTime": linkAvailabilityUnavailableTime,
       "linkAvailabilityRatio": linkAvailabilityRatio,
       "linkAvailabilityInSUTI": linkAvailabilityInSUTI,
       "berRSinServiceTable": berRSinServiceTable,
       "berRSinServiceEntry": berRSinServiceEntry,
       "berRSinServiceInputNumber": berRSinServiceInputNumber,
       "berRSinServiceTestState": berRSinServiceTestState,
       "berRSinServiceEnable": berRSinServiceEnable,
       "berRSinServiceCounter": berRSinServiceCounter,
       "berRSinServiceCounterDiscontinuity": berRSinServiceCounterDiscontinuity,
       "berRSinServiceCounterReset": berRSinServiceCounterReset,
       "berRSinServiceLatestError": berRSinServiceLatestError,
       "berRSinServiceActiveTime": berRSinServiceActiveTime,
       "berRSinServiceMeasurementState": berRSinServiceMeasurementState,
       "berRSinServiceValue": berRSinServiceValue,
       "rfIFsignalPowerTable": rfIFsignalPowerTable,
       "rfIFsignalPowerEntry": rfIFsignalPowerEntry,
       "rfIFsignalPowerInputNumber": rfIFsignalPowerInputNumber,
       "rfIFsignalPowerTestState": rfIFsignalPowerTestState,
       "rfIFsignalPowerEnable": rfIFsignalPowerEnable,
       "rfIFsignalPowerCounter": rfIFsignalPowerCounter,
       "rfIFsignalPowerCounterDiscontinuity": rfIFsignalPowerCounterDiscontinuity,
       "rfIFsignalPowerCounterReset": rfIFsignalPowerCounterReset,
       "rfIFsignalPowerLatestError": rfIFsignalPowerLatestError,
       "rfIFsignalPowerActiveTime": rfIFsignalPowerActiveTime,
       "rfIFsignalPowerMeasurementState": rfIFsignalPowerMeasurementState,
       "rfIFsignalPowerValue": rfIFsignalPowerValue,
       "noisePowerTable": noisePowerTable,
       "noisePowerEntry": noisePowerEntry,
       "noisePowerInputNumber": noisePowerInputNumber,
       "noisePowerTestState": noisePowerTestState,
       "noisePowerEnable": noisePowerEnable,
       "noisePowerCounter": noisePowerCounter,
       "noisePowerCounterDiscontinuity": noisePowerCounterDiscontinuity,
       "noisePowerCounterReset": noisePowerCounterReset,
       "noisePowerLatestError": noisePowerLatestError,
       "noisePowerActiveTime": noisePowerActiveTime,
       "noisePowerMeasurementState": noisePowerMeasurementState,
       "noisePowerValue": noisePowerValue,
       "iqAnalysisCS": iqAnalysisCS,
       "merCSTable": merCSTable,
       "merCSEntry": merCSEntry,
       "merCSInputNumber": merCSInputNumber,
       "merCSTestState": merCSTestState,
       "merCSEnable": merCSEnable,
       "merCSCounter": merCSCounter,
       "merCSCounterDiscontinuity": merCSCounterDiscontinuity,
       "merCSCounterReset": merCSCounterReset,
       "merCSLatestError": merCSLatestError,
       "merCSActiveTime": merCSActiveTime,
       "merCSMeasurementState": merCSMeasurementState,
       "merCSValue": merCSValue,
       "steCS": steCS,
       "steMeanCSTable": steMeanCSTable,
       "steMeanCSEntry": steMeanCSEntry,
       "steMeanCSInputNumber": steMeanCSInputNumber,
       "steMeanCSTestState": steMeanCSTestState,
       "steMeanCSEnable": steMeanCSEnable,
       "steMeanCSCounter": steMeanCSCounter,
       "steMeanCSCounterDiscontinuity": steMeanCSCounterDiscontinuity,
       "steMeanCSCounterReset": steMeanCSCounterReset,
       "steMeanCSLatestError": steMeanCSLatestError,
       "steMeanCSActiveTime": steMeanCSActiveTime,
       "steMeanCSMeasurementState": steMeanCSMeasurementState,
       "steMeanCSValue": steMeanCSValue,
       "steDeviationCSTable": steDeviationCSTable,
       "steDeviationCSEntry": steDeviationCSEntry,
       "steDeviationCSInputNumber": steDeviationCSInputNumber,
       "steDeviationCSTestState": steDeviationCSTestState,
       "steDeviationCSEnable": steDeviationCSEnable,
       "steDeviationCSCounter": steDeviationCSCounter,
       "steDeviationCSCounterDiscontinuity": steDeviationCSCounterDiscontinuity,
       "steDeviationCSCounterReset": steDeviationCSCounterReset,
       "steDeviationCSLatestError": steDeviationCSLatestError,
       "steDeviationCSActiveTime": steDeviationCSActiveTime,
       "steDeviationCSMeasurementState": steDeviationCSMeasurementState,
       "steDeviationCSValue": steDeviationCSValue,
       "csCSTable": csCSTable,
       "csCSEntry": csCSEntry,
       "csCSInputNumber": csCSInputNumber,
       "csCSTestState": csCSTestState,
       "csCSEnable": csCSEnable,
       "csCSCounter": csCSCounter,
       "csCSCounterDiscontinuity": csCSCounterDiscontinuity,
       "csCSCounterReset": csCSCounterReset,
       "csCSLatestError": csCSLatestError,
       "csCSActiveTime": csCSActiveTime,
       "csCSMeasurementState": csCSMeasurementState,
       "csCSValue": csCSValue,
       "aiCSTable": aiCSTable,
       "aiCSEntry": aiCSEntry,
       "aiCSInputNumber": aiCSInputNumber,
       "aiCSTestState": aiCSTestState,
       "aiCSEnable": aiCSEnable,
       "aiCSCounter": aiCSCounter,
       "aiCSCounterDiscontinuity": aiCSCounterDiscontinuity,
       "aiCSCounterReset": aiCSCounterReset,
       "aiCSLatestError": aiCSLatestError,
       "aiCSActiveTime": aiCSActiveTime,
       "aiCSMeasurementState": aiCSMeasurementState,
       "aiCSValue": aiCSValue,
       "qeCSTable": qeCSTable,
       "qeCSEntry": qeCSEntry,
       "qeCSInputNumber": qeCSInputNumber,
       "qeCSTestState": qeCSTestState,
       "qeCSEnable": qeCSEnable,
       "qeCSCounter": qeCSCounter,
       "qeCSCounterDiscontinuity": qeCSCounterDiscontinuity,
       "qeCSCounterReset": qeCSCounterReset,
       "qeCSLatestError": qeCSLatestError,
       "qeCSActiveTime": qeCSActiveTime,
       "qeCSMeasurementState": qeCSMeasurementState,
       "qeCSValue": qeCSValue,
       "rteCSTable": rteCSTable,
       "rteCSEntry": rteCSEntry,
       "rteCSInputNumber": rteCSInputNumber,
       "rteCSTestState": rteCSTestState,
       "rteCSEnable": rteCSEnable,
       "rteCSCounter": rteCSCounter,
       "rteCSCounterDiscontinuity": rteCSCounterDiscontinuity,
       "rteCSCounterReset": rteCSCounterReset,
       "rteCSLatestError": rteCSLatestError,
       "rteCSActiveTime": rteCSActiveTime,
       "rteCSMeasurementState": rteCSMeasurementState,
       "rteCSValue": rteCSValue,
       "ciCSTable": ciCSTable,
       "ciCSEntry": ciCSEntry,
       "ciCSInputNumber": ciCSInputNumber,
       "ciCSTestState": ciCSTestState,
       "ciCSEnable": ciCSEnable,
       "ciCSCounter": ciCSCounter,
       "ciCSCounterDiscontinuity": ciCSCounterDiscontinuity,
       "ciCSCounterReset": ciCSCounterReset,
       "ciCSLatestError": ciCSLatestError,
       "ciCSActiveTime": ciCSActiveTime,
       "ciCSMeasurementState": ciCSMeasurementState,
       "ciCSValue": ciCSValue,
       "pjCSTable": pjCSTable,
       "pjCSEntry": pjCSEntry,
       "pjCSInputNumber": pjCSInputNumber,
       "pjCSTestState": pjCSTestState,
       "pjCSEnable": pjCSEnable,
       "pjCSCounter": pjCSCounter,
       "pjCSCounterDiscontinuity": pjCSCounterDiscontinuity,
       "pjCSCounterReset": pjCSCounterReset,
       "pjCSLatestError": pjCSLatestError,
       "pjCSActiveTime": pjCSActiveTime,
       "pjCSMeasurementState": pjCSMeasurementState,
       "pjCSValue": pjCSValue,
       "snrCSTable": snrCSTable,
       "snrCSEntry": snrCSEntry,
       "snrCSInputNumber": snrCSInputNumber,
       "snrCSTestState": snrCSTestState,
       "snrCSEnable": snrCSEnable,
       "snrCSCounter": snrCSCounter,
       "snrCSCounterDiscontinuity": snrCSCounterDiscontinuity,
       "snrCSCounterReset": snrCSCounterReset,
       "snrCSLatestError": snrCSLatestError,
       "snrCSActiveTime": snrCSActiveTime,
       "snrCSMeasurementState": snrCSMeasurementState,
       "snrCSValue": snrCSValue,
       "cableSatPreferencesTable": cableSatPreferencesTable,
       "cableSatPreferencesEntry": cableSatPreferencesEntry,
       "cableSatPrefInputNumber": cableSatPrefInputNumber,
       "cableSatPrefCentreFrequency": cableSatPrefCentreFrequency,
       "cableSatPrefModulation": cableSatPrefModulation,
       "cableSatPrefSysAvailUATMode": cableSatPrefSysAvailUATMode,
       "cableSatPrefSysAvailN": cableSatPrefSysAvailN,
       "cableSatPrefSysAvailT": cableSatPrefSysAvailT,
       "cableSatPrefSysAvailM": cableSatPrefSysAvailM,
       "cableSatPrefSysAvailTI": cableSatPrefSysAvailTI,
       "cableSatPrefSysAvailEBPerCent": cableSatPrefSysAvailEBPerCent,
       "cableSatPrefSysAvailTotalTime": cableSatPrefSysAvailTotalTime,
       "cableSatPrefLinkAvailUATMode": cableSatPrefLinkAvailUATMode,
       "cableSatPrefLinkAvailN": cableSatPrefLinkAvailN,
       "cableSatPrefLinkAvailT": cableSatPrefLinkAvailT,
       "cableSatPrefLinkAvailM": cableSatPrefLinkAvailM,
       "cableSatPrefLinkAvailTI": cableSatPrefLinkAvailTI,
       "cableSatPrefLinkAvailUPPerCent": cableSatPrefLinkAvailUPPerCent,
       "cableSatPrefLinkAvailTotalTime": cableSatPrefLinkAvailTotalTime,
       "cableSatPrefBERMax": cableSatPrefBERMax,
       "cableSatPrefSignalPowerMin": cableSatPrefSignalPowerMin,
       "cableSatPrefSignalPowerMax": cableSatPrefSignalPowerMax,
       "cableSatPrefNoisePowerMax": cableSatPrefNoisePowerMax,
       "cableSatPrefMerCSMin": cableSatPrefMerCSMin,
       "cableSatPrefSteMeanCSMax": cableSatPrefSteMeanCSMax,
       "cableSatPrefSteDeviationCSMax": cableSatPrefSteDeviationCSMax,
       "cableSatPrefCsCSMin": cableSatPrefCsCSMin,
       "cableSatPrefAiCSMax": cableSatPrefAiCSMax,
       "cableSatPrefQeCSMax": cableSatPrefQeCSMax,
       "cableSatPrefRteCSMax": cableSatPrefRteCSMax,
       "cableSatPrefCiCSMin": cableSatPrefCiCSMin,
       "cableSatPrefPjCSMax": cableSatPrefPjCSMax,
       "cableSatPrefSnrCSMin": cableSatPrefSnrCSMin,
       "tr101290Cable": tr101290Cable,
       "noiseMarginTable": noiseMarginTable,
       "noiseMarginEntry": noiseMarginEntry,
       "noiseMarginInputNumber": noiseMarginInputNumber,
       "noiseMarginTestState": noiseMarginTestState,
       "noiseMarginEnable": noiseMarginEnable,
       "noiseMarginCounter": noiseMarginCounter,
       "noiseMarginCounterDiscontinuity": noiseMarginCounterDiscontinuity,
       "noiseMarginCounterReset": noiseMarginCounterReset,
       "noiseMarginLatestError": noiseMarginLatestError,
       "noiseMarginActiveTime": noiseMarginActiveTime,
       "noiseMarginMeasurementState": noiseMarginMeasurementState,
       "noiseMarginValue": noiseMarginValue,
       "estNoiseMarginTable": estNoiseMarginTable,
       "estNoiseMarginEntry": estNoiseMarginEntry,
       "estNoiseMarginInputNumber": estNoiseMarginInputNumber,
       "estNoiseMarginTestState": estNoiseMarginTestState,
       "estNoiseMarginEnable": estNoiseMarginEnable,
       "estNoiseMarginCounter": estNoiseMarginCounter,
       "estNoiseMarginCounterDiscontinuity": estNoiseMarginCounterDiscontinuity,
       "estNoiseMarginCounterReset": estNoiseMarginCounterReset,
       "estNoiseMarginLatestError": estNoiseMarginLatestError,
       "estNoiseMarginActiveTime": estNoiseMarginActiveTime,
       "estNoiseMarginMeasurementState": estNoiseMarginMeasurementState,
       "estNoiseMarginValue": estNoiseMarginValue,
       "signQualMarTTable": signQualMarTTable,
       "signQualMarTEntry": signQualMarTEntry,
       "signQualMarTInputNumber": signQualMarTInputNumber,
       "signQualMarTTestState": signQualMarTTestState,
       "signQualMarTEnable": signQualMarTEnable,
       "signQualMarTCounter": signQualMarTCounter,
       "signQualMarTCounterDiscontinuity": signQualMarTCounterDiscontinuity,
       "signQualMarTCounterReset": signQualMarTCounterReset,
       "signQualMarTLatestError": signQualMarTLatestError,
       "signQualMarTActiveTime": signQualMarTActiveTime,
       "eNDCTable": eNDCTable,
       "eNDCEntry": eNDCEntry,
       "eNDCInputNumber": eNDCInputNumber,
       "eNDCTestState": eNDCTestState,
       "eNDCEnable": eNDCEnable,
       "eNDCCounter": eNDCCounter,
       "eNDCCounterDiscontinuity": eNDCCounterDiscontinuity,
       "eNDCCounterReset": eNDCCounterReset,
       "eNDCLatestError": eNDCLatestError,
       "eNDCActiveTime": eNDCActiveTime,
       "eNDCMeasurementState": eNDCMeasurementState,
       "eNDCValue": eNDCValue,
       "outBandEmissTable": outBandEmissTable,
       "outBandEmissEntry": outBandEmissEntry,
       "outBandEmissInputNumber": outBandEmissInputNumber,
       "outBandEmissTestState": outBandEmissTestState,
       "outBandEmissEnable": outBandEmissEnable,
       "outBandEmissCounter": outBandEmissCounter,
       "outBandEmissCounterDiscontinuity": outBandEmissCounterDiscontinuity,
       "outBandEmissCounterReset": outBandEmissCounterReset,
       "outBandEmissLatestError": outBandEmissLatestError,
       "outBandEmissActiveTime": outBandEmissActiveTime,
       "cablePreferencesTable": cablePreferencesTable,
       "cablePreferencesEntry": cablePreferencesEntry,
       "cablePrefInputNumber": cablePrefInputNumber,
       "cablePrefNoiseMarginMin": cablePrefNoiseMarginMin,
       "cablePrefEstNoiseMarginMin": cablePrefEstNoiseMarginMin,
       "cablePrefSignQualBoxSize": cablePrefSignQualBoxSize,
       "cablePrefSignQualPercentMax": cablePrefSignQualPercentMax,
       "cablePrefENDBER": cablePrefENDBER,
       "cablePrefENDCtoNSpecified": cablePrefENDCtoNSpecified,
       "cablePrefENDIdeal": cablePrefENDIdeal,
       "cablePrefENDMax": cablePrefENDMax,
       "tr101290Satellite": tr101290Satellite,
       "berViterbiSTable": berViterbiSTable,
       "berViterbiSEntry": berViterbiSEntry,
       "berViterbiSInputNumber": berViterbiSInputNumber,
       "berViterbiSTestState": berViterbiSTestState,
       "berViterbiSEnable": berViterbiSEnable,
       "berViterbiSCounter": berViterbiSCounter,
       "berViterbiSCounterDiscontinuity": berViterbiSCounterDiscontinuity,
       "berViterbiSCounterReset": berViterbiSCounterReset,
       "berViterbiSLatestError": berViterbiSLatestError,
       "berViterbiSActiveTime": berViterbiSActiveTime,
       "berViterbiSMeasurementState": berViterbiSMeasurementState,
       "berViterbiSIValue": berViterbiSIValue,
       "berViterbiSQValue": berViterbiSQValue,
       "berViterbiSMeasurementMethod": berViterbiSMeasurementMethod,
       "ifSpectrumTable": ifSpectrumTable,
       "ifSpectrumEntry": ifSpectrumEntry,
       "ifSpectrumInputNumber": ifSpectrumInputNumber,
       "ifSpectrumTestState": ifSpectrumTestState,
       "ifSpectrumEnable": ifSpectrumEnable,
       "ifSpectrumCounter": ifSpectrumCounter,
       "ifSpectrumCounterDiscontinuity": ifSpectrumCounterDiscontinuity,
       "ifSpectrumCounterReset": ifSpectrumCounterReset,
       "ifSpectrumLatestError": ifSpectrumLatestError,
       "ifSpectrumActiveTime": ifSpectrumActiveTime,
       "satellitePreferencesTable": satellitePreferencesTable,
       "satellitePreferencesEntry": satellitePreferencesEntry,
       "satellitePrefInputNumber": satellitePrefInputNumber,
       "satellitePrefBERMax": satellitePrefBERMax,
       "tr101290Terrestrial": tr101290Terrestrial,
       "rfTerr": rfTerr,
       "rfAccuracyTable": rfAccuracyTable,
       "rfAccuracyEntry": rfAccuracyEntry,
       "rfAccuracyInputNumber": rfAccuracyInputNumber,
       "rfAccuracyTestState": rfAccuracyTestState,
       "rfAccuracyEnable": rfAccuracyEnable,
       "rfAccuracyCounter": rfAccuracyCounter,
       "rfAccuracyCounterDiscontinuity": rfAccuracyCounterDiscontinuity,
       "rfAccuracyCounterReset": rfAccuracyCounterReset,
       "rfAccuracyLatestError": rfAccuracyLatestError,
       "rfAccuracyActiveTime": rfAccuracyActiveTime,
       "rfAccuracyMeasurementState": rfAccuracyMeasurementState,
       "rfAccuracyValue": rfAccuracyValue,
       "rfChannelWidthTable": rfChannelWidthTable,
       "rfChannelWidthEntry": rfChannelWidthEntry,
       "rfChannelWidthInputNumber": rfChannelWidthInputNumber,
       "rfChannelWidthTestState": rfChannelWidthTestState,
       "rfChannelWidthEnable": rfChannelWidthEnable,
       "rfChannelWidthCounter": rfChannelWidthCounter,
       "rfChannelWidthCounterDiscontinuity": rfChannelWidthCounterDiscontinuity,
       "rfChannelWidthCounterReset": rfChannelWidthCounterReset,
       "rfChannelWidthLatestError": rfChannelWidthLatestError,
       "rfChannelWidthActiveTime": rfChannelWidthActiveTime,
       "rfChannelWidthMeasurementState": rfChannelWidthMeasurementState,
       "rfChannelWidthValue": rfChannelWidthValue,
       "symbolLengthTable": symbolLengthTable,
       "symbolLengthEntry": symbolLengthEntry,
       "symbolLengthInputNumber": symbolLengthInputNumber,
       "symbolLengthTestState": symbolLengthTestState,
       "symbolLengthEnable": symbolLengthEnable,
       "symbolLengthCounter": symbolLengthCounter,
       "symbolLengthCounterDiscontinuity": symbolLengthCounterDiscontinuity,
       "symbolLengthCounterReset": symbolLengthCounterReset,
       "symbolLengthLatestError": symbolLengthLatestError,
       "symbolLengthActiveTime": symbolLengthActiveTime,
       "symbolLengthMeasurementState": symbolLengthMeasurementState,
       "symbolLengthValue": symbolLengthValue,
       "rfIfPowerTable": rfIfPowerTable,
       "rfIfPowerEntry": rfIfPowerEntry,
       "rfIfPowerInputNumber": rfIfPowerInputNumber,
       "rfIfPowerTestState": rfIfPowerTestState,
       "rfIfPowerEnable": rfIfPowerEnable,
       "rfIfPowerCounter": rfIfPowerCounter,
       "rfIfPowerCounterDiscontinuity": rfIfPowerCounterDiscontinuity,
       "rfIfPowerCounterReset": rfIfPowerCounterReset,
       "rfIfPowerLatestError": rfIfPowerLatestError,
       "rfIfPowerActiveTime": rfIfPowerActiveTime,
       "rfIfPowerMeasurementState": rfIfPowerMeasurementState,
       "rfIfPowerValue": rfIfPowerValue,
       "rfIfSpectrumTable": rfIfSpectrumTable,
       "rfIfSpectrumEntry": rfIfSpectrumEntry,
       "rfIfSpectrumInputNumber": rfIfSpectrumInputNumber,
       "rfIfSpectrumTestState": rfIfSpectrumTestState,
       "rfIfSpectrumEnable": rfIfSpectrumEnable,
       "rfIfSpectrumCounter": rfIfSpectrumCounter,
       "rfIfSpectrumCounterDiscontinuity": rfIfSpectrumCounterDiscontinuity,
       "rfIfSpectrumCounterReset": rfIfSpectrumCounterReset,
       "rfIfSpectrumLatestError": rfIfSpectrumLatestError,
       "rfIfSpectrumActiveTime": rfIfSpectrumActiveTime,
       "eNDT": eNDT,
       "eNDTTable": eNDTTable,
       "eNDTEntry": eNDTEntry,
       "eNDTInputNumber": eNDTInputNumber,
       "eNDTTestState": eNDTTestState,
       "eNDTEnable": eNDTEnable,
       "eNDTCounter": eNDTCounter,
       "eNDTCounterDiscontinuity": eNDTCounterDiscontinuity,
       "eNDTCounterReset": eNDTCounterReset,
       "eNDTLatestError": eNDTLatestError,
       "eNDTActiveTime": eNDTActiveTime,
       "eNDTMeasurementState": eNDTMeasurementState,
       "eNDTValue": eNDTValue,
       "eNFTTable": eNFTTable,
       "eNFTEntry": eNFTEntry,
       "eNFTInputNumber": eNFTInputNumber,
       "eNFTTestState": eNFTTestState,
       "eNFTEnable": eNFTEnable,
       "eNFTCounter": eNFTCounter,
       "eNFTCounterDiscontinuity": eNFTCounterDiscontinuity,
       "eNFTCounterReset": eNFTCounterReset,
       "eNFTLatestError": eNFTLatestError,
       "eNFTActiveTime": eNFTActiveTime,
       "eNFTMeasurementState": eNFTMeasurementState,
       "eNFTValue": eNFTValue,
       "eNDTLPTable": eNDTLPTable,
       "eNDTLPEntry": eNDTLPEntry,
       "eNDTLPInputNumber": eNDTLPInputNumber,
       "eNDTLPTestState": eNDTLPTestState,
       "eNDTLPEnable": eNDTLPEnable,
       "eNDTLPCounter": eNDTLPCounter,
       "eNDTLPCounterDiscontinuity": eNDTLPCounterDiscontinuity,
       "eNDTLPCounterReset": eNDTLPCounterReset,
       "eNDTLPLatestError": eNDTLPLatestError,
       "eNDTLPActiveTime": eNDTLPActiveTime,
       "eNDTLPMeasurementState": eNDTLPMeasurementState,
       "eNDTLPValue": eNDTLPValue,
       "eNFTLPTable": eNFTLPTable,
       "eNFTLPEntry": eNFTLPEntry,
       "eNFTLPInputNumber": eNFTLPInputNumber,
       "eNFTLPTestState": eNFTLPTestState,
       "eNFTLPEnable": eNFTLPEnable,
       "eNFTLPCounter": eNFTLPCounter,
       "eNFTLPCounterDiscontinuity": eNFTLPCounterDiscontinuity,
       "eNFTLPCounterReset": eNFTLPCounterReset,
       "eNFTLPLatestError": eNFTLPLatestError,
       "eNFTLPActiveTime": eNFTLPActiveTime,
       "eNFTLPMeasurementState": eNFTLPMeasurementState,
       "eNFTLPValue": eNFTLPValue,
       "linearityTable": linearityTable,
       "linearityEntry": linearityEntry,
       "linearityInputNumber": linearityInputNumber,
       "linearityTestState": linearityTestState,
       "linearityEnable": linearityEnable,
       "linearityCounter": linearityCounter,
       "linearityCounterDiscontinuity": linearityCounterDiscontinuity,
       "linearityCounterReset": linearityCounterReset,
       "linearityLatestError": linearityLatestError,
       "linearityActiveTime": linearityActiveTime,
       "linearityMeasurementState": linearityMeasurementState,
       "linearityValue": linearityValue,
       "berViterbiT": berViterbiT,
       "berViterbiTTable": berViterbiTTable,
       "berViterbiTEntry": berViterbiTEntry,
       "berViterbiTInputNumber": berViterbiTInputNumber,
       "berViterbiTTestState": berViterbiTTestState,
       "berViterbiTEnable": berViterbiTEnable,
       "berViterbiTCounter": berViterbiTCounter,
       "berViterbiTCounterDiscontinuity": berViterbiTCounterDiscontinuity,
       "berViterbiTCounterReset": berViterbiTCounterReset,
       "berViterbiTLatestError": berViterbiTLatestError,
       "berViterbiTActiveTime": berViterbiTActiveTime,
       "berViterbiTMeasurementState": berViterbiTMeasurementState,
       "berViterbiTValue": berViterbiTValue,
       "berViterbiTLPTable": berViterbiTLPTable,
       "berViterbiTLPEntry": berViterbiTLPEntry,
       "berViterbiTLPInputNumber": berViterbiTLPInputNumber,
       "berViterbiTLPTestState": berViterbiTLPTestState,
       "berViterbiTLPEnable": berViterbiTLPEnable,
       "berViterbiTLPCounter": berViterbiTLPCounter,
       "berViterbiTLPCounterDiscontinuity": berViterbiTLPCounterDiscontinuity,
       "berViterbiTLPCounterReset": berViterbiTLPCounterReset,
       "berViterbiTLPLatestError": berViterbiTLPLatestError,
       "berViterbiTLPActiveTime": berViterbiTLPActiveTime,
       "berViterbiTLPMeasurementState": berViterbiTLPMeasurementState,
       "berViterbiTLPValue": berViterbiTLPValue,
       "berRS": berRS,
       "berRSTable": berRSTable,
       "berRSEntry": berRSEntry,
       "berRSInputNumber": berRSInputNumber,
       "berRSTestState": berRSTestState,
       "berRSEnable": berRSEnable,
       "berRSCounter": berRSCounter,
       "berRSCounterDiscontinuity": berRSCounterDiscontinuity,
       "berRSCounterReset": berRSCounterReset,
       "berRSLatestError": berRSLatestError,
       "berRSActiveTime": berRSActiveTime,
       "berRSMeasurementState": berRSMeasurementState,
       "berRSValue": berRSValue,
       "berRSLPTable": berRSLPTable,
       "berRSLPEntry": berRSLPEntry,
       "berRSLPInputNumber": berRSLPInputNumber,
       "berRSLPTestState": berRSLPTestState,
       "berRSLPEnable": berRSLPEnable,
       "berRSLPCounter": berRSLPCounter,
       "berRSLPCounterDiscontinuity": berRSLPCounterDiscontinuity,
       "berRSLPCounterReset": berRSLPCounterReset,
       "berRSLPLatestError": berRSLPLatestError,
       "berRSLPActiveTime": berRSLPActiveTime,
       "berRSLPMeasurementState": berRSLPMeasurementState,
       "berRSLPValue": berRSLPValue,
       "iqAnalysisT": iqAnalysisT,
       "merTTable": merTTable,
       "merTEntry": merTEntry,
       "merTInputNumber": merTInputNumber,
       "merTTestState": merTTestState,
       "merTEnable": merTEnable,
       "merTCounter": merTCounter,
       "merTCounterDiscontinuity": merTCounterDiscontinuity,
       "merTCounterReset": merTCounterReset,
       "merTLatestError": merTLatestError,
       "merTActiveTime": merTActiveTime,
       "merTMeasurementState": merTMeasurementState,
       "merTValue": merTValue,
       "steT": steT,
       "steMeanTTable": steMeanTTable,
       "steMeanTEntry": steMeanTEntry,
       "steMeanTInputNumber": steMeanTInputNumber,
       "steMeanTTestState": steMeanTTestState,
       "steMeanTEnable": steMeanTEnable,
       "steMeanTCounter": steMeanTCounter,
       "steMeanTCounterDiscontinuity": steMeanTCounterDiscontinuity,
       "steMeanTCounterReset": steMeanTCounterReset,
       "steMeanTLatestError": steMeanTLatestError,
       "steMeanTActiveTime": steMeanTActiveTime,
       "steMeanTMeasurementState": steMeanTMeasurementState,
       "steMeanTValue": steMeanTValue,
       "steDeviationTTable": steDeviationTTable,
       "steDeviationTEntry": steDeviationTEntry,
       "steDeviationTInputNumber": steDeviationTInputNumber,
       "steDeviationTTestState": steDeviationTTestState,
       "steDeviationTEnable": steDeviationTEnable,
       "steDeviationTCounter": steDeviationTCounter,
       "steDeviationTCounterDiscontinuity": steDeviationTCounterDiscontinuity,
       "steDeviationTCounterReset": steDeviationTCounterReset,
       "steDeviationTLatestError": steDeviationTLatestError,
       "steDeviationTActiveTime": steDeviationTActiveTime,
       "steDeviationTMeasurementState": steDeviationTMeasurementState,
       "steDeviationTValue": steDeviationTValue,
       "csTTable": csTTable,
       "csTEntry": csTEntry,
       "csTInputNumber": csTInputNumber,
       "csTTestState": csTTestState,
       "csTEnable": csTEnable,
       "csTCounter": csTCounter,
       "csTCounterDiscontinuity": csTCounterDiscontinuity,
       "csTCounterReset": csTCounterReset,
       "csTLatestError": csTLatestError,
       "csTActiveTime": csTActiveTime,
       "csTMeasurementState": csTMeasurementState,
       "csTValue": csTValue,
       "aiTTable": aiTTable,
       "aiTEntry": aiTEntry,
       "aiTInputNumber": aiTInputNumber,
       "aiTTestState": aiTTestState,
       "aiTEnable": aiTEnable,
       "aiTCounter": aiTCounter,
       "aiTCounterDiscontinuity": aiTCounterDiscontinuity,
       "aiTCounterReset": aiTCounterReset,
       "aiTLatestError": aiTLatestError,
       "aiTActiveTime": aiTActiveTime,
       "aiTMeasurementState": aiTMeasurementState,
       "aiTValue": aiTValue,
       "qeTTable": qeTTable,
       "qeTEntry": qeTEntry,
       "qeTInputNumber": qeTInputNumber,
       "qeTTestState": qeTTestState,
       "qeTEnable": qeTEnable,
       "qeTCounter": qeTCounter,
       "qeTCounterDiscontinuity": qeTCounterDiscontinuity,
       "qeTCounterReset": qeTCounterReset,
       "qeTLatestError": qeTLatestError,
       "qeTActiveTime": qeTActiveTime,
       "qeTMeasurementState": qeTMeasurementState,
       "qeTValue": qeTValue,
       "pjTTable": pjTTable,
       "pjTEntry": pjTEntry,
       "pjTInputNumber": pjTInputNumber,
       "pjTTestState": pjTTestState,
       "pjTEnable": pjTEnable,
       "pjTCounter": pjTCounter,
       "pjTCounterDiscontinuity": pjTCounterDiscontinuity,
       "pjTCounterReset": pjTCounterReset,
       "pjTLatestError": pjTLatestError,
       "pjTActiveTime": pjTActiveTime,
       "pjTMeasurementState": pjTMeasurementState,
       "pjTValue": pjTValue,
       "mipSyntaxTable": mipSyntaxTable,
       "mipSyntaxEntry": mipSyntaxEntry,
       "mipSyntaxInputNumber": mipSyntaxInputNumber,
       "mipSyntaxTestNumber": mipSyntaxTestNumber,
       "mipSyntaxState": mipSyntaxState,
       "mipSyntaxEnable": mipSyntaxEnable,
       "mipSyntaxCounter": mipSyntaxCounter,
       "mipSyntaxCounterDiscontinuity": mipSyntaxCounterDiscontinuity,
       "mipSyntaxCounterReset": mipSyntaxCounterReset,
       "mipSyntaxLatestError": mipSyntaxLatestError,
       "mipSyntaxActiveTime": mipSyntaxActiveTime,
       "systemErrorPerformance": systemErrorPerformance,
       "sepEtiTable": sepEtiTable,
       "sepEtiEntry": sepEtiEntry,
       "sepEtiInputNumber": sepEtiInputNumber,
       "sepEtiTestState": sepEtiTestState,
       "sepEtiEnable": sepEtiEnable,
       "sepEtiCounter": sepEtiCounter,
       "sepEtiCounterDiscontinuity": sepEtiCounterDiscontinuity,
       "sepEtiCounterReset": sepEtiCounterReset,
       "sepEtiLatestError": sepEtiLatestError,
       "sepEtiActiveTime": sepEtiActiveTime,
       "sepEtiMeasurementState": sepEtiMeasurementState,
       "sepEtiValue": sepEtiValue,
       "sepSetiTable": sepSetiTable,
       "sepSetiEntry": sepSetiEntry,
       "sepSetiInputNumber": sepSetiInputNumber,
       "sepSetiTestState": sepSetiTestState,
       "sepSetiEnable": sepSetiEnable,
       "sepSetiCounter": sepSetiCounter,
       "sepSetiCounterDiscontinuity": sepSetiCounterDiscontinuity,
       "sepSetiCounterReset": sepSetiCounterReset,
       "sepSetiLatestError": sepSetiLatestError,
       "sepSetiActiveTime": sepSetiActiveTime,
       "sepSetiMeasurementState": sepSetiMeasurementState,
       "sepSetiValue": sepSetiValue,
       "terrestrialPreferencesTable": terrestrialPreferencesTable,
       "terrestrialPreferencesEntry": terrestrialPreferencesEntry,
       "terrestrialPrefInputNumber": terrestrialPrefInputNumber,
       "terrestrialPrefCentreFrequency": terrestrialPrefCentreFrequency,
       "terrestrialPrefBandwidth": terrestrialPrefBandwidth,
       "terrestrialPrefModulation": terrestrialPrefModulation,
       "terrestrialPrefTransmissionMode": terrestrialPrefTransmissionMode,
       "terrestrialPrefGuardInterval": terrestrialPrefGuardInterval,
       "terrestrialPrefHierarchical": terrestrialPrefHierarchical,
       "terrestrialPrefCentreFreqExpected": terrestrialPrefCentreFreqExpected,
       "terrestrialPrefCentreFreqLimit": terrestrialPrefCentreFreqLimit,
       "terrestrialPrefChannelWidthLimit": terrestrialPrefChannelWidthLimit,
       "terrestrialPrefSymbolLengthLimit": terrestrialPrefSymbolLengthLimit,
       "terrestrialPrefPowerMin": terrestrialPrefPowerMin,
       "terrestrialPrefPowerMax": terrestrialPrefPowerMax,
       "terrestrialPrefENDBER": terrestrialPrefENDBER,
       "terrestrialPrefENDIdeal": terrestrialPrefENDIdeal,
       "terrestrialPrefENDMax": terrestrialPrefENDMax,
       "terrestrialPrefENFIdeal": terrestrialPrefENFIdeal,
       "terrestrialPrefENFMax": terrestrialPrefENFMax,
       "terrestrialPrefENDLPIdeal": terrestrialPrefENDLPIdeal,
       "terrestrialPrefENDLPMax": terrestrialPrefENDLPMax,
       "terrestrialPrefENFLPIdeal": terrestrialPrefENFLPIdeal,
       "terrestrialPrefENFLPMax": terrestrialPrefENFLPMax,
       "terrestrialPrefLinearityMin": terrestrialPrefLinearityMin,
       "terrestrialPrefBERViterbiMax": terrestrialPrefBERViterbiMax,
       "terrestrialPrefBERViterbiLPMax": terrestrialPrefBERViterbiLPMax,
       "terrestrialPrefBERRSMax": terrestrialPrefBERRSMax,
       "terrestrialPrefBERRSLPMax": terrestrialPrefBERRSLPMax,
       "terrestrialPrefMerTMin": terrestrialPrefMerTMin,
       "terrestrialPrefSteMeanMax": terrestrialPrefSteMeanMax,
       "terrestrialPrefSteDeviationMax": terrestrialPrefSteDeviationMax,
       "terrestrialPrefCsMin": terrestrialPrefCsMin,
       "terrestrialPrefAiMax": terrestrialPrefAiMax,
       "terrestrialPrefQeMax": terrestrialPrefQeMax,
       "terrestrialPrefPjMax": terrestrialPrefPjMax,
       "terrestrialPrefMIPTimingLimit": terrestrialPrefMIPTimingLimit,
       "terrestrialPrefMIPDeviationMax": terrestrialPrefMIPDeviationMax,
       "terrestrialPrefSEPUATMode": terrestrialPrefSEPUATMode,
       "terrestrialPrefSEPN": terrestrialPrefSEPN,
       "terrestrialPrefSEPT": terrestrialPrefSEPT,
       "terrestrialPrefSEPM": terrestrialPrefSEPM,
       "terrestrialPrefSEPTI": terrestrialPrefSEPTI,
       "terrestrialPrefSEPEBPerCent": terrestrialPrefSEPEBPerCent,
       "terrestrialPrefSEPMeasurementInterval": terrestrialPrefSEPMeasurementInterval,
       "tr101290Conformance": tr101290Conformance,
       "tr101290Compliances": tr101290Compliances,
       "complianceTransportStream": complianceTransportStream,
       "complianceCable": complianceCable,
       "complianceSatellite": complianceSatellite,
       "complianceTerrestrial": complianceTerrestrial,
       "tr101290ObjectGroups": tr101290ObjectGroups,
       "groupControl": groupControl,
       "groupTrapControl": groupTrapControl,
       "groupTraps": groupTraps,
       "groupCapability": groupCapability,
       "groupTransportStream": groupTransportStream,
       "groupCable": groupCable,
       "groupSatellite": groupSatellite,
       "groupTerrestrial": groupTerrestrial}
)
