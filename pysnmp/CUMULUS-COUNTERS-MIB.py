# SNMP MIB module (CUMULUS-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CUMULUS-COUNTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:59 2024
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

(DateAndTime,
 DisplayString,
 cumulusMib) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "DateAndTime",
    "DisplayString",
    "cumulusMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysSpecificCounters_ObjectIdentity = ObjectIdentity
sysSpecificCounters = _SysSpecificCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 2)
)
_DiscardCounters_ObjectIdentity = ObjectIdentity
discardCounters = _DiscardCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1)
)
_DiscardCountersTable_Object = MibTable
discardCountersTable = _DiscardCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1)
)
if mibBuilder.loadTexts:
    discardCountersTable.setStatus("current")
_DiscardCountersEntry_Object = MibTableRow
discardCountersEntry = _DiscardCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1)
)
discardCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    discardCountersEntry.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 1),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _L3v4InDiscards_Type(Counter32):
    """Custom type l3v4InDiscards based on Counter32"""
    defaultValue = 0


_L3v4InDiscards_Object = MibTableColumn
l3v4InDiscards = _L3v4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 2),
    _L3v4InDiscards_Type()
)
l3v4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3v4InDiscards.setStatus("current")


class _BufferOverflowDiscards_Type(Counter32):
    """Custom type bufferOverflowDiscards based on Counter32"""
    defaultValue = 0


_BufferOverflowDiscards_Object = MibTableColumn
bufferOverflowDiscards = _BufferOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 3),
    _BufferOverflowDiscards_Type()
)
bufferOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferOverflowDiscards.setStatus("current")


class _L3AclDiscards_Type(Counter32):
    """Custom type l3AclDiscards based on Counter32"""
    defaultValue = 0


_L3AclDiscards_Object = MibTableColumn
l3AclDiscards = _L3AclDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 4),
    _L3AclDiscards_Type()
)
l3AclDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3AclDiscards.setStatus("current")


class _EgressQOverflowDiscards_Type(Counter32):
    """Custom type egressQOverflowDiscards based on Counter32"""
    defaultValue = 0


_EgressQOverflowDiscards_Object = MibTableColumn
egressQOverflowDiscards = _EgressQOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 6),
    _EgressQOverflowDiscards_Type()
)
egressQOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressQOverflowDiscards.setStatus("current")


class _EgressNonQDiscards_Type(Counter32):
    """Custom type egressNonQDiscards based on Counter32"""
    defaultValue = 0


_EgressNonQDiscards_Object = MibTableColumn
egressNonQDiscards = _EgressNonQDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 7),
    _EgressNonQDiscards_Type()
)
egressNonQDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressNonQDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-COUNTERS-MIB",
    **{"sysSpecificCounters": sysSpecificCounters,
       "discardCounters": discardCounters,
       "discardCountersTable": discardCountersTable,
       "discardCountersEntry": discardCountersEntry,
       "portName": portName,
       "l3v4InDiscards": l3v4InDiscards,
       "bufferOverflowDiscards": bufferOverflowDiscards,
       "l3AclDiscards": l3AclDiscards,
       "egressQOverflowDiscards": egressQOverflowDiscards,
       "egressNonQDiscards": egressNonQDiscards}
)
