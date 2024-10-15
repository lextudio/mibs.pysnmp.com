# SNMP MIB module (DISMAN-EXPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-EXPRESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:15 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 mib_2,
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
    "mib-2",
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

dismanExpressionMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 90)
)
dismanExpressionMIB.setRevisions(
        ("2000-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysUpTimeInstance_ObjectIdentity = ObjectIdentity
sysUpTimeInstance = _SysUpTimeInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 3, 0)
)
_DismanExpressionMIBObjects_ObjectIdentity = ObjectIdentity
dismanExpressionMIBObjects = _DismanExpressionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1)
)
_ExpResource_ObjectIdentity = ObjectIdentity
expResource = _ExpResource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 1)
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
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 1),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 2),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 3),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 4),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 5),
    _ExpResourceDeltaWildcardInstanceResourceLacks_Type()
)
expResourceDeltaWildcardInstanceResourceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setUnits("instances")
_ExpDefine_ObjectIdentity = ObjectIdentity
expDefine = _ExpDefine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 2)
)
_ExpExpressionTable_Object = MibTable
expExpressionTable = _ExpExpressionTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    expExpressionTable.setStatus("current")
_ExpExpressionEntry_Object = MibTableRow
expExpressionEntry = _ExpExpressionEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1)
)
expExpressionEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
)
if mibBuilder.loadTexts:
    expExpressionEntry.setStatus("current")


class _ExpExpressionOwner_Type(SnmpAdminString):
    """Custom type expExpressionOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpExpressionOwner_Type.__name__ = "SnmpAdminString"
_ExpExpressionOwner_Object = MibTableColumn
expExpressionOwner = _ExpExpressionOwner_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 1),
    _ExpExpressionOwner_Type()
)
expExpressionOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expExpressionOwner.setStatus("current")


class _ExpExpressionName_Type(SnmpAdminString):
    """Custom type expExpressionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExpExpressionName_Type.__name__ = "SnmpAdminString"
_ExpExpressionName_Object = MibTableColumn
expExpressionName = _ExpExpressionName_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 2),
    _ExpExpressionName_Type()
)
expExpressionName.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 3),
    _ExpExpression_Type()
)
expExpression.setMaxAccess("read-create")
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
          ("unsigned32", 2))
    )


_ExpExpressionValueType_Type.__name__ = "Integer32"
_ExpExpressionValueType_Object = MibTableColumn
expExpressionValueType = _ExpExpressionValueType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 4),
    _ExpExpressionValueType_Type()
)
expExpressionValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionValueType.setStatus("current")


class _ExpExpressionComment_Type(SnmpAdminString):
    """Custom type expExpressionComment based on SnmpAdminString"""
    defaultHexValue = ""


_ExpExpressionComment_Object = MibTableColumn
expExpressionComment = _ExpExpressionComment_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 5),
    _ExpExpressionComment_Type()
)
expExpressionComment.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 6),
    _ExpExpressionDeltaInterval_Type()
)
expExpressionDeltaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setUnits("seconds")
_ExpExpressionPrefix_Type = ObjectIdentifier
_ExpExpressionPrefix_Object = MibTableColumn
expExpressionPrefix = _ExpExpressionPrefix_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 7),
    _ExpExpressionPrefix_Type()
)
expExpressionPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionPrefix.setStatus("current")
_ExpExpressionErrors_Type = Counter32
_ExpExpressionErrors_Object = MibTableColumn
expExpressionErrors = _ExpExpressionErrors_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 8),
    _ExpExpressionErrors_Type()
)
expExpressionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionErrors.setStatus("current")
_ExpExpressionEntryStatus_Type = RowStatus
_ExpExpressionEntryStatus_Object = MibTableColumn
expExpressionEntryStatus = _ExpExpressionEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 9),
    _ExpExpressionEntryStatus_Type()
)
expExpressionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionEntryStatus.setStatus("current")
_ExpErrorTable_Object = MibTable
expErrorTable = _ExpErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2)
)
if mibBuilder.loadTexts:
    expErrorTable.setStatus("current")
_ExpErrorEntry_Object = MibTableRow
expErrorEntry = _ExpErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1)
)
expErrorEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
)
if mibBuilder.loadTexts:
    expErrorEntry.setStatus("current")
_ExpErrorTime_Type = TimeStamp
_ExpErrorTime_Object = MibTableColumn
expErrorTime = _ExpErrorTime_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 1),
    _ExpErrorTime_Type()
)
expErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorTime.setStatus("current")
_ExpErrorIndex_Type = Integer32
_ExpErrorIndex_Object = MibTableColumn
expErrorIndex = _ExpErrorIndex_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 2),
    _ExpErrorIndex_Type()
)
expErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorIndex.setStatus("current")


class _ExpErrorCode_Type(Integer32):
    """Custom type expErrorCode based on Integer32"""
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


_ExpErrorCode_Type.__name__ = "Integer32"
_ExpErrorCode_Object = MibTableColumn
expErrorCode = _ExpErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 3),
    _ExpErrorCode_Type()
)
expErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorCode.setStatus("current")
_ExpErrorInstance_Type = ObjectIdentifier
_ExpErrorInstance_Object = MibTableColumn
expErrorInstance = _ExpErrorInstance_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 4),
    _ExpErrorInstance_Type()
)
expErrorInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorInstance.setStatus("current")
_ExpObjectTable_Object = MibTable
expObjectTable = _ExpObjectTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3)
)
if mibBuilder.loadTexts:
    expObjectTable.setStatus("current")
_ExpObjectEntry_Object = MibTableRow
expObjectEntry = _ExpObjectEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1)
)
expObjectEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
    (0, "DISMAN-EXPRESSION-MIB", "expObjectIndex"),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 1),
    _ExpObjectIndex_Type()
)
expObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expObjectIndex.setStatus("current")
_ExpObjectID_Type = ObjectIdentifier
_ExpObjectID_Object = MibTableColumn
expObjectID = _ExpObjectID_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 2),
    _ExpObjectID_Type()
)
expObjectID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectID.setStatus("current")


class _ExpObjectIDWildcard_Type(TruthValue):
    """Custom type expObjectIDWildcard based on TruthValue"""


_ExpObjectIDWildcard_Object = MibTableColumn
expObjectIDWildcard = _ExpObjectIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 3),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("changedValue", 3),
          ("deltaValue", 2))
    )


_ExpObjectSampleType_Type.__name__ = "Integer32"
_ExpObjectSampleType_Object = MibTableColumn
expObjectSampleType = _ExpObjectSampleType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 5),
    _ExpObjectDeltaDiscontinuityID_Type()
)
expObjectDeltaDiscontinuityID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDeltaDiscontinuityID.setStatus("current")


class _ExpObjectDiscontinuityIDWildcard_Type(TruthValue):
    """Custom type expObjectDiscontinuityIDWildcard based on TruthValue"""


_ExpObjectDiscontinuityIDWildcard_Object = MibTableColumn
expObjectDiscontinuityIDWildcard = _ExpObjectDiscontinuityIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 6),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dateAndTime", 3),
          ("timeStamp", 2),
          ("timeTicks", 1))
    )


_ExpObjectDiscontinuityIDType_Type.__name__ = "Integer32"
_ExpObjectDiscontinuityIDType_Object = MibTableColumn
expObjectDiscontinuityIDType = _ExpObjectDiscontinuityIDType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 7),
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
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 8),
    _ExpObjectConditional_Type()
)
expObjectConditional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditional.setStatus("current")


class _ExpObjectConditionalWildcard_Type(TruthValue):
    """Custom type expObjectConditionalWildcard based on TruthValue"""


_ExpObjectConditionalWildcard_Object = MibTableColumn
expObjectConditionalWildcard = _ExpObjectConditionalWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 9),
    _ExpObjectConditionalWildcard_Type()
)
expObjectConditionalWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditionalWildcard.setStatus("current")
_ExpObjectEntryStatus_Type = RowStatus
_ExpObjectEntryStatus_Object = MibTableColumn
expObjectEntryStatus = _ExpObjectEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 10),
    _ExpObjectEntryStatus_Type()
)
expObjectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectEntryStatus.setStatus("current")
_ExpValue_ObjectIdentity = ObjectIdentity
expValue = _ExpValue_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 3)
)
_ExpValueTable_Object = MibTable
expValueTable = _ExpValueTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1)
)
if mibBuilder.loadTexts:
    expValueTable.setStatus("current")
_ExpValueEntry_Object = MibTableRow
expValueEntry = _ExpValueEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1)
)
expValueEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
    (1, "DISMAN-EXPRESSION-MIB", "expValueInstance"),
)
if mibBuilder.loadTexts:
    expValueEntry.setStatus("current")
_ExpValueInstance_Type = ObjectIdentifier
_ExpValueInstance_Object = MibTableColumn
expValueInstance = _ExpValueInstance_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 1),
    _ExpValueInstance_Type()
)
expValueInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expValueInstance.setStatus("current")
_ExpValueCounter32Val_Type = Counter32
_ExpValueCounter32Val_Object = MibTableColumn
expValueCounter32Val = _ExpValueCounter32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 2),
    _ExpValueCounter32Val_Type()
)
expValueCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter32Val.setStatus("current")
_ExpValueUnsigned32Val_Type = Unsigned32
_ExpValueUnsigned32Val_Object = MibTableColumn
expValueUnsigned32Val = _ExpValueUnsigned32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 3),
    _ExpValueUnsigned32Val_Type()
)
expValueUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueUnsigned32Val.setStatus("current")
_ExpValueTimeTicksVal_Type = TimeTicks
_ExpValueTimeTicksVal_Object = MibTableColumn
expValueTimeTicksVal = _ExpValueTimeTicksVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 4),
    _ExpValueTimeTicksVal_Type()
)
expValueTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueTimeTicksVal.setStatus("current")
_ExpValueInteger32Val_Type = Integer32
_ExpValueInteger32Val_Object = MibTableColumn
expValueInteger32Val = _ExpValueInteger32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 5),
    _ExpValueInteger32Val_Type()
)
expValueInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueInteger32Val.setStatus("current")
_ExpValueIpAddressVal_Type = IpAddress
_ExpValueIpAddressVal_Object = MibTableColumn
expValueIpAddressVal = _ExpValueIpAddressVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 6),
    _ExpValueIpAddressVal_Type()
)
expValueIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueIpAddressVal.setStatus("current")


class _ExpValueOctetStringVal_Type(OctetString):
    """Custom type expValueOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_ExpValueOctetStringVal_Type.__name__ = "OctetString"
_ExpValueOctetStringVal_Object = MibTableColumn
expValueOctetStringVal = _ExpValueOctetStringVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 7),
    _ExpValueOctetStringVal_Type()
)
expValueOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOctetStringVal.setStatus("current")
_ExpValueOidVal_Type = ObjectIdentifier
_ExpValueOidVal_Object = MibTableColumn
expValueOidVal = _ExpValueOidVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 8),
    _ExpValueOidVal_Type()
)
expValueOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOidVal.setStatus("current")
_ExpValueCounter64Val_Type = Counter64
_ExpValueCounter64Val_Object = MibTableColumn
expValueCounter64Val = _ExpValueCounter64Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 9),
    _ExpValueCounter64Val_Type()
)
expValueCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter64Val.setStatus("current")
_DismanExpressionMIBConformance_ObjectIdentity = ObjectIdentity
dismanExpressionMIBConformance = _DismanExpressionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3)
)
_DismanExpressionMIBCompliances_ObjectIdentity = ObjectIdentity
dismanExpressionMIBCompliances = _DismanExpressionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3, 1)
)
_DismanExpressionMIBGroups_ObjectIdentity = ObjectIdentity
dismanExpressionMIBGroups = _DismanExpressionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3, 2)
)

# Managed Objects groups

dismanExpressionResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 1)
)
dismanExpressionResourceGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expResourceDeltaMinimum"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceMaximum"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstances"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstancesHigh"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceResourceLacks"))
)
if mibBuilder.loadTexts:
    dismanExpressionResourceGroup.setStatus("current")

dismanExpressionDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 2)
)
dismanExpressionDefinitionGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expExpression"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionValueType"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionComment"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionDeltaInterval"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionPrefix"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionErrors"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionEntryStatus"),
        ("DISMAN-EXPRESSION-MIB", "expErrorTime"),
        ("DISMAN-EXPRESSION-MIB", "expErrorIndex"),
        ("DISMAN-EXPRESSION-MIB", "expErrorCode"),
        ("DISMAN-EXPRESSION-MIB", "expErrorInstance"),
        ("DISMAN-EXPRESSION-MIB", "expObjectID"),
        ("DISMAN-EXPRESSION-MIB", "expObjectIDWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectSampleType"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDeltaDiscontinuityID"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDType"),
        ("DISMAN-EXPRESSION-MIB", "expObjectConditional"),
        ("DISMAN-EXPRESSION-MIB", "expObjectConditionalWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectEntryStatus"))
)
if mibBuilder.loadTexts:
    dismanExpressionDefinitionGroup.setStatus("current")

dismanExpressionValueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 3)
)
dismanExpressionValueGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expValueCounter32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueUnsigned32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueTimeTicksVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueInteger32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueIpAddressVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueOctetStringVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueOidVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueCounter64Val"))
)
if mibBuilder.loadTexts:
    dismanExpressionValueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dismanExpressionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 90, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dismanExpressionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-EXPRESSION-MIB",
    **{"sysUpTimeInstance": sysUpTimeInstance,
       "dismanExpressionMIB": dismanExpressionMIB,
       "dismanExpressionMIBObjects": dismanExpressionMIBObjects,
       "expResource": expResource,
       "expResourceDeltaMinimum": expResourceDeltaMinimum,
       "expResourceDeltaWildcardInstanceMaximum": expResourceDeltaWildcardInstanceMaximum,
       "expResourceDeltaWildcardInstances": expResourceDeltaWildcardInstances,
       "expResourceDeltaWildcardInstancesHigh": expResourceDeltaWildcardInstancesHigh,
       "expResourceDeltaWildcardInstanceResourceLacks": expResourceDeltaWildcardInstanceResourceLacks,
       "expDefine": expDefine,
       "expExpressionTable": expExpressionTable,
       "expExpressionEntry": expExpressionEntry,
       "expExpressionOwner": expExpressionOwner,
       "expExpressionName": expExpressionName,
       "expExpression": expExpression,
       "expExpressionValueType": expExpressionValueType,
       "expExpressionComment": expExpressionComment,
       "expExpressionDeltaInterval": expExpressionDeltaInterval,
       "expExpressionPrefix": expExpressionPrefix,
       "expExpressionErrors": expExpressionErrors,
       "expExpressionEntryStatus": expExpressionEntryStatus,
       "expErrorTable": expErrorTable,
       "expErrorEntry": expErrorEntry,
       "expErrorTime": expErrorTime,
       "expErrorIndex": expErrorIndex,
       "expErrorCode": expErrorCode,
       "expErrorInstance": expErrorInstance,
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
       "expObjectEntryStatus": expObjectEntryStatus,
       "expValue": expValue,
       "expValueTable": expValueTable,
       "expValueEntry": expValueEntry,
       "expValueInstance": expValueInstance,
       "expValueCounter32Val": expValueCounter32Val,
       "expValueUnsigned32Val": expValueUnsigned32Val,
       "expValueTimeTicksVal": expValueTimeTicksVal,
       "expValueInteger32Val": expValueInteger32Val,
       "expValueIpAddressVal": expValueIpAddressVal,
       "expValueOctetStringVal": expValueOctetStringVal,
       "expValueOidVal": expValueOidVal,
       "expValueCounter64Val": expValueCounter64Val,
       "dismanExpressionMIBConformance": dismanExpressionMIBConformance,
       "dismanExpressionMIBCompliances": dismanExpressionMIBCompliances,
       "dismanExpressionMIBCompliance": dismanExpressionMIBCompliance,
       "dismanExpressionMIBGroups": dismanExpressionMIBGroups,
       "dismanExpressionResourceGroup": dismanExpressionResourceGroup,
       "dismanExpressionDefinitionGroup": dismanExpressionDefinitionGroup,
       "dismanExpressionValueGroup": dismanExpressionValueGroup}
)
