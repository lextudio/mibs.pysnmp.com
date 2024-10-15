# SNMP MIB module (BIANCA-BRICK-X25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-X25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:51 2024
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


# MODULE-IDENTITY


# Types definitions



class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""




class Date(Integer32):
    """Custom type Date based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6)
)
_X25LinkTable_Object = MibTable
x25LinkTable = _X25LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1)
)
if mibBuilder.loadTexts:
    x25LinkTable.setStatus("mandatory")
_X25LinkEntry_Object = MibTableRow
x25LinkEntry = _X25LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1)
)
x25LinkEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25LkIfIndex"),
)
if mibBuilder.loadTexts:
    x25LinkEntry.setStatus("mandatory")
_X25LkIfIndex_Type = Integer32
_X25LkIfIndex_Object = MibTableColumn
x25LkIfIndex = _X25LkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 1),
    _X25LkIfIndex_Type()
)
x25LkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkIfIndex.setStatus("mandatory")
_X25LkAddr_Type = OctetString
_X25LkAddr_Object = MibTableColumn
x25LkAddr = _X25LkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 2),
    _X25LkAddr_Type()
)
x25LkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkAddr.setStatus("mandatory")


class _X25LkMode_Type(Integer32):
    """Custom type x25LkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_X25LkMode_Type.__name__ = "Integer32"
_X25LkMode_Object = MibTableColumn
x25LkMode = _X25LkMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 3),
    _X25LkMode_Type()
)
x25LkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkMode.setStatus("mandatory")


class _X25LkModulo_Type(Integer32):
    """Custom type x25LkModulo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mod128", 2),
          ("mod8", 1))
    )


_X25LkModulo_Type.__name__ = "Integer32"
_X25LkModulo_Object = MibTableColumn
x25LkModulo = _X25LkModulo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 4),
    _X25LkModulo_Type()
)
x25LkModulo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkModulo.setStatus("mandatory")


class _X25LkLIC_Type(Integer32):
    """Custom type x25LkLIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkLIC_Type.__name__ = "Integer32"
_X25LkLIC_Object = MibTableColumn
x25LkLIC = _X25LkLIC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 5),
    _X25LkLIC_Type()
)
x25LkLIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkLIC.setStatus("mandatory")


class _X25LkHIC_Type(Integer32):
    """Custom type x25LkHIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkHIC_Type.__name__ = "Integer32"
_X25LkHIC_Object = MibTableColumn
x25LkHIC = _X25LkHIC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 6),
    _X25LkHIC_Type()
)
x25LkHIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkHIC.setStatus("mandatory")


class _X25LkLTC_Type(Integer32):
    """Custom type x25LkLTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkLTC_Type.__name__ = "Integer32"
_X25LkLTC_Object = MibTableColumn
x25LkLTC = _X25LkLTC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 7),
    _X25LkLTC_Type()
)
x25LkLTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkLTC.setStatus("mandatory")


class _X25LkHTC_Type(Integer32):
    """Custom type x25LkHTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkHTC_Type.__name__ = "Integer32"
_X25LkHTC_Object = MibTableColumn
x25LkHTC = _X25LkHTC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 8),
    _X25LkHTC_Type()
)
x25LkHTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkHTC.setStatus("mandatory")


class _X25LkLOC_Type(Integer32):
    """Custom type x25LkLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkLOC_Type.__name__ = "Integer32"
_X25LkLOC_Object = MibTableColumn
x25LkLOC = _X25LkLOC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 9),
    _X25LkLOC_Type()
)
x25LkLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkLOC.setStatus("mandatory")


class _X25LkHOC_Type(Integer32):
    """Custom type x25LkHOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkHOC_Type.__name__ = "Integer32"
_X25LkHOC_Object = MibTableColumn
x25LkHOC = _X25LkHOC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 10),
    _X25LkHOC_Type()
)
x25LkHOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkHOC.setStatus("mandatory")


class _X25LkDefPktSize_Type(Integer32):
    """Custom type x25LkDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p2048", 11),
          ("p256", 8),
          ("p4096", 12),
          ("p512", 9))
    )


_X25LkDefPktSize_Type.__name__ = "Integer32"
_X25LkDefPktSize_Object = MibTableColumn
x25LkDefPktSize = _X25LkDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 11),
    _X25LkDefPktSize_Type()
)
x25LkDefPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkDefPktSize.setStatus("mandatory")


class _X25LkDefWinSize_Type(Integer32):
    """Custom type x25LkDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkDefWinSize_Type.__name__ = "Integer32"
_X25LkDefWinSize_Object = MibTableColumn
x25LkDefWinSize = _X25LkDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 12),
    _X25LkDefWinSize_Type()
)
x25LkDefWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkDefWinSize.setStatus("mandatory")


class _X25LkMaxPktSize_Type(Integer32):
    """Custom type x25LkMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p2048", 11),
          ("p256", 8),
          ("p4096", 12),
          ("p512", 9),
          ("unrestricted", 1))
    )


_X25LkMaxPktSize_Type.__name__ = "Integer32"
_X25LkMaxPktSize_Object = MibTableColumn
x25LkMaxPktSize = _X25LkMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 13),
    _X25LkMaxPktSize_Type()
)
x25LkMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkMaxPktSize.setStatus("mandatory")


class _X25LkMaxWinSize_Type(Integer32):
    """Custom type x25LkMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25LkMaxWinSize_Type.__name__ = "Integer32"
_X25LkMaxWinSize_Object = MibTableColumn
x25LkMaxWinSize = _X25LkMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 14),
    _X25LkMaxWinSize_Type()
)
x25LkMaxWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkMaxWinSize.setStatus("mandatory")


class _X25LkL2WinSize_Type(Integer32):
    """Custom type x25LkL2WinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkL2WinSize_Type.__name__ = "Integer32"
_X25LkL2WinSize_Object = MibTableColumn
x25LkL2WinSize = _X25LkL2WinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 15),
    _X25LkL2WinSize_Type()
)
x25LkL2WinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkL2WinSize.setStatus("mandatory")


class _X25LkL2RetrTimer_Type(Integer32):
    """Custom type x25LkL2RetrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_X25LkL2RetrTimer_Type.__name__ = "Integer32"
_X25LkL2RetrTimer_Object = MibTableColumn
x25LkL2RetrTimer = _X25LkL2RetrTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 16),
    _X25LkL2RetrTimer_Type()
)
x25LkL2RetrTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkL2RetrTimer.setStatus("mandatory")


class _X25LkL2RetrCounter_Type(Integer32):
    """Custom type x25LkL2RetrCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkL2RetrCounter_Type.__name__ = "Integer32"
_X25LkL2RetrCounter_Object = MibTableColumn
x25LkL2RetrCounter = _X25LkL2RetrCounter_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 17),
    _X25LkL2RetrCounter_Type()
)
x25LkL2RetrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkL2RetrCounter.setStatus("mandatory")


class _X25LkL2SupervTimer_Type(Integer32):
    """Custom type x25LkL2SupervTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_X25LkL2SupervTimer_Type.__name__ = "Integer32"
_X25LkL2SupervTimer_Object = MibTableColumn
x25LkL2SupervTimer = _X25LkL2SupervTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 18),
    _X25LkL2SupervTimer_Type()
)
x25LkL2SupervTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkL2SupervTimer.setStatus("mandatory")


class _X25LkL2IdleTimer_Type(Integer32):
    """Custom type x25LkL2IdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 30000),
    )


_X25LkL2IdleTimer_Type.__name__ = "Integer32"
_X25LkL2IdleTimer_Object = MibTableColumn
x25LkL2IdleTimer = _X25LkL2IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 19),
    _X25LkL2IdleTimer_Type()
)
x25LkL2IdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkL2IdleTimer.setStatus("mandatory")


class _X25LkState_Type(Integer32):
    """Custom type x25LkState based on Integer32"""
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
        *(("disc-pending", 4),
          ("ready", 3),
          ("reset-pending", 5),
          ("restart-collision", 2),
          ("restart-pending", 1),
          ("sabm-pending", 6),
          ("sabm-wait", 8),
          ("xid-pending", 7))
    )


_X25LkState_Type.__name__ = "Integer32"
_X25LkState_Object = MibTableColumn
x25LkState = _X25LkState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 20),
    _X25LkState_Type()
)
x25LkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkState.setStatus("mandatory")


class _X25LkNegotiation_Type(Integer32):
    """Custom type x25LkNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("never", 3),
          ("when-necessary", 1))
    )


_X25LkNegotiation_Type.__name__ = "Integer32"
_X25LkNegotiation_Object = MibTableColumn
x25LkNegotiation = _X25LkNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 21),
    _X25LkNegotiation_Type()
)
x25LkNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkNegotiation.setStatus("mandatory")


class _X25LkDiscDelayTimer_Type(Integer32):
    """Custom type x25LkDiscDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_X25LkDiscDelayTimer_Type.__name__ = "Integer32"
_X25LkDiscDelayTimer_Object = MibTableColumn
x25LkDiscDelayTimer = _X25LkDiscDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 22),
    _X25LkDiscDelayTimer_Type()
)
x25LkDiscDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkDiscDelayTimer.setStatus("mandatory")


class _X25LkCallDelayTimer_Type(Integer32):
    """Custom type x25LkCallDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_X25LkCallDelayTimer_Type.__name__ = "Integer32"
_X25LkCallDelayTimer_Object = MibTableColumn
x25LkCallDelayTimer = _X25LkCallDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 23),
    _X25LkCallDelayTimer_Type()
)
x25LkCallDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkCallDelayTimer.setStatus("mandatory")


class _X25LkRestDelayTimer_Type(Integer32):
    """Custom type x25LkRestDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_X25LkRestDelayTimer_Type.__name__ = "Integer32"
_X25LkRestDelayTimer_Object = MibTableColumn
x25LkRestDelayTimer = _X25LkRestDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 1, 1, 24),
    _X25LkRestDelayTimer_Type()
)
x25LkRestDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LkRestDelayTimer.setStatus("mandatory")
_X25LinkPresetTable_Object = MibTable
x25LinkPresetTable = _X25LinkPresetTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2)
)
if mibBuilder.loadTexts:
    x25LinkPresetTable.setStatus("mandatory")
_X25LinkPresetEntry_Object = MibTableRow
x25LinkPresetEntry = _X25LinkPresetEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1)
)
x25LinkPresetEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25LkPrIfIndex"),
)
if mibBuilder.loadTexts:
    x25LinkPresetEntry.setStatus("mandatory")
_X25LkPrIfIndex_Type = Integer32
_X25LkPrIfIndex_Object = MibTableColumn
x25LkPrIfIndex = _X25LkPrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 1),
    _X25LkPrIfIndex_Type()
)
x25LkPrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrIfIndex.setStatus("mandatory")
_X25LkPrAddr_Type = OctetString
_X25LkPrAddr_Object = MibTableColumn
x25LkPrAddr = _X25LkPrAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 2),
    _X25LkPrAddr_Type()
)
x25LkPrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrAddr.setStatus("mandatory")


class _X25LkPrMode_Type(Integer32):
    """Custom type x25LkPrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("delete", 3),
          ("dte", 1))
    )


_X25LkPrMode_Type.__name__ = "Integer32"
_X25LkPrMode_Object = MibTableColumn
x25LkPrMode = _X25LkPrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 3),
    _X25LkPrMode_Type()
)
x25LkPrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrMode.setStatus("mandatory")


class _X25LkPrModulo_Type(Integer32):
    """Custom type x25LkPrModulo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mod128", 2),
          ("mod8", 1))
    )


_X25LkPrModulo_Type.__name__ = "Integer32"
_X25LkPrModulo_Object = MibTableColumn
x25LkPrModulo = _X25LkPrModulo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 4),
    _X25LkPrModulo_Type()
)
x25LkPrModulo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrModulo.setStatus("mandatory")


class _X25LkPrLIC_Type(Integer32):
    """Custom type x25LkPrLIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrLIC_Type.__name__ = "Integer32"
_X25LkPrLIC_Object = MibTableColumn
x25LkPrLIC = _X25LkPrLIC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 5),
    _X25LkPrLIC_Type()
)
x25LkPrLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrLIC.setStatus("mandatory")


class _X25LkPrHIC_Type(Integer32):
    """Custom type x25LkPrHIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrHIC_Type.__name__ = "Integer32"
_X25LkPrHIC_Object = MibTableColumn
x25LkPrHIC = _X25LkPrHIC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 6),
    _X25LkPrHIC_Type()
)
x25LkPrHIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrHIC.setStatus("mandatory")


class _X25LkPrLTC_Type(Integer32):
    """Custom type x25LkPrLTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrLTC_Type.__name__ = "Integer32"
_X25LkPrLTC_Object = MibTableColumn
x25LkPrLTC = _X25LkPrLTC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 7),
    _X25LkPrLTC_Type()
)
x25LkPrLTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrLTC.setStatus("mandatory")


class _X25LkPrHTC_Type(Integer32):
    """Custom type x25LkPrHTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrHTC_Type.__name__ = "Integer32"
_X25LkPrHTC_Object = MibTableColumn
x25LkPrHTC = _X25LkPrHTC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 8),
    _X25LkPrHTC_Type()
)
x25LkPrHTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrHTC.setStatus("mandatory")


class _X25LkPrLOC_Type(Integer32):
    """Custom type x25LkPrLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrLOC_Type.__name__ = "Integer32"
_X25LkPrLOC_Object = MibTableColumn
x25LkPrLOC = _X25LkPrLOC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 9),
    _X25LkPrLOC_Type()
)
x25LkPrLOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrLOC.setStatus("mandatory")


class _X25LkPrHOC_Type(Integer32):
    """Custom type x25LkPrHOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25LkPrHOC_Type.__name__ = "Integer32"
_X25LkPrHOC_Object = MibTableColumn
x25LkPrHOC = _X25LkPrHOC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 10),
    _X25LkPrHOC_Type()
)
x25LkPrHOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrHOC.setStatus("mandatory")


class _X25LkPrDefPktSize_Type(Integer32):
    """Custom type x25LkPrDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p2048", 11),
          ("p256", 8),
          ("p4096", 12),
          ("p512", 9))
    )


_X25LkPrDefPktSize_Type.__name__ = "Integer32"
_X25LkPrDefPktSize_Object = MibTableColumn
x25LkPrDefPktSize = _X25LkPrDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 11),
    _X25LkPrDefPktSize_Type()
)
x25LkPrDefPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrDefPktSize.setStatus("mandatory")


class _X25LkPrDefWinSize_Type(Integer32):
    """Custom type x25LkPrDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkPrDefWinSize_Type.__name__ = "Integer32"
_X25LkPrDefWinSize_Object = MibTableColumn
x25LkPrDefWinSize = _X25LkPrDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 12),
    _X25LkPrDefWinSize_Type()
)
x25LkPrDefWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrDefWinSize.setStatus("mandatory")


class _X25LkPrMaxPktSize_Type(Integer32):
    """Custom type x25LkPrMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p2048", 11),
          ("p256", 8),
          ("p4096", 12),
          ("p512", 9),
          ("unrestricted", 1))
    )


_X25LkPrMaxPktSize_Type.__name__ = "Integer32"
_X25LkPrMaxPktSize_Object = MibTableColumn
x25LkPrMaxPktSize = _X25LkPrMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 13),
    _X25LkPrMaxPktSize_Type()
)
x25LkPrMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrMaxPktSize.setStatus("mandatory")


class _X25LkPrMaxWinSize_Type(Integer32):
    """Custom type x25LkPrMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkPrMaxWinSize_Type.__name__ = "Integer32"
_X25LkPrMaxWinSize_Object = MibTableColumn
x25LkPrMaxWinSize = _X25LkPrMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 14),
    _X25LkPrMaxWinSize_Type()
)
x25LkPrMaxWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrMaxWinSize.setStatus("mandatory")


class _X25LkPrL2WinSize_Type(Integer32):
    """Custom type x25LkPrL2WinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkPrL2WinSize_Type.__name__ = "Integer32"
_X25LkPrL2WinSize_Object = MibTableColumn
x25LkPrL2WinSize = _X25LkPrL2WinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 15),
    _X25LkPrL2WinSize_Type()
)
x25LkPrL2WinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrL2WinSize.setStatus("mandatory")


class _X25LkPrL2RetrTimer_Type(Integer32):
    """Custom type x25LkPrL2RetrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_X25LkPrL2RetrTimer_Type.__name__ = "Integer32"
_X25LkPrL2RetrTimer_Object = MibTableColumn
x25LkPrL2RetrTimer = _X25LkPrL2RetrTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 16),
    _X25LkPrL2RetrTimer_Type()
)
x25LkPrL2RetrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrL2RetrTimer.setStatus("mandatory")


class _X25LkPrL2RetrCounter_Type(Integer32):
    """Custom type x25LkPrL2RetrCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LkPrL2RetrCounter_Type.__name__ = "Integer32"
_X25LkPrL2RetrCounter_Object = MibTableColumn
x25LkPrL2RetrCounter = _X25LkPrL2RetrCounter_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 17),
    _X25LkPrL2RetrCounter_Type()
)
x25LkPrL2RetrCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrL2RetrCounter.setStatus("mandatory")


class _X25LkPrL2SupervTimer_Type(Integer32):
    """Custom type x25LkPrL2SupervTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_X25LkPrL2SupervTimer_Type.__name__ = "Integer32"
_X25LkPrL2SupervTimer_Object = MibTableColumn
x25LkPrL2SupervTimer = _X25LkPrL2SupervTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 18),
    _X25LkPrL2SupervTimer_Type()
)
x25LkPrL2SupervTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrL2SupervTimer.setStatus("mandatory")


class _X25LkPrL2IdleTimer_Type(Integer32):
    """Custom type x25LkPrL2IdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 30000),
    )


_X25LkPrL2IdleTimer_Type.__name__ = "Integer32"
_X25LkPrL2IdleTimer_Object = MibTableColumn
x25LkPrL2IdleTimer = _X25LkPrL2IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 19),
    _X25LkPrL2IdleTimer_Type()
)
x25LkPrL2IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrL2IdleTimer.setStatus("mandatory")


class _X25LkPrNegotiation_Type(Integer32):
    """Custom type x25LkPrNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("never", 3),
          ("when-necessary", 1))
    )


_X25LkPrNegotiation_Type.__name__ = "Integer32"
_X25LkPrNegotiation_Object = MibTableColumn
x25LkPrNegotiation = _X25LkPrNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 20),
    _X25LkPrNegotiation_Type()
)
x25LkPrNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrNegotiation.setStatus("mandatory")


class _X25LkPrDiscDelayTimer_Type(Integer32):
    """Custom type x25LkPrDiscDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_X25LkPrDiscDelayTimer_Type.__name__ = "Integer32"
_X25LkPrDiscDelayTimer_Object = MibTableColumn
x25LkPrDiscDelayTimer = _X25LkPrDiscDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 21),
    _X25LkPrDiscDelayTimer_Type()
)
x25LkPrDiscDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrDiscDelayTimer.setStatus("mandatory")


class _X25LkPrCallDelayTimer_Type(Integer32):
    """Custom type x25LkPrCallDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_X25LkPrCallDelayTimer_Type.__name__ = "Integer32"
_X25LkPrCallDelayTimer_Object = MibTableColumn
x25LkPrCallDelayTimer = _X25LkPrCallDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 22),
    _X25LkPrCallDelayTimer_Type()
)
x25LkPrCallDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrCallDelayTimer.setStatus("mandatory")


class _X25LkPrRestDelayTimer_Type(Integer32):
    """Custom type x25LkPrRestDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_X25LkPrRestDelayTimer_Type.__name__ = "Integer32"
_X25LkPrRestDelayTimer_Object = MibTableColumn
x25LkPrRestDelayTimer = _X25LkPrRestDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 2, 1, 23),
    _X25LkPrRestDelayTimer_Type()
)
x25LkPrRestDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LkPrRestDelayTimer.setStatus("mandatory")
_X25CallTable_Object = MibTable
x25CallTable = _X25CallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3)
)
if mibBuilder.loadTexts:
    x25CallTable.setStatus("mandatory")
_X25CallEntry_Object = MibTableRow
x25CallEntry = _X25CallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1)
)
x25CallEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25CallSrcIfIndex"),
    (0, "BIANCA-BRICK-X25-MIB", "x25CallSrcVCNumber"),
    (0, "BIANCA-BRICK-X25-MIB", "x25CallDstIfIndex"),
    (0, "BIANCA-BRICK-X25-MIB", "x25CallDstVCNumber"),
)
if mibBuilder.loadTexts:
    x25CallEntry.setStatus("mandatory")
_X25CallSrcIfIndex_Type = Integer32
_X25CallSrcIfIndex_Object = MibTableColumn
x25CallSrcIfIndex = _X25CallSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 1),
    _X25CallSrcIfIndex_Type()
)
x25CallSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallSrcIfIndex.setStatus("mandatory")
_X25CallSrcLinkAddr_Type = OctetString
_X25CallSrcLinkAddr_Object = MibTableColumn
x25CallSrcLinkAddr = _X25CallSrcLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 2),
    _X25CallSrcLinkAddr_Type()
)
x25CallSrcLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallSrcLinkAddr.setStatus("mandatory")


class _X25CallSrcVCNumber_Type(Integer32):
    """Custom type x25CallSrcVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25CallSrcVCNumber_Type.__name__ = "Integer32"
_X25CallSrcVCNumber_Object = MibTableColumn
x25CallSrcVCNumber = _X25CallSrcVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 3),
    _X25CallSrcVCNumber_Type()
)
x25CallSrcVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallSrcVCNumber.setStatus("mandatory")
_X25CallDstIfIndex_Type = Integer32
_X25CallDstIfIndex_Object = MibTableColumn
x25CallDstIfIndex = _X25CallDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 4),
    _X25CallDstIfIndex_Type()
)
x25CallDstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallDstIfIndex.setStatus("mandatory")
_X25CallDstLinkAddr_Type = OctetString
_X25CallDstLinkAddr_Object = MibTableColumn
x25CallDstLinkAddr = _X25CallDstLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 5),
    _X25CallDstLinkAddr_Type()
)
x25CallDstLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallDstLinkAddr.setStatus("mandatory")


class _X25CallDstVCNumber_Type(Integer32):
    """Custom type x25CallDstVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25CallDstVCNumber_Type.__name__ = "Integer32"
_X25CallDstVCNumber_Object = MibTableColumn
x25CallDstVCNumber = _X25CallDstVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 6),
    _X25CallDstVCNumber_Type()
)
x25CallDstVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallDstVCNumber.setStatus("mandatory")
_X25CallSrcAddr_Type = DisplayString
_X25CallSrcAddr_Object = MibTableColumn
x25CallSrcAddr = _X25CallSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 7),
    _X25CallSrcAddr_Type()
)
x25CallSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallSrcAddr.setStatus("mandatory")
_X25CallDstAddr_Type = DisplayString
_X25CallDstAddr_Object = MibTableColumn
x25CallDstAddr = _X25CallDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 8),
    _X25CallDstAddr_Type()
)
x25CallDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallDstAddr.setStatus("mandatory")
_X25CallProtocolId_Type = Integer32
_X25CallProtocolId_Object = MibTableColumn
x25CallProtocolId = _X25CallProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 9),
    _X25CallProtocolId_Type()
)
x25CallProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallProtocolId.setStatus("mandatory")
_X25CallFacilities_Type = OctetString
_X25CallFacilities_Object = MibTableColumn
x25CallFacilities = _X25CallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 10),
    _X25CallFacilities_Type()
)
x25CallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallFacilities.setStatus("mandatory")
_X25CallUserData_Type = DisplayString
_X25CallUserData_Object = MibTableColumn
x25CallUserData = _X25CallUserData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 11),
    _X25CallUserData_Type()
)
x25CallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallUserData.setStatus("mandatory")
_X25CallAge_Type = TimeTicks
_X25CallAge_Object = MibTableColumn
x25CallAge = _X25CallAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 12),
    _X25CallAge_Type()
)
x25CallAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallAge.setStatus("mandatory")


class _X25CallState_Type(Integer32):
    """Custom type x25CallState based on Integer32"""
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
        *(("call-pending", 2),
          ("dataxfer", 3),
          ("in-clear-pending", 7),
          ("in-reset-pending", 5),
          ("out-clear-pending", 6),
          ("out-reset-pending", 4),
          ("routing", 1))
    )


_X25CallState_Type.__name__ = "Integer32"
_X25CallState_Object = MibTableColumn
x25CallState = _X25CallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 13),
    _X25CallState_Type()
)
x25CallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallState.setStatus("mandatory")


class _X25CallInPktSize_Type(Integer32):
    """Custom type x25CallInPktSize based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p16", 4),
          ("p16384", 14),
          ("p2", 1),
          ("p2048", 11),
          ("p256", 8),
          ("p32", 5),
          ("p32768", 15),
          ("p4", 2),
          ("p4096", 12),
          ("p512", 9),
          ("p64", 6),
          ("p8", 3),
          ("p8192", 13))
    )


_X25CallInPktSize_Type.__name__ = "Integer32"
_X25CallInPktSize_Object = MibTableColumn
x25CallInPktSize = _X25CallInPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 14),
    _X25CallInPktSize_Type()
)
x25CallInPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallInPktSize.setStatus("mandatory")


class _X25CallOutPktSize_Type(Integer32):
    """Custom type x25CallOutPktSize based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p16", 4),
          ("p16384", 14),
          ("p2", 1),
          ("p2048", 11),
          ("p256", 8),
          ("p32", 5),
          ("p32768", 15),
          ("p4", 2),
          ("p4096", 12),
          ("p512", 9),
          ("p64", 6),
          ("p8", 3),
          ("p8192", 13))
    )


_X25CallOutPktSize_Type.__name__ = "Integer32"
_X25CallOutPktSize_Object = MibTableColumn
x25CallOutPktSize = _X25CallOutPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 15),
    _X25CallOutPktSize_Type()
)
x25CallOutPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallOutPktSize.setStatus("mandatory")


class _X25CallInWinSize_Type(Integer32):
    """Custom type x25CallInWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CallInWinSize_Type.__name__ = "Integer32"
_X25CallInWinSize_Object = MibTableColumn
x25CallInWinSize = _X25CallInWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 16),
    _X25CallInWinSize_Type()
)
x25CallInWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallInWinSize.setStatus("mandatory")


class _X25CallOutWinSize_Type(Integer32):
    """Custom type x25CallOutWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CallOutWinSize_Type.__name__ = "Integer32"
_X25CallOutWinSize_Object = MibTableColumn
x25CallOutWinSize = _X25CallOutWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 17),
    _X25CallOutWinSize_Type()
)
x25CallOutWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallOutWinSize.setStatus("mandatory")
_X25CallPktsSent_Type = Counter32
_X25CallPktsSent_Object = MibTableColumn
x25CallPktsSent = _X25CallPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 18),
    _X25CallPktsSent_Type()
)
x25CallPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallPktsSent.setStatus("mandatory")
_X25CallBytesSent_Type = Counter32
_X25CallBytesSent_Object = MibTableColumn
x25CallBytesSent = _X25CallBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 19),
    _X25CallBytesSent_Type()
)
x25CallBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallBytesSent.setStatus("mandatory")
_X25CallPktsRecvd_Type = Counter32
_X25CallPktsRecvd_Object = MibTableColumn
x25CallPktsRecvd = _X25CallPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 20),
    _X25CallPktsRecvd_Type()
)
x25CallPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallPktsRecvd.setStatus("mandatory")
_X25CallBytesRecvd_Type = Counter32
_X25CallBytesRecvd_Object = MibTableColumn
x25CallBytesRecvd = _X25CallBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 3, 1, 21),
    _X25CallBytesRecvd_Type()
)
x25CallBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallBytesRecvd.setStatus("mandatory")
_X25CallHistoryTable_Object = MibTable
x25CallHistoryTable = _X25CallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4)
)
if mibBuilder.loadTexts:
    x25CallHistoryTable.setStatus("mandatory")
_X25CallHistoryEntry_Object = MibTableRow
x25CallHistoryEntry = _X25CallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1)
)
x25CallHistoryEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25CallHistorySrcIfIndex"),
    (0, "BIANCA-BRICK-X25-MIB", "x25CallHistoryDstIfIndex"),
)
if mibBuilder.loadTexts:
    x25CallHistoryEntry.setStatus("mandatory")
_X25CallHistoryTime_Type = Date
_X25CallHistoryTime_Object = MibTableColumn
x25CallHistoryTime = _X25CallHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 1),
    _X25CallHistoryTime_Type()
)
x25CallHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryTime.setStatus("mandatory")
_X25CallHistoryDuration_Type = Integer32
_X25CallHistoryDuration_Object = MibTableColumn
x25CallHistoryDuration = _X25CallHistoryDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 2),
    _X25CallHistoryDuration_Type()
)
x25CallHistoryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryDuration.setStatus("mandatory")
_X25CallHistorySrcIfIndex_Type = Integer32
_X25CallHistorySrcIfIndex_Object = MibTableColumn
x25CallHistorySrcIfIndex = _X25CallHistorySrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 3),
    _X25CallHistorySrcIfIndex_Type()
)
x25CallHistorySrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistorySrcIfIndex.setStatus("mandatory")
_X25CallHistorySrcLinkAddr_Type = OctetString
_X25CallHistorySrcLinkAddr_Object = MibTableColumn
x25CallHistorySrcLinkAddr = _X25CallHistorySrcLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 4),
    _X25CallHistorySrcLinkAddr_Type()
)
x25CallHistorySrcLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistorySrcLinkAddr.setStatus("mandatory")


class _X25CallHistorySrcVCNumber_Type(Integer32):
    """Custom type x25CallHistorySrcVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25CallHistorySrcVCNumber_Type.__name__ = "Integer32"
_X25CallHistorySrcVCNumber_Object = MibTableColumn
x25CallHistorySrcVCNumber = _X25CallHistorySrcVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 5),
    _X25CallHistorySrcVCNumber_Type()
)
x25CallHistorySrcVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistorySrcVCNumber.setStatus("mandatory")
_X25CallHistoryDstIfIndex_Type = Integer32
_X25CallHistoryDstIfIndex_Object = MibTableColumn
x25CallHistoryDstIfIndex = _X25CallHistoryDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 6),
    _X25CallHistoryDstIfIndex_Type()
)
x25CallHistoryDstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryDstIfIndex.setStatus("mandatory")
_X25CallHistoryDstLinkAddr_Type = OctetString
_X25CallHistoryDstLinkAddr_Object = MibTableColumn
x25CallHistoryDstLinkAddr = _X25CallHistoryDstLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 7),
    _X25CallHistoryDstLinkAddr_Type()
)
x25CallHistoryDstLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryDstLinkAddr.setStatus("mandatory")


class _X25CallHistoryDstVCNumber_Type(Integer32):
    """Custom type x25CallHistoryDstVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25CallHistoryDstVCNumber_Type.__name__ = "Integer32"
_X25CallHistoryDstVCNumber_Object = MibTableColumn
x25CallHistoryDstVCNumber = _X25CallHistoryDstVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 8),
    _X25CallHistoryDstVCNumber_Type()
)
x25CallHistoryDstVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryDstVCNumber.setStatus("mandatory")
_X25CallHistorySrcAddr_Type = DisplayString
_X25CallHistorySrcAddr_Object = MibTableColumn
x25CallHistorySrcAddr = _X25CallHistorySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 9),
    _X25CallHistorySrcAddr_Type()
)
x25CallHistorySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistorySrcAddr.setStatus("mandatory")
_X25CallHistoryDstAddr_Type = DisplayString
_X25CallHistoryDstAddr_Object = MibTableColumn
x25CallHistoryDstAddr = _X25CallHistoryDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 10),
    _X25CallHistoryDstAddr_Type()
)
x25CallHistoryDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryDstAddr.setStatus("mandatory")
_X25CallHistoryProtocolId_Type = Integer32
_X25CallHistoryProtocolId_Object = MibTableColumn
x25CallHistoryProtocolId = _X25CallHistoryProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 11),
    _X25CallHistoryProtocolId_Type()
)
x25CallHistoryProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryProtocolId.setStatus("mandatory")
_X25CallHistoryFacilities_Type = OctetString
_X25CallHistoryFacilities_Object = MibTableColumn
x25CallHistoryFacilities = _X25CallHistoryFacilities_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 12),
    _X25CallHistoryFacilities_Type()
)
x25CallHistoryFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryFacilities.setStatus("mandatory")
_X25CallHistoryUserData_Type = DisplayString
_X25CallHistoryUserData_Object = MibTableColumn
x25CallHistoryUserData = _X25CallHistoryUserData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 13),
    _X25CallHistoryUserData_Type()
)
x25CallHistoryUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryUserData.setStatus("mandatory")


class _X25CallHistoryInPktSize_Type(Integer32):
    """Custom type x25CallHistoryInPktSize based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p16", 4),
          ("p16384", 14),
          ("p2", 1),
          ("p2048", 11),
          ("p256", 8),
          ("p32", 5),
          ("p32768", 15),
          ("p4", 2),
          ("p4096", 12),
          ("p512", 9),
          ("p64", 6),
          ("p8", 3),
          ("p8192", 13))
    )


_X25CallHistoryInPktSize_Type.__name__ = "Integer32"
_X25CallHistoryInPktSize_Object = MibTableColumn
x25CallHistoryInPktSize = _X25CallHistoryInPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 14),
    _X25CallHistoryInPktSize_Type()
)
x25CallHistoryInPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryInPktSize.setStatus("mandatory")


class _X25CallHistoryOutPktSize_Type(Integer32):
    """Custom type x25CallHistoryOutPktSize based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p16", 4),
          ("p16384", 14),
          ("p2", 1),
          ("p2048", 11),
          ("p256", 8),
          ("p32", 5),
          ("p32768", 15),
          ("p4", 2),
          ("p4096", 12),
          ("p512", 9),
          ("p64", 6),
          ("p8", 3),
          ("p8192", 13))
    )


_X25CallHistoryOutPktSize_Type.__name__ = "Integer32"
_X25CallHistoryOutPktSize_Object = MibTableColumn
x25CallHistoryOutPktSize = _X25CallHistoryOutPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 15),
    _X25CallHistoryOutPktSize_Type()
)
x25CallHistoryOutPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryOutPktSize.setStatus("mandatory")


class _X25CallHistoryInWinSize_Type(Integer32):
    """Custom type x25CallHistoryInWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CallHistoryInWinSize_Type.__name__ = "Integer32"
_X25CallHistoryInWinSize_Object = MibTableColumn
x25CallHistoryInWinSize = _X25CallHistoryInWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 16),
    _X25CallHistoryInWinSize_Type()
)
x25CallHistoryInWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryInWinSize.setStatus("mandatory")


class _X25CallHistoryOutWinSize_Type(Integer32):
    """Custom type x25CallHistoryOutWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CallHistoryOutWinSize_Type.__name__ = "Integer32"
_X25CallHistoryOutWinSize_Object = MibTableColumn
x25CallHistoryOutWinSize = _X25CallHistoryOutWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 17),
    _X25CallHistoryOutWinSize_Type()
)
x25CallHistoryOutWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryOutWinSize.setStatus("mandatory")
_X25CallHistoryPktsSent_Type = Counter32
_X25CallHistoryPktsSent_Object = MibTableColumn
x25CallHistoryPktsSent = _X25CallHistoryPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 18),
    _X25CallHistoryPktsSent_Type()
)
x25CallHistoryPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryPktsSent.setStatus("mandatory")
_X25CallHistoryBytesSent_Type = Counter32
_X25CallHistoryBytesSent_Object = MibTableColumn
x25CallHistoryBytesSent = _X25CallHistoryBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 19),
    _X25CallHistoryBytesSent_Type()
)
x25CallHistoryBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryBytesSent.setStatus("mandatory")
_X25CallHistoryPktsRecvd_Type = Counter32
_X25CallHistoryPktsRecvd_Object = MibTableColumn
x25CallHistoryPktsRecvd = _X25CallHistoryPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 20),
    _X25CallHistoryPktsRecvd_Type()
)
x25CallHistoryPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryPktsRecvd.setStatus("mandatory")
_X25CallHistoryBytesRecvd_Type = Counter32
_X25CallHistoryBytesRecvd_Object = MibTableColumn
x25CallHistoryBytesRecvd = _X25CallHistoryBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 21),
    _X25CallHistoryBytesRecvd_Type()
)
x25CallHistoryBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryBytesRecvd.setStatus("mandatory")


class _X25CallHistoryClearCause_Type(Integer32):
    """Custom type x25CallHistoryClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_X25CallHistoryClearCause_Type.__name__ = "Integer32"
_X25CallHistoryClearCause_Object = MibTableColumn
x25CallHistoryClearCause = _X25CallHistoryClearCause_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 22),
    _X25CallHistoryClearCause_Type()
)
x25CallHistoryClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryClearCause.setStatus("mandatory")


class _X25CallHistoryClearDiag_Type(Integer32):
    """Custom type x25CallHistoryClearDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_X25CallHistoryClearDiag_Type.__name__ = "Integer32"
_X25CallHistoryClearDiag_Object = MibTableColumn
x25CallHistoryClearDiag = _X25CallHistoryClearDiag_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 4, 1, 23),
    _X25CallHistoryClearDiag_Type()
)
x25CallHistoryClearDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallHistoryClearDiag.setStatus("mandatory")
_X25RouteTable_Object = MibTable
x25RouteTable = _X25RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5)
)
if mibBuilder.loadTexts:
    x25RouteTable.setStatus("mandatory")
_X25RouteEntry_Object = MibTableRow
x25RouteEntry = _X25RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1)
)
x25RouteEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25RtSrcIfIndex"),
    (0, "BIANCA-BRICK-X25-MIB", "x25RtDstIfIndex"),
)
if mibBuilder.loadTexts:
    x25RouteEntry.setStatus("mandatory")
_X25RtSrcIfIndex_Type = Integer32
_X25RtSrcIfIndex_Object = MibTableColumn
x25RtSrcIfIndex = _X25RtSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 1),
    _X25RtSrcIfIndex_Type()
)
x25RtSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtSrcIfIndex.setStatus("mandatory")
_X25RtSrcLinkAddr_Type = OctetString
_X25RtSrcLinkAddr_Object = MibTableColumn
x25RtSrcLinkAddr = _X25RtSrcLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 2),
    _X25RtSrcLinkAddr_Type()
)
x25RtSrcLinkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtSrcLinkAddr.setStatus("mandatory")
_X25RtDstIfIndex_Type = Integer32
_X25RtDstIfIndex_Object = MibTableColumn
x25RtDstIfIndex = _X25RtDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 3),
    _X25RtDstIfIndex_Type()
)
x25RtDstIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtDstIfIndex.setStatus("mandatory")
_X25RtDstLinkAddr_Type = OctetString
_X25RtDstLinkAddr_Object = MibTableColumn
x25RtDstLinkAddr = _X25RtDstLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 4),
    _X25RtDstLinkAddr_Type()
)
x25RtDstLinkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtDstLinkAddr.setStatus("mandatory")


class _X25RtDstLinkAddrMode_Type(Integer32):
    """Custom type x25RtDstLinkAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 5),
          ("default", 1),
          ("delete", 3),
          ("direct", 2),
          ("rule", 4))
    )


_X25RtDstLinkAddrMode_Type.__name__ = "Integer32"
_X25RtDstLinkAddrMode_Object = MibScalar
x25RtDstLinkAddrMode = _X25RtDstLinkAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 5),
    _X25RtDstLinkAddrMode_Type()
)
x25RtDstLinkAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtDstLinkAddrMode.setStatus("mandatory")
_X25RtSrcAddr_Type = DisplayString
_X25RtSrcAddr_Object = MibTableColumn
x25RtSrcAddr = _X25RtSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 6),
    _X25RtSrcAddr_Type()
)
x25RtSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtSrcAddr.setStatus("mandatory")
_X25RtSrcNSAP_Type = DisplayString
_X25RtSrcNSAP_Object = MibTableColumn
x25RtSrcNSAP = _X25RtSrcNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 7),
    _X25RtSrcNSAP_Type()
)
x25RtSrcNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtSrcNSAP.setStatus("mandatory")
_X25RtDstAddr_Type = DisplayString
_X25RtDstAddr_Object = MibTableColumn
x25RtDstAddr = _X25RtDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 8),
    _X25RtDstAddr_Type()
)
x25RtDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtDstAddr.setStatus("mandatory")
_X25RtDstNSAP_Type = DisplayString
_X25RtDstNSAP_Object = MibTableColumn
x25RtDstNSAP = _X25RtDstNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 9),
    _X25RtDstNSAP_Type()
)
x25RtDstNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtDstNSAP.setStatus("mandatory")
_X25RtProtocolId_Type = Integer32
_X25RtProtocolId_Object = MibTableColumn
x25RtProtocolId = _X25RtProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 10),
    _X25RtProtocolId_Type()
)
x25RtProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtProtocolId.setStatus("mandatory")
_X25RtCallUserData_Type = OctetString
_X25RtCallUserData_Object = MibTableColumn
x25RtCallUserData = _X25RtCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 11),
    _X25RtCallUserData_Type()
)
x25RtCallUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtCallUserData.setStatus("mandatory")


class _X25RtRPOA_Type(Integer32):
    """Custom type x25RtRPOA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9999),
    )


_X25RtRPOA_Type.__name__ = "Integer32"
_X25RtRPOA_Object = MibTableColumn
x25RtRPOA = _X25RtRPOA_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 12),
    _X25RtRPOA_Type()
)
x25RtRPOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtRPOA.setStatus("mandatory")
_X25RtNUI_Type = DisplayString
_X25RtNUI_Object = MibTableColumn
x25RtNUI = _X25RtNUI_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 13),
    _X25RtNUI_Type()
)
x25RtNUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtNUI.setStatus("mandatory")


class _X25RtRewritingRule_Type(Integer32):
    """Custom type x25RtRewritingRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_X25RtRewritingRule_Type.__name__ = "Integer32"
_X25RtRewritingRule_Object = MibTableColumn
x25RtRewritingRule = _X25RtRewritingRule_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 14),
    _X25RtRewritingRule_Type()
)
x25RtRewritingRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtRewritingRule.setStatus("mandatory")


class _X25RtMetric_Type(Integer32):
    """Custom type x25RtMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25RtMetric_Type.__name__ = "Integer32"
_X25RtMetric_Object = MibTableColumn
x25RtMetric = _X25RtMetric_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 15),
    _X25RtMetric_Type()
)
x25RtMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtMetric.setStatus("mandatory")


class _X25RtCug_Type(Integer32):
    """Custom type x25RtCug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9999),
    )


_X25RtCug_Type.__name__ = "Integer32"
_X25RtCug_Object = MibTableColumn
x25RtCug = _X25RtCug_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 16),
    _X25RtCug_Type()
)
x25RtCug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtCug.setStatus("mandatory")


class _X25RtCugOutgoing_Type(Integer32):
    """Custom type x25RtCugOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9999),
    )


_X25RtCugOutgoing_Type.__name__ = "Integer32"
_X25RtCugOutgoing_Object = MibTableColumn
x25RtCugOutgoing = _X25RtCugOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 17),
    _X25RtCugOutgoing_Type()
)
x25RtCugOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtCugOutgoing.setStatus("mandatory")


class _X25RtCugBilateral_Type(Integer32):
    """Custom type x25RtCugBilateral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9999),
    )


_X25RtCugBilateral_Type.__name__ = "Integer32"
_X25RtCugBilateral_Object = MibTableColumn
x25RtCugBilateral = _X25RtCugBilateral_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 5, 1, 18),
    _X25RtCugBilateral_Type()
)
x25RtCugBilateral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RtCugBilateral.setStatus("mandatory")
_X25RewriteTable_Object = MibTable
x25RewriteTable = _X25RewriteTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6)
)
if mibBuilder.loadTexts:
    x25RewriteTable.setStatus("mandatory")
_X25RewriteEntry_Object = MibTableRow
x25RewriteEntry = _X25RewriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1)
)
x25RewriteEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25RwRewritingRule"),
)
if mibBuilder.loadTexts:
    x25RewriteEntry.setStatus("mandatory")


class _X25RwRewritingRule_Type(Integer32):
    """Custom type x25RwRewritingRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_X25RwRewritingRule_Type.__name__ = "Integer32"
_X25RwRewritingRule_Object = MibTableColumn
x25RwRewritingRule = _X25RwRewritingRule_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 1),
    _X25RwRewritingRule_Type()
)
x25RwRewritingRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRewritingRule.setStatus("mandatory")


class _X25RwReverseCharging_Type(Integer32):
    """Custom type x25RwReverseCharging based on Integer32"""
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
        *(("clear", 3),
          ("delete", 4),
          ("dont-change", 1),
          ("set", 2))
    )


_X25RwReverseCharging_Type.__name__ = "Integer32"
_X25RwReverseCharging_Object = MibTableColumn
x25RwReverseCharging = _X25RwReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 2),
    _X25RwReverseCharging_Type()
)
x25RwReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwReverseCharging.setStatus("mandatory")


class _X25RwRPOA_Type(Integer32):
    """Custom type x25RwRPOA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-change", 1),
          ("remove-first", 2))
    )


_X25RwRPOA_Type.__name__ = "Integer32"
_X25RwRPOA_Object = MibTableColumn
x25RwRPOA = _X25RwRPOA_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 3),
    _X25RwRPOA_Type()
)
x25RwRPOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRPOA.setStatus("mandatory")
_X25RwNUI_Type = DisplayString
_X25RwNUI_Object = MibTableColumn
x25RwNUI = _X25RwNUI_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 4),
    _X25RwNUI_Type()
)
x25RwNUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwNUI.setStatus("mandatory")
_X25RwSrcAddr_Type = DisplayString
_X25RwSrcAddr_Object = MibTableColumn
x25RwSrcAddr = _X25RwSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 5),
    _X25RwSrcAddr_Type()
)
x25RwSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwSrcAddr.setStatus("mandatory")
_X25RwSrcNSAP_Type = DisplayString
_X25RwSrcNSAP_Object = MibTableColumn
x25RwSrcNSAP = _X25RwSrcNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 6),
    _X25RwSrcNSAP_Type()
)
x25RwSrcNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwSrcNSAP.setStatus("mandatory")
_X25RwDstAddr_Type = DisplayString
_X25RwDstAddr_Object = MibTableColumn
x25RwDstAddr = _X25RwDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 7),
    _X25RwDstAddr_Type()
)
x25RwDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwDstAddr.setStatus("mandatory")
_X25RwDstNSAP_Type = DisplayString
_X25RwDstNSAP_Object = MibTableColumn
x25RwDstNSAP = _X25RwDstNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 8),
    _X25RwDstNSAP_Type()
)
x25RwDstNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwDstNSAP.setStatus("mandatory")
_X25RwProtocolId_Type = Integer32
_X25RwProtocolId_Object = MibTableColumn
x25RwProtocolId = _X25RwProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 9),
    _X25RwProtocolId_Type()
)
x25RwProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwProtocolId.setStatus("mandatory")
_X25RwCallUserData_Type = OctetString
_X25RwCallUserData_Object = MibTableColumn
x25RwCallUserData = _X25RwCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 10),
    _X25RwCallUserData_Type()
)
x25RwCallUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwCallUserData.setStatus("mandatory")
_X25RwRespSrcAddr_Type = DisplayString
_X25RwRespSrcAddr_Object = MibTableColumn
x25RwRespSrcAddr = _X25RwRespSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 11),
    _X25RwRespSrcAddr_Type()
)
x25RwRespSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespSrcAddr.setStatus("mandatory")
_X25RwRespSrcNSAP_Type = DisplayString
_X25RwRespSrcNSAP_Object = MibTableColumn
x25RwRespSrcNSAP = _X25RwRespSrcNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 12),
    _X25RwRespSrcNSAP_Type()
)
x25RwRespSrcNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespSrcNSAP.setStatus("mandatory")
_X25RwRespDstAddr_Type = DisplayString
_X25RwRespDstAddr_Object = MibTableColumn
x25RwRespDstAddr = _X25RwRespDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 13),
    _X25RwRespDstAddr_Type()
)
x25RwRespDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespDstAddr.setStatus("mandatory")
_X25RwRespDstNSAP_Type = DisplayString
_X25RwRespDstNSAP_Object = MibTableColumn
x25RwRespDstNSAP = _X25RwRespDstNSAP_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 14),
    _X25RwRespDstNSAP_Type()
)
x25RwRespDstNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespDstNSAP.setStatus("mandatory")
_X25RwRespProtocolId_Type = Integer32
_X25RwRespProtocolId_Object = MibTableColumn
x25RwRespProtocolId = _X25RwRespProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 15),
    _X25RwRespProtocolId_Type()
)
x25RwRespProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespProtocolId.setStatus("mandatory")
_X25RwRespCallUserData_Type = OctetString
_X25RwRespCallUserData_Object = MibTableColumn
x25RwRespCallUserData = _X25RwRespCallUserData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 16),
    _X25RwRespCallUserData_Type()
)
x25RwRespCallUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwRespCallUserData.setStatus("mandatory")


class _X25RwCug_Type(Integer32):
    """Custom type x25RwCug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 9999),
    )


_X25RwCug_Type.__name__ = "Integer32"
_X25RwCug_Object = MibTableColumn
x25RwCug = _X25RwCug_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 17),
    _X25RwCug_Type()
)
x25RwCug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwCug.setStatus("mandatory")


class _X25RwCugOutgoing_Type(Integer32):
    """Custom type x25RwCugOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 9999),
    )


_X25RwCugOutgoing_Type.__name__ = "Integer32"
_X25RwCugOutgoing_Object = MibTableColumn
x25RwCugOutgoing = _X25RwCugOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 18),
    _X25RwCugOutgoing_Type()
)
x25RwCugOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwCugOutgoing.setStatus("mandatory")


class _X25RwCugBilateral_Type(Integer32):
    """Custom type x25RwCugBilateral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 9999),
    )


_X25RwCugBilateral_Type.__name__ = "Integer32"
_X25RwCugBilateral_Object = MibTableColumn
x25RwCugBilateral = _X25RwCugBilateral_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 19),
    _X25RwCugBilateral_Type()
)
x25RwCugBilateral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwCugBilateral.setStatus("mandatory")
_X25RwDstLinkAddr_Type = DisplayString
_X25RwDstLinkAddr_Object = MibTableColumn
x25RwDstLinkAddr = _X25RwDstLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 6, 1, 20),
    _X25RwDstLinkAddr_Type()
)
x25RwDstLinkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RwDstLinkAddr.setStatus("mandatory")
_X25MprTable_Object = MibTable
x25MprTable = _X25MprTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7)
)
if mibBuilder.loadTexts:
    x25MprTable.setStatus("mandatory")
_X25MprEntry_Object = MibTableRow
x25MprEntry = _X25MprEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1)
)
x25MprEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25-MIB", "x25MprIfIndex"),
)
if mibBuilder.loadTexts:
    x25MprEntry.setStatus("mandatory")
_X25MprIfIndex_Type = Integer32
_X25MprIfIndex_Object = MibTableColumn
x25MprIfIndex = _X25MprIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 1),
    _X25MprIfIndex_Type()
)
x25MprIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprIfIndex.setStatus("mandatory")


class _X25MprMtu_Type(Integer32):
    """Custom type x25MprMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 8180),
    )


_X25MprMtu_Type.__name__ = "Integer32"
_X25MprMtu_Object = MibTableColumn
x25MprMtu = _X25MprMtu_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 2),
    _X25MprMtu_Type()
)
x25MprMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprMtu.setStatus("mandatory")


class _X25MprEncapsulation_Type(Integer32):
    """Custom type x25MprEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("delete", 5),
          ("ip", 2),
          ("ip-rfc877", 1),
          ("ipx", 3),
          ("mpr", 4))
    )


_X25MprEncapsulation_Type.__name__ = "Integer32"
_X25MprEncapsulation_Object = MibTableColumn
x25MprEncapsulation = _X25MprEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 3),
    _X25MprEncapsulation_Type()
)
x25MprEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprEncapsulation.setStatus("mandatory")


class _X25MprNumVC_Type(Integer32):
    """Custom type x25MprNumVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25MprNumVC_Type.__name__ = "Integer32"
_X25MprNumVC_Object = MibTableColumn
x25MprNumVC = _X25MprNumVC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 4),
    _X25MprNumVC_Type()
)
x25MprNumVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprNumVC.setStatus("mandatory")


class _X25MprMaxVC_Type(Integer32):
    """Custom type x25MprMaxVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25MprMaxVC_Type.__name__ = "Integer32"
_X25MprMaxVC_Object = MibTableColumn
x25MprMaxVC = _X25MprMaxVC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 5),
    _X25MprMaxVC_Type()
)
x25MprMaxVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprMaxVC.setStatus("mandatory")


class _X25MprWinSize_Type(Integer32):
    """Custom type x25MprWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_X25MprWinSize_Type.__name__ = "Integer32"
_X25MprWinSize_Object = MibTableColumn
x25MprWinSize = _X25MprWinSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 6),
    _X25MprWinSize_Type()
)
x25MprWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprWinSize.setStatus("mandatory")


class _X25MprPktSize_Type(Integer32):
    """Custom type x25MprPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("p1024", 10),
          ("p128", 7),
          ("p2048", 11),
          ("p256", 8),
          ("p4096", 12),
          ("p512", 9))
    )


_X25MprPktSize_Type.__name__ = "Integer32"
_X25MprPktSize_Object = MibTableColumn
x25MprPktSize = _X25MprPktSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 7),
    _X25MprPktSize_Type()
)
x25MprPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprPktSize.setStatus("mandatory")


class _X25MprShortHold_Type(Integer32):
    """Custom type x25MprShortHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25MprShortHold_Type.__name__ = "Integer32"
_X25MprShortHold_Object = MibTableColumn
x25MprShortHold = _X25MprShortHold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 8),
    _X25MprShortHold_Type()
)
x25MprShortHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprShortHold.setStatus("mandatory")


class _X25MprMaxRetries_Type(Integer32):
    """Custom type x25MprMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_X25MprMaxRetries_Type.__name__ = "Integer32"
_X25MprMaxRetries_Object = MibTableColumn
x25MprMaxRetries = _X25MprMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 9),
    _X25MprMaxRetries_Type()
)
x25MprMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprMaxRetries.setStatus("mandatory")


class _X25MprBlockTime_Type(Integer32):
    """Custom type x25MprBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_X25MprBlockTime_Type.__name__ = "Integer32"
_X25MprBlockTime_Object = MibTableColumn
x25MprBlockTime = _X25MprBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 10),
    _X25MprBlockTime_Type()
)
x25MprBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprBlockTime.setStatus("mandatory")
_X25MprAddr_Type = DisplayString
_X25MprAddr_Object = MibTableColumn
x25MprAddr = _X25MprAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 7, 1, 11),
    _X25MprAddr_Type()
)
x25MprAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25MprAddr.setStatus("mandatory")


class _X25LocalPadCall_Type(Integer32):
    """Custom type x25LocalPadCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dont-accept", 2))
    )


_X25LocalPadCall_Type.__name__ = "Integer32"
_X25LocalPadCall_Object = MibScalar
x25LocalPadCall = _X25LocalPadCall_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 10),
    _X25LocalPadCall_Type()
)
x25LocalPadCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LocalPadCall.setStatus("mandatory")
_X25LocalAddr_Type = DisplayString
_X25LocalAddr_Object = MibScalar
x25LocalAddr = _X25LocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 11),
    _X25LocalAddr_Type()
)
x25LocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LocalAddr.setStatus("mandatory")


class _X25Rerouting_Type(Integer32):
    """Custom type x25Rerouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_X25Rerouting_Type.__name__ = "Integer32"
_X25Rerouting_Object = MibScalar
x25Rerouting = _X25Rerouting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 12),
    _X25Rerouting_Type()
)
x25Rerouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Rerouting.setStatus("mandatory")


class _X25HistoryMaxEntries_Type(Integer32):
    """Custom type x25HistoryMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25HistoryMaxEntries_Type.__name__ = "Integer32"
_X25HistoryMaxEntries_Object = MibScalar
x25HistoryMaxEntries = _X25HistoryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 13),
    _X25HistoryMaxEntries_Type()
)
x25HistoryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25HistoryMaxEntries.setStatus("mandatory")


class _X25AccountingTemplate_Type(DisplayString):
    """Custom type x25AccountingTemplate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_X25AccountingTemplate_Type.__name__ = "DisplayString"
_X25AccountingTemplate_Object = MibScalar
x25AccountingTemplate = _X25AccountingTemplate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 14),
    _X25AccountingTemplate_Type()
)
x25AccountingTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AccountingTemplate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-X25-MIB",
    **{"HexValue": HexValue,
       "Date": Date,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "x25": x25,
       "x25LinkTable": x25LinkTable,
       "x25LinkEntry": x25LinkEntry,
       "x25LkIfIndex": x25LkIfIndex,
       "x25LkAddr": x25LkAddr,
       "x25LkMode": x25LkMode,
       "x25LkModulo": x25LkModulo,
       "x25LkLIC": x25LkLIC,
       "x25LkHIC": x25LkHIC,
       "x25LkLTC": x25LkLTC,
       "x25LkHTC": x25LkHTC,
       "x25LkLOC": x25LkLOC,
       "x25LkHOC": x25LkHOC,
       "x25LkDefPktSize": x25LkDefPktSize,
       "x25LkDefWinSize": x25LkDefWinSize,
       "x25LkMaxPktSize": x25LkMaxPktSize,
       "x25LkMaxWinSize": x25LkMaxWinSize,
       "x25LkL2WinSize": x25LkL2WinSize,
       "x25LkL2RetrTimer": x25LkL2RetrTimer,
       "x25LkL2RetrCounter": x25LkL2RetrCounter,
       "x25LkL2SupervTimer": x25LkL2SupervTimer,
       "x25LkL2IdleTimer": x25LkL2IdleTimer,
       "x25LkState": x25LkState,
       "x25LkNegotiation": x25LkNegotiation,
       "x25LkDiscDelayTimer": x25LkDiscDelayTimer,
       "x25LkCallDelayTimer": x25LkCallDelayTimer,
       "x25LkRestDelayTimer": x25LkRestDelayTimer,
       "x25LinkPresetTable": x25LinkPresetTable,
       "x25LinkPresetEntry": x25LinkPresetEntry,
       "x25LkPrIfIndex": x25LkPrIfIndex,
       "x25LkPrAddr": x25LkPrAddr,
       "x25LkPrMode": x25LkPrMode,
       "x25LkPrModulo": x25LkPrModulo,
       "x25LkPrLIC": x25LkPrLIC,
       "x25LkPrHIC": x25LkPrHIC,
       "x25LkPrLTC": x25LkPrLTC,
       "x25LkPrHTC": x25LkPrHTC,
       "x25LkPrLOC": x25LkPrLOC,
       "x25LkPrHOC": x25LkPrHOC,
       "x25LkPrDefPktSize": x25LkPrDefPktSize,
       "x25LkPrDefWinSize": x25LkPrDefWinSize,
       "x25LkPrMaxPktSize": x25LkPrMaxPktSize,
       "x25LkPrMaxWinSize": x25LkPrMaxWinSize,
       "x25LkPrL2WinSize": x25LkPrL2WinSize,
       "x25LkPrL2RetrTimer": x25LkPrL2RetrTimer,
       "x25LkPrL2RetrCounter": x25LkPrL2RetrCounter,
       "x25LkPrL2SupervTimer": x25LkPrL2SupervTimer,
       "x25LkPrL2IdleTimer": x25LkPrL2IdleTimer,
       "x25LkPrNegotiation": x25LkPrNegotiation,
       "x25LkPrDiscDelayTimer": x25LkPrDiscDelayTimer,
       "x25LkPrCallDelayTimer": x25LkPrCallDelayTimer,
       "x25LkPrRestDelayTimer": x25LkPrRestDelayTimer,
       "x25CallTable": x25CallTable,
       "x25CallEntry": x25CallEntry,
       "x25CallSrcIfIndex": x25CallSrcIfIndex,
       "x25CallSrcLinkAddr": x25CallSrcLinkAddr,
       "x25CallSrcVCNumber": x25CallSrcVCNumber,
       "x25CallDstIfIndex": x25CallDstIfIndex,
       "x25CallDstLinkAddr": x25CallDstLinkAddr,
       "x25CallDstVCNumber": x25CallDstVCNumber,
       "x25CallSrcAddr": x25CallSrcAddr,
       "x25CallDstAddr": x25CallDstAddr,
       "x25CallProtocolId": x25CallProtocolId,
       "x25CallFacilities": x25CallFacilities,
       "x25CallUserData": x25CallUserData,
       "x25CallAge": x25CallAge,
       "x25CallState": x25CallState,
       "x25CallInPktSize": x25CallInPktSize,
       "x25CallOutPktSize": x25CallOutPktSize,
       "x25CallInWinSize": x25CallInWinSize,
       "x25CallOutWinSize": x25CallOutWinSize,
       "x25CallPktsSent": x25CallPktsSent,
       "x25CallBytesSent": x25CallBytesSent,
       "x25CallPktsRecvd": x25CallPktsRecvd,
       "x25CallBytesRecvd": x25CallBytesRecvd,
       "x25CallHistoryTable": x25CallHistoryTable,
       "x25CallHistoryEntry": x25CallHistoryEntry,
       "x25CallHistoryTime": x25CallHistoryTime,
       "x25CallHistoryDuration": x25CallHistoryDuration,
       "x25CallHistorySrcIfIndex": x25CallHistorySrcIfIndex,
       "x25CallHistorySrcLinkAddr": x25CallHistorySrcLinkAddr,
       "x25CallHistorySrcVCNumber": x25CallHistorySrcVCNumber,
       "x25CallHistoryDstIfIndex": x25CallHistoryDstIfIndex,
       "x25CallHistoryDstLinkAddr": x25CallHistoryDstLinkAddr,
       "x25CallHistoryDstVCNumber": x25CallHistoryDstVCNumber,
       "x25CallHistorySrcAddr": x25CallHistorySrcAddr,
       "x25CallHistoryDstAddr": x25CallHistoryDstAddr,
       "x25CallHistoryProtocolId": x25CallHistoryProtocolId,
       "x25CallHistoryFacilities": x25CallHistoryFacilities,
       "x25CallHistoryUserData": x25CallHistoryUserData,
       "x25CallHistoryInPktSize": x25CallHistoryInPktSize,
       "x25CallHistoryOutPktSize": x25CallHistoryOutPktSize,
       "x25CallHistoryInWinSize": x25CallHistoryInWinSize,
       "x25CallHistoryOutWinSize": x25CallHistoryOutWinSize,
       "x25CallHistoryPktsSent": x25CallHistoryPktsSent,
       "x25CallHistoryBytesSent": x25CallHistoryBytesSent,
       "x25CallHistoryPktsRecvd": x25CallHistoryPktsRecvd,
       "x25CallHistoryBytesRecvd": x25CallHistoryBytesRecvd,
       "x25CallHistoryClearCause": x25CallHistoryClearCause,
       "x25CallHistoryClearDiag": x25CallHistoryClearDiag,
       "x25RouteTable": x25RouteTable,
       "x25RouteEntry": x25RouteEntry,
       "x25RtSrcIfIndex": x25RtSrcIfIndex,
       "x25RtSrcLinkAddr": x25RtSrcLinkAddr,
       "x25RtDstIfIndex": x25RtDstIfIndex,
       "x25RtDstLinkAddr": x25RtDstLinkAddr,
       "x25RtDstLinkAddrMode": x25RtDstLinkAddrMode,
       "x25RtSrcAddr": x25RtSrcAddr,
       "x25RtSrcNSAP": x25RtSrcNSAP,
       "x25RtDstAddr": x25RtDstAddr,
       "x25RtDstNSAP": x25RtDstNSAP,
       "x25RtProtocolId": x25RtProtocolId,
       "x25RtCallUserData": x25RtCallUserData,
       "x25RtRPOA": x25RtRPOA,
       "x25RtNUI": x25RtNUI,
       "x25RtRewritingRule": x25RtRewritingRule,
       "x25RtMetric": x25RtMetric,
       "x25RtCug": x25RtCug,
       "x25RtCugOutgoing": x25RtCugOutgoing,
       "x25RtCugBilateral": x25RtCugBilateral,
       "x25RewriteTable": x25RewriteTable,
       "x25RewriteEntry": x25RewriteEntry,
       "x25RwRewritingRule": x25RwRewritingRule,
       "x25RwReverseCharging": x25RwReverseCharging,
       "x25RwRPOA": x25RwRPOA,
       "x25RwNUI": x25RwNUI,
       "x25RwSrcAddr": x25RwSrcAddr,
       "x25RwSrcNSAP": x25RwSrcNSAP,
       "x25RwDstAddr": x25RwDstAddr,
       "x25RwDstNSAP": x25RwDstNSAP,
       "x25RwProtocolId": x25RwProtocolId,
       "x25RwCallUserData": x25RwCallUserData,
       "x25RwRespSrcAddr": x25RwRespSrcAddr,
       "x25RwRespSrcNSAP": x25RwRespSrcNSAP,
       "x25RwRespDstAddr": x25RwRespDstAddr,
       "x25RwRespDstNSAP": x25RwRespDstNSAP,
       "x25RwRespProtocolId": x25RwRespProtocolId,
       "x25RwRespCallUserData": x25RwRespCallUserData,
       "x25RwCug": x25RwCug,
       "x25RwCugOutgoing": x25RwCugOutgoing,
       "x25RwCugBilateral": x25RwCugBilateral,
       "x25RwDstLinkAddr": x25RwDstLinkAddr,
       "x25MprTable": x25MprTable,
       "x25MprEntry": x25MprEntry,
       "x25MprIfIndex": x25MprIfIndex,
       "x25MprMtu": x25MprMtu,
       "x25MprEncapsulation": x25MprEncapsulation,
       "x25MprNumVC": x25MprNumVC,
       "x25MprMaxVC": x25MprMaxVC,
       "x25MprWinSize": x25MprWinSize,
       "x25MprPktSize": x25MprPktSize,
       "x25MprShortHold": x25MprShortHold,
       "x25MprMaxRetries": x25MprMaxRetries,
       "x25MprBlockTime": x25MprBlockTime,
       "x25MprAddr": x25MprAddr,
       "x25LocalPadCall": x25LocalPadCall,
       "x25LocalAddr": x25LocalAddr,
       "x25Rerouting": x25Rerouting,
       "x25HistoryMaxEntries": x25HistoryMaxEntries,
       "x25AccountingTemplate": x25AccountingTemplate}
)
