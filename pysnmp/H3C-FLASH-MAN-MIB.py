# SNMP MIB module (H3C-FLASH-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-FLASH-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:34 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cFlash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cFlashOperationStatus(Integer32, TextualConvention):
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



class H3cFlashPartitionUpgradeMode(Integer32, TextualConvention):
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



class H3cFlashPartitionStatus(Integer32, TextualConvention):
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

_H3cFlashManMIBObjects_ObjectIdentity = ObjectIdentity
h3cFlashManMIBObjects = _H3cFlashManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1)
)
_H3cFlashDevice_ObjectIdentity = ObjectIdentity
h3cFlashDevice = _H3cFlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1)
)
_H3cFlhSupportNum_Type = Integer32
_H3cFlhSupportNum_Object = MibScalar
h3cFlhSupportNum = _H3cFlhSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 1),
    _H3cFlhSupportNum_Type()
)
h3cFlhSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhSupportNum.setStatus("current")
_H3cFlashTable_Object = MibTable
h3cFlashTable = _H3cFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFlashTable.setStatus("current")
_H3cFlashEntry_Object = MibTableRow
h3cFlashEntry = _H3cFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1)
)
h3cFlashEntry.setIndexNames(
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"),
)
if mibBuilder.loadTexts:
    h3cFlashEntry.setStatus("current")


class _H3cFlhIndex_Type(Integer32):
    """Custom type h3cFlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cFlhIndex_Type.__name__ = "Integer32"
_H3cFlhIndex_Object = MibTableColumn
h3cFlhIndex = _H3cFlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 1),
    _H3cFlhIndex_Type()
)
h3cFlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhIndex.setStatus("current")
_H3cFlhSize_Type = Integer32
_H3cFlhSize_Object = MibTableColumn
h3cFlhSize = _H3cFlhSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 2),
    _H3cFlhSize_Type()
)
h3cFlhSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlhSize.setUnits("bytes")
_H3cFlhPos_Type = PhysicalIndex
_H3cFlhPos_Object = MibTableColumn
h3cFlhPos = _H3cFlhPos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 3),
    _H3cFlhPos_Type()
)
h3cFlhPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPos.setStatus("current")


class _H3cFlhName_Type(DisplayString):
    """Custom type h3cFlhName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_H3cFlhName_Type.__name__ = "DisplayString"
_H3cFlhName_Object = MibTableColumn
h3cFlhName = _H3cFlhName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 4),
    _H3cFlhName_Type()
)
h3cFlhName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhName.setStatus("current")


class _H3cFlhChipNum_Type(Integer32):
    """Custom type h3cFlhChipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cFlhChipNum_Type.__name__ = "Integer32"
_H3cFlhChipNum_Object = MibTableColumn
h3cFlhChipNum = _H3cFlhChipNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 5),
    _H3cFlhChipNum_Type()
)
h3cFlhChipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipNum.setStatus("current")


class _H3cFlhDescr_Type(DisplayString):
    """Custom type h3cFlhDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cFlhDescr_Type.__name__ = "DisplayString"
_H3cFlhDescr_Object = MibTableColumn
h3cFlhDescr = _H3cFlhDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 6),
    _H3cFlhDescr_Type()
)
h3cFlhDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhDescr.setStatus("current")
_H3cFlhInitTime_Type = TimeStamp
_H3cFlhInitTime_Object = MibTableColumn
h3cFlhInitTime = _H3cFlhInitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 8),
    _H3cFlhInitTime_Type()
)
h3cFlhInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhInitTime.setStatus("current")
_H3cFlhRemovable_Type = TruthValue
_H3cFlhRemovable_Object = MibTableColumn
h3cFlhRemovable = _H3cFlhRemovable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 9),
    _H3cFlhRemovable_Type()
)
h3cFlhRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhRemovable.setStatus("current")
_H3cFlhPartitionBool_Type = TruthValue
_H3cFlhPartitionBool_Object = MibTableColumn
h3cFlhPartitionBool = _H3cFlhPartitionBool_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 11),
    _H3cFlhPartitionBool_Type()
)
h3cFlhPartitionBool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFlhPartitionBool.setStatus("current")
_H3cFlhMinPartitionSize_Type = Integer32
_H3cFlhMinPartitionSize_Object = MibTableColumn
h3cFlhMinPartitionSize = _H3cFlhMinPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 12),
    _H3cFlhMinPartitionSize_Type()
)
h3cFlhMinPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhMinPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlhMinPartitionSize.setUnits("bytes")


class _H3cFlhMaxPartitions_Type(Integer32):
    """Custom type h3cFlhMaxPartitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cFlhMaxPartitions_Type.__name__ = "Integer32"
_H3cFlhMaxPartitions_Object = MibTableColumn
h3cFlhMaxPartitions = _H3cFlhMaxPartitions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 13),
    _H3cFlhMaxPartitions_Type()
)
h3cFlhMaxPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhMaxPartitions.setStatus("current")
_H3cFlhPartitionNum_Type = Integer32
_H3cFlhPartitionNum_Object = MibTableColumn
h3cFlhPartitionNum = _H3cFlhPartitionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 14),
    _H3cFlhPartitionNum_Type()
)
h3cFlhPartitionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartitionNum.setStatus("current")
_H3cFlhKbyteSize_Type = Integer32
_H3cFlhKbyteSize_Object = MibTableColumn
h3cFlhKbyteSize = _H3cFlhKbyteSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 15),
    _H3cFlhKbyteSize_Type()
)
h3cFlhKbyteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhKbyteSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlhKbyteSize.setUnits("kbytes")
_H3cFlashChips_ObjectIdentity = ObjectIdentity
h3cFlashChips = _H3cFlashChips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3)
)
_H3cFlhChipTable_Object = MibTable
h3cFlhChipTable = _H3cFlhChipTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cFlhChipTable.setStatus("current")
_H3cFlhChipEntry_Object = MibTableRow
h3cFlhChipEntry = _H3cFlhChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1)
)
h3cFlhChipEntry.setIndexNames(
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"),
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhChipSerialNo"),
)
if mibBuilder.loadTexts:
    h3cFlhChipEntry.setStatus("current")


class _H3cFlhChipSerialNo_Type(Integer32):
    """Custom type h3cFlhChipSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cFlhChipSerialNo_Type.__name__ = "Integer32"
_H3cFlhChipSerialNo_Object = MibTableColumn
h3cFlhChipSerialNo = _H3cFlhChipSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 1),
    _H3cFlhChipSerialNo_Type()
)
h3cFlhChipSerialNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFlhChipSerialNo.setStatus("current")


class _H3cFlhChipID_Type(DisplayString):
    """Custom type h3cFlhChipID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_H3cFlhChipID_Type.__name__ = "DisplayString"
_H3cFlhChipID_Object = MibTableColumn
h3cFlhChipID = _H3cFlhChipID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 2),
    _H3cFlhChipID_Type()
)
h3cFlhChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipID.setStatus("current")


class _H3cFlhChipDescr_Type(DisplayString):
    """Custom type h3cFlhChipDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cFlhChipDescr_Type.__name__ = "DisplayString"
_H3cFlhChipDescr_Object = MibTableColumn
h3cFlhChipDescr = _H3cFlhChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 3),
    _H3cFlhChipDescr_Type()
)
h3cFlhChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipDescr.setStatus("current")
_H3cFlhChipWriteTimesLimit_Type = Integer32
_H3cFlhChipWriteTimesLimit_Object = MibTableColumn
h3cFlhChipWriteTimesLimit = _H3cFlhChipWriteTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 4),
    _H3cFlhChipWriteTimesLimit_Type()
)
h3cFlhChipWriteTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipWriteTimesLimit.setStatus("current")
_H3cFlhChipWriteTimes_Type = Counter32
_H3cFlhChipWriteTimes_Object = MibTableColumn
h3cFlhChipWriteTimes = _H3cFlhChipWriteTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 5),
    _H3cFlhChipWriteTimes_Type()
)
h3cFlhChipWriteTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipWriteTimes.setStatus("current")
_H3cFlhChipEraseTimesLimit_Type = Integer32
_H3cFlhChipEraseTimesLimit_Object = MibTableColumn
h3cFlhChipEraseTimesLimit = _H3cFlhChipEraseTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 6),
    _H3cFlhChipEraseTimesLimit_Type()
)
h3cFlhChipEraseTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipEraseTimesLimit.setStatus("current")
_H3cFlhChipEraseTimes_Type = Counter32
_H3cFlhChipEraseTimes_Object = MibTableColumn
h3cFlhChipEraseTimes = _H3cFlhChipEraseTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 7),
    _H3cFlhChipEraseTimes_Type()
)
h3cFlhChipEraseTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhChipEraseTimes.setStatus("current")
_H3cFlashPartitions_ObjectIdentity = ObjectIdentity
h3cFlashPartitions = _H3cFlashPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4)
)
_H3cFlhPartitionTable_Object = MibTable
h3cFlhPartitionTable = _H3cFlhPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cFlhPartitionTable.setStatus("current")
_H3cFlhPartitionEntry_Object = MibTableRow
h3cFlhPartitionEntry = _H3cFlhPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1)
)
h3cFlhPartitionEntry.setIndexNames(
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"),
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhPartIndex"),
)
if mibBuilder.loadTexts:
    h3cFlhPartitionEntry.setStatus("current")


class _H3cFlhPartIndex_Type(Integer32):
    """Custom type h3cFlhPartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cFlhPartIndex_Type.__name__ = "Integer32"
_H3cFlhPartIndex_Object = MibTableColumn
h3cFlhPartIndex = _H3cFlhPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 1),
    _H3cFlhPartIndex_Type()
)
h3cFlhPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFlhPartIndex.setStatus("current")


class _H3cFlhPartFirstChip_Type(Integer32):
    """Custom type h3cFlhPartFirstChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cFlhPartFirstChip_Type.__name__ = "Integer32"
_H3cFlhPartFirstChip_Object = MibTableColumn
h3cFlhPartFirstChip = _H3cFlhPartFirstChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 2),
    _H3cFlhPartFirstChip_Type()
)
h3cFlhPartFirstChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartFirstChip.setStatus("current")


class _H3cFlhPartLastChip_Type(Integer32):
    """Custom type h3cFlhPartLastChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cFlhPartLastChip_Type.__name__ = "Integer32"
_H3cFlhPartLastChip_Object = MibTableColumn
h3cFlhPartLastChip = _H3cFlhPartLastChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 3),
    _H3cFlhPartLastChip_Type()
)
h3cFlhPartLastChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartLastChip.setStatus("current")
_H3cFlhPartSpace_Type = Integer32
_H3cFlhPartSpace_Object = MibTableColumn
h3cFlhPartSpace = _H3cFlhPartSpace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 4),
    _H3cFlhPartSpace_Type()
)
h3cFlhPartSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartSpace.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlhPartSpace.setUnits("bytes")
_H3cFlhPartSpaceFree_Type = Gauge32
_H3cFlhPartSpaceFree_Object = MibTableColumn
h3cFlhPartSpaceFree = _H3cFlhPartSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 5),
    _H3cFlhPartSpaceFree_Type()
)
h3cFlhPartSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlhPartSpaceFree.setUnits("bytes")
_H3cFlhPartFileNum_Type = Integer32
_H3cFlhPartFileNum_Object = MibTableColumn
h3cFlhPartFileNum = _H3cFlhPartFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 6),
    _H3cFlhPartFileNum_Type()
)
h3cFlhPartFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartFileNum.setStatus("current")


class _H3cFlhPartChecksumMethod_Type(Integer32):
    """Custom type h3cFlhPartChecksumMethod based on Integer32"""
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


_H3cFlhPartChecksumMethod_Type.__name__ = "Integer32"
_H3cFlhPartChecksumMethod_Object = MibTableColumn
h3cFlhPartChecksumMethod = _H3cFlhPartChecksumMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 7),
    _H3cFlhPartChecksumMethod_Type()
)
h3cFlhPartChecksumMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartChecksumMethod.setStatus("current")
_H3cFlhPartStatus_Type = H3cFlashPartitionStatus
_H3cFlhPartStatus_Object = MibTableColumn
h3cFlhPartStatus = _H3cFlhPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 8),
    _H3cFlhPartStatus_Type()
)
h3cFlhPartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartStatus.setStatus("current")
_H3cFlhPartUpgradeMode_Type = H3cFlashPartitionUpgradeMode
_H3cFlhPartUpgradeMode_Object = MibTableColumn
h3cFlhPartUpgradeMode = _H3cFlhPartUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 9),
    _H3cFlhPartUpgradeMode_Type()
)
h3cFlhPartUpgradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartUpgradeMode.setStatus("current")


class _H3cFlhPartName_Type(DisplayString):
    """Custom type h3cFlhPartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_H3cFlhPartName_Type.__name__ = "DisplayString"
_H3cFlhPartName_Object = MibTableColumn
h3cFlhPartName = _H3cFlhPartName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 10),
    _H3cFlhPartName_Type()
)
h3cFlhPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartName.setStatus("current")
_H3cFlhPartRequireErase_Type = TruthValue
_H3cFlhPartRequireErase_Object = MibTableColumn
h3cFlhPartRequireErase = _H3cFlhPartRequireErase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 11),
    _H3cFlhPartRequireErase_Type()
)
h3cFlhPartRequireErase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartRequireErase.setStatus("current")


class _H3cFlhPartFileNameLen_Type(Integer32):
    """Custom type h3cFlhPartFileNameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_H3cFlhPartFileNameLen_Type.__name__ = "Integer32"
_H3cFlhPartFileNameLen_Object = MibTableColumn
h3cFlhPartFileNameLen = _H3cFlhPartFileNameLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 12),
    _H3cFlhPartFileNameLen_Type()
)
h3cFlhPartFileNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhPartFileNameLen.setStatus("current")
_H3cFlhFiles_ObjectIdentity = ObjectIdentity
h3cFlhFiles = _H3cFlhFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2)
)
_H3cFlhFileTable_Object = MibTable
h3cFlhFileTable = _H3cFlhFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFlhFileTable.setStatus("current")
_H3cFlhFileEntry_Object = MibTableRow
h3cFlhFileEntry = _H3cFlhFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1)
)
h3cFlhFileEntry.setIndexNames(
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"),
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhPartIndex"),
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhFileIndex"),
)
if mibBuilder.loadTexts:
    h3cFlhFileEntry.setStatus("current")


class _H3cFlhFileIndex_Type(Integer32):
    """Custom type h3cFlhFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cFlhFileIndex_Type.__name__ = "Integer32"
_H3cFlhFileIndex_Object = MibTableColumn
h3cFlhFileIndex = _H3cFlhFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 1),
    _H3cFlhFileIndex_Type()
)
h3cFlhFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFlhFileIndex.setStatus("current")


class _H3cFlhFileName_Type(DisplayString):
    """Custom type h3cFlhFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cFlhFileName_Type.__name__ = "DisplayString"
_H3cFlhFileName_Object = MibTableColumn
h3cFlhFileName = _H3cFlhFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 2),
    _H3cFlhFileName_Type()
)
h3cFlhFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhFileName.setStatus("current")
_H3cFlhFileSize_Type = Integer32
_H3cFlhFileSize_Object = MibTableColumn
h3cFlhFileSize = _H3cFlhFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 3),
    _H3cFlhFileSize_Type()
)
h3cFlhFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhFileSize.setStatus("current")


class _H3cFlhFileStatus_Type(Integer32):
    """Custom type h3cFlhFileStatus based on Integer32"""
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


_H3cFlhFileStatus_Type.__name__ = "Integer32"
_H3cFlhFileStatus_Object = MibTableColumn
h3cFlhFileStatus = _H3cFlhFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 4),
    _H3cFlhFileStatus_Type()
)
h3cFlhFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhFileStatus.setStatus("current")
_H3cFlhFileChecksum_Type = OctetString
_H3cFlhFileChecksum_Object = MibTableColumn
h3cFlhFileChecksum = _H3cFlhFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 5),
    _H3cFlhFileChecksum_Type()
)
h3cFlhFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhFileChecksum.setStatus("current")
_H3cFlashOperate_ObjectIdentity = ObjectIdentity
h3cFlashOperate = _H3cFlashOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2)
)
_H3cFlhOpTable_Object = MibTable
h3cFlhOpTable = _H3cFlhOpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFlhOpTable.setStatus("current")
_H3cFlhOpEntry_Object = MibTableRow
h3cFlhOpEntry = _H3cFlhOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1)
)
h3cFlhOpEntry.setIndexNames(
    (0, "H3C-FLASH-MAN-MIB", "h3cFlhOperIndex"),
)
if mibBuilder.loadTexts:
    h3cFlhOpEntry.setStatus("current")


class _H3cFlhOperIndex_Type(Integer32):
    """Custom type h3cFlhOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cFlhOperIndex_Type.__name__ = "Integer32"
_H3cFlhOperIndex_Object = MibTableColumn
h3cFlhOperIndex = _H3cFlhOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 1),
    _H3cFlhOperIndex_Type()
)
h3cFlhOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFlhOperIndex.setStatus("current")


class _H3cFlhOperType_Type(Integer32):
    """Custom type h3cFlhOperType based on Integer32"""
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


_H3cFlhOperType_Type.__name__ = "Integer32"
_H3cFlhOperType_Object = MibTableColumn
h3cFlhOperType = _H3cFlhOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 2),
    _H3cFlhOperType_Type()
)
h3cFlhOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperType.setStatus("current")


class _H3cFlhOperProtocol_Type(Integer32):
    """Custom type h3cFlhOperProtocol based on Integer32"""
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


_H3cFlhOperProtocol_Type.__name__ = "Integer32"
_H3cFlhOperProtocol_Object = MibTableColumn
h3cFlhOperProtocol = _H3cFlhOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 3),
    _H3cFlhOperProtocol_Type()
)
h3cFlhOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperProtocol.setStatus("current")


class _H3cFlhOperServerAddress_Type(IpAddress):
    """Custom type h3cFlhOperServerAddress based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_H3cFlhOperServerAddress_Object = MibTableColumn
h3cFlhOperServerAddress = _H3cFlhOperServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 4),
    _H3cFlhOperServerAddress_Type()
)
h3cFlhOperServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperServerAddress.setStatus("current")
_H3cFlhOperServerUser_Type = DisplayString
_H3cFlhOperServerUser_Object = MibTableColumn
h3cFlhOperServerUser = _H3cFlhOperServerUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 5),
    _H3cFlhOperServerUser_Type()
)
h3cFlhOperServerUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperServerUser.setStatus("current")
_H3cFlhOperPassword_Type = DisplayString
_H3cFlhOperPassword_Object = MibTableColumn
h3cFlhOperPassword = _H3cFlhOperPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 6),
    _H3cFlhOperPassword_Type()
)
h3cFlhOperPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperPassword.setStatus("current")


class _H3cFlhOperSourceFile_Type(DisplayString):
    """Custom type h3cFlhOperSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cFlhOperSourceFile_Type.__name__ = "DisplayString"
_H3cFlhOperSourceFile_Object = MibTableColumn
h3cFlhOperSourceFile = _H3cFlhOperSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 7),
    _H3cFlhOperSourceFile_Type()
)
h3cFlhOperSourceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperSourceFile.setStatus("current")
_H3cFlhOperDestinationFile_Type = DisplayString
_H3cFlhOperDestinationFile_Object = MibTableColumn
h3cFlhOperDestinationFile = _H3cFlhOperDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 8),
    _H3cFlhOperDestinationFile_Type()
)
h3cFlhOperDestinationFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperDestinationFile.setStatus("current")
_H3cFlhOperStatus_Type = H3cFlashOperationStatus
_H3cFlhOperStatus_Object = MibTableColumn
h3cFlhOperStatus = _H3cFlhOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 9),
    _H3cFlhOperStatus_Type()
)
h3cFlhOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhOperStatus.setStatus("current")


class _H3cFlhOperEndNotification_Type(TruthValue):
    """Custom type h3cFlhOperEndNotification based on TruthValue"""


_H3cFlhOperEndNotification_Object = MibTableColumn
h3cFlhOperEndNotification = _H3cFlhOperEndNotification_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 10),
    _H3cFlhOperEndNotification_Type()
)
h3cFlhOperEndNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperEndNotification.setStatus("current")
_H3cFlhOperProgress_Type = TimeTicks
_H3cFlhOperProgress_Object = MibTableColumn
h3cFlhOperProgress = _H3cFlhOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 11),
    _H3cFlhOperProgress_Type()
)
h3cFlhOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhOperProgress.setStatus("current")
_H3cFlhOperRowStatus_Type = RowStatus
_H3cFlhOperRowStatus_Object = MibTableColumn
h3cFlhOperRowStatus = _H3cFlhOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 12),
    _H3cFlhOperRowStatus_Type()
)
h3cFlhOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperRowStatus.setStatus("current")


class _H3cFlhOperServerPort_Type(Integer32):
    """Custom type h3cFlhOperServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cFlhOperServerPort_Type.__name__ = "Integer32"
_H3cFlhOperServerPort_Object = MibTableColumn
h3cFlhOperServerPort = _H3cFlhOperServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 13),
    _H3cFlhOperServerPort_Type()
)
h3cFlhOperServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFlhOperServerPort.setStatus("current")
_H3cFlhOperFailReason_Type = DisplayString
_H3cFlhOperFailReason_Object = MibTableColumn
h3cFlhOperFailReason = _H3cFlhOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 14),
    _H3cFlhOperFailReason_Type()
)
h3cFlhOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlhOperFailReason.setStatus("current")
_H3cFlashNotification_ObjectIdentity = ObjectIdentity
h3cFlashNotification = _H3cFlashNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 3)
)
_H3cFlashMIBConformance_ObjectIdentity = ObjectIdentity
h3cFlashMIBConformance = _H3cFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2)
)
_H3cFlhMIBCompliances_ObjectIdentity = ObjectIdentity
h3cFlhMIBCompliances = _H3cFlhMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 1)
)
_H3cFlashMIBGroups_ObjectIdentity = ObjectIdentity
h3cFlashMIBGroups = _H3cFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2)
)

# Managed Objects groups

h3cFlhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 1)
)
h3cFlhGroup.setObjects(
      *(("H3C-FLASH-MAN-MIB", "h3cFlhSupportNum"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhSize"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPos"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhName"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipNum"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhDescr"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhInitTime"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhRemovable"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartitionBool"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhMinPartitionSize"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhMaxPartitions"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartitionNum"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhIndex"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhKbyteSize"))
)
if mibBuilder.loadTexts:
    h3cFlhGroup.setStatus("current")

h3cFlhChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 3)
)
h3cFlhChipGroup.setObjects(
      *(("H3C-FLASH-MAN-MIB", "h3cFlhChipID"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipDescr"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipWriteTimesLimit"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipWriteTimes"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipEraseTimesLimit"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhChipEraseTimes"))
)
if mibBuilder.loadTexts:
    h3cFlhChipGroup.setStatus("current")

h3cFlhPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 4)
)
h3cFlhPartitionGroup.setObjects(
      *(("H3C-FLASH-MAN-MIB", "h3cFlhPartFirstChip"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartLastChip"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartSpace"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartSpaceFree"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartFileNum"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartChecksumMethod"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartStatus"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartUpgradeMode"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartName"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartRequireErase"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhPartFileNameLen"))
)
if mibBuilder.loadTexts:
    h3cFlhPartitionGroup.setStatus("current")

h3cFlhFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 5)
)
h3cFlhFileGroup.setObjects(
      *(("H3C-FLASH-MAN-MIB", "h3cFlhFileName"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhFileSize"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhFileStatus"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhFileChecksum"))
)
if mibBuilder.loadTexts:
    h3cFlhFileGroup.setStatus("current")

h3cFlhOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 6)
)
h3cFlhOperationGroup.setObjects(
      *(("H3C-FLASH-MAN-MIB", "h3cFlhOperType"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperProtocol"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerAddress"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerUser"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperPassword"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperSourceFile"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperDestinationFile"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperStatus"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperEndNotification"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperProgress"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperRowStatus"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerPort"),
        ("H3C-FLASH-MAN-MIB", "h3cFlhOperFailReason"))
)
if mibBuilder.loadTexts:
    h3cFlhOperationGroup.setStatus("current")


# Notification objects

h3cFlhOperNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 3, 1)
)
h3cFlhOperNotification.setObjects(
    ("H3C-FLASH-MAN-MIB", "h3cFlhOperStatus")
)
if mibBuilder.loadTexts:
    h3cFlhOperNotification.setStatus(
        "current"
    )


# Notifications groups

h3cFlhNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 7)
)
h3cFlhNotificationGroup.setObjects(
    ("H3C-FLASH-MAN-MIB", "h3cFlhOperNotification")
)
if mibBuilder.loadTexts:
    h3cFlhNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cFlhMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFlhMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FLASH-MAN-MIB",
    **{"H3cFlashOperationStatus": H3cFlashOperationStatus,
       "H3cFlashPartitionUpgradeMode": H3cFlashPartitionUpgradeMode,
       "H3cFlashPartitionStatus": H3cFlashPartitionStatus,
       "h3cFlash": h3cFlash,
       "h3cFlashManMIBObjects": h3cFlashManMIBObjects,
       "h3cFlashDevice": h3cFlashDevice,
       "h3cFlhSupportNum": h3cFlhSupportNum,
       "h3cFlashTable": h3cFlashTable,
       "h3cFlashEntry": h3cFlashEntry,
       "h3cFlhIndex": h3cFlhIndex,
       "h3cFlhSize": h3cFlhSize,
       "h3cFlhPos": h3cFlhPos,
       "h3cFlhName": h3cFlhName,
       "h3cFlhChipNum": h3cFlhChipNum,
       "h3cFlhDescr": h3cFlhDescr,
       "h3cFlhInitTime": h3cFlhInitTime,
       "h3cFlhRemovable": h3cFlhRemovable,
       "h3cFlhPartitionBool": h3cFlhPartitionBool,
       "h3cFlhMinPartitionSize": h3cFlhMinPartitionSize,
       "h3cFlhMaxPartitions": h3cFlhMaxPartitions,
       "h3cFlhPartitionNum": h3cFlhPartitionNum,
       "h3cFlhKbyteSize": h3cFlhKbyteSize,
       "h3cFlashChips": h3cFlashChips,
       "h3cFlhChipTable": h3cFlhChipTable,
       "h3cFlhChipEntry": h3cFlhChipEntry,
       "h3cFlhChipSerialNo": h3cFlhChipSerialNo,
       "h3cFlhChipID": h3cFlhChipID,
       "h3cFlhChipDescr": h3cFlhChipDescr,
       "h3cFlhChipWriteTimesLimit": h3cFlhChipWriteTimesLimit,
       "h3cFlhChipWriteTimes": h3cFlhChipWriteTimes,
       "h3cFlhChipEraseTimesLimit": h3cFlhChipEraseTimesLimit,
       "h3cFlhChipEraseTimes": h3cFlhChipEraseTimes,
       "h3cFlashPartitions": h3cFlashPartitions,
       "h3cFlhPartitionTable": h3cFlhPartitionTable,
       "h3cFlhPartitionEntry": h3cFlhPartitionEntry,
       "h3cFlhPartIndex": h3cFlhPartIndex,
       "h3cFlhPartFirstChip": h3cFlhPartFirstChip,
       "h3cFlhPartLastChip": h3cFlhPartLastChip,
       "h3cFlhPartSpace": h3cFlhPartSpace,
       "h3cFlhPartSpaceFree": h3cFlhPartSpaceFree,
       "h3cFlhPartFileNum": h3cFlhPartFileNum,
       "h3cFlhPartChecksumMethod": h3cFlhPartChecksumMethod,
       "h3cFlhPartStatus": h3cFlhPartStatus,
       "h3cFlhPartUpgradeMode": h3cFlhPartUpgradeMode,
       "h3cFlhPartName": h3cFlhPartName,
       "h3cFlhPartRequireErase": h3cFlhPartRequireErase,
       "h3cFlhPartFileNameLen": h3cFlhPartFileNameLen,
       "h3cFlhFiles": h3cFlhFiles,
       "h3cFlhFileTable": h3cFlhFileTable,
       "h3cFlhFileEntry": h3cFlhFileEntry,
       "h3cFlhFileIndex": h3cFlhFileIndex,
       "h3cFlhFileName": h3cFlhFileName,
       "h3cFlhFileSize": h3cFlhFileSize,
       "h3cFlhFileStatus": h3cFlhFileStatus,
       "h3cFlhFileChecksum": h3cFlhFileChecksum,
       "h3cFlashOperate": h3cFlashOperate,
       "h3cFlhOpTable": h3cFlhOpTable,
       "h3cFlhOpEntry": h3cFlhOpEntry,
       "h3cFlhOperIndex": h3cFlhOperIndex,
       "h3cFlhOperType": h3cFlhOperType,
       "h3cFlhOperProtocol": h3cFlhOperProtocol,
       "h3cFlhOperServerAddress": h3cFlhOperServerAddress,
       "h3cFlhOperServerUser": h3cFlhOperServerUser,
       "h3cFlhOperPassword": h3cFlhOperPassword,
       "h3cFlhOperSourceFile": h3cFlhOperSourceFile,
       "h3cFlhOperDestinationFile": h3cFlhOperDestinationFile,
       "h3cFlhOperStatus": h3cFlhOperStatus,
       "h3cFlhOperEndNotification": h3cFlhOperEndNotification,
       "h3cFlhOperProgress": h3cFlhOperProgress,
       "h3cFlhOperRowStatus": h3cFlhOperRowStatus,
       "h3cFlhOperServerPort": h3cFlhOperServerPort,
       "h3cFlhOperFailReason": h3cFlhOperFailReason,
       "h3cFlashNotification": h3cFlashNotification,
       "h3cFlhOperNotification": h3cFlhOperNotification,
       "h3cFlashMIBConformance": h3cFlashMIBConformance,
       "h3cFlhMIBCompliances": h3cFlhMIBCompliances,
       "h3cFlhMIBCompliance": h3cFlhMIBCompliance,
       "h3cFlashMIBGroups": h3cFlashMIBGroups,
       "h3cFlhGroup": h3cFlhGroup,
       "h3cFlhChipGroup": h3cFlhChipGroup,
       "h3cFlhPartitionGroup": h3cFlhPartitionGroup,
       "h3cFlhFileGroup": h3cFlhFileGroup,
       "h3cFlhOperationGroup": h3cFlhOperationGroup,
       "h3cFlhNotificationGroup": h3cFlhNotificationGroup}
)
