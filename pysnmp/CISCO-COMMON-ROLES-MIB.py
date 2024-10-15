# SNMP MIB module (CISCO-COMMON-ROLES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-COMMON-ROLES-MIB
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

ciscoCommonRolesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361)
)
ciscoCommonRolesMIB.setRevisions(
        ("2008-02-15 00:00",
         "2003-09-15 00:00",
         "2003-06-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CommonRoleOperation(Integer32, TextualConvention):
    status = "current"
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
        *(("clear", 1),
          ("config", 2),
          ("debug", 3),
          ("exec", 5),
          ("show", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCommonRolesNotifications_ObjectIdentity = ObjectIdentity
ciscoCommonRolesNotifications = _CiscoCommonRolesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 0)
)
_CiscoCommonRolesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCommonRolesMIBObjects = _CiscoCommonRolesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1)
)
_CcrInfo_ObjectIdentity = ObjectIdentity
ccrInfo = _CcrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1)
)
_CommonRoleFeatureTable_Object = MibTable
commonRoleFeatureTable = _CommonRoleFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1)
)
if mibBuilder.loadTexts:
    commonRoleFeatureTable.setStatus("current")
_CommonRoleFeatureEntry_Object = MibTableRow
commonRoleFeatureEntry = _CommonRoleFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1)
)
commonRoleFeatureEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-MIB", "commonRoleFeatureIndex"),
)
if mibBuilder.loadTexts:
    commonRoleFeatureEntry.setStatus("current")


class _CommonRoleFeatureIndex_Type(Unsigned32):
    """Custom type commonRoleFeatureIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CommonRoleFeatureIndex_Type.__name__ = "Unsigned32"
_CommonRoleFeatureIndex_Object = MibTableColumn
commonRoleFeatureIndex = _CommonRoleFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 1),
    _CommonRoleFeatureIndex_Type()
)
commonRoleFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commonRoleFeatureIndex.setStatus("current")


class _CommonRoleFeatureName_Type(SnmpAdminString):
    """Custom type commonRoleFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CommonRoleFeatureName_Type.__name__ = "SnmpAdminString"
_CommonRoleFeatureName_Object = MibTableColumn
commonRoleFeatureName = _CommonRoleFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 2),
    _CommonRoleFeatureName_Type()
)
commonRoleFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRoleFeatureName.setStatus("current")
_CommonRoleFeatureOperation_Type = CommonRoleOperation
_CommonRoleFeatureOperation_Object = MibTableColumn
commonRoleFeatureOperation = _CommonRoleFeatureOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 3),
    _CommonRoleFeatureOperation_Type()
)
commonRoleFeatureOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRoleFeatureOperation.setStatus("current")
_CommonRoleSupportedOperTable_Object = MibTable
commonRoleSupportedOperTable = _CommonRoleSupportedOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2)
)
if mibBuilder.loadTexts:
    commonRoleSupportedOperTable.setStatus("current")
_CommonRoleSupportedOperEntry_Object = MibTableRow
commonRoleSupportedOperEntry = _CommonRoleSupportedOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1)
)
commonRoleSupportedOperEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-MIB", "commonRoleAccessMethod"),
)
if mibBuilder.loadTexts:
    commonRoleSupportedOperEntry.setStatus("current")


class _CommonRoleAccessMethod_Type(Integer32):
    """Custom type commonRoleAccessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("snmp", 2))
    )


_CommonRoleAccessMethod_Type.__name__ = "Integer32"
_CommonRoleAccessMethod_Object = MibTableColumn
commonRoleAccessMethod = _CommonRoleAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 1),
    _CommonRoleAccessMethod_Type()
)
commonRoleAccessMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commonRoleAccessMethod.setStatus("current")


class _CommonRoleSupportedOperation_Type(Bits):
    """Custom type commonRoleSupportedOperation based on Bits"""
    namedValues = NamedValues(
        *(("clear", 0),
          ("config", 1),
          ("debug", 2),
          ("exec", 4),
          ("read", 5),
          ("readWrite", 6),
          ("show", 3))
    )

_CommonRoleSupportedOperation_Type.__name__ = "Bits"
_CommonRoleSupportedOperation_Object = MibTableColumn
commonRoleSupportedOperation = _CommonRoleSupportedOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 2),
    _CommonRoleSupportedOperation_Type()
)
commonRoleSupportedOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRoleSupportedOperation.setStatus("current")
_CcrRoleConfig_ObjectIdentity = ObjectIdentity
ccrRoleConfig = _CcrRoleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2)
)


class _CommonRoleMaxRoles_Type(Unsigned32):
    """Custom type commonRoleMaxRoles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommonRoleMaxRoles_Type.__name__ = "Unsigned32"
_CommonRoleMaxRoles_Object = MibScalar
commonRoleMaxRoles = _CommonRoleMaxRoles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 1),
    _CommonRoleMaxRoles_Type()
)
commonRoleMaxRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRoleMaxRoles.setStatus("current")
_CommonRoleTable_Object = MibTable
commonRoleTable = _CommonRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2)
)
if mibBuilder.loadTexts:
    commonRoleTable.setStatus("current")
_CommonRoleEntry_Object = MibTableRow
commonRoleEntry = _CommonRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1)
)
commonRoleEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"),
)
if mibBuilder.loadTexts:
    commonRoleEntry.setStatus("current")


class _CommonRoleName_Type(SnmpAdminString):
    """Custom type commonRoleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CommonRoleName_Type.__name__ = "SnmpAdminString"
_CommonRoleName_Object = MibTableColumn
commonRoleName = _CommonRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 1),
    _CommonRoleName_Type()
)
commonRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commonRoleName.setStatus("current")


class _CommonRoleDescription_Type(SnmpAdminString):
    """Custom type commonRoleDescription based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CommonRoleDescription_Type.__name__ = "SnmpAdminString"
_CommonRoleDescription_Object = MibTableColumn
commonRoleDescription = _CommonRoleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 2),
    _CommonRoleDescription_Type()
)
commonRoleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleDescription.setStatus("current")


class _CommonRoleScopeRestriction_Type(Integer32):
    """Custom type commonRoleScopeRestriction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vsan", 2))
    )


_CommonRoleScopeRestriction_Type.__name__ = "Integer32"
_CommonRoleScopeRestriction_Object = MibTableColumn
commonRoleScopeRestriction = _CommonRoleScopeRestriction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 3),
    _CommonRoleScopeRestriction_Type()
)
commonRoleScopeRestriction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleScopeRestriction.setStatus("current")


class _CommonRoleScope1_Type(OctetString):
    """Custom type commonRoleScope1 based on OctetString"""
    defaultHexValue = ""


_CommonRoleScope1_Object = MibTableColumn
commonRoleScope1 = _CommonRoleScope1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 4),
    _CommonRoleScope1_Type()
)
commonRoleScope1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleScope1.setStatus("current")


class _CommonRoleScope2_Type(OctetString):
    """Custom type commonRoleScope2 based on OctetString"""
    defaultHexValue = ""


_CommonRoleScope2_Object = MibTableColumn
commonRoleScope2 = _CommonRoleScope2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 5),
    _CommonRoleScope2_Type()
)
commonRoleScope2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleScope2.setStatus("current")
_CommonRoleRowStatus_Type = RowStatus
_CommonRoleRowStatus_Object = MibTableColumn
commonRoleRowStatus = _CommonRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 6),
    _CommonRoleRowStatus_Type()
)
commonRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleRowStatus.setStatus("current")
_CcrRuleConfig_ObjectIdentity = ObjectIdentity
ccrRuleConfig = _CcrRuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3)
)


class _CommonRoleMaxRulesPerRole_Type(Unsigned32):
    """Custom type commonRoleMaxRulesPerRole based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommonRoleMaxRulesPerRole_Type.__name__ = "Unsigned32"
_CommonRoleMaxRulesPerRole_Object = MibScalar
commonRoleMaxRulesPerRole = _CommonRoleMaxRulesPerRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 1),
    _CommonRoleMaxRulesPerRole_Type()
)
commonRoleMaxRulesPerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRoleMaxRulesPerRole.setStatus("current")
_CommonRoleRuleTable_Object = MibTable
commonRoleRuleTable = _CommonRoleRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2)
)
if mibBuilder.loadTexts:
    commonRoleRuleTable.setStatus("current")
_CommonRoleRuleEntry_Object = MibTableRow
commonRoleRuleEntry = _CommonRoleRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1)
)
commonRoleRuleEntry.setIndexNames(
    (0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"),
    (0, "CISCO-COMMON-ROLES-MIB", "commonRoleRuleIndex"),
)
if mibBuilder.loadTexts:
    commonRoleRuleEntry.setStatus("current")


class _CommonRoleRuleIndex_Type(Unsigned32):
    """Custom type commonRoleRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CommonRoleRuleIndex_Type.__name__ = "Unsigned32"
_CommonRoleRuleIndex_Object = MibTableColumn
commonRoleRuleIndex = _CommonRoleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 1),
    _CommonRoleRuleIndex_Type()
)
commonRoleRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commonRoleRuleIndex.setStatus("current")


class _CommonRoleRuleFeatureName_Type(SnmpAdminString):
    """Custom type commonRoleRuleFeatureName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CommonRoleRuleFeatureName_Type.__name__ = "SnmpAdminString"
_CommonRoleRuleFeatureName_Object = MibTableColumn
commonRoleRuleFeatureName = _CommonRoleRuleFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 2),
    _CommonRoleRuleFeatureName_Type()
)
commonRoleRuleFeatureName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleRuleFeatureName.setStatus("current")
_CommonRoleRuleOperation_Type = CommonRoleOperation
_CommonRoleRuleOperation_Object = MibTableColumn
commonRoleRuleOperation = _CommonRoleRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 3),
    _CommonRoleRuleOperation_Type()
)
commonRoleRuleOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleRuleOperation.setStatus("current")


class _CommonRoleRuleOperPermitted_Type(TruthValue):
    """Custom type commonRoleRuleOperPermitted based on TruthValue"""


_CommonRoleRuleOperPermitted_Object = MibTableColumn
commonRoleRuleOperPermitted = _CommonRoleRuleOperPermitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 4),
    _CommonRoleRuleOperPermitted_Type()
)
commonRoleRuleOperPermitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleRuleOperPermitted.setStatus("current")
_CommonRoleRuleRowStatus_Type = RowStatus
_CommonRoleRuleRowStatus_Object = MibTableColumn
commonRoleRuleRowStatus = _CommonRoleRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 5),
    _CommonRoleRuleRowStatus_Type()
)
commonRoleRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonRoleRuleRowStatus.setStatus("current")
_CiscoCommonRolesMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCommonRolesMIBConformance = _CiscoCommonRolesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2)
)
_CiscoCommonRolesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCommonRolesMIBCompliances = _CiscoCommonRolesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1)
)
_CiscoCommonRolesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCommonRolesMIBGroups = _CiscoCommonRolesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2)
)

# Managed Objects groups

ccrmConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 1)
)
ccrmConfigurationGroup.setObjects(
      *(("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureName"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureOperation"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleDescription"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleScopeRestriction"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleScope1"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleScope2"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleRowStatus"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleFeatureName"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperation"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperPermitted"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ccrmConfigurationGroup.setStatus("current")

ccrmConfigurationExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 2)
)
ccrmConfigurationExtGroup.setObjects(
      *(("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"),
        ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"))
)
if mibBuilder.loadTexts:
    ccrmConfigurationExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCommonRolesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCommonRolesMIBCompliance.setStatus(
        "current"
    )

ciscoCommonRolesExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCommonRolesExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-COMMON-ROLES-MIB",
    **{"CommonRoleOperation": CommonRoleOperation,
       "ciscoCommonRolesMIB": ciscoCommonRolesMIB,
       "ciscoCommonRolesNotifications": ciscoCommonRolesNotifications,
       "ciscoCommonRolesMIBObjects": ciscoCommonRolesMIBObjects,
       "ccrInfo": ccrInfo,
       "commonRoleFeatureTable": commonRoleFeatureTable,
       "commonRoleFeatureEntry": commonRoleFeatureEntry,
       "commonRoleFeatureIndex": commonRoleFeatureIndex,
       "commonRoleFeatureName": commonRoleFeatureName,
       "commonRoleFeatureOperation": commonRoleFeatureOperation,
       "commonRoleSupportedOperTable": commonRoleSupportedOperTable,
       "commonRoleSupportedOperEntry": commonRoleSupportedOperEntry,
       "commonRoleAccessMethod": commonRoleAccessMethod,
       "commonRoleSupportedOperation": commonRoleSupportedOperation,
       "ccrRoleConfig": ccrRoleConfig,
       "commonRoleMaxRoles": commonRoleMaxRoles,
       "commonRoleTable": commonRoleTable,
       "commonRoleEntry": commonRoleEntry,
       "commonRoleName": commonRoleName,
       "commonRoleDescription": commonRoleDescription,
       "commonRoleScopeRestriction": commonRoleScopeRestriction,
       "commonRoleScope1": commonRoleScope1,
       "commonRoleScope2": commonRoleScope2,
       "commonRoleRowStatus": commonRoleRowStatus,
       "ccrRuleConfig": ccrRuleConfig,
       "commonRoleMaxRulesPerRole": commonRoleMaxRulesPerRole,
       "commonRoleRuleTable": commonRoleRuleTable,
       "commonRoleRuleEntry": commonRoleRuleEntry,
       "commonRoleRuleIndex": commonRoleRuleIndex,
       "commonRoleRuleFeatureName": commonRoleRuleFeatureName,
       "commonRoleRuleOperation": commonRoleRuleOperation,
       "commonRoleRuleOperPermitted": commonRoleRuleOperPermitted,
       "commonRoleRuleRowStatus": commonRoleRuleRowStatus,
       "ciscoCommonRolesMIBConformance": ciscoCommonRolesMIBConformance,
       "ciscoCommonRolesMIBCompliances": ciscoCommonRolesMIBCompliances,
       "ciscoCommonRolesMIBCompliance": ciscoCommonRolesMIBCompliance,
       "ciscoCommonRolesExtMIBCompliance": ciscoCommonRolesExtMIBCompliance,
       "ciscoCommonRolesMIBGroups": ciscoCommonRolesMIBGroups,
       "ccrmConfigurationGroup": ccrmConfigurationGroup,
       "ccrmConfigurationExtGroup": ccrmConfigurationExtGroup}
)
