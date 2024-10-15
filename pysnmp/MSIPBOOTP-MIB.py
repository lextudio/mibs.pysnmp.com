# SNMP MIB module (MSIPBOOTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSIPBOOTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:57 2024
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Msipbootp_ObjectIdentity = ObjectIdentity
msipbootp = _Msipbootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 12)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1)
)


class _GlobalLoggingLevel_Type(Integer32):
    """Custom type globalLoggingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("information", 4),
          ("none", 1),
          ("warning", 3))
    )


_GlobalLoggingLevel_Type.__name__ = "Integer32"
_GlobalLoggingLevel_Object = MibScalar
globalLoggingLevel = _GlobalLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 1),
    _GlobalLoggingLevel_Type()
)
globalLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalLoggingLevel.setStatus("mandatory")
_GlobalMaxRecQueueSize_Type = Integer32
_GlobalMaxRecQueueSize_Object = MibScalar
globalMaxRecQueueSize = _GlobalMaxRecQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 2),
    _GlobalMaxRecQueueSize_Type()
)
globalMaxRecQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalMaxRecQueueSize.setStatus("mandatory")
_GlobalServerCount_Type = Integer32
_GlobalServerCount_Object = MibScalar
globalServerCount = _GlobalServerCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 3),
    _GlobalServerCount_Type()
)
globalServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalServerCount.setStatus("mandatory")
_GlobalBOOTPServerTable_Object = MibTable
globalBOOTPServerTable = _GlobalBOOTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    globalBOOTPServerTable.setStatus("mandatory")
_GlobalBOOTPServerEntry_Object = MibTableRow
globalBOOTPServerEntry = _GlobalBOOTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1)
)
globalBOOTPServerEntry.setIndexNames(
    (0, "MSIPBOOTP-MIB", "globalBOOTPServerAddr"),
)
if mibBuilder.loadTexts:
    globalBOOTPServerEntry.setStatus("mandatory")
_GlobalBOOTPServerAddr_Type = IpAddress
_GlobalBOOTPServerAddr_Object = MibTableColumn
globalBOOTPServerAddr = _GlobalBOOTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1, 1),
    _GlobalBOOTPServerAddr_Type()
)
globalBOOTPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalBOOTPServerAddr.setStatus("mandatory")


class _GlobalBOOTPServerTag_Type(Integer32):
    """Custom type globalBOOTPServerTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_GlobalBOOTPServerTag_Type.__name__ = "Integer32"
_GlobalBOOTPServerTag_Object = MibTableColumn
globalBOOTPServerTag = _GlobalBOOTPServerTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1, 2),
    _GlobalBOOTPServerTag_Type()
)
globalBOOTPServerTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalBOOTPServerTag.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2)
)
_IfStatsTable_Object = MibTable
ifStatsTable = _IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ifStatsTable.setStatus("mandatory")
_IfStatsEntry_Object = MibTableRow
ifStatsEntry = _IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1)
)
ifStatsEntry.setIndexNames(
    (0, "MSIPBOOTP-MIB", "ifSEIndex"),
)
if mibBuilder.loadTexts:
    ifStatsEntry.setStatus("mandatory")
_IfSEIndex_Type = Integer32
_IfSEIndex_Object = MibTableColumn
ifSEIndex = _IfSEIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 1),
    _IfSEIndex_Type()
)
ifSEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEIndex.setStatus("mandatory")


class _IfSEState_Type(Integer32):
    """Custom type ifSEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfSEState_Type.__name__ = "Integer32"
_IfSEState_Object = MibTableColumn
ifSEState = _IfSEState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 2),
    _IfSEState_Type()
)
ifSEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEState.setStatus("mandatory")
_IfSESendFailures_Type = Counter32
_IfSESendFailures_Object = MibTableColumn
ifSESendFailures = _IfSESendFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 3),
    _IfSESendFailures_Type()
)
ifSESendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSESendFailures.setStatus("mandatory")
_IfSEReceiveFailures_Type = Counter32
_IfSEReceiveFailures_Object = MibTableColumn
ifSEReceiveFailures = _IfSEReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 4),
    _IfSEReceiveFailures_Type()
)
ifSEReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEReceiveFailures.setStatus("mandatory")
_IfSEArpUpdateFailures_Type = Counter32
_IfSEArpUpdateFailures_Object = MibTableColumn
ifSEArpUpdateFailures = _IfSEArpUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 5),
    _IfSEArpUpdateFailures_Type()
)
ifSEArpUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEArpUpdateFailures.setStatus("mandatory")
_IfSERequestReceiveds_Type = Counter32
_IfSERequestReceiveds_Object = MibTableColumn
ifSERequestReceiveds = _IfSERequestReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 6),
    _IfSERequestReceiveds_Type()
)
ifSERequestReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSERequestReceiveds.setStatus("mandatory")
_IfSERequestDiscards_Type = Counter32
_IfSERequestDiscards_Object = MibTableColumn
ifSERequestDiscards = _IfSERequestDiscards_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 7),
    _IfSERequestDiscards_Type()
)
ifSERequestDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSERequestDiscards.setStatus("mandatory")
_IfSEReplyReceiveds_Type = Counter32
_IfSEReplyReceiveds_Object = MibTableColumn
ifSEReplyReceiveds = _IfSEReplyReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 8),
    _IfSEReplyReceiveds_Type()
)
ifSEReplyReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEReplyReceiveds.setStatus("mandatory")
_IfSEReplyDiscards_Type = Counter32
_IfSEReplyDiscards_Object = MibTableColumn
ifSEReplyDiscards = _IfSEReplyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 9),
    _IfSEReplyDiscards_Type()
)
ifSEReplyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEReplyDiscards.setStatus("mandatory")
_IfConfigTable_Object = MibTable
ifConfigTable = _IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2)
)
if mibBuilder.loadTexts:
    ifConfigTable.setStatus("mandatory")
_IfConfigEntry_Object = MibTableRow
ifConfigEntry = _IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1)
)
ifConfigEntry.setIndexNames(
    (0, "MSIPBOOTP-MIB", "ifCEIndex"),
)
if mibBuilder.loadTexts:
    ifConfigEntry.setStatus("mandatory")
_IfCEIndex_Type = Integer32
_IfCEIndex_Object = MibTableColumn
ifCEIndex = _IfCEIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 1),
    _IfCEIndex_Type()
)
ifCEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCEIndex.setStatus("mandatory")


class _IfCEState_Type(Integer32):
    """Custom type ifCEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfCEState_Type.__name__ = "Integer32"
_IfCEState_Object = MibTableColumn
ifCEState = _IfCEState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 2),
    _IfCEState_Type()
)
ifCEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCEState.setStatus("mandatory")


class _IfCERelayMode_Type(Integer32):
    """Custom type ifCERelayMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IfCERelayMode_Type.__name__ = "Integer32"
_IfCERelayMode_Object = MibTableColumn
ifCERelayMode = _IfCERelayMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 3),
    _IfCERelayMode_Type()
)
ifCERelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCERelayMode.setStatus("mandatory")


class _IfCEMaxHopCount_Type(Integer32):
    """Custom type ifCEMaxHopCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IfCEMaxHopCount_Type.__name__ = "Integer32"
_IfCEMaxHopCount_Object = MibTableColumn
ifCEMaxHopCount = _IfCEMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 4),
    _IfCEMaxHopCount_Type()
)
ifCEMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEMaxHopCount.setStatus("mandatory")


class _IfCEMinSecondsSinceBoot_Type(Integer32):
    """Custom type ifCEMinSecondsSinceBoot based on Integer32"""
    defaultValue = 4


_IfCEMinSecondsSinceBoot_Object = MibTableColumn
ifCEMinSecondsSinceBoot = _IfCEMinSecondsSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 5),
    _IfCEMinSecondsSinceBoot_Type()
)
ifCEMinSecondsSinceBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEMinSecondsSinceBoot.setStatus("mandatory")
_IfBindingTable_Object = MibTable
ifBindingTable = _IfBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3)
)
if mibBuilder.loadTexts:
    ifBindingTable.setStatus("mandatory")
_IfBindingEntry_Object = MibTableRow
ifBindingEntry = _IfBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1)
)
ifBindingEntry.setIndexNames(
    (0, "MSIPBOOTP-MIB", "ifBindingIndex"),
)
if mibBuilder.loadTexts:
    ifBindingEntry.setStatus("mandatory")
_IfBindingIndex_Type = Integer32
_IfBindingIndex_Object = MibTableColumn
ifBindingIndex = _IfBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 1),
    _IfBindingIndex_Type()
)
ifBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingIndex.setStatus("mandatory")


class _IfBindingState_Type(Integer32):
    """Custom type ifBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfBindingState_Type.__name__ = "Integer32"
_IfBindingState_Object = MibTableColumn
ifBindingState = _IfBindingState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 2),
    _IfBindingState_Type()
)
ifBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingState.setStatus("mandatory")
_IfBindingAddrCount_Type = Integer32
_IfBindingAddrCount_Object = MibTableColumn
ifBindingAddrCount = _IfBindingAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 3),
    _IfBindingAddrCount_Type()
)
ifBindingAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingAddrCount.setStatus("mandatory")
_IfAddressTable_Object = MibTable
ifAddressTable = _IfAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4)
)
if mibBuilder.loadTexts:
    ifAddressTable.setStatus("mandatory")
_IfAddressEntry_Object = MibTableRow
ifAddressEntry = _IfAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1)
)
ifAddressEntry.setIndexNames(
    (0, "MSIPBOOTP-MIB", "ifAEIfIndex"),
    (0, "MSIPBOOTP-MIB", "ifAEAddress"),
    (0, "MSIPBOOTP-MIB", "ifAEMask"),
)
if mibBuilder.loadTexts:
    ifAddressEntry.setStatus("mandatory")
_IfAEIfIndex_Type = Integer32
_IfAEIfIndex_Object = MibTableColumn
ifAEIfIndex = _IfAEIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 1),
    _IfAEIfIndex_Type()
)
ifAEIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEIfIndex.setStatus("mandatory")
_IfAEAddress_Type = IpAddress
_IfAEAddress_Object = MibTableColumn
ifAEAddress = _IfAEAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 2),
    _IfAEAddress_Type()
)
ifAEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEAddress.setStatus("mandatory")
_IfAEMask_Type = IpAddress
_IfAEMask_Object = MibTableColumn
ifAEMask = _IfAEMask_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 3),
    _IfAEMask_Type()
)
ifAEMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSIPBOOTP-MIB",
    **{"msipbootp": msipbootp,
       "global": _pysmi_global,
       "globalLoggingLevel": globalLoggingLevel,
       "globalMaxRecQueueSize": globalMaxRecQueueSize,
       "globalServerCount": globalServerCount,
       "globalBOOTPServerTable": globalBOOTPServerTable,
       "globalBOOTPServerEntry": globalBOOTPServerEntry,
       "globalBOOTPServerAddr": globalBOOTPServerAddr,
       "globalBOOTPServerTag": globalBOOTPServerTag,
       "interface": interface,
       "ifStatsTable": ifStatsTable,
       "ifStatsEntry": ifStatsEntry,
       "ifSEIndex": ifSEIndex,
       "ifSEState": ifSEState,
       "ifSESendFailures": ifSESendFailures,
       "ifSEReceiveFailures": ifSEReceiveFailures,
       "ifSEArpUpdateFailures": ifSEArpUpdateFailures,
       "ifSERequestReceiveds": ifSERequestReceiveds,
       "ifSERequestDiscards": ifSERequestDiscards,
       "ifSEReplyReceiveds": ifSEReplyReceiveds,
       "ifSEReplyDiscards": ifSEReplyDiscards,
       "ifConfigTable": ifConfigTable,
       "ifConfigEntry": ifConfigEntry,
       "ifCEIndex": ifCEIndex,
       "ifCEState": ifCEState,
       "ifCERelayMode": ifCERelayMode,
       "ifCEMaxHopCount": ifCEMaxHopCount,
       "ifCEMinSecondsSinceBoot": ifCEMinSecondsSinceBoot,
       "ifBindingTable": ifBindingTable,
       "ifBindingEntry": ifBindingEntry,
       "ifBindingIndex": ifBindingIndex,
       "ifBindingState": ifBindingState,
       "ifBindingAddrCount": ifBindingAddrCount,
       "ifAddressTable": ifAddressTable,
       "ifAddressEntry": ifAddressEntry,
       "ifAEIfIndex": ifAEIfIndex,
       "ifAEAddress": ifAEAddress,
       "ifAEMask": ifAEMask}
)
