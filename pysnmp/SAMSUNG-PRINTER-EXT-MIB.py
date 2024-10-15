# SNMP MIB module (SAMSUNG-PRINTER-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-PRINTER-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:41 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(PresentOnOff,
 prtChannelEntry,
 prtGeneralEntry,
 prtInputEntry,
 prtInterpreterEntry,
 prtInterpreterIndex,
 prtOutputEntry) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff",
    "prtChannelEntry",
    "prtGeneralEntry",
    "prtInputEntry",
    "prtInterpreterEntry",
    "prtInterpreterIndex",
    "prtOutputEntry")

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

(Cardinal32,
 Ordinal32) = mibBuilder.importSymbols(
    "SAMSUNG-GENERAL-TC",
    "Cardinal32",
    "Ordinal32")

(ScmPrtOutputOffsetStackingType,) = mibBuilder.importSymbols(
    "SAMSUNG-PRINTER-EXT-TC",
    "ScmPrtOutputOffsetStackingType")

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

scmPrintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmPrtBase_ObjectIdentity = ObjectIdentity
scmPrtBase = _ScmPrtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 1)
)
_ScmPrtBaseTable_Object = MibTable
scmPrtBaseTable = _ScmPrtBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 1, 2)
)
if mibBuilder.loadTexts:
    scmPrtBaseTable.setStatus("current")
_ScmPrtBaseEntry_Object = MibTableRow
scmPrtBaseEntry = _ScmPrtBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 1, 2, 1)
)
scmPrtBaseEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtBaseIndex"),
)
if mibBuilder.loadTexts:
    scmPrtBaseEntry.setStatus("current")
_ScmPrtBaseIndex_Type = Ordinal32
_ScmPrtBaseIndex_Object = MibTableColumn
scmPrtBaseIndex = _ScmPrtBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 1, 2, 1, 1),
    _ScmPrtBaseIndex_Type()
)
scmPrtBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scmPrtBaseIndex.setStatus("current")
_ScmPrtBaseRowStatus_Type = RowStatus
_ScmPrtBaseRowStatus_Object = MibTableColumn
scmPrtBaseRowStatus = _ScmPrtBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 1, 2, 1, 2),
    _ScmPrtBaseRowStatus_Type()
)
scmPrtBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtBaseRowStatus.setStatus("current")
_ScmPrtMIBConformance_ObjectIdentity = ObjectIdentity
scmPrtMIBConformance = _ScmPrtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2)
)
_ScmPrtMIBGroups_ObjectIdentity = ObjectIdentity
scmPrtMIBGroups = _ScmPrtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3)
)
_ScmPrtGeneral_ObjectIdentity = ObjectIdentity
scmPrtGeneral = _ScmPrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5)
)
_ScmPrtGeneralSimple_ObjectIdentity = ObjectIdentity
scmPrtGeneralSimple = _ScmPrtGeneralSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1)
)


class _ScmPrtGeneralPrnModelName_Type(DisplayString):
    """Custom type scmPrtGeneralPrnModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnModelName_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnModelName_Object = MibScalar
scmPrtGeneralPrnModelName = _ScmPrtGeneralPrnModelName_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 1),
    _ScmPrtGeneralPrnModelName_Type()
)
scmPrtGeneralPrnModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnModelName.setStatus("current")


class _ScmPrtGeneralPrnOSFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnOSFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnOSFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnOSFWVer_Object = MibScalar
scmPrtGeneralPrnOSFWVer = _ScmPrtGeneralPrnOSFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 2),
    _ScmPrtGeneralPrnOSFWVer_Type()
)
scmPrtGeneralPrnOSFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnOSFWVer.setStatus("current")


class _ScmPrtGeneralPrnModelVer_Type(OctetString):
    """Custom type scmPrtGeneralPrnModelVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnModelVer_Type.__name__ = "OctetString"
_ScmPrtGeneralPrnModelVer_Object = MibScalar
scmPrtGeneralPrnModelVer = _ScmPrtGeneralPrnModelVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 3),
    _ScmPrtGeneralPrnModelVer_Type()
)
scmPrtGeneralPrnModelVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnModelVer.setStatus("current")


class _ScmPrtGeneralPrnSerialNo_Type(DisplayString):
    """Custom type scmPrtGeneralPrnSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnSerialNo_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnSerialNo_Object = MibScalar
scmPrtGeneralPrnSerialNo = _ScmPrtGeneralPrnSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 4),
    _ScmPrtGeneralPrnSerialNo_Type()
)
scmPrtGeneralPrnSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnSerialNo.setStatus("current")


class _ScmPrtGeneralPrnModelDescr_Type(OctetString):
    """Custom type scmPrtGeneralPrnModelDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScmPrtGeneralPrnModelDescr_Type.__name__ = "OctetString"
_ScmPrtGeneralPrnModelDescr_Object = MibScalar
scmPrtGeneralPrnModelDescr = _ScmPrtGeneralPrnModelDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 5),
    _ScmPrtGeneralPrnModelDescr_Type()
)
scmPrtGeneralPrnModelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnModelDescr.setStatus("current")


class _ScmPrtGeneralPrnManufacture_Type(OctetString):
    """Custom type scmPrtGeneralPrnManufacture based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnManufacture_Type.__name__ = "OctetString"
_ScmPrtGeneralPrnManufacture_Object = MibScalar
scmPrtGeneralPrnManufacture = _ScmPrtGeneralPrnManufacture_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 6),
    _ScmPrtGeneralPrnManufacture_Type()
)
scmPrtGeneralPrnManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnManufacture.setStatus("current")


class _ScmPrtGeneralPrnVendor_Type(OctetString):
    """Custom type scmPrtGeneralPrnVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnVendor_Type.__name__ = "OctetString"
_ScmPrtGeneralPrnVendor_Object = MibScalar
scmPrtGeneralPrnVendor = _ScmPrtGeneralPrnVendor_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 7),
    _ScmPrtGeneralPrnVendor_Type()
)
scmPrtGeneralPrnVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnVendor.setStatus("current")


class _ScmPrtGeneralPrnPCLFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnPCLFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnPCLFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnPCLFWVer_Object = MibScalar
scmPrtGeneralPrnPCLFWVer = _ScmPrtGeneralPrnPCLFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 11),
    _ScmPrtGeneralPrnPCLFWVer_Type()
)
scmPrtGeneralPrnPCLFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnPCLFWVer.setStatus("current")


class _ScmPrtGeneralPrnEngFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnEngFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnEngFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnEngFWVer_Object = MibScalar
scmPrtGeneralPrnEngFWVer = _ScmPrtGeneralPrnEngFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 12),
    _ScmPrtGeneralPrnEngFWVer_Type()
)
scmPrtGeneralPrnEngFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnEngFWVer.setStatus("current")


class _ScmPrtGeneralPrnSCFFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnSCFFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnSCFFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnSCFFWVer_Object = MibScalar
scmPrtGeneralPrnSCFFWVer = _ScmPrtGeneralPrnSCFFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 13),
    _ScmPrtGeneralPrnSCFFWVer_Type()
)
scmPrtGeneralPrnSCFFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnSCFFWVer.setStatus("current")


class _ScmPrtGeneralPrnEpsonVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnEpsonVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnEpsonVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnEpsonVer_Object = MibScalar
scmPrtGeneralPrnEpsonVer = _ScmPrtGeneralPrnEpsonVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 14),
    _ScmPrtGeneralPrnEpsonVer_Type()
)
scmPrtGeneralPrnEpsonVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnEpsonVer.setStatus("current")


class _ScmPrtGeneralPrnPCL5eVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnPCL5eVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnPCL5eVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnPCL5eVer_Object = MibScalar
scmPrtGeneralPrnPCL5eVer = _ScmPrtGeneralPrnPCL5eVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 15),
    _ScmPrtGeneralPrnPCL5eVer_Type()
)
scmPrtGeneralPrnPCL5eVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnPCL5eVer.setStatus("current")


class _ScmPrtGeneralPrnPSFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnPSFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnPSFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnPSFWVer_Object = MibScalar
scmPrtGeneralPrnPSFWVer = _ScmPrtGeneralPrnPSFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 16),
    _ScmPrtGeneralPrnPSFWVer_Type()
)
scmPrtGeneralPrnPSFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnPSFWVer.setStatus("current")


class _ScmPrtGeneralPrnScanFWVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnScanFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnScanFWVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnScanFWVer_Object = MibScalar
scmPrtGeneralPrnScanFWVer = _ScmPrtGeneralPrnScanFWVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 17),
    _ScmPrtGeneralPrnScanFWVer_Type()
)
scmPrtGeneralPrnScanFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnScanFWVer.setStatus("current")


class _ScmPrtGeneralPrnKS5843Ver_Type(DisplayString):
    """Custom type scmPrtGeneralPrnKS5843Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnKS5843Ver_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnKS5843Ver_Object = MibScalar
scmPrtGeneralPrnKS5843Ver = _ScmPrtGeneralPrnKS5843Ver_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 18),
    _ScmPrtGeneralPrnKS5843Ver_Type()
)
scmPrtGeneralPrnKS5843Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnKS5843Ver.setStatus("current")


class _ScmPrtGeneralPrnKSSMVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnKSSMVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnKSSMVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnKSSMVer_Object = MibScalar
scmPrtGeneralPrnKSSMVer = _ScmPrtGeneralPrnKSSMVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 19),
    _ScmPrtGeneralPrnKSSMVer_Type()
)
scmPrtGeneralPrnKSSMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnKSSMVer.setStatus("current")


class _ScmPrtGeneralPrnKS5895Ver_Type(DisplayString):
    """Custom type scmPrtGeneralPrnKS5895Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnKS5895Ver_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnKS5895Ver_Object = MibScalar
scmPrtGeneralPrnKS5895Ver = _ScmPrtGeneralPrnKS5895Ver_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 20),
    _ScmPrtGeneralPrnKS5895Ver_Type()
)
scmPrtGeneralPrnKS5895Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnKS5895Ver.setStatus("current")


class _ScmPrtGeneralPrnMainSystemVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnMainSystemVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnMainSystemVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnMainSystemVer_Object = MibScalar
scmPrtGeneralPrnMainSystemVer = _ScmPrtGeneralPrnMainSystemVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 21),
    _ScmPrtGeneralPrnMainSystemVer_Type()
)
scmPrtGeneralPrnMainSystemVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnMainSystemVer.setStatus("current")


class _ScmPrtGeneralPrnSPLVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnSPLVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnSPLVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnSPLVer_Object = MibScalar
scmPrtGeneralPrnSPLVer = _ScmPrtGeneralPrnSPLVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 22),
    _ScmPrtGeneralPrnSPLVer_Type()
)
scmPrtGeneralPrnSPLVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnSPLVer.setStatus("current")


class _ScmPrtGeneralPrncolorPPM_Type(Integer32):
    """Custom type scmPrtGeneralPrncolorPPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScmPrtGeneralPrncolorPPM_Type.__name__ = "Integer32"
_ScmPrtGeneralPrncolorPPM_Object = MibScalar
scmPrtGeneralPrncolorPPM = _ScmPrtGeneralPrncolorPPM_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 23),
    _ScmPrtGeneralPrncolorPPM_Type()
)
scmPrtGeneralPrncolorPPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrncolorPPM.setStatus("current")


class _ScmPrtGeneralPrnPCL5CeVer_Type(DisplayString):
    """Custom type scmPrtGeneralPrnPCL5CeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmPrtGeneralPrnPCL5CeVer_Type.__name__ = "DisplayString"
_ScmPrtGeneralPrnPCL5CeVer_Object = MibScalar
scmPrtGeneralPrnPCL5CeVer = _ScmPrtGeneralPrnPCL5CeVer_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 1, 24),
    _ScmPrtGeneralPrnPCL5CeVer_Type()
)
scmPrtGeneralPrnPCL5CeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtGeneralPrnPCL5CeVer.setStatus("current")
_ScmPrtGeneralTable_Object = MibTable
scmPrtGeneralTable = _ScmPrtGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 2)
)
if mibBuilder.loadTexts:
    scmPrtGeneralTable.setStatus("current")
_ScmPrtGeneralEntry_Object = MibTableRow
scmPrtGeneralEntry = _ScmPrtGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 2, 1)
)
if mibBuilder.loadTexts:
    scmPrtGeneralEntry.setStatus("current")
_ScmPrtGeneralRowStatus_Type = RowStatus
_ScmPrtGeneralRowStatus_Object = MibTableColumn
scmPrtGeneralRowStatus = _ScmPrtGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 5, 2, 1, 1),
    _ScmPrtGeneralRowStatus_Type()
)
scmPrtGeneralRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtGeneralRowStatus.setStatus("current")
_ScmPrtInput_ObjectIdentity = ObjectIdentity
scmPrtInput = _ScmPrtInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8)
)
_ScmPrtInputSimple_ObjectIdentity = ObjectIdentity
scmPrtInputSimple = _ScmPrtInputSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1)
)
_ScmPrtInputTraySwitch_Type = Integer32
_ScmPrtInputTraySwitch_Object = MibScalar
scmPrtInputTraySwitch = _ScmPrtInputTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 1),
    _ScmPrtInputTraySwitch_Type()
)
scmPrtInputTraySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputTraySwitch.setStatus("current")


class _ScmPrtInputTraySwitchOptions_Type(Integer32):
    """Custom type scmPrtInputTraySwitchOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1),
          ("tray1", 4),
          ("tray2", 8))
    )


_ScmPrtInputTraySwitchOptions_Type.__name__ = "Integer32"
_ScmPrtInputTraySwitchOptions_Object = MibScalar
scmPrtInputTraySwitchOptions = _ScmPrtInputTraySwitchOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 2),
    _ScmPrtInputTraySwitchOptions_Type()
)
scmPrtInputTraySwitchOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputTraySwitchOptions.setStatus("current")
_ScmPrtInputLockTray_Type = Integer32
_ScmPrtInputLockTray_Object = MibScalar
scmPrtInputLockTray = _ScmPrtInputLockTray_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 3),
    _ScmPrtInputLockTray_Type()
)
scmPrtInputLockTray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputLockTray.setStatus("current")
_ScmPrtInputLockTrayOptions_Type = Integer32
_ScmPrtInputLockTrayOptions_Object = MibScalar
scmPrtInputLockTrayOptions = _ScmPrtInputLockTrayOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 4),
    _ScmPrtInputLockTrayOptions_Type()
)
scmPrtInputLockTrayOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputLockTrayOptions.setStatus("current")
_ScmPrtInputPaperType_Type = Integer32
_ScmPrtInputPaperType_Object = MibScalar
scmPrtInputPaperType = _ScmPrtInputPaperType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 5),
    _ScmPrtInputPaperType_Type()
)
scmPrtInputPaperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputPaperType.setStatus("current")


class _ScmPrtInputPaperTypeOptions_Type(Integer32):
    """Custom type scmPrtInputPaperTypeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("thick", 2),
          ("transparency", 8),
          ("wet", 4))
    )


_ScmPrtInputPaperTypeOptions_Type.__name__ = "Integer32"
_ScmPrtInputPaperTypeOptions_Object = MibScalar
scmPrtInputPaperTypeOptions = _ScmPrtInputPaperTypeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 1, 6),
    _ScmPrtInputPaperTypeOptions_Type()
)
scmPrtInputPaperTypeOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInputPaperTypeOptions.setStatus("current")
_ScmPrtInputTable_Object = MibTable
scmPrtInputTable = _ScmPrtInputTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2)
)
if mibBuilder.loadTexts:
    scmPrtInputTable.setStatus("current")
_ScmPrtInputEntry_Object = MibTableRow
scmPrtInputEntry = _ScmPrtInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1)
)
if mibBuilder.loadTexts:
    scmPrtInputEntry.setStatus("current")
_ScmPrtInputRowStatus_Type = RowStatus
_ScmPrtInputRowStatus_Object = MibTableColumn
scmPrtInputRowStatus = _ScmPrtInputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 1),
    _ScmPrtInputRowStatus_Type()
)
scmPrtInputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputRowStatus.setStatus("current")


class _ScmPrtInputNextPrtInputIndex_Type(Integer32):
    """Custom type scmPrtInputNextPrtInputIndex based on Integer32"""
    defaultValue = 0


_ScmPrtInputNextPrtInputIndex_Object = MibTableColumn
scmPrtInputNextPrtInputIndex = _ScmPrtInputNextPrtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 2),
    _ScmPrtInputNextPrtInputIndex_Type()
)
scmPrtInputNextPrtInputIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputNextPrtInputIndex.setStatus("current")


class _ScmPrtInputUseCustomSize_Type(PresentOnOff):
    """Custom type scmPrtInputUseCustomSize based on PresentOnOff"""


_ScmPrtInputUseCustomSize_Object = MibTableColumn
scmPrtInputUseCustomSize = _ScmPrtInputUseCustomSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 3),
    _ScmPrtInputUseCustomSize_Type()
)
scmPrtInputUseCustomSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputUseCustomSize.setStatus("current")


class _ScmPrtInputCustDimFeedDirDecl_Type(Integer32):
    """Custom type scmPrtInputCustDimFeedDirDecl based on Integer32"""
    defaultValue = 0


_ScmPrtInputCustDimFeedDirDecl_Object = MibTableColumn
scmPrtInputCustDimFeedDirDecl = _ScmPrtInputCustDimFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 4),
    _ScmPrtInputCustDimFeedDirDecl_Type()
)
scmPrtInputCustDimFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputCustDimFeedDirDecl.setStatus("current")


class _ScmPrtInputCustDimXFeedDirDecl_Type(Integer32):
    """Custom type scmPrtInputCustDimXFeedDirDecl based on Integer32"""
    defaultValue = 0


_ScmPrtInputCustDimXFeedDirDecl_Object = MibTableColumn
scmPrtInputCustDimXFeedDirDecl = _ScmPrtInputCustDimXFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 5),
    _ScmPrtInputCustDimXFeedDirDecl_Type()
)
scmPrtInputCustDimXFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputCustDimXFeedDirDecl.setStatus("current")


class _ScmPrtInputTrayPriority_Type(Integer32):
    """Custom type scmPrtInputTrayPriority based on Integer32"""
    defaultValue = 0


_ScmPrtInputTrayPriority_Object = MibTableColumn
scmPrtInputTrayPriority = _ScmPrtInputTrayPriority_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 6),
    _ScmPrtInputTrayPriority_Type()
)
scmPrtInputTrayPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputTrayPriority.setStatus("current")
_ScmPrtInputPaperSize_Type = Integer32
_ScmPrtInputPaperSize_Object = MibTableColumn
scmPrtInputPaperSize = _ScmPrtInputPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 7),
    _ScmPrtInputPaperSize_Type()
)
scmPrtInputPaperSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputPaperSize.setStatus("current")


class _ScmPrtInputPaperSizeOptions_Type(Integer32):
    """Custom type scmPrtInputPaperSizeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768,
              65536,
              131072,
              262144,
              524288,
              1048576,
              2097152,
              4194304,
              8388608,
              16777216,
              33554432,
              67108864,
              134217728,
              268435456,
              536870912)
        )
    )
    namedValues = NamedValues(
        *(("a3", 131072),
          ("a3Over", 268435456),
          ("a4", 4),
          ("a4P", 8388608),
          ("a5", 8192),
          ("a5P", 33554432),
          ("a6", 32768),
          ("b5Envelope", 536870912),
          ("c5", 512),
          ("c6", 2048),
          ("com10", 64),
          ("custom", 2097152),
          ("dl", 256),
          ("executive", 8),
          ("executiveP", 67108864),
          ("folio", 4096),
          ("isoB5", 32),
          ("jisB4", 262144),
          ("jisB5", 16),
          ("jisB5P", 16777216),
          ("jpost", 524288),
          ("jpostd", 1048576),
          ("ledger", 65536),
          ("legal", 2),
          ("letter", 1),
          ("letterP", 4194304),
          ("monarch", 128),
          ("postA6", 1024),
          ("statement", 16384),
          ("statementP", 134217728))
    )


_ScmPrtInputPaperSizeOptions_Type.__name__ = "Integer32"
_ScmPrtInputPaperSizeOptions_Object = MibTableColumn
scmPrtInputPaperSizeOptions = _ScmPrtInputPaperSizeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 8),
    _ScmPrtInputPaperSizeOptions_Type()
)
scmPrtInputPaperSizeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtInputPaperSizeOptions.setStatus("current")
_ScmPrtInputTrayNum_Type = Integer32
_ScmPrtInputTrayNum_Object = MibTableColumn
scmPrtInputTrayNum = _ScmPrtInputTrayNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 9),
    _ScmPrtInputTrayNum_Type()
)
scmPrtInputTrayNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputTrayNum.setStatus("current")
_ScmPrtInputTrayNumOptions_Type = Integer32
_ScmPrtInputTrayNumOptions_Object = MibTableColumn
scmPrtInputTrayNumOptions = _ScmPrtInputTrayNumOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 8, 2, 1, 10),
    _ScmPrtInputTrayNumOptions_Type()
)
scmPrtInputTrayNumOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInputTrayNumOptions.setStatus("current")
_ScmPrtOutput_ObjectIdentity = ObjectIdentity
scmPrtOutput = _ScmPrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9)
)
_ScmPrtOutputTable_Object = MibTable
scmPrtOutputTable = _ScmPrtOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1)
)
if mibBuilder.loadTexts:
    scmPrtOutputTable.setStatus("current")
_ScmPrtOutputEntry_Object = MibTableRow
scmPrtOutputEntry = _ScmPrtOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1)
)
if mibBuilder.loadTexts:
    scmPrtOutputEntry.setStatus("current")
_ScmPrtOutputRowStatus_Type = RowStatus
_ScmPrtOutputRowStatus_Object = MibTableColumn
scmPrtOutputRowStatus = _ScmPrtOutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 1),
    _ScmPrtOutputRowStatus_Type()
)
scmPrtOutputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputRowStatus.setStatus("current")


class _ScmPrtOutputNextIndex_Type(Integer32):
    """Custom type scmPrtOutputNextIndex based on Integer32"""
    defaultValue = 0


_ScmPrtOutputNextIndex_Object = MibTableColumn
scmPrtOutputNextIndex = _ScmPrtOutputNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 2),
    _ScmPrtOutputNextIndex_Type()
)
scmPrtOutputNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputNextIndex.setStatus("current")


class _ScmPrtOutputPassword_Type(OctetString):
    """Custom type scmPrtOutputPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScmPrtOutputPassword_Type.__name__ = "OctetString"
_ScmPrtOutputPassword_Object = MibTableColumn
scmPrtOutputPassword = _ScmPrtOutputPassword_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 3),
    _ScmPrtOutputPassword_Type()
)
scmPrtOutputPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputPassword.setStatus("current")


class _ScmPrtOutputOffsetStackingType_Type(ScmPrtOutputOffsetStackingType):
    """Custom type scmPrtOutputOffsetStackingType based on ScmPrtOutputOffsetStackingType"""


_ScmPrtOutputOffsetStackingType_Object = MibTableColumn
scmPrtOutputOffsetStackingType = _ScmPrtOutputOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 4),
    _ScmPrtOutputOffsetStackingType_Type()
)
scmPrtOutputOffsetStackingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputOffsetStackingType.setStatus("current")


class _ScmPrtOutputTrayTimeoutSupport_Type(PresentOnOff):
    """Custom type scmPrtOutputTrayTimeoutSupport based on PresentOnOff"""


_ScmPrtOutputTrayTimeoutSupport_Object = MibTableColumn
scmPrtOutputTrayTimeoutSupport = _ScmPrtOutputTrayTimeoutSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 5),
    _ScmPrtOutputTrayTimeoutSupport_Type()
)
scmPrtOutputTrayTimeoutSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputTrayTimeoutSupport.setStatus("current")


class _ScmPrtOutputTrayTimeout_Type(Cardinal32):
    """Custom type scmPrtOutputTrayTimeout based on Cardinal32"""
    defaultValue = 0


_ScmPrtOutputTrayTimeout_Object = MibTableColumn
scmPrtOutputTrayTimeout = _ScmPrtOutputTrayTimeout_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 6),
    _ScmPrtOutputTrayTimeout_Type()
)
scmPrtOutputTrayTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputTrayTimeout.setStatus("current")
if mibBuilder.loadTexts:
    scmPrtOutputTrayTimeout.setUnits("Seconds")
_ScmPrtOutputFinishier_Type = Integer32
_ScmPrtOutputFinishier_Object = MibTableColumn
scmPrtOutputFinishier = _ScmPrtOutputFinishier_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 51),
    _ScmPrtOutputFinishier_Type()
)
scmPrtOutputFinishier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputFinishier.setStatus("current")
_ScmPrtOutputFinishierOptions_Type = Integer32
_ScmPrtOutputFinishierOptions_Object = MibTableColumn
scmPrtOutputFinishierOptions = _ScmPrtOutputFinishierOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 9, 1, 1, 52),
    _ScmPrtOutputFinishierOptions_Type()
)
scmPrtOutputFinishierOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtOutputFinishierOptions.setStatus("current")
_ScmPrtChannel_ObjectIdentity = ObjectIdentity
scmPrtChannel = _ScmPrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14)
)
_ScmPrtChannelSimple_ObjectIdentity = ObjectIdentity
scmPrtChannelSimple = _ScmPrtChannelSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14, 1)
)
_ScmPrtChannelTable_Object = MibTable
scmPrtChannelTable = _ScmPrtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14, 2)
)
if mibBuilder.loadTexts:
    scmPrtChannelTable.setStatus("current")
_ScmPrtChannelEntry_Object = MibTableRow
scmPrtChannelEntry = _ScmPrtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14, 2, 1)
)
if mibBuilder.loadTexts:
    scmPrtChannelEntry.setStatus("current")
_ScmPrtChannelRowStatus_Type = RowStatus
_ScmPrtChannelRowStatus_Object = MibTableColumn
scmPrtChannelRowStatus = _ScmPrtChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14, 2, 1, 1),
    _ScmPrtChannelRowStatus_Type()
)
scmPrtChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtChannelRowStatus.setStatus("current")


class _ScmPrtChannelEOJTimeout_Type(Cardinal32):
    """Custom type scmPrtChannelEOJTimeout based on Cardinal32"""
    defaultValue = 0


_ScmPrtChannelEOJTimeout_Object = MibTableColumn
scmPrtChannelEOJTimeout = _ScmPrtChannelEOJTimeout_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 14, 2, 1, 2),
    _ScmPrtChannelEOJTimeout_Type()
)
scmPrtChannelEOJTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtChannelEOJTimeout.setStatus("current")
if mibBuilder.loadTexts:
    scmPrtChannelEOJTimeout.setUnits("Seconds")
_ScmPrtInterpreter_ObjectIdentity = ObjectIdentity
scmPrtInterpreter = _ScmPrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15)
)
_ScmPrtInterpreterSimple_ObjectIdentity = ObjectIdentity
scmPrtInterpreterSimple = _ScmPrtInterpreterSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 1)
)


class _ScmPrtInterpreterCopyNum_Type(Integer32):
    """Custom type scmPrtInterpreterCopyNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_ScmPrtInterpreterCopyNum_Type.__name__ = "Integer32"
_ScmPrtInterpreterCopyNum_Object = MibScalar
scmPrtInterpreterCopyNum = _ScmPrtInterpreterCopyNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 1, 1),
    _ScmPrtInterpreterCopyNum_Type()
)
scmPrtInterpreterCopyNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInterpreterCopyNum.setStatus("current")
_ScmPrtInterpreterEmulation_Type = Integer32
_ScmPrtInterpreterEmulation_Object = MibScalar
scmPrtInterpreterEmulation = _ScmPrtInterpreterEmulation_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 1, 2),
    _ScmPrtInterpreterEmulation_Type()
)
scmPrtInterpreterEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInterpreterEmulation.setStatus("current")


class _ScmPrtInterpreterEmulationOptions_Type(Integer32):
    """Custom type scmPrtInterpreterEmulationOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("colorGDI", 32768),
          ("epson", 4096),
          ("hexDump", 2048),
          ("hwp", 256),
          ("ksc5843", 32),
          ("ksc5895", 128),
          ("kssm", 64),
          ("pcl4", 4),
          ("pcl5e", 2),
          ("pclxl", 512),
          ("ps2", 1024),
          ("ps3", 16384),
          ("ps3swrender", 8192),
          ("wps3", 8),
          ("wps6", 16))
    )


_ScmPrtInterpreterEmulationOptions_Type.__name__ = "Integer32"
_ScmPrtInterpreterEmulationOptions_Object = MibScalar
scmPrtInterpreterEmulationOptions = _ScmPrtInterpreterEmulationOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 1, 3),
    _ScmPrtInterpreterEmulationOptions_Type()
)
scmPrtInterpreterEmulationOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtInterpreterEmulationOptions.setStatus("current")
_ScmPrtInterpreterTable_Object = MibTable
scmPrtInterpreterTable = _ScmPrtInterpreterTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2)
)
if mibBuilder.loadTexts:
    scmPrtInterpreterTable.setStatus("current")
_ScmPrtInterpreterEntry_Object = MibTableRow
scmPrtInterpreterEntry = _ScmPrtInterpreterEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1)
)
if mibBuilder.loadTexts:
    scmPrtInterpreterEntry.setStatus("current")
_ScmPrtInterpRowStatus_Type = RowStatus
_ScmPrtInterpRowStatus_Object = MibTableColumn
scmPrtInterpRowStatus = _ScmPrtInterpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 1),
    _ScmPrtInterpRowStatus_Type()
)
scmPrtInterpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInterpRowStatus.setStatus("current")
_ScmPrtInterpJobCopiesDefault_Type = Ordinal32
_ScmPrtInterpJobCopiesDefault_Object = MibTableColumn
scmPrtInterpJobCopiesDefault = _ScmPrtInterpJobCopiesDefault_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 9),
    _ScmPrtInterpJobCopiesDefault_Type()
)
scmPrtInterpJobCopiesDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInterpJobCopiesDefault.setStatus("current")


class _ScmPrtInterpLineTerm_Type(PresentOnOff):
    """Custom type scmPrtInterpLineTerm based on PresentOnOff"""


_ScmPrtInterpLineTerm_Object = MibTableColumn
scmPrtInterpLineTerm = _ScmPrtInterpLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 33),
    _ScmPrtInterpLineTerm_Type()
)
scmPrtInterpLineTerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInterpLineTerm.setStatus("current")


class _ScmPrtInterpProcessBarcodes_Type(PresentOnOff):
    """Custom type scmPrtInterpProcessBarcodes based on PresentOnOff"""


_ScmPrtInterpProcessBarcodes_Object = MibTableColumn
scmPrtInterpProcessBarcodes = _ScmPrtInterpProcessBarcodes_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 54),
    _ScmPrtInterpProcessBarcodes_Type()
)
scmPrtInterpProcessBarcodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInterpProcessBarcodes.setStatus("current")
_ScmPrtInterpOrientation_Type = Integer32
_ScmPrtInterpOrientation_Object = MibTableColumn
scmPrtInterpOrientation = _ScmPrtInterpOrientation_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 60),
    _ScmPrtInterpOrientation_Type()
)
scmPrtInterpOrientation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmPrtInterpOrientation.setStatus("current")


class _ScmPrtInterpOrientationOptions_Type(Integer32):
    """Custom type scmPrtInterpOrientationOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 2),
          ("portrait", 1),
          ("reverseLandscape", 4),
          ("reversePortrait", 8))
    )


_ScmPrtInterpOrientationOptions_Type.__name__ = "Integer32"
_ScmPrtInterpOrientationOptions_Object = MibTableColumn
scmPrtInterpOrientationOptions = _ScmPrtInterpOrientationOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 15, 2, 1, 61),
    _ScmPrtInterpOrientationOptions_Type()
)
scmPrtInterpOrientationOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtInterpOrientationOptions.setStatus("current")
_ScmPrtMediaPath_ObjectIdentity = ObjectIdentity
scmPrtMediaPath = _ScmPrtMediaPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 16)
)
_ScmPrtMarker_ObjectIdentity = ObjectIdentity
scmPrtMarker = _ScmPrtMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17)
)
_ScmPrtMarkerSimple_ObjectIdentity = ObjectIdentity
scmPrtMarkerSimple = _ScmPrtMarkerSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1)
)


class _ScmPrtMarkerMarginUnit_Type(Integer32):
    """Custom type scmPrtMarkerMarginUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inch", 2),
          ("mm", 1))
    )


_ScmPrtMarkerMarginUnit_Type.__name__ = "Integer32"
_ScmPrtMarkerMarginUnit_Object = MibScalar
scmPrtMarkerMarginUnit = _ScmPrtMarkerMarginUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 1),
    _ScmPrtMarkerMarginUnit_Type()
)
scmPrtMarkerMarginUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerMarginUnit.setStatus("current")
_ScmPrtMarkerSrt_Type = Integer32
_ScmPrtMarkerSrt_Object = MibScalar
scmPrtMarkerSrt = _ScmPrtMarkerSrt_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 2),
    _ScmPrtMarkerSrt_Type()
)
scmPrtMarkerSrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtMarkerSrt.setStatus("current")


class _ScmPrtMarkerSrtOptions_Type(Integer32):
    """Custom type scmPrtMarkerSrtOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("enhance", 1),
          ("gray", 8),
          ("grayPlus", 4),
          ("normal", 2),
          ("res1200fast", 16),
          ("res1200true", 32))
    )


_ScmPrtMarkerSrtOptions_Type.__name__ = "Integer32"
_ScmPrtMarkerSrtOptions_Object = MibScalar
scmPrtMarkerSrtOptions = _ScmPrtMarkerSrtOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 3),
    _ScmPrtMarkerSrtOptions_Type()
)
scmPrtMarkerSrtOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerSrtOptions.setStatus("current")
_ScmPrtMarkerDensity_Type = Integer32
_ScmPrtMarkerDensity_Object = MibScalar
scmPrtMarkerDensity = _ScmPrtMarkerDensity_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 4),
    _ScmPrtMarkerDensity_Type()
)
scmPrtMarkerDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerDensity.setStatus("current")


class _ScmPrtMarkerDensityOptions_Type(Integer32):
    """Custom type scmPrtMarkerDensityOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dark", 4),
          ("light", 1),
          ("medium", 2))
    )


_ScmPrtMarkerDensityOptions_Type.__name__ = "Integer32"
_ScmPrtMarkerDensityOptions_Object = MibScalar
scmPrtMarkerDensityOptions = _ScmPrtMarkerDensityOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 5),
    _ScmPrtMarkerDensityOptions_Type()
)
scmPrtMarkerDensityOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerDensityOptions.setStatus("current")
_ScmPrtMarkerSmetMode_Type = Integer32
_ScmPrtMarkerSmetMode_Object = MibScalar
scmPrtMarkerSmetMode = _ScmPrtMarkerSmetMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 6),
    _ScmPrtMarkerSmetMode_Type()
)
scmPrtMarkerSmetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerSmetMode.setStatus("current")


class _ScmPrtMarkerSmetModeOptions_Type(Integer32):
    """Custom type scmPrtMarkerSmetModeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtMarkerSmetModeOptions_Type.__name__ = "Integer32"
_ScmPrtMarkerSmetModeOptions_Object = MibScalar
scmPrtMarkerSmetModeOptions = _ScmPrtMarkerSmetModeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 7),
    _ScmPrtMarkerSmetModeOptions_Type()
)
scmPrtMarkerSmetModeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerSmetModeOptions.setStatus("current")


class _ScmPrtMarkerduplexTopMargin_Type(Integer32):
    """Custom type scmPrtMarkerduplexTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ScmPrtMarkerduplexTopMargin_Type.__name__ = "Integer32"
_ScmPrtMarkerduplexTopMargin_Object = MibScalar
scmPrtMarkerduplexTopMargin = _ScmPrtMarkerduplexTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 8),
    _ScmPrtMarkerduplexTopMargin_Type()
)
scmPrtMarkerduplexTopMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerduplexTopMargin.setStatus("current")


class _ScmPrtMarkerduplexLeftMargin_Type(Integer32):
    """Custom type scmPrtMarkerduplexLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ScmPrtMarkerduplexLeftMargin_Type.__name__ = "Integer32"
_ScmPrtMarkerduplexLeftMargin_Object = MibScalar
scmPrtMarkerduplexLeftMargin = _ScmPrtMarkerduplexLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 9),
    _ScmPrtMarkerduplexLeftMargin_Type()
)
scmPrtMarkerduplexLeftMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerduplexLeftMargin.setStatus("current")


class _ScmPrtMarkerShortEdgeBindingMargin_Type(Integer32):
    """Custom type scmPrtMarkerShortEdgeBindingMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ScmPrtMarkerShortEdgeBindingMargin_Type.__name__ = "Integer32"
_ScmPrtMarkerShortEdgeBindingMargin_Object = MibScalar
scmPrtMarkerShortEdgeBindingMargin = _ScmPrtMarkerShortEdgeBindingMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 10),
    _ScmPrtMarkerShortEdgeBindingMargin_Type()
)
scmPrtMarkerShortEdgeBindingMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerShortEdgeBindingMargin.setStatus("current")


class _ScmPrtMarkerLongEdgeBindingMargin_Type(Integer32):
    """Custom type scmPrtMarkerLongEdgeBindingMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ScmPrtMarkerLongEdgeBindingMargin_Type.__name__ = "Integer32"
_ScmPrtMarkerLongEdgeBindingMargin_Object = MibScalar
scmPrtMarkerLongEdgeBindingMargin = _ScmPrtMarkerLongEdgeBindingMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 11),
    _ScmPrtMarkerLongEdgeBindingMargin_Type()
)
scmPrtMarkerLongEdgeBindingMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerLongEdgeBindingMargin.setStatus("current")
_ScmPrtMarkerTonerSave_Type = Integer32
_ScmPrtMarkerTonerSave_Object = MibScalar
scmPrtMarkerTonerSave = _ScmPrtMarkerTonerSave_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 12),
    _ScmPrtMarkerTonerSave_Type()
)
scmPrtMarkerTonerSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerSave.setStatus("current")
_ScmPrtMarkerTonerSaveOptions_Type = Integer32
_ScmPrtMarkerTonerSaveOptions_Object = MibScalar
scmPrtMarkerTonerSaveOptions = _ScmPrtMarkerTonerSaveOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 13),
    _ScmPrtMarkerTonerSaveOptions_Type()
)
scmPrtMarkerTonerSaveOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerSaveOptions.setStatus("current")
_ScmPrtMarkerTonerOutAction_Type = Integer32
_ScmPrtMarkerTonerOutAction_Object = MibScalar
scmPrtMarkerTonerOutAction = _ScmPrtMarkerTonerOutAction_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 14),
    _ScmPrtMarkerTonerOutAction_Type()
)
scmPrtMarkerTonerOutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerOutAction.setStatus("current")


class _ScmPrtMarkerTonerOutActionOptions_Type(Integer32):
    """Custom type scmPrtMarkerTonerOutActionOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("stop", 2))
    )


_ScmPrtMarkerTonerOutActionOptions_Type.__name__ = "Integer32"
_ScmPrtMarkerTonerOutActionOptions_Object = MibScalar
scmPrtMarkerTonerOutActionOptions = _ScmPrtMarkerTonerOutActionOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 1, 15),
    _ScmPrtMarkerTonerOutActionOptions_Type()
)
scmPrtMarkerTonerOutActionOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerOutActionOptions.setStatus("current")
_ScmPrtMarkerTable_Object = MibTable
scmPrtMarkerTable = _ScmPrtMarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2)
)
if mibBuilder.loadTexts:
    scmPrtMarkerTable.setStatus("current")
_ScmPrtMarkerEntry_Object = MibTableRow
scmPrtMarkerEntry = _ScmPrtMarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1)
)
scmPrtMarkerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerIndex"),
)
if mibBuilder.loadTexts:
    scmPrtMarkerEntry.setStatus("current")
_ScmPrtMarkerTonerIndex_Type = Ordinal32
_ScmPrtMarkerTonerIndex_Object = MibTableColumn
scmPrtMarkerTonerIndex = _ScmPrtMarkerTonerIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 1),
    _ScmPrtMarkerTonerIndex_Type()
)
scmPrtMarkerTonerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerIndex.setStatus("current")
_ScmPrtMarkerResolution_Type = Integer32
_ScmPrtMarkerResolution_Object = MibTableColumn
scmPrtMarkerResolution = _ScmPrtMarkerResolution_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 2),
    _ScmPrtMarkerResolution_Type()
)
scmPrtMarkerResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtMarkerResolution.setStatus("current")


class _ScmPrtMarkerResolutionOptions_Type(Integer32):
    """Custom type scmPrtMarkerResolutionOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("res1200", 4),
          ("res1200best", 16),
          ("res1200fast", 8),
          ("res300", 1),
          ("res600", 2))
    )


_ScmPrtMarkerResolutionOptions_Type.__name__ = "Integer32"
_ScmPrtMarkerResolutionOptions_Object = MibTableColumn
scmPrtMarkerResolutionOptions = _ScmPrtMarkerResolutionOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 3),
    _ScmPrtMarkerResolutionOptions_Type()
)
scmPrtMarkerResolutionOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerResolutionOptions.setStatus("current")
_ScmPrtMarkerTonerColor_Type = Integer32
_ScmPrtMarkerTonerColor_Object = MibTableColumn
scmPrtMarkerTonerColor = _ScmPrtMarkerTonerColor_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 4),
    _ScmPrtMarkerTonerColor_Type()
)
scmPrtMarkerTonerColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerColor.setStatus("current")
_ScmPrtMarkerTonerColorDescription_Type = OctetString
_ScmPrtMarkerTonerColorDescription_Object = MibTableColumn
scmPrtMarkerTonerColorDescription = _ScmPrtMarkerTonerColorDescription_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 5),
    _ScmPrtMarkerTonerColorDescription_Type()
)
scmPrtMarkerTonerColorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerColorDescription.setStatus("current")
_ScmPrtMarkerTonerLevel_Type = Integer32
_ScmPrtMarkerTonerLevel_Object = MibTableColumn
scmPrtMarkerTonerLevel = _ScmPrtMarkerTonerLevel_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 17, 2, 1, 6),
    _ScmPrtMarkerTonerLevel_Type()
)
scmPrtMarkerTonerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtMarkerTonerLevel.setStatus("current")
_ScmPrtOperation_ObjectIdentity = ObjectIdentity
scmPrtOperation = _ScmPrtOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18)
)
_ScmPrtOperationSimple_ObjectIdentity = ObjectIdentity
scmPrtOperationSimple = _ScmPrtOperationSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1)
)


class _ScmPrtOperationJobCancel_Type(Integer32):
    """Custom type scmPrtOperationJobCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancelJob", 1)
    )


_ScmPrtOperationJobCancel_Type.__name__ = "Integer32"
_ScmPrtOperationJobCancel_Object = MibScalar
scmPrtOperationJobCancel = _ScmPrtOperationJobCancel_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 1),
    _ScmPrtOperationJobCancel_Type()
)
scmPrtOperationJobCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationJobCancel.setStatus("current")


class _ScmPrtOperarionMenuClear_Type(Integer32):
    """Custom type scmPrtOperarionMenuClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmPrtOperarionMenuClear_Type.__name__ = "Integer32"
_ScmPrtOperarionMenuClear_Object = MibScalar
scmPrtOperarionMenuClear = _ScmPrtOperarionMenuClear_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 2),
    _ScmPrtOperarionMenuClear_Type()
)
scmPrtOperarionMenuClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperarionMenuClear.setStatus("current")


class _ScmPrtOperationMenuClearOptions_Type(Integer32):
    """Custom type scmPrtOperationMenuClearOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ScmPrtOperationMenuClearOptions_Type.__name__ = "Integer32"
_ScmPrtOperationMenuClearOptions_Object = MibScalar
scmPrtOperationMenuClearOptions = _ScmPrtOperationMenuClearOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 3),
    _ScmPrtOperationMenuClearOptions_Type()
)
scmPrtOperationMenuClearOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtOperationMenuClearOptions.setStatus("current")


class _ScmPrtOperationFuserClean_Type(Integer32):
    """Custom type scmPrtOperationFuserClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtOperationFuserClean_Type.__name__ = "Integer32"
_ScmPrtOperationFuserClean_Object = MibScalar
scmPrtOperationFuserClean = _ScmPrtOperationFuserClean_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 4),
    _ScmPrtOperationFuserClean_Type()
)
scmPrtOperationFuserClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationFuserClean.setStatus("current")


class _ScmPrtOperationFuserCleanOptions_Type(Integer32):
    """Custom type scmPrtOperationFuserCleanOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ScmPrtOperationFuserCleanOptions_Type.__name__ = "Integer32"
_ScmPrtOperationFuserCleanOptions_Object = MibScalar
scmPrtOperationFuserCleanOptions = _ScmPrtOperationFuserCleanOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 5),
    _ScmPrtOperationFuserCleanOptions_Type()
)
scmPrtOperationFuserCleanOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtOperationFuserCleanOptions.setStatus("current")


class _ScmPrtOperationOpcClean_Type(Integer32):
    """Custom type scmPrtOperationOpcClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtOperationOpcClean_Type.__name__ = "Integer32"
_ScmPrtOperationOpcClean_Object = MibScalar
scmPrtOperationOpcClean = _ScmPrtOperationOpcClean_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 6),
    _ScmPrtOperationOpcClean_Type()
)
scmPrtOperationOpcClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationOpcClean.setStatus("current")


class _ScmPrtOperationOpcCleanOptions_Type(Integer32):
    """Custom type scmPrtOperationOpcCleanOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ScmPrtOperationOpcCleanOptions_Type.__name__ = "Integer32"
_ScmPrtOperationOpcCleanOptions_Object = MibScalar
scmPrtOperationOpcCleanOptions = _ScmPrtOperationOpcCleanOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 7),
    _ScmPrtOperationOpcCleanOptions_Type()
)
scmPrtOperationOpcCleanOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtOperationOpcCleanOptions.setStatus("current")
_ScmPrtOperationTestPrtRequest_Type = Integer32
_ScmPrtOperationTestPrtRequest_Object = MibScalar
scmPrtOperationTestPrtRequest = _ScmPrtOperationTestPrtRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 8),
    _ScmPrtOperationTestPrtRequest_Type()
)
scmPrtOperationTestPrtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationTestPrtRequest.setStatus("current")


class _ScmPrtOperationPrintFontRequest_Type(Integer32):
    """Custom type scmPrtOperationPrintFontRequest based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("configpage", 9),
          ("demopage", 10),
          ("epson", 6),
          ("fuserClean", 8),
          ("ks5843", 3),
          ("ks5895", 5),
          ("kssm", 4),
          ("menuMap", 11),
          ("opcClean", 7),
          ("pcl", 1),
          ("ps", 2),
          ("psFlashDirectory", 12))
    )


_ScmPrtOperationPrintFontRequest_Type.__name__ = "Integer32"
_ScmPrtOperationPrintFontRequest_Object = MibScalar
scmPrtOperationPrintFontRequest = _ScmPrtOperationPrintFontRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 9),
    _ScmPrtOperationPrintFontRequest_Type()
)
scmPrtOperationPrintFontRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationPrintFontRequest.setStatus("current")


class _ScmPrtOperationPrintBlackOnly_Type(Integer32):
    """Custom type scmPrtOperationPrintBlackOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmPrtOperationPrintBlackOnly_Type.__name__ = "Integer32"
_ScmPrtOperationPrintBlackOnly_Object = MibScalar
scmPrtOperationPrintBlackOnly = _ScmPrtOperationPrintBlackOnly_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 1, 10),
    _ScmPrtOperationPrintBlackOnly_Type()
)
scmPrtOperationPrintBlackOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtOperationPrintBlackOnly.setStatus("current")
_ScmPrtOperationTable_Object = MibTable
scmPrtOperationTable = _ScmPrtOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 2)
)
if mibBuilder.loadTexts:
    scmPrtOperationTable.setStatus("current")
_ScmPrtOperationEntry_Object = MibTableRow
scmPrtOperationEntry = _ScmPrtOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 2, 1)
)
scmPrtOperationEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationIndex"),
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    scmPrtOperationEntry.setStatus("current")
_ScmPrtOperationIndex_Type = Ordinal32
_ScmPrtOperationIndex_Object = MibTableColumn
scmPrtOperationIndex = _ScmPrtOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 18, 2, 1, 1),
    _ScmPrtOperationIndex_Type()
)
scmPrtOperationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtOperationIndex.setStatus("current")
_ScmPrtConfiguration_ObjectIdentity = ObjectIdentity
scmPrtConfiguration = _ScmPrtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19)
)
_ScmPrtConfigurationSimple_ObjectIdentity = ObjectIdentity
scmPrtConfigurationSimple = _ScmPrtConfigurationSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1)
)
_ScmPrtConfigurationPowerSave_Type = Integer32
_ScmPrtConfigurationPowerSave_Object = MibScalar
scmPrtConfigurationPowerSave = _ScmPrtConfigurationPowerSave_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 1),
    _ScmPrtConfigurationPowerSave_Type()
)
scmPrtConfigurationPowerSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConfigurationPowerSave.setStatus("current")


class _ScmPrtConfigurationPowerSaveOptions_Type(Integer32):
    """Custom type scmPrtConfigurationPowerSaveOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("pwSave15", 2),
          ("pwSave30", 4),
          ("pwSave45", 8),
          ("pwSave60", 16),
          ("pwSaveoff", 1))
    )


_ScmPrtConfigurationPowerSaveOptions_Type.__name__ = "Integer32"
_ScmPrtConfigurationPowerSaveOptions_Object = MibScalar
scmPrtConfigurationPowerSaveOptions = _ScmPrtConfigurationPowerSaveOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 2),
    _ScmPrtConfigurationPowerSaveOptions_Type()
)
scmPrtConfigurationPowerSaveOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtConfigurationPowerSaveOptions.setStatus("current")
_ScmPrtConfigurationAutocont_Type = Integer32
_ScmPrtConfigurationAutocont_Object = MibScalar
scmPrtConfigurationAutocont = _ScmPrtConfigurationAutocont_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 3),
    _ScmPrtConfigurationAutocont_Type()
)
scmPrtConfigurationAutocont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConfigurationAutocont.setStatus("current")


class _ScmPrtConfigurationAutoCountOptions_Type(Integer32):
    """Custom type scmPrtConfigurationAutoCountOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtConfigurationAutoCountOptions_Type.__name__ = "Integer32"
_ScmPrtConfigurationAutoCountOptions_Object = MibScalar
scmPrtConfigurationAutoCountOptions = _ScmPrtConfigurationAutoCountOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 4),
    _ScmPrtConfigurationAutoCountOptions_Type()
)
scmPrtConfigurationAutoCountOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtConfigurationAutoCountOptions.setStatus("current")
_ScmPrtConfigurationJam2Recover_Type = Integer32
_ScmPrtConfigurationJam2Recover_Object = MibScalar
scmPrtConfigurationJam2Recover = _ScmPrtConfigurationJam2Recover_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 5),
    _ScmPrtConfigurationJam2Recover_Type()
)
scmPrtConfigurationJam2Recover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConfigurationJam2Recover.setStatus("current")


class _ScmPrtConfigurationJam2RecOptions_Type(Integer32):
    """Custom type scmPrtConfigurationJam2RecOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtConfigurationJam2RecOptions_Type.__name__ = "Integer32"
_ScmPrtConfigurationJam2RecOptions_Object = MibScalar
scmPrtConfigurationJam2RecOptions = _ScmPrtConfigurationJam2RecOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 6),
    _ScmPrtConfigurationJam2RecOptions_Type()
)
scmPrtConfigurationJam2RecOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtConfigurationJam2RecOptions.setStatus("current")
_ScmPrtConfigurationAltitudeAction_Type = Integer32
_ScmPrtConfigurationAltitudeAction_Object = MibScalar
scmPrtConfigurationAltitudeAction = _ScmPrtConfigurationAltitudeAction_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 7),
    _ScmPrtConfigurationAltitudeAction_Type()
)
scmPrtConfigurationAltitudeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConfigurationAltitudeAction.setStatus("current")


class _ScmPrtConfigurationAltitudeActionOptions_Type(Integer32):
    """Custom type scmPrtConfigurationAltitudeActionOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_ScmPrtConfigurationAltitudeActionOptions_Type.__name__ = "Integer32"
_ScmPrtConfigurationAltitudeActionOptions_Object = MibScalar
scmPrtConfigurationAltitudeActionOptions = _ScmPrtConfigurationAltitudeActionOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 1, 8),
    _ScmPrtConfigurationAltitudeActionOptions_Type()
)
scmPrtConfigurationAltitudeActionOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtConfigurationAltitudeActionOptions.setStatus("current")
_ScmPrtConfigurationTable_Object = MibTable
scmPrtConfigurationTable = _ScmPrtConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 2)
)
if mibBuilder.loadTexts:
    scmPrtConfigurationTable.setStatus("current")
_ScmPrtConfigurationEntry_Object = MibTableRow
scmPrtConfigurationEntry = _ScmPrtConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 2, 1)
)
scmPrtConfigurationEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationIndex"),
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    scmPrtConfigurationEntry.setStatus("current")
_ScmPrtConfigurationIndex_Type = Ordinal32
_ScmPrtConfigurationIndex_Object = MibTableColumn
scmPrtConfigurationIndex = _ScmPrtConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 19, 2, 1, 1),
    _ScmPrtConfigurationIndex_Type()
)
scmPrtConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtConfigurationIndex.setStatus("current")
_ScmPrtCount_ObjectIdentity = ObjectIdentity
scmPrtCount = _ScmPrtCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20)
)
_ScmPrtCountSimple_ObjectIdentity = ObjectIdentity
scmPrtCountSimple = _ScmPrtCountSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1)
)
_ScmPrtCountDrumImageCount_Type = Integer32
_ScmPrtCountDrumImageCount_Object = MibScalar
scmPrtCountDrumImageCount = _ScmPrtCountDrumImageCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 1),
    _ScmPrtCountDrumImageCount_Type()
)
scmPrtCountDrumImageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountDrumImageCount.setStatus("current")


class _ScmPrtCountDrumImageCountReset_Type(Integer32):
    """Custom type scmPrtCountDrumImageCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtCountDrumImageCountReset_Type.__name__ = "Integer32"
_ScmPrtCountDrumImageCountReset_Object = MibScalar
scmPrtCountDrumImageCountReset = _ScmPrtCountDrumImageCountReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 2),
    _ScmPrtCountDrumImageCountReset_Type()
)
scmPrtCountDrumImageCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountDrumImageCountReset.setStatus("current")
_ScmPrtCountTransferImageCount_Type = Integer32
_ScmPrtCountTransferImageCount_Object = MibScalar
scmPrtCountTransferImageCount = _ScmPrtCountTransferImageCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 3),
    _ScmPrtCountTransferImageCount_Type()
)
scmPrtCountTransferImageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountTransferImageCount.setStatus("current")


class _ScmPrtCountTransferImageCountReset_Type(Integer32):
    """Custom type scmPrtCountTransferImageCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtCountTransferImageCountReset_Type.__name__ = "Integer32"
_ScmPrtCountTransferImageCountReset_Object = MibScalar
scmPrtCountTransferImageCountReset = _ScmPrtCountTransferImageCountReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 4),
    _ScmPrtCountTransferImageCountReset_Type()
)
scmPrtCountTransferImageCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountTransferImageCountReset.setStatus("current")
_ScmPrtCountFuserImageCount_Type = Integer32
_ScmPrtCountFuserImageCount_Object = MibScalar
scmPrtCountFuserImageCount = _ScmPrtCountFuserImageCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 5),
    _ScmPrtCountFuserImageCount_Type()
)
scmPrtCountFuserImageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountFuserImageCount.setStatus("current")


class _ScmPrtCountFuserImageCountReset_Type(Integer32):
    """Custom type scmPrtCountFuserImageCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtCountFuserImageCountReset_Type.__name__ = "Integer32"
_ScmPrtCountFuserImageCountReset_Object = MibScalar
scmPrtCountFuserImageCountReset = _ScmPrtCountFuserImageCountReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 6),
    _ScmPrtCountFuserImageCountReset_Type()
)
scmPrtCountFuserImageCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountFuserImageCountReset.setStatus("current")
_ScmPrtCountTwoRollerCount_Type = Integer32
_ScmPrtCountTwoRollerCount_Object = MibScalar
scmPrtCountTwoRollerCount = _ScmPrtCountTwoRollerCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 7),
    _ScmPrtCountTwoRollerCount_Type()
)
scmPrtCountTwoRollerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountTwoRollerCount.setStatus("current")


class _ScmPrtCountTwoRollerReset_Type(Integer32):
    """Custom type scmPrtCountTwoRollerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_ScmPrtCountTwoRollerReset_Type.__name__ = "Integer32"
_ScmPrtCountTwoRollerReset_Object = MibScalar
scmPrtCountTwoRollerReset = _ScmPrtCountTwoRollerReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 8),
    _ScmPrtCountTwoRollerReset_Type()
)
scmPrtCountTwoRollerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountTwoRollerReset.setStatus("current")
_ScmPrtCountPickupMPCount_Type = Integer32
_ScmPrtCountPickupMPCount_Object = MibScalar
scmPrtCountPickupMPCount = _ScmPrtCountPickupMPCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 9),
    _ScmPrtCountPickupMPCount_Type()
)
scmPrtCountPickupMPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountPickupMPCount.setStatus("current")


class _ScmPrtCountPickupMPReset_Type(Integer32):
    """Custom type scmPrtCountPickupMPReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_ScmPrtCountPickupMPReset_Type.__name__ = "Integer32"
_ScmPrtCountPickupMPReset_Object = MibScalar
scmPrtCountPickupMPReset = _ScmPrtCountPickupMPReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 10),
    _ScmPrtCountPickupMPReset_Type()
)
scmPrtCountPickupMPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountPickupMPReset.setStatus("current")
_ScmPrtCountPickupTray1Count_Type = Integer32
_ScmPrtCountPickupTray1Count_Object = MibScalar
scmPrtCountPickupTray1Count = _ScmPrtCountPickupTray1Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 11),
    _ScmPrtCountPickupTray1Count_Type()
)
scmPrtCountPickupTray1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountPickupTray1Count.setStatus("current")


class _ScmPrtCountPickupTray1Reset_Type(Integer32):
    """Custom type scmPrtCountPickupTray1Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_ScmPrtCountPickupTray1Reset_Type.__name__ = "Integer32"
_ScmPrtCountPickupTray1Reset_Object = MibScalar
scmPrtCountPickupTray1Reset = _ScmPrtCountPickupTray1Reset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 12),
    _ScmPrtCountPickupTray1Reset_Type()
)
scmPrtCountPickupTray1Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountPickupTray1Reset.setStatus("current")
_ScmPrtCountPickupTray2Count_Type = Integer32
_ScmPrtCountPickupTray2Count_Object = MibScalar
scmPrtCountPickupTray2Count = _ScmPrtCountPickupTray2Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 13),
    _ScmPrtCountPickupTray2Count_Type()
)
scmPrtCountPickupTray2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountPickupTray2Count.setStatus("current")


class _ScmPrtCountPickupTray2Reset_Type(Integer32):
    """Custom type scmPrtCountPickupTray2Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_ScmPrtCountPickupTray2Reset_Type.__name__ = "Integer32"
_ScmPrtCountPickupTray2Reset_Object = MibScalar
scmPrtCountPickupTray2Reset = _ScmPrtCountPickupTray2Reset_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 1, 14),
    _ScmPrtCountPickupTray2Reset_Type()
)
scmPrtCountPickupTray2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountPickupTray2Reset.setStatus("current")
_ScmPrtCountTable_Object = MibTable
scmPrtCountTable = _ScmPrtCountTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2)
)
if mibBuilder.loadTexts:
    scmPrtCountTable.setStatus("current")
_ScmPrtCountEntry_Object = MibTableRow
scmPrtCountEntry = _ScmPrtCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1)
)
scmPrtCountEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountIndex"),
)
if mibBuilder.loadTexts:
    scmPrtCountEntry.setStatus("current")


class _ScmPrtCountIndex_Type(Integer32):
    """Custom type scmPrtCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmPrtCountIndex_Type.__name__ = "Integer32"
_ScmPrtCountIndex_Object = MibTableColumn
scmPrtCountIndex = _ScmPrtCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 1),
    _ScmPrtCountIndex_Type()
)
scmPrtCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountIndex.setStatus("current")


class _ScmPrtCountDeviceType_Type(Integer32):
    """Custom type scmPrtCountDeviceType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("basicFunctionFinisher", 10),
          ("copier", 3),
          ("externalIFFinisher", 12),
          ("fax", 4),
          ("feeder", 7),
          ("finisher", 6),
          ("mailbox", 5),
          ("marker", 9),
          ("multiFunctionFinisher", 11),
          ("payment", 14),
          ("printer", 1),
          ("scanner", 2),
          ("sorter", 8),
          ("thirdPartyFinisher", 13))
    )


_ScmPrtCountDeviceType_Type.__name__ = "Integer32"
_ScmPrtCountDeviceType_Object = MibTableColumn
scmPrtCountDeviceType = _ScmPrtCountDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 2),
    _ScmPrtCountDeviceType_Type()
)
scmPrtCountDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountDeviceType.setStatus("current")


class _ScmPrtCountType_Type(Integer32):
    """Custom type scmPrtCountType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("copy", 3),
          ("digitalReceive", 7),
          ("digitalSend", 6),
          ("faxIn", 4),
          ("faxout", 5),
          ("other", 1),
          ("print", 9),
          ("scan", 8),
          ("unknown", 2))
    )


_ScmPrtCountType_Type.__name__ = "Integer32"
_ScmPrtCountType_Object = MibTableColumn
scmPrtCountType = _ScmPrtCountType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 3),
    _ScmPrtCountType_Type()
)
scmPrtCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountType.setStatus("current")


class _ScmPrtCountMediaSize_Type(Integer32):
    """Custom type scmPrtCountMediaSize based on Integer32"""
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
        *(("a3", 19),
          ("a3Over", 30),
          ("a4", 4),
          ("a4P", 25),
          ("a5", 15),
          ("a5P", 27),
          ("a6", 17),
          ("b5Envelope", 31),
          ("c5", 11),
          ("c6", 13),
          ("com10", 8),
          ("custom", 23),
          ("dl", 10),
          ("executive", 5),
          ("executiveP", 28),
          ("folio", 14),
          ("isoB5", 7),
          ("jisB4", 20),
          ("jisB5", 6),
          ("jisB5P", 26),
          ("jpost", 21),
          ("jpostd", 22),
          ("ledger", 18),
          ("legal", 3),
          ("letter", 2),
          ("letterP", 24),
          ("monarch", 9),
          ("postA6", 12),
          ("statement", 16),
          ("statementP", 29),
          ("unknown", 1))
    )


_ScmPrtCountMediaSize_Type.__name__ = "Integer32"
_ScmPrtCountMediaSize_Object = MibTableColumn
scmPrtCountMediaSize = _ScmPrtCountMediaSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 4),
    _ScmPrtCountMediaSize_Type()
)
scmPrtCountMediaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountMediaSize.setStatus("current")


class _ScmPrtCountColorant_Type(Integer32):
    """Custom type scmPrtCountColorant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color", 2),
          ("mono", 1))
    )


_ScmPrtCountColorant_Type.__name__ = "Integer32"
_ScmPrtCountColorant_Object = MibTableColumn
scmPrtCountColorant = _ScmPrtCountColorant_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 5),
    _ScmPrtCountColorant_Type()
)
scmPrtCountColorant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountColorant.setStatus("current")


class _ScmPrtCountDuplex_Type(Integer32):
    """Custom type scmPrtCountDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 2),
          ("simplex", 1))
    )


_ScmPrtCountDuplex_Type.__name__ = "Integer32"
_ScmPrtCountDuplex_Object = MibTableColumn
scmPrtCountDuplex = _ScmPrtCountDuplex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 6),
    _ScmPrtCountDuplex_Type()
)
scmPrtCountDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountDuplex.setStatus("current")


class _ScmPrtCountResolution_Type(Integer32):
    """Custom type scmPrtCountResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high1200dpi", 3),
          ("low300dpi", 1),
          ("normal600dpi", 2))
    )


_ScmPrtCountResolution_Type.__name__ = "Integer32"
_ScmPrtCountResolution_Object = MibTableColumn
scmPrtCountResolution = _ScmPrtCountResolution_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 7),
    _ScmPrtCountResolution_Type()
)
scmPrtCountResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtCountResolution.setStatus("current")


class _ScmPrtCountUnit_Type(Integer32):
    """Custom type scmPrtCountUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              11,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("characters", 5),
          ("dotRow", 9),
          ("feet", 16),
          ("hours", 11),
          ("impressions", 7),
          ("lines", 6),
          ("meters", 17),
          ("micrometers", 4),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3))
    )


_ScmPrtCountUnit_Type.__name__ = "Integer32"
_ScmPrtCountUnit_Object = MibTableColumn
scmPrtCountUnit = _ScmPrtCountUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 8),
    _ScmPrtCountUnit_Type()
)
scmPrtCountUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountUnit.setStatus("current")
_ScmPrtCountValue_Type = Integer32
_ScmPrtCountValue_Object = MibTableColumn
scmPrtCountValue = _ScmPrtCountValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 20, 2, 1, 9),
    _ScmPrtCountValue_Type()
)
scmPrtCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtCountValue.setStatus("current")
_ScmPrtSerial_ObjectIdentity = ObjectIdentity
scmPrtSerial = _ScmPrtSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21)
)
_ScmPrtSerialSimple_ObjectIdentity = ObjectIdentity
scmPrtSerialSimple = _ScmPrtSerialSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 1)
)
_ScmPrtSerialTable_Object = MibTable
scmPrtSerialTable = _ScmPrtSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2)
)
if mibBuilder.loadTexts:
    scmPrtSerialTable.setStatus("current")
_ScmPrtSerialEntry_Object = MibTableRow
scmPrtSerialEntry = _ScmPrtSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1)
)
scmPrtSerialEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtSerialIndex"),
)
if mibBuilder.loadTexts:
    scmPrtSerialEntry.setStatus("current")
_ScmPrtSerialIndex_Type = Ordinal32
_ScmPrtSerialIndex_Object = MibTableColumn
scmPrtSerialIndex = _ScmPrtSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1, 1),
    _ScmPrtSerialIndex_Type()
)
scmPrtSerialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scmPrtSerialIndex.setStatus("current")
_ScmPrtSerialNbaudRate_Type = Integer32
_ScmPrtSerialNbaudRate_Object = MibTableColumn
scmPrtSerialNbaudRate = _ScmPrtSerialNbaudRate_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1, 2),
    _ScmPrtSerialNbaudRate_Type()
)
scmPrtSerialNbaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtSerialNbaudRate.setStatus("current")
_ScmPrtSerialBrOptions_Type = Integer32
_ScmPrtSerialBrOptions_Object = MibTableColumn
scmPrtSerialBrOptions = _ScmPrtSerialBrOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1, 3),
    _ScmPrtSerialBrOptions_Type()
)
scmPrtSerialBrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtSerialBrOptions.setStatus("current")


class _ScmPrtSerialBobuxon_Type(Integer32):
    """Custom type scmPrtSerialBobuxon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmPrtSerialBobuxon_Type.__name__ = "Integer32"
_ScmPrtSerialBobuxon_Object = MibTableColumn
scmPrtSerialBobuxon = _ScmPrtSerialBobuxon_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1, 4),
    _ScmPrtSerialBobuxon_Type()
)
scmPrtSerialBobuxon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtSerialBobuxon.setStatus("current")
_ScmPrtSerialBobuxonOptions_Type = Integer32
_ScmPrtSerialBobuxonOptions_Object = MibTableColumn
scmPrtSerialBobuxonOptions = _ScmPrtSerialBobuxonOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 21, 2, 1, 5),
    _ScmPrtSerialBobuxonOptions_Type()
)
scmPrtSerialBobuxonOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtSerialBobuxonOptions.setStatus("current")
_ScmPrtPCL_ObjectIdentity = ObjectIdentity
scmPrtPCL = _ScmPrtPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22)
)
_ScmPrtPCLSimple_ObjectIdentity = ObjectIdentity
scmPrtPCLSimple = _ScmPrtPCLSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1)
)


class _ScmPrtPCLFont_Type(Integer32):
    """Custom type scmPrtPCLFont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_ScmPrtPCLFont_Type.__name__ = "Integer32"
_ScmPrtPCLFont_Object = MibScalar
scmPrtPCLFont = _ScmPrtPCLFont_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 1),
    _ScmPrtPCLFont_Type()
)
scmPrtPCLFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLFont.setStatus("current")


class _ScmPrtPCLSymbolSet_Type(Integer32):
    """Custom type scmPrtPCLSymbolSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 37),
    )


_ScmPrtPCLSymbolSet_Type.__name__ = "Integer32"
_ScmPrtPCLSymbolSet_Object = MibScalar
scmPrtPCLSymbolSet = _ScmPrtPCLSymbolSet_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 2),
    _ScmPrtPCLSymbolSet_Type()
)
scmPrtPCLSymbolSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLSymbolSet.setStatus("current")


class _ScmPrtPCLFormLine_Type(Integer32):
    """Custom type scmPrtPCLFormLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_ScmPrtPCLFormLine_Type.__name__ = "Integer32"
_ScmPrtPCLFormLine_Object = MibScalar
scmPrtPCLFormLine = _ScmPrtPCLFormLine_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 3),
    _ScmPrtPCLFormLine_Type()
)
scmPrtPCLFormLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLFormLine.setStatus("current")


class _ScmPrtPCLPitch_Type(Integer32):
    """Custom type scmPrtPCLPitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 399),
    )


_ScmPrtPCLPitch_Type.__name__ = "Integer32"
_ScmPrtPCLPitch_Object = MibScalar
scmPrtPCLPitch = _ScmPrtPCLPitch_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 4),
    _ScmPrtPCLPitch_Type()
)
scmPrtPCLPitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLPitch.setStatus("current")


class _ScmPrtPCLPointSize_Type(Integer32):
    """Custom type scmPrtPCLPointSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 399),
    )


_ScmPrtPCLPointSize_Type.__name__ = "Integer32"
_ScmPrtPCLPointSize_Object = MibScalar
scmPrtPCLPointSize = _ScmPrtPCLPointSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 5),
    _ScmPrtPCLPointSize_Type()
)
scmPrtPCLPointSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLPointSize.setStatus("current")
_ScmPrtPCLCourier_Type = Integer32
_ScmPrtPCLCourier_Object = MibScalar
scmPrtPCLCourier = _ScmPrtPCLCourier_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 6),
    _ScmPrtPCLCourier_Type()
)
scmPrtPCLCourier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLCourier.setStatus("current")


class _ScmPrtPCLCourierOptions_Type(Integer32):
    """Custom type scmPrtPCLCourierOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dark", 2),
          ("regular", 1))
    )


_ScmPrtPCLCourierOptions_Type.__name__ = "Integer32"
_ScmPrtPCLCourierOptions_Object = MibScalar
scmPrtPCLCourierOptions = _ScmPrtPCLCourierOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 7),
    _ScmPrtPCLCourierOptions_Type()
)
scmPrtPCLCourierOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtPCLCourierOptions.setStatus("current")
_ScmPrtPCLAppendCR_Type = Integer32
_ScmPrtPCLAppendCR_Object = MibScalar
scmPrtPCLAppendCR = _ScmPrtPCLAppendCR_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 8),
    _ScmPrtPCLAppendCR_Type()
)
scmPrtPCLAppendCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLAppendCR.setStatus("current")


class _ScmPrtPCLAppendCROptions_Type(Integer32):
    """Custom type scmPrtPCLAppendCROptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lf", 1),
          ("lfCR", 2))
    )


_ScmPrtPCLAppendCROptions_Type.__name__ = "Integer32"
_ScmPrtPCLAppendCROptions_Object = MibScalar
scmPrtPCLAppendCROptions = _ScmPrtPCLAppendCROptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 9),
    _ScmPrtPCLAppendCROptions_Type()
)
scmPrtPCLAppendCROptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtPCLAppendCROptions.setStatus("current")
_ScmPrtPCLWideA4_Type = Integer32
_ScmPrtPCLWideA4_Object = MibScalar
scmPrtPCLWideA4 = _ScmPrtPCLWideA4_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 10),
    _ScmPrtPCLWideA4_Type()
)
scmPrtPCLWideA4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLWideA4.setStatus("current")


class _ScmPrtPCLWideA4Options_Type(Integer32):
    """Custom type scmPrtPCLWideA4Options based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtPCLWideA4Options_Type.__name__ = "Integer32"
_ScmPrtPCLWideA4Options_Object = MibScalar
scmPrtPCLWideA4Options = _ScmPrtPCLWideA4Options_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 11),
    _ScmPrtPCLWideA4Options_Type()
)
scmPrtPCLWideA4Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtPCLWideA4Options.setStatus("current")


class _ScmPrtPCLTopMargin_Type(Integer32):
    """Custom type scmPrtPCLTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_ScmPrtPCLTopMargin_Type.__name__ = "Integer32"
_ScmPrtPCLTopMargin_Object = MibScalar
scmPrtPCLTopMargin = _ScmPrtPCLTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 12),
    _ScmPrtPCLTopMargin_Type()
)
scmPrtPCLTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLTopMargin.setStatus("current")


class _ScmPrtPCLLeftMargin_Type(Integer32):
    """Custom type scmPrtPCLLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_ScmPrtPCLLeftMargin_Type.__name__ = "Integer32"
_ScmPrtPCLLeftMargin_Object = MibScalar
scmPrtPCLLeftMargin = _ScmPrtPCLLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 1, 13),
    _ScmPrtPCLLeftMargin_Type()
)
scmPrtPCLLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtPCLLeftMargin.setStatus("current")
_ScmPrtPCLTable_Object = MibTable
scmPrtPCLTable = _ScmPrtPCLTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 2)
)
if mibBuilder.loadTexts:
    scmPrtPCLTable.setStatus("current")
_ScmPrtPCLEntry_Object = MibTableRow
scmPrtPCLEntry = _ScmPrtPCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 2, 1)
)
scmPrtPCLEntry.setIndexNames(
    (0, "SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLIndex"),
)
if mibBuilder.loadTexts:
    scmPrtPCLEntry.setStatus("current")
_ScmPrtPCLIndex_Type = Ordinal32
_ScmPrtPCLIndex_Object = MibTableColumn
scmPrtPCLIndex = _ScmPrtPCLIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 22, 2, 1, 1),
    _ScmPrtPCLIndex_Type()
)
scmPrtPCLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtPCLIndex.setStatus("current")
_ScmPrtKS5843_ObjectIdentity = ObjectIdentity
scmPrtKS5843 = _ScmPrtKS5843_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23)
)
_ScmPrtKS5843Simple_ObjectIdentity = ObjectIdentity
scmPrtKS5843Simple = _ScmPrtKS5843Simple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1)
)
_ScmPrtKS5843Font_Type = Integer32
_ScmPrtKS5843Font_Object = MibScalar
scmPrtKS5843Font = _ScmPrtKS5843Font_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 1),
    _ScmPrtKS5843Font_Type()
)
scmPrtKS5843Font.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Font.setStatus("current")


class _ScmPrtKS5843FontOptions_Type(Integer32):
    """Custom type scmPrtKS5843FontOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("gothic", 2),
          ("gullim", 8),
          ("gungseo", 4),
          ("headline", 1024),
          ("myoungjo", 1),
          ("newgraph", 128),
          ("ocrB1", 2048),
          ("pilgi", 512),
          ("post", 64),
          ("sammool", 16),
          ("sunmyun", 256),
          ("yetche", 32))
    )


_ScmPrtKS5843FontOptions_Type.__name__ = "Integer32"
_ScmPrtKS5843FontOptions_Object = MibScalar
scmPrtKS5843FontOptions = _ScmPrtKS5843FontOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 2),
    _ScmPrtKS5843FontOptions_Type()
)
scmPrtKS5843FontOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKS5843FontOptions.setStatus("current")
_ScmPrtKS5843Code_Type = Integer32
_ScmPrtKS5843Code_Object = MibScalar
scmPrtKS5843Code = _ScmPrtKS5843Code_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 3),
    _ScmPrtKS5843Code_Type()
)
scmPrtKS5843Code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Code.setStatus("current")


class _ScmPrtKS5843CodeOptions_Type(Integer32):
    """Custom type scmPrtKS5843CodeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("johap", 2),
          ("wansung", 1))
    )


_ScmPrtKS5843CodeOptions_Type.__name__ = "Integer32"
_ScmPrtKS5843CodeOptions_Object = MibScalar
scmPrtKS5843CodeOptions = _ScmPrtKS5843CodeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 4),
    _ScmPrtKS5843CodeOptions_Type()
)
scmPrtKS5843CodeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKS5843CodeOptions.setStatus("current")
_ScmPrtKS5843cpi_Type = Integer32
_ScmPrtKS5843cpi_Object = MibScalar
scmPrtKS5843cpi = _ScmPrtKS5843cpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 5),
    _ScmPrtKS5843cpi_Type()
)
scmPrtKS5843cpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843cpi.setStatus("current")


class _ScmPrtKS5843cpiOptions_Type(Integer32):
    """Custom type scmPrtKS5843cpiOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("kscpi10", 1),
          ("kscpi12", 2),
          ("kscpi133", 4),
          ("kscpi15", 8),
          ("kscpi20", 16),
          ("kscpi24", 32),
          ("kscpi267", 64),
          ("kscpi30", 128))
    )


_ScmPrtKS5843cpiOptions_Type.__name__ = "Integer32"
_ScmPrtKS5843cpiOptions_Object = MibScalar
scmPrtKS5843cpiOptions = _ScmPrtKS5843cpiOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 6),
    _ScmPrtKS5843cpiOptions_Type()
)
scmPrtKS5843cpiOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKS5843cpiOptions.setStatus("current")


class _ScmPrtKS5843Lines_Type(Integer32):
    """Custom type scmPrtKS5843Lines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_ScmPrtKS5843Lines_Type.__name__ = "Integer32"
_ScmPrtKS5843Lines_Object = MibScalar
scmPrtKS5843Lines = _ScmPrtKS5843Lines_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 7),
    _ScmPrtKS5843Lines_Type()
)
scmPrtKS5843Lines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Lines.setStatus("current")


class _ScmPrtKS5843Zoom_Type(Integer32):
    """Custom type scmPrtKS5843Zoom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_ScmPrtKS5843Zoom_Type.__name__ = "Integer32"
_ScmPrtKS5843Zoom_Object = MibScalar
scmPrtKS5843Zoom = _ScmPrtKS5843Zoom_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 8),
    _ScmPrtKS5843Zoom_Type()
)
scmPrtKS5843Zoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Zoom.setStatus("current")
_ScmPrtKS5843AutoWrap_Type = Integer32
_ScmPrtKS5843AutoWrap_Object = MibScalar
scmPrtKS5843AutoWrap = _ScmPrtKS5843AutoWrap_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 9),
    _ScmPrtKS5843AutoWrap_Type()
)
scmPrtKS5843AutoWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843AutoWrap.setStatus("current")


class _ScmPrtKS5843AutoWrapOptions_Type(Integer32):
    """Custom type scmPrtKS5843AutoWrapOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtKS5843AutoWrapOptions_Type.__name__ = "Integer32"
_ScmPrtKS5843AutoWrapOptions_Object = MibScalar
scmPrtKS5843AutoWrapOptions = _ScmPrtKS5843AutoWrapOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 10),
    _ScmPrtKS5843AutoWrapOptions_Type()
)
scmPrtKS5843AutoWrapOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKS5843AutoWrapOptions.setStatus("current")


class _ScmPrtKS5843Topmargin_Type(Integer32):
    """Custom type scmPrtKS5843Topmargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ScmPrtKS5843Topmargin_Type.__name__ = "Integer32"
_ScmPrtKS5843Topmargin_Object = MibScalar
scmPrtKS5843Topmargin = _ScmPrtKS5843Topmargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 11),
    _ScmPrtKS5843Topmargin_Type()
)
scmPrtKS5843Topmargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Topmargin.setStatus("current")


class _ScmPrtKS5843Sitemode_Type(Integer32):
    """Custom type scmPrtKS5843Sitemode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ScmPrtKS5843Sitemode_Type.__name__ = "Integer32"
_ScmPrtKS5843Sitemode_Object = MibScalar
scmPrtKS5843Sitemode = _ScmPrtKS5843Sitemode_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 23, 1, 12),
    _ScmPrtKS5843Sitemode_Type()
)
scmPrtKS5843Sitemode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKS5843Sitemode.setStatus("current")
_ScmPrtKSSM_ObjectIdentity = ObjectIdentity
scmPrtKSSM = _ScmPrtKSSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24)
)
_ScmPrtKSSMSimple_ObjectIdentity = ObjectIdentity
scmPrtKSSMSimple = _ScmPrtKSSMSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1)
)
_ScmPrtKSSMFont_Type = Integer32
_ScmPrtKSSMFont_Object = MibScalar
scmPrtKSSMFont = _ScmPrtKSSMFont_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 1),
    _ScmPrtKSSMFont_Type()
)
scmPrtKSSMFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMFont.setStatus("current")


class _ScmPrtKSSMFontOptions_Type(Integer32):
    """Custom type scmPrtKSSMFontOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("gothic", 2),
          ("gullim", 8),
          ("gungseo", 4),
          ("headline", 1024),
          ("myoungjo", 1),
          ("newgraph", 128),
          ("ocrB1", 2048),
          ("pilgi", 512),
          ("post", 64),
          ("sammool", 16),
          ("sunmyun", 256),
          ("yetche", 32))
    )


_ScmPrtKSSMFontOptions_Type.__name__ = "Integer32"
_ScmPrtKSSMFontOptions_Object = MibScalar
scmPrtKSSMFontOptions = _ScmPrtKSSMFontOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 2),
    _ScmPrtKSSMFontOptions_Type()
)
scmPrtKSSMFontOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKSSMFontOptions.setStatus("current")
_ScmPrtKSSMCode_Type = Integer32
_ScmPrtKSSMCode_Object = MibScalar
scmPrtKSSMCode = _ScmPrtKSSMCode_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 3),
    _ScmPrtKSSMCode_Type()
)
scmPrtKSSMCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMCode.setStatus("current")


class _ScmPrtKSSMCodeOptions_Type(Integer32):
    """Custom type scmPrtKSSMCodeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("johap", 2),
          ("wansung", 1))
    )


_ScmPrtKSSMCodeOptions_Type.__name__ = "Integer32"
_ScmPrtKSSMCodeOptions_Object = MibScalar
scmPrtKSSMCodeOptions = _ScmPrtKSSMCodeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 4),
    _ScmPrtKSSMCodeOptions_Type()
)
scmPrtKSSMCodeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKSSMCodeOptions.setStatus("current")
_ScmPrtKSSMCPI_Type = Integer32
_ScmPrtKSSMCPI_Object = MibScalar
scmPrtKSSMCPI = _ScmPrtKSSMCPI_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 5),
    _ScmPrtKSSMCPI_Type()
)
scmPrtKSSMCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMCPI.setStatus("current")


class _ScmPrtKSSMCPIOptions_Type(Integer32):
    """Custom type scmPrtKSSMCPIOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("kscpi10", 1),
          ("kscpi12", 2),
          ("kscpi133", 4),
          ("kscpi15", 8),
          ("kscpi20", 16),
          ("kscpi24", 32),
          ("kscpi267", 64),
          ("kscpi30", 128))
    )


_ScmPrtKSSMCPIOptions_Type.__name__ = "Integer32"
_ScmPrtKSSMCPIOptions_Object = MibScalar
scmPrtKSSMCPIOptions = _ScmPrtKSSMCPIOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 6),
    _ScmPrtKSSMCPIOptions_Type()
)
scmPrtKSSMCPIOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKSSMCPIOptions.setStatus("current")


class _ScmPrtKSSMLines_Type(Integer32):
    """Custom type scmPrtKSSMLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_ScmPrtKSSMLines_Type.__name__ = "Integer32"
_ScmPrtKSSMLines_Object = MibScalar
scmPrtKSSMLines = _ScmPrtKSSMLines_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 7),
    _ScmPrtKSSMLines_Type()
)
scmPrtKSSMLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMLines.setStatus("current")


class _ScmPrtKSSMZoom_Type(Integer32):
    """Custom type scmPrtKSSMZoom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_ScmPrtKSSMZoom_Type.__name__ = "Integer32"
_ScmPrtKSSMZoom_Object = MibScalar
scmPrtKSSMZoom = _ScmPrtKSSMZoom_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 8),
    _ScmPrtKSSMZoom_Type()
)
scmPrtKSSMZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMZoom.setStatus("current")
_ScmPrtKSSMAutoWrap_Type = Integer32
_ScmPrtKSSMAutoWrap_Object = MibScalar
scmPrtKSSMAutoWrap = _ScmPrtKSSMAutoWrap_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 9),
    _ScmPrtKSSMAutoWrap_Type()
)
scmPrtKSSMAutoWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMAutoWrap.setStatus("current")


class _ScmPrtKSSMAutoWrapOptions_Type(Integer32):
    """Custom type scmPrtKSSMAutoWrapOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtKSSMAutoWrapOptions_Type.__name__ = "Integer32"
_ScmPrtKSSMAutoWrapOptions_Object = MibScalar
scmPrtKSSMAutoWrapOptions = _ScmPrtKSSMAutoWrapOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 10),
    _ScmPrtKSSMAutoWrapOptions_Type()
)
scmPrtKSSMAutoWrapOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtKSSMAutoWrapOptions.setStatus("current")


class _ScmPrtKSSMTopMargin_Type(Integer32):
    """Custom type scmPrtKSSMTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ScmPrtKSSMTopMargin_Type.__name__ = "Integer32"
_ScmPrtKSSMTopMargin_Object = MibScalar
scmPrtKSSMTopMargin = _ScmPrtKSSMTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 11),
    _ScmPrtKSSMTopMargin_Type()
)
scmPrtKSSMTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMTopMargin.setStatus("current")


class _ScmPrtKSSMSiteMode_Type(Integer32):
    """Custom type scmPrtKSSMSiteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ScmPrtKSSMSiteMode_Type.__name__ = "Integer32"
_ScmPrtKSSMSiteMode_Object = MibScalar
scmPrtKSSMSiteMode = _ScmPrtKSSMSiteMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 24, 1, 12),
    _ScmPrtKSSMSiteMode_Type()
)
scmPrtKSSMSiteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtKSSMSiteMode.setStatus("current")
_ScmPrtIPP_ObjectIdentity = ObjectIdentity
scmPrtIPP = _ScmPrtIPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25)
)
_ScmPrtIPPSimple_ObjectIdentity = ObjectIdentity
scmPrtIPPSimple = _ScmPrtIPPSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1)
)


class _ScmPrtIPPColorSupported_Type(Integer32):
    """Custom type scmPrtIPPColorSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ScmPrtIPPColorSupported_Type.__name__ = "Integer32"
_ScmPrtIPPColorSupported_Object = MibScalar
scmPrtIPPColorSupported = _ScmPrtIPPColorSupported_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 1),
    _ScmPrtIPPColorSupported_Type()
)
scmPrtIPPColorSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPColorSupported.setStatus("current")
_ScmPrtIPPJobKOctetsSupportedLBound_Type = Integer32
_ScmPrtIPPJobKOctetsSupportedLBound_Object = MibScalar
scmPrtIPPJobKOctetsSupportedLBound = _ScmPrtIPPJobKOctetsSupportedLBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 2),
    _ScmPrtIPPJobKOctetsSupportedLBound_Type()
)
scmPrtIPPJobKOctetsSupportedLBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobKOctetsSupportedLBound.setStatus("current")
_ScmPrtIPPJobKOctetsSupportedUBound_Type = Integer32
_ScmPrtIPPJobKOctetsSupportedUBound_Object = MibScalar
scmPrtIPPJobKOctetsSupportedUBound = _ScmPrtIPPJobKOctetsSupportedUBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 3),
    _ScmPrtIPPJobKOctetsSupportedUBound_Type()
)
scmPrtIPPJobKOctetsSupportedUBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobKOctetsSupportedUBound.setStatus("current")
_ScmPrtIPPJobImpressionsSupportedLBound_Type = Integer32
_ScmPrtIPPJobImpressionsSupportedLBound_Object = MibScalar
scmPrtIPPJobImpressionsSupportedLBound = _ScmPrtIPPJobImpressionsSupportedLBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 4),
    _ScmPrtIPPJobImpressionsSupportedLBound_Type()
)
scmPrtIPPJobImpressionsSupportedLBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobImpressionsSupportedLBound.setStatus("current")
_ScmPrtIPPJobImpressionsSupportedUBound_Type = Integer32
_ScmPrtIPPJobImpressionsSupportedUBound_Object = MibScalar
scmPrtIPPJobImpressionsSupportedUBound = _ScmPrtIPPJobImpressionsSupportedUBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 5),
    _ScmPrtIPPJobImpressionsSupportedUBound_Type()
)
scmPrtIPPJobImpressionsSupportedUBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobImpressionsSupportedUBound.setStatus("current")
_ScmPrtIPPJobMediaSheetsSupportedLBound_Type = Integer32
_ScmPrtIPPJobMediaSheetsSupportedLBound_Object = MibScalar
scmPrtIPPJobMediaSheetsSupportedLBound = _ScmPrtIPPJobMediaSheetsSupportedLBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 6),
    _ScmPrtIPPJobMediaSheetsSupportedLBound_Type()
)
scmPrtIPPJobMediaSheetsSupportedLBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobMediaSheetsSupportedLBound.setStatus("current")
_ScmPrtIPPJobMediaSheetsSupportedUBound_Type = Integer32
_ScmPrtIPPJobMediaSheetsSupportedUBound_Object = MibScalar
scmPrtIPPJobMediaSheetsSupportedUBound = _ScmPrtIPPJobMediaSheetsSupportedUBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 7),
    _ScmPrtIPPJobMediaSheetsSupportedUBound_Type()
)
scmPrtIPPJobMediaSheetsSupportedUBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobMediaSheetsSupportedUBound.setStatus("current")


class _ScmPrtIPPJobSheets_Type(Integer32):
    """Custom type scmPrtIPPJobSheets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("standard", 1))
    )


_ScmPrtIPPJobSheets_Type.__name__ = "Integer32"
_ScmPrtIPPJobSheets_Object = MibScalar
scmPrtIPPJobSheets = _ScmPrtIPPJobSheets_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 8),
    _ScmPrtIPPJobSheets_Type()
)
scmPrtIPPJobSheets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPJobSheets.setStatus("current")
_ScmPrtIPPCollatedCopiesLBound_Type = Integer32
_ScmPrtIPPCollatedCopiesLBound_Object = MibScalar
scmPrtIPPCollatedCopiesLBound = _ScmPrtIPPCollatedCopiesLBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 9),
    _ScmPrtIPPCollatedCopiesLBound_Type()
)
scmPrtIPPCollatedCopiesLBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPCollatedCopiesLBound.setStatus("current")
_ScmPrtIPPCollatedCopiesUBound_Type = Integer32
_ScmPrtIPPCollatedCopiesUBound_Object = MibScalar
scmPrtIPPCollatedCopiesUBound = _ScmPrtIPPCollatedCopiesUBound_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 10),
    _ScmPrtIPPCollatedCopiesUBound_Type()
)
scmPrtIPPCollatedCopiesUBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPCollatedCopiesUBound.setStatus("current")
_ScmPrtIPPCollatedCopies_Type = Integer32
_ScmPrtIPPCollatedCopies_Object = MibScalar
scmPrtIPPCollatedCopies = _ScmPrtIPPCollatedCopies_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 11),
    _ScmPrtIPPCollatedCopies_Type()
)
scmPrtIPPCollatedCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPCollatedCopies.setStatus("current")
_ScmPrtIPPFinishingsSupported_Type = Integer32
_ScmPrtIPPFinishingsSupported_Object = MibScalar
scmPrtIPPFinishingsSupported = _ScmPrtIPPFinishingsSupported_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 12),
    _ScmPrtIPPFinishingsSupported_Type()
)
scmPrtIPPFinishingsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPFinishingsSupported.setStatus("current")
_ScmPrtIPPFinishings_Type = Integer32
_ScmPrtIPPFinishings_Object = MibScalar
scmPrtIPPFinishings = _ScmPrtIPPFinishings_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 13),
    _ScmPrtIPPFinishings_Type()
)
scmPrtIPPFinishings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPFinishings.setStatus("current")


class _ScmPrtIPPPageRangesSupported_Type(Integer32):
    """Custom type scmPrtIPPPageRangesSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmPrtIPPPageRangesSupported_Type.__name__ = "Integer32"
_ScmPrtIPPPageRangesSupported_Object = MibScalar
scmPrtIPPPageRangesSupported = _ScmPrtIPPPageRangesSupported_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 14),
    _ScmPrtIPPPageRangesSupported_Type()
)
scmPrtIPPPageRangesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPPageRangesSupported.setStatus("current")
_ScmPrtIPPNumberUp_Type = Integer32
_ScmPrtIPPNumberUp_Object = MibScalar
scmPrtIPPNumberUp = _ScmPrtIPPNumberUp_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 15),
    _ScmPrtIPPNumberUp_Type()
)
scmPrtIPPNumberUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPNumberUp.setStatus("current")


class _ScmPrtIPPNumberUpOptions_Type(Integer32):
    """Custom type scmPrtIPPNumberUpOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("numberUp1", 1),
          ("numberUp16", 32),
          ("numberUp2", 2),
          ("numberUp4", 4),
          ("numberUp6", 8),
          ("numberUp9", 16))
    )


_ScmPrtIPPNumberUpOptions_Type.__name__ = "Integer32"
_ScmPrtIPPNumberUpOptions_Object = MibScalar
scmPrtIPPNumberUpOptions = _ScmPrtIPPNumberUpOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 16),
    _ScmPrtIPPNumberUpOptions_Type()
)
scmPrtIPPNumberUpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPNumberUpOptions.setStatus("current")
_ScmPrtIPPPrintQuality_Type = Integer32
_ScmPrtIPPPrintQuality_Object = MibScalar
scmPrtIPPPrintQuality = _ScmPrtIPPPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 17),
    _ScmPrtIPPPrintQuality_Type()
)
scmPrtIPPPrintQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtIPPPrintQuality.setStatus("current")


class _ScmPrtIPPPrintQualityOptions_Type(Integer32):
    """Custom type scmPrtIPPPrintQualityOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("draft", 1),
          ("high", 4),
          ("normal", 2))
    )


_ScmPrtIPPPrintQualityOptions_Type.__name__ = "Integer32"
_ScmPrtIPPPrintQualityOptions_Object = MibScalar
scmPrtIPPPrintQualityOptions = _ScmPrtIPPPrintQualityOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 18),
    _ScmPrtIPPPrintQualityOptions_Type()
)
scmPrtIPPPrintQualityOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPPrintQualityOptions.setStatus("current")
_ScmPrtIPPJobKOctetsProcessed_Type = Integer32
_ScmPrtIPPJobKOctetsProcessed_Object = MibScalar
scmPrtIPPJobKOctetsProcessed = _ScmPrtIPPJobKOctetsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 19),
    _ScmPrtIPPJobKOctetsProcessed_Type()
)
scmPrtIPPJobKOctetsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobKOctetsProcessed.setStatus("current")
_ScmPrtIPPJobImpressionsCompleted_Type = Integer32
_ScmPrtIPPJobImpressionsCompleted_Object = MibScalar
scmPrtIPPJobImpressionsCompleted = _ScmPrtIPPJobImpressionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 20),
    _ScmPrtIPPJobImpressionsCompleted_Type()
)
scmPrtIPPJobImpressionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobImpressionsCompleted.setStatus("current")
_ScmPrtIPPJobMediaSheetsCompleted_Type = Integer32
_ScmPrtIPPJobMediaSheetsCompleted_Object = MibScalar
scmPrtIPPJobMediaSheetsCompleted = _ScmPrtIPPJobMediaSheetsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 25, 1, 21),
    _ScmPrtIPPJobMediaSheetsCompleted_Type()
)
scmPrtIPPJobMediaSheetsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtIPPJobMediaSheetsCompleted.setStatus("current")
_ScmPrtAlert_ObjectIdentity = ObjectIdentity
scmPrtAlert = _ScmPrtAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 26)
)
_ScmPrtAlertSimple_ObjectIdentity = ObjectIdentity
scmPrtAlertSimple = _ScmPrtAlertSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 26, 1)
)


class _ScmPrtAlertAlarmShortage_Type(Integer32):
    """Custom type scmPrtAlertAlarmShortage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ScmPrtAlertAlarmShortage_Type.__name__ = "Integer32"
_ScmPrtAlertAlarmShortage_Object = MibScalar
scmPrtAlertAlarmShortage = _ScmPrtAlertAlarmShortage_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 26, 1, 1),
    _ScmPrtAlertAlarmShortage_Type()
)
scmPrtAlertAlarmShortage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtAlertAlarmShortage.setStatus("current")
_ScmPrtAlertAlarmShortageOptions_Type = Integer32
_ScmPrtAlertAlarmShortageOptions_Object = MibScalar
scmPrtAlertAlarmShortageOptions = _ScmPrtAlertAlarmShortageOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 26, 1, 2),
    _ScmPrtAlertAlarmShortageOptions_Type()
)
scmPrtAlertAlarmShortageOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPrtAlertAlarmShortageOptions.setStatus("current")
_ScmPrtConsoleDisplayBuffer_ObjectIdentity = ObjectIdentity
scmPrtConsoleDisplayBuffer = _ScmPrtConsoleDisplayBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 27)
)
_ScmPrtConsoleDisplayBufferSimple_ObjectIdentity = ObjectIdentity
scmPrtConsoleDisplayBufferSimple = _ScmPrtConsoleDisplayBufferSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 27, 1)
)


class _ScmPrtConsoleDisplayBufferLcdLangType_Type(Integer32):
    """Custom type scmPrtConsoleDisplayBufferLcdLangType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("french", 4),
          ("german", 2),
          ("italian", 8),
          ("spanish", 16))
    )


_ScmPrtConsoleDisplayBufferLcdLangType_Type.__name__ = "Integer32"
_ScmPrtConsoleDisplayBufferLcdLangType_Object = MibScalar
scmPrtConsoleDisplayBufferLcdLangType = _ScmPrtConsoleDisplayBufferLcdLangType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 27, 1, 1),
    _ScmPrtConsoleDisplayBufferLcdLangType_Type()
)
scmPrtConsoleDisplayBufferLcdLangType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConsoleDisplayBufferLcdLangType.setStatus("current")
_ScmPrtConsoleDisplayBufferLcdLangTypeOptions_Type = Integer32
_ScmPrtConsoleDisplayBufferLcdLangTypeOptions_Object = MibScalar
scmPrtConsoleDisplayBufferLcdLangTypeOptions = _ScmPrtConsoleDisplayBufferLcdLangTypeOptions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 27, 1, 2),
    _ScmPrtConsoleDisplayBufferLcdLangTypeOptions_Type()
)
scmPrtConsoleDisplayBufferLcdLangTypeOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmPrtConsoleDisplayBufferLcdLangTypeOptions.setStatus("current")
prtGeneralEntry.registerAugmentions(
    ("SAMSUNG-PRINTER-EXT-MIB",
     "scmPrtGeneralEntry")
)
scmPrtGeneralEntry.setIndexNames(*prtGeneralEntry.getIndexNames())
prtInputEntry.registerAugmentions(
    ("SAMSUNG-PRINTER-EXT-MIB",
     "scmPrtInputEntry")
)
scmPrtInputEntry.setIndexNames(*prtInputEntry.getIndexNames())
prtOutputEntry.registerAugmentions(
    ("SAMSUNG-PRINTER-EXT-MIB",
     "scmPrtOutputEntry")
)
scmPrtOutputEntry.setIndexNames(*prtOutputEntry.getIndexNames())
prtChannelEntry.registerAugmentions(
    ("SAMSUNG-PRINTER-EXT-MIB",
     "scmPrtChannelEntry")
)
scmPrtChannelEntry.setIndexNames(*prtChannelEntry.getIndexNames())
prtInterpreterEntry.registerAugmentions(
    ("SAMSUNG-PRINTER-EXT-MIB",
     "scmPrtInterpreterEntry")
)
scmPrtInterpreterEntry.setIndexNames(*prtInterpreterEntry.getIndexNames())

# Managed Objects groups

scmPrtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 1)
)
scmPrtBaseGroup.setObjects(
    ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtBaseRowStatus")
)
if mibBuilder.loadTexts:
    scmPrtBaseGroup.setStatus("current")

scmPrtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 5)
)
scmPrtGeneralGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralRowStatus"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnModelName"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnModelVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnOSFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnSerialNo"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnPCLFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnEngFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnSCFFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnEpsonVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnPCL5eVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnPSFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnScanFWVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnKS5843Ver"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnKSSMVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnKS5895Ver"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnMainSystemVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnSPLVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrncolorPPM"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnPCL5CeVer"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnModelDescr"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnManufacture"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtGeneralPrnVendor"))
)
if mibBuilder.loadTexts:
    scmPrtGeneralGroup.setStatus("current")

scmPrtInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 8)
)
scmPrtInputGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputRowStatus"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputNextPrtInputIndex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputUseCustomSize"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputCustDimFeedDirDecl"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputCustDimXFeedDirDecl"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputTrayPriority"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputPaperSize"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputPaperSizeOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputTrayNum"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputTrayNumOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputTraySwitch"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputTraySwitchOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputLockTray"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputLockTrayOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputPaperType"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInputPaperTypeOptions"))
)
if mibBuilder.loadTexts:
    scmPrtInputGroup.setStatus("current")

scmPrtOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 9)
)
scmPrtOutputGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputRowStatus"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputNextIndex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputPassword"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputOffsetStackingType"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputTrayTimeoutSupport"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputTrayTimeout"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputFinishier"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOutputFinishierOptions"))
)
if mibBuilder.loadTexts:
    scmPrtOutputGroup.setStatus("current")

scmPrtChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 14)
)
scmPrtChannelGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtChannelRowStatus"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtChannelEOJTimeout"))
)
if mibBuilder.loadTexts:
    scmPrtChannelGroup.setStatus("current")

scmPrtInterpreterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 15)
)
scmPrtInterpreterGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpRowStatus"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpJobCopiesDefault"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpLineTerm"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpProcessBarcodes"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpOrientation"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpOrientationOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpreterCopyNum"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpreterEmulation"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtInterpreterEmulationOptions"))
)
if mibBuilder.loadTexts:
    scmPrtInterpreterGroup.setStatus("current")

scmPrtMarkerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 17)
)
scmPrtMarkerGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerResolution"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerResolutionOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerIndex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerColor"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerColorDescription"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerSrt"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerMarginUnit"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerLevel"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerDensity"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerSrtOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerDensityOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerSmetMode"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerSmetModeOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerduplexTopMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerduplexLeftMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerShortEdgeBindingMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerLongEdgeBindingMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerSave"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerSaveOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerOutAction"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtMarkerTonerOutActionOptions"))
)
if mibBuilder.loadTexts:
    scmPrtMarkerGroup.setStatus("current")

scmPrtOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 18)
)
scmPrtOperationGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationJobCancel"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperarionMenuClear"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationMenuClearOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationFuserClean"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationFuserCleanOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationOpcClean"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationOpcCleanOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationTestPrtRequest"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationPrintFontRequest"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationIndex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtOperationPrintBlackOnly"))
)
if mibBuilder.loadTexts:
    scmPrtOperationGroup.setStatus("current")

scmPrtConfiguratioinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 19)
)
scmPrtConfiguratioinGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationPowerSave"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationPowerSaveOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationAutocont"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationAutoCountOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationJam2Recover"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationJam2RecOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationAltitudeAction"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationAltitudeActionOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConfigurationIndex"))
)
if mibBuilder.loadTexts:
    scmPrtConfiguratioinGroup.setStatus("current")

scmPrtCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 20)
)
scmPrtCountGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountDrumImageCount"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountDrumImageCountReset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountTransferImageCount"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountTransferImageCountReset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountFuserImageCount"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountFuserImageCountReset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountTwoRollerCount"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountTwoRollerReset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupMPCount"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupMPReset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupTray1Count"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupTray1Reset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupTray2Count"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountPickupTray2Reset"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountIndex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountType"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountMediaSize"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountColorant"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountDuplex"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountUnit"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountResolution"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountValue"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtCountDeviceType"))
)
if mibBuilder.loadTexts:
    scmPrtCountGroup.setStatus("current")

scmPrtSerialGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 21)
)
scmPrtSerialGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtSerialNbaudRate"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtSerialBrOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtSerialBobuxon"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtSerialBobuxonOptions"))
)
if mibBuilder.loadTexts:
    scmPrtSerialGroup.setStatus("current")

scmPrtPCLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 22)
)
scmPrtPCLGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLFont"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLSymbolSet"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLFormLine"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLPitch"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLPointSize"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLCourier"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLCourierOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLAppendCR"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLAppendCROptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLWideA4"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLWideA4Options"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLTopMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLLeftMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtPCLIndex"))
)
if mibBuilder.loadTexts:
    scmPrtPCLGroup.setStatus("current")

scmPrtKS5843Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 23)
)
scmPrtKS5843Group.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Font"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843FontOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Code"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843CodeOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843cpi"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843cpiOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Lines"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Zoom"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843AutoWrap"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843AutoWrapOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Topmargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKS5843Sitemode"))
)
if mibBuilder.loadTexts:
    scmPrtKS5843Group.setStatus("current")

scmPrtKSSMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 24)
)
scmPrtKSSMGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMFont"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMFontOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMCode"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMCodeOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMCPI"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMCPIOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMLines"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMZoom"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMAutoWrap"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMAutoWrapOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMTopMargin"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtKSSMSiteMode"))
)
if mibBuilder.loadTexts:
    scmPrtKSSMGroup.setStatus("current")

scmPrtIPPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 25)
)
scmPrtIPPGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPColorSupported"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobKOctetsSupportedLBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobKOctetsSupportedUBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobImpressionsSupportedLBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobImpressionsSupportedUBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobMediaSheetsSupportedLBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobMediaSheetsSupportedUBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobSheets"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPCollatedCopiesLBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPCollatedCopiesUBound"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPCollatedCopies"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPFinishingsSupported"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPFinishings"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPPageRangesSupported"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPNumberUp"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPNumberUpOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPPrintQuality"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPPrintQualityOptions"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobKOctetsProcessed"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobImpressionsCompleted"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtIPPJobMediaSheetsCompleted"))
)
if mibBuilder.loadTexts:
    scmPrtIPPGroup.setStatus("current")

scmPrtAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 26)
)
scmPrtAlertGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtAlertAlarmShortage"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtAlertAlarmShortageOptions"))
)
if mibBuilder.loadTexts:
    scmPrtAlertGroup.setStatus("current")

scmPrtConsoleDisplayBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 3, 27)
)
scmPrtConsoleDisplayBufferGroup.setObjects(
      *(("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConsoleDisplayBufferLcdLangType"),
        ("SAMSUNG-PRINTER-EXT-MIB", "scmPrtConsoleDisplayBufferLcdLangTypeOptions"))
)
if mibBuilder.loadTexts:
    scmPrtConsoleDisplayBufferGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

scmPrtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 55, 2, 1)
)
if mibBuilder.loadTexts:
    scmPrtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-PRINTER-EXT-MIB",
    **{"scmPrintMIB": scmPrintMIB,
       "scmPrtBase": scmPrtBase,
       "scmPrtBaseTable": scmPrtBaseTable,
       "scmPrtBaseEntry": scmPrtBaseEntry,
       "scmPrtBaseIndex": scmPrtBaseIndex,
       "scmPrtBaseRowStatus": scmPrtBaseRowStatus,
       "scmPrtMIBConformance": scmPrtMIBConformance,
       "scmPrtMIBCompliance": scmPrtMIBCompliance,
       "scmPrtMIBGroups": scmPrtMIBGroups,
       "scmPrtBaseGroup": scmPrtBaseGroup,
       "scmPrtGeneralGroup": scmPrtGeneralGroup,
       "scmPrtInputGroup": scmPrtInputGroup,
       "scmPrtOutputGroup": scmPrtOutputGroup,
       "scmPrtChannelGroup": scmPrtChannelGroup,
       "scmPrtInterpreterGroup": scmPrtInterpreterGroup,
       "scmPrtMarkerGroup": scmPrtMarkerGroup,
       "scmPrtOperationGroup": scmPrtOperationGroup,
       "scmPrtConfiguratioinGroup": scmPrtConfiguratioinGroup,
       "scmPrtCountGroup": scmPrtCountGroup,
       "scmPrtSerialGroup": scmPrtSerialGroup,
       "scmPrtPCLGroup": scmPrtPCLGroup,
       "scmPrtKS5843Group": scmPrtKS5843Group,
       "scmPrtKSSMGroup": scmPrtKSSMGroup,
       "scmPrtIPPGroup": scmPrtIPPGroup,
       "scmPrtAlertGroup": scmPrtAlertGroup,
       "scmPrtConsoleDisplayBufferGroup": scmPrtConsoleDisplayBufferGroup,
       "scmPrtGeneral": scmPrtGeneral,
       "scmPrtGeneralSimple": scmPrtGeneralSimple,
       "scmPrtGeneralPrnModelName": scmPrtGeneralPrnModelName,
       "scmPrtGeneralPrnOSFWVer": scmPrtGeneralPrnOSFWVer,
       "scmPrtGeneralPrnModelVer": scmPrtGeneralPrnModelVer,
       "scmPrtGeneralPrnSerialNo": scmPrtGeneralPrnSerialNo,
       "scmPrtGeneralPrnModelDescr": scmPrtGeneralPrnModelDescr,
       "scmPrtGeneralPrnManufacture": scmPrtGeneralPrnManufacture,
       "scmPrtGeneralPrnVendor": scmPrtGeneralPrnVendor,
       "scmPrtGeneralPrnPCLFWVer": scmPrtGeneralPrnPCLFWVer,
       "scmPrtGeneralPrnEngFWVer": scmPrtGeneralPrnEngFWVer,
       "scmPrtGeneralPrnSCFFWVer": scmPrtGeneralPrnSCFFWVer,
       "scmPrtGeneralPrnEpsonVer": scmPrtGeneralPrnEpsonVer,
       "scmPrtGeneralPrnPCL5eVer": scmPrtGeneralPrnPCL5eVer,
       "scmPrtGeneralPrnPSFWVer": scmPrtGeneralPrnPSFWVer,
       "scmPrtGeneralPrnScanFWVer": scmPrtGeneralPrnScanFWVer,
       "scmPrtGeneralPrnKS5843Ver": scmPrtGeneralPrnKS5843Ver,
       "scmPrtGeneralPrnKSSMVer": scmPrtGeneralPrnKSSMVer,
       "scmPrtGeneralPrnKS5895Ver": scmPrtGeneralPrnKS5895Ver,
       "scmPrtGeneralPrnMainSystemVer": scmPrtGeneralPrnMainSystemVer,
       "scmPrtGeneralPrnSPLVer": scmPrtGeneralPrnSPLVer,
       "scmPrtGeneralPrncolorPPM": scmPrtGeneralPrncolorPPM,
       "scmPrtGeneralPrnPCL5CeVer": scmPrtGeneralPrnPCL5CeVer,
       "scmPrtGeneralTable": scmPrtGeneralTable,
       "scmPrtGeneralEntry": scmPrtGeneralEntry,
       "scmPrtGeneralRowStatus": scmPrtGeneralRowStatus,
       "scmPrtInput": scmPrtInput,
       "scmPrtInputSimple": scmPrtInputSimple,
       "scmPrtInputTraySwitch": scmPrtInputTraySwitch,
       "scmPrtInputTraySwitchOptions": scmPrtInputTraySwitchOptions,
       "scmPrtInputLockTray": scmPrtInputLockTray,
       "scmPrtInputLockTrayOptions": scmPrtInputLockTrayOptions,
       "scmPrtInputPaperType": scmPrtInputPaperType,
       "scmPrtInputPaperTypeOptions": scmPrtInputPaperTypeOptions,
       "scmPrtInputTable": scmPrtInputTable,
       "scmPrtInputEntry": scmPrtInputEntry,
       "scmPrtInputRowStatus": scmPrtInputRowStatus,
       "scmPrtInputNextPrtInputIndex": scmPrtInputNextPrtInputIndex,
       "scmPrtInputUseCustomSize": scmPrtInputUseCustomSize,
       "scmPrtInputCustDimFeedDirDecl": scmPrtInputCustDimFeedDirDecl,
       "scmPrtInputCustDimXFeedDirDecl": scmPrtInputCustDimXFeedDirDecl,
       "scmPrtInputTrayPriority": scmPrtInputTrayPriority,
       "scmPrtInputPaperSize": scmPrtInputPaperSize,
       "scmPrtInputPaperSizeOptions": scmPrtInputPaperSizeOptions,
       "scmPrtInputTrayNum": scmPrtInputTrayNum,
       "scmPrtInputTrayNumOptions": scmPrtInputTrayNumOptions,
       "scmPrtOutput": scmPrtOutput,
       "scmPrtOutputTable": scmPrtOutputTable,
       "scmPrtOutputEntry": scmPrtOutputEntry,
       "scmPrtOutputRowStatus": scmPrtOutputRowStatus,
       "scmPrtOutputNextIndex": scmPrtOutputNextIndex,
       "scmPrtOutputPassword": scmPrtOutputPassword,
       "scmPrtOutputOffsetStackingType": scmPrtOutputOffsetStackingType,
       "scmPrtOutputTrayTimeoutSupport": scmPrtOutputTrayTimeoutSupport,
       "scmPrtOutputTrayTimeout": scmPrtOutputTrayTimeout,
       "scmPrtOutputFinishier": scmPrtOutputFinishier,
       "scmPrtOutputFinishierOptions": scmPrtOutputFinishierOptions,
       "scmPrtChannel": scmPrtChannel,
       "scmPrtChannelSimple": scmPrtChannelSimple,
       "scmPrtChannelTable": scmPrtChannelTable,
       "scmPrtChannelEntry": scmPrtChannelEntry,
       "scmPrtChannelRowStatus": scmPrtChannelRowStatus,
       "scmPrtChannelEOJTimeout": scmPrtChannelEOJTimeout,
       "scmPrtInterpreter": scmPrtInterpreter,
       "scmPrtInterpreterSimple": scmPrtInterpreterSimple,
       "scmPrtInterpreterCopyNum": scmPrtInterpreterCopyNum,
       "scmPrtInterpreterEmulation": scmPrtInterpreterEmulation,
       "scmPrtInterpreterEmulationOptions": scmPrtInterpreterEmulationOptions,
       "scmPrtInterpreterTable": scmPrtInterpreterTable,
       "scmPrtInterpreterEntry": scmPrtInterpreterEntry,
       "scmPrtInterpRowStatus": scmPrtInterpRowStatus,
       "scmPrtInterpJobCopiesDefault": scmPrtInterpJobCopiesDefault,
       "scmPrtInterpLineTerm": scmPrtInterpLineTerm,
       "scmPrtInterpProcessBarcodes": scmPrtInterpProcessBarcodes,
       "scmPrtInterpOrientation": scmPrtInterpOrientation,
       "scmPrtInterpOrientationOptions": scmPrtInterpOrientationOptions,
       "scmPrtMediaPath": scmPrtMediaPath,
       "scmPrtMarker": scmPrtMarker,
       "scmPrtMarkerSimple": scmPrtMarkerSimple,
       "scmPrtMarkerMarginUnit": scmPrtMarkerMarginUnit,
       "scmPrtMarkerSrt": scmPrtMarkerSrt,
       "scmPrtMarkerSrtOptions": scmPrtMarkerSrtOptions,
       "scmPrtMarkerDensity": scmPrtMarkerDensity,
       "scmPrtMarkerDensityOptions": scmPrtMarkerDensityOptions,
       "scmPrtMarkerSmetMode": scmPrtMarkerSmetMode,
       "scmPrtMarkerSmetModeOptions": scmPrtMarkerSmetModeOptions,
       "scmPrtMarkerduplexTopMargin": scmPrtMarkerduplexTopMargin,
       "scmPrtMarkerduplexLeftMargin": scmPrtMarkerduplexLeftMargin,
       "scmPrtMarkerShortEdgeBindingMargin": scmPrtMarkerShortEdgeBindingMargin,
       "scmPrtMarkerLongEdgeBindingMargin": scmPrtMarkerLongEdgeBindingMargin,
       "scmPrtMarkerTonerSave": scmPrtMarkerTonerSave,
       "scmPrtMarkerTonerSaveOptions": scmPrtMarkerTonerSaveOptions,
       "scmPrtMarkerTonerOutAction": scmPrtMarkerTonerOutAction,
       "scmPrtMarkerTonerOutActionOptions": scmPrtMarkerTonerOutActionOptions,
       "scmPrtMarkerTable": scmPrtMarkerTable,
       "scmPrtMarkerEntry": scmPrtMarkerEntry,
       "scmPrtMarkerTonerIndex": scmPrtMarkerTonerIndex,
       "scmPrtMarkerResolution": scmPrtMarkerResolution,
       "scmPrtMarkerResolutionOptions": scmPrtMarkerResolutionOptions,
       "scmPrtMarkerTonerColor": scmPrtMarkerTonerColor,
       "scmPrtMarkerTonerColorDescription": scmPrtMarkerTonerColorDescription,
       "scmPrtMarkerTonerLevel": scmPrtMarkerTonerLevel,
       "scmPrtOperation": scmPrtOperation,
       "scmPrtOperationSimple": scmPrtOperationSimple,
       "scmPrtOperationJobCancel": scmPrtOperationJobCancel,
       "scmPrtOperarionMenuClear": scmPrtOperarionMenuClear,
       "scmPrtOperationMenuClearOptions": scmPrtOperationMenuClearOptions,
       "scmPrtOperationFuserClean": scmPrtOperationFuserClean,
       "scmPrtOperationFuserCleanOptions": scmPrtOperationFuserCleanOptions,
       "scmPrtOperationOpcClean": scmPrtOperationOpcClean,
       "scmPrtOperationOpcCleanOptions": scmPrtOperationOpcCleanOptions,
       "scmPrtOperationTestPrtRequest": scmPrtOperationTestPrtRequest,
       "scmPrtOperationPrintFontRequest": scmPrtOperationPrintFontRequest,
       "scmPrtOperationPrintBlackOnly": scmPrtOperationPrintBlackOnly,
       "scmPrtOperationTable": scmPrtOperationTable,
       "scmPrtOperationEntry": scmPrtOperationEntry,
       "scmPrtOperationIndex": scmPrtOperationIndex,
       "scmPrtConfiguration": scmPrtConfiguration,
       "scmPrtConfigurationSimple": scmPrtConfigurationSimple,
       "scmPrtConfigurationPowerSave": scmPrtConfigurationPowerSave,
       "scmPrtConfigurationPowerSaveOptions": scmPrtConfigurationPowerSaveOptions,
       "scmPrtConfigurationAutocont": scmPrtConfigurationAutocont,
       "scmPrtConfigurationAutoCountOptions": scmPrtConfigurationAutoCountOptions,
       "scmPrtConfigurationJam2Recover": scmPrtConfigurationJam2Recover,
       "scmPrtConfigurationJam2RecOptions": scmPrtConfigurationJam2RecOptions,
       "scmPrtConfigurationAltitudeAction": scmPrtConfigurationAltitudeAction,
       "scmPrtConfigurationAltitudeActionOptions": scmPrtConfigurationAltitudeActionOptions,
       "scmPrtConfigurationTable": scmPrtConfigurationTable,
       "scmPrtConfigurationEntry": scmPrtConfigurationEntry,
       "scmPrtConfigurationIndex": scmPrtConfigurationIndex,
       "scmPrtCount": scmPrtCount,
       "scmPrtCountSimple": scmPrtCountSimple,
       "scmPrtCountDrumImageCount": scmPrtCountDrumImageCount,
       "scmPrtCountDrumImageCountReset": scmPrtCountDrumImageCountReset,
       "scmPrtCountTransferImageCount": scmPrtCountTransferImageCount,
       "scmPrtCountTransferImageCountReset": scmPrtCountTransferImageCountReset,
       "scmPrtCountFuserImageCount": scmPrtCountFuserImageCount,
       "scmPrtCountFuserImageCountReset": scmPrtCountFuserImageCountReset,
       "scmPrtCountTwoRollerCount": scmPrtCountTwoRollerCount,
       "scmPrtCountTwoRollerReset": scmPrtCountTwoRollerReset,
       "scmPrtCountPickupMPCount": scmPrtCountPickupMPCount,
       "scmPrtCountPickupMPReset": scmPrtCountPickupMPReset,
       "scmPrtCountPickupTray1Count": scmPrtCountPickupTray1Count,
       "scmPrtCountPickupTray1Reset": scmPrtCountPickupTray1Reset,
       "scmPrtCountPickupTray2Count": scmPrtCountPickupTray2Count,
       "scmPrtCountPickupTray2Reset": scmPrtCountPickupTray2Reset,
       "scmPrtCountTable": scmPrtCountTable,
       "scmPrtCountEntry": scmPrtCountEntry,
       "scmPrtCountIndex": scmPrtCountIndex,
       "scmPrtCountDeviceType": scmPrtCountDeviceType,
       "scmPrtCountType": scmPrtCountType,
       "scmPrtCountMediaSize": scmPrtCountMediaSize,
       "scmPrtCountColorant": scmPrtCountColorant,
       "scmPrtCountDuplex": scmPrtCountDuplex,
       "scmPrtCountResolution": scmPrtCountResolution,
       "scmPrtCountUnit": scmPrtCountUnit,
       "scmPrtCountValue": scmPrtCountValue,
       "scmPrtSerial": scmPrtSerial,
       "scmPrtSerialSimple": scmPrtSerialSimple,
       "scmPrtSerialTable": scmPrtSerialTable,
       "scmPrtSerialEntry": scmPrtSerialEntry,
       "scmPrtSerialIndex": scmPrtSerialIndex,
       "scmPrtSerialNbaudRate": scmPrtSerialNbaudRate,
       "scmPrtSerialBrOptions": scmPrtSerialBrOptions,
       "scmPrtSerialBobuxon": scmPrtSerialBobuxon,
       "scmPrtSerialBobuxonOptions": scmPrtSerialBobuxonOptions,
       "scmPrtPCL": scmPrtPCL,
       "scmPrtPCLSimple": scmPrtPCLSimple,
       "scmPrtPCLFont": scmPrtPCLFont,
       "scmPrtPCLSymbolSet": scmPrtPCLSymbolSet,
       "scmPrtPCLFormLine": scmPrtPCLFormLine,
       "scmPrtPCLPitch": scmPrtPCLPitch,
       "scmPrtPCLPointSize": scmPrtPCLPointSize,
       "scmPrtPCLCourier": scmPrtPCLCourier,
       "scmPrtPCLCourierOptions": scmPrtPCLCourierOptions,
       "scmPrtPCLAppendCR": scmPrtPCLAppendCR,
       "scmPrtPCLAppendCROptions": scmPrtPCLAppendCROptions,
       "scmPrtPCLWideA4": scmPrtPCLWideA4,
       "scmPrtPCLWideA4Options": scmPrtPCLWideA4Options,
       "scmPrtPCLTopMargin": scmPrtPCLTopMargin,
       "scmPrtPCLLeftMargin": scmPrtPCLLeftMargin,
       "scmPrtPCLTable": scmPrtPCLTable,
       "scmPrtPCLEntry": scmPrtPCLEntry,
       "scmPrtPCLIndex": scmPrtPCLIndex,
       "scmPrtKS5843": scmPrtKS5843,
       "scmPrtKS5843Simple": scmPrtKS5843Simple,
       "scmPrtKS5843Font": scmPrtKS5843Font,
       "scmPrtKS5843FontOptions": scmPrtKS5843FontOptions,
       "scmPrtKS5843Code": scmPrtKS5843Code,
       "scmPrtKS5843CodeOptions": scmPrtKS5843CodeOptions,
       "scmPrtKS5843cpi": scmPrtKS5843cpi,
       "scmPrtKS5843cpiOptions": scmPrtKS5843cpiOptions,
       "scmPrtKS5843Lines": scmPrtKS5843Lines,
       "scmPrtKS5843Zoom": scmPrtKS5843Zoom,
       "scmPrtKS5843AutoWrap": scmPrtKS5843AutoWrap,
       "scmPrtKS5843AutoWrapOptions": scmPrtKS5843AutoWrapOptions,
       "scmPrtKS5843Topmargin": scmPrtKS5843Topmargin,
       "scmPrtKS5843Sitemode": scmPrtKS5843Sitemode,
       "scmPrtKSSM": scmPrtKSSM,
       "scmPrtKSSMSimple": scmPrtKSSMSimple,
       "scmPrtKSSMFont": scmPrtKSSMFont,
       "scmPrtKSSMFontOptions": scmPrtKSSMFontOptions,
       "scmPrtKSSMCode": scmPrtKSSMCode,
       "scmPrtKSSMCodeOptions": scmPrtKSSMCodeOptions,
       "scmPrtKSSMCPI": scmPrtKSSMCPI,
       "scmPrtKSSMCPIOptions": scmPrtKSSMCPIOptions,
       "scmPrtKSSMLines": scmPrtKSSMLines,
       "scmPrtKSSMZoom": scmPrtKSSMZoom,
       "scmPrtKSSMAutoWrap": scmPrtKSSMAutoWrap,
       "scmPrtKSSMAutoWrapOptions": scmPrtKSSMAutoWrapOptions,
       "scmPrtKSSMTopMargin": scmPrtKSSMTopMargin,
       "scmPrtKSSMSiteMode": scmPrtKSSMSiteMode,
       "scmPrtIPP": scmPrtIPP,
       "scmPrtIPPSimple": scmPrtIPPSimple,
       "scmPrtIPPColorSupported": scmPrtIPPColorSupported,
       "scmPrtIPPJobKOctetsSupportedLBound": scmPrtIPPJobKOctetsSupportedLBound,
       "scmPrtIPPJobKOctetsSupportedUBound": scmPrtIPPJobKOctetsSupportedUBound,
       "scmPrtIPPJobImpressionsSupportedLBound": scmPrtIPPJobImpressionsSupportedLBound,
       "scmPrtIPPJobImpressionsSupportedUBound": scmPrtIPPJobImpressionsSupportedUBound,
       "scmPrtIPPJobMediaSheetsSupportedLBound": scmPrtIPPJobMediaSheetsSupportedLBound,
       "scmPrtIPPJobMediaSheetsSupportedUBound": scmPrtIPPJobMediaSheetsSupportedUBound,
       "scmPrtIPPJobSheets": scmPrtIPPJobSheets,
       "scmPrtIPPCollatedCopiesLBound": scmPrtIPPCollatedCopiesLBound,
       "scmPrtIPPCollatedCopiesUBound": scmPrtIPPCollatedCopiesUBound,
       "scmPrtIPPCollatedCopies": scmPrtIPPCollatedCopies,
       "scmPrtIPPFinishingsSupported": scmPrtIPPFinishingsSupported,
       "scmPrtIPPFinishings": scmPrtIPPFinishings,
       "scmPrtIPPPageRangesSupported": scmPrtIPPPageRangesSupported,
       "scmPrtIPPNumberUp": scmPrtIPPNumberUp,
       "scmPrtIPPNumberUpOptions": scmPrtIPPNumberUpOptions,
       "scmPrtIPPPrintQuality": scmPrtIPPPrintQuality,
       "scmPrtIPPPrintQualityOptions": scmPrtIPPPrintQualityOptions,
       "scmPrtIPPJobKOctetsProcessed": scmPrtIPPJobKOctetsProcessed,
       "scmPrtIPPJobImpressionsCompleted": scmPrtIPPJobImpressionsCompleted,
       "scmPrtIPPJobMediaSheetsCompleted": scmPrtIPPJobMediaSheetsCompleted,
       "scmPrtAlert": scmPrtAlert,
       "scmPrtAlertSimple": scmPrtAlertSimple,
       "scmPrtAlertAlarmShortage": scmPrtAlertAlarmShortage,
       "scmPrtAlertAlarmShortageOptions": scmPrtAlertAlarmShortageOptions,
       "scmPrtConsoleDisplayBuffer": scmPrtConsoleDisplayBuffer,
       "scmPrtConsoleDisplayBufferSimple": scmPrtConsoleDisplayBufferSimple,
       "scmPrtConsoleDisplayBufferLcdLangType": scmPrtConsoleDisplayBufferLcdLangType,
       "scmPrtConsoleDisplayBufferLcdLangTypeOptions": scmPrtConsoleDisplayBufferLcdLangTypeOptions}
)
