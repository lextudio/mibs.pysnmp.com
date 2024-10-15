# SNMP MIB module (ZYXEL-PORT-ISOLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PORT-ISOLATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:34 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPortIsolation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPortIsolationSetup_ObjectIdentity = ObjectIdentity
zyxelPortIsolationSetup = _ZyxelPortIsolationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1)
)
_ZyxelPortIsolationPortTable_Object = MibTable
zyxelPortIsolationPortTable = _ZyxelPortIsolationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelPortIsolationPortTable.setStatus("current")
_ZyxelPortIsolationPortEntry_Object = MibTableRow
zyxelPortIsolationPortEntry = _ZyxelPortIsolationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1)
)
zyxelPortIsolationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortIsolationPortEntry.setStatus("current")
_ZyPortIsolationPortState_Type = EnabledStatus
_ZyPortIsolationPortState_Object = MibTableColumn
zyPortIsolationPortState = _ZyPortIsolationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1, 1),
    _ZyPortIsolationPortState_Type()
)
zyPortIsolationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortIsolationPortState.setStatus("current")
_ZyPortIsolationSmartIsolationState_Type = EnabledStatus
_ZyPortIsolationSmartIsolationState_Object = MibScalar
zyPortIsolationSmartIsolationState = _ZyPortIsolationSmartIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 2),
    _ZyPortIsolationSmartIsolationState_Type()
)
zyPortIsolationSmartIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortIsolationSmartIsolationState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PORT-ISOLATION-MIB",
    **{"zyxelPortIsolation": zyxelPortIsolation,
       "zyxelPortIsolationSetup": zyxelPortIsolationSetup,
       "zyxelPortIsolationPortTable": zyxelPortIsolationPortTable,
       "zyxelPortIsolationPortEntry": zyxelPortIsolationPortEntry,
       "zyPortIsolationPortState": zyPortIsolationPortState,
       "zyPortIsolationSmartIsolationState": zyPortIsolationSmartIsolationState}
)
