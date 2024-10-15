# SNMP MIB module (HP-ICF-L3MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-L3MAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:41 2024
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

(ifRcvAddressEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifRcvAddressEntry")

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

hpicfL3MacConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36)
)
hpicfL3MacConfigMIB.setRevisions(
        ("2008-10-01 00:00",
         "2006-08-08 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfL3MacConfigObjects_ObjectIdentity = ObjectIdentity
hpicfL3MacConfigObjects = _HpicfL3MacConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1)
)
_HpicfL3MacConfigIfTable_Object = MibTable
hpicfL3MacConfigIfTable = _HpicfL3MacConfigIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfL3MacConfigIfTable.setStatus("current")
_HpicfL3MacConfigIfEntry_Object = MibTableRow
hpicfL3MacConfigIfEntry = _HpicfL3MacConfigIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfL3MacConfigIfEntry.setStatus("current")


class _HpicfL3MacConfigIfAdvTimer_Type(Integer32):
    """Custom type hpicfL3MacConfigIfAdvTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfL3MacConfigIfAdvTimer_Type.__name__ = "Integer32"
_HpicfL3MacConfigIfAdvTimer_Object = MibTableColumn
hpicfL3MacConfigIfAdvTimer = _HpicfL3MacConfigIfAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1, 1),
    _HpicfL3MacConfigIfAdvTimer_Type()
)
hpicfL3MacConfigIfAdvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfL3MacConfigIfAdvTimer.setStatus("current")
_HpicfL3MacConfigConformance_ObjectIdentity = ObjectIdentity
hpicfL3MacConfigConformance = _HpicfL3MacConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2)
)
_HpicfL3MacConfigMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfL3MacConfigMIBCompliances = _HpicfL3MacConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1)
)
_HpicfL3MacConfigMIBGroups_ObjectIdentity = ObjectIdentity
hpicfL3MacConfigMIBGroups = _HpicfL3MacConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2)
)
ifRcvAddressEntry.registerAugmentions(
    ("HP-ICF-L3MAC-MIB",
     "hpicfL3MacConfigIfEntry")
)
hpicfL3MacConfigIfEntry.setIndexNames(*ifRcvAddressEntry.getIndexNames())

# Managed Objects groups

hpicfL3MacConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2, 1)
)
hpicfL3MacConfigGroup.setObjects(
    ("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfAdvTimer")
)
if mibBuilder.loadTexts:
    hpicfL3MacConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfL3MacConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfL3MacConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-L3MAC-MIB",
    **{"hpicfL3MacConfigMIB": hpicfL3MacConfigMIB,
       "hpicfL3MacConfigObjects": hpicfL3MacConfigObjects,
       "hpicfL3MacConfigIfTable": hpicfL3MacConfigIfTable,
       "hpicfL3MacConfigIfEntry": hpicfL3MacConfigIfEntry,
       "hpicfL3MacConfigIfAdvTimer": hpicfL3MacConfigIfAdvTimer,
       "hpicfL3MacConfigConformance": hpicfL3MacConfigConformance,
       "hpicfL3MacConfigMIBCompliances": hpicfL3MacConfigMIBCompliances,
       "hpicfL3MacConfigMIBCompliance": hpicfL3MacConfigMIBCompliance,
       "hpicfL3MacConfigMIBGroups": hpicfL3MacConfigMIBGroups,
       "hpicfL3MacConfigGroup": hpicfL3MacConfigGroup}
)
