# SNMP MIB module (LIGO-W-JET-MIMO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-W-JET-MIMO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:13 2024
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

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ligoWJetMimoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9)
)
ligoWJetMimoMIB.setRevisions(
        ("2010-03-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoWJetMimoMIBObjects_ObjectIdentity = ObjectIdentity
ligoWJetMimoMIBObjects = _LigoWJetMimoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1)
)
_LigoWJetMimoNotifs_ObjectIdentity = ObjectIdentity
ligoWJetMimoNotifs = _LigoWJetMimoNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 0)
)
_LigoWJetMimoInfo_ObjectIdentity = ObjectIdentity
ligoWJetMimoInfo = _LigoWJetMimoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 1)
)
_LigoWJetMimoConf_ObjectIdentity = ObjectIdentity
ligoWJetMimoConf = _LigoWJetMimoConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 2)
)
_LigoWJetMimoStats_ObjectIdentity = ObjectIdentity
ligoWJetMimoStats = _LigoWJetMimoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3)
)
_WJetMimoStatsTable_Object = MibTable
wJetMimoStatsTable = _WJetMimoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wJetMimoStatsTable.setStatus("current")
_WJetMimoStatsEntry_Object = MibTableRow
wJetMimoStatsEntry = _WJetMimoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1)
)
wJetMimoStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LIGO-W-JET-MIMO-MIB", "wJetMimoPeerIndex"),
)
if mibBuilder.loadTexts:
    wJetMimoStatsEntry.setStatus("current")
_WJetMimoPeerIndex_Type = Integer32
_WJetMimoPeerIndex_Object = MibTableColumn
wJetMimoPeerIndex = _WJetMimoPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 1),
    _WJetMimoPeerIndex_Type()
)
wJetMimoPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wJetMimoPeerIndex.setStatus("current")
_WJetMimoMacAddress_Type = MacAddress
_WJetMimoMacAddress_Object = MibTableColumn
wJetMimoMacAddress = _WJetMimoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 2),
    _WJetMimoMacAddress_Type()
)
wJetMimoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoMacAddress.setStatus("current")
_WJetMimoTxTokens_Type = Counter32
_WJetMimoTxTokens_Object = MibTableColumn
wJetMimoTxTokens = _WJetMimoTxTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 3),
    _WJetMimoTxTokens_Type()
)
wJetMimoTxTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoTxTokens.setStatus("current")
_WJetMimoRxTokens_Type = Counter32
_WJetMimoRxTokens_Object = MibTableColumn
wJetMimoRxTokens = _WJetMimoRxTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 4),
    _WJetMimoRxTokens_Type()
)
wJetMimoRxTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoRxTokens.setStatus("current")
_WJetMimoDupTokens_Type = Counter32
_WJetMimoDupTokens_Object = MibTableColumn
wJetMimoDupTokens = _WJetMimoDupTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 5),
    _WJetMimoDupTokens_Type()
)
wJetMimoDupTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoDupTokens.setStatus("current")
_WJetMimoLostTokens_Type = Counter32
_WJetMimoLostTokens_Object = MibTableColumn
wJetMimoLostTokens = _WJetMimoLostTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 6),
    _WJetMimoLostTokens_Type()
)
wJetMimoLostTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoLostTokens.setStatus("current")
_WJetMimoDroppedTokens_Type = Counter32
_WJetMimoDroppedTokens_Object = MibTableColumn
wJetMimoDroppedTokens = _WJetMimoDroppedTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 7),
    _WJetMimoDroppedTokens_Type()
)
wJetMimoDroppedTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoDroppedTokens.setStatus("current")
_WJetMimoTxFailures_Type = Counter32
_WJetMimoTxFailures_Object = MibTableColumn
wJetMimoTxFailures = _WJetMimoTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 8),
    _WJetMimoTxFailures_Type()
)
wJetMimoTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoTxFailures.setStatus("current")
_WJetMimoReinjectedTokens_Type = Counter32
_WJetMimoReinjectedTokens_Object = MibTableColumn
wJetMimoReinjectedTokens = _WJetMimoReinjectedTokens_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 9),
    _WJetMimoReinjectedTokens_Type()
)
wJetMimoReinjectedTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetMimoReinjectedTokens.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-W-JET-MIMO-MIB",
    **{"ligoWJetMimoMIB": ligoWJetMimoMIB,
       "ligoWJetMimoMIBObjects": ligoWJetMimoMIBObjects,
       "ligoWJetMimoNotifs": ligoWJetMimoNotifs,
       "ligoWJetMimoInfo": ligoWJetMimoInfo,
       "ligoWJetMimoConf": ligoWJetMimoConf,
       "ligoWJetMimoStats": ligoWJetMimoStats,
       "wJetMimoStatsTable": wJetMimoStatsTable,
       "wJetMimoStatsEntry": wJetMimoStatsEntry,
       "wJetMimoPeerIndex": wJetMimoPeerIndex,
       "wJetMimoMacAddress": wJetMimoMacAddress,
       "wJetMimoTxTokens": wJetMimoTxTokens,
       "wJetMimoRxTokens": wJetMimoRxTokens,
       "wJetMimoDupTokens": wJetMimoDupTokens,
       "wJetMimoLostTokens": wJetMimoLostTokens,
       "wJetMimoDroppedTokens": wJetMimoDroppedTokens,
       "wJetMimoTxFailures": wJetMimoTxFailures,
       "wJetMimoReinjectedTokens": wJetMimoReinjectedTokens}
)
