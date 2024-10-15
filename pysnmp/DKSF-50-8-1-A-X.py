# SNMP MIB module (DKSF-50-8-1-A-X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DKSF-50-8-1-A-X
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:23 2024
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 50)
)
netPing.setRevisions(
        ("2010-04-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpPwr_ObjectIdentity = ObjectIdentity
npPwr = _NpPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5800)
)
_NpPwrTable_Object = MibTable
npPwrTable = _NpPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3)
)
if mibBuilder.loadTexts:
    npPwrTable.setStatus("current")
_NpPwrEntry_Object = MibTableRow
npPwrEntry = _NpPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1)
)
npPwrEntry.setIndexNames(
    (0, "DKSF-50-8-1-A-X", "npPwrChannelN"),
)
if mibBuilder.loadTexts:
    npPwrEntry.setStatus("current")


class _NpPwrChannelN_Type(Integer32):
    """Custom type npPwrChannelN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NpPwrChannelN_Type.__name__ = "Integer32"
_NpPwrChannelN_Object = MibTableColumn
npPwrChannelN = _NpPwrChannelN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 1),
    _NpPwrChannelN_Type()
)
npPwrChannelN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npPwrChannelN.setStatus("current")


class _NpPwrStartReset_Type(Integer32):
    """Custom type npPwrStartReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_NpPwrStartReset_Type.__name__ = "Integer32"
_NpPwrStartReset_Object = MibTableColumn
npPwrStartReset = _NpPwrStartReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 2),
    _NpPwrStartReset_Type()
)
npPwrStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npPwrStartReset.setStatus("current")


class _NpPwrManualMode_Type(Integer32):
    """Custom type npPwrManualMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("watchdog", 2))
    )


_NpPwrManualMode_Type.__name__ = "Integer32"
_NpPwrManualMode_Object = MibTableColumn
npPwrManualMode = _NpPwrManualMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 3),
    _NpPwrManualMode_Type()
)
npPwrManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npPwrManualMode.setStatus("current")


class _NpPwrResetsCounter_Type(Integer32):
    """Custom type npPwrResetsCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NpPwrResetsCounter_Type.__name__ = "Integer32"
_NpPwrResetsCounter_Object = MibTableColumn
npPwrResetsCounter = _NpPwrResetsCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 4),
    _NpPwrResetsCounter_Type()
)
npPwrResetsCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npPwrResetsCounter.setStatus("current")


class _NpPwrRepeatingResetsCounter_Type(Integer32):
    """Custom type npPwrRepeatingResetsCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NpPwrRepeatingResetsCounter_Type.__name__ = "Integer32"
_NpPwrRepeatingResetsCounter_Object = MibTableColumn
npPwrRepeatingResetsCounter = _NpPwrRepeatingResetsCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 5),
    _NpPwrRepeatingResetsCounter_Type()
)
npPwrRepeatingResetsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npPwrRepeatingResetsCounter.setStatus("current")
_NpPwrMemo_Type = DisplayString
_NpPwrMemo_Object = MibTableColumn
npPwrMemo = _NpPwrMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 6),
    _NpPwrMemo_Type()
)
npPwrMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npPwrMemo.setStatus("current")
_NpCurLoop_ObjectIdentity = ObjectIdentity
npCurLoop = _NpCurLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300)
)
_NpCurLoopTable_Object = MibTable
npCurLoopTable = _NpCurLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1)
)
if mibBuilder.loadTexts:
    npCurLoopTable.setStatus("current")
_NpCurLoopEntry_Object = MibTableRow
npCurLoopEntry = _NpCurLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1)
)
npCurLoopEntry.setIndexNames(
    (0, "DKSF-50-8-1-A-X", "npCurLoopN"),
)
if mibBuilder.loadTexts:
    npCurLoopEntry.setStatus("current")


class _NpCurLoopN_Type(Integer32):
    """Custom type npCurLoopN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopN_Type.__name__ = "Integer32"
_NpCurLoopN_Object = MibTableColumn
npCurLoopN = _NpCurLoopN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1),
    _NpCurLoopN_Type()
)
npCurLoopN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopN.setStatus("current")


class _NpCurLoopStatus_Type(Integer32):
    """Custom type npCurLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("cut", 2),
          ("notPowered", 4),
          ("ok", 0),
          ("short", 3))
    )


_NpCurLoopStatus_Type.__name__ = "Integer32"
_NpCurLoopStatus_Object = MibTableColumn
npCurLoopStatus = _NpCurLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2),
    _NpCurLoopStatus_Type()
)
npCurLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopStatus.setStatus("current")


class _NpCurLoopI_Type(Integer32):
    """Custom type npCurLoopI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopI_Type.__name__ = "Integer32"
_NpCurLoopI_Object = MibTableColumn
npCurLoopI = _NpCurLoopI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3),
    _NpCurLoopI_Type()
)
npCurLoopI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopI.setStatus("current")


class _NpCurLoopV_Type(Integer32):
    """Custom type npCurLoopV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopV_Type.__name__ = "Integer32"
_NpCurLoopV_Object = MibTableColumn
npCurLoopV = _NpCurLoopV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4),
    _NpCurLoopV_Type()
)
npCurLoopV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopV.setStatus("current")


class _NpCurLoopR_Type(Integer32):
    """Custom type npCurLoopR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopR_Type.__name__ = "Integer32"
_NpCurLoopR_Object = MibTableColumn
npCurLoopR = _NpCurLoopR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5),
    _NpCurLoopR_Type()
)
npCurLoopR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopR.setStatus("current")


class _NpCurLoopPower_Type(Integer32):
    """Custom type npCurLoopPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cyclePower", 2),
          ("off", 0),
          ("on", 1))
    )


_NpCurLoopPower_Type.__name__ = "Integer32"
_NpCurLoopPower_Object = MibTableColumn
npCurLoopPower = _NpCurLoopPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7),
    _NpCurLoopPower_Type()
)
npCurLoopPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopPower.setStatus("current")
_NpRelHumidity_ObjectIdentity = ObjectIdentity
npRelHumidity = _NpRelHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400)
)
_NpRelHumSensor_ObjectIdentity = ObjectIdentity
npRelHumSensor = _NpRelHumSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2)
)


class _NpRelHumSensorValueH_Type(Integer32):
    """Custom type npRelHumSensorValueH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSensorValueH_Type.__name__ = "Integer32"
_NpRelHumSensorValueH_Object = MibScalar
npRelHumSensorValueH = _NpRelHumSensorValueH_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2),
    _NpRelHumSensorValueH_Type()
)
npRelHumSensorValueH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorValueH.setStatus("current")


class _NpRelHumSensorStatus_Type(Integer32):
    """Custom type npRelHumSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ok", 0))
    )


_NpRelHumSensorStatus_Type.__name__ = "Integer32"
_NpRelHumSensorStatus_Object = MibScalar
npRelHumSensorStatus = _NpRelHumSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3),
    _NpRelHumSensorStatus_Type()
)
npRelHumSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorStatus.setStatus("current")


class _NpRelHumSensorValueT_Type(Integer32):
    """Custom type npRelHumSensorValueT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 200),
    )


_NpRelHumSensorValueT_Type.__name__ = "Integer32"
_NpRelHumSensorValueT_Object = MibScalar
npRelHumSensorValueT = _NpRelHumSensorValueT_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4),
    _NpRelHumSensorValueT_Type()
)
npRelHumSensorValueT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorValueT.setStatus("current")
_NpThermo_ObjectIdentity = ObjectIdentity
npThermo = _NpThermo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800)
)
_NpThermoTable_Object = MibTable
npThermoTable = _NpThermoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1)
)
if mibBuilder.loadTexts:
    npThermoTable.setStatus("current")
_NpThermoEntry_Object = MibTableRow
npThermoEntry = _NpThermoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1)
)
npThermoEntry.setIndexNames(
    (0, "DKSF-50-8-1-A-X", "npThermoSensorN"),
)
if mibBuilder.loadTexts:
    npThermoEntry.setStatus("current")


class _NpThermoSensorN_Type(Integer32):
    """Custom type npThermoSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoSensorN_Type.__name__ = "Integer32"
_NpThermoSensorN_Object = MibTableColumn
npThermoSensorN = _NpThermoSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1),
    _NpThermoSensorN_Type()
)
npThermoSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoSensorN.setStatus("current")


class _NpThermoValue_Type(Integer32):
    """Custom type npThermoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoValue_Type.__name__ = "Integer32"
_NpThermoValue_Object = MibTableColumn
npThermoValue = _NpThermoValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2),
    _NpThermoValue_Type()
)
npThermoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValue.setStatus("current")


class _NpThermoStatus_Type(Integer32):
    """Custom type npThermoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("high", 3),
          ("low", 1),
          ("norm", 2))
    )


_NpThermoStatus_Type.__name__ = "Integer32"
_NpThermoStatus_Object = MibTableColumn
npThermoStatus = _NpThermoStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3),
    _NpThermoStatus_Type()
)
npThermoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoStatus.setStatus("current")


class _NpThermoLow_Type(Integer32):
    """Custom type npThermoLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoLow_Type.__name__ = "Integer32"
_NpThermoLow_Object = MibTableColumn
npThermoLow = _NpThermoLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4),
    _NpThermoLow_Type()
)
npThermoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoLow.setStatus("current")


class _NpThermoHigh_Type(Integer32):
    """Custom type npThermoHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoHigh_Type.__name__ = "Integer32"
_NpThermoHigh_Object = MibTableColumn
npThermoHigh = _NpThermoHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5),
    _NpThermoHigh_Type()
)
npThermoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoHigh.setStatus("current")
_NpThermoMemo_Type = DisplayString
_NpThermoMemo_Object = MibTableColumn
npThermoMemo = _NpThermoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6),
    _NpThermoMemo_Type()
)
npThermoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoMemo.setStatus("current")
_NpIo_ObjectIdentity = ObjectIdentity
npIo = _NpIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900)
)
_NpIoTable_Object = MibTable
npIoTable = _NpIoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1)
)
if mibBuilder.loadTexts:
    npIoTable.setStatus("current")
_NpIoEntry_Object = MibTableRow
npIoEntry = _NpIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1)
)
npIoEntry.setIndexNames(
    (0, "DKSF-50-8-1-A-X", "npIoLineN"),
)
if mibBuilder.loadTexts:
    npIoEntry.setStatus("current")


class _NpIoLineN_Type(Integer32):
    """Custom type npIoLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NpIoLineN_Type.__name__ = "Integer32"
_NpIoLineN_Object = MibTableColumn
npIoLineN = _NpIoLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1),
    _NpIoLineN_Type()
)
npIoLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLineN.setStatus("current")


class _NpIoLevelIn_Type(Integer32):
    """Custom type npIoLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelIn_Type.__name__ = "Integer32"
_NpIoLevelIn_Object = MibTableColumn
npIoLevelIn = _NpIoLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2),
    _NpIoLevelIn_Type()
)
npIoLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLevelIn.setStatus("current")


class _NpIoLevelOut_Type(Integer32):
    """Custom type npIoLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelOut_Type.__name__ = "Integer32"
_NpIoLevelOut_Object = MibTableColumn
npIoLevelOut = _NpIoLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3),
    _NpIoLevelOut_Type()
)
npIoLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoLevelOut.setStatus("current")
_NpIoMemo_Type = DisplayString
_NpIoMemo_Object = MibTableColumn
npIoMemo = _NpIoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6),
    _NpIoMemo_Type()
)
npIoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoMemo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-50-8-1-A-X",
    **{"lightcom": lightcom,
       "netPing": netPing,
       "npPwr": npPwr,
       "npPwrTable": npPwrTable,
       "npPwrEntry": npPwrEntry,
       "npPwrChannelN": npPwrChannelN,
       "npPwrStartReset": npPwrStartReset,
       "npPwrManualMode": npPwrManualMode,
       "npPwrResetsCounter": npPwrResetsCounter,
       "npPwrRepeatingResetsCounter": npPwrRepeatingResetsCounter,
       "npPwrMemo": npPwrMemo,
       "npCurLoop": npCurLoop,
       "npCurLoopTable": npCurLoopTable,
       "npCurLoopEntry": npCurLoopEntry,
       "npCurLoopN": npCurLoopN,
       "npCurLoopStatus": npCurLoopStatus,
       "npCurLoopI": npCurLoopI,
       "npCurLoopV": npCurLoopV,
       "npCurLoopR": npCurLoopR,
       "npCurLoopPower": npCurLoopPower,
       "npRelHumidity": npRelHumidity,
       "npRelHumSensor": npRelHumSensor,
       "npRelHumSensorValueH": npRelHumSensorValueH,
       "npRelHumSensorStatus": npRelHumSensorStatus,
       "npRelHumSensorValueT": npRelHumSensorValueT,
       "npThermo": npThermo,
       "npThermoTable": npThermoTable,
       "npThermoEntry": npThermoEntry,
       "npThermoSensorN": npThermoSensorN,
       "npThermoValue": npThermoValue,
       "npThermoStatus": npThermoStatus,
       "npThermoLow": npThermoLow,
       "npThermoHigh": npThermoHigh,
       "npThermoMemo": npThermoMemo,
       "npIo": npIo,
       "npIoTable": npIoTable,
       "npIoEntry": npIoEntry,
       "npIoLineN": npIoLineN,
       "npIoLevelIn": npIoLevelIn,
       "npIoLevelOut": npIoLevelOut,
       "npIoMemo": npIoMemo}
)
