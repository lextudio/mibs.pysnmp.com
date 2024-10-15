# SNMP MIB module (SYMMCOMMONPPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMCOMMONPPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:45 2024
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

symmPPS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5)
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





class MasterValidValue(Integer32):
    """Custom type MasterValidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
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

_PpsInput_ObjectIdentity = ObjectIdentity
ppsInput = _PpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1)
)
_PpsInputStatus_ObjectIdentity = ObjectIdentity
ppsInputStatus = _PpsInputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1, 1)
)
_PpsInputConfig_ObjectIdentity = ObjectIdentity
ppsInputConfig = _PpsInputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1, 2)
)
_PpsOutput_ObjectIdentity = ObjectIdentity
ppsOutput = _PpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2)
)
_PpsOutputStatus_ObjectIdentity = ObjectIdentity
ppsOutputStatus = _PpsOutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2, 1)
)
_PpsOutputConfig_ObjectIdentity = ObjectIdentity
ppsOutputConfig = _PpsOutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2, 2)
)
_PpsConformance_ObjectIdentity = ObjectIdentity
ppsConformance = _PpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ppsConformance.setStatus("current")
_PpsCompliances_ObjectIdentity = ObjectIdentity
ppsCompliances = _PpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3, 1)
)
_PpsUocGroups_ObjectIdentity = ObjectIdentity
ppsUocGroups = _PpsUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMCOMMONPPS",
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
       "YesValue": YesValue,
       "OkValue": OkValue,
       "ValidValue": ValidValue,
       "TableRowChange": TableRowChange,
       "MasterValidValue": MasterValidValue,
       "PPS10MOutGenMode": PPS10MOutGenMode,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmPPS": symmPPS,
       "ppsInput": ppsInput,
       "ppsInputStatus": ppsInputStatus,
       "ppsInputConfig": ppsInputConfig,
       "ppsOutput": ppsOutput,
       "ppsOutputStatus": ppsOutputStatus,
       "ppsOutputConfig": ppsOutputConfig,
       "ppsConformance": ppsConformance,
       "ppsCompliances": ppsCompliances,
       "ppsUocGroups": ppsUocGroups}
)
