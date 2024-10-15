# SNMP MIB module (SYMMCOMMON10M) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMCOMMON10M
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:42 2024
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

(symmPhysicalSignal,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmCommon10M = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4)
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





class TPInputPriority(Integer32):
    """Custom type TPInputPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )





class InputFrameType(Integer32):
    """Custom type InputFrameType based on Integer32"""
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





class TPSSMValue(Integer32):
    """Custom type TPSSMValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
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





class TableRowChange(Integer32):
    """Custom type TableRowChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3))
    )





class PPS10MOutGenMode(Integer32):
    """Custom type PPS10MOutGenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("squelch", 1))
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

_TenMInput_ObjectIdentity = ObjectIdentity
tenMInput = _TenMInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1)
)
_TenMInputStatus_ObjectIdentity = ObjectIdentity
tenMInputStatus = _TenMInputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1, 1)
)
_TenMInputConfig_ObjectIdentity = ObjectIdentity
tenMInputConfig = _TenMInputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1, 2)
)
_TenMOutput_ObjectIdentity = ObjectIdentity
tenMOutput = _TenMOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2)
)
_TenMOutputStatus_ObjectIdentity = ObjectIdentity
tenMOutputStatus = _TenMOutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2, 1)
)
_TenMOutputConfig_ObjectIdentity = ObjectIdentity
tenMOutputConfig = _TenMOutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2, 2)
)
_TenMInOutConformance_ObjectIdentity = ObjectIdentity
tenMInOutConformance = _TenMInOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tenMInOutConformance.setStatus("current")
_TenMInOutCompliances_ObjectIdentity = ObjectIdentity
tenMInOutCompliances = _TenMInOutCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3, 1)
)
_TenMInOutUocGroups_ObjectIdentity = ObjectIdentity
tenMInOutUocGroups = _TenMInOutUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMCOMMON10M",
    **{"EnaValue": EnaValue,
       "TPModuleID": TPModuleID,
       "OnValue": OnValue,
       "TPInputPriority": TPInputPriority,
       "InputFrameType": InputFrameType,
       "TPSSMValue": TPSSMValue,
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
       "TableRowChange": TableRowChange,
       "PPS10MOutGenMode": PPS10MOutGenMode,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmCommon10M": symmCommon10M,
       "tenMInput": tenMInput,
       "tenMInputStatus": tenMInputStatus,
       "tenMInputConfig": tenMInputConfig,
       "tenMOutput": tenMOutput,
       "tenMOutputStatus": tenMOutputStatus,
       "tenMOutputConfig": tenMOutputConfig,
       "tenMInOutConformance": tenMInOutConformance,
       "tenMInOutCompliances": tenMInOutCompliances,
       "tenMInOutUocGroups": tenMInOutUocGroups}
)
