# SNMP MIB module (CISCO-DMN-DSG-DL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-DL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:21 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGDl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1)
)
ciscoDSGDl.setRevisions(
        ("2010-10-13 08:00",
         "2010-08-30 11:00",
         "2010-05-25 08:00",
         "2010-02-12 15:00",
         "2009-12-20 15:00",
         "2009-11-22 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlAbout_ObjectIdentity = ObjectIdentity
dlAbout = _DlAbout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1)
)


class _DlAboutCurrentVer_Type(DisplayString):
    """Custom type dlAboutCurrentVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DlAboutCurrentVer_Type.__name__ = "DisplayString"
_DlAboutCurrentVer_Object = MibScalar
dlAboutCurrentVer = _DlAboutCurrentVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 1),
    _DlAboutCurrentVer_Type()
)
dlAboutCurrentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutCurrentVer.setStatus("current")


class _DlAboutSafeVer_Type(DisplayString):
    """Custom type dlAboutSafeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DlAboutSafeVer_Type.__name__ = "DisplayString"
_DlAboutSafeVer_Object = MibScalar
dlAboutSafeVer = _DlAboutSafeVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 2),
    _DlAboutSafeVer_Type()
)
dlAboutSafeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutSafeVer.setStatus("current")


class _DlAboutBootVer_Type(DisplayString):
    """Custom type dlAboutBootVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DlAboutBootVer_Type.__name__ = "DisplayString"
_DlAboutBootVer_Object = MibScalar
dlAboutBootVer = _DlAboutBootVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 3),
    _DlAboutBootVer_Type()
)
dlAboutBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutBootVer.setStatus("current")


class _DlAboutProductId_Type(DisplayString):
    """Custom type dlAboutProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DlAboutProductId_Type.__name__ = "DisplayString"
_DlAboutProductId_Object = MibScalar
dlAboutProductId = _DlAboutProductId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 4),
    _DlAboutProductId_Type()
)
dlAboutProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutProductId.setStatus("current")


class _DlAboutTrackingId_Type(DisplayString):
    """Custom type dlAboutTrackingId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlAboutTrackingId_Type.__name__ = "DisplayString"
_DlAboutTrackingId_Object = MibScalar
dlAboutTrackingId = _DlAboutTrackingId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 5),
    _DlAboutTrackingId_Type()
)
dlAboutTrackingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutTrackingId.setStatus("current")


class _DlAboutChangeApp_Type(Integer32):
    """Custom type dlAboutChangeApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DlAboutChangeApp_Type.__name__ = "Integer32"
_DlAboutChangeApp_Object = MibScalar
dlAboutChangeApp = _DlAboutChangeApp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 6),
    _DlAboutChangeApp_Type()
)
dlAboutChangeApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlAboutChangeApp.setStatus("current")


class _DlAboutEraseApp_Type(Integer32):
    """Custom type dlAboutEraseApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DlAboutEraseApp_Type.__name__ = "Integer32"
_DlAboutEraseApp_Object = MibScalar
dlAboutEraseApp = _DlAboutEraseApp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 7),
    _DlAboutEraseApp_Type()
)
dlAboutEraseApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlAboutEraseApp.setStatus("current")


class _DlAboutReboot_Type(Integer32):
    """Custom type dlAboutReboot based on Integer32"""
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


_DlAboutReboot_Type.__name__ = "Integer32"
_DlAboutReboot_Object = MibScalar
dlAboutReboot = _DlAboutReboot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 8),
    _DlAboutReboot_Type()
)
dlAboutReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlAboutReboot.setStatus("current")
_DlAboutAppTable_Object = MibTable
dlAboutAppTable = _DlAboutAppTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    dlAboutAppTable.setStatus("current")
_DlAboutAppEntry_Object = MibTableRow
dlAboutAppEntry = _DlAboutAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 9, 1)
)
dlAboutAppEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DL-MIB", "dlAboutAppIndex"),
)
if mibBuilder.loadTexts:
    dlAboutAppEntry.setStatus("current")


class _DlAboutAppIndex_Type(Integer32):
    """Custom type dlAboutAppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DlAboutAppIndex_Type.__name__ = "Integer32"
_DlAboutAppIndex_Object = MibTableColumn
dlAboutAppIndex = _DlAboutAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 9, 1, 1),
    _DlAboutAppIndex_Type()
)
dlAboutAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlAboutAppIndex.setStatus("current")


class _DlAboutAppString_Type(DisplayString):
    """Custom type dlAboutAppString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DlAboutAppString_Type.__name__ = "DisplayString"
_DlAboutAppString_Object = MibTableColumn
dlAboutAppString = _DlAboutAppString_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 1, 9, 1, 2),
    _DlAboutAppString_Type()
)
dlAboutAppString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlAboutAppString.setStatus("current")
_DlDownload_ObjectIdentity = ObjectIdentity
dlDownload = _DlDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2)
)
_DlDownloadTftpServerIP_Type = IpAddress
_DlDownloadTftpServerIP_Object = MibScalar
dlDownloadTftpServerIP = _DlDownloadTftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 1),
    _DlDownloadTftpServerIP_Type()
)
dlDownloadTftpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadTftpServerIP.setStatus("current")


class _DlDownloadMicroCode_Type(Integer32):
    """Custom type dlDownloadMicroCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlDownloadMicroCode_Type.__name__ = "Integer32"
_DlDownloadMicroCode_Object = MibScalar
dlDownloadMicroCode = _DlDownloadMicroCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 2),
    _DlDownloadMicroCode_Type()
)
dlDownloadMicroCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadMicroCode.setStatus("current")


class _DlDownloadCodeVersion_Type(Integer32):
    """Custom type dlDownloadCodeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlDownloadCodeVersion_Type.__name__ = "Integer32"
_DlDownloadCodeVersion_Object = MibScalar
dlDownloadCodeVersion = _DlDownloadCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 3),
    _DlDownloadCodeVersion_Type()
)
dlDownloadCodeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadCodeVersion.setStatus("current")


class _DlDownloadNanoVersion_Type(Integer32):
    """Custom type dlDownloadNanoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlDownloadNanoVersion_Type.__name__ = "Integer32"
_DlDownloadNanoVersion_Object = MibScalar
dlDownloadNanoVersion = _DlDownloadNanoVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 4),
    _DlDownloadNanoVersion_Type()
)
dlDownloadNanoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadNanoVersion.setStatus("current")


class _DlDownloadBankSelect_Type(Integer32):
    """Custom type dlDownloadBankSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlDownloadBankSelect_Type.__name__ = "Integer32"
_DlDownloadBankSelect_Object = MibScalar
dlDownloadBankSelect = _DlDownloadBankSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 5),
    _DlDownloadBankSelect_Type()
)
dlDownloadBankSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadBankSelect.setStatus("current")


class _DlDownloadForcedFlag_Type(Integer32):
    """Custom type dlDownloadForcedFlag based on Integer32"""
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


_DlDownloadForcedFlag_Type.__name__ = "Integer32"
_DlDownloadForcedFlag_Object = MibScalar
dlDownloadForcedFlag = _DlDownloadForcedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 6),
    _DlDownloadForcedFlag_Type()
)
dlDownloadForcedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadForcedFlag.setStatus("current")


class _DlDownloadTransitionBlocked_Type(Integer32):
    """Custom type dlDownloadTransitionBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlDownloadTransitionBlocked_Type.__name__ = "Integer32"
_DlDownloadTransitionBlocked_Object = MibScalar
dlDownloadTransitionBlocked = _DlDownloadTransitionBlocked_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 7),
    _DlDownloadTransitionBlocked_Type()
)
dlDownloadTransitionBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadTransitionBlocked.setStatus("current")


class _DlDownloadTftpFilename_Type(DisplayString):
    """Custom type dlDownloadTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlDownloadTftpFilename_Type.__name__ = "DisplayString"
_DlDownloadTftpFilename_Object = MibScalar
dlDownloadTftpFilename = _DlDownloadTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 8),
    _DlDownloadTftpFilename_Type()
)
dlDownloadTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadTftpFilename.setStatus("current")


class _DlDownloadAbort_Type(Integer32):
    """Custom type dlDownloadAbort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("no", 0))
    )


_DlDownloadAbort_Type.__name__ = "Integer32"
_DlDownloadAbort_Object = MibScalar
dlDownloadAbort = _DlDownloadAbort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 9),
    _DlDownloadAbort_Type()
)
dlDownloadAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadAbort.setStatus("current")


class _DlDownloadState_Type(Integer32):
    """Custom type dlDownloadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("idle", 0))
    )


_DlDownloadState_Type.__name__ = "Integer32"
_DlDownloadState_Object = MibScalar
dlDownloadState = _DlDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 10),
    _DlDownloadState_Type()
)
dlDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlDownloadState.setStatus("current")


class _DlDownloadErrorStatus_Type(Integer32):
    """Custom type dlDownloadErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fails", 2),
          ("ok", 0),
          ("reject", 1))
    )


_DlDownloadErrorStatus_Type.__name__ = "Integer32"
_DlDownloadErrorStatus_Object = MibScalar
dlDownloadErrorStatus = _DlDownloadErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 2, 11),
    _DlDownloadErrorStatus_Type()
)
dlDownloadErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlDownloadErrorStatus.setStatus("current")
_DlCfg_ObjectIdentity = ObjectIdentity
dlCfg = _DlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3)
)


class _DlStatus_Type(Integer32):
    """Custom type dlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("noTrigger", 1),
          ("trigger", 3))
    )


_DlStatus_Type.__name__ = "Integer32"
_DlStatus_Object = MibScalar
dlStatus = _DlStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 1),
    _DlStatus_Type()
)
dlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlStatus.setStatus("current")


class _DlMode_Type(Integer32):
    """Custom type dlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("never", 3),
          ("once", 2))
    )


_DlMode_Type.__name__ = "Integer32"
_DlMode_Object = MibScalar
dlMode = _DlMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 2),
    _DlMode_Type()
)
dlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlMode.setStatus("current")


class _DlType_Type(Integer32):
    """Custom type dlType based on Integer32"""
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
        *(("http", 3),
          ("none", 1),
          ("overAir", 4),
          ("rearPanel", 2))
    )


_DlType_Type.__name__ = "Integer32"
_DlType_Object = MibScalar
dlType = _DlType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 3),
    _DlType_Type()
)
dlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlType.setStatus("current")


class _DlBank_Type(Integer32):
    """Custom type dlBank based on Integer32"""
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
        *(("app5514", 1),
          ("app7109", 2),
          ("appPPC", 8),
          ("appVASA", 9),
          ("dbUpdate", 10),
          ("ethLogo", 7),
          ("execBin", 11),
          ("fpga7109", 3),
          ("menuLogo", 6),
          ("sat7109", 4),
          ("screenLogo", 5))
    )


_DlBank_Type.__name__ = "Integer32"
_DlBank_Object = MibScalar
dlBank = _DlBank_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 4),
    _DlBank_Type()
)
dlBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlBank.setStatus("current")


class _DlTotalCdt_Type(DisplayString):
    """Custom type dlTotalCdt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlTotalCdt_Type.__name__ = "DisplayString"
_DlTotalCdt_Object = MibScalar
dlTotalCdt = _DlTotalCdt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 5),
    _DlTotalCdt_Type()
)
dlTotalCdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlTotalCdt.setStatus("current")


class _DlReceived_Type(DisplayString):
    """Custom type dlReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlReceived_Type.__name__ = "DisplayString"
_DlReceived_Object = MibScalar
dlReceived = _DlReceived_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 6),
    _DlReceived_Type()
)
dlReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlReceived.setStatus("current")


class _DlRejected_Type(DisplayString):
    """Custom type dlRejected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlRejected_Type.__name__ = "DisplayString"
_DlRejected_Object = MibScalar
dlRejected = _DlRejected_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 7),
    _DlRejected_Type()
)
dlRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlRejected.setStatus("current")


class _DlCommand_Type(Integer32):
    """Custom type dlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("restart", 1),
          ("writeOnly", 3))
    )


_DlCommand_Type.__name__ = "Integer32"
_DlCommand_Object = MibScalar
dlCommand = _DlCommand_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 1, 3, 8),
    _DlCommand_Type()
)
dlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlCommand.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DL-MIB",
    **{"ciscoDSGDl": ciscoDSGDl,
       "dlAbout": dlAbout,
       "dlAboutCurrentVer": dlAboutCurrentVer,
       "dlAboutSafeVer": dlAboutSafeVer,
       "dlAboutBootVer": dlAboutBootVer,
       "dlAboutProductId": dlAboutProductId,
       "dlAboutTrackingId": dlAboutTrackingId,
       "dlAboutChangeApp": dlAboutChangeApp,
       "dlAboutEraseApp": dlAboutEraseApp,
       "dlAboutReboot": dlAboutReboot,
       "dlAboutAppTable": dlAboutAppTable,
       "dlAboutAppEntry": dlAboutAppEntry,
       "dlAboutAppIndex": dlAboutAppIndex,
       "dlAboutAppString": dlAboutAppString,
       "dlDownload": dlDownload,
       "dlDownloadTftpServerIP": dlDownloadTftpServerIP,
       "dlDownloadMicroCode": dlDownloadMicroCode,
       "dlDownloadCodeVersion": dlDownloadCodeVersion,
       "dlDownloadNanoVersion": dlDownloadNanoVersion,
       "dlDownloadBankSelect": dlDownloadBankSelect,
       "dlDownloadForcedFlag": dlDownloadForcedFlag,
       "dlDownloadTransitionBlocked": dlDownloadTransitionBlocked,
       "dlDownloadTftpFilename": dlDownloadTftpFilename,
       "dlDownloadAbort": dlDownloadAbort,
       "dlDownloadState": dlDownloadState,
       "dlDownloadErrorStatus": dlDownloadErrorStatus,
       "dlCfg": dlCfg,
       "dlStatus": dlStatus,
       "dlMode": dlMode,
       "dlType": dlType,
       "dlBank": dlBank,
       "dlTotalCdt": dlTotalCdt,
       "dlReceived": dlReceived,
       "dlRejected": dlRejected,
       "dlCommand": dlCommand}
)
