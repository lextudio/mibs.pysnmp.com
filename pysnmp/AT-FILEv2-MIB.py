# SNMP MIB module (AT-FILEv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-FILEv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:09 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

atFilev2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600)
)
atFilev2.setRevisions(
        ("2014-01-17 00:00",
         "2012-09-27 00:00",
         "2012-09-21 00:00",
         "2012-05-22 05:00",
         "2012-05-07 00:00",
         "2011-09-12 00:00",
         "2011-05-30 00:00",
         "2011-04-21 00:00",
         "2011-03-24 00:00",
         "2011-01-26 00:00",
         "2010-09-07 00:00",
         "2010-06-14 04:59",
         "2008-12-05 00:00",
         "2008-11-11 00:00",
         "2008-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtFilev2TableOptions_ObjectIdentity = ObjectIdentity
atFilev2TableOptions = _AtFilev2TableOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1)
)


class _AtFilev2Recursive_Type(Integer32):
    """Custom type atFilev2Recursive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtFilev2Recursive_Type.__name__ = "Integer32"
_AtFilev2Recursive_Object = MibScalar
atFilev2Recursive = _AtFilev2Recursive_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 1),
    _AtFilev2Recursive_Type()
)
atFilev2Recursive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2Recursive.setStatus("obsolete")


class _AtFilev2AllFiles_Type(Integer32):
    """Custom type atFilev2AllFiles based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtFilev2AllFiles_Type.__name__ = "Integer32"
_AtFilev2AllFiles_Object = MibScalar
atFilev2AllFiles = _AtFilev2AllFiles_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 2),
    _AtFilev2AllFiles_Type()
)
atFilev2AllFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2AllFiles.setStatus("obsolete")


class _AtFilev2Device_Type(Integer32):
    """Custom type atFilev2Device based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AtFilev2Device_Type.__name__ = "Integer32"
_AtFilev2Device_Object = MibScalar
atFilev2Device = _AtFilev2Device_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 3),
    _AtFilev2Device_Type()
)
atFilev2Device.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2Device.setStatus("obsolete")


class _AtFilev2StackID_Type(Integer32):
    """Custom type atFilev2StackID based on Integer32"""
    defaultValue = 1


_AtFilev2StackID_Object = MibScalar
atFilev2StackID = _AtFilev2StackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 4),
    _AtFilev2StackID_Type()
)
atFilev2StackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2StackID.setStatus("obsolete")
_AtFilev2Table_Object = MibTable
atFilev2Table = _AtFilev2Table_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2)
)
if mibBuilder.loadTexts:
    atFilev2Table.setStatus("obsolete")
_AtFilev2Entry_Object = MibTableRow
atFilev2Entry = _AtFilev2Entry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1)
)
atFilev2Entry.setIndexNames(
    (0, "AT-FILEv2-MIB", "atFilev2Filename"),
)
if mibBuilder.loadTexts:
    atFilev2Entry.setStatus("obsolete")


class _AtFilev2Filename_Type(OctetString):
    """Custom type atFilev2Filename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 112),
    )


_AtFilev2Filename_Type.__name__ = "OctetString"
_AtFilev2Filename_Object = MibTableColumn
atFilev2Filename = _AtFilev2Filename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 1),
    _AtFilev2Filename_Type()
)
atFilev2Filename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2Filename.setStatus("obsolete")
_AtFilev2FileSize_Type = Integer32
_AtFilev2FileSize_Object = MibTableColumn
atFilev2FileSize = _AtFilev2FileSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 2),
    _AtFilev2FileSize_Type()
)
atFilev2FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileSize.setStatus("obsolete")
_AtFilev2FileCreationTime_Type = OctetString
_AtFilev2FileCreationTime_Object = MibTableColumn
atFilev2FileCreationTime = _AtFilev2FileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 3),
    _AtFilev2FileCreationTime_Type()
)
atFilev2FileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileCreationTime.setStatus("obsolete")
_AtFilev2FileAttribs_Type = OctetString
_AtFilev2FileAttribs_Object = MibTableColumn
atFilev2FileAttribs = _AtFilev2FileAttribs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 4),
    _AtFilev2FileAttribs_Type()
)
atFilev2FileAttribs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileAttribs.setStatus("obsolete")
_AtFilev2FileOperation_ObjectIdentity = ObjectIdentity
atFilev2FileOperation = _AtFilev2FileOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3)
)
_AtFilev2SourceStackID_Type = Integer32
_AtFilev2SourceStackID_Object = MibScalar
atFilev2SourceStackID = _AtFilev2SourceStackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 1),
    _AtFilev2SourceStackID_Type()
)
atFilev2SourceStackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceStackID.setStatus("current")


class _AtFilev2SourceDevice_Type(Integer32):
    """Custom type atFilev2SourceDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("flash", 1),
          ("nvs", 3),
          ("tftp", 4),
          ("usb", 5))
    )


_AtFilev2SourceDevice_Type.__name__ = "Integer32"
_AtFilev2SourceDevice_Object = MibScalar
atFilev2SourceDevice = _AtFilev2SourceDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 2),
    _AtFilev2SourceDevice_Type()
)
atFilev2SourceDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceDevice.setStatus("current")
_AtFilev2SourceFilename_Type = DisplayString
_AtFilev2SourceFilename_Object = MibScalar
atFilev2SourceFilename = _AtFilev2SourceFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 3),
    _AtFilev2SourceFilename_Type()
)
atFilev2SourceFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceFilename.setStatus("current")
_AtFilev2DestinationStackID_Type = Integer32
_AtFilev2DestinationStackID_Object = MibScalar
atFilev2DestinationStackID = _AtFilev2DestinationStackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 4),
    _AtFilev2DestinationStackID_Type()
)
atFilev2DestinationStackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationStackID.setStatus("current")


class _AtFilev2DestinationDevice_Type(Integer32):
    """Custom type atFilev2DestinationDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("flash", 1),
          ("nvs", 3),
          ("tftp", 4),
          ("usb", 5))
    )


_AtFilev2DestinationDevice_Type.__name__ = "Integer32"
_AtFilev2DestinationDevice_Object = MibScalar
atFilev2DestinationDevice = _AtFilev2DestinationDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 5),
    _AtFilev2DestinationDevice_Type()
)
atFilev2DestinationDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationDevice.setStatus("current")
_AtFilev2DestinationFilename_Type = DisplayString
_AtFilev2DestinationFilename_Object = MibScalar
atFilev2DestinationFilename = _AtFilev2DestinationFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 6),
    _AtFilev2DestinationFilename_Type()
)
atFilev2DestinationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationFilename.setStatus("current")
_AtFilev2CopyBegin_Type = OctetString
_AtFilev2CopyBegin_Object = MibScalar
atFilev2CopyBegin = _AtFilev2CopyBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 7),
    _AtFilev2CopyBegin_Type()
)
atFilev2CopyBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2CopyBegin.setStatus("current")
_AtFilev2MoveBegin_Type = OctetString
_AtFilev2MoveBegin_Object = MibScalar
atFilev2MoveBegin = _AtFilev2MoveBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 8),
    _AtFilev2MoveBegin_Type()
)
atFilev2MoveBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2MoveBegin.setStatus("current")
_AtFilev2DeleteBegin_Type = OctetString
_AtFilev2DeleteBegin_Object = MibScalar
atFilev2DeleteBegin = _AtFilev2DeleteBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 9),
    _AtFilev2DeleteBegin_Type()
)
atFilev2DeleteBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DeleteBegin.setStatus("current")
_AtFilev2Flash_1_ObjectIdentity = ObjectIdentity
atFilev2Flash_1 = _AtFilev2Flash_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 10)
)
_AtFilev2Card_2_ObjectIdentity = ObjectIdentity
atFilev2Card_2 = _AtFilev2Card_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 11)
)
_AtFilev2Nvs_3_ObjectIdentity = ObjectIdentity
atFilev2Nvs_3 = _AtFilev2Nvs_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 12)
)
_AtFilev2Tftp_4_ObjectIdentity = ObjectIdentity
atFilev2Tftp_4 = _AtFilev2Tftp_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13)
)
_AtFilev2TftpIPAddr_Type = IpAddress
_AtFilev2TftpIPAddr_Object = MibScalar
atFilev2TftpIPAddr = _AtFilev2TftpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13, 1),
    _AtFilev2TftpIPAddr_Type()
)
atFilev2TftpIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2TftpIPAddr.setStatus("current")
_AtFilev2DirOperation_ObjectIdentity = ObjectIdentity
atFilev2DirOperation = _AtFilev2DirOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14)
)
_AtFilev2DirStackID_Type = Integer32
_AtFilev2DirStackID_Object = MibScalar
atFilev2DirStackID = _AtFilev2DirStackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 1),
    _AtFilev2DirStackID_Type()
)
atFilev2DirStackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DirStackID.setStatus("current")


class _AtFilev2DirFileSystem_Type(Integer32):
    """Custom type atFilev2DirFileSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("flash", 1),
          ("nvs", 3),
          ("usb", 5))
    )


_AtFilev2DirFileSystem_Type.__name__ = "Integer32"
_AtFilev2DirFileSystem_Object = MibScalar
atFilev2DirFileSystem = _AtFilev2DirFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 2),
    _AtFilev2DirFileSystem_Type()
)
atFilev2DirFileSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DirFileSystem.setStatus("current")
_AtFilev2DirPath_Type = DisplayString
_AtFilev2DirPath_Object = MibScalar
atFilev2DirPath = _AtFilev2DirPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 3),
    _AtFilev2DirPath_Type()
)
atFilev2DirPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DirPath.setStatus("current")
_AtFilev2SourceDirName_Type = DisplayString
_AtFilev2SourceDirName_Object = MibScalar
atFilev2SourceDirName = _AtFilev2SourceDirName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 4),
    _AtFilev2SourceDirName_Type()
)
atFilev2SourceDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceDirName.setStatus("current")
_AtFilev2DestDirName_Type = DisplayString
_AtFilev2DestDirName_Object = MibScalar
atFilev2DestDirName = _AtFilev2DestDirName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 5),
    _AtFilev2DestDirName_Type()
)
atFilev2DestDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestDirName.setStatus("current")


class _AtFilev2BeginDirOperation_Type(Integer32):
    """Custom type atFilev2BeginDirOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("createDir", 2),
          ("deleteEmptyDir", 4),
          ("deleteForceDir", 5),
          ("idle", 1),
          ("renameDir", 3))
    )


_AtFilev2BeginDirOperation_Type.__name__ = "Integer32"
_AtFilev2BeginDirOperation_Object = MibScalar
atFilev2BeginDirOperation = _AtFilev2BeginDirOperation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 6),
    _AtFilev2BeginDirOperation_Type()
)
atFilev2BeginDirOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2BeginDirOperation.setStatus("current")
_AtFilev2LastDirOpResult_Type = DisplayString
_AtFilev2LastDirOpResult_Object = MibScalar
atFilev2LastDirOpResult = _AtFilev2LastDirOpResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 7),
    _AtFilev2LastDirOpResult_Type()
)
atFilev2LastDirOpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2LastDirOpResult.setStatus("current")
_AtFilev2Usb_5_ObjectIdentity = ObjectIdentity
atFilev2Usb_5 = _AtFilev2Usb_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 15)
)
_AtFilev2SDcardTable_Object = MibTable
atFilev2SDcardTable = _AtFilev2SDcardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4)
)
if mibBuilder.loadTexts:
    atFilev2SDcardTable.setStatus("current")
_AtFilev2SDcardEntry_Object = MibTableRow
atFilev2SDcardEntry = _AtFilev2SDcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1)
)
atFilev2SDcardEntry.setIndexNames(
    (0, "AT-FILEv2-MIB", "atFilev2SDcardStackMemberId"),
)
if mibBuilder.loadTexts:
    atFilev2SDcardEntry.setStatus("current")
_AtFilev2SDcardStackMemberId_Type = Unsigned32
_AtFilev2SDcardStackMemberId_Object = MibTableColumn
atFilev2SDcardStackMemberId = _AtFilev2SDcardStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 1),
    _AtFilev2SDcardStackMemberId_Type()
)
atFilev2SDcardStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2SDcardStackMemberId.setStatus("current")


class _AtFilev2SDcardPresence_Type(Integer32):
    """Custom type atFilev2SDcardPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_AtFilev2SDcardPresence_Type.__name__ = "Integer32"
_AtFilev2SDcardPresence_Object = MibTableColumn
atFilev2SDcardPresence = _AtFilev2SDcardPresence_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 2),
    _AtFilev2SDcardPresence_Type()
)
atFilev2SDcardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2SDcardPresence.setStatus("current")
_AtFilev2InfoTable_Object = MibTable
atFilev2InfoTable = _AtFilev2InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5)
)
if mibBuilder.loadTexts:
    atFilev2InfoTable.setStatus("obsolete")
_AtFilev2InfoEntry_Object = MibTableRow
atFilev2InfoEntry = _AtFilev2InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1)
)
atFilev2InfoEntry.setIndexNames(
    (1, "AT-FILEv2-MIB", "atFilev2InfoFilepath"),
)
if mibBuilder.loadTexts:
    atFilev2InfoEntry.setStatus("obsolete")


class _AtFilev2InfoFilepath_Type(OctetString):
    """Custom type atFilev2InfoFilepath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 112),
    )


_AtFilev2InfoFilepath_Type.__name__ = "OctetString"
_AtFilev2InfoFilepath_Object = MibTableColumn
atFilev2InfoFilepath = _AtFilev2InfoFilepath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 1),
    _AtFilev2InfoFilepath_Type()
)
atFilev2InfoFilepath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFilepath.setStatus("obsolete")
_AtFilev2InfoFileSize_Type = Counter64
_AtFilev2InfoFileSize_Object = MibTableColumn
atFilev2InfoFileSize = _AtFilev2InfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 2),
    _AtFilev2InfoFileSize_Type()
)
atFilev2InfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileSize.setStatus("obsolete")
_AtFilev2InfoFileCreationTime_Type = OctetString
_AtFilev2InfoFileCreationTime_Object = MibTableColumn
atFilev2InfoFileCreationTime = _AtFilev2InfoFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 3),
    _AtFilev2InfoFileCreationTime_Type()
)
atFilev2InfoFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileCreationTime.setStatus("obsolete")
_AtFilev2InfoFileIsDirectory_Type = TruthValue
_AtFilev2InfoFileIsDirectory_Object = MibTableColumn
atFilev2InfoFileIsDirectory = _AtFilev2InfoFileIsDirectory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 4),
    _AtFilev2InfoFileIsDirectory_Type()
)
atFilev2InfoFileIsDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileIsDirectory.setStatus("obsolete")
_AtFilev2InfoFileIsReadable_Type = TruthValue
_AtFilev2InfoFileIsReadable_Object = MibTableColumn
atFilev2InfoFileIsReadable = _AtFilev2InfoFileIsReadable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 5),
    _AtFilev2InfoFileIsReadable_Type()
)
atFilev2InfoFileIsReadable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileIsReadable.setStatus("obsolete")
_AtFilev2InfoFileIsWriteable_Type = TruthValue
_AtFilev2InfoFileIsWriteable_Object = MibTableColumn
atFilev2InfoFileIsWriteable = _AtFilev2InfoFileIsWriteable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 6),
    _AtFilev2InfoFileIsWriteable_Type()
)
atFilev2InfoFileIsWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileIsWriteable.setStatus("obsolete")
_AtFilev2InfoFileIsExecutable_Type = TruthValue
_AtFilev2InfoFileIsExecutable_Object = MibTableColumn
atFilev2InfoFileIsExecutable = _AtFilev2InfoFileIsExecutable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 7),
    _AtFilev2InfoFileIsExecutable_Type()
)
atFilev2InfoFileIsExecutable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2InfoFileIsExecutable.setStatus("obsolete")
_AtFilev2USBMediaTable_Object = MibTable
atFilev2USBMediaTable = _AtFilev2USBMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6)
)
if mibBuilder.loadTexts:
    atFilev2USBMediaTable.setStatus("current")
_AtFilev2USBMediaEntry_Object = MibTableRow
atFilev2USBMediaEntry = _AtFilev2USBMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1)
)
atFilev2USBMediaEntry.setIndexNames(
    (0, "AT-FILEv2-MIB", "atFilev2USBMediaStackMemberId"),
)
if mibBuilder.loadTexts:
    atFilev2USBMediaEntry.setStatus("current")
_AtFilev2USBMediaStackMemberId_Type = Unsigned32
_AtFilev2USBMediaStackMemberId_Object = MibTableColumn
atFilev2USBMediaStackMemberId = _AtFilev2USBMediaStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1, 1),
    _AtFilev2USBMediaStackMemberId_Type()
)
atFilev2USBMediaStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2USBMediaStackMemberId.setStatus("current")


class _AtFilev2USBMediaPresence_Type(Integer32):
    """Custom type atFilev2USBMediaPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_AtFilev2USBMediaPresence_Type.__name__ = "Integer32"
_AtFilev2USBMediaPresence_Object = MibTableColumn
atFilev2USBMediaPresence = _AtFilev2USBMediaPresence_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1, 2),
    _AtFilev2USBMediaPresence_Type()
)
atFilev2USBMediaPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2USBMediaPresence.setStatus("current")
_AtFilev2FileViewer_ObjectIdentity = ObjectIdentity
atFilev2FileViewer = _AtFilev2FileViewer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7)
)


class _AtFilev2FileViewerStackId_Type(Integer32):
    """Custom type atFilev2FileViewerStackId based on Integer32"""
    defaultValue = 1


_AtFilev2FileViewerStackId_Object = MibScalar
atFilev2FileViewerStackId = _AtFilev2FileViewerStackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 1),
    _AtFilev2FileViewerStackId_Type()
)
atFilev2FileViewerStackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2FileViewerStackId.setStatus("current")


class _AtFilev2FileViewerDevice_Type(Integer32):
    """Custom type atFilev2FileViewerDevice based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("flash", 1),
          ("nvs", 3),
          ("tftp", 4),
          ("usb", 5))
    )


_AtFilev2FileViewerDevice_Type.__name__ = "Integer32"
_AtFilev2FileViewerDevice_Object = MibScalar
atFilev2FileViewerDevice = _AtFilev2FileViewerDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 2),
    _AtFilev2FileViewerDevice_Type()
)
atFilev2FileViewerDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2FileViewerDevice.setStatus("current")
_AtFilev2FileViewerCurrentPath_Type = DisplayString
_AtFilev2FileViewerCurrentPath_Object = MibScalar
atFilev2FileViewerCurrentPath = _AtFilev2FileViewerCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 3),
    _AtFilev2FileViewerCurrentPath_Type()
)
atFilev2FileViewerCurrentPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2FileViewerCurrentPath.setStatus("current")
_AtFilev2FileViewerTable_Object = MibTable
atFilev2FileViewerTable = _AtFilev2FileViewerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4)
)
if mibBuilder.loadTexts:
    atFilev2FileViewerTable.setStatus("current")
_AtFilev2FileViewerEntry_Object = MibTableRow
atFilev2FileViewerEntry = _AtFilev2FileViewerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1)
)
atFilev2FileViewerEntry.setIndexNames(
    (1, "AT-FILEv2-MIB", "atFilev2FileViewerName"),
)
if mibBuilder.loadTexts:
    atFilev2FileViewerEntry.setStatus("current")


class _AtFilev2FileViewerName_Type(DisplayString):
    """Custom type atFilev2FileViewerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 112),
    )


_AtFilev2FileViewerName_Type.__name__ = "DisplayString"
_AtFilev2FileViewerName_Object = MibTableColumn
atFilev2FileViewerName = _AtFilev2FileViewerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 1),
    _AtFilev2FileViewerName_Type()
)
atFilev2FileViewerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerName.setStatus("current")
_AtFilev2FileViewerSize_Type = Counter64
_AtFilev2FileViewerSize_Object = MibTableColumn
atFilev2FileViewerSize = _AtFilev2FileViewerSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 2),
    _AtFilev2FileViewerSize_Type()
)
atFilev2FileViewerSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerSize.setStatus("current")
_AtFilev2FileViewerCreationTime_Type = DisplayString
_AtFilev2FileViewerCreationTime_Object = MibTableColumn
atFilev2FileViewerCreationTime = _AtFilev2FileViewerCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 3),
    _AtFilev2FileViewerCreationTime_Type()
)
atFilev2FileViewerCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerCreationTime.setStatus("current")
_AtFilev2FileViewerIsDirectory_Type = TruthValue
_AtFilev2FileViewerIsDirectory_Object = MibTableColumn
atFilev2FileViewerIsDirectory = _AtFilev2FileViewerIsDirectory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 4),
    _AtFilev2FileViewerIsDirectory_Type()
)
atFilev2FileViewerIsDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerIsDirectory.setStatus("current")
_AtFilev2FileViewerIsReadable_Type = TruthValue
_AtFilev2FileViewerIsReadable_Object = MibTableColumn
atFilev2FileViewerIsReadable = _AtFilev2FileViewerIsReadable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 5),
    _AtFilev2FileViewerIsReadable_Type()
)
atFilev2FileViewerIsReadable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerIsReadable.setStatus("current")
_AtFilev2FileViewerIsWriteable_Type = TruthValue
_AtFilev2FileViewerIsWriteable_Object = MibTableColumn
atFilev2FileViewerIsWriteable = _AtFilev2FileViewerIsWriteable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 6),
    _AtFilev2FileViewerIsWriteable_Type()
)
atFilev2FileViewerIsWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerIsWriteable.setStatus("current")
_AtFilev2FileViewerIsExecutable_Type = TruthValue
_AtFilev2FileViewerIsExecutable_Object = MibTableColumn
atFilev2FileViewerIsExecutable = _AtFilev2FileViewerIsExecutable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 7),
    _AtFilev2FileViewerIsExecutable_Type()
)
atFilev2FileViewerIsExecutable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileViewerIsExecutable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FILEv2-MIB",
    **{"atFilev2": atFilev2,
       "atFilev2TableOptions": atFilev2TableOptions,
       "atFilev2Recursive": atFilev2Recursive,
       "atFilev2AllFiles": atFilev2AllFiles,
       "atFilev2Device": atFilev2Device,
       "atFilev2StackID": atFilev2StackID,
       "atFilev2Table": atFilev2Table,
       "atFilev2Entry": atFilev2Entry,
       "atFilev2Filename": atFilev2Filename,
       "atFilev2FileSize": atFilev2FileSize,
       "atFilev2FileCreationTime": atFilev2FileCreationTime,
       "atFilev2FileAttribs": atFilev2FileAttribs,
       "atFilev2FileOperation": atFilev2FileOperation,
       "atFilev2SourceStackID": atFilev2SourceStackID,
       "atFilev2SourceDevice": atFilev2SourceDevice,
       "atFilev2SourceFilename": atFilev2SourceFilename,
       "atFilev2DestinationStackID": atFilev2DestinationStackID,
       "atFilev2DestinationDevice": atFilev2DestinationDevice,
       "atFilev2DestinationFilename": atFilev2DestinationFilename,
       "atFilev2CopyBegin": atFilev2CopyBegin,
       "atFilev2MoveBegin": atFilev2MoveBegin,
       "atFilev2DeleteBegin": atFilev2DeleteBegin,
       "atFilev2Flash_1": atFilev2Flash_1,
       "atFilev2Card_2": atFilev2Card_2,
       "atFilev2Nvs_3": atFilev2Nvs_3,
       "atFilev2Tftp_4": atFilev2Tftp_4,
       "atFilev2TftpIPAddr": atFilev2TftpIPAddr,
       "atFilev2DirOperation": atFilev2DirOperation,
       "atFilev2DirStackID": atFilev2DirStackID,
       "atFilev2DirFileSystem": atFilev2DirFileSystem,
       "atFilev2DirPath": atFilev2DirPath,
       "atFilev2SourceDirName": atFilev2SourceDirName,
       "atFilev2DestDirName": atFilev2DestDirName,
       "atFilev2BeginDirOperation": atFilev2BeginDirOperation,
       "atFilev2LastDirOpResult": atFilev2LastDirOpResult,
       "atFilev2Usb_5": atFilev2Usb_5,
       "atFilev2SDcardTable": atFilev2SDcardTable,
       "atFilev2SDcardEntry": atFilev2SDcardEntry,
       "atFilev2SDcardStackMemberId": atFilev2SDcardStackMemberId,
       "atFilev2SDcardPresence": atFilev2SDcardPresence,
       "atFilev2InfoTable": atFilev2InfoTable,
       "atFilev2InfoEntry": atFilev2InfoEntry,
       "atFilev2InfoFilepath": atFilev2InfoFilepath,
       "atFilev2InfoFileSize": atFilev2InfoFileSize,
       "atFilev2InfoFileCreationTime": atFilev2InfoFileCreationTime,
       "atFilev2InfoFileIsDirectory": atFilev2InfoFileIsDirectory,
       "atFilev2InfoFileIsReadable": atFilev2InfoFileIsReadable,
       "atFilev2InfoFileIsWriteable": atFilev2InfoFileIsWriteable,
       "atFilev2InfoFileIsExecutable": atFilev2InfoFileIsExecutable,
       "atFilev2USBMediaTable": atFilev2USBMediaTable,
       "atFilev2USBMediaEntry": atFilev2USBMediaEntry,
       "atFilev2USBMediaStackMemberId": atFilev2USBMediaStackMemberId,
       "atFilev2USBMediaPresence": atFilev2USBMediaPresence,
       "atFilev2FileViewer": atFilev2FileViewer,
       "atFilev2FileViewerStackId": atFilev2FileViewerStackId,
       "atFilev2FileViewerDevice": atFilev2FileViewerDevice,
       "atFilev2FileViewerCurrentPath": atFilev2FileViewerCurrentPath,
       "atFilev2FileViewerTable": atFilev2FileViewerTable,
       "atFilev2FileViewerEntry": atFilev2FileViewerEntry,
       "atFilev2FileViewerName": atFilev2FileViewerName,
       "atFilev2FileViewerSize": atFilev2FileViewerSize,
       "atFilev2FileViewerCreationTime": atFilev2FileViewerCreationTime,
       "atFilev2FileViewerIsDirectory": atFilev2FileViewerIsDirectory,
       "atFilev2FileViewerIsReadable": atFilev2FileViewerIsReadable,
       "atFilev2FileViewerIsWriteable": atFilev2FileViewerIsWriteable,
       "atFilev2FileViewerIsExecutable": atFilev2FileViewerIsExecutable}
)
