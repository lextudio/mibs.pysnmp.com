# SNMP MIB module (HP-ICF-DOS-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DOS-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:23 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpicfDosFilterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60)
)
hpicfDosFilterMib.setRevisions(
        ("2009-04-03 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDosFilterObjects_ObjectIdentity = ObjectIdentity
hpicfDosFilterObjects = _HpicfDosFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1)
)


class _HpicfDosFilterConfig_Type(Integer32):
    """Custom type hpicfDosFilterConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDosFilterConfig_Type.__name__ = "Integer32"
_HpicfDosFilterConfig_Object = MibScalar
hpicfDosFilterConfig = _HpicfDosFilterConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1, 1),
    _HpicfDosFilterConfig_Type()
)
hpicfDosFilterConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDosFilterConfig.setStatus("current")
_HpicfDosFilterConformance_ObjectIdentity = ObjectIdentity
hpicfDosFilterConformance = _HpicfDosFilterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2)
)
_HpicfDosFilterCompliances_ObjectIdentity = ObjectIdentity
hpicfDosFilterCompliances = _HpicfDosFilterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1)
)
_HpicfDosFilterGroups_ObjectIdentity = ObjectIdentity
hpicfDosFilterGroups = _HpicfDosFilterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2)
)

# Managed Objects groups

hpicfDosFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2, 1)
)
hpicfDosFilterGroup.setObjects(
    ("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterConfig")
)
if mibBuilder.loadTexts:
    hpicfDosFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDosFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDosFilterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DOS-FILTER-MIB",
    **{"hpicfDosFilterMib": hpicfDosFilterMib,
       "hpicfDosFilterObjects": hpicfDosFilterObjects,
       "hpicfDosFilterConfig": hpicfDosFilterConfig,
       "hpicfDosFilterConformance": hpicfDosFilterConformance,
       "hpicfDosFilterCompliances": hpicfDosFilterCompliances,
       "hpicfDosFilterCompliance": hpicfDosFilterCompliance,
       "hpicfDosFilterGroups": hpicfDosFilterGroups,
       "hpicfDosFilterGroup": hpicfDosFilterGroup}
)
