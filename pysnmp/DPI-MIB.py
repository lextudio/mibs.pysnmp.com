# SNMP MIB module (DPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:19 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

fwdpi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51)
)
fwdpi.setRevisions(
        ("2008-11-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxrDPI_ObjectIdentity = ObjectIdentity
zxrDPI = _ZxrDPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1)
)
_DpiSystemControl_ObjectIdentity = ObjectIdentity
dpiSystemControl = _DpiSystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 1)
)


class _DpiSlotNumber_Type(Integer32):
    """Custom type dpiSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiSlotNumber_Type.__name__ = "Integer32"
_DpiSlotNumber_Object = MibScalar
dpiSlotNumber = _DpiSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 1, 1),
    _DpiSlotNumber_Type()
)
dpiSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSlotNumber.setStatus("current")


class _DpiRestartFunc_Type(Integer32):
    """Custom type dpiRestartFunc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiRestartFunc_Type.__name__ = "Integer32"
_DpiRestartFunc_Object = MibScalar
dpiRestartFunc = _DpiRestartFunc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 1, 2),
    _DpiRestartFunc_Type()
)
dpiRestartFunc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiRestartFunc.setStatus("current")
_DpiConfigMode_ObjectIdentity = ObjectIdentity
dpiConfigMode = _DpiConfigMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2)
)
_DpiBindMngServiceIp_ObjectIdentity = ObjectIdentity
dpiBindMngServiceIp = _DpiBindMngServiceIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 2)
)


class _DpiMngServerSlot_Type(Integer32):
    """Custom type dpiMngServerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiMngServerSlot_Type.__name__ = "Integer32"
_DpiMngServerSlot_Object = MibScalar
dpiMngServerSlot = _DpiMngServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 2, 1),
    _DpiMngServerSlot_Type()
)
dpiMngServerSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiMngServerSlot.setStatus("current")
_DpiMngIp_Type = IpAddress
_DpiMngIp_Object = MibScalar
dpiMngIp = _DpiMngIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 2, 2),
    _DpiMngIp_Type()
)
dpiMngIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiMngIp.setStatus("current")
_DpiServerIp_Type = IpAddress
_DpiServerIp_Object = MibScalar
dpiServerIp = _DpiServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 2, 3),
    _DpiServerIp_Type()
)
dpiServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiServerIp.setStatus("current")


class _DpiMngServerOK_Type(Integer32):
    """Custom type dpiMngServerOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiMngServerOK_Type.__name__ = "Integer32"
_DpiMngServerOK_Object = MibScalar
dpiMngServerOK = _DpiMngServerOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 2, 4),
    _DpiMngServerOK_Type()
)
dpiMngServerOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiMngServerOK.setStatus("current")
_DpiSignatureEntry_ObjectIdentity = ObjectIdentity
dpiSignatureEntry = _DpiSignatureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3)
)


class _DpiCurrentSignatureEntry_Type(Integer32):
    """Custom type dpiCurrentSignatureEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12287),
    )


_DpiCurrentSignatureEntry_Type.__name__ = "Integer32"
_DpiCurrentSignatureEntry_Object = MibScalar
dpiCurrentSignatureEntry = _DpiCurrentSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 1),
    _DpiCurrentSignatureEntry_Type()
)
dpiCurrentSignatureEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentSignatureEntry.setStatus("current")
_DpiShowSignatureEntry_ObjectIdentity = ObjectIdentity
dpiShowSignatureEntry = _DpiShowSignatureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 2)
)
_DpiSignatureEntryTable_Object = MibTable
dpiSignatureEntryTable = _DpiSignatureEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dpiSignatureEntryTable.setStatus("current")
_DpiSignatureTableEntry_Object = MibTableRow
dpiSignatureTableEntry = _DpiSignatureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 2, 1, 1)
)
dpiSignatureTableEntry.setIndexNames(
    (0, "DPI-MIB", "dpiSignatureEntryID"),
)
if mibBuilder.loadTexts:
    dpiSignatureTableEntry.setStatus("current")


class _DpiSignatureEntryID_Type(Integer32):
    """Custom type dpiSignatureEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12287),
    )


_DpiSignatureEntryID_Type.__name__ = "Integer32"
_DpiSignatureEntryID_Object = MibTableColumn
dpiSignatureEntryID = _DpiSignatureEntryID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 2, 1, 1, 1),
    _DpiSignatureEntryID_Type()
)
dpiSignatureEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSignatureEntryID.setStatus("current")
_DpiSignatureEntryContent_Type = DisplayString
_DpiSignatureEntryContent_Object = MibTableColumn
dpiSignatureEntryContent = _DpiSignatureEntryContent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 2, 1, 1, 2),
    _DpiSignatureEntryContent_Type()
)
dpiSignatureEntryContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSignatureEntryContent.setStatus("current")
_DpiSetContent_Type = DisplayString
_DpiSetContent_Object = MibScalar
dpiSetContent = _DpiSetContent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 3, 3),
    _DpiSetContent_Type()
)
dpiSetContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSetContent.setStatus("current")
_DpiSignatureSymbol_ObjectIdentity = ObjectIdentity
dpiSignatureSymbol = _DpiSignatureSymbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4)
)


class _DpiCurrentSignatureSymbol_Type(Integer32):
    """Custom type dpiCurrentSignatureSymbol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6143),
    )


_DpiCurrentSignatureSymbol_Type.__name__ = "Integer32"
_DpiCurrentSignatureSymbol_Object = MibScalar
dpiCurrentSignatureSymbol = _DpiCurrentSignatureSymbol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 1),
    _DpiCurrentSignatureSymbol_Type()
)
dpiCurrentSignatureSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentSignatureSymbol.setStatus("current")
_DpiShowSignatureSymbol_ObjectIdentity = ObjectIdentity
dpiShowSignatureSymbol = _DpiShowSignatureSymbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2)
)
_DpiSignatureSymbolTable_Object = MibTable
dpiSignatureSymbolTable = _DpiSignatureSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dpiSignatureSymbolTable.setStatus("current")
_DpiSignatureSymbolTableEntry_Object = MibTableRow
dpiSignatureSymbolTableEntry = _DpiSignatureSymbolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2, 1, 1)
)
dpiSignatureSymbolTableEntry.setIndexNames(
    (0, "DPI-MIB", "dpiSignatureSymbolID"),
)
if mibBuilder.loadTexts:
    dpiSignatureSymbolTableEntry.setStatus("current")


class _DpiSignatureSymbolID_Type(Integer32):
    """Custom type dpiSignatureSymbolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6143),
    )


_DpiSignatureSymbolID_Type.__name__ = "Integer32"
_DpiSignatureSymbolID_Object = MibTableColumn
dpiSignatureSymbolID = _DpiSignatureSymbolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2, 1, 1, 1),
    _DpiSignatureSymbolID_Type()
)
dpiSignatureSymbolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSignatureSymbolID.setStatus("current")
_DpiSignatureSymbolEntryID_Type = DisplayString
_DpiSignatureSymbolEntryID_Object = MibTableColumn
dpiSignatureSymbolEntryID = _DpiSignatureSymbolEntryID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2, 1, 1, 2),
    _DpiSignatureSymbolEntryID_Type()
)
dpiSignatureSymbolEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSignatureSymbolEntryID.setStatus("current")


class _DpiSignatureSymbolHitNumLimit_Type(Integer32):
    """Custom type dpiSignatureSymbolHitNumLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DpiSignatureSymbolHitNumLimit_Type.__name__ = "Integer32"
_DpiSignatureSymbolHitNumLimit_Object = MibTableColumn
dpiSignatureSymbolHitNumLimit = _DpiSignatureSymbolHitNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 2, 1, 1, 3),
    _DpiSignatureSymbolHitNumLimit_Type()
)
dpiSignatureSymbolHitNumLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSignatureSymbolHitNumLimit.setStatus("current")


class _DpiAddSignatureEntry_Type(Integer32):
    """Custom type dpiAddSignatureEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12287),
    )


_DpiAddSignatureEntry_Type.__name__ = "Integer32"
_DpiAddSignatureEntry_Object = MibScalar
dpiAddSignatureEntry = _DpiAddSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 3),
    _DpiAddSignatureEntry_Type()
)
dpiAddSignatureEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddSignatureEntry.setStatus("current")


class _DpiNoAddSignatureEntry_Type(Integer32):
    """Custom type dpiNoAddSignatureEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12287),
    )


_DpiNoAddSignatureEntry_Type.__name__ = "Integer32"
_DpiNoAddSignatureEntry_Object = MibScalar
dpiNoAddSignatureEntry = _DpiNoAddSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 4),
    _DpiNoAddSignatureEntry_Type()
)
dpiNoAddSignatureEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoAddSignatureEntry.setStatus("current")


class _DpiSetHitNumLimit_Type(Integer32):
    """Custom type dpiSetHitNumLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DpiSetHitNumLimit_Type.__name__ = "Integer32"
_DpiSetHitNumLimit_Object = MibScalar
dpiSetHitNumLimit = _DpiSetHitNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 4, 5),
    _DpiSetHitNumLimit_Type()
)
dpiSetHitNumLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSetHitNumLimit.setStatus("current")
_DpiFlowPool_ObjectIdentity = ObjectIdentity
dpiFlowPool = _DpiFlowPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5)
)


class _DpiCurrentFlowPool_Type(Integer32):
    """Custom type dpiCurrentFlowPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiCurrentFlowPool_Type.__name__ = "Integer32"
_DpiCurrentFlowPool_Object = MibScalar
dpiCurrentFlowPool = _DpiCurrentFlowPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 1),
    _DpiCurrentFlowPool_Type()
)
dpiCurrentFlowPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentFlowPool.setStatus("current")
_DpiShowFlowPool_ObjectIdentity = ObjectIdentity
dpiShowFlowPool = _DpiShowFlowPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2)
)
_DpiStreamLimitTable_Object = MibTable
dpiStreamLimitTable = _DpiStreamLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dpiStreamLimitTable.setStatus("current")
_DpiStreamLimitTableEntry_Object = MibTableRow
dpiStreamLimitTableEntry = _DpiStreamLimitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1)
)
dpiStreamLimitTableEntry.setIndexNames(
    (0, "DPI-MIB", "dpiStreamLimitID"),
    (0, "DPI-MIB", "dpiStreamLimitType"),
)
if mibBuilder.loadTexts:
    dpiStreamLimitTableEntry.setStatus("current")


class _DpiStreamLimitID_Type(Integer32):
    """Custom type dpiStreamLimitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiStreamLimitID_Type.__name__ = "Integer32"
_DpiStreamLimitID_Object = MibTableColumn
dpiStreamLimitID = _DpiStreamLimitID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1, 1),
    _DpiStreamLimitID_Type()
)
dpiStreamLimitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiStreamLimitID.setStatus("current")


class _DpiStreamLimitType_Type(Integer32):
    """Custom type dpiStreamLimitType based on Integer32"""
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


_DpiStreamLimitType_Type.__name__ = "Integer32"
_DpiStreamLimitType_Object = MibTableColumn
dpiStreamLimitType = _DpiStreamLimitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1, 2),
    _DpiStreamLimitType_Type()
)
dpiStreamLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiStreamLimitType.setStatus("current")


class _DpiStreamRate_Type(Integer32):
    """Custom type dpiStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_DpiStreamRate_Type.__name__ = "Integer32"
_DpiStreamRate_Object = MibTableColumn
dpiStreamRate = _DpiStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1, 3),
    _DpiStreamRate_Type()
)
dpiStreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiStreamRate.setStatus("current")
_DpiStreamCbs_Type = Integer32
_DpiStreamCbs_Object = MibTableColumn
dpiStreamCbs = _DpiStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1, 4),
    _DpiStreamCbs_Type()
)
dpiStreamCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiStreamCbs.setStatus("current")
_DpiStreamEbs_Type = Integer32
_DpiStreamEbs_Object = MibTableColumn
dpiStreamEbs = _DpiStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 2, 1, 1, 5),
    _DpiStreamEbs_Type()
)
dpiStreamEbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiStreamEbs.setStatus("current")
_DpiUpStreamRateLimit_ObjectIdentity = ObjectIdentity
dpiUpStreamRateLimit = _DpiUpStreamRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 3)
)


class _DpiUpStreamRate_Type(Integer32):
    """Custom type dpiUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_DpiUpStreamRate_Type.__name__ = "Integer32"
_DpiUpStreamRate_Object = MibScalar
dpiUpStreamRate = _DpiUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 3, 1),
    _DpiUpStreamRate_Type()
)
dpiUpStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpStreamRate.setStatus("current")
_DpiUpStreamCbs_Type = Integer32
_DpiUpStreamCbs_Object = MibScalar
dpiUpStreamCbs = _DpiUpStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 3, 2),
    _DpiUpStreamCbs_Type()
)
dpiUpStreamCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpStreamCbs.setStatus("current")
_DpiUpStreamEbs_Type = Integer32
_DpiUpStreamEbs_Object = MibScalar
dpiUpStreamEbs = _DpiUpStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 3, 3),
    _DpiUpStreamEbs_Type()
)
dpiUpStreamEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpStreamEbs.setStatus("current")


class _DpiUpStreamOK_Type(Integer32):
    """Custom type dpiUpStreamOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiUpStreamOK_Type.__name__ = "Integer32"
_DpiUpStreamOK_Object = MibScalar
dpiUpStreamOK = _DpiUpStreamOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 3, 4),
    _DpiUpStreamOK_Type()
)
dpiUpStreamOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpStreamOK.setStatus("current")


class _DpiNoUpStreamRateLimit_Type(Integer32):
    """Custom type dpiNoUpStreamRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiNoUpStreamRateLimit_Type.__name__ = "Integer32"
_DpiNoUpStreamRateLimit_Object = MibScalar
dpiNoUpStreamRateLimit = _DpiNoUpStreamRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 4),
    _DpiNoUpStreamRateLimit_Type()
)
dpiNoUpStreamRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoUpStreamRateLimit.setStatus("current")
_DpiDownStreamRateLimit_ObjectIdentity = ObjectIdentity
dpiDownStreamRateLimit = _DpiDownStreamRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 5)
)


class _DpiDownStreamRate_Type(Integer32):
    """Custom type dpiDownStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_DpiDownStreamRate_Type.__name__ = "Integer32"
_DpiDownStreamRate_Object = MibScalar
dpiDownStreamRate = _DpiDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 5, 1),
    _DpiDownStreamRate_Type()
)
dpiDownStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiDownStreamRate.setStatus("current")
_DpiDownStreamCbs_Type = Integer32
_DpiDownStreamCbs_Object = MibScalar
dpiDownStreamCbs = _DpiDownStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 5, 2),
    _DpiDownStreamCbs_Type()
)
dpiDownStreamCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiDownStreamCbs.setStatus("current")
_DpiDownStreamEbs_Type = Integer32
_DpiDownStreamEbs_Object = MibScalar
dpiDownStreamEbs = _DpiDownStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 5, 3),
    _DpiDownStreamEbs_Type()
)
dpiDownStreamEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiDownStreamEbs.setStatus("current")


class _DpiDownStreamOK_Type(Integer32):
    """Custom type dpiDownStreamOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiDownStreamOK_Type.__name__ = "Integer32"
_DpiDownStreamOK_Object = MibScalar
dpiDownStreamOK = _DpiDownStreamOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 5, 4),
    _DpiDownStreamOK_Type()
)
dpiDownStreamOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiDownStreamOK.setStatus("current")


class _DpiNoDownStreamRateLimit_Type(Integer32):
    """Custom type dpiNoDownStreamRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiNoDownStreamRateLimit_Type.__name__ = "Integer32"
_DpiNoDownStreamRateLimit_Object = MibScalar
dpiNoDownStreamRateLimit = _DpiNoDownStreamRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 5, 6),
    _DpiNoDownStreamRateLimit_Type()
)
dpiNoDownStreamRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoDownStreamRateLimit.setStatus("current")
_DpiSubservice_ObjectIdentity = ObjectIdentity
dpiSubservice = _DpiSubservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6)
)


class _DpiCurrentSubservice_Type(Integer32):
    """Custom type dpiCurrentSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiCurrentSubservice_Type.__name__ = "Integer32"
_DpiCurrentSubservice_Object = MibScalar
dpiCurrentSubservice = _DpiCurrentSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 1),
    _DpiCurrentSubservice_Type()
)
dpiCurrentSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentSubservice.setStatus("current")
_DpiShowSubservice_ObjectIdentity = ObjectIdentity
dpiShowSubservice = _DpiShowSubservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2)
)
_DpiSubserviceTable_Object = MibTable
dpiSubserviceTable = _DpiSubserviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    dpiSubserviceTable.setStatus("current")
_DpiSubserviceEntry_Object = MibTableRow
dpiSubserviceEntry = _DpiSubserviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1)
)
dpiSubserviceEntry.setIndexNames(
    (0, "DPI-MIB", "dpiSubserviceID"),
)
if mibBuilder.loadTexts:
    dpiSubserviceEntry.setStatus("current")


class _DpiSubserviceID_Type(Integer32):
    """Custom type dpiSubserviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiSubserviceID_Type.__name__ = "Integer32"
_DpiSubserviceID_Object = MibTableColumn
dpiSubserviceID = _DpiSubserviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 1),
    _DpiSubserviceID_Type()
)
dpiSubserviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceID.setStatus("current")


class _DpiSubserviceSymbolNum_Type(Integer32):
    """Custom type dpiSubserviceSymbolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6143),
    )


_DpiSubserviceSymbolNum_Type.__name__ = "Integer32"
_DpiSubserviceSymbolNum_Object = MibTableColumn
dpiSubserviceSymbolNum = _DpiSubserviceSymbolNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 2),
    _DpiSubserviceSymbolNum_Type()
)
dpiSubserviceSymbolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceSymbolNum.setStatus("current")


class _DpiSubserviceFlowpoolID_Type(Integer32):
    """Custom type dpiSubserviceFlowpoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiSubserviceFlowpoolID_Type.__name__ = "Integer32"
_DpiSubserviceFlowpoolID_Object = MibTableColumn
dpiSubserviceFlowpoolID = _DpiSubserviceFlowpoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 3),
    _DpiSubserviceFlowpoolID_Type()
)
dpiSubserviceFlowpoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceFlowpoolID.setStatus("current")


class _DpiSubserviceAction_Type(Integer32):
    """Custom type dpiSubserviceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_DpiSubserviceAction_Type.__name__ = "Integer32"
_DpiSubserviceAction_Object = MibTableColumn
dpiSubserviceAction = _DpiSubserviceAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 4),
    _DpiSubserviceAction_Type()
)
dpiSubserviceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceAction.setStatus("current")


class _DpiSubserviceAgingTime_Type(Integer32):
    """Custom type dpiSubserviceAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DpiSubserviceAgingTime_Type.__name__ = "Integer32"
_DpiSubserviceAgingTime_Object = MibTableColumn
dpiSubserviceAgingTime = _DpiSubserviceAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 5),
    _DpiSubserviceAgingTime_Type()
)
dpiSubserviceAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceAgingTime.setStatus("current")
_DpiSubserviceSymbolList_Type = DisplayString
_DpiSubserviceSymbolList_Object = MibTableColumn
dpiSubserviceSymbolList = _DpiSubserviceSymbolList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 2, 1, 1, 6),
    _DpiSubserviceSymbolList_Type()
)
dpiSubserviceSymbolList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiSubserviceSymbolList.setStatus("current")
_DpiAddSignatureSymbol_ObjectIdentity = ObjectIdentity
dpiAddSignatureSymbol = _DpiAddSignatureSymbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 3)
)
_DpiAddSignatureSymbolId_Type = DisplayString
_DpiAddSignatureSymbolId_Object = MibScalar
dpiAddSignatureSymbolId = _DpiAddSignatureSymbolId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 3, 1),
    _DpiAddSignatureSymbolId_Type()
)
dpiAddSignatureSymbolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddSignatureSymbolId.setStatus("current")
_DpiAddSignatureSymbolRelationName_Type = DisplayString
_DpiAddSignatureSymbolRelationName_Object = MibScalar
dpiAddSignatureSymbolRelationName = _DpiAddSignatureSymbolRelationName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 3, 2),
    _DpiAddSignatureSymbolRelationName_Type()
)
dpiAddSignatureSymbolRelationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddSignatureSymbolRelationName.setStatus("current")


class _DpiAddSignatureSymbolOK_Type(Integer32):
    """Custom type dpiAddSignatureSymbolOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiAddSignatureSymbolOK_Type.__name__ = "Integer32"
_DpiAddSignatureSymbolOK_Object = MibScalar
dpiAddSignatureSymbolOK = _DpiAddSignatureSymbolOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 3, 3),
    _DpiAddSignatureSymbolOK_Type()
)
dpiAddSignatureSymbolOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddSignatureSymbolOK.setStatus("current")
_DpiNoAddSignatureSymbol_Type = DisplayString
_DpiNoAddSignatureSymbol_Object = MibScalar
dpiNoAddSignatureSymbol = _DpiNoAddSignatureSymbol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 4),
    _DpiNoAddSignatureSymbol_Type()
)
dpiNoAddSignatureSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoAddSignatureSymbol.setStatus("current")
_DpiAddProtocol_Type = DisplayString
_DpiAddProtocol_Object = MibScalar
dpiAddProtocol = _DpiAddProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 5),
    _DpiAddProtocol_Type()
)
dpiAddProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddProtocol.setStatus("current")
_DpiNoAddProtocol_Type = DisplayString
_DpiNoAddProtocol_Object = MibScalar
dpiNoAddProtocol = _DpiNoAddProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 6),
    _DpiNoAddProtocol_Type()
)
dpiNoAddProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoAddProtocol.setStatus("current")


class _DpiBindFlowPool_Type(Integer32):
    """Custom type dpiBindFlowPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiBindFlowPool_Type.__name__ = "Integer32"
_DpiBindFlowPool_Object = MibScalar
dpiBindFlowPool = _DpiBindFlowPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 7),
    _DpiBindFlowPool_Type()
)
dpiBindFlowPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindFlowPool.setStatus("current")


class _DpiNoBindFlowPool_Type(Integer32):
    """Custom type dpiNoBindFlowPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiNoBindFlowPool_Type.__name__ = "Integer32"
_DpiNoBindFlowPool_Object = MibScalar
dpiNoBindFlowPool = _DpiNoBindFlowPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 8),
    _DpiNoBindFlowPool_Type()
)
dpiNoBindFlowPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoBindFlowPool.setStatus("current")


class _DpiSetAction_Type(Integer32):
    """Custom type dpiSetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_DpiSetAction_Type.__name__ = "Integer32"
_DpiSetAction_Object = MibScalar
dpiSetAction = _DpiSetAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 9),
    _DpiSetAction_Type()
)
dpiSetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSetAction.setStatus("current")


class _DpiSetAgingTime_Type(Integer32):
    """Custom type dpiSetAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DpiSetAgingTime_Type.__name__ = "Integer32"
_DpiSetAgingTime_Object = MibScalar
dpiSetAgingTime = _DpiSetAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 6, 10),
    _DpiSetAgingTime_Type()
)
dpiSetAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSetAgingTime.setStatus("current")
_DpiService_ObjectIdentity = ObjectIdentity
dpiService = _DpiService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7)
)


class _DpiCurrentService_Type(Integer32):
    """Custom type dpiCurrentService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiCurrentService_Type.__name__ = "Integer32"
_DpiCurrentService_Object = MibScalar
dpiCurrentService = _DpiCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 1),
    _DpiCurrentService_Type()
)
dpiCurrentService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentService.setStatus("current")
_DpiShowService_ObjectIdentity = ObjectIdentity
dpiShowService = _DpiShowService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2)
)
_DpiServiceTable_Object = MibTable
dpiServiceTable = _DpiServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    dpiServiceTable.setStatus("current")
_DpiServiceEntry_Object = MibTableRow
dpiServiceEntry = _DpiServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1)
)
dpiServiceEntry.setIndexNames(
    (0, "DPI-MIB", "dpiServiceID"),
)
if mibBuilder.loadTexts:
    dpiServiceEntry.setStatus("current")


class _DpiServiceID_Type(Integer32):
    """Custom type dpiServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiServiceID_Type.__name__ = "Integer32"
_DpiServiceID_Object = MibTableColumn
dpiServiceID = _DpiServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1, 1),
    _DpiServiceID_Type()
)
dpiServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiServiceID.setStatus("current")


class _DpiServiceFlowPoolID_Type(Integer32):
    """Custom type dpiServiceFlowPoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiServiceFlowPoolID_Type.__name__ = "Integer32"
_DpiServiceFlowPoolID_Object = MibTableColumn
dpiServiceFlowPoolID = _DpiServiceFlowPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1, 2),
    _DpiServiceFlowPoolID_Type()
)
dpiServiceFlowPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiServiceFlowPoolID.setStatus("current")


class _DpiServiceConnectionLimit_Type(Integer32):
    """Custom type dpiServiceConnectionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310719),
    )


_DpiServiceConnectionLimit_Type.__name__ = "Integer32"
_DpiServiceConnectionLimit_Object = MibTableColumn
dpiServiceConnectionLimit = _DpiServiceConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1, 3),
    _DpiServiceConnectionLimit_Type()
)
dpiServiceConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiServiceConnectionLimit.setStatus("current")


class _DpiServiceSubserviceNum_Type(Integer32):
    """Custom type dpiServiceSubserviceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiServiceSubserviceNum_Type.__name__ = "Integer32"
_DpiServiceSubserviceNum_Object = MibTableColumn
dpiServiceSubserviceNum = _DpiServiceSubserviceNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1, 4),
    _DpiServiceSubserviceNum_Type()
)
dpiServiceSubserviceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiServiceSubserviceNum.setStatus("current")
_DpiServiceSubserviceList_Type = DisplayString
_DpiServiceSubserviceList_Object = MibTableColumn
dpiServiceSubserviceList = _DpiServiceSubserviceList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 2, 1, 1, 5),
    _DpiServiceSubserviceList_Type()
)
dpiServiceSubserviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiServiceSubserviceList.setStatus("current")


class _DpiAddSubservice_Type(Integer32):
    """Custom type dpiAddSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiAddSubservice_Type.__name__ = "Integer32"
_DpiAddSubservice_Object = MibScalar
dpiAddSubservice = _DpiAddSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 3),
    _DpiAddSubservice_Type()
)
dpiAddSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiAddSubservice.setStatus("current")


class _DpiNoAddSubservice_Type(Integer32):
    """Custom type dpiNoAddSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiNoAddSubservice_Type.__name__ = "Integer32"
_DpiNoAddSubservice_Object = MibScalar
dpiNoAddSubservice = _DpiNoAddSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 4),
    _DpiNoAddSubservice_Type()
)
dpiNoAddSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoAddSubservice.setStatus("current")
_DpiImportSubservice_ObjectIdentity = ObjectIdentity
dpiImportSubservice = _DpiImportSubservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 5)
)


class _DpiImportDestSubservice_Type(Integer32):
    """Custom type dpiImportDestSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiImportDestSubservice_Type.__name__ = "Integer32"
_DpiImportDestSubservice_Object = MibScalar
dpiImportDestSubservice = _DpiImportDestSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 5, 1),
    _DpiImportDestSubservice_Type()
)
dpiImportDestSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiImportDestSubservice.setStatus("current")


class _DpiImportSrcSubservice_Type(Integer32):
    """Custom type dpiImportSrcSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiImportSrcSubservice_Type.__name__ = "Integer32"
_DpiImportSrcSubservice_Object = MibScalar
dpiImportSrcSubservice = _DpiImportSrcSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 5, 2),
    _DpiImportSrcSubservice_Type()
)
dpiImportSrcSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiImportSrcSubservice.setStatus("current")


class _DpiImportSubserviceOK_Type(Integer32):
    """Custom type dpiImportSubserviceOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiImportSubserviceOK_Type.__name__ = "Integer32"
_DpiImportSubserviceOK_Object = MibScalar
dpiImportSubserviceOK = _DpiImportSubserviceOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 5, 3),
    _DpiImportSubserviceOK_Type()
)
dpiImportSubserviceOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiImportSubserviceOK.setStatus("current")


class _DpiNoImportSubservice_Type(Integer32):
    """Custom type dpiNoImportSubservice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiNoImportSubservice_Type.__name__ = "Integer32"
_DpiNoImportSubservice_Object = MibScalar
dpiNoImportSubservice = _DpiNoImportSubservice_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 5, 4),
    _DpiNoImportSubservice_Type()
)
dpiNoImportSubservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoImportSubservice.setStatus("current")


class _DpiServiceBindFlowPool_Type(Integer32):
    """Custom type dpiServiceBindFlowPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiServiceBindFlowPool_Type.__name__ = "Integer32"
_DpiServiceBindFlowPool_Object = MibScalar
dpiServiceBindFlowPool = _DpiServiceBindFlowPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 6),
    _DpiServiceBindFlowPool_Type()
)
dpiServiceBindFlowPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiServiceBindFlowPool.setStatus("current")


class _DpiServiceNoBindFlowPool_Type(Integer32):
    """Custom type dpiServiceNoBindFlowPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiServiceNoBindFlowPool_Type.__name__ = "Integer32"
_DpiServiceNoBindFlowPool_Object = MibScalar
dpiServiceNoBindFlowPool = _DpiServiceNoBindFlowPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 7, 7),
    _DpiServiceNoBindFlowPool_Type()
)
dpiServiceNoBindFlowPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiServiceNoBindFlowPool.setStatus("current")
_DpiTemplate_ObjectIdentity = ObjectIdentity
dpiTemplate = _DpiTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8)
)


class _DpiCurrentTemplate_Type(Integer32):
    """Custom type dpiCurrentTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DpiCurrentTemplate_Type.__name__ = "Integer32"
_DpiCurrentTemplate_Object = MibScalar
dpiCurrentTemplate = _DpiCurrentTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 1),
    _DpiCurrentTemplate_Type()
)
dpiCurrentTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCurrentTemplate.setStatus("current")


class _DpiBindSlot_Type(Integer32):
    """Custom type dpiBindSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiBindSlot_Type.__name__ = "Integer32"
_DpiBindSlot_Object = MibScalar
dpiBindSlot = _DpiBindSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 2),
    _DpiBindSlot_Type()
)
dpiBindSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindSlot.setStatus("current")


class _DpiNoBindSlot_Type(Integer32):
    """Custom type dpiNoBindSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiNoBindSlot_Type.__name__ = "Integer32"
_DpiNoBindSlot_Object = MibScalar
dpiNoBindSlot = _DpiNoBindSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 3),
    _DpiNoBindSlot_Type()
)
dpiNoBindSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoBindSlot.setStatus("current")


class _DpiBindService_Type(Integer32):
    """Custom type dpiBindService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiBindService_Type.__name__ = "Integer32"
_DpiBindService_Object = MibScalar
dpiBindService = _DpiBindService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 4),
    _DpiBindService_Type()
)
dpiBindService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindService.setStatus("current")


class _DpiNoBindService_Type(Integer32):
    """Custom type dpiNoBindService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiNoBindService_Type.__name__ = "Integer32"
_DpiNoBindService_Object = MibScalar
dpiNoBindService = _DpiNoBindService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 5),
    _DpiNoBindService_Type()
)
dpiNoBindService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoBindService.setStatus("current")
_DpiBindSipAddr_ObjectIdentity = ObjectIdentity
dpiBindSipAddr = _DpiBindSipAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6)
)
_DpiSipAddress_Type = IpAddress
_DpiSipAddress_Object = MibScalar
dpiSipAddress = _DpiSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 1),
    _DpiSipAddress_Type()
)
dpiSipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSipAddress.setStatus("current")
_DpiSipMask_Type = IpAddress
_DpiSipMask_Object = MibScalar
dpiSipMask = _DpiSipMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 2),
    _DpiSipMask_Type()
)
dpiSipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSipMask.setStatus("current")


class _DpiSipServiceID_Type(Integer32):
    """Custom type dpiSipServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiSipServiceID_Type.__name__ = "Integer32"
_DpiSipServiceID_Object = MibScalar
dpiSipServiceID = _DpiSipServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 3),
    _DpiSipServiceID_Type()
)
dpiSipServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSipServiceID.setStatus("current")


class _DpiBindSipAddrOK_Type(Integer32):
    """Custom type dpiBindSipAddrOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiBindSipAddrOK_Type.__name__ = "Integer32"
_DpiBindSipAddrOK_Object = MibScalar
dpiBindSipAddrOK = _DpiBindSipAddrOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 4),
    _DpiBindSipAddrOK_Type()
)
dpiBindSipAddrOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindSipAddrOK.setStatus("current")


class _DpiNoBindSipAddr_Type(Integer32):
    """Custom type dpiNoBindSipAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiNoBindSipAddr_Type.__name__ = "Integer32"
_DpiNoBindSipAddr_Object = MibScalar
dpiNoBindSipAddr = _DpiNoBindSipAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 5),
    _DpiNoBindSipAddr_Type()
)
dpiNoBindSipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoBindSipAddr.setStatus("current")


class _DpiShowIpService_Type(Integer32):
    """Custom type dpiShowIpService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiShowIpService_Type.__name__ = "Integer32"
_DpiShowIpService_Object = MibScalar
dpiShowIpService = _DpiShowIpService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 6, 6),
    _DpiShowIpService_Type()
)
dpiShowIpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiShowIpService.setStatus("current")
_DpiBindSwitchport_ObjectIdentity = ObjectIdentity
dpiBindSwitchport = _DpiBindSwitchport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7)
)
_DpiBindSwitchportPort_Type = DisplayString
_DpiBindSwitchportPort_Object = MibScalar
dpiBindSwitchportPort = _DpiBindSwitchportPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7, 2),
    _DpiBindSwitchportPort_Type()
)
dpiBindSwitchportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindSwitchportPort.setStatus("current")


class _DpiBindSwitchService_Type(Integer32):
    """Custom type dpiBindSwitchService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiBindSwitchService_Type.__name__ = "Integer32"
_DpiBindSwitchService_Object = MibScalar
dpiBindSwitchService = _DpiBindSwitchService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7, 3),
    _DpiBindSwitchService_Type()
)
dpiBindSwitchService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindSwitchService.setStatus("current")


class _DpiBindSwitchportOK_Type(Integer32):
    """Custom type dpiBindSwitchportOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiBindSwitchportOK_Type.__name__ = "Integer32"
_DpiBindSwitchportOK_Object = MibScalar
dpiBindSwitchportOK = _DpiBindSwitchportOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7, 4),
    _DpiBindSwitchportOK_Type()
)
dpiBindSwitchportOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindSwitchportOK.setStatus("current")


class _DpiNoBindSwitchport_Type(Integer32):
    """Custom type dpiNoBindSwitchport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiNoBindSwitchport_Type.__name__ = "Integer32"
_DpiNoBindSwitchport_Object = MibScalar
dpiNoBindSwitchport = _DpiNoBindSwitchport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7, 5),
    _DpiNoBindSwitchport_Type()
)
dpiNoBindSwitchport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiNoBindSwitchport.setStatus("current")


class _DpiShowPortService_Type(Integer32):
    """Custom type dpiShowPortService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiShowPortService_Type.__name__ = "Integer32"
_DpiShowPortService_Object = MibScalar
dpiShowPortService = _DpiShowPortService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 8, 7, 6),
    _DpiShowPortService_Type()
)
dpiShowPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiShowPortService.setStatus("current")


class _DpiSetActiceConnectionSaveInterval_Type(Integer32):
    """Custom type dpiSetActiceConnectionSaveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DpiSetActiceConnectionSaveInterval_Type.__name__ = "Integer32"
_DpiSetActiceConnectionSaveInterval_Object = MibScalar
dpiSetActiceConnectionSaveInterval = _DpiSetActiceConnectionSaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 9),
    _DpiSetActiceConnectionSaveInterval_Type()
)
dpiSetActiceConnectionSaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiSetActiceConnectionSaveInterval.setStatus("current")


class _DpiClearConnectionAll_Type(Integer32):
    """Custom type dpiClearConnectionAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiClearConnectionAll_Type.__name__ = "Integer32"
_DpiClearConnectionAll_Object = MibScalar
dpiClearConnectionAll = _DpiClearConnectionAll_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 2, 10),
    _DpiClearConnectionAll_Type()
)
dpiClearConnectionAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiClearConnectionAll.setStatus("current")
_DpiMonitorLog_ObjectIdentity = ObjectIdentity
dpiMonitorLog = _DpiMonitorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3)
)
_DpiUploadAuto_ObjectIdentity = ObjectIdentity
dpiUploadAuto = _DpiUploadAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 1)
)


class _DpiUploadAutoSlot_Type(Integer32):
    """Custom type dpiUploadAutoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiUploadAutoSlot_Type.__name__ = "Integer32"
_DpiUploadAutoSlot_Object = MibScalar
dpiUploadAutoSlot = _DpiUploadAutoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 1, 1),
    _DpiUploadAutoSlot_Type()
)
dpiUploadAutoSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadAutoSlot.setStatus("current")


class _DpiUploadAutoEnable_Type(Integer32):
    """Custom type dpiUploadAutoEnable based on Integer32"""
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


_DpiUploadAutoEnable_Type.__name__ = "Integer32"
_DpiUploadAutoEnable_Object = MibScalar
dpiUploadAutoEnable = _DpiUploadAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 1, 2),
    _DpiUploadAutoEnable_Type()
)
dpiUploadAutoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadAutoEnable.setStatus("current")


class _DpiUploadAutoOK_Type(Integer32):
    """Custom type dpiUploadAutoOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiUploadAutoOK_Type.__name__ = "Integer32"
_DpiUploadAutoOK_Object = MibScalar
dpiUploadAutoOK = _DpiUploadAutoOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 1, 3),
    _DpiUploadAutoOK_Type()
)
dpiUploadAutoOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadAutoOK.setStatus("current")
_DpiUploadInterval_ObjectIdentity = ObjectIdentity
dpiUploadInterval = _DpiUploadInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 2)
)


class _DpiUploadIntervalSlot_Type(Integer32):
    """Custom type dpiUploadIntervalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiUploadIntervalSlot_Type.__name__ = "Integer32"
_DpiUploadIntervalSlot_Object = MibScalar
dpiUploadIntervalSlot = _DpiUploadIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 2, 1),
    _DpiUploadIntervalSlot_Type()
)
dpiUploadIntervalSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadIntervalSlot.setStatus("current")


class _DpiUploadTimeInterval_Type(Integer32):
    """Custom type dpiUploadTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_DpiUploadTimeInterval_Type.__name__ = "Integer32"
_DpiUploadTimeInterval_Object = MibScalar
dpiUploadTimeInterval = _DpiUploadTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 2, 2),
    _DpiUploadTimeInterval_Type()
)
dpiUploadTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadTimeInterval.setStatus("current")


class _DpiUploadIntervalOK_Type(Integer32):
    """Custom type dpiUploadIntervalOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiUploadIntervalOK_Type.__name__ = "Integer32"
_DpiUploadIntervalOK_Object = MibScalar
dpiUploadIntervalOK = _DpiUploadIntervalOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 2, 3),
    _DpiUploadIntervalOK_Type()
)
dpiUploadIntervalOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadIntervalOK.setStatus("current")
_DpiLogFileListDir_ObjectIdentity = ObjectIdentity
dpiLogFileListDir = _DpiLogFileListDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 3)
)


class _DpiLogFileListDirSlot_Type(Integer32):
    """Custom type dpiLogFileListDirSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiLogFileListDirSlot_Type.__name__ = "Integer32"
_DpiLogFileListDirSlot_Object = MibScalar
dpiLogFileListDirSlot = _DpiLogFileListDirSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 3, 1),
    _DpiLogFileListDirSlot_Type()
)
dpiLogFileListDirSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileListDirSlot.setStatus("current")
_DpiLogFileListDirFtpFile_Type = DisplayString
_DpiLogFileListDirFtpFile_Object = MibScalar
dpiLogFileListDirFtpFile = _DpiLogFileListDirFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 3, 2),
    _DpiLogFileListDirFtpFile_Type()
)
dpiLogFileListDirFtpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileListDirFtpFile.setStatus("current")
_DpiLogFileListDirLocalDir_Type = DisplayString
_DpiLogFileListDirLocalDir_Object = MibScalar
dpiLogFileListDirLocalDir = _DpiLogFileListDirLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 3, 3),
    _DpiLogFileListDirLocalDir_Type()
)
dpiLogFileListDirLocalDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileListDirLocalDir.setStatus("current")


class _DpiLogFileListDirOK_Type(Integer32):
    """Custom type dpiLogFileListDirOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiLogFileListDirOK_Type.__name__ = "Integer32"
_DpiLogFileListDirOK_Object = MibScalar
dpiLogFileListDirOK = _DpiLogFileListDirOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 3, 4),
    _DpiLogFileListDirOK_Type()
)
dpiLogFileListDirOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileListDirOK.setStatus("current")
_DpiLogFileDeleteDir_ObjectIdentity = ObjectIdentity
dpiLogFileDeleteDir = _DpiLogFileDeleteDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 4)
)


class _DpiLogFileDeleteDirSlot_Type(Integer32):
    """Custom type dpiLogFileDeleteDirSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiLogFileDeleteDirSlot_Type.__name__ = "Integer32"
_DpiLogFileDeleteDirSlot_Object = MibScalar
dpiLogFileDeleteDirSlot = _DpiLogFileDeleteDirSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 4, 1),
    _DpiLogFileDeleteDirSlot_Type()
)
dpiLogFileDeleteDirSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteDirSlot.setStatus("current")
_DpiLogFileDeleteDirName_Type = DisplayString
_DpiLogFileDeleteDirName_Object = MibScalar
dpiLogFileDeleteDirName = _DpiLogFileDeleteDirName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 4, 2),
    _DpiLogFileDeleteDirName_Type()
)
dpiLogFileDeleteDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteDirName.setStatus("current")


class _DpiLogFileDeleteDirOK_Type(Integer32):
    """Custom type dpiLogFileDeleteDirOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiLogFileDeleteDirOK_Type.__name__ = "Integer32"
_DpiLogFileDeleteDirOK_Object = MibScalar
dpiLogFileDeleteDirOK = _DpiLogFileDeleteDirOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 4, 3),
    _DpiLogFileDeleteDirOK_Type()
)
dpiLogFileDeleteDirOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteDirOK.setStatus("current")
_DpiLogFileDeleteFile_ObjectIdentity = ObjectIdentity
dpiLogFileDeleteFile = _DpiLogFileDeleteFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 5)
)


class _DpiLogFileDeleteFileSlot_Type(Integer32):
    """Custom type dpiLogFileDeleteFileSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiLogFileDeleteFileSlot_Type.__name__ = "Integer32"
_DpiLogFileDeleteFileSlot_Object = MibScalar
dpiLogFileDeleteFileSlot = _DpiLogFileDeleteFileSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 5, 1),
    _DpiLogFileDeleteFileSlot_Type()
)
dpiLogFileDeleteFileSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteFileSlot.setStatus("current")
_DpiLogFileDeleteFileName_Type = DisplayString
_DpiLogFileDeleteFileName_Object = MibScalar
dpiLogFileDeleteFileName = _DpiLogFileDeleteFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 5, 2),
    _DpiLogFileDeleteFileName_Type()
)
dpiLogFileDeleteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteFileName.setStatus("current")


class _DpiLogFileDeleteFileOK_Type(Integer32):
    """Custom type dpiLogFileDeleteFileOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiLogFileDeleteFileOK_Type.__name__ = "Integer32"
_DpiLogFileDeleteFileOK_Object = MibScalar
dpiLogFileDeleteFileOK = _DpiLogFileDeleteFileOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 5, 3),
    _DpiLogFileDeleteFileOK_Type()
)
dpiLogFileDeleteFileOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogFileDeleteFileOK.setStatus("current")
_DpiUpdateDpiLog_ObjectIdentity = ObjectIdentity
dpiUpdateDpiLog = _DpiUpdateDpiLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 6)
)


class _DpiUpdateDpiLogSlot_Type(Integer32):
    """Custom type dpiUpdateDpiLogSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiUpdateDpiLogSlot_Type.__name__ = "Integer32"
_DpiUpdateDpiLogSlot_Object = MibScalar
dpiUpdateDpiLogSlot = _DpiUpdateDpiLogSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 6, 1),
    _DpiUpdateDpiLogSlot_Type()
)
dpiUpdateDpiLogSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpdateDpiLogSlot.setStatus("current")
_DpiLogServerFileName_Type = DisplayString
_DpiLogServerFileName_Object = MibScalar
dpiLogServerFileName = _DpiLogServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 6, 3),
    _DpiLogServerFileName_Type()
)
dpiLogServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogServerFileName.setStatus("current")
_DpiLogLocalFileName_Type = DisplayString
_DpiLogLocalFileName_Object = MibScalar
dpiLogLocalFileName = _DpiLogLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 6, 5),
    _DpiLogLocalFileName_Type()
)
dpiLogLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogLocalFileName.setStatus("current")


class _DpiUpdateDpiLogOK_Type(Integer32):
    """Custom type dpiUpdateDpiLogOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiUpdateDpiLogOK_Type.__name__ = "Integer32"
_DpiUpdateDpiLogOK_Object = MibScalar
dpiUpdateDpiLogOK = _DpiUpdateDpiLogOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 6, 6),
    _DpiUpdateDpiLogOK_Type()
)
dpiUpdateDpiLogOK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpdateDpiLogOK.setStatus("current")


class _DpiUploadTodayLog_Type(Integer32):
    """Custom type dpiUploadTodayLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiUploadTodayLog_Type.__name__ = "Integer32"
_DpiUploadTodayLog_Object = MibScalar
dpiUploadTodayLog = _DpiUploadTodayLog_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 3, 7),
    _DpiUploadTodayLog_Type()
)
dpiUploadTodayLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUploadTodayLog.setStatus("current")


class _DpiCommit_Type(Integer32):
    """Custom type dpiCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiCommit_Type.__name__ = "Integer32"
_DpiCommit_Object = MibScalar
dpiCommit = _DpiCommit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 4),
    _DpiCommit_Type()
)
dpiCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiCommit.setStatus("current")


class _DpiUpdateSignatureVersion_Type(Integer32):
    """Custom type dpiUpdateSignatureVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_DpiUpdateSignatureVersion_Type.__name__ = "Integer32"
_DpiUpdateSignatureVersion_Object = MibScalar
dpiUpdateSignatureVersion = _DpiUpdateSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 5),
    _DpiUpdateSignatureVersion_Type()
)
dpiUpdateSignatureVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiUpdateSignatureVersion.setStatus("current")
_DpiVlanBindDpiTemplate_ObjectIdentity = ObjectIdentity
dpiVlanBindDpiTemplate = _DpiVlanBindDpiTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 6)
)
_DpiVlanInterfaceName_Type = DisplayString
_DpiVlanInterfaceName_Object = MibScalar
dpiVlanInterfaceName = _DpiVlanInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 6, 1),
    _DpiVlanInterfaceName_Type()
)
dpiVlanInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiVlanInterfaceName.setStatus("current")


class _DpiBindDpiTemplate_Type(Integer32):
    """Custom type dpiBindDpiTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DpiBindDpiTemplate_Type.__name__ = "Integer32"
_DpiBindDpiTemplate_Object = MibScalar
dpiBindDpiTemplate = _DpiBindDpiTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 6, 2),
    _DpiBindDpiTemplate_Type()
)
dpiBindDpiTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiBindDpiTemplate.setStatus("current")
_DpiShowAllSignatureEntryTable_Object = MibTable
dpiShowAllSignatureEntryTable = _DpiShowAllSignatureEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 7)
)
if mibBuilder.loadTexts:
    dpiShowAllSignatureEntryTable.setStatus("current")
_DpiShowAllSignatureEntry_Object = MibTableRow
dpiShowAllSignatureEntry = _DpiShowAllSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 7, 1)
)
dpiShowAllSignatureEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllSignatureEntryID"),
)
if mibBuilder.loadTexts:
    dpiShowAllSignatureEntry.setStatus("current")


class _DpiAllSignatureEntryID_Type(Integer32):
    """Custom type dpiAllSignatureEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12287),
    )


_DpiAllSignatureEntryID_Type.__name__ = "Integer32"
_DpiAllSignatureEntryID_Object = MibTableColumn
dpiAllSignatureEntryID = _DpiAllSignatureEntryID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 7, 1, 1),
    _DpiAllSignatureEntryID_Type()
)
dpiAllSignatureEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureEntryID.setStatus("current")
_DpiAllSignatureEntryContent_Type = DisplayString
_DpiAllSignatureEntryContent_Object = MibTableColumn
dpiAllSignatureEntryContent = _DpiAllSignatureEntryContent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 7, 1, 2),
    _DpiAllSignatureEntryContent_Type()
)
dpiAllSignatureEntryContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureEntryContent.setStatus("current")
_DpiShowAllSignatureSymbolTable_Object = MibTable
dpiShowAllSignatureSymbolTable = _DpiShowAllSignatureSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8)
)
if mibBuilder.loadTexts:
    dpiShowAllSignatureSymbolTable.setStatus("current")
_DpiShowAllSignatureSymbolEntry_Object = MibTableRow
dpiShowAllSignatureSymbolEntry = _DpiShowAllSignatureSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8, 1)
)
dpiShowAllSignatureSymbolEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllSignatureSymbolID"),
)
if mibBuilder.loadTexts:
    dpiShowAllSignatureSymbolEntry.setStatus("current")


class _DpiAllSignatureSymbolID_Type(Integer32):
    """Custom type dpiAllSignatureSymbolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6143),
    )


_DpiAllSignatureSymbolID_Type.__name__ = "Integer32"
_DpiAllSignatureSymbolID_Object = MibTableColumn
dpiAllSignatureSymbolID = _DpiAllSignatureSymbolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8, 1, 1),
    _DpiAllSignatureSymbolID_Type()
)
dpiAllSignatureSymbolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureSymbolID.setStatus("current")
_DpiAllSignatureSymbolEntryList_Type = DisplayString
_DpiAllSignatureSymbolEntryList_Object = MibTableColumn
dpiAllSignatureSymbolEntryList = _DpiAllSignatureSymbolEntryList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8, 1, 2),
    _DpiAllSignatureSymbolEntryList_Type()
)
dpiAllSignatureSymbolEntryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureSymbolEntryList.setStatus("current")


class _DpiAllSignatureSymbolHitNumLimit_Type(Integer32):
    """Custom type dpiAllSignatureSymbolHitNumLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DpiAllSignatureSymbolHitNumLimit_Type.__name__ = "Integer32"
_DpiAllSignatureSymbolHitNumLimit_Object = MibTableColumn
dpiAllSignatureSymbolHitNumLimit = _DpiAllSignatureSymbolHitNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8, 1, 3),
    _DpiAllSignatureSymbolHitNumLimit_Type()
)
dpiAllSignatureSymbolHitNumLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureSymbolHitNumLimit.setStatus("current")


class _DpiAllSignatureSymbolProtocol_Type(Integer32):
    """Custom type dpiAllSignatureSymbolProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 2),
          ("normal", 1))
    )


_DpiAllSignatureSymbolProtocol_Type.__name__ = "Integer32"
_DpiAllSignatureSymbolProtocol_Object = MibTableColumn
dpiAllSignatureSymbolProtocol = _DpiAllSignatureSymbolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 8, 1, 4),
    _DpiAllSignatureSymbolProtocol_Type()
)
dpiAllSignatureSymbolProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSignatureSymbolProtocol.setStatus("current")
_DpiShowAllFlowPoolTable_Object = MibTable
dpiShowAllFlowPoolTable = _DpiShowAllFlowPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9)
)
if mibBuilder.loadTexts:
    dpiShowAllFlowPoolTable.setStatus("current")
_DpiShowAllFlowPoolEntry_Object = MibTableRow
dpiShowAllFlowPoolEntry = _DpiShowAllFlowPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1)
)
dpiShowAllFlowPoolEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllFlowPoolID"),
)
if mibBuilder.loadTexts:
    dpiShowAllFlowPoolEntry.setStatus("current")


class _DpiAllFlowPoolID_Type(Integer32):
    """Custom type dpiAllFlowPoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiAllFlowPoolID_Type.__name__ = "Integer32"
_DpiAllFlowPoolID_Object = MibTableColumn
dpiAllFlowPoolID = _DpiAllFlowPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 1),
    _DpiAllFlowPoolID_Type()
)
dpiAllFlowPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllFlowPoolID.setStatus("current")


class _DpiAllUpStreamRate_Type(Integer32):
    """Custom type dpiAllUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_DpiAllUpStreamRate_Type.__name__ = "Integer32"
_DpiAllUpStreamRate_Object = MibTableColumn
dpiAllUpStreamRate = _DpiAllUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 2),
    _DpiAllUpStreamRate_Type()
)
dpiAllUpStreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllUpStreamRate.setStatus("current")
_DpiAllUpStreamCbs_Type = Integer32
_DpiAllUpStreamCbs_Object = MibTableColumn
dpiAllUpStreamCbs = _DpiAllUpStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 3),
    _DpiAllUpStreamCbs_Type()
)
dpiAllUpStreamCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllUpStreamCbs.setStatus("current")
_DpiAllUpStreamEbs_Type = Integer32
_DpiAllUpStreamEbs_Object = MibTableColumn
dpiAllUpStreamEbs = _DpiAllUpStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 4),
    _DpiAllUpStreamEbs_Type()
)
dpiAllUpStreamEbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllUpStreamEbs.setStatus("current")


class _DpiAllDownStreamRate_Type(Integer32):
    """Custom type dpiAllDownStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_DpiAllDownStreamRate_Type.__name__ = "Integer32"
_DpiAllDownStreamRate_Object = MibTableColumn
dpiAllDownStreamRate = _DpiAllDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 5),
    _DpiAllDownStreamRate_Type()
)
dpiAllDownStreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllDownStreamRate.setStatus("current")
_DpiAllDownStreamCbs_Type = Integer32
_DpiAllDownStreamCbs_Object = MibTableColumn
dpiAllDownStreamCbs = _DpiAllDownStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 6),
    _DpiAllDownStreamCbs_Type()
)
dpiAllDownStreamCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllDownStreamCbs.setStatus("current")
_DpiAllDownStreamEbs_Type = Integer32
_DpiAllDownStreamEbs_Object = MibTableColumn
dpiAllDownStreamEbs = _DpiAllDownStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 9, 1, 7),
    _DpiAllDownStreamEbs_Type()
)
dpiAllDownStreamEbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllDownStreamEbs.setStatus("current")
_DpiShowAllSubserviceTable_Object = MibTable
dpiShowAllSubserviceTable = _DpiShowAllSubserviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10)
)
if mibBuilder.loadTexts:
    dpiShowAllSubserviceTable.setStatus("current")
_DpiShowAllSubserviceEntry_Object = MibTableRow
dpiShowAllSubserviceEntry = _DpiShowAllSubserviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1)
)
dpiShowAllSubserviceEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllSubserviceID"),
)
if mibBuilder.loadTexts:
    dpiShowAllSubserviceEntry.setStatus("current")


class _DpiAllSubserviceID_Type(Integer32):
    """Custom type dpiAllSubserviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiAllSubserviceID_Type.__name__ = "Integer32"
_DpiAllSubserviceID_Object = MibTableColumn
dpiAllSubserviceID = _DpiAllSubserviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 1),
    _DpiAllSubserviceID_Type()
)
dpiAllSubserviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceID.setStatus("current")


class _DpiAllSubserviceFlowpoolID_Type(Integer32):
    """Custom type dpiAllSubserviceFlowpoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiAllSubserviceFlowpoolID_Type.__name__ = "Integer32"
_DpiAllSubserviceFlowpoolID_Object = MibTableColumn
dpiAllSubserviceFlowpoolID = _DpiAllSubserviceFlowpoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 3),
    _DpiAllSubserviceFlowpoolID_Type()
)
dpiAllSubserviceFlowpoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceFlowpoolID.setStatus("current")


class _DpiAllSubserviceAction_Type(Integer32):
    """Custom type dpiAllSubserviceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_DpiAllSubserviceAction_Type.__name__ = "Integer32"
_DpiAllSubserviceAction_Object = MibTableColumn
dpiAllSubserviceAction = _DpiAllSubserviceAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 4),
    _DpiAllSubserviceAction_Type()
)
dpiAllSubserviceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceAction.setStatus("current")


class _DpiAllSubserviceAgingTime_Type(Integer32):
    """Custom type dpiAllSubserviceAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DpiAllSubserviceAgingTime_Type.__name__ = "Integer32"
_DpiAllSubserviceAgingTime_Object = MibTableColumn
dpiAllSubserviceAgingTime = _DpiAllSubserviceAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 5),
    _DpiAllSubserviceAgingTime_Type()
)
dpiAllSubserviceAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceAgingTime.setStatus("current")
_DpiAllSubserviceSymbolList_Type = DisplayString
_DpiAllSubserviceSymbolList_Object = MibTableColumn
dpiAllSubserviceSymbolList = _DpiAllSubserviceSymbolList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 6),
    _DpiAllSubserviceSymbolList_Type()
)
dpiAllSubserviceSymbolList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceSymbolList.setStatus("current")
_DpiAllSubserviceProtocol_Type = DisplayString
_DpiAllSubserviceProtocol_Object = MibTableColumn
dpiAllSubserviceProtocol = _DpiAllSubserviceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 10, 1, 7),
    _DpiAllSubserviceProtocol_Type()
)
dpiAllSubserviceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSubserviceProtocol.setStatus("current")
_DpiShowAllServiceTable_Object = MibTable
dpiShowAllServiceTable = _DpiShowAllServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11)
)
if mibBuilder.loadTexts:
    dpiShowAllServiceTable.setStatus("current")
_DpiShowAllServiceEntry_Object = MibTableRow
dpiShowAllServiceEntry = _DpiShowAllServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11, 1)
)
dpiShowAllServiceEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllServiceID"),
)
if mibBuilder.loadTexts:
    dpiShowAllServiceEntry.setStatus("current")


class _DpiAllServiceID_Type(Integer32):
    """Custom type dpiAllServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_DpiAllServiceID_Type.__name__ = "Integer32"
_DpiAllServiceID_Object = MibTableColumn
dpiAllServiceID = _DpiAllServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11, 1, 1),
    _DpiAllServiceID_Type()
)
dpiAllServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllServiceID.setStatus("current")


class _DpiAllServiceFlowPoolID_Type(Integer32):
    """Custom type dpiAllServiceFlowPoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_DpiAllServiceFlowPoolID_Type.__name__ = "Integer32"
_DpiAllServiceFlowPoolID_Object = MibTableColumn
dpiAllServiceFlowPoolID = _DpiAllServiceFlowPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11, 1, 2),
    _DpiAllServiceFlowPoolID_Type()
)
dpiAllServiceFlowPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllServiceFlowPoolID.setStatus("current")


class _DpiAllServiceSubserviceNum_Type(Integer32):
    """Custom type dpiAllServiceSubserviceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DpiAllServiceSubserviceNum_Type.__name__ = "Integer32"
_DpiAllServiceSubserviceNum_Object = MibTableColumn
dpiAllServiceSubserviceNum = _DpiAllServiceSubserviceNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11, 1, 4),
    _DpiAllServiceSubserviceNum_Type()
)
dpiAllServiceSubserviceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllServiceSubserviceNum.setStatus("current")


class _DpiAllServiceSubserviceList_Type(OctetString):
    """Custom type dpiAllServiceSubserviceList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1049),
    )


_DpiAllServiceSubserviceList_Type.__name__ = "OctetString"
_DpiAllServiceSubserviceList_Object = MibTableColumn
dpiAllServiceSubserviceList = _DpiAllServiceSubserviceList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 11, 1, 5),
    _DpiAllServiceSubserviceList_Type()
)
dpiAllServiceSubserviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllServiceSubserviceList.setStatus("current")
_DpiShowAllTemplateTable_Object = MibTable
dpiShowAllTemplateTable = _DpiShowAllTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 12)
)
if mibBuilder.loadTexts:
    dpiShowAllTemplateTable.setStatus("current")
_DpiShowAllTemplateEntry_Object = MibTableRow
dpiShowAllTemplateEntry = _DpiShowAllTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 12, 1)
)
dpiShowAllTemplateEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllTemplateID"),
)
if mibBuilder.loadTexts:
    dpiShowAllTemplateEntry.setStatus("current")


class _DpiAllTemplateID_Type(Integer32):
    """Custom type dpiAllTemplateID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DpiAllTemplateID_Type.__name__ = "Integer32"
_DpiAllTemplateID_Object = MibTableColumn
dpiAllTemplateID = _DpiAllTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 12, 1, 1),
    _DpiAllTemplateID_Type()
)
dpiAllTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllTemplateID.setStatus("current")
_DpiAllTemplateCfgCmd_Type = DisplayString
_DpiAllTemplateCfgCmd_Object = MibTableColumn
dpiAllTemplateCfgCmd = _DpiAllTemplateCfgCmd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 12, 1, 2),
    _DpiAllTemplateCfgCmd_Type()
)
dpiAllTemplateCfgCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllTemplateCfgCmd.setStatus("current")
_DpiShowAllMnpIpTable_Object = MibTable
dpiShowAllMnpIpTable = _DpiShowAllMnpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13)
)
if mibBuilder.loadTexts:
    dpiShowAllMnpIpTable.setStatus("current")
_DpiShowAllMngIpEntry_Object = MibTableRow
dpiShowAllMngIpEntry = _DpiShowAllMngIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1)
)
dpiShowAllMngIpEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllSlotID"),
)
if mibBuilder.loadTexts:
    dpiShowAllMngIpEntry.setStatus("current")


class _DpiAllSlotID_Type(Integer32):
    """Custom type dpiAllSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DpiAllSlotID_Type.__name__ = "Integer32"
_DpiAllSlotID_Object = MibTableColumn
dpiAllSlotID = _DpiAllSlotID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 1),
    _DpiAllSlotID_Type()
)
dpiAllSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllSlotID.setStatus("current")
_DpiAllMngIp_Type = IpAddress
_DpiAllMngIp_Object = MibTableColumn
dpiAllMngIp = _DpiAllMngIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 2),
    _DpiAllMngIp_Type()
)
dpiAllMngIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllMngIp.setStatus("current")
_DpiAllServerIp_Type = IpAddress
_DpiAllServerIp_Object = MibTableColumn
dpiAllServerIp = _DpiAllServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 3),
    _DpiAllServerIp_Type()
)
dpiAllServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllServerIp.setStatus("current")


class _DpiAllMngIpIsUsed_Type(Integer32):
    """Custom type dpiAllMngIpIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_DpiAllMngIpIsUsed_Type.__name__ = "Integer32"
_DpiAllMngIpIsUsed_Object = MibTableColumn
dpiAllMngIpIsUsed = _DpiAllMngIpIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 4),
    _DpiAllMngIpIsUsed_Type()
)
dpiAllMngIpIsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllMngIpIsUsed.setStatus("current")
_DpiAllLogSaveInterval_Type = Integer32
_DpiAllLogSaveInterval_Object = MibTableColumn
dpiAllLogSaveInterval = _DpiAllLogSaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 5),
    _DpiAllLogSaveInterval_Type()
)
dpiAllLogSaveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllLogSaveInterval.setStatus("current")


class _DpiAllLogAutoUpload_Type(Integer32):
    """Custom type dpiAllLogAutoUpload based on Integer32"""
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


_DpiAllLogAutoUpload_Type.__name__ = "Integer32"
_DpiAllLogAutoUpload_Object = MibTableColumn
dpiAllLogAutoUpload = _DpiAllLogAutoUpload_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 6),
    _DpiAllLogAutoUpload_Type()
)
dpiAllLogAutoUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllLogAutoUpload.setStatus("current")
_DpiAllLogUploadInterval_Type = Integer32
_DpiAllLogUploadInterval_Object = MibTableColumn
dpiAllLogUploadInterval = _DpiAllLogUploadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 13, 1, 7),
    _DpiAllLogUploadInterval_Type()
)
dpiAllLogUploadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllLogUploadInterval.setStatus("current")
_DpiShowAllVlanDpiTable_Object = MibTable
dpiShowAllVlanDpiTable = _DpiShowAllVlanDpiTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14)
)
if mibBuilder.loadTexts:
    dpiShowAllVlanDpiTable.setStatus("current")
_DpiShowAllVlanDpiEntry_Object = MibTableRow
dpiShowAllVlanDpiEntry = _DpiShowAllVlanDpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1)
)
dpiShowAllVlanDpiEntry.setIndexNames(
    (0, "DPI-MIB", "dpiAllVlanID"),
)
if mibBuilder.loadTexts:
    dpiShowAllVlanDpiEntry.setStatus("current")
_DpiAllVlanID_Type = Integer32
_DpiAllVlanID_Object = MibTableColumn
dpiAllVlanID = _DpiAllVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1, 1),
    _DpiAllVlanID_Type()
)
dpiAllVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllVlanID.setStatus("current")
_DpiAllVlanBindTemplateID_Type = Integer32
_DpiAllVlanBindTemplateID_Object = MibTableColumn
dpiAllVlanBindTemplateID = _DpiAllVlanBindTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1, 2),
    _DpiAllVlanBindTemplateID_Type()
)
dpiAllVlanBindTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllVlanBindTemplateID.setStatus("current")
_DpiAllVlanBindSlotID_Type = Integer32
_DpiAllVlanBindSlotID_Object = MibTableColumn
dpiAllVlanBindSlotID = _DpiAllVlanBindSlotID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1, 3),
    _DpiAllVlanBindSlotID_Type()
)
dpiAllVlanBindSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllVlanBindSlotID.setStatus("current")
_DpiAllVlanBindServiceID_Type = Integer32
_DpiAllVlanBindServiceID_Object = MibTableColumn
dpiAllVlanBindServiceID = _DpiAllVlanBindServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1, 4),
    _DpiAllVlanBindServiceID_Type()
)
dpiAllVlanBindServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllVlanBindServiceID.setStatus("current")


class _DpiAllVlanBindIsUsed_Type(Integer32):
    """Custom type dpiAllVlanBindIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_DpiAllVlanBindIsUsed_Type.__name__ = "Integer32"
_DpiAllVlanBindIsUsed_Object = MibTableColumn
dpiAllVlanBindIsUsed = _DpiAllVlanBindIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 51, 1, 14, 1, 5),
    _DpiAllVlanBindIsUsed_Type()
)
dpiAllVlanBindIsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiAllVlanBindIsUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPI-MIB",
    **{"zte": zte,
       "fwdpi": fwdpi,
       "zxrDPI": zxrDPI,
       "dpiSystemControl": dpiSystemControl,
       "dpiSlotNumber": dpiSlotNumber,
       "dpiRestartFunc": dpiRestartFunc,
       "dpiConfigMode": dpiConfigMode,
       "dpiBindMngServiceIp": dpiBindMngServiceIp,
       "dpiMngServerSlot": dpiMngServerSlot,
       "dpiMngIp": dpiMngIp,
       "dpiServerIp": dpiServerIp,
       "dpiMngServerOK": dpiMngServerOK,
       "dpiSignatureEntry": dpiSignatureEntry,
       "dpiCurrentSignatureEntry": dpiCurrentSignatureEntry,
       "dpiShowSignatureEntry": dpiShowSignatureEntry,
       "dpiSignatureEntryTable": dpiSignatureEntryTable,
       "dpiSignatureTableEntry": dpiSignatureTableEntry,
       "dpiSignatureEntryID": dpiSignatureEntryID,
       "dpiSignatureEntryContent": dpiSignatureEntryContent,
       "dpiSetContent": dpiSetContent,
       "dpiSignatureSymbol": dpiSignatureSymbol,
       "dpiCurrentSignatureSymbol": dpiCurrentSignatureSymbol,
       "dpiShowSignatureSymbol": dpiShowSignatureSymbol,
       "dpiSignatureSymbolTable": dpiSignatureSymbolTable,
       "dpiSignatureSymbolTableEntry": dpiSignatureSymbolTableEntry,
       "dpiSignatureSymbolID": dpiSignatureSymbolID,
       "dpiSignatureSymbolEntryID": dpiSignatureSymbolEntryID,
       "dpiSignatureSymbolHitNumLimit": dpiSignatureSymbolHitNumLimit,
       "dpiAddSignatureEntry": dpiAddSignatureEntry,
       "dpiNoAddSignatureEntry": dpiNoAddSignatureEntry,
       "dpiSetHitNumLimit": dpiSetHitNumLimit,
       "dpiFlowPool": dpiFlowPool,
       "dpiCurrentFlowPool": dpiCurrentFlowPool,
       "dpiShowFlowPool": dpiShowFlowPool,
       "dpiStreamLimitTable": dpiStreamLimitTable,
       "dpiStreamLimitTableEntry": dpiStreamLimitTableEntry,
       "dpiStreamLimitID": dpiStreamLimitID,
       "dpiStreamLimitType": dpiStreamLimitType,
       "dpiStreamRate": dpiStreamRate,
       "dpiStreamCbs": dpiStreamCbs,
       "dpiStreamEbs": dpiStreamEbs,
       "dpiUpStreamRateLimit": dpiUpStreamRateLimit,
       "dpiUpStreamRate": dpiUpStreamRate,
       "dpiUpStreamCbs": dpiUpStreamCbs,
       "dpiUpStreamEbs": dpiUpStreamEbs,
       "dpiUpStreamOK": dpiUpStreamOK,
       "dpiNoUpStreamRateLimit": dpiNoUpStreamRateLimit,
       "dpiDownStreamRateLimit": dpiDownStreamRateLimit,
       "dpiDownStreamRate": dpiDownStreamRate,
       "dpiDownStreamCbs": dpiDownStreamCbs,
       "dpiDownStreamEbs": dpiDownStreamEbs,
       "dpiDownStreamOK": dpiDownStreamOK,
       "dpiNoDownStreamRateLimit": dpiNoDownStreamRateLimit,
       "dpiSubservice": dpiSubservice,
       "dpiCurrentSubservice": dpiCurrentSubservice,
       "dpiShowSubservice": dpiShowSubservice,
       "dpiSubserviceTable": dpiSubserviceTable,
       "dpiSubserviceEntry": dpiSubserviceEntry,
       "dpiSubserviceID": dpiSubserviceID,
       "dpiSubserviceSymbolNum": dpiSubserviceSymbolNum,
       "dpiSubserviceFlowpoolID": dpiSubserviceFlowpoolID,
       "dpiSubserviceAction": dpiSubserviceAction,
       "dpiSubserviceAgingTime": dpiSubserviceAgingTime,
       "dpiSubserviceSymbolList": dpiSubserviceSymbolList,
       "dpiAddSignatureSymbol": dpiAddSignatureSymbol,
       "dpiAddSignatureSymbolId": dpiAddSignatureSymbolId,
       "dpiAddSignatureSymbolRelationName": dpiAddSignatureSymbolRelationName,
       "dpiAddSignatureSymbolOK": dpiAddSignatureSymbolOK,
       "dpiNoAddSignatureSymbol": dpiNoAddSignatureSymbol,
       "dpiAddProtocol": dpiAddProtocol,
       "dpiNoAddProtocol": dpiNoAddProtocol,
       "dpiBindFlowPool": dpiBindFlowPool,
       "dpiNoBindFlowPool": dpiNoBindFlowPool,
       "dpiSetAction": dpiSetAction,
       "dpiSetAgingTime": dpiSetAgingTime,
       "dpiService": dpiService,
       "dpiCurrentService": dpiCurrentService,
       "dpiShowService": dpiShowService,
       "dpiServiceTable": dpiServiceTable,
       "dpiServiceEntry": dpiServiceEntry,
       "dpiServiceID": dpiServiceID,
       "dpiServiceFlowPoolID": dpiServiceFlowPoolID,
       "dpiServiceConnectionLimit": dpiServiceConnectionLimit,
       "dpiServiceSubserviceNum": dpiServiceSubserviceNum,
       "dpiServiceSubserviceList": dpiServiceSubserviceList,
       "dpiAddSubservice": dpiAddSubservice,
       "dpiNoAddSubservice": dpiNoAddSubservice,
       "dpiImportSubservice": dpiImportSubservice,
       "dpiImportDestSubservice": dpiImportDestSubservice,
       "dpiImportSrcSubservice": dpiImportSrcSubservice,
       "dpiImportSubserviceOK": dpiImportSubserviceOK,
       "dpiNoImportSubservice": dpiNoImportSubservice,
       "dpiServiceBindFlowPool": dpiServiceBindFlowPool,
       "dpiServiceNoBindFlowPool": dpiServiceNoBindFlowPool,
       "dpiTemplate": dpiTemplate,
       "dpiCurrentTemplate": dpiCurrentTemplate,
       "dpiBindSlot": dpiBindSlot,
       "dpiNoBindSlot": dpiNoBindSlot,
       "dpiBindService": dpiBindService,
       "dpiNoBindService": dpiNoBindService,
       "dpiBindSipAddr": dpiBindSipAddr,
       "dpiSipAddress": dpiSipAddress,
       "dpiSipMask": dpiSipMask,
       "dpiSipServiceID": dpiSipServiceID,
       "dpiBindSipAddrOK": dpiBindSipAddrOK,
       "dpiNoBindSipAddr": dpiNoBindSipAddr,
       "dpiShowIpService": dpiShowIpService,
       "dpiBindSwitchport": dpiBindSwitchport,
       "dpiBindSwitchportPort": dpiBindSwitchportPort,
       "dpiBindSwitchService": dpiBindSwitchService,
       "dpiBindSwitchportOK": dpiBindSwitchportOK,
       "dpiNoBindSwitchport": dpiNoBindSwitchport,
       "dpiShowPortService": dpiShowPortService,
       "dpiSetActiceConnectionSaveInterval": dpiSetActiceConnectionSaveInterval,
       "dpiClearConnectionAll": dpiClearConnectionAll,
       "dpiMonitorLog": dpiMonitorLog,
       "dpiUploadAuto": dpiUploadAuto,
       "dpiUploadAutoSlot": dpiUploadAutoSlot,
       "dpiUploadAutoEnable": dpiUploadAutoEnable,
       "dpiUploadAutoOK": dpiUploadAutoOK,
       "dpiUploadInterval": dpiUploadInterval,
       "dpiUploadIntervalSlot": dpiUploadIntervalSlot,
       "dpiUploadTimeInterval": dpiUploadTimeInterval,
       "dpiUploadIntervalOK": dpiUploadIntervalOK,
       "dpiLogFileListDir": dpiLogFileListDir,
       "dpiLogFileListDirSlot": dpiLogFileListDirSlot,
       "dpiLogFileListDirFtpFile": dpiLogFileListDirFtpFile,
       "dpiLogFileListDirLocalDir": dpiLogFileListDirLocalDir,
       "dpiLogFileListDirOK": dpiLogFileListDirOK,
       "dpiLogFileDeleteDir": dpiLogFileDeleteDir,
       "dpiLogFileDeleteDirSlot": dpiLogFileDeleteDirSlot,
       "dpiLogFileDeleteDirName": dpiLogFileDeleteDirName,
       "dpiLogFileDeleteDirOK": dpiLogFileDeleteDirOK,
       "dpiLogFileDeleteFile": dpiLogFileDeleteFile,
       "dpiLogFileDeleteFileSlot": dpiLogFileDeleteFileSlot,
       "dpiLogFileDeleteFileName": dpiLogFileDeleteFileName,
       "dpiLogFileDeleteFileOK": dpiLogFileDeleteFileOK,
       "dpiUpdateDpiLog": dpiUpdateDpiLog,
       "dpiUpdateDpiLogSlot": dpiUpdateDpiLogSlot,
       "dpiLogServerFileName": dpiLogServerFileName,
       "dpiLogLocalFileName": dpiLogLocalFileName,
       "dpiUpdateDpiLogOK": dpiUpdateDpiLogOK,
       "dpiUploadTodayLog": dpiUploadTodayLog,
       "dpiCommit": dpiCommit,
       "dpiUpdateSignatureVersion": dpiUpdateSignatureVersion,
       "dpiVlanBindDpiTemplate": dpiVlanBindDpiTemplate,
       "dpiVlanInterfaceName": dpiVlanInterfaceName,
       "dpiBindDpiTemplate": dpiBindDpiTemplate,
       "dpiShowAllSignatureEntryTable": dpiShowAllSignatureEntryTable,
       "dpiShowAllSignatureEntry": dpiShowAllSignatureEntry,
       "dpiAllSignatureEntryID": dpiAllSignatureEntryID,
       "dpiAllSignatureEntryContent": dpiAllSignatureEntryContent,
       "dpiShowAllSignatureSymbolTable": dpiShowAllSignatureSymbolTable,
       "dpiShowAllSignatureSymbolEntry": dpiShowAllSignatureSymbolEntry,
       "dpiAllSignatureSymbolID": dpiAllSignatureSymbolID,
       "dpiAllSignatureSymbolEntryList": dpiAllSignatureSymbolEntryList,
       "dpiAllSignatureSymbolHitNumLimit": dpiAllSignatureSymbolHitNumLimit,
       "dpiAllSignatureSymbolProtocol": dpiAllSignatureSymbolProtocol,
       "dpiShowAllFlowPoolTable": dpiShowAllFlowPoolTable,
       "dpiShowAllFlowPoolEntry": dpiShowAllFlowPoolEntry,
       "dpiAllFlowPoolID": dpiAllFlowPoolID,
       "dpiAllUpStreamRate": dpiAllUpStreamRate,
       "dpiAllUpStreamCbs": dpiAllUpStreamCbs,
       "dpiAllUpStreamEbs": dpiAllUpStreamEbs,
       "dpiAllDownStreamRate": dpiAllDownStreamRate,
       "dpiAllDownStreamCbs": dpiAllDownStreamCbs,
       "dpiAllDownStreamEbs": dpiAllDownStreamEbs,
       "dpiShowAllSubserviceTable": dpiShowAllSubserviceTable,
       "dpiShowAllSubserviceEntry": dpiShowAllSubserviceEntry,
       "dpiAllSubserviceID": dpiAllSubserviceID,
       "dpiAllSubserviceFlowpoolID": dpiAllSubserviceFlowpoolID,
       "dpiAllSubserviceAction": dpiAllSubserviceAction,
       "dpiAllSubserviceAgingTime": dpiAllSubserviceAgingTime,
       "dpiAllSubserviceSymbolList": dpiAllSubserviceSymbolList,
       "dpiAllSubserviceProtocol": dpiAllSubserviceProtocol,
       "dpiShowAllServiceTable": dpiShowAllServiceTable,
       "dpiShowAllServiceEntry": dpiShowAllServiceEntry,
       "dpiAllServiceID": dpiAllServiceID,
       "dpiAllServiceFlowPoolID": dpiAllServiceFlowPoolID,
       "dpiAllServiceSubserviceNum": dpiAllServiceSubserviceNum,
       "dpiAllServiceSubserviceList": dpiAllServiceSubserviceList,
       "dpiShowAllTemplateTable": dpiShowAllTemplateTable,
       "dpiShowAllTemplateEntry": dpiShowAllTemplateEntry,
       "dpiAllTemplateID": dpiAllTemplateID,
       "dpiAllTemplateCfgCmd": dpiAllTemplateCfgCmd,
       "dpiShowAllMnpIpTable": dpiShowAllMnpIpTable,
       "dpiShowAllMngIpEntry": dpiShowAllMngIpEntry,
       "dpiAllSlotID": dpiAllSlotID,
       "dpiAllMngIp": dpiAllMngIp,
       "dpiAllServerIp": dpiAllServerIp,
       "dpiAllMngIpIsUsed": dpiAllMngIpIsUsed,
       "dpiAllLogSaveInterval": dpiAllLogSaveInterval,
       "dpiAllLogAutoUpload": dpiAllLogAutoUpload,
       "dpiAllLogUploadInterval": dpiAllLogUploadInterval,
       "dpiShowAllVlanDpiTable": dpiShowAllVlanDpiTable,
       "dpiShowAllVlanDpiEntry": dpiShowAllVlanDpiEntry,
       "dpiAllVlanID": dpiAllVlanID,
       "dpiAllVlanBindTemplateID": dpiAllVlanBindTemplateID,
       "dpiAllVlanBindSlotID": dpiAllVlanBindSlotID,
       "dpiAllVlanBindServiceID": dpiAllVlanBindServiceID,
       "dpiAllVlanBindIsUsed": dpiAllVlanBindIsUsed}
)
