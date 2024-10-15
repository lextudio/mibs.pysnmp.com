# SNMP MIB module (TPLINK-PORTLOOPBACKDETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PORTLOOPBACKDETECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:29 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkLoopbackDetectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80)
)
tplinkLoopbackDetectionMIB.setRevisions(
        ("2009-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkLoopbackDetectionMIBObjects_ObjectIdentity = ObjectIdentity
tplinkLoopbackDetectionMIBObjects = _TplinkLoopbackDetectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1)
)


class _LoopbackDetectionEnable_Type(Integer32):
    """Custom type loopbackDetectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopbackDetectionEnable_Type.__name__ = "Integer32"
_LoopbackDetectionEnable_Object = MibScalar
loopbackDetectionEnable = _LoopbackDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 1),
    _LoopbackDetectionEnable_Type()
)
loopbackDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionEnable.setStatus("current")


class _LoopbackDetectionInterval_Type(Integer32):
    """Custom type loopbackDetectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_LoopbackDetectionInterval_Type.__name__ = "Integer32"
_LoopbackDetectionInterval_Object = MibScalar
loopbackDetectionInterval = _LoopbackDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 2),
    _LoopbackDetectionInterval_Type()
)
loopbackDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionInterval.setStatus("current")


class _LoopbackDetectionRecoveryTime_Type(Integer32):
    """Custom type loopbackDetectionRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LoopbackDetectionRecoveryTime_Type.__name__ = "Integer32"
_LoopbackDetectionRecoveryTime_Object = MibScalar
loopbackDetectionRecoveryTime = _LoopbackDetectionRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 3),
    _LoopbackDetectionRecoveryTime_Type()
)
loopbackDetectionRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionRecoveryTime.setStatus("current")
_LoopbackDetectionCtrlTable_Object = MibTable
loopbackDetectionCtrlTable = _LoopbackDetectionCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4)
)
if mibBuilder.loadTexts:
    loopbackDetectionCtrlTable.setStatus("current")
_LoopbackDetectionCtrlEntry_Object = MibTableRow
loopbackDetectionCtrlEntry = _LoopbackDetectionCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1)
)
loopbackDetectionCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    loopbackDetectionCtrlEntry.setStatus("current")


class _LoopbackDetectionPort_Type(OctetString):
    """Custom type loopbackDetectionPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoopbackDetectionPort_Type.__name__ = "OctetString"
_LoopbackDetectionPort_Object = MibTableColumn
loopbackDetectionPort = _LoopbackDetectionPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 1),
    _LoopbackDetectionPort_Type()
)
loopbackDetectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackDetectionPort.setStatus("current")


class _LoopbackDetectionState_Type(Integer32):
    """Custom type loopbackDetectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopbackDetectionState_Type.__name__ = "Integer32"
_LoopbackDetectionState_Object = MibTableColumn
loopbackDetectionState = _LoopbackDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 2),
    _LoopbackDetectionState_Type()
)
loopbackDetectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionState.setStatus("current")


class _LoopbackDetectionProcessMode_Type(Integer32):
    """Custom type loopbackDetectionProcessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alert", 0),
          ("portbased", 1))
    )


_LoopbackDetectionProcessMode_Type.__name__ = "Integer32"
_LoopbackDetectionProcessMode_Object = MibTableColumn
loopbackDetectionProcessMode = _LoopbackDetectionProcessMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 3),
    _LoopbackDetectionProcessMode_Type()
)
loopbackDetectionProcessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionProcessMode.setStatus("current")


class _LoopbackDetectionRecoverMode_Type(Integer32):
    """Custom type loopbackDetectionRecoverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_LoopbackDetectionRecoverMode_Type.__name__ = "Integer32"
_LoopbackDetectionRecoverMode_Object = MibTableColumn
loopbackDetectionRecoverMode = _LoopbackDetectionRecoverMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 4),
    _LoopbackDetectionRecoverMode_Type()
)
loopbackDetectionRecoverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionRecoverMode.setStatus("current")


class _LoopbackDetectionLoopState_Type(OctetString):
    """Custom type loopbackDetectionLoopState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoopbackDetectionLoopState_Type.__name__ = "OctetString"
_LoopbackDetectionLoopState_Object = MibTableColumn
loopbackDetectionLoopState = _LoopbackDetectionLoopState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 5),
    _LoopbackDetectionLoopState_Type()
)
loopbackDetectionLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackDetectionLoopState.setStatus("current")


class _LoopbackDetectionBlockState_Type(OctetString):
    """Custom type loopbackDetectionBlockState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoopbackDetectionBlockState_Type.__name__ = "OctetString"
_LoopbackDetectionBlockState_Object = MibTableColumn
loopbackDetectionBlockState = _LoopbackDetectionBlockState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 6),
    _LoopbackDetectionBlockState_Type()
)
loopbackDetectionBlockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackDetectionBlockState.setStatus("current")


class _LoopbackDetectionLagState_Type(OctetString):
    """Custom type loopbackDetectionLagState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoopbackDetectionLagState_Type.__name__ = "OctetString"
_LoopbackDetectionLagState_Object = MibTableColumn
loopbackDetectionLagState = _LoopbackDetectionLagState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 7),
    _LoopbackDetectionLagState_Type()
)
loopbackDetectionLagState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackDetectionLagState.setStatus("current")
_LoopbackDetectionRecoverPort_Type = Integer32
_LoopbackDetectionRecoverPort_Object = MibTableColumn
loopbackDetectionRecoverPort = _LoopbackDetectionRecoverPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 8),
    _LoopbackDetectionRecoverPort_Type()
)
loopbackDetectionRecoverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDetectionRecoverPort.setStatus("current")
_TplinkLoopbackDetectionNotifications_ObjectIdentity = ObjectIdentity
tplinkLoopbackDetectionNotifications = _TplinkLoopbackDetectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 2)
)

# Managed Objects groups


# Notification objects

loopbackStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 80, 2, 1)
)
if mibBuilder.loadTexts:
    loopbackStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTLOOPBACKDETECTION-MIB",
    **{"tplinkLoopbackDetectionMIB": tplinkLoopbackDetectionMIB,
       "tplinkLoopbackDetectionMIBObjects": tplinkLoopbackDetectionMIBObjects,
       "loopbackDetectionEnable": loopbackDetectionEnable,
       "loopbackDetectionInterval": loopbackDetectionInterval,
       "loopbackDetectionRecoveryTime": loopbackDetectionRecoveryTime,
       "loopbackDetectionCtrlTable": loopbackDetectionCtrlTable,
       "loopbackDetectionCtrlEntry": loopbackDetectionCtrlEntry,
       "loopbackDetectionPort": loopbackDetectionPort,
       "loopbackDetectionState": loopbackDetectionState,
       "loopbackDetectionProcessMode": loopbackDetectionProcessMode,
       "loopbackDetectionRecoverMode": loopbackDetectionRecoverMode,
       "loopbackDetectionLoopState": loopbackDetectionLoopState,
       "loopbackDetectionBlockState": loopbackDetectionBlockState,
       "loopbackDetectionLagState": loopbackDetectionLagState,
       "loopbackDetectionRecoverPort": loopbackDetectionRecoverPort,
       "tplinkLoopbackDetectionNotifications": tplinkLoopbackDetectionNotifications,
       "loopbackStatusChange": loopbackStatusChange}
)
