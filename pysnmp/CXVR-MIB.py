# SNMP MIB module (CXVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:00 2024
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

(Alias,
 cxVR) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxVR")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrRegTable_Object = MibTable
vrRegTable = _VrRegTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10)
)
if mibBuilder.loadTexts:
    vrRegTable.setStatus("mandatory")
_VrRegEntry_Object = MibTableRow
vrRegEntry = _VrRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1)
)
vrRegEntry.setIndexNames(
    (0, "CXVR-MIB", "vrRegDialNo"),
)
if mibBuilder.loadTexts:
    vrRegEntry.setStatus("mandatory")


class _VrRegDialNo_Type(Integer32):
    """Custom type vrRegDialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_VrRegDialNo_Type.__name__ = "Integer32"
_VrRegDialNo_Object = MibTableColumn
vrRegDialNo = _VrRegDialNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 10),
    _VrRegDialNo_Type()
)
vrRegDialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegDialNo.setStatus("mandatory")


class _VrRegState_Type(Integer32):
    """Custom type vrRegState based on Integer32"""
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
        *(("vrAgedOut", 2),
          ("vrMemallocFail", 4),
          ("vrOk", 1),
          ("vrTableFull", 3))
    )


_VrRegState_Type.__name__ = "Integer32"
_VrRegState_Object = MibTableColumn
vrRegState = _VrRegState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 11),
    _VrRegState_Type()
)
vrRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegState.setStatus("mandatory")


class _VrRegVceStationId_Type(DisplayString):
    """Custom type vrRegVceStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VrRegVceStationId_Type.__name__ = "DisplayString"
_VrRegVceStationId_Object = MibTableColumn
vrRegVceStationId = _VrRegVceStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 12),
    _VrRegVceStationId_Type()
)
vrRegVceStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegVceStationId.setStatus("mandatory")


class _VrRegVceSoftId_Type(DisplayString):
    """Custom type vrRegVceSoftId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VrRegVceSoftId_Type.__name__ = "DisplayString"
_VrRegVceSoftId_Object = MibTableColumn
vrRegVceSoftId = _VrRegVceSoftId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 13),
    _VrRegVceSoftId_Type()
)
vrRegVceSoftId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegVceSoftId.setStatus("mandatory")
_VrRegSlotNo_Type = Integer32
_VrRegSlotNo_Object = MibTableColumn
vrRegSlotNo = _VrRegSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 14),
    _VrRegSlotNo_Type()
)
vrRegSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegSlotNo.setStatus("mandatory")


class _VrRegHuntChannel_Type(DisplayString):
    """Custom type vrRegHuntChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrRegHuntChannel_Type.__name__ = "DisplayString"
_VrRegHuntChannel_Object = MibTableColumn
vrRegHuntChannel = _VrRegHuntChannel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 10, 1, 15),
    _VrRegHuntChannel_Type()
)
vrRegHuntChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRegHuntChannel.setStatus("mandatory")
_VrConfigGroup_ObjectIdentity = ObjectIdentity
vrConfigGroup = _VrConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20)
)


class _VrConfigNodeId_Type(DisplayString):
    """Custom type vrConfigNodeId based on DisplayString"""
    defaultValue = OctetString("VoiceRouting")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VrConfigNodeId_Type.__name__ = "DisplayString"
_VrConfigNodeId_Object = MibScalar
vrConfigNodeId = _VrConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 1),
    _VrConfigNodeId_Type()
)
vrConfigNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigNodeId.setStatus("mandatory")


class _VrConfigSoftId_Type(DisplayString):
    """Custom type vrConfigSoftId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VrConfigSoftId_Type.__name__ = "DisplayString"
_VrConfigSoftId_Object = MibScalar
vrConfigSoftId = _VrConfigSoftId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 2),
    _VrConfigSoftId_Type()
)
vrConfigSoftId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrConfigSoftId.setStatus("mandatory")


class _VrConfigNoOfSysRouteSupported_Type(Integer32):
    """Custom type vrConfigNoOfSysRouteSupported based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrConfigNoOfSysRouteSupported_Type.__name__ = "Integer32"
_VrConfigNoOfSysRouteSupported_Object = MibScalar
vrConfigNoOfSysRouteSupported = _VrConfigNoOfSysRouteSupported_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 3),
    _VrConfigNoOfSysRouteSupported_Type()
)
vrConfigNoOfSysRouteSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigNoOfSysRouteSupported.setStatus("mandatory")


class _VrConfigNoOfDigitSupported_Type(Integer32):
    """Custom type vrConfigNoOfDigitSupported based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dig5", 5),
          ("dig7", 7))
    )


_VrConfigNoOfDigitSupported_Type.__name__ = "Integer32"
_VrConfigNoOfDigitSupported_Object = MibScalar
vrConfigNoOfDigitSupported = _VrConfigNoOfDigitSupported_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 4),
    _VrConfigNoOfDigitSupported_Type()
)
vrConfigNoOfDigitSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigNoOfDigitSupported.setStatus("mandatory")


class _VrConfigMaxBufferPoolSize_Type(Integer32):
    """Custom type vrConfigMaxBufferPoolSize based on Integer32"""
    defaultValue = 0


_VrConfigMaxBufferPoolSize_Object = MibScalar
vrConfigMaxBufferPoolSize = _VrConfigMaxBufferPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 5),
    _VrConfigMaxBufferPoolSize_Type()
)
vrConfigMaxBufferPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigMaxBufferPoolSize.setStatus("mandatory")


class _VrConfigFastSwitchingOption_Type(Integer32):
    """Custom type vrConfigFastSwitchingOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vrprtyroute", 2),
          ("vrprtysmall", 1))
    )


_VrConfigFastSwitchingOption_Type.__name__ = "Integer32"
_VrConfigFastSwitchingOption_Object = MibScalar
vrConfigFastSwitchingOption = _VrConfigFastSwitchingOption_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 6),
    _VrConfigFastSwitchingOption_Type()
)
vrConfigFastSwitchingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigFastSwitchingOption.setStatus("mandatory")


class _VrConfigStatsSamplingPeriod_Type(Integer32):
    """Custom type vrConfigStatsSamplingPeriod based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VrConfigStatsSamplingPeriod_Type.__name__ = "Integer32"
_VrConfigStatsSamplingPeriod_Object = MibScalar
vrConfigStatsSamplingPeriod = _VrConfigStatsSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 7),
    _VrConfigStatsSamplingPeriod_Type()
)
vrConfigStatsSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigStatsSamplingPeriod.setStatus("mandatory")


class _VrConfigControl_Type(Integer32):
    """Custom type vrConfigControl based on Integer32"""
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
        *(("vrcfgidle", 1),
          ("vrcfgreg", 3),
          ("vrcfgrte", 2))
    )


_VrConfigControl_Type.__name__ = "Integer32"
_VrConfigControl_Object = MibScalar
vrConfigControl = _VrConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 8),
    _VrConfigControl_Type()
)
vrConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigControl.setStatus("mandatory")


class _VrConfigOptimization_Type(Integer32):
    """Custom type vrConfigOptimization based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vroptbwmgt", 3),
          ("vroptdisabled", 1),
          ("vroptenabled", 2))
    )


_VrConfigOptimization_Type.__name__ = "Integer32"
_VrConfigOptimization_Object = MibScalar
vrConfigOptimization = _VrConfigOptimization_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 9),
    _VrConfigOptimization_Type()
)
vrConfigOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrConfigOptimization.setStatus("mandatory")


class _VrMibLevel_Type(Integer32):
    """Custom type vrMibLevel based on Integer32"""
    defaultValue = 0


_VrMibLevel_Object = MibScalar
vrMibLevel = _VrMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 20, 20),
    _VrMibLevel_Type()
)
vrMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMibLevel.setStatus("mandatory")
_VrStatGroup_ObjectIdentity = ObjectIdentity
vrStatGroup = _VrStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30)
)


class _VrStatInitState_Type(Integer32):
    """Custom type vrStatInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("vrConfigRead", 4),
          ("vrDead", 1),
          ("vrInitialized", 10),
          ("vrTablesBuilt", 3),
          ("vrUnrecoverableError", 2))
    )


_VrStatInitState_Type.__name__ = "Integer32"
_VrStatInitState_Object = MibScalar
vrStatInitState = _VrStatInitState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 30),
    _VrStatInitState_Type()
)
vrStatInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatInitState.setStatus("mandatory")
_VrStatLongestMuxPassInMs_Type = Counter32
_VrStatLongestMuxPassInMs_Object = MibScalar
vrStatLongestMuxPassInMs = _VrStatLongestMuxPassInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 50),
    _VrStatLongestMuxPassInMs_Type()
)
vrStatLongestMuxPassInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatLongestMuxPassInMs.setStatus("mandatory")
_VrStatNbPacketsForwardedPerSec_Type = Counter32
_VrStatNbPacketsForwardedPerSec_Object = MibScalar
vrStatNbPacketsForwardedPerSec = _VrStatNbPacketsForwardedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 51),
    _VrStatNbPacketsForwardedPerSec_Type()
)
vrStatNbPacketsForwardedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbPacketsForwardedPerSec.setStatus("mandatory")
_VrStatNbRoutingConflicts_Type = Counter32
_VrStatNbRoutingConflicts_Object = MibScalar
vrStatNbRoutingConflicts = _VrStatNbRoutingConflicts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 52),
    _VrStatNbRoutingConflicts_Type()
)
vrStatNbRoutingConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbRoutingConflicts.setStatus("mandatory")
_VrStatRegOverallNumber_Type = Counter32
_VrStatRegOverallNumber_Object = MibScalar
vrStatRegOverallNumber = _VrStatRegOverallNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 60),
    _VrStatRegOverallNumber_Type()
)
vrStatRegOverallNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatRegOverallNumber.setStatus("mandatory")
_VrStatRegNotOwner_Type = Counter32
_VrStatRegNotOwner_Object = MibScalar
vrStatRegNotOwner = _VrStatRegNotOwner_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 61),
    _VrStatRegNotOwner_Type()
)
vrStatRegNotOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatRegNotOwner.setStatus("mandatory")
_VrStatRegInvalidDialNumber_Type = Counter32
_VrStatRegInvalidDialNumber_Object = MibScalar
vrStatRegInvalidDialNumber = _VrStatRegInvalidDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 62),
    _VrStatRegInvalidDialNumber_Type()
)
vrStatRegInvalidDialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatRegInvalidDialNumber.setStatus("mandatory")
_VrStatRegFormatError_Type = Counter32
_VrStatRegFormatError_Object = MibScalar
vrStatRegFormatError = _VrStatRegFormatError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 63),
    _VrStatRegFormatError_Type()
)
vrStatRegFormatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatRegFormatError.setStatus("mandatory")
_VrStatNbVceMsgRx_Type = Counter32
_VrStatNbVceMsgRx_Object = MibScalar
vrStatNbVceMsgRx = _VrStatNbVceMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 75),
    _VrStatNbVceMsgRx_Type()
)
vrStatNbVceMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbVceMsgRx.setStatus("mandatory")
_VrStatNbVceMsgTx_Type = Counter32
_VrStatNbVceMsgTx_Object = MibScalar
vrStatNbVceMsgTx = _VrStatNbVceMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 76),
    _VrStatNbVceMsgTx_Type()
)
vrStatNbVceMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbVceMsgTx.setStatus("mandatory")
_VrStatNbBusMsgRx_Type = Counter32
_VrStatNbBusMsgRx_Object = MibScalar
vrStatNbBusMsgRx = _VrStatNbBusMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 77),
    _VrStatNbBusMsgRx_Type()
)
vrStatNbBusMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbBusMsgRx.setStatus("mandatory")
_VrStatNbBusMsgTx_Type = Counter32
_VrStatNbBusMsgTx_Object = MibScalar
vrStatNbBusMsgTx = _VrStatNbBusMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 78),
    _VrStatNbBusMsgTx_Type()
)
vrStatNbBusMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbBusMsgTx.setStatus("mandatory")
_VrStatNbWanMsgRx_Type = Counter32
_VrStatNbWanMsgRx_Object = MibScalar
vrStatNbWanMsgRx = _VrStatNbWanMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 79),
    _VrStatNbWanMsgRx_Type()
)
vrStatNbWanMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbWanMsgRx.setStatus("mandatory")
_VrStatNbWanMsgTx_Type = Counter32
_VrStatNbWanMsgTx_Object = MibScalar
vrStatNbWanMsgTx = _VrStatNbWanMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 80),
    _VrStatNbWanMsgTx_Type()
)
vrStatNbWanMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbWanMsgTx.setStatus("mandatory")
_VrStatNbOutboundQueueFull_Type = Counter32
_VrStatNbOutboundQueueFull_Object = MibScalar
vrStatNbOutboundQueueFull = _VrStatNbOutboundQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 81),
    _VrStatNbOutboundQueueFull_Type()
)
vrStatNbOutboundQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbOutboundQueueFull.setStatus("mandatory")
_VrStatNbOverallForwards_Type = Counter32
_VrStatNbOverallForwards_Object = MibScalar
vrStatNbOverallForwards = _VrStatNbOverallForwards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 90),
    _VrStatNbOverallForwards_Type()
)
vrStatNbOverallForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbOverallForwards.setStatus("mandatory")
_VrStatNbOverallDiscards_Type = Counter32
_VrStatNbOverallDiscards_Object = MibScalar
vrStatNbOverallDiscards = _VrStatNbOverallDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 91),
    _VrStatNbOverallDiscards_Type()
)
vrStatNbOverallDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbOverallDiscards.setStatus("mandatory")
_VrStatNbDeadEnds_Type = Counter32
_VrStatNbDeadEnds_Object = MibScalar
vrStatNbDeadEnds = _VrStatNbDeadEnds_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 92),
    _VrStatNbDeadEnds_Type()
)
vrStatNbDeadEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatNbDeadEnds.setStatus("mandatory")
_VrStatError_Type = Counter32
_VrStatError_Object = MibScalar
vrStatError = _VrStatError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 93),
    _VrStatError_Type()
)
vrStatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatError.setStatus("mandatory")


class _VrStatFieldsAddress_Type(DisplayString):
    """Custom type vrStatFieldsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VrStatFieldsAddress_Type.__name__ = "DisplayString"
_VrStatFieldsAddress_Object = MibScalar
vrStatFieldsAddress = _VrStatFieldsAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 94),
    _VrStatFieldsAddress_Type()
)
vrStatFieldsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatFieldsAddress.setStatus("mandatory")


class _VrStatIamUnxFieldAddress_Type(DisplayString):
    """Custom type vrStatIamUnxFieldAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VrStatIamUnxFieldAddress_Type.__name__ = "DisplayString"
_VrStatIamUnxFieldAddress_Object = MibScalar
vrStatIamUnxFieldAddress = _VrStatIamUnxFieldAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 30, 95),
    _VrStatIamUnxFieldAddress_Type()
)
vrStatIamUnxFieldAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStatIamUnxFieldAddress.setStatus("mandatory")
_VrSrTable_Object = MibTable
vrSrTable = _VrSrTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40)
)
if mibBuilder.loadTexts:
    vrSrTable.setStatus("mandatory")
_VrSrEntry_Object = MibTableRow
vrSrEntry = _VrSrEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1)
)
vrSrEntry.setIndexNames(
    (0, "CXVR-MIB", "vrSrIndex"),
)
if mibBuilder.loadTexts:
    vrSrEntry.setStatus("mandatory")


class _VrSrIndex_Type(Integer32):
    """Custom type vrSrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSrIndex_Type.__name__ = "Integer32"
_VrSrIndex_Object = MibTableColumn
vrSrIndex = _VrSrIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 1),
    _VrSrIndex_Type()
)
vrSrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrIndex.setStatus("mandatory")


class _VrSrRowStatus_Type(Integer32):
    """Custom type vrSrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_VrSrRowStatus_Type.__name__ = "Integer32"
_VrSrRowStatus_Object = MibTableColumn
vrSrRowStatus = _VrSrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 2),
    _VrSrRowStatus_Type()
)
vrSrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSrRowStatus.setStatus("mandatory")
_VrSrDestAlias_Type = Alias
_VrSrDestAlias_Object = MibTableColumn
vrSrDestAlias = _VrSrDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 3),
    _VrSrDestAlias_Type()
)
vrSrDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSrDestAlias.setStatus("mandatory")


class _VrSrSubRef_Type(Integer32):
    """Custom type vrSrSubRef based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_VrSrSubRef_Type.__name__ = "Integer32"
_VrSrSubRef_Object = MibTableColumn
vrSrSubRef = _VrSrSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 10),
    _VrSrSubRef_Type()
)
vrSrSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSrSubRef.setStatus("mandatory")


class _VrSrBandwidth_Type(Integer32):
    """Custom type vrSrBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrSrBandwidth_Type.__name__ = "Integer32"
_VrSrBandwidth_Object = MibTableColumn
vrSrBandwidth = _VrSrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 20),
    _VrSrBandwidth_Type()
)
vrSrBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSrBandwidth.setStatus("mandatory")


class _VrSrBwIndex_Type(Integer32):
    """Custom type vrSrBwIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrSrBwIndex_Type.__name__ = "Integer32"
_VrSrBwIndex_Object = MibTableColumn
vrSrBwIndex = _VrSrBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 21),
    _VrSrBwIndex_Type()
)
vrSrBwIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSrBwIndex.setStatus("mandatory")


class _VrSrStatus_Type(Integer32):
    """Custom type vrSrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vrSrDown", 1),
          ("vrSrInFlowCtl", 2),
          ("vrSrUp", 3))
    )


_VrSrStatus_Type.__name__ = "Integer32"
_VrSrStatus_Object = MibTableColumn
vrSrStatus = _VrSrStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 30),
    _VrSrStatus_Type()
)
vrSrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrStatus.setStatus("mandatory")


class _VrSrConStatus_Type(Integer32):
    """Custom type vrSrConStatus based on Integer32"""
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
        *(("vrClose", 2),
          ("vrNotConfigured", 1),
          ("vrOpen", 5),
          ("vrWaitForOpenConf", 4),
          ("vrWaitForQuery", 3))
    )


_VrSrConStatus_Type.__name__ = "Integer32"
_VrSrConStatus_Object = MibTableColumn
vrSrConStatus = _VrSrConStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 31),
    _VrSrConStatus_Type()
)
vrSrConStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrConStatus.setStatus("mandatory")


class _VrSrFailStatus_Type(Integer32):
    """Custom type vrSrFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("vrAdjaReset", 14),
          ("vrInternalError", 2),
          ("vrLocalDsnFailure", 10),
          ("vrLocalFcnFailure", 8),
          ("vrLocalMemFail", 3),
          ("vrNoFailure", 1),
          ("vrNoPvcService", 12),
          ("vrOpenReqTimeout", 13),
          ("vrRemAliasNotFound", 11),
          ("vrRemFcnFailure", 9),
          ("vrRemMemFail", 4),
          ("vrRemNoAcces", 5),
          ("vrRemPvcBusy", 7),
          ("vrRemPvcDown", 6),
          ("vrUnsupportedSR", 15))
    )


_VrSrFailStatus_Type.__name__ = "Integer32"
_VrSrFailStatus_Object = MibTableColumn
vrSrFailStatus = _VrSrFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 32),
    _VrSrFailStatus_Type()
)
vrSrFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrFailStatus.setStatus("mandatory")
_VrSrNbLinkDown_Type = Counter32
_VrSrNbLinkDown_Object = MibTableColumn
vrSrNbLinkDown = _VrSrNbLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 50),
    _VrSrNbLinkDown_Type()
)
vrSrNbLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbLinkDown.setStatus("mandatory")
_VrSrNbResetFrameRx_Type = Counter32
_VrSrNbResetFrameRx_Object = MibTableColumn
vrSrNbResetFrameRx = _VrSrNbResetFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 51),
    _VrSrNbResetFrameRx_Type()
)
vrSrNbResetFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbResetFrameRx.setStatus("mandatory")
_VrSrNbOutboundFrame_Type = Counter32
_VrSrNbOutboundFrame_Object = MibTableColumn
vrSrNbOutboundFrame = _VrSrNbOutboundFrame_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 52),
    _VrSrNbOutboundFrame_Type()
)
vrSrNbOutboundFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbOutboundFrame.setStatus("mandatory")
_VrSrNbInboundFrame_Type = Counter32
_VrSrNbInboundFrame_Object = MibTableColumn
vrSrNbInboundFrame = _VrSrNbInboundFrame_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 53),
    _VrSrNbInboundFrame_Type()
)
vrSrNbInboundFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbInboundFrame.setStatus("mandatory")
_VrSrNbOutboundBw_Type = Counter32
_VrSrNbOutboundBw_Object = MibTableColumn
vrSrNbOutboundBw = _VrSrNbOutboundBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 54),
    _VrSrNbOutboundBw_Type()
)
vrSrNbOutboundBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbOutboundBw.setStatus("mandatory")
_VrSrNbInboundBw_Type = Counter32
_VrSrNbInboundBw_Object = MibTableColumn
vrSrNbInboundBw = _VrSrNbInboundBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 55),
    _VrSrNbInboundBw_Type()
)
vrSrNbInboundBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbInboundBw.setStatus("mandatory")
_VrSrBwUsed_Type = Counter32
_VrSrBwUsed_Object = MibTableColumn
vrSrBwUsed = _VrSrBwUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 56),
    _VrSrBwUsed_Type()
)
vrSrBwUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrBwUsed.setStatus("mandatory")
_VrSrNbCalls_Type = Counter32
_VrSrNbCalls_Object = MibTableColumn
vrSrNbCalls = _VrSrNbCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 57),
    _VrSrNbCalls_Type()
)
vrSrNbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbCalls.setStatus("mandatory")
_VrSrNbPktDropped_Type = Counter32
_VrSrNbPktDropped_Object = MibTableColumn
vrSrNbPktDropped = _VrSrNbPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 40, 1, 58),
    _VrSrNbPktDropped_Type()
)
vrSrNbPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSrNbPktDropped.setStatus("mandatory")
_VrRouteTable_Object = MibTable
vrRouteTable = _VrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50)
)
if mibBuilder.loadTexts:
    vrRouteTable.setStatus("mandatory")
_VrRouteEntry_Object = MibTableRow
vrRouteEntry = _VrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1)
)
vrRouteEntry.setIndexNames(
    (0, "CXVR-MIB", "vrRouteDialNo"),
)
if mibBuilder.loadTexts:
    vrRouteEntry.setStatus("mandatory")


class _VrRouteDialNo_Type(Integer32):
    """Custom type vrRouteDialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_VrRouteDialNo_Type.__name__ = "Integer32"
_VrRouteDialNo_Object = MibTableColumn
vrRouteDialNo = _VrRouteDialNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1, 1),
    _VrRouteDialNo_Type()
)
vrRouteDialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRouteDialNo.setStatus("mandatory")


class _VrRouteRowStatus_Type(Integer32):
    """Custom type vrRouteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_VrRouteRowStatus_Type.__name__ = "Integer32"
_VrRouteRowStatus_Object = MibTableColumn
vrRouteRowStatus = _VrRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1, 2),
    _VrRouteRowStatus_Type()
)
vrRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrRouteRowStatus.setStatus("mandatory")


class _VrRouteMask_Type(Integer32):
    """Custom type vrRouteMask based on Integer32"""
    defaultValue = 1111111

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1111111),
    )


_VrRouteMask_Type.__name__ = "Integer32"
_VrRouteMask_Object = MibTableColumn
vrRouteMask = _VrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1, 10),
    _VrRouteMask_Type()
)
vrRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrRouteMask.setStatus("mandatory")


class _VrRouteSrNumber_Type(Integer32):
    """Custom type vrRouteSrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrRouteSrNumber_Type.__name__ = "Integer32"
_VrRouteSrNumber_Object = MibTableColumn
vrRouteSrNumber = _VrRouteSrNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1, 11),
    _VrRouteSrNumber_Type()
)
vrRouteSrNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrRouteSrNumber.setStatus("mandatory")
_VrRouteForwardedPkt_Type = Counter32
_VrRouteForwardedPkt_Object = MibTableColumn
vrRouteForwardedPkt = _VrRouteForwardedPkt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 50, 1, 50),
    _VrRouteForwardedPkt_Type()
)
vrRouteForwardedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRouteForwardedPkt.setStatus("mandatory")
_VrPingGroup_ObjectIdentity = ObjectIdentity
vrPingGroup = _VrPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60)
)


class _VrPingDialNo_Type(Integer32):
    """Custom type vrPingDialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_VrPingDialNo_Type.__name__ = "Integer32"
_VrPingDialNo_Object = MibScalar
vrPingDialNo = _VrPingDialNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 1),
    _VrPingDialNo_Type()
)
vrPingDialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingDialNo.setStatus("mandatory")


class _VrPingNbToBeSent_Type(Integer32):
    """Custom type vrPingNbToBeSent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000000),
    )


_VrPingNbToBeSent_Type.__name__ = "Integer32"
_VrPingNbToBeSent_Object = MibScalar
vrPingNbToBeSent = _VrPingNbToBeSent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 2),
    _VrPingNbToBeSent_Type()
)
vrPingNbToBeSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingNbToBeSent.setStatus("mandatory")


class _VrPingGapsInMs_Type(Integer32):
    """Custom type vrPingGapsInMs based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrPingGapsInMs_Type.__name__ = "Integer32"
_VrPingGapsInMs_Object = MibScalar
vrPingGapsInMs = _VrPingGapsInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 3),
    _VrPingGapsInMs_Type()
)
vrPingGapsInMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingGapsInMs.setStatus("mandatory")


class _VrPingMaxHopCount_Type(Integer32):
    """Custom type vrPingMaxHopCount based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VrPingMaxHopCount_Type.__name__ = "Integer32"
_VrPingMaxHopCount_Object = MibScalar
vrPingMaxHopCount = _VrPingMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 4),
    _VrPingMaxHopCount_Type()
)
vrPingMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingMaxHopCount.setStatus("mandatory")


class _VrPingProbeReturnAddress_Type(Integer32):
    """Custom type vrPingProbeReturnAddress based on Integer32"""
    defaultValue = 9999999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_VrPingProbeReturnAddress_Type.__name__ = "Integer32"
_VrPingProbeReturnAddress_Object = MibScalar
vrPingProbeReturnAddress = _VrPingProbeReturnAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 5),
    _VrPingProbeReturnAddress_Type()
)
vrPingProbeReturnAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingProbeReturnAddress.setStatus("mandatory")


class _VrPingTriggerSend_Type(Integer32):
    """Custom type vrPingTriggerSend based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vrIdle", 1),
          ("vrSend", 2))
    )


_VrPingTriggerSend_Type.__name__ = "Integer32"
_VrPingTriggerSend_Object = MibScalar
vrPingTriggerSend = _VrPingTriggerSend_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 6),
    _VrPingTriggerSend_Type()
)
vrPingTriggerSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPingTriggerSend.setStatus("mandatory")
_VrPingNbReplyRx_Type = Counter32
_VrPingNbReplyRx_Object = MibScalar
vrPingNbReplyRx = _VrPingNbReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 30),
    _VrPingNbReplyRx_Type()
)
vrPingNbReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingNbReplyRx.setStatus("mandatory")
_VrPingFormatError_Type = Counter32
_VrPingFormatError_Object = MibScalar
vrPingFormatError = _VrPingFormatError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 31),
    _VrPingFormatError_Type()
)
vrPingFormatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingFormatError.setStatus("mandatory")
_VrPingNbVrNodesCrossedForward_Type = Counter32
_VrPingNbVrNodesCrossedForward_Object = MibScalar
vrPingNbVrNodesCrossedForward = _VrPingNbVrNodesCrossedForward_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 32),
    _VrPingNbVrNodesCrossedForward_Type()
)
vrPingNbVrNodesCrossedForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingNbVrNodesCrossedForward.setStatus("mandatory")
_VrPingNbVrNodesCrossedBackward_Type = Counter32
_VrPingNbVrNodesCrossedBackward_Object = MibScalar
vrPingNbVrNodesCrossedBackward = _VrPingNbVrNodesCrossedBackward_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 33),
    _VrPingNbVrNodesCrossedBackward_Type()
)
vrPingNbVrNodesCrossedBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingNbVrNodesCrossedBackward.setStatus("mandatory")
_VrPingLastRoundTripInMs_Type = Counter32
_VrPingLastRoundTripInMs_Object = MibScalar
vrPingLastRoundTripInMs = _VrPingLastRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 34),
    _VrPingLastRoundTripInMs_Type()
)
vrPingLastRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingLastRoundTripInMs.setStatus("mandatory")
_VrPingLastSequenceNumberRx_Type = Counter32
_VrPingLastSequenceNumberRx_Object = MibScalar
vrPingLastSequenceNumberRx = _VrPingLastSequenceNumberRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 35),
    _VrPingLastSequenceNumberRx_Type()
)
vrPingLastSequenceNumberRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingLastSequenceNumberRx.setStatus("mandatory")
_VrPingSequenceError_Type = Counter32
_VrPingSequenceError_Object = MibScalar
vrPingSequenceError = _VrPingSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 36),
    _VrPingSequenceError_Type()
)
vrPingSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingSequenceError.setStatus("mandatory")
_VrPingMinRoundTripInMs_Type = Counter32
_VrPingMinRoundTripInMs_Object = MibScalar
vrPingMinRoundTripInMs = _VrPingMinRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 37),
    _VrPingMinRoundTripInMs_Type()
)
vrPingMinRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingMinRoundTripInMs.setStatus("mandatory")
_VrPingMaxRoundTripInMs_Type = Counter32
_VrPingMaxRoundTripInMs_Object = MibScalar
vrPingMaxRoundTripInMs = _VrPingMaxRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 38),
    _VrPingMaxRoundTripInMs_Type()
)
vrPingMaxRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingMaxRoundTripInMs.setStatus("mandatory")


class _VrPingRemStatus_Type(Integer32):
    """Custom type vrPingRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vrOk", 1),
          ("vrUnknown", 5))
    )


_VrPingRemStatus_Type.__name__ = "Integer32"
_VrPingRemStatus_Object = MibScalar
vrPingRemStatus = _VrPingRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 39),
    _VrPingRemStatus_Type()
)
vrPingRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemStatus.setStatus("mandatory")


class _VrPingRemVrNodeId_Type(DisplayString):
    """Custom type vrPingRemVrNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VrPingRemVrNodeId_Type.__name__ = "DisplayString"
_VrPingRemVrNodeId_Object = MibScalar
vrPingRemVrNodeId = _VrPingRemVrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 40),
    _VrPingRemVrNodeId_Type()
)
vrPingRemVrNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemVrNodeId.setStatus("mandatory")


class _VrPingRemVceStationId_Type(DisplayString):
    """Custom type vrPingRemVceStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VrPingRemVceStationId_Type.__name__ = "DisplayString"
_VrPingRemVceStationId_Object = MibScalar
vrPingRemVceStationId = _VrPingRemVceStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 41),
    _VrPingRemVceStationId_Type()
)
vrPingRemVceStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemVceStationId.setStatus("mandatory")


class _VrPingRemVrSoftId_Type(DisplayString):
    """Custom type vrPingRemVrSoftId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VrPingRemVrSoftId_Type.__name__ = "DisplayString"
_VrPingRemVrSoftId_Object = MibScalar
vrPingRemVrSoftId = _VrPingRemVrSoftId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 42),
    _VrPingRemVrSoftId_Type()
)
vrPingRemVrSoftId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemVrSoftId.setStatus("mandatory")


class _VrPingRemVceSoftId_Type(DisplayString):
    """Custom type vrPingRemVceSoftId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VrPingRemVceSoftId_Type.__name__ = "DisplayString"
_VrPingRemVceSoftId_Object = MibScalar
vrPingRemVceSoftId = _VrPingRemVceSoftId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 43),
    _VrPingRemVceSoftId_Type()
)
vrPingRemVceSoftId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemVceSoftId.setStatus("mandatory")


class _VrPingRemSlotIndex_Type(Integer32):
    """Custom type vrPingRemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VrPingRemSlotIndex_Type.__name__ = "Integer32"
_VrPingRemSlotIndex_Object = MibScalar
vrPingRemSlotIndex = _VrPingRemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 44),
    _VrPingRemSlotIndex_Type()
)
vrPingRemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemSlotIndex.setStatus("mandatory")


class _VrPingRemHuntChannel_Type(DisplayString):
    """Custom type vrPingRemHuntChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrPingRemHuntChannel_Type.__name__ = "DisplayString"
_VrPingRemHuntChannel_Object = MibScalar
vrPingRemHuntChannel = _VrPingRemHuntChannel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 45),
    _VrPingRemHuntChannel_Type()
)
vrPingRemHuntChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemHuntChannel.setStatus("mandatory")
_VrPingRemNbForwardedPacket_Type = Counter32
_VrPingRemNbForwardedPacket_Object = MibScalar
vrPingRemNbForwardedPacket = _VrPingRemNbForwardedPacket_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 46),
    _VrPingRemNbForwardedPacket_Type()
)
vrPingRemNbForwardedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemNbForwardedPacket.setStatus("mandatory")
_VrPingRemNbRestart_Type = Counter32
_VrPingRemNbRestart_Object = MibScalar
vrPingRemNbRestart = _VrPingRemNbRestart_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 60, 47),
    _VrPingRemNbRestart_Type()
)
vrPingRemNbRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPingRemNbRestart.setStatus("mandatory")
_VrBwTable_Object = MibTable
vrBwTable = _VrBwTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70)
)
if mibBuilder.loadTexts:
    vrBwTable.setStatus("mandatory")
_VrBwEntry_Object = MibTableRow
vrBwEntry = _VrBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1)
)
vrBwEntry.setIndexNames(
    (0, "CXVR-MIB", "vrBwIndex"),
)
if mibBuilder.loadTexts:
    vrBwEntry.setStatus("mandatory")


class _VrBwIndex_Type(Integer32):
    """Custom type vrBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VrBwIndex_Type.__name__ = "Integer32"
_VrBwIndex_Object = MibTableColumn
vrBwIndex = _VrBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 1),
    _VrBwIndex_Type()
)
vrBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBwIndex.setStatus("mandatory")


class _VrBwRowStatus_Type(Integer32):
    """Custom type vrBwRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_VrBwRowStatus_Type.__name__ = "Integer32"
_VrBwRowStatus_Object = MibTableColumn
vrBwRowStatus = _VrBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 2),
    _VrBwRowStatus_Type()
)
vrBwRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBwRowStatus.setStatus("mandatory")


class _VrBwBandwidthCfg_Type(Integer32):
    """Custom type vrBwBandwidthCfg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBwBandwidthCfg_Type.__name__ = "Integer32"
_VrBwBandwidthCfg_Object = MibTableColumn
vrBwBandwidthCfg = _VrBwBandwidthCfg_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 3),
    _VrBwBandwidthCfg_Type()
)
vrBwBandwidthCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrBwBandwidthCfg.setStatus("mandatory")


class _VrBwBandwidthUsed_Type(Integer32):
    """Custom type vrBwBandwidthUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBwBandwidthUsed_Type.__name__ = "Integer32"
_VrBwBandwidthUsed_Object = MibTableColumn
vrBwBandwidthUsed = _VrBwBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 10),
    _VrBwBandwidthUsed_Type()
)
vrBwBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBwBandwidthUsed.setStatus("mandatory")


class _VrBwNbCalls_Type(Integer32):
    """Custom type vrBwNbCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrBwNbCalls_Type.__name__ = "Integer32"
_VrBwNbCalls_Object = MibTableColumn
vrBwNbCalls = _VrBwNbCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 11),
    _VrBwNbCalls_Type()
)
vrBwNbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBwNbCalls.setStatus("mandatory")
_VrBwNbPktDropped_Type = Counter32
_VrBwNbPktDropped_Object = MibTableColumn
vrBwNbPktDropped = _VrBwNbPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50, 70, 1, 12),
    _VrBwNbPktDropped_Type()
)
vrBwNbPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrBwNbPktDropped.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXVR-MIB",
    **{"vrRegTable": vrRegTable,
       "vrRegEntry": vrRegEntry,
       "vrRegDialNo": vrRegDialNo,
       "vrRegState": vrRegState,
       "vrRegVceStationId": vrRegVceStationId,
       "vrRegVceSoftId": vrRegVceSoftId,
       "vrRegSlotNo": vrRegSlotNo,
       "vrRegHuntChannel": vrRegHuntChannel,
       "vrConfigGroup": vrConfigGroup,
       "vrConfigNodeId": vrConfigNodeId,
       "vrConfigSoftId": vrConfigSoftId,
       "vrConfigNoOfSysRouteSupported": vrConfigNoOfSysRouteSupported,
       "vrConfigNoOfDigitSupported": vrConfigNoOfDigitSupported,
       "vrConfigMaxBufferPoolSize": vrConfigMaxBufferPoolSize,
       "vrConfigFastSwitchingOption": vrConfigFastSwitchingOption,
       "vrConfigStatsSamplingPeriod": vrConfigStatsSamplingPeriod,
       "vrConfigControl": vrConfigControl,
       "vrConfigOptimization": vrConfigOptimization,
       "vrMibLevel": vrMibLevel,
       "vrStatGroup": vrStatGroup,
       "vrStatInitState": vrStatInitState,
       "vrStatLongestMuxPassInMs": vrStatLongestMuxPassInMs,
       "vrStatNbPacketsForwardedPerSec": vrStatNbPacketsForwardedPerSec,
       "vrStatNbRoutingConflicts": vrStatNbRoutingConflicts,
       "vrStatRegOverallNumber": vrStatRegOverallNumber,
       "vrStatRegNotOwner": vrStatRegNotOwner,
       "vrStatRegInvalidDialNumber": vrStatRegInvalidDialNumber,
       "vrStatRegFormatError": vrStatRegFormatError,
       "vrStatNbVceMsgRx": vrStatNbVceMsgRx,
       "vrStatNbVceMsgTx": vrStatNbVceMsgTx,
       "vrStatNbBusMsgRx": vrStatNbBusMsgRx,
       "vrStatNbBusMsgTx": vrStatNbBusMsgTx,
       "vrStatNbWanMsgRx": vrStatNbWanMsgRx,
       "vrStatNbWanMsgTx": vrStatNbWanMsgTx,
       "vrStatNbOutboundQueueFull": vrStatNbOutboundQueueFull,
       "vrStatNbOverallForwards": vrStatNbOverallForwards,
       "vrStatNbOverallDiscards": vrStatNbOverallDiscards,
       "vrStatNbDeadEnds": vrStatNbDeadEnds,
       "vrStatError": vrStatError,
       "vrStatFieldsAddress": vrStatFieldsAddress,
       "vrStatIamUnxFieldAddress": vrStatIamUnxFieldAddress,
       "vrSrTable": vrSrTable,
       "vrSrEntry": vrSrEntry,
       "vrSrIndex": vrSrIndex,
       "vrSrRowStatus": vrSrRowStatus,
       "vrSrDestAlias": vrSrDestAlias,
       "vrSrSubRef": vrSrSubRef,
       "vrSrBandwidth": vrSrBandwidth,
       "vrSrBwIndex": vrSrBwIndex,
       "vrSrStatus": vrSrStatus,
       "vrSrConStatus": vrSrConStatus,
       "vrSrFailStatus": vrSrFailStatus,
       "vrSrNbLinkDown": vrSrNbLinkDown,
       "vrSrNbResetFrameRx": vrSrNbResetFrameRx,
       "vrSrNbOutboundFrame": vrSrNbOutboundFrame,
       "vrSrNbInboundFrame": vrSrNbInboundFrame,
       "vrSrNbOutboundBw": vrSrNbOutboundBw,
       "vrSrNbInboundBw": vrSrNbInboundBw,
       "vrSrBwUsed": vrSrBwUsed,
       "vrSrNbCalls": vrSrNbCalls,
       "vrSrNbPktDropped": vrSrNbPktDropped,
       "vrRouteTable": vrRouteTable,
       "vrRouteEntry": vrRouteEntry,
       "vrRouteDialNo": vrRouteDialNo,
       "vrRouteRowStatus": vrRouteRowStatus,
       "vrRouteMask": vrRouteMask,
       "vrRouteSrNumber": vrRouteSrNumber,
       "vrRouteForwardedPkt": vrRouteForwardedPkt,
       "vrPingGroup": vrPingGroup,
       "vrPingDialNo": vrPingDialNo,
       "vrPingNbToBeSent": vrPingNbToBeSent,
       "vrPingGapsInMs": vrPingGapsInMs,
       "vrPingMaxHopCount": vrPingMaxHopCount,
       "vrPingProbeReturnAddress": vrPingProbeReturnAddress,
       "vrPingTriggerSend": vrPingTriggerSend,
       "vrPingNbReplyRx": vrPingNbReplyRx,
       "vrPingFormatError": vrPingFormatError,
       "vrPingNbVrNodesCrossedForward": vrPingNbVrNodesCrossedForward,
       "vrPingNbVrNodesCrossedBackward": vrPingNbVrNodesCrossedBackward,
       "vrPingLastRoundTripInMs": vrPingLastRoundTripInMs,
       "vrPingLastSequenceNumberRx": vrPingLastSequenceNumberRx,
       "vrPingSequenceError": vrPingSequenceError,
       "vrPingMinRoundTripInMs": vrPingMinRoundTripInMs,
       "vrPingMaxRoundTripInMs": vrPingMaxRoundTripInMs,
       "vrPingRemStatus": vrPingRemStatus,
       "vrPingRemVrNodeId": vrPingRemVrNodeId,
       "vrPingRemVceStationId": vrPingRemVceStationId,
       "vrPingRemVrSoftId": vrPingRemVrSoftId,
       "vrPingRemVceSoftId": vrPingRemVceSoftId,
       "vrPingRemSlotIndex": vrPingRemSlotIndex,
       "vrPingRemHuntChannel": vrPingRemHuntChannel,
       "vrPingRemNbForwardedPacket": vrPingRemNbForwardedPacket,
       "vrPingRemNbRestart": vrPingRemNbRestart,
       "vrBwTable": vrBwTable,
       "vrBwEntry": vrBwEntry,
       "vrBwIndex": vrBwIndex,
       "vrBwRowStatus": vrBwRowStatus,
       "vrBwBandwidthCfg": vrBwBandwidthCfg,
       "vrBwBandwidthUsed": vrBwBandwidthUsed,
       "vrBwNbCalls": vrBwNbCalls,
       "vrBwNbPktDropped": vrBwNbPktDropped}
)
