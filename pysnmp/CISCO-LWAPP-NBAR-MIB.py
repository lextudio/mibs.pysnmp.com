# SNMP MIB module (CISCO-LWAPP-NBAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-NBAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:48 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLwappNbarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995)
)
ciscoLwappNbarMIB.setRevisions(
        ("2012-06-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappNbarMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBNotifs = _CiscoLwappNbarMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 0)
)
_CiscoLwappNbarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBObjects = _CiscoLwappNbarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1)
)
_CiscoLwappNbarTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarTableObjects = _CiscoLwappNbarTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1)
)
_CLNbarAVCProfileTable_Object = MibTable
cLNbarAVCProfileTable = _CLNbarAVCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLNbarAVCProfileTable.setStatus("current")
_CLNbarAVCProfileEntry_Object = MibTableRow
cLNbarAVCProfileEntry = _CLNbarAVCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 1, 1)
)
cLNbarAVCProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCProfileEntry.setStatus("current")


class _CLNbarAVCProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCProfileName_Object = MibTableColumn
cLNbarAVCProfileName = _CLNbarAVCProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 1, 1, 1),
    _CLNbarAVCProfileName_Type()
)
cLNbarAVCProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCProfileName.setStatus("current")
_CLNbarAVCProfileRowStatus_Type = RowStatus
_CLNbarAVCProfileRowStatus_Object = MibTableColumn
cLNbarAVCProfileRowStatus = _CLNbarAVCProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 1, 1, 2),
    _CLNbarAVCProfileRowStatus_Type()
)
cLNbarAVCProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCProfileRowStatus.setStatus("current")
_CLNbarAVCRuleTable_Object = MibTable
cLNbarAVCRuleTable = _CLNbarAVCRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLNbarAVCRuleTable.setStatus("current")
_CLNbarAVCRuleEntry_Object = MibTableRow
cLNbarAVCRuleEntry = _CLNbarAVCRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1)
)
cLNbarAVCRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleProfileName"),
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCRuleEntry.setStatus("current")


class _CLNbarAVCRuleProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCRuleProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCRuleProfileName_Object = MibTableColumn
cLNbarAVCRuleProfileName = _CLNbarAVCRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 1),
    _CLNbarAVCRuleProfileName_Type()
)
cLNbarAVCRuleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCRuleProfileName.setStatus("current")
_CLNbarAVCRuleApplicationName_Type = SnmpAdminString
_CLNbarAVCRuleApplicationName_Object = MibTableColumn
cLNbarAVCRuleApplicationName = _CLNbarAVCRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 2),
    _CLNbarAVCRuleApplicationName_Type()
)
cLNbarAVCRuleApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationName.setStatus("current")
_CLNbarAVCRuleApplicationGroupName_Type = SnmpAdminString
_CLNbarAVCRuleApplicationGroupName_Object = MibTableColumn
cLNbarAVCRuleApplicationGroupName = _CLNbarAVCRuleApplicationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 3),
    _CLNbarAVCRuleApplicationGroupName_Type()
)
cLNbarAVCRuleApplicationGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationGroupName.setStatus("current")


class _CLNbarAVCRuleApplicationAction_Type(Integer32):
    """Custom type cLNbarAVCRuleApplicationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("mark", 3),
          ("ratelimit", 4))
    )


_CLNbarAVCRuleApplicationAction_Type.__name__ = "Integer32"
_CLNbarAVCRuleApplicationAction_Object = MibTableColumn
cLNbarAVCRuleApplicationAction = _CLNbarAVCRuleApplicationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 4),
    _CLNbarAVCRuleApplicationAction_Type()
)
cLNbarAVCRuleApplicationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationAction.setStatus("current")
_CLNbarAVCRuleDscpValue_Type = Unsigned32
_CLNbarAVCRuleDscpValue_Object = MibTableColumn
cLNbarAVCRuleDscpValue = _CLNbarAVCRuleDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 5),
    _CLNbarAVCRuleDscpValue_Type()
)
cLNbarAVCRuleDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleDscpValue.setStatus("current")
_CLNbarAVCRuleRowStatus_Type = RowStatus
_CLNbarAVCRuleRowStatus_Object = MibTableColumn
cLNbarAVCRuleRowStatus = _CLNbarAVCRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 6),
    _CLNbarAVCRuleRowStatus_Type()
)
cLNbarAVCRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleRowStatus.setStatus("current")
_CLNbarAVCRuleAppAvgRateLimit_Type = Unsigned32
_CLNbarAVCRuleAppAvgRateLimit_Object = MibTableColumn
cLNbarAVCRuleAppAvgRateLimit = _CLNbarAVCRuleAppAvgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 7),
    _CLNbarAVCRuleAppAvgRateLimit_Type()
)
cLNbarAVCRuleAppAvgRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleAppAvgRateLimit.setStatus("current")
_CLNbarAVCRuleAppBurstRateLimit_Type = Unsigned32
_CLNbarAVCRuleAppBurstRateLimit_Object = MibTableColumn
cLNbarAVCRuleAppBurstRateLimit = _CLNbarAVCRuleAppBurstRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 1, 2, 1, 8),
    _CLNbarAVCRuleAppBurstRateLimit_Type()
)
cLNbarAVCRuleAppBurstRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleAppBurstRateLimit.setStatus("current")
_CiscoLwappNbarGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarGlobalObjects = _CiscoLwappNbarGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 2)
)
_CLNbarAVCEngineVersion_Type = OctetString
_CLNbarAVCEngineVersion_Object = MibScalar
cLNbarAVCEngineVersion = _CLNbarAVCEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 2, 1),
    _CLNbarAVCEngineVersion_Type()
)
cLNbarAVCEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCEngineVersion.setStatus("current")
_CLNbarAVCProtoPackName_Type = OctetString
_CLNbarAVCProtoPackName_Object = MibScalar
cLNbarAVCProtoPackName = _CLNbarAVCProtoPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 2, 2),
    _CLNbarAVCProtoPackName_Type()
)
cLNbarAVCProtoPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCProtoPackName.setStatus("current")
_CLNbarAVCProtoPackVer_Type = OctetString
_CLNbarAVCProtoPackVer_Object = MibScalar
cLNbarAVCProtoPackVer = _CLNbarAVCProtoPackVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 1, 2, 3),
    _CLNbarAVCProtoPackVer_Type()
)
cLNbarAVCProtoPackVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCProtoPackVer.setStatus("current")
_CiscoLwappNbarMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBConform = _CiscoLwappNbarMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2)
)
_CiscoLwappNbarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBCompliances = _CiscoLwappNbarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 1)
)
_CiscoLwappNbarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBGroups = _CiscoLwappNbarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 2)
)

# Managed Objects groups

cLNbarConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 2, 1)
)
cLNbarConfigGroup.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileRowStatus"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationGroupName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationAction"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleDscpValue"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleRowStatus"))
)
if mibBuilder.loadTexts:
    cLNbarConfigGroup.setStatus("current")

cLNbarGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 2, 2)
)
cLNbarGlobalGroup.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCEngineVersion"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"))
)
if mibBuilder.loadTexts:
    cLNbarGlobalGroup.setStatus("current")


# Notification objects

cLAVCProtoPackLoadNotifFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 0, 1)
)
cLAVCProtoPackLoadNotifFailed.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"))
)
if mibBuilder.loadTexts:
    cLAVCProtoPackLoadNotifFailed.setStatus(
        "current"
    )

cLAVCProtoPackLoadNotifSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 0, 2)
)
cLAVCProtoPackLoadNotifSuccess.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"))
)
if mibBuilder.loadTexts:
    cLAVCProtoPackLoadNotifSuccess.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappNbarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappNbarMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappNbarMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99995, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappNbarMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-NBAR-MIB",
    **{"ciscoLwappNbarMIB": ciscoLwappNbarMIB,
       "ciscoLwappNbarMIBNotifs": ciscoLwappNbarMIBNotifs,
       "cLAVCProtoPackLoadNotifFailed": cLAVCProtoPackLoadNotifFailed,
       "cLAVCProtoPackLoadNotifSuccess": cLAVCProtoPackLoadNotifSuccess,
       "ciscoLwappNbarMIBObjects": ciscoLwappNbarMIBObjects,
       "ciscoLwappNbarTableObjects": ciscoLwappNbarTableObjects,
       "cLNbarAVCProfileTable": cLNbarAVCProfileTable,
       "cLNbarAVCProfileEntry": cLNbarAVCProfileEntry,
       "cLNbarAVCProfileName": cLNbarAVCProfileName,
       "cLNbarAVCProfileRowStatus": cLNbarAVCProfileRowStatus,
       "cLNbarAVCRuleTable": cLNbarAVCRuleTable,
       "cLNbarAVCRuleEntry": cLNbarAVCRuleEntry,
       "cLNbarAVCRuleProfileName": cLNbarAVCRuleProfileName,
       "cLNbarAVCRuleApplicationName": cLNbarAVCRuleApplicationName,
       "cLNbarAVCRuleApplicationGroupName": cLNbarAVCRuleApplicationGroupName,
       "cLNbarAVCRuleApplicationAction": cLNbarAVCRuleApplicationAction,
       "cLNbarAVCRuleDscpValue": cLNbarAVCRuleDscpValue,
       "cLNbarAVCRuleRowStatus": cLNbarAVCRuleRowStatus,
       "cLNbarAVCRuleAppAvgRateLimit": cLNbarAVCRuleAppAvgRateLimit,
       "cLNbarAVCRuleAppBurstRateLimit": cLNbarAVCRuleAppBurstRateLimit,
       "ciscoLwappNbarGlobalObjects": ciscoLwappNbarGlobalObjects,
       "cLNbarAVCEngineVersion": cLNbarAVCEngineVersion,
       "cLNbarAVCProtoPackName": cLNbarAVCProtoPackName,
       "cLNbarAVCProtoPackVer": cLNbarAVCProtoPackVer,
       "ciscoLwappNbarMIBConform": ciscoLwappNbarMIBConform,
       "ciscoLwappNbarMIBCompliances": ciscoLwappNbarMIBCompliances,
       "ciscoLwappNbarMIBCompliance": ciscoLwappNbarMIBCompliance,
       "ciscoLwappNbarMIBComplianceRev1": ciscoLwappNbarMIBComplianceRev1,
       "ciscoLwappNbarMIBGroups": ciscoLwappNbarMIBGroups,
       "cLNbarConfigGroup": cLNbarConfigGroup,
       "cLNbarGlobalGroup": cLNbarGlobalGroup}
)
