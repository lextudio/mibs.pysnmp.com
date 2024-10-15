# SNMP MIB module (HPN-ICF-FLASH-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FLASH-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:25 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpnicfFlash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5)
)
hpnicfFlash.setRevisions(
        ("2013-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfFlashOperationStatus(Integer32, TextualConvention):
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
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("opAuthFail", 17),
          ("opCopyToSlaveFailure", 31),
          ("opDeleteDeviceBusy", 25),
          ("opDeleteFileFailedInSlave", 29),
          ("opDeleteFileNotExistInSlave", 28),
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
          ("opSlaveFull", 30),
          ("opSuccess", 2),
          ("opTimeout", 18),
          ("opUnknownFailure", 19))
    )



class HpnicfFlashPartitionUpgradeMode(Integer32, TextualConvention):
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



class HpnicfFlashPartitionStatus(Integer32, TextualConvention):
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

_HpnicfFlashManMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfFlashManMIBObjects = _HpnicfFlashManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1)
)
_HpnicfFlashDevice_ObjectIdentity = ObjectIdentity
hpnicfFlashDevice = _HpnicfFlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1)
)
_HpnicfFlhSupportNum_Type = Integer32
_HpnicfFlhSupportNum_Object = MibScalar
hpnicfFlhSupportNum = _HpnicfFlhSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 1),
    _HpnicfFlhSupportNum_Type()
)
hpnicfFlhSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhSupportNum.setStatus("current")
_HpnicfFlashTable_Object = MibTable
hpnicfFlashTable = _HpnicfFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFlashTable.setStatus("current")
_HpnicfFlashEntry_Object = MibTableRow
hpnicfFlashEntry = _HpnicfFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1)
)
hpnicfFlashEntry.setIndexNames(
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFlashEntry.setStatus("current")


class _HpnicfFlhIndex_Type(Integer32):
    """Custom type hpnicfFlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfFlhIndex_Type.__name__ = "Integer32"
_HpnicfFlhIndex_Object = MibTableColumn
hpnicfFlhIndex = _HpnicfFlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 1),
    _HpnicfFlhIndex_Type()
)
hpnicfFlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhIndex.setStatus("current")
_HpnicfFlhSize_Type = Integer32
_HpnicfFlhSize_Object = MibTableColumn
hpnicfFlhSize = _HpnicfFlhSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 2),
    _HpnicfFlhSize_Type()
)
hpnicfFlhSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpnicfFlhSize.setUnits("bytes")
_HpnicfFlhPos_Type = PhysicalIndex
_HpnicfFlhPos_Object = MibTableColumn
hpnicfFlhPos = _HpnicfFlhPos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 3),
    _HpnicfFlhPos_Type()
)
hpnicfFlhPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPos.setStatus("current")


class _HpnicfFlhName_Type(DisplayString):
    """Custom type hpnicfFlhName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfFlhName_Type.__name__ = "DisplayString"
_HpnicfFlhName_Object = MibTableColumn
hpnicfFlhName = _HpnicfFlhName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 4),
    _HpnicfFlhName_Type()
)
hpnicfFlhName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhName.setStatus("current")


class _HpnicfFlhChipNum_Type(Integer32):
    """Custom type hpnicfFlhChipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfFlhChipNum_Type.__name__ = "Integer32"
_HpnicfFlhChipNum_Object = MibTableColumn
hpnicfFlhChipNum = _HpnicfFlhChipNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 5),
    _HpnicfFlhChipNum_Type()
)
hpnicfFlhChipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipNum.setStatus("current")


class _HpnicfFlhDescr_Type(DisplayString):
    """Custom type hpnicfFlhDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfFlhDescr_Type.__name__ = "DisplayString"
_HpnicfFlhDescr_Object = MibTableColumn
hpnicfFlhDescr = _HpnicfFlhDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 6),
    _HpnicfFlhDescr_Type()
)
hpnicfFlhDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhDescr.setStatus("current")
_HpnicfFlhInitTime_Type = TimeStamp
_HpnicfFlhInitTime_Object = MibTableColumn
hpnicfFlhInitTime = _HpnicfFlhInitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 8),
    _HpnicfFlhInitTime_Type()
)
hpnicfFlhInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhInitTime.setStatus("current")
_HpnicfFlhRemovable_Type = TruthValue
_HpnicfFlhRemovable_Object = MibTableColumn
hpnicfFlhRemovable = _HpnicfFlhRemovable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 9),
    _HpnicfFlhRemovable_Type()
)
hpnicfFlhRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhRemovable.setStatus("current")
_HpnicfFlhPartitionBool_Type = TruthValue
_HpnicfFlhPartitionBool_Object = MibTableColumn
hpnicfFlhPartitionBool = _HpnicfFlhPartitionBool_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 11),
    _HpnicfFlhPartitionBool_Type()
)
hpnicfFlhPartitionBool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFlhPartitionBool.setStatus("current")
_HpnicfFlhMinPartitionSize_Type = Integer32
_HpnicfFlhMinPartitionSize_Object = MibTableColumn
hpnicfFlhMinPartitionSize = _HpnicfFlhMinPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 12),
    _HpnicfFlhMinPartitionSize_Type()
)
hpnicfFlhMinPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhMinPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhMinPartitionSize.setUnits("bytes")


class _HpnicfFlhMaxPartitions_Type(Integer32):
    """Custom type hpnicfFlhMaxPartitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfFlhMaxPartitions_Type.__name__ = "Integer32"
_HpnicfFlhMaxPartitions_Object = MibTableColumn
hpnicfFlhMaxPartitions = _HpnicfFlhMaxPartitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 13),
    _HpnicfFlhMaxPartitions_Type()
)
hpnicfFlhMaxPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhMaxPartitions.setStatus("current")
_HpnicfFlhPartitionNum_Type = Integer32
_HpnicfFlhPartitionNum_Object = MibTableColumn
hpnicfFlhPartitionNum = _HpnicfFlhPartitionNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 14),
    _HpnicfFlhPartitionNum_Type()
)
hpnicfFlhPartitionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartitionNum.setStatus("current")
_HpnicfFlhKbyteSize_Type = Integer32
_HpnicfFlhKbyteSize_Object = MibTableColumn
hpnicfFlhKbyteSize = _HpnicfFlhKbyteSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 15),
    _HpnicfFlhKbyteSize_Type()
)
hpnicfFlhKbyteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhKbyteSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhKbyteSize.setUnits("kbytes")
_HpnicfFlhHCSize_Type = CounterBasedGauge64
_HpnicfFlhHCSize_Object = MibTableColumn
hpnicfFlhHCSize = _HpnicfFlhHCSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 2, 1, 16),
    _HpnicfFlhHCSize_Type()
)
hpnicfFlhHCSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhHCSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhHCSize.setUnits("bytes")
_HpnicfFlashChips_ObjectIdentity = ObjectIdentity
hpnicfFlashChips = _HpnicfFlashChips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3)
)
_HpnicfFlhChipTable_Object = MibTable
hpnicfFlhChipTable = _HpnicfFlhChipTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlhChipTable.setStatus("current")
_HpnicfFlhChipEntry_Object = MibTableRow
hpnicfFlhChipEntry = _HpnicfFlhChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1)
)
hpnicfFlhChipEntry.setIndexNames(
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhIndex"),
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipSerialNo"),
)
if mibBuilder.loadTexts:
    hpnicfFlhChipEntry.setStatus("current")


class _HpnicfFlhChipSerialNo_Type(Integer32):
    """Custom type hpnicfFlhChipSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfFlhChipSerialNo_Type.__name__ = "Integer32"
_HpnicfFlhChipSerialNo_Object = MibTableColumn
hpnicfFlhChipSerialNo = _HpnicfFlhChipSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 1),
    _HpnicfFlhChipSerialNo_Type()
)
hpnicfFlhChipSerialNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFlhChipSerialNo.setStatus("current")


class _HpnicfFlhChipID_Type(DisplayString):
    """Custom type hpnicfFlhChipID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnicfFlhChipID_Type.__name__ = "DisplayString"
_HpnicfFlhChipID_Object = MibTableColumn
hpnicfFlhChipID = _HpnicfFlhChipID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 2),
    _HpnicfFlhChipID_Type()
)
hpnicfFlhChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipID.setStatus("current")


class _HpnicfFlhChipDescr_Type(DisplayString):
    """Custom type hpnicfFlhChipDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfFlhChipDescr_Type.__name__ = "DisplayString"
_HpnicfFlhChipDescr_Object = MibTableColumn
hpnicfFlhChipDescr = _HpnicfFlhChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 3),
    _HpnicfFlhChipDescr_Type()
)
hpnicfFlhChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipDescr.setStatus("current")
_HpnicfFlhChipWriteTimesLimit_Type = Integer32
_HpnicfFlhChipWriteTimesLimit_Object = MibTableColumn
hpnicfFlhChipWriteTimesLimit = _HpnicfFlhChipWriteTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 4),
    _HpnicfFlhChipWriteTimesLimit_Type()
)
hpnicfFlhChipWriteTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipWriteTimesLimit.setStatus("current")
_HpnicfFlhChipWriteTimes_Type = Counter32
_HpnicfFlhChipWriteTimes_Object = MibTableColumn
hpnicfFlhChipWriteTimes = _HpnicfFlhChipWriteTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 5),
    _HpnicfFlhChipWriteTimes_Type()
)
hpnicfFlhChipWriteTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipWriteTimes.setStatus("current")
_HpnicfFlhChipEraseTimesLimit_Type = Integer32
_HpnicfFlhChipEraseTimesLimit_Object = MibTableColumn
hpnicfFlhChipEraseTimesLimit = _HpnicfFlhChipEraseTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 6),
    _HpnicfFlhChipEraseTimesLimit_Type()
)
hpnicfFlhChipEraseTimesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipEraseTimesLimit.setStatus("current")
_HpnicfFlhChipEraseTimes_Type = Counter32
_HpnicfFlhChipEraseTimes_Object = MibTableColumn
hpnicfFlhChipEraseTimes = _HpnicfFlhChipEraseTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 3, 1, 1, 7),
    _HpnicfFlhChipEraseTimes_Type()
)
hpnicfFlhChipEraseTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhChipEraseTimes.setStatus("current")
_HpnicfFlashPartitions_ObjectIdentity = ObjectIdentity
hpnicfFlashPartitions = _HpnicfFlashPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4)
)
_HpnicfFlhPartitionTable_Object = MibTable
hpnicfFlhPartitionTable = _HpnicfFlhPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlhPartitionTable.setStatus("current")
_HpnicfFlhPartitionEntry_Object = MibTableRow
hpnicfFlhPartitionEntry = _HpnicfFlhPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1)
)
hpnicfFlhPartitionEntry.setIndexNames(
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhIndex"),
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFlhPartitionEntry.setStatus("current")


class _HpnicfFlhPartIndex_Type(Integer32):
    """Custom type hpnicfFlhPartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfFlhPartIndex_Type.__name__ = "Integer32"
_HpnicfFlhPartIndex_Object = MibTableColumn
hpnicfFlhPartIndex = _HpnicfFlhPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 1),
    _HpnicfFlhPartIndex_Type()
)
hpnicfFlhPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFlhPartIndex.setStatus("current")


class _HpnicfFlhPartFirstChip_Type(Integer32):
    """Custom type hpnicfFlhPartFirstChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfFlhPartFirstChip_Type.__name__ = "Integer32"
_HpnicfFlhPartFirstChip_Object = MibTableColumn
hpnicfFlhPartFirstChip = _HpnicfFlhPartFirstChip_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 2),
    _HpnicfFlhPartFirstChip_Type()
)
hpnicfFlhPartFirstChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartFirstChip.setStatus("current")


class _HpnicfFlhPartLastChip_Type(Integer32):
    """Custom type hpnicfFlhPartLastChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfFlhPartLastChip_Type.__name__ = "Integer32"
_HpnicfFlhPartLastChip_Object = MibTableColumn
hpnicfFlhPartLastChip = _HpnicfFlhPartLastChip_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 3),
    _HpnicfFlhPartLastChip_Type()
)
hpnicfFlhPartLastChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartLastChip.setStatus("current")
_HpnicfFlhPartSpace_Type = Integer32
_HpnicfFlhPartSpace_Object = MibTableColumn
hpnicfFlhPartSpace = _HpnicfFlhPartSpace_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 4),
    _HpnicfFlhPartSpace_Type()
)
hpnicfFlhPartSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartSpace.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpnicfFlhPartSpace.setUnits("bytes")
_HpnicfFlhPartSpaceFree_Type = Gauge32
_HpnicfFlhPartSpaceFree_Object = MibTableColumn
hpnicfFlhPartSpaceFree = _HpnicfFlhPartSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 5),
    _HpnicfFlhPartSpaceFree_Type()
)
hpnicfFlhPartSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartSpaceFree.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpnicfFlhPartSpaceFree.setUnits("bytes")
_HpnicfFlhPartFileNum_Type = Integer32
_HpnicfFlhPartFileNum_Object = MibTableColumn
hpnicfFlhPartFileNum = _HpnicfFlhPartFileNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 6),
    _HpnicfFlhPartFileNum_Type()
)
hpnicfFlhPartFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartFileNum.setStatus("current")


class _HpnicfFlhPartChecksumMethod_Type(Integer32):
    """Custom type hpnicfFlhPartChecksumMethod based on Integer32"""
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


_HpnicfFlhPartChecksumMethod_Type.__name__ = "Integer32"
_HpnicfFlhPartChecksumMethod_Object = MibTableColumn
hpnicfFlhPartChecksumMethod = _HpnicfFlhPartChecksumMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 7),
    _HpnicfFlhPartChecksumMethod_Type()
)
hpnicfFlhPartChecksumMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartChecksumMethod.setStatus("current")
_HpnicfFlhPartStatus_Type = HpnicfFlashPartitionStatus
_HpnicfFlhPartStatus_Object = MibTableColumn
hpnicfFlhPartStatus = _HpnicfFlhPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 8),
    _HpnicfFlhPartStatus_Type()
)
hpnicfFlhPartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartStatus.setStatus("current")
_HpnicfFlhPartUpgradeMode_Type = HpnicfFlashPartitionUpgradeMode
_HpnicfFlhPartUpgradeMode_Object = MibTableColumn
hpnicfFlhPartUpgradeMode = _HpnicfFlhPartUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 9),
    _HpnicfFlhPartUpgradeMode_Type()
)
hpnicfFlhPartUpgradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartUpgradeMode.setStatus("current")


class _HpnicfFlhPartName_Type(DisplayString):
    """Custom type hpnicfFlhPartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfFlhPartName_Type.__name__ = "DisplayString"
_HpnicfFlhPartName_Object = MibTableColumn
hpnicfFlhPartName = _HpnicfFlhPartName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 10),
    _HpnicfFlhPartName_Type()
)
hpnicfFlhPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartName.setStatus("current")
_HpnicfFlhPartRequireErase_Type = TruthValue
_HpnicfFlhPartRequireErase_Object = MibTableColumn
hpnicfFlhPartRequireErase = _HpnicfFlhPartRequireErase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 11),
    _HpnicfFlhPartRequireErase_Type()
)
hpnicfFlhPartRequireErase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartRequireErase.setStatus("current")


class _HpnicfFlhPartFileNameLen_Type(Integer32):
    """Custom type hpnicfFlhPartFileNameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfFlhPartFileNameLen_Type.__name__ = "Integer32"
_HpnicfFlhPartFileNameLen_Object = MibTableColumn
hpnicfFlhPartFileNameLen = _HpnicfFlhPartFileNameLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 12),
    _HpnicfFlhPartFileNameLen_Type()
)
hpnicfFlhPartFileNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartFileNameLen.setStatus("current")
_HpnicfFlhPartBootable_Type = TruthValue
_HpnicfFlhPartBootable_Object = MibTableColumn
hpnicfFlhPartBootable = _HpnicfFlhPartBootable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 13),
    _HpnicfFlhPartBootable_Type()
)
hpnicfFlhPartBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartBootable.setStatus("current")
_HpnicfFlhPartPathForGlobalOpt_Type = TruthValue
_HpnicfFlhPartPathForGlobalOpt_Object = MibTableColumn
hpnicfFlhPartPathForGlobalOpt = _HpnicfFlhPartPathForGlobalOpt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 14),
    _HpnicfFlhPartPathForGlobalOpt_Type()
)
hpnicfFlhPartPathForGlobalOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFlhPartPathForGlobalOpt.setStatus("current")
_HpnicfFlhPartHCSpace_Type = CounterBasedGauge64
_HpnicfFlhPartHCSpace_Object = MibTableColumn
hpnicfFlhPartHCSpace = _HpnicfFlhPartHCSpace_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 15),
    _HpnicfFlhPartHCSpace_Type()
)
hpnicfFlhPartHCSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartHCSpace.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhPartHCSpace.setUnits("bytes")
_HpnicfFlhPartHCSpaceFree_Type = CounterBasedGauge64
_HpnicfFlhPartHCSpaceFree_Object = MibTableColumn
hpnicfFlhPartHCSpaceFree = _HpnicfFlhPartHCSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 1, 1, 16),
    _HpnicfFlhPartHCSpaceFree_Type()
)
hpnicfFlhPartHCSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhPartHCSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhPartHCSpaceFree.setUnits("bytes")
_HpnicfFlhFiles_ObjectIdentity = ObjectIdentity
hpnicfFlhFiles = _HpnicfFlhFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2)
)
_HpnicfFlhFileTable_Object = MibTable
hpnicfFlhFileTable = _HpnicfFlhFileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlhFileTable.setStatus("current")
_HpnicfFlhFileEntry_Object = MibTableRow
hpnicfFlhFileEntry = _HpnicfFlhFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1)
)
hpnicfFlhFileEntry.setIndexNames(
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhIndex"),
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartIndex"),
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhFileIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFlhFileEntry.setStatus("current")


class _HpnicfFlhFileIndex_Type(Integer32):
    """Custom type hpnicfFlhFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfFlhFileIndex_Type.__name__ = "Integer32"
_HpnicfFlhFileIndex_Object = MibTableColumn
hpnicfFlhFileIndex = _HpnicfFlhFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 1),
    _HpnicfFlhFileIndex_Type()
)
hpnicfFlhFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFlhFileIndex.setStatus("current")


class _HpnicfFlhFileName_Type(DisplayString):
    """Custom type hpnicfFlhFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfFlhFileName_Type.__name__ = "DisplayString"
_HpnicfFlhFileName_Object = MibTableColumn
hpnicfFlhFileName = _HpnicfFlhFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 2),
    _HpnicfFlhFileName_Type()
)
hpnicfFlhFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhFileName.setStatus("current")
_HpnicfFlhFileSize_Type = Integer32
_HpnicfFlhFileSize_Object = MibTableColumn
hpnicfFlhFileSize = _HpnicfFlhFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 3),
    _HpnicfFlhFileSize_Type()
)
hpnicfFlhFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhFileSize.setStatus("deprecated")


class _HpnicfFlhFileStatus_Type(Integer32):
    """Custom type hpnicfFlhFileStatus based on Integer32"""
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


_HpnicfFlhFileStatus_Type.__name__ = "Integer32"
_HpnicfFlhFileStatus_Object = MibTableColumn
hpnicfFlhFileStatus = _HpnicfFlhFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 4),
    _HpnicfFlhFileStatus_Type()
)
hpnicfFlhFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhFileStatus.setStatus("current")
_HpnicfFlhFileChecksum_Type = OctetString
_HpnicfFlhFileChecksum_Object = MibTableColumn
hpnicfFlhFileChecksum = _HpnicfFlhFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 5),
    _HpnicfFlhFileChecksum_Type()
)
hpnicfFlhFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhFileChecksum.setStatus("current")
_HpnicfFlhFileHCSize_Type = CounterBasedGauge64
_HpnicfFlhFileHCSize_Object = MibTableColumn
hpnicfFlhFileHCSize = _HpnicfFlhFileHCSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 1, 4, 2, 1, 1, 6),
    _HpnicfFlhFileHCSize_Type()
)
hpnicfFlhFileHCSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhFileHCSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlhFileHCSize.setUnits("bytes")
_HpnicfFlashOperate_ObjectIdentity = ObjectIdentity
hpnicfFlashOperate = _HpnicfFlashOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2)
)
_HpnicfFlhOpTable_Object = MibTable
hpnicfFlhOpTable = _HpnicfFlhOpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlhOpTable.setStatus("current")
_HpnicfFlhOpEntry_Object = MibTableRow
hpnicfFlhOpEntry = _HpnicfFlhOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1)
)
hpnicfFlhOpEntry.setIndexNames(
    (0, "HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFlhOpEntry.setStatus("current")


class _HpnicfFlhOperIndex_Type(Integer32):
    """Custom type hpnicfFlhOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfFlhOperIndex_Type.__name__ = "Integer32"
_HpnicfFlhOperIndex_Object = MibTableColumn
hpnicfFlhOperIndex = _HpnicfFlhOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 1),
    _HpnicfFlhOperIndex_Type()
)
hpnicfFlhOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFlhOperIndex.setStatus("current")


class _HpnicfFlhOperType_Type(Integer32):
    """Custom type hpnicfFlhOperType based on Integer32"""
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


_HpnicfFlhOperType_Type.__name__ = "Integer32"
_HpnicfFlhOperType_Object = MibTableColumn
hpnicfFlhOperType = _HpnicfFlhOperType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 2),
    _HpnicfFlhOperType_Type()
)
hpnicfFlhOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperType.setStatus("current")


class _HpnicfFlhOperProtocol_Type(Integer32):
    """Custom type hpnicfFlhOperProtocol based on Integer32"""
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


_HpnicfFlhOperProtocol_Type.__name__ = "Integer32"
_HpnicfFlhOperProtocol_Object = MibTableColumn
hpnicfFlhOperProtocol = _HpnicfFlhOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 3),
    _HpnicfFlhOperProtocol_Type()
)
hpnicfFlhOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperProtocol.setStatus("current")


class _HpnicfFlhOperServerAddress_Type(IpAddress):
    """Custom type hpnicfFlhOperServerAddress based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_HpnicfFlhOperServerAddress_Object = MibTableColumn
hpnicfFlhOperServerAddress = _HpnicfFlhOperServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 4),
    _HpnicfFlhOperServerAddress_Type()
)
hpnicfFlhOperServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperServerAddress.setStatus("deprecated")
_HpnicfFlhOperServerUser_Type = DisplayString
_HpnicfFlhOperServerUser_Object = MibTableColumn
hpnicfFlhOperServerUser = _HpnicfFlhOperServerUser_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 5),
    _HpnicfFlhOperServerUser_Type()
)
hpnicfFlhOperServerUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperServerUser.setStatus("current")
_HpnicfFlhOperPassword_Type = DisplayString
_HpnicfFlhOperPassword_Object = MibTableColumn
hpnicfFlhOperPassword = _HpnicfFlhOperPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 6),
    _HpnicfFlhOperPassword_Type()
)
hpnicfFlhOperPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperPassword.setStatus("current")


class _HpnicfFlhOperSourceFile_Type(DisplayString):
    """Custom type hpnicfFlhOperSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfFlhOperSourceFile_Type.__name__ = "DisplayString"
_HpnicfFlhOperSourceFile_Object = MibTableColumn
hpnicfFlhOperSourceFile = _HpnicfFlhOperSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 7),
    _HpnicfFlhOperSourceFile_Type()
)
hpnicfFlhOperSourceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperSourceFile.setStatus("current")
_HpnicfFlhOperDestinationFile_Type = DisplayString
_HpnicfFlhOperDestinationFile_Object = MibTableColumn
hpnicfFlhOperDestinationFile = _HpnicfFlhOperDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 8),
    _HpnicfFlhOperDestinationFile_Type()
)
hpnicfFlhOperDestinationFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperDestinationFile.setStatus("current")
_HpnicfFlhOperStatus_Type = HpnicfFlashOperationStatus
_HpnicfFlhOperStatus_Object = MibTableColumn
hpnicfFlhOperStatus = _HpnicfFlhOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 9),
    _HpnicfFlhOperStatus_Type()
)
hpnicfFlhOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhOperStatus.setStatus("current")


class _HpnicfFlhOperEndNotification_Type(TruthValue):
    """Custom type hpnicfFlhOperEndNotification based on TruthValue"""


_HpnicfFlhOperEndNotification_Object = MibTableColumn
hpnicfFlhOperEndNotification = _HpnicfFlhOperEndNotification_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 10),
    _HpnicfFlhOperEndNotification_Type()
)
hpnicfFlhOperEndNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperEndNotification.setStatus("current")
_HpnicfFlhOperProgress_Type = TimeTicks
_HpnicfFlhOperProgress_Object = MibTableColumn
hpnicfFlhOperProgress = _HpnicfFlhOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 11),
    _HpnicfFlhOperProgress_Type()
)
hpnicfFlhOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhOperProgress.setStatus("current")
_HpnicfFlhOperRowStatus_Type = RowStatus
_HpnicfFlhOperRowStatus_Object = MibTableColumn
hpnicfFlhOperRowStatus = _HpnicfFlhOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 12),
    _HpnicfFlhOperRowStatus_Type()
)
hpnicfFlhOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperRowStatus.setStatus("current")


class _HpnicfFlhOperServerPort_Type(Integer32):
    """Custom type hpnicfFlhOperServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfFlhOperServerPort_Type.__name__ = "Integer32"
_HpnicfFlhOperServerPort_Object = MibTableColumn
hpnicfFlhOperServerPort = _HpnicfFlhOperServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 13),
    _HpnicfFlhOperServerPort_Type()
)
hpnicfFlhOperServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperServerPort.setStatus("current")
_HpnicfFlhOperFailReason_Type = DisplayString
_HpnicfFlhOperFailReason_Object = MibTableColumn
hpnicfFlhOperFailReason = _HpnicfFlhOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 14),
    _HpnicfFlhOperFailReason_Type()
)
hpnicfFlhOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhOperFailReason.setStatus("current")
_HpnicfFlhOperSrvAddrType_Type = InetAddressType
_HpnicfFlhOperSrvAddrType_Object = MibTableColumn
hpnicfFlhOperSrvAddrType = _HpnicfFlhOperSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 15),
    _HpnicfFlhOperSrvAddrType_Type()
)
hpnicfFlhOperSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperSrvAddrType.setStatus("current")
_HpnicfFlhOperSrvAddrRev_Type = InetAddress
_HpnicfFlhOperSrvAddrRev_Object = MibTableColumn
hpnicfFlhOperSrvAddrRev = _HpnicfFlhOperSrvAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 16),
    _HpnicfFlhOperSrvAddrRev_Type()
)
hpnicfFlhOperSrvAddrRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperSrvAddrRev.setStatus("current")
_HpnicfFlhOperSrvVPNName_Type = DisplayString
_HpnicfFlhOperSrvVPNName_Object = MibTableColumn
hpnicfFlhOperSrvVPNName = _HpnicfFlhOperSrvVPNName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 2, 1, 1, 17),
    _HpnicfFlhOperSrvVPNName_Type()
)
hpnicfFlhOperSrvVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlhOperSrvVPNName.setStatus("current")
_HpnicfFlashNotification_ObjectIdentity = ObjectIdentity
hpnicfFlashNotification = _HpnicfFlashNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 3)
)
_HpnicfFlashMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfFlashMIBConformance = _HpnicfFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2)
)
_HpnicfFlhMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfFlhMIBCompliances = _HpnicfFlhMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 1)
)
_HpnicfFlashMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfFlashMIBGroups = _HpnicfFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2)
)

# Managed Objects groups

hpnicfFlhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 1)
)
hpnicfFlhGroup.setObjects(
      *(("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhSupportNum"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhSize"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPos"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhName"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipNum"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhDescr"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhInitTime"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhRemovable"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartitionBool"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhMinPartitionSize"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhMaxPartitions"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartitionNum"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhIndex"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhKbyteSize"))
)
if mibBuilder.loadTexts:
    hpnicfFlhGroup.setStatus("current")

hpnicfFlhChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 3)
)
hpnicfFlhChipGroup.setObjects(
      *(("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipID"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipDescr"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipWriteTimesLimit"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipWriteTimes"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipEraseTimesLimit"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhChipEraseTimes"))
)
if mibBuilder.loadTexts:
    hpnicfFlhChipGroup.setStatus("current")

hpnicfFlhPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 4)
)
hpnicfFlhPartitionGroup.setObjects(
      *(("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartFirstChip"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartLastChip"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartSpace"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartSpaceFree"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartFileNum"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartChecksumMethod"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartStatus"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartUpgradeMode"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartName"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartRequireErase"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartFileNameLen"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartBootable"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhPartPathForGlobalOpt"))
)
if mibBuilder.loadTexts:
    hpnicfFlhPartitionGroup.setStatus("current")

hpnicfFlhFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 5)
)
hpnicfFlhFileGroup.setObjects(
      *(("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhFileName"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhFileSize"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhFileStatus"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhFileChecksum"))
)
if mibBuilder.loadTexts:
    hpnicfFlhFileGroup.setStatus("current")

hpnicfFlhOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 6)
)
hpnicfFlhOperationGroup.setObjects(
      *(("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperType"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperProtocol"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperServerAddress"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperServerUser"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperPassword"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperSourceFile"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperDestinationFile"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperStatus"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperEndNotification"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperProgress"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperRowStatus"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperServerPort"),
        ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperFailReason"))
)
if mibBuilder.loadTexts:
    hpnicfFlhOperationGroup.setStatus("current")


# Notification objects

hpnicfFlhOperNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 1, 3, 1)
)
hpnicfFlhOperNotification.setObjects(
    ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperStatus")
)
if mibBuilder.loadTexts:
    hpnicfFlhOperNotification.setStatus(
        "current"
    )


# Notifications groups

hpnicfFlhNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 2, 7)
)
hpnicfFlhNotificationGroup.setObjects(
    ("HPN-ICF-FLASH-MAN-MIB", "hpnicfFlhOperNotification")
)
if mibBuilder.loadTexts:
    hpnicfFlhNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfFlhMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlhMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FLASH-MAN-MIB",
    **{"HpnicfFlashOperationStatus": HpnicfFlashOperationStatus,
       "HpnicfFlashPartitionUpgradeMode": HpnicfFlashPartitionUpgradeMode,
       "HpnicfFlashPartitionStatus": HpnicfFlashPartitionStatus,
       "hpnicfFlash": hpnicfFlash,
       "hpnicfFlashManMIBObjects": hpnicfFlashManMIBObjects,
       "hpnicfFlashDevice": hpnicfFlashDevice,
       "hpnicfFlhSupportNum": hpnicfFlhSupportNum,
       "hpnicfFlashTable": hpnicfFlashTable,
       "hpnicfFlashEntry": hpnicfFlashEntry,
       "hpnicfFlhIndex": hpnicfFlhIndex,
       "hpnicfFlhSize": hpnicfFlhSize,
       "hpnicfFlhPos": hpnicfFlhPos,
       "hpnicfFlhName": hpnicfFlhName,
       "hpnicfFlhChipNum": hpnicfFlhChipNum,
       "hpnicfFlhDescr": hpnicfFlhDescr,
       "hpnicfFlhInitTime": hpnicfFlhInitTime,
       "hpnicfFlhRemovable": hpnicfFlhRemovable,
       "hpnicfFlhPartitionBool": hpnicfFlhPartitionBool,
       "hpnicfFlhMinPartitionSize": hpnicfFlhMinPartitionSize,
       "hpnicfFlhMaxPartitions": hpnicfFlhMaxPartitions,
       "hpnicfFlhPartitionNum": hpnicfFlhPartitionNum,
       "hpnicfFlhKbyteSize": hpnicfFlhKbyteSize,
       "hpnicfFlhHCSize": hpnicfFlhHCSize,
       "hpnicfFlashChips": hpnicfFlashChips,
       "hpnicfFlhChipTable": hpnicfFlhChipTable,
       "hpnicfFlhChipEntry": hpnicfFlhChipEntry,
       "hpnicfFlhChipSerialNo": hpnicfFlhChipSerialNo,
       "hpnicfFlhChipID": hpnicfFlhChipID,
       "hpnicfFlhChipDescr": hpnicfFlhChipDescr,
       "hpnicfFlhChipWriteTimesLimit": hpnicfFlhChipWriteTimesLimit,
       "hpnicfFlhChipWriteTimes": hpnicfFlhChipWriteTimes,
       "hpnicfFlhChipEraseTimesLimit": hpnicfFlhChipEraseTimesLimit,
       "hpnicfFlhChipEraseTimes": hpnicfFlhChipEraseTimes,
       "hpnicfFlashPartitions": hpnicfFlashPartitions,
       "hpnicfFlhPartitionTable": hpnicfFlhPartitionTable,
       "hpnicfFlhPartitionEntry": hpnicfFlhPartitionEntry,
       "hpnicfFlhPartIndex": hpnicfFlhPartIndex,
       "hpnicfFlhPartFirstChip": hpnicfFlhPartFirstChip,
       "hpnicfFlhPartLastChip": hpnicfFlhPartLastChip,
       "hpnicfFlhPartSpace": hpnicfFlhPartSpace,
       "hpnicfFlhPartSpaceFree": hpnicfFlhPartSpaceFree,
       "hpnicfFlhPartFileNum": hpnicfFlhPartFileNum,
       "hpnicfFlhPartChecksumMethod": hpnicfFlhPartChecksumMethod,
       "hpnicfFlhPartStatus": hpnicfFlhPartStatus,
       "hpnicfFlhPartUpgradeMode": hpnicfFlhPartUpgradeMode,
       "hpnicfFlhPartName": hpnicfFlhPartName,
       "hpnicfFlhPartRequireErase": hpnicfFlhPartRequireErase,
       "hpnicfFlhPartFileNameLen": hpnicfFlhPartFileNameLen,
       "hpnicfFlhPartBootable": hpnicfFlhPartBootable,
       "hpnicfFlhPartPathForGlobalOpt": hpnicfFlhPartPathForGlobalOpt,
       "hpnicfFlhPartHCSpace": hpnicfFlhPartHCSpace,
       "hpnicfFlhPartHCSpaceFree": hpnicfFlhPartHCSpaceFree,
       "hpnicfFlhFiles": hpnicfFlhFiles,
       "hpnicfFlhFileTable": hpnicfFlhFileTable,
       "hpnicfFlhFileEntry": hpnicfFlhFileEntry,
       "hpnicfFlhFileIndex": hpnicfFlhFileIndex,
       "hpnicfFlhFileName": hpnicfFlhFileName,
       "hpnicfFlhFileSize": hpnicfFlhFileSize,
       "hpnicfFlhFileStatus": hpnicfFlhFileStatus,
       "hpnicfFlhFileChecksum": hpnicfFlhFileChecksum,
       "hpnicfFlhFileHCSize": hpnicfFlhFileHCSize,
       "hpnicfFlashOperate": hpnicfFlashOperate,
       "hpnicfFlhOpTable": hpnicfFlhOpTable,
       "hpnicfFlhOpEntry": hpnicfFlhOpEntry,
       "hpnicfFlhOperIndex": hpnicfFlhOperIndex,
       "hpnicfFlhOperType": hpnicfFlhOperType,
       "hpnicfFlhOperProtocol": hpnicfFlhOperProtocol,
       "hpnicfFlhOperServerAddress": hpnicfFlhOperServerAddress,
       "hpnicfFlhOperServerUser": hpnicfFlhOperServerUser,
       "hpnicfFlhOperPassword": hpnicfFlhOperPassword,
       "hpnicfFlhOperSourceFile": hpnicfFlhOperSourceFile,
       "hpnicfFlhOperDestinationFile": hpnicfFlhOperDestinationFile,
       "hpnicfFlhOperStatus": hpnicfFlhOperStatus,
       "hpnicfFlhOperEndNotification": hpnicfFlhOperEndNotification,
       "hpnicfFlhOperProgress": hpnicfFlhOperProgress,
       "hpnicfFlhOperRowStatus": hpnicfFlhOperRowStatus,
       "hpnicfFlhOperServerPort": hpnicfFlhOperServerPort,
       "hpnicfFlhOperFailReason": hpnicfFlhOperFailReason,
       "hpnicfFlhOperSrvAddrType": hpnicfFlhOperSrvAddrType,
       "hpnicfFlhOperSrvAddrRev": hpnicfFlhOperSrvAddrRev,
       "hpnicfFlhOperSrvVPNName": hpnicfFlhOperSrvVPNName,
       "hpnicfFlashNotification": hpnicfFlashNotification,
       "hpnicfFlhOperNotification": hpnicfFlhOperNotification,
       "hpnicfFlashMIBConformance": hpnicfFlashMIBConformance,
       "hpnicfFlhMIBCompliances": hpnicfFlhMIBCompliances,
       "hpnicfFlhMIBCompliance": hpnicfFlhMIBCompliance,
       "hpnicfFlashMIBGroups": hpnicfFlashMIBGroups,
       "hpnicfFlhGroup": hpnicfFlhGroup,
       "hpnicfFlhChipGroup": hpnicfFlhChipGroup,
       "hpnicfFlhPartitionGroup": hpnicfFlhPartitionGroup,
       "hpnicfFlhFileGroup": hpnicfFlhFileGroup,
       "hpnicfFlhOperationGroup": hpnicfFlhOperationGroup,
       "hpnicfFlhNotificationGroup": hpnicfFlhNotificationGroup}
)
