# SNMP MIB module (CISCO-CDSTV-INGESTMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-INGESTMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:18 2024
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

(CiscoURLString,
 CiscoURLStringOrEmpty,
 TimeIntervalMin,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString",
    "CiscoURLStringOrEmpty",
    "TimeIntervalMin",
    "TimeIntervalSec")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdstvIngestmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739)
)
ciscoCdstvIngestmgrMIB.setRevisions(
        ("2010-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvIngestMgrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestMgrMIBNotifs = _CiscoCdstvIngestMgrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 0)
)
_CiscoCdstvIngestMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestMgrMIBObjects = _CiscoCdstvIngestMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1)
)
_CdstvIngestMgrGeneralSettings_ObjectIdentity = ObjectIdentity
cdstvIngestMgrGeneralSettings = _CdstvIngestMgrGeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1)
)
_CdstvIngestMgrHostAddressType_Type = InetAddressType
_CdstvIngestMgrHostAddressType_Object = MibScalar
cdstvIngestMgrHostAddressType = _CdstvIngestMgrHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 1),
    _CdstvIngestMgrHostAddressType_Type()
)
cdstvIngestMgrHostAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrHostAddressType.setStatus("current")
_CdstvIngestMgrHostAddress_Type = InetAddress
_CdstvIngestMgrHostAddress_Object = MibScalar
cdstvIngestMgrHostAddress = _CdstvIngestMgrHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 2),
    _CdstvIngestMgrHostAddress_Type()
)
cdstvIngestMgrHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrHostAddress.setStatus("current")


class _CdstvIngestMgrPort_Type(InetPortNumber):
    """Custom type cdstvIngestMgrPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdstvIngestMgrPort_Type.__name__ = "InetPortNumber"
_CdstvIngestMgrPort_Object = MibScalar
cdstvIngestMgrPort = _CdstvIngestMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 3),
    _CdstvIngestMgrPort_Type()
)
cdstvIngestMgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrPort.setStatus("current")


class _CdstvIngestMgrFsiCallbackPort_Type(InetPortNumber):
    """Custom type cdstvIngestMgrFsiCallbackPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdstvIngestMgrFsiCallbackPort_Type.__name__ = "InetPortNumber"
_CdstvIngestMgrFsiCallbackPort_Object = MibScalar
cdstvIngestMgrFsiCallbackPort = _CdstvIngestMgrFsiCallbackPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 4),
    _CdstvIngestMgrFsiCallbackPort_Type()
)
cdstvIngestMgrFsiCallbackPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrFsiCallbackPort.setStatus("current")
_CdstvIngestMgrAdditionalPackageWindow_Type = Unsigned32
_CdstvIngestMgrAdditionalPackageWindow_Object = MibScalar
cdstvIngestMgrAdditionalPackageWindow = _CdstvIngestMgrAdditionalPackageWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 5),
    _CdstvIngestMgrAdditionalPackageWindow_Type()
)
cdstvIngestMgrAdditionalPackageWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrAdditionalPackageWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdstvIngestMgrAdditionalPackageWindow.setUnits("days")
_CdstvIngestMgrFtpTimeout_Type = TimeIntervalSec
_CdstvIngestMgrFtpTimeout_Object = MibScalar
cdstvIngestMgrFtpTimeout = _CdstvIngestMgrFtpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 6),
    _CdstvIngestMgrFtpTimeout_Type()
)
cdstvIngestMgrFtpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrFtpTimeout.setStatus("current")
_CdstvIngestMgrUseAssetIdEnable_Type = TruthValue
_CdstvIngestMgrUseAssetIdEnable_Object = MibScalar
cdstvIngestMgrUseAssetIdEnable = _CdstvIngestMgrUseAssetIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 7),
    _CdstvIngestMgrUseAssetIdEnable_Type()
)
cdstvIngestMgrUseAssetIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrUseAssetIdEnable.setStatus("current")
_CdstvIngestMgrManageCorbaServices_Type = TruthValue
_CdstvIngestMgrManageCorbaServices_Object = MibScalar
cdstvIngestMgrManageCorbaServices = _CdstvIngestMgrManageCorbaServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 8),
    _CdstvIngestMgrManageCorbaServices_Type()
)
cdstvIngestMgrManageCorbaServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrManageCorbaServices.setStatus("current")
_CdstvIngestMgrRequireNotifyService_Type = TruthValue
_CdstvIngestMgrRequireNotifyService_Object = MibScalar
cdstvIngestMgrRequireNotifyService = _CdstvIngestMgrRequireNotifyService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 9),
    _CdstvIngestMgrRequireNotifyService_Type()
)
cdstvIngestMgrRequireNotifyService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrRequireNotifyService.setStatus("current")


class _CdstvIngestMgrDebugLevel_Type(Integer32):
    """Custom type cdstvIngestMgrDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("errors", 1),
          ("off", 3))
    )


_CdstvIngestMgrDebugLevel_Type.__name__ = "Integer32"
_CdstvIngestMgrDebugLevel_Object = MibScalar
cdstvIngestMgrDebugLevel = _CdstvIngestMgrDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 10),
    _CdstvIngestMgrDebugLevel_Type()
)
cdstvIngestMgrDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrDebugLevel.setStatus("current")
_CdstvIngestMgrMetaDataPublish_Type = TruthValue
_CdstvIngestMgrMetaDataPublish_Object = MibScalar
cdstvIngestMgrMetaDataPublish = _CdstvIngestMgrMetaDataPublish_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 11),
    _CdstvIngestMgrMetaDataPublish_Type()
)
cdstvIngestMgrMetaDataPublish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrMetaDataPublish.setStatus("current")
_CdstvIngestMgrMetaPublishUrl_Type = CiscoURLString
_CdstvIngestMgrMetaPublishUrl_Object = MibScalar
cdstvIngestMgrMetaPublishUrl = _CdstvIngestMgrMetaPublishUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 12),
    _CdstvIngestMgrMetaPublishUrl_Type()
)
cdstvIngestMgrMetaPublishUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrMetaPublishUrl.setStatus("current")
_CdstvIngestMgrMetaPublishBackupUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrMetaPublishBackupUrl_Object = MibScalar
cdstvIngestMgrMetaPublishBackupUrl = _CdstvIngestMgrMetaPublishBackupUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 13),
    _CdstvIngestMgrMetaPublishBackupUrl_Type()
)
cdstvIngestMgrMetaPublishBackupUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrMetaPublishBackupUrl.setStatus("current")
_CdstvIngestMgrIngestSettings_ObjectIdentity = ObjectIdentity
cdstvIngestMgrIngestSettings = _CdstvIngestMgrIngestSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2)
)


class _CdstvIngestMgrIngestInterface_Type(Bits):
    """Custom type cdstvIngestMgrIngestInterface based on Bits"""
    namedValues = NamedValues(
        *(("ciscoSoap", 1),
          ("isa", 0),
          ("prodisSoap", 2))
    )

_CdstvIngestMgrIngestInterface_Type.__name__ = "Bits"
_CdstvIngestMgrIngestInterface_Object = MibScalar
cdstvIngestMgrIngestInterface = _CdstvIngestMgrIngestInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 1),
    _CdstvIngestMgrIngestInterface_Type()
)
cdstvIngestMgrIngestInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrIngestInterface.setStatus("current")
_CdstvIngestMgrCiscoSoapUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrCiscoSoapUrl_Object = MibScalar
cdstvIngestMgrCiscoSoapUrl = _CdstvIngestMgrCiscoSoapUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 2),
    _CdstvIngestMgrCiscoSoapUrl_Type()
)
cdstvIngestMgrCiscoSoapUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrCiscoSoapUrl.setStatus("current")
_CdstvIngestMgrProdisSoapUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrProdisSoapUrl_Object = MibScalar
cdstvIngestMgrProdisSoapUrl = _CdstvIngestMgrProdisSoapUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 3),
    _CdstvIngestMgrProdisSoapUrl_Type()
)
cdstvIngestMgrProdisSoapUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrProdisSoapUrl.setStatus("current")
_CdstvIngestMgrBackOfficeSettings_ObjectIdentity = ObjectIdentity
cdstvIngestMgrBackOfficeSettings = _CdstvIngestMgrBackOfficeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3)
)


class _CdstvIngestMgrBackOfficeMaxRetries_Type(Unsigned32):
    """Custom type cdstvIngestMgrBackOfficeMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CdstvIngestMgrBackOfficeMaxRetries_Type.__name__ = "Unsigned32"
_CdstvIngestMgrBackOfficeMaxRetries_Object = MibScalar
cdstvIngestMgrBackOfficeMaxRetries = _CdstvIngestMgrBackOfficeMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 1),
    _CdstvIngestMgrBackOfficeMaxRetries_Type()
)
cdstvIngestMgrBackOfficeMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeMaxRetries.setStatus("current")
_CdstvIngestMgrBackOfficeRetryInterval_Type = TimeIntervalMin
_CdstvIngestMgrBackOfficeRetryInterval_Object = MibScalar
cdstvIngestMgrBackOfficeRetryInterval = _CdstvIngestMgrBackOfficeRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 2),
    _CdstvIngestMgrBackOfficeRetryInterval_Type()
)
cdstvIngestMgrBackOfficeRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeRetryInterval.setStatus("current")
_CdstvIngestMgrBackOfficeTimeout_Type = TimeIntervalSec
_CdstvIngestMgrBackOfficeTimeout_Object = MibScalar
cdstvIngestMgrBackOfficeTimeout = _CdstvIngestMgrBackOfficeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 3),
    _CdstvIngestMgrBackOfficeTimeout_Type()
)
cdstvIngestMgrBackOfficeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeTimeout.setStatus("current")
_CdstvIngestMgrBackOfficeTable_Object = MibTable
cdstvIngestMgrBackOfficeTable = _CdstvIngestMgrBackOfficeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeTable.setStatus("current")
_CdstvIngestMgrBackOfficeEntry_Object = MibTableRow
cdstvIngestMgrBackOfficeEntry = _CdstvIngestMgrBackOfficeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1)
)
cdstvIngestMgrBackOfficeEntry.setIndexNames(
    (0, "CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeIndex"),
)
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeEntry.setStatus("current")
_CdstvIngestMgrBackOfficeIndex_Type = Unsigned32
_CdstvIngestMgrBackOfficeIndex_Object = MibTableColumn
cdstvIngestMgrBackOfficeIndex = _CdstvIngestMgrBackOfficeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 1),
    _CdstvIngestMgrBackOfficeIndex_Type()
)
cdstvIngestMgrBackOfficeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeIndex.setStatus("current")


class _CdstvIngestMgrBackOfficeType_Type(Integer32):
    """Custom type cdstvIngestMgrBackOfficeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("totalManage", 2))
    )


_CdstvIngestMgrBackOfficeType_Type.__name__ = "Integer32"
_CdstvIngestMgrBackOfficeType_Object = MibTableColumn
cdstvIngestMgrBackOfficeType = _CdstvIngestMgrBackOfficeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 2),
    _CdstvIngestMgrBackOfficeType_Type()
)
cdstvIngestMgrBackOfficeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeType.setStatus("current")
_CdstvIngestMgrBackOfficeUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrBackOfficeUrl_Object = MibTableColumn
cdstvIngestMgrBackOfficeUrl = _CdstvIngestMgrBackOfficeUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 3),
    _CdstvIngestMgrBackOfficeUrl_Type()
)
cdstvIngestMgrBackOfficeUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrBackOfficeUrl.setStatus("current")
_CdstvIngestMgrContentStoreSettings_ObjectIdentity = ObjectIdentity
cdstvIngestMgrContentStoreSettings = _CdstvIngestMgrContentStoreSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4)
)


class _CdstvIngestMgrContentStore_Type(Integer32):
    """Custom type cdstvIngestMgrContentStore based on Integer32"""
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
        *(("fsi", 3),
          ("isa", 2),
          ("ngod", 4),
          ("none", 1),
          ("openStream", 5))
    )


_CdstvIngestMgrContentStore_Type.__name__ = "Integer32"
_CdstvIngestMgrContentStore_Object = MibScalar
cdstvIngestMgrContentStore = _CdstvIngestMgrContentStore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4, 1),
    _CdstvIngestMgrContentStore_Type()
)
cdstvIngestMgrContentStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrContentStore.setStatus("current")
_CdstvIngestMgrContentStoreUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrContentStoreUrl_Object = MibScalar
cdstvIngestMgrContentStoreUrl = _CdstvIngestMgrContentStoreUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4, 2),
    _CdstvIngestMgrContentStoreUrl_Type()
)
cdstvIngestMgrContentStoreUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrContentStoreUrl.setStatus("current")
_CdstvIngestMgrEncryptionSettings_ObjectIdentity = ObjectIdentity
cdstvIngestMgrEncryptionSettings = _CdstvIngestMgrEncryptionSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5)
)


class _CdstvIngestMgrEncryptionType_Type(Integer32):
    """Custom type cdstvIngestMgrEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("verimatrix", 2),
          ("widevine", 3))
    )


_CdstvIngestMgrEncryptionType_Type.__name__ = "Integer32"
_CdstvIngestMgrEncryptionType_Object = MibScalar
cdstvIngestMgrEncryptionType = _CdstvIngestMgrEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 1),
    _CdstvIngestMgrEncryptionType_Type()
)
cdstvIngestMgrEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrEncryptionType.setStatus("current")
_CdstvIngestMgrEncryptionTargetUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrEncryptionTargetUrl_Object = MibScalar
cdstvIngestMgrEncryptionTargetUrl = _CdstvIngestMgrEncryptionTargetUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 2),
    _CdstvIngestMgrEncryptionTargetUrl_Type()
)
cdstvIngestMgrEncryptionTargetUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrEncryptionTargetUrl.setStatus("current")
_CdstvIngestMgrEncryptionRetrievalUrl_Type = CiscoURLStringOrEmpty
_CdstvIngestMgrEncryptionRetrievalUrl_Object = MibScalar
cdstvIngestMgrEncryptionRetrievalUrl = _CdstvIngestMgrEncryptionRetrievalUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 3),
    _CdstvIngestMgrEncryptionRetrievalUrl_Type()
)
cdstvIngestMgrEncryptionRetrievalUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvIngestMgrEncryptionRetrievalUrl.setStatus("current")
_CiscoCdstvIngestMgrMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestMgrMIBConform = _CiscoCdstvIngestMgrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2)
)
_CiscoCdstvIngestMgrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestMgrMIBCompliances = _CiscoCdstvIngestMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 1)
)
_CiscoCdstvIngestMgrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvIngestMgrMIBGroups = _CiscoCdstvIngestMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2)
)

# Managed Objects groups

ciscoCdstvIngestMgrMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 1)
)
ciscoCdstvIngestMgrMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrHostAddress"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrPort"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrFsiCallbackPort"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrAdditionalPackageWindow"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrFtpTimeout"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrUseAssetIdEnable"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrManageCorbaServices"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrRequireNotifyService"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrDebugLevel"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaDataPublish"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaPublishUrl"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaPublishBackupUrl"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrHostAddressType"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBMainObjectGroup.setStatus("current")

ciscoCdstvIngestMgrMIBIngestSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 2)
)
ciscoCdstvIngestMgrMIBIngestSettingsGroup.setObjects(
      *(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrIngestInterface"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrCiscoSoapUrl"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrProdisSoapUrl"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBIngestSettingsGroup.setStatus("current")

ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 3)
)
ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup.setObjects(
      *(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeMaxRetries"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeRetryInterval"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeTimeout"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeType"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeUrl"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup.setStatus("current")

ciscoCdstvIngestMgrMIBContentStoreSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 4)
)
ciscoCdstvIngestMgrMIBContentStoreSettingsGroup.setObjects(
      *(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrContentStore"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrContentStoreUrl"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBContentStoreSettingsGroup.setStatus("current")

ciscoCdstvIngestMgrMIBEncryptionSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 5)
)
ciscoCdstvIngestMgrMIBEncryptionSettingsGroup.setObjects(
      *(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionType"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionTargetUrl"),
        ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionRetrievalUrl"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBEncryptionSettingsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvIngestMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvIngestMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-INGESTMGR-MIB",
    **{"ciscoCdstvIngestmgrMIB": ciscoCdstvIngestmgrMIB,
       "ciscoCdstvIngestMgrMIBNotifs": ciscoCdstvIngestMgrMIBNotifs,
       "ciscoCdstvIngestMgrMIBObjects": ciscoCdstvIngestMgrMIBObjects,
       "cdstvIngestMgrGeneralSettings": cdstvIngestMgrGeneralSettings,
       "cdstvIngestMgrHostAddressType": cdstvIngestMgrHostAddressType,
       "cdstvIngestMgrHostAddress": cdstvIngestMgrHostAddress,
       "cdstvIngestMgrPort": cdstvIngestMgrPort,
       "cdstvIngestMgrFsiCallbackPort": cdstvIngestMgrFsiCallbackPort,
       "cdstvIngestMgrAdditionalPackageWindow": cdstvIngestMgrAdditionalPackageWindow,
       "cdstvIngestMgrFtpTimeout": cdstvIngestMgrFtpTimeout,
       "cdstvIngestMgrUseAssetIdEnable": cdstvIngestMgrUseAssetIdEnable,
       "cdstvIngestMgrManageCorbaServices": cdstvIngestMgrManageCorbaServices,
       "cdstvIngestMgrRequireNotifyService": cdstvIngestMgrRequireNotifyService,
       "cdstvIngestMgrDebugLevel": cdstvIngestMgrDebugLevel,
       "cdstvIngestMgrMetaDataPublish": cdstvIngestMgrMetaDataPublish,
       "cdstvIngestMgrMetaPublishUrl": cdstvIngestMgrMetaPublishUrl,
       "cdstvIngestMgrMetaPublishBackupUrl": cdstvIngestMgrMetaPublishBackupUrl,
       "cdstvIngestMgrIngestSettings": cdstvIngestMgrIngestSettings,
       "cdstvIngestMgrIngestInterface": cdstvIngestMgrIngestInterface,
       "cdstvIngestMgrCiscoSoapUrl": cdstvIngestMgrCiscoSoapUrl,
       "cdstvIngestMgrProdisSoapUrl": cdstvIngestMgrProdisSoapUrl,
       "cdstvIngestMgrBackOfficeSettings": cdstvIngestMgrBackOfficeSettings,
       "cdstvIngestMgrBackOfficeMaxRetries": cdstvIngestMgrBackOfficeMaxRetries,
       "cdstvIngestMgrBackOfficeRetryInterval": cdstvIngestMgrBackOfficeRetryInterval,
       "cdstvIngestMgrBackOfficeTimeout": cdstvIngestMgrBackOfficeTimeout,
       "cdstvIngestMgrBackOfficeTable": cdstvIngestMgrBackOfficeTable,
       "cdstvIngestMgrBackOfficeEntry": cdstvIngestMgrBackOfficeEntry,
       "cdstvIngestMgrBackOfficeIndex": cdstvIngestMgrBackOfficeIndex,
       "cdstvIngestMgrBackOfficeType": cdstvIngestMgrBackOfficeType,
       "cdstvIngestMgrBackOfficeUrl": cdstvIngestMgrBackOfficeUrl,
       "cdstvIngestMgrContentStoreSettings": cdstvIngestMgrContentStoreSettings,
       "cdstvIngestMgrContentStore": cdstvIngestMgrContentStore,
       "cdstvIngestMgrContentStoreUrl": cdstvIngestMgrContentStoreUrl,
       "cdstvIngestMgrEncryptionSettings": cdstvIngestMgrEncryptionSettings,
       "cdstvIngestMgrEncryptionType": cdstvIngestMgrEncryptionType,
       "cdstvIngestMgrEncryptionTargetUrl": cdstvIngestMgrEncryptionTargetUrl,
       "cdstvIngestMgrEncryptionRetrievalUrl": cdstvIngestMgrEncryptionRetrievalUrl,
       "ciscoCdstvIngestMgrMIBConform": ciscoCdstvIngestMgrMIBConform,
       "ciscoCdstvIngestMgrMIBCompliances": ciscoCdstvIngestMgrMIBCompliances,
       "ciscoCdstvIngestMgrMIBCompliance": ciscoCdstvIngestMgrMIBCompliance,
       "ciscoCdstvIngestMgrMIBGroups": ciscoCdstvIngestMgrMIBGroups,
       "ciscoCdstvIngestMgrMIBMainObjectGroup": ciscoCdstvIngestMgrMIBMainObjectGroup,
       "ciscoCdstvIngestMgrMIBIngestSettingsGroup": ciscoCdstvIngestMgrMIBIngestSettingsGroup,
       "ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup": ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup,
       "ciscoCdstvIngestMgrMIBContentStoreSettingsGroup": ciscoCdstvIngestMgrMIBContentStoreSettingsGroup,
       "ciscoCdstvIngestMgrMIBEncryptionSettingsGroup": ciscoCdstvIngestMgrMIBEncryptionSettingsGroup}
)
