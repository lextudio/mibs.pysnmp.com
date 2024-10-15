# SNMP MIB module (HH3C-DOT11-LIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-LIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:52 2024
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "hh3cDot11")

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


# MODULE-IDENTITY

hh3cDot11LIC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14)
)
hh3cDot11LIC.setRevisions(
        ("2012-04-25 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11LICConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11LICConfigGroup = _Hh3cDot11LICConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 1)
)


class _Hh3cDot11LICSerialNumber_Type(OctetString):
    """Custom type hh3cDot11LICSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11LICSerialNumber_Type.__name__ = "OctetString"
_Hh3cDot11LICSerialNumber_Object = MibScalar
hh3cDot11LICSerialNumber = _Hh3cDot11LICSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 1, 1),
    _Hh3cDot11LICSerialNumber_Type()
)
hh3cDot11LICSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICSerialNumber.setStatus("current")


class _Hh3cDot11LicApNumGroupSupport_Type(TruthValue):
    """Custom type hh3cDot11LicApNumGroupSupport based on TruthValue"""


_Hh3cDot11LicApNumGroupSupport_Object = MibScalar
hh3cDot11LicApNumGroupSupport = _Hh3cDot11LicApNumGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 1, 2),
    _Hh3cDot11LicApNumGroupSupport_Type()
)
hh3cDot11LicApNumGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LicApNumGroupSupport.setStatus("current")
_Hh3cDot11LICApNumGroup_ObjectIdentity = ObjectIdentity
hh3cDot11LICApNumGroup = _Hh3cDot11LICApNumGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2)
)
_Hh3cDot11LICApNumAttrTable_ObjectIdentity = ObjectIdentity
hh3cDot11LICApNumAttrTable = _Hh3cDot11LICApNumAttrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 1)
)
_Hh3cDot11LICDefautAPNumPermit_Type = Integer32
_Hh3cDot11LICDefautAPNumPermit_Object = MibScalar
hh3cDot11LICDefautAPNumPermit = _Hh3cDot11LICDefautAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 1, 1),
    _Hh3cDot11LICDefautAPNumPermit_Type()
)
hh3cDot11LICDefautAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICDefautAPNumPermit.setStatus("current")
_Hh3cDot11LICCurrentAPNumPermit_Type = Integer32
_Hh3cDot11LICCurrentAPNumPermit_Object = MibScalar
hh3cDot11LICCurrentAPNumPermit = _Hh3cDot11LICCurrentAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 1, 2),
    _Hh3cDot11LICCurrentAPNumPermit_Type()
)
hh3cDot11LICCurrentAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICCurrentAPNumPermit.setStatus("current")
_Hh3cDot11LICMaxAPNumPermit_Type = Integer32
_Hh3cDot11LICMaxAPNumPermit_Object = MibScalar
hh3cDot11LICMaxAPNumPermit = _Hh3cDot11LICMaxAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 1, 3),
    _Hh3cDot11LICMaxAPNumPermit_Type()
)
hh3cDot11LICMaxAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICMaxAPNumPermit.setStatus("current")
_Hh3cDot11LICApNumLicTable_Object = MibTable
hh3cDot11LICApNumLicTable = _Hh3cDot11LICApNumLicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11LICApNumLicTable.setStatus("current")
_Hh3cDot11LICApNumLicEntry_Object = MibTableRow
hh3cDot11LICApNumLicEntry = _Hh3cDot11LICApNumLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2, 1)
)
hh3cDot11LICApNumLicEntry.setIndexNames(
    (0, "HH3C-DOT11-LIC-MIB", "hh3cDot11LICLicenseKeyIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11LICApNumLicEntry.setStatus("current")


class _Hh3cDot11LICLicenseKeyIndex_Type(Integer32):
    """Custom type hh3cDot11LICLicenseKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11LICLicenseKeyIndex_Type.__name__ = "Integer32"
_Hh3cDot11LICLicenseKeyIndex_Object = MibTableColumn
hh3cDot11LICLicenseKeyIndex = _Hh3cDot11LICLicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2, 1, 1),
    _Hh3cDot11LICLicenseKeyIndex_Type()
)
hh3cDot11LICLicenseKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICLicenseKeyIndex.setStatus("current")
_Hh3cDot11LICLicenseKey_Type = OctetString
_Hh3cDot11LICLicenseKey_Object = MibTableColumn
hh3cDot11LICLicenseKey = _Hh3cDot11LICLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2, 1, 2),
    _Hh3cDot11LICLicenseKey_Type()
)
hh3cDot11LICLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICLicenseKey.setStatus("current")
_Hh3cDot11LICActivationKey_Type = OctetString
_Hh3cDot11LICActivationKey_Object = MibTableColumn
hh3cDot11LICActivationKey = _Hh3cDot11LICActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2, 1, 3),
    _Hh3cDot11LICActivationKey_Type()
)
hh3cDot11LICActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICActivationKey.setStatus("current")
_Hh3cDot11LICApNum_Type = Integer32
_Hh3cDot11LICApNum_Object = MibTableColumn
hh3cDot11LICApNum = _Hh3cDot11LICApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 2, 2, 1, 4),
    _Hh3cDot11LICApNum_Type()
)
hh3cDot11LICApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICApNum.setStatus("current")
_Hh3cDot11LICFeatureGroup_ObjectIdentity = ObjectIdentity
hh3cDot11LICFeatureGroup = _Hh3cDot11LICFeatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3)
)
_Hh3cDot11LICFeatureAttrTable_Object = MibTable
hh3cDot11LICFeatureAttrTable = _Hh3cDot11LICFeatureAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11LICFeatureAttrTable.setStatus("current")
_Hh3cDot11LICFeatureAttrEntry_Object = MibTableRow
hh3cDot11LICFeatureAttrEntry = _Hh3cDot11LICFeatureAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1, 1)
)
hh3cDot11LICFeatureAttrEntry.setIndexNames(
    (0, "HH3C-DOT11-LIC-MIB", "hh3cDot11LICAttrIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11LICFeatureAttrEntry.setStatus("current")


class _Hh3cDot11LICAttrIndex_Type(Integer32):
    """Custom type hh3cDot11LICAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11LICAttrIndex_Type.__name__ = "Integer32"
_Hh3cDot11LICAttrIndex_Object = MibTableColumn
hh3cDot11LICAttrIndex = _Hh3cDot11LICAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1, 1, 1),
    _Hh3cDot11LICAttrIndex_Type()
)
hh3cDot11LICAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICAttrIndex.setStatus("current")
_Hh3cDot11LICAttrTypeName_Type = OctetString
_Hh3cDot11LICAttrTypeName_Object = MibTableColumn
hh3cDot11LICAttrTypeName = _Hh3cDot11LICAttrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1, 1, 2),
    _Hh3cDot11LICAttrTypeName_Type()
)
hh3cDot11LICAttrTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICAttrTypeName.setStatus("current")
_Hh3cDot11LICAttrDefVal_Type = Integer32
_Hh3cDot11LICAttrDefVal_Object = MibTableColumn
hh3cDot11LICAttrDefVal = _Hh3cDot11LICAttrDefVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1, 1, 3),
    _Hh3cDot11LICAttrDefVal_Type()
)
hh3cDot11LICAttrDefVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICAttrDefVal.setStatus("current")
_Hh3cDot11LICAttrMaxVal_Type = Integer32
_Hh3cDot11LICAttrMaxVal_Object = MibTableColumn
hh3cDot11LICAttrMaxVal = _Hh3cDot11LICAttrMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 1, 1, 4),
    _Hh3cDot11LICAttrMaxVal_Type()
)
hh3cDot11LICAttrMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICAttrMaxVal.setStatus("current")
_Hh3cDot11LICFeatureLicTable_Object = MibTable
hh3cDot11LICFeatureLicTable = _Hh3cDot11LICFeatureLicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11LICFeatureLicTable.setStatus("current")
_Hh3cDot11LICFeatureLicEntry_Object = MibTableRow
hh3cDot11LICFeatureLicEntry = _Hh3cDot11LICFeatureLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1)
)
hh3cDot11LICFeatureLicEntry.setIndexNames(
    (0, "HH3C-DOT11-LIC-MIB", "hh3cDot11LICKeyIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11LICFeatureLicEntry.setStatus("current")


class _Hh3cDot11LICKeyIndex_Type(Integer32):
    """Custom type hh3cDot11LICKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11LICKeyIndex_Type.__name__ = "Integer32"
_Hh3cDot11LICKeyIndex_Object = MibTableColumn
hh3cDot11LICKeyIndex = _Hh3cDot11LICKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1, 1),
    _Hh3cDot11LICKeyIndex_Type()
)
hh3cDot11LICKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICKeyIndex.setStatus("current")
_Hh3cDot11LICTypeName_Type = OctetString
_Hh3cDot11LICTypeName_Object = MibTableColumn
hh3cDot11LICTypeName = _Hh3cDot11LICTypeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1, 2),
    _Hh3cDot11LICTypeName_Type()
)
hh3cDot11LICTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICTypeName.setStatus("current")
_Hh3cDot11LICKey_Type = OctetString
_Hh3cDot11LICKey_Object = MibTableColumn
hh3cDot11LICKey = _Hh3cDot11LICKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1, 3),
    _Hh3cDot11LICKey_Type()
)
hh3cDot11LICKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICKey.setStatus("current")
_Hh3cDot11LICTimeLimit_Type = Integer32
_Hh3cDot11LICTimeLimit_Object = MibTableColumn
hh3cDot11LICTimeLimit = _Hh3cDot11LICTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1, 4),
    _Hh3cDot11LICTimeLimit_Type()
)
hh3cDot11LICTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICTimeLimit.setStatus("current")
_Hh3cDot11LICValue_Type = Integer32
_Hh3cDot11LICValue_Object = MibTableColumn
hh3cDot11LICValue = _Hh3cDot11LICValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 14, 3, 2, 1, 5),
    _Hh3cDot11LICValue_Type()
)
hh3cDot11LICValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LICValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-LIC-MIB",
    **{"hh3cDot11LIC": hh3cDot11LIC,
       "hh3cDot11LICConfigGroup": hh3cDot11LICConfigGroup,
       "hh3cDot11LICSerialNumber": hh3cDot11LICSerialNumber,
       "hh3cDot11LicApNumGroupSupport": hh3cDot11LicApNumGroupSupport,
       "hh3cDot11LICApNumGroup": hh3cDot11LICApNumGroup,
       "hh3cDot11LICApNumAttrTable": hh3cDot11LICApNumAttrTable,
       "hh3cDot11LICDefautAPNumPermit": hh3cDot11LICDefautAPNumPermit,
       "hh3cDot11LICCurrentAPNumPermit": hh3cDot11LICCurrentAPNumPermit,
       "hh3cDot11LICMaxAPNumPermit": hh3cDot11LICMaxAPNumPermit,
       "hh3cDot11LICApNumLicTable": hh3cDot11LICApNumLicTable,
       "hh3cDot11LICApNumLicEntry": hh3cDot11LICApNumLicEntry,
       "hh3cDot11LICLicenseKeyIndex": hh3cDot11LICLicenseKeyIndex,
       "hh3cDot11LICLicenseKey": hh3cDot11LICLicenseKey,
       "hh3cDot11LICActivationKey": hh3cDot11LICActivationKey,
       "hh3cDot11LICApNum": hh3cDot11LICApNum,
       "hh3cDot11LICFeatureGroup": hh3cDot11LICFeatureGroup,
       "hh3cDot11LICFeatureAttrTable": hh3cDot11LICFeatureAttrTable,
       "hh3cDot11LICFeatureAttrEntry": hh3cDot11LICFeatureAttrEntry,
       "hh3cDot11LICAttrIndex": hh3cDot11LICAttrIndex,
       "hh3cDot11LICAttrTypeName": hh3cDot11LICAttrTypeName,
       "hh3cDot11LICAttrDefVal": hh3cDot11LICAttrDefVal,
       "hh3cDot11LICAttrMaxVal": hh3cDot11LICAttrMaxVal,
       "hh3cDot11LICFeatureLicTable": hh3cDot11LICFeatureLicTable,
       "hh3cDot11LICFeatureLicEntry": hh3cDot11LICFeatureLicEntry,
       "hh3cDot11LICKeyIndex": hh3cDot11LICKeyIndex,
       "hh3cDot11LICTypeName": hh3cDot11LICTypeName,
       "hh3cDot11LICKey": hh3cDot11LICKey,
       "hh3cDot11LICTimeLimit": hh3cDot11LICTimeLimit,
       "hh3cDot11LICValue": hh3cDot11LICValue}
)
