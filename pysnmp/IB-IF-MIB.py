# SNMP MIB module (IB-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:16 2024
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

(IbIpoibClientIdentifier,
 IbVirtualLane,
 infinibandMIB) = mibBuilder.importSymbols(
    "IB-TC-MIB",
    "IbIpoibClientIdentifier",
    "IbVirtualLane",
    "infinibandMIB")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ibIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 117, 2)
)
ibIfMIB.setRevisions(
        ("2006-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbIfObjects_ObjectIdentity = ObjectIdentity
ibIfObjects = _IbIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 2, 1)
)
_IbIfPortStatTable_Object = MibTable
ibIfPortStatTable = _IbIfPortStatTable_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibIfPortStatTable.setStatus("current")
_IbIfPortStatEntry_Object = MibTableRow
ibIfPortStatEntry = _IbIfPortStatEntry_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1)
)
ibIfPortStatEntry.setIndexNames(
    (0, "IB-IF-MIB", "ibIfPortStatIfIndex"),
)
if mibBuilder.loadTexts:
    ibIfPortStatEntry.setStatus("current")
_IbIfPortStatIfIndex_Type = InterfaceIndex
_IbIfPortStatIfIndex_Object = MibTableColumn
ibIfPortStatIfIndex = _IbIfPortStatIfIndex_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 1),
    _IbIfPortStatIfIndex_Type()
)
ibIfPortStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibIfPortStatIfIndex.setStatus("current")
_IbIfPortSymbolErrs_Type = Counter32
_IbIfPortSymbolErrs_Object = MibTableColumn
ibIfPortSymbolErrs = _IbIfPortSymbolErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 2),
    _IbIfPortSymbolErrs_Type()
)
ibIfPortSymbolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortSymbolErrs.setStatus("current")
_IbIfPortLinkErrRecovery_Type = Counter32
_IbIfPortLinkErrRecovery_Object = MibTableColumn
ibIfPortLinkErrRecovery = _IbIfPortLinkErrRecovery_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 3),
    _IbIfPortLinkErrRecovery_Type()
)
ibIfPortLinkErrRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortLinkErrRecovery.setStatus("current")
_IbIfPortLinkDowned_Type = Counter32
_IbIfPortLinkDowned_Object = MibTableColumn
ibIfPortLinkDowned = _IbIfPortLinkDowned_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 4),
    _IbIfPortLinkDowned_Type()
)
ibIfPortLinkDowned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortLinkDowned.setStatus("current")
_IbIfPortStatLocalPhyErrs_Type = Counter32
_IbIfPortStatLocalPhyErrs_Object = MibTableColumn
ibIfPortStatLocalPhyErrs = _IbIfPortStatLocalPhyErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 5),
    _IbIfPortStatLocalPhyErrs_Type()
)
ibIfPortStatLocalPhyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatLocalPhyErrs.setStatus("current")
_IbIfPortStatMalPktErrs_Type = Counter32
_IbIfPortStatMalPktErrs_Object = MibTableColumn
ibIfPortStatMalPktErrs = _IbIfPortStatMalPktErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 6),
    _IbIfPortStatMalPktErrs_Type()
)
ibIfPortStatMalPktErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatMalPktErrs.setStatus("current")
_IbIfPortStatRcvRemPhyErrs_Type = Counter32
_IbIfPortStatRcvRemPhyErrs_Object = MibTableColumn
ibIfPortStatRcvRemPhyErrs = _IbIfPortStatRcvRemPhyErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 7),
    _IbIfPortStatRcvRemPhyErrs_Type()
)
ibIfPortStatRcvRemPhyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatRcvRemPhyErrs.setStatus("current")
_IbIfPortStatRcvConstrErrs_Type = Counter32
_IbIfPortStatRcvConstrErrs_Object = MibTableColumn
ibIfPortStatRcvConstrErrs = _IbIfPortStatRcvConstrErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 8),
    _IbIfPortStatRcvConstrErrs_Type()
)
ibIfPortStatRcvConstrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatRcvConstrErrs.setStatus("current")
_IbIfPortStatInactDiscards_Type = Counter32
_IbIfPortStatInactDiscards_Object = MibTableColumn
ibIfPortStatInactDiscards = _IbIfPortStatInactDiscards_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 9),
    _IbIfPortStatInactDiscards_Type()
)
ibIfPortStatInactDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatInactDiscards.setStatus("current")
_IbIfPortStatNeighMTUDiscards_Type = Counter32
_IbIfPortStatNeighMTUDiscards_Object = MibTableColumn
ibIfPortStatNeighMTUDiscards = _IbIfPortStatNeighMTUDiscards_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 10),
    _IbIfPortStatNeighMTUDiscards_Type()
)
ibIfPortStatNeighMTUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatNeighMTUDiscards.setStatus("current")
_IbIfPortStatSwLifetimeDiscards_Type = Counter32
_IbIfPortStatSwLifetimeDiscards_Object = MibTableColumn
ibIfPortStatSwLifetimeDiscards = _IbIfPortStatSwLifetimeDiscards_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 11),
    _IbIfPortStatSwLifetimeDiscards_Type()
)
ibIfPortStatSwLifetimeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatSwLifetimeDiscards.setStatus("current")
_IbIfPortStatHOQLifetimeDiscards_Type = Counter32
_IbIfPortStatHOQLifetimeDiscards_Object = MibTableColumn
ibIfPortStatHOQLifetimeDiscards = _IbIfPortStatHOQLifetimeDiscards_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 12),
    _IbIfPortStatHOQLifetimeDiscards_Type()
)
ibIfPortStatHOQLifetimeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatHOQLifetimeDiscards.setStatus("current")
_IbIfPortStatLinkIntergrityErrs_Type = Counter32
_IbIfPortStatLinkIntergrityErrs_Object = MibTableColumn
ibIfPortStatLinkIntergrityErrs = _IbIfPortStatLinkIntergrityErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 13),
    _IbIfPortStatLinkIntergrityErrs_Type()
)
ibIfPortStatLinkIntergrityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatLinkIntergrityErrs.setStatus("current")
_IbIfPortStatExcBufOverrunErrs_Type = Counter32
_IbIfPortStatExcBufOverrunErrs_Object = MibTableColumn
ibIfPortStatExcBufOverrunErrs = _IbIfPortStatExcBufOverrunErrs_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 14),
    _IbIfPortStatExcBufOverrunErrs_Type()
)
ibIfPortStatExcBufOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatExcBufOverrunErrs.setStatus("current")
_IbIfPortStatVL15Dropped_Type = Counter32
_IbIfPortStatVL15Dropped_Object = MibTableColumn
ibIfPortStatVL15Dropped = _IbIfPortStatVL15Dropped_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 15),
    _IbIfPortStatVL15Dropped_Type()
)
ibIfPortStatVL15Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfPortStatVL15Dropped.setStatus("current")
_IbIfVLTrafficTable_Object = MibTable
ibIfVLTrafficTable = _IbIfVLTrafficTable_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibIfVLTrafficTable.setStatus("current")
_IbIfVLTrafficEntry_Object = MibTableRow
ibIfVLTrafficEntry = _IbIfVLTrafficEntry_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1)
)
ibIfVLTrafficEntry.setIndexNames(
    (0, "IB-IF-MIB", "ibIfVLTrafficIfIndex"),
    (0, "IB-IF-MIB", "ibIfVLIndex"),
)
if mibBuilder.loadTexts:
    ibIfVLTrafficEntry.setStatus("current")
_IbIfVLTrafficIfIndex_Type = InterfaceIndex
_IbIfVLTrafficIfIndex_Object = MibTableColumn
ibIfVLTrafficIfIndex = _IbIfVLTrafficIfIndex_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 1),
    _IbIfVLTrafficIfIndex_Type()
)
ibIfVLTrafficIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibIfVLTrafficIfIndex.setStatus("current")
_IbIfVLIndex_Type = IbVirtualLane
_IbIfVLIndex_Object = MibTableColumn
ibIfVLIndex = _IbIfVLIndex_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 2),
    _IbIfVLIndex_Type()
)
ibIfVLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibIfVLIndex.setStatus("current")
_IbIfVLOutOctets_Type = Counter64
_IbIfVLOutOctets_Object = MibTableColumn
ibIfVLOutOctets = _IbIfVLOutOctets_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 3),
    _IbIfVLOutOctets_Type()
)
ibIfVLOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfVLOutOctets.setStatus("current")
_IbIfVLOutPkts_Type = Counter64
_IbIfVLOutPkts_Object = MibTableColumn
ibIfVLOutPkts = _IbIfVLOutPkts_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 4),
    _IbIfVLOutPkts_Type()
)
ibIfVLOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfVLOutPkts.setStatus("current")
_IbIfVLInOctets_Type = Counter64
_IbIfVLInOctets_Object = MibTableColumn
ibIfVLInOctets = _IbIfVLInOctets_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 5),
    _IbIfVLInOctets_Type()
)
ibIfVLInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfVLInOctets.setStatus("current")
_IbIfVLInPkts_Type = Counter64
_IbIfVLInPkts_Object = MibTableColumn
ibIfVLInPkts = _IbIfVLInPkts_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 6),
    _IbIfVLInPkts_Type()
)
ibIfVLInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIfVLInPkts.setStatus("current")
_IbIpoibLinkLayerAddrTable_Object = MibTable
ibIpoibLinkLayerAddrTable = _IbIpoibLinkLayerAddrTable_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ibIpoibLinkLayerAddrTable.setStatus("current")
_IbIpoibLinkLayerAddrEntry_Object = MibTableRow
ibIpoibLinkLayerAddrEntry = _IbIpoibLinkLayerAddrEntry_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 3, 1)
)
ibIpoibLinkLayerAddrEntry.setIndexNames(
    (0, "IB-IF-MIB", "ibIpoibLinkLayerIfIndex"),
    (0, "IB-IF-MIB", "ibIpoibLinkLayerIndex"),
)
if mibBuilder.loadTexts:
    ibIpoibLinkLayerAddrEntry.setStatus("current")
_IbIpoibLinkLayerIfIndex_Type = InterfaceIndex
_IbIpoibLinkLayerIfIndex_Object = MibTableColumn
ibIpoibLinkLayerIfIndex = _IbIpoibLinkLayerIfIndex_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 1),
    _IbIpoibLinkLayerIfIndex_Type()
)
ibIpoibLinkLayerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibIpoibLinkLayerIfIndex.setStatus("current")


class _IbIpoibLinkLayerIndex_Type(Unsigned32):
    """Custom type ibIpoibLinkLayerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbIpoibLinkLayerIndex_Type.__name__ = "Unsigned32"
_IbIpoibLinkLayerIndex_Object = MibTableColumn
ibIpoibLinkLayerIndex = _IbIpoibLinkLayerIndex_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 2),
    _IbIpoibLinkLayerIndex_Type()
)
ibIpoibLinkLayerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibIpoibLinkLayerIndex.setStatus("current")
_IbIpoibLinkLayerAddr_Type = IbIpoibClientIdentifier
_IbIpoibLinkLayerAddr_Object = MibTableColumn
ibIpoibLinkLayerAddr = _IbIpoibLinkLayerAddr_Object(
    (1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 3),
    _IbIpoibLinkLayerAddr_Type()
)
ibIpoibLinkLayerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibIpoibLinkLayerAddr.setStatus("current")
_IbIfNotifications_ObjectIdentity = ObjectIdentity
ibIfNotifications = _IbIfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 2, 2)
)
_IbIfConformance_ObjectIdentity = ObjectIdentity
ibIfConformance = _IbIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 2, 3)
)
_IbIfCompliances_ObjectIdentity = ObjectIdentity
ibIfCompliances = _IbIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 2, 3, 1)
)
_IbIfMIBGroups_ObjectIdentity = ObjectIdentity
ibIfMIBGroups = _IbIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 2, 3, 2)
)

# Managed Objects groups

ibIfStatMandatoryPortStatGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 2, 3, 2, 1)
)
ibIfStatMandatoryPortStatGroup.setObjects(
      *(("IB-IF-MIB", "ibIfPortSymbolErrs"),
        ("IB-IF-MIB", "ibIfPortLinkErrRecovery"),
        ("IB-IF-MIB", "ibIfPortLinkDowned"),
        ("IB-IF-MIB", "ibIfPortStatRcvRemPhyErrs"),
        ("IB-IF-MIB", "ibIfPortStatRcvConstrErrs"),
        ("IB-IF-MIB", "ibIfPortStatLinkIntergrityErrs"),
        ("IB-IF-MIB", "ibIfPortStatExcBufOverrunErrs"),
        ("IB-IF-MIB", "ibIfPortStatVL15Dropped"))
)
if mibBuilder.loadTexts:
    ibIfStatMandatoryPortStatGroup.setStatus("current")

ibIfStatOptionalPortStatGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 2, 3, 2, 2)
)
ibIfStatOptionalPortStatGroup.setObjects(
      *(("IB-IF-MIB", "ibIfPortStatLocalPhyErrs"),
        ("IB-IF-MIB", "ibIfPortStatMalPktErrs"),
        ("IB-IF-MIB", "ibIfPortStatInactDiscards"),
        ("IB-IF-MIB", "ibIfPortStatNeighMTUDiscards"),
        ("IB-IF-MIB", "ibIfPortStatSwLifetimeDiscards"),
        ("IB-IF-MIB", "ibIfPortStatHOQLifetimeDiscards"))
)
if mibBuilder.loadTexts:
    ibIfStatOptionalPortStatGroup.setStatus("current")

ibIfVLTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 2, 3, 2, 3)
)
ibIfVLTrafficGroup.setObjects(
      *(("IB-IF-MIB", "ibIfVLOutOctets"),
        ("IB-IF-MIB", "ibIfVLOutPkts"),
        ("IB-IF-MIB", "ibIfVLInOctets"),
        ("IB-IF-MIB", "ibIfVLInPkts"))
)
if mibBuilder.loadTexts:
    ibIfVLTrafficGroup.setStatus("current")

ibIpoibLinkAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 2, 3, 2, 4)
)
ibIpoibLinkAddrGroup.setObjects(
    ("IB-IF-MIB", "ibIpoibLinkLayerAddr")
)
if mibBuilder.loadTexts:
    ibIpoibLinkAddrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibIfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibIfBasicCompliance.setStatus(
        "current"
    )

ibIfFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibIfFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-IF-MIB",
    **{"ibIfMIB": ibIfMIB,
       "ibIfObjects": ibIfObjects,
       "ibIfPortStatTable": ibIfPortStatTable,
       "ibIfPortStatEntry": ibIfPortStatEntry,
       "ibIfPortStatIfIndex": ibIfPortStatIfIndex,
       "ibIfPortSymbolErrs": ibIfPortSymbolErrs,
       "ibIfPortLinkErrRecovery": ibIfPortLinkErrRecovery,
       "ibIfPortLinkDowned": ibIfPortLinkDowned,
       "ibIfPortStatLocalPhyErrs": ibIfPortStatLocalPhyErrs,
       "ibIfPortStatMalPktErrs": ibIfPortStatMalPktErrs,
       "ibIfPortStatRcvRemPhyErrs": ibIfPortStatRcvRemPhyErrs,
       "ibIfPortStatRcvConstrErrs": ibIfPortStatRcvConstrErrs,
       "ibIfPortStatInactDiscards": ibIfPortStatInactDiscards,
       "ibIfPortStatNeighMTUDiscards": ibIfPortStatNeighMTUDiscards,
       "ibIfPortStatSwLifetimeDiscards": ibIfPortStatSwLifetimeDiscards,
       "ibIfPortStatHOQLifetimeDiscards": ibIfPortStatHOQLifetimeDiscards,
       "ibIfPortStatLinkIntergrityErrs": ibIfPortStatLinkIntergrityErrs,
       "ibIfPortStatExcBufOverrunErrs": ibIfPortStatExcBufOverrunErrs,
       "ibIfPortStatVL15Dropped": ibIfPortStatVL15Dropped,
       "ibIfVLTrafficTable": ibIfVLTrafficTable,
       "ibIfVLTrafficEntry": ibIfVLTrafficEntry,
       "ibIfVLTrafficIfIndex": ibIfVLTrafficIfIndex,
       "ibIfVLIndex": ibIfVLIndex,
       "ibIfVLOutOctets": ibIfVLOutOctets,
       "ibIfVLOutPkts": ibIfVLOutPkts,
       "ibIfVLInOctets": ibIfVLInOctets,
       "ibIfVLInPkts": ibIfVLInPkts,
       "ibIpoibLinkLayerAddrTable": ibIpoibLinkLayerAddrTable,
       "ibIpoibLinkLayerAddrEntry": ibIpoibLinkLayerAddrEntry,
       "ibIpoibLinkLayerIfIndex": ibIpoibLinkLayerIfIndex,
       "ibIpoibLinkLayerIndex": ibIpoibLinkLayerIndex,
       "ibIpoibLinkLayerAddr": ibIpoibLinkLayerAddr,
       "ibIfNotifications": ibIfNotifications,
       "ibIfConformance": ibIfConformance,
       "ibIfCompliances": ibIfCompliances,
       "ibIfBasicCompliance": ibIfBasicCompliance,
       "ibIfFullCompliance": ibIfFullCompliance,
       "ibIfMIBGroups": ibIfMIBGroups,
       "ibIfStatMandatoryPortStatGroup": ibIfStatMandatoryPortStatGroup,
       "ibIfStatOptionalPortStatGroup": ibIfStatOptionalPortStatGroup,
       "ibIfVLTrafficGroup": ibIfVLTrafficGroup,
       "ibIpoibLinkAddrGroup": ibIpoibLinkAddrGroup}
)
