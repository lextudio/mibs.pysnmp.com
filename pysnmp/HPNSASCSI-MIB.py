# SNMP MIB module (HPNSASCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSASCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:25 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaScsi_ObjectIdentity = ObjectIdentity
hpnsaScsi = _HpnsaScsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14)
)
_HpnsaScsiMibRev_ObjectIdentity = ObjectIdentity
hpnsaScsiMibRev = _HpnsaScsiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1)
)


class _HpnsaScsiMibRevMajor_Type(Integer32):
    """Custom type hpnsaScsiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaScsiMibRevMajor_Type.__name__ = "Integer32"
_HpnsaScsiMibRevMajor_Object = MibScalar
hpnsaScsiMibRevMajor = _HpnsaScsiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1, 1),
    _HpnsaScsiMibRevMajor_Type()
)
hpnsaScsiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiMibRevMajor.setStatus("mandatory")


class _HpnsaScsiMibRevMinor_Type(Integer32):
    """Custom type hpnsaScsiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaScsiMibRevMinor_Type.__name__ = "Integer32"
_HpnsaScsiMibRevMinor_Object = MibScalar
hpnsaScsiMibRevMinor = _HpnsaScsiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1, 2),
    _HpnsaScsiMibRevMinor_Type()
)
hpnsaScsiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiMibRevMinor.setStatus("mandatory")
_HpnsaScsiAgent_ObjectIdentity = ObjectIdentity
hpnsaScsiAgent = _HpnsaScsiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2)
)
_HpnsaScsiAgentModuleTable_Object = MibTable
hpnsaScsiAgentModuleTable = _HpnsaScsiAgentModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleTable.setStatus("mandatory")
_HpnsaScsiAgentModuleEntry_Object = MibTableRow
hpnsaScsiAgentModuleEntry = _HpnsaScsiAgentModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1)
)
hpnsaScsiAgentModuleEntry.setIndexNames(
    (0, "HPNSASCSI-MIB", "hpnsaScsiAgentModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleEntry.setStatus("mandatory")


class _HpnsaScsiAgentModuleIndex_Type(Integer32):
    """Custom type hpnsaScsiAgentModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaScsiAgentModuleIndex_Type.__name__ = "Integer32"
_HpnsaScsiAgentModuleIndex_Object = MibTableColumn
hpnsaScsiAgentModuleIndex = _HpnsaScsiAgentModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 1),
    _HpnsaScsiAgentModuleIndex_Type()
)
hpnsaScsiAgentModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleIndex.setStatus("mandatory")


class _HpnsaScsiAgentModuleName_Type(DisplayString):
    """Custom type hpnsaScsiAgentModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaScsiAgentModuleName_Type.__name__ = "DisplayString"
_HpnsaScsiAgentModuleName_Object = MibTableColumn
hpnsaScsiAgentModuleName = _HpnsaScsiAgentModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 2),
    _HpnsaScsiAgentModuleName_Type()
)
hpnsaScsiAgentModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleName.setStatus("mandatory")


class _HpnsaScsiAgentModuleVersion_Type(DisplayString):
    """Custom type hpnsaScsiAgentModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaScsiAgentModuleVersion_Type.__name__ = "DisplayString"
_HpnsaScsiAgentModuleVersion_Object = MibTableColumn
hpnsaScsiAgentModuleVersion = _HpnsaScsiAgentModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 3),
    _HpnsaScsiAgentModuleVersion_Type()
)
hpnsaScsiAgentModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleVersion.setStatus("mandatory")


class _HpnsaScsiAgentModuleDate_Type(OctetString):
    """Custom type hpnsaScsiAgentModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HpnsaScsiAgentModuleDate_Type.__name__ = "OctetString"
_HpnsaScsiAgentModuleDate_Object = MibTableColumn
hpnsaScsiAgentModuleDate = _HpnsaScsiAgentModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 4),
    _HpnsaScsiAgentModuleDate_Type()
)
hpnsaScsiAgentModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiAgentModuleDate.setStatus("mandatory")
_HpnsaScsiHba_ObjectIdentity = ObjectIdentity
hpnsaScsiHba = _HpnsaScsiHba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3)
)
_HpnsaScsiHbaTable_Object = MibTable
hpnsaScsiHbaTable = _HpnsaScsiHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaScsiHbaTable.setStatus("mandatory")
_HpnsaScsiHbaEntry_Object = MibTableRow
hpnsaScsiHbaEntry = _HpnsaScsiHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1)
)
hpnsaScsiHbaEntry.setIndexNames(
    (0, "HPNSASCSI-MIB", "hpnsaScsiHbaIndex"),
)
if mibBuilder.loadTexts:
    hpnsaScsiHbaEntry.setStatus("mandatory")


class _HpnsaScsiHbaIndex_Type(Integer32):
    """Custom type hpnsaScsiHbaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaScsiHbaIndex_Type.__name__ = "Integer32"
_HpnsaScsiHbaIndex_Object = MibTableColumn
hpnsaScsiHbaIndex = _HpnsaScsiHbaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 1),
    _HpnsaScsiHbaIndex_Type()
)
hpnsaScsiHbaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiHbaIndex.setStatus("mandatory")


class _HpnsaScsiHbaTargetId_Type(Integer32):
    """Custom type hpnsaScsiHbaTargetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaScsiHbaTargetId_Type.__name__ = "Integer32"
_HpnsaScsiHbaTargetId_Object = MibTableColumn
hpnsaScsiHbaTargetId = _HpnsaScsiHbaTargetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 2),
    _HpnsaScsiHbaTargetId_Type()
)
hpnsaScsiHbaTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiHbaTargetId.setStatus("mandatory")


class _HpnsaScsiHbaManagerId_Type(DisplayString):
    """Custom type hpnsaScsiHbaManagerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpnsaScsiHbaManagerId_Type.__name__ = "DisplayString"
_HpnsaScsiHbaManagerId_Object = MibTableColumn
hpnsaScsiHbaManagerId = _HpnsaScsiHbaManagerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 3),
    _HpnsaScsiHbaManagerId_Type()
)
hpnsaScsiHbaManagerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiHbaManagerId.setStatus("mandatory")


class _HpnsaScsiHbaHostAdapterId_Type(DisplayString):
    """Custom type hpnsaScsiHbaHostAdapterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpnsaScsiHbaHostAdapterId_Type.__name__ = "DisplayString"
_HpnsaScsiHbaHostAdapterId_Object = MibTableColumn
hpnsaScsiHbaHostAdapterId = _HpnsaScsiHbaHostAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 4),
    _HpnsaScsiHbaHostAdapterId_Type()
)
hpnsaScsiHbaHostAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiHbaHostAdapterId.setStatus("mandatory")
_HpnsaScsiDev_ObjectIdentity = ObjectIdentity
hpnsaScsiDev = _HpnsaScsiDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4)
)
_HpnsaScsiDevTable_Object = MibTable
hpnsaScsiDevTable = _HpnsaScsiDevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaScsiDevTable.setStatus("mandatory")
_HpnsaScsiDevEntry_Object = MibTableRow
hpnsaScsiDevEntry = _HpnsaScsiDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1)
)
hpnsaScsiDevEntry.setIndexNames(
    (0, "HPNSASCSI-MIB", "hpnsaScsiDevHbaIndex"),
    (0, "HPNSASCSI-MIB", "hpnsaScsiDevTargIdIndex"),
    (0, "HPNSASCSI-MIB", "hpnsaScsiDevLunIndex"),
)
if mibBuilder.loadTexts:
    hpnsaScsiDevEntry.setStatus("mandatory")


class _HpnsaScsiDevHbaIndex_Type(Integer32):
    """Custom type hpnsaScsiDevHbaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaScsiDevHbaIndex_Type.__name__ = "Integer32"
_HpnsaScsiDevHbaIndex_Object = MibTableColumn
hpnsaScsiDevHbaIndex = _HpnsaScsiDevHbaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 1),
    _HpnsaScsiDevHbaIndex_Type()
)
hpnsaScsiDevHbaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevHbaIndex.setStatus("mandatory")


class _HpnsaScsiDevTargIdIndex_Type(Integer32):
    """Custom type hpnsaScsiDevTargIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaScsiDevTargIdIndex_Type.__name__ = "Integer32"
_HpnsaScsiDevTargIdIndex_Object = MibTableColumn
hpnsaScsiDevTargIdIndex = _HpnsaScsiDevTargIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 2),
    _HpnsaScsiDevTargIdIndex_Type()
)
hpnsaScsiDevTargIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevTargIdIndex.setStatus("mandatory")


class _HpnsaScsiDevLunIndex_Type(Integer32):
    """Custom type hpnsaScsiDevLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaScsiDevLunIndex_Type.__name__ = "Integer32"
_HpnsaScsiDevLunIndex_Object = MibTableColumn
hpnsaScsiDevLunIndex = _HpnsaScsiDevLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 3),
    _HpnsaScsiDevLunIndex_Type()
)
hpnsaScsiDevLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevLunIndex.setStatus("mandatory")


class _HpnsaScsiDevType_Type(Integer32):
    """Custom type hpnsaScsiDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpnsaScsiDevType_Type.__name__ = "Integer32"
_HpnsaScsiDevType_Object = MibTableColumn
hpnsaScsiDevType = _HpnsaScsiDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 4),
    _HpnsaScsiDevType_Type()
)
hpnsaScsiDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevType.setStatus("mandatory")


class _HpnsaScsiDevRmb_Type(Integer32):
    """Custom type hpnsaScsiDevRmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaScsiDevRmb_Type.__name__ = "Integer32"
_HpnsaScsiDevRmb_Object = MibTableColumn
hpnsaScsiDevRmb = _HpnsaScsiDevRmb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 5),
    _HpnsaScsiDevRmb_Type()
)
hpnsaScsiDevRmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevRmb.setStatus("mandatory")


class _HpnsaScsiDevAnsiVer_Type(Integer32):
    """Custom type hpnsaScsiDevAnsiVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaScsiDevAnsiVer_Type.__name__ = "Integer32"
_HpnsaScsiDevAnsiVer_Object = MibTableColumn
hpnsaScsiDevAnsiVer = _HpnsaScsiDevAnsiVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 6),
    _HpnsaScsiDevAnsiVer_Type()
)
hpnsaScsiDevAnsiVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevAnsiVer.setStatus("mandatory")


class _HpnsaScsiDevEcmaVer_Type(Integer32):
    """Custom type hpnsaScsiDevEcmaVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaScsiDevEcmaVer_Type.__name__ = "Integer32"
_HpnsaScsiDevEcmaVer_Object = MibTableColumn
hpnsaScsiDevEcmaVer = _HpnsaScsiDevEcmaVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 7),
    _HpnsaScsiDevEcmaVer_Type()
)
hpnsaScsiDevEcmaVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevEcmaVer.setStatus("mandatory")


class _HpnsaScsiDevIsoVer_Type(Integer32):
    """Custom type hpnsaScsiDevIsoVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HpnsaScsiDevIsoVer_Type.__name__ = "Integer32"
_HpnsaScsiDevIsoVer_Object = MibTableColumn
hpnsaScsiDevIsoVer = _HpnsaScsiDevIsoVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 8),
    _HpnsaScsiDevIsoVer_Type()
)
hpnsaScsiDevIsoVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevIsoVer.setStatus("mandatory")


class _HpnsaScsiDevVendorId_Type(DisplayString):
    """Custom type hpnsaScsiDevVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaScsiDevVendorId_Type.__name__ = "DisplayString"
_HpnsaScsiDevVendorId_Object = MibTableColumn
hpnsaScsiDevVendorId = _HpnsaScsiDevVendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 9),
    _HpnsaScsiDevVendorId_Type()
)
hpnsaScsiDevVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevVendorId.setStatus("mandatory")


class _HpnsaScsiDevProductId_Type(DisplayString):
    """Custom type hpnsaScsiDevProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpnsaScsiDevProductId_Type.__name__ = "DisplayString"
_HpnsaScsiDevProductId_Object = MibTableColumn
hpnsaScsiDevProductId = _HpnsaScsiDevProductId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 10),
    _HpnsaScsiDevProductId_Type()
)
hpnsaScsiDevProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevProductId.setStatus("mandatory")


class _HpnsaScsiDevProductRev_Type(DisplayString):
    """Custom type hpnsaScsiDevProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HpnsaScsiDevProductRev_Type.__name__ = "DisplayString"
_HpnsaScsiDevProductRev_Object = MibTableColumn
hpnsaScsiDevProductRev = _HpnsaScsiDevProductRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 11),
    _HpnsaScsiDevProductRev_Type()
)
hpnsaScsiDevProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevProductRev.setStatus("mandatory")
_HpnsaScsiDevLogicalBlocks_Type = Integer32
_HpnsaScsiDevLogicalBlocks_Object = MibTableColumn
hpnsaScsiDevLogicalBlocks = _HpnsaScsiDevLogicalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 12),
    _HpnsaScsiDevLogicalBlocks_Type()
)
hpnsaScsiDevLogicalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevLogicalBlocks.setStatus("mandatory")
_HpnsaScsiDevBlockLength_Type = Integer32
_HpnsaScsiDevBlockLength_Object = MibTableColumn
hpnsaScsiDevBlockLength = _HpnsaScsiDevBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 13),
    _HpnsaScsiDevBlockLength_Type()
)
hpnsaScsiDevBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevBlockLength.setStatus("mandatory")


class _HpnsaScsiDevCapacity_Type(Integer32):
    """Custom type hpnsaScsiDevCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaScsiDevCapacity_Type.__name__ = "Integer32"
_HpnsaScsiDevCapacity_Object = MibTableColumn
hpnsaScsiDevCapacity = _HpnsaScsiDevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 14),
    _HpnsaScsiDevCapacity_Type()
)
hpnsaScsiDevCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaScsiDevCapacity.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASCSI-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaScsi": hpnsaScsi,
       "hpnsaScsiMibRev": hpnsaScsiMibRev,
       "hpnsaScsiMibRevMajor": hpnsaScsiMibRevMajor,
       "hpnsaScsiMibRevMinor": hpnsaScsiMibRevMinor,
       "hpnsaScsiAgent": hpnsaScsiAgent,
       "hpnsaScsiAgentModuleTable": hpnsaScsiAgentModuleTable,
       "hpnsaScsiAgentModuleEntry": hpnsaScsiAgentModuleEntry,
       "hpnsaScsiAgentModuleIndex": hpnsaScsiAgentModuleIndex,
       "hpnsaScsiAgentModuleName": hpnsaScsiAgentModuleName,
       "hpnsaScsiAgentModuleVersion": hpnsaScsiAgentModuleVersion,
       "hpnsaScsiAgentModuleDate": hpnsaScsiAgentModuleDate,
       "hpnsaScsiHba": hpnsaScsiHba,
       "hpnsaScsiHbaTable": hpnsaScsiHbaTable,
       "hpnsaScsiHbaEntry": hpnsaScsiHbaEntry,
       "hpnsaScsiHbaIndex": hpnsaScsiHbaIndex,
       "hpnsaScsiHbaTargetId": hpnsaScsiHbaTargetId,
       "hpnsaScsiHbaManagerId": hpnsaScsiHbaManagerId,
       "hpnsaScsiHbaHostAdapterId": hpnsaScsiHbaHostAdapterId,
       "hpnsaScsiDev": hpnsaScsiDev,
       "hpnsaScsiDevTable": hpnsaScsiDevTable,
       "hpnsaScsiDevEntry": hpnsaScsiDevEntry,
       "hpnsaScsiDevHbaIndex": hpnsaScsiDevHbaIndex,
       "hpnsaScsiDevTargIdIndex": hpnsaScsiDevTargIdIndex,
       "hpnsaScsiDevLunIndex": hpnsaScsiDevLunIndex,
       "hpnsaScsiDevType": hpnsaScsiDevType,
       "hpnsaScsiDevRmb": hpnsaScsiDevRmb,
       "hpnsaScsiDevAnsiVer": hpnsaScsiDevAnsiVer,
       "hpnsaScsiDevEcmaVer": hpnsaScsiDevEcmaVer,
       "hpnsaScsiDevIsoVer": hpnsaScsiDevIsoVer,
       "hpnsaScsiDevVendorId": hpnsaScsiDevVendorId,
       "hpnsaScsiDevProductId": hpnsaScsiDevProductId,
       "hpnsaScsiDevProductRev": hpnsaScsiDevProductRev,
       "hpnsaScsiDevLogicalBlocks": hpnsaScsiDevLogicalBlocks,
       "hpnsaScsiDevBlockLength": hpnsaScsiDevBlockLength,
       "hpnsaScsiDevCapacity": hpnsaScsiDevCapacity}
)
