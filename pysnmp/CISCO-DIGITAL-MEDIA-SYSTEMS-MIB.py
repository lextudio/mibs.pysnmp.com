# SNMP MIB module (CISCO-DIGITAL-MEDIA-SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIGITAL-MEDIA-SYSTEMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:05 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDigitalMediaSystemsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655)
)
ciscoDigitalMediaSystemsMIB.setRevisions(
        ("2011-09-07 00:00",
         "2011-07-29 00:00",
         "2009-10-12 00:00",
         "2008-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDmsUserAuthenMethod(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("kerberos", 5),
          ("ldap", 7),
          ("local", 6),
          ("none", 1),
          ("ntlm", 8),
          ("other", 2),
          ("radius", 3),
          ("sdi", 9),
          ("tacacsPlus", 4))
    )



class CDmsServerType(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aaaServer", 7),
          ("dnsServer", 2),
          ("ldapServer", 3),
          ("ntpServer", 8),
          ("other", 1),
          ("smtpServer", 5),
          ("snmpServer", 4),
          ("syslogServer", 6))
    )



class CDmsElementType(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dmm", 8),
          ("encoder", 2),
          ("mediaPlayer", 4),
          ("other", 1),
          ("storageServer", 6),
          ("streamingServer", 7),
          ("transCoder", 5),
          ("videoPortal", 3))
    )



class CDmsFunctionalStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("initialize", 2),
          ("other", 1),
          ("shutdown", 4),
          ("standby", 5))
    )



class CDmsEmailAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CDmsLicensedFeature(Integer32, TextualConvention):
    status = "current"
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
        *(("base", 2),
          ("clustering", 11),
          ("deskTopVideo", 3),
          ("digitalMediaPlayer", 8),
          ("digitalMediaPlayerAuthorPack", 9),
          ("digitalMedialPlayerProofOfPlayPack", 10),
          ("digitalSignage", 5),
          ("enterpriseTv", 6),
          ("liveWebcastEnabler", 4),
          ("other", 1),
          ("snmpManagement", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDmsMonitorMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDmsMonitorMIBNotifs = _CiscoDmsMonitorMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0)
)
_CiscoDmsMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDmsMonitorMIBObjects = _CiscoDmsMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1)
)
_CdmsSystem_ObjectIdentity = ObjectIdentity
cdmsSystem = _CdmsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 1)
)


class _CdmsMajorVersion_Type(SnmpAdminString):
    """Custom type cdmsMajorVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CdmsMajorVersion_Type.__name__ = "SnmpAdminString"
_CdmsMajorVersion_Object = MibScalar
cdmsMajorVersion = _CdmsMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 1, 1),
    _CdmsMajorVersion_Type()
)
cdmsMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsMajorVersion.setStatus("current")


class _CdmsMinorVersion_Type(SnmpAdminString):
    """Custom type cdmsMinorVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CdmsMinorVersion_Type.__name__ = "SnmpAdminString"
_CdmsMinorVersion_Object = MibScalar
cdmsMinorVersion = _CdmsMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 1, 2),
    _CdmsMinorVersion_Type()
)
cdmsMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsMinorVersion.setStatus("current")


class _CdmsPatchVersion_Type(SnmpAdminString):
    """Custom type cdmsPatchVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CdmsPatchVersion_Type.__name__ = "SnmpAdminString"
_CdmsPatchVersion_Object = MibScalar
cdmsPatchVersion = _CdmsPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 1, 3),
    _CdmsPatchVersion_Type()
)
cdmsPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsPatchVersion.setStatus("current")
_CdmsAdministrator_Type = CDmsEmailAddress
_CdmsAdministrator_Object = MibScalar
cdmsAdministrator = _CdmsAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 1, 4),
    _CdmsAdministrator_Type()
)
cdmsAdministrator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsAdministrator.setStatus("current")
_CdmsFeatures_ObjectIdentity = ObjectIdentity
cdmsFeatures = _CdmsFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2)
)
_CdmsFeatureSummary_ObjectIdentity = ObjectIdentity
cdmsFeatureSummary = _CdmsFeatureSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 1)
)
_CdmsLicensableFeatures_Type = Unsigned32
_CdmsLicensableFeatures_Object = MibScalar
cdmsLicensableFeatures = _CdmsLicensableFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 1, 1),
    _CdmsLicensableFeatures_Type()
)
cdmsLicensableFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensableFeatures.setStatus("current")
_CdmsLicensedFeatures_Type = Unsigned32
_CdmsLicensedFeatures_Object = MibScalar
cdmsLicensedFeatures = _CdmsLicensedFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 1, 2),
    _CdmsLicensedFeatures_Type()
)
cdmsLicensedFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensedFeatures.setStatus("current")
_CdmsLastLicenseUpdate_Type = DateAndTime
_CdmsLastLicenseUpdate_Object = MibScalar
cdmsLastLicenseUpdate = _CdmsLastLicenseUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 1, 3),
    _CdmsLastLicenseUpdate_Type()
)
cdmsLastLicenseUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLastLicenseUpdate.setStatus("current")
_CdmsLicensedFeatureTable_Object = MibTable
cdmsLicensedFeatureTable = _CdmsLicensedFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdmsLicensedFeatureTable.setStatus("current")
_CdmsLicensedFeatureEntry_Object = MibTableRow
cdmsLicensedFeatureEntry = _CdmsLicensedFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1)
)
cdmsLicensedFeatureEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeature"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeatureIndex"),
)
if mibBuilder.loadTexts:
    cdmsLicensedFeatureEntry.setStatus("current")
_CdmsLicensedFeature_Type = CDmsLicensedFeature
_CdmsLicensedFeature_Object = MibTableColumn
cdmsLicensedFeature = _CdmsLicensedFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 1),
    _CdmsLicensedFeature_Type()
)
cdmsLicensedFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsLicensedFeature.setStatus("current")


class _CdmsLicensedFeatureIndex_Type(Unsigned32):
    """Custom type cdmsLicensedFeatureIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CdmsLicensedFeatureIndex_Type.__name__ = "Unsigned32"
_CdmsLicensedFeatureIndex_Object = MibTableColumn
cdmsLicensedFeatureIndex = _CdmsLicensedFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 2),
    _CdmsLicensedFeatureIndex_Type()
)
cdmsLicensedFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsLicensedFeatureIndex.setStatus("current")


class _CdmsLicensedFeatureLimit_Type(Unsigned32):
    """Custom type cdmsLicensedFeatureLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdmsLicensedFeatureLimit_Type.__name__ = "Unsigned32"
_CdmsLicensedFeatureLimit_Object = MibTableColumn
cdmsLicensedFeatureLimit = _CdmsLicensedFeatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 3),
    _CdmsLicensedFeatureLimit_Type()
)
cdmsLicensedFeatureLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensedFeatureLimit.setStatus("deprecated")
_CdmsLicensedFeatureDescription_Type = SnmpAdminString
_CdmsLicensedFeatureDescription_Object = MibTableColumn
cdmsLicensedFeatureDescription = _CdmsLicensedFeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 4),
    _CdmsLicensedFeatureDescription_Type()
)
cdmsLicensedFeatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensedFeatureDescription.setStatus("current")
_CdmsLicensedFeatureInstallDate_Type = DateAndTime
_CdmsLicensedFeatureInstallDate_Object = MibTableColumn
cdmsLicensedFeatureInstallDate = _CdmsLicensedFeatureInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 5),
    _CdmsLicensedFeatureInstallDate_Type()
)
cdmsLicensedFeatureInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensedFeatureInstallDate.setStatus("current")


class _CdmsLicensedFeatureLimitRev1_Type(Integer32):
    """Custom type cdmsLicensedFeatureLimitRev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_CdmsLicensedFeatureLimitRev1_Type.__name__ = "Integer32"
_CdmsLicensedFeatureLimitRev1_Object = MibTableColumn
cdmsLicensedFeatureLimitRev1 = _CdmsLicensedFeatureLimitRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 2, 2, 1, 6),
    _CdmsLicensedFeatureLimitRev1_Type()
)
cdmsLicensedFeatureLimitRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLicensedFeatureLimitRev1.setStatus("current")
_CdmsInventory_ObjectIdentity = ObjectIdentity
cdmsInventory = _CdmsInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3)
)
_CdmsInventoryGlobalCounters_ObjectIdentity = ObjectIdentity
cdmsInventoryGlobalCounters = _CdmsInventoryGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 1)
)
_CdmsNumMediaIngestionDevices_Type = Gauge32
_CdmsNumMediaIngestionDevices_Object = MibScalar
cdmsNumMediaIngestionDevices = _CdmsNumMediaIngestionDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 1, 1),
    _CdmsNumMediaIngestionDevices_Type()
)
cdmsNumMediaIngestionDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumMediaIngestionDevices.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumMediaIngestionDevices.setUnits("Encoders")
_CdmsNumMediaPlayerDevices_Type = Gauge32
_CdmsNumMediaPlayerDevices_Object = MibScalar
cdmsNumMediaPlayerDevices = _CdmsNumMediaPlayerDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 1, 2),
    _CdmsNumMediaPlayerDevices_Type()
)
cdmsNumMediaPlayerDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumMediaPlayerDevices.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumMediaPlayerDevices.setUnits("Media Players")
_CdmsNumVideoPortalDevices_Type = Gauge32
_CdmsNumVideoPortalDevices_Object = MibScalar
cdmsNumVideoPortalDevices = _CdmsNumVideoPortalDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 1, 3),
    _CdmsNumVideoPortalDevices_Type()
)
cdmsNumVideoPortalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumVideoPortalDevices.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumVideoPortalDevices.setUnits("Video Portals")
_CdmsInventoryTable_Object = MibTable
cdmsInventoryTable = _CdmsInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdmsInventoryTable.setStatus("current")
_CdmsInventoryEntry_Object = MibTableRow
cdmsInventoryEntry = _CdmsInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1)
)
cdmsInventoryEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementId"),
)
if mibBuilder.loadTexts:
    cdmsInventoryEntry.setStatus("current")
_CdmsInventoryElementType_Type = CDmsElementType
_CdmsInventoryElementType_Object = MibTableColumn
cdmsInventoryElementType = _CdmsInventoryElementType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 1),
    _CdmsInventoryElementType_Type()
)
cdmsInventoryElementType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsInventoryElementType.setStatus("current")


class _CdmsInventoryElementId_Type(SnmpAdminString):
    """Custom type cdmsInventoryElementId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CdmsInventoryElementId_Type.__name__ = "SnmpAdminString"
_CdmsInventoryElementId_Object = MibTableColumn
cdmsInventoryElementId = _CdmsInventoryElementId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 2),
    _CdmsInventoryElementId_Type()
)
cdmsInventoryElementId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsInventoryElementId.setStatus("current")
_CdmsInventoryElementMacAddress_Type = MacAddress
_CdmsInventoryElementMacAddress_Object = MibTableColumn
cdmsInventoryElementMacAddress = _CdmsInventoryElementMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 3),
    _CdmsInventoryElementMacAddress_Type()
)
cdmsInventoryElementMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsInventoryElementMacAddress.setStatus("current")
_CdmsInventoryElementAddrType_Type = InetAddressType
_CdmsInventoryElementAddrType_Object = MibTableColumn
cdmsInventoryElementAddrType = _CdmsInventoryElementAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 4),
    _CdmsInventoryElementAddrType_Type()
)
cdmsInventoryElementAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsInventoryElementAddrType.setStatus("current")
_CdmsInventoryElementAddress_Type = InetAddress
_CdmsInventoryElementAddress_Object = MibTableColumn
cdmsInventoryElementAddress = _CdmsInventoryElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 5),
    _CdmsInventoryElementAddress_Type()
)
cdmsInventoryElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsInventoryElementAddress.setStatus("current")
_CdmsInventoryElementMetadata_Type = SnmpAdminString
_CdmsInventoryElementMetadata_Object = MibTableColumn
cdmsInventoryElementMetadata = _CdmsInventoryElementMetadata_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 6),
    _CdmsInventoryElementMetadata_Type()
)
cdmsInventoryElementMetadata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsInventoryElementMetadata.setStatus("current")
_CdmsInventoryElementState_Type = CDmsFunctionalStatus
_CdmsInventoryElementState_Object = MibTableColumn
cdmsInventoryElementState = _CdmsInventoryElementState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 3, 2, 1, 7),
    _CdmsInventoryElementState_Type()
)
cdmsInventoryElementState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsInventoryElementState.setStatus("current")
_CdmsServers_ObjectIdentity = ObjectIdentity
cdmsServers = _CdmsServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4)
)
_CdmsServerTable_Object = MibTable
cdmsServerTable = _CdmsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdmsServerTable.setStatus("current")
_CdmsServerEntry_Object = MibTableRow
cdmsServerEntry = _CdmsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1)
)
cdmsServerEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsServerType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsServerAddrType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsServerAddress"),
)
if mibBuilder.loadTexts:
    cdmsServerEntry.setStatus("current")
_CdmsServerType_Type = CDmsServerType
_CdmsServerType_Object = MibTableColumn
cdmsServerType = _CdmsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1, 1),
    _CdmsServerType_Type()
)
cdmsServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsServerType.setStatus("current")
_CdmsServerAddrType_Type = InetAddressType
_CdmsServerAddrType_Object = MibTableColumn
cdmsServerAddrType = _CdmsServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1, 2),
    _CdmsServerAddrType_Type()
)
cdmsServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsServerAddrType.setStatus("current")


class _CdmsServerAddress_Type(InetAddress):
    """Custom type cdmsServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CdmsServerAddress_Type.__name__ = "InetAddress"
_CdmsServerAddress_Object = MibTableColumn
cdmsServerAddress = _CdmsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1, 3),
    _CdmsServerAddress_Type()
)
cdmsServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsServerAddress.setStatus("current")
_CdmsServerState_Type = CDmsFunctionalStatus
_CdmsServerState_Object = MibTableColumn
cdmsServerState = _CdmsServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1, 4),
    _CdmsServerState_Type()
)
cdmsServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsServerState.setStatus("current")
_CdmsServerStatus_Type = RowStatus
_CdmsServerStatus_Object = MibTableColumn
cdmsServerStatus = _CdmsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 4, 1, 1, 5),
    _CdmsServerStatus_Type()
)
cdmsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdmsServerStatus.setStatus("current")
_CdmsDamServices_ObjectIdentity = ObjectIdentity
cdmsDamServices = _CdmsDamServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 5)
)
_CdmsDamGlobalCounters_ObjectIdentity = ObjectIdentity
cdmsDamGlobalCounters = _CdmsDamGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 5, 1)
)
_CdmsNumContentElements_Type = Gauge32
_CdmsNumContentElements_Object = MibScalar
cdmsNumContentElements = _CdmsNumContentElements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 5, 1, 1),
    _CdmsNumContentElements_Type()
)
cdmsNumContentElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumContentElements.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumContentElements.setUnits("content elements")
_CdmsNumAuthenRequestsApproved_Type = Counter64
_CdmsNumAuthenRequestsApproved_Object = MibScalar
cdmsNumAuthenRequestsApproved = _CdmsNumAuthenRequestsApproved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 5, 1, 2),
    _CdmsNumAuthenRequestsApproved_Type()
)
cdmsNumAuthenRequestsApproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequestsApproved.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequestsApproved.setUnits("requests")
_CdmsNumAuthenRequestsDeclined_Type = Counter64
_CdmsNumAuthenRequestsDeclined_Object = MibScalar
cdmsNumAuthenRequestsDeclined = _CdmsNumAuthenRequestsDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 5, 1, 3),
    _CdmsNumAuthenRequestsDeclined_Type()
)
cdmsNumAuthenRequestsDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequestsDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequestsDeclined.setUnits("requests")
_CdmsSecurity_ObjectIdentity = ObjectIdentity
cdmsSecurity = _CdmsSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 6)
)
_CdmsSecurityGlobalCounters_ObjectIdentity = ObjectIdentity
cdmsSecurityGlobalCounters = _CdmsSecurityGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 6, 1)
)
_CdmsNumAuthenRequests_Type = Counter64
_CdmsNumAuthenRequests_Object = MibScalar
cdmsNumAuthenRequests = _CdmsNumAuthenRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 6, 1, 1),
    _CdmsNumAuthenRequests_Type()
)
cdmsNumAuthenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequests.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumAuthenRequests.setUnits("requests")
_CdmsSecurityConfiguration_ObjectIdentity = ObjectIdentity
cdmsSecurityConfiguration = _CdmsSecurityConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 6, 2)
)
_CdmsAuthenticationMode_Type = CDmsUserAuthenMethod
_CdmsAuthenticationMode_Object = MibScalar
cdmsAuthenticationMode = _CdmsAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 6, 2, 1),
    _CdmsAuthenticationMode_Type()
)
cdmsAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsAuthenticationMode.setStatus("current")
_CdmsUserGroup_ObjectIdentity = ObjectIdentity
cdmsUserGroup = _CdmsUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 7)
)
_CdmsNumUsers_Type = Gauge32
_CdmsNumUsers_Object = MibScalar
cdmsNumUsers = _CdmsNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 7, 1),
    _CdmsNumUsers_Type()
)
cdmsNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumUsers.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumUsers.setUnits("Users")
_CdmsNumActiveDmmUsers_Type = Gauge32
_CdmsNumActiveDmmUsers_Object = MibScalar
cdmsNumActiveDmmUsers = _CdmsNumActiveDmmUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 7, 2),
    _CdmsNumActiveDmmUsers_Type()
)
cdmsNumActiveDmmUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumActiveDmmUsers.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumActiveDmmUsers.setUnits("Users")
_CdmsNumActiveVpUsers_Type = Gauge32
_CdmsNumActiveVpUsers_Object = MibScalar
cdmsNumActiveVpUsers = _CdmsNumActiveVpUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 7, 3),
    _CdmsNumActiveVpUsers_Type()
)
cdmsNumActiveVpUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumActiveVpUsers.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumActiveVpUsers.setUnits("Users")
_CdmsLastUserLastChange_Type = DateAndTime
_CdmsLastUserLastChange_Object = MibScalar
cdmsLastUserLastChange = _CdmsLastUserLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 7, 4),
    _CdmsLastUserLastChange_Type()
)
cdmsLastUserLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsLastUserLastChange.setStatus("current")
_CdmsEvents_ObjectIdentity = ObjectIdentity
cdmsEvents = _CdmsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8)
)
_CdmsEventConfiguration_ObjectIdentity = ObjectIdentity
cdmsEventConfiguration = _CdmsEventConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 1)
)
_CdmsEventStatistics_ObjectIdentity = ObjectIdentity
cdmsEventStatistics = _CdmsEventStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2)
)
_CdmsNumEvents_Type = Counter64
_CdmsNumEvents_Object = MibScalar
cdmsNumEvents = _CdmsNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 1),
    _CdmsNumEvents_Type()
)
cdmsNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumEvents.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumEvents.setUnits("Events")
_CdmsNumEventRate_Type = Gauge32
_CdmsNumEventRate_Object = MibScalar
cdmsNumEventRate = _CdmsNumEventRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 2),
    _CdmsNumEventRate_Type()
)
cdmsNumEventRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumEventRate.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumEventRate.setUnits("Events per minute")
_CdmsNumAlarms_Type = Counter64
_CdmsNumAlarms_Object = MibScalar
cdmsNumAlarms = _CdmsNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 3),
    _CdmsNumAlarms_Type()
)
cdmsNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumAlarms.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumAlarms.setUnits("Alarms")
_CdmsNumAlarmRate_Type = Gauge32
_CdmsNumAlarmRate_Object = MibScalar
cdmsNumAlarmRate = _CdmsNumAlarmRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 4),
    _CdmsNumAlarmRate_Type()
)
cdmsNumAlarmRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumAlarmRate.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumAlarmRate.setUnits("Alarms per minute")
_CdmsNumNotifications_Type = Counter64
_CdmsNumNotifications_Object = MibScalar
cdmsNumNotifications = _CdmsNumNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 5),
    _CdmsNumNotifications_Type()
)
cdmsNumNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumNotifications.setUnits("Notifications")
_CdmsNumNotificationRate_Type = Gauge32
_CdmsNumNotificationRate_Object = MibScalar
cdmsNumNotificationRate = _CdmsNumNotificationRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 8, 2, 6),
    _CdmsNumNotificationRate_Type()
)
cdmsNumNotificationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsNumNotificationRate.setStatus("current")
if mibBuilder.loadTexts:
    cdmsNumNotificationRate.setUnits("Notifications per minute")
_CdmsHa_ObjectIdentity = ObjectIdentity
cdmsHa = _CdmsHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10)
)
_CdmsHaClusterInfo_ObjectIdentity = ObjectIdentity
cdmsHaClusterInfo = _CdmsHaClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 1)
)


class _CdmsHaClusterEnabled_Type(TruthValue):
    """Custom type cdmsHaClusterEnabled based on TruthValue"""


_CdmsHaClusterEnabled_Object = MibScalar
cdmsHaClusterEnabled = _CdmsHaClusterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 1, 1),
    _CdmsHaClusterEnabled_Type()
)
cdmsHaClusterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterEnabled.setStatus("current")


class _CdmsHaClusterName_Type(SnmpAdminString):
    """Custom type cdmsHaClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CdmsHaClusterName_Type.__name__ = "SnmpAdminString"
_CdmsHaClusterName_Object = MibScalar
cdmsHaClusterName = _CdmsHaClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 1, 2),
    _CdmsHaClusterName_Type()
)
cdmsHaClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsHaClusterName.setStatus("current")
_CdmsHaClusterComposition_ObjectIdentity = ObjectIdentity
cdmsHaClusterComposition = _CdmsHaClusterComposition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2)
)
_CdmsHaDmmCluster_ObjectIdentity = ObjectIdentity
cdmsHaDmmCluster = _CdmsHaDmmCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1)
)


class _CdmsHaClusterNumTotalDmms_Type(Integer32):
    """Custom type cdmsHaClusterNumTotalDmms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_CdmsHaClusterNumTotalDmms_Type.__name__ = "Integer32"
_CdmsHaClusterNumTotalDmms_Object = MibScalar
cdmsHaClusterNumTotalDmms = _CdmsHaClusterNumTotalDmms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 1),
    _CdmsHaClusterNumTotalDmms_Type()
)
cdmsHaClusterNumTotalDmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterNumTotalDmms.setStatus("current")
if mibBuilder.loadTexts:
    cdmsHaClusterNumTotalDmms.setUnits("Nodes")


class _CdmsHaClusterNumActiveDmms_Type(Gauge32):
    """Custom type cdmsHaClusterNumActiveDmms based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CdmsHaClusterNumActiveDmms_Type.__name__ = "Gauge32"
_CdmsHaClusterNumActiveDmms_Object = MibScalar
cdmsHaClusterNumActiveDmms = _CdmsHaClusterNumActiveDmms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 2),
    _CdmsHaClusterNumActiveDmms_Type()
)
cdmsHaClusterNumActiveDmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterNumActiveDmms.setStatus("current")
if mibBuilder.loadTexts:
    cdmsHaClusterNumActiveDmms.setUnits("Nodes")
_CdmsHaClusterDmmVipType_Type = InetAddressType
_CdmsHaClusterDmmVipType_Object = MibScalar
cdmsHaClusterDmmVipType = _CdmsHaClusterDmmVipType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 3),
    _CdmsHaClusterDmmVipType_Type()
)
cdmsHaClusterDmmVipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterDmmVipType.setStatus("current")
_CdmsHaClusterDmmVip_Type = InetAddress
_CdmsHaClusterDmmVip_Object = MibScalar
cdmsHaClusterDmmVip = _CdmsHaClusterDmmVip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 4),
    _CdmsHaClusterDmmVip_Type()
)
cdmsHaClusterDmmVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterDmmVip.setStatus("current")
_CdmsHaDmmClusterMemberTable_Object = MibTable
cdmsHaDmmClusterMemberTable = _CdmsHaDmmClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberTable.setStatus("current")
_CdmsHaDmmClusterMemberEntry_Object = MibTableRow
cdmsHaDmmClusterMemberEntry = _CdmsHaDmmClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5, 1)
)
cdmsHaDmmClusterMemberEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaDmmClusterMemberAddrType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaDmmClusterMemberAddress"),
)
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberEntry.setStatus("current")
_CdmsHaDmmClusterMemberAddrType_Type = InetAddressType
_CdmsHaDmmClusterMemberAddrType_Object = MibTableColumn
cdmsHaDmmClusterMemberAddrType = _CdmsHaDmmClusterMemberAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5, 1, 1),
    _CdmsHaDmmClusterMemberAddrType_Type()
)
cdmsHaDmmClusterMemberAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberAddrType.setStatus("current")
_CdmsHaDmmClusterMemberAddress_Type = InetAddress
_CdmsHaDmmClusterMemberAddress_Object = MibTableColumn
cdmsHaDmmClusterMemberAddress = _CdmsHaDmmClusterMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5, 1, 2),
    _CdmsHaDmmClusterMemberAddress_Type()
)
cdmsHaDmmClusterMemberAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberAddress.setStatus("current")
_CdmsHaDmmClusterMemberIsPrimary_Type = TruthValue
_CdmsHaDmmClusterMemberIsPrimary_Object = MibTableColumn
cdmsHaDmmClusterMemberIsPrimary = _CdmsHaDmmClusterMemberIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5, 1, 3),
    _CdmsHaDmmClusterMemberIsPrimary_Type()
)
cdmsHaDmmClusterMemberIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberIsPrimary.setStatus("current")
_CdmsHaDmmClusterMemberOperState_Type = CDmsFunctionalStatus
_CdmsHaDmmClusterMemberOperState_Object = MibTableColumn
cdmsHaDmmClusterMemberOperState = _CdmsHaDmmClusterMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 1, 5, 1, 4),
    _CdmsHaDmmClusterMemberOperState_Type()
)
cdmsHaDmmClusterMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaDmmClusterMemberOperState.setStatus("current")
_CdmsHaVpCluster_ObjectIdentity = ObjectIdentity
cdmsHaVpCluster = _CdmsHaVpCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2)
)


class _CdmsHaVpClusterNumClusters_Type(Integer32):
    """Custom type cdmsHaVpClusterNumClusters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CdmsHaVpClusterNumClusters_Type.__name__ = "Integer32"
_CdmsHaVpClusterNumClusters_Object = MibScalar
cdmsHaVpClusterNumClusters = _CdmsHaVpClusterNumClusters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 1),
    _CdmsHaVpClusterNumClusters_Type()
)
cdmsHaVpClusterNumClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaVpClusterNumClusters.setStatus("current")
_CdmsHaVpClusterMemberTable_Object = MibTable
cdmsHaVpClusterMemberTable = _CdmsHaVpClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberTable.setStatus("current")
_CdmsHaVpClusterMemberEntry_Object = MibTableRow
cdmsHaVpClusterMemberEntry = _CdmsHaVpClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1)
)
cdmsHaVpClusterMemberEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberClusterName"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberVipType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberVip"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberAddrType"),
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberAddress"),
)
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberEntry.setStatus("current")


class _CdmsHaVpClusterMemberClusterName_Type(SnmpAdminString):
    """Custom type cdmsHaVpClusterMemberClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CdmsHaVpClusterMemberClusterName_Type.__name__ = "SnmpAdminString"
_CdmsHaVpClusterMemberClusterName_Object = MibTableColumn
cdmsHaVpClusterMemberClusterName = _CdmsHaVpClusterMemberClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 1),
    _CdmsHaVpClusterMemberClusterName_Type()
)
cdmsHaVpClusterMemberClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberClusterName.setStatus("current")
_CdmsHaVpClusterMemberVipType_Type = InetAddressType
_CdmsHaVpClusterMemberVipType_Object = MibTableColumn
cdmsHaVpClusterMemberVipType = _CdmsHaVpClusterMemberVipType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 2),
    _CdmsHaVpClusterMemberVipType_Type()
)
cdmsHaVpClusterMemberVipType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberVipType.setStatus("current")
_CdmsHaVpClusterMemberVip_Type = InetAddress
_CdmsHaVpClusterMemberVip_Object = MibTableColumn
cdmsHaVpClusterMemberVip = _CdmsHaVpClusterMemberVip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 3),
    _CdmsHaVpClusterMemberVip_Type()
)
cdmsHaVpClusterMemberVip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberVip.setStatus("current")
_CdmsHaVpClusterMemberAddrType_Type = InetAddressType
_CdmsHaVpClusterMemberAddrType_Object = MibTableColumn
cdmsHaVpClusterMemberAddrType = _CdmsHaVpClusterMemberAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 4),
    _CdmsHaVpClusterMemberAddrType_Type()
)
cdmsHaVpClusterMemberAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberAddrType.setStatus("current")
_CdmsHaVpClusterMemberAddress_Type = InetAddress
_CdmsHaVpClusterMemberAddress_Object = MibTableColumn
cdmsHaVpClusterMemberAddress = _CdmsHaVpClusterMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 5),
    _CdmsHaVpClusterMemberAddress_Type()
)
cdmsHaVpClusterMemberAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberAddress.setStatus("current")
_CdmsHaVpClusterMemberIsPrimary_Type = TruthValue
_CdmsHaVpClusterMemberIsPrimary_Object = MibTableColumn
cdmsHaVpClusterMemberIsPrimary = _CdmsHaVpClusterMemberIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 6),
    _CdmsHaVpClusterMemberIsPrimary_Type()
)
cdmsHaVpClusterMemberIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberIsPrimary.setStatus("current")
_CdmsHaVpClusterMemberOperState_Type = CDmsFunctionalStatus
_CdmsHaVpClusterMemberOperState_Object = MibTableColumn
cdmsHaVpClusterMemberOperState = _CdmsHaVpClusterMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 2, 2, 2, 1, 7),
    _CdmsHaVpClusterMemberOperState_Type()
)
cdmsHaVpClusterMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaVpClusterMemberOperState.setStatus("current")
_CdmsHaClusterStatus_ObjectIdentity = ObjectIdentity
cdmsHaClusterStatus = _CdmsHaClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3)
)
_CdmsHaClusterLastDmmStatusChangeTime_Type = DateAndTime
_CdmsHaClusterLastDmmStatusChangeTime_Object = MibScalar
cdmsHaClusterLastDmmStatusChangeTime = _CdmsHaClusterLastDmmStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 1),
    _CdmsHaClusterLastDmmStatusChangeTime_Type()
)
cdmsHaClusterLastDmmStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastDmmStatusChangeTime.setStatus("current")
_CdmsHaClusterLastDmmStatusChangeAddrType_Type = InetAddressType
_CdmsHaClusterLastDmmStatusChangeAddrType_Object = MibScalar
cdmsHaClusterLastDmmStatusChangeAddrType = _CdmsHaClusterLastDmmStatusChangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 2),
    _CdmsHaClusterLastDmmStatusChangeAddrType_Type()
)
cdmsHaClusterLastDmmStatusChangeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastDmmStatusChangeAddrType.setStatus("current")
_CdmsHaClusterLastDmmStatusChangeAddress_Type = InetAddress
_CdmsHaClusterLastDmmStatusChangeAddress_Object = MibScalar
cdmsHaClusterLastDmmStatusChangeAddress = _CdmsHaClusterLastDmmStatusChangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 3),
    _CdmsHaClusterLastDmmStatusChangeAddress_Type()
)
cdmsHaClusterLastDmmStatusChangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastDmmStatusChangeAddress.setStatus("current")
_CdmsHaClusterLastVpStatusChangeTime_Type = DateAndTime
_CdmsHaClusterLastVpStatusChangeTime_Object = MibScalar
cdmsHaClusterLastVpStatusChangeTime = _CdmsHaClusterLastVpStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 4),
    _CdmsHaClusterLastVpStatusChangeTime_Type()
)
cdmsHaClusterLastVpStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastVpStatusChangeTime.setStatus("current")


class _CdmsHaClusterLastVpStatusChangeCluster_Type(SnmpAdminString):
    """Custom type cdmsHaClusterLastVpStatusChangeCluster based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CdmsHaClusterLastVpStatusChangeCluster_Type.__name__ = "SnmpAdminString"
_CdmsHaClusterLastVpStatusChangeCluster_Object = MibScalar
cdmsHaClusterLastVpStatusChangeCluster = _CdmsHaClusterLastVpStatusChangeCluster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 5),
    _CdmsHaClusterLastVpStatusChangeCluster_Type()
)
cdmsHaClusterLastVpStatusChangeCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastVpStatusChangeCluster.setStatus("current")
_CdmsHaClusterLastStatusChangeVpAddrType_Type = InetAddressType
_CdmsHaClusterLastStatusChangeVpAddrType_Object = MibScalar
cdmsHaClusterLastStatusChangeVpAddrType = _CdmsHaClusterLastStatusChangeVpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 6),
    _CdmsHaClusterLastStatusChangeVpAddrType_Type()
)
cdmsHaClusterLastStatusChangeVpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastStatusChangeVpAddrType.setStatus("current")
_CdmsHaClusterLastVpStatusChangeVpAddress_Type = InetAddress
_CdmsHaClusterLastVpStatusChangeVpAddress_Object = MibScalar
cdmsHaClusterLastVpStatusChangeVpAddress = _CdmsHaClusterLastVpStatusChangeVpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 7),
    _CdmsHaClusterLastVpStatusChangeVpAddress_Type()
)
cdmsHaClusterLastVpStatusChangeVpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterLastVpStatusChangeVpAddress.setStatus("current")
_CdmsHaClusterStatusHistory_ObjectIdentity = ObjectIdentity
cdmsHaClusterStatusHistory = _CdmsHaClusterStatusHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8)
)


class _CdmsHaClusterHistoryMaxRecords_Type(Integer32):
    """Custom type cdmsHaClusterHistoryMaxRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdmsHaClusterHistoryMaxRecords_Type.__name__ = "Integer32"
_CdmsHaClusterHistoryMaxRecords_Object = MibScalar
cdmsHaClusterHistoryMaxRecords = _CdmsHaClusterHistoryMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 1),
    _CdmsHaClusterHistoryMaxRecords_Type()
)
cdmsHaClusterHistoryMaxRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsHaClusterHistoryMaxRecords.setStatus("current")
_CdmsHaClusterHistoryTable_Object = MibTable
cdmsHaClusterHistoryTable = _CdmsHaClusterHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2)
)
if mibBuilder.loadTexts:
    cdmsHaClusterHistoryTable.setStatus("current")
_CdmsHaClusterHistoryEntry_Object = MibTableRow
cdmsHaClusterHistoryEntry = _CdmsHaClusterHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1)
)
cdmsHaClusterHistoryEntry.setIndexNames(
    (0, "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistId"),
)
if mibBuilder.loadTexts:
    cdmsHaClusterHistoryEntry.setStatus("current")


class _CdmsHaClusterHistId_Type(Integer32):
    """Custom type cdmsHaClusterHistId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdmsHaClusterHistId_Type.__name__ = "Integer32"
_CdmsHaClusterHistId_Object = MibTableColumn
cdmsHaClusterHistId = _CdmsHaClusterHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 1),
    _CdmsHaClusterHistId_Type()
)
cdmsHaClusterHistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdmsHaClusterHistId.setStatus("current")
_CdmsHaClusterHistTimestamp_Type = TimeStamp
_CdmsHaClusterHistTimestamp_Object = MibTableColumn
cdmsHaClusterHistTimestamp = _CdmsHaClusterHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 2),
    _CdmsHaClusterHistTimestamp_Type()
)
cdmsHaClusterHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistTimestamp.setStatus("current")


class _CdmsHaClusterHistClusterName_Type(SnmpAdminString):
    """Custom type cdmsHaClusterHistClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CdmsHaClusterHistClusterName_Type.__name__ = "SnmpAdminString"
_CdmsHaClusterHistClusterName_Object = MibTableColumn
cdmsHaClusterHistClusterName = _CdmsHaClusterHistClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 3),
    _CdmsHaClusterHistClusterName_Type()
)
cdmsHaClusterHistClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistClusterName.setStatus("current")
_CdmsHaClusterHistNodeType_Type = CDmsElementType
_CdmsHaClusterHistNodeType_Object = MibTableColumn
cdmsHaClusterHistNodeType = _CdmsHaClusterHistNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 4),
    _CdmsHaClusterHistNodeType_Type()
)
cdmsHaClusterHistNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistNodeType.setStatus("current")
_CdmsHaClusterHistNodeNewStatus_Type = CDmsFunctionalStatus
_CdmsHaClusterHistNodeNewStatus_Object = MibTableColumn
cdmsHaClusterHistNodeNewStatus = _CdmsHaClusterHistNodeNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 5),
    _CdmsHaClusterHistNodeNewStatus_Type()
)
cdmsHaClusterHistNodeNewStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistNodeNewStatus.setStatus("current")
_CdmsHaClusterHistNodeAddrType_Type = InetAddressType
_CdmsHaClusterHistNodeAddrType_Object = MibTableColumn
cdmsHaClusterHistNodeAddrType = _CdmsHaClusterHistNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 6),
    _CdmsHaClusterHistNodeAddrType_Type()
)
cdmsHaClusterHistNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistNodeAddrType.setStatus("current")
_CdmsHaClusterHistNodeAddr_Type = InetAddress
_CdmsHaClusterHistNodeAddr_Object = MibTableColumn
cdmsHaClusterHistNodeAddr = _CdmsHaClusterHistNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 10, 3, 8, 2, 1, 7),
    _CdmsHaClusterHistNodeAddr_Type()
)
cdmsHaClusterHistNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmsHaClusterHistNodeAddr.setStatus("current")
_CdmsNotifControl_ObjectIdentity = ObjectIdentity
cdmsNotifControl = _CdmsNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13)
)


class _CdmsMediaPlayerRegisteredEnable_Type(TruthValue):
    """Custom type cdmsMediaPlayerRegisteredEnable based on TruthValue"""


_CdmsMediaPlayerRegisteredEnable_Object = MibScalar
cdmsMediaPlayerRegisteredEnable = _CdmsMediaPlayerRegisteredEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 1),
    _CdmsMediaPlayerRegisteredEnable_Type()
)
cdmsMediaPlayerRegisteredEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsMediaPlayerRegisteredEnable.setStatus("current")


class _CdmsMediaPlayerUpEnable_Type(TruthValue):
    """Custom type cdmsMediaPlayerUpEnable based on TruthValue"""


_CdmsMediaPlayerUpEnable_Object = MibScalar
cdmsMediaPlayerUpEnable = _CdmsMediaPlayerUpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 2),
    _CdmsMediaPlayerUpEnable_Type()
)
cdmsMediaPlayerUpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsMediaPlayerUpEnable.setStatus("current")


class _CdmsMediaPlayerDownEnable_Type(TruthValue):
    """Custom type cdmsMediaPlayerDownEnable based on TruthValue"""


_CdmsMediaPlayerDownEnable_Object = MibScalar
cdmsMediaPlayerDownEnable = _CdmsMediaPlayerDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 3),
    _CdmsMediaPlayerDownEnable_Type()
)
cdmsMediaPlayerDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsMediaPlayerDownEnable.setStatus("current")


class _CdmsMediaPlayerAddrTakenEnable_Type(TruthValue):
    """Custom type cdmsMediaPlayerAddrTakenEnable based on TruthValue"""


_CdmsMediaPlayerAddrTakenEnable_Object = MibScalar
cdmsMediaPlayerAddrTakenEnable = _CdmsMediaPlayerAddrTakenEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 4),
    _CdmsMediaPlayerAddrTakenEnable_Type()
)
cdmsMediaPlayerAddrTakenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsMediaPlayerAddrTakenEnable.setStatus("current")


class _CdmsHaClusterNodeUpEnable_Type(TruthValue):
    """Custom type cdmsHaClusterNodeUpEnable based on TruthValue"""


_CdmsHaClusterNodeUpEnable_Object = MibScalar
cdmsHaClusterNodeUpEnable = _CdmsHaClusterNodeUpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 5),
    _CdmsHaClusterNodeUpEnable_Type()
)
cdmsHaClusterNodeUpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsHaClusterNodeUpEnable.setStatus("current")


class _CdmsHaClusterNodeDownEnable_Type(TruthValue):
    """Custom type cdmsHaClusterNodeDownEnable based on TruthValue"""


_CdmsHaClusterNodeDownEnable_Object = MibScalar
cdmsHaClusterNodeDownEnable = _CdmsHaClusterNodeDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 6),
    _CdmsHaClusterNodeDownEnable_Type()
)
cdmsHaClusterNodeDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsHaClusterNodeDownEnable.setStatus("current")


class _CdmsHaClusterConfigChangeEnable_Type(TruthValue):
    """Custom type cdmsHaClusterConfigChangeEnable based on TruthValue"""


_CdmsHaClusterConfigChangeEnable_Object = MibScalar
cdmsHaClusterConfigChangeEnable = _CdmsHaClusterConfigChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 1, 13, 7),
    _CdmsHaClusterConfigChangeEnable_Type()
)
cdmsHaClusterConfigChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdmsHaClusterConfigChangeEnable.setStatus("current")
_CiscoDmsMonitorMIBConform_ObjectIdentity = ObjectIdentity
ciscoDmsMonitorMIBConform = _CiscoDmsMonitorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2)
)
_CiscoDmsMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDmsMonitorMIBCompliances = _CiscoDmsMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 1)
)
_CiscoDmsMonitorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDmsMonitorMIBGroups = _CiscoDmsMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2)
)

# Managed Objects groups

ciscoDmsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 1)
)
ciscoDmsSystemGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMajorVersion"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMinorVersion"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsPatchVersion"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsAdministrator"))
)
if mibBuilder.loadTexts:
    ciscoDmsSystemGroup.setStatus("current")

ciscoDmsFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 2)
)
ciscoDmsFeatureGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensableFeatures"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeatures"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLastLicenseUpdate"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeatureLimit"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeatureDescription"))
)
if mibBuilder.loadTexts:
    ciscoDmsFeatureGroup.setStatus("current")

ciscoDmsFeatureAdvancedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 3)
)
ciscoDmsFeatureAdvancedGroup.setObjects(
    ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLicensedFeatureInstallDate")
)
if mibBuilder.loadTexts:
    ciscoDmsFeatureAdvancedGroup.setStatus("current")

ciscoDmsInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 4)
)
ciscoDmsInventoryGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumMediaIngestionDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumMediaPlayerDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumVideoPortalDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementMacAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementMetadata"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementState"))
)
if mibBuilder.loadTexts:
    ciscoDmsInventoryGroup.setStatus("current")

ciscoDmsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 5)
)
ciscoDmsServerGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsServerState"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsServerStatus"))
)
if mibBuilder.loadTexts:
    ciscoDmsServerGroup.setStatus("current")

ciscoDamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 6)
)
ciscoDamGroup.setObjects(
    ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumContentElements")
)
if mibBuilder.loadTexts:
    ciscoDamGroup.setStatus("current")

ciscoDmsSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 7)
)
ciscoDmsSecurityGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumAuthenRequests"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumAuthenRequestsApproved"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumAuthenRequestsDeclined"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsAuthenticationMode"))
)
if mibBuilder.loadTexts:
    ciscoDmsSecurityGroup.setStatus("current")

ciscoDmsUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 8)
)
ciscoDmsUserGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumUsers"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumActiveDmmUsers"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumActiveVpUsers"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsLastUserLastChange"))
)
if mibBuilder.loadTexts:
    ciscoDmsUserGroup.setStatus("current")

ciscoDmsEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 9)
)
ciscoDmsEventGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumEvents"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumEventRate"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumAlarms"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumAlarmRate"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumNotifications"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumNotificationRate"))
)
if mibBuilder.loadTexts:
    ciscoDmsEventGroup.setStatus("current")

ciscoDmsNotificationCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 10)
)
ciscoDmsNotificationCntlGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerRegisteredEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerUpEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerDownEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerAddrTakenEnable"))
)
if mibBuilder.loadTexts:
    ciscoDmsNotificationCntlGroup.setStatus("deprecated")

ciscoDmsHaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 13)
)
ciscoDmsHaGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNodeUpEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNodeDownEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterConfigChangeEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterEnabled"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterName"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNumTotalDmms"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNumActiveDmms"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterDmmVipType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterDmmVip"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaDmmClusterMemberIsPrimary"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaDmmClusterMemberOperState"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterNumClusters"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberIsPrimary"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaVpClusterMemberOperState"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastDmmStatusChangeTime"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastDmmStatusChangeAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastDmmStatusChangeAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastVpStatusChangeTime"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastVpStatusChangeCluster"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastStatusChangeVpAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterLastVpStatusChangeVpAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistoryMaxRecords"))
)
if mibBuilder.loadTexts:
    ciscoDmsHaGroup.setStatus("current")

ciscoDmsHaAdvancedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 14)
)
ciscoDmsHaAdvancedGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistTimestamp"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistClusterName"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeNewStatus"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddr"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistoryMaxRecords"))
)
if mibBuilder.loadTexts:
    ciscoDmsHaAdvancedGroup.setStatus("current")

ciscoDmsNotificationCntlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 15)
)
ciscoDmsNotificationCntlGroupRev1.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerRegisteredEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerUpEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerDownEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsMediaPlayerAddrTakenEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNodeUpEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterNodeDownEnable"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterConfigChangeEnable"))
)
if mibBuilder.loadTexts:
    ciscoDmsNotificationCntlGroupRev1.setStatus("current")


# Notification objects

ciscoDmsMediaPlayerRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 1)
)
ciscoDmsMediaPlayerRegistered.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumMediaPlayerDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementMacAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddress"))
)
if mibBuilder.loadTexts:
    ciscoDmsMediaPlayerRegistered.setStatus(
        "current"
    )

ciscoDmsMediaPlayerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 2)
)
ciscoDmsMediaPlayerUp.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumMediaPlayerDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementMacAddress"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddress"))
)
if mibBuilder.loadTexts:
    ciscoDmsMediaPlayerUp.setStatus(
        "current"
    )

ciscoDmsMediaPlayerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 3)
)
ciscoDmsMediaPlayerDown.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsNumMediaPlayerDevices"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddress"))
)
if mibBuilder.loadTexts:
    ciscoDmsMediaPlayerDown.setStatus(
        "current"
    )

ciscoDmsMediaPlayerAddrTaken = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 4)
)
ciscoDmsMediaPlayerAddrTaken.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsInventoryElementAddress"))
)
if mibBuilder.loadTexts:
    ciscoDmsMediaPlayerAddrTaken.setStatus(
        "current"
    )

ciscoDmsHaClusterNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 5)
)
ciscoDmsHaClusterNodeUp.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistClusterName"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddr"))
)
if mibBuilder.loadTexts:
    ciscoDmsHaClusterNodeUp.setStatus(
        "current"
    )

ciscoDmsHaClusterNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 6)
)
ciscoDmsHaClusterNodeDown.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistClusterName"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddrType"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistNodeAddr"))
)
if mibBuilder.loadTexts:
    ciscoDmsHaClusterNodeDown.setStatus(
        "current"
    )

cdmsDmsHaClusterConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 0, 7)
)
cdmsDmsHaClusterConfigChange.setObjects(
    ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsHaClusterHistClusterName")
)
if mibBuilder.loadTexts:
    cdmsDmsHaClusterConfigChange.setStatus(
        "current"
    )


# Notifications groups

ciscoDmsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 11)
)
ciscoDmsNotificationsGroup.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerRegistered"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerUp"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerDown"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerAddrTaken"))
)
if mibBuilder.loadTexts:
    ciscoDmsNotificationsGroup.setStatus(
        "deprecated"
    )

ciscoDmsAdvancedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 12)
)
ciscoDmsAdvancedNotificationsGroup.setObjects(
    ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "cdmsDmsHaClusterConfigChange")
)
if mibBuilder.loadTexts:
    ciscoDmsAdvancedNotificationsGroup.setStatus(
        "current"
    )

ciscoDmsNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 2, 16)
)
ciscoDmsNotificationsGroupRev1.setObjects(
      *(("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerRegistered"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerUp"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerDown"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsMediaPlayerAddrTaken"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsHaClusterNodeUp"),
        ("CISCO-DIGITAL-MEDIA-SYSTEMS-MIB", "ciscoDmsHaClusterNodeDown"))
)
if mibBuilder.loadTexts:
    ciscoDmsNotificationsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDmsMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDmsMonitorMIBCompliance.setStatus(
        "deprecated"
    )

ciscoDmsMonitorMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 655, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDmsMonitorMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIGITAL-MEDIA-SYSTEMS-MIB",
    **{"CDmsUserAuthenMethod": CDmsUserAuthenMethod,
       "CDmsServerType": CDmsServerType,
       "CDmsElementType": CDmsElementType,
       "CDmsFunctionalStatus": CDmsFunctionalStatus,
       "CDmsEmailAddress": CDmsEmailAddress,
       "CDmsLicensedFeature": CDmsLicensedFeature,
       "ciscoDigitalMediaSystemsMIB": ciscoDigitalMediaSystemsMIB,
       "ciscoDmsMonitorMIBNotifs": ciscoDmsMonitorMIBNotifs,
       "ciscoDmsMediaPlayerRegistered": ciscoDmsMediaPlayerRegistered,
       "ciscoDmsMediaPlayerUp": ciscoDmsMediaPlayerUp,
       "ciscoDmsMediaPlayerDown": ciscoDmsMediaPlayerDown,
       "ciscoDmsMediaPlayerAddrTaken": ciscoDmsMediaPlayerAddrTaken,
       "ciscoDmsHaClusterNodeUp": ciscoDmsHaClusterNodeUp,
       "ciscoDmsHaClusterNodeDown": ciscoDmsHaClusterNodeDown,
       "cdmsDmsHaClusterConfigChange": cdmsDmsHaClusterConfigChange,
       "ciscoDmsMonitorMIBObjects": ciscoDmsMonitorMIBObjects,
       "cdmsSystem": cdmsSystem,
       "cdmsMajorVersion": cdmsMajorVersion,
       "cdmsMinorVersion": cdmsMinorVersion,
       "cdmsPatchVersion": cdmsPatchVersion,
       "cdmsAdministrator": cdmsAdministrator,
       "cdmsFeatures": cdmsFeatures,
       "cdmsFeatureSummary": cdmsFeatureSummary,
       "cdmsLicensableFeatures": cdmsLicensableFeatures,
       "cdmsLicensedFeatures": cdmsLicensedFeatures,
       "cdmsLastLicenseUpdate": cdmsLastLicenseUpdate,
       "cdmsLicensedFeatureTable": cdmsLicensedFeatureTable,
       "cdmsLicensedFeatureEntry": cdmsLicensedFeatureEntry,
       "cdmsLicensedFeature": cdmsLicensedFeature,
       "cdmsLicensedFeatureIndex": cdmsLicensedFeatureIndex,
       "cdmsLicensedFeatureLimit": cdmsLicensedFeatureLimit,
       "cdmsLicensedFeatureDescription": cdmsLicensedFeatureDescription,
       "cdmsLicensedFeatureInstallDate": cdmsLicensedFeatureInstallDate,
       "cdmsLicensedFeatureLimitRev1": cdmsLicensedFeatureLimitRev1,
       "cdmsInventory": cdmsInventory,
       "cdmsInventoryGlobalCounters": cdmsInventoryGlobalCounters,
       "cdmsNumMediaIngestionDevices": cdmsNumMediaIngestionDevices,
       "cdmsNumMediaPlayerDevices": cdmsNumMediaPlayerDevices,
       "cdmsNumVideoPortalDevices": cdmsNumVideoPortalDevices,
       "cdmsInventoryTable": cdmsInventoryTable,
       "cdmsInventoryEntry": cdmsInventoryEntry,
       "cdmsInventoryElementType": cdmsInventoryElementType,
       "cdmsInventoryElementId": cdmsInventoryElementId,
       "cdmsInventoryElementMacAddress": cdmsInventoryElementMacAddress,
       "cdmsInventoryElementAddrType": cdmsInventoryElementAddrType,
       "cdmsInventoryElementAddress": cdmsInventoryElementAddress,
       "cdmsInventoryElementMetadata": cdmsInventoryElementMetadata,
       "cdmsInventoryElementState": cdmsInventoryElementState,
       "cdmsServers": cdmsServers,
       "cdmsServerTable": cdmsServerTable,
       "cdmsServerEntry": cdmsServerEntry,
       "cdmsServerType": cdmsServerType,
       "cdmsServerAddrType": cdmsServerAddrType,
       "cdmsServerAddress": cdmsServerAddress,
       "cdmsServerState": cdmsServerState,
       "cdmsServerStatus": cdmsServerStatus,
       "cdmsDamServices": cdmsDamServices,
       "cdmsDamGlobalCounters": cdmsDamGlobalCounters,
       "cdmsNumContentElements": cdmsNumContentElements,
       "cdmsNumAuthenRequestsApproved": cdmsNumAuthenRequestsApproved,
       "cdmsNumAuthenRequestsDeclined": cdmsNumAuthenRequestsDeclined,
       "cdmsSecurity": cdmsSecurity,
       "cdmsSecurityGlobalCounters": cdmsSecurityGlobalCounters,
       "cdmsNumAuthenRequests": cdmsNumAuthenRequests,
       "cdmsSecurityConfiguration": cdmsSecurityConfiguration,
       "cdmsAuthenticationMode": cdmsAuthenticationMode,
       "cdmsUserGroup": cdmsUserGroup,
       "cdmsNumUsers": cdmsNumUsers,
       "cdmsNumActiveDmmUsers": cdmsNumActiveDmmUsers,
       "cdmsNumActiveVpUsers": cdmsNumActiveVpUsers,
       "cdmsLastUserLastChange": cdmsLastUserLastChange,
       "cdmsEvents": cdmsEvents,
       "cdmsEventConfiguration": cdmsEventConfiguration,
       "cdmsEventStatistics": cdmsEventStatistics,
       "cdmsNumEvents": cdmsNumEvents,
       "cdmsNumEventRate": cdmsNumEventRate,
       "cdmsNumAlarms": cdmsNumAlarms,
       "cdmsNumAlarmRate": cdmsNumAlarmRate,
       "cdmsNumNotifications": cdmsNumNotifications,
       "cdmsNumNotificationRate": cdmsNumNotificationRate,
       "cdmsHa": cdmsHa,
       "cdmsHaClusterInfo": cdmsHaClusterInfo,
       "cdmsHaClusterEnabled": cdmsHaClusterEnabled,
       "cdmsHaClusterName": cdmsHaClusterName,
       "cdmsHaClusterComposition": cdmsHaClusterComposition,
       "cdmsHaDmmCluster": cdmsHaDmmCluster,
       "cdmsHaClusterNumTotalDmms": cdmsHaClusterNumTotalDmms,
       "cdmsHaClusterNumActiveDmms": cdmsHaClusterNumActiveDmms,
       "cdmsHaClusterDmmVipType": cdmsHaClusterDmmVipType,
       "cdmsHaClusterDmmVip": cdmsHaClusterDmmVip,
       "cdmsHaDmmClusterMemberTable": cdmsHaDmmClusterMemberTable,
       "cdmsHaDmmClusterMemberEntry": cdmsHaDmmClusterMemberEntry,
       "cdmsHaDmmClusterMemberAddrType": cdmsHaDmmClusterMemberAddrType,
       "cdmsHaDmmClusterMemberAddress": cdmsHaDmmClusterMemberAddress,
       "cdmsHaDmmClusterMemberIsPrimary": cdmsHaDmmClusterMemberIsPrimary,
       "cdmsHaDmmClusterMemberOperState": cdmsHaDmmClusterMemberOperState,
       "cdmsHaVpCluster": cdmsHaVpCluster,
       "cdmsHaVpClusterNumClusters": cdmsHaVpClusterNumClusters,
       "cdmsHaVpClusterMemberTable": cdmsHaVpClusterMemberTable,
       "cdmsHaVpClusterMemberEntry": cdmsHaVpClusterMemberEntry,
       "cdmsHaVpClusterMemberClusterName": cdmsHaVpClusterMemberClusterName,
       "cdmsHaVpClusterMemberVipType": cdmsHaVpClusterMemberVipType,
       "cdmsHaVpClusterMemberVip": cdmsHaVpClusterMemberVip,
       "cdmsHaVpClusterMemberAddrType": cdmsHaVpClusterMemberAddrType,
       "cdmsHaVpClusterMemberAddress": cdmsHaVpClusterMemberAddress,
       "cdmsHaVpClusterMemberIsPrimary": cdmsHaVpClusterMemberIsPrimary,
       "cdmsHaVpClusterMemberOperState": cdmsHaVpClusterMemberOperState,
       "cdmsHaClusterStatus": cdmsHaClusterStatus,
       "cdmsHaClusterLastDmmStatusChangeTime": cdmsHaClusterLastDmmStatusChangeTime,
       "cdmsHaClusterLastDmmStatusChangeAddrType": cdmsHaClusterLastDmmStatusChangeAddrType,
       "cdmsHaClusterLastDmmStatusChangeAddress": cdmsHaClusterLastDmmStatusChangeAddress,
       "cdmsHaClusterLastVpStatusChangeTime": cdmsHaClusterLastVpStatusChangeTime,
       "cdmsHaClusterLastVpStatusChangeCluster": cdmsHaClusterLastVpStatusChangeCluster,
       "cdmsHaClusterLastStatusChangeVpAddrType": cdmsHaClusterLastStatusChangeVpAddrType,
       "cdmsHaClusterLastVpStatusChangeVpAddress": cdmsHaClusterLastVpStatusChangeVpAddress,
       "cdmsHaClusterStatusHistory": cdmsHaClusterStatusHistory,
       "cdmsHaClusterHistoryMaxRecords": cdmsHaClusterHistoryMaxRecords,
       "cdmsHaClusterHistoryTable": cdmsHaClusterHistoryTable,
       "cdmsHaClusterHistoryEntry": cdmsHaClusterHistoryEntry,
       "cdmsHaClusterHistId": cdmsHaClusterHistId,
       "cdmsHaClusterHistTimestamp": cdmsHaClusterHistTimestamp,
       "cdmsHaClusterHistClusterName": cdmsHaClusterHistClusterName,
       "cdmsHaClusterHistNodeType": cdmsHaClusterHistNodeType,
       "cdmsHaClusterHistNodeNewStatus": cdmsHaClusterHistNodeNewStatus,
       "cdmsHaClusterHistNodeAddrType": cdmsHaClusterHistNodeAddrType,
       "cdmsHaClusterHistNodeAddr": cdmsHaClusterHistNodeAddr,
       "cdmsNotifControl": cdmsNotifControl,
       "cdmsMediaPlayerRegisteredEnable": cdmsMediaPlayerRegisteredEnable,
       "cdmsMediaPlayerUpEnable": cdmsMediaPlayerUpEnable,
       "cdmsMediaPlayerDownEnable": cdmsMediaPlayerDownEnable,
       "cdmsMediaPlayerAddrTakenEnable": cdmsMediaPlayerAddrTakenEnable,
       "cdmsHaClusterNodeUpEnable": cdmsHaClusterNodeUpEnable,
       "cdmsHaClusterNodeDownEnable": cdmsHaClusterNodeDownEnable,
       "cdmsHaClusterConfigChangeEnable": cdmsHaClusterConfigChangeEnable,
       "ciscoDmsMonitorMIBConform": ciscoDmsMonitorMIBConform,
       "ciscoDmsMonitorMIBCompliances": ciscoDmsMonitorMIBCompliances,
       "ciscoDmsMonitorMIBCompliance": ciscoDmsMonitorMIBCompliance,
       "ciscoDmsMonitorMIBComplianceRev1": ciscoDmsMonitorMIBComplianceRev1,
       "ciscoDmsMonitorMIBGroups": ciscoDmsMonitorMIBGroups,
       "ciscoDmsSystemGroup": ciscoDmsSystemGroup,
       "ciscoDmsFeatureGroup": ciscoDmsFeatureGroup,
       "ciscoDmsFeatureAdvancedGroup": ciscoDmsFeatureAdvancedGroup,
       "ciscoDmsInventoryGroup": ciscoDmsInventoryGroup,
       "ciscoDmsServerGroup": ciscoDmsServerGroup,
       "ciscoDamGroup": ciscoDamGroup,
       "ciscoDmsSecurityGroup": ciscoDmsSecurityGroup,
       "ciscoDmsUserGroup": ciscoDmsUserGroup,
       "ciscoDmsEventGroup": ciscoDmsEventGroup,
       "ciscoDmsNotificationCntlGroup": ciscoDmsNotificationCntlGroup,
       "ciscoDmsNotificationsGroup": ciscoDmsNotificationsGroup,
       "ciscoDmsAdvancedNotificationsGroup": ciscoDmsAdvancedNotificationsGroup,
       "ciscoDmsHaGroup": ciscoDmsHaGroup,
       "ciscoDmsHaAdvancedGroup": ciscoDmsHaAdvancedGroup,
       "ciscoDmsNotificationCntlGroupRev1": ciscoDmsNotificationCntlGroupRev1,
       "ciscoDmsNotificationsGroupRev1": ciscoDmsNotificationsGroupRev1}
)
