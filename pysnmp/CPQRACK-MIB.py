# SNMP MIB module (CPQRACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQRACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:47 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqRackInfo_ObjectIdentity = ObjectIdentity
cpqRackInfo = _CpqRackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22)
)
_CpqRackMibRev_ObjectIdentity = ObjectIdentity
cpqRackMibRev = _CpqRackMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 1)
)


class _CpqRackMibRevMajor_Type(Integer32):
    """Custom type cpqRackMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqRackMibRevMajor_Type.__name__ = "Integer32"
_CpqRackMibRevMajor_Object = MibScalar
cpqRackMibRevMajor = _CpqRackMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 1, 1),
    _CpqRackMibRevMajor_Type()
)
cpqRackMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackMibRevMajor.setStatus("mandatory")


class _CpqRackMibRevMinor_Type(Integer32):
    """Custom type cpqRackMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqRackMibRevMinor_Type.__name__ = "Integer32"
_CpqRackMibRevMinor_Object = MibScalar
cpqRackMibRevMinor = _CpqRackMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 1, 2),
    _CpqRackMibRevMinor_Type()
)
cpqRackMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackMibRevMinor.setStatus("mandatory")


class _CpqRackMibCondition_Type(Integer32):
    """Custom type cpqRackMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackMibCondition_Type.__name__ = "Integer32"
_CpqRackMibCondition_Object = MibScalar
cpqRackMibCondition = _CpqRackMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 1, 3),
    _CpqRackMibCondition_Type()
)
cpqRackMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackMibCondition.setStatus("mandatory")
_CpqRackComponent_ObjectIdentity = ObjectIdentity
cpqRackComponent = _CpqRackComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2)
)
_CpqRackInterface_ObjectIdentity = ObjectIdentity
cpqRackInterface = _CpqRackInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 1)
)
_CpqRackOsCommon_ObjectIdentity = ObjectIdentity
cpqRackOsCommon = _CpqRackOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 1, 4)
)


class _CpqRackOsCommonPollFreq_Type(Integer32):
    """Custom type cpqRackOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqRackOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqRackOsCommonPollFreq_Object = MibScalar
cpqRackOsCommonPollFreq = _CpqRackOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 1, 4, 1),
    _CpqRackOsCommonPollFreq_Type()
)
cpqRackOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackOsCommonPollFreq.setStatus("mandatory")
_CpqRackAsset_ObjectIdentity = ObjectIdentity
cpqRackAsset = _CpqRackAsset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2)
)
_CpqRackAssetTable_Object = MibTable
cpqRackAssetTable = _CpqRackAssetTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqRackAssetTable.setStatus("mandatory")
_CpqRackAssetEntry_Object = MibTableRow
cpqRackAssetEntry = _CpqRackAssetEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1)
)
cpqRackAssetEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackAssetIndex"),
)
if mibBuilder.loadTexts:
    cpqRackAssetEntry.setStatus("mandatory")
_CpqRackAssetIndex_Type = Integer32
_CpqRackAssetIndex_Object = MibTableColumn
cpqRackAssetIndex = _CpqRackAssetIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 1),
    _CpqRackAssetIndex_Type()
)
cpqRackAssetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackAssetIndex.setStatus("mandatory")


class _CpqRackName_Type(DisplayString):
    """Custom type cpqRackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackName_Type.__name__ = "DisplayString"
_CpqRackName_Object = MibTableColumn
cpqRackName = _CpqRackName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 2),
    _CpqRackName_Type()
)
cpqRackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackName.setStatus("mandatory")


class _CpqRackUid_Type(DisplayString):
    """Custom type cpqRackUid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackUid_Type.__name__ = "DisplayString"
_CpqRackUid_Object = MibTableColumn
cpqRackUid = _CpqRackUid_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 3),
    _CpqRackUid_Type()
)
cpqRackUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackUid.setStatus("mandatory")


class _CpqRackSerialNum_Type(DisplayString):
    """Custom type cpqRackSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackSerialNum_Type.__name__ = "DisplayString"
_CpqRackSerialNum_Object = MibTableColumn
cpqRackSerialNum = _CpqRackSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 4),
    _CpqRackSerialNum_Type()
)
cpqRackSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackSerialNum.setStatus("mandatory")
_CpqRackTrapSequenceNum_Type = Integer32
_CpqRackTrapSequenceNum_Object = MibTableColumn
cpqRackTrapSequenceNum = _CpqRackTrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 5),
    _CpqRackTrapSequenceNum_Type()
)
cpqRackTrapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackTrapSequenceNum.setStatus("mandatory")
_CpqRackHeight_Type = Integer32
_CpqRackHeight_Object = MibTableColumn
cpqRackHeight = _CpqRackHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 6),
    _CpqRackHeight_Type()
)
cpqRackHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackHeight.setStatus("mandatory")
_CpqRackWidth_Type = Integer32
_CpqRackWidth_Object = MibTableColumn
cpqRackWidth = _CpqRackWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 7),
    _CpqRackWidth_Type()
)
cpqRackWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackWidth.setStatus("mandatory")
_CpqRackDepth_Type = Integer32
_CpqRackDepth_Object = MibTableColumn
cpqRackDepth = _CpqRackDepth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 2, 1, 1, 8),
    _CpqRackDepth_Type()
)
cpqRackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackDepth.setStatus("mandatory")
_CpqRackEnclosure_ObjectIdentity = ObjectIdentity
cpqRackEnclosure = _CpqRackEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3)
)
_CpqRackCommonEnclosure_ObjectIdentity = ObjectIdentity
cpqRackCommonEnclosure = _CpqRackCommonEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1)
)
_CpqRackCommonEnclosureTable_Object = MibTable
cpqRackCommonEnclosureTable = _CpqRackCommonEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTable.setStatus("mandatory")
_CpqRackCommonEnclosureEntry_Object = MibTableRow
cpqRackCommonEnclosureEntry = _CpqRackCommonEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1)
)
cpqRackCommonEnclosureEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureEntry.setStatus("mandatory")
_CpqRackCommonEnclosureRack_Type = Integer32
_CpqRackCommonEnclosureRack_Object = MibTableColumn
cpqRackCommonEnclosureRack = _CpqRackCommonEnclosureRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 1),
    _CpqRackCommonEnclosureRack_Type()
)
cpqRackCommonEnclosureRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureRack.setStatus("mandatory")
_CpqRackCommonEnclosureIndex_Type = Integer32
_CpqRackCommonEnclosureIndex_Object = MibTableColumn
cpqRackCommonEnclosureIndex = _CpqRackCommonEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 2),
    _CpqRackCommonEnclosureIndex_Type()
)
cpqRackCommonEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureModel_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureModel_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureModel_Object = MibTableColumn
cpqRackCommonEnclosureModel = _CpqRackCommonEnclosureModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 3),
    _CpqRackCommonEnclosureModel_Type()
)
cpqRackCommonEnclosureModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureModel.setStatus("mandatory")


class _CpqRackCommonEnclosureAssetTag_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureAssetTag_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureAssetTag_Object = MibTableColumn
cpqRackCommonEnclosureAssetTag = _CpqRackCommonEnclosureAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 4),
    _CpqRackCommonEnclosureAssetTag_Type()
)
cpqRackCommonEnclosureAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureAssetTag.setStatus("mandatory")


class _CpqRackCommonEnclosurePartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosurePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosurePartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosurePartNumber_Object = MibTableColumn
cpqRackCommonEnclosurePartNumber = _CpqRackCommonEnclosurePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 5),
    _CpqRackCommonEnclosurePartNumber_Type()
)
cpqRackCommonEnclosurePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosurePartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureSparePartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureSparePartNumber_Object = MibTableColumn
cpqRackCommonEnclosureSparePartNumber = _CpqRackCommonEnclosureSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 6),
    _CpqRackCommonEnclosureSparePartNumber_Type()
)
cpqRackCommonEnclosureSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureSparePartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureSerialNum = _CpqRackCommonEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 7),
    _CpqRackCommonEnclosureSerialNum_Type()
)
cpqRackCommonEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureSerialNum.setStatus("mandatory")


class _CpqRackCommonEnclosureFWRev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFWRev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFWRev_Object = MibTableColumn
cpqRackCommonEnclosureFWRev = _CpqRackCommonEnclosureFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 8),
    _CpqRackCommonEnclosureFWRev_Type()
)
cpqRackCommonEnclosureFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFWRev.setStatus("mandatory")


class _CpqRackCommonEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureName = _CpqRackCommonEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 9),
    _CpqRackCommonEnclosureName_Type()
)
cpqRackCommonEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureNeighborNamePrev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureNeighborNamePrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureNeighborNamePrev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureNeighborNamePrev_Object = MibTableColumn
cpqRackCommonEnclosureNeighborNamePrev = _CpqRackCommonEnclosureNeighborNamePrev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 10),
    _CpqRackCommonEnclosureNeighborNamePrev_Type()
)
cpqRackCommonEnclosureNeighborNamePrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureNeighborNamePrev.setStatus("mandatory")


class _CpqRackCommonEnclosureNeighborNameNext_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureNeighborNameNext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureNeighborNameNext_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureNeighborNameNext_Object = MibTableColumn
cpqRackCommonEnclosureNeighborNameNext = _CpqRackCommonEnclosureNeighborNameNext_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 11),
    _CpqRackCommonEnclosureNeighborNameNext_Type()
)
cpqRackCommonEnclosureNeighborNameNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureNeighborNameNext.setStatus("mandatory")
_CpqRackCommonEnclosureHeight_Type = Integer32
_CpqRackCommonEnclosureHeight_Object = MibTableColumn
cpqRackCommonEnclosureHeight = _CpqRackCommonEnclosureHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 12),
    _CpqRackCommonEnclosureHeight_Type()
)
cpqRackCommonEnclosureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHeight.setStatus("mandatory")
_CpqRackCommonEnclosureWidth_Type = Integer32
_CpqRackCommonEnclosureWidth_Object = MibTableColumn
cpqRackCommonEnclosureWidth = _CpqRackCommonEnclosureWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 13),
    _CpqRackCommonEnclosureWidth_Type()
)
cpqRackCommonEnclosureWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureWidth.setStatus("mandatory")
_CpqRackCommonEnclosureDepth_Type = Integer32
_CpqRackCommonEnclosureDepth_Object = MibTableColumn
cpqRackCommonEnclosureDepth = _CpqRackCommonEnclosureDepth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 14),
    _CpqRackCommonEnclosureDepth_Type()
)
cpqRackCommonEnclosureDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureDepth.setStatus("mandatory")
_CpqRackCommonEnclosureTrapSequenceNum_Type = Integer32
_CpqRackCommonEnclosureTrapSequenceNum_Object = MibTableColumn
cpqRackCommonEnclosureTrapSequenceNum = _CpqRackCommonEnclosureTrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 15),
    _CpqRackCommonEnclosureTrapSequenceNum_Type()
)
cpqRackCommonEnclosureTrapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTrapSequenceNum.setStatus("mandatory")


class _CpqRackCommonEnclosureCondition_Type(Integer32):
    """Custom type cpqRackCommonEnclosureCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureCondition_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureCondition_Object = MibTableColumn
cpqRackCommonEnclosureCondition = _CpqRackCommonEnclosureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 16),
    _CpqRackCommonEnclosureCondition_Type()
)
cpqRackCommonEnclosureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureCondition.setStatus("mandatory")


class _CpqRackCommonEnclosureHasServerBlades_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasServerBlades based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasServerBlades_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasServerBlades_Object = MibTableColumn
cpqRackCommonEnclosureHasServerBlades = _CpqRackCommonEnclosureHasServerBlades_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 17),
    _CpqRackCommonEnclosureHasServerBlades_Type()
)
cpqRackCommonEnclosureHasServerBlades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasServerBlades.setStatus("mandatory")


class _CpqRackCommonEnclosureHasPowerSupplies_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasPowerSupplies_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasPowerSupplies_Object = MibTableColumn
cpqRackCommonEnclosureHasPowerSupplies = _CpqRackCommonEnclosureHasPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 18),
    _CpqRackCommonEnclosureHasPowerSupplies_Type()
)
cpqRackCommonEnclosureHasPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasPowerSupplies.setStatus("mandatory")


class _CpqRackCommonEnclosureHasNetConnectors_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasNetConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasNetConnectors_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasNetConnectors_Object = MibTableColumn
cpqRackCommonEnclosureHasNetConnectors = _CpqRackCommonEnclosureHasNetConnectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 19),
    _CpqRackCommonEnclosureHasNetConnectors_Type()
)
cpqRackCommonEnclosureHasNetConnectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasNetConnectors.setStatus("mandatory")


class _CpqRackCommonEnclosureHasTempSensors_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasTempSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasTempSensors_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasTempSensors_Object = MibTableColumn
cpqRackCommonEnclosureHasTempSensors = _CpqRackCommonEnclosureHasTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 20),
    _CpqRackCommonEnclosureHasTempSensors_Type()
)
cpqRackCommonEnclosureHasTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasTempSensors.setStatus("mandatory")


class _CpqRackCommonEnclosureHasFans_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasFans_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasFans_Object = MibTableColumn
cpqRackCommonEnclosureHasFans = _CpqRackCommonEnclosureHasFans_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 21),
    _CpqRackCommonEnclosureHasFans_Type()
)
cpqRackCommonEnclosureHasFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasFans.setStatus("mandatory")


class _CpqRackCommonEnclosureHasFuses_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasFuses_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasFuses_Object = MibTableColumn
cpqRackCommonEnclosureHasFuses = _CpqRackCommonEnclosureHasFuses_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 22),
    _CpqRackCommonEnclosureHasFuses_Type()
)
cpqRackCommonEnclosureHasFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasFuses.setStatus("mandatory")


class _CpqRackCommonEnclosureMgmtUID_Type(Integer32):
    """Custom type cpqRackCommonEnclosureMgmtUID based on Integer32"""
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
        *(("ledOff", 4),
          ("ledOn", 3),
          ("none", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureMgmtUID_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureMgmtUID_Object = MibTableColumn
cpqRackCommonEnclosureMgmtUID = _CpqRackCommonEnclosureMgmtUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 23),
    _CpqRackCommonEnclosureMgmtUID_Type()
)
cpqRackCommonEnclosureMgmtUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureMgmtUID.setStatus("mandatory")


class _CpqRackCommonEnclosureSerialNumPrev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureSerialNumPrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureSerialNumPrev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureSerialNumPrev_Object = MibTableColumn
cpqRackCommonEnclosureSerialNumPrev = _CpqRackCommonEnclosureSerialNumPrev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 24),
    _CpqRackCommonEnclosureSerialNumPrev_Type()
)
cpqRackCommonEnclosureSerialNumPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureSerialNumPrev.setStatus("mandatory")


class _CpqRackCommonEnclosureSerialNumNext_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureSerialNumNext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureSerialNumNext_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureSerialNumNext_Object = MibTableColumn
cpqRackCommonEnclosureSerialNumNext = _CpqRackCommonEnclosureSerialNumNext_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 25),
    _CpqRackCommonEnclosureSerialNumNext_Type()
)
cpqRackCommonEnclosureSerialNumNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureSerialNumNext.setStatus("mandatory")
_CpqRackCommonEnclosureAddress_Type = Integer32
_CpqRackCommonEnclosureAddress_Object = MibTableColumn
cpqRackCommonEnclosureAddress = _CpqRackCommonEnclosureAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 26),
    _CpqRackCommonEnclosureAddress_Type()
)
cpqRackCommonEnclosureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureAddress.setStatus("mandatory")


class _CpqRackCommonEnclosureProductId_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureProductId_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureProductId_Object = MibTableColumn
cpqRackCommonEnclosureProductId = _CpqRackCommonEnclosureProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 27),
    _CpqRackCommonEnclosureProductId_Type()
)
cpqRackCommonEnclosureProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureProductId.setStatus("mandatory")


class _CpqRackCommonEnclosureProductIdPrev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureProductIdPrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureProductIdPrev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureProductIdPrev_Object = MibTableColumn
cpqRackCommonEnclosureProductIdPrev = _CpqRackCommonEnclosureProductIdPrev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 28),
    _CpqRackCommonEnclosureProductIdPrev_Type()
)
cpqRackCommonEnclosureProductIdPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureProductIdPrev.setStatus("mandatory")


class _CpqRackCommonEnclosureProductIdNext_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureProductIdNext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureProductIdNext_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureProductIdNext_Object = MibTableColumn
cpqRackCommonEnclosureProductIdNext = _CpqRackCommonEnclosureProductIdNext_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 29),
    _CpqRackCommonEnclosureProductIdNext_Type()
)
cpqRackCommonEnclosureProductIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureProductIdNext.setStatus("mandatory")


class _CpqRackCommonEnclosureUUID_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureUUID_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureUUID_Object = MibTableColumn
cpqRackCommonEnclosureUUID = _CpqRackCommonEnclosureUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 30),
    _CpqRackCommonEnclosureUUID_Type()
)
cpqRackCommonEnclosureUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureUUID.setStatus("mandatory")


class _CpqRackCommonEnclosureUUIDPrev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureUUIDPrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureUUIDPrev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureUUIDPrev_Object = MibTableColumn
cpqRackCommonEnclosureUUIDPrev = _CpqRackCommonEnclosureUUIDPrev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 31),
    _CpqRackCommonEnclosureUUIDPrev_Type()
)
cpqRackCommonEnclosureUUIDPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureUUIDPrev.setStatus("mandatory")


class _CpqRackCommonEnclosureUUIDNext_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureUUIDNext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureUUIDNext_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureUUIDNext_Object = MibTableColumn
cpqRackCommonEnclosureUUIDNext = _CpqRackCommonEnclosureUUIDNext_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 32),
    _CpqRackCommonEnclosureUUIDNext_Type()
)
cpqRackCommonEnclosureUUIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureUUIDNext.setStatus("mandatory")


class _CpqRackCommonEnclosureHasManagers_Type(Integer32):
    """Custom type cpqRackCommonEnclosureHasManagers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackCommonEnclosureHasManagers_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureHasManagers_Object = MibTableColumn
cpqRackCommonEnclosureHasManagers = _CpqRackCommonEnclosureHasManagers_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 1, 1, 33),
    _CpqRackCommonEnclosureHasManagers_Type()
)
cpqRackCommonEnclosureHasManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureHasManagers.setStatus("mandatory")
_CpqRackCommonEnclosureTempTable_Object = MibTable
cpqRackCommonEnclosureTempTable = _CpqRackCommonEnclosureTempTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempTable.setStatus("mandatory")
_CpqRackCommonEnclosureTempEntry_Object = MibTableRow
cpqRackCommonEnclosureTempEntry = _CpqRackCommonEnclosureTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1)
)
cpqRackCommonEnclosureTempEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureTempRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureTempChassis"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureTempSensorIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempEntry.setStatus("mandatory")
_CpqRackCommonEnclosureTempRack_Type = Integer32
_CpqRackCommonEnclosureTempRack_Object = MibTableColumn
cpqRackCommonEnclosureTempRack = _CpqRackCommonEnclosureTempRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 1),
    _CpqRackCommonEnclosureTempRack_Type()
)
cpqRackCommonEnclosureTempRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempRack.setStatus("mandatory")
_CpqRackCommonEnclosureTempChassis_Type = Integer32
_CpqRackCommonEnclosureTempChassis_Object = MibTableColumn
cpqRackCommonEnclosureTempChassis = _CpqRackCommonEnclosureTempChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 2),
    _CpqRackCommonEnclosureTempChassis_Type()
)
cpqRackCommonEnclosureTempChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempChassis.setStatus("mandatory")
_CpqRackCommonEnclosureTempSensorIndex_Type = Integer32
_CpqRackCommonEnclosureTempSensorIndex_Object = MibTableColumn
cpqRackCommonEnclosureTempSensorIndex = _CpqRackCommonEnclosureTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 3),
    _CpqRackCommonEnclosureTempSensorIndex_Type()
)
cpqRackCommonEnclosureTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempSensorIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureTempSensorEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureTempSensorEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureTempSensorEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureTempSensorEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureTempSensorEnclosureName = _CpqRackCommonEnclosureTempSensorEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 4),
    _CpqRackCommonEnclosureTempSensorEnclosureName_Type()
)
cpqRackCommonEnclosureTempSensorEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempSensorEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureTempLocation_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureTempLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureTempLocation_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureTempLocation_Object = MibTableColumn
cpqRackCommonEnclosureTempLocation = _CpqRackCommonEnclosureTempLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 5),
    _CpqRackCommonEnclosureTempLocation_Type()
)
cpqRackCommonEnclosureTempLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempLocation.setStatus("mandatory")
_CpqRackCommonEnclosureTempCurrent_Type = Integer32
_CpqRackCommonEnclosureTempCurrent_Object = MibTableColumn
cpqRackCommonEnclosureTempCurrent = _CpqRackCommonEnclosureTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 6),
    _CpqRackCommonEnclosureTempCurrent_Type()
)
cpqRackCommonEnclosureTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempCurrent.setStatus("mandatory")
_CpqRackCommonEnclosureTempThreshold_Type = Integer32
_CpqRackCommonEnclosureTempThreshold_Object = MibTableColumn
cpqRackCommonEnclosureTempThreshold = _CpqRackCommonEnclosureTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 7),
    _CpqRackCommonEnclosureTempThreshold_Type()
)
cpqRackCommonEnclosureTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempThreshold.setStatus("mandatory")


class _CpqRackCommonEnclosureTempCondition_Type(Integer32):
    """Custom type cpqRackCommonEnclosureTempCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureTempCondition_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureTempCondition_Object = MibTableColumn
cpqRackCommonEnclosureTempCondition = _CpqRackCommonEnclosureTempCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 8),
    _CpqRackCommonEnclosureTempCondition_Type()
)
cpqRackCommonEnclosureTempCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempCondition.setStatus("mandatory")


class _CpqRackCommonEnclosureTempType_Type(Integer32):
    """Custom type cpqRackCommonEnclosureTempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("blowout", 5),
          ("caution", 9),
          ("critical", 15),
          ("other", 1))
    )


_CpqRackCommonEnclosureTempType_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureTempType_Object = MibTableColumn
cpqRackCommonEnclosureTempType = _CpqRackCommonEnclosureTempType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 9),
    _CpqRackCommonEnclosureTempType_Type()
)
cpqRackCommonEnclosureTempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempType.setStatus("mandatory")


class _CpqRackCommonEnclosureTempSensorEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureTempSensorEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureTempSensorEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureTempSensorEnclosureSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureTempSensorEnclosureSerialNum = _CpqRackCommonEnclosureTempSensorEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 2, 1, 10),
    _CpqRackCommonEnclosureTempSensorEnclosureSerialNum_Type()
)
cpqRackCommonEnclosureTempSensorEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureTempSensorEnclosureSerialNum.setStatus("mandatory")
_CpqRackCommonEnclosureFanTable_Object = MibTable
cpqRackCommonEnclosureFanTable = _CpqRackCommonEnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanTable.setStatus("mandatory")
_CpqRackCommonEnclosureFanEntry_Object = MibTableRow
cpqRackCommonEnclosureFanEntry = _CpqRackCommonEnclosureFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1)
)
cpqRackCommonEnclosureFanEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFanRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFanChassis"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFanIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanEntry.setStatus("mandatory")
_CpqRackCommonEnclosureFanRack_Type = Integer32
_CpqRackCommonEnclosureFanRack_Object = MibTableColumn
cpqRackCommonEnclosureFanRack = _CpqRackCommonEnclosureFanRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 1),
    _CpqRackCommonEnclosureFanRack_Type()
)
cpqRackCommonEnclosureFanRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanRack.setStatus("mandatory")
_CpqRackCommonEnclosureFanChassis_Type = Integer32
_CpqRackCommonEnclosureFanChassis_Object = MibTableColumn
cpqRackCommonEnclosureFanChassis = _CpqRackCommonEnclosureFanChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 2),
    _CpqRackCommonEnclosureFanChassis_Type()
)
cpqRackCommonEnclosureFanChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanChassis.setStatus("mandatory")
_CpqRackCommonEnclosureFanIndex_Type = Integer32
_CpqRackCommonEnclosureFanIndex_Object = MibTableColumn
cpqRackCommonEnclosureFanIndex = _CpqRackCommonEnclosureFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 3),
    _CpqRackCommonEnclosureFanIndex_Type()
)
cpqRackCommonEnclosureFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureFanEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFanEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFanEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFanEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureFanEnclosureName = _CpqRackCommonEnclosureFanEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 4),
    _CpqRackCommonEnclosureFanEnclosureName_Type()
)
cpqRackCommonEnclosureFanEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureFanLocation_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFanLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFanLocation_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFanLocation_Object = MibTableColumn
cpqRackCommonEnclosureFanLocation = _CpqRackCommonEnclosureFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 5),
    _CpqRackCommonEnclosureFanLocation_Type()
)
cpqRackCommonEnclosureFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanLocation.setStatus("mandatory")


class _CpqRackCommonEnclosureFanPartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFanPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFanPartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFanPartNumber_Object = MibTableColumn
cpqRackCommonEnclosureFanPartNumber = _CpqRackCommonEnclosureFanPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 6),
    _CpqRackCommonEnclosureFanPartNumber_Type()
)
cpqRackCommonEnclosureFanPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanPartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureFanSparePartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFanSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFanSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFanSparePartNumber_Object = MibTableColumn
cpqRackCommonEnclosureFanSparePartNumber = _CpqRackCommonEnclosureFanSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 7),
    _CpqRackCommonEnclosureFanSparePartNumber_Type()
)
cpqRackCommonEnclosureFanSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanSparePartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureFanPresent_Type(Integer32):
    """Custom type cpqRackCommonEnclosureFanPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackCommonEnclosureFanPresent_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureFanPresent_Object = MibTableColumn
cpqRackCommonEnclosureFanPresent = _CpqRackCommonEnclosureFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 8),
    _CpqRackCommonEnclosureFanPresent_Type()
)
cpqRackCommonEnclosureFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanPresent.setStatus("mandatory")


class _CpqRackCommonEnclosureFanRedundant_Type(Integer32):
    """Custom type cpqRackCommonEnclosureFanRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqRackCommonEnclosureFanRedundant_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureFanRedundant_Object = MibTableColumn
cpqRackCommonEnclosureFanRedundant = _CpqRackCommonEnclosureFanRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 9),
    _CpqRackCommonEnclosureFanRedundant_Type()
)
cpqRackCommonEnclosureFanRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanRedundant.setStatus("mandatory")
_CpqRackCommonEnclosureFanRedundantGroupId_Type = Integer32
_CpqRackCommonEnclosureFanRedundantGroupId_Object = MibTableColumn
cpqRackCommonEnclosureFanRedundantGroupId = _CpqRackCommonEnclosureFanRedundantGroupId_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 10),
    _CpqRackCommonEnclosureFanRedundantGroupId_Type()
)
cpqRackCommonEnclosureFanRedundantGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanRedundantGroupId.setStatus("mandatory")


class _CpqRackCommonEnclosureFanCondition_Type(Integer32):
    """Custom type cpqRackCommonEnclosureFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureFanCondition_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureFanCondition_Object = MibTableColumn
cpqRackCommonEnclosureFanCondition = _CpqRackCommonEnclosureFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 11),
    _CpqRackCommonEnclosureFanCondition_Type()
)
cpqRackCommonEnclosureFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanCondition.setStatus("mandatory")


class _CpqRackCommonEnclosureFanEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFanEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFanEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFanEnclosureSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureFanEnclosureSerialNum = _CpqRackCommonEnclosureFanEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 3, 1, 12),
    _CpqRackCommonEnclosureFanEnclosureSerialNum_Type()
)
cpqRackCommonEnclosureFanEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFanEnclosureSerialNum.setStatus("mandatory")
_CpqRackCommonEnclosureFuseTable_Object = MibTable
cpqRackCommonEnclosureFuseTable = _CpqRackCommonEnclosureFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseTable.setStatus("mandatory")
_CpqRackCommonEnclosureFuseEntry_Object = MibTableRow
cpqRackCommonEnclosureFuseEntry = _CpqRackCommonEnclosureFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1)
)
cpqRackCommonEnclosureFuseEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFuseRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFuseChassis"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFuseIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseEntry.setStatus("mandatory")
_CpqRackCommonEnclosureFuseRack_Type = Integer32
_CpqRackCommonEnclosureFuseRack_Object = MibTableColumn
cpqRackCommonEnclosureFuseRack = _CpqRackCommonEnclosureFuseRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 1),
    _CpqRackCommonEnclosureFuseRack_Type()
)
cpqRackCommonEnclosureFuseRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseRack.setStatus("mandatory")
_CpqRackCommonEnclosureFuseChassis_Type = Integer32
_CpqRackCommonEnclosureFuseChassis_Object = MibTableColumn
cpqRackCommonEnclosureFuseChassis = _CpqRackCommonEnclosureFuseChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 2),
    _CpqRackCommonEnclosureFuseChassis_Type()
)
cpqRackCommonEnclosureFuseChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseChassis.setStatus("mandatory")
_CpqRackCommonEnclosureFuseIndex_Type = Integer32
_CpqRackCommonEnclosureFuseIndex_Object = MibTableColumn
cpqRackCommonEnclosureFuseIndex = _CpqRackCommonEnclosureFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 3),
    _CpqRackCommonEnclosureFuseIndex_Type()
)
cpqRackCommonEnclosureFuseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureFuseEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFuseEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFuseEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFuseEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureFuseEnclosureName = _CpqRackCommonEnclosureFuseEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 4),
    _CpqRackCommonEnclosureFuseEnclosureName_Type()
)
cpqRackCommonEnclosureFuseEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureFuseLocation_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFuseLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFuseLocation_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFuseLocation_Object = MibTableColumn
cpqRackCommonEnclosureFuseLocation = _CpqRackCommonEnclosureFuseLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 5),
    _CpqRackCommonEnclosureFuseLocation_Type()
)
cpqRackCommonEnclosureFuseLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseLocation.setStatus("mandatory")


class _CpqRackCommonEnclosureFusePresent_Type(Integer32):
    """Custom type cpqRackCommonEnclosureFusePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackCommonEnclosureFusePresent_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureFusePresent_Object = MibTableColumn
cpqRackCommonEnclosureFusePresent = _CpqRackCommonEnclosureFusePresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 6),
    _CpqRackCommonEnclosureFusePresent_Type()
)
cpqRackCommonEnclosureFusePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFusePresent.setStatus("mandatory")


class _CpqRackCommonEnclosureFuseCondition_Type(Integer32):
    """Custom type cpqRackCommonEnclosureFuseCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureFuseCondition_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureFuseCondition_Object = MibTableColumn
cpqRackCommonEnclosureFuseCondition = _CpqRackCommonEnclosureFuseCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 4, 1, 7),
    _CpqRackCommonEnclosureFuseCondition_Type()
)
cpqRackCommonEnclosureFuseCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFuseCondition.setStatus("mandatory")
_CpqRackCommonEnclosureFruTable_Object = MibTable
cpqRackCommonEnclosureFruTable = _CpqRackCommonEnclosureFruTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruTable.setStatus("mandatory")
_CpqRackCommonEnclosureFruEntry_Object = MibTableRow
cpqRackCommonEnclosureFruEntry = _CpqRackCommonEnclosureFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1)
)
cpqRackCommonEnclosureFruEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFruRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFruChassis"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureFruIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruEntry.setStatus("mandatory")
_CpqRackCommonEnclosureFruRack_Type = Integer32
_CpqRackCommonEnclosureFruRack_Object = MibTableColumn
cpqRackCommonEnclosureFruRack = _CpqRackCommonEnclosureFruRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 1),
    _CpqRackCommonEnclosureFruRack_Type()
)
cpqRackCommonEnclosureFruRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruRack.setStatus("mandatory")
_CpqRackCommonEnclosureFruChassis_Type = Integer32
_CpqRackCommonEnclosureFruChassis_Object = MibTableColumn
cpqRackCommonEnclosureFruChassis = _CpqRackCommonEnclosureFruChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 2),
    _CpqRackCommonEnclosureFruChassis_Type()
)
cpqRackCommonEnclosureFruChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruChassis.setStatus("mandatory")
_CpqRackCommonEnclosureFruIndex_Type = Integer32
_CpqRackCommonEnclosureFruIndex_Object = MibTableColumn
cpqRackCommonEnclosureFruIndex = _CpqRackCommonEnclosureFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 3),
    _CpqRackCommonEnclosureFruIndex_Type()
)
cpqRackCommonEnclosureFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureFruEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureFruEnclosureName = _CpqRackCommonEnclosureFruEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 4),
    _CpqRackCommonEnclosureFruEnclosureName_Type()
)
cpqRackCommonEnclosureFruEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureFruDescription_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruDescription_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruDescription_Object = MibTableColumn
cpqRackCommonEnclosureFruDescription = _CpqRackCommonEnclosureFruDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 5),
    _CpqRackCommonEnclosureFruDescription_Type()
)
cpqRackCommonEnclosureFruDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruDescription.setStatus("mandatory")


class _CpqRackCommonEnclosureFruLocation_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruLocation_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruLocation_Object = MibTableColumn
cpqRackCommonEnclosureFruLocation = _CpqRackCommonEnclosureFruLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 6),
    _CpqRackCommonEnclosureFruLocation_Type()
)
cpqRackCommonEnclosureFruLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruLocation.setStatus("mandatory")


class _CpqRackCommonEnclosureFruAssemblyPartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruAssemblyPartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruAssemblyPartNumber_Object = MibTableColumn
cpqRackCommonEnclosureFruAssemblyPartNumber = _CpqRackCommonEnclosureFruAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 7),
    _CpqRackCommonEnclosureFruAssemblyPartNumber_Type()
)
cpqRackCommonEnclosureFruAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruAssemblyPartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureFruSparePartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruSparePartNumber_Object = MibTableColumn
cpqRackCommonEnclosureFruSparePartNumber = _CpqRackCommonEnclosureFruSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 8),
    _CpqRackCommonEnclosureFruSparePartNumber_Type()
)
cpqRackCommonEnclosureFruSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruSparePartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureFruAutoRev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruAutoRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruAutoRev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruAutoRev_Object = MibTableColumn
cpqRackCommonEnclosureFruAutoRev = _CpqRackCommonEnclosureFruAutoRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 9),
    _CpqRackCommonEnclosureFruAutoRev_Type()
)
cpqRackCommonEnclosureFruAutoRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruAutoRev.setStatus("mandatory")


class _CpqRackCommonEnclosureFruSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureFruSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureFruSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureFruSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureFruSerialNum = _CpqRackCommonEnclosureFruSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 5, 1, 10),
    _CpqRackCommonEnclosureFruSerialNum_Type()
)
cpqRackCommonEnclosureFruSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureFruSerialNum.setStatus("mandatory")
_CpqRackCommonEnclosureManagerTable_Object = MibTable
cpqRackCommonEnclosureManagerTable = _CpqRackCommonEnclosureManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerTable.setStatus("mandatory")
_CpqRackCommonEnclosureManagerEntry_Object = MibTableRow
cpqRackCommonEnclosureManagerEntry = _CpqRackCommonEnclosureManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1)
)
cpqRackCommonEnclosureManagerEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureManagerRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureManagerChassis"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureManagerIndex"),
)
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerEntry.setStatus("mandatory")
_CpqRackCommonEnclosureManagerRack_Type = Integer32
_CpqRackCommonEnclosureManagerRack_Object = MibTableColumn
cpqRackCommonEnclosureManagerRack = _CpqRackCommonEnclosureManagerRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 1),
    _CpqRackCommonEnclosureManagerRack_Type()
)
cpqRackCommonEnclosureManagerRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerRack.setStatus("mandatory")
_CpqRackCommonEnclosureManagerChassis_Type = Integer32
_CpqRackCommonEnclosureManagerChassis_Object = MibTableColumn
cpqRackCommonEnclosureManagerChassis = _CpqRackCommonEnclosureManagerChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 2),
    _CpqRackCommonEnclosureManagerChassis_Type()
)
cpqRackCommonEnclosureManagerChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerChassis.setStatus("mandatory")
_CpqRackCommonEnclosureManagerIndex_Type = Integer32
_CpqRackCommonEnclosureManagerIndex_Object = MibTableColumn
cpqRackCommonEnclosureManagerIndex = _CpqRackCommonEnclosureManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 3),
    _CpqRackCommonEnclosureManagerIndex_Type()
)
cpqRackCommonEnclosureManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerIndex.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerEnclosureName_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerEnclosureName_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerEnclosureName_Object = MibTableColumn
cpqRackCommonEnclosureManagerEnclosureName = _CpqRackCommonEnclosureManagerEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 4),
    _CpqRackCommonEnclosureManagerEnclosureName_Type()
)
cpqRackCommonEnclosureManagerEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerEnclosureName.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerLocation_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerLocation_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerLocation_Object = MibTableColumn
cpqRackCommonEnclosureManagerLocation = _CpqRackCommonEnclosureManagerLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 5),
    _CpqRackCommonEnclosureManagerLocation_Type()
)
cpqRackCommonEnclosureManagerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerLocation.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerPartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerPartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerPartNumber_Object = MibTableColumn
cpqRackCommonEnclosureManagerPartNumber = _CpqRackCommonEnclosureManagerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 6),
    _CpqRackCommonEnclosureManagerPartNumber_Type()
)
cpqRackCommonEnclosureManagerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerPartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerSparePartNumber_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerSparePartNumber_Object = MibTableColumn
cpqRackCommonEnclosureManagerSparePartNumber = _CpqRackCommonEnclosureManagerSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 7),
    _CpqRackCommonEnclosureManagerSparePartNumber_Type()
)
cpqRackCommonEnclosureManagerSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerSparePartNumber.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureManagerSerialNum = _CpqRackCommonEnclosureManagerSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 8),
    _CpqRackCommonEnclosureManagerSerialNum_Type()
)
cpqRackCommonEnclosureManagerSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerSerialNum.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerRole_Type(Integer32):
    """Custom type cpqRackCommonEnclosureManagerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1))
    )


_CpqRackCommonEnclosureManagerRole_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureManagerRole_Object = MibTableColumn
cpqRackCommonEnclosureManagerRole = _CpqRackCommonEnclosureManagerRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 9),
    _CpqRackCommonEnclosureManagerRole_Type()
)
cpqRackCommonEnclosureManagerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerRole.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerPresent_Type(Integer32):
    """Custom type cpqRackCommonEnclosureManagerPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackCommonEnclosureManagerPresent_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureManagerPresent_Object = MibTableColumn
cpqRackCommonEnclosureManagerPresent = _CpqRackCommonEnclosureManagerPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 10),
    _CpqRackCommonEnclosureManagerPresent_Type()
)
cpqRackCommonEnclosureManagerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerPresent.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerRedundant_Type(Integer32):
    """Custom type cpqRackCommonEnclosureManagerRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqRackCommonEnclosureManagerRedundant_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureManagerRedundant_Object = MibTableColumn
cpqRackCommonEnclosureManagerRedundant = _CpqRackCommonEnclosureManagerRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 11),
    _CpqRackCommonEnclosureManagerRedundant_Type()
)
cpqRackCommonEnclosureManagerRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerRedundant.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerCondition_Type(Integer32):
    """Custom type cpqRackCommonEnclosureManagerCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackCommonEnclosureManagerCondition_Type.__name__ = "Integer32"
_CpqRackCommonEnclosureManagerCondition_Object = MibTableColumn
cpqRackCommonEnclosureManagerCondition = _CpqRackCommonEnclosureManagerCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 12),
    _CpqRackCommonEnclosureManagerCondition_Type()
)
cpqRackCommonEnclosureManagerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerCondition.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerEnclosureSerialNum_Object = MibTableColumn
cpqRackCommonEnclosureManagerEnclosureSerialNum = _CpqRackCommonEnclosureManagerEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 13),
    _CpqRackCommonEnclosureManagerEnclosureSerialNum_Type()
)
cpqRackCommonEnclosureManagerEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerEnclosureSerialNum.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerUUID_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerUUID_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerUUID_Object = MibTableColumn
cpqRackCommonEnclosureManagerUUID = _CpqRackCommonEnclosureManagerUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 14),
    _CpqRackCommonEnclosureManagerUUID_Type()
)
cpqRackCommonEnclosureManagerUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerUUID.setStatus("mandatory")


class _CpqRackCommonEnclosureManagerFWRev_Type(DisplayString):
    """Custom type cpqRackCommonEnclosureManagerFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackCommonEnclosureManagerFWRev_Type.__name__ = "DisplayString"
_CpqRackCommonEnclosureManagerFWRev_Object = MibTableColumn
cpqRackCommonEnclosureManagerFWRev = _CpqRackCommonEnclosureManagerFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 1, 6, 1, 15),
    _CpqRackCommonEnclosureManagerFWRev_Type()
)
cpqRackCommonEnclosureManagerFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackCommonEnclosureManagerFWRev.setStatus("mandatory")
_CpqRackServerEnclosure_ObjectIdentity = ObjectIdentity
cpqRackServerEnclosure = _CpqRackServerEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2)
)
_CpqRackServerEnclosureTable_Object = MibTable
cpqRackServerEnclosureTable = _CpqRackServerEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cpqRackServerEnclosureTable.setStatus("mandatory")
_CpqRackServerEnclosureEntry_Object = MibTableRow
cpqRackServerEnclosureEntry = _CpqRackServerEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1)
)
cpqRackServerEnclosureEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackServerEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackServerEnclosureIndex"),
)
if mibBuilder.loadTexts:
    cpqRackServerEnclosureEntry.setStatus("mandatory")
_CpqRackServerEnclosureRack_Type = Integer32
_CpqRackServerEnclosureRack_Object = MibTableColumn
cpqRackServerEnclosureRack = _CpqRackServerEnclosureRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 1),
    _CpqRackServerEnclosureRack_Type()
)
cpqRackServerEnclosureRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureRack.setStatus("mandatory")
_CpqRackServerEnclosureIndex_Type = Integer32
_CpqRackServerEnclosureIndex_Object = MibTableColumn
cpqRackServerEnclosureIndex = _CpqRackServerEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 2),
    _CpqRackServerEnclosureIndex_Type()
)
cpqRackServerEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureIndex.setStatus("mandatory")


class _CpqRackServerEnclosureName_Type(DisplayString):
    """Custom type cpqRackServerEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerEnclosureName_Type.__name__ = "DisplayString"
_CpqRackServerEnclosureName_Object = MibTableColumn
cpqRackServerEnclosureName = _CpqRackServerEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 3),
    _CpqRackServerEnclosureName_Type()
)
cpqRackServerEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureName.setStatus("mandatory")
_CpqRackServerEnclosureMaxNumBlades_Type = Integer32
_CpqRackServerEnclosureMaxNumBlades_Object = MibTableColumn
cpqRackServerEnclosureMaxNumBlades = _CpqRackServerEnclosureMaxNumBlades_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 4),
    _CpqRackServerEnclosureMaxNumBlades_Type()
)
cpqRackServerEnclosureMaxNumBlades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureMaxNumBlades.setStatus("mandatory")
_CpqRackServerEnclosureMaxNumBladesX_Type = Integer32
_CpqRackServerEnclosureMaxNumBladesX_Object = MibTableColumn
cpqRackServerEnclosureMaxNumBladesX = _CpqRackServerEnclosureMaxNumBladesX_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 5),
    _CpqRackServerEnclosureMaxNumBladesX_Type()
)
cpqRackServerEnclosureMaxNumBladesX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureMaxNumBladesX.setStatus("mandatory")
_CpqRackServerEnclosureMaxNumBladesY_Type = Integer32
_CpqRackServerEnclosureMaxNumBladesY_Object = MibTableColumn
cpqRackServerEnclosureMaxNumBladesY = _CpqRackServerEnclosureMaxNumBladesY_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 2, 1, 1, 6),
    _CpqRackServerEnclosureMaxNumBladesY_Type()
)
cpqRackServerEnclosureMaxNumBladesY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerEnclosureMaxNumBladesY.setStatus("mandatory")
_CpqRackPowerEnclosure_ObjectIdentity = ObjectIdentity
cpqRackPowerEnclosure = _CpqRackPowerEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3)
)
_CpqRackPowerEnclosureTable_Object = MibTable
cpqRackPowerEnclosureTable = _CpqRackPowerEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureTable.setStatus("mandatory")
_CpqRackPowerEnclosureEntry_Object = MibTableRow
cpqRackPowerEnclosureEntry = _CpqRackPowerEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1)
)
cpqRackPowerEnclosureEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackPowerEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackPowerEnclosureIndex"),
)
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureEntry.setStatus("mandatory")
_CpqRackPowerEnclosureRack_Type = Integer32
_CpqRackPowerEnclosureRack_Object = MibTableColumn
cpqRackPowerEnclosureRack = _CpqRackPowerEnclosureRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 1),
    _CpqRackPowerEnclosureRack_Type()
)
cpqRackPowerEnclosureRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureRack.setStatus("mandatory")
_CpqRackPowerEnclosureIndex_Type = Integer32
_CpqRackPowerEnclosureIndex_Object = MibTableColumn
cpqRackPowerEnclosureIndex = _CpqRackPowerEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 2),
    _CpqRackPowerEnclosureIndex_Type()
)
cpqRackPowerEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureIndex.setStatus("mandatory")


class _CpqRackPowerEnclosureName_Type(DisplayString):
    """Custom type cpqRackPowerEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerEnclosureName_Type.__name__ = "DisplayString"
_CpqRackPowerEnclosureName_Object = MibTableColumn
cpqRackPowerEnclosureName = _CpqRackPowerEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 3),
    _CpqRackPowerEnclosureName_Type()
)
cpqRackPowerEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureName.setStatus("mandatory")


class _CpqRackPowerEnclosureMgmtBoardSerialNum_Type(DisplayString):
    """Custom type cpqRackPowerEnclosureMgmtBoardSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerEnclosureMgmtBoardSerialNum_Type.__name__ = "DisplayString"
_CpqRackPowerEnclosureMgmtBoardSerialNum_Object = MibTableColumn
cpqRackPowerEnclosureMgmtBoardSerialNum = _CpqRackPowerEnclosureMgmtBoardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 4),
    _CpqRackPowerEnclosureMgmtBoardSerialNum_Type()
)
cpqRackPowerEnclosureMgmtBoardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureMgmtBoardSerialNum.setStatus("mandatory")


class _CpqRackPowerEnclosureRedundant_Type(Integer32):
    """Custom type cpqRackPowerEnclosureRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqRackPowerEnclosureRedundant_Type.__name__ = "Integer32"
_CpqRackPowerEnclosureRedundant_Object = MibTableColumn
cpqRackPowerEnclosureRedundant = _CpqRackPowerEnclosureRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 5),
    _CpqRackPowerEnclosureRedundant_Type()
)
cpqRackPowerEnclosureRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureRedundant.setStatus("mandatory")


class _CpqRackPowerEnclosureLoadBalanced_Type(Integer32):
    """Custom type cpqRackPowerEnclosureLoadBalanced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadBalanced", 3),
          ("notLoadBalanced", 2),
          ("other", 1))
    )


_CpqRackPowerEnclosureLoadBalanced_Type.__name__ = "Integer32"
_CpqRackPowerEnclosureLoadBalanced_Object = MibTableColumn
cpqRackPowerEnclosureLoadBalanced = _CpqRackPowerEnclosureLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 6),
    _CpqRackPowerEnclosureLoadBalanced_Type()
)
cpqRackPowerEnclosureLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureLoadBalanced.setStatus("mandatory")


class _CpqRackPowerEnclosureInputPwrType_Type(Integer32):
    """Custom type cpqRackPowerEnclosureInputPwrType based on Integer32"""
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
        *(("directCurrent", 4),
          ("other", 1),
          ("singlePhase", 2),
          ("threePhase", 3))
    )


_CpqRackPowerEnclosureInputPwrType_Type.__name__ = "Integer32"
_CpqRackPowerEnclosureInputPwrType_Object = MibTableColumn
cpqRackPowerEnclosureInputPwrType = _CpqRackPowerEnclosureInputPwrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 7),
    _CpqRackPowerEnclosureInputPwrType_Type()
)
cpqRackPowerEnclosureInputPwrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureInputPwrType.setStatus("mandatory")
_CpqRackPowerEnclosurePwrFeedMax_Type = Integer32
_CpqRackPowerEnclosurePwrFeedMax_Object = MibTableColumn
cpqRackPowerEnclosurePwrFeedMax = _CpqRackPowerEnclosurePwrFeedMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 8),
    _CpqRackPowerEnclosurePwrFeedMax_Type()
)
cpqRackPowerEnclosurePwrFeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosurePwrFeedMax.setStatus("mandatory")


class _CpqRackPowerEnclosureCondition_Type(Integer32):
    """Custom type cpqRackPowerEnclosureCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackPowerEnclosureCondition_Type.__name__ = "Integer32"
_CpqRackPowerEnclosureCondition_Object = MibTableColumn
cpqRackPowerEnclosureCondition = _CpqRackPowerEnclosureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 9),
    _CpqRackPowerEnclosureCondition_Type()
)
cpqRackPowerEnclosureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureCondition.setStatus("mandatory")


class _CpqRackPowerEnclosureBladeAutopoweron_Type(Integer32):
    """Custom type cpqRackPowerEnclosureBladeAutopoweron based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqRackPowerEnclosureBladeAutopoweron_Type.__name__ = "Integer32"
_CpqRackPowerEnclosureBladeAutopoweron_Object = MibTableColumn
cpqRackPowerEnclosureBladeAutopoweron = _CpqRackPowerEnclosureBladeAutopoweron_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 3, 3, 1, 1, 10),
    _CpqRackPowerEnclosureBladeAutopoweron_Type()
)
cpqRackPowerEnclosureBladeAutopoweron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackPowerEnclosureBladeAutopoweron.setStatus("optional")
_CpqRackServer_ObjectIdentity = ObjectIdentity
cpqRackServer = _CpqRackServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4)
)
_CpqRackServerBlade_ObjectIdentity = ObjectIdentity
cpqRackServerBlade = _CpqRackServerBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1)
)
_CpqRackServerBladeTable_Object = MibTable
cpqRackServerBladeTable = _CpqRackServerBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cpqRackServerBladeTable.setStatus("mandatory")
_CpqRackServerBladeEntry_Object = MibTableRow
cpqRackServerBladeEntry = _CpqRackServerBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1)
)
cpqRackServerBladeEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackServerBladeRack"),
    (0, "CPQRACK-MIB", "cpqRackServerBladeChassis"),
    (0, "CPQRACK-MIB", "cpqRackServerBladeIndex"),
)
if mibBuilder.loadTexts:
    cpqRackServerBladeEntry.setStatus("mandatory")
_CpqRackServerBladeRack_Type = Integer32
_CpqRackServerBladeRack_Object = MibTableColumn
cpqRackServerBladeRack = _CpqRackServerBladeRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 1),
    _CpqRackServerBladeRack_Type()
)
cpqRackServerBladeRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeRack.setStatus("mandatory")
_CpqRackServerBladeChassis_Type = Integer32
_CpqRackServerBladeChassis_Object = MibTableColumn
cpqRackServerBladeChassis = _CpqRackServerBladeChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 2),
    _CpqRackServerBladeChassis_Type()
)
cpqRackServerBladeChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeChassis.setStatus("mandatory")
_CpqRackServerBladeIndex_Type = Integer32
_CpqRackServerBladeIndex_Object = MibTableColumn
cpqRackServerBladeIndex = _CpqRackServerBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 3),
    _CpqRackServerBladeIndex_Type()
)
cpqRackServerBladeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeIndex.setStatus("mandatory")


class _CpqRackServerBladeName_Type(DisplayString):
    """Custom type cpqRackServerBladeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeName_Type.__name__ = "DisplayString"
_CpqRackServerBladeName_Object = MibTableColumn
cpqRackServerBladeName = _CpqRackServerBladeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 4),
    _CpqRackServerBladeName_Type()
)
cpqRackServerBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeName.setStatus("mandatory")


class _CpqRackServerBladeEnclosureName_Type(DisplayString):
    """Custom type cpqRackServerBladeEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeEnclosureName_Type.__name__ = "DisplayString"
_CpqRackServerBladeEnclosureName_Object = MibTableColumn
cpqRackServerBladeEnclosureName = _CpqRackServerBladeEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 5),
    _CpqRackServerBladeEnclosureName_Type()
)
cpqRackServerBladeEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeEnclosureName.setStatus("mandatory")


class _CpqRackServerBladePartNumber_Type(DisplayString):
    """Custom type cpqRackServerBladePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladePartNumber_Type.__name__ = "DisplayString"
_CpqRackServerBladePartNumber_Object = MibTableColumn
cpqRackServerBladePartNumber = _CpqRackServerBladePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 6),
    _CpqRackServerBladePartNumber_Type()
)
cpqRackServerBladePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladePartNumber.setStatus("mandatory")


class _CpqRackServerBladeSparePartNumber_Type(DisplayString):
    """Custom type cpqRackServerBladeSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackServerBladeSparePartNumber_Object = MibTableColumn
cpqRackServerBladeSparePartNumber = _CpqRackServerBladeSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 7),
    _CpqRackServerBladeSparePartNumber_Type()
)
cpqRackServerBladeSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSparePartNumber.setStatus("mandatory")
_CpqRackServerBladePosition_Type = Integer32
_CpqRackServerBladePosition_Object = MibTableColumn
cpqRackServerBladePosition = _CpqRackServerBladePosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 8),
    _CpqRackServerBladePosition_Type()
)
cpqRackServerBladePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladePosition.setStatus("mandatory")
_CpqRackServerBladeHeight_Type = Integer32
_CpqRackServerBladeHeight_Object = MibTableColumn
cpqRackServerBladeHeight = _CpqRackServerBladeHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 9),
    _CpqRackServerBladeHeight_Type()
)
cpqRackServerBladeHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeHeight.setStatus("mandatory")
_CpqRackServerBladeWidth_Type = Integer32
_CpqRackServerBladeWidth_Object = MibTableColumn
cpqRackServerBladeWidth = _CpqRackServerBladeWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 10),
    _CpqRackServerBladeWidth_Type()
)
cpqRackServerBladeWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeWidth.setStatus("mandatory")
_CpqRackServerBladeDepth_Type = Integer32
_CpqRackServerBladeDepth_Object = MibTableColumn
cpqRackServerBladeDepth = _CpqRackServerBladeDepth_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 11),
    _CpqRackServerBladeDepth_Type()
)
cpqRackServerBladeDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeDepth.setStatus("mandatory")


class _CpqRackServerBladePresent_Type(Integer32):
    """Custom type cpqRackServerBladePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackServerBladePresent_Type.__name__ = "Integer32"
_CpqRackServerBladePresent_Object = MibTableColumn
cpqRackServerBladePresent = _CpqRackServerBladePresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 12),
    _CpqRackServerBladePresent_Type()
)
cpqRackServerBladePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladePresent.setStatus("mandatory")


class _CpqRackServerBladeHasFuses_Type(Integer32):
    """Custom type cpqRackServerBladeHasFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackServerBladeHasFuses_Type.__name__ = "Integer32"
_CpqRackServerBladeHasFuses_Object = MibTableColumn
cpqRackServerBladeHasFuses = _CpqRackServerBladeHasFuses_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 13),
    _CpqRackServerBladeHasFuses_Type()
)
cpqRackServerBladeHasFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeHasFuses.setStatus("mandatory")


class _CpqRackServerBladeEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackServerBladeEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackServerBladeEnclosureSerialNum_Object = MibTableColumn
cpqRackServerBladeEnclosureSerialNum = _CpqRackServerBladeEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 14),
    _CpqRackServerBladeEnclosureSerialNum_Type()
)
cpqRackServerBladeEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeEnclosureSerialNum.setStatus("mandatory")
_CpqRackServerBladeSlotsUsed_Type = Integer32
_CpqRackServerBladeSlotsUsed_Object = MibTableColumn
cpqRackServerBladeSlotsUsed = _CpqRackServerBladeSlotsUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 15),
    _CpqRackServerBladeSlotsUsed_Type()
)
cpqRackServerBladeSlotsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSlotsUsed.setStatus("mandatory")


class _CpqRackServerBladeSerialNum_Type(DisplayString):
    """Custom type cpqRackServerBladeSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeSerialNum_Type.__name__ = "DisplayString"
_CpqRackServerBladeSerialNum_Object = MibTableColumn
cpqRackServerBladeSerialNum = _CpqRackServerBladeSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 16),
    _CpqRackServerBladeSerialNum_Type()
)
cpqRackServerBladeSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSerialNum.setStatus("mandatory")


class _CpqRackServerBladeProductId_Type(DisplayString):
    """Custom type cpqRackServerBladeProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeProductId_Type.__name__ = "DisplayString"
_CpqRackServerBladeProductId_Object = MibTableColumn
cpqRackServerBladeProductId = _CpqRackServerBladeProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 17),
    _CpqRackServerBladeProductId_Type()
)
cpqRackServerBladeProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeProductId.setStatus("mandatory")


class _CpqRackServerBladeUid_Type(DisplayString):
    """Custom type cpqRackServerBladeUid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeUid_Type.__name__ = "DisplayString"
_CpqRackServerBladeUid_Object = MibTableColumn
cpqRackServerBladeUid = _CpqRackServerBladeUid_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 18),
    _CpqRackServerBladeUid_Type()
)
cpqRackServerBladeUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeUid.setStatus("mandatory")
_CpqRackServerBladeSlotsUsedX_Type = Integer32
_CpqRackServerBladeSlotsUsedX_Object = MibTableColumn
cpqRackServerBladeSlotsUsedX = _CpqRackServerBladeSlotsUsedX_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 19),
    _CpqRackServerBladeSlotsUsedX_Type()
)
cpqRackServerBladeSlotsUsedX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSlotsUsedX.setStatus("mandatory")
_CpqRackServerBladeSlotsUsedY_Type = Integer32
_CpqRackServerBladeSlotsUsedY_Object = MibTableColumn
cpqRackServerBladeSlotsUsedY = _CpqRackServerBladeSlotsUsedY_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 20),
    _CpqRackServerBladeSlotsUsedY_Type()
)
cpqRackServerBladeSlotsUsedY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSlotsUsedY.setStatus("mandatory")


class _CpqRackServerBladeStatus_Type(Integer32):
    """Custom type cpqRackServerBladeStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackServerBladeStatus_Type.__name__ = "Integer32"
_CpqRackServerBladeStatus_Object = MibTableColumn
cpqRackServerBladeStatus = _CpqRackServerBladeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 21),
    _CpqRackServerBladeStatus_Type()
)
cpqRackServerBladeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeStatus.setStatus("optional")
_CpqRackServerBladeFaultMajor_Type = Integer32
_CpqRackServerBladeFaultMajor_Object = MibTableColumn
cpqRackServerBladeFaultMajor = _CpqRackServerBladeFaultMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 22),
    _CpqRackServerBladeFaultMajor_Type()
)
cpqRackServerBladeFaultMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeFaultMajor.setStatus("optional")
_CpqRackServerBladeFaultMinor_Type = Integer32
_CpqRackServerBladeFaultMinor_Object = MibTableColumn
cpqRackServerBladeFaultMinor = _CpqRackServerBladeFaultMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 23),
    _CpqRackServerBladeFaultMinor_Type()
)
cpqRackServerBladeFaultMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeFaultMinor.setStatus("optional")


class _CpqRackServerBladeFaultDiagnosticString_Type(DisplayString):
    """Custom type cpqRackServerBladeFaultDiagnosticString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqRackServerBladeFaultDiagnosticString_Type.__name__ = "DisplayString"
_CpqRackServerBladeFaultDiagnosticString_Object = MibTableColumn
cpqRackServerBladeFaultDiagnosticString = _CpqRackServerBladeFaultDiagnosticString_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 24),
    _CpqRackServerBladeFaultDiagnosticString_Type()
)
cpqRackServerBladeFaultDiagnosticString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeFaultDiagnosticString.setStatus("optional")


class _CpqRackServerBladePowered_Type(Integer32):
    """Custom type cpqRackServerBladePowered based on Integer32"""
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
        *(("off", 3),
          ("on", 2),
          ("other", 1),
          ("powerStagedOff", 4),
          ("reboot", 5))
    )


_CpqRackServerBladePowered_Type.__name__ = "Integer32"
_CpqRackServerBladePowered_Object = MibTableColumn
cpqRackServerBladePowered = _CpqRackServerBladePowered_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 25),
    _CpqRackServerBladePowered_Type()
)
cpqRackServerBladePowered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackServerBladePowered.setStatus("optional")


class _CpqRackServerBladeUIDState_Type(Integer32):
    """Custom type cpqRackServerBladeUIDState based on Integer32"""
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
        *(("ledOff", 4),
          ("ledOn", 3),
          ("none", 2),
          ("other", 1))
    )


_CpqRackServerBladeUIDState_Type.__name__ = "Integer32"
_CpqRackServerBladeUIDState_Object = MibTableColumn
cpqRackServerBladeUIDState = _CpqRackServerBladeUIDState_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 26),
    _CpqRackServerBladeUIDState_Type()
)
cpqRackServerBladeUIDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackServerBladeUIDState.setStatus("optional")


class _CpqRackServerBladeSystemBIOSRevision_Type(DisplayString):
    """Custom type cpqRackServerBladeSystemBIOSRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeSystemBIOSRevision_Type.__name__ = "DisplayString"
_CpqRackServerBladeSystemBIOSRevision_Object = MibTableColumn
cpqRackServerBladeSystemBIOSRevision = _CpqRackServerBladeSystemBIOSRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 27),
    _CpqRackServerBladeSystemBIOSRevision_Type()
)
cpqRackServerBladeSystemBIOSRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSystemBIOSRevision.setStatus("optional")


class _CpqRackServerBladeSystemBIOSFlashingStatus_Type(Integer32):
    """Custom type cpqRackServerBladeSystemBIOSFlashingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flashing", 3),
          ("normal", 2),
          ("other", 1))
    )


_CpqRackServerBladeSystemBIOSFlashingStatus_Type.__name__ = "Integer32"
_CpqRackServerBladeSystemBIOSFlashingStatus_Object = MibTableColumn
cpqRackServerBladeSystemBIOSFlashingStatus = _CpqRackServerBladeSystemBIOSFlashingStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 28),
    _CpqRackServerBladeSystemBIOSFlashingStatus_Type()
)
cpqRackServerBladeSystemBIOSFlashingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeSystemBIOSFlashingStatus.setStatus("optional")


class _CpqRackServerBladeHasManagementDevice_Type(Integer32):
    """Custom type cpqRackServerBladeHasManagementDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackServerBladeHasManagementDevice_Type.__name__ = "Integer32"
_CpqRackServerBladeHasManagementDevice_Object = MibTableColumn
cpqRackServerBladeHasManagementDevice = _CpqRackServerBladeHasManagementDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 29),
    _CpqRackServerBladeHasManagementDevice_Type()
)
cpqRackServerBladeHasManagementDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeHasManagementDevice.setStatus("optional")


class _CpqRackServerBladeManagementDeviceFirmwareRevision_Type(DisplayString):
    """Custom type cpqRackServerBladeManagementDeviceFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerBladeManagementDeviceFirmwareRevision_Type.__name__ = "DisplayString"
_CpqRackServerBladeManagementDeviceFirmwareRevision_Object = MibTableColumn
cpqRackServerBladeManagementDeviceFirmwareRevision = _CpqRackServerBladeManagementDeviceFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 30),
    _CpqRackServerBladeManagementDeviceFirmwareRevision_Type()
)
cpqRackServerBladeManagementDeviceFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeManagementDeviceFirmwareRevision.setStatus("optional")


class _CpqRackServerBladeManagementDeviceFirmwareFlashingStatus_Type(Integer32):
    """Custom type cpqRackServerBladeManagementDeviceFirmwareFlashingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flashing", 3),
          ("normal", 2),
          ("other", 1))
    )


_CpqRackServerBladeManagementDeviceFirmwareFlashingStatus_Type.__name__ = "Integer32"
_CpqRackServerBladeManagementDeviceFirmwareFlashingStatus_Object = MibTableColumn
cpqRackServerBladeManagementDeviceFirmwareFlashingStatus = _CpqRackServerBladeManagementDeviceFirmwareFlashingStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 31),
    _CpqRackServerBladeManagementDeviceFirmwareFlashingStatus_Type()
)
cpqRackServerBladeManagementDeviceFirmwareFlashingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeManagementDeviceFirmwareFlashingStatus.setStatus("optional")


class _CpqRackServerBladeDiagnosticAdaptorPresence_Type(Integer32):
    """Custom type cpqRackServerBladeDiagnosticAdaptorPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackServerBladeDiagnosticAdaptorPresence_Type.__name__ = "Integer32"
_CpqRackServerBladeDiagnosticAdaptorPresence_Object = MibTableColumn
cpqRackServerBladeDiagnosticAdaptorPresence = _CpqRackServerBladeDiagnosticAdaptorPresence_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 32),
    _CpqRackServerBladeDiagnosticAdaptorPresence_Type()
)
cpqRackServerBladeDiagnosticAdaptorPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeDiagnosticAdaptorPresence.setStatus("optional")


class _CpqRackServerBladeASREnabled_Type(Integer32):
    """Custom type cpqRackServerBladeASREnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackServerBladeASREnabled_Type.__name__ = "Integer32"
_CpqRackServerBladeASREnabled_Object = MibTableColumn
cpqRackServerBladeASREnabled = _CpqRackServerBladeASREnabled_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 33),
    _CpqRackServerBladeASREnabled_Type()
)
cpqRackServerBladeASREnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeASREnabled.setStatus("optional")


class _CpqRackServerBladeFrontIOBlankingModeStatus_Type(Integer32):
    """Custom type cpqRackServerBladeFrontIOBlankingModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_CpqRackServerBladeFrontIOBlankingModeStatus_Type.__name__ = "Integer32"
_CpqRackServerBladeFrontIOBlankingModeStatus_Object = MibTableColumn
cpqRackServerBladeFrontIOBlankingModeStatus = _CpqRackServerBladeFrontIOBlankingModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 34),
    _CpqRackServerBladeFrontIOBlankingModeStatus_Type()
)
cpqRackServerBladeFrontIOBlankingModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladeFrontIOBlankingModeStatus.setStatus("optional")


class _CpqRackServerBladePOSTStatus_Type(Integer32):
    """Custom type cpqRackServerBladePOSTStatus based on Integer32"""
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
        *(("completed", 3),
          ("failed", 4),
          ("other", 1),
          ("started", 2))
    )


_CpqRackServerBladePOSTStatus_Type.__name__ = "Integer32"
_CpqRackServerBladePOSTStatus_Object = MibTableColumn
cpqRackServerBladePOSTStatus = _CpqRackServerBladePOSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 35),
    _CpqRackServerBladePOSTStatus_Type()
)
cpqRackServerBladePOSTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladePOSTStatus.setStatus("optional")


class _CpqRackServerBladePXEBootModeStatus_Type(Integer32):
    """Custom type cpqRackServerBladePXEBootModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_CpqRackServerBladePXEBootModeStatus_Type.__name__ = "Integer32"
_CpqRackServerBladePXEBootModeStatus_Object = MibTableColumn
cpqRackServerBladePXEBootModeStatus = _CpqRackServerBladePXEBootModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 36),
    _CpqRackServerBladePXEBootModeStatus_Type()
)
cpqRackServerBladePXEBootModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerBladePXEBootModeStatus.setStatus("optional")


class _CpqRackServerBladePendingBootOrderChange_Type(Integer32):
    """Custom type cpqRackServerBladePendingBootOrderChange based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("alwaysHDD", 10),
          ("alwaysPXE", 9),
          ("alwaysRBSU", 11),
          ("firstHDD", 4),
          ("firstPXE", 3),
          ("firstRBSU", 5),
          ("none", 2),
          ("onceHDD", 7),
          ("oncePXE", 6),
          ("onceRBSU", 8),
          ("other", 1))
    )


_CpqRackServerBladePendingBootOrderChange_Type.__name__ = "Integer32"
_CpqRackServerBladePendingBootOrderChange_Object = MibTableColumn
cpqRackServerBladePendingBootOrderChange = _CpqRackServerBladePendingBootOrderChange_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 1, 1, 1, 37),
    _CpqRackServerBladePendingBootOrderChange_Type()
)
cpqRackServerBladePendingBootOrderChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqRackServerBladePendingBootOrderChange.setStatus("optional")
_CpqRackServerNetworking_ObjectIdentity = ObjectIdentity
cpqRackServerNetworking = _CpqRackServerNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2)
)
_CpqRackServerNetworkingTable_Object = MibTable
cpqRackServerNetworkingTable = _CpqRackServerNetworkingTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cpqRackServerNetworkingTable.setStatus("optional")
_CpqRackServerNetworkingEntry_Object = MibTableRow
cpqRackServerNetworkingEntry = _CpqRackServerNetworkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1)
)
cpqRackServerNetworkingEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackServerNetworkingRack"),
    (0, "CPQRACK-MIB", "cpqRackServerNetworkingChassis"),
    (0, "CPQRACK-MIB", "cpqRackServerNetworkingIndex"),
)
if mibBuilder.loadTexts:
    cpqRackServerNetworkingEntry.setStatus("optional")
_CpqRackServerNetworkingRack_Type = Integer32
_CpqRackServerNetworkingRack_Object = MibTableColumn
cpqRackServerNetworkingRack = _CpqRackServerNetworkingRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 1),
    _CpqRackServerNetworkingRack_Type()
)
cpqRackServerNetworkingRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingRack.setStatus("optional")
_CpqRackServerNetworkingChassis_Type = Integer32
_CpqRackServerNetworkingChassis_Object = MibTableColumn
cpqRackServerNetworkingChassis = _CpqRackServerNetworkingChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 2),
    _CpqRackServerNetworkingChassis_Type()
)
cpqRackServerNetworkingChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingChassis.setStatus("mandatory")
_CpqRackServerNetworkingIndex_Type = Integer32
_CpqRackServerNetworkingIndex_Object = MibTableColumn
cpqRackServerNetworkingIndex = _CpqRackServerNetworkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 3),
    _CpqRackServerNetworkingIndex_Type()
)
cpqRackServerNetworkingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingIndex.setStatus("optional")


class _CpqRackServerNetworkingName_Type(DisplayString):
    """Custom type cpqRackServerNetworkingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerNetworkingName_Type.__name__ = "DisplayString"
_CpqRackServerNetworkingName_Object = MibTableColumn
cpqRackServerNetworkingName = _CpqRackServerNetworkingName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 4),
    _CpqRackServerNetworkingName_Type()
)
cpqRackServerNetworkingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingName.setStatus("optional")


class _CpqRackServerNetworkingEnclosureName_Type(DisplayString):
    """Custom type cpqRackServerNetworkingEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerNetworkingEnclosureName_Type.__name__ = "DisplayString"
_CpqRackServerNetworkingEnclosureName_Object = MibTableColumn
cpqRackServerNetworkingEnclosureName = _CpqRackServerNetworkingEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 5),
    _CpqRackServerNetworkingEnclosureName_Type()
)
cpqRackServerNetworkingEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingEnclosureName.setStatus("optional")
_CpqRackServerNetworkingEthernetInterfaces_Type = Integer32
_CpqRackServerNetworkingEthernetInterfaces_Object = MibTableColumn
cpqRackServerNetworkingEthernetInterfaces = _CpqRackServerNetworkingEthernetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 6),
    _CpqRackServerNetworkingEthernetInterfaces_Type()
)
cpqRackServerNetworkingEthernetInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingEthernetInterfaces.setStatus("optional")


class _CpqRackServerNetworkingEthernetMACAddress_Type(DisplayString):
    """Custom type cpqRackServerNetworkingEthernetMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerNetworkingEthernetMACAddress_Type.__name__ = "DisplayString"
_CpqRackServerNetworkingEthernetMACAddress_Object = MibTableColumn
cpqRackServerNetworkingEthernetMACAddress = _CpqRackServerNetworkingEthernetMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 2, 1, 1, 7),
    _CpqRackServerNetworkingEthernetMACAddress_Type()
)
cpqRackServerNetworkingEthernetMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerNetworkingEthernetMACAddress.setStatus("optional")
_CpqRackServerTempSensor_ObjectIdentity = ObjectIdentity
cpqRackServerTempSensor = _CpqRackServerTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3)
)
_CpqRackServerTempSensorTable_Object = MibTable
cpqRackServerTempSensorTable = _CpqRackServerTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cpqRackServerTempSensorTable.setStatus("optional")
_CpqRackServerTempSensorEntry_Object = MibTableRow
cpqRackServerTempSensorEntry = _CpqRackServerTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1)
)
cpqRackServerTempSensorEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackServerTempSensorRack"),
    (0, "CPQRACK-MIB", "cpqRackServerTempSensorChassis"),
    (0, "CPQRACK-MIB", "cpqRackServerTempSensorIndex"),
)
if mibBuilder.loadTexts:
    cpqRackServerTempSensorEntry.setStatus("optional")
_CpqRackServerTempSensorRack_Type = Integer32
_CpqRackServerTempSensorRack_Object = MibTableColumn
cpqRackServerTempSensorRack = _CpqRackServerTempSensorRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 1),
    _CpqRackServerTempSensorRack_Type()
)
cpqRackServerTempSensorRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorRack.setStatus("optional")
_CpqRackServerTempSensorChassis_Type = Integer32
_CpqRackServerTempSensorChassis_Object = MibTableColumn
cpqRackServerTempSensorChassis = _CpqRackServerTempSensorChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 2),
    _CpqRackServerTempSensorChassis_Type()
)
cpqRackServerTempSensorChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorChassis.setStatus("optional")
_CpqRackServerTempSensorIndex_Type = Integer32
_CpqRackServerTempSensorIndex_Object = MibTableColumn
cpqRackServerTempSensorIndex = _CpqRackServerTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 3),
    _CpqRackServerTempSensorIndex_Type()
)
cpqRackServerTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorIndex.setStatus("optional")


class _CpqRackServerTempSensorName_Type(DisplayString):
    """Custom type cpqRackServerTempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerTempSensorName_Type.__name__ = "DisplayString"
_CpqRackServerTempSensorName_Object = MibTableColumn
cpqRackServerTempSensorName = _CpqRackServerTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 4),
    _CpqRackServerTempSensorName_Type()
)
cpqRackServerTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorName.setStatus("optional")


class _CpqRackServerTempSensorEnclosureName_Type(DisplayString):
    """Custom type cpqRackServerTempSensorEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerTempSensorEnclosureName_Type.__name__ = "DisplayString"
_CpqRackServerTempSensorEnclosureName_Object = MibTableColumn
cpqRackServerTempSensorEnclosureName = _CpqRackServerTempSensorEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 5),
    _CpqRackServerTempSensorEnclosureName_Type()
)
cpqRackServerTempSensorEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorEnclosureName.setStatus("optional")
_CpqRackServerTempSensorCount_Type = Integer32
_CpqRackServerTempSensorCount_Object = MibTableColumn
cpqRackServerTempSensorCount = _CpqRackServerTempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 6),
    _CpqRackServerTempSensorCount_Type()
)
cpqRackServerTempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorCount.setStatus("optional")


class _CpqRackServerTempSensorLocation_Type(DisplayString):
    """Custom type cpqRackServerTempSensorLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackServerTempSensorLocation_Type.__name__ = "DisplayString"
_CpqRackServerTempSensorLocation_Object = MibTableColumn
cpqRackServerTempSensorLocation = _CpqRackServerTempSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 7),
    _CpqRackServerTempSensorLocation_Type()
)
cpqRackServerTempSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorLocation.setStatus("optional")
_CpqRackServerTempSensorCurrent_Type = Integer32
_CpqRackServerTempSensorCurrent_Object = MibTableColumn
cpqRackServerTempSensorCurrent = _CpqRackServerTempSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 8),
    _CpqRackServerTempSensorCurrent_Type()
)
cpqRackServerTempSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorCurrent.setStatus("optional")
_CpqRackServerTempSensorThreshold_Type = Integer32
_CpqRackServerTempSensorThreshold_Object = MibTableColumn
cpqRackServerTempSensorThreshold = _CpqRackServerTempSensorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 9),
    _CpqRackServerTempSensorThreshold_Type()
)
cpqRackServerTempSensorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorThreshold.setStatus("optional")


class _CpqRackServerTempSensorCondition_Type(Integer32):
    """Custom type cpqRackServerTempSensorCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackServerTempSensorCondition_Type.__name__ = "Integer32"
_CpqRackServerTempSensorCondition_Object = MibTableColumn
cpqRackServerTempSensorCondition = _CpqRackServerTempSensorCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 10),
    _CpqRackServerTempSensorCondition_Type()
)
cpqRackServerTempSensorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorCondition.setStatus("optional")


class _CpqRackServerTempSensorType_Type(Integer32):
    """Custom type cpqRackServerTempSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("blowout", 5),
          ("caution", 9),
          ("critical", 15),
          ("other", 1))
    )


_CpqRackServerTempSensorType_Type.__name__ = "Integer32"
_CpqRackServerTempSensorType_Object = MibTableColumn
cpqRackServerTempSensorType = _CpqRackServerTempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 4, 3, 1, 1, 11),
    _CpqRackServerTempSensorType_Type()
)
cpqRackServerTempSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackServerTempSensorType.setStatus("optional")
_CpqRackPower_ObjectIdentity = ObjectIdentity
cpqRackPower = _CpqRackPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5)
)
_CpqRackPowerSupply_ObjectIdentity = ObjectIdentity
cpqRackPowerSupply = _CpqRackPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1)
)
_CpqRackPowerSupplyTable_Object = MibTable
cpqRackPowerSupplyTable = _CpqRackPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyTable.setStatus("mandatory")
_CpqRackPowerSupplyEntry_Object = MibTableRow
cpqRackPowerSupplyEntry = _CpqRackPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1)
)
cpqRackPowerSupplyEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackPowerSupplyRack"),
    (0, "CPQRACK-MIB", "cpqRackPowerSupplyChassis"),
    (0, "CPQRACK-MIB", "cpqRackPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyEntry.setStatus("mandatory")
_CpqRackPowerSupplyRack_Type = Integer32
_CpqRackPowerSupplyRack_Object = MibTableColumn
cpqRackPowerSupplyRack = _CpqRackPowerSupplyRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 1),
    _CpqRackPowerSupplyRack_Type()
)
cpqRackPowerSupplyRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyRack.setStatus("mandatory")
_CpqRackPowerSupplyChassis_Type = Integer32
_CpqRackPowerSupplyChassis_Object = MibTableColumn
cpqRackPowerSupplyChassis = _CpqRackPowerSupplyChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 2),
    _CpqRackPowerSupplyChassis_Type()
)
cpqRackPowerSupplyChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyChassis.setStatus("mandatory")
_CpqRackPowerSupplyIndex_Type = Integer32
_CpqRackPowerSupplyIndex_Object = MibTableColumn
cpqRackPowerSupplyIndex = _CpqRackPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 3),
    _CpqRackPowerSupplyIndex_Type()
)
cpqRackPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyIndex.setStatus("mandatory")


class _CpqRackPowerSupplyEnclosureName_Type(DisplayString):
    """Custom type cpqRackPowerSupplyEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplyEnclosureName_Type.__name__ = "DisplayString"
_CpqRackPowerSupplyEnclosureName_Object = MibTableColumn
cpqRackPowerSupplyEnclosureName = _CpqRackPowerSupplyEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 4),
    _CpqRackPowerSupplyEnclosureName_Type()
)
cpqRackPowerSupplyEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyEnclosureName.setStatus("mandatory")


class _CpqRackPowerSupplySerialNum_Type(DisplayString):
    """Custom type cpqRackPowerSupplySerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplySerialNum_Type.__name__ = "DisplayString"
_CpqRackPowerSupplySerialNum_Object = MibTableColumn
cpqRackPowerSupplySerialNum = _CpqRackPowerSupplySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 5),
    _CpqRackPowerSupplySerialNum_Type()
)
cpqRackPowerSupplySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplySerialNum.setStatus("mandatory")


class _CpqRackPowerSupplyPartNumber_Type(DisplayString):
    """Custom type cpqRackPowerSupplyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplyPartNumber_Type.__name__ = "DisplayString"
_CpqRackPowerSupplyPartNumber_Object = MibTableColumn
cpqRackPowerSupplyPartNumber = _CpqRackPowerSupplyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 6),
    _CpqRackPowerSupplyPartNumber_Type()
)
cpqRackPowerSupplyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyPartNumber.setStatus("mandatory")


class _CpqRackPowerSupplySparePartNumber_Type(DisplayString):
    """Custom type cpqRackPowerSupplySparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplySparePartNumber_Type.__name__ = "DisplayString"
_CpqRackPowerSupplySparePartNumber_Object = MibTableColumn
cpqRackPowerSupplySparePartNumber = _CpqRackPowerSupplySparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 7),
    _CpqRackPowerSupplySparePartNumber_Type()
)
cpqRackPowerSupplySparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplySparePartNumber.setStatus("mandatory")


class _CpqRackPowerSupplyFWRev_Type(DisplayString):
    """Custom type cpqRackPowerSupplyFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplyFWRev_Type.__name__ = "DisplayString"
_CpqRackPowerSupplyFWRev_Object = MibTableColumn
cpqRackPowerSupplyFWRev = _CpqRackPowerSupplyFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 8),
    _CpqRackPowerSupplyFWRev_Type()
)
cpqRackPowerSupplyFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyFWRev.setStatus("mandatory")
_CpqRackPowerSupplyMaxPwrOutput_Type = Integer32
_CpqRackPowerSupplyMaxPwrOutput_Object = MibTableColumn
cpqRackPowerSupplyMaxPwrOutput = _CpqRackPowerSupplyMaxPwrOutput_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 9),
    _CpqRackPowerSupplyMaxPwrOutput_Type()
)
cpqRackPowerSupplyMaxPwrOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyMaxPwrOutput.setStatus("mandatory")
_CpqRackPowerSupplyCurPwrOutput_Type = Integer32
_CpqRackPowerSupplyCurPwrOutput_Object = MibTableColumn
cpqRackPowerSupplyCurPwrOutput = _CpqRackPowerSupplyCurPwrOutput_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 10),
    _CpqRackPowerSupplyCurPwrOutput_Type()
)
cpqRackPowerSupplyCurPwrOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyCurPwrOutput.setStatus("mandatory")
_CpqRackPowerSupplyPosition_Type = Integer32
_CpqRackPowerSupplyPosition_Object = MibTableColumn
cpqRackPowerSupplyPosition = _CpqRackPowerSupplyPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 11),
    _CpqRackPowerSupplyPosition_Type()
)
cpqRackPowerSupplyPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyPosition.setStatus("mandatory")
_CpqRackPowerSupplyIntakeTemp_Type = Integer32
_CpqRackPowerSupplyIntakeTemp_Object = MibTableColumn
cpqRackPowerSupplyIntakeTemp = _CpqRackPowerSupplyIntakeTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 12),
    _CpqRackPowerSupplyIntakeTemp_Type()
)
cpqRackPowerSupplyIntakeTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyIntakeTemp.setStatus("mandatory")
_CpqRackPowerSupplyExhaustTemp_Type = Integer32
_CpqRackPowerSupplyExhaustTemp_Object = MibTableColumn
cpqRackPowerSupplyExhaustTemp = _CpqRackPowerSupplyExhaustTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 13),
    _CpqRackPowerSupplyExhaustTemp_Type()
)
cpqRackPowerSupplyExhaustTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyExhaustTemp.setStatus("mandatory")


class _CpqRackPowerSupplyStatus_Type(Integer32):
    """Custom type cpqRackPowerSupplyStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bistFailure", 3),
          ("brownOut", 13),
          ("calibrationTableInvalid", 16),
          ("dacFailed", 9),
          ("epromFailed", 7),
          ("fanFailure", 4),
          ("generalFailure", 2),
          ("giveupOnStartup", 14),
          ("interlockOpen", 6),
          ("noError", 1),
          ("nvramInvalid", 15),
          ("orringdiodeFailed", 12),
          ("ramTestFailed", 10),
          ("tempFailure", 5),
          ("voltageChannelFailed", 11),
          ("vrefFailed", 8))
    )


_CpqRackPowerSupplyStatus_Type.__name__ = "Integer32"
_CpqRackPowerSupplyStatus_Object = MibTableColumn
cpqRackPowerSupplyStatus = _CpqRackPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 14),
    _CpqRackPowerSupplyStatus_Type()
)
cpqRackPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyStatus.setStatus("mandatory")


class _CpqRackPowerSupplyInputLineStatus_Type(Integer32):
    """Custom type cpqRackPowerSupplyInputLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("brownOut", 5),
          ("lineHit", 4),
          ("lineOverVoltage", 2),
          ("linePowerLoss", 6),
          ("lineUnderVoltage", 3),
          ("noError", 1))
    )


_CpqRackPowerSupplyInputLineStatus_Type.__name__ = "Integer32"
_CpqRackPowerSupplyInputLineStatus_Object = MibTableColumn
cpqRackPowerSupplyInputLineStatus = _CpqRackPowerSupplyInputLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 15),
    _CpqRackPowerSupplyInputLineStatus_Type()
)
cpqRackPowerSupplyInputLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyInputLineStatus.setStatus("mandatory")


class _CpqRackPowerSupplyPresent_Type(Integer32):
    """Custom type cpqRackPowerSupplyPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackPowerSupplyPresent_Type.__name__ = "Integer32"
_CpqRackPowerSupplyPresent_Object = MibTableColumn
cpqRackPowerSupplyPresent = _CpqRackPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 16),
    _CpqRackPowerSupplyPresent_Type()
)
cpqRackPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyPresent.setStatus("mandatory")


class _CpqRackPowerSupplyCondition_Type(Integer32):
    """Custom type cpqRackPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqRackPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqRackPowerSupplyCondition_Object = MibTableColumn
cpqRackPowerSupplyCondition = _CpqRackPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 17),
    _CpqRackPowerSupplyCondition_Type()
)
cpqRackPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyCondition.setStatus("mandatory")


class _CpqRackPowerSupplyEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackPowerSupplyEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackPowerSupplyEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackPowerSupplyEnclosureSerialNum_Object = MibTableColumn
cpqRackPowerSupplyEnclosureSerialNum = _CpqRackPowerSupplyEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 5, 1, 1, 1, 18),
    _CpqRackPowerSupplyEnclosureSerialNum_Type()
)
cpqRackPowerSupplyEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackPowerSupplyEnclosureSerialNum.setStatus("mandatory")
_CpqRackNetwork_ObjectIdentity = ObjectIdentity
cpqRackNetwork = _CpqRackNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6)
)
_CpqRackNetConnector_ObjectIdentity = ObjectIdentity
cpqRackNetConnector = _CpqRackNetConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1)
)
_CpqRackNetConnectorTable_Object = MibTable
cpqRackNetConnectorTable = _CpqRackNetConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorTable.setStatus("mandatory")
_CpqRackNetConnectorEntry_Object = MibTableRow
cpqRackNetConnectorEntry = _CpqRackNetConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1)
)
cpqRackNetConnectorEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"),
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorEntry.setStatus("mandatory")
_CpqRackNetConnectorRack_Type = Integer32
_CpqRackNetConnectorRack_Object = MibTableColumn
cpqRackNetConnectorRack = _CpqRackNetConnectorRack_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 1),
    _CpqRackNetConnectorRack_Type()
)
cpqRackNetConnectorRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorRack.setStatus("mandatory")
_CpqRackNetConnectorChassis_Type = Integer32
_CpqRackNetConnectorChassis_Object = MibTableColumn
cpqRackNetConnectorChassis = _CpqRackNetConnectorChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 2),
    _CpqRackNetConnectorChassis_Type()
)
cpqRackNetConnectorChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorChassis.setStatus("mandatory")
_CpqRackNetConnectorIndex_Type = Integer32
_CpqRackNetConnectorIndex_Object = MibTableColumn
cpqRackNetConnectorIndex = _CpqRackNetConnectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 3),
    _CpqRackNetConnectorIndex_Type()
)
cpqRackNetConnectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorIndex.setStatus("mandatory")


class _CpqRackNetConnectorEnclosureName_Type(DisplayString):
    """Custom type cpqRackNetConnectorEnclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorEnclosureName_Type.__name__ = "DisplayString"
_CpqRackNetConnectorEnclosureName_Object = MibTableColumn
cpqRackNetConnectorEnclosureName = _CpqRackNetConnectorEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 4),
    _CpqRackNetConnectorEnclosureName_Type()
)
cpqRackNetConnectorEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorEnclosureName.setStatus("mandatory")


class _CpqRackNetConnectorName_Type(DisplayString):
    """Custom type cpqRackNetConnectorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorName_Type.__name__ = "DisplayString"
_CpqRackNetConnectorName_Object = MibTableColumn
cpqRackNetConnectorName = _CpqRackNetConnectorName_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 5),
    _CpqRackNetConnectorName_Type()
)
cpqRackNetConnectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorName.setStatus("mandatory")


class _CpqRackNetConnectorModel_Type(DisplayString):
    """Custom type cpqRackNetConnectorModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorModel_Type.__name__ = "DisplayString"
_CpqRackNetConnectorModel_Object = MibTableColumn
cpqRackNetConnectorModel = _CpqRackNetConnectorModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 6),
    _CpqRackNetConnectorModel_Type()
)
cpqRackNetConnectorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorModel.setStatus("mandatory")


class _CpqRackNetConnectorSerialNum_Type(DisplayString):
    """Custom type cpqRackNetConnectorSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorSerialNum_Type.__name__ = "DisplayString"
_CpqRackNetConnectorSerialNum_Object = MibTableColumn
cpqRackNetConnectorSerialNum = _CpqRackNetConnectorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 7),
    _CpqRackNetConnectorSerialNum_Type()
)
cpqRackNetConnectorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorSerialNum.setStatus("mandatory")


class _CpqRackNetConnectorPartNumber_Type(DisplayString):
    """Custom type cpqRackNetConnectorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorPartNumber_Type.__name__ = "DisplayString"
_CpqRackNetConnectorPartNumber_Object = MibTableColumn
cpqRackNetConnectorPartNumber = _CpqRackNetConnectorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 8),
    _CpqRackNetConnectorPartNumber_Type()
)
cpqRackNetConnectorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorPartNumber.setStatus("mandatory")


class _CpqRackNetConnectorSparePartNumber_Type(DisplayString):
    """Custom type cpqRackNetConnectorSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorSparePartNumber_Type.__name__ = "DisplayString"
_CpqRackNetConnectorSparePartNumber_Object = MibTableColumn
cpqRackNetConnectorSparePartNumber = _CpqRackNetConnectorSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 9),
    _CpqRackNetConnectorSparePartNumber_Type()
)
cpqRackNetConnectorSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorSparePartNumber.setStatus("mandatory")


class _CpqRackNetConnectorFWRev_Type(DisplayString):
    """Custom type cpqRackNetConnectorFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorFWRev_Type.__name__ = "DisplayString"
_CpqRackNetConnectorFWRev_Object = MibTableColumn
cpqRackNetConnectorFWRev = _CpqRackNetConnectorFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 10),
    _CpqRackNetConnectorFWRev_Type()
)
cpqRackNetConnectorFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorFWRev.setStatus("mandatory")


class _CpqRackNetConnectorType_Type(Integer32):
    """Custom type cpqRackNetConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("other", 1),
          ("passive", 2))
    )


_CpqRackNetConnectorType_Type.__name__ = "Integer32"
_CpqRackNetConnectorType_Object = MibTableColumn
cpqRackNetConnectorType = _CpqRackNetConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 11),
    _CpqRackNetConnectorType_Type()
)
cpqRackNetConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorType.setStatus("mandatory")


class _CpqRackNetConnectorLocation_Type(DisplayString):
    """Custom type cpqRackNetConnectorLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorLocation_Type.__name__ = "DisplayString"
_CpqRackNetConnectorLocation_Object = MibTableColumn
cpqRackNetConnectorLocation = _CpqRackNetConnectorLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 12),
    _CpqRackNetConnectorLocation_Type()
)
cpqRackNetConnectorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorLocation.setStatus("mandatory")


class _CpqRackNetConnectorPresent_Type(Integer32):
    """Custom type cpqRackNetConnectorPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqRackNetConnectorPresent_Type.__name__ = "Integer32"
_CpqRackNetConnectorPresent_Object = MibTableColumn
cpqRackNetConnectorPresent = _CpqRackNetConnectorPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 13),
    _CpqRackNetConnectorPresent_Type()
)
cpqRackNetConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorPresent.setStatus("mandatory")


class _CpqRackNetConnectorHasFuses_Type(Integer32):
    """Custom type cpqRackNetConnectorHasFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CpqRackNetConnectorHasFuses_Type.__name__ = "Integer32"
_CpqRackNetConnectorHasFuses_Object = MibTableColumn
cpqRackNetConnectorHasFuses = _CpqRackNetConnectorHasFuses_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 14),
    _CpqRackNetConnectorHasFuses_Type()
)
cpqRackNetConnectorHasFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorHasFuses.setStatus("mandatory")


class _CpqRackNetConnectorEnclosureSerialNum_Type(DisplayString):
    """Custom type cpqRackNetConnectorEnclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackNetConnectorEnclosureSerialNum_Type.__name__ = "DisplayString"
_CpqRackNetConnectorEnclosureSerialNum_Object = MibTableColumn
cpqRackNetConnectorEnclosureSerialNum = _CpqRackNetConnectorEnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 15),
    _CpqRackNetConnectorEnclosureSerialNum_Type()
)
cpqRackNetConnectorEnclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorEnclosureSerialNum.setStatus("mandatory")


class _CpqRackNetConnectorTechnologyType_Type(Integer32):
    """Custom type cpqRackNetConnectorTechnologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("other", 1),
          ("passive", 2))
    )


_CpqRackNetConnectorTechnologyType_Type.__name__ = "Integer32"
_CpqRackNetConnectorTechnologyType_Object = MibTableColumn
cpqRackNetConnectorTechnologyType = _CpqRackNetConnectorTechnologyType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 16),
    _CpqRackNetConnectorTechnologyType_Type()
)
cpqRackNetConnectorTechnologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorTechnologyType.setStatus("mandatory")


class _CpqRackNetConnectorDeviceType_Type(Integer32):
    """Custom type cpqRackNetConnectorDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fibrechannel", 3),
          ("inifiband", 5),
          ("network", 2),
          ("noconnect", 1),
          ("pciexpress", 6),
          ("sas", 4))
    )


_CpqRackNetConnectorDeviceType_Type.__name__ = "Integer32"
_CpqRackNetConnectorDeviceType_Object = MibTableColumn
cpqRackNetConnectorDeviceType = _CpqRackNetConnectorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 2, 6, 1, 1, 1, 17),
    _CpqRackNetConnectorDeviceType_Type()
)
cpqRackNetConnectorDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackNetConnectorDeviceType.setStatus("mandatory")
_CpqRackSysObjID_ObjectIdentity = ObjectIdentity
cpqRackSysObjID = _CpqRackSysObjID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 22, 3)
)


class _CpqRackSystemObjectIdentification_Type(DisplayString):
    """Custom type cpqRackSystemObjectIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqRackSystemObjectIdentification_Type.__name__ = "DisplayString"
_CpqRackSystemObjectIdentification_Object = MibScalar
cpqRackSystemObjectIdentification = _CpqRackSystemObjectIdentification_Object(
    (1, 3, 6, 1, 4, 1, 232, 22, 3, 1),
    _CpqRackSystemObjectIdentification_Type()
)
cpqRackSystemObjectIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRackSystemObjectIdentification.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqRackNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22001)
)
cpqRackNameChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackSerialNum"),
        ("CPQRACK-MIB", "cpqRackTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNameChanged.setStatus(
        ""
    )

cpqRackEnclosureNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22002)
)
cpqRackEnclosureNameChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureModel"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureNameChanged.setStatus(
        ""
    )

cpqRackEnclosureRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22003)
)
cpqRackEnclosureRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureModel"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureRemoved.setStatus(
        ""
    )

cpqRackEnclosureInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22004)
)
cpqRackEnclosureInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureModel"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureInserted.setStatus(
        ""
    )

cpqRackEnclosureTempFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22005)
)
cpqRackEnclosureTempFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTempLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureTempFailed.setStatus(
        ""
    )

cpqRackEnclosureTempDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22006)
)
cpqRackEnclosureTempDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTempLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureTempDegraded.setStatus(
        ""
    )

cpqRackEnclosureTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22007)
)
cpqRackEnclosureTempOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTempLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureTempOk.setStatus(
        ""
    )

cpqRackEnclosureFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22008)
)
cpqRackEnclosureFanFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureFanFailed.setStatus(
        ""
    )

cpqRackEnclosureFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22009)
)
cpqRackEnclosureFanDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureFanDegraded.setStatus(
        ""
    )

cpqRackEnclosureFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22010)
)
cpqRackEnclosureFanOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureFanOk.setStatus(
        ""
    )

cpqRackEnclosureFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22011)
)
cpqRackEnclosureFanRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureFanRemoved.setStatus(
        ""
    )

cpqRackEnclosureFanInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22012)
)
cpqRackEnclosureFanInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFanSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureFanInserted.setStatus(
        ""
    )

cpqRackPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22013)
)
cpqRackPowerSupplyFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySerialNum"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyFailed.setStatus(
        ""
    )

cpqRackPowerSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22014)
)
cpqRackPowerSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySerialNum"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyDegraded.setStatus(
        ""
    )

cpqRackPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22015)
)
cpqRackPowerSupplyOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySerialNum"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyOk.setStatus(
        ""
    )

cpqRackPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22016)
)
cpqRackPowerSupplyRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySerialNum"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyRemoved.setStatus(
        ""
    )

cpqRackPowerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22017)
)
cpqRackPowerSupplyInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySerialNum"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSupplyInserted.setStatus(
        ""
    )

cpqRackPowerSubsystemNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22018)
)
cpqRackPowerSubsystemNotRedundant.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSubsystemNotRedundant.setStatus(
        ""
    )

cpqRackPowerSubsystemLineVoltageProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22019)
)
cpqRackPowerSubsystemLineVoltageProblem.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyEnclosureName"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyPosition"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyFWRev"),
        ("CPQRACK-MIB", "cpqRackPowerSupplyInputLineStatus"),
        ("CPQRACK-MIB", "cpqRackPowerSupplySparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSubsystemLineVoltageProblem.setStatus(
        ""
    )

cpqRackPowerSubsystemOverloadCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22020)
)
cpqRackPowerSubsystemOverloadCondition.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackPowerEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerSubsystemOverloadCondition.setStatus(
        ""
    )

cpqRackPowerShedAutoShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22021)
)
cpqRackPowerShedAutoShutdown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerShedAutoShutdown.setStatus(
        ""
    )

cpqRackServerPowerOnFailedNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22022)
)
cpqRackServerPowerOnFailedNotRedundant.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerPowerOnFailedNotRedundant.setStatus(
        ""
    )

cpqRackServerPowerOnFailedNotEnoughPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22023)
)
cpqRackServerPowerOnFailedNotEnoughPower.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerPowerOnFailedNotEnoughPower.setStatus(
        ""
    )

cpqRackServerPowerOnFailedEnclosureNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22024)
)
cpqRackServerPowerOnFailedEnclosureNotFound.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerPowerOnFailedEnclosureNotFound.setStatus(
        ""
    )

cpqRackServerPowerOnFailedPowerChassisNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22025)
)
cpqRackServerPowerOnFailedPowerChassisNotFound.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerPowerOnFailedPowerChassisNotFound.setStatus(
        ""
    )

cpqRackServerPowerOnManualOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22026)
)
cpqRackServerPowerOnManualOverride.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerPowerOnManualOverride.setStatus(
        ""
    )

cpqRackFuseOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22027)
)
cpqRackFuseOpen.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureFuseLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackFuseOpen.setStatus(
        ""
    )

cpqRackServerBladeRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22028)
)
cpqRackServerBladeRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeRemoved.setStatus(
        ""
    )

cpqRackServerBladeInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22029)
)
cpqRackServerBladeInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeInserted.setStatus(
        ""
    )

cpqRackPowerChassisNotLoadBalanced = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22030)
)
cpqRackPowerChassisNotLoadBalanced.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisNotLoadBalanced.setStatus(
        ""
    )

cpqRackPowerChassisDcPowerProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22031)
)
cpqRackPowerChassisDcPowerProblem.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisDcPowerProblem.setStatus(
        ""
    )

cpqRackPowerChassisAcFacilityPowerExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22032)
)
cpqRackPowerChassisAcFacilityPowerExceeded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisAcFacilityPowerExceeded.setStatus(
        ""
    )

cpqRackPowerUnknownPowerConsumption = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22033)
)
cpqRackPowerUnknownPowerConsumption.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerUnknownPowerConsumption.setStatus(
        ""
    )

cpqRackPowerChassisLoadBalancingWireMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22034)
)
cpqRackPowerChassisLoadBalancingWireMissing.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisLoadBalancingWireMissing.setStatus(
        ""
    )

cpqRackPowerChassisTooManyPowerChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22035)
)
cpqRackPowerChassisTooManyPowerChassis.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisTooManyPowerChassis.setStatus(
        ""
    )

cpqRackPowerChassisConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22036)
)
cpqRackPowerChassisConfigError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackPowerChassisConfigError.setStatus(
        ""
    )

cpqRackEnclosureManagerDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22037)
)
cpqRackEnclosureManagerDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureManagerDegraded.setStatus(
        ""
    )

cpqRackEnclosureManagerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22038)
)
cpqRackEnclosureManagerOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureManagerOk.setStatus(
        ""
    )

cpqRackEnclosureManagerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22039)
)
cpqRackEnclosureManagerRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureManagerRemoved.setStatus(
        ""
    )

cpqRackEnclosureManagerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22040)
)
cpqRackEnclosureManagerInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackEnclosureManagerInserted.setStatus(
        ""
    )

cpqRackManagerPrimaryRole = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22041)
)
cpqRackManagerPrimaryRole.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerLocation"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureManagerSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackManagerPrimaryRole.setStatus(
        ""
    )

cpqRackServerBladeEKeyingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22042)
)
cpqRackServerBladeEKeyingFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeEKeyingFailed.setStatus(
        ""
    )

cpqRackServerBladeEKeyingOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22043)
)
cpqRackServerBladeEKeyingOK.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeEKeyingOK.setStatus(
        ""
    )

cpqRackNetConnectorRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22044)
)
cpqRackNetConnectorRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackNetConnectorEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorRemoved.setStatus(
        ""
    )

cpqRackNetConnectorInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22045)
)
cpqRackNetConnectorInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackNetConnectorEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorInserted.setStatus(
        ""
    )

cpqRackNetConnectorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22046)
)
cpqRackNetConnectorFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackNetConnectorEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorFailed.setStatus(
        ""
    )

cpqRackNetConnectorDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22047)
)
cpqRackNetConnectorDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackNetConnectorEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorDegraded.setStatus(
        ""
    )

cpqRackNetConnectorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22048)
)
cpqRackNetConnectorOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackNetConnectorEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackNetConnectorOk.setStatus(
        ""
    )

cpqRackServerBladeToLowPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22049)
)
cpqRackServerBladeToLowPower.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeToLowPower.setStatus(
        ""
    )

cpqRackServerBladeRemoved2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22050)
)
cpqRackServerBladeRemoved2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeRemoved2.setStatus(
        ""
    )

cpqRackServerBladeInserted2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22051)
)
cpqRackServerBladeInserted2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeInserted2.setStatus(
        ""
    )

cpqRackServerBladeStatusRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22052)
)
cpqRackServerBladeStatusRepaired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladeProductId"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeStatusRepaired.setStatus(
        ""
    )

cpqRackServerBladeStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22053)
)
cpqRackServerBladeStatusDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladeProductId"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultMajor"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultMinor"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultDiagnosticString"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeStatusDegraded.setStatus(
        ""
    )

cpqRackServerBladeStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22054)
)
cpqRackServerBladeStatusCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladeProductId"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultMajor"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultMinor"),
        ("CPQRACK-MIB", "cpqRackServerBladeFaultDiagnosticString"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeStatusCritical.setStatus(
        ""
    )

cpqRackServerBladeGrpCapTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22055)
)
cpqRackServerBladeGrpCapTimeout.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeGrpCapTimeout.setStatus(
        ""
    )

cpqRackServerBladeUnexpectedShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22056)
)
cpqRackServerBladeUnexpectedShutdown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeUnexpectedShutdown.setStatus(
        ""
    )

cpqRackServerBladeMangementControllerFirmwareUpdating = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22057)
)
cpqRackServerBladeMangementControllerFirmwareUpdating.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeManagementDeviceFirmwareFlashingStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeMangementControllerFirmwareUpdating.setStatus(
        ""
    )

cpqRackServerBladeMangementControllerFirmwareUpdateComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22058)
)
cpqRackServerBladeMangementControllerFirmwareUpdateComplete.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeManagementDeviceFirmwareFlashingStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeMangementControllerFirmwareUpdateComplete.setStatus(
        ""
    )

cpqRackServerBladeSystemBIOSFirmwareUpdating = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22059)
)
cpqRackServerBladeSystemBIOSFirmwareUpdating.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeSystemBIOSFlashingStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeSystemBIOSFirmwareUpdating.setStatus(
        ""
    )

cpqRackServerBladeSystemBIOSFirmwareUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22060)
)
cpqRackServerBladeSystemBIOSFirmwareUpdateCompleted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeSystemBIOSFlashingStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeSystemBIOSFirmwareUpdateCompleted.setStatus(
        ""
    )

cpqRackServerBladeFrontIOBlankingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22061)
)
cpqRackServerBladeFrontIOBlankingActive.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeFrontIOBlankingModeStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeFrontIOBlankingActive.setStatus(
        ""
    )

cpqRackServerBladeRemoteFrontIOBlankingInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22062)
)
cpqRackServerBladeRemoteFrontIOBlankingInactive.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeFrontIOBlankingModeStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeRemoteFrontIOBlankingInactive.setStatus(
        ""
    )

cpqRackServerBladeDiagnosticAdaptorInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22063)
)
cpqRackServerBladeDiagnosticAdaptorInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeDiagnosticAdaptorPresence"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeDiagnosticAdaptorInserted.setStatus(
        ""
    )

cpqRackServerBladeDiagnosticAdaptorRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22064)
)
cpqRackServerBladeDiagnosticAdaptorRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeDiagnosticAdaptorPresence"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeDiagnosticAdaptorRemoved.setStatus(
        ""
    )

cpqRackServerBladeEnteredPXEBootMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22065)
)
cpqRackServerBladeEnteredPXEBootMode.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePXEBootModeStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeEnteredPXEBootMode.setStatus(
        ""
    )

cpqRackServerBladeExitedPXEBootMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22066)
)
cpqRackServerBladeExitedPXEBootMode.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePXEBootModeStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeExitedPXEBootMode.setStatus(
        ""
    )

cpqRackServerBladeWarmReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22067)
)
cpqRackServerBladeWarmReset.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePOSTStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladeWarmReset.setStatus(
        ""
    )

cpqRackServerBladePOSTCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22068)
)
cpqRackServerBladePOSTCompleted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePOSTStatus"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladePOSTCompleted.setStatus(
        ""
    )

cpqRackServerBladePoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22069)
)
cpqRackServerBladePoweredOn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePowered"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladePoweredOn.setStatus(
        ""
    )

cpqRackServerBladePoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 22070)
)
cpqRackServerBladePoweredOff.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackServerBladeEnclosureName"),
        ("CPQRACK-MIB", "cpqRackServerBladeName"),
        ("CPQRACK-MIB", "cpqRackServerBladePosition"),
        ("CPQRACK-MIB", "cpqRackServerBladeSparePartNumber"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeSerialNum"),
        ("CPQRACK-MIB", "cpqRackServerBladeUid"),
        ("CPQRACK-MIB", "cpqRackServerBladePowered"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureTrapSequenceNum"))
)
if mibBuilder.loadTexts:
    cpqRackServerBladePoweredOff.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQRACK-MIB",
    **{"cpqRackNameChanged": cpqRackNameChanged,
       "cpqRackEnclosureNameChanged": cpqRackEnclosureNameChanged,
       "cpqRackEnclosureRemoved": cpqRackEnclosureRemoved,
       "cpqRackEnclosureInserted": cpqRackEnclosureInserted,
       "cpqRackEnclosureTempFailed": cpqRackEnclosureTempFailed,
       "cpqRackEnclosureTempDegraded": cpqRackEnclosureTempDegraded,
       "cpqRackEnclosureTempOk": cpqRackEnclosureTempOk,
       "cpqRackEnclosureFanFailed": cpqRackEnclosureFanFailed,
       "cpqRackEnclosureFanDegraded": cpqRackEnclosureFanDegraded,
       "cpqRackEnclosureFanOk": cpqRackEnclosureFanOk,
       "cpqRackEnclosureFanRemoved": cpqRackEnclosureFanRemoved,
       "cpqRackEnclosureFanInserted": cpqRackEnclosureFanInserted,
       "cpqRackPowerSupplyFailed": cpqRackPowerSupplyFailed,
       "cpqRackPowerSupplyDegraded": cpqRackPowerSupplyDegraded,
       "cpqRackPowerSupplyOk": cpqRackPowerSupplyOk,
       "cpqRackPowerSupplyRemoved": cpqRackPowerSupplyRemoved,
       "cpqRackPowerSupplyInserted": cpqRackPowerSupplyInserted,
       "cpqRackPowerSubsystemNotRedundant": cpqRackPowerSubsystemNotRedundant,
       "cpqRackPowerSubsystemLineVoltageProblem": cpqRackPowerSubsystemLineVoltageProblem,
       "cpqRackPowerSubsystemOverloadCondition": cpqRackPowerSubsystemOverloadCondition,
       "cpqRackPowerShedAutoShutdown": cpqRackPowerShedAutoShutdown,
       "cpqRackServerPowerOnFailedNotRedundant": cpqRackServerPowerOnFailedNotRedundant,
       "cpqRackServerPowerOnFailedNotEnoughPower": cpqRackServerPowerOnFailedNotEnoughPower,
       "cpqRackServerPowerOnFailedEnclosureNotFound": cpqRackServerPowerOnFailedEnclosureNotFound,
       "cpqRackServerPowerOnFailedPowerChassisNotFound": cpqRackServerPowerOnFailedPowerChassisNotFound,
       "cpqRackServerPowerOnManualOverride": cpqRackServerPowerOnManualOverride,
       "cpqRackFuseOpen": cpqRackFuseOpen,
       "cpqRackServerBladeRemoved": cpqRackServerBladeRemoved,
       "cpqRackServerBladeInserted": cpqRackServerBladeInserted,
       "cpqRackPowerChassisNotLoadBalanced": cpqRackPowerChassisNotLoadBalanced,
       "cpqRackPowerChassisDcPowerProblem": cpqRackPowerChassisDcPowerProblem,
       "cpqRackPowerChassisAcFacilityPowerExceeded": cpqRackPowerChassisAcFacilityPowerExceeded,
       "cpqRackPowerUnknownPowerConsumption": cpqRackPowerUnknownPowerConsumption,
       "cpqRackPowerChassisLoadBalancingWireMissing": cpqRackPowerChassisLoadBalancingWireMissing,
       "cpqRackPowerChassisTooManyPowerChassis": cpqRackPowerChassisTooManyPowerChassis,
       "cpqRackPowerChassisConfigError": cpqRackPowerChassisConfigError,
       "cpqRackEnclosureManagerDegraded": cpqRackEnclosureManagerDegraded,
       "cpqRackEnclosureManagerOk": cpqRackEnclosureManagerOk,
       "cpqRackEnclosureManagerRemoved": cpqRackEnclosureManagerRemoved,
       "cpqRackEnclosureManagerInserted": cpqRackEnclosureManagerInserted,
       "cpqRackManagerPrimaryRole": cpqRackManagerPrimaryRole,
       "cpqRackServerBladeEKeyingFailed": cpqRackServerBladeEKeyingFailed,
       "cpqRackServerBladeEKeyingOK": cpqRackServerBladeEKeyingOK,
       "cpqRackNetConnectorRemoved": cpqRackNetConnectorRemoved,
       "cpqRackNetConnectorInserted": cpqRackNetConnectorInserted,
       "cpqRackNetConnectorFailed": cpqRackNetConnectorFailed,
       "cpqRackNetConnectorDegraded": cpqRackNetConnectorDegraded,
       "cpqRackNetConnectorOk": cpqRackNetConnectorOk,
       "cpqRackServerBladeToLowPower": cpqRackServerBladeToLowPower,
       "cpqRackServerBladeRemoved2": cpqRackServerBladeRemoved2,
       "cpqRackServerBladeInserted2": cpqRackServerBladeInserted2,
       "cpqRackServerBladeStatusRepaired": cpqRackServerBladeStatusRepaired,
       "cpqRackServerBladeStatusDegraded": cpqRackServerBladeStatusDegraded,
       "cpqRackServerBladeStatusCritical": cpqRackServerBladeStatusCritical,
       "cpqRackServerBladeGrpCapTimeout": cpqRackServerBladeGrpCapTimeout,
       "cpqRackServerBladeUnexpectedShutdown": cpqRackServerBladeUnexpectedShutdown,
       "cpqRackServerBladeMangementControllerFirmwareUpdating": cpqRackServerBladeMangementControllerFirmwareUpdating,
       "cpqRackServerBladeMangementControllerFirmwareUpdateComplete": cpqRackServerBladeMangementControllerFirmwareUpdateComplete,
       "cpqRackServerBladeSystemBIOSFirmwareUpdating": cpqRackServerBladeSystemBIOSFirmwareUpdating,
       "cpqRackServerBladeSystemBIOSFirmwareUpdateCompleted": cpqRackServerBladeSystemBIOSFirmwareUpdateCompleted,
       "cpqRackServerBladeFrontIOBlankingActive": cpqRackServerBladeFrontIOBlankingActive,
       "cpqRackServerBladeRemoteFrontIOBlankingInactive": cpqRackServerBladeRemoteFrontIOBlankingInactive,
       "cpqRackServerBladeDiagnosticAdaptorInserted": cpqRackServerBladeDiagnosticAdaptorInserted,
       "cpqRackServerBladeDiagnosticAdaptorRemoved": cpqRackServerBladeDiagnosticAdaptorRemoved,
       "cpqRackServerBladeEnteredPXEBootMode": cpqRackServerBladeEnteredPXEBootMode,
       "cpqRackServerBladeExitedPXEBootMode": cpqRackServerBladeExitedPXEBootMode,
       "cpqRackServerBladeWarmReset": cpqRackServerBladeWarmReset,
       "cpqRackServerBladePOSTCompleted": cpqRackServerBladePOSTCompleted,
       "cpqRackServerBladePoweredOn": cpqRackServerBladePoweredOn,
       "cpqRackServerBladePoweredOff": cpqRackServerBladePoweredOff,
       "cpqRackInfo": cpqRackInfo,
       "cpqRackMibRev": cpqRackMibRev,
       "cpqRackMibRevMajor": cpqRackMibRevMajor,
       "cpqRackMibRevMinor": cpqRackMibRevMinor,
       "cpqRackMibCondition": cpqRackMibCondition,
       "cpqRackComponent": cpqRackComponent,
       "cpqRackInterface": cpqRackInterface,
       "cpqRackOsCommon": cpqRackOsCommon,
       "cpqRackOsCommonPollFreq": cpqRackOsCommonPollFreq,
       "cpqRackAsset": cpqRackAsset,
       "cpqRackAssetTable": cpqRackAssetTable,
       "cpqRackAssetEntry": cpqRackAssetEntry,
       "cpqRackAssetIndex": cpqRackAssetIndex,
       "cpqRackName": cpqRackName,
       "cpqRackUid": cpqRackUid,
       "cpqRackSerialNum": cpqRackSerialNum,
       "cpqRackTrapSequenceNum": cpqRackTrapSequenceNum,
       "cpqRackHeight": cpqRackHeight,
       "cpqRackWidth": cpqRackWidth,
       "cpqRackDepth": cpqRackDepth,
       "cpqRackEnclosure": cpqRackEnclosure,
       "cpqRackCommonEnclosure": cpqRackCommonEnclosure,
       "cpqRackCommonEnclosureTable": cpqRackCommonEnclosureTable,
       "cpqRackCommonEnclosureEntry": cpqRackCommonEnclosureEntry,
       "cpqRackCommonEnclosureRack": cpqRackCommonEnclosureRack,
       "cpqRackCommonEnclosureIndex": cpqRackCommonEnclosureIndex,
       "cpqRackCommonEnclosureModel": cpqRackCommonEnclosureModel,
       "cpqRackCommonEnclosureAssetTag": cpqRackCommonEnclosureAssetTag,
       "cpqRackCommonEnclosurePartNumber": cpqRackCommonEnclosurePartNumber,
       "cpqRackCommonEnclosureSparePartNumber": cpqRackCommonEnclosureSparePartNumber,
       "cpqRackCommonEnclosureSerialNum": cpqRackCommonEnclosureSerialNum,
       "cpqRackCommonEnclosureFWRev": cpqRackCommonEnclosureFWRev,
       "cpqRackCommonEnclosureName": cpqRackCommonEnclosureName,
       "cpqRackCommonEnclosureNeighborNamePrev": cpqRackCommonEnclosureNeighborNamePrev,
       "cpqRackCommonEnclosureNeighborNameNext": cpqRackCommonEnclosureNeighborNameNext,
       "cpqRackCommonEnclosureHeight": cpqRackCommonEnclosureHeight,
       "cpqRackCommonEnclosureWidth": cpqRackCommonEnclosureWidth,
       "cpqRackCommonEnclosureDepth": cpqRackCommonEnclosureDepth,
       "cpqRackCommonEnclosureTrapSequenceNum": cpqRackCommonEnclosureTrapSequenceNum,
       "cpqRackCommonEnclosureCondition": cpqRackCommonEnclosureCondition,
       "cpqRackCommonEnclosureHasServerBlades": cpqRackCommonEnclosureHasServerBlades,
       "cpqRackCommonEnclosureHasPowerSupplies": cpqRackCommonEnclosureHasPowerSupplies,
       "cpqRackCommonEnclosureHasNetConnectors": cpqRackCommonEnclosureHasNetConnectors,
       "cpqRackCommonEnclosureHasTempSensors": cpqRackCommonEnclosureHasTempSensors,
       "cpqRackCommonEnclosureHasFans": cpqRackCommonEnclosureHasFans,
       "cpqRackCommonEnclosureHasFuses": cpqRackCommonEnclosureHasFuses,
       "cpqRackCommonEnclosureMgmtUID": cpqRackCommonEnclosureMgmtUID,
       "cpqRackCommonEnclosureSerialNumPrev": cpqRackCommonEnclosureSerialNumPrev,
       "cpqRackCommonEnclosureSerialNumNext": cpqRackCommonEnclosureSerialNumNext,
       "cpqRackCommonEnclosureAddress": cpqRackCommonEnclosureAddress,
       "cpqRackCommonEnclosureProductId": cpqRackCommonEnclosureProductId,
       "cpqRackCommonEnclosureProductIdPrev": cpqRackCommonEnclosureProductIdPrev,
       "cpqRackCommonEnclosureProductIdNext": cpqRackCommonEnclosureProductIdNext,
       "cpqRackCommonEnclosureUUID": cpqRackCommonEnclosureUUID,
       "cpqRackCommonEnclosureUUIDPrev": cpqRackCommonEnclosureUUIDPrev,
       "cpqRackCommonEnclosureUUIDNext": cpqRackCommonEnclosureUUIDNext,
       "cpqRackCommonEnclosureHasManagers": cpqRackCommonEnclosureHasManagers,
       "cpqRackCommonEnclosureTempTable": cpqRackCommonEnclosureTempTable,
       "cpqRackCommonEnclosureTempEntry": cpqRackCommonEnclosureTempEntry,
       "cpqRackCommonEnclosureTempRack": cpqRackCommonEnclosureTempRack,
       "cpqRackCommonEnclosureTempChassis": cpqRackCommonEnclosureTempChassis,
       "cpqRackCommonEnclosureTempSensorIndex": cpqRackCommonEnclosureTempSensorIndex,
       "cpqRackCommonEnclosureTempSensorEnclosureName": cpqRackCommonEnclosureTempSensorEnclosureName,
       "cpqRackCommonEnclosureTempLocation": cpqRackCommonEnclosureTempLocation,
       "cpqRackCommonEnclosureTempCurrent": cpqRackCommonEnclosureTempCurrent,
       "cpqRackCommonEnclosureTempThreshold": cpqRackCommonEnclosureTempThreshold,
       "cpqRackCommonEnclosureTempCondition": cpqRackCommonEnclosureTempCondition,
       "cpqRackCommonEnclosureTempType": cpqRackCommonEnclosureTempType,
       "cpqRackCommonEnclosureTempSensorEnclosureSerialNum": cpqRackCommonEnclosureTempSensorEnclosureSerialNum,
       "cpqRackCommonEnclosureFanTable": cpqRackCommonEnclosureFanTable,
       "cpqRackCommonEnclosureFanEntry": cpqRackCommonEnclosureFanEntry,
       "cpqRackCommonEnclosureFanRack": cpqRackCommonEnclosureFanRack,
       "cpqRackCommonEnclosureFanChassis": cpqRackCommonEnclosureFanChassis,
       "cpqRackCommonEnclosureFanIndex": cpqRackCommonEnclosureFanIndex,
       "cpqRackCommonEnclosureFanEnclosureName": cpqRackCommonEnclosureFanEnclosureName,
       "cpqRackCommonEnclosureFanLocation": cpqRackCommonEnclosureFanLocation,
       "cpqRackCommonEnclosureFanPartNumber": cpqRackCommonEnclosureFanPartNumber,
       "cpqRackCommonEnclosureFanSparePartNumber": cpqRackCommonEnclosureFanSparePartNumber,
       "cpqRackCommonEnclosureFanPresent": cpqRackCommonEnclosureFanPresent,
       "cpqRackCommonEnclosureFanRedundant": cpqRackCommonEnclosureFanRedundant,
       "cpqRackCommonEnclosureFanRedundantGroupId": cpqRackCommonEnclosureFanRedundantGroupId,
       "cpqRackCommonEnclosureFanCondition": cpqRackCommonEnclosureFanCondition,
       "cpqRackCommonEnclosureFanEnclosureSerialNum": cpqRackCommonEnclosureFanEnclosureSerialNum,
       "cpqRackCommonEnclosureFuseTable": cpqRackCommonEnclosureFuseTable,
       "cpqRackCommonEnclosureFuseEntry": cpqRackCommonEnclosureFuseEntry,
       "cpqRackCommonEnclosureFuseRack": cpqRackCommonEnclosureFuseRack,
       "cpqRackCommonEnclosureFuseChassis": cpqRackCommonEnclosureFuseChassis,
       "cpqRackCommonEnclosureFuseIndex": cpqRackCommonEnclosureFuseIndex,
       "cpqRackCommonEnclosureFuseEnclosureName": cpqRackCommonEnclosureFuseEnclosureName,
       "cpqRackCommonEnclosureFuseLocation": cpqRackCommonEnclosureFuseLocation,
       "cpqRackCommonEnclosureFusePresent": cpqRackCommonEnclosureFusePresent,
       "cpqRackCommonEnclosureFuseCondition": cpqRackCommonEnclosureFuseCondition,
       "cpqRackCommonEnclosureFruTable": cpqRackCommonEnclosureFruTable,
       "cpqRackCommonEnclosureFruEntry": cpqRackCommonEnclosureFruEntry,
       "cpqRackCommonEnclosureFruRack": cpqRackCommonEnclosureFruRack,
       "cpqRackCommonEnclosureFruChassis": cpqRackCommonEnclosureFruChassis,
       "cpqRackCommonEnclosureFruIndex": cpqRackCommonEnclosureFruIndex,
       "cpqRackCommonEnclosureFruEnclosureName": cpqRackCommonEnclosureFruEnclosureName,
       "cpqRackCommonEnclosureFruDescription": cpqRackCommonEnclosureFruDescription,
       "cpqRackCommonEnclosureFruLocation": cpqRackCommonEnclosureFruLocation,
       "cpqRackCommonEnclosureFruAssemblyPartNumber": cpqRackCommonEnclosureFruAssemblyPartNumber,
       "cpqRackCommonEnclosureFruSparePartNumber": cpqRackCommonEnclosureFruSparePartNumber,
       "cpqRackCommonEnclosureFruAutoRev": cpqRackCommonEnclosureFruAutoRev,
       "cpqRackCommonEnclosureFruSerialNum": cpqRackCommonEnclosureFruSerialNum,
       "cpqRackCommonEnclosureManagerTable": cpqRackCommonEnclosureManagerTable,
       "cpqRackCommonEnclosureManagerEntry": cpqRackCommonEnclosureManagerEntry,
       "cpqRackCommonEnclosureManagerRack": cpqRackCommonEnclosureManagerRack,
       "cpqRackCommonEnclosureManagerChassis": cpqRackCommonEnclosureManagerChassis,
       "cpqRackCommonEnclosureManagerIndex": cpqRackCommonEnclosureManagerIndex,
       "cpqRackCommonEnclosureManagerEnclosureName": cpqRackCommonEnclosureManagerEnclosureName,
       "cpqRackCommonEnclosureManagerLocation": cpqRackCommonEnclosureManagerLocation,
       "cpqRackCommonEnclosureManagerPartNumber": cpqRackCommonEnclosureManagerPartNumber,
       "cpqRackCommonEnclosureManagerSparePartNumber": cpqRackCommonEnclosureManagerSparePartNumber,
       "cpqRackCommonEnclosureManagerSerialNum": cpqRackCommonEnclosureManagerSerialNum,
       "cpqRackCommonEnclosureManagerRole": cpqRackCommonEnclosureManagerRole,
       "cpqRackCommonEnclosureManagerPresent": cpqRackCommonEnclosureManagerPresent,
       "cpqRackCommonEnclosureManagerRedundant": cpqRackCommonEnclosureManagerRedundant,
       "cpqRackCommonEnclosureManagerCondition": cpqRackCommonEnclosureManagerCondition,
       "cpqRackCommonEnclosureManagerEnclosureSerialNum": cpqRackCommonEnclosureManagerEnclosureSerialNum,
       "cpqRackCommonEnclosureManagerUUID": cpqRackCommonEnclosureManagerUUID,
       "cpqRackCommonEnclosureManagerFWRev": cpqRackCommonEnclosureManagerFWRev,
       "cpqRackServerEnclosure": cpqRackServerEnclosure,
       "cpqRackServerEnclosureTable": cpqRackServerEnclosureTable,
       "cpqRackServerEnclosureEntry": cpqRackServerEnclosureEntry,
       "cpqRackServerEnclosureRack": cpqRackServerEnclosureRack,
       "cpqRackServerEnclosureIndex": cpqRackServerEnclosureIndex,
       "cpqRackServerEnclosureName": cpqRackServerEnclosureName,
       "cpqRackServerEnclosureMaxNumBlades": cpqRackServerEnclosureMaxNumBlades,
       "cpqRackServerEnclosureMaxNumBladesX": cpqRackServerEnclosureMaxNumBladesX,
       "cpqRackServerEnclosureMaxNumBladesY": cpqRackServerEnclosureMaxNumBladesY,
       "cpqRackPowerEnclosure": cpqRackPowerEnclosure,
       "cpqRackPowerEnclosureTable": cpqRackPowerEnclosureTable,
       "cpqRackPowerEnclosureEntry": cpqRackPowerEnclosureEntry,
       "cpqRackPowerEnclosureRack": cpqRackPowerEnclosureRack,
       "cpqRackPowerEnclosureIndex": cpqRackPowerEnclosureIndex,
       "cpqRackPowerEnclosureName": cpqRackPowerEnclosureName,
       "cpqRackPowerEnclosureMgmtBoardSerialNum": cpqRackPowerEnclosureMgmtBoardSerialNum,
       "cpqRackPowerEnclosureRedundant": cpqRackPowerEnclosureRedundant,
       "cpqRackPowerEnclosureLoadBalanced": cpqRackPowerEnclosureLoadBalanced,
       "cpqRackPowerEnclosureInputPwrType": cpqRackPowerEnclosureInputPwrType,
       "cpqRackPowerEnclosurePwrFeedMax": cpqRackPowerEnclosurePwrFeedMax,
       "cpqRackPowerEnclosureCondition": cpqRackPowerEnclosureCondition,
       "cpqRackPowerEnclosureBladeAutopoweron": cpqRackPowerEnclosureBladeAutopoweron,
       "cpqRackServer": cpqRackServer,
       "cpqRackServerBlade": cpqRackServerBlade,
       "cpqRackServerBladeTable": cpqRackServerBladeTable,
       "cpqRackServerBladeEntry": cpqRackServerBladeEntry,
       "cpqRackServerBladeRack": cpqRackServerBladeRack,
       "cpqRackServerBladeChassis": cpqRackServerBladeChassis,
       "cpqRackServerBladeIndex": cpqRackServerBladeIndex,
       "cpqRackServerBladeName": cpqRackServerBladeName,
       "cpqRackServerBladeEnclosureName": cpqRackServerBladeEnclosureName,
       "cpqRackServerBladePartNumber": cpqRackServerBladePartNumber,
       "cpqRackServerBladeSparePartNumber": cpqRackServerBladeSparePartNumber,
       "cpqRackServerBladePosition": cpqRackServerBladePosition,
       "cpqRackServerBladeHeight": cpqRackServerBladeHeight,
       "cpqRackServerBladeWidth": cpqRackServerBladeWidth,
       "cpqRackServerBladeDepth": cpqRackServerBladeDepth,
       "cpqRackServerBladePresent": cpqRackServerBladePresent,
       "cpqRackServerBladeHasFuses": cpqRackServerBladeHasFuses,
       "cpqRackServerBladeEnclosureSerialNum": cpqRackServerBladeEnclosureSerialNum,
       "cpqRackServerBladeSlotsUsed": cpqRackServerBladeSlotsUsed,
       "cpqRackServerBladeSerialNum": cpqRackServerBladeSerialNum,
       "cpqRackServerBladeProductId": cpqRackServerBladeProductId,
       "cpqRackServerBladeUid": cpqRackServerBladeUid,
       "cpqRackServerBladeSlotsUsedX": cpqRackServerBladeSlotsUsedX,
       "cpqRackServerBladeSlotsUsedY": cpqRackServerBladeSlotsUsedY,
       "cpqRackServerBladeStatus": cpqRackServerBladeStatus,
       "cpqRackServerBladeFaultMajor": cpqRackServerBladeFaultMajor,
       "cpqRackServerBladeFaultMinor": cpqRackServerBladeFaultMinor,
       "cpqRackServerBladeFaultDiagnosticString": cpqRackServerBladeFaultDiagnosticString,
       "cpqRackServerBladePowered": cpqRackServerBladePowered,
       "cpqRackServerBladeUIDState": cpqRackServerBladeUIDState,
       "cpqRackServerBladeSystemBIOSRevision": cpqRackServerBladeSystemBIOSRevision,
       "cpqRackServerBladeSystemBIOSFlashingStatus": cpqRackServerBladeSystemBIOSFlashingStatus,
       "cpqRackServerBladeHasManagementDevice": cpqRackServerBladeHasManagementDevice,
       "cpqRackServerBladeManagementDeviceFirmwareRevision": cpqRackServerBladeManagementDeviceFirmwareRevision,
       "cpqRackServerBladeManagementDeviceFirmwareFlashingStatus": cpqRackServerBladeManagementDeviceFirmwareFlashingStatus,
       "cpqRackServerBladeDiagnosticAdaptorPresence": cpqRackServerBladeDiagnosticAdaptorPresence,
       "cpqRackServerBladeASREnabled": cpqRackServerBladeASREnabled,
       "cpqRackServerBladeFrontIOBlankingModeStatus": cpqRackServerBladeFrontIOBlankingModeStatus,
       "cpqRackServerBladePOSTStatus": cpqRackServerBladePOSTStatus,
       "cpqRackServerBladePXEBootModeStatus": cpqRackServerBladePXEBootModeStatus,
       "cpqRackServerBladePendingBootOrderChange": cpqRackServerBladePendingBootOrderChange,
       "cpqRackServerNetworking": cpqRackServerNetworking,
       "cpqRackServerNetworkingTable": cpqRackServerNetworkingTable,
       "cpqRackServerNetworkingEntry": cpqRackServerNetworkingEntry,
       "cpqRackServerNetworkingRack": cpqRackServerNetworkingRack,
       "cpqRackServerNetworkingChassis": cpqRackServerNetworkingChassis,
       "cpqRackServerNetworkingIndex": cpqRackServerNetworkingIndex,
       "cpqRackServerNetworkingName": cpqRackServerNetworkingName,
       "cpqRackServerNetworkingEnclosureName": cpqRackServerNetworkingEnclosureName,
       "cpqRackServerNetworkingEthernetInterfaces": cpqRackServerNetworkingEthernetInterfaces,
       "cpqRackServerNetworkingEthernetMACAddress": cpqRackServerNetworkingEthernetMACAddress,
       "cpqRackServerTempSensor": cpqRackServerTempSensor,
       "cpqRackServerTempSensorTable": cpqRackServerTempSensorTable,
       "cpqRackServerTempSensorEntry": cpqRackServerTempSensorEntry,
       "cpqRackServerTempSensorRack": cpqRackServerTempSensorRack,
       "cpqRackServerTempSensorChassis": cpqRackServerTempSensorChassis,
       "cpqRackServerTempSensorIndex": cpqRackServerTempSensorIndex,
       "cpqRackServerTempSensorName": cpqRackServerTempSensorName,
       "cpqRackServerTempSensorEnclosureName": cpqRackServerTempSensorEnclosureName,
       "cpqRackServerTempSensorCount": cpqRackServerTempSensorCount,
       "cpqRackServerTempSensorLocation": cpqRackServerTempSensorLocation,
       "cpqRackServerTempSensorCurrent": cpqRackServerTempSensorCurrent,
       "cpqRackServerTempSensorThreshold": cpqRackServerTempSensorThreshold,
       "cpqRackServerTempSensorCondition": cpqRackServerTempSensorCondition,
       "cpqRackServerTempSensorType": cpqRackServerTempSensorType,
       "cpqRackPower": cpqRackPower,
       "cpqRackPowerSupply": cpqRackPowerSupply,
       "cpqRackPowerSupplyTable": cpqRackPowerSupplyTable,
       "cpqRackPowerSupplyEntry": cpqRackPowerSupplyEntry,
       "cpqRackPowerSupplyRack": cpqRackPowerSupplyRack,
       "cpqRackPowerSupplyChassis": cpqRackPowerSupplyChassis,
       "cpqRackPowerSupplyIndex": cpqRackPowerSupplyIndex,
       "cpqRackPowerSupplyEnclosureName": cpqRackPowerSupplyEnclosureName,
       "cpqRackPowerSupplySerialNum": cpqRackPowerSupplySerialNum,
       "cpqRackPowerSupplyPartNumber": cpqRackPowerSupplyPartNumber,
       "cpqRackPowerSupplySparePartNumber": cpqRackPowerSupplySparePartNumber,
       "cpqRackPowerSupplyFWRev": cpqRackPowerSupplyFWRev,
       "cpqRackPowerSupplyMaxPwrOutput": cpqRackPowerSupplyMaxPwrOutput,
       "cpqRackPowerSupplyCurPwrOutput": cpqRackPowerSupplyCurPwrOutput,
       "cpqRackPowerSupplyPosition": cpqRackPowerSupplyPosition,
       "cpqRackPowerSupplyIntakeTemp": cpqRackPowerSupplyIntakeTemp,
       "cpqRackPowerSupplyExhaustTemp": cpqRackPowerSupplyExhaustTemp,
       "cpqRackPowerSupplyStatus": cpqRackPowerSupplyStatus,
       "cpqRackPowerSupplyInputLineStatus": cpqRackPowerSupplyInputLineStatus,
       "cpqRackPowerSupplyPresent": cpqRackPowerSupplyPresent,
       "cpqRackPowerSupplyCondition": cpqRackPowerSupplyCondition,
       "cpqRackPowerSupplyEnclosureSerialNum": cpqRackPowerSupplyEnclosureSerialNum,
       "cpqRackNetwork": cpqRackNetwork,
       "cpqRackNetConnector": cpqRackNetConnector,
       "cpqRackNetConnectorTable": cpqRackNetConnectorTable,
       "cpqRackNetConnectorEntry": cpqRackNetConnectorEntry,
       "cpqRackNetConnectorRack": cpqRackNetConnectorRack,
       "cpqRackNetConnectorChassis": cpqRackNetConnectorChassis,
       "cpqRackNetConnectorIndex": cpqRackNetConnectorIndex,
       "cpqRackNetConnectorEnclosureName": cpqRackNetConnectorEnclosureName,
       "cpqRackNetConnectorName": cpqRackNetConnectorName,
       "cpqRackNetConnectorModel": cpqRackNetConnectorModel,
       "cpqRackNetConnectorSerialNum": cpqRackNetConnectorSerialNum,
       "cpqRackNetConnectorPartNumber": cpqRackNetConnectorPartNumber,
       "cpqRackNetConnectorSparePartNumber": cpqRackNetConnectorSparePartNumber,
       "cpqRackNetConnectorFWRev": cpqRackNetConnectorFWRev,
       "cpqRackNetConnectorType": cpqRackNetConnectorType,
       "cpqRackNetConnectorLocation": cpqRackNetConnectorLocation,
       "cpqRackNetConnectorPresent": cpqRackNetConnectorPresent,
       "cpqRackNetConnectorHasFuses": cpqRackNetConnectorHasFuses,
       "cpqRackNetConnectorEnclosureSerialNum": cpqRackNetConnectorEnclosureSerialNum,
       "cpqRackNetConnectorTechnologyType": cpqRackNetConnectorTechnologyType,
       "cpqRackNetConnectorDeviceType": cpqRackNetConnectorDeviceType,
       "cpqRackSysObjID": cpqRackSysObjID,
       "cpqRackSystemObjectIdentification": cpqRackSystemObjectIdentification}
)
