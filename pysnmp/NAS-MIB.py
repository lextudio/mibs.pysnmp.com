# SNMP MIB module (NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:38 2024
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
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5)
)
_SubmodelID_ObjectIdentity = ObjectIdentity
submodelID = _SubmodelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1)
)
_NasAgent_ObjectIdentity = ObjectIdentity
nasAgent = _NasAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1)
)
_Dns345AgentVer_Type = DisplayString
_Dns345AgentVer_Object = MibScalar
dns345AgentVer = _Dns345AgentVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 1),
    _Dns345AgentVer_Type()
)
dns345AgentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345AgentVer.setStatus("current")
_Dns345SoftwareVersion_Type = DisplayString
_Dns345SoftwareVersion_Object = MibScalar
dns345SoftwareVersion = _Dns345SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 2),
    _Dns345SoftwareVersion_Type()
)
dns345SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345SoftwareVersion.setStatus("current")
_Dns345HostName_Type = DisplayString
_Dns345HostName_Object = MibScalar
dns345HostName = _Dns345HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 3),
    _Dns345HostName_Type()
)
dns345HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345HostName.setStatus("current")
_Dns345FTPServer_Type = DisplayString
_Dns345FTPServer_Object = MibScalar
dns345FTPServer = _Dns345FTPServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 5),
    _Dns345FTPServer_Type()
)
dns345FTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345FTPServer.setStatus("current")
_Dns345NetType_Type = DisplayString
_Dns345NetType_Object = MibScalar
dns345NetType = _Dns345NetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 6),
    _Dns345NetType_Type()
)
dns345NetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345NetType.setStatus("current")
_Dns345Temperature_Type = DisplayString
_Dns345Temperature_Object = MibScalar
dns345Temperature = _Dns345Temperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 7),
    _Dns345Temperature_Type()
)
dns345Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345Temperature.setStatus("current")
_Dns345FanStatus_Type = DisplayString
_Dns345FanStatus_Object = MibScalar
dns345FanStatus = _Dns345FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 8),
    _Dns345FanStatus_Type()
)
dns345FanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345FanStatus.setStatus("current")
_Dns345VolumeTable_Object = MibTable
dns345VolumeTable = _Dns345VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    dns345VolumeTable.setStatus("current")
_Dns345VolumeEntry_Object = MibTableRow
dns345VolumeEntry = _Dns345VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1)
)
dns345VolumeEntry.setIndexNames(
    (0, "NAS-MIB", "dns345VolumeNum"),
)
if mibBuilder.loadTexts:
    dns345VolumeEntry.setStatus("current")
_Dns345VolumeNum_Type = Integer32
_Dns345VolumeNum_Object = MibTableColumn
dns345VolumeNum = _Dns345VolumeNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 1),
    _Dns345VolumeNum_Type()
)
dns345VolumeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeNum.setStatus("current")
_Dns345VolumeName_Type = DisplayString
_Dns345VolumeName_Object = MibTableColumn
dns345VolumeName = _Dns345VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 2),
    _Dns345VolumeName_Type()
)
dns345VolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeName.setStatus("current")
_Dns345VolumeFsType_Type = DisplayString
_Dns345VolumeFsType_Object = MibTableColumn
dns345VolumeFsType = _Dns345VolumeFsType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 3),
    _Dns345VolumeFsType_Type()
)
dns345VolumeFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeFsType.setStatus("current")
_Dns345VolumeRaidLevel_Type = DisplayString
_Dns345VolumeRaidLevel_Object = MibTableColumn
dns345VolumeRaidLevel = _Dns345VolumeRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 4),
    _Dns345VolumeRaidLevel_Type()
)
dns345VolumeRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeRaidLevel.setStatus("current")
_Dns345VolumeSize_Type = DisplayString
_Dns345VolumeSize_Object = MibTableColumn
dns345VolumeSize = _Dns345VolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 5),
    _Dns345VolumeSize_Type()
)
dns345VolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeSize.setStatus("current")
_Dns345VolumeFreeSpace_Type = DisplayString
_Dns345VolumeFreeSpace_Object = MibTableColumn
dns345VolumeFreeSpace = _Dns345VolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 9, 1, 6),
    _Dns345VolumeFreeSpace_Type()
)
dns345VolumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345VolumeFreeSpace.setStatus("current")
_Dns345DiskTable_Object = MibTable
dns345DiskTable = _Dns345DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    dns345DiskTable.setStatus("current")
_Dns345DiskEntry_Object = MibTableRow
dns345DiskEntry = _Dns345DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1)
)
dns345DiskEntry.setIndexNames(
    (0, "NAS-MIB", "dns345DiskNum"),
)
if mibBuilder.loadTexts:
    dns345DiskEntry.setStatus("current")
_Dns345DiskNum_Type = Integer32
_Dns345DiskNum_Object = MibTableColumn
dns345DiskNum = _Dns345DiskNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 1),
    _Dns345DiskNum_Type()
)
dns345DiskNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskNum.setStatus("current")
_Dns345DiskVendor_Type = DisplayString
_Dns345DiskVendor_Object = MibTableColumn
dns345DiskVendor = _Dns345DiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 2),
    _Dns345DiskVendor_Type()
)
dns345DiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskVendor.setStatus("current")
_Dns345DiskModel_Type = DisplayString
_Dns345DiskModel_Object = MibTableColumn
dns345DiskModel = _Dns345DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 3),
    _Dns345DiskModel_Type()
)
dns345DiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskModel.setStatus("current")
_Dns345DiskSerialNumber_Type = DisplayString
_Dns345DiskSerialNumber_Object = MibTableColumn
dns345DiskSerialNumber = _Dns345DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 4),
    _Dns345DiskSerialNumber_Type()
)
dns345DiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskSerialNumber.setStatus("current")
_Dns345DiskTemperature_Type = DisplayString
_Dns345DiskTemperature_Object = MibTableColumn
dns345DiskTemperature = _Dns345DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 5),
    _Dns345DiskTemperature_Type()
)
dns345DiskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskTemperature.setStatus("current")
_Dns345DiskCapacity_Type = DisplayString
_Dns345DiskCapacity_Object = MibTableColumn
dns345DiskCapacity = _Dns345DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 10, 1, 6),
    _Dns345DiskCapacity_Type()
)
dns345DiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns345DiskCapacity.setStatus("current")
_NotifyEvts_ObjectIdentity = ObjectIdentity
notifyEvts = _NotifyEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 200)
)

# Managed Objects groups


# Notification objects

notifyPasswdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 200, 1)
)
if mibBuilder.loadTexts:
    notifyPasswdChanged.setStatus(
        "current"
    )

notifyFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 200, 2)
)
if mibBuilder.loadTexts:
    notifyFirmwareUpgraded.setStatus(
        "current"
    )

notifyNetworkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 200, 3)
)
if mibBuilder.loadTexts:
    notifyNetworkChanged.setStatus(
        "current"
    )

notifyTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 5, 1, 1, 200, 4)
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
    "NAS-MIB",
    **{"d-link": d_link,
       "productID": productID,
       "projectID": projectID,
       "modelID": modelID,
       "submodelID": submodelID,
       "nasAgent": nasAgent,
       "dns345AgentVer": dns345AgentVer,
       "dns345SoftwareVersion": dns345SoftwareVersion,
       "dns345HostName": dns345HostName,
       "dns345FTPServer": dns345FTPServer,
       "dns345NetType": dns345NetType,
       "dns345Temperature": dns345Temperature,
       "dns345FanStatus": dns345FanStatus,
       "dns345VolumeTable": dns345VolumeTable,
       "dns345VolumeEntry": dns345VolumeEntry,
       "dns345VolumeNum": dns345VolumeNum,
       "dns345VolumeName": dns345VolumeName,
       "dns345VolumeFsType": dns345VolumeFsType,
       "dns345VolumeRaidLevel": dns345VolumeRaidLevel,
       "dns345VolumeSize": dns345VolumeSize,
       "dns345VolumeFreeSpace": dns345VolumeFreeSpace,
       "dns345DiskTable": dns345DiskTable,
       "dns345DiskEntry": dns345DiskEntry,
       "dns345DiskNum": dns345DiskNum,
       "dns345DiskVendor": dns345DiskVendor,
       "dns345DiskModel": dns345DiskModel,
       "dns345DiskSerialNumber": dns345DiskSerialNumber,
       "dns345DiskTemperature": dns345DiskTemperature,
       "dns345DiskCapacity": dns345DiskCapacity,
       "notifyEvts": notifyEvts,
       "notifyPasswdChanged": notifyPasswdChanged,
       "notifyFirmwareUpgraded": notifyFirmwareUpgraded,
       "notifyNetworkChanged": notifyNetworkChanged,
       "notifyTemperatureExceeded": notifyTemperatureExceeded}
)
