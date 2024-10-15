# SNMP MIB module (Wellfleet-MODCTL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MODCTL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:40 2024
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

(wfModCtlGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfModCtlGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfModCtlBase_ObjectIdentity = ObjectIdentity
wfModCtlBase = _WfModCtlBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1)
)


class _WfModCtlPrimarySlot_Type(Integer32):
    """Custom type wfModCtlPrimarySlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_WfModCtlPrimarySlot_Type.__name__ = "Integer32"
_WfModCtlPrimarySlot_Object = MibScalar
wfModCtlPrimarySlot = _WfModCtlPrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 1),
    _WfModCtlPrimarySlot_Type()
)
wfModCtlPrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModCtlPrimarySlot.setStatus("mandatory")


class _WfModCtlState_Type(Integer32):
    """Custom type wfModCtlState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("config", 4),
          ("down", 2),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfModCtlState_Type.__name__ = "Integer32"
_WfModCtlState_Object = MibScalar
wfModCtlState = _WfModCtlState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 2),
    _WfModCtlState_Type()
)
wfModCtlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModCtlState.setStatus("mandatory")


class _WfModCtlActiveMask_Type(Gauge32):
    """Custom type wfModCtlActiveMask based on Gauge32"""
    defaultValue = 0


_WfModCtlActiveMask_Object = MibScalar
wfModCtlActiveMask = _WfModCtlActiveMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 3),
    _WfModCtlActiveMask_Type()
)
wfModCtlActiveMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModCtlActiveMask.setStatus("mandatory")


class _WfModCtlCfgSlotDisableMask_Type(Gauge32):
    """Custom type wfModCtlCfgSlotDisableMask based on Gauge32"""
    defaultValue = 0


_WfModCtlCfgSlotDisableMask_Object = MibScalar
wfModCtlCfgSlotDisableMask = _WfModCtlCfgSlotDisableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 4),
    _WfModCtlCfgSlotDisableMask_Type()
)
wfModCtlCfgSlotDisableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgSlotDisableMask.setStatus("mandatory")


class _WfModCtlCfgHeartbeatPeriod_Type(Integer32):
    """Custom type wfModCtlCfgHeartbeatPeriod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfModCtlCfgHeartbeatPeriod_Type.__name__ = "Integer32"
_WfModCtlCfgHeartbeatPeriod_Object = MibScalar
wfModCtlCfgHeartbeatPeriod = _WfModCtlCfgHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 5),
    _WfModCtlCfgHeartbeatPeriod_Type()
)
wfModCtlCfgHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgHeartbeatPeriod.setStatus("mandatory")


class _WfModCtlCfgHeartbeatDisableMask_Type(Gauge32):
    """Custom type wfModCtlCfgHeartbeatDisableMask based on Gauge32"""
    defaultValue = 0


_WfModCtlCfgHeartbeatDisableMask_Object = MibScalar
wfModCtlCfgHeartbeatDisableMask = _WfModCtlCfgHeartbeatDisableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 6),
    _WfModCtlCfgHeartbeatDisableMask_Type()
)
wfModCtlCfgHeartbeatDisableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgHeartbeatDisableMask.setStatus("mandatory")


class _WfModCtlCfgBoflFailPeriod_Type(Integer32):
    """Custom type wfModCtlCfgBoflFailPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfModCtlCfgBoflFailPeriod_Type.__name__ = "Integer32"
_WfModCtlCfgBoflFailPeriod_Object = MibScalar
wfModCtlCfgBoflFailPeriod = _WfModCtlCfgBoflFailPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 7),
    _WfModCtlCfgBoflFailPeriod_Type()
)
wfModCtlCfgBoflFailPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgBoflFailPeriod.setStatus("mandatory")


class _WfModCtlCfgBoflDisableMask_Type(Gauge32):
    """Custom type wfModCtlCfgBoflDisableMask based on Gauge32"""
    defaultValue = 0


_WfModCtlCfgBoflDisableMask_Object = MibScalar
wfModCtlCfgBoflDisableMask = _WfModCtlCfgBoflDisableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 8),
    _WfModCtlCfgBoflDisableMask_Type()
)
wfModCtlCfgBoflDisableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgBoflDisableMask.setStatus("mandatory")


class _WfModCtlCfgRspImageType_Type(Integer32):
    """Custom type wfModCtlCfgRspImageType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("trace", 2))
    )


_WfModCtlCfgRspImageType_Type.__name__ = "Integer32"
_WfModCtlCfgRspImageType_Object = MibScalar
wfModCtlCfgRspImageType = _WfModCtlCfgRspImageType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 9),
    _WfModCtlCfgRspImageType_Type()
)
wfModCtlCfgRspImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlCfgRspImageType.setStatus("mandatory")


class _WfModCtlDbgMsgLevel_Type(Integer32):
    """Custom type wfModCtlDbgMsgLevel based on Integer32"""
    defaultValue = 2031616

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              131072,
              262144,
              524288,
              1048576,
              2031616)
        )
    )
    namedValues = NamedValues(
        *(("all", 2031616),
          ("debug", 65536),
          ("fault", 524288),
          ("info", 131072),
          ("trace", 1048576),
          ("warning", 262144))
    )


_WfModCtlDbgMsgLevel_Type.__name__ = "Integer32"
_WfModCtlDbgMsgLevel_Object = MibScalar
wfModCtlDbgMsgLevel = _WfModCtlDbgMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 10),
    _WfModCtlDbgMsgLevel_Type()
)
wfModCtlDbgMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlDbgMsgLevel.setStatus("mandatory")


class _WfModCtlScdLogMask_Type(Integer32):
    """Custom type wfModCtlScdLogMask based on Integer32"""
    defaultValue = 0


_WfModCtlScdLogMask_Object = MibScalar
wfModCtlScdLogMask = _WfModCtlScdLogMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 11),
    _WfModCtlScdLogMask_Type()
)
wfModCtlScdLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlScdLogMask.setStatus("mandatory")


class _WfModCtlScdDbgMask_Type(Integer32):
    """Custom type wfModCtlScdDbgMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfModCtlScdDbgMask_Type.__name__ = "Integer32"
_WfModCtlScdDbgMask_Object = MibScalar
wfModCtlScdDbgMask = _WfModCtlScdDbgMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1, 1, 12),
    _WfModCtlScdDbgMask_Type()
)
wfModCtlScdDbgMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModCtlScdDbgMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MODCTL-MIB",
    **{"wfModCtlBase": wfModCtlBase,
       "wfModCtlPrimarySlot": wfModCtlPrimarySlot,
       "wfModCtlState": wfModCtlState,
       "wfModCtlActiveMask": wfModCtlActiveMask,
       "wfModCtlCfgSlotDisableMask": wfModCtlCfgSlotDisableMask,
       "wfModCtlCfgHeartbeatPeriod": wfModCtlCfgHeartbeatPeriod,
       "wfModCtlCfgHeartbeatDisableMask": wfModCtlCfgHeartbeatDisableMask,
       "wfModCtlCfgBoflFailPeriod": wfModCtlCfgBoflFailPeriod,
       "wfModCtlCfgBoflDisableMask": wfModCtlCfgBoflDisableMask,
       "wfModCtlCfgRspImageType": wfModCtlCfgRspImageType,
       "wfModCtlDbgMsgLevel": wfModCtlDbgMsgLevel,
       "wfModCtlScdLogMask": wfModCtlScdLogMask,
       "wfModCtlScdDbgMask": wfModCtlScdDbgMask}
)
