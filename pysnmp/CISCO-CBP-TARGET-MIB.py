# SNMP MIB module (CISCO-CBP-TARGET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CBP-TARGET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:05 2024
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

(CcbptPolicyIdentifier,
 CcbptPolicyIdentifierOrZero,
 CcbptPolicySourceType,
 CcbptTargetDirection,
 CcbptTargetId,
 CcbptTargetType) = mibBuilder.importSymbols(
    "CISCO-CBP-TARGET-TC-MIB",
    "CcbptPolicyIdentifier",
    "CcbptPolicyIdentifierOrZero",
    "CcbptPolicySourceType",
    "CcbptTargetDirection",
    "CcbptTargetId",
    "CcbptTargetType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoCbpTargetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533)
)
ciscoCbpTargetMIB.setRevisions(
        ("2006-05-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCbpTargetMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCbpTargetMIBNotifs = _CiscoCbpTargetMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 0)
)
_CiscoCbpTargetMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCbpTargetMIBObjects = _CiscoCbpTargetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1)
)
_CcbptTargetAttachCfg_ObjectIdentity = ObjectIdentity
ccbptTargetAttachCfg = _CcbptTargetAttachCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1)
)
_CcbptPolicyIdNext_Type = CcbptPolicyIdentifierOrZero
_CcbptPolicyIdNext_Object = MibScalar
ccbptPolicyIdNext = _CcbptPolicyIdNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 1),
    _CcbptPolicyIdNext_Type()
)
ccbptPolicyIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccbptPolicyIdNext.setStatus("current")
_CcbptTargetTable_Object = MibTable
ccbptTargetTable = _CcbptTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ccbptTargetTable.setStatus("current")
_CcbptTargetEntry_Object = MibTableRow
ccbptTargetEntry = _CcbptTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1)
)
ccbptTargetEntry.setIndexNames(
    (0, "CISCO-CBP-TARGET-MIB", "ccbptTargetType"),
    (0, "CISCO-CBP-TARGET-MIB", "ccbptTargetId"),
    (0, "CISCO-CBP-TARGET-MIB", "ccbptTargetDir"),
    (0, "CISCO-CBP-TARGET-MIB", "ccbptPolicySourceType"),
    (0, "CISCO-CBP-TARGET-MIB", "ccbptPolicyId"),
)
if mibBuilder.loadTexts:
    ccbptTargetEntry.setStatus("current")
_CcbptTargetType_Type = CcbptTargetType
_CcbptTargetType_Object = MibTableColumn
ccbptTargetType = _CcbptTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 1),
    _CcbptTargetType_Type()
)
ccbptTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccbptTargetType.setStatus("current")
_CcbptTargetId_Type = CcbptTargetId
_CcbptTargetId_Object = MibTableColumn
ccbptTargetId = _CcbptTargetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 2),
    _CcbptTargetId_Type()
)
ccbptTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccbptTargetId.setStatus("current")
_CcbptTargetDir_Type = CcbptTargetDirection
_CcbptTargetDir_Object = MibTableColumn
ccbptTargetDir = _CcbptTargetDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 3),
    _CcbptTargetDir_Type()
)
ccbptTargetDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccbptTargetDir.setStatus("current")
_CcbptPolicySourceType_Type = CcbptPolicySourceType
_CcbptPolicySourceType_Object = MibTableColumn
ccbptPolicySourceType = _CcbptPolicySourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 4),
    _CcbptPolicySourceType_Type()
)
ccbptPolicySourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccbptPolicySourceType.setStatus("current")
_CcbptPolicyId_Type = CcbptPolicyIdentifier
_CcbptPolicyId_Object = MibTableColumn
ccbptPolicyId = _CcbptPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 5),
    _CcbptPolicyId_Type()
)
ccbptPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccbptPolicyId.setStatus("current")
_CcbptTargetStatus_Type = RowStatus
_CcbptTargetStatus_Object = MibTableColumn
ccbptTargetStatus = _CcbptTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 6),
    _CcbptTargetStatus_Type()
)
ccbptTargetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccbptTargetStatus.setStatus("current")
_CcbptTargetStorageType_Type = StorageType
_CcbptTargetStorageType_Object = MibTableColumn
ccbptTargetStorageType = _CcbptTargetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 7),
    _CcbptTargetStorageType_Type()
)
ccbptTargetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccbptTargetStorageType.setStatus("current")
_CcbptPolicyMap_Type = RowPointer
_CcbptPolicyMap_Object = MibTableColumn
ccbptPolicyMap = _CcbptPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 8),
    _CcbptPolicyMap_Type()
)
ccbptPolicyMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccbptPolicyMap.setStatus("current")
_CcbptPolicyInstance_Type = RowPointer
_CcbptPolicyInstance_Object = MibTableColumn
ccbptPolicyInstance = _CcbptPolicyInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 9),
    _CcbptPolicyInstance_Type()
)
ccbptPolicyInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccbptPolicyInstance.setStatus("current")
_CcbptPolicyAttachTime_Type = TimeStamp
_CcbptPolicyAttachTime_Object = MibTableColumn
ccbptPolicyAttachTime = _CcbptPolicyAttachTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 2, 1, 10),
    _CcbptPolicyAttachTime_Type()
)
ccbptPolicyAttachTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccbptPolicyAttachTime.setStatus("current")
_CcbptTargetTableLastChange_Type = TimeStamp
_CcbptTargetTableLastChange_Object = MibScalar
ccbptTargetTableLastChange = _CcbptTargetTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 1, 1, 3),
    _CcbptTargetTableLastChange_Type()
)
ccbptTargetTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccbptTargetTableLastChange.setStatus("current")
_CiscoCbpTargetMIBConform_ObjectIdentity = ObjectIdentity
ciscoCbpTargetMIBConform = _CiscoCbpTargetMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2)
)
_CiscoCbpTargetMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCbpTargetMIBCompliances = _CiscoCbpTargetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2, 1)
)
_CiscoCbpTargetMIBMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCbpTargetMIBMIBGroups = _CiscoCbpTargetMIBMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2, 2)
)

# Managed Objects groups

ccbptTargetProvisioningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2, 2, 1)
)
ccbptTargetProvisioningGroup.setObjects(
      *(("CISCO-CBP-TARGET-MIB", "ccbptPolicyIdNext"),
        ("CISCO-CBP-TARGET-MIB", "ccbptTargetStatus"),
        ("CISCO-CBP-TARGET-MIB", "ccbptTargetStorageType"),
        ("CISCO-CBP-TARGET-MIB", "ccbptPolicyMap"),
        ("CISCO-CBP-TARGET-MIB", "ccbptPolicyInstance"))
)
if mibBuilder.loadTexts:
    ccbptTargetProvisioningGroup.setStatus("current")

ccbptTargetTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2, 2, 2)
)
ccbptTargetTimeGroup.setObjects(
      *(("CISCO-CBP-TARGET-MIB", "ccbptTargetTableLastChange"),
        ("CISCO-CBP-TARGET-MIB", "ccbptPolicyAttachTime"))
)
if mibBuilder.loadTexts:
    ccbptTargetTimeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCbpTargetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 533, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCbpTargetMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CBP-TARGET-MIB",
    **{"ciscoCbpTargetMIB": ciscoCbpTargetMIB,
       "ciscoCbpTargetMIBNotifs": ciscoCbpTargetMIBNotifs,
       "ciscoCbpTargetMIBObjects": ciscoCbpTargetMIBObjects,
       "ccbptTargetAttachCfg": ccbptTargetAttachCfg,
       "ccbptPolicyIdNext": ccbptPolicyIdNext,
       "ccbptTargetTable": ccbptTargetTable,
       "ccbptTargetEntry": ccbptTargetEntry,
       "ccbptTargetType": ccbptTargetType,
       "ccbptTargetId": ccbptTargetId,
       "ccbptTargetDir": ccbptTargetDir,
       "ccbptPolicySourceType": ccbptPolicySourceType,
       "ccbptPolicyId": ccbptPolicyId,
       "ccbptTargetStatus": ccbptTargetStatus,
       "ccbptTargetStorageType": ccbptTargetStorageType,
       "ccbptPolicyMap": ccbptPolicyMap,
       "ccbptPolicyInstance": ccbptPolicyInstance,
       "ccbptPolicyAttachTime": ccbptPolicyAttachTime,
       "ccbptTargetTableLastChange": ccbptTargetTableLastChange,
       "ciscoCbpTargetMIBConform": ciscoCbpTargetMIBConform,
       "ciscoCbpTargetMIBCompliances": ciscoCbpTargetMIBCompliances,
       "ciscoCbpTargetMIBCompliance": ciscoCbpTargetMIBCompliance,
       "ciscoCbpTargetMIBMIBGroups": ciscoCbpTargetMIBMIBGroups,
       "ccbptTargetProvisioningGroup": ccbptTargetProvisioningGroup,
       "ccbptTargetTimeGroup": ccbptTargetTimeGroup}
)
