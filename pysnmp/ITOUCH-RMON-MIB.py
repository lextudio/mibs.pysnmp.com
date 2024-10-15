# SNMP MIB module (ITOUCH-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:22 2024
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

(DateTime,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "DateTime",
    "iTouch")

(alarmIndex,
 etherStatsIndex) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "alarmIndex",
    "etherStatsIndex")

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

_XRmon_ObjectIdentity = ObjectIdentity
xRmon = _XRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 31)
)
_XRmonMonitor_ObjectIdentity = ObjectIdentity
xRmonMonitor = _XRmonMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 31, 1)
)


class _XRmonMonitorRemote_Type(Integer32):
    """Custom type xRmonMonitorRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XRmonMonitorRemote_Type.__name__ = "Integer32"
_XRmonMonitorRemote_Object = MibScalar
xRmonMonitorRemote = _XRmonMonitorRemote_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 1),
    _XRmonMonitorRemote_Type()
)
xRmonMonitorRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonMonitorRemote.setStatus("mandatory")


class _XRmonMonitorLocal_Type(Integer32):
    """Custom type xRmonMonitorLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XRmonMonitorLocal_Type.__name__ = "Integer32"
_XRmonMonitorLocal_Object = MibScalar
xRmonMonitorLocal = _XRmonMonitorLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 2),
    _XRmonMonitorLocal_Type()
)
xRmonMonitorLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonMonitorLocal.setStatus("mandatory")


class _XRmonLogClear_Type(Integer32):
    """Custom type xRmonLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_XRmonLogClear_Type.__name__ = "Integer32"
_XRmonLogClear_Object = MibScalar
xRmonLogClear = _XRmonLogClear_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 3),
    _XRmonLogClear_Type()
)
xRmonLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonLogClear.setStatus("mandatory")
_XRmonLogTotal_Type = Counter32
_XRmonLogTotal_Object = MibScalar
xRmonLogTotal = _XRmonLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 4),
    _XRmonLogTotal_Type()
)
xRmonLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonLogTotal.setStatus("mandatory")
_XRmonLogLastDateTime_Type = DateTime
_XRmonLogLastDateTime_Object = MibScalar
xRmonLogLastDateTime = _XRmonLogLastDateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 5),
    _XRmonLogLastDateTime_Type()
)
xRmonLogLastDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonLogLastDateTime.setStatus("mandatory")


class _XRmonTrapType_Type(Integer32):
    """Custom type xRmonTrapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iTouchFormat", 2),
          ("standardFormat", 1))
    )


_XRmonTrapType_Type.__name__ = "Integer32"
_XRmonTrapType_Object = MibScalar
xRmonTrapType = _XRmonTrapType_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 6),
    _XRmonTrapType_Type()
)
xRmonTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonTrapType.setStatus("mandatory")


class _XRmonRepeaterManagement_Type(Integer32):
    """Custom type xRmonRepeaterManagement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XRmonRepeaterManagement_Type.__name__ = "Integer32"
_XRmonRepeaterManagement_Object = MibScalar
xRmonRepeaterManagement = _XRmonRepeaterManagement_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 7),
    _XRmonRepeaterManagement_Type()
)
xRmonRepeaterManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonRepeaterManagement.setStatus("mandatory")


class _XRmonAlarmActivate_Type(Integer32):
    """Custom type xRmonAlarmActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activateAll", 2),
          ("deactivateAll", 3),
          ("noAction", 1))
    )


_XRmonAlarmActivate_Type.__name__ = "Integer32"
_XRmonAlarmActivate_Object = MibScalar
xRmonAlarmActivate = _XRmonAlarmActivate_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 8),
    _XRmonAlarmActivate_Type()
)
xRmonAlarmActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonAlarmActivate.setStatus("mandatory")


class _XRmonAlarmClear_Type(Integer32):
    """Custom type xRmonAlarmClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 2),
          ("noAction", 1))
    )


_XRmonAlarmClear_Type.__name__ = "Integer32"
_XRmonAlarmClear_Object = MibScalar
xRmonAlarmClear = _XRmonAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 9),
    _XRmonAlarmClear_Type()
)
xRmonAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonAlarmClear.setStatus("mandatory")
_XRmonAlarmCount_ObjectIdentity = ObjectIdentity
xRmonAlarmCount = _XRmonAlarmCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 10)
)
_XRmonAlarmsIncomplete_Type = Integer32
_XRmonAlarmsIncomplete_Object = MibScalar
xRmonAlarmsIncomplete = _XRmonAlarmsIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 1),
    _XRmonAlarmsIncomplete_Type()
)
xRmonAlarmsIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonAlarmsIncomplete.setStatus("mandatory")
_XRmonAlarmsActive_Type = Integer32
_XRmonAlarmsActive_Object = MibScalar
xRmonAlarmsActive = _XRmonAlarmsActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 2),
    _XRmonAlarmsActive_Type()
)
xRmonAlarmsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonAlarmsActive.setStatus("mandatory")
_XRmonAlarmsHeld_Type = Integer32
_XRmonAlarmsHeld_Object = MibScalar
xRmonAlarmsHeld = _XRmonAlarmsHeld_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 3),
    _XRmonAlarmsHeld_Type()
)
xRmonAlarmsHeld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonAlarmsHeld.setStatus("mandatory")
_XRmonAlarmsOther_Type = Integer32
_XRmonAlarmsOther_Object = MibScalar
xRmonAlarmsOther = _XRmonAlarmsOther_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 4),
    _XRmonAlarmsOther_Type()
)
xRmonAlarmsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonAlarmsOther.setStatus("mandatory")


class _XRmonAlarmInitAction_Type(Integer32):
    """Custom type xRmonAlarmInitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activateUponInit", 1),
          ("inactiveUponInit", 2))
    )


_XRmonAlarmInitAction_Type.__name__ = "Integer32"
_XRmonAlarmInitAction_Object = MibScalar
xRmonAlarmInitAction = _XRmonAlarmInitAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 1, 11),
    _XRmonAlarmInitAction_Type()
)
xRmonAlarmInitAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonAlarmInitAction.setStatus("mandatory")
_XRmonMB_ObjectIdentity = ObjectIdentity
xRmonMB = _XRmonMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 31, 2)
)
_XRmonMBConfig_ObjectIdentity = ObjectIdentity
xRmonMBConfig = _XRmonMBConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1)
)


class _MbAlarmIndex_Type(Integer32):
    """Custom type mbAlarmIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MbAlarmIndex_Type.__name__ = "Integer32"
_MbAlarmIndex_Object = MibScalar
mbAlarmIndex = _MbAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 1),
    _MbAlarmIndex_Type()
)
mbAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmIndex.setStatus("mandatory")


class _MbAlarmInterval_Type(Integer32):
    """Custom type mbAlarmInterval based on Integer32"""
    defaultValue = 10


_MbAlarmInterval_Object = MibScalar
mbAlarmInterval = _MbAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 2),
    _MbAlarmInterval_Type()
)
mbAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmInterval.setStatus("mandatory")
_MbAlarmVariable_Type = ObjectIdentifier
_MbAlarmVariable_Object = MibScalar
mbAlarmVariable = _MbAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 3),
    _MbAlarmVariable_Type()
)
mbAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmVariable.setStatus("mandatory")


class _MbAlarmInterpretation_Type(Integer32):
    """Custom type mbAlarmInterpretation based on Integer32"""
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
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("chassisSlotIOCardOperStatus", 95),
          ("chassisSlotMinus12Status", 98),
          ("chassisSlotMinus12Watts", 101),
          ("chassisSlotOperStatus", 93),
          ("chassisSlotPlus12Status", 97),
          ("chassisSlotPlus12Watts", 100),
          ("chassisSlotPlus5Status", 96),
          ("chassisSlotPlus5Watts", 99),
          ("chassisSlotSecondsSinceReset", 94),
          ("portAccessAddressViolations", 36),
          ("portAccessState", 35),
          ("portAdminStatus", 39),
          ("portAlignmentErrors", 21),
          ("portAutoPartitionState", 40),
          ("portAutoPartitions", 22),
          ("portBroadcastFrames", 6),
          ("portBroadcastRatio", 18),
          ("portCRCAlignErrors", 24),
          ("portCRCErrors", 25),
          ("portCollisionRatio", 16),
          ("portCollisions", 23),
          ("portDataRateMismatches", 26),
          ("portErrorRatio", 17),
          ("portFrameTooLongErrors", 27),
          ("portFrames1024to1518Octets", 13),
          ("portFrames128to255Octets", 10),
          ("portFrames256to511Octets", 11),
          ("portFrames512to1023Octets", 12),
          ("portFrames64Octets", 8),
          ("portFrames65to127Octets", 9),
          ("portGlobalAddressChanges", 37),
          ("portLateCollisionErrors", 28),
          ("portManchesterCodeViolations", 29),
          ("portMulticastFrames", 7),
          ("portMulticastRatio", 19),
          ("portOperStatus", 41),
          ("portPercentUtilization", 14),
          ("portPulseLosses", 44),
          ("portPulseStatus", 43),
          ("portReadableFrames", 2),
          ("portReadableOctets", 3),
          ("portRunts", 30),
          ("portSecondsSinceCountersZeroed", 45),
          ("portShortPacketErrors", 31),
          ("portSourceAddressChanges", 38),
          ("portStartOfFrameMissing", 32),
          ("portTotalErrors", 34),
          ("portTotalFrames", 4),
          ("portTotalOctets", 5),
          ("portTrafficRatio", 15),
          ("portUnicastRatio", 20),
          ("portVeryLongFrameErrors", 33),
          ("powerSupplyChassisWatts", 115),
          ("powerSupplyChassisWattsMax", 116),
          ("powerSupplyFanStatus", 108),
          ("powerSupplyHardwareInhibitStatus", 109),
          ("powerSupplyHardwareType", 117),
          ("powerSupplyMinus12Status", 105),
          ("powerSupplyMinus12Volts", 112),
          ("powerSupplyPlus12Status", 104),
          ("powerSupplyPlus12Volts", 111),
          ("powerSupplyPlus5Status", 103),
          ("powerSupplyPlus5Volts", 110),
          ("powerSupplyRedundancyStatus", 102),
          ("powerSupplyThermalShutdownStatus", 107),
          ("powerSupplyThermalWarningStatus", 106),
          ("powerSupplyWatts", 113),
          ("powerSupplyWattsMax", 114),
          ("redundancyGroupPathChanges", 67),
          ("redundancyGroupRollbackAttempts", 68),
          ("redundancyPathTestAttempts", 70),
          ("redundancyPathTestStatus", 71),
          ("redundancySecondsSinceCountersZeroed", 69),
          ("repeaterCollisions", 49),
          ("repeaterFifoOverflows", 50),
          ("repeaterJabbers", 51),
          ("repeaterPercentUtilization", 48),
          ("repeaterSQEErrors", 52),
          ("repeaterSecondsSinceCountersZeroed", 53),
          ("repeaterTotalFrames", 46),
          ("repeaterTotalOctets", 47),
          ("slotAlarmCount", 59),
          ("slotCpuUtilization", 57),
          ("slotFifoErrors", 60),
          ("slotIOCardOperStatus", 64),
          ("slotMemoryUtilization", 58),
          ("slotOperStatus", 61),
          ("slotOperStatusChange", 62),
          ("slotSecurityLockState", 63),
          ("slotTotalErrors", 56),
          ("slotTotalFrames", 54),
          ("slotTotalOctets", 55),
          ("systemCurrentFreeMemory", 78),
          ("systemCurrentIPCs", 77),
          ("systemCurrentPackets", 76),
          ("systemCurrentPctCPU", 72),
          ("systemCurrentPctMemory", 73),
          ("systemCurrentProcesses", 74),
          ("systemCurrentTimers", 75),
          ("systemUpTime", 92),
          ("systemWorstFreeMemory", 88),
          ("systemWorstIPCs", 87),
          ("systemWorstPackets", 86),
          ("systemWorstPctCPU", 82),
          ("systemWorstPctMemory", 83),
          ("systemWorstProcesses", 84),
          ("systemWorstTimers", 85),
          ("unlistedAlarmVariable", 1))
    )


_MbAlarmInterpretation_Type.__name__ = "Integer32"
_MbAlarmInterpretation_Object = MibScalar
mbAlarmInterpretation = _MbAlarmInterpretation_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 4),
    _MbAlarmInterpretation_Type()
)
mbAlarmInterpretation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmInterpretation.setStatus("mandatory")


class _MbAlarmKey1Meaning_Type(DisplayString):
    """Custom type mbAlarmKey1Meaning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_MbAlarmKey1Meaning_Type.__name__ = "DisplayString"
_MbAlarmKey1Meaning_Object = MibScalar
mbAlarmKey1Meaning = _MbAlarmKey1Meaning_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 5),
    _MbAlarmKey1Meaning_Type()
)
mbAlarmKey1Meaning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAlarmKey1Meaning.setStatus("mandatory")
_MbAlarmKey1_Type = Integer32
_MbAlarmKey1_Object = MibScalar
mbAlarmKey1 = _MbAlarmKey1_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 6),
    _MbAlarmKey1_Type()
)
mbAlarmKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmKey1.setStatus("mandatory")


class _MbAlarmKey2Meaning_Type(DisplayString):
    """Custom type mbAlarmKey2Meaning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_MbAlarmKey2Meaning_Type.__name__ = "DisplayString"
_MbAlarmKey2Meaning_Object = MibScalar
mbAlarmKey2Meaning = _MbAlarmKey2Meaning_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 7),
    _MbAlarmKey2Meaning_Type()
)
mbAlarmKey2Meaning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAlarmKey2Meaning.setStatus("mandatory")
_MbAlarmKey2_Type = Integer32
_MbAlarmKey2_Object = MibScalar
mbAlarmKey2 = _MbAlarmKey2_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 8),
    _MbAlarmKey2_Type()
)
mbAlarmKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmKey2.setStatus("mandatory")


class _MbAlarmSampleType_Type(Integer32):
    """Custom type mbAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("changeInValue", 2))
    )


_MbAlarmSampleType_Type.__name__ = "Integer32"
_MbAlarmSampleType_Object = MibScalar
mbAlarmSampleType = _MbAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 9),
    _MbAlarmSampleType_Type()
)
mbAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmSampleType.setStatus("mandatory")
_MbAlarmValue_Type = Integer32
_MbAlarmValue_Object = MibScalar
mbAlarmValue = _MbAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 10),
    _MbAlarmValue_Type()
)
mbAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAlarmValue.setStatus("mandatory")
_MbAlarmRisingThreshold_Type = Integer32
_MbAlarmRisingThreshold_Object = MibScalar
mbAlarmRisingThreshold = _MbAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 11),
    _MbAlarmRisingThreshold_Type()
)
mbAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmRisingThreshold.setStatus("mandatory")
_MbAlarmFallingThreshold_Type = Integer32
_MbAlarmFallingThreshold_Object = MibScalar
mbAlarmFallingThreshold = _MbAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 12),
    _MbAlarmFallingThreshold_Type()
)
mbAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmFallingThreshold.setStatus("mandatory")


class _MbAlarmRisingEventType_Type(Integer32):
    """Custom type mbAlarmRisingEventType based on Integer32"""
    defaultValue = 4

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
        *(("logAndTrap", 4),
          ("logOnly", 2),
          ("noAction", 1),
          ("trapOnly", 3))
    )


_MbAlarmRisingEventType_Type.__name__ = "Integer32"
_MbAlarmRisingEventType_Object = MibScalar
mbAlarmRisingEventType = _MbAlarmRisingEventType_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 13),
    _MbAlarmRisingEventType_Type()
)
mbAlarmRisingEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmRisingEventType.setStatus("mandatory")


class _MbAlarmFallingEventType_Type(Integer32):
    """Custom type mbAlarmFallingEventType based on Integer32"""
    defaultValue = 4

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
        *(("logAndTrap", 4),
          ("logOnly", 2),
          ("noAction", 1),
          ("trapOnly", 3))
    )


_MbAlarmFallingEventType_Type.__name__ = "Integer32"
_MbAlarmFallingEventType_Object = MibScalar
mbAlarmFallingEventType = _MbAlarmFallingEventType_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 14),
    _MbAlarmFallingEventType_Type()
)
mbAlarmFallingEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmFallingEventType.setStatus("mandatory")


class _MbAlarmSummary_Type(DisplayString):
    """Custom type mbAlarmSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MbAlarmSummary_Type.__name__ = "DisplayString"
_MbAlarmSummary_Object = MibScalar
mbAlarmSummary = _MbAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 15),
    _MbAlarmSummary_Type()
)
mbAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAlarmSummary.setStatus("mandatory")


class _MbAlarmStatus_Type(Integer32):
    """Custom type mbAlarmStatus based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("activating", 15),
          ("active", 2),
          ("deactivating", 16),
          ("delete", 4),
          ("held", 5),
          ("inaccessible", 22),
          ("inactive", 3),
          ("inconsistency", 19),
          ("invalidFlags", 20),
          ("invalidSlot", 21),
          ("keysMissing", 12),
          ("loading", 14),
          ("monitorStopped", 10),
          ("noHubCard", 6),
          ("noResources", 13),
          ("oldFirmware", 7),
          ("otherError", 23),
          ("slotFailed", 9),
          ("slotTimeout", 8),
          ("underCreation", 1),
          ("unknownAlarm", 18),
          ("unknownVariable", 11),
          ("unsupported", 17))
    )


_MbAlarmStatus_Type.__name__ = "Integer32"
_MbAlarmStatus_Object = MibScalar
mbAlarmStatus = _MbAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 16),
    _MbAlarmStatus_Type()
)
mbAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmStatus.setStatus("mandatory")
_MbAlarmTable_Object = MibTable
mbAlarmTable = _MbAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 2)
)
if mibBuilder.loadTexts:
    mbAlarmTable.setStatus("mandatory")
_MbAlarmEntry_Object = MibTableRow
mbAlarmEntry = _MbAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1)
)
mbAlarmEntry.setIndexNames(
    (0, "RFC1271-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    mbAlarmEntry.setStatus("mandatory")


class _MbAlarmCondition_Type(Integer32):
    """Custom type mbAlarmCondition based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("activating", 15),
          ("active", 2),
          ("deactivating", 16),
          ("delete", 4),
          ("held", 5),
          ("inaccessible", 22),
          ("inactive", 3),
          ("inconsistency", 19),
          ("invalidFlags", 20),
          ("invalidSlot", 21),
          ("keysMissing", 12),
          ("loading", 14),
          ("monitorStopped", 10),
          ("noHubCard", 6),
          ("noResources", 13),
          ("oldFirmware", 7),
          ("otherError", 23),
          ("slotFailed", 9),
          ("slotTimeout", 8),
          ("underCreation", 1),
          ("unknownAlarm", 18),
          ("unknownVariable", 11),
          ("unsupported", 17))
    )


_MbAlarmCondition_Type.__name__ = "Integer32"
_MbAlarmCondition_Object = MibTableColumn
mbAlarmCondition = _MbAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1, 1),
    _MbAlarmCondition_Type()
)
mbAlarmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbAlarmCondition.setStatus("mandatory")


class _MbAlarmDescription_Type(DisplayString):
    """Custom type mbAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MbAlarmDescription_Type.__name__ = "DisplayString"
_MbAlarmDescription_Object = MibTableColumn
mbAlarmDescription = _MbAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1, 2),
    _MbAlarmDescription_Type()
)
mbAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAlarmDescription.setStatus("mandatory")
_MbLogTable_Object = MibTable
mbLogTable = _MbLogTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 3)
)
if mibBuilder.loadTexts:
    mbLogTable.setStatus("mandatory")
_MbLogEntry_Object = MibTableRow
mbLogEntry = _MbLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1)
)
mbLogEntry.setIndexNames(
    (0, "ITOUCH-RMON-MIB", "mbLogIndex"),
)
if mibBuilder.loadTexts:
    mbLogEntry.setStatus("mandatory")
_MbLogIndex_Type = Integer32
_MbLogIndex_Object = MibTableColumn
mbLogIndex = _MbLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1, 1),
    _MbLogIndex_Type()
)
mbLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbLogIndex.setStatus("mandatory")


class _MbLogDescription_Type(DisplayString):
    """Custom type mbLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MbLogDescription_Type.__name__ = "DisplayString"
_MbLogDescription_Object = MibTableColumn
mbLogDescription = _MbLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1, 2),
    _MbLogDescription_Type()
)
mbLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbLogDescription.setStatus("mandatory")
_MbResourceTable_Object = MibTable
mbResourceTable = _MbResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4)
)
if mibBuilder.loadTexts:
    mbResourceTable.setStatus("mandatory")
_MbResourceEntry_Object = MibTableRow
mbResourceEntry = _MbResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1)
)
mbResourceEntry.setIndexNames(
    (0, "ITOUCH-RMON-MIB", "mbResourceType"),
)
if mibBuilder.loadTexts:
    mbResourceEntry.setStatus("mandatory")


class _MbResourceType_Type(Integer32):
    """Custom type mbResourceType based on Integer32"""
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
        *(("rmonAlarms", 1),
          ("rmonEvents", 2),
          ("rmonLogEntries", 3),
          ("rmonStatistics", 4))
    )


_MbResourceType_Type.__name__ = "Integer32"
_MbResourceType_Object = MibTableColumn
mbResourceType = _MbResourceType_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 1),
    _MbResourceType_Type()
)
mbResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbResourceType.setStatus("mandatory")
_MbResourceCurrent_Type = Gauge32
_MbResourceCurrent_Object = MibTableColumn
mbResourceCurrent = _MbResourceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 2),
    _MbResourceCurrent_Type()
)
mbResourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbResourceCurrent.setStatus("mandatory")
_MbResourceWorst_Type = Gauge32
_MbResourceWorst_Object = MibTableColumn
mbResourceWorst = _MbResourceWorst_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 3),
    _MbResourceWorst_Type()
)
mbResourceWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbResourceWorst.setStatus("mandatory")
_MbResourceMaximum_Type = Integer32
_MbResourceMaximum_Object = MibTableColumn
mbResourceMaximum = _MbResourceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 4),
    _MbResourceMaximum_Type()
)
mbResourceMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbResourceMaximum.setStatus("mandatory")
_MbResourceOperMaximum_Type = Integer32
_MbResourceOperMaximum_Object = MibTableColumn
mbResourceOperMaximum = _MbResourceOperMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 5),
    _MbResourceOperMaximum_Type()
)
mbResourceOperMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbResourceOperMaximum.setStatus("mandatory")
_XRmonMapTable_Object = MibTable
xRmonMapTable = _XRmonMapTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 3)
)
if mibBuilder.loadTexts:
    xRmonMapTable.setStatus("mandatory")
_XRmonMapEntry_Object = MibTableRow
xRmonMapEntry = _XRmonMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 3, 1)
)
xRmonMapEntry.setIndexNames(
    (0, "RFC1271-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    xRmonMapEntry.setStatus("mandatory")
_XRmonMapSlot_Type = Integer32
_XRmonMapSlot_Object = MibTableColumn
xRmonMapSlot = _XRmonMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 1),
    _XRmonMapSlot_Type()
)
xRmonMapSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonMapSlot.setStatus("mandatory")
_XRmonMapPort_Type = Integer32
_XRmonMapPort_Object = MibTableColumn
xRmonMapPort = _XRmonMapPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 2),
    _XRmonMapPort_Type()
)
xRmonMapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRmonMapPort.setStatus("mandatory")
_XRmonMapIfIndex_Type = Integer32
_XRmonMapIfIndex_Object = MibTableColumn
xRmonMapIfIndex = _XRmonMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 3),
    _XRmonMapIfIndex_Type()
)
xRmonMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRmonMapIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects

iTouchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 31, 0, 1)
)
iTouchAlarm.setObjects(
    ("ITOUCH-RMON-MIB", "mbLogDescription")
)
if mibBuilder.loadTexts:
    iTouchAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-RMON-MIB",
    **{"xRmon": xRmon,
       "iTouchAlarm": iTouchAlarm,
       "xRmonMonitor": xRmonMonitor,
       "xRmonMonitorRemote": xRmonMonitorRemote,
       "xRmonMonitorLocal": xRmonMonitorLocal,
       "xRmonLogClear": xRmonLogClear,
       "xRmonLogTotal": xRmonLogTotal,
       "xRmonLogLastDateTime": xRmonLogLastDateTime,
       "xRmonTrapType": xRmonTrapType,
       "xRmonRepeaterManagement": xRmonRepeaterManagement,
       "xRmonAlarmActivate": xRmonAlarmActivate,
       "xRmonAlarmClear": xRmonAlarmClear,
       "xRmonAlarmCount": xRmonAlarmCount,
       "xRmonAlarmsIncomplete": xRmonAlarmsIncomplete,
       "xRmonAlarmsActive": xRmonAlarmsActive,
       "xRmonAlarmsHeld": xRmonAlarmsHeld,
       "xRmonAlarmsOther": xRmonAlarmsOther,
       "xRmonAlarmInitAction": xRmonAlarmInitAction,
       "xRmonMB": xRmonMB,
       "xRmonMBConfig": xRmonMBConfig,
       "mbAlarmIndex": mbAlarmIndex,
       "mbAlarmInterval": mbAlarmInterval,
       "mbAlarmVariable": mbAlarmVariable,
       "mbAlarmInterpretation": mbAlarmInterpretation,
       "mbAlarmKey1Meaning": mbAlarmKey1Meaning,
       "mbAlarmKey1": mbAlarmKey1,
       "mbAlarmKey2Meaning": mbAlarmKey2Meaning,
       "mbAlarmKey2": mbAlarmKey2,
       "mbAlarmSampleType": mbAlarmSampleType,
       "mbAlarmValue": mbAlarmValue,
       "mbAlarmRisingThreshold": mbAlarmRisingThreshold,
       "mbAlarmFallingThreshold": mbAlarmFallingThreshold,
       "mbAlarmRisingEventType": mbAlarmRisingEventType,
       "mbAlarmFallingEventType": mbAlarmFallingEventType,
       "mbAlarmSummary": mbAlarmSummary,
       "mbAlarmStatus": mbAlarmStatus,
       "mbAlarmTable": mbAlarmTable,
       "mbAlarmEntry": mbAlarmEntry,
       "mbAlarmCondition": mbAlarmCondition,
       "mbAlarmDescription": mbAlarmDescription,
       "mbLogTable": mbLogTable,
       "mbLogEntry": mbLogEntry,
       "mbLogIndex": mbLogIndex,
       "mbLogDescription": mbLogDescription,
       "mbResourceTable": mbResourceTable,
       "mbResourceEntry": mbResourceEntry,
       "mbResourceType": mbResourceType,
       "mbResourceCurrent": mbResourceCurrent,
       "mbResourceWorst": mbResourceWorst,
       "mbResourceMaximum": mbResourceMaximum,
       "mbResourceOperMaximum": mbResourceOperMaximum,
       "xRmonMapTable": xRmonMapTable,
       "xRmonMapEntry": xRmonMapEntry,
       "xRmonMapSlot": xRmonMapSlot,
       "xRmonMapPort": xRmonMapPort,
       "xRmonMapIfIndex": xRmonMapIfIndex}
)
