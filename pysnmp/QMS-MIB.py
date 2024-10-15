# SNMP MIB module (QMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:54 2024
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

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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
    "NotificationType",
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

_QmsInc_ObjectIdentity = ObjectIdentity
qmsInc = _QmsInc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480)
)
_QmsUIH_ObjectIdentity = ObjectIdentity
qmsUIH = _QmsUIH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1)
)
_QmsSystem_ObjectIdentity = ObjectIdentity
qmsSystem = _QmsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 1)
)
_QmsSYSPageCount_Type = Integer32
_QmsSYSPageCount_Object = MibScalar
qmsSYSPageCount = _QmsSYSPageCount_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1001),
    _QmsSYSPageCount_Type()
)
qmsSYSPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSPageCount.setStatus("mandatory")
_QmsSYSSheetCount_Type = Integer32
_QmsSYSSheetCount_Object = MibScalar
qmsSYSSheetCount = _QmsSYSSheetCount_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1002),
    _QmsSYSSheetCount_Type()
)
qmsSYSSheetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSSheetCount.setStatus("mandatory")


class _QmsSYSPrinterModel_Type(DisplayString):
    """Custom type qmsSYSPrinterModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsSYSPrinterModel_Type.__name__ = "DisplayString"
_QmsSYSPrinterModel_Object = MibScalar
qmsSYSPrinterModel = _QmsSYSPrinterModel_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1003),
    _QmsSYSPrinterModel_Type()
)
qmsSYSPrinterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSPrinterModel.setStatus("mandatory")


class _QmsSYSPrinterVersion_Type(DisplayString):
    """Custom type qmsSYSPrinterVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsSYSPrinterVersion_Type.__name__ = "DisplayString"
_QmsSYSPrinterVersion_Object = MibScalar
qmsSYSPrinterVersion = _QmsSYSPrinterVersion_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1004),
    _QmsSYSPrinterVersion_Type()
)
qmsSYSPrinterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSPrinterVersion.setStatus("mandatory")


class _QmsSYSPrinterName_Type(DisplayString):
    """Custom type qmsSYSPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QmsSYSPrinterName_Type.__name__ = "DisplayString"
_QmsSYSPrinterName_Object = MibScalar
qmsSYSPrinterName = _QmsSYSPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1005),
    _QmsSYSPrinterName_Type()
)
qmsSYSPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSYSPrinterName.setStatus("mandatory")
_QmsSYSA3PageCount_Type = Integer32
_QmsSYSA3PageCount_Object = MibScalar
qmsSYSA3PageCount = _QmsSYSA3PageCount_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1006),
    _QmsSYSA3PageCount_Type()
)
qmsSYSA3PageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSA3PageCount.setStatus("mandatory")
_QmsSYSA3SheetCount_Type = Integer32
_QmsSYSA3SheetCount_Object = MibScalar
qmsSYSA3SheetCount = _QmsSYSA3SheetCount_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1007),
    _QmsSYSA3SheetCount_Type()
)
qmsSYSA3SheetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSA3SheetCount.setStatus("mandatory")


class _QmsSYSFPA_Type(Integer32):
    """Custom type qmsSYSFPA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsSYSFPA_Type.__name__ = "Integer32"
_QmsSYSFPA_Object = MibScalar
qmsSYSFPA = _QmsSYSFPA_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1008),
    _QmsSYSFPA_Type()
)
qmsSYSFPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSFPA.setStatus("mandatory")


class _QmsSYSSystemImage_Type(Integer32):
    """Custom type qmsSYSSystemImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diskSystem", 1),
          ("flashSystem", 2))
    )


_QmsSYSSystemImage_Type.__name__ = "Integer32"
_QmsSYSSystemImage_Object = MibScalar
qmsSYSSystemImage = _QmsSYSSystemImage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1009),
    _QmsSYSSystemImage_Type()
)
qmsSYSSystemImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSSystemImage.setStatus("mandatory")


class _QmsSYSDiskSwap_Type(Integer32):
    """Custom type qmsSYSDiskSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diskSwapingDisabled", 1),
          ("diskSwapingEnabled", 2))
    )


_QmsSYSDiskSwap_Type.__name__ = "Integer32"
_QmsSYSDiskSwap_Object = MibScalar
qmsSYSDiskSwap = _QmsSYSDiskSwap_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1010),
    _QmsSYSDiskSwap_Type()
)
qmsSYSDiskSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSDiskSwap.setStatus("mandatory")


class _QmsSYSMultiRes_Type(Integer32):
    """Custom type qmsSYSMultiRes based on Integer32"""
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
        *(("disabled", 4),
          ("lowMemory", 3),
          ("notPresent", 2),
          ("notSupported", 1),
          ("optional", 5),
          ("standard", 6))
    )


_QmsSYSMultiRes_Type.__name__ = "Integer32"
_QmsSYSMultiRes_Object = MibScalar
qmsSYSMultiRes = _QmsSYSMultiRes_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 1, 1011),
    _QmsSYSMultiRes_Type()
)
qmsSYSMultiRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSYSMultiRes.setStatus("mandatory")
_QmsMemory_ObjectIdentity = ObjectIdentity
qmsMemory = _QmsMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 5)
)
_QmsMEMPhysical_Type = Integer32
_QmsMEMPhysical_Object = MibScalar
qmsMEMPhysical = _QmsMEMPhysical_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 1),
    _QmsMEMPhysical_Type()
)
qmsMEMPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsMEMPhysical.setStatus("mandatory")
_QmsMEMTotal_Type = Integer32
_QmsMEMTotal_Object = MibScalar
qmsMEMTotal = _QmsMEMTotal_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 2),
    _QmsMEMTotal_Type()
)
qmsMEMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsMEMTotal.setStatus("mandatory")
_QmsClientSystem_Type = Integer32
_QmsClientSystem_Object = MibScalar
qmsClientSystem = _QmsClientSystem_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 3),
    _QmsClientSystem_Type()
)
qmsClientSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientSystem.setStatus("mandatory")
_QmsClientSpool_Type = Integer32
_QmsClientSpool_Object = MibScalar
qmsClientSpool = _QmsClientSpool_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 4),
    _QmsClientSpool_Type()
)
qmsClientSpool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientSpool.setStatus("mandatory")
_QmsClientEmulation_Type = Integer32
_QmsClientEmulation_Object = MibScalar
qmsClientEmulation = _QmsClientEmulation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 5),
    _QmsClientEmulation_Type()
)
qmsClientEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientEmulation.setStatus("mandatory")
_QmsClientHeap_Type = Integer32
_QmsClientHeap_Object = MibScalar
qmsClientHeap = _QmsClientHeap_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 6),
    _QmsClientHeap_Type()
)
qmsClientHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientHeap.setStatus("mandatory")
_QmsClientFontCache_Type = Integer32
_QmsClientFontCache_Object = MibScalar
qmsClientFontCache = _QmsClientFontCache_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 7),
    _QmsClientFontCache_Type()
)
qmsClientFontCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientFontCache.setStatus("mandatory")
_QmsClientDisplayList_Type = Integer32
_QmsClientDisplayList_Object = MibScalar
qmsClientDisplayList = _QmsClientDisplayList_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 8),
    _QmsClientDisplayList_Type()
)
qmsClientDisplayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientDisplayList.setStatus("mandatory")
_QmsClientFrameBuffer_Type = Integer32
_QmsClientFrameBuffer_Object = MibScalar
qmsClientFrameBuffer = _QmsClientFrameBuffer_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 9),
    _QmsClientFrameBuffer_Type()
)
qmsClientFrameBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientFrameBuffer.setStatus("mandatory")
_QmsClientEmulTemp_Type = Integer32
_QmsClientEmulTemp_Object = MibScalar
qmsClientEmulTemp = _QmsClientEmulTemp_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 10),
    _QmsClientEmulTemp_Type()
)
qmsClientEmulTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientEmulTemp.setStatus("mandatory")
_QmsClientDisk_Type = Integer32
_QmsClientDisk_Object = MibScalar
qmsClientDisk = _QmsClientDisk_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 11),
    _QmsClientDisk_Type()
)
qmsClientDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientDisk.setStatus("mandatory")
_QmsClientColorMatching_Type = Integer32
_QmsClientColorMatching_Object = MibScalar
qmsClientColorMatching = _QmsClientColorMatching_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 13),
    _QmsClientColorMatching_Type()
)
qmsClientColorMatching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientColorMatching.setStatus("mandatory")
_QmsClientHPStoragePool_Type = Integer32
_QmsClientHPStoragePool_Object = MibScalar
qmsClientHPStoragePool = _QmsClientHPStoragePool_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 5, 14),
    _QmsClientHPStoragePool_Type()
)
qmsClientHPStoragePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsClientHPStoragePool.setStatus("mandatory")
_QmsIoCtl_ObjectIdentity = ObjectIdentity
qmsIoCtl = _QmsIoCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 101)
)


class _QmsFEEspEmul_Type(Integer32):
    """Custom type qmsFEEspEmul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              13,
              15,
              19,
              20,
              22,
              23,
              25)
        )
    )
    namedValues = NamedValues(
        *(("cals", 23),
          ("ccitt", 19),
          ("cgm", 25),
          ("hpgl", 5),
          ("hppcl", 6),
          ("lineprinter", 20),
          ("ln03", 13),
          ("postscript", 1),
          ("quic2", 15),
          ("tiff", 22))
    )


_QmsFEEspEmul_Type.__name__ = "Integer32"
_QmsFEEspEmul_Object = MibScalar
qmsFEEspEmul = _QmsFEEspEmul_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 101, 7),
    _QmsFEEspEmul_Type()
)
qmsFEEspEmul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEEspEmul.setStatus("mandatory")


class _QmsFECopies_Type(Integer32):
    """Custom type qmsFECopies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_QmsFECopies_Type.__name__ = "Integer32"
_QmsFECopies_Object = MibScalar
qmsFECopies = _QmsFECopies_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 101, 17),
    _QmsFECopies_Type()
)
qmsFECopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFECopies.setStatus("mandatory")
_QmsHTTP_ObjectIdentity = ObjectIdentity
qmsHTTP = _QmsHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 102)
)


class _QmsHTTPContact_Type(DisplayString):
    """Custom type qmsHTTPContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QmsHTTPContact_Type.__name__ = "DisplayString"
_QmsHTTPContact_Object = MibScalar
qmsHTTPContact = _QmsHTTPContact_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 102, 1),
    _QmsHTTPContact_Type()
)
qmsHTTPContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHTTPContact.setStatus("mandatory")


class _QmsHTTPHelpURL_Type(DisplayString):
    """Custom type qmsHTTPHelpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QmsHTTPHelpURL_Type.__name__ = "DisplayString"
_QmsHTTPHelpURL_Object = MibScalar
qmsHTTPHelpURL = _QmsHTTPHelpURL_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 102, 2),
    _QmsHTTPHelpURL_Type()
)
qmsHTTPHelpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHTTPHelpURL.setStatus("mandatory")


class _QmsHTTPContactNumber_Type(DisplayString):
    """Custom type qmsHTTPContactNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QmsHTTPContactNumber_Type.__name__ = "DisplayString"
_QmsHTTPContactNumber_Object = MibScalar
qmsHTTPContactNumber = _QmsHTTPContactNumber_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 102, 3),
    _QmsHTTPContactNumber_Type()
)
qmsHTTPContactNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHTTPContactNumber.setStatus("mandatory")


class _QmsHTTPCorpURL_Type(DisplayString):
    """Custom type qmsHTTPCorpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QmsHTTPCorpURL_Type.__name__ = "DisplayString"
_QmsHTTPCorpURL_Object = MibScalar
qmsHTTPCorpURL = _QmsHTTPCorpURL_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 102, 4),
    _QmsHTTPCorpURL_Type()
)
qmsHTTPCorpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHTTPCorpURL.setStatus("mandatory")


class _QmsHTTPSuppliesNumber_Type(DisplayString):
    """Custom type qmsHTTPSuppliesNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QmsHTTPSuppliesNumber_Type.__name__ = "DisplayString"
_QmsHTTPSuppliesNumber_Object = MibScalar
qmsHTTPSuppliesNumber = _QmsHTTPSuppliesNumber_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 102, 5),
    _QmsHTTPSuppliesNumber_Type()
)
qmsHTTPSuppliesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHTTPSuppliesNumber.setStatus("mandatory")
_QmsIoTimeOuts_ObjectIdentity = ObjectIdentity
qmsIoTimeOuts = _QmsIoTimeOuts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 103)
)


class _QmsFETmPSWait_Type(Integer32):
    """Custom type qmsFETmPSWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsFETmPSWait_Type.__name__ = "Integer32"
_QmsFETmPSWait_Object = MibScalar
qmsFETmPSWait = _QmsFETmPSWait_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 103, 1),
    _QmsFETmPSWait_Type()
)
qmsFETmPSWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETmPSWait.setStatus("mandatory")


class _QmsFETmJob_Type(Integer32):
    """Custom type qmsFETmJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsFETmJob_Type.__name__ = "Integer32"
_QmsFETmJob_Object = MibScalar
qmsFETmJob = _QmsFETmJob_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 103, 2),
    _QmsFETmJob_Type()
)
qmsFETmJob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETmJob.setStatus("mandatory")


class _QmsFETmNonPSEmul_Type(Integer32):
    """Custom type qmsFETmNonPSEmul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsFETmNonPSEmul_Type.__name__ = "Integer32"
_QmsFETmNonPSEmul_Object = MibScalar
qmsFETmNonPSEmul = _QmsFETmNonPSEmul_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 103, 3),
    _QmsFETmNonPSEmul_Type()
)
qmsFETmNonPSEmul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETmNonPSEmul.setStatus("mandatory")


class _QmsFETmEsp_Type(Integer32):
    """Custom type qmsFETmEsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsFETmEsp_Type.__name__ = "Integer32"
_QmsFETmEsp_Object = MibScalar
qmsFETmEsp = _QmsFETmEsp_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 103, 4),
    _QmsFETmEsp_Type()
)
qmsFETmEsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETmEsp.setStatus("mandatory")
_QmsIoPages_ObjectIdentity = ObjectIdentity
qmsIoPages = _QmsIoPages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 104)
)


class _QmsFEDoStartPage_Type(Integer32):
    """Custom type qmsFEDoStartPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsFEDoStartPage_Type.__name__ = "Integer32"
_QmsFEDoStartPage_Object = MibScalar
qmsFEDoStartPage = _QmsFEDoStartPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 5),
    _QmsFEDoStartPage_Type()
)
qmsFEDoStartPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEDoStartPage.setStatus("mandatory")


class _QmsFEHeaderPage_Type(Integer32):
    """Custom type qmsFEHeaderPage based on Integer32"""
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


_QmsFEHeaderPage_Type.__name__ = "Integer32"
_QmsFEHeaderPage_Object = MibScalar
qmsFEHeaderPage = _QmsFEHeaderPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 8),
    _QmsFEHeaderPage_Type()
)
qmsFEHeaderPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEHeaderPage.setStatus("mandatory")
_QmsFEHeaderInputbin_Type = Integer32
_QmsFEHeaderInputbin_Object = MibScalar
qmsFEHeaderInputbin = _QmsFEHeaderInputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 9),
    _QmsFEHeaderInputbin_Type()
)
qmsFEHeaderInputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEHeaderInputbin.setStatus("mandatory")


class _QmsFETrailerPage_Type(Integer32):
    """Custom type qmsFETrailerPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("errorOnly", 3),
          ("off", 1),
          ("on", 4),
          ("onError", 5))
    )


_QmsFETrailerPage_Type.__name__ = "Integer32"
_QmsFETrailerPage_Object = MibScalar
qmsFETrailerPage = _QmsFETrailerPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 10),
    _QmsFETrailerPage_Type()
)
qmsFETrailerPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETrailerPage.setStatus("mandatory")
_QmsFETrailerInputbin_Type = Integer32
_QmsFETrailerInputbin_Object = MibScalar
qmsFETrailerInputbin = _QmsFETrailerInputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 11),
    _QmsFETrailerInputbin_Type()
)
qmsFETrailerInputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFETrailerInputbin.setStatus("mandatory")


class _QmsFEDoSysStart_Type(Integer32):
    """Custom type qmsFEDoSysStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsFEDoSysStart_Type.__name__ = "Integer32"
_QmsFEDoSysStart_Object = MibScalar
qmsFEDoSysStart = _QmsFEDoSysStart_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 12),
    _QmsFEDoSysStart_Type()
)
qmsFEDoSysStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEDoSysStart.setStatus("mandatory")


class _QmsFEStatusPageType_Type(Integer32):
    """Custom type qmsFEStatusPageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("standard", 1))
    )


_QmsFEStatusPageType_Type.__name__ = "Integer32"
_QmsFEStatusPageType_Object = MibScalar
qmsFEStatusPageType = _QmsFEStatusPageType_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 104, 15),
    _QmsFEStatusPageType_Type()
)
qmsFEStatusPageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsFEStatusPageType.setStatus("mandatory")
_QmsSerial_ObjectIdentity = ObjectIdentity
qmsSerial = _QmsSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 160)
)


class _QmsSerPSProtocol_Type(Integer32):
    """Custom type qmsSerPSProtocol based on Integer32"""
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
        *(("binary", 3),
          ("binaryfixed", 4),
          ("normal", 1),
          ("normalfixed", 2))
    )


_QmsSerPSProtocol_Type.__name__ = "Integer32"
_QmsSerPSProtocol_Object = MibScalar
qmsSerPSProtocol = _QmsSerPSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 100),
    _QmsSerPSProtocol_Type()
)
qmsSerPSProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerPSProtocol.setStatus("mandatory")


class _QmsSerMode_Type(Integer32):
    """Custom type qmsSerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("interactive", 3),
          ("noninteractive", 4))
    )


_QmsSerMode_Type.__name__ = "Integer32"
_QmsSerMode_Object = MibScalar
qmsSerMode = _QmsSerMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 101),
    _QmsSerMode_Type()
)
qmsSerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerMode.setStatus("mandatory")


class _QmsSerEmulation_Type(Integer32):
    """Custom type qmsSerEmulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              13,
              15,
              19,
              20,
              22,
              23,
              25,
              201)
        )
    )
    namedValues = NamedValues(
        *(("cals", 23),
          ("ccitt", 19),
          ("cgm", 25),
          ("esp", 201),
          ("hexdump", 7),
          ("hpgl", 5),
          ("hppcl", 6),
          ("lineprinter", 20),
          ("ln03", 13),
          ("postscript", 1),
          ("quic2", 15),
          ("tiff", 22))
    )


_QmsSerEmulation_Type.__name__ = "Integer32"
_QmsSerEmulation_Object = MibScalar
qmsSerEmulation = _QmsSerEmulation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 102),
    _QmsSerEmulation_Type()
)
qmsSerEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerEmulation.setStatus("mandatory")


class _QmsSerPriority_Type(Integer32):
    """Custom type qmsSerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QmsSerPriority_Type.__name__ = "Integer32"
_QmsSerPriority_Object = MibScalar
qmsSerPriority = _QmsSerPriority_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 103),
    _QmsSerPriority_Type()
)
qmsSerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerPriority.setStatus("mandatory")
_QmsSerBufferSize_Type = Integer32
_QmsSerBufferSize_Object = MibScalar
qmsSerBufferSize = _QmsSerBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 104),
    _QmsSerBufferSize_Type()
)
qmsSerBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsSerBufferSize.setStatus("mandatory")


class _QmsSerEndDocumentMode_Type(Integer32):
    """Custom type qmsSerEndDocumentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hpeod", 3),
          ("none", 1),
          ("qmseod", 2))
    )


_QmsSerEndDocumentMode_Type.__name__ = "Integer32"
_QmsSerEndDocumentMode_Object = MibScalar
qmsSerEndDocumentMode = _QmsSerEndDocumentMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 111),
    _QmsSerEndDocumentMode_Type()
)
qmsSerEndDocumentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerEndDocumentMode.setStatus("mandatory")


class _QmsSerSpoolTimeout_Type(Integer32):
    """Custom type qmsSerSpoolTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsSerSpoolTimeout_Type.__name__ = "Integer32"
_QmsSerSpoolTimeout_Object = MibScalar
qmsSerSpoolTimeout = _QmsSerSpoolTimeout_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 112),
    _QmsSerSpoolTimeout_Type()
)
qmsSerSpoolTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerSpoolTimeout.setStatus("mandatory")


class _QmsSerBaudRate_Type(Integer32):
    """Custom type qmsSerBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(301,
              601,
              1201,
              2401,
              4801,
              9601,
              19201,
              38401)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 1201),
          ("bps19200", 19201),
          ("bps2400", 2401),
          ("bps300", 301),
          ("bps38400", 38401),
          ("bps4800", 4801),
          ("bps600", 601),
          ("bps9600", 9601))
    )


_QmsSerBaudRate_Type.__name__ = "Integer32"
_QmsSerBaudRate_Object = MibScalar
qmsSerBaudRate = _QmsSerBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 201),
    _QmsSerBaudRate_Type()
)
qmsSerBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerBaudRate.setStatus("mandatory")


class _QmsSerParity_Type(Integer32):
    """Custom type qmsSerParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("even", 5),
          ("none", 1),
          ("odd", 4))
    )


_QmsSerParity_Type.__name__ = "Integer32"
_QmsSerParity_Object = MibScalar
qmsSerParity = _QmsSerParity_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 202),
    _QmsSerParity_Type()
)
qmsSerParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerParity.setStatus("mandatory")


class _QmsSerIgnoreParity_Type(Integer32):
    """Custom type qmsSerIgnoreParity based on Integer32"""
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


_QmsSerIgnoreParity_Type.__name__ = "Integer32"
_QmsSerIgnoreParity_Object = MibScalar
qmsSerIgnoreParity = _QmsSerIgnoreParity_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 203),
    _QmsSerIgnoreParity_Type()
)
qmsSerIgnoreParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerIgnoreParity.setStatus("mandatory")


class _QmsSerRxSWFlow_Type(Integer32):
    """Custom type qmsSerRxSWFlow based on Integer32"""
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
        *(("etxack", 3),
          ("none", 1),
          ("robustxonxoff", 4),
          ("xonxoff", 2))
    )


_QmsSerRxSWFlow_Type.__name__ = "Integer32"
_QmsSerRxSWFlow_Object = MibScalar
qmsSerRxSWFlow = _QmsSerRxSWFlow_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 204),
    _QmsSerRxSWFlow_Type()
)
qmsSerRxSWFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerRxSWFlow.setStatus("mandatory")


class _QmsSerTxSWFlow_Type(Integer32):
    """Custom type qmsSerTxSWFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etxack", 3),
          ("none", 1),
          ("xonxoff", 2))
    )


_QmsSerTxSWFlow_Type.__name__ = "Integer32"
_QmsSerTxSWFlow_Object = MibScalar
qmsSerTxSWFlow = _QmsSerTxSWFlow_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 205),
    _QmsSerTxSWFlow_Type()
)
qmsSerTxSWFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerTxSWFlow.setStatus("mandatory")


class _QmsSerDataBits_Type(Integer32):
    """Custom type qmsSerDataBits based on Integer32"""
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
        *(("bits5", 4),
          ("bits6", 3),
          ("bits7", 2),
          ("bits8", 1))
    )


_QmsSerDataBits_Type.__name__ = "Integer32"
_QmsSerDataBits_Object = MibScalar
qmsSerDataBits = _QmsSerDataBits_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 206),
    _QmsSerDataBits_Type()
)
qmsSerDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerDataBits.setStatus("mandatory")


class _QmsSerStopBits_Type(Integer32):
    """Custom type qmsSerStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneandhalf", 3),
          ("onebit", 1),
          ("twobits", 2))
    )


_QmsSerStopBits_Type.__name__ = "Integer32"
_QmsSerStopBits_Object = MibScalar
qmsSerStopBits = _QmsSerStopBits_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 207),
    _QmsSerStopBits_Type()
)
qmsSerStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerStopBits.setStatus("mandatory")


class _QmsSerHwCTS_Type(Integer32):
    """Custom type qmsSerHwCTS based on Integer32"""
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


_QmsSerHwCTS_Type.__name__ = "Integer32"
_QmsSerHwCTS_Object = MibScalar
qmsSerHwCTS = _QmsSerHwCTS_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 208),
    _QmsSerHwCTS_Type()
)
qmsSerHwCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwCTS.setStatus("mandatory")


class _QmsSerHwRTS_Type(Integer32):
    """Custom type qmsSerHwRTS based on Integer32"""
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


_QmsSerHwRTS_Type.__name__ = "Integer32"
_QmsSerHwRTS_Object = MibScalar
qmsSerHwRTS = _QmsSerHwRTS_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 209),
    _QmsSerHwRTS_Type()
)
qmsSerHwRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwRTS.setStatus("mandatory")


class _QmsSerHwDTR_Type(Integer32):
    """Custom type qmsSerHwDTR based on Integer32"""
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


_QmsSerHwDTR_Type.__name__ = "Integer32"
_QmsSerHwDTR_Object = MibScalar
qmsSerHwDTR = _QmsSerHwDTR_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 210),
    _QmsSerHwDTR_Type()
)
qmsSerHwDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwDTR.setStatus("mandatory")


class _QmsSerHwDTRPOL_Type(Integer32):
    """Custom type qmsSerHwDTRPOL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reverse", 1))
    )


_QmsSerHwDTRPOL_Type.__name__ = "Integer32"
_QmsSerHwDTRPOL_Object = MibScalar
qmsSerHwDTRPOL = _QmsSerHwDTRPOL_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 211),
    _QmsSerHwDTRPOL_Type()
)
qmsSerHwDTRPOL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwDTRPOL.setStatus("mandatory")


class _QmsSerHwDSR_Type(Integer32):
    """Custom type qmsSerHwDSR based on Integer32"""
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


_QmsSerHwDSR_Type.__name__ = "Integer32"
_QmsSerHwDSR_Object = MibScalar
qmsSerHwDSR = _QmsSerHwDSR_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 212),
    _QmsSerHwDSR_Type()
)
qmsSerHwDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwDSR.setStatus("mandatory")


class _QmsSerHwDSRPOL_Type(Integer32):
    """Custom type qmsSerHwDSRPOL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reverse", 1))
    )


_QmsSerHwDSRPOL_Type.__name__ = "Integer32"
_QmsSerHwDSRPOL_Object = MibScalar
qmsSerHwDSRPOL = _QmsSerHwDSRPOL_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 160, 213),
    _QmsSerHwDSRPOL_Type()
)
qmsSerHwDSRPOL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSerHwDSRPOL.setStatus("mandatory")
_QmsParallel_ObjectIdentity = ObjectIdentity
qmsParallel = _QmsParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 161)
)


class _QmsParPSProtocol_Type(Integer32):
    """Custom type qmsParPSProtocol based on Integer32"""
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
        *(("binary", 3),
          ("binaryfixed", 4),
          ("normal", 1),
          ("normalfixed", 2))
    )


_QmsParPSProtocol_Type.__name__ = "Integer32"
_QmsParPSProtocol_Object = MibScalar
qmsParPSProtocol = _QmsParPSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 100),
    _QmsParPSProtocol_Type()
)
qmsParPSProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParPSProtocol.setStatus("mandatory")


class _QmsParMode_Type(Integer32):
    """Custom type qmsParMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("interactive", 3),
          ("noninteractive", 4))
    )


_QmsParMode_Type.__name__ = "Integer32"
_QmsParMode_Object = MibScalar
qmsParMode = _QmsParMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 101),
    _QmsParMode_Type()
)
qmsParMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParMode.setStatus("mandatory")


class _QmsParEmulation_Type(Integer32):
    """Custom type qmsParEmulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              13,
              15,
              19,
              20,
              22,
              23,
              25,
              201)
        )
    )
    namedValues = NamedValues(
        *(("cals", 23),
          ("ccitt", 19),
          ("cgm", 25),
          ("esp", 201),
          ("hexdump", 7),
          ("hpgl", 5),
          ("hppcl", 6),
          ("lineprinter", 20),
          ("ln03", 13),
          ("postscript", 1),
          ("quic2", 15),
          ("tiff", 22))
    )


_QmsParEmulation_Type.__name__ = "Integer32"
_QmsParEmulation_Object = MibScalar
qmsParEmulation = _QmsParEmulation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 102),
    _QmsParEmulation_Type()
)
qmsParEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParEmulation.setStatus("mandatory")


class _QmsParPriority_Type(Integer32):
    """Custom type qmsParPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QmsParPriority_Type.__name__ = "Integer32"
_QmsParPriority_Object = MibScalar
qmsParPriority = _QmsParPriority_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 103),
    _QmsParPriority_Type()
)
qmsParPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParPriority.setStatus("mandatory")
_QmsParBufferSize_Type = Integer32
_QmsParBufferSize_Object = MibScalar
qmsParBufferSize = _QmsParBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 104),
    _QmsParBufferSize_Type()
)
qmsParBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsParBufferSize.setStatus("mandatory")


class _QmsParSpoolTimeout_Type(Integer32):
    """Custom type qmsParSpoolTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsParSpoolTimeout_Type.__name__ = "Integer32"
_QmsParSpoolTimeout_Object = MibScalar
qmsParSpoolTimeout = _QmsParSpoolTimeout_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 111),
    _QmsParSpoolTimeout_Type()
)
qmsParSpoolTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParSpoolTimeout.setStatus("mandatory")


class _QmsParEndDocumentMode_Type(Integer32):
    """Custom type qmsParEndDocumentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hpeod", 3),
          ("none", 1),
          ("qmseod", 2))
    )


_QmsParEndDocumentMode_Type.__name__ = "Integer32"
_QmsParEndDocumentMode_Object = MibScalar
qmsParEndDocumentMode = _QmsParEndDocumentMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 112),
    _QmsParEndDocumentMode_Type()
)
qmsParEndDocumentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParEndDocumentMode.setStatus("mandatory")


class _QmsParDataBits_Type(Integer32):
    """Custom type qmsParDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits7", 2),
          ("bits8", 1))
    )


_QmsParDataBits_Type.__name__ = "Integer32"
_QmsParDataBits_Object = MibScalar
qmsParDataBits = _QmsParDataBits_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 161, 113),
    _QmsParDataBits_Type()
)
qmsParDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsParDataBits.setStatus("mandatory")
_QmsEngine_ObjectIdentity = ObjectIdentity
qmsEngine = _QmsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 304)
)


class _QmsENGTopOffset_Type(Integer32):
    """Custom type qmsENGTopOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_QmsENGTopOffset_Type.__name__ = "Integer32"
_QmsENGTopOffset_Object = MibScalar
qmsENGTopOffset = _QmsENGTopOffset_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1),
    _QmsENGTopOffset_Type()
)
qmsENGTopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGTopOffset.setStatus("mandatory")


class _QmsENGLeftOffset_Type(Integer32):
    """Custom type qmsENGLeftOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_QmsENGLeftOffset_Type.__name__ = "Integer32"
_QmsENGLeftOffset_Object = MibScalar
qmsENGLeftOffset = _QmsENGLeftOffset_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 2),
    _QmsENGLeftOffset_Type()
)
qmsENGLeftOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGLeftOffset.setStatus("mandatory")


class _QmsENGTopOffsetDuplex_Type(Integer32):
    """Custom type qmsENGTopOffsetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_QmsENGTopOffsetDuplex_Type.__name__ = "Integer32"
_QmsENGTopOffsetDuplex_Object = MibScalar
qmsENGTopOffsetDuplex = _QmsENGTopOffsetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 4),
    _QmsENGTopOffsetDuplex_Type()
)
qmsENGTopOffsetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGTopOffsetDuplex.setStatus("mandatory")


class _QmsENGLeftOffsetDuplex_Type(Integer32):
    """Custom type qmsENGLeftOffsetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_QmsENGLeftOffsetDuplex_Type.__name__ = "Integer32"
_QmsENGLeftOffsetDuplex_Object = MibScalar
qmsENGLeftOffsetDuplex = _QmsENGLeftOffsetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 6),
    _QmsENGLeftOffsetDuplex_Type()
)
qmsENGLeftOffsetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGLeftOffsetDuplex.setStatus("mandatory")


class _QmsENGResolution_Type(Integer32):
    """Custom type qmsENGResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(301,
              601,
              1201,
              2401)
        )
    )
    namedValues = NamedValues(
        *(("dpi1200", 1201),
          ("dpi2401", 2401),
          ("dpi300", 301),
          ("dpi600", 601))
    )


_QmsENGResolution_Type.__name__ = "Integer32"
_QmsENGResolution_Object = MibScalar
qmsENGResolution = _QmsENGResolution_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 8),
    _QmsENGResolution_Type()
)
qmsENGResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGResolution.setStatus("mandatory")


class _QmsENGDefaultPaper_Type(Integer32):
    """Custom type qmsENGDefaultPaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a4", 2),
          ("letter", 1))
    )


_QmsENGDefaultPaper_Type.__name__ = "Integer32"
_QmsENGDefaultPaper_Object = MibScalar
qmsENGDefaultPaper = _QmsENGDefaultPaper_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 11),
    _QmsENGDefaultPaper_Type()
)
qmsENGDefaultPaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGDefaultPaper.setStatus("mandatory")


class _QmsENGDuplex_Type(Integer32):
    """Custom type qmsENGDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("longedge", 2),
          ("off", 1),
          ("shortedge", 3))
    )


_QmsENGDuplex_Type.__name__ = "Integer32"
_QmsENGDuplex_Object = MibScalar
qmsENGDuplex = _QmsENGDuplex_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 12),
    _QmsENGDuplex_Type()
)
qmsENGDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGDuplex.setStatus("mandatory")


class _QmsENGOrientation_Type(Integer32):
    """Custom type qmsENGOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 2),
          ("portrait", 1))
    )


_QmsENGOrientation_Type.__name__ = "Integer32"
_QmsENGOrientation_Object = MibScalar
qmsENGOrientation = _QmsENGOrientation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 14),
    _QmsENGOrientation_Type()
)
qmsENGOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGOrientation.setStatus("mandatory")
_QmsENGInputbin_Type = Integer32
_QmsENGInputbin_Object = MibScalar
qmsENGInputbin = _QmsENGInputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 15),
    _QmsENGInputbin_Type()
)
qmsENGInputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGInputbin.setStatus("mandatory")
_QmsENGOutputbin_Type = Integer32
_QmsENGOutputbin_Object = MibScalar
qmsENGOutputbin = _QmsENGOutputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 16),
    _QmsENGOutputbin_Type()
)
qmsENGOutputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGOutputbin.setStatus("mandatory")


class _QmsENGCollation_Type(Integer32):
    """Custom type qmsENGCollation based on Integer32"""
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


_QmsENGCollation_Type.__name__ = "Integer32"
_QmsENGCollation_Object = MibScalar
qmsENGCollation = _QmsENGCollation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 17),
    _QmsENGCollation_Type()
)
qmsENGCollation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGCollation.setStatus("mandatory")


class _QmsENGErrorRecovery_Type(Integer32):
    """Custom type qmsENGErrorRecovery based on Integer32"""
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


_QmsENGErrorRecovery_Type.__name__ = "Integer32"
_QmsENGErrorRecovery_Object = MibScalar
qmsENGErrorRecovery = _QmsENGErrorRecovery_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 19),
    _QmsENGErrorRecovery_Type()
)
qmsENGErrorRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGErrorRecovery.setStatus("mandatory")


class _QmsENGManualTrayMedia_Type(Integer32):
    """Custom type qmsENGManualTrayMedia based on Integer32"""
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
        *(("a3", 5),
          ("a4", 6),
          ("a5", 7),
          ("b4", 8),
          ("b5", 9),
          ("c5", 15),
          ("com10", 12),
          ("dl", 13),
          ("envelope", 16),
          ("executive", 3),
          ("legal", 2),
          ("letter", 1),
          ("monarch", 14),
          ("statement", 10),
          ("sz11x17", 4),
          ("universal", 11))
    )


_QmsENGManualTrayMedia_Type.__name__ = "Integer32"
_QmsENGManualTrayMedia_Object = MibScalar
qmsENGManualTrayMedia = _QmsENGManualTrayMedia_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 20),
    _QmsENGManualTrayMedia_Type()
)
qmsENGManualTrayMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGManualTrayMedia.setStatus("mandatory")


class _QmsENGToneroutAction_Type(Integer32):
    """Custom type qmsENGToneroutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("stop", 1))
    )


_QmsENGToneroutAction_Type.__name__ = "Integer32"
_QmsENGToneroutAction_Object = MibScalar
qmsENGToneroutAction = _QmsENGToneroutAction_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 21),
    _QmsENGToneroutAction_Type()
)
qmsENGToneroutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGToneroutAction.setStatus("mandatory")


class _QmsENGLetterheadMode_Type(Integer32):
    """Custom type qmsENGLetterheadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplexPath", 2),
          ("off", 1),
          ("rotateSimplex", 3))
    )


_QmsENGLetterheadMode_Type.__name__ = "Integer32"
_QmsENGLetterheadMode_Object = MibScalar
qmsENGLetterheadMode = _QmsENGLetterheadMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 23),
    _QmsENGLetterheadMode_Type()
)
qmsENGLetterheadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGLetterheadMode.setStatus("mandatory")


class _QmsENGManualFeedTimeout_Type(Integer32):
    """Custom type qmsENGManualFeedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_QmsENGManualFeedTimeout_Type.__name__ = "Integer32"
_QmsENGManualFeedTimeout_Object = MibScalar
qmsENGManualFeedTimeout = _QmsENGManualFeedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 24),
    _QmsENGManualFeedTimeout_Type()
)
qmsENGManualFeedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGManualFeedTimeout.setStatus("mandatory")


class _QmsENGOffsetStacking_Type(Integer32):
    """Custom type qmsENGOffsetStacking based on Integer32"""
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


_QmsENGOffsetStacking_Type.__name__ = "Integer32"
_QmsENGOffsetStacking_Object = MibScalar
qmsENGOffsetStacking = _QmsENGOffsetStacking_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 26),
    _QmsENGOffsetStacking_Type()
)
qmsENGOffsetStacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGOffsetStacking.setStatus("mandatory")


class _QmsENGEnergyStar_Type(Integer32):
    """Custom type qmsENGEnergyStar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              31,
              61,
              121,
              181)
        )
    )
    namedValues = NamedValues(
        *(("hour1", 61),
          ("hour2", 121),
          ("hour3", 181),
          ("min15", 16),
          ("min30", 31),
          ("off", 1))
    )


_QmsENGEnergyStar_Type.__name__ = "Integer32"
_QmsENGEnergyStar_Object = MibScalar
qmsENGEnergyStar = _QmsENGEnergyStar_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 27),
    _QmsENGEnergyStar_Type()
)
qmsENGEnergyStar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGEnergyStar.setStatus("mandatory")


class _QmsENGPageOrder_Type(Integer32):
    """Custom type qmsENGPageOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reverse", 1))
    )


_QmsENGPageOrder_Type.__name__ = "Integer32"
_QmsENGPageOrder_Object = MibScalar
qmsENGPageOrder = _QmsENGPageOrder_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 40),
    _QmsENGPageOrder_Type()
)
qmsENGPageOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGPageOrder.setStatus("mandatory")


class _QmsENGEnvelopeTrayMedia_Type(Integer32):
    """Custom type qmsENGEnvelopeTrayMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("c5", 15),
          ("com10", 12),
          ("dl", 13),
          ("envelope", 16),
          ("monarch", 14))
    )


_QmsENGEnvelopeTrayMedia_Type.__name__ = "Integer32"
_QmsENGEnvelopeTrayMedia_Object = MibScalar
qmsENGEnvelopeTrayMedia = _QmsENGEnvelopeTrayMedia_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 41),
    _QmsENGEnvelopeTrayMedia_Type()
)
qmsENGEnvelopeTrayMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGEnvelopeTrayMedia.setStatus("mandatory")
_QmsENGDensity_Type = Integer32
_QmsENGDensity_Object = MibScalar
qmsENGDensity = _QmsENGDensity_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 42),
    _QmsENGDensity_Type()
)
qmsENGDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGDensity.setStatus("mandatory")


class _QmsENGColorModel_Type(Integer32):
    """Custom type qmsENGColorModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cmy", 3),
          ("cmyk", 5),
          ("gray", 2),
          ("rgb", 4))
    )


_QmsENGColorModel_Type.__name__ = "Integer32"
_QmsENGColorModel_Object = MibScalar
qmsENGColorModel = _QmsENGColorModel_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 43),
    _QmsENGColorModel_Type()
)
qmsENGColorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGColorModel.setStatus("mandatory")


class _QmsENGColorSeparation_Type(Integer32):
    """Custom type qmsENGColorSeparation based on Integer32"""
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


_QmsENGColorSeparation_Type.__name__ = "Integer32"
_QmsENGColorSeparation_Object = MibScalar
qmsENGColorSeparation = _QmsENGColorSeparation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 44),
    _QmsENGColorSeparation_Type()
)
qmsENGColorSeparation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGColorSeparation.setStatus("mandatory")


class _QmsENGUnderColor_Type(Integer32):
    """Custom type qmsENGUnderColor based on Integer32"""
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


_QmsENGUnderColor_Type.__name__ = "Integer32"
_QmsENGUnderColor_Object = MibScalar
qmsENGUnderColor = _QmsENGUnderColor_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 45),
    _QmsENGUnderColor_Type()
)
qmsENGUnderColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGUnderColor.setStatus("mandatory")


class _QmsENGQuality_Type(Integer32):
    """Custom type qmsENGQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("conserveToner", 2),
          ("fineMode", 5),
          ("normal", 1),
          ("smooth600dpi", 3))
    )


_QmsENGQuality_Type.__name__ = "Integer32"
_QmsENGQuality_Object = MibScalar
qmsENGQuality = _QmsENGQuality_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 48),
    _QmsENGQuality_Type()
)
qmsENGQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGQuality.setStatus("mandatory")
_QmsENGConsumeNameMulti_Object = MibTable
qmsENGConsumeNameMulti = _QmsENGConsumeNameMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1000)
)
if mibBuilder.loadTexts:
    qmsENGConsumeNameMulti.setStatus("mandatory")


class _QmsENGConsumeName_Type(DisplayString):
    """Custom type qmsENGConsumeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsENGConsumeName_Type.__name__ = "DisplayString"
_QmsENGConsumeName_Object = MibTableColumn
qmsENGConsumeName = _QmsENGConsumeName_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1000, 1),
    _QmsENGConsumeName_Type()
)
qmsENGConsumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeName.setStatus("mandatory")
_QmsENGConsumeLevelMulti_Object = MibTable
qmsENGConsumeLevelMulti = _QmsENGConsumeLevelMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1001)
)
if mibBuilder.loadTexts:
    qmsENGConsumeLevelMulti.setStatus("mandatory")
_QmsENGConsumeLevel_Type = Integer32
_QmsENGConsumeLevel_Object = MibTableColumn
qmsENGConsumeLevel = _QmsENGConsumeLevel_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1001, 1),
    _QmsENGConsumeLevel_Type()
)
qmsENGConsumeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeLevel.setStatus("mandatory")
_QmsENGConsumeMaxMulti_Object = MibTable
qmsENGConsumeMaxMulti = _QmsENGConsumeMaxMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1002)
)
if mibBuilder.loadTexts:
    qmsENGConsumeMaxMulti.setStatus("mandatory")
_QmsENGConsumeMax_Type = Integer32
_QmsENGConsumeMax_Object = MibTableColumn
qmsENGConsumeMax = _QmsENGConsumeMax_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1002, 1),
    _QmsENGConsumeMax_Type()
)
qmsENGConsumeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeMax.setStatus("mandatory")
_QmsENGConsumeUnitsMulti_Object = MibTable
qmsENGConsumeUnitsMulti = _QmsENGConsumeUnitsMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1003)
)
if mibBuilder.loadTexts:
    qmsENGConsumeUnitsMulti.setStatus("mandatory")


class _QmsENGConsumeUnits_Type(DisplayString):
    """Custom type qmsENGConsumeUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsENGConsumeUnits_Type.__name__ = "DisplayString"
_QmsENGConsumeUnits_Object = MibTableColumn
qmsENGConsumeUnits = _QmsENGConsumeUnits_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1003, 1),
    _QmsENGConsumeUnits_Type()
)
qmsENGConsumeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeUnits.setStatus("mandatory")
_QmsENGConsumeTypeMulti_Object = MibTable
qmsENGConsumeTypeMulti = _QmsENGConsumeTypeMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1004)
)
if mibBuilder.loadTexts:
    qmsENGConsumeTypeMulti.setStatus("mandatory")


class _QmsENGConsumeType_Type(Integer32):
    """Custom type qmsENGConsumeType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fuserCRoller", 8),
          ("fuserOil", 9),
          ("fuserUnit", 7),
          ("inputBin", 2),
          ("invalid", 1),
          ("opc", 6),
          ("outputBin", 3),
          ("pmService", 10),
          ("toner", 4),
          ("wasteToner", 5))
    )


_QmsENGConsumeType_Type.__name__ = "Integer32"
_QmsENGConsumeType_Object = MibTableColumn
qmsENGConsumeType = _QmsENGConsumeType_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1004, 1),
    _QmsENGConsumeType_Type()
)
qmsENGConsumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeType.setStatus("mandatory")
_QmsENGConsumeNote1Multi_Object = MibTable
qmsENGConsumeNote1Multi = _QmsENGConsumeNote1Multi_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1005)
)
if mibBuilder.loadTexts:
    qmsENGConsumeNote1Multi.setStatus("mandatory")


class _QmsENGConsumeNote1_Type(DisplayString):
    """Custom type qmsENGConsumeNote1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsENGConsumeNote1_Type.__name__ = "DisplayString"
_QmsENGConsumeNote1_Object = MibTableColumn
qmsENGConsumeNote1 = _QmsENGConsumeNote1_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1005, 1),
    _QmsENGConsumeNote1_Type()
)
qmsENGConsumeNote1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeNote1.setStatus("mandatory")
_QmsENGConsumeNote2Multi_Object = MibTable
qmsENGConsumeNote2Multi = _QmsENGConsumeNote2Multi_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1006)
)
if mibBuilder.loadTexts:
    qmsENGConsumeNote2Multi.setStatus("mandatory")


class _QmsENGConsumeNote2_Type(DisplayString):
    """Custom type qmsENGConsumeNote2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_QmsENGConsumeNote2_Type.__name__ = "DisplayString"
_QmsENGConsumeNote2_Object = MibTableColumn
qmsENGConsumeNote2 = _QmsENGConsumeNote2_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1006, 1),
    _QmsENGConsumeNote2_Type()
)
qmsENGConsumeNote2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeNote2.setStatus("mandatory")
_QmsENGConsumeIndexMulti_Object = MibTable
qmsENGConsumeIndexMulti = _QmsENGConsumeIndexMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1007)
)
if mibBuilder.loadTexts:
    qmsENGConsumeIndexMulti.setStatus("mandatory")
_QmsENGConsumeIndex_Type = Integer32
_QmsENGConsumeIndex_Object = MibTableColumn
qmsENGConsumeIndex = _QmsENGConsumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1007, 1),
    _QmsENGConsumeIndex_Type()
)
qmsENGConsumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGConsumeIndex.setStatus("mandatory")
_QmsENGNumConsumables_Type = Integer32
_QmsENGNumConsumables_Object = MibScalar
qmsENGNumConsumables = _QmsENGNumConsumables_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1010),
    _QmsENGNumConsumables_Type()
)
qmsENGNumConsumables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGNumConsumables.setStatus("mandatory")


class _QmsENGChainInputBins_Type(Integer32):
    """Custom type qmsENGChainInputBins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("onAny", 3))
    )


_QmsENGChainInputBins_Type.__name__ = "Integer32"
_QmsENGChainInputBins_Object = MibScalar
qmsENGChainInputBins = _QmsENGChainInputBins_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1011),
    _QmsENGChainInputBins_Type()
)
qmsENGChainInputBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGChainInputBins.setStatus("mandatory")
_QmsENGChainOutputbinMulti_Object = MibTable
qmsENGChainOutputbinMulti = _QmsENGChainOutputbinMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1012)
)
if mibBuilder.loadTexts:
    qmsENGChainOutputbinMulti.setStatus("mandatory")


class _QmsENGChainOutputbin_Type(Integer32):
    """Custom type qmsENGChainOutputbin based on Integer32"""
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


_QmsENGChainOutputbin_Type.__name__ = "Integer32"
_QmsENGChainOutputbin_Object = MibTableColumn
qmsENGChainOutputbin = _QmsENGChainOutputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1012, 1),
    _QmsENGChainOutputbin_Type()
)
qmsENGChainOutputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGChainOutputbin.setStatus("mandatory")
_QmsENGInputbinMediatypeMulti_Object = MibTable
qmsENGInputbinMediatypeMulti = _QmsENGInputbinMediatypeMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1013)
)
if mibBuilder.loadTexts:
    qmsENGInputbinMediatypeMulti.setStatus("mandatory")


class _QmsENGInputbinMediatype_Type(Integer32):
    """Custom type qmsENGInputbinMediatype based on Integer32"""
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
        *(("automatic", 13),
          ("bond", 8),
          ("cardStock", 11),
          ("color", 10),
          ("labels", 7),
          ("letterhead", 5),
          ("plainPaper", 1),
          ("prePrinted", 4),
          ("prePunched", 6),
          ("recycled", 9),
          ("thermal", 3),
          ("thickStock", 14),
          ("thinStock", 12),
          ("transparency", 2))
    )


_QmsENGInputbinMediatype_Type.__name__ = "Integer32"
_QmsENGInputbinMediatype_Object = MibTableColumn
qmsENGInputbinMediatype = _QmsENGInputbinMediatype_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1013, 1),
    _QmsENGInputbinMediatype_Type()
)
qmsENGInputbinMediatype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsENGInputbinMediatype.setStatus("mandatory")
_QmsENGChainInputbinMulti_Object = MibTable
qmsENGChainInputbinMulti = _QmsENGChainInputbinMulti_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1014)
)
if mibBuilder.loadTexts:
    qmsENGChainInputbinMulti.setStatus("mandatory")


class _QmsENGChainInputbin_Type(Integer32):
    """Custom type qmsENGChainInputbin based on Integer32"""
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


_QmsENGChainInputbin_Type.__name__ = "Integer32"
_QmsENGChainInputbin_Object = MibTableColumn
qmsENGChainInputbin = _QmsENGChainInputbin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1014, 1),
    _QmsENGChainInputbin_Type()
)
qmsENGChainInputbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGChainInputbin.setStatus("mandatory")


class _QmsENGStaplePosition_Type(Integer32):
    """Custom type qmsENGStaplePosition based on Integer32"""
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
        *(("backCorner", 3),
          ("center", 4),
          ("frontCorner", 2),
          ("off", 1),
          ("offsetStacking", 5))
    )


_QmsENGStaplePosition_Type.__name__ = "Integer32"
_QmsENGStaplePosition_Object = MibScalar
qmsENGStaplePosition = _QmsENGStaplePosition_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 304, 1015),
    _QmsENGStaplePosition_Type()
)
qmsENGStaplePosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsENGStaplePosition.setStatus("mandatory")
_QmsAccounting_ObjectIdentity = ObjectIdentity
qmsAccounting = _QmsAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 401)
)


class _QmsACCMode_Type(Integer32):
    """Custom type qmsACCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QmsACCMode_Type.__name__ = "Integer32"
_QmsACCMode_Object = MibScalar
qmsACCMode = _QmsACCMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 401, 1),
    _QmsACCMode_Type()
)
qmsACCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsACCMode.setStatus("mandatory")
_QmsACCDiskSpace_Type = Integer32
_QmsACCDiskSpace_Object = MibScalar
qmsACCDiskSpace = _QmsACCDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 401, 2),
    _QmsACCDiskSpace_Type()
)
qmsACCDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsACCDiskSpace.setStatus("mandatory")


class _QmsACCFileSegment_Type(Integer32):
    """Custom type qmsACCFileSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 3),
          ("single", 2))
    )


_QmsACCFileSegment_Type.__name__ = "Integer32"
_QmsACCFileSegment_Object = MibScalar
qmsACCFileSegment = _QmsACCFileSegment_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 401, 3),
    _QmsACCFileSegment_Type()
)
qmsACCFileSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsACCFileSegment.setStatus("mandatory")
_QmsScanner_ObjectIdentity = ObjectIdentity
qmsScanner = _QmsScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 402)
)
_QmsSCColorAdjust_Type = Integer32
_QmsSCColorAdjust_Object = MibScalar
qmsSCColorAdjust = _QmsSCColorAdjust_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 3),
    _QmsSCColorAdjust_Type()
)
qmsSCColorAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCColorAdjust.setStatus("mandatory")


class _QmsSCScanResolution_Type(Integer32):
    """Custom type qmsSCScanResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              151,
              201,
              301)
        )
    )
    namedValues = NamedValues(
        *(("dpi100", 101),
          ("dpi150", 151),
          ("dpi200", 201),
          ("dpi300", 301))
    )


_QmsSCScanResolution_Type.__name__ = "Integer32"
_QmsSCScanResolution_Object = MibScalar
qmsSCScanResolution = _QmsSCScanResolution_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 4),
    _QmsSCScanResolution_Type()
)
qmsSCScanResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCScanResolution.setStatus("mandatory")


class _QmsSCSizeHorizontal_Type(Integer32):
    """Custom type qmsSCSizeHorizontal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 850),
    )


_QmsSCSizeHorizontal_Type.__name__ = "Integer32"
_QmsSCSizeHorizontal_Object = MibScalar
qmsSCSizeHorizontal = _QmsSCSizeHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 8),
    _QmsSCSizeHorizontal_Type()
)
qmsSCSizeHorizontal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCSizeHorizontal.setStatus("mandatory")


class _QmsSCSizeVertical_Type(Integer32):
    """Custom type qmsSCSizeVertical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1400),
    )


_QmsSCSizeVertical_Type.__name__ = "Integer32"
_QmsSCSizeVertical_Object = MibScalar
qmsSCSizeVertical = _QmsSCSizeVertical_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 12),
    _QmsSCSizeVertical_Type()
)
qmsSCSizeVertical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCSizeVertical.setStatus("mandatory")


class _QmsSCOffsetHorizontal_Type(Integer32):
    """Custom type qmsSCOffsetHorizontal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 850),
    )


_QmsSCOffsetHorizontal_Type.__name__ = "Integer32"
_QmsSCOffsetHorizontal_Object = MibScalar
qmsSCOffsetHorizontal = _QmsSCOffsetHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 16),
    _QmsSCOffsetHorizontal_Type()
)
qmsSCOffsetHorizontal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCOffsetHorizontal.setStatus("mandatory")


class _QmsSCOffsetVertical_Type(Integer32):
    """Custom type qmsSCOffsetVertical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1100),
    )


_QmsSCOffsetVertical_Type.__name__ = "Integer32"
_QmsSCOffsetVertical_Object = MibScalar
qmsSCOffsetVertical = _QmsSCOffsetVertical_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 20),
    _QmsSCOffsetVertical_Type()
)
qmsSCOffsetVertical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCOffsetVertical.setStatus("mandatory")


class _QmsSCCopyMode_Type(Integer32):
    """Custom type qmsSCCopyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
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
        *(("automaticColor", 8),
          ("automaticGray", 4),
          ("binaryBandW", 6),
          ("binaryColor", 10),
          ("customColor", 9),
          ("customGray", 5),
          ("halftoneBandW", 7),
          ("halftoneColor", 11))
    )


_QmsSCCopyMode_Type.__name__ = "Integer32"
_QmsSCCopyMode_Object = MibScalar
qmsSCCopyMode = _QmsSCCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 24),
    _QmsSCCopyMode_Type()
)
qmsSCCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCCopyMode.setStatus("mandatory")
_QmsSCRedGammaFunction_Type = Integer32
_QmsSCRedGammaFunction_Object = MibScalar
qmsSCRedGammaFunction = _QmsSCRedGammaFunction_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 26),
    _QmsSCRedGammaFunction_Type()
)
qmsSCRedGammaFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCRedGammaFunction.setStatus("mandatory")
_QmsSCGreenGammaFunction_Type = Integer32
_QmsSCGreenGammaFunction_Object = MibScalar
qmsSCGreenGammaFunction = _QmsSCGreenGammaFunction_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 27),
    _QmsSCGreenGammaFunction_Type()
)
qmsSCGreenGammaFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCGreenGammaFunction.setStatus("mandatory")
_QmsSCBlueGammaFunction_Type = Integer32
_QmsSCBlueGammaFunction_Object = MibScalar
qmsSCBlueGammaFunction = _QmsSCBlueGammaFunction_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 28),
    _QmsSCBlueGammaFunction_Type()
)
qmsSCBlueGammaFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCBlueGammaFunction.setStatus("mandatory")


class _QmsSCGrayGammaFunction_Type(Integer32):
    """Custom type qmsSCGrayGammaFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("photoGraphic", 2),
          ("reverseImage", 3))
    )


_QmsSCGrayGammaFunction_Type.__name__ = "Integer32"
_QmsSCGrayGammaFunction_Object = MibScalar
qmsSCGrayGammaFunction = _QmsSCGrayGammaFunction_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 29),
    _QmsSCGrayGammaFunction_Type()
)
qmsSCGrayGammaFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCGrayGammaFunction.setStatus("mandatory")
_QmsSCBinaryAdjustment_Type = Integer32
_QmsSCBinaryAdjustment_Object = MibScalar
qmsSCBinaryAdjustment = _QmsSCBinaryAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 31),
    _QmsSCBinaryAdjustment_Type()
)
qmsSCBinaryAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCBinaryAdjustment.setStatus("mandatory")


class _QmsSCTrans_Type(Integer32):
    """Custom type qmsSCTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QmsSCTrans_Type.__name__ = "Integer32"
_QmsSCTrans_Object = MibScalar
qmsSCTrans = _QmsSCTrans_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 35),
    _QmsSCTrans_Type()
)
qmsSCTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCTrans.setStatus("mandatory")
_QmsSCContrast_Type = Integer32
_QmsSCContrast_Object = MibScalar
qmsSCContrast = _QmsSCContrast_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 402, 36),
    _QmsSCContrast_Type()
)
qmsSCContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsSCContrast.setStatus("mandatory")
_QmsCostPerPage_ObjectIdentity = ObjectIdentity
qmsCostPerPage = _QmsCostPerPage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 403)
)


class _QmsCPPSerialNumber_Type(DisplayString):
    """Custom type qmsCPPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QmsCPPSerialNumber_Type.__name__ = "DisplayString"
_QmsCPPSerialNumber_Object = MibScalar
qmsCPPSerialNumber = _QmsCPPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 403, 2),
    _QmsCPPSerialNumber_Type()
)
qmsCPPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsCPPSerialNumber.setStatus("mandatory")
_QmsColorMatch_ObjectIdentity = ObjectIdentity
qmsColorMatch = _QmsColorMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 404)
)


class _QmsCMMICCColorMatch_Type(Integer32):
    """Custom type qmsCMMICCColorMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QmsCMMICCColorMatch_Type.__name__ = "Integer32"
_QmsCMMICCColorMatch_Object = MibScalar
qmsCMMICCColorMatch = _QmsCMMICCColorMatch_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1),
    _QmsCMMICCColorMatch_Type()
)
qmsCMMICCColorMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMICCColorMatch.setStatus("mandatory")
_QmsCMMICCRGBSource_Type = Integer32
_QmsCMMICCRGBSource_Object = MibScalar
qmsCMMICCRGBSource = _QmsCMMICCRGBSource_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 2),
    _QmsCMMICCRGBSource_Type()
)
qmsCMMICCRGBSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMICCRGBSource.setStatus("mandatory")
_QmsCMMICCSimulation_Type = Integer32
_QmsCMMICCSimulation_Object = MibScalar
qmsCMMICCSimulation = _QmsCMMICCSimulation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 4),
    _QmsCMMICCSimulation_Type()
)
qmsCMMICCSimulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMICCSimulation.setStatus("mandatory")
_QmsCMMICCDestination_Type = Integer32
_QmsCMMICCDestination_Object = MibScalar
qmsCMMICCDestination = _QmsCMMICCDestination_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 6),
    _QmsCMMICCDestination_Type()
)
qmsCMMICCDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMICCDestination.setStatus("mandatory")


class _QmsCMMLinkQuality_Type(Integer32):
    """Custom type qmsCMMLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_QmsCMMLinkQuality_Type.__name__ = "Integer32"
_QmsCMMLinkQuality_Object = MibScalar
qmsCMMLinkQuality = _QmsCMMLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 8),
    _QmsCMMLinkQuality_Type()
)
qmsCMMLinkQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMLinkQuality.setStatus("mandatory")


class _QmsCMMSimInRGBLinks_Type(Integer32):
    """Custom type qmsCMMSimInRGBLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsCMMSimInRGBLinks_Type.__name__ = "Integer32"
_QmsCMMSimInRGBLinks_Object = MibScalar
qmsCMMSimInRGBLinks = _QmsCMMSimInRGBLinks_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 10),
    _QmsCMMSimInRGBLinks_Type()
)
qmsCMMSimInRGBLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMSimInRGBLinks.setStatus("mandatory")


class _QmsCMMICCHP_Type(Integer32):
    """Custom type qmsCMMICCHP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("srgb", 2))
    )


_QmsCMMICCHP_Type.__name__ = "Integer32"
_QmsCMMICCHP_Object = MibScalar
qmsCMMICCHP = _QmsCMMICCHP_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 12),
    _QmsCMMICCHP_Type()
)
qmsCMMICCHP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCMMICCHP.setStatus("mandatory")
_QmsCMMProfileTable_Object = MibTable
qmsCMMProfileTable = _QmsCMMProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1000)
)
if mibBuilder.loadTexts:
    qmsCMMProfileTable.setStatus("mandatory")
_QmsCMMProfileEntry_Object = MibTableRow
qmsCMMProfileEntry = _QmsCMMProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1000, 1)
)
qmsCMMProfileEntry.setIndexNames(
    (0, "QMS-MIB", "qmsCMMProfileIndex"),
)
if mibBuilder.loadTexts:
    qmsCMMProfileEntry.setStatus("mandatory")
_QmsCMMProfileIndex_Type = Integer32
_QmsCMMProfileIndex_Object = MibTableColumn
qmsCMMProfileIndex = _QmsCMMProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1000, 1, 1000),
    _QmsCMMProfileIndex_Type()
)
qmsCMMProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsCMMProfileIndex.setStatus("mandatory")


class _QmsCMMProfileDescription_Type(DisplayString):
    """Custom type qmsCMMProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QmsCMMProfileDescription_Type.__name__ = "DisplayString"
_QmsCMMProfileDescription_Object = MibTableColumn
qmsCMMProfileDescription = _QmsCMMProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1000, 1, 1001),
    _QmsCMMProfileDescription_Type()
)
qmsCMMProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsCMMProfileDescription.setStatus("mandatory")


class _QmsCMMProfileType_Type(Integer32):
    """Custom type qmsCMMProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("simulation", 3),
          ("source", 1))
    )


_QmsCMMProfileType_Type.__name__ = "Integer32"
_QmsCMMProfileType_Object = MibTableColumn
qmsCMMProfileType = _QmsCMMProfileType_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 404, 1000, 1, 1002),
    _QmsCMMProfileType_Type()
)
qmsCMMProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsCMMProfileType.setStatus("mandatory")
_QmsPS_ObjectIdentity = ObjectIdentity
qmsPS = _QmsPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 520)
)


class _QmsPSErrorHandler_Type(Integer32):
    """Custom type qmsPSErrorHandler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsPSErrorHandler_Type.__name__ = "Integer32"
_QmsPSErrorHandler_Object = MibScalar
qmsPSErrorHandler = _QmsPSErrorHandler_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 5),
    _QmsPSErrorHandler_Type()
)
qmsPSErrorHandler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsPSErrorHandler.setStatus("mandatory")


class _QmsPSOutputPositioning_Type(Integer32):
    """Custom type qmsPSOutputPositioning based on Integer32"""
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


_QmsPSOutputPositioning_Type.__name__ = "Integer32"
_QmsPSOutputPositioning_Object = MibScalar
qmsPSOutputPositioning = _QmsPSOutputPositioning_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 6),
    _QmsPSOutputPositioning_Type()
)
qmsPSOutputPositioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPSOutputPositioning.setStatus("mandatory")


class _QmsPSDefaultHalftone_Type(Integer32):
    """Custom type qmsPSDefaultHalftone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 3),
          ("basic", 1),
          ("standard", 2))
    )


_QmsPSDefaultHalftone_Type.__name__ = "Integer32"
_QmsPSDefaultHalftone_Object = MibScalar
qmsPSDefaultHalftone = _QmsPSDefaultHalftone_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 138),
    _QmsPSDefaultHalftone_Type()
)
qmsPSDefaultHalftone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsPSDefaultHalftone.setStatus("mandatory")


class _QmsPSDefaultBlackOverPrint_Type(Integer32):
    """Custom type qmsPSDefaultBlackOverPrint based on Integer32"""
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


_QmsPSDefaultBlackOverPrint_Type.__name__ = "Integer32"
_QmsPSDefaultBlackOverPrint_Object = MibScalar
qmsPSDefaultBlackOverPrint = _QmsPSDefaultBlackOverPrint_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 139),
    _QmsPSDefaultBlackOverPrint_Type()
)
qmsPSDefaultBlackOverPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPSDefaultBlackOverPrint.setStatus("mandatory")


class _QmsPSDefaultCRD_Type(Integer32):
    """Custom type qmsPSDefaultCRD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QmsPSDefaultCRD_Type.__name__ = "Integer32"
_QmsPSDefaultCRD_Object = MibScalar
qmsPSDefaultCRD = _QmsPSDefaultCRD_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 140),
    _QmsPSDefaultCRD_Type()
)
qmsPSDefaultCRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPSDefaultCRD.setStatus("mandatory")


class _QmsPSDefaultDither_Type(Integer32):
    """Custom type qmsPSDefaultDither based on Integer32"""
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


_QmsPSDefaultDither_Type.__name__ = "Integer32"
_QmsPSDefaultDither_Object = MibScalar
qmsPSDefaultDither = _QmsPSDefaultDither_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 141),
    _QmsPSDefaultDither_Type()
)
qmsPSDefaultDither.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPSDefaultDither.setStatus("mandatory")


class _QmsPSDefaultGamma_Type(Integer32):
    """Custom type qmsPSDefaultGamma based on Integer32"""
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


_QmsPSDefaultGamma_Type.__name__ = "Integer32"
_QmsPSDefaultGamma_Object = MibScalar
qmsPSDefaultGamma = _QmsPSDefaultGamma_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 152),
    _QmsPSDefaultGamma_Type()
)
qmsPSDefaultGamma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsPSDefaultGamma.setStatus("mandatory")


class _QmsPSIntensity_Type(Integer32):
    """Custom type qmsPSIntensity based on Integer32"""
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
        *(("darker", 2),
          ("darkest", 1),
          ("lighter", 4),
          ("lightest", 5),
          ("normal", 3))
    )


_QmsPSIntensity_Type.__name__ = "Integer32"
_QmsPSIntensity_Object = MibScalar
qmsPSIntensity = _QmsPSIntensity_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 520, 154),
    _QmsPSIntensity_Type()
)
qmsPSIntensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsPSIntensity.setStatus("mandatory")
_QmsHPGL_ObjectIdentity = ObjectIdentity
qmsHPGL = _QmsHPGL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 524)
)


class _QmsHPGLPaperType_Type(Integer32):
    """Custom type qmsHPGLPaperType based on Integer32"""
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
        *(("a", 1),
          ("a0", 13),
          ("a1", 12),
          ("a2", 11),
          ("a3", 4),
          ("a4", 2),
          ("b", 3),
          ("c", 5),
          ("cArch", 8),
          ("d", 6),
          ("dArch", 9),
          ("e", 7),
          ("eArch", 10),
          ("scaleToPaper", 14))
    )


_QmsHPGLPaperType_Type.__name__ = "Integer32"
_QmsHPGLPaperType_Object = MibScalar
qmsHPGLPaperType = _QmsHPGLPaperType_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 2),
    _QmsHPGLPaperType_Type()
)
qmsHPGLPaperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPaperType.setStatus("mandatory")


class _QmsHPGLPlotter_Type(Integer32):
    """Custom type qmsHPGLPlotter based on Integer32"""
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
        *(("colorpro", 3),
          ("draftmaster", 5),
          ("plotter7470A", 2),
          ("plotter7475A", 1),
          ("plotter7550A", 4))
    )


_QmsHPGLPlotter_Type.__name__ = "Integer32"
_QmsHPGLPlotter_Object = MibScalar
qmsHPGLPlotter = _QmsHPGLPlotter_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 12),
    _QmsHPGLPlotter_Type()
)
qmsHPGLPlotter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPlotter.setStatus("mandatory")


class _QmsHPGLScalingPercent_Type(Integer32):
    """Custom type qmsHPGLScalingPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_QmsHPGLScalingPercent_Type.__name__ = "Integer32"
_QmsHPGLScalingPercent_Object = MibScalar
qmsHPGLScalingPercent = _QmsHPGLScalingPercent_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 13),
    _QmsHPGLScalingPercent_Type()
)
qmsHPGLScalingPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLScalingPercent.setStatus("mandatory")


class _QmsHPGLEnhancedMode_Type(Integer32):
    """Custom type qmsHPGLEnhancedMode based on Integer32"""
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


_QmsHPGLEnhancedMode_Type.__name__ = "Integer32"
_QmsHPGLEnhancedMode_Object = MibScalar
qmsHPGLEnhancedMode = _QmsHPGLEnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 14),
    _QmsHPGLEnhancedMode_Type()
)
qmsHPGLEnhancedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLEnhancedMode.setStatus("mandatory")


class _QmsHPGLExpandMode_Type(Integer32):
    """Custom type qmsHPGLExpandMode based on Integer32"""
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


_QmsHPGLExpandMode_Type.__name__ = "Integer32"
_QmsHPGLExpandMode_Object = MibScalar
qmsHPGLExpandMode = _QmsHPGLExpandMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 15),
    _QmsHPGLExpandMode_Type()
)
qmsHPGLExpandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLExpandMode.setStatus("mandatory")


class _QmsHPGLPenWidth1_Type(Integer32):
    """Custom type qmsHPGLPenWidth1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth1_Type.__name__ = "Integer32"
_QmsHPGLPenWidth1_Object = MibScalar
qmsHPGLPenWidth1 = _QmsHPGLPenWidth1_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 16),
    _QmsHPGLPenWidth1_Type()
)
qmsHPGLPenWidth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth1.setStatus("mandatory")


class _QmsHPGLPenWidth2_Type(Integer32):
    """Custom type qmsHPGLPenWidth2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth2_Type.__name__ = "Integer32"
_QmsHPGLPenWidth2_Object = MibScalar
qmsHPGLPenWidth2 = _QmsHPGLPenWidth2_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 17),
    _QmsHPGLPenWidth2_Type()
)
qmsHPGLPenWidth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth2.setStatus("mandatory")


class _QmsHPGLPenWidth3_Type(Integer32):
    """Custom type qmsHPGLPenWidth3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth3_Type.__name__ = "Integer32"
_QmsHPGLPenWidth3_Object = MibScalar
qmsHPGLPenWidth3 = _QmsHPGLPenWidth3_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 18),
    _QmsHPGLPenWidth3_Type()
)
qmsHPGLPenWidth3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth3.setStatus("mandatory")


class _QmsHPGLPenWidth4_Type(Integer32):
    """Custom type qmsHPGLPenWidth4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth4_Type.__name__ = "Integer32"
_QmsHPGLPenWidth4_Object = MibScalar
qmsHPGLPenWidth4 = _QmsHPGLPenWidth4_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 19),
    _QmsHPGLPenWidth4_Type()
)
qmsHPGLPenWidth4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth4.setStatus("mandatory")


class _QmsHPGLPenWidth5_Type(Integer32):
    """Custom type qmsHPGLPenWidth5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth5_Type.__name__ = "Integer32"
_QmsHPGLPenWidth5_Object = MibScalar
qmsHPGLPenWidth5 = _QmsHPGLPenWidth5_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 20),
    _QmsHPGLPenWidth5_Type()
)
qmsHPGLPenWidth5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth5.setStatus("mandatory")


class _QmsHPGLPenWidth6_Type(Integer32):
    """Custom type qmsHPGLPenWidth6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth6_Type.__name__ = "Integer32"
_QmsHPGLPenWidth6_Object = MibScalar
qmsHPGLPenWidth6 = _QmsHPGLPenWidth6_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 21),
    _QmsHPGLPenWidth6_Type()
)
qmsHPGLPenWidth6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth6.setStatus("mandatory")


class _QmsHPGLPenWidth7_Type(Integer32):
    """Custom type qmsHPGLPenWidth7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth7_Type.__name__ = "Integer32"
_QmsHPGLPenWidth7_Object = MibScalar
qmsHPGLPenWidth7 = _QmsHPGLPenWidth7_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 22),
    _QmsHPGLPenWidth7_Type()
)
qmsHPGLPenWidth7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth7.setStatus("mandatory")


class _QmsHPGLPenWidth8_Type(Integer32):
    """Custom type qmsHPGLPenWidth8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QmsHPGLPenWidth8_Type.__name__ = "Integer32"
_QmsHPGLPenWidth8_Object = MibScalar
qmsHPGLPenWidth8 = _QmsHPGLPenWidth8_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 23),
    _QmsHPGLPenWidth8_Type()
)
qmsHPGLPenWidth8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenWidth8.setStatus("mandatory")


class _QmsHPGLPenColor1_Type(Integer32):
    """Custom type qmsHPGLPenColor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor1_Type.__name__ = "Integer32"
_QmsHPGLPenColor1_Object = MibScalar
qmsHPGLPenColor1 = _QmsHPGLPenColor1_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 24),
    _QmsHPGLPenColor1_Type()
)
qmsHPGLPenColor1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor1.setStatus("mandatory")


class _QmsHPGLPenColor2_Type(Integer32):
    """Custom type qmsHPGLPenColor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor2_Type.__name__ = "Integer32"
_QmsHPGLPenColor2_Object = MibScalar
qmsHPGLPenColor2 = _QmsHPGLPenColor2_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 25),
    _QmsHPGLPenColor2_Type()
)
qmsHPGLPenColor2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor2.setStatus("mandatory")


class _QmsHPGLPenColor3_Type(Integer32):
    """Custom type qmsHPGLPenColor3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor3_Type.__name__ = "Integer32"
_QmsHPGLPenColor3_Object = MibScalar
qmsHPGLPenColor3 = _QmsHPGLPenColor3_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 26),
    _QmsHPGLPenColor3_Type()
)
qmsHPGLPenColor3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor3.setStatus("mandatory")


class _QmsHPGLPenColor4_Type(Integer32):
    """Custom type qmsHPGLPenColor4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor4_Type.__name__ = "Integer32"
_QmsHPGLPenColor4_Object = MibScalar
qmsHPGLPenColor4 = _QmsHPGLPenColor4_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 27),
    _QmsHPGLPenColor4_Type()
)
qmsHPGLPenColor4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor4.setStatus("mandatory")


class _QmsHPGLPenColor5_Type(Integer32):
    """Custom type qmsHPGLPenColor5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor5_Type.__name__ = "Integer32"
_QmsHPGLPenColor5_Object = MibScalar
qmsHPGLPenColor5 = _QmsHPGLPenColor5_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 28),
    _QmsHPGLPenColor5_Type()
)
qmsHPGLPenColor5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor5.setStatus("mandatory")


class _QmsHPGLPenColor6_Type(Integer32):
    """Custom type qmsHPGLPenColor6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor6_Type.__name__ = "Integer32"
_QmsHPGLPenColor6_Object = MibScalar
qmsHPGLPenColor6 = _QmsHPGLPenColor6_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 29),
    _QmsHPGLPenColor6_Type()
)
qmsHPGLPenColor6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor6.setStatus("mandatory")


class _QmsHPGLPenColor7_Type(Integer32):
    """Custom type qmsHPGLPenColor7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor7_Type.__name__ = "Integer32"
_QmsHPGLPenColor7_Object = MibScalar
qmsHPGLPenColor7 = _QmsHPGLPenColor7_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 30),
    _QmsHPGLPenColor7_Type()
)
qmsHPGLPenColor7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor7.setStatus("mandatory")


class _QmsHPGLPenColor8_Type(Integer32):
    """Custom type qmsHPGLPenColor8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("black", 9),
          ("blue", 6),
          ("brown", 11),
          ("cyan", 7),
          ("gray25Percent", 12),
          ("gray50Percent", 13),
          ("gray75Percent", 14),
          ("green", 5),
          ("magenta", 8),
          ("orange", 3),
          ("red", 2),
          ("violet", 10),
          ("yellow", 4))
    )


_QmsHPGLPenColor8_Type.__name__ = "Integer32"
_QmsHPGLPenColor8_Object = MibScalar
qmsHPGLPenColor8 = _QmsHPGLPenColor8_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 524, 31),
    _QmsHPGLPenColor8_Type()
)
qmsHPGLPenColor8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPGLPenColor8.setStatus("mandatory")
_QmsHPPCL_ObjectIdentity = ObjectIdentity
qmsHPPCL = _QmsHPPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 525)
)


class _QmsHPPCLLineTermination_Type(Integer32):
    """Custom type qmsHPPCLLineTermination based on Integer32"""
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
        *(("crEQcr-lfEQcrANDlf", 3),
          ("crEQcr-lfEQlf", 1),
          ("crEQcrANDlf-lfEQlf", 2),
          ("crORlfEQcrANDlf", 4))
    )


_QmsHPPCLLineTermination_Type.__name__ = "Integer32"
_QmsHPPCLLineTermination_Object = MibScalar
qmsHPPCLLineTermination = _QmsHPPCLLineTermination_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 2),
    _QmsHPPCLLineTermination_Type()
)
qmsHPPCLLineTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLLineTermination.setStatus("mandatory")


class _QmsHPPCLFontNumber_Type(Integer32):
    """Custom type qmsHPPCLFontNumber based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("courier10", 4),
          ("courier10Bold", 5),
          ("courier10Italic", 6),
          ("courier12", 1),
          ("courier12Bold", 2),
          ("courier12Italic", 3),
          ("lineprinter", 7),
          ("selectByIndex", 20),
          ("times", 8),
          ("timesBldItalic", 11),
          ("timesBold", 10),
          ("timesItalic", 9),
          ("univ", 12),
          ("univBold", 14),
          ("univBoldItalic", 15),
          ("univItalic", 13),
          ("univcond", 16),
          ("univcondBldItlc", 19),
          ("univcondBold", 18),
          ("univcondItalic", 17))
    )


_QmsHPPCLFontNumber_Type.__name__ = "Integer32"
_QmsHPPCLFontNumber_Object = MibScalar
qmsHPPCLFontNumber = _QmsHPPCLFontNumber_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 4),
    _QmsHPPCLFontNumber_Type()
)
qmsHPPCLFontNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLFontNumber.setStatus("mandatory")


class _QmsHPPCLLinesPerInch_Type(Integer32):
    """Custom type qmsHPPCLLinesPerInch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4800),
    )


_QmsHPPCLLinesPerInch_Type.__name__ = "Integer32"
_QmsHPPCLLinesPerInch_Object = MibScalar
qmsHPPCLLinesPerInch = _QmsHPPCLLinesPerInch_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 6),
    _QmsHPPCLLinesPerInch_Type()
)
qmsHPPCLLinesPerInch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLLinesPerInch.setStatus("mandatory")


class _QmsHPPCLDefaultSymbolSet_Type(Integer32):
    """Custom type qmsHPPCLDefaultSymbolSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              22,
              38,
              39,
              40,
              54,
              79,
              84,
              174,
              175,
              181,
              203,
              206,
              235,
              270,
              278,
              294,
              309,
              310,
              331,
              342,
              374,
              395,
              406,
              427,
              459,
              502,
              566,
              630)
        )
    )
    namedValues = NamedValues(
        *(("desktop", 235),
          ("iso11SWED", 20),
          ("iso15ITAL", 10),
          ("iso17SPAN", 84),
          ("iso21GERM", 40),
          ("iso4UK", 38),
          ("iso60NORW", 5),
          ("iso69FREN", 39),
          ("iso6ASCII", 22),
          ("isoLatin1", 15),
          ("isoLatin2", 79),
          ("isoLatin5", 175),
          ("legal", 54),
          ("math8", 270),
          ("mcText", 395),
          ("microsoftPub", 203),
          ("pc850", 406),
          ("pc852Latin2", 566),
          ("pc8DN", 374),
          ("pc8TK", 309),
          ("pc8US", 342),
          ("piFont", 502),
          ("psMath", 174),
          ("psText", 331),
          ("roman8", 278),
          ("ventura-Math", 206),
          ("venturaIntl", 427),
          ("venturaUS", 459),
          ("win30Latin1", 310),
          ("win31Latin1", 630),
          ("win31Latin2", 294),
          ("win31Latin5", 181))
    )


_QmsHPPCLDefaultSymbolSet_Type.__name__ = "Integer32"
_QmsHPPCLDefaultSymbolSet_Object = MibScalar
qmsHPPCLDefaultSymbolSet = _QmsHPPCLDefaultSymbolSet_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 8),
    _QmsHPPCLDefaultSymbolSet_Type()
)
qmsHPPCLDefaultSymbolSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLDefaultSymbolSet.setStatus("mandatory")


class _QmsHPPCLPreJobReset_Type(Integer32):
    """Custom type qmsHPPCLPreJobReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("oncompatibility", 3))
    )


_QmsHPPCLPreJobReset_Type.__name__ = "Integer32"
_QmsHPPCLPreJobReset_Object = MibScalar
qmsHPPCLPreJobReset = _QmsHPPCLPreJobReset_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 10),
    _QmsHPPCLPreJobReset_Type()
)
qmsHPPCLPreJobReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLPreJobReset.setStatus("mandatory")


class _QmsHPPCLPointSize_Type(Integer32):
    """Custom type qmsHPPCLPointSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 99975),
    )


_QmsHPPCLPointSize_Type.__name__ = "Integer32"
_QmsHPPCLPointSize_Object = MibScalar
qmsHPPCLPointSize = _QmsHPPCLPointSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 12),
    _QmsHPPCLPointSize_Type()
)
qmsHPPCLPointSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLPointSize.setStatus("mandatory")


class _QmsHPPCLDefaultFontID_Type(Integer32):
    """Custom type qmsHPPCLDefaultFontID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QmsHPPCLDefaultFontID_Type.__name__ = "Integer32"
_QmsHPPCLDefaultFontID_Object = MibScalar
qmsHPPCLDefaultFontID = _QmsHPPCLDefaultFontID_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 16),
    _QmsHPPCLDefaultFontID_Type()
)
qmsHPPCLDefaultFontID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLDefaultFontID.setStatus("mandatory")


class _QmsHPPCLGL2Plotter_Type(Integer32):
    """Custom type qmsHPPCLGL2Plotter based on Integer32"""
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


_QmsHPPCLGL2Plotter_Type.__name__ = "Integer32"
_QmsHPPCLGL2Plotter_Object = MibScalar
qmsHPPCLGL2Plotter = _QmsHPPCLGL2Plotter_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 18),
    _QmsHPPCLGL2Plotter_Type()
)
qmsHPPCLGL2Plotter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsHPPCLGL2Plotter.setStatus("mandatory")


class _QmsHPPCLDiskOrRam_Type(Integer32):
    """Custom type qmsHPPCLDiskOrRam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disk", 2),
          ("memory", 1))
    )


_QmsHPPCLDiskOrRam_Type.__name__ = "Integer32"
_QmsHPPCLDiskOrRam_Object = MibScalar
qmsHPPCLDiskOrRam = _QmsHPPCLDiskOrRam_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 525, 24),
    _QmsHPPCLDiskOrRam_Type()
)
qmsHPPCLDiskOrRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsHPPCLDiskOrRam.setStatus("mandatory")
_QmsDECLN03_ObjectIdentity = ObjectIdentity
qmsDECLN03 = _QmsDECLN03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 532)
)


class _QmsDECLN03ProductID_Type(Integer32):
    """Custom type qmsDECLN03ProductID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("la100", 3),
          ("ln03", 1),
          ("lqp02", 2))
    )


_QmsDECLN03ProductID_Type.__name__ = "Integer32"
_QmsDECLN03ProductID_Object = MibScalar
qmsDECLN03ProductID = _QmsDECLN03ProductID_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 4),
    _QmsDECLN03ProductID_Type()
)
qmsDECLN03ProductID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03ProductID.setStatus("mandatory")


class _QmsDECLN03AutowrapMode_Type(Integer32):
    """Custom type qmsDECLN03AutowrapMode based on Integer32"""
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


_QmsDECLN03AutowrapMode_Type.__name__ = "Integer32"
_QmsDECLN03AutowrapMode_Object = MibScalar
qmsDECLN03AutowrapMode = _QmsDECLN03AutowrapMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 5),
    _QmsDECLN03AutowrapMode_Type()
)
qmsDECLN03AutowrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03AutowrapMode.setStatus("mandatory")


class _QmsDECLN03PaperSize_Type(Integer32):
    """Custom type qmsDECLN03PaperSize based on Integer32"""
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
        *(("a4", 2),
          ("legal", 3),
          ("letter", 1),
          ("sz11x17", 4))
    )


_QmsDECLN03PaperSize_Type.__name__ = "Integer32"
_QmsDECLN03PaperSize_Object = MibScalar
qmsDECLN03PaperSize = _QmsDECLN03PaperSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 6),
    _QmsDECLN03PaperSize_Type()
)
qmsDECLN03PaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03PaperSize.setStatus("mandatory")


class _QmsDECLN03PaperSizeOverride_Type(Integer32):
    """Custom type qmsDECLN03PaperSizeOverride based on Integer32"""
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


_QmsDECLN03PaperSizeOverride_Type.__name__ = "Integer32"
_QmsDECLN03PaperSizeOverride_Object = MibScalar
qmsDECLN03PaperSizeOverride = _QmsDECLN03PaperSizeOverride_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 7),
    _QmsDECLN03PaperSizeOverride_Type()
)
qmsDECLN03PaperSizeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03PaperSizeOverride.setStatus("mandatory")
_QmsDECLN03Xorigin_Type = Integer32
_QmsDECLN03Xorigin_Object = MibScalar
qmsDECLN03Xorigin = _QmsDECLN03Xorigin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 8),
    _QmsDECLN03Xorigin_Type()
)
qmsDECLN03Xorigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03Xorigin.setStatus("mandatory")
_QmsDECLN03Yorigin_Type = Integer32
_QmsDECLN03Yorigin_Object = MibScalar
qmsDECLN03Yorigin = _QmsDECLN03Yorigin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 10),
    _QmsDECLN03Yorigin_Type()
)
qmsDECLN03Yorigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03Yorigin.setStatus("mandatory")


class _QmsDECLN03Reset_Type(Integer32):
    """Custom type qmsDECLN03Reset based on Integer32"""
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


_QmsDECLN03Reset_Type.__name__ = "Integer32"
_QmsDECLN03Reset_Object = MibScalar
qmsDECLN03Reset = _QmsDECLN03Reset_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 12),
    _QmsDECLN03Reset_Type()
)
qmsDECLN03Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03Reset.setStatus("mandatory")


class _QmsDECLN03Orientation_Type(Integer32):
    """Custom type qmsDECLN03Orientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 2),
          ("portrait", 1))
    )


_QmsDECLN03Orientation_Type.__name__ = "Integer32"
_QmsDECLN03Orientation_Object = MibScalar
qmsDECLN03Orientation = _QmsDECLN03Orientation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 532, 14),
    _QmsDECLN03Orientation_Type()
)
qmsDECLN03Orientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsDECLN03Orientation.setStatus("mandatory")
_QmsQUIC2_ObjectIdentity = ObjectIdentity
qmsQUIC2 = _QmsQUIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 534)
)


class _QmsQUIC2CommandCharacter_Type(Integer32):
    """Custom type qmsQUIC2CommandCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_QmsQUIC2CommandCharacter_Type.__name__ = "Integer32"
_QmsQUIC2CommandCharacter_Object = MibScalar
qmsQUIC2CommandCharacter = _QmsQUIC2CommandCharacter_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 4),
    _QmsQUIC2CommandCharacter_Type()
)
qmsQUIC2CommandCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2CommandCharacter.setStatus("mandatory")


class _QmsQUIC2TopMargin_Type(Integer32):
    """Custom type qmsQUIC2TopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_QmsQUIC2TopMargin_Type.__name__ = "Integer32"
_QmsQUIC2TopMargin_Object = MibScalar
qmsQUIC2TopMargin = _QmsQUIC2TopMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 6),
    _QmsQUIC2TopMargin_Type()
)
qmsQUIC2TopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TopMargin.setStatus("mandatory")


class _QmsQUIC2BottomMargin_Type(Integer32):
    """Custom type qmsQUIC2BottomMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_QmsQUIC2BottomMargin_Type.__name__ = "Integer32"
_QmsQUIC2BottomMargin_Object = MibScalar
qmsQUIC2BottomMargin = _QmsQUIC2BottomMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 8),
    _QmsQUIC2BottomMargin_Type()
)
qmsQUIC2BottomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2BottomMargin.setStatus("mandatory")


class _QmsQUIC2LeftMargin_Type(Integer32):
    """Custom type qmsQUIC2LeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_QmsQUIC2LeftMargin_Type.__name__ = "Integer32"
_QmsQUIC2LeftMargin_Object = MibScalar
qmsQUIC2LeftMargin = _QmsQUIC2LeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 10),
    _QmsQUIC2LeftMargin_Type()
)
qmsQUIC2LeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2LeftMargin.setStatus("mandatory")


class _QmsQUIC2RightMargin_Type(Integer32):
    """Custom type qmsQUIC2RightMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_QmsQUIC2RightMargin_Type.__name__ = "Integer32"
_QmsQUIC2RightMargin_Object = MibScalar
qmsQUIC2RightMargin = _QmsQUIC2RightMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 12),
    _QmsQUIC2RightMargin_Type()
)
qmsQUIC2RightMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2RightMargin.setStatus("mandatory")


class _QmsQUIC2IfParam_Type(Integer32):
    """Custom type qmsQUIC2IfParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediateEject", 2),
          ("immediateErase", 1),
          ("onPageEject", 3))
    )


_QmsQUIC2IfParam_Type.__name__ = "Integer32"
_QmsQUIC2IfParam_Object = MibScalar
qmsQUIC2IfParam = _QmsQUIC2IfParam_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 14),
    _QmsQUIC2IfParam_Type()
)
qmsQUIC2IfParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2IfParam.setStatus("mandatory")


class _QmsQUIC2CReqCRLF_Type(Integer32):
    """Custom type qmsQUIC2CReqCRLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crEQcr", 1),
          ("crEQcrANDlf", 2))
    )


_QmsQUIC2CReqCRLF_Type.__name__ = "Integer32"
_QmsQUIC2CReqCRLF_Object = MibScalar
qmsQUIC2CReqCRLF = _QmsQUIC2CReqCRLF_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 15),
    _QmsQUIC2CReqCRLF_Type()
)
qmsQUIC2CReqCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2CReqCRLF.setStatus("mandatory")


class _QmsQUIC2LFeqLFCR_Type(Integer32):
    """Custom type qmsQUIC2LFeqLFCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lfEQlf", 1),
          ("lfEQlfANDcr", 2))
    )


_QmsQUIC2LFeqLFCR_Type.__name__ = "Integer32"
_QmsQUIC2LFeqLFCR_Object = MibScalar
qmsQUIC2LFeqLFCR = _QmsQUIC2LFeqLFCR_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 16),
    _QmsQUIC2LFeqLFCR_Type()
)
qmsQUIC2LFeqLFCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2LFeqLFCR.setStatus("mandatory")


class _QmsQUIC2Decimal_Type(Integer32):
    """Custom type qmsQUIC2Decimal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("explicit", 3),
          ("implicitLeft", 1),
          ("implicitRight", 2))
    )


_QmsQUIC2Decimal_Type.__name__ = "Integer32"
_QmsQUIC2Decimal_Object = MibScalar
qmsQUIC2Decimal = _QmsQUIC2Decimal_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 17),
    _QmsQUIC2Decimal_Type()
)
qmsQUIC2Decimal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2Decimal.setStatus("mandatory")


class _QmsQUIC2Dimensions_Type(Integer32):
    """Custom type qmsQUIC2Dimensions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("centimeters", 2),
          ("dots", 1),
          ("inches", 3))
    )


_QmsQUIC2Dimensions_Type.__name__ = "Integer32"
_QmsQUIC2Dimensions_Object = MibScalar
qmsQUIC2Dimensions = _QmsQUIC2Dimensions_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 18),
    _QmsQUIC2Dimensions_Type()
)
qmsQUIC2Dimensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2Dimensions.setStatus("mandatory")


class _QmsQUIC2EDPMode_Type(Integer32):
    """Custom type qmsQUIC2EDPMode based on Integer32"""
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


_QmsQUIC2EDPMode_Type.__name__ = "Integer32"
_QmsQUIC2EDPMode_Object = MibScalar
qmsQUIC2EDPMode = _QmsQUIC2EDPMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 19),
    _QmsQUIC2EDPMode_Type()
)
qmsQUIC2EDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2EDPMode.setStatus("mandatory")


class _QmsQUIC2DefaultFont_Type(Integer32):
    """Custom type qmsQUIC2DefaultFont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QmsQUIC2DefaultFont_Type.__name__ = "Integer32"
_QmsQUIC2DefaultFont_Object = MibScalar
qmsQUIC2DefaultFont = _QmsQUIC2DefaultFont_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 20),
    _QmsQUIC2DefaultFont_Type()
)
qmsQUIC2DefaultFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2DefaultFont.setStatus("mandatory")


class _QmsQUIC2LineSpacing_Type(Integer32):
    """Custom type qmsQUIC2LineSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lpi6", 1),
          ("lpi8", 2))
    )


_QmsQUIC2LineSpacing_Type.__name__ = "Integer32"
_QmsQUIC2LineSpacing_Object = MibScalar
qmsQUIC2LineSpacing = _QmsQUIC2LineSpacing_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 22),
    _QmsQUIC2LineSpacing_Type()
)
qmsQUIC2LineSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2LineSpacing.setStatus("mandatory")


class _QmsQUIC2Orientation_Type(Integer32):
    """Custom type qmsQUIC2Orientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 2),
          ("portrait", 1))
    )


_QmsQUIC2Orientation_Type.__name__ = "Integer32"
_QmsQUIC2Orientation_Object = MibScalar
qmsQUIC2Orientation = _QmsQUIC2Orientation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 23),
    _QmsQUIC2Orientation_Type()
)
qmsQUIC2Orientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2Orientation.setStatus("mandatory")


class _QmsQUIC2Scan_Type(Integer32):
    """Custom type qmsQUIC2Scan based on Integer32"""
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


_QmsQUIC2Scan_Type.__name__ = "Integer32"
_QmsQUIC2Scan_Object = MibScalar
qmsQUIC2Scan = _QmsQUIC2Scan_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 24),
    _QmsQUIC2Scan_Type()
)
qmsQUIC2Scan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2Scan.setStatus("mandatory")


class _QmsQUIC2Spaces_Type(Integer32):
    """Custom type qmsQUIC2Spaces based on Integer32"""
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


_QmsQUIC2Spaces_Type.__name__ = "Integer32"
_QmsQUIC2Spaces_Object = MibScalar
qmsQUIC2Spaces = _QmsQUIC2Spaces_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 25),
    _QmsQUIC2Spaces_Type()
)
qmsQUIC2Spaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2Spaces.setStatus("mandatory")


class _QmsQUIC2AllowDataRepeats_Type(Integer32):
    """Custom type qmsQUIC2AllowDataRepeats based on Integer32"""
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


_QmsQUIC2AllowDataRepeats_Type.__name__ = "Integer32"
_QmsQUIC2AllowDataRepeats_Object = MibScalar
qmsQUIC2AllowDataRepeats = _QmsQUIC2AllowDataRepeats_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 26),
    _QmsQUIC2AllowDataRepeats_Type()
)
qmsQUIC2AllowDataRepeats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2AllowDataRepeats.setStatus("mandatory")


class _QmsQUIC2AllowOverlays_Type(Integer32):
    """Custom type qmsQUIC2AllowOverlays based on Integer32"""
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


_QmsQUIC2AllowOverlays_Type.__name__ = "Integer32"
_QmsQUIC2AllowOverlays_Object = MibScalar
qmsQUIC2AllowOverlays = _QmsQUIC2AllowOverlays_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 27),
    _QmsQUIC2AllowOverlays_Type()
)
qmsQUIC2AllowOverlays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2AllowOverlays.setStatus("mandatory")


class _QmsQUIC2AllowPageCopies_Type(Integer32):
    """Custom type qmsQUIC2AllowPageCopies based on Integer32"""
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


_QmsQUIC2AllowPageCopies_Type.__name__ = "Integer32"
_QmsQUIC2AllowPageCopies_Object = MibScalar
qmsQUIC2AllowPageCopies = _QmsQUIC2AllowPageCopies_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 28),
    _QmsQUIC2AllowPageCopies_Type()
)
qmsQUIC2AllowPageCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2AllowPageCopies.setStatus("mandatory")


class _QmsQUIC2SaveDLF_Type(Integer32):
    """Custom type qmsQUIC2SaveDLF based on Integer32"""
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


_QmsQUIC2SaveDLF_Type.__name__ = "Integer32"
_QmsQUIC2SaveDLF_Object = MibScalar
qmsQUIC2SaveDLF = _QmsQUIC2SaveDLF_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 29),
    _QmsQUIC2SaveDLF_Type()
)
qmsQUIC2SaveDLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2SaveDLF.setStatus("mandatory")


class _QmsQUIC2SaveOverlays_Type(Integer32):
    """Custom type qmsQUIC2SaveOverlays based on Integer32"""
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


_QmsQUIC2SaveOverlays_Type.__name__ = "Integer32"
_QmsQUIC2SaveOverlays_Object = MibScalar
qmsQUIC2SaveOverlays = _QmsQUIC2SaveOverlays_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 30),
    _QmsQUIC2SaveOverlays_Type()
)
qmsQUIC2SaveOverlays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2SaveOverlays.setStatus("mandatory")


class _QmsQUIC2DefaultMode_Type(Integer32):
    """Custom type qmsQUIC2DefaultMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandFree", 2),
          ("commandNoFree", 3),
          ("linePrinter", 1))
    )


_QmsQUIC2DefaultMode_Type.__name__ = "Integer32"
_QmsQUIC2DefaultMode_Object = MibScalar
qmsQUIC2DefaultMode = _QmsQUIC2DefaultMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 31),
    _QmsQUIC2DefaultMode_Type()
)
qmsQUIC2DefaultMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2DefaultMode.setStatus("mandatory")


class _QmsQUIC2RebuildFontTable_Type(Integer32):
    """Custom type qmsQUIC2RebuildFontTable based on Integer32"""
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


_QmsQUIC2RebuildFontTable_Type.__name__ = "Integer32"
_QmsQUIC2RebuildFontTable_Object = MibScalar
qmsQUIC2RebuildFontTable = _QmsQUIC2RebuildFontTable_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 32),
    _QmsQUIC2RebuildFontTable_Type()
)
qmsQUIC2RebuildFontTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2RebuildFontTable.setStatus("mandatory")


class _QmsQUIC2TrayMap1_Type(Integer32):
    """Custom type qmsQUIC2TrayMap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_QmsQUIC2TrayMap1_Type.__name__ = "Integer32"
_QmsQUIC2TrayMap1_Object = MibScalar
qmsQUIC2TrayMap1 = _QmsQUIC2TrayMap1_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 33),
    _QmsQUIC2TrayMap1_Type()
)
qmsQUIC2TrayMap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TrayMap1.setStatus("mandatory")


class _QmsQUIC2TrayMap2_Type(Integer32):
    """Custom type qmsQUIC2TrayMap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_QmsQUIC2TrayMap2_Type.__name__ = "Integer32"
_QmsQUIC2TrayMap2_Object = MibScalar
qmsQUIC2TrayMap2 = _QmsQUIC2TrayMap2_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 34),
    _QmsQUIC2TrayMap2_Type()
)
qmsQUIC2TrayMap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TrayMap2.setStatus("mandatory")


class _QmsQUIC2TrayMap3_Type(Integer32):
    """Custom type qmsQUIC2TrayMap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_QmsQUIC2TrayMap3_Type.__name__ = "Integer32"
_QmsQUIC2TrayMap3_Object = MibScalar
qmsQUIC2TrayMap3 = _QmsQUIC2TrayMap3_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 35),
    _QmsQUIC2TrayMap3_Type()
)
qmsQUIC2TrayMap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TrayMap3.setStatus("mandatory")


class _QmsQUIC2TrayMap4_Type(Integer32):
    """Custom type qmsQUIC2TrayMap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_QmsQUIC2TrayMap4_Type.__name__ = "Integer32"
_QmsQUIC2TrayMap4_Object = MibScalar
qmsQUIC2TrayMap4 = _QmsQUIC2TrayMap4_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 36),
    _QmsQUIC2TrayMap4_Type()
)
qmsQUIC2TrayMap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TrayMap4.setStatus("mandatory")


class _QmsQUIC2TrayMap5_Type(Integer32):
    """Custom type qmsQUIC2TrayMap5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_QmsQUIC2TrayMap5_Type.__name__ = "Integer32"
_QmsQUIC2TrayMap5_Object = MibScalar
qmsQUIC2TrayMap5 = _QmsQUIC2TrayMap5_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 37),
    _QmsQUIC2TrayMap5_Type()
)
qmsQUIC2TrayMap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2TrayMap5.setStatus("mandatory")


class _QmsQUIC2PatternType_Type(Integer32):
    """Custom type qmsQUIC2PatternType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opaque", 1),
          ("transparent", 2))
    )


_QmsQUIC2PatternType_Type.__name__ = "Integer32"
_QmsQUIC2PatternType_Object = MibScalar
qmsQUIC2PatternType = _QmsQUIC2PatternType_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 534, 38),
    _QmsQUIC2PatternType_Type()
)
qmsQUIC2PatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsQUIC2PatternType.setStatus("mandatory")
_QmsCCITT_ObjectIdentity = ObjectIdentity
qmsCCITT = _QmsCCITT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 538)
)
_QmsLinePrinter_ObjectIdentity = ObjectIdentity
qmsLinePrinter = _QmsLinePrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 539)
)


class _QmsLPPointSize_Type(Integer32):
    """Custom type qmsLPPointSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_QmsLPPointSize_Type.__name__ = "Integer32"
_QmsLPPointSize_Object = MibScalar
qmsLPPointSize = _QmsLPPointSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 4),
    _QmsLPPointSize_Type()
)
qmsLPPointSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPPointSize.setStatus("mandatory")


class _QmsLPTabStops_Type(Integer32):
    """Custom type qmsLPTabStops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_QmsLPTabStops_Type.__name__ = "Integer32"
_QmsLPTabStops_Object = MibScalar
qmsLPTabStops = _QmsLPTabStops_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 8),
    _QmsLPTabStops_Type()
)
qmsLPTabStops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPTabStops.setStatus("mandatory")


class _QmsLPLinesPerPage_Type(Integer32):
    """Custom type qmsLPLinesPerPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_QmsLPLinesPerPage_Type.__name__ = "Integer32"
_QmsLPLinesPerPage_Object = MibScalar
qmsLPLinesPerPage = _QmsLPLinesPerPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 12),
    _QmsLPLinesPerPage_Type()
)
qmsLPLinesPerPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPLinesPerPage.setStatus("mandatory")


class _QmsLPLeftMargin_Type(Integer32):
    """Custom type qmsLPLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 79200),
    )


_QmsLPLeftMargin_Type.__name__ = "Integer32"
_QmsLPLeftMargin_Object = MibScalar
qmsLPLeftMargin = _QmsLPLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 16),
    _QmsLPLeftMargin_Type()
)
qmsLPLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPLeftMargin.setStatus("mandatory")


class _QmsLPRightMargin_Type(Integer32):
    """Custom type qmsLPRightMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 79200),
    )


_QmsLPRightMargin_Type.__name__ = "Integer32"
_QmsLPRightMargin_Object = MibScalar
qmsLPRightMargin = _QmsLPRightMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 20),
    _QmsLPRightMargin_Type()
)
qmsLPRightMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPRightMargin.setStatus("mandatory")


class _QmsLPTopMargin_Type(Integer32):
    """Custom type qmsLPTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 79200),
    )


_QmsLPTopMargin_Type.__name__ = "Integer32"
_QmsLPTopMargin_Object = MibScalar
qmsLPTopMargin = _QmsLPTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 24),
    _QmsLPTopMargin_Type()
)
qmsLPTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPTopMargin.setStatus("mandatory")


class _QmsLPBottomMargin_Type(Integer32):
    """Custom type qmsLPBottomMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 79200),
    )


_QmsLPBottomMargin_Type.__name__ = "Integer32"
_QmsLPBottomMargin_Object = MibScalar
qmsLPBottomMargin = _QmsLPBottomMargin_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 28),
    _QmsLPBottomMargin_Type()
)
qmsLPBottomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPBottomMargin.setStatus("mandatory")


class _QmsLPAsciiMap_Type(Integer32):
    """Custom type qmsLPAsciiMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("ebcdic", 1))
    )


_QmsLPAsciiMap_Type.__name__ = "Integer32"
_QmsLPAsciiMap_Object = MibScalar
qmsLPAsciiMap = _QmsLPAsciiMap_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 32),
    _QmsLPAsciiMap_Type()
)
qmsLPAsciiMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPAsciiMap.setStatus("mandatory")


class _QmsLPLineNumbering_Type(Integer32):
    """Custom type qmsLPLineNumbering based on Integer32"""
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


_QmsLPLineNumbering_Type.__name__ = "Integer32"
_QmsLPLineNumbering_Object = MibScalar
qmsLPLineNumbering = _QmsLPLineNumbering_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 34),
    _QmsLPLineNumbering_Type()
)
qmsLPLineNumbering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPLineNumbering.setStatus("mandatory")


class _QmsLPLFisCRLF_Type(Integer32):
    """Custom type qmsLPLFisCRLF based on Integer32"""
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


_QmsLPLFisCRLF_Type.__name__ = "Integer32"
_QmsLPLFisCRLF_Object = MibScalar
qmsLPLFisCRLF = _QmsLPLFisCRLF_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 36),
    _QmsLPLFisCRLF_Type()
)
qmsLPLFisCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPLFisCRLF.setStatus("mandatory")


class _QmsLPCRisCRLF_Type(Integer32):
    """Custom type qmsLPCRisCRLF based on Integer32"""
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


_QmsLPCRisCRLF_Type.__name__ = "Integer32"
_QmsLPCRisCRLF_Object = MibScalar
qmsLPCRisCRLF = _QmsLPCRisCRLF_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 38),
    _QmsLPCRisCRLF_Type()
)
qmsLPCRisCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPCRisCRLF.setStatus("mandatory")


class _QmsLPFFisCRFF_Type(Integer32):
    """Custom type qmsLPFFisCRFF based on Integer32"""
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


_QmsLPFFisCRFF_Type.__name__ = "Integer32"
_QmsLPFFisCRFF_Object = MibScalar
qmsLPFFisCRFF = _QmsLPFFisCRFF_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 40),
    _QmsLPFFisCRFF_Type()
)
qmsLPFFisCRFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPFFisCRFF.setStatus("mandatory")


class _QmsLPOrientation_Type(Integer32):
    """Custom type qmsLPOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 2),
          ("portrait", 1))
    )


_QmsLPOrientation_Type.__name__ = "Integer32"
_QmsLPOrientation_Object = MibScalar
qmsLPOrientation = _QmsLPOrientation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 42),
    _QmsLPOrientation_Type()
)
qmsLPOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPOrientation.setStatus("mandatory")


class _QmsLPLineWrap_Type(Integer32):
    """Custom type qmsLPLineWrap based on Integer32"""
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


_QmsLPLineWrap_Type.__name__ = "Integer32"
_QmsLPLineWrap_Object = MibScalar
qmsLPLineWrap = _QmsLPLineWrap_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 44),
    _QmsLPLineWrap_Type()
)
qmsLPLineWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPLineWrap.setStatus("mandatory")


class _QmsLPFont_Type(DisplayString):
    """Custom type qmsLPFont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QmsLPFont_Type.__name__ = "DisplayString"
_QmsLPFont_Object = MibScalar
qmsLPFont = _QmsLPFont_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 539, 46),
    _QmsLPFont_Type()
)
qmsLPFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsLPFont.setStatus("mandatory")
_QmsTIFF_ObjectIdentity = ObjectIdentity
qmsTIFF = _QmsTIFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 541)
)


class _QmsTIFFAutoRotation_Type(Integer32):
    """Custom type qmsTIFFAutoRotation based on Integer32"""
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
        *(("off", 1),
          ("rot180", 4),
          ("rot270", 3),
          ("rot90", 2))
    )


_QmsTIFFAutoRotation_Type.__name__ = "Integer32"
_QmsTIFFAutoRotation_Object = MibScalar
qmsTIFFAutoRotation = _QmsTIFFAutoRotation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 1),
    _QmsTIFFAutoRotation_Type()
)
qmsTIFFAutoRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFAutoRotation.setStatus("mandatory")


class _QmsTIFFScratchFileSize_Type(Integer32):
    """Custom type qmsTIFFScratchFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QmsTIFFScratchFileSize_Type.__name__ = "Integer32"
_QmsTIFFScratchFileSize_Object = MibScalar
qmsTIFFScratchFileSize = _QmsTIFFScratchFileSize_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 2),
    _QmsTIFFScratchFileSize_Type()
)
qmsTIFFScratchFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFScratchFileSize.setStatus("mandatory")


class _QmsTIFFPaperToImage_Type(Integer32):
    """Custom type qmsTIFFPaperToImage based on Integer32"""
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


_QmsTIFFPaperToImage_Type.__name__ = "Integer32"
_QmsTIFFPaperToImage_Object = MibScalar
qmsTIFFPaperToImage = _QmsTIFFPaperToImage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 3),
    _QmsTIFFPaperToImage_Type()
)
qmsTIFFPaperToImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFPaperToImage.setStatus("mandatory")


class _QmsTIFFAnnotationState_Type(Integer32):
    """Custom type qmsTIFFAnnotationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QmsTIFFAnnotationState_Type.__name__ = "Integer32"
_QmsTIFFAnnotationState_Object = MibScalar
qmsTIFFAnnotationState = _QmsTIFFAnnotationState_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 4),
    _QmsTIFFAnnotationState_Type()
)
qmsTIFFAnnotationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFAnnotationState.setStatus("mandatory")


class _QmsTIFFAnnotationTag_Type(Integer32):
    """Custom type qmsTIFFAnnotationTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_QmsTIFFAnnotationTag_Type.__name__ = "Integer32"
_QmsTIFFAnnotationTag_Object = MibScalar
qmsTIFFAnnotationTag = _QmsTIFFAnnotationTag_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 5),
    _QmsTIFFAnnotationTag_Type()
)
qmsTIFFAnnotationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFAnnotationTag.setStatus("mandatory")


class _QmsTIFFReverseImage_Type(Integer32):
    """Custom type qmsTIFFReverseImage based on Integer32"""
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


_QmsTIFFReverseImage_Type.__name__ = "Integer32"
_QmsTIFFReverseImage_Object = MibScalar
qmsTIFFReverseImage = _QmsTIFFReverseImage_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 7),
    _QmsTIFFReverseImage_Type()
)
qmsTIFFReverseImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFReverseImage.setStatus("mandatory")


class _QmsTIFFAutoScaling_Type(Integer32):
    """Custom type qmsTIFFAutoScaling based on Integer32"""
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
        *(("downOnly", 4),
          ("off", 1),
          ("upANDdown", 2),
          ("upOnly", 3))
    )


_QmsTIFFAutoScaling_Type.__name__ = "Integer32"
_QmsTIFFAutoScaling_Object = MibScalar
qmsTIFFAutoScaling = _QmsTIFFAutoScaling_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 541, 50),
    _QmsTIFFAutoScaling_Type()
)
qmsTIFFAutoScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsTIFFAutoScaling.setStatus("mandatory")
_QmsCALS_ObjectIdentity = ObjectIdentity
qmsCALS = _QmsCALS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 542)
)


class _QmsCALSAutoRotation_Type(Integer32):
    """Custom type qmsCALSAutoRotation based on Integer32"""
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
        *(("off", 1),
          ("rot180", 4),
          ("rot270", 3),
          ("rot90", 2))
    )


_QmsCALSAutoRotation_Type.__name__ = "Integer32"
_QmsCALSAutoRotation_Object = MibScalar
qmsCALSAutoRotation = _QmsCALSAutoRotation_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 542, 1),
    _QmsCALSAutoRotation_Type()
)
qmsCALSAutoRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCALSAutoRotation.setStatus("mandatory")


class _QmsCALSAutoScaling_Type(Integer32):
    """Custom type qmsCALSAutoScaling based on Integer32"""
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
        *(("downOnly", 4),
          ("off", 1),
          ("upANDdown", 2),
          ("upOnly", 3))
    )


_QmsCALSAutoScaling_Type.__name__ = "Integer32"
_QmsCALSAutoScaling_Object = MibScalar
qmsCALSAutoScaling = _QmsCALSAutoScaling_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 542, 50),
    _QmsCALSAutoScaling_Type()
)
qmsCALSAutoScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCALSAutoScaling.setStatus("mandatory")
_QmsCGM_ObjectIdentity = ObjectIdentity
qmsCGM = _QmsCGM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 1, 544)
)


class _QmsCGMSuppressScale_Type(Integer32):
    """Custom type qmsCGMSuppressScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsCGMSuppressScale_Type.__name__ = "Integer32"
_QmsCGMSuppressScale_Object = MibScalar
qmsCGMSuppressScale = _QmsCGMSuppressScale_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 1),
    _QmsCGMSuppressScale_Type()
)
qmsCGMSuppressScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMSuppressScale.setStatus("mandatory")


class _QmsCGMMono_Type(Integer32):
    """Custom type qmsCGMMono based on Integer32"""
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


_QmsCGMMono_Type.__name__ = "Integer32"
_QmsCGMMono_Object = MibScalar
qmsCGMMono = _QmsCGMMono_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 2),
    _QmsCGMMono_Type()
)
qmsCGMMono.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMMono.setStatus("mandatory")


class _QmsCGMIgnoreBorder_Type(Integer32):
    """Custom type qmsCGMIgnoreBorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsCGMIgnoreBorder_Type.__name__ = "Integer32"
_QmsCGMIgnoreBorder_Object = MibScalar
qmsCGMIgnoreBorder = _QmsCGMIgnoreBorder_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 3),
    _QmsCGMIgnoreBorder_Type()
)
qmsCGMIgnoreBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMIgnoreBorder.setStatus("mandatory")


class _QmsCGMOriginX_Type(Integer32):
    """Custom type qmsCGMOriginX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1700),
    )


_QmsCGMOriginX_Type.__name__ = "Integer32"
_QmsCGMOriginX_Object = MibScalar
qmsCGMOriginX = _QmsCGMOriginX_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 4),
    _QmsCGMOriginX_Type()
)
qmsCGMOriginX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMOriginX.setStatus("mandatory")


class _QmsCGMOriginY_Type(Integer32):
    """Custom type qmsCGMOriginY based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1700),
    )


_QmsCGMOriginY_Type.__name__ = "Integer32"
_QmsCGMOriginY_Object = MibScalar
qmsCGMOriginY = _QmsCGMOriginY_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 8),
    _QmsCGMOriginY_Type()
)
qmsCGMOriginY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMOriginY.setStatus("mandatory")


class _QmsCGMPrintErrors_Type(Integer32):
    """Custom type qmsCGMPrintErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QmsCGMPrintErrors_Type.__name__ = "Integer32"
_QmsCGMPrintErrors_Object = MibScalar
qmsCGMPrintErrors = _QmsCGMPrintErrors_Object(
    (1, 3, 6, 1, 4, 1, 480, 1, 544, 12),
    _QmsCGMPrintErrors_Type()
)
qmsCGMPrintErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsCGMPrintErrors.setStatus("mandatory")
_QmsRel_ObjectIdentity = ObjectIdentity
qmsRel = _QmsRel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2)
)
_QmsPrinter_ObjectIdentity = ObjectIdentity
qmsPrinter = _QmsPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 1)
)
_QmsPtrSys_ObjectIdentity = ObjectIdentity
qmsPtrSys = _QmsPtrSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1)
)


class _QmsPtrSysStatus_Type(DisplayString):
    """Custom type qmsPtrSysStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrSysStatus_Type.__name__ = "DisplayString"
_QmsPtrSysStatus_Object = MibScalar
qmsPtrSysStatus = _QmsPtrSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 1),
    _QmsPtrSysStatus_Type()
)
qmsPtrSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrSysStatus.setStatus("mandatory")


class _QmsPtrSysNamePrinter_Type(DisplayString):
    """Custom type qmsPtrSysNamePrinter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrSysNamePrinter_Type.__name__ = "DisplayString"
_QmsPtrSysNamePrinter_Object = MibScalar
qmsPtrSysNamePrinter = _QmsPtrSysNamePrinter_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 2),
    _QmsPtrSysNamePrinter_Type()
)
qmsPtrSysNamePrinter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrSysNamePrinter.setStatus("optional")
_QmsPtrIfTable_Object = MibTable
qmsPtrIfTable = _QmsPtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qmsPtrIfTable.setStatus("mandatory")
_QmsPtrIfEntry_Object = MibTableRow
qmsPtrIfEntry = _QmsPtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 3, 1)
)
qmsPtrIfEntry.setIndexNames(
    (0, "QMS-MIB", "qmsPtrIfIndex"),
)
if mibBuilder.loadTexts:
    qmsPtrIfEntry.setStatus("mandatory")
_QmsPtrIfIndex_Type = Integer32
_QmsPtrIfIndex_Object = MibTableColumn
qmsPtrIfIndex = _QmsPtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 3, 1, 1),
    _QmsPtrIfIndex_Type()
)
qmsPtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrIfIndex.setStatus("mandatory")


class _QmsPtrIfName_Type(DisplayString):
    """Custom type qmsPtrIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrIfName_Type.__name__ = "DisplayString"
_QmsPtrIfName_Object = MibTableColumn
qmsPtrIfName = _QmsPtrIfName_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 3, 1, 2),
    _QmsPtrIfName_Type()
)
qmsPtrIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrIfName.setStatus("mandatory")


class _QmsPtrIfDefEmu_Type(Integer32):
    """Custom type qmsPtrIfDefEmu based on Integer32"""
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
              201,
              65534,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("ccitt", 19),
          ("code-v", 17),
          ("dec-ansi", 11),
          ("diablo-630", 3),
          ("epson-fx", 10),
          ("esp", 201),
          ("hex-dump", 7),
          ("hp-gl", 5),
          ("hp-pcl", 6),
          ("hp-pcl-5", 21),
          ("ibm-ext-ascii", 12),
          ("ibm-proprinter", 2),
          ("impress", 16),
          ("line-printer", 20),
          ("ln03", 13),
          ("not-supported", 65534),
          ("quic-2", 15),
          ("r1", 18),
          ("tektronix-4014", 14),
          ("ti-810", 9),
          ("ti-855", 4),
          ("ti-855-dp", 8),
          ("ultrascript", 1),
          ("wild-card", 65535))
    )


_QmsPtrIfDefEmu_Type.__name__ = "Integer32"
_QmsPtrIfDefEmu_Object = MibTableColumn
qmsPtrIfDefEmu = _QmsPtrIfDefEmu_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 3, 1, 3),
    _QmsPtrIfDefEmu_Type()
)
qmsPtrIfDefEmu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrIfDefEmu.setStatus("mandatory")
_QmsPtrBinTable_Object = MibTable
qmsPtrBinTable = _QmsPtrBinTable_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qmsPtrBinTable.setStatus("mandatory")
_QmsPtrBinEntry_Object = MibTableRow
qmsPtrBinEntry = _QmsPtrBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1)
)
qmsPtrBinEntry.setIndexNames(
    (0, "QMS-MIB", "qmsPtrBinIndex"),
)
if mibBuilder.loadTexts:
    qmsPtrBinEntry.setStatus("mandatory")
_QmsPtrBinIndex_Type = Integer32
_QmsPtrBinIndex_Object = MibTableColumn
qmsPtrBinIndex = _QmsPtrBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1, 1),
    _QmsPtrBinIndex_Type()
)
qmsPtrBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrBinIndex.setStatus("mandatory")


class _QmsPtrBinType_Type(Integer32):
    """Custom type qmsPtrBinType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 2),
          ("output", 1))
    )


_QmsPtrBinType_Type.__name__ = "Integer32"
_QmsPtrBinType_Object = MibTableColumn
qmsPtrBinType = _QmsPtrBinType_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1, 2),
    _QmsPtrBinType_Type()
)
qmsPtrBinType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrBinType.setStatus("mandatory")
_QmsPtrBinId_Type = Integer32
_QmsPtrBinId_Object = MibTableColumn
qmsPtrBinId = _QmsPtrBinId_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1, 3),
    _QmsPtrBinId_Type()
)
qmsPtrBinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrBinId.setStatus("mandatory")


class _QmsPtrBinPaper_Type(DisplayString):
    """Custom type qmsPtrBinPaper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrBinPaper_Type.__name__ = "DisplayString"
_QmsPtrBinPaper_Object = MibTableColumn
qmsPtrBinPaper = _QmsPtrBinPaper_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1, 4),
    _QmsPtrBinPaper_Type()
)
qmsPtrBinPaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrBinPaper.setStatus("mandatory")


class _QmsPtrBinName_Type(DisplayString):
    """Custom type qmsPtrBinName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrBinName_Type.__name__ = "DisplayString"
_QmsPtrBinName_Object = MibTableColumn
qmsPtrBinName = _QmsPtrBinName_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 1, 4, 1, 5),
    _QmsPtrBinName_Type()
)
qmsPtrBinName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrBinName.setStatus("mandatory")
_QmsPtrEmu_ObjectIdentity = ObjectIdentity
qmsPtrEmu = _QmsPtrEmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 2)
)
_QmsPtrJobs_ObjectIdentity = ObjectIdentity
qmsPtrJobs = _QmsPtrJobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3)
)


class _QmsPtrJobsCurStatus_Type(Integer32):
    """Custom type qmsPtrJobsCurStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("canceled", 256),
          ("internal", 32768),
          ("interpreting", 2),
          ("printed", 128),
          ("printing", 8),
          ("rasterizing", 4),
          ("spooled", 64),
          ("spooling", 1),
          ("terminating", 16),
          ("waiting", 32))
    )


_QmsPtrJobsCurStatus_Type.__name__ = "Integer32"
_QmsPtrJobsCurStatus_Object = MibScalar
qmsPtrJobsCurStatus = _QmsPtrJobsCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 1),
    _QmsPtrJobsCurStatus_Type()
)
qmsPtrJobsCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsCurStatus.setStatus("mandatory")
_QmsPtrJobsCurSheet_Type = Integer32
_QmsPtrJobsCurSheet_Object = MibScalar
qmsPtrJobsCurSheet = _QmsPtrJobsCurSheet_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 2),
    _QmsPtrJobsCurSheet_Type()
)
qmsPtrJobsCurSheet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsCurSheet.setStatus("mandatory")
_QmsPtrJobsCurPage_Type = Integer32
_QmsPtrJobsCurPage_Object = MibScalar
qmsPtrJobsCurPage = _QmsPtrJobsCurPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 3),
    _QmsPtrJobsCurPage_Type()
)
qmsPtrJobsCurPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsCurPage.setStatus("mandatory")
_QmsPtrJobsTable_Object = MibTable
qmsPtrJobsTable = _QmsPtrJobsTable_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    qmsPtrJobsTable.setStatus("mandatory")
_QmsPtrJobsEntry_Object = MibTableRow
qmsPtrJobsEntry = _QmsPtrJobsEntry_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1)
)
qmsPtrJobsEntry.setIndexNames(
    (0, "QMS-MIB", "qmsPtrJobsIndex"),
)
if mibBuilder.loadTexts:
    qmsPtrJobsEntry.setStatus("mandatory")
_QmsPtrJobsIndex_Type = Integer32
_QmsPtrJobsIndex_Object = MibTableColumn
qmsPtrJobsIndex = _QmsPtrJobsIndex_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 1),
    _QmsPtrJobsIndex_Type()
)
qmsPtrJobsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsIndex.setStatus("mandatory")


class _QmsPtrJobsStatus_Type(Integer32):
    """Custom type qmsPtrJobsStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("canceled", 256),
          ("internal", 32768),
          ("interpreting", 2),
          ("printed", 128),
          ("printing", 8),
          ("rasterizing", 4),
          ("spooled", 64),
          ("spooling", 1),
          ("terminating", 16),
          ("waiting", 32))
    )


_QmsPtrJobsStatus_Type.__name__ = "Integer32"
_QmsPtrJobsStatus_Object = MibTableColumn
qmsPtrJobsStatus = _QmsPtrJobsStatus_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 2),
    _QmsPtrJobsStatus_Type()
)
qmsPtrJobsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsStatus.setStatus("mandatory")


class _QmsPtrJobsEmulation_Type(Integer32):
    """Custom type qmsPtrJobsEmulation based on Integer32"""
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
              25,
              26,
              201,
              65536)
        )
    )
    namedValues = NamedValues(
        *(("cals", 23),
          ("ccitt", 19),
          ("cgm", 25),
          ("code-v", 17),
          ("dec-ansi", 11),
          ("diablo-630", 3),
          ("epson-fx", 10),
          ("esp", 201),
          ("hex-dump", 7),
          ("hp-gl", 5),
          ("hp-pcl", 6),
          ("hp-pcl-5", 21),
          ("hp-pcl-xl", 26),
          ("ibm-ext-ascii", 12),
          ("ibm-proprinter", 2),
          ("impress", 16),
          ("line-printer", 20),
          ("ln03", 13),
          ("quic-2", 15),
          ("r1", 18),
          ("tektronix-4014", 14),
          ("ti-810", 9),
          ("ti-855", 4),
          ("ti-855-dp", 8),
          ("tiff", 22),
          ("ultrascript", 1),
          ("wild-card", 65536))
    )


_QmsPtrJobsEmulation_Type.__name__ = "Integer32"
_QmsPtrJobsEmulation_Object = MibTableColumn
qmsPtrJobsEmulation = _QmsPtrJobsEmulation_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 4),
    _QmsPtrJobsEmulation_Type()
)
qmsPtrJobsEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsEmulation.setStatus("mandatory")
_QmsPtrJobsPage_Type = Integer32
_QmsPtrJobsPage_Object = MibTableColumn
qmsPtrJobsPage = _QmsPtrJobsPage_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 5),
    _QmsPtrJobsPage_Type()
)
qmsPtrJobsPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsPage.setStatus("mandatory")
_QmsPtrJobsSheet_Type = Integer32
_QmsPtrJobsSheet_Object = MibTableColumn
qmsPtrJobsSheet = _QmsPtrJobsSheet_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 6),
    _QmsPtrJobsSheet_Type()
)
qmsPtrJobsSheet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsSheet.setStatus("mandatory")


class _QmsPtrJobsChannel_Type(Integer32):
    """Custom type qmsPtrJobsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              12,
              13,
              14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 14),
          ("optional-io", 16),
          ("other", 1),
          ("parallel", 13),
          ("rs-232", 12))
    )


_QmsPtrJobsChannel_Type.__name__ = "Integer32"
_QmsPtrJobsChannel_Object = MibTableColumn
qmsPtrJobsChannel = _QmsPtrJobsChannel_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 7),
    _QmsPtrJobsChannel_Type()
)
qmsPtrJobsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsChannel.setStatus("mandatory")


class _QmsPtrJobsComment_Type(DisplayString):
    """Custom type qmsPtrJobsComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrJobsComment_Type.__name__ = "DisplayString"
_QmsPtrJobsComment_Object = MibTableColumn
qmsPtrJobsComment = _QmsPtrJobsComment_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 8),
    _QmsPtrJobsComment_Type()
)
qmsPtrJobsComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsComment.setStatus("mandatory")


class _QmsPtrJobsTitle_Type(DisplayString):
    """Custom type qmsPtrJobsTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrJobsTitle_Type.__name__ = "DisplayString"
_QmsPtrJobsTitle_Object = MibTableColumn
qmsPtrJobsTitle = _QmsPtrJobsTitle_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 9),
    _QmsPtrJobsTitle_Type()
)
qmsPtrJobsTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsTitle.setStatus("mandatory")


class _QmsPtrJobsOwner_Type(DisplayString):
    """Custom type qmsPtrJobsOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QmsPtrJobsOwner_Type.__name__ = "DisplayString"
_QmsPtrJobsOwner_Object = MibTableColumn
qmsPtrJobsOwner = _QmsPtrJobsOwner_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 4, 1, 10),
    _QmsPtrJobsOwner_Type()
)
qmsPtrJobsOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsOwner.setStatus("mandatory")
_QmsPtrJobsStatPages_Type = Integer32
_QmsPtrJobsStatPages_Object = MibScalar
qmsPtrJobsStatPages = _QmsPtrJobsStatPages_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 6),
    _QmsPtrJobsStatPages_Type()
)
qmsPtrJobsStatPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsStatPages.setStatus("mandatory")
_QmsPtrJobsStatSheets_Type = Integer32
_QmsPtrJobsStatSheets_Object = MibScalar
qmsPtrJobsStatSheets = _QmsPtrJobsStatSheets_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 1, 3, 7),
    _QmsPtrJobsStatSheets_Type()
)
qmsPtrJobsStatSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmsPtrJobsStatSheets.setStatus("mandatory")
_QmsIF_ObjectIdentity = ObjectIdentity
qmsIF = _QmsIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9)
)
_QmsIFAdmin_ObjectIdentity = ObjectIdentity
qmsIFAdmin = _QmsIFAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 1)
)


class _QmsIFAdminUnitStatus_Type(Integer32):
    """Custom type qmsIFAdminUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardReset", 3),
          ("resetOnNoClient", 2),
          ("running", 1))
    )


_QmsIFAdminUnitStatus_Type.__name__ = "Integer32"
_QmsIFAdminUnitStatus_Object = MibTableColumn
qmsIFAdminUnitStatus = _QmsIFAdminUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 1, 1),
    _QmsIFAdminUnitStatus_Type()
)
qmsIFAdminUnitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsIFAdminUnitStatus.setStatus("mandatory")


class _QmsIFAdminConfigStatus_Type(Integer32):
    """Custom type qmsIFAdminConfigStatus based on Integer32"""
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
        *(("configDefaultRequest", 5),
          ("configLoadRequest", 3),
          ("configSaveRequest", 4),
          ("configUnknown1", 1),
          ("configUnknown2", 2))
    )


_QmsIFAdminConfigStatus_Type.__name__ = "Integer32"
_QmsIFAdminConfigStatus_Object = MibTableColumn
qmsIFAdminConfigStatus = _QmsIFAdminConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 1, 2),
    _QmsIFAdminConfigStatus_Type()
)
qmsIFAdminConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsIFAdminConfigStatus.setStatus("mandatory")
_QmsIFAdminOldIntAddr_Type = IpAddress
_QmsIFAdminOldIntAddr_Object = MibTableColumn
qmsIFAdminOldIntAddr = _QmsIFAdminOldIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 1, 3),
    _QmsIFAdminOldIntAddr_Type()
)
qmsIFAdminOldIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmsIFAdminOldIntAddr.setStatus("mandatory")
_QmsIFSetup_ObjectIdentity = ObjectIdentity
qmsIFSetup = _QmsIFSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2)
)
_QmsIFConfig_ObjectIdentity = ObjectIdentity
qmsIFConfig = _QmsIFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1)
)
_IntAddr_Type = IpAddress
_IntAddr_Object = MibTableColumn
intAddr = _IntAddr_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 1),
    _IntAddr_Type()
)
intAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intAddr.setStatus("mandatory")
_EthAddr_Type = IpAddress
_EthAddr_Object = MibTableColumn
ethAddr = _EthAddr_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 2),
    _EthAddr_Type()
)
ethAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAddr.setStatus("mandatory")
_DefRout_Type = IpAddress
_DefRout_Object = MibTableColumn
defRout = _DefRout_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 3),
    _DefRout_Type()
)
defRout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defRout.setStatus("mandatory")
_NetMask_Type = IpAddress
_NetMask_Object = MibTableColumn
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 4),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")


class _TcpEnb_Type(Integer32):
    """Custom type tcpEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpEnb_Type.__name__ = "Integer32"
_TcpEnb_Object = MibTableColumn
tcpEnb = _TcpEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 5),
    _TcpEnb_Type()
)
tcpEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEnb.setStatus("mandatory")


class _TftpEnb_Type(Integer32):
    """Custom type tftpEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TftpEnb_Type.__name__ = "Integer32"
_TftpEnb_Object = MibTableColumn
tftpEnb = _TftpEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 13),
    _TftpEnb_Type()
)
tftpEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpEnb.setStatus("mandatory")
_TnPort_Type = Integer32
_TnPort_Object = MibTableColumn
tnPort = _TnPort_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 16),
    _TnPort_Type()
)
tnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPort.setStatus("obsolete")


class _RtnOpt_Type(Integer32):
    """Custom type rtnOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RtnOpt_Type.__name__ = "Integer32"
_RtnOpt_Object = MibTableColumn
rtnOpt = _RtnOpt_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 18),
    _RtnOpt_Type()
)
rtnOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtnOpt.setStatus("obsolete")
_TrP1_Type = Integer32
_TrP1_Object = MibTableColumn
trP1 = _TrP1_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 30),
    _TrP1_Type()
)
trP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trP1.setStatus("mandatory")


class _BootP_Type(Integer32):
    """Custom type bootP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BootP_Type.__name__ = "Integer32"
_BootP_Object = MibTableColumn
bootP = _BootP_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 698),
    _BootP_Type()
)
bootP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootP.setStatus("mandatory")


class _Rarp_Type(Integer32):
    """Custom type rarp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Rarp_Type.__name__ = "Integer32"
_Rarp_Object = MibTableColumn
rarp = _Rarp_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 699),
    _Rarp_Type()
)
rarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rarp.setStatus("mandatory")


class _Spooling_Type(Integer32):
    """Custom type spooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("onIdle", 3),
          ("onInputIdle", 2))
    )


_Spooling_Type.__name__ = "Integer32"
_Spooling_Object = MibScalar
spooling = _Spooling_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 1, 9000),
    _Spooling_Type()
)
spooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spooling.setStatus("mandatory")
_QmsIFNetware_ObjectIdentity = ObjectIdentity
qmsIFNetware = _QmsIFNetware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5)
)


class _NetwEnb_Type(Integer32):
    """Custom type netwEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NetwEnb_Type.__name__ = "Integer32"
_NetwEnb_Object = MibTableColumn
netwEnb = _NetwEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 400),
    _NetwEnb_Type()
)
netwEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netwEnb.setStatus("mandatory")
_PsName_Type = DisplayString
_PsName_Object = MibTableColumn
psName = _PsName_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 401),
    _PsName_Type()
)
psName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psName.setStatus("mandatory")
_ConfServ_Type = DisplayString
_ConfServ_Object = MibTableColumn
confServ = _ConfServ_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 402),
    _ConfServ_Type()
)
confServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confServ.setStatus("mandatory")


class _MsgLog_Type(Integer32):
    """Custom type msgLog based on Integer32"""
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
        *(("both", 4),
          ("console", 2),
          ("netlog", 3),
          ("none", 1))
    )


_MsgLog_Type.__name__ = "Integer32"
_MsgLog_Object = MibTableColumn
msgLog = _MsgLog_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 403),
    _MsgLog_Type()
)
msgLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgLog.setStatus("mandatory")


class _NwMode_Type(Integer32):
    """Custom type nwMode based on Integer32"""
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
        *(("both", 4),
          ("off", 1),
          ("pserver", 2),
          ("rprinter", 3))
    )


_NwMode_Type.__name__ = "Integer32"
_NwMode_Object = MibTableColumn
nwMode = _NwMode_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 404),
    _NwMode_Type()
)
nwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwMode.setStatus("mandatory")


class _PsPoll_Type(Integer32):
    """Custom type psPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PsPoll_Type.__name__ = "Integer32"
_PsPoll_Object = MibTableColumn
psPoll = _PsPoll_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 405),
    _PsPoll_Type()
)
psPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPoll.setStatus("mandatory")


class _Fr8023_Type(Integer32):
    """Custom type fr8023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Fr8023_Type.__name__ = "Integer32"
_Fr8023_Object = MibScalar
fr8023 = _Fr8023_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 420),
    _Fr8023_Type()
)
fr8023.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fr8023.setStatus("mandatory")


class _Freth2_Type(Integer32):
    """Custom type freth2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Freth2_Type.__name__ = "Integer32"
_Freth2_Object = MibScalar
freth2 = _Freth2_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 421),
    _Freth2_Type()
)
freth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    freth2.setStatus("mandatory")


class _Fr8022_Type(Integer32):
    """Custom type fr8022 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Fr8022_Type.__name__ = "Integer32"
_Fr8022_Object = MibScalar
fr8022 = _Fr8022_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 422),
    _Fr8022_Type()
)
fr8022.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fr8022.setStatus("mandatory")


class _FrSnap_Type(Integer32):
    """Custom type frSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrSnap_Type.__name__ = "Integer32"
_FrSnap_Object = MibScalar
frSnap = _FrSnap_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 423),
    _FrSnap_Type()
)
frSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSnap.setStatus("mandatory")
_Login1_Type = DisplayString
_Login1_Object = MibTableColumn
login1 = _Login1_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 432),
    _Login1_Type()
)
login1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login1.setStatus("mandatory")
_Login2_Type = DisplayString
_Login2_Object = MibTableColumn
login2 = _Login2_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 433),
    _Login2_Type()
)
login2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login2.setStatus("mandatory")
_Login3_Type = DisplayString
_Login3_Object = MibTableColumn
login3 = _Login3_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 434),
    _Login3_Type()
)
login3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login3.setStatus("mandatory")
_Login4_Type = DisplayString
_Login4_Object = MibTableColumn
login4 = _Login4_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 435),
    _Login4_Type()
)
login4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login4.setStatus("mandatory")
_Login5_Type = DisplayString
_Login5_Object = MibTableColumn
login5 = _Login5_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 436),
    _Login5_Type()
)
login5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login5.setStatus("mandatory")
_Login6_Type = DisplayString
_Login6_Object = MibTableColumn
login6 = _Login6_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 437),
    _Login6_Type()
)
login6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login6.setStatus("mandatory")
_Login7_Type = DisplayString
_Login7_Object = MibTableColumn
login7 = _Login7_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 438),
    _Login7_Type()
)
login7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login7.setStatus("mandatory")
_Login8_Type = DisplayString
_Login8_Object = MibTableColumn
login8 = _Login8_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 439),
    _Login8_Type()
)
login8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login8.setStatus("mandatory")
_Login9_Type = DisplayString
_Login9_Object = MibTableColumn
login9 = _Login9_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 440),
    _Login9_Type()
)
login9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login9.setStatus("mandatory")
_Login10_Type = DisplayString
_Login10_Object = MibTableColumn
login10 = _Login10_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 441),
    _Login10_Type()
)
login10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login10.setStatus("mandatory")
_Login11_Type = DisplayString
_Login11_Object = MibTableColumn
login11 = _Login11_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 442),
    _Login11_Type()
)
login11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login11.setStatus("mandatory")
_Login12_Type = DisplayString
_Login12_Object = MibTableColumn
login12 = _Login12_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 443),
    _Login12_Type()
)
login12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login12.setStatus("mandatory")
_Login13_Type = DisplayString
_Login13_Object = MibTableColumn
login13 = _Login13_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 444),
    _Login13_Type()
)
login13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login13.setStatus("mandatory")
_Login14_Type = DisplayString
_Login14_Object = MibTableColumn
login14 = _Login14_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 445),
    _Login14_Type()
)
login14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login14.setStatus("mandatory")
_Login15_Type = DisplayString
_Login15_Object = MibTableColumn
login15 = _Login15_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 446),
    _Login15_Type()
)
login15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login15.setStatus("mandatory")
_Login16_Type = DisplayString
_Login16_Object = MibTableColumn
login16 = _Login16_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 447),
    _Login16_Type()
)
login16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login16.setStatus("mandatory")
_Rprinter1_Type = DisplayString
_Rprinter1_Object = MibTableColumn
rprinter1 = _Rprinter1_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 470),
    _Rprinter1_Type()
)
rprinter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter1.setStatus("mandatory")
_Rprinter2_Type = DisplayString
_Rprinter2_Object = MibTableColumn
rprinter2 = _Rprinter2_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 471),
    _Rprinter2_Type()
)
rprinter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter2.setStatus("mandatory")
_Rprinter3_Type = DisplayString
_Rprinter3_Object = MibTableColumn
rprinter3 = _Rprinter3_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 472),
    _Rprinter3_Type()
)
rprinter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter3.setStatus("mandatory")
_Rprinter4_Type = DisplayString
_Rprinter4_Object = MibTableColumn
rprinter4 = _Rprinter4_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 473),
    _Rprinter4_Type()
)
rprinter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter4.setStatus("mandatory")
_Rprinter5_Type = DisplayString
_Rprinter5_Object = MibTableColumn
rprinter5 = _Rprinter5_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 474),
    _Rprinter5_Type()
)
rprinter5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter5.setStatus("mandatory")
_Rprinter6_Type = DisplayString
_Rprinter6_Object = MibTableColumn
rprinter6 = _Rprinter6_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 475),
    _Rprinter6_Type()
)
rprinter6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter6.setStatus("mandatory")
_Rprinter7_Type = DisplayString
_Rprinter7_Object = MibTableColumn
rprinter7 = _Rprinter7_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 476),
    _Rprinter7_Type()
)
rprinter7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter7.setStatus("mandatory")
_Rprinter8_Type = DisplayString
_Rprinter8_Object = MibTableColumn
rprinter8 = _Rprinter8_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 5, 477),
    _Rprinter8_Type()
)
rprinter8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprinter8.setStatus("mandatory")
_QmsIFApple_ObjectIdentity = ObjectIdentity
qmsIFApple = _QmsIFApple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6)
)


class _AtlkEnb_Type(Integer32):
    """Custom type atlkEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtlkEnb_Type.__name__ = "Integer32"
_AtlkEnb_Object = MibTableColumn
atlkEnb = _AtlkEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 500),
    _AtlkEnb_Type()
)
atlkEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkEnb.setStatus("mandatory")
_AtlkZone_Type = DisplayString
_AtlkZone_Object = MibTableColumn
atlkZone = _AtlkZone_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 502),
    _AtlkZone_Type()
)
atlkZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkZone.setStatus("mandatory")


class _AtlkZonerEnb_Type(Integer32):
    """Custom type atlkZonerEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtlkZonerEnb_Type.__name__ = "Integer32"
_AtlkZonerEnb_Object = MibTableColumn
atlkZonerEnb = _AtlkZonerEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 503),
    _AtlkZonerEnb_Type()
)
atlkZonerEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkZonerEnb.setStatus("mandatory")


class _AtlkLWEnb_Type(Integer32):
    """Custom type atlkLWEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtlkLWEnb_Type.__name__ = "Integer32"
_AtlkLWEnb_Object = MibTableColumn
atlkLWEnb = _AtlkLWEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 560),
    _AtlkLWEnb_Type()
)
atlkLWEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkLWEnb.setStatus("mandatory")


class _AtlkQMSRemConEnb_Type(Integer32):
    """Custom type atlkQMSRemConEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtlkQMSRemConEnb_Type.__name__ = "Integer32"
_AtlkQMSRemConEnb_Object = MibTableColumn
atlkQMSRemConEnb = _AtlkQMSRemConEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 561),
    _AtlkQMSRemConEnb_Type()
)
atlkQMSRemConEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkQMSRemConEnb.setStatus("mandatory")


class _AtlkConnType_Type(Integer32):
    """Custom type atlkConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("conventional", 1),
          ("spooling", 2))
    )


_AtlkConnType_Type.__name__ = "Integer32"
_AtlkConnType_Object = MibTableColumn
atlkConnType = _AtlkConnType_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 6, 562),
    _AtlkConnType_Type()
)
atlkConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atlkConnType.setStatus("mandatory")
_QmsIFSnmpcontrol_ObjectIdentity = ObjectIdentity
qmsIFSnmpcontrol = _QmsIFSnmpcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8)
)


class _EnableAuthenTraps_Type(Integer32):
    """Custom type enableAuthenTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EnableAuthenTraps_Type.__name__ = "Integer32"
_EnableAuthenTraps_Object = MibTableColumn
enableAuthenTraps = _EnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 715),
    _EnableAuthenTraps_Type()
)
enableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAuthenTraps.setStatus("mandatory")


class _EnablePrinterTraps_Type(Integer32):
    """Custom type enablePrinterTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EnablePrinterTraps_Type.__name__ = "Integer32"
_EnablePrinterTraps_Object = MibTableColumn
enablePrinterTraps = _EnablePrinterTraps_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 716),
    _EnablePrinterTraps_Type()
)
enablePrinterTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePrinterTraps.setStatus("mandatory")
_Nms1Address_Type = IpAddress
_Nms1Address_Object = MibTableColumn
nms1Address = _Nms1Address_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 730),
    _Nms1Address_Type()
)
nms1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms1Address.setStatus("mandatory")
_Nms1Community_Type = DisplayString
_Nms1Community_Object = MibTableColumn
nms1Community = _Nms1Community_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 731),
    _Nms1Community_Type()
)
nms1Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms1Community.setStatus("mandatory")


class _Nms1Access_Type(Integer32):
    """Custom type nms1Access based on Integer32"""
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
        *(("none", 1),
          ("read", 3),
          ("readtrap", 4),
          ("trap", 2),
          ("write", 5),
          ("writetrap", 6))
    )


_Nms1Access_Type.__name__ = "Integer32"
_Nms1Access_Object = MibTableColumn
nms1Access = _Nms1Access_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 732),
    _Nms1Access_Type()
)
nms1Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms1Access.setStatus("mandatory")
_Nms2Address_Type = IpAddress
_Nms2Address_Object = MibTableColumn
nms2Address = _Nms2Address_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 735),
    _Nms2Address_Type()
)
nms2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms2Address.setStatus("mandatory")
_Nms2Community_Type = DisplayString
_Nms2Community_Object = MibTableColumn
nms2Community = _Nms2Community_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 736),
    _Nms2Community_Type()
)
nms2Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms2Community.setStatus("mandatory")


class _Nms2Access_Type(Integer32):
    """Custom type nms2Access based on Integer32"""
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
        *(("none", 1),
          ("read", 3),
          ("readtrap", 4),
          ("trap", 2),
          ("write", 5),
          ("writetrap", 6))
    )


_Nms2Access_Type.__name__ = "Integer32"
_Nms2Access_Object = MibTableColumn
nms2Access = _Nms2Access_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 737),
    _Nms2Access_Type()
)
nms2Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms2Access.setStatus("mandatory")
_Nms3Address_Type = IpAddress
_Nms3Address_Object = MibTableColumn
nms3Address = _Nms3Address_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 740),
    _Nms3Address_Type()
)
nms3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms3Address.setStatus("mandatory")
_Nms3Community_Type = DisplayString
_Nms3Community_Object = MibTableColumn
nms3Community = _Nms3Community_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 741),
    _Nms3Community_Type()
)
nms3Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms3Community.setStatus("mandatory")


class _Nms3Access_Type(Integer32):
    """Custom type nms3Access based on Integer32"""
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
        *(("none", 1),
          ("read", 3),
          ("readtrap", 4),
          ("trap", 2),
          ("write", 5),
          ("writetrap", 6))
    )


_Nms3Access_Type.__name__ = "Integer32"
_Nms3Access_Object = MibTableColumn
nms3Access = _Nms3Access_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 742),
    _Nms3Access_Type()
)
nms3Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms3Access.setStatus("mandatory")
_Nms4Address_Type = IpAddress
_Nms4Address_Object = MibTableColumn
nms4Address = _Nms4Address_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 745),
    _Nms4Address_Type()
)
nms4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms4Address.setStatus("mandatory")
_Nms4Community_Type = DisplayString
_Nms4Community_Object = MibTableColumn
nms4Community = _Nms4Community_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 746),
    _Nms4Community_Type()
)
nms4Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms4Community.setStatus("mandatory")


class _Nms4Access_Type(Integer32):
    """Custom type nms4Access based on Integer32"""
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
        *(("none", 1),
          ("read", 3),
          ("readtrap", 4),
          ("trap", 2),
          ("write", 5),
          ("writetrap", 6))
    )


_Nms4Access_Type.__name__ = "Integer32"
_Nms4Access_Object = MibTableColumn
nms4Access = _Nms4Access_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 747),
    _Nms4Access_Type()
)
nms4Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms4Access.setStatus("mandatory")
_Nms5Address_Type = IpAddress
_Nms5Address_Object = MibTableColumn
nms5Address = _Nms5Address_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 750),
    _Nms5Address_Type()
)
nms5Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms5Address.setStatus("mandatory")
_Nms5Community_Type = DisplayString
_Nms5Community_Object = MibTableColumn
nms5Community = _Nms5Community_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 751),
    _Nms5Community_Type()
)
nms5Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms5Community.setStatus("mandatory")


class _Nms5Access_Type(Integer32):
    """Custom type nms5Access based on Integer32"""
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
        *(("none", 1),
          ("read", 3),
          ("readtrap", 4),
          ("trap", 2),
          ("write", 5),
          ("writetrap", 6))
    )


_Nms5Access_Type.__name__ = "Integer32"
_Nms5Access_Object = MibTableColumn
nms5Access = _Nms5Access_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 8, 752),
    _Nms5Access_Type()
)
nms5Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms5Access.setStatus("mandatory")
_QmsIFLservlmgr_ObjectIdentity = ObjectIdentity
qmsIFLservlmgr = _QmsIFLservlmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 9)
)


class _LslmEnb_Type(Integer32):
    """Custom type lslmEnb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LslmEnb_Type.__name__ = "Integer32"
_LslmEnb_Object = MibTableColumn
lslmEnb = _LslmEnb_Object(
    (1, 3, 6, 1, 4, 1, 480, 2, 9, 2, 9, 800),
    _LslmEnb_Type()
)
lslmEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lslmEnb.setStatus("mandatory")
_QmsConfig_ObjectIdentity = ObjectIdentity
qmsConfig = _QmsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 10)
)
_QmsCfgUser_ObjectIdentity = ObjectIdentity
qmsCfgUser = _QmsCfgUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 10, 10)
)
_QmsCfgAdmin_ObjectIdentity = ObjectIdentity
qmsCfgAdmin = _QmsCfgAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 10, 20)
)
_QmsCfgSecurity_ObjectIdentity = ObjectIdentity
qmsCfgSecurity = _QmsCfgSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 480, 2, 10, 30)
)

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

qmsPtrErrorMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 480, 0, 1)
)
qmsPtrErrorMsg.setObjects(
    ("QMS-MIB", "qmsPtrSysStatus")
)
if mibBuilder.loadTexts:
    qmsPtrErrorMsg.setStatus(
        ""
    )

trapNewIPaddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 480, 0, 2)
)
trapNewIPaddr.setObjects(
    ("QMS-MIB", "qmsIFAdminOldIntAddr")
)
if mibBuilder.loadTexts:
    trapNewIPaddr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QMS-MIB",
    **{"coldStart": coldStart,
       "authenticationFailure": authenticationFailure,
       "qmsInc": qmsInc,
       "qmsPtrErrorMsg": qmsPtrErrorMsg,
       "trapNewIPaddr": trapNewIPaddr,
       "qmsUIH": qmsUIH,
       "qmsSystem": qmsSystem,
       "qmsSYSPageCount": qmsSYSPageCount,
       "qmsSYSSheetCount": qmsSYSSheetCount,
       "qmsSYSPrinterModel": qmsSYSPrinterModel,
       "qmsSYSPrinterVersion": qmsSYSPrinterVersion,
       "qmsSYSPrinterName": qmsSYSPrinterName,
       "qmsSYSA3PageCount": qmsSYSA3PageCount,
       "qmsSYSA3SheetCount": qmsSYSA3SheetCount,
       "qmsSYSFPA": qmsSYSFPA,
       "qmsSYSSystemImage": qmsSYSSystemImage,
       "qmsSYSDiskSwap": qmsSYSDiskSwap,
       "qmsSYSMultiRes": qmsSYSMultiRes,
       "qmsMemory": qmsMemory,
       "qmsMEMPhysical": qmsMEMPhysical,
       "qmsMEMTotal": qmsMEMTotal,
       "qmsClientSystem": qmsClientSystem,
       "qmsClientSpool": qmsClientSpool,
       "qmsClientEmulation": qmsClientEmulation,
       "qmsClientHeap": qmsClientHeap,
       "qmsClientFontCache": qmsClientFontCache,
       "qmsClientDisplayList": qmsClientDisplayList,
       "qmsClientFrameBuffer": qmsClientFrameBuffer,
       "qmsClientEmulTemp": qmsClientEmulTemp,
       "qmsClientDisk": qmsClientDisk,
       "qmsClientColorMatching": qmsClientColorMatching,
       "qmsClientHPStoragePool": qmsClientHPStoragePool,
       "qmsIoCtl": qmsIoCtl,
       "qmsFEEspEmul": qmsFEEspEmul,
       "qmsFECopies": qmsFECopies,
       "qmsHTTP": qmsHTTP,
       "qmsHTTPContact": qmsHTTPContact,
       "qmsHTTPHelpURL": qmsHTTPHelpURL,
       "qmsHTTPContactNumber": qmsHTTPContactNumber,
       "qmsHTTPCorpURL": qmsHTTPCorpURL,
       "qmsHTTPSuppliesNumber": qmsHTTPSuppliesNumber,
       "qmsIoTimeOuts": qmsIoTimeOuts,
       "qmsFETmPSWait": qmsFETmPSWait,
       "qmsFETmJob": qmsFETmJob,
       "qmsFETmNonPSEmul": qmsFETmNonPSEmul,
       "qmsFETmEsp": qmsFETmEsp,
       "qmsIoPages": qmsIoPages,
       "qmsFEDoStartPage": qmsFEDoStartPage,
       "qmsFEHeaderPage": qmsFEHeaderPage,
       "qmsFEHeaderInputbin": qmsFEHeaderInputbin,
       "qmsFETrailerPage": qmsFETrailerPage,
       "qmsFETrailerInputbin": qmsFETrailerInputbin,
       "qmsFEDoSysStart": qmsFEDoSysStart,
       "qmsFEStatusPageType": qmsFEStatusPageType,
       "qmsSerial": qmsSerial,
       "qmsSerPSProtocol": qmsSerPSProtocol,
       "qmsSerMode": qmsSerMode,
       "qmsSerEmulation": qmsSerEmulation,
       "qmsSerPriority": qmsSerPriority,
       "qmsSerBufferSize": qmsSerBufferSize,
       "qmsSerEndDocumentMode": qmsSerEndDocumentMode,
       "qmsSerSpoolTimeout": qmsSerSpoolTimeout,
       "qmsSerBaudRate": qmsSerBaudRate,
       "qmsSerParity": qmsSerParity,
       "qmsSerIgnoreParity": qmsSerIgnoreParity,
       "qmsSerRxSWFlow": qmsSerRxSWFlow,
       "qmsSerTxSWFlow": qmsSerTxSWFlow,
       "qmsSerDataBits": qmsSerDataBits,
       "qmsSerStopBits": qmsSerStopBits,
       "qmsSerHwCTS": qmsSerHwCTS,
       "qmsSerHwRTS": qmsSerHwRTS,
       "qmsSerHwDTR": qmsSerHwDTR,
       "qmsSerHwDTRPOL": qmsSerHwDTRPOL,
       "qmsSerHwDSR": qmsSerHwDSR,
       "qmsSerHwDSRPOL": qmsSerHwDSRPOL,
       "qmsParallel": qmsParallel,
       "qmsParPSProtocol": qmsParPSProtocol,
       "qmsParMode": qmsParMode,
       "qmsParEmulation": qmsParEmulation,
       "qmsParPriority": qmsParPriority,
       "qmsParBufferSize": qmsParBufferSize,
       "qmsParSpoolTimeout": qmsParSpoolTimeout,
       "qmsParEndDocumentMode": qmsParEndDocumentMode,
       "qmsParDataBits": qmsParDataBits,
       "qmsEngine": qmsEngine,
       "qmsENGTopOffset": qmsENGTopOffset,
       "qmsENGLeftOffset": qmsENGLeftOffset,
       "qmsENGTopOffsetDuplex": qmsENGTopOffsetDuplex,
       "qmsENGLeftOffsetDuplex": qmsENGLeftOffsetDuplex,
       "qmsENGResolution": qmsENGResolution,
       "qmsENGDefaultPaper": qmsENGDefaultPaper,
       "qmsENGDuplex": qmsENGDuplex,
       "qmsENGOrientation": qmsENGOrientation,
       "qmsENGInputbin": qmsENGInputbin,
       "qmsENGOutputbin": qmsENGOutputbin,
       "qmsENGCollation": qmsENGCollation,
       "qmsENGErrorRecovery": qmsENGErrorRecovery,
       "qmsENGManualTrayMedia": qmsENGManualTrayMedia,
       "qmsENGToneroutAction": qmsENGToneroutAction,
       "qmsENGLetterheadMode": qmsENGLetterheadMode,
       "qmsENGManualFeedTimeout": qmsENGManualFeedTimeout,
       "qmsENGOffsetStacking": qmsENGOffsetStacking,
       "qmsENGEnergyStar": qmsENGEnergyStar,
       "qmsENGPageOrder": qmsENGPageOrder,
       "qmsENGEnvelopeTrayMedia": qmsENGEnvelopeTrayMedia,
       "qmsENGDensity": qmsENGDensity,
       "qmsENGColorModel": qmsENGColorModel,
       "qmsENGColorSeparation": qmsENGColorSeparation,
       "qmsENGUnderColor": qmsENGUnderColor,
       "qmsENGQuality": qmsENGQuality,
       "qmsENGConsumeNameMulti": qmsENGConsumeNameMulti,
       "qmsENGConsumeName": qmsENGConsumeName,
       "qmsENGConsumeLevelMulti": qmsENGConsumeLevelMulti,
       "qmsENGConsumeLevel": qmsENGConsumeLevel,
       "qmsENGConsumeMaxMulti": qmsENGConsumeMaxMulti,
       "qmsENGConsumeMax": qmsENGConsumeMax,
       "qmsENGConsumeUnitsMulti": qmsENGConsumeUnitsMulti,
       "qmsENGConsumeUnits": qmsENGConsumeUnits,
       "qmsENGConsumeTypeMulti": qmsENGConsumeTypeMulti,
       "qmsENGConsumeType": qmsENGConsumeType,
       "qmsENGConsumeNote1Multi": qmsENGConsumeNote1Multi,
       "qmsENGConsumeNote1": qmsENGConsumeNote1,
       "qmsENGConsumeNote2Multi": qmsENGConsumeNote2Multi,
       "qmsENGConsumeNote2": qmsENGConsumeNote2,
       "qmsENGConsumeIndexMulti": qmsENGConsumeIndexMulti,
       "qmsENGConsumeIndex": qmsENGConsumeIndex,
       "qmsENGNumConsumables": qmsENGNumConsumables,
       "qmsENGChainInputBins": qmsENGChainInputBins,
       "qmsENGChainOutputbinMulti": qmsENGChainOutputbinMulti,
       "qmsENGChainOutputbin": qmsENGChainOutputbin,
       "qmsENGInputbinMediatypeMulti": qmsENGInputbinMediatypeMulti,
       "qmsENGInputbinMediatype": qmsENGInputbinMediatype,
       "qmsENGChainInputbinMulti": qmsENGChainInputbinMulti,
       "qmsENGChainInputbin": qmsENGChainInputbin,
       "qmsENGStaplePosition": qmsENGStaplePosition,
       "qmsAccounting": qmsAccounting,
       "qmsACCMode": qmsACCMode,
       "qmsACCDiskSpace": qmsACCDiskSpace,
       "qmsACCFileSegment": qmsACCFileSegment,
       "qmsScanner": qmsScanner,
       "qmsSCColorAdjust": qmsSCColorAdjust,
       "qmsSCScanResolution": qmsSCScanResolution,
       "qmsSCSizeHorizontal": qmsSCSizeHorizontal,
       "qmsSCSizeVertical": qmsSCSizeVertical,
       "qmsSCOffsetHorizontal": qmsSCOffsetHorizontal,
       "qmsSCOffsetVertical": qmsSCOffsetVertical,
       "qmsSCCopyMode": qmsSCCopyMode,
       "qmsSCRedGammaFunction": qmsSCRedGammaFunction,
       "qmsSCGreenGammaFunction": qmsSCGreenGammaFunction,
       "qmsSCBlueGammaFunction": qmsSCBlueGammaFunction,
       "qmsSCGrayGammaFunction": qmsSCGrayGammaFunction,
       "qmsSCBinaryAdjustment": qmsSCBinaryAdjustment,
       "qmsSCTrans": qmsSCTrans,
       "qmsSCContrast": qmsSCContrast,
       "qmsCostPerPage": qmsCostPerPage,
       "qmsCPPSerialNumber": qmsCPPSerialNumber,
       "qmsColorMatch": qmsColorMatch,
       "qmsCMMICCColorMatch": qmsCMMICCColorMatch,
       "qmsCMMICCRGBSource": qmsCMMICCRGBSource,
       "qmsCMMICCSimulation": qmsCMMICCSimulation,
       "qmsCMMICCDestination": qmsCMMICCDestination,
       "qmsCMMLinkQuality": qmsCMMLinkQuality,
       "qmsCMMSimInRGBLinks": qmsCMMSimInRGBLinks,
       "qmsCMMICCHP": qmsCMMICCHP,
       "qmsCMMProfileTable": qmsCMMProfileTable,
       "qmsCMMProfileEntry": qmsCMMProfileEntry,
       "qmsCMMProfileIndex": qmsCMMProfileIndex,
       "qmsCMMProfileDescription": qmsCMMProfileDescription,
       "qmsCMMProfileType": qmsCMMProfileType,
       "qmsPS": qmsPS,
       "qmsPSErrorHandler": qmsPSErrorHandler,
       "qmsPSOutputPositioning": qmsPSOutputPositioning,
       "qmsPSDefaultHalftone": qmsPSDefaultHalftone,
       "qmsPSDefaultBlackOverPrint": qmsPSDefaultBlackOverPrint,
       "qmsPSDefaultCRD": qmsPSDefaultCRD,
       "qmsPSDefaultDither": qmsPSDefaultDither,
       "qmsPSDefaultGamma": qmsPSDefaultGamma,
       "qmsPSIntensity": qmsPSIntensity,
       "qmsHPGL": qmsHPGL,
       "qmsHPGLPaperType": qmsHPGLPaperType,
       "qmsHPGLPlotter": qmsHPGLPlotter,
       "qmsHPGLScalingPercent": qmsHPGLScalingPercent,
       "qmsHPGLEnhancedMode": qmsHPGLEnhancedMode,
       "qmsHPGLExpandMode": qmsHPGLExpandMode,
       "qmsHPGLPenWidth1": qmsHPGLPenWidth1,
       "qmsHPGLPenWidth2": qmsHPGLPenWidth2,
       "qmsHPGLPenWidth3": qmsHPGLPenWidth3,
       "qmsHPGLPenWidth4": qmsHPGLPenWidth4,
       "qmsHPGLPenWidth5": qmsHPGLPenWidth5,
       "qmsHPGLPenWidth6": qmsHPGLPenWidth6,
       "qmsHPGLPenWidth7": qmsHPGLPenWidth7,
       "qmsHPGLPenWidth8": qmsHPGLPenWidth8,
       "qmsHPGLPenColor1": qmsHPGLPenColor1,
       "qmsHPGLPenColor2": qmsHPGLPenColor2,
       "qmsHPGLPenColor3": qmsHPGLPenColor3,
       "qmsHPGLPenColor4": qmsHPGLPenColor4,
       "qmsHPGLPenColor5": qmsHPGLPenColor5,
       "qmsHPGLPenColor6": qmsHPGLPenColor6,
       "qmsHPGLPenColor7": qmsHPGLPenColor7,
       "qmsHPGLPenColor8": qmsHPGLPenColor8,
       "qmsHPPCL": qmsHPPCL,
       "qmsHPPCLLineTermination": qmsHPPCLLineTermination,
       "qmsHPPCLFontNumber": qmsHPPCLFontNumber,
       "qmsHPPCLLinesPerInch": qmsHPPCLLinesPerInch,
       "qmsHPPCLDefaultSymbolSet": qmsHPPCLDefaultSymbolSet,
       "qmsHPPCLPreJobReset": qmsHPPCLPreJobReset,
       "qmsHPPCLPointSize": qmsHPPCLPointSize,
       "qmsHPPCLDefaultFontID": qmsHPPCLDefaultFontID,
       "qmsHPPCLGL2Plotter": qmsHPPCLGL2Plotter,
       "qmsHPPCLDiskOrRam": qmsHPPCLDiskOrRam,
       "qmsDECLN03": qmsDECLN03,
       "qmsDECLN03ProductID": qmsDECLN03ProductID,
       "qmsDECLN03AutowrapMode": qmsDECLN03AutowrapMode,
       "qmsDECLN03PaperSize": qmsDECLN03PaperSize,
       "qmsDECLN03PaperSizeOverride": qmsDECLN03PaperSizeOverride,
       "qmsDECLN03Xorigin": qmsDECLN03Xorigin,
       "qmsDECLN03Yorigin": qmsDECLN03Yorigin,
       "qmsDECLN03Reset": qmsDECLN03Reset,
       "qmsDECLN03Orientation": qmsDECLN03Orientation,
       "qmsQUIC2": qmsQUIC2,
       "qmsQUIC2CommandCharacter": qmsQUIC2CommandCharacter,
       "qmsQUIC2TopMargin": qmsQUIC2TopMargin,
       "qmsQUIC2BottomMargin": qmsQUIC2BottomMargin,
       "qmsQUIC2LeftMargin": qmsQUIC2LeftMargin,
       "qmsQUIC2RightMargin": qmsQUIC2RightMargin,
       "qmsQUIC2IfParam": qmsQUIC2IfParam,
       "qmsQUIC2CReqCRLF": qmsQUIC2CReqCRLF,
       "qmsQUIC2LFeqLFCR": qmsQUIC2LFeqLFCR,
       "qmsQUIC2Decimal": qmsQUIC2Decimal,
       "qmsQUIC2Dimensions": qmsQUIC2Dimensions,
       "qmsQUIC2EDPMode": qmsQUIC2EDPMode,
       "qmsQUIC2DefaultFont": qmsQUIC2DefaultFont,
       "qmsQUIC2LineSpacing": qmsQUIC2LineSpacing,
       "qmsQUIC2Orientation": qmsQUIC2Orientation,
       "qmsQUIC2Scan": qmsQUIC2Scan,
       "qmsQUIC2Spaces": qmsQUIC2Spaces,
       "qmsQUIC2AllowDataRepeats": qmsQUIC2AllowDataRepeats,
       "qmsQUIC2AllowOverlays": qmsQUIC2AllowOverlays,
       "qmsQUIC2AllowPageCopies": qmsQUIC2AllowPageCopies,
       "qmsQUIC2SaveDLF": qmsQUIC2SaveDLF,
       "qmsQUIC2SaveOverlays": qmsQUIC2SaveOverlays,
       "qmsQUIC2DefaultMode": qmsQUIC2DefaultMode,
       "qmsQUIC2RebuildFontTable": qmsQUIC2RebuildFontTable,
       "qmsQUIC2TrayMap1": qmsQUIC2TrayMap1,
       "qmsQUIC2TrayMap2": qmsQUIC2TrayMap2,
       "qmsQUIC2TrayMap3": qmsQUIC2TrayMap3,
       "qmsQUIC2TrayMap4": qmsQUIC2TrayMap4,
       "qmsQUIC2TrayMap5": qmsQUIC2TrayMap5,
       "qmsQUIC2PatternType": qmsQUIC2PatternType,
       "qmsCCITT": qmsCCITT,
       "qmsLinePrinter": qmsLinePrinter,
       "qmsLPPointSize": qmsLPPointSize,
       "qmsLPTabStops": qmsLPTabStops,
       "qmsLPLinesPerPage": qmsLPLinesPerPage,
       "qmsLPLeftMargin": qmsLPLeftMargin,
       "qmsLPRightMargin": qmsLPRightMargin,
       "qmsLPTopMargin": qmsLPTopMargin,
       "qmsLPBottomMargin": qmsLPBottomMargin,
       "qmsLPAsciiMap": qmsLPAsciiMap,
       "qmsLPLineNumbering": qmsLPLineNumbering,
       "qmsLPLFisCRLF": qmsLPLFisCRLF,
       "qmsLPCRisCRLF": qmsLPCRisCRLF,
       "qmsLPFFisCRFF": qmsLPFFisCRFF,
       "qmsLPOrientation": qmsLPOrientation,
       "qmsLPLineWrap": qmsLPLineWrap,
       "qmsLPFont": qmsLPFont,
       "qmsTIFF": qmsTIFF,
       "qmsTIFFAutoRotation": qmsTIFFAutoRotation,
       "qmsTIFFScratchFileSize": qmsTIFFScratchFileSize,
       "qmsTIFFPaperToImage": qmsTIFFPaperToImage,
       "qmsTIFFAnnotationState": qmsTIFFAnnotationState,
       "qmsTIFFAnnotationTag": qmsTIFFAnnotationTag,
       "qmsTIFFReverseImage": qmsTIFFReverseImage,
       "qmsTIFFAutoScaling": qmsTIFFAutoScaling,
       "qmsCALS": qmsCALS,
       "qmsCALSAutoRotation": qmsCALSAutoRotation,
       "qmsCALSAutoScaling": qmsCALSAutoScaling,
       "qmsCGM": qmsCGM,
       "qmsCGMSuppressScale": qmsCGMSuppressScale,
       "qmsCGMMono": qmsCGMMono,
       "qmsCGMIgnoreBorder": qmsCGMIgnoreBorder,
       "qmsCGMOriginX": qmsCGMOriginX,
       "qmsCGMOriginY": qmsCGMOriginY,
       "qmsCGMPrintErrors": qmsCGMPrintErrors,
       "qmsRel": qmsRel,
       "qmsPrinter": qmsPrinter,
       "qmsPtrSys": qmsPtrSys,
       "qmsPtrSysStatus": qmsPtrSysStatus,
       "qmsPtrSysNamePrinter": qmsPtrSysNamePrinter,
       "qmsPtrIfTable": qmsPtrIfTable,
       "qmsPtrIfEntry": qmsPtrIfEntry,
       "qmsPtrIfIndex": qmsPtrIfIndex,
       "qmsPtrIfName": qmsPtrIfName,
       "qmsPtrIfDefEmu": qmsPtrIfDefEmu,
       "qmsPtrBinTable": qmsPtrBinTable,
       "qmsPtrBinEntry": qmsPtrBinEntry,
       "qmsPtrBinIndex": qmsPtrBinIndex,
       "qmsPtrBinType": qmsPtrBinType,
       "qmsPtrBinId": qmsPtrBinId,
       "qmsPtrBinPaper": qmsPtrBinPaper,
       "qmsPtrBinName": qmsPtrBinName,
       "qmsPtrEmu": qmsPtrEmu,
       "qmsPtrJobs": qmsPtrJobs,
       "qmsPtrJobsCurStatus": qmsPtrJobsCurStatus,
       "qmsPtrJobsCurSheet": qmsPtrJobsCurSheet,
       "qmsPtrJobsCurPage": qmsPtrJobsCurPage,
       "qmsPtrJobsTable": qmsPtrJobsTable,
       "qmsPtrJobsEntry": qmsPtrJobsEntry,
       "qmsPtrJobsIndex": qmsPtrJobsIndex,
       "qmsPtrJobsStatus": qmsPtrJobsStatus,
       "qmsPtrJobsEmulation": qmsPtrJobsEmulation,
       "qmsPtrJobsPage": qmsPtrJobsPage,
       "qmsPtrJobsSheet": qmsPtrJobsSheet,
       "qmsPtrJobsChannel": qmsPtrJobsChannel,
       "qmsPtrJobsComment": qmsPtrJobsComment,
       "qmsPtrJobsTitle": qmsPtrJobsTitle,
       "qmsPtrJobsOwner": qmsPtrJobsOwner,
       "qmsPtrJobsStatPages": qmsPtrJobsStatPages,
       "qmsPtrJobsStatSheets": qmsPtrJobsStatSheets,
       "qmsIF": qmsIF,
       "qmsIFAdmin": qmsIFAdmin,
       "qmsIFAdminUnitStatus": qmsIFAdminUnitStatus,
       "qmsIFAdminConfigStatus": qmsIFAdminConfigStatus,
       "qmsIFAdminOldIntAddr": qmsIFAdminOldIntAddr,
       "qmsIFSetup": qmsIFSetup,
       "qmsIFConfig": qmsIFConfig,
       "intAddr": intAddr,
       "ethAddr": ethAddr,
       "defRout": defRout,
       "netMask": netMask,
       "tcpEnb": tcpEnb,
       "tftpEnb": tftpEnb,
       "tnPort": tnPort,
       "rtnOpt": rtnOpt,
       "trP1": trP1,
       "bootP": bootP,
       "rarp": rarp,
       "spooling": spooling,
       "qmsIFNetware": qmsIFNetware,
       "netwEnb": netwEnb,
       "psName": psName,
       "confServ": confServ,
       "msgLog": msgLog,
       "nwMode": nwMode,
       "psPoll": psPoll,
       "fr8023": fr8023,
       "freth2": freth2,
       "fr8022": fr8022,
       "frSnap": frSnap,
       "login1": login1,
       "login2": login2,
       "login3": login3,
       "login4": login4,
       "login5": login5,
       "login6": login6,
       "login7": login7,
       "login8": login8,
       "login9": login9,
       "login10": login10,
       "login11": login11,
       "login12": login12,
       "login13": login13,
       "login14": login14,
       "login15": login15,
       "login16": login16,
       "rprinter1": rprinter1,
       "rprinter2": rprinter2,
       "rprinter3": rprinter3,
       "rprinter4": rprinter4,
       "rprinter5": rprinter5,
       "rprinter6": rprinter6,
       "rprinter7": rprinter7,
       "rprinter8": rprinter8,
       "qmsIFApple": qmsIFApple,
       "atlkEnb": atlkEnb,
       "atlkZone": atlkZone,
       "atlkZonerEnb": atlkZonerEnb,
       "atlkLWEnb": atlkLWEnb,
       "atlkQMSRemConEnb": atlkQMSRemConEnb,
       "atlkConnType": atlkConnType,
       "qmsIFSnmpcontrol": qmsIFSnmpcontrol,
       "enableAuthenTraps": enableAuthenTraps,
       "enablePrinterTraps": enablePrinterTraps,
       "nms1Address": nms1Address,
       "nms1Community": nms1Community,
       "nms1Access": nms1Access,
       "nms2Address": nms2Address,
       "nms2Community": nms2Community,
       "nms2Access": nms2Access,
       "nms3Address": nms3Address,
       "nms3Community": nms3Community,
       "nms3Access": nms3Access,
       "nms4Address": nms4Address,
       "nms4Community": nms4Community,
       "nms4Access": nms4Access,
       "nms5Address": nms5Address,
       "nms5Community": nms5Community,
       "nms5Access": nms5Access,
       "qmsIFLservlmgr": qmsIFLservlmgr,
       "lslmEnb": lslmEnb,
       "qmsConfig": qmsConfig,
       "qmsCfgUser": qmsCfgUser,
       "qmsCfgAdmin": qmsCfgAdmin,
       "qmsCfgSecurity": qmsCfgSecurity}
)
