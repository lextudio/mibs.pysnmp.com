# SNMP MIB module (Fore-Framnetmod-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Framnetmod-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:01 2024
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

(frCircuitDlci,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "frCircuitDlci")

(atmSwitch,
 frameInternetworking) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "atmSwitch",
    "frameInternetworking")

(funiConnFuniVci,
 funiConnFuniVpi) = mibBuilder.importSymbols(
    "Fore-Funi-MIB",
    "funiConnFuniVci",
    "funiConnFuniVpi")

(ifConvertToIfIndexChannelId,
 ifConvertToIfIndexPortId) = mibBuilder.importSymbols(
    "Fore-Ifcreate-MIB",
    "ifConvertToIfIndexChannelId",
    "ifConvertToIfIndexPortId")

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

fram = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmFramNetmodConfTable_Object = MibTable
nmFramNetmodConfTable = _NmFramNetmodConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    nmFramNetmodConfTable.setStatus("current")
_NmFramNetmodConfEntry_Object = MibTableRow
nmFramNetmodConfEntry = _NmFramNetmodConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1)
)
nmFramNetmodConfEntry.setIndexNames(
    (0, "Fore-Framnetmod-MIB", "nmFramBoard"),
    (0, "Fore-Framnetmod-MIB", "nmFramModule"),
)
if mibBuilder.loadTexts:
    nmFramNetmodConfEntry.setStatus("current")
_NmFramBoard_Type = Integer32
_NmFramBoard_Object = MibTableColumn
nmFramBoard = _NmFramBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 1),
    _NmFramBoard_Type()
)
nmFramBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramBoard.setStatus("current")
_NmFramModule_Type = Integer32
_NmFramModule_Object = MibTableColumn
nmFramModule = _NmFramModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 2),
    _NmFramModule_Type()
)
nmFramModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramModule.setStatus("current")


class _NmFramEpdPpdBufferProportion_Type(Integer32):
    """Custom type nmFramEpdPpdBufferProportion based on Integer32"""
    defaultValue = 3

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
        *(("high1quarter", 2),
          ("high2quarter", 3),
          ("high3quarter", 4),
          ("highzero", 1))
    )


_NmFramEpdPpdBufferProportion_Type.__name__ = "Integer32"
_NmFramEpdPpdBufferProportion_Object = MibTableColumn
nmFramEpdPpdBufferProportion = _NmFramEpdPpdBufferProportion_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 3),
    _NmFramEpdPpdBufferProportion_Type()
)
nmFramEpdPpdBufferProportion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramEpdPpdBufferProportion.setStatus("current")


class _NmFramEpdclp1HighPrio_Type(Integer32):
    """Custom type nmFramEpdclp1HighPrio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(37, 37),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
    )


_NmFramEpdclp1HighPrio_Type.__name__ = "Integer32"
_NmFramEpdclp1HighPrio_Object = MibTableColumn
nmFramEpdclp1HighPrio = _NmFramEpdclp1HighPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 4),
    _NmFramEpdclp1HighPrio_Type()
)
nmFramEpdclp1HighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramEpdclp1HighPrio.setStatus("current")


class _NmFramEpdclp0HighPrio_Type(Integer32):
    """Custom type nmFramEpdclp0HighPrio based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(87, 87),
    )


_NmFramEpdclp0HighPrio_Type.__name__ = "Integer32"
_NmFramEpdclp0HighPrio_Object = MibTableColumn
nmFramEpdclp0HighPrio = _NmFramEpdclp0HighPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 5),
    _NmFramEpdclp0HighPrio_Type()
)
nmFramEpdclp0HighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramEpdclp0HighPrio.setStatus("current")


class _NmFramPpdclp1HighPrio_Type(Integer32):
    """Custom type nmFramPpdclp1HighPrio based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(87, 87),
    )


_NmFramPpdclp1HighPrio_Type.__name__ = "Integer32"
_NmFramPpdclp1HighPrio_Object = MibTableColumn
nmFramPpdclp1HighPrio = _NmFramPpdclp1HighPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 6),
    _NmFramPpdclp1HighPrio_Type()
)
nmFramPpdclp1HighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramPpdclp1HighPrio.setStatus("current")


class _NmFramEpdclp1LowPrio_Type(Integer32):
    """Custom type nmFramEpdclp1LowPrio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(37, 37),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
    )


_NmFramEpdclp1LowPrio_Type.__name__ = "Integer32"
_NmFramEpdclp1LowPrio_Object = MibTableColumn
nmFramEpdclp1LowPrio = _NmFramEpdclp1LowPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 7),
    _NmFramEpdclp1LowPrio_Type()
)
nmFramEpdclp1LowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramEpdclp1LowPrio.setStatus("current")


class _NmFramEpdclp0LowPrio_Type(Integer32):
    """Custom type nmFramEpdclp0LowPrio based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(87, 87),
    )


_NmFramEpdclp0LowPrio_Type.__name__ = "Integer32"
_NmFramEpdclp0LowPrio_Object = MibTableColumn
nmFramEpdclp0LowPrio = _NmFramEpdclp0LowPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 8),
    _NmFramEpdclp0LowPrio_Type()
)
nmFramEpdclp0LowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramEpdclp0LowPrio.setStatus("current")


class _NmFramPpdclp1LowPrio_Type(Integer32):
    """Custom type nmFramPpdclp1LowPrio based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(62, 62),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(87, 87),
    )


_NmFramPpdclp1LowPrio_Type.__name__ = "Integer32"
_NmFramPpdclp1LowPrio_Object = MibTableColumn
nmFramPpdclp1LowPrio = _NmFramPpdclp1LowPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 9),
    _NmFramPpdclp1LowPrio_Type()
)
nmFramPpdclp1LowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramPpdclp1LowPrio.setStatus("current")


class _NmFramOamF5Supervision_Type(Integer32):
    """Custom type nmFramOamF5Supervision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NmFramOamF5Supervision_Type.__name__ = "Integer32"
_NmFramOamF5Supervision_Object = MibTableColumn
nmFramOamF5Supervision = _NmFramOamF5Supervision_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 10),
    _NmFramOamF5Supervision_Type()
)
nmFramOamF5Supervision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramOamF5Supervision.setStatus("current")


class _NmFramOamF5AISRxPeriod_Type(Integer32):
    """Custom type nmFramOamF5AISRxPeriod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NmFramOamF5AISRxPeriod_Type.__name__ = "Integer32"
_NmFramOamF5AISRxPeriod_Object = MibTableColumn
nmFramOamF5AISRxPeriod = _NmFramOamF5AISRxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 11),
    _NmFramOamF5AISRxPeriod_Type()
)
nmFramOamF5AISRxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramOamF5AISRxPeriod.setStatus("current")


class _NmFramOamF5AISTxPeriod_Type(Integer32):
    """Custom type nmFramOamF5AISTxPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NmFramOamF5AISTxPeriod_Type.__name__ = "Integer32"
_NmFramOamF5AISTxPeriod_Object = MibTableColumn
nmFramOamF5AISTxPeriod = _NmFramOamF5AISTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 12),
    _NmFramOamF5AISTxPeriod_Type()
)
nmFramOamF5AISTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramOamF5AISTxPeriod.setStatus("current")


class _NmFramOamF5RDIRxPeriod_Type(Integer32):
    """Custom type nmFramOamF5RDIRxPeriod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NmFramOamF5RDIRxPeriod_Type.__name__ = "Integer32"
_NmFramOamF5RDIRxPeriod_Object = MibTableColumn
nmFramOamF5RDIRxPeriod = _NmFramOamF5RDIRxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 13),
    _NmFramOamF5RDIRxPeriod_Type()
)
nmFramOamF5RDIRxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramOamF5RDIRxPeriod.setStatus("current")


class _NmFramOamF5RDITxPeriod_Type(Integer32):
    """Custom type nmFramOamF5RDITxPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NmFramOamF5RDITxPeriod_Type.__name__ = "Integer32"
_NmFramOamF5RDITxPeriod_Object = MibTableColumn
nmFramOamF5RDITxPeriod = _NmFramOamF5RDITxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 14),
    _NmFramOamF5RDITxPeriod_Type()
)
nmFramOamF5RDITxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramOamF5RDITxPeriod.setStatus("current")


class _NmFramOperState_Type(Integer32):
    """Custom type nmFramOperState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("appluprunning", 10),
          ("bootconsole", 9),
          ("down", 11),
          ("justinserted", 1),
          ("pulledout", 8),
          ("releasedreset", 2),
          ("selftest", 6),
          ("startupfailed", 7),
          ("waitapplstartup", 5),
          ("waitmsgstartup", 3),
          ("waittestend", 4))
    )


_NmFramOperState_Type.__name__ = "Integer32"
_NmFramOperState_Object = MibTableColumn
nmFramOperState = _NmFramOperState_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 15),
    _NmFramOperState_Type()
)
nmFramOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramOperState.setStatus("deprecated")
_NmFramApplSwRelease_Type = DisplayString
_NmFramApplSwRelease_Object = MibTableColumn
nmFramApplSwRelease = _NmFramApplSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 16),
    _NmFramApplSwRelease_Type()
)
nmFramApplSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramApplSwRelease.setStatus("deprecated")
_NmFramBootSwRelease_Type = DisplayString
_NmFramBootSwRelease_Object = MibTableColumn
nmFramBootSwRelease = _NmFramBootSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 17),
    _NmFramBootSwRelease_Type()
)
nmFramBootSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramBootSwRelease.setStatus("deprecated")
_NmFramApplKey_Type = DisplayString
_NmFramApplKey_Object = MibTableColumn
nmFramApplKey = _NmFramApplKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 18),
    _NmFramApplKey_Type()
)
nmFramApplKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramApplKey.setStatus("deprecated")


class _NmFramApplication_Type(Integer32):
    """Custom type nmFramApplication based on Integer32"""
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
        *(("frAtmNetworkAppl", 2),
          ("frAtmServiceAppl", 1),
          ("framFuniAppl", 3))
    )


_NmFramApplication_Type.__name__ = "Integer32"
_NmFramApplication_Object = MibTableColumn
nmFramApplication = _NmFramApplication_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 19),
    _NmFramApplication_Type()
)
nmFramApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramApplication.setStatus("current")


class _NmFramOosLED_Type(Integer32):
    """Custom type nmFramOosLED based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("red", 3))
    )


_NmFramOosLED_Type.__name__ = "Integer32"
_NmFramOosLED_Object = MibTableColumn
nmFramOosLED = _NmFramOosLED_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 20),
    _NmFramOosLED_Type()
)
nmFramOosLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramOosLED.setStatus("deprecated")


class _NmFramMaxSigPathsPerPort_Type(Integer32):
    """Custom type nmFramMaxSigPathsPerPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_NmFramMaxSigPathsPerPort_Type.__name__ = "Integer32"
_NmFramMaxSigPathsPerPort_Object = MibTableColumn
nmFramMaxSigPathsPerPort = _NmFramMaxSigPathsPerPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 21),
    _NmFramMaxSigPathsPerPort_Type()
)
nmFramMaxSigPathsPerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramMaxSigPathsPerPort.setStatus("current")


class _NmFramStatsMonitor_Type(Integer32):
    """Custom type nmFramStatsMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NmFramStatsMonitor_Type.__name__ = "Integer32"
_NmFramStatsMonitor_Object = MibTableColumn
nmFramStatsMonitor = _NmFramStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 22),
    _NmFramStatsMonitor_Type()
)
nmFramStatsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFramStatsMonitor.setStatus("current")
_NmFramStatsEnabledTimeStamp_Type = TimeTicks
_NmFramStatsEnabledTimeStamp_Object = MibTableColumn
nmFramStatsEnabledTimeStamp = _NmFramStatsEnabledTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 23),
    _NmFramStatsEnabledTimeStamp_Type()
)
nmFramStatsEnabledTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramStatsEnabledTimeStamp.setStatus("current")
_NmFramMsgType_Type = Integer32
_NmFramMsgType_Object = MibTableColumn
nmFramMsgType = _NmFramMsgType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 24),
    _NmFramMsgType_Type()
)
nmFramMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramMsgType.setStatus("current")
_NmFramNakCause_Type = Integer32
_NmFramNakCause_Object = MibTableColumn
nmFramNakCause = _NmFramNakCause_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 25),
    _NmFramNakCause_Type()
)
nmFramNakCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFramNakCause.setStatus("current")

# Managed Objects groups


# Notification objects

framNakMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2003)
)
framNakMsg.setObjects(
      *(("Fore-Framnetmod-MIB", "nmFramMsgType"),
        ("Fore-Framnetmod-MIB", "nmFramNakCause"),
        ("Fore-Framnetmod-MIB", "nmFramBoard"),
        ("Fore-Framnetmod-MIB", "nmFramModule"),
        ("Fore-Ifcreate-MIB", "ifConvertToIfIndexPortId"),
        ("Fore-Ifcreate-MIB", "ifConvertToIfIndexChannelId"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
        ("Fore-Funi-MIB", "funiConnFuniVpi"),
        ("Fore-Funi-MIB", "funiConnFuniVci"))
)
if mibBuilder.loadTexts:
    framNakMsg.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Framnetmod-MIB",
    **{"fram": fram,
       "nmFramNetmodConfTable": nmFramNetmodConfTable,
       "nmFramNetmodConfEntry": nmFramNetmodConfEntry,
       "nmFramBoard": nmFramBoard,
       "nmFramModule": nmFramModule,
       "nmFramEpdPpdBufferProportion": nmFramEpdPpdBufferProportion,
       "nmFramEpdclp1HighPrio": nmFramEpdclp1HighPrio,
       "nmFramEpdclp0HighPrio": nmFramEpdclp0HighPrio,
       "nmFramPpdclp1HighPrio": nmFramPpdclp1HighPrio,
       "nmFramEpdclp1LowPrio": nmFramEpdclp1LowPrio,
       "nmFramEpdclp0LowPrio": nmFramEpdclp0LowPrio,
       "nmFramPpdclp1LowPrio": nmFramPpdclp1LowPrio,
       "nmFramOamF5Supervision": nmFramOamF5Supervision,
       "nmFramOamF5AISRxPeriod": nmFramOamF5AISRxPeriod,
       "nmFramOamF5AISTxPeriod": nmFramOamF5AISTxPeriod,
       "nmFramOamF5RDIRxPeriod": nmFramOamF5RDIRxPeriod,
       "nmFramOamF5RDITxPeriod": nmFramOamF5RDITxPeriod,
       "nmFramOperState": nmFramOperState,
       "nmFramApplSwRelease": nmFramApplSwRelease,
       "nmFramBootSwRelease": nmFramBootSwRelease,
       "nmFramApplKey": nmFramApplKey,
       "nmFramApplication": nmFramApplication,
       "nmFramOosLED": nmFramOosLED,
       "nmFramMaxSigPathsPerPort": nmFramMaxSigPathsPerPort,
       "nmFramStatsMonitor": nmFramStatsMonitor,
       "nmFramStatsEnabledTimeStamp": nmFramStatsEnabledTimeStamp,
       "nmFramMsgType": nmFramMsgType,
       "nmFramNakCause": nmFramNakCause,
       "framNakMsg": framNakMsg}
)
