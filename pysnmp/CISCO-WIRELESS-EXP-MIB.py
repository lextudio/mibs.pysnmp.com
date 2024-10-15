# SNMP MIB module (CISCO-WIRELESS-EXP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-EXP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:36 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWirelessExpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52)
)
ciscoWirelessExpMIB.setRevisions(
        ("2005-12-27 10:03",
         "1999-05-13 20:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwrRadioExpMibObjects_ObjectIdentity = ObjectIdentity
cwrRadioExpMibObjects = _CwrRadioExpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1)
)
_CwrRadioFreqEntityGroup_ObjectIdentity = ObjectIdentity
cwrRadioFreqEntityGroup = _CwrRadioFreqEntityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1)
)
_CwrRfEntityTable_Object = MibTable
cwrRfEntityTable = _CwrRfEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwrRfEntityTable.setStatus("current")
_CwrRfEntityEntry_Object = MibTableRow
cwrRfEntityEntry = _CwrRfEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1)
)
cwrRfEntityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-EXP-MIB", "cwrRfEntityIndex"),
)
if mibBuilder.loadTexts:
    cwrRfEntityEntry.setStatus("current")


class _CwrRfEntityIndex_Type(Integer32):
    """Custom type cwrRfEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrRfEntityIndex_Type.__name__ = "Integer32"
_CwrRfEntityIndex_Object = MibTableColumn
cwrRfEntityIndex = _CwrRfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 1),
    _CwrRfEntityIndex_Type()
)
cwrRfEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrRfEntityIndex.setStatus("current")
_CwrRfSwRevision_Type = Unsigned32
_CwrRfSwRevision_Object = MibTableColumn
cwrRfSwRevision = _CwrRfSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 2),
    _CwrRfSwRevision_Type()
)
cwrRfSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfSwRevision.setStatus("current")
_CwrRfAssemblyPartNumberClass_Type = Unsigned32
_CwrRfAssemblyPartNumberClass_Object = MibTableColumn
cwrRfAssemblyPartNumberClass = _CwrRfAssemblyPartNumberClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 3),
    _CwrRfAssemblyPartNumberClass_Type()
)
cwrRfAssemblyPartNumberClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfAssemblyPartNumberClass.setStatus("current")
_CwrRfAssemblyPartNumberBase_Type = Unsigned32
_CwrRfAssemblyPartNumberBase_Object = MibTableColumn
cwrRfAssemblyPartNumberBase = _CwrRfAssemblyPartNumberBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 4),
    _CwrRfAssemblyPartNumberBase_Type()
)
cwrRfAssemblyPartNumberBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfAssemblyPartNumberBase.setStatus("current")
_CwrRfAssemblyPartNumberVersion_Type = Unsigned32
_CwrRfAssemblyPartNumberVersion_Object = MibTableColumn
cwrRfAssemblyPartNumberVersion = _CwrRfAssemblyPartNumberVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 5),
    _CwrRfAssemblyPartNumberVersion_Type()
)
cwrRfAssemblyPartNumberVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfAssemblyPartNumberVersion.setStatus("current")
_CwrRfBoardPartNumberClass_Type = Unsigned32
_CwrRfBoardPartNumberClass_Object = MibTableColumn
cwrRfBoardPartNumberClass = _CwrRfBoardPartNumberClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 6),
    _CwrRfBoardPartNumberClass_Type()
)
cwrRfBoardPartNumberClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfBoardPartNumberClass.setStatus("current")
_CwrRfBoardPartNumberBase_Type = Unsigned32
_CwrRfBoardPartNumberBase_Object = MibTableColumn
cwrRfBoardPartNumberBase = _CwrRfBoardPartNumberBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 7),
    _CwrRfBoardPartNumberBase_Type()
)
cwrRfBoardPartNumberBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfBoardPartNumberBase.setStatus("current")
_CwrRfBoardPartNumberVersion_Type = Unsigned32
_CwrRfBoardPartNumberVersion_Object = MibTableColumn
cwrRfBoardPartNumberVersion = _CwrRfBoardPartNumberVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 8),
    _CwrRfBoardPartNumberVersion_Type()
)
cwrRfBoardPartNumberVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfBoardPartNumberVersion.setStatus("current")
_CwrRfBoardRevision_Type = DisplayString
_CwrRfBoardRevision_Object = MibTableColumn
cwrRfBoardRevision = _CwrRfBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 9),
    _CwrRfBoardRevision_Type()
)
cwrRfBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfBoardRevision.setStatus("current")
_CwrRfSerialNumber_Type = DisplayString
_CwrRfSerialNumber_Object = MibTableColumn
cwrRfSerialNumber = _CwrRfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 10),
    _CwrRfSerialNumber_Type()
)
cwrRfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfSerialNumber.setStatus("current")
_CwrRfManfDate_Type = DateAndTime
_CwrRfManfDate_Object = MibTableColumn
cwrRfManfDate = _CwrRfManfDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 11),
    _CwrRfManfDate_Type()
)
cwrRfManfDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfManfDate.setStatus("current")


class _CwrRfVendorId_Type(Integer32):
    """Custom type cwrRfVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CwrRfVendorId_Type.__name__ = "Integer32"
_CwrRfVendorId_Object = MibTableColumn
cwrRfVendorId = _CwrRfVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 12),
    _CwrRfVendorId_Type()
)
cwrRfVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfVendorId.setStatus("current")


class _CwrRfDuplexorIndex_Type(Integer32):
    """Custom type cwrRfDuplexorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrRfDuplexorIndex_Type.__name__ = "Integer32"
_CwrRfDuplexorIndex_Object = MibTableColumn
cwrRfDuplexorIndex = _CwrRfDuplexorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 13),
    _CwrRfDuplexorIndex_Type()
)
cwrRfDuplexorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfDuplexorIndex.setStatus("current")
_CwrIntFreqEntityTable_Object = MibTable
cwrIntFreqEntityTable = _CwrIntFreqEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwrIntFreqEntityTable.setStatus("current")
_CwrIntFreqEntityEntry_Object = MibTableRow
cwrIntFreqEntityEntry = _CwrIntFreqEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1)
)
cwrIntFreqEntityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrIntFreqEntityEntry.setStatus("current")
_CwrIfAssemblyPartNumberClass_Type = Unsigned32
_CwrIfAssemblyPartNumberClass_Object = MibTableColumn
cwrIfAssemblyPartNumberClass = _CwrIfAssemblyPartNumberClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 1),
    _CwrIfAssemblyPartNumberClass_Type()
)
cwrIfAssemblyPartNumberClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfAssemblyPartNumberClass.setStatus("current")
_CwrIfAssemblyPartNumberBase_Type = Unsigned32
_CwrIfAssemblyPartNumberBase_Object = MibTableColumn
cwrIfAssemblyPartNumberBase = _CwrIfAssemblyPartNumberBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 2),
    _CwrIfAssemblyPartNumberBase_Type()
)
cwrIfAssemblyPartNumberBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfAssemblyPartNumberBase.setStatus("current")
_CwrIfAssemblyPartNumberVersion_Type = Unsigned32
_CwrIfAssemblyPartNumberVersion_Object = MibTableColumn
cwrIfAssemblyPartNumberVersion = _CwrIfAssemblyPartNumberVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 3),
    _CwrIfAssemblyPartNumberVersion_Type()
)
cwrIfAssemblyPartNumberVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfAssemblyPartNumberVersion.setStatus("current")
_CwrIfBoardPartNumberClass_Type = Unsigned32
_CwrIfBoardPartNumberClass_Object = MibTableColumn
cwrIfBoardPartNumberClass = _CwrIfBoardPartNumberClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 4),
    _CwrIfBoardPartNumberClass_Type()
)
cwrIfBoardPartNumberClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfBoardPartNumberClass.setStatus("current")
_CwrIfBoardPartNumberBase_Type = Unsigned32
_CwrIfBoardPartNumberBase_Object = MibTableColumn
cwrIfBoardPartNumberBase = _CwrIfBoardPartNumberBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 5),
    _CwrIfBoardPartNumberBase_Type()
)
cwrIfBoardPartNumberBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfBoardPartNumberBase.setStatus("current")
_CwrIfBoardPartNumberVersion_Type = Unsigned32
_CwrIfBoardPartNumberVersion_Object = MibTableColumn
cwrIfBoardPartNumberVersion = _CwrIfBoardPartNumberVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 6),
    _CwrIfBoardPartNumberVersion_Type()
)
cwrIfBoardPartNumberVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfBoardPartNumberVersion.setStatus("current")
_CwrIfBoardRevision_Type = DisplayString
_CwrIfBoardRevision_Object = MibTableColumn
cwrIfBoardRevision = _CwrIfBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 7),
    _CwrIfBoardRevision_Type()
)
cwrIfBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfBoardRevision.setStatus("current")
_CwrIfSerialNumber_Type = DisplayString
_CwrIfSerialNumber_Object = MibTableColumn
cwrIfSerialNumber = _CwrIfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 8),
    _CwrIfSerialNumber_Type()
)
cwrIfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfSerialNumber.setStatus("current")
_CwrIfManfDate_Type = DateAndTime
_CwrIfManfDate_Object = MibTableColumn
cwrIfManfDate = _CwrIfManfDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 9),
    _CwrIfManfDate_Type()
)
cwrIfManfDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfManfDate.setStatus("current")


class _CwrIfVendorId_Type(Integer32):
    """Custom type cwrIfVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CwrIfVendorId_Type.__name__ = "Integer32"
_CwrIfVendorId_Object = MibTableColumn
cwrIfVendorId = _CwrIfVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 10),
    _CwrIfVendorId_Type()
)
cwrIfVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfVendorId.setStatus("current")
_CwrIfSwRevision_Type = Unsigned32
_CwrIfSwRevision_Object = MibTableColumn
cwrIfSwRevision = _CwrIfSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 11),
    _CwrIfSwRevision_Type()
)
cwrIfSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfSwRevision.setStatus("current")
_CwrRadioImageGroup_ObjectIdentity = ObjectIdentity
cwrRadioImageGroup = _CwrRadioImageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2)
)
_CwrImageTable_Object = MibTable
cwrImageTable = _CwrImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwrImageTable.setStatus("current")
_CwrImageEntry_Object = MibTableRow
cwrImageEntry = _CwrImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1)
)
cwrImageEntry.setIndexNames(
    (0, "CISCO-WIRELESS-EXP-MIB", "cwrImageIndex"),
)
if mibBuilder.loadTexts:
    cwrImageEntry.setStatus("current")


class _CwrImageIndex_Type(Integer32):
    """Custom type cwrImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrImageIndex_Type.__name__ = "Integer32"
_CwrImageIndex_Object = MibTableColumn
cwrImageIndex = _CwrImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 1),
    _CwrImageIndex_Type()
)
cwrImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrImageIndex.setStatus("current")


class _CwrImageNameUrl_Type(DisplayString):
    """Custom type cwrImageNameUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CwrImageNameUrl_Type.__name__ = "DisplayString"
_CwrImageNameUrl_Object = MibTableColumn
cwrImageNameUrl = _CwrImageNameUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 2),
    _CwrImageNameUrl_Type()
)
cwrImageNameUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrImageNameUrl.setStatus("current")


class _CwrImageState_Type(Integer32):
    """Custom type cwrImageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imageInvalid", 1),
          ("imageValid", 2))
    )


_CwrImageState_Type.__name__ = "Integer32"
_CwrImageState_Object = MibTableColumn
cwrImageState = _CwrImageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 3),
    _CwrImageState_Type()
)
cwrImageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageState.setStatus("current")
_CwrImageSize_Type = Unsigned32
_CwrImageSize_Object = MibTableColumn
cwrImageSize = _CwrImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 4),
    _CwrImageSize_Type()
)
cwrImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageSize.setStatus("current")
_CwrImageChipClass_Type = Unsigned32
_CwrImageChipClass_Object = MibTableColumn
cwrImageChipClass = _CwrImageChipClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 5),
    _CwrImageChipClass_Type()
)
cwrImageChipClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageChipClass.setStatus("current")
_CwrImageChipType_Type = Unsigned32
_CwrImageChipType_Object = MibTableColumn
cwrImageChipType = _CwrImageChipType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 6),
    _CwrImageChipType_Type()
)
cwrImageChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageChipType.setStatus("current")
_CwrImageCapability1_Type = Unsigned32
_CwrImageCapability1_Object = MibTableColumn
cwrImageCapability1 = _CwrImageCapability1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 7),
    _CwrImageCapability1_Type()
)
cwrImageCapability1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageCapability1.setStatus("current")
_CwrImageCapability2_Type = Unsigned32
_CwrImageCapability2_Object = MibTableColumn
cwrImageCapability2 = _CwrImageCapability2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 8),
    _CwrImageCapability2_Type()
)
cwrImageCapability2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageCapability2.setStatus("current")
_CwrImageVersion_Type = Unsigned32
_CwrImageVersion_Object = MibTableColumn
cwrImageVersion = _CwrImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 9),
    _CwrImageVersion_Type()
)
cwrImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageVersion.setStatus("current")


class _CwrImageTag_Type(DisplayString):
    """Custom type cwrImageTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CwrImageTag_Type.__name__ = "DisplayString"
_CwrImageTag_Object = MibTableColumn
cwrImageTag = _CwrImageTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 10),
    _CwrImageTag_Type()
)
cwrImageTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImageTag.setStatus("current")


class _CwrImageOp_Type(Integer32):
    """Custom type cwrImageOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("move", 3),
          ("nop", 0))
    )


_CwrImageOp_Type.__name__ = "Integer32"
_CwrImageOp_Object = MibTableColumn
cwrImageOp = _CwrImageOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 11),
    _CwrImageOp_Type()
)
cwrImageOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrImageOp.setStatus("current")
_CwrRadioLedGroup_ObjectIdentity = ObjectIdentity
cwrRadioLedGroup = _CwrRadioLedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3)
)
_CwrLedTable_Object = MibTable
cwrLedTable = _CwrLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwrLedTable.setStatus("current")
_CwrLedEntry_Object = MibTableRow
cwrLedEntry = _CwrLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1)
)
cwrLedEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WIRELESS-EXP-MIB", "cwrLedIndex"),
)
if mibBuilder.loadTexts:
    cwrLedEntry.setStatus("current")


class _CwrLedIndex_Type(Integer32):
    """Custom type cwrLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CwrLedIndex_Type.__name__ = "Integer32"
_CwrLedIndex_Object = MibTableColumn
cwrLedIndex = _CwrLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 1),
    _CwrLedIndex_Type()
)
cwrLedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrLedIndex.setStatus("current")
_CwrLedName_Type = DisplayString
_CwrLedName_Object = MibTableColumn
cwrLedName = _CwrLedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 2),
    _CwrLedName_Type()
)
cwrLedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLedName.setStatus("current")


class _CwrLedVerticalPosition_Type(Integer32):
    """Custom type cwrLedVerticalPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CwrLedVerticalPosition_Type.__name__ = "Integer32"
_CwrLedVerticalPosition_Object = MibTableColumn
cwrLedVerticalPosition = _CwrLedVerticalPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 3),
    _CwrLedVerticalPosition_Type()
)
cwrLedVerticalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLedVerticalPosition.setStatus("current")


class _CwrLedHorizontalPosition_Type(Integer32):
    """Custom type cwrLedHorizontalPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CwrLedHorizontalPosition_Type.__name__ = "Integer32"
_CwrLedHorizontalPosition_Object = MibTableColumn
cwrLedHorizontalPosition = _CwrLedHorizontalPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 4),
    _CwrLedHorizontalPosition_Type()
)
cwrLedHorizontalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLedHorizontalPosition.setStatus("current")


class _CwrLedMode_Type(Integer32):
    """Custom type cwrLedMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("forceBlinkBoth", 8),
          ("forceBlinkGreen", 6),
          ("forceBlinkYellow", 7),
          ("forceOff", 3),
          ("forceSolidGreen", 4),
          ("forceSolidYellow", 5),
          ("latched", 2))
    )


_CwrLedMode_Type.__name__ = "Integer32"
_CwrLedMode_Object = MibTableColumn
cwrLedMode = _CwrLedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 5),
    _CwrLedMode_Type()
)
cwrLedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLedMode.setStatus("current")


class _CwrLedCurrentColor_Type(Integer32):
    """Custom type cwrLedCurrentColor based on Integer32"""
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
        *(("blinkGreen", 3),
          ("blinkGreenYellow", 5),
          ("blinkYellow", 4),
          ("green", 1),
          ("off", 6),
          ("yellow", 2))
    )


_CwrLedCurrentColor_Type.__name__ = "Integer32"
_CwrLedCurrentColor_Object = MibTableColumn
cwrLedCurrentColor = _CwrLedCurrentColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 6),
    _CwrLedCurrentColor_Type()
)
cwrLedCurrentColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLedCurrentColor.setStatus("current")
_CwrRadioDuplexorGroup_ObjectIdentity = ObjectIdentity
cwrRadioDuplexorGroup = _CwrRadioDuplexorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4)
)
_CwrDuplexorTable_Object = MibTable
cwrDuplexorTable = _CwrDuplexorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwrDuplexorTable.setStatus("current")
_CwrDuplexorEntry_Object = MibTableRow
cwrDuplexorEntry = _CwrDuplexorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1)
)
cwrDuplexorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-EXP-MIB", "cwrDuplexorIndex"),
)
if mibBuilder.loadTexts:
    cwrDuplexorEntry.setStatus("current")


class _CwrDuplexorIndex_Type(Integer32):
    """Custom type cwrDuplexorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrDuplexorIndex_Type.__name__ = "Integer32"
_CwrDuplexorIndex_Object = MibTableColumn
cwrDuplexorIndex = _CwrDuplexorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 1),
    _CwrDuplexorIndex_Type()
)
cwrDuplexorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrDuplexorIndex.setStatus("current")
_CwrDuplexorCiscoPartNumber_Type = DisplayString
_CwrDuplexorCiscoPartNumber_Object = MibTableColumn
cwrDuplexorCiscoPartNumber = _CwrDuplexorCiscoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 2),
    _CwrDuplexorCiscoPartNumber_Type()
)
cwrDuplexorCiscoPartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorCiscoPartNumber.setStatus("current")
_CwrDuplexorLoPassbandRange_Type = DisplayString
_CwrDuplexorLoPassbandRange_Object = MibTableColumn
cwrDuplexorLoPassbandRange = _CwrDuplexorLoPassbandRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 3),
    _CwrDuplexorLoPassbandRange_Type()
)
cwrDuplexorLoPassbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorLoPassbandRange.setStatus("current")
_CwrDuplexorHiPassbandRange_Type = DisplayString
_CwrDuplexorHiPassbandRange_Object = MibTableColumn
cwrDuplexorHiPassbandRange = _CwrDuplexorHiPassbandRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 4),
    _CwrDuplexorHiPassbandRange_Type()
)
cwrDuplexorHiPassbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorHiPassbandRange.setStatus("current")


class _CwrDuplexorReceivePassband_Type(Integer32):
    """Custom type cwrDuplexorReceivePassband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hiPassband", 2),
          ("loPassband", 1))
    )


_CwrDuplexorReceivePassband_Type.__name__ = "Integer32"
_CwrDuplexorReceivePassband_Object = MibTableColumn
cwrDuplexorReceivePassband = _CwrDuplexorReceivePassband_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 5),
    _CwrDuplexorReceivePassband_Type()
)
cwrDuplexorReceivePassband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorReceivePassband.setStatus("current")
_CwrDuplexorCLEICode_Type = DisplayString
_CwrDuplexorCLEICode_Object = MibTableColumn
cwrDuplexorCLEICode = _CwrDuplexorCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 6),
    _CwrDuplexorCLEICode_Type()
)
cwrDuplexorCLEICode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorCLEICode.setStatus("current")
_CwrDuplexorVendorName_Type = DisplayString
_CwrDuplexorVendorName_Object = MibTableColumn
cwrDuplexorVendorName = _CwrDuplexorVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 7),
    _CwrDuplexorVendorName_Type()
)
cwrDuplexorVendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorVendorName.setStatus("current")
_CwrDuplexorSerialNumber_Type = DisplayString
_CwrDuplexorSerialNumber_Object = MibTableColumn
cwrDuplexorSerialNumber = _CwrDuplexorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 8),
    _CwrDuplexorSerialNumber_Type()
)
cwrDuplexorSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrDuplexorSerialNumber.setStatus("current")
_CwrRadioExpConformance_ObjectIdentity = ObjectIdentity
cwrRadioExpConformance = _CwrRadioExpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2)
)
_CwrRadioExpCompliances_ObjectIdentity = ObjectIdentity
cwrRadioExpCompliances = _CwrRadioExpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 1)
)
_CwrRadioExpGroups_ObjectIdentity = ObjectIdentity
cwrRadioExpGroups = _CwrRadioExpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2)
)

# Managed Objects groups

cwrComplianceRadioRFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 1)
)
cwrComplianceRadioRFGroup.setObjects(
      *(("CISCO-WIRELESS-EXP-MIB", "cwrRfSwRevision"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberClass"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberBase"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberVersion"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberClass"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberBase"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberVersion"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardRevision"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfSerialNumber"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfManfDate"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfVendorId"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrRfDuplexorIndex"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberClass"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberBase"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberVersion"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberClass"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberBase"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberVersion"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardRevision"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfSerialNumber"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfManfDate"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfVendorId"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrIfSwRevision"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioRFGroup.setStatus("current")

cwrComplianceRadioImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 2)
)
cwrComplianceRadioImageGroup.setObjects(
      *(("CISCO-WIRELESS-EXP-MIB", "cwrImageNameUrl"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageState"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageSize"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageChipType"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageChipClass"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageCapability1"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageCapability2"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageVersion"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageTag"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrImageOp"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioImageGroup.setStatus("current")

cwrComplianceRadioLEDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 3)
)
cwrComplianceRadioLEDGroup.setObjects(
      *(("CISCO-WIRELESS-EXP-MIB", "cwrLedName"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrLedVerticalPosition"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrLedHorizontalPosition"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrLedMode"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrLedCurrentColor"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioLEDGroup.setStatus("current")

cwrComplianceRadioDuplexorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 4)
)
cwrComplianceRadioDuplexorGroup.setObjects(
      *(("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorCiscoPartNumber"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorLoPassbandRange"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorHiPassbandRange"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorReceivePassband"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorCLEICode"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorVendorName"),
        ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorSerialNumber"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioDuplexorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwrRadioExpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwrRadioExpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-EXP-MIB",
    **{"ciscoWirelessExpMIB": ciscoWirelessExpMIB,
       "cwrRadioExpMibObjects": cwrRadioExpMibObjects,
       "cwrRadioFreqEntityGroup": cwrRadioFreqEntityGroup,
       "cwrRfEntityTable": cwrRfEntityTable,
       "cwrRfEntityEntry": cwrRfEntityEntry,
       "cwrRfEntityIndex": cwrRfEntityIndex,
       "cwrRfSwRevision": cwrRfSwRevision,
       "cwrRfAssemblyPartNumberClass": cwrRfAssemblyPartNumberClass,
       "cwrRfAssemblyPartNumberBase": cwrRfAssemblyPartNumberBase,
       "cwrRfAssemblyPartNumberVersion": cwrRfAssemblyPartNumberVersion,
       "cwrRfBoardPartNumberClass": cwrRfBoardPartNumberClass,
       "cwrRfBoardPartNumberBase": cwrRfBoardPartNumberBase,
       "cwrRfBoardPartNumberVersion": cwrRfBoardPartNumberVersion,
       "cwrRfBoardRevision": cwrRfBoardRevision,
       "cwrRfSerialNumber": cwrRfSerialNumber,
       "cwrRfManfDate": cwrRfManfDate,
       "cwrRfVendorId": cwrRfVendorId,
       "cwrRfDuplexorIndex": cwrRfDuplexorIndex,
       "cwrIntFreqEntityTable": cwrIntFreqEntityTable,
       "cwrIntFreqEntityEntry": cwrIntFreqEntityEntry,
       "cwrIfAssemblyPartNumberClass": cwrIfAssemblyPartNumberClass,
       "cwrIfAssemblyPartNumberBase": cwrIfAssemblyPartNumberBase,
       "cwrIfAssemblyPartNumberVersion": cwrIfAssemblyPartNumberVersion,
       "cwrIfBoardPartNumberClass": cwrIfBoardPartNumberClass,
       "cwrIfBoardPartNumberBase": cwrIfBoardPartNumberBase,
       "cwrIfBoardPartNumberVersion": cwrIfBoardPartNumberVersion,
       "cwrIfBoardRevision": cwrIfBoardRevision,
       "cwrIfSerialNumber": cwrIfSerialNumber,
       "cwrIfManfDate": cwrIfManfDate,
       "cwrIfVendorId": cwrIfVendorId,
       "cwrIfSwRevision": cwrIfSwRevision,
       "cwrRadioImageGroup": cwrRadioImageGroup,
       "cwrImageTable": cwrImageTable,
       "cwrImageEntry": cwrImageEntry,
       "cwrImageIndex": cwrImageIndex,
       "cwrImageNameUrl": cwrImageNameUrl,
       "cwrImageState": cwrImageState,
       "cwrImageSize": cwrImageSize,
       "cwrImageChipClass": cwrImageChipClass,
       "cwrImageChipType": cwrImageChipType,
       "cwrImageCapability1": cwrImageCapability1,
       "cwrImageCapability2": cwrImageCapability2,
       "cwrImageVersion": cwrImageVersion,
       "cwrImageTag": cwrImageTag,
       "cwrImageOp": cwrImageOp,
       "cwrRadioLedGroup": cwrRadioLedGroup,
       "cwrLedTable": cwrLedTable,
       "cwrLedEntry": cwrLedEntry,
       "cwrLedIndex": cwrLedIndex,
       "cwrLedName": cwrLedName,
       "cwrLedVerticalPosition": cwrLedVerticalPosition,
       "cwrLedHorizontalPosition": cwrLedHorizontalPosition,
       "cwrLedMode": cwrLedMode,
       "cwrLedCurrentColor": cwrLedCurrentColor,
       "cwrRadioDuplexorGroup": cwrRadioDuplexorGroup,
       "cwrDuplexorTable": cwrDuplexorTable,
       "cwrDuplexorEntry": cwrDuplexorEntry,
       "cwrDuplexorIndex": cwrDuplexorIndex,
       "cwrDuplexorCiscoPartNumber": cwrDuplexorCiscoPartNumber,
       "cwrDuplexorLoPassbandRange": cwrDuplexorLoPassbandRange,
       "cwrDuplexorHiPassbandRange": cwrDuplexorHiPassbandRange,
       "cwrDuplexorReceivePassband": cwrDuplexorReceivePassband,
       "cwrDuplexorCLEICode": cwrDuplexorCLEICode,
       "cwrDuplexorVendorName": cwrDuplexorVendorName,
       "cwrDuplexorSerialNumber": cwrDuplexorSerialNumber,
       "cwrRadioExpConformance": cwrRadioExpConformance,
       "cwrRadioExpCompliances": cwrRadioExpCompliances,
       "cwrRadioExpCompliance": cwrRadioExpCompliance,
       "cwrRadioExpGroups": cwrRadioExpGroups,
       "cwrComplianceRadioRFGroup": cwrComplianceRadioRFGroup,
       "cwrComplianceRadioImageGroup": cwrComplianceRadioImageGroup,
       "cwrComplianceRadioLEDGroup": cwrComplianceRadioLEDGroup,
       "cwrComplianceRadioDuplexorGroup": cwrComplianceRadioDuplexorGroup}
)
