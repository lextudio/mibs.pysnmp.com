# SNMP MIB module (HUAWEI-FLASH-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FLASH-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:51 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

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

hwFlash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9)
)
hwFlash.setRevisions(
        ("2015-02-10 00:01",
         "2015-01-26 00:01",
         "2014-12-15 00:01",
         "2013-07-09 00:01",
         "2002-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwFlashPartitionStatus(Integer32, TextualConvention):
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



class HwFlashPartitionUpgradeMode(Integer32, TextualConvention):
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



class HwFlashOperationStatus(Integer32, TextualConvention):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("opAbort", 19),
          ("opAuthFail", 17),
          ("opCurrentVersionFileConfilt", 22),
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
          ("opInvalidSourceAddress", 20),
          ("opInvalidSourceInterface", 21),
          ("opInvalidSourceName", 5),
          ("opNoMemory", 16),
          ("opSuccess", 2),
          ("opUnknownFailure", 18))
    )



# MIB Managed Objects in the order of their OIDs

_HuaweiFlashManMIBObjects_ObjectIdentity = ObjectIdentity
huaweiFlashManMIBObjects = _HuaweiFlashManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1)
)
_HuaweiFlashDevice_ObjectIdentity = ObjectIdentity
huaweiFlashDevice = _HuaweiFlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1)
)


class _HwFlhSupportNum_Type(Integer32):
    """Custom type hwFlhSupportNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwFlhSupportNum_Type.__name__ = "Integer32"
_HwFlhSupportNum_Object = MibScalar
hwFlhSupportNum = _HwFlhSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 1),
    _HwFlhSupportNum_Type()
)
hwFlhSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhSupportNum.setStatus("current")
_HwFlashTable_Object = MibTable
hwFlashTable = _HwFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwFlashTable.setStatus("current")
_HwFlashEntry_Object = MibTableRow
hwFlashEntry = _HwFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1)
)
hwFlashEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhIndex"),
)
if mibBuilder.loadTexts:
    hwFlashEntry.setStatus("current")


class _HwFlhIndex_Type(Integer32):
    """Custom type hwFlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwFlhIndex_Type.__name__ = "Integer32"
_HwFlhIndex_Object = MibTableColumn
hwFlhIndex = _HwFlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 1),
    _HwFlhIndex_Type()
)
hwFlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhIndex.setStatus("current")
_HwFlhSize_Type = Integer32
_HwFlhSize_Object = MibTableColumn
hwFlhSize = _HwFlhSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 2),
    _HwFlhSize_Type()
)
hwFlhSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhSize.setStatus("current")
if mibBuilder.loadTexts:
    hwFlhSize.setUnits("bytes")


class _HwFlhPos_Type(Integer32):
    """Custom type hwFlhPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwFlhPos_Type.__name__ = "Integer32"
_HwFlhPos_Object = MibTableColumn
hwFlhPos = _HwFlhPos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 3),
    _HwFlhPos_Type()
)
hwFlhPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPos.setStatus("current")


class _HwFlhName_Type(DisplayString):
    """Custom type hwFlhName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwFlhName_Type.__name__ = "DisplayString"
_HwFlhName_Object = MibTableColumn
hwFlhName = _HwFlhName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 4),
    _HwFlhName_Type()
)
hwFlhName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhName.setStatus("current")


class _HwFlhChipNum_Type(Integer32):
    """Custom type hwFlhChipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwFlhChipNum_Type.__name__ = "Integer32"
_HwFlhChipNum_Object = MibTableColumn
hwFlhChipNum = _HwFlhChipNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 5),
    _HwFlhChipNum_Type()
)
hwFlhChipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipNum.setStatus("current")


class _HwFlhDescr_Type(DisplayString):
    """Custom type hwFlhDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwFlhDescr_Type.__name__ = "DisplayString"
_HwFlhDescr_Object = MibTableColumn
hwFlhDescr = _HwFlhDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 6),
    _HwFlhDescr_Type()
)
hwFlhDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhDescr.setStatus("current")
_HwFlhInitTime_Type = TimeStamp
_HwFlhInitTime_Object = MibTableColumn
hwFlhInitTime = _HwFlhInitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 8),
    _HwFlhInitTime_Type()
)
hwFlhInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhInitTime.setStatus("current")
_HwFlhRemovable_Type = TruthValue
_HwFlhRemovable_Object = MibTableColumn
hwFlhRemovable = _HwFlhRemovable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 9),
    _HwFlhRemovable_Type()
)
hwFlhRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhRemovable.setStatus("current")
_HwFlhPartitionBool_Type = TruthValue
_HwFlhPartitionBool_Object = MibTableColumn
hwFlhPartitionBool = _HwFlhPartitionBool_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 11),
    _HwFlhPartitionBool_Type()
)
hwFlhPartitionBool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFlhPartitionBool.setStatus("current")
_HwFlhMinPartitionSize_Type = Integer32
_HwFlhMinPartitionSize_Object = MibTableColumn
hwFlhMinPartitionSize = _HwFlhMinPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 12),
    _HwFlhMinPartitionSize_Type()
)
hwFlhMinPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhMinPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    hwFlhMinPartitionSize.setUnits("bytes")


class _HwFlhMaxPartitions_Type(Integer32):
    """Custom type hwFlhMaxPartitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwFlhMaxPartitions_Type.__name__ = "Integer32"
_HwFlhMaxPartitions_Object = MibTableColumn
hwFlhMaxPartitions = _HwFlhMaxPartitions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 13),
    _HwFlhMaxPartitions_Type()
)
hwFlhMaxPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhMaxPartitions.setStatus("current")
_HwFlhPartitionNum_Type = Integer32
_HwFlhPartitionNum_Object = MibTableColumn
hwFlhPartitionNum = _HwFlhPartitionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 2, 1, 14),
    _HwFlhPartitionNum_Type()
)
hwFlhPartitionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartitionNum.setStatus("current")
_HwFlashChips_ObjectIdentity = ObjectIdentity
hwFlashChips = _HwFlashChips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3)
)
_HwFlhChipTable_Object = MibTable
hwFlhChipTable = _HwFlhChipTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwFlhChipTable.setStatus("current")
_HwFlhChipEntry_Object = MibTableRow
hwFlhChipEntry = _HwFlhChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1)
)
hwFlhChipEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhIndex"),
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhChipSerialNo"),
)
if mibBuilder.loadTexts:
    hwFlhChipEntry.setStatus("current")


class _HwFlhChipSerialNo_Type(Integer32):
    """Custom type hwFlhChipSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwFlhChipSerialNo_Type.__name__ = "Integer32"
_HwFlhChipSerialNo_Object = MibTableColumn
hwFlhChipSerialNo = _HwFlhChipSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 1),
    _HwFlhChipSerialNo_Type()
)
hwFlhChipSerialNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlhChipSerialNo.setStatus("current")


class _HwFlhChipID_Type(DisplayString):
    """Custom type hwFlhChipID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HwFlhChipID_Type.__name__ = "DisplayString"
_HwFlhChipID_Object = MibTableColumn
hwFlhChipID = _HwFlhChipID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 2),
    _HwFlhChipID_Type()
)
hwFlhChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipID.setStatus("current")


class _HwFlhChipDescr_Type(DisplayString):
    """Custom type hwFlhChipDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwFlhChipDescr_Type.__name__ = "DisplayString"
_HwFlhChipDescr_Object = MibTableColumn
hwFlhChipDescr = _HwFlhChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 3),
    _HwFlhChipDescr_Type()
)
hwFlhChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipDescr.setStatus("current")
_HwFlhChipWriteTimesLimit_Type = Integer32
_HwFlhChipWriteTimesLimit_Object = MibTableColumn
hwFlhChipWriteTimesLimit = _HwFlhChipWriteTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 4),
    _HwFlhChipWriteTimesLimit_Type()
)
hwFlhChipWriteTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipWriteTimesLimit.setStatus("current")
_HwFlhChipWriteTimes_Type = Counter32
_HwFlhChipWriteTimes_Object = MibTableColumn
hwFlhChipWriteTimes = _HwFlhChipWriteTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 5),
    _HwFlhChipWriteTimes_Type()
)
hwFlhChipWriteTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipWriteTimes.setStatus("current")
_HwFlhChipEraseTimesLimit_Type = Integer32
_HwFlhChipEraseTimesLimit_Object = MibTableColumn
hwFlhChipEraseTimesLimit = _HwFlhChipEraseTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 6),
    _HwFlhChipEraseTimesLimit_Type()
)
hwFlhChipEraseTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipEraseTimesLimit.setStatus("current")
_HwFlhChipEraseTimes_Type = Counter32
_HwFlhChipEraseTimes_Object = MibTableColumn
hwFlhChipEraseTimes = _HwFlhChipEraseTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 3, 1, 1, 7),
    _HwFlhChipEraseTimes_Type()
)
hwFlhChipEraseTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhChipEraseTimes.setStatus("current")
_HwFlashPartitions_ObjectIdentity = ObjectIdentity
hwFlashPartitions = _HwFlashPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4)
)
_HwFlhPartitionTable_Object = MibTable
hwFlhPartitionTable = _HwFlhPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwFlhPartitionTable.setStatus("current")
_HwFlhPartitionEntry_Object = MibTableRow
hwFlhPartitionEntry = _HwFlhPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1)
)
hwFlhPartitionEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhIndex"),
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhPartIndex"),
)
if mibBuilder.loadTexts:
    hwFlhPartitionEntry.setStatus("current")


class _HwFlhPartIndex_Type(Integer32):
    """Custom type hwFlhPartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwFlhPartIndex_Type.__name__ = "Integer32"
_HwFlhPartIndex_Object = MibTableColumn
hwFlhPartIndex = _HwFlhPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 1),
    _HwFlhPartIndex_Type()
)
hwFlhPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlhPartIndex.setStatus("current")


class _HwFlhPartFirstChip_Type(Integer32):
    """Custom type hwFlhPartFirstChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwFlhPartFirstChip_Type.__name__ = "Integer32"
_HwFlhPartFirstChip_Object = MibTableColumn
hwFlhPartFirstChip = _HwFlhPartFirstChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 2),
    _HwFlhPartFirstChip_Type()
)
hwFlhPartFirstChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartFirstChip.setStatus("current")


class _HwFlhPartLastChip_Type(Integer32):
    """Custom type hwFlhPartLastChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwFlhPartLastChip_Type.__name__ = "Integer32"
_HwFlhPartLastChip_Object = MibTableColumn
hwFlhPartLastChip = _HwFlhPartLastChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 3),
    _HwFlhPartLastChip_Type()
)
hwFlhPartLastChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartLastChip.setStatus("current")
_HwFlhPartSpace_Type = Integer32
_HwFlhPartSpace_Object = MibTableColumn
hwFlhPartSpace = _HwFlhPartSpace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 4),
    _HwFlhPartSpace_Type()
)
hwFlhPartSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartSpace.setStatus("current")
if mibBuilder.loadTexts:
    hwFlhPartSpace.setUnits("bytes")
_HwFlhPartSpaceFree_Type = Gauge32
_HwFlhPartSpaceFree_Object = MibTableColumn
hwFlhPartSpaceFree = _HwFlhPartSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 5),
    _HwFlhPartSpaceFree_Type()
)
hwFlhPartSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    hwFlhPartSpaceFree.setUnits("bytes")
_HwFlhPartFileNum_Type = Integer32
_HwFlhPartFileNum_Object = MibTableColumn
hwFlhPartFileNum = _HwFlhPartFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 6),
    _HwFlhPartFileNum_Type()
)
hwFlhPartFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartFileNum.setStatus("current")


class _HwFlhPartChecksumMethod_Type(Integer32):
    """Custom type hwFlhPartChecksumMethod based on Integer32"""
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


_HwFlhPartChecksumMethod_Type.__name__ = "Integer32"
_HwFlhPartChecksumMethod_Object = MibTableColumn
hwFlhPartChecksumMethod = _HwFlhPartChecksumMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 7),
    _HwFlhPartChecksumMethod_Type()
)
hwFlhPartChecksumMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartChecksumMethod.setStatus("current")
_HwFlhPartStatus_Type = HwFlashPartitionStatus
_HwFlhPartStatus_Object = MibTableColumn
hwFlhPartStatus = _HwFlhPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 8),
    _HwFlhPartStatus_Type()
)
hwFlhPartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartStatus.setStatus("current")
_HwFlhPartUpgradeMode_Type = HwFlashPartitionUpgradeMode
_HwFlhPartUpgradeMode_Object = MibTableColumn
hwFlhPartUpgradeMode = _HwFlhPartUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 9),
    _HwFlhPartUpgradeMode_Type()
)
hwFlhPartUpgradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartUpgradeMode.setStatus("current")


class _HwFlhPartName_Type(DisplayString):
    """Custom type hwFlhPartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwFlhPartName_Type.__name__ = "DisplayString"
_HwFlhPartName_Object = MibTableColumn
hwFlhPartName = _HwFlhPartName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 10),
    _HwFlhPartName_Type()
)
hwFlhPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartName.setStatus("current")
_HwFlhPartRequireErase_Type = TruthValue
_HwFlhPartRequireErase_Object = MibTableColumn
hwFlhPartRequireErase = _HwFlhPartRequireErase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 11),
    _HwFlhPartRequireErase_Type()
)
hwFlhPartRequireErase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartRequireErase.setStatus("current")


class _HwFlhPartFileNameLen_Type(Integer32):
    """Custom type hwFlhPartFileNameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwFlhPartFileNameLen_Type.__name__ = "Integer32"
_HwFlhPartFileNameLen_Object = MibTableColumn
hwFlhPartFileNameLen = _HwFlhPartFileNameLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 1, 1, 12),
    _HwFlhPartFileNameLen_Type()
)
hwFlhPartFileNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhPartFileNameLen.setStatus("current")
_HwFlhFiles_ObjectIdentity = ObjectIdentity
hwFlhFiles = _HwFlhFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2)
)
_HuaweiFlhFileTable_Object = MibTable
huaweiFlhFileTable = _HuaweiFlhFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    huaweiFlhFileTable.setStatus("current")
_HuaweiFlhFileEntry_Object = MibTableRow
huaweiFlhFileEntry = _HuaweiFlhFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1)
)
huaweiFlhFileEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhIndex"),
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhPartIndex"),
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhFileIndex"),
)
if mibBuilder.loadTexts:
    huaweiFlhFileEntry.setStatus("current")


class _HwFlhFileIndex_Type(Integer32):
    """Custom type hwFlhFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFlhFileIndex_Type.__name__ = "Integer32"
_HwFlhFileIndex_Object = MibTableColumn
hwFlhFileIndex = _HwFlhFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 1),
    _HwFlhFileIndex_Type()
)
hwFlhFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlhFileIndex.setStatus("current")


class _HwFlhFileName_Type(DisplayString):
    """Custom type hwFlhFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhFileName_Type.__name__ = "DisplayString"
_HwFlhFileName_Object = MibTableColumn
hwFlhFileName = _HwFlhFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 2),
    _HwFlhFileName_Type()
)
hwFlhFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhFileName.setStatus("current")
_HwFlhFileSize_Type = Integer32
_HwFlhFileSize_Object = MibTableColumn
hwFlhFileSize = _HwFlhFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 3),
    _HwFlhFileSize_Type()
)
hwFlhFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhFileSize.setStatus("current")


class _HwFlhFileStatus_Type(Integer32):
    """Custom type hwFlhFileStatus based on Integer32"""
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


_HwFlhFileStatus_Type.__name__ = "Integer32"
_HwFlhFileStatus_Object = MibTableColumn
hwFlhFileStatus = _HwFlhFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 4),
    _HwFlhFileStatus_Type()
)
hwFlhFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhFileStatus.setStatus("current")
_HwFlhFileChecksum_Type = OctetString
_HwFlhFileChecksum_Object = MibTableColumn
hwFlhFileChecksum = _HwFlhFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 5),
    _HwFlhFileChecksum_Type()
)
hwFlhFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhFileChecksum.setStatus("current")
_HwFlhFileTime_Type = TimeStamp
_HwFlhFileTime_Object = MibTableColumn
hwFlhFileTime = _HwFlhFileTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 1, 4, 2, 1, 1, 6),
    _HwFlhFileTime_Type()
)
hwFlhFileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhFileTime.setStatus("current")
_HuaweiFlashOperate_ObjectIdentity = ObjectIdentity
huaweiFlashOperate = _HuaweiFlashOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2)
)
_HuaweiFlhOpTable_Object = MibTable
huaweiFlhOpTable = _HuaweiFlhOpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    huaweiFlhOpTable.setStatus("current")
_HuaweiFlhOpEntry_Object = MibTableRow
huaweiFlhOpEntry = _HuaweiFlhOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1)
)
huaweiFlhOpEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhOperIndex"),
)
if mibBuilder.loadTexts:
    huaweiFlhOpEntry.setStatus("current")


class _HwFlhOperIndex_Type(Integer32):
    """Custom type hwFlhOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFlhOperIndex_Type.__name__ = "Integer32"
_HwFlhOperIndex_Object = MibTableColumn
hwFlhOperIndex = _HwFlhOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 1),
    _HwFlhOperIndex_Type()
)
hwFlhOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlhOperIndex.setStatus("current")


class _HwFlhOperType_Type(Integer32):
    """Custom type hwFlhOperType based on Integer32"""
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
        *(("delete", 4),
          ("flash2Net", 3),
          ("net2FlashWithErase", 1),
          ("net2FlashWithoutErase", 2))
    )


_HwFlhOperType_Type.__name__ = "Integer32"
_HwFlhOperType_Object = MibTableColumn
hwFlhOperType = _HwFlhOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 2),
    _HwFlhOperType_Type()
)
hwFlhOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperType.setStatus("current")


class _HwFlhOperProtocol_Type(Integer32):
    """Custom type hwFlhOperProtocol based on Integer32"""
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
        *(("ftp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_HwFlhOperProtocol_Type.__name__ = "Integer32"
_HwFlhOperProtocol_Object = MibTableColumn
hwFlhOperProtocol = _HwFlhOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 3),
    _HwFlhOperProtocol_Type()
)
hwFlhOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperProtocol.setStatus("current")
_HwFlhOperServerAddress_Type = IpAddress
_HwFlhOperServerAddress_Object = MibTableColumn
hwFlhOperServerAddress = _HwFlhOperServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 4),
    _HwFlhOperServerAddress_Type()
)
hwFlhOperServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperServerAddress.setStatus("current")


class _HwFlhOperServerUser_Type(DisplayString):
    """Custom type hwFlhOperServerUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhOperServerUser_Type.__name__ = "DisplayString"
_HwFlhOperServerUser_Object = MibTableColumn
hwFlhOperServerUser = _HwFlhOperServerUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 5),
    _HwFlhOperServerUser_Type()
)
hwFlhOperServerUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperServerUser.setStatus("current")


class _HwFlhOperPassword_Type(DisplayString):
    """Custom type hwFlhOperPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhOperPassword_Type.__name__ = "DisplayString"
_HwFlhOperPassword_Object = MibTableColumn
hwFlhOperPassword = _HwFlhOperPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 6),
    _HwFlhOperPassword_Type()
)
hwFlhOperPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperPassword.setStatus("current")


class _HwFlhOperSourceFile_Type(DisplayString):
    """Custom type hwFlhOperSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhOperSourceFile_Type.__name__ = "DisplayString"
_HwFlhOperSourceFile_Object = MibTableColumn
hwFlhOperSourceFile = _HwFlhOperSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 7),
    _HwFlhOperSourceFile_Type()
)
hwFlhOperSourceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperSourceFile.setStatus("current")


class _HwFlhOperDestinationFile_Type(DisplayString):
    """Custom type hwFlhOperDestinationFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwFlhOperDestinationFile_Type.__name__ = "DisplayString"
_HwFlhOperDestinationFile_Object = MibTableColumn
hwFlhOperDestinationFile = _HwFlhOperDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 8),
    _HwFlhOperDestinationFile_Type()
)
hwFlhOperDestinationFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperDestinationFile.setStatus("current")
_HwFlhOperStatus_Type = HwFlashOperationStatus
_HwFlhOperStatus_Object = MibTableColumn
hwFlhOperStatus = _HwFlhOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 9),
    _HwFlhOperStatus_Type()
)
hwFlhOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhOperStatus.setStatus("current")


class _HwFlhOperEndNotification_Type(TruthValue):
    """Custom type hwFlhOperEndNotification based on TruthValue"""


_HwFlhOperEndNotification_Object = MibTableColumn
hwFlhOperEndNotification = _HwFlhOperEndNotification_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 10),
    _HwFlhOperEndNotification_Type()
)
hwFlhOperEndNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperEndNotification.setStatus("current")
_HwFlhOperProgress_Type = TimeTicks
_HwFlhOperProgress_Object = MibTableColumn
hwFlhOperProgress = _HwFlhOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 11),
    _HwFlhOperProgress_Type()
)
hwFlhOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhOperProgress.setStatus("current")
_HwFlhOperRowStatus_Type = RowStatus
_HwFlhOperRowStatus_Object = MibTableColumn
hwFlhOperRowStatus = _HwFlhOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 12),
    _HwFlhOperRowStatus_Type()
)
hwFlhOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperRowStatus.setStatus("current")


class _HwFlhOperServerPort_Type(Integer32):
    """Custom type hwFlhOperServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwFlhOperServerPort_Type.__name__ = "Integer32"
_HwFlhOperServerPort_Object = MibTableColumn
hwFlhOperServerPort = _HwFlhOperServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 13),
    _HwFlhOperServerPort_Type()
)
hwFlhOperServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperServerPort.setStatus("current")


class _HwFlhOperSourceAddress_Type(IpAddress):
    """Custom type hwFlhOperSourceAddress based on IpAddress"""
    defaultValue = 0


_HwFlhOperSourceAddress_Object = MibTableColumn
hwFlhOperSourceAddress = _HwFlhOperSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 14),
    _HwFlhOperSourceAddress_Type()
)
hwFlhOperSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperSourceAddress.setStatus("current")


class _HwFlhOperSourceInterface_Type(OctetString):
    """Custom type hwFlhOperSourceInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwFlhOperSourceInterface_Type.__name__ = "OctetString"
_HwFlhOperSourceInterface_Object = MibTableColumn
hwFlhOperSourceInterface = _HwFlhOperSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 15),
    _HwFlhOperSourceInterface_Type()
)
hwFlhOperSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperSourceInterface.setStatus("current")
_HwFlhOperMemSize_Type = Integer32
_HwFlhOperMemSize_Object = MibTableColumn
hwFlhOperMemSize = _HwFlhOperMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 16),
    _HwFlhOperMemSize_Type()
)
hwFlhOperMemSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperMemSize.setStatus("current")


class _HwFlhOperVpnInstanceName_Type(OctetString):
    """Custom type hwFlhOperVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwFlhOperVpnInstanceName_Type.__name__ = "OctetString"
_HwFlhOperVpnInstanceName_Object = MibTableColumn
hwFlhOperVpnInstanceName = _HwFlhOperVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 17),
    _HwFlhOperVpnInstanceName_Type()
)
hwFlhOperVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperVpnInstanceName.setStatus("current")


class _HwFlhOperTotalFileLength_Type(Integer32):
    """Custom type hwFlhOperTotalFileLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwFlhOperTotalFileLength_Type.__name__ = "Integer32"
_HwFlhOperTotalFileLength_Object = MibTableColumn
hwFlhOperTotalFileLength = _HwFlhOperTotalFileLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 18),
    _HwFlhOperTotalFileLength_Type()
)
hwFlhOperTotalFileLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperTotalFileLength.setStatus("current")


class _HwFlhOperTransferProgress_Type(Integer32):
    """Custom type hwFlhOperTransferProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwFlhOperTransferProgress_Type.__name__ = "Integer32"
_HwFlhOperTransferProgress_Object = MibTableColumn
hwFlhOperTransferProgress = _HwFlhOperTransferProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 19),
    _HwFlhOperTransferProgress_Type()
)
hwFlhOperTransferProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhOperTransferProgress.setStatus("current")


class _HwFlhOperErrorReason_Type(DisplayString):
    """Custom type hwFlhOperErrorReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhOperErrorReason_Type.__name__ = "DisplayString"
_HwFlhOperErrorReason_Object = MibTableColumn
hwFlhOperErrorReason = _HwFlhOperErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 20),
    _HwFlhOperErrorReason_Type()
)
hwFlhOperErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhOperErrorReason.setStatus("current")


class _HwFlhOperServerIpv6Address_Type(OctetString):
    """Custom type hwFlhOperServerIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwFlhOperServerIpv6Address_Type.__name__ = "OctetString"
_HwFlhOperServerIpv6Address_Object = MibTableColumn
hwFlhOperServerIpv6Address = _HwFlhOperServerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 1, 1, 21),
    _HwFlhOperServerIpv6Address_Type()
)
hwFlhOperServerIpv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhOperServerIpv6Address.setStatus("current")
_HwFlhSyncTable_Object = MibTable
hwFlhSyncTable = _HwFlhSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwFlhSyncTable.setStatus("current")
_HwFlhSyncEntry_Object = MibTableRow
hwFlhSyncEntry = _HwFlhSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1)
)
hwFlhSyncEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwFlhSyncIndex"),
)
if mibBuilder.loadTexts:
    hwFlhSyncEntry.setStatus("current")


class _HwFlhSyncIndex_Type(Integer32):
    """Custom type hwFlhSyncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFlhSyncIndex_Type.__name__ = "Integer32"
_HwFlhSyncIndex_Object = MibTableColumn
hwFlhSyncIndex = _HwFlhSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 1),
    _HwFlhSyncIndex_Type()
)
hwFlhSyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlhSyncIndex.setStatus("current")


class _HwFlhSyncType_Type(Integer32):
    """Custom type hwFlhSyncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("net2FlashCopy", 1)
    )


_HwFlhSyncType_Type.__name__ = "Integer32"
_HwFlhSyncType_Object = MibTableColumn
hwFlhSyncType = _HwFlhSyncType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 2),
    _HwFlhSyncType_Type()
)
hwFlhSyncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncType.setStatus("current")


class _HwFlhSyncRange_Type(Integer32):
    """Custom type hwFlhSyncRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("designate", 1))
    )


_HwFlhSyncRange_Type.__name__ = "Integer32"
_HwFlhSyncRange_Object = MibTableColumn
hwFlhSyncRange = _HwFlhSyncRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 3),
    _HwFlhSyncRange_Type()
)
hwFlhSyncRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncRange.setStatus("current")


class _HwFlhSyncSourcePath_Type(DisplayString):
    """Custom type hwFlhSyncSourcePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhSyncSourcePath_Type.__name__ = "DisplayString"
_HwFlhSyncSourcePath_Object = MibTableColumn
hwFlhSyncSourcePath = _HwFlhSyncSourcePath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 4),
    _HwFlhSyncSourcePath_Type()
)
hwFlhSyncSourcePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncSourcePath.setStatus("current")


class _HwFlhSyncSourceFile_Type(DisplayString):
    """Custom type hwFlhSyncSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhSyncSourceFile_Type.__name__ = "DisplayString"
_HwFlhSyncSourceFile_Object = MibTableColumn
hwFlhSyncSourceFile = _HwFlhSyncSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 5),
    _HwFlhSyncSourceFile_Type()
)
hwFlhSyncSourceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncSourceFile.setStatus("current")


class _HwFlhSyncDestinationPath_Type(DisplayString):
    """Custom type hwFlhSyncDestinationPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhSyncDestinationPath_Type.__name__ = "DisplayString"
_HwFlhSyncDestinationPath_Object = MibTableColumn
hwFlhSyncDestinationPath = _HwFlhSyncDestinationPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 6),
    _HwFlhSyncDestinationPath_Type()
)
hwFlhSyncDestinationPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncDestinationPath.setStatus("current")


class _HwFlhSyncDestinationFile_Type(DisplayString):
    """Custom type hwFlhSyncDestinationFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwFlhSyncDestinationFile_Type.__name__ = "DisplayString"
_HwFlhSyncDestinationFile_Object = MibTableColumn
hwFlhSyncDestinationFile = _HwFlhSyncDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 7),
    _HwFlhSyncDestinationFile_Type()
)
hwFlhSyncDestinationFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncDestinationFile.setStatus("current")
_HwFlhSyncRowStatus_Type = RowStatus
_HwFlhSyncRowStatus_Object = MibTableColumn
hwFlhSyncRowStatus = _HwFlhSyncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 2, 2, 1, 8),
    _HwFlhSyncRowStatus_Type()
)
hwFlhSyncRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlhSyncRowStatus.setStatus("current")
_HuaweiFlashNotification_ObjectIdentity = ObjectIdentity
huaweiFlashNotification = _HuaweiFlashNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 3)
)
_HuaweiStorageDevice_ObjectIdentity = ObjectIdentity
huaweiStorageDevice = _HuaweiStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4)
)
_HwStorageTable_Object = MibTable
hwStorageTable = _HwStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwStorageTable.setStatus("current")
_HwStorageEntry_Object = MibTableRow
hwStorageEntry = _HwStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1)
)
hwStorageEntry.setIndexNames(
    (0, "HUAWEI-FLASH-MAN-MIB", "hwStorageIndex"),
)
if mibBuilder.loadTexts:
    hwStorageEntry.setStatus("current")


class _HwStorageIndex_Type(Integer32):
    """Custom type hwStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwStorageIndex_Type.__name__ = "Integer32"
_HwStorageIndex_Object = MibTableColumn
hwStorageIndex = _HwStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 1),
    _HwStorageIndex_Type()
)
hwStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStorageIndex.setStatus("current")


class _HwStorageType_Type(Integer32):
    """Custom type hwStorageType based on Integer32"""
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
        *(("cfCard", 3),
          ("flash", 1),
          ("hardDisk", 2),
          ("sdCard", 5),
          ("usbDisk", 4))
    )


_HwStorageType_Type.__name__ = "Integer32"
_HwStorageType_Object = MibTableColumn
hwStorageType = _HwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 2),
    _HwStorageType_Type()
)
hwStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageType.setStatus("current")
_HwStorageSpace_Type = Integer32
_HwStorageSpace_Object = MibTableColumn
hwStorageSpace = _HwStorageSpace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 3),
    _HwStorageSpace_Type()
)
hwStorageSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSpace.setStatus("current")
if mibBuilder.loadTexts:
    hwStorageSpace.setUnits("kbytes")
_HwStorageSpaceFree_Type = Integer32
_HwStorageSpaceFree_Object = MibTableColumn
hwStorageSpaceFree = _HwStorageSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 4),
    _HwStorageSpaceFree_Type()
)
hwStorageSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    hwStorageSpaceFree.setUnits("kbytes")


class _HwStorageName_Type(DisplayString):
    """Custom type hwStorageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwStorageName_Type.__name__ = "DisplayString"
_HwStorageName_Object = MibTableColumn
hwStorageName = _HwStorageName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 5),
    _HwStorageName_Type()
)
hwStorageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageName.setStatus("current")
_HwStorageDescr_Type = DisplayString
_HwStorageDescr_Object = MibTableColumn
hwStorageDescr = _HwStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 4, 2, 1, 6),
    _HwStorageDescr_Type()
)
hwStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageDescr.setStatus("current")
_HuaweiFlashMIBConformance_ObjectIdentity = ObjectIdentity
huaweiFlashMIBConformance = _HuaweiFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2)
)
_HwFlhMIBCompliances_ObjectIdentity = ObjectIdentity
hwFlhMIBCompliances = _HwFlhMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 1)
)
_HuaweiFlashMIBGroups_ObjectIdentity = ObjectIdentity
huaweiFlashMIBGroups = _HuaweiFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2)
)

# Managed Objects groups

hwFlhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 1)
)
hwFlhGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhSupportNum"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSize"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPos"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhName"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipNum"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhDescr"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhInitTime"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhRemovable"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartitionBool"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhMinPartitionSize"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhMaxPartitions"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartitionNum"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhIndex"))
)
if mibBuilder.loadTexts:
    hwFlhGroup.setStatus("current")

hwFlhChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 3)
)
hwFlhChipGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhChipID"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipDescr"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipWriteTimesLimit"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipWriteTimes"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipEraseTimesLimit"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhChipEraseTimes"))
)
if mibBuilder.loadTexts:
    hwFlhChipGroup.setStatus("current")

hwFlhPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 4)
)
hwFlhPartitionGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhPartFirstChip"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartLastChip"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartSpace"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartSpaceFree"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartFileNum"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartChecksumMethod"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartStatus"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartUpgradeMode"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartName"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartRequireErase"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhPartFileNameLen"))
)
if mibBuilder.loadTexts:
    hwFlhPartitionGroup.setStatus("current")

hwFlhFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 5)
)
hwFlhFileGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhFileName"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhFileSize"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhFileStatus"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhFileChecksum"))
)
if mibBuilder.loadTexts:
    hwFlhFileGroup.setStatus("current")

hwFlhOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 6)
)
hwFlhOperationGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhOperType"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperProtocol"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperServerAddress"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperServerUser"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperPassword"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperSourceFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperDestinationFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperStatus"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperEndNotification"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperProgress"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperRowStatus"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperServerPort"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperSourceAddress"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperSourceInterface"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperMemSize"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncType"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncRange"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncSourcePath"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncSourceFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncDestinationPath"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncDestinationFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncRowStatus"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperServerIpv6Address"))
)
if mibBuilder.loadTexts:
    hwFlhOperationGroup.setStatus("current")

hwStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 8)
)
hwStorageGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwStorageType"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageSpace"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageSpaceFree"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageName"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageDescr"))
)
if mibBuilder.loadTexts:
    hwStorageGroup.setStatus("current")


# Notification objects

hwFlhOperNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 3, 1)
)
hwFlhOperNotification.setObjects(
    ("HUAWEI-FLASH-MAN-MIB", "hwFlhOperStatus")
)
if mibBuilder.loadTexts:
    hwFlhOperNotification.setStatus(
        "current"
    )

hwFlhSyncSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 3, 2)
)
hwFlhSyncSuccessNotification.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncSourceFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncDestinationFile"))
)
if mibBuilder.loadTexts:
    hwFlhSyncSuccessNotification.setStatus(
        "current"
    )

hwFlhSyncFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 1, 3, 3)
)
hwFlhSyncFailNotification.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncSourceFile"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncDestinationFile"))
)
if mibBuilder.loadTexts:
    hwFlhSyncFailNotification.setStatus(
        "current"
    )


# Notifications groups

hwFlhNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 2, 7)
)
hwFlhNotificationGroup.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwFlhOperNotification"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncSuccessNotification"),
        ("HUAWEI-FLASH-MAN-MIB", "hwFlhSyncFailNotification"))
)
if mibBuilder.loadTexts:
    hwFlhNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwFlhMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwFlhMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FLASH-MAN-MIB",
    **{"HwFlashPartitionStatus": HwFlashPartitionStatus,
       "HwFlashPartitionUpgradeMode": HwFlashPartitionUpgradeMode,
       "HwFlashOperationStatus": HwFlashOperationStatus,
       "hwFlash": hwFlash,
       "huaweiFlashManMIBObjects": huaweiFlashManMIBObjects,
       "huaweiFlashDevice": huaweiFlashDevice,
       "hwFlhSupportNum": hwFlhSupportNum,
       "hwFlashTable": hwFlashTable,
       "hwFlashEntry": hwFlashEntry,
       "hwFlhIndex": hwFlhIndex,
       "hwFlhSize": hwFlhSize,
       "hwFlhPos": hwFlhPos,
       "hwFlhName": hwFlhName,
       "hwFlhChipNum": hwFlhChipNum,
       "hwFlhDescr": hwFlhDescr,
       "hwFlhInitTime": hwFlhInitTime,
       "hwFlhRemovable": hwFlhRemovable,
       "hwFlhPartitionBool": hwFlhPartitionBool,
       "hwFlhMinPartitionSize": hwFlhMinPartitionSize,
       "hwFlhMaxPartitions": hwFlhMaxPartitions,
       "hwFlhPartitionNum": hwFlhPartitionNum,
       "hwFlashChips": hwFlashChips,
       "hwFlhChipTable": hwFlhChipTable,
       "hwFlhChipEntry": hwFlhChipEntry,
       "hwFlhChipSerialNo": hwFlhChipSerialNo,
       "hwFlhChipID": hwFlhChipID,
       "hwFlhChipDescr": hwFlhChipDescr,
       "hwFlhChipWriteTimesLimit": hwFlhChipWriteTimesLimit,
       "hwFlhChipWriteTimes": hwFlhChipWriteTimes,
       "hwFlhChipEraseTimesLimit": hwFlhChipEraseTimesLimit,
       "hwFlhChipEraseTimes": hwFlhChipEraseTimes,
       "hwFlashPartitions": hwFlashPartitions,
       "hwFlhPartitionTable": hwFlhPartitionTable,
       "hwFlhPartitionEntry": hwFlhPartitionEntry,
       "hwFlhPartIndex": hwFlhPartIndex,
       "hwFlhPartFirstChip": hwFlhPartFirstChip,
       "hwFlhPartLastChip": hwFlhPartLastChip,
       "hwFlhPartSpace": hwFlhPartSpace,
       "hwFlhPartSpaceFree": hwFlhPartSpaceFree,
       "hwFlhPartFileNum": hwFlhPartFileNum,
       "hwFlhPartChecksumMethod": hwFlhPartChecksumMethod,
       "hwFlhPartStatus": hwFlhPartStatus,
       "hwFlhPartUpgradeMode": hwFlhPartUpgradeMode,
       "hwFlhPartName": hwFlhPartName,
       "hwFlhPartRequireErase": hwFlhPartRequireErase,
       "hwFlhPartFileNameLen": hwFlhPartFileNameLen,
       "hwFlhFiles": hwFlhFiles,
       "huaweiFlhFileTable": huaweiFlhFileTable,
       "huaweiFlhFileEntry": huaweiFlhFileEntry,
       "hwFlhFileIndex": hwFlhFileIndex,
       "hwFlhFileName": hwFlhFileName,
       "hwFlhFileSize": hwFlhFileSize,
       "hwFlhFileStatus": hwFlhFileStatus,
       "hwFlhFileChecksum": hwFlhFileChecksum,
       "hwFlhFileTime": hwFlhFileTime,
       "huaweiFlashOperate": huaweiFlashOperate,
       "huaweiFlhOpTable": huaweiFlhOpTable,
       "huaweiFlhOpEntry": huaweiFlhOpEntry,
       "hwFlhOperIndex": hwFlhOperIndex,
       "hwFlhOperType": hwFlhOperType,
       "hwFlhOperProtocol": hwFlhOperProtocol,
       "hwFlhOperServerAddress": hwFlhOperServerAddress,
       "hwFlhOperServerUser": hwFlhOperServerUser,
       "hwFlhOperPassword": hwFlhOperPassword,
       "hwFlhOperSourceFile": hwFlhOperSourceFile,
       "hwFlhOperDestinationFile": hwFlhOperDestinationFile,
       "hwFlhOperStatus": hwFlhOperStatus,
       "hwFlhOperEndNotification": hwFlhOperEndNotification,
       "hwFlhOperProgress": hwFlhOperProgress,
       "hwFlhOperRowStatus": hwFlhOperRowStatus,
       "hwFlhOperServerPort": hwFlhOperServerPort,
       "hwFlhOperSourceAddress": hwFlhOperSourceAddress,
       "hwFlhOperSourceInterface": hwFlhOperSourceInterface,
       "hwFlhOperMemSize": hwFlhOperMemSize,
       "hwFlhOperVpnInstanceName": hwFlhOperVpnInstanceName,
       "hwFlhOperTotalFileLength": hwFlhOperTotalFileLength,
       "hwFlhOperTransferProgress": hwFlhOperTransferProgress,
       "hwFlhOperErrorReason": hwFlhOperErrorReason,
       "hwFlhOperServerIpv6Address": hwFlhOperServerIpv6Address,
       "hwFlhSyncTable": hwFlhSyncTable,
       "hwFlhSyncEntry": hwFlhSyncEntry,
       "hwFlhSyncIndex": hwFlhSyncIndex,
       "hwFlhSyncType": hwFlhSyncType,
       "hwFlhSyncRange": hwFlhSyncRange,
       "hwFlhSyncSourcePath": hwFlhSyncSourcePath,
       "hwFlhSyncSourceFile": hwFlhSyncSourceFile,
       "hwFlhSyncDestinationPath": hwFlhSyncDestinationPath,
       "hwFlhSyncDestinationFile": hwFlhSyncDestinationFile,
       "hwFlhSyncRowStatus": hwFlhSyncRowStatus,
       "huaweiFlashNotification": huaweiFlashNotification,
       "hwFlhOperNotification": hwFlhOperNotification,
       "hwFlhSyncSuccessNotification": hwFlhSyncSuccessNotification,
       "hwFlhSyncFailNotification": hwFlhSyncFailNotification,
       "huaweiStorageDevice": huaweiStorageDevice,
       "hwStorageTable": hwStorageTable,
       "hwStorageEntry": hwStorageEntry,
       "hwStorageIndex": hwStorageIndex,
       "hwStorageType": hwStorageType,
       "hwStorageSpace": hwStorageSpace,
       "hwStorageSpaceFree": hwStorageSpaceFree,
       "hwStorageName": hwStorageName,
       "hwStorageDescr": hwStorageDescr,
       "huaweiFlashMIBConformance": huaweiFlashMIBConformance,
       "hwFlhMIBCompliances": hwFlhMIBCompliances,
       "hwFlhMIBCompliance": hwFlhMIBCompliance,
       "huaweiFlashMIBGroups": huaweiFlashMIBGroups,
       "hwFlhGroup": hwFlhGroup,
       "hwFlhChipGroup": hwFlhChipGroup,
       "hwFlhPartitionGroup": hwFlhPartitionGroup,
       "hwFlhFileGroup": hwFlhFileGroup,
       "hwFlhOperationGroup": hwFlhOperationGroup,
       "hwFlhNotificationGroup": hwFlhNotificationGroup,
       "hwStorageGroup": hwStorageGroup}
)
