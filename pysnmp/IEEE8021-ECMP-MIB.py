# SNMP MIB module (IEEE8021-ECMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-ECMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:20 2024
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

(ieee8021BridgeBasePort,
 ieee8021BridgeBasePortComponentId) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortComponentId")

(ieee8021QBridgePortVlanStatisticsEntry,
 ieee8021QBridgeTpFdbEntry) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgePortVlanStatisticsEntry",
    "ieee8021QBridgeTpFdbEntry")

(IEEE8021SpbBridgePriority,
 ieee8021SpbTopIx,
 ieee8021SpbmTopSrvTableEntry) = mibBuilder.importSymbols(
    "IEEE8021-SPB-MIB",
    "IEEE8021SpbBridgePriority",
    "ieee8021SpbTopIx",
    "ieee8021SpbmTopSrvTableEntry")

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021EcmpMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28)
)
ieee8021EcmpMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2013-05-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021EcmpNotifications_ObjectIdentity = ObjectIdentity
ieee8021EcmpNotifications = _Ieee8021EcmpNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28, 0)
)
_Ieee8021EcmpObjects_ObjectIdentity = ObjectIdentity
ieee8021EcmpObjects = _Ieee8021EcmpObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28, 1)
)
_Ieee8021QBridgeEcmpFdbTable_Object = MibTable
ieee8021QBridgeEcmpFdbTable = _Ieee8021QBridgeEcmpFdbTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEcmpFdbTable.setStatus("current")
_Ieee8021QBridgeEcmpFdbEntry_Object = MibTableRow
ieee8021QBridgeEcmpFdbEntry = _Ieee8021QBridgeEcmpFdbEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEcmpFdbEntry.setStatus("current")
_Ieee8021QBridgeEcmpFdbPortList_Type = PortList
_Ieee8021QBridgeEcmpFdbPortList_Object = MibTableColumn
ieee8021QBridgeEcmpFdbPortList = _Ieee8021QBridgeEcmpFdbPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1, 1),
    _Ieee8021QBridgeEcmpFdbPortList_Type()
)
ieee8021QBridgeEcmpFdbPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeEcmpFdbPortList.setStatus("current")
_Ieee8021EcmpFlowFilterCtlTable_Object = MibTable
ieee8021EcmpFlowFilterCtlTable = _Ieee8021EcmpFlowFilterCtlTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlTable.setStatus("current")
_Ieee8021EcmpFlowFilterCtlEntry_Object = MibTableRow
ieee8021EcmpFlowFilterCtlEntry = _Ieee8021EcmpFlowFilterCtlEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1)
)
ieee8021EcmpFlowFilterCtlEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlVid"),
)
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlEntry.setStatus("current")
_Ieee8021EcmpFlowFilterCtlVid_Type = VlanId
_Ieee8021EcmpFlowFilterCtlVid_Object = MibTableColumn
ieee8021EcmpFlowFilterCtlVid = _Ieee8021EcmpFlowFilterCtlVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 1),
    _Ieee8021EcmpFlowFilterCtlVid_Type()
)
ieee8021EcmpFlowFilterCtlVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlVid.setStatus("current")
_Ieee8021EcmpFlowFilterCtlEnabled_Type = TruthValue
_Ieee8021EcmpFlowFilterCtlEnabled_Object = MibTableColumn
ieee8021EcmpFlowFilterCtlEnabled = _Ieee8021EcmpFlowFilterCtlEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 2),
    _Ieee8021EcmpFlowFilterCtlEnabled_Type()
)
ieee8021EcmpFlowFilterCtlEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlEnabled.setStatus("current")
_Ieee8021EcmpFlowFilterCtlHashGen_Type = TruthValue
_Ieee8021EcmpFlowFilterCtlHashGen_Object = MibTableColumn
ieee8021EcmpFlowFilterCtlHashGen = _Ieee8021EcmpFlowFilterCtlHashGen_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 3),
    _Ieee8021EcmpFlowFilterCtlHashGen_Type()
)
ieee8021EcmpFlowFilterCtlHashGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlHashGen.setStatus("current")


class _Ieee8021EcmpFlowFilterCtlTtl_Type(Integer32):
    """Custom type ieee8021EcmpFlowFilterCtlTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Ieee8021EcmpFlowFilterCtlTtl_Type.__name__ = "Integer32"
_Ieee8021EcmpFlowFilterCtlTtl_Object = MibTableColumn
ieee8021EcmpFlowFilterCtlTtl = _Ieee8021EcmpFlowFilterCtlTtl_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 4),
    _Ieee8021EcmpFlowFilterCtlTtl_Type()
)
ieee8021EcmpFlowFilterCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlTtl.setStatus("current")
_Ieee8021EcmpEctStaticTable_Object = MibTable
ieee8021EcmpEctStaticTable = _Ieee8021EcmpEctStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticTable.setStatus("current")
_Ieee8021EcmpEctStaticEntry_Object = MibTableRow
ieee8021EcmpEctStaticEntry = _Ieee8021EcmpEctStaticEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1)
)
ieee8021EcmpEctStaticEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"),
    (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryTieBreakMask"),
)
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticEntry.setStatus("current")


class _Ieee8021EcmpEctStaticEntryTieBreakMask_Type(Integer32):
    """Custom type ieee8021EcmpEctStaticEntryTieBreakMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021EcmpEctStaticEntryTieBreakMask_Type.__name__ = "Integer32"
_Ieee8021EcmpEctStaticEntryTieBreakMask_Object = MibTableColumn
ieee8021EcmpEctStaticEntryTieBreakMask = _Ieee8021EcmpEctStaticEntryTieBreakMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 1),
    _Ieee8021EcmpEctStaticEntryTieBreakMask_Type()
)
ieee8021EcmpEctStaticEntryTieBreakMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticEntryTieBreakMask.setStatus("current")
_Ieee8021EcmpEctStaticEntryBridgePriority_Type = IEEE8021SpbBridgePriority
_Ieee8021EcmpEctStaticEntryBridgePriority_Object = MibTableColumn
ieee8021EcmpEctStaticEntryBridgePriority = _Ieee8021EcmpEctStaticEntryBridgePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 2),
    _Ieee8021EcmpEctStaticEntryBridgePriority_Type()
)
ieee8021EcmpEctStaticEntryBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticEntryBridgePriority.setStatus("current")
_Ieee8021EcmpEctStaticEntryRowStatus_Type = RowStatus
_Ieee8021EcmpEctStaticEntryRowStatus_Object = MibTableColumn
ieee8021EcmpEctStaticEntryRowStatus = _Ieee8021EcmpEctStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 3),
    _Ieee8021EcmpEctStaticEntryRowStatus_Type()
)
ieee8021EcmpEctStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticEntryRowStatus.setStatus("current")
_Ieee8021EcmpTopSrvTable_Object = MibTable
ieee8021EcmpTopSrvTable = _Ieee8021EcmpTopSrvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021EcmpTopSrvTable.setStatus("current")
_Ieee8021EcmpTopSrvEntry_Object = MibTableRow
ieee8021EcmpTopSrvEntry = _Ieee8021EcmpTopSrvEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021EcmpTopSrvEntry.setStatus("current")
_Ieee8021EcmpTopSrvEntryTsBit_Type = TruthValue
_Ieee8021EcmpTopSrvEntryTsBit_Object = MibTableColumn
ieee8021EcmpTopSrvEntryTsBit = _Ieee8021EcmpTopSrvEntryTsBit_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 1),
    _Ieee8021EcmpTopSrvEntryTsBit_Type()
)
ieee8021EcmpTopSrvEntryTsBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021EcmpTopSrvEntryTsBit.setStatus("current")


class _Ieee8021EcmpTopSrvEntryTieBreakMask_Type(Integer32):
    """Custom type ieee8021EcmpTopSrvEntryTieBreakMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021EcmpTopSrvEntryTieBreakMask_Type.__name__ = "Integer32"
_Ieee8021EcmpTopSrvEntryTieBreakMask_Object = MibTableColumn
ieee8021EcmpTopSrvEntryTieBreakMask = _Ieee8021EcmpTopSrvEntryTieBreakMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 2),
    _Ieee8021EcmpTopSrvEntryTieBreakMask_Type()
)
ieee8021EcmpTopSrvEntryTieBreakMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021EcmpTopSrvEntryTieBreakMask.setStatus("current")
_Ieee8021QBridgePortVlanTtlStatisticsTable_Object = MibTable
ieee8021QBridgePortVlanTtlStatisticsTable = _Ieee8021QBridgePortVlanTtlStatisticsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanTtlStatisticsTable.setStatus("current")
_Ieee8021QBridgePortVlanTtlStatisticsEntry_Object = MibTableRow
ieee8021QBridgePortVlanTtlStatisticsEntry = _Ieee8021QBridgePortVlanTtlStatisticsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanTtlStatisticsEntry.setStatus("current")
_Ieee8021QBridgeTpVlanPortTtlDiscards_Type = Counter64
_Ieee8021QBridgeTpVlanPortTtlDiscards_Object = MibTableColumn
ieee8021QBridgeTpVlanPortTtlDiscards = _Ieee8021QBridgeTpVlanPortTtlDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1, 1),
    _Ieee8021QBridgeTpVlanPortTtlDiscards_Type()
)
ieee8021QBridgeTpVlanPortTtlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortTtlDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortTtlDiscards.setUnits("frames")
_Ieee8021EcmpConformance_ObjectIdentity = ObjectIdentity
ieee8021EcmpConformance = _Ieee8021EcmpConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28, 2)
)
_Ieee8021EcmpGroups_ObjectIdentity = ObjectIdentity
ieee8021EcmpGroups = _Ieee8021EcmpGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1)
)
_Ieee8021EcmpCompliances_ObjectIdentity = ObjectIdentity
ieee8021EcmpCompliances = _Ieee8021EcmpCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 2)
)
ieee8021QBridgeTpFdbEntry.registerAugmentions(
    ("IEEE8021-ECMP-MIB",
     "ieee8021QBridgeEcmpFdbEntry")
)
ieee8021QBridgeEcmpFdbEntry.setIndexNames(*ieee8021QBridgeTpFdbEntry.getIndexNames())
ieee8021SpbmTopSrvTableEntry.registerAugmentions(
    ("IEEE8021-ECMP-MIB",
     "ieee8021EcmpTopSrvEntry")
)
ieee8021EcmpTopSrvEntry.setIndexNames(*ieee8021SpbmTopSrvTableEntry.getIndexNames())
ieee8021QBridgePortVlanStatisticsEntry.registerAugmentions(
    ("IEEE8021-ECMP-MIB",
     "ieee8021QBridgePortVlanTtlStatisticsEntry")
)
ieee8021QBridgePortVlanTtlStatisticsEntry.setIndexNames(*ieee8021QBridgePortVlanStatisticsEntry.getIndexNames())

# Managed Objects groups

ieee8021QBridgeEcmpFdbGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 1)
)
ieee8021QBridgeEcmpFdbGroup.setObjects(
    ("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbPortList")
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEcmpFdbGroup.setStatus("current")

ieee8021EcmpFlowFilterCtlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 2)
)
ieee8021EcmpFlowFilterCtlGroup.setObjects(
      *(("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlEnabled"),
        ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlHashGen"),
        ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlTtl"))
)
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilterCtlGroup.setStatus("current")

ieee8021EcmpEctStaticGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 3)
)
ieee8021EcmpEctStaticGroup.setObjects(
      *(("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryBridgePriority"),
        ("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021EcmpEctStaticGroup.setStatus("current")

ieee8021EcmpTopSrvGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 4)
)
ieee8021EcmpTopSrvGroup.setObjects(
      *(("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTsBit"),
        ("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTieBreakMask"))
)
if mibBuilder.loadTexts:
    ieee8021EcmpTopSrvGroup.setStatus("current")

ieee8021QBridgePortVlanTtlStatisticsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 5)
)
ieee8021QBridgePortVlanTtlStatisticsGroup.setObjects(
    ("IEEE8021-ECMP-MIB", "ieee8021QBridgeTpVlanPortTtlDiscards")
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanTtlStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021EcmpCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021EcmpCompliance.setStatus(
        "current"
    )

ieee8021EcmpFlowFilteringCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021EcmpFlowFilteringCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-ECMP-MIB",
    **{"ieee8021EcmpMib": ieee8021EcmpMib,
       "ieee8021EcmpNotifications": ieee8021EcmpNotifications,
       "ieee8021EcmpObjects": ieee8021EcmpObjects,
       "ieee8021QBridgeEcmpFdbTable": ieee8021QBridgeEcmpFdbTable,
       "ieee8021QBridgeEcmpFdbEntry": ieee8021QBridgeEcmpFdbEntry,
       "ieee8021QBridgeEcmpFdbPortList": ieee8021QBridgeEcmpFdbPortList,
       "ieee8021EcmpFlowFilterCtlTable": ieee8021EcmpFlowFilterCtlTable,
       "ieee8021EcmpFlowFilterCtlEntry": ieee8021EcmpFlowFilterCtlEntry,
       "ieee8021EcmpFlowFilterCtlVid": ieee8021EcmpFlowFilterCtlVid,
       "ieee8021EcmpFlowFilterCtlEnabled": ieee8021EcmpFlowFilterCtlEnabled,
       "ieee8021EcmpFlowFilterCtlHashGen": ieee8021EcmpFlowFilterCtlHashGen,
       "ieee8021EcmpFlowFilterCtlTtl": ieee8021EcmpFlowFilterCtlTtl,
       "ieee8021EcmpEctStaticTable": ieee8021EcmpEctStaticTable,
       "ieee8021EcmpEctStaticEntry": ieee8021EcmpEctStaticEntry,
       "ieee8021EcmpEctStaticEntryTieBreakMask": ieee8021EcmpEctStaticEntryTieBreakMask,
       "ieee8021EcmpEctStaticEntryBridgePriority": ieee8021EcmpEctStaticEntryBridgePriority,
       "ieee8021EcmpEctStaticEntryRowStatus": ieee8021EcmpEctStaticEntryRowStatus,
       "ieee8021EcmpTopSrvTable": ieee8021EcmpTopSrvTable,
       "ieee8021EcmpTopSrvEntry": ieee8021EcmpTopSrvEntry,
       "ieee8021EcmpTopSrvEntryTsBit": ieee8021EcmpTopSrvEntryTsBit,
       "ieee8021EcmpTopSrvEntryTieBreakMask": ieee8021EcmpTopSrvEntryTieBreakMask,
       "ieee8021QBridgePortVlanTtlStatisticsTable": ieee8021QBridgePortVlanTtlStatisticsTable,
       "ieee8021QBridgePortVlanTtlStatisticsEntry": ieee8021QBridgePortVlanTtlStatisticsEntry,
       "ieee8021QBridgeTpVlanPortTtlDiscards": ieee8021QBridgeTpVlanPortTtlDiscards,
       "ieee8021EcmpConformance": ieee8021EcmpConformance,
       "ieee8021EcmpGroups": ieee8021EcmpGroups,
       "ieee8021QBridgeEcmpFdbGroup": ieee8021QBridgeEcmpFdbGroup,
       "ieee8021EcmpFlowFilterCtlGroup": ieee8021EcmpFlowFilterCtlGroup,
       "ieee8021EcmpEctStaticGroup": ieee8021EcmpEctStaticGroup,
       "ieee8021EcmpTopSrvGroup": ieee8021EcmpTopSrvGroup,
       "ieee8021QBridgePortVlanTtlStatisticsGroup": ieee8021QBridgePortVlanTtlStatisticsGroup,
       "ieee8021EcmpCompliances": ieee8021EcmpCompliances,
       "ieee8021EcmpCompliance": ieee8021EcmpCompliance,
       "ieee8021EcmpFlowFilteringCompliance": ieee8021EcmpFlowFilteringCompliance}
)
