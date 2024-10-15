# SNMP MIB module (CISCO-IPSLA-VIDEO-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-VIDEO-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:05 2024
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

(CvcVideoProfile,) = mibBuilder.importSymbols(
    "CISCO-VIDEO-SESSION-MIB",
    "CvcVideoProfile")

(CvcVideoResolution,) = mibBuilder.importSymbols(
    "CISCO-VIDEO-TC",
    "CvcVideoResolution")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIpslaVideoProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766)
)
ciscoIpslaVideoProfileMIB.setRevisions(
        ("2011-01-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpslaVideoProfileMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoProfileMIBNotifs = _CiscoIpslaVideoProfileMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 0)
)
_CiscoIpslaVideoProfileMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoProfileMIBObjects = _CiscoIpslaVideoProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1)
)
_CipslaVideoProfile_ObjectIdentity = ObjectIdentity
cipslaVideoProfile = _CipslaVideoProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1)
)
_CipslaVideoProfileTable_Object = MibTable
cipslaVideoProfileTable = _CipslaVideoProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipslaVideoProfileTable.setStatus("current")
_CipslaVideoProfileEntry_Object = MibTableRow
cipslaVideoProfileEntry = _CipslaVideoProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1)
)
cipslaVideoProfileEntry.setIndexNames(
    (0, "CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileID"),
)
if mibBuilder.loadTexts:
    cipslaVideoProfileEntry.setStatus("current")


class _CipslaVideoProfileID_Type(Unsigned32):
    """Custom type cipslaVideoProfileID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CipslaVideoProfileID_Type.__name__ = "Unsigned32"
_CipslaVideoProfileID_Object = MibTableColumn
cipslaVideoProfileID = _CipslaVideoProfileID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 1),
    _CipslaVideoProfileID_Type()
)
cipslaVideoProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaVideoProfileID.setStatus("current")
_CipslaVideoProfileRowStatus_Type = RowStatus
_CipslaVideoProfileRowStatus_Object = MibTableColumn
cipslaVideoProfileRowStatus = _CipslaVideoProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 2),
    _CipslaVideoProfileRowStatus_Type()
)
cipslaVideoProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileRowStatus.setStatus("current")
_CipslaVideoProfileStorageType_Type = StorageType
_CipslaVideoProfileStorageType_Object = MibTableColumn
cipslaVideoProfileStorageType = _CipslaVideoProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 3),
    _CipslaVideoProfileStorageType_Type()
)
cipslaVideoProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileStorageType.setStatus("current")
_CipslaVideoProfileName_Type = SnmpAdminString
_CipslaVideoProfileName_Object = MibTableColumn
cipslaVideoProfileName = _CipslaVideoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 4),
    _CipslaVideoProfileName_Type()
)
cipslaVideoProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileName.setStatus("current")
_CipslaVideoProfileDescription_Type = SnmpAdminString
_CipslaVideoProfileDescription_Object = MibTableColumn
cipslaVideoProfileDescription = _CipslaVideoProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 5),
    _CipslaVideoProfileDescription_Type()
)
cipslaVideoProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileDescription.setStatus("current")


class _CipslaVideoProfileEndpointType_Type(Integer32):
    """Custom type cipslaVideoProfileEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21,
              22,
              31,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cp99xx", 31),
          ("cts1k", 21),
          ("cts3k", 22),
          ("custom", 1),
          ("unknown", 9999))
    )


_CipslaVideoProfileEndpointType_Type.__name__ = "Integer32"
_CipslaVideoProfileEndpointType_Object = MibTableColumn
cipslaVideoProfileEndpointType = _CipslaVideoProfileEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 6),
    _CipslaVideoProfileEndpointType_Type()
)
cipslaVideoProfileEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileEndpointType.setStatus("current")


class _CipslaVideoProfileCodec_Type(CvcVideoProfile):
    """Custom type cipslaVideoProfileCodec based on CvcVideoProfile"""


_CipslaVideoProfileCodec_Object = MibTableColumn
cipslaVideoProfileCodec = _CipslaVideoProfileCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 7),
    _CipslaVideoProfileCodec_Type()
)
cipslaVideoProfileCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileCodec.setStatus("current")


class _CipslaVideoProfileVideoContents_Type(Integer32):
    """Custom type cipslaVideoProfileVideoContents based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("conferenceRoom", 1),
          ("other", 255),
          ("presentation", 3),
          ("singlePerson", 2),
          ("sports", 4),
          ("streetView", 5))
    )


_CipslaVideoProfileVideoContents_Type.__name__ = "Integer32"
_CipslaVideoProfileVideoContents_Object = MibTableColumn
cipslaVideoProfileVideoContents = _CipslaVideoProfileVideoContents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 8),
    _CipslaVideoProfileVideoContents_Type()
)
cipslaVideoProfileVideoContents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileVideoContents.setStatus("current")


class _CipslaVideoProfileFrameRate_Type(Unsigned32):
    """Custom type cipslaVideoProfileFrameRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120000),
    )


_CipslaVideoProfileFrameRate_Type.__name__ = "Unsigned32"
_CipslaVideoProfileFrameRate_Object = MibTableColumn
cipslaVideoProfileFrameRate = _CipslaVideoProfileFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 9),
    _CipslaVideoProfileFrameRate_Type()
)
cipslaVideoProfileFrameRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileFrameRate.setUnits("fpks")
_CipslaVideoProfileResolution_Type = CvcVideoResolution
_CipslaVideoProfileResolution_Object = MibTableColumn
cipslaVideoProfileResolution = _CipslaVideoProfileResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 10),
    _CipslaVideoProfileResolution_Type()
)
cipslaVideoProfileResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileResolution.setStatus("current")


class _CipslaVideoProfileAvgBitrate_Type(Unsigned32):
    """Custom type cipslaVideoProfileAvgBitrate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_CipslaVideoProfileAvgBitrate_Type.__name__ = "Unsigned32"
_CipslaVideoProfileAvgBitrate_Object = MibTableColumn
cipslaVideoProfileAvgBitrate = _CipslaVideoProfileAvgBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 11),
    _CipslaVideoProfileAvgBitrate_Type()
)
cipslaVideoProfileAvgBitrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileAvgBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileAvgBitrate.setUnits("kbps")


class _CipslaVideoProfileMaxBitrate_Type(Unsigned32):
    """Custom type cipslaVideoProfileMaxBitrate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240000),
    )


_CipslaVideoProfileMaxBitrate_Type.__name__ = "Unsigned32"
_CipslaVideoProfileMaxBitrate_Object = MibTableColumn
cipslaVideoProfileMaxBitrate = _CipslaVideoProfileMaxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 12),
    _CipslaVideoProfileMaxBitrate_Type()
)
cipslaVideoProfileMaxBitrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileMaxBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileMaxBitrate.setUnits("kbps")


class _CipslaVideoProfileMinBitrate_Type(Unsigned32):
    """Custom type cipslaVideoProfileMinBitrate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_CipslaVideoProfileMinBitrate_Type.__name__ = "Unsigned32"
_CipslaVideoProfileMinBitrate_Object = MibTableColumn
cipslaVideoProfileMinBitrate = _CipslaVideoProfileMinBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 13),
    _CipslaVideoProfileMinBitrate_Type()
)
cipslaVideoProfileMinBitrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileMinBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileMinBitrate.setUnits("kbps")


class _CipslaVideoProfileBitrateWindowSize_Type(Unsigned32):
    """Custom type cipslaVideoProfileBitrateWindowSize based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CipslaVideoProfileBitrateWindowSize_Type.__name__ = "Unsigned32"
_CipslaVideoProfileBitrateWindowSize_Object = MibTableColumn
cipslaVideoProfileBitrateWindowSize = _CipslaVideoProfileBitrateWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 14),
    _CipslaVideoProfileBitrateWindowSize_Type()
)
cipslaVideoProfileBitrateWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileBitrateWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileBitrateWindowSize.setUnits("ms")


class _CipslaVideoProfileIframeMaxSize_Type(Unsigned32):
    """Custom type cipslaVideoProfileIframeMaxSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CipslaVideoProfileIframeMaxSize_Type.__name__ = "Unsigned32"
_CipslaVideoProfileIframeMaxSize_Object = MibTableColumn
cipslaVideoProfileIframeMaxSize = _CipslaVideoProfileIframeMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 15),
    _CipslaVideoProfileIframeMaxSize_Type()
)
cipslaVideoProfileIframeMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileIframeMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileIframeMaxSize.setUnits("kB")


class _CipslaVideoProfileIframeRefreshInterval_Type(Unsigned32):
    """Custom type cipslaVideoProfileIframeRefreshInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CipslaVideoProfileIframeRefreshInterval_Type.__name__ = "Unsigned32"
_CipslaVideoProfileIframeRefreshInterval_Object = MibTableColumn
cipslaVideoProfileIframeRefreshInterval = _CipslaVideoProfileIframeRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 16),
    _CipslaVideoProfileIframeRefreshInterval_Type()
)
cipslaVideoProfileIframeRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileIframeRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileIframeRefreshInterval.setUnits("ms")


class _CipslaVideoProfileRtpAvgSize_Type(Unsigned32):
    """Custom type cipslaVideoProfileRtpAvgSize based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1600),
    )


_CipslaVideoProfileRtpAvgSize_Type.__name__ = "Unsigned32"
_CipslaVideoProfileRtpAvgSize_Object = MibTableColumn
cipslaVideoProfileRtpAvgSize = _CipslaVideoProfileRtpAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 17),
    _CipslaVideoProfileRtpAvgSize_Type()
)
cipslaVideoProfileRtpAvgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileRtpAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoProfileRtpAvgSize.setUnits("byte")


class _CipslaVideoProfileRtpJitterPattern_Type(Integer32):
    """Custom type cipslaVideoProfileRtpJitterPattern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bursty", 1),
          ("other", 99),
          ("shaped", 2))
    )


_CipslaVideoProfileRtpJitterPattern_Type.__name__ = "Integer32"
_CipslaVideoProfileRtpJitterPattern_Object = MibTableColumn
cipslaVideoProfileRtpJitterPattern = _CipslaVideoProfileRtpJitterPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 18),
    _CipslaVideoProfileRtpJitterPattern_Type()
)
cipslaVideoProfileRtpJitterPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaVideoProfileRtpJitterPattern.setStatus("current")
_CiscoIpslaVideoProfileMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoProfileMIBConform = _CiscoIpslaVideoProfileMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2)
)
_CiscoIpslaVideoProfileMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoProfileMIBCompliances = _CiscoIpslaVideoProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 1)
)
_CiscoIpslaVideoProfileMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoProfileMIBGroups = _CiscoIpslaVideoProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2)
)

# Managed Objects groups

ciscoIpslaVideoProfileBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2, 1)
)
ciscoIpslaVideoProfileBaseGroup.setObjects(
      *(("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRowStatus"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileStorageType"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileDescription"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileName"))
)
if mibBuilder.loadTexts:
    ciscoIpslaVideoProfileBaseGroup.setStatus("current")

ciscoIpslaVideoProfileIsrg2Pvdm3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2, 2)
)
ciscoIpslaVideoProfileIsrg2Pvdm3Group.setObjects(
      *(("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileEndpointType"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileCodec"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileVideoContents"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileFrameRate"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileResolution"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileAvgBitrate"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileMaxBitrate"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileMinBitrate"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileBitrateWindowSize"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileIframeMaxSize"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileIframeRefreshInterval"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRtpAvgSize"),
        ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRtpJitterPattern"))
)
if mibBuilder.loadTexts:
    ciscoIpslaVideoProfileIsrg2Pvdm3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpslaVideoProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpslaVideoProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-VIDEO-PROFILE-MIB",
    **{"ciscoIpslaVideoProfileMIB": ciscoIpslaVideoProfileMIB,
       "ciscoIpslaVideoProfileMIBNotifs": ciscoIpslaVideoProfileMIBNotifs,
       "ciscoIpslaVideoProfileMIBObjects": ciscoIpslaVideoProfileMIBObjects,
       "cipslaVideoProfile": cipslaVideoProfile,
       "cipslaVideoProfileTable": cipslaVideoProfileTable,
       "cipslaVideoProfileEntry": cipslaVideoProfileEntry,
       "cipslaVideoProfileID": cipslaVideoProfileID,
       "cipslaVideoProfileRowStatus": cipslaVideoProfileRowStatus,
       "cipslaVideoProfileStorageType": cipslaVideoProfileStorageType,
       "cipslaVideoProfileName": cipslaVideoProfileName,
       "cipslaVideoProfileDescription": cipslaVideoProfileDescription,
       "cipslaVideoProfileEndpointType": cipslaVideoProfileEndpointType,
       "cipslaVideoProfileCodec": cipslaVideoProfileCodec,
       "cipslaVideoProfileVideoContents": cipslaVideoProfileVideoContents,
       "cipslaVideoProfileFrameRate": cipslaVideoProfileFrameRate,
       "cipslaVideoProfileResolution": cipslaVideoProfileResolution,
       "cipslaVideoProfileAvgBitrate": cipslaVideoProfileAvgBitrate,
       "cipslaVideoProfileMaxBitrate": cipslaVideoProfileMaxBitrate,
       "cipslaVideoProfileMinBitrate": cipslaVideoProfileMinBitrate,
       "cipslaVideoProfileBitrateWindowSize": cipslaVideoProfileBitrateWindowSize,
       "cipslaVideoProfileIframeMaxSize": cipslaVideoProfileIframeMaxSize,
       "cipslaVideoProfileIframeRefreshInterval": cipslaVideoProfileIframeRefreshInterval,
       "cipslaVideoProfileRtpAvgSize": cipslaVideoProfileRtpAvgSize,
       "cipslaVideoProfileRtpJitterPattern": cipslaVideoProfileRtpJitterPattern,
       "ciscoIpslaVideoProfileMIBConform": ciscoIpslaVideoProfileMIBConform,
       "ciscoIpslaVideoProfileMIBCompliances": ciscoIpslaVideoProfileMIBCompliances,
       "ciscoIpslaVideoProfileMIBCompliance": ciscoIpslaVideoProfileMIBCompliance,
       "ciscoIpslaVideoProfileMIBGroups": ciscoIpslaVideoProfileMIBGroups,
       "ciscoIpslaVideoProfileBaseGroup": ciscoIpslaVideoProfileBaseGroup,
       "ciscoIpslaVideoProfileIsrg2Pvdm3Group": ciscoIpslaVideoProfileIsrg2Pvdm3Group}
)
