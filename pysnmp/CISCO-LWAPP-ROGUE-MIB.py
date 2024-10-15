# SNMP MIB module (CISCO-LWAPP-ROGUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-ROGUE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:57 2024
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

(cLApName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRogueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610)
)
ciscoLwappRogueMIB.setRevisions(
        ("2014-07-14 00:00",
         "2011-09-07 00:00",
         "2011-03-11 00:00",
         "2010-07-17 00:00",
         "2007-02-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CLAutoContainActions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 1),
          ("contain", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRogueMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBNotifs = _CiscoLwappRogueMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0)
)
_CiscoLwappRogueMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBObjects = _CiscoLwappRogueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1)
)
_CLRogueConfig_ObjectIdentity = ObjectIdentity
cLRogueConfig = _CLRogueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1)
)
_CLRoguePolicyConfig_ObjectIdentity = ObjectIdentity
cLRoguePolicyConfig = _CLRoguePolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1)
)


class _CLRogueAdhocRogueReportEnable_Type(TruthValue):
    """Custom type cLRogueAdhocRogueReportEnable based on TruthValue"""


_CLRogueAdhocRogueReportEnable_Object = MibScalar
cLRogueAdhocRogueReportEnable = _CLRogueAdhocRogueReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 1),
    _CLRogueAdhocRogueReportEnable_Type()
)
cLRogueAdhocRogueReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueAdhocRogueReportEnable.setStatus("current")


class _CLRogueReportInterval_Type(Unsigned32):
    """Custom type cLRogueReportInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CLRogueReportInterval_Type.__name__ = "Unsigned32"
_CLRogueReportInterval_Object = MibScalar
cLRogueReportInterval = _CLRogueReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 2),
    _CLRogueReportInterval_Type()
)
cLRogueReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueReportInterval.setUnits("seconds")


class _CLRogueMinimumRssi_Type(Integer32):
    """Custom type cLRogueMinimumRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -70),
    )


_CLRogueMinimumRssi_Type.__name__ = "Integer32"
_CLRogueMinimumRssi_Object = MibScalar
cLRogueMinimumRssi = _CLRogueMinimumRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 3),
    _CLRogueMinimumRssi_Type()
)
cLRogueMinimumRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueMinimumRssi.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueMinimumRssi.setUnits("dBm")


class _CLRogueTransientInterval_Type(Unsigned32):
    """Custom type cLRogueTransientInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 1800),
    )


_CLRogueTransientInterval_Type.__name__ = "Unsigned32"
_CLRogueTransientInterval_Object = MibScalar
cLRogueTransientInterval = _CLRogueTransientInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 4),
    _CLRogueTransientInterval_Type()
)
cLRogueTransientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueTransientInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueTransientInterval.setUnits("seconds")
_CLRogueClientNumThreshold_Type = Unsigned32
_CLRogueClientNumThreshold_Object = MibScalar
cLRogueClientNumThreshold = _CLRogueClientNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 5),
    _CLRogueClientNumThreshold_Type()
)
cLRogueClientNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueClientNumThreshold.setStatus("current")


class _CLRogueDetectionSecurityLevel_Type(Integer32):
    """Custom type cLRogueDetectionSecurityLevel based on Integer32"""
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
        *(("critical", 3),
          ("custom", 4),
          ("high", 2),
          ("low", 1))
    )


_CLRogueDetectionSecurityLevel_Type.__name__ = "Integer32"
_CLRogueDetectionSecurityLevel_Object = MibScalar
cLRogueDetectionSecurityLevel = _CLRogueDetectionSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 6),
    _CLRogueDetectionSecurityLevel_Type()
)
cLRogueDetectionSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueDetectionSecurityLevel.setStatus("current")


class _CLRogueValidateRogueClientsAgainstMse_Type(Integer32):
    """Custom type cLRogueValidateRogueClientsAgainstMse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRogueValidateRogueClientsAgainstMse_Type.__name__ = "Integer32"
_CLRogueValidateRogueClientsAgainstMse_Object = MibScalar
cLRogueValidateRogueClientsAgainstMse = _CLRogueValidateRogueClientsAgainstMse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 7),
    _CLRogueValidateRogueClientsAgainstMse_Type()
)
cLRogueValidateRogueClientsAgainstMse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueValidateRogueClientsAgainstMse.setStatus("current")


class _CLRogueAdhocRogueNotifEnabled_Type(TruthValue):
    """Custom type cLRogueAdhocRogueNotifEnabled based on TruthValue"""


_CLRogueAdhocRogueNotifEnabled_Object = MibScalar
cLRogueAdhocRogueNotifEnabled = _CLRogueAdhocRogueNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 2),
    _CLRogueAdhocRogueNotifEnabled_Type()
)
cLRogueAdhocRogueNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueAdhocRogueNotifEnabled.setStatus("current")
_CLRogueRuleConfig_ObjectIdentity = ObjectIdentity
cLRogueRuleConfig = _CLRogueRuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3)
)
_CLRuleConfigTable_Object = MibTable
cLRuleConfigTable = _CLRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLRuleConfigTable.setStatus("current")
_CLRuleConfigEntry_Object = MibTableRow
cLRuleConfigEntry = _CLRuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1)
)
cLRuleConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
)
if mibBuilder.loadTexts:
    cLRuleConfigEntry.setStatus("current")


class _CLRuleName_Type(SnmpAdminString):
    """Custom type cLRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRuleName_Type.__name__ = "SnmpAdminString"
_CLRuleName_Object = MibTableColumn
cLRuleName = _CLRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 1),
    _CLRuleName_Type()
)
cLRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRuleName.setStatus("current")


class _CLRuleRogueType_Type(Integer32):
    """Custom type cLRuleRogueType based on Integer32"""
    defaultValue = 4

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
        *(("custom", 4),
          ("friendly", 1),
          ("malicious", 2),
          ("unclassified", 3))
    )


_CLRuleRogueType_Type.__name__ = "Integer32"
_CLRuleRogueType_Object = MibTableColumn
cLRuleRogueType = _CLRuleRogueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 2),
    _CLRuleRogueType_Type()
)
cLRuleRogueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleRogueType.setStatus("current")


class _CLRuleConditionsMatch_Type(Integer32):
    """Custom type cLRuleConditionsMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_CLRuleConditionsMatch_Type.__name__ = "Integer32"
_CLRuleConditionsMatch_Object = MibTableColumn
cLRuleConditionsMatch = _CLRuleConditionsMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 3),
    _CLRuleConditionsMatch_Type()
)
cLRuleConditionsMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleConditionsMatch.setStatus("current")
_CLRulePriority_Type = Unsigned32
_CLRulePriority_Object = MibTableColumn
cLRulePriority = _CLRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 4),
    _CLRulePriority_Type()
)
cLRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRulePriority.setStatus("current")
_CLRuleEnable_Type = TruthValue
_CLRuleEnable_Object = MibTableColumn
cLRuleEnable = _CLRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 5),
    _CLRuleEnable_Type()
)
cLRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleEnable.setStatus("current")


class _CLRuleStorageType_Type(StorageType):
    """Custom type cLRuleStorageType based on StorageType"""


_CLRuleStorageType_Object = MibTableColumn
cLRuleStorageType = _CLRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 6),
    _CLRuleStorageType_Type()
)
cLRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleStorageType.setStatus("current")
_CLRuleRowStatus_Type = RowStatus
_CLRuleRowStatus_Object = MibTableColumn
cLRuleRowStatus = _CLRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 7),
    _CLRuleRowStatus_Type()
)
cLRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleRowStatus.setStatus("current")
_CLConditionConfigTable_Object = MibTable
cLConditionConfigTable = _CLConditionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLConditionConfigTable.setStatus("current")
_CLConditionConfigEntry_Object = MibTableRow
cLConditionConfigEntry = _CLConditionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1)
)
cLConditionConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"),
)
if mibBuilder.loadTexts:
    cLConditionConfigEntry.setStatus("current")


class _CLConditionName_Type(SnmpAdminString):
    """Custom type cLConditionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLConditionName_Type.__name__ = "SnmpAdminString"
_CLConditionName_Object = MibTableColumn
cLConditionName = _CLConditionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 1),
    _CLConditionName_Type()
)
cLConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLConditionName.setStatus("current")


class _CLConditionType_Type(Integer32):
    """Custom type cLConditionType based on Integer32"""
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
        *(("clientCount", 4),
          ("duration", 3),
          ("managedSsid", 1),
          ("noEncryption", 5),
          ("rssi", 2),
          ("userConfigSsid", 6))
    )


_CLConditionType_Type.__name__ = "Integer32"
_CLConditionType_Object = MibTableColumn
cLConditionType = _CLConditionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 2),
    _CLConditionType_Type()
)
cLConditionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionType.setStatus("current")
_CLConditionValue_Type = Integer32
_CLConditionValue_Object = MibTableColumn
cLConditionValue = _CLConditionValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 3),
    _CLConditionValue_Type()
)
cLConditionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionValue.setStatus("current")
_CLConditionEnable_Type = TruthValue
_CLConditionEnable_Object = MibTableColumn
cLConditionEnable = _CLConditionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 4),
    _CLConditionEnable_Type()
)
cLConditionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionEnable.setStatus("current")


class _CLConditionStorageType_Type(StorageType):
    """Custom type cLConditionStorageType based on StorageType"""


_CLConditionStorageType_Object = MibTableColumn
cLConditionStorageType = _CLConditionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 5),
    _CLConditionStorageType_Type()
)
cLConditionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionStorageType.setStatus("current")
_CLConditionRowStatus_Type = RowStatus
_CLConditionRowStatus_Object = MibTableColumn
cLConditionRowStatus = _CLConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 6),
    _CLConditionRowStatus_Type()
)
cLConditionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionRowStatus.setStatus("current")


class _CLConditionRssi_Type(Integer32):
    """Custom type cLConditionRssi based on Integer32"""
    defaultValue = 0


_CLConditionRssi_Object = MibTableColumn
cLConditionRssi = _CLConditionRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 7),
    _CLConditionRssi_Type()
)
cLConditionRssi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionRssi.setStatus("current")


class _CLConditionClientCount_Type(Unsigned32):
    """Custom type cLConditionClientCount based on Unsigned32"""
    defaultValue = 0


_CLConditionClientCount_Object = MibTableColumn
cLConditionClientCount = _CLConditionClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 8),
    _CLConditionClientCount_Type()
)
cLConditionClientCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionClientCount.setStatus("current")


class _CLConditionNoEncryptionEnabled_Type(TruthValue):
    """Custom type cLConditionNoEncryptionEnabled based on TruthValue"""


_CLConditionNoEncryptionEnabled_Object = MibTableColumn
cLConditionNoEncryptionEnabled = _CLConditionNoEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 9),
    _CLConditionNoEncryptionEnabled_Type()
)
cLConditionNoEncryptionEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionNoEncryptionEnabled.setStatus("current")


class _CLConditionManagedSsidEnabled_Type(TruthValue):
    """Custom type cLConditionManagedSsidEnabled based on TruthValue"""


_CLConditionManagedSsidEnabled_Object = MibTableColumn
cLConditionManagedSsidEnabled = _CLConditionManagedSsidEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 10),
    _CLConditionManagedSsidEnabled_Type()
)
cLConditionManagedSsidEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionManagedSsidEnabled.setStatus("current")


class _CLConditionDuration_Type(Unsigned32):
    """Custom type cLConditionDuration based on Unsigned32"""
    defaultValue = 0


_CLConditionDuration_Object = MibTableColumn
cLConditionDuration = _CLConditionDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 11),
    _CLConditionDuration_Type()
)
cLConditionDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionDuration.setStatus("current")
if mibBuilder.loadTexts:
    cLConditionDuration.setUnits("seconds")
_CLConditionSsidConfigTable_Object = MibTable
cLConditionSsidConfigTable = _CLConditionSsidConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLConditionSsidConfigTable.setStatus("current")
_CLConditionSsidConfigEntry_Object = MibTableRow
cLConditionSsidConfigEntry = _CLConditionSsidConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1)
)
cLConditionSsidConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidValue"),
)
if mibBuilder.loadTexts:
    cLConditionSsidConfigEntry.setStatus("current")


class _CLConditionSsidValue_Type(SnmpAdminString):
    """Custom type cLConditionSsidValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLConditionSsidValue_Type.__name__ = "SnmpAdminString"
_CLConditionSsidValue_Object = MibTableColumn
cLConditionSsidValue = _CLConditionSsidValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 1),
    _CLConditionSsidValue_Type()
)
cLConditionSsidValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLConditionSsidValue.setStatus("current")


class _CLConditionSsidStorageType_Type(StorageType):
    """Custom type cLConditionSsidStorageType based on StorageType"""


_CLConditionSsidStorageType_Object = MibTableColumn
cLConditionSsidStorageType = _CLConditionSsidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 2),
    _CLConditionSsidStorageType_Type()
)
cLConditionSsidStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionSsidStorageType.setStatus("current")
_CLConditionSsidRowStatus_Type = RowStatus
_CLConditionSsidRowStatus_Object = MibTableColumn
cLConditionSsidRowStatus = _CLConditionSsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 3),
    _CLConditionSsidRowStatus_Type()
)
cLConditionSsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionSsidRowStatus.setStatus("current")
_CLRogueIgnoreListConfig_ObjectIdentity = ObjectIdentity
cLRogueIgnoreListConfig = _CLRogueIgnoreListConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4)
)
_CLRogueIgnoreListTable_Object = MibTable
cLRogueIgnoreListTable = _CLRogueIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLRogueIgnoreListTable.setStatus("current")
_CLRogueIgnoreListEntry_Object = MibTableRow
cLRogueIgnoreListEntry = _CLRogueIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1)
)
cLRogueIgnoreListEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListMACAddress"),
)
if mibBuilder.loadTexts:
    cLRogueIgnoreListEntry.setStatus("current")
_CLRogueIgnoreListMACAddress_Type = MacAddress
_CLRogueIgnoreListMACAddress_Object = MibTableColumn
cLRogueIgnoreListMACAddress = _CLRogueIgnoreListMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 1),
    _CLRogueIgnoreListMACAddress_Type()
)
cLRogueIgnoreListMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueIgnoreListMACAddress.setStatus("current")


class _CLRogueIgnoreListStorageType_Type(StorageType):
    """Custom type cLRogueIgnoreListStorageType based on StorageType"""


_CLRogueIgnoreListStorageType_Object = MibTableColumn
cLRogueIgnoreListStorageType = _CLRogueIgnoreListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 2),
    _CLRogueIgnoreListStorageType_Type()
)
cLRogueIgnoreListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueIgnoreListStorageType.setStatus("current")
_CLRogueIgnoreListRowStatus_Type = RowStatus
_CLRogueIgnoreListRowStatus_Object = MibTableColumn
cLRogueIgnoreListRowStatus = _CLRogueIgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 3),
    _CLRogueIgnoreListRowStatus_Type()
)
cLRogueIgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueIgnoreListRowStatus.setStatus("current")
_CLRldpAutoContainConfig_ObjectIdentity = ObjectIdentity
cLRldpAutoContainConfig = _CLRldpAutoContainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5)
)


class _CLRldpAutoContainFeatureOnWiredNetwork_Type(Integer32):
    """Custom type cLRldpAutoContainFeatureOnWiredNetwork based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRldpAutoContainFeatureOnWiredNetwork_Type.__name__ = "Integer32"
_CLRldpAutoContainFeatureOnWiredNetwork_Object = MibScalar
cLRldpAutoContainFeatureOnWiredNetwork = _CLRldpAutoContainFeatureOnWiredNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 1),
    _CLRldpAutoContainFeatureOnWiredNetwork_Type()
)
cLRldpAutoContainFeatureOnWiredNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainFeatureOnWiredNetwork.setStatus("current")


class _CLRldpAutoContainRoguesAdvertisingSsid_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainRoguesAdvertisingSsid based on CLAutoContainActions"""


_CLRldpAutoContainRoguesAdvertisingSsid_Object = MibScalar
cLRldpAutoContainRoguesAdvertisingSsid = _CLRldpAutoContainRoguesAdvertisingSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 2),
    _CLRldpAutoContainRoguesAdvertisingSsid_Type()
)
cLRldpAutoContainRoguesAdvertisingSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainRoguesAdvertisingSsid.setStatus("current")


class _CLRldpAutoContainAdhocNetworks_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainAdhocNetworks based on CLAutoContainActions"""


_CLRldpAutoContainAdhocNetworks_Object = MibScalar
cLRldpAutoContainAdhocNetworks = _CLRldpAutoContainAdhocNetworks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 3),
    _CLRldpAutoContainAdhocNetworks_Type()
)
cLRldpAutoContainAdhocNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainAdhocNetworks.setStatus("current")


class _CLRldpAutoContainTrustedClientsOnRogueAps_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainTrustedClientsOnRogueAps based on CLAutoContainActions"""


_CLRldpAutoContainTrustedClientsOnRogueAps_Object = MibScalar
cLRldpAutoContainTrustedClientsOnRogueAps = _CLRldpAutoContainTrustedClientsOnRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 4),
    _CLRldpAutoContainTrustedClientsOnRogueAps_Type()
)
cLRldpAutoContainTrustedClientsOnRogueAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainTrustedClientsOnRogueAps.setStatus("current")


class _CLRldpAutoContainLevel_Type(Integer32):
    """Custom type cLRldpAutoContainLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLRldpAutoContainLevel_Type.__name__ = "Integer32"
_CLRldpAutoContainLevel_Object = MibScalar
cLRldpAutoContainLevel = _CLRldpAutoContainLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 5),
    _CLRldpAutoContainLevel_Type()
)
cLRldpAutoContainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainLevel.setStatus("current")


class _CLRldpAutoContainOnlyforMonitorModeAps_Type(Integer32):
    """Custom type cLRldpAutoContainOnlyforMonitorModeAps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRldpAutoContainOnlyforMonitorModeAps_Type.__name__ = "Integer32"
_CLRldpAutoContainOnlyforMonitorModeAps_Object = MibScalar
cLRldpAutoContainOnlyforMonitorModeAps = _CLRldpAutoContainOnlyforMonitorModeAps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 6),
    _CLRldpAutoContainOnlyforMonitorModeAps_Type()
)
cLRldpAutoContainOnlyforMonitorModeAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainOnlyforMonitorModeAps.setStatus("current")
_CLRogueApConfig_ObjectIdentity = ObjectIdentity
cLRogueApConfig = _CLRogueApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6)
)
_CLRogueApTable_Object = MibTable
cLRogueApTable = _CLRogueApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLRogueApTable.setStatus("current")
_CLRogueApEntry_Object = MibTableRow
cLRogueApEntry = _CLRogueApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1)
)
cLRogueApEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueApMACAddress"),
)
if mibBuilder.loadTexts:
    cLRogueApEntry.setStatus("current")
_CLRogueApMACAddress_Type = MacAddress
_CLRogueApMACAddress_Object = MibTableColumn
cLRogueApMACAddress = _CLRogueApMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 1),
    _CLRogueApMACAddress_Type()
)
cLRogueApMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueApMACAddress.setStatus("current")


class _CLRogueApClassType_Type(Integer32):
    """Custom type cLRogueApClassType based on Integer32"""
    defaultValue = 4

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
        *(("custom", 4),
          ("friendly", 1),
          ("malicious", 2),
          ("unclassified", 3))
    )


_CLRogueApClassType_Type.__name__ = "Integer32"
_CLRogueApClassType_Object = MibTableColumn
cLRogueApClassType = _CLRogueApClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 2),
    _CLRogueApClassType_Type()
)
cLRogueApClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApClassType.setStatus("current")


class _CLRogueApState_Type(Integer32):
    """Custom type cLRogueApState based on Integer32"""
    defaultValue = 2

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
        *(("acknowledge", 5),
          ("alert", 2),
          ("contained", 6),
          ("containedPending", 8),
          ("detectedLrad", 3),
          ("initializing", 11),
          ("known", 4),
          ("knownContained", 9),
          ("pending", 1),
          ("threat", 7),
          ("trustedMissing", 10))
    )


_CLRogueApState_Type.__name__ = "Integer32"
_CLRogueApState_Object = MibTableColumn
cLRogueApState = _CLRogueApState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 3),
    _CLRogueApState_Type()
)
cLRogueApState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApState.setStatus("current")


class _CLRogueApStorageType_Type(StorageType):
    """Custom type cLRogueApStorageType based on StorageType"""


_CLRogueApStorageType_Object = MibTableColumn
cLRogueApStorageType = _CLRogueApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 4),
    _CLRogueApStorageType_Type()
)
cLRogueApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApStorageType.setStatus("current")
_CLRogueApRowStatus_Type = RowStatus
_CLRogueApRowStatus_Object = MibTableColumn
cLRogueApRowStatus = _CLRogueApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 5),
    _CLRogueApRowStatus_Type()
)
cLRogueApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApRowStatus.setStatus("current")
_CiscoLwappRogueMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBConform = _CiscoLwappRogueMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2)
)
_CiscoLwappRogueMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBCompliances = _CiscoLwappRogueMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1)
)
_CiscoLwappRogueMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBGroups = _CiscoLwappRogueMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2)
)

# Managed Objects groups

ciscoLwappRogueConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 1)
)
ciscoLwappRogueConfigGroup.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueReportEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigGroup.setStatus("current")

ciscoLwappRogueConfigSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 3)
)
ciscoLwappRogueConfigSup1Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup1Group.setStatus("deprecated")

ciscoLwappRogueConfigSup2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 4)
)
ciscoLwappRogueConfigSup2Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup2Group.setStatus("deprecated")

ciscoLwappRogueConfigSup3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 5)
)
ciscoLwappRogueConfigSup3Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueReportInterval"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueMinimumRssi"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueTransientInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup3Group.setStatus("current")

ciscoLwappRogueConfigSup4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 6)
)
ciscoLwappRogueConfigSup4Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueApClassType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApState"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientNumThreshold"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueDetectionSecurityLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueValidateRogueClientsAgainstMse"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRssi"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionClientCount"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionNoEncryptionEnabled"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionManagedSsidEnabled"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionDuration"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup4Group.setStatus("current")


# Notification objects

cLRogueAdhocRogueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 1)
)
cLRogueAdhocRogueDetected.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    cLRogueAdhocRogueDetected.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappRogueNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 2)
)
ciscoLwappRogueNotifsGroup.setObjects(
    ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueDetected")
)
if mibBuilder.loadTexts:
    ciscoLwappRogueNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappRogueMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-ROGUE-MIB",
    **{"CLAutoContainActions": CLAutoContainActions,
       "ciscoLwappRogueMIB": ciscoLwappRogueMIB,
       "ciscoLwappRogueMIBNotifs": ciscoLwappRogueMIBNotifs,
       "cLRogueAdhocRogueDetected": cLRogueAdhocRogueDetected,
       "ciscoLwappRogueMIBObjects": ciscoLwappRogueMIBObjects,
       "cLRogueConfig": cLRogueConfig,
       "cLRoguePolicyConfig": cLRoguePolicyConfig,
       "cLRogueAdhocRogueReportEnable": cLRogueAdhocRogueReportEnable,
       "cLRogueReportInterval": cLRogueReportInterval,
       "cLRogueMinimumRssi": cLRogueMinimumRssi,
       "cLRogueTransientInterval": cLRogueTransientInterval,
       "cLRogueClientNumThreshold": cLRogueClientNumThreshold,
       "cLRogueDetectionSecurityLevel": cLRogueDetectionSecurityLevel,
       "cLRogueValidateRogueClientsAgainstMse": cLRogueValidateRogueClientsAgainstMse,
       "cLRogueAdhocRogueNotifEnabled": cLRogueAdhocRogueNotifEnabled,
       "cLRogueRuleConfig": cLRogueRuleConfig,
       "cLRuleConfigTable": cLRuleConfigTable,
       "cLRuleConfigEntry": cLRuleConfigEntry,
       "cLRuleName": cLRuleName,
       "cLRuleRogueType": cLRuleRogueType,
       "cLRuleConditionsMatch": cLRuleConditionsMatch,
       "cLRulePriority": cLRulePriority,
       "cLRuleEnable": cLRuleEnable,
       "cLRuleStorageType": cLRuleStorageType,
       "cLRuleRowStatus": cLRuleRowStatus,
       "cLConditionConfigTable": cLConditionConfigTable,
       "cLConditionConfigEntry": cLConditionConfigEntry,
       "cLConditionName": cLConditionName,
       "cLConditionType": cLConditionType,
       "cLConditionValue": cLConditionValue,
       "cLConditionEnable": cLConditionEnable,
       "cLConditionStorageType": cLConditionStorageType,
       "cLConditionRowStatus": cLConditionRowStatus,
       "cLConditionRssi": cLConditionRssi,
       "cLConditionClientCount": cLConditionClientCount,
       "cLConditionNoEncryptionEnabled": cLConditionNoEncryptionEnabled,
       "cLConditionManagedSsidEnabled": cLConditionManagedSsidEnabled,
       "cLConditionDuration": cLConditionDuration,
       "cLConditionSsidConfigTable": cLConditionSsidConfigTable,
       "cLConditionSsidConfigEntry": cLConditionSsidConfigEntry,
       "cLConditionSsidValue": cLConditionSsidValue,
       "cLConditionSsidStorageType": cLConditionSsidStorageType,
       "cLConditionSsidRowStatus": cLConditionSsidRowStatus,
       "cLRogueIgnoreListConfig": cLRogueIgnoreListConfig,
       "cLRogueIgnoreListTable": cLRogueIgnoreListTable,
       "cLRogueIgnoreListEntry": cLRogueIgnoreListEntry,
       "cLRogueIgnoreListMACAddress": cLRogueIgnoreListMACAddress,
       "cLRogueIgnoreListStorageType": cLRogueIgnoreListStorageType,
       "cLRogueIgnoreListRowStatus": cLRogueIgnoreListRowStatus,
       "cLRldpAutoContainConfig": cLRldpAutoContainConfig,
       "cLRldpAutoContainFeatureOnWiredNetwork": cLRldpAutoContainFeatureOnWiredNetwork,
       "cLRldpAutoContainRoguesAdvertisingSsid": cLRldpAutoContainRoguesAdvertisingSsid,
       "cLRldpAutoContainAdhocNetworks": cLRldpAutoContainAdhocNetworks,
       "cLRldpAutoContainTrustedClientsOnRogueAps": cLRldpAutoContainTrustedClientsOnRogueAps,
       "cLRldpAutoContainLevel": cLRldpAutoContainLevel,
       "cLRldpAutoContainOnlyforMonitorModeAps": cLRldpAutoContainOnlyforMonitorModeAps,
       "cLRogueApConfig": cLRogueApConfig,
       "cLRogueApTable": cLRogueApTable,
       "cLRogueApEntry": cLRogueApEntry,
       "cLRogueApMACAddress": cLRogueApMACAddress,
       "cLRogueApClassType": cLRogueApClassType,
       "cLRogueApState": cLRogueApState,
       "cLRogueApStorageType": cLRogueApStorageType,
       "cLRogueApRowStatus": cLRogueApRowStatus,
       "ciscoLwappRogueMIBConform": ciscoLwappRogueMIBConform,
       "ciscoLwappRogueMIBCompliances": ciscoLwappRogueMIBCompliances,
       "ciscoLwappRogueMIBCompliance": ciscoLwappRogueMIBCompliance,
       "ciscoLwappRogueMIBComplianceRev1": ciscoLwappRogueMIBComplianceRev1,
       "ciscoLwappRogueMIBComplianceRev2": ciscoLwappRogueMIBComplianceRev2,
       "ciscoLwappRogueMIBComplianceRev3": ciscoLwappRogueMIBComplianceRev3,
       "ciscoLwappRogueMIBComplianceRev4": ciscoLwappRogueMIBComplianceRev4,
       "ciscoLwappRogueMIBGroups": ciscoLwappRogueMIBGroups,
       "ciscoLwappRogueConfigGroup": ciscoLwappRogueConfigGroup,
       "ciscoLwappRogueNotifsGroup": ciscoLwappRogueNotifsGroup,
       "ciscoLwappRogueConfigSup1Group": ciscoLwappRogueConfigSup1Group,
       "ciscoLwappRogueConfigSup2Group": ciscoLwappRogueConfigSup2Group,
       "ciscoLwappRogueConfigSup3Group": ciscoLwappRogueConfigSup3Group,
       "ciscoLwappRogueConfigSup4Group": ciscoLwappRogueConfigSup4Group}
)
