# SNMP MIB module (IOMEGANAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IOMEGANAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:31 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lenovoemc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11369)
)
lenovoemc.setRevisions(
        ("2007-03-01 10:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_IomegaNAS_ObjectIdentity = ObjectIdentity
iomegaNAS = _IomegaNAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10)
)
_IomegaNASInfo_ObjectIdentity = ObjectIdentity
iomegaNASInfo = _IomegaNASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1)
)


class _DeviceDescr_Type(DisplayString):
    """Custom type deviceDescr based on DisplayString"""
    defaultValue = OctetString("Iomega NAS BOX")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceDescr_Type.__name__ = "DisplayString"
_DeviceDescr_Object = MibScalar
deviceDescr = _DeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 1),
    _DeviceDescr_Type()
)
deviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDescr.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_NetConfig_ObjectIdentity = ObjectIdentity
netConfig = _NetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 3)
)
_Dns0_Type = IpAddress
_Dns0_Object = MibScalar
dns0 = _Dns0_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 3, 1),
    _Dns0_Type()
)
dns0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns0.setStatus("current")
_Dns1_Type = IpAddress
_Dns1_Object = MibScalar
dns1 = _Dns1_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 3, 2),
    _Dns1_Type()
)
dns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns1.setStatus("current")
_Wins0_Type = IpAddress
_Wins0_Object = MibScalar
wins0 = _Wins0_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 3, 3),
    _Wins0_Type()
)
wins0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wins0.setStatus("current")
_Wins1_Type = IpAddress
_Wins1_Object = MibScalar
wins1 = _Wins1_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 1, 3, 4),
    _Wins1_Type()
)
wins1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wins1.setStatus("current")
_SystemPerformance_ObjectIdentity = ObjectIdentity
systemPerformance = _SystemPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2)
)
_IoTable_Object = MibTable
ioTable = _IoTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1)
)
if mibBuilder.loadTexts:
    ioTable.setStatus("current")
_IoEntry_Object = MibTableRow
ioEntry = _IoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1)
)
ioEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "ioIndex"),
)
if mibBuilder.loadTexts:
    ioEntry.setStatus("current")
_IoIndex_Type = Integer32
_IoIndex_Object = MibTableColumn
ioIndex = _IoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 1),
    _IoIndex_Type()
)
ioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioIndex.setStatus("current")
_DiskName_Type = OctetString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 2),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")
_IoMgrs_Type = OctetString
_IoMgrs_Object = MibTableColumn
ioMgrs = _IoMgrs_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 3),
    _IoMgrs_Type()
)
ioMgrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioMgrs.setStatus("current")
_IoMgws_Type = OctetString
_IoMgws_Object = MibTableColumn
ioMgws = _IoMgws_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 4),
    _IoMgws_Type()
)
ioMgws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioMgws.setStatus("current")
_IoReqrs_Type = OctetString
_IoReqrs_Object = MibTableColumn
ioReqrs = _IoReqrs_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 5),
    _IoReqrs_Type()
)
ioReqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReqrs.setStatus("current")
_IoReqws_Type = OctetString
_IoReqws_Object = MibTableColumn
ioReqws = _IoReqws_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 6),
    _IoReqws_Type()
)
ioReqws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReqws.setStatus("current")
_IoKbrs_Type = OctetString
_IoKbrs_Object = MibTableColumn
ioKbrs = _IoKbrs_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 7),
    _IoKbrs_Type()
)
ioKbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioKbrs.setStatus("current")
_IoKbws_Type = OctetString
_IoKbws_Object = MibTableColumn
ioKbws = _IoKbws_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 8),
    _IoKbws_Type()
)
ioKbws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioKbws.setStatus("current")
_IoAvgQueue_Type = OctetString
_IoAvgQueue_Object = MibTableColumn
ioAvgQueue = _IoAvgQueue_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 9),
    _IoAvgQueue_Type()
)
ioAvgQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioAvgQueue.setStatus("current")
_IoAvgWait_Type = OctetString
_IoAvgWait_Object = MibTableColumn
ioAvgWait = _IoAvgWait_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 10),
    _IoAvgWait_Type()
)
ioAvgWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioAvgWait.setStatus("current")
_IoAvgSvc_Type = OctetString
_IoAvgSvc_Object = MibTableColumn
ioAvgSvc = _IoAvgSvc_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 11),
    _IoAvgSvc_Type()
)
ioAvgSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioAvgSvc.setStatus("current")
_IoAvgUtil_Type = OctetString
_IoAvgUtil_Object = MibTableColumn
ioAvgUtil = _IoAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 12),
    _IoAvgUtil_Type()
)
ioAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioAvgUtil.setStatus("current")
_IoCpuTime_Type = OctetString
_IoCpuTime_Object = MibTableColumn
ioCpuTime = _IoCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 2, 1, 1, 13),
    _IoCpuTime_Type()
)
ioCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioCpuTime.setStatus("current")
_IomegaNASFunctionStatus_ObjectIdentity = ObjectIdentity
iomegaNASFunctionStatus = _IomegaNASFunctionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3)
)
_BkupTable_Object = MibTable
bkupTable = _BkupTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1)
)
if mibBuilder.loadTexts:
    bkupTable.setStatus("current")
_BkupEntry_Object = MibTableRow
bkupEntry = _BkupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1, 1)
)
bkupEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "bkupIndex"),
)
if mibBuilder.loadTexts:
    bkupEntry.setStatus("current")
_BkupIndex_Type = Integer32
_BkupIndex_Object = MibTableColumn
bkupIndex = _BkupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1, 1, 1),
    _BkupIndex_Type()
)
bkupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bkupIndex.setStatus("current")
_BkupClient_Type = OctetString
_BkupClient_Object = MibTableColumn
bkupClient = _BkupClient_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1, 1, 2),
    _BkupClient_Type()
)
bkupClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bkupClient.setStatus("current")
_BkupltStatus_Type = OctetString
_BkupltStatus_Object = MibTableColumn
bkupltStatus = _BkupltStatus_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1, 1, 3),
    _BkupltStatus_Type()
)
bkupltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bkupltStatus.setStatus("current")
_BkupTotalSpace_Type = OctetString
_BkupTotalSpace_Object = MibTableColumn
bkupTotalSpace = _BkupTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 1, 1, 4),
    _BkupTotalSpace_Type()
)
bkupTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bkupTotalSpace.setStatus("current")
_RemoteAccess_ObjectIdentity = ObjectIdentity
remoteAccess = _RemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 2)
)
_RaEnabled_Type = Integer32
_RaEnabled_Object = MibScalar
raEnabled = _RaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 2, 1),
    _RaEnabled_Type()
)
raEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raEnabled.setStatus("current")
_ConTable_Object = MibTable
conTable = _ConTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 3)
)
if mibBuilder.loadTexts:
    conTable.setStatus("current")
_ConEntry_Object = MibTableRow
conEntry = _ConEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 3, 1)
)
conEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "conIndex"),
)
if mibBuilder.loadTexts:
    conEntry.setStatus("current")


class _ConIndex_Type(Integer32):
    """Custom type conIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ConIndex_Type.__name__ = "Integer32"
_ConIndex_Object = MibTableColumn
conIndex = _ConIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 3, 1, 1),
    _ConIndex_Type()
)
conIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    conIndex.setStatus("current")


class _ConCount_Type(Integer32):
    """Custom type conCount based on Integer32"""
    defaultValue = 0


_ConCount_Object = MibTableColumn
conCount = _ConCount_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 3, 1, 2),
    _ConCount_Type()
)
conCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conCount.setStatus("current")
_ConProtocol_Type = DisplayString
_ConProtocol_Object = MibTableColumn
conProtocol = _ConProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 3, 1, 3),
    _ConProtocol_Type()
)
conProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conProtocol.setStatus("current")
_MediaService_ObjectIdentity = ObjectIdentity
mediaService = _MediaService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 4)
)
_MediaServiceEnabled_Type = Integer32
_MediaServiceEnabled_Object = MibScalar
mediaServiceEnabled = _MediaServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 3, 4, 1),
    _MediaServiceEnabled_Type()
)
mediaServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaServiceEnabled.setStatus("current")
_IomegaNASStorage_ObjectIdentity = ObjectIdentity
iomegaNASStorage = _IomegaNASStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4)
)
_RaidStatus_Type = OctetString
_RaidStatus_Object = MibScalar
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 1),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")


class _RaidLevel_Type(Integer32):
    """Custom type raidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_RaidLevel_Type.__name__ = "Integer32"
_RaidLevel_Object = MibScalar
raidLevel = _RaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 2),
    _RaidLevel_Type()
)
raidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidLevel.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3, 1)
)
diskEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskID_Type = OctetString
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("current")
_DiskSize_Type = OctetString
_DiskSize_Object = MibTableColumn
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3, 1, 3),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")
_DiskStatus_Type = OctetString
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 4, 3, 1, 4),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_IomegaNASDevice_ObjectIdentity = ObjectIdentity
iomegaNASDevice = _IomegaNASDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5)
)
_UsbTable_Object = MibTable
usbTable = _UsbTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1)
)
if mibBuilder.loadTexts:
    usbTable.setStatus("current")
_UsbEntry_Object = MibTableRow
usbEntry = _UsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1, 1)
)
usbEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "usbIndex"),
)
if mibBuilder.loadTexts:
    usbEntry.setStatus("current")
_UsbIndex_Type = Integer32
_UsbIndex_Object = MibTableColumn
usbIndex = _UsbIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1, 1, 1),
    _UsbIndex_Type()
)
usbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usbIndex.setStatus("current")


class _UsbManufacture_Type(DisplayString):
    """Custom type usbManufacture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsbManufacture_Type.__name__ = "DisplayString"
_UsbManufacture_Object = MibTableColumn
usbManufacture = _UsbManufacture_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1, 1, 2),
    _UsbManufacture_Type()
)
usbManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbManufacture.setStatus("current")


class _UsbModel_Type(DisplayString):
    """Custom type usbModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsbModel_Type.__name__ = "DisplayString"
_UsbModel_Object = MibTableColumn
usbModel = _UsbModel_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1, 1, 3),
    _UsbModel_Type()
)
usbModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbModel.setStatus("current")
_UsbType_Type = Integer32
_UsbType_Object = MibTableColumn
usbType = _UsbType_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 5, 1, 1, 4),
    _UsbType_Type()
)
usbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbType.setStatus("current")
_IomegaNASSensor_ObjectIdentity = ObjectIdentity
iomegaNASSensor = _IomegaNASSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6)
)
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 1)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 1, 1)
)
fanEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanIndex_Type = Integer32
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 1, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanName_Type = DisplayString
_FanName_Object = MibTableColumn
fanName = _FanName_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 1, 1, 2),
    _FanName_Type()
)
fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanName.setStatus("current")
_FanValue_Type = Gauge32
_FanValue_Object = MibTableColumn
fanValue = _FanValue_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 1, 1, 3),
    _FanValue_Type()
)
fanValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanValue.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 2, 1)
)
tempEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")
_TempIndex_Type = Integer32
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempName_Type = DisplayString
_TempName_Object = MibTableColumn
tempName = _TempName_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 2, 1, 2),
    _TempName_Type()
)
tempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempName.setStatus("current")
_TempValue_Type = Gauge32
_TempValue_Object = MibTableColumn
tempValue = _TempValue_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 2, 1, 3),
    _TempValue_Type()
)
tempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempValue.setStatus("current")
_VoltTable_Object = MibTable
voltTable = _VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 3)
)
if mibBuilder.loadTexts:
    voltTable.setStatus("current")
_VoltEntry_Object = MibTableRow
voltEntry = _VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 3, 1)
)
voltEntry.setIndexNames(
    (0, "IOMEGANAS-MIB", "voltIndex"),
)
if mibBuilder.loadTexts:
    voltEntry.setStatus("current")
_VoltIndex_Type = Integer32
_VoltIndex_Object = MibTableColumn
voltIndex = _VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 3, 1, 1),
    _VoltIndex_Type()
)
voltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voltIndex.setStatus("current")
_VoltName_Type = DisplayString
_VoltName_Object = MibTableColumn
voltName = _VoltName_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 3, 1, 2),
    _VoltName_Type()
)
voltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltName.setStatus("current")
_VoltValue_Type = Gauge32
_VoltValue_Object = MibTableColumn
voltValue = _VoltValue_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 6, 3, 1, 3),
    _VoltValue_Type()
)
voltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltValue.setStatus("current")
_IomegaNASEvent_ObjectIdentity = ObjectIdentity
iomegaNASEvent = _IomegaNASEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 7)
)
_EventID_Type = DisplayString
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 7, 1),
    _EventID_Type()
)
eventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventID.setStatus("current")
_EventText_Type = DisplayString
_EventText_Object = MibScalar
eventText = _EventText_Object(
    (1, 3, 6, 1, 4, 1, 11369, 10, 7, 2),
    _EventText_Type()
)
eventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventText.setStatus("current")
_IomegaNASNotifications_ObjectIdentity = ObjectIdentity
iomegaNASNotifications = _IomegaNASNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11369, 10, 8)
)

# Managed Objects groups


# Notification objects

iomegaNASNotificationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11369, 10, 8, 1)
)
iomegaNASNotificationError.setObjects(
      *(("IOMEGANAS-MIB", "deviceDescr"),
        ("IOMEGANAS-MIB", "deviceName"),
        ("IOMEGANAS-MIB", "eventID"),
        ("IOMEGANAS-MIB", "eventText"))
)
if mibBuilder.loadTexts:
    iomegaNASNotificationError.setStatus(
        "current"
    )

iomegaNASNotificationWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11369, 10, 8, 2)
)
iomegaNASNotificationWarn.setObjects(
      *(("IOMEGANAS-MIB", "deviceDescr"),
        ("IOMEGANAS-MIB", "deviceName"),
        ("IOMEGANAS-MIB", "eventID"),
        ("IOMEGANAS-MIB", "eventText"))
)
if mibBuilder.loadTexts:
    iomegaNASNotificationWarn.setStatus(
        "current"
    )

iomegaNASNotificationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 11369, 10, 8, 3)
)
iomegaNASNotificationInfo.setObjects(
      *(("IOMEGANAS-MIB", "deviceDescr"),
        ("IOMEGANAS-MIB", "deviceName"),
        ("IOMEGANAS-MIB", "eventID"),
        ("IOMEGANAS-MIB", "eventText"))
)
if mibBuilder.loadTexts:
    iomegaNASNotificationInfo.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IOMEGANAS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "lenovoemc": lenovoemc,
       "iomegaNAS": iomegaNAS,
       "iomegaNASInfo": iomegaNASInfo,
       "deviceDescr": deviceDescr,
       "deviceName": deviceName,
       "netConfig": netConfig,
       "dns0": dns0,
       "dns1": dns1,
       "wins0": wins0,
       "wins1": wins1,
       "systemPerformance": systemPerformance,
       "ioTable": ioTable,
       "ioEntry": ioEntry,
       "ioIndex": ioIndex,
       "diskName": diskName,
       "ioMgrs": ioMgrs,
       "ioMgws": ioMgws,
       "ioReqrs": ioReqrs,
       "ioReqws": ioReqws,
       "ioKbrs": ioKbrs,
       "ioKbws": ioKbws,
       "ioAvgQueue": ioAvgQueue,
       "ioAvgWait": ioAvgWait,
       "ioAvgSvc": ioAvgSvc,
       "ioAvgUtil": ioAvgUtil,
       "ioCpuTime": ioCpuTime,
       "iomegaNASFunctionStatus": iomegaNASFunctionStatus,
       "bkupTable": bkupTable,
       "bkupEntry": bkupEntry,
       "bkupIndex": bkupIndex,
       "bkupClient": bkupClient,
       "bkupltStatus": bkupltStatus,
       "bkupTotalSpace": bkupTotalSpace,
       "remoteAccess": remoteAccess,
       "raEnabled": raEnabled,
       "conTable": conTable,
       "conEntry": conEntry,
       "conIndex": conIndex,
       "conCount": conCount,
       "conProtocol": conProtocol,
       "mediaService": mediaService,
       "mediaServiceEnabled": mediaServiceEnabled,
       "iomegaNASStorage": iomegaNASStorage,
       "raidStatus": raidStatus,
       "raidLevel": raidLevel,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskID": diskID,
       "diskSize": diskSize,
       "diskStatus": diskStatus,
       "iomegaNASDevice": iomegaNASDevice,
       "usbTable": usbTable,
       "usbEntry": usbEntry,
       "usbIndex": usbIndex,
       "usbManufacture": usbManufacture,
       "usbModel": usbModel,
       "usbType": usbType,
       "iomegaNASSensor": iomegaNASSensor,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanName": fanName,
       "fanValue": fanValue,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempName": tempName,
       "tempValue": tempValue,
       "voltTable": voltTable,
       "voltEntry": voltEntry,
       "voltIndex": voltIndex,
       "voltName": voltName,
       "voltValue": voltValue,
       "iomegaNASEvent": iomegaNASEvent,
       "eventID": eventID,
       "eventText": eventText,
       "iomegaNASNotifications": iomegaNASNotifications,
       "iomegaNASNotificationError": iomegaNASNotificationError,
       "iomegaNASNotificationWarn": iomegaNASNotificationWarn,
       "iomegaNASNotificationInfo": iomegaNASNotificationInfo}
)
