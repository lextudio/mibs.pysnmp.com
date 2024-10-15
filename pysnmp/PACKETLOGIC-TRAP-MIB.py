# SNMP MIB module (PACKETLOGIC-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETLOGIC-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:11 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pl2Trap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8)
)
pl2Trap.setRevisions(
        ("2012-09-26 12:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pl2Traps_ObjectIdentity = ObjectIdentity
pl2Traps = _Pl2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0)
)
_Pl2TrapVals_ObjectIdentity = ObjectIdentity
pl2TrapVals = _Pl2TrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1)
)
_Pl2TrapMessage_Type = DisplayString
_Pl2TrapMessage_Object = MibScalar
pl2TrapMessage = _Pl2TrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 1),
    _Pl2TrapMessage_Type()
)
pl2TrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapMessage.setStatus("current")
_Pl2TrapOid_Type = ObjectIdentifier
_Pl2TrapOid_Object = MibScalar
pl2TrapOid = _Pl2TrapOid_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 2),
    _Pl2TrapOid_Type()
)
pl2TrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapOid.setStatus("current")
_Pl2TrapValue_Type = Unsigned32
_Pl2TrapValue_Object = MibScalar
pl2TrapValue = _Pl2TrapValue_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 3),
    _Pl2TrapValue_Type()
)
pl2TrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapValue.setStatus("current")
_Pl2TrapThreshold_Type = Unsigned32
_Pl2TrapThreshold_Object = MibScalar
pl2TrapThreshold = _Pl2TrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 4),
    _Pl2TrapThreshold_Type()
)
pl2TrapThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapThreshold.setStatus("current")
_Pl2TrapValue64_Type = Counter64
_Pl2TrapValue64_Object = MibScalar
pl2TrapValue64 = _Pl2TrapValue64_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 5),
    _Pl2TrapValue64_Type()
)
pl2TrapValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapValue64.setStatus("current")
_Pl2TrapThreshold64_Type = Counter64
_Pl2TrapThreshold64_Object = MibScalar
pl2TrapThreshold64 = _Pl2TrapThreshold64_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 6),
    _Pl2TrapThreshold64_Type()
)
pl2TrapThreshold64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapThreshold64.setStatus("current")
_Pl2ChannelTraps_ObjectIdentity = ObjectIdentity
pl2ChannelTraps = _Pl2ChannelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 2)
)
_Pl2ChannelTrapVals_ObjectIdentity = ObjectIdentity
pl2ChannelTrapVals = _Pl2ChannelTrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3)
)
_ChannelIndex_Type = Unsigned32
_ChannelIndex_Object = MibScalar
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")
_ChannelDescr_Type = DisplayString
_ChannelDescr_Object = MibScalar
channelDescr = _ChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 2),
    _ChannelDescr_Type()
)
channelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelDescr.setStatus("current")


class _ChannelPort_Type(Integer32):
    """Custom type channelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 0),
          ("internal", 1))
    )


_ChannelPort_Type.__name__ = "Integer32"
_ChannelPort_Object = MibScalar
channelPort = _ChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 3),
    _ChannelPort_Type()
)
channelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPort.setStatus("current")


class _PrevState_Type(Integer32):
    """Custom type prevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fd-10", 2),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("hd-10", 1),
          ("hd-100", 3))
    )


_PrevState_Type.__name__ = "Integer32"
_PrevState_Object = MibScalar
prevState = _PrevState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 4),
    _PrevState_Type()
)
prevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prevState.setStatus("current")


class _NewState_Type(Integer32):
    """Custom type newState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fd-10", 2),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("hd-10", 1),
          ("hd-100", 3))
    )


_NewState_Type.__name__ = "Integer32"
_NewState_Object = MibScalar
newState = _NewState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 5),
    _NewState_Type()
)
newState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newState.setStatus("current")

# Managed Objects groups


# Notification objects

pl2TrapGenericMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 1)
)
pl2TrapGenericMsg.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2TrapGenericMsg.setStatus(
        "current"
    )

pl2TrapGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 2)
)
if mibBuilder.loadTexts:
    pl2TrapGeneric.setStatus(
        "current"
    )

pl2TrapSystemStatsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 3)
)
pl2TrapSystemStatsAlert.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlert.setStatus(
        "current"
    )

pl2TrapSystemStatsAlert64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 4)
)
pl2TrapSystemStatsAlert64.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold64"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue64"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlert64.setStatus(
        "current"
    )

pl2TrapSystemStatsAlertClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 5)
)
pl2TrapSystemStatsAlertClear.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid")
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlertClear.setStatus(
        "current"
    )

pl2ChannelStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 2, 1)
)
pl2ChannelStateChanged.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "channelIndex"),
        ("PACKETLOGIC-TRAP-MIB", "channelDescr"),
        ("PACKETLOGIC-TRAP-MIB", "channelPort"),
        ("PACKETLOGIC-TRAP-MIB", "newState"),
        ("PACKETLOGIC-TRAP-MIB", "prevState"))
)
if mibBuilder.loadTexts:
    pl2ChannelStateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-TRAP-MIB",
    **{"pl2Trap": pl2Trap,
       "pl2Traps": pl2Traps,
       "pl2TrapGenericMsg": pl2TrapGenericMsg,
       "pl2TrapGeneric": pl2TrapGeneric,
       "pl2TrapSystemStatsAlert": pl2TrapSystemStatsAlert,
       "pl2TrapSystemStatsAlert64": pl2TrapSystemStatsAlert64,
       "pl2TrapSystemStatsAlertClear": pl2TrapSystemStatsAlertClear,
       "pl2TrapVals": pl2TrapVals,
       "pl2TrapMessage": pl2TrapMessage,
       "pl2TrapOid": pl2TrapOid,
       "pl2TrapValue": pl2TrapValue,
       "pl2TrapThreshold": pl2TrapThreshold,
       "pl2TrapValue64": pl2TrapValue64,
       "pl2TrapThreshold64": pl2TrapThreshold64,
       "pl2ChannelTraps": pl2ChannelTraps,
       "pl2ChannelStateChanged": pl2ChannelStateChanged,
       "pl2ChannelTrapVals": pl2ChannelTrapVals,
       "channelIndex": channelIndex,
       "channelDescr": channelDescr,
       "channelPort": channelPort,
       "prevState": prevState,
       "newState": newState}
)
