# SNMP MIB module (HUAWEI-BULKSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BULKSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:16 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwBulkStat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140)
)
hwBulkStat.setRevisions(
        ("2013-07-01 13:39",
         "2006-11-22 14:14")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwBulkStatMibObjects_ObjectIdentity = ObjectIdentity
hwBulkStatMibObjects = _HwBulkStatMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1)
)


class _HwBulkStatEnable_Type(Integer32):
    """Custom type hwBulkStatEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwBulkStatEnable_Type.__name__ = "Integer32"
_HwBulkStatEnable_Object = MibScalar
hwBulkStatEnable = _HwBulkStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 1),
    _HwBulkStatEnable_Type()
)
hwBulkStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBulkStatEnable.setStatus("current")
_HwBulkStatCollectCapability_Type = Integer32
_HwBulkStatCollectCapability_Object = MibScalar
hwBulkStatCollectCapability = _HwBulkStatCollectCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 2),
    _HwBulkStatCollectCapability_Type()
)
hwBulkStatCollectCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatCollectCapability.setStatus("current")
_HwBulkStatDefineMaxFiles_Type = Integer32
_HwBulkStatDefineMaxFiles_Object = MibScalar
hwBulkStatDefineMaxFiles = _HwBulkStatDefineMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 3),
    _HwBulkStatDefineMaxFiles_Type()
)
hwBulkStatDefineMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineMaxFiles.setStatus("current")
_HwBulkStatDefineFiles_Type = Integer32
_HwBulkStatDefineFiles_Object = MibScalar
hwBulkStatDefineFiles = _HwBulkStatDefineFiles_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 4),
    _HwBulkStatDefineFiles_Type()
)
hwBulkStatDefineFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineFiles.setStatus("current")
_HwBulkStatDefineObjects_Type = Integer32
_HwBulkStatDefineObjects_Object = MibScalar
hwBulkStatDefineObjects = _HwBulkStatDefineObjects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 5),
    _HwBulkStatDefineObjects_Type()
)
hwBulkStatDefineObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjects.setStatus("current")


class _HwBulkStatTrapEnable_Type(Integer32):
    """Custom type hwBulkStatTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwBulkStatTrapEnable_Type.__name__ = "Integer32"
_HwBulkStatTrapEnable_Object = MibScalar
hwBulkStatTrapEnable = _HwBulkStatTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 6),
    _HwBulkStatTrapEnable_Type()
)
hwBulkStatTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBulkStatTrapEnable.setStatus("current")
_HwBulkStatDefineFileTableNextIndex_Type = Integer32
_HwBulkStatDefineFileTableNextIndex_Object = MibScalar
hwBulkStatDefineFileTableNextIndex = _HwBulkStatDefineFileTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 7),
    _HwBulkStatDefineFileTableNextIndex_Type()
)
hwBulkStatDefineFileTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTableNextIndex.setStatus("current")
_HwBulkStatDefineFileTable_Object = MibTable
hwBulkStatDefineFileTable = _HwBulkStatDefineFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8)
)
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTable.setStatus("current")
_HwBulkStatDefineFileEntry_Object = MibTableRow
hwBulkStatDefineFileEntry = _HwBulkStatDefineFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1)
)
hwBulkStatDefineFileEntry.setIndexNames(
    (0, "HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileIndex"),
)
if mibBuilder.loadTexts:
    hwBulkStatDefineFileEntry.setStatus("current")


class _HwBulkStatDefineFileIndex_Type(Integer32):
    """Custom type hwBulkStatDefineFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwBulkStatDefineFileIndex_Type.__name__ = "Integer32"
_HwBulkStatDefineFileIndex_Object = MibTableColumn
hwBulkStatDefineFileIndex = _HwBulkStatDefineFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 1),
    _HwBulkStatDefineFileIndex_Type()
)
hwBulkStatDefineFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileIndex.setStatus("current")


class _HwBulkStatDefineFileName_Type(OctetString):
    """Custom type hwBulkStatDefineFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBulkStatDefineFileName_Type.__name__ = "OctetString"
_HwBulkStatDefineFileName_Object = MibTableColumn
hwBulkStatDefineFileName = _HwBulkStatDefineFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 11),
    _HwBulkStatDefineFileName_Type()
)
hwBulkStatDefineFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileName.setStatus("current")


class _HwBulkStatDefineFileStorage_Type(Integer32):
    """Custom type hwBulkStatDefineFileStorage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ephemeral", 1)
    )


_HwBulkStatDefineFileStorage_Type.__name__ = "Integer32"
_HwBulkStatDefineFileStorage_Object = MibTableColumn
hwBulkStatDefineFileStorage = _HwBulkStatDefineFileStorage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 12),
    _HwBulkStatDefineFileStorage_Type()
)
hwBulkStatDefineFileStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileStorage.setStatus("current")


class _HwBulkStatDefineFileFormat_Type(Integer32):
    """Custom type hwBulkStatDefineFileFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bulkASCII", 1)
    )


_HwBulkStatDefineFileFormat_Type.__name__ = "Integer32"
_HwBulkStatDefineFileFormat_Object = MibTableColumn
hwBulkStatDefineFileFormat = _HwBulkStatDefineFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 13),
    _HwBulkStatDefineFileFormat_Type()
)
hwBulkStatDefineFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileFormat.setStatus("current")


class _HwBulkStatDefineFileCollectInterval_Type(Integer32):
    """Custom type hwBulkStatDefineFileCollectInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(30, 30),
    )


_HwBulkStatDefineFileCollectInterval_Type.__name__ = "Integer32"
_HwBulkStatDefineFileCollectInterval_Object = MibTableColumn
hwBulkStatDefineFileCollectInterval = _HwBulkStatDefineFileCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 14),
    _HwBulkStatDefineFileCollectInterval_Type()
)
hwBulkStatDefineFileCollectInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileCollectInterval.setStatus("current")


class _HwBulkStatDefineFileTransferInterval_Type(Integer32):
    """Custom type hwBulkStatDefineFileTransferInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(30, 30),
    )


_HwBulkStatDefineFileTransferInterval_Type.__name__ = "Integer32"
_HwBulkStatDefineFileTransferInterval_Object = MibTableColumn
hwBulkStatDefineFileTransferInterval = _HwBulkStatDefineFileTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 15),
    _HwBulkStatDefineFileTransferInterval_Type()
)
hwBulkStatDefineFileTransferInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTransferInterval.setStatus("current")


class _HwBulkStatDefineFileTransferPrimaryURL_Type(OctetString):
    """Custom type hwBulkStatDefineFileTransferPrimaryURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwBulkStatDefineFileTransferPrimaryURL_Type.__name__ = "OctetString"
_HwBulkStatDefineFileTransferPrimaryURL_Object = MibTableColumn
hwBulkStatDefineFileTransferPrimaryURL = _HwBulkStatDefineFileTransferPrimaryURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 16),
    _HwBulkStatDefineFileTransferPrimaryURL_Type()
)
hwBulkStatDefineFileTransferPrimaryURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTransferPrimaryURL.setStatus("current")


class _HwBulkStatDefineFileTransferSecondaryURL_Type(OctetString):
    """Custom type hwBulkStatDefineFileTransferSecondaryURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwBulkStatDefineFileTransferSecondaryURL_Type.__name__ = "OctetString"
_HwBulkStatDefineFileTransferSecondaryURL_Object = MibTableColumn
hwBulkStatDefineFileTransferSecondaryURL = _HwBulkStatDefineFileTransferSecondaryURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 17),
    _HwBulkStatDefineFileTransferSecondaryURL_Type()
)
hwBulkStatDefineFileTransferSecondaryURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTransferSecondaryURL.setStatus("current")


class _HwBulkStatDefineFileTransferRetryTimes_Type(Integer32):
    """Custom type hwBulkStatDefineFileTransferRetryTimes based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwBulkStatDefineFileTransferRetryTimes_Type.__name__ = "Integer32"
_HwBulkStatDefineFileTransferRetryTimes_Object = MibTableColumn
hwBulkStatDefineFileTransferRetryTimes = _HwBulkStatDefineFileTransferRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 18),
    _HwBulkStatDefineFileTransferRetryTimes_Type()
)
hwBulkStatDefineFileTransferRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileTransferRetryTimes.setStatus("current")


class _HwBulkStatDefineFileRemainTime_Type(Integer32):
    """Custom type hwBulkStatDefineFileRemainTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HwBulkStatDefineFileRemainTime_Type.__name__ = "Integer32"
_HwBulkStatDefineFileRemainTime_Object = MibTableColumn
hwBulkStatDefineFileRemainTime = _HwBulkStatDefineFileRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 19),
    _HwBulkStatDefineFileRemainTime_Type()
)
hwBulkStatDefineFileRemainTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileRemainTime.setStatus("current")


class _HwBulkStatDefineFileStatus_Type(Integer32):
    """Custom type hwBulkStatDefineFileStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("running", 2),
          ("stopped", 3))
    )


_HwBulkStatDefineFileStatus_Type.__name__ = "Integer32"
_HwBulkStatDefineFileStatus_Object = MibTableColumn
hwBulkStatDefineFileStatus = _HwBulkStatDefineFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 20),
    _HwBulkStatDefineFileStatus_Type()
)
hwBulkStatDefineFileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileStatus.setStatus("current")
_HwBulkStatDefineFileLastTransferSuccessTime_Type = Integer32
_HwBulkStatDefineFileLastTransferSuccessTime_Object = MibTableColumn
hwBulkStatDefineFileLastTransferSuccessTime = _HwBulkStatDefineFileLastTransferSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 21),
    _HwBulkStatDefineFileLastTransferSuccessTime_Type()
)
hwBulkStatDefineFileLastTransferSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileLastTransferSuccessTime.setStatus("current")
_HwBulkStatDefineFileLastTransferFailTime_Type = Integer32
_HwBulkStatDefineFileLastTransferFailTime_Object = MibTableColumn
hwBulkStatDefineFileLastTransferFailTime = _HwBulkStatDefineFileLastTransferFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 22),
    _HwBulkStatDefineFileLastTransferFailTime_Type()
)
hwBulkStatDefineFileLastTransferFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileLastTransferFailTime.setStatus("current")


class _HwBulkStatDefineFileNextObjectIndex_Type(Integer32):
    """Custom type hwBulkStatDefineFileNextObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwBulkStatDefineFileNextObjectIndex_Type.__name__ = "Integer32"
_HwBulkStatDefineFileNextObjectIndex_Object = MibTableColumn
hwBulkStatDefineFileNextObjectIndex = _HwBulkStatDefineFileNextObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 23),
    _HwBulkStatDefineFileNextObjectIndex_Type()
)
hwBulkStatDefineFileNextObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileNextObjectIndex.setStatus("current")
_HwBulkStatDefineFileRowStatus_Type = RowStatus
_HwBulkStatDefineFileRowStatus_Object = MibTableColumn
hwBulkStatDefineFileRowStatus = _HwBulkStatDefineFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 8, 1, 51),
    _HwBulkStatDefineFileRowStatus_Type()
)
hwBulkStatDefineFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineFileRowStatus.setStatus("current")
_HwBulkStatDefineObjectTable_Object = MibTable
hwBulkStatDefineObjectTable = _HwBulkStatDefineObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9)
)
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectTable.setStatus("current")
_HwBulkStatDefineObjectEntry_Object = MibTableRow
hwBulkStatDefineObjectEntry = _HwBulkStatDefineObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1)
)
hwBulkStatDefineObjectEntry.setIndexNames(
    (0, "HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileIndex"),
    (0, "HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectIndex"),
)
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectEntry.setStatus("current")


class _HwBulkStatDefineObjectIndex_Type(Integer32):
    """Custom type hwBulkStatDefineObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwBulkStatDefineObjectIndex_Type.__name__ = "Integer32"
_HwBulkStatDefineObjectIndex_Object = MibTableColumn
hwBulkStatDefineObjectIndex = _HwBulkStatDefineObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 1),
    _HwBulkStatDefineObjectIndex_Type()
)
hwBulkStatDefineObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectIndex.setStatus("current")


class _HwBulkStatDefineObjectClass_Type(Integer32):
    """Custom type hwBulkStatDefineObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("column", 2),
          ("single", 1))
    )


_HwBulkStatDefineObjectClass_Type.__name__ = "Integer32"
_HwBulkStatDefineObjectClass_Object = MibTableColumn
hwBulkStatDefineObjectClass = _HwBulkStatDefineObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 11),
    _HwBulkStatDefineObjectClass_Type()
)
hwBulkStatDefineObjectClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectClass.setStatus("current")


class _HwBulkStatDefineObjectOID_Type(OctetString):
    """Custom type hwBulkStatDefineObjectOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwBulkStatDefineObjectOID_Type.__name__ = "OctetString"
_HwBulkStatDefineObjectOID_Object = MibTableColumn
hwBulkStatDefineObjectOID = _HwBulkStatDefineObjectOID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 12),
    _HwBulkStatDefineObjectOID_Type()
)
hwBulkStatDefineObjectOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectOID.setStatus("current")


class _HwBulkStatDefineObjectIndexBegin_Type(OctetString):
    """Custom type hwBulkStatDefineObjectIndexBegin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwBulkStatDefineObjectIndexBegin_Type.__name__ = "OctetString"
_HwBulkStatDefineObjectIndexBegin_Object = MibTableColumn
hwBulkStatDefineObjectIndexBegin = _HwBulkStatDefineObjectIndexBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 13),
    _HwBulkStatDefineObjectIndexBegin_Type()
)
hwBulkStatDefineObjectIndexBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectIndexBegin.setStatus("current")


class _HwBulkStatDefineObjectInstanceNum_Type(Integer32):
    """Custom type hwBulkStatDefineObjectInstanceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBulkStatDefineObjectInstanceNum_Type.__name__ = "Integer32"
_HwBulkStatDefineObjectInstanceNum_Object = MibTableColumn
hwBulkStatDefineObjectInstanceNum = _HwBulkStatDefineObjectInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 14),
    _HwBulkStatDefineObjectInstanceNum_Type()
)
hwBulkStatDefineObjectInstanceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectInstanceNum.setStatus("current")
_HwBulkStatDefineObjectRowStatus_Type = RowStatus
_HwBulkStatDefineObjectRowStatus_Object = MibTableColumn
hwBulkStatDefineObjectRowStatus = _HwBulkStatDefineObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 1, 9, 1, 51),
    _HwBulkStatDefineObjectRowStatus_Type()
)
hwBulkStatDefineObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectRowStatus.setStatus("current")
_HwBulkStatNotifications_ObjectIdentity = ObjectIdentity
hwBulkStatNotifications = _HwBulkStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2)
)
_HwBulkStatConformance_ObjectIdentity = ObjectIdentity
hwBulkStatConformance = _HwBulkStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3)
)
_HwBulkStatCompliances_ObjectIdentity = ObjectIdentity
hwBulkStatCompliances = _HwBulkStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 1)
)
_HwBulkStatGroups_ObjectIdentity = ObjectIdentity
hwBulkStatGroups = _HwBulkStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 2)
)

# Managed Objects groups

hwBulkStatObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 2, 1)
)
hwBulkStatObjectGroup.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatEnable"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatCollectCapability"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineMaxFiles"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFiles"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjects"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatTrapEnable"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTableNextIndex"))
)
if mibBuilder.loadTexts:
    hwBulkStatObjectGroup.setStatus("current")

hwBulkStatsDefineFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 2, 2)
)
hwBulkStatsDefineFileGroup.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileStorage"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileFormat"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileCollectInterval"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferInterval"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileStatus"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferPrimaryURL"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferSecondaryURL"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferRetryTimes"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileRemainTime"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileLastTransferSuccessTime"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileLastTransferFailTime"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileNextObjectIndex"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileRowStatus"))
)
if mibBuilder.loadTexts:
    hwBulkStatsDefineFileGroup.setStatus("current")

hwBulkStatDefineObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 2, 3)
)
hwBulkStatDefineObjectGroup.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectClass"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectOID"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectIndexBegin"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectInstanceNum"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineObjectRowStatus"))
)
if mibBuilder.loadTexts:
    hwBulkStatDefineObjectGroup.setStatus("current")


# Notification objects

hwBulkStatCollectIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2, 1)
)
hwBulkStatCollectIncomplete.setObjects(
    ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName")
)
if mibBuilder.loadTexts:
    hwBulkStatCollectIncomplete.setStatus(
        "current"
    )

hwBulkStatCollectResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2, 2)
)
hwBulkStatCollectResume.setObjects(
    ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName")
)
if mibBuilder.loadTexts:
    hwBulkStatCollectResume.setStatus(
        "current"
    )

hwBulkStatURLConnectionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2, 3)
)
hwBulkStatURLConnectionFail.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferPrimaryURL"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferSecondaryURL"))
)
if mibBuilder.loadTexts:
    hwBulkStatURLConnectionFail.setStatus(
        "current"
    )

hwBulkStatURLConnectionResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2, 4)
)
hwBulkStatURLConnectionResume.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferPrimaryURL"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileTransferSecondaryURL"))
)
if mibBuilder.loadTexts:
    hwBulkStatURLConnectionResume.setStatus(
        "current"
    )

hwBulkStatTransferFileDiscard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 2, 5)
)
hwBulkStatTransferFileDiscard.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileName"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatDefineFileLastTransferFailTime"))
)
if mibBuilder.loadTexts:
    hwBulkStatTransferFileDiscard.setStatus(
        "current"
    )


# Notifications groups

hwBulkStatNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 2, 4)
)
hwBulkStatNotificationGroup.setObjects(
      *(("HUAWEI-BULKSTAT-MIB", "hwBulkStatCollectIncomplete"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatCollectResume"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatURLConnectionFail"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatURLConnectionResume"),
        ("HUAWEI-BULKSTAT-MIB", "hwBulkStatTransferFileDiscard"))
)
if mibBuilder.loadTexts:
    hwBulkStatNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBulkStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 140, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwBulkStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BULKSTAT-MIB",
    **{"hwBulkStat": hwBulkStat,
       "hwBulkStatMibObjects": hwBulkStatMibObjects,
       "hwBulkStatEnable": hwBulkStatEnable,
       "hwBulkStatCollectCapability": hwBulkStatCollectCapability,
       "hwBulkStatDefineMaxFiles": hwBulkStatDefineMaxFiles,
       "hwBulkStatDefineFiles": hwBulkStatDefineFiles,
       "hwBulkStatDefineObjects": hwBulkStatDefineObjects,
       "hwBulkStatTrapEnable": hwBulkStatTrapEnable,
       "hwBulkStatDefineFileTableNextIndex": hwBulkStatDefineFileTableNextIndex,
       "hwBulkStatDefineFileTable": hwBulkStatDefineFileTable,
       "hwBulkStatDefineFileEntry": hwBulkStatDefineFileEntry,
       "hwBulkStatDefineFileIndex": hwBulkStatDefineFileIndex,
       "hwBulkStatDefineFileName": hwBulkStatDefineFileName,
       "hwBulkStatDefineFileStorage": hwBulkStatDefineFileStorage,
       "hwBulkStatDefineFileFormat": hwBulkStatDefineFileFormat,
       "hwBulkStatDefineFileCollectInterval": hwBulkStatDefineFileCollectInterval,
       "hwBulkStatDefineFileTransferInterval": hwBulkStatDefineFileTransferInterval,
       "hwBulkStatDefineFileTransferPrimaryURL": hwBulkStatDefineFileTransferPrimaryURL,
       "hwBulkStatDefineFileTransferSecondaryURL": hwBulkStatDefineFileTransferSecondaryURL,
       "hwBulkStatDefineFileTransferRetryTimes": hwBulkStatDefineFileTransferRetryTimes,
       "hwBulkStatDefineFileRemainTime": hwBulkStatDefineFileRemainTime,
       "hwBulkStatDefineFileStatus": hwBulkStatDefineFileStatus,
       "hwBulkStatDefineFileLastTransferSuccessTime": hwBulkStatDefineFileLastTransferSuccessTime,
       "hwBulkStatDefineFileLastTransferFailTime": hwBulkStatDefineFileLastTransferFailTime,
       "hwBulkStatDefineFileNextObjectIndex": hwBulkStatDefineFileNextObjectIndex,
       "hwBulkStatDefineFileRowStatus": hwBulkStatDefineFileRowStatus,
       "hwBulkStatDefineObjectTable": hwBulkStatDefineObjectTable,
       "hwBulkStatDefineObjectEntry": hwBulkStatDefineObjectEntry,
       "hwBulkStatDefineObjectIndex": hwBulkStatDefineObjectIndex,
       "hwBulkStatDefineObjectClass": hwBulkStatDefineObjectClass,
       "hwBulkStatDefineObjectOID": hwBulkStatDefineObjectOID,
       "hwBulkStatDefineObjectIndexBegin": hwBulkStatDefineObjectIndexBegin,
       "hwBulkStatDefineObjectInstanceNum": hwBulkStatDefineObjectInstanceNum,
       "hwBulkStatDefineObjectRowStatus": hwBulkStatDefineObjectRowStatus,
       "hwBulkStatNotifications": hwBulkStatNotifications,
       "hwBulkStatCollectIncomplete": hwBulkStatCollectIncomplete,
       "hwBulkStatCollectResume": hwBulkStatCollectResume,
       "hwBulkStatURLConnectionFail": hwBulkStatURLConnectionFail,
       "hwBulkStatURLConnectionResume": hwBulkStatURLConnectionResume,
       "hwBulkStatTransferFileDiscard": hwBulkStatTransferFileDiscard,
       "hwBulkStatConformance": hwBulkStatConformance,
       "hwBulkStatCompliances": hwBulkStatCompliances,
       "hwBulkStatCompliance": hwBulkStatCompliance,
       "hwBulkStatGroups": hwBulkStatGroups,
       "hwBulkStatObjectGroup": hwBulkStatObjectGroup,
       "hwBulkStatsDefineFileGroup": hwBulkStatsDefineFileGroup,
       "hwBulkStatDefineObjectGroup": hwBulkStatDefineObjectGroup,
       "hwBulkStatNotificationGroup": hwBulkStatNotificationGroup}
)
