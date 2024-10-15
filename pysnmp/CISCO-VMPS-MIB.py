# SNMP MIB module (CISCO-VMPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VMPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:10 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVmpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53)
)
ciscoVmpsMIB.setRevisions(
        ("2004-01-20 00:00",
         "2003-10-16 10:00",
         "2002-06-19 10:00",
         "2002-04-04 10:00",
         "2001-01-30 13:04")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVlanMemberPolicyServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVlanMemberPolicyServerMIBObjects = _CiscoVlanMemberPolicyServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1)
)
_VmpsInfo_ObjectIdentity = ObjectIdentity
vmpsInfo = _VmpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1)
)
_VmpsConfigTable_Object = MibTable
vmpsConfigTable = _VmpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vmpsConfigTable.setStatus("current")
_VmpsConfigEntry_Object = MibTableRow
vmpsConfigEntry = _VmpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1)
)
vmpsConfigEntry.setIndexNames(
    (0, "CISCO-VMPS-MIB", "vmpsIndex"),
)
if mibBuilder.loadTexts:
    vmpsConfigEntry.setStatus("current")


class _VmpsIndex_Type(Integer32):
    """Custom type vmpsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmpsIndex_Type.__name__ = "Integer32"
_VmpsIndex_Object = MibTableColumn
vmpsIndex = _VmpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 1),
    _VmpsIndex_Type()
)
vmpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmpsIndex.setStatus("current")


class _VmpsAdminStatus_Type(Integer32):
    """Custom type vmpsAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VmpsAdminStatus_Type.__name__ = "Integer32"
_VmpsAdminStatus_Object = MibTableColumn
vmpsAdminStatus = _VmpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 2),
    _VmpsAdminStatus_Type()
)
vmpsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsAdminStatus.setStatus("current")


class _VmpsDownloadServerAddress_Type(IpAddress):
    """Custom type vmpsDownloadServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VmpsDownloadServerAddress_Object = MibTableColumn
vmpsDownloadServerAddress = _VmpsDownloadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 3),
    _VmpsDownloadServerAddress_Type()
)
vmpsDownloadServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsDownloadServerAddress.setStatus("current")


class _VmpsConfigFileName_Type(DisplayString):
    """Custom type vmpsConfigFileName based on DisplayString"""
    defaultHexValue = ""


_VmpsConfigFileName_Object = MibTableColumn
vmpsConfigFileName = _VmpsConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 4),
    _VmpsConfigFileName_Type()
)
vmpsConfigFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsConfigFileName.setStatus("current")


class _VmpsTriggerDownload_Type(Integer32):
    """Custom type vmpsTriggerDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadDatabase", 2),
          ("loadRcpDataBase", 3),
          ("noOperation", 1))
    )


_VmpsTriggerDownload_Type.__name__ = "Integer32"
_VmpsTriggerDownload_Object = MibTableColumn
vmpsTriggerDownload = _VmpsTriggerDownload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 5),
    _VmpsTriggerDownload_Type()
)
vmpsTriggerDownload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsTriggerDownload.setStatus("current")


class _VmpsFallbackVlan_Type(VlanName):
    """Custom type vmpsFallbackVlan based on VlanName"""
    defaultHexValue = ""


_VmpsFallbackVlan_Object = MibTableColumn
vmpsFallbackVlan = _VmpsFallbackVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 6),
    _VmpsFallbackVlan_Type()
)
vmpsFallbackVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsFallbackVlan.setStatus("current")


class _VmpsSecureMode_Type(Integer32):
    """Custom type vmpsSecureMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 2),
          ("secure", 1))
    )


_VmpsSecureMode_Type.__name__ = "Integer32"
_VmpsSecureMode_Object = MibTableColumn
vmpsSecureMode = _VmpsSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 7),
    _VmpsSecureMode_Type()
)
vmpsSecureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsSecureMode.setStatus("current")


class _VmpsManagementDomain_Type(DisplayString):
    """Custom type vmpsManagementDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VmpsManagementDomain_Type.__name__ = "DisplayString"
_VmpsManagementDomain_Object = MibTableColumn
vmpsManagementDomain = _VmpsManagementDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 8),
    _VmpsManagementDomain_Type()
)
vmpsManagementDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsManagementDomain.setStatus("current")
_VmpsRowStatus_Type = RowStatus
_VmpsRowStatus_Object = MibTableColumn
vmpsRowStatus = _VmpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 9),
    _VmpsRowStatus_Type()
)
vmpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsRowStatus.setStatus("current")


class _VmpsRcpRemoteUserName_Type(SnmpAdminString):
    """Custom type vmpsRcpRemoteUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_VmpsRcpRemoteUserName_Type.__name__ = "SnmpAdminString"
_VmpsRcpRemoteUserName_Object = MibTableColumn
vmpsRcpRemoteUserName = _VmpsRcpRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 10),
    _VmpsRcpRemoteUserName_Type()
)
vmpsRcpRemoteUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsRcpRemoteUserName.setStatus("deprecated")
_VmpsRcpRemoteUserName2_Type = SnmpAdminString
_VmpsRcpRemoteUserName2_Object = MibTableColumn
vmpsRcpRemoteUserName2 = _VmpsRcpRemoteUserName2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 1, 1, 11),
    _VmpsRcpRemoteUserName2_Type()
)
vmpsRcpRemoteUserName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsRcpRemoteUserName2.setStatus("current")
_VmpsStatsTable_Object = MibTable
vmpsStatsTable = _VmpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vmpsStatsTable.setStatus("current")
_VmpsStatsEntry_Object = MibTableRow
vmpsStatsEntry = _VmpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vmpsStatsEntry.setStatus("current")
_VmpsLastRestart_Type = TimeStamp
_VmpsLastRestart_Object = MibTableColumn
vmpsLastRestart = _VmpsLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 1),
    _VmpsLastRestart_Type()
)
vmpsLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsLastRestart.setStatus("current")
_VmpsInConfigReqs_Type = Counter32
_VmpsInConfigReqs_Object = MibTableColumn
vmpsInConfigReqs = _VmpsInConfigReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 2),
    _VmpsInConfigReqs_Type()
)
vmpsInConfigReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsInConfigReqs.setStatus("current")
_VmpsInConfigErrors_Type = Counter32
_VmpsInConfigErrors_Object = MibTableColumn
vmpsInConfigErrors = _VmpsInConfigErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 3),
    _VmpsInConfigErrors_Type()
)
vmpsInConfigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsInConfigErrors.setStatus("current")
_VmpsOutConfigFails_Type = Counter32
_VmpsOutConfigFails_Object = MibTableColumn
vmpsOutConfigFails = _VmpsOutConfigFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 4),
    _VmpsOutConfigFails_Type()
)
vmpsOutConfigFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsOutConfigFails.setStatus("current")
_VmpsLastFailClient_Type = MacAddress
_VmpsLastFailClient_Object = MibTableColumn
vmpsLastFailClient = _VmpsLastFailClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 5),
    _VmpsLastFailClient_Type()
)
vmpsLastFailClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsLastFailClient.setStatus("current")


class _VmpsOperStatus_Type(Integer32):
    """Custom type vmpsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("loading", 3))
    )


_VmpsOperStatus_Type.__name__ = "Integer32"
_VmpsOperStatus_Object = MibTableColumn
vmpsOperStatus = _VmpsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 1, 2, 1, 6),
    _VmpsOperStatus_Type()
)
vmpsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsOperStatus.setStatus("current")
_VmpsDatabase_ObjectIdentity = ObjectIdentity
vmpsDatabase = _VmpsDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2)
)
_VmpsMacConfigTable_Object = MibTable
vmpsMacConfigTable = _VmpsMacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vmpsMacConfigTable.setStatus("current")
_VmpsMacConfigEntry_Object = MibTableRow
vmpsMacConfigEntry = _VmpsMacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1)
)
vmpsMacConfigEntry.setIndexNames(
    (0, "CISCO-VMPS-MIB", "vmpsIndex"),
    (0, "CISCO-VMPS-MIB", "vmpsMacConfigAddress"),
)
if mibBuilder.loadTexts:
    vmpsMacConfigEntry.setStatus("current")
_VmpsMacConfigAddress_Type = MacAddress
_VmpsMacConfigAddress_Object = MibTableColumn
vmpsMacConfigAddress = _VmpsMacConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 1),
    _VmpsMacConfigAddress_Type()
)
vmpsMacConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmpsMacConfigAddress.setStatus("current")
_VmpsMacConfigVlan_Type = VlanName
_VmpsMacConfigVlan_Object = MibTableColumn
vmpsMacConfigVlan = _VmpsMacConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 2),
    _VmpsMacConfigVlan_Type()
)
vmpsMacConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsMacConfigVlan.setStatus("current")
_VmpsMacConfigLastAccessed_Type = TimeStamp
_VmpsMacConfigLastAccessed_Object = MibTableColumn
vmpsMacConfigLastAccessed = _VmpsMacConfigLastAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 3),
    _VmpsMacConfigLastAccessed_Type()
)
vmpsMacConfigLastAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsMacConfigLastAccessed.setStatus("current")
_VmpsMacConfigLastRequestor_Type = IpAddress
_VmpsMacConfigLastRequestor_Object = MibTableColumn
vmpsMacConfigLastRequestor = _VmpsMacConfigLastRequestor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 4),
    _VmpsMacConfigLastRequestor_Type()
)
vmpsMacConfigLastRequestor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsMacConfigLastRequestor.setStatus("current")
_VmpsMacConfigLastRequestPortId_Type = DisplayString
_VmpsMacConfigLastRequestPortId_Object = MibTableColumn
vmpsMacConfigLastRequestPortId = _VmpsMacConfigLastRequestPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 5),
    _VmpsMacConfigLastRequestPortId_Type()
)
vmpsMacConfigLastRequestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsMacConfigLastRequestPortId.setStatus("current")


class _VmpsMacConfigLastResponseStatus_Type(Integer32):
    """Custom type vmpsMacConfigLastResponseStatus based on Integer32"""
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
        *(("accessDenied", 4),
          ("insufficientResources", 3),
          ("portShutdown", 5),
          ("success", 1),
          ("unknownManagementDomain", 6),
          ("versionNotSupported", 2))
    )


_VmpsMacConfigLastResponseStatus_Type.__name__ = "Integer32"
_VmpsMacConfigLastResponseStatus_Object = MibTableColumn
vmpsMacConfigLastResponseStatus = _VmpsMacConfigLastResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 6),
    _VmpsMacConfigLastResponseStatus_Type()
)
vmpsMacConfigLastResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsMacConfigLastResponseStatus.setStatus("current")
_VmpsMacConfigStatus_Type = RowStatus
_VmpsMacConfigStatus_Object = MibTableColumn
vmpsMacConfigStatus = _VmpsMacConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 1, 1, 7),
    _VmpsMacConfigStatus_Type()
)
vmpsMacConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsMacConfigStatus.setStatus("current")
_VmpsVlanConfigTable_Object = MibTable
vmpsVlanConfigTable = _VmpsVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vmpsVlanConfigTable.setStatus("current")
_VmpsVlanConfigEntry_Object = MibTableRow
vmpsVlanConfigEntry = _VmpsVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2, 1)
)
vmpsVlanConfigEntry.setIndexNames(
    (0, "CISCO-VMPS-MIB", "vmpsIndex"),
    (0, "CISCO-VMPS-MIB", "vmpsVlanName"),
    (0, "CISCO-VMPS-MIB", "vmpsDeviceId"),
    (0, "CISCO-VMPS-MIB", "vmpsPortName"),
)
if mibBuilder.loadTexts:
    vmpsVlanConfigEntry.setStatus("current")
_VmpsVlanName_Type = VlanName
_VmpsVlanName_Object = MibTableColumn
vmpsVlanName = _VmpsVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2, 1, 1),
    _VmpsVlanName_Type()
)
vmpsVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmpsVlanName.setStatus("current")
_VmpsDeviceId_Type = IpAddress
_VmpsDeviceId_Object = MibTableColumn
vmpsDeviceId = _VmpsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2, 1, 2),
    _VmpsDeviceId_Type()
)
vmpsDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmpsDeviceId.setStatus("current")
_VmpsPortName_Type = DisplayString
_VmpsPortName_Object = MibTableColumn
vmpsPortName = _VmpsPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2, 1, 3),
    _VmpsPortName_Type()
)
vmpsPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmpsPortName.setStatus("current")
_VmpsVlanConfigStatus_Type = RowStatus
_VmpsVlanConfigStatus_Object = MibTableColumn
vmpsVlanConfigStatus = _VmpsVlanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 2, 2, 1, 4),
    _VmpsVlanConfigStatus_Type()
)
vmpsVlanConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsVlanConfigStatus.setStatus("current")
_VmpsGlobalConfig_ObjectIdentity = ObjectIdentity
vmpsGlobalConfig = _VmpsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 3)
)
_VmpsAutoBackupEnable_Type = TruthValue
_VmpsAutoBackupEnable_Object = MibScalar
vmpsAutoBackupEnable = _VmpsAutoBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 3, 1),
    _VmpsAutoBackupEnable_Type()
)
vmpsAutoBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmpsAutoBackupEnable.setStatus("current")
_VmpsAutoBackupFileName_Type = SnmpAdminString
_VmpsAutoBackupFileName_Object = MibScalar
vmpsAutoBackupFileName = _VmpsAutoBackupFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 1, 3, 2),
    _VmpsAutoBackupFileName_Type()
)
vmpsAutoBackupFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmpsAutoBackupFileName.setStatus("current")
_CiscoVlanMemberPolicyServerMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoVlanMemberPolicyServerMIBNotifications = _CiscoVlanMemberPolicyServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 2)
)
_CiscoVlanMemberPolicyServerMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVlanMemberPolicyServerMIBConformance = _CiscoVlanMemberPolicyServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3)
)
_CiscoVlanMemberPolicyServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVlanMemberPolicyServerMIBCompliances = _CiscoVlanMemberPolicyServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 1)
)
_CiscoVlanMemberPolicyServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVlanMemberPolicyServerMIBGroups = _CiscoVlanMemberPolicyServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 2)
)
vmpsConfigEntry.registerAugmentions(
    ("CISCO-VMPS-MIB",
     "vmpsStatsEntry")
)
vmpsStatsEntry.setIndexNames(*vmpsConfigEntry.getIndexNames())

# Managed Objects groups

ciscoVlanMemberPolicyServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 2, 1)
)
ciscoVlanMemberPolicyServerGroup.setObjects(
      *(("CISCO-VMPS-MIB", "vmpsLastRestart"),
        ("CISCO-VMPS-MIB", "vmpsInConfigReqs"),
        ("CISCO-VMPS-MIB", "vmpsInConfigErrors"),
        ("CISCO-VMPS-MIB", "vmpsOutConfigFails"),
        ("CISCO-VMPS-MIB", "vmpsLastFailClient"),
        ("CISCO-VMPS-MIB", "vmpsOperStatus"),
        ("CISCO-VMPS-MIB", "vmpsAdminStatus"),
        ("CISCO-VMPS-MIB", "vmpsDownloadServerAddress"),
        ("CISCO-VMPS-MIB", "vmpsConfigFileName"),
        ("CISCO-VMPS-MIB", "vmpsTriggerDownload"),
        ("CISCO-VMPS-MIB", "vmpsFallbackVlan"),
        ("CISCO-VMPS-MIB", "vmpsSecureMode"),
        ("CISCO-VMPS-MIB", "vmpsManagementDomain"),
        ("CISCO-VMPS-MIB", "vmpsRowStatus"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigVlan"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigLastAccessed"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigLastRequestor"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigLastRequestPortId"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigLastResponseStatus"),
        ("CISCO-VMPS-MIB", "vmpsMacConfigStatus"),
        ("CISCO-VMPS-MIB", "vmpsVlanConfigStatus"))
)
if mibBuilder.loadTexts:
    ciscoVlanMemberPolicyServerGroup.setStatus("current")

ciscoVlanMemberPolicyServerRcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 2, 2)
)
ciscoVlanMemberPolicyServerRcpGroup.setObjects(
    ("CISCO-VMPS-MIB", "vmpsRcpRemoteUserName")
)
if mibBuilder.loadTexts:
    ciscoVlanMemberPolicyServerRcpGroup.setStatus("deprecated")

ciscoVmpsAutoBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 2, 3)
)
ciscoVmpsAutoBackupGroup.setObjects(
      *(("CISCO-VMPS-MIB", "vmpsAutoBackupEnable"),
        ("CISCO-VMPS-MIB", "vmpsAutoBackupFileName"))
)
if mibBuilder.loadTexts:
    ciscoVmpsAutoBackupGroup.setStatus("current")

ciscoVlanMemberPolicyServerRcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 2, 4)
)
ciscoVlanMemberPolicyServerRcpGroup2.setObjects(
    ("CISCO-VMPS-MIB", "vmpsRcpRemoteUserName2")
)
if mibBuilder.loadTexts:
    ciscoVlanMemberPolicyServerRcpGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVlanMemberPolicyServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVlanMemberPolicyServerMIBCompliance.setStatus(
        "deprecated"
    )

ciscoVmpsMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVmpsMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoVmpsMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 53, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoVmpsMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VMPS-MIB",
    **{"VlanName": VlanName,
       "ciscoVmpsMIB": ciscoVmpsMIB,
       "ciscoVlanMemberPolicyServerMIBObjects": ciscoVlanMemberPolicyServerMIBObjects,
       "vmpsInfo": vmpsInfo,
       "vmpsConfigTable": vmpsConfigTable,
       "vmpsConfigEntry": vmpsConfigEntry,
       "vmpsIndex": vmpsIndex,
       "vmpsAdminStatus": vmpsAdminStatus,
       "vmpsDownloadServerAddress": vmpsDownloadServerAddress,
       "vmpsConfigFileName": vmpsConfigFileName,
       "vmpsTriggerDownload": vmpsTriggerDownload,
       "vmpsFallbackVlan": vmpsFallbackVlan,
       "vmpsSecureMode": vmpsSecureMode,
       "vmpsManagementDomain": vmpsManagementDomain,
       "vmpsRowStatus": vmpsRowStatus,
       "vmpsRcpRemoteUserName": vmpsRcpRemoteUserName,
       "vmpsRcpRemoteUserName2": vmpsRcpRemoteUserName2,
       "vmpsStatsTable": vmpsStatsTable,
       "vmpsStatsEntry": vmpsStatsEntry,
       "vmpsLastRestart": vmpsLastRestart,
       "vmpsInConfigReqs": vmpsInConfigReqs,
       "vmpsInConfigErrors": vmpsInConfigErrors,
       "vmpsOutConfigFails": vmpsOutConfigFails,
       "vmpsLastFailClient": vmpsLastFailClient,
       "vmpsOperStatus": vmpsOperStatus,
       "vmpsDatabase": vmpsDatabase,
       "vmpsMacConfigTable": vmpsMacConfigTable,
       "vmpsMacConfigEntry": vmpsMacConfigEntry,
       "vmpsMacConfigAddress": vmpsMacConfigAddress,
       "vmpsMacConfigVlan": vmpsMacConfigVlan,
       "vmpsMacConfigLastAccessed": vmpsMacConfigLastAccessed,
       "vmpsMacConfigLastRequestor": vmpsMacConfigLastRequestor,
       "vmpsMacConfigLastRequestPortId": vmpsMacConfigLastRequestPortId,
       "vmpsMacConfigLastResponseStatus": vmpsMacConfigLastResponseStatus,
       "vmpsMacConfigStatus": vmpsMacConfigStatus,
       "vmpsVlanConfigTable": vmpsVlanConfigTable,
       "vmpsVlanConfigEntry": vmpsVlanConfigEntry,
       "vmpsVlanName": vmpsVlanName,
       "vmpsDeviceId": vmpsDeviceId,
       "vmpsPortName": vmpsPortName,
       "vmpsVlanConfigStatus": vmpsVlanConfigStatus,
       "vmpsGlobalConfig": vmpsGlobalConfig,
       "vmpsAutoBackupEnable": vmpsAutoBackupEnable,
       "vmpsAutoBackupFileName": vmpsAutoBackupFileName,
       "ciscoVlanMemberPolicyServerMIBNotifications": ciscoVlanMemberPolicyServerMIBNotifications,
       "ciscoVlanMemberPolicyServerMIBConformance": ciscoVlanMemberPolicyServerMIBConformance,
       "ciscoVlanMemberPolicyServerMIBCompliances": ciscoVlanMemberPolicyServerMIBCompliances,
       "ciscoVlanMemberPolicyServerMIBCompliance": ciscoVlanMemberPolicyServerMIBCompliance,
       "ciscoVmpsMIBCompliance2": ciscoVmpsMIBCompliance2,
       "ciscoVmpsMIBCompliance3": ciscoVmpsMIBCompliance3,
       "ciscoVlanMemberPolicyServerMIBGroups": ciscoVlanMemberPolicyServerMIBGroups,
       "ciscoVlanMemberPolicyServerGroup": ciscoVlanMemberPolicyServerGroup,
       "ciscoVlanMemberPolicyServerRcpGroup": ciscoVlanMemberPolicyServerRcpGroup,
       "ciscoVmpsAutoBackupGroup": ciscoVmpsAutoBackupGroup,
       "ciscoVlanMemberPolicyServerRcpGroup2": ciscoVlanMemberPolicyServerRcpGroup2}
)
