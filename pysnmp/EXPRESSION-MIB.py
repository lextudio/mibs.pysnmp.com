# SNMP MIB module (EXPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXPRESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:13 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

expressionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22)
)
expressionMIB.setRevisions(
        ("2005-11-24 00:00",
         "1998-02-25 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ExpressionName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class ExpressionIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ExpressionIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_SysUpTimeInstance_ObjectIdentity = ObjectIdentity
sysUpTimeInstance = _SysUpTimeInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 3, 0)
)
_ExpressionMIBObjects_ObjectIdentity = ObjectIdentity
expressionMIBObjects = _ExpressionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1)
)
_ExpResource_ObjectIdentity = ObjectIdentity
expResource = _ExpResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1)
)


class _ExpResourceDeltaMinimum_Type(Integer32):
    """Custom type expResourceDeltaMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 600),
    )


_ExpResourceDeltaMinimum_Type.__name__ = "Integer32"
_ExpResourceDeltaMinimum_Object = MibScalar
expResourceDeltaMinimum = _ExpResourceDeltaMinimum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 1),
    _ExpResourceDeltaMinimum_Type()
)
expResourceDeltaMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expResourceDeltaMinimum.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaMinimum.setUnits("seconds")
_ExpResourceDeltaWildcardInstanceMaximum_Type = Unsigned32
_ExpResourceDeltaWildcardInstanceMaximum_Object = MibScalar
expResourceDeltaWildcardInstanceMaximum = _ExpResourceDeltaWildcardInstanceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 2),
    _ExpResourceDeltaWildcardInstanceMaximum_Type()
)
expResourceDeltaWildcardInstanceMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceMaximum.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceMaximum.setUnits("instances")
_ExpResourceDeltaWildcardInstances_Type = Gauge32
_ExpResourceDeltaWildcardInstances_Object = MibScalar
expResourceDeltaWildcardInstances = _ExpResourceDeltaWildcardInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 3),
    _ExpResourceDeltaWildcardInstances_Type()
)
expResourceDeltaWildcardInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstances.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstances.setUnits("instances")
_ExpResourceDeltaWildcardInstancesHigh_Type = Gauge32
_ExpResourceDeltaWildcardInstancesHigh_Object = MibScalar
expResourceDeltaWildcardInstancesHigh = _ExpResourceDeltaWildcardInstancesHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 4),
    _ExpResourceDeltaWildcardInstancesHigh_Type()
)
expResourceDeltaWildcardInstancesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstancesHigh.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstancesHigh.setUnits("instances")
_ExpResourceDeltaWildcardInstanceResourceLacks_Type = Counter32
_ExpResourceDeltaWildcardInstanceResourceLacks_Object = MibScalar
expResourceDeltaWildcardInstanceResourceLacks = _ExpResourceDeltaWildcardInstanceResourceLacks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 5),
    _ExpResourceDeltaWildcardInstanceResourceLacks_Type()
)
expResourceDeltaWildcardInstanceResourceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setUnits("instances")
_ExpNames_ObjectIdentity = ObjectIdentity
expNames = _ExpNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2)
)
_ExpNameLastChange_Type = TimeStamp
_ExpNameLastChange_Object = MibScalar
expNameLastChange = _ExpNameLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 1),
    _ExpNameLastChange_Type()
)
expNameLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expNameLastChange.setStatus("current")
_ExpNameHighestIndex_Type = ExpressionIndexOrZero
_ExpNameHighestIndex_Object = MibScalar
expNameHighestIndex = _ExpNameHighestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 2),
    _ExpNameHighestIndex_Type()
)
expNameHighestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expNameHighestIndex.setStatus("current")
_ExpNameTable_Object = MibTable
expNameTable = _ExpNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3)
)
if mibBuilder.loadTexts:
    expNameTable.setStatus("current")
_ExpNameEntry_Object = MibTableRow
expNameEntry = _ExpNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1)
)
expNameEntry.setIndexNames(
    (0, "EXPRESSION-MIB", "expName"),
)
if mibBuilder.loadTexts:
    expNameEntry.setStatus("current")
_ExpName_Type = ExpressionName
_ExpName_Object = MibTableColumn
expName = _ExpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 1),
    _ExpName_Type()
)
expName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expName.setStatus("current")
_ExpExpressionIndex_Type = ExpressionIndex
_ExpExpressionIndex_Object = MibTableColumn
expExpressionIndex = _ExpExpressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 2),
    _ExpExpressionIndex_Type()
)
expExpressionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionIndex.setStatus("current")
_ExpNameStatus_Type = RowStatus
_ExpNameStatus_Object = MibTableColumn
expNameStatus = _ExpNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 3),
    _ExpNameStatus_Type()
)
expNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expNameStatus.setStatus("current")
_ExpDefine_ObjectIdentity = ObjectIdentity
expDefine = _ExpDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3)
)
_ExpExpressionTable_Object = MibTable
expExpressionTable = _ExpExpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    expExpressionTable.setStatus("current")
_ExpExpressionEntry_Object = MibTableRow
expExpressionEntry = _ExpExpressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1)
)
expExpressionEntry.setIndexNames(
    (0, "EXPRESSION-MIB", "expExpressionIndex"),
)
if mibBuilder.loadTexts:
    expExpressionEntry.setStatus("current")
_ExpExpressionName_Type = ExpressionName
_ExpExpressionName_Object = MibTableColumn
expExpressionName = _ExpExpressionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 1),
    _ExpExpressionName_Type()
)
expExpressionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpressionName.setStatus("current")


class _ExpExpression_Type(OctetString):
    """Custom type expExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_ExpExpression_Type.__name__ = "OctetString"
_ExpExpression_Object = MibTableColumn
expExpression = _ExpExpression_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 2),
    _ExpExpression_Type()
)
expExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpression.setStatus("current")


class _ExpExpressionValueType_Type(Integer32):
    """Custom type expExpressionValueType based on Integer32"""
    defaultValue = 1

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
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("timeTicks", 3),
          ("unsignedOrGauge32", 2))
    )


_ExpExpressionValueType_Type.__name__ = "Integer32"
_ExpExpressionValueType_Object = MibTableColumn
expExpressionValueType = _ExpExpressionValueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 3),
    _ExpExpressionValueType_Type()
)
expExpressionValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpressionValueType.setStatus("current")
_ExpExpressionComment_Type = DisplayString
_ExpExpressionComment_Object = MibTableColumn
expExpressionComment = _ExpExpressionComment_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 4),
    _ExpExpressionComment_Type()
)
expExpressionComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpressionComment.setStatus("current")


class _ExpExpressionDeltaInterval_Type(Integer32):
    """Custom type expExpressionDeltaInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ExpExpressionDeltaInterval_Type.__name__ = "Integer32"
_ExpExpressionDeltaInterval_Object = MibTableColumn
expExpressionDeltaInterval = _ExpExpressionDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 5),
    _ExpExpressionDeltaInterval_Type()
)
expExpressionDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setUnits("seconds")
_ExpExpressionPrefix_Type = ObjectIdentifier
_ExpExpressionPrefix_Object = MibTableColumn
expExpressionPrefix = _ExpExpressionPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 6),
    _ExpExpressionPrefix_Type()
)
expExpressionPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionPrefix.setStatus("current")
_ExpExpressionErrors_Type = Counter32
_ExpExpressionErrors_Object = MibTableColumn
expExpressionErrors = _ExpExpressionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 7),
    _ExpExpressionErrors_Type()
)
expExpressionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionErrors.setStatus("current")
_ExpExpressionErrorTime_Type = TimeStamp
_ExpExpressionErrorTime_Object = MibTableColumn
expExpressionErrorTime = _ExpExpressionErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 8),
    _ExpExpressionErrorTime_Type()
)
expExpressionErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionErrorTime.setStatus("current")
_ExpExpressionErrorIndex_Type = Integer32
_ExpExpressionErrorIndex_Object = MibTableColumn
expExpressionErrorIndex = _ExpExpressionErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 9),
    _ExpExpressionErrorIndex_Type()
)
expExpressionErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionErrorIndex.setStatus("current")


class _ExpExpressionError_Type(Integer32):
    """Custom type expExpressionError based on Integer32"""
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
        *(("deltaTooShort", 9),
          ("divideByZero", 11),
          ("invalidOperandType", 5),
          ("invalidSyntax", 1),
          ("recursion", 8),
          ("resourceUnavailable", 10),
          ("tooManyWildcardValues", 7),
          ("undefinedObjectIndex", 2),
          ("unmatchedParenthesis", 6),
          ("unrecognizedFunction", 4),
          ("unrecognizedOperator", 3))
    )


_ExpExpressionError_Type.__name__ = "Integer32"
_ExpExpressionError_Object = MibTableColumn
expExpressionError = _ExpExpressionError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 10),
    _ExpExpressionError_Type()
)
expExpressionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionError.setStatus("current")
_ExpExpressionInstance_Type = ObjectIdentifier
_ExpExpressionInstance_Object = MibTableColumn
expExpressionInstance = _ExpExpressionInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 11),
    _ExpExpressionInstance_Type()
)
expExpressionInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionInstance.setStatus("current")


class _ExpExpressionOwner_Type(DisplayString):
    """Custom type expExpressionOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExpExpressionOwner_Type.__name__ = "DisplayString"
_ExpExpressionOwner_Object = MibTableColumn
expExpressionOwner = _ExpExpressionOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 12),
    _ExpExpressionOwner_Type()
)
expExpressionOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expExpressionOwner.setStatus("current")
_ExpObjectTable_Object = MibTable
expObjectTable = _ExpObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2)
)
if mibBuilder.loadTexts:
    expObjectTable.setStatus("current")
_ExpObjectEntry_Object = MibTableRow
expObjectEntry = _ExpObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1)
)
expObjectEntry.setIndexNames(
    (0, "EXPRESSION-MIB", "expExpressionIndex"),
    (0, "EXPRESSION-MIB", "expObjectIndex"),
)
if mibBuilder.loadTexts:
    expObjectEntry.setStatus("current")


class _ExpObjectIndex_Type(Unsigned32):
    """Custom type expObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExpObjectIndex_Type.__name__ = "Unsigned32"
_ExpObjectIndex_Object = MibTableColumn
expObjectIndex = _ExpObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 1),
    _ExpObjectIndex_Type()
)
expObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expObjectIndex.setStatus("current")
_ExpObjectID_Type = ObjectIdentifier
_ExpObjectID_Object = MibTableColumn
expObjectID = _ExpObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 2),
    _ExpObjectID_Type()
)
expObjectID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectID.setStatus("current")


class _ExpObjectIDWildcard_Type(TruthValue):
    """Custom type expObjectIDWildcard based on TruthValue"""


_ExpObjectIDWildcard_Object = MibTableColumn
expObjectIDWildcard = _ExpObjectIDWildcard_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 3),
    _ExpObjectIDWildcard_Type()
)
expObjectIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectIDWildcard.setStatus("current")


class _ExpObjectSampleType_Type(Integer32):
    """Custom type expObjectSampleType based on Integer32"""
    defaultValue = 1

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


_ExpObjectSampleType_Type.__name__ = "Integer32"
_ExpObjectSampleType_Object = MibTableColumn
expObjectSampleType = _ExpObjectSampleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 4),
    _ExpObjectSampleType_Type()
)
expObjectSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectSampleType.setStatus("current")


class _ExpObjectDeltaDiscontinuityID_Type(ObjectIdentifier):
    """Custom type expObjectDeltaDiscontinuityID based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 1, 3, 0)


_ExpObjectDeltaDiscontinuityID_Object = MibTableColumn
expObjectDeltaDiscontinuityID = _ExpObjectDeltaDiscontinuityID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 5),
    _ExpObjectDeltaDiscontinuityID_Type()
)
expObjectDeltaDiscontinuityID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDeltaDiscontinuityID.setStatus("current")


class _ExpObjectDiscontinuityIDWildcard_Type(TruthValue):
    """Custom type expObjectDiscontinuityIDWildcard based on TruthValue"""


_ExpObjectDiscontinuityIDWildcard_Object = MibTableColumn
expObjectDiscontinuityIDWildcard = _ExpObjectDiscontinuityIDWildcard_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 6),
    _ExpObjectDiscontinuityIDWildcard_Type()
)
expObjectDiscontinuityIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDWildcard.setStatus("current")


class _ExpObjectDiscontinuityIDType_Type(Integer32):
    """Custom type expObjectDiscontinuityIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timeStamp", 2),
          ("timeTicks", 1))
    )


_ExpObjectDiscontinuityIDType_Type.__name__ = "Integer32"
_ExpObjectDiscontinuityIDType_Object = MibTableColumn
expObjectDiscontinuityIDType = _ExpObjectDiscontinuityIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 7),
    _ExpObjectDiscontinuityIDType_Type()
)
expObjectDiscontinuityIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDType.setStatus("current")


class _ExpObjectConditional_Type(ObjectIdentifier):
    """Custom type expObjectConditional based on ObjectIdentifier"""
    defaultValue = (0, 0)


_ExpObjectConditional_Object = MibTableColumn
expObjectConditional = _ExpObjectConditional_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 8),
    _ExpObjectConditional_Type()
)
expObjectConditional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditional.setStatus("current")


class _ExpObjectConditionalWildcard_Type(TruthValue):
    """Custom type expObjectConditionalWildcard based on TruthValue"""


_ExpObjectConditionalWildcard_Object = MibTableColumn
expObjectConditionalWildcard = _ExpObjectConditionalWildcard_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 9),
    _ExpObjectConditionalWildcard_Type()
)
expObjectConditionalWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditionalWildcard.setStatus("current")
_ExpObjectStatus_Type = RowStatus
_ExpObjectStatus_Object = MibTableColumn
expObjectStatus = _ExpObjectStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 10),
    _ExpObjectStatus_Type()
)
expObjectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectStatus.setStatus("current")
_ExpValue_ObjectIdentity = ObjectIdentity
expValue = _ExpValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4)
)
_ExpValueTable_Object = MibTable
expValueTable = _ExpValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    expValueTable.setStatus("current")
_ExpValueEntry_Object = MibTableRow
expValueEntry = _ExpValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1)
)
expValueEntry.setIndexNames(
    (0, "EXPRESSION-MIB", "expExpressionIndex"),
    (0, "EXPRESSION-MIB", "expValueInstance"),
)
if mibBuilder.loadTexts:
    expValueEntry.setStatus("current")
_ExpValueInstance_Type = ObjectIdentifier
_ExpValueInstance_Object = MibTableColumn
expValueInstance = _ExpValueInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 1),
    _ExpValueInstance_Type()
)
expValueInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expValueInstance.setStatus("current")
_ExpValueCounter32Val_Type = Counter32
_ExpValueCounter32Val_Object = MibTableColumn
expValueCounter32Val = _ExpValueCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 2),
    _ExpValueCounter32Val_Type()
)
expValueCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter32Val.setStatus("current")
_ExpValueUnsigned32Val_Type = Unsigned32
_ExpValueUnsigned32Val_Object = MibTableColumn
expValueUnsigned32Val = _ExpValueUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 3),
    _ExpValueUnsigned32Val_Type()
)
expValueUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueUnsigned32Val.setStatus("current")
_ExpValueInteger32Val_Type = Integer32
_ExpValueInteger32Val_Object = MibTableColumn
expValueInteger32Val = _ExpValueInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 4),
    _ExpValueInteger32Val_Type()
)
expValueInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueInteger32Val.setStatus("current")
_ExpValueIpAddressVal_Type = IpAddress
_ExpValueIpAddressVal_Object = MibTableColumn
expValueIpAddressVal = _ExpValueIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 5),
    _ExpValueIpAddressVal_Type()
)
expValueIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueIpAddressVal.setStatus("current")


class _ExpValueOctetStringVal_Type(OctetString):
    """Custom type expValueOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ExpValueOctetStringVal_Type.__name__ = "OctetString"
_ExpValueOctetStringVal_Object = MibTableColumn
expValueOctetStringVal = _ExpValueOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 6),
    _ExpValueOctetStringVal_Type()
)
expValueOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOctetStringVal.setStatus("current")
_ExpValueOidVal_Type = ObjectIdentifier
_ExpValueOidVal_Object = MibTableColumn
expValueOidVal = _ExpValueOidVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 7),
    _ExpValueOidVal_Type()
)
expValueOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOidVal.setStatus("current")
_ExpValueCounter64Val_Type = Counter64
_ExpValueCounter64Val_Object = MibTableColumn
expValueCounter64Val = _ExpValueCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 8),
    _ExpValueCounter64Val_Type()
)
expValueCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter64Val.setStatus("current")
_ExpressionMIBConformance_ObjectIdentity = ObjectIdentity
expressionMIBConformance = _ExpressionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3)
)
_ExpressionMIBCompliances_ObjectIdentity = ObjectIdentity
expressionMIBCompliances = _ExpressionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 1)
)
_ExpressionMIBGroups_ObjectIdentity = ObjectIdentity
expressionMIBGroups = _ExpressionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2)
)

# Managed Objects groups

expressionResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 1)
)
expressionResourceGroup.setObjects(
      *(("EXPRESSION-MIB", "expResourceDeltaMinimum"),
        ("EXPRESSION-MIB", "expResourceDeltaWildcardInstanceMaximum"),
        ("EXPRESSION-MIB", "expResourceDeltaWildcardInstances"),
        ("EXPRESSION-MIB", "expResourceDeltaWildcardInstancesHigh"),
        ("EXPRESSION-MIB", "expResourceDeltaWildcardInstanceResourceLacks"))
)
if mibBuilder.loadTexts:
    expressionResourceGroup.setStatus("current")

expressionDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 2)
)
expressionDefinitionGroup.setObjects(
      *(("EXPRESSION-MIB", "expNameLastChange"),
        ("EXPRESSION-MIB", "expNameHighestIndex"),
        ("EXPRESSION-MIB", "expExpressionIndex"),
        ("EXPRESSION-MIB", "expNameStatus"),
        ("EXPRESSION-MIB", "expExpressionName"),
        ("EXPRESSION-MIB", "expExpression"),
        ("EXPRESSION-MIB", "expExpressionValueType"),
        ("EXPRESSION-MIB", "expExpressionComment"),
        ("EXPRESSION-MIB", "expExpressionDeltaInterval"),
        ("EXPRESSION-MIB", "expExpressionPrefix"),
        ("EXPRESSION-MIB", "expExpressionErrors"),
        ("EXPRESSION-MIB", "expExpressionErrorTime"),
        ("EXPRESSION-MIB", "expExpressionErrorIndex"),
        ("EXPRESSION-MIB", "expExpressionError"),
        ("EXPRESSION-MIB", "expExpressionInstance"),
        ("EXPRESSION-MIB", "expExpressionOwner"),
        ("EXPRESSION-MIB", "expObjectID"),
        ("EXPRESSION-MIB", "expObjectIDWildcard"),
        ("EXPRESSION-MIB", "expObjectSampleType"),
        ("EXPRESSION-MIB", "expObjectDeltaDiscontinuityID"),
        ("EXPRESSION-MIB", "expObjectDiscontinuityIDWildcard"),
        ("EXPRESSION-MIB", "expObjectDiscontinuityIDType"),
        ("EXPRESSION-MIB", "expObjectConditional"),
        ("EXPRESSION-MIB", "expObjectConditionalWildcard"),
        ("EXPRESSION-MIB", "expObjectStatus"))
)
if mibBuilder.loadTexts:
    expressionDefinitionGroup.setStatus("current")

expressionValueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 3)
)
expressionValueGroup.setObjects(
      *(("EXPRESSION-MIB", "expValueCounter32Val"),
        ("EXPRESSION-MIB", "expValueUnsigned32Val"),
        ("EXPRESSION-MIB", "expValueInteger32Val"),
        ("EXPRESSION-MIB", "expValueIpAddressVal"),
        ("EXPRESSION-MIB", "expValueOctetStringVal"),
        ("EXPRESSION-MIB", "expValueOidVal"),
        ("EXPRESSION-MIB", "expValueCounter64Val"))
)
if mibBuilder.loadTexts:
    expressionValueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

expressionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    expressionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXPRESSION-MIB",
    **{"ExpressionName": ExpressionName,
       "ExpressionIndex": ExpressionIndex,
       "ExpressionIndexOrZero": ExpressionIndexOrZero,
       "sysUpTimeInstance": sysUpTimeInstance,
       "expressionMIB": expressionMIB,
       "expressionMIBObjects": expressionMIBObjects,
       "expResource": expResource,
       "expResourceDeltaMinimum": expResourceDeltaMinimum,
       "expResourceDeltaWildcardInstanceMaximum": expResourceDeltaWildcardInstanceMaximum,
       "expResourceDeltaWildcardInstances": expResourceDeltaWildcardInstances,
       "expResourceDeltaWildcardInstancesHigh": expResourceDeltaWildcardInstancesHigh,
       "expResourceDeltaWildcardInstanceResourceLacks": expResourceDeltaWildcardInstanceResourceLacks,
       "expNames": expNames,
       "expNameLastChange": expNameLastChange,
       "expNameHighestIndex": expNameHighestIndex,
       "expNameTable": expNameTable,
       "expNameEntry": expNameEntry,
       "expName": expName,
       "expExpressionIndex": expExpressionIndex,
       "expNameStatus": expNameStatus,
       "expDefine": expDefine,
       "expExpressionTable": expExpressionTable,
       "expExpressionEntry": expExpressionEntry,
       "expExpressionName": expExpressionName,
       "expExpression": expExpression,
       "expExpressionValueType": expExpressionValueType,
       "expExpressionComment": expExpressionComment,
       "expExpressionDeltaInterval": expExpressionDeltaInterval,
       "expExpressionPrefix": expExpressionPrefix,
       "expExpressionErrors": expExpressionErrors,
       "expExpressionErrorTime": expExpressionErrorTime,
       "expExpressionErrorIndex": expExpressionErrorIndex,
       "expExpressionError": expExpressionError,
       "expExpressionInstance": expExpressionInstance,
       "expExpressionOwner": expExpressionOwner,
       "expObjectTable": expObjectTable,
       "expObjectEntry": expObjectEntry,
       "expObjectIndex": expObjectIndex,
       "expObjectID": expObjectID,
       "expObjectIDWildcard": expObjectIDWildcard,
       "expObjectSampleType": expObjectSampleType,
       "expObjectDeltaDiscontinuityID": expObjectDeltaDiscontinuityID,
       "expObjectDiscontinuityIDWildcard": expObjectDiscontinuityIDWildcard,
       "expObjectDiscontinuityIDType": expObjectDiscontinuityIDType,
       "expObjectConditional": expObjectConditional,
       "expObjectConditionalWildcard": expObjectConditionalWildcard,
       "expObjectStatus": expObjectStatus,
       "expValue": expValue,
       "expValueTable": expValueTable,
       "expValueEntry": expValueEntry,
       "expValueInstance": expValueInstance,
       "expValueCounter32Val": expValueCounter32Val,
       "expValueUnsigned32Val": expValueUnsigned32Val,
       "expValueInteger32Val": expValueInteger32Val,
       "expValueIpAddressVal": expValueIpAddressVal,
       "expValueOctetStringVal": expValueOctetStringVal,
       "expValueOidVal": expValueOidVal,
       "expValueCounter64Val": expValueCounter64Val,
       "expressionMIBConformance": expressionMIBConformance,
       "expressionMIBCompliances": expressionMIBCompliances,
       "expressionMIBCompliance": expressionMIBCompliance,
       "expressionMIBGroups": expressionMIBGroups,
       "expressionResourceGroup": expressionResourceGroup,
       "expressionDefinitionGroup": expressionDefinitionGroup,
       "expressionValueGroup": expressionValueGroup}
)
