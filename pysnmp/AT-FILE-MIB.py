# SNMP MIB module (AT-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-FILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:08 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

file = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56)
)
file.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("current")
_FileEntry_Object = MibTableRow
fileEntry = _FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1)
)
fileEntry.setIndexNames(
    (0, "AT-FILE-MIB", "fileIndex"),
)
if mibBuilder.loadTexts:
    fileEntry.setStatus("current")
_FileIndex_Type = Integer32
_FileIndex_Object = MibTableColumn
fileIndex = _FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 1),
    _FileIndex_Type()
)
fileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileIndex.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("current")


class _FileDevice_Type(Integer32):
    """Custom type fileDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("nvs", 2))
    )


_FileDevice_Type.__name__ = "Integer32"
_FileDevice_Object = MibTableColumn
fileDevice = _FileDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 3),
    _FileDevice_Type()
)
fileDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileDevice.setStatus("current")
_FileCreationTime_Type = DisplayString
_FileCreationTime_Object = MibTableColumn
fileCreationTime = _FileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 4),
    _FileCreationTime_Type()
)
fileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCreationTime.setStatus("current")


class _FileStatus_Type(Integer32):
    """Custom type fileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("ok", 1))
    )


_FileStatus_Type.__name__ = "Integer32"
_FileStatus_Object = MibTableColumn
fileStatus = _FileStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 5),
    _FileStatus_Type()
)
fileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileStatus.setStatus("current")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 6),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("current")
_FileNumbers_Type = Integer32
_FileNumbers_Object = MibScalar
fileNumbers = _FileNumbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 2),
    _FileNumbers_Type()
)
fileNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileNumbers.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FILE-MIB",
    **{"file": file,
       "fileTable": fileTable,
       "fileEntry": fileEntry,
       "fileIndex": fileIndex,
       "fileName": fileName,
       "fileDevice": fileDevice,
       "fileCreationTime": fileCreationTime,
       "fileStatus": fileStatus,
       "fileSize": fileSize,
       "fileNumbers": fileNumbers}
)
