# SNMP MIB module (DNOS-PFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-PFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:10 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathPFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47)
)
fastPathPFC.setRevisions(
        ("2011-01-26 00:00",
         "2009-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentPfcCfgGroup_ObjectIdentity = ObjectIdentity
agentPfcCfgGroup = _AgentPfcCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1)
)
_AgentPfcTable_Object = MibTable
agentPfcTable = _AgentPfcTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1)
)
if mibBuilder.loadTexts:
    agentPfcTable.setStatus("current")
_AgentPfcEntry_Object = MibTableRow
agentPfcEntry = _AgentPfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1)
)
agentPfcEntry.setIndexNames(
    (0, "DNOS-PFC-MIB", "agentPfcIntfIndex"),
)
if mibBuilder.loadTexts:
    agentPfcEntry.setStatus("current")
_AgentPfcIntfIndex_Type = InterfaceIndex
_AgentPfcIntfIndex_Object = MibTableColumn
agentPfcIntfIndex = _AgentPfcIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 1),
    _AgentPfcIntfIndex_Type()
)
agentPfcIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPfcIntfIndex.setStatus("current")


class _AgentPfcIntfAdminMode_Type(Integer32):
    """Custom type agentPfcIntfAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPfcIntfAdminMode_Type.__name__ = "Integer32"
_AgentPfcIntfAdminMode_Object = MibTableColumn
agentPfcIntfAdminMode = _AgentPfcIntfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 2),
    _AgentPfcIntfAdminMode_Type()
)
agentPfcIntfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPfcIntfAdminMode.setStatus("current")


class _AgentPfcIntfPfcStatus_Type(Integer32):
    """Custom type agentPfcIntfPfcStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentPfcIntfPfcStatus_Type.__name__ = "Integer32"
_AgentPfcIntfPfcStatus_Object = MibTableColumn
agentPfcIntfPfcStatus = _AgentPfcIntfPfcStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 3),
    _AgentPfcIntfPfcStatus_Type()
)
agentPfcIntfPfcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPfcStatus.setStatus("current")
_AgentPfcTotalIntfPfcFramesRx_Type = Unsigned32
_AgentPfcTotalIntfPfcFramesRx_Object = MibTableColumn
agentPfcTotalIntfPfcFramesRx = _AgentPfcTotalIntfPfcFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 4),
    _AgentPfcTotalIntfPfcFramesRx_Type()
)
agentPfcTotalIntfPfcFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcTotalIntfPfcFramesRx.setStatus("current")
_AgentPfcTotalIntfPfcFramesTx_Type = Unsigned32
_AgentPfcTotalIntfPfcFramesTx_Object = MibTableColumn
agentPfcTotalIntfPfcFramesTx = _AgentPfcTotalIntfPfcFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 5),
    _AgentPfcTotalIntfPfcFramesTx_Type()
)
agentPfcTotalIntfPfcFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcTotalIntfPfcFramesTx.setStatus("current")
_AgentPfcIntfLinkDelayAllowance_Type = Unsigned32
_AgentPfcIntfLinkDelayAllowance_Object = MibTableColumn
agentPfcIntfLinkDelayAllowance = _AgentPfcIntfLinkDelayAllowance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 6),
    _AgentPfcIntfLinkDelayAllowance_Type()
)
agentPfcIntfLinkDelayAllowance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfLinkDelayAllowance.setStatus("current")


class _AgentPfcIntfAdvWilling_Type(Integer32):
    """Custom type agentPfcIntfAdvWilling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unwilling", 2),
          ("willing", 1))
    )


_AgentPfcIntfAdvWilling_Type.__name__ = "Integer32"
_AgentPfcIntfAdvWilling_Object = MibTableColumn
agentPfcIntfAdvWilling = _AgentPfcIntfAdvWilling_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 7),
    _AgentPfcIntfAdvWilling_Type()
)
agentPfcIntfAdvWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfAdvWilling.setStatus("current")


class _AgentPfcIntfPeerDetected_Type(Integer32):
    """Custom type agentPfcIntfPeerDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("detected", 1))
    )


_AgentPfcIntfPeerDetected_Type.__name__ = "Integer32"
_AgentPfcIntfPeerDetected_Object = MibTableColumn
agentPfcIntfPeerDetected = _AgentPfcIntfPeerDetected_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 8),
    _AgentPfcIntfPeerDetected_Type()
)
agentPfcIntfPeerDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerDetected.setStatus("current")
_AgentPfcIntfPeerMacAddr_Type = MacAddress
_AgentPfcIntfPeerMacAddr_Object = MibTableColumn
agentPfcIntfPeerMacAddr = _AgentPfcIntfPeerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 9),
    _AgentPfcIntfPeerMacAddr_Type()
)
agentPfcIntfPeerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerMacAddr.setStatus("current")


class _AgentPfcIntfPeerWilling_Type(Integer32):
    """Custom type agentPfcIntfPeerWilling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("unwilling", 3),
          ("willing", 2))
    )


_AgentPfcIntfPeerWilling_Type.__name__ = "Integer32"
_AgentPfcIntfPeerWilling_Object = MibTableColumn
agentPfcIntfPeerWilling = _AgentPfcIntfPeerWilling_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 10),
    _AgentPfcIntfPeerWilling_Type()
)
agentPfcIntfPeerWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerWilling.setStatus("current")


class _AgentPfcIntfPeerMBCStatus_Type(Integer32):
    """Custom type agentPfcIntfPeerMBCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("false", 3),
          ("true", 2))
    )


_AgentPfcIntfPeerMBCStatus_Type.__name__ = "Integer32"
_AgentPfcIntfPeerMBCStatus_Object = MibTableColumn
agentPfcIntfPeerMBCStatus = _AgentPfcIntfPeerMBCStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 11),
    _AgentPfcIntfPeerMBCStatus_Type()
)
agentPfcIntfPeerMBCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerMBCStatus.setStatus("current")
_AgentPfcIntfPeerCapability_Type = Unsigned32
_AgentPfcIntfPeerCapability_Object = MibTableColumn
agentPfcIntfPeerCapability = _AgentPfcIntfPeerCapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 12),
    _AgentPfcIntfPeerCapability_Type()
)
agentPfcIntfPeerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerCapability.setStatus("current")


class _AgentPfcIntfPeerCfgCompatible_Type(Integer32):
    """Custom type agentPfcIntfPeerCfgCompatible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("false", 3),
          ("true", 2))
    )


_AgentPfcIntfPeerCfgCompatible_Type.__name__ = "Integer32"
_AgentPfcIntfPeerCfgCompatible_Object = MibTableColumn
agentPfcIntfPeerCfgCompatible = _AgentPfcIntfPeerCfgCompatible_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 13),
    _AgentPfcIntfPeerCfgCompatible_Type()
)
agentPfcIntfPeerCfgCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerCfgCompatible.setStatus("current")
_AgentPfcIntfPeerCompatibleCfgCount_Type = Unsigned32
_AgentPfcIntfPeerCompatibleCfgCount_Object = MibTableColumn
agentPfcIntfPeerCompatibleCfgCount = _AgentPfcIntfPeerCompatibleCfgCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 14),
    _AgentPfcIntfPeerCompatibleCfgCount_Type()
)
agentPfcIntfPeerCompatibleCfgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerCompatibleCfgCount.setStatus("current")
_AgentPfcIntfPeerIncompatibleCfgCount_Type = Unsigned32
_AgentPfcIntfPeerIncompatibleCfgCount_Object = MibTableColumn
agentPfcIntfPeerIncompatibleCfgCount = _AgentPfcIntfPeerIncompatibleCfgCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 15),
    _AgentPfcIntfPeerIncompatibleCfgCount_Type()
)
agentPfcIntfPeerIncompatibleCfgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPeerIncompatibleCfgCount.setStatus("current")
_AgentPfcActionTable_Object = MibTable
agentPfcActionTable = _AgentPfcActionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2)
)
if mibBuilder.loadTexts:
    agentPfcActionTable.setStatus("current")
_AgentPfcActionEntry_Object = MibTableRow
agentPfcActionEntry = _AgentPfcActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1)
)
agentPfcActionEntry.setIndexNames(
    (0, "DNOS-PFC-MIB", "agentPfcIntfIndex"),
    (0, "DNOS-PFC-MIB", "agentPfcPriority"),
)
if mibBuilder.loadTexts:
    agentPfcActionEntry.setStatus("current")


class _AgentPfcPriority_Type(Unsigned32):
    """Custom type agentPfcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentPfcPriority_Type.__name__ = "Unsigned32"
_AgentPfcPriority_Object = MibTableColumn
agentPfcPriority = _AgentPfcPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 1),
    _AgentPfcPriority_Type()
)
agentPfcPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPfcPriority.setStatus("current")


class _AgentPfcAction_Type(Integer32):
    """Custom type agentPfcAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("nodrop", 2))
    )


_AgentPfcAction_Type.__name__ = "Integer32"
_AgentPfcAction_Object = MibTableColumn
agentPfcAction = _AgentPfcAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 2),
    _AgentPfcAction_Type()
)
agentPfcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPfcAction.setStatus("current")


class _AgentPfcOperAction_Type(Integer32):
    """Custom type agentPfcOperAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("nodrop", 2))
    )


_AgentPfcOperAction_Type.__name__ = "Integer32"
_AgentPfcOperAction_Object = MibTableColumn
agentPfcOperAction = _AgentPfcOperAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 3),
    _AgentPfcOperAction_Type()
)
agentPfcOperAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcOperAction.setStatus("current")


class _AgentPfcAdvAction_Type(Integer32):
    """Custom type agentPfcAdvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("nodrop", 2))
    )


_AgentPfcAdvAction_Type.__name__ = "Integer32"
_AgentPfcAdvAction_Object = MibTableColumn
agentPfcAdvAction = _AgentPfcAdvAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 4),
    _AgentPfcAdvAction_Type()
)
agentPfcAdvAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcAdvAction.setStatus("current")


class _AgentPfcPeerAction_Type(Integer32):
    """Custom type agentPfcPeerAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("drop", 2),
          ("nodrop", 3))
    )


_AgentPfcPeerAction_Type.__name__ = "Integer32"
_AgentPfcPeerAction_Object = MibTableColumn
agentPfcPeerAction = _AgentPfcPeerAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 5),
    _AgentPfcPeerAction_Type()
)
agentPfcPeerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcPeerAction.setStatus("current")
_AgentPfcIntfStatsPerPriorityTable_Object = MibTable
agentPfcIntfStatsPerPriorityTable = _AgentPfcIntfStatsPerPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3)
)
if mibBuilder.loadTexts:
    agentPfcIntfStatsPerPriorityTable.setStatus("current")
_AgentPfcIntfStatsPerPriorityEntry_Object = MibTableRow
agentPfcIntfStatsPerPriorityEntry = _AgentPfcIntfStatsPerPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1)
)
agentPfcIntfStatsPerPriorityEntry.setIndexNames(
    (0, "DNOS-PFC-MIB", "agentPfcIntfIndex"),
    (0, "DNOS-PFC-MIB", "agentPfcPriority"),
)
if mibBuilder.loadTexts:
    agentPfcIntfStatsPerPriorityEntry.setStatus("current")
_AgentPfcIntfPfcPriorityFramesRx_Type = Unsigned32
_AgentPfcIntfPfcPriorityFramesRx_Object = MibTableColumn
agentPfcIntfPfcPriorityFramesRx = _AgentPfcIntfPfcPriorityFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1, 1),
    _AgentPfcIntfPfcPriorityFramesRx_Type()
)
agentPfcIntfPfcPriorityFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPfcPriorityFramesRx.setStatus("current")
_AgentPfcIntfPfcPriorityFramesTx_Type = Unsigned32
_AgentPfcIntfPfcPriorityFramesTx_Object = MibTableColumn
agentPfcIntfPfcPriorityFramesTx = _AgentPfcIntfPfcPriorityFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1, 2),
    _AgentPfcIntfPfcPriorityFramesTx_Type()
)
agentPfcIntfPfcPriorityFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPfcIntfPfcPriorityFramesTx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-PFC-MIB",
    **{"fastPathPFC": fastPathPFC,
       "agentPfcCfgGroup": agentPfcCfgGroup,
       "agentPfcTable": agentPfcTable,
       "agentPfcEntry": agentPfcEntry,
       "agentPfcIntfIndex": agentPfcIntfIndex,
       "agentPfcIntfAdminMode": agentPfcIntfAdminMode,
       "agentPfcIntfPfcStatus": agentPfcIntfPfcStatus,
       "agentPfcTotalIntfPfcFramesRx": agentPfcTotalIntfPfcFramesRx,
       "agentPfcTotalIntfPfcFramesTx": agentPfcTotalIntfPfcFramesTx,
       "agentPfcIntfLinkDelayAllowance": agentPfcIntfLinkDelayAllowance,
       "agentPfcIntfAdvWilling": agentPfcIntfAdvWilling,
       "agentPfcIntfPeerDetected": agentPfcIntfPeerDetected,
       "agentPfcIntfPeerMacAddr": agentPfcIntfPeerMacAddr,
       "agentPfcIntfPeerWilling": agentPfcIntfPeerWilling,
       "agentPfcIntfPeerMBCStatus": agentPfcIntfPeerMBCStatus,
       "agentPfcIntfPeerCapability": agentPfcIntfPeerCapability,
       "agentPfcIntfPeerCfgCompatible": agentPfcIntfPeerCfgCompatible,
       "agentPfcIntfPeerCompatibleCfgCount": agentPfcIntfPeerCompatibleCfgCount,
       "agentPfcIntfPeerIncompatibleCfgCount": agentPfcIntfPeerIncompatibleCfgCount,
       "agentPfcActionTable": agentPfcActionTable,
       "agentPfcActionEntry": agentPfcActionEntry,
       "agentPfcPriority": agentPfcPriority,
       "agentPfcAction": agentPfcAction,
       "agentPfcOperAction": agentPfcOperAction,
       "agentPfcAdvAction": agentPfcAdvAction,
       "agentPfcPeerAction": agentPfcPeerAction,
       "agentPfcIntfStatsPerPriorityTable": agentPfcIntfStatsPerPriorityTable,
       "agentPfcIntfStatsPerPriorityEntry": agentPfcIntfStatsPerPriorityEntry,
       "agentPfcIntfPfcPriorityFramesRx": agentPfcIntfPfcPriorityFramesRx,
       "agentPfcIntfPfcPriorityFramesTx": agentPfcIntfPfcPriorityFramesTx}
)
