# SNMP MIB module (FSCAN-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSCAN-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:29 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

filescan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24)
)
filescan.setRevisions(
        ("1999-08-03 10:20",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_FsFileStaticInfo_ObjectIdentity = ObjectIdentity
fsFileStaticInfo = _FsFileStaticInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 1)
)
_FsFileName_Type = DisplayString
_FsFileName_Object = MibScalar
fsFileName = _FsFileName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 1, 1),
    _FsFileName_Type()
)
fsFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileName.setStatus("current")
_FsFileScanMode_Type = DisplayString
_FsFileScanMode_Object = MibScalar
fsFileScanMode = _FsFileScanMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 1, 2),
    _FsFileScanMode_Type()
)
fsFileScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileScanMode.setStatus("current")
_FsFileScanStartTime_Type = DisplayString
_FsFileScanStartTime_Object = MibScalar
fsFileScanStartTime = _FsFileScanStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 1, 3),
    _FsFileScanStartTime_Type()
)
fsFileScanStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileScanStartTime.setStatus("current")
_FsFileDynamicInfo_ObjectIdentity = ObjectIdentity
fsFileDynamicInfo = _FsFileDynamicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 2)
)
_FsFileModificationTime_Type = DisplayString
_FsFileModificationTime_Object = MibScalar
fsFileModificationTime = _FsFileModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 2, 1),
    _FsFileModificationTime_Type()
)
fsFileModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileModificationTime.setStatus("current")
_FsFileSize_Type = Integer32
_FsFileSize_Object = MibScalar
fsFileSize = _FsFileSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 2, 2),
    _FsFileSize_Type()
)
fsFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileSize.setStatus("current")
if mibBuilder.loadTexts:
    fsFileSize.setUnits("bytes")
_FsFileLength_Type = Integer32
_FsFileLength_Object = MibScalar
fsFileLength = _FsFileLength_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 2, 3),
    _FsFileLength_Type()
)
fsFileLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileLength.setStatus("current")
if mibBuilder.loadTexts:
    fsFileLength.setUnits("lines")
_FsFileLengthRate_Type = DisplayString
_FsFileLengthRate_Object = MibScalar
fsFileLengthRate = _FsFileLengthRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 2, 4),
    _FsFileLengthRate_Type()
)
fsFileLengthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileLengthRate.setStatus("current")
if mibBuilder.loadTexts:
    fsFileLengthRate.setUnits("lines/sec")
_FsFileScanTable_Object = MibTable
fsFileScanTable = _FsFileScanTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    fsFileScanTable.setStatus("current")
_FsFileScanEntry_Object = MibTableRow
fsFileScanEntry = _FsFileScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1)
)
fsFileScanEntry.setIndexNames(
    (0, "FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanEntryName"),
)
if mibBuilder.loadTexts:
    fsFileScanEntry.setStatus("current")
_FsFileScanRowStatus_Type = RowStatus
_FsFileScanRowStatus_Object = MibTableColumn
fsFileScanRowStatus = _FsFileScanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 1),
    _FsFileScanRowStatus_Type()
)
fsFileScanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileScanRowStatus.setStatus("current")
_FsFileScanEntryName_Type = DisplayString
_FsFileScanEntryName_Object = MibTableColumn
fsFileScanEntryName = _FsFileScanEntryName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 2),
    _FsFileScanEntryName_Type()
)
fsFileScanEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileScanEntryName.setStatus("current")
_FsFileScanEntryDesc_Type = DisplayString
_FsFileScanEntryDesc_Object = MibTableColumn
fsFileScanEntryDesc = _FsFileScanEntryDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 3),
    _FsFileScanEntryDesc_Type()
)
fsFileScanEntryDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileScanEntryDesc.setStatus("current")
_FsFileScanPattern_Type = DisplayString
_FsFileScanPattern_Object = MibTableColumn
fsFileScanPattern = _FsFileScanPattern_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 4),
    _FsFileScanPattern_Type()
)
fsFileScanPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileScanPattern.setStatus("current")
_FsFileScanState_Type = DisplayString
_FsFileScanState_Object = MibTableColumn
fsFileScanState = _FsFileScanState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 5),
    _FsFileScanState_Type()
)
fsFileScanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileScanState.setStatus("current")
_FsFileScanNumberOfMatches_Type = Integer32
_FsFileScanNumberOfMatches_Object = MibTableColumn
fsFileScanNumberOfMatches = _FsFileScanNumberOfMatches_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1, 3, 1, 6),
    _FsFileScanNumberOfMatches_Type()
)
fsFileScanNumberOfMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileScanNumberOfMatches.setStatus("current")

# Managed Objects groups

fsFileScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24, 1)
)
fsFileScanGroup.setObjects(
      *(("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileName"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanMode"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanStartTime"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileModificationTime"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileSize"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileLength"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileLengthRate"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanRowStatus"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanEntryName"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanEntryDesc"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanPattern"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanState"),
        ("FSCAN-SUNMANAGEMENTCENTER-MIB", "fsFileScanNumberOfMatches"))
)
if mibBuilder.loadTexts:
    fsFileScanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSCAN-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "filescan": filescan,
       "fsFileScanGroup": fsFileScanGroup,
       "fsFileStaticInfo": fsFileStaticInfo,
       "fsFileName": fsFileName,
       "fsFileScanMode": fsFileScanMode,
       "fsFileScanStartTime": fsFileScanStartTime,
       "fsFileDynamicInfo": fsFileDynamicInfo,
       "fsFileModificationTime": fsFileModificationTime,
       "fsFileSize": fsFileSize,
       "fsFileLength": fsFileLength,
       "fsFileLengthRate": fsFileLengthRate,
       "fsFileScanTable": fsFileScanTable,
       "fsFileScanEntry": fsFileScanEntry,
       "fsFileScanRowStatus": fsFileScanRowStatus,
       "fsFileScanEntryName": fsFileScanEntryName,
       "fsFileScanEntryDesc": fsFileScanEntryDesc,
       "fsFileScanPattern": fsFileScanPattern,
       "fsFileScanState": fsFileScanState,
       "fsFileScanNumberOfMatches": fsFileScanNumberOfMatches}
)
