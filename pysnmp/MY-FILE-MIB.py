# SNMP MIB module (MY-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-FILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:20 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

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

myFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11)
)
myFileMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyFileMIBObjects_ObjectIdentity = ObjectIdentity
myFileMIBObjects = _MyFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1)
)
_MyFileTransTable_Object = MibTable
myFileTransTable = _MyFileTransTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    myFileTransTable.setStatus("current")
_MyFileTransEntry_Object = MibTableRow
myFileTransEntry = _MyFileTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1)
)
myFileTransEntry.setIndexNames(
    (0, "MY-FILE-MIB", "myFileTransIndex"),
)
if mibBuilder.loadTexts:
    myFileTransEntry.setStatus("current")
_MyFileTransIndex_Type = Integer32
_MyFileTransIndex_Object = MibTableColumn
myFileTransIndex = _MyFileTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 1),
    _MyFileTransIndex_Type()
)
myFileTransIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileTransIndex.setStatus("current")


class _MyFileTransMeans_Type(Integer32):
    """Custom type myFileTransMeans based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("tftp", 1),
          ("xmodem", 2))
    )


_MyFileTransMeans_Type.__name__ = "Integer32"
_MyFileTransMeans_Object = MibTableColumn
myFileTransMeans = _MyFileTransMeans_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 2),
    _MyFileTransMeans_Type()
)
myFileTransMeans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myFileTransMeans.setStatus("current")


class _MyFileTransOperType_Type(Integer32):
    """Custom type myFileTransOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("synchronize", 3),
          ("upload", 1))
    )


_MyFileTransOperType_Type.__name__ = "Integer32"
_MyFileTransOperType_Object = MibTableColumn
myFileTransOperType = _MyFileTransOperType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 3),
    _MyFileTransOperType_Type()
)
myFileTransOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myFileTransOperType.setStatus("current")
_MyFileTransSrcFileName_Type = DisplayString
_MyFileTransSrcFileName_Object = MibTableColumn
myFileTransSrcFileName = _MyFileTransSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 4),
    _MyFileTransSrcFileName_Type()
)
myFileTransSrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myFileTransSrcFileName.setStatus("current")
_MyFileTransDescFileName_Type = DisplayString
_MyFileTransDescFileName_Object = MibTableColumn
myFileTransDescFileName = _MyFileTransDescFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 5),
    _MyFileTransDescFileName_Type()
)
myFileTransDescFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myFileTransDescFileName.setStatus("current")
_MyFileTransServerAddr_Type = IpAddress
_MyFileTransServerAddr_Object = MibTableColumn
myFileTransServerAddr = _MyFileTransServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 6),
    _MyFileTransServerAddr_Type()
)
myFileTransServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myFileTransServerAddr.setStatus("current")


class _MyFileTransResult_Type(Integer32):
    """Custom type myFileTransResult based on Integer32"""
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
        *(("failure", 2),
          ("parametersIllegel", 3),
          ("success", 1),
          ("timeout", 4))
    )


_MyFileTransResult_Type.__name__ = "Integer32"
_MyFileTransResult_Object = MibTableColumn
myFileTransResult = _MyFileTransResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 7),
    _MyFileTransResult_Type()
)
myFileTransResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileTransResult.setStatus("current")
_MyFileTransComplete_Type = TruthValue
_MyFileTransComplete_Object = MibTableColumn
myFileTransComplete = _MyFileTransComplete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 8),
    _MyFileTransComplete_Type()
)
myFileTransComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileTransComplete.setStatus("current")
_MyFileTransDataLength_Type = Gauge32
_MyFileTransDataLength_Object = MibTableColumn
myFileTransDataLength = _MyFileTransDataLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 9),
    _MyFileTransDataLength_Type()
)
myFileTransDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileTransDataLength.setStatus("current")
_MyFileTransEntryStatus_Type = RowStatus
_MyFileTransEntryStatus_Object = MibTableColumn
myFileTransEntryStatus = _MyFileTransEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 10),
    _MyFileTransEntryStatus_Type()
)
myFileTransEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myFileTransEntryStatus.setStatus("current")
_MyFileSystemMaxRoom_Type = Integer32
_MyFileSystemMaxRoom_Object = MibScalar
myFileSystemMaxRoom = _MyFileSystemMaxRoom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 2),
    _MyFileSystemMaxRoom_Type()
)
myFileSystemMaxRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileSystemMaxRoom.setStatus("current")
_MyFileSystemAvailableRoom_Type = Integer32
_MyFileSystemAvailableRoom_Object = MibScalar
myFileSystemAvailableRoom = _MyFileSystemAvailableRoom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 3),
    _MyFileSystemAvailableRoom_Type()
)
myFileSystemAvailableRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFileSystemAvailableRoom.setStatus("current")
_MyFileMIBConformance_ObjectIdentity = ObjectIdentity
myFileMIBConformance = _MyFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2)
)
_MyFileMIBCompliances_ObjectIdentity = ObjectIdentity
myFileMIBCompliances = _MyFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 1)
)
_MyFileMIBGroups_ObjectIdentity = ObjectIdentity
myFileMIBGroups = _MyFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2)
)

# Managed Objects groups

myFileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2, 1)
)
myFileMIBGroup.setObjects(
      *(("MY-FILE-MIB", "myFileTransIndex"),
        ("MY-FILE-MIB", "myFileTransOperType"),
        ("MY-FILE-MIB", "myFileTransSrcFileName"),
        ("MY-FILE-MIB", "myFileTransDescFileName"),
        ("MY-FILE-MIB", "myFileTransServerAddr"),
        ("MY-FILE-MIB", "myFileTransResult"),
        ("MY-FILE-MIB", "myFileTransComplete"),
        ("MY-FILE-MIB", "myFileTransDataLength"),
        ("MY-FILE-MIB", "myFileTransEntryStatus"),
        ("MY-FILE-MIB", "myFileSystemMaxRoom"),
        ("MY-FILE-MIB", "myFileSystemAvailableRoom"))
)
if mibBuilder.loadTexts:
    myFileMIBGroup.setStatus("current")

myFileTransMeansMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2, 2)
)
myFileTransMeansMIBGroup.setObjects(
    ("MY-FILE-MIB", "myFileTransMeans")
)
if mibBuilder.loadTexts:
    myFileTransMeansMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myFileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-FILE-MIB",
    **{"myFileMIB": myFileMIB,
       "myFileMIBObjects": myFileMIBObjects,
       "myFileTransTable": myFileTransTable,
       "myFileTransEntry": myFileTransEntry,
       "myFileTransIndex": myFileTransIndex,
       "myFileTransMeans": myFileTransMeans,
       "myFileTransOperType": myFileTransOperType,
       "myFileTransSrcFileName": myFileTransSrcFileName,
       "myFileTransDescFileName": myFileTransDescFileName,
       "myFileTransServerAddr": myFileTransServerAddr,
       "myFileTransResult": myFileTransResult,
       "myFileTransComplete": myFileTransComplete,
       "myFileTransDataLength": myFileTransDataLength,
       "myFileTransEntryStatus": myFileTransEntryStatus,
       "myFileSystemMaxRoom": myFileSystemMaxRoom,
       "myFileSystemAvailableRoom": myFileSystemAvailableRoom,
       "myFileMIBConformance": myFileMIBConformance,
       "myFileMIBCompliances": myFileMIBCompliances,
       "myFileMIBCompliance": myFileMIBCompliance,
       "myFileMIBGroups": myFileMIBGroups,
       "myFileMIBGroup": myFileMIBGroup,
       "myFileTransMeansMIBGroup": myFileTransMeansMIBGroup}
)
