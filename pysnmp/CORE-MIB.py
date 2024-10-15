# SNMP MIB module (CORE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CORE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:05 2024
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



class LedColor(Integer32):
    """Custom type LedColor based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("black", 3),
          ("blue", 7),
          ("green", 2),
          ("grey", 9),
          ("magenta", 8),
          ("none", 1),
          ("red", 5),
          ("white", 6),
          ("yellow", 4))
    )





class RingId(Integer32):
    """Custom type RingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("undefined", 1))
    )





class AdminStatus(Integer32):
    """Custom type AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("undefined", 1))
    )





class LinkStatus(Integer32):
    """Custom type LinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkOff", 2),
          ("linkOn", 3),
          ("undefined", 1))
    )





class FlowControlStatus(Integer32):
    """Custom type FlowControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flowControlOff", 2),
          ("flowControlOn", 3),
          ("undefined", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_Core_ObjectIdentity = ObjectIdentity
core = _Core_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9)
)
_CoreInfo_ObjectIdentity = ObjectIdentity
coreInfo = _CoreInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1)
)
_CoreSlotsMaxNumber_Type = Integer32
_CoreSlotsMaxNumber_Object = MibScalar
coreSlotsMaxNumber = _CoreSlotsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1, 1),
    _CoreSlotsMaxNumber_Type()
)
coreSlotsMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotsMaxNumber.setStatus("mandatory")
_CoreChannelsMaxNumber_Type = Integer32
_CoreChannelsMaxNumber_Object = MibScalar
coreChannelsMaxNumber = _CoreChannelsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1, 2),
    _CoreChannelsMaxNumber_Type()
)
coreChannelsMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelsMaxNumber.setStatus("mandatory")
_CoreRingsMaxNumber_Type = Integer32
_CoreRingsMaxNumber_Object = MibScalar
coreRingsMaxNumber = _CoreRingsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1, 3),
    _CoreRingsMaxNumber_Type()
)
coreRingsMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreRingsMaxNumber.setStatus("mandatory")
_CoreSlotsActNumber_Type = Integer32
_CoreSlotsActNumber_Object = MibScalar
coreSlotsActNumber = _CoreSlotsActNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1, 4),
    _CoreSlotsActNumber_Type()
)
coreSlotsActNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotsActNumber.setStatus("mandatory")
_CoreRingsActNumber_Type = Integer32
_CoreRingsActNumber_Object = MibScalar
coreRingsActNumber = _CoreRingsActNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 1, 6),
    _CoreRingsActNumber_Type()
)
coreRingsActNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreRingsActNumber.setStatus("mandatory")
_CoreSlotsTable_Object = MibTable
coreSlotsTable = _CoreSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 2)
)
if mibBuilder.loadTexts:
    coreSlotsTable.setStatus("mandatory")
_CoreSlotEntry_Object = MibTableRow
coreSlotEntry = _CoreSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 2, 1)
)
coreSlotEntry.setIndexNames(
    (0, "CORE-MIB", "coreSlotPosition"),
)
if mibBuilder.loadTexts:
    coreSlotEntry.setStatus("mandatory")
_CoreSlotPosition_Type = Integer32
_CoreSlotPosition_Object = MibTableColumn
coreSlotPosition = _CoreSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 2, 1, 1),
    _CoreSlotPosition_Type()
)
coreSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotPosition.setStatus("mandatory")


class _CoreSlotType_Type(Integer32):
    """Custom type coreSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              11,
              12,
              13,
              14,
              20,
              30,
              40,
              50)
        )
    )
    namedValues = NamedValues(
        *(("cooper20", 2),
          ("empty", 1),
          ("mCore1Wdm1", 11),
          ("mCore1Wdm2", 12),
          ("mCore1Wdm3", 13),
          ("mCore1Wdm4", 14),
          ("mCore4Giga", 30),
          ("mCore4Wdm", 20),
          ("mCoreAgent", 9),
          ("mEdge2Giga", 40),
          ("mEdge2Wdm", 50))
    )


_CoreSlotType_Type.__name__ = "Integer32"
_CoreSlotType_Object = MibTableColumn
coreSlotType = _CoreSlotType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 2, 1, 2),
    _CoreSlotType_Type()
)
coreSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotType.setStatus("mandatory")
_CoreSlotPortsNumber_Type = Integer32
_CoreSlotPortsNumber_Object = MibTableColumn
coreSlotPortsNumber = _CoreSlotPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 2, 1, 3),
    _CoreSlotPortsNumber_Type()
)
coreSlotPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotPortsNumber.setStatus("mandatory")
_CorePortTable_Object = MibTable
corePortTable = _CorePortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3)
)
if mibBuilder.loadTexts:
    corePortTable.setStatus("mandatory")
_CorePortEntry_Object = MibTableRow
corePortEntry = _CorePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1)
)
corePortEntry.setIndexNames(
    (0, "CORE-MIB", "coreSlotNumber"),
    (0, "CORE-MIB", "corePortNumber"),
)
if mibBuilder.loadTexts:
    corePortEntry.setStatus("mandatory")
_CoreSlotNumber_Type = Integer32
_CoreSlotNumber_Object = MibTableColumn
coreSlotNumber = _CoreSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 1),
    _CoreSlotNumber_Type()
)
coreSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreSlotNumber.setStatus("mandatory")
_CorePortNumber_Type = Integer32
_CorePortNumber_Object = MibTableColumn
corePortNumber = _CorePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 2),
    _CorePortNumber_Type()
)
corePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortNumber.setStatus("mandatory")


class _CorePortType_Type(Integer32):
    """Custom type corePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coreGigaBit", 2),
          ("coreWDM", 3),
          ("undefined", 1))
    )


_CorePortType_Type.__name__ = "Integer32"
_CorePortType_Object = MibTableColumn
corePortType = _CorePortType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 3),
    _CorePortType_Type()
)
corePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortType.setStatus("mandatory")
_CorePortRingId_Type = RingId
_CorePortRingId_Object = MibTableColumn
corePortRingId = _CorePortRingId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 4),
    _CorePortRingId_Type()
)
corePortRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortRingId.setStatus("mandatory")
_CorePortFirstChannel_Type = Integer32
_CorePortFirstChannel_Object = MibTableColumn
corePortFirstChannel = _CorePortFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 5),
    _CorePortFirstChannel_Type()
)
corePortFirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFirstChannel.setStatus("mandatory")
_CorePortLastChannel_Type = Integer32
_CorePortLastChannel_Object = MibTableColumn
corePortLastChannel = _CorePortLastChannel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 6),
    _CorePortLastChannel_Type()
)
corePortLastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortLastChannel.setStatus("mandatory")
_CorePortLinkStatus_Type = LinkStatus
_CorePortLinkStatus_Object = MibTableColumn
corePortLinkStatus = _CorePortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 7),
    _CorePortLinkStatus_Type()
)
corePortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortLinkStatus.setStatus("mandatory")
_CorePortAdminStatus_Type = AdminStatus
_CorePortAdminStatus_Object = MibTableColumn
corePortAdminStatus = _CorePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 8),
    _CorePortAdminStatus_Type()
)
corePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corePortAdminStatus.setStatus("mandatory")


class _CorePortRingStatus_Type(Integer32):
    """Custom type corePortRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("nonRing", 1))
    )


_CorePortRingStatus_Type.__name__ = "Integer32"
_CorePortRingStatus_Object = MibTableColumn
corePortRingStatus = _CorePortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 9),
    _CorePortRingStatus_Type()
)
corePortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortRingStatus.setStatus("mandatory")
_CorePortFlowControl_Type = FlowControlStatus
_CorePortFlowControl_Object = MibTableColumn
corePortFlowControl = _CorePortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 10),
    _CorePortFlowControl_Type()
)
corePortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corePortFlowControl.setStatus("mandatory")


class _CorePortDuplex_Type(Integer32):
    """Custom type corePortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_CorePortDuplex_Type.__name__ = "Integer32"
_CorePortDuplex_Object = MibTableColumn
corePortDuplex = _CorePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 11),
    _CorePortDuplex_Type()
)
corePortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corePortDuplex.setStatus("mandatory")
_CorePortSpeed_Type = Integer32
_CorePortSpeed_Object = MibTableColumn
corePortSpeed = _CorePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 12),
    _CorePortSpeed_Type()
)
corePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortSpeed.setStatus("mandatory")
_CorePortGoodByteRx_Type = Counter32
_CorePortGoodByteRx_Object = MibTableColumn
corePortGoodByteRx = _CorePortGoodByteRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 13),
    _CorePortGoodByteRx_Type()
)
corePortGoodByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortGoodByteRx.setStatus("mandatory")
_CorePortByteTx_Type = Counter32
_CorePortByteTx_Object = MibTableColumn
corePortByteTx = _CorePortByteTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 14),
    _CorePortByteTx_Type()
)
corePortByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortByteTx.setStatus("mandatory")
_CorePortGoodFrameRx_Type = Counter32
_CorePortGoodFrameRx_Object = MibTableColumn
corePortGoodFrameRx = _CorePortGoodFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 15),
    _CorePortGoodFrameRx_Type()
)
corePortGoodFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortGoodFrameRx.setStatus("mandatory")
_CorePortFrameTx_Type = Counter32
_CorePortFrameTx_Object = MibTableColumn
corePortFrameTx = _CorePortFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 16),
    _CorePortFrameTx_Type()
)
corePortFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFrameTx.setStatus("mandatory")
_CorePortTotalByteRx_Type = Counter32
_CorePortTotalByteRx_Object = MibTableColumn
corePortTotalByteRx = _CorePortTotalByteRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 17),
    _CorePortTotalByteRx_Type()
)
corePortTotalByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortTotalByteRx.setStatus("mandatory")
_CorePortTotalFrameRx_Type = Counter32
_CorePortTotalFrameRx_Object = MibTableColumn
corePortTotalFrameRx = _CorePortTotalFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 18),
    _CorePortTotalFrameRx_Type()
)
corePortTotalFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortTotalFrameRx.setStatus("mandatory")
_CorePortBcstFrameRx_Type = Counter32
_CorePortBcstFrameRx_Object = MibTableColumn
corePortBcstFrameRx = _CorePortBcstFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 19),
    _CorePortBcstFrameRx_Type()
)
corePortBcstFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortBcstFrameRx.setStatus("mandatory")
_CorePortMcstFrameRx_Type = Counter32
_CorePortMcstFrameRx_Object = MibTableColumn
corePortMcstFrameRx = _CorePortMcstFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 20),
    _CorePortMcstFrameRx_Type()
)
corePortMcstFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortMcstFrameRx.setStatus("mandatory")
_CorePortCRCError_Type = Counter32
_CorePortCRCError_Object = MibTableColumn
corePortCRCError = _CorePortCRCError_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 21),
    _CorePortCRCError_Type()
)
corePortCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortCRCError.setStatus("mandatory")
_CorePortOversize_Type = Counter32
_CorePortOversize_Object = MibTableColumn
corePortOversize = _CorePortOversize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 22),
    _CorePortOversize_Type()
)
corePortOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortOversize.setStatus("mandatory")
_CorePortFragment_Type = Counter32
_CorePortFragment_Object = MibTableColumn
corePortFragment = _CorePortFragment_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 23),
    _CorePortFragment_Type()
)
corePortFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFragment.setStatus("mandatory")
_CorePortJabber_Type = Counter32
_CorePortJabber_Object = MibTableColumn
corePortJabber = _CorePortJabber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 24),
    _CorePortJabber_Type()
)
corePortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortJabber.setStatus("mandatory")
_CorePortCollision_Type = Counter32
_CorePortCollision_Object = MibTableColumn
corePortCollision = _CorePortCollision_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 25),
    _CorePortCollision_Type()
)
corePortCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortCollision.setStatus("mandatory")
_CorePortLateCollision_Type = Counter32
_CorePortLateCollision_Object = MibTableColumn
corePortLateCollision = _CorePortLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 26),
    _CorePortLateCollision_Type()
)
corePortLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortLateCollision.setStatus("mandatory")
_CorePortFr64_Type = Counter32
_CorePortFr64_Object = MibTableColumn
corePortFr64 = _CorePortFr64_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 27),
    _CorePortFr64_Type()
)
corePortFr64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr64.setStatus("mandatory")
_CorePortFr64to127_Type = Counter32
_CorePortFr64to127_Object = MibTableColumn
corePortFr64to127 = _CorePortFr64to127_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 28),
    _CorePortFr64to127_Type()
)
corePortFr64to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr64to127.setStatus("mandatory")
_CorePortFr128to255_Type = Counter32
_CorePortFr128to255_Object = MibTableColumn
corePortFr128to255 = _CorePortFr128to255_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 29),
    _CorePortFr128to255_Type()
)
corePortFr128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr128to255.setStatus("mandatory")
_CorePortFr256to511_Type = Counter32
_CorePortFr256to511_Object = MibTableColumn
corePortFr256to511 = _CorePortFr256to511_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 30),
    _CorePortFr256to511_Type()
)
corePortFr256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr256to511.setStatus("mandatory")
_CorePortFr512to1023_Type = Counter32
_CorePortFr512to1023_Object = MibTableColumn
corePortFr512to1023 = _CorePortFr512to1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 31),
    _CorePortFr512to1023_Type()
)
corePortFr512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr512to1023.setStatus("mandatory")
_CorePortFr1024to1023_Type = Counter32
_CorePortFr1024to1023_Object = MibTableColumn
corePortFr1024to1023 = _CorePortFr1024to1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 32),
    _CorePortFr1024to1023_Type()
)
corePortFr1024to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr1024to1023.setStatus("mandatory")
_CorePortFr1023toMAX_Type = Counter32
_CorePortFr1023toMAX_Object = MibTableColumn
corePortFr1023toMAX = _CorePortFr1023toMAX_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 33),
    _CorePortFr1023toMAX_Type()
)
corePortFr1023toMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortFr1023toMAX.setStatus("mandatory")
_CorePortDropped_Type = Counter32
_CorePortDropped_Object = MibTableColumn
corePortDropped = _CorePortDropped_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 34),
    _CorePortDropped_Type()
)
corePortDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortDropped.setStatus("mandatory")
_CorePortMcstFrameTx_Type = Counter32
_CorePortMcstFrameTx_Object = MibTableColumn
corePortMcstFrameTx = _CorePortMcstFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 35),
    _CorePortMcstFrameTx_Type()
)
corePortMcstFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortMcstFrameTx.setStatus("mandatory")
_CorePortBcstFrameTx_Type = Counter32
_CorePortBcstFrameTx_Object = MibTableColumn
corePortBcstFrameTx = _CorePortBcstFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 36),
    _CorePortBcstFrameTx_Type()
)
corePortBcstFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortBcstFrameTx.setStatus("mandatory")
_CorePortUndersize_Type = Counter32
_CorePortUndersize_Object = MibTableColumn
corePortUndersize = _CorePortUndersize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 3, 1, 37),
    _CorePortUndersize_Type()
)
corePortUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corePortUndersize.setStatus("mandatory")
_CoreChannelTable_Object = MibTable
coreChannelTable = _CoreChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4)
)
if mibBuilder.loadTexts:
    coreChannelTable.setStatus("mandatory")
_CoreChannelEntry_Object = MibTableRow
coreChannelEntry = _CoreChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1)
)
coreChannelEntry.setIndexNames(
    (0, "CORE-MIB", "coreChannelRingId"),
    (0, "CORE-MIB", "coreChannelNumber"),
)
if mibBuilder.loadTexts:
    coreChannelEntry.setStatus("mandatory")
_CoreChannelRingId_Type = RingId
_CoreChannelRingId_Object = MibTableColumn
coreChannelRingId = _CoreChannelRingId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 1),
    _CoreChannelRingId_Type()
)
coreChannelRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelRingId.setStatus("mandatory")
_CoreChannelNumber_Type = Integer32
_CoreChannelNumber_Object = MibTableColumn
coreChannelNumber = _CoreChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 2),
    _CoreChannelNumber_Type()
)
coreChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelNumber.setStatus("mandatory")
_CoreChannelTxPwr_Type = LedColor
_CoreChannelTxPwr_Object = MibTableColumn
coreChannelTxPwr = _CoreChannelTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 3),
    _CoreChannelTxPwr_Type()
)
coreChannelTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelTxPwr.setStatus("mandatory")
_CoreChannelTxWave_Type = LedColor
_CoreChannelTxWave_Object = MibTableColumn
coreChannelTxWave = _CoreChannelTxWave_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 4),
    _CoreChannelTxWave_Type()
)
coreChannelTxWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelTxWave.setStatus("mandatory")
_CoreChannelRxPwr_Type = LedColor
_CoreChannelRxPwr_Object = MibTableColumn
coreChannelRxPwr = _CoreChannelRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 5),
    _CoreChannelRxPwr_Type()
)
coreChannelRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelRxPwr.setStatus("mandatory")
_CoreChannelRxLink_Type = LedColor
_CoreChannelRxLink_Object = MibTableColumn
coreChannelRxLink = _CoreChannelRxLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 9, 4, 1, 6),
    _CoreChannelRxLink_Type()
)
coreChannelRxLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreChannelRxLink.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORE-MIB",
    **{"LedColor": LedColor,
       "RingId": RingId,
       "AdminStatus": AdminStatus,
       "LinkStatus": LinkStatus,
       "FlowControlStatus": FlowControlStatus,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "core": core,
       "coreInfo": coreInfo,
       "coreSlotsMaxNumber": coreSlotsMaxNumber,
       "coreChannelsMaxNumber": coreChannelsMaxNumber,
       "coreRingsMaxNumber": coreRingsMaxNumber,
       "coreSlotsActNumber": coreSlotsActNumber,
       "coreRingsActNumber": coreRingsActNumber,
       "coreSlotsTable": coreSlotsTable,
       "coreSlotEntry": coreSlotEntry,
       "coreSlotPosition": coreSlotPosition,
       "coreSlotType": coreSlotType,
       "coreSlotPortsNumber": coreSlotPortsNumber,
       "corePortTable": corePortTable,
       "corePortEntry": corePortEntry,
       "coreSlotNumber": coreSlotNumber,
       "corePortNumber": corePortNumber,
       "corePortType": corePortType,
       "corePortRingId": corePortRingId,
       "corePortFirstChannel": corePortFirstChannel,
       "corePortLastChannel": corePortLastChannel,
       "corePortLinkStatus": corePortLinkStatus,
       "corePortAdminStatus": corePortAdminStatus,
       "corePortRingStatus": corePortRingStatus,
       "corePortFlowControl": corePortFlowControl,
       "corePortDuplex": corePortDuplex,
       "corePortSpeed": corePortSpeed,
       "corePortGoodByteRx": corePortGoodByteRx,
       "corePortByteTx": corePortByteTx,
       "corePortGoodFrameRx": corePortGoodFrameRx,
       "corePortFrameTx": corePortFrameTx,
       "corePortTotalByteRx": corePortTotalByteRx,
       "corePortTotalFrameRx": corePortTotalFrameRx,
       "corePortBcstFrameRx": corePortBcstFrameRx,
       "corePortMcstFrameRx": corePortMcstFrameRx,
       "corePortCRCError": corePortCRCError,
       "corePortOversize": corePortOversize,
       "corePortFragment": corePortFragment,
       "corePortJabber": corePortJabber,
       "corePortCollision": corePortCollision,
       "corePortLateCollision": corePortLateCollision,
       "corePortFr64": corePortFr64,
       "corePortFr64to127": corePortFr64to127,
       "corePortFr128to255": corePortFr128to255,
       "corePortFr256to511": corePortFr256to511,
       "corePortFr512to1023": corePortFr512to1023,
       "corePortFr1024to1023": corePortFr1024to1023,
       "corePortFr1023toMAX": corePortFr1023toMAX,
       "corePortDropped": corePortDropped,
       "corePortMcstFrameTx": corePortMcstFrameTx,
       "corePortBcstFrameTx": corePortBcstFrameTx,
       "corePortUndersize": corePortUndersize,
       "coreChannelTable": coreChannelTable,
       "coreChannelEntry": coreChannelEntry,
       "coreChannelRingId": coreChannelRingId,
       "coreChannelNumber": coreChannelNumber,
       "coreChannelTxPwr": coreChannelTxPwr,
       "coreChannelTxWave": coreChannelTxWave,
       "coreChannelRxPwr": coreChannelRxPwr,
       "coreChannelRxLink": coreChannelRxLink}
)
