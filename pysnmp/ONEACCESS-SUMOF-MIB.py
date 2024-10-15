# SNMP MIB module (ONEACCESS-SUMOF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-SUMOF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:05 2024
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

(oacExpIMManagement,) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement")

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

oacSumOfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7)
)
oacSumOfMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacSumOfObjects_ObjectIdentity = ObjectIdentity
oacSumOfObjects = _OacSumOfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1)
)
_OacSumOfIfTable_Object = MibTable
oacSumOfIfTable = _OacSumOfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    oacSumOfIfTable.setStatus("current")
_OacSumOfIfEntry_Object = MibTableRow
oacSumOfIfEntry = _OacSumOfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1)
)
oacSumOfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacSumOfIfEntry.setStatus("current")
_SumOfIfInOctets_Type = Counter32
_SumOfIfInOctets_Object = MibTableColumn
sumOfIfInOctets = _SumOfIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 1),
    _SumOfIfInOctets_Type()
)
sumOfIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInOctets.setStatus("current")
_SumOfIfInUcastPkts_Type = Counter32
_SumOfIfInUcastPkts_Object = MibTableColumn
sumOfIfInUcastPkts = _SumOfIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 2),
    _SumOfIfInUcastPkts_Type()
)
sumOfIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInUcastPkts.setStatus("current")
_SumOfIfInNUcastPkts_Type = Counter32
_SumOfIfInNUcastPkts_Object = MibTableColumn
sumOfIfInNUcastPkts = _SumOfIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 3),
    _SumOfIfInNUcastPkts_Type()
)
sumOfIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInNUcastPkts.setStatus("current")
_SumOfIfInDiscards_Type = Counter32
_SumOfIfInDiscards_Object = MibTableColumn
sumOfIfInDiscards = _SumOfIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 4),
    _SumOfIfInDiscards_Type()
)
sumOfIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInDiscards.setStatus("current")
_SumOfIfInErrors_Type = Counter32
_SumOfIfInErrors_Object = MibTableColumn
sumOfIfInErrors = _SumOfIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 5),
    _SumOfIfInErrors_Type()
)
sumOfIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInErrors.setStatus("current")
_SumOfIfInUnknownProtos_Type = Counter32
_SumOfIfInUnknownProtos_Object = MibTableColumn
sumOfIfInUnknownProtos = _SumOfIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 6),
    _SumOfIfInUnknownProtos_Type()
)
sumOfIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInUnknownProtos.setStatus("current")
_SumOfIfOutOctets_Type = Counter32
_SumOfIfOutOctets_Object = MibTableColumn
sumOfIfOutOctets = _SumOfIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 7),
    _SumOfIfOutOctets_Type()
)
sumOfIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutOctets.setStatus("current")
_SumOfIfOutUcastPkts_Type = Counter32
_SumOfIfOutUcastPkts_Object = MibTableColumn
sumOfIfOutUcastPkts = _SumOfIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 8),
    _SumOfIfOutUcastPkts_Type()
)
sumOfIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutUcastPkts.setStatus("current")
_SumOfIfOutNUcastPkts_Type = Counter32
_SumOfIfOutNUcastPkts_Object = MibTableColumn
sumOfIfOutNUcastPkts = _SumOfIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 9),
    _SumOfIfOutNUcastPkts_Type()
)
sumOfIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutNUcastPkts.setStatus("current")
_SumOfIfOutDiscards_Type = Counter32
_SumOfIfOutDiscards_Object = MibTableColumn
sumOfIfOutDiscards = _SumOfIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 10),
    _SumOfIfOutDiscards_Type()
)
sumOfIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutDiscards.setStatus("current")
_SumOfIfOutErrors_Type = Counter32
_SumOfIfOutErrors_Object = MibTableColumn
sumOfIfOutErrors = _SumOfIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 11),
    _SumOfIfOutErrors_Type()
)
sumOfIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutErrors.setStatus("current")
_OacSumOfIfXTable_Object = MibTable
oacSumOfIfXTable = _OacSumOfIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    oacSumOfIfXTable.setStatus("current")
_OacSumOfIfXEntry_Object = MibTableRow
oacSumOfIfXEntry = _OacSumOfIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1)
)
oacSumOfIfXEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacSumOfIfXEntry.setStatus("current")
_SumOfIfInMulticastPkts_Type = Counter32
_SumOfIfInMulticastPkts_Object = MibTableColumn
sumOfIfInMulticastPkts = _SumOfIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 1),
    _SumOfIfInMulticastPkts_Type()
)
sumOfIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInMulticastPkts.setStatus("current")
_SumOfIfInBroadcastPkts_Type = Counter32
_SumOfIfInBroadcastPkts_Object = MibTableColumn
sumOfIfInBroadcastPkts = _SumOfIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 2),
    _SumOfIfInBroadcastPkts_Type()
)
sumOfIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfInBroadcastPkts.setStatus("current")
_SumOfIfOutMulticastPkts_Type = Counter32
_SumOfIfOutMulticastPkts_Object = MibTableColumn
sumOfIfOutMulticastPkts = _SumOfIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 3),
    _SumOfIfOutMulticastPkts_Type()
)
sumOfIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutMulticastPkts.setStatus("current")
_SumOfIfOutBroadcastPkts_Type = Counter32
_SumOfIfOutBroadcastPkts_Object = MibTableColumn
sumOfIfOutBroadcastPkts = _SumOfIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 4),
    _SumOfIfOutBroadcastPkts_Type()
)
sumOfIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfOutBroadcastPkts.setStatus("current")
_SumOfIfHCInOctets_Type = Counter64
_SumOfIfHCInOctets_Object = MibTableColumn
sumOfIfHCInOctets = _SumOfIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 5),
    _SumOfIfHCInOctets_Type()
)
sumOfIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCInOctets.setStatus("current")
_SumOfIfHCInUcastPkts_Type = Counter64
_SumOfIfHCInUcastPkts_Object = MibTableColumn
sumOfIfHCInUcastPkts = _SumOfIfHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 6),
    _SumOfIfHCInUcastPkts_Type()
)
sumOfIfHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCInUcastPkts.setStatus("current")
_SumOfIfHCInMulticastPkts_Type = Counter64
_SumOfIfHCInMulticastPkts_Object = MibTableColumn
sumOfIfHCInMulticastPkts = _SumOfIfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 7),
    _SumOfIfHCInMulticastPkts_Type()
)
sumOfIfHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCInMulticastPkts.setStatus("current")
_SumOfIfHCInBroadcastPkts_Type = Counter64
_SumOfIfHCInBroadcastPkts_Object = MibTableColumn
sumOfIfHCInBroadcastPkts = _SumOfIfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 8),
    _SumOfIfHCInBroadcastPkts_Type()
)
sumOfIfHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCInBroadcastPkts.setStatus("current")
_SumOfIfHCOutOctets_Type = Counter64
_SumOfIfHCOutOctets_Object = MibTableColumn
sumOfIfHCOutOctets = _SumOfIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 9),
    _SumOfIfHCOutOctets_Type()
)
sumOfIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCOutOctets.setStatus("current")
_SumOfIfHCOutUcastPkts_Type = Counter64
_SumOfIfHCOutUcastPkts_Object = MibTableColumn
sumOfIfHCOutUcastPkts = _SumOfIfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 10),
    _SumOfIfHCOutUcastPkts_Type()
)
sumOfIfHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCOutUcastPkts.setStatus("current")
_SumOfIfHCOutMulticastPkts_Type = Counter64
_SumOfIfHCOutMulticastPkts_Object = MibTableColumn
sumOfIfHCOutMulticastPkts = _SumOfIfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 11),
    _SumOfIfHCOutMulticastPkts_Type()
)
sumOfIfHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCOutMulticastPkts.setStatus("current")
_SumOfIfHCOutBroadcastPkts_Type = Counter64
_SumOfIfHCOutBroadcastPkts_Object = MibTableColumn
sumOfIfHCOutBroadcastPkts = _SumOfIfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 12),
    _SumOfIfHCOutBroadcastPkts_Type()
)
sumOfIfHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfIfHCOutBroadcastPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-SUMOF-MIB",
    **{"oacSumOfMIBModule": oacSumOfMIBModule,
       "oacSumOfObjects": oacSumOfObjects,
       "oacSumOfIfTable": oacSumOfIfTable,
       "oacSumOfIfEntry": oacSumOfIfEntry,
       "sumOfIfInOctets": sumOfIfInOctets,
       "sumOfIfInUcastPkts": sumOfIfInUcastPkts,
       "sumOfIfInNUcastPkts": sumOfIfInNUcastPkts,
       "sumOfIfInDiscards": sumOfIfInDiscards,
       "sumOfIfInErrors": sumOfIfInErrors,
       "sumOfIfInUnknownProtos": sumOfIfInUnknownProtos,
       "sumOfIfOutOctets": sumOfIfOutOctets,
       "sumOfIfOutUcastPkts": sumOfIfOutUcastPkts,
       "sumOfIfOutNUcastPkts": sumOfIfOutNUcastPkts,
       "sumOfIfOutDiscards": sumOfIfOutDiscards,
       "sumOfIfOutErrors": sumOfIfOutErrors,
       "oacSumOfIfXTable": oacSumOfIfXTable,
       "oacSumOfIfXEntry": oacSumOfIfXEntry,
       "sumOfIfInMulticastPkts": sumOfIfInMulticastPkts,
       "sumOfIfInBroadcastPkts": sumOfIfInBroadcastPkts,
       "sumOfIfOutMulticastPkts": sumOfIfOutMulticastPkts,
       "sumOfIfOutBroadcastPkts": sumOfIfOutBroadcastPkts,
       "sumOfIfHCInOctets": sumOfIfHCInOctets,
       "sumOfIfHCInUcastPkts": sumOfIfHCInUcastPkts,
       "sumOfIfHCInMulticastPkts": sumOfIfHCInMulticastPkts,
       "sumOfIfHCInBroadcastPkts": sumOfIfHCInBroadcastPkts,
       "sumOfIfHCOutOctets": sumOfIfHCOutOctets,
       "sumOfIfHCOutUcastPkts": sumOfIfHCOutUcastPkts,
       "sumOfIfHCOutMulticastPkts": sumOfIfHCOutMulticastPkts,
       "sumOfIfHCOutBroadcastPkts": sumOfIfHCOutBroadcastPkts}
)
