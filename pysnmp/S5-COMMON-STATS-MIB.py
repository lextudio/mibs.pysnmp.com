# SNMP MIB module (S5-COMMON-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-COMMON-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:04 2024
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

(s5Com,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Com")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5CmStat_ObjectIdentity = ObjectIdentity
s5CmStat = _S5CmStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1)
)
_S5CmSNodeTable_Object = MibTable
s5CmSNodeTable = _S5CmSNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1)
)
if mibBuilder.loadTexts:
    s5CmSNodeTable.setStatus("mandatory")
_S5CmSNodeEntry_Object = MibTableRow
s5CmSNodeEntry = _S5CmSNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1)
)
s5CmSNodeEntry.setIndexNames(
    (0, "S5-COMMON-STATS-MIB", "s5CmSNodeIfIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmSNodeBrdIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmSNodePortIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmSNodeMacAddr"),
)
if mibBuilder.loadTexts:
    s5CmSNodeEntry.setStatus("mandatory")


class _S5CmSNodeIfIndx_Type(Integer32):
    """Custom type s5CmSNodeIfIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5CmSNodeIfIndx_Type.__name__ = "Integer32"
_S5CmSNodeIfIndx_Object = MibTableColumn
s5CmSNodeIfIndx = _S5CmSNodeIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1, 1),
    _S5CmSNodeIfIndx_Type()
)
s5CmSNodeIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmSNodeIfIndx.setStatus("mandatory")


class _S5CmSNodeBrdIndx_Type(Integer32):
    """Custom type s5CmSNodeBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5CmSNodeBrdIndx_Type.__name__ = "Integer32"
_S5CmSNodeBrdIndx_Object = MibTableColumn
s5CmSNodeBrdIndx = _S5CmSNodeBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1, 2),
    _S5CmSNodeBrdIndx_Type()
)
s5CmSNodeBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmSNodeBrdIndx.setStatus("mandatory")


class _S5CmSNodePortIndx_Type(Integer32):
    """Custom type s5CmSNodePortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5CmSNodePortIndx_Type.__name__ = "Integer32"
_S5CmSNodePortIndx_Object = MibTableColumn
s5CmSNodePortIndx = _S5CmSNodePortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1, 3),
    _S5CmSNodePortIndx_Type()
)
s5CmSNodePortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmSNodePortIndx.setStatus("mandatory")
_S5CmSNodeMacAddr_Type = MacAddress
_S5CmSNodeMacAddr_Object = MibTableColumn
s5CmSNodeMacAddr = _S5CmSNodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1, 4),
    _S5CmSNodeMacAddr_Type()
)
s5CmSNodeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmSNodeMacAddr.setStatus("mandatory")


class _S5CmSNodeStatus_Type(Integer32):
    """Custom type s5CmSNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("other", 1))
    )


_S5CmSNodeStatus_Type.__name__ = "Integer32"
_S5CmSNodeStatus_Object = MibTableColumn
s5CmSNodeStatus = _S5CmSNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 1, 1, 5),
    _S5CmSNodeStatus_Type()
)
s5CmSNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmSNodeStatus.setStatus("mandatory")
_S5CmFNodeTable_Object = MibTable
s5CmFNodeTable = _S5CmFNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    s5CmFNodeTable.setStatus("mandatory")
_S5CmFNodeEntry_Object = MibTableRow
s5CmFNodeEntry = _S5CmFNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2, 1)
)
s5CmFNodeEntry.setIndexNames(
    (0, "S5-COMMON-STATS-MIB", "s5CmFNodeIfIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmFNodeMacAddr"),
)
if mibBuilder.loadTexts:
    s5CmFNodeEntry.setStatus("mandatory")


class _S5CmFNodeIfIndx_Type(Integer32):
    """Custom type s5CmFNodeIfIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5CmFNodeIfIndx_Type.__name__ = "Integer32"
_S5CmFNodeIfIndx_Object = MibTableColumn
s5CmFNodeIfIndx = _S5CmFNodeIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2, 1, 1),
    _S5CmFNodeIfIndx_Type()
)
s5CmFNodeIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmFNodeIfIndx.setStatus("mandatory")
_S5CmFNodeMacAddr_Type = MacAddress
_S5CmFNodeMacAddr_Object = MibTableColumn
s5CmFNodeMacAddr = _S5CmFNodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2, 1, 2),
    _S5CmFNodeMacAddr_Type()
)
s5CmFNodeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmFNodeMacAddr.setStatus("mandatory")


class _S5CmFNodeBrdIndx_Type(Integer32):
    """Custom type s5CmFNodeBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5CmFNodeBrdIndx_Type.__name__ = "Integer32"
_S5CmFNodeBrdIndx_Object = MibTableColumn
s5CmFNodeBrdIndx = _S5CmFNodeBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2, 1, 3),
    _S5CmFNodeBrdIndx_Type()
)
s5CmFNodeBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmFNodeBrdIndx.setStatus("mandatory")


class _S5CmFNodePortIndx_Type(Integer32):
    """Custom type s5CmFNodePortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5CmFNodePortIndx_Type.__name__ = "Integer32"
_S5CmFNodePortIndx_Object = MibTableColumn
s5CmFNodePortIndx = _S5CmFNodePortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 2, 1, 4),
    _S5CmFNodePortIndx_Type()
)
s5CmFNodePortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmFNodePortIndx.setStatus("mandatory")
_S5CmNetAddrTable_Object = MibTable
s5CmNetAddrTable = _S5CmNetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3)
)
if mibBuilder.loadTexts:
    s5CmNetAddrTable.setStatus("mandatory")
_S5CmNetAddrEntry_Object = MibTableRow
s5CmNetAddrEntry = _S5CmNetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1)
)
s5CmNetAddrEntry.setIndexNames(
    (0, "S5-COMMON-STATS-MIB", "s5CmNetAddrIfIndex"),
    (0, "S5-COMMON-STATS-MIB", "s5CmNetAddrBrdIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmNetAddrPortIndx"),
    (0, "S5-COMMON-STATS-MIB", "s5CmNetAddrMacAddr"),
    (0, "S5-COMMON-STATS-MIB", "s5CmNetAddrNetIndx"),
)
if mibBuilder.loadTexts:
    s5CmNetAddrEntry.setStatus("mandatory")


class _S5CmNetAddrIfIndex_Type(Integer32):
    """Custom type s5CmNetAddrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S5CmNetAddrIfIndex_Type.__name__ = "Integer32"
_S5CmNetAddrIfIndex_Object = MibTableColumn
s5CmNetAddrIfIndex = _S5CmNetAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 1),
    _S5CmNetAddrIfIndex_Type()
)
s5CmNetAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrIfIndex.setStatus("mandatory")


class _S5CmNetAddrBrdIndx_Type(Integer32):
    """Custom type s5CmNetAddrBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5CmNetAddrBrdIndx_Type.__name__ = "Integer32"
_S5CmNetAddrBrdIndx_Object = MibTableColumn
s5CmNetAddrBrdIndx = _S5CmNetAddrBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 2),
    _S5CmNetAddrBrdIndx_Type()
)
s5CmNetAddrBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrBrdIndx.setStatus("mandatory")


class _S5CmNetAddrPortIndx_Type(Integer32):
    """Custom type s5CmNetAddrPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5CmNetAddrPortIndx_Type.__name__ = "Integer32"
_S5CmNetAddrPortIndx_Object = MibTableColumn
s5CmNetAddrPortIndx = _S5CmNetAddrPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 3),
    _S5CmNetAddrPortIndx_Type()
)
s5CmNetAddrPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrPortIndx.setStatus("mandatory")
_S5CmNetAddrMacAddr_Type = MacAddress
_S5CmNetAddrMacAddr_Object = MibTableColumn
s5CmNetAddrMacAddr = _S5CmNetAddrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 4),
    _S5CmNetAddrMacAddr_Type()
)
s5CmNetAddrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrMacAddr.setStatus("mandatory")


class _S5CmNetAddrNetIndx_Type(Integer32):
    """Custom type s5CmNetAddrNetIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5CmNetAddrNetIndx_Type.__name__ = "Integer32"
_S5CmNetAddrNetIndx_Object = MibTableColumn
s5CmNetAddrNetIndx = _S5CmNetAddrNetIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 5),
    _S5CmNetAddrNetIndx_Type()
)
s5CmNetAddrNetIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrNetIndx.setStatus("mandatory")


class _S5CmNetAddrType_Type(Integer32):
    """Custom type s5CmNetAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_S5CmNetAddrType_Type.__name__ = "Integer32"
_S5CmNetAddrType_Object = MibTableColumn
s5CmNetAddrType = _S5CmNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 6),
    _S5CmNetAddrType_Type()
)
s5CmNetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrType.setStatus("mandatory")
_S5CmNetAddrAddr_Type = OctetString
_S5CmNetAddrAddr_Object = MibTableColumn
s5CmNetAddrAddr = _S5CmNetAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 7),
    _S5CmNetAddrAddr_Type()
)
s5CmNetAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrAddr.setStatus("mandatory")
_S5CmNetAddrLastSeen_Type = TimeTicks
_S5CmNetAddrLastSeen_Object = MibTableColumn
s5CmNetAddrLastSeen = _S5CmNetAddrLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 1, 3, 1, 8),
    _S5CmNetAddrLastSeen_Type()
)
s5CmNetAddrLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5CmNetAddrLastSeen.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-COMMON-STATS-MIB",
    **{"s5CmStat": s5CmStat,
       "s5CmSNodeTable": s5CmSNodeTable,
       "s5CmSNodeEntry": s5CmSNodeEntry,
       "s5CmSNodeIfIndx": s5CmSNodeIfIndx,
       "s5CmSNodeBrdIndx": s5CmSNodeBrdIndx,
       "s5CmSNodePortIndx": s5CmSNodePortIndx,
       "s5CmSNodeMacAddr": s5CmSNodeMacAddr,
       "s5CmSNodeStatus": s5CmSNodeStatus,
       "s5CmFNodeTable": s5CmFNodeTable,
       "s5CmFNodeEntry": s5CmFNodeEntry,
       "s5CmFNodeIfIndx": s5CmFNodeIfIndx,
       "s5CmFNodeMacAddr": s5CmFNodeMacAddr,
       "s5CmFNodeBrdIndx": s5CmFNodeBrdIndx,
       "s5CmFNodePortIndx": s5CmFNodePortIndx,
       "s5CmNetAddrTable": s5CmNetAddrTable,
       "s5CmNetAddrEntry": s5CmNetAddrEntry,
       "s5CmNetAddrIfIndex": s5CmNetAddrIfIndex,
       "s5CmNetAddrBrdIndx": s5CmNetAddrBrdIndx,
       "s5CmNetAddrPortIndx": s5CmNetAddrPortIndx,
       "s5CmNetAddrMacAddr": s5CmNetAddrMacAddr,
       "s5CmNetAddrNetIndx": s5CmNetAddrNetIndx,
       "s5CmNetAddrType": s5CmNetAddrType,
       "s5CmNetAddrAddr": s5CmNetAddrAddr,
       "s5CmNetAddrLastSeen": s5CmNetAddrLastSeen}
)
