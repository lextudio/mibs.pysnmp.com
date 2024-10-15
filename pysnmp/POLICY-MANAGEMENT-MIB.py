# SNMP MIB module (POLICY-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:11 2024
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
    "TimeTicks",
    "Unsigned32",
    "experimental",
    "iso")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

policyMgt = ModuleIdentity(
    (1, 3, 6, 1, 3, 107)
)
policyMgt.setRevisions(
        ("2000-10-11 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UTF8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"


# MIB Managed Objects in the order of their OIDs

_PmPolicyTable_Object = MibTable
pmPolicyTable = _PmPolicyTable_Object(
    (1, 3, 6, 1, 3, 107, 1)
)
if mibBuilder.loadTexts:
    pmPolicyTable.setStatus("current")
_PmPolicyEntry_Object = MibTableRow
pmPolicyEntry = _PmPolicyEntry_Object(
    (1, 3, 6, 1, 3, 107, 1, 1)
)
pmPolicyEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"),
)
if mibBuilder.loadTexts:
    pmPolicyEntry.setStatus("current")
_PmPolicyIndex_Type = Unsigned32
_PmPolicyIndex_Object = MibTableColumn
pmPolicyIndex = _PmPolicyIndex_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 1),
    _PmPolicyIndex_Type()
)
pmPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPolicyIndex.setStatus("current")
_PmPolicyFilter_Type = UTF8String
_PmPolicyFilter_Object = MibTableColumn
pmPolicyFilter = _PmPolicyFilter_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 2),
    _PmPolicyFilter_Type()
)
pmPolicyFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyFilter.setStatus("current")
_PmPolicyCalendar_Type = RowPointer
_PmPolicyCalendar_Object = MibTableColumn
pmPolicyCalendar = _PmPolicyCalendar_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 3),
    _PmPolicyCalendar_Type()
)
pmPolicyCalendar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyCalendar.setStatus("current")
_PmPolicyAction_Type = UTF8String
_PmPolicyAction_Object = MibTableColumn
pmPolicyAction = _PmPolicyAction_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 4),
    _PmPolicyAction_Type()
)
pmPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyAction.setStatus("current")
_PmPolicyFilterMaxLatency_Type = Unsigned32
_PmPolicyFilterMaxLatency_Object = MibTableColumn
pmPolicyFilterMaxLatency = _PmPolicyFilterMaxLatency_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 5),
    _PmPolicyFilterMaxLatency_Type()
)
pmPolicyFilterMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyFilterMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyFilterMaxLatency.setUnits("milliseconds")
_PmPolicyActionMaxLatency_Type = Unsigned32
_PmPolicyActionMaxLatency_Object = MibTableColumn
pmPolicyActionMaxLatency = _PmPolicyActionMaxLatency_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 6),
    _PmPolicyActionMaxLatency_Type()
)
pmPolicyActionMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyActionMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyActionMaxLatency.setUnits("milliseconds")


class _PmPolicyPrecedence_Type(Unsigned32):
    """Custom type pmPolicyPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmPolicyPrecedence_Type.__name__ = "Unsigned32"
_PmPolicyPrecedence_Object = MibTableColumn
pmPolicyPrecedence = _PmPolicyPrecedence_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 7),
    _PmPolicyPrecedence_Type()
)
pmPolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyPrecedence.setStatus("current")


class _PmPolicyGroup_Type(UTF8String):
    """Custom type pmPolicyGroup based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmPolicyGroup_Type.__name__ = "UTF8String"
_PmPolicyGroup_Object = MibTableColumn
pmPolicyGroup = _PmPolicyGroup_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 8),
    _PmPolicyGroup_Type()
)
pmPolicyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyGroup.setStatus("current")


class _PmPolicyDescription_Type(UTF8String):
    """Custom type pmPolicyDescription based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PmPolicyDescription_Type.__name__ = "UTF8String"
_PmPolicyDescription_Object = MibTableColumn
pmPolicyDescription = _PmPolicyDescription_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 9),
    _PmPolicyDescription_Type()
)
pmPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyDescription.setStatus("current")
_PmPolicyMatches_Type = Gauge32
_PmPolicyMatches_Object = MibTableColumn
pmPolicyMatches = _PmPolicyMatches_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 10),
    _PmPolicyMatches_Type()
)
pmPolicyMatches.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyMatches.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyMatches.setUnits("elements")
_PmPolicyExecutionErrors_Type = Counter32
_PmPolicyExecutionErrors_Object = MibTableColumn
pmPolicyExecutionErrors = _PmPolicyExecutionErrors_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 11),
    _PmPolicyExecutionErrors_Type()
)
pmPolicyExecutionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyExecutionErrors.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyExecutionErrors.setUnits("errors")


class _PmPolicyDebugging_Type(Integer32):
    """Custom type pmPolicyDebugging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PmPolicyDebugging_Type.__name__ = "Integer32"
_PmPolicyDebugging_Object = MibTableColumn
pmPolicyDebugging = _PmPolicyDebugging_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 12),
    _PmPolicyDebugging_Type()
)
pmPolicyDebugging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyDebugging.setStatus("current")
_PmPolicyStatus_Type = RowStatus
_PmPolicyStatus_Object = MibTableColumn
pmPolicyStatus = _PmPolicyStatus_Object(
    (1, 3, 6, 1, 3, 107, 1, 1, 13),
    _PmPolicyStatus_Type()
)
pmPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyStatus.setStatus("current")
_PmElementTypeRegTable_Object = MibTable
pmElementTypeRegTable = _PmElementTypeRegTable_Object(
    (1, 3, 6, 1, 3, 107, 2)
)
if mibBuilder.loadTexts:
    pmElementTypeRegTable.setStatus("current")
_PmElementTypeRegEntry_Object = MibTableRow
pmElementTypeRegEntry = _PmElementTypeRegEntry_Object(
    (1, 3, 6, 1, 3, 107, 2, 1)
)
pmElementTypeRegEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmElementTypeRegIndex"),
)
if mibBuilder.loadTexts:
    pmElementTypeRegEntry.setStatus("current")
_PmElementTypeRegIndex_Type = Unsigned32
_PmElementTypeRegIndex_Object = MibTableColumn
pmElementTypeRegIndex = _PmElementTypeRegIndex_Object(
    (1, 3, 6, 1, 3, 107, 2, 1, 1),
    _PmElementTypeRegIndex_Type()
)
pmElementTypeRegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmElementTypeRegIndex.setStatus("current")
_PmElementTypeRegOIDPrefix_Type = ObjectIdentifier
_PmElementTypeRegOIDPrefix_Object = MibTableColumn
pmElementTypeRegOIDPrefix = _PmElementTypeRegOIDPrefix_Object(
    (1, 3, 6, 1, 3, 107, 2, 1, 2),
    _PmElementTypeRegOIDPrefix_Type()
)
pmElementTypeRegOIDPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegOIDPrefix.setStatus("current")


class _PmElementTypeRegName_Type(UTF8String):
    """Custom type pmElementTypeRegName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmElementTypeRegName_Type.__name__ = "UTF8String"
_PmElementTypeRegName_Object = MibTableColumn
pmElementTypeRegName = _PmElementTypeRegName_Object(
    (1, 3, 6, 1, 3, 107, 2, 1, 3),
    _PmElementTypeRegName_Type()
)
pmElementTypeRegName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegName.setStatus("current")
_PmElementTypeRegRowStatus_Type = RowStatus
_PmElementTypeRegRowStatus_Object = MibTableColumn
pmElementTypeRegRowStatus = _PmElementTypeRegRowStatus_Object(
    (1, 3, 6, 1, 3, 107, 2, 1, 4),
    _PmElementTypeRegRowStatus_Type()
)
pmElementTypeRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegRowStatus.setStatus("current")
_PmRoleESTable_Object = MibTable
pmRoleESTable = _PmRoleESTable_Object(
    (1, 3, 6, 1, 3, 107, 3)
)
if mibBuilder.loadTexts:
    pmRoleESTable.setStatus("current")
_PmRoleESEntry_Object = MibTableRow
pmRoleESEntry = _PmRoleESEntry_Object(
    (1, 3, 6, 1, 3, 107, 3, 1)
)
pmRoleESEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmRoleESElement"),
    (0, "POLICY-MANAGEMENT-MIB", "pmRoleESString"),
)
if mibBuilder.loadTexts:
    pmRoleESEntry.setStatus("current")
_PmRoleESElement_Type = RowPointer
_PmRoleESElement_Object = MibTableColumn
pmRoleESElement = _PmRoleESElement_Object(
    (1, 3, 6, 1, 3, 107, 3, 1, 1),
    _PmRoleESElement_Type()
)
pmRoleESElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleESElement.setStatus("current")


class _PmRoleESString_Type(UTF8String):
    """Custom type pmRoleESString based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PmRoleESString_Type.__name__ = "UTF8String"
_PmRoleESString_Object = MibTableColumn
pmRoleESString = _PmRoleESString_Object(
    (1, 3, 6, 1, 3, 107, 3, 1, 2),
    _PmRoleESString_Type()
)
pmRoleESString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleESString.setStatus("current")
_PmRoleESStatus_Type = RowStatus
_PmRoleESStatus_Object = MibTableColumn
pmRoleESStatus = _PmRoleESStatus_Object(
    (1, 3, 6, 1, 3, 107, 3, 1, 3),
    _PmRoleESStatus_Type()
)
pmRoleESStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRoleESStatus.setStatus("current")
_PmRoleSETable_Object = MibTable
pmRoleSETable = _PmRoleSETable_Object(
    (1, 3, 6, 1, 3, 107, 4)
)
if mibBuilder.loadTexts:
    pmRoleSETable.setStatus("current")
_PmRoleSEEntry_Object = MibTableRow
pmRoleSEEntry = _PmRoleSEEntry_Object(
    (1, 3, 6, 1, 3, 107, 4, 1)
)
pmRoleSEEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmRoleSEString"),
    (0, "POLICY-MANAGEMENT-MIB", "pmRoleSEElement"),
)
if mibBuilder.loadTexts:
    pmRoleSEEntry.setStatus("current")


class _PmRoleSEString_Type(UTF8String):
    """Custom type pmRoleSEString based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PmRoleSEString_Type.__name__ = "UTF8String"
_PmRoleSEString_Object = MibTableColumn
pmRoleSEString = _PmRoleSEString_Object(
    (1, 3, 6, 1, 3, 107, 4, 1, 1),
    _PmRoleSEString_Type()
)
pmRoleSEString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleSEString.setStatus("current")
_PmRoleSEElement_Type = RowPointer
_PmRoleSEElement_Object = MibTableColumn
pmRoleSEElement = _PmRoleSEElement_Object(
    (1, 3, 6, 1, 3, 107, 4, 1, 2),
    _PmRoleSEElement_Type()
)
pmRoleSEElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRoleSEElement.setStatus("current")
_PmCapabilitiesTable_Object = MibTable
pmCapabilitiesTable = _PmCapabilitiesTable_Object(
    (1, 3, 6, 1, 3, 107, 5)
)
if mibBuilder.loadTexts:
    pmCapabilitiesTable.setStatus("current")
_PmCapabilitiesEntry_Object = MibTableRow
pmCapabilitiesEntry = _PmCapabilitiesEntry_Object(
    (1, 3, 6, 1, 3, 107, 5, 1)
)
pmCapabilitiesEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmCapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmCapabilitiesEntry.setStatus("current")
_PmCapabilitiesIndex_Type = Unsigned32
_PmCapabilitiesIndex_Object = MibTableColumn
pmCapabilitiesIndex = _PmCapabilitiesIndex_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 1),
    _PmCapabilitiesIndex_Type()
)
pmCapabilitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmCapabilitiesIndex.setStatus("current")
_PmCapabilitiesType_Type = ObjectIdentifier
_PmCapabilitiesType_Object = MibTableColumn
pmCapabilitiesType = _PmCapabilitiesType_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 2),
    _PmCapabilitiesType_Type()
)
pmCapabilitiesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesType.setStatus("current")
_PmCapabilitiesSubType_Type = ObjectIdentifier
_PmCapabilitiesSubType_Object = MibTableColumn
pmCapabilitiesSubType = _PmCapabilitiesSubType_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 3),
    _PmCapabilitiesSubType_Type()
)
pmCapabilitiesSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesSubType.setStatus("current")
_PmCapabilitiesModificationOID_Type = ObjectIdentifier
_PmCapabilitiesModificationOID_Object = MibTableColumn
pmCapabilitiesModificationOID = _PmCapabilitiesModificationOID_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 4),
    _PmCapabilitiesModificationOID_Type()
)
pmCapabilitiesModificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesModificationOID.setStatus("current")


class _PmCapabilitiesModificationType_Type(Integer32):
    """Custom type pmCapabilitiesModificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("additional", 2),
          ("addvalue", 3),
          ("maxlimit", 4),
          ("minlimit", 5),
          ("restricted", 1),
          ("unsupported", 0))
    )


_PmCapabilitiesModificationType_Type.__name__ = "Integer32"
_PmCapabilitiesModificationType_Object = MibTableColumn
pmCapabilitiesModificationType = _PmCapabilitiesModificationType_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 5),
    _PmCapabilitiesModificationType_Type()
)
pmCapabilitiesModificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesModificationType.setStatus("current")


class _PmCapabilitiesModificationValue_Type(Integer32):
    """Custom type pmCapabilitiesModificationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmCapabilitiesModificationValue_Type.__name__ = "Integer32"
_PmCapabilitiesModificationValue_Object = MibTableColumn
pmCapabilitiesModificationValue = _PmCapabilitiesModificationValue_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 6),
    _PmCapabilitiesModificationValue_Type()
)
pmCapabilitiesModificationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesModificationValue.setStatus("current")
_PmCapabilitiesModificationString_Type = OctetString
_PmCapabilitiesModificationString_Object = MibTableColumn
pmCapabilitiesModificationString = _PmCapabilitiesModificationString_Object(
    (1, 3, 6, 1, 3, 107, 5, 1, 7),
    _PmCapabilitiesModificationString_Type()
)
pmCapabilitiesModificationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesModificationString.setStatus("current")
_PmTrackingPolicyToElementTable_Object = MibTable
pmTrackingPolicyToElementTable = _PmTrackingPolicyToElementTable_Object(
    (1, 3, 6, 1, 3, 107, 6)
)
if mibBuilder.loadTexts:
    pmTrackingPolicyToElementTable.setStatus("current")
_PmTrackingPolicyToElementEntry_Object = MibTableRow
pmTrackingPolicyToElementEntry = _PmTrackingPolicyToElementEntry_Object(
    (1, 3, 6, 1, 3, 107, 6, 1)
)
pmTrackingPolicyToElementEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"),
    (0, "POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementElement"),
)
if mibBuilder.loadTexts:
    pmTrackingPolicyToElementEntry.setStatus("current")
_PmTrackingPolicyToElementElement_Type = RowPointer
_PmTrackingPolicyToElementElement_Object = MibTableColumn
pmTrackingPolicyToElementElement = _PmTrackingPolicyToElementElement_Object(
    (1, 3, 6, 1, 3, 107, 6, 1, 1),
    _PmTrackingPolicyToElementElement_Type()
)
pmTrackingPolicyToElementElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingPolicyToElementElement.setStatus("current")


class _PmTrackingPolicyToElementStatus_Type(Integer32):
    """Custom type pmTrackingPolicyToElementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PmTrackingPolicyToElementStatus_Type.__name__ = "Integer32"
_PmTrackingPolicyToElementStatus_Object = MibTableColumn
pmTrackingPolicyToElementStatus = _PmTrackingPolicyToElementStatus_Object(
    (1, 3, 6, 1, 3, 107, 6, 1, 2),
    _PmTrackingPolicyToElementStatus_Type()
)
pmTrackingPolicyToElementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTrackingPolicyToElementStatus.setStatus("current")
_PmTrackingElementToPolicyTable_Object = MibTable
pmTrackingElementToPolicyTable = _PmTrackingElementToPolicyTable_Object(
    (1, 3, 6, 1, 3, 107, 7)
)
if mibBuilder.loadTexts:
    pmTrackingElementToPolicyTable.setStatus("current")
_PmTrackingElementToPolicyEntry_Object = MibTableRow
pmTrackingElementToPolicyEntry = _PmTrackingElementToPolicyEntry_Object(
    (1, 3, 6, 1, 3, 107, 7, 1)
)
pmTrackingElementToPolicyEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyElement"),
    (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"),
)
if mibBuilder.loadTexts:
    pmTrackingElementToPolicyEntry.setStatus("current")
_PmTrackingElementToPolicyElement_Type = RowPointer
_PmTrackingElementToPolicyElement_Object = MibTableColumn
pmTrackingElementToPolicyElement = _PmTrackingElementToPolicyElement_Object(
    (1, 3, 6, 1, 3, 107, 7, 1, 1),
    _PmTrackingElementToPolicyElement_Type()
)
pmTrackingElementToPolicyElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingElementToPolicyElement.setStatus("current")


class _PmTrackingElementToPolicyStatus_Type(Integer32):
    """Custom type pmTrackingElementToPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOff", 2),
          ("off", 0),
          ("on", 1))
    )


_PmTrackingElementToPolicyStatus_Type.__name__ = "Integer32"
_PmTrackingElementToPolicyStatus_Object = MibTableColumn
pmTrackingElementToPolicyStatus = _PmTrackingElementToPolicyStatus_Object(
    (1, 3, 6, 1, 3, 107, 7, 1, 2),
    _PmTrackingElementToPolicyStatus_Type()
)
pmTrackingElementToPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTrackingElementToPolicyStatus.setStatus("current")
_PmDebuggingTable_Object = MibTable
pmDebuggingTable = _PmDebuggingTable_Object(
    (1, 3, 6, 1, 3, 107, 8)
)
if mibBuilder.loadTexts:
    pmDebuggingTable.setStatus("current")
_PmDebuggingEntry_Object = MibTableRow
pmDebuggingEntry = _PmDebuggingEntry_Object(
    (1, 3, 6, 1, 3, 107, 8, 1)
)
pmDebuggingEntry.setIndexNames(
    (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"),
    (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingElement"),
    (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"),
)
if mibBuilder.loadTexts:
    pmDebuggingEntry.setStatus("current")
_PmDebuggingElement_Type = RowPointer
_PmDebuggingElement_Object = MibTableColumn
pmDebuggingElement = _PmDebuggingElement_Object(
    (1, 3, 6, 1, 3, 107, 8, 1, 1),
    _PmDebuggingElement_Type()
)
pmDebuggingElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDebuggingElement.setStatus("current")
_PmDebuggingLogIndex_Type = Unsigned32
_PmDebuggingLogIndex_Object = MibTableColumn
pmDebuggingLogIndex = _PmDebuggingLogIndex_Object(
    (1, 3, 6, 1, 3, 107, 8, 1, 2),
    _PmDebuggingLogIndex_Type()
)
pmDebuggingLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDebuggingLogIndex.setStatus("current")


class _PmDebuggingMessage_Type(UTF8String):
    """Custom type pmDebuggingMessage based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PmDebuggingMessage_Type.__name__ = "UTF8String"
_PmDebuggingMessage_Object = MibTableColumn
pmDebuggingMessage = _PmDebuggingMessage_Object(
    (1, 3, 6, 1, 3, 107, 8, 1, 3),
    _PmDebuggingMessage_Type()
)
pmDebuggingMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDebuggingMessage.setStatus("current")
_PmConformance_ObjectIdentity = ObjectIdentity
pmConformance = _PmConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 107, 20)
)
_PmCompliances_ObjectIdentity = ObjectIdentity
pmCompliances = _PmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 107, 20, 1)
)
_PmGroups_ObjectIdentity = ObjectIdentity
pmGroups = _PmGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 107, 20, 2)
)
_PmBaseFunctionLibrary_ObjectIdentity = ObjectIdentity
pmBaseFunctionLibrary = _PmBaseFunctionLibrary_ObjectIdentity(
    (1, 3, 6, 1, 3, 107, 20, 2, 2)
)

# Managed Objects groups

pmPolicyManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 107, 20, 2, 1)
)
pmPolicyManagementGroup.setObjects(
      *(("POLICY-MANAGEMENT-MIB", "pmPolicyFilter"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyCalendar"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyAction"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyFilterMaxLatency"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyActionMaxLatency"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyPrecedence"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyGroup"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyDescription"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyMatches"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyExecutionErrors"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyDebugging"),
        ("POLICY-MANAGEMENT-MIB", "pmPolicyStatus"),
        ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegOIDPrefix"),
        ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegName"),
        ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegRowStatus"),
        ("POLICY-MANAGEMENT-MIB", "pmRoleESStatus"),
        ("POLICY-MANAGEMENT-MIB", "pmRoleSEElement"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesType"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesSubType"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationOID"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationType"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationValue"),
        ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationString"),
        ("POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementStatus"),
        ("POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyStatus"),
        ("POLICY-MANAGEMENT-MIB", "pmDebuggingElement"),
        ("POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"),
        ("POLICY-MANAGEMENT-MIB", "pmDebuggingMessage"))
)
if mibBuilder.loadTexts:
    pmPolicyManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 107, 20, 1, 1)
)
if mibBuilder.loadTexts:
    pmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-MANAGEMENT-MIB",
    **{"UTF8String": UTF8String,
       "policyMgt": policyMgt,
       "pmPolicyTable": pmPolicyTable,
       "pmPolicyEntry": pmPolicyEntry,
       "pmPolicyIndex": pmPolicyIndex,
       "pmPolicyFilter": pmPolicyFilter,
       "pmPolicyCalendar": pmPolicyCalendar,
       "pmPolicyAction": pmPolicyAction,
       "pmPolicyFilterMaxLatency": pmPolicyFilterMaxLatency,
       "pmPolicyActionMaxLatency": pmPolicyActionMaxLatency,
       "pmPolicyPrecedence": pmPolicyPrecedence,
       "pmPolicyGroup": pmPolicyGroup,
       "pmPolicyDescription": pmPolicyDescription,
       "pmPolicyMatches": pmPolicyMatches,
       "pmPolicyExecutionErrors": pmPolicyExecutionErrors,
       "pmPolicyDebugging": pmPolicyDebugging,
       "pmPolicyStatus": pmPolicyStatus,
       "pmElementTypeRegTable": pmElementTypeRegTable,
       "pmElementTypeRegEntry": pmElementTypeRegEntry,
       "pmElementTypeRegIndex": pmElementTypeRegIndex,
       "pmElementTypeRegOIDPrefix": pmElementTypeRegOIDPrefix,
       "pmElementTypeRegName": pmElementTypeRegName,
       "pmElementTypeRegRowStatus": pmElementTypeRegRowStatus,
       "pmRoleESTable": pmRoleESTable,
       "pmRoleESEntry": pmRoleESEntry,
       "pmRoleESElement": pmRoleESElement,
       "pmRoleESString": pmRoleESString,
       "pmRoleESStatus": pmRoleESStatus,
       "pmRoleSETable": pmRoleSETable,
       "pmRoleSEEntry": pmRoleSEEntry,
       "pmRoleSEString": pmRoleSEString,
       "pmRoleSEElement": pmRoleSEElement,
       "pmCapabilitiesTable": pmCapabilitiesTable,
       "pmCapabilitiesEntry": pmCapabilitiesEntry,
       "pmCapabilitiesIndex": pmCapabilitiesIndex,
       "pmCapabilitiesType": pmCapabilitiesType,
       "pmCapabilitiesSubType": pmCapabilitiesSubType,
       "pmCapabilitiesModificationOID": pmCapabilitiesModificationOID,
       "pmCapabilitiesModificationType": pmCapabilitiesModificationType,
       "pmCapabilitiesModificationValue": pmCapabilitiesModificationValue,
       "pmCapabilitiesModificationString": pmCapabilitiesModificationString,
       "pmTrackingPolicyToElementTable": pmTrackingPolicyToElementTable,
       "pmTrackingPolicyToElementEntry": pmTrackingPolicyToElementEntry,
       "pmTrackingPolicyToElementElement": pmTrackingPolicyToElementElement,
       "pmTrackingPolicyToElementStatus": pmTrackingPolicyToElementStatus,
       "pmTrackingElementToPolicyTable": pmTrackingElementToPolicyTable,
       "pmTrackingElementToPolicyEntry": pmTrackingElementToPolicyEntry,
       "pmTrackingElementToPolicyElement": pmTrackingElementToPolicyElement,
       "pmTrackingElementToPolicyStatus": pmTrackingElementToPolicyStatus,
       "pmDebuggingTable": pmDebuggingTable,
       "pmDebuggingEntry": pmDebuggingEntry,
       "pmDebuggingElement": pmDebuggingElement,
       "pmDebuggingLogIndex": pmDebuggingLogIndex,
       "pmDebuggingMessage": pmDebuggingMessage,
       "pmConformance": pmConformance,
       "pmCompliances": pmCompliances,
       "pmCompliance": pmCompliance,
       "pmGroups": pmGroups,
       "pmPolicyManagementGroup": pmPolicyManagementGroup,
       "pmBaseFunctionLibrary": pmBaseFunctionLibrary}
)
