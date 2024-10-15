# SNMP MIB module (Nortel-Magellan-Passport-ExtensionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ExtensionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:41 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(RowPointer,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "RowPointer")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Extensions_ObjectIdentity = ObjectIdentity
extensions = _Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 4)
)
_ExtensionIfTable_Object = MibTable
extensionIfTable = _ExtensionIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    extensionIfTable.setStatus("mandatory")
_ExtensionIfEntry_Object = MibTableRow
extensionIfEntry = _ExtensionIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 4, 1, 1)
)
extensionIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extensionIfEntry.setStatus("mandatory")
_IfRowPointer_Type = RowPointer
_IfRowPointer_Object = MibTableColumn
ifRowPointer = _IfRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 4, 1, 1, 1),
    _IfRowPointer_Type()
)
ifRowPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRowPointer.setStatus("mandatory")
_ExtensionsMIB_ObjectIdentity = ObjectIdentity
extensionsMIB = _ExtensionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5)
)
_ExtensionsGroup_ObjectIdentity = ObjectIdentity
extensionsGroup = _ExtensionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 1)
)
_ExtensionsGroupBC_ObjectIdentity = ObjectIdentity
extensionsGroupBC = _ExtensionsGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 1, 3)
)
_ExtensionsGroupBC02_ObjectIdentity = ObjectIdentity
extensionsGroupBC02 = _ExtensionsGroupBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 1, 3, 2)
)
_ExtensionsGroupBC02A_ObjectIdentity = ObjectIdentity
extensionsGroupBC02A = _ExtensionsGroupBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 1, 3, 2, 2)
)
_ExtensionsCapabilities_ObjectIdentity = ObjectIdentity
extensionsCapabilities = _ExtensionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 3)
)
_ExtensionsCapabilitiesBC_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesBC = _ExtensionsCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 3, 3)
)
_ExtensionsCapabilitiesBC02_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesBC02 = _ExtensionsCapabilitiesBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 3, 3, 2)
)
_ExtensionsCapabilitiesBC02A_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesBC02A = _ExtensionsCapabilitiesBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 5, 3, 3, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ExtensionsMIB",
    **{"extensions": extensions,
       "extensionIfTable": extensionIfTable,
       "extensionIfEntry": extensionIfEntry,
       "ifRowPointer": ifRowPointer,
       "extensionsMIB": extensionsMIB,
       "extensionsGroup": extensionsGroup,
       "extensionsGroupBC": extensionsGroupBC,
       "extensionsGroupBC02": extensionsGroupBC02,
       "extensionsGroupBC02A": extensionsGroupBC02A,
       "extensionsCapabilities": extensionsCapabilities,
       "extensionsCapabilitiesBC": extensionsCapabilitiesBC,
       "extensionsCapabilitiesBC02": extensionsCapabilitiesBC02,
       "extensionsCapabilitiesBC02A": extensionsCapabilitiesBC02A}
)
