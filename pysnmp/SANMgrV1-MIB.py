# SNMP MIB module (SANMgrV1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SANMgrV1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:42 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ProductID(ObjectIdentifier):
    """Custom type ProductID based on ObjectIdentifier"""




class PathlightProduct(Integer32):
    """Custom type PathlightProduct based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("adicFCR2", 4),
          ("adicHoneoye", 8),
          ("dellFCR2", 5),
          ("dellHoneoye", 9),
          ("ibmGatewayModule", 11),
          ("sanBridge", 3),
          ("sanGateway", 1),
          ("sanHoneoye", 7),
          ("sanRouter", 2),
          ("siemensFCR2", 6),
          ("siemensHoneoye", 10))
    )





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





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class LogCommand(Integer32):
    """Custom type LogCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 4),
          ("doHealthCheck", 8),
          ("idle", 0),
          ("logModeAbsolute", 7),
          ("logModeCurrent", 6),
          ("removeFile", 5),
          ("save", 3),
          ("scroll", 2),
          ("snapshot", 1))
    )





class PltStatus(Integer32):
    """Custom type PltStatus based on Integer32"""
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
        *(("down", 2),
          ("failed", 1),
          ("testing", 3),
          ("up", 4))
    )





class FcStatus(Integer32):
    """Custom type FcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("configWait", 0),
          ("error", 5),
          ("failed", 8),
          ("login", 2),
          ("loopInit", 1),
          ("lostSync", 4),
          ("nonPart", 7),
          ("ready", 3),
          ("reinit", 6))
    )





class Interface(Integer32):
    """Custom type Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("ethernet", 5),
          ("fibreChannel", 3),
          ("none", 0),
          ("sanGateway", 1),
          ("sanReplication", 8),
          ("scsi", 4),
          ("ssa", 2),
          ("unknown", 6))
    )





class Reset(Integer32):
    """Custom type Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 2),
          ("reset", 1),
          ("run", 0))
    )





class BaudRate(Integer32):
    """Custom type BaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baud19200", 1),
          ("baud38400", 2),
          ("baud9600", 0))
    )





class HealthCheckLevel(Integer32):
    """Custom type HealthCheckLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deviceReady", 4),
          ("interface", 2),
          ("none", 0),
          ("simpleDevice", 3),
          ("system", 1))
    )





class LogViewingLevel(Integer32):
    """Custom type LogViewingLevel based on Integer32"""
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
        *(("information", 3),
          ("notice", 1),
          ("private", 0),
          ("warning", 2))
    )





class DeviceType(Integer32):
    """Custom type DeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("ascIt81", 10),
          ("ascIt82", 11),
          ("cd", 5),
          ("communications", 9),
          ("directAccess", 0),
          ("enclosure", 13),
          ("mediumChanger", 8),
          ("opticalCardReader", 15),
          ("opticalMemory", 7),
          ("printer", 2),
          ("processor", 3),
          ("scanner", 6),
          ("sequentialAccess", 1),
          ("simplifiedDirectAccess", 14),
          ("storageArrayController", 12),
          ("unknown", 31),
          ("worm", 4))
    )





class VendorIDInt(Integer32):
    """Custom type VendorIDInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              4130,
              4215,
              4537)
        )
    )
    namedValues = NamedValues(
        *(("amd", 4130),
          ("pathlight", 4537),
          ("qlogic", 4215),
          ("symbios", 4096),
          ("unknown", 0))
    )





class FibreMedia(Integer32):
    """Custom type FibreMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("gbicCopperDB9OneGB", 13),
          ("gbicCopperDB9TwoGB", 19),
          ("gbicCopperHSSDCOneGB", 12),
          ("gbicCopperHSSDCTwoGB", 18),
          ("gbicLW1300HPOneGB", 10),
          ("gbicLW1300HPTwoGB", 16),
          ("gbicLW1300OneGB", 9),
          ("gbicLW1300TwoGB", 15),
          ("gbicLW1550HPOneGB", 11),
          ("gbicLW1550HPTwoGB", 17),
          ("gbicSWOneGB", 8),
          ("gbicSWTwoGB", 14),
          ("longWaveOptical", 3),
          ("longWaveOpticalDual", 5),
          ("longWaveOpticalLongDistance", 7),
          ("noGBIC", 20),
          ("shortWaveOptical", 2),
          ("shortWaveOpticalDual", 4),
          ("shortWaveOpticalLongDistance", 6),
          ("unknown", 0))
    )





class FibrePort(Integer32):
    """Custom type FibrePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fabric", 4),
          ("fabricLoop", 3),
          ("node", 1),
          ("nodeLoop", 0),
          ("none", 255))
    )





class FibreLoopIDMode(Integer32):
    """Custom type FibreLoopIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0))
    )





class FibrePortMode(Integer32):
    """Custom type FibrePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("privateInitiatorOnly", 2),
          ("privateTargetAndInitiator", 3),
          ("privateTargetOnly", 1),
          ("publicInitiatorOnly", 18),
          ("publicTargetAndInitiator", 19),
          ("publicTargetOnly", 17))
    )





class FibreConnOptions(Integer32):
    """Custom type FibreConnOptions based on Integer32"""
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
        *(("loopOnly", 0),
          ("loopPreferred", 2),
          ("pointToPointOnly", 1),
          ("pointToPointPreferred", 3))
    )





class SsaSpeed(Integer32):
    """Custom type SsaSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssa160", 2),
          ("ssa80", 1))
    )





class PathingAlgorithm(Integer32):
    """Custom type PathingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("skipInitiators", 1),
          ("unknown", 2))
    )





class ScsiSpeed(Integer32):
    """Custom type ScsiSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("async", 0),
          ("fast", 1),
          ("ultra", 2),
          ("ultra160", 4),
          ("ultra2", 3))
    )





class ScsiRole(Integer32):
    """Custom type ScsiRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 0))
    )





class ScsiTermination(Integer32):
    """Custom type ScsiTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notPresent", 2))
    )





class ScsiCardType(Integer32):
    """Custom type ScsiCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("differentialNoTermination", 1),
          ("differentialTerminated", 2),
          ("lowVoltageDifferential", 7),
          ("lowVoltageMultiFunction", 8),
          ("lowVoltageSingleEnded", 6),
          ("none", 0),
          ("singleEndedNoTermination", 3),
          ("singleEndedTerminated", 4),
          ("unknown", 5))
    )





class ScsiAnsiLevel(Integer32):
    """Custom type ScsiAnsiLevel based on Integer32"""
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
        *(("notScsi", 0),
          ("scsi-1", 1),
          ("scsi-2", 2),
          ("scsi-3", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pathlight_ObjectIdentity = ObjectIdentity
pathlight = _Pathlight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 1)
)
_SanGateway_ObjectIdentity = ObjectIdentity
sanGateway = _SanGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 1, 1)
)
_SanGateway1_ObjectIdentity = ObjectIdentity
sanGateway1 = _SanGateway1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 1, 1, 1)
)
_SanGateway2_ObjectIdentity = ObjectIdentity
sanGateway2 = _SanGateway2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 1, 1, 2)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 2)
)
_PaIdentify_Type = Integer32
_PaIdentify_Object = MibScalar
paIdentify = _PaIdentify_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 1),
    _PaIdentify_Type()
)
paIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paIdentify.setStatus("mandatory")
_PaReboot_Type = Reset
_PaReboot_Object = MibScalar
paReboot = _PaReboot_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 2),
    _PaReboot_Type()
)
paReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paReboot.setStatus("mandatory")
_PaHealthCheckValue_Type = Gauge32
_PaHealthCheckValue_Object = MibScalar
paHealthCheckValue = _PaHealthCheckValue_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 3),
    _PaHealthCheckValue_Type()
)
paHealthCheckValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paHealthCheckValue.setStatus("mandatory")
_PaHealthCheckLevel_Type = HealthCheckLevel
_PaHealthCheckLevel_Object = MibScalar
paHealthCheckLevel = _PaHealthCheckLevel_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 4),
    _PaHealthCheckLevel_Type()
)
paHealthCheckLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paHealthCheckLevel.setStatus("mandatory")
_PaHealthCheckInterval_Type = Gauge32
_PaHealthCheckInterval_Object = MibScalar
paHealthCheckInterval = _PaHealthCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 5),
    _PaHealthCheckInterval_Type()
)
paHealthCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paHealthCheckInterval.setStatus("mandatory")
_PaEvRptLevel_Type = LogViewingLevel
_PaEvRptLevel_Object = MibScalar
paEvRptLevel = _PaEvRptLevel_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 6),
    _PaEvRptLevel_Type()
)
paEvRptLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paEvRptLevel.setStatus("mandatory")


class _PaEventLogLevels_Type(OctetString):
    """Custom type paEventLogLevels based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_PaEventLogLevels_Type.__name__ = "OctetString"
_PaEventLogLevels_Object = MibScalar
paEventLogLevels = _PaEventLogLevels_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 7),
    _PaEventLogLevels_Type()
)
paEventLogLevels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paEventLogLevels.setStatus("mandatory")


class _PaTrapThresholds_Type(OctetString):
    """Custom type paTrapThresholds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_PaTrapThresholds_Type.__name__ = "OctetString"
_PaTrapThresholds_Object = MibScalar
paTrapThresholds = _PaTrapThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 8),
    _PaTrapThresholds_Type()
)
paTrapThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paTrapThresholds.setStatus("mandatory")
_PaBaudRate_Type = BaudRate
_PaBaudRate_Object = MibScalar
paBaudRate = _PaBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 9),
    _PaBaudRate_Type()
)
paBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paBaudRate.setStatus("mandatory")
_PaEventLog_Object = MibTable
paEventLog = _PaEventLog_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10)
)
if mibBuilder.loadTexts:
    paEventLog.setStatus("mandatory")
_PaEventLogEntry_Object = MibTableRow
paEventLogEntry = _PaEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1)
)
paEventLogEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "paIndex"),
)
if mibBuilder.loadTexts:
    paEventLogEntry.setStatus("mandatory")
_PaIndex_Type = Integer32
_PaIndex_Object = MibTableColumn
paIndex = _PaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 1),
    _PaIndex_Type()
)
paIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paIndex.setStatus("mandatory")
_PaTime_Type = TimeTicks
_PaTime_Object = MibTableColumn
paTime = _PaTime_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 2),
    _PaTime_Type()
)
paTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paTime.setStatus("mandatory")
_PaProducer_Type = Integer32
_PaProducer_Object = MibTableColumn
paProducer = _PaProducer_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 3),
    _PaProducer_Type()
)
paProducer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paProducer.setStatus("mandatory")
_PaEventClass_Type = Integer32
_PaEventClass_Object = MibTableColumn
paEventClass = _PaEventClass_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 4),
    _PaEventClass_Type()
)
paEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paEventClass.setStatus("mandatory")
_PaEventCode_Type = Integer32
_PaEventCode_Object = MibTableColumn
paEventCode = _PaEventCode_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 5),
    _PaEventCode_Type()
)
paEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paEventCode.setStatus("mandatory")
_PaSeq_Type = Integer32
_PaSeq_Object = MibTableColumn
paSeq = _PaSeq_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 6),
    _PaSeq_Type()
)
paSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paSeq.setStatus("mandatory")


class _PaEventVars_Type(DisplayString):
    """Custom type paEventVars based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PaEventVars_Type.__name__ = "DisplayString"
_PaEventVars_Object = MibTableColumn
paEventVars = _PaEventVars_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 10, 1, 7),
    _PaEventVars_Type()
)
paEventVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paEventVars.setStatus("mandatory")
_PaLogSize_Type = Gauge32
_PaLogSize_Object = MibScalar
paLogSize = _PaLogSize_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 11),
    _PaLogSize_Type()
)
paLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogSize.setStatus("mandatory")
_PaCommand_Type = LogCommand
_PaCommand_Object = MibScalar
paCommand = _PaCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 12),
    _PaCommand_Type()
)
paCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paCommand.setStatus("mandatory")
_PaLogBoot_Type = Gauge32
_PaLogBoot_Object = MibScalar
paLogBoot = _PaLogBoot_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 13),
    _PaLogBoot_Type()
)
paLogBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paLogBoot.setStatus("mandatory")
_PaLogNCurrent_Type = Gauge32
_PaLogNCurrent_Object = MibScalar
paLogNCurrent = _PaLogNCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 14),
    _PaLogNCurrent_Type()
)
paLogNCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogNCurrent.setStatus("mandatory")
_PaLogChronFirst_Type = Gauge32
_PaLogChronFirst_Object = MibScalar
paLogChronFirst = _PaLogChronFirst_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 15),
    _PaLogChronFirst_Type()
)
paLogChronFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogChronFirst.setStatus("mandatory")
_PaLogChronLast_Type = Gauge32
_PaLogChronLast_Object = MibScalar
paLogChronLast = _PaLogChronLast_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 16),
    _PaLogChronLast_Type()
)
paLogChronLast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogChronLast.setStatus("mandatory")
_PaLogScroll_Type = Integer32
_PaLogScroll_Object = MibScalar
paLogScroll = _PaLogScroll_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 17),
    _PaLogScroll_Type()
)
paLogScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogScroll.setStatus("mandatory")


class _PaLogFilename_Type(DisplayString):
    """Custom type paLogFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PaLogFilename_Type.__name__ = "DisplayString"
_PaLogFilename_Object = MibScalar
paLogFilename = _PaLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 18),
    _PaLogFilename_Type()
)
paLogFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLogFilename.setStatus("mandatory")
_PaEnvironmentState_Type = Integer32
_PaEnvironmentState_Object = MibScalar
paEnvironmentState = _PaEnvironmentState_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 19),
    _PaEnvironmentState_Type()
)
paEnvironmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paEnvironmentState.setStatus("mandatory")


class _PaGatewayFWRev_Type(DisplayString):
    """Custom type paGatewayFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PaGatewayFWRev_Type.__name__ = "DisplayString"
_PaGatewayFWRev_Object = MibScalar
paGatewayFWRev = _PaGatewayFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 20),
    _PaGatewayFWRev_Type()
)
paGatewayFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paGatewayFWRev.setStatus("mandatory")


class _PaGatewayHWRev_Type(DisplayString):
    """Custom type paGatewayHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PaGatewayHWRev_Type.__name__ = "DisplayString"
_PaGatewayHWRev_Object = MibScalar
paGatewayHWRev = _PaGatewayHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 21),
    _PaGatewayHWRev_Type()
)
paGatewayHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paGatewayHWRev.setStatus("mandatory")


class _PaSnmpFWRev_Type(DisplayString):
    """Custom type paSnmpFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PaSnmpFWRev_Type.__name__ = "DisplayString"
_PaSnmpFWRev_Object = MibScalar
paSnmpFWRev = _PaSnmpFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 22),
    _PaSnmpFWRev_Type()
)
paSnmpFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paSnmpFWRev.setStatus("mandatory")


class _PaRidTag_Type(DisplayString):
    """Custom type paRidTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PaRidTag_Type.__name__ = "DisplayString"
_PaRidTag_Object = MibScalar
paRidTag = _PaRidTag_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 23),
    _PaRidTag_Type()
)
paRidTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paRidTag.setStatus("mandatory")


class _PaSerialNumber_Type(DisplayString):
    """Custom type paSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PaSerialNumber_Type.__name__ = "DisplayString"
_PaSerialNumber_Object = MibScalar
paSerialNumber = _PaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 24),
    _PaSerialNumber_Type()
)
paSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paSerialNumber.setStatus("mandatory")
_PaServerVersion_Type = Integer32
_PaServerVersion_Object = MibScalar
paServerVersion = _PaServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 25),
    _PaServerVersion_Type()
)
paServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paServerVersion.setStatus("mandatory")
_PaProductType_Type = PathlightProduct
_PaProductType_Object = MibScalar
paProductType = _PaProductType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 26),
    _PaProductType_Type()
)
paProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paProductType.setStatus("mandatory")
_PaVPSEnabled_Type = Boolean
_PaVPSEnabled_Object = MibScalar
paVPSEnabled = _PaVPSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 27),
    _PaVPSEnabled_Type()
)
paVPSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paVPSEnabled.setStatus("mandatory")


class _PaLicenseKey_Type(DisplayString):
    """Custom type paLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PaLicenseKey_Type.__name__ = "DisplayString"
_PaLicenseKey_Object = MibScalar
paLicenseKey = _PaLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 28),
    _PaLicenseKey_Type()
)
paLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paLicenseKey.setStatus("mandatory")
_PaThirdPartyCopyEnabled_Type = Boolean
_PaThirdPartyCopyEnabled_Object = MibScalar
paThirdPartyCopyEnabled = _PaThirdPartyCopyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 29),
    _PaThirdPartyCopyEnabled_Type()
)
paThirdPartyCopyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paThirdPartyCopyEnabled.setStatus("mandatory")
_PaVPSStatus_Type = Integer32
_PaVPSStatus_Object = MibScalar
paVPSStatus = _PaVPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 30),
    _PaVPSStatus_Type()
)
paVPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paVPSStatus.setStatus("mandatory")
_PaThirdPartyCopyStatus_Type = Integer32
_PaThirdPartyCopyStatus_Object = MibScalar
paThirdPartyCopyStatus = _PaThirdPartyCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 31),
    _PaThirdPartyCopyStatus_Type()
)
paThirdPartyCopyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paThirdPartyCopyStatus.setStatus("mandatory")
_PaCommandControlLUN_Type = Integer32
_PaCommandControlLUN_Object = MibScalar
paCommandControlLUN = _PaCommandControlLUN_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 32),
    _PaCommandControlLUN_Type()
)
paCommandControlLUN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paCommandControlLUN.setStatus("mandatory")
_PaSanDirectorEnabled_Type = Boolean
_PaSanDirectorEnabled_Object = MibScalar
paSanDirectorEnabled = _PaSanDirectorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 33),
    _PaSanDirectorEnabled_Type()
)
paSanDirectorEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paSanDirectorEnabled.setStatus("mandatory")


class _PaNodeName_Type(OctetString):
    """Custom type paNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PaNodeName_Type.__name__ = "OctetString"
_PaNodeName_Object = MibScalar
paNodeName = _PaNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 34),
    _PaNodeName_Type()
)
paNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paNodeName.setStatus("mandatory")
_PaVPMStatus_Type = Integer32
_PaVPMStatus_Object = MibScalar
paVPMStatus = _PaVPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 35),
    _PaVPMStatus_Type()
)
paVPMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paVPMStatus.setStatus("mandatory")
_PaSRSStatus_Type = Integer32
_PaSRSStatus_Object = MibScalar
paSRSStatus = _PaSRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 36),
    _PaSRSStatus_Type()
)
paSRSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paSRSStatus.setStatus("mandatory")
_PaEthernetType_Type = DisplayString
_PaEthernetType_Object = MibScalar
paEthernetType = _PaEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 37),
    _PaEthernetType_Type()
)
paEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paEthernetType.setStatus("mandatory")
_PaTrapSequenceNumber_Type = Integer32
_PaTrapSequenceNumber_Object = MibScalar
paTrapSequenceNumber = _PaTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 38),
    _PaTrapSequenceNumber_Type()
)
paTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paTrapSequenceNumber.setStatus("mandatory")


class _PaSysNodeNameMode_Type(Integer32):
    """Custom type paSysNodeNameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("differentForEachPort", 1),
          ("sameForEachPort", 0))
    )


_PaSysNodeNameMode_Type.__name__ = "Integer32"
_PaSysNodeNameMode_Object = MibScalar
paSysNodeNameMode = _PaSysNodeNameMode_Object(
    (1, 3, 6, 1, 4, 1, 2935, 2, 39),
    _PaSysNodeNameMode_Type()
)
paSysNodeNameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paSysNodeNameMode.setStatus("mandatory")
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 3)
)
_PdDevices_Object = MibTable
pdDevices = _PdDevices_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1)
)
if mibBuilder.loadTexts:
    pdDevices.setStatus("mandatory")
_PdDevEntry_Object = MibTableRow
pdDevEntry = _PdDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1)
)
pdDevEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pdIndex"),
)
if mibBuilder.loadTexts:
    pdDevEntry.setStatus("mandatory")
_PdIndex_Type = Integer32
_PdIndex_Object = MibTableColumn
pdIndex = _PdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 1),
    _PdIndex_Type()
)
pdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdIndex.setStatus("mandatory")


class _PdUID_Type(DisplayString):
    """Custom type pdUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PdUID_Type.__name__ = "DisplayString"
_PdUID_Object = MibTableColumn
pdUID = _PdUID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 2),
    _PdUID_Type()
)
pdUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdUID.setStatus("mandatory")
_PdType_Type = DeviceType
_PdType_Object = MibTableColumn
pdType = _PdType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 3),
    _PdType_Type()
)
pdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdType.setStatus("mandatory")


class _PdVendor_Type(DisplayString):
    """Custom type pdVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PdVendor_Type.__name__ = "DisplayString"
_PdVendor_Object = MibTableColumn
pdVendor = _PdVendor_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 4),
    _PdVendor_Type()
)
pdVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdVendor.setStatus("mandatory")


class _PdProduct_Type(DisplayString):
    """Custom type pdProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PdProduct_Type.__name__ = "DisplayString"
_PdProduct_Object = MibTableColumn
pdProduct = _PdProduct_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 5),
    _PdProduct_Type()
)
pdProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdProduct.setStatus("mandatory")
_PdBlockSize_Type = Integer32
_PdBlockSize_Object = MibTableColumn
pdBlockSize = _PdBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 6),
    _PdBlockSize_Type()
)
pdBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdBlockSize.setStatus("mandatory")
_PdCapacity_Type = Gauge32
_PdCapacity_Object = MibTableColumn
pdCapacity = _PdCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 7),
    _PdCapacity_Type()
)
pdCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdCapacity.setStatus("mandatory")
_PdAccess_Type = Integer32
_PdAccess_Object = MibTableColumn
pdAccess = _PdAccess_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 8),
    _PdAccess_Type()
)
pdAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdAccess.setStatus("mandatory")
_PdRemovable_Type = Boolean
_PdRemovable_Object = MibTableColumn
pdRemovable = _PdRemovable_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 9),
    _PdRemovable_Type()
)
pdRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdRemovable.setStatus("mandatory")
_PdStatus_Type = PltStatus
_PdStatus_Object = MibTableColumn
pdStatus = _PdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 10),
    _PdStatus_Type()
)
pdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdStatus.setStatus("mandatory")
_PdSpeed_Type = Integer32
_PdSpeed_Object = MibTableColumn
pdSpeed = _PdSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 11),
    _PdSpeed_Type()
)
pdSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdSpeed.setStatus("mandatory")
_PdWidth_Type = Integer32
_PdWidth_Object = MibTableColumn
pdWidth = _PdWidth_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 12),
    _PdWidth_Type()
)
pdWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdWidth.setStatus("mandatory")


class _PdSerial_Type(DisplayString):
    """Custom type pdSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdSerial_Type.__name__ = "DisplayString"
_PdSerial_Object = MibTableColumn
pdSerial = _PdSerial_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 13),
    _PdSerial_Type()
)
pdSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdSerial.setStatus("mandatory")
_PdIdentify_Type = Integer32
_PdIdentify_Object = MibTableColumn
pdIdentify = _PdIdentify_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 14),
    _PdIdentify_Type()
)
pdIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdIdentify.setStatus("mandatory")
_PdInterfaceType_Type = Interface
_PdInterfaceType_Object = MibTableColumn
pdInterfaceType = _PdInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 15),
    _PdInterfaceType_Type()
)
pdInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdInterfaceType.setStatus("mandatory")
_PdBus_Type = Integer32
_PdBus_Object = MibTableColumn
pdBus = _PdBus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 16),
    _PdBus_Type()
)
pdBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdBus.setStatus("mandatory")
_PdId_Type = Integer32
_PdId_Object = MibTableColumn
pdId = _PdId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 17),
    _PdId_Type()
)
pdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdId.setStatus("mandatory")
_PdLun_Type = Integer32
_PdLun_Object = MibTableColumn
pdLun = _PdLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 18),
    _PdLun_Type()
)
pdLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdLun.setStatus("mandatory")
_PdCtlrIndex_Type = Integer32
_PdCtlrIndex_Object = MibTableColumn
pdCtlrIndex = _PdCtlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 19),
    _PdCtlrIndex_Type()
)
pdCtlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdCtlrIndex.setStatus("mandatory")


class _PdHWRev_Type(DisplayString):
    """Custom type pdHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdHWRev_Type.__name__ = "DisplayString"
_PdHWRev_Object = MibTableColumn
pdHWRev = _PdHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 20),
    _PdHWRev_Type()
)
pdHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdHWRev.setStatus("mandatory")


class _PdFWRev_Type(DisplayString):
    """Custom type pdFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdFWRev_Type.__name__ = "DisplayString"
_PdFWRev_Object = MibTableColumn
pdFWRev = _PdFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 21),
    _PdFWRev_Type()
)
pdFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdFWRev.setStatus("mandatory")
_PdReset_Type = Reset
_PdReset_Object = MibTableColumn
pdReset = _PdReset_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 22),
    _PdReset_Type()
)
pdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdReset.setStatus("mandatory")
_PdStatusBits_Type = Integer32
_PdStatusBits_Object = MibTableColumn
pdStatusBits = _PdStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 23),
    _PdStatusBits_Type()
)
pdStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdStatusBits.setStatus("mandatory")
_PdScsiAnsiLevel_Type = ScsiAnsiLevel
_PdScsiAnsiLevel_Object = MibTableColumn
pdScsiAnsiLevel = _PdScsiAnsiLevel_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 24),
    _PdScsiAnsiLevel_Type()
)
pdScsiAnsiLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdScsiAnsiLevel.setStatus("mandatory")
_PdTargetLun_Type = Integer32
_PdTargetLun_Object = MibTableColumn
pdTargetLun = _PdTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 25),
    _PdTargetLun_Type()
)
pdTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdTargetLun.setStatus("mandatory")
_PdIpAddress_Type = IpAddress
_PdIpAddress_Object = MibTableColumn
pdIpAddress = _PdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2935, 3, 1, 1, 26),
    _PdIpAddress_Type()
)
pdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdIpAddress.setStatus("mandatory")
_Controllers_ObjectIdentity = ObjectIdentity
controllers = _Controllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 4)
)
_PcControllers_Object = MibTable
pcControllers = _PcControllers_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1)
)
if mibBuilder.loadTexts:
    pcControllers.setStatus("mandatory")
_PcCtlrEntry_Object = MibTableRow
pcCtlrEntry = _PcCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1)
)
pcCtlrEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pcIndex"),
)
if mibBuilder.loadTexts:
    pcCtlrEntry.setStatus("mandatory")
_PcIndex_Type = Integer32
_PcIndex_Object = MibTableColumn
pcIndex = _PcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 1),
    _PcIndex_Type()
)
pcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcIndex.setStatus("mandatory")
_PcType_Type = Interface
_PcType_Object = MibTableColumn
pcType = _PcType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 2),
    _PcType_Type()
)
pcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcType.setStatus("mandatory")
_PcVendorId_Type = VendorIDInt
_PcVendorId_Object = MibTableColumn
pcVendorId = _PcVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 3),
    _PcVendorId_Type()
)
pcVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcVendorId.setStatus("mandatory")
_PcProductId_Type = Integer32
_PcProductId_Object = MibTableColumn
pcProductId = _PcProductId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 4),
    _PcProductId_Type()
)
pcProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcProductId.setStatus("mandatory")


class _PcRevision_Type(DisplayString):
    """Custom type pcRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcRevision_Type.__name__ = "DisplayString"
_PcRevision_Object = MibTableColumn
pcRevision = _PcRevision_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 5),
    _PcRevision_Type()
)
pcRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcRevision.setStatus("deprecated")
_PcSubVendor_Type = Integer32
_PcSubVendor_Object = MibTableColumn
pcSubVendor = _PcSubVendor_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 6),
    _PcSubVendor_Type()
)
pcSubVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSubVendor.setStatus("mandatory")
_PcSubProduct_Type = Integer32
_PcSubProduct_Object = MibTableColumn
pcSubProduct = _PcSubProduct_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 7),
    _PcSubProduct_Type()
)
pcSubProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSubProduct.setStatus("mandatory")
_PcMaxBurst_Type = Integer32
_PcMaxBurst_Object = MibTableColumn
pcMaxBurst = _PcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 8),
    _PcMaxBurst_Type()
)
pcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcMaxBurst.setStatus("mandatory")


class _PcLatency_Type(Integer32):
    """Custom type pcLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcLatency_Type.__name__ = "Integer32"
_PcLatency_Object = MibTableColumn
pcLatency = _PcLatency_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 9),
    _PcLatency_Type()
)
pcLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcLatency.setStatus("mandatory")
_PcIdentify_Type = Integer32
_PcIdentify_Object = MibTableColumn
pcIdentify = _PcIdentify_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 10),
    _PcIdentify_Type()
)
pcIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcIdentify.setStatus("mandatory")
_PcPCIBus_Type = Integer32
_PcPCIBus_Object = MibTableColumn
pcPCIBus = _PcPCIBus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 11),
    _PcPCIBus_Type()
)
pcPCIBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPCIBus.setStatus("mandatory")
_PcPCIDev_Type = Integer32
_PcPCIDev_Object = MibTableColumn
pcPCIDev = _PcPCIDev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 12),
    _PcPCIDev_Type()
)
pcPCIDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPCIDev.setStatus("mandatory")
_PcPCIFunc_Type = Integer32
_PcPCIFunc_Object = MibTableColumn
pcPCIFunc = _PcPCIFunc_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 13),
    _PcPCIFunc_Type()
)
pcPCIFunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPCIFunc.setStatus("mandatory")
_PcReset_Type = Reset
_PcReset_Object = MibTableColumn
pcReset = _PcReset_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 14),
    _PcReset_Type()
)
pcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcReset.setStatus("mandatory")
_PcRescan_Type = Boolean
_PcRescan_Object = MibTableColumn
pcRescan = _PcRescan_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 15),
    _PcRescan_Type()
)
pcRescan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcRescan.setStatus("mandatory")


class _PcLED_Type(OctetString):
    """Custom type pcLED based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PcLED_Type.__name__ = "OctetString"
_PcLED_Object = MibTableColumn
pcLED = _PcLED_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 16),
    _PcLED_Type()
)
pcLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLED.setStatus("mandatory")


class _PcHWRev_Type(DisplayString):
    """Custom type pcHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcHWRev_Type.__name__ = "DisplayString"
_PcHWRev_Object = MibTableColumn
pcHWRev = _PcHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 17),
    _PcHWRev_Type()
)
pcHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcHWRev.setStatus("mandatory")


class _PcFWRev_Type(DisplayString):
    """Custom type pcFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcFWRev_Type.__name__ = "DisplayString"
_PcFWRev_Object = MibTableColumn
pcFWRev = _PcFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 18),
    _PcFWRev_Type()
)
pcFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcFWRev.setStatus("mandatory")
_PcPCISlot_Type = Integer32
_PcPCISlot_Object = MibTableColumn
pcPCISlot = _PcPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 19),
    _PcPCISlot_Type()
)
pcPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPCISlot.setStatus("mandatory")
_PcPMCSlot_Type = Integer32
_PcPMCSlot_Object = MibTableColumn
pcPMCSlot = _PcPMCSlot_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 20),
    _PcPMCSlot_Type()
)
pcPMCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPMCSlot.setStatus("mandatory")


class _PcPCIClass_Type(OctetString):
    """Custom type pcPCIClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_PcPCIClass_Type.__name__ = "OctetString"
_PcPCIClass_Object = MibTableColumn
pcPCIClass = _PcPCIClass_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 21),
    _PcPCIClass_Type()
)
pcPCIClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcPCIClass.setStatus("mandatory")
_PcSplitMode_Type = Boolean
_PcSplitMode_Object = MibTableColumn
pcSplitMode = _PcSplitMode_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 22),
    _PcSplitMode_Type()
)
pcSplitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcSplitMode.setStatus("mandatory")
_PcChannelMask_Type = Gauge32
_PcChannelMask_Object = MibTableColumn
pcChannelMask = _PcChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 23),
    _PcChannelMask_Type()
)
pcChannelMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcChannelMask.setStatus("mandatory")


class _PcPortHostType_Type(DisplayString):
    """Custom type pcPortHostType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcPortHostType_Type.__name__ = "DisplayString"
_PcPortHostType_Object = MibTableColumn
pcPortHostType = _PcPortHostType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 1, 1, 24),
    _PcPortHostType_Type()
)
pcPortHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcPortHostType.setStatus("mandatory")
_PcFCCtlrs_Object = MibTable
pcFCCtlrs = _PcFCCtlrs_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2)
)
if mibBuilder.loadTexts:
    pcFCCtlrs.setStatus("mandatory")
_FcCtlrEntry_Object = MibTableRow
fcCtlrEntry = _FcCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1)
)
fcCtlrEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pcIndex"),
)
if mibBuilder.loadTexts:
    fcCtlrEntry.setStatus("mandatory")
_FcStatus_Type = FcStatus
_FcStatus_Object = MibTableColumn
fcStatus = _FcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 1),
    _FcStatus_Type()
)
fcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatus.setStatus("mandatory")
_FcMaxSpeed_Type = Gauge32
_FcMaxSpeed_Object = MibTableColumn
fcMaxSpeed = _FcMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 2),
    _FcMaxSpeed_Type()
)
fcMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcMaxSpeed.setStatus("mandatory")


class _FcWWID_Type(DisplayString):
    """Custom type fcWWID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_FcWWID_Type.__name__ = "DisplayString"
_FcWWID_Object = MibTableColumn
fcWWID = _FcWWID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 3),
    _FcWWID_Type()
)
fcWWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcWWID.setStatus("mandatory")


class _FcFWRev_Type(DisplayString):
    """Custom type fcFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcFWRev_Type.__name__ = "DisplayString"
_FcFWRev_Object = MibTableColumn
fcFWRev = _FcFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 4),
    _FcFWRev_Type()
)
fcFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFWRev.setStatus("mandatory")


class _FcHWRev_Type(DisplayString):
    """Custom type fcHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcHWRev_Type.__name__ = "DisplayString"
_FcHWRev_Object = MibTableColumn
fcHWRev = _FcHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 5),
    _FcHWRev_Type()
)
fcHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcHWRev.setStatus("mandatory")


class _FcLoopID_Type(Integer32):
    """Custom type fcLoopID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_FcLoopID_Type.__name__ = "Integer32"
_FcLoopID_Object = MibTableColumn
fcLoopID = _FcLoopID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 6),
    _FcLoopID_Type()
)
fcLoopID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcLoopID.setStatus("mandatory")
_FcFrameSize_Type = Integer32
_FcFrameSize_Object = MibTableColumn
fcFrameSize = _FcFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 7),
    _FcFrameSize_Type()
)
fcFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFrameSize.setStatus("mandatory")
_FcPortType_Type = FibrePort
_FcPortType_Object = MibTableColumn
fcPortType = _FcPortType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 8),
    _FcPortType_Type()
)
fcPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcPortType.setStatus("mandatory")
_FcMedia_Type = FibreMedia
_FcMedia_Object = MibTableColumn
fcMedia = _FcMedia_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 9),
    _FcMedia_Type()
)
fcMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcMedia.setStatus("mandatory")


class _FcSerialNumber_Type(DisplayString):
    """Custom type fcSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcSerialNumber_Type.__name__ = "DisplayString"
_FcSerialNumber_Object = MibTableColumn
fcSerialNumber = _FcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 10),
    _FcSerialNumber_Type()
)
fcSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSerialNumber.setStatus("mandatory")
_FcLoopIDMode_Type = FibreLoopIDMode
_FcLoopIDMode_Object = MibTableColumn
fcLoopIDMode = _FcLoopIDMode_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 11),
    _FcLoopIDMode_Type()
)
fcLoopIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLoopIDMode.setStatus("mandatory")
_FcALPhysicalAddress_Type = Integer32
_FcALPhysicalAddress_Object = MibTableColumn
fcALPhysicalAddress = _FcALPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 12),
    _FcALPhysicalAddress_Type()
)
fcALPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcALPhysicalAddress.setStatus("mandatory")
_FcPortMode_Type = FibrePortMode
_FcPortMode_Object = MibTableColumn
fcPortMode = _FcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 13),
    _FcPortMode_Type()
)
fcPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcPortMode.setStatus("mandatory")
_FcConnectionOptions_Type = FibreConnOptions
_FcConnectionOptions_Object = MibTableColumn
fcConnectionOptions = _FcConnectionOptions_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 14),
    _FcConnectionOptions_Type()
)
fcConnectionOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnectionOptions.setStatus("mandatory")
_FcCtlrChipType_Type = Integer32
_FcCtlrChipType_Object = MibTableColumn
fcCtlrChipType = _FcCtlrChipType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 15),
    _FcCtlrChipType_Type()
)
fcCtlrChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcCtlrChipType.setStatus("mandatory")
_FcTapeFeature_Type = Boolean
_FcTapeFeature_Object = MibTableColumn
fcTapeFeature = _FcTapeFeature_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 16),
    _FcTapeFeature_Type()
)
fcTapeFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTapeFeature.setStatus("mandatory")


class _FcHardID_Type(Integer32):
    """Custom type fcHardID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_FcHardID_Type.__name__ = "Integer32"
_FcHardID_Object = MibTableColumn
fcHardID = _FcHardID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 17),
    _FcHardID_Type()
)
fcHardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcHardID.setStatus("mandatory")
_FcCurrentSpeedSetting_Type = Integer32
_FcCurrentSpeedSetting_Object = MibTableColumn
fcCurrentSpeedSetting = _FcCurrentSpeedSetting_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 18),
    _FcCurrentSpeedSetting_Type()
)
fcCurrentSpeedSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcCurrentSpeedSetting.setStatus("mandatory")
_FcCurrentSpeed_Type = Integer32
_FcCurrentSpeed_Object = MibTableColumn
fcCurrentSpeed = _FcCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 19),
    _FcCurrentSpeed_Type()
)
fcCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcCurrentSpeed.setStatus("mandatory")
_FcFrameBufferSize_Type = Integer32
_FcFrameBufferSize_Object = MibTableColumn
fcFrameBufferSize = _FcFrameBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 20),
    _FcFrameBufferSize_Type()
)
fcFrameBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFrameBufferSize.setStatus("mandatory")
_FcLinkFailureCount_Type = Integer32
_FcLinkFailureCount_Object = MibTableColumn
fcLinkFailureCount = _FcLinkFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 21),
    _FcLinkFailureCount_Type()
)
fcLinkFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLinkFailureCount.setStatus("mandatory")
_FcLossSyncCount_Type = Integer32
_FcLossSyncCount_Object = MibTableColumn
fcLossSyncCount = _FcLossSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 22),
    _FcLossSyncCount_Type()
)
fcLossSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLossSyncCount.setStatus("mandatory")
_FcLossSignalCount_Type = Integer32
_FcLossSignalCount_Object = MibTableColumn
fcLossSignalCount = _FcLossSignalCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 23),
    _FcLossSignalCount_Type()
)
fcLossSignalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLossSignalCount.setStatus("mandatory")
_FcProtocolErrorCount_Type = Integer32
_FcProtocolErrorCount_Object = MibTableColumn
fcProtocolErrorCount = _FcProtocolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 24),
    _FcProtocolErrorCount_Type()
)
fcProtocolErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcProtocolErrorCount.setStatus("mandatory")
_FcInvalidTxWordCount_Type = Integer32
_FcInvalidTxWordCount_Object = MibTableColumn
fcInvalidTxWordCount = _FcInvalidTxWordCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 25),
    _FcInvalidTxWordCount_Type()
)
fcInvalidTxWordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInvalidTxWordCount.setStatus("mandatory")
_FcInvalidCRCCount_Type = Integer32
_FcInvalidCRCCount_Object = MibTableColumn
fcInvalidCRCCount = _FcInvalidCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 26),
    _FcInvalidCRCCount_Type()
)
fcInvalidCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInvalidCRCCount.setStatus("mandatory")


class _FcWWNodeName_Type(DisplayString):
    """Custom type fcWWNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_FcWWNodeName_Type.__name__ = "DisplayString"
_FcWWNodeName_Object = MibTableColumn
fcWWNodeName = _FcWWNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 2, 1, 27),
    _FcWWNodeName_Type()
)
fcWWNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcWWNodeName.setStatus("mandatory")
_PcSSACtlrs_Object = MibTable
pcSSACtlrs = _PcSSACtlrs_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3)
)
if mibBuilder.loadTexts:
    pcSSACtlrs.setStatus("mandatory")
_SsaCtlrEntry_Object = MibTableRow
ssaCtlrEntry = _SsaCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1)
)
ssaCtlrEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pcIndex"),
)
if mibBuilder.loadTexts:
    ssaCtlrEntry.setStatus("mandatory")
_SsaStatus1_Type = PltStatus
_SsaStatus1_Object = MibTableColumn
ssaStatus1 = _SsaStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 1),
    _SsaStatus1_Type()
)
ssaStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaStatus1.setStatus("mandatory")
_SsaStatus2_Type = PltStatus
_SsaStatus2_Object = MibTableColumn
ssaStatus2 = _SsaStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 2),
    _SsaStatus2_Type()
)
ssaStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaStatus2.setStatus("mandatory")
_SsaSpeed_Type = SsaSpeed
_SsaSpeed_Object = MibTableColumn
ssaSpeed = _SsaSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 3),
    _SsaSpeed_Type()
)
ssaSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssaSpeed.setStatus("mandatory")


class _SsaUID_Type(DisplayString):
    """Custom type ssaUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SsaUID_Type.__name__ = "DisplayString"
_SsaUID_Object = MibTableColumn
ssaUID = _SsaUID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 4),
    _SsaUID_Type()
)
ssaUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaUID.setStatus("mandatory")


class _SsaFWRev_Type(DisplayString):
    """Custom type ssaFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SsaFWRev_Type.__name__ = "DisplayString"
_SsaFWRev_Object = MibTableColumn
ssaFWRev = _SsaFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 5),
    _SsaFWRev_Type()
)
ssaFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaFWRev.setStatus("mandatory")
_SsaMaxTarg_Type = Gauge32
_SsaMaxTarg_Object = MibTableColumn
ssaMaxTarg = _SsaMaxTarg_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 6),
    _SsaMaxTarg_Type()
)
ssaMaxTarg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssaMaxTarg.setStatus("mandatory")
_SsaMaxInit_Type = Gauge32
_SsaMaxInit_Object = MibTableColumn
ssaMaxInit = _SsaMaxInit_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 7),
    _SsaMaxInit_Type()
)
ssaMaxInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssaMaxInit.setStatus("mandatory")
_SsaPathAlg_Type = PathingAlgorithm
_SsaPathAlg_Object = MibTableColumn
ssaPathAlg = _SsaPathAlg_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 8),
    _SsaPathAlg_Type()
)
ssaPathAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssaPathAlg.setStatus("mandatory")


class _SsaHWRev_Type(DisplayString):
    """Custom type ssaHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SsaHWRev_Type.__name__ = "DisplayString"
_SsaHWRev_Object = MibTableColumn
ssaHWRev = _SsaHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 9),
    _SsaHWRev_Type()
)
ssaHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaHWRev.setStatus("mandatory")


class _SsaMasterPriority_Type(Integer32):
    """Custom type ssaMasterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SsaMasterPriority_Type.__name__ = "Integer32"
_SsaMasterPriority_Object = MibTableColumn
ssaMasterPriority = _SsaMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 10),
    _SsaMasterPriority_Type()
)
ssaMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaMasterPriority.setStatus("mandatory")


class _SsaSATAQuota_Type(Integer32):
    """Custom type ssaSATAQuota based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SsaSATAQuota_Type.__name__ = "Integer32"
_SsaSATAQuota_Object = MibTableColumn
ssaSATAQuota = _SsaSATAQuota_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 11),
    _SsaSATAQuota_Type()
)
ssaSATAQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaSATAQuota.setStatus("mandatory")


class _SsaSATBQuota_Type(Integer32):
    """Custom type ssaSATBQuota based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SsaSATBQuota_Type.__name__ = "Integer32"
_SsaSATBQuota_Object = MibTableColumn
ssaSATBQuota = _SsaSATBQuota_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 12),
    _SsaSATBQuota_Type()
)
ssaSATBQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaSATBQuota.setStatus("mandatory")


class _SsaSATIQuota_Type(Integer32):
    """Custom type ssaSATIQuota based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SsaSATIQuota_Type.__name__ = "Integer32"
_SsaSATIQuota_Object = MibTableColumn
ssaSATIQuota = _SsaSATIQuota_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 3, 1, 13),
    _SsaSATIQuota_Type()
)
ssaSATIQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssaSATIQuota.setStatus("mandatory")
_PcSCSICtlrs_Object = MibTable
pcSCSICtlrs = _PcSCSICtlrs_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4)
)
if mibBuilder.loadTexts:
    pcSCSICtlrs.setStatus("mandatory")
_ScsiCtlrEntry_Object = MibTableRow
scsiCtlrEntry = _ScsiCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1)
)
scsiCtlrEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pcIndex"),
)
if mibBuilder.loadTexts:
    scsiCtlrEntry.setStatus("mandatory")
_ScsiStatus_Type = PltStatus
_ScsiStatus_Object = MibTableColumn
scsiStatus = _ScsiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 1),
    _ScsiStatus_Type()
)
scsiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiStatus.setStatus("mandatory")
_ScsiSpeed_Type = ScsiSpeed
_ScsiSpeed_Object = MibTableColumn
scsiSpeed = _ScsiSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 2),
    _ScsiSpeed_Type()
)
scsiSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiSpeed.setStatus("mandatory")
_ScsiRole_Type = ScsiRole
_ScsiRole_Object = MibTableColumn
scsiRole = _ScsiRole_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 3),
    _ScsiRole_Type()
)
scsiRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiRole.setStatus("mandatory")


class _ScsiHostId_Type(Integer32):
    """Custom type scsiHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ScsiHostId_Type.__name__ = "Integer32"
_ScsiHostId_Object = MibTableColumn
scsiHostId = _ScsiHostId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 4),
    _ScsiHostId_Type()
)
scsiHostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiHostId.setStatus("mandatory")
_ScsiMaxSpeed_Type = ScsiSpeed
_ScsiMaxSpeed_Object = MibTableColumn
scsiMaxSpeed = _ScsiMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 5),
    _ScsiMaxSpeed_Type()
)
scsiMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMaxSpeed.setStatus("mandatory")
_ScsiTerm_Type = ScsiTermination
_ScsiTerm_Object = MibTableColumn
scsiTerm = _ScsiTerm_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 6),
    _ScsiTerm_Type()
)
scsiTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiTerm.setStatus("mandatory")
_ScsiIoCard_Type = ScsiCardType
_ScsiIoCard_Object = MibTableColumn
scsiIoCard = _ScsiIoCard_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 7),
    _ScsiIoCard_Type()
)
scsiIoCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIoCard.setStatus("mandatory")
_ScsiMaxIds_Type = Integer32
_ScsiMaxIds_Object = MibTableColumn
scsiMaxIds = _ScsiMaxIds_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 8),
    _ScsiMaxIds_Type()
)
scsiMaxIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMaxIds.setStatus("mandatory")
_ScsiMaxLuns_Type = Integer32
_ScsiMaxLuns_Object = MibTableColumn
scsiMaxLuns = _ScsiMaxLuns_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 9),
    _ScsiMaxLuns_Type()
)
scsiMaxLuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMaxLuns.setStatus("mandatory")
_ScsiMaxWidth_Type = Integer32
_ScsiMaxWidth_Object = MibTableColumn
scsiMaxWidth = _ScsiMaxWidth_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 10),
    _ScsiMaxWidth_Type()
)
scsiMaxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiMaxWidth.setStatus("mandatory")


class _ScsiHWRev_Type(DisplayString):
    """Custom type scsiHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScsiHWRev_Type.__name__ = "DisplayString"
_ScsiHWRev_Object = MibTableColumn
scsiHWRev = _ScsiHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 11),
    _ScsiHWRev_Type()
)
scsiHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiHWRev.setStatus("mandatory")


class _ScsiFWRev_Type(DisplayString):
    """Custom type scsiFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScsiFWRev_Type.__name__ = "DisplayString"
_ScsiFWRev_Object = MibTableColumn
scsiFWRev = _ScsiFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 12),
    _ScsiFWRev_Type()
)
scsiFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiFWRev.setStatus("mandatory")
_ScsiResetOnPowerUp_Type = Boolean
_ScsiResetOnPowerUp_Object = MibTableColumn
scsiResetOnPowerUp = _ScsiResetOnPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 13),
    _ScsiResetOnPowerUp_Type()
)
scsiResetOnPowerUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiResetOnPowerUp.setStatus("mandatory")
_ScsiMultiInitEnabled_Type = Boolean
_ScsiMultiInitEnabled_Object = MibTableColumn
scsiMultiInitEnabled = _ScsiMultiInitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 14),
    _ScsiMultiInitEnabled_Type()
)
scsiMultiInitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMultiInitEnabled.setStatus("mandatory")


class _ScsiAlternateHostId_Type(Integer32):
    """Custom type scsiAlternateHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_ScsiAlternateHostId_Type.__name__ = "Integer32"
_ScsiAlternateHostId_Object = MibTableColumn
scsiAlternateHostId = _ScsiAlternateHostId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 4, 4, 1, 15),
    _ScsiAlternateHostId_Type()
)
scsiAlternateHostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiAlternateHostId.setStatus("mandatory")
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 5)
)
_PnTrapDest_Object = MibTable
pnTrapDest = _PnTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1)
)
if mibBuilder.loadTexts:
    pnTrapDest.setStatus("mandatory")
_PnTrapDestEntry_Object = MibTableRow
pnTrapDestEntry = _PnTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1, 1)
)
pnTrapDestEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "pnIPAddr"),
    (0, "SANMgrV1-MIB", "pnUdpPort"),
)
if mibBuilder.loadTexts:
    pnTrapDestEntry.setStatus("mandatory")
_PnIndex_Type = Integer32
_PnIndex_Object = MibTableColumn
pnIndex = _PnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1, 1, 1),
    _PnIndex_Type()
)
pnIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnIndex.setStatus("mandatory")
_PnIPAddr_Type = IpAddress
_PnIPAddr_Object = MibTableColumn
pnIPAddr = _PnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1, 1, 2),
    _PnIPAddr_Type()
)
pnIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnIPAddr.setStatus("mandatory")


class _PnUdpPort_Type(Integer32):
    """Custom type pnUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnUdpPort_Type.__name__ = "Integer32"
_PnUdpPort_Object = MibTableColumn
pnUdpPort = _PnUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1, 1, 3),
    _PnUdpPort_Type()
)
pnUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnUdpPort.setStatus("mandatory")


class _PnTrapStyle_Type(Integer32):
    """Custom type pnTrapStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("rfc1215", 2))
    )


_PnTrapStyle_Type.__name__ = "Integer32"
_PnTrapStyle_Object = MibTableColumn
pnTrapStyle = _PnTrapStyle_Object(
    (1, 3, 6, 1, 4, 1, 2935, 5, 1, 1, 4),
    _PnTrapStyle_Type()
)
pnTrapStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnTrapStyle.setStatus("mandatory")
_PanelLED_ObjectIdentity = ObjectIdentity
panelLED = _PanelLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 6)
)


class _LedReady_Type(OctetString):
    """Custom type ledReady based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedReady_Type.__name__ = "OctetString"
_LedReady_Object = MibScalar
ledReady = _LedReady_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 1),
    _LedReady_Type()
)
ledReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledReady.setStatus("mandatory")


class _LedAuxPower_Type(OctetString):
    """Custom type ledAuxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedAuxPower_Type.__name__ = "OctetString"
_LedAuxPower_Object = MibScalar
ledAuxPower = _LedAuxPower_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 2),
    _LedAuxPower_Type()
)
ledAuxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledAuxPower.setStatus("mandatory")


class _LedMainPower_Type(OctetString):
    """Custom type ledMainPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedMainPower_Type.__name__ = "OctetString"
_LedMainPower_Object = MibScalar
ledMainPower = _LedMainPower_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 3),
    _LedMainPower_Type()
)
ledMainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledMainPower.setStatus("mandatory")


class _LedTempAlarm_Type(OctetString):
    """Custom type ledTempAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedTempAlarm_Type.__name__ = "OctetString"
_LedTempAlarm_Object = MibScalar
ledTempAlarm = _LedTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 4),
    _LedTempAlarm_Type()
)
ledTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledTempAlarm.setStatus("mandatory")


class _LedTempWarn_Type(OctetString):
    """Custom type ledTempWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedTempWarn_Type.__name__ = "OctetString"
_LedTempWarn_Object = MibScalar
ledTempWarn = _LedTempWarn_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 5),
    _LedTempWarn_Type()
)
ledTempWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledTempWarn.setStatus("mandatory")


class _LedEtherCollision_Type(OctetString):
    """Custom type ledEtherCollision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedEtherCollision_Type.__name__ = "OctetString"
_LedEtherCollision_Object = MibScalar
ledEtherCollision = _LedEtherCollision_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 6),
    _LedEtherCollision_Type()
)
ledEtherCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEtherCollision.setStatus("mandatory")


class _LedEtherTransmit_Type(OctetString):
    """Custom type ledEtherTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedEtherTransmit_Type.__name__ = "OctetString"
_LedEtherTransmit_Object = MibScalar
ledEtherTransmit = _LedEtherTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 7),
    _LedEtherTransmit_Type()
)
ledEtherTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEtherTransmit.setStatus("mandatory")


class _LedEtherLink_Type(OctetString):
    """Custom type ledEtherLink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedEtherLink_Type.__name__ = "OctetString"
_LedEtherLink_Object = MibScalar
ledEtherLink = _LedEtherLink_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 8),
    _LedEtherLink_Type()
)
ledEtherLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEtherLink.setStatus("mandatory")


class _LedScsi1_Type(OctetString):
    """Custom type ledScsi1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedScsi1_Type.__name__ = "OctetString"
_LedScsi1_Object = MibScalar
ledScsi1 = _LedScsi1_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 9),
    _LedScsi1_Type()
)
ledScsi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledScsi1.setStatus("mandatory")


class _LedScsi2_Type(OctetString):
    """Custom type ledScsi2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedScsi2_Type.__name__ = "OctetString"
_LedScsi2_Object = MibScalar
ledScsi2 = _LedScsi2_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 10),
    _LedScsi2_Type()
)
ledScsi2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledScsi2.setStatus("mandatory")


class _LedScsi3_Type(OctetString):
    """Custom type ledScsi3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedScsi3_Type.__name__ = "OctetString"
_LedScsi3_Object = MibScalar
ledScsi3 = _LedScsi3_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 11),
    _LedScsi3_Type()
)
ledScsi3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledScsi3.setStatus("mandatory")


class _LedScsi4_Type(OctetString):
    """Custom type ledScsi4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedScsi4_Type.__name__ = "OctetString"
_LedScsi4_Object = MibScalar
ledScsi4 = _LedScsi4_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 12),
    _LedScsi4_Type()
)
ledScsi4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledScsi4.setStatus("mandatory")


class _LedActivity1_Type(OctetString):
    """Custom type ledActivity1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedActivity1_Type.__name__ = "OctetString"
_LedActivity1_Object = MibScalar
ledActivity1 = _LedActivity1_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 13),
    _LedActivity1_Type()
)
ledActivity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledActivity1.setStatus("mandatory")


class _LedActivity2_Type(OctetString):
    """Custom type ledActivity2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedActivity2_Type.__name__ = "OctetString"
_LedActivity2_Object = MibScalar
ledActivity2 = _LedActivity2_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 14),
    _LedActivity2_Type()
)
ledActivity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledActivity2.setStatus("mandatory")


class _LedActivity3_Type(OctetString):
    """Custom type ledActivity3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedActivity3_Type.__name__ = "OctetString"
_LedActivity3_Object = MibScalar
ledActivity3 = _LedActivity3_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 15),
    _LedActivity3_Type()
)
ledActivity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledActivity3.setStatus("mandatory")


class _LedStatus1_Type(OctetString):
    """Custom type ledStatus1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedStatus1_Type.__name__ = "OctetString"
_LedStatus1_Object = MibScalar
ledStatus1 = _LedStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 16),
    _LedStatus1_Type()
)
ledStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus1.setStatus("mandatory")


class _LedStatus2_Type(OctetString):
    """Custom type ledStatus2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedStatus2_Type.__name__ = "OctetString"
_LedStatus2_Object = MibScalar
ledStatus2 = _LedStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 17),
    _LedStatus2_Type()
)
ledStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus2.setStatus("mandatory")


class _LedStatus3_Type(OctetString):
    """Custom type ledStatus3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedStatus3_Type.__name__ = "OctetString"
_LedStatus3_Object = MibScalar
ledStatus3 = _LedStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 18),
    _LedStatus3_Type()
)
ledStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus3.setStatus("mandatory")
_LedAll_Type = Integer32
_LedAll_Object = MibScalar
ledAll = _LedAll_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 19),
    _LedAll_Type()
)
ledAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledAll.setStatus("mandatory")


class _LedError_Type(OctetString):
    """Custom type ledError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedError_Type.__name__ = "OctetString"
_LedError_Object = MibScalar
ledError = _LedError_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 20),
    _LedError_Type()
)
ledError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledError.setStatus("mandatory")


class _LedEthernetSpeed_Type(OctetString):
    """Custom type ledEthernetSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LedEthernetSpeed_Type.__name__ = "OctetString"
_LedEthernetSpeed_Object = MibScalar
ledEthernetSpeed = _LedEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2935, 6, 21),
    _LedEthernetSpeed_Type()
)
ledEthernetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEthernetSpeed.setStatus("mandatory")
_PaHost_ObjectIdentity = ObjectIdentity
paHost = _PaHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 7)
)
_HostCommand_Type = Integer32
_HostCommand_Object = MibScalar
hostCommand = _HostCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 1),
    _HostCommand_Type()
)
hostCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostCommand.setStatus("mandatory")
_HostInitiator_Object = MibTable
hostInitiator = _HostInitiator_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2)
)
if mibBuilder.loadTexts:
    hostInitiator.setStatus("mandatory")
_HostInitiatorEntry_Object = MibTableRow
hostInitiatorEntry = _HostInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1)
)
hostInitiatorEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostInitiatorEntry.setStatus("mandatory")
_HostIndex_Type = Integer32
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIndex.setStatus("mandatory")
_HostRowStatus_Type = Integer32
_HostRowStatus_Object = MibTableColumn
hostRowStatus = _HostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 2),
    _HostRowStatus_Type()
)
hostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostRowStatus.setStatus("mandatory")


class _HostWWName_Type(DisplayString):
    """Custom type hostWWName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostWWName_Type.__name__ = "DisplayString"
_HostWWName_Object = MibTableColumn
hostWWName = _HostWWName_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 3),
    _HostWWName_Type()
)
hostWWName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostWWName.setStatus("mandatory")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 4),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")


class _HostType_Type(DisplayString):
    """Custom type hostType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostType_Type.__name__ = "DisplayString"
_HostType_Object = MibTableColumn
hostType = _HostType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 5),
    _HostType_Type()
)
hostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostType.setStatus("mandatory")


class _HostPortID_Type(DisplayString):
    """Custom type hostPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostPortID_Type.__name__ = "DisplayString"
_HostPortID_Object = MibTableColumn
hostPortID = _HostPortID_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 6),
    _HostPortID_Type()
)
hostPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostPortID.setStatus("mandatory")
_HostSANConnection_Type = Integer32
_HostSANConnection_Object = MibTableColumn
hostSANConnection = _HostSANConnection_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 7),
    _HostSANConnection_Type()
)
hostSANConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSANConnection.setStatus("mandatory")
_HostConnectionType_Type = Integer32
_HostConnectionType_Object = MibTableColumn
hostConnectionType = _HostConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 8),
    _HostConnectionType_Type()
)
hostConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConnectionType.setStatus("mandatory")


class _HostITLData_Type(OctetString):
    """Custom type hostITLData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HostITLData_Type.__name__ = "OctetString"
_HostITLData_Object = MibTableColumn
hostITLData = _HostITLData_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 9),
    _HostITLData_Type()
)
hostITLData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostITLData.setStatus("mandatory")
_HostIPAddr_Type = IpAddress
_HostIPAddr_Object = MibTableColumn
hostIPAddr = _HostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2935, 7, 2, 1, 10),
    _HostIPAddr_Type()
)
hostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPAddr.setStatus("mandatory")
_ScsiMap_ObjectIdentity = ObjectIdentity
scsiMap = _ScsiMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 8)
)
_ScsiMapCommand_Type = Integer32
_ScsiMapCommand_Object = MibScalar
scsiMapCommand = _ScsiMapCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 1),
    _ScsiMapCommand_Type()
)
scsiMapCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMapCommand.setStatus("mandatory")
_ScsiChannelMap_Object = MibTable
scsiChannelMap = _ScsiChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2)
)
if mibBuilder.loadTexts:
    scsiChannelMap.setStatus("mandatory")
_ScsiMapEntry_Object = MibTableRow
scsiMapEntry = _ScsiMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1)
)
scsiMapEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "scsiMapPort"),
    (0, "SANMgrV1-MIB", "scsiMapTid"),
    (0, "SANMgrV1-MIB", "scsiMapLun"),
)
if mibBuilder.loadTexts:
    scsiMapEntry.setStatus("mandatory")
_ScsiMapRowStatus_Type = RowStatus
_ScsiMapRowStatus_Object = MibTableColumn
scsiMapRowStatus = _ScsiMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 1),
    _ScsiMapRowStatus_Type()
)
scsiMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMapRowStatus.setStatus("mandatory")
_ScsiMapPort_Type = Integer32
_ScsiMapPort_Object = MibTableColumn
scsiMapPort = _ScsiMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 2),
    _ScsiMapPort_Type()
)
scsiMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiMapPort.setStatus("mandatory")
_ScsiMapTid_Type = Integer32
_ScsiMapTid_Object = MibTableColumn
scsiMapTid = _ScsiMapTid_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 3),
    _ScsiMapTid_Type()
)
scsiMapTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiMapTid.setStatus("mandatory")
_ScsiMapLun_Type = Integer32
_ScsiMapLun_Object = MibTableColumn
scsiMapLun = _ScsiMapLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 4),
    _ScsiMapLun_Type()
)
scsiMapLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiMapLun.setStatus("mandatory")
_ScsiMapAssignedLun_Type = Integer32
_ScsiMapAssignedLun_Object = MibTableColumn
scsiMapAssignedLun = _ScsiMapAssignedLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 5),
    _ScsiMapAssignedLun_Type()
)
scsiMapAssignedLun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMapAssignedLun.setStatus("mandatory")


class _ScsiMapComments_Type(DisplayString):
    """Custom type scsiMapComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScsiMapComments_Type.__name__ = "DisplayString"
_ScsiMapComments_Object = MibTableColumn
scsiMapComments = _ScsiMapComments_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 6),
    _ScsiMapComments_Type()
)
scsiMapComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiMapComments.setStatus("mandatory")
_ScsiMapPdIndex_Type = Integer32
_ScsiMapPdIndex_Object = MibTableColumn
scsiMapPdIndex = _ScsiMapPdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2935, 8, 2, 1, 7),
    _ScsiMapPdIndex_Type()
)
scsiMapPdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiMapPdIndex.setStatus("mandatory")
_DeviceMap_ObjectIdentity = ObjectIdentity
deviceMap = _DeviceMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 9)
)


class _DeviceMapCommand_Type(Integer32):
    """Custom type deviceMapCommand based on Integer32"""
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
        *(("clearCopy", 1),
          ("commit", 2),
          ("mapClearDatabase", 4),
          ("winnow", 3))
    )


_DeviceMapCommand_Type.__name__ = "Integer32"
_DeviceMapCommand_Object = MibScalar
deviceMapCommand = _DeviceMapCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 1),
    _DeviceMapCommand_Type()
)
deviceMapCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMapCommand.setStatus("mandatory")
_DmDeviceMap_Object = MibTable
dmDeviceMap = _DmDeviceMap_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2)
)
if mibBuilder.loadTexts:
    dmDeviceMap.setStatus("mandatory")
_DmDevMapEntry_Object = MibTableRow
dmDevMapEntry = _DmDevMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1)
)
dmDevMapEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "dmAssignedLun"),
)
if mibBuilder.loadTexts:
    dmDevMapEntry.setStatus("mandatory")
_DmRowStatus_Type = RowStatus
_DmRowStatus_Object = MibTableColumn
dmRowStatus = _DmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 1),
    _DmRowStatus_Type()
)
dmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmRowStatus.setStatus("mandatory")
_DmAssignedLun_Type = Integer32
_DmAssignedLun_Object = MibTableColumn
dmAssignedLun = _DmAssignedLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 2),
    _DmAssignedLun_Type()
)
dmAssignedLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmAssignedLun.setStatus("mandatory")
_DmType_Type = Interface
_DmType_Object = MibTableColumn
dmType = _DmType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 3),
    _DmType_Type()
)
dmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmType.setStatus("mandatory")
_DmPort_Type = Integer32
_DmPort_Object = MibTableColumn
dmPort = _DmPort_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 4),
    _DmPort_Type()
)
dmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmPort.setStatus("mandatory")
_DmTargetId_Type = Integer32
_DmTargetId_Object = MibTableColumn
dmTargetId = _DmTargetId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 5),
    _DmTargetId_Type()
)
dmTargetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmTargetId.setStatus("mandatory")
_DmTargetLun_Type = Integer32
_DmTargetLun_Object = MibTableColumn
dmTargetLun = _DmTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 6),
    _DmTargetLun_Type()
)
dmTargetLun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmTargetLun.setStatus("mandatory")


class _DmUid_Type(OctetString):
    """Custom type dmUid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DmUid_Type.__name__ = "OctetString"
_DmUid_Object = MibTableColumn
dmUid = _DmUid_Object(
    (1, 3, 6, 1, 4, 1, 2935, 9, 2, 1, 7),
    _DmUid_Type()
)
dmUid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmUid.setStatus("mandatory")
_Replication_ObjectIdentity = ObjectIdentity
replication = _Replication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 10)
)
_SrsDevTable_Object = MibTable
srsDevTable = _SrsDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1)
)
if mibBuilder.loadTexts:
    srsDevTable.setStatus("mandatory")
_SrsDevEntry_Object = MibTableRow
srsDevEntry = _SrsDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1)
)
srsDevEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "srsDevId"),
)
if mibBuilder.loadTexts:
    srsDevEntry.setStatus("mandatory")
_SrsDevId_Type = Integer32
_SrsDevId_Object = MibTableColumn
srsDevId = _SrsDevId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 1),
    _SrsDevId_Type()
)
srsDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsDevId.setStatus("mandatory")


class _SrsDevState_Type(Integer32):
    """Custom type srsDevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 4),
          ("error", 3),
          ("initialized", 1),
          ("online", 2),
          ("unknown", 0))
    )


_SrsDevState_Type.__name__ = "Integer32"
_SrsDevState_Object = MibTableColumn
srsDevState = _SrsDevState_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 2),
    _SrsDevState_Type()
)
srsDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsDevState.setStatus("mandatory")


class _SrsDevCommand_Type(Integer32):
    """Custom type srsDevCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("remove", 2))
    )


_SrsDevCommand_Type.__name__ = "Integer32"
_SrsDevCommand_Object = MibTableColumn
srsDevCommand = _SrsDevCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 3),
    _SrsDevCommand_Type()
)
srsDevCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevCommand.setStatus("mandatory")
_SrsDevAssignedLun_Type = Integer32
_SrsDevAssignedLun_Object = MibTableColumn
srsDevAssignedLun = _SrsDevAssignedLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 4),
    _SrsDevAssignedLun_Type()
)
srsDevAssignedLun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevAssignedLun.setStatus("mandatory")
_SrsDevMemberCount_Type = Integer32
_SrsDevMemberCount_Object = MibTableColumn
srsDevMemberCount = _SrsDevMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 5),
    _SrsDevMemberCount_Type()
)
srsDevMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsDevMemberCount.setStatus("mandatory")
_SrsDevMembersOnline_Type = Integer32
_SrsDevMembersOnline_Object = MibTableColumn
srsDevMembersOnline = _SrsDevMembersOnline_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 6),
    _SrsDevMembersOnline_Type()
)
srsDevMembersOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsDevMembersOnline.setStatus("mandatory")
_SrsDevFlags_Type = Integer32
_SrsDevFlags_Object = MibTableColumn
srsDevFlags = _SrsDevFlags_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 7),
    _SrsDevFlags_Type()
)
srsDevFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevFlags.setStatus("mandatory")
_SrsDevSizeInBlocks_Type = Gauge32
_SrsDevSizeInBlocks_Object = MibTableColumn
srsDevSizeInBlocks = _SrsDevSizeInBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 8),
    _SrsDevSizeInBlocks_Type()
)
srsDevSizeInBlocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevSizeInBlocks.setStatus("mandatory")
_SrsDevBlockSize_Type = Integer32
_SrsDevBlockSize_Object = MibTableColumn
srsDevBlockSize = _SrsDevBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 9),
    _SrsDevBlockSize_Type()
)
srsDevBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevBlockSize.setStatus("mandatory")
_SrsDevPrimary_Type = Integer32
_SrsDevPrimary_Object = MibTableColumn
srsDevPrimary = _SrsDevPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 1, 1, 10),
    _SrsDevPrimary_Type()
)
srsDevPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsDevPrimary.setStatus("mandatory")
_SrsMemTable_Object = MibTable
srsMemTable = _SrsMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2)
)
if mibBuilder.loadTexts:
    srsMemTable.setStatus("mandatory")
_SrsMemEntry_Object = MibTableRow
srsMemEntry = _SrsMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1)
)
srsMemEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "srsMemDeviceId"),
    (0, "SANMgrV1-MIB", "srsMemId"),
)
if mibBuilder.loadTexts:
    srsMemEntry.setStatus("mandatory")
_SrsMemDeviceId_Type = Integer32
_SrsMemDeviceId_Object = MibTableColumn
srsMemDeviceId = _SrsMemDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 1),
    _SrsMemDeviceId_Type()
)
srsMemDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsMemDeviceId.setStatus("mandatory")
_SrsMemId_Type = Integer32
_SrsMemId_Object = MibTableColumn
srsMemId = _SrsMemId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 2),
    _SrsMemId_Type()
)
srsMemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsMemId.setStatus("mandatory")


class _SrsMemState_Type(Integer32):
    """Custom type srsMemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("offline", 7),
          ("online", 1),
          ("readError", 5),
          ("suspended", 4),
          ("synchronized", 2),
          ("synchronizing", 3),
          ("unknown", 0),
          ("writeError", 6))
    )


_SrsMemState_Type.__name__ = "Integer32"
_SrsMemState_Object = MibTableColumn
srsMemState = _SrsMemState_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 3),
    _SrsMemState_Type()
)
srsMemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsMemState.setStatus("mandatory")


class _SrsMemCommand_Type(Integer32):
    """Custom type srsMemCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fullSynchronize", 6),
          ("memberAdd", 1),
          ("memberChange", 8),
          ("primarySet", 5),
          ("quickSynchronize", 7),
          ("remove", 4),
          ("resume", 3),
          ("suspend", 2))
    )


_SrsMemCommand_Type.__name__ = "Integer32"
_SrsMemCommand_Object = MibTableColumn
srsMemCommand = _SrsMemCommand_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 4),
    _SrsMemCommand_Type()
)
srsMemCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsMemCommand.setStatus("mandatory")


class _SrsMemType_Type(Integer32):
    """Custom type srsMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SrsMemType_Type.__name__ = "Integer32"
_SrsMemType_Object = MibTableColumn
srsMemType = _SrsMemType_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 5),
    _SrsMemType_Type()
)
srsMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsMemType.setStatus("mandatory")
_SrsMemSyncPoint_Type = Integer32
_SrsMemSyncPoint_Object = MibTableColumn
srsMemSyncPoint = _SrsMemSyncPoint_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 6),
    _SrsMemSyncPoint_Type()
)
srsMemSyncPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsMemSyncPoint.setStatus("mandatory")
_SrsMemAssignedLun_Type = Integer32
_SrsMemAssignedLun_Object = MibTableColumn
srsMemAssignedLun = _SrsMemAssignedLun_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 7),
    _SrsMemAssignedLun_Type()
)
srsMemAssignedLun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsMemAssignedLun.setStatus("mandatory")


class _SrsMemReadOptions_Type(Integer32):
    """Custom type srsMemReadOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SrsMemReadOptions_Type.__name__ = "Integer32"
_SrsMemReadOptions_Object = MibTableColumn
srsMemReadOptions = _SrsMemReadOptions_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 8),
    _SrsMemReadOptions_Type()
)
srsMemReadOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsMemReadOptions.setStatus("mandatory")


class _SrsMemWriteOptions_Type(Integer32):
    """Custom type srsMemWriteOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous", 0))
    )


_SrsMemWriteOptions_Type.__name__ = "Integer32"
_SrsMemWriteOptions_Object = MibTableColumn
srsMemWriteOptions = _SrsMemWriteOptions_Object(
    (1, 3, 6, 1, 4, 1, 2935, 10, 2, 1, 9),
    _SrsMemWriteOptions_Type()
)
srsMemWriteOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srsMemWriteOptions.setStatus("mandatory")
_EnvData_ObjectIdentity = ObjectIdentity
envData = _EnvData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 11)
)
_EnvDataTable_Object = MibTable
envDataTable = _EnvDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1)
)
if mibBuilder.loadTexts:
    envDataTable.setStatus("mandatory")
_EnvDataEntry_Object = MibTableRow
envDataEntry = _EnvDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1)
)
envDataEntry.setIndexNames(
    (0, "SANMgrV1-MIB", "envDataId"),
)
if mibBuilder.loadTexts:
    envDataEntry.setStatus("mandatory")
_EnvDataId_Type = Integer32
_EnvDataId_Object = MibTableColumn
envDataId = _EnvDataId_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 1),
    _EnvDataId_Type()
)
envDataId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDataId.setStatus("mandatory")


class _EnvDataName_Type(DisplayString):
    """Custom type envDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EnvDataName_Type.__name__ = "DisplayString"
_EnvDataName_Object = MibTableColumn
envDataName = _EnvDataName_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 2),
    _EnvDataName_Type()
)
envDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDataName.setStatus("mandatory")


class _EnvNominalLo_Type(DisplayString):
    """Custom type envNominalLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvNominalLo_Type.__name__ = "DisplayString"
_EnvNominalLo_Object = MibTableColumn
envNominalLo = _EnvNominalLo_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 3),
    _EnvNominalLo_Type()
)
envNominalLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNominalLo.setStatus("mandatory")


class _EnvNominalHi_Type(DisplayString):
    """Custom type envNominalHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvNominalHi_Type.__name__ = "DisplayString"
_EnvNominalHi_Object = MibTableColumn
envNominalHi = _EnvNominalHi_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 4),
    _EnvNominalHi_Type()
)
envNominalHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNominalHi.setStatus("mandatory")


class _EnvWarningLo_Type(DisplayString):
    """Custom type envWarningLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvWarningLo_Type.__name__ = "DisplayString"
_EnvWarningLo_Object = MibTableColumn
envWarningLo = _EnvWarningLo_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 5),
    _EnvWarningLo_Type()
)
envWarningLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envWarningLo.setStatus("mandatory")


class _EnvWarningHi_Type(DisplayString):
    """Custom type envWarningHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvWarningHi_Type.__name__ = "DisplayString"
_EnvWarningHi_Object = MibTableColumn
envWarningHi = _EnvWarningHi_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 6),
    _EnvWarningHi_Type()
)
envWarningHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envWarningHi.setStatus("mandatory")


class _EnvCurValue_Type(DisplayString):
    """Custom type envCurValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvCurValue_Type.__name__ = "DisplayString"
_EnvCurValue_Object = MibTableColumn
envCurValue = _EnvCurValue_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 7),
    _EnvCurValue_Type()
)
envCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCurValue.setStatus("mandatory")


class _EnvCurStatus_Type(DisplayString):
    """Custom type envCurStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvCurStatus_Type.__name__ = "DisplayString"
_EnvCurStatus_Object = MibTableColumn
envCurStatus = _EnvCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 8),
    _EnvCurStatus_Type()
)
envCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCurStatus.setStatus("mandatory")


class _EnvUnit_Type(DisplayString):
    """Custom type envUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvUnit_Type.__name__ = "DisplayString"
_EnvUnit_Object = MibTableColumn
envUnit = _EnvUnit_Object(
    (1, 3, 6, 1, 4, 1, 2935, 11, 1, 1, 9),
    _EnvUnit_Type()
)
envUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envUnit.setStatus("mandatory")
_TrapDefinition_ObjectIdentity = ObjectIdentity
trapDefinition = _TrapDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2935, 1000)
)

# Managed Objects groups


# Notification objects

ssaPortUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 1)
)
ssaPortUpEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaPortUpEvent.setStatus(
        ""
    )

ssaPortDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 2)
)
ssaPortDownEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaPortDownEvent.setStatus(
        ""
    )

ssaUidAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 3)
)
ssaUidAddedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaUidAddedEvent.setStatus(
        ""
    )

ssaUidRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 4)
)
ssaUidRemovedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaUidRemovedEvent.setStatus(
        ""
    )

ssaWebReconfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 5)
)
ssaWebReconfiguredEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaWebReconfiguredEvent.setStatus(
        ""
    )

ssaAsyncErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 6)
)
ssaAsyncErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaAsyncErrorEvent.setStatus(
        ""
    )

ssaAdapterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 7)
)
ssaAdapterEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaAdapterEvent.setStatus(
        ""
    )

senseDataEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 8)
)
senseDataEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    senseDataEvent.setStatus(
        ""
    )

unitAttentionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 9)
)
unitAttentionEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    unitAttentionEvent.setStatus(
        ""
    )

ibfEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 10)
)
ibfEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ibfEvent.setStatus(
        ""
    )

temperatureChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 11)
)
temperatureChangeEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    temperatureChangeEvent.setStatus(
        ""
    )

timeReferenceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 12)
)
timeReferenceEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    timeReferenceEvent.setStatus(
        ""
    )

shutdownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 13)
)
shutdownEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    shutdownEvent.setStatus(
        ""
    )

diagnosticEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 14)
)
diagnosticEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    diagnosticEvent.setStatus(
        ""
    )

configurationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 15)
)
configurationEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    configurationEvent.setStatus(
        ""
    )

unexpectedScsiInterruptEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 16)
)
unexpectedScsiInterruptEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    unexpectedScsiInterruptEvent.setStatus(
        ""
    )

lipResetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 17)
)
lipResetEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    lipResetEvent.setStatus(
        ""
    )

fcSystemErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 18)
)
fcSystemErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcSystemErrorEvent.setStatus(
        ""
    )

fcRequestTransferErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 19)
)
fcRequestTransferErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcRequestTransferErrorEvent.setStatus(
        ""
    )

fcResponseTransferErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 20)
)
fcResponseTransferErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcResponseTransferErrorEvent.setStatus(
        ""
    )

memoryFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 21)
)
memoryFaultEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    memoryFaultEvent.setStatus(
        ""
    )

fcLipEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 22)
)
fcLipEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcLipEvent.setStatus(
        ""
    )

fcLoopUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 23)
)
fcLoopUpEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcLoopUpEvent.setStatus(
        ""
    )

fcLoopDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 24)
)
fcLoopDownEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcLoopDownEvent.setStatus(
        ""
    )

pciBusParityErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 25)
)
pciBusParityErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    pciBusParityErrorEvent.setStatus(
        ""
    )

pciInterfaceErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 26)
)
pciInterfaceErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    pciInterfaceErrorEvent.setStatus(
        ""
    )

scsiDeviceAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 27)
)
scsiDeviceAddedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    scsiDeviceAddedEvent.setStatus(
        ""
    )

scsiBusResetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 28)
)
scsiBusResetEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    scsiBusResetEvent.setStatus(
        ""
    )

deviceAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 29)
)
deviceAddedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    deviceAddedEvent.setStatus(
        ""
    )

deviceRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 30)
)
deviceRemovedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    deviceRemovedEvent.setStatus(
        ""
    )

loggingStartedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 31)
)
loggingStartedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    loggingStartedEvent.setStatus(
        ""
    )

loggingStoppedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 32)
)
loggingStoppedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    loggingStoppedEvent.setStatus(
        ""
    )

interfaceBusFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 33)
)
interfaceBusFaultEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    interfaceBusFaultEvent.setStatus(
        ""
    )

interfaceDeviceFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 34)
)
interfaceDeviceFaultEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    interfaceDeviceFaultEvent.setStatus(
        ""
    )

scsiUnexpectedDisconnectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 35)
)
scsiUnexpectedDisconnectEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    scsiUnexpectedDisconnectEvent.setStatus(
        ""
    )

scsiParityErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 36)
)
scsiParityErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    scsiParityErrorEvent.setStatus(
        ""
    )

fcPortDatabaseChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 37)
)
fcPortDatabaseChangeEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcPortDatabaseChangeEvent.setStatus(
        ""
    )

ddfMemoryErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 38)
)
ddfMemoryErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ddfMemoryErrorEvent.setStatus(
        ""
    )

fcDirectoryServerChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 39)
)
fcDirectoryServerChangeEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcDirectoryServerChangeEvent.setStatus(
        ""
    )

lunLimitExcededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 40)
)
lunLimitExcededEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    lunLimitExcededEvent.setStatus(
        ""
    )

fcTransferFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 41)
)
fcTransferFailureEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcTransferFailureEvent.setStatus(
        ""
    )

deviceLimitExcededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 42)
)
deviceLimitExcededEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    deviceLimitExcededEvent.setStatus(
        ""
    )

fcDebugDumpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 43)
)
fcDebugDumpEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcDebugDumpEvent.setStatus(
        ""
    )

excessiveScsiBusErrorsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 44)
)
excessiveScsiBusErrorsEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    excessiveScsiBusErrorsEvent.setStatus(
        ""
    )

memoryScrubberErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 45)
)
memoryScrubberErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    memoryScrubberErrorEvent.setStatus(
        ""
    )

srsDeviceCreatedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 46)
)
srsDeviceCreatedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsDeviceCreatedEvent.setStatus(
        ""
    )

srsDeviceOnlineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 47)
)
srsDeviceOnlineEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsDeviceOnlineEvent.setStatus(
        ""
    )

srsDeviceRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 48)
)
srsDeviceRemovedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsDeviceRemovedEvent.setStatus(
        ""
    )

srsDeviceFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 49)
)
srsDeviceFailedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsDeviceFailedEvent.setStatus(
        ""
    )

srsMemberAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 50)
)
srsMemberAddedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberAddedEvent.setStatus(
        ""
    )

srsMemberSuspendedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 51)
)
srsMemberSuspendedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberSuspendedEvent.setStatus(
        ""
    )

srsMemberRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 52)
)
srsMemberRemovedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberRemovedEvent.setStatus(
        ""
    )

srsMemberSyncStartedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 53)
)
srsMemberSyncStartedEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberSyncStartedEvent.setStatus(
        ""
    )

srsMemberSyncDoneEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 54)
)
srsMemberSyncDoneEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberSyncDoneEvent.setStatus(
        ""
    )

srsMemberSyncErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 55)
)
srsMemberSyncErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberSyncErrorEvent.setStatus(
        ""
    )

srsMemberRetryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 56)
)
srsMemberRetryEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberRetryEvent.setStatus(
        ""
    )

srsMemberErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 57)
)
srsMemberErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    srsMemberErrorEvent.setStatus(
        ""
    )

envPowerNominalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 58)
)
envPowerNominalEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envPowerNominalEvent.setStatus(
        ""
    )

envPowerWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 59)
)
envPowerWarningEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envPowerWarningEvent.setStatus(
        ""
    )

envPowerAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 60)
)
envPowerAlarmEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envPowerAlarmEvent.setStatus(
        ""
    )

envTemperatureNominalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 61)
)
envTemperatureNominalEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envTemperatureNominalEvent.setStatus(
        ""
    )

envInletTemperatureWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 62)
)
envInletTemperatureWarningEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envInletTemperatureWarningEvent.setStatus(
        ""
    )

envInletTemperatureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 63)
)
envInletTemperatureAlarmEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envInletTemperatureAlarmEvent.setStatus(
        ""
    )

envOutletTemperatureWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 64)
)
envOutletTemperatureWarningEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envOutletTemperatureWarningEvent.setStatus(
        ""
    )

envOutletTemperatureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 65)
)
envOutletTemperatureAlarmEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envOutletTemperatureAlarmEvent.setStatus(
        ""
    )

envFanNominalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 66)
)
envFanNominalEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envFanNominalEvent.setStatus(
        ""
    )

envFanWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 67)
)
envFanWarningEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envFanWarningEvent.setStatus(
        ""
    )

envFanAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 68)
)
envFanAlarmEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    envFanAlarmEvent.setStatus(
        ""
    )

eccMemoryErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 69)
)
eccMemoryErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    eccMemoryErrorEvent.setStatus(
        ""
    )

firmwareUploadCompleteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 70)
)
firmwareUploadCompleteEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    firmwareUploadCompleteEvent.setStatus(
        ""
    )

restartCompleteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 71)
)
restartCompleteEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    restartCompleteEvent.setStatus(
        ""
    )

maxInitiatorsExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 72)
)
maxInitiatorsExceededEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    maxInitiatorsExceededEvent.setStatus(
        ""
    )

powerSupplyOutOfSpecEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 100)
)
powerSupplyOutOfSpecEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    powerSupplyOutOfSpecEvent.setStatus(
        ""
    )

auxPowerOutOfSpecEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 101)
)
auxPowerOutOfSpecEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    auxPowerOutOfSpecEvent.setStatus(
        ""
    )

newTemperatureChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 102)
)
newTemperatureChangeEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    newTemperatureChangeEvent.setStatus(
        ""
    )

newPciErrorsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 103)
)
newPciErrorsEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    newPciErrorsEvent.setStatus(
        ""
    )

newMemoryParityErrorsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 104)
)
newMemoryParityErrorsEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    newMemoryParityErrorsEvent.setStatus(
        ""
    )

pciBusInterfaceErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 105)
)
pciBusInterfaceErrorEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    pciBusInterfaceErrorEvent.setStatus(
        ""
    )

fcInterfaceFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 106)
)
fcInterfaceFailureEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcInterfaceFailureEvent.setStatus(
        ""
    )

scsiInterfaceFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 107)
)
scsiInterfaceFailureEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    scsiInterfaceFailureEvent.setStatus(
        ""
    )

ssaInterfaceFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 108)
)
ssaInterfaceFailureEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    ssaInterfaceFailureEvent.setStatus(
        ""
    )

deviceFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 109)
)
deviceFailureEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    deviceFailureEvent.setStatus(
        ""
    )

fcLinkStatusChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 110)
)
fcLinkStatusChangeEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    fcLinkStatusChangeEvent.setStatus(
        ""
    )

newFcTranferErrorsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 111)
)
newFcTranferErrorsEvent.setObjects(
      *(("SANMgrV1-MIB", "paTrapSequenceNumber"),
        ("SANMgrV1-MIB", "paTime"),
        ("SANMgrV1-MIB", "paProducer"),
        ("SANMgrV1-MIB", "paEventClass"),
        ("SANMgrV1-MIB", "paEventCode"),
        ("SANMgrV1-MIB", "paSeq"),
        ("SANMgrV1-MIB", "paEventVars"))
)
if mibBuilder.loadTexts:
    newFcTranferErrorsEvent.setStatus(
        ""
    )

logWillOverwriteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 150)
)
if mibBuilder.loadTexts:
    logWillOverwriteEvent.setStatus(
        ""
    )

bootCompletedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2935, 1000, 0, 4444)
)
if mibBuilder.loadTexts:
    bootCompletedEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SANMgrV1-MIB",
    **{"ProductID": ProductID,
       "PathlightProduct": PathlightProduct,
       "Boolean": Boolean,
       "RowStatus": RowStatus,
       "LogCommand": LogCommand,
       "PltStatus": PltStatus,
       "FcStatus": FcStatus,
       "Interface": Interface,
       "Reset": Reset,
       "BaudRate": BaudRate,
       "HealthCheckLevel": HealthCheckLevel,
       "LogViewingLevel": LogViewingLevel,
       "DeviceType": DeviceType,
       "VendorIDInt": VendorIDInt,
       "FibreMedia": FibreMedia,
       "FibrePort": FibrePort,
       "FibreLoopIDMode": FibreLoopIDMode,
       "FibrePortMode": FibrePortMode,
       "FibreConnOptions": FibreConnOptions,
       "SsaSpeed": SsaSpeed,
       "PathingAlgorithm": PathingAlgorithm,
       "ScsiSpeed": ScsiSpeed,
       "ScsiRole": ScsiRole,
       "ScsiTermination": ScsiTermination,
       "ScsiCardType": ScsiCardType,
       "ScsiAnsiLevel": ScsiAnsiLevel,
       "pathlight": pathlight,
       "products": products,
       "sanGateway": sanGateway,
       "sanGateway1": sanGateway1,
       "sanGateway2": sanGateway2,
       "agent": agent,
       "paIdentify": paIdentify,
       "paReboot": paReboot,
       "paHealthCheckValue": paHealthCheckValue,
       "paHealthCheckLevel": paHealthCheckLevel,
       "paHealthCheckInterval": paHealthCheckInterval,
       "paEvRptLevel": paEvRptLevel,
       "paEventLogLevels": paEventLogLevels,
       "paTrapThresholds": paTrapThresholds,
       "paBaudRate": paBaudRate,
       "paEventLog": paEventLog,
       "paEventLogEntry": paEventLogEntry,
       "paIndex": paIndex,
       "paTime": paTime,
       "paProducer": paProducer,
       "paEventClass": paEventClass,
       "paEventCode": paEventCode,
       "paSeq": paSeq,
       "paEventVars": paEventVars,
       "paLogSize": paLogSize,
       "paCommand": paCommand,
       "paLogBoot": paLogBoot,
       "paLogNCurrent": paLogNCurrent,
       "paLogChronFirst": paLogChronFirst,
       "paLogChronLast": paLogChronLast,
       "paLogScroll": paLogScroll,
       "paLogFilename": paLogFilename,
       "paEnvironmentState": paEnvironmentState,
       "paGatewayFWRev": paGatewayFWRev,
       "paGatewayHWRev": paGatewayHWRev,
       "paSnmpFWRev": paSnmpFWRev,
       "paRidTag": paRidTag,
       "paSerialNumber": paSerialNumber,
       "paServerVersion": paServerVersion,
       "paProductType": paProductType,
       "paVPSEnabled": paVPSEnabled,
       "paLicenseKey": paLicenseKey,
       "paThirdPartyCopyEnabled": paThirdPartyCopyEnabled,
       "paVPSStatus": paVPSStatus,
       "paThirdPartyCopyStatus": paThirdPartyCopyStatus,
       "paCommandControlLUN": paCommandControlLUN,
       "paSanDirectorEnabled": paSanDirectorEnabled,
       "paNodeName": paNodeName,
       "paVPMStatus": paVPMStatus,
       "paSRSStatus": paSRSStatus,
       "paEthernetType": paEthernetType,
       "paTrapSequenceNumber": paTrapSequenceNumber,
       "paSysNodeNameMode": paSysNodeNameMode,
       "devices": devices,
       "pdDevices": pdDevices,
       "pdDevEntry": pdDevEntry,
       "pdIndex": pdIndex,
       "pdUID": pdUID,
       "pdType": pdType,
       "pdVendor": pdVendor,
       "pdProduct": pdProduct,
       "pdBlockSize": pdBlockSize,
       "pdCapacity": pdCapacity,
       "pdAccess": pdAccess,
       "pdRemovable": pdRemovable,
       "pdStatus": pdStatus,
       "pdSpeed": pdSpeed,
       "pdWidth": pdWidth,
       "pdSerial": pdSerial,
       "pdIdentify": pdIdentify,
       "pdInterfaceType": pdInterfaceType,
       "pdBus": pdBus,
       "pdId": pdId,
       "pdLun": pdLun,
       "pdCtlrIndex": pdCtlrIndex,
       "pdHWRev": pdHWRev,
       "pdFWRev": pdFWRev,
       "pdReset": pdReset,
       "pdStatusBits": pdStatusBits,
       "pdScsiAnsiLevel": pdScsiAnsiLevel,
       "pdTargetLun": pdTargetLun,
       "pdIpAddress": pdIpAddress,
       "controllers": controllers,
       "pcControllers": pcControllers,
       "pcCtlrEntry": pcCtlrEntry,
       "pcIndex": pcIndex,
       "pcType": pcType,
       "pcVendorId": pcVendorId,
       "pcProductId": pcProductId,
       "pcRevision": pcRevision,
       "pcSubVendor": pcSubVendor,
       "pcSubProduct": pcSubProduct,
       "pcMaxBurst": pcMaxBurst,
       "pcLatency": pcLatency,
       "pcIdentify": pcIdentify,
       "pcPCIBus": pcPCIBus,
       "pcPCIDev": pcPCIDev,
       "pcPCIFunc": pcPCIFunc,
       "pcReset": pcReset,
       "pcRescan": pcRescan,
       "pcLED": pcLED,
       "pcHWRev": pcHWRev,
       "pcFWRev": pcFWRev,
       "pcPCISlot": pcPCISlot,
       "pcPMCSlot": pcPMCSlot,
       "pcPCIClass": pcPCIClass,
       "pcSplitMode": pcSplitMode,
       "pcChannelMask": pcChannelMask,
       "pcPortHostType": pcPortHostType,
       "pcFCCtlrs": pcFCCtlrs,
       "fcCtlrEntry": fcCtlrEntry,
       "fcStatus": fcStatus,
       "fcMaxSpeed": fcMaxSpeed,
       "fcWWID": fcWWID,
       "fcFWRev": fcFWRev,
       "fcHWRev": fcHWRev,
       "fcLoopID": fcLoopID,
       "fcFrameSize": fcFrameSize,
       "fcPortType": fcPortType,
       "fcMedia": fcMedia,
       "fcSerialNumber": fcSerialNumber,
       "fcLoopIDMode": fcLoopIDMode,
       "fcALPhysicalAddress": fcALPhysicalAddress,
       "fcPortMode": fcPortMode,
       "fcConnectionOptions": fcConnectionOptions,
       "fcCtlrChipType": fcCtlrChipType,
       "fcTapeFeature": fcTapeFeature,
       "fcHardID": fcHardID,
       "fcCurrentSpeedSetting": fcCurrentSpeedSetting,
       "fcCurrentSpeed": fcCurrentSpeed,
       "fcFrameBufferSize": fcFrameBufferSize,
       "fcLinkFailureCount": fcLinkFailureCount,
       "fcLossSyncCount": fcLossSyncCount,
       "fcLossSignalCount": fcLossSignalCount,
       "fcProtocolErrorCount": fcProtocolErrorCount,
       "fcInvalidTxWordCount": fcInvalidTxWordCount,
       "fcInvalidCRCCount": fcInvalidCRCCount,
       "fcWWNodeName": fcWWNodeName,
       "pcSSACtlrs": pcSSACtlrs,
       "ssaCtlrEntry": ssaCtlrEntry,
       "ssaStatus1": ssaStatus1,
       "ssaStatus2": ssaStatus2,
       "ssaSpeed": ssaSpeed,
       "ssaUID": ssaUID,
       "ssaFWRev": ssaFWRev,
       "ssaMaxTarg": ssaMaxTarg,
       "ssaMaxInit": ssaMaxInit,
       "ssaPathAlg": ssaPathAlg,
       "ssaHWRev": ssaHWRev,
       "ssaMasterPriority": ssaMasterPriority,
       "ssaSATAQuota": ssaSATAQuota,
       "ssaSATBQuota": ssaSATBQuota,
       "ssaSATIQuota": ssaSATIQuota,
       "pcSCSICtlrs": pcSCSICtlrs,
       "scsiCtlrEntry": scsiCtlrEntry,
       "scsiStatus": scsiStatus,
       "scsiSpeed": scsiSpeed,
       "scsiRole": scsiRole,
       "scsiHostId": scsiHostId,
       "scsiMaxSpeed": scsiMaxSpeed,
       "scsiTerm": scsiTerm,
       "scsiIoCard": scsiIoCard,
       "scsiMaxIds": scsiMaxIds,
       "scsiMaxLuns": scsiMaxLuns,
       "scsiMaxWidth": scsiMaxWidth,
       "scsiHWRev": scsiHWRev,
       "scsiFWRev": scsiFWRev,
       "scsiResetOnPowerUp": scsiResetOnPowerUp,
       "scsiMultiInitEnabled": scsiMultiInitEnabled,
       "scsiAlternateHostId": scsiAlternateHostId,
       "notification": notification,
       "pnTrapDest": pnTrapDest,
       "pnTrapDestEntry": pnTrapDestEntry,
       "pnIndex": pnIndex,
       "pnIPAddr": pnIPAddr,
       "pnUdpPort": pnUdpPort,
       "pnTrapStyle": pnTrapStyle,
       "panelLED": panelLED,
       "ledReady": ledReady,
       "ledAuxPower": ledAuxPower,
       "ledMainPower": ledMainPower,
       "ledTempAlarm": ledTempAlarm,
       "ledTempWarn": ledTempWarn,
       "ledEtherCollision": ledEtherCollision,
       "ledEtherTransmit": ledEtherTransmit,
       "ledEtherLink": ledEtherLink,
       "ledScsi1": ledScsi1,
       "ledScsi2": ledScsi2,
       "ledScsi3": ledScsi3,
       "ledScsi4": ledScsi4,
       "ledActivity1": ledActivity1,
       "ledActivity2": ledActivity2,
       "ledActivity3": ledActivity3,
       "ledStatus1": ledStatus1,
       "ledStatus2": ledStatus2,
       "ledStatus3": ledStatus3,
       "ledAll": ledAll,
       "ledError": ledError,
       "ledEthernetSpeed": ledEthernetSpeed,
       "paHost": paHost,
       "hostCommand": hostCommand,
       "hostInitiator": hostInitiator,
       "hostInitiatorEntry": hostInitiatorEntry,
       "hostIndex": hostIndex,
       "hostRowStatus": hostRowStatus,
       "hostWWName": hostWWName,
       "hostName": hostName,
       "hostType": hostType,
       "hostPortID": hostPortID,
       "hostSANConnection": hostSANConnection,
       "hostConnectionType": hostConnectionType,
       "hostITLData": hostITLData,
       "hostIPAddr": hostIPAddr,
       "scsiMap": scsiMap,
       "scsiMapCommand": scsiMapCommand,
       "scsiChannelMap": scsiChannelMap,
       "scsiMapEntry": scsiMapEntry,
       "scsiMapRowStatus": scsiMapRowStatus,
       "scsiMapPort": scsiMapPort,
       "scsiMapTid": scsiMapTid,
       "scsiMapLun": scsiMapLun,
       "scsiMapAssignedLun": scsiMapAssignedLun,
       "scsiMapComments": scsiMapComments,
       "scsiMapPdIndex": scsiMapPdIndex,
       "deviceMap": deviceMap,
       "deviceMapCommand": deviceMapCommand,
       "dmDeviceMap": dmDeviceMap,
       "dmDevMapEntry": dmDevMapEntry,
       "dmRowStatus": dmRowStatus,
       "dmAssignedLun": dmAssignedLun,
       "dmType": dmType,
       "dmPort": dmPort,
       "dmTargetId": dmTargetId,
       "dmTargetLun": dmTargetLun,
       "dmUid": dmUid,
       "replication": replication,
       "srsDevTable": srsDevTable,
       "srsDevEntry": srsDevEntry,
       "srsDevId": srsDevId,
       "srsDevState": srsDevState,
       "srsDevCommand": srsDevCommand,
       "srsDevAssignedLun": srsDevAssignedLun,
       "srsDevMemberCount": srsDevMemberCount,
       "srsDevMembersOnline": srsDevMembersOnline,
       "srsDevFlags": srsDevFlags,
       "srsDevSizeInBlocks": srsDevSizeInBlocks,
       "srsDevBlockSize": srsDevBlockSize,
       "srsDevPrimary": srsDevPrimary,
       "srsMemTable": srsMemTable,
       "srsMemEntry": srsMemEntry,
       "srsMemDeviceId": srsMemDeviceId,
       "srsMemId": srsMemId,
       "srsMemState": srsMemState,
       "srsMemCommand": srsMemCommand,
       "srsMemType": srsMemType,
       "srsMemSyncPoint": srsMemSyncPoint,
       "srsMemAssignedLun": srsMemAssignedLun,
       "srsMemReadOptions": srsMemReadOptions,
       "srsMemWriteOptions": srsMemWriteOptions,
       "envData": envData,
       "envDataTable": envDataTable,
       "envDataEntry": envDataEntry,
       "envDataId": envDataId,
       "envDataName": envDataName,
       "envNominalLo": envNominalLo,
       "envNominalHi": envNominalHi,
       "envWarningLo": envWarningLo,
       "envWarningHi": envWarningHi,
       "envCurValue": envCurValue,
       "envCurStatus": envCurStatus,
       "envUnit": envUnit,
       "trapDefinition": trapDefinition,
       "ssaPortUpEvent": ssaPortUpEvent,
       "ssaPortDownEvent": ssaPortDownEvent,
       "ssaUidAddedEvent": ssaUidAddedEvent,
       "ssaUidRemovedEvent": ssaUidRemovedEvent,
       "ssaWebReconfiguredEvent": ssaWebReconfiguredEvent,
       "ssaAsyncErrorEvent": ssaAsyncErrorEvent,
       "ssaAdapterEvent": ssaAdapterEvent,
       "senseDataEvent": senseDataEvent,
       "unitAttentionEvent": unitAttentionEvent,
       "ibfEvent": ibfEvent,
       "temperatureChangeEvent": temperatureChangeEvent,
       "timeReferenceEvent": timeReferenceEvent,
       "shutdownEvent": shutdownEvent,
       "diagnosticEvent": diagnosticEvent,
       "configurationEvent": configurationEvent,
       "unexpectedScsiInterruptEvent": unexpectedScsiInterruptEvent,
       "lipResetEvent": lipResetEvent,
       "fcSystemErrorEvent": fcSystemErrorEvent,
       "fcRequestTransferErrorEvent": fcRequestTransferErrorEvent,
       "fcResponseTransferErrorEvent": fcResponseTransferErrorEvent,
       "memoryFaultEvent": memoryFaultEvent,
       "fcLipEvent": fcLipEvent,
       "fcLoopUpEvent": fcLoopUpEvent,
       "fcLoopDownEvent": fcLoopDownEvent,
       "pciBusParityErrorEvent": pciBusParityErrorEvent,
       "pciInterfaceErrorEvent": pciInterfaceErrorEvent,
       "scsiDeviceAddedEvent": scsiDeviceAddedEvent,
       "scsiBusResetEvent": scsiBusResetEvent,
       "deviceAddedEvent": deviceAddedEvent,
       "deviceRemovedEvent": deviceRemovedEvent,
       "loggingStartedEvent": loggingStartedEvent,
       "loggingStoppedEvent": loggingStoppedEvent,
       "interfaceBusFaultEvent": interfaceBusFaultEvent,
       "interfaceDeviceFaultEvent": interfaceDeviceFaultEvent,
       "scsiUnexpectedDisconnectEvent": scsiUnexpectedDisconnectEvent,
       "scsiParityErrorEvent": scsiParityErrorEvent,
       "fcPortDatabaseChangeEvent": fcPortDatabaseChangeEvent,
       "ddfMemoryErrorEvent": ddfMemoryErrorEvent,
       "fcDirectoryServerChangeEvent": fcDirectoryServerChangeEvent,
       "lunLimitExcededEvent": lunLimitExcededEvent,
       "fcTransferFailureEvent": fcTransferFailureEvent,
       "deviceLimitExcededEvent": deviceLimitExcededEvent,
       "fcDebugDumpEvent": fcDebugDumpEvent,
       "excessiveScsiBusErrorsEvent": excessiveScsiBusErrorsEvent,
       "memoryScrubberErrorEvent": memoryScrubberErrorEvent,
       "srsDeviceCreatedEvent": srsDeviceCreatedEvent,
       "srsDeviceOnlineEvent": srsDeviceOnlineEvent,
       "srsDeviceRemovedEvent": srsDeviceRemovedEvent,
       "srsDeviceFailedEvent": srsDeviceFailedEvent,
       "srsMemberAddedEvent": srsMemberAddedEvent,
       "srsMemberSuspendedEvent": srsMemberSuspendedEvent,
       "srsMemberRemovedEvent": srsMemberRemovedEvent,
       "srsMemberSyncStartedEvent": srsMemberSyncStartedEvent,
       "srsMemberSyncDoneEvent": srsMemberSyncDoneEvent,
       "srsMemberSyncErrorEvent": srsMemberSyncErrorEvent,
       "srsMemberRetryEvent": srsMemberRetryEvent,
       "srsMemberErrorEvent": srsMemberErrorEvent,
       "envPowerNominalEvent": envPowerNominalEvent,
       "envPowerWarningEvent": envPowerWarningEvent,
       "envPowerAlarmEvent": envPowerAlarmEvent,
       "envTemperatureNominalEvent": envTemperatureNominalEvent,
       "envInletTemperatureWarningEvent": envInletTemperatureWarningEvent,
       "envInletTemperatureAlarmEvent": envInletTemperatureAlarmEvent,
       "envOutletTemperatureWarningEvent": envOutletTemperatureWarningEvent,
       "envOutletTemperatureAlarmEvent": envOutletTemperatureAlarmEvent,
       "envFanNominalEvent": envFanNominalEvent,
       "envFanWarningEvent": envFanWarningEvent,
       "envFanAlarmEvent": envFanAlarmEvent,
       "eccMemoryErrorEvent": eccMemoryErrorEvent,
       "firmwareUploadCompleteEvent": firmwareUploadCompleteEvent,
       "restartCompleteEvent": restartCompleteEvent,
       "maxInitiatorsExceededEvent": maxInitiatorsExceededEvent,
       "powerSupplyOutOfSpecEvent": powerSupplyOutOfSpecEvent,
       "auxPowerOutOfSpecEvent": auxPowerOutOfSpecEvent,
       "newTemperatureChangeEvent": newTemperatureChangeEvent,
       "newPciErrorsEvent": newPciErrorsEvent,
       "newMemoryParityErrorsEvent": newMemoryParityErrorsEvent,
       "pciBusInterfaceErrorEvent": pciBusInterfaceErrorEvent,
       "fcInterfaceFailureEvent": fcInterfaceFailureEvent,
       "scsiInterfaceFailureEvent": scsiInterfaceFailureEvent,
       "ssaInterfaceFailureEvent": ssaInterfaceFailureEvent,
       "deviceFailureEvent": deviceFailureEvent,
       "fcLinkStatusChangeEvent": fcLinkStatusChangeEvent,
       "newFcTranferErrorsEvent": newFcTranferErrorsEvent,
       "logWillOverwriteEvent": logWillOverwriteEvent,
       "bootCompletedEvent": bootCompletedEvent}
)
