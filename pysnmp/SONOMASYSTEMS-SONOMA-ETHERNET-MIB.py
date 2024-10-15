# SNMP MIB module (SONOMASYSTEMS-SONOMA-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:44 2024
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

(sonomaLAN,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaLAN")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaEthernet_ObjectIdentity = ObjectIdentity
sonomaEthernet = _SonomaEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1)
)
_EthernetAdapterGroup_ObjectIdentity = ObjectIdentity
ethernetAdapterGroup = _EthernetAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1)
)
_EnetSMCGroup_ObjectIdentity = ObjectIdentity
enetSMCGroup = _EnetSMCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1)
)
_EnetSMCConfigTable_Object = MibTable
enetSMCConfigTable = _EnetSMCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    enetSMCConfigTable.setStatus("mandatory")
_EnetSMCConfigEntry_Object = MibTableRow
enetSMCConfigEntry = _EnetSMCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1, 1)
)
enetSMCConfigEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ETHERNET-MIB", "enetSMCConfigIndex"),
)
if mibBuilder.loadTexts:
    enetSMCConfigEntry.setStatus("mandatory")
_EnetSMCConfigIndex_Type = Integer32
_EnetSMCConfigIndex_Object = MibTableColumn
enetSMCConfigIndex = _EnetSMCConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1, 1, 1),
    _EnetSMCConfigIndex_Type()
)
enetSMCConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCConfigIndex.setStatus("mandatory")


class _EnetSMCConfigLineSpeed_Type(Integer32):
    """Custom type enetSMCConfigLineSpeed based on Integer32"""
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
        *(("speed100Mbps", 2),
          ("speed10Mbps", 1),
          ("speedAuto", 3))
    )


_EnetSMCConfigLineSpeed_Type.__name__ = "Integer32"
_EnetSMCConfigLineSpeed_Object = MibTableColumn
enetSMCConfigLineSpeed = _EnetSMCConfigLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1, 1, 2),
    _EnetSMCConfigLineSpeed_Type()
)
enetSMCConfigLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetSMCConfigLineSpeed.setStatus("mandatory")


class _EnetSMCConfigInterface_Type(Integer32):
    """Custom type enetSMCConfigInterface based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("auto", 5),
          ("bnc", 4),
          ("twistedPair", 2),
          ("utp", 3))
    )


_EnetSMCConfigInterface_Type.__name__ = "Integer32"
_EnetSMCConfigInterface_Object = MibTableColumn
enetSMCConfigInterface = _EnetSMCConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1, 1, 3),
    _EnetSMCConfigInterface_Type()
)
enetSMCConfigInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetSMCConfigInterface.setStatus("mandatory")


class _EnetSMCConfigMode_Type(Integer32):
    """Custom type enetSMCConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_EnetSMCConfigMode_Type.__name__ = "Integer32"
_EnetSMCConfigMode_Object = MibTableColumn
enetSMCConfigMode = _EnetSMCConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 1, 1, 4),
    _EnetSMCConfigMode_Type()
)
enetSMCConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetSMCConfigMode.setStatus("mandatory")
_EnetSMCStatsTable_Object = MibTable
enetSMCStatsTable = _EnetSMCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    enetSMCStatsTable.setStatus("mandatory")
_EnetSMCStatsEntry_Object = MibTableRow
enetSMCStatsEntry = _EnetSMCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1)
)
enetSMCStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ETHERNET-MIB", "enetSMCStatsIndex"),
)
if mibBuilder.loadTexts:
    enetSMCStatsEntry.setStatus("mandatory")
_EnetSMCStatsIndex_Type = Integer32
_EnetSMCStatsIndex_Object = MibTableColumn
enetSMCStatsIndex = _EnetSMCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 1),
    _EnetSMCStatsIndex_Type()
)
enetSMCStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCStatsIndex.setStatus("mandatory")
_EnetSMCSQEErrors_Type = Counter32
_EnetSMCSQEErrors_Object = MibTableColumn
enetSMCSQEErrors = _EnetSMCSQEErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 2),
    _EnetSMCSQEErrors_Type()
)
enetSMCSQEErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCSQEErrors.setStatus("mandatory")
_EnetSMCRxMissedFrames_Type = Counter32
_EnetSMCRxMissedFrames_Object = MibTableColumn
enetSMCRxMissedFrames = _EnetSMCRxMissedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 3),
    _EnetSMCRxMissedFrames_Type()
)
enetSMCRxMissedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCRxMissedFrames.setStatus("mandatory")
_EnetSMCRetries_Type = Counter32
_EnetSMCRetries_Object = MibTableColumn
enetSMCRetries = _EnetSMCRetries_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 4),
    _EnetSMCRetries_Type()
)
enetSMCRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCRetries.setStatus("mandatory")
_EnetSMCCollisions_Type = Counter32
_EnetSMCCollisions_Object = MibTableColumn
enetSMCCollisions = _EnetSMCCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 5),
    _EnetSMCCollisions_Type()
)
enetSMCCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCCollisions.setStatus("mandatory")
_EnetSMCRunts_Type = Counter32
_EnetSMCRunts_Object = MibTableColumn
enetSMCRunts = _EnetSMCRunts_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 6),
    _EnetSMCRunts_Type()
)
enetSMCRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCRunts.setStatus("mandatory")
_EnetSMCFRAMorCRCErrors_Type = Counter32
_EnetSMCFRAMorCRCErrors_Object = MibTableColumn
enetSMCFRAMorCRCErrors = _EnetSMCFRAMorCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 7),
    _EnetSMCFRAMorCRCErrors_Type()
)
enetSMCFRAMorCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCFRAMorCRCErrors.setStatus("mandatory")
_EnetSMCTxDeferrals_Type = Counter32
_EnetSMCTxDeferrals_Object = MibTableColumn
enetSMCTxDeferrals = _EnetSMCTxDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 8),
    _EnetSMCTxDeferrals_Type()
)
enetSMCTxDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCTxDeferrals.setStatus("mandatory")
_EnetSMCLateCollisions_Type = Counter32
_EnetSMCLateCollisions_Object = MibTableColumn
enetSMCLateCollisions = _EnetSMCLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 9),
    _EnetSMCLateCollisions_Type()
)
enetSMCLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLateCollisions.setStatus("mandatory")
_EnetSMCLossofCarrierErrors_Type = Counter32
_EnetSMCLossofCarrierErrors_Object = MibTableColumn
enetSMCLossofCarrierErrors = _EnetSMCLossofCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 10),
    _EnetSMCLossofCarrierErrors_Type()
)
enetSMCLossofCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLossofCarrierErrors.setStatus("mandatory")
_EnetSMCRetryErrors_Type = Counter32
_EnetSMCRetryErrors_Object = MibTableColumn
enetSMCRetryErrors = _EnetSMCRetryErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 11),
    _EnetSMCRetryErrors_Type()
)
enetSMCRetryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCRetryErrors.setStatus("mandatory")
_EnetSMCNoOfLinkResets_Type = Counter32
_EnetSMCNoOfLinkResets_Object = MibTableColumn
enetSMCNoOfLinkResets = _EnetSMCNoOfLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 18),
    _EnetSMCNoOfLinkResets_Type()
)
enetSMCNoOfLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCNoOfLinkResets.setStatus("mandatory")


class _EnetSMCLastLinkResetReason_Type(Integer32):
    """Custom type enetSMCLastLinkResetReason based on Integer32"""
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
        *(("cableDrop", 4),
          ("deviceReset", 3),
          ("management", 2),
          ("noReason", 1))
    )


_EnetSMCLastLinkResetReason_Type.__name__ = "Integer32"
_EnetSMCLastLinkResetReason_Object = MibTableColumn
enetSMCLastLinkResetReason = _EnetSMCLastLinkResetReason_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 19),
    _EnetSMCLastLinkResetReason_Type()
)
enetSMCLastLinkResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLastLinkResetReason.setStatus("mandatory")
_EnetSMCTimeSinceLastLinkReset_Type = Integer32
_EnetSMCTimeSinceLastLinkReset_Object = MibTableColumn
enetSMCTimeSinceLastLinkReset = _EnetSMCTimeSinceLastLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 20),
    _EnetSMCTimeSinceLastLinkReset_Type()
)
enetSMCTimeSinceLastLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCTimeSinceLastLinkReset.setStatus("mandatory")
_EnetSMCRxPackets_Type = Counter32
_EnetSMCRxPackets_Object = MibTableColumn
enetSMCRxPackets = _EnetSMCRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 2, 1, 21),
    _EnetSMCRxPackets_Type()
)
enetSMCRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCRxPackets.setStatus("mandatory")
_EnetSMCStatusTable_Object = MibTable
enetSMCStatusTable = _EnetSMCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    enetSMCStatusTable.setStatus("mandatory")
_EnetSMCStatusEntry_Object = MibTableRow
enetSMCStatusEntry = _EnetSMCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 3, 1)
)
enetSMCStatusEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ETHERNET-MIB", "enetSMCStatsIndex"),
)
if mibBuilder.loadTexts:
    enetSMCStatusEntry.setStatus("mandatory")


class _EnetSMCLineSpeed_Type(Integer32):
    """Custom type enetSMCLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100Mbps", 2),
          ("speed10Mbps", 1),
          ("speedAuto", 3))
    )


_EnetSMCLineSpeed_Type.__name__ = "Integer32"
_EnetSMCLineSpeed_Object = MibTableColumn
enetSMCLineSpeed = _EnetSMCLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 3, 1, 1),
    _EnetSMCLineSpeed_Type()
)
enetSMCLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLineSpeed.setStatus("mandatory")


class _EnetSMCLineMode_Type(Integer32):
    """Custom type enetSMCLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_EnetSMCLineMode_Type.__name__ = "Integer32"
_EnetSMCLineMode_Object = MibTableColumn
enetSMCLineMode = _EnetSMCLineMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 3, 1, 2),
    _EnetSMCLineMode_Type()
)
enetSMCLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLineMode.setStatus("mandatory")


class _EnetSMCLineInterface_Type(Integer32):
    """Custom type enetSMCLineInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("auto", 5),
          ("bnc", 4),
          ("twistedPair", 2),
          ("utp", 3))
    )


_EnetSMCLineInterface_Type.__name__ = "Integer32"
_EnetSMCLineInterface_Object = MibTableColumn
enetSMCLineInterface = _EnetSMCLineInterface_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 1, 1, 1, 3, 1, 3),
    _EnetSMCLineInterface_Type()
)
enetSMCLineInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMCLineInterface.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ETHERNET-MIB",
    **{"sonomaEthernet": sonomaEthernet,
       "ethernetAdapterGroup": ethernetAdapterGroup,
       "enetSMCGroup": enetSMCGroup,
       "enetSMCConfigTable": enetSMCConfigTable,
       "enetSMCConfigEntry": enetSMCConfigEntry,
       "enetSMCConfigIndex": enetSMCConfigIndex,
       "enetSMCConfigLineSpeed": enetSMCConfigLineSpeed,
       "enetSMCConfigInterface": enetSMCConfigInterface,
       "enetSMCConfigMode": enetSMCConfigMode,
       "enetSMCStatsTable": enetSMCStatsTable,
       "enetSMCStatsEntry": enetSMCStatsEntry,
       "enetSMCStatsIndex": enetSMCStatsIndex,
       "enetSMCSQEErrors": enetSMCSQEErrors,
       "enetSMCRxMissedFrames": enetSMCRxMissedFrames,
       "enetSMCRetries": enetSMCRetries,
       "enetSMCCollisions": enetSMCCollisions,
       "enetSMCRunts": enetSMCRunts,
       "enetSMCFRAMorCRCErrors": enetSMCFRAMorCRCErrors,
       "enetSMCTxDeferrals": enetSMCTxDeferrals,
       "enetSMCLateCollisions": enetSMCLateCollisions,
       "enetSMCLossofCarrierErrors": enetSMCLossofCarrierErrors,
       "enetSMCRetryErrors": enetSMCRetryErrors,
       "enetSMCNoOfLinkResets": enetSMCNoOfLinkResets,
       "enetSMCLastLinkResetReason": enetSMCLastLinkResetReason,
       "enetSMCTimeSinceLastLinkReset": enetSMCTimeSinceLastLinkReset,
       "enetSMCRxPackets": enetSMCRxPackets,
       "enetSMCStatusTable": enetSMCStatusTable,
       "enetSMCStatusEntry": enetSMCStatusEntry,
       "enetSMCLineSpeed": enetSMCLineSpeed,
       "enetSMCLineMode": enetSMCLineMode,
       "enetSMCLineInterface": enetSMCLineInterface}
)
