# SNMP MIB module (TPT-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:58 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_license_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15)
)
tpt_license_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LicenseStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("info", 0),
          ("ok", 1),
          ("warning", 2))
    )



class LicenseAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("deny", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1)
)
licenseEntry.setIndexNames(
    (0, "TPT-LICENSE-MIB", "licenseEntryIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")
_LicenseEntryIndex_Type = Unsigned32
_LicenseEntryIndex_Object = MibTableColumn
licenseEntryIndex = _LicenseEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 1),
    _LicenseEntryIndex_Type()
)
licenseEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseEntryIndex.setStatus("current")


class _LicenseEntryFeature_Type(OctetString):
    """Custom type licenseEntryFeature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LicenseEntryFeature_Type.__name__ = "OctetString"
_LicenseEntryFeature_Object = MibTableColumn
licenseEntryFeature = _LicenseEntryFeature_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 2),
    _LicenseEntryFeature_Type()
)
licenseEntryFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEntryFeature.setStatus("current")
_LicenseEntryStatus_Type = LicenseStatus
_LicenseEntryStatus_Object = MibTableColumn
licenseEntryStatus = _LicenseEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 3),
    _LicenseEntryStatus_Type()
)
licenseEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEntryStatus.setStatus("current")
_LicenseEntryAction_Type = LicenseAction
_LicenseEntryAction_Object = MibTableColumn
licenseEntryAction = _LicenseEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 4),
    _LicenseEntryAction_Type()
)
licenseEntryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEntryAction.setStatus("current")


class _LicenseEntryExpiry_Type(OctetString):
    """Custom type licenseEntryExpiry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LicenseEntryExpiry_Type.__name__ = "OctetString"
_LicenseEntryExpiry_Object = MibTableColumn
licenseEntryExpiry = _LicenseEntryExpiry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 5),
    _LicenseEntryExpiry_Type()
)
licenseEntryExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEntryExpiry.setStatus("current")


class _LicenseEntryDetails_Type(OctetString):
    """Custom type licenseEntryDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LicenseEntryDetails_Type.__name__ = "OctetString"
_LicenseEntryDetails_Object = MibTableColumn
licenseEntryDetails = _LicenseEntryDetails_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 6),
    _LicenseEntryDetails_Type()
)
licenseEntryDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEntryDetails.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-LICENSE-MIB",
    **{"LicenseStatus": LicenseStatus,
       "LicenseAction": LicenseAction,
       "tpt-license-objs": tpt_license_objs,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseEntryIndex": licenseEntryIndex,
       "licenseEntryFeature": licenseEntryFeature,
       "licenseEntryStatus": licenseEntryStatus,
       "licenseEntryAction": licenseEntryAction,
       "licenseEntryExpiry": licenseEntryExpiry,
       "licenseEntryDetails": licenseEntryDetails}
)
