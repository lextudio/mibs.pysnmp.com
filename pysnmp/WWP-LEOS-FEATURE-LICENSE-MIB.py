# SNMP MIB module (WWP-LEOS-FEATURE-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-FEATURE-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:51 2024
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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosFeatureLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29)
)
wwpLeosFeatureLicenseMIB.setRevisions(
        ("2010-01-28 00:00",
         "2005-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosFeatureLicenseMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBObjects = _WwpLeosFeatureLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1)
)
_WwpLeosPremiumFeatureLicense_ObjectIdentity = ObjectIdentity
wwpLeosPremiumFeatureLicense = _WwpLeosPremiumFeatureLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1)
)
_WwpLeosPremiumFeatureStatusTable_Object = MibTable
wwpLeosPremiumFeatureStatusTable = _WwpLeosPremiumFeatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureStatusTable.setStatus("current")
_WwpLeosPremiumFeatureStatusEntry_Object = MibTableRow
wwpLeosPremiumFeatureStatusEntry = _WwpLeosPremiumFeatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1)
)
wwpLeosPremiumFeatureStatusEntry.setIndexNames(
    (0, "WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureId"),
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureStatusEntry.setStatus("current")


class _WwpLeosPremiumFeatureId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("advanced10G", 8),
          ("advancedEthernet", 5),
          ("advancedOam", 6),
          ("advancedSync", 11),
          ("aeAndAoam", 9),
          ("baseFeatures", 0),
          ("carrierEdition", 4),
          ("dynamicVPLS", 1),
          ("pbb", 10),
          ("pbbTe", 7),
          ("pbt", 3),
          ("security", 2))
    )


_WwpLeosPremiumFeatureId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureId_Object = MibTableColumn
wwpLeosPremiumFeatureId = _WwpLeosPremiumFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 1),
    _WwpLeosPremiumFeatureId_Type()
)
wwpLeosPremiumFeatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureId.setStatus("current")


class _WwpLeosPremiumFeatureName_Type(OctetString):
    """Custom type wwpLeosPremiumFeatureName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosPremiumFeatureName_Type.__name__ = "OctetString"
_WwpLeosPremiumFeatureName_Object = MibTableColumn
wwpLeosPremiumFeatureName = _WwpLeosPremiumFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 2),
    _WwpLeosPremiumFeatureName_Type()
)
wwpLeosPremiumFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureName.setStatus("current")


class _WwpLeosPremiumFeatureDomainName_Type(OctetString):
    """Custom type wwpLeosPremiumFeatureDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosPremiumFeatureDomainName_Type.__name__ = "OctetString"
_WwpLeosPremiumFeatureDomainName_Object = MibTableColumn
wwpLeosPremiumFeatureDomainName = _WwpLeosPremiumFeatureDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 3),
    _WwpLeosPremiumFeatureDomainName_Type()
)
wwpLeosPremiumFeatureDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureDomainName.setStatus("current")


class _WwpLeosPremiumFeatureDomainId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureDomainId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureDomainId_Object = MibTableColumn
wwpLeosPremiumFeatureDomainId = _WwpLeosPremiumFeatureDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 4),
    _WwpLeosPremiumFeatureDomainId_Type()
)
wwpLeosPremiumFeatureDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureDomainId.setStatus("current")


class _WwpLeosPremiumFeatureCustomerId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureCustomerId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureCustomerId_Object = MibTableColumn
wwpLeosPremiumFeatureCustomerId = _WwpLeosPremiumFeatureCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 5),
    _WwpLeosPremiumFeatureCustomerId_Type()
)
wwpLeosPremiumFeatureCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureCustomerId.setStatus("current")


class _WwpLeosPremiumFeatureLicenseAdminId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseAdminId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseAdminId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseAdminId_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseAdminId = _WwpLeosPremiumFeatureLicenseAdminId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 6),
    _WwpLeosPremiumFeatureLicenseAdminId_Type()
)
wwpLeosPremiumFeatureLicenseAdminId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseAdminId.setStatus("current")


class _WwpLeosPremiumFeatureOperStatus_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureOperStatus based on Integer32"""
    defaultValue = 2

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
        *(("infoNotAvailable", 1),
          ("installed", 3),
          ("noBaseLic", 5),
          ("notInstalled", 2),
          ("partial", 4))
    )


_WwpLeosPremiumFeatureOperStatus_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureOperStatus_Object = MibTableColumn
wwpLeosPremiumFeatureOperStatus = _WwpLeosPremiumFeatureOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 7),
    _WwpLeosPremiumFeatureOperStatus_Type()
)
wwpLeosPremiumFeatureOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureOperStatus.setStatus("current")


class _WwpLeosPremiumFeatureDaysRemaining_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureDaysRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureDaysRemaining_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureDaysRemaining_Object = MibTableColumn
wwpLeosPremiumFeatureDaysRemaining = _WwpLeosPremiumFeatureDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 8),
    _WwpLeosPremiumFeatureDaysRemaining_Type()
)
wwpLeosPremiumFeatureDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureDaysRemaining.setStatus("current")


class _WwpLeosPremiumFeatureLicenseKey_Type(OctetString):
    """Custom type wwpLeosPremiumFeatureLicenseKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosPremiumFeatureLicenseKey_Type.__name__ = "OctetString"
_WwpLeosPremiumFeatureLicenseKey_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseKey = _WwpLeosPremiumFeatureLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 1, 1, 9),
    _WwpLeosPremiumFeatureLicenseKey_Type()
)
wwpLeosPremiumFeatureLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseKey.setStatus("current")
_WwpLeosPremiumFeatureLicenseKeyInstall_Type = DisplayString
_WwpLeosPremiumFeatureLicenseKeyInstall_Object = MibScalar
wwpLeosPremiumFeatureLicenseKeyInstall = _WwpLeosPremiumFeatureLicenseKeyInstall_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 2),
    _WwpLeosPremiumFeatureLicenseKeyInstall_Type()
)
wwpLeosPremiumFeatureLicenseKeyInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseKeyInstall.setStatus("current")
_WwpLeosPremiumFeatureLicenseNameUnInstall_Type = DisplayString
_WwpLeosPremiumFeatureLicenseNameUnInstall_Object = MibScalar
wwpLeosPremiumFeatureLicenseNameUnInstall = _WwpLeosPremiumFeatureLicenseNameUnInstall_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 1, 3),
    _WwpLeosPremiumFeatureLicenseNameUnInstall_Type()
)
wwpLeosPremiumFeatureLicenseNameUnInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseNameUnInstall.setStatus("current")
_WwpLeosPremiumFeatureLicenseStatusNotif_ObjectIdentity = ObjectIdentity
wwpLeosPremiumFeatureLicenseStatusNotif = _WwpLeosPremiumFeatureLicenseStatusNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 2)
)
_WwpLeosTcePremiumFeatureLicense_ObjectIdentity = ObjectIdentity
wwpLeosTcePremiumFeatureLicense = _WwpLeosTcePremiumFeatureLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10)
)
_WwpLeosPremiumFeatureLicenseInstalledTable_Object = MibTable
wwpLeosPremiumFeatureLicenseInstalledTable = _WwpLeosPremiumFeatureLicenseInstalledTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1)
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledTable.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstalledEntry_Object = MibTableRow
wwpLeosPremiumFeatureLicenseInstalledEntry = _WwpLeosPremiumFeatureLicenseInstalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1)
)
wwpLeosPremiumFeatureLicenseInstalledEntry.setIndexNames(
    (0, "WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureLicenseInstalledModuleIndex"),
    (0, "WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureId"),
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledEntry.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WwpLeosPremiumFeatureLicenseInstalledModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosPremiumFeatureLicenseInstalledModuleIndex_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledModuleIndex = _WwpLeosPremiumFeatureLicenseInstalledModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 1),
    _WwpLeosPremiumFeatureLicenseInstalledModuleIndex_Type()
)
wwpLeosPremiumFeatureLicenseInstalledModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledModuleIndex.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledOemId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledOemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseInstalledOemId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseInstalledOemId_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledOemId = _WwpLeosPremiumFeatureLicenseInstalledOemId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 3),
    _WwpLeosPremiumFeatureLicenseInstalledOemId_Type()
)
wwpLeosPremiumFeatureLicenseInstalledOemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledOemId.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledCustomerId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseInstalledCustomerId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseInstalledCustomerId_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledCustomerId = _WwpLeosPremiumFeatureLicenseInstalledCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 4),
    _WwpLeosPremiumFeatureLicenseInstalledCustomerId_Type()
)
wwpLeosPremiumFeatureLicenseInstalledCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledCustomerId.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledAdminId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledAdminId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseInstalledAdminId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseInstalledAdminId_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledAdminId = _WwpLeosPremiumFeatureLicenseInstalledAdminId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 5),
    _WwpLeosPremiumFeatureLicenseInstalledAdminId_Type()
)
wwpLeosPremiumFeatureLicenseInstalledAdminId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledAdminId.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledDaysRemaining_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledDaysRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseInstalledDaysRemaining_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseInstalledDaysRemaining_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledDaysRemaining = _WwpLeosPremiumFeatureLicenseInstalledDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 6),
    _WwpLeosPremiumFeatureLicenseInstalledDaysRemaining_Type()
)
wwpLeosPremiumFeatureLicenseInstalledDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledDaysRemaining.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstalledEnabled_Type = TruthValue
_WwpLeosPremiumFeatureLicenseInstalledEnabled_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledEnabled = _WwpLeosPremiumFeatureLicenseInstalledEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 7),
    _WwpLeosPremiumFeatureLicenseInstalledEnabled_Type()
)
wwpLeosPremiumFeatureLicenseInstalledEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledEnabled.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstalledSequence_Type = Unsigned32
_WwpLeosPremiumFeatureLicenseInstalledSequence_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledSequence = _WwpLeosPremiumFeatureLicenseInstalledSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 8),
    _WwpLeosPremiumFeatureLicenseInstalledSequence_Type()
)
wwpLeosPremiumFeatureLicenseInstalledSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledSequence.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledDomainId_Type(Integer32):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPremiumFeatureLicenseInstalledDomainId_Type.__name__ = "Integer32"
_WwpLeosPremiumFeatureLicenseInstalledDomainId_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledDomainId = _WwpLeosPremiumFeatureLicenseInstalledDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 9),
    _WwpLeosPremiumFeatureLicenseInstalledDomainId_Type()
)
wwpLeosPremiumFeatureLicenseInstalledDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledDomainId.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstalledName_Type = DisplayString
_WwpLeosPremiumFeatureLicenseInstalledName_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledName = _WwpLeosPremiumFeatureLicenseInstalledName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 10),
    _WwpLeosPremiumFeatureLicenseInstalledName_Type()
)
wwpLeosPremiumFeatureLicenseInstalledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledName.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstalledDomainName_Type = DisplayString
_WwpLeosPremiumFeatureLicenseInstalledDomainName_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledDomainName = _WwpLeosPremiumFeatureLicenseInstalledDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 11),
    _WwpLeosPremiumFeatureLicenseInstalledDomainName_Type()
)
wwpLeosPremiumFeatureLicenseInstalledDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledDomainName.setStatus("current")


class _WwpLeosPremiumFeatureLicenseInstalledKey_Type(OctetString):
    """Custom type wwpLeosPremiumFeatureLicenseInstalledKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosPremiumFeatureLicenseInstalledKey_Type.__name__ = "OctetString"
_WwpLeosPremiumFeatureLicenseInstalledKey_Object = MibTableColumn
wwpLeosPremiumFeatureLicenseInstalledKey = _WwpLeosPremiumFeatureLicenseInstalledKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 1, 1, 12),
    _WwpLeosPremiumFeatureLicenseInstalledKey_Type()
)
wwpLeosPremiumFeatureLicenseInstalledKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstalledKey.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstall_ObjectIdentity = ObjectIdentity
wwpLeosPremiumFeatureLicenseInstall = _WwpLeosPremiumFeatureLicenseInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 2)
)


class _WwpLeosPremiumFeatureLicenseInstallModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosPremiumFeatureLicenseInstallModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WwpLeosPremiumFeatureLicenseInstallModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosPremiumFeatureLicenseInstallModuleIndex_Object = MibScalar
wwpLeosPremiumFeatureLicenseInstallModuleIndex = _WwpLeosPremiumFeatureLicenseInstallModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 2, 1),
    _WwpLeosPremiumFeatureLicenseInstallModuleIndex_Type()
)
wwpLeosPremiumFeatureLicenseInstallModuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstallModuleIndex.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstallKey_Type = DisplayString
_WwpLeosPremiumFeatureLicenseInstallKey_Object = MibScalar
wwpLeosPremiumFeatureLicenseInstallKey = _WwpLeosPremiumFeatureLicenseInstallKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 2, 2),
    _WwpLeosPremiumFeatureLicenseInstallKey_Type()
)
wwpLeosPremiumFeatureLicenseInstallKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstallKey.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstallCommit_Type = TruthValue
_WwpLeosPremiumFeatureLicenseInstallCommit_Object = MibScalar
wwpLeosPremiumFeatureLicenseInstallCommit = _WwpLeosPremiumFeatureLicenseInstallCommit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 2, 3),
    _WwpLeosPremiumFeatureLicenseInstallCommit_Type()
)
wwpLeosPremiumFeatureLicenseInstallCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstallCommit.setStatus("current")
_WwpLeosPremiumFeatureLicenseInstallUnsuccessful_Type = DisplayString
_WwpLeosPremiumFeatureLicenseInstallUnsuccessful_Object = MibScalar
wwpLeosPremiumFeatureLicenseInstallUnsuccessful = _WwpLeosPremiumFeatureLicenseInstallUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 2, 4),
    _WwpLeosPremiumFeatureLicenseInstallUnsuccessful_Type()
)
wwpLeosPremiumFeatureLicenseInstallUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstallUnsuccessful.setStatus("current")
_WwpLeosPremiumFeatureLicenseUninstall_ObjectIdentity = ObjectIdentity
wwpLeosPremiumFeatureLicenseUninstall = _WwpLeosPremiumFeatureLicenseUninstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 3)
)


class _WwpLeosPremiumFeatureLicenseUninstallModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosPremiumFeatureLicenseUninstallModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WwpLeosPremiumFeatureLicenseUninstallModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosPremiumFeatureLicenseUninstallModuleIndex_Object = MibScalar
wwpLeosPremiumFeatureLicenseUninstallModuleIndex = _WwpLeosPremiumFeatureLicenseUninstallModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 3, 1),
    _WwpLeosPremiumFeatureLicenseUninstallModuleIndex_Type()
)
wwpLeosPremiumFeatureLicenseUninstallModuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseUninstallModuleIndex.setStatus("current")
_WwpLeosPremiumFeatureLicenseUninstallName_Type = DisplayString
_WwpLeosPremiumFeatureLicenseUninstallName_Object = MibScalar
wwpLeosPremiumFeatureLicenseUninstallName = _WwpLeosPremiumFeatureLicenseUninstallName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 3, 2),
    _WwpLeosPremiumFeatureLicenseUninstallName_Type()
)
wwpLeosPremiumFeatureLicenseUninstallName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseUninstallName.setStatus("current")
_WwpLeosPremiumFeatureLicenseUninstallCommit_Type = TruthValue
_WwpLeosPremiumFeatureLicenseUninstallCommit_Object = MibScalar
wwpLeosPremiumFeatureLicenseUninstallCommit = _WwpLeosPremiumFeatureLicenseUninstallCommit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 1, 10, 3, 3),
    _WwpLeosPremiumFeatureLicenseUninstallCommit_Type()
)
wwpLeosPremiumFeatureLicenseUninstallCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseUninstallCommit.setStatus("current")
_WwpLeosFeatureLicenseMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBNotificationPrefix = _WwpLeosFeatureLicenseMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 2)
)
_WwpLeosFeatureLicenseMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBNotifications = _WwpLeosFeatureLicenseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 2, 0)
)
_WwpLeosFeatureLicenseMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBConformance = _WwpLeosFeatureLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 3)
)
_WwpLeosFeatureLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBCompliances = _WwpLeosFeatureLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 3, 1)
)
_WwpLeosFeatureLicenseMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosFeatureLicenseMIBGroups = _WwpLeosFeatureLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosPremiumFeatureLicenseStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 2, 0, 1)
)
wwpLeosPremiumFeatureLicenseStatusNotification.setObjects(
      *(("WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureName"),
        ("WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureOperStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseStatusNotification.setStatus(
        "current"
    )

wwpLeosPremiumFeatureLicenseInstallErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 29, 2, 0, 2)
)
wwpLeosPremiumFeatureLicenseInstallErrorNotification.setObjects(
      *(("WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureLicenseInstallModuleIndex"),
        ("WWP-LEOS-FEATURE-LICENSE-MIB", "wwpLeosPremiumFeatureLicenseInstallUnsuccessful"))
)
if mibBuilder.loadTexts:
    wwpLeosPremiumFeatureLicenseInstallErrorNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-FEATURE-LICENSE-MIB",
    **{"wwpLeosFeatureLicenseMIB": wwpLeosFeatureLicenseMIB,
       "wwpLeosFeatureLicenseMIBObjects": wwpLeosFeatureLicenseMIBObjects,
       "wwpLeosPremiumFeatureLicense": wwpLeosPremiumFeatureLicense,
       "wwpLeosPremiumFeatureStatusTable": wwpLeosPremiumFeatureStatusTable,
       "wwpLeosPremiumFeatureStatusEntry": wwpLeosPremiumFeatureStatusEntry,
       "wwpLeosPremiumFeatureId": wwpLeosPremiumFeatureId,
       "wwpLeosPremiumFeatureName": wwpLeosPremiumFeatureName,
       "wwpLeosPremiumFeatureDomainName": wwpLeosPremiumFeatureDomainName,
       "wwpLeosPremiumFeatureDomainId": wwpLeosPremiumFeatureDomainId,
       "wwpLeosPremiumFeatureCustomerId": wwpLeosPremiumFeatureCustomerId,
       "wwpLeosPremiumFeatureLicenseAdminId": wwpLeosPremiumFeatureLicenseAdminId,
       "wwpLeosPremiumFeatureOperStatus": wwpLeosPremiumFeatureOperStatus,
       "wwpLeosPremiumFeatureDaysRemaining": wwpLeosPremiumFeatureDaysRemaining,
       "wwpLeosPremiumFeatureLicenseKey": wwpLeosPremiumFeatureLicenseKey,
       "wwpLeosPremiumFeatureLicenseKeyInstall": wwpLeosPremiumFeatureLicenseKeyInstall,
       "wwpLeosPremiumFeatureLicenseNameUnInstall": wwpLeosPremiumFeatureLicenseNameUnInstall,
       "wwpLeosPremiumFeatureLicenseStatusNotif": wwpLeosPremiumFeatureLicenseStatusNotif,
       "wwpLeosTcePremiumFeatureLicense": wwpLeosTcePremiumFeatureLicense,
       "wwpLeosPremiumFeatureLicenseInstalledTable": wwpLeosPremiumFeatureLicenseInstalledTable,
       "wwpLeosPremiumFeatureLicenseInstalledEntry": wwpLeosPremiumFeatureLicenseInstalledEntry,
       "wwpLeosPremiumFeatureLicenseInstalledModuleIndex": wwpLeosPremiumFeatureLicenseInstalledModuleIndex,
       "wwpLeosPremiumFeatureLicenseInstalledOemId": wwpLeosPremiumFeatureLicenseInstalledOemId,
       "wwpLeosPremiumFeatureLicenseInstalledCustomerId": wwpLeosPremiumFeatureLicenseInstalledCustomerId,
       "wwpLeosPremiumFeatureLicenseInstalledAdminId": wwpLeosPremiumFeatureLicenseInstalledAdminId,
       "wwpLeosPremiumFeatureLicenseInstalledDaysRemaining": wwpLeosPremiumFeatureLicenseInstalledDaysRemaining,
       "wwpLeosPremiumFeatureLicenseInstalledEnabled": wwpLeosPremiumFeatureLicenseInstalledEnabled,
       "wwpLeosPremiumFeatureLicenseInstalledSequence": wwpLeosPremiumFeatureLicenseInstalledSequence,
       "wwpLeosPremiumFeatureLicenseInstalledDomainId": wwpLeosPremiumFeatureLicenseInstalledDomainId,
       "wwpLeosPremiumFeatureLicenseInstalledName": wwpLeosPremiumFeatureLicenseInstalledName,
       "wwpLeosPremiumFeatureLicenseInstalledDomainName": wwpLeosPremiumFeatureLicenseInstalledDomainName,
       "wwpLeosPremiumFeatureLicenseInstalledKey": wwpLeosPremiumFeatureLicenseInstalledKey,
       "wwpLeosPremiumFeatureLicenseInstall": wwpLeosPremiumFeatureLicenseInstall,
       "wwpLeosPremiumFeatureLicenseInstallModuleIndex": wwpLeosPremiumFeatureLicenseInstallModuleIndex,
       "wwpLeosPremiumFeatureLicenseInstallKey": wwpLeosPremiumFeatureLicenseInstallKey,
       "wwpLeosPremiumFeatureLicenseInstallCommit": wwpLeosPremiumFeatureLicenseInstallCommit,
       "wwpLeosPremiumFeatureLicenseInstallUnsuccessful": wwpLeosPremiumFeatureLicenseInstallUnsuccessful,
       "wwpLeosPremiumFeatureLicenseUninstall": wwpLeosPremiumFeatureLicenseUninstall,
       "wwpLeosPremiumFeatureLicenseUninstallModuleIndex": wwpLeosPremiumFeatureLicenseUninstallModuleIndex,
       "wwpLeosPremiumFeatureLicenseUninstallName": wwpLeosPremiumFeatureLicenseUninstallName,
       "wwpLeosPremiumFeatureLicenseUninstallCommit": wwpLeosPremiumFeatureLicenseUninstallCommit,
       "wwpLeosFeatureLicenseMIBNotificationPrefix": wwpLeosFeatureLicenseMIBNotificationPrefix,
       "wwpLeosFeatureLicenseMIBNotifications": wwpLeosFeatureLicenseMIBNotifications,
       "wwpLeosPremiumFeatureLicenseStatusNotification": wwpLeosPremiumFeatureLicenseStatusNotification,
       "wwpLeosPremiumFeatureLicenseInstallErrorNotification": wwpLeosPremiumFeatureLicenseInstallErrorNotification,
       "wwpLeosFeatureLicenseMIBConformance": wwpLeosFeatureLicenseMIBConformance,
       "wwpLeosFeatureLicenseMIBCompliances": wwpLeosFeatureLicenseMIBCompliances,
       "wwpLeosFeatureLicenseMIBGroups": wwpLeosFeatureLicenseMIBGroups}
)
