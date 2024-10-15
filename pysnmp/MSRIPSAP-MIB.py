# SNMP MIB module (MSRIPSAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSRIPSAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:59 2024
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

_Ripsap_ObjectIdentity = ObjectIdentity
ripsap = _Ripsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 9)
)
_RipsapBase_ObjectIdentity = ObjectIdentity
ripsapBase = _RipsapBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 1)
)


class _RipsapBaseRipOperState_Type(Integer32):
    """Custom type ripsapBaseRipOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_RipsapBaseRipOperState_Type.__name__ = "Integer32"
_RipsapBaseRipOperState_Object = MibScalar
ripsapBaseRipOperState = _RipsapBaseRipOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 1, 1),
    _RipsapBaseRipOperState_Type()
)
ripsapBaseRipOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapBaseRipOperState.setStatus("mandatory")


class _RipsapBaseSapOperState_Type(Integer32):
    """Custom type ripsapBaseSapOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_RipsapBaseSapOperState_Type.__name__ = "Integer32"
_RipsapBaseSapOperState_Object = MibScalar
ripsapBaseSapOperState = _RipsapBaseSapOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 1, 2),
    _RipsapBaseSapOperState_Type()
)
ripsapBaseSapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapBaseSapOperState.setStatus("mandatory")
_RipsapInterface_ObjectIdentity = ObjectIdentity
ripsapInterface = _RipsapInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2)
)
_RipIfTable_Object = MibTable
ripIfTable = _RipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    ripIfTable.setStatus("mandatory")
_RipIfEntry_Object = MibTableRow
ripIfEntry = _RipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1)
)
ripIfEntry.setIndexNames(
    (0, "MSRIPSAP-MIB", "ripIfIndex"),
)
if mibBuilder.loadTexts:
    ripIfEntry.setStatus("mandatory")
_RipIfIndex_Type = Integer32
_RipIfIndex_Object = MibTableColumn
ripIfIndex = _RipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 1),
    _RipIfIndex_Type()
)
ripIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfIndex.setStatus("mandatory")


class _RipIfAdminState_Type(Integer32):
    """Custom type ripIfAdminState based on Integer32"""
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


_RipIfAdminState_Type.__name__ = "Integer32"
_RipIfAdminState_Object = MibTableColumn
ripIfAdminState = _RipIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 2),
    _RipIfAdminState_Type()
)
ripIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAdminState.setStatus("mandatory")


class _RipIfOperState_Type(Integer32):
    """Custom type ripIfOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("sleeping", 3),
          ("up", 2))
    )


_RipIfOperState_Type.__name__ = "Integer32"
_RipIfOperState_Object = MibTableColumn
ripIfOperState = _RipIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 3),
    _RipIfOperState_Type()
)
ripIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfOperState.setStatus("mandatory")


class _RipIfUpdateMode_Type(Integer32):
    """Custom type ripIfUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autostatic", 3),
          ("none", 2),
          ("standard", 1))
    )


_RipIfUpdateMode_Type.__name__ = "Integer32"
_RipIfUpdateMode_Object = MibTableColumn
ripIfUpdateMode = _RipIfUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 4),
    _RipIfUpdateMode_Type()
)
ripIfUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfUpdateMode.setStatus("mandatory")
_RipIfUpdateInterval_Type = Integer32
_RipIfUpdateInterval_Object = MibTableColumn
ripIfUpdateInterval = _RipIfUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 5),
    _RipIfUpdateInterval_Type()
)
ripIfUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfUpdateInterval.setStatus("mandatory")
_RipIfAgeMultiplier_Type = Integer32
_RipIfAgeMultiplier_Object = MibTableColumn
ripIfAgeMultiplier = _RipIfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 6),
    _RipIfAgeMultiplier_Type()
)
ripIfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAgeMultiplier.setStatus("mandatory")


class _RipIfSupply_Type(Integer32):
    """Custom type ripIfSupply based on Integer32"""
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


_RipIfSupply_Type.__name__ = "Integer32"
_RipIfSupply_Object = MibTableColumn
ripIfSupply = _RipIfSupply_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 7),
    _RipIfSupply_Type()
)
ripIfSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSupply.setStatus("mandatory")


class _RipIfListen_Type(Integer32):
    """Custom type ripIfListen based on Integer32"""
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


_RipIfListen_Type.__name__ = "Integer32"
_RipIfListen_Object = MibTableColumn
ripIfListen = _RipIfListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 8),
    _RipIfListen_Type()
)
ripIfListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfListen.setStatus("mandatory")
_RipIfOutPackets_Type = Counter32
_RipIfOutPackets_Object = MibTableColumn
ripIfOutPackets = _RipIfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 9),
    _RipIfOutPackets_Type()
)
ripIfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfOutPackets.setStatus("mandatory")
_RipIfInPackets_Type = Counter32
_RipIfInPackets_Object = MibTableColumn
ripIfInPackets = _RipIfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 1, 1, 10),
    _RipIfInPackets_Type()
)
ripIfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInPackets.setStatus("mandatory")
_SapIfTable_Object = MibTable
sapIfTable = _SapIfTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    sapIfTable.setStatus("mandatory")
_SapIfEntry_Object = MibTableRow
sapIfEntry = _SapIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1)
)
sapIfEntry.setIndexNames(
    (0, "MSRIPSAP-MIB", "sapIfIndex"),
)
if mibBuilder.loadTexts:
    sapIfEntry.setStatus("mandatory")
_SapIfIndex_Type = Integer32
_SapIfIndex_Object = MibTableColumn
sapIfIndex = _SapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 1),
    _SapIfIndex_Type()
)
sapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIfIndex.setStatus("mandatory")


class _SapIfAdminState_Type(Integer32):
    """Custom type sapIfAdminState based on Integer32"""
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


_SapIfAdminState_Type.__name__ = "Integer32"
_SapIfAdminState_Object = MibTableColumn
sapIfAdminState = _SapIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 2),
    _SapIfAdminState_Type()
)
sapIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfAdminState.setStatus("mandatory")


class _SapIfOperState_Type(Integer32):
    """Custom type sapIfOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("sleeping", 3),
          ("up", 2))
    )


_SapIfOperState_Type.__name__ = "Integer32"
_SapIfOperState_Object = MibTableColumn
sapIfOperState = _SapIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 3),
    _SapIfOperState_Type()
)
sapIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIfOperState.setStatus("mandatory")


class _SapIfUpdateMode_Type(Integer32):
    """Custom type sapIfUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autostatic", 3),
          ("none", 2),
          ("standard", 1))
    )


_SapIfUpdateMode_Type.__name__ = "Integer32"
_SapIfUpdateMode_Object = MibTableColumn
sapIfUpdateMode = _SapIfUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 4),
    _SapIfUpdateMode_Type()
)
sapIfUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfUpdateMode.setStatus("mandatory")
_SapIfUpdateInterval_Type = Integer32
_SapIfUpdateInterval_Object = MibTableColumn
sapIfUpdateInterval = _SapIfUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 5),
    _SapIfUpdateInterval_Type()
)
sapIfUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfUpdateInterval.setStatus("mandatory")
_SapIfAgeMultiplier_Type = Integer32
_SapIfAgeMultiplier_Object = MibTableColumn
sapIfAgeMultiplier = _SapIfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 6),
    _SapIfAgeMultiplier_Type()
)
sapIfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfAgeMultiplier.setStatus("mandatory")


class _SapIfSupply_Type(Integer32):
    """Custom type sapIfSupply based on Integer32"""
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


_SapIfSupply_Type.__name__ = "Integer32"
_SapIfSupply_Object = MibTableColumn
sapIfSupply = _SapIfSupply_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 7),
    _SapIfSupply_Type()
)
sapIfSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfSupply.setStatus("mandatory")


class _SapIfListen_Type(Integer32):
    """Custom type sapIfListen based on Integer32"""
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


_SapIfListen_Type.__name__ = "Integer32"
_SapIfListen_Object = MibTableColumn
sapIfListen = _SapIfListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 8),
    _SapIfListen_Type()
)
sapIfListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfListen.setStatus("mandatory")


class _SapIfGetNearestServerReply_Type(Integer32):
    """Custom type sapIfGetNearestServerReply based on Integer32"""
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


_SapIfGetNearestServerReply_Type.__name__ = "Integer32"
_SapIfGetNearestServerReply_Object = MibTableColumn
sapIfGetNearestServerReply = _SapIfGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 9),
    _SapIfGetNearestServerReply_Type()
)
sapIfGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIfGetNearestServerReply.setStatus("mandatory")
_SapIfOutPackets_Type = Counter32
_SapIfOutPackets_Object = MibTableColumn
sapIfOutPackets = _SapIfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 10),
    _SapIfOutPackets_Type()
)
sapIfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIfOutPackets.setStatus("mandatory")
_SapIfInPackets_Type = Counter32
_SapIfInPackets_Object = MibTableColumn
sapIfInPackets = _SapIfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 9, 2, 2, 1, 11),
    _SapIfInPackets_Type()
)
sapIfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIfInPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSRIPSAP-MIB",
    **{"ripsap": ripsap,
       "ripsapBase": ripsapBase,
       "ripsapBaseRipOperState": ripsapBaseRipOperState,
       "ripsapBaseSapOperState": ripsapBaseSapOperState,
       "ripsapInterface": ripsapInterface,
       "ripIfTable": ripIfTable,
       "ripIfEntry": ripIfEntry,
       "ripIfIndex": ripIfIndex,
       "ripIfAdminState": ripIfAdminState,
       "ripIfOperState": ripIfOperState,
       "ripIfUpdateMode": ripIfUpdateMode,
       "ripIfUpdateInterval": ripIfUpdateInterval,
       "ripIfAgeMultiplier": ripIfAgeMultiplier,
       "ripIfSupply": ripIfSupply,
       "ripIfListen": ripIfListen,
       "ripIfOutPackets": ripIfOutPackets,
       "ripIfInPackets": ripIfInPackets,
       "sapIfTable": sapIfTable,
       "sapIfEntry": sapIfEntry,
       "sapIfIndex": sapIfIndex,
       "sapIfAdminState": sapIfAdminState,
       "sapIfOperState": sapIfOperState,
       "sapIfUpdateMode": sapIfUpdateMode,
       "sapIfUpdateInterval": sapIfUpdateInterval,
       "sapIfAgeMultiplier": sapIfAgeMultiplier,
       "sapIfSupply": sapIfSupply,
       "sapIfListen": sapIfListen,
       "sapIfGetNearestServerReply": sapIfGetNearestServerReply,
       "sapIfOutPackets": sapIfOutPackets,
       "sapIfInPackets": sapIfInPackets}
)
