# SNMP MIB module (MIDCOM-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIDCOM-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:00 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(midcomGroupIndex,
 midcomRuleIndex,
 midcomSessionOwner) = mibBuilder.importSymbols(
    "MIDCOM-MIB",
    "midcomGroupIndex",
    "midcomRuleIndex",
    "midcomSessionOwner")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

midcomSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 44445)
)
midcomSrvMIB.setRevisions(
        ("2003-11-24 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MidcomNatBindMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressBind", 1),
          ("addressPortBind", 2))
    )



class MidcomNatBindId(Unsigned32, TextualConvention):
    status = "current"


class MidcomNatSessionId(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_MidcomSrvObjects_ObjectIdentity = ObjectIdentity
midcomSrvObjects = _MidcomSrvObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 1)
)
_MidcomSrvResources_ObjectIdentity = ObjectIdentity
midcomSrvResources = _MidcomSrvResources_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1)
)
_MidcomSrvResourceTable_Object = MibTable
midcomSrvResourceTable = _MidcomSrvResourceTable_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1)
)
if mibBuilder.loadTexts:
    midcomSrvResourceTable.setStatus("current")
_MidcomSrvResourceEntry_Object = MibTableRow
midcomSrvResourceEntry = _MidcomSrvResourceEntry_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1)
)
midcomSrvResourceEntry.setIndexNames(
    (0, "MIDCOM-MIB", "midcomSessionOwner"),
    (0, "MIDCOM-MIB", "midcomGroupIndex"),
    (0, "MIDCOM-MIB", "midcomRuleIndex"),
)
if mibBuilder.loadTexts:
    midcomSrvResourceEntry.setStatus("current")
_NatSrcBindMode_Type = MidcomNatBindMode
_NatSrcBindMode_Object = MibTableColumn
natSrcBindMode = _NatSrcBindMode_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 4),
    _NatSrcBindMode_Type()
)
natSrcBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSrcBindMode.setStatus("current")
_NatSrcBindId_Type = MidcomNatBindId
_NatSrcBindId_Object = MibTableColumn
natSrcBindId = _NatSrcBindId_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 5),
    _NatSrcBindId_Type()
)
natSrcBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSrcBindId.setStatus("current")
_NatDstBindMode_Type = MidcomNatBindMode
_NatDstBindMode_Object = MibTableColumn
natDstBindMode = _NatDstBindMode_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 6),
    _NatDstBindMode_Type()
)
natDstBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDstBindMode.setStatus("current")
_NatDstBindId_Type = MidcomNatBindId
_NatDstBindId_Object = MibTableColumn
natDstBindId = _NatDstBindId_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 7),
    _NatDstBindId_Type()
)
natDstBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDstBindId.setStatus("current")
_NatSessionId1_Type = MidcomNatSessionId
_NatSessionId1_Object = MibTableColumn
natSessionId1 = _NatSessionId1_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 8),
    _NatSessionId1_Type()
)
natSessionId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionId1.setStatus("current")
_NatSessionId2_Type = MidcomNatSessionId
_NatSessionId2_Object = MibTableColumn
natSessionId2 = _NatSessionId2_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 9),
    _NatSessionId2_Type()
)
natSessionId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionId2.setStatus("current")
_FwRuleId_Type = Unsigned32
_FwRuleId_Object = MibTableColumn
fwRuleId = _FwRuleId_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 1, 1, 10),
    _FwRuleId_Type()
)
fwRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRuleId.setStatus("current")
_MidcomSrvFwTable_Object = MibTable
midcomSrvFwTable = _MidcomSrvFwTable_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 2)
)
if mibBuilder.loadTexts:
    midcomSrvFwTable.setStatus("current")
_MidcomSrvFwEntry_Object = MibTableRow
midcomSrvFwEntry = _MidcomSrvFwEntry_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 2, 1)
)
midcomSrvFwEntry.setIndexNames(
    (0, "MIDCOM-SERVER-MIB", "midcomifIndex"),
)
if mibBuilder.loadTexts:
    midcomSrvFwEntry.setStatus("current")
_MidcomifIndex_Type = InterfaceIndex
_MidcomifIndex_Object = MibTableColumn
midcomifIndex = _MidcomifIndex_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 2, 1, 1),
    _MidcomifIndex_Type()
)
midcomifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomifIndex.setStatus("current")
_FwGroup_Type = SnmpAdminString
_FwGroup_Object = MibTableColumn
fwGroup = _FwGroup_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 2, 1, 2),
    _FwGroup_Type()
)
fwGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwGroup.setStatus("current")
_FwPriority_Type = Unsigned32
_FwPriority_Object = MibTableColumn
fwPriority = _FwPriority_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 1, 2, 1, 3),
    _FwPriority_Type()
)
fwPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwPriority.setStatus("current")
_MidcomSrvStatistics_ObjectIdentity = ObjectIdentity
midcomSrvStatistics = _MidcomSrvStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2)
)
_MidcomSrvSessionsRejected_Type = Unsigned32
_MidcomSrvSessionsRejected_Object = MibScalar
midcomSrvSessionsRejected = _MidcomSrvSessionsRejected_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 1),
    _MidcomSrvSessionsRejected_Type()
)
midcomSrvSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvSessionsRejected.setStatus("current")
_MidcomSrvSessionsCurrent_Type = Unsigned32
_MidcomSrvSessionsCurrent_Object = MibScalar
midcomSrvSessionsCurrent = _MidcomSrvSessionsCurrent_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 2),
    _MidcomSrvSessionsCurrent_Type()
)
midcomSrvSessionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvSessionsCurrent.setStatus("current")
_MidcomSrvSessionsTotal_Type = Unsigned32
_MidcomSrvSessionsTotal_Object = MibScalar
midcomSrvSessionsTotal = _MidcomSrvSessionsTotal_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 3),
    _MidcomSrvSessionsTotal_Type()
)
midcomSrvSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvSessionsTotal.setStatus("current")
_MidcomSrvRuleEntriesRejected_Type = Unsigned32
_MidcomSrvRuleEntriesRejected_Object = MibScalar
midcomSrvRuleEntriesRejected = _MidcomSrvRuleEntriesRejected_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 4),
    _MidcomSrvRuleEntriesRejected_Type()
)
midcomSrvRuleEntriesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvRuleEntriesRejected.setStatus("current")
_MidcomSrvRulesIncomplete_Type = Unsigned32
_MidcomSrvRulesIncomplete_Object = MibScalar
midcomSrvRulesIncomplete = _MidcomSrvRulesIncomplete_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 5),
    _MidcomSrvRulesIncomplete_Type()
)
midcomSrvRulesIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvRulesIncomplete.setStatus("current")
_MidcomSrvResRulesRejected_Type = Unsigned32
_MidcomSrvResRulesRejected_Object = MibScalar
midcomSrvResRulesRejected = _MidcomSrvResRulesRejected_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 6),
    _MidcomSrvResRulesRejected_Type()
)
midcomSrvResRulesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesRejected.setStatus("current")
_MidcomSrvResRulesFailed_Type = Unsigned32
_MidcomSrvResRulesFailed_Object = MibScalar
midcomSrvResRulesFailed = _MidcomSrvResRulesFailed_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 7),
    _MidcomSrvResRulesFailed_Type()
)
midcomSrvResRulesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesFailed.setStatus("current")
_MidcomSrvResRulesActive_Type = Unsigned32
_MidcomSrvResRulesActive_Object = MibScalar
midcomSrvResRulesActive = _MidcomSrvResRulesActive_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 8),
    _MidcomSrvResRulesActive_Type()
)
midcomSrvResRulesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesActive.setStatus("current")
_MidcomSrvResRulesExpired_Type = Unsigned32
_MidcomSrvResRulesExpired_Object = MibScalar
midcomSrvResRulesExpired = _MidcomSrvResRulesExpired_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 9),
    _MidcomSrvResRulesExpired_Type()
)
midcomSrvResRulesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesExpired.setStatus("current")
_MidcomSrvResRulesTerminated_Type = Unsigned32
_MidcomSrvResRulesTerminated_Object = MibScalar
midcomSrvResRulesTerminated = _MidcomSrvResRulesTerminated_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 10),
    _MidcomSrvResRulesTerminated_Type()
)
midcomSrvResRulesTerminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesTerminated.setStatus("current")
_MidcomSrvResRulesOnRequest_Type = Unsigned32
_MidcomSrvResRulesOnRequest_Object = MibScalar
midcomSrvResRulesOnRequest = _MidcomSrvResRulesOnRequest_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 11),
    _MidcomSrvResRulesOnRequest_Type()
)
midcomSrvResRulesOnRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvResRulesOnRequest.setStatus("current")
_MidcomSrvEnabledRulesRejected_Type = Unsigned32
_MidcomSrvEnabledRulesRejected_Object = MibScalar
midcomSrvEnabledRulesRejected = _MidcomSrvEnabledRulesRejected_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 12),
    _MidcomSrvEnabledRulesRejected_Type()
)
midcomSrvEnabledRulesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesRejected.setStatus("current")
_MidcomSrvEnabledRulesFailed_Type = Unsigned32
_MidcomSrvEnabledRulesFailed_Object = MibScalar
midcomSrvEnabledRulesFailed = _MidcomSrvEnabledRulesFailed_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 13),
    _MidcomSrvEnabledRulesFailed_Type()
)
midcomSrvEnabledRulesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesFailed.setStatus("current")
_MidcomSrvEnabledRulesActive_Type = Unsigned32
_MidcomSrvEnabledRulesActive_Object = MibScalar
midcomSrvEnabledRulesActive = _MidcomSrvEnabledRulesActive_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 14),
    _MidcomSrvEnabledRulesActive_Type()
)
midcomSrvEnabledRulesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesActive.setStatus("current")
_MidcomSrvEnabledRulesExpired_Type = Unsigned32
_MidcomSrvEnabledRulesExpired_Object = MibScalar
midcomSrvEnabledRulesExpired = _MidcomSrvEnabledRulesExpired_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 15),
    _MidcomSrvEnabledRulesExpired_Type()
)
midcomSrvEnabledRulesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesExpired.setStatus("current")
_MidcomSrvEnabledRulesTerminated_Type = Unsigned32
_MidcomSrvEnabledRulesTerminated_Object = MibScalar
midcomSrvEnabledRulesTerminated = _MidcomSrvEnabledRulesTerminated_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 16),
    _MidcomSrvEnabledRulesTerminated_Type()
)
midcomSrvEnabledRulesTerminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesTerminated.setStatus("current")
_MidcomSrvEnabledRulesOnRequest_Type = Unsigned32
_MidcomSrvEnabledRulesOnRequest_Object = MibScalar
midcomSrvEnabledRulesOnRequest = _MidcomSrvEnabledRulesOnRequest_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 17),
    _MidcomSrvEnabledRulesOnRequest_Type()
)
midcomSrvEnabledRulesOnRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvEnabledRulesOnRequest.setStatus("current")
_MidcomSrvTransRejected_Type = Unsigned32
_MidcomSrvTransRejected_Object = MibScalar
midcomSrvTransRejected = _MidcomSrvTransRejected_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 18),
    _MidcomSrvTransRejected_Type()
)
midcomSrvTransRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvTransRejected.setStatus("current")
_MidcomSrvTransFailed_Type = Unsigned32
_MidcomSrvTransFailed_Object = MibScalar
midcomSrvTransFailed = _MidcomSrvTransFailed_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 19),
    _MidcomSrvTransFailed_Type()
)
midcomSrvTransFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvTransFailed.setStatus("current")
_MidcomSrvTransCompleted_Type = Unsigned32
_MidcomSrvTransCompleted_Object = MibScalar
midcomSrvTransCompleted = _MidcomSrvTransCompleted_Object(
    (1, 3, 6, 1, 2, 1, 44445, 1, 2, 20),
    _MidcomSrvTransCompleted_Type()
)
midcomSrvTransCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomSrvTransCompleted.setStatus("current")
_MidcomSrvConformance_ObjectIdentity = ObjectIdentity
midcomSrvConformance = _MidcomSrvConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 2)
)
_MidcomSrvCompliances_ObjectIdentity = ObjectIdentity
midcomSrvCompliances = _MidcomSrvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 2, 1)
)
_MidcomSrvGroups_ObjectIdentity = ObjectIdentity
midcomSrvGroups = _MidcomSrvGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44445, 2, 2)
)

# Managed Objects groups

midcomSrvResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44445, 2, 2, 1)
)
midcomSrvResourceGroup.setObjects(
      *(("MIDCOM-SERVER-MIB", "natSrcBindMode"),
        ("MIDCOM-SERVER-MIB", "natSrcBindId"),
        ("MIDCOM-SERVER-MIB", "natDstBindMode"),
        ("MIDCOM-SERVER-MIB", "natDstBindId"),
        ("MIDCOM-SERVER-MIB", "natSessionId1"),
        ("MIDCOM-SERVER-MIB", "natSessionId2"),
        ("MIDCOM-SERVER-MIB", "fwRuleId"))
)
if mibBuilder.loadTexts:
    midcomSrvResourceGroup.setStatus("current")

midcomSrvFwGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44445, 2, 2, 2)
)
midcomSrvFwGroup.setObjects(
      *(("MIDCOM-SERVER-MIB", "fwGroup"),
        ("MIDCOM-SERVER-MIB", "fwPriority"))
)
if mibBuilder.loadTexts:
    midcomSrvFwGroup.setStatus("current")

midcomSrvStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44445, 2, 2, 3)
)
midcomSrvStatisticsGroup.setObjects(
      *(("MIDCOM-SERVER-MIB", "midcomSrvSessionsRejected"),
        ("MIDCOM-SERVER-MIB", "midcomSrvSessionsCurrent"),
        ("MIDCOM-SERVER-MIB", "midcomSrvSessionsTotal"),
        ("MIDCOM-SERVER-MIB", "midcomSrvRuleEntriesRejected"),
        ("MIDCOM-SERVER-MIB", "midcomSrvRulesIncomplete"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesRejected"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesFailed"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesActive"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesExpired"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesTerminated"),
        ("MIDCOM-SERVER-MIB", "midcomSrvResRulesOnRequest"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesRejected"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesFailed"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesActive"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesExpired"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesTerminated"),
        ("MIDCOM-SERVER-MIB", "midcomSrvEnabledRulesOnRequest"),
        ("MIDCOM-SERVER-MIB", "midcomSrvTransRejected"),
        ("MIDCOM-SERVER-MIB", "midcomSrvTransFailed"),
        ("MIDCOM-SERVER-MIB", "midcomSrvTransCompleted"))
)
if mibBuilder.loadTexts:
    midcomSrvStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

midcomSrvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 44445, 2, 1, 1)
)
if mibBuilder.loadTexts:
    midcomSrvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIDCOM-SERVER-MIB",
    **{"MidcomNatBindMode": MidcomNatBindMode,
       "MidcomNatBindId": MidcomNatBindId,
       "MidcomNatSessionId": MidcomNatSessionId,
       "midcomSrvMIB": midcomSrvMIB,
       "midcomSrvObjects": midcomSrvObjects,
       "midcomSrvResources": midcomSrvResources,
       "midcomSrvResourceTable": midcomSrvResourceTable,
       "midcomSrvResourceEntry": midcomSrvResourceEntry,
       "natSrcBindMode": natSrcBindMode,
       "natSrcBindId": natSrcBindId,
       "natDstBindMode": natDstBindMode,
       "natDstBindId": natDstBindId,
       "natSessionId1": natSessionId1,
       "natSessionId2": natSessionId2,
       "fwRuleId": fwRuleId,
       "midcomSrvFwTable": midcomSrvFwTable,
       "midcomSrvFwEntry": midcomSrvFwEntry,
       "midcomifIndex": midcomifIndex,
       "fwGroup": fwGroup,
       "fwPriority": fwPriority,
       "midcomSrvStatistics": midcomSrvStatistics,
       "midcomSrvSessionsRejected": midcomSrvSessionsRejected,
       "midcomSrvSessionsCurrent": midcomSrvSessionsCurrent,
       "midcomSrvSessionsTotal": midcomSrvSessionsTotal,
       "midcomSrvRuleEntriesRejected": midcomSrvRuleEntriesRejected,
       "midcomSrvRulesIncomplete": midcomSrvRulesIncomplete,
       "midcomSrvResRulesRejected": midcomSrvResRulesRejected,
       "midcomSrvResRulesFailed": midcomSrvResRulesFailed,
       "midcomSrvResRulesActive": midcomSrvResRulesActive,
       "midcomSrvResRulesExpired": midcomSrvResRulesExpired,
       "midcomSrvResRulesTerminated": midcomSrvResRulesTerminated,
       "midcomSrvResRulesOnRequest": midcomSrvResRulesOnRequest,
       "midcomSrvEnabledRulesRejected": midcomSrvEnabledRulesRejected,
       "midcomSrvEnabledRulesFailed": midcomSrvEnabledRulesFailed,
       "midcomSrvEnabledRulesActive": midcomSrvEnabledRulesActive,
       "midcomSrvEnabledRulesExpired": midcomSrvEnabledRulesExpired,
       "midcomSrvEnabledRulesTerminated": midcomSrvEnabledRulesTerminated,
       "midcomSrvEnabledRulesOnRequest": midcomSrvEnabledRulesOnRequest,
       "midcomSrvTransRejected": midcomSrvTransRejected,
       "midcomSrvTransFailed": midcomSrvTransFailed,
       "midcomSrvTransCompleted": midcomSrvTransCompleted,
       "midcomSrvConformance": midcomSrvConformance,
       "midcomSrvCompliances": midcomSrvCompliances,
       "midcomSrvCompliance": midcomSrvCompliance,
       "midcomSrvGroups": midcomSrvGroups,
       "midcomSrvResourceGroup": midcomSrvResourceGroup,
       "midcomSrvFwGroup": midcomSrvFwGroup,
       "midcomSrvStatisticsGroup": midcomSrvStatisticsGroup}
)
