# SNMP MIB module (CISCO-DEVICE-LOCATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DEVICE-LOCATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:56 2024
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

(CountryCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode")

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

ciscoDeviceLocationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732)
)
ciscoDeviceLocationMIB.setRevisions(
        ("2010-10-28 00:00",
         "2010-04-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CdlMIBNotifications_ObjectIdentity = ObjectIdentity
cdlMIBNotifications = _CdlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 0)
)
_CdlMIBObjects_ObjectIdentity = ObjectIdentity
cdlMIBObjects = _CdlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1)
)
_CdlMIBScalars_ObjectIdentity = ObjectIdentity
cdlMIBScalars = _CdlMIBScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 1)
)


class _CdlKey_Type(SnmpAdminString):
    """Custom type cdlKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CdlKey_Type.__name__ = "SnmpAdminString"
_CdlKey_Object = MibScalar
cdlKey = _CdlKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 1, 1),
    _CdlKey_Type()
)
cdlKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdlKey.setStatus("current")
_CdlLocationTable_Object = MibTable
cdlLocationTable = _CdlLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2)
)
if mibBuilder.loadTexts:
    cdlLocationTable.setStatus("current")
_CdlLocationEntry_Object = MibTableRow
cdlLocationEntry = _CdlLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1)
)
cdlLocationEntry.setIndexNames(
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlLocationIndex"),
)
if mibBuilder.loadTexts:
    cdlLocationEntry.setStatus("current")
_CdlLocationIndex_Type = Unsigned32
_CdlLocationIndex_Object = MibTableColumn
cdlLocationIndex = _CdlLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1, 1),
    _CdlLocationIndex_Type()
)
cdlLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdlLocationIndex.setStatus("current")


class _CdlLocationSubTypeCapability_Type(Bits):
    """Custom type cdlLocationSubTypeCapability based on Bits"""
    namedValues = NamedValues(
        *(("civic", 2),
          ("custom", 4),
          ("elin", 3),
          ("geoLocation", 1),
          ("noSubtypesConfigured", 0))
    )

_CdlLocationSubTypeCapability_Type.__name__ = "Bits"
_CdlLocationSubTypeCapability_Object = MibTableColumn
cdlLocationSubTypeCapability = _CdlLocationSubTypeCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1, 2),
    _CdlLocationSubTypeCapability_Type()
)
cdlLocationSubTypeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdlLocationSubTypeCapability.setStatus("current")
_CdlLocationCountryCode_Type = CountryCode
_CdlLocationCountryCode_Object = MibTableColumn
cdlLocationCountryCode = _CdlLocationCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1, 3),
    _CdlLocationCountryCode_Type()
)
cdlLocationCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdlLocationCountryCode.setStatus("current")


class _CdlLocationTargetType_Type(Integer32):
    """Custom type cdlLocationTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("ipv4Addr", 2))
    )


_CdlLocationTargetType_Type.__name__ = "Integer32"
_CdlLocationTargetType_Object = MibTableColumn
cdlLocationTargetType = _CdlLocationTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1, 4),
    _CdlLocationTargetType_Type()
)
cdlLocationTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdlLocationTargetType.setStatus("current")


class _CdlLocationTargetIdentifier_Type(OctetString):
    """Custom type cdlLocationTargetIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CdlLocationTargetIdentifier_Type.__name__ = "OctetString"
_CdlLocationTargetIdentifier_Object = MibTableColumn
cdlLocationTargetIdentifier = _CdlLocationTargetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 2, 1, 5),
    _CdlLocationTargetIdentifier_Type()
)
cdlLocationTargetIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdlLocationTargetIdentifier.setStatus("current")
_CdlCivicAddrLocationTable_Object = MibTable
cdlCivicAddrLocationTable = _CdlCivicAddrLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3)
)
if mibBuilder.loadTexts:
    cdlCivicAddrLocationTable.setStatus("current")
_CdlCivicAddrLocationEntry_Object = MibTableRow
cdlCivicAddrLocationEntry = _CdlCivicAddrLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3, 1)
)
cdlCivicAddrLocationEntry.setIndexNames(
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlLocationIndex"),
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlCivicAddrLocationType"),
)
if mibBuilder.loadTexts:
    cdlCivicAddrLocationEntry.setStatus("current")


class _CdlCivicAddrLocationType_Type(Integer32):
    """Custom type cdlCivicAddrLocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("additionalCode", 32),
          ("additionalLoc", 22),
          ("building", 25),
          ("city", 3),
          ("cityDivision", 4),
          ("county", 2),
          ("floor", 27),
          ("house", 19),
          ("landmark", 21),
          ("leadingStreetDirection", 16),
          ("name", 23),
          ("neighborhood", 5),
          ("place", 29),
          ("postOffiiceBox", 31),
          ("postalCommunityName", 30),
          ("primaryRoad", 34),
          ("roadBranch", 36),
          ("roadSection", 35),
          ("roadSubBranch", 37),
          ("room", 28),
          ("seat", 33),
          ("state", 1),
          ("streetGroup", 6),
          ("streetNamePostMod", 39),
          ("streetNamePreMod", 38),
          ("streetNumber", 20),
          ("streetSuffix", 18),
          ("trailingStreetDirection", 17),
          ("unit", 26),
          ("zipcode", 24))
    )


_CdlCivicAddrLocationType_Type.__name__ = "Integer32"
_CdlCivicAddrLocationType_Object = MibTableColumn
cdlCivicAddrLocationType = _CdlCivicAddrLocationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3, 1, 1),
    _CdlCivicAddrLocationType_Type()
)
cdlCivicAddrLocationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdlCivicAddrLocationType.setStatus("current")
_CdlCivicAddrLocationValue_Type = SnmpAdminString
_CdlCivicAddrLocationValue_Object = MibTableColumn
cdlCivicAddrLocationValue = _CdlCivicAddrLocationValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3, 1, 2),
    _CdlCivicAddrLocationValue_Type()
)
cdlCivicAddrLocationValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCivicAddrLocationValue.setStatus("current")
_CdlCivicAddrLocationStorageType_Type = StorageType
_CdlCivicAddrLocationStorageType_Object = MibTableColumn
cdlCivicAddrLocationStorageType = _CdlCivicAddrLocationStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3, 1, 3),
    _CdlCivicAddrLocationStorageType_Type()
)
cdlCivicAddrLocationStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCivicAddrLocationStorageType.setStatus("current")
_CdlCivicAddrLocationStatus_Type = RowStatus
_CdlCivicAddrLocationStatus_Object = MibTableColumn
cdlCivicAddrLocationStatus = _CdlCivicAddrLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 3, 1, 4),
    _CdlCivicAddrLocationStatus_Type()
)
cdlCivicAddrLocationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCivicAddrLocationStatus.setStatus("current")
_CdlCustomLocationTable_Object = MibTable
cdlCustomLocationTable = _CdlCustomLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4)
)
if mibBuilder.loadTexts:
    cdlCustomLocationTable.setStatus("current")
_CdlCustomLocationEntry_Object = MibTableRow
cdlCustomLocationEntry = _CdlCustomLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4, 1)
)
cdlCustomLocationEntry.setIndexNames(
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlLocationIndex"),
    (1, "CISCO-DEVICE-LOCATION-MIB", "cdlCustomLocationName"),
)
if mibBuilder.loadTexts:
    cdlCustomLocationEntry.setStatus("current")


class _CdlCustomLocationName_Type(SnmpAdminString):
    """Custom type cdlCustomLocationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CdlCustomLocationName_Type.__name__ = "SnmpAdminString"
_CdlCustomLocationName_Object = MibTableColumn
cdlCustomLocationName = _CdlCustomLocationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4, 1, 1),
    _CdlCustomLocationName_Type()
)
cdlCustomLocationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdlCustomLocationName.setStatus("current")


class _CdlCustomLocationValue_Type(SnmpAdminString):
    """Custom type cdlCustomLocationValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CdlCustomLocationValue_Type.__name__ = "SnmpAdminString"
_CdlCustomLocationValue_Object = MibTableColumn
cdlCustomLocationValue = _CdlCustomLocationValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4, 1, 2),
    _CdlCustomLocationValue_Type()
)
cdlCustomLocationValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCustomLocationValue.setStatus("current")


class _CdlCustomLocationStorageType_Type(StorageType):
    """Custom type cdlCustomLocationStorageType based on StorageType"""


_CdlCustomLocationStorageType_Object = MibTableColumn
cdlCustomLocationStorageType = _CdlCustomLocationStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4, 1, 3),
    _CdlCustomLocationStorageType_Type()
)
cdlCustomLocationStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCustomLocationStorageType.setStatus("current")
_CdlCustomLocationStatus_Type = RowStatus
_CdlCustomLocationStatus_Object = MibTableColumn
cdlCustomLocationStatus = _CdlCustomLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 4, 1, 4),
    _CdlCustomLocationStatus_Type()
)
cdlCustomLocationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlCustomLocationStatus.setStatus("current")
_CdlGeoLocationTable_Object = MibTable
cdlGeoLocationTable = _CdlGeoLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5)
)
if mibBuilder.loadTexts:
    cdlGeoLocationTable.setStatus("current")
_CdlGeoLocationEntry_Object = MibTableRow
cdlGeoLocationEntry = _CdlGeoLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1)
)
cdlGeoLocationEntry.setIndexNames(
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlLocationIndex"),
)
if mibBuilder.loadTexts:
    cdlGeoLocationEntry.setStatus("current")


class _CdlGeoLatitude_Type(SnmpAdminString):
    """Custom type cdlGeoLatitude based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdlGeoLatitude_Type.__name__ = "SnmpAdminString"
_CdlGeoLatitude_Object = MibTableColumn
cdlGeoLatitude = _CdlGeoLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 1),
    _CdlGeoLatitude_Type()
)
cdlGeoLatitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoLatitude.setStatus("current")
_CdlGeoLatitudeResolution_Type = SnmpAdminString
_CdlGeoLatitudeResolution_Object = MibTableColumn
cdlGeoLatitudeResolution = _CdlGeoLatitudeResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 2),
    _CdlGeoLatitudeResolution_Type()
)
cdlGeoLatitudeResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoLatitudeResolution.setStatus("current")


class _CdlGeoLongitude_Type(SnmpAdminString):
    """Custom type cdlGeoLongitude based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdlGeoLongitude_Type.__name__ = "SnmpAdminString"
_CdlGeoLongitude_Object = MibTableColumn
cdlGeoLongitude = _CdlGeoLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 3),
    _CdlGeoLongitude_Type()
)
cdlGeoLongitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoLongitude.setStatus("current")
_CdlGeoLongitudeResolution_Type = SnmpAdminString
_CdlGeoLongitudeResolution_Object = MibTableColumn
cdlGeoLongitudeResolution = _CdlGeoLongitudeResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 4),
    _CdlGeoLongitudeResolution_Type()
)
cdlGeoLongitudeResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoLongitudeResolution.setStatus("current")


class _CdlGeoAltitude_Type(SnmpAdminString):
    """Custom type cdlGeoAltitude based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdlGeoAltitude_Type.__name__ = "SnmpAdminString"
_CdlGeoAltitude_Object = MibTableColumn
cdlGeoAltitude = _CdlGeoAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 5),
    _CdlGeoAltitude_Type()
)
cdlGeoAltitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoAltitude.setStatus("current")


class _CdlGeoAltitudeType_Type(Integer32):
    """Custom type cdlGeoAltitudeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("floors", 2),
          ("meters", 1))
    )


_CdlGeoAltitudeType_Type.__name__ = "Integer32"
_CdlGeoAltitudeType_Object = MibTableColumn
cdlGeoAltitudeType = _CdlGeoAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 6),
    _CdlGeoAltitudeType_Type()
)
cdlGeoAltitudeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoAltitudeType.setStatus("current")


class _CdlGeoAltitudeResolution_Type(SnmpAdminString):
    """Custom type cdlGeoAltitudeResolution based on SnmpAdminString"""
    defaultValue = OctetString("10")


_CdlGeoAltitudeResolution_Object = MibTableColumn
cdlGeoAltitudeResolution = _CdlGeoAltitudeResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 7),
    _CdlGeoAltitudeResolution_Type()
)
cdlGeoAltitudeResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoAltitudeResolution.setStatus("current")


class _CdlGeoResolution_Type(SnmpAdminString):
    """Custom type cdlGeoResolution based on SnmpAdminString"""
    defaultValue = OctetString("10")


_CdlGeoResolution_Object = MibTableColumn
cdlGeoResolution = _CdlGeoResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 8),
    _CdlGeoResolution_Type()
)
cdlGeoResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoResolution.setStatus("current")


class _CdlGeoStorageType_Type(StorageType):
    """Custom type cdlGeoStorageType based on StorageType"""


_CdlGeoStorageType_Object = MibTableColumn
cdlGeoStorageType = _CdlGeoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 9),
    _CdlGeoStorageType_Type()
)
cdlGeoStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoStorageType.setStatus("current")
_CdlGeoStatus_Type = RowStatus
_CdlGeoStatus_Object = MibTableColumn
cdlGeoStatus = _CdlGeoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 5, 1, 10),
    _CdlGeoStatus_Type()
)
cdlGeoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdlGeoStatus.setStatus("current")
_CdlLocationPreferWeightTable_Object = MibTable
cdlLocationPreferWeightTable = _CdlLocationPreferWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 6)
)
if mibBuilder.loadTexts:
    cdlLocationPreferWeightTable.setStatus("current")
_CdlLocationPreferWeightEntry_Object = MibTableRow
cdlLocationPreferWeightEntry = _CdlLocationPreferWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 6, 1)
)
cdlLocationPreferWeightEntry.setIndexNames(
    (0, "CISCO-DEVICE-LOCATION-MIB", "cdlLocationPreferWeightType"),
)
if mibBuilder.loadTexts:
    cdlLocationPreferWeightEntry.setStatus("current")


class _CdlLocationPreferWeightType_Type(Integer32):
    """Custom type cdlLocationPreferWeightType based on Integer32"""
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
        *(("cdp", 5),
          ("dhcp", 3),
          ("lldp", 4),
          ("locp", 2),
          ("static", 1))
    )


_CdlLocationPreferWeightType_Type.__name__ = "Integer32"
_CdlLocationPreferWeightType_Object = MibTableColumn
cdlLocationPreferWeightType = _CdlLocationPreferWeightType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 6, 1, 1),
    _CdlLocationPreferWeightType_Type()
)
cdlLocationPreferWeightType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdlLocationPreferWeightType.setStatus("current")
_CdlLocationPreferWeightValue_Type = Unsigned32
_CdlLocationPreferWeightValue_Object = MibTableColumn
cdlLocationPreferWeightValue = _CdlLocationPreferWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 1, 6, 1, 2),
    _CdlLocationPreferWeightValue_Type()
)
cdlLocationPreferWeightValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdlLocationPreferWeightValue.setStatus("current")
_CdlMIBConform_ObjectIdentity = ObjectIdentity
cdlMIBConform = _CdlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2)
)
_CdlMIBCompliances_ObjectIdentity = ObjectIdentity
cdlMIBCompliances = _CdlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 1)
)
_CdlMIBGroups_ObjectIdentity = ObjectIdentity
cdlMIBGroups = _CdlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2)
)

# Managed Objects groups

cdlLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2, 1)
)
cdlLocationGroup.setObjects(
      *(("CISCO-DEVICE-LOCATION-MIB", "cdlLocationSubTypeCapability"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlLocationCountryCode"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlLocationTargetType"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlLocationTargetIdentifier"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlKey"))
)
if mibBuilder.loadTexts:
    cdlLocationGroup.setStatus("current")

cdlCivicAddrLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2, 2)
)
cdlCivicAddrLocationGroup.setObjects(
      *(("CISCO-DEVICE-LOCATION-MIB", "cdlCivicAddrLocationValue"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlCivicAddrLocationStatus"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlCivicAddrLocationStorageType"))
)
if mibBuilder.loadTexts:
    cdlCivicAddrLocationGroup.setStatus("current")

cdlCustomLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2, 3)
)
cdlCustomLocationGroup.setObjects(
      *(("CISCO-DEVICE-LOCATION-MIB", "cdlCustomLocationValue"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlCustomLocationStatus"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlCustomLocationStorageType"))
)
if mibBuilder.loadTexts:
    cdlCustomLocationGroup.setStatus("current")

cdlGeoLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2, 4)
)
cdlGeoLocationGroup.setObjects(
      *(("CISCO-DEVICE-LOCATION-MIB", "cdlGeoLatitude"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoLatitudeResolution"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoLongitude"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoLongitudeResolution"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoAltitude"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoAltitudeType"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoAltitudeResolution"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoResolution"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoStatus"),
        ("CISCO-DEVICE-LOCATION-MIB", "cdlGeoStorageType"))
)
if mibBuilder.loadTexts:
    cdlGeoLocationGroup.setStatus("current")

cdlLocationPreferWeightGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 2, 5)
)
cdlLocationPreferWeightGroup.setObjects(
    ("CISCO-DEVICE-LOCATION-MIB", "cdlLocationPreferWeightValue")
)
if mibBuilder.loadTexts:
    cdlLocationPreferWeightGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cdlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cdlMIBCompliance.setStatus(
        "deprecated"
    )

cdlMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 732, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cdlMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DEVICE-LOCATION-MIB",
    **{"ciscoDeviceLocationMIB": ciscoDeviceLocationMIB,
       "cdlMIBNotifications": cdlMIBNotifications,
       "cdlMIBObjects": cdlMIBObjects,
       "cdlMIBScalars": cdlMIBScalars,
       "cdlKey": cdlKey,
       "cdlLocationTable": cdlLocationTable,
       "cdlLocationEntry": cdlLocationEntry,
       "cdlLocationIndex": cdlLocationIndex,
       "cdlLocationSubTypeCapability": cdlLocationSubTypeCapability,
       "cdlLocationCountryCode": cdlLocationCountryCode,
       "cdlLocationTargetType": cdlLocationTargetType,
       "cdlLocationTargetIdentifier": cdlLocationTargetIdentifier,
       "cdlCivicAddrLocationTable": cdlCivicAddrLocationTable,
       "cdlCivicAddrLocationEntry": cdlCivicAddrLocationEntry,
       "cdlCivicAddrLocationType": cdlCivicAddrLocationType,
       "cdlCivicAddrLocationValue": cdlCivicAddrLocationValue,
       "cdlCivicAddrLocationStorageType": cdlCivicAddrLocationStorageType,
       "cdlCivicAddrLocationStatus": cdlCivicAddrLocationStatus,
       "cdlCustomLocationTable": cdlCustomLocationTable,
       "cdlCustomLocationEntry": cdlCustomLocationEntry,
       "cdlCustomLocationName": cdlCustomLocationName,
       "cdlCustomLocationValue": cdlCustomLocationValue,
       "cdlCustomLocationStorageType": cdlCustomLocationStorageType,
       "cdlCustomLocationStatus": cdlCustomLocationStatus,
       "cdlGeoLocationTable": cdlGeoLocationTable,
       "cdlGeoLocationEntry": cdlGeoLocationEntry,
       "cdlGeoLatitude": cdlGeoLatitude,
       "cdlGeoLatitudeResolution": cdlGeoLatitudeResolution,
       "cdlGeoLongitude": cdlGeoLongitude,
       "cdlGeoLongitudeResolution": cdlGeoLongitudeResolution,
       "cdlGeoAltitude": cdlGeoAltitude,
       "cdlGeoAltitudeType": cdlGeoAltitudeType,
       "cdlGeoAltitudeResolution": cdlGeoAltitudeResolution,
       "cdlGeoResolution": cdlGeoResolution,
       "cdlGeoStorageType": cdlGeoStorageType,
       "cdlGeoStatus": cdlGeoStatus,
       "cdlLocationPreferWeightTable": cdlLocationPreferWeightTable,
       "cdlLocationPreferWeightEntry": cdlLocationPreferWeightEntry,
       "cdlLocationPreferWeightType": cdlLocationPreferWeightType,
       "cdlLocationPreferWeightValue": cdlLocationPreferWeightValue,
       "cdlMIBConform": cdlMIBConform,
       "cdlMIBCompliances": cdlMIBCompliances,
       "cdlMIBCompliance": cdlMIBCompliance,
       "cdlMIBComplianceRev1": cdlMIBComplianceRev1,
       "cdlMIBGroups": cdlMIBGroups,
       "cdlLocationGroup": cdlLocationGroup,
       "cdlCivicAddrLocationGroup": cdlCivicAddrLocationGroup,
       "cdlCustomLocationGroup": cdlCustomLocationGroup,
       "cdlGeoLocationGroup": cdlGeoLocationGroup,
       "cdlLocationPreferWeightGroup": cdlLocationPreferWeightGroup}
)
