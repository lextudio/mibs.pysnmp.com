# SNMP MIB module (SYMMCOMMONPPSTOD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMCOMMONPPSTOD
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:46 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(symmPhysicalSignal,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmPPSTOD = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3)
)


# Types definitions



class EnaValue(Integer32):
    """Custom type EnaValue based on Integer32"""
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





class TODPortType(Integer32):
    """Custom type TODPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("error", 2),
          ("normal", 1))
    )





class TPModuleID(Integer32):
    """Custom type TPModuleID based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("exp0", 5),
          ("exp1", 6),
          ("exp2", 7),
          ("exp3", 8),
          ("exp4", 9),
          ("exp5", 10),
          ("exp6", 11),
          ("exp7", 12),
          ("exp8", 13),
          ("exp9", 14),
          ("imc", 2),
          ("ioc1", 3),
          ("ioc2", 4),
          ("sys", 1))
    )





class OnValue(Integer32):
    """Custom type OnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )





class TPOutputType(Integer32):
    """Custom type TPOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("output10Mhz", 2),
          ("outputGeneral", 1),
          ("outputPPS", 3))
    )





class TPOutputGeneration(Integer32):
    """Custom type TPOutputGeneration based on Integer32"""
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
        *(("fastlock", 3),
          ("freerun", 2),
          ("normal", 4),
          ("warmup", 1))
    )





class OutputFrameType(Integer32):
    """Custom type OutputFrameType based on Integer32"""
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
        *(("cas", 4),
          ("ccs", 3),
          ("d4", 5),
          ("esf", 6),
          ("freq1544khz", 1),
          ("freq2048khz", 2))
    )





class ActionApply(Integer32):
    """Custom type ActionApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("nonapply", 2))
    )





class OpMode(Integer32):
    """Custom type OpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )





class ActiveValue(Integer32):
    """Custom type ActiveValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class InputQualityLevel(Integer32):
    """Custom type InputQualityLevel based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dus", 9),
          ("opt3smc", 8),
          ("prcprs", 1),
          ("typei", 4),
          ("typeiiist3e", 6),
          ("typeiist2", 3),
          ("typeivst3", 7),
          ("typevtnc", 5),
          ("unkstu", 2))
    )





class InputPriority(Integer32):
    """Custom type InputPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )





class YesValue(Integer32):
    """Custom type YesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )





class OkValue(Integer32):
    """Custom type OkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("ok", 1))
    )





class ValidValue(Integer32):
    """Custom type ValidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("nurture", 3),
          ("valid", 1))
    )





class TODInputFrameType(Integer32):
    """Custom type TODInputFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chinaMobile", 1),
          ("ntp4", 2))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_PpstodInput_ObjectIdentity = ObjectIdentity
ppstodInput = _PpstodInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1)
)
_PpstodInputStatus_ObjectIdentity = ObjectIdentity
ppstodInputStatus = _PpstodInputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1)
)
_PpstodInputStatusTable_Object = MibTable
ppstodInputStatusTable = _PpstodInputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ppstodInputStatusTable.setStatus("current")
_PpstodInputStatusEntry_Object = MibTableRow
ppstodInputStatusEntry = _PpstodInputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1)
)
ppstodInputStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPPSTOD", "ppstodInputStatusIndex"),
)
if mibBuilder.loadTexts:
    ppstodInputStatusEntry.setStatus("current")


class _PpstodInputStatusIndex_Type(Integer32):
    """Custom type ppstodInputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PpstodInputStatusIndex_Type.__name__ = "Integer32"
_PpstodInputStatusIndex_Object = MibTableColumn
ppstodInputStatusIndex = _PpstodInputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 1),
    _PpstodInputStatusIndex_Type()
)
ppstodInputStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppstodInputStatusIndex.setStatus("current")
_PpstodInputPortStatus_Type = TODPortType
_PpstodInputPortStatus_Object = MibTableColumn
ppstodInputPortStatus = _PpstodInputPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 2),
    _PpstodInputPortStatus_Type()
)
ppstodInputPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputPortStatus.setStatus("current")
_PpstodInputPPSStatus_Type = DisplayString
_PpstodInputPPSStatus_Object = MibTableColumn
ppstodInputPPSStatus = _PpstodInputPPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 3),
    _PpstodInputPPSStatus_Type()
)
ppstodInputPPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputPPSStatus.setStatus("current")
_PpstodInputPhaseOffset_Type = DisplayString
_PpstodInputPhaseOffset_Object = MibTableColumn
ppstodInputPhaseOffset = _PpstodInputPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 4),
    _PpstodInputPhaseOffset_Type()
)
ppstodInputPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputPhaseOffset.setStatus("current")
_PpstodInputClockSourceType_Type = DisplayString
_PpstodInputClockSourceType_Object = MibTableColumn
ppstodInputClockSourceType = _PpstodInputClockSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 5),
    _PpstodInputClockSourceType_Type()
)
ppstodInputClockSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputClockSourceType.setStatus("current")
_PpstodInputClockSourceStatus_Type = DisplayString
_PpstodInputClockSourceStatus_Object = MibTableColumn
ppstodInputClockSourceStatus = _PpstodInputClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 6),
    _PpstodInputClockSourceStatus_Type()
)
ppstodInputClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputClockSourceStatus.setStatus("current")
_PpstodInputAccuracy_Type = DisplayString
_PpstodInputAccuracy_Object = MibTableColumn
ppstodInputAccuracy = _PpstodInputAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 7),
    _PpstodInputAccuracy_Type()
)
ppstodInputAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputAccuracy.setStatus("current")
_PpstodInputAlarm_Type = DisplayString
_PpstodInputAlarm_Object = MibTableColumn
ppstodInputAlarm = _PpstodInputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 8),
    _PpstodInputAlarm_Type()
)
ppstodInputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstodInputAlarm.setStatus("current")
_PpstodInputConfig_ObjectIdentity = ObjectIdentity
ppstodInputConfig = _PpstodInputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2)
)
_PpstodInputTable_Object = MibTable
ppstodInputTable = _PpstodInputTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ppstodInputTable.setStatus("current")
_PpstodInputEntry_Object = MibTableRow
ppstodInputEntry = _PpstodInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1)
)
ppstodInputEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPPSTOD", "ppstodInputIndex"),
)
if mibBuilder.loadTexts:
    ppstodInputEntry.setStatus("current")


class _PpstodInputIndex_Type(Integer32):
    """Custom type ppstodInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PpstodInputIndex_Type.__name__ = "Integer32"
_PpstodInputIndex_Object = MibTableColumn
ppstodInputIndex = _PpstodInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 1),
    _PpstodInputIndex_Type()
)
ppstodInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppstodInputIndex.setStatus("current")
_PpstodInputCableDelay_Type = Integer32
_PpstodInputCableDelay_Object = MibTableColumn
ppstodInputCableDelay = _PpstodInputCableDelay_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 5),
    _PpstodInputCableDelay_Type()
)
ppstodInputCableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppstodInputCableDelay.setStatus("current")
_PpstodInputFormat_Type = TODInputFrameType
_PpstodInputFormat_Object = MibTableColumn
ppstodInputFormat = _PpstodInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 6),
    _PpstodInputFormat_Type()
)
ppstodInputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppstodInputFormat.setStatus("current")


class _PpstodInputManualLeapSeconds_Type(Integer32):
    """Custom type ppstodInputManualLeapSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_PpstodInputManualLeapSeconds_Type.__name__ = "Integer32"
_PpstodInputManualLeapSeconds_Object = MibTableColumn
ppstodInputManualLeapSeconds = _PpstodInputManualLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 7),
    _PpstodInputManualLeapSeconds_Type()
)
ppstodInputManualLeapSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppstodInputManualLeapSeconds.setStatus("current")
_PpstodOutput_ObjectIdentity = ObjectIdentity
ppstodOutput = _PpstodOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2)
)
_PpstodOutputStatus_ObjectIdentity = ObjectIdentity
ppstodOutputStatus = _PpstodOutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 1)
)
_PpstodOutputConfig_ObjectIdentity = ObjectIdentity
ppstodOutputConfig = _PpstodOutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 2)
)
_PpstodConformance_ObjectIdentity = ObjectIdentity
ppstodConformance = _PpstodConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ppstodConformance.setStatus("current")
_PpstodCompliances_ObjectIdentity = ObjectIdentity
ppstodCompliances = _PpstodCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1)
)
_PpstodUocGroups_ObjectIdentity = ObjectIdentity
ppstodUocGroups = _PpstodUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2)
)

# Managed Objects groups

ppstodInputConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2, 1)
)
ppstodInputConfigGroup.setObjects(
      *(("SYMMCOMMONPPSTOD", "ppstodInputCableDelay"),
        ("SYMMCOMMONPPSTOD", "ppstodInputFormat"),
        ("SYMMCOMMONPPSTOD", "ppstodInputManualLeapSeconds"),
        ("SYMMCOMMONPPSTOD", "ppstodInputPortStatus"),
        ("SYMMCOMMONPPSTOD", "ppstodInputPPSStatus"),
        ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceType"),
        ("SYMMCOMMONPPSTOD", "ppstodInputPhaseOffset"),
        ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceStatus"),
        ("SYMMCOMMONPPSTOD", "ppstodInputAccuracy"),
        ("SYMMCOMMONPPSTOD", "ppstodInputAlarm"))
)
if mibBuilder.loadTexts:
    ppstodInputConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ppstodBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ppstodBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMCOMMONPPSTOD",
    **{"EnaValue": EnaValue,
       "TODPortType": TODPortType,
       "TPModuleID": TPModuleID,
       "OnValue": OnValue,
       "TPOutputType": TPOutputType,
       "TPOutputGeneration": TPOutputGeneration,
       "OutputFrameType": OutputFrameType,
       "ActionApply": ActionApply,
       "OpMode": OpMode,
       "ActiveValue": ActiveValue,
       "InputQualityLevel": InputQualityLevel,
       "InputPriority": InputPriority,
       "YesValue": YesValue,
       "OkValue": OkValue,
       "ValidValue": ValidValue,
       "TODInputFrameType": TODInputFrameType,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmPPSTOD": symmPPSTOD,
       "ppstodInput": ppstodInput,
       "ppstodInputStatus": ppstodInputStatus,
       "ppstodInputStatusTable": ppstodInputStatusTable,
       "ppstodInputStatusEntry": ppstodInputStatusEntry,
       "ppstodInputStatusIndex": ppstodInputStatusIndex,
       "ppstodInputPortStatus": ppstodInputPortStatus,
       "ppstodInputPPSStatus": ppstodInputPPSStatus,
       "ppstodInputPhaseOffset": ppstodInputPhaseOffset,
       "ppstodInputClockSourceType": ppstodInputClockSourceType,
       "ppstodInputClockSourceStatus": ppstodInputClockSourceStatus,
       "ppstodInputAccuracy": ppstodInputAccuracy,
       "ppstodInputAlarm": ppstodInputAlarm,
       "ppstodInputConfig": ppstodInputConfig,
       "ppstodInputTable": ppstodInputTable,
       "ppstodInputEntry": ppstodInputEntry,
       "ppstodInputIndex": ppstodInputIndex,
       "ppstodInputCableDelay": ppstodInputCableDelay,
       "ppstodInputFormat": ppstodInputFormat,
       "ppstodInputManualLeapSeconds": ppstodInputManualLeapSeconds,
       "ppstodOutput": ppstodOutput,
       "ppstodOutputStatus": ppstodOutputStatus,
       "ppstodOutputConfig": ppstodOutputConfig,
       "ppstodConformance": ppstodConformance,
       "ppstodCompliances": ppstodCompliances,
       "ppstodBasicCompliance": ppstodBasicCompliance,
       "ppstodUocGroups": ppstodUocGroups,
       "ppstodInputConfigGroup": ppstodInputConfigGroup}
)
