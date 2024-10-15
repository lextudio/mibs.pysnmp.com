# SNMP MIB module (POLICY-BASED-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-BASED-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:09 2024
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

pmMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 124)
)
pmMib.setRevisions(
        ("2005-02-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PmUTF8String(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_PmNotifications_ObjectIdentity = ObjectIdentity
pmNotifications = _PmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 124, 0)
)
_PmPolicyTable_Object = MibTable
pmPolicyTable = _PmPolicyTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 1)
)
if mibBuilder.loadTexts:
    pmPolicyTable.setStatus("current")
_PmPolicyEntry_Object = MibTableRow
pmPolicyEntry = _PmPolicyEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1)
)
pmPolicyEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyAdminGroup"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyIndex"),
)
if mibBuilder.loadTexts:
    pmPolicyEntry.setStatus("current")


class _PmPolicyAdminGroup_Type(PmUTF8String):
    """Custom type pmPolicyAdminGroup based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmPolicyAdminGroup_Type.__name__ = "PmUTF8String"
_PmPolicyAdminGroup_Object = MibTableColumn
pmPolicyAdminGroup = _PmPolicyAdminGroup_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 1),
    _PmPolicyAdminGroup_Type()
)
pmPolicyAdminGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPolicyAdminGroup.setStatus("current")


class _PmPolicyIndex_Type(Unsigned32):
    """Custom type pmPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicyIndex_Type.__name__ = "Unsigned32"
_PmPolicyIndex_Object = MibTableColumn
pmPolicyIndex = _PmPolicyIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 2),
    _PmPolicyIndex_Type()
)
pmPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPolicyIndex.setStatus("current")


class _PmPolicyPrecedenceGroup_Type(PmUTF8String):
    """Custom type pmPolicyPrecedenceGroup based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmPolicyPrecedenceGroup_Type.__name__ = "PmUTF8String"
_PmPolicyPrecedenceGroup_Object = MibTableColumn
pmPolicyPrecedenceGroup = _PmPolicyPrecedenceGroup_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 3),
    _PmPolicyPrecedenceGroup_Type()
)
pmPolicyPrecedenceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyPrecedenceGroup.setStatus("current")


class _PmPolicyPrecedence_Type(Unsigned32):
    """Custom type pmPolicyPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmPolicyPrecedence_Type.__name__ = "Unsigned32"
_PmPolicyPrecedence_Object = MibTableColumn
pmPolicyPrecedence = _PmPolicyPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 4),
    _PmPolicyPrecedence_Type()
)
pmPolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyPrecedence.setStatus("current")


class _PmPolicySchedule_Type(Unsigned32):
    """Custom type pmPolicySchedule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicySchedule_Type.__name__ = "Unsigned32"
_PmPolicySchedule_Object = MibTableColumn
pmPolicySchedule = _PmPolicySchedule_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 5),
    _PmPolicySchedule_Type()
)
pmPolicySchedule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicySchedule.setStatus("current")


class _PmPolicyElementTypeFilter_Type(PmUTF8String):
    """Custom type pmPolicyElementTypeFilter based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PmPolicyElementTypeFilter_Type.__name__ = "PmUTF8String"
_PmPolicyElementTypeFilter_Object = MibTableColumn
pmPolicyElementTypeFilter = _PmPolicyElementTypeFilter_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 6),
    _PmPolicyElementTypeFilter_Type()
)
pmPolicyElementTypeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyElementTypeFilter.setStatus("current")


class _PmPolicyConditionScriptIndex_Type(Unsigned32):
    """Custom type pmPolicyConditionScriptIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicyConditionScriptIndex_Type.__name__ = "Unsigned32"
_PmPolicyConditionScriptIndex_Object = MibTableColumn
pmPolicyConditionScriptIndex = _PmPolicyConditionScriptIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 7),
    _PmPolicyConditionScriptIndex_Type()
)
pmPolicyConditionScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyConditionScriptIndex.setStatus("current")


class _PmPolicyActionScriptIndex_Type(Unsigned32):
    """Custom type pmPolicyActionScriptIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicyActionScriptIndex_Type.__name__ = "Unsigned32"
_PmPolicyActionScriptIndex_Object = MibTableColumn
pmPolicyActionScriptIndex = _PmPolicyActionScriptIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 8),
    _PmPolicyActionScriptIndex_Type()
)
pmPolicyActionScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyActionScriptIndex.setStatus("current")


class _PmPolicyParameters_Type(OctetString):
    """Custom type pmPolicyParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_PmPolicyParameters_Type.__name__ = "OctetString"
_PmPolicyParameters_Object = MibTableColumn
pmPolicyParameters = _PmPolicyParameters_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 9),
    _PmPolicyParameters_Type()
)
pmPolicyParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyParameters.setStatus("current")


class _PmPolicyConditionMaxLatency_Type(Unsigned32):
    """Custom type pmPolicyConditionMaxLatency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmPolicyConditionMaxLatency_Type.__name__ = "Unsigned32"
_PmPolicyConditionMaxLatency_Object = MibTableColumn
pmPolicyConditionMaxLatency = _PmPolicyConditionMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 10),
    _PmPolicyConditionMaxLatency_Type()
)
pmPolicyConditionMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyConditionMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyConditionMaxLatency.setUnits("milliseconds")


class _PmPolicyActionMaxLatency_Type(Unsigned32):
    """Custom type pmPolicyActionMaxLatency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmPolicyActionMaxLatency_Type.__name__ = "Unsigned32"
_PmPolicyActionMaxLatency_Object = MibTableColumn
pmPolicyActionMaxLatency = _PmPolicyActionMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 11),
    _PmPolicyActionMaxLatency_Type()
)
pmPolicyActionMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyActionMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyActionMaxLatency.setUnits("milliseconds")
_PmPolicyMaxIterations_Type = Unsigned32
_PmPolicyMaxIterations_Object = MibTableColumn
pmPolicyMaxIterations = _PmPolicyMaxIterations_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 12),
    _PmPolicyMaxIterations_Type()
)
pmPolicyMaxIterations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyMaxIterations.setStatus("current")
_PmPolicyDescription_Type = PmUTF8String
_PmPolicyDescription_Object = MibTableColumn
pmPolicyDescription = _PmPolicyDescription_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 13),
    _PmPolicyDescription_Type()
)
pmPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyDescription.setStatus("current")
_PmPolicyMatches_Type = Gauge32
_PmPolicyMatches_Object = MibTableColumn
pmPolicyMatches = _PmPolicyMatches_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 14),
    _PmPolicyMatches_Type()
)
pmPolicyMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyMatches.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyMatches.setUnits("elements")
_PmPolicyAbnormalTerminations_Type = Gauge32
_PmPolicyAbnormalTerminations_Object = MibTableColumn
pmPolicyAbnormalTerminations = _PmPolicyAbnormalTerminations_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 15),
    _PmPolicyAbnormalTerminations_Type()
)
pmPolicyAbnormalTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyAbnormalTerminations.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyAbnormalTerminations.setUnits("elements")
_PmPolicyExecutionErrors_Type = Counter32
_PmPolicyExecutionErrors_Object = MibTableColumn
pmPolicyExecutionErrors = _PmPolicyExecutionErrors_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 16),
    _PmPolicyExecutionErrors_Type()
)
pmPolicyExecutionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPolicyExecutionErrors.setStatus("current")
if mibBuilder.loadTexts:
    pmPolicyExecutionErrors.setUnits("errors")


class _PmPolicyDebugging_Type(Integer32):
    """Custom type pmPolicyDebugging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PmPolicyDebugging_Type.__name__ = "Integer32"
_PmPolicyDebugging_Object = MibTableColumn
pmPolicyDebugging = _PmPolicyDebugging_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 17),
    _PmPolicyDebugging_Type()
)
pmPolicyDebugging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyDebugging.setStatus("current")


class _PmPolicyAdminStatus_Type(Integer32):
    """Custom type pmPolicyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledAutoRemove", 3))
    )


_PmPolicyAdminStatus_Type.__name__ = "Integer32"
_PmPolicyAdminStatus_Object = MibTableColumn
pmPolicyAdminStatus = _PmPolicyAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 18),
    _PmPolicyAdminStatus_Type()
)
pmPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyAdminStatus.setStatus("current")
_PmPolicyStorageType_Type = StorageType
_PmPolicyStorageType_Object = MibTableColumn
pmPolicyStorageType = _PmPolicyStorageType_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 19),
    _PmPolicyStorageType_Type()
)
pmPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyStorageType.setStatus("current")
_PmPolicyRowStatus_Type = RowStatus
_PmPolicyRowStatus_Object = MibTableColumn
pmPolicyRowStatus = _PmPolicyRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 1, 1, 20),
    _PmPolicyRowStatus_Type()
)
pmPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyRowStatus.setStatus("current")
_PmPolicyCodeTable_Object = MibTable
pmPolicyCodeTable = _PmPolicyCodeTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 2)
)
if mibBuilder.loadTexts:
    pmPolicyCodeTable.setStatus("current")
_PmPolicyCodeEntry_Object = MibTableRow
pmPolicyCodeEntry = _PmPolicyCodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 2, 1)
)
pmPolicyCodeEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyAdminGroup"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyCodeScriptIndex"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyCodeSegment"),
)
if mibBuilder.loadTexts:
    pmPolicyCodeEntry.setStatus("current")


class _PmPolicyCodeScriptIndex_Type(Unsigned32):
    """Custom type pmPolicyCodeScriptIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicyCodeScriptIndex_Type.__name__ = "Unsigned32"
_PmPolicyCodeScriptIndex_Object = MibTableColumn
pmPolicyCodeScriptIndex = _PmPolicyCodeScriptIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 2, 1, 1),
    _PmPolicyCodeScriptIndex_Type()
)
pmPolicyCodeScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPolicyCodeScriptIndex.setStatus("current")


class _PmPolicyCodeSegment_Type(Unsigned32):
    """Custom type pmPolicyCodeSegment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmPolicyCodeSegment_Type.__name__ = "Unsigned32"
_PmPolicyCodeSegment_Object = MibTableColumn
pmPolicyCodeSegment = _PmPolicyCodeSegment_Object(
    (1, 3, 6, 1, 2, 1, 124, 2, 1, 2),
    _PmPolicyCodeSegment_Type()
)
pmPolicyCodeSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPolicyCodeSegment.setStatus("current")


class _PmPolicyCodeText_Type(PmUTF8String):
    """Custom type pmPolicyCodeText based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PmPolicyCodeText_Type.__name__ = "PmUTF8String"
_PmPolicyCodeText_Object = MibTableColumn
pmPolicyCodeText = _PmPolicyCodeText_Object(
    (1, 3, 6, 1, 2, 1, 124, 2, 1, 3),
    _PmPolicyCodeText_Type()
)
pmPolicyCodeText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyCodeText.setStatus("current")
_PmPolicyCodeStatus_Type = RowStatus
_PmPolicyCodeStatus_Object = MibTableColumn
pmPolicyCodeStatus = _PmPolicyCodeStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 2, 1, 4),
    _PmPolicyCodeStatus_Type()
)
pmPolicyCodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPolicyCodeStatus.setStatus("current")
_PmElementTypeRegTable_Object = MibTable
pmElementTypeRegTable = _PmElementTypeRegTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 3)
)
if mibBuilder.loadTexts:
    pmElementTypeRegTable.setStatus("current")
_PmElementTypeRegEntry_Object = MibTableRow
pmElementTypeRegEntry = _PmElementTypeRegEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1)
)
pmElementTypeRegEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmElementTypeRegOIDPrefix"),
)
if mibBuilder.loadTexts:
    pmElementTypeRegEntry.setStatus("current")
_PmElementTypeRegOIDPrefix_Type = ObjectIdentifier
_PmElementTypeRegOIDPrefix_Object = MibTableColumn
pmElementTypeRegOIDPrefix = _PmElementTypeRegOIDPrefix_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1, 2),
    _PmElementTypeRegOIDPrefix_Type()
)
pmElementTypeRegOIDPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmElementTypeRegOIDPrefix.setStatus("current")
_PmElementTypeRegMaxLatency_Type = Unsigned32
_PmElementTypeRegMaxLatency_Object = MibTableColumn
pmElementTypeRegMaxLatency = _PmElementTypeRegMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1, 3),
    _PmElementTypeRegMaxLatency_Type()
)
pmElementTypeRegMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    pmElementTypeRegMaxLatency.setUnits("milliseconds")


class _PmElementTypeRegDescription_Type(PmUTF8String):
    """Custom type pmElementTypeRegDescription based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PmElementTypeRegDescription_Type.__name__ = "PmUTF8String"
_PmElementTypeRegDescription_Object = MibTableColumn
pmElementTypeRegDescription = _PmElementTypeRegDescription_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1, 4),
    _PmElementTypeRegDescription_Type()
)
pmElementTypeRegDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegDescription.setStatus("current")
_PmElementTypeRegStorageType_Type = StorageType
_PmElementTypeRegStorageType_Object = MibTableColumn
pmElementTypeRegStorageType = _PmElementTypeRegStorageType_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1, 5),
    _PmElementTypeRegStorageType_Type()
)
pmElementTypeRegStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegStorageType.setStatus("current")
_PmElementTypeRegRowStatus_Type = RowStatus
_PmElementTypeRegRowStatus_Object = MibTableColumn
pmElementTypeRegRowStatus = _PmElementTypeRegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 3, 1, 6),
    _PmElementTypeRegRowStatus_Type()
)
pmElementTypeRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmElementTypeRegRowStatus.setStatus("current")
_PmRoleTable_Object = MibTable
pmRoleTable = _PmRoleTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 4)
)
if mibBuilder.loadTexts:
    pmRoleTable.setStatus("current")
_PmRoleEntry_Object = MibTableRow
pmRoleEntry = _PmRoleEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1)
)
pmRoleEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmRoleElement"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmRoleContextName"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmRoleContextEngineID"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmRoleString"),
)
if mibBuilder.loadTexts:
    pmRoleEntry.setStatus("current")
_PmRoleElement_Type = RowPointer
_PmRoleElement_Object = MibTableColumn
pmRoleElement = _PmRoleElement_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1, 1),
    _PmRoleElement_Type()
)
pmRoleElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleElement.setStatus("current")


class _PmRoleContextName_Type(SnmpAdminString):
    """Custom type pmRoleContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmRoleContextName_Type.__name__ = "SnmpAdminString"
_PmRoleContextName_Object = MibTableColumn
pmRoleContextName = _PmRoleContextName_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1, 2),
    _PmRoleContextName_Type()
)
pmRoleContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleContextName.setStatus("current")


class _PmRoleContextEngineID_Type(OctetString):
    """Custom type pmRoleContextEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_PmRoleContextEngineID_Type.__name__ = "OctetString"
_PmRoleContextEngineID_Object = MibTableColumn
pmRoleContextEngineID = _PmRoleContextEngineID_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1, 3),
    _PmRoleContextEngineID_Type()
)
pmRoleContextEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleContextEngineID.setStatus("current")


class _PmRoleString_Type(PmUTF8String):
    """Custom type pmRoleString based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PmRoleString_Type.__name__ = "PmUTF8String"
_PmRoleString_Object = MibTableColumn
pmRoleString = _PmRoleString_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1, 4),
    _PmRoleString_Type()
)
pmRoleString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmRoleString.setStatus("current")
_PmRoleStatus_Type = RowStatus
_PmRoleStatus_Object = MibTableColumn
pmRoleStatus = _PmRoleStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 4, 1, 5),
    _PmRoleStatus_Type()
)
pmRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRoleStatus.setStatus("current")
_PmCapabilitiesTable_Object = MibTable
pmCapabilitiesTable = _PmCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 5)
)
if mibBuilder.loadTexts:
    pmCapabilitiesTable.setStatus("current")
_PmCapabilitiesEntry_Object = MibTableRow
pmCapabilitiesEntry = _PmCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 5, 1)
)
pmCapabilitiesEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesType"),
)
if mibBuilder.loadTexts:
    pmCapabilitiesEntry.setStatus("current")
_PmCapabilitiesType_Type = ObjectIdentifier
_PmCapabilitiesType_Object = MibTableColumn
pmCapabilitiesType = _PmCapabilitiesType_Object(
    (1, 3, 6, 1, 2, 1, 124, 5, 1, 1),
    _PmCapabilitiesType_Type()
)
pmCapabilitiesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCapabilitiesType.setStatus("current")
_PmCapabilitiesOverrideTable_Object = MibTable
pmCapabilitiesOverrideTable = _PmCapabilitiesOverrideTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 6)
)
if mibBuilder.loadTexts:
    pmCapabilitiesOverrideTable.setStatus("current")
_PmCapabilitiesOverrideEntry_Object = MibTableRow
pmCapabilitiesOverrideEntry = _PmCapabilitiesOverrideEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 6, 1)
)
pmCapabilitiesOverrideEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesOverrideType"),
)
if mibBuilder.loadTexts:
    pmCapabilitiesOverrideEntry.setStatus("current")
_PmCapabilitiesOverrideType_Type = ObjectIdentifier
_PmCapabilitiesOverrideType_Object = MibTableColumn
pmCapabilitiesOverrideType = _PmCapabilitiesOverrideType_Object(
    (1, 3, 6, 1, 2, 1, 124, 6, 1, 1),
    _PmCapabilitiesOverrideType_Type()
)
pmCapabilitiesOverrideType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmCapabilitiesOverrideType.setStatus("current")


class _PmCapabilitiesOverrideState_Type(Integer32):
    """Custom type pmCapabilitiesOverrideState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PmCapabilitiesOverrideState_Type.__name__ = "Integer32"
_PmCapabilitiesOverrideState_Object = MibTableColumn
pmCapabilitiesOverrideState = _PmCapabilitiesOverrideState_Object(
    (1, 3, 6, 1, 2, 1, 124, 6, 1, 2),
    _PmCapabilitiesOverrideState_Type()
)
pmCapabilitiesOverrideState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmCapabilitiesOverrideState.setStatus("current")
_PmCapabilitiesOverrideRowStatus_Type = RowStatus
_PmCapabilitiesOverrideRowStatus_Object = MibTableColumn
pmCapabilitiesOverrideRowStatus = _PmCapabilitiesOverrideRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 6, 1, 3),
    _PmCapabilitiesOverrideRowStatus_Type()
)
pmCapabilitiesOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmCapabilitiesOverrideRowStatus.setStatus("current")


class _PmSchedLocalTime_Type(DateAndTime):
    """Custom type pmSchedLocalTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_PmSchedLocalTime_Type.__name__ = "DateAndTime"
_PmSchedLocalTime_Object = MibScalar
pmSchedLocalTime = _PmSchedLocalTime_Object(
    (1, 3, 6, 1, 2, 1, 124, 7),
    _PmSchedLocalTime_Type()
)
pmSchedLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmSchedLocalTime.setStatus("current")
_PmSchedTable_Object = MibTable
pmSchedTable = _PmSchedTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 8)
)
if mibBuilder.loadTexts:
    pmSchedTable.setStatus("current")
_PmSchedEntry_Object = MibTableRow
pmSchedEntry = _PmSchedEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1)
)
pmSchedEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmSchedIndex"),
)
if mibBuilder.loadTexts:
    pmSchedEntry.setStatus("current")


class _PmSchedIndex_Type(Unsigned32):
    """Custom type pmSchedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmSchedIndex_Type.__name__ = "Unsigned32"
_PmSchedIndex_Object = MibTableColumn
pmSchedIndex = _PmSchedIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 1),
    _PmSchedIndex_Type()
)
pmSchedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmSchedIndex.setStatus("current")


class _PmSchedGroupIndex_Type(Unsigned32):
    """Custom type pmSchedGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmSchedGroupIndex_Type.__name__ = "Unsigned32"
_PmSchedGroupIndex_Object = MibTableColumn
pmSchedGroupIndex = _PmSchedGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 2),
    _PmSchedGroupIndex_Type()
)
pmSchedGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedGroupIndex.setStatus("current")


class _PmSchedDescr_Type(PmUTF8String):
    """Custom type pmSchedDescr based on PmUTF8String"""
    defaultHexValue = ""


_PmSchedDescr_Object = MibTableColumn
pmSchedDescr = _PmSchedDescr_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 3),
    _PmSchedDescr_Type()
)
pmSchedDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedDescr.setStatus("current")


class _PmSchedTimePeriod_Type(PmUTF8String):
    """Custom type pmSchedTimePeriod based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PmSchedTimePeriod_Type.__name__ = "PmUTF8String"
_PmSchedTimePeriod_Object = MibTableColumn
pmSchedTimePeriod = _PmSchedTimePeriod_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 4),
    _PmSchedTimePeriod_Type()
)
pmSchedTimePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedTimePeriod.setStatus("current")


class _PmSchedMonth_Type(Bits):
    """Custom type pmSchedMonth based on Bits"""
    defaultBinValue = "111111111111"

    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )

_PmSchedMonth_Type.__name__ = "Bits"
_PmSchedMonth_Object = MibTableColumn
pmSchedMonth = _PmSchedMonth_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 5),
    _PmSchedMonth_Type()
)
pmSchedMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedMonth.setStatus("current")


class _PmSchedDay_Type(Bits):
    """Custom type pmSchedDay based on Bits"""
    defaultBinValue = "11111111111111111111111111111111111111111111111111111111111111"

    namedValues = NamedValues(
        *(("d1", 0),
          ("d10", 9),
          ("d11", 10),
          ("d12", 11),
          ("d13", 12),
          ("d14", 13),
          ("d15", 14),
          ("d16", 15),
          ("d17", 16),
          ("d18", 17),
          ("d19", 18),
          ("d2", 1),
          ("d20", 19),
          ("d21", 20),
          ("d22", 21),
          ("d23", 22),
          ("d24", 23),
          ("d25", 24),
          ("d26", 25),
          ("d27", 26),
          ("d28", 27),
          ("d29", 28),
          ("d3", 2),
          ("d30", 29),
          ("d31", 30),
          ("d4", 3),
          ("d5", 4),
          ("d6", 5),
          ("d7", 6),
          ("d8", 7),
          ("d9", 8),
          ("r1", 31),
          ("r10", 40),
          ("r11", 41),
          ("r12", 42),
          ("r13", 43),
          ("r14", 44),
          ("r15", 45),
          ("r16", 46),
          ("r17", 47),
          ("r18", 48),
          ("r19", 49),
          ("r2", 32),
          ("r20", 50),
          ("r21", 51),
          ("r22", 52),
          ("r23", 53),
          ("r24", 54),
          ("r25", 55),
          ("r26", 56),
          ("r27", 57),
          ("r28", 58),
          ("r29", 59),
          ("r3", 33),
          ("r30", 60),
          ("r31", 61),
          ("r4", 34),
          ("r5", 35),
          ("r6", 36),
          ("r7", 37),
          ("r8", 38),
          ("r9", 39))
    )

_PmSchedDay_Type.__name__ = "Bits"
_PmSchedDay_Object = MibTableColumn
pmSchedDay = _PmSchedDay_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 6),
    _PmSchedDay_Type()
)
pmSchedDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedDay.setStatus("current")


class _PmSchedWeekDay_Type(Bits):
    """Custom type pmSchedWeekDay based on Bits"""
    defaultBinValue = "1111111"

    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_PmSchedWeekDay_Type.__name__ = "Bits"
_PmSchedWeekDay_Object = MibTableColumn
pmSchedWeekDay = _PmSchedWeekDay_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 7),
    _PmSchedWeekDay_Type()
)
pmSchedWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedWeekDay.setStatus("current")


class _PmSchedTimeOfDay_Type(PmUTF8String):
    """Custom type pmSchedTimeOfDay based on PmUTF8String"""
    defaultHexValue = "543030303030302F54323335393539"

    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PmSchedTimeOfDay_Type.__name__ = "PmUTF8String"
_PmSchedTimeOfDay_Object = MibTableColumn
pmSchedTimeOfDay = _PmSchedTimeOfDay_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 8),
    _PmSchedTimeOfDay_Type()
)
pmSchedTimeOfDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedTimeOfDay.setStatus("current")


class _PmSchedLocalOrUtc_Type(Integer32):
    """Custom type pmSchedLocalOrUtc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTime", 1),
          ("utcTime", 2))
    )


_PmSchedLocalOrUtc_Type.__name__ = "Integer32"
_PmSchedLocalOrUtc_Object = MibTableColumn
pmSchedLocalOrUtc = _PmSchedLocalOrUtc_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 9),
    _PmSchedLocalOrUtc_Type()
)
pmSchedLocalOrUtc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedLocalOrUtc.setStatus("current")


class _PmSchedStorageType_Type(StorageType):
    """Custom type pmSchedStorageType based on StorageType"""


_PmSchedStorageType_Object = MibTableColumn
pmSchedStorageType = _PmSchedStorageType_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 10),
    _PmSchedStorageType_Type()
)
pmSchedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedStorageType.setStatus("current")
_PmSchedRowStatus_Type = RowStatus
_PmSchedRowStatus_Object = MibTableColumn
pmSchedRowStatus = _PmSchedRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 8, 1, 11),
    _PmSchedRowStatus_Type()
)
pmSchedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmSchedRowStatus.setStatus("current")
_PmTrackingPETable_Object = MibTable
pmTrackingPETable = _PmTrackingPETable_Object(
    (1, 3, 6, 1, 2, 1, 124, 9)
)
if mibBuilder.loadTexts:
    pmTrackingPETable.setStatus("current")
_PmTrackingPEEntry_Object = MibTableRow
pmTrackingPEEntry = _PmTrackingPEEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 9, 1)
)
pmTrackingPEEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyIndex"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingPEElement"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingPEContextName"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingPEContextEngineID"),
)
if mibBuilder.loadTexts:
    pmTrackingPEEntry.setStatus("current")
_PmTrackingPEElement_Type = RowPointer
_PmTrackingPEElement_Object = MibTableColumn
pmTrackingPEElement = _PmTrackingPEElement_Object(
    (1, 3, 6, 1, 2, 1, 124, 9, 1, 1),
    _PmTrackingPEElement_Type()
)
pmTrackingPEElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingPEElement.setStatus("current")


class _PmTrackingPEContextName_Type(SnmpAdminString):
    """Custom type pmTrackingPEContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmTrackingPEContextName_Type.__name__ = "SnmpAdminString"
_PmTrackingPEContextName_Object = MibTableColumn
pmTrackingPEContextName = _PmTrackingPEContextName_Object(
    (1, 3, 6, 1, 2, 1, 124, 9, 1, 2),
    _PmTrackingPEContextName_Type()
)
pmTrackingPEContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingPEContextName.setStatus("current")


class _PmTrackingPEContextEngineID_Type(OctetString):
    """Custom type pmTrackingPEContextEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_PmTrackingPEContextEngineID_Type.__name__ = "OctetString"
_PmTrackingPEContextEngineID_Object = MibTableColumn
pmTrackingPEContextEngineID = _PmTrackingPEContextEngineID_Object(
    (1, 3, 6, 1, 2, 1, 124, 9, 1, 3),
    _PmTrackingPEContextEngineID_Type()
)
pmTrackingPEContextEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingPEContextEngineID.setStatus("current")


class _PmTrackingPEInfo_Type(Bits):
    """Custom type pmTrackingPEInfo based on Bits"""
    namedValues = NamedValues(
        *(("actionRunTimeException", 3),
          ("actionSkippedDueToPrecedence", 0),
          ("actionUserSignal", 4),
          ("conditionRunTimeException", 1),
          ("conditionUserSignal", 2))
    )

_PmTrackingPEInfo_Type.__name__ = "Bits"
_PmTrackingPEInfo_Object = MibTableColumn
pmTrackingPEInfo = _PmTrackingPEInfo_Object(
    (1, 3, 6, 1, 2, 1, 124, 9, 1, 4),
    _PmTrackingPEInfo_Type()
)
pmTrackingPEInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTrackingPEInfo.setStatus("current")
_PmTrackingEPTable_Object = MibTable
pmTrackingEPTable = _PmTrackingEPTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 10)
)
if mibBuilder.loadTexts:
    pmTrackingEPTable.setStatus("current")
_PmTrackingEPEntry_Object = MibTableRow
pmTrackingEPEntry = _PmTrackingEPEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 10, 1)
)
pmTrackingEPEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingEPElement"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingEPContextName"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmTrackingEPContextEngineID"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyIndex"),
)
if mibBuilder.loadTexts:
    pmTrackingEPEntry.setStatus("current")
_PmTrackingEPElement_Type = RowPointer
_PmTrackingEPElement_Object = MibTableColumn
pmTrackingEPElement = _PmTrackingEPElement_Object(
    (1, 3, 6, 1, 2, 1, 124, 10, 1, 1),
    _PmTrackingEPElement_Type()
)
pmTrackingEPElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingEPElement.setStatus("current")


class _PmTrackingEPContextName_Type(SnmpAdminString):
    """Custom type pmTrackingEPContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmTrackingEPContextName_Type.__name__ = "SnmpAdminString"
_PmTrackingEPContextName_Object = MibTableColumn
pmTrackingEPContextName = _PmTrackingEPContextName_Object(
    (1, 3, 6, 1, 2, 1, 124, 10, 1, 2),
    _PmTrackingEPContextName_Type()
)
pmTrackingEPContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingEPContextName.setStatus("current")


class _PmTrackingEPContextEngineID_Type(OctetString):
    """Custom type pmTrackingEPContextEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_PmTrackingEPContextEngineID_Type.__name__ = "OctetString"
_PmTrackingEPContextEngineID_Object = MibTableColumn
pmTrackingEPContextEngineID = _PmTrackingEPContextEngineID_Object(
    (1, 3, 6, 1, 2, 1, 124, 10, 1, 3),
    _PmTrackingEPContextEngineID_Type()
)
pmTrackingEPContextEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTrackingEPContextEngineID.setStatus("current")


class _PmTrackingEPStatus_Type(Integer32):
    """Custom type pmTrackingEPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOff", 2),
          ("on", 1))
    )


_PmTrackingEPStatus_Type.__name__ = "Integer32"
_PmTrackingEPStatus_Object = MibTableColumn
pmTrackingEPStatus = _PmTrackingEPStatus_Object(
    (1, 3, 6, 1, 2, 1, 124, 10, 1, 4),
    _PmTrackingEPStatus_Type()
)
pmTrackingEPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTrackingEPStatus.setStatus("current")
_PmDebuggingTable_Object = MibTable
pmDebuggingTable = _PmDebuggingTable_Object(
    (1, 3, 6, 1, 2, 1, 124, 11)
)
if mibBuilder.loadTexts:
    pmDebuggingTable.setStatus("current")
_PmDebuggingEntry_Object = MibTableRow
pmDebuggingEntry = _PmDebuggingEntry_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1)
)
pmDebuggingEntry.setIndexNames(
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmPolicyIndex"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmDebuggingElement"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmDebuggingContextName"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmDebuggingContextEngineID"),
    (0, "POLICY-BASED-MANAGEMENT-MIB", "pmDebuggingLogIndex"),
)
if mibBuilder.loadTexts:
    pmDebuggingEntry.setStatus("current")
_PmDebuggingElement_Type = RowPointer
_PmDebuggingElement_Object = MibTableColumn
pmDebuggingElement = _PmDebuggingElement_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1, 1),
    _PmDebuggingElement_Type()
)
pmDebuggingElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDebuggingElement.setStatus("current")


class _PmDebuggingContextName_Type(SnmpAdminString):
    """Custom type pmDebuggingContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmDebuggingContextName_Type.__name__ = "SnmpAdminString"
_PmDebuggingContextName_Object = MibTableColumn
pmDebuggingContextName = _PmDebuggingContextName_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1, 2),
    _PmDebuggingContextName_Type()
)
pmDebuggingContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDebuggingContextName.setStatus("current")


class _PmDebuggingContextEngineID_Type(OctetString):
    """Custom type pmDebuggingContextEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_PmDebuggingContextEngineID_Type.__name__ = "OctetString"
_PmDebuggingContextEngineID_Object = MibTableColumn
pmDebuggingContextEngineID = _PmDebuggingContextEngineID_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1, 3),
    _PmDebuggingContextEngineID_Type()
)
pmDebuggingContextEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDebuggingContextEngineID.setStatus("current")


class _PmDebuggingLogIndex_Type(Unsigned32):
    """Custom type pmDebuggingLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PmDebuggingLogIndex_Type.__name__ = "Unsigned32"
_PmDebuggingLogIndex_Object = MibTableColumn
pmDebuggingLogIndex = _PmDebuggingLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1, 4),
    _PmDebuggingLogIndex_Type()
)
pmDebuggingLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDebuggingLogIndex.setStatus("current")


class _PmDebuggingMessage_Type(PmUTF8String):
    """Custom type pmDebuggingMessage based on PmUTF8String"""
    subtypeSpec = PmUTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PmDebuggingMessage_Type.__name__ = "PmUTF8String"
_PmDebuggingMessage_Object = MibTableColumn
pmDebuggingMessage = _PmDebuggingMessage_Object(
    (1, 3, 6, 1, 2, 1, 124, 11, 1, 5),
    _PmDebuggingMessage_Type()
)
pmDebuggingMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDebuggingMessage.setStatus("current")
_PmConformance_ObjectIdentity = ObjectIdentity
pmConformance = _PmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 124, 12)
)
_PmCompliances_ObjectIdentity = ObjectIdentity
pmCompliances = _PmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 124, 12, 1)
)
_PmGroups_ObjectIdentity = ObjectIdentity
pmGroups = _PmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 124, 12, 2)
)
_PmBaseFunctionLibrary_ObjectIdentity = ObjectIdentity
pmBaseFunctionLibrary = _PmBaseFunctionLibrary_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 124, 12, 2, 4)
)

# Managed Objects groups

pmPolicyManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 124, 12, 2, 1)
)
pmPolicyManagementGroup.setObjects(
      *(("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyPrecedenceGroup"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyPrecedence"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicySchedule"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyElementTypeFilter"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyConditionScriptIndex"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyActionScriptIndex"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyParameters"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyConditionMaxLatency"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyActionMaxLatency"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyMaxIterations"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyDescription"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyMatches"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyAbnormalTerminations"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyExecutionErrors"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyDebugging"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyStorageType"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyAdminStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyRowStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyCodeText"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmPolicyCodeStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmElementTypeRegMaxLatency"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmElementTypeRegDescription"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmElementTypeRegStorageType"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmElementTypeRegRowStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmRoleStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesType"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesOverrideState"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesOverrideRowStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmTrackingPEInfo"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmTrackingEPStatus"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmDebuggingMessage"))
)
if mibBuilder.loadTexts:
    pmPolicyManagementGroup.setStatus("current")

pmSchedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 124, 12, 2, 2)
)
pmSchedGroup.setObjects(
      *(("POLICY-BASED-MANAGEMENT-MIB", "pmSchedLocalTime"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedGroupIndex"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedDescr"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedTimePeriod"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedMonth"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedDay"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedWeekDay"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedTimeOfDay"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedLocalOrUtc"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedStorageType"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmSchedRowStatus"))
)
if mibBuilder.loadTexts:
    pmSchedGroup.setStatus("current")


# Notification objects

pmNewRoleNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 124, 0, 1)
)
pmNewRoleNotification.setObjects(
    ("POLICY-BASED-MANAGEMENT-MIB", "pmRoleStatus")
)
if mibBuilder.loadTexts:
    pmNewRoleNotification.setStatus(
        "current"
    )

pmNewCapabilityNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 124, 0, 2)
)
pmNewCapabilityNotification.setObjects(
    ("POLICY-BASED-MANAGEMENT-MIB", "pmCapabilitiesType")
)
if mibBuilder.loadTexts:
    pmNewCapabilityNotification.setStatus(
        "current"
    )

pmAbnormalTermNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 124, 0, 3)
)
pmAbnormalTermNotification.setObjects(
    ("POLICY-BASED-MANAGEMENT-MIB", "pmTrackingPEInfo")
)
if mibBuilder.loadTexts:
    pmAbnormalTermNotification.setStatus(
        "current"
    )


# Notifications groups

pmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 124, 12, 2, 3)
)
pmNotificationGroup.setObjects(
      *(("POLICY-BASED-MANAGEMENT-MIB", "pmNewRoleNotification"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmNewCapabilityNotification"),
        ("POLICY-BASED-MANAGEMENT-MIB", "pmAbnormalTermNotification"))
)
if mibBuilder.loadTexts:
    pmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 124, 12, 1, 1)
)
if mibBuilder.loadTexts:
    pmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-BASED-MANAGEMENT-MIB",
    **{"PmUTF8String": PmUTF8String,
       "pmMib": pmMib,
       "pmNotifications": pmNotifications,
       "pmNewRoleNotification": pmNewRoleNotification,
       "pmNewCapabilityNotification": pmNewCapabilityNotification,
       "pmAbnormalTermNotification": pmAbnormalTermNotification,
       "pmPolicyTable": pmPolicyTable,
       "pmPolicyEntry": pmPolicyEntry,
       "pmPolicyAdminGroup": pmPolicyAdminGroup,
       "pmPolicyIndex": pmPolicyIndex,
       "pmPolicyPrecedenceGroup": pmPolicyPrecedenceGroup,
       "pmPolicyPrecedence": pmPolicyPrecedence,
       "pmPolicySchedule": pmPolicySchedule,
       "pmPolicyElementTypeFilter": pmPolicyElementTypeFilter,
       "pmPolicyConditionScriptIndex": pmPolicyConditionScriptIndex,
       "pmPolicyActionScriptIndex": pmPolicyActionScriptIndex,
       "pmPolicyParameters": pmPolicyParameters,
       "pmPolicyConditionMaxLatency": pmPolicyConditionMaxLatency,
       "pmPolicyActionMaxLatency": pmPolicyActionMaxLatency,
       "pmPolicyMaxIterations": pmPolicyMaxIterations,
       "pmPolicyDescription": pmPolicyDescription,
       "pmPolicyMatches": pmPolicyMatches,
       "pmPolicyAbnormalTerminations": pmPolicyAbnormalTerminations,
       "pmPolicyExecutionErrors": pmPolicyExecutionErrors,
       "pmPolicyDebugging": pmPolicyDebugging,
       "pmPolicyAdminStatus": pmPolicyAdminStatus,
       "pmPolicyStorageType": pmPolicyStorageType,
       "pmPolicyRowStatus": pmPolicyRowStatus,
       "pmPolicyCodeTable": pmPolicyCodeTable,
       "pmPolicyCodeEntry": pmPolicyCodeEntry,
       "pmPolicyCodeScriptIndex": pmPolicyCodeScriptIndex,
       "pmPolicyCodeSegment": pmPolicyCodeSegment,
       "pmPolicyCodeText": pmPolicyCodeText,
       "pmPolicyCodeStatus": pmPolicyCodeStatus,
       "pmElementTypeRegTable": pmElementTypeRegTable,
       "pmElementTypeRegEntry": pmElementTypeRegEntry,
       "pmElementTypeRegOIDPrefix": pmElementTypeRegOIDPrefix,
       "pmElementTypeRegMaxLatency": pmElementTypeRegMaxLatency,
       "pmElementTypeRegDescription": pmElementTypeRegDescription,
       "pmElementTypeRegStorageType": pmElementTypeRegStorageType,
       "pmElementTypeRegRowStatus": pmElementTypeRegRowStatus,
       "pmRoleTable": pmRoleTable,
       "pmRoleEntry": pmRoleEntry,
       "pmRoleElement": pmRoleElement,
       "pmRoleContextName": pmRoleContextName,
       "pmRoleContextEngineID": pmRoleContextEngineID,
       "pmRoleString": pmRoleString,
       "pmRoleStatus": pmRoleStatus,
       "pmCapabilitiesTable": pmCapabilitiesTable,
       "pmCapabilitiesEntry": pmCapabilitiesEntry,
       "pmCapabilitiesType": pmCapabilitiesType,
       "pmCapabilitiesOverrideTable": pmCapabilitiesOverrideTable,
       "pmCapabilitiesOverrideEntry": pmCapabilitiesOverrideEntry,
       "pmCapabilitiesOverrideType": pmCapabilitiesOverrideType,
       "pmCapabilitiesOverrideState": pmCapabilitiesOverrideState,
       "pmCapabilitiesOverrideRowStatus": pmCapabilitiesOverrideRowStatus,
       "pmSchedLocalTime": pmSchedLocalTime,
       "pmSchedTable": pmSchedTable,
       "pmSchedEntry": pmSchedEntry,
       "pmSchedIndex": pmSchedIndex,
       "pmSchedGroupIndex": pmSchedGroupIndex,
       "pmSchedDescr": pmSchedDescr,
       "pmSchedTimePeriod": pmSchedTimePeriod,
       "pmSchedMonth": pmSchedMonth,
       "pmSchedDay": pmSchedDay,
       "pmSchedWeekDay": pmSchedWeekDay,
       "pmSchedTimeOfDay": pmSchedTimeOfDay,
       "pmSchedLocalOrUtc": pmSchedLocalOrUtc,
       "pmSchedStorageType": pmSchedStorageType,
       "pmSchedRowStatus": pmSchedRowStatus,
       "pmTrackingPETable": pmTrackingPETable,
       "pmTrackingPEEntry": pmTrackingPEEntry,
       "pmTrackingPEElement": pmTrackingPEElement,
       "pmTrackingPEContextName": pmTrackingPEContextName,
       "pmTrackingPEContextEngineID": pmTrackingPEContextEngineID,
       "pmTrackingPEInfo": pmTrackingPEInfo,
       "pmTrackingEPTable": pmTrackingEPTable,
       "pmTrackingEPEntry": pmTrackingEPEntry,
       "pmTrackingEPElement": pmTrackingEPElement,
       "pmTrackingEPContextName": pmTrackingEPContextName,
       "pmTrackingEPContextEngineID": pmTrackingEPContextEngineID,
       "pmTrackingEPStatus": pmTrackingEPStatus,
       "pmDebuggingTable": pmDebuggingTable,
       "pmDebuggingEntry": pmDebuggingEntry,
       "pmDebuggingElement": pmDebuggingElement,
       "pmDebuggingContextName": pmDebuggingContextName,
       "pmDebuggingContextEngineID": pmDebuggingContextEngineID,
       "pmDebuggingLogIndex": pmDebuggingLogIndex,
       "pmDebuggingMessage": pmDebuggingMessage,
       "pmConformance": pmConformance,
       "pmCompliances": pmCompliances,
       "pmCompliance": pmCompliance,
       "pmGroups": pmGroups,
       "pmPolicyManagementGroup": pmPolicyManagementGroup,
       "pmSchedGroup": pmSchedGroup,
       "pmNotificationGroup": pmNotificationGroup,
       "pmBaseFunctionLibrary": pmBaseFunctionLibrary}
)
