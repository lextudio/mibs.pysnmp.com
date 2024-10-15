# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:46 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonSecurity,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonSecurity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

lhnNusCommonSecurityModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SecUserCount_Type = Integer32
_SecUserCount_Object = MibScalar
secUserCount = _SecUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 1),
    _SecUserCount_Type()
)
secUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserCount.setStatus("current")
_SecUserTable_Object = MibTable
secUserTable = _SecUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    secUserTable.setStatus("current")
_SecUserEntry_Object = MibTableRow
secUserEntry = _SecUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1)
)
secUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secUserIndex"),
)
if mibBuilder.loadTexts:
    secUserEntry.setStatus("current")
_SecUserIndex_Type = Integer32
_SecUserIndex_Object = MibTableColumn
secUserIndex = _SecUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 1),
    _SecUserIndex_Type()
)
secUserIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secUserIndex.setStatus("current")
_SecUserName_Type = OctetString
_SecUserName_Object = MibTableColumn
secUserName = _SecUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 2),
    _SecUserName_Type()
)
secUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secUserName.setStatus("current")
_SecUserDesc_Type = OctetString
_SecUserDesc_Object = MibTableColumn
secUserDesc = _SecUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 3),
    _SecUserDesc_Type()
)
secUserDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserDesc.setStatus("current")
_SecUserPasswd_Type = OctetString
_SecUserPasswd_Object = MibTableColumn
secUserPasswd = _SecUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 4),
    _SecUserPasswd_Type()
)
secUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserPasswd.setStatus("current")
_SecUserRowStatus_Type = RowStatus
_SecUserRowStatus_Object = MibTableColumn
secUserRowStatus = _SecUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 5),
    _SecUserRowStatus_Type()
)
secUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secUserRowStatus.setStatus("current")
_SecGroupCount_Type = Integer32
_SecGroupCount_Object = MibScalar
secGroupCount = _SecGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 3),
    _SecGroupCount_Type()
)
secGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupCount.setStatus("current")
_SecGroupTable_Object = MibTable
secGroupTable = _SecGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    secGroupTable.setStatus("current")
_SecGroupEntry_Object = MibTableRow
secGroupEntry = _SecGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1)
)
secGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secGroupIndex"),
)
if mibBuilder.loadTexts:
    secGroupEntry.setStatus("current")
_SecGroupIndex_Type = Integer32
_SecGroupIndex_Object = MibTableColumn
secGroupIndex = _SecGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 1),
    _SecGroupIndex_Type()
)
secGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secGroupIndex.setStatus("current")
_SecGroupName_Type = OctetString
_SecGroupName_Object = MibTableColumn
secGroupName = _SecGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 2),
    _SecGroupName_Type()
)
secGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secGroupName.setStatus("current")
_SecGroupDesc_Type = OctetString
_SecGroupDesc_Object = MibTableColumn
secGroupDesc = _SecGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 3),
    _SecGroupDesc_Type()
)
secGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secGroupDesc.setStatus("current")
_SecGroupUserCount_Type = Integer32
_SecGroupUserCount_Object = MibTableColumn
secGroupUserCount = _SecGroupUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 4),
    _SecGroupUserCount_Type()
)
secGroupUserCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secGroupUserCount.setStatus("current")
_SecGroupRowStatus_Type = RowStatus
_SecGroupRowStatus_Object = MibTableColumn
secGroupRowStatus = _SecGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 5),
    _SecGroupRowStatus_Type()
)
secGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secGroupRowStatus.setStatus("current")
_SecGroupUserTable_Object = MibTable
secGroupUserTable = _SecGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    secGroupUserTable.setStatus("current")
_SecGroupUserEntry_Object = MibTableRow
secGroupUserEntry = _SecGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1)
)
secGroupUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secGroupUserIndex"),
)
if mibBuilder.loadTexts:
    secGroupUserEntry.setStatus("current")
_SecGroupUserIndex_Type = Integer32
_SecGroupUserIndex_Object = MibTableColumn
secGroupUserIndex = _SecGroupUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 1),
    _SecGroupUserIndex_Type()
)
secGroupUserIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secGroupUserIndex.setStatus("current")
_SecGroupUserName_Type = OctetString
_SecGroupUserName_Object = MibTableColumn
secGroupUserName = _SecGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 2),
    _SecGroupUserName_Type()
)
secGroupUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secGroupUserName.setStatus("current")
_SecGroupUserRowStatus_Type = RowStatus
_SecGroupUserRowStatus_Object = MibTableColumn
secGroupUserRowStatus = _SecGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 3),
    _SecGroupUserRowStatus_Type()
)
secGroupUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secGroupUserRowStatus.setStatus("current")
_SecAdminUserCount_Type = Integer32
_SecAdminUserCount_Object = MibScalar
secAdminUserCount = _SecAdminUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 6),
    _SecAdminUserCount_Type()
)
secAdminUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminUserCount.setStatus("current")
_SecAdminUserTable_Object = MibTable
secAdminUserTable = _SecAdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7)
)
if mibBuilder.loadTexts:
    secAdminUserTable.setStatus("current")
_SecAdminUserEntry_Object = MibTableRow
secAdminUserEntry = _SecAdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1)
)
secAdminUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminUserIndex"),
)
if mibBuilder.loadTexts:
    secAdminUserEntry.setStatus("current")
_SecAdminUserIndex_Type = Integer32
_SecAdminUserIndex_Object = MibTableColumn
secAdminUserIndex = _SecAdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 1),
    _SecAdminUserIndex_Type()
)
secAdminUserIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminUserIndex.setStatus("current")
_SecAdminUserName_Type = OctetString
_SecAdminUserName_Object = MibTableColumn
secAdminUserName = _SecAdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 2),
    _SecAdminUserName_Type()
)
secAdminUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminUserName.setStatus("current")
_SecAdminUserDesc_Type = OctetString
_SecAdminUserDesc_Object = MibTableColumn
secAdminUserDesc = _SecAdminUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 3),
    _SecAdminUserDesc_Type()
)
secAdminUserDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminUserDesc.setStatus("current")
_SecAdminUserPasswd_Type = OctetString
_SecAdminUserPasswd_Object = MibTableColumn
secAdminUserPasswd = _SecAdminUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 4),
    _SecAdminUserPasswd_Type()
)
secAdminUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminUserPasswd.setStatus("current")
_SecAdminUserRowStatus_Type = RowStatus
_SecAdminUserRowStatus_Object = MibTableColumn
secAdminUserRowStatus = _SecAdminUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 5),
    _SecAdminUserRowStatus_Type()
)
secAdminUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminUserRowStatus.setStatus("current")
_SecAdminGroupCount_Type = Integer32
_SecAdminGroupCount_Object = MibScalar
secAdminGroupCount = _SecAdminGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 8),
    _SecAdminGroupCount_Type()
)
secAdminGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupCount.setStatus("current")
_SecAdminGroupTable_Object = MibTable
secAdminGroupTable = _SecAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9)
)
if mibBuilder.loadTexts:
    secAdminGroupTable.setStatus("current")
_SecAdminGroupEntry_Object = MibTableRow
secAdminGroupEntry = _SecAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1)
)
secAdminGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminGroupIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupEntry.setStatus("current")
_SecAdminGroupIndex_Type = Integer32
_SecAdminGroupIndex_Object = MibTableColumn
secAdminGroupIndex = _SecAdminGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 1),
    _SecAdminGroupIndex_Type()
)
secAdminGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupIndex.setStatus("current")
_SecAdminGroupName_Type = OctetString
_SecAdminGroupName_Object = MibTableColumn
secAdminGroupName = _SecAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 2),
    _SecAdminGroupName_Type()
)
secAdminGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminGroupName.setStatus("current")
_SecAdminGroupDesc_Type = OctetString
_SecAdminGroupDesc_Object = MibTableColumn
secAdminGroupDesc = _SecAdminGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 3),
    _SecAdminGroupDesc_Type()
)
secAdminGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminGroupDesc.setStatus("current")
_SecAdminGroupUserOrSubGroupCount_Type = Integer32
_SecAdminGroupUserOrSubGroupCount_Object = MibTableColumn
secAdminGroupUserOrSubGroupCount = _SecAdminGroupUserOrSubGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 4),
    _SecAdminGroupUserOrSubGroupCount_Type()
)
secAdminGroupUserOrSubGroupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupCount.setStatus("current")
_SecAdminGroupRowStatus_Type = RowStatus
_SecAdminGroupRowStatus_Object = MibTableColumn
secAdminGroupRowStatus = _SecAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 5),
    _SecAdminGroupRowStatus_Type()
)
secAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupRowStatus.setStatus("current")
_SecAdminGroupUserOrSubGroupTable_Object = MibTable
secAdminGroupUserOrSubGroupTable = _SecAdminGroupUserOrSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10)
)
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupTable.setStatus("current")
_SecAdminGroupUserOrSubGroupEntry_Object = MibTableRow
secAdminGroupUserOrSubGroupEntry = _SecAdminGroupUserOrSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1)
)
secAdminGroupUserOrSubGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminGroupUserOrSubGroupIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupEntry.setStatus("current")
_SecAdminGroupUserOrSubGroupIndex_Type = Integer32
_SecAdminGroupUserOrSubGroupIndex_Object = MibTableColumn
secAdminGroupUserOrSubGroupIndex = _SecAdminGroupUserOrSubGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 1),
    _SecAdminGroupUserOrSubGroupIndex_Type()
)
secAdminGroupUserOrSubGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupIndex.setStatus("current")
_SecAdminGroupUserOrSubGroupName_Type = OctetString
_SecAdminGroupUserOrSubGroupName_Object = MibTableColumn
secAdminGroupUserOrSubGroupName = _SecAdminGroupUserOrSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 2),
    _SecAdminGroupUserOrSubGroupName_Type()
)
secAdminGroupUserOrSubGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupName.setStatus("current")
_SecAdminGroupUserOrSubGroupRowStatus_Type = RowStatus
_SecAdminGroupUserOrSubGroupRowStatus_Object = MibTableColumn
secAdminGroupUserOrSubGroupRowStatus = _SecAdminGroupUserOrSubGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 3),
    _SecAdminGroupUserOrSubGroupRowStatus_Type()
)
secAdminGroupUserOrSubGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupUserOrSubGroupRowStatus.setStatus("current")
_SecAdminGroupAccessTable_Object = MibTable
secAdminGroupAccessTable = _SecAdminGroupAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11)
)
if mibBuilder.loadTexts:
    secAdminGroupAccessTable.setStatus("current")
_SecAdminGroupAccessEntry_Object = MibTableRow
secAdminGroupAccessEntry = _SecAdminGroupAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1)
)
secAdminGroupAccessEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB", "secAdminGroupAccessIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupAccessEntry.setStatus("current")
_SecAdminGroupAccessIndex_Type = Integer32
_SecAdminGroupAccessIndex_Object = MibTableColumn
secAdminGroupAccessIndex = _SecAdminGroupAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 1),
    _SecAdminGroupAccessIndex_Type()
)
secAdminGroupAccessIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupAccessIndex.setStatus("current")
_SecAdminGroupAccessKey_Type = OctetString
_SecAdminGroupAccessKey_Object = MibTableColumn
secAdminGroupAccessKey = _SecAdminGroupAccessKey_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 2),
    _SecAdminGroupAccessKey_Type()
)
secAdminGroupAccessKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminGroupAccessKey.setStatus("current")


class _SecAdminGroupAccessMode_Type(Bits):
    """Custom type secAdminGroupAccessMode based on Bits"""
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("get", 0),
          ("set", 1))
    )

_SecAdminGroupAccessMode_Type.__name__ = "Bits"
_SecAdminGroupAccessMode_Object = MibTableColumn
secAdminGroupAccessMode = _SecAdminGroupAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 3),
    _SecAdminGroupAccessMode_Type()
)
secAdminGroupAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupAccessMode.setStatus("current")
_SecAdminGroupAccessRowStatus_Type = RowStatus
_SecAdminGroupAccessRowStatus_Object = MibTableColumn
secAdminGroupAccessRowStatus = _SecAdminGroupAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 4),
    _SecAdminGroupAccessRowStatus_Type()
)
secAdminGroupAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secAdminGroupAccessRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB",
    **{"lhnNusCommonSecurityModule": lhnNusCommonSecurityModule,
       "secUserCount": secUserCount,
       "secUserTable": secUserTable,
       "secUserEntry": secUserEntry,
       "secUserIndex": secUserIndex,
       "secUserName": secUserName,
       "secUserDesc": secUserDesc,
       "secUserPasswd": secUserPasswd,
       "secUserRowStatus": secUserRowStatus,
       "secGroupCount": secGroupCount,
       "secGroupTable": secGroupTable,
       "secGroupEntry": secGroupEntry,
       "secGroupIndex": secGroupIndex,
       "secGroupName": secGroupName,
       "secGroupDesc": secGroupDesc,
       "secGroupUserCount": secGroupUserCount,
       "secGroupRowStatus": secGroupRowStatus,
       "secGroupUserTable": secGroupUserTable,
       "secGroupUserEntry": secGroupUserEntry,
       "secGroupUserIndex": secGroupUserIndex,
       "secGroupUserName": secGroupUserName,
       "secGroupUserRowStatus": secGroupUserRowStatus,
       "secAdminUserCount": secAdminUserCount,
       "secAdminUserTable": secAdminUserTable,
       "secAdminUserEntry": secAdminUserEntry,
       "secAdminUserIndex": secAdminUserIndex,
       "secAdminUserName": secAdminUserName,
       "secAdminUserDesc": secAdminUserDesc,
       "secAdminUserPasswd": secAdminUserPasswd,
       "secAdminUserRowStatus": secAdminUserRowStatus,
       "secAdminGroupCount": secAdminGroupCount,
       "secAdminGroupTable": secAdminGroupTable,
       "secAdminGroupEntry": secAdminGroupEntry,
       "secAdminGroupIndex": secAdminGroupIndex,
       "secAdminGroupName": secAdminGroupName,
       "secAdminGroupDesc": secAdminGroupDesc,
       "secAdminGroupUserOrSubGroupCount": secAdminGroupUserOrSubGroupCount,
       "secAdminGroupRowStatus": secAdminGroupRowStatus,
       "secAdminGroupUserOrSubGroupTable": secAdminGroupUserOrSubGroupTable,
       "secAdminGroupUserOrSubGroupEntry": secAdminGroupUserOrSubGroupEntry,
       "secAdminGroupUserOrSubGroupIndex": secAdminGroupUserOrSubGroupIndex,
       "secAdminGroupUserOrSubGroupName": secAdminGroupUserOrSubGroupName,
       "secAdminGroupUserOrSubGroupRowStatus": secAdminGroupUserOrSubGroupRowStatus,
       "secAdminGroupAccessTable": secAdminGroupAccessTable,
       "secAdminGroupAccessEntry": secAdminGroupAccessEntry,
       "secAdminGroupAccessIndex": secAdminGroupAccessIndex,
       "secAdminGroupAccessKey": secAdminGroupAccessKey,
       "secAdminGroupAccessMode": secAdminGroupAccessMode,
       "secAdminGroupAccessRowStatus": secAdminGroupAccessRowStatus}
)
