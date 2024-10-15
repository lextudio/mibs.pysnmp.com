# SNMP MIB module (CISCO-DMN-DSG-ABOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-ABOUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:14 2024
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

ciscoDSGAbout = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7)
)
ciscoDSGAbout.setRevisions(
        ("2010-08-03 06:00",
         "2010-03-22 05:00",
         "2009-12-20 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AboutTable_ObjectIdentity = ObjectIdentity
aboutTable = _AboutTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2)
)
_BoardTable_Object = MibTable
boardTable = _BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    boardTable.setStatus("current")
_BoardEntry_Object = MibTableRow
boardEntry = _BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1)
)
boardEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-MIB", "boardIdx"),
)
if mibBuilder.loadTexts:
    boardEntry.setStatus("current")


class _BoardIdx_Type(Integer32):
    """Custom type boardIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardIdx_Type.__name__ = "Integer32"
_BoardIdx_Object = MibTableColumn
boardIdx = _BoardIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 1),
    _BoardIdx_Type()
)
boardIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardIdx.setStatus("current")


class _BoardPosition_Type(Integer32):
    """Custom type boardPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardPosition_Type.__name__ = "Integer32"
_BoardPosition_Object = MibTableColumn
boardPosition = _BoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 2),
    _BoardPosition_Type()
)
boardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPosition.setStatus("current")


class _BoardID_Type(DisplayString):
    """Custom type boardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_BoardID_Type.__name__ = "DisplayString"
_BoardID_Object = MibTableColumn
boardID = _BoardID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 3),
    _BoardID_Type()
)
boardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardID.setStatus("current")


class _BoardRev_Type(DisplayString):
    """Custom type boardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_BoardRev_Type.__name__ = "DisplayString"
_BoardRev_Object = MibTableColumn
boardRev = _BoardRev_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 4),
    _BoardRev_Type()
)
boardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRev.setStatus("current")


class _BoardOptionBits_Type(Integer32):
    """Custom type boardOptionBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardOptionBits_Type.__name__ = "Integer32"
_BoardOptionBits_Object = MibTableColumn
boardOptionBits = _BoardOptionBits_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 5),
    _BoardOptionBits_Type()
)
boardOptionBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardOptionBits.setStatus("current")


class _BoardSerialNum_Type(DisplayString):
    """Custom type boardSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_BoardSerialNum_Type.__name__ = "DisplayString"
_BoardSerialNum_Object = MibTableColumn
boardSerialNum = _BoardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 6),
    _BoardSerialNum_Type()
)
boardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerialNum.setStatus("current")
_SwTable_Object = MibTable
swTable = _SwTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3)
)
if mibBuilder.loadTexts:
    swTable.setStatus("current")
_SwEntry_Object = MibTableRow
swEntry = _SwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1)
)
swEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-MIB", "swIdx"),
)
if mibBuilder.loadTexts:
    swEntry.setStatus("current")


class _SwIdx_Type(Integer32):
    """Custom type swIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwIdx_Type.__name__ = "Integer32"
_SwIdx_Object = MibTableColumn
swIdx = _SwIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 1),
    _SwIdx_Type()
)
swIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIdx.setStatus("current")


class _SwBoardIdx_Type(DisplayString):
    """Custom type swBoardIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwBoardIdx_Type.__name__ = "DisplayString"
_SwBoardIdx_Object = MibTableColumn
swBoardIdx = _SwBoardIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 2),
    _SwBoardIdx_Type()
)
swBoardIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardIdx.setStatus("current")


class _SwID_Type(DisplayString):
    """Custom type swID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwID_Type.__name__ = "DisplayString"
_SwID_Object = MibTableColumn
swID = _SwID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 3),
    _SwID_Type()
)
swID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swID.setStatus("current")


class _SwFileIdx_Type(Integer32):
    """Custom type swFileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFileIdx_Type.__name__ = "Integer32"
_SwFileIdx_Object = MibTableColumn
swFileIdx = _SwFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 4),
    _SwFileIdx_Type()
)
swFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFileIdx.setStatus("current")


class _SwVersion_Type(DisplayString):
    """Custom type swVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_SwVersion_Type.__name__ = "DisplayString"
_SwVersion_Object = MibTableColumn
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 5),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")


class _SwValidationCode_Type(DisplayString):
    """Custom type swValidationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_SwValidationCode_Type.__name__ = "DisplayString"
_SwValidationCode_Object = MibTableColumn
swValidationCode = _SwValidationCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 6),
    _SwValidationCode_Type()
)
swValidationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swValidationCode.setStatus("current")


class _SwStatus_Type(Integer32):
    """Custom type swStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("running", 1))
    )


_SwStatus_Type.__name__ = "Integer32"
_SwStatus_Object = MibTableColumn
swStatus = _SwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 7),
    _SwStatus_Type()
)
swStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStatus.setStatus("current")


class _SwCtrl_Type(Integer32):
    """Custom type swCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("none", 1),
          ("select", 2))
    )


_SwCtrl_Type.__name__ = "Integer32"
_SwCtrl_Object = MibTableColumn
swCtrl = _SwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 8),
    _SwCtrl_Type()
)
swCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCtrl.setStatus("current")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareEntry_Object = MibTableRow
firmwareEntry = _FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1)
)
firmwareEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ABOUT-MIB", "firmwareIdx"),
)
if mibBuilder.loadTexts:
    firmwareEntry.setStatus("current")


class _FirmwareIdx_Type(Integer32):
    """Custom type firmwareIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FirmwareIdx_Type.__name__ = "Integer32"
_FirmwareIdx_Object = MibTableColumn
firmwareIdx = _FirmwareIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 1),
    _FirmwareIdx_Type()
)
firmwareIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firmwareIdx.setStatus("current")


class _FirmwareBoardID_Type(DisplayString):
    """Custom type firmwareBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FirmwareBoardID_Type.__name__ = "DisplayString"
_FirmwareBoardID_Object = MibTableColumn
firmwareBoardID = _FirmwareBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 2),
    _FirmwareBoardID_Type()
)
firmwareBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBoardID.setStatus("current")


class _FirmwareID_Type(DisplayString):
    """Custom type firmwareID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FirmwareID_Type.__name__ = "DisplayString"
_FirmwareID_Object = MibTableColumn
firmwareID = _FirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 3),
    _FirmwareID_Type()
)
firmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareID.setStatus("current")


class _FirmwareVersion_Type(DisplayString):
    """Custom type firmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_FirmwareVersion_Type.__name__ = "DisplayString"
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _FirmwareValidationCode_Type(DisplayString):
    """Custom type firmwareValidationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_FirmwareValidationCode_Type.__name__ = "DisplayString"
_FirmwareValidationCode_Object = MibTableColumn
firmwareValidationCode = _FirmwareValidationCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 5),
    _FirmwareValidationCode_Type()
)
firmwareValidationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareValidationCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-ABOUT-MIB",
    **{"ciscoDSGAbout": ciscoDSGAbout,
       "aboutTable": aboutTable,
       "boardTable": boardTable,
       "boardEntry": boardEntry,
       "boardIdx": boardIdx,
       "boardPosition": boardPosition,
       "boardID": boardID,
       "boardRev": boardRev,
       "boardOptionBits": boardOptionBits,
       "boardSerialNum": boardSerialNum,
       "swTable": swTable,
       "swEntry": swEntry,
       "swIdx": swIdx,
       "swBoardIdx": swBoardIdx,
       "swID": swID,
       "swFileIdx": swFileIdx,
       "swVersion": swVersion,
       "swValidationCode": swValidationCode,
       "swStatus": swStatus,
       "swCtrl": swCtrl,
       "firmwareTable": firmwareTable,
       "firmwareEntry": firmwareEntry,
       "firmwareIdx": firmwareIdx,
       "firmwareBoardID": firmwareBoardID,
       "firmwareID": firmwareID,
       "firmwareVersion": firmwareVersion,
       "firmwareValidationCode": firmwareValidationCode}
)
