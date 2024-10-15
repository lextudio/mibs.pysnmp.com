# SNMP MIB module (XYLAN-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:59 2024
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

(xylanPportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPportArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx1Port_ObjectIdentity = ObjectIdentity
dsx1Port = _Dsx1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1)
)
_Dsx1PortConfigTable_Object = MibTable
dsx1PortConfigTable = _Dsx1PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1PortConfigTable.setStatus("mandatory")
_Dsx1PortConfigEntry_Object = MibTableRow
dsx1PortConfigEntry = _Dsx1PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1)
)
dsx1PortConfigEntry.setIndexNames(
    (0, "XYLAN-DS1-MIB", "dsx1PortConfigSlotIndex"),
    (0, "XYLAN-DS1-MIB", "dsx1PortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    dsx1PortConfigEntry.setStatus("mandatory")


class _Dsx1PortConfigSlotIndex_Type(Integer32):
    """Custom type dsx1PortConfigSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Dsx1PortConfigSlotIndex_Type.__name__ = "Integer32"
_Dsx1PortConfigSlotIndex_Object = MibTableColumn
dsx1PortConfigSlotIndex = _Dsx1PortConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 1),
    _Dsx1PortConfigSlotIndex_Type()
)
dsx1PortConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortConfigSlotIndex.setStatus("mandatory")


class _Dsx1PortConfigPortIndex_Type(Integer32):
    """Custom type dsx1PortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dsx1PortConfigPortIndex_Type.__name__ = "Integer32"
_Dsx1PortConfigPortIndex_Object = MibTableColumn
dsx1PortConfigPortIndex = _Dsx1PortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 2),
    _Dsx1PortConfigPortIndex_Type()
)
dsx1PortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortConfigPortIndex.setStatus("mandatory")


class _Dsx1PortConfigIfType_Type(Integer32):
    """Custom type dsx1PortConfigIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_Dsx1PortConfigIfType_Type.__name__ = "Integer32"
_Dsx1PortConfigIfType_Object = MibTableColumn
dsx1PortConfigIfType = _Dsx1PortConfigIfType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 3),
    _Dsx1PortConfigIfType_Type()
)
dsx1PortConfigIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortConfigIfType.setStatus("mandatory")


class _Dsx1PortFdlRole_Type(Integer32):
    """Custom type dsx1PortFdlRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_Dsx1PortFdlRole_Type.__name__ = "Integer32"
_Dsx1PortFdlRole_Object = MibTableColumn
dsx1PortFdlRole = _Dsx1PortFdlRole_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 4),
    _Dsx1PortFdlRole_Type()
)
dsx1PortFdlRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortFdlRole.setStatus("mandatory")


class _Dsx1PortNfasAlign_Type(Integer32):
    """Custom type dsx1PortNfasAlign based on Integer32"""
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


_Dsx1PortNfasAlign_Type.__name__ = "Integer32"
_Dsx1PortNfasAlign_Object = MibTableColumn
dsx1PortNfasAlign = _Dsx1PortNfasAlign_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 5),
    _Dsx1PortNfasAlign_Type()
)
dsx1PortNfasAlign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortNfasAlign.setStatus("mandatory")


class _Dsx1PortConfigYelAlarmDetectEnable_Type(Integer32):
    """Custom type dsx1PortConfigYelAlarmDetectEnable based on Integer32"""
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


_Dsx1PortConfigYelAlarmDetectEnable_Type.__name__ = "Integer32"
_Dsx1PortConfigYelAlarmDetectEnable_Object = MibTableColumn
dsx1PortConfigYelAlarmDetectEnable = _Dsx1PortConfigYelAlarmDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 6),
    _Dsx1PortConfigYelAlarmDetectEnable_Type()
)
dsx1PortConfigYelAlarmDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortConfigYelAlarmDetectEnable.setStatus("mandatory")
_Dsx1PortStatsTable_Object = MibTable
dsx1PortStatsTable = _Dsx1PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2)
)
if mibBuilder.loadTexts:
    dsx1PortStatsTable.setStatus("mandatory")
_Dsx1PortStatsEntry_Object = MibTableRow
dsx1PortStatsEntry = _Dsx1PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1)
)
dsx1PortStatsEntry.setIndexNames(
    (0, "XYLAN-DS1-MIB", "dsx1PortStatsSlotIndex"),
    (0, "XYLAN-DS1-MIB", "dsx1PortStatsPortIndex"),
)
if mibBuilder.loadTexts:
    dsx1PortStatsEntry.setStatus("mandatory")


class _Dsx1PortStatsSlotIndex_Type(Integer32):
    """Custom type dsx1PortStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Dsx1PortStatsSlotIndex_Type.__name__ = "Integer32"
_Dsx1PortStatsSlotIndex_Object = MibTableColumn
dsx1PortStatsSlotIndex = _Dsx1PortStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 1),
    _Dsx1PortStatsSlotIndex_Type()
)
dsx1PortStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsSlotIndex.setStatus("mandatory")


class _Dsx1PortStatsPortIndex_Type(Integer32):
    """Custom type dsx1PortStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dsx1PortStatsPortIndex_Type.__name__ = "Integer32"
_Dsx1PortStatsPortIndex_Object = MibTableColumn
dsx1PortStatsPortIndex = _Dsx1PortStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 2),
    _Dsx1PortStatsPortIndex_Type()
)
dsx1PortStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsPortIndex.setStatus("mandatory")
_Dsx1PortStatsLossOfSignal_Type = Counter32
_Dsx1PortStatsLossOfSignal_Object = MibTableColumn
dsx1PortStatsLossOfSignal = _Dsx1PortStatsLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 3),
    _Dsx1PortStatsLossOfSignal_Type()
)
dsx1PortStatsLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsLossOfSignal.setStatus("mandatory")
_Dsx1PortStatsOutOfFrame_Type = Counter32
_Dsx1PortStatsOutOfFrame_Object = MibTableColumn
dsx1PortStatsOutOfFrame = _Dsx1PortStatsOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 4),
    _Dsx1PortStatsOutOfFrame_Type()
)
dsx1PortStatsOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsOutOfFrame.setStatus("mandatory")
_Dsx1PortStatsRedAlarmEvent_Type = Counter32
_Dsx1PortStatsRedAlarmEvent_Object = MibTableColumn
dsx1PortStatsRedAlarmEvent = _Dsx1PortStatsRedAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 5),
    _Dsx1PortStatsRedAlarmEvent_Type()
)
dsx1PortStatsRedAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsRedAlarmEvent.setStatus("mandatory")
_Dsx1PortStatsYellowAlarmEvent_Type = Counter32
_Dsx1PortStatsYellowAlarmEvent_Object = MibTableColumn
dsx1PortStatsYellowAlarmEvent = _Dsx1PortStatsYellowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 6),
    _Dsx1PortStatsYellowAlarmEvent_Type()
)
dsx1PortStatsYellowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsYellowAlarmEvent.setStatus("mandatory")
_Dsx1PortStatsSquelchAlarmEvent_Type = Counter32
_Dsx1PortStatsSquelchAlarmEvent_Object = MibTableColumn
dsx1PortStatsSquelchAlarmEvent = _Dsx1PortStatsSquelchAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 7),
    _Dsx1PortStatsSquelchAlarmEvent_Type()
)
dsx1PortStatsSquelchAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsSquelchAlarmEvent.setStatus("mandatory")
_Dsx1PortStatsBipolarVioEvent_Type = Counter32
_Dsx1PortStatsBipolarVioEvent_Object = MibTableColumn
dsx1PortStatsBipolarVioEvent = _Dsx1PortStatsBipolarVioEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 8),
    _Dsx1PortStatsBipolarVioEvent_Type()
)
dsx1PortStatsBipolarVioEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsBipolarVioEvent.setStatus("mandatory")
_Dsx1PortStatsAISEvent_Type = Counter32
_Dsx1PortStatsAISEvent_Object = MibTableColumn
dsx1PortStatsAISEvent = _Dsx1PortStatsAISEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 9),
    _Dsx1PortStatsAISEvent_Type()
)
dsx1PortStatsAISEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsAISEvent.setStatus("mandatory")
_Dsx1PortStatsCrcErrorEvent_Type = Counter32
_Dsx1PortStatsCrcErrorEvent_Object = MibTableColumn
dsx1PortStatsCrcErrorEvent = _Dsx1PortStatsCrcErrorEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 10),
    _Dsx1PortStatsCrcErrorEvent_Type()
)
dsx1PortStatsCrcErrorEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsCrcErrorEvent.setStatus("mandatory")
_Dsx1PortStatsOutOfSubMultiFrame_Type = Counter32
_Dsx1PortStatsOutOfSubMultiFrame_Object = MibTableColumn
dsx1PortStatsOutOfSubMultiFrame = _Dsx1PortStatsOutOfSubMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 11),
    _Dsx1PortStatsOutOfSubMultiFrame_Type()
)
dsx1PortStatsOutOfSubMultiFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsOutOfSubMultiFrame.setStatus("mandatory")
_Dsx1PortStatsOutOfTs16MultiFrame_Type = Counter32
_Dsx1PortStatsOutOfTs16MultiFrame_Object = MibTableColumn
dsx1PortStatsOutOfTs16MultiFrame = _Dsx1PortStatsOutOfTs16MultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 12),
    _Dsx1PortStatsOutOfTs16MultiFrame_Type()
)
dsx1PortStatsOutOfTs16MultiFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsOutOfTs16MultiFrame.setStatus("mandatory")
_Dsx1PortStatsRemFrameAlarm_Type = Counter32
_Dsx1PortStatsRemFrameAlarm_Object = MibTableColumn
dsx1PortStatsRemFrameAlarm = _Dsx1PortStatsRemFrameAlarm_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 13),
    _Dsx1PortStatsRemFrameAlarm_Type()
)
dsx1PortStatsRemFrameAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsRemFrameAlarm.setStatus("mandatory")
_Dsx1PortStatsRemMultiFrameAlarm_Type = Counter32
_Dsx1PortStatsRemMultiFrameAlarm_Object = MibTableColumn
dsx1PortStatsRemMultiFrameAlarm = _Dsx1PortStatsRemMultiFrameAlarm_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 14),
    _Dsx1PortStatsRemMultiFrameAlarm_Type()
)
dsx1PortStatsRemMultiFrameAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsRemMultiFrameAlarm.setStatus("mandatory")
_Dsx1PortStatsFarEndBlkError_Type = Counter32
_Dsx1PortStatsFarEndBlkError_Object = MibTableColumn
dsx1PortStatsFarEndBlkError = _Dsx1PortStatsFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 15),
    _Dsx1PortStatsFarEndBlkError_Type()
)
dsx1PortStatsFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsFarEndBlkError.setStatus("mandatory")
_Dsx1PortStatsFramingBitError_Type = Counter32
_Dsx1PortStatsFramingBitError_Object = MibTableColumn
dsx1PortStatsFramingBitError = _Dsx1PortStatsFramingBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 16),
    _Dsx1PortStatsFramingBitError_Type()
)
dsx1PortStatsFramingBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortStatsFramingBitError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-DS1-MIB",
    **{"dsx1Port": dsx1Port,
       "dsx1PortConfigTable": dsx1PortConfigTable,
       "dsx1PortConfigEntry": dsx1PortConfigEntry,
       "dsx1PortConfigSlotIndex": dsx1PortConfigSlotIndex,
       "dsx1PortConfigPortIndex": dsx1PortConfigPortIndex,
       "dsx1PortConfigIfType": dsx1PortConfigIfType,
       "dsx1PortFdlRole": dsx1PortFdlRole,
       "dsx1PortNfasAlign": dsx1PortNfasAlign,
       "dsx1PortConfigYelAlarmDetectEnable": dsx1PortConfigYelAlarmDetectEnable,
       "dsx1PortStatsTable": dsx1PortStatsTable,
       "dsx1PortStatsEntry": dsx1PortStatsEntry,
       "dsx1PortStatsSlotIndex": dsx1PortStatsSlotIndex,
       "dsx1PortStatsPortIndex": dsx1PortStatsPortIndex,
       "dsx1PortStatsLossOfSignal": dsx1PortStatsLossOfSignal,
       "dsx1PortStatsOutOfFrame": dsx1PortStatsOutOfFrame,
       "dsx1PortStatsRedAlarmEvent": dsx1PortStatsRedAlarmEvent,
       "dsx1PortStatsYellowAlarmEvent": dsx1PortStatsYellowAlarmEvent,
       "dsx1PortStatsSquelchAlarmEvent": dsx1PortStatsSquelchAlarmEvent,
       "dsx1PortStatsBipolarVioEvent": dsx1PortStatsBipolarVioEvent,
       "dsx1PortStatsAISEvent": dsx1PortStatsAISEvent,
       "dsx1PortStatsCrcErrorEvent": dsx1PortStatsCrcErrorEvent,
       "dsx1PortStatsOutOfSubMultiFrame": dsx1PortStatsOutOfSubMultiFrame,
       "dsx1PortStatsOutOfTs16MultiFrame": dsx1PortStatsOutOfTs16MultiFrame,
       "dsx1PortStatsRemFrameAlarm": dsx1PortStatsRemFrameAlarm,
       "dsx1PortStatsRemMultiFrameAlarm": dsx1PortStatsRemMultiFrameAlarm,
       "dsx1PortStatsFarEndBlkError": dsx1PortStatsFarEndBlkError,
       "dsx1PortStatsFramingBitError": dsx1PortStatsFramingBitError}
)
