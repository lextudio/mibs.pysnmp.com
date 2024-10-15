# SNMP MIB module (RARITANCCv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RARITANCCv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:46 2024
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
 internet,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "internet",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2011-04-11 11:08",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 1)
)
_EnterpriseManagement_ObjectIdentity = ObjectIdentity
enterpriseManagement = _EnterpriseManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1)
)
_CommandCenter_ObjectIdentity = ObjectIdentity
commandCenter = _CommandCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1)
)
_CcObject_ObjectIdentity = ObjectIdentity
ccObject = _CcObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0)
)
_CcObjectName_Type = DisplayString
_CcObjectName_Object = MibScalar
ccObjectName = _CcObjectName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 1),
    _CcObjectName_Type()
)
ccObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccObjectName.setStatus("current")
_CcObjectInstance_Type = DisplayString
_CcObjectInstance_Object = MibScalar
ccObjectInstance = _CcObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 2),
    _CcObjectInstance_Type()
)
ccObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccObjectInstance.setStatus("current")
_CcUserName_Type = DisplayString
_CcUserName_Object = MibScalar
ccUserName = _CcUserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 3),
    _CcUserName_Type()
)
ccUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserName.setStatus("current")
_CcUserSessionId_Type = DisplayString
_CcUserSessionId_Object = MibScalar
ccUserSessionId = _CcUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 4),
    _CcUserSessionId_Type()
)
ccUserSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserSessionId.setStatus("current")
_CcUserNameInitiated_Type = DisplayString
_CcUserNameInitiated_Object = MibScalar
ccUserNameInitiated = _CcUserNameInitiated_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 5),
    _CcUserNameInitiated_Type()
)
ccUserNameInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserNameInitiated.setStatus("current")
_CcUserNameTerminated_Type = DisplayString
_CcUserNameTerminated_Object = MibScalar
ccUserNameTerminated = _CcUserNameTerminated_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 6),
    _CcUserNameTerminated_Type()
)
ccUserNameTerminated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserNameTerminated.setStatus("current")
_CcImageType_Type = DisplayString
_CcImageType_Object = MibScalar
ccImageType = _CcImageType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 7),
    _CcImageType_Type()
)
ccImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccImageType.setStatus("current")
_CcImageVersion_Type = DisplayString
_CcImageVersion_Object = MibScalar
ccImageVersion = _CcImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 8),
    _CcImageVersion_Type()
)
ccImageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccImageVersion.setStatus("current")


class _CcImageVersionStatus_Type(Integer32):
    """Custom type ccImageVersionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_CcImageVersionStatus_Type.__name__ = "Integer32"
_CcImageVersionStatus_Object = MibScalar
ccImageVersionStatus = _CcImageVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 9),
    _CcImageVersionStatus_Type()
)
ccImageVersionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccImageVersionStatus.setStatus("current")
_CcUserWhoAdded_Type = DisplayString
_CcUserWhoAdded_Object = MibScalar
ccUserWhoAdded = _CcUserWhoAdded_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 10),
    _CcUserWhoAdded_Type()
)
ccUserWhoAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserWhoAdded.setStatus("current")
_CcUserWhoDeleted_Type = DisplayString
_CcUserWhoDeleted_Object = MibScalar
ccUserWhoDeleted = _CcUserWhoDeleted_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 11),
    _CcUserWhoDeleted_Type()
)
ccUserWhoDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserWhoDeleted.setStatus("current")
_CcUserWhoModified_Type = DisplayString
_CcUserWhoModified_Object = MibScalar
ccUserWhoModified = _CcUserWhoModified_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 12),
    _CcUserWhoModified_Type()
)
ccUserWhoModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserWhoModified.setStatus("current")
_CcNodeName_Type = DisplayString
_CcNodeName_Object = MibScalar
ccNodeName = _CcNodeName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 13),
    _CcNodeName_Type()
)
ccNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNodeName.setStatus("current")


class _CcLanCard_Type(Integer32):
    """Custom type ccLanCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_CcLanCard_Type.__name__ = "Integer32"
_CcLanCard_Object = MibScalar
ccLanCard = _CcLanCard_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 14),
    _CcLanCard_Type()
)
ccLanCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanCard.setStatus("current")


class _CcHardDisk_Type(Integer32):
    """Custom type ccHardDisk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_CcHardDisk_Type.__name__ = "Integer32"
_CcHardDisk_Object = MibScalar
ccHardDisk = _CcHardDisk_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 15),
    _CcHardDisk_Type()
)
ccHardDisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHardDisk.setStatus("current")


class _CcSessionType_Type(Integer32):
    """Custom type ccSessionType based on Integer32"""
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
        *(("admin", 4),
          ("diagnostics", 5),
          ("kvm", 2),
          ("powerOutlet", 3),
          ("serial", 1))
    )


_CcSessionType_Type.__name__ = "Integer32"
_CcSessionType_Object = MibScalar
ccSessionType = _CcSessionType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 16),
    _CcSessionType_Type()
)
ccSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSessionType.setStatus("current")


class _CcClusterState_Type(Integer32):
    """Custom type ccClusterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("standAlone", 3))
    )


_CcClusterState_Type.__name__ = "Integer32"
_CcClusterState_Object = MibScalar
ccClusterState = _CcClusterState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 17),
    _CcClusterState_Type()
)
ccClusterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClusterState.setStatus("current")
_CcLeafNodeName_Type = DisplayString
_CcLeafNodeName_Object = MibScalar
ccLeafNodeName = _CcLeafNodeName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 18),
    _CcLeafNodeName_Type()
)
ccLeafNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLeafNodeName.setStatus("current")
_CcLeafNodeIPAddress_Type = DisplayString
_CcLeafNodeIPAddress_Object = MibScalar
ccLeafNodeIPAddress = _CcLeafNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 19),
    _CcLeafNodeIPAddress_Type()
)
ccLeafNodeIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLeafNodeIPAddress.setStatus("current")
_CcLeafNodeFirmwareVersion_Type = DisplayString
_CcLeafNodeFirmwareVersion_Object = MibScalar
ccLeafNodeFirmwareVersion = _CcLeafNodeFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 20),
    _CcLeafNodeFirmwareVersion_Type()
)
ccLeafNodeFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLeafNodeFirmwareVersion.setStatus("current")
_CcScheduledTaskDescription_Type = DisplayString
_CcScheduledTaskDescription_Object = MibScalar
ccScheduledTaskDescription = _CcScheduledTaskDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 21),
    _CcScheduledTaskDescription_Type()
)
ccScheduledTaskDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccScheduledTaskDescription.setStatus("current")
_CcScheduledTaskFailureReason_Type = DisplayString
_CcScheduledTaskFailureReason_Object = MibScalar
ccScheduledTaskFailureReason = _CcScheduledTaskFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 22),
    _CcScheduledTaskFailureReason_Type()
)
ccScheduledTaskFailureReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccScheduledTaskFailureReason.setStatus("current")
_CcDiagnosticConsoleMAX_ACCESSLevel_Type = DisplayString
_CcDiagnosticConsoleMAX_ACCESSLevel_Object = MibScalar
ccDiagnosticConsoleMAX_ACCESSLevel = _CcDiagnosticConsoleMAX_ACCESSLevel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 23),
    _CcDiagnosticConsoleMAX_ACCESSLevel_Type()
)
ccDiagnosticConsoleMAX_ACCESSLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDiagnosticConsoleMAX_ACCESSLevel.setStatus("current")
_CcDeviceName_Type = DisplayString
_CcDeviceName_Object = MibScalar
ccDeviceName = _CcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 24),
    _CcDeviceName_Type()
)
ccDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDeviceName.setStatus("current")
_CcUserGroupName_Type = DisplayString
_CcUserGroupName_Object = MibScalar
ccUserGroupName = _CcUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 25),
    _CcUserGroupName_Type()
)
ccUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserGroupName.setStatus("current")


class _CcBannerChanges_Type(Integer32):
    """Custom type ccBannerChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("modified", 3))
    )


_CcBannerChanges_Type.__name__ = "Integer32"
_CcBannerChanges_Object = MibScalar
ccBannerChanges = _CcBannerChanges_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 26),
    _CcBannerChanges_Type()
)
ccBannerChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccBannerChanges.setStatus("current")


class _CcMOTDChanges_Type(Integer32):
    """Custom type ccMOTDChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("modified", 3))
    )


_CcMOTDChanges_Type.__name__ = "Integer32"
_CcMOTDChanges_Object = MibScalar
ccMOTDChanges = _CcMOTDChanges_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 27),
    _CcMOTDChanges_Type()
)
ccMOTDChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMOTDChanges.setStatus("current")
_CcOldNumberOfOutlets_Type = DisplayString
_CcOldNumberOfOutlets_Object = MibScalar
ccOldNumberOfOutlets = _CcOldNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 28),
    _CcOldNumberOfOutlets_Type()
)
ccOldNumberOfOutlets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOldNumberOfOutlets.setStatus("current")
_CcNewNumberOfOutlets_Type = DisplayString
_CcNewNumberOfOutlets_Object = MibScalar
ccNewNumberOfOutlets = _CcNewNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 29),
    _CcNewNumberOfOutlets_Type()
)
ccNewNumberOfOutlets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNewNumberOfOutlets.setStatus("current")
_CcSystemMonitorNotificationLevel_Type = DisplayString
_CcSystemMonitorNotificationLevel_Object = MibScalar
ccSystemMonitorNotificationLevel = _CcSystemMonitorNotificationLevel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 30),
    _CcSystemMonitorNotificationLevel_Type()
)
ccSystemMonitorNotificationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemMonitorNotificationLevel.setStatus("current")
_CcSystemMonitorNotificationMessage_Type = DisplayString
_CcSystemMonitorNotificationMessage_Object = MibScalar
ccSystemMonitorNotificationMessage = _CcSystemMonitorNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 31),
    _CcSystemMonitorNotificationMessage_Type()
)
ccSystemMonitorNotificationMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemMonitorNotificationMessage.setStatus("current")
_CcDominionPXFirmwareVersion_Type = DisplayString
_CcDominionPXFirmwareVersion_Object = MibScalar
ccDominionPXFirmwareVersion = _CcDominionPXFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 32),
    _CcDominionPXFirmwareVersion_Type()
)
ccDominionPXFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDominionPXFirmwareVersion.setStatus("current")
_CcClusterPeer_Type = DisplayString
_CcClusterPeer_Object = MibScalar
ccClusterPeer = _CcClusterPeer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 33),
    _CcClusterPeer_Type()
)
ccClusterPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClusterPeer.setStatus("current")
_CcClusterOperation_Type = DisplayString
_CcClusterOperation_Object = MibScalar
ccClusterOperation = _CcClusterOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 34),
    _CcClusterOperation_Type()
)
ccClusterOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClusterOperation.setStatus("current")


class _CcClusterOperationStatus_Type(Integer32):
    """Custom type ccClusterOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_CcClusterOperationStatus_Type.__name__ = "Integer32"
_CcClusterOperationStatus_Object = MibScalar
ccClusterOperationStatus = _CcClusterOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 35),
    _CcClusterOperationStatus_Type()
)
ccClusterOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClusterOperationStatus.setStatus("current")


class _CcTransferOperation_Type(Integer32):
    """Custom type ccTransferOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 1),
          ("import", 2))
    )


_CcTransferOperation_Type.__name__ = "Integer32"
_CcTransferOperation_Object = MibScalar
ccTransferOperation = _CcTransferOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 36),
    _CcTransferOperation_Type()
)
ccTransferOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTransferOperation.setStatus("current")
_CcFileType_Type = DisplayString
_CcFileType_Object = MibScalar
ccFileType = _CcFileType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 37),
    _CcFileType_Type()
)
ccFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccFileType.setStatus("current")
_CcLicensedFeature_Type = DisplayString
_CcLicensedFeature_Object = MibScalar
ccLicensedFeature = _CcLicensedFeature_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 38),
    _CcLicensedFeature_Type()
)
ccLicensedFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLicensedFeature.setStatus("current")
_CcLicenseServer_Type = DisplayString
_CcLicenseServer_Object = MibScalar
ccLicenseServer = _CcLicenseServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 39),
    _CcLicenseServer_Type()
)
ccLicenseServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLicenseServer.setStatus("current")
_CcLicenseTerminatedReason_Type = DisplayString
_CcLicenseTerminatedReason_Object = MibScalar
ccLicenseTerminatedReason = _CcLicenseTerminatedReason_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 40),
    _CcLicenseTerminatedReason_Type()
)
ccLicenseTerminatedReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLicenseTerminatedReason.setStatus("current")
_CcPortName_Type = DisplayString
_CcPortName_Object = MibScalar
ccPortName = _CcPortName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 41),
    _CcPortName_Type()
)
ccPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortName.setStatus("current")
_CcNotify_ObjectIdentity = ObjectIdentity
ccNotify = _CcNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1)
)

# Managed Objects groups


# Notification objects

ccUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 1)
)
ccUnavailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccClusterState"))
)
if mibBuilder.loadTexts:
    ccUnavailable.setStatus(
        "current"
    )

ccAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 2)
)
ccAvailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccClusterState"))
)
if mibBuilder.loadTexts:
    ccAvailable.setStatus(
        "current"
    )

ccUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 3)
)
ccUserLogin.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccUserLogin.setStatus(
        "current"
    )

ccUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 4)
)
ccUserLogout.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccUserLogout.setStatus(
        "current"
    )

ccSPortConnectionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 5)
)
ccSPortConnectionStarted.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccSessionType"),
        ("RARITANCCv2-MIB", "ccUserSessionId"),
        ("RARITANCCv2-MIB", "ccNodeName"),
        ("RARITANCCv2-MIB", "ccPortName"))
)
if mibBuilder.loadTexts:
    ccSPortConnectionStarted.setStatus(
        "current"
    )

ccPortConnectionStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 6)
)
ccPortConnectionStopped.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccSessionType"),
        ("RARITANCCv2-MIB", "ccUserSessionId"),
        ("RARITANCCv2-MIB", "ccNodeName"),
        ("RARITANCCv2-MIB", "ccPortName"))
)
if mibBuilder.loadTexts:
    ccPortConnectionStopped.setStatus(
        "current"
    )

ccPortConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 7)
)
ccPortConnectionTerminated.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserNameInitiated"),
        ("RARITANCCv2-MIB", "ccUserNameTerminated"),
        ("RARITANCCv2-MIB", "ccSessionType"),
        ("RARITANCCv2-MIB", "ccUserSessionId"),
        ("RARITANCCv2-MIB", "ccNodeName"),
        ("RARITANCCv2-MIB", "ccPortName"))
)
if mibBuilder.loadTexts:
    ccPortConnectionTerminated.setStatus(
        "current"
    )

ccImageUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 8)
)
ccImageUpgradeStarted.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccImageType"),
        ("RARITANCCv2-MIB", "ccImageVersion"))
)
if mibBuilder.loadTexts:
    ccImageUpgradeStarted.setStatus(
        "current"
    )

ccImageUpgradeResults = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 9)
)
ccImageUpgradeResults.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccImageType"),
        ("RARITANCCv2-MIB", "ccImageVersion"),
        ("RARITANCCv2-MIB", "ccImageVersionStatus"))
)
if mibBuilder.loadTexts:
    ccImageUpgradeResults.setStatus(
        "current"
    )

ccUserAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 10)
)
ccUserAdded.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccUserWhoAdded"))
)
if mibBuilder.loadTexts:
    ccUserAdded.setStatus(
        "current"
    )

ccUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 11)
)
ccUserDeleted.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccUserWhoDeleted"))
)
if mibBuilder.loadTexts:
    ccUserDeleted.setStatus(
        "current"
    )

ccUserModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 12)
)
ccUserModified.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccUserModified.setStatus(
        "current"
    )

ccUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 13)
)
ccUserAuthenticationFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccUserAuthenticationFailure.setStatus(
        "current"
    )

ccRootPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 14)
)
ccRootPasswordChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccRootPasswordChanged.setStatus(
        "current"
    )

ccLanCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 15)
)
ccLanCardFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLanCard"),
        ("RARITANCCv2-MIB", "ccClusterState"))
)
if mibBuilder.loadTexts:
    ccLanCardFailure.setStatus(
        "current"
    )

ccHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 16)
)
ccHardDiskFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccHardDisk"),
        ("RARITANCCv2-MIB", "ccClusterState"))
)
if mibBuilder.loadTexts:
    ccHardDiskFailure.setStatus(
        "current"
    )

ccLeafNodeUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 17)
)
ccLeafNodeUnavailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccLeafNodeUnavailable.setStatus(
        "current"
    )

ccLeafNodeAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 18)
)
ccLeafNodeAvailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccLeafNodeAvailable.setStatus(
        "current"
    )

ccIncompatibleDeviceFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 19)
)
ccIncompatibleDeviceFirmware.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"),
        ("RARITANCCv2-MIB", "ccLeafNodeFirmwareVersion"))
)
if mibBuilder.loadTexts:
    ccIncompatibleDeviceFirmware.setStatus(
        "current"
    )

ccDeviceUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 20)
)
ccDeviceUpgrade.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"),
        ("RARITANCCv2-MIB", "ccLeafNodeFirmwareVersion"),
        ("RARITANCCv2-MIB", "ccImageVersionStatus"))
)
if mibBuilder.loadTexts:
    ccDeviceUpgrade.setStatus(
        "current"
    )

ccEnterMaintenanceMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 21)
)
ccEnterMaintenanceMode.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccEnterMaintenanceMode.setStatus(
        "current"
    )

ccExitMaintenanceMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 22)
)
ccExitMaintenanceMode.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccExitMaintenanceMode.setStatus(
        "current"
    )

ccUserLockedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 23)
)
ccUserLockedOut.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"))
)
if mibBuilder.loadTexts:
    ccUserLockedOut.setStatus(
        "current"
    )

ccDeviceAddedAfterCCNOCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 24)
)
ccDeviceAddedAfterCCNOCNotification.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccDeviceName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccDeviceAddedAfterCCNOCNotification.setStatus(
        "current"
    )

ccScheduledTaskExecutionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 25)
)
ccScheduledTaskExecutionFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccScheduledTaskDescription"),
        ("RARITANCCv2-MIB", "ccScheduledTaskFailureReason"))
)
if mibBuilder.loadTexts:
    ccScheduledTaskExecutionFailure.setStatus(
        "current"
    )

ccDiagnosticConsoleLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 26)
)
ccDiagnosticConsoleLogin.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccDiagnosticConsoleMAX_ACCESSLevel"))
)
if mibBuilder.loadTexts:
    ccDiagnosticConsoleLogin.setStatus(
        "current"
    )

ccDiagnosticConsoleLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 27)
)
ccDiagnosticConsoleLogout.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccDiagnosticConsoleMAX_ACCESSLevel"))
)
if mibBuilder.loadTexts:
    ccDiagnosticConsoleLogout.setStatus(
        "current"
    )

ccNOCAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 28)
)
ccNOCAvailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccNOCAvailable.setStatus(
        "current"
    )

ccNOCUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 29)
)
ccNOCUnavailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccNOCUnavailable.setStatus(
        "current"
    )

ccUserGroupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 30)
)
ccUserGroupAdded.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserGroupName"),
        ("RARITANCCv2-MIB", "ccUserWhoAdded"))
)
if mibBuilder.loadTexts:
    ccUserGroupAdded.setStatus(
        "current"
    )

ccUserGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 31)
)
ccUserGroupDeleted.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserGroupName"),
        ("RARITANCCv2-MIB", "ccUserWhoDeleted"))
)
if mibBuilder.loadTexts:
    ccUserGroupDeleted.setStatus(
        "current"
    )

ccUserGroupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 32)
)
ccUserGroupModified.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserGroupName"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccUserGroupModified.setStatus(
        "current"
    )

ccSuperuserNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 33)
)
ccSuperuserNameChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccSuperuserNameChanged.setStatus(
        "current"
    )

ccSuperuserPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 34)
)
ccSuperuserPasswordChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccSuperuserPasswordChanged.setStatus(
        "current"
    )

ccLoginBannerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 35)
)
ccLoginBannerChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"),
        ("RARITANCCv2-MIB", "ccBannerChanges"))
)
if mibBuilder.loadTexts:
    ccLoginBannerChanged.setStatus(
        "current"
    )

ccMOTDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 36)
)
ccMOTDChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"),
        ("RARITANCCv2-MIB", "ccMOTDChanges"))
)
if mibBuilder.loadTexts:
    ccMOTDChanged.setStatus(
        "current"
    )

ccDominionPXReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 37)
)
ccDominionPXReplaced.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccOldNumberOfOutlets"),
        ("RARITANCCv2-MIB", "ccNewNumberOfOutlets"))
)
if mibBuilder.loadTexts:
    ccDominionPXReplaced.setStatus(
        "current"
    )

ccSystemMonitorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 38)
)
ccSystemMonitorNotification.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccSystemMonitorNotificationLevel"),
        ("RARITANCCv2-MIB", "ccSystemMonitorNotificationMessage"))
)
if mibBuilder.loadTexts:
    ccSystemMonitorNotification.setStatus(
        "current"
    )

ccNeighborhoodActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 39)
)
ccNeighborhoodActivated.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"))
)
if mibBuilder.loadTexts:
    ccNeighborhoodActivated.setStatus(
        "current"
    )

ccNeighborhoodUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 40)
)
ccNeighborhoodUpdated.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"))
)
if mibBuilder.loadTexts:
    ccNeighborhoodUpdated.setStatus(
        "current"
    )

ccDominionPXFirmwareChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 41)
)
ccDominionPXFirmwareChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccDominionPXFirmwareVersion"))
)
if mibBuilder.loadTexts:
    ccDominionPXFirmwareChanged.setStatus(
        "current"
    )

ccClusterFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 42)
)
ccClusterFailover.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccClusterPeer"))
)
if mibBuilder.loadTexts:
    ccClusterFailover.setStatus(
        "current"
    )

ccClusterBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 43)
)
ccClusterBackupFailed.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccClusterPeer"))
)
if mibBuilder.loadTexts:
    ccClusterBackupFailed.setStatus(
        "current"
    )

ccClusterWaitingPeerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 44)
)
ccClusterWaitingPeerDetected.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccClusterPeer"))
)
if mibBuilder.loadTexts:
    ccClusterWaitingPeerDetected.setStatus(
        "current"
    )

ccClusterAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 45)
)
ccClusterAction.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccClusterOperation"),
        ("RARITANCCv2-MIB", "ccClusterOperationStatus"))
)
if mibBuilder.loadTexts:
    ccClusterAction.setStatus(
        "current"
    )

ccCSVFileTransferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 46)
)
ccCSVFileTransferred.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccFileType"),
        ("RARITANCCv2-MIB", "ccTransferOperation"))
)
if mibBuilder.loadTexts:
    ccCSVFileTransferred.setStatus(
        "current"
    )

ccPIQUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 47)
)
ccPIQUnavailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccPIQUnavailable.setStatus(
        "current"
    )

ccPIQAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 48)
)
ccPIQAvailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLeafNodeName"),
        ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
)
if mibBuilder.loadTexts:
    ccPIQAvailable.setStatus(
        "current"
    )

ccLicenseServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 49)
)
ccLicenseServerUnavailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLicenseServer"))
)
if mibBuilder.loadTexts:
    ccLicenseServerUnavailable.setStatus(
        "current"
    )

ccLicenseServerFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 50)
)
ccLicenseServerFailover.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLicenseServer"))
)
if mibBuilder.loadTexts:
    ccLicenseServerFailover.setStatus(
        "current"
    )

ccLicenseServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 51)
)
ccLicenseServerAvailable.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLicenseServer"))
)
if mibBuilder.loadTexts:
    ccLicenseServerAvailable.setStatus(
        "current"
    )

ccLicenseTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 52)
)
ccLicenseTerminated.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"))
)
if mibBuilder.loadTexts:
    ccLicenseTerminated.setStatus(
        "current"
    )

ccAddLicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 53)
)
ccAddLicenseFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"))
)
if mibBuilder.loadTexts:
    ccAddLicenseFailure.setStatus(
        "current"
    )

ccAddFeatureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 54)
)
ccAddFeatureFailure.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLicensedFeature"))
)
if mibBuilder.loadTexts:
    ccAddFeatureFailure.setStatus(
        "current"
    )

ccLicenseTerminatedWithReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 55)
)
ccLicenseTerminatedWithReason.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccLicenseTerminatedReason"))
)
if mibBuilder.loadTexts:
    ccLicenseTerminatedWithReason.setStatus(
        "current"
    )

ccUserPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 56)
)
ccUserPasswordChanged.setObjects(
      *(("RARITANCCv2-MIB", "ccObjectName"),
        ("RARITANCCv2-MIB", "ccObjectInstance"),
        ("RARITANCCv2-MIB", "ccUserName"),
        ("RARITANCCv2-MIB", "ccUserWhoModified"))
)
if mibBuilder.loadTexts:
    ccUserPasswordChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RARITANCCv2-MIB",
    **{"raritan": raritan,
       "products": products,
       "enterpriseManagement": enterpriseManagement,
       "commandCenter": commandCenter,
       "ccObject": ccObject,
       "ccObjectName": ccObjectName,
       "ccObjectInstance": ccObjectInstance,
       "ccUserName": ccUserName,
       "ccUserSessionId": ccUserSessionId,
       "ccUserNameInitiated": ccUserNameInitiated,
       "ccUserNameTerminated": ccUserNameTerminated,
       "ccImageType": ccImageType,
       "ccImageVersion": ccImageVersion,
       "ccImageVersionStatus": ccImageVersionStatus,
       "ccUserWhoAdded": ccUserWhoAdded,
       "ccUserWhoDeleted": ccUserWhoDeleted,
       "ccUserWhoModified": ccUserWhoModified,
       "ccNodeName": ccNodeName,
       "ccLanCard": ccLanCard,
       "ccHardDisk": ccHardDisk,
       "ccSessionType": ccSessionType,
       "ccClusterState": ccClusterState,
       "ccLeafNodeName": ccLeafNodeName,
       "ccLeafNodeIPAddress": ccLeafNodeIPAddress,
       "ccLeafNodeFirmwareVersion": ccLeafNodeFirmwareVersion,
       "ccScheduledTaskDescription": ccScheduledTaskDescription,
       "ccScheduledTaskFailureReason": ccScheduledTaskFailureReason,
       "ccDiagnosticConsoleMAX-ACCESSLevel": ccDiagnosticConsoleMAX_ACCESSLevel,
       "ccDeviceName": ccDeviceName,
       "ccUserGroupName": ccUserGroupName,
       "ccBannerChanges": ccBannerChanges,
       "ccMOTDChanges": ccMOTDChanges,
       "ccOldNumberOfOutlets": ccOldNumberOfOutlets,
       "ccNewNumberOfOutlets": ccNewNumberOfOutlets,
       "ccSystemMonitorNotificationLevel": ccSystemMonitorNotificationLevel,
       "ccSystemMonitorNotificationMessage": ccSystemMonitorNotificationMessage,
       "ccDominionPXFirmwareVersion": ccDominionPXFirmwareVersion,
       "ccClusterPeer": ccClusterPeer,
       "ccClusterOperation": ccClusterOperation,
       "ccClusterOperationStatus": ccClusterOperationStatus,
       "ccTransferOperation": ccTransferOperation,
       "ccFileType": ccFileType,
       "ccLicensedFeature": ccLicensedFeature,
       "ccLicenseServer": ccLicenseServer,
       "ccLicenseTerminatedReason": ccLicenseTerminatedReason,
       "ccPortName": ccPortName,
       "ccNotify": ccNotify,
       "ccUnavailable": ccUnavailable,
       "ccAvailable": ccAvailable,
       "ccUserLogin": ccUserLogin,
       "ccUserLogout": ccUserLogout,
       "ccSPortConnectionStarted": ccSPortConnectionStarted,
       "ccPortConnectionStopped": ccPortConnectionStopped,
       "ccPortConnectionTerminated": ccPortConnectionTerminated,
       "ccImageUpgradeStarted": ccImageUpgradeStarted,
       "ccImageUpgradeResults": ccImageUpgradeResults,
       "ccUserAdded": ccUserAdded,
       "ccUserDeleted": ccUserDeleted,
       "ccUserModified": ccUserModified,
       "ccUserAuthenticationFailure": ccUserAuthenticationFailure,
       "ccRootPasswordChanged": ccRootPasswordChanged,
       "ccLanCardFailure": ccLanCardFailure,
       "ccHardDiskFailure": ccHardDiskFailure,
       "ccLeafNodeUnavailable": ccLeafNodeUnavailable,
       "ccLeafNodeAvailable": ccLeafNodeAvailable,
       "ccIncompatibleDeviceFirmware": ccIncompatibleDeviceFirmware,
       "ccDeviceUpgrade": ccDeviceUpgrade,
       "ccEnterMaintenanceMode": ccEnterMaintenanceMode,
       "ccExitMaintenanceMode": ccExitMaintenanceMode,
       "ccUserLockedOut": ccUserLockedOut,
       "ccDeviceAddedAfterCCNOCNotification": ccDeviceAddedAfterCCNOCNotification,
       "ccScheduledTaskExecutionFailure": ccScheduledTaskExecutionFailure,
       "ccDiagnosticConsoleLogin": ccDiagnosticConsoleLogin,
       "ccDiagnosticConsoleLogout": ccDiagnosticConsoleLogout,
       "ccNOCAvailable": ccNOCAvailable,
       "ccNOCUnavailable": ccNOCUnavailable,
       "ccUserGroupAdded": ccUserGroupAdded,
       "ccUserGroupDeleted": ccUserGroupDeleted,
       "ccUserGroupModified": ccUserGroupModified,
       "ccSuperuserNameChanged": ccSuperuserNameChanged,
       "ccSuperuserPasswordChanged": ccSuperuserPasswordChanged,
       "ccLoginBannerChanged": ccLoginBannerChanged,
       "ccMOTDChanged": ccMOTDChanged,
       "ccDominionPXReplaced": ccDominionPXReplaced,
       "ccSystemMonitorNotification": ccSystemMonitorNotification,
       "ccNeighborhoodActivated": ccNeighborhoodActivated,
       "ccNeighborhoodUpdated": ccNeighborhoodUpdated,
       "ccDominionPXFirmwareChanged": ccDominionPXFirmwareChanged,
       "ccClusterFailover": ccClusterFailover,
       "ccClusterBackupFailed": ccClusterBackupFailed,
       "ccClusterWaitingPeerDetected": ccClusterWaitingPeerDetected,
       "ccClusterAction": ccClusterAction,
       "ccCSVFileTransferred": ccCSVFileTransferred,
       "ccPIQUnavailable": ccPIQUnavailable,
       "ccPIQAvailable": ccPIQAvailable,
       "ccLicenseServerUnavailable": ccLicenseServerUnavailable,
       "ccLicenseServerFailover": ccLicenseServerFailover,
       "ccLicenseServerAvailable": ccLicenseServerAvailable,
       "ccLicenseTerminated": ccLicenseTerminated,
       "ccAddLicenseFailure": ccAddLicenseFailure,
       "ccAddFeatureFailure": ccAddFeatureFailure,
       "ccLicenseTerminatedWithReason": ccLicenseTerminatedWithReason,
       "ccUserPasswordChanged": ccUserPasswordChanged}
)
