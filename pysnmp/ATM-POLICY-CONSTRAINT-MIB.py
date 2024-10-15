# SNMP MIB module (ATM-POLICY-CONSTRAINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-POLICY-CONSTRAINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:58 2024
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmPolicyConstraintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1)
)
atmPolicyConstraintMIB.setRevisions(
        ("2003-07-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NetworkEntityNetworkServiceCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )



class ResourcePartitionNetworkServiceCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PolicyConstraintIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PolicyConstraintPolicyIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class PolicyIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PolicyOperator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mustAvoid", 2),
          ("requires", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSignalling_ObjectIdentity = ObjectIdentity
atmfSignalling = _AtmfSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9)
)
_AtmfPolicyConstraint_ObjectIdentity = ObjectIdentity
atmfPolicyConstraint = _AtmfPolicyConstraint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5)
)
_PolicyConstraintMIBObjects_ObjectIdentity = ObjectIdentity
policyConstraintMIBObjects = _PolicyConstraintMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1)
)
_PolicyConstraintBaseGroup_ObjectIdentity = ObjectIdentity
policyConstraintBaseGroup = _PolicyConstraintBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1)
)


class _PolicyConstraintMaximum_Type(Integer32):
    """Custom type policyConstraintMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyConstraintMaximum_Type.__name__ = "Integer32"
_PolicyConstraintMaximum_Object = MibScalar
policyConstraintMaximum = _PolicyConstraintMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 1),
    _PolicyConstraintMaximum_Type()
)
policyConstraintMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyConstraintMaximum.setStatus("current")


class _PolicyMaximum_Type(Integer32):
    """Custom type policyMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyMaximum_Type.__name__ = "Integer32"
_PolicyMaximum_Object = MibScalar
policyMaximum = _PolicyMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 2),
    _PolicyMaximum_Type()
)
policyMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMaximum.setStatus("current")


class _PolicyNeNSCListMaximum_Type(Integer32):
    """Custom type policyNeNSCListMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyNeNSCListMaximum_Type.__name__ = "Integer32"
_PolicyNeNSCListMaximum_Object = MibScalar
policyNeNSCListMaximum = _PolicyNeNSCListMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 3),
    _PolicyNeNSCListMaximum_Type()
)
policyNeNSCListMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyNeNSCListMaximum.setStatus("current")


class _PolicyRpNSCListMaximum_Type(Integer32):
    """Custom type policyRpNSCListMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyRpNSCListMaximum_Type.__name__ = "Integer32"
_PolicyRpNSCListMaximum_Object = MibScalar
policyRpNSCListMaximum = _PolicyRpNSCListMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 4),
    _PolicyRpNSCListMaximum_Type()
)
policyRpNSCListMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRpNSCListMaximum.setStatus("current")
_PolicyConstraintGroup_ObjectIdentity = ObjectIdentity
policyConstraintGroup = _PolicyConstraintGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2)
)
_PolicyNextPolicyConstraintIndex_Type = PolicyConstraintIndex
_PolicyNextPolicyConstraintIndex_Object = MibScalar
policyNextPolicyConstraintIndex = _PolicyNextPolicyConstraintIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 1),
    _PolicyNextPolicyConstraintIndex_Type()
)
policyNextPolicyConstraintIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyNextPolicyConstraintIndex.setStatus("current")
_PolicyConstraintTable_Object = MibTable
policyConstraintTable = _PolicyConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    policyConstraintTable.setStatus("current")
_PolicyConstraintEntry_Object = MibTableRow
policyConstraintEntry = _PolicyConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1)
)
policyConstraintEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"),
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintPolicyIndex"),
)
if mibBuilder.loadTexts:
    policyConstraintEntry.setStatus("current")
_PolicyConstraintIndex_Type = PolicyConstraintIndex
_PolicyConstraintIndex_Object = MibTableColumn
policyConstraintIndex = _PolicyConstraintIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 1),
    _PolicyConstraintIndex_Type()
)
policyConstraintIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyConstraintIndex.setStatus("current")
_PolicyConstraintPolicyIndex_Type = PolicyConstraintPolicyIndex
_PolicyConstraintPolicyIndex_Object = MibTableColumn
policyConstraintPolicyIndex = _PolicyConstraintPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 2),
    _PolicyConstraintPolicyIndex_Type()
)
policyConstraintPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyConstraintPolicyIndex.setStatus("current")
_PolicyIndex_Type = PolicyIndex
_PolicyIndex_Object = MibTableColumn
policyIndex = _PolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 3),
    _PolicyIndex_Type()
)
policyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyIndex.setStatus("current")
_PolicyConstraintRowStatus_Type = RowStatus
_PolicyConstraintRowStatus_Object = MibTableColumn
policyConstraintRowStatus = _PolicyConstraintRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 4),
    _PolicyConstraintRowStatus_Type()
)
policyConstraintRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyConstraintRowStatus.setStatus("current")
_PolicyConstraintNameTable_Object = MibTable
policyConstraintNameTable = _PolicyConstraintNameTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    policyConstraintNameTable.setStatus("current")
_PolicyConstraintNameEntry_Object = MibTableRow
policyConstraintNameEntry = _PolicyConstraintNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1)
)
policyConstraintNameEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"),
)
if mibBuilder.loadTexts:
    policyConstraintNameEntry.setStatus("current")
_PolicyConstraintName_Type = DisplayString
_PolicyConstraintName_Object = MibTableColumn
policyConstraintName = _PolicyConstraintName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1, 1),
    _PolicyConstraintName_Type()
)
policyConstraintName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyConstraintName.setStatus("current")
_PolicyConstraintNameRowStatus_Type = RowStatus
_PolicyConstraintNameRowStatus_Object = MibTableColumn
policyConstraintNameRowStatus = _PolicyConstraintNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1, 2),
    _PolicyConstraintNameRowStatus_Type()
)
policyConstraintNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyConstraintNameRowStatus.setStatus("current")
_PolicyGroup_ObjectIdentity = ObjectIdentity
policyGroup = _PolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3)
)
_PolicyNextPolicyIndex_Type = PolicyIndex
_PolicyNextPolicyIndex_Object = MibScalar
policyNextPolicyIndex = _PolicyNextPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 1),
    _PolicyNextPolicyIndex_Type()
)
policyNextPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyNextPolicyIndex.setStatus("current")
_PolicyTable_Object = MibTable
policyTable = _PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    policyTable.setStatus("current")
_PolicyEntry_Object = MibTableRow
policyEntry = _PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1)
)
policyEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"),
)
if mibBuilder.loadTexts:
    policyEntry.setStatus("current")
_PolicyName_Type = DisplayString
_PolicyName_Object = MibTableColumn
policyName = _PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 1),
    _PolicyName_Type()
)
policyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyName.setStatus("current")


class _RequireNeNscOperator_Type(Integer32):
    """Custom type requireNeNscOperator based on Integer32"""
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
        *(("logicalAND", 2),
          ("logicalOR", 3),
          ("noop", 1))
    )


_RequireNeNscOperator_Type.__name__ = "Integer32"
_RequireNeNscOperator_Object = MibTableColumn
requireNeNscOperator = _RequireNeNscOperator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 2),
    _RequireNeNscOperator_Type()
)
requireNeNscOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requireNeNscOperator.setStatus("current")


class _RequireRpNscOperator_Type(Integer32):
    """Custom type requireRpNscOperator based on Integer32"""
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
        *(("logicalAND", 2),
          ("logicalOR", 3),
          ("noop", 1))
    )


_RequireRpNscOperator_Type.__name__ = "Integer32"
_RequireRpNscOperator_Object = MibTableColumn
requireRpNscOperator = _RequireRpNscOperator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 3),
    _RequireRpNscOperator_Type()
)
requireRpNscOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requireRpNscOperator.setStatus("current")


class _MustAvoidNeNscOperator_Type(Integer32):
    """Custom type mustAvoidNeNscOperator based on Integer32"""
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
        *(("logicalAND", 2),
          ("logicalOR", 3),
          ("noop", 1))
    )


_MustAvoidNeNscOperator_Type.__name__ = "Integer32"
_MustAvoidNeNscOperator_Object = MibTableColumn
mustAvoidNeNscOperator = _MustAvoidNeNscOperator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 4),
    _MustAvoidNeNscOperator_Type()
)
mustAvoidNeNscOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mustAvoidNeNscOperator.setStatus("current")
_PolicyRowStatus_Type = RowStatus
_PolicyRowStatus_Object = MibTableColumn
policyRowStatus = _PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 5),
    _PolicyRowStatus_Type()
)
policyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRowStatus.setStatus("current")
_PolicyNeNscTable_Object = MibTable
policyNeNscTable = _PolicyNeNscTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    policyNeNscTable.setStatus("current")
_PolicyNeNscEntry_Object = MibTableRow
policyNeNscEntry = _PolicyNeNscEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1)
)
policyNeNscEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"),
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyOperator"),
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyNeNscIndex"),
)
if mibBuilder.loadTexts:
    policyNeNscEntry.setStatus("current")


class _PolicyNeNscIndex_Type(Integer32):
    """Custom type policyNeNscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PolicyNeNscIndex_Type.__name__ = "Integer32"
_PolicyNeNscIndex_Object = MibTableColumn
policyNeNscIndex = _PolicyNeNscIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 1),
    _PolicyNeNscIndex_Type()
)
policyNeNscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyNeNscIndex.setStatus("current")
_PolicyOperator_Type = PolicyOperator
_PolicyOperator_Object = MibTableColumn
policyOperator = _PolicyOperator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 2),
    _PolicyOperator_Type()
)
policyOperator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyOperator.setStatus("current")
_PolicyNeNsc_Type = NetworkEntityNetworkServiceCategory
_PolicyNeNsc_Object = MibTableColumn
policyNeNsc = _PolicyNeNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 3),
    _PolicyNeNsc_Type()
)
policyNeNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyNeNsc.setStatus("current")
_PolicyNeNscRowStatus_Type = RowStatus
_PolicyNeNscRowStatus_Object = MibTableColumn
policyNeNscRowStatus = _PolicyNeNscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 4),
    _PolicyNeNscRowStatus_Type()
)
policyNeNscRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyNeNscRowStatus.setStatus("current")
_PolicyRpNscTable_Object = MibTable
policyRpNscTable = _PolicyRpNscTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    policyRpNscTable.setStatus("current")
_PolicyRpNscEntry_Object = MibTableRow
policyRpNscEntry = _PolicyRpNscEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1)
)
policyRpNscEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"),
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyRpNscIndex"),
)
if mibBuilder.loadTexts:
    policyRpNscEntry.setStatus("current")


class _PolicyRpNscIndex_Type(Integer32):
    """Custom type policyRpNscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PolicyRpNscIndex_Type.__name__ = "Integer32"
_PolicyRpNscIndex_Object = MibTableColumn
policyRpNscIndex = _PolicyRpNscIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 1),
    _PolicyRpNscIndex_Type()
)
policyRpNscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyRpNscIndex.setStatus("current")
_PolicyRpNsc_Type = ResourcePartitionNetworkServiceCategory
_PolicyRpNsc_Object = MibTableColumn
policyRpNsc = _PolicyRpNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 2),
    _PolicyRpNsc_Type()
)
policyRpNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRpNsc.setStatus("current")
_PolicyRpNscRowStatus_Type = RowStatus
_PolicyRpNscRowStatus_Object = MibTableColumn
policyRpNscRowStatus = _PolicyRpNscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 3),
    _PolicyRpNscRowStatus_Type()
)
policyRpNscRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRpNscRowStatus.setStatus("current")
_PolicyReferenceTable_Object = MibTable
policyReferenceTable = _PolicyReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    policyReferenceTable.setStatus("current")
_PolicyReferenceEntry_Object = MibTableRow
policyReferenceEntry = _PolicyReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5, 1)
)
policyReferenceEntry.setIndexNames(
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"),
    (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"),
)
if mibBuilder.loadTexts:
    policyReferenceEntry.setStatus("current")
_PolicyReferencePCIndex_Type = PolicyConstraintIndex
_PolicyReferencePCIndex_Object = MibTableColumn
policyReferencePCIndex = _PolicyReferencePCIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5, 1, 1),
    _PolicyReferencePCIndex_Type()
)
policyReferencePCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyReferencePCIndex.setStatus("current")
_PolicyConstraintMIBConformance_ObjectIdentity = ObjectIdentity
policyConstraintMIBConformance = _PolicyConstraintMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4)
)
_PolicyConstraintMIBCompliances_ObjectIdentity = ObjectIdentity
policyConstraintMIBCompliances = _PolicyConstraintMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 1)
)
_PolicyConstraintMIBGroups_ObjectIdentity = ObjectIdentity
policyConstraintMIBGroups = _PolicyConstraintMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2)
)

# Managed Objects groups

policyConstraintMIBMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2, 1)
)
policyConstraintMIBMandatoryGroup.setObjects(
      *(("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintMaximum"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyMaximum"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNSCListMaximum"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNSCListMaximum"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyIndex"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintRowStatus"),
        ("ATM-POLICY-CONSTRAINT-MIB", "requireNeNscOperator"),
        ("ATM-POLICY-CONSTRAINT-MIB", "requireRpNscOperator"),
        ("ATM-POLICY-CONSTRAINT-MIB", "mustAvoidNeNscOperator"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyRowStatus"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNsc"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNscRowStatus"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNsc"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNscRowStatus"))
)
if mibBuilder.loadTexts:
    policyConstraintMIBMandatoryGroup.setStatus("current")

policyConstraintMIBOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2, 2)
)
policyConstraintMIBOptionalGroup.setObjects(
      *(("ATM-POLICY-CONSTRAINT-MIB", "policyNextPolicyConstraintIndex"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintName"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintNameRowStatus"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyNextPolicyIndex"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyName"),
        ("ATM-POLICY-CONSTRAINT-MIB", "policyReferencePCIndex"))
)
if mibBuilder.loadTexts:
    policyConstraintMIBOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

policyConstraintMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    policyConstraintMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-POLICY-CONSTRAINT-MIB",
    **{"NetworkEntityNetworkServiceCategory": NetworkEntityNetworkServiceCategory,
       "ResourcePartitionNetworkServiceCategory": ResourcePartitionNetworkServiceCategory,
       "PolicyConstraintIndex": PolicyConstraintIndex,
       "PolicyConstraintPolicyIndex": PolicyConstraintPolicyIndex,
       "PolicyIndex": PolicyIndex,
       "PolicyOperator": PolicyOperator,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSignalling": atmfSignalling,
       "atmfPolicyConstraint": atmfPolicyConstraint,
       "atmPolicyConstraintMIB": atmPolicyConstraintMIB,
       "policyConstraintMIBObjects": policyConstraintMIBObjects,
       "policyConstraintBaseGroup": policyConstraintBaseGroup,
       "policyConstraintMaximum": policyConstraintMaximum,
       "policyMaximum": policyMaximum,
       "policyNeNSCListMaximum": policyNeNSCListMaximum,
       "policyRpNSCListMaximum": policyRpNSCListMaximum,
       "policyConstraintGroup": policyConstraintGroup,
       "policyNextPolicyConstraintIndex": policyNextPolicyConstraintIndex,
       "policyConstraintTable": policyConstraintTable,
       "policyConstraintEntry": policyConstraintEntry,
       "policyConstraintIndex": policyConstraintIndex,
       "policyConstraintPolicyIndex": policyConstraintPolicyIndex,
       "policyIndex": policyIndex,
       "policyConstraintRowStatus": policyConstraintRowStatus,
       "policyConstraintNameTable": policyConstraintNameTable,
       "policyConstraintNameEntry": policyConstraintNameEntry,
       "policyConstraintName": policyConstraintName,
       "policyConstraintNameRowStatus": policyConstraintNameRowStatus,
       "policyGroup": policyGroup,
       "policyNextPolicyIndex": policyNextPolicyIndex,
       "policyTable": policyTable,
       "policyEntry": policyEntry,
       "policyName": policyName,
       "requireNeNscOperator": requireNeNscOperator,
       "requireRpNscOperator": requireRpNscOperator,
       "mustAvoidNeNscOperator": mustAvoidNeNscOperator,
       "policyRowStatus": policyRowStatus,
       "policyNeNscTable": policyNeNscTable,
       "policyNeNscEntry": policyNeNscEntry,
       "policyNeNscIndex": policyNeNscIndex,
       "policyOperator": policyOperator,
       "policyNeNsc": policyNeNsc,
       "policyNeNscRowStatus": policyNeNscRowStatus,
       "policyRpNscTable": policyRpNscTable,
       "policyRpNscEntry": policyRpNscEntry,
       "policyRpNscIndex": policyRpNscIndex,
       "policyRpNsc": policyRpNsc,
       "policyRpNscRowStatus": policyRpNscRowStatus,
       "policyReferenceTable": policyReferenceTable,
       "policyReferenceEntry": policyReferenceEntry,
       "policyReferencePCIndex": policyReferencePCIndex,
       "policyConstraintMIBConformance": policyConstraintMIBConformance,
       "policyConstraintMIBCompliances": policyConstraintMIBCompliances,
       "policyConstraintMIBCompliance": policyConstraintMIBCompliance,
       "policyConstraintMIBGroups": policyConstraintMIBGroups,
       "policyConstraintMIBMandatoryGroup": policyConstraintMIBMandatoryGroup,
       "policyConstraintMIBOptionalGroup": policyConstraintMIBOptionalGroup}
)
