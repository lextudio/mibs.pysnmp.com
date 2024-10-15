# SNMP MIB module (WDMYCLOUDEX4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WDMYCLOUDEX4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:42 2024
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

_Wd_ObjectIdentity = ObjectIdentity
wd = _Wd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1)
)
_ProjectID_ObjectIdentity = ObjectIdentity
projectID = _ProjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1)
)
_ModelID_ObjectIdentity = ObjectIdentity
modelID = _ModelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1)
)
_SubmodelID_ObjectIdentity = ObjectIdentity
submodelID = _SubmodelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1)
)
_NasAgent_ObjectIdentity = ObjectIdentity
nasAgent = _NasAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1)
)
_Wdmycloudex4AgentVer_Type = DisplayString
_Wdmycloudex4AgentVer_Object = MibScalar
wdmycloudex4AgentVer = _Wdmycloudex4AgentVer_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 1),
    _Wdmycloudex4AgentVer_Type()
)
wdmycloudex4AgentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4AgentVer.setStatus("current")
_Wdmycloudex4SoftwareVersion_Type = DisplayString
_Wdmycloudex4SoftwareVersion_Object = MibScalar
wdmycloudex4SoftwareVersion = _Wdmycloudex4SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 2),
    _Wdmycloudex4SoftwareVersion_Type()
)
wdmycloudex4SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4SoftwareVersion.setStatus("current")
_Wdmycloudex4HostName_Type = DisplayString
_Wdmycloudex4HostName_Object = MibScalar
wdmycloudex4HostName = _Wdmycloudex4HostName_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 3),
    _Wdmycloudex4HostName_Type()
)
wdmycloudex4HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4HostName.setStatus("current")
_Wdmycloudex4FTPServer_Type = DisplayString
_Wdmycloudex4FTPServer_Object = MibScalar
wdmycloudex4FTPServer = _Wdmycloudex4FTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 5),
    _Wdmycloudex4FTPServer_Type()
)
wdmycloudex4FTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4FTPServer.setStatus("current")
_Wdmycloudex4NetType_Type = DisplayString
_Wdmycloudex4NetType_Object = MibScalar
wdmycloudex4NetType = _Wdmycloudex4NetType_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 6),
    _Wdmycloudex4NetType_Type()
)
wdmycloudex4NetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4NetType.setStatus("current")
_Wdmycloudex4Temperature_Type = DisplayString
_Wdmycloudex4Temperature_Object = MibScalar
wdmycloudex4Temperature = _Wdmycloudex4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 7),
    _Wdmycloudex4Temperature_Type()
)
wdmycloudex4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4Temperature.setStatus("current")
_Wdmycloudex4FanStatus_Type = DisplayString
_Wdmycloudex4FanStatus_Object = MibScalar
wdmycloudex4FanStatus = _Wdmycloudex4FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 8),
    _Wdmycloudex4FanStatus_Type()
)
wdmycloudex4FanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4FanStatus.setStatus("current")
_Wdmycloudex4VolumeTable_Object = MibTable
wdmycloudex4VolumeTable = _Wdmycloudex4VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wdmycloudex4VolumeTable.setStatus("current")
_Wdmycloudex4VolumeEntry_Object = MibTableRow
wdmycloudex4VolumeEntry = _Wdmycloudex4VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1)
)
wdmycloudex4VolumeEntry.setIndexNames(
    (0, "WDMYCLOUDEX4-MIB", "wdmycloudex4VolumeNum"),
)
if mibBuilder.loadTexts:
    wdmycloudex4VolumeEntry.setStatus("current")
_Wdmycloudex4VolumeNum_Type = Integer32
_Wdmycloudex4VolumeNum_Object = MibTableColumn
wdmycloudex4VolumeNum = _Wdmycloudex4VolumeNum_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 1),
    _Wdmycloudex4VolumeNum_Type()
)
wdmycloudex4VolumeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeNum.setStatus("current")
_Wdmycloudex4VolumeName_Type = DisplayString
_Wdmycloudex4VolumeName_Object = MibTableColumn
wdmycloudex4VolumeName = _Wdmycloudex4VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 2),
    _Wdmycloudex4VolumeName_Type()
)
wdmycloudex4VolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeName.setStatus("current")
_Wdmycloudex4VolumeFsType_Type = DisplayString
_Wdmycloudex4VolumeFsType_Object = MibTableColumn
wdmycloudex4VolumeFsType = _Wdmycloudex4VolumeFsType_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 3),
    _Wdmycloudex4VolumeFsType_Type()
)
wdmycloudex4VolumeFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeFsType.setStatus("current")
_Wdmycloudex4VolumeRaidLevel_Type = DisplayString
_Wdmycloudex4VolumeRaidLevel_Object = MibTableColumn
wdmycloudex4VolumeRaidLevel = _Wdmycloudex4VolumeRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 4),
    _Wdmycloudex4VolumeRaidLevel_Type()
)
wdmycloudex4VolumeRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeRaidLevel.setStatus("current")
_Wdmycloudex4VolumeSize_Type = DisplayString
_Wdmycloudex4VolumeSize_Object = MibTableColumn
wdmycloudex4VolumeSize = _Wdmycloudex4VolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 5),
    _Wdmycloudex4VolumeSize_Type()
)
wdmycloudex4VolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeSize.setStatus("current")
_Wdmycloudex4VolumeFreeSpace_Type = DisplayString
_Wdmycloudex4VolumeFreeSpace_Object = MibTableColumn
wdmycloudex4VolumeFreeSpace = _Wdmycloudex4VolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 9, 1, 6),
    _Wdmycloudex4VolumeFreeSpace_Type()
)
wdmycloudex4VolumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4VolumeFreeSpace.setStatus("current")
_Wdmycloudex4DiskTable_Object = MibTable
wdmycloudex4DiskTable = _Wdmycloudex4DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wdmycloudex4DiskTable.setStatus("current")
_Wdmycloudex4DiskEntry_Object = MibTableRow
wdmycloudex4DiskEntry = _Wdmycloudex4DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1)
)
wdmycloudex4DiskEntry.setIndexNames(
    (0, "WDMYCLOUDEX4-MIB", "wdmycloudex4DiskNum"),
)
if mibBuilder.loadTexts:
    wdmycloudex4DiskEntry.setStatus("current")
_Wdmycloudex4DiskNum_Type = Integer32
_Wdmycloudex4DiskNum_Object = MibTableColumn
wdmycloudex4DiskNum = _Wdmycloudex4DiskNum_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 1),
    _Wdmycloudex4DiskNum_Type()
)
wdmycloudex4DiskNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskNum.setStatus("current")
_Wdmycloudex4DiskVendor_Type = DisplayString
_Wdmycloudex4DiskVendor_Object = MibTableColumn
wdmycloudex4DiskVendor = _Wdmycloudex4DiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 2),
    _Wdmycloudex4DiskVendor_Type()
)
wdmycloudex4DiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskVendor.setStatus("current")
_Wdmycloudex4DiskModel_Type = DisplayString
_Wdmycloudex4DiskModel_Object = MibTableColumn
wdmycloudex4DiskModel = _Wdmycloudex4DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 3),
    _Wdmycloudex4DiskModel_Type()
)
wdmycloudex4DiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskModel.setStatus("current")
_Wdmycloudex4DiskSerialNumber_Type = DisplayString
_Wdmycloudex4DiskSerialNumber_Object = MibTableColumn
wdmycloudex4DiskSerialNumber = _Wdmycloudex4DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 4),
    _Wdmycloudex4DiskSerialNumber_Type()
)
wdmycloudex4DiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskSerialNumber.setStatus("current")
_Wdmycloudex4DiskTemperature_Type = DisplayString
_Wdmycloudex4DiskTemperature_Object = MibTableColumn
wdmycloudex4DiskTemperature = _Wdmycloudex4DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 5),
    _Wdmycloudex4DiskTemperature_Type()
)
wdmycloudex4DiskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskTemperature.setStatus("current")
_Wdmycloudex4DiskCapacity_Type = DisplayString
_Wdmycloudex4DiskCapacity_Object = MibTableColumn
wdmycloudex4DiskCapacity = _Wdmycloudex4DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 10, 1, 6),
    _Wdmycloudex4DiskCapacity_Type()
)
wdmycloudex4DiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4DiskCapacity.setStatus("current")
_Wdmycloudex4UPSTable_Object = MibTable
wdmycloudex4UPSTable = _Wdmycloudex4UPSTable_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wdmycloudex4UPSTable.setStatus("current")
_Wdmycloudex4UPSEntry_Object = MibTableRow
wdmycloudex4UPSEntry = _Wdmycloudex4UPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1)
)
wdmycloudex4UPSEntry.setIndexNames(
    (0, "WDMYCLOUDEX4-MIB", "wdmycloudex4UPSNum"),
)
if mibBuilder.loadTexts:
    wdmycloudex4UPSEntry.setStatus("current")
_Wdmycloudex4UPSNum_Type = Integer32
_Wdmycloudex4UPSNum_Object = MibTableColumn
wdmycloudex4UPSNum = _Wdmycloudex4UPSNum_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 1),
    _Wdmycloudex4UPSNum_Type()
)
wdmycloudex4UPSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSNum.setStatus("current")
_Wdmycloudex4UPSMode_Type = DisplayString
_Wdmycloudex4UPSMode_Object = MibTableColumn
wdmycloudex4UPSMode = _Wdmycloudex4UPSMode_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 2),
    _Wdmycloudex4UPSMode_Type()
)
wdmycloudex4UPSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSMode.setStatus("current")
_Wdmycloudex4UPSManufacturer_Type = DisplayString
_Wdmycloudex4UPSManufacturer_Object = MibTableColumn
wdmycloudex4UPSManufacturer = _Wdmycloudex4UPSManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 3),
    _Wdmycloudex4UPSManufacturer_Type()
)
wdmycloudex4UPSManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSManufacturer.setStatus("current")
_Wdmycloudex4UPSProduct_Type = DisplayString
_Wdmycloudex4UPSProduct_Object = MibTableColumn
wdmycloudex4UPSProduct = _Wdmycloudex4UPSProduct_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 4),
    _Wdmycloudex4UPSProduct_Type()
)
wdmycloudex4UPSProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSProduct.setStatus("current")
_Wdmycloudex4UPSBatteryCharge_Type = DisplayString
_Wdmycloudex4UPSBatteryCharge_Object = MibTableColumn
wdmycloudex4UPSBatteryCharge = _Wdmycloudex4UPSBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 5),
    _Wdmycloudex4UPSBatteryCharge_Type()
)
wdmycloudex4UPSBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSBatteryCharge.setStatus("current")
_Wdmycloudex4UPSStatus_Type = DisplayString
_Wdmycloudex4UPSStatus_Object = MibTableColumn
wdmycloudex4UPSStatus = _Wdmycloudex4UPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 11, 1, 6),
    _Wdmycloudex4UPSStatus_Type()
)
wdmycloudex4UPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmycloudex4UPSStatus.setStatus("current")
_NotifyEvts_ObjectIdentity = ObjectIdentity
notifyEvts = _NotifyEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 200)
)

# Managed Objects groups


# Notification objects

notifyPasswdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 200, 1)
)
if mibBuilder.loadTexts:
    notifyPasswdChanged.setStatus(
        "current"
    )

notifyFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 200, 2)
)
if mibBuilder.loadTexts:
    notifyFirmwareUpgraded.setStatus(
        "current"
    )

notifyNetworkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 200, 3)
)
if mibBuilder.loadTexts:
    notifyNetworkChanged.setStatus(
        "current"
    )

notifyTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5127, 1, 1, 1, 1, 1, 200, 4)
)
if mibBuilder.loadTexts:
    notifyTemperatureExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WDMYCLOUDEX4-MIB",
    **{"wd": wd,
       "productID": productID,
       "projectID": projectID,
       "modelID": modelID,
       "submodelID": submodelID,
       "nasAgent": nasAgent,
       "wdmycloudex4AgentVer": wdmycloudex4AgentVer,
       "wdmycloudex4SoftwareVersion": wdmycloudex4SoftwareVersion,
       "wdmycloudex4HostName": wdmycloudex4HostName,
       "wdmycloudex4FTPServer": wdmycloudex4FTPServer,
       "wdmycloudex4NetType": wdmycloudex4NetType,
       "wdmycloudex4Temperature": wdmycloudex4Temperature,
       "wdmycloudex4FanStatus": wdmycloudex4FanStatus,
       "wdmycloudex4VolumeTable": wdmycloudex4VolumeTable,
       "wdmycloudex4VolumeEntry": wdmycloudex4VolumeEntry,
       "wdmycloudex4VolumeNum": wdmycloudex4VolumeNum,
       "wdmycloudex4VolumeName": wdmycloudex4VolumeName,
       "wdmycloudex4VolumeFsType": wdmycloudex4VolumeFsType,
       "wdmycloudex4VolumeRaidLevel": wdmycloudex4VolumeRaidLevel,
       "wdmycloudex4VolumeSize": wdmycloudex4VolumeSize,
       "wdmycloudex4VolumeFreeSpace": wdmycloudex4VolumeFreeSpace,
       "wdmycloudex4DiskTable": wdmycloudex4DiskTable,
       "wdmycloudex4DiskEntry": wdmycloudex4DiskEntry,
       "wdmycloudex4DiskNum": wdmycloudex4DiskNum,
       "wdmycloudex4DiskVendor": wdmycloudex4DiskVendor,
       "wdmycloudex4DiskModel": wdmycloudex4DiskModel,
       "wdmycloudex4DiskSerialNumber": wdmycloudex4DiskSerialNumber,
       "wdmycloudex4DiskTemperature": wdmycloudex4DiskTemperature,
       "wdmycloudex4DiskCapacity": wdmycloudex4DiskCapacity,
       "wdmycloudex4UPSTable": wdmycloudex4UPSTable,
       "wdmycloudex4UPSEntry": wdmycloudex4UPSEntry,
       "wdmycloudex4UPSNum": wdmycloudex4UPSNum,
       "wdmycloudex4UPSMode": wdmycloudex4UPSMode,
       "wdmycloudex4UPSManufacturer": wdmycloudex4UPSManufacturer,
       "wdmycloudex4UPSProduct": wdmycloudex4UPSProduct,
       "wdmycloudex4UPSBatteryCharge": wdmycloudex4UPSBatteryCharge,
       "wdmycloudex4UPSStatus": wdmycloudex4UPSStatus,
       "notifyEvts": notifyEvts,
       "notifyPasswdChanged": notifyPasswdChanged,
       "notifyFirmwareUpgraded": notifyFirmwareUpgraded,
       "notifyNetworkChanged": notifyNetworkChanged,
       "notifyTemperatureExceeded": notifyTemperatureExceeded}
)
