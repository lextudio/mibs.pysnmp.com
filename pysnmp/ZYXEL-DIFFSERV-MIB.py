# SNMP MIB module (ZYXEL-DIFFSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DIFFSERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:37 2024
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

zyxelDiffserv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDiffservSetup_ObjectIdentity = ObjectIdentity
zyxelDiffservSetup = _ZyxelDiffservSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1)
)
_ZyDiffservState_Type = EnabledStatus
_ZyDiffservState_Object = MibScalar
zyDiffservState = _ZyDiffservState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 1),
    _ZyDiffservState_Type()
)
zyDiffservState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDiffservState.setStatus("current")
_ZyxelDiffservMapTable_Object = MibTable
zyxelDiffservMapTable = _ZyxelDiffservMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDiffservMapTable.setStatus("current")
_ZyxelDiffservMapEntry_Object = MibTableRow
zyxelDiffservMapEntry = _ZyxelDiffservMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1)
)
zyxelDiffservMapEntry.setIndexNames(
    (0, "ZYXEL-DIFFSERV-MIB", "zyDiffservMapDscp"),
)
if mibBuilder.loadTexts:
    zyxelDiffservMapEntry.setStatus("current")
_ZyDiffservMapDscp_Type = Integer32
_ZyDiffservMapDscp_Object = MibTableColumn
zyDiffservMapDscp = _ZyDiffservMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1, 1),
    _ZyDiffservMapDscp_Type()
)
zyDiffservMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDiffservMapDscp.setStatus("current")
_ZyDiffservMapPriority_Type = Integer32
_ZyDiffservMapPriority_Object = MibTableColumn
zyDiffservMapPriority = _ZyDiffservMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1, 2),
    _ZyDiffservMapPriority_Type()
)
zyDiffservMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDiffservMapPriority.setStatus("current")
_ZyxelDiffservPortTable_Object = MibTable
zyxelDiffservPortTable = _ZyxelDiffservPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelDiffservPortTable.setStatus("current")
_ZyxelDiffservPortEntry_Object = MibTableRow
zyxelDiffservPortEntry = _ZyxelDiffservPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3, 1)
)
zyxelDiffservPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDiffservPortEntry.setStatus("current")
_ZyDiffservPortState_Type = EnabledStatus
_ZyDiffservPortState_Object = MibTableColumn
zyDiffservPortState = _ZyDiffservPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3, 1, 1),
    _ZyDiffservPortState_Type()
)
zyDiffservPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDiffservPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DIFFSERV-MIB",
    **{"zyxelDiffserv": zyxelDiffserv,
       "zyxelDiffservSetup": zyxelDiffservSetup,
       "zyDiffservState": zyDiffservState,
       "zyxelDiffservMapTable": zyxelDiffservMapTable,
       "zyxelDiffservMapEntry": zyxelDiffservMapEntry,
       "zyDiffservMapDscp": zyDiffservMapDscp,
       "zyDiffservMapPriority": zyDiffservMapPriority,
       "zyxelDiffservPortTable": zyxelDiffservPortTable,
       "zyxelDiffservPortEntry": zyxelDiffservPortEntry,
       "zyDiffservPortState": zyDiffservPortState}
)
