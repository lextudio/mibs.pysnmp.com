# SNMP MIB module (MC2350-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MC2350-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:39 2024
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class CodedCharSet(Integer32, TextualConvention):
    status = "mandatory"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )



# MIB Managed Objects in the order of their OIDs

_Minolta_ObjectIdentity = ObjectIdentity
minolta = _Minolta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590)
)
_MltMgmt_ObjectIdentity = ObjectIdentity
mltMgmt = _MltMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1)
)
_MltMib_ObjectIdentity = ObjectIdentity
mltMib = _MltMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1)
)
_MltSystem_ObjectIdentity = ObjectIdentity
mltSystem = _MltSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1)
)
_MltPrinter_ObjectIdentity = ObjectIdentity
mltPrinter = _MltPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1)
)
_MltPrinterMib_ObjectIdentity = ObjectIdentity
mltPrinterMib = _MltPrinterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6)
)
_MltPrtMibInfo_ObjectIdentity = ObjectIdentity
mltPrtMibInfo = _MltPrtMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 1)
)


class _MltPrtMibVersion_Type(DisplayString):
    """Custom type mltPrtMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MltPrtMibVersion_Type.__name__ = "DisplayString"
_MltPrtMibVersion_Object = MibScalar
mltPrtMibVersion = _MltPrtMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 1, 1),
    _MltPrtMibVersion_Type()
)
mltPrtMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtMibVersion.setStatus("mandatory")
_MltPrtCommand_ObjectIdentity = ObjectIdentity
mltPrtCommand = _MltPrtCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4)
)
_MltPrtCommandTable_Object = MibTable
mltPrtCommandTable = _MltPrtCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mltPrtCommandTable.setStatus("mandatory")
_MltPrtCommandEntry_Object = MibTableRow
mltPrtCommandEntry = _MltPrtCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 1, 1)
)
mltPrtCommandEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    mltPrtCommandEntry.setStatus("mandatory")


class _MltPrtCommandOnline_Type(Integer32):
    """Custom type mltPrtCommandOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("offLine", 2),
          ("onLine", 1))
    )


_MltPrtCommandOnline_Type.__name__ = "Integer32"
_MltPrtCommandOnline_Object = MibTableColumn
mltPrtCommandOnline = _MltPrtCommandOnline_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 1, 1, 1),
    _MltPrtCommandOnline_Type()
)
mltPrtCommandOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtCommandOnline.setStatus("mandatory")


class _MltPrtCommandJobCancel_Type(Integer32):
    """Custom type mltPrtCommandJobCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jobCancel", 2),
          ("notCancel", 1),
          ("notSupported", 0))
    )


_MltPrtCommandJobCancel_Type.__name__ = "Integer32"
_MltPrtCommandJobCancel_Object = MibTableColumn
mltPrtCommandJobCancel = _MltPrtCommandJobCancel_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 1, 1, 2),
    _MltPrtCommandJobCancel_Type()
)
mltPrtCommandJobCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtCommandJobCancel.setStatus("mandatory")


class _MltPrtCommandJobProceed_Type(Integer32):
    """Custom type mltPrtCommandJobProceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jobProceed", 2),
          ("notProceed", 1),
          ("notSupported", 0))
    )


_MltPrtCommandJobProceed_Type.__name__ = "Integer32"
_MltPrtCommandJobProceed_Object = MibTableColumn
mltPrtCommandJobProceed = _MltPrtCommandJobProceed_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 1, 1, 3),
    _MltPrtCommandJobProceed_Type()
)
mltPrtCommandJobProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtCommandJobProceed.setStatus("mandatory")
_MltPrtPrintPageTable_Object = MibTable
mltPrtPrintPageTable = _MltPrtPrintPageTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    mltPrtPrintPageTable.setStatus("mandatory")
_MltPrtPrintPageEntry_Object = MibTableRow
mltPrtPrintPageEntry = _MltPrtPrintPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 2, 1)
)
mltPrtPrintPageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPrtPrintPageIndex"),
)
if mibBuilder.loadTexts:
    mltPrtPrintPageEntry.setStatus("mandatory")


class _MltPrtPrintPageIndex_Type(Integer32):
    """Custom type mltPrtPrintPageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MltPrtPrintPageIndex_Type.__name__ = "Integer32"
_MltPrtPrintPageIndex_Object = MibTableColumn
mltPrtPrintPageIndex = _MltPrtPrintPageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 2, 1, 1),
    _MltPrtPrintPageIndex_Type()
)
mltPrtPrintPageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPrintPageIndex.setStatus("mandatory")


class _MltPrtPrintPageName_Type(DisplayString):
    """Custom type mltPrtPrintPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltPrtPrintPageName_Type.__name__ = "DisplayString"
_MltPrtPrintPageName_Object = MibTableColumn
mltPrtPrintPageName = _MltPrtPrintPageName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 2, 1, 2),
    _MltPrtPrintPageName_Type()
)
mltPrtPrintPageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPrintPageName.setStatus("mandatory")


class _MltPrtPrintCommand_Type(Integer32):
    """Custom type mltPrtPrintCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("print", 2),
          ("supported", 1))
    )


_MltPrtPrintCommand_Type.__name__ = "Integer32"
_MltPrtPrintCommand_Object = MibTableColumn
mltPrtPrintCommand = _MltPrtPrintCommand_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 4, 2, 1, 3),
    _MltPrtPrintCommand_Type()
)
mltPrtPrintCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPrintCommand.setStatus("mandatory")
_MltPrtConfig_ObjectIdentity = ObjectIdentity
mltPrtConfig = _MltPrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5)
)
_MltPrtSysConfigTable_Object = MibTable
mltPrtSysConfigTable = _MltPrtSysConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mltPrtSysConfigTable.setStatus("mandatory")
_MltPrtSysConfigEntry_Object = MibTableRow
mltPrtSysConfigEntry = _MltPrtSysConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1)
)
mltPrtSysConfigEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    mltPrtSysConfigEntry.setStatus("mandatory")


class _MltPrtJobLanguage_Type(Integer32):
    """Custom type mltPrtJobLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("gdi", 3),
          ("linePrinter", 4),
          ("other", 7),
          ("pcl", 1),
          ("ps", 2))
    )


_MltPrtJobLanguage_Type.__name__ = "Integer32"
_MltPrtJobLanguage_Object = MibTableColumn
mltPrtJobLanguage = _MltPrtJobLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1, 1),
    _MltPrtJobLanguage_Type()
)
mltPrtJobLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtJobLanguage.setStatus("mandatory")
_MltPrtPowerSave_Type = Integer32
_MltPrtPowerSave_Object = MibTableColumn
mltPrtPowerSave = _MltPrtPowerSave_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1, 2),
    _MltPrtPowerSave_Type()
)
mltPrtPowerSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPowerSave.setStatus("mandatory")


class _MltPrtAutoContinue_Type(Integer32):
    """Custom type mltPrtAutoContinue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("ac0Sec", 2),
          ("ac10Sec", 3),
          ("ac120Sec", 8),
          ("ac20Sec", 4),
          ("ac30Sec", 5),
          ("ac60Sec", 6),
          ("ac90Sec", 7),
          ("notSupported", 0),
          ("off", 1))
    )


_MltPrtAutoContinue_Type.__name__ = "Integer32"
_MltPrtAutoContinue_Object = MibTableColumn
mltPrtAutoContinue = _MltPrtAutoContinue_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1, 3),
    _MltPrtAutoContinue_Type()
)
mltPrtAutoContinue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtAutoContinue.setStatus("mandatory")


class _MltPrtPaperTimeOut_Type(Integer32):
    """Custom type mltPrtPaperTimeOut based on Integer32"""
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
        *(("cancelJob", 3),
          ("notSupported", 0),
          ("off", 1),
          ("proceedJob", 2))
    )


_MltPrtPaperTimeOut_Type.__name__ = "Integer32"
_MltPrtPaperTimeOut_Object = MibTableColumn
mltPrtPaperTimeOut = _MltPrtPaperTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1, 4),
    _MltPrtPaperTimeOut_Type()
)
mltPrtPaperTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPaperTimeOut.setStatus("mandatory")


class _MltPrtPsErrorPrint_Type(Integer32):
    """Custom type mltPrtPsErrorPrint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("off", 1),
          ("on", 2))
    )


_MltPrtPsErrorPrint_Type.__name__ = "Integer32"
_MltPrtPsErrorPrint_Object = MibTableColumn
mltPrtPsErrorPrint = _MltPrtPsErrorPrint_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 1, 1, 5),
    _MltPrtPsErrorPrint_Type()
)
mltPrtPsErrorPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPsErrorPrint.setStatus("mandatory")
_MltPrtPrintConfigTable_Object = MibTable
mltPrtPrintConfigTable = _MltPrtPrintConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    mltPrtPrintConfigTable.setStatus("mandatory")
_MltPrtPrintConfigEntry_Object = MibTableRow
mltPrtPrintConfigEntry = _MltPrtPrintConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1)
)
mltPrtPrintConfigEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    mltPrtPrintConfigEntry.setStatus("mandatory")
_MltPrtCopies_Type = Integer32
_MltPrtCopies_Object = MibTableColumn
mltPrtCopies = _MltPrtCopies_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1, 1),
    _MltPrtCopies_Type()
)
mltPrtCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtCopies.setStatus("mandatory")
_MltPrtPaperSize_Type = Integer32
_MltPrtPaperSize_Object = MibTableColumn
mltPrtPaperSize = _MltPrtPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1, 2),
    _MltPrtPaperSize_Type()
)
mltPrtPaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPaperSize.setStatus("mandatory")
_MltPrtPaperSource_Type = Integer32
_MltPrtPaperSource_Object = MibTableColumn
mltPrtPaperSource = _MltPrtPaperSource_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1, 3),
    _MltPrtPaperSource_Type()
)
mltPrtPaperSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPaperSource.setStatus("mandatory")


class _MltPrtFineArt_Type(Integer32):
    """Custom type mltPrtFineArt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dark", 3),
          ("light", 5),
          ("medium", 4),
          ("notSupported", 0),
          ("offStep", 6),
          ("offSwitch", 2),
          ("on", 1))
    )


_MltPrtFineArt_Type.__name__ = "Integer32"
_MltPrtFineArt_Object = MibTableColumn
mltPrtFineArt = _MltPrtFineArt_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1, 4),
    _MltPrtFineArt_Type()
)
mltPrtFineArt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtFineArt.setStatus("mandatory")


class _MltPrtTonerSave_Type(Integer32):
    """Custom type mltPrtTonerSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("off", 2),
          ("on", 1))
    )


_MltPrtTonerSave_Type.__name__ = "Integer32"
_MltPrtTonerSave_Object = MibTableColumn
mltPrtTonerSave = _MltPrtTonerSave_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 5, 2, 1, 5),
    _MltPrtTonerSave_Type()
)
mltPrtTonerSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtTonerSave.setStatus("mandatory")
_MltPrtFont_ObjectIdentity = ObjectIdentity
mltPrtFont = _MltPrtFont_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6)
)
_MltPrtPclFontTable_Object = MibTable
mltPrtPclFontTable = _MltPrtPclFontTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mltPrtPclFontTable.setStatus("mandatory")
_MltPrtPclFontEntry_Object = MibTableRow
mltPrtPclFontEntry = _MltPrtPclFontEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1, 1)
)
mltPrtPclFontEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPrtPclFontIndex"),
)
if mibBuilder.loadTexts:
    mltPrtPclFontEntry.setStatus("mandatory")


class _MltPrtPclFontIndex_Type(Integer32):
    """Custom type mltPrtPclFontIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MltPrtPclFontIndex_Type.__name__ = "Integer32"
_MltPrtPclFontIndex_Object = MibTableColumn
mltPrtPclFontIndex = _MltPrtPclFontIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1, 1, 1),
    _MltPrtPclFontIndex_Type()
)
mltPrtPclFontIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPclFontIndex.setStatus("mandatory")


class _MltPrtPclFontName_Type(DisplayString):
    """Custom type mltPrtPclFontName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltPrtPclFontName_Type.__name__ = "DisplayString"
_MltPrtPclFontName_Object = MibTableColumn
mltPrtPclFontName = _MltPrtPclFontName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1, 1, 2),
    _MltPrtPclFontName_Type()
)
mltPrtPclFontName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPclFontName.setStatus("mandatory")


class _MltPrtPclFontNumber_Type(Integer32):
    """Custom type mltPrtPclFontNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MltPrtPclFontNumber_Type.__name__ = "Integer32"
_MltPrtPclFontNumber_Object = MibTableColumn
mltPrtPclFontNumber = _MltPrtPclFontNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1, 1, 3),
    _MltPrtPclFontNumber_Type()
)
mltPrtPclFontNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPclFontNumber.setStatus("mandatory")


class _MltPrtPclFontSource_Type(Integer32):
    """Custom type mltPrtPclFontSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("downLoadFlashRom", 5),
          ("downLoadHd", 4),
          ("downLoadRam", 3),
          ("internalHd", 2),
          ("internalRom", 1),
          ("unknown", 0))
    )


_MltPrtPclFontSource_Type.__name__ = "Integer32"
_MltPrtPclFontSource_Object = MibTableColumn
mltPrtPclFontSource = _MltPrtPclFontSource_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 1, 1, 4),
    _MltPrtPclFontSource_Type()
)
mltPrtPclFontSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPclFontSource.setStatus("mandatory")
_MltPrtPsFontTable_Object = MibTable
mltPrtPsFontTable = _MltPrtPsFontTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    mltPrtPsFontTable.setStatus("mandatory")
_MltPrtPsFontEntry_Object = MibTableRow
mltPrtPsFontEntry = _MltPrtPsFontEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2, 1)
)
mltPrtPsFontEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPrtPsFontIndex"),
)
if mibBuilder.loadTexts:
    mltPrtPsFontEntry.setStatus("mandatory")


class _MltPrtPsFontIndex_Type(Integer32):
    """Custom type mltPrtPsFontIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MltPrtPsFontIndex_Type.__name__ = "Integer32"
_MltPrtPsFontIndex_Object = MibTableColumn
mltPrtPsFontIndex = _MltPrtPsFontIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2, 1, 1),
    _MltPrtPsFontIndex_Type()
)
mltPrtPsFontIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPsFontIndex.setStatus("mandatory")


class _MltPrtPsFontName_Type(DisplayString):
    """Custom type mltPrtPsFontName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltPrtPsFontName_Type.__name__ = "DisplayString"
_MltPrtPsFontName_Object = MibTableColumn
mltPrtPsFontName = _MltPrtPsFontName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2, 1, 2),
    _MltPrtPsFontName_Type()
)
mltPrtPsFontName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPsFontName.setStatus("mandatory")


class _MltPrtPsFontNumber_Type(Integer32):
    """Custom type mltPrtPsFontNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MltPrtPsFontNumber_Type.__name__ = "Integer32"
_MltPrtPsFontNumber_Object = MibTableColumn
mltPrtPsFontNumber = _MltPrtPsFontNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2, 1, 3),
    _MltPrtPsFontNumber_Type()
)
mltPrtPsFontNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPsFontNumber.setStatus("mandatory")


class _MltPrtPsFontSource_Type(Integer32):
    """Custom type mltPrtPsFontSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("downLoadFlashRom", 5),
          ("downLoadHd", 4),
          ("downLoadRam", 3),
          ("internalHd", 2),
          ("internalRom", 1),
          ("unknown", 0))
    )


_MltPrtPsFontSource_Type.__name__ = "Integer32"
_MltPrtPsFontSource_Object = MibTableColumn
mltPrtPsFontSource = _MltPrtPsFontSource_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 2, 1, 4),
    _MltPrtPsFontSource_Type()
)
mltPrtPsFontSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPsFontSource.setStatus("mandatory")
_MltPrtSymbolSetTable_Object = MibTable
mltPrtSymbolSetTable = _MltPrtSymbolSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 3)
)
if mibBuilder.loadTexts:
    mltPrtSymbolSetTable.setStatus("mandatory")
_MltPrtSymbolSetEntry_Object = MibTableRow
mltPrtSymbolSetEntry = _MltPrtSymbolSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 3, 1)
)
mltPrtSymbolSetEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPrtSymbolSetIndex"),
)
if mibBuilder.loadTexts:
    mltPrtSymbolSetEntry.setStatus("mandatory")


class _MltPrtSymbolSetIndex_Type(Integer32):
    """Custom type mltPrtSymbolSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MltPrtSymbolSetIndex_Type.__name__ = "Integer32"
_MltPrtSymbolSetIndex_Object = MibTableColumn
mltPrtSymbolSetIndex = _MltPrtSymbolSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 3, 1, 1),
    _MltPrtSymbolSetIndex_Type()
)
mltPrtSymbolSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtSymbolSetIndex.setStatus("mandatory")


class _MltPrtSymbolSetName_Type(DisplayString):
    """Custom type mltPrtSymbolSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltPrtSymbolSetName_Type.__name__ = "DisplayString"
_MltPrtSymbolSetName_Object = MibTableColumn
mltPrtSymbolSetName = _MltPrtSymbolSetName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 3, 1, 2),
    _MltPrtSymbolSetName_Type()
)
mltPrtSymbolSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtSymbolSetName.setStatus("mandatory")


class _MltPrtCharSetID_Type(Integer32):
    """Custom type mltPrtCharSetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MltPrtCharSetID_Type.__name__ = "Integer32"
_MltPrtCharSetID_Object = MibTableColumn
mltPrtCharSetID = _MltPrtCharSetID_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 6, 3, 1, 3),
    _MltPrtCharSetID_Type()
)
mltPrtCharSetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtCharSetID.setStatus("mandatory")
_MltPrtPaper_ObjectIdentity = ObjectIdentity
mltPrtPaper = _MltPrtPaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7)
)
_MltPrtPaperSizeTable_Object = MibTable
mltPrtPaperSizeTable = _MltPrtPaperSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mltPrtPaperSizeTable.setStatus("mandatory")
_MltPrtPaperSizeEntry_Object = MibTableRow
mltPrtPaperSizeEntry = _MltPrtPaperSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7, 1, 1)
)
mltPrtPaperSizeEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPaperSizeIndex"),
)
if mibBuilder.loadTexts:
    mltPrtPaperSizeEntry.setStatus("mandatory")


class _MltPaperSizeIndex_Type(Integer32):
    """Custom type mltPaperSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MltPaperSizeIndex_Type.__name__ = "Integer32"
_MltPaperSizeIndex_Object = MibTableColumn
mltPaperSizeIndex = _MltPaperSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7, 1, 1, 1),
    _MltPaperSizeIndex_Type()
)
mltPaperSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPaperSizeIndex.setStatus("mandatory")


class _MltPaperSizeName_Type(DisplayString):
    """Custom type mltPaperSizeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltPaperSizeName_Type.__name__ = "DisplayString"
_MltPaperSizeName_Object = MibTableColumn
mltPaperSizeName = _MltPaperSizeName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7, 1, 1, 2),
    _MltPaperSizeName_Type()
)
mltPaperSizeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPaperSizeName.setStatus("mandatory")


class _MltPaperFeedDir_Type(Integer32):
    """Custom type mltPaperFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lef", 2),
          ("other", 0),
          ("sef", 1))
    )


_MltPaperFeedDir_Type.__name__ = "Integer32"
_MltPaperFeedDir_Object = MibTableColumn
mltPaperFeedDir = _MltPaperFeedDir_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 7, 1, 1, 3),
    _MltPaperFeedDir_Type()
)
mltPaperFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPaperFeedDir.setStatus("mandatory")
_MltPrtRemotePanel_ObjectIdentity = ObjectIdentity
mltPrtRemotePanel = _MltPrtRemotePanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10)
)
_MltPrtRemotePanelButtonTable_Object = MibTable
mltPrtRemotePanelButtonTable = _MltPrtRemotePanelButtonTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    mltPrtRemotePanelButtonTable.setStatus("optional")
_MltPrtRemotePanelButtonEntry_Object = MibTableRow
mltPrtRemotePanelButtonEntry = _MltPrtRemotePanelButtonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1, 1)
)
mltPrtRemotePanelButtonEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "MC2350-MIB", "mltPrtPanelButtonIndex"),
)
if mibBuilder.loadTexts:
    mltPrtRemotePanelButtonEntry.setStatus("optional")


class _MltPrtPanelButtonIndex_Type(Integer32):
    """Custom type mltPrtPanelButtonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MltPrtPanelButtonIndex_Type.__name__ = "Integer32"
_MltPrtPanelButtonIndex_Object = MibTableColumn
mltPrtPanelButtonIndex = _MltPrtPanelButtonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1, 1, 1),
    _MltPrtPanelButtonIndex_Type()
)
mltPrtPanelButtonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPanelButtonIndex.setStatus("optional")


class _MltPrtPanelButtonName_Type(DisplayString):
    """Custom type mltPrtPanelButtonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltPrtPanelButtonName_Type.__name__ = "DisplayString"
_MltPrtPanelButtonName_Object = MibTableColumn
mltPrtPanelButtonName = _MltPrtPanelButtonName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1, 1, 2),
    _MltPrtPanelButtonName_Type()
)
mltPrtPanelButtonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPanelButtonName.setStatus("optional")


class _MltPrtPanelButtonPush_Type(Integer32):
    """Custom type mltPrtPanelButtonPush based on Integer32"""
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
        *(("longPush", 2),
          ("noAction", 0),
          ("push", 1),
          ("shiftPush", 3))
    )


_MltPrtPanelButtonPush_Type.__name__ = "Integer32"
_MltPrtPanelButtonPush_Object = MibTableColumn
mltPrtPanelButtonPush = _MltPrtPanelButtonPush_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1, 1, 3),
    _MltPrtPanelButtonPush_Type()
)
mltPrtPanelButtonPush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltPrtPanelButtonPush.setStatus("optional")


class _MltPrtPanelButtonDescr_Type(DisplayString):
    """Custom type mltPrtPanelButtonDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltPrtPanelButtonDescr_Type.__name__ = "DisplayString"
_MltPrtPanelButtonDescr_Object = MibTableColumn
mltPrtPanelButtonDescr = _MltPrtPanelButtonDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 1, 6, 10, 1, 1, 4),
    _MltPrtPanelButtonDescr_Type()
)
mltPrtPanelButtonDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrtPanelButtonDescr.setStatus("optional")
_MltSysMib_ObjectIdentity = ObjectIdentity
mltSysMib = _MltSysMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5)
)


class _MltSysMibVersion_Type(DisplayString):
    """Custom type mltSysMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MltSysMibVersion_Type.__name__ = "DisplayString"
_MltSysMibVersion_Object = MibScalar
mltSysMibVersion = _MltSysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 1),
    _MltSysMibVersion_Type()
)
mltSysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysMibVersion.setStatus("mandatory")
_MltSysGeneralInfo_ObjectIdentity = ObjectIdentity
mltSysGeneralInfo = _MltSysGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 2)
)
_MltSysPriorityDevice_Type = Integer32
_MltSysPriorityDevice_Object = MibScalar
mltSysPriorityDevice = _MltSysPriorityDevice_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 2, 2),
    _MltSysPriorityDevice_Type()
)
mltSysPriorityDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysPriorityDevice.setStatus("mandatory")
_MltSysCurrentDateTime_Type = DateAndTime
_MltSysCurrentDateTime_Object = MibScalar
mltSysCurrentDateTime = _MltSysCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 2, 4),
    _MltSysCurrentDateTime_Type()
)
mltSysCurrentDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysCurrentDateTime.setStatus("mandatory")
_MltSysContact_ObjectIdentity = ObjectIdentity
mltSysContact = _MltSysContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3)
)


class _MltSysContactSiteName_Type(DisplayString):
    """Custom type mltSysContactSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MltSysContactSiteName_Type.__name__ = "DisplayString"
_MltSysContactSiteName_Object = MibScalar
mltSysContactSiteName = _MltSysContactSiteName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3, 1),
    _MltSysContactSiteName_Type()
)
mltSysContactSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysContactSiteName.setStatus("mandatory")


class _MltSysContactInfo_Type(DisplayString):
    """Custom type mltSysContactInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MltSysContactInfo_Type.__name__ = "DisplayString"
_MltSysContactInfo_Object = MibScalar
mltSysContactInfo = _MltSysContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3, 2),
    _MltSysContactInfo_Type()
)
mltSysContactInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysContactInfo.setStatus("mandatory")


class _MltSysProductHelpURL_Type(DisplayString):
    """Custom type mltSysProductHelpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MltSysProductHelpURL_Type.__name__ = "DisplayString"
_MltSysProductHelpURL_Object = MibScalar
mltSysProductHelpURL = _MltSysProductHelpURL_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3, 3),
    _MltSysProductHelpURL_Type()
)
mltSysProductHelpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysProductHelpURL.setStatus("mandatory")


class _MltSysCorpURL_Type(DisplayString):
    """Custom type mltSysCorpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MltSysCorpURL_Type.__name__ = "DisplayString"
_MltSysCorpURL_Object = MibScalar
mltSysCorpURL = _MltSysCorpURL_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3, 4),
    _MltSysCorpURL_Type()
)
mltSysCorpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysCorpURL.setStatus("mandatory")


class _MltSysSuppliesInfo_Type(DisplayString):
    """Custom type mltSysSuppliesInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MltSysSuppliesInfo_Type.__name__ = "DisplayString"
_MltSysSuppliesInfo_Object = MibScalar
mltSysSuppliesInfo = _MltSysSuppliesInfo_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 3, 5),
    _MltSysSuppliesInfo_Type()
)
mltSysSuppliesInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysSuppliesInfo.setStatus("mandatory")
_MltSysVersion_ObjectIdentity = ObjectIdentity
mltSysVersion = _MltSysVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5)
)
_MltSysVersionTable_Object = MibTable
mltSysVersionTable = _MltSysVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mltSysVersionTable.setStatus("mandatory")
_MltSysVersionEntry_Object = MibTableRow
mltSysVersionEntry = _MltSysVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1, 1)
)
mltSysVersionEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysVersionIndex"),
)
if mibBuilder.loadTexts:
    mltSysVersionEntry.setStatus("mandatory")
_MltSysVersionIndex_Type = Integer32
_MltSysVersionIndex_Object = MibTableColumn
mltSysVersionIndex = _MltSysVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1, 1, 1),
    _MltSysVersionIndex_Type()
)
mltSysVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysVersionIndex.setStatus("mandatory")


class _MltSysVerName_Type(DisplayString):
    """Custom type mltSysVerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltSysVerName_Type.__name__ = "DisplayString"
_MltSysVerName_Object = MibTableColumn
mltSysVerName = _MltSysVerName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1, 1, 2),
    _MltSysVerName_Type()
)
mltSysVerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysVerName.setStatus("mandatory")


class _MltSysVersionCode_Type(DisplayString):
    """Custom type mltSysVersionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltSysVersionCode_Type.__name__ = "DisplayString"
_MltSysVersionCode_Object = MibTableColumn
mltSysVersionCode = _MltSysVersionCode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1, 1, 3),
    _MltSysVersionCode_Type()
)
mltSysVersionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysVersionCode.setStatus("mandatory")


class _MltSysVerDescr_Type(DisplayString):
    """Custom type mltSysVerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltSysVerDescr_Type.__name__ = "DisplayString"
_MltSysVerDescr_Object = MibTableColumn
mltSysVerDescr = _MltSysVerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 5, 1, 1, 4),
    _MltSysVerDescr_Type()
)
mltSysVerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysVerDescr.setStatus("mandatory")
_MltSysComponent_ObjectIdentity = ObjectIdentity
mltSysComponent = _MltSysComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6)
)
_MltSysCompConfigID_Type = Integer32
_MltSysCompConfigID_Object = MibScalar
mltSysCompConfigID = _MltSysCompConfigID_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 1),
    _MltSysCompConfigID_Type()
)
mltSysCompConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysCompConfigID.setStatus("mandatory")
_MltSysInputTrayTable_Object = MibTable
mltSysInputTrayTable = _MltSysInputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    mltSysInputTrayTable.setStatus("mandatory")
_MltSysInputTrayEntry_Object = MibTableRow
mltSysInputTrayEntry = _MltSysInputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1)
)
mltSysInputTrayEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysInputTrayIndex"),
)
if mibBuilder.loadTexts:
    mltSysInputTrayEntry.setStatus("mandatory")
_MltSysInputTrayIndex_Type = Integer32
_MltSysInputTrayIndex_Object = MibTableColumn
mltSysInputTrayIndex = _MltSysInputTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 1),
    _MltSysInputTrayIndex_Type()
)
mltSysInputTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysInputTrayIndex.setStatus("mandatory")
_MltSysInputTrayRefIndex_Type = Integer32
_MltSysInputTrayRefIndex_Object = MibTableColumn
mltSysInputTrayRefIndex = _MltSysInputTrayRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 2),
    _MltSysInputTrayRefIndex_Type()
)
mltSysInputTrayRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysInputTrayRefIndex.setStatus("mandatory")


class _MltSysInputTrayName_Type(DisplayString):
    """Custom type mltSysInputTrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltSysInputTrayName_Type.__name__ = "DisplayString"
_MltSysInputTrayName_Object = MibTableColumn
mltSysInputTrayName = _MltSysInputTrayName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 3),
    _MltSysInputTrayName_Type()
)
mltSysInputTrayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysInputTrayName.setStatus("mandatory")


class _MltSysInputTrayCapacitySence_Type(Integer32):
    """Custom type mltSysInputTrayCapacitySence based on Integer32"""
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
        *(("emptyOnly", 1),
          ("linearSense", 3),
          ("nearEmpty", 2),
          ("noSensor", 0))
    )


_MltSysInputTrayCapacitySence_Type.__name__ = "Integer32"
_MltSysInputTrayCapacitySence_Object = MibTableColumn
mltSysInputTrayCapacitySence = _MltSysInputTrayCapacitySence_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 4),
    _MltSysInputTrayCapacitySence_Type()
)
mltSysInputTrayCapacitySence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysInputTrayCapacitySence.setStatus("mandatory")


class _MltSysInputTraySpecialPaper_Type(Integer32):
    """Custom type mltSysInputTraySpecialPaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10,
              11,
              12,
              14,
              16,
              20,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              36,
              40,
              41,
              42,
              44,
              46,
              48)
        )
    )
    namedValues = NamedValues(
        *(("envelope", 40),
          ("envelope-2side", 41),
          ("label", 42),
          ("letterHead", 46),
          ("ohp", 30),
          ("other", 0),
          ("plainPaper", 10),
          ("plainPaper-Color", 16),
          ("plainPaper-Exclusive", 14),
          ("plainPaper-NotFor2Sided", 11),
          ("plainPaper-Recycled", 12),
          ("postCard", 44),
          ("tab", 48),
          ("thick", 20),
          ("thick1", 22),
          ("thick1-2side", 23),
          ("thick2", 24),
          ("thick2-2side", 25),
          ("thick3", 26),
          ("thick3-2side", 27),
          ("thin", 36),
          ("unknown", 1))
    )


_MltSysInputTraySpecialPaper_Type.__name__ = "Integer32"
_MltSysInputTraySpecialPaper_Object = MibTableColumn
mltSysInputTraySpecialPaper = _MltSysInputTraySpecialPaper_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 5),
    _MltSysInputTraySpecialPaper_Type()
)
mltSysInputTraySpecialPaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysInputTraySpecialPaper.setStatus("mandatory")


class _MltSysInputTrayPaperAttribute_Type(Integer32):
    """Custom type mltSysInputTrayPaperAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("s0-normalPaper", 1),
          ("s1-recyclePaper", 2),
          ("s2-specialPaper", 3),
          ("s3-reusePaper", 4))
    )


_MltSysInputTrayPaperAttribute_Type.__name__ = "Integer32"
_MltSysInputTrayPaperAttribute_Object = MibTableColumn
mltSysInputTrayPaperAttribute = _MltSysInputTrayPaperAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 2, 1, 6),
    _MltSysInputTrayPaperAttribute_Type()
)
mltSysInputTrayPaperAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysInputTrayPaperAttribute.setStatus("optional")
_MltSysOutputTrayTable_Object = MibTable
mltSysOutputTrayTable = _MltSysOutputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    mltSysOutputTrayTable.setStatus("mandatory")
_MltSysOutputTrayEntry_Object = MibTableRow
mltSysOutputTrayEntry = _MltSysOutputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1)
)
mltSysOutputTrayEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysOutputTrayIndex"),
)
if mibBuilder.loadTexts:
    mltSysOutputTrayEntry.setStatus("mandatory")
_MltSysOutputTrayIndex_Type = Integer32
_MltSysOutputTrayIndex_Object = MibTableColumn
mltSysOutputTrayIndex = _MltSysOutputTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1, 1),
    _MltSysOutputTrayIndex_Type()
)
mltSysOutputTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysOutputTrayIndex.setStatus("mandatory")
_MltSysOutputTrayRefIndex_Type = Integer32
_MltSysOutputTrayRefIndex_Object = MibTableColumn
mltSysOutputTrayRefIndex = _MltSysOutputTrayRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1, 2),
    _MltSysOutputTrayRefIndex_Type()
)
mltSysOutputTrayRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysOutputTrayRefIndex.setStatus("mandatory")


class _MltSysOutputTrayDefaultName_Type(DisplayString):
    """Custom type mltSysOutputTrayDefaultName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltSysOutputTrayDefaultName_Type.__name__ = "DisplayString"
_MltSysOutputTrayDefaultName_Object = MibTableColumn
mltSysOutputTrayDefaultName = _MltSysOutputTrayDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1, 3),
    _MltSysOutputTrayDefaultName_Type()
)
mltSysOutputTrayDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysOutputTrayDefaultName.setStatus("mandatory")


class _MltSysOutputTrayNickName_Type(DisplayString):
    """Custom type mltSysOutputTrayNickName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltSysOutputTrayNickName_Type.__name__ = "DisplayString"
_MltSysOutputTrayNickName_Object = MibTableColumn
mltSysOutputTrayNickName = _MltSysOutputTrayNickName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1, 4),
    _MltSysOutputTrayNickName_Type()
)
mltSysOutputTrayNickName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysOutputTrayNickName.setStatus("mandatory")


class _MltSysOutputTrayType_Type(Integer32):
    """Custom type mltSysOutputTrayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fixedMailBin", 5),
          ("mailBox", 4),
          ("other", 0),
          ("sortBin", 3),
          ("standardBin", 1))
    )


_MltSysOutputTrayType_Type.__name__ = "Integer32"
_MltSysOutputTrayType_Object = MibTableColumn
mltSysOutputTrayType = _MltSysOutputTrayType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 6, 3, 1, 5),
    _MltSysOutputTrayType_Type()
)
mltSysOutputTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysOutputTrayType.setStatus("mandatory")
_MltSysCounter_ObjectIdentity = ObjectIdentity
mltSysCounter = _MltSysCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7)
)
_MltSysCounterConfig_ObjectIdentity = ObjectIdentity
mltSysCounterConfig = _MltSysCounterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1)
)
_MltSysSupportedCounterType_Type = Integer32
_MltSysSupportedCounterType_Object = MibScalar
mltSysSupportedCounterType = _MltSysSupportedCounterType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1, 1),
    _MltSysSupportedCounterType_Type()
)
mltSysSupportedCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSupportedCounterType.setStatus("mandatory")


class _MltSysDuplexCountMode_Type(Integer32):
    """Custom type mltSysDuplexCountMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doubleCount", 2),
          ("singleCount", 1),
          ("unknown", 0))
    )


_MltSysDuplexCountMode_Type.__name__ = "Integer32"
_MltSysDuplexCountMode_Object = MibScalar
mltSysDuplexCountMode = _MltSysDuplexCountMode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1, 2),
    _MltSysDuplexCountMode_Type()
)
mltSysDuplexCountMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysDuplexCountMode.setStatus("mandatory")


class _MltSysLargeSizeCountMode_Type(Integer32):
    """Custom type mltSysLargeSizeCountMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doubleCount", 2),
          ("singleCount", 1),
          ("unknown", 0))
    )


_MltSysLargeSizeCountMode_Type.__name__ = "Integer32"
_MltSysLargeSizeCountMode_Object = MibScalar
mltSysLargeSizeCountMode = _MltSysLargeSizeCountMode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1, 3),
    _MltSysLargeSizeCountMode_Type()
)
mltSysLargeSizeCountMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysLargeSizeCountMode.setStatus("mandatory")


class _MltSysLargeSizeType_Type(Integer32):
    """Custom type mltSysLargeSizeType based on Integer32"""
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
        *(("noLargeSize", 0),
          ("typeA", 1),
          ("typeB", 2),
          ("typeC", 3))
    )


_MltSysLargeSizeType_Type.__name__ = "Integer32"
_MltSysLargeSizeType_Object = MibScalar
mltSysLargeSizeType = _MltSysLargeSizeType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1, 4),
    _MltSysLargeSizeType_Type()
)
mltSysLargeSizeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltSysLargeSizeType.setStatus("mandatory")
_MltSysColorCountSupportType_Type = Integer32
_MltSysColorCountSupportType_Object = MibScalar
mltSysColorCountSupportType = _MltSysColorCountSupportType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 1, 5),
    _MltSysColorCountSupportType_Type()
)
mltSysColorCountSupportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysColorCountSupportType.setStatus("mandatory")
_MltSysSystemCounter_ObjectIdentity = ObjectIdentity
mltSysSystemCounter = _MltSysSystemCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2)
)
_MltSysGeneralCounter_ObjectIdentity = ObjectIdentity
mltSysGeneralCounter = _MltSysGeneralCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1)
)
_MltSysTotalCount_Type = Integer32
_MltSysTotalCount_Object = MibScalar
mltSysTotalCount = _MltSysTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 1),
    _MltSysTotalCount_Type()
)
mltSysTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysTotalCount.setStatus("mandatory")
_MltSysLargeSizeCount_Type = Integer32
_MltSysLargeSizeCount_Object = MibScalar
mltSysLargeSizeCount = _MltSysLargeSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 2),
    _MltSysLargeSizeCount_Type()
)
mltSysLargeSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysLargeSizeCount.setStatus("mandatory")
_MltSysDuplexCount_Type = Integer32
_MltSysDuplexCount_Object = MibScalar
mltSysDuplexCount = _MltSysDuplexCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 3),
    _MltSysDuplexCount_Type()
)
mltSysDuplexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysDuplexCount.setStatus("mandatory")
_MltSysLargeDuplexCount_Type = Integer32
_MltSysLargeDuplexCount_Object = MibScalar
mltSysLargeDuplexCount = _MltSysLargeDuplexCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 4),
    _MltSysLargeDuplexCount_Type()
)
mltSysLargeDuplexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysLargeDuplexCount.setStatus("mandatory")
_MltSysSendTotalCount_Type = Integer32
_MltSysSendTotalCount_Object = MibScalar
mltSysSendTotalCount = _MltSysSendTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 5),
    _MltSysSendTotalCount_Type()
)
mltSysSendTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSendTotalCount.setStatus("mandatory")
_MltSysTotalJamCount_Type = Integer32
_MltSysTotalJamCount_Object = MibScalar
mltSysTotalJamCount = _MltSysTotalJamCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 6),
    _MltSysTotalJamCount_Type()
)
mltSysTotalJamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysTotalJamCount.setStatus("mandatory")
_MltSysTotalTroubleCount_Type = Integer32
_MltSysTotalTroubleCount_Object = MibScalar
mltSysTotalTroubleCount = _MltSysTotalTroubleCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 1, 7),
    _MltSysTotalTroubleCount_Type()
)
mltSysTotalTroubleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysTotalTroubleCount.setStatus("mandatory")
_MltSysPrintFunctionCounterTable_Object = MibTable
mltSysPrintFunctionCounterTable = _MltSysPrintFunctionCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2)
)
if mibBuilder.loadTexts:
    mltSysPrintFunctionCounterTable.setStatus("optional")
_MltSysPrintFunctionCounterEntry_Object = MibTableRow
mltSysPrintFunctionCounterEntry = _MltSysPrintFunctionCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1)
)
mltSysPrintFunctionCounterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysPrintFunctionColorIndex"),
    (0, "MC2350-MIB", "mltSysPrintFunctionIndex"),
)
if mibBuilder.loadTexts:
    mltSysPrintFunctionCounterEntry.setStatus("optional")
_MltSysPrintFunctionColorIndex_Type = Integer32
_MltSysPrintFunctionColorIndex_Object = MibTableColumn
mltSysPrintFunctionColorIndex = _MltSysPrintFunctionColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 1),
    _MltSysPrintFunctionColorIndex_Type()
)
mltSysPrintFunctionColorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionColorIndex.setStatus("optional")
_MltSysPrintFunctionIndex_Type = Integer32
_MltSysPrintFunctionIndex_Object = MibTableColumn
mltSysPrintFunctionIndex = _MltSysPrintFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 2),
    _MltSysPrintFunctionIndex_Type()
)
mltSysPrintFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionIndex.setStatus("optional")


class _MltSysPrintFunctionColorType_Type(Integer32):
    """Custom type mltSysPrintFunctionColorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bw", 1),
          ("cmy", 4),
          ("fourColor", 2),
          ("monoColor", 6),
          ("paperPath", 7),
          ("rgb", 5),
          ("threeColor", 3))
    )


_MltSysPrintFunctionColorType_Type.__name__ = "Integer32"
_MltSysPrintFunctionColorType_Object = MibTableColumn
mltSysPrintFunctionColorType = _MltSysPrintFunctionColorType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 3),
    _MltSysPrintFunctionColorType_Type()
)
mltSysPrintFunctionColorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionColorType.setStatus("optional")


class _MltSysPrintFunctionType_Type(Integer32):
    """Custom type mltSysPrintFunctionType based on Integer32"""
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
        *(("copyFunction", 1),
          ("faxReceiveFunction", 4),
          ("printFunction", 2),
          ("receiveFunction", 3),
          ("reportPrint", 5))
    )


_MltSysPrintFunctionType_Type.__name__ = "Integer32"
_MltSysPrintFunctionType_Object = MibTableColumn
mltSysPrintFunctionType = _MltSysPrintFunctionType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 4),
    _MltSysPrintFunctionType_Type()
)
mltSysPrintFunctionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionType.setStatus("optional")
_MltSysPrintFunctionTotalCount_Type = Integer32
_MltSysPrintFunctionTotalCount_Object = MibTableColumn
mltSysPrintFunctionTotalCount = _MltSysPrintFunctionTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 5),
    _MltSysPrintFunctionTotalCount_Type()
)
mltSysPrintFunctionTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionTotalCount.setStatus("optional")
_MltSysPrintFunctionDuplexCount_Type = Integer32
_MltSysPrintFunctionDuplexCount_Object = MibTableColumn
mltSysPrintFunctionDuplexCount = _MltSysPrintFunctionDuplexCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 6),
    _MltSysPrintFunctionDuplexCount_Type()
)
mltSysPrintFunctionDuplexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionDuplexCount.setStatus("optional")
_MltSysPrintFunctionLargeSizeCount_Type = Integer32
_MltSysPrintFunctionLargeSizeCount_Object = MibTableColumn
mltSysPrintFunctionLargeSizeCount = _MltSysPrintFunctionLargeSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 7),
    _MltSysPrintFunctionLargeSizeCount_Type()
)
mltSysPrintFunctionLargeSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionLargeSizeCount.setStatus("optional")
_MltSysPrintFunctionLargeDuplexCount_Type = Integer32
_MltSysPrintFunctionLargeDuplexCount_Object = MibTableColumn
mltSysPrintFunctionLargeDuplexCount = _MltSysPrintFunctionLargeDuplexCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 2, 1, 8),
    _MltSysPrintFunctionLargeDuplexCount_Type()
)
mltSysPrintFunctionLargeDuplexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysPrintFunctionLargeDuplexCount.setStatus("optional")
_MltSysSizeCounterTable_Object = MibTable
mltSysSizeCounterTable = _MltSysSizeCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4)
)
if mibBuilder.loadTexts:
    mltSysSizeCounterTable.setStatus("mandatory")
_MltSysSizeCounterEntry_Object = MibTableRow
mltSysSizeCounterEntry = _MltSysSizeCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1)
)
mltSysSizeCounterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysSizeFunctionIndex"),
    (0, "MC2350-MIB", "mltSysSizeTypeIndex"),
)
if mibBuilder.loadTexts:
    mltSysSizeCounterEntry.setStatus("mandatory")
_MltSysSizeFunctionIndex_Type = Integer32
_MltSysSizeFunctionIndex_Object = MibTableColumn
mltSysSizeFunctionIndex = _MltSysSizeFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1, 1),
    _MltSysSizeFunctionIndex_Type()
)
mltSysSizeFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSizeFunctionIndex.setStatus("mandatory")
_MltSysSizeTypeIndex_Type = Integer32
_MltSysSizeTypeIndex_Object = MibTableColumn
mltSysSizeTypeIndex = _MltSysSizeTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1, 2),
    _MltSysSizeTypeIndex_Type()
)
mltSysSizeTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSizeTypeIndex.setStatus("mandatory")


class _MltSysSizeFunction_Type(Integer32):
    """Custom type mltSysSizeFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("total", 0)
    )


_MltSysSizeFunction_Type.__name__ = "Integer32"
_MltSysSizeFunction_Object = MibTableColumn
mltSysSizeFunction = _MltSysSizeFunction_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1, 3),
    _MltSysSizeFunction_Type()
)
mltSysSizeFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSizeFunction.setStatus("mandatory")


class _MltSysSizeType_Type(Integer32):
    """Custom type mltSysSizeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              50,
              51,
              52,
              53,
              54,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              70,
              71,
              72,
              83,
              84,
              93,
              100,
              101,
              102,
              103,
              104,
              106,
              114,
              115,
              116,
              117,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              214,
              216,
              222,
              223,
              224,
              225,
              226,
              227,
              230,
              236,
              240,
              241,
              242,
              244,
              246,
              248)
        )
    )
    namedValues = NamedValues(
        *(("a0", 11),
          ("a1", 12),
          ("a2", 13),
          ("a3", 14),
          ("a3W", 114),
          ("a4", 15),
          ("a4W", 115),
          ("a5", 16),
          ("a5W", 116),
          ("a6", 17),
          ("a6W", 117),
          ("b0", 21),
          ("b1", 22),
          ("b2", 23),
          ("b3", 24),
          ("b4", 25),
          ("b5", 26),
          ("b6", 27),
          ("choukei-3Gou", 83),
          ("choukei-4Gou", 84),
          ("comp", 34),
          ("cover", 205),
          ("envelope", 240),
          ("envelope-2side", 241),
          ("envelopeB5", 63),
          ("envelopeC5", 65),
          ("envelopeC6", 68),
          ("envelopeCom10", 64),
          ("envelopeDL", 66),
          ("envelopeMonarch", 67),
          ("exclusive", 202),
          ("executive", 42),
          ("fls", 50),
          ("fls0", 51),
          ("fls1", 52),
          ("fls2", 53),
          ("fls3", 54),
          ("govermentLetter", 40),
          ("hagaki", 61),
          ("inserter", 206),
          ("kakugata-3Gou", 93),
          ("label", 242),
          ("ledger", 31),
          ("legal", 37),
          ("letter", 39),
          ("letterHead", 246),
          ("notFor2Sided", 203),
          ("ohp", 230),
          ("otherMediaType", 208),
          ("otherPaperAttribute", 199),
          ("otherPaperSize", 0),
          ("oufuku-Hagaki", 62),
          ("plain", 201),
          ("plainPaper", 210),
          ("plainPaper-2side", 211),
          ("plainPaper-Color", 216),
          ("plainPaper-Exclusive", 214),
          ("plainPaper-Recycled", 212),
          ("postCard", 244),
          ("quarto", 41),
          ("reuse", 207),
          ("special0", 100),
          ("special1", 101),
          ("special2", 102),
          ("special3", 103),
          ("special4", 104),
          ("special5", 106),
          ("specialPaper", 204),
          ("statement", 43),
          ("tab", 248),
          ("thick1", 222),
          ("thick1-2side", 223),
          ("thick2", 224),
          ("thick2-2side", 225),
          ("thick3", 226),
          ("thick3-2side", 227),
          ("thin", 236),
          ("unknownMediaType", 209),
          ("unknownPaperAttribute", 200),
          ("unknownPaperSize", 1),
          ("us10x14", 35),
          ("us11x14", 33),
          ("us11x15", 32),
          ("us12x14", 30),
          ("us8-1by4x11-3by4", 38),
          ("us9-1by4x14", 36),
          ("youkei-0Gou", 70),
          ("youkei-4Gou", 71),
          ("youkei-6Gou", 72))
    )


_MltSysSizeType_Type.__name__ = "Integer32"
_MltSysSizeType_Object = MibTableColumn
mltSysSizeType = _MltSysSizeType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1, 4),
    _MltSysSizeType_Type()
)
mltSysSizeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSizeType.setStatus("mandatory")
_MltSysSizeCount_Type = Integer32
_MltSysSizeCount_Object = MibTableColumn
mltSysSizeCount = _MltSysSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 4, 1, 5),
    _MltSysSizeCount_Type()
)
mltSysSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysSizeCount.setStatus("mandatory")
_MltSysTonerLifeCounterTable_Object = MibTable
mltSysTonerLifeCounterTable = _MltSysTonerLifeCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 5)
)
if mibBuilder.loadTexts:
    mltSysTonerLifeCounterTable.setStatus("optional")
_MltSysTonerLifeCounterEntry_Object = MibTableRow
mltSysTonerLifeCounterEntry = _MltSysTonerLifeCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 5, 1)
)
mltSysTonerLifeCounterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltSysTonerTypeIndex"),
)
if mibBuilder.loadTexts:
    mltSysTonerLifeCounterEntry.setStatus("optional")
_MltSysTonerTypeIndex_Type = Integer32
_MltSysTonerTypeIndex_Object = MibTableColumn
mltSysTonerTypeIndex = _MltSysTonerTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 5, 1, 1),
    _MltSysTonerTypeIndex_Type()
)
mltSysTonerTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysTonerTypeIndex.setStatus("optional")


class _MltSysTonerType_Type(Integer32):
    """Custom type mltSysTonerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("black", 4),
          ("cyan", 1),
          ("magenta", 2),
          ("other", 0),
          ("yellow", 3))
    )


_MltSysTonerType_Type.__name__ = "Integer32"
_MltSysTonerType_Object = MibTableColumn
mltSysTonerType = _MltSysTonerType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 5, 1, 2),
    _MltSysTonerType_Type()
)
mltSysTonerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltSysTonerType.setStatus("optional")
_MltTonerTypeCount_Type = Counter32
_MltTonerTypeCount_Object = MibTableColumn
mltTonerTypeCount = _MltTonerTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 1, 5, 7, 2, 5, 1, 3),
    _MltTonerTypeCount_Type()
)
mltTonerTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTonerTypeCount.setStatus("optional")
_MltInterface_ObjectIdentity = ObjectIdentity
mltInterface = _MltInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2)
)
_MltNetwork_ObjectIdentity = ObjectIdentity
mltNetwork = _MltNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1)
)
_MltNetworkMib_ObjectIdentity = ObjectIdentity
mltNetworkMib = _MltNetworkMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5)
)


class _MltNetMibVersion_Type(DisplayString):
    """Custom type mltNetMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MltNetMibVersion_Type.__name__ = "DisplayString"
_MltNetMibVersion_Object = MibScalar
mltNetMibVersion = _MltNetMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 1),
    _MltNetMibVersion_Type()
)
mltNetMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetMibVersion.setStatus("mandatory")
_MltNetGeneral_ObjectIdentity = ObjectIdentity
mltNetGeneral = _MltNetGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2)
)
_MltNetGeneralTable_Object = MibTable
mltNetGeneralTable = _MltNetGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mltNetGeneralTable.setStatus("mandatory")
_MltNetGeneralEntry_Object = MibTableRow
mltNetGeneralEntry = _MltNetGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1)
)
mltNetGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetGeneralIndex"),
)
if mibBuilder.loadTexts:
    mltNetGeneralEntry.setStatus("mandatory")
_MltNetGeneralIndex_Type = Integer32
_MltNetGeneralIndex_Object = MibTableColumn
mltNetGeneralIndex = _MltNetGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 1),
    _MltNetGeneralIndex_Type()
)
mltNetGeneralIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetGeneralIndex.setStatus("mandatory")


class _MltNetFirmVersion_Type(DisplayString):
    """Custom type mltNetFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MltNetFirmVersion_Type.__name__ = "DisplayString"
_MltNetFirmVersion_Object = MibTableColumn
mltNetFirmVersion = _MltNetFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 2),
    _MltNetFirmVersion_Type()
)
mltNetFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFirmVersion.setStatus("mandatory")
_MltNetHardwareAddress_Type = PhysAddress
_MltNetHardwareAddress_Object = MibTableColumn
mltNetHardwareAddress = _MltNetHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 3),
    _MltNetHardwareAddress_Type()
)
mltNetHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetHardwareAddress.setStatus("mandatory")


class _MltNetSerialNumber_Type(DisplayString):
    """Custom type mltNetSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetSerialNumber_Type.__name__ = "DisplayString"
_MltNetSerialNumber_Object = MibTableColumn
mltNetSerialNumber = _MltNetSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 4),
    _MltNetSerialNumber_Type()
)
mltNetSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSerialNumber.setStatus("mandatory")
_MltNetSupportedConnector_Type = Integer32
_MltNetSupportedConnector_Object = MibTableColumn
mltNetSupportedConnector = _MltNetSupportedConnector_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 5),
    _MltNetSupportedConnector_Type()
)
mltNetSupportedConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSupportedConnector.setStatus("mandatory")


class _MltNetCurrentConnector_Type(Integer32):
    """Custom type mltNetCurrentConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7,
              8,
              9,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("blueTooth", 13),
          ("etherAUI", 1),
          ("etherBNC", 2),
          ("etherFiber", 4),
          ("etherRJ", 3),
          ("ieee1394", 14),
          ("notWorking", 0),
          ("tokenFiber", 9),
          ("tokenSTP", 7),
          ("tokenUTP", 8),
          ("wirelessA", 11),
          ("wirelessB", 12))
    )


_MltNetCurrentConnector_Type.__name__ = "Integer32"
_MltNetCurrentConnector_Object = MibTableColumn
mltNetCurrentConnector = _MltNetCurrentConnector_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 6),
    _MltNetCurrentConnector_Type()
)
mltNetCurrentConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCurrentConnector.setStatus("mandatory")


class _MltNetSpeedConfig_Type(Integer32):
    """Custom type mltNetSpeedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              10,
              11,
              12,
              13,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("autoDetectEther", 1),
          ("autoDetectToken", 10),
          ("autoDetectWireless", 20),
          ("et100MbpsFullDuplex", 5),
          ("et100MbpsHalfDuplex", 4),
          ("et10MbpsFullDuplex", 3),
          ("et10MbpsHalfDuplex", 2),
          ("etGbpsFullDuplex", 7),
          ("etGbpsHalfDuplex", 6),
          ("other", 0),
          ("tr16Mbps", 12),
          ("tr32Mbps", 13),
          ("tr4Mbps", 11),
          ("wireless11Mbps", 24),
          ("wireless1Mbps", 21),
          ("wireless2Mbps", 22),
          ("wireless5-5Mbps", 23))
    )


_MltNetSpeedConfig_Type.__name__ = "Integer32"
_MltNetSpeedConfig_Object = MibTableColumn
mltNetSpeedConfig = _MltNetSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 7),
    _MltNetSpeedConfig_Type()
)
mltNetSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSpeedConfig.setStatus("mandatory")


class _MltNetInterfaceType_Type(Integer32):
    """Custom type mltNetInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              11,
              12,
              100,
              101,
              102,
              103,
              104,
              201,
              202)
        )
    )
    namedValues = NamedValues(
        *(("dpo", 11),
          ("dual1284", 10),
          ("ieee1284", 1),
          ("ieee1394", 2),
          ("noPhysicalNIC", 101),
          ("onBoard", 102),
          ("onBoardDPO", 100),
          ("onBoardOneChip", 103),
          ("onBoardPSIO", 104),
          ("other", 0),
          ("pciIntelligent", 202),
          ("pciNonIntelligent", 201),
          ("psio", 12),
          ("usb", 3))
    )


_MltNetInterfaceType_Type.__name__ = "Integer32"
_MltNetInterfaceType_Object = MibTableColumn
mltNetInterfaceType = _MltNetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 8),
    _MltNetInterfaceType_Type()
)
mltNetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetInterfaceType.setStatus("mandatory")


class _MltNetIfDescr_Type(DisplayString):
    """Custom type mltNetIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetIfDescr_Type.__name__ = "DisplayString"
_MltNetIfDescr_Object = MibTableColumn
mltNetIfDescr = _MltNetIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 2, 1, 1, 9),
    _MltNetIfDescr_Type()
)
mltNetIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetIfDescr.setStatus("mandatory")
_MltNetProtocol_ObjectIdentity = ObjectIdentity
mltNetProtocol = _MltNetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3)
)
_MltNetProtocolTable_Object = MibTable
mltNetProtocolTable = _MltNetProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mltNetProtocolTable.setStatus("mandatory")
_MltNetProtocolEntry_Object = MibTableRow
mltNetProtocolEntry = _MltNetProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1)
)
mltNetProtocolEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetProtocolIfIndex"),
    (0, "MC2350-MIB", "mltNetProtocolIndex"),
)
if mibBuilder.loadTexts:
    mltNetProtocolEntry.setStatus("mandatory")
_MltNetProtocolIfIndex_Type = Integer32
_MltNetProtocolIfIndex_Object = MibTableColumn
mltNetProtocolIfIndex = _MltNetProtocolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 1),
    _MltNetProtocolIfIndex_Type()
)
mltNetProtocolIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetProtocolIfIndex.setStatus("mandatory")
_MltNetProtocolIndex_Type = Integer32
_MltNetProtocolIndex_Object = MibTableColumn
mltNetProtocolIndex = _MltNetProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 2),
    _MltNetProtocolIndex_Type()
)
mltNetProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetProtocolIndex.setStatus("mandatory")


class _MltNetProtocolType_Type(Integer32):
    """Custom type mltNetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 3),
          ("netWare", 2),
          ("other", 7),
          ("smb", 4),
          ("tcp-ip", 1),
          ("unknown", 0))
    )


_MltNetProtocolType_Type.__name__ = "Integer32"
_MltNetProtocolType_Object = MibTableColumn
mltNetProtocolType = _MltNetProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 3),
    _MltNetProtocolType_Type()
)
mltNetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetProtocolType.setStatus("mandatory")


class _MltNetProtocolDescr_Type(DisplayString):
    """Custom type mltNetProtocolDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetProtocolDescr_Type.__name__ = "DisplayString"
_MltNetProtocolDescr_Object = MibTableColumn
mltNetProtocolDescr = _MltNetProtocolDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 4),
    _MltNetProtocolDescr_Type()
)
mltNetProtocolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetProtocolDescr.setStatus("mandatory")


class _MltNetProtocolVer_Type(DisplayString):
    """Custom type mltNetProtocolVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetProtocolVer_Type.__name__ = "DisplayString"
_MltNetProtocolVer_Object = MibTableColumn
mltNetProtocolVer = _MltNetProtocolVer_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 5),
    _MltNetProtocolVer_Type()
)
mltNetProtocolVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetProtocolVer.setStatus("mandatory")


class _MltNetProtocolOnOff_Type(Integer32):
    """Custom type mltNetProtocolOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 0))
    )


_MltNetProtocolOnOff_Type.__name__ = "Integer32"
_MltNetProtocolOnOff_Object = MibTableColumn
mltNetProtocolOnOff = _MltNetProtocolOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 3, 1, 1, 6),
    _MltNetProtocolOnOff_Type()
)
mltNetProtocolOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetProtocolOnOff.setStatus("mandatory")
_MltNetCommand_ObjectIdentity = ObjectIdentity
mltNetCommand = _MltNetCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5)
)
_MltNetCommandTable_Object = MibTable
mltNetCommandTable = _MltNetCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mltNetCommandTable.setStatus("mandatory")
_MltNetCommandEntry_Object = MibTableRow
mltNetCommandEntry = _MltNetCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1)
)
mltNetCommandEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetCommandIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetCommandEntry.setStatus("mandatory")
_MltNetCommandIfIndex_Type = Integer32
_MltNetCommandIfIndex_Object = MibTableColumn
mltNetCommandIfIndex = _MltNetCommandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 1),
    _MltNetCommandIfIndex_Type()
)
mltNetCommandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCommandIfIndex.setStatus("mandatory")


class _MltNetCommandReset_Type(Integer32):
    """Custom type mltNetCommandReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("reset", 2),
          ("supported", 1))
    )


_MltNetCommandReset_Type.__name__ = "Integer32"
_MltNetCommandReset_Object = MibTableColumn
mltNetCommandReset = _MltNetCommandReset_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 2),
    _MltNetCommandReset_Type()
)
mltNetCommandReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCommandReset.setStatus("mandatory")


class _MltNetCommandDefault_Type(Integer32):
    """Custom type mltNetCommandDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("resetToDefault", 2),
          ("supported", 1))
    )


_MltNetCommandDefault_Type.__name__ = "Integer32"
_MltNetCommandDefault_Object = MibTableColumn
mltNetCommandDefault = _MltNetCommandDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 3),
    _MltNetCommandDefault_Type()
)
mltNetCommandDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetCommandDefault.setStatus("mandatory")


class _MltNetCommandPrintNicConfig_Type(Integer32):
    """Custom type mltNetCommandPrintNicConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 10),
          ("printing", 12),
          ("supported", 11))
    )


_MltNetCommandPrintNicConfig_Type.__name__ = "Integer32"
_MltNetCommandPrintNicConfig_Object = MibTableColumn
mltNetCommandPrintNicConfig = _MltNetCommandPrintNicConfig_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 4),
    _MltNetCommandPrintNicConfig_Type()
)
mltNetCommandPrintNicConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCommandPrintNicConfig.setStatus("mandatory")


class _MltNetCommandStartupConfig_Type(Integer32):
    """Custom type mltNetCommandStartupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 10),
          ("printStartUp", 12),
          ("supported", 11))
    )


_MltNetCommandStartupConfig_Type.__name__ = "Integer32"
_MltNetCommandStartupConfig_Object = MibTableColumn
mltNetCommandStartupConfig = _MltNetCommandStartupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 5),
    _MltNetCommandStartupConfig_Type()
)
mltNetCommandStartupConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCommandStartupConfig.setStatus("mandatory")


class _MltNetCommandDownLoad_Type(Integer32):
    """Custom type mltNetCommandDownLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downLoading", 2),
          ("notDownLoad", 1),
          ("notSupported", 0))
    )


_MltNetCommandDownLoad_Type.__name__ = "Integer32"
_MltNetCommandDownLoad_Object = MibTableColumn
mltNetCommandDownLoad = _MltNetCommandDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 5, 1, 1, 6),
    _MltNetCommandDownLoad_Type()
)
mltNetCommandDownLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetCommandDownLoad.setStatus("mandatory")
_MltNetSnmp_ObjectIdentity = ObjectIdentity
mltNetSnmp = _MltNetSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6)
)
_MltNetSnmpCommTable_Object = MibTable
mltNetSnmpCommTable = _MltNetSnmpCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mltNetSnmpCommTable.setStatus("mandatory")
_MltNetSnmpCommEntry_Object = MibTableRow
mltNetSnmpCommEntry = _MltNetSnmpCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 1, 1)
)
mltNetSnmpCommEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSnmpCommIndex"),
)
if mibBuilder.loadTexts:
    mltNetSnmpCommEntry.setStatus("mandatory")
_MltNetSnmpCommIndex_Type = Integer32
_MltNetSnmpCommIndex_Object = MibTableColumn
mltNetSnmpCommIndex = _MltNetSnmpCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 1, 1, 1),
    _MltNetSnmpCommIndex_Type()
)
mltNetSnmpCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSnmpCommIndex.setStatus("mandatory")


class _MltNetSnmpCommName_Type(DisplayString):
    """Custom type mltNetSnmpCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetSnmpCommName_Type.__name__ = "DisplayString"
_MltNetSnmpCommName_Object = MibTableColumn
mltNetSnmpCommName = _MltNetSnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 1, 1, 2),
    _MltNetSnmpCommName_Type()
)
mltNetSnmpCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpCommName.setStatus("mandatory")


class _MltNetSnmpCommAccessRight_Type(Integer32):
    """Custom type mltNetSnmpCommAccessRight based on Integer32"""
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
        *(("none", 0),
          ("readOnly", 1),
          ("readWrite", 3),
          ("writeOnly", 2))
    )


_MltNetSnmpCommAccessRight_Type.__name__ = "Integer32"
_MltNetSnmpCommAccessRight_Object = MibTableColumn
mltNetSnmpCommAccessRight = _MltNetSnmpCommAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 1, 1, 3),
    _MltNetSnmpCommAccessRight_Type()
)
mltNetSnmpCommAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpCommAccessRight.setStatus("mandatory")
_MltNetSnmpTrapTable_Object = MibTable
mltNetSnmpTrapTable = _MltNetSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    mltNetSnmpTrapTable.setStatus("mandatory")
_MltNetSnmpTrapEntry_Object = MibTableRow
mltNetSnmpTrapEntry = _MltNetSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1)
)
mltNetSnmpTrapEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSnmpTrapIfIndex"),
    (0, "MC2350-MIB", "mltNetSnmpTrapIndex"),
)
if mibBuilder.loadTexts:
    mltNetSnmpTrapEntry.setStatus("mandatory")
_MltNetSnmpTrapIfIndex_Type = Integer32
_MltNetSnmpTrapIfIndex_Object = MibTableColumn
mltNetSnmpTrapIfIndex = _MltNetSnmpTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 1),
    _MltNetSnmpTrapIfIndex_Type()
)
mltNetSnmpTrapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSnmpTrapIfIndex.setStatus("mandatory")
_MltNetSnmpTrapIndex_Type = Integer32
_MltNetSnmpTrapIndex_Object = MibTableColumn
mltNetSnmpTrapIndex = _MltNetSnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 2),
    _MltNetSnmpTrapIndex_Type()
)
mltNetSnmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSnmpTrapIndex.setStatus("mandatory")


class _MltNetSnmpTrapCommunity_Type(DisplayString):
    """Custom type mltNetSnmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetSnmpTrapCommunity_Type.__name__ = "DisplayString"
_MltNetSnmpTrapCommunity_Object = MibTableColumn
mltNetSnmpTrapCommunity = _MltNetSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 3),
    _MltNetSnmpTrapCommunity_Type()
)
mltNetSnmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpTrapCommunity.setStatus("mandatory")
_MltNetSnmpTrapIpAddress_Type = IpAddress
_MltNetSnmpTrapIpAddress_Object = MibTableColumn
mltNetSnmpTrapIpAddress = _MltNetSnmpTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 4),
    _MltNetSnmpTrapIpAddress_Type()
)
mltNetSnmpTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpTrapIpAddress.setStatus("mandatory")


class _MltNetSnmpTrapIpxAddress_Type(DisplayString):
    """Custom type mltNetSnmpTrapIpxAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSnmpTrapIpxAddress_Type.__name__ = "DisplayString"
_MltNetSnmpTrapIpxAddress_Object = MibTableColumn
mltNetSnmpTrapIpxAddress = _MltNetSnmpTrapIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 5),
    _MltNetSnmpTrapIpxAddress_Type()
)
mltNetSnmpTrapIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpTrapIpxAddress.setStatus("mandatory")


class _MltNetSnmpTrapOnOff_Type(Integer32):
    """Custom type mltNetSnmpTrapOnOff based on Integer32"""
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


_MltNetSnmpTrapOnOff_Type.__name__ = "Integer32"
_MltNetSnmpTrapOnOff_Object = MibTableColumn
mltNetSnmpTrapOnOff = _MltNetSnmpTrapOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 6, 2, 1, 6),
    _MltNetSnmpTrapOnOff_Type()
)
mltNetSnmpTrapOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSnmpTrapOnOff.setStatus("mandatory")
_MltNetTcpip_ObjectIdentity = ObjectIdentity
mltNetTcpip = _MltNetTcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7)
)
_MltNetTcpipGeneral_ObjectIdentity = ObjectIdentity
mltNetTcpipGeneral = _MltNetTcpipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1)
)
_MltNetTcpipGeneralTable_Object = MibTable
mltNetTcpipGeneralTable = _MltNetTcpipGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    mltNetTcpipGeneralTable.setStatus("mandatory")
_MltNetTcpipGeneralEntry_Object = MibTableRow
mltNetTcpipGeneralEntry = _MltNetTcpipGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1)
)
mltNetTcpipGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetTcpipIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetTcpipGeneralEntry.setStatus("mandatory")
_MltNetTcpipIfIndex_Type = Integer32
_MltNetTcpipIfIndex_Object = MibTableColumn
mltNetTcpipIfIndex = _MltNetTcpipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 1),
    _MltNetTcpipIfIndex_Type()
)
mltNetTcpipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipIfIndex.setStatus("mandatory")


class _MltNetTcpipDefault_Type(Integer32):
    """Custom type mltNetTcpipDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("resetToDefault", 2),
          ("supported", 1))
    )


_MltNetTcpipDefault_Type.__name__ = "Integer32"
_MltNetTcpipDefault_Object = MibTableColumn
mltNetTcpipDefault = _MltNetTcpipDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 2),
    _MltNetTcpipDefault_Type()
)
mltNetTcpipDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipDefault.setStatus("mandatory")
_MltNetTcpipAddress_Type = IpAddress
_MltNetTcpipAddress_Object = MibTableColumn
mltNetTcpipAddress = _MltNetTcpipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 3),
    _MltNetTcpipAddress_Type()
)
mltNetTcpipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipAddress.setStatus("mandatory")
_MltNetTcpipSubnet_Type = IpAddress
_MltNetTcpipSubnet_Object = MibTableColumn
mltNetTcpipSubnet = _MltNetTcpipSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 4),
    _MltNetTcpipSubnet_Type()
)
mltNetTcpipSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipSubnet.setStatus("mandatory")
_MltNetTcpipGateway_Type = IpAddress
_MltNetTcpipGateway_Object = MibTableColumn
mltNetTcpipGateway = _MltNetTcpipGateway_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 5),
    _MltNetTcpipGateway_Type()
)
mltNetTcpipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipGateway.setStatus("mandatory")


class _MltNetTcpipUseBootProtocol_Type(Integer32):
    """Custom type mltNetTcpipUseBootProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neverUse", 0),
          ("useEveryTime", 2),
          ("useWhenNoAddress", 1))
    )


_MltNetTcpipUseBootProtocol_Type.__name__ = "Integer32"
_MltNetTcpipUseBootProtocol_Object = MibTableColumn
mltNetTcpipUseBootProtocol = _MltNetTcpipUseBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 6),
    _MltNetTcpipUseBootProtocol_Type()
)
mltNetTcpipUseBootProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipUseBootProtocol.setStatus("mandatory")
_MltNetTcpipBootProtocolEnable_Type = Integer32
_MltNetTcpipBootProtocolEnable_Object = MibTableColumn
mltNetTcpipBootProtocolEnable = _MltNetTcpipBootProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 7),
    _MltNetTcpipBootProtocolEnable_Type()
)
mltNetTcpipBootProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipBootProtocolEnable.setStatus("mandatory")
_MltNetTcpipAddressServer_Type = IpAddress
_MltNetTcpipAddressServer_Object = MibTableColumn
mltNetTcpipAddressServer = _MltNetTcpipAddressServer_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 8),
    _MltNetTcpipAddressServer_Type()
)
mltNetTcpipAddressServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipAddressServer.setStatus("mandatory")
_MltNetTcpipRawPortNumber_Type = Integer32
_MltNetTcpipRawPortNumber_Object = MibTableColumn
mltNetTcpipRawPortNumber = _MltNetTcpipRawPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 9),
    _MltNetTcpipRawPortNumber_Type()
)
mltNetTcpipRawPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipRawPortNumber.setStatus("mandatory")
_MltNetTcpipSupportService_Type = Integer32
_MltNetTcpipSupportService_Object = MibTableColumn
mltNetTcpipSupportService = _MltNetTcpipSupportService_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 10),
    _MltNetTcpipSupportService_Type()
)
mltNetTcpipSupportService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipSupportService.setStatus("mandatory")


class _MltNetTcpipDnsSupport_Type(Integer32):
    """Custom type mltNetTcpipDnsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUse", 2),
          ("notSupported", 0),
          ("use", 1))
    )


_MltNetTcpipDnsSupport_Type.__name__ = "Integer32"
_MltNetTcpipDnsSupport_Object = MibTableColumn
mltNetTcpipDnsSupport = _MltNetTcpipDnsSupport_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 11),
    _MltNetTcpipDnsSupport_Type()
)
mltNetTcpipDnsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipDnsSupport.setStatus("mandatory")


class _MltNetTcpipDnsHostName_Type(DisplayString):
    """Custom type mltNetTcpipDnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetTcpipDnsHostName_Type.__name__ = "DisplayString"
_MltNetTcpipDnsHostName_Object = MibTableColumn
mltNetTcpipDnsHostName = _MltNetTcpipDnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 12),
    _MltNetTcpipDnsHostName_Type()
)
mltNetTcpipDnsHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipDnsHostName.setStatus("mandatory")


class _MltNetTcpipDnsDomainName_Type(DisplayString):
    """Custom type mltNetTcpipDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetTcpipDnsDomainName_Type.__name__ = "DisplayString"
_MltNetTcpipDnsDomainName_Object = MibTableColumn
mltNetTcpipDnsDomainName = _MltNetTcpipDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 1, 1, 13),
    _MltNetTcpipDnsDomainName_Type()
)
mltNetTcpipDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipDnsDomainName.setStatus("mandatory")
_MltNetTcpipDnsTable_Object = MibTable
mltNetTcpipDnsTable = _MltNetTcpipDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 2)
)
if mibBuilder.loadTexts:
    mltNetTcpipDnsTable.setStatus("mandatory")
_MltNetTcpipDnsEntry_Object = MibTableRow
mltNetTcpipDnsEntry = _MltNetTcpipDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 2, 1)
)
mltNetTcpipDnsEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetTcpipDnsIfIndex"),
    (0, "MC2350-MIB", "mltNetTcpipDnsServerIndex"),
)
if mibBuilder.loadTexts:
    mltNetTcpipDnsEntry.setStatus("mandatory")
_MltNetTcpipDnsIfIndex_Type = Integer32
_MltNetTcpipDnsIfIndex_Object = MibTableColumn
mltNetTcpipDnsIfIndex = _MltNetTcpipDnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 2, 1, 1),
    _MltNetTcpipDnsIfIndex_Type()
)
mltNetTcpipDnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipDnsIfIndex.setStatus("mandatory")
_MltNetTcpipDnsServerIndex_Type = Integer32
_MltNetTcpipDnsServerIndex_Object = MibTableColumn
mltNetTcpipDnsServerIndex = _MltNetTcpipDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 2, 1, 2),
    _MltNetTcpipDnsServerIndex_Type()
)
mltNetTcpipDnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetTcpipDnsServerIndex.setStatus("mandatory")
_MltNetTcpipDnsServerAddress_Type = IpAddress
_MltNetTcpipDnsServerAddress_Object = MibTableColumn
mltNetTcpipDnsServerAddress = _MltNetTcpipDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 1, 2, 1, 3),
    _MltNetTcpipDnsServerAddress_Type()
)
mltNetTcpipDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetTcpipDnsServerAddress.setStatus("mandatory")
_MltNetLpd_ObjectIdentity = ObjectIdentity
mltNetLpd = _MltNetLpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2)
)
_MltNetLpdGeneralTable_Object = MibTable
mltNetLpdGeneralTable = _MltNetLpdGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mltNetLpdGeneralTable.setStatus("mandatory")
_MltNetLpdGeneralEntry_Object = MibTableRow
mltNetLpdGeneralEntry = _MltNetLpdGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 1, 1)
)
mltNetLpdGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetLpdIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetLpdGeneralEntry.setStatus("mandatory")
_MltNetLpdIfIndex_Type = Integer32
_MltNetLpdIfIndex_Object = MibTableColumn
mltNetLpdIfIndex = _MltNetLpdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 1, 1, 1),
    _MltNetLpdIfIndex_Type()
)
mltNetLpdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdIfIndex.setStatus("mandatory")


class _MltNetLpdEnable_Type(Integer32):
    """Custom type mltNetLpdEnable based on Integer32"""
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


_MltNetLpdEnable_Type.__name__ = "Integer32"
_MltNetLpdEnable_Object = MibTableColumn
mltNetLpdEnable = _MltNetLpdEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 1, 1, 2),
    _MltNetLpdEnable_Type()
)
mltNetLpdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetLpdEnable.setStatus("mandatory")
_MltNetLpdPort_Type = Integer32
_MltNetLpdPort_Object = MibTableColumn
mltNetLpdPort = _MltNetLpdPort_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 1, 1, 3),
    _MltNetLpdPort_Type()
)
mltNetLpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetLpdPort.setStatus("mandatory")
_MltNetLpdQueueTable_Object = MibTable
mltNetLpdQueueTable = _MltNetLpdQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2)
)
if mibBuilder.loadTexts:
    mltNetLpdQueueTable.setStatus("mandatory")
_MltNetLpdQueueEntry_Object = MibTableRow
mltNetLpdQueueEntry = _MltNetLpdQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1)
)
mltNetLpdQueueEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetLpdQueueIfIndex"),
    (0, "MC2350-MIB", "mltNetLpdQueueIndex"),
)
if mibBuilder.loadTexts:
    mltNetLpdQueueEntry.setStatus("mandatory")
_MltNetLpdQueueIfIndex_Type = Integer32
_MltNetLpdQueueIfIndex_Object = MibTableColumn
mltNetLpdQueueIfIndex = _MltNetLpdQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 1),
    _MltNetLpdQueueIfIndex_Type()
)
mltNetLpdQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdQueueIfIndex.setStatus("mandatory")
_MltNetLpdQueueIndex_Type = Integer32
_MltNetLpdQueueIndex_Object = MibTableColumn
mltNetLpdQueueIndex = _MltNetLpdQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 2),
    _MltNetLpdQueueIndex_Type()
)
mltNetLpdQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdQueueIndex.setStatus("mandatory")


class _MltNetLpdQueueName_Type(DisplayString):
    """Custom type mltNetLpdQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetLpdQueueName_Type.__name__ = "DisplayString"
_MltNetLpdQueueName_Object = MibTableColumn
mltNetLpdQueueName = _MltNetLpdQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 3),
    _MltNetLpdQueueName_Type()
)
mltNetLpdQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetLpdQueueName.setStatus("mandatory")


class _MltNetLpdQueueDescr_Type(DisplayString):
    """Custom type mltNetLpdQueueDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetLpdQueueDescr_Type.__name__ = "DisplayString"
_MltNetLpdQueueDescr_Object = MibTableColumn
mltNetLpdQueueDescr = _MltNetLpdQueueDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 4),
    _MltNetLpdQueueDescr_Type()
)
mltNetLpdQueueDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetLpdQueueDescr.setStatus("mandatory")
_MltNetLpdQueueFilter_Type = Integer32
_MltNetLpdQueueFilter_Object = MibTableColumn
mltNetLpdQueueFilter = _MltNetLpdQueueFilter_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 5),
    _MltNetLpdQueueFilter_Type()
)
mltNetLpdQueueFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdQueueFilter.setStatus("mandatory")


class _MltNetLpdQueueBanner_Type(Integer32):
    """Custom type mltNetLpdQueueBanner based on Integer32"""
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
        *(("ascii", 1),
          ("noBanner", 0),
          ("pcl", 2),
          ("ps", 3))
    )


_MltNetLpdQueueBanner_Type.__name__ = "Integer32"
_MltNetLpdQueueBanner_Object = MibTableColumn
mltNetLpdQueueBanner = _MltNetLpdQueueBanner_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 6),
    _MltNetLpdQueueBanner_Type()
)
mltNetLpdQueueBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdQueueBanner.setStatus("mandatory")


class _MltNetLpdQueueEnable_Type(Integer32):
    """Custom type mltNetLpdQueueEnable based on Integer32"""
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


_MltNetLpdQueueEnable_Type.__name__ = "Integer32"
_MltNetLpdQueueEnable_Object = MibTableColumn
mltNetLpdQueueEnable = _MltNetLpdQueueEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 2, 2, 1, 7),
    _MltNetLpdQueueEnable_Type()
)
mltNetLpdQueueEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetLpdQueueEnable.setStatus("mandatory")
_MltNetFtpd_ObjectIdentity = ObjectIdentity
mltNetFtpd = _MltNetFtpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6)
)
_MltNetFtpdGeneralTable_Object = MibTable
mltNetFtpdGeneralTable = _MltNetFtpdGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 1)
)
if mibBuilder.loadTexts:
    mltNetFtpdGeneralTable.setStatus("mandatory")
_MltNetFtpdGeneralEntry_Object = MibTableRow
mltNetFtpdGeneralEntry = _MltNetFtpdGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 1, 1)
)
mltNetFtpdGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetFtpdIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetFtpdGeneralEntry.setStatus("mandatory")
_MltNetFtpdIfIndex_Type = Integer32
_MltNetFtpdIfIndex_Object = MibTableColumn
mltNetFtpdIfIndex = _MltNetFtpdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 1, 1, 1),
    _MltNetFtpdIfIndex_Type()
)
mltNetFtpdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdIfIndex.setStatus("mandatory")


class _MltNetFtpdEnable_Type(Integer32):
    """Custom type mltNetFtpdEnable based on Integer32"""
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


_MltNetFtpdEnable_Type.__name__ = "Integer32"
_MltNetFtpdEnable_Object = MibTableColumn
mltNetFtpdEnable = _MltNetFtpdEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 1, 1, 2),
    _MltNetFtpdEnable_Type()
)
mltNetFtpdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetFtpdEnable.setStatus("mandatory")
_MltNetFtpdPort_Type = Integer32
_MltNetFtpdPort_Object = MibTableColumn
mltNetFtpdPort = _MltNetFtpdPort_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 1, 1, 3),
    _MltNetFtpdPort_Type()
)
mltNetFtpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetFtpdPort.setStatus("mandatory")
_MltNetFtpdConfigTable_Object = MibTable
mltNetFtpdConfigTable = _MltNetFtpdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mltNetFtpdConfigTable.setStatus("mandatory")
_MltNetFtpdConfigEntry_Object = MibTableRow
mltNetFtpdConfigEntry = _MltNetFtpdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1)
)
mltNetFtpdConfigEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetFtpdConfigIfIndex"),
    (0, "MC2350-MIB", "mltNetFtpdUserIndex"),
)
if mibBuilder.loadTexts:
    mltNetFtpdConfigEntry.setStatus("mandatory")
_MltNetFtpdConfigIfIndex_Type = Integer32
_MltNetFtpdConfigIfIndex_Object = MibTableColumn
mltNetFtpdConfigIfIndex = _MltNetFtpdConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 1),
    _MltNetFtpdConfigIfIndex_Type()
)
mltNetFtpdConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdConfigIfIndex.setStatus("mandatory")
_MltNetFtpdUserIndex_Type = Integer32
_MltNetFtpdUserIndex_Object = MibTableColumn
mltNetFtpdUserIndex = _MltNetFtpdUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 2),
    _MltNetFtpdUserIndex_Type()
)
mltNetFtpdUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdUserIndex.setStatus("mandatory")


class _MltNetFtpdUser_Type(DisplayString):
    """Custom type mltNetFtpdUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetFtpdUser_Type.__name__ = "DisplayString"
_MltNetFtpdUser_Object = MibTableColumn
mltNetFtpdUser = _MltNetFtpdUser_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 3),
    _MltNetFtpdUser_Type()
)
mltNetFtpdUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdUser.setStatus("mandatory")


class _MltNetFtpdUserPassWd_Type(DisplayString):
    """Custom type mltNetFtpdUserPassWd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MltNetFtpdUserPassWd_Type.__name__ = "DisplayString"
_MltNetFtpdUserPassWd_Object = MibTableColumn
mltNetFtpdUserPassWd = _MltNetFtpdUserPassWd_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 4),
    _MltNetFtpdUserPassWd_Type()
)
mltNetFtpdUserPassWd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdUserPassWd.setStatus("mandatory")
_MltNetFtpdCapability_Type = Integer32
_MltNetFtpdCapability_Object = MibTableColumn
mltNetFtpdCapability = _MltNetFtpdCapability_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 5),
    _MltNetFtpdCapability_Type()
)
mltNetFtpdCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetFtpdCapability.setStatus("mandatory")


class _MltNetFtpdDescr_Type(DisplayString):
    """Custom type mltNetFtpdDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetFtpdDescr_Type.__name__ = "DisplayString"
_MltNetFtpdDescr_Object = MibTableColumn
mltNetFtpdDescr = _MltNetFtpdDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 6, 2, 1, 6),
    _MltNetFtpdDescr_Type()
)
mltNetFtpdDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetFtpdDescr.setStatus("mandatory")
_MltNetHttpd_ObjectIdentity = ObjectIdentity
mltNetHttpd = _MltNetHttpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8)
)
_MltNetHttpdGeneralTable_Object = MibTable
mltNetHttpdGeneralTable = _MltNetHttpdGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1)
)
if mibBuilder.loadTexts:
    mltNetHttpdGeneralTable.setStatus("mandatory")
_MltNetHttpdGeneralEntry_Object = MibTableRow
mltNetHttpdGeneralEntry = _MltNetHttpdGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1, 1)
)
mltNetHttpdGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetHttpdIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetHttpdGeneralEntry.setStatus("mandatory")
_MltNetHttpdIfIndex_Type = Integer32
_MltNetHttpdIfIndex_Object = MibTableColumn
mltNetHttpdIfIndex = _MltNetHttpdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1, 1, 1),
    _MltNetHttpdIfIndex_Type()
)
mltNetHttpdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetHttpdIfIndex.setStatus("mandatory")


class _MltNetHttpdEnable_Type(Integer32):
    """Custom type mltNetHttpdEnable based on Integer32"""
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


_MltNetHttpdEnable_Type.__name__ = "Integer32"
_MltNetHttpdEnable_Object = MibTableColumn
mltNetHttpdEnable = _MltNetHttpdEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1, 1, 2),
    _MltNetHttpdEnable_Type()
)
mltNetHttpdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetHttpdEnable.setStatus("mandatory")
_MltNetHttpdPort_Type = Integer32
_MltNetHttpdPort_Object = MibTableColumn
mltNetHttpdPort = _MltNetHttpdPort_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1, 1, 3),
    _MltNetHttpdPort_Type()
)
mltNetHttpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetHttpdPort.setStatus("mandatory")


class _MltNetHttpdDescr_Type(DisplayString):
    """Custom type mltNetHttpdDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetHttpdDescr_Type.__name__ = "DisplayString"
_MltNetHttpdDescr_Object = MibTableColumn
mltNetHttpdDescr = _MltNetHttpdDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 8, 1, 1, 4),
    _MltNetHttpdDescr_Type()
)
mltNetHttpdDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetHttpdDescr.setStatus("mandatory")
_MltNetSmtpClient_ObjectIdentity = ObjectIdentity
mltNetSmtpClient = _MltNetSmtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13)
)
_MltNetSmtpGeneralTable_Object = MibTable
mltNetSmtpGeneralTable = _MltNetSmtpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1)
)
if mibBuilder.loadTexts:
    mltNetSmtpGeneralTable.setStatus("mandatory")
_MltNetSmtpGeneralEntry_Object = MibTableRow
mltNetSmtpGeneralEntry = _MltNetSmtpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1, 1)
)
mltNetSmtpGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSmtpIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetSmtpGeneralEntry.setStatus("mandatory")
_MltNetSmtpIfIndex_Type = Integer32
_MltNetSmtpIfIndex_Object = MibTableColumn
mltNetSmtpIfIndex = _MltNetSmtpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1, 1, 1),
    _MltNetSmtpIfIndex_Type()
)
mltNetSmtpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmtpIfIndex.setStatus("mandatory")


class _MltNetSmtpEnable_Type(Integer32):
    """Custom type mltNetSmtpEnable based on Integer32"""
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


_MltNetSmtpEnable_Type.__name__ = "Integer32"
_MltNetSmtpEnable_Object = MibTableColumn
mltNetSmtpEnable = _MltNetSmtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1, 1, 2),
    _MltNetSmtpEnable_Type()
)
mltNetSmtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpEnable.setStatus("mandatory")


class _MltNetSmtpServerAddress_Type(DisplayString):
    """Custom type mltNetSmtpServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetSmtpServerAddress_Type.__name__ = "DisplayString"
_MltNetSmtpServerAddress_Object = MibTableColumn
mltNetSmtpServerAddress = _MltNetSmtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1, 1, 3),
    _MltNetSmtpServerAddress_Type()
)
mltNetSmtpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmtpServerAddress.setStatus("mandatory")
_MltNetSmtpPort_Type = Integer32
_MltNetSmtpPort_Object = MibTableColumn
mltNetSmtpPort = _MltNetSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 1, 1, 4),
    _MltNetSmtpPort_Type()
)
mltNetSmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpPort.setStatus("mandatory")
_MltNetSmtpAccountTable_Object = MibTable
mltNetSmtpAccountTable = _MltNetSmtpAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2)
)
if mibBuilder.loadTexts:
    mltNetSmtpAccountTable.setStatus("mandatory")
_MltNetSmtpAccountEntry_Object = MibTableRow
mltNetSmtpAccountEntry = _MltNetSmtpAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1)
)
mltNetSmtpAccountEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSmtpAccountIfIndex"),
    (0, "MC2350-MIB", "mltNetSmtpAccountIndex"),
)
if mibBuilder.loadTexts:
    mltNetSmtpAccountEntry.setStatus("mandatory")
_MltNetSmtpAccountIfIndex_Type = Integer32
_MltNetSmtpAccountIfIndex_Object = MibTableColumn
mltNetSmtpAccountIfIndex = _MltNetSmtpAccountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 1),
    _MltNetSmtpAccountIfIndex_Type()
)
mltNetSmtpAccountIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmtpAccountIfIndex.setStatus("mandatory")
_MltNetSmtpAccountIndex_Type = Integer32
_MltNetSmtpAccountIndex_Object = MibTableColumn
mltNetSmtpAccountIndex = _MltNetSmtpAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 2),
    _MltNetSmtpAccountIndex_Type()
)
mltNetSmtpAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmtpAccountIndex.setStatus("mandatory")


class _MltNetSmtpFromAddress_Type(DisplayString):
    """Custom type mltNetSmtpFromAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_MltNetSmtpFromAddress_Type.__name__ = "DisplayString"
_MltNetSmtpFromAddress_Object = MibTableColumn
mltNetSmtpFromAddress = _MltNetSmtpFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 3),
    _MltNetSmtpFromAddress_Type()
)
mltNetSmtpFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpFromAddress.setStatus("mandatory")


class _MltNetSmtpReplyAddress_Type(DisplayString):
    """Custom type mltNetSmtpReplyAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_MltNetSmtpReplyAddress_Type.__name__ = "DisplayString"
_MltNetSmtpReplyAddress_Object = MibTableColumn
mltNetSmtpReplyAddress = _MltNetSmtpReplyAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 4),
    _MltNetSmtpReplyAddress_Type()
)
mltNetSmtpReplyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpReplyAddress.setStatus("mandatory")
_MltNetSmtpConnTimeout_Type = Integer32
_MltNetSmtpConnTimeout_Object = MibTableColumn
mltNetSmtpConnTimeout = _MltNetSmtpConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 5),
    _MltNetSmtpConnTimeout_Type()
)
mltNetSmtpConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpConnTimeout.setStatus("mandatory")


class _MltNetSmtpPurpose_Type(Integer32):
    """Custom type mltNetSmtpPurpose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("epNet", 1),
          ("other", 0),
          ("scanFunction", 2))
    )


_MltNetSmtpPurpose_Type.__name__ = "Integer32"
_MltNetSmtpPurpose_Object = MibTableColumn
mltNetSmtpPurpose = _MltNetSmtpPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 6),
    _MltNetSmtpPurpose_Type()
)
mltNetSmtpPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmtpPurpose.setStatus("mandatory")


class _MltNetSmtpDescription_Type(DisplayString):
    """Custom type mltNetSmtpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSmtpDescription_Type.__name__ = "DisplayString"
_MltNetSmtpDescription_Object = MibTableColumn
mltNetSmtpDescription = _MltNetSmtpDescription_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 13, 2, 1, 7),
    _MltNetSmtpDescription_Type()
)
mltNetSmtpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmtpDescription.setStatus("mandatory")
_MltNetIpp_ObjectIdentity = ObjectIdentity
mltNetIpp = _MltNetIpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14)
)
_MltNetIppGeneral_ObjectIdentity = ObjectIdentity
mltNetIppGeneral = _MltNetIppGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1)
)
_MltNetIppGeneralTable_Object = MibTable
mltNetIppGeneralTable = _MltNetIppGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 1)
)
if mibBuilder.loadTexts:
    mltNetIppGeneralTable.setStatus("optional")
_MltNetIppGeneralEntry_Object = MibTableRow
mltNetIppGeneralEntry = _MltNetIppGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 1, 1)
)
mltNetIppGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetIppGeneralIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetIppGeneralEntry.setStatus("optional")
_MltNetIppGeneralIfIndex_Type = Integer32
_MltNetIppGeneralIfIndex_Object = MibTableColumn
mltNetIppGeneralIfIndex = _MltNetIppGeneralIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 1, 1, 1),
    _MltNetIppGeneralIfIndex_Type()
)
mltNetIppGeneralIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetIppGeneralIfIndex.setStatus("optional")


class _MltNetIppServiceEnable_Type(Integer32):
    """Custom type mltNetIppServiceEnable based on Integer32"""
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


_MltNetIppServiceEnable_Type.__name__ = "Integer32"
_MltNetIppServiceEnable_Object = MibTableColumn
mltNetIppServiceEnable = _MltNetIppServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 1, 1, 2),
    _MltNetIppServiceEnable_Type()
)
mltNetIppServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetIppServiceEnable.setStatus("optional")
_MltNetIppDefaultPortIndex_Type = Integer32
_MltNetIppDefaultPortIndex_Object = MibTableColumn
mltNetIppDefaultPortIndex = _MltNetIppDefaultPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 1, 1, 3),
    _MltNetIppDefaultPortIndex_Type()
)
mltNetIppDefaultPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetIppDefaultPortIndex.setStatus("optional")
_MltNetIppPortTable_Object = MibTable
mltNetIppPortTable = _MltNetIppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 2)
)
if mibBuilder.loadTexts:
    mltNetIppPortTable.setStatus("optional")
_MltNetIppPortEntry_Object = MibTableRow
mltNetIppPortEntry = _MltNetIppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 2, 1)
)
mltNetIppPortEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetIppPortIfIndex"),
    (0, "MC2350-MIB", "mltNetIppPortIndex"),
)
if mibBuilder.loadTexts:
    mltNetIppPortEntry.setStatus("optional")
_MltNetIppPortIfIndex_Type = Integer32
_MltNetIppPortIfIndex_Object = MibTableColumn
mltNetIppPortIfIndex = _MltNetIppPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 2, 1, 1),
    _MltNetIppPortIfIndex_Type()
)
mltNetIppPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetIppPortIfIndex.setStatus("optional")
_MltNetIppPortIndex_Type = Integer32
_MltNetIppPortIndex_Object = MibTableColumn
mltNetIppPortIndex = _MltNetIppPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 2, 1, 2),
    _MltNetIppPortIndex_Type()
)
mltNetIppPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetIppPortIndex.setStatus("optional")
_MltNetIppPortNumber_Type = Integer32
_MltNetIppPortNumber_Object = MibTableColumn
mltNetIppPortNumber = _MltNetIppPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 1, 2, 1, 3),
    _MltNetIppPortNumber_Type()
)
mltNetIppPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetIppPortNumber.setStatus("optional")
_MltNetIppPrtDescrAttribute_ObjectIdentity = ObjectIdentity
mltNetIppPrtDescrAttribute = _MltNetIppPrtDescrAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2)
)
_MltNetIppPrtDescGeneralTable_Object = MibTable
mltNetIppPrtDescGeneralTable = _MltNetIppPrtDescGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mltNetIppPrtDescGeneralTable.setStatus("optional")
_MltNetIppPrtDescGeneralEntry_Object = MibTableRow
mltNetIppPrtDescGeneralEntry = _MltNetIppPrtDescGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1)
)
mltNetIppPrtDescGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppPrtDescGeneralIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetIppPrtDescGeneralEntry.setStatus("optional")
_MltIppPrtDescGeneralIfIndex_Type = Integer32
_MltIppPrtDescGeneralIfIndex_Object = MibTableColumn
mltIppPrtDescGeneralIfIndex = _MltIppPrtDescGeneralIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 1),
    _MltIppPrtDescGeneralIfIndex_Type()
)
mltIppPrtDescGeneralIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrtDescGeneralIfIndex.setStatus("optional")


class _MltIppPrtName_Type(DisplayString):
    """Custom type mltIppPrtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppPrtName_Type.__name__ = "DisplayString"
_MltIppPrtName_Object = MibTableColumn
mltIppPrtName = _MltIppPrtName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 2),
    _MltIppPrtName_Type()
)
mltIppPrtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrtName.setStatus("optional")


class _MltIppPrtMoreInfo_Type(DisplayString):
    """Custom type mltIppPrtMoreInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppPrtMoreInfo_Type.__name__ = "DisplayString"
_MltIppPrtMoreInfo_Object = MibTableColumn
mltIppPrtMoreInfo = _MltIppPrtMoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 3),
    _MltIppPrtMoreInfo_Type()
)
mltIppPrtMoreInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrtMoreInfo.setStatus("optional")


class _MltIppPrtState_Type(Integer32):
    """Custom type mltIppPrtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 3),
          ("processing", 4),
          ("stopped", 5))
    )


_MltIppPrtState_Type.__name__ = "Integer32"
_MltIppPrtState_Object = MibTableColumn
mltIppPrtState = _MltIppPrtState_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 4),
    _MltIppPrtState_Type()
)
mltIppPrtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrtState.setStatus("optional")
_MltIppCharSetConfiguredIndex_Type = Integer32
_MltIppCharSetConfiguredIndex_Object = MibTableColumn
mltIppCharSetConfiguredIndex = _MltIppCharSetConfiguredIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 5),
    _MltIppCharSetConfiguredIndex_Type()
)
mltIppCharSetConfiguredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCharSetConfiguredIndex.setStatus("optional")
_MltIppNaturalLanguageConfiguredIndex_Type = Integer32
_MltIppNaturalLanguageConfiguredIndex_Object = MibTableColumn
mltIppNaturalLanguageConfiguredIndex = _MltIppNaturalLanguageConfiguredIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 6),
    _MltIppNaturalLanguageConfiguredIndex_Type()
)
mltIppNaturalLanguageConfiguredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNaturalLanguageConfiguredIndex.setStatus("optional")
_MltIppDocFormatDefaultIndex_Type = Integer32
_MltIppDocFormatDefaultIndex_Object = MibTableColumn
mltIppDocFormatDefaultIndex = _MltIppDocFormatDefaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 7),
    _MltIppDocFormatDefaultIndex_Type()
)
mltIppDocFormatDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppDocFormatDefaultIndex.setStatus("optional")


class _MltIppPrinterIsAcceptingJobs_Type(Integer32):
    """Custom type mltIppPrinterIsAcceptingJobs based on Integer32"""
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


_MltIppPrinterIsAcceptingJobs_Type.__name__ = "Integer32"
_MltIppPrinterIsAcceptingJobs_Object = MibTableColumn
mltIppPrinterIsAcceptingJobs = _MltIppPrinterIsAcceptingJobs_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 8),
    _MltIppPrinterIsAcceptingJobs_Type()
)
mltIppPrinterIsAcceptingJobs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrinterIsAcceptingJobs.setStatus("optional")
_MltIppQueuedJobCount_Type = Counter32
_MltIppQueuedJobCount_Object = MibTableColumn
mltIppQueuedJobCount = _MltIppQueuedJobCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 9),
    _MltIppQueuedJobCount_Type()
)
mltIppQueuedJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppQueuedJobCount.setStatus("optional")


class _MltIppColorSupported_Type(Integer32):
    """Custom type mltIppColorSupported based on Integer32"""
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


_MltIppColorSupported_Type.__name__ = "Integer32"
_MltIppColorSupported_Object = MibTableColumn
mltIppColorSupported = _MltIppColorSupported_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 10),
    _MltIppColorSupported_Type()
)
mltIppColorSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppColorSupported.setStatus("optional")


class _MltIppPdlOverrideSupported_Type(Integer32):
    """Custom type mltIppPdlOverrideSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("attempted", 3),
          ("notAttempted", 4))
    )


_MltIppPdlOverrideSupported_Type.__name__ = "Integer32"
_MltIppPdlOverrideSupported_Object = MibTableColumn
mltIppPdlOverrideSupported = _MltIppPdlOverrideSupported_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 11),
    _MltIppPdlOverrideSupported_Type()
)
mltIppPdlOverrideSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPdlOverrideSupported.setStatus("optional")
_MltIppPrinterUpTime_Type = TimeTicks
_MltIppPrinterUpTime_Object = MibTableColumn
mltIppPrinterUpTime = _MltIppPrinterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 12),
    _MltIppPrinterUpTime_Type()
)
mltIppPrinterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrinterUpTime.setStatus("optional")


class _MltIppPrtLocation_Type(DisplayString):
    """Custom type mltIppPrtLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppPrtLocation_Type.__name__ = "DisplayString"
_MltIppPrtLocation_Object = MibTableColumn
mltIppPrtLocation = _MltIppPrtLocation_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 13),
    _MltIppPrtLocation_Type()
)
mltIppPrtLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrtLocation.setStatus("optional")
_MltIppPrinterCurrentTime_Type = DateAndTime
_MltIppPrinterCurrentTime_Object = MibTableColumn
mltIppPrinterCurrentTime = _MltIppPrinterCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 1, 1, 21),
    _MltIppPrinterCurrentTime_Type()
)
mltIppPrinterCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrinterCurrentTime.setStatus("optional")
_MltIppUriSupportedTable_Object = MibTable
mltIppUriSupportedTable = _MltIppUriSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2)
)
if mibBuilder.loadTexts:
    mltIppUriSupportedTable.setStatus("optional")
_MltIppUriSupportedEntry_Object = MibTableRow
mltIppUriSupportedEntry = _MltIppUriSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1)
)
mltIppUriSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppUriIfIndex"),
    (0, "MC2350-MIB", "mltIppUriIndex"),
)
if mibBuilder.loadTexts:
    mltIppUriSupportedEntry.setStatus("optional")
_MltIppUriIfIndex_Type = Integer32
_MltIppUriIfIndex_Object = MibTableColumn
mltIppUriIfIndex = _MltIppUriIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1, 1),
    _MltIppUriIfIndex_Type()
)
mltIppUriIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppUriIfIndex.setStatus("optional")
_MltIppUriIndex_Type = Integer32
_MltIppUriIndex_Object = MibTableColumn
mltIppUriIndex = _MltIppUriIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1, 2),
    _MltIppUriIndex_Type()
)
mltIppUriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppUriIndex.setStatus("optional")


class _MltIppUri_Type(DisplayString):
    """Custom type mltIppUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppUri_Type.__name__ = "DisplayString"
_MltIppUri_Object = MibTableColumn
mltIppUri = _MltIppUri_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1, 3),
    _MltIppUri_Type()
)
mltIppUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppUri.setStatus("optional")


class _MltIppUriSecurity_Type(Integer32):
    """Custom type mltIppUriSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("ssl3", 4),
          ("tls", 5))
    )


_MltIppUriSecurity_Type.__name__ = "Integer32"
_MltIppUriSecurity_Object = MibTableColumn
mltIppUriSecurity = _MltIppUriSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1, 4),
    _MltIppUriSecurity_Type()
)
mltIppUriSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppUriSecurity.setStatus("optional")


class _MltIppUriAuthentication_Type(Integer32):
    """Custom type mltIppUriAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("basic", 5),
          ("certificate", 7),
          ("digest", 6),
          ("none", 3),
          ("requestingUserName", 4))
    )


_MltIppUriAuthentication_Type.__name__ = "Integer32"
_MltIppUriAuthentication_Object = MibTableColumn
mltIppUriAuthentication = _MltIppUriAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 2, 1, 5),
    _MltIppUriAuthentication_Type()
)
mltIppUriAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppUriAuthentication.setStatus("optional")
_MltIppPrtStateReasonsTable_Object = MibTable
mltIppPrtStateReasonsTable = _MltIppPrtStateReasonsTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3)
)
if mibBuilder.loadTexts:
    mltIppPrtStateReasonsTable.setStatus("optional")
_MltIppPrtStateReasonsEntry_Object = MibTableRow
mltIppPrtStateReasonsEntry = _MltIppPrtStateReasonsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3, 1)
)
mltIppPrtStateReasonsEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppPrtStateReasonIfIndex"),
    (0, "MC2350-MIB", "mltIppPrtStateReasonIndex"),
)
if mibBuilder.loadTexts:
    mltIppPrtStateReasonsEntry.setStatus("optional")
_MltIppPrtStateReasonIfIndex_Type = Integer32
_MltIppPrtStateReasonIfIndex_Object = MibTableColumn
mltIppPrtStateReasonIfIndex = _MltIppPrtStateReasonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3, 1, 1),
    _MltIppPrtStateReasonIfIndex_Type()
)
mltIppPrtStateReasonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrtStateReasonIfIndex.setStatus("optional")
_MltIppPrtStateReasonIndex_Type = Integer32
_MltIppPrtStateReasonIndex_Object = MibTableColumn
mltIppPrtStateReasonIndex = _MltIppPrtStateReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3, 1, 2),
    _MltIppPrtStateReasonIndex_Type()
)
mltIppPrtStateReasonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrtStateReasonIndex.setStatus("optional")


class _MltIppPrinterStateReason_Type(Integer32):
    """Custom type mltIppPrinterStateReason based on Integer32"""
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
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("connectingToDevice", 9),
          ("coverOpen", 16),
          ("developerEmpty", 34),
          ("developerLow", 33),
          ("doorOpen", 18),
          ("fuserOverTemp", 29),
          ("fuserUnderTemp", 30),
          ("inputTrayMissing", 19),
          ("interlockOpen", 17),
          ("interpreterResourceUnavailable", 35),
          ("markerSupplyEmpty", 26),
          ("markerSupplyLow", 25),
          ("markerWasteAlmostFull", 27),
          ("markerWasteFull", 28),
          ("mediaEmpty", 21),
          ("mediaJam", 5),
          ("mediaLow", 20),
          ("mediaNeeded", 4),
          ("movingToPaused", 6),
          ("none", 3),
          ("opcLifeOver", 32),
          ("opcNearEndOfLife", 31),
          ("other", 2),
          ("outputAreaAlmostFull", 23),
          ("outputAreaFull", 24),
          ("outputTrayMissing", 22),
          ("paused", 7),
          ("shutDown", 8),
          ("spoolAreaFull", 15),
          ("stoppedPartly", 12),
          ("stopping", 11),
          ("timedOut", 10),
          ("tonerEmpty", 14),
          ("tonerLow", 13))
    )


_MltIppPrinterStateReason_Type.__name__ = "Integer32"
_MltIppPrinterStateReason_Object = MibTableColumn
mltIppPrinterStateReason = _MltIppPrinterStateReason_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3, 1, 3),
    _MltIppPrinterStateReason_Type()
)
mltIppPrinterStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrinterStateReason.setStatus("optional")


class _MltIppPrtStateReasonSuffix_Type(Integer32):
    """Custom type mltIppPrtStateReasonSuffix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", 5),
          ("report", 3),
          ("warning", 4))
    )


_MltIppPrtStateReasonSuffix_Type.__name__ = "Integer32"
_MltIppPrtStateReasonSuffix_Object = MibTableColumn
mltIppPrtStateReasonSuffix = _MltIppPrtStateReasonSuffix_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 3, 1, 4),
    _MltIppPrtStateReasonSuffix_Type()
)
mltIppPrtStateReasonSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPrtStateReasonSuffix.setStatus("optional")
_MltIppVersionsSupportedTable_Object = MibTable
mltIppVersionsSupportedTable = _MltIppVersionsSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 4)
)
if mibBuilder.loadTexts:
    mltIppVersionsSupportedTable.setStatus("optional")
_MltIppVersionsSupportedEntry_Object = MibTableRow
mltIppVersionsSupportedEntry = _MltIppVersionsSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 4, 1)
)
mltIppVersionsSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppVersionIfIndex"),
    (0, "MC2350-MIB", "mltIppVersionIndex"),
)
if mibBuilder.loadTexts:
    mltIppVersionsSupportedEntry.setStatus("optional")
_MltIppVersionIfIndex_Type = Integer32
_MltIppVersionIfIndex_Object = MibTableColumn
mltIppVersionIfIndex = _MltIppVersionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 4, 1, 1),
    _MltIppVersionIfIndex_Type()
)
mltIppVersionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppVersionIfIndex.setStatus("optional")
_MltIppVersionIndex_Type = Integer32
_MltIppVersionIndex_Object = MibTableColumn
mltIppVersionIndex = _MltIppVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 4, 1, 2),
    _MltIppVersionIndex_Type()
)
mltIppVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppVersionIndex.setStatus("optional")


class _MltIppVersionType_Type(Integer32):
    """Custom type mltIppVersionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipp10", 3),
          ("ipp11", 4))
    )


_MltIppVersionType_Type.__name__ = "Integer32"
_MltIppVersionType_Object = MibTableColumn
mltIppVersionType = _MltIppVersionType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 4, 1, 3),
    _MltIppVersionType_Type()
)
mltIppVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppVersionType.setStatus("optional")
_MltIppOperationSupportedTable_Object = MibTable
mltIppOperationSupportedTable = _MltIppOperationSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5)
)
if mibBuilder.loadTexts:
    mltIppOperationSupportedTable.setStatus("optional")
_MltIppOperationSupportedEntry_Object = MibTableRow
mltIppOperationSupportedEntry = _MltIppOperationSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5, 1)
)
mltIppOperationSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppOperationIfIndex"),
    (0, "MC2350-MIB", "mltIppOperationIndex"),
)
if mibBuilder.loadTexts:
    mltIppOperationSupportedEntry.setStatus("optional")
_MltIppOperationIfIndex_Type = Integer32
_MltIppOperationIfIndex_Object = MibTableColumn
mltIppOperationIfIndex = _MltIppOperationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5, 1, 1),
    _MltIppOperationIfIndex_Type()
)
mltIppOperationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOperationIfIndex.setStatus("optional")
_MltIppOperationIndex_Type = Integer32
_MltIppOperationIndex_Object = MibTableColumn
mltIppOperationIndex = _MltIppOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5, 1, 2),
    _MltIppOperationIndex_Type()
)
mltIppOperationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOperationIndex.setStatus("optional")


class _MltIppOperationType_Type(Integer32):
    """Custom type mltIppOperationType based on Integer32"""
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
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("cancelJob", 8),
          ("createJob", 5),
          ("getJobAttributes", 9),
          ("getJobs", 10),
          ("getPrinterAttributes", 11),
          ("holdJobs", 12),
          ("pausePrinter", 16),
          ("printJob", 2),
          ("printURI", 3),
          ("purgeJobs", 18),
          ("releaseJob", 13),
          ("restartJob", 14),
          ("resumePrinter", 17),
          ("sendDocument", 6),
          ("sendURI", 7),
          ("validateJob", 4))
    )


_MltIppOperationType_Type.__name__ = "Integer32"
_MltIppOperationType_Object = MibTableColumn
mltIppOperationType = _MltIppOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5, 1, 3),
    _MltIppOperationType_Type()
)
mltIppOperationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOperationType.setStatus("optional")


class _MltIppOperationEnable_Type(Integer32):
    """Custom type mltIppOperationEnable based on Integer32"""
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


_MltIppOperationEnable_Type.__name__ = "Integer32"
_MltIppOperationEnable_Object = MibTableColumn
mltIppOperationEnable = _MltIppOperationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 5, 1, 4),
    _MltIppOperationEnable_Type()
)
mltIppOperationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppOperationEnable.setStatus("optional")
_MltIppCharSetSupportedTable_Object = MibTable
mltIppCharSetSupportedTable = _MltIppCharSetSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6)
)
if mibBuilder.loadTexts:
    mltIppCharSetSupportedTable.setStatus("optional")
_MltIppCharSetSupportedEntry_Object = MibTableRow
mltIppCharSetSupportedEntry = _MltIppCharSetSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6, 1)
)
mltIppCharSetSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppCharSetIfIndex"),
    (0, "MC2350-MIB", "mltIppCharSetIndex"),
)
if mibBuilder.loadTexts:
    mltIppCharSetSupportedEntry.setStatus("optional")
_MltIppCharSetIfIndex_Type = Integer32
_MltIppCharSetIfIndex_Object = MibTableColumn
mltIppCharSetIfIndex = _MltIppCharSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6, 1, 1),
    _MltIppCharSetIfIndex_Type()
)
mltIppCharSetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCharSetIfIndex.setStatus("optional")
_MltIppCharSetIndex_Type = Integer32
_MltIppCharSetIndex_Object = MibTableColumn
mltIppCharSetIndex = _MltIppCharSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6, 1, 2),
    _MltIppCharSetIndex_Type()
)
mltIppCharSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCharSetIndex.setStatus("optional")


class _MltIppCharSetName_Type(DisplayString):
    """Custom type mltIppCharSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppCharSetName_Type.__name__ = "DisplayString"
_MltIppCharSetName_Object = MibTableColumn
mltIppCharSetName = _MltIppCharSetName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6, 1, 3),
    _MltIppCharSetName_Type()
)
mltIppCharSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCharSetName.setStatus("optional")
_MltIppCharSetCode_Type = Integer32
_MltIppCharSetCode_Object = MibTableColumn
mltIppCharSetCode = _MltIppCharSetCode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 6, 1, 4),
    _MltIppCharSetCode_Type()
)
mltIppCharSetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCharSetCode.setStatus("optional")
_MltIppNaturalLanguageSupportedTable_Object = MibTable
mltIppNaturalLanguageSupportedTable = _MltIppNaturalLanguageSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 7)
)
if mibBuilder.loadTexts:
    mltIppNaturalLanguageSupportedTable.setStatus("optional")
_MltIppNaturalLanguageSupportedEntry_Object = MibTableRow
mltIppNaturalLanguageSupportedEntry = _MltIppNaturalLanguageSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 7, 1)
)
mltIppNaturalLanguageSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppNaturalLangIfIndex"),
    (0, "MC2350-MIB", "mltIppNaturalLangIndex"),
)
if mibBuilder.loadTexts:
    mltIppNaturalLanguageSupportedEntry.setStatus("optional")
_MltIppNaturalLangIfIndex_Type = Integer32
_MltIppNaturalLangIfIndex_Object = MibTableColumn
mltIppNaturalLangIfIndex = _MltIppNaturalLangIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 7, 1, 1),
    _MltIppNaturalLangIfIndex_Type()
)
mltIppNaturalLangIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNaturalLangIfIndex.setStatus("optional")
_MltIppNaturalLangIndex_Type = Integer32
_MltIppNaturalLangIndex_Object = MibTableColumn
mltIppNaturalLangIndex = _MltIppNaturalLangIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 7, 1, 2),
    _MltIppNaturalLangIndex_Type()
)
mltIppNaturalLangIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNaturalLangIndex.setStatus("optional")


class _MltIppNaturalLangName_Type(DisplayString):
    """Custom type mltIppNaturalLangName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppNaturalLangName_Type.__name__ = "DisplayString"
_MltIppNaturalLangName_Object = MibTableColumn
mltIppNaturalLangName = _MltIppNaturalLangName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 7, 1, 3),
    _MltIppNaturalLangName_Type()
)
mltIppNaturalLangName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNaturalLangName.setStatus("optional")
_MltIppDocFormatSupportedTable_Object = MibTable
mltIppDocFormatSupportedTable = _MltIppDocFormatSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 8)
)
if mibBuilder.loadTexts:
    mltIppDocFormatSupportedTable.setStatus("optional")
_MltIppDocFormatSupportedEntry_Object = MibTableRow
mltIppDocFormatSupportedEntry = _MltIppDocFormatSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 8, 1)
)
mltIppDocFormatSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppDocFormatIfIndex"),
    (0, "MC2350-MIB", "mltIppDocFormatIndex"),
)
if mibBuilder.loadTexts:
    mltIppDocFormatSupportedEntry.setStatus("optional")
_MltIppDocFormatIfIndex_Type = Integer32
_MltIppDocFormatIfIndex_Object = MibTableColumn
mltIppDocFormatIfIndex = _MltIppDocFormatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 8, 1, 1),
    _MltIppDocFormatIfIndex_Type()
)
mltIppDocFormatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppDocFormatIfIndex.setStatus("optional")
_MltIppDocFormatIndex_Type = Integer32
_MltIppDocFormatIndex_Object = MibTableColumn
mltIppDocFormatIndex = _MltIppDocFormatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 8, 1, 2),
    _MltIppDocFormatIndex_Type()
)
mltIppDocFormatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppDocFormatIndex.setStatus("optional")


class _MltIppDocFormatName_Type(DisplayString):
    """Custom type mltIppDocFormatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MltIppDocFormatName_Type.__name__ = "DisplayString"
_MltIppDocFormatName_Object = MibTableColumn
mltIppDocFormatName = _MltIppDocFormatName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 8, 1, 3),
    _MltIppDocFormatName_Type()
)
mltIppDocFormatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppDocFormatName.setStatus("optional")
_MltIppCompressionSupportedTable_Object = MibTable
mltIppCompressionSupportedTable = _MltIppCompressionSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mltIppCompressionSupportedTable.setStatus("optional")
_MltIppCompressionSupportedEntry_Object = MibTableRow
mltIppCompressionSupportedEntry = _MltIppCompressionSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 10, 1)
)
mltIppCompressionSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppCompressionIfIndex"),
    (0, "MC2350-MIB", "mltIppCompressionIndex"),
)
if mibBuilder.loadTexts:
    mltIppCompressionSupportedEntry.setStatus("optional")
_MltIppCompressionIfIndex_Type = Integer32
_MltIppCompressionIfIndex_Object = MibTableColumn
mltIppCompressionIfIndex = _MltIppCompressionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 10, 1, 1),
    _MltIppCompressionIfIndex_Type()
)
mltIppCompressionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCompressionIfIndex.setStatus("optional")
_MltIppCompressionIndex_Type = Integer32
_MltIppCompressionIndex_Object = MibTableColumn
mltIppCompressionIndex = _MltIppCompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 10, 1, 2),
    _MltIppCompressionIndex_Type()
)
mltIppCompressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCompressionIndex.setStatus("optional")


class _MltIppCompressionType_Type(Integer32):
    """Custom type mltIppCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compress", 6),
          ("deflate", 4),
          ("gzip", 5),
          ("none", 3))
    )


_MltIppCompressionType_Type.__name__ = "Integer32"
_MltIppCompressionType_Object = MibTableColumn
mltIppCompressionType = _MltIppCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 2, 10, 1, 3),
    _MltIppCompressionType_Type()
)
mltIppCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCompressionType.setStatus("optional")
_MltNetIppJobTemplateAttribute_ObjectIdentity = ObjectIdentity
mltNetIppJobTemplateAttribute = _MltNetIppJobTemplateAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3)
)
_MltNetIppJobTemplateGeneralTable_Object = MibTable
mltNetIppJobTemplateGeneralTable = _MltNetIppJobTemplateGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1)
)
if mibBuilder.loadTexts:
    mltNetIppJobTemplateGeneralTable.setStatus("optional")
_MltNetIppJobTemplateGeneralEntry_Object = MibTableRow
mltNetIppJobTemplateGeneralEntry = _MltNetIppJobTemplateGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1)
)
mltNetIppJobTemplateGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppJobTemplateGeneralIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetIppJobTemplateGeneralEntry.setStatus("optional")
_MltIppJobTemplateGeneralIfIndex_Type = Integer32
_MltIppJobTemplateGeneralIfIndex_Object = MibTableColumn
mltIppJobTemplateGeneralIfIndex = _MltIppJobTemplateGeneralIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 1),
    _MltIppJobTemplateGeneralIfIndex_Type()
)
mltIppJobTemplateGeneralIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobTemplateGeneralIfIndex.setStatus("optional")
_MltIppJobPriorityDefault_Type = Integer32
_MltIppJobPriorityDefault_Object = MibTableColumn
mltIppJobPriorityDefault = _MltIppJobPriorityDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 2),
    _MltIppJobPriorityDefault_Type()
)
mltIppJobPriorityDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobPriorityDefault.setStatus("optional")
_MltIppJobPrioritySupported_Type = Integer32
_MltIppJobPrioritySupported_Object = MibTableColumn
mltIppJobPrioritySupported = _MltIppJobPrioritySupported_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 3),
    _MltIppJobPrioritySupported_Type()
)
mltIppJobPrioritySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobPrioritySupported.setStatus("optional")
_MltIppJobHoldUntilDefault_Type = Integer32
_MltIppJobHoldUntilDefault_Object = MibTableColumn
mltIppJobHoldUntilDefault = _MltIppJobHoldUntilDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 4),
    _MltIppJobHoldUntilDefault_Type()
)
mltIppJobHoldUntilDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobHoldUntilDefault.setStatus("optional")
_MltIppJobSheetsDefault_Type = Integer32
_MltIppJobSheetsDefault_Object = MibTableColumn
mltIppJobSheetsDefault = _MltIppJobSheetsDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 5),
    _MltIppJobSheetsDefault_Type()
)
mltIppJobSheetsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobSheetsDefault.setStatus("optional")
_MltIppCopiesDefault_Type = Integer32
_MltIppCopiesDefault_Object = MibTableColumn
mltIppCopiesDefault = _MltIppCopiesDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 6),
    _MltIppCopiesDefault_Type()
)
mltIppCopiesDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppCopiesDefault.setStatus("optional")
_MltIppCopiesMaxSupported_Type = Integer32
_MltIppCopiesMaxSupported_Object = MibTableColumn
mltIppCopiesMaxSupported = _MltIppCopiesMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 7),
    _MltIppCopiesMaxSupported_Type()
)
mltIppCopiesMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppCopiesMaxSupported.setStatus("optional")
_MltIppFinishingsDefault_Type = Integer32
_MltIppFinishingsDefault_Object = MibTableColumn
mltIppFinishingsDefault = _MltIppFinishingsDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 8),
    _MltIppFinishingsDefault_Type()
)
mltIppFinishingsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppFinishingsDefault.setStatus("optional")


class _MltIppPageRangesSupported_Type(Integer32):
    """Custom type mltIppPageRangesSupported based on Integer32"""
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


_MltIppPageRangesSupported_Type.__name__ = "Integer32"
_MltIppPageRangesSupported_Object = MibTableColumn
mltIppPageRangesSupported = _MltIppPageRangesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 9),
    _MltIppPageRangesSupported_Type()
)
mltIppPageRangesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppPageRangesSupported.setStatus("optional")
_MltIppSidesDefault_Type = Integer32
_MltIppSidesDefault_Object = MibTableColumn
mltIppSidesDefault = _MltIppSidesDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 10),
    _MltIppSidesDefault_Type()
)
mltIppSidesDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppSidesDefault.setStatus("optional")
_MltIppNumberUpDefault_Type = Integer32
_MltIppNumberUpDefault_Object = MibTableColumn
mltIppNumberUpDefault = _MltIppNumberUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 11),
    _MltIppNumberUpDefault_Type()
)
mltIppNumberUpDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNumberUpDefault.setStatus("optional")
_MltIppOrientationRequestedDefault_Type = Integer32
_MltIppOrientationRequestedDefault_Object = MibTableColumn
mltIppOrientationRequestedDefault = _MltIppOrientationRequestedDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 12),
    _MltIppOrientationRequestedDefault_Type()
)
mltIppOrientationRequestedDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppOrientationRequestedDefault.setStatus("optional")
_MltIppMediaDefault_Type = Integer32
_MltIppMediaDefault_Object = MibTableColumn
mltIppMediaDefault = _MltIppMediaDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 13),
    _MltIppMediaDefault_Type()
)
mltIppMediaDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppMediaDefault.setStatus("optional")
_MltIppPrinterResolutionDefault_Type = Integer32
_MltIppPrinterResolutionDefault_Object = MibTableColumn
mltIppPrinterResolutionDefault = _MltIppPrinterResolutionDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 14),
    _MltIppPrinterResolutionDefault_Type()
)
mltIppPrinterResolutionDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrinterResolutionDefault.setStatus("optional")
_MltIppPrintQualityDefault_Type = Integer32
_MltIppPrintQualityDefault_Object = MibTableColumn
mltIppPrintQualityDefault = _MltIppPrintQualityDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 1, 1, 15),
    _MltIppPrintQualityDefault_Type()
)
mltIppPrintQualityDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltIppPrintQualityDefault.setStatus("optional")
_MltIppJobHoldUntilSupportedTable_Object = MibTable
mltIppJobHoldUntilSupportedTable = _MltIppJobHoldUntilSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 2)
)
if mibBuilder.loadTexts:
    mltIppJobHoldUntilSupportedTable.setStatus("optional")
_MltIppJobHoldUntilSupportedEntry_Object = MibTableRow
mltIppJobHoldUntilSupportedEntry = _MltIppJobHoldUntilSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 2, 1)
)
mltIppJobHoldUntilSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppJobHoldUntilIfIndex"),
    (0, "MC2350-MIB", "mltIppJobHoldUntilIndex"),
)
if mibBuilder.loadTexts:
    mltIppJobHoldUntilSupportedEntry.setStatus("optional")
_MltIppJobHoldUntilIfIndex_Type = Integer32
_MltIppJobHoldUntilIfIndex_Object = MibTableColumn
mltIppJobHoldUntilIfIndex = _MltIppJobHoldUntilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 2, 1, 1),
    _MltIppJobHoldUntilIfIndex_Type()
)
mltIppJobHoldUntilIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobHoldUntilIfIndex.setStatus("optional")
_MltIppJobHoldUntilIndex_Type = Integer32
_MltIppJobHoldUntilIndex_Object = MibTableColumn
mltIppJobHoldUntilIndex = _MltIppJobHoldUntilIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 2, 1, 2),
    _MltIppJobHoldUntilIndex_Type()
)
mltIppJobHoldUntilIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobHoldUntilIndex.setStatus("optional")


class _MltIppJobHoldUntilType_Type(Integer32):
    """Custom type mltIppJobHoldUntilType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dayTime", 5),
          ("evening", 6),
          ("indefinite", 4),
          ("night", 7),
          ("noHold", 3),
          ("secondShift", 9),
          ("thirdShift", 10),
          ("weekend", 8))
    )


_MltIppJobHoldUntilType_Type.__name__ = "Integer32"
_MltIppJobHoldUntilType_Object = MibTableColumn
mltIppJobHoldUntilType = _MltIppJobHoldUntilType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 2, 1, 3),
    _MltIppJobHoldUntilType_Type()
)
mltIppJobHoldUntilType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobHoldUntilType.setStatus("optional")
_MltIppJobSheetsSupportedTable_Object = MibTable
mltIppJobSheetsSupportedTable = _MltIppJobSheetsSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 3)
)
if mibBuilder.loadTexts:
    mltIppJobSheetsSupportedTable.setStatus("optional")
_MltIppJobSheetsSupportedEntry_Object = MibTableRow
mltIppJobSheetsSupportedEntry = _MltIppJobSheetsSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 3, 1)
)
mltIppJobSheetsSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppJobSheetsIfIndex"),
    (0, "MC2350-MIB", "mltIppJobSheetsIndex"),
)
if mibBuilder.loadTexts:
    mltIppJobSheetsSupportedEntry.setStatus("optional")
_MltIppJobSheetsIfIndex_Type = Integer32
_MltIppJobSheetsIfIndex_Object = MibTableColumn
mltIppJobSheetsIfIndex = _MltIppJobSheetsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 3, 1, 1),
    _MltIppJobSheetsIfIndex_Type()
)
mltIppJobSheetsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobSheetsIfIndex.setStatus("optional")
_MltIppJobSheetsIndex_Type = Integer32
_MltIppJobSheetsIndex_Object = MibTableColumn
mltIppJobSheetsIndex = _MltIppJobSheetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 3, 1, 2),
    _MltIppJobSheetsIndex_Type()
)
mltIppJobSheetsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobSheetsIndex.setStatus("optional")


class _MltIppJobSheetsType_Type(Integer32):
    """Custom type mltIppJobSheetsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("standard", 4))
    )


_MltIppJobSheetsType_Type.__name__ = "Integer32"
_MltIppJobSheetsType_Object = MibTableColumn
mltIppJobSheetsType = _MltIppJobSheetsType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 3, 1, 3),
    _MltIppJobSheetsType_Type()
)
mltIppJobSheetsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppJobSheetsType.setStatus("optional")
_MltIppFinishingsSupportedTable_Object = MibTable
mltIppFinishingsSupportedTable = _MltIppFinishingsSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 4)
)
if mibBuilder.loadTexts:
    mltIppFinishingsSupportedTable.setStatus("optional")
_MltIppFinishingsSupportedEntry_Object = MibTableRow
mltIppFinishingsSupportedEntry = _MltIppFinishingsSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 4, 1)
)
mltIppFinishingsSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppFinishingsIfIndex"),
    (0, "MC2350-MIB", "mltIppFinishingsIndex"),
)
if mibBuilder.loadTexts:
    mltIppFinishingsSupportedEntry.setStatus("optional")
_MltIppFinishingsIfIndex_Type = Integer32
_MltIppFinishingsIfIndex_Object = MibTableColumn
mltIppFinishingsIfIndex = _MltIppFinishingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 4, 1, 1),
    _MltIppFinishingsIfIndex_Type()
)
mltIppFinishingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppFinishingsIfIndex.setStatus("optional")
_MltIppFinishingsIndex_Type = Integer32
_MltIppFinishingsIndex_Object = MibTableColumn
mltIppFinishingsIndex = _MltIppFinishingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 4, 1, 2),
    _MltIppFinishingsIndex_Type()
)
mltIppFinishingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppFinishingsIndex.setStatus("optional")


class _MltIppFinishingsType_Type(Integer32):
    """Custom type mltIppFinishingsType based on Integer32"""
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
        *(("bind", 7),
          ("cover", 6),
          ("edge-stitch", 9),
          ("edge-stitch-bottom", 27),
          ("edge-stitch-left", 24),
          ("edge-stitch-right", 26),
          ("edge-stitch-top", 25),
          ("none", 3),
          ("punch", 5),
          ("saddle-stitch", 8),
          ("staple", 4),
          ("staple-bottom-left", 21),
          ("staple-bottom-right", 23),
          ("staple-dual-bottom", 31),
          ("staple-dual-left", 28),
          ("staple-dual-right", 30),
          ("staple-dual-top", 29),
          ("staple-top-left", 20),
          ("staple-top-right", 22))
    )


_MltIppFinishingsType_Type.__name__ = "Integer32"
_MltIppFinishingsType_Object = MibTableColumn
mltIppFinishingsType = _MltIppFinishingsType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 4, 1, 3),
    _MltIppFinishingsType_Type()
)
mltIppFinishingsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppFinishingsType.setStatus("optional")
_MltIppSidesSupportedTable_Object = MibTable
mltIppSidesSupportedTable = _MltIppSidesSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 5)
)
if mibBuilder.loadTexts:
    mltIppSidesSupportedTable.setStatus("optional")
_MltIppSidesSupportedEntry_Object = MibTableRow
mltIppSidesSupportedEntry = _MltIppSidesSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 5, 1)
)
mltIppSidesSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppSidesIfIndex"),
    (0, "MC2350-MIB", "mltIppSidesIndex"),
)
if mibBuilder.loadTexts:
    mltIppSidesSupportedEntry.setStatus("optional")
_MltIppSidesIfIndex_Type = Integer32
_MltIppSidesIfIndex_Object = MibTableColumn
mltIppSidesIfIndex = _MltIppSidesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 5, 1, 1),
    _MltIppSidesIfIndex_Type()
)
mltIppSidesIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppSidesIfIndex.setStatus("optional")
_MltIppSidesIndex_Type = Integer32
_MltIppSidesIndex_Object = MibTableColumn
mltIppSidesIndex = _MltIppSidesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 5, 1, 2),
    _MltIppSidesIndex_Type()
)
mltIppSidesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppSidesIndex.setStatus("optional")


class _MltIppSidesType_Type(Integer32):
    """Custom type mltIppSidesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("one-sided", 3),
          ("two-sided-long-edge", 4),
          ("two-sided-short-edge", 5))
    )


_MltIppSidesType_Type.__name__ = "Integer32"
_MltIppSidesType_Object = MibTableColumn
mltIppSidesType = _MltIppSidesType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 5, 1, 3),
    _MltIppSidesType_Type()
)
mltIppSidesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppSidesType.setStatus("optional")
_MltIppNumberUpSupportedTable_Object = MibTable
mltIppNumberUpSupportedTable = _MltIppNumberUpSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 6)
)
if mibBuilder.loadTexts:
    mltIppNumberUpSupportedTable.setStatus("optional")
_MltIppNumberUpSupportedEntry_Object = MibTableRow
mltIppNumberUpSupportedEntry = _MltIppNumberUpSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 6, 1)
)
mltIppNumberUpSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppNumberUpIfIndex"),
    (0, "MC2350-MIB", "mltIppNumberUpIndex"),
)
if mibBuilder.loadTexts:
    mltIppNumberUpSupportedEntry.setStatus("optional")
_MltIppNumberUpIfIndex_Type = Integer32
_MltIppNumberUpIfIndex_Object = MibTableColumn
mltIppNumberUpIfIndex = _MltIppNumberUpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 6, 1, 1),
    _MltIppNumberUpIfIndex_Type()
)
mltIppNumberUpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNumberUpIfIndex.setStatus("optional")
_MltIppNumberUpIndex_Type = Integer32
_MltIppNumberUpIndex_Object = MibTableColumn
mltIppNumberUpIndex = _MltIppNumberUpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 6, 1, 2),
    _MltIppNumberUpIndex_Type()
)
mltIppNumberUpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNumberUpIndex.setStatus("optional")


class _MltIppNumberUpType_Type(Integer32):
    """Custom type mltIppNumberUpType based on Integer32"""
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
        *(("num16Up", 5),
          ("num1Up", 1),
          ("num2Up", 2),
          ("num4Up", 3),
          ("num9Up", 4))
    )


_MltIppNumberUpType_Type.__name__ = "Integer32"
_MltIppNumberUpType_Object = MibTableColumn
mltIppNumberUpType = _MltIppNumberUpType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 6, 1, 3),
    _MltIppNumberUpType_Type()
)
mltIppNumberUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppNumberUpType.setStatus("optional")
_MltIppOrientationRequestedSupportedTable_Object = MibTable
mltIppOrientationRequestedSupportedTable = _MltIppOrientationRequestedSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 7)
)
if mibBuilder.loadTexts:
    mltIppOrientationRequestedSupportedTable.setStatus("optional")
_MltIppOrientationRequestedSupportedEntry_Object = MibTableRow
mltIppOrientationRequestedSupportedEntry = _MltIppOrientationRequestedSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 7, 1)
)
mltIppOrientationRequestedSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppOrientationRequestedIfIndex"),
    (0, "MC2350-MIB", "mltIppOrientationRequestedIndex"),
)
if mibBuilder.loadTexts:
    mltIppOrientationRequestedSupportedEntry.setStatus("optional")
_MltIppOrientationRequestedIfIndex_Type = Integer32
_MltIppOrientationRequestedIfIndex_Object = MibTableColumn
mltIppOrientationRequestedIfIndex = _MltIppOrientationRequestedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 7, 1, 1),
    _MltIppOrientationRequestedIfIndex_Type()
)
mltIppOrientationRequestedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOrientationRequestedIfIndex.setStatus("optional")
_MltIppOrientationRequestedIndex_Type = Integer32
_MltIppOrientationRequestedIndex_Object = MibTableColumn
mltIppOrientationRequestedIndex = _MltIppOrientationRequestedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 7, 1, 2),
    _MltIppOrientationRequestedIndex_Type()
)
mltIppOrientationRequestedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOrientationRequestedIndex.setStatus("optional")


class _MltIppOrientationRequestedType_Type(Integer32):
    """Custom type mltIppOrientationRequestedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 4),
          ("portrait", 3),
          ("reverse-landscape", 5),
          ("reverse-portrait", 6))
    )


_MltIppOrientationRequestedType_Type.__name__ = "Integer32"
_MltIppOrientationRequestedType_Object = MibTableColumn
mltIppOrientationRequestedType = _MltIppOrientationRequestedType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 7, 1, 3),
    _MltIppOrientationRequestedType_Type()
)
mltIppOrientationRequestedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppOrientationRequestedType.setStatus("optional")
_MltIppMediaSupportedTable_Object = MibTable
mltIppMediaSupportedTable = _MltIppMediaSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8)
)
if mibBuilder.loadTexts:
    mltIppMediaSupportedTable.setStatus("optional")
_MltIppMediaSupportedEntry_Object = MibTableRow
mltIppMediaSupportedEntry = _MltIppMediaSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1)
)
mltIppMediaSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltIppMediaIfIndex"),
    (0, "MC2350-MIB", "mltIppMediaIndex"),
)
if mibBuilder.loadTexts:
    mltIppMediaSupportedEntry.setStatus("optional")
_MltIppMediaIfIndex_Type = Integer32
_MltIppMediaIfIndex_Object = MibTableColumn
mltIppMediaIfIndex = _MltIppMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 1),
    _MltIppMediaIfIndex_Type()
)
mltIppMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaIfIndex.setStatus("optional")
_MltIppMediaIndex_Type = Integer32
_MltIppMediaIndex_Object = MibTableColumn
mltIppMediaIndex = _MltIppMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 2),
    _MltIppMediaIndex_Type()
)
mltIppMediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaIndex.setStatus("optional")


class _MltIppMediaName_Type(OctetString):
    """Custom type mltIppMediaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltIppMediaName_Type.__name__ = "OctetString"
_MltIppMediaName_Object = MibTableColumn
mltIppMediaName = _MltIppMediaName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 3),
    _MltIppMediaName_Type()
)
mltIppMediaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaName.setStatus("optional")


class _MltIppMediaType_Type(OctetString):
    """Custom type mltIppMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltIppMediaType_Type.__name__ = "OctetString"
_MltIppMediaType_Object = MibTableColumn
mltIppMediaType = _MltIppMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 4),
    _MltIppMediaType_Type()
)
mltIppMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaType.setStatus("optional")


class _MltIppMediaColor_Type(OctetString):
    """Custom type mltIppMediaColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltIppMediaColor_Type.__name__ = "OctetString"
_MltIppMediaColor_Object = MibTableColumn
mltIppMediaColor = _MltIppMediaColor_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 5),
    _MltIppMediaColor_Type()
)
mltIppMediaColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaColor.setStatus("optional")


class _MltIppMediaInputTray_Type(OctetString):
    """Custom type mltIppMediaInputTray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltIppMediaInputTray_Type.__name__ = "OctetString"
_MltIppMediaInputTray_Object = MibTableColumn
mltIppMediaInputTray = _MltIppMediaInputTray_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 8, 1, 6),
    _MltIppMediaInputTray_Type()
)
mltIppMediaInputTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltIppMediaInputTray.setStatus("optional")
_MltPrinterResolutionSupportedTable_Object = MibTable
mltPrinterResolutionSupportedTable = _MltPrinterResolutionSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9)
)
if mibBuilder.loadTexts:
    mltPrinterResolutionSupportedTable.setStatus("optional")
_MltPrinterResolutionSupportedEntry_Object = MibTableRow
mltPrinterResolutionSupportedEntry = _MltPrinterResolutionSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1)
)
mltPrinterResolutionSupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltPrinterResolutionIfIndex"),
    (0, "MC2350-MIB", "mltPrinterResolutionIndex"),
)
if mibBuilder.loadTexts:
    mltPrinterResolutionSupportedEntry.setStatus("optional")
_MltPrinterResolutionIfIndex_Type = Integer32
_MltPrinterResolutionIfIndex_Object = MibTableColumn
mltPrinterResolutionIfIndex = _MltPrinterResolutionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1, 1),
    _MltPrinterResolutionIfIndex_Type()
)
mltPrinterResolutionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrinterResolutionIfIndex.setStatus("optional")
_MltPrinterResolutionIndex_Type = Integer32
_MltPrinterResolutionIndex_Object = MibTableColumn
mltPrinterResolutionIndex = _MltPrinterResolutionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1, 2),
    _MltPrinterResolutionIndex_Type()
)
mltPrinterResolutionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrinterResolutionIndex.setStatus("optional")
_MltPrinterResolutionFeedDir_Type = Integer32
_MltPrinterResolutionFeedDir_Object = MibTableColumn
mltPrinterResolutionFeedDir = _MltPrinterResolutionFeedDir_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1, 3),
    _MltPrinterResolutionFeedDir_Type()
)
mltPrinterResolutionFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrinterResolutionFeedDir.setStatus("optional")
_MltPrinterResolutionXFeedDir_Type = Integer32
_MltPrinterResolutionXFeedDir_Object = MibTableColumn
mltPrinterResolutionXFeedDir = _MltPrinterResolutionXFeedDir_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1, 4),
    _MltPrinterResolutionXFeedDir_Type()
)
mltPrinterResolutionXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrinterResolutionXFeedDir.setStatus("optional")


class _MltPrinterResolutionUnit_Type(Integer32):
    """Custom type mltPrinterResolutionUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("micrometers", 4),
          ("other", 1),
          ("tenThousandthsOfInches", 3))
    )


_MltPrinterResolutionUnit_Type.__name__ = "Integer32"
_MltPrinterResolutionUnit_Object = MibTableColumn
mltPrinterResolutionUnit = _MltPrinterResolutionUnit_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 9, 1, 5),
    _MltPrinterResolutionUnit_Type()
)
mltPrinterResolutionUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrinterResolutionUnit.setStatus("optional")
_MltPrintQualitySupportedTable_Object = MibTable
mltPrintQualitySupportedTable = _MltPrintQualitySupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 10)
)
if mibBuilder.loadTexts:
    mltPrintQualitySupportedTable.setStatus("optional")
_MltPrintQualitySupportedEntry_Object = MibTableRow
mltPrintQualitySupportedEntry = _MltPrintQualitySupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 10, 1)
)
mltPrintQualitySupportedEntry.setIndexNames(
    (0, "MC2350-MIB", "mltPrintQualityIfIndex"),
    (0, "MC2350-MIB", "mltPrintQualityIndex"),
)
if mibBuilder.loadTexts:
    mltPrintQualitySupportedEntry.setStatus("optional")
_MltPrintQualityIfIndex_Type = Integer32
_MltPrintQualityIfIndex_Object = MibTableColumn
mltPrintQualityIfIndex = _MltPrintQualityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 10, 1, 1),
    _MltPrintQualityIfIndex_Type()
)
mltPrintQualityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrintQualityIfIndex.setStatus("optional")
_MltPrintQualityIndex_Type = Integer32
_MltPrintQualityIndex_Object = MibTableColumn
mltPrintQualityIndex = _MltPrintQualityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 10, 1, 2),
    _MltPrintQualityIndex_Type()
)
mltPrintQualityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrintQualityIndex.setStatus("optional")


class _MltPrintQualityType_Type(Integer32):
    """Custom type mltPrintQualityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("draft", 3),
          ("high", 5),
          ("normal", 4))
    )


_MltPrintQualityType_Type.__name__ = "Integer32"
_MltPrintQualityType_Object = MibTableColumn
mltPrintQualityType = _MltPrintQualityType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 14, 3, 10, 1, 3),
    _MltPrintQualityType_Type()
)
mltPrintQualityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltPrintQualityType.setStatus("optional")
_MltNetSlp_ObjectIdentity = ObjectIdentity
mltNetSlp = _MltNetSlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17)
)
_MltNetSlpGeneralTable_Object = MibTable
mltNetSlpGeneralTable = _MltNetSlpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1)
)
if mibBuilder.loadTexts:
    mltNetSlpGeneralTable.setStatus("mandatory")
_MltNetSlpGeneralEntry_Object = MibTableRow
mltNetSlpGeneralEntry = _MltNetSlpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1)
)
mltNetSlpGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSlpIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetSlpGeneralEntry.setStatus("mandatory")
_MltNetSlpIfIndex_Type = Integer32
_MltNetSlpIfIndex_Object = MibTableColumn
mltNetSlpIfIndex = _MltNetSlpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 1),
    _MltNetSlpIfIndex_Type()
)
mltNetSlpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSlpIfIndex.setStatus("mandatory")


class _MltNetSlpEnable_Type(Integer32):
    """Custom type mltNetSlpEnable based on Integer32"""
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


_MltNetSlpEnable_Type.__name__ = "Integer32"
_MltNetSlpEnable_Object = MibTableColumn
mltNetSlpEnable = _MltNetSlpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 2),
    _MltNetSlpEnable_Type()
)
mltNetSlpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpEnable.setStatus("mandatory")
_MltNetSlpPortNumber_Type = Integer32
_MltNetSlpPortNumber_Object = MibTableColumn
mltNetSlpPortNumber = _MltNetSlpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 3),
    _MltNetSlpPortNumber_Type()
)
mltNetSlpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpPortNumber.setStatus("mandatory")
_MltNetSlpMTU_Type = Integer32
_MltNetSlpMTU_Object = MibTableColumn
mltNetSlpMTU = _MltNetSlpMTU_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 4),
    _MltNetSlpMTU_Type()
)
mltNetSlpMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpMTU.setStatus("mandatory")
_MltNetSlpTTL_Type = Integer32
_MltNetSlpTTL_Object = MibTableColumn
mltNetSlpTTL = _MltNetSlpTTL_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 5),
    _MltNetSlpTTL_Type()
)
mltNetSlpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpTTL.setStatus("mandatory")


class _MltNetSlpBroadcastSupport_Type(Integer32):
    """Custom type mltNetSlpBroadcastSupport based on Integer32"""
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
          ("broadcastOnly", 1),
          ("multicastOnly", 2))
    )


_MltNetSlpBroadcastSupport_Type.__name__ = "Integer32"
_MltNetSlpBroadcastSupport_Object = MibTableColumn
mltNetSlpBroadcastSupport = _MltNetSlpBroadcastSupport_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 1, 1, 6),
    _MltNetSlpBroadcastSupport_Type()
)
mltNetSlpBroadcastSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpBroadcastSupport.setStatus("mandatory")
_MltNetSlpConfigTable_Object = MibTable
mltNetSlpConfigTable = _MltNetSlpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2)
)
if mibBuilder.loadTexts:
    mltNetSlpConfigTable.setStatus("mandatory")
_MltNetSlpConfigEntry_Object = MibTableRow
mltNetSlpConfigEntry = _MltNetSlpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1)
)
mltNetSlpConfigEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSlpConfigIfIndex"),
    (0, "MC2350-MIB", "mltNetSlpIndex"),
)
if mibBuilder.loadTexts:
    mltNetSlpConfigEntry.setStatus("mandatory")
_MltNetSlpConfigIfIndex_Type = Integer32
_MltNetSlpConfigIfIndex_Object = MibTableColumn
mltNetSlpConfigIfIndex = _MltNetSlpConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1, 1),
    _MltNetSlpConfigIfIndex_Type()
)
mltNetSlpConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSlpConfigIfIndex.setStatus("mandatory")
_MltNetSlpIndex_Type = Integer32
_MltNetSlpIndex_Object = MibTableColumn
mltNetSlpIndex = _MltNetSlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1, 2),
    _MltNetSlpIndex_Type()
)
mltNetSlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSlpIndex.setStatus("mandatory")


class _MltNetSlpService_Type(DisplayString):
    """Custom type mltNetSlpService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSlpService_Type.__name__ = "DisplayString"
_MltNetSlpService_Object = MibTableColumn
mltNetSlpService = _MltNetSlpService_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1, 3),
    _MltNetSlpService_Type()
)
mltNetSlpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSlpService.setStatus("mandatory")


class _MltNetSlpScope_Type(DisplayString):
    """Custom type mltNetSlpScope based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSlpScope_Type.__name__ = "DisplayString"
_MltNetSlpScope_Object = MibTableColumn
mltNetSlpScope = _MltNetSlpScope_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1, 4),
    _MltNetSlpScope_Type()
)
mltNetSlpScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpScope.setStatus("mandatory")
_MltNetSlpLifetime_Type = Integer32
_MltNetSlpLifetime_Object = MibTableColumn
mltNetSlpLifetime = _MltNetSlpLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 7, 17, 2, 1, 5),
    _MltNetSlpLifetime_Type()
)
mltNetSlpLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSlpLifetime.setStatus("mandatory")
_MltNetNetWare_ObjectIdentity = ObjectIdentity
mltNetNetWare = _MltNetNetWare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8)
)
_MltNetNwGeneralTable_Object = MibTable
mltNetNwGeneralTable = _MltNetNwGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mltNetNwGeneralTable.setStatus("mandatory")
_MltNetNwGeneralEntry_Object = MibTableRow
mltNetNwGeneralEntry = _MltNetNwGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1, 1)
)
mltNetNwGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetNwIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetNwGeneralEntry.setStatus("mandatory")
_MltNetNwIfIndex_Type = Integer32
_MltNetNwIfIndex_Object = MibTableColumn
mltNetNwIfIndex = _MltNetNwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1, 1, 1),
    _MltNetNwIfIndex_Type()
)
mltNetNwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwIfIndex.setStatus("mandatory")


class _MltNetNwDefault_Type(Integer32):
    """Custom type mltNetNwDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("resetToDefault", 2),
          ("supported", 1))
    )


_MltNetNwDefault_Type.__name__ = "Integer32"
_MltNetNwDefault_Object = MibTableColumn
mltNetNwDefault = _MltNetNwDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1, 1, 2),
    _MltNetNwDefault_Type()
)
mltNetNwDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwDefault.setStatus("mandatory")
_MltNetNwFrameTypeConfig_Type = Integer32
_MltNetNwFrameTypeConfig_Object = MibTableColumn
mltNetNwFrameTypeConfig = _MltNetNwFrameTypeConfig_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1, 1, 3),
    _MltNetNwFrameTypeConfig_Type()
)
mltNetNwFrameTypeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwFrameTypeConfig.setStatus("mandatory")


class _MltNetNwPrintMode_Type(Integer32):
    """Custom type mltNetNwPrintMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nPrinterMode", 2),
          ("pServerMode", 1))
    )


_MltNetNwPrintMode_Type.__name__ = "Integer32"
_MltNetNwPrintMode_Object = MibTableColumn
mltNetNwPrintMode = _MltNetNwPrintMode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 1, 1, 4),
    _MltNetNwPrintMode_Type()
)
mltNetNwPrintMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPrintMode.setStatus("mandatory")
_MltNetNwFrameTable_Object = MibTable
mltNetNwFrameTable = _MltNetNwFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2)
)
if mibBuilder.loadTexts:
    mltNetNwFrameTable.setStatus("optional")
_MltNetNwFrameEntry_Object = MibTableRow
mltNetNwFrameEntry = _MltNetNwFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2, 1)
)
mltNetNwFrameEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetNwFrameIfIndex"),
    (0, "MC2350-MIB", "mltNetNwFrameIndex"),
)
if mibBuilder.loadTexts:
    mltNetNwFrameEntry.setStatus("optional")
_MltNetNwFrameIfIndex_Type = Integer32
_MltNetNwFrameIfIndex_Object = MibTableColumn
mltNetNwFrameIfIndex = _MltNetNwFrameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2, 1, 1),
    _MltNetNwFrameIfIndex_Type()
)
mltNetNwFrameIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwFrameIfIndex.setStatus("optional")
_MltNetNwFrameIndex_Type = Integer32
_MltNetNwFrameIndex_Object = MibTableColumn
mltNetNwFrameIndex = _MltNetNwFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2, 1, 2),
    _MltNetNwFrameIndex_Type()
)
mltNetNwFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwFrameIndex.setStatus("optional")


class _MltNetNwFrameType_Type(Integer32):
    """Custom type mltNetNwFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ethernet8022", 4),
          ("ethernet8023", 1),
          ("ethernetII", 2),
          ("ethernetSnap", 3),
          ("tokenRing8025", 6),
          ("tokenRingSnap", 7))
    )


_MltNetNwFrameType_Type.__name__ = "Integer32"
_MltNetNwFrameType_Object = MibTableColumn
mltNetNwFrameType = _MltNetNwFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2, 1, 3),
    _MltNetNwFrameType_Type()
)
mltNetNwFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwFrameType.setStatus("optional")


class _MltNetNwNetworkNumber_Type(OctetString):
    """Custom type mltNetNwNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MltNetNwNetworkNumber_Type.__name__ = "OctetString"
_MltNetNwNetworkNumber_Object = MibTableColumn
mltNetNwNetworkNumber = _MltNetNwNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 2, 1, 4),
    _MltNetNwNetworkNumber_Type()
)
mltNetNwNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwNetworkNumber.setStatus("optional")
_MltNetNwPserverTable_Object = MibTable
mltNetNwPserverTable = _MltNetNwPserverTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3)
)
if mibBuilder.loadTexts:
    mltNetNwPserverTable.setStatus("mandatory")
_MltNetNwPserverEntry_Object = MibTableRow
mltNetNwPserverEntry = _MltNetNwPserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1)
)
mltNetNwPserverEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetNwPsIfIndex"),
    (0, "MC2350-MIB", "mltNetNwPsIndex"),
)
if mibBuilder.loadTexts:
    mltNetNwPserverEntry.setStatus("mandatory")
_MltNetNwPsIfIndex_Type = Integer32
_MltNetNwPsIfIndex_Object = MibTableColumn
mltNetNwPsIfIndex = _MltNetNwPsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 1),
    _MltNetNwPsIfIndex_Type()
)
mltNetNwPsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwPsIfIndex.setStatus("mandatory")
_MltNetNwPsIndex_Type = Integer32
_MltNetNwPsIndex_Object = MibTableColumn
mltNetNwPsIndex = _MltNetNwPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 2),
    _MltNetNwPsIndex_Type()
)
mltNetNwPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwPsIndex.setStatus("mandatory")


class _MltNetNwPsName_Type(DisplayString):
    """Custom type mltNetNwPsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetNwPsName_Type.__name__ = "DisplayString"
_MltNetNwPsName_Object = MibTableColumn
mltNetNwPsName = _MltNetNwPsName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 3),
    _MltNetNwPsName_Type()
)
mltNetNwPsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsName.setStatus("mandatory")


class _MltNetNwPsPasswd_Type(DisplayString):
    """Custom type mltNetNwPsPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetNwPsPasswd_Type.__name__ = "DisplayString"
_MltNetNwPsPasswd_Object = MibTableColumn
mltNetNwPsPasswd = _MltNetNwPsPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 4),
    _MltNetNwPsPasswd_Type()
)
mltNetNwPsPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsPasswd.setStatus("mandatory")


class _MltNetNwPsMode_Type(Integer32):
    """Custom type mltNetNwPsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("binderyMode", 1),
          ("both", 0),
          ("ndsMode", 2))
    )


_MltNetNwPsMode_Type.__name__ = "Integer32"
_MltNetNwPsMode_Object = MibTableColumn
mltNetNwPsMode = _MltNetNwPsMode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 5),
    _MltNetNwPsMode_Type()
)
mltNetNwPsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsMode.setStatus("mandatory")


class _MltNetNwPsPrefFServer_Type(DisplayString):
    """Custom type mltNetNwPsPrefFServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_MltNetNwPsPrefFServer_Type.__name__ = "DisplayString"
_MltNetNwPsPrefFServer_Object = MibTableColumn
mltNetNwPsPrefFServer = _MltNetNwPsPrefFServer_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 6),
    _MltNetNwPsPrefFServer_Type()
)
mltNetNwPsPrefFServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsPrefFServer.setStatus("mandatory")


class _MltNetNwPsPrefTree_Type(DisplayString):
    """Custom type mltNetNwPsPrefTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetNwPsPrefTree_Type.__name__ = "DisplayString"
_MltNetNwPsPrefTree_Object = MibTableColumn
mltNetNwPsPrefTree = _MltNetNwPsPrefTree_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 7),
    _MltNetNwPsPrefTree_Type()
)
mltNetNwPsPrefTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsPrefTree.setStatus("mandatory")


class _MltNetNwPsPrefContext_Type(DisplayString):
    """Custom type mltNetNwPsPrefContext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 191),
    )


_MltNetNwPsPrefContext_Type.__name__ = "DisplayString"
_MltNetNwPsPrefContext_Object = MibTableColumn
mltNetNwPsPrefContext = _MltNetNwPsPrefContext_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 8),
    _MltNetNwPsPrefContext_Type()
)
mltNetNwPsPrefContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsPrefContext.setStatus("mandatory")
_MltNetNwPsPollingRate_Type = Integer32
_MltNetNwPsPollingRate_Object = MibTableColumn
mltNetNwPsPollingRate = _MltNetNwPsPollingRate_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 3, 1, 9),
    _MltNetNwPsPollingRate_Type()
)
mltNetNwPsPollingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwPsPollingRate.setStatus("mandatory")
_MltNetNwQueueTable_Object = MibTable
mltNetNwQueueTable = _MltNetNwQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4)
)
if mibBuilder.loadTexts:
    mltNetNwQueueTable.setStatus("mandatory")
_MltNetNwQueueEntry_Object = MibTableRow
mltNetNwQueueEntry = _MltNetNwQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1)
)
mltNetNwQueueEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetNwQueueIndex"),
)
if mibBuilder.loadTexts:
    mltNetNwQueueEntry.setStatus("mandatory")
_MltNetNwQueueIndex_Type = Integer32
_MltNetNwQueueIndex_Object = MibTableColumn
mltNetNwQueueIndex = _MltNetNwQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1, 1),
    _MltNetNwQueueIndex_Type()
)
mltNetNwQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwQueueIndex.setStatus("mandatory")


class _MltNetNwQueueName_Type(DisplayString):
    """Custom type mltNetNwQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetNwQueueName_Type.__name__ = "DisplayString"
_MltNetNwQueueName_Object = MibTableColumn
mltNetNwQueueName = _MltNetNwQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1, 2),
    _MltNetNwQueueName_Type()
)
mltNetNwQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwQueueName.setStatus("mandatory")
_MltNetNwQueueRefIfIndex_Type = Integer32
_MltNetNwQueueRefIfIndex_Object = MibTableColumn
mltNetNwQueueRefIfIndex = _MltNetNwQueueRefIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1, 3),
    _MltNetNwQueueRefIfIndex_Type()
)
mltNetNwQueueRefIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwQueueRefIfIndex.setStatus("mandatory")
_MltNetNwQueueRefPsIndex_Type = Integer32
_MltNetNwQueueRefPsIndex_Object = MibTableColumn
mltNetNwQueueRefPsIndex = _MltNetNwQueueRefPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1, 4),
    _MltNetNwQueueRefPsIndex_Type()
)
mltNetNwQueueRefPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwQueueRefPsIndex.setStatus("mandatory")


class _MltNetNwQueueStatus_Type(Integer32):
    """Custom type mltNetNwQueueStatus based on Integer32"""
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
        *(("allocated", 2),
          ("available", 1),
          ("inUse", 3),
          ("unknown", 0))
    )


_MltNetNwQueueStatus_Type.__name__ = "Integer32"
_MltNetNwQueueStatus_Object = MibTableColumn
mltNetNwQueueStatus = _MltNetNwQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 4, 1, 5),
    _MltNetNwQueueStatus_Type()
)
mltNetNwQueueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwQueueStatus.setStatus("mandatory")
_MltNetNwNPrinterTable_Object = MibTable
mltNetNwNPrinterTable = _MltNetNwNPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5)
)
if mibBuilder.loadTexts:
    mltNetNwNPrinterTable.setStatus("mandatory")
_MltNetNwNPrinterEntry_Object = MibTableRow
mltNetNwNPrinterEntry = _MltNetNwNPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5, 1)
)
mltNetNwNPrinterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetNwNPrinterIfIndex"),
    (0, "MC2350-MIB", "mltNetNwNPrinterIndex"),
)
if mibBuilder.loadTexts:
    mltNetNwNPrinterEntry.setStatus("mandatory")
_MltNetNwNPrinterIfIndex_Type = Integer32
_MltNetNwNPrinterIfIndex_Object = MibTableColumn
mltNetNwNPrinterIfIndex = _MltNetNwNPrinterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5, 1, 1),
    _MltNetNwNPrinterIfIndex_Type()
)
mltNetNwNPrinterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwNPrinterIfIndex.setStatus("mandatory")
_MltNetNwNPrinterIndex_Type = Integer32
_MltNetNwNPrinterIndex_Object = MibTableColumn
mltNetNwNPrinterIndex = _MltNetNwNPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5, 1, 2),
    _MltNetNwNPrinterIndex_Type()
)
mltNetNwNPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetNwNPrinterIndex.setStatus("mandatory")


class _MltNetNwNPrinterName_Type(DisplayString):
    """Custom type mltNetNwNPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltNetNwNPrinterName_Type.__name__ = "DisplayString"
_MltNetNwNPrinterName_Object = MibTableColumn
mltNetNwNPrinterName = _MltNetNwNPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5, 1, 3),
    _MltNetNwNPrinterName_Type()
)
mltNetNwNPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwNPrinterName.setStatus("mandatory")
_MltNetNwNPrinterNumber_Type = Integer32
_MltNetNwNPrinterNumber_Object = MibTableColumn
mltNetNwNPrinterNumber = _MltNetNwNPrinterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 8, 5, 1, 4),
    _MltNetNwNPrinterNumber_Type()
)
mltNetNwNPrinterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetNwNPrinterNumber.setStatus("mandatory")
_MltNetAppleTalk_ObjectIdentity = ObjectIdentity
mltNetAppleTalk = _MltNetAppleTalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9)
)
_MltNetAppleTalkGeneralTable_Object = MibTable
mltNetAppleTalkGeneralTable = _MltNetAppleTalkGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mltNetAppleTalkGeneralTable.setStatus("mandatory")
_MltNetAppleTalkGeneralEntry_Object = MibTableRow
mltNetAppleTalkGeneralEntry = _MltNetAppleTalkGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1)
)
mltNetAppleTalkGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetAtIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetAppleTalkGeneralEntry.setStatus("mandatory")
_MltNetAtIfIndex_Type = Integer32
_MltNetAtIfIndex_Object = MibTableColumn
mltNetAtIfIndex = _MltNetAtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 1),
    _MltNetAtIfIndex_Type()
)
mltNetAtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtIfIndex.setStatus("mandatory")


class _MltNetAtDefault_Type(Integer32):
    """Custom type mltNetAtDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("resetToDefault", 2),
          ("supported", 1))
    )


_MltNetAtDefault_Type.__name__ = "Integer32"
_MltNetAtDefault_Object = MibTableColumn
mltNetAtDefault = _MltNetAtDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 2),
    _MltNetAtDefault_Type()
)
mltNetAtDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetAtDefault.setStatus("mandatory")
_MltNetAtNetNumber_Type = Integer32
_MltNetAtNetNumber_Object = MibTableColumn
mltNetAtNetNumber = _MltNetAtNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 3),
    _MltNetAtNetNumber_Type()
)
mltNetAtNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtNetNumber.setStatus("mandatory")
_MltNetAtNodeNumber_Type = Integer32
_MltNetAtNodeNumber_Object = MibTableColumn
mltNetAtNodeNumber = _MltNetAtNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 4),
    _MltNetAtNodeNumber_Type()
)
mltNetAtNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtNodeNumber.setStatus("mandatory")


class _MltNetAtDesiredZone_Type(DisplayString):
    """Custom type mltNetAtDesiredZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetAtDesiredZone_Type.__name__ = "DisplayString"
_MltNetAtDesiredZone_Object = MibTableColumn
mltNetAtDesiredZone = _MltNetAtDesiredZone_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 5),
    _MltNetAtDesiredZone_Type()
)
mltNetAtDesiredZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetAtDesiredZone.setStatus("mandatory")


class _MltNetAtCurrentZone_Type(DisplayString):
    """Custom type mltNetAtCurrentZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetAtCurrentZone_Type.__name__ = "DisplayString"
_MltNetAtCurrentZone_Object = MibTableColumn
mltNetAtCurrentZone = _MltNetAtCurrentZone_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 1, 1, 6),
    _MltNetAtCurrentZone_Type()
)
mltNetAtCurrentZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtCurrentZone.setStatus("mandatory")
_MltNetAtPrinterTable_Object = MibTable
mltNetAtPrinterTable = _MltNetAtPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2)
)
if mibBuilder.loadTexts:
    mltNetAtPrinterTable.setStatus("mandatory")
_MltNetAtPrinterEntry_Object = MibTableRow
mltNetAtPrinterEntry = _MltNetAtPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2, 1)
)
mltNetAtPrinterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetAtPrinterIfIndex"),
    (0, "MC2350-MIB", "mltNetAtPrinterIndex"),
)
if mibBuilder.loadTexts:
    mltNetAtPrinterEntry.setStatus("mandatory")
_MltNetAtPrinterIfIndex_Type = Integer32
_MltNetAtPrinterIfIndex_Object = MibTableColumn
mltNetAtPrinterIfIndex = _MltNetAtPrinterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2, 1, 1),
    _MltNetAtPrinterIfIndex_Type()
)
mltNetAtPrinterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtPrinterIfIndex.setStatus("mandatory")
_MltNetAtPrinterIndex_Type = Integer32
_MltNetAtPrinterIndex_Object = MibTableColumn
mltNetAtPrinterIndex = _MltNetAtPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2, 1, 2),
    _MltNetAtPrinterIndex_Type()
)
mltNetAtPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtPrinterIndex.setStatus("mandatory")


class _MltNetAtPrinterName_Type(DisplayString):
    """Custom type mltNetAtPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MltNetAtPrinterName_Type.__name__ = "DisplayString"
_MltNetAtPrinterName_Object = MibTableColumn
mltNetAtPrinterName = _MltNetAtPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2, 1, 3),
    _MltNetAtPrinterName_Type()
)
mltNetAtPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetAtPrinterName.setStatus("mandatory")


class _MltNetAtPrinterType_Type(DisplayString):
    """Custom type mltNetAtPrinterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetAtPrinterType_Type.__name__ = "DisplayString"
_MltNetAtPrinterType_Object = MibTableColumn
mltNetAtPrinterType = _MltNetAtPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 9, 2, 1, 4),
    _MltNetAtPrinterType_Type()
)
mltNetAtPrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetAtPrinterType.setStatus("mandatory")
_MltNetSmb_ObjectIdentity = ObjectIdentity
mltNetSmb = _MltNetSmb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10)
)
_MltNetSmbGeneralTable_Object = MibTable
mltNetSmbGeneralTable = _MltNetSmbGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mltNetSmbGeneralTable.setStatus("mandatory")
_MltNetSmbGeneralEntry_Object = MibTableRow
mltNetSmbGeneralEntry = _MltNetSmbGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1)
)
mltNetSmbGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSmbIfIndex"),
)
if mibBuilder.loadTexts:
    mltNetSmbGeneralEntry.setStatus("mandatory")
_MltNetSmbIfIndex_Type = Integer32
_MltNetSmbIfIndex_Object = MibTableColumn
mltNetSmbIfIndex = _MltNetSmbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 1),
    _MltNetSmbIfIndex_Type()
)
mltNetSmbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbIfIndex.setStatus("mandatory")


class _MltNetSmbDefault_Type(Integer32):
    """Custom type mltNetSmbDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("resetToDefault", 2),
          ("supported", 1))
    )


_MltNetSmbDefault_Type.__name__ = "Integer32"
_MltNetSmbDefault_Object = MibTableColumn
mltNetSmbDefault = _MltNetSmbDefault_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 2),
    _MltNetSmbDefault_Type()
)
mltNetSmbDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmbDefault.setStatus("mandatory")


class _MltNetSmbWorkGroupName_Type(DisplayString):
    """Custom type mltNetSmbWorkGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSmbWorkGroupName_Type.__name__ = "DisplayString"
_MltNetSmbWorkGroupName_Object = MibTableColumn
mltNetSmbWorkGroupName = _MltNetSmbWorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 3),
    _MltNetSmbWorkGroupName_Type()
)
mltNetSmbWorkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmbWorkGroupName.setStatus("mandatory")


class _MltNetSmbHostName_Type(DisplayString):
    """Custom type mltNetSmbHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSmbHostName_Type.__name__ = "DisplayString"
_MltNetSmbHostName_Object = MibTableColumn
mltNetSmbHostName = _MltNetSmbHostName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 4),
    _MltNetSmbHostName_Type()
)
mltNetSmbHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmbHostName.setStatus("mandatory")


class _MltNetSmbWinsSupport_Type(Integer32):
    """Custom type mltNetSmbWinsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 0))
    )


_MltNetSmbWinsSupport_Type.__name__ = "Integer32"
_MltNetSmbWinsSupport_Object = MibTableColumn
mltNetSmbWinsSupport = _MltNetSmbWinsSupport_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 5),
    _MltNetSmbWinsSupport_Type()
)
mltNetSmbWinsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbWinsSupport.setStatus("mandatory")
_MltNetSmbWinsPrimaryServer_Type = IpAddress
_MltNetSmbWinsPrimaryServer_Object = MibTableColumn
mltNetSmbWinsPrimaryServer = _MltNetSmbWinsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 6),
    _MltNetSmbWinsPrimaryServer_Type()
)
mltNetSmbWinsPrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbWinsPrimaryServer.setStatus("mandatory")
_MltNetSmbWinsSecondaryServer_Type = IpAddress
_MltNetSmbWinsSecondaryServer_Object = MibTableColumn
mltNetSmbWinsSecondaryServer = _MltNetSmbWinsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 1, 1, 7),
    _MltNetSmbWinsSecondaryServer_Type()
)
mltNetSmbWinsSecondaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbWinsSecondaryServer.setStatus("mandatory")
_MltNetSmbPrinterTable_Object = MibTable
mltNetSmbPrinterTable = _MltNetSmbPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    mltNetSmbPrinterTable.setStatus("mandatory")
_MltNetSmbPrinterEntry_Object = MibTableRow
mltNetSmbPrinterEntry = _MltNetSmbPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2, 1)
)
mltNetSmbPrinterEntry.setIndexNames(
    (0, "MC2350-MIB", "mltNetSmbPrinterIfIndex"),
    (0, "MC2350-MIB", "mltNetSmbPrinterIndex"),
)
if mibBuilder.loadTexts:
    mltNetSmbPrinterEntry.setStatus("mandatory")
_MltNetSmbPrinterIfIndex_Type = Integer32
_MltNetSmbPrinterIfIndex_Object = MibTableColumn
mltNetSmbPrinterIfIndex = _MltNetSmbPrinterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2, 1, 1),
    _MltNetSmbPrinterIfIndex_Type()
)
mltNetSmbPrinterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbPrinterIfIndex.setStatus("mandatory")
_MltNetSmbPrinterIndex_Type = Integer32
_MltNetSmbPrinterIndex_Object = MibTableColumn
mltNetSmbPrinterIndex = _MltNetSmbPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2, 1, 2),
    _MltNetSmbPrinterIndex_Type()
)
mltNetSmbPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbPrinterIndex.setStatus("mandatory")


class _MltNetSmbPrinterName_Type(DisplayString):
    """Custom type mltNetSmbPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSmbPrinterName_Type.__name__ = "DisplayString"
_MltNetSmbPrinterName_Object = MibTableColumn
mltNetSmbPrinterName = _MltNetSmbPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2, 1, 3),
    _MltNetSmbPrinterName_Type()
)
mltNetSmbPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltNetSmbPrinterName.setStatus("mandatory")


class _MltNetSmbPrinterDescr_Type(DisplayString):
    """Custom type mltNetSmbPrinterDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltNetSmbPrinterDescr_Type.__name__ = "DisplayString"
_MltNetSmbPrinterDescr_Object = MibTableColumn
mltNetSmbPrinterDescr = _MltNetSmbPrinterDescr_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 2, 1, 5, 10, 2, 1, 4),
    _MltNetSmbPrinterDescr_Type()
)
mltNetSmbPrinterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltNetSmbPrinterDescr.setStatus("mandatory")
_MltDevice_ObjectIdentity = ObjectIdentity
mltDevice = _MltDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 3)
)
_MltJob_ObjectIdentity = ObjectIdentity
mltJob = _MltJob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4)
)
_MltJobManagement_ObjectIdentity = ObjectIdentity
mltJobManagement = _MltJobManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1)
)


class _MltJmMibVersion_Type(DisplayString):
    """Custom type mltJmMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MltJmMibVersion_Type.__name__ = "DisplayString"
_MltJmMibVersion_Object = MibScalar
mltJmMibVersion = _MltJmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 1),
    _MltJmMibVersion_Type()
)
mltJmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmMibVersion.setStatus("mandatory")
_MltJmGeneral_ObjectIdentity = ObjectIdentity
mltJmGeneral = _MltJmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2)
)
_MltJmGeneralTable_Object = MibTable
mltJmGeneralTable = _MltJmGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mltJmGeneralTable.setStatus("mandatory")
_MltJmGeneralEntry_Object = MibTableRow
mltJmGeneralEntry = _MltJmGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1)
)
mltJmGeneralEntry.setIndexNames(
    (0, "MC2350-MIB", "mltJmGeneralJobSetIndex"),
)
if mibBuilder.loadTexts:
    mltJmGeneralEntry.setStatus("mandatory")
_MltJmGeneralJobSetIndex_Type = Integer32
_MltJmGeneralJobSetIndex_Object = MibTableColumn
mltJmGeneralJobSetIndex = _MltJmGeneralJobSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 1),
    _MltJmGeneralJobSetIndex_Type()
)
mltJmGeneralJobSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralJobSetIndex.setStatus("mandatory")
_MltJmGeneralNumberOfActiveJobs_Type = Integer32
_MltJmGeneralNumberOfActiveJobs_Object = MibTableColumn
mltJmGeneralNumberOfActiveJobs = _MltJmGeneralNumberOfActiveJobs_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 2),
    _MltJmGeneralNumberOfActiveJobs_Type()
)
mltJmGeneralNumberOfActiveJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralNumberOfActiveJobs.setStatus("mandatory")
_MltJmGeneralOldestActiveJobIndex_Type = Integer32
_MltJmGeneralOldestActiveJobIndex_Object = MibTableColumn
mltJmGeneralOldestActiveJobIndex = _MltJmGeneralOldestActiveJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 3),
    _MltJmGeneralOldestActiveJobIndex_Type()
)
mltJmGeneralOldestActiveJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralOldestActiveJobIndex.setStatus("mandatory")
_MltJmGeneralNewestActiveJobIndex_Type = Integer32
_MltJmGeneralNewestActiveJobIndex_Object = MibTableColumn
mltJmGeneralNewestActiveJobIndex = _MltJmGeneralNewestActiveJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 4),
    _MltJmGeneralNewestActiveJobIndex_Type()
)
mltJmGeneralNewestActiveJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralNewestActiveJobIndex.setStatus("mandatory")
_MltJmGeneralJobPersistence_Type = Integer32
_MltJmGeneralJobPersistence_Object = MibTableColumn
mltJmGeneralJobPersistence = _MltJmGeneralJobPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 5),
    _MltJmGeneralJobPersistence_Type()
)
mltJmGeneralJobPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralJobPersistence.setStatus("mandatory")


class _MltJmGeneralJobSetType_Type(Integer32):
    """Custom type mltJmGeneralJobSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("faxReceive", 5),
          ("faxSend", 6),
          ("mfpAll", 0),
          ("other", 7),
          ("print", 2),
          ("receiveJob", 3),
          ("sendJob", 4))
    )


_MltJmGeneralJobSetType_Type.__name__ = "Integer32"
_MltJmGeneralJobSetType_Object = MibTableColumn
mltJmGeneralJobSetType = _MltJmGeneralJobSetType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 2, 1, 1, 6),
    _MltJmGeneralJobSetType_Type()
)
mltJmGeneralJobSetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmGeneralJobSetType.setStatus("mandatory")
_MltJmJob_ObjectIdentity = ObjectIdentity
mltJmJob = _MltJmJob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3)
)
_MltJmJobTable_Object = MibTable
mltJmJobTable = _MltJmJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mltJmJobTable.setStatus("mandatory")
_MltJmJobEntry_Object = MibTableRow
mltJmJobEntry = _MltJmJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1)
)
mltJmJobEntry.setIndexNames(
    (0, "MC2350-MIB", "mltJmJobJobSetIndex"),
    (0, "MC2350-MIB", "mltJmJobIndex"),
)
if mibBuilder.loadTexts:
    mltJmJobEntry.setStatus("mandatory")
_MltJmJobJobSetIndex_Type = Integer32
_MltJmJobJobSetIndex_Object = MibTableColumn
mltJmJobJobSetIndex = _MltJmJobJobSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 1),
    _MltJmJobJobSetIndex_Type()
)
mltJmJobJobSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobJobSetIndex.setStatus("mandatory")


class _MltJmJobIndex_Type(Integer32):
    """Custom type mltJmJobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MltJmJobIndex_Type.__name__ = "Integer32"
_MltJmJobIndex_Object = MibTableColumn
mltJmJobIndex = _MltJmJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 2),
    _MltJmJobIndex_Type()
)
mltJmJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobIndex.setStatus("mandatory")


class _MltJmJobFunction_Type(Integer32):
    """Custom type mltJmJobFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("faxReceive", 5),
          ("faxSend", 6),
          ("other", 7),
          ("print", 2),
          ("receiveJob", 3),
          ("sendJob", 4),
          ("unknown", 0))
    )


_MltJmJobFunction_Type.__name__ = "Integer32"
_MltJmJobFunction_Object = MibTableColumn
mltJmJobFunction = _MltJmJobFunction_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 3),
    _MltJmJobFunction_Type()
)
mltJmJobFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobFunction.setStatus("mandatory")


class _MltJmJobStatus_Type(Integer32):
    """Custom type mltJmJobStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10,
              11,
              12,
              20,
              21,
              22,
              23,
              24,
              25,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 32),
          ("cancelRequest", 2),
          ("canceled", 33),
          ("caution", 31),
          ("completed", 30),
          ("other", 1),
          ("pending", 10),
          ("pendingHeld", 11),
          ("pendingPaused", 12),
          ("printing", 23),
          ("processing", 20),
          ("processingStopped", 25),
          ("puaseRequest", 3),
          ("receiving", 22),
          ("restartRequest", 4),
          ("scanning", 24),
          ("sending", 21),
          ("unknown", 0))
    )


_MltJmJobStatus_Type.__name__ = "Integer32"
_MltJmJobStatus_Object = MibTableColumn
mltJmJobStatus = _MltJmJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 4),
    _MltJmJobStatus_Type()
)
mltJmJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmJobStatus.setStatus("mandatory")
_MltJmJobReceivedTime_Type = DateAndTime
_MltJmJobReceivedTime_Object = MibTableColumn
mltJmJobReceivedTime = _MltJmJobReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 6),
    _MltJmJobReceivedTime_Type()
)
mltJmJobReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobReceivedTime.setStatus("mandatory")
_MltJmJobCompleteTime_Type = DateAndTime
_MltJmJobCompleteTime_Object = MibTableColumn
mltJmJobCompleteTime = _MltJmJobCompleteTime_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 7),
    _MltJmJobCompleteTime_Type()
)
mltJmJobCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobCompleteTime.setStatus("mandatory")


class _MltJmJobPriority_Type(Integer32):
    """Custom type mltJmJobPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 4),
          ("highestPriority", 5),
          ("lowPriority", 2),
          ("lowestPriority", 1),
          ("normalPriority", 3),
          ("notSupported", 0))
    )


_MltJmJobPriority_Type.__name__ = "Integer32"
_MltJmJobPriority_Object = MibTableColumn
mltJmJobPriority = _MltJmJobPriority_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 8),
    _MltJmJobPriority_Type()
)
mltJmJobPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmJobPriority.setStatus("mandatory")
_MltJmJobDivNumber_Type = Integer32
_MltJmJobDivNumber_Object = MibTableColumn
mltJmJobDivNumber = _MltJmJobDivNumber_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 9),
    _MltJmJobDivNumber_Type()
)
mltJmJobDivNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDivNumber.setStatus("mandatory")


class _MltJmJobOwner_Type(DisplayString):
    """Custom type mltJmJobOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltJmJobOwner_Type.__name__ = "DisplayString"
_MltJmJobOwner_Object = MibTableColumn
mltJmJobOwner = _MltJmJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 10),
    _MltJmJobOwner_Type()
)
mltJmJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobOwner.setStatus("mandatory")


class _MltJmJobType_Type(Integer32):
    """Custom type mltJmJobType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              11,
              12,
              13,
              14,
              15,
              16,
              20,
              21,
              22,
              23,
              24,
              25,
              29,
              31,
              40,
              51,
              52)
        )
    )
    namedValues = NamedValues(
        *(("eMail", 11),
          ("faxRecieved", 51),
          ("faxSend", 52),
          ("iFaxReceive", 31),
          ("iFaxSend", 12),
          ("ippPrint", 21),
          ("normalCopy", 40),
          ("normalPrint", 20),
          ("other", 0),
          ("printToHDD", 24),
          ("proofAndPrint", 25),
          ("reportPrint", 29),
          ("scanToHDD", 15),
          ("scanToPC", 14),
          ("scanToServer", 13),
          ("securePrint", 22),
          ("timerPrint", 23),
          ("twain", 16))
    )


_MltJmJobType_Type.__name__ = "Integer32"
_MltJmJobType_Object = MibTableColumn
mltJmJobType = _MltJmJobType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 11),
    _MltJmJobType_Type()
)
mltJmJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobType.setStatus("mandatory")


class _MltJmJobName_Type(DisplayString):
    """Custom type mltJmJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MltJmJobName_Type.__name__ = "DisplayString"
_MltJmJobName_Object = MibTableColumn
mltJmJobName = _MltJmJobName_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 12),
    _MltJmJobName_Type()
)
mltJmJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobName.setStatus("mandatory")
_MltJmJobDocPageNumbers_Type = Integer32
_MltJmJobDocPageNumbers_Object = MibTableColumn
mltJmJobDocPageNumbers = _MltJmJobDocPageNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 13),
    _MltJmJobDocPageNumbers_Type()
)
mltJmJobDocPageNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDocPageNumbers.setStatus("mandatory")
_MltJmJobDocCopyNumbers_Type = Integer32
_MltJmJobDocCopyNumbers_Object = MibTableColumn
mltJmJobDocCopyNumbers = _MltJmJobDocCopyNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 14),
    _MltJmJobDocCopyNumbers_Type()
)
mltJmJobDocCopyNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDocCopyNumbers.setStatus("mandatory")


class _MltJmJobPageSize_Type(Integer32):
    """Custom type mltJmJobPageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
              50,
              51,
              52,
              53,
              54,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              70,
              71,
              74,
              76,
              83,
              84,
              93,
              114,
              115,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("a0", 11),
          ("a1", 12),
          ("a2", 13),
          ("a3", 14),
          ("a3W", 114),
          ("a4", 15),
          ("a4W", 115),
          ("a5", 16),
          ("a5W", 116),
          ("a6", 17),
          ("a6W", 117),
          ("b0", 21),
          ("b1", 22),
          ("b2", 23),
          ("b3", 24),
          ("b4", 25),
          ("b5", 26),
          ("b6", 27),
          ("choukei-3Gou", 83),
          ("choukei-4Gou", 84),
          ("comp", 34),
          ("envelopeB5", 63),
          ("envelopeC5", 65),
          ("envelopeC6", 68),
          ("envelopeCom10", 64),
          ("envelopeDL", 66),
          ("envelopeMonarch", 67),
          ("executive", 42),
          ("fls", 50),
          ("fls0", 51),
          ("fls1", 52),
          ("fls2", 53),
          ("fls3", 54),
          ("govLetter", 40),
          ("govRegal", 44),
          ("hagaki", 61),
          ("kakugata-3Gou", 93),
          ("ledger", 31),
          ("legal", 37),
          ("letter", 39),
          ("otherPaperSize", 0),
          ("oufuku-Hagaki", 62),
          ("quarto", 41),
          ("statement", 43),
          ("unknownPaperSize", 1),
          ("us10x14", 35),
          ("us11x14", 33),
          ("us11x15", 32),
          ("us12x14", 30),
          ("us3x5", 46),
          ("us4x6", 47),
          ("us8-1by4x11-3by4", 38),
          ("us9-1by4x14", 36),
          ("youkei-0Gou", 70),
          ("youkei-1Gou", 71),
          ("youkei-4Gou", 74),
          ("youkei-6Gou", 76))
    )


_MltJmJobPageSize_Type.__name__ = "Integer32"
_MltJmJobPageSize_Object = MibTableColumn
mltJmJobPageSize = _MltJmJobPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 15),
    _MltJmJobPageSize_Type()
)
mltJmJobPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobPageSize.setStatus("mandatory")


class _MltJmJobDestination_Type(DisplayString):
    """Custom type mltJmJobDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltJmJobDestination_Type.__name__ = "DisplayString"
_MltJmJobDestination_Object = MibTableColumn
mltJmJobDestination = _MltJmJobDestination_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 16),
    _MltJmJobDestination_Type()
)
mltJmJobDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDestination.setStatus("mandatory")
_MltJmJobDataSize_Type = Integer32
_MltJmJobDataSize_Object = MibTableColumn
mltJmJobDataSize = _MltJmJobDataSize_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 18),
    _MltJmJobDataSize_Type()
)
mltJmJobDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDataSize.setStatus("optional")


class _MltJmJobColorMode_Type(Integer32):
    """Custom type mltJmJobColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blackWhite", 4),
          ("color", 2),
          ("grayScale", 3),
          ("other", 0),
          ("unknown", 1))
    )


_MltJmJobColorMode_Type.__name__ = "Integer32"
_MltJmJobColorMode_Object = MibTableColumn
mltJmJobColorMode = _MltJmJobColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 19),
    _MltJmJobColorMode_Type()
)
mltJmJobColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobColorMode.setStatus("optional")


class _MltJmJobFormat_Type(Integer32):
    """Custom type mltJmJobFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("gdi", 11),
          ("jpeg", 7),
          ("linePrinter", 12),
          ("other", 0),
          ("pcl", 9),
          ("pdf", 8),
          ("postScript", 10),
          ("raw", 2),
          ("tiff", 3),
          ("tiff-MH", 4),
          ("tiff-MMR", 6),
          ("tiff-MR", 5),
          ("unknown", 1))
    )


_MltJmJobFormat_Type.__name__ = "Integer32"
_MltJmJobFormat_Object = MibTableColumn
mltJmJobFormat = _MltJmJobFormat_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 20),
    _MltJmJobFormat_Type()
)
mltJmJobFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobFormat.setStatus("optional")
_MltJmJobXResolution_Type = Integer32
_MltJmJobXResolution_Object = MibTableColumn
mltJmJobXResolution = _MltJmJobXResolution_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 21),
    _MltJmJobXResolution_Type()
)
mltJmJobXResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobXResolution.setStatus("optional")
_MltJmJobYResolution_Type = Integer32
_MltJmJobYResolution_Object = MibTableColumn
mltJmJobYResolution = _MltJmJobYResolution_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 22),
    _MltJmJobYResolution_Type()
)
mltJmJobYResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobYResolution.setStatus("optional")


class _MltJmJobDuplex_Type(Integer32):
    """Custom type mltJmJobDuplex based on Integer32"""
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


_MltJmJobDuplex_Type.__name__ = "Integer32"
_MltJmJobDuplex_Object = MibTableColumn
mltJmJobDuplex = _MltJmJobDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 23),
    _MltJmJobDuplex_Type()
)
mltJmJobDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobDuplex.setStatus("optional")
_MltJmJobOutputPages_Type = Integer32
_MltJmJobOutputPages_Object = MibTableColumn
mltJmJobOutputPages = _MltJmJobOutputPages_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 25),
    _MltJmJobOutputPages_Type()
)
mltJmJobOutputPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobOutputPages.setStatus("optional")
_MltJmJobOutputSheets_Type = Integer32
_MltJmJobOutputSheets_Object = MibTableColumn
mltJmJobOutputSheets = _MltJmJobOutputSheets_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 26),
    _MltJmJobOutputSheets_Type()
)
mltJmJobOutputSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobOutputSheets.setStatus("optional")


class _MltJmJobMediaType_Type(Integer32):
    """Custom type mltJmJobMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(208,
              209,
              210,
              211,
              212,
              214,
              216,
              222,
              223,
              224,
              225,
              226,
              227,
              230,
              236,
              240,
              241,
              242,
              244,
              246,
              248)
        )
    )
    namedValues = NamedValues(
        *(("envelope", 240),
          ("envelope-2side", 241),
          ("label", 242),
          ("letterHead", 246),
          ("ohp", 230),
          ("otherMediaType", 208),
          ("plainPaper", 210),
          ("plainPaper2side", 211),
          ("plainPaperColor", 216),
          ("plainPaperExclusive", 214),
          ("plainPaperRecycled", 212),
          ("postCard", 244),
          ("tab", 248),
          ("thick1", 222),
          ("thick1-2side", 223),
          ("thick2", 224),
          ("thick2-2side", 225),
          ("thick3", 226),
          ("thick3-2side", 227),
          ("thin", 236),
          ("unknownMediaType", 209))
    )


_MltJmJobMediaType_Type.__name__ = "Integer32"
_MltJmJobMediaType_Object = MibTableColumn
mltJmJobMediaType = _MltJmJobMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 3, 1, 1, 27),
    _MltJmJobMediaType_Type()
)
mltJmJobMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmJobMediaType.setStatus("mandatory")
_MltJmReport_ObjectIdentity = ObjectIdentity
mltJmReport = _MltJmReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4)
)
_MltJmReportTable_Object = MibTable
mltJmReportTable = _MltJmReportTable_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mltJmReportTable.setStatus("mandatory")
_MltJmReportEntry_Object = MibTableRow
mltJmReportEntry = _MltJmReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1)
)
mltJmReportEntry.setIndexNames(
    (0, "MC2350-MIB", "mltJmReportIndex"),
)
if mibBuilder.loadTexts:
    mltJmReportEntry.setStatus("mandatory")
_MltJmReportIndex_Type = Integer32
_MltJmReportIndex_Object = MibTableColumn
mltJmReportIndex = _MltJmReportIndex_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 1),
    _MltJmReportIndex_Type()
)
mltJmReportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmReportIndex.setStatus("mandatory")


class _MltJmReportAddress_Type(DisplayString):
    """Custom type mltJmReportAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_MltJmReportAddress_Type.__name__ = "DisplayString"
_MltJmReportAddress_Object = MibTableColumn
mltJmReportAddress = _MltJmReportAddress_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 2),
    _MltJmReportAddress_Type()
)
mltJmReportAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmReportAddress.setStatus("mandatory")
_MltJmKeepAliveCount_Type = Integer32
_MltJmKeepAliveCount_Object = MibTableColumn
mltJmKeepAliveCount = _MltJmKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 3),
    _MltJmKeepAliveCount_Type()
)
mltJmKeepAliveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmKeepAliveCount.setStatus("mandatory")


class _MltJmReportInterval_Type(Integer32):
    """Custom type mltJmReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("each1", 1),
          ("each10", 2),
          ("each100", 4),
          ("each250", 5),
          ("each50", 3),
          ("each500", 6),
          ("notSend", 0))
    )


_MltJmReportInterval_Type.__name__ = "Integer32"
_MltJmReportInterval_Object = MibTableColumn
mltJmReportInterval = _MltJmReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 5),
    _MltJmReportInterval_Type()
)
mltJmReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmReportInterval.setStatus("optional")


class _MltJmReporIntervalSelection_Type(Integer32):
    """Custom type mltJmReporIntervalSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("each1", 1),
          ("each10", 2),
          ("each100", 4),
          ("each250", 5),
          ("each50", 3),
          ("each500", 6),
          ("notSend", 0))
    )


_MltJmReporIntervalSelection_Type.__name__ = "Integer32"
_MltJmReporIntervalSelection_Object = MibTableColumn
mltJmReporIntervalSelection = _MltJmReporIntervalSelection_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 6),
    _MltJmReporIntervalSelection_Type()
)
mltJmReporIntervalSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltJmReporIntervalSelection.setStatus("optional")
_MltJmReportRequest_Type = Integer32
_MltJmReportRequest_Object = MibTableColumn
mltJmReportRequest = _MltJmReportRequest_Object(
    (1, 3, 6, 1, 4, 1, 2590, 1, 1, 4, 1, 4, 1, 1, 7),
    _MltJmReportRequest_Type()
)
mltJmReportRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltJmReportRequest.setStatus("optional")
_MltDirectory_ObjectIdentity = ObjectIdentity
mltDirectory = _MltDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2590, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MC2350-MIB",
    **{"CodedCharSet": CodedCharSet,
       "minolta": minolta,
       "mltMgmt": mltMgmt,
       "mltMib": mltMib,
       "mltSystem": mltSystem,
       "mltPrinter": mltPrinter,
       "mltPrinterMib": mltPrinterMib,
       "mltPrtMibInfo": mltPrtMibInfo,
       "mltPrtMibVersion": mltPrtMibVersion,
       "mltPrtCommand": mltPrtCommand,
       "mltPrtCommandTable": mltPrtCommandTable,
       "mltPrtCommandEntry": mltPrtCommandEntry,
       "mltPrtCommandOnline": mltPrtCommandOnline,
       "mltPrtCommandJobCancel": mltPrtCommandJobCancel,
       "mltPrtCommandJobProceed": mltPrtCommandJobProceed,
       "mltPrtPrintPageTable": mltPrtPrintPageTable,
       "mltPrtPrintPageEntry": mltPrtPrintPageEntry,
       "mltPrtPrintPageIndex": mltPrtPrintPageIndex,
       "mltPrtPrintPageName": mltPrtPrintPageName,
       "mltPrtPrintCommand": mltPrtPrintCommand,
       "mltPrtConfig": mltPrtConfig,
       "mltPrtSysConfigTable": mltPrtSysConfigTable,
       "mltPrtSysConfigEntry": mltPrtSysConfigEntry,
       "mltPrtJobLanguage": mltPrtJobLanguage,
       "mltPrtPowerSave": mltPrtPowerSave,
       "mltPrtAutoContinue": mltPrtAutoContinue,
       "mltPrtPaperTimeOut": mltPrtPaperTimeOut,
       "mltPrtPsErrorPrint": mltPrtPsErrorPrint,
       "mltPrtPrintConfigTable": mltPrtPrintConfigTable,
       "mltPrtPrintConfigEntry": mltPrtPrintConfigEntry,
       "mltPrtCopies": mltPrtCopies,
       "mltPrtPaperSize": mltPrtPaperSize,
       "mltPrtPaperSource": mltPrtPaperSource,
       "mltPrtFineArt": mltPrtFineArt,
       "mltPrtTonerSave": mltPrtTonerSave,
       "mltPrtFont": mltPrtFont,
       "mltPrtPclFontTable": mltPrtPclFontTable,
       "mltPrtPclFontEntry": mltPrtPclFontEntry,
       "mltPrtPclFontIndex": mltPrtPclFontIndex,
       "mltPrtPclFontName": mltPrtPclFontName,
       "mltPrtPclFontNumber": mltPrtPclFontNumber,
       "mltPrtPclFontSource": mltPrtPclFontSource,
       "mltPrtPsFontTable": mltPrtPsFontTable,
       "mltPrtPsFontEntry": mltPrtPsFontEntry,
       "mltPrtPsFontIndex": mltPrtPsFontIndex,
       "mltPrtPsFontName": mltPrtPsFontName,
       "mltPrtPsFontNumber": mltPrtPsFontNumber,
       "mltPrtPsFontSource": mltPrtPsFontSource,
       "mltPrtSymbolSetTable": mltPrtSymbolSetTable,
       "mltPrtSymbolSetEntry": mltPrtSymbolSetEntry,
       "mltPrtSymbolSetIndex": mltPrtSymbolSetIndex,
       "mltPrtSymbolSetName": mltPrtSymbolSetName,
       "mltPrtCharSetID": mltPrtCharSetID,
       "mltPrtPaper": mltPrtPaper,
       "mltPrtPaperSizeTable": mltPrtPaperSizeTable,
       "mltPrtPaperSizeEntry": mltPrtPaperSizeEntry,
       "mltPaperSizeIndex": mltPaperSizeIndex,
       "mltPaperSizeName": mltPaperSizeName,
       "mltPaperFeedDir": mltPaperFeedDir,
       "mltPrtRemotePanel": mltPrtRemotePanel,
       "mltPrtRemotePanelButtonTable": mltPrtRemotePanelButtonTable,
       "mltPrtRemotePanelButtonEntry": mltPrtRemotePanelButtonEntry,
       "mltPrtPanelButtonIndex": mltPrtPanelButtonIndex,
       "mltPrtPanelButtonName": mltPrtPanelButtonName,
       "mltPrtPanelButtonPush": mltPrtPanelButtonPush,
       "mltPrtPanelButtonDescr": mltPrtPanelButtonDescr,
       "mltSysMib": mltSysMib,
       "mltSysMibVersion": mltSysMibVersion,
       "mltSysGeneralInfo": mltSysGeneralInfo,
       "mltSysPriorityDevice": mltSysPriorityDevice,
       "mltSysCurrentDateTime": mltSysCurrentDateTime,
       "mltSysContact": mltSysContact,
       "mltSysContactSiteName": mltSysContactSiteName,
       "mltSysContactInfo": mltSysContactInfo,
       "mltSysProductHelpURL": mltSysProductHelpURL,
       "mltSysCorpURL": mltSysCorpURL,
       "mltSysSuppliesInfo": mltSysSuppliesInfo,
       "mltSysVersion": mltSysVersion,
       "mltSysVersionTable": mltSysVersionTable,
       "mltSysVersionEntry": mltSysVersionEntry,
       "mltSysVersionIndex": mltSysVersionIndex,
       "mltSysVerName": mltSysVerName,
       "mltSysVersionCode": mltSysVersionCode,
       "mltSysVerDescr": mltSysVerDescr,
       "mltSysComponent": mltSysComponent,
       "mltSysCompConfigID": mltSysCompConfigID,
       "mltSysInputTrayTable": mltSysInputTrayTable,
       "mltSysInputTrayEntry": mltSysInputTrayEntry,
       "mltSysInputTrayIndex": mltSysInputTrayIndex,
       "mltSysInputTrayRefIndex": mltSysInputTrayRefIndex,
       "mltSysInputTrayName": mltSysInputTrayName,
       "mltSysInputTrayCapacitySence": mltSysInputTrayCapacitySence,
       "mltSysInputTraySpecialPaper": mltSysInputTraySpecialPaper,
       "mltSysInputTrayPaperAttribute": mltSysInputTrayPaperAttribute,
       "mltSysOutputTrayTable": mltSysOutputTrayTable,
       "mltSysOutputTrayEntry": mltSysOutputTrayEntry,
       "mltSysOutputTrayIndex": mltSysOutputTrayIndex,
       "mltSysOutputTrayRefIndex": mltSysOutputTrayRefIndex,
       "mltSysOutputTrayDefaultName": mltSysOutputTrayDefaultName,
       "mltSysOutputTrayNickName": mltSysOutputTrayNickName,
       "mltSysOutputTrayType": mltSysOutputTrayType,
       "mltSysCounter": mltSysCounter,
       "mltSysCounterConfig": mltSysCounterConfig,
       "mltSysSupportedCounterType": mltSysSupportedCounterType,
       "mltSysDuplexCountMode": mltSysDuplexCountMode,
       "mltSysLargeSizeCountMode": mltSysLargeSizeCountMode,
       "mltSysLargeSizeType": mltSysLargeSizeType,
       "mltSysColorCountSupportType": mltSysColorCountSupportType,
       "mltSysSystemCounter": mltSysSystemCounter,
       "mltSysGeneralCounter": mltSysGeneralCounter,
       "mltSysTotalCount": mltSysTotalCount,
       "mltSysLargeSizeCount": mltSysLargeSizeCount,
       "mltSysDuplexCount": mltSysDuplexCount,
       "mltSysLargeDuplexCount": mltSysLargeDuplexCount,
       "mltSysSendTotalCount": mltSysSendTotalCount,
       "mltSysTotalJamCount": mltSysTotalJamCount,
       "mltSysTotalTroubleCount": mltSysTotalTroubleCount,
       "mltSysPrintFunctionCounterTable": mltSysPrintFunctionCounterTable,
       "mltSysPrintFunctionCounterEntry": mltSysPrintFunctionCounterEntry,
       "mltSysPrintFunctionColorIndex": mltSysPrintFunctionColorIndex,
       "mltSysPrintFunctionIndex": mltSysPrintFunctionIndex,
       "mltSysPrintFunctionColorType": mltSysPrintFunctionColorType,
       "mltSysPrintFunctionType": mltSysPrintFunctionType,
       "mltSysPrintFunctionTotalCount": mltSysPrintFunctionTotalCount,
       "mltSysPrintFunctionDuplexCount": mltSysPrintFunctionDuplexCount,
       "mltSysPrintFunctionLargeSizeCount": mltSysPrintFunctionLargeSizeCount,
       "mltSysPrintFunctionLargeDuplexCount": mltSysPrintFunctionLargeDuplexCount,
       "mltSysSizeCounterTable": mltSysSizeCounterTable,
       "mltSysSizeCounterEntry": mltSysSizeCounterEntry,
       "mltSysSizeFunctionIndex": mltSysSizeFunctionIndex,
       "mltSysSizeTypeIndex": mltSysSizeTypeIndex,
       "mltSysSizeFunction": mltSysSizeFunction,
       "mltSysSizeType": mltSysSizeType,
       "mltSysSizeCount": mltSysSizeCount,
       "mltSysTonerLifeCounterTable": mltSysTonerLifeCounterTable,
       "mltSysTonerLifeCounterEntry": mltSysTonerLifeCounterEntry,
       "mltSysTonerTypeIndex": mltSysTonerTypeIndex,
       "mltSysTonerType": mltSysTonerType,
       "mltTonerTypeCount": mltTonerTypeCount,
       "mltInterface": mltInterface,
       "mltNetwork": mltNetwork,
       "mltNetworkMib": mltNetworkMib,
       "mltNetMibVersion": mltNetMibVersion,
       "mltNetGeneral": mltNetGeneral,
       "mltNetGeneralTable": mltNetGeneralTable,
       "mltNetGeneralEntry": mltNetGeneralEntry,
       "mltNetGeneralIndex": mltNetGeneralIndex,
       "mltNetFirmVersion": mltNetFirmVersion,
       "mltNetHardwareAddress": mltNetHardwareAddress,
       "mltNetSerialNumber": mltNetSerialNumber,
       "mltNetSupportedConnector": mltNetSupportedConnector,
       "mltNetCurrentConnector": mltNetCurrentConnector,
       "mltNetSpeedConfig": mltNetSpeedConfig,
       "mltNetInterfaceType": mltNetInterfaceType,
       "mltNetIfDescr": mltNetIfDescr,
       "mltNetProtocol": mltNetProtocol,
       "mltNetProtocolTable": mltNetProtocolTable,
       "mltNetProtocolEntry": mltNetProtocolEntry,
       "mltNetProtocolIfIndex": mltNetProtocolIfIndex,
       "mltNetProtocolIndex": mltNetProtocolIndex,
       "mltNetProtocolType": mltNetProtocolType,
       "mltNetProtocolDescr": mltNetProtocolDescr,
       "mltNetProtocolVer": mltNetProtocolVer,
       "mltNetProtocolOnOff": mltNetProtocolOnOff,
       "mltNetCommand": mltNetCommand,
       "mltNetCommandTable": mltNetCommandTable,
       "mltNetCommandEntry": mltNetCommandEntry,
       "mltNetCommandIfIndex": mltNetCommandIfIndex,
       "mltNetCommandReset": mltNetCommandReset,
       "mltNetCommandDefault": mltNetCommandDefault,
       "mltNetCommandPrintNicConfig": mltNetCommandPrintNicConfig,
       "mltNetCommandStartupConfig": mltNetCommandStartupConfig,
       "mltNetCommandDownLoad": mltNetCommandDownLoad,
       "mltNetSnmp": mltNetSnmp,
       "mltNetSnmpCommTable": mltNetSnmpCommTable,
       "mltNetSnmpCommEntry": mltNetSnmpCommEntry,
       "mltNetSnmpCommIndex": mltNetSnmpCommIndex,
       "mltNetSnmpCommName": mltNetSnmpCommName,
       "mltNetSnmpCommAccessRight": mltNetSnmpCommAccessRight,
       "mltNetSnmpTrapTable": mltNetSnmpTrapTable,
       "mltNetSnmpTrapEntry": mltNetSnmpTrapEntry,
       "mltNetSnmpTrapIfIndex": mltNetSnmpTrapIfIndex,
       "mltNetSnmpTrapIndex": mltNetSnmpTrapIndex,
       "mltNetSnmpTrapCommunity": mltNetSnmpTrapCommunity,
       "mltNetSnmpTrapIpAddress": mltNetSnmpTrapIpAddress,
       "mltNetSnmpTrapIpxAddress": mltNetSnmpTrapIpxAddress,
       "mltNetSnmpTrapOnOff": mltNetSnmpTrapOnOff,
       "mltNetTcpip": mltNetTcpip,
       "mltNetTcpipGeneral": mltNetTcpipGeneral,
       "mltNetTcpipGeneralTable": mltNetTcpipGeneralTable,
       "mltNetTcpipGeneralEntry": mltNetTcpipGeneralEntry,
       "mltNetTcpipIfIndex": mltNetTcpipIfIndex,
       "mltNetTcpipDefault": mltNetTcpipDefault,
       "mltNetTcpipAddress": mltNetTcpipAddress,
       "mltNetTcpipSubnet": mltNetTcpipSubnet,
       "mltNetTcpipGateway": mltNetTcpipGateway,
       "mltNetTcpipUseBootProtocol": mltNetTcpipUseBootProtocol,
       "mltNetTcpipBootProtocolEnable": mltNetTcpipBootProtocolEnable,
       "mltNetTcpipAddressServer": mltNetTcpipAddressServer,
       "mltNetTcpipRawPortNumber": mltNetTcpipRawPortNumber,
       "mltNetTcpipSupportService": mltNetTcpipSupportService,
       "mltNetTcpipDnsSupport": mltNetTcpipDnsSupport,
       "mltNetTcpipDnsHostName": mltNetTcpipDnsHostName,
       "mltNetTcpipDnsDomainName": mltNetTcpipDnsDomainName,
       "mltNetTcpipDnsTable": mltNetTcpipDnsTable,
       "mltNetTcpipDnsEntry": mltNetTcpipDnsEntry,
       "mltNetTcpipDnsIfIndex": mltNetTcpipDnsIfIndex,
       "mltNetTcpipDnsServerIndex": mltNetTcpipDnsServerIndex,
       "mltNetTcpipDnsServerAddress": mltNetTcpipDnsServerAddress,
       "mltNetLpd": mltNetLpd,
       "mltNetLpdGeneralTable": mltNetLpdGeneralTable,
       "mltNetLpdGeneralEntry": mltNetLpdGeneralEntry,
       "mltNetLpdIfIndex": mltNetLpdIfIndex,
       "mltNetLpdEnable": mltNetLpdEnable,
       "mltNetLpdPort": mltNetLpdPort,
       "mltNetLpdQueueTable": mltNetLpdQueueTable,
       "mltNetLpdQueueEntry": mltNetLpdQueueEntry,
       "mltNetLpdQueueIfIndex": mltNetLpdQueueIfIndex,
       "mltNetLpdQueueIndex": mltNetLpdQueueIndex,
       "mltNetLpdQueueName": mltNetLpdQueueName,
       "mltNetLpdQueueDescr": mltNetLpdQueueDescr,
       "mltNetLpdQueueFilter": mltNetLpdQueueFilter,
       "mltNetLpdQueueBanner": mltNetLpdQueueBanner,
       "mltNetLpdQueueEnable": mltNetLpdQueueEnable,
       "mltNetFtpd": mltNetFtpd,
       "mltNetFtpdGeneralTable": mltNetFtpdGeneralTable,
       "mltNetFtpdGeneralEntry": mltNetFtpdGeneralEntry,
       "mltNetFtpdIfIndex": mltNetFtpdIfIndex,
       "mltNetFtpdEnable": mltNetFtpdEnable,
       "mltNetFtpdPort": mltNetFtpdPort,
       "mltNetFtpdConfigTable": mltNetFtpdConfigTable,
       "mltNetFtpdConfigEntry": mltNetFtpdConfigEntry,
       "mltNetFtpdConfigIfIndex": mltNetFtpdConfigIfIndex,
       "mltNetFtpdUserIndex": mltNetFtpdUserIndex,
       "mltNetFtpdUser": mltNetFtpdUser,
       "mltNetFtpdUserPassWd": mltNetFtpdUserPassWd,
       "mltNetFtpdCapability": mltNetFtpdCapability,
       "mltNetFtpdDescr": mltNetFtpdDescr,
       "mltNetHttpd": mltNetHttpd,
       "mltNetHttpdGeneralTable": mltNetHttpdGeneralTable,
       "mltNetHttpdGeneralEntry": mltNetHttpdGeneralEntry,
       "mltNetHttpdIfIndex": mltNetHttpdIfIndex,
       "mltNetHttpdEnable": mltNetHttpdEnable,
       "mltNetHttpdPort": mltNetHttpdPort,
       "mltNetHttpdDescr": mltNetHttpdDescr,
       "mltNetSmtpClient": mltNetSmtpClient,
       "mltNetSmtpGeneralTable": mltNetSmtpGeneralTable,
       "mltNetSmtpGeneralEntry": mltNetSmtpGeneralEntry,
       "mltNetSmtpIfIndex": mltNetSmtpIfIndex,
       "mltNetSmtpEnable": mltNetSmtpEnable,
       "mltNetSmtpServerAddress": mltNetSmtpServerAddress,
       "mltNetSmtpPort": mltNetSmtpPort,
       "mltNetSmtpAccountTable": mltNetSmtpAccountTable,
       "mltNetSmtpAccountEntry": mltNetSmtpAccountEntry,
       "mltNetSmtpAccountIfIndex": mltNetSmtpAccountIfIndex,
       "mltNetSmtpAccountIndex": mltNetSmtpAccountIndex,
       "mltNetSmtpFromAddress": mltNetSmtpFromAddress,
       "mltNetSmtpReplyAddress": mltNetSmtpReplyAddress,
       "mltNetSmtpConnTimeout": mltNetSmtpConnTimeout,
       "mltNetSmtpPurpose": mltNetSmtpPurpose,
       "mltNetSmtpDescription": mltNetSmtpDescription,
       "mltNetIpp": mltNetIpp,
       "mltNetIppGeneral": mltNetIppGeneral,
       "mltNetIppGeneralTable": mltNetIppGeneralTable,
       "mltNetIppGeneralEntry": mltNetIppGeneralEntry,
       "mltNetIppGeneralIfIndex": mltNetIppGeneralIfIndex,
       "mltNetIppServiceEnable": mltNetIppServiceEnable,
       "mltNetIppDefaultPortIndex": mltNetIppDefaultPortIndex,
       "mltNetIppPortTable": mltNetIppPortTable,
       "mltNetIppPortEntry": mltNetIppPortEntry,
       "mltNetIppPortIfIndex": mltNetIppPortIfIndex,
       "mltNetIppPortIndex": mltNetIppPortIndex,
       "mltNetIppPortNumber": mltNetIppPortNumber,
       "mltNetIppPrtDescrAttribute": mltNetIppPrtDescrAttribute,
       "mltNetIppPrtDescGeneralTable": mltNetIppPrtDescGeneralTable,
       "mltNetIppPrtDescGeneralEntry": mltNetIppPrtDescGeneralEntry,
       "mltIppPrtDescGeneralIfIndex": mltIppPrtDescGeneralIfIndex,
       "mltIppPrtName": mltIppPrtName,
       "mltIppPrtMoreInfo": mltIppPrtMoreInfo,
       "mltIppPrtState": mltIppPrtState,
       "mltIppCharSetConfiguredIndex": mltIppCharSetConfiguredIndex,
       "mltIppNaturalLanguageConfiguredIndex": mltIppNaturalLanguageConfiguredIndex,
       "mltIppDocFormatDefaultIndex": mltIppDocFormatDefaultIndex,
       "mltIppPrinterIsAcceptingJobs": mltIppPrinterIsAcceptingJobs,
       "mltIppQueuedJobCount": mltIppQueuedJobCount,
       "mltIppColorSupported": mltIppColorSupported,
       "mltIppPdlOverrideSupported": mltIppPdlOverrideSupported,
       "mltIppPrinterUpTime": mltIppPrinterUpTime,
       "mltIppPrtLocation": mltIppPrtLocation,
       "mltIppPrinterCurrentTime": mltIppPrinterCurrentTime,
       "mltIppUriSupportedTable": mltIppUriSupportedTable,
       "mltIppUriSupportedEntry": mltIppUriSupportedEntry,
       "mltIppUriIfIndex": mltIppUriIfIndex,
       "mltIppUriIndex": mltIppUriIndex,
       "mltIppUri": mltIppUri,
       "mltIppUriSecurity": mltIppUriSecurity,
       "mltIppUriAuthentication": mltIppUriAuthentication,
       "mltIppPrtStateReasonsTable": mltIppPrtStateReasonsTable,
       "mltIppPrtStateReasonsEntry": mltIppPrtStateReasonsEntry,
       "mltIppPrtStateReasonIfIndex": mltIppPrtStateReasonIfIndex,
       "mltIppPrtStateReasonIndex": mltIppPrtStateReasonIndex,
       "mltIppPrinterStateReason": mltIppPrinterStateReason,
       "mltIppPrtStateReasonSuffix": mltIppPrtStateReasonSuffix,
       "mltIppVersionsSupportedTable": mltIppVersionsSupportedTable,
       "mltIppVersionsSupportedEntry": mltIppVersionsSupportedEntry,
       "mltIppVersionIfIndex": mltIppVersionIfIndex,
       "mltIppVersionIndex": mltIppVersionIndex,
       "mltIppVersionType": mltIppVersionType,
       "mltIppOperationSupportedTable": mltIppOperationSupportedTable,
       "mltIppOperationSupportedEntry": mltIppOperationSupportedEntry,
       "mltIppOperationIfIndex": mltIppOperationIfIndex,
       "mltIppOperationIndex": mltIppOperationIndex,
       "mltIppOperationType": mltIppOperationType,
       "mltIppOperationEnable": mltIppOperationEnable,
       "mltIppCharSetSupportedTable": mltIppCharSetSupportedTable,
       "mltIppCharSetSupportedEntry": mltIppCharSetSupportedEntry,
       "mltIppCharSetIfIndex": mltIppCharSetIfIndex,
       "mltIppCharSetIndex": mltIppCharSetIndex,
       "mltIppCharSetName": mltIppCharSetName,
       "mltIppCharSetCode": mltIppCharSetCode,
       "mltIppNaturalLanguageSupportedTable": mltIppNaturalLanguageSupportedTable,
       "mltIppNaturalLanguageSupportedEntry": mltIppNaturalLanguageSupportedEntry,
       "mltIppNaturalLangIfIndex": mltIppNaturalLangIfIndex,
       "mltIppNaturalLangIndex": mltIppNaturalLangIndex,
       "mltIppNaturalLangName": mltIppNaturalLangName,
       "mltIppDocFormatSupportedTable": mltIppDocFormatSupportedTable,
       "mltIppDocFormatSupportedEntry": mltIppDocFormatSupportedEntry,
       "mltIppDocFormatIfIndex": mltIppDocFormatIfIndex,
       "mltIppDocFormatIndex": mltIppDocFormatIndex,
       "mltIppDocFormatName": mltIppDocFormatName,
       "mltIppCompressionSupportedTable": mltIppCompressionSupportedTable,
       "mltIppCompressionSupportedEntry": mltIppCompressionSupportedEntry,
       "mltIppCompressionIfIndex": mltIppCompressionIfIndex,
       "mltIppCompressionIndex": mltIppCompressionIndex,
       "mltIppCompressionType": mltIppCompressionType,
       "mltNetIppJobTemplateAttribute": mltNetIppJobTemplateAttribute,
       "mltNetIppJobTemplateGeneralTable": mltNetIppJobTemplateGeneralTable,
       "mltNetIppJobTemplateGeneralEntry": mltNetIppJobTemplateGeneralEntry,
       "mltIppJobTemplateGeneralIfIndex": mltIppJobTemplateGeneralIfIndex,
       "mltIppJobPriorityDefault": mltIppJobPriorityDefault,
       "mltIppJobPrioritySupported": mltIppJobPrioritySupported,
       "mltIppJobHoldUntilDefault": mltIppJobHoldUntilDefault,
       "mltIppJobSheetsDefault": mltIppJobSheetsDefault,
       "mltIppCopiesDefault": mltIppCopiesDefault,
       "mltIppCopiesMaxSupported": mltIppCopiesMaxSupported,
       "mltIppFinishingsDefault": mltIppFinishingsDefault,
       "mltIppPageRangesSupported": mltIppPageRangesSupported,
       "mltIppSidesDefault": mltIppSidesDefault,
       "mltIppNumberUpDefault": mltIppNumberUpDefault,
       "mltIppOrientationRequestedDefault": mltIppOrientationRequestedDefault,
       "mltIppMediaDefault": mltIppMediaDefault,
       "mltIppPrinterResolutionDefault": mltIppPrinterResolutionDefault,
       "mltIppPrintQualityDefault": mltIppPrintQualityDefault,
       "mltIppJobHoldUntilSupportedTable": mltIppJobHoldUntilSupportedTable,
       "mltIppJobHoldUntilSupportedEntry": mltIppJobHoldUntilSupportedEntry,
       "mltIppJobHoldUntilIfIndex": mltIppJobHoldUntilIfIndex,
       "mltIppJobHoldUntilIndex": mltIppJobHoldUntilIndex,
       "mltIppJobHoldUntilType": mltIppJobHoldUntilType,
       "mltIppJobSheetsSupportedTable": mltIppJobSheetsSupportedTable,
       "mltIppJobSheetsSupportedEntry": mltIppJobSheetsSupportedEntry,
       "mltIppJobSheetsIfIndex": mltIppJobSheetsIfIndex,
       "mltIppJobSheetsIndex": mltIppJobSheetsIndex,
       "mltIppJobSheetsType": mltIppJobSheetsType,
       "mltIppFinishingsSupportedTable": mltIppFinishingsSupportedTable,
       "mltIppFinishingsSupportedEntry": mltIppFinishingsSupportedEntry,
       "mltIppFinishingsIfIndex": mltIppFinishingsIfIndex,
       "mltIppFinishingsIndex": mltIppFinishingsIndex,
       "mltIppFinishingsType": mltIppFinishingsType,
       "mltIppSidesSupportedTable": mltIppSidesSupportedTable,
       "mltIppSidesSupportedEntry": mltIppSidesSupportedEntry,
       "mltIppSidesIfIndex": mltIppSidesIfIndex,
       "mltIppSidesIndex": mltIppSidesIndex,
       "mltIppSidesType": mltIppSidesType,
       "mltIppNumberUpSupportedTable": mltIppNumberUpSupportedTable,
       "mltIppNumberUpSupportedEntry": mltIppNumberUpSupportedEntry,
       "mltIppNumberUpIfIndex": mltIppNumberUpIfIndex,
       "mltIppNumberUpIndex": mltIppNumberUpIndex,
       "mltIppNumberUpType": mltIppNumberUpType,
       "mltIppOrientationRequestedSupportedTable": mltIppOrientationRequestedSupportedTable,
       "mltIppOrientationRequestedSupportedEntry": mltIppOrientationRequestedSupportedEntry,
       "mltIppOrientationRequestedIfIndex": mltIppOrientationRequestedIfIndex,
       "mltIppOrientationRequestedIndex": mltIppOrientationRequestedIndex,
       "mltIppOrientationRequestedType": mltIppOrientationRequestedType,
       "mltIppMediaSupportedTable": mltIppMediaSupportedTable,
       "mltIppMediaSupportedEntry": mltIppMediaSupportedEntry,
       "mltIppMediaIfIndex": mltIppMediaIfIndex,
       "mltIppMediaIndex": mltIppMediaIndex,
       "mltIppMediaName": mltIppMediaName,
       "mltIppMediaType": mltIppMediaType,
       "mltIppMediaColor": mltIppMediaColor,
       "mltIppMediaInputTray": mltIppMediaInputTray,
       "mltPrinterResolutionSupportedTable": mltPrinterResolutionSupportedTable,
       "mltPrinterResolutionSupportedEntry": mltPrinterResolutionSupportedEntry,
       "mltPrinterResolutionIfIndex": mltPrinterResolutionIfIndex,
       "mltPrinterResolutionIndex": mltPrinterResolutionIndex,
       "mltPrinterResolutionFeedDir": mltPrinterResolutionFeedDir,
       "mltPrinterResolutionXFeedDir": mltPrinterResolutionXFeedDir,
       "mltPrinterResolutionUnit": mltPrinterResolutionUnit,
       "mltPrintQualitySupportedTable": mltPrintQualitySupportedTable,
       "mltPrintQualitySupportedEntry": mltPrintQualitySupportedEntry,
       "mltPrintQualityIfIndex": mltPrintQualityIfIndex,
       "mltPrintQualityIndex": mltPrintQualityIndex,
       "mltPrintQualityType": mltPrintQualityType,
       "mltNetSlp": mltNetSlp,
       "mltNetSlpGeneralTable": mltNetSlpGeneralTable,
       "mltNetSlpGeneralEntry": mltNetSlpGeneralEntry,
       "mltNetSlpIfIndex": mltNetSlpIfIndex,
       "mltNetSlpEnable": mltNetSlpEnable,
       "mltNetSlpPortNumber": mltNetSlpPortNumber,
       "mltNetSlpMTU": mltNetSlpMTU,
       "mltNetSlpTTL": mltNetSlpTTL,
       "mltNetSlpBroadcastSupport": mltNetSlpBroadcastSupport,
       "mltNetSlpConfigTable": mltNetSlpConfigTable,
       "mltNetSlpConfigEntry": mltNetSlpConfigEntry,
       "mltNetSlpConfigIfIndex": mltNetSlpConfigIfIndex,
       "mltNetSlpIndex": mltNetSlpIndex,
       "mltNetSlpService": mltNetSlpService,
       "mltNetSlpScope": mltNetSlpScope,
       "mltNetSlpLifetime": mltNetSlpLifetime,
       "mltNetNetWare": mltNetNetWare,
       "mltNetNwGeneralTable": mltNetNwGeneralTable,
       "mltNetNwGeneralEntry": mltNetNwGeneralEntry,
       "mltNetNwIfIndex": mltNetNwIfIndex,
       "mltNetNwDefault": mltNetNwDefault,
       "mltNetNwFrameTypeConfig": mltNetNwFrameTypeConfig,
       "mltNetNwPrintMode": mltNetNwPrintMode,
       "mltNetNwFrameTable": mltNetNwFrameTable,
       "mltNetNwFrameEntry": mltNetNwFrameEntry,
       "mltNetNwFrameIfIndex": mltNetNwFrameIfIndex,
       "mltNetNwFrameIndex": mltNetNwFrameIndex,
       "mltNetNwFrameType": mltNetNwFrameType,
       "mltNetNwNetworkNumber": mltNetNwNetworkNumber,
       "mltNetNwPserverTable": mltNetNwPserverTable,
       "mltNetNwPserverEntry": mltNetNwPserverEntry,
       "mltNetNwPsIfIndex": mltNetNwPsIfIndex,
       "mltNetNwPsIndex": mltNetNwPsIndex,
       "mltNetNwPsName": mltNetNwPsName,
       "mltNetNwPsPasswd": mltNetNwPsPasswd,
       "mltNetNwPsMode": mltNetNwPsMode,
       "mltNetNwPsPrefFServer": mltNetNwPsPrefFServer,
       "mltNetNwPsPrefTree": mltNetNwPsPrefTree,
       "mltNetNwPsPrefContext": mltNetNwPsPrefContext,
       "mltNetNwPsPollingRate": mltNetNwPsPollingRate,
       "mltNetNwQueueTable": mltNetNwQueueTable,
       "mltNetNwQueueEntry": mltNetNwQueueEntry,
       "mltNetNwQueueIndex": mltNetNwQueueIndex,
       "mltNetNwQueueName": mltNetNwQueueName,
       "mltNetNwQueueRefIfIndex": mltNetNwQueueRefIfIndex,
       "mltNetNwQueueRefPsIndex": mltNetNwQueueRefPsIndex,
       "mltNetNwQueueStatus": mltNetNwQueueStatus,
       "mltNetNwNPrinterTable": mltNetNwNPrinterTable,
       "mltNetNwNPrinterEntry": mltNetNwNPrinterEntry,
       "mltNetNwNPrinterIfIndex": mltNetNwNPrinterIfIndex,
       "mltNetNwNPrinterIndex": mltNetNwNPrinterIndex,
       "mltNetNwNPrinterName": mltNetNwNPrinterName,
       "mltNetNwNPrinterNumber": mltNetNwNPrinterNumber,
       "mltNetAppleTalk": mltNetAppleTalk,
       "mltNetAppleTalkGeneralTable": mltNetAppleTalkGeneralTable,
       "mltNetAppleTalkGeneralEntry": mltNetAppleTalkGeneralEntry,
       "mltNetAtIfIndex": mltNetAtIfIndex,
       "mltNetAtDefault": mltNetAtDefault,
       "mltNetAtNetNumber": mltNetAtNetNumber,
       "mltNetAtNodeNumber": mltNetAtNodeNumber,
       "mltNetAtDesiredZone": mltNetAtDesiredZone,
       "mltNetAtCurrentZone": mltNetAtCurrentZone,
       "mltNetAtPrinterTable": mltNetAtPrinterTable,
       "mltNetAtPrinterEntry": mltNetAtPrinterEntry,
       "mltNetAtPrinterIfIndex": mltNetAtPrinterIfIndex,
       "mltNetAtPrinterIndex": mltNetAtPrinterIndex,
       "mltNetAtPrinterName": mltNetAtPrinterName,
       "mltNetAtPrinterType": mltNetAtPrinterType,
       "mltNetSmb": mltNetSmb,
       "mltNetSmbGeneralTable": mltNetSmbGeneralTable,
       "mltNetSmbGeneralEntry": mltNetSmbGeneralEntry,
       "mltNetSmbIfIndex": mltNetSmbIfIndex,
       "mltNetSmbDefault": mltNetSmbDefault,
       "mltNetSmbWorkGroupName": mltNetSmbWorkGroupName,
       "mltNetSmbHostName": mltNetSmbHostName,
       "mltNetSmbWinsSupport": mltNetSmbWinsSupport,
       "mltNetSmbWinsPrimaryServer": mltNetSmbWinsPrimaryServer,
       "mltNetSmbWinsSecondaryServer": mltNetSmbWinsSecondaryServer,
       "mltNetSmbPrinterTable": mltNetSmbPrinterTable,
       "mltNetSmbPrinterEntry": mltNetSmbPrinterEntry,
       "mltNetSmbPrinterIfIndex": mltNetSmbPrinterIfIndex,
       "mltNetSmbPrinterIndex": mltNetSmbPrinterIndex,
       "mltNetSmbPrinterName": mltNetSmbPrinterName,
       "mltNetSmbPrinterDescr": mltNetSmbPrinterDescr,
       "mltDevice": mltDevice,
       "mltJob": mltJob,
       "mltJobManagement": mltJobManagement,
       "mltJmMibVersion": mltJmMibVersion,
       "mltJmGeneral": mltJmGeneral,
       "mltJmGeneralTable": mltJmGeneralTable,
       "mltJmGeneralEntry": mltJmGeneralEntry,
       "mltJmGeneralJobSetIndex": mltJmGeneralJobSetIndex,
       "mltJmGeneralNumberOfActiveJobs": mltJmGeneralNumberOfActiveJobs,
       "mltJmGeneralOldestActiveJobIndex": mltJmGeneralOldestActiveJobIndex,
       "mltJmGeneralNewestActiveJobIndex": mltJmGeneralNewestActiveJobIndex,
       "mltJmGeneralJobPersistence": mltJmGeneralJobPersistence,
       "mltJmGeneralJobSetType": mltJmGeneralJobSetType,
       "mltJmJob": mltJmJob,
       "mltJmJobTable": mltJmJobTable,
       "mltJmJobEntry": mltJmJobEntry,
       "mltJmJobJobSetIndex": mltJmJobJobSetIndex,
       "mltJmJobIndex": mltJmJobIndex,
       "mltJmJobFunction": mltJmJobFunction,
       "mltJmJobStatus": mltJmJobStatus,
       "mltJmJobReceivedTime": mltJmJobReceivedTime,
       "mltJmJobCompleteTime": mltJmJobCompleteTime,
       "mltJmJobPriority": mltJmJobPriority,
       "mltJmJobDivNumber": mltJmJobDivNumber,
       "mltJmJobOwner": mltJmJobOwner,
       "mltJmJobType": mltJmJobType,
       "mltJmJobName": mltJmJobName,
       "mltJmJobDocPageNumbers": mltJmJobDocPageNumbers,
       "mltJmJobDocCopyNumbers": mltJmJobDocCopyNumbers,
       "mltJmJobPageSize": mltJmJobPageSize,
       "mltJmJobDestination": mltJmJobDestination,
       "mltJmJobDataSize": mltJmJobDataSize,
       "mltJmJobColorMode": mltJmJobColorMode,
       "mltJmJobFormat": mltJmJobFormat,
       "mltJmJobXResolution": mltJmJobXResolution,
       "mltJmJobYResolution": mltJmJobYResolution,
       "mltJmJobDuplex": mltJmJobDuplex,
       "mltJmJobOutputPages": mltJmJobOutputPages,
       "mltJmJobOutputSheets": mltJmJobOutputSheets,
       "mltJmJobMediaType": mltJmJobMediaType,
       "mltJmReport": mltJmReport,
       "mltJmReportTable": mltJmReportTable,
       "mltJmReportEntry": mltJmReportEntry,
       "mltJmReportIndex": mltJmReportIndex,
       "mltJmReportAddress": mltJmReportAddress,
       "mltJmKeepAliveCount": mltJmKeepAliveCount,
       "mltJmReportInterval": mltJmReportInterval,
       "mltJmReporIntervalSelection": mltJmReporIntervalSelection,
       "mltJmReportRequest": mltJmReportRequest,
       "mltDirectory": mltDirectory}
)
