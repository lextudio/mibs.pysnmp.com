# SNMP MIB module (FORCE10-SYSTEM-COMPONENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORCE10-SYSTEM-COMPONENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:26 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(F10CamPartitionType,) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10CamPartitionType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

f10SysComponentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10SysComponentObjects_ObjectIdentity = ObjectIdentity
f10SysComponentObjects = _F10SysComponentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1)
)
_F10CamEntries_ObjectIdentity = ObjectIdentity
f10CamEntries = _F10CamEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1)
)
_CamUsageTable_Object = MibTable
camUsageTable = _CamUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    camUsageTable.setStatus("current")
_CamUsageEntry_Object = MibTableRow
camUsageEntry = _CamUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1)
)
camUsageEntry.setIndexNames(
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageSlot"),
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsagePipeNum"),
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsagePartId"),
)
if mibBuilder.loadTexts:
    camUsageEntry.setStatus("current")
_CamUsageSlot_Type = Integer32
_CamUsageSlot_Object = MibTableColumn
camUsageSlot = _CamUsageSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 1),
    _CamUsageSlot_Type()
)
camUsageSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageSlot.setStatus("current")
_CamUsagePipeNum_Type = Integer32
_CamUsagePipeNum_Object = MibTableColumn
camUsagePipeNum = _CamUsagePipeNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 2),
    _CamUsagePipeNum_Type()
)
camUsagePipeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsagePipeNum.setStatus("current")
_CamUsagePartId_Type = F10CamPartitionType
_CamUsagePartId_Object = MibTableColumn
camUsagePartId = _CamUsagePartId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 3),
    _CamUsagePartId_Type()
)
camUsagePartId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsagePartId.setStatus("current")
_CamUsagePartDesc_Type = DisplayString
_CamUsagePartDesc_Object = MibTableColumn
camUsagePartDesc = _CamUsagePartDesc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 4),
    _CamUsagePartDesc_Type()
)
camUsagePartDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsagePartDesc.setStatus("current")
_CamUsageTotal_Type = Integer32
_CamUsageTotal_Object = MibTableColumn
camUsageTotal = _CamUsageTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 5),
    _CamUsageTotal_Type()
)
camUsageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageTotal.setStatus("current")
_CamUsageUsed_Type = Integer32
_CamUsageUsed_Object = MibTableColumn
camUsageUsed = _CamUsageUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 1, 1, 6),
    _CamUsageUsed_Type()
)
camUsageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageUsed.setStatus("current")
_CamUsageL2Table_Object = MibTable
camUsageL2Table = _CamUsageL2Table_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    camUsageL2Table.setStatus("current")
_CamUsageL2Entry_Object = MibTableRow
camUsageL2Entry = _CamUsageL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1)
)
camUsageL2Entry.setIndexNames(
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL2Slot"),
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL2PipeId"),
)
if mibBuilder.loadTexts:
    camUsageL2Entry.setStatus("current")
_CamUsageL2Slot_Type = Integer32
_CamUsageL2Slot_Object = MibTableColumn
camUsageL2Slot = _CamUsageL2Slot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 1),
    _CamUsageL2Slot_Type()
)
camUsageL2Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL2Slot.setStatus("current")
_CamUsageL2PipeId_Type = Integer32
_CamUsageL2PipeId_Object = MibTableColumn
camUsageL2PipeId = _CamUsageL2PipeId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 2),
    _CamUsageL2PipeId_Type()
)
camUsageL2PipeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL2PipeId.setStatus("current")
_CamUsageL2IngAclTotal_Type = Integer32
_CamUsageL2IngAclTotal_Object = MibTableColumn
camUsageL2IngAclTotal = _CamUsageL2IngAclTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 3),
    _CamUsageL2IngAclTotal_Type()
)
camUsageL2IngAclTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2IngAclTotal.setStatus("current")
_CamUsageL2IngAclUsed_Type = Integer32
_CamUsageL2IngAclUsed_Object = MibTableColumn
camUsageL2IngAclUsed = _CamUsageL2IngAclUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 4),
    _CamUsageL2IngAclUsed_Type()
)
camUsageL2IngAclUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2IngAclUsed.setStatus("current")
_CamUsageL2IngFibTotal_Type = Integer32
_CamUsageL2IngFibTotal_Object = MibTableColumn
camUsageL2IngFibTotal = _CamUsageL2IngFibTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 7),
    _CamUsageL2IngFibTotal_Type()
)
camUsageL2IngFibTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2IngFibTotal.setStatus("current")
_CamUsageL2IngFibUsed_Type = Integer32
_CamUsageL2IngFibUsed_Object = MibTableColumn
camUsageL2IngFibUsed = _CamUsageL2IngFibUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 8),
    _CamUsageL2IngFibUsed_Type()
)
camUsageL2IngFibUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2IngFibUsed.setStatus("current")
_CamUsageL2EgrAclTotal_Type = Integer32
_CamUsageL2EgrAclTotal_Object = MibTableColumn
camUsageL2EgrAclTotal = _CamUsageL2EgrAclTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 9),
    _CamUsageL2EgrAclTotal_Type()
)
camUsageL2EgrAclTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2EgrAclTotal.setStatus("current")
_CamUsageL2EgrAclUsed_Type = Integer32
_CamUsageL2EgrAclUsed_Object = MibTableColumn
camUsageL2EgrAclUsed = _CamUsageL2EgrAclUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 2, 1, 10),
    _CamUsageL2EgrAclUsed_Type()
)
camUsageL2EgrAclUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL2EgrAclUsed.setStatus("current")
_CamUsageL3Table_Object = MibTable
camUsageL3Table = _CamUsageL3Table_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    camUsageL3Table.setStatus("current")
_CamUsageL3Entry_Object = MibTableRow
camUsageL3Entry = _CamUsageL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1)
)
camUsageL3Entry.setIndexNames(
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL3Slot"),
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL3PipeId"),
)
if mibBuilder.loadTexts:
    camUsageL3Entry.setStatus("current")
_CamUsageL3Slot_Type = Integer32
_CamUsageL3Slot_Object = MibTableColumn
camUsageL3Slot = _CamUsageL3Slot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 1),
    _CamUsageL3Slot_Type()
)
camUsageL3Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL3Slot.setStatus("current")
_CamUsageL3PipeId_Type = Integer32
_CamUsageL3PipeId_Object = MibTableColumn
camUsageL3PipeId = _CamUsageL3PipeId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 2),
    _CamUsageL3PipeId_Type()
)
camUsageL3PipeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL3PipeId.setStatus("current")
_CamUsageL3IngFibTotal_Type = Integer32
_CamUsageL3IngFibTotal_Object = MibTableColumn
camUsageL3IngFibTotal = _CamUsageL3IngFibTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 3),
    _CamUsageL3IngFibTotal_Type()
)
camUsageL3IngFibTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngFibTotal.setStatus("current")
_CamUsageL3IngFibUsed_Type = Integer32
_CamUsageL3IngFibUsed_Object = MibTableColumn
camUsageL3IngFibUsed = _CamUsageL3IngFibUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 4),
    _CamUsageL3IngFibUsed_Type()
)
camUsageL3IngFibUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngFibUsed.setStatus("current")
_CamUsageL3IngSysFlowTotal_Type = Integer32
_CamUsageL3IngSysFlowTotal_Object = MibTableColumn
camUsageL3IngSysFlowTotal = _CamUsageL3IngSysFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 5),
    _CamUsageL3IngSysFlowTotal_Type()
)
camUsageL3IngSysFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngSysFlowTotal.setStatus("current")
_CamUsageL3IngSysFlowUsed_Type = Integer32
_CamUsageL3IngSysFlowUsed_Object = MibTableColumn
camUsageL3IngSysFlowUsed = _CamUsageL3IngSysFlowUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 6),
    _CamUsageL3IngSysFlowUsed_Type()
)
camUsageL3IngSysFlowUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngSysFlowUsed.setStatus("current")
_CamUsageL3IngTrcListTotal_Type = Integer32
_CamUsageL3IngTrcListTotal_Object = MibTableColumn
camUsageL3IngTrcListTotal = _CamUsageL3IngTrcListTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 7),
    _CamUsageL3IngTrcListTotal_Type()
)
camUsageL3IngTrcListTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngTrcListTotal.setStatus("current")
_CamUsageL3IngTrcListUsed_Type = Integer32
_CamUsageL3IngTrcListUsed_Object = MibTableColumn
camUsageL3IngTrcListUsed = _CamUsageL3IngTrcListUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 8),
    _CamUsageL3IngTrcListUsed_Type()
)
camUsageL3IngTrcListUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngTrcListUsed.setStatus("current")
_CamUsageL3IngMcastFibTotal_Type = Integer32
_CamUsageL3IngMcastFibTotal_Object = MibTableColumn
camUsageL3IngMcastFibTotal = _CamUsageL3IngMcastFibTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 9),
    _CamUsageL3IngMcastFibTotal_Type()
)
camUsageL3IngMcastFibTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngMcastFibTotal.setStatus("current")
_CamUsageL3IngMcastFibUsed_Type = Integer32
_CamUsageL3IngMcastFibUsed_Object = MibTableColumn
camUsageL3IngMcastFibUsed = _CamUsageL3IngMcastFibUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 10),
    _CamUsageL3IngMcastFibUsed_Type()
)
camUsageL3IngMcastFibUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngMcastFibUsed.setStatus("current")
_CamUsageL3IngQosTotal_Type = Integer32
_CamUsageL3IngQosTotal_Object = MibTableColumn
camUsageL3IngQosTotal = _CamUsageL3IngQosTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 11),
    _CamUsageL3IngQosTotal_Type()
)
camUsageL3IngQosTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngQosTotal.setStatus("current")
_CamUsageL3IngQosUsed_Type = Integer32
_CamUsageL3IngQosUsed_Object = MibTableColumn
camUsageL3IngQosUsed = _CamUsageL3IngQosUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 12),
    _CamUsageL3IngQosUsed_Type()
)
camUsageL3IngQosUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngQosUsed.setStatus("current")
_CamUsageL3IngPbrTotal_Type = Integer32
_CamUsageL3IngPbrTotal_Object = MibTableColumn
camUsageL3IngPbrTotal = _CamUsageL3IngPbrTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 13),
    _CamUsageL3IngPbrTotal_Type()
)
camUsageL3IngPbrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngPbrTotal.setStatus("current")
_CamUsageL3IngPbrUsed_Type = Integer32
_CamUsageL3IngPbrUsed_Object = MibTableColumn
camUsageL3IngPbrUsed = _CamUsageL3IngPbrUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 14),
    _CamUsageL3IngPbrUsed_Type()
)
camUsageL3IngPbrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngPbrUsed.setStatus("current")
_CamUsageL3IngAclTotal_Type = Integer32
_CamUsageL3IngAclTotal_Object = MibTableColumn
camUsageL3IngAclTotal = _CamUsageL3IngAclTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 15),
    _CamUsageL3IngAclTotal_Type()
)
camUsageL3IngAclTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngAclTotal.setStatus("current")
_CamUsageL3IngAclUsed_Type = Integer32
_CamUsageL3IngAclUsed_Object = MibTableColumn
camUsageL3IngAclUsed = _CamUsageL3IngAclUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 16),
    _CamUsageL3IngAclUsed_Type()
)
camUsageL3IngAclUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3IngAclUsed.setStatus("current")
_CamUsageL3EgrAclTotal_Type = Integer32
_CamUsageL3EgrAclTotal_Object = MibTableColumn
camUsageL3EgrAclTotal = _CamUsageL3EgrAclTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 17),
    _CamUsageL3EgrAclTotal_Type()
)
camUsageL3EgrAclTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3EgrAclTotal.setStatus("current")
_CamUsageL3EgrAclUsed_Type = Integer32
_CamUsageL3EgrAclUsed_Object = MibTableColumn
camUsageL3EgrAclUsed = _CamUsageL3EgrAclUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 3, 1, 18),
    _CamUsageL3EgrAclUsed_Type()
)
camUsageL3EgrAclUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3EgrAclUsed.setStatus("current")
_CamUsageL3ExtTable_Object = MibTable
camUsageL3ExtTable = _CamUsageL3ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    camUsageL3ExtTable.setStatus("current")
_CamUsageL3ExtEntry_Object = MibTableRow
camUsageL3ExtEntry = _CamUsageL3ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1)
)
camUsageL3ExtEntry.setIndexNames(
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL3ExtSlot"),
    (0, "FORCE10-SYSTEM-COMPONENT-MIB", "camUsageL3ExtPipeId"),
)
if mibBuilder.loadTexts:
    camUsageL3ExtEntry.setStatus("current")
_CamUsageL3ExtSlot_Type = Integer32
_CamUsageL3ExtSlot_Object = MibTableColumn
camUsageL3ExtSlot = _CamUsageL3ExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 1),
    _CamUsageL3ExtSlot_Type()
)
camUsageL3ExtSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL3ExtSlot.setStatus("current")
_CamUsageL3ExtPipeId_Type = Integer32
_CamUsageL3ExtPipeId_Object = MibTableColumn
camUsageL3ExtPipeId = _CamUsageL3ExtPipeId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 2),
    _CamUsageL3ExtPipeId_Type()
)
camUsageL3ExtPipeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camUsageL3ExtPipeId.setStatus("current")
_CamUsageL3ExtHostTotal_Type = Integer32
_CamUsageL3ExtHostTotal_Object = MibTableColumn
camUsageL3ExtHostTotal = _CamUsageL3ExtHostTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 3),
    _CamUsageL3ExtHostTotal_Type()
)
camUsageL3ExtHostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3ExtHostTotal.setStatus("current")
_CamUsageL3ExtHostUsed_Type = Integer32
_CamUsageL3ExtHostUsed_Object = MibTableColumn
camUsageL3ExtHostUsed = _CamUsageL3ExtHostUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 4),
    _CamUsageL3ExtHostUsed_Type()
)
camUsageL3ExtHostUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3ExtHostUsed.setStatus("current")
_CamUsageL3ExtLPMTotal_Type = Integer32
_CamUsageL3ExtLPMTotal_Object = MibTableColumn
camUsageL3ExtLPMTotal = _CamUsageL3ExtLPMTotal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 5),
    _CamUsageL3ExtLPMTotal_Type()
)
camUsageL3ExtLPMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3ExtLPMTotal.setStatus("current")
_CamUsageL3ExtLPMUsed_Type = Integer32
_CamUsageL3ExtLPMUsed_Object = MibTableColumn
camUsageL3ExtLPMUsed = _CamUsageL3ExtLPMUsed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 1, 4, 1, 6),
    _CamUsageL3ExtLPMUsed_Type()
)
camUsageL3ExtLPMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camUsageL3ExtLPMUsed.setStatus("current")
_F10SysComponentTrap_ObjectIdentity = ObjectIdentity
f10SysComponentTrap = _F10SysComponentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2)
)
_SysCompAlarmMibNotifications_ObjectIdentity = ObjectIdentity
sysCompAlarmMibNotifications = _SysCompAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 0)
)
_SysCompAlarmVariable_ObjectIdentity = ObjectIdentity
sysCompAlarmVariable = _SysCompAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1)
)
_SysCompAlarmLevel_Type = Integer32
_SysCompAlarmLevel_Object = MibScalar
sysCompAlarmLevel = _SysCompAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1, 1),
    _SysCompAlarmLevel_Type()
)
sysCompAlarmLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysCompAlarmLevel.setStatus("current")
_SysCompAlarmVarString_Type = OctetString
_SysCompAlarmVarString_Object = MibScalar
sysCompAlarmVarString = _SysCompAlarmVarString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1, 2),
    _SysCompAlarmVarString_Type()
)
sysCompAlarmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysCompAlarmVarString.setStatus("current")
_SysCompSlotId_Type = Integer32
_SysCompSlotId_Object = MibScalar
sysCompSlotId = _SysCompSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1, 3),
    _SysCompSlotId_Type()
)
sysCompSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysCompSlotId.setStatus("current")
_SysCompPortPipe_Type = Integer32
_SysCompPortPipe_Object = MibScalar
sysCompPortPipe = _SysCompPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1, 4),
    _SysCompPortPipe_Type()
)
sysCompPortPipe.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysCompPortPipe.setStatus("current")
_SysCompCamPartId_Type = DisplayString
_SysCompCamPartId_Object = MibScalar
sysCompCamPartId = _SysCompCamPartId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 1, 5),
    _SysCompCamPartId_Type()
)
sysCompCamPartId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysCompCamPartId.setStatus("current")

# Managed Objects groups


# Notification objects

camUsageThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 0, 1)
)
camUsageThresholdExceed.setObjects(
      *(("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmLevel"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmVarString"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompSlotId"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompPortPipe"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompCamPartId"))
)
if mibBuilder.loadTexts:
    camUsageThresholdExceed.setStatus(
        "current"
    )

camIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 0, 2)
)
camIsFull.setObjects(
      *(("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmLevel"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmVarString"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompSlotId"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompPortPipe"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompCamPartId"))
)
if mibBuilder.loadTexts:
    camIsFull.setStatus(
        "current"
    )

camAuditError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 7, 1, 2, 0, 3)
)
camAuditError.setObjects(
      *(("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmLevel"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompAlarmVarString"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompSlotId"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompPortPipe"),
        ("FORCE10-SYSTEM-COMPONENT-MIB", "sysCompCamPartId"))
)
if mibBuilder.loadTexts:
    camAuditError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-SYSTEM-COMPONENT-MIB",
    **{"f10SysComponentMib": f10SysComponentMib,
       "f10SysComponentObjects": f10SysComponentObjects,
       "f10CamEntries": f10CamEntries,
       "camUsageTable": camUsageTable,
       "camUsageEntry": camUsageEntry,
       "camUsageSlot": camUsageSlot,
       "camUsagePipeNum": camUsagePipeNum,
       "camUsagePartId": camUsagePartId,
       "camUsagePartDesc": camUsagePartDesc,
       "camUsageTotal": camUsageTotal,
       "camUsageUsed": camUsageUsed,
       "camUsageL2Table": camUsageL2Table,
       "camUsageL2Entry": camUsageL2Entry,
       "camUsageL2Slot": camUsageL2Slot,
       "camUsageL2PipeId": camUsageL2PipeId,
       "camUsageL2IngAclTotal": camUsageL2IngAclTotal,
       "camUsageL2IngAclUsed": camUsageL2IngAclUsed,
       "camUsageL2IngFibTotal": camUsageL2IngFibTotal,
       "camUsageL2IngFibUsed": camUsageL2IngFibUsed,
       "camUsageL2EgrAclTotal": camUsageL2EgrAclTotal,
       "camUsageL2EgrAclUsed": camUsageL2EgrAclUsed,
       "camUsageL3Table": camUsageL3Table,
       "camUsageL3Entry": camUsageL3Entry,
       "camUsageL3Slot": camUsageL3Slot,
       "camUsageL3PipeId": camUsageL3PipeId,
       "camUsageL3IngFibTotal": camUsageL3IngFibTotal,
       "camUsageL3IngFibUsed": camUsageL3IngFibUsed,
       "camUsageL3IngSysFlowTotal": camUsageL3IngSysFlowTotal,
       "camUsageL3IngSysFlowUsed": camUsageL3IngSysFlowUsed,
       "camUsageL3IngTrcListTotal": camUsageL3IngTrcListTotal,
       "camUsageL3IngTrcListUsed": camUsageL3IngTrcListUsed,
       "camUsageL3IngMcastFibTotal": camUsageL3IngMcastFibTotal,
       "camUsageL3IngMcastFibUsed": camUsageL3IngMcastFibUsed,
       "camUsageL3IngQosTotal": camUsageL3IngQosTotal,
       "camUsageL3IngQosUsed": camUsageL3IngQosUsed,
       "camUsageL3IngPbrTotal": camUsageL3IngPbrTotal,
       "camUsageL3IngPbrUsed": camUsageL3IngPbrUsed,
       "camUsageL3IngAclTotal": camUsageL3IngAclTotal,
       "camUsageL3IngAclUsed": camUsageL3IngAclUsed,
       "camUsageL3EgrAclTotal": camUsageL3EgrAclTotal,
       "camUsageL3EgrAclUsed": camUsageL3EgrAclUsed,
       "camUsageL3ExtTable": camUsageL3ExtTable,
       "camUsageL3ExtEntry": camUsageL3ExtEntry,
       "camUsageL3ExtSlot": camUsageL3ExtSlot,
       "camUsageL3ExtPipeId": camUsageL3ExtPipeId,
       "camUsageL3ExtHostTotal": camUsageL3ExtHostTotal,
       "camUsageL3ExtHostUsed": camUsageL3ExtHostUsed,
       "camUsageL3ExtLPMTotal": camUsageL3ExtLPMTotal,
       "camUsageL3ExtLPMUsed": camUsageL3ExtLPMUsed,
       "f10SysComponentTrap": f10SysComponentTrap,
       "sysCompAlarmMibNotifications": sysCompAlarmMibNotifications,
       "camUsageThresholdExceed": camUsageThresholdExceed,
       "camIsFull": camIsFull,
       "camAuditError": camAuditError,
       "sysCompAlarmVariable": sysCompAlarmVariable,
       "sysCompAlarmLevel": sysCompAlarmLevel,
       "sysCompAlarmVarString": sysCompAlarmVarString,
       "sysCompSlotId": sysCompSlotId,
       "sysCompPortPipe": sysCompPortPipe,
       "sysCompCamPartId": sysCompCamPartId}
)
