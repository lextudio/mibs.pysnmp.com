# SNMP MIB module (MERU-CONFIG-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:02 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlLicenseType,
 MwlSofwControllerType) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlLicenseType",
    "MwlSofwControllerType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigLicense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwLicenseTemplateTable_Object = MibTable
mwLicenseTemplateTable = _MwLicenseTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    mwLicenseTemplateTable.setStatus("current")
_MwLicenseTemplateEntry_Object = MibTableRow
mwLicenseTemplateEntry = _MwLicenseTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1)
)
mwLicenseTemplateEntry.setIndexNames(
    (0, "MERU-CONFIG-LICENSE-MIB", "mwLicenseTemplateTableIndex"),
)
if mibBuilder.loadTexts:
    mwLicenseTemplateEntry.setStatus("current")
_MwLicenseTemplateTableIndex_Type = Integer32
_MwLicenseTemplateTableIndex_Object = MibTableColumn
mwLicenseTemplateTableIndex = _MwLicenseTemplateTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 1),
    _MwLicenseTemplateTableIndex_Type()
)
mwLicenseTemplateTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwLicenseTemplateTableIndex.setStatus("current")
_MwLicenseTemplateExpiryDate_Type = DateAndTime
_MwLicenseTemplateExpiryDate_Object = MibTableColumn
mwLicenseTemplateExpiryDate = _MwLicenseTemplateExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 2),
    _MwLicenseTemplateExpiryDate_Type()
)
mwLicenseTemplateExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateExpiryDate.setStatus("current")
_MwLicenseTemplateFeatureName_Type = DisplayString
_MwLicenseTemplateFeatureName_Object = MibTableColumn
mwLicenseTemplateFeatureName = _MwLicenseTemplateFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 3),
    _MwLicenseTemplateFeatureName_Type()
)
mwLicenseTemplateFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateFeatureName.setStatus("current")
_MwLicenseTemplateLicenseType_Type = MwlLicenseType
_MwLicenseTemplateLicenseType_Object = MibTableColumn
mwLicenseTemplateLicenseType = _MwLicenseTemplateLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 4),
    _MwLicenseTemplateLicenseType_Type()
)
mwLicenseTemplateLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateLicenseType.setStatus("current")
_MwLicenseTemplateNumOfLicenses_Type = Unsigned32
_MwLicenseTemplateNumOfLicenses_Object = MibTableColumn
mwLicenseTemplateNumOfLicenses = _MwLicenseTemplateNumOfLicenses_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 5),
    _MwLicenseTemplateNumOfLicenses_Type()
)
mwLicenseTemplateNumOfLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateNumOfLicenses.setStatus("current")
_MwLicenseTemplateControllerType_Type = MwlSofwControllerType
_MwLicenseTemplateControllerType_Object = MibTableColumn
mwLicenseTemplateControllerType = _MwLicenseTemplateControllerType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 6),
    _MwLicenseTemplateControllerType_Type()
)
mwLicenseTemplateControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateControllerType.setStatus("current")
_MwLicenseTemplateLicensesInUsed_Type = Unsigned32
_MwLicenseTemplateLicensesInUsed_Object = MibTableColumn
mwLicenseTemplateLicensesInUsed = _MwLicenseTemplateLicensesInUsed_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 11, 1, 1, 7),
    _MwLicenseTemplateLicensesInUsed_Type()
)
mwLicenseTemplateLicensesInUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLicenseTemplateLicensesInUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-LICENSE-MIB",
    **{"mwConfigLicense": mwConfigLicense,
       "mwLicenseTemplateTable": mwLicenseTemplateTable,
       "mwLicenseTemplateEntry": mwLicenseTemplateEntry,
       "mwLicenseTemplateTableIndex": mwLicenseTemplateTableIndex,
       "mwLicenseTemplateExpiryDate": mwLicenseTemplateExpiryDate,
       "mwLicenseTemplateFeatureName": mwLicenseTemplateFeatureName,
       "mwLicenseTemplateLicenseType": mwLicenseTemplateLicenseType,
       "mwLicenseTemplateNumOfLicenses": mwLicenseTemplateNumOfLicenses,
       "mwLicenseTemplateControllerType": mwLicenseTemplateControllerType,
       "mwLicenseTemplateLicensesInUsed": mwLicenseTemplateLicensesInUsed}
)
