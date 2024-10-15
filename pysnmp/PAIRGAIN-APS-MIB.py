# SNMP MIB module (PAIRGAIN-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:15 2024
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

(pgApsMIB,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgApsMIB")

(TimeSeconds,) = mibBuilder.importSymbols(
    "PAIRGAIN-DSLAM-CHASSIS-MIB",
    "TimeSeconds")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pgAps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1)
)


# Types definitions



class Byte(Integer32):
    """Custom type Byte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



class PgApsK1K2(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PgApsMIBNotifications_ObjectIdentity = ObjectIdentity
pgApsMIBNotifications = _PgApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 0)
)
_PgApsMibObjects_ObjectIdentity = ObjectIdentity
pgApsMibObjects = _PgApsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1)
)
_PgApsConfigTable_Object = MibTable
pgApsConfigTable = _PgApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pgApsConfigTable.setStatus("current")
_PgApsConfigEntry_Object = MibTableRow
pgApsConfigEntry = _PgApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1)
)
pgApsConfigEntry.setIndexNames(
    (0, "PAIRGAIN-APS-MIB", "pgApsIndex"),
)
if mibBuilder.loadTexts:
    pgApsConfigEntry.setStatus("current")


class _PgApsIndex_Type(Integer32):
    """Custom type pgApsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgApsIndex_Type.__name__ = "Integer32"
_PgApsIndex_Object = MibTableColumn
pgApsIndex = _PgApsIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 1),
    _PgApsIndex_Type()
)
pgApsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsIndex.setStatus("current")


class _PgApsEnable_Type(Integer32):
    """Custom type pgApsEnable based on Integer32"""
    defaultValue = 2

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


_PgApsEnable_Type.__name__ = "Integer32"
_PgApsEnable_Object = MibTableColumn
pgApsEnable = _PgApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 2),
    _PgApsEnable_Type()
)
pgApsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgApsEnable.setStatus("current")


class _PgApsTrapEnable_Type(Integer32):
    """Custom type pgApsTrapEnable based on Integer32"""
    defaultValue = 2

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


_PgApsTrapEnable_Type.__name__ = "Integer32"
_PgApsTrapEnable_Object = MibTableColumn
pgApsTrapEnable = _PgApsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 3),
    _PgApsTrapEnable_Type()
)
pgApsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgApsTrapEnable.setStatus("current")
_PgApsWorkChanIfIndex_Type = Integer32
_PgApsWorkChanIfIndex_Object = MibTableColumn
pgApsWorkChanIfIndex = _PgApsWorkChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 4),
    _PgApsWorkChanIfIndex_Type()
)
pgApsWorkChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkChanIfIndex.setStatus("current")
_PgApsProtChanIfIndex_Type = Integer32
_PgApsProtChanIfIndex_Object = MibTableColumn
pgApsProtChanIfIndex = _PgApsProtChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 5),
    _PgApsProtChanIfIndex_Type()
)
pgApsProtChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtChanIfIndex.setStatus("current")


class _PgApsConfigMode_Type(Integer32):
    """Custom type pgApsConfigMode based on Integer32"""
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
        *(("nonRevertive", 1),
          ("nonRevertiveAuto", 2),
          ("revertive", 3))
    )


_PgApsConfigMode_Type.__name__ = "Integer32"
_PgApsConfigMode_Object = MibTableColumn
pgApsConfigMode = _PgApsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 6),
    _PgApsConfigMode_Type()
)
pgApsConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgApsConfigMode.setStatus("current")


class _PgApsConfigSigDegradeThresh_Type(Integer32):
    """Custom type pgApsConfigSigDegradeThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_PgApsConfigSigDegradeThresh_Type.__name__ = "Integer32"
_PgApsConfigSigDegradeThresh_Object = MibTableColumn
pgApsConfigSigDegradeThresh = _PgApsConfigSigDegradeThresh_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 7),
    _PgApsConfigSigDegradeThresh_Type()
)
pgApsConfigSigDegradeThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsConfigSigDegradeThresh.setStatus("current")


class _PgApsConfigWaitToRevert_Type(Integer32):
    """Custom type pgApsConfigWaitToRevert based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 720),
    )


_PgApsConfigWaitToRevert_Type.__name__ = "Integer32"
_PgApsConfigWaitToRevert_Object = MibTableColumn
pgApsConfigWaitToRevert = _PgApsConfigWaitToRevert_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 8),
    _PgApsConfigWaitToRevert_Type()
)
pgApsConfigWaitToRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgApsConfigWaitToRevert.setStatus("current")
_PgApsSwitchCommand_Type = Integer32
_PgApsSwitchCommand_Object = MibTableColumn
pgApsSwitchCommand = _PgApsSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 9),
    _PgApsSwitchCommand_Type()
)
pgApsSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgApsSwitchCommand.setStatus("current")
_PgApsStatusTable_Object = MibTable
pgApsStatusTable = _PgApsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pgApsStatusTable.setStatus("current")
_PgApsStatusEntry_Object = MibTableRow
pgApsStatusEntry = _PgApsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1)
)
pgApsStatusEntry.setIndexNames(
    (0, "PAIRGAIN-APS-MIB", "pgApsIndex"),
)
if mibBuilder.loadTexts:
    pgApsStatusEntry.setStatus("current")
_PgApsStatusK1K2Rx_Type = PgApsK1K2
_PgApsStatusK1K2Rx_Object = MibTableColumn
pgApsStatusK1K2Rx = _PgApsStatusK1K2Rx_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 1),
    _PgApsStatusK1K2Rx_Type()
)
pgApsStatusK1K2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsStatusK1K2Rx.setStatus("current")
_PgApsStatusK1K2Tx_Type = PgApsK1K2
_PgApsStatusK1K2Tx_Object = MibTableColumn
pgApsStatusK1K2Tx = _PgApsStatusK1K2Tx_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 2),
    _PgApsStatusK1K2Tx_Type()
)
pgApsStatusK1K2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsStatusK1K2Tx.setStatus("current")
_PgApsStatusCurrent_Type = Byte
_PgApsStatusCurrent_Object = MibTableColumn
pgApsStatusCurrent = _PgApsStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 3),
    _PgApsStatusCurrent_Type()
)
pgApsStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsStatusCurrent.setStatus("current")


class _PgApsWorkChanStatus_Type(Bits):
    """Custom type pgApsWorkChanStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2))
    )

_PgApsWorkChanStatus_Type.__name__ = "Bits"
_PgApsWorkChanStatus_Object = MibTableColumn
pgApsWorkChanStatus = _PgApsWorkChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 4),
    _PgApsWorkChanStatus_Type()
)
pgApsWorkChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkChanStatus.setStatus("current")
_PgApsWorkChanLastSwitch_Type = TimeTicks
_PgApsWorkChanLastSwitch_Object = MibTableColumn
pgApsWorkChanLastSwitch = _PgApsWorkChanLastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 5),
    _PgApsWorkChanLastSwitch_Type()
)
pgApsWorkChanLastSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkChanLastSwitch.setStatus("current")
_PgApsWorkChanSDs_Type = Counter32
_PgApsWorkChanSDs_Object = MibTableColumn
pgApsWorkChanSDs = _PgApsWorkChanSDs_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 6),
    _PgApsWorkChanSDs_Type()
)
pgApsWorkChanSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkChanSDs.setStatus("current")
_PgApsWorkChanSFs_Type = Counter32
_PgApsWorkChanSFs_Object = MibTableColumn
pgApsWorkChanSFs = _PgApsWorkChanSFs_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 7),
    _PgApsWorkChanSFs_Type()
)
pgApsWorkChanSFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkChanSFs.setStatus("current")
_PgApsWorkNumSwitchOvers_Type = Counter32
_PgApsWorkNumSwitchOvers_Object = MibTableColumn
pgApsWorkNumSwitchOvers = _PgApsWorkNumSwitchOvers_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 8),
    _PgApsWorkNumSwitchOvers_Type()
)
pgApsWorkNumSwitchOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsWorkNumSwitchOvers.setStatus("current")


class _PgApsProtChanStatus_Type(Bits):
    """Custom type pgApsProtChanStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2))
    )

_PgApsProtChanStatus_Type.__name__ = "Bits"
_PgApsProtChanStatus_Object = MibTableColumn
pgApsProtChanStatus = _PgApsProtChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 9),
    _PgApsProtChanStatus_Type()
)
pgApsProtChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtChanStatus.setStatus("current")
_PgApsProtChanLastSwitch_Type = TimeTicks
_PgApsProtChanLastSwitch_Object = MibTableColumn
pgApsProtChanLastSwitch = _PgApsProtChanLastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 10),
    _PgApsProtChanLastSwitch_Type()
)
pgApsProtChanLastSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtChanLastSwitch.setStatus("current")
_PgApsProtChanSDs_Type = Counter32
_PgApsProtChanSDs_Object = MibTableColumn
pgApsProtChanSDs = _PgApsProtChanSDs_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 11),
    _PgApsProtChanSDs_Type()
)
pgApsProtChanSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtChanSDs.setStatus("current")
_PgApsProtChanSFs_Type = Counter32
_PgApsProtChanSFs_Object = MibTableColumn
pgApsProtChanSFs = _PgApsProtChanSFs_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 12),
    _PgApsProtChanSFs_Type()
)
pgApsProtChanSFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtChanSFs.setStatus("current")
_PgApsProtNumSwitchOvers_Type = Counter32
_PgApsProtNumSwitchOvers_Object = MibTableColumn
pgApsProtNumSwitchOvers = _PgApsProtNumSwitchOvers_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 13),
    _PgApsProtNumSwitchOvers_Type()
)
pgApsProtNumSwitchOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgApsProtNumSwitchOvers.setStatus("current")

# Managed Objects groups


# Notification objects

pgApsTrapSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 0, 1)
)
pgApsTrapSwitchOver.setObjects(
    ("PAIRGAIN-APS-MIB", "pgApsStatusEntry")
)
if mibBuilder.loadTexts:
    pgApsTrapSwitchOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-APS-MIB",
    **{"Byte": Byte,
       "PgApsK1K2": PgApsK1K2,
       "pgAps": pgAps,
       "pgApsMIBNotifications": pgApsMIBNotifications,
       "pgApsTrapSwitchOver": pgApsTrapSwitchOver,
       "pgApsMibObjects": pgApsMibObjects,
       "pgApsConfigTable": pgApsConfigTable,
       "pgApsConfigEntry": pgApsConfigEntry,
       "pgApsIndex": pgApsIndex,
       "pgApsEnable": pgApsEnable,
       "pgApsTrapEnable": pgApsTrapEnable,
       "pgApsWorkChanIfIndex": pgApsWorkChanIfIndex,
       "pgApsProtChanIfIndex": pgApsProtChanIfIndex,
       "pgApsConfigMode": pgApsConfigMode,
       "pgApsConfigSigDegradeThresh": pgApsConfigSigDegradeThresh,
       "pgApsConfigWaitToRevert": pgApsConfigWaitToRevert,
       "pgApsSwitchCommand": pgApsSwitchCommand,
       "pgApsStatusTable": pgApsStatusTable,
       "pgApsStatusEntry": pgApsStatusEntry,
       "pgApsStatusK1K2Rx": pgApsStatusK1K2Rx,
       "pgApsStatusK1K2Tx": pgApsStatusK1K2Tx,
       "pgApsStatusCurrent": pgApsStatusCurrent,
       "pgApsWorkChanStatus": pgApsWorkChanStatus,
       "pgApsWorkChanLastSwitch": pgApsWorkChanLastSwitch,
       "pgApsWorkChanSDs": pgApsWorkChanSDs,
       "pgApsWorkChanSFs": pgApsWorkChanSFs,
       "pgApsWorkNumSwitchOvers": pgApsWorkNumSwitchOvers,
       "pgApsProtChanStatus": pgApsProtChanStatus,
       "pgApsProtChanLastSwitch": pgApsProtChanLastSwitch,
       "pgApsProtChanSDs": pgApsProtChanSDs,
       "pgApsProtChanSFs": pgApsProtChanSFs,
       "pgApsProtNumSwitchOvers": pgApsProtNumSwitchOvers}
)
