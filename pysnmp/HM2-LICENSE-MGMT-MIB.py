# SNMP MIB module (HM2-LICENSE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-LICENSE-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:03 2024
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

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hm2LicenseMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3)
)
hm2LicenseMgmtMib.setRevisions(
        ("2012-08-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmLmSwLvlCap(Bits, TextualConvention):
    status = "current"


class HmLmLicenseLvlCap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hm2LicenseMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2LicenseMgmtMibNotifications = _Hm2LicenseMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 0)
)
_Hm2LicenseMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2LicenseMgmtMibObjects = _Hm2LicenseMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1)
)
_Hm2LMLicenseKeyGroup_ObjectIdentity = ObjectIdentity
hm2LMLicenseKeyGroup = _Hm2LMLicenseKeyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 1)
)


class _Hm2LMLicenseKeyUdi_Type(SnmpAdminString):
    """Custom type hm2LMLicenseKeyUdi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LMLicenseKeyUdi_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseKeyUdi_Object = MibScalar
hm2LMLicenseKeyUdi = _Hm2LMLicenseKeyUdi_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 1, 1),
    _Hm2LMLicenseKeyUdi_Type()
)
hm2LMLicenseKeyUdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseKeyUdi.setStatus("current")


class _Hm2LMLicenseKeyInstall_Type(SnmpAdminString):
    """Custom type hm2LMLicenseKeyInstall based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LMLicenseKeyInstall_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseKeyInstall_Object = MibScalar
hm2LMLicenseKeyInstall = _Hm2LMLicenseKeyInstall_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 1, 2),
    _Hm2LMLicenseKeyInstall_Type()
)
hm2LMLicenseKeyInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LMLicenseKeyInstall.setStatus("current")


class _Hm2LMLicenseKeyDelete_Type(SnmpAdminString):
    """Custom type hm2LMLicenseKeyDelete based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LMLicenseKeyDelete_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseKeyDelete_Object = MibScalar
hm2LMLicenseKeyDelete = _Hm2LMLicenseKeyDelete_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 1, 3),
    _Hm2LMLicenseKeyDelete_Type()
)
hm2LMLicenseKeyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LMLicenseKeyDelete.setStatus("current")
_Hm2LMLicenseGroup_ObjectIdentity = ObjectIdentity
hm2LMLicenseGroup = _Hm2LMLicenseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2)
)
_Hm2LMLicenseTable_Object = MibTable
hm2LMLicenseTable = _Hm2LMLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2LMLicenseTable.setStatus("current")
_Hm2LMLicenseEntry_Object = MibTableRow
hm2LMLicenseEntry = _Hm2LMLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1)
)
hm2LMLicenseEntry.setIndexNames(
    (0, "HM2-LICENSE-MGMT-MIB", "hm2LMLicenseId"),
)
if mibBuilder.loadTexts:
    hm2LMLicenseEntry.setStatus("current")
_Hm2LMLicenseId_Type = Integer32
_Hm2LMLicenseId_Object = MibTableColumn
hm2LMLicenseId = _Hm2LMLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 1),
    _Hm2LMLicenseId_Type()
)
hm2LMLicenseId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LMLicenseId.setStatus("current")


class _Hm2LMLicenseDescription_Type(SnmpAdminString):
    """Custom type hm2LMLicenseDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hm2LMLicenseDescription_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseDescription_Object = MibTableColumn
hm2LMLicenseDescription = _Hm2LMLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 2),
    _Hm2LMLicenseDescription_Type()
)
hm2LMLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseDescription.setStatus("current")


class _Hm2LMLicenseVersion_Type(SnmpAdminString):
    """Custom type hm2LMLicenseVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hm2LMLicenseVersion_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseVersion_Object = MibTableColumn
hm2LMLicenseVersion = _Hm2LMLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 3),
    _Hm2LMLicenseVersion_Type()
)
hm2LMLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseVersion.setStatus("current")


class _Hm2LMLicenseKey_Type(SnmpAdminString):
    """Custom type hm2LMLicenseKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LMLicenseKey_Type.__name__ = "SnmpAdminString"
_Hm2LMLicenseKey_Object = MibTableColumn
hm2LMLicenseKey = _Hm2LMLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 4),
    _Hm2LMLicenseKey_Type()
)
hm2LMLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseKey.setStatus("current")


class _Hm2LMLicenseModel_Type(Integer32):
    """Custom type hm2LMLicenseModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("permanent", 2))
    )


_Hm2LMLicenseModel_Type.__name__ = "Integer32"
_Hm2LMLicenseModel_Object = MibTableColumn
hm2LMLicenseModel = _Hm2LMLicenseModel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 5),
    _Hm2LMLicenseModel_Type()
)
hm2LMLicenseModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseModel.setStatus("current")
_Hm2LMLicenseExpiryPeriod_Type = Integer32
_Hm2LMLicenseExpiryPeriod_Object = MibTableColumn
hm2LMLicenseExpiryPeriod = _Hm2LMLicenseExpiryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 6),
    _Hm2LMLicenseExpiryPeriod_Type()
)
hm2LMLicenseExpiryPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseExpiryPeriod.setStatus("current")


class _Hm2LMLicenseOperStatus_Type(Integer32):
    """Custom type hm2LMLicenseOperStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 4),
          ("expired", 3),
          ("inactive", 2),
          ("no-license", 5))
    )


_Hm2LMLicenseOperStatus_Type.__name__ = "Integer32"
_Hm2LMLicenseOperStatus_Object = MibTableColumn
hm2LMLicenseOperStatus = _Hm2LMLicenseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 9),
    _Hm2LMLicenseOperStatus_Type()
)
hm2LMLicenseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseOperStatus.setStatus("current")


class _Hm2LMLicenseAdminStatus_Type(Integer32):
    """Custom type hm2LMLicenseAdminStatus based on Integer32"""
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


_Hm2LMLicenseAdminStatus_Type.__name__ = "Integer32"
_Hm2LMLicenseAdminStatus_Object = MibTableColumn
hm2LMLicenseAdminStatus = _Hm2LMLicenseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 10),
    _Hm2LMLicenseAdminStatus_Type()
)
hm2LMLicenseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LMLicenseAdminStatus.setStatus("current")
_Hm2LMLicenseSwLvlCap_Type = HmLmSwLvlCap
_Hm2LMLicenseSwLvlCap_Object = MibTableColumn
hm2LMLicenseSwLvlCap = _Hm2LMLicenseSwLvlCap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 2, 1, 1, 11),
    _Hm2LMLicenseSwLvlCap_Type()
)
hm2LMLicenseSwLvlCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMLicenseSwLvlCap.setStatus("current")
_Hm2LMFeatureGroup_ObjectIdentity = ObjectIdentity
hm2LMFeatureGroup = _Hm2LMFeatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3)
)
_Hm2LMFeatureTable_Object = MibTable
hm2LMFeatureTable = _Hm2LMFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2LMFeatureTable.setStatus("current")
_Hm2LMFeatureEntry_Object = MibTableRow
hm2LMFeatureEntry = _Hm2LMFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1)
)
hm2LMFeatureEntry.setIndexNames(
    (1, "HM2-LICENSE-MGMT-MIB", "hm2LMFeatureId"),
)
if mibBuilder.loadTexts:
    hm2LMFeatureEntry.setStatus("current")
_Hm2LMFeatureId_Type = ObjectIdentifier
_Hm2LMFeatureId_Object = MibTableColumn
hm2LMFeatureId = _Hm2LMFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 1),
    _Hm2LMFeatureId_Type()
)
hm2LMFeatureId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LMFeatureId.setStatus("current")
_Hm2LMFeatureDescription_Type = SnmpAdminString
_Hm2LMFeatureDescription_Object = MibTableColumn
hm2LMFeatureDescription = _Hm2LMFeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 2),
    _Hm2LMFeatureDescription_Type()
)
hm2LMFeatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureDescription.setStatus("current")
_Hm2LMFeatureBinaryID_Type = Unsigned32
_Hm2LMFeatureBinaryID_Object = MibTableColumn
hm2LMFeatureBinaryID = _Hm2LMFeatureBinaryID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 3),
    _Hm2LMFeatureBinaryID_Type()
)
hm2LMFeatureBinaryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureBinaryID.setStatus("current")
_Hm2LMFeatureCount_Type = Unsigned32
_Hm2LMFeatureCount_Object = MibTableColumn
hm2LMFeatureCount = _Hm2LMFeatureCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 4),
    _Hm2LMFeatureCount_Type()
)
hm2LMFeatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureCount.setStatus("current")
_Hm2LMFeatureLicenseId_Type = Integer32
_Hm2LMFeatureLicenseId_Object = MibTableColumn
hm2LMFeatureLicenseId = _Hm2LMFeatureLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 5),
    _Hm2LMFeatureLicenseId_Type()
)
hm2LMFeatureLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureLicenseId.setStatus("current")


class _Hm2LMFeatureStatus_Type(Integer32):
    """Custom type hm2LMFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 4),
          ("expired", 3),
          ("inactive", 2))
    )


_Hm2LMFeatureStatus_Type.__name__ = "Integer32"
_Hm2LMFeatureStatus_Object = MibTableColumn
hm2LMFeatureStatus = _Hm2LMFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 9),
    _Hm2LMFeatureStatus_Type()
)
hm2LMFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureStatus.setStatus("current")
_Hm2LMFeatureSwLvlCap_Type = HmLmSwLvlCap
_Hm2LMFeatureSwLvlCap_Object = MibTableColumn
hm2LMFeatureSwLvlCap = _Hm2LMFeatureSwLvlCap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 10),
    _Hm2LMFeatureSwLvlCap_Type()
)
hm2LMFeatureSwLvlCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureSwLvlCap.setStatus("current")
_Hm2LMFeatureSwLicCap_Type = HmLmLicenseLvlCap
_Hm2LMFeatureSwLicCap_Object = MibTableColumn
hm2LMFeatureSwLicCap = _Hm2LMFeatureSwLicCap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 3, 1, 1, 11),
    _Hm2LMFeatureSwLicCap_Type()
)
hm2LMFeatureSwLicCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMFeatureSwLicCap.setStatus("current")
_Hm2LMSwLvlGroup_ObjectIdentity = ObjectIdentity
hm2LMSwLvlGroup = _Hm2LMSwLvlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 4)
)
_Hm2LMSwLvlDescription_Type = SnmpAdminString
_Hm2LMSwLvlDescription_Object = MibScalar
hm2LMSwLvlDescription = _Hm2LMSwLvlDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 4, 1),
    _Hm2LMSwLvlDescription_Type()
)
hm2LMSwLvlDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMSwLvlDescription.setStatus("current")
_Hm2LMSwLvlCap_Type = HmLmSwLvlCap
_Hm2LMSwLvlCap_Object = MibScalar
hm2LMSwLvlCap = _Hm2LMSwLvlCap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 4, 2),
    _Hm2LMSwLvlCap_Type()
)
hm2LMSwLvlCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMSwLvlCap.setStatus("current")


class _Hm2LMSwLvlAdminStatus_Type(HmLmSwLvlCap):
    """Custom type hm2LMSwLvlAdminStatus based on HmLmSwLvlCap"""
    defaultBinValue = "1"


_Hm2LMSwLvlAdminStatus_Object = MibScalar
hm2LMSwLvlAdminStatus = _Hm2LMSwLvlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 4, 3),
    _Hm2LMSwLvlAdminStatus_Type()
)
hm2LMSwLvlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LMSwLvlAdminStatus.setStatus("current")
_Hm2LMSwLvlOperStatus_Type = HmLmSwLvlCap
_Hm2LMSwLvlOperStatus_Object = MibScalar
hm2LMSwLvlOperStatus = _Hm2LMSwLvlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 1, 4, 4),
    _Hm2LMSwLvlOperStatus_Type()
)
hm2LMSwLvlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LMSwLvlOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hm2LMLicenseChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 0, 1)
)
hm2LMLicenseChangeTrap.setObjects(
      *(("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseId"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseDescription"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseVersion"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseKey"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseModel"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseExpiryPeriod"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseOperStatus"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMLicenseAdminStatus"))
)
if mibBuilder.loadTexts:
    hm2LMLicenseChangeTrap.setStatus(
        "current"
    )

hm2LMFeatureChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 3, 0, 2)
)
hm2LMFeatureChangeTrap.setObjects(
      *(("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureId"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureDescription"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureBinaryID"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureCount"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureLicenseId"),
        ("HM2-LICENSE-MGMT-MIB", "hm2LMFeatureStatus"))
)
if mibBuilder.loadTexts:
    hm2LMFeatureChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-LICENSE-MGMT-MIB",
    **{"HmLmSwLvlCap": HmLmSwLvlCap,
       "HmLmLicenseLvlCap": HmLmLicenseLvlCap,
       "hm2LicenseMgmtMib": hm2LicenseMgmtMib,
       "hm2LicenseMgmtMibNotifications": hm2LicenseMgmtMibNotifications,
       "hm2LMLicenseChangeTrap": hm2LMLicenseChangeTrap,
       "hm2LMFeatureChangeTrap": hm2LMFeatureChangeTrap,
       "hm2LicenseMgmtMibObjects": hm2LicenseMgmtMibObjects,
       "hm2LMLicenseKeyGroup": hm2LMLicenseKeyGroup,
       "hm2LMLicenseKeyUdi": hm2LMLicenseKeyUdi,
       "hm2LMLicenseKeyInstall": hm2LMLicenseKeyInstall,
       "hm2LMLicenseKeyDelete": hm2LMLicenseKeyDelete,
       "hm2LMLicenseGroup": hm2LMLicenseGroup,
       "hm2LMLicenseTable": hm2LMLicenseTable,
       "hm2LMLicenseEntry": hm2LMLicenseEntry,
       "hm2LMLicenseId": hm2LMLicenseId,
       "hm2LMLicenseDescription": hm2LMLicenseDescription,
       "hm2LMLicenseVersion": hm2LMLicenseVersion,
       "hm2LMLicenseKey": hm2LMLicenseKey,
       "hm2LMLicenseModel": hm2LMLicenseModel,
       "hm2LMLicenseExpiryPeriod": hm2LMLicenseExpiryPeriod,
       "hm2LMLicenseOperStatus": hm2LMLicenseOperStatus,
       "hm2LMLicenseAdminStatus": hm2LMLicenseAdminStatus,
       "hm2LMLicenseSwLvlCap": hm2LMLicenseSwLvlCap,
       "hm2LMFeatureGroup": hm2LMFeatureGroup,
       "hm2LMFeatureTable": hm2LMFeatureTable,
       "hm2LMFeatureEntry": hm2LMFeatureEntry,
       "hm2LMFeatureId": hm2LMFeatureId,
       "hm2LMFeatureDescription": hm2LMFeatureDescription,
       "hm2LMFeatureBinaryID": hm2LMFeatureBinaryID,
       "hm2LMFeatureCount": hm2LMFeatureCount,
       "hm2LMFeatureLicenseId": hm2LMFeatureLicenseId,
       "hm2LMFeatureStatus": hm2LMFeatureStatus,
       "hm2LMFeatureSwLvlCap": hm2LMFeatureSwLvlCap,
       "hm2LMFeatureSwLicCap": hm2LMFeatureSwLicCap,
       "hm2LMSwLvlGroup": hm2LMSwLvlGroup,
       "hm2LMSwLvlDescription": hm2LMSwLvlDescription,
       "hm2LMSwLvlCap": hm2LMSwLvlCap,
       "hm2LMSwLvlAdminStatus": hm2LMSwLvlAdminStatus,
       "hm2LMSwLvlOperStatus": hm2LMSwLvlOperStatus}
)
