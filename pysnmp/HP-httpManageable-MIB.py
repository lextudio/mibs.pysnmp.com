# SNMP MIB module (HP-httpManageable-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-httpManageable-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:14 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpHttpMgMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1)
)
hpHttpMgMod.setRevisions(
        ("1997-06-26 00:00",
         "1996-06-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Utf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpWebMgmt_ObjectIdentity = ObjectIdentity
hpWebMgmt = _HpWebMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36)
)
_HpHttpMgTraps_ObjectIdentity = ObjectIdentity
hpHttpMgTraps = _HpHttpMgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0)
)
_HpHttpMgObjects_ObjectIdentity = ObjectIdentity
hpHttpMgObjects = _HpHttpMgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1)
)
_HpHttpMgDefaults_ObjectIdentity = ObjectIdentity
hpHttpMgDefaults = _HpHttpMgDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 1)
)
_HpHttpMgDefaultURL_Type = Utf8String
_HpHttpMgDefaultURL_Object = MibScalar
hpHttpMgDefaultURL = _HpHttpMgDefaultURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 1, 1),
    _HpHttpMgDefaultURL_Type()
)
hpHttpMgDefaultURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDefaultURL.setStatus("current")
_HpHttpMgNetCitizen_ObjectIdentity = ObjectIdentity
hpHttpMgNetCitizen = _HpHttpMgNetCitizen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2)
)
_HpHttpMgMgmtSrvrURL_Type = Utf8String
_HpHttpMgMgmtSrvrURL_Object = MibScalar
hpHttpMgMgmtSrvrURL = _HpHttpMgMgmtSrvrURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 1),
    _HpHttpMgMgmtSrvrURL_Type()
)
hpHttpMgMgmtSrvrURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgMgmtSrvrURL.setStatus("current")
_HpHttpMgID_Type = Utf8String
_HpHttpMgID_Object = MibScalar
hpHttpMgID = _HpHttpMgID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 2),
    _HpHttpMgID_Type()
)
hpHttpMgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgID.setStatus("current")


class _HpHttpMgHealth_Type(Integer32):
    """Custom type hpHttpMgHealth based on Integer32"""
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
        *(("critical", 5),
          ("information", 2),
          ("nonrecoverable", 6),
          ("ok", 3),
          ("unknown", 1),
          ("warning", 4))
    )


_HpHttpMgHealth_Type.__name__ = "Integer32"
_HpHttpMgHealth_Object = MibScalar
hpHttpMgHealth = _HpHttpMgHealth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 3),
    _HpHttpMgHealth_Type()
)
hpHttpMgHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgHealth.setStatus("current")
_HpHttpMgManufacturer_Type = Utf8String
_HpHttpMgManufacturer_Object = MibScalar
hpHttpMgManufacturer = _HpHttpMgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 4),
    _HpHttpMgManufacturer_Type()
)
hpHttpMgManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgManufacturer.setStatus("current")


class _HpHttpMgProduct_Type(Utf8String):
    """Custom type hpHttpMgProduct based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgProduct_Type.__name__ = "Utf8String"
_HpHttpMgProduct_Object = MibScalar
hpHttpMgProduct = _HpHttpMgProduct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 5),
    _HpHttpMgProduct_Type()
)
hpHttpMgProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgProduct.setStatus("current")


class _HpHttpMgVersion_Type(Utf8String):
    """Custom type hpHttpMgVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgVersion_Type.__name__ = "Utf8String"
_HpHttpMgVersion_Object = MibScalar
hpHttpMgVersion = _HpHttpMgVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 6),
    _HpHttpMgVersion_Type()
)
hpHttpMgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgVersion.setStatus("current")


class _HpHttpMgHWVersion_Type(Utf8String):
    """Custom type hpHttpMgHWVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgHWVersion_Type.__name__ = "Utf8String"
_HpHttpMgHWVersion_Object = MibScalar
hpHttpMgHWVersion = _HpHttpMgHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 7),
    _HpHttpMgHWVersion_Type()
)
hpHttpMgHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgHWVersion.setStatus("current")


class _HpHttpMgROMVersion_Type(Utf8String):
    """Custom type hpHttpMgROMVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgROMVersion_Type.__name__ = "Utf8String"
_HpHttpMgROMVersion_Object = MibScalar
hpHttpMgROMVersion = _HpHttpMgROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 8),
    _HpHttpMgROMVersion_Type()
)
hpHttpMgROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgROMVersion.setStatus("current")


class _HpHttpMgSerialNumber_Type(Utf8String):
    """Custom type hpHttpMgSerialNumber based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgSerialNumber_Type.__name__ = "Utf8String"
_HpHttpMgSerialNumber_Object = MibScalar
hpHttpMgSerialNumber = _HpHttpMgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 9),
    _HpHttpMgSerialNumber_Type()
)
hpHttpMgSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgSerialNumber.setStatus("current")


class _HpHttpMgAssetNumber_Type(Utf8String):
    """Custom type hpHttpMgAssetNumber based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgAssetNumber_Type.__name__ = "Utf8String"
_HpHttpMgAssetNumber_Object = MibScalar
hpHttpMgAssetNumber = _HpHttpMgAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 10),
    _HpHttpMgAssetNumber_Type()
)
hpHttpMgAssetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgAssetNumber.setStatus("current")


class _HpHttpMgPhone_Type(Utf8String):
    """Custom type hpHttpMgPhone based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgPhone_Type.__name__ = "Utf8String"
_HpHttpMgPhone_Object = MibScalar
hpHttpMgPhone = _HpHttpMgPhone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 11),
    _HpHttpMgPhone_Type()
)
hpHttpMgPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgPhone.setStatus("current")
_HpHttpMgGroups_ObjectIdentity = ObjectIdentity
hpHttpMgGroups = _HpHttpMgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2)
)
_HpHttpMgCompliances_ObjectIdentity = ObjectIdentity
hpHttpMgCompliances = _HpHttpMgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3)
)

# Managed Objects groups

hpHttpMgDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 1)
)
hpHttpMgDefaultGroup.setObjects(
    ("HP-httpManageable-MIB", "hpHttpMgDefaultURL")
)
if mibBuilder.loadTexts:
    hpHttpMgDefaultGroup.setStatus("current")

hpHttpMgBasicNetCitizenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 2)
)
hpHttpMgBasicNetCitizenGroup.setObjects(
      *(("HP-httpManageable-MIB", "hpHttpMgMgmtSrvrURL"),
        ("HP-httpManageable-MIB", "hpHttpMgID"),
        ("HP-httpManageable-MIB", "hpHttpMgHealth"),
        ("HP-httpManageable-MIB", "hpHttpMgManufacturer"),
        ("HP-httpManageable-MIB", "hpHttpMgProduct"),
        ("HP-httpManageable-MIB", "hpHttpMgVersion"))
)
if mibBuilder.loadTexts:
    hpHttpMgBasicNetCitizenGroup.setStatus("current")

hpHttpMgExtendedNetCitizenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 4)
)
hpHttpMgExtendedNetCitizenGroup.setObjects(
      *(("HP-httpManageable-MIB", "hpHttpMgHWVersion"),
        ("HP-httpManageable-MIB", "hpHttpMgROMVersion"),
        ("HP-httpManageable-MIB", "hpHttpMgSerialNumber"),
        ("HP-httpManageable-MIB", "hpHttpMgAssetNumber"),
        ("HP-httpManageable-MIB", "hpHttpMgPhone"))
)
if mibBuilder.loadTexts:
    hpHttpMgExtendedNetCitizenGroup.setStatus("current")


# Notification objects

hpHttpMgHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 1)
)
hpHttpMgHealthTrap.setObjects(
    ("HP-httpManageable-MIB", "hpHttpMgHealth")
)
if mibBuilder.loadTexts:
    hpHttpMgHealthTrap.setStatus(
        "current"
    )

hpHttpMgShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpHttpMgShutdown.setStatus(
        "current"
    )


# Notifications groups

hpHttpMgBasicNetCitizenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 3)
)
hpHttpMgBasicNetCitizenTrapGroup.setObjects(
    ("HP-httpManageable-MIB", "hpHttpMgHealthTrap")
)
if mibBuilder.loadTexts:
    hpHttpMgBasicNetCitizenTrapGroup.setStatus(
        "current"
    )

hpHttpMgExtendedNetCitizenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 5)
)
hpHttpMgExtendedNetCitizenTrapGroup.setObjects(
    ("HP-httpManageable-MIB", "hpHttpMgShutdown")
)
if mibBuilder.loadTexts:
    hpHttpMgExtendedNetCitizenTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpHttpMgMinCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpHttpMgMinCompliance.setStatus(
        "current"
    )

hpHttpMgBasicNetCitizenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpHttpMgBasicNetCitizenCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-httpManageable-MIB",
    **{"Utf8String": Utf8String,
       "hp": hp,
       "nm": nm,
       "hpWebMgmt": hpWebMgmt,
       "hpHttpMgMod": hpHttpMgMod,
       "hpHttpMgTraps": hpHttpMgTraps,
       "hpHttpMgHealthTrap": hpHttpMgHealthTrap,
       "hpHttpMgShutdown": hpHttpMgShutdown,
       "hpHttpMgObjects": hpHttpMgObjects,
       "hpHttpMgDefaults": hpHttpMgDefaults,
       "hpHttpMgDefaultURL": hpHttpMgDefaultURL,
       "hpHttpMgNetCitizen": hpHttpMgNetCitizen,
       "hpHttpMgMgmtSrvrURL": hpHttpMgMgmtSrvrURL,
       "hpHttpMgID": hpHttpMgID,
       "hpHttpMgHealth": hpHttpMgHealth,
       "hpHttpMgManufacturer": hpHttpMgManufacturer,
       "hpHttpMgProduct": hpHttpMgProduct,
       "hpHttpMgVersion": hpHttpMgVersion,
       "hpHttpMgHWVersion": hpHttpMgHWVersion,
       "hpHttpMgROMVersion": hpHttpMgROMVersion,
       "hpHttpMgSerialNumber": hpHttpMgSerialNumber,
       "hpHttpMgAssetNumber": hpHttpMgAssetNumber,
       "hpHttpMgPhone": hpHttpMgPhone,
       "hpHttpMgGroups": hpHttpMgGroups,
       "hpHttpMgDefaultGroup": hpHttpMgDefaultGroup,
       "hpHttpMgBasicNetCitizenGroup": hpHttpMgBasicNetCitizenGroup,
       "hpHttpMgBasicNetCitizenTrapGroup": hpHttpMgBasicNetCitizenTrapGroup,
       "hpHttpMgExtendedNetCitizenGroup": hpHttpMgExtendedNetCitizenGroup,
       "hpHttpMgExtendedNetCitizenTrapGroup": hpHttpMgExtendedNetCitizenTrapGroup,
       "hpHttpMgCompliances": hpHttpMgCompliances,
       "hpHttpMgMinCompliance": hpHttpMgMinCompliance,
       "hpHttpMgBasicNetCitizenCompliance": hpHttpMgBasicNetCitizenCompliance}
)
