# SNMP MIB module (GENLIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENLIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:33 2024
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

license = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 81, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lannet_ObjectIdentity = ObjectIdentity
lannet = _Lannet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81)
)
_LicensePerModule_ObjectIdentity = ObjectIdentity
licensePerModule = _LicensePerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 37, 1)
)
_LicModuleIdentTable_Object = MibTable
licModuleIdentTable = _LicModuleIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 1)
)
if mibBuilder.loadTexts:
    licModuleIdentTable.setStatus("current")
_LicModuleIdentEntry_Object = MibTableRow
licModuleIdentEntry = _LicModuleIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1)
)
licModuleIdentEntry.setIndexNames(
    (0, "GENLIC-MIB", "licModuleIdentIndex"),
)
if mibBuilder.loadTexts:
    licModuleIdentEntry.setStatus("current")


class _LicModuleIdentIndex_Type(Integer32):
    """Custom type licModuleIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LicModuleIdentIndex_Type.__name__ = "Integer32"
_LicModuleIdentIndex_Object = MibTableColumn
licModuleIdentIndex = _LicModuleIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1, 1),
    _LicModuleIdentIndex_Type()
)
licModuleIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licModuleIdentIndex.setStatus("current")


class _LicModuleIdentUniqueID_Type(OctetString):
    """Custom type licModuleIdentUniqueID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LicModuleIdentUniqueID_Type.__name__ = "OctetString"
_LicModuleIdentUniqueID_Object = MibTableColumn
licModuleIdentUniqueID = _LicModuleIdentUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1, 2),
    _LicModuleIdentUniqueID_Type()
)
licModuleIdentUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licModuleIdentUniqueID.setStatus("current")
_LicFeatureTable_Object = MibTable
licFeatureTable = _LicFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2)
)
if mibBuilder.loadTexts:
    licFeatureTable.setStatus("current")
_LicFeatureTableEntry_Object = MibTableRow
licFeatureTableEntry = _LicFeatureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1)
)
licFeatureTableEntry.setIndexNames(
    (0, "GENLIC-MIB", "licModuleIdentIndex"),
    (0, "GENLIC-MIB", "licFeatureId"),
)
if mibBuilder.loadTexts:
    licFeatureTableEntry.setStatus("current")


class _LicFeatureId_Type(Integer32):
    """Custom type licFeatureId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              208,
              209)
        )
    )
    namedValues = NamedValues(
        *(("cajunViewPlus", 208),
          ("loadBalance", 6),
          ("realNetRules", 209),
          ("rfc1483", 5),
          ("richLayer2", 2),
          ("routing", 3),
          ("serverLoadBalance", 4),
          ("smon", 1))
    )


_LicFeatureId_Type.__name__ = "Integer32"
_LicFeatureId_Object = MibTableColumn
licFeatureId = _LicFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 1),
    _LicFeatureId_Type()
)
licFeatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licFeatureId.setStatus("current")


class _LicFeatureModifier_Type(OctetString):
    """Custom type licFeatureModifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LicFeatureModifier_Type.__name__ = "OctetString"
_LicFeatureModifier_Object = MibTableColumn
licFeatureModifier = _LicFeatureModifier_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 2),
    _LicFeatureModifier_Type()
)
licFeatureModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licFeatureModifier.setStatus("current")


class _LicFeatureName_Type(DisplayString):
    """Custom type licFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_LicFeatureName_Type.__name__ = "DisplayString"
_LicFeatureName_Object = MibTableColumn
licFeatureName = _LicFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 3),
    _LicFeatureName_Type()
)
licFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licFeatureName.setStatus("current")


class _LicFeatureLicense_Type(OctetString):
    """Custom type licFeatureLicense based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_LicFeatureLicense_Type.__name__ = "OctetString"
_LicFeatureLicense_Object = MibTableColumn
licFeatureLicense = _LicFeatureLicense_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 4),
    _LicFeatureLicense_Type()
)
licFeatureLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licFeatureLicense.setStatus("current")


class _LicFeatureLicenseStatus_Type(Integer32):
    """Custom type licFeatureLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensed", 1),
          ("unlicensed", 2))
    )


_LicFeatureLicenseStatus_Type.__name__ = "Integer32"
_LicFeatureLicenseStatus_Object = MibTableColumn
licFeatureLicenseStatus = _LicFeatureLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 5),
    _LicFeatureLicenseStatus_Type()
)
licFeatureLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licFeatureLicenseStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENLIC-MIB",
    **{"lannet": lannet,
       "license": license,
       "licensePerModule": licensePerModule,
       "licModuleIdentTable": licModuleIdentTable,
       "licModuleIdentEntry": licModuleIdentEntry,
       "licModuleIdentIndex": licModuleIdentIndex,
       "licModuleIdentUniqueID": licModuleIdentUniqueID,
       "licFeatureTable": licFeatureTable,
       "licFeatureTableEntry": licFeatureTableEntry,
       "licFeatureId": licFeatureId,
       "licFeatureModifier": licFeatureModifier,
       "licFeatureName": licFeatureName,
       "licFeatureLicense": licFeatureLicense,
       "licFeatureLicenseStatus": licFeatureLicenseStatus}
)
