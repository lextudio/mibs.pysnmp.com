# SNMP MIB module (RFC1407-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1407-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:30 2024
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

(EnableIndicator,
 extensions) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "extensions")

(dsx3TotalIndex,) = mibBuilder.importSymbols(
    "RFC1407-MIB",
    "dsx3TotalIndex")

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

_Cnds3e3Ext_ObjectIdentity = ObjectIdentity
cnds3e3Ext = _Cnds3e3Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 6)
)
_Cndsx3Oper_ObjectIdentity = ObjectIdentity
cndsx3Oper = _Cndsx3Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1)
)
_Cndsx3OperTable_Object = MibTable
cndsx3OperTable = _Cndsx3OperTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cndsx3OperTable.setStatus("mandatory")
_Cndsx3OperEntry_Object = MibTableRow
cndsx3OperEntry = _Cndsx3OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1)
)
cndsx3OperEntry.setIndexNames(
    (0, "RFC1407-EXT-MIB", "cndsx3OperLineIndex"),
)
if mibBuilder.loadTexts:
    cndsx3OperEntry.setStatus("mandatory")


class _Cndsx3OperLineIndex_Type(Integer32):
    """Custom type cndsx3OperLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cndsx3OperLineIndex_Type.__name__ = "Integer32"
_Cndsx3OperLineIndex_Object = MibTableColumn
cndsx3OperLineIndex = _Cndsx3OperLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 1),
    _Cndsx3OperLineIndex_Type()
)
cndsx3OperLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperLineIndex.setStatus("mandatory")


class _Cndsx3OperLineType_Type(Integer32):
    """Custom type cndsx3OperLineType based on Integer32"""
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
        *(("dsx3CbitParity", 4),
          ("dsx3ClearChannel", 5),
          ("dsx3M23", 2),
          ("dsx3SYNTRAN", 3),
          ("dsx3other", 1),
          ("e3Framed", 7),
          ("e3Plcp", 8),
          ("e3other", 6))
    )


_Cndsx3OperLineType_Type.__name__ = "Integer32"
_Cndsx3OperLineType_Object = MibTableColumn
cndsx3OperLineType = _Cndsx3OperLineType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 2),
    _Cndsx3OperLineType_Type()
)
cndsx3OperLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperLineType.setStatus("mandatory")


class _Cndsx3OperLoopbackConfig_Type(Integer32):
    """Custom type cndsx3OperLoopbackConfig based on Integer32"""
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
        *(("dsx3LineLoop", 3),
          ("dsx3NoLoop", 1),
          ("dsx3OtherLoop", 4),
          ("dsx3PayloadLoop", 2))
    )


_Cndsx3OperLoopbackConfig_Type.__name__ = "Integer32"
_Cndsx3OperLoopbackConfig_Object = MibTableColumn
cndsx3OperLoopbackConfig = _Cndsx3OperLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 3),
    _Cndsx3OperLoopbackConfig_Type()
)
cndsx3OperLoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperLoopbackConfig.setStatus("mandatory")


class _Cndsx3OperLineStatus_Type(Integer32):
    """Custom type cndsx3OperLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_Cndsx3OperLineStatus_Type.__name__ = "Integer32"
_Cndsx3OperLineStatus_Object = MibTableColumn
cndsx3OperLineStatus = _Cndsx3OperLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 4),
    _Cndsx3OperLineStatus_Type()
)
cndsx3OperLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperLineStatus.setStatus("mandatory")


class _Cndsx3OperTransmitClockSource_Type(Integer32):
    """Custom type cndsx3OperTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_Cndsx3OperTransmitClockSource_Type.__name__ = "Integer32"
_Cndsx3OperTransmitClockSource_Object = MibTableColumn
cndsx3OperTransmitClockSource = _Cndsx3OperTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 5),
    _Cndsx3OperTransmitClockSource_Type()
)
cndsx3OperTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperTransmitClockSource.setStatus("mandatory")


class _Cndsx3OperPlcpLOFEvent_Type(Integer32):
    """Custom type cndsx3OperPlcpLOFEvent based on Integer32"""
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


_Cndsx3OperPlcpLOFEvent_Type.__name__ = "Integer32"
_Cndsx3OperPlcpLOFEvent_Object = MibTableColumn
cndsx3OperPlcpLOFEvent = _Cndsx3OperPlcpLOFEvent_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 6),
    _Cndsx3OperPlcpLOFEvent_Type()
)
cndsx3OperPlcpLOFEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperPlcpLOFEvent.setStatus("mandatory")


class _Cndsx3OperG832CellDelineation_Type(Integer32):
    """Custom type cndsx3OperG832CellDelineation based on Integer32"""
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


_Cndsx3OperG832CellDelineation_Type.__name__ = "Integer32"
_Cndsx3OperG832CellDelineation_Object = MibTableColumn
cndsx3OperG832CellDelineation = _Cndsx3OperG832CellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 7),
    _Cndsx3OperG832CellDelineation_Type()
)
cndsx3OperG832CellDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperG832CellDelineation.setStatus("mandatory")
_Cndsx3OperLineBuildOut_Type = EnableIndicator
_Cndsx3OperLineBuildOut_Object = MibTableColumn
cndsx3OperLineBuildOut = _Cndsx3OperLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 8),
    _Cndsx3OperLineBuildOut_Type()
)
cndsx3OperLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperLineBuildOut.setStatus("mandatory")
_Cndsx3OperScramblingEnable_Type = EnableIndicator
_Cndsx3OperScramblingEnable_Object = MibTableColumn
cndsx3OperScramblingEnable = _Cndsx3OperScramblingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 9),
    _Cndsx3OperScramblingEnable_Type()
)
cndsx3OperScramblingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperScramblingEnable.setStatus("mandatory")


class _Cndsx3OperE3ConfigType_Type(Integer32):
    """Custom type cndsx3OperE3ConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g751", 2),
          ("g832", 3),
          ("other", 1))
    )


_Cndsx3OperE3ConfigType_Type.__name__ = "Integer32"
_Cndsx3OperE3ConfigType_Object = MibTableColumn
cndsx3OperE3ConfigType = _Cndsx3OperE3ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 10),
    _Cndsx3OperE3ConfigType_Type()
)
cndsx3OperE3ConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3OperE3ConfigType.setStatus("mandatory")
_Cndsx3TotalExt_ObjectIdentity = ObjectIdentity
cndsx3TotalExt = _Cndsx3TotalExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 2)
)
_Cndsx3TotalExtTable_Object = MibTable
cndsx3TotalExtTable = _Cndsx3TotalExtTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cndsx3TotalExtTable.setStatus("mandatory")
_Cndsx3TotalExtEntry_Object = MibTableRow
cndsx3TotalExtEntry = _Cndsx3TotalExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1, 1)
)
cndsx3TotalExtEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3TotalIndex"),
)
if mibBuilder.loadTexts:
    cndsx3TotalExtEntry.setStatus("mandatory")
_Cndsx3CellPayloadHECError_Type = Gauge32
_Cndsx3CellPayloadHECError_Object = MibTableColumn
cndsx3CellPayloadHECError = _Cndsx3CellPayloadHECError_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1, 1, 1),
    _Cndsx3CellPayloadHECError_Type()
)
cndsx3CellPayloadHECError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3CellPayloadHECError.setStatus("mandatory")
_Cndsx3ConfigExt_ObjectIdentity = ObjectIdentity
cndsx3ConfigExt = _Cndsx3ConfigExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3)
)
_Cndsx3ConfigExtTable_Object = MibTable
cndsx3ConfigExtTable = _Cndsx3ConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    cndsx3ConfigExtTable.setStatus("mandatory")
_Cndsx3ConfigExtEntry_Object = MibTableRow
cndsx3ConfigExtEntry = _Cndsx3ConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1)
)
cndsx3ConfigExtEntry.setIndexNames(
    (0, "RFC1407-EXT-MIB", "cndsx3LineIndex"),
)
if mibBuilder.loadTexts:
    cndsx3ConfigExtEntry.setStatus("mandatory")
_Cndsx3LineBuildOut_Type = EnableIndicator
_Cndsx3LineBuildOut_Object = MibTableColumn
cndsx3LineBuildOut = _Cndsx3LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 1),
    _Cndsx3LineBuildOut_Type()
)
cndsx3LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndsx3LineBuildOut.setStatus("mandatory")


class _Cndsx3LineIndex_Type(Integer32):
    """Custom type cndsx3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cndsx3LineIndex_Type.__name__ = "Integer32"
_Cndsx3LineIndex_Object = MibTableColumn
cndsx3LineIndex = _Cndsx3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 2),
    _Cndsx3LineIndex_Type()
)
cndsx3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndsx3LineIndex.setStatus("mandatory")
_Cndsx3ScramblingEnable_Type = EnableIndicator
_Cndsx3ScramblingEnable_Object = MibTableColumn
cndsx3ScramblingEnable = _Cndsx3ScramblingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 3),
    _Cndsx3ScramblingEnable_Type()
)
cndsx3ScramblingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndsx3ScramblingEnable.setStatus("mandatory")


class _Cndsx3E3ConfigType_Type(Integer32):
    """Custom type cndsx3E3ConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g751", 2),
          ("g832", 3),
          ("other", 1))
    )


_Cndsx3E3ConfigType_Type.__name__ = "Integer32"
_Cndsx3E3ConfigType_Object = MibTableColumn
cndsx3E3ConfigType = _Cndsx3E3ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 4),
    _Cndsx3E3ConfigType_Type()
)
cndsx3E3ConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndsx3E3ConfigType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1407-EXT-MIB",
    **{"cnds3e3Ext": cnds3e3Ext,
       "cndsx3Oper": cndsx3Oper,
       "cndsx3OperTable": cndsx3OperTable,
       "cndsx3OperEntry": cndsx3OperEntry,
       "cndsx3OperLineIndex": cndsx3OperLineIndex,
       "cndsx3OperLineType": cndsx3OperLineType,
       "cndsx3OperLoopbackConfig": cndsx3OperLoopbackConfig,
       "cndsx3OperLineStatus": cndsx3OperLineStatus,
       "cndsx3OperTransmitClockSource": cndsx3OperTransmitClockSource,
       "cndsx3OperPlcpLOFEvent": cndsx3OperPlcpLOFEvent,
       "cndsx3OperG832CellDelineation": cndsx3OperG832CellDelineation,
       "cndsx3OperLineBuildOut": cndsx3OperLineBuildOut,
       "cndsx3OperScramblingEnable": cndsx3OperScramblingEnable,
       "cndsx3OperE3ConfigType": cndsx3OperE3ConfigType,
       "cndsx3TotalExt": cndsx3TotalExt,
       "cndsx3TotalExtTable": cndsx3TotalExtTable,
       "cndsx3TotalExtEntry": cndsx3TotalExtEntry,
       "cndsx3CellPayloadHECError": cndsx3CellPayloadHECError,
       "cndsx3ConfigExt": cndsx3ConfigExt,
       "cndsx3ConfigExtTable": cndsx3ConfigExtTable,
       "cndsx3ConfigExtEntry": cndsx3ConfigExtEntry,
       "cndsx3LineBuildOut": cndsx3LineBuildOut,
       "cndsx3LineIndex": cndsx3LineIndex,
       "cndsx3ScramblingEnable": cndsx3ScramblingEnable,
       "cndsx3E3ConfigType": cndsx3E3ConfigType}
)
