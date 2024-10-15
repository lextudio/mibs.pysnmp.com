# SNMP MIB module (RUCKUS-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:39 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusCommonEthModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonEthModule")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusEthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusEthObjects_ObjectIdentity = ObjectIdentity
ruckusEthObjects = _RuckusEthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1)
)
_RuckusEthInfo_ObjectIdentity = ObjectIdentity
ruckusEthInfo = _RuckusEthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1)
)
_RuckusEthStatsTable_Object = MibTable
ruckusEthStatsTable = _RuckusEthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusEthStatsTable.setStatus("current")
_RuckusEthStatsEntry_Object = MibTableRow
ruckusEthStatsEntry = _RuckusEthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1)
)
ruckusEthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusEthStatsEntry.setStatus("current")
_RuckusEthName_Type = DisplayString
_RuckusEthName_Object = MibTableColumn
ruckusEthName = _RuckusEthName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 1),
    _RuckusEthName_Type()
)
ruckusEthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusEthName.setStatus("current")
_RuckusEthStatsRxRate_Type = Counter32
_RuckusEthStatsRxRate_Object = MibTableColumn
ruckusEthStatsRxRate = _RuckusEthStatsRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 2),
    _RuckusEthStatsRxRate_Type()
)
ruckusEthStatsRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusEthStatsRxRate.setStatus("current")
_RuckusEthStatsRxErrorRate_Type = Counter32
_RuckusEthStatsRxErrorRate_Object = MibTableColumn
ruckusEthStatsRxErrorRate = _RuckusEthStatsRxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 3),
    _RuckusEthStatsRxErrorRate_Type()
)
ruckusEthStatsRxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusEthStatsRxErrorRate.setStatus("current")
_RuckusEthStatsTxRate_Type = Counter32
_RuckusEthStatsTxRate_Object = MibTableColumn
ruckusEthStatsTxRate = _RuckusEthStatsTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 4),
    _RuckusEthStatsTxRate_Type()
)
ruckusEthStatsTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusEthStatsTxRate.setStatus("current")
_RuckusEthStatsTxErrorRate_Type = Counter32
_RuckusEthStatsTxErrorRate_Object = MibTableColumn
ruckusEthStatsTxErrorRate = _RuckusEthStatsTxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 5),
    _RuckusEthStatsTxErrorRate_Type()
)
ruckusEthStatsTxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusEthStatsTxErrorRate.setStatus("current")
_RuckusEthEvents_ObjectIdentity = ObjectIdentity
ruckusEthEvents = _RuckusEthEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ETH-MIB",
    **{"ruckusEthMIB": ruckusEthMIB,
       "ruckusEthObjects": ruckusEthObjects,
       "ruckusEthInfo": ruckusEthInfo,
       "ruckusEthStatsTable": ruckusEthStatsTable,
       "ruckusEthStatsEntry": ruckusEthStatsEntry,
       "ruckusEthName": ruckusEthName,
       "ruckusEthStatsRxRate": ruckusEthStatsRxRate,
       "ruckusEthStatsRxErrorRate": ruckusEthStatsRxErrorRate,
       "ruckusEthStatsTxRate": ruckusEthStatsTxRate,
       "ruckusEthStatsTxErrorRate": ruckusEthStatsTxErrorRate,
       "ruckusEthEvents": ruckusEthEvents}
)
