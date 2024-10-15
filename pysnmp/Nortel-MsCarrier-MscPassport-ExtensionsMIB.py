# SNMP MIB module (Nortel-MsCarrier-MscPassport-ExtensionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ExtensionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:18 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "RowPointer")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscExtensions_ObjectIdentity = ObjectIdentity
mscExtensions = _MscExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 4)
)
_MscExtensionIfTable_Object = MibTable
mscExtensionIfTable = _MscExtensionIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mscExtensionIfTable.setStatus("mandatory")
_MscExtensionIfEntry_Object = MibTableRow
mscExtensionIfEntry = _MscExtensionIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 4, 1, 1)
)
mscExtensionIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mscExtensionIfEntry.setStatus("mandatory")
_MscIfRowPointer_Type = RowPointer
_MscIfRowPointer_Object = MibTableColumn
mscIfRowPointer = _MscIfRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 4, 1, 1, 1),
    _MscIfRowPointer_Type()
)
mscIfRowPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIfRowPointer.setStatus("mandatory")
_ExtensionsMIB_ObjectIdentity = ObjectIdentity
extensionsMIB = _ExtensionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5)
)
_ExtensionsGroup_ObjectIdentity = ObjectIdentity
extensionsGroup = _ExtensionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 1)
)
_ExtensionsGroupCA_ObjectIdentity = ObjectIdentity
extensionsGroupCA = _ExtensionsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 1, 1)
)
_ExtensionsGroupCA01_ObjectIdentity = ObjectIdentity
extensionsGroupCA01 = _ExtensionsGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 1, 1, 2)
)
_ExtensionsGroupCA01A_ObjectIdentity = ObjectIdentity
extensionsGroupCA01A = _ExtensionsGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 1, 1, 2, 2)
)
_ExtensionsCapabilities_ObjectIdentity = ObjectIdentity
extensionsCapabilities = _ExtensionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 3)
)
_ExtensionsCapabilitiesCA_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesCA = _ExtensionsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 3, 1)
)
_ExtensionsCapabilitiesCA01_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesCA01 = _ExtensionsCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 3, 1, 2)
)
_ExtensionsCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
extensionsCapabilitiesCA01A = _ExtensionsCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 5, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ExtensionsMIB",
    **{"mscExtensions": mscExtensions,
       "mscExtensionIfTable": mscExtensionIfTable,
       "mscExtensionIfEntry": mscExtensionIfEntry,
       "mscIfRowPointer": mscIfRowPointer,
       "extensionsMIB": extensionsMIB,
       "extensionsGroup": extensionsGroup,
       "extensionsGroupCA": extensionsGroupCA,
       "extensionsGroupCA01": extensionsGroupCA01,
       "extensionsGroupCA01A": extensionsGroupCA01A,
       "extensionsCapabilities": extensionsCapabilities,
       "extensionsCapabilitiesCA": extensionsCapabilitiesCA,
       "extensionsCapabilitiesCA01": extensionsCapabilitiesCA01,
       "extensionsCapabilitiesCA01A": extensionsCapabilitiesCA01A}
)
