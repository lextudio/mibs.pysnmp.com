# SNMP MIB module (REDSTONE-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:44 2024
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsNextIfIndex,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsNextIfIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rsPPPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18)
)
rsPPPoEMIB.setRevisions(
        ("1998-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsPPPoEObjects_ObjectIdentity = ObjectIdentity
rsPPPoEObjects = _RsPPPoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1)
)
_RsPPPoEIfLayer_ObjectIdentity = ObjectIdentity
rsPPPoEIfLayer = _RsPPPoEIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1)
)
_RsPPPoENextIfIndex_Type = RsNextIfIndex
_RsPPPoENextIfIndex_Object = MibScalar
rsPPPoENextIfIndex = _RsPPPoENextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 1),
    _RsPPPoENextIfIndex_Type()
)
rsPPPoENextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoENextIfIndex.setStatus("current")
_RsPPPoEIfTable_Object = MibTable
rsPPPoEIfTable = _RsPPPoEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsPPPoEIfTable.setStatus("current")
_RsPPPoEIfEntry_Object = MibTableRow
rsPPPoEIfEntry = _RsPPPoEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2, 1)
)
rsPPPoEIfEntry.setIndexNames(
    (0, "REDSTONE-PPPOE-MIB", "rsPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    rsPPPoEIfEntry.setStatus("current")
_RsPPPoEIfIfIndex_Type = InterfaceIndex
_RsPPPoEIfIfIndex_Object = MibTableColumn
rsPPPoEIfIfIndex = _RsPPPoEIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2, 1, 1),
    _RsPPPoEIfIfIndex_Type()
)
rsPPPoEIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfIfIndex.setStatus("current")


class _RsPPPoEIfMaxNumSessions_Type(Integer32):
    """Custom type rsPPPoEIfMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65336),
    )


_RsPPPoEIfMaxNumSessions_Type.__name__ = "Integer32"
_RsPPPoEIfMaxNumSessions_Object = MibTableColumn
rsPPPoEIfMaxNumSessions = _RsPPPoEIfMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2, 1, 2),
    _RsPPPoEIfMaxNumSessions_Type()
)
rsPPPoEIfMaxNumSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPPPoEIfMaxNumSessions.setStatus("current")
_RsPPPoEIfRowStatus_Type = RowStatus
_RsPPPoEIfRowStatus_Object = MibTableColumn
rsPPPoEIfRowStatus = _RsPPPoEIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2, 1, 3),
    _RsPPPoEIfRowStatus_Type()
)
rsPPPoEIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPPPoEIfRowStatus.setStatus("current")
_RsPPPoEIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsPPPoEIfLowerIfIndex_Object = MibTableColumn
rsPPPoEIfLowerIfIndex = _RsPPPoEIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 2, 1, 4),
    _RsPPPoEIfLowerIfIndex_Type()
)
rsPPPoEIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPPPoEIfLowerIfIndex.setStatus("current")
_RsPPPoEIfStatsTable_Object = MibTable
rsPPPoEIfStatsTable = _RsPPPoEIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rsPPPoEIfStatsTable.setStatus("current")
_RsPPPoEIfStatsEntry_Object = MibTableRow
rsPPPoEIfStatsEntry = _RsPPPoEIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1)
)
rsPPPoEIfStatsEntry.setIndexNames(
    (0, "REDSTONE-PPPOE-MIB", "rsPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    rsPPPoEIfStatsEntry.setStatus("current")
_RsPPPoEIfStatsRxPADI_Type = Counter32
_RsPPPoEIfStatsRxPADI_Object = MibTableColumn
rsPPPoEIfStatsRxPADI = _RsPPPoEIfStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 1),
    _RsPPPoEIfStatsRxPADI_Type()
)
rsPPPoEIfStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxPADI.setStatus("current")
_RsPPPoEIfStatsTxPADO_Type = Counter32
_RsPPPoEIfStatsTxPADO_Object = MibTableColumn
rsPPPoEIfStatsTxPADO = _RsPPPoEIfStatsTxPADO_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 2),
    _RsPPPoEIfStatsTxPADO_Type()
)
rsPPPoEIfStatsTxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsTxPADO.setStatus("current")
_RsPPPoEIfStatsRxPADR_Type = Counter32
_RsPPPoEIfStatsRxPADR_Object = MibTableColumn
rsPPPoEIfStatsRxPADR = _RsPPPoEIfStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 3),
    _RsPPPoEIfStatsRxPADR_Type()
)
rsPPPoEIfStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxPADR.setStatus("current")
_RsPPPoEIfStatsTxPADS_Type = Counter32
_RsPPPoEIfStatsTxPADS_Object = MibTableColumn
rsPPPoEIfStatsTxPADS = _RsPPPoEIfStatsTxPADS_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 4),
    _RsPPPoEIfStatsTxPADS_Type()
)
rsPPPoEIfStatsTxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsTxPADS.setStatus("current")
_RsPPPoEIfStatsRxPADT_Type = Counter32
_RsPPPoEIfStatsRxPADT_Object = MibTableColumn
rsPPPoEIfStatsRxPADT = _RsPPPoEIfStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 5),
    _RsPPPoEIfStatsRxPADT_Type()
)
rsPPPoEIfStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxPADT.setStatus("current")
_RsPPPoEIfStatsTxPADT_Type = Counter32
_RsPPPoEIfStatsTxPADT_Object = MibTableColumn
rsPPPoEIfStatsTxPADT = _RsPPPoEIfStatsTxPADT_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 6),
    _RsPPPoEIfStatsTxPADT_Type()
)
rsPPPoEIfStatsTxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsTxPADT.setStatus("current")
_RsPPPoEIfStatsRxInvVersion_Type = Counter32
_RsPPPoEIfStatsRxInvVersion_Object = MibTableColumn
rsPPPoEIfStatsRxInvVersion = _RsPPPoEIfStatsRxInvVersion_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 7),
    _RsPPPoEIfStatsRxInvVersion_Type()
)
rsPPPoEIfStatsRxInvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvVersion.setStatus("current")
_RsPPPoEIfStatsRxInvCode_Type = Counter32
_RsPPPoEIfStatsRxInvCode_Object = MibTableColumn
rsPPPoEIfStatsRxInvCode = _RsPPPoEIfStatsRxInvCode_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 8),
    _RsPPPoEIfStatsRxInvCode_Type()
)
rsPPPoEIfStatsRxInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvCode.setStatus("current")
_RsPPPoEIfStatsRxInvTags_Type = Counter32
_RsPPPoEIfStatsRxInvTags_Object = MibTableColumn
rsPPPoEIfStatsRxInvTags = _RsPPPoEIfStatsRxInvTags_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 9),
    _RsPPPoEIfStatsRxInvTags_Type()
)
rsPPPoEIfStatsRxInvTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvTags.setStatus("current")
_RsPPPoEIfStatsRxInvSession_Type = Counter32
_RsPPPoEIfStatsRxInvSession_Object = MibTableColumn
rsPPPoEIfStatsRxInvSession = _RsPPPoEIfStatsRxInvSession_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 10),
    _RsPPPoEIfStatsRxInvSession_Type()
)
rsPPPoEIfStatsRxInvSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvSession.setStatus("current")
_RsPPPoEIfStatsRxInvTypes_Type = Counter32
_RsPPPoEIfStatsRxInvTypes_Object = MibTableColumn
rsPPPoEIfStatsRxInvTypes = _RsPPPoEIfStatsRxInvTypes_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 11),
    _RsPPPoEIfStatsRxInvTypes_Type()
)
rsPPPoEIfStatsRxInvTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvTypes.setStatus("current")
_RsPPPoEIfStatsRxInvPackets_Type = Counter32
_RsPPPoEIfStatsRxInvPackets_Object = MibTableColumn
rsPPPoEIfStatsRxInvPackets = _RsPPPoEIfStatsRxInvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 12),
    _RsPPPoEIfStatsRxInvPackets_Type()
)
rsPPPoEIfStatsRxInvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInvPackets.setStatus("current")
_RsPPPoEIfStatsRxInsufficientResources_Type = Counter32
_RsPPPoEIfStatsRxInsufficientResources_Object = MibTableColumn
rsPPPoEIfStatsRxInsufficientResources = _RsPPPoEIfStatsRxInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 1, 3, 1, 13),
    _RsPPPoEIfStatsRxInsufficientResources_Type()
)
rsPPPoEIfStatsRxInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoEIfStatsRxInsufficientResources.setStatus("current")
_RsPPPoESubIfLayer_ObjectIdentity = ObjectIdentity
rsPPPoESubIfLayer = _RsPPPoESubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2)
)
_RsPPPoESubIfNextIfIndex_Type = RsNextIfIndex
_RsPPPoESubIfNextIfIndex_Object = MibScalar
rsPPPoESubIfNextIfIndex = _RsPPPoESubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 1),
    _RsPPPoESubIfNextIfIndex_Type()
)
rsPPPoESubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoESubIfNextIfIndex.setStatus("current")
_RsPPPoESubIfTable_Object = MibTable
rsPPPoESubIfTable = _RsPPPoESubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsPPPoESubIfTable.setStatus("current")
_RsPPPoESubIfEntry_Object = MibTableRow
rsPPPoESubIfEntry = _RsPPPoESubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1)
)
rsPPPoESubIfEntry.setIndexNames(
    (0, "REDSTONE-PPPOE-MIB", "rsPPPoESubIfIndex"),
)
if mibBuilder.loadTexts:
    rsPPPoESubIfEntry.setStatus("current")
_RsPPPoESubIfIndex_Type = InterfaceIndex
_RsPPPoESubIfIndex_Object = MibTableColumn
rsPPPoESubIfIndex = _RsPPPoESubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1, 1),
    _RsPPPoESubIfIndex_Type()
)
rsPPPoESubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsPPPoESubIfIndex.setStatus("current")
_RsPPPoESubIfRowStatus_Type = RowStatus
_RsPPPoESubIfRowStatus_Object = MibTableColumn
rsPPPoESubIfRowStatus = _RsPPPoESubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1, 2),
    _RsPPPoESubIfRowStatus_Type()
)
rsPPPoESubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPPPoESubIfRowStatus.setStatus("current")
_RsPPPoESubIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsPPPoESubIfLowerIfIndex_Object = MibTableColumn
rsPPPoESubIfLowerIfIndex = _RsPPPoESubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1, 3),
    _RsPPPoESubIfLowerIfIndex_Type()
)
rsPPPoESubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPPPoESubIfLowerIfIndex.setStatus("current")


class _RsPPPoESubIfId_Type(Integer32):
    """Custom type rsPPPoESubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RsPPPoESubIfId_Type.__name__ = "Integer32"
_RsPPPoESubIfId_Object = MibTableColumn
rsPPPoESubIfId = _RsPPPoESubIfId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1, 4),
    _RsPPPoESubIfId_Type()
)
rsPPPoESubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPPPoESubIfId.setStatus("current")


class _RsPPPoESubIfSessionId_Type(Integer32):
    """Custom type rsPPPoESubIfSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsPPPoESubIfSessionId_Type.__name__ = "Integer32"
_RsPPPoESubIfSessionId_Object = MibTableColumn
rsPPPoESubIfSessionId = _RsPPPoESubIfSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 1, 2, 2, 1, 5),
    _RsPPPoESubIfSessionId_Type()
)
rsPPPoESubIfSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPPPoESubIfSessionId.setStatus("current")
_RsPPPoEConformance_ObjectIdentity = ObjectIdentity
rsPPPoEConformance = _RsPPPoEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4)
)
_RsPPPoECompliances_ObjectIdentity = ObjectIdentity
rsPPPoECompliances = _RsPPPoECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4, 1)
)
_RsPPPoEGroups_ObjectIdentity = ObjectIdentity
rsPPPoEGroups = _RsPPPoEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4, 2)
)

# Managed Objects groups

rsPPPoEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4, 2, 1)
)
rsPPPoEGroup.setObjects(
      *(("REDSTONE-PPPOE-MIB", "rsPPPoENextIfIndex"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfIfIndex"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfMaxNumSessions"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfRowStatus"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfLowerIfIndex"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxPADI"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsTxPADO"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxPADR"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsTxPADS"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxPADT"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsTxPADT"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxInvVersion"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxInvCode"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxInvTags"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoEIfStatsRxInvSession"))
)
if mibBuilder.loadTexts:
    rsPPPoEGroup.setStatus("current")

rsPPPoESubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4, 2, 2)
)
rsPPPoESubIfGroup.setObjects(
      *(("REDSTONE-PPPOE-MIB", "rsPPPoESubIfNextIfIndex"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoESubIfRowStatus"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoESubIfLowerIfIndex"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoESubIfId"),
        ("REDSTONE-PPPOE-MIB", "rsPPPoESubIfSessionId"))
)
if mibBuilder.loadTexts:
    rsPPPoESubIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsPPPoECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 18, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsPPPoECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-PPPOE-MIB",
    **{"rsPPPoEMIB": rsPPPoEMIB,
       "rsPPPoEObjects": rsPPPoEObjects,
       "rsPPPoEIfLayer": rsPPPoEIfLayer,
       "rsPPPoENextIfIndex": rsPPPoENextIfIndex,
       "rsPPPoEIfTable": rsPPPoEIfTable,
       "rsPPPoEIfEntry": rsPPPoEIfEntry,
       "rsPPPoEIfIfIndex": rsPPPoEIfIfIndex,
       "rsPPPoEIfMaxNumSessions": rsPPPoEIfMaxNumSessions,
       "rsPPPoEIfRowStatus": rsPPPoEIfRowStatus,
       "rsPPPoEIfLowerIfIndex": rsPPPoEIfLowerIfIndex,
       "rsPPPoEIfStatsTable": rsPPPoEIfStatsTable,
       "rsPPPoEIfStatsEntry": rsPPPoEIfStatsEntry,
       "rsPPPoEIfStatsRxPADI": rsPPPoEIfStatsRxPADI,
       "rsPPPoEIfStatsTxPADO": rsPPPoEIfStatsTxPADO,
       "rsPPPoEIfStatsRxPADR": rsPPPoEIfStatsRxPADR,
       "rsPPPoEIfStatsTxPADS": rsPPPoEIfStatsTxPADS,
       "rsPPPoEIfStatsRxPADT": rsPPPoEIfStatsRxPADT,
       "rsPPPoEIfStatsTxPADT": rsPPPoEIfStatsTxPADT,
       "rsPPPoEIfStatsRxInvVersion": rsPPPoEIfStatsRxInvVersion,
       "rsPPPoEIfStatsRxInvCode": rsPPPoEIfStatsRxInvCode,
       "rsPPPoEIfStatsRxInvTags": rsPPPoEIfStatsRxInvTags,
       "rsPPPoEIfStatsRxInvSession": rsPPPoEIfStatsRxInvSession,
       "rsPPPoEIfStatsRxInvTypes": rsPPPoEIfStatsRxInvTypes,
       "rsPPPoEIfStatsRxInvPackets": rsPPPoEIfStatsRxInvPackets,
       "rsPPPoEIfStatsRxInsufficientResources": rsPPPoEIfStatsRxInsufficientResources,
       "rsPPPoESubIfLayer": rsPPPoESubIfLayer,
       "rsPPPoESubIfNextIfIndex": rsPPPoESubIfNextIfIndex,
       "rsPPPoESubIfTable": rsPPPoESubIfTable,
       "rsPPPoESubIfEntry": rsPPPoESubIfEntry,
       "rsPPPoESubIfIndex": rsPPPoESubIfIndex,
       "rsPPPoESubIfRowStatus": rsPPPoESubIfRowStatus,
       "rsPPPoESubIfLowerIfIndex": rsPPPoESubIfLowerIfIndex,
       "rsPPPoESubIfId": rsPPPoESubIfId,
       "rsPPPoESubIfSessionId": rsPPPoESubIfSessionId,
       "rsPPPoEConformance": rsPPPoEConformance,
       "rsPPPoECompliances": rsPPPoECompliances,
       "rsPPPoECompliance": rsPPPoECompliance,
       "rsPPPoEGroups": rsPPPoEGroups,
       "rsPPPoEGroup": rsPPPoEGroup,
       "rsPPPoESubIfGroup": rsPPPoESubIfGroup}
)
