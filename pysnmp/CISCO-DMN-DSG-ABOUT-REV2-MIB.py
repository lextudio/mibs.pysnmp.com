# SNMP MIB module (CISCO-DMN-DSG-ABOUT-REV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-ABOUT-REV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:15 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGAboutRev2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42)
)
ciscoDSGAboutRev2.setRevisions(
        ("2013-05-15 06:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AboutRev2Table_ObjectIdentity = ObjectIdentity
aboutRev2Table = _AboutRev2Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2)
)
_PcbVersionTable_Object = MibTable
pcbVersionTable = _PcbVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1)
)
if mibBuilder.loadTexts:
    pcbVersionTable.setStatus("current")
_PcbVersionEntry_Object = MibTableRow
pcbVersionEntry = _PcbVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1)
)
pcbVersionEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "pcbVersionIdx"),
)
if mibBuilder.loadTexts:
    pcbVersionEntry.setStatus("current")


class _PcbVersionIdx_Type(Integer32):
    """Custom type pcbVersionIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcbVersionIdx_Type.__name__ = "Integer32"
_PcbVersionIdx_Object = MibTableColumn
pcbVersionIdx = _PcbVersionIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 1),
    _PcbVersionIdx_Type()
)
pcbVersionIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionIdx.setStatus("current")


class _PcbVersionPosition_Type(Integer32):
    """Custom type pcbVersionPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcbVersionPosition_Type.__name__ = "Integer32"
_PcbVersionPosition_Object = MibTableColumn
pcbVersionPosition = _PcbVersionPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 2),
    _PcbVersionPosition_Type()
)
pcbVersionPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionPosition.setStatus("current")


class _PcbVersionID_Type(DisplayString):
    """Custom type pcbVersionID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcbVersionID_Type.__name__ = "DisplayString"
_PcbVersionID_Object = MibTableColumn
pcbVersionID = _PcbVersionID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 3),
    _PcbVersionID_Type()
)
pcbVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionID.setStatus("current")


class _PcbVersionRev_Type(DisplayString):
    """Custom type pcbVersionRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcbVersionRev_Type.__name__ = "DisplayString"
_PcbVersionRev_Object = MibTableColumn
pcbVersionRev = _PcbVersionRev_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 4),
    _PcbVersionRev_Type()
)
pcbVersionRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionRev.setStatus("current")


class _PcbVersionOptions_Type(DisplayString):
    """Custom type pcbVersionOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcbVersionOptions_Type.__name__ = "DisplayString"
_PcbVersionOptions_Object = MibTableColumn
pcbVersionOptions = _PcbVersionOptions_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 5),
    _PcbVersionOptions_Type()
)
pcbVersionOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionOptions.setStatus("current")


class _PcbVersionSerialNum_Type(DisplayString):
    """Custom type pcbVersionSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcbVersionSerialNum_Type.__name__ = "DisplayString"
_PcbVersionSerialNum_Object = MibTableColumn
pcbVersionSerialNum = _PcbVersionSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 1, 1, 6),
    _PcbVersionSerialNum_Type()
)
pcbVersionSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbVersionSerialNum.setStatus("current")
_FirmwareVersionTable_Object = MibTable
firmwareVersionTable = _FirmwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2)
)
if mibBuilder.loadTexts:
    firmwareVersionTable.setStatus("current")
_FirmwareVersionEntry_Object = MibTableRow
firmwareVersionEntry = _FirmwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1)
)
firmwareVersionEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "firmwareVersionBoard"),
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "firmwareVersionrow"),
)
if mibBuilder.loadTexts:
    firmwareVersionEntry.setStatus("current")


class _FirmwareVersionBoard_Type(Integer32):
    """Custom type firmwareVersionBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FirmwareVersionBoard_Type.__name__ = "Integer32"
_FirmwareVersionBoard_Object = MibTableColumn
firmwareVersionBoard = _FirmwareVersionBoard_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1, 1),
    _FirmwareVersionBoard_Type()
)
firmwareVersionBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionBoard.setStatus("current")


class _FirmwareVersionrow_Type(Integer32):
    """Custom type firmwareVersionrow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FirmwareVersionrow_Type.__name__ = "Integer32"
_FirmwareVersionrow_Object = MibTableColumn
firmwareVersionrow = _FirmwareVersionrow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1, 2),
    _FirmwareVersionrow_Type()
)
firmwareVersionrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionrow.setStatus("current")


class _FirmwareVersionID_Type(DisplayString):
    """Custom type firmwareVersionID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirmwareVersionID_Type.__name__ = "DisplayString"
_FirmwareVersionID_Object = MibTableColumn
firmwareVersionID = _FirmwareVersionID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1, 3),
    _FirmwareVersionID_Type()
)
firmwareVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionID.setStatus("current")


class _FirmwareVersionVersion_Type(DisplayString):
    """Custom type firmwareVersionVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirmwareVersionVersion_Type.__name__ = "DisplayString"
_FirmwareVersionVersion_Object = MibTableColumn
firmwareVersionVersion = _FirmwareVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1, 4),
    _FirmwareVersionVersion_Type()
)
firmwareVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionVersion.setStatus("current")


class _FirmwareVersionValidationCode_Type(Integer32):
    """Custom type firmwareVersionValidationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FirmwareVersionValidationCode_Type.__name__ = "Integer32"
_FirmwareVersionValidationCode_Object = MibTableColumn
firmwareVersionValidationCode = _FirmwareVersionValidationCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 2, 1, 5),
    _FirmwareVersionValidationCode_Type()
)
firmwareVersionValidationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionValidationCode.setStatus("current")
_CurrentAppTable_Object = MibTable
currentAppTable = _CurrentAppTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3)
)
if mibBuilder.loadTexts:
    currentAppTable.setStatus("current")
_CurrentAppEntry_Object = MibTableRow
currentAppEntry = _CurrentAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1)
)
currentAppEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "currentAppBoard"),
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "currentApprow"),
)
if mibBuilder.loadTexts:
    currentAppEntry.setStatus("current")


class _CurrentAppBoard_Type(Integer32):
    """Custom type currentAppBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentAppBoard_Type.__name__ = "Integer32"
_CurrentAppBoard_Object = MibTableColumn
currentAppBoard = _CurrentAppBoard_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1, 1),
    _CurrentAppBoard_Type()
)
currentAppBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAppBoard.setStatus("current")


class _CurrentApprow_Type(Integer32):
    """Custom type currentApprow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentApprow_Type.__name__ = "Integer32"
_CurrentApprow_Object = MibTableColumn
currentApprow = _CurrentApprow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1, 2),
    _CurrentApprow_Type()
)
currentApprow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentApprow.setStatus("current")


class _CurrentAppID_Type(DisplayString):
    """Custom type currentAppID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CurrentAppID_Type.__name__ = "DisplayString"
_CurrentAppID_Object = MibTableColumn
currentAppID = _CurrentAppID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1, 3),
    _CurrentAppID_Type()
)
currentAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAppID.setStatus("current")


class _CurrentAppVersion_Type(DisplayString):
    """Custom type currentAppVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CurrentAppVersion_Type.__name__ = "DisplayString"
_CurrentAppVersion_Object = MibTableColumn
currentAppVersion = _CurrentAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1, 4),
    _CurrentAppVersion_Type()
)
currentAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAppVersion.setStatus("current")


class _CurrentAppValidationCode_Type(Integer32):
    """Custom type currentAppValidationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentAppValidationCode_Type.__name__ = "Integer32"
_CurrentAppValidationCode_Object = MibTableColumn
currentAppValidationCode = _CurrentAppValidationCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 3, 1, 5),
    _CurrentAppValidationCode_Type()
)
currentAppValidationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAppValidationCode.setStatus("current")
_CurrentFpgaTable_Object = MibTable
currentFpgaTable = _CurrentFpgaTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4)
)
if mibBuilder.loadTexts:
    currentFpgaTable.setStatus("current")
_CurrentFpgaEntry_Object = MibTableRow
currentFpgaEntry = _CurrentFpgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1)
)
currentFpgaEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "currentFpgaBoard"),
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "currentFpgarow"),
)
if mibBuilder.loadTexts:
    currentFpgaEntry.setStatus("current")


class _CurrentFpgaBoard_Type(Integer32):
    """Custom type currentFpgaBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentFpgaBoard_Type.__name__ = "Integer32"
_CurrentFpgaBoard_Object = MibTableColumn
currentFpgaBoard = _CurrentFpgaBoard_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1, 1),
    _CurrentFpgaBoard_Type()
)
currentFpgaBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFpgaBoard.setStatus("current")


class _CurrentFpgarow_Type(Integer32):
    """Custom type currentFpgarow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentFpgarow_Type.__name__ = "Integer32"
_CurrentFpgarow_Object = MibTableColumn
currentFpgarow = _CurrentFpgarow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1, 2),
    _CurrentFpgarow_Type()
)
currentFpgarow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFpgarow.setStatus("current")


class _CurrentFpgaID_Type(DisplayString):
    """Custom type currentFpgaID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CurrentFpgaID_Type.__name__ = "DisplayString"
_CurrentFpgaID_Object = MibTableColumn
currentFpgaID = _CurrentFpgaID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1, 3),
    _CurrentFpgaID_Type()
)
currentFpgaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFpgaID.setStatus("current")


class _CurrentFpgaVersion_Type(DisplayString):
    """Custom type currentFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CurrentFpgaVersion_Type.__name__ = "DisplayString"
_CurrentFpgaVersion_Object = MibTableColumn
currentFpgaVersion = _CurrentFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1, 4),
    _CurrentFpgaVersion_Type()
)
currentFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFpgaVersion.setStatus("current")


class _CurrentFpgaValidationCode_Type(Integer32):
    """Custom type currentFpgaValidationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentFpgaValidationCode_Type.__name__ = "Integer32"
_CurrentFpgaValidationCode_Object = MibTableColumn
currentFpgaValidationCode = _CurrentFpgaValidationCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 4, 1, 5),
    _CurrentFpgaValidationCode_Type()
)
currentFpgaValidationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFpgaValidationCode.setStatus("current")
_RunnableAppTable_Object = MibTable
runnableAppTable = _RunnableAppTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5)
)
if mibBuilder.loadTexts:
    runnableAppTable.setStatus("current")
_RunnableAppEntry_Object = MibTableRow
runnableAppEntry = _RunnableAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1)
)
runnableAppEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "runnableAppIdx"),
)
if mibBuilder.loadTexts:
    runnableAppEntry.setStatus("current")


class _RunnableAppIdx_Type(Integer32):
    """Custom type runnableAppIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableAppIdx_Type.__name__ = "Integer32"
_RunnableAppIdx_Object = MibTableColumn
runnableAppIdx = _RunnableAppIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1, 1),
    _RunnableAppIdx_Type()
)
runnableAppIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableAppIdx.setStatus("current")


class _RunnableAppFileIdx_Type(Integer32):
    """Custom type runnableAppFileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableAppFileIdx_Type.__name__ = "Integer32"
_RunnableAppFileIdx_Object = MibTableColumn
runnableAppFileIdx = _RunnableAppFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1, 2),
    _RunnableAppFileIdx_Type()
)
runnableAppFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableAppFileIdx.setStatus("current")


class _RunnableAppVersion_Type(DisplayString):
    """Custom type runnableAppVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RunnableAppVersion_Type.__name__ = "DisplayString"
_RunnableAppVersion_Object = MibTableColumn
runnableAppVersion = _RunnableAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1, 3),
    _RunnableAppVersion_Type()
)
runnableAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableAppVersion.setStatus("current")


class _RunnableAppSelect_Type(Integer32):
    """Custom type runnableAppSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableAppSelect_Type.__name__ = "Integer32"
_RunnableAppSelect_Object = MibTableColumn
runnableAppSelect = _RunnableAppSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1, 4),
    _RunnableAppSelect_Type()
)
runnableAppSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableAppSelect.setStatus("current")


class _RunnableAppErase_Type(Integer32):
    """Custom type runnableAppErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableAppErase_Type.__name__ = "Integer32"
_RunnableAppErase_Object = MibTableColumn
runnableAppErase = _RunnableAppErase_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 5, 1, 5),
    _RunnableAppErase_Type()
)
runnableAppErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableAppErase.setStatus("current")
_RunnableFpgaTable_Object = MibTable
runnableFpgaTable = _RunnableFpgaTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6)
)
if mibBuilder.loadTexts:
    runnableFpgaTable.setStatus("current")
_RunnableFpgaEntry_Object = MibTableRow
runnableFpgaEntry = _RunnableFpgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1)
)
runnableFpgaEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "runnableFpgaIdx"),
)
if mibBuilder.loadTexts:
    runnableFpgaEntry.setStatus("current")


class _RunnableFpgaIdx_Type(Integer32):
    """Custom type runnableFpgaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableFpgaIdx_Type.__name__ = "Integer32"
_RunnableFpgaIdx_Object = MibTableColumn
runnableFpgaIdx = _RunnableFpgaIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1, 1),
    _RunnableFpgaIdx_Type()
)
runnableFpgaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFpgaIdx.setStatus("current")


class _RunnableFpgaFileIdx_Type(Integer32):
    """Custom type runnableFpgaFileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableFpgaFileIdx_Type.__name__ = "Integer32"
_RunnableFpgaFileIdx_Object = MibTableColumn
runnableFpgaFileIdx = _RunnableFpgaFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1, 2),
    _RunnableFpgaFileIdx_Type()
)
runnableFpgaFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFpgaFileIdx.setStatus("current")


class _RunnableFpgaVersion_Type(DisplayString):
    """Custom type runnableFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RunnableFpgaVersion_Type.__name__ = "DisplayString"
_RunnableFpgaVersion_Object = MibTableColumn
runnableFpgaVersion = _RunnableFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1, 3),
    _RunnableFpgaVersion_Type()
)
runnableFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFpgaVersion.setStatus("current")


class _RunnableFpgaSelect_Type(Integer32):
    """Custom type runnableFpgaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableFpgaSelect_Type.__name__ = "Integer32"
_RunnableFpgaSelect_Object = MibTableColumn
runnableFpgaSelect = _RunnableFpgaSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1, 4),
    _RunnableFpgaSelect_Type()
)
runnableFpgaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableFpgaSelect.setStatus("current")


class _RunnableFpgaErase_Type(Integer32):
    """Custom type runnableFpgaErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableFpgaErase_Type.__name__ = "Integer32"
_RunnableFpgaErase_Object = MibTableColumn
runnableFpgaErase = _RunnableFpgaErase_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 6, 1, 5),
    _RunnableFpgaErase_Type()
)
runnableFpgaErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableFpgaErase.setStatus("current")
_RunnableFecFpgaTable_Object = MibTable
runnableFecFpgaTable = _RunnableFecFpgaTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7)
)
if mibBuilder.loadTexts:
    runnableFecFpgaTable.setStatus("current")
_RunnableFecFpgaEntry_Object = MibTableRow
runnableFecFpgaEntry = _RunnableFecFpgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1)
)
runnableFecFpgaEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-REV2-MIB", "runnableFecFpgaIdx"),
)
if mibBuilder.loadTexts:
    runnableFecFpgaEntry.setStatus("current")


class _RunnableFecFpgaIdx_Type(Integer32):
    """Custom type runnableFecFpgaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableFecFpgaIdx_Type.__name__ = "Integer32"
_RunnableFecFpgaIdx_Object = MibTableColumn
runnableFecFpgaIdx = _RunnableFecFpgaIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1, 1),
    _RunnableFecFpgaIdx_Type()
)
runnableFecFpgaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFecFpgaIdx.setStatus("current")


class _RunnableFecFpgaFileIdx_Type(Integer32):
    """Custom type runnableFecFpgaFileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RunnableFecFpgaFileIdx_Type.__name__ = "Integer32"
_RunnableFecFpgaFileIdx_Object = MibTableColumn
runnableFecFpgaFileIdx = _RunnableFecFpgaFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1, 2),
    _RunnableFecFpgaFileIdx_Type()
)
runnableFecFpgaFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFecFpgaFileIdx.setStatus("current")


class _RunnableFecFpgaVersion_Type(DisplayString):
    """Custom type runnableFecFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RunnableFecFpgaVersion_Type.__name__ = "DisplayString"
_RunnableFecFpgaVersion_Object = MibTableColumn
runnableFecFpgaVersion = _RunnableFecFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1, 3),
    _RunnableFecFpgaVersion_Type()
)
runnableFecFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runnableFecFpgaVersion.setStatus("current")


class _RunnableFecFpgaSelect_Type(Integer32):
    """Custom type runnableFecFpgaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableFecFpgaSelect_Type.__name__ = "Integer32"
_RunnableFecFpgaSelect_Object = MibTableColumn
runnableFecFpgaSelect = _RunnableFecFpgaSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1, 4),
    _RunnableFecFpgaSelect_Type()
)
runnableFecFpgaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableFecFpgaSelect.setStatus("current")


class _RunnableFecFpgaErase_Type(Integer32):
    """Custom type runnableFecFpgaErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RunnableFecFpgaErase_Type.__name__ = "Integer32"
_RunnableFecFpgaErase_Object = MibTableColumn
runnableFecFpgaErase = _RunnableFecFpgaErase_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 42, 2, 7, 1, 5),
    _RunnableFecFpgaErase_Type()
)
runnableFecFpgaErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runnableFecFpgaErase.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-ABOUT-REV2-MIB",
    **{"ciscoDSGAboutRev2": ciscoDSGAboutRev2,
       "aboutRev2Table": aboutRev2Table,
       "pcbVersionTable": pcbVersionTable,
       "pcbVersionEntry": pcbVersionEntry,
       "pcbVersionIdx": pcbVersionIdx,
       "pcbVersionPosition": pcbVersionPosition,
       "pcbVersionID": pcbVersionID,
       "pcbVersionRev": pcbVersionRev,
       "pcbVersionOptions": pcbVersionOptions,
       "pcbVersionSerialNum": pcbVersionSerialNum,
       "firmwareVersionTable": firmwareVersionTable,
       "firmwareVersionEntry": firmwareVersionEntry,
       "firmwareVersionBoard": firmwareVersionBoard,
       "firmwareVersionrow": firmwareVersionrow,
       "firmwareVersionID": firmwareVersionID,
       "firmwareVersionVersion": firmwareVersionVersion,
       "firmwareVersionValidationCode": firmwareVersionValidationCode,
       "currentAppTable": currentAppTable,
       "currentAppEntry": currentAppEntry,
       "currentAppBoard": currentAppBoard,
       "currentApprow": currentApprow,
       "currentAppID": currentAppID,
       "currentAppVersion": currentAppVersion,
       "currentAppValidationCode": currentAppValidationCode,
       "currentFpgaTable": currentFpgaTable,
       "currentFpgaEntry": currentFpgaEntry,
       "currentFpgaBoard": currentFpgaBoard,
       "currentFpgarow": currentFpgarow,
       "currentFpgaID": currentFpgaID,
       "currentFpgaVersion": currentFpgaVersion,
       "currentFpgaValidationCode": currentFpgaValidationCode,
       "runnableAppTable": runnableAppTable,
       "runnableAppEntry": runnableAppEntry,
       "runnableAppIdx": runnableAppIdx,
       "runnableAppFileIdx": runnableAppFileIdx,
       "runnableAppVersion": runnableAppVersion,
       "runnableAppSelect": runnableAppSelect,
       "runnableAppErase": runnableAppErase,
       "runnableFpgaTable": runnableFpgaTable,
       "runnableFpgaEntry": runnableFpgaEntry,
       "runnableFpgaIdx": runnableFpgaIdx,
       "runnableFpgaFileIdx": runnableFpgaFileIdx,
       "runnableFpgaVersion": runnableFpgaVersion,
       "runnableFpgaSelect": runnableFpgaSelect,
       "runnableFpgaErase": runnableFpgaErase,
       "runnableFecFpgaTable": runnableFecFpgaTable,
       "runnableFecFpgaEntry": runnableFecFpgaEntry,
       "runnableFecFpgaIdx": runnableFecFpgaIdx,
       "runnableFecFpgaFileIdx": runnableFecFpgaFileIdx,
       "runnableFecFpgaVersion": runnableFecFpgaVersion,
       "runnableFecFpgaSelect": runnableFecFpgaSelect,
       "runnableFecFpgaErase": runnableFecFpgaErase}
)
