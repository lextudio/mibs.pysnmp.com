# SNMP MIB module (SEMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SEMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:19 2024
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
        ("2000-10-16 00:00",
         "2000-10-12 00:00",
         "2000-10-04 00:00",
         "2000-01-12 00:00",
         "1999-03-17 00:00",
         "1998-12-01 00:00",
         "1997-06-26 00:00",
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
_HpHttpMgDeviceSpecificEventCode_Type = Utf8String
_HpHttpMgDeviceSpecificEventCode_Object = MibScalar
hpHttpMgDeviceSpecificEventCode = _HpHttpMgDeviceSpecificEventCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 10),
    _HpHttpMgDeviceSpecificEventCode_Type()
)
hpHttpMgDeviceSpecificEventCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceSpecificEventCode.setStatus("current")
_HpHttpMgDeviceSpecificFRU_Type = Utf8String
_HpHttpMgDeviceSpecificFRU_Object = MibScalar
hpHttpMgDeviceSpecificFRU = _HpHttpMgDeviceSpecificFRU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 11),
    _HpHttpMgDeviceSpecificFRU_Type()
)
hpHttpMgDeviceSpecificFRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceSpecificFRU.setStatus("current")
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
    hpHttpMgMgmtSrvrURL.setStatus("deprecated")
_HpHttpMgID_Type = Utf8String
_HpHttpMgID_Object = MibScalar
hpHttpMgID = _HpHttpMgID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 2),
    _HpHttpMgID_Type()
)
hpHttpMgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgID.setStatus("deprecated")


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
    hpHttpMgHealth.setStatus("deprecated")
_HpHttpMgManufacturer_Type = Utf8String
_HpHttpMgManufacturer_Object = MibScalar
hpHttpMgManufacturer = _HpHttpMgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 2, 4),
    _HpHttpMgManufacturer_Type()
)
hpHttpMgManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgManufacturer.setStatus("deprecated")


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
    hpHttpMgProduct.setStatus("deprecated")


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
    hpHttpMgVersion.setStatus("deprecated")


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
    hpHttpMgHWVersion.setStatus("deprecated")


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
    hpHttpMgROMVersion.setStatus("deprecated")


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
    hpHttpMgSerialNumber.setStatus("deprecated")


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
    hpHttpMgAssetNumber.setStatus("deprecated")


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
    hpHttpMgPhone.setStatus("deprecated")
_HpHttpMgEntityNetInfo_ObjectIdentity = ObjectIdentity
hpHttpMgEntityNetInfo = _HpHttpMgEntityNetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3)
)
_HpHttpMgEntityNetInfoTable_Object = MibTable
hpHttpMgEntityNetInfoTable = _HpHttpMgEntityNetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoTable.setStatus("current")
_HpHttpMgEntityNetInfoEntry_Object = MibTableRow
hpHttpMgEntityNetInfoEntry = _HpHttpMgEntityNetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1)
)
hpHttpMgEntityNetInfoEntry.setIndexNames(
    (0, "SEMI-MIB", "hpHttpMgEntityNetInfoIndex"),
)
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoEntry.setStatus("current")


class _HpHttpMgEntityNetInfoIndex_Type(Integer32):
    """Custom type hpHttpMgEntityNetInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HpHttpMgEntityNetInfoIndex_Type.__name__ = "Integer32"
_HpHttpMgEntityNetInfoIndex_Object = MibTableColumn
hpHttpMgEntityNetInfoIndex = _HpHttpMgEntityNetInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 1),
    _HpHttpMgEntityNetInfoIndex_Type()
)
hpHttpMgEntityNetInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoIndex.setStatus("current")
_HpHttpMgEntityNetInfoSysObjID_Type = Utf8String
_HpHttpMgEntityNetInfoSysObjID_Object = MibTableColumn
hpHttpMgEntityNetInfoSysObjID = _HpHttpMgEntityNetInfoSysObjID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 2),
    _HpHttpMgEntityNetInfoSysObjID_Type()
)
hpHttpMgEntityNetInfoSysObjID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoSysObjID.setStatus("current")


class _HpHttpMgEntityNetInfoRelationshipType_Type(Integer32):
    """Custom type hpHttpMgEntityNetInfoRelationshipType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clusterNode", 5),
          ("containedEntity", 1),
          ("containingEntity", 2),
          ("externallyAttachedEntity", 3),
          ("indirectlyAttachedEntity", 4),
          ("self", 0))
    )


_HpHttpMgEntityNetInfoRelationshipType_Type.__name__ = "Integer32"
_HpHttpMgEntityNetInfoRelationshipType_Object = MibTableColumn
hpHttpMgEntityNetInfoRelationshipType = _HpHttpMgEntityNetInfoRelationshipType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 3),
    _HpHttpMgEntityNetInfoRelationshipType_Type()
)
hpHttpMgEntityNetInfoRelationshipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoRelationshipType.setStatus("current")
_HpHttpMgEntityNetInfoUniqueID_Type = Utf8String
_HpHttpMgEntityNetInfoUniqueID_Object = MibTableColumn
hpHttpMgEntityNetInfoUniqueID = _HpHttpMgEntityNetInfoUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 4),
    _HpHttpMgEntityNetInfoUniqueID_Type()
)
hpHttpMgEntityNetInfoUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoUniqueID.setStatus("current")
_HpHttpMgEntityNetInfoURL_Type = Utf8String
_HpHttpMgEntityNetInfoURL_Object = MibTableColumn
hpHttpMgEntityNetInfoURL = _HpHttpMgEntityNetInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 5),
    _HpHttpMgEntityNetInfoURL_Type()
)
hpHttpMgEntityNetInfoURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoURL.setStatus("current")
_HpHttpMgEntityNetInfoURLLabel_Type = Utf8String
_HpHttpMgEntityNetInfoURLLabel_Object = MibTableColumn
hpHttpMgEntityNetInfoURLLabel = _HpHttpMgEntityNetInfoURLLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 6),
    _HpHttpMgEntityNetInfoURLLabel_Type()
)
hpHttpMgEntityNetInfoURLLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoURLLabel.setStatus("current")
_HpHttpMgEntityNetInfoIPAddress_Type = Utf8String
_HpHttpMgEntityNetInfoIPAddress_Object = MibTableColumn
hpHttpMgEntityNetInfoIPAddress = _HpHttpMgEntityNetInfoIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 3, 1, 1, 7),
    _HpHttpMgEntityNetInfoIPAddress_Type()
)
hpHttpMgEntityNetInfoIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgEntityNetInfoIPAddress.setStatus("current")
_HpHttpMgCluster_ObjectIdentity = ObjectIdentity
hpHttpMgCluster = _HpHttpMgCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 4)
)
_HpHttpMgClusterName_Type = Utf8String
_HpHttpMgClusterName_Object = MibScalar
hpHttpMgClusterName = _HpHttpMgClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 4, 1),
    _HpHttpMgClusterName_Type()
)
hpHttpMgClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgClusterName.setStatus("current")
_HpHttpMgDeviceInfo_ObjectIdentity = ObjectIdentity
hpHttpMgDeviceInfo = _HpHttpMgDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5)
)
_HpHttpMgDeviceTable_Object = MibTable
hpHttpMgDeviceTable = _HpHttpMgDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpHttpMgDeviceTable.setStatus("current")
_HpHttpMgDeviceEntry_Object = MibTableRow
hpHttpMgDeviceEntry = _HpHttpMgDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1)
)
hpHttpMgDeviceEntry.setIndexNames(
    (0, "SEMI-MIB", "hpHttpMgDeviceIndex"),
)
if mibBuilder.loadTexts:
    hpHttpMgDeviceEntry.setStatus("current")


class _HpHttpMgDeviceIndex_Type(Integer32):
    """Custom type hpHttpMgDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HpHttpMgDeviceIndex_Type.__name__ = "Integer32"
_HpHttpMgDeviceIndex_Object = MibTableColumn
hpHttpMgDeviceIndex = _HpHttpMgDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 1),
    _HpHttpMgDeviceIndex_Type()
)
hpHttpMgDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceIndex.setStatus("current")
_HpHttpMgDeviceGlobalUniqueID_Type = Utf8String
_HpHttpMgDeviceGlobalUniqueID_Object = MibTableColumn
hpHttpMgDeviceGlobalUniqueID = _HpHttpMgDeviceGlobalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 2),
    _HpHttpMgDeviceGlobalUniqueID_Type()
)
hpHttpMgDeviceGlobalUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceGlobalUniqueID.setStatus("current")


class _HpHttpMgDeviceHealth_Type(Integer32):
    """Custom type hpHttpMgDeviceHealth based on Integer32"""
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
          ("nonrecoverable", 6),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_HpHttpMgDeviceHealth_Type.__name__ = "Integer32"
_HpHttpMgDeviceHealth_Object = MibTableColumn
hpHttpMgDeviceHealth = _HpHttpMgDeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 3),
    _HpHttpMgDeviceHealth_Type()
)
hpHttpMgDeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceHealth.setStatus("current")
_HpHttpMgDeviceSysObjID_Type = Utf8String
_HpHttpMgDeviceSysObjID_Object = MibTableColumn
hpHttpMgDeviceSysObjID = _HpHttpMgDeviceSysObjID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 4),
    _HpHttpMgDeviceSysObjID_Type()
)
hpHttpMgDeviceSysObjID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceSysObjID.setStatus("current")
_HpHttpMgDeviceManagementURL_Type = Utf8String
_HpHttpMgDeviceManagementURL_Object = MibTableColumn
hpHttpMgDeviceManagementURL = _HpHttpMgDeviceManagementURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 5),
    _HpHttpMgDeviceManagementURL_Type()
)
hpHttpMgDeviceManagementURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceManagementURL.setStatus("current")
_HpHttpMgDeviceManagementURLLabel_Type = Utf8String
_HpHttpMgDeviceManagementURLLabel_Object = MibTableColumn
hpHttpMgDeviceManagementURLLabel = _HpHttpMgDeviceManagementURLLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 6),
    _HpHttpMgDeviceManagementURLLabel_Type()
)
hpHttpMgDeviceManagementURLLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceManagementURLLabel.setStatus("current")
_HpHttpMgDeviceManufacturer_Type = Utf8String
_HpHttpMgDeviceManufacturer_Object = MibTableColumn
hpHttpMgDeviceManufacturer = _HpHttpMgDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 7),
    _HpHttpMgDeviceManufacturer_Type()
)
hpHttpMgDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceManufacturer.setStatus("current")
_HpHttpMgDeviceProductName_Type = Utf8String
_HpHttpMgDeviceProductName_Object = MibTableColumn
hpHttpMgDeviceProductName = _HpHttpMgDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 8),
    _HpHttpMgDeviceProductName_Type()
)
hpHttpMgDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceProductName.setStatus("current")
_HpHttpMgDeviceProductCaption_Type = Utf8String
_HpHttpMgDeviceProductCaption_Object = MibTableColumn
hpHttpMgDeviceProductCaption = _HpHttpMgDeviceProductCaption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 9),
    _HpHttpMgDeviceProductCaption_Type()
)
hpHttpMgDeviceProductCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceProductCaption.setStatus("current")
_HpHttpMgDeviceSerialNumber_Type = Utf8String
_HpHttpMgDeviceSerialNumber_Object = MibTableColumn
hpHttpMgDeviceSerialNumber = _HpHttpMgDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 10),
    _HpHttpMgDeviceSerialNumber_Type()
)
hpHttpMgDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceSerialNumber.setStatus("current")


class _HpHttpMgDeviceVersion_Type(Utf8String):
    """Custom type hpHttpMgDeviceVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceVersion_Type.__name__ = "Utf8String"
_HpHttpMgDeviceVersion_Object = MibTableColumn
hpHttpMgDeviceVersion = _HpHttpMgDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 11),
    _HpHttpMgDeviceVersion_Type()
)
hpHttpMgDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceVersion.setStatus("current")


class _HpHttpMgDeviceHWVersion_Type(Utf8String):
    """Custom type hpHttpMgDeviceHWVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceHWVersion_Type.__name__ = "Utf8String"
_HpHttpMgDeviceHWVersion_Object = MibTableColumn
hpHttpMgDeviceHWVersion = _HpHttpMgDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 12),
    _HpHttpMgDeviceHWVersion_Type()
)
hpHttpMgDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceHWVersion.setStatus("current")


class _HpHttpMgDeviceROMVersion_Type(Utf8String):
    """Custom type hpHttpMgDeviceROMVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceROMVersion_Type.__name__ = "Utf8String"
_HpHttpMgDeviceROMVersion_Object = MibTableColumn
hpHttpMgDeviceROMVersion = _HpHttpMgDeviceROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 13),
    _HpHttpMgDeviceROMVersion_Type()
)
hpHttpMgDeviceROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceROMVersion.setStatus("current")


class _HpHttpMgDeviceAssetNumber_Type(Utf8String):
    """Custom type hpHttpMgDeviceAssetNumber based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceAssetNumber_Type.__name__ = "Utf8String"
_HpHttpMgDeviceAssetNumber_Object = MibTableColumn
hpHttpMgDeviceAssetNumber = _HpHttpMgDeviceAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 14),
    _HpHttpMgDeviceAssetNumber_Type()
)
hpHttpMgDeviceAssetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceAssetNumber.setStatus("current")


class _HpHttpMgDeviceContactPerson_Type(Utf8String):
    """Custom type hpHttpMgDeviceContactPerson based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceContactPerson_Type.__name__ = "Utf8String"
_HpHttpMgDeviceContactPerson_Object = MibTableColumn
hpHttpMgDeviceContactPerson = _HpHttpMgDeviceContactPerson_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 15),
    _HpHttpMgDeviceContactPerson_Type()
)
hpHttpMgDeviceContactPerson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceContactPerson.setStatus("current")


class _HpHttpMgDeviceContactPhone_Type(Utf8String):
    """Custom type hpHttpMgDeviceContactPhone based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceContactPhone_Type.__name__ = "Utf8String"
_HpHttpMgDeviceContactPhone_Object = MibTableColumn
hpHttpMgDeviceContactPhone = _HpHttpMgDeviceContactPhone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 16),
    _HpHttpMgDeviceContactPhone_Type()
)
hpHttpMgDeviceContactPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceContactPhone.setStatus("current")
_HpHttpMgDeviceContactEmail_Type = Utf8String
_HpHttpMgDeviceContactEmail_Object = MibTableColumn
hpHttpMgDeviceContactEmail = _HpHttpMgDeviceContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 17),
    _HpHttpMgDeviceContactEmail_Type()
)
hpHttpMgDeviceContactEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceContactEmail.setStatus("current")


class _HpHttpMgDeviceContactPagerNumber_Type(Utf8String):
    """Custom type hpHttpMgDeviceContactPagerNumber based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpHttpMgDeviceContactPagerNumber_Type.__name__ = "Utf8String"
_HpHttpMgDeviceContactPagerNumber_Object = MibTableColumn
hpHttpMgDeviceContactPagerNumber = _HpHttpMgDeviceContactPagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 18),
    _HpHttpMgDeviceContactPagerNumber_Type()
)
hpHttpMgDeviceContactPagerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceContactPagerNumber.setStatus("current")
_HpHttpMgDeviceLocation_Type = Utf8String
_HpHttpMgDeviceLocation_Object = MibTableColumn
hpHttpMgDeviceLocation = _HpHttpMgDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 19),
    _HpHttpMgDeviceLocation_Type()
)
hpHttpMgDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceLocation.setStatus("current")
_HpHttpMgDeviceRackId_Type = Utf8String
_HpHttpMgDeviceRackId_Object = MibTableColumn
hpHttpMgDeviceRackId = _HpHttpMgDeviceRackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 20),
    _HpHttpMgDeviceRackId_Type()
)
hpHttpMgDeviceRackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceRackId.setStatus("current")
_HpHttpMgDeviceRackPosition_Type = Utf8String
_HpHttpMgDeviceRackPosition_Object = MibTableColumn
hpHttpMgDeviceRackPosition = _HpHttpMgDeviceRackPosition_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 21),
    _HpHttpMgDeviceRackPosition_Type()
)
hpHttpMgDeviceRackPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpHttpMgDeviceRackPosition.setStatus("current")


class _HpHttpMgDeviceRelationshipType_Type(Integer32):
    """Custom type hpHttpMgDeviceRelationshipType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("other", 2))
    )


_HpHttpMgDeviceRelationshipType_Type.__name__ = "Integer32"
_HpHttpMgDeviceRelationshipType_Object = MibTableColumn
hpHttpMgDeviceRelationshipType = _HpHttpMgDeviceRelationshipType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 1, 5, 1, 1, 22),
    _HpHttpMgDeviceRelationshipType_Type()
)
hpHttpMgDeviceRelationshipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpHttpMgDeviceRelationshipType.setStatus("current")
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
    ("SEMI-MIB", "hpHttpMgDefaultURL")
)
if mibBuilder.loadTexts:
    hpHttpMgDefaultGroup.setStatus("current")

hpHttpMgBasicNetCitizenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 2)
)
hpHttpMgBasicNetCitizenGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgMgmtSrvrURL"),
        ("SEMI-MIB", "hpHttpMgID"),
        ("SEMI-MIB", "hpHttpMgHealth"),
        ("SEMI-MIB", "hpHttpMgManufacturer"),
        ("SEMI-MIB", "hpHttpMgProduct"),
        ("SEMI-MIB", "hpHttpMgVersion"))
)
if mibBuilder.loadTexts:
    hpHttpMgBasicNetCitizenGroup.setStatus("deprecated")

hpHttpMgExtendedNetCitizenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 4)
)
hpHttpMgExtendedNetCitizenGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgHWVersion"),
        ("SEMI-MIB", "hpHttpMgROMVersion"),
        ("SEMI-MIB", "hpHttpMgSerialNumber"),
        ("SEMI-MIB", "hpHttpMgAssetNumber"),
        ("SEMI-MIB", "hpHttpMgPhone"))
)
if mibBuilder.loadTexts:
    hpHttpMgExtendedNetCitizenGroup.setStatus("deprecated")

hpHttpMgEntityRelationshipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 6)
)
hpHttpMgEntityRelationshipGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgEntityNetInfoIndex"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoSysObjID"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoRelationshipType"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoUniqueID"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoURL"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoURLLabel"),
        ("SEMI-MIB", "hpHttpMgEntityNetInfoIPAddress"))
)
if mibBuilder.loadTexts:
    hpHttpMgEntityRelationshipGroup.setStatus("current")

hpHttpMgClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 7)
)
hpHttpMgClusterGroup.setObjects(
    ("SEMI-MIB", "hpHttpMgClusterName")
)
if mibBuilder.loadTexts:
    hpHttpMgClusterGroup.setStatus("current")

hpHttpMgEnhancedNetCitizenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 8)
)
hpHttpMgEnhancedNetCitizenGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceHealth"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceManufacturer"),
        ("SEMI-MIB", "hpHttpMgDeviceProductName"),
        ("SEMI-MIB", "hpHttpMgDeviceProductCaption"),
        ("SEMI-MIB", "hpHttpMgDeviceSerialNumber"),
        ("SEMI-MIB", "hpHttpMgDeviceVersion"),
        ("SEMI-MIB", "hpHttpMgDeviceHWVersion"),
        ("SEMI-MIB", "hpHttpMgDeviceROMVersion"),
        ("SEMI-MIB", "hpHttpMgDeviceAssetNumber"),
        ("SEMI-MIB", "hpHttpMgDeviceContactPerson"),
        ("SEMI-MIB", "hpHttpMgDeviceContactPhone"),
        ("SEMI-MIB", "hpHttpMgDeviceContactEmail"),
        ("SEMI-MIB", "hpHttpMgDeviceContactPagerNumber"),
        ("SEMI-MIB", "hpHttpMgDeviceLocation"),
        ("SEMI-MIB", "hpHttpMgDeviceRackId"),
        ("SEMI-MIB", "hpHttpMgDeviceRackPosition"),
        ("SEMI-MIB", "hpHttpMgDeviceRelationshipType"))
)
if mibBuilder.loadTexts:
    hpHttpMgEnhancedNetCitizenGroup.setStatus("current")

hpHttpMgDeviceSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 10)
)
hpHttpMgDeviceSpecificGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgDeviceSpecificGroup.setStatus("current")


# Notification objects

hpHttpMgHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 1)
)
hpHttpMgHealthTrap.setObjects(
    ("SEMI-MIB", "hpHttpMgHealth")
)
if mibBuilder.loadTexts:
    hpHttpMgHealthTrap.setStatus(
        "deprecated"
    )

hpHttpMgShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpHttpMgShutdown.setStatus(
        "deprecated"
    )

hpHttpMgUnknownHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 3)
)
hpHttpMgUnknownHealthTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgUnknownHealthTrap.setStatus(
        "current"
    )

hpHttpMgOKHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 4)
)
hpHttpMgOKHealthTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgOKHealthTrap.setStatus(
        "current"
    )

hpHttpMgWarningHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 5)
)
hpHttpMgWarningHealthTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgWarningHealthTrap.setStatus(
        "current"
    )

hpHttpMgCriticalHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 6)
)
hpHttpMgCriticalHealthTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgCriticalHealthTrap.setStatus(
        "current"
    )

hpHttpMgNonRecoverableHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 7)
)
hpHttpMgNonRecoverableHealthTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificEventCode"),
        ("SEMI-MIB", "hpHttpMgDeviceSpecificFRU"))
)
if mibBuilder.loadTexts:
    hpHttpMgNonRecoverableHealthTrap.setStatus(
        "current"
    )

hpHttpMgDeviceAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 8)
)
hpHttpMgDeviceAddedTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURL"),
        ("SEMI-MIB", "hpHttpMgDeviceManagementURLLabel"))
)
if mibBuilder.loadTexts:
    hpHttpMgDeviceAddedTrap.setStatus(
        "current"
    )

hpHttpMgDeviceRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 0, 9)
)
hpHttpMgDeviceRemovedTrap.setObjects(
      *(("SEMI-MIB", "hpHttpMgDeviceIndex"),
        ("SEMI-MIB", "hpHttpMgDeviceSysObjID"),
        ("SEMI-MIB", "hpHttpMgDeviceGlobalUniqueID"))
)
if mibBuilder.loadTexts:
    hpHttpMgDeviceRemovedTrap.setStatus(
        "current"
    )


# Notifications groups

hpHttpMgBasicNetCitizenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 3)
)
hpHttpMgBasicNetCitizenTrapGroup.setObjects(
    ("SEMI-MIB", "hpHttpMgHealthTrap")
)
if mibBuilder.loadTexts:
    hpHttpMgBasicNetCitizenTrapGroup.setStatus(
        "deprecated"
    )

hpHttpMgExtendedNetCitizenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 5)
)
hpHttpMgExtendedNetCitizenTrapGroup.setObjects(
    ("SEMI-MIB", "hpHttpMgShutdown")
)
if mibBuilder.loadTexts:
    hpHttpMgExtendedNetCitizenTrapGroup.setStatus(
        "current"
    )

hpHttpMgEnhancedNetCitizenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 2, 9)
)
hpHttpMgEnhancedNetCitizenTrapGroup.setObjects(
      *(("SEMI-MIB", "hpHttpMgUnknownHealthTrap"),
        ("SEMI-MIB", "hpHttpMgOKHealthTrap"),
        ("SEMI-MIB", "hpHttpMgWarningHealthTrap"),
        ("SEMI-MIB", "hpHttpMgCriticalHealthTrap"),
        ("SEMI-MIB", "hpHttpMgNonRecoverableHealthTrap"),
        ("SEMI-MIB", "hpHttpMgDeviceAddedTrap"),
        ("SEMI-MIB", "hpHttpMgDeviceRemovedTrap"))
)
if mibBuilder.loadTexts:
    hpHttpMgEnhancedNetCitizenTrapGroup.setStatus(
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
        "deprecated"
    )

hpHttpMgEnhancedNetCitizenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpHttpMgEnhancedNetCitizenCompliance.setStatus(
        "current"
    )

hpHttpMgExtentedNetCitizenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpHttpMgExtentedNetCitizenCompliance.setStatus(
        "current"
    )

hpHttpMgExtentedNetCitizenCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hpHttpMgExtentedNetCitizenCompliance1.setStatus(
        "deprecated"
    )

hpHttpMgExtentedNetCitizenCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 36, 1, 3, 6)
)
if mibBuilder.loadTexts:
    hpHttpMgExtentedNetCitizenCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEMI-MIB",
    **{"Utf8String": Utf8String,
       "hp": hp,
       "nm": nm,
       "hpWebMgmt": hpWebMgmt,
       "hpHttpMgMod": hpHttpMgMod,
       "hpHttpMgTraps": hpHttpMgTraps,
       "hpHttpMgHealthTrap": hpHttpMgHealthTrap,
       "hpHttpMgShutdown": hpHttpMgShutdown,
       "hpHttpMgUnknownHealthTrap": hpHttpMgUnknownHealthTrap,
       "hpHttpMgOKHealthTrap": hpHttpMgOKHealthTrap,
       "hpHttpMgWarningHealthTrap": hpHttpMgWarningHealthTrap,
       "hpHttpMgCriticalHealthTrap": hpHttpMgCriticalHealthTrap,
       "hpHttpMgNonRecoverableHealthTrap": hpHttpMgNonRecoverableHealthTrap,
       "hpHttpMgDeviceAddedTrap": hpHttpMgDeviceAddedTrap,
       "hpHttpMgDeviceRemovedTrap": hpHttpMgDeviceRemovedTrap,
       "hpHttpMgDeviceSpecificEventCode": hpHttpMgDeviceSpecificEventCode,
       "hpHttpMgDeviceSpecificFRU": hpHttpMgDeviceSpecificFRU,
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
       "hpHttpMgEntityNetInfo": hpHttpMgEntityNetInfo,
       "hpHttpMgEntityNetInfoTable": hpHttpMgEntityNetInfoTable,
       "hpHttpMgEntityNetInfoEntry": hpHttpMgEntityNetInfoEntry,
       "hpHttpMgEntityNetInfoIndex": hpHttpMgEntityNetInfoIndex,
       "hpHttpMgEntityNetInfoSysObjID": hpHttpMgEntityNetInfoSysObjID,
       "hpHttpMgEntityNetInfoRelationshipType": hpHttpMgEntityNetInfoRelationshipType,
       "hpHttpMgEntityNetInfoUniqueID": hpHttpMgEntityNetInfoUniqueID,
       "hpHttpMgEntityNetInfoURL": hpHttpMgEntityNetInfoURL,
       "hpHttpMgEntityNetInfoURLLabel": hpHttpMgEntityNetInfoURLLabel,
       "hpHttpMgEntityNetInfoIPAddress": hpHttpMgEntityNetInfoIPAddress,
       "hpHttpMgCluster": hpHttpMgCluster,
       "hpHttpMgClusterName": hpHttpMgClusterName,
       "hpHttpMgDeviceInfo": hpHttpMgDeviceInfo,
       "hpHttpMgDeviceTable": hpHttpMgDeviceTable,
       "hpHttpMgDeviceEntry": hpHttpMgDeviceEntry,
       "hpHttpMgDeviceIndex": hpHttpMgDeviceIndex,
       "hpHttpMgDeviceGlobalUniqueID": hpHttpMgDeviceGlobalUniqueID,
       "hpHttpMgDeviceHealth": hpHttpMgDeviceHealth,
       "hpHttpMgDeviceSysObjID": hpHttpMgDeviceSysObjID,
       "hpHttpMgDeviceManagementURL": hpHttpMgDeviceManagementURL,
       "hpHttpMgDeviceManagementURLLabel": hpHttpMgDeviceManagementURLLabel,
       "hpHttpMgDeviceManufacturer": hpHttpMgDeviceManufacturer,
       "hpHttpMgDeviceProductName": hpHttpMgDeviceProductName,
       "hpHttpMgDeviceProductCaption": hpHttpMgDeviceProductCaption,
       "hpHttpMgDeviceSerialNumber": hpHttpMgDeviceSerialNumber,
       "hpHttpMgDeviceVersion": hpHttpMgDeviceVersion,
       "hpHttpMgDeviceHWVersion": hpHttpMgDeviceHWVersion,
       "hpHttpMgDeviceROMVersion": hpHttpMgDeviceROMVersion,
       "hpHttpMgDeviceAssetNumber": hpHttpMgDeviceAssetNumber,
       "hpHttpMgDeviceContactPerson": hpHttpMgDeviceContactPerson,
       "hpHttpMgDeviceContactPhone": hpHttpMgDeviceContactPhone,
       "hpHttpMgDeviceContactEmail": hpHttpMgDeviceContactEmail,
       "hpHttpMgDeviceContactPagerNumber": hpHttpMgDeviceContactPagerNumber,
       "hpHttpMgDeviceLocation": hpHttpMgDeviceLocation,
       "hpHttpMgDeviceRackId": hpHttpMgDeviceRackId,
       "hpHttpMgDeviceRackPosition": hpHttpMgDeviceRackPosition,
       "hpHttpMgDeviceRelationshipType": hpHttpMgDeviceRelationshipType,
       "hpHttpMgGroups": hpHttpMgGroups,
       "hpHttpMgDefaultGroup": hpHttpMgDefaultGroup,
       "hpHttpMgBasicNetCitizenGroup": hpHttpMgBasicNetCitizenGroup,
       "hpHttpMgBasicNetCitizenTrapGroup": hpHttpMgBasicNetCitizenTrapGroup,
       "hpHttpMgExtendedNetCitizenGroup": hpHttpMgExtendedNetCitizenGroup,
       "hpHttpMgExtendedNetCitizenTrapGroup": hpHttpMgExtendedNetCitizenTrapGroup,
       "hpHttpMgEntityRelationshipGroup": hpHttpMgEntityRelationshipGroup,
       "hpHttpMgClusterGroup": hpHttpMgClusterGroup,
       "hpHttpMgEnhancedNetCitizenGroup": hpHttpMgEnhancedNetCitizenGroup,
       "hpHttpMgEnhancedNetCitizenTrapGroup": hpHttpMgEnhancedNetCitizenTrapGroup,
       "hpHttpMgDeviceSpecificGroup": hpHttpMgDeviceSpecificGroup,
       "hpHttpMgCompliances": hpHttpMgCompliances,
       "hpHttpMgMinCompliance": hpHttpMgMinCompliance,
       "hpHttpMgBasicNetCitizenCompliance": hpHttpMgBasicNetCitizenCompliance,
       "hpHttpMgEnhancedNetCitizenCompliance": hpHttpMgEnhancedNetCitizenCompliance,
       "hpHttpMgExtentedNetCitizenCompliance": hpHttpMgExtentedNetCitizenCompliance,
       "hpHttpMgExtentedNetCitizenCompliance1": hpHttpMgExtentedNetCitizenCompliance1,
       "hpHttpMgExtentedNetCitizenCompliance2": hpHttpMgExtentedNetCitizenCompliance2}
)
