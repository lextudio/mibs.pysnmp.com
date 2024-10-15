# SNMP MIB module (INNOVX-DTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INNOVX-DTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:27 2024
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

(dteGroup,) = mibBuilder.importSymbols(
    "INNOVX-CORE-MIB",
    "dteGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DteAdmin_ObjectIdentity = ObjectIdentity
dteAdmin = _DteAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 1)
)


class _DtesMIBversion_Type(DisplayString):
    """Custom type dtesMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_DtesMIBversion_Type.__name__ = "DisplayString"
_DtesMIBversion_Object = MibScalar
dtesMIBversion = _DtesMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 1, 1),
    _DtesMIBversion_Type()
)
dtesMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtesMIBversion.setStatus("mandatory")
_DteCfg_ObjectIdentity = ObjectIdentity
dteCfg = _DteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 2)
)


class _DteInterfaceType_Type(Integer32):
    """Custom type dteInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 4),
          ("eia530a", 5),
          ("rs449", 3),
          ("v28", 1),
          ("v35", 2),
          ("x21", 6))
    )


_DteInterfaceType_Type.__name__ = "Integer32"
_DteInterfaceType_Object = MibScalar
dteInterfaceType = _DteInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 2, 1),
    _DteInterfaceType_Type()
)
dteInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteInterfaceType.setStatus("mandatory")


class _DteTxInvertingTiming_Type(Integer32):
    """Custom type dteTxInvertingTiming based on Integer32"""
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
          ("slaveInvert", 2),
          ("slaveNormal", 1))
    )


_DteTxInvertingTiming_Type.__name__ = "Integer32"
_DteTxInvertingTiming_Object = MibScalar
dteTxInvertingTiming = _DteTxInvertingTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 2, 2),
    _DteTxInvertingTiming_Type()
)
dteTxInvertingTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteTxInvertingTiming.setStatus("mandatory")


class _DteRxCarrier_Type(Integer32):
    """Custom type dteRxCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 1),
          ("normal", 2))
    )


_DteRxCarrier_Type.__name__ = "Integer32"
_DteRxCarrier_Object = MibScalar
dteRxCarrier = _DteRxCarrier_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 2, 3),
    _DteRxCarrier_Type()
)
dteRxCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteRxCarrier.setStatus("mandatory")


class _DteDsrControl_Type(Integer32):
    """Custom type dteDsrControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsDTR", 2),
          ("forcedOn", 1))
    )


_DteDsrControl_Type.__name__ = "Integer32"
_DteDsrControl_Object = MibScalar
dteDsrControl = _DteDsrControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 2, 4),
    _DteDsrControl_Type()
)
dteDsrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteDsrControl.setStatus("mandatory")
_DteAlarmCfg_ObjectIdentity = ObjectIdentity
dteAlarmCfg = _DteAlarmCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 3)
)


class _DteDtrLossTrapSeverity_Type(Integer32):
    """Custom type dteDtrLossTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_DteDtrLossTrapSeverity_Type.__name__ = "Integer32"
_DteDtrLossTrapSeverity_Object = MibScalar
dteDtrLossTrapSeverity = _DteDtrLossTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 3, 1),
    _DteDtrLossTrapSeverity_Type()
)
dteDtrLossTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteDtrLossTrapSeverity.setStatus("mandatory")
_DteDiagnostics_ObjectIdentity = ObjectIdentity
dteDiagnostics = _DteDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 4)
)


class _DteLoopback_Type(Integer32):
    """Custom type dteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 1),
          ("toChan", 2))
    )


_DteLoopback_Type.__name__ = "Integer32"
_DteLoopback_Object = MibScalar
dteLoopback = _DteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 4, 1),
    _DteLoopback_Type()
)
dteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteLoopback.setStatus("mandatory")


class _DteDiagTestDuration_Type(Integer32):
    """Custom type dteDiagTestDuration based on Integer32"""
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
        *(("testTime10Mins", 3),
          ("testTime1Min", 1),
          ("testTime20Mins", 4),
          ("testTime5Mins", 2))
    )


_DteDiagTestDuration_Type.__name__ = "Integer32"
_DteDiagTestDuration_Object = MibScalar
dteDiagTestDuration = _DteDiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 4, 2),
    _DteDiagTestDuration_Type()
)
dteDiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteDiagTestDuration.setStatus("mandatory")


class _DteDiagTestStatus_Type(Integer32):
    """Custom type dteDiagTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statDteLoop", 1),
          ("statNoTestinProgress", 2))
    )


_DteDiagTestStatus_Type.__name__ = "Integer32"
_DteDiagTestStatus_Object = MibScalar
dteDiagTestStatus = _DteDiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 4, 3),
    _DteDiagTestStatus_Type()
)
dteDiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteDiagTestStatus.setStatus("mandatory")
_DteStatus_ObjectIdentity = ObjectIdentity
dteStatus = _DteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 5)
)


class _DteLedStatus_Type(OctetString):
    """Custom type dteLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DteLedStatus_Type.__name__ = "OctetString"
_DteLedStatus_Object = MibScalar
dteLedStatus = _DteLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 5, 1),
    _DteLedStatus_Type()
)
dteLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteLedStatus.setStatus("mandatory")


class _DtePortStatus_Type(OctetString):
    """Custom type dtePortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DtePortStatus_Type.__name__ = "OctetString"
_DtePortStatus_Object = MibScalar
dtePortStatus = _DtePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 5, 2),
    _DtePortStatus_Type()
)
dtePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtePortStatus.setStatus("mandatory")


class _DtePortFrameCounts_Type(OctetString):
    """Custom type dtePortFrameCounts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DtePortFrameCounts_Type.__name__ = "OctetString"
_DtePortFrameCounts_Object = MibScalar
dtePortFrameCounts = _DtePortFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6, 5, 3),
    _DtePortFrameCounts_Type()
)
dtePortFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtePortFrameCounts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNOVX-DTE-MIB",
    **{"dteAdmin": dteAdmin,
       "dtesMIBversion": dtesMIBversion,
       "dteCfg": dteCfg,
       "dteInterfaceType": dteInterfaceType,
       "dteTxInvertingTiming": dteTxInvertingTiming,
       "dteRxCarrier": dteRxCarrier,
       "dteDsrControl": dteDsrControl,
       "dteAlarmCfg": dteAlarmCfg,
       "dteDtrLossTrapSeverity": dteDtrLossTrapSeverity,
       "dteDiagnostics": dteDiagnostics,
       "dteLoopback": dteLoopback,
       "dteDiagTestDuration": dteDiagTestDuration,
       "dteDiagTestStatus": dteDiagTestStatus,
       "dteStatus": dteStatus,
       "dteLedStatus": dteLedStatus,
       "dtePortStatus": dtePortStatus,
       "dtePortFrameCounts": dtePortFrameCounts}
)
