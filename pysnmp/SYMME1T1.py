# SNMP MIB module (SYMME1T1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMME1T1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:49 2024
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

(EnableValue,
 ONVALUETYPE,
 symmPhysicalSignal) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "ONVALUETYPE",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmE1T1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2)
)
symmE1T1.setRevisions(
        ("2011-03-18 17:06",)
)


# Types definitions



class TP5000PQLVALUE(Integer32):
    """Custom type TP5000PQLVALUE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )





class INPUTE1T1FRAMETYPE(Integer32):
    """Custom type INPUTE1T1FRAMETYPE based on Integer32"""
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





class PORTSTATETYPE(Integer32):
    """Custom type PORTSTATETYPE based on Integer32"""
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





class OUTPUTE1T1FRAMETYPE(Integer32):
    """Custom type OUTPUTE1T1FRAMETYPE based on Integer32"""
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

_E1T1input_ObjectIdentity = ObjectIdentity
e1T1input = _E1T1input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1)
)
_InputE1T1Status_ObjectIdentity = ObjectIdentity
inputE1T1Status = _InputE1T1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1)
)
_E1T1InputStatusTable_Object = MibTable
e1T1InputStatusTable = _E1T1InputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    e1T1InputStatusTable.setStatus("current")
_E1T1InputStatusEntry_Object = MibTableRow
e1T1InputStatusEntry = _E1T1InputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1)
)
e1T1InputStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMME1T1", "e1T1InputStatusIndex"),
)
if mibBuilder.loadTexts:
    e1T1InputStatusEntry.setStatus("current")


class _E1T1InputStatusIndex_Type(Integer32):
    """Custom type e1T1InputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_E1T1InputStatusIndex_Type.__name__ = "Integer32"
_E1T1InputStatusIndex_Object = MibTableColumn
e1T1InputStatusIndex = _E1T1InputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 1),
    _E1T1InputStatusIndex_Type()
)
e1T1InputStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1T1InputStatusIndex.setStatus("current")
_E1T1InputPQLCurValueV1_Type = TP5000PQLVALUE
_E1T1InputPQLCurValueV1_Object = MibTableColumn
e1T1InputPQLCurValueV1 = _E1T1InputPQLCurValueV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 3),
    _E1T1InputPQLCurValueV1_Type()
)
e1T1InputPQLCurValueV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1T1InputPQLCurValueV1.setStatus("current")
_E1T1InputPortStatusV1_Type = DisplayString
_E1T1InputPortStatusV1_Object = MibTableColumn
e1T1InputPortStatusV1 = _E1T1InputPortStatusV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 4),
    _E1T1InputPortStatusV1_Type()
)
e1T1InputPortStatusV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1T1InputPortStatusV1.setStatus("current")
_E1T1InputConfig_ObjectIdentity = ObjectIdentity
e1T1InputConfig = _E1T1InputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2)
)
_E1T1InputConfigTable_Object = MibTable
e1T1InputConfigTable = _E1T1InputConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    e1T1InputConfigTable.setStatus("current")
_E1T1InputConfigEntry_Object = MibTableRow
e1T1InputConfigEntry = _E1T1InputConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1)
)
e1T1InputConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMME1T1", "e1T1InputConfigIndex"),
)
if mibBuilder.loadTexts:
    e1T1InputConfigEntry.setStatus("current")


class _E1T1InputConfigIndex_Type(Integer32):
    """Custom type e1T1InputConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_E1T1InputConfigIndex_Type.__name__ = "Integer32"
_E1T1InputConfigIndex_Object = MibTableColumn
e1T1InputConfigIndex = _E1T1InputConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 1),
    _E1T1InputConfigIndex_Type()
)
e1T1InputConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1T1InputConfigIndex.setStatus("current")
_E1T1InputFrameTypeV1_Type = INPUTE1T1FRAMETYPE
_E1T1InputFrameTypeV1_Object = MibTableColumn
e1T1InputFrameTypeV1 = _E1T1InputFrameTypeV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 2),
    _E1T1InputFrameTypeV1_Type()
)
e1T1InputFrameTypeV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1InputFrameTypeV1.setStatus("current")
_E1T1InputCRCStateV1_Type = EnableValue
_E1T1InputCRCStateV1_Object = MibTableColumn
e1T1InputCRCStateV1 = _E1T1InputCRCStateV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 3),
    _E1T1InputCRCStateV1_Type()
)
e1T1InputCRCStateV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1InputCRCStateV1.setStatus("current")
_E1T1InputSSMStateV1_Type = EnableValue
_E1T1InputSSMStateV1_Object = MibTableColumn
e1T1InputSSMStateV1 = _E1T1InputSSMStateV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 4),
    _E1T1InputSSMStateV1_Type()
)
e1T1InputSSMStateV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1InputSSMStateV1.setStatus("current")


class _E1T1InputSSMBitV1_Type(Integer32):
    """Custom type e1T1InputSSMBitV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_E1T1InputSSMBitV1_Type.__name__ = "Integer32"
_E1T1InputSSMBitV1_Object = MibTableColumn
e1T1InputSSMBitV1 = _E1T1InputSSMBitV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 5),
    _E1T1InputSSMBitV1_Type()
)
e1T1InputSSMBitV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1InputSSMBitV1.setStatus("current")
_E1T1InputPQLValueV1_Type = TP5000PQLVALUE
_E1T1InputPQLValueV1_Object = MibTableColumn
e1T1InputPQLValueV1 = _E1T1InputPQLValueV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 6),
    _E1T1InputPQLValueV1_Type()
)
e1T1InputPQLValueV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1InputPQLValueV1.setStatus("current")
_ET1InputZeroSupprV1_Type = ONVALUETYPE
_ET1InputZeroSupprV1_Object = MibTableColumn
eT1InputZeroSupprV1 = _ET1InputZeroSupprV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 7),
    _ET1InputZeroSupprV1_Type()
)
eT1InputZeroSupprV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eT1InputZeroSupprV1.setStatus("current")
_E1T1Output_ObjectIdentity = ObjectIdentity
e1T1Output = _E1T1Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2)
)
_E1T1OutputStatus_ObjectIdentity = ObjectIdentity
e1T1OutputStatus = _E1T1OutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1)
)
_E1T1OutputStatusTable_Object = MibTable
e1T1OutputStatusTable = _E1T1OutputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    e1T1OutputStatusTable.setStatus("current")
_E1T1OutputStatusEntry_Object = MibTableRow
e1T1OutputStatusEntry = _E1T1OutputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1)
)
e1T1OutputStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMME1T1", "e1T1OutputStatusIndex"),
)
if mibBuilder.loadTexts:
    e1T1OutputStatusEntry.setStatus("current")


class _E1T1OutputStatusIndex_Type(Integer32):
    """Custom type e1T1OutputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_E1T1OutputStatusIndex_Type.__name__ = "Integer32"
_E1T1OutputStatusIndex_Object = MibTableColumn
e1T1OutputStatusIndex = _E1T1OutputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 1),
    _E1T1OutputStatusIndex_Type()
)
e1T1OutputStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1T1OutputStatusIndex.setStatus("current")
_E1T1OutputPortStatusV1_Type = DisplayString
_E1T1OutputPortStatusV1_Object = MibTableColumn
e1T1OutputPortStatusV1 = _E1T1OutputPortStatusV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 2),
    _E1T1OutputPortStatusV1_Type()
)
e1T1OutputPortStatusV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1T1OutputPortStatusV1.setStatus("current")
_E1T1OutputPQLValueV1_Type = TP5000PQLVALUE
_E1T1OutputPQLValueV1_Object = MibTableColumn
e1T1OutputPQLValueV1 = _E1T1OutputPQLValueV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 3),
    _E1T1OutputPQLValueV1_Type()
)
e1T1OutputPQLValueV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1T1OutputPQLValueV1.setStatus("current")
_E1T1OutputConfig_ObjectIdentity = ObjectIdentity
e1T1OutputConfig = _E1T1OutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2)
)
_E1T1OutputConfigTable_Object = MibTable
e1T1OutputConfigTable = _E1T1OutputConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    e1T1OutputConfigTable.setStatus("current")
_E1T1OutputConfigEntry_Object = MibTableRow
e1T1OutputConfigEntry = _E1T1OutputConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1)
)
e1T1OutputConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMME1T1", "e1T1OutputConfigIndex"),
)
if mibBuilder.loadTexts:
    e1T1OutputConfigEntry.setStatus("current")


class _E1T1OutputConfigIndex_Type(Integer32):
    """Custom type e1T1OutputConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_E1T1OutputConfigIndex_Type.__name__ = "Integer32"
_E1T1OutputConfigIndex_Object = MibTableColumn
e1T1OutputConfigIndex = _E1T1OutputConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 1),
    _E1T1OutputConfigIndex_Type()
)
e1T1OutputConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1T1OutputConfigIndex.setStatus("current")
_E1T1OutputStateV1_Type = PORTSTATETYPE
_E1T1OutputStateV1_Object = MibTableColumn
e1T1OutputStateV1 = _E1T1OutputStateV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 2),
    _E1T1OutputStateV1_Type()
)
e1T1OutputStateV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputStateV1.setStatus("current")
_E1T1OutputFrameTypeV1_Type = OUTPUTE1T1FRAMETYPE
_E1T1OutputFrameTypeV1_Object = MibTableColumn
e1T1OutputFrameTypeV1 = _E1T1OutputFrameTypeV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 3),
    _E1T1OutputFrameTypeV1_Type()
)
e1T1OutputFrameTypeV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputFrameTypeV1.setStatus("current")
_E1T1OutputCRCStateV1_Type = EnableValue
_E1T1OutputCRCStateV1_Object = MibTableColumn
e1T1OutputCRCStateV1 = _E1T1OutputCRCStateV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 4),
    _E1T1OutputCRCStateV1_Type()
)
e1T1OutputCRCStateV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputCRCStateV1.setStatus("current")
_E1T1OutputSSMStateV1_Type = EnableValue
_E1T1OutputSSMStateV1_Object = MibTableColumn
e1T1OutputSSMStateV1 = _E1T1OutputSSMStateV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 5),
    _E1T1OutputSSMStateV1_Type()
)
e1T1OutputSSMStateV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputSSMStateV1.setStatus("current")


class _E1T1OutputSSMBitV1_Type(Integer32):
    """Custom type e1T1OutputSSMBitV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_E1T1OutputSSMBitV1_Type.__name__ = "Integer32"
_E1T1OutputSSMBitV1_Object = MibTableColumn
e1T1OutputSSMBitV1 = _E1T1OutputSSMBitV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 6),
    _E1T1OutputSSMBitV1_Type()
)
e1T1OutputSSMBitV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputSSMBitV1.setStatus("current")
_E1T1OutputZeroSupprV1_Type = ONVALUETYPE
_E1T1OutputZeroSupprV1_Object = MibTableColumn
e1T1OutputZeroSupprV1 = _E1T1OutputZeroSupprV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 7),
    _E1T1OutputZeroSupprV1_Type()
)
e1T1OutputZeroSupprV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputZeroSupprV1.setStatus("current")
_E1T1OutputLengthV1_Type = Integer32
_E1T1OutputLengthV1_Object = MibTableColumn
e1T1OutputLengthV1 = _E1T1OutputLengthV1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 8),
    _E1T1OutputLengthV1_Type()
)
e1T1OutputLengthV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1T1OutputLengthV1.setStatus("current")
_E1T1Conformance_ObjectIdentity = ObjectIdentity
e1T1Conformance = _E1T1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3)
)
if mibBuilder.loadTexts:
    e1T1Conformance.setStatus("current")
_E1T1Compliances_ObjectIdentity = ObjectIdentity
e1T1Compliances = _E1T1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1)
)
_E1T1UocGroups_ObjectIdentity = ObjectIdentity
e1T1UocGroups = _E1T1UocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2)
)

# Managed Objects groups

e1T1InputStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 1)
)
e1T1InputStatusGroup.setObjects(
      *(("SYMME1T1", "e1T1InputPortStatusV1"),
        ("SYMME1T1", "e1T1InputPQLCurValueV1"))
)
if mibBuilder.loadTexts:
    e1T1InputStatusGroup.setStatus("current")

e11T1InputConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 2)
)
e11T1InputConfigGroup.setObjects(
      *(("SYMME1T1", "e1T1InputFrameTypeV1"),
        ("SYMME1T1", "e1T1InputCRCStateV1"),
        ("SYMME1T1", "e1T1InputSSMStateV1"),
        ("SYMME1T1", "e1T1InputSSMBitV1"),
        ("SYMME1T1", "e1T1InputPQLValueV1"),
        ("SYMME1T1", "eT1InputZeroSupprV1"))
)
if mibBuilder.loadTexts:
    e11T1InputConfigGroup.setStatus("current")

e11T1OutputStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 3)
)
e11T1OutputStatusGroup.setObjects(
      *(("SYMME1T1", "e1T1OutputPortStatusV1"),
        ("SYMME1T1", "e1T1OutputPQLValueV1"))
)
if mibBuilder.loadTexts:
    e11T1OutputStatusGroup.setStatus("current")

e11T1OutputConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 4)
)
e11T1OutputConfigGroup.setObjects(
      *(("SYMME1T1", "e1T1OutputStateV1"),
        ("SYMME1T1", "e1T1OutputFrameTypeV1"),
        ("SYMME1T1", "e1T1OutputCRCStateV1"),
        ("SYMME1T1", "e1T1OutputSSMStateV1"),
        ("SYMME1T1", "e1T1OutputSSMBitV1"),
        ("SYMME1T1", "e1T1OutputLengthV1"),
        ("SYMME1T1", "e1T1OutputZeroSupprV1"))
)
if mibBuilder.loadTexts:
    e11T1OutputConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

e1T1BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    e1T1BasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMME1T1",
    **{"TP5000PQLVALUE": TP5000PQLVALUE,
       "INPUTE1T1FRAMETYPE": INPUTE1T1FRAMETYPE,
       "PORTSTATETYPE": PORTSTATETYPE,
       "OUTPUTE1T1FRAMETYPE": OUTPUTE1T1FRAMETYPE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmE1T1": symmE1T1,
       "e1T1input": e1T1input,
       "inputE1T1Status": inputE1T1Status,
       "e1T1InputStatusTable": e1T1InputStatusTable,
       "e1T1InputStatusEntry": e1T1InputStatusEntry,
       "e1T1InputStatusIndex": e1T1InputStatusIndex,
       "e1T1InputPQLCurValueV1": e1T1InputPQLCurValueV1,
       "e1T1InputPortStatusV1": e1T1InputPortStatusV1,
       "e1T1InputConfig": e1T1InputConfig,
       "e1T1InputConfigTable": e1T1InputConfigTable,
       "e1T1InputConfigEntry": e1T1InputConfigEntry,
       "e1T1InputConfigIndex": e1T1InputConfigIndex,
       "e1T1InputFrameTypeV1": e1T1InputFrameTypeV1,
       "e1T1InputCRCStateV1": e1T1InputCRCStateV1,
       "e1T1InputSSMStateV1": e1T1InputSSMStateV1,
       "e1T1InputSSMBitV1": e1T1InputSSMBitV1,
       "e1T1InputPQLValueV1": e1T1InputPQLValueV1,
       "eT1InputZeroSupprV1": eT1InputZeroSupprV1,
       "e1T1Output": e1T1Output,
       "e1T1OutputStatus": e1T1OutputStatus,
       "e1T1OutputStatusTable": e1T1OutputStatusTable,
       "e1T1OutputStatusEntry": e1T1OutputStatusEntry,
       "e1T1OutputStatusIndex": e1T1OutputStatusIndex,
       "e1T1OutputPortStatusV1": e1T1OutputPortStatusV1,
       "e1T1OutputPQLValueV1": e1T1OutputPQLValueV1,
       "e1T1OutputConfig": e1T1OutputConfig,
       "e1T1OutputConfigTable": e1T1OutputConfigTable,
       "e1T1OutputConfigEntry": e1T1OutputConfigEntry,
       "e1T1OutputConfigIndex": e1T1OutputConfigIndex,
       "e1T1OutputStateV1": e1T1OutputStateV1,
       "e1T1OutputFrameTypeV1": e1T1OutputFrameTypeV1,
       "e1T1OutputCRCStateV1": e1T1OutputCRCStateV1,
       "e1T1OutputSSMStateV1": e1T1OutputSSMStateV1,
       "e1T1OutputSSMBitV1": e1T1OutputSSMBitV1,
       "e1T1OutputZeroSupprV1": e1T1OutputZeroSupprV1,
       "e1T1OutputLengthV1": e1T1OutputLengthV1,
       "e1T1Conformance": e1T1Conformance,
       "e1T1Compliances": e1T1Compliances,
       "e1T1BasicCompliance": e1T1BasicCompliance,
       "e1T1UocGroups": e1T1UocGroups,
       "e1T1InputStatusGroup": e1T1InputStatusGroup,
       "e11T1InputConfigGroup": e11T1InputConfigGroup,
       "e11T1OutputStatusGroup": e11T1OutputStatusGroup,
       "e11T1OutputConfigGroup": e11T1OutputConfigGroup}
)
