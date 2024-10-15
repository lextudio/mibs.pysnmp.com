# SNMP MIB module (IPSEC-SPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-SPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:10 2024
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

(IfDirection,
 diffServMIBMultiFieldClfrGroup,
 diffServMultiFieldClfrNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IfDirection",
    "diffServMIBMultiFieldClfrGroup",
    "diffServMultiFieldClfrNextFree")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

spdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 153)
)
spdMIB.setRevisions(
        ("2007-02-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SpdBooleanOperator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 2),
          ("or", 1))
    )



class SpdAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class SpdIPPacketLogging(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class SpdTimePeriod(OctetString, TextualConvention):
    status = "current"
    displayHint = "31t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



# MIB Managed Objects in the order of their OIDs

_SpdConfigObjects_ObjectIdentity = ObjectIdentity
spdConfigObjects = _SpdConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1)
)
_SpdLocalConfigObjects_ObjectIdentity = ObjectIdentity
spdLocalConfigObjects = _SpdLocalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 1)
)


class _SpdIngressPolicyGroupName_Type(SnmpAdminString):
    """Custom type spdIngressPolicyGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpdIngressPolicyGroupName_Type.__name__ = "SnmpAdminString"
_SpdIngressPolicyGroupName_Object = MibScalar
spdIngressPolicyGroupName = _SpdIngressPolicyGroupName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 1, 1),
    _SpdIngressPolicyGroupName_Type()
)
spdIngressPolicyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spdIngressPolicyGroupName.setStatus("current")


class _SpdEgressPolicyGroupName_Type(SnmpAdminString):
    """Custom type spdEgressPolicyGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpdEgressPolicyGroupName_Type.__name__ = "SnmpAdminString"
_SpdEgressPolicyGroupName_Object = MibScalar
spdEgressPolicyGroupName = _SpdEgressPolicyGroupName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 1, 2),
    _SpdEgressPolicyGroupName_Type()
)
spdEgressPolicyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spdEgressPolicyGroupName.setStatus("current")
_SpdEndpointToGroupTable_Object = MibTable
spdEndpointToGroupTable = _SpdEndpointToGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2)
)
if mibBuilder.loadTexts:
    spdEndpointToGroupTable.setStatus("current")
_SpdEndpointToGroupEntry_Object = MibTableRow
spdEndpointToGroupEntry = _SpdEndpointToGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1)
)
spdEndpointToGroupEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdEndGroupDirection"),
    (0, "IPSEC-SPD-MIB", "spdEndGroupInterface"),
)
if mibBuilder.loadTexts:
    spdEndpointToGroupEntry.setStatus("current")
_SpdEndGroupDirection_Type = IfDirection
_SpdEndGroupDirection_Object = MibTableColumn
spdEndGroupDirection = _SpdEndGroupDirection_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 1),
    _SpdEndGroupDirection_Type()
)
spdEndGroupDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdEndGroupDirection.setStatus("current")
_SpdEndGroupInterface_Type = InterfaceIndex
_SpdEndGroupInterface_Object = MibTableColumn
spdEndGroupInterface = _SpdEndGroupInterface_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 2),
    _SpdEndGroupInterface_Type()
)
spdEndGroupInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdEndGroupInterface.setStatus("current")


class _SpdEndGroupName_Type(SnmpAdminString):
    """Custom type spdEndGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdEndGroupName_Type.__name__ = "SnmpAdminString"
_SpdEndGroupName_Object = MibTableColumn
spdEndGroupName = _SpdEndGroupName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 3),
    _SpdEndGroupName_Type()
)
spdEndGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdEndGroupName.setStatus("current")
_SpdEndGroupLastChanged_Type = TimeStamp
_SpdEndGroupLastChanged_Object = MibTableColumn
spdEndGroupLastChanged = _SpdEndGroupLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 4),
    _SpdEndGroupLastChanged_Type()
)
spdEndGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdEndGroupLastChanged.setStatus("current")


class _SpdEndGroupStorageType_Type(StorageType):
    """Custom type spdEndGroupStorageType based on StorageType"""


_SpdEndGroupStorageType_Object = MibTableColumn
spdEndGroupStorageType = _SpdEndGroupStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 5),
    _SpdEndGroupStorageType_Type()
)
spdEndGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdEndGroupStorageType.setStatus("current")
_SpdEndGroupRowStatus_Type = RowStatus
_SpdEndGroupRowStatus_Object = MibTableColumn
spdEndGroupRowStatus = _SpdEndGroupRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 6),
    _SpdEndGroupRowStatus_Type()
)
spdEndGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdEndGroupRowStatus.setStatus("current")
_SpdGroupContentsTable_Object = MibTable
spdGroupContentsTable = _SpdGroupContentsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3)
)
if mibBuilder.loadTexts:
    spdGroupContentsTable.setStatus("current")
_SpdGroupContentsEntry_Object = MibTableRow
spdGroupContentsEntry = _SpdGroupContentsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1)
)
spdGroupContentsEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdGroupContName"),
    (0, "IPSEC-SPD-MIB", "spdGroupContPriority"),
)
if mibBuilder.loadTexts:
    spdGroupContentsEntry.setStatus("current")


class _SpdGroupContName_Type(SnmpAdminString):
    """Custom type spdGroupContName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdGroupContName_Type.__name__ = "SnmpAdminString"
_SpdGroupContName_Object = MibTableColumn
spdGroupContName = _SpdGroupContName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 1),
    _SpdGroupContName_Type()
)
spdGroupContName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdGroupContName.setStatus("current")


class _SpdGroupContPriority_Type(Integer32):
    """Custom type spdGroupContPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpdGroupContPriority_Type.__name__ = "Integer32"
_SpdGroupContPriority_Object = MibTableColumn
spdGroupContPriority = _SpdGroupContPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 2),
    _SpdGroupContPriority_Type()
)
spdGroupContPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdGroupContPriority.setStatus("current")


class _SpdGroupContFilter_Type(VariablePointer):
    """Custom type spdGroupContFilter based on VariablePointer"""
    defaultValue = (1, 3, 6, 1, 2, 1, 153, 1, 7, 1, 0)


_SpdGroupContFilter_Object = MibTableColumn
spdGroupContFilter = _SpdGroupContFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 3),
    _SpdGroupContFilter_Type()
)
spdGroupContFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdGroupContFilter.setStatus("current")


class _SpdGroupContComponentType_Type(Integer32):
    """Custom type spdGroupContComponentType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("rule", 2))
    )


_SpdGroupContComponentType_Type.__name__ = "Integer32"
_SpdGroupContComponentType_Object = MibTableColumn
spdGroupContComponentType = _SpdGroupContComponentType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 4),
    _SpdGroupContComponentType_Type()
)
spdGroupContComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdGroupContComponentType.setStatus("current")


class _SpdGroupContComponentName_Type(SnmpAdminString):
    """Custom type spdGroupContComponentName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdGroupContComponentName_Type.__name__ = "SnmpAdminString"
_SpdGroupContComponentName_Object = MibTableColumn
spdGroupContComponentName = _SpdGroupContComponentName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 5),
    _SpdGroupContComponentName_Type()
)
spdGroupContComponentName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdGroupContComponentName.setStatus("current")
_SpdGroupContLastChanged_Type = TimeStamp
_SpdGroupContLastChanged_Object = MibTableColumn
spdGroupContLastChanged = _SpdGroupContLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 6),
    _SpdGroupContLastChanged_Type()
)
spdGroupContLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdGroupContLastChanged.setStatus("current")


class _SpdGroupContStorageType_Type(StorageType):
    """Custom type spdGroupContStorageType based on StorageType"""


_SpdGroupContStorageType_Object = MibTableColumn
spdGroupContStorageType = _SpdGroupContStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 7),
    _SpdGroupContStorageType_Type()
)
spdGroupContStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdGroupContStorageType.setStatus("current")
_SpdGroupContRowStatus_Type = RowStatus
_SpdGroupContRowStatus_Object = MibTableColumn
spdGroupContRowStatus = _SpdGroupContRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 8),
    _SpdGroupContRowStatus_Type()
)
spdGroupContRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdGroupContRowStatus.setStatus("current")
_SpdRuleDefinitionTable_Object = MibTable
spdRuleDefinitionTable = _SpdRuleDefinitionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4)
)
if mibBuilder.loadTexts:
    spdRuleDefinitionTable.setStatus("current")
_SpdRuleDefinitionEntry_Object = MibTableRow
spdRuleDefinitionEntry = _SpdRuleDefinitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1)
)
spdRuleDefinitionEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdRuleDefName"),
)
if mibBuilder.loadTexts:
    spdRuleDefinitionEntry.setStatus("current")


class _SpdRuleDefName_Type(SnmpAdminString):
    """Custom type spdRuleDefName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdRuleDefName_Type.__name__ = "SnmpAdminString"
_SpdRuleDefName_Object = MibTableColumn
spdRuleDefName = _SpdRuleDefName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 1),
    _SpdRuleDefName_Type()
)
spdRuleDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdRuleDefName.setStatus("current")
_SpdRuleDefDescription_Type = SnmpAdminString
_SpdRuleDefDescription_Object = MibTableColumn
spdRuleDefDescription = _SpdRuleDefDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 2),
    _SpdRuleDefDescription_Type()
)
spdRuleDefDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefDescription.setStatus("current")
_SpdRuleDefFilter_Type = VariablePointer
_SpdRuleDefFilter_Object = MibTableColumn
spdRuleDefFilter = _SpdRuleDefFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 3),
    _SpdRuleDefFilter_Type()
)
spdRuleDefFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefFilter.setStatus("current")


class _SpdRuleDefFilterNegated_Type(TruthValue):
    """Custom type spdRuleDefFilterNegated based on TruthValue"""


_SpdRuleDefFilterNegated_Object = MibTableColumn
spdRuleDefFilterNegated = _SpdRuleDefFilterNegated_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 4),
    _SpdRuleDefFilterNegated_Type()
)
spdRuleDefFilterNegated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefFilterNegated.setStatus("current")
_SpdRuleDefAction_Type = VariablePointer
_SpdRuleDefAction_Object = MibTableColumn
spdRuleDefAction = _SpdRuleDefAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 5),
    _SpdRuleDefAction_Type()
)
spdRuleDefAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefAction.setStatus("current")


class _SpdRuleDefAdminStatus_Type(SpdAdminStatus):
    """Custom type spdRuleDefAdminStatus based on SpdAdminStatus"""


_SpdRuleDefAdminStatus_Object = MibTableColumn
spdRuleDefAdminStatus = _SpdRuleDefAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 6),
    _SpdRuleDefAdminStatus_Type()
)
spdRuleDefAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefAdminStatus.setStatus("current")
_SpdRuleDefLastChanged_Type = TimeStamp
_SpdRuleDefLastChanged_Object = MibTableColumn
spdRuleDefLastChanged = _SpdRuleDefLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 7),
    _SpdRuleDefLastChanged_Type()
)
spdRuleDefLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdRuleDefLastChanged.setStatus("current")


class _SpdRuleDefStorageType_Type(StorageType):
    """Custom type spdRuleDefStorageType based on StorageType"""


_SpdRuleDefStorageType_Object = MibTableColumn
spdRuleDefStorageType = _SpdRuleDefStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 8),
    _SpdRuleDefStorageType_Type()
)
spdRuleDefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefStorageType.setStatus("current")
_SpdRuleDefRowStatus_Type = RowStatus
_SpdRuleDefRowStatus_Object = MibTableColumn
spdRuleDefRowStatus = _SpdRuleDefRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 9),
    _SpdRuleDefRowStatus_Type()
)
spdRuleDefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdRuleDefRowStatus.setStatus("current")
_SpdCompoundFilterTable_Object = MibTable
spdCompoundFilterTable = _SpdCompoundFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5)
)
if mibBuilder.loadTexts:
    spdCompoundFilterTable.setStatus("current")
_SpdCompoundFilterEntry_Object = MibTableRow
spdCompoundFilterEntry = _SpdCompoundFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1)
)
spdCompoundFilterEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdCompFiltName"),
)
if mibBuilder.loadTexts:
    spdCompoundFilterEntry.setStatus("current")


class _SpdCompFiltName_Type(SnmpAdminString):
    """Custom type spdCompFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdCompFiltName_Type.__name__ = "SnmpAdminString"
_SpdCompFiltName_Object = MibTableColumn
spdCompFiltName = _SpdCompFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 1),
    _SpdCompFiltName_Type()
)
spdCompFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdCompFiltName.setStatus("current")
_SpdCompFiltDescription_Type = SnmpAdminString
_SpdCompFiltDescription_Object = MibTableColumn
spdCompFiltDescription = _SpdCompFiltDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 2),
    _SpdCompFiltDescription_Type()
)
spdCompFiltDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompFiltDescription.setStatus("current")


class _SpdCompFiltLogicType_Type(SpdBooleanOperator):
    """Custom type spdCompFiltLogicType based on SpdBooleanOperator"""


_SpdCompFiltLogicType_Object = MibTableColumn
spdCompFiltLogicType = _SpdCompFiltLogicType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 3),
    _SpdCompFiltLogicType_Type()
)
spdCompFiltLogicType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompFiltLogicType.setStatus("current")
_SpdCompFiltLastChanged_Type = TimeStamp
_SpdCompFiltLastChanged_Object = MibTableColumn
spdCompFiltLastChanged = _SpdCompFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 4),
    _SpdCompFiltLastChanged_Type()
)
spdCompFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdCompFiltLastChanged.setStatus("current")


class _SpdCompFiltStorageType_Type(StorageType):
    """Custom type spdCompFiltStorageType based on StorageType"""


_SpdCompFiltStorageType_Object = MibTableColumn
spdCompFiltStorageType = _SpdCompFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 5),
    _SpdCompFiltStorageType_Type()
)
spdCompFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompFiltStorageType.setStatus("current")
_SpdCompFiltRowStatus_Type = RowStatus
_SpdCompFiltRowStatus_Object = MibTableColumn
spdCompFiltRowStatus = _SpdCompFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 6),
    _SpdCompFiltRowStatus_Type()
)
spdCompFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompFiltRowStatus.setStatus("current")
_SpdSubfiltersTable_Object = MibTable
spdSubfiltersTable = _SpdSubfiltersTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6)
)
if mibBuilder.loadTexts:
    spdSubfiltersTable.setStatus("current")
_SpdSubfiltersEntry_Object = MibTableRow
spdSubfiltersEntry = _SpdSubfiltersEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1)
)
spdSubfiltersEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdCompFiltName"),
    (0, "IPSEC-SPD-MIB", "spdSubFiltPriority"),
)
if mibBuilder.loadTexts:
    spdSubfiltersEntry.setStatus("current")


class _SpdSubFiltPriority_Type(Integer32):
    """Custom type spdSubFiltPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpdSubFiltPriority_Type.__name__ = "Integer32"
_SpdSubFiltPriority_Object = MibTableColumn
spdSubFiltPriority = _SpdSubFiltPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 1),
    _SpdSubFiltPriority_Type()
)
spdSubFiltPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdSubFiltPriority.setStatus("current")
_SpdSubFiltSubfilter_Type = VariablePointer
_SpdSubFiltSubfilter_Object = MibTableColumn
spdSubFiltSubfilter = _SpdSubFiltSubfilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 2),
    _SpdSubFiltSubfilter_Type()
)
spdSubFiltSubfilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubFiltSubfilter.setStatus("current")


class _SpdSubFiltSubfilterIsNegated_Type(TruthValue):
    """Custom type spdSubFiltSubfilterIsNegated based on TruthValue"""


_SpdSubFiltSubfilterIsNegated_Object = MibTableColumn
spdSubFiltSubfilterIsNegated = _SpdSubFiltSubfilterIsNegated_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 3),
    _SpdSubFiltSubfilterIsNegated_Type()
)
spdSubFiltSubfilterIsNegated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubFiltSubfilterIsNegated.setStatus("current")
_SpdSubFiltLastChanged_Type = TimeStamp
_SpdSubFiltLastChanged_Object = MibTableColumn
spdSubFiltLastChanged = _SpdSubFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 4),
    _SpdSubFiltLastChanged_Type()
)
spdSubFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdSubFiltLastChanged.setStatus("current")


class _SpdSubFiltStorageType_Type(StorageType):
    """Custom type spdSubFiltStorageType based on StorageType"""


_SpdSubFiltStorageType_Object = MibTableColumn
spdSubFiltStorageType = _SpdSubFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 5),
    _SpdSubFiltStorageType_Type()
)
spdSubFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubFiltStorageType.setStatus("current")
_SpdSubFiltRowStatus_Type = RowStatus
_SpdSubFiltRowStatus_Object = MibTableColumn
spdSubFiltRowStatus = _SpdSubFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 6),
    _SpdSubFiltRowStatus_Type()
)
spdSubFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubFiltRowStatus.setStatus("current")
_SpdStaticFilters_ObjectIdentity = ObjectIdentity
spdStaticFilters = _SpdStaticFilters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 7)
)


class _SpdTrueFilter_Type(Integer32):
    """Custom type spdTrueFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpdTrueFilter_Type.__name__ = "Integer32"
_SpdTrueFilter_Object = MibScalar
spdTrueFilter = _SpdTrueFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 1),
    _SpdTrueFilter_Type()
)
spdTrueFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdTrueFilter.setStatus("current")
_SpdTrueFilterInstance_ObjectIdentity = ObjectIdentity
spdTrueFilterInstance = _SpdTrueFilterInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 1, 0)
)
_SpdIpOffsetFilterTable_Object = MibTable
spdIpOffsetFilterTable = _SpdIpOffsetFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8)
)
if mibBuilder.loadTexts:
    spdIpOffsetFilterTable.setStatus("current")
_SpdIpOffsetFilterEntry_Object = MibTableRow
spdIpOffsetFilterEntry = _SpdIpOffsetFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1)
)
spdIpOffsetFilterEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdIpOffFiltName"),
)
if mibBuilder.loadTexts:
    spdIpOffsetFilterEntry.setStatus("current")


class _SpdIpOffFiltName_Type(SnmpAdminString):
    """Custom type spdIpOffFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdIpOffFiltName_Type.__name__ = "SnmpAdminString"
_SpdIpOffFiltName_Object = MibTableColumn
spdIpOffFiltName = _SpdIpOffFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 1),
    _SpdIpOffFiltName_Type()
)
spdIpOffFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdIpOffFiltName.setStatus("current")


class _SpdIpOffFiltOffset_Type(Unsigned32):
    """Custom type spdIpOffFiltOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpdIpOffFiltOffset_Type.__name__ = "Unsigned32"
_SpdIpOffFiltOffset_Object = MibTableColumn
spdIpOffFiltOffset = _SpdIpOffFiltOffset_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 2),
    _SpdIpOffFiltOffset_Type()
)
spdIpOffFiltOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpOffFiltOffset.setStatus("current")


class _SpdIpOffFiltType_Type(Integer32):
    """Custom type spdIpOffFiltType based on Integer32"""
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
        *(("arithmeticGreater", 5),
          ("arithmeticGreaterOrEqual", 4),
          ("arithmeticLess", 3),
          ("arithmeticLessOrEqual", 6),
          ("equal", 1),
          ("notEqual", 2))
    )


_SpdIpOffFiltType_Type.__name__ = "Integer32"
_SpdIpOffFiltType_Object = MibTableColumn
spdIpOffFiltType = _SpdIpOffFiltType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 3),
    _SpdIpOffFiltType_Type()
)
spdIpOffFiltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpOffFiltType.setStatus("current")


class _SpdIpOffFiltValue_Type(OctetString):
    """Custom type spdIpOffFiltValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_SpdIpOffFiltValue_Type.__name__ = "OctetString"
_SpdIpOffFiltValue_Object = MibTableColumn
spdIpOffFiltValue = _SpdIpOffFiltValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 4),
    _SpdIpOffFiltValue_Type()
)
spdIpOffFiltValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpOffFiltValue.setStatus("current")
_SpdIpOffFiltLastChanged_Type = TimeStamp
_SpdIpOffFiltLastChanged_Object = MibTableColumn
spdIpOffFiltLastChanged = _SpdIpOffFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 5),
    _SpdIpOffFiltLastChanged_Type()
)
spdIpOffFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdIpOffFiltLastChanged.setStatus("current")


class _SpdIpOffFiltStorageType_Type(StorageType):
    """Custom type spdIpOffFiltStorageType based on StorageType"""


_SpdIpOffFiltStorageType_Object = MibTableColumn
spdIpOffFiltStorageType = _SpdIpOffFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 6),
    _SpdIpOffFiltStorageType_Type()
)
spdIpOffFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpOffFiltStorageType.setStatus("current")
_SpdIpOffFiltRowStatus_Type = RowStatus
_SpdIpOffFiltRowStatus_Object = MibTableColumn
spdIpOffFiltRowStatus = _SpdIpOffFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 7),
    _SpdIpOffFiltRowStatus_Type()
)
spdIpOffFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpOffFiltRowStatus.setStatus("current")
_SpdTimeFilterTable_Object = MibTable
spdTimeFilterTable = _SpdTimeFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9)
)
if mibBuilder.loadTexts:
    spdTimeFilterTable.setStatus("current")
_SpdTimeFilterEntry_Object = MibTableRow
spdTimeFilterEntry = _SpdTimeFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1)
)
spdTimeFilterEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdTimeFiltName"),
)
if mibBuilder.loadTexts:
    spdTimeFilterEntry.setStatus("current")


class _SpdTimeFiltName_Type(SnmpAdminString):
    """Custom type spdTimeFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdTimeFiltName_Type.__name__ = "SnmpAdminString"
_SpdTimeFiltName_Object = MibTableColumn
spdTimeFiltName = _SpdTimeFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 1),
    _SpdTimeFiltName_Type()
)
spdTimeFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdTimeFiltName.setStatus("current")


class _SpdTimeFiltPeriod_Type(SpdTimePeriod):
    """Custom type spdTimeFiltPeriod based on SpdTimePeriod"""
    defaultValue = OctetString("THISANDPRIOR/THISANDFUTURE")


_SpdTimeFiltPeriod_Object = MibTableColumn
spdTimeFiltPeriod = _SpdTimeFiltPeriod_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 2),
    _SpdTimeFiltPeriod_Type()
)
spdTimeFiltPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltPeriod.setStatus("current")


class _SpdTimeFiltMonthOfYearMask_Type(Bits):
    """Custom type spdTimeFiltMonthOfYearMask based on Bits"""
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

_SpdTimeFiltMonthOfYearMask_Type.__name__ = "Bits"
_SpdTimeFiltMonthOfYearMask_Object = MibTableColumn
spdTimeFiltMonthOfYearMask = _SpdTimeFiltMonthOfYearMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 3),
    _SpdTimeFiltMonthOfYearMask_Type()
)
spdTimeFiltMonthOfYearMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltMonthOfYearMask.setStatus("current")


class _SpdTimeFiltDayOfMonthMask_Type(OctetString):
    """Custom type spdTimeFiltDayOfMonthMask based on OctetString"""
    defaultHexValue = "fffffffffffffffe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SpdTimeFiltDayOfMonthMask_Type.__name__ = "OctetString"
_SpdTimeFiltDayOfMonthMask_Object = MibTableColumn
spdTimeFiltDayOfMonthMask = _SpdTimeFiltDayOfMonthMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 4),
    _SpdTimeFiltDayOfMonthMask_Type()
)
spdTimeFiltDayOfMonthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltDayOfMonthMask.setStatus("current")


class _SpdTimeFiltDayOfWeekMask_Type(Bits):
    """Custom type spdTimeFiltDayOfWeekMask based on Bits"""
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

_SpdTimeFiltDayOfWeekMask_Type.__name__ = "Bits"
_SpdTimeFiltDayOfWeekMask_Object = MibTableColumn
spdTimeFiltDayOfWeekMask = _SpdTimeFiltDayOfWeekMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 5),
    _SpdTimeFiltDayOfWeekMask_Type()
)
spdTimeFiltDayOfWeekMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltDayOfWeekMask.setStatus("current")


class _SpdTimeFiltTimeOfDayMask_Type(SpdTimePeriod):
    """Custom type spdTimeFiltTimeOfDayMask based on SpdTimePeriod"""
    defaultValue = OctetString("00000000T000000/00000000T240000")


_SpdTimeFiltTimeOfDayMask_Object = MibTableColumn
spdTimeFiltTimeOfDayMask = _SpdTimeFiltTimeOfDayMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 6),
    _SpdTimeFiltTimeOfDayMask_Type()
)
spdTimeFiltTimeOfDayMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltTimeOfDayMask.setStatus("current")
_SpdTimeFiltLastChanged_Type = TimeStamp
_SpdTimeFiltLastChanged_Object = MibTableColumn
spdTimeFiltLastChanged = _SpdTimeFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 7),
    _SpdTimeFiltLastChanged_Type()
)
spdTimeFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdTimeFiltLastChanged.setStatus("current")


class _SpdTimeFiltStorageType_Type(StorageType):
    """Custom type spdTimeFiltStorageType based on StorageType"""


_SpdTimeFiltStorageType_Object = MibTableColumn
spdTimeFiltStorageType = _SpdTimeFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 8),
    _SpdTimeFiltStorageType_Type()
)
spdTimeFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltStorageType.setStatus("current")
_SpdTimeFiltRowStatus_Type = RowStatus
_SpdTimeFiltRowStatus_Object = MibTableColumn
spdTimeFiltRowStatus = _SpdTimeFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 9),
    _SpdTimeFiltRowStatus_Type()
)
spdTimeFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdTimeFiltRowStatus.setStatus("current")
_SpdIpsoHeaderFilterTable_Object = MibTable
spdIpsoHeaderFilterTable = _SpdIpsoHeaderFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10)
)
if mibBuilder.loadTexts:
    spdIpsoHeaderFilterTable.setStatus("current")
_SpdIpsoHeaderFilterEntry_Object = MibTableRow
spdIpsoHeaderFilterEntry = _SpdIpsoHeaderFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1)
)
spdIpsoHeaderFilterEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdIpsoHeadFiltName"),
)
if mibBuilder.loadTexts:
    spdIpsoHeaderFilterEntry.setStatus("current")


class _SpdIpsoHeadFiltName_Type(SnmpAdminString):
    """Custom type spdIpsoHeadFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdIpsoHeadFiltName_Type.__name__ = "SnmpAdminString"
_SpdIpsoHeadFiltName_Object = MibTableColumn
spdIpsoHeadFiltName = _SpdIpsoHeadFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 1),
    _SpdIpsoHeadFiltName_Type()
)
spdIpsoHeadFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltName.setStatus("current")


class _SpdIpsoHeadFiltType_Type(Bits):
    """Custom type spdIpsoHeadFiltType based on Bits"""
    namedValues = NamedValues(
        *(("classificationLevel", 0),
          ("protectionAuthority", 1))
    )

_SpdIpsoHeadFiltType_Type.__name__ = "Bits"
_SpdIpsoHeadFiltType_Object = MibTableColumn
spdIpsoHeadFiltType = _SpdIpsoHeadFiltType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 2),
    _SpdIpsoHeadFiltType_Type()
)
spdIpsoHeadFiltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltType.setStatus("current")


class _SpdIpsoHeadFiltClassification_Type(Integer32):
    """Custom type spdIpsoHeadFiltClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topSecret", 61),
          ("unclassified", 171))
    )


_SpdIpsoHeadFiltClassification_Type.__name__ = "Integer32"
_SpdIpsoHeadFiltClassification_Object = MibTableColumn
spdIpsoHeadFiltClassification = _SpdIpsoHeadFiltClassification_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 3),
    _SpdIpsoHeadFiltClassification_Type()
)
spdIpsoHeadFiltClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltClassification.setStatus("current")


class _SpdIpsoHeadFiltProtectionAuth_Type(Integer32):
    """Custom type spdIpsoHeadFiltProtectionAuth based on Integer32"""
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
        *(("doe", 4),
          ("genser", 0),
          ("nsa", 3),
          ("sci", 2),
          ("siopesi", 1))
    )


_SpdIpsoHeadFiltProtectionAuth_Type.__name__ = "Integer32"
_SpdIpsoHeadFiltProtectionAuth_Object = MibTableColumn
spdIpsoHeadFiltProtectionAuth = _SpdIpsoHeadFiltProtectionAuth_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 4),
    _SpdIpsoHeadFiltProtectionAuth_Type()
)
spdIpsoHeadFiltProtectionAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltProtectionAuth.setStatus("current")
_SpdIpsoHeadFiltLastChanged_Type = TimeStamp
_SpdIpsoHeadFiltLastChanged_Object = MibTableColumn
spdIpsoHeadFiltLastChanged = _SpdIpsoHeadFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 5),
    _SpdIpsoHeadFiltLastChanged_Type()
)
spdIpsoHeadFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltLastChanged.setStatus("current")


class _SpdIpsoHeadFiltStorageType_Type(StorageType):
    """Custom type spdIpsoHeadFiltStorageType based on StorageType"""


_SpdIpsoHeadFiltStorageType_Object = MibTableColumn
spdIpsoHeadFiltStorageType = _SpdIpsoHeadFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 6),
    _SpdIpsoHeadFiltStorageType_Type()
)
spdIpsoHeadFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltStorageType.setStatus("current")
_SpdIpsoHeadFiltRowStatus_Type = RowStatus
_SpdIpsoHeadFiltRowStatus_Object = MibTableColumn
spdIpsoHeadFiltRowStatus = _SpdIpsoHeadFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 7),
    _SpdIpsoHeadFiltRowStatus_Type()
)
spdIpsoHeadFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdIpsoHeadFiltRowStatus.setStatus("current")
_SpdCompoundActionTable_Object = MibTable
spdCompoundActionTable = _SpdCompoundActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11)
)
if mibBuilder.loadTexts:
    spdCompoundActionTable.setStatus("current")
_SpdCompoundActionEntry_Object = MibTableRow
spdCompoundActionEntry = _SpdCompoundActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1)
)
spdCompoundActionEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdCompActName"),
)
if mibBuilder.loadTexts:
    spdCompoundActionEntry.setStatus("current")


class _SpdCompActName_Type(SnmpAdminString):
    """Custom type spdCompActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpdCompActName_Type.__name__ = "SnmpAdminString"
_SpdCompActName_Object = MibTableColumn
spdCompActName = _SpdCompActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 1),
    _SpdCompActName_Type()
)
spdCompActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdCompActName.setStatus("current")


class _SpdCompActExecutionStrategy_Type(Integer32):
    """Custom type spdCompActExecutionStrategy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doAll", 1),
          ("doUntilFailure", 3),
          ("doUntilSuccess", 2))
    )


_SpdCompActExecutionStrategy_Type.__name__ = "Integer32"
_SpdCompActExecutionStrategy_Object = MibTableColumn
spdCompActExecutionStrategy = _SpdCompActExecutionStrategy_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 2),
    _SpdCompActExecutionStrategy_Type()
)
spdCompActExecutionStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompActExecutionStrategy.setStatus("current")
_SpdCompActLastChanged_Type = TimeStamp
_SpdCompActLastChanged_Object = MibTableColumn
spdCompActLastChanged = _SpdCompActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 3),
    _SpdCompActLastChanged_Type()
)
spdCompActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdCompActLastChanged.setStatus("current")


class _SpdCompActStorageType_Type(StorageType):
    """Custom type spdCompActStorageType based on StorageType"""


_SpdCompActStorageType_Object = MibTableColumn
spdCompActStorageType = _SpdCompActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 4),
    _SpdCompActStorageType_Type()
)
spdCompActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompActStorageType.setStatus("current")
_SpdCompActRowStatus_Type = RowStatus
_SpdCompActRowStatus_Object = MibTableColumn
spdCompActRowStatus = _SpdCompActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 5),
    _SpdCompActRowStatus_Type()
)
spdCompActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdCompActRowStatus.setStatus("current")
_SpdSubactionsTable_Object = MibTable
spdSubactionsTable = _SpdSubactionsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12)
)
if mibBuilder.loadTexts:
    spdSubactionsTable.setStatus("current")
_SpdSubactionsEntry_Object = MibTableRow
spdSubactionsEntry = _SpdSubactionsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1)
)
spdSubactionsEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdCompActName"),
    (0, "IPSEC-SPD-MIB", "spdSubActPriority"),
)
if mibBuilder.loadTexts:
    spdSubactionsEntry.setStatus("current")


class _SpdSubActPriority_Type(Integer32):
    """Custom type spdSubActPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpdSubActPriority_Type.__name__ = "Integer32"
_SpdSubActPriority_Object = MibTableColumn
spdSubActPriority = _SpdSubActPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 1),
    _SpdSubActPriority_Type()
)
spdSubActPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spdSubActPriority.setStatus("current")
_SpdSubActSubActionName_Type = VariablePointer
_SpdSubActSubActionName_Object = MibTableColumn
spdSubActSubActionName = _SpdSubActSubActionName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 2),
    _SpdSubActSubActionName_Type()
)
spdSubActSubActionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubActSubActionName.setStatus("current")
_SpdSubActLastChanged_Type = TimeStamp
_SpdSubActLastChanged_Object = MibTableColumn
spdSubActLastChanged = _SpdSubActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 3),
    _SpdSubActLastChanged_Type()
)
spdSubActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdSubActLastChanged.setStatus("current")


class _SpdSubActStorageType_Type(StorageType):
    """Custom type spdSubActStorageType based on StorageType"""


_SpdSubActStorageType_Object = MibTableColumn
spdSubActStorageType = _SpdSubActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 4),
    _SpdSubActStorageType_Type()
)
spdSubActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubActStorageType.setStatus("current")
_SpdSubActRowStatus_Type = RowStatus
_SpdSubActRowStatus_Object = MibTableColumn
spdSubActRowStatus = _SpdSubActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 5),
    _SpdSubActRowStatus_Type()
)
spdSubActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spdSubActRowStatus.setStatus("current")
_SpdStaticActions_ObjectIdentity = ObjectIdentity
spdStaticActions = _SpdStaticActions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 13)
)


class _SpdDropAction_Type(Integer32):
    """Custom type spdDropAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpdDropAction_Type.__name__ = "Integer32"
_SpdDropAction_Object = MibScalar
spdDropAction = _SpdDropAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1),
    _SpdDropAction_Type()
)
spdDropAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdDropAction.setStatus("current")


class _SpdDropActionLog_Type(Integer32):
    """Custom type spdDropActionLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpdDropActionLog_Type.__name__ = "Integer32"
_SpdDropActionLog_Object = MibScalar
spdDropActionLog = _SpdDropActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 2),
    _SpdDropActionLog_Type()
)
spdDropActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdDropActionLog.setStatus("current")


class _SpdAcceptAction_Type(Integer32):
    """Custom type spdAcceptAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpdAcceptAction_Type.__name__ = "Integer32"
_SpdAcceptAction_Object = MibScalar
spdAcceptAction = _SpdAcceptAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 3),
    _SpdAcceptAction_Type()
)
spdAcceptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdAcceptAction.setStatus("current")


class _SpdAcceptActionLog_Type(Integer32):
    """Custom type spdAcceptActionLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpdAcceptActionLog_Type.__name__ = "Integer32"
_SpdAcceptActionLog_Object = MibScalar
spdAcceptActionLog = _SpdAcceptActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 4),
    _SpdAcceptActionLog_Type()
)
spdAcceptActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdAcceptActionLog.setStatus("current")
_SpdNotificationObjects_ObjectIdentity = ObjectIdentity
spdNotificationObjects = _SpdNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2)
)
_SpdNotifications_ObjectIdentity = ObjectIdentity
spdNotifications = _SpdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2, 0)
)
_SpdNotificationVariables_ObjectIdentity = ObjectIdentity
spdNotificationVariables = _SpdNotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2, 1)
)
_SpdActionExecuted_Type = VariablePointer
_SpdActionExecuted_Object = MibScalar
spdActionExecuted = _SpdActionExecuted_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 1),
    _SpdActionExecuted_Type()
)
spdActionExecuted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdActionExecuted.setStatus("current")
_SpdIPEndpointAddType_Type = InetAddressType
_SpdIPEndpointAddType_Object = MibScalar
spdIPEndpointAddType = _SpdIPEndpointAddType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 2),
    _SpdIPEndpointAddType_Type()
)
spdIPEndpointAddType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPEndpointAddType.setStatus("current")
_SpdIPEndpointAddress_Type = InetAddress
_SpdIPEndpointAddress_Object = MibScalar
spdIPEndpointAddress = _SpdIPEndpointAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 3),
    _SpdIPEndpointAddress_Type()
)
spdIPEndpointAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPEndpointAddress.setStatus("current")
_SpdIPSourceType_Type = InetAddressType
_SpdIPSourceType_Object = MibScalar
spdIPSourceType = _SpdIPSourceType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 4),
    _SpdIPSourceType_Type()
)
spdIPSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPSourceType.setStatus("current")
_SpdIPSourceAddress_Type = InetAddress
_SpdIPSourceAddress_Object = MibScalar
spdIPSourceAddress = _SpdIPSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 5),
    _SpdIPSourceAddress_Type()
)
spdIPSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPSourceAddress.setStatus("current")
_SpdIPDestinationType_Type = InetAddressType
_SpdIPDestinationType_Object = MibScalar
spdIPDestinationType = _SpdIPDestinationType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 6),
    _SpdIPDestinationType_Type()
)
spdIPDestinationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPDestinationType.setStatus("current")
_SpdIPDestinationAddress_Type = InetAddress
_SpdIPDestinationAddress_Object = MibScalar
spdIPDestinationAddress = _SpdIPDestinationAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 7),
    _SpdIPDestinationAddress_Type()
)
spdIPDestinationAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdIPDestinationAddress.setStatus("current")
_SpdPacketDirection_Type = IfDirection
_SpdPacketDirection_Object = MibScalar
spdPacketDirection = _SpdPacketDirection_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 8),
    _SpdPacketDirection_Type()
)
spdPacketDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdPacketDirection.setStatus("current")


class _SpdPacketPart_Type(OctetString):
    """Custom type spdPacketPart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_SpdPacketPart_Type.__name__ = "OctetString"
_SpdPacketPart_Object = MibScalar
spdPacketPart = _SpdPacketPart_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 9),
    _SpdPacketPart_Type()
)
spdPacketPart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spdPacketPart.setStatus("current")
_SpdConformanceObjects_ObjectIdentity = ObjectIdentity
spdConformanceObjects = _SpdConformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3)
)
_SpdCompliances_ObjectIdentity = ObjectIdentity
spdCompliances = _SpdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3, 1)
)
_SpdGroups_ObjectIdentity = ObjectIdentity
spdGroups = _SpdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3, 2)
)
_SpdActions_ObjectIdentity = ObjectIdentity
spdActions = _SpdActions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4)
)

# Managed Objects groups

spdEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 1)
)
spdEndpointGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdEndGroupName"),
        ("IPSEC-SPD-MIB", "spdEndGroupLastChanged"),
        ("IPSEC-SPD-MIB", "spdEndGroupStorageType"),
        ("IPSEC-SPD-MIB", "spdEndGroupRowStatus"))
)
if mibBuilder.loadTexts:
    spdEndpointGroup.setStatus("current")

spdGroupContentsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 2)
)
spdGroupContentsGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdGroupContComponentType"),
        ("IPSEC-SPD-MIB", "spdGroupContFilter"),
        ("IPSEC-SPD-MIB", "spdGroupContComponentName"),
        ("IPSEC-SPD-MIB", "spdGroupContLastChanged"),
        ("IPSEC-SPD-MIB", "spdGroupContStorageType"),
        ("IPSEC-SPD-MIB", "spdGroupContRowStatus"))
)
if mibBuilder.loadTexts:
    spdGroupContentsGroup.setStatus("current")

spdIpsecSystemPolicyNameGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 3)
)
spdIpsecSystemPolicyNameGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdIngressPolicyGroupName"),
        ("IPSEC-SPD-MIB", "spdEgressPolicyGroupName"))
)
if mibBuilder.loadTexts:
    spdIpsecSystemPolicyNameGroup.setStatus("current")

spdRuleDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 4)
)
spdRuleDefinitionGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdRuleDefDescription"),
        ("IPSEC-SPD-MIB", "spdRuleDefFilter"),
        ("IPSEC-SPD-MIB", "spdRuleDefFilterNegated"),
        ("IPSEC-SPD-MIB", "spdRuleDefAction"),
        ("IPSEC-SPD-MIB", "spdRuleDefAdminStatus"),
        ("IPSEC-SPD-MIB", "spdRuleDefLastChanged"),
        ("IPSEC-SPD-MIB", "spdRuleDefStorageType"),
        ("IPSEC-SPD-MIB", "spdRuleDefRowStatus"))
)
if mibBuilder.loadTexts:
    spdRuleDefinitionGroup.setStatus("current")

spdCompoundFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 5)
)
spdCompoundFilterGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdCompFiltDescription"),
        ("IPSEC-SPD-MIB", "spdCompFiltLogicType"),
        ("IPSEC-SPD-MIB", "spdCompFiltLastChanged"),
        ("IPSEC-SPD-MIB", "spdCompFiltStorageType"),
        ("IPSEC-SPD-MIB", "spdCompFiltRowStatus"),
        ("IPSEC-SPD-MIB", "spdSubFiltSubfilter"),
        ("IPSEC-SPD-MIB", "spdSubFiltSubfilterIsNegated"),
        ("IPSEC-SPD-MIB", "spdSubFiltLastChanged"),
        ("IPSEC-SPD-MIB", "spdSubFiltStorageType"),
        ("IPSEC-SPD-MIB", "spdSubFiltRowStatus"))
)
if mibBuilder.loadTexts:
    spdCompoundFilterGroup.setStatus("current")

spdStaticFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 6)
)
spdStaticFilterGroup.setObjects(
    ("IPSEC-SPD-MIB", "spdTrueFilter")
)
if mibBuilder.loadTexts:
    spdStaticFilterGroup.setStatus("current")

spdIPOffsetFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 7)
)
spdIPOffsetFilterGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdIpOffFiltOffset"),
        ("IPSEC-SPD-MIB", "spdIpOffFiltType"),
        ("IPSEC-SPD-MIB", "spdIpOffFiltValue"),
        ("IPSEC-SPD-MIB", "spdIpOffFiltLastChanged"),
        ("IPSEC-SPD-MIB", "spdIpOffFiltStorageType"),
        ("IPSEC-SPD-MIB", "spdIpOffFiltRowStatus"))
)
if mibBuilder.loadTexts:
    spdIPOffsetFilterGroup.setStatus("current")

spdTimeFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 8)
)
spdTimeFilterGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdTimeFiltPeriod"),
        ("IPSEC-SPD-MIB", "spdTimeFiltMonthOfYearMask"),
        ("IPSEC-SPD-MIB", "spdTimeFiltDayOfMonthMask"),
        ("IPSEC-SPD-MIB", "spdTimeFiltDayOfWeekMask"),
        ("IPSEC-SPD-MIB", "spdTimeFiltTimeOfDayMask"),
        ("IPSEC-SPD-MIB", "spdTimeFiltLastChanged"),
        ("IPSEC-SPD-MIB", "spdTimeFiltStorageType"),
        ("IPSEC-SPD-MIB", "spdTimeFiltRowStatus"))
)
if mibBuilder.loadTexts:
    spdTimeFilterGroup.setStatus("current")

spdIpsoHeaderFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 9)
)
spdIpsoHeaderFilterGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdIpsoHeadFiltType"),
        ("IPSEC-SPD-MIB", "spdIpsoHeadFiltClassification"),
        ("IPSEC-SPD-MIB", "spdIpsoHeadFiltProtectionAuth"),
        ("IPSEC-SPD-MIB", "spdIpsoHeadFiltLastChanged"),
        ("IPSEC-SPD-MIB", "spdIpsoHeadFiltStorageType"),
        ("IPSEC-SPD-MIB", "spdIpsoHeadFiltRowStatus"))
)
if mibBuilder.loadTexts:
    spdIpsoHeaderFilterGroup.setStatus("current")

spdStaticActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 10)
)
spdStaticActionGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdDropAction"),
        ("IPSEC-SPD-MIB", "spdAcceptAction"),
        ("IPSEC-SPD-MIB", "spdDropActionLog"),
        ("IPSEC-SPD-MIB", "spdAcceptActionLog"))
)
if mibBuilder.loadTexts:
    spdStaticActionGroup.setStatus("current")

spdCompoundActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 11)
)
spdCompoundActionGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdCompActExecutionStrategy"),
        ("IPSEC-SPD-MIB", "spdCompActLastChanged"),
        ("IPSEC-SPD-MIB", "spdCompActStorageType"),
        ("IPSEC-SPD-MIB", "spdCompActRowStatus"),
        ("IPSEC-SPD-MIB", "spdSubActSubActionName"),
        ("IPSEC-SPD-MIB", "spdSubActLastChanged"),
        ("IPSEC-SPD-MIB", "spdSubActStorageType"),
        ("IPSEC-SPD-MIB", "spdSubActRowStatus"))
)
if mibBuilder.loadTexts:
    spdCompoundActionGroup.setStatus("current")

spdActionLoggingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 12)
)
spdActionLoggingObjectGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdActionExecuted"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddType"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddress"),
        ("IPSEC-SPD-MIB", "spdIPSourceType"),
        ("IPSEC-SPD-MIB", "spdIPSourceAddress"),
        ("IPSEC-SPD-MIB", "spdIPDestinationType"),
        ("IPSEC-SPD-MIB", "spdIPDestinationAddress"),
        ("IPSEC-SPD-MIB", "spdPacketDirection"),
        ("IPSEC-SPD-MIB", "spdPacketPart"))
)
if mibBuilder.loadTexts:
    spdActionLoggingObjectGroup.setStatus("current")


# Notification objects

spdActionNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 153, 2, 0, 1)
)
spdActionNotification.setObjects(
      *(("IPSEC-SPD-MIB", "spdActionExecuted"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddType"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddress"),
        ("IPSEC-SPD-MIB", "spdIPSourceType"),
        ("IPSEC-SPD-MIB", "spdIPSourceAddress"),
        ("IPSEC-SPD-MIB", "spdIPDestinationType"),
        ("IPSEC-SPD-MIB", "spdIPDestinationAddress"),
        ("IPSEC-SPD-MIB", "spdPacketDirection"))
)
if mibBuilder.loadTexts:
    spdActionNotification.setStatus(
        "current"
    )

spdPacketNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 153, 2, 0, 2)
)
spdPacketNotification.setObjects(
      *(("IPSEC-SPD-MIB", "spdActionExecuted"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddType"),
        ("IPSEC-SPD-MIB", "spdIPEndpointAddress"),
        ("IPSEC-SPD-MIB", "spdIPSourceType"),
        ("IPSEC-SPD-MIB", "spdIPSourceAddress"),
        ("IPSEC-SPD-MIB", "spdIPDestinationType"),
        ("IPSEC-SPD-MIB", "spdIPDestinationAddress"),
        ("IPSEC-SPD-MIB", "spdPacketDirection"),
        ("IPSEC-SPD-MIB", "spdPacketPart"))
)
if mibBuilder.loadTexts:
    spdPacketNotification.setStatus(
        "current"
    )


# Notifications groups

spdActionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 13)
)
spdActionNotificationGroup.setObjects(
      *(("IPSEC-SPD-MIB", "spdActionNotification"),
        ("IPSEC-SPD-MIB", "spdPacketNotification"))
)
if mibBuilder.loadTexts:
    spdActionNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

spdRuleFilterFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 1)
)
if mibBuilder.loadTexts:
    spdRuleFilterFullCompliance.setStatus(
        "current"
    )

spdLoggingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 2)
)
if mibBuilder.loadTexts:
    spdLoggingCompliance.setStatus(
        "current"
    )

spdRuleFilterReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 3)
)
if mibBuilder.loadTexts:
    spdRuleFilterReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-SPD-MIB",
    **{"SpdBooleanOperator": SpdBooleanOperator,
       "SpdAdminStatus": SpdAdminStatus,
       "SpdIPPacketLogging": SpdIPPacketLogging,
       "SpdTimePeriod": SpdTimePeriod,
       "spdMIB": spdMIB,
       "spdConfigObjects": spdConfigObjects,
       "spdLocalConfigObjects": spdLocalConfigObjects,
       "spdIngressPolicyGroupName": spdIngressPolicyGroupName,
       "spdEgressPolicyGroupName": spdEgressPolicyGroupName,
       "spdEndpointToGroupTable": spdEndpointToGroupTable,
       "spdEndpointToGroupEntry": spdEndpointToGroupEntry,
       "spdEndGroupDirection": spdEndGroupDirection,
       "spdEndGroupInterface": spdEndGroupInterface,
       "spdEndGroupName": spdEndGroupName,
       "spdEndGroupLastChanged": spdEndGroupLastChanged,
       "spdEndGroupStorageType": spdEndGroupStorageType,
       "spdEndGroupRowStatus": spdEndGroupRowStatus,
       "spdGroupContentsTable": spdGroupContentsTable,
       "spdGroupContentsEntry": spdGroupContentsEntry,
       "spdGroupContName": spdGroupContName,
       "spdGroupContPriority": spdGroupContPriority,
       "spdGroupContFilter": spdGroupContFilter,
       "spdGroupContComponentType": spdGroupContComponentType,
       "spdGroupContComponentName": spdGroupContComponentName,
       "spdGroupContLastChanged": spdGroupContLastChanged,
       "spdGroupContStorageType": spdGroupContStorageType,
       "spdGroupContRowStatus": spdGroupContRowStatus,
       "spdRuleDefinitionTable": spdRuleDefinitionTable,
       "spdRuleDefinitionEntry": spdRuleDefinitionEntry,
       "spdRuleDefName": spdRuleDefName,
       "spdRuleDefDescription": spdRuleDefDescription,
       "spdRuleDefFilter": spdRuleDefFilter,
       "spdRuleDefFilterNegated": spdRuleDefFilterNegated,
       "spdRuleDefAction": spdRuleDefAction,
       "spdRuleDefAdminStatus": spdRuleDefAdminStatus,
       "spdRuleDefLastChanged": spdRuleDefLastChanged,
       "spdRuleDefStorageType": spdRuleDefStorageType,
       "spdRuleDefRowStatus": spdRuleDefRowStatus,
       "spdCompoundFilterTable": spdCompoundFilterTable,
       "spdCompoundFilterEntry": spdCompoundFilterEntry,
       "spdCompFiltName": spdCompFiltName,
       "spdCompFiltDescription": spdCompFiltDescription,
       "spdCompFiltLogicType": spdCompFiltLogicType,
       "spdCompFiltLastChanged": spdCompFiltLastChanged,
       "spdCompFiltStorageType": spdCompFiltStorageType,
       "spdCompFiltRowStatus": spdCompFiltRowStatus,
       "spdSubfiltersTable": spdSubfiltersTable,
       "spdSubfiltersEntry": spdSubfiltersEntry,
       "spdSubFiltPriority": spdSubFiltPriority,
       "spdSubFiltSubfilter": spdSubFiltSubfilter,
       "spdSubFiltSubfilterIsNegated": spdSubFiltSubfilterIsNegated,
       "spdSubFiltLastChanged": spdSubFiltLastChanged,
       "spdSubFiltStorageType": spdSubFiltStorageType,
       "spdSubFiltRowStatus": spdSubFiltRowStatus,
       "spdStaticFilters": spdStaticFilters,
       "spdTrueFilter": spdTrueFilter,
       "spdTrueFilterInstance": spdTrueFilterInstance,
       "spdIpOffsetFilterTable": spdIpOffsetFilterTable,
       "spdIpOffsetFilterEntry": spdIpOffsetFilterEntry,
       "spdIpOffFiltName": spdIpOffFiltName,
       "spdIpOffFiltOffset": spdIpOffFiltOffset,
       "spdIpOffFiltType": spdIpOffFiltType,
       "spdIpOffFiltValue": spdIpOffFiltValue,
       "spdIpOffFiltLastChanged": spdIpOffFiltLastChanged,
       "spdIpOffFiltStorageType": spdIpOffFiltStorageType,
       "spdIpOffFiltRowStatus": spdIpOffFiltRowStatus,
       "spdTimeFilterTable": spdTimeFilterTable,
       "spdTimeFilterEntry": spdTimeFilterEntry,
       "spdTimeFiltName": spdTimeFiltName,
       "spdTimeFiltPeriod": spdTimeFiltPeriod,
       "spdTimeFiltMonthOfYearMask": spdTimeFiltMonthOfYearMask,
       "spdTimeFiltDayOfMonthMask": spdTimeFiltDayOfMonthMask,
       "spdTimeFiltDayOfWeekMask": spdTimeFiltDayOfWeekMask,
       "spdTimeFiltTimeOfDayMask": spdTimeFiltTimeOfDayMask,
       "spdTimeFiltLastChanged": spdTimeFiltLastChanged,
       "spdTimeFiltStorageType": spdTimeFiltStorageType,
       "spdTimeFiltRowStatus": spdTimeFiltRowStatus,
       "spdIpsoHeaderFilterTable": spdIpsoHeaderFilterTable,
       "spdIpsoHeaderFilterEntry": spdIpsoHeaderFilterEntry,
       "spdIpsoHeadFiltName": spdIpsoHeadFiltName,
       "spdIpsoHeadFiltType": spdIpsoHeadFiltType,
       "spdIpsoHeadFiltClassification": spdIpsoHeadFiltClassification,
       "spdIpsoHeadFiltProtectionAuth": spdIpsoHeadFiltProtectionAuth,
       "spdIpsoHeadFiltLastChanged": spdIpsoHeadFiltLastChanged,
       "spdIpsoHeadFiltStorageType": spdIpsoHeadFiltStorageType,
       "spdIpsoHeadFiltRowStatus": spdIpsoHeadFiltRowStatus,
       "spdCompoundActionTable": spdCompoundActionTable,
       "spdCompoundActionEntry": spdCompoundActionEntry,
       "spdCompActName": spdCompActName,
       "spdCompActExecutionStrategy": spdCompActExecutionStrategy,
       "spdCompActLastChanged": spdCompActLastChanged,
       "spdCompActStorageType": spdCompActStorageType,
       "spdCompActRowStatus": spdCompActRowStatus,
       "spdSubactionsTable": spdSubactionsTable,
       "spdSubactionsEntry": spdSubactionsEntry,
       "spdSubActPriority": spdSubActPriority,
       "spdSubActSubActionName": spdSubActSubActionName,
       "spdSubActLastChanged": spdSubActLastChanged,
       "spdSubActStorageType": spdSubActStorageType,
       "spdSubActRowStatus": spdSubActRowStatus,
       "spdStaticActions": spdStaticActions,
       "spdDropAction": spdDropAction,
       "spdDropActionLog": spdDropActionLog,
       "spdAcceptAction": spdAcceptAction,
       "spdAcceptActionLog": spdAcceptActionLog,
       "spdNotificationObjects": spdNotificationObjects,
       "spdNotifications": spdNotifications,
       "spdActionNotification": spdActionNotification,
       "spdPacketNotification": spdPacketNotification,
       "spdNotificationVariables": spdNotificationVariables,
       "spdActionExecuted": spdActionExecuted,
       "spdIPEndpointAddType": spdIPEndpointAddType,
       "spdIPEndpointAddress": spdIPEndpointAddress,
       "spdIPSourceType": spdIPSourceType,
       "spdIPSourceAddress": spdIPSourceAddress,
       "spdIPDestinationType": spdIPDestinationType,
       "spdIPDestinationAddress": spdIPDestinationAddress,
       "spdPacketDirection": spdPacketDirection,
       "spdPacketPart": spdPacketPart,
       "spdConformanceObjects": spdConformanceObjects,
       "spdCompliances": spdCompliances,
       "spdRuleFilterFullCompliance": spdRuleFilterFullCompliance,
       "spdLoggingCompliance": spdLoggingCompliance,
       "spdRuleFilterReadOnlyCompliance": spdRuleFilterReadOnlyCompliance,
       "spdGroups": spdGroups,
       "spdEndpointGroup": spdEndpointGroup,
       "spdGroupContentsGroup": spdGroupContentsGroup,
       "spdIpsecSystemPolicyNameGroup": spdIpsecSystemPolicyNameGroup,
       "spdRuleDefinitionGroup": spdRuleDefinitionGroup,
       "spdCompoundFilterGroup": spdCompoundFilterGroup,
       "spdStaticFilterGroup": spdStaticFilterGroup,
       "spdIPOffsetFilterGroup": spdIPOffsetFilterGroup,
       "spdTimeFilterGroup": spdTimeFilterGroup,
       "spdIpsoHeaderFilterGroup": spdIpsoHeaderFilterGroup,
       "spdStaticActionGroup": spdStaticActionGroup,
       "spdCompoundActionGroup": spdCompoundActionGroup,
       "spdActionLoggingObjectGroup": spdActionLoggingObjectGroup,
       "spdActionNotificationGroup": spdActionNotificationGroup,
       "spdActions": spdActions}
)
