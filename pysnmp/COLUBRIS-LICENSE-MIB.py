# SNMP MIB module (COLUBRIS-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:19 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisLicenseMIBObjects_ObjectIdentity = ObjectIdentity
colubrisLicenseMIBObjects = _ColubrisLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1)
)
_CoLicenseGroup_ObjectIdentity = ObjectIdentity
coLicenseGroup = _CoLicenseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1)
)
_CoLicenseFeatureTable_Object = MibTable
coLicenseFeatureTable = _CoLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coLicenseFeatureTable.setStatus("current")
_CoLicenseFeatureEntry_Object = MibTableRow
coLicenseFeatureEntry = _CoLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1)
)
coLicenseFeatureEntry.setIndexNames(
    (0, "COLUBRIS-LICENSE-MIB", "coLicenseFeatureIndex"),
)
if mibBuilder.loadTexts:
    coLicenseFeatureEntry.setStatus("current")


class _CoLicenseFeatureIndex_Type(Integer32):
    """Custom type coLicenseFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoLicenseFeatureIndex_Type.__name__ = "Integer32"
_CoLicenseFeatureIndex_Object = MibTableColumn
coLicenseFeatureIndex = _CoLicenseFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 1),
    _CoLicenseFeatureIndex_Type()
)
coLicenseFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coLicenseFeatureIndex.setStatus("current")
_CoLicenseFeatureName_Type = DisplayString
_CoLicenseFeatureName_Object = MibTableColumn
coLicenseFeatureName = _CoLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 2),
    _CoLicenseFeatureName_Type()
)
coLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coLicenseFeatureName.setStatus("current")


class _CoLicenseFeatureState_Type(Integer32):
    """Custom type coLicenseFeatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CoLicenseFeatureState_Type.__name__ = "Integer32"
_CoLicenseFeatureState_Object = MibTableColumn
coLicenseFeatureState = _CoLicenseFeatureState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 3),
    _CoLicenseFeatureState_Type()
)
coLicenseFeatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coLicenseFeatureState.setStatus("current")


class _CoLicenseFeatureEndingDate_Type(OctetString):
    """Custom type coLicenseFeatureEndingDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_CoLicenseFeatureEndingDate_Type.__name__ = "OctetString"
_CoLicenseFeatureEndingDate_Object = MibTableColumn
coLicenseFeatureEndingDate = _CoLicenseFeatureEndingDate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 4),
    _CoLicenseFeatureEndingDate_Type()
)
coLicenseFeatureEndingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coLicenseFeatureEndingDate.setStatus("current")


class _CoLicenseFeatureRemainingDays_Type(Integer32):
    """Custom type coLicenseFeatureRemainingDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CoLicenseFeatureRemainingDays_Type.__name__ = "Integer32"
_CoLicenseFeatureRemainingDays_Object = MibTableColumn
coLicenseFeatureRemainingDays = _CoLicenseFeatureRemainingDays_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 5),
    _CoLicenseFeatureRemainingDays_Type()
)
coLicenseFeatureRemainingDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coLicenseFeatureRemainingDays.setStatus("current")
_ColubrisLicenseMIBConformance_ObjectIdentity = ObjectIdentity
colubrisLicenseMIBConformance = _ColubrisLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 2)
)
_ColubrisLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisLicenseMIBCompliances = _ColubrisLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1)
)
_ColubrisLicenseMIBGroups_ObjectIdentity = ObjectIdentity
colubrisLicenseMIBGroups = _ColubrisLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2)
)

# Managed Objects groups

colubrisLicenseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2, 1)
)
colubrisLicenseMIBGroup.setObjects(
      *(("COLUBRIS-LICENSE-MIB", "coLicenseFeatureName"),
        ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureState"),
        ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureEndingDate"),
        ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureRemainingDays"))
)
if mibBuilder.loadTexts:
    colubrisLicenseMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisLicenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisLicenseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-LICENSE-MIB",
    **{"colubrisLicenseMIB": colubrisLicenseMIB,
       "colubrisLicenseMIBObjects": colubrisLicenseMIBObjects,
       "coLicenseGroup": coLicenseGroup,
       "coLicenseFeatureTable": coLicenseFeatureTable,
       "coLicenseFeatureEntry": coLicenseFeatureEntry,
       "coLicenseFeatureIndex": coLicenseFeatureIndex,
       "coLicenseFeatureName": coLicenseFeatureName,
       "coLicenseFeatureState": coLicenseFeatureState,
       "coLicenseFeatureEndingDate": coLicenseFeatureEndingDate,
       "coLicenseFeatureRemainingDays": coLicenseFeatureRemainingDays,
       "colubrisLicenseMIBConformance": colubrisLicenseMIBConformance,
       "colubrisLicenseMIBCompliances": colubrisLicenseMIBCompliances,
       "colubrisLicenseMIBCompliance": colubrisLicenseMIBCompliance,
       "colubrisLicenseMIBGroups": colubrisLicenseMIBGroups,
       "colubrisLicenseMIBGroup": colubrisLicenseMIBGroup}
)
