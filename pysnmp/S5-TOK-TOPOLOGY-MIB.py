# SNMP MIB module (S5-TOK-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-TOK-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:11 2024
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

(s5TrTop,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5TrTop")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(SnpxBackplaneType,
 SnpxChassisType) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "SnpxBackplaneType",
    "SnpxChassisType")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5TrTopIfTable_Object = MibTable
s5TrTopIfTable = _S5TrTopIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    s5TrTopIfTable.setStatus("mandatory")
_S5TrTopIfEntry_Object = MibTableRow
s5TrTopIfEntry = _S5TrTopIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1)
)
s5TrTopIfEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopIfIpAddr"),
)
if mibBuilder.loadTexts:
    s5TrTopIfEntry.setStatus("mandatory")
_S5TrTopIfIpAddr_Type = IpAddress
_S5TrTopIfIpAddr_Object = MibTableColumn
s5TrTopIfIpAddr = _S5TrTopIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 1),
    _S5TrTopIfIpAddr_Type()
)
s5TrTopIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfIpAddr.setStatus("mandatory")


class _S5TrTopIfNum_Type(Integer32):
    """Custom type s5TrTopIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S5TrTopIfNum_Type.__name__ = "Integer32"
_S5TrTopIfNum_Object = MibTableColumn
s5TrTopIfNum = _S5TrTopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 2),
    _S5TrTopIfNum_Type()
)
s5TrTopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfNum.setStatus("mandatory")


class _S5TrTopIfStatus_Type(Integer32):
    """Custom type s5TrTopIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("topOff", 2),
          ("topOn", 1))
    )


_S5TrTopIfStatus_Type.__name__ = "Integer32"
_S5TrTopIfStatus_Object = MibTableColumn
s5TrTopIfStatus = _S5TrTopIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 3),
    _S5TrTopIfStatus_Type()
)
s5TrTopIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTopIfStatus.setStatus("mandatory")
_S5TrTopIfNmmLstChg_Type = TimeTicks
_S5TrTopIfNmmLstChg_Object = MibTableColumn
s5TrTopIfNmmLstChg = _S5TrTopIfNmmLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 4),
    _S5TrTopIfNmmLstChg_Type()
)
s5TrTopIfNmmLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfNmmLstChg.setStatus("mandatory")
_S5TrTopIfBdgLstChg_Type = TimeTicks
_S5TrTopIfBdgLstChg_Object = MibTableColumn
s5TrTopIfBdgLstChg = _S5TrTopIfBdgLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 5),
    _S5TrTopIfBdgLstChg_Type()
)
s5TrTopIfBdgLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfBdgLstChg.setStatus("mandatory")
_S5TrTopIfRingNmmLstChg_Type = TimeTicks
_S5TrTopIfRingNmmLstChg_Object = MibTableColumn
s5TrTopIfRingNmmLstChg = _S5TrTopIfRingNmmLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 6),
    _S5TrTopIfRingNmmLstChg_Type()
)
s5TrTopIfRingNmmLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfRingNmmLstChg.setStatus("mandatory")


class _S5TrTopIfNmmMaxNum_Type(Integer32):
    """Custom type s5TrTopIfNmmMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrTopIfNmmMaxNum_Type.__name__ = "Integer32"
_S5TrTopIfNmmMaxNum_Object = MibTableColumn
s5TrTopIfNmmMaxNum = _S5TrTopIfNmmMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 7),
    _S5TrTopIfNmmMaxNum_Type()
)
s5TrTopIfNmmMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfNmmMaxNum.setStatus("mandatory")


class _S5TrTopIfNmmCurNum_Type(Integer32):
    """Custom type s5TrTopIfNmmCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrTopIfNmmCurNum_Type.__name__ = "Integer32"
_S5TrTopIfNmmCurNum_Object = MibTableColumn
s5TrTopIfNmmCurNum = _S5TrTopIfNmmCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 8),
    _S5TrTopIfNmmCurNum_Type()
)
s5TrTopIfNmmCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfNmmCurNum.setStatus("mandatory")


class _S5TrTopIfBdgMaxNum_Type(Integer32):
    """Custom type s5TrTopIfBdgMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrTopIfBdgMaxNum_Type.__name__ = "Integer32"
_S5TrTopIfBdgMaxNum_Object = MibTableColumn
s5TrTopIfBdgMaxNum = _S5TrTopIfBdgMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 9),
    _S5TrTopIfBdgMaxNum_Type()
)
s5TrTopIfBdgMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfBdgMaxNum.setStatus("mandatory")


class _S5TrTopIfBdgCurNum_Type(Integer32):
    """Custom type s5TrTopIfBdgCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrTopIfBdgCurNum_Type.__name__ = "Integer32"
_S5TrTopIfBdgCurNum_Object = MibTableColumn
s5TrTopIfBdgCurNum = _S5TrTopIfBdgCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 10),
    _S5TrTopIfBdgCurNum_Type()
)
s5TrTopIfBdgCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfBdgCurNum.setStatus("mandatory")


class _S5TrTopIfRingNmmMaxNum_Type(Integer32):
    """Custom type s5TrTopIfRingNmmMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopIfRingNmmMaxNum_Type.__name__ = "Integer32"
_S5TrTopIfRingNmmMaxNum_Object = MibTableColumn
s5TrTopIfRingNmmMaxNum = _S5TrTopIfRingNmmMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 11),
    _S5TrTopIfRingNmmMaxNum_Type()
)
s5TrTopIfRingNmmMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfRingNmmMaxNum.setStatus("mandatory")


class _S5TrTopIfRingNmmCurNum_Type(Integer32):
    """Custom type s5TrTopIfRingNmmCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopIfRingNmmCurNum_Type.__name__ = "Integer32"
_S5TrTopIfRingNmmCurNum_Object = MibTableColumn
s5TrTopIfRingNmmCurNum = _S5TrTopIfRingNmmCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 12),
    _S5TrTopIfRingNmmCurNum_Type()
)
s5TrTopIfRingNmmCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopIfRingNmmCurNum.setStatus("mandatory")


class _S5TrTopIfTopSpeed_Type(Integer32):
    """Custom type s5TrTopIfTopSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("topFast", 2),
          ("topSlow", 3))
    )


_S5TrTopIfTopSpeed_Type.__name__ = "Integer32"
_S5TrTopIfTopSpeed_Object = MibTableColumn
s5TrTopIfTopSpeed = _S5TrTopIfTopSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 1, 1, 13),
    _S5TrTopIfTopSpeed_Type()
)
s5TrTopIfTopSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTopIfTopSpeed.setStatus("mandatory")
_S5TrTopNmmTable_Object = MibTable
s5TrTopNmmTable = _S5TrTopNmmTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2)
)
if mibBuilder.loadTexts:
    s5TrTopNmmTable.setStatus("mandatory")
_S5TrTopNmmEntry_Object = MibTableRow
s5TrTopNmmEntry = _S5TrTopNmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1)
)
s5TrTopNmmEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopNmmIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s5TrTopNmmEntry.setStatus("mandatory")
_S5TrTopNmmIfIpAddr_Type = IpAddress
_S5TrTopNmmIfIpAddr_Object = MibTableColumn
s5TrTopNmmIfIpAddr = _S5TrTopNmmIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 1),
    _S5TrTopNmmIfIpAddr_Type()
)
s5TrTopNmmIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmIfIpAddr.setStatus("mandatory")
_S5TrTopNmmIpAddr_Type = IpAddress
_S5TrTopNmmIpAddr_Object = MibTableColumn
s5TrTopNmmIpAddr = _S5TrTopNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 2),
    _S5TrTopNmmIpAddr_Type()
)
s5TrTopNmmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmIpAddr.setStatus("mandatory")


class _S5TrTopNmmRingNum_Type(Integer32):
    """Custom type s5TrTopNmmRingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_S5TrTopNmmRingNum_Type.__name__ = "Integer32"
_S5TrTopNmmRingNum_Object = MibTableColumn
s5TrTopNmmRingNum = _S5TrTopNmmRingNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 3),
    _S5TrTopNmmRingNum_Type()
)
s5TrTopNmmRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmRingNum.setStatus("mandatory")


class _S5TrTopNmmRingMaster_Type(Integer32):
    """Custom type s5TrTopNmmRingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("normal", 1))
    )


_S5TrTopNmmRingMaster_Type.__name__ = "Integer32"
_S5TrTopNmmRingMaster_Object = MibTableColumn
s5TrTopNmmRingMaster = _S5TrTopNmmRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 4),
    _S5TrTopNmmRingMaster_Type()
)
s5TrTopNmmRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmRingMaster.setStatus("mandatory")
_S5TrTopNmmRingSpeed_Type = Integer32
_S5TrTopNmmRingSpeed_Object = MibTableColumn
s5TrTopNmmRingSpeed = _S5TrTopNmmRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 5),
    _S5TrTopNmmRingSpeed_Type()
)
s5TrTopNmmRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmRingSpeed.setStatus("mandatory")
_S5TrTopNmmBridgeGroupIdentifier_Type = Integer32
_S5TrTopNmmBridgeGroupIdentifier_Object = MibTableColumn
s5TrTopNmmBridgeGroupIdentifier = _S5TrTopNmmBridgeGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 6),
    _S5TrTopNmmBridgeGroupIdentifier_Type()
)
s5TrTopNmmBridgeGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmBridgeGroupIdentifier.setStatus("mandatory")
_S5TrTopNmmSlotNum_Type = Integer32
_S5TrTopNmmSlotNum_Object = MibTableColumn
s5TrTopNmmSlotNum = _S5TrTopNmmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 7),
    _S5TrTopNmmSlotNum_Type()
)
s5TrTopNmmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmSlotNum.setStatus("mandatory")


class _S5TrTopNmmPortNum_Type(Integer32):
    """Custom type s5TrTopNmmPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopNmmPortNum_Type.__name__ = "Integer32"
_S5TrTopNmmPortNum_Object = MibTableColumn
s5TrTopNmmPortNum = _S5TrTopNmmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 2, 1, 8),
    _S5TrTopNmmPortNum_Type()
)
s5TrTopNmmPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmPortNum.setStatus("mandatory")
_S5TrTopBdgTable_Object = MibTable
s5TrTopBdgTable = _S5TrTopBdgTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3)
)
if mibBuilder.loadTexts:
    s5TrTopBdgTable.setStatus("mandatory")
_S5TrTopBdgEntry_Object = MibTableRow
s5TrTopBdgEntry = _S5TrTopBdgEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1)
)
s5TrTopBdgEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopBdgIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopBdgIndx"),
)
if mibBuilder.loadTexts:
    s5TrTopBdgEntry.setStatus("mandatory")
_S5TrTopBdgIfIpAddr_Type = IpAddress
_S5TrTopBdgIfIpAddr_Object = MibTableColumn
s5TrTopBdgIfIpAddr = _S5TrTopBdgIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 1),
    _S5TrTopBdgIfIpAddr_Type()
)
s5TrTopBdgIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgIfIpAddr.setStatus("mandatory")


class _S5TrTopBdgIndx_Type(Integer32):
    """Custom type s5TrTopBdgIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S5TrTopBdgIndx_Type.__name__ = "Integer32"
_S5TrTopBdgIndx_Object = MibTableColumn
s5TrTopBdgIndx = _S5TrTopBdgIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 2),
    _S5TrTopBdgIndx_Type()
)
s5TrTopBdgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgIndx.setStatus("mandatory")


class _S5TrTopBdgNum_Type(Integer32):
    """Custom type s5TrTopBdgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_S5TrTopBdgNum_Type.__name__ = "Integer32"
_S5TrTopBdgNum_Object = MibTableColumn
s5TrTopBdgNum = _S5TrTopBdgNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 3),
    _S5TrTopBdgNum_Type()
)
s5TrTopBdgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgNum.setStatus("mandatory")


class _S5TrTopBdgOwnRingNum_Type(Integer32):
    """Custom type s5TrTopBdgOwnRingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_S5TrTopBdgOwnRingNum_Type.__name__ = "Integer32"
_S5TrTopBdgOwnRingNum_Object = MibTableColumn
s5TrTopBdgOwnRingNum = _S5TrTopBdgOwnRingNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 4),
    _S5TrTopBdgOwnRingNum_Type()
)
s5TrTopBdgOwnRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgOwnRingNum.setStatus("mandatory")


class _S5TrTopBdgAdjRingNum_Type(Integer32):
    """Custom type s5TrTopBdgAdjRingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_S5TrTopBdgAdjRingNum_Type.__name__ = "Integer32"
_S5TrTopBdgAdjRingNum_Object = MibTableColumn
s5TrTopBdgAdjRingNum = _S5TrTopBdgAdjRingNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 5),
    _S5TrTopBdgAdjRingNum_Type()
)
s5TrTopBdgAdjRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgAdjRingNum.setStatus("mandatory")
_S5TrTopBdgAdjMasterNmmIpAddr_Type = IpAddress
_S5TrTopBdgAdjMasterNmmIpAddr_Object = MibTableColumn
s5TrTopBdgAdjMasterNmmIpAddr = _S5TrTopBdgAdjMasterNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 6),
    _S5TrTopBdgAdjMasterNmmIpAddr_Type()
)
s5TrTopBdgAdjMasterNmmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgAdjMasterNmmIpAddr.setStatus("mandatory")
_S5TrTopBdgMacAddr_Type = MacAddress
_S5TrTopBdgMacAddr_Object = MibTableColumn
s5TrTopBdgMacAddr = _S5TrTopBdgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 7),
    _S5TrTopBdgMacAddr_Type()
)
s5TrTopBdgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgMacAddr.setStatus("mandatory")
_S5TrTopBdgIpAddr_Type = IpAddress
_S5TrTopBdgIpAddr_Object = MibTableColumn
s5TrTopBdgIpAddr = _S5TrTopBdgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 8),
    _S5TrTopBdgIpAddr_Type()
)
s5TrTopBdgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgIpAddr.setStatus("mandatory")


class _S5TrTopBdgType_Type(Integer32):
    """Custom type s5TrTopBdgType based on Integer32"""
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
        *(("other", 1),
          ("t2722Syn2Port", 3),
          ("t3522Syn2Port", 2),
          ("tCenTillionTrSwitch", 4))
    )


_S5TrTopBdgType_Type.__name__ = "Integer32"
_S5TrTopBdgType_Object = MibTableColumn
s5TrTopBdgType = _S5TrTopBdgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 9),
    _S5TrTopBdgType_Type()
)
s5TrTopBdgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgType.setStatus("mandatory")


class _S5TrTopBdgSlotNum_Type(Integer32):
    """Custom type s5TrTopBdgSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopBdgSlotNum_Type.__name__ = "Integer32"
_S5TrTopBdgSlotNum_Object = MibTableColumn
s5TrTopBdgSlotNum = _S5TrTopBdgSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 10),
    _S5TrTopBdgSlotNum_Type()
)
s5TrTopBdgSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgSlotNum.setStatus("mandatory")


class _S5TrTopBdgPortNum_Type(Integer32):
    """Custom type s5TrTopBdgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopBdgPortNum_Type.__name__ = "Integer32"
_S5TrTopBdgPortNum_Object = MibTableColumn
s5TrTopBdgPortNum = _S5TrTopBdgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 11),
    _S5TrTopBdgPortNum_Type()
)
s5TrTopBdgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgPortNum.setStatus("mandatory")


class _S5TrTopBdgNumPort_Type(Integer32):
    """Custom type s5TrTopBdgNumPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopBdgNumPort_Type.__name__ = "Integer32"
_S5TrTopBdgNumPort_Object = MibTableColumn
s5TrTopBdgNumPort = _S5TrTopBdgNumPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 12),
    _S5TrTopBdgNumPort_Type()
)
s5TrTopBdgNumPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgNumPort.setStatus("mandatory")


class _S5TrTopBdgHelloPortNum_Type(Integer32):
    """Custom type s5TrTopBdgHelloPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopBdgHelloPortNum_Type.__name__ = "Integer32"
_S5TrTopBdgHelloPortNum_Object = MibTableColumn
s5TrTopBdgHelloPortNum = _S5TrTopBdgHelloPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 13),
    _S5TrTopBdgHelloPortNum_Type()
)
s5TrTopBdgHelloPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgHelloPortNum.setStatus("mandatory")


class _S5TrTopBdgHelloPortStatus_Type(Integer32):
    """Custom type s5TrTopBdgHelloPortStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("srSrsOff", 5),
          ("srSrsOffStnBy", 9),
          ("srSrsOffTranAct", 7),
          ("srSrsOn", 4),
          ("srSrsOnStnBy", 8),
          ("srSrsOnTranAct", 6),
          ("tranAct", 2),
          ("tranStnBy", 3))
    )


_S5TrTopBdgHelloPortStatus_Type.__name__ = "Integer32"
_S5TrTopBdgHelloPortStatus_Object = MibTableColumn
s5TrTopBdgHelloPortStatus = _S5TrTopBdgHelloPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 14),
    _S5TrTopBdgHelloPortStatus_Type()
)
s5TrTopBdgHelloPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgHelloPortStatus.setStatus("mandatory")


class _S5TrTopBdgMonPortStatus_Type(Integer32):
    """Custom type s5TrTopBdgMonPortStatus based on Integer32"""
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
        *(("other", 1),
          ("phantomOff", 2),
          ("phantomOffWrapped", 4),
          ("phantomOn", 3),
          ("phantomOnWrapped", 5),
          ("wrongSpeedWrap", 6))
    )


_S5TrTopBdgMonPortStatus_Type.__name__ = "Integer32"
_S5TrTopBdgMonPortStatus_Object = MibTableColumn
s5TrTopBdgMonPortStatus = _S5TrTopBdgMonPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 15),
    _S5TrTopBdgMonPortStatus_Type()
)
s5TrTopBdgMonPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgMonPortStatus.setStatus("mandatory")


class _S5TrTopBdgHelloType_Type(Integer32):
    """Custom type s5TrTopBdgHelloType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ibm", 3),
          ("other", 1),
          ("synoptics", 2))
    )


_S5TrTopBdgHelloType_Type.__name__ = "Integer32"
_S5TrTopBdgHelloType_Object = MibTableColumn
s5TrTopBdgHelloType = _S5TrTopBdgHelloType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 3, 1, 16),
    _S5TrTopBdgHelloType_Type()
)
s5TrTopBdgHelloType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgHelloType.setStatus("mandatory")
_S5TrTopRingNmmTable_Object = MibTable
s5TrTopRingNmmTable = _S5TrTopRingNmmTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4)
)
if mibBuilder.loadTexts:
    s5TrTopRingNmmTable.setStatus("mandatory")
_S5TrTopRingNmmEntry_Object = MibTableRow
s5TrTopRingNmmEntry = _S5TrTopRingNmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1)
)
s5TrTopRingNmmEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopRingNmmIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopRingNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s5TrTopRingNmmEntry.setStatus("mandatory")
_S5TrTopRingNmmIfIpAddr_Type = IpAddress
_S5TrTopRingNmmIfIpAddr_Object = MibTableColumn
s5TrTopRingNmmIfIpAddr = _S5TrTopRingNmmIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 1),
    _S5TrTopRingNmmIfIpAddr_Type()
)
s5TrTopRingNmmIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmIfIpAddr.setStatus("mandatory")
_S5TrTopRingNmmIpAddr_Type = IpAddress
_S5TrTopRingNmmIpAddr_Object = MibTableColumn
s5TrTopRingNmmIpAddr = _S5TrTopRingNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 2),
    _S5TrTopRingNmmIpAddr_Type()
)
s5TrTopRingNmmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmIpAddr.setStatus("mandatory")
_S5TrTopRingNmmMacAddr_Type = MacAddress
_S5TrTopRingNmmMacAddr_Object = MibTableColumn
s5TrTopRingNmmMacAddr = _S5TrTopRingNmmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 3),
    _S5TrTopRingNmmMacAddr_Type()
)
s5TrTopRingNmmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmMacAddr.setStatus("mandatory")
_S5TrTopRingNmmChassisType_Type = SnpxChassisType
_S5TrTopRingNmmChassisType_Object = MibTableColumn
s5TrTopRingNmmChassisType = _S5TrTopRingNmmChassisType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 4),
    _S5TrTopRingNmmChassisType_Type()
)
s5TrTopRingNmmChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmChassisType.setStatus("mandatory")
_S5TrTopRingNmmBkplType_Type = SnpxBackplaneType
_S5TrTopRingNmmBkplType_Object = MibTableColumn
s5TrTopRingNmmBkplType = _S5TrTopRingNmmBkplType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 5),
    _S5TrTopRingNmmBkplType_Type()
)
s5TrTopRingNmmBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmBkplType.setStatus("mandatory")


class _S5TrTopRingNmmSlotNum_Type(Integer32):
    """Custom type s5TrTopRingNmmSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrTopRingNmmSlotNum_Type.__name__ = "Integer32"
_S5TrTopRingNmmSlotNum_Object = MibTableColumn
s5TrTopRingNmmSlotNum = _S5TrTopRingNmmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 6),
    _S5TrTopRingNmmSlotNum_Type()
)
s5TrTopRingNmmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmSlotNum.setStatus("mandatory")
_S5TrTopRingNmmUnaIpAddr_Type = IpAddress
_S5TrTopRingNmmUnaIpAddr_Object = MibTableColumn
s5TrTopRingNmmUnaIpAddr = _S5TrTopRingNmmUnaIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 4, 1, 7),
    _S5TrTopRingNmmUnaIpAddr_Type()
)
s5TrTopRingNmmUnaIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmUnaIpAddr.setStatus("mandatory")


class _S5TrTopNmmEosSize_Type(Integer32):
    """Custom type s5TrTopNmmEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_S5TrTopNmmEosSize_Type.__name__ = "Integer32"
_S5TrTopNmmEosSize_Object = MibScalar
s5TrTopNmmEosSize = _S5TrTopNmmEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 5),
    _S5TrTopNmmEosSize_Type()
)
s5TrTopNmmEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmEosSize.setStatus("mandatory")
_S5TrTopNmmEosTable_Object = MibTable
s5TrTopNmmEosTable = _S5TrTopNmmEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 6)
)
if mibBuilder.loadTexts:
    s5TrTopNmmEosTable.setStatus("mandatory")
_S5TrTopNmmEosEntry_Object = MibTableRow
s5TrTopNmmEosEntry = _S5TrTopNmmEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 6, 1)
)
s5TrTopNmmEosEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopNmmIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s5TrTopNmmEosEntry.setStatus("mandatory")


class _S5TrTopNmmEos_Type(OctetString):
    """Custom type s5TrTopNmmEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5TrTopNmmEos_Type.__name__ = "OctetString"
_S5TrTopNmmEos_Object = MibTableColumn
s5TrTopNmmEos = _S5TrTopNmmEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 6, 1, 1),
    _S5TrTopNmmEos_Type()
)
s5TrTopNmmEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopNmmEos.setStatus("mandatory")


class _S5TrTopBdgEosSize_Type(Integer32):
    """Custom type s5TrTopBdgEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_S5TrTopBdgEosSize_Type.__name__ = "Integer32"
_S5TrTopBdgEosSize_Object = MibScalar
s5TrTopBdgEosSize = _S5TrTopBdgEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 7),
    _S5TrTopBdgEosSize_Type()
)
s5TrTopBdgEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgEosSize.setStatus("mandatory")
_S5TrTopBdgEosTable_Object = MibTable
s5TrTopBdgEosTable = _S5TrTopBdgEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 8)
)
if mibBuilder.loadTexts:
    s5TrTopBdgEosTable.setStatus("mandatory")
_S5TrTopBdgEosEntry_Object = MibTableRow
s5TrTopBdgEosEntry = _S5TrTopBdgEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 8, 1)
)
s5TrTopBdgEosEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopBdgIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopBdgIndx"),
)
if mibBuilder.loadTexts:
    s5TrTopBdgEosEntry.setStatus("mandatory")


class _S5TrTopBdgEos_Type(OctetString):
    """Custom type s5TrTopBdgEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5TrTopBdgEos_Type.__name__ = "OctetString"
_S5TrTopBdgEos_Object = MibTableColumn
s5TrTopBdgEos = _S5TrTopBdgEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 8, 1, 1),
    _S5TrTopBdgEos_Type()
)
s5TrTopBdgEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopBdgEos.setStatus("mandatory")


class _S5TrTopRingNmmEosSize_Type(Integer32):
    """Custom type s5TrTopRingNmmEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_S5TrTopRingNmmEosSize_Type.__name__ = "Integer32"
_S5TrTopRingNmmEosSize_Object = MibScalar
s5TrTopRingNmmEosSize = _S5TrTopRingNmmEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 9),
    _S5TrTopRingNmmEosSize_Type()
)
s5TrTopRingNmmEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmEosSize.setStatus("mandatory")
_S5TrTopRingNmmEosTable_Object = MibTable
s5TrTopRingNmmEosTable = _S5TrTopRingNmmEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 10)
)
if mibBuilder.loadTexts:
    s5TrTopRingNmmEosTable.setStatus("mandatory")
_S5TrTopRingNmmEosEntry_Object = MibTableRow
s5TrTopRingNmmEosEntry = _S5TrTopRingNmmEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 10, 1)
)
s5TrTopRingNmmEosEntry.setIndexNames(
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopRingNmmIfIpAddr"),
    (0, "S5-TOK-TOPOLOGY-MIB", "s5TrTopRingNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s5TrTopRingNmmEosEntry.setStatus("mandatory")


class _S5TrTopRingNmmEos_Type(OctetString):
    """Custom type s5TrTopRingNmmEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5TrTopRingNmmEos_Type.__name__ = "OctetString"
_S5TrTopRingNmmEos_Object = MibTableColumn
s5TrTopRingNmmEos = _S5TrTopRingNmmEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10, 10, 1, 1),
    _S5TrTopRingNmmEos_Type()
)
s5TrTopRingNmmEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTopRingNmmEos.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-TOK-TOPOLOGY-MIB",
    **{"s5TrTopIfTable": s5TrTopIfTable,
       "s5TrTopIfEntry": s5TrTopIfEntry,
       "s5TrTopIfIpAddr": s5TrTopIfIpAddr,
       "s5TrTopIfNum": s5TrTopIfNum,
       "s5TrTopIfStatus": s5TrTopIfStatus,
       "s5TrTopIfNmmLstChg": s5TrTopIfNmmLstChg,
       "s5TrTopIfBdgLstChg": s5TrTopIfBdgLstChg,
       "s5TrTopIfRingNmmLstChg": s5TrTopIfRingNmmLstChg,
       "s5TrTopIfNmmMaxNum": s5TrTopIfNmmMaxNum,
       "s5TrTopIfNmmCurNum": s5TrTopIfNmmCurNum,
       "s5TrTopIfBdgMaxNum": s5TrTopIfBdgMaxNum,
       "s5TrTopIfBdgCurNum": s5TrTopIfBdgCurNum,
       "s5TrTopIfRingNmmMaxNum": s5TrTopIfRingNmmMaxNum,
       "s5TrTopIfRingNmmCurNum": s5TrTopIfRingNmmCurNum,
       "s5TrTopIfTopSpeed": s5TrTopIfTopSpeed,
       "s5TrTopNmmTable": s5TrTopNmmTable,
       "s5TrTopNmmEntry": s5TrTopNmmEntry,
       "s5TrTopNmmIfIpAddr": s5TrTopNmmIfIpAddr,
       "s5TrTopNmmIpAddr": s5TrTopNmmIpAddr,
       "s5TrTopNmmRingNum": s5TrTopNmmRingNum,
       "s5TrTopNmmRingMaster": s5TrTopNmmRingMaster,
       "s5TrTopNmmRingSpeed": s5TrTopNmmRingSpeed,
       "s5TrTopNmmBridgeGroupIdentifier": s5TrTopNmmBridgeGroupIdentifier,
       "s5TrTopNmmSlotNum": s5TrTopNmmSlotNum,
       "s5TrTopNmmPortNum": s5TrTopNmmPortNum,
       "s5TrTopBdgTable": s5TrTopBdgTable,
       "s5TrTopBdgEntry": s5TrTopBdgEntry,
       "s5TrTopBdgIfIpAddr": s5TrTopBdgIfIpAddr,
       "s5TrTopBdgIndx": s5TrTopBdgIndx,
       "s5TrTopBdgNum": s5TrTopBdgNum,
       "s5TrTopBdgOwnRingNum": s5TrTopBdgOwnRingNum,
       "s5TrTopBdgAdjRingNum": s5TrTopBdgAdjRingNum,
       "s5TrTopBdgAdjMasterNmmIpAddr": s5TrTopBdgAdjMasterNmmIpAddr,
       "s5TrTopBdgMacAddr": s5TrTopBdgMacAddr,
       "s5TrTopBdgIpAddr": s5TrTopBdgIpAddr,
       "s5TrTopBdgType": s5TrTopBdgType,
       "s5TrTopBdgSlotNum": s5TrTopBdgSlotNum,
       "s5TrTopBdgPortNum": s5TrTopBdgPortNum,
       "s5TrTopBdgNumPort": s5TrTopBdgNumPort,
       "s5TrTopBdgHelloPortNum": s5TrTopBdgHelloPortNum,
       "s5TrTopBdgHelloPortStatus": s5TrTopBdgHelloPortStatus,
       "s5TrTopBdgMonPortStatus": s5TrTopBdgMonPortStatus,
       "s5TrTopBdgHelloType": s5TrTopBdgHelloType,
       "s5TrTopRingNmmTable": s5TrTopRingNmmTable,
       "s5TrTopRingNmmEntry": s5TrTopRingNmmEntry,
       "s5TrTopRingNmmIfIpAddr": s5TrTopRingNmmIfIpAddr,
       "s5TrTopRingNmmIpAddr": s5TrTopRingNmmIpAddr,
       "s5TrTopRingNmmMacAddr": s5TrTopRingNmmMacAddr,
       "s5TrTopRingNmmChassisType": s5TrTopRingNmmChassisType,
       "s5TrTopRingNmmBkplType": s5TrTopRingNmmBkplType,
       "s5TrTopRingNmmSlotNum": s5TrTopRingNmmSlotNum,
       "s5TrTopRingNmmUnaIpAddr": s5TrTopRingNmmUnaIpAddr,
       "s5TrTopNmmEosSize": s5TrTopNmmEosSize,
       "s5TrTopNmmEosTable": s5TrTopNmmEosTable,
       "s5TrTopNmmEosEntry": s5TrTopNmmEosEntry,
       "s5TrTopNmmEos": s5TrTopNmmEos,
       "s5TrTopBdgEosSize": s5TrTopBdgEosSize,
       "s5TrTopBdgEosTable": s5TrTopBdgEosTable,
       "s5TrTopBdgEosEntry": s5TrTopBdgEosEntry,
       "s5TrTopBdgEos": s5TrTopBdgEos,
       "s5TrTopRingNmmEosSize": s5TrTopRingNmmEosSize,
       "s5TrTopRingNmmEosTable": s5TrTopRingNmmEosTable,
       "s5TrTopRingNmmEosEntry": s5TrTopRingNmmEosEntry,
       "s5TrTopRingNmmEos": s5TrTopRingNmmEos}
)
