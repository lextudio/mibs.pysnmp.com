# SNMP MIB module (HPICF-ACTIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-ACTIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:16 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfActivateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129)
)
hpicfActivateMIB.setRevisions(
        ("2016-05-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfActivateObjects_ObjectIdentity = ObjectIdentity
hpicfActivateObjects = _HpicfActivateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1)
)


class _HpicfActivateSoftwareUpdateMode_Type(TruthValue):
    """Custom type hpicfActivateSoftwareUpdateMode based on TruthValue"""


_HpicfActivateSoftwareUpdateMode_Object = MibScalar
hpicfActivateSoftwareUpdateMode = _HpicfActivateSoftwareUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 1),
    _HpicfActivateSoftwareUpdateMode_Type()
)
hpicfActivateSoftwareUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfActivateSoftwareUpdateMode.setStatus("current")


class _HpicfActivateProvisionMode_Type(TruthValue):
    """Custom type hpicfActivateProvisionMode based on TruthValue"""


_HpicfActivateProvisionMode_Object = MibScalar
hpicfActivateProvisionMode = _HpicfActivateProvisionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 2),
    _HpicfActivateProvisionMode_Type()
)
hpicfActivateProvisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfActivateProvisionMode.setStatus("current")
_HpicfActivateConformance_ObjectIdentity = ObjectIdentity
hpicfActivateConformance = _HpicfActivateConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2)
)
_HpicfActivateMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfActivateMIBCompliances = _HpicfActivateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1)
)
_HpicfActivateMIBGroups_ObjectIdentity = ObjectIdentity
hpicfActivateMIBGroups = _HpicfActivateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2)
)

# Managed Objects groups

hpicfActivateConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 1)
)
hpicfActivateConfigGroup.setObjects(
      *(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"),
        ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"))
)
if mibBuilder.loadTexts:
    hpicfActivateConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfActivateMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfActivateMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-ACTIVATE-MIB",
    **{"hpicfActivateMIB": hpicfActivateMIB,
       "hpicfActivateObjects": hpicfActivateObjects,
       "hpicfActivateSoftwareUpdateMode": hpicfActivateSoftwareUpdateMode,
       "hpicfActivateProvisionMode": hpicfActivateProvisionMode,
       "hpicfActivateConformance": hpicfActivateConformance,
       "hpicfActivateMIBCompliances": hpicfActivateMIBCompliances,
       "hpicfActivateMIBCompliance": hpicfActivateMIBCompliance,
       "hpicfActivateMIBGroups": hpicfActivateMIBGroups,
       "hpicfActivateConfigGroup": hpicfActivateConfigGroup}
)
