# SNMP MIB module (CISCO-COMMON-ROLES-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-COMMON-ROLES-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:36 2024
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

(ccrmConfigurationExtGroup,) = mibBuilder.importSymbols(
    "CISCO-COMMON-ROLES-MIB",
    "ccrmConfigurationExtGroup")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCommonRolesExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651)
)
ciscoCommonRolesExtMIB.setRevisions(
        ("2008-02-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcreOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readWrite", 2))
    )



class CcreResourceAccess(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoCommonRolesExtNotifications_ObjectIdentity = ObjectIdentity
ciscoCommonRolesExtNotifications = _CiscoCommonRolesExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 0)
)
_CiscoCommonRolesExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCommonRolesExtMIBObjects = _CiscoCommonRolesExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1)
)
_CcreInfo_ObjectIdentity = ObjectIdentity
ccreInfo = _CcreInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1)
)
_CcreFeatureElementTable_Object = MibTable
ccreFeatureElementTable = _CcreFeatureElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccreFeatureElementTable.setStatus("current")
_CcreFeatureElementEntry_Object = MibTableRow
ccreFeatureElementEntry = _CcreFeatureElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1)
)
ccreFeatureElementEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreFeatureName"),
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreFeatureElementIndex"),
)
if mibBuilder.loadTexts:
    ccreFeatureElementEntry.setStatus("current")


class _CcreFeatureName_Type(SnmpAdminString):
    """Custom type ccreFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcreFeatureName_Type.__name__ = "SnmpAdminString"
_CcreFeatureName_Object = MibTableColumn
ccreFeatureName = _CcreFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1, 1),
    _CcreFeatureName_Type()
)
ccreFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccreFeatureName.setStatus("current")


class _CcreFeatureElementIndex_Type(Unsigned32):
    """Custom type ccreFeatureElementIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcreFeatureElementIndex_Type.__name__ = "Unsigned32"
_CcreFeatureElementIndex_Object = MibTableColumn
ccreFeatureElementIndex = _CcreFeatureElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1, 2),
    _CcreFeatureElementIndex_Type()
)
ccreFeatureElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccreFeatureElementIndex.setStatus("current")


class _CcreFeatureElementName_Type(SnmpAdminString):
    """Custom type ccreFeatureElementName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcreFeatureElementName_Type.__name__ = "SnmpAdminString"
_CcreFeatureElementName_Object = MibTableColumn
ccreFeatureElementName = _CcreFeatureElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1, 3),
    _CcreFeatureElementName_Type()
)
ccreFeatureElementName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreFeatureElementName.setStatus("current")


class _CcreFeatureElementType_Type(Integer32):
    """Custom type ccreFeatureElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("command", 1),
          ("feature", 2),
          ("none", 3))
    )


_CcreFeatureElementType_Type.__name__ = "Integer32"
_CcreFeatureElementType_Object = MibTableColumn
ccreFeatureElementType = _CcreFeatureElementType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1, 4),
    _CcreFeatureElementType_Type()
)
ccreFeatureElementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreFeatureElementType.setStatus("current")
_CcreFeatureRowStatus_Type = RowStatus
_CcreFeatureRowStatus_Object = MibTableColumn
ccreFeatureRowStatus = _CcreFeatureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 1, 1, 1, 5),
    _CcreFeatureRowStatus_Type()
)
ccreFeatureRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreFeatureRowStatus.setStatus("current")
_CcreRoleConfig_ObjectIdentity = ObjectIdentity
ccreRoleConfig = _CcreRoleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2)
)
_CcreRoleTable_Object = MibTable
ccreRoleTable = _CcreRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccreRoleTable.setStatus("current")
_CcreRoleEntry_Object = MibTableRow
ccreRoleEntry = _CcreRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2, 1)
)
ccreRoleEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleName"),
)
if mibBuilder.loadTexts:
    ccreRoleEntry.setStatus("current")


class _CcreRoleName_Type(SnmpAdminString):
    """Custom type ccreRoleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcreRoleName_Type.__name__ = "SnmpAdminString"
_CcreRoleName_Object = MibTableColumn
ccreRoleName = _CcreRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2, 1, 1),
    _CcreRoleName_Type()
)
ccreRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccreRoleName.setStatus("current")


class _CcreRoleDescription_Type(SnmpAdminString):
    """Custom type ccreRoleDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcreRoleDescription_Type.__name__ = "SnmpAdminString"
_CcreRoleDescription_Object = MibTableColumn
ccreRoleDescription = _CcreRoleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2, 1, 2),
    _CcreRoleDescription_Type()
)
ccreRoleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleDescription.setStatus("current")
_CcreRoleResourceAccess_Type = CcreResourceAccess
_CcreRoleResourceAccess_Object = MibTableColumn
ccreRoleResourceAccess = _CcreRoleResourceAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2, 1, 3),
    _CcreRoleResourceAccess_Type()
)
ccreRoleResourceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleResourceAccess.setStatus("current")
_CcreRoleRowStatus_Type = RowStatus
_CcreRoleRowStatus_Object = MibTableColumn
ccreRoleRowStatus = _CcreRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 2, 1, 4),
    _CcreRoleRowStatus_Type()
)
ccreRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleRowStatus.setStatus("current")
_CcreRoleScopeTable_Object = MibTable
ccreRoleScopeTable = _CcreRoleScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccreRoleScopeTable.setStatus("current")
_CcreRoleScopeEntry_Object = MibTableRow
ccreRoleScopeEntry = _CcreRoleScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3, 1)
)
ccreRoleScopeEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleName"),
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleScopeIndex"),
)
if mibBuilder.loadTexts:
    ccreRoleScopeEntry.setStatus("current")


class _CcreRoleScopeIndex_Type(Unsigned32):
    """Custom type ccreRoleScopeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcreRoleScopeIndex_Type.__name__ = "Unsigned32"
_CcreRoleScopeIndex_Object = MibTableColumn
ccreRoleScopeIndex = _CcreRoleScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3, 1, 1),
    _CcreRoleScopeIndex_Type()
)
ccreRoleScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccreRoleScopeIndex.setStatus("current")


class _CcreRoleScopeRestriction_Type(Integer32):
    """Custom type ccreRoleScopeRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 3),
          ("vlan", 2),
          ("vsan", 1))
    )


_CcreRoleScopeRestriction_Type.__name__ = "Integer32"
_CcreRoleScopeRestriction_Object = MibTableColumn
ccreRoleScopeRestriction = _CcreRoleScopeRestriction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3, 1, 2),
    _CcreRoleScopeRestriction_Type()
)
ccreRoleScopeRestriction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleScopeRestriction.setStatus("current")


class _CcreRoleScopeValue_Type(Integer32):
    """Custom type ccreRoleScopeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcreRoleScopeValue_Type.__name__ = "Integer32"
_CcreRoleScopeValue_Object = MibTableColumn
ccreRoleScopeValue = _CcreRoleScopeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3, 1, 3),
    _CcreRoleScopeValue_Type()
)
ccreRoleScopeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleScopeValue.setStatus("current")
_CcreRoleScopeRowStatus_Type = RowStatus
_CcreRoleScopeRowStatus_Object = MibTableColumn
ccreRoleScopeRowStatus = _CcreRoleScopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 2, 3, 1, 4),
    _CcreRoleScopeRowStatus_Type()
)
ccreRoleScopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRoleScopeRowStatus.setStatus("current")
_CcreRuleConfig_ObjectIdentity = ObjectIdentity
ccreRuleConfig = _CcreRuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3)
)
_CcreRuleTable_Object = MibTable
ccreRuleTable = _CcreRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccreRuleTable.setStatus("current")
_CcreRuleEntry_Object = MibTableRow
ccreRuleEntry = _CcreRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1)
)
ccreRuleEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleName"),
    (0, "CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleNumber"),
)
if mibBuilder.loadTexts:
    ccreRuleEntry.setStatus("current")


class _CcreRuleNumber_Type(Unsigned32):
    """Custom type ccreRuleNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CcreRuleNumber_Type.__name__ = "Unsigned32"
_CcreRuleNumber_Object = MibTableColumn
ccreRuleNumber = _CcreRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 1),
    _CcreRuleNumber_Type()
)
ccreRuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccreRuleNumber.setStatus("current")


class _CcreRuleFeatureElementName_Type(SnmpAdminString):
    """Custom type ccreRuleFeatureElementName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcreRuleFeatureElementName_Type.__name__ = "SnmpAdminString"
_CcreRuleFeatureElementName_Object = MibTableColumn
ccreRuleFeatureElementName = _CcreRuleFeatureElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 2),
    _CcreRuleFeatureElementName_Type()
)
ccreRuleFeatureElementName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRuleFeatureElementName.setStatus("current")


class _CcreRuleFeatureElementType_Type(Integer32):
    """Custom type ccreRuleFeatureElementType based on Integer32"""
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
        *(("all", 4),
          ("command", 1),
          ("feature", 2),
          ("featureGroup", 3))
    )


_CcreRuleFeatureElementType_Type.__name__ = "Integer32"
_CcreRuleFeatureElementType_Object = MibTableColumn
ccreRuleFeatureElementType = _CcreRuleFeatureElementType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 3),
    _CcreRuleFeatureElementType_Type()
)
ccreRuleFeatureElementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRuleFeatureElementType.setStatus("current")
_CcreRuleOperation_Type = CcreOperation
_CcreRuleOperation_Object = MibTableColumn
ccreRuleOperation = _CcreRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 4),
    _CcreRuleOperation_Type()
)
ccreRuleOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRuleOperation.setStatus("current")


class _CcreRuleOperationPermitted_Type(TruthValue):
    """Custom type ccreRuleOperationPermitted based on TruthValue"""


_CcreRuleOperationPermitted_Object = MibTableColumn
ccreRuleOperationPermitted = _CcreRuleOperationPermitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 5),
    _CcreRuleOperationPermitted_Type()
)
ccreRuleOperationPermitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRuleOperationPermitted.setStatus("current")
_CcreRuleRowStatus_Type = RowStatus
_CcreRuleRowStatus_Object = MibTableColumn
ccreRuleRowStatus = _CcreRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 1, 3, 2, 1, 6),
    _CcreRuleRowStatus_Type()
)
ccreRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccreRuleRowStatus.setStatus("current")
_CiscoCommonRolesExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCommonRolesExtMIBConformance = _CiscoCommonRolesExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 2)
)
_CcreMIBCompliances_ObjectIdentity = ObjectIdentity
ccreMIBCompliances = _CcreMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 2, 1)
)
_CcreMIBGroups_ObjectIdentity = ObjectIdentity
ccreMIBGroups = _CcreMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 2, 2)
)

# Managed Objects groups

ccreConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 2, 2, 1)
)
ccreConfigurationGroup.setObjects(
      *(("CISCO-COMMON-ROLES-EXT-MIB", "ccreFeatureElementName"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreFeatureElementType"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreFeatureRowStatus"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleDescription"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleResourceAccess"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleRowStatus"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleScopeRestriction"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleScopeValue"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRoleScopeRowStatus"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleFeatureElementName"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleFeatureElementType"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleOperation"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleOperationPermitted"),
        ("CISCO-COMMON-ROLES-EXT-MIB", "ccreRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ccreConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccreMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 651, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccreMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-COMMON-ROLES-EXT-MIB",
    **{"CcreOperation": CcreOperation,
       "CcreResourceAccess": CcreResourceAccess,
       "ciscoCommonRolesExtMIB": ciscoCommonRolesExtMIB,
       "ciscoCommonRolesExtNotifications": ciscoCommonRolesExtNotifications,
       "ciscoCommonRolesExtMIBObjects": ciscoCommonRolesExtMIBObjects,
       "ccreInfo": ccreInfo,
       "ccreFeatureElementTable": ccreFeatureElementTable,
       "ccreFeatureElementEntry": ccreFeatureElementEntry,
       "ccreFeatureName": ccreFeatureName,
       "ccreFeatureElementIndex": ccreFeatureElementIndex,
       "ccreFeatureElementName": ccreFeatureElementName,
       "ccreFeatureElementType": ccreFeatureElementType,
       "ccreFeatureRowStatus": ccreFeatureRowStatus,
       "ccreRoleConfig": ccreRoleConfig,
       "ccreRoleTable": ccreRoleTable,
       "ccreRoleEntry": ccreRoleEntry,
       "ccreRoleName": ccreRoleName,
       "ccreRoleDescription": ccreRoleDescription,
       "ccreRoleResourceAccess": ccreRoleResourceAccess,
       "ccreRoleRowStatus": ccreRoleRowStatus,
       "ccreRoleScopeTable": ccreRoleScopeTable,
       "ccreRoleScopeEntry": ccreRoleScopeEntry,
       "ccreRoleScopeIndex": ccreRoleScopeIndex,
       "ccreRoleScopeRestriction": ccreRoleScopeRestriction,
       "ccreRoleScopeValue": ccreRoleScopeValue,
       "ccreRoleScopeRowStatus": ccreRoleScopeRowStatus,
       "ccreRuleConfig": ccreRuleConfig,
       "ccreRuleTable": ccreRuleTable,
       "ccreRuleEntry": ccreRuleEntry,
       "ccreRuleNumber": ccreRuleNumber,
       "ccreRuleFeatureElementName": ccreRuleFeatureElementName,
       "ccreRuleFeatureElementType": ccreRuleFeatureElementType,
       "ccreRuleOperation": ccreRuleOperation,
       "ccreRuleOperationPermitted": ccreRuleOperationPermitted,
       "ccreRuleRowStatus": ccreRuleRowStatus,
       "ciscoCommonRolesExtMIBConformance": ciscoCommonRolesExtMIBConformance,
       "ccreMIBCompliances": ccreMIBCompliances,
       "ccreMIBCompliance": ccreMIBCompliance,
       "ccreMIBGroups": ccreMIBGroups,
       "ccreConfigurationGroup": ccreConfigurationGroup}
)
