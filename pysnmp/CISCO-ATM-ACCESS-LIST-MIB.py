# SNMP MIB module (CISCO-ATM-ACCESS-LIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-ACCESS-LIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:44 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtmAccessListMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67)
)
ciscoAtmAccessListMIB.setRevisions(
        ("1996-11-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAtmAddressTemplate(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmAccessListMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmAccessListMIBObjects = _CiscoAtmAccessListMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1)
)
_CiscoAtmAddressTemplate_ObjectIdentity = ObjectIdentity
ciscoAtmAddressTemplate = _CiscoAtmAddressTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1)
)
_CiscoAtmAddressTemplateTable_Object = MibTable
ciscoAtmAddressTemplateTable = _CiscoAtmAddressTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmAddressTemplateTable.setStatus("current")
_CiscoAtmAddressTemplateEntry_Object = MibTableRow
ciscoAtmAddressTemplateEntry = _CiscoAtmAddressTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1)
)
ciscoAtmAddressTemplateEntry.setIndexNames(
    (0, "CISCO-ATM-ACCESS-LIST-MIB", "atmAddressAliasName"),
)
if mibBuilder.loadTexts:
    ciscoAtmAddressTemplateEntry.setStatus("current")


class _AtmAddressAliasName_Type(DisplayString):
    """Custom type atmAddressAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AtmAddressAliasName_Type.__name__ = "DisplayString"
_AtmAddressAliasName_Object = MibTableColumn
atmAddressAliasName = _AtmAddressAliasName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 1),
    _AtmAddressAliasName_Type()
)
atmAddressAliasName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddressAliasName.setStatus("current")
_AtmAddressTemplate_Type = CiscoAtmAddressTemplate
_AtmAddressTemplate_Object = MibTableColumn
atmAddressTemplate = _AtmAddressTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 2),
    _AtmAddressTemplate_Type()
)
atmAddressTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressTemplate.setStatus("current")
_AtmAddressTemplateRowStatus_Type = RowStatus
_AtmAddressTemplateRowStatus_Object = MibTableColumn
atmAddressTemplateRowStatus = _AtmAddressTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 3),
    _AtmAddressTemplateRowStatus_Type()
)
atmAddressTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressTemplateRowStatus.setStatus("current")
_CiscoAtmAddressFilter_ObjectIdentity = ObjectIdentity
ciscoAtmAddressFilter = _CiscoAtmAddressFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2)
)
_CiscoAtmAddressFilterSetTable_Object = MibTable
ciscoAtmAddressFilterSetTable = _CiscoAtmAddressFilterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmAddressFilterSetTable.setStatus("current")
_CiscoAtmAddressFilterSetEntry_Object = MibTableRow
ciscoAtmAddressFilterSetEntry = _CiscoAtmAddressFilterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1)
)
ciscoAtmAddressFilterSetEntry.setIndexNames(
    (0, "CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetName"),
    (0, "CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetIndex"),
)
if mibBuilder.loadTexts:
    ciscoAtmAddressFilterSetEntry.setStatus("current")


class _AtmAddressFilterSetName_Type(DisplayString):
    """Custom type atmAddressFilterSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AtmAddressFilterSetName_Type.__name__ = "DisplayString"
_AtmAddressFilterSetName_Object = MibTableColumn
atmAddressFilterSetName = _AtmAddressFilterSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 1),
    _AtmAddressFilterSetName_Type()
)
atmAddressFilterSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddressFilterSetName.setStatus("current")


class _AtmAddressFilterSetIndex_Type(Integer32):
    """Custom type atmAddressFilterSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmAddressFilterSetIndex_Type.__name__ = "Integer32"
_AtmAddressFilterSetIndex_Object = MibTableColumn
atmAddressFilterSetIndex = _AtmAddressFilterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 2),
    _AtmAddressFilterSetIndex_Type()
)
atmAddressFilterSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddressFilterSetIndex.setStatus("current")


class _AtmAddressFilterSetType_Type(Integer32):
    """Custom type atmAddressFilterSetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressFilter", 1),
          ("timeOfDayFilter", 2))
    )


_AtmAddressFilterSetType_Type.__name__ = "Integer32"
_AtmAddressFilterSetType_Object = MibTableColumn
atmAddressFilterSetType = _AtmAddressFilterSetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 3),
    _AtmAddressFilterSetType_Type()
)
atmAddressFilterSetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetType.setStatus("current")


class _AtmAddressFilterSetTemplate_Type(DisplayString):
    """Custom type atmAddressFilterSetTemplate based on DisplayString"""
    defaultValue = OctetString("...")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AtmAddressFilterSetTemplate_Type.__name__ = "DisplayString"
_AtmAddressFilterSetTemplate_Object = MibTableColumn
atmAddressFilterSetTemplate = _AtmAddressFilterSetTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 4),
    _AtmAddressFilterSetTemplate_Type()
)
atmAddressFilterSetTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetTemplate.setStatus("current")


class _AtmAddressFilterSetStartHour_Type(Integer32):
    """Custom type atmAddressFilterSetStartHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AtmAddressFilterSetStartHour_Type.__name__ = "Integer32"
_AtmAddressFilterSetStartHour_Object = MibTableColumn
atmAddressFilterSetStartHour = _AtmAddressFilterSetStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 5),
    _AtmAddressFilterSetStartHour_Type()
)
atmAddressFilterSetStartHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetStartHour.setStatus("current")


class _AtmAddressFilterSetStartMinute_Type(Integer32):
    """Custom type atmAddressFilterSetStartMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AtmAddressFilterSetStartMinute_Type.__name__ = "Integer32"
_AtmAddressFilterSetStartMinute_Object = MibTableColumn
atmAddressFilterSetStartMinute = _AtmAddressFilterSetStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 6),
    _AtmAddressFilterSetStartMinute_Type()
)
atmAddressFilterSetStartMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetStartMinute.setStatus("current")


class _AtmAddressFilterSetEndHour_Type(Integer32):
    """Custom type atmAddressFilterSetEndHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AtmAddressFilterSetEndHour_Type.__name__ = "Integer32"
_AtmAddressFilterSetEndHour_Object = MibTableColumn
atmAddressFilterSetEndHour = _AtmAddressFilterSetEndHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 7),
    _AtmAddressFilterSetEndHour_Type()
)
atmAddressFilterSetEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetEndHour.setStatus("current")


class _AtmAddressFilterSetEndMinute_Type(Integer32):
    """Custom type atmAddressFilterSetEndMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AtmAddressFilterSetEndMinute_Type.__name__ = "Integer32"
_AtmAddressFilterSetEndMinute_Object = MibTableColumn
atmAddressFilterSetEndMinute = _AtmAddressFilterSetEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 8),
    _AtmAddressFilterSetEndMinute_Type()
)
atmAddressFilterSetEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetEndMinute.setStatus("current")


class _AtmAddressFilterSetPermission_Type(Integer32):
    """Custom type atmAddressFilterSetPermission based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AtmAddressFilterSetPermission_Type.__name__ = "Integer32"
_AtmAddressFilterSetPermission_Object = MibTableColumn
atmAddressFilterSetPermission = _AtmAddressFilterSetPermission_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 9),
    _AtmAddressFilterSetPermission_Type()
)
atmAddressFilterSetPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetPermission.setStatus("current")
_AtmAddressFilterSetRowStatus_Type = RowStatus
_AtmAddressFilterSetRowStatus_Object = MibTableColumn
atmAddressFilterSetRowStatus = _AtmAddressFilterSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 10),
    _AtmAddressFilterSetRowStatus_Type()
)
atmAddressFilterSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterSetRowStatus.setStatus("current")
_CiscoAtmAddressFilterExpressionTable_Object = MibTable
ciscoAtmAddressFilterExpressionTable = _CiscoAtmAddressFilterExpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmAddressFilterExpressionTable.setStatus("current")
_CiscoAtmAddressFilterExpressionEntry_Object = MibTableRow
ciscoAtmAddressFilterExpressionEntry = _CiscoAtmAddressFilterExpressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1)
)
ciscoAtmAddressFilterExpressionEntry.setIndexNames(
    (0, "CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionName"),
)
if mibBuilder.loadTexts:
    ciscoAtmAddressFilterExpressionEntry.setStatus("current")


class _AtmAddressFilterExpressionName_Type(DisplayString):
    """Custom type atmAddressFilterExpressionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AtmAddressFilterExpressionName_Type.__name__ = "DisplayString"
_AtmAddressFilterExpressionName_Object = MibTableColumn
atmAddressFilterExpressionName = _AtmAddressFilterExpressionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 1),
    _AtmAddressFilterExpressionName_Type()
)
atmAddressFilterExpressionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionName.setStatus("current")


class _AtmAddressFilterExpressionQualifier1_Type(Integer32):
    """Custom type atmAddressFilterExpressionQualifier1 based on Integer32"""
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
        *(("destination", 2),
          ("none", 3),
          ("source", 1))
    )


_AtmAddressFilterExpressionQualifier1_Type.__name__ = "Integer32"
_AtmAddressFilterExpressionQualifier1_Object = MibTableColumn
atmAddressFilterExpressionQualifier1 = _AtmAddressFilterExpressionQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 2),
    _AtmAddressFilterExpressionQualifier1_Type()
)
atmAddressFilterExpressionQualifier1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionQualifier1.setStatus("current")


class _AtmAddressFilterExpressionTerm1_Type(DisplayString):
    """Custom type atmAddressFilterExpressionTerm1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AtmAddressFilterExpressionTerm1_Type.__name__ = "DisplayString"
_AtmAddressFilterExpressionTerm1_Object = MibTableColumn
atmAddressFilterExpressionTerm1 = _AtmAddressFilterExpressionTerm1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 3),
    _AtmAddressFilterExpressionTerm1_Type()
)
atmAddressFilterExpressionTerm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionTerm1.setStatus("current")


class _AtmAddressFilterExpressionQualifier2_Type(Integer32):
    """Custom type atmAddressFilterExpressionQualifier2 based on Integer32"""
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
        *(("destination", 2),
          ("none", 3),
          ("source", 1))
    )


_AtmAddressFilterExpressionQualifier2_Type.__name__ = "Integer32"
_AtmAddressFilterExpressionQualifier2_Object = MibTableColumn
atmAddressFilterExpressionQualifier2 = _AtmAddressFilterExpressionQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 4),
    _AtmAddressFilterExpressionQualifier2_Type()
)
atmAddressFilterExpressionQualifier2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionQualifier2.setStatus("current")


class _AtmAddressFilterExpressionTerm2_Type(DisplayString):
    """Custom type atmAddressFilterExpressionTerm2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtmAddressFilterExpressionTerm2_Type.__name__ = "DisplayString"
_AtmAddressFilterExpressionTerm2_Object = MibTableColumn
atmAddressFilterExpressionTerm2 = _AtmAddressFilterExpressionTerm2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 5),
    _AtmAddressFilterExpressionTerm2_Type()
)
atmAddressFilterExpressionTerm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionTerm2.setStatus("current")


class _AtmAddressFilterExpressionOperator_Type(Integer32):
    """Custom type atmAddressFilterExpressionOperator based on Integer32"""
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
        *(("and", 1),
          ("none", 5),
          ("not", 4),
          ("or", 2),
          ("xor", 3))
    )


_AtmAddressFilterExpressionOperator_Type.__name__ = "Integer32"
_AtmAddressFilterExpressionOperator_Object = MibTableColumn
atmAddressFilterExpressionOperator = _AtmAddressFilterExpressionOperator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 6),
    _AtmAddressFilterExpressionOperator_Type()
)
atmAddressFilterExpressionOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionOperator.setStatus("current")
_AtmAddressFilterExpressionRowStatus_Type = RowStatus
_AtmAddressFilterExpressionRowStatus_Object = MibTableColumn
atmAddressFilterExpressionRowStatus = _AtmAddressFilterExpressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 7),
    _AtmAddressFilterExpressionRowStatus_Type()
)
atmAddressFilterExpressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmAddressFilterExpressionRowStatus.setStatus("current")
_CiscoAtmAccessGroup_ObjectIdentity = ObjectIdentity
ciscoAtmAccessGroup = _CiscoAtmAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3)
)
_CiscoAtmAccessGroupTable_Object = MibTable
ciscoAtmAccessGroupTable = _CiscoAtmAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmAccessGroupTable.setStatus("current")
_CiscoAtmAccessGroupEntry_Object = MibTableRow
ciscoAtmAccessGroupEntry = _CiscoAtmAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1)
)
ciscoAtmAccessGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoAtmAccessGroupEntry.setStatus("current")


class _AtmInboundAccessGroupName_Type(DisplayString):
    """Custom type atmInboundAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtmInboundAccessGroupName_Type.__name__ = "DisplayString"
_AtmInboundAccessGroupName_Object = MibTableColumn
atmInboundAccessGroupName = _AtmInboundAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1, 1),
    _AtmInboundAccessGroupName_Type()
)
atmInboundAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInboundAccessGroupName.setStatus("current")


class _AtmOutboundAccessGroupName_Type(DisplayString):
    """Custom type atmOutboundAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtmOutboundAccessGroupName_Type.__name__ = "DisplayString"
_AtmOutboundAccessGroupName_Object = MibTableColumn
atmOutboundAccessGroupName = _AtmOutboundAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1, 2),
    _AtmOutboundAccessGroupName_Type()
)
atmOutboundAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOutboundAccessGroupName.setStatus("current")
_CiscoAtmAccessListMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmAccessListMIBConformance = _CiscoAtmAccessListMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 3)
)
_CiscoAtmAccessListMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmAccessListMIBCompliances = _CiscoAtmAccessListMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 1)
)
_CiscoAtmAccessListMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmAccessListMIBGroups = _CiscoAtmAccessListMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 2)
)

# Managed Objects groups

ciscoAtmAccessListMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 2, 1)
)
ciscoAtmAccessListMIBGroup.setObjects(
      *(("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressTemplate"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressTemplateRowStatus"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetType"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetTemplate"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetStartHour"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetStartMinute"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetEndHour"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetEndMinute"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetPermission"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterSetRowStatus"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionQualifier1"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionTerm1"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionQualifier2"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionTerm2"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionOperator"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmAddressFilterExpressionRowStatus"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmInboundAccessGroupName"),
        ("CISCO-ATM-ACCESS-LIST-MIB", "atmOutboundAccessGroupName"))
)
if mibBuilder.loadTexts:
    ciscoAtmAccessListMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmAccessListMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmAccessListMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-ACCESS-LIST-MIB",
    **{"CiscoAtmAddressTemplate": CiscoAtmAddressTemplate,
       "ciscoAtmAccessListMIB": ciscoAtmAccessListMIB,
       "ciscoAtmAccessListMIBObjects": ciscoAtmAccessListMIBObjects,
       "ciscoAtmAddressTemplate": ciscoAtmAddressTemplate,
       "ciscoAtmAddressTemplateTable": ciscoAtmAddressTemplateTable,
       "ciscoAtmAddressTemplateEntry": ciscoAtmAddressTemplateEntry,
       "atmAddressAliasName": atmAddressAliasName,
       "atmAddressTemplate": atmAddressTemplate,
       "atmAddressTemplateRowStatus": atmAddressTemplateRowStatus,
       "ciscoAtmAddressFilter": ciscoAtmAddressFilter,
       "ciscoAtmAddressFilterSetTable": ciscoAtmAddressFilterSetTable,
       "ciscoAtmAddressFilterSetEntry": ciscoAtmAddressFilterSetEntry,
       "atmAddressFilterSetName": atmAddressFilterSetName,
       "atmAddressFilterSetIndex": atmAddressFilterSetIndex,
       "atmAddressFilterSetType": atmAddressFilterSetType,
       "atmAddressFilterSetTemplate": atmAddressFilterSetTemplate,
       "atmAddressFilterSetStartHour": atmAddressFilterSetStartHour,
       "atmAddressFilterSetStartMinute": atmAddressFilterSetStartMinute,
       "atmAddressFilterSetEndHour": atmAddressFilterSetEndHour,
       "atmAddressFilterSetEndMinute": atmAddressFilterSetEndMinute,
       "atmAddressFilterSetPermission": atmAddressFilterSetPermission,
       "atmAddressFilterSetRowStatus": atmAddressFilterSetRowStatus,
       "ciscoAtmAddressFilterExpressionTable": ciscoAtmAddressFilterExpressionTable,
       "ciscoAtmAddressFilterExpressionEntry": ciscoAtmAddressFilterExpressionEntry,
       "atmAddressFilterExpressionName": atmAddressFilterExpressionName,
       "atmAddressFilterExpressionQualifier1": atmAddressFilterExpressionQualifier1,
       "atmAddressFilterExpressionTerm1": atmAddressFilterExpressionTerm1,
       "atmAddressFilterExpressionQualifier2": atmAddressFilterExpressionQualifier2,
       "atmAddressFilterExpressionTerm2": atmAddressFilterExpressionTerm2,
       "atmAddressFilterExpressionOperator": atmAddressFilterExpressionOperator,
       "atmAddressFilterExpressionRowStatus": atmAddressFilterExpressionRowStatus,
       "ciscoAtmAccessGroup": ciscoAtmAccessGroup,
       "ciscoAtmAccessGroupTable": ciscoAtmAccessGroupTable,
       "ciscoAtmAccessGroupEntry": ciscoAtmAccessGroupEntry,
       "atmInboundAccessGroupName": atmInboundAccessGroupName,
       "atmOutboundAccessGroupName": atmOutboundAccessGroupName,
       "ciscoAtmAccessListMIBConformance": ciscoAtmAccessListMIBConformance,
       "ciscoAtmAccessListMIBCompliances": ciscoAtmAccessListMIBCompliances,
       "ciscoAtmAccessListMIBCompliance": ciscoAtmAccessListMIBCompliance,
       "ciscoAtmAccessListMIBGroups": ciscoAtmAccessListMIBGroups,
       "ciscoAtmAccessListMIBGroup": ciscoAtmAccessListMIBGroup}
)
