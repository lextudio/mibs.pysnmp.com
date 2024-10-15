# SNMP MIB module (AISLCDISCRETE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLCDISCRETE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:21 2024
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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLCDiscrete = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 24)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLCDiscreteInputTable_Object = MibTable
aiSLCDiscreteInputTable = _AiSLCDiscreteInputTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1)
)
if mibBuilder.loadTexts:
    aiSLCDiscreteInputTable.setStatus("current")
_AiSLCDiscreteInputEntry_Object = MibTableRow
aiSLCDiscreteInputEntry = _AiSLCDiscreteInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1)
)
aiSLCDiscreteInputEntry.setIndexNames(
    (0, "AISLCDISCRETE-MIB", "aislcdinPointNumber"),
)
if mibBuilder.loadTexts:
    aiSLCDiscreteInputEntry.setStatus("current")
_AislcdinPointNumber_Type = PositiveInteger
_AislcdinPointNumber_Object = MibTableColumn
aislcdinPointNumber = _AislcdinPointNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 1),
    _AislcdinPointNumber_Type()
)
aislcdinPointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdinPointNumber.setStatus("current")


class _AislcdinDescription_Type(DisplayString):
    """Custom type aislcdinDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdinDescription_Type.__name__ = "DisplayString"
_AislcdinDescription_Object = MibTableColumn
aislcdinDescription = _AislcdinDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 2),
    _AislcdinDescription_Type()
)
aislcdinDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinDescription.setStatus("current")


class _AislcdinTrapEnable_Type(Integer32):
    """Custom type aislcdinTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AislcdinTrapEnable_Type.__name__ = "Integer32"
_AislcdinTrapEnable_Object = MibTableColumn
aislcdinTrapEnable = _AislcdinTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 3),
    _AislcdinTrapEnable_Type()
)
aislcdinTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinTrapEnable.setStatus("current")


class _AislcdinNormalInput_Type(Integer32):
    """Custom type aislcdinNormalInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_AislcdinNormalInput_Type.__name__ = "Integer32"
_AislcdinNormalInput_Object = MibTableColumn
aislcdinNormalInput = _AislcdinNormalInput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 4),
    _AislcdinNormalInput_Type()
)
aislcdinNormalInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinNormalInput.setStatus("current")


class _AislcdinAlarmSeverity_Type(Integer32):
    """Custom type aislcdinAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("notReported", 5))
    )


_AislcdinAlarmSeverity_Type.__name__ = "Integer32"
_AislcdinAlarmSeverity_Object = MibTableColumn
aislcdinAlarmSeverity = _AislcdinAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 5),
    _AislcdinAlarmSeverity_Type()
)
aislcdinAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinAlarmSeverity.setStatus("current")


class _AislcdinNormalStateText_Type(DisplayString):
    """Custom type aislcdinNormalStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdinNormalStateText_Type.__name__ = "DisplayString"
_AislcdinNormalStateText_Object = MibTableColumn
aislcdinNormalStateText = _AislcdinNormalStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 6),
    _AislcdinNormalStateText_Type()
)
aislcdinNormalStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinNormalStateText.setStatus("current")


class _AislcdinAlarmStateText_Type(DisplayString):
    """Custom type aislcdinAlarmStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdinAlarmStateText_Type.__name__ = "DisplayString"
_AislcdinAlarmStateText_Object = MibTableColumn
aislcdinAlarmStateText = _AislcdinAlarmStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 7),
    _AislcdinAlarmStateText_Type()
)
aislcdinAlarmStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinAlarmStateText.setStatus("current")


class _AislcdinCurrentInput_Type(Integer32):
    """Custom type aislcdinCurrentInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_AislcdinCurrentInput_Type.__name__ = "Integer32"
_AislcdinCurrentInput_Object = MibTableColumn
aislcdinCurrentInput = _AislcdinCurrentInput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 8),
    _AislcdinCurrentInput_Type()
)
aislcdinCurrentInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdinCurrentInput.setStatus("current")


class _AislcdinLastChangeTime_Type(DisplayString):
    """Custom type aislcdinLastChangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 23),
    )


_AislcdinLastChangeTime_Type.__name__ = "DisplayString"
_AislcdinLastChangeTime_Object = MibTableColumn
aislcdinLastChangeTime = _AislcdinLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 9),
    _AislcdinLastChangeTime_Type()
)
aislcdinLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdinLastChangeTime.setStatus("current")


class _AislcdinCurrentState_Type(Integer32):
    """Custom type aislcdinCurrentState based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("normal", 5))
    )


_AislcdinCurrentState_Type.__name__ = "Integer32"
_AislcdinCurrentState_Object = MibTableColumn
aislcdinCurrentState = _AislcdinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 10),
    _AislcdinCurrentState_Type()
)
aislcdinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdinCurrentState.setStatus("current")


class _AislcdinCurrentStateText_Type(DisplayString):
    """Custom type aislcdinCurrentStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdinCurrentStateText_Type.__name__ = "DisplayString"
_AislcdinCurrentStateText_Object = MibTableColumn
aislcdinCurrentStateText = _AislcdinCurrentStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 11),
    _AislcdinCurrentStateText_Type()
)
aislcdinCurrentStateText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdinCurrentStateText.setStatus("current")


class _Aislcdintl1AccessID_Type(DisplayString):
    """Custom type aislcdintl1AccessID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Aislcdintl1AccessID_Type.__name__ = "DisplayString"
_Aislcdintl1AccessID_Object = MibTableColumn
aislcdintl1AccessID = _Aislcdintl1AccessID_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 12),
    _Aislcdintl1AccessID_Type()
)
aislcdintl1AccessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1AccessID.setStatus("current")
_Aislcdintl1Provisioned_Type = TruthValue
_Aislcdintl1Provisioned_Object = MibTableColumn
aislcdintl1Provisioned = _Aislcdintl1Provisioned_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 13),
    _Aislcdintl1Provisioned_Type()
)
aislcdintl1Provisioned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1Provisioned.setStatus("current")


class _Aislcdintl1AccessIDType_Type(Integer32):
    """Custom type aislcdintl1AccessIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("environmental", 2),
          ("equipment", 1))
    )


_Aislcdintl1AccessIDType_Type.__name__ = "Integer32"
_Aislcdintl1AccessIDType_Object = MibTableColumn
aislcdintl1AccessIDType = _Aislcdintl1AccessIDType_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 14),
    _Aislcdintl1AccessIDType_Type()
)
aislcdintl1AccessIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1AccessIDType.setStatus("current")


class _Aislcdintl1NotificationCode_Type(Integer32):
    """Custom type aislcdintl1NotificationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_Aislcdintl1NotificationCode_Type.__name__ = "Integer32"
_Aislcdintl1NotificationCode_Object = MibTableColumn
aislcdintl1NotificationCode = _Aislcdintl1NotificationCode_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 15),
    _Aislcdintl1NotificationCode_Type()
)
aislcdintl1NotificationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1NotificationCode.setStatus("current")


class _Aislcdintl1ServiceAffecting_Type(Integer32):
    """Custom type aislcdintl1ServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceAffecting", 2),
          ("serviceAffecting", 1))
    )


_Aislcdintl1ServiceAffecting_Type.__name__ = "Integer32"
_Aislcdintl1ServiceAffecting_Object = MibTableColumn
aislcdintl1ServiceAffecting = _Aislcdintl1ServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 16),
    _Aislcdintl1ServiceAffecting_Type()
)
aislcdintl1ServiceAffecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1ServiceAffecting.setStatus("current")


class _Aislcdintl1ConditionType_Type(DisplayString):
    """Custom type aislcdintl1ConditionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Aislcdintl1ConditionType_Type.__name__ = "DisplayString"
_Aislcdintl1ConditionType_Object = MibTableColumn
aislcdintl1ConditionType = _Aislcdintl1ConditionType_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 17),
    _Aislcdintl1ConditionType_Type()
)
aislcdintl1ConditionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1ConditionType.setStatus("current")


class _Aislcdintl1ConditionDescription_Type(DisplayString):
    """Custom type aislcdintl1ConditionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Aislcdintl1ConditionDescription_Type.__name__ = "DisplayString"
_Aislcdintl1ConditionDescription_Object = MibTableColumn
aislcdintl1ConditionDescription = _Aislcdintl1ConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 18),
    _Aislcdintl1ConditionDescription_Type()
)
aislcdintl1ConditionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1ConditionDescription.setStatus("current")


class _Aislcdintl1AlarmType_Type(DisplayString):
    """Custom type aislcdintl1AlarmType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Aislcdintl1AlarmType_Type.__name__ = "DisplayString"
_Aislcdintl1AlarmType_Object = MibTableColumn
aislcdintl1AlarmType = _Aislcdintl1AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 19),
    _Aislcdintl1AlarmType_Type()
)
aislcdintl1AlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1AlarmType.setStatus("current")


class _Aislcdintl1AlarmMessage_Type(DisplayString):
    """Custom type aislcdintl1AlarmMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aislcdintl1AlarmMessage_Type.__name__ = "DisplayString"
_Aislcdintl1AlarmMessage_Object = MibTableColumn
aislcdintl1AlarmMessage = _Aislcdintl1AlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 20),
    _Aislcdintl1AlarmMessage_Type()
)
aislcdintl1AlarmMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdintl1AlarmMessage.setStatus("current")


class _AislcdinDebounceValue_Type(Integer32):
    """Custom type aislcdinDebounceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AislcdinDebounceValue_Type.__name__ = "Integer32"
_AislcdinDebounceValue_Object = MibTableColumn
aislcdinDebounceValue = _AislcdinDebounceValue_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 1, 1, 21),
    _AislcdinDebounceValue_Type()
)
aislcdinDebounceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdinDebounceValue.setStatus("current")
_AiSLCDiscreteOutputTable_Object = MibTable
aiSLCDiscreteOutputTable = _AiSLCDiscreteOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2)
)
if mibBuilder.loadTexts:
    aiSLCDiscreteOutputTable.setStatus("current")
_AiSLCDiscreteOutputEntry_Object = MibTableRow
aiSLCDiscreteOutputEntry = _AiSLCDiscreteOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1)
)
aiSLCDiscreteOutputEntry.setIndexNames(
    (0, "AISLCDISCRETE-MIB", "aislcdoutPointNumber"),
)
if mibBuilder.loadTexts:
    aiSLCDiscreteOutputEntry.setStatus("current")
_AislcdoutPointNumber_Type = PositiveInteger
_AislcdoutPointNumber_Object = MibTableColumn
aislcdoutPointNumber = _AislcdoutPointNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 1),
    _AislcdoutPointNumber_Type()
)
aislcdoutPointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdoutPointNumber.setStatus("current")


class _AislcdoutDescription_Type(DisplayString):
    """Custom type aislcdoutDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdoutDescription_Type.__name__ = "DisplayString"
_AislcdoutDescription_Object = MibTableColumn
aislcdoutDescription = _AislcdoutDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 2),
    _AislcdoutDescription_Type()
)
aislcdoutDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutDescription.setStatus("current")


class _AislcdoutOutputEnable_Type(Integer32):
    """Custom type aislcdoutOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AislcdoutOutputEnable_Type.__name__ = "Integer32"
_AislcdoutOutputEnable_Object = MibTableColumn
aislcdoutOutputEnable = _AislcdoutOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 3),
    _AislcdoutOutputEnable_Type()
)
aislcdoutOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutOutputEnable.setStatus("current")


class _AislcdoutNormalOutput_Type(Integer32):
    """Custom type aislcdoutNormalOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relayOff", 2),
          ("relayOn", 1))
    )


_AislcdoutNormalOutput_Type.__name__ = "Integer32"
_AislcdoutNormalOutput_Object = MibTableColumn
aislcdoutNormalOutput = _AislcdoutNormalOutput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 4),
    _AislcdoutNormalOutput_Type()
)
aislcdoutNormalOutput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aislcdoutNormalOutput.setStatus("deprecated")


class _AislcdoutMomentaryTimeout_Type(Integer32):
    """Custom type aislcdoutMomentaryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AislcdoutMomentaryTimeout_Type.__name__ = "Integer32"
_AislcdoutMomentaryTimeout_Object = MibTableColumn
aislcdoutMomentaryTimeout = _AislcdoutMomentaryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 5),
    _AislcdoutMomentaryTimeout_Type()
)
aislcdoutMomentaryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutMomentaryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aislcdoutMomentaryTimeout.setUnits("0.1 second")


class _AislcdoutCurrentOutput_Type(Integer32):
    """Custom type aislcdoutCurrentOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relayOff", 2),
          ("relayOn", 1))
    )


_AislcdoutCurrentOutput_Type.__name__ = "Integer32"
_AislcdoutCurrentOutput_Object = MibTableColumn
aislcdoutCurrentOutput = _AislcdoutCurrentOutput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 6),
    _AislcdoutCurrentOutput_Type()
)
aislcdoutCurrentOutput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aislcdoutCurrentOutput.setStatus("deprecated")


class _Aislcdouttl1AccessID_Type(DisplayString):
    """Custom type aislcdouttl1AccessID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Aislcdouttl1AccessID_Type.__name__ = "DisplayString"
_Aislcdouttl1AccessID_Object = MibTableColumn
aislcdouttl1AccessID = _Aislcdouttl1AccessID_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 7),
    _Aislcdouttl1AccessID_Type()
)
aislcdouttl1AccessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdouttl1AccessID.setStatus("current")


class _AislcdoutTrapEnable_Type(Integer32):
    """Custom type aislcdoutTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AislcdoutTrapEnable_Type.__name__ = "Integer32"
_AislcdoutTrapEnable_Object = MibTableColumn
aislcdoutTrapEnable = _AislcdoutTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 8),
    _AislcdoutTrapEnable_Type()
)
aislcdoutTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutTrapEnable.setStatus("current")


class _AislcdoutAlarmStateOutput_Type(Integer32):
    """Custom type aislcdoutAlarmStateOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("de-energized", 2),
          ("energized", 1))
    )


_AislcdoutAlarmStateOutput_Type.__name__ = "Integer32"
_AislcdoutAlarmStateOutput_Object = MibTableColumn
aislcdoutAlarmStateOutput = _AislcdoutAlarmStateOutput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 9),
    _AislcdoutAlarmStateOutput_Type()
)
aislcdoutAlarmStateOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutAlarmStateOutput.setStatus("current")


class _AislcdoutAlarmSeverity_Type(Integer32):
    """Custom type aislcdoutAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("notReported", 5))
    )


_AislcdoutAlarmSeverity_Type.__name__ = "Integer32"
_AislcdoutAlarmSeverity_Object = MibTableColumn
aislcdoutAlarmSeverity = _AislcdoutAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 10),
    _AislcdoutAlarmSeverity_Type()
)
aislcdoutAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutAlarmSeverity.setStatus("current")


class _AislcdoutNonAlarmStateText_Type(DisplayString):
    """Custom type aislcdoutNonAlarmStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdoutNonAlarmStateText_Type.__name__ = "DisplayString"
_AislcdoutNonAlarmStateText_Object = MibTableColumn
aislcdoutNonAlarmStateText = _AislcdoutNonAlarmStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 11),
    _AislcdoutNonAlarmStateText_Type()
)
aislcdoutNonAlarmStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutNonAlarmStateText.setStatus("current")


class _AislcdoutAlarmStateText_Type(DisplayString):
    """Custom type aislcdoutAlarmStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdoutAlarmStateText_Type.__name__ = "DisplayString"
_AislcdoutAlarmStateText_Object = MibTableColumn
aislcdoutAlarmStateText = _AislcdoutAlarmStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 12),
    _AislcdoutAlarmStateText_Type()
)
aislcdoutAlarmStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutAlarmStateText.setStatus("current")


class _AislcdoutOutput_Type(Integer32):
    """Custom type aislcdoutOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("de-energized", 2),
          ("energized", 1))
    )


_AislcdoutOutput_Type.__name__ = "Integer32"
_AislcdoutOutput_Object = MibTableColumn
aislcdoutOutput = _AislcdoutOutput_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 13),
    _AislcdoutOutput_Type()
)
aislcdoutOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutOutput.setStatus("current")


class _AislcdoutLastChangeTime_Type(DisplayString):
    """Custom type aislcdoutLastChangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 23),
    )


_AislcdoutLastChangeTime_Type.__name__ = "DisplayString"
_AislcdoutLastChangeTime_Object = MibTableColumn
aislcdoutLastChangeTime = _AislcdoutLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 14),
    _AislcdoutLastChangeTime_Type()
)
aislcdoutLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdoutLastChangeTime.setStatus("current")


class _AislcdoutCurrentState_Type(Integer32):
    """Custom type aislcdoutCurrentState based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("normal", 5))
    )


_AislcdoutCurrentState_Type.__name__ = "Integer32"
_AislcdoutCurrentState_Object = MibTableColumn
aislcdoutCurrentState = _AislcdoutCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 15),
    _AislcdoutCurrentState_Type()
)
aislcdoutCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdoutCurrentState.setStatus("current")


class _AislcdoutCurrentStateText_Type(DisplayString):
    """Custom type aislcdoutCurrentStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcdoutCurrentStateText_Type.__name__ = "DisplayString"
_AislcdoutCurrentStateText_Object = MibTableColumn
aislcdoutCurrentStateText = _AislcdoutCurrentStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 16),
    _AislcdoutCurrentStateText_Type()
)
aislcdoutCurrentStateText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdoutCurrentStateText.setStatus("current")


class _AislcdoutEnergizeExpression_Type(DisplayString):
    """Custom type aislcdoutEnergizeExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AislcdoutEnergizeExpression_Type.__name__ = "DisplayString"
_AislcdoutEnergizeExpression_Object = MibTableColumn
aislcdoutEnergizeExpression = _AislcdoutEnergizeExpression_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 2, 1, 17),
    _AislcdoutEnergizeExpression_Type()
)
aislcdoutEnergizeExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcdoutEnergizeExpression.setStatus("current")


class _AislcdiscPowerSupplyStatus_Type(Integer32):
    """Custom type aislcdiscPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("trouble", 2))
    )


_AislcdiscPowerSupplyStatus_Type.__name__ = "Integer32"
_AislcdiscPowerSupplyStatus_Object = MibScalar
aislcdiscPowerSupplyStatus = _AislcdiscPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 3),
    _AislcdiscPowerSupplyStatus_Type()
)
aislcdiscPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscPowerSupplyStatus.setStatus("current")


class _AislcdiscPowerSupplyAStatus_Type(Integer32):
    """Custom type aislcdiscPowerSupplyAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("overVoltage", 3),
          ("underVoltage", 2))
    )


_AislcdiscPowerSupplyAStatus_Type.__name__ = "Integer32"
_AislcdiscPowerSupplyAStatus_Object = MibScalar
aislcdiscPowerSupplyAStatus = _AislcdiscPowerSupplyAStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 4),
    _AislcdiscPowerSupplyAStatus_Type()
)
aislcdiscPowerSupplyAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscPowerSupplyAStatus.setStatus("current")


class _AislcdiscPowerSupplyBStatus_Type(Integer32):
    """Custom type aislcdiscPowerSupplyBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("overVoltage", 3),
          ("underVoltage", 2))
    )


_AislcdiscPowerSupplyBStatus_Type.__name__ = "Integer32"
_AislcdiscPowerSupplyBStatus_Object = MibScalar
aislcdiscPowerSupplyBStatus = _AislcdiscPowerSupplyBStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 5),
    _AislcdiscPowerSupplyBStatus_Type()
)
aislcdiscPowerSupplyBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscPowerSupplyBStatus.setStatus("current")


class _AislcdiscFanStatus_Type(Integer32):
    """Custom type aislcdiscFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("okay", 1))
    )


_AislcdiscFanStatus_Type.__name__ = "Integer32"
_AislcdiscFanStatus_Object = MibScalar
aislcdiscFanStatus = _AislcdiscFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 6),
    _AislcdiscFanStatus_Type()
)
aislcdiscFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscFanStatus.setStatus("current")


class _Aislcdisc5VPowerSupplyAStatus_Type(Integer32):
    """Custom type aislcdisc5VPowerSupplyAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("okay", 1))
    )


_Aislcdisc5VPowerSupplyAStatus_Type.__name__ = "Integer32"
_Aislcdisc5VPowerSupplyAStatus_Object = MibScalar
aislcdisc5VPowerSupplyAStatus = _Aislcdisc5VPowerSupplyAStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 7),
    _Aislcdisc5VPowerSupplyAStatus_Type()
)
aislcdisc5VPowerSupplyAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdisc5VPowerSupplyAStatus.setStatus("current")


class _Aislcdisc5VPowerSupplyBStatus_Type(Integer32):
    """Custom type aislcdisc5VPowerSupplyBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notPresent", 3),
          ("okay", 1))
    )


_Aislcdisc5VPowerSupplyBStatus_Type.__name__ = "Integer32"
_Aislcdisc5VPowerSupplyBStatus_Object = MibScalar
aislcdisc5VPowerSupplyBStatus = _Aislcdisc5VPowerSupplyBStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 8),
    _Aislcdisc5VPowerSupplyBStatus_Type()
)
aislcdisc5VPowerSupplyBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdisc5VPowerSupplyBStatus.setStatus("current")


class _AislcdiscFiber1TransmitterStatus_Type(Integer32):
    """Custom type aislcdiscFiber1TransmitterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notPresent", 3),
          ("okay", 1))
    )


_AislcdiscFiber1TransmitterStatus_Type.__name__ = "Integer32"
_AislcdiscFiber1TransmitterStatus_Object = MibScalar
aislcdiscFiber1TransmitterStatus = _AislcdiscFiber1TransmitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 9),
    _AislcdiscFiber1TransmitterStatus_Type()
)
aislcdiscFiber1TransmitterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscFiber1TransmitterStatus.setStatus("current")


class _AislcdiscFiber2TransmitterStatus_Type(Integer32):
    """Custom type aislcdiscFiber2TransmitterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notPresent", 3),
          ("okay", 1))
    )


_AislcdiscFiber2TransmitterStatus_Type.__name__ = "Integer32"
_AislcdiscFiber2TransmitterStatus_Object = MibScalar
aislcdiscFiber2TransmitterStatus = _AislcdiscFiber2TransmitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 10),
    _AislcdiscFiber2TransmitterStatus_Type()
)
aislcdiscFiber2TransmitterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscFiber2TransmitterStatus.setStatus("current")


class _AislcdiscAnalogInputPowerSupplyStatus_Type(Integer32):
    """Custom type aislcdiscAnalogInputPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notPresent", 3),
          ("okay", 1))
    )


_AislcdiscAnalogInputPowerSupplyStatus_Type.__name__ = "Integer32"
_AislcdiscAnalogInputPowerSupplyStatus_Object = MibScalar
aislcdiscAnalogInputPowerSupplyStatus = _AislcdiscAnalogInputPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 24, 11),
    _AislcdiscAnalogInputPowerSupplyStatus_Type()
)
aislcdiscAnalogInputPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcdiscAnalogInputPowerSupplyStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLCDISCRETE-MIB",
    **{"PositiveInteger": PositiveInteger,
       "aii": aii,
       "aiSLCDiscrete": aiSLCDiscrete,
       "aiSLCDiscreteInputTable": aiSLCDiscreteInputTable,
       "aiSLCDiscreteInputEntry": aiSLCDiscreteInputEntry,
       "aislcdinPointNumber": aislcdinPointNumber,
       "aislcdinDescription": aislcdinDescription,
       "aislcdinTrapEnable": aislcdinTrapEnable,
       "aislcdinNormalInput": aislcdinNormalInput,
       "aislcdinAlarmSeverity": aislcdinAlarmSeverity,
       "aislcdinNormalStateText": aislcdinNormalStateText,
       "aislcdinAlarmStateText": aislcdinAlarmStateText,
       "aislcdinCurrentInput": aislcdinCurrentInput,
       "aislcdinLastChangeTime": aislcdinLastChangeTime,
       "aislcdinCurrentState": aislcdinCurrentState,
       "aislcdinCurrentStateText": aislcdinCurrentStateText,
       "aislcdintl1AccessID": aislcdintl1AccessID,
       "aislcdintl1Provisioned": aislcdintl1Provisioned,
       "aislcdintl1AccessIDType": aislcdintl1AccessIDType,
       "aislcdintl1NotificationCode": aislcdintl1NotificationCode,
       "aislcdintl1ServiceAffecting": aislcdintl1ServiceAffecting,
       "aislcdintl1ConditionType": aislcdintl1ConditionType,
       "aislcdintl1ConditionDescription": aislcdintl1ConditionDescription,
       "aislcdintl1AlarmType": aislcdintl1AlarmType,
       "aislcdintl1AlarmMessage": aislcdintl1AlarmMessage,
       "aislcdinDebounceValue": aislcdinDebounceValue,
       "aiSLCDiscreteOutputTable": aiSLCDiscreteOutputTable,
       "aiSLCDiscreteOutputEntry": aiSLCDiscreteOutputEntry,
       "aislcdoutPointNumber": aislcdoutPointNumber,
       "aislcdoutDescription": aislcdoutDescription,
       "aislcdoutOutputEnable": aislcdoutOutputEnable,
       "aislcdoutNormalOutput": aislcdoutNormalOutput,
       "aislcdoutMomentaryTimeout": aislcdoutMomentaryTimeout,
       "aislcdoutCurrentOutput": aislcdoutCurrentOutput,
       "aislcdouttl1AccessID": aislcdouttl1AccessID,
       "aislcdoutTrapEnable": aislcdoutTrapEnable,
       "aislcdoutAlarmStateOutput": aislcdoutAlarmStateOutput,
       "aislcdoutAlarmSeverity": aislcdoutAlarmSeverity,
       "aislcdoutNonAlarmStateText": aislcdoutNonAlarmStateText,
       "aislcdoutAlarmStateText": aislcdoutAlarmStateText,
       "aislcdoutOutput": aislcdoutOutput,
       "aislcdoutLastChangeTime": aislcdoutLastChangeTime,
       "aislcdoutCurrentState": aislcdoutCurrentState,
       "aislcdoutCurrentStateText": aislcdoutCurrentStateText,
       "aislcdoutEnergizeExpression": aislcdoutEnergizeExpression,
       "aislcdiscPowerSupplyStatus": aislcdiscPowerSupplyStatus,
       "aislcdiscPowerSupplyAStatus": aislcdiscPowerSupplyAStatus,
       "aislcdiscPowerSupplyBStatus": aislcdiscPowerSupplyBStatus,
       "aislcdiscFanStatus": aislcdiscFanStatus,
       "aislcdisc5VPowerSupplyAStatus": aislcdisc5VPowerSupplyAStatus,
       "aislcdisc5VPowerSupplyBStatus": aislcdisc5VPowerSupplyBStatus,
       "aislcdiscFiber1TransmitterStatus": aislcdiscFiber1TransmitterStatus,
       "aislcdiscFiber2TransmitterStatus": aislcdiscFiber2TransmitterStatus,
       "aislcdiscAnalogInputPowerSupplyStatus": aislcdiscAnalogInputPowerSupplyStatus}
)
