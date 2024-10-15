# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-TOKEN-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-TOKEN-RING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:54 2024
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
 NotificationType,
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
    "NotificationType",
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComSysTokenRingPort_ObjectIdentity = ObjectIdentity
a3ComSysTokenRingPort = _A3ComSysTokenRingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13)
)
_A3ComSysTokenRingPortCount_Type = Integer32
_A3ComSysTokenRingPortCount_Object = MibScalar
a3ComSysTokenRingPortCount = _A3ComSysTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 1),
    _A3ComSysTokenRingPortCount_Type()
)
a3ComSysTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortCount.setStatus("mandatory")
_A3ComSysTokenRingPortTable_Object = MibTable
a3ComSysTokenRingPortTable = _A3ComSysTokenRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2)
)
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTable.setStatus("mandatory")
_A3ComSysTokenRingPortEntry_Object = MibTableRow
a3ComSysTokenRingPortEntry = _A3ComSysTokenRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1)
)
a3ComSysTokenRingPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-TOKEN-RING-MIB", "a3ComSysTokenRingPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortEntry.setStatus("mandatory")


class _A3ComSysTokenRingPortIndex_Type(Integer32):
    """Custom type a3ComSysTokenRingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysTokenRingPortIndex_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortIndex_Object = MibTableColumn
a3ComSysTokenRingPortIndex = _A3ComSysTokenRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 1),
    _A3ComSysTokenRingPortIndex_Type()
)
a3ComSysTokenRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortIndex.setStatus("mandatory")


class _A3ComSysTokenRingPortIfIndex_Type(Integer32):
    """Custom type a3ComSysTokenRingPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysTokenRingPortIfIndex_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortIfIndex_Object = MibTableColumn
a3ComSysTokenRingPortIfIndex = _A3ComSysTokenRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 2),
    _A3ComSysTokenRingPortIfIndex_Type()
)
a3ComSysTokenRingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortIfIndex.setStatus("mandatory")


class _A3ComSysTokenRingPortLabel_Type(DisplayString):
    """Custom type a3ComSysTokenRingPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysTokenRingPortLabel_Type.__name__ = "DisplayString"
_A3ComSysTokenRingPortLabel_Object = MibTableColumn
a3ComSysTokenRingPortLabel = _A3ComSysTokenRingPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 3),
    _A3ComSysTokenRingPortLabel_Type()
)
a3ComSysTokenRingPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLabel.setStatus("mandatory")


class _A3ComSysTokenRingPortInsertStatus_Type(Integer32):
    """Custom type a3ComSysTokenRingPortInsertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deinserted", 2),
          ("inserted", 1))
    )


_A3ComSysTokenRingPortInsertStatus_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortInsertStatus_Object = MibTableColumn
a3ComSysTokenRingPortInsertStatus = _A3ComSysTokenRingPortInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 4),
    _A3ComSysTokenRingPortInsertStatus_Type()
)
a3ComSysTokenRingPortInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortInsertStatus.setStatus("mandatory")


class _A3ComSysTokenRingPortType_Type(Integer32):
    """Custom type a3ComSysTokenRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("rj45", 1))
    )


_A3ComSysTokenRingPortType_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortType_Object = MibTableColumn
a3ComSysTokenRingPortType = _A3ComSysTokenRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 5),
    _A3ComSysTokenRingPortType_Type()
)
a3ComSysTokenRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortType.setStatus("mandatory")


class _A3ComSysTokenRingPortMode_Type(Integer32):
    """Custom type a3ComSysTokenRingPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lobe", 2),
          ("station", 1))
    )


_A3ComSysTokenRingPortMode_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortMode_Object = MibTableColumn
a3ComSysTokenRingPortMode = _A3ComSysTokenRingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 6),
    _A3ComSysTokenRingPortMode_Type()
)
a3ComSysTokenRingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortMode.setStatus("mandatory")


class _A3ComSysTokenRingPortSpeed_Type(Integer32):
    """Custom type a3ComSysTokenRingPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2),
          ("sixteenMegabitETR", 3))
    )


_A3ComSysTokenRingPortSpeed_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortSpeed_Object = MibTableColumn
a3ComSysTokenRingPortSpeed = _A3ComSysTokenRingPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 7),
    _A3ComSysTokenRingPortSpeed_Type()
)
a3ComSysTokenRingPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSpeed.setStatus("mandatory")
_A3ComSysTokenRingPortLineErrors_Type = Counter32
_A3ComSysTokenRingPortLineErrors_Object = MibTableColumn
a3ComSysTokenRingPortLineErrors = _A3ComSysTokenRingPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 8),
    _A3ComSysTokenRingPortLineErrors_Type()
)
a3ComSysTokenRingPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLineErrors.setStatus("mandatory")
_A3ComSysTokenRingPortBurstErrors_Type = Counter32
_A3ComSysTokenRingPortBurstErrors_Object = MibTableColumn
a3ComSysTokenRingPortBurstErrors = _A3ComSysTokenRingPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 9),
    _A3ComSysTokenRingPortBurstErrors_Type()
)
a3ComSysTokenRingPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortBurstErrors.setStatus("mandatory")
_A3ComSysTokenRingPortACErrors_Type = Counter32
_A3ComSysTokenRingPortACErrors_Object = MibTableColumn
a3ComSysTokenRingPortACErrors = _A3ComSysTokenRingPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 10),
    _A3ComSysTokenRingPortACErrors_Type()
)
a3ComSysTokenRingPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortACErrors.setStatus("mandatory")
_A3ComSysTokenRingPortAbortTransErrors_Type = Counter32
_A3ComSysTokenRingPortAbortTransErrors_Object = MibTableColumn
a3ComSysTokenRingPortAbortTransErrors = _A3ComSysTokenRingPortAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 11),
    _A3ComSysTokenRingPortAbortTransErrors_Type()
)
a3ComSysTokenRingPortAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortAbortTransErrors.setStatus("mandatory")
_A3ComSysTokenRingPortInternalErrors_Type = Counter32
_A3ComSysTokenRingPortInternalErrors_Object = MibTableColumn
a3ComSysTokenRingPortInternalErrors = _A3ComSysTokenRingPortInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 12),
    _A3ComSysTokenRingPortInternalErrors_Type()
)
a3ComSysTokenRingPortInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortInternalErrors.setStatus("mandatory")
_A3ComSysTokenRingPortLostFrameErrors_Type = Counter32
_A3ComSysTokenRingPortLostFrameErrors_Object = MibTableColumn
a3ComSysTokenRingPortLostFrameErrors = _A3ComSysTokenRingPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 13),
    _A3ComSysTokenRingPortLostFrameErrors_Type()
)
a3ComSysTokenRingPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLostFrameErrors.setStatus("mandatory")
_A3ComSysTokenRingPortReceiveCongestionErrors_Type = Counter32
_A3ComSysTokenRingPortReceiveCongestionErrors_Object = MibTableColumn
a3ComSysTokenRingPortReceiveCongestionErrors = _A3ComSysTokenRingPortReceiveCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 14),
    _A3ComSysTokenRingPortReceiveCongestionErrors_Type()
)
a3ComSysTokenRingPortReceiveCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortReceiveCongestionErrors.setStatus("mandatory")
_A3ComSysTokenRingPortFrameCopiedErrors_Type = Counter32
_A3ComSysTokenRingPortFrameCopiedErrors_Object = MibTableColumn
a3ComSysTokenRingPortFrameCopiedErrors = _A3ComSysTokenRingPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 15),
    _A3ComSysTokenRingPortFrameCopiedErrors_Type()
)
a3ComSysTokenRingPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortFrameCopiedErrors.setStatus("mandatory")
_A3ComSysTokenRingPortTokenErrors_Type = Counter32
_A3ComSysTokenRingPortTokenErrors_Object = MibTableColumn
a3ComSysTokenRingPortTokenErrors = _A3ComSysTokenRingPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 16),
    _A3ComSysTokenRingPortTokenErrors_Type()
)
a3ComSysTokenRingPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTokenErrors.setStatus("mandatory")
_A3ComSysTokenRingPortSoftErrors_Type = Counter32
_A3ComSysTokenRingPortSoftErrors_Object = MibTableColumn
a3ComSysTokenRingPortSoftErrors = _A3ComSysTokenRingPortSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 17),
    _A3ComSysTokenRingPortSoftErrors_Type()
)
a3ComSysTokenRingPortSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSoftErrors.setStatus("mandatory")
_A3ComSysTokenRingPortHardErrors_Type = Counter32
_A3ComSysTokenRingPortHardErrors_Object = MibTableColumn
a3ComSysTokenRingPortHardErrors = _A3ComSysTokenRingPortHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 18),
    _A3ComSysTokenRingPortHardErrors_Type()
)
a3ComSysTokenRingPortHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortHardErrors.setStatus("mandatory")
_A3ComSysTokenRingPortTransmitBeacons_Type = Counter32
_A3ComSysTokenRingPortTransmitBeacons_Object = MibTableColumn
a3ComSysTokenRingPortTransmitBeacons = _A3ComSysTokenRingPortTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 19),
    _A3ComSysTokenRingPortTransmitBeacons_Type()
)
a3ComSysTokenRingPortTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTransmitBeacons.setStatus("mandatory")
_A3ComSysTokenRingPortLobeWires_Type = Counter32
_A3ComSysTokenRingPortLobeWires_Object = MibTableColumn
a3ComSysTokenRingPortLobeWires = _A3ComSysTokenRingPortLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 20),
    _A3ComSysTokenRingPortLobeWires_Type()
)
a3ComSysTokenRingPortLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLobeWires.setStatus("mandatory")
_A3ComSysTokenRingPortRemoves_Type = Counter32
_A3ComSysTokenRingPortRemoves_Object = MibTableColumn
a3ComSysTokenRingPortRemoves = _A3ComSysTokenRingPortRemoves_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 21),
    _A3ComSysTokenRingPortRemoves_Type()
)
a3ComSysTokenRingPortRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortRemoves.setStatus("mandatory")
_A3ComSysTokenRingPortSingles_Type = Counter32
_A3ComSysTokenRingPortSingles_Object = MibTableColumn
a3ComSysTokenRingPortSingles = _A3ComSysTokenRingPortSingles_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 22),
    _A3ComSysTokenRingPortSingles_Type()
)
a3ComSysTokenRingPortSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSingles.setStatus("mandatory")
_A3ComSysTokenRingPortFreqErrors_Type = Counter32
_A3ComSysTokenRingPortFreqErrors_Object = MibTableColumn
a3ComSysTokenRingPortFreqErrors = _A3ComSysTokenRingPortFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 23),
    _A3ComSysTokenRingPortFreqErrors_Type()
)
a3ComSysTokenRingPortFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortFreqErrors.setStatus("mandatory")
_A3ComSysTokenRingPortRingStatus_Type = Integer32
_A3ComSysTokenRingPortRingStatus_Object = MibTableColumn
a3ComSysTokenRingPortRingStatus = _A3ComSysTokenRingPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 24),
    _A3ComSysTokenRingPortRingStatus_Type()
)
a3ComSysTokenRingPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortRingStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-TOKEN-RING-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComSysTokenRingPort": a3ComSysTokenRingPort,
       "a3ComSysTokenRingPortCount": a3ComSysTokenRingPortCount,
       "a3ComSysTokenRingPortTable": a3ComSysTokenRingPortTable,
       "a3ComSysTokenRingPortEntry": a3ComSysTokenRingPortEntry,
       "a3ComSysTokenRingPortIndex": a3ComSysTokenRingPortIndex,
       "a3ComSysTokenRingPortIfIndex": a3ComSysTokenRingPortIfIndex,
       "a3ComSysTokenRingPortLabel": a3ComSysTokenRingPortLabel,
       "a3ComSysTokenRingPortInsertStatus": a3ComSysTokenRingPortInsertStatus,
       "a3ComSysTokenRingPortType": a3ComSysTokenRingPortType,
       "a3ComSysTokenRingPortMode": a3ComSysTokenRingPortMode,
       "a3ComSysTokenRingPortSpeed": a3ComSysTokenRingPortSpeed,
       "a3ComSysTokenRingPortLineErrors": a3ComSysTokenRingPortLineErrors,
       "a3ComSysTokenRingPortBurstErrors": a3ComSysTokenRingPortBurstErrors,
       "a3ComSysTokenRingPortACErrors": a3ComSysTokenRingPortACErrors,
       "a3ComSysTokenRingPortAbortTransErrors": a3ComSysTokenRingPortAbortTransErrors,
       "a3ComSysTokenRingPortInternalErrors": a3ComSysTokenRingPortInternalErrors,
       "a3ComSysTokenRingPortLostFrameErrors": a3ComSysTokenRingPortLostFrameErrors,
       "a3ComSysTokenRingPortReceiveCongestionErrors": a3ComSysTokenRingPortReceiveCongestionErrors,
       "a3ComSysTokenRingPortFrameCopiedErrors": a3ComSysTokenRingPortFrameCopiedErrors,
       "a3ComSysTokenRingPortTokenErrors": a3ComSysTokenRingPortTokenErrors,
       "a3ComSysTokenRingPortSoftErrors": a3ComSysTokenRingPortSoftErrors,
       "a3ComSysTokenRingPortHardErrors": a3ComSysTokenRingPortHardErrors,
       "a3ComSysTokenRingPortTransmitBeacons": a3ComSysTokenRingPortTransmitBeacons,
       "a3ComSysTokenRingPortLobeWires": a3ComSysTokenRingPortLobeWires,
       "a3ComSysTokenRingPortRemoves": a3ComSysTokenRingPortRemoves,
       "a3ComSysTokenRingPortSingles": a3ComSysTokenRingPortSingles,
       "a3ComSysTokenRingPortFreqErrors": a3ComSysTokenRingPortFreqErrors,
       "a3ComSysTokenRingPortRingStatus": a3ComSysTokenRingPortRingStatus}
)
