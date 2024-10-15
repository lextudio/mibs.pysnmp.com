# SNMP MIB module (OPENBSD-MEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-MEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:18 2024
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

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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

memMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 5)
)
memMIBObjects.setRevisions(
        ("2012-02-09 00:00",
         "2008-12-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MemMIBVersion_Type = Integer32
_MemMIBVersion_Object = MibScalar
memMIBVersion = _MemMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 30155, 5, 1),
    _MemMIBVersion_Type()
)
memMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMIBVersion.setStatus("current")
_MemIfTable_Object = MibTable
memIfTable = _MemIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 5, 2)
)
if mibBuilder.loadTexts:
    memIfTable.setStatus("current")
_MemIfEntry_Object = MibTableRow
memIfEntry = _MemIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 5, 2, 1)
)
memIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    memIfEntry.setStatus("current")
_MemIfName_Type = DisplayString
_MemIfName_Object = MibTableColumn
memIfName = _MemIfName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 1),
    _MemIfName_Type()
)
memIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIfName.setStatus("current")
_MemIfLiveLocks_Type = Counter64
_MemIfLiveLocks_Object = MibTableColumn
memIfLiveLocks = _MemIfLiveLocks_Object(
    (1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 2),
    _MemIfLiveLocks_Type()
)
memIfLiveLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIfLiveLocks.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-MEM-MIB",
    **{"memMIBObjects": memMIBObjects,
       "memMIBVersion": memMIBVersion,
       "memIfTable": memIfTable,
       "memIfEntry": memIfEntry,
       "memIfName": memIfName,
       "memIfLiveLocks": memIfLiveLocks}
)
