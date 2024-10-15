# SNMP MIB module (PACKETFRONT-DRG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETFRONT-DRG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:05 2024
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

(pfMgmt,) = mibBuilder.importSymbols(
    "PACKETFRONT-SMI",
    "pfMgmt")

(PortList,) = mibBuilder.importSymbols(
    "PACKETFRONT-TC",
    "PortList")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pfDrgMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3)
)
pfDrgMib.setRevisions(
        ("2009-03-23 15:38",
         "2008-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DrgNotification_ObjectIdentity = ObjectIdentity
drgNotification = _DrgNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 0)
)
_DrgConfig_ObjectIdentity = ObjectIdentity
drgConfig = _DrgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1)
)
_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1)
)


class _ProductName_Type(OctetString):
    """Custom type productName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProductName_Type.__name__ = "OctetString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _ProductSerialNo_Type(OctetString):
    """Custom type productSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ProductSerialNo_Type.__name__ = "OctetString"
_ProductSerialNo_Object = MibScalar
productSerialNo = _ProductSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 2),
    _ProductSerialNo_Type()
)
productSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNo.setStatus("current")


class _ProductProductionWeek_Type(OctetString):
    """Custom type productProductionWeek based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ProductProductionWeek_Type.__name__ = "OctetString"
_ProductProductionWeek_Object = MibScalar
productProductionWeek = _ProductProductionWeek_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 3),
    _ProductProductionWeek_Type()
)
productProductionWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productProductionWeek.setStatus("current")


class _ProductSwImageRev_Type(OctetString):
    """Custom type productSwImageRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductSwImageRev_Type.__name__ = "OctetString"
_ProductSwImageRev_Object = MibScalar
productSwImageRev = _ProductSwImageRev_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 4),
    _ProductSwImageRev_Type()
)
productSwImageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSwImageRev.setStatus("current")


class _ProductFwImageRev_Type(OctetString):
    """Custom type productFwImageRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductFwImageRev_Type.__name__ = "OctetString"
_ProductFwImageRev_Object = MibScalar
productFwImageRev = _ProductFwImageRev_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 5),
    _ProductFwImageRev_Type()
)
productFwImageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFwImageRev.setStatus("current")


class _ProductDefaultRevision_Type(OctetString):
    """Custom type productDefaultRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ProductDefaultRevision_Type.__name__ = "OctetString"
_ProductDefaultRevision_Object = MibScalar
productDefaultRevision = _ProductDefaultRevision_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 6),
    _ProductDefaultRevision_Type()
)
productDefaultRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDefaultRevision.setStatus("current")


class _ProductOpDefRev_Type(OctetString):
    """Custom type productOpDefRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductOpDefRev_Type.__name__ = "OctetString"
_ProductOpDefRev_Object = MibScalar
productOpDefRev = _ProductOpDefRev_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 7),
    _ProductOpDefRev_Type()
)
productOpDefRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productOpDefRev.setStatus("current")


class _ProductHardwareRev_Type(OctetString):
    """Custom type productHardwareRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductHardwareRev_Type.__name__ = "OctetString"
_ProductHardwareRev_Object = MibScalar
productHardwareRev = _ProductHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 8),
    _ProductHardwareRev_Type()
)
productHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardwareRev.setStatus("current")


class _ProductPlatform_Type(OctetString):
    """Custom type productPlatform based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProductPlatform_Type.__name__ = "OctetString"
_ProductPlatform_Object = MibScalar
productPlatform = _ProductPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 9),
    _ProductPlatform_Type()
)
productPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPlatform.setStatus("current")
_ProductHardwarePCBARevision_Type = Integer32
_ProductHardwarePCBARevision_Object = MibScalar
productHardwarePCBARevision = _ProductHardwarePCBARevision_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 10),
    _ProductHardwarePCBARevision_Type()
)
productHardwarePCBARevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardwarePCBARevision.setStatus("current")


class _ProductFunctionIdentity_Type(OctetString):
    """Custom type productFunctionIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductFunctionIdentity_Type.__name__ = "OctetString"
_ProductFunctionIdentity_Object = MibScalar
productFunctionIdentity = _ProductFunctionIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 11),
    _ProductFunctionIdentity_Type()
)
productFunctionIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFunctionIdentity.setStatus("current")
_ProductMacAddress_Type = MacAddress
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 12),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")


class _ProductIdentity_Type(OctetString):
    """Custom type productIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIdentity_Type.__name__ = "OctetString"
_ProductIdentity_Object = MibScalar
productIdentity = _ProductIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 1, 13),
    _ProductIdentity_Type()
)
productIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentity.setStatus("current")
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2)
)


class _SystemConfigRestartControl_Type(Integer32):
    """Custom type systemConfigRestartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restartNow", 2),
          ("running", 1))
    )


_SystemConfigRestartControl_Type.__name__ = "Integer32"
_SystemConfigRestartControl_Object = MibScalar
systemConfigRestartControl = _SystemConfigRestartControl_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2, 1),
    _SystemConfigRestartControl_Type()
)
systemConfigRestartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigRestartControl.setStatus("current")


class _SystemConfigRestartControlNotify_Type(Integer32):
    """Custom type systemConfigRestartControlNotify based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notifying", 2),
          ("silent", 1))
    )


_SystemConfigRestartControlNotify_Type.__name__ = "Integer32"
_SystemConfigRestartControlNotify_Object = MibScalar
systemConfigRestartControlNotify = _SystemConfigRestartControlNotify_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2, 2),
    _SystemConfigRestartControlNotify_Type()
)
systemConfigRestartControlNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigRestartControlNotify.setStatus("current")


class _SystemConfigSave_Type(Integer32):
    """Custom type systemConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changed", 2),
          ("notChanged", 3),
          ("save", 1))
    )


_SystemConfigSave_Type.__name__ = "Integer32"
_SystemConfigSave_Object = MibScalar
systemConfigSave = _SystemConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2, 3),
    _SystemConfigSave_Type()
)
systemConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigSave.setStatus("current")


class _SystemConfigFactoryReset_Type(Integer32):
    """Custom type systemConfigFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 2),
          ("running", 1))
    )


_SystemConfigFactoryReset_Type.__name__ = "Integer32"
_SystemConfigFactoryReset_Object = MibScalar
systemConfigFactoryReset = _SystemConfigFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2, 4),
    _SystemConfigFactoryReset_Type()
)
systemConfigFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigFactoryReset.setStatus("current")


class _SystemConfigSaveNotify_Type(Integer32):
    """Custom type systemConfigSaveNotify based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("onlyErrors", 3),
          ("silent", 1))
    )


_SystemConfigSaveNotify_Type.__name__ = "Integer32"
_SystemConfigSaveNotify_Object = MibScalar
systemConfigSaveNotify = _SystemConfigSaveNotify_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 2, 5),
    _SystemConfigSaveNotify_Type()
)
systemConfigSaveNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigSaveNotify.setStatus("current")
_DownloadConfig_ObjectIdentity = ObjectIdentity
downloadConfig = _DownloadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3)
)


class _DownloadServer_Type(OctetString):
    """Custom type downloadServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DownloadServer_Type.__name__ = "OctetString"
_DownloadServer_Object = MibScalar
downloadServer = _DownloadServer_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 1),
    _DownloadServer_Type()
)
downloadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadServer.setStatus("current")


class _DownloadFile_Type(OctetString):
    """Custom type downloadFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DownloadFile_Type.__name__ = "OctetString"
_DownloadFile_Object = MibScalar
downloadFile = _DownloadFile_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 2),
    _DownloadFile_Type()
)
downloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFile.setStatus("current")


class _DownloadAction_Type(Integer32):
    """Custom type downloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDownloading", 1),
          ("startDownload", 2))
    )


_DownloadAction_Type.__name__ = "Integer32"
_DownloadAction_Object = MibScalar
downloadAction = _DownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 3),
    _DownloadAction_Type()
)
downloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadAction.setStatus("current")


class _DownloadMethod_Type(Integer32):
    """Custom type downloadMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("http", 2),
          ("tftp", 1))
    )


_DownloadMethod_Type.__name__ = "Integer32"
_DownloadMethod_Object = MibScalar
downloadMethod = _DownloadMethod_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 4),
    _DownloadMethod_Type()
)
downloadMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadMethod.setStatus("current")


class _DownloadRetryCount_Type(Integer32):
    """Custom type downloadRetryCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DownloadRetryCount_Type.__name__ = "Integer32"
_DownloadRetryCount_Object = MibScalar
downloadRetryCount = _DownloadRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 5),
    _DownloadRetryCount_Type()
)
downloadRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadRetryCount.setStatus("current")


class _DownloadResultCode_Type(Integer32):
    """Custom type downloadResultCode based on Integer32"""
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
        *(("failureFileIncompatible", 7),
          ("failureFileIncorrectSize", 5),
          ("failureFileNotFound", 4),
          ("failureFileVerifyFailure", 6),
          ("failureHostNotFound", 3),
          ("failureUnknownError", 8),
          ("inProgress", 1),
          ("none", 0),
          ("success", 2))
    )


_DownloadResultCode_Type.__name__ = "Integer32"
_DownloadResultCode_Object = MibScalar
downloadResultCode = _DownloadResultCode_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 6),
    _DownloadResultCode_Type()
)
downloadResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadResultCode.setStatus("current")


class _DownloadResultNotify_Type(Integer32):
    """Custom type downloadResultNotify based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("onError", 3),
          ("silent", 1))
    )


_DownloadResultNotify_Type.__name__ = "Integer32"
_DownloadResultNotify_Object = MibScalar
downloadResultNotify = _DownloadResultNotify_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 3, 7),
    _DownloadResultNotify_Type()
)
downloadResultNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadResultNotify.setStatus("current")
_HostConfig_ObjectIdentity = ObjectIdentity
hostConfig = _HostConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4)
)
_HostIfMax_Type = Integer32
_HostIfMax_Object = MibScalar
hostIfMax = _HostIfMax_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 1),
    _HostIfMax_Type()
)
hostIfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfMax.setStatus("current")
_HostIfDefined_Type = Integer32
_HostIfDefined_Object = MibScalar
hostIfDefined = _HostIfDefined_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 2),
    _HostIfDefined_Type()
)
hostIfDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfDefined.setStatus("current")
_HostIfTable_Object = MibTable
hostIfTable = _HostIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hostIfTable.setStatus("current")
_HostIfEntry_Object = MibTableRow
hostIfEntry = _HostIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1)
)
hostIfEntry.setIndexNames(
    (0, "PACKETFRONT-DRG-MIB", "hostIfIndex"),
)
if mibBuilder.loadTexts:
    hostIfEntry.setStatus("current")


class _HostIfIndex_Type(Integer32):
    """Custom type hostIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HostIfIndex_Type.__name__ = "Integer32"
_HostIfIndex_Object = MibTableColumn
hostIfIndex = _HostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 1),
    _HostIfIndex_Type()
)
hostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfIndex.setStatus("current")


class _HostIfMode_Type(Integer32):
    """Custom type hostIfMode based on Integer32"""
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
        *(("dhcp", 1),
          ("pppoe", 3),
          ("pppoeFixed", 4),
          ("static", 2))
    )


_HostIfMode_Type.__name__ = "Integer32"
_HostIfMode_Object = MibTableColumn
hostIfMode = _HostIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 2),
    _HostIfMode_Type()
)
hostIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfMode.setStatus("current")


class _HostIfHostName_Type(OctetString):
    """Custom type hostIfHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostIfHostName_Type.__name__ = "OctetString"
_HostIfHostName_Object = MibTableColumn
hostIfHostName = _HostIfHostName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 3),
    _HostIfHostName_Type()
)
hostIfHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfHostName.setStatus("current")
_HostIfAddress_Type = IpAddress
_HostIfAddress_Object = MibTableColumn
hostIfAddress = _HostIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 4),
    _HostIfAddress_Type()
)
hostIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostIfAddress.setStatus("current")
_HostIfSubnetMask_Type = IpAddress
_HostIfSubnetMask_Object = MibTableColumn
hostIfSubnetMask = _HostIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 5),
    _HostIfSubnetMask_Type()
)
hostIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfSubnetMask.setStatus("current")
_HostIfDefaultRouter_Type = IpAddress
_HostIfDefaultRouter_Object = MibTableColumn
hostIfDefaultRouter = _HostIfDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 6),
    _HostIfDefaultRouter_Type()
)
hostIfDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDefaultRouter.setStatus("current")


class _HostIfDomainName_Type(OctetString):
    """Custom type hostIfDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostIfDomainName_Type.__name__ = "OctetString"
_HostIfDomainName_Object = MibTableColumn
hostIfDomainName = _HostIfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 7),
    _HostIfDomainName_Type()
)
hostIfDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDomainName.setStatus("current")
_HostIfDnsServer1_Type = IpAddress
_HostIfDnsServer1_Object = MibTableColumn
hostIfDnsServer1 = _HostIfDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 8),
    _HostIfDnsServer1_Type()
)
hostIfDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDnsServer1.setStatus("current")
_HostIfDnsServer2_Type = IpAddress
_HostIfDnsServer2_Object = MibTableColumn
hostIfDnsServer2 = _HostIfDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 9),
    _HostIfDnsServer2_Type()
)
hostIfDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDnsServer2.setStatus("current")


class _HostIfDhcpClientID_Type(OctetString):
    """Custom type hostIfDhcpClientID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostIfDhcpClientID_Type.__name__ = "OctetString"
_HostIfDhcpClientID_Object = MibTableColumn
hostIfDhcpClientID = _HostIfDhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 10),
    _HostIfDhcpClientID_Type()
)
hostIfDhcpClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDhcpClientID.setStatus("current")


class _HostIfDhcpVendorClassID_Type(OctetString):
    """Custom type hostIfDhcpVendorClassID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HostIfDhcpVendorClassID_Type.__name__ = "OctetString"
_HostIfDhcpVendorClassID_Object = MibTableColumn
hostIfDhcpVendorClassID = _HostIfDhcpVendorClassID_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 11),
    _HostIfDhcpVendorClassID_Type()
)
hostIfDhcpVendorClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDhcpVendorClassID.setStatus("current")


class _HostIfDiffservCodePoint_Type(Integer32):
    """Custom type hostIfDiffservCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HostIfDiffservCodePoint_Type.__name__ = "Integer32"
_HostIfDiffservCodePoint_Object = MibTableColumn
hostIfDiffservCodePoint = _HostIfDiffservCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 12),
    _HostIfDiffservCodePoint_Type()
)
hostIfDiffservCodePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfDiffservCodePoint.setStatus("current")


class _HostIfVlan_Type(Integer32):
    """Custom type hostIfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HostIfVlan_Type.__name__ = "Integer32"
_HostIfVlan_Object = MibTableColumn
hostIfVlan = _HostIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 13),
    _HostIfVlan_Type()
)
hostIfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfVlan.setStatus("current")


class _HostIfVlanPriority_Type(Integer32):
    """Custom type hostIfVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HostIfVlanPriority_Type.__name__ = "Integer32"
_HostIfVlanPriority_Object = MibTableColumn
hostIfVlanPriority = _HostIfVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 14),
    _HostIfVlanPriority_Type()
)
hostIfVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfVlanPriority.setStatus("current")


class _HostIfSecurePing_Type(Integer32):
    """Custom type hostIfSecurePing based on Integer32"""
    defaultValue = 2

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


_HostIfSecurePing_Type.__name__ = "Integer32"
_HostIfSecurePing_Object = MibTableColumn
hostIfSecurePing = _HostIfSecurePing_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 4, 3, 1, 15),
    _HostIfSecurePing_Type()
)
hostIfSecurePing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIfSecurePing.setStatus("current")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7)
)
_SnmpTrapDestHostsMax_Type = Integer32
_SnmpTrapDestHostsMax_Object = MibScalar
snmpTrapDestHostsMax = _SnmpTrapDestHostsMax_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 1),
    _SnmpTrapDestHostsMax_Type()
)
snmpTrapDestHostsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestHostsMax.setStatus("current")
_SnmpTrapDestHostsDefined_Type = Integer32
_SnmpTrapDestHostsDefined_Object = MibScalar
snmpTrapDestHostsDefined = _SnmpTrapDestHostsDefined_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 2),
    _SnmpTrapDestHostsDefined_Type()
)
snmpTrapDestHostsDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestHostsDefined.setStatus("current")
_SnmpTrapDestinationTable_Object = MibTable
snmpTrapDestinationTable = _SnmpTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3)
)
if mibBuilder.loadTexts:
    snmpTrapDestinationTable.setStatus("current")
_SnmpTrapDestinationEntry_Object = MibTableRow
snmpTrapDestinationEntry = _SnmpTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1)
)
snmpTrapDestinationEntry.setIndexNames(
    (0, "PACKETFRONT-DRG-MIB", "snmpTrapDestIndex"),
    (0, "PACKETFRONT-DRG-MIB", "snmpTrapDestName"),
)
if mibBuilder.loadTexts:
    snmpTrapDestinationEntry.setStatus("current")


class _SnmpTrapDestIndex_Type(Integer32):
    """Custom type snmpTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SnmpTrapDestIndex_Type.__name__ = "Integer32"
_SnmpTrapDestIndex_Object = MibTableColumn
snmpTrapDestIndex = _SnmpTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1, 1),
    _SnmpTrapDestIndex_Type()
)
snmpTrapDestIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestIndex.setStatus("current")


class _SnmpTrapDestName_Type(OctetString):
    """Custom type snmpTrapDestName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpTrapDestName_Type.__name__ = "OctetString"
_SnmpTrapDestName_Object = MibTableColumn
snmpTrapDestName = _SnmpTrapDestName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1, 2),
    _SnmpTrapDestName_Type()
)
snmpTrapDestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestName.setStatus("current")
_SnmpTrapDestAddress_Type = IpAddress
_SnmpTrapDestAddress_Object = MibTableColumn
snmpTrapDestAddress = _SnmpTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1, 3),
    _SnmpTrapDestAddress_Type()
)
snmpTrapDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestAddress.setStatus("current")


class _SnmpTrapDestTagList_Type(OctetString):
    """Custom type snmpTrapDestTagList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpTrapDestTagList_Type.__name__ = "OctetString"
_SnmpTrapDestTagList_Object = MibTableColumn
snmpTrapDestTagList = _SnmpTrapDestTagList_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1, 4),
    _SnmpTrapDestTagList_Type()
)
snmpTrapDestTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestTagList.setStatus("current")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 3, 1, 5),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("current")


class _SnmpReadCommunityName_Type(OctetString):
    """Custom type snmpReadCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpReadCommunityName_Type.__name__ = "OctetString"
_SnmpReadCommunityName_Object = MibScalar
snmpReadCommunityName = _SnmpReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 4),
    _SnmpReadCommunityName_Type()
)
snmpReadCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunityName.setStatus("current")


class _SnmpWriteCommunityName_Type(OctetString):
    """Custom type snmpWriteCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpWriteCommunityName_Type.__name__ = "OctetString"
_SnmpWriteCommunityName_Object = MibScalar
snmpWriteCommunityName = _SnmpWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 5),
    _SnmpWriteCommunityName_Type()
)
snmpWriteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunityName.setStatus("current")


class _SnmpTrapCommunityName_Type(OctetString):
    """Custom type snmpTrapCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpTrapCommunityName_Type.__name__ = "OctetString"
_SnmpTrapCommunityName_Object = MibScalar
snmpTrapCommunityName = _SnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 6),
    _SnmpTrapCommunityName_Type()
)
snmpTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunityName.setStatus("current")


class _SnmpDiffservCodePoint_Type(Integer32):
    """Custom type snmpDiffservCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SnmpDiffservCodePoint_Type.__name__ = "Integer32"
_SnmpDiffservCodePoint_Object = MibScalar
snmpDiffservCodePoint = _SnmpDiffservCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 7),
    _SnmpDiffservCodePoint_Type()
)
snmpDiffservCodePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDiffservCodePoint.setStatus("current")


class _SnmpAtomicSet_Type(Integer32):
    """Custom type snmpAtomicSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 3),
          ("idle", 1),
          ("stage", 2))
    )


_SnmpAtomicSet_Type.__name__ = "Integer32"
_SnmpAtomicSet_Object = MibScalar
snmpAtomicSet = _SnmpAtomicSet_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 7, 8),
    _SnmpAtomicSet_Type()
)
snmpAtomicSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtomicSet.setStatus("current")
_VlanConfig_ObjectIdentity = ObjectIdentity
vlanConfig = _VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8)
)
_VlanBase_ObjectIdentity = ObjectIdentity
vlanBase = _VlanBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 1)
)


class _VlanVersionNumber_Type(Integer32):
    """Custom type vlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_VlanVersionNumber_Type.__name__ = "Integer32"
_VlanVersionNumber_Object = MibScalar
vlanVersionNumber = _VlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 1, 1),
    _VlanVersionNumber_Type()
)
vlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVersionNumber.setStatus("current")


class _VlanMaxVlanId_Type(Integer32):
    """Custom type vlanMaxVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanMaxVlanId_Type.__name__ = "Integer32"
_VlanMaxVlanId_Object = MibScalar
vlanMaxVlanId = _VlanMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 1, 2),
    _VlanMaxVlanId_Type()
)
vlanMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxVlanId.setStatus("current")
_VlanMaxSupportedVlans_Type = Unsigned32
_VlanMaxSupportedVlans_Object = MibScalar
vlanMaxSupportedVlans = _VlanMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 1, 3),
    _VlanMaxSupportedVlans_Type()
)
vlanMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxSupportedVlans.setStatus("current")
_VlanNumVlans_Type = Unsigned32
_VlanNumVlans_Object = MibScalar
vlanNumVlans = _VlanNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 1, 4),
    _VlanNumVlans_Type()
)
vlanNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNumVlans.setStatus("current")
_VlanTp_ObjectIdentity = ObjectIdentity
vlanTp = _VlanTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2)
)
_VlanFdbTable_Object = MibTable
vlanFdbTable = _VlanFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vlanFdbTable.setStatus("current")
_VlanFdbEntry_Object = MibTableRow
vlanFdbEntry = _VlanFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 1, 1)
)
vlanFdbEntry.setIndexNames(
    (0, "PACKETFRONT-DRG-MIB", "vlanFdbId"),
)
if mibBuilder.loadTexts:
    vlanFdbEntry.setStatus("current")
_VlanFdbId_Type = Unsigned32
_VlanFdbId_Object = MibTableColumn
vlanFdbId = _VlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 1, 1, 1),
    _VlanFdbId_Type()
)
vlanFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanFdbId.setStatus("current")
_VlanFdbDynamicCount_Type = Counter32
_VlanFdbDynamicCount_Object = MibTableColumn
vlanFdbDynamicCount = _VlanFdbDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 1, 1, 2),
    _VlanFdbDynamicCount_Type()
)
vlanFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanFdbDynamicCount.setStatus("current")
_VlanTpFdbTable_Object = MibTable
vlanTpFdbTable = _VlanTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    vlanTpFdbTable.setStatus("current")
_VlanTpFdbEntry_Object = MibTableRow
vlanTpFdbEntry = _VlanTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 2, 1)
)
vlanTpFdbEntry.setIndexNames(
    (0, "PACKETFRONT-DRG-MIB", "vlanFdbId"),
    (0, "PACKETFRONT-DRG-MIB", "vlanTpFdbAddress"),
)
if mibBuilder.loadTexts:
    vlanTpFdbEntry.setStatus("current")
_VlanTpFdbAddress_Type = MacAddress
_VlanTpFdbAddress_Object = MibTableColumn
vlanTpFdbAddress = _VlanTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 2, 1, 1),
    _VlanTpFdbAddress_Type()
)
vlanTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanTpFdbAddress.setStatus("current")


class _VlanTpFdbPort_Type(Integer32):
    """Custom type vlanTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanTpFdbPort_Type.__name__ = "Integer32"
_VlanTpFdbPort_Object = MibTableColumn
vlanTpFdbPort = _VlanTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 2, 1, 2),
    _VlanTpFdbPort_Type()
)
vlanTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTpFdbPort.setStatus("current")


class _VlanTpFdbStatus_Type(Integer32):
    """Custom type vlanTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_VlanTpFdbStatus_Type.__name__ = "Integer32"
_VlanTpFdbStatus_Object = MibTableColumn
vlanTpFdbStatus = _VlanTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 2, 2, 1, 3),
    _VlanTpFdbStatus_Type()
)
vlanTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTpFdbStatus.setStatus("current")
_VlanStatic_ObjectIdentity = ObjectIdentity
vlanStatic = _VlanStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3)
)
_VlanStaticTable_Object = MibTable
vlanStaticTable = _VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vlanStaticTable.setStatus("current")
_VlanStaticEntry_Object = MibTableRow
vlanStaticEntry = _VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1)
)
vlanStaticEntry.setIndexNames(
    (0, "PACKETFRONT-DRG-MIB", "vlanStaticIndex"),
)
if mibBuilder.loadTexts:
    vlanStaticEntry.setStatus("current")


class _VlanStaticIndex_Type(Integer32):
    """Custom type vlanStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VlanStaticIndex_Type.__name__ = "Integer32"
_VlanStaticIndex_Object = MibTableColumn
vlanStaticIndex = _VlanStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 1),
    _VlanStaticIndex_Type()
)
vlanStaticIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStaticIndex.setStatus("current")


class _VlanStaticName_Type(OctetString):
    """Custom type vlanStaticName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanStaticName_Type.__name__ = "OctetString"
_VlanStaticName_Object = MibTableColumn
vlanStaticName = _VlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 2),
    _VlanStaticName_Type()
)
vlanStaticName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticName.setStatus("current")


class _VlanStaticVlanId_Type(Integer32):
    """Custom type vlanStaticVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanStaticVlanId_Type.__name__ = "Integer32"
_VlanStaticVlanId_Object = MibTableColumn
vlanStaticVlanId = _VlanStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 3),
    _VlanStaticVlanId_Type()
)
vlanStaticVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticVlanId.setStatus("current")


class _VlanStaticPriority_Type(Integer32):
    """Custom type vlanStaticPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanStaticPriority_Type.__name__ = "Integer32"
_VlanStaticPriority_Object = MibTableColumn
vlanStaticPriority = _VlanStaticPriority_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 4),
    _VlanStaticPriority_Type()
)
vlanStaticPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticPriority.setStatus("current")
_VlanStaticEgressPorts_Type = PortList
_VlanStaticEgressPorts_Object = MibTableColumn
vlanStaticEgressPorts = _VlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 5),
    _VlanStaticEgressPorts_Type()
)
vlanStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticEgressPorts.setStatus("current")
_VlanStaticUntaggedPorts_Type = PortList
_VlanStaticUntaggedPorts_Object = MibTableColumn
vlanStaticUntaggedPorts = _VlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 6),
    _VlanStaticUntaggedPorts_Type()
)
vlanStaticUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticUntaggedPorts.setStatus("current")
_VlanStaticUnmodifiedPorts_Type = PortList
_VlanStaticUnmodifiedPorts_Object = MibTableColumn
vlanStaticUnmodifiedPorts = _VlanStaticUnmodifiedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 7),
    _VlanStaticUnmodifiedPorts_Type()
)
vlanStaticUnmodifiedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStaticUnmodifiedPorts.setStatus("current")
_VlanStaticRowStatus_Type = RowStatus
_VlanStaticRowStatus_Object = MibTableColumn
vlanStaticRowStatus = _VlanStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 1, 8, 3, 1, 1, 8),
    _VlanStaticRowStatus_Type()
)
vlanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStaticRowStatus.setStatus("current")
_DrgConformance_ObjectIdentity = ObjectIdentity
drgConformance = _DrgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 2)
)
_DrgGroups_ObjectIdentity = ObjectIdentity
drgGroups = _DrgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 2, 1)
)
_DrgCompliance_ObjectIdentity = ObjectIdentity
drgCompliance = _DrgCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 2, 2)
)
_DrgCompatibility_ObjectIdentity = ObjectIdentity
drgCompatibility = _DrgCompatibility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 2, 3)
)

# Managed Objects groups


# Notification objects

notifyRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 0, 1)
)
notifyRestart.setObjects(
      *(("PACKETFRONT-DRG-MIB", "productMacAddress"),
        ("PACKETFRONT-DRG-MIB", "productIdentity"),
        ("PACKETFRONT-DRG-MIB", "productSwImageRev"),
        ("PACKETFRONT-DRG-MIB", "productHardwareRev"),
        ("PACKETFRONT-DRG-MIB", "productOpDefRev"),
        ("PACKETFRONT-DRG-MIB", "productFunctionIdentity"))
)
if mibBuilder.loadTexts:
    notifyRestart.setStatus(
        "current"
    )

notifyDownloadResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 0, 2)
)
notifyDownloadResult.setObjects(
      *(("PACKETFRONT-DRG-MIB", "productMacAddress"),
        ("PACKETFRONT-DRG-MIB", "productIdentity"),
        ("PACKETFRONT-DRG-MIB", "downloadResultCode"))
)
if mibBuilder.loadTexts:
    notifyDownloadResult.setStatus(
        "current"
    )

notifyConfigSaveResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 3, 0, 3)
)
notifyConfigSaveResult.setObjects(
      *(("PACKETFRONT-DRG-MIB", "productMacAddress"),
        ("PACKETFRONT-DRG-MIB", "productIdentity"),
        ("PACKETFRONT-DRG-MIB", "downloadResultCode"))
)
if mibBuilder.loadTexts:
    notifyConfigSaveResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFRONT-DRG-MIB",
    **{"pfDrgMib": pfDrgMib,
       "drgNotification": drgNotification,
       "notifyRestart": notifyRestart,
       "notifyDownloadResult": notifyDownloadResult,
       "notifyConfigSaveResult": notifyConfigSaveResult,
       "drgConfig": drgConfig,
       "productInfo": productInfo,
       "productName": productName,
       "productSerialNo": productSerialNo,
       "productProductionWeek": productProductionWeek,
       "productSwImageRev": productSwImageRev,
       "productFwImageRev": productFwImageRev,
       "productDefaultRevision": productDefaultRevision,
       "productOpDefRev": productOpDefRev,
       "productHardwareRev": productHardwareRev,
       "productPlatform": productPlatform,
       "productHardwarePCBARevision": productHardwarePCBARevision,
       "productFunctionIdentity": productFunctionIdentity,
       "productMacAddress": productMacAddress,
       "productIdentity": productIdentity,
       "systemConfig": systemConfig,
       "systemConfigRestartControl": systemConfigRestartControl,
       "systemConfigRestartControlNotify": systemConfigRestartControlNotify,
       "systemConfigSave": systemConfigSave,
       "systemConfigFactoryReset": systemConfigFactoryReset,
       "systemConfigSaveNotify": systemConfigSaveNotify,
       "downloadConfig": downloadConfig,
       "downloadServer": downloadServer,
       "downloadFile": downloadFile,
       "downloadAction": downloadAction,
       "downloadMethod": downloadMethod,
       "downloadRetryCount": downloadRetryCount,
       "downloadResultCode": downloadResultCode,
       "downloadResultNotify": downloadResultNotify,
       "hostConfig": hostConfig,
       "hostIfMax": hostIfMax,
       "hostIfDefined": hostIfDefined,
       "hostIfTable": hostIfTable,
       "hostIfEntry": hostIfEntry,
       "hostIfIndex": hostIfIndex,
       "hostIfMode": hostIfMode,
       "hostIfHostName": hostIfHostName,
       "hostIfAddress": hostIfAddress,
       "hostIfSubnetMask": hostIfSubnetMask,
       "hostIfDefaultRouter": hostIfDefaultRouter,
       "hostIfDomainName": hostIfDomainName,
       "hostIfDnsServer1": hostIfDnsServer1,
       "hostIfDnsServer2": hostIfDnsServer2,
       "hostIfDhcpClientID": hostIfDhcpClientID,
       "hostIfDhcpVendorClassID": hostIfDhcpVendorClassID,
       "hostIfDiffservCodePoint": hostIfDiffservCodePoint,
       "hostIfVlan": hostIfVlan,
       "hostIfVlanPriority": hostIfVlanPriority,
       "hostIfSecurePing": hostIfSecurePing,
       "snmpConfig": snmpConfig,
       "snmpTrapDestHostsMax": snmpTrapDestHostsMax,
       "snmpTrapDestHostsDefined": snmpTrapDestHostsDefined,
       "snmpTrapDestinationTable": snmpTrapDestinationTable,
       "snmpTrapDestinationEntry": snmpTrapDestinationEntry,
       "snmpTrapDestIndex": snmpTrapDestIndex,
       "snmpTrapDestName": snmpTrapDestName,
       "snmpTrapDestAddress": snmpTrapDestAddress,
       "snmpTrapDestTagList": snmpTrapDestTagList,
       "snmpTrapDestRowStatus": snmpTrapDestRowStatus,
       "snmpReadCommunityName": snmpReadCommunityName,
       "snmpWriteCommunityName": snmpWriteCommunityName,
       "snmpTrapCommunityName": snmpTrapCommunityName,
       "snmpDiffservCodePoint": snmpDiffservCodePoint,
       "snmpAtomicSet": snmpAtomicSet,
       "vlanConfig": vlanConfig,
       "vlanBase": vlanBase,
       "vlanVersionNumber": vlanVersionNumber,
       "vlanMaxVlanId": vlanMaxVlanId,
       "vlanMaxSupportedVlans": vlanMaxSupportedVlans,
       "vlanNumVlans": vlanNumVlans,
       "vlanTp": vlanTp,
       "vlanFdbTable": vlanFdbTable,
       "vlanFdbEntry": vlanFdbEntry,
       "vlanFdbId": vlanFdbId,
       "vlanFdbDynamicCount": vlanFdbDynamicCount,
       "vlanTpFdbTable": vlanTpFdbTable,
       "vlanTpFdbEntry": vlanTpFdbEntry,
       "vlanTpFdbAddress": vlanTpFdbAddress,
       "vlanTpFdbPort": vlanTpFdbPort,
       "vlanTpFdbStatus": vlanTpFdbStatus,
       "vlanStatic": vlanStatic,
       "vlanStaticTable": vlanStaticTable,
       "vlanStaticEntry": vlanStaticEntry,
       "vlanStaticIndex": vlanStaticIndex,
       "vlanStaticName": vlanStaticName,
       "vlanStaticVlanId": vlanStaticVlanId,
       "vlanStaticPriority": vlanStaticPriority,
       "vlanStaticEgressPorts": vlanStaticEgressPorts,
       "vlanStaticUntaggedPorts": vlanStaticUntaggedPorts,
       "vlanStaticUnmodifiedPorts": vlanStaticUnmodifiedPorts,
       "vlanStaticRowStatus": vlanStaticRowStatus,
       "drgConformance": drgConformance,
       "drgGroups": drgGroups,
       "drgCompliance": drgCompliance,
       "drgCompatibility": drgCompatibility}
)
