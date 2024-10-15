# SNMP MIB module (ADTRAN-AOSFILESYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOSFILESYSTEM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:18 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSFileSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 6)
)
adGenAOSFileSystemMib.setRevisions(
        ("2005-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSFileSystem_ObjectIdentity = ObjectIdentity
adGenAOSFileSystem = _AdGenAOSFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6)
)
_AdAOSFileSystemRecordTable_Object = MibTable
adAOSFileSystemRecordTable = _AdAOSFileSystemRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1)
)
if mibBuilder.loadTexts:
    adAOSFileSystemRecordTable.setStatus("current")
_AdAOSFileSystemRecordEntry_Object = MibTableRow
adAOSFileSystemRecordEntry = _AdAOSFileSystemRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1)
)
adAOSFileSystemRecordEntry.setIndexNames(
    (0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"),
)
if mibBuilder.loadTexts:
    adAOSFileSystemRecordEntry.setStatus("current")
_AdAOSFileSystemRecordID_Type = Unsigned32
_AdAOSFileSystemRecordID_Object = MibTableColumn
adAOSFileSystemRecordID = _AdAOSFileSystemRecordID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 1),
    _AdAOSFileSystemRecordID_Type()
)
adAOSFileSystemRecordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordID.setStatus("current")
_AdAOSFileSystemRecordSystem_Type = DisplayString
_AdAOSFileSystemRecordSystem_Object = MibTableColumn
adAOSFileSystemRecordSystem = _AdAOSFileSystemRecordSystem_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 2),
    _AdAOSFileSystemRecordSystem_Type()
)
adAOSFileSystemRecordSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordSystem.setStatus("current")


class _AdAOSFileSystemRecordType_Type(Integer32):
    """Custom type adAOSFileSystemRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directory", 2),
          ("file", 1))
    )


_AdAOSFileSystemRecordType_Type.__name__ = "Integer32"
_AdAOSFileSystemRecordType_Object = MibTableColumn
adAOSFileSystemRecordType = _AdAOSFileSystemRecordType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 3),
    _AdAOSFileSystemRecordType_Type()
)
adAOSFileSystemRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordType.setStatus("current")
_AdAOSFileSystemRecordPath_Type = DisplayString
_AdAOSFileSystemRecordPath_Object = MibTableColumn
adAOSFileSystemRecordPath = _AdAOSFileSystemRecordPath_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 4),
    _AdAOSFileSystemRecordPath_Type()
)
adAOSFileSystemRecordPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordPath.setStatus("current")
_AdAOSFileSystemRecordName_Type = DisplayString
_AdAOSFileSystemRecordName_Object = MibTableColumn
adAOSFileSystemRecordName = _AdAOSFileSystemRecordName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 5),
    _AdAOSFileSystemRecordName_Type()
)
adAOSFileSystemRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordName.setStatus("current")
_AdAOSFileSystemRecordSize_Type = Unsigned32
_AdAOSFileSystemRecordSize_Object = MibTableColumn
adAOSFileSystemRecordSize = _AdAOSFileSystemRecordSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 6),
    _AdAOSFileSystemRecordSize_Type()
)
adAOSFileSystemRecordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordSize.setStatus("current")
_AdAOSFileSystemRecordStatus_Type = RowStatus
_AdAOSFileSystemRecordStatus_Object = MibTableColumn
adAOSFileSystemRecordStatus = _AdAOSFileSystemRecordStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 7),
    _AdAOSFileSystemRecordStatus_Type()
)
adAOSFileSystemRecordStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSFileSystemRecordStatus.setStatus("current")
_AdAOSFileSystemTable_Object = MibTable
adAOSFileSystemTable = _AdAOSFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adAOSFileSystemTable.setStatus("current")
_AdAOSFileSystemEntry_Object = MibTableRow
adAOSFileSystemEntry = _AdAOSFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1)
)
adAOSFileSystemEntry.setIndexNames(
    (0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"),
)
if mibBuilder.loadTexts:
    adAOSFileSystemEntry.setStatus("current")
_AdAOSFileSystemID_Type = Unsigned32
_AdAOSFileSystemID_Object = MibTableColumn
adAOSFileSystemID = _AdAOSFileSystemID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 1),
    _AdAOSFileSystemID_Type()
)
adAOSFileSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemID.setStatus("current")
_AdAOSFileSystemType_Type = DisplayString
_AdAOSFileSystemType_Object = MibTableColumn
adAOSFileSystemType = _AdAOSFileSystemType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 2),
    _AdAOSFileSystemType_Type()
)
adAOSFileSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemType.setStatus("current")
_AdAOSFileSystemTotalSize_Type = Unsigned32
_AdAOSFileSystemTotalSize_Object = MibTableColumn
adAOSFileSystemTotalSize = _AdAOSFileSystemTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 3),
    _AdAOSFileSystemTotalSize_Type()
)
adAOSFileSystemTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemTotalSize.setStatus("current")
_AdAOSFileSystemFreeSize_Type = Unsigned32
_AdAOSFileSystemFreeSize_Object = MibTableColumn
adAOSFileSystemFreeSize = _AdAOSFileSystemFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 4),
    _AdAOSFileSystemFreeSize_Type()
)
adAOSFileSystemFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSFileSystemFreeSize.setStatus("current")
_AdGenAOSFileSystemConformance_ObjectIdentity = ObjectIdentity
adGenAOSFileSystemConformance = _AdGenAOSFileSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5)
)
_AdAOSFileSystemCompliances_ObjectIdentity = ObjectIdentity
adAOSFileSystemCompliances = _AdAOSFileSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1)
)
_AdAOSFileSystemRecordGroups_ObjectIdentity = ObjectIdentity
adAOSFileSystemRecordGroups = _AdAOSFileSystemRecordGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2)
)
_AdAOSFileSystemGroups_ObjectIdentity = ObjectIdentity
adAOSFileSystemGroups = _AdAOSFileSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3)
)

# Managed Objects groups

adGenAOSFileSystemRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2, 1)
)
adGenAOSFileSystemRecordGroup.setObjects(
      *(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSystem"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordType"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordPath"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordName"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSize"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordStatus"))
)
if mibBuilder.loadTexts:
    adGenAOSFileSystemRecordGroup.setStatus("current")

adGenAOSFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3, 1)
)
adGenAOSFileSystemGroup.setObjects(
      *(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemType"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemTotalSize"),
        ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemFreeSize"))
)
if mibBuilder.loadTexts:
    adGenAOSFileSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adAOSFileSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSFileSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOSFILESYSTEM",
    **{"adGenAOSFileSystem": adGenAOSFileSystem,
       "adAOSFileSystemRecordTable": adAOSFileSystemRecordTable,
       "adAOSFileSystemRecordEntry": adAOSFileSystemRecordEntry,
       "adAOSFileSystemRecordID": adAOSFileSystemRecordID,
       "adAOSFileSystemRecordSystem": adAOSFileSystemRecordSystem,
       "adAOSFileSystemRecordType": adAOSFileSystemRecordType,
       "adAOSFileSystemRecordPath": adAOSFileSystemRecordPath,
       "adAOSFileSystemRecordName": adAOSFileSystemRecordName,
       "adAOSFileSystemRecordSize": adAOSFileSystemRecordSize,
       "adAOSFileSystemRecordStatus": adAOSFileSystemRecordStatus,
       "adAOSFileSystemTable": adAOSFileSystemTable,
       "adAOSFileSystemEntry": adAOSFileSystemEntry,
       "adAOSFileSystemID": adAOSFileSystemID,
       "adAOSFileSystemType": adAOSFileSystemType,
       "adAOSFileSystemTotalSize": adAOSFileSystemTotalSize,
       "adAOSFileSystemFreeSize": adAOSFileSystemFreeSize,
       "adGenAOSFileSystemConformance": adGenAOSFileSystemConformance,
       "adAOSFileSystemCompliances": adAOSFileSystemCompliances,
       "adAOSFileSystemCompliance": adAOSFileSystemCompliance,
       "adAOSFileSystemRecordGroups": adAOSFileSystemRecordGroups,
       "adGenAOSFileSystemRecordGroup": adGenAOSFileSystemRecordGroup,
       "adAOSFileSystemGroups": adAOSFileSystemGroups,
       "adGenAOSFileSystemGroup": adGenAOSFileSystemGroup,
       "adGenAOSFileSystemMib": adGenAOSFileSystemMib}
)
