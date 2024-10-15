# SNMP MIB module (BIANCA-BRICK-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-GRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:26 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23)
)
_GreIfTable_Object = MibTable
greIfTable = _GreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5)
)
if mibBuilder.loadTexts:
    greIfTable.setStatus("mandatory")
_GreIfEntry_Object = MibTableRow
greIfEntry = _GreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1)
)
greIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-GRE-MIB", "greDstIpAddr"),
)
if mibBuilder.loadTexts:
    greIfEntry.setStatus("mandatory")


class _GreIfIndex_Type(Integer32):
    """Custom type greIfIndex based on Integer32"""
    defaultValue = 0


_GreIfIndex_Object = MibTableColumn
greIfIndex = _GreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 1),
    _GreIfIndex_Type()
)
greIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIfIndex.setStatus("mandatory")


class _GreIfDescr_Type(DisplayString):
    """Custom type greIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GreIfDescr_Type.__name__ = "DisplayString"
_GreIfDescr_Object = MibTableColumn
greIfDescr = _GreIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 2),
    _GreIfDescr_Type()
)
greIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greIfDescr.setStatus("mandatory")


class _GreIfMtu_Type(Integer32):
    """Custom type greIfMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_GreIfMtu_Type.__name__ = "Integer32"
_GreIfMtu_Object = MibTableColumn
greIfMtu = _GreIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 3),
    _GreIfMtu_Type()
)
greIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greIfMtu.setStatus("mandatory")
_GreDstIpAddr_Type = IpAddress
_GreDstIpAddr_Object = MibTableColumn
greDstIpAddr = _GreDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 4),
    _GreDstIpAddr_Type()
)
greDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greDstIpAddr.setStatus("mandatory")


class _GreKey_Type(Integer32):
    """Custom type greKey based on Integer32"""
    defaultValue = 0


_GreKey_Object = MibTableColumn
greKey = _GreKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 5),
    _GreKey_Type()
)
greKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greKey.setStatus("mandatory")


class _GreUseKey_Type(Integer32):
    """Custom type greUseKey based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("no", 3),
          ("yes", 2))
    )


_GreUseKey_Type.__name__ = "Integer32"
_GreUseKey_Object = MibTableColumn
greUseKey = _GreUseKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 6),
    _GreUseKey_Type()
)
greUseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greUseKey.setStatus("mandatory")
_GreSrcIpAddr_Type = IpAddress
_GreSrcIpAddr_Object = MibTableColumn
greSrcIpAddr = _GreSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 5, 1, 7),
    _GreSrcIpAddr_Type()
)
greSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greSrcIpAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-GRE-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "vpn": vpn,
       "greIfTable": greIfTable,
       "greIfEntry": greIfEntry,
       "greIfIndex": greIfIndex,
       "greIfDescr": greIfDescr,
       "greIfMtu": greIfMtu,
       "greDstIpAddr": greDstIpAddr,
       "greKey": greKey,
       "greUseKey": greUseKey,
       "greSrcIpAddr": greSrcIpAddr}
)
