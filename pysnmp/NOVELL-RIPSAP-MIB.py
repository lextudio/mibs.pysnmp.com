# SNMP MIB module (NOVELL-RIPSAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOVELL-RIPSAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:03 2024
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

(mibDoc,) = mibBuilder.importSymbols(
    "NOVELL-IPX-MIB",
    "mibDoc")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ripsap_ObjectIdentity = ObjectIdentity
ripsap = _Ripsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 20)
)
_RipsapSystem_ObjectIdentity = ObjectIdentity
ripsapSystem = _RipsapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1)
)
_RipSysTable_Object = MibTable
ripSysTable = _RipSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 1)
)
if mibBuilder.loadTexts:
    ripSysTable.setStatus("mandatory")
_RipSysEntry_Object = MibTableRow
ripSysEntry = _RipSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 1, 1)
)
ripSysEntry.setIndexNames(
    (0, "NOVELL-RIPSAP-MIB", "ripSysInstance"),
)
if mibBuilder.loadTexts:
    ripSysEntry.setStatus("mandatory")
_RipSysInstance_Type = Integer32
_RipSysInstance_Object = MibTableColumn
ripSysInstance = _RipSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 1, 1, 1),
    _RipSysInstance_Type()
)
ripSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysInstance.setStatus("mandatory")


class _RipSysState_Type(Integer32):
    """Custom type ripSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RipSysState_Type.__name__ = "Integer32"
_RipSysState_Object = MibTableColumn
ripSysState = _RipSysState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 1, 1, 2),
    _RipSysState_Type()
)
ripSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysState.setStatus("mandatory")
_RipSysIncorrectPackets_Type = Counter32
_RipSysIncorrectPackets_Object = MibTableColumn
ripSysIncorrectPackets = _RipSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 1, 1, 3),
    _RipSysIncorrectPackets_Type()
)
ripSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripSysIncorrectPackets.setStatus("mandatory")
_SapSysTable_Object = MibTable
sapSysTable = _SapSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    sapSysTable.setStatus("mandatory")
_SapSysEntry_Object = MibTableRow
sapSysEntry = _SapSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 2, 1)
)
sapSysEntry.setIndexNames(
    (0, "NOVELL-RIPSAP-MIB", "sapSysInstance"),
)
if mibBuilder.loadTexts:
    sapSysEntry.setStatus("mandatory")
_SapSysInstance_Type = Integer32
_SapSysInstance_Object = MibTableColumn
sapSysInstance = _SapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 2, 1, 1),
    _SapSysInstance_Type()
)
sapSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapSysInstance.setStatus("mandatory")


class _SapSysState_Type(Integer32):
    """Custom type sapSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SapSysState_Type.__name__ = "Integer32"
_SapSysState_Object = MibTableColumn
sapSysState = _SapSysState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 2, 1, 2),
    _SapSysState_Type()
)
sapSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapSysState.setStatus("mandatory")
_SapSysIncorrectPackets_Type = Counter32
_SapSysIncorrectPackets_Object = MibTableColumn
sapSysIncorrectPackets = _SapSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 1, 2, 1, 3),
    _SapSysIncorrectPackets_Type()
)
sapSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapSysIncorrectPackets.setStatus("mandatory")
_RipsapCircuit_ObjectIdentity = ObjectIdentity
ripsapCircuit = _RipsapCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2)
)
_RipCircTable_Object = MibTable
ripCircTable = _RipCircTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    ripCircTable.setStatus("mandatory")
_RipCircEntry_Object = MibTableRow
ripCircEntry = _RipCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1)
)
ripCircEntry.setIndexNames(
    (0, "NOVELL-RIPSAP-MIB", "ripCircSysInstance"),
    (0, "NOVELL-RIPSAP-MIB", "ripCircIndex"),
)
if mibBuilder.loadTexts:
    ripCircEntry.setStatus("mandatory")
_RipCircSysInstance_Type = Integer32
_RipCircSysInstance_Object = MibTableColumn
ripCircSysInstance = _RipCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 1),
    _RipCircSysInstance_Type()
)
ripCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircSysInstance.setStatus("mandatory")
_RipCircIndex_Type = Integer32
_RipCircIndex_Object = MibTableColumn
ripCircIndex = _RipCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 2),
    _RipCircIndex_Type()
)
ripCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircIndex.setStatus("mandatory")


class _RipCircState_Type(Integer32):
    """Custom type ripCircState based on Integer32"""
    defaultValue = 4

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
        *(("auto-off", 4),
          ("auto-on", 3),
          ("off", 1),
          ("on", 2))
    )


_RipCircState_Type.__name__ = "Integer32"
_RipCircState_Object = MibTableColumn
ripCircState = _RipCircState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 3),
    _RipCircState_Type()
)
ripCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircState.setStatus("mandatory")
_RipCircPace_Type = Integer32
_RipCircPace_Object = MibTableColumn
ripCircPace = _RipCircPace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 4),
    _RipCircPace_Type()
)
ripCircPace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircPace.setStatus("mandatory")


class _RipCircUpdate_Type(Integer32):
    """Custom type ripCircUpdate based on Integer32"""
    defaultValue = 60


_RipCircUpdate_Object = MibTableColumn
ripCircUpdate = _RipCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 5),
    _RipCircUpdate_Type()
)
ripCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircUpdate.setStatus("mandatory")


class _RipCircAgeMultiplier_Type(Integer32):
    """Custom type ripCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_RipCircAgeMultiplier_Object = MibTableColumn
ripCircAgeMultiplier = _RipCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 6),
    _RipCircAgeMultiplier_Type()
)
ripCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircAgeMultiplier.setStatus("mandatory")
_RipCircPacketSize_Type = Integer32
_RipCircPacketSize_Object = MibTableColumn
ripCircPacketSize = _RipCircPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 7),
    _RipCircPacketSize_Type()
)
ripCircPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircPacketSize.setStatus("mandatory")
_RipCircOutPackets_Type = Counter32
_RipCircOutPackets_Object = MibTableColumn
ripCircOutPackets = _RipCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 8),
    _RipCircOutPackets_Type()
)
ripCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircOutPackets.setStatus("mandatory")
_RipCircInPackets_Type = Counter32
_RipCircInPackets_Object = MibTableColumn
ripCircInPackets = _RipCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 1, 1, 9),
    _RipCircInPackets_Type()
)
ripCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircInPackets.setStatus("mandatory")
_SapCircTable_Object = MibTable
sapCircTable = _SapCircTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    sapCircTable.setStatus("mandatory")
_SapCircEntry_Object = MibTableRow
sapCircEntry = _SapCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1)
)
sapCircEntry.setIndexNames(
    (0, "NOVELL-RIPSAP-MIB", "sapCircSysInstance"),
    (0, "NOVELL-RIPSAP-MIB", "sapCircIndex"),
)
if mibBuilder.loadTexts:
    sapCircEntry.setStatus("mandatory")
_SapCircSysInstance_Type = Integer32
_SapCircSysInstance_Object = MibTableColumn
sapCircSysInstance = _SapCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 1),
    _SapCircSysInstance_Type()
)
sapCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircSysInstance.setStatus("mandatory")
_SapCircIndex_Type = Integer32
_SapCircIndex_Object = MibTableColumn
sapCircIndex = _SapCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 2),
    _SapCircIndex_Type()
)
sapCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircIndex.setStatus("mandatory")


class _SapCircState_Type(Integer32):
    """Custom type sapCircState based on Integer32"""
    defaultValue = 4

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
        *(("auto-off", 4),
          ("auto-on", 3),
          ("off", 1),
          ("on", 2))
    )


_SapCircState_Type.__name__ = "Integer32"
_SapCircState_Object = MibTableColumn
sapCircState = _SapCircState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 3),
    _SapCircState_Type()
)
sapCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircState.setStatus("mandatory")
_SapCircPace_Type = Integer32
_SapCircPace_Object = MibTableColumn
sapCircPace = _SapCircPace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 4),
    _SapCircPace_Type()
)
sapCircPace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircPace.setStatus("mandatory")


class _SapCircUpdate_Type(Integer32):
    """Custom type sapCircUpdate based on Integer32"""
    defaultValue = 60


_SapCircUpdate_Object = MibTableColumn
sapCircUpdate = _SapCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 5),
    _SapCircUpdate_Type()
)
sapCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircUpdate.setStatus("mandatory")


class _SapCircAgeMultiplier_Type(Integer32):
    """Custom type sapCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_SapCircAgeMultiplier_Object = MibTableColumn
sapCircAgeMultiplier = _SapCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 6),
    _SapCircAgeMultiplier_Type()
)
sapCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircAgeMultiplier.setStatus("mandatory")
_SapCircPacketSize_Type = Integer32
_SapCircPacketSize_Object = MibTableColumn
sapCircPacketSize = _SapCircPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 7),
    _SapCircPacketSize_Type()
)
sapCircPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircPacketSize.setStatus("mandatory")


class _SapCircGetNearestServerReply_Type(Integer32):
    """Custom type sapCircGetNearestServerReply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SapCircGetNearestServerReply_Type.__name__ = "Integer32"
_SapCircGetNearestServerReply_Object = MibTableColumn
sapCircGetNearestServerReply = _SapCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 8),
    _SapCircGetNearestServerReply_Type()
)
sapCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircGetNearestServerReply.setStatus("mandatory")
_SapCircOutPackets_Type = Counter32
_SapCircOutPackets_Object = MibTableColumn
sapCircOutPackets = _SapCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 9),
    _SapCircOutPackets_Type()
)
sapCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircOutPackets.setStatus("mandatory")
_SapCircInPackets_Type = Counter32
_SapCircInPackets_Object = MibTableColumn
sapCircInPackets = _SapCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 20, 2, 2, 1, 10),
    _SapCircInPackets_Type()
)
sapCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircInPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOVELL-RIPSAP-MIB",
    **{"ripsap": ripsap,
       "ripsapSystem": ripsapSystem,
       "ripSysTable": ripSysTable,
       "ripSysEntry": ripSysEntry,
       "ripSysInstance": ripSysInstance,
       "ripSysState": ripSysState,
       "ripSysIncorrectPackets": ripSysIncorrectPackets,
       "sapSysTable": sapSysTable,
       "sapSysEntry": sapSysEntry,
       "sapSysInstance": sapSysInstance,
       "sapSysState": sapSysState,
       "sapSysIncorrectPackets": sapSysIncorrectPackets,
       "ripsapCircuit": ripsapCircuit,
       "ripCircTable": ripCircTable,
       "ripCircEntry": ripCircEntry,
       "ripCircSysInstance": ripCircSysInstance,
       "ripCircIndex": ripCircIndex,
       "ripCircState": ripCircState,
       "ripCircPace": ripCircPace,
       "ripCircUpdate": ripCircUpdate,
       "ripCircAgeMultiplier": ripCircAgeMultiplier,
       "ripCircPacketSize": ripCircPacketSize,
       "ripCircOutPackets": ripCircOutPackets,
       "ripCircInPackets": ripCircInPackets,
       "sapCircTable": sapCircTable,
       "sapCircEntry": sapCircEntry,
       "sapCircSysInstance": sapCircSysInstance,
       "sapCircIndex": sapCircIndex,
       "sapCircState": sapCircState,
       "sapCircPace": sapCircPace,
       "sapCircUpdate": sapCircUpdate,
       "sapCircAgeMultiplier": sapCircAgeMultiplier,
       "sapCircPacketSize": sapCircPacketSize,
       "sapCircGetNearestServerReply": sapCircGetNearestServerReply,
       "sapCircOutPackets": sapCircOutPackets,
       "sapCircInPackets": sapCircInPackets}
)
