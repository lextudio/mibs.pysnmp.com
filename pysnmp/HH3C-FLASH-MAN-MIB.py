# SNMP MIB module (HH3C-FLASH-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FLASH-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:25 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hh3cFlash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cFlashOperationStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("opAuthFail", 17),
          ("opDeleteDeviceBusy", 25),
          ("opDeleteFileOpenError", 20),
          ("opDeleteInvalidDevice", 21),
          ("opDeleteInvalidFileName", 24),
          ("opDeleteInvalidFunction", 22),
          ("opDeleteInvalidPath", 27),
          ("opDeleteOperationError", 23),
          ("opDeleteParaError", 26),
          ("opDeviceBusy", 8),
          ("opDeviceError", 10),
          ("opDeviceFull", 12),
          ("opDeviceNotProgrammable", 11),
          ("opDeviceOpenError", 9),
          ("opFileChecksumError", 15),
          ("opFileOpenError", 13),
          ("opFileTransferError", 14),
          ("opInProgress", 1),
          ("opInvalid", 3),
          ("opInvalidDestName", 6),
          ("opInvalidProtocol", 4),
          ("opInvalidServerAddress", 7),
          ("opInvalidSourceName", 5),
          ("opNoMemory", 16),
          ("opSuccess", 2),
          ("opTimeout", 18),
          ("opUnknownFailure", 19))
    )



class Hh3cFlashPartitionUpgradeMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("rxbootFLH", 2),
          ("unknown", 1))
    )



class Hh3cFlashPartitionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 3),
          ("runFromFlash", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cFlashManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cFlashManMIBObjects = _Hh3cFlashManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1)
)
_Hh3cFlashDevice_ObjectIdentity = ObjectIdentity
hh3cFlashDevice = _Hh3cFlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1)
)
_Hh3cFlhSupportNum_Type = Integer32
_Hh3cFlhSupportNum_Object = MibScalar
hh3cFlhSupportNum = _Hh3cFlhSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 1),
    _Hh3cFlhSupportNum_Type()
)
hh3cFlhSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhSupportNum.setStatus("current")
_Hh3cFlashTable_Object = MibTable
hh3cFlashTable = _Hh3cFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFlashTable.setStatus("current")
_Hh3cFlashEntry_Object = MibTableRow
hh3cFlashEntry = _Hh3cFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1)
)
hh3cFlashEntry.setIndexNames(
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlashEntry.setStatus("current")


class _Hh3cFlhIndex_Type(Integer32):
    """Custom type hh3cFlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cFlhIndex_Type.__name__ = "Integer32"
_Hh3cFlhIndex_Object = MibTableColumn
hh3cFlhIndex = _Hh3cFlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 1),
    _Hh3cFlhIndex_Type()
)
hh3cFlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhIndex.setStatus("current")
_Hh3cFlhSize_Type = Integer32
_Hh3cFlhSize_Object = MibTableColumn
hh3cFlhSize = _Hh3cFlhSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 2),
    _Hh3cFlhSize_Type()
)
hh3cFlhSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlhSize.setUnits("bytes")
_Hh3cFlhPos_Type = PhysicalIndex
_Hh3cFlhPos_Object = MibTableColumn
hh3cFlhPos = _Hh3cFlhPos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 3),
    _Hh3cFlhPos_Type()
)
hh3cFlhPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPos.setStatus("current")


class _Hh3cFlhName_Type(DisplayString):
    """Custom type hh3cFlhName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cFlhName_Type.__name__ = "DisplayString"
_Hh3cFlhName_Object = MibTableColumn
hh3cFlhName = _Hh3cFlhName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 4),
    _Hh3cFlhName_Type()
)
hh3cFlhName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhName.setStatus("current")


class _Hh3cFlhChipNum_Type(Integer32):
    """Custom type hh3cFlhChipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cFlhChipNum_Type.__name__ = "Integer32"
_Hh3cFlhChipNum_Object = MibTableColumn
hh3cFlhChipNum = _Hh3cFlhChipNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 5),
    _Hh3cFlhChipNum_Type()
)
hh3cFlhChipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipNum.setStatus("current")


class _Hh3cFlhDescr_Type(DisplayString):
    """Custom type hh3cFlhDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cFlhDescr_Type.__name__ = "DisplayString"
_Hh3cFlhDescr_Object = MibTableColumn
hh3cFlhDescr = _Hh3cFlhDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 6),
    _Hh3cFlhDescr_Type()
)
hh3cFlhDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhDescr.setStatus("current")
_Hh3cFlhInitTime_Type = TimeStamp
_Hh3cFlhInitTime_Object = MibTableColumn
hh3cFlhInitTime = _Hh3cFlhInitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 8),
    _Hh3cFlhInitTime_Type()
)
hh3cFlhInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhInitTime.setStatus("current")
_Hh3cFlhRemovable_Type = TruthValue
_Hh3cFlhRemovable_Object = MibTableColumn
hh3cFlhRemovable = _Hh3cFlhRemovable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 9),
    _Hh3cFlhRemovable_Type()
)
hh3cFlhRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhRemovable.setStatus("current")
_Hh3cFlhPartitionBool_Type = TruthValue
_Hh3cFlhPartitionBool_Object = MibTableColumn
hh3cFlhPartitionBool = _Hh3cFlhPartitionBool_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 11),
    _Hh3cFlhPartitionBool_Type()
)
hh3cFlhPartitionBool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlhPartitionBool.setStatus("current")
_Hh3cFlhMinPartitionSize_Type = Integer32
_Hh3cFlhMinPartitionSize_Object = MibTableColumn
hh3cFlhMinPartitionSize = _Hh3cFlhMinPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 12),
    _Hh3cFlhMinPartitionSize_Type()
)
hh3cFlhMinPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhMinPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlhMinPartitionSize.setUnits("bytes")


class _Hh3cFlhMaxPartitions_Type(Integer32):
    """Custom type hh3cFlhMaxPartitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cFlhMaxPartitions_Type.__name__ = "Integer32"
_Hh3cFlhMaxPartitions_Object = MibTableColumn
hh3cFlhMaxPartitions = _Hh3cFlhMaxPartitions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 13),
    _Hh3cFlhMaxPartitions_Type()
)
hh3cFlhMaxPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhMaxPartitions.setStatus("current")
_Hh3cFlhPartitionNum_Type = Integer32
_Hh3cFlhPartitionNum_Object = MibTableColumn
hh3cFlhPartitionNum = _Hh3cFlhPartitionNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 14),
    _Hh3cFlhPartitionNum_Type()
)
hh3cFlhPartitionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartitionNum.setStatus("current")
_Hh3cFlhKbyteSize_Type = Integer32
_Hh3cFlhKbyteSize_Object = MibTableColumn
hh3cFlhKbyteSize = _Hh3cFlhKbyteSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 15),
    _Hh3cFlhKbyteSize_Type()
)
hh3cFlhKbyteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhKbyteSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlhKbyteSize.setUnits("kbytes")
_Hh3cFlashChips_ObjectIdentity = ObjectIdentity
hh3cFlashChips = _Hh3cFlashChips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3)
)
_Hh3cFlhChipTable_Object = MibTable
hh3cFlhChipTable = _Hh3cFlhChipTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cFlhChipTable.setStatus("current")
_Hh3cFlhChipEntry_Object = MibTableRow
hh3cFlhChipEntry = _Hh3cFlhChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1)
)
hh3cFlhChipEntry.setIndexNames(
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"),
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhChipSerialNo"),
)
if mibBuilder.loadTexts:
    hh3cFlhChipEntry.setStatus("current")


class _Hh3cFlhChipSerialNo_Type(Integer32):
    """Custom type hh3cFlhChipSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cFlhChipSerialNo_Type.__name__ = "Integer32"
_Hh3cFlhChipSerialNo_Object = MibTableColumn
hh3cFlhChipSerialNo = _Hh3cFlhChipSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 1),
    _Hh3cFlhChipSerialNo_Type()
)
hh3cFlhChipSerialNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFlhChipSerialNo.setStatus("current")


class _Hh3cFlhChipID_Type(DisplayString):
    """Custom type hh3cFlhChipID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Hh3cFlhChipID_Type.__name__ = "DisplayString"
_Hh3cFlhChipID_Object = MibTableColumn
hh3cFlhChipID = _Hh3cFlhChipID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 2),
    _Hh3cFlhChipID_Type()
)
hh3cFlhChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipID.setStatus("current")


class _Hh3cFlhChipDescr_Type(DisplayString):
    """Custom type hh3cFlhChipDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cFlhChipDescr_Type.__name__ = "DisplayString"
_Hh3cFlhChipDescr_Object = MibTableColumn
hh3cFlhChipDescr = _Hh3cFlhChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 3),
    _Hh3cFlhChipDescr_Type()
)
hh3cFlhChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipDescr.setStatus("current")
_Hh3cFlhChipWriteTimesLimit_Type = Integer32
_Hh3cFlhChipWriteTimesLimit_Object = MibTableColumn
hh3cFlhChipWriteTimesLimit = _Hh3cFlhChipWriteTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 4),
    _Hh3cFlhChipWriteTimesLimit_Type()
)
hh3cFlhChipWriteTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipWriteTimesLimit.setStatus("current")
_Hh3cFlhChipWriteTimes_Type = Counter32
_Hh3cFlhChipWriteTimes_Object = MibTableColumn
hh3cFlhChipWriteTimes = _Hh3cFlhChipWriteTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 5),
    _Hh3cFlhChipWriteTimes_Type()
)
hh3cFlhChipWriteTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipWriteTimes.setStatus("current")
_Hh3cFlhChipEraseTimesLimit_Type = Integer32
_Hh3cFlhChipEraseTimesLimit_Object = MibTableColumn
hh3cFlhChipEraseTimesLimit = _Hh3cFlhChipEraseTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 6),
    _Hh3cFlhChipEraseTimesLimit_Type()
)
hh3cFlhChipEraseTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipEraseTimesLimit.setStatus("current")
_Hh3cFlhChipEraseTimes_Type = Counter32
_Hh3cFlhChipEraseTimes_Object = MibTableColumn
hh3cFlhChipEraseTimes = _Hh3cFlhChipEraseTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 7),
    _Hh3cFlhChipEraseTimes_Type()
)
hh3cFlhChipEraseTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhChipEraseTimes.setStatus("current")
_Hh3cFlashPartitions_ObjectIdentity = ObjectIdentity
hh3cFlashPartitions = _Hh3cFlashPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4)
)
_Hh3cFlhPartitionTable_Object = MibTable
hh3cFlhPartitionTable = _Hh3cFlhPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cFlhPartitionTable.setStatus("current")
_Hh3cFlhPartitionEntry_Object = MibTableRow
hh3cFlhPartitionEntry = _Hh3cFlhPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1)
)
hh3cFlhPartitionEntry.setIndexNames(
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"),
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhPartIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlhPartitionEntry.setStatus("current")


class _Hh3cFlhPartIndex_Type(Integer32):
    """Custom type hh3cFlhPartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cFlhPartIndex_Type.__name__ = "Integer32"
_Hh3cFlhPartIndex_Object = MibTableColumn
hh3cFlhPartIndex = _Hh3cFlhPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 1),
    _Hh3cFlhPartIndex_Type()
)
hh3cFlhPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFlhPartIndex.setStatus("current")


class _Hh3cFlhPartFirstChip_Type(Integer32):
    """Custom type hh3cFlhPartFirstChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cFlhPartFirstChip_Type.__name__ = "Integer32"
_Hh3cFlhPartFirstChip_Object = MibTableColumn
hh3cFlhPartFirstChip = _Hh3cFlhPartFirstChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 2),
    _Hh3cFlhPartFirstChip_Type()
)
hh3cFlhPartFirstChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartFirstChip.setStatus("current")


class _Hh3cFlhPartLastChip_Type(Integer32):
    """Custom type hh3cFlhPartLastChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cFlhPartLastChip_Type.__name__ = "Integer32"
_Hh3cFlhPartLastChip_Object = MibTableColumn
hh3cFlhPartLastChip = _Hh3cFlhPartLastChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 3),
    _Hh3cFlhPartLastChip_Type()
)
hh3cFlhPartLastChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartLastChip.setStatus("current")
_Hh3cFlhPartSpace_Type = Integer32
_Hh3cFlhPartSpace_Object = MibTableColumn
hh3cFlhPartSpace = _Hh3cFlhPartSpace_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 4),
    _Hh3cFlhPartSpace_Type()
)
hh3cFlhPartSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartSpace.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlhPartSpace.setUnits("bytes")
_Hh3cFlhPartSpaceFree_Type = Gauge32
_Hh3cFlhPartSpaceFree_Object = MibTableColumn
hh3cFlhPartSpaceFree = _Hh3cFlhPartSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 5),
    _Hh3cFlhPartSpaceFree_Type()
)
hh3cFlhPartSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlhPartSpaceFree.setUnits("bytes")
_Hh3cFlhPartFileNum_Type = Integer32
_Hh3cFlhPartFileNum_Object = MibTableColumn
hh3cFlhPartFileNum = _Hh3cFlhPartFileNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 6),
    _Hh3cFlhPartFileNum_Type()
)
hh3cFlhPartFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartFileNum.setStatus("current")


class _Hh3cFlhPartChecksumMethod_Type(Integer32):
    """Custom type hh3cFlhPartChecksumMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("simpleCRC", 3),
          ("simpleChecksum", 1),
          ("undefined", 2))
    )


_Hh3cFlhPartChecksumMethod_Type.__name__ = "Integer32"
_Hh3cFlhPartChecksumMethod_Object = MibTableColumn
hh3cFlhPartChecksumMethod = _Hh3cFlhPartChecksumMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 7),
    _Hh3cFlhPartChecksumMethod_Type()
)
hh3cFlhPartChecksumMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartChecksumMethod.setStatus("current")
_Hh3cFlhPartStatus_Type = Hh3cFlashPartitionStatus
_Hh3cFlhPartStatus_Object = MibTableColumn
hh3cFlhPartStatus = _Hh3cFlhPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 8),
    _Hh3cFlhPartStatus_Type()
)
hh3cFlhPartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartStatus.setStatus("current")
_Hh3cFlhPartUpgradeMode_Type = Hh3cFlashPartitionUpgradeMode
_Hh3cFlhPartUpgradeMode_Object = MibTableColumn
hh3cFlhPartUpgradeMode = _Hh3cFlhPartUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 9),
    _Hh3cFlhPartUpgradeMode_Type()
)
hh3cFlhPartUpgradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartUpgradeMode.setStatus("current")


class _Hh3cFlhPartName_Type(DisplayString):
    """Custom type hh3cFlhPartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cFlhPartName_Type.__name__ = "DisplayString"
_Hh3cFlhPartName_Object = MibTableColumn
hh3cFlhPartName = _Hh3cFlhPartName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 10),
    _Hh3cFlhPartName_Type()
)
hh3cFlhPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartName.setStatus("current")
_Hh3cFlhPartRequireErase_Type = TruthValue
_Hh3cFlhPartRequireErase_Object = MibTableColumn
hh3cFlhPartRequireErase = _Hh3cFlhPartRequireErase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 11),
    _Hh3cFlhPartRequireErase_Type()
)
hh3cFlhPartRequireErase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartRequireErase.setStatus("current")


class _Hh3cFlhPartFileNameLen_Type(Integer32):
    """Custom type hh3cFlhPartFileNameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cFlhPartFileNameLen_Type.__name__ = "Integer32"
_Hh3cFlhPartFileNameLen_Object = MibTableColumn
hh3cFlhPartFileNameLen = _Hh3cFlhPartFileNameLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 12),
    _Hh3cFlhPartFileNameLen_Type()
)
hh3cFlhPartFileNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhPartFileNameLen.setStatus("current")
_Hh3cFlhFiles_ObjectIdentity = ObjectIdentity
hh3cFlhFiles = _Hh3cFlhFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2)
)
_Hh3cFlhFileTable_Object = MibTable
hh3cFlhFileTable = _Hh3cFlhFileTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFlhFileTable.setStatus("current")
_Hh3cFlhFileEntry_Object = MibTableRow
hh3cFlhFileEntry = _Hh3cFlhFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1)
)
hh3cFlhFileEntry.setIndexNames(
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"),
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhPartIndex"),
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhFileIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlhFileEntry.setStatus("current")


class _Hh3cFlhFileIndex_Type(Integer32):
    """Custom type hh3cFlhFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cFlhFileIndex_Type.__name__ = "Integer32"
_Hh3cFlhFileIndex_Object = MibTableColumn
hh3cFlhFileIndex = _Hh3cFlhFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 1),
    _Hh3cFlhFileIndex_Type()
)
hh3cFlhFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFlhFileIndex.setStatus("current")


class _Hh3cFlhFileName_Type(DisplayString):
    """Custom type hh3cFlhFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cFlhFileName_Type.__name__ = "DisplayString"
_Hh3cFlhFileName_Object = MibTableColumn
hh3cFlhFileName = _Hh3cFlhFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 2),
    _Hh3cFlhFileName_Type()
)
hh3cFlhFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhFileName.setStatus("current")
_Hh3cFlhFileSize_Type = Integer32
_Hh3cFlhFileSize_Object = MibTableColumn
hh3cFlhFileSize = _Hh3cFlhFileSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 3),
    _Hh3cFlhFileSize_Type()
)
hh3cFlhFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhFileSize.setStatus("current")


class _Hh3cFlhFileStatus_Type(Integer32):
    """Custom type hh3cFlhFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("invalidChecksum", 2),
          ("valid", 3))
    )


_Hh3cFlhFileStatus_Type.__name__ = "Integer32"
_Hh3cFlhFileStatus_Object = MibTableColumn
hh3cFlhFileStatus = _Hh3cFlhFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 4),
    _Hh3cFlhFileStatus_Type()
)
hh3cFlhFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhFileStatus.setStatus("current")
_Hh3cFlhFileChecksum_Type = OctetString
_Hh3cFlhFileChecksum_Object = MibTableColumn
hh3cFlhFileChecksum = _Hh3cFlhFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 5),
    _Hh3cFlhFileChecksum_Type()
)
hh3cFlhFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhFileChecksum.setStatus("current")
_Hh3cFlashOperate_ObjectIdentity = ObjectIdentity
hh3cFlashOperate = _Hh3cFlashOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2)
)
_Hh3cFlhOpTable_Object = MibTable
hh3cFlhOpTable = _Hh3cFlhOpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFlhOpTable.setStatus("current")
_Hh3cFlhOpEntry_Object = MibTableRow
hh3cFlhOpEntry = _Hh3cFlhOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1)
)
hh3cFlhOpEntry.setIndexNames(
    (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhOperIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlhOpEntry.setStatus("current")


class _Hh3cFlhOperIndex_Type(Integer32):
    """Custom type hh3cFlhOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cFlhOperIndex_Type.__name__ = "Integer32"
_Hh3cFlhOperIndex_Object = MibTableColumn
hh3cFlhOperIndex = _Hh3cFlhOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 1),
    _Hh3cFlhOperIndex_Type()
)
hh3cFlhOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFlhOperIndex.setStatus("current")


class _Hh3cFlhOperType_Type(Integer32):
    """Custom type hh3cFlhOperType based on Integer32"""
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
        *(("delete", 4),
          ("flash2Net", 3),
          ("net2FlashWithErase", 1),
          ("net2FlashWithoutErase", 2),
          ("rename", 5))
    )


_Hh3cFlhOperType_Type.__name__ = "Integer32"
_Hh3cFlhOperType_Object = MibTableColumn
hh3cFlhOperType = _Hh3cFlhOperType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 2),
    _Hh3cFlhOperType_Type()
)
hh3cFlhOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperType.setStatus("current")


class _Hh3cFlhOperProtocol_Type(Integer32):
    """Custom type hh3cFlhOperProtocol based on Integer32"""
    defaultValue = 1

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
        *(("clusterftp", 3),
          ("clustertftp", 4),
          ("ftp", 1),
          ("tftp", 2))
    )


_Hh3cFlhOperProtocol_Type.__name__ = "Integer32"
_Hh3cFlhOperProtocol_Object = MibTableColumn
hh3cFlhOperProtocol = _Hh3cFlhOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 3),
    _Hh3cFlhOperProtocol_Type()
)
hh3cFlhOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperProtocol.setStatus("current")


class _Hh3cFlhOperServerAddress_Type(IpAddress):
    """Custom type hh3cFlhOperServerAddress based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Hh3cFlhOperServerAddress_Object = MibTableColumn
hh3cFlhOperServerAddress = _Hh3cFlhOperServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 4),
    _Hh3cFlhOperServerAddress_Type()
)
hh3cFlhOperServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperServerAddress.setStatus("current")
_Hh3cFlhOperServerUser_Type = DisplayString
_Hh3cFlhOperServerUser_Object = MibTableColumn
hh3cFlhOperServerUser = _Hh3cFlhOperServerUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 5),
    _Hh3cFlhOperServerUser_Type()
)
hh3cFlhOperServerUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperServerUser.setStatus("current")
_Hh3cFlhOperPassword_Type = DisplayString
_Hh3cFlhOperPassword_Object = MibTableColumn
hh3cFlhOperPassword = _Hh3cFlhOperPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 6),
    _Hh3cFlhOperPassword_Type()
)
hh3cFlhOperPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperPassword.setStatus("current")


class _Hh3cFlhOperSourceFile_Type(DisplayString):
    """Custom type hh3cFlhOperSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cFlhOperSourceFile_Type.__name__ = "DisplayString"
_Hh3cFlhOperSourceFile_Object = MibTableColumn
hh3cFlhOperSourceFile = _Hh3cFlhOperSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 7),
    _Hh3cFlhOperSourceFile_Type()
)
hh3cFlhOperSourceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperSourceFile.setStatus("current")
_Hh3cFlhOperDestinationFile_Type = DisplayString
_Hh3cFlhOperDestinationFile_Object = MibTableColumn
hh3cFlhOperDestinationFile = _Hh3cFlhOperDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 8),
    _Hh3cFlhOperDestinationFile_Type()
)
hh3cFlhOperDestinationFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperDestinationFile.setStatus("current")
_Hh3cFlhOperStatus_Type = Hh3cFlashOperationStatus
_Hh3cFlhOperStatus_Object = MibTableColumn
hh3cFlhOperStatus = _Hh3cFlhOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 9),
    _Hh3cFlhOperStatus_Type()
)
hh3cFlhOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhOperStatus.setStatus("current")


class _Hh3cFlhOperEndNotification_Type(TruthValue):
    """Custom type hh3cFlhOperEndNotification based on TruthValue"""


_Hh3cFlhOperEndNotification_Object = MibTableColumn
hh3cFlhOperEndNotification = _Hh3cFlhOperEndNotification_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 10),
    _Hh3cFlhOperEndNotification_Type()
)
hh3cFlhOperEndNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperEndNotification.setStatus("current")
_Hh3cFlhOperProgress_Type = TimeTicks
_Hh3cFlhOperProgress_Object = MibTableColumn
hh3cFlhOperProgress = _Hh3cFlhOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 11),
    _Hh3cFlhOperProgress_Type()
)
hh3cFlhOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhOperProgress.setStatus("current")
_Hh3cFlhOperRowStatus_Type = RowStatus
_Hh3cFlhOperRowStatus_Object = MibTableColumn
hh3cFlhOperRowStatus = _Hh3cFlhOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 12),
    _Hh3cFlhOperRowStatus_Type()
)
hh3cFlhOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperRowStatus.setStatus("current")


class _Hh3cFlhOperServerPort_Type(Integer32):
    """Custom type hh3cFlhOperServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cFlhOperServerPort_Type.__name__ = "Integer32"
_Hh3cFlhOperServerPort_Object = MibTableColumn
hh3cFlhOperServerPort = _Hh3cFlhOperServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 13),
    _Hh3cFlhOperServerPort_Type()
)
hh3cFlhOperServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlhOperServerPort.setStatus("current")
_Hh3cFlhOperFailReason_Type = DisplayString
_Hh3cFlhOperFailReason_Object = MibTableColumn
hh3cFlhOperFailReason = _Hh3cFlhOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 14),
    _Hh3cFlhOperFailReason_Type()
)
hh3cFlhOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhOperFailReason.setStatus("current")
_Hh3cFlashNotification_ObjectIdentity = ObjectIdentity
hh3cFlashNotification = _Hh3cFlashNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 3)
)
_Hh3cFlashMIBConformance_ObjectIdentity = ObjectIdentity
hh3cFlashMIBConformance = _Hh3cFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2)
)
_Hh3cFlhMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cFlhMIBCompliances = _Hh3cFlhMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 1)
)
_Hh3cFlashMIBGroups_ObjectIdentity = ObjectIdentity
hh3cFlashMIBGroups = _Hh3cFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2)
)

# Managed Objects groups

hh3cFlhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 1)
)
hh3cFlhGroup.setObjects(
      *(("HH3C-FLASH-MAN-MIB", "hh3cFlhSupportNum"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhSize"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPos"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhName"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipNum"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhDescr"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhInitTime"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhRemovable"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartitionBool"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhMinPartitionSize"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhMaxPartitions"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartitionNum"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhKbyteSize"))
)
if mibBuilder.loadTexts:
    hh3cFlhGroup.setStatus("current")

hh3cFlhChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 3)
)
hh3cFlhChipGroup.setObjects(
      *(("HH3C-FLASH-MAN-MIB", "hh3cFlhChipID"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipDescr"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipWriteTimesLimit"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipWriteTimes"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipEraseTimesLimit"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipEraseTimes"))
)
if mibBuilder.loadTexts:
    hh3cFlhChipGroup.setStatus("current")

hh3cFlhPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 4)
)
hh3cFlhPartitionGroup.setObjects(
      *(("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFirstChip"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartLastChip"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartSpace"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartSpaceFree"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFileNum"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartChecksumMethod"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartStatus"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartUpgradeMode"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartName"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartRequireErase"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFileNameLen"))
)
if mibBuilder.loadTexts:
    hh3cFlhPartitionGroup.setStatus("current")

hh3cFlhFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 5)
)
hh3cFlhFileGroup.setObjects(
      *(("HH3C-FLASH-MAN-MIB", "hh3cFlhFileName"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileSize"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileStatus"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileChecksum"))
)
if mibBuilder.loadTexts:
    hh3cFlhFileGroup.setStatus("current")

hh3cFlhOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 6)
)
hh3cFlhOperationGroup.setObjects(
      *(("HH3C-FLASH-MAN-MIB", "hh3cFlhOperType"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperProtocol"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerAddress"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerUser"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperPassword"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperSourceFile"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperDestinationFile"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperStatus"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperEndNotification"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperProgress"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperRowStatus"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerPort"),
        ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperFailReason"))
)
if mibBuilder.loadTexts:
    hh3cFlhOperationGroup.setStatus("current")


# Notification objects

hh3cFlhOperNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 3, 1)
)
hh3cFlhOperNotification.setObjects(
    ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperStatus")
)
if mibBuilder.loadTexts:
    hh3cFlhOperNotification.setStatus(
        "current"
    )


# Notifications groups

hh3cFlhNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 7)
)
hh3cFlhNotificationGroup.setObjects(
    ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperNotification")
)
if mibBuilder.loadTexts:
    hh3cFlhNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cFlhMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFlhMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FLASH-MAN-MIB",
    **{"Hh3cFlashOperationStatus": Hh3cFlashOperationStatus,
       "Hh3cFlashPartitionUpgradeMode": Hh3cFlashPartitionUpgradeMode,
       "Hh3cFlashPartitionStatus": Hh3cFlashPartitionStatus,
       "hh3cFlash": hh3cFlash,
       "hh3cFlashManMIBObjects": hh3cFlashManMIBObjects,
       "hh3cFlashDevice": hh3cFlashDevice,
       "hh3cFlhSupportNum": hh3cFlhSupportNum,
       "hh3cFlashTable": hh3cFlashTable,
       "hh3cFlashEntry": hh3cFlashEntry,
       "hh3cFlhIndex": hh3cFlhIndex,
       "hh3cFlhSize": hh3cFlhSize,
       "hh3cFlhPos": hh3cFlhPos,
       "hh3cFlhName": hh3cFlhName,
       "hh3cFlhChipNum": hh3cFlhChipNum,
       "hh3cFlhDescr": hh3cFlhDescr,
       "hh3cFlhInitTime": hh3cFlhInitTime,
       "hh3cFlhRemovable": hh3cFlhRemovable,
       "hh3cFlhPartitionBool": hh3cFlhPartitionBool,
       "hh3cFlhMinPartitionSize": hh3cFlhMinPartitionSize,
       "hh3cFlhMaxPartitions": hh3cFlhMaxPartitions,
       "hh3cFlhPartitionNum": hh3cFlhPartitionNum,
       "hh3cFlhKbyteSize": hh3cFlhKbyteSize,
       "hh3cFlashChips": hh3cFlashChips,
       "hh3cFlhChipTable": hh3cFlhChipTable,
       "hh3cFlhChipEntry": hh3cFlhChipEntry,
       "hh3cFlhChipSerialNo": hh3cFlhChipSerialNo,
       "hh3cFlhChipID": hh3cFlhChipID,
       "hh3cFlhChipDescr": hh3cFlhChipDescr,
       "hh3cFlhChipWriteTimesLimit": hh3cFlhChipWriteTimesLimit,
       "hh3cFlhChipWriteTimes": hh3cFlhChipWriteTimes,
       "hh3cFlhChipEraseTimesLimit": hh3cFlhChipEraseTimesLimit,
       "hh3cFlhChipEraseTimes": hh3cFlhChipEraseTimes,
       "hh3cFlashPartitions": hh3cFlashPartitions,
       "hh3cFlhPartitionTable": hh3cFlhPartitionTable,
       "hh3cFlhPartitionEntry": hh3cFlhPartitionEntry,
       "hh3cFlhPartIndex": hh3cFlhPartIndex,
       "hh3cFlhPartFirstChip": hh3cFlhPartFirstChip,
       "hh3cFlhPartLastChip": hh3cFlhPartLastChip,
       "hh3cFlhPartSpace": hh3cFlhPartSpace,
       "hh3cFlhPartSpaceFree": hh3cFlhPartSpaceFree,
       "hh3cFlhPartFileNum": hh3cFlhPartFileNum,
       "hh3cFlhPartChecksumMethod": hh3cFlhPartChecksumMethod,
       "hh3cFlhPartStatus": hh3cFlhPartStatus,
       "hh3cFlhPartUpgradeMode": hh3cFlhPartUpgradeMode,
       "hh3cFlhPartName": hh3cFlhPartName,
       "hh3cFlhPartRequireErase": hh3cFlhPartRequireErase,
       "hh3cFlhPartFileNameLen": hh3cFlhPartFileNameLen,
       "hh3cFlhFiles": hh3cFlhFiles,
       "hh3cFlhFileTable": hh3cFlhFileTable,
       "hh3cFlhFileEntry": hh3cFlhFileEntry,
       "hh3cFlhFileIndex": hh3cFlhFileIndex,
       "hh3cFlhFileName": hh3cFlhFileName,
       "hh3cFlhFileSize": hh3cFlhFileSize,
       "hh3cFlhFileStatus": hh3cFlhFileStatus,
       "hh3cFlhFileChecksum": hh3cFlhFileChecksum,
       "hh3cFlashOperate": hh3cFlashOperate,
       "hh3cFlhOpTable": hh3cFlhOpTable,
       "hh3cFlhOpEntry": hh3cFlhOpEntry,
       "hh3cFlhOperIndex": hh3cFlhOperIndex,
       "hh3cFlhOperType": hh3cFlhOperType,
       "hh3cFlhOperProtocol": hh3cFlhOperProtocol,
       "hh3cFlhOperServerAddress": hh3cFlhOperServerAddress,
       "hh3cFlhOperServerUser": hh3cFlhOperServerUser,
       "hh3cFlhOperPassword": hh3cFlhOperPassword,
       "hh3cFlhOperSourceFile": hh3cFlhOperSourceFile,
       "hh3cFlhOperDestinationFile": hh3cFlhOperDestinationFile,
       "hh3cFlhOperStatus": hh3cFlhOperStatus,
       "hh3cFlhOperEndNotification": hh3cFlhOperEndNotification,
       "hh3cFlhOperProgress": hh3cFlhOperProgress,
       "hh3cFlhOperRowStatus": hh3cFlhOperRowStatus,
       "hh3cFlhOperServerPort": hh3cFlhOperServerPort,
       "hh3cFlhOperFailReason": hh3cFlhOperFailReason,
       "hh3cFlashNotification": hh3cFlashNotification,
       "hh3cFlhOperNotification": hh3cFlhOperNotification,
       "hh3cFlashMIBConformance": hh3cFlashMIBConformance,
       "hh3cFlhMIBCompliances": hh3cFlhMIBCompliances,
       "hh3cFlhMIBCompliance": hh3cFlhMIBCompliance,
       "hh3cFlashMIBGroups": hh3cFlashMIBGroups,
       "hh3cFlhGroup": hh3cFlhGroup,
       "hh3cFlhChipGroup": hh3cFlhChipGroup,
       "hh3cFlhPartitionGroup": hh3cFlhPartitionGroup,
       "hh3cFlhFileGroup": hh3cFlhFileGroup,
       "hh3cFlhOperationGroup": hh3cFlhOperationGroup,
       "hh3cFlhNotificationGroup": hh3cFlhNotificationGroup}
)
