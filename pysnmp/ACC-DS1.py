# SNMP MIB module (ACC-DS1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DS1
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:07 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccDs1ExtTable_Object = MibTable
accDs1ExtTable = _AccDs1ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42)
)
if mibBuilder.loadTexts:
    accDs1ExtTable.setStatus("mandatory")
_AccDs1ExtEntry_Object = MibTableRow
accDs1ExtEntry = _AccDs1ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1)
)
accDs1ExtEntry.setIndexNames(
    (0, "ACC-DS1", "accDs1ExtLineIndex"),
)
if mibBuilder.loadTexts:
    accDs1ExtEntry.setStatus("mandatory")
_AccDs1ExtLineIndex_Type = Integer32
_AccDs1ExtLineIndex_Object = MibTableColumn
accDs1ExtLineIndex = _AccDs1ExtLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 1),
    _AccDs1ExtLineIndex_Type()
)
accDs1ExtLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs1ExtLineIndex.setStatus("mandatory")


class _AccDs1ExtLineLength_Type(Integer32):
    """Custom type accDs1ExtLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long", 3),
          ("medium", 2),
          ("short", 1))
    )


_AccDs1ExtLineLength_Type.__name__ = "Integer32"
_AccDs1ExtLineLength_Object = MibTableColumn
accDs1ExtLineLength = _AccDs1ExtLineLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 2),
    _AccDs1ExtLineLength_Type()
)
accDs1ExtLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtLineLength.setStatus("mandatory")
_AccDS1ExtNfasGroup_Type = Integer32
_AccDS1ExtNfasGroup_Object = MibTableColumn
accDS1ExtNfasGroup = _AccDS1ExtNfasGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 3),
    _AccDS1ExtNfasGroup_Type()
)
accDS1ExtNfasGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDS1ExtNfasGroup.setStatus("mandatory")


class _AccDs1ExtInterfaceId_Type(Integer32):
    """Custom type accDs1ExtInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AccDs1ExtInterfaceId_Type.__name__ = "Integer32"
_AccDs1ExtInterfaceId_Object = MibTableColumn
accDs1ExtInterfaceId = _AccDs1ExtInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 4),
    _AccDs1ExtInterfaceId_Type()
)
accDs1ExtInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtInterfaceId.setStatus("mandatory")


class _AccDs1ExtE1Type_Type(Integer32):
    """Custom type accDs1ExtE1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nordic", 2),
          ("normal", 1))
    )


_AccDs1ExtE1Type_Type.__name__ = "Integer32"
_AccDs1ExtE1Type_Object = MibTableColumn
accDs1ExtE1Type = _AccDs1ExtE1Type_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 5),
    _AccDs1ExtE1Type_Type()
)
accDs1ExtE1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtE1Type.setStatus("mandatory")


class _AccDs1ExtXcvr_Type(Integer32):
    """Custom type accDs1ExtXcvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("csu2", 2),
          ("dsx1", 1),
          ("e1-120ohm", 5),
          ("e1-75ohm", 7),
          ("hdsl", 6),
          ("hdsl-master", 3),
          ("hdsl-slave", 4))
    )


_AccDs1ExtXcvr_Type.__name__ = "Integer32"
_AccDs1ExtXcvr_Object = MibTableColumn
accDs1ExtXcvr = _AccDs1ExtXcvr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 6),
    _AccDs1ExtXcvr_Type()
)
accDs1ExtXcvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtXcvr.setStatus("mandatory")


class _AccDs1ExtPrecedence_Type(Integer32):
    """Custom type accDs1ExtPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AccDs1ExtPrecedence_Type.__name__ = "Integer32"
_AccDs1ExtPrecedence_Object = MibTableColumn
accDs1ExtPrecedence = _AccDs1ExtPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 7),
    _AccDs1ExtPrecedence_Type()
)
accDs1ExtPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtPrecedence.setStatus("mandatory")


class _AccDs1ExtSignalGroup_Type(Integer32):
    """Custom type accDs1ExtSignalGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccDs1ExtSignalGroup_Type.__name__ = "Integer32"
_AccDs1ExtSignalGroup_Object = MibTableColumn
accDs1ExtSignalGroup = _AccDs1ExtSignalGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 8),
    _AccDs1ExtSignalGroup_Type()
)
accDs1ExtSignalGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtSignalGroup.setStatus("mandatory")
_AccDs1ExtNumberGroup_Type = Integer32
_AccDs1ExtNumberGroup_Object = MibTableColumn
accDs1ExtNumberGroup = _AccDs1ExtNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 9),
    _AccDs1ExtNumberGroup_Type()
)
accDs1ExtNumberGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtNumberGroup.setStatus("mandatory")


class _AccDs1ExtIntegAccess_Type(Integer32):
    """Custom type accDs1ExtIntegAccess based on Integer32"""
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


_AccDs1ExtIntegAccess_Type.__name__ = "Integer32"
_AccDs1ExtIntegAccess_Object = MibTableColumn
accDs1ExtIntegAccess = _AccDs1ExtIntegAccess_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 10),
    _AccDs1ExtIntegAccess_Type()
)
accDs1ExtIntegAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtIntegAccess.setStatus("mandatory")


class _AccDs1ExtSignalMode_Type(Integer32):
    """Custom type accDs1ExtSignalMode based on Integer32"""
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
        *(("cas", 3),
          ("ccs", 4),
          ("etheric", 6),
          ("nfas", 5),
          ("none", 1),
          ("rbs", 2))
    )


_AccDs1ExtSignalMode_Type.__name__ = "Integer32"
_AccDs1ExtSignalMode_Object = MibTableColumn
accDs1ExtSignalMode = _AccDs1ExtSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 11),
    _AccDs1ExtSignalMode_Type()
)
accDs1ExtSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtSignalMode.setStatus("mandatory")
_AccDs1ExtCICBase_Type = Integer32
_AccDs1ExtCICBase_Object = MibTableColumn
accDs1ExtCICBase = _AccDs1ExtCICBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 12),
    _AccDs1ExtCICBase_Type()
)
accDs1ExtCICBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtCICBase.setStatus("mandatory")
_AccDs1ExtMessageLevel_Type = Integer32
_AccDs1ExtMessageLevel_Object = MibTableColumn
accDs1ExtMessageLevel = _AccDs1ExtMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 13),
    _AccDs1ExtMessageLevel_Type()
)
accDs1ExtMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1ExtMessageLevel.setStatus("mandatory")


class _AccDs1ExtServiceState_Type(Integer32):
    """Custom type accDs1ExtServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1InService", 1),
          ("ds1OutOfService", 2))
    )


_AccDs1ExtServiceState_Type.__name__ = "Integer32"
_AccDs1ExtServiceState_Object = MibTableColumn
accDs1ExtServiceState = _AccDs1ExtServiceState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 42, 1, 14),
    _AccDs1ExtServiceState_Type()
)
accDs1ExtServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs1ExtServiceState.setStatus("mandatory")
_AccDs1CircuitTable_Object = MibTable
accDs1CircuitTable = _AccDs1CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43)
)
if mibBuilder.loadTexts:
    accDs1CircuitTable.setStatus("mandatory")
_AccDs1CircuitEntry_Object = MibTableRow
accDs1CircuitEntry = _AccDs1CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1)
)
accDs1CircuitEntry.setIndexNames(
    (0, "ACC-DS1", "accDs1CircuitIndex"),
)
if mibBuilder.loadTexts:
    accDs1CircuitEntry.setStatus("mandatory")
_AccDs1CircuitIndex_Type = Integer32
_AccDs1CircuitIndex_Object = MibTableColumn
accDs1CircuitIndex = _AccDs1CircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 1),
    _AccDs1CircuitIndex_Type()
)
accDs1CircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDs1CircuitIndex.setStatus("mandatory")


class _AccDs1CircuitAdi_Type(Integer32):
    """Custom type accDs1CircuitAdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccDs1CircuitAdi_Type.__name__ = "Integer32"
_AccDs1CircuitAdi_Object = MibTableColumn
accDs1CircuitAdi = _AccDs1CircuitAdi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 2),
    _AccDs1CircuitAdi_Type()
)
accDs1CircuitAdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitAdi.setStatus("mandatory")


class _AccDs1CircuitBandwidth_Type(Integer32):
    """Custom type accDs1CircuitBandwidth based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-16", 2),
          ("bandwidth-24", 3),
          ("bandwidth-32", 4),
          ("bandwidth-40", 5),
          ("bandwidth-48", 6),
          ("bandwidth-56", 7),
          ("bandwidth-64", 8),
          ("bandwidth-8", 1))
    )


_AccDs1CircuitBandwidth_Type.__name__ = "Integer32"
_AccDs1CircuitBandwidth_Object = MibTableColumn
accDs1CircuitBandwidth = _AccDs1CircuitBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 3),
    _AccDs1CircuitBandwidth_Type()
)
accDs1CircuitBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitBandwidth.setStatus("mandatory")


class _AccDs1CircuitBusyout_Type(Integer32):
    """Custom type accDs1CircuitBusyout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("unbusy", 2))
    )


_AccDs1CircuitBusyout_Type.__name__ = "Integer32"
_AccDs1CircuitBusyout_Object = MibTableColumn
accDs1CircuitBusyout = _AccDs1CircuitBusyout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 4),
    _AccDs1CircuitBusyout_Type()
)
accDs1CircuitBusyout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitBusyout.setStatus("mandatory")


class _AccDs1CircuitInversion_Type(Integer32):
    """Custom type accDs1CircuitInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccDs1CircuitInversion_Type.__name__ = "Integer32"
_AccDs1CircuitInversion_Object = MibTableColumn
accDs1CircuitInversion = _AccDs1CircuitInversion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 5),
    _AccDs1CircuitInversion_Type()
)
accDs1CircuitInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitInversion.setStatus("mandatory")
_AccDs1CircuitName_Type = DisplayString
_AccDs1CircuitName_Object = MibTableColumn
accDs1CircuitName = _AccDs1CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 6),
    _AccDs1CircuitName_Type()
)
accDs1CircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitName.setStatus("mandatory")


class _AccDs1CircuitConfigStatus_Type(Integer32):
    """Custom type accDs1CircuitConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("static", 2),
          ("unconfig", 1))
    )


_AccDs1CircuitConfigStatus_Type.__name__ = "Integer32"
_AccDs1CircuitConfigStatus_Object = MibTableColumn
accDs1CircuitConfigStatus = _AccDs1CircuitConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 7),
    _AccDs1CircuitConfigStatus_Type()
)
accDs1CircuitConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitConfigStatus.setStatus("mandatory")


class _AccDs1CircuitLoopback_Type(Integer32):
    """Custom type accDs1CircuitLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback-a", 2),
          ("loopback-c", 3),
          ("none", 1))
    )


_AccDs1CircuitLoopback_Type.__name__ = "Integer32"
_AccDs1CircuitLoopback_Object = MibTableColumn
accDs1CircuitLoopback = _AccDs1CircuitLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 8),
    _AccDs1CircuitLoopback_Type()
)
accDs1CircuitLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitLoopback.setStatus("mandatory")


class _AccDs1CircuitRbs_Type(Integer32):
    """Custom type accDs1CircuitRbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccDs1CircuitRbs_Type.__name__ = "Integer32"
_AccDs1CircuitRbs_Object = MibTableColumn
accDs1CircuitRbs = _AccDs1CircuitRbs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 9),
    _AccDs1CircuitRbs_Type()
)
accDs1CircuitRbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitRbs.setStatus("mandatory")
_AccDs1CircuitSuperrateMask_Type = Integer32
_AccDs1CircuitSuperrateMask_Object = MibTableColumn
accDs1CircuitSuperrateMask = _AccDs1CircuitSuperrateMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 43, 1, 10),
    _AccDs1CircuitSuperrateMask_Type()
)
accDs1CircuitSuperrateMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDs1CircuitSuperrateMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DS1",
    **{"accDs1ExtTable": accDs1ExtTable,
       "accDs1ExtEntry": accDs1ExtEntry,
       "accDs1ExtLineIndex": accDs1ExtLineIndex,
       "accDs1ExtLineLength": accDs1ExtLineLength,
       "accDS1ExtNfasGroup": accDS1ExtNfasGroup,
       "accDs1ExtInterfaceId": accDs1ExtInterfaceId,
       "accDs1ExtE1Type": accDs1ExtE1Type,
       "accDs1ExtXcvr": accDs1ExtXcvr,
       "accDs1ExtPrecedence": accDs1ExtPrecedence,
       "accDs1ExtSignalGroup": accDs1ExtSignalGroup,
       "accDs1ExtNumberGroup": accDs1ExtNumberGroup,
       "accDs1ExtIntegAccess": accDs1ExtIntegAccess,
       "accDs1ExtSignalMode": accDs1ExtSignalMode,
       "accDs1ExtCICBase": accDs1ExtCICBase,
       "accDs1ExtMessageLevel": accDs1ExtMessageLevel,
       "accDs1ExtServiceState": accDs1ExtServiceState,
       "accDs1CircuitTable": accDs1CircuitTable,
       "accDs1CircuitEntry": accDs1CircuitEntry,
       "accDs1CircuitIndex": accDs1CircuitIndex,
       "accDs1CircuitAdi": accDs1CircuitAdi,
       "accDs1CircuitBandwidth": accDs1CircuitBandwidth,
       "accDs1CircuitBusyout": accDs1CircuitBusyout,
       "accDs1CircuitInversion": accDs1CircuitInversion,
       "accDs1CircuitName": accDs1CircuitName,
       "accDs1CircuitConfigStatus": accDs1CircuitConfigStatus,
       "accDs1CircuitLoopback": accDs1CircuitLoopback,
       "accDs1CircuitRbs": accDs1CircuitRbs,
       "accDs1CircuitSuperrateMask": accDs1CircuitSuperrateMask}
)
