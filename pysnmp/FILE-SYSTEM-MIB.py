# SNMP MIB module (FILE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FILE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:54 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

swFileSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwFSBasicInfo_ObjectIdentity = ObjectIdentity
swFSBasicInfo = _SwFSBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 1)
)


class _SwFSBasicInfoCtrlStatus_Type(Integer32):
    """Custom type swFSBasicInfoCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("access-media-error", 20),
          ("error-char", 18),
          ("error-filename", 19),
          ("error-input", 17),
          ("exist-file-in-directory", 12),
          ("exist-same-directory", 11),
          ("fail", 4),
          ("file-readonly", 10),
          ("finish", 2),
          ("fs-no-match-media", 16),
          ("in-process", 3),
          ("insufficient-disk", 8),
          ("invalid-directory", 9),
          ("invalid-drive-name", 5),
          ("no-file-or-dir", 13),
          ("no-format", 14),
          ("no-storage-media", 15),
          ("other", 0),
          ("root-area-full", 7),
          ("same-file-name", 6),
          ("start", 1))
    )


_SwFSBasicInfoCtrlStatus_Type.__name__ = "Integer32"
_SwFSBasicInfoCtrlStatus_Object = MibScalar
swFSBasicInfoCtrlStatus = _SwFSBasicInfoCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 1, 1),
    _SwFSBasicInfoCtrlStatus_Type()
)
swFSBasicInfoCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSBasicInfoCtrlStatus.setStatus("current")


class _SwFSBasicInfoCtrlProcess_Type(Integer32):
    """Custom type swFSBasicInfoCtrlProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwFSBasicInfoCtrlProcess_Type.__name__ = "Integer32"
_SwFSBasicInfoCtrlProcess_Object = MibScalar
swFSBasicInfoCtrlProcess = _SwFSBasicInfoCtrlProcess_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 1, 2),
    _SwFSBasicInfoCtrlProcess_Type()
)
swFSBasicInfoCtrlProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSBasicInfoCtrlProcess.setStatus("current")
if mibBuilder.loadTexts:
    swFSBasicInfoCtrlProcess.setUnits("%")
_SwFSDriveCtrl_ObjectIdentity = ObjectIdentity
swFSDriveCtrl = _SwFSDriveCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2)
)
_SwFSDriveInfoTable_Object = MibTable
swFSDriveInfoTable = _SwFSDriveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1)
)
if mibBuilder.loadTexts:
    swFSDriveInfoTable.setStatus("current")
_SwFSDriveInfoEntry_Object = MibTableRow
swFSDriveInfoEntry = _SwFSDriveInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1)
)
swFSDriveInfoEntry.setIndexNames(
    (0, "FILE-SYSTEM-MIB", "swFSDriveInfoIndex"),
)
if mibBuilder.loadTexts:
    swFSDriveInfoEntry.setStatus("current")
_SwFSDriveInfoIndex_Type = Integer32
_SwFSDriveInfoIndex_Object = MibTableColumn
swFSDriveInfoIndex = _SwFSDriveInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 1),
    _SwFSDriveInfoIndex_Type()
)
swFSDriveInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swFSDriveInfoIndex.setStatus("current")


class _SwFSDriveInfoDriveID_Type(Integer32):
    """Custom type swFSDriveInfoDriveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4),
          ("f", 5),
          ("g", 6),
          ("h", 7),
          ("i", 8),
          ("j", 9),
          ("k", 10),
          ("l", 11),
          ("m", 12),
          ("n", 13),
          ("o", 14),
          ("p", 15),
          ("q", 16),
          ("r", 17),
          ("s", 18),
          ("t", 19),
          ("u", 20),
          ("v", 21),
          ("w", 22),
          ("x", 23),
          ("y", 24),
          ("z", 25))
    )


_SwFSDriveInfoDriveID_Type.__name__ = "Integer32"
_SwFSDriveInfoDriveID_Object = MibTableColumn
swFSDriveInfoDriveID = _SwFSDriveInfoDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 2),
    _SwFSDriveInfoDriveID_Type()
)
swFSDriveInfoDriveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoDriveID.setStatus("current")


class _SwFSDriveInfoType_Type(DisplayString):
    """Custom type swFSDriveInfoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoType_Type.__name__ = "DisplayString"
_SwFSDriveInfoType_Object = MibTableColumn
swFSDriveInfoType = _SwFSDriveInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 3),
    _SwFSDriveInfoType_Type()
)
swFSDriveInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoType.setStatus("current")
_SwFSDriveInfoSize_Type = Integer32
_SwFSDriveInfoSize_Object = MibTableColumn
swFSDriveInfoSize = _SwFSDriveInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 4),
    _SwFSDriveInfoSize_Type()
)
swFSDriveInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoSize.setStatus("current")


class _SwFSDriveInfoPartition_Type(DisplayString):
    """Custom type swFSDriveInfoPartition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoPartition_Type.__name__ = "DisplayString"
_SwFSDriveInfoPartition_Object = MibTableColumn
swFSDriveInfoPartition = _SwFSDriveInfoPartition_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 5),
    _SwFSDriveInfoPartition_Type()
)
swFSDriveInfoPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoPartition.setStatus("current")


class _SwFSDriveInfoFStype_Type(DisplayString):
    """Custom type swFSDriveInfoFStype based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoFStype_Type.__name__ = "DisplayString"
_SwFSDriveInfoFStype_Object = MibTableColumn
swFSDriveInfoFStype = _SwFSDriveInfoFStype_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 1, 1, 6),
    _SwFSDriveInfoFStype_Type()
)
swFSDriveInfoFStype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoFStype.setStatus("current")
_SwFSDriveFormatCtrl_ObjectIdentity = ObjectIdentity
swFSDriveFormatCtrl = _SwFSDriveFormatCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2)
)


class _SwFSDriveFormatDriveID_Type(Integer32):
    """Custom type swFSDriveFormatDriveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8),
          ("i", 9),
          ("j", 10),
          ("k", 11),
          ("l", 12),
          ("m", 13),
          ("n", 14),
          ("none", 0),
          ("o", 15),
          ("p", 16),
          ("q", 17),
          ("r", 18),
          ("s", 19),
          ("t", 20),
          ("u", 21),
          ("v", 22),
          ("w", 23),
          ("x", 24),
          ("y", 25),
          ("z", 26))
    )


_SwFSDriveFormatDriveID_Type.__name__ = "Integer32"
_SwFSDriveFormatDriveID_Object = MibScalar
swFSDriveFormatDriveID = _SwFSDriveFormatDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2, 1),
    _SwFSDriveFormatDriveID_Type()
)
swFSDriveFormatDriveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveFormatDriveID.setStatus("current")


class _SwFSDriveFormatFat_Type(Integer32):
    """Custom type swFSDriveFormatFat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fat16", 1),
          ("fat32", 2))
    )


_SwFSDriveFormatFat_Type.__name__ = "Integer32"
_SwFSDriveFormatFat_Object = MibScalar
swFSDriveFormatFat = _SwFSDriveFormatFat_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2, 2),
    _SwFSDriveFormatFat_Type()
)
swFSDriveFormatFat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveFormatFat.setStatus("current")


class _SwFSDriveFormatLabelName_Type(DisplayString):
    """Custom type swFSDriveFormatLabelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SwFSDriveFormatLabelName_Type.__name__ = "DisplayString"
_SwFSDriveFormatLabelName_Object = MibScalar
swFSDriveFormatLabelName = _SwFSDriveFormatLabelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2, 3),
    _SwFSDriveFormatLabelName_Type()
)
swFSDriveFormatLabelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveFormatLabelName.setStatus("current")


class _SwFSDriveFormatType_Type(Integer32):
    """Custom type swFSDriveFormatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("full", 2),
          ("full-with-mbr", 3))
    )


_SwFSDriveFormatType_Type.__name__ = "Integer32"
_SwFSDriveFormatType_Object = MibScalar
swFSDriveFormatType = _SwFSDriveFormatType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2, 4),
    _SwFSDriveFormatType_Type()
)
swFSDriveFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveFormatType.setStatus("current")


class _SwFSDriveFormatActivity_Type(Integer32):
    """Custom type swFSDriveFormatActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwFSDriveFormatActivity_Type.__name__ = "Integer32"
_SwFSDriveFormatActivity_Object = MibScalar
swFSDriveFormatActivity = _SwFSDriveFormatActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 2, 5),
    _SwFSDriveFormatActivity_Type()
)
swFSDriveFormatActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveFormatActivity.setStatus("current")
_SwFSDriveChangeCtrl_ObjectIdentity = ObjectIdentity
swFSDriveChangeCtrl = _SwFSDriveChangeCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 3)
)
_SwFSDriveChangeUnitID_Type = Integer32
_SwFSDriveChangeUnitID_Object = MibScalar
swFSDriveChangeUnitID = _SwFSDriveChangeUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 3, 1),
    _SwFSDriveChangeUnitID_Type()
)
swFSDriveChangeUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveChangeUnitID.setStatus("current")


class _SwFSDriveChangeDriveID_Type(Integer32):
    """Custom type swFSDriveChangeDriveID based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_SwFSDriveChangeDriveID_Type.__name__ = "Integer32"
_SwFSDriveChangeDriveID_Object = MibScalar
swFSDriveChangeDriveID = _SwFSDriveChangeDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 3, 2),
    _SwFSDriveChangeDriveID_Type()
)
swFSDriveChangeDriveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveChangeDriveID.setStatus("current")


class _SwFSDriveCurrentDirectory_Type(DisplayString):
    """Custom type swFSDriveCurrentDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFSDriveCurrentDirectory_Type.__name__ = "DisplayString"
_SwFSDriveCurrentDirectory_Object = MibScalar
swFSDriveCurrentDirectory = _SwFSDriveCurrentDirectory_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 3, 3),
    _SwFSDriveCurrentDirectory_Type()
)
swFSDriveCurrentDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDriveCurrentDirectory.setStatus("current")
_SwFSDriveInfoStackTable_Object = MibTable
swFSDriveInfoStackTable = _SwFSDriveInfoStackTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4)
)
if mibBuilder.loadTexts:
    swFSDriveInfoStackTable.setStatus("current")
_SwFSDriveInfoStackEntry_Object = MibTableRow
swFSDriveInfoStackEntry = _SwFSDriveInfoStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1)
)
swFSDriveInfoStackEntry.setIndexNames(
    (0, "FILE-SYSTEM-MIB", "swFSDriveInfoStackUnitID"),
    (0, "FILE-SYSTEM-MIB", "swFSDriveInfoStackIndex"),
)
if mibBuilder.loadTexts:
    swFSDriveInfoStackEntry.setStatus("current")
_SwFSDriveInfoStackUnitID_Type = Integer32
_SwFSDriveInfoStackUnitID_Object = MibTableColumn
swFSDriveInfoStackUnitID = _SwFSDriveInfoStackUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 1),
    _SwFSDriveInfoStackUnitID_Type()
)
swFSDriveInfoStackUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackUnitID.setStatus("current")
_SwFSDriveInfoStackIndex_Type = Integer32
_SwFSDriveInfoStackIndex_Object = MibTableColumn
swFSDriveInfoStackIndex = _SwFSDriveInfoStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 2),
    _SwFSDriveInfoStackIndex_Type()
)
swFSDriveInfoStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swFSDriveInfoStackIndex.setStatus("current")


class _SwFSDriveInfoStackDriveID_Type(Integer32):
    """Custom type swFSDriveInfoStackDriveID based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8),
          ("i", 9),
          ("j", 10),
          ("k", 11),
          ("l", 12),
          ("m", 13),
          ("n", 14),
          ("o", 15),
          ("p", 16),
          ("q", 17),
          ("r", 18),
          ("s", 19),
          ("t", 20),
          ("u", 21),
          ("v", 22),
          ("w", 23),
          ("x", 24),
          ("y", 25),
          ("z", 26))
    )


_SwFSDriveInfoStackDriveID_Type.__name__ = "Integer32"
_SwFSDriveInfoStackDriveID_Object = MibTableColumn
swFSDriveInfoStackDriveID = _SwFSDriveInfoStackDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 3),
    _SwFSDriveInfoStackDriveID_Type()
)
swFSDriveInfoStackDriveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackDriveID.setStatus("current")


class _SwFSDriveInfoStackType_Type(DisplayString):
    """Custom type swFSDriveInfoStackType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoStackType_Type.__name__ = "DisplayString"
_SwFSDriveInfoStackType_Object = MibTableColumn
swFSDriveInfoStackType = _SwFSDriveInfoStackType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 4),
    _SwFSDriveInfoStackType_Type()
)
swFSDriveInfoStackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackType.setStatus("current")
_SwFSDriveInfoStackSize_Type = Integer32
_SwFSDriveInfoStackSize_Object = MibTableColumn
swFSDriveInfoStackSize = _SwFSDriveInfoStackSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 5),
    _SwFSDriveInfoStackSize_Type()
)
swFSDriveInfoStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackSize.setStatus("current")


class _SwFSDriveInfoStackPartition_Type(DisplayString):
    """Custom type swFSDriveInfoStackPartition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoStackPartition_Type.__name__ = "DisplayString"
_SwFSDriveInfoStackPartition_Object = MibTableColumn
swFSDriveInfoStackPartition = _SwFSDriveInfoStackPartition_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 6),
    _SwFSDriveInfoStackPartition_Type()
)
swFSDriveInfoStackPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackPartition.setStatus("current")


class _SwFSDriveInfoStackFStype_Type(DisplayString):
    """Custom type swFSDriveInfoStackFStype based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDriveInfoStackFStype_Type.__name__ = "DisplayString"
_SwFSDriveInfoStackFStype_Object = MibTableColumn
swFSDriveInfoStackFStype = _SwFSDriveInfoStackFStype_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 2, 4, 1, 7),
    _SwFSDriveInfoStackFStype_Type()
)
swFSDriveInfoStackFStype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDriveInfoStackFStype.setStatus("current")
_SwFSDirectoryCtrl_ObjectIdentity = ObjectIdentity
swFSDirectoryCtrl = _SwFSDirectoryCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3)
)


class _SwFSDirectoryMake_Type(DisplayString):
    """Custom type swFSDirectoryMake based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDirectoryMake_Type.__name__ = "DisplayString"
_SwFSDirectoryMake_Object = MibScalar
swFSDirectoryMake = _SwFSDirectoryMake_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 1),
    _SwFSDirectoryMake_Type()
)
swFSDirectoryMake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDirectoryMake.setStatus("current")


class _SwFSDirectoryDel_Type(DisplayString):
    """Custom type swFSDirectoryDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDirectoryDel_Type.__name__ = "DisplayString"
_SwFSDirectoryDel_Object = MibScalar
swFSDirectoryDel = _SwFSDirectoryDel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 2),
    _SwFSDirectoryDel_Type()
)
swFSDirectoryDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDirectoryDel.setStatus("current")
_SwFSctrlDirectoryDir_ObjectIdentity = ObjectIdentity
swFSctrlDirectoryDir = _SwFSctrlDirectoryDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3)
)


class _SwFSDirectoryPath_Type(DisplayString):
    """Custom type swFSDirectoryPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDirectoryPath_Type.__name__ = "DisplayString"
_SwFSDirectoryPath_Object = MibScalar
swFSDirectoryPath = _SwFSDirectoryPath_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 1),
    _SwFSDirectoryPath_Type()
)
swFSDirectoryPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSDirectoryPath.setStatus("current")
_SwFSDirectoryTable_Object = MibTable
swFSDirectoryTable = _SwFSDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2)
)
if mibBuilder.loadTexts:
    swFSDirectoryTable.setStatus("current")
_SwFSDirectoryEntry_Object = MibTableRow
swFSDirectoryEntry = _SwFSDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2, 1)
)
swFSDirectoryEntry.setIndexNames(
    (0, "FILE-SYSTEM-MIB", "swFSDirectoryName"),
)
if mibBuilder.loadTexts:
    swFSDirectoryEntry.setStatus("current")


class _SwFSDirectoryName_Type(DisplayString):
    """Custom type swFSDirectoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSDirectoryName_Type.__name__ = "DisplayString"
_SwFSDirectoryName_Object = MibTableColumn
swFSDirectoryName = _SwFSDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2, 1, 1),
    _SwFSDirectoryName_Type()
)
swFSDirectoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDirectoryName.setStatus("current")


class _SwFSDirectoryAttr_Type(Integer32):
    """Custom type swFSDirectoryAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dir", 1),
          ("file", 2))
    )


_SwFSDirectoryAttr_Type.__name__ = "Integer32"
_SwFSDirectoryAttr_Object = MibTableColumn
swFSDirectoryAttr = _SwFSDirectoryAttr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2, 1, 2),
    _SwFSDirectoryAttr_Type()
)
swFSDirectoryAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDirectoryAttr.setStatus("current")


class _SwFSDirectoryTime_Type(DisplayString):
    """Custom type swFSDirectoryTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFSDirectoryTime_Type.__name__ = "DisplayString"
_SwFSDirectoryTime_Object = MibTableColumn
swFSDirectoryTime = _SwFSDirectoryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2, 1, 3),
    _SwFSDirectoryTime_Type()
)
swFSDirectoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDirectoryTime.setStatus("current")
_SwFSDirectorySize_Type = Integer32
_SwFSDirectorySize_Object = MibTableColumn
swFSDirectorySize = _SwFSDirectorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 3, 3, 2, 1, 4),
    _SwFSDirectorySize_Type()
)
swFSDirectorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFSDirectorySize.setStatus("current")
if mibBuilder.loadTexts:
    swFSDirectorySize.setUnits("bytes")
_SwFSFileCtrl_ObjectIdentity = ObjectIdentity
swFSFileCtrl = _SwFSFileCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4)
)
_SwFSFileRename_ObjectIdentity = ObjectIdentity
swFSFileRename = _SwFSFileRename_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 1)
)


class _SwFSFileSourceName_Type(DisplayString):
    """Custom type swFSFileSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSFileSourceName_Type.__name__ = "DisplayString"
_SwFSFileSourceName_Object = MibScalar
swFSFileSourceName = _SwFSFileSourceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 1, 1),
    _SwFSFileSourceName_Type()
)
swFSFileSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileSourceName.setStatus("current")


class _SwFSFileTargetName_Type(DisplayString):
    """Custom type swFSFileTargetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSFileTargetName_Type.__name__ = "DisplayString"
_SwFSFileTargetName_Object = MibScalar
swFSFileTargetName = _SwFSFileTargetName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 1, 2),
    _SwFSFileTargetName_Type()
)
swFSFileTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileTargetName.setStatus("current")


class _SwFSFileRenameActivity_Type(Integer32):
    """Custom type swFSFileRenameActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwFSFileRenameActivity_Type.__name__ = "Integer32"
_SwFSFileRenameActivity_Object = MibScalar
swFSFileRenameActivity = _SwFSFileRenameActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 1, 3),
    _SwFSFileRenameActivity_Type()
)
swFSFileRenameActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileRenameActivity.setStatus("current")
_SwFSFileDel_ObjectIdentity = ObjectIdentity
swFSFileDel = _SwFSFileDel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 2)
)


class _SwFSFileDelName_Type(DisplayString):
    """Custom type swFSFileDelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSFileDelName_Type.__name__ = "DisplayString"
_SwFSFileDelName_Object = MibScalar
swFSFileDelName = _SwFSFileDelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 2, 1),
    _SwFSFileDelName_Type()
)
swFSFileDelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileDelName.setStatus("current")


class _SwFSFileDelOption_Type(Integer32):
    """Custom type swFSFileDelOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("recursive", 2))
    )


_SwFSFileDelOption_Type.__name__ = "Integer32"
_SwFSFileDelOption_Object = MibScalar
swFSFileDelOption = _SwFSFileDelOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 2, 2),
    _SwFSFileDelOption_Type()
)
swFSFileDelOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileDelOption.setStatus("current")


class _SwFSFileDelActivity_Type(Integer32):
    """Custom type swFSFileDelActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwFSFileDelActivity_Type.__name__ = "Integer32"
_SwFSFileDelActivity_Object = MibScalar
swFSFileDelActivity = _SwFSFileDelActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 4, 2, 3),
    _SwFSFileDelActivity_Type()
)
swFSFileDelActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSFileDelActivity.setStatus("current")
_SwFSCopyCtrl_ObjectIdentity = ObjectIdentity
swFSCopyCtrl = _SwFSCopyCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5)
)


class _SwFSCopySourceName_Type(DisplayString):
    """Custom type swFSCopySourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSCopySourceName_Type.__name__ = "DisplayString"
_SwFSCopySourceName_Object = MibScalar
swFSCopySourceName = _SwFSCopySourceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 1),
    _SwFSCopySourceName_Type()
)
swFSCopySourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopySourceName.setStatus("current")


class _SwFSCopyDestinationName_Type(DisplayString):
    """Custom type swFSCopyDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSCopyDestinationName_Type.__name__ = "DisplayString"
_SwFSCopyDestinationName_Object = MibScalar
swFSCopyDestinationName = _SwFSCopyDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 2),
    _SwFSCopyDestinationName_Type()
)
swFSCopyDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyDestinationName.setStatus("current")


class _SwFSCopyActivity_Type(Integer32):
    """Custom type swFSCopyActivity based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("config-to-file", 8),
          ("file-to-config", 5),
          ("file-to-file", 3),
          ("file-to-image", 4),
          ("file-to-prom", 6),
          ("image-to-file", 7),
          ("log-to-file", 9),
          ("none", 1),
          ("prom-to-file", 10),
          ("start", 2))
    )


_SwFSCopyActivity_Type.__name__ = "Integer32"
_SwFSCopyActivity_Object = MibScalar
swFSCopyActivity = _SwFSCopyActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 3),
    _SwFSCopyActivity_Type()
)
swFSCopyActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyActivity.setStatus("current")
_SwFSCopyDestinationUnitID_Type = Integer32
_SwFSCopyDestinationUnitID_Object = MibScalar
swFSCopyDestinationUnitID = _SwFSCopyDestinationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 4),
    _SwFSCopyDestinationUnitID_Type()
)
swFSCopyDestinationUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyDestinationUnitID.setStatus("current")


class _SwFSCopyDestinationDriveID_Type(Integer32):
    """Custom type swFSCopyDestinationDriveID based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_SwFSCopyDestinationDriveID_Type.__name__ = "Integer32"
_SwFSCopyDestinationDriveID_Object = MibScalar
swFSCopyDestinationDriveID = _SwFSCopyDestinationDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 5),
    _SwFSCopyDestinationDriveID_Type()
)
swFSCopyDestinationDriveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyDestinationDriveID.setStatus("current")
_SwFSCopyConfigID_Type = Integer32
_SwFSCopyConfigID_Object = MibScalar
swFSCopyConfigID = _SwFSCopyConfigID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 6),
    _SwFSCopyConfigID_Type()
)
swFSCopyConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyConfigID.setStatus("current")
_SwFSCopyImageID_Type = Integer32
_SwFSCopyImageID_Object = MibScalar
swFSCopyImageID = _SwFSCopyImageID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 5, 7),
    _SwFSCopyImageID_Type()
)
swFSCopyImageID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSCopyImageID.setStatus("current")
_SwFSMoveCtrl_ObjectIdentity = ObjectIdentity
swFSMoveCtrl = _SwFSMoveCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6)
)


class _SwFSMoveSourceName_Type(DisplayString):
    """Custom type swFSMoveSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSMoveSourceName_Type.__name__ = "DisplayString"
_SwFSMoveSourceName_Object = MibScalar
swFSMoveSourceName = _SwFSMoveSourceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6, 1),
    _SwFSMoveSourceName_Type()
)
swFSMoveSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSMoveSourceName.setStatus("current")
_SwFSMoveDestinationUnitID_Type = Integer32
_SwFSMoveDestinationUnitID_Object = MibScalar
swFSMoveDestinationUnitID = _SwFSMoveDestinationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6, 2),
    _SwFSMoveDestinationUnitID_Type()
)
swFSMoveDestinationUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSMoveDestinationUnitID.setStatus("current")


class _SwFSMoveDestinationDriveID_Type(Integer32):
    """Custom type swFSMoveDestinationDriveID based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_SwFSMoveDestinationDriveID_Type.__name__ = "Integer32"
_SwFSMoveDestinationDriveID_Object = MibScalar
swFSMoveDestinationDriveID = _SwFSMoveDestinationDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6, 3),
    _SwFSMoveDestinationDriveID_Type()
)
swFSMoveDestinationDriveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSMoveDestinationDriveID.setStatus("current")


class _SwFSMoveDestinationName_Type(DisplayString):
    """Custom type swFSMoveDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFSMoveDestinationName_Type.__name__ = "DisplayString"
_SwFSMoveDestinationName_Object = MibScalar
swFSMoveDestinationName = _SwFSMoveDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6, 4),
    _SwFSMoveDestinationName_Type()
)
swFSMoveDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSMoveDestinationName.setStatus("current")


class _SwFSMoveActivity_Type(Integer32):
    """Custom type swFSMoveActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwFSMoveActivity_Type.__name__ = "Integer32"
_SwFSMoveActivity_Object = MibScalar
swFSMoveActivity = _SwFSMoveActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 14, 6, 5),
    _SwFSMoveActivity_Type()
)
swFSMoveActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFSMoveActivity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FILE-SYSTEM-MIB",
    **{"swFileSystemMIB": swFileSystemMIB,
       "swFSBasicInfo": swFSBasicInfo,
       "swFSBasicInfoCtrlStatus": swFSBasicInfoCtrlStatus,
       "swFSBasicInfoCtrlProcess": swFSBasicInfoCtrlProcess,
       "swFSDriveCtrl": swFSDriveCtrl,
       "swFSDriveInfoTable": swFSDriveInfoTable,
       "swFSDriveInfoEntry": swFSDriveInfoEntry,
       "swFSDriveInfoIndex": swFSDriveInfoIndex,
       "swFSDriveInfoDriveID": swFSDriveInfoDriveID,
       "swFSDriveInfoType": swFSDriveInfoType,
       "swFSDriveInfoSize": swFSDriveInfoSize,
       "swFSDriveInfoPartition": swFSDriveInfoPartition,
       "swFSDriveInfoFStype": swFSDriveInfoFStype,
       "swFSDriveFormatCtrl": swFSDriveFormatCtrl,
       "swFSDriveFormatDriveID": swFSDriveFormatDriveID,
       "swFSDriveFormatFat": swFSDriveFormatFat,
       "swFSDriveFormatLabelName": swFSDriveFormatLabelName,
       "swFSDriveFormatType": swFSDriveFormatType,
       "swFSDriveFormatActivity": swFSDriveFormatActivity,
       "swFSDriveChangeCtrl": swFSDriveChangeCtrl,
       "swFSDriveChangeUnitID": swFSDriveChangeUnitID,
       "swFSDriveChangeDriveID": swFSDriveChangeDriveID,
       "swFSDriveCurrentDirectory": swFSDriveCurrentDirectory,
       "swFSDriveInfoStackTable": swFSDriveInfoStackTable,
       "swFSDriveInfoStackEntry": swFSDriveInfoStackEntry,
       "swFSDriveInfoStackUnitID": swFSDriveInfoStackUnitID,
       "swFSDriveInfoStackIndex": swFSDriveInfoStackIndex,
       "swFSDriveInfoStackDriveID": swFSDriveInfoStackDriveID,
       "swFSDriveInfoStackType": swFSDriveInfoStackType,
       "swFSDriveInfoStackSize": swFSDriveInfoStackSize,
       "swFSDriveInfoStackPartition": swFSDriveInfoStackPartition,
       "swFSDriveInfoStackFStype": swFSDriveInfoStackFStype,
       "swFSDirectoryCtrl": swFSDirectoryCtrl,
       "swFSDirectoryMake": swFSDirectoryMake,
       "swFSDirectoryDel": swFSDirectoryDel,
       "swFSctrlDirectoryDir": swFSctrlDirectoryDir,
       "swFSDirectoryPath": swFSDirectoryPath,
       "swFSDirectoryTable": swFSDirectoryTable,
       "swFSDirectoryEntry": swFSDirectoryEntry,
       "swFSDirectoryName": swFSDirectoryName,
       "swFSDirectoryAttr": swFSDirectoryAttr,
       "swFSDirectoryTime": swFSDirectoryTime,
       "swFSDirectorySize": swFSDirectorySize,
       "swFSFileCtrl": swFSFileCtrl,
       "swFSFileRename": swFSFileRename,
       "swFSFileSourceName": swFSFileSourceName,
       "swFSFileTargetName": swFSFileTargetName,
       "swFSFileRenameActivity": swFSFileRenameActivity,
       "swFSFileDel": swFSFileDel,
       "swFSFileDelName": swFSFileDelName,
       "swFSFileDelOption": swFSFileDelOption,
       "swFSFileDelActivity": swFSFileDelActivity,
       "swFSCopyCtrl": swFSCopyCtrl,
       "swFSCopySourceName": swFSCopySourceName,
       "swFSCopyDestinationName": swFSCopyDestinationName,
       "swFSCopyActivity": swFSCopyActivity,
       "swFSCopyDestinationUnitID": swFSCopyDestinationUnitID,
       "swFSCopyDestinationDriveID": swFSCopyDestinationDriveID,
       "swFSCopyConfigID": swFSCopyConfigID,
       "swFSCopyImageID": swFSCopyImageID,
       "swFSMoveCtrl": swFSMoveCtrl,
       "swFSMoveSourceName": swFSMoveSourceName,
       "swFSMoveDestinationUnitID": swFSMoveDestinationUnitID,
       "swFSMoveDestinationDriveID": swFSMoveDestinationDriveID,
       "swFSMoveDestinationName": swFSMoveDestinationName,
       "swFSMoveActivity": swFSMoveActivity}
)
