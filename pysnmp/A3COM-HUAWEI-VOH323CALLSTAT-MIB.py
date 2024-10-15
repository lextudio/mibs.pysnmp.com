# SNMP MIB module (A3COM-HUAWEI-VOH323CALLSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VOH323CALLSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:23 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

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

h3cVoiceH323CallStat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11)
)
h3cVoiceH323CallStat.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVOIPH225StatTable_Object = MibTable
h3cVOIPH225StatTable = _H3cVOIPH225StatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1)
)
if mibBuilder.loadTexts:
    h3cVOIPH225StatTable.setStatus("current")
_H3cVOIPH225StatEntry_Object = MibTableRow
h3cVOIPH225StatEntry = _H3cVOIPH225StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1, 1)
)
h3cVOIPH225StatEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOH323CALLSTAT-MIB", "h3cH225MsgIndex"),
)
if mibBuilder.loadTexts:
    h3cVOIPH225StatEntry.setStatus("current")
_H3cH225MsgIndex_Type = Integer32
_H3cH225MsgIndex_Object = MibTableColumn
h3cH225MsgIndex = _H3cH225MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1, 1, 1),
    _H3cH225MsgIndex_Type()
)
h3cH225MsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cH225MsgIndex.setStatus("current")
_H3cH225MsgName_Type = OctetString
_H3cH225MsgName_Object = MibTableColumn
h3cH225MsgName = _H3cH225MsgName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1, 1, 2),
    _H3cH225MsgName_Type()
)
h3cH225MsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH225MsgName.setStatus("current")
_H3cH225MsgSend_Type = Counter32
_H3cH225MsgSend_Object = MibTableColumn
h3cH225MsgSend = _H3cH225MsgSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1, 1, 3),
    _H3cH225MsgSend_Type()
)
h3cH225MsgSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH225MsgSend.setStatus("current")
_H3cH225MsgReceive_Type = Counter32
_H3cH225MsgReceive_Object = MibTableColumn
h3cH225MsgReceive = _H3cH225MsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 1, 1, 4),
    _H3cH225MsgReceive_Type()
)
h3cH225MsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH225MsgReceive.setStatus("current")
_H3cVOIPH245StatTable_Object = MibTable
h3cVOIPH245StatTable = _H3cVOIPH245StatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2)
)
if mibBuilder.loadTexts:
    h3cVOIPH245StatTable.setStatus("current")
_H3cVOIPH245StatEntry_Object = MibTableRow
h3cVOIPH245StatEntry = _H3cVOIPH245StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2, 1)
)
h3cVOIPH245StatEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOH323CALLSTAT-MIB", "h3cH245MsgIndex"),
)
if mibBuilder.loadTexts:
    h3cVOIPH245StatEntry.setStatus("current")
_H3cH245MsgIndex_Type = Integer32
_H3cH245MsgIndex_Object = MibTableColumn
h3cH245MsgIndex = _H3cH245MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2, 1, 1),
    _H3cH245MsgIndex_Type()
)
h3cH245MsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cH245MsgIndex.setStatus("current")
_H3cH245MsgName_Type = OctetString
_H3cH245MsgName_Object = MibTableColumn
h3cH245MsgName = _H3cH245MsgName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2, 1, 2),
    _H3cH245MsgName_Type()
)
h3cH245MsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH245MsgName.setStatus("current")
_H3cH245MsgSend_Type = Counter32
_H3cH245MsgSend_Object = MibTableColumn
h3cH245MsgSend = _H3cH245MsgSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2, 1, 3),
    _H3cH245MsgSend_Type()
)
h3cH245MsgSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH245MsgSend.setStatus("current")
_H3cH245MsgReceive_Type = Counter32
_H3cH245MsgReceive_Object = MibTableColumn
h3cH245MsgReceive = _H3cH245MsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 2, 1, 4),
    _H3cH245MsgReceive_Type()
)
h3cH245MsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cH245MsgReceive.setStatus("current")
_H3cVOIPRasStatTable_Object = MibTable
h3cVOIPRasStatTable = _H3cVOIPRasStatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3)
)
if mibBuilder.loadTexts:
    h3cVOIPRasStatTable.setStatus("current")
_H3cVOIPRasStatEntry_Object = MibTableRow
h3cVOIPRasStatEntry = _H3cVOIPRasStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3, 1)
)
h3cVOIPRasStatEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOH323CALLSTAT-MIB", "h3cRasMsgIndex"),
)
if mibBuilder.loadTexts:
    h3cVOIPRasStatEntry.setStatus("current")
_H3cRasMsgIndex_Type = Integer32
_H3cRasMsgIndex_Object = MibTableColumn
h3cRasMsgIndex = _H3cRasMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3, 1, 1),
    _H3cRasMsgIndex_Type()
)
h3cRasMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRasMsgIndex.setStatus("current")
_H3cRasMsgName_Type = OctetString
_H3cRasMsgName_Object = MibTableColumn
h3cRasMsgName = _H3cRasMsgName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3, 1, 2),
    _H3cRasMsgName_Type()
)
h3cRasMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRasMsgName.setStatus("current")
_H3cRasMsgSend_Type = Counter32
_H3cRasMsgSend_Object = MibTableColumn
h3cRasMsgSend = _H3cRasMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3, 1, 3),
    _H3cRasMsgSend_Type()
)
h3cRasMsgSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRasMsgSend.setStatus("current")
_H3cRasMsgReceive_Type = Counter32
_H3cRasMsgReceive_Object = MibTableColumn
h3cRasMsgReceive = _H3cRasMsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 11, 3, 1, 4),
    _H3cRasMsgReceive_Type()
)
h3cRasMsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRasMsgReceive.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOH323CALLSTAT-MIB",
    **{"h3cVoiceH323CallStat": h3cVoiceH323CallStat,
       "h3cVOIPH225StatTable": h3cVOIPH225StatTable,
       "h3cVOIPH225StatEntry": h3cVOIPH225StatEntry,
       "h3cH225MsgIndex": h3cH225MsgIndex,
       "h3cH225MsgName": h3cH225MsgName,
       "h3cH225MsgSend": h3cH225MsgSend,
       "h3cH225MsgReceive": h3cH225MsgReceive,
       "h3cVOIPH245StatTable": h3cVOIPH245StatTable,
       "h3cVOIPH245StatEntry": h3cVOIPH245StatEntry,
       "h3cH245MsgIndex": h3cH245MsgIndex,
       "h3cH245MsgName": h3cH245MsgName,
       "h3cH245MsgSend": h3cH245MsgSend,
       "h3cH245MsgReceive": h3cH245MsgReceive,
       "h3cVOIPRasStatTable": h3cVOIPRasStatTable,
       "h3cVOIPRasStatEntry": h3cVOIPRasStatEntry,
       "h3cRasMsgIndex": h3cRasMsgIndex,
       "h3cRasMsgName": h3cRasMsgName,
       "h3cRasMsgSend": h3cRasMsgSend,
       "h3cRasMsgReceive": h3cRasMsgReceive}
)
