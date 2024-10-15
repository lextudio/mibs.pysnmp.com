# SNMP MIB module (HUAWEI-MODULE-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MODULE-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:03 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwModuleInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwModuleInfoObjects_ObjectIdentity = ObjectIdentity
hwModuleInfoObjects = _HwModuleInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1)
)
_HwModuleInfoTable_Object = MibTable
hwModuleInfoTable = _HwModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1)
)
if mibBuilder.loadTexts:
    hwModuleInfoTable.setStatus("current")
_HwModuleInfoEntry_Object = MibTableRow
hwModuleInfoEntry = _HwModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1)
)
hwModuleInfoEntry.setIndexNames(
    (0, "HUAWEI-MODULE-INFO-MIB", "hwModuleIndex"),
    (0, "HUAWEI-MODULE-INFO-MIB", "hwSubModuleIndex"),
)
if mibBuilder.loadTexts:
    hwModuleInfoEntry.setStatus("current")
_HwModuleIndex_Type = Integer32
_HwModuleIndex_Object = MibTableColumn
hwModuleIndex = _HwModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 1),
    _HwModuleIndex_Type()
)
hwModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleIndex.setStatus("current")
_HwSubModuleIndex_Type = Integer32
_HwSubModuleIndex_Object = MibTableColumn
hwSubModuleIndex = _HwSubModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 2),
    _HwSubModuleIndex_Type()
)
hwSubModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubModuleIndex.setStatus("current")
_HwModuleBomId_Type = SnmpAdminString
_HwModuleBomId_Object = MibTableColumn
hwModuleBomId = _HwModuleBomId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 3),
    _HwModuleBomId_Type()
)
hwModuleBomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleBomId.setStatus("current")
_HwModuleBomEnDesc_Type = SnmpAdminString
_HwModuleBomEnDesc_Object = MibTableColumn
hwModuleBomEnDesc = _HwModuleBomEnDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 4),
    _HwModuleBomEnDesc_Type()
)
hwModuleBomEnDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleBomEnDesc.setStatus("current")
_HwModuleBomLocalDesc_Type = SnmpAdminString
_HwModuleBomLocalDesc_Object = MibTableColumn
hwModuleBomLocalDesc = _HwModuleBomLocalDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 5),
    _HwModuleBomLocalDesc_Type()
)
hwModuleBomLocalDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleBomLocalDesc.setStatus("current")
_HwModuleManufacturedDate_Type = DateAndTime
_HwModuleManufacturedDate_Object = MibTableColumn
hwModuleManufacturedDate = _HwModuleManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 6),
    _HwModuleManufacturedDate_Type()
)
hwModuleManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleManufacturedDate.setStatus("current")
_HwModuleManufactureCode_Type = Integer32
_HwModuleManufactureCode_Object = MibTableColumn
hwModuleManufactureCode = _HwModuleManufactureCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 7),
    _HwModuleManufactureCode_Type()
)
hwModuleManufactureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleManufactureCode.setStatus("current")
_HwModuleCLEICode_Type = SnmpAdminString
_HwModuleCLEICode_Object = MibTableColumn
hwModuleCLEICode = _HwModuleCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 8),
    _HwModuleCLEICode_Type()
)
hwModuleCLEICode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwModuleCLEICode.setStatus("current")
_HwModuleUpdateLog_Type = SnmpAdminString
_HwModuleUpdateLog_Object = MibTableColumn
hwModuleUpdateLog = _HwModuleUpdateLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 9),
    _HwModuleUpdateLog_Type()
)
hwModuleUpdateLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleUpdateLog.setStatus("current")
_HwModuleArchivesInfoVersion_Type = SnmpAdminString
_HwModuleArchivesInfoVersion_Object = MibTableColumn
hwModuleArchivesInfoVersion = _HwModuleArchivesInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 10),
    _HwModuleArchivesInfoVersion_Type()
)
hwModuleArchivesInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleArchivesInfoVersion.setStatus("current")
_HwModuleSerialNum_Type = SnmpAdminString
_HwModuleSerialNum_Object = MibTableColumn
hwModuleSerialNum = _HwModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 43, 1, 1, 1, 11),
    _HwModuleSerialNum_Type()
)
hwModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleSerialNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MODULE-INFO-MIB",
    **{"hwModuleInfo": hwModuleInfo,
       "hwModuleInfoObjects": hwModuleInfoObjects,
       "hwModuleInfoTable": hwModuleInfoTable,
       "hwModuleInfoEntry": hwModuleInfoEntry,
       "hwModuleIndex": hwModuleIndex,
       "hwSubModuleIndex": hwSubModuleIndex,
       "hwModuleBomId": hwModuleBomId,
       "hwModuleBomEnDesc": hwModuleBomEnDesc,
       "hwModuleBomLocalDesc": hwModuleBomLocalDesc,
       "hwModuleManufacturedDate": hwModuleManufacturedDate,
       "hwModuleManufactureCode": hwModuleManufactureCode,
       "hwModuleCLEICode": hwModuleCLEICode,
       "hwModuleUpdateLog": hwModuleUpdateLog,
       "hwModuleArchivesInfoVersion": hwModuleArchivesInfoVersion,
       "hwModuleSerialNum": hwModuleSerialNum}
)
