# SNMP MIB module (RemoteKVMDevice-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RemoteKVMDevice-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2014-11-06 12:00",
         "2013-11-01 12:00",
         "2011-12-20 12:00",
         "2011-07-08 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RemoteKVMDevice_ObjectIdentity = ObjectIdentity
remoteKVMDevice = _RemoteKVMDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 3)
)
_RemoteKVMDeviceNotifications_ObjectIdentity = ObjectIdentity
remoteKVMDeviceNotifications = _RemoteKVMDeviceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0)
)
_RcpObjectProductVersion_Type = DisplayString
_RcpObjectProductVersion_Object = MibScalar
rcpObjectProductVersion = _RcpObjectProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 1),
    _RcpObjectProductVersion_Type()
)
rcpObjectProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpObjectProductVersion.setStatus("current")
_RcpObjectName_Type = DisplayString
_RcpObjectName_Object = MibScalar
rcpObjectName = _RcpObjectName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 2),
    _RcpObjectName_Type()
)
rcpObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcpObjectName.setStatus("current")
_RcpObjectInstance_Type = DisplayString
_RcpObjectInstance_Object = MibScalar
rcpObjectInstance = _RcpObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 3),
    _RcpObjectInstance_Type()
)
rcpObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcpObjectInstance.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 4),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_TargetUser_Type = DisplayString
_TargetUser_Object = MibScalar
targetUser = _TargetUser_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 5),
    _TargetUser_Type()
)
targetUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetUser.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibScalar
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 6),
    _GroupName_Type()
)
groupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_RcpIPAddress_Type = DisplayString
_RcpIPAddress_Object = MibScalar
rcpIPAddress = _RcpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 7),
    _RcpIPAddress_Type()
)
rcpIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcpIPAddress.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 8),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_PortStatus_Type = DisplayString
_PortStatus_Object = MibScalar
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 9),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStatus.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibScalar
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 10),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_ClusterID_Type = DisplayString
_ClusterID_Object = MibScalar
clusterID = _ClusterID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 11),
    _ClusterID_Type()
)
clusterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterID.setStatus("current")
_IpPort_Type = DisplayString
_IpPort_Object = MibScalar
ipPort = _IpPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 12),
    _IpPort_Type()
)
ipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPort.setStatus("current")
_ResetType_Type = DisplayString
_ResetType_Object = MibScalar
resetType = _ResetType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 13),
    _ResetType_Type()
)
resetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetType.setStatus("current")


class _Interface_Type(Integer32):
    """Custom type interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("modem", 2))
    )


_Interface_Type.__name__ = "Integer32"
_Interface_Object = MibScalar
interface = _Interface_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 14),
    _Interface_Type()
)
interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interface.setStatus("current")


class _EthernetInterface_Type(Integer32):
    """Custom type ethernetInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lan0", 0),
          ("lan1", 1))
    )


_EthernetInterface_Type.__name__ = "Integer32"
_EthernetInterface_Object = MibScalar
ethernetInterface = _EthernetInterface_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 15),
    _EthernetInterface_Type()
)
ethernetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterface.setStatus("current")


class _BackupRestoreAction_Type(Integer32):
    """Custom type backupRestoreAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 0),
          ("restore", 1))
    )


_BackupRestoreAction_Type.__name__ = "Integer32"
_BackupRestoreAction_Object = MibScalar
backupRestoreAction = _BackupRestoreAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 16),
    _BackupRestoreAction_Type()
)
backupRestoreAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreAction.setStatus("current")
_ImageType_Type = DisplayString
_ImageType_Object = MibScalar
imageType = _ImageType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 17),
    _ImageType_Type()
)
imageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageType.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibScalar
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 18),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_Status_Type = DisplayString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 19),
    _Status_Type()
)
status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status.setStatus("current")
_FileVersion_Type = DisplayString
_FileVersion_Object = MibScalar
fileVersion = _FileVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 20),
    _FileVersion_Type()
)
fileVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileVersion.setStatus("current")
_FileType_Type = DisplayString
_FileType_Object = MibScalar
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 21),
    _FileType_Type()
)
fileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileType.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibScalar
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 22),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_PortNumber_Type = Integer32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 23),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 24),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_CimName_Type = DisplayString
_CimName_Object = MibScalar
cimName = _CimName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 25),
    _CimName_Type()
)
cimName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimName.setStatus("current")
_Count_Type = Integer32
_Count_Object = MibScalar
count = _Count_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 26),
    _Count_Type()
)
count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    count.setStatus("current")
_RestoredLanPort_Type = Integer32
_RestoredLanPort_Object = MibScalar
restoredLanPort = _RestoredLanPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 27),
    _RestoredLanPort_Type()
)
restoredLanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoredLanPort.setStatus("current")
_RemoteIpAddress_Type = DisplayString
_RemoteIpAddress_Object = MibScalar
remoteIpAddress = _RemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 28),
    _RemoteIpAddress_Type()
)
remoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteIpAddress.setStatus("current")
_OldIpAddress_Type = DisplayString
_OldIpAddress_Object = MibScalar
oldIpAddress = _OldIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 29),
    _OldIpAddress_Type()
)
oldIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpAddress.setStatus("current")
_NewIpAddress_Type = DisplayString
_NewIpAddress_Object = MibScalar
newIpAddress = _NewIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 30),
    _NewIpAddress_Type()
)
newIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newIpAddress.setStatus("current")
_NewNetmask_Type = DisplayString
_NewNetmask_Object = MibScalar
newNetmask = _NewNetmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 31),
    _NewNetmask_Type()
)
newNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newNetmask.setStatus("current")
_OldNetmask_Type = DisplayString
_OldNetmask_Object = MibScalar
oldNetmask = _OldNetmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 32),
    _OldNetmask_Type()
)
oldNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldNetmask.setStatus("current")
_OldGateway_Type = DisplayString
_OldGateway_Object = MibScalar
oldGateway = _OldGateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 33),
    _OldGateway_Type()
)
oldGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldGateway.setStatus("current")
_NewGateway_Type = DisplayString
_NewGateway_Object = MibScalar
newGateway = _NewGateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 34),
    _NewGateway_Type()
)
newGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newGateway.setStatus("current")
_SxAlertString_Type = DisplayString
_SxAlertString_Object = MibScalar
sxAlertString = _SxAlertString_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 38),
    _SxAlertString_Type()
)
sxAlertString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAlertString.setStatus("current")
_PduName_Type = DisplayString
_PduName_Object = MibScalar
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 39),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")
_ChangeEventText_Type = DisplayString
_ChangeEventText_Object = MibScalar
changeEventText = _ChangeEventText_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 40),
    _ChangeEventText_Type()
)
changeEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changeEventText.setStatus("current")
_CertificateAuthorityName_Type = DisplayString
_CertificateAuthorityName_Object = MibScalar
certificateAuthorityName = _CertificateAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 41),
    _CertificateAuthorityName_Type()
)
certificateAuthorityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateAuthorityName.setStatus("current")
_SysDateAndTime_Type = DateAndTime
_SysDateAndTime_Object = MibScalar
sysDateAndTime = _SysDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 42),
    _SysDateAndTime_Type()
)
sysDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateAndTime.setStatus("current")
_FipsModeStatus_Type = DisplayString
_FipsModeStatus_Object = MibScalar
fipsModeStatus = _FipsModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 43),
    _FipsModeStatus_Type()
)
fipsModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fipsModeStatus.setStatus("current")


class _BannerChanges_Type(Integer32):
    """Custom type bannerChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("modified", 2))
    )


_BannerChanges_Type.__name__ = "Integer32"
_BannerChanges_Object = MibScalar
bannerChanges = _BannerChanges_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 44),
    _BannerChanges_Type()
)
bannerChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bannerChanges.setStatus("current")


class _BannerAction_Type(Integer32):
    """Custom type bannerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("declined", 0))
    )


_BannerAction_Type.__name__ = "Integer32"
_BannerAction_Object = MibScalar
bannerAction = _BannerAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 45),
    _BannerAction_Type()
)
bannerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bannerAction.setStatus("current")


class _PortList_Type(OctetString):
    """Custom type portList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PortList_Type.__name__ = "OctetString"
_PortList_Object = MibScalar
portList = _PortList_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 46),
    _PortList_Type()
)
portList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portList.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 3, 47),
    _FileName_Type()
)
fileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_RaritanMibConformance_ObjectIdentity = ObjectIdentity
raritanMibConformance = _RaritanMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9)
)
_RaritanMibCompliances_ObjectIdentity = ObjectIdentity
raritanMibCompliances = _RaritanMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1)
)
_RaritanMibGroups_ObjectIdentity = ObjectIdentity
raritanMibGroups = _RaritanMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2)
)

# Managed Objects groups

raritanMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1)
)
raritanMibBasicGroup.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectProductVersion"),
        ("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "targetUser"),
        ("RemoteKVMDevice-MIB", "groupName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "deviceName"),
        ("RemoteKVMDevice-MIB", "portStatus"),
        ("RemoteKVMDevice-MIB", "portName"),
        ("RemoteKVMDevice-MIB", "clusterID"),
        ("RemoteKVMDevice-MIB", "ipPort"),
        ("RemoteKVMDevice-MIB", "resetType"),
        ("RemoteKVMDevice-MIB", "interface"),
        ("RemoteKVMDevice-MIB", "ethernetInterface"),
        ("RemoteKVMDevice-MIB", "backupRestoreAction"),
        ("RemoteKVMDevice-MIB", "imageType"),
        ("RemoteKVMDevice-MIB", "imageVersion"),
        ("RemoteKVMDevice-MIB", "status"),
        ("RemoteKVMDevice-MIB", "fileVersion"),
        ("RemoteKVMDevice-MIB", "fileType"),
        ("RemoteKVMDevice-MIB", "outletName"),
        ("RemoteKVMDevice-MIB", "portNumber"),
        ("RemoteKVMDevice-MIB", "serialNumber"),
        ("RemoteKVMDevice-MIB", "cimName"),
        ("RemoteKVMDevice-MIB", "count"),
        ("RemoteKVMDevice-MIB", "restoredLanPort"),
        ("RemoteKVMDevice-MIB", "remoteIpAddress"),
        ("RemoteKVMDevice-MIB", "oldIpAddress"),
        ("RemoteKVMDevice-MIB", "newIpAddress"),
        ("RemoteKVMDevice-MIB", "newNetmask"),
        ("RemoteKVMDevice-MIB", "oldNetmask"),
        ("RemoteKVMDevice-MIB", "oldGateway"),
        ("RemoteKVMDevice-MIB", "newGateway"),
        ("RemoteKVMDevice-MIB", "sxAlertString"),
        ("RemoteKVMDevice-MIB", "pduName"),
        ("RemoteKVMDevice-MIB", "changeEventText"),
        ("RemoteKVMDevice-MIB", "certificateAuthorityName"),
        ("RemoteKVMDevice-MIB", "sysDateAndTime"),
        ("RemoteKVMDevice-MIB", "fipsModeStatus"),
        ("RemoteKVMDevice-MIB", "bannerChanges"),
        ("RemoteKVMDevice-MIB", "bannerAction"),
        ("RemoteKVMDevice-MIB", "portList"),
        ("RemoteKVMDevice-MIB", "fileName"))
)
if mibBuilder.loadTexts:
    raritanMibBasicGroup.setStatus("current")


# Notification objects

rebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 1)
)
rebootStarted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"))
)
if mibBuilder.loadTexts:
    rebootStarted.setStatus(
        "current"
    )

rebootCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 2)
)
rebootCompleted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
)
if mibBuilder.loadTexts:
    rebootCompleted.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 3)
)
userLogin.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 4)
)
userLogout.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

userAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 5)
)
userAuthenticationFailure.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailure.setStatus(
        "current"
    )

portConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 6)
)
portConnect.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portName"))
)
if mibBuilder.loadTexts:
    portConnect.setStatus(
        "current"
    )

portDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 7)
)
portDisconnect.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portName"))
)
if mibBuilder.loadTexts:
    portDisconnect.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 8)
)
userSessionTimeout.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 9)
)
userConnectionLost.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userConnectionLost.setStatus(
        "current"
    )

portStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 10)
)
portStatusChange.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "deviceName"),
        ("RemoteKVMDevice-MIB", "portName"),
        ("RemoteKVMDevice-MIB", "portStatus"))
)
if mibBuilder.loadTexts:
    portStatusChange.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 11)
)
userAdded.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 12)
)
userModified.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 13)
)
userDeleted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

groupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 14)
)
groupAdded.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupAdded.setStatus(
        "current"
    )

groupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 15)
)
groupModified.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupModified.setStatus(
        "current"
    )

groupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 16)
)
groupDeleted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupDeleted.setStatus(
        "current"
    )

startCCManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 17)
)
startCCManagement.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    startCCManagement.setStatus(
        "current"
    )

stopCCManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 18)
)
stopCCManagement.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    stopCCManagement.setStatus(
        "current"
    )

factoryReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 19)
)
factoryReset.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    factoryReset.setStatus(
        "current"
    )

deviceUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 20)
)
deviceUpdateStarted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "imageVersion"))
)
if mibBuilder.loadTexts:
    deviceUpdateStarted.setStatus(
        "current"
    )

deviceUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 21)
)
deviceUpdateCompleted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "imageVersion"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    deviceUpdateCompleted.setStatus(
        "current"
    )

configBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 22)
)
configBackup.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "fileType"),
        ("RemoteKVMDevice-MIB", "fileVersion"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    configBackup.setStatus(
        "current"
    )

configRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 23)
)
configRestore.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "fileType"),
        ("RemoteKVMDevice-MIB", "fileVersion"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    configRestore.setStatus(
        "current"
    )

userPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 24)
)
userPasswordChanged.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "targetUser"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userPasswordChanged.setStatus(
        "current"
    )

powerNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 25)
)
powerNotification.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "outletName"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    powerNotification.setStatus(
        "current"
    )

networkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 26)
)
networkFailure.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "ethernetInterface"))
)
if mibBuilder.loadTexts:
    networkFailure.setStatus(
        "current"
    )

networkParameterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 27)
)
networkParameterChanged.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "remoteIpAddress"),
        ("RemoteKVMDevice-MIB", "oldIpAddress"),
        ("RemoteKVMDevice-MIB", "newIpAddress"),
        ("RemoteKVMDevice-MIB", "oldNetmask"),
        ("RemoteKVMDevice-MIB", "newNetmask"),
        ("RemoteKVMDevice-MIB", "newGateway"),
        ("RemoteKVMDevice-MIB", "oldGateway"))
)
if mibBuilder.loadTexts:
    networkParameterChanged.setStatus(
        "current"
    )

vmImageConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 28)
)
vmImageConnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    vmImageConnected.setStatus(
        "current"
    )

vmImageDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 29)
)
vmImageDisconnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    vmImageDisconnected.setStatus(
        "current"
    )

cimUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 30)
)
cimUpdateStarted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
)
if mibBuilder.loadTexts:
    cimUpdateStarted.setStatus(
        "current"
    )

cimUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 31)
)
cimUpdateCompleted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
)
if mibBuilder.loadTexts:
    cimUpdateCompleted.setStatus(
        "current"
    )

cimConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 32)
)
cimConnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "cimName"),
        ("RemoteKVMDevice-MIB", "serialNumber"),
        ("RemoteKVMDevice-MIB", "portNumber"))
)
if mibBuilder.loadTexts:
    cimConnected.setStatus(
        "current"
    )

cimDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 33)
)
cimDisconnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "cimName"),
        ("RemoteKVMDevice-MIB", "serialNumber"),
        ("RemoteKVMDevice-MIB", "portNumber"))
)
if mibBuilder.loadTexts:
    cimDisconnected.setStatus(
        "current"
    )

powerOutletNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 34)
)
powerOutletNotification.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "outletName"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    powerOutletNotification.setStatus(
        "current"
    )

portConnectionDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 35)
)
portConnectionDenied.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portName"))
)
if mibBuilder.loadTexts:
    portConnectionDenied.setStatus(
        "current"
    )

firmwareFileDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 36)
)
firmwareFileDiscarded.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareFileDiscarded.setStatus(
        "current"
    )

firmwareUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 37)
)
firmwareUpdateFailed.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareUpdateFailed.setStatus(
        "current"
    )

firmwareValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 38)
)
firmwareValidationFailed.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareValidationFailed.setStatus(
        "current"
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 39)
)
securityViolation.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        "current"
    )

deviceUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 40)
)
deviceUpdateFailed.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"))
)
if mibBuilder.loadTexts:
    deviceUpdateFailed.setStatus(
        "current"
    )

passwordSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 41)
)
passwordSettingsChanged.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    passwordSettingsChanged.setStatus(
        "current"
    )

ethernetFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 42)
)
ethernetFailover.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "restoredLanPort"))
)
if mibBuilder.loadTexts:
    ethernetFailover.setStatus(
        "current"
    )

ipConflictDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 43)
)
ipConflictDetected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "count"))
)
if mibBuilder.loadTexts:
    ipConflictDetected.setStatus(
        "current"
    )

ipConflictResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 44)
)
ipConflictResolved.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    ipConflictResolved.setStatus(
        "current"
    )

sxPortAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 45)
)
sxPortAlert.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "portNumber"),
        ("RemoteKVMDevice-MIB", "sxAlertString"))
)
if mibBuilder.loadTexts:
    sxPortAlert.setStatus(
        "current"
    )

pduConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 46)
)
pduConnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "portNumber"),
        ("RemoteKVMDevice-MIB", "pduName"))
)
if mibBuilder.loadTexts:
    pduConnected.setStatus(
        "current"
    )

pduDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 47)
)
pduDisconnected.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "portNumber"),
        ("RemoteKVMDevice-MIB", "pduName"))
)
if mibBuilder.loadTexts:
    pduDisconnected.setStatus(
        "current"
    )

networkParameterChangedv2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 48)
)
networkParameterChangedv2.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "remoteIpAddress"),
        ("RemoteKVMDevice-MIB", "changeEventText"))
)
if mibBuilder.loadTexts:
    networkParameterChangedv2.setStatus(
        "current"
    )

portConnectv2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 49)
)
portConnectv2.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    portConnectv2.setStatus(
        "current"
    )

portDisconnectv2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 50)
)
portDisconnectv2.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    portDisconnectv2.setStatus(
        "current"
    )

userForcedLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 51)
)
userForcedLogout.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userForcedLogout.setStatus(
        "current"
    )

userUploadedCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 52)
)
userUploadedCertificate.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "certificateAuthorityName"))
)
if mibBuilder.loadTexts:
    userUploadedCertificate.setStatus(
        "current"
    )

bladeChassisCommError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 53)
)
bladeChassisCommError.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "deviceName"),
        ("RemoteKVMDevice-MIB", "portNumber"),
        ("RemoteKVMDevice-MIB", "portName"))
)
if mibBuilder.loadTexts:
    bladeChassisCommError.setStatus(
        "current"
    )

setDateTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 54)
)
setDateTime.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "deviceName"),
        ("RemoteKVMDevice-MIB", "sysDateAndTime"))
)
if mibBuilder.loadTexts:
    setDateTime.setStatus(
        "current"
    )

setFIPSMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 55)
)
setFIPSMode.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "deviceName"),
        ("RemoteKVMDevice-MIB", "fipsModeStatus"))
)
if mibBuilder.loadTexts:
    setFIPSMode.setStatus(
        "current"
    )

securityBannerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 56)
)
securityBannerChanged.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "bannerChanges"))
)
if mibBuilder.loadTexts:
    securityBannerChanged.setStatus(
        "current"
    )

securityBannerAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 57)
)
securityBannerAction.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "bannerAction"))
)
if mibBuilder.loadTexts:
    securityBannerAction.setStatus(
        "current"
    )

scanStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 58)
)
scanStarted.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portList"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    scanStarted.setStatus(
        "current"
    )

scanStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 59)
)
scanStopped.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "portList"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    scanStopped.setStatus(
        "current"
    )

userDisconnectedFromPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 60)
)
userDisconnectedFromPort.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "targetUser"),
        ("RemoteKVMDevice-MIB", "portName"),
        ("RemoteKVMDevice-MIB", "userName"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"))
)
if mibBuilder.loadTexts:
    userDisconnectedFromPort.setStatus(
        "current"
    )

automaticScriptConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 3, 0, 61)
)
automaticScriptConfiguration.setObjects(
      *(("RemoteKVMDevice-MIB", "rcpObjectName"),
        ("RemoteKVMDevice-MIB", "rcpObjectInstance"),
        ("RemoteKVMDevice-MIB", "rcpIPAddress"),
        ("RemoteKVMDevice-MIB", "fileName"),
        ("RemoteKVMDevice-MIB", "status"))
)
if mibBuilder.loadTexts:
    automaticScriptConfiguration.setStatus(
        "current"
    )


# Notifications groups

raritanMibTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 2)
)
raritanMibTrapGroup.setObjects(
      *(("RemoteKVMDevice-MIB", "rebootStarted"),
        ("RemoteKVMDevice-MIB", "rebootCompleted"),
        ("RemoteKVMDevice-MIB", "userLogin"),
        ("RemoteKVMDevice-MIB", "userLogout"),
        ("RemoteKVMDevice-MIB", "userAuthenticationFailure"),
        ("RemoteKVMDevice-MIB", "portConnect"),
        ("RemoteKVMDevice-MIB", "portDisconnect"),
        ("RemoteKVMDevice-MIB", "userSessionTimeout"),
        ("RemoteKVMDevice-MIB", "userConnectionLost"),
        ("RemoteKVMDevice-MIB", "portStatusChange"),
        ("RemoteKVMDevice-MIB", "userAdded"),
        ("RemoteKVMDevice-MIB", "userModified"),
        ("RemoteKVMDevice-MIB", "userDeleted"),
        ("RemoteKVMDevice-MIB", "groupAdded"),
        ("RemoteKVMDevice-MIB", "groupModified"),
        ("RemoteKVMDevice-MIB", "groupDeleted"),
        ("RemoteKVMDevice-MIB", "startCCManagement"),
        ("RemoteKVMDevice-MIB", "stopCCManagement"),
        ("RemoteKVMDevice-MIB", "factoryReset"),
        ("RemoteKVMDevice-MIB", "deviceUpdateStarted"),
        ("RemoteKVMDevice-MIB", "deviceUpdateCompleted"),
        ("RemoteKVMDevice-MIB", "configBackup"),
        ("RemoteKVMDevice-MIB", "configRestore"),
        ("RemoteKVMDevice-MIB", "userPasswordChanged"),
        ("RemoteKVMDevice-MIB", "powerNotification"),
        ("RemoteKVMDevice-MIB", "networkFailure"),
        ("RemoteKVMDevice-MIB", "networkParameterChanged"),
        ("RemoteKVMDevice-MIB", "vmImageConnected"),
        ("RemoteKVMDevice-MIB", "vmImageDisconnected"),
        ("RemoteKVMDevice-MIB", "cimUpdateStarted"),
        ("RemoteKVMDevice-MIB", "cimUpdateCompleted"),
        ("RemoteKVMDevice-MIB", "cimConnected"),
        ("RemoteKVMDevice-MIB", "cimDisconnected"),
        ("RemoteKVMDevice-MIB", "powerOutletNotification"),
        ("RemoteKVMDevice-MIB", "portConnectionDenied"),
        ("RemoteKVMDevice-MIB", "firmwareFileDiscarded"),
        ("RemoteKVMDevice-MIB", "firmwareUpdateFailed"),
        ("RemoteKVMDevice-MIB", "firmwareValidationFailed"),
        ("RemoteKVMDevice-MIB", "securityViolation"),
        ("RemoteKVMDevice-MIB", "deviceUpdateFailed"),
        ("RemoteKVMDevice-MIB", "passwordSettingsChanged"),
        ("RemoteKVMDevice-MIB", "ethernetFailover"),
        ("RemoteKVMDevice-MIB", "ipConflictDetected"),
        ("RemoteKVMDevice-MIB", "ipConflictResolved"),
        ("RemoteKVMDevice-MIB", "sxPortAlert"),
        ("RemoteKVMDevice-MIB", "pduConnected"),
        ("RemoteKVMDevice-MIB", "pduDisconnected"),
        ("RemoteKVMDevice-MIB", "networkParameterChangedv2"),
        ("RemoteKVMDevice-MIB", "portConnectv2"),
        ("RemoteKVMDevice-MIB", "portDisconnectv2"),
        ("RemoteKVMDevice-MIB", "userForcedLogout"),
        ("RemoteKVMDevice-MIB", "userUploadedCertificate"),
        ("RemoteKVMDevice-MIB", "bladeChassisCommError"),
        ("RemoteKVMDevice-MIB", "setDateTime"),
        ("RemoteKVMDevice-MIB", "setFIPSMode"),
        ("RemoteKVMDevice-MIB", "securityBannerChanged"),
        ("RemoteKVMDevice-MIB", "securityBannerAction"),
        ("RemoteKVMDevice-MIB", "scanStarted"),
        ("RemoteKVMDevice-MIB", "scanStopped"),
        ("RemoteKVMDevice-MIB", "userDisconnectedFromPort"),
        ("RemoteKVMDevice-MIB", "automaticScriptConfiguration"))
)
if mibBuilder.loadTexts:
    raritanMibTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

raritanMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 1)
)
if mibBuilder.loadTexts:
    raritanMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RemoteKVMDevice-MIB",
    **{"raritan": raritan,
       "remoteKVMDevice": remoteKVMDevice,
       "remoteKVMDeviceNotifications": remoteKVMDeviceNotifications,
       "rebootStarted": rebootStarted,
       "rebootCompleted": rebootCompleted,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "userAuthenticationFailure": userAuthenticationFailure,
       "portConnect": portConnect,
       "portDisconnect": portDisconnect,
       "userSessionTimeout": userSessionTimeout,
       "userConnectionLost": userConnectionLost,
       "portStatusChange": portStatusChange,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "groupAdded": groupAdded,
       "groupModified": groupModified,
       "groupDeleted": groupDeleted,
       "startCCManagement": startCCManagement,
       "stopCCManagement": stopCCManagement,
       "factoryReset": factoryReset,
       "deviceUpdateStarted": deviceUpdateStarted,
       "deviceUpdateCompleted": deviceUpdateCompleted,
       "configBackup": configBackup,
       "configRestore": configRestore,
       "userPasswordChanged": userPasswordChanged,
       "powerNotification": powerNotification,
       "networkFailure": networkFailure,
       "networkParameterChanged": networkParameterChanged,
       "vmImageConnected": vmImageConnected,
       "vmImageDisconnected": vmImageDisconnected,
       "cimUpdateStarted": cimUpdateStarted,
       "cimUpdateCompleted": cimUpdateCompleted,
       "cimConnected": cimConnected,
       "cimDisconnected": cimDisconnected,
       "powerOutletNotification": powerOutletNotification,
       "portConnectionDenied": portConnectionDenied,
       "firmwareFileDiscarded": firmwareFileDiscarded,
       "firmwareUpdateFailed": firmwareUpdateFailed,
       "firmwareValidationFailed": firmwareValidationFailed,
       "securityViolation": securityViolation,
       "deviceUpdateFailed": deviceUpdateFailed,
       "passwordSettingsChanged": passwordSettingsChanged,
       "ethernetFailover": ethernetFailover,
       "ipConflictDetected": ipConflictDetected,
       "ipConflictResolved": ipConflictResolved,
       "sxPortAlert": sxPortAlert,
       "pduConnected": pduConnected,
       "pduDisconnected": pduDisconnected,
       "networkParameterChangedv2": networkParameterChangedv2,
       "portConnectv2": portConnectv2,
       "portDisconnectv2": portDisconnectv2,
       "userForcedLogout": userForcedLogout,
       "userUploadedCertificate": userUploadedCertificate,
       "bladeChassisCommError": bladeChassisCommError,
       "setDateTime": setDateTime,
       "setFIPSMode": setFIPSMode,
       "securityBannerChanged": securityBannerChanged,
       "securityBannerAction": securityBannerAction,
       "scanStarted": scanStarted,
       "scanStopped": scanStopped,
       "userDisconnectedFromPort": userDisconnectedFromPort,
       "automaticScriptConfiguration": automaticScriptConfiguration,
       "rcpObjectProductVersion": rcpObjectProductVersion,
       "rcpObjectName": rcpObjectName,
       "rcpObjectInstance": rcpObjectInstance,
       "userName": userName,
       "targetUser": targetUser,
       "groupName": groupName,
       "rcpIPAddress": rcpIPAddress,
       "deviceName": deviceName,
       "portStatus": portStatus,
       "portName": portName,
       "clusterID": clusterID,
       "ipPort": ipPort,
       "resetType": resetType,
       "interface": interface,
       "ethernetInterface": ethernetInterface,
       "backupRestoreAction": backupRestoreAction,
       "imageType": imageType,
       "imageVersion": imageVersion,
       "status": status,
       "fileVersion": fileVersion,
       "fileType": fileType,
       "outletName": outletName,
       "portNumber": portNumber,
       "serialNumber": serialNumber,
       "cimName": cimName,
       "count": count,
       "restoredLanPort": restoredLanPort,
       "remoteIpAddress": remoteIpAddress,
       "oldIpAddress": oldIpAddress,
       "newIpAddress": newIpAddress,
       "newNetmask": newNetmask,
       "oldNetmask": oldNetmask,
       "oldGateway": oldGateway,
       "newGateway": newGateway,
       "sxAlertString": sxAlertString,
       "pduName": pduName,
       "changeEventText": changeEventText,
       "certificateAuthorityName": certificateAuthorityName,
       "sysDateAndTime": sysDateAndTime,
       "fipsModeStatus": fipsModeStatus,
       "bannerChanges": bannerChanges,
       "bannerAction": bannerAction,
       "portList": portList,
       "fileName": fileName,
       "raritanMibConformance": raritanMibConformance,
       "raritanMibCompliances": raritanMibCompliances,
       "raritanMibCompliance": raritanMibCompliance,
       "raritanMibGroups": raritanMibGroups,
       "raritanMibBasicGroup": raritanMibBasicGroup,
       "raritanMibTrapGroup": raritanMibTrapGroup}
)
