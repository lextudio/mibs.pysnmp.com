# SNMP MIB module (CISCO-DMN-DSG-FEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-FEATURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:24 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGFeature = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27)
)
ciscoDSGFeature.setRevisions(
        ("2012-02-28 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FeatureTable_ObjectIdentity = ObjectIdentity
featureTable = _FeatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2)
)
_FeatureLicenceTable_Object = MibTable
featureLicenceTable = _FeatureLicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 1)
)
if mibBuilder.loadTexts:
    featureLicenceTable.setStatus("current")
_FeatureLicenceEntry_Object = MibTableRow
featureLicenceEntry = _FeatureLicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 1, 1)
)
featureLicenceEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FEATURE-MIB", "featureLicenceIdx"),
)
if mibBuilder.loadTexts:
    featureLicenceEntry.setStatus("current")


class _FeatureLicenceIdx_Type(Integer32):
    """Custom type featureLicenceIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FeatureLicenceIdx_Type.__name__ = "Integer32"
_FeatureLicenceIdx_Object = MibTableColumn
featureLicenceIdx = _FeatureLicenceIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 1, 1, 1),
    _FeatureLicenceIdx_Type()
)
featureLicenceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    featureLicenceIdx.setStatus("current")


class _FeatureLicenceID_Type(DisplayString):
    """Custom type featureLicenceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FeatureLicenceID_Type.__name__ = "DisplayString"
_FeatureLicenceID_Object = MibTableColumn
featureLicenceID = _FeatureLicenceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 1, 1, 2),
    _FeatureLicenceID_Type()
)
featureLicenceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureLicenceID.setStatus("current")


class _FeatureLicenceStatus_Type(DisplayString):
    """Custom type featureLicenceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FeatureLicenceStatus_Type.__name__ = "DisplayString"
_FeatureLicenceStatus_Object = MibTableColumn
featureLicenceStatus = _FeatureLicenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 1, 1, 3),
    _FeatureLicenceStatus_Type()
)
featureLicenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureLicenceStatus.setStatus("current")
_InstalledOptionTable_Object = MibTable
installedOptionTable = _InstalledOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 2)
)
if mibBuilder.loadTexts:
    installedOptionTable.setStatus("current")
_InstalledOptionEntry_Object = MibTableRow
installedOptionEntry = _InstalledOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 2, 1)
)
installedOptionEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FEATURE-MIB", "installedOptionIdx"),
)
if mibBuilder.loadTexts:
    installedOptionEntry.setStatus("current")


class _InstalledOptionIdx_Type(Integer32):
    """Custom type installedOptionIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_InstalledOptionIdx_Type.__name__ = "Integer32"
_InstalledOptionIdx_Object = MibTableColumn
installedOptionIdx = _InstalledOptionIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 2, 1, 1),
    _InstalledOptionIdx_Type()
)
installedOptionIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    installedOptionIdx.setStatus("current")


class _InstalledOptionID_Type(DisplayString):
    """Custom type installedOptionID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InstalledOptionID_Type.__name__ = "DisplayString"
_InstalledOptionID_Object = MibTableColumn
installedOptionID = _InstalledOptionID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 2, 1, 2),
    _InstalledOptionID_Type()
)
installedOptionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedOptionID.setStatus("current")


class _InstalledOptionStatus_Type(DisplayString):
    """Custom type installedOptionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InstalledOptionStatus_Type.__name__ = "DisplayString"
_InstalledOptionStatus_Object = MibTableColumn
installedOptionStatus = _InstalledOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 27, 2, 2, 1, 3),
    _InstalledOptionStatus_Type()
)
installedOptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedOptionStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-FEATURE-MIB",
    **{"ciscoDSGFeature": ciscoDSGFeature,
       "featureTable": featureTable,
       "featureLicenceTable": featureLicenceTable,
       "featureLicenceEntry": featureLicenceEntry,
       "featureLicenceIdx": featureLicenceIdx,
       "featureLicenceID": featureLicenceID,
       "featureLicenceStatus": featureLicenceStatus,
       "installedOptionTable": installedOptionTable,
       "installedOptionEntry": installedOptionEntry,
       "installedOptionIdx": installedOptionIdx,
       "installedOptionID": installedOptionID,
       "installedOptionStatus": installedOptionStatus}
)
