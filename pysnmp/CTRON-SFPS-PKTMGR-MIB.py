# SNMP MIB module (CTRON-SFPS-PKTMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-PKTMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:28 2024
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

(sfpsCSPPacket,
 sfpsPktDispatchStats,
 sfpsSwitchSfpsPacket) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsCSPPacket",
    "sfpsPktDispatchStats",
    "sfpsSwitchSfpsPacket")

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


# Types definitions



class SfpsSwitchInstance(Integer32):
    """Custom type SfpsSwitchInstance based on Integer32"""




class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsPacketMgrTable_Object = MibTable
sfpsPacketMgrTable = _SfpsPacketMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    sfpsPacketMgrTable.setStatus("mandatory")
_SfpsPacketMgrEntry_Object = MibTableRow
sfpsPacketMgrEntry = _SfpsPacketMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1)
)
sfpsPacketMgrEntry.setIndexNames(
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrSwitchID"),
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrPacketType"),
)
if mibBuilder.loadTexts:
    sfpsPacketMgrEntry.setStatus("mandatory")
_SfpsPacketMgrSwitchID_Type = Integer32
_SfpsPacketMgrSwitchID_Object = MibTableColumn
sfpsPacketMgrSwitchID = _SfpsPacketMgrSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 1),
    _SfpsPacketMgrSwitchID_Type()
)
sfpsPacketMgrSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrSwitchID.setStatus("mandatory")
_SfpsPacketMgrPacketType_Type = HexInteger
_SfpsPacketMgrPacketType_Object = MibTableColumn
sfpsPacketMgrPacketType = _SfpsPacketMgrPacketType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 2),
    _SfpsPacketMgrPacketType_Type()
)
sfpsPacketMgrPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrPacketType.setStatus("mandatory")
_SfpsPacketMgrTotalPackets_Type = Integer32
_SfpsPacketMgrTotalPackets_Object = MibTableColumn
sfpsPacketMgrTotalPackets = _SfpsPacketMgrTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 3),
    _SfpsPacketMgrTotalPackets_Type()
)
sfpsPacketMgrTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrTotalPackets.setStatus("mandatory")
_SfpsPacketMgrPktsUsed_Type = Integer32
_SfpsPacketMgrPktsUsed_Object = MibTableColumn
sfpsPacketMgrPktsUsed = _SfpsPacketMgrPktsUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 4),
    _SfpsPacketMgrPktsUsed_Type()
)
sfpsPacketMgrPktsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrPktsUsed.setStatus("mandatory")
_SfpsPacketMgrPktsAvailable_Type = Integer32
_SfpsPacketMgrPktsAvailable_Object = MibTableColumn
sfpsPacketMgrPktsAvailable = _SfpsPacketMgrPktsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 5),
    _SfpsPacketMgrPktsAvailable_Type()
)
sfpsPacketMgrPktsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrPktsAvailable.setStatus("mandatory")
_SfpsPacketMgrPktsInUse_Type = Integer32
_SfpsPacketMgrPktsInUse_Object = MibTableColumn
sfpsPacketMgrPktsInUse = _SfpsPacketMgrPktsInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 6),
    _SfpsPacketMgrPktsInUse_Type()
)
sfpsPacketMgrPktsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrPktsInUse.setStatus("mandatory")
_SfpsPacketMgrNotFound_Type = Integer32
_SfpsPacketMgrNotFound_Object = MibTableColumn
sfpsPacketMgrNotFound = _SfpsPacketMgrNotFound_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 8),
    _SfpsPacketMgrNotFound_Type()
)
sfpsPacketMgrNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrNotFound.setStatus("mandatory")
_SfpsPacketMgrTooLarge_Type = Integer32
_SfpsPacketMgrTooLarge_Object = MibTableColumn
sfpsPacketMgrTooLarge = _SfpsPacketMgrTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 9),
    _SfpsPacketMgrTooLarge_Type()
)
sfpsPacketMgrTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketMgrTooLarge.setStatus("mandatory")
_SfpsPacketMgrToCreate_Type = Integer32
_SfpsPacketMgrToCreate_Object = MibTableColumn
sfpsPacketMgrToCreate = _SfpsPacketMgrToCreate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 10),
    _SfpsPacketMgrToCreate_Type()
)
sfpsPacketMgrToCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPacketMgrToCreate.setStatus("mandatory")


class _SfpsPacketMgrReInit_Type(Integer32):
    """Custom type sfpsPacketMgrReInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reinit", 2))
    )


_SfpsPacketMgrReInit_Type.__name__ = "Integer32"
_SfpsPacketMgrReInit_Object = MibTableColumn
sfpsPacketMgrReInit = _SfpsPacketMgrReInit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 11),
    _SfpsPacketMgrReInit_Type()
)
sfpsPacketMgrReInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPacketMgrReInit.setStatus("mandatory")
_SfpsPacketListTable_Object = MibTable
sfpsPacketListTable = _SfpsPacketListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    sfpsPacketListTable.setStatus("mandatory")
_SfpsPacketListEntry_Object = MibTableRow
sfpsPacketListEntry = _SfpsPacketListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1)
)
sfpsPacketListEntry.setIndexNames(
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListPacketType"),
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListSize"),
)
if mibBuilder.loadTexts:
    sfpsPacketListEntry.setStatus("mandatory")
_SfpsPacketListPacketType_Type = HexInteger
_SfpsPacketListPacketType_Object = MibTableColumn
sfpsPacketListPacketType = _SfpsPacketListPacketType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 1),
    _SfpsPacketListPacketType_Type()
)
sfpsPacketListPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListPacketType.setStatus("mandatory")
_SfpsPacketListSize_Type = Integer32
_SfpsPacketListSize_Object = MibTableColumn
sfpsPacketListSize = _SfpsPacketListSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 2),
    _SfpsPacketListSize_Type()
)
sfpsPacketListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListSize.setStatus("mandatory")
_SfpsPacketListTotalPackets_Type = Integer32
_SfpsPacketListTotalPackets_Object = MibTableColumn
sfpsPacketListTotalPackets = _SfpsPacketListTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 3),
    _SfpsPacketListTotalPackets_Type()
)
sfpsPacketListTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListTotalPackets.setStatus("mandatory")
_SfpsPacketListPktsUsed_Type = Integer32
_SfpsPacketListPktsUsed_Object = MibTableColumn
sfpsPacketListPktsUsed = _SfpsPacketListPktsUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 4),
    _SfpsPacketListPktsUsed_Type()
)
sfpsPacketListPktsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListPktsUsed.setStatus("mandatory")
_SfpsPacketListPktsLeft_Type = Integer32
_SfpsPacketListPktsLeft_Object = MibTableColumn
sfpsPacketListPktsLeft = _SfpsPacketListPktsLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 5),
    _SfpsPacketListPktsLeft_Type()
)
sfpsPacketListPktsLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListPktsLeft.setStatus("mandatory")
_SfpsPacketListPktsInUse_Type = Integer32
_SfpsPacketListPktsInUse_Object = MibTableColumn
sfpsPacketListPktsInUse = _SfpsPacketListPktsInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 6),
    _SfpsPacketListPktsInUse_Type()
)
sfpsPacketListPktsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListPktsInUse.setStatus("mandatory")
_SfpsPacketListLowWater_Type = Integer32
_SfpsPacketListLowWater_Object = MibTableColumn
sfpsPacketListLowWater = _SfpsPacketListLowWater_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 7),
    _SfpsPacketListLowWater_Type()
)
sfpsPacketListLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListLowWater.setStatus("mandatory")
_SfpsPacketListNotFound_Type = Integer32
_SfpsPacketListNotFound_Object = MibTableColumn
sfpsPacketListNotFound = _SfpsPacketListNotFound_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 8),
    _SfpsPacketListNotFound_Type()
)
sfpsPacketListNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListNotFound.setStatus("mandatory")


class _SfpsPacketListStatus_Type(Integer32):
    """Custom type sfpsPacketListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SfpsPacketListStatus_Type.__name__ = "Integer32"
_SfpsPacketListStatus_Object = MibTableColumn
sfpsPacketListStatus = _SfpsPacketListStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 9),
    _SfpsPacketListStatus_Type()
)
sfpsPacketListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketListStatus.setStatus("mandatory")
_SfpsPacketSizeTable_Object = MibTable
sfpsPacketSizeTable = _SfpsPacketSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    sfpsPacketSizeTable.setStatus("mandatory")
_SfpsPacketSizeEntry_Object = MibTableRow
sfpsPacketSizeEntry = _SfpsPacketSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1)
)
sfpsPacketSizeEntry.setIndexNames(
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSwitchInstance"),
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSize"),
)
if mibBuilder.loadTexts:
    sfpsPacketSizeEntry.setStatus("mandatory")
_SfpsPacketSizeSwitchInstance_Type = SfpsSwitchInstance
_SfpsPacketSizeSwitchInstance_Object = MibTableColumn
sfpsPacketSizeSwitchInstance = _SfpsPacketSizeSwitchInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 1),
    _SfpsPacketSizeSwitchInstance_Type()
)
sfpsPacketSizeSwitchInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketSizeSwitchInstance.setStatus("mandatory")
_SfpsPacketSizeSize_Type = Integer32
_SfpsPacketSizeSize_Object = MibTableColumn
sfpsPacketSizeSize = _SfpsPacketSizeSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 2),
    _SfpsPacketSizeSize_Type()
)
sfpsPacketSizeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketSizeSize.setStatus("mandatory")
_SfpsPacketSizePktsUsed_Type = Integer32
_SfpsPacketSizePktsUsed_Object = MibTableColumn
sfpsPacketSizePktsUsed = _SfpsPacketSizePktsUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 3),
    _SfpsPacketSizePktsUsed_Type()
)
sfpsPacketSizePktsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketSizePktsUsed.setStatus("mandatory")
_SfpsPacketSizeNotFound_Type = Integer32
_SfpsPacketSizeNotFound_Object = MibTableColumn
sfpsPacketSizeNotFound = _SfpsPacketSizeNotFound_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 4),
    _SfpsPacketSizeNotFound_Type()
)
sfpsPacketSizeNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketSizeNotFound.setStatus("mandatory")
_SfpsPacketQTable_Object = MibTable
sfpsPacketQTable = _SfpsPacketQTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    sfpsPacketQTable.setStatus("mandatory")
_SfpsPacketQEntry_Object = MibTableRow
sfpsPacketQEntry = _SfpsPacketQEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1)
)
sfpsPacketQEntry.setIndexNames(
    (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketQPriorityQ"),
)
if mibBuilder.loadTexts:
    sfpsPacketQEntry.setStatus("mandatory")


class _SfpsPacketQPriorityQ_Type(Integer32):
    """Custom type sfpsPacketQPriorityQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_SfpsPacketQPriorityQ_Type.__name__ = "Integer32"
_SfpsPacketQPriorityQ_Object = MibTableColumn
sfpsPacketQPriorityQ = _SfpsPacketQPriorityQ_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 1),
    _SfpsPacketQPriorityQ_Type()
)
sfpsPacketQPriorityQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketQPriorityQ.setStatus("mandatory")
_SfpsPacketQTotalPackets_Type = Integer32
_SfpsPacketQTotalPackets_Object = MibTableColumn
sfpsPacketQTotalPackets = _SfpsPacketQTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 2),
    _SfpsPacketQTotalPackets_Type()
)
sfpsPacketQTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketQTotalPackets.setStatus("mandatory")
_SfpsPacketQCurrent_Type = Integer32
_SfpsPacketQCurrent_Object = MibTableColumn
sfpsPacketQCurrent = _SfpsPacketQCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 3),
    _SfpsPacketQCurrent_Type()
)
sfpsPacketQCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketQCurrent.setStatus("mandatory")
_SfpsPacketQHighWater_Type = Integer32
_SfpsPacketQHighWater_Object = MibTableColumn
sfpsPacketQHighWater = _SfpsPacketQHighWater_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 4),
    _SfpsPacketQHighWater_Type()
)
sfpsPacketQHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPacketQHighWater.setStatus("mandatory")


class _SfpsPktDispatchStatsVerb_Type(Integer32):
    """Custom type sfpsPktDispatchStatsVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("resetAllStats", 2))
    )


_SfpsPktDispatchStatsVerb_Type.__name__ = "Integer32"
_SfpsPktDispatchStatsVerb_Object = MibScalar
sfpsPktDispatchStatsVerb = _SfpsPktDispatchStatsVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 1),
    _SfpsPktDispatchStatsVerb_Type()
)
sfpsPktDispatchStatsVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPktDispatchStatsVerb.setStatus("mandatory")
_NumHPMInvalidFrameTypeDrops_Type = Integer32
_NumHPMInvalidFrameTypeDrops_Object = MibScalar
numHPMInvalidFrameTypeDrops = _NumHPMInvalidFrameTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 2),
    _NumHPMInvalidFrameTypeDrops_Type()
)
numHPMInvalidFrameTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPMInvalidFrameTypeDrops.setStatus("mandatory")
_NumHPMFilterMgtPortDrops_Type = Integer32
_NumHPMFilterMgtPortDrops_Object = MibScalar
numHPMFilterMgtPortDrops = _NumHPMFilterMgtPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 3),
    _NumHPMFilterMgtPortDrops_Type()
)
numHPMFilterMgtPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPMFilterMgtPortDrops.setStatus("mandatory")
_NumHPMPhysToLogPortDrops_Type = Integer32
_NumHPMPhysToLogPortDrops_Object = MibScalar
numHPMPhysToLogPortDrops = _NumHPMPhysToLogPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 4),
    _NumHPMPhysToLogPortDrops_Type()
)
numHPMPhysToLogPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPMPhysToLogPortDrops.setStatus("mandatory")
_NumHPMNullSFPSPktDrops_Type = Integer32
_NumHPMNullSFPSPktDrops_Object = MibScalar
numHPMNullSFPSPktDrops = _NumHPMNullSFPSPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 5),
    _NumHPMNullSFPSPktDrops_Type()
)
numHPMNullSFPSPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPMNullSFPSPktDrops.setStatus("mandatory")
_NumHPM81fdThrottleDrops_Type = Integer32
_NumHPM81fdThrottleDrops_Object = MibScalar
numHPM81fdThrottleDrops = _NumHPM81fdThrottleDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 6),
    _NumHPM81fdThrottleDrops_Type()
)
numHPM81fdThrottleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPM81fdThrottleDrops.setStatus("mandatory")
_NumHPM81ffThrottleDrops_Type = Integer32
_NumHPM81ffThrottleDrops_Object = MibScalar
numHPM81ffThrottleDrops = _NumHPM81ffThrottleDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 7),
    _NumHPM81ffThrottleDrops_Type()
)
numHPM81ffThrottleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPM81ffThrottleDrops.setStatus("mandatory")
_NumHPMPhysStandbyMaskDrops_Type = Integer32
_NumHPMPhysStandbyMaskDrops_Object = MibScalar
numHPMPhysStandbyMaskDrops = _NumHPMPhysStandbyMaskDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 8),
    _NumHPMPhysStandbyMaskDrops_Type()
)
numHPMPhysStandbyMaskDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPMPhysStandbyMaskDrops.setStatus("mandatory")
_NumBSInvSrcPortDrops_Type = Integer32
_NumBSInvSrcPortDrops_Object = MibScalar
numBSInvSrcPortDrops = _NumBSInvSrcPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 9),
    _NumBSInvSrcPortDrops_Type()
)
numBSInvSrcPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSInvSrcPortDrops.setStatus("mandatory")
_NumBSSourceBlockDrops_Type = Integer32
_NumBSSourceBlockDrops_Object = MibScalar
numBSSourceBlockDrops = _NumBSSourceBlockDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 10),
    _NumBSSourceBlockDrops_Type()
)
numBSSourceBlockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSSourceBlockDrops.setStatus("mandatory")
_NumBSViolationDrops_Type = Integer32
_NumBSViolationDrops_Object = MibScalar
numBSViolationDrops = _NumBSViolationDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 11),
    _NumBSViolationDrops_Type()
)
numBSViolationDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSViolationDrops.setStatus("mandatory")
_NumBSUnknownPortDrops_Type = Integer32
_NumBSUnknownPortDrops_Object = MibScalar
numBSUnknownPortDrops = _NumBSUnknownPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 12),
    _NumBSUnknownPortDrops_Type()
)
numBSUnknownPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSUnknownPortDrops.setStatus("mandatory")
_NumBSStandbyPortDrops_Type = Integer32
_NumBSStandbyPortDrops_Object = MibScalar
numBSStandbyPortDrops = _NumBSStandbyPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 13),
    _NumBSStandbyPortDrops_Type()
)
numBSStandbyPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSStandbyPortDrops.setStatus("mandatory")
_NumBSFabricNghbrPortDrops_Type = Integer32
_NumBSFabricNghbrPortDrops_Object = MibScalar
numBSFabricNghbrPortDrops = _NumBSFabricNghbrPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 14),
    _NumBSFabricNghbrPortDrops_Type()
)
numBSFabricNghbrPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSFabricNghbrPortDrops.setStatus("mandatory")
_NumBSGoingToAccessPortDrops_Type = Integer32
_NumBSGoingToAccessPortDrops_Object = MibScalar
numBSGoingToAccessPortDrops = _NumBSGoingToAccessPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 15),
    _NumBSGoingToAccessPortDrops_Type()
)
numBSGoingToAccessPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSGoingToAccessPortDrops.setStatus("mandatory")
_NumBSInvPortTypeDrops_Type = Integer32
_NumBSInvPortTypeDrops_Object = MibScalar
numBSInvPortTypeDrops = _NumBSInvPortTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 16),
    _NumBSInvPortTypeDrops_Type()
)
numBSInvPortTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSInvPortTypeDrops.setStatus("mandatory")
_NumBSNullCallDrops_Type = Integer32
_NumBSNullCallDrops_Object = MibScalar
numBSNullCallDrops = _NumBSNullCallDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 17),
    _NumBSNullCallDrops_Type()
)
numBSNullCallDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSNullCallDrops.setStatus("mandatory")
_NumBSNullBottomCPDrops_Type = Integer32
_NumBSNullBottomCPDrops_Object = MibScalar
numBSNullBottomCPDrops = _NumBSNullBottomCPDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 18),
    _NumBSNullBottomCPDrops_Type()
)
numBSNullBottomCPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSNullBottomCPDrops.setStatus("mandatory")
_NumBSInvCSPTypeDrops_Type = Integer32
_NumBSInvCSPTypeDrops_Object = MibScalar
numBSInvCSPTypeDrops = _NumBSInvCSPTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 19),
    _NumBSInvCSPTypeDrops_Type()
)
numBSInvCSPTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSInvCSPTypeDrops.setStatus("mandatory")
_NumBSNonHello81fdDrops_Type = Integer32
_NumBSNonHello81fdDrops_Object = MibScalar
numBSNonHello81fdDrops = _NumBSNonHello81fdDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 20),
    _NumBSNonHello81fdDrops_Type()
)
numBSNonHello81fdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSNonHello81fdDrops.setStatus("mandatory")
_NumBSCSPCtrlDisableDrops_Type = Integer32
_NumBSCSPCtrlDisableDrops_Object = MibScalar
numBSCSPCtrlDisableDrops = _NumBSCSPCtrlDisableDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 21),
    _NumBSCSPCtrlDisableDrops_Type()
)
numBSCSPCtrlDisableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSCSPCtrlDisableDrops.setStatus("mandatory")
_NumBSCSPCtrlIndexDrops_Type = Integer32
_NumBSCSPCtrlIndexDrops_Object = MibScalar
numBSCSPCtrlIndexDrops = _NumBSCSPCtrlIndexDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 22),
    _NumBSCSPCtrlIndexDrops_Type()
)
numBSCSPCtrlIndexDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBSCSPCtrlIndexDrops.setStatus("mandatory")
_NumBCPNullCallDrops_Type = Integer32
_NumBCPNullCallDrops_Object = MibScalar
numBCPNullCallDrops = _NumBCPNullCallDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 23),
    _NumBCPNullCallDrops_Type()
)
numBCPNullCallDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPNullCallDrops.setStatus("mandatory")
_NumBCPCPFaultedDrops_Type = Integer32
_NumBCPCPFaultedDrops_Object = MibScalar
numBCPCPFaultedDrops = _NumBCPCPFaultedDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 24),
    _NumBCPCPFaultedDrops_Type()
)
numBCPCPFaultedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPCPFaultedDrops.setStatus("mandatory")
_NumBCPGleanFailDrops_Type = Integer32
_NumBCPGleanFailDrops_Object = MibScalar
numBCPGleanFailDrops = _NumBCPGleanFailDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 25),
    _NumBCPGleanFailDrops_Type()
)
numBCPGleanFailDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPGleanFailDrops.setStatus("mandatory")
_NumBCPCPHaltedDrops_Type = Integer32
_NumBCPCPHaltedDrops_Object = MibScalar
numBCPCPHaltedDrops = _NumBCPCPHaltedDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 26),
    _NumBCPCPHaltedDrops_Type()
)
numBCPCPHaltedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPCPHaltedDrops.setStatus("mandatory")
_NumBCPSwitchedBCADrops_Type = Integer32
_NumBCPSwitchedBCADrops_Object = MibScalar
numBCPSwitchedBCADrops = _NumBCPSwitchedBCADrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 27),
    _NumBCPSwitchedBCADrops_Type()
)
numBCPSwitchedBCADrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPSwitchedBCADrops.setStatus("mandatory")
_NumBCPCallNotAcceptedDrops_Type = Integer32
_NumBCPCallNotAcceptedDrops_Object = MibScalar
numBCPCallNotAcceptedDrops = _NumBCPCallNotAcceptedDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 28),
    _NumBCPCallNotAcceptedDrops_Type()
)
numBCPCallNotAcceptedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBCPCallNotAcceptedDrops.setStatus("mandatory")
_NumHPM81fdNullPktDrops_Type = Integer32
_NumHPM81fdNullPktDrops_Object = MibScalar
numHPM81fdNullPktDrops = _NumHPM81fdNullPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 29),
    _NumHPM81fdNullPktDrops_Type()
)
numHPM81fdNullPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPM81fdNullPktDrops.setStatus("mandatory")
_NumHPM81fdHelloNullPktDrops_Type = Integer32
_NumHPM81fdHelloNullPktDrops_Object = MibScalar
numHPM81fdHelloNullPktDrops = _NumHPM81fdHelloNullPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 30),
    _NumHPM81fdHelloNullPktDrops_Type()
)
numHPM81fdHelloNullPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHPM81fdHelloNullPktDrops.setStatus("mandatory")
_SfpsCSPPacketStatsPacketsSentBad_Type = Integer32
_SfpsCSPPacketStatsPacketsSentBad_Object = MibScalar
sfpsCSPPacketStatsPacketsSentBad = _SfpsCSPPacketStatsPacketsSentBad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 1),
    _SfpsCSPPacketStatsPacketsSentBad_Type()
)
sfpsCSPPacketStatsPacketsSentBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPPacketStatsPacketsSentBad.setStatus("mandatory")
_SfpsCSPPacketStatsPacketsSentGood_Type = Integer32
_SfpsCSPPacketStatsPacketsSentGood_Object = MibScalar
sfpsCSPPacketStatsPacketsSentGood = _SfpsCSPPacketStatsPacketsSentGood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 2),
    _SfpsCSPPacketStatsPacketsSentGood_Type()
)
sfpsCSPPacketStatsPacketsSentGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPPacketStatsPacketsSentGood.setStatus("mandatory")
_SfpsCSPPacketStatsPacketsReceivedBad_Type = Integer32
_SfpsCSPPacketStatsPacketsReceivedBad_Object = MibScalar
sfpsCSPPacketStatsPacketsReceivedBad = _SfpsCSPPacketStatsPacketsReceivedBad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 3),
    _SfpsCSPPacketStatsPacketsReceivedBad_Type()
)
sfpsCSPPacketStatsPacketsReceivedBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPPacketStatsPacketsReceivedBad.setStatus("mandatory")
_SfpsCSPPacketStatsPacketsReceivedGood_Type = Integer32
_SfpsCSPPacketStatsPacketsReceivedGood_Object = MibScalar
sfpsCSPPacketStatsPacketsReceivedGood = _SfpsCSPPacketStatsPacketsReceivedGood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 4),
    _SfpsCSPPacketStatsPacketsReceivedGood_Type()
)
sfpsCSPPacketStatsPacketsReceivedGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPPacketStatsPacketsReceivedGood.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-PKTMGR-MIB",
    **{"SfpsSwitchInstance": SfpsSwitchInstance,
       "HexInteger": HexInteger,
       "sfpsPacketMgrTable": sfpsPacketMgrTable,
       "sfpsPacketMgrEntry": sfpsPacketMgrEntry,
       "sfpsPacketMgrSwitchID": sfpsPacketMgrSwitchID,
       "sfpsPacketMgrPacketType": sfpsPacketMgrPacketType,
       "sfpsPacketMgrTotalPackets": sfpsPacketMgrTotalPackets,
       "sfpsPacketMgrPktsUsed": sfpsPacketMgrPktsUsed,
       "sfpsPacketMgrPktsAvailable": sfpsPacketMgrPktsAvailable,
       "sfpsPacketMgrPktsInUse": sfpsPacketMgrPktsInUse,
       "sfpsPacketMgrNotFound": sfpsPacketMgrNotFound,
       "sfpsPacketMgrTooLarge": sfpsPacketMgrTooLarge,
       "sfpsPacketMgrToCreate": sfpsPacketMgrToCreate,
       "sfpsPacketMgrReInit": sfpsPacketMgrReInit,
       "sfpsPacketListTable": sfpsPacketListTable,
       "sfpsPacketListEntry": sfpsPacketListEntry,
       "sfpsPacketListPacketType": sfpsPacketListPacketType,
       "sfpsPacketListSize": sfpsPacketListSize,
       "sfpsPacketListTotalPackets": sfpsPacketListTotalPackets,
       "sfpsPacketListPktsUsed": sfpsPacketListPktsUsed,
       "sfpsPacketListPktsLeft": sfpsPacketListPktsLeft,
       "sfpsPacketListPktsInUse": sfpsPacketListPktsInUse,
       "sfpsPacketListLowWater": sfpsPacketListLowWater,
       "sfpsPacketListNotFound": sfpsPacketListNotFound,
       "sfpsPacketListStatus": sfpsPacketListStatus,
       "sfpsPacketSizeTable": sfpsPacketSizeTable,
       "sfpsPacketSizeEntry": sfpsPacketSizeEntry,
       "sfpsPacketSizeSwitchInstance": sfpsPacketSizeSwitchInstance,
       "sfpsPacketSizeSize": sfpsPacketSizeSize,
       "sfpsPacketSizePktsUsed": sfpsPacketSizePktsUsed,
       "sfpsPacketSizeNotFound": sfpsPacketSizeNotFound,
       "sfpsPacketQTable": sfpsPacketQTable,
       "sfpsPacketQEntry": sfpsPacketQEntry,
       "sfpsPacketQPriorityQ": sfpsPacketQPriorityQ,
       "sfpsPacketQTotalPackets": sfpsPacketQTotalPackets,
       "sfpsPacketQCurrent": sfpsPacketQCurrent,
       "sfpsPacketQHighWater": sfpsPacketQHighWater,
       "sfpsPktDispatchStatsVerb": sfpsPktDispatchStatsVerb,
       "numHPMInvalidFrameTypeDrops": numHPMInvalidFrameTypeDrops,
       "numHPMFilterMgtPortDrops": numHPMFilterMgtPortDrops,
       "numHPMPhysToLogPortDrops": numHPMPhysToLogPortDrops,
       "numHPMNullSFPSPktDrops": numHPMNullSFPSPktDrops,
       "numHPM81fdThrottleDrops": numHPM81fdThrottleDrops,
       "numHPM81ffThrottleDrops": numHPM81ffThrottleDrops,
       "numHPMPhysStandbyMaskDrops": numHPMPhysStandbyMaskDrops,
       "numBSInvSrcPortDrops": numBSInvSrcPortDrops,
       "numBSSourceBlockDrops": numBSSourceBlockDrops,
       "numBSViolationDrops": numBSViolationDrops,
       "numBSUnknownPortDrops": numBSUnknownPortDrops,
       "numBSStandbyPortDrops": numBSStandbyPortDrops,
       "numBSFabricNghbrPortDrops": numBSFabricNghbrPortDrops,
       "numBSGoingToAccessPortDrops": numBSGoingToAccessPortDrops,
       "numBSInvPortTypeDrops": numBSInvPortTypeDrops,
       "numBSNullCallDrops": numBSNullCallDrops,
       "numBSNullBottomCPDrops": numBSNullBottomCPDrops,
       "numBSInvCSPTypeDrops": numBSInvCSPTypeDrops,
       "numBSNonHello81fdDrops": numBSNonHello81fdDrops,
       "numBSCSPCtrlDisableDrops": numBSCSPCtrlDisableDrops,
       "numBSCSPCtrlIndexDrops": numBSCSPCtrlIndexDrops,
       "numBCPNullCallDrops": numBCPNullCallDrops,
       "numBCPCPFaultedDrops": numBCPCPFaultedDrops,
       "numBCPGleanFailDrops": numBCPGleanFailDrops,
       "numBCPCPHaltedDrops": numBCPCPHaltedDrops,
       "numBCPSwitchedBCADrops": numBCPSwitchedBCADrops,
       "numBCPCallNotAcceptedDrops": numBCPCallNotAcceptedDrops,
       "numHPM81fdNullPktDrops": numHPM81fdNullPktDrops,
       "numHPM81fdHelloNullPktDrops": numHPM81fdHelloNullPktDrops,
       "sfpsCSPPacketStatsPacketsSentBad": sfpsCSPPacketStatsPacketsSentBad,
       "sfpsCSPPacketStatsPacketsSentGood": sfpsCSPPacketStatsPacketsSentGood,
       "sfpsCSPPacketStatsPacketsReceivedBad": sfpsCSPPacketStatsPacketsReceivedBad,
       "sfpsCSPPacketStatsPacketsReceivedGood": sfpsCSPPacketStatsPacketsReceivedGood}
)
