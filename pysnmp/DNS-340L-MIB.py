# SNMP MIB module (DNS-340L-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNS-340L-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:22 2024
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

_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50)
)
_ProjectID_ObjectIdentity = ObjectIdentity
projectID = _ProjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1)
)
_ModelID_ObjectIdentity = ObjectIdentity
modelID = _ModelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10)
)
_SubmodelID_ObjectIdentity = ObjectIdentity
submodelID = _SubmodelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1)
)
_NasAgent_ObjectIdentity = ObjectIdentity
nasAgent = _NasAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1)
)
_Dns340LAgentVer_Type = DisplayString
_Dns340LAgentVer_Object = MibScalar
dns340LAgentVer = _Dns340LAgentVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 1),
    _Dns340LAgentVer_Type()
)
dns340LAgentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LAgentVer.setStatus("current")
_Dns340LSoftwareVersion_Type = DisplayString
_Dns340LSoftwareVersion_Object = MibScalar
dns340LSoftwareVersion = _Dns340LSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 2),
    _Dns340LSoftwareVersion_Type()
)
dns340LSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LSoftwareVersion.setStatus("current")
_Dns340LHostName_Type = DisplayString
_Dns340LHostName_Object = MibScalar
dns340LHostName = _Dns340LHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 3),
    _Dns340LHostName_Type()
)
dns340LHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LHostName.setStatus("current")
_Dns340LFTPServer_Type = DisplayString
_Dns340LFTPServer_Object = MibScalar
dns340LFTPServer = _Dns340LFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 5),
    _Dns340LFTPServer_Type()
)
dns340LFTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LFTPServer.setStatus("current")
_Dns340LNetType_Type = DisplayString
_Dns340LNetType_Object = MibScalar
dns340LNetType = _Dns340LNetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 6),
    _Dns340LNetType_Type()
)
dns340LNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LNetType.setStatus("current")
_Dns340LTemperature_Type = DisplayString
_Dns340LTemperature_Object = MibScalar
dns340LTemperature = _Dns340LTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 7),
    _Dns340LTemperature_Type()
)
dns340LTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LTemperature.setStatus("current")
_Dns340LFanStatus_Type = DisplayString
_Dns340LFanStatus_Object = MibScalar
dns340LFanStatus = _Dns340LFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 8),
    _Dns340LFanStatus_Type()
)
dns340LFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LFanStatus.setStatus("current")
_Dns340LVolumeTable_Object = MibTable
dns340LVolumeTable = _Dns340LVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9)
)
if mibBuilder.loadTexts:
    dns340LVolumeTable.setStatus("current")
_Dns340LVolumeEntry_Object = MibTableRow
dns340LVolumeEntry = _Dns340LVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1)
)
dns340LVolumeEntry.setIndexNames(
    (0, "DNS-340L-MIB", "dns340LVolumeNum"),
)
if mibBuilder.loadTexts:
    dns340LVolumeEntry.setStatus("current")
_Dns340LVolumeNum_Type = Integer32
_Dns340LVolumeNum_Object = MibTableColumn
dns340LVolumeNum = _Dns340LVolumeNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 1),
    _Dns340LVolumeNum_Type()
)
dns340LVolumeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeNum.setStatus("current")
_Dns340LVolumeName_Type = DisplayString
_Dns340LVolumeName_Object = MibTableColumn
dns340LVolumeName = _Dns340LVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 2),
    _Dns340LVolumeName_Type()
)
dns340LVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeName.setStatus("current")
_Dns340LVolumeFsType_Type = DisplayString
_Dns340LVolumeFsType_Object = MibTableColumn
dns340LVolumeFsType = _Dns340LVolumeFsType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 3),
    _Dns340LVolumeFsType_Type()
)
dns340LVolumeFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeFsType.setStatus("current")
_Dns340LVolumeRaidLevel_Type = DisplayString
_Dns340LVolumeRaidLevel_Object = MibTableColumn
dns340LVolumeRaidLevel = _Dns340LVolumeRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 4),
    _Dns340LVolumeRaidLevel_Type()
)
dns340LVolumeRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeRaidLevel.setStatus("current")
_Dns340LVolumeSize_Type = DisplayString
_Dns340LVolumeSize_Object = MibTableColumn
dns340LVolumeSize = _Dns340LVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 5),
    _Dns340LVolumeSize_Type()
)
dns340LVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeSize.setStatus("current")
_Dns340LVolumeFreeSpace_Type = DisplayString
_Dns340LVolumeFreeSpace_Object = MibTableColumn
dns340LVolumeFreeSpace = _Dns340LVolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 6),
    _Dns340LVolumeFreeSpace_Type()
)
dns340LVolumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LVolumeFreeSpace.setStatus("current")
_Dns340LDiskTable_Object = MibTable
dns340LDiskTable = _Dns340LDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10)
)
if mibBuilder.loadTexts:
    dns340LDiskTable.setStatus("current")
_Dns340LDiskEntry_Object = MibTableRow
dns340LDiskEntry = _Dns340LDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1)
)
dns340LDiskEntry.setIndexNames(
    (0, "DNS-340L-MIB", "dns340LDiskNum"),
)
if mibBuilder.loadTexts:
    dns340LDiskEntry.setStatus("current")
_Dns340LDiskNum_Type = Integer32
_Dns340LDiskNum_Object = MibTableColumn
dns340LDiskNum = _Dns340LDiskNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 1),
    _Dns340LDiskNum_Type()
)
dns340LDiskNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskNum.setStatus("current")
_Dns340LDiskVendor_Type = DisplayString
_Dns340LDiskVendor_Object = MibTableColumn
dns340LDiskVendor = _Dns340LDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 2),
    _Dns340LDiskVendor_Type()
)
dns340LDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskVendor.setStatus("current")
_Dns340LDiskModel_Type = DisplayString
_Dns340LDiskModel_Object = MibTableColumn
dns340LDiskModel = _Dns340LDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 3),
    _Dns340LDiskModel_Type()
)
dns340LDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskModel.setStatus("current")
_Dns340LDiskSerialNumber_Type = DisplayString
_Dns340LDiskSerialNumber_Object = MibTableColumn
dns340LDiskSerialNumber = _Dns340LDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 4),
    _Dns340LDiskSerialNumber_Type()
)
dns340LDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskSerialNumber.setStatus("current")
_Dns340LDiskTemperature_Type = DisplayString
_Dns340LDiskTemperature_Object = MibTableColumn
dns340LDiskTemperature = _Dns340LDiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 5),
    _Dns340LDiskTemperature_Type()
)
dns340LDiskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskTemperature.setStatus("current")
_Dns340LDiskCapacity_Type = DisplayString
_Dns340LDiskCapacity_Object = MibTableColumn
dns340LDiskCapacity = _Dns340LDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 6),
    _Dns340LDiskCapacity_Type()
)
dns340LDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LDiskCapacity.setStatus("current")
_Dns340LUPSTable_Object = MibTable
dns340LUPSTable = _Dns340LUPSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11)
)
if mibBuilder.loadTexts:
    dns340LUPSTable.setStatus("current")
_Dns340LUPSEntry_Object = MibTableRow
dns340LUPSEntry = _Dns340LUPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1)
)
dns340LUPSEntry.setIndexNames(
    (0, "DNS-340L-MIB", "dns340LUPSNum"),
)
if mibBuilder.loadTexts:
    dns340LUPSEntry.setStatus("current")
_Dns340LUPSNum_Type = Integer32
_Dns340LUPSNum_Object = MibTableColumn
dns340LUPSNum = _Dns340LUPSNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 1),
    _Dns340LUPSNum_Type()
)
dns340LUPSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSNum.setStatus("current")
_Dns340LUPSMode_Type = DisplayString
_Dns340LUPSMode_Object = MibTableColumn
dns340LUPSMode = _Dns340LUPSMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 2),
    _Dns340LUPSMode_Type()
)
dns340LUPSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSMode.setStatus("current")
_Dns340LUPSManufacturer_Type = DisplayString
_Dns340LUPSManufacturer_Object = MibTableColumn
dns340LUPSManufacturer = _Dns340LUPSManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 3),
    _Dns340LUPSManufacturer_Type()
)
dns340LUPSManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSManufacturer.setStatus("current")
_Dns340LUPSProduct_Type = DisplayString
_Dns340LUPSProduct_Object = MibTableColumn
dns340LUPSProduct = _Dns340LUPSProduct_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 4),
    _Dns340LUPSProduct_Type()
)
dns340LUPSProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSProduct.setStatus("current")
_Dns340LUPSBatteryCharge_Type = DisplayString
_Dns340LUPSBatteryCharge_Object = MibTableColumn
dns340LUPSBatteryCharge = _Dns340LUPSBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 5),
    _Dns340LUPSBatteryCharge_Type()
)
dns340LUPSBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSBatteryCharge.setStatus("current")
_Dns340LUPSStatus_Type = DisplayString
_Dns340LUPSStatus_Object = MibTableColumn
dns340LUPSStatus = _Dns340LUPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 6),
    _Dns340LUPSStatus_Type()
)
dns340LUPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns340LUPSStatus.setStatus("current")
_NotifyEvts_ObjectIdentity = ObjectIdentity
notifyEvts = _NotifyEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200)
)

# Managed Objects groups


# Notification objects

notifyPasswdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 1)
)
if mibBuilder.loadTexts:
    notifyPasswdChanged.setStatus(
        "current"
    )

notifyFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 2)
)
if mibBuilder.loadTexts:
    notifyFirmwareUpgraded.setStatus(
        "current"
    )

notifyNetworkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 3)
)
if mibBuilder.loadTexts:
    notifyNetworkChanged.setStatus(
        "current"
    )

notifyTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 4)
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
    "DNS-340L-MIB",
    **{"d-link": d_link,
       "productID": productID,
       "projectID": projectID,
       "modelID": modelID,
       "submodelID": submodelID,
       "nasAgent": nasAgent,
       "dns340LAgentVer": dns340LAgentVer,
       "dns340LSoftwareVersion": dns340LSoftwareVersion,
       "dns340LHostName": dns340LHostName,
       "dns340LFTPServer": dns340LFTPServer,
       "dns340LNetType": dns340LNetType,
       "dns340LTemperature": dns340LTemperature,
       "dns340LFanStatus": dns340LFanStatus,
       "dns340LVolumeTable": dns340LVolumeTable,
       "dns340LVolumeEntry": dns340LVolumeEntry,
       "dns340LVolumeNum": dns340LVolumeNum,
       "dns340LVolumeName": dns340LVolumeName,
       "dns340LVolumeFsType": dns340LVolumeFsType,
       "dns340LVolumeRaidLevel": dns340LVolumeRaidLevel,
       "dns340LVolumeSize": dns340LVolumeSize,
       "dns340LVolumeFreeSpace": dns340LVolumeFreeSpace,
       "dns340LDiskTable": dns340LDiskTable,
       "dns340LDiskEntry": dns340LDiskEntry,
       "dns340LDiskNum": dns340LDiskNum,
       "dns340LDiskVendor": dns340LDiskVendor,
       "dns340LDiskModel": dns340LDiskModel,
       "dns340LDiskSerialNumber": dns340LDiskSerialNumber,
       "dns340LDiskTemperature": dns340LDiskTemperature,
       "dns340LDiskCapacity": dns340LDiskCapacity,
       "dns340LUPSTable": dns340LUPSTable,
       "dns340LUPSEntry": dns340LUPSEntry,
       "dns340LUPSNum": dns340LUPSNum,
       "dns340LUPSMode": dns340LUPSMode,
       "dns340LUPSManufacturer": dns340LUPSManufacturer,
       "dns340LUPSProduct": dns340LUPSProduct,
       "dns340LUPSBatteryCharge": dns340LUPSBatteryCharge,
       "dns340LUPSStatus": dns340LUPSStatus,
       "notifyEvts": notifyEvts,
       "notifyPasswdChanged": notifyPasswdChanged,
       "notifyFirmwareUpgraded": notifyFirmwareUpgraded,
       "notifyNetworkChanged": notifyNetworkChanged,
       "notifyTemperatureExceeded": notifyTemperatureExceeded}
)
