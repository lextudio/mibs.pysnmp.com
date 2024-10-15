# SNMP MIB module (BIANCA-BRICK-IP-OLDACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-IP-OLDACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:29 2024
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
_Biboipold_ObjectIdentity = ObjectIdentity
biboipold = _Biboipold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpAllowTable_Object = MibTable
ipAllowTable = _IpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ipAllowTable.setStatus("mandatory")
_IpAllowEntry_Object = MibTableRow
ipAllowEntry = _IpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1)
)
ipAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipAllowProtocolMode"),
    (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipAllowSrcIfIndexMode"),
)
if mibBuilder.loadTexts:
    ipAllowEntry.setStatus("mandatory")


class _IpAllowProtocolMode_Type(Integer32):
    """Custom type ipAllowProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_IpAllowProtocolMode_Type.__name__ = "Integer32"
_IpAllowProtocolMode_Object = MibTableColumn
ipAllowProtocolMode = _IpAllowProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 1),
    _IpAllowProtocolMode_Type()
)
ipAllowProtocolMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowProtocolMode.setStatus("mandatory")


class _IpAllowProtocol_Type(Integer32):
    """Custom type ipAllowProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              8,
              12,
              17,
              20,
              22,
              27,
              89)
        )
    )
    namedValues = NamedValues(
        *(("egp", 8),
          ("ggp", 3),
          ("hmp", 20),
          ("icmp", 1),
          ("ospf", 89),
          ("pup", 12),
          ("rdp", 27),
          ("tcp", 6),
          ("udp", 17),
          ("xns-idp", 22))
    )


_IpAllowProtocol_Type.__name__ = "Integer32"
_IpAllowProtocol_Object = MibTableColumn
ipAllowProtocol = _IpAllowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 2),
    _IpAllowProtocol_Type()
)
ipAllowProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowProtocol.setStatus("mandatory")


class _IpAllowSrcIfIndexMode_Type(Integer32):
    """Custom type ipAllowSrcIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpAllowSrcIfIndexMode_Type.__name__ = "Integer32"
_IpAllowSrcIfIndexMode_Object = MibTableColumn
ipAllowSrcIfIndexMode = _IpAllowSrcIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 3),
    _IpAllowSrcIfIndexMode_Type()
)
ipAllowSrcIfIndexMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcIfIndexMode.setStatus("mandatory")
_IpAllowSrcIfIndex_Type = Integer32
_IpAllowSrcIfIndex_Object = MibTableColumn
ipAllowSrcIfIndex = _IpAllowSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 4),
    _IpAllowSrcIfIndex_Type()
)
ipAllowSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcIfIndex.setStatus("mandatory")
_IpAllowSrcAddr_Type = IpAddress
_IpAllowSrcAddr_Object = MibTableColumn
ipAllowSrcAddr = _IpAllowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 5),
    _IpAllowSrcAddr_Type()
)
ipAllowSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcAddr.setStatus("mandatory")
_IpAllowSrcMask_Type = IpAddress
_IpAllowSrcMask_Object = MibTableColumn
ipAllowSrcMask = _IpAllowSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 6),
    _IpAllowSrcMask_Type()
)
ipAllowSrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcMask.setStatus("mandatory")


class _IpAllowSrcPortMode_Type(Integer32):
    """Custom type ipAllowSrcPortMode based on Integer32"""
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
        *(("clients", 3),
          ("ignore", 1),
          ("priv", 6),
          ("server", 4),
          ("specific", 2),
          ("unpriv", 5))
    )


_IpAllowSrcPortMode_Type.__name__ = "Integer32"
_IpAllowSrcPortMode_Object = MibTableColumn
ipAllowSrcPortMode = _IpAllowSrcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 7),
    _IpAllowSrcPortMode_Type()
)
ipAllowSrcPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcPortMode.setStatus("mandatory")


class _IpAllowSrcPort_Type(Integer32):
    """Custom type ipAllowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpAllowSrcPort_Type.__name__ = "Integer32"
_IpAllowSrcPort_Object = MibTableColumn
ipAllowSrcPort = _IpAllowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 8),
    _IpAllowSrcPort_Type()
)
ipAllowSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcPort.setStatus("mandatory")
_IpAllowDstAddr_Type = IpAddress
_IpAllowDstAddr_Object = MibTableColumn
ipAllowDstAddr = _IpAllowDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 9),
    _IpAllowDstAddr_Type()
)
ipAllowDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowDstAddr.setStatus("mandatory")
_IpAllowDstMask_Type = IpAddress
_IpAllowDstMask_Object = MibTableColumn
ipAllowDstMask = _IpAllowDstMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 10),
    _IpAllowDstMask_Type()
)
ipAllowDstMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowDstMask.setStatus("mandatory")


class _IpAllowDstPortMode_Type(Integer32):
    """Custom type ipAllowDstPortMode based on Integer32"""
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
        *(("clients", 3),
          ("ignore", 1),
          ("priv", 6),
          ("server", 4),
          ("specific", 2),
          ("unpriv", 5))
    )


_IpAllowDstPortMode_Type.__name__ = "Integer32"
_IpAllowDstPortMode_Object = MibTableColumn
ipAllowDstPortMode = _IpAllowDstPortMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 11),
    _IpAllowDstPortMode_Type()
)
ipAllowDstPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowDstPortMode.setStatus("mandatory")


class _IpAllowDstPort_Type(Integer32):
    """Custom type ipAllowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpAllowDstPort_Type.__name__ = "Integer32"
_IpAllowDstPort_Object = MibTableColumn
ipAllowDstPort = _IpAllowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 12),
    _IpAllowDstPort_Type()
)
ipAllowDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowDstPort.setStatus("mandatory")


class _IpAllowSrcPortRange_Type(Integer32):
    """Custom type ipAllowSrcPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpAllowSrcPortRange_Type.__name__ = "Integer32"
_IpAllowSrcPortRange_Object = MibTableColumn
ipAllowSrcPortRange = _IpAllowSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 13),
    _IpAllowSrcPortRange_Type()
)
ipAllowSrcPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowSrcPortRange.setStatus("mandatory")


class _IpAllowDstPortRange_Type(Integer32):
    """Custom type ipAllowDstPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpAllowDstPortRange_Type.__name__ = "Integer32"
_IpAllowDstPortRange_Object = MibTableColumn
ipAllowDstPortRange = _IpAllowDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 14),
    _IpAllowDstPortRange_Type()
)
ipAllowDstPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAllowDstPortRange.setStatus("mandatory")
_IpDenyTable_Object = MibTable
ipDenyTable = _IpDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ipDenyTable.setStatus("mandatory")
_IpDenyEntry_Object = MibTableRow
ipDenyEntry = _IpDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1)
)
ipDenyEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipDenyProtocolMode"),
    (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipDenySrcIfIndexMode"),
)
if mibBuilder.loadTexts:
    ipDenyEntry.setStatus("mandatory")


class _IpDenyProtocolMode_Type(Integer32):
    """Custom type ipDenyProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_IpDenyProtocolMode_Type.__name__ = "Integer32"
_IpDenyProtocolMode_Object = MibTableColumn
ipDenyProtocolMode = _IpDenyProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 1),
    _IpDenyProtocolMode_Type()
)
ipDenyProtocolMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyProtocolMode.setStatus("mandatory")


class _IpDenyProtocol_Type(Integer32):
    """Custom type ipDenyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              8,
              12,
              17,
              20,
              22,
              27,
              89)
        )
    )
    namedValues = NamedValues(
        *(("egp", 8),
          ("ggp", 3),
          ("hmp", 20),
          ("icmp", 1),
          ("ospf", 89),
          ("pup", 12),
          ("rdp", 27),
          ("tcp", 6),
          ("udp", 17),
          ("xns-idp", 22))
    )


_IpDenyProtocol_Type.__name__ = "Integer32"
_IpDenyProtocol_Object = MibTableColumn
ipDenyProtocol = _IpDenyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 2),
    _IpDenyProtocol_Type()
)
ipDenyProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyProtocol.setStatus("mandatory")


class _IpDenySrcIfIndexMode_Type(Integer32):
    """Custom type ipDenySrcIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpDenySrcIfIndexMode_Type.__name__ = "Integer32"
_IpDenySrcIfIndexMode_Object = MibTableColumn
ipDenySrcIfIndexMode = _IpDenySrcIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 3),
    _IpDenySrcIfIndexMode_Type()
)
ipDenySrcIfIndexMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcIfIndexMode.setStatus("mandatory")
_IpDenySrcIfIndex_Type = Integer32
_IpDenySrcIfIndex_Object = MibTableColumn
ipDenySrcIfIndex = _IpDenySrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 4),
    _IpDenySrcIfIndex_Type()
)
ipDenySrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcIfIndex.setStatus("mandatory")
_IpDenySrcAddr_Type = IpAddress
_IpDenySrcAddr_Object = MibTableColumn
ipDenySrcAddr = _IpDenySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 5),
    _IpDenySrcAddr_Type()
)
ipDenySrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcAddr.setStatus("mandatory")
_IpDenySrcMask_Type = IpAddress
_IpDenySrcMask_Object = MibTableColumn
ipDenySrcMask = _IpDenySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 6),
    _IpDenySrcMask_Type()
)
ipDenySrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcMask.setStatus("mandatory")


class _IpDenySrcPortMode_Type(Integer32):
    """Custom type ipDenySrcPortMode based on Integer32"""
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
        *(("clients", 3),
          ("ignore", 1),
          ("priv", 6),
          ("server", 4),
          ("specific", 2),
          ("unpriv", 5))
    )


_IpDenySrcPortMode_Type.__name__ = "Integer32"
_IpDenySrcPortMode_Object = MibTableColumn
ipDenySrcPortMode = _IpDenySrcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 7),
    _IpDenySrcPortMode_Type()
)
ipDenySrcPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcPortMode.setStatus("mandatory")


class _IpDenySrcPort_Type(Integer32):
    """Custom type ipDenySrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpDenySrcPort_Type.__name__ = "Integer32"
_IpDenySrcPort_Object = MibTableColumn
ipDenySrcPort = _IpDenySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 8),
    _IpDenySrcPort_Type()
)
ipDenySrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcPort.setStatus("mandatory")
_IpDenyDstAddr_Type = IpAddress
_IpDenyDstAddr_Object = MibTableColumn
ipDenyDstAddr = _IpDenyDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 9),
    _IpDenyDstAddr_Type()
)
ipDenyDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyDstAddr.setStatus("mandatory")
_IpDenyDstMask_Type = IpAddress
_IpDenyDstMask_Object = MibTableColumn
ipDenyDstMask = _IpDenyDstMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 10),
    _IpDenyDstMask_Type()
)
ipDenyDstMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyDstMask.setStatus("mandatory")


class _IpDenyDstPortMode_Type(Integer32):
    """Custom type ipDenyDstPortMode based on Integer32"""
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
        *(("clients", 3),
          ("ignore", 1),
          ("priv", 6),
          ("server", 4),
          ("specific", 2),
          ("unpriv", 5))
    )


_IpDenyDstPortMode_Type.__name__ = "Integer32"
_IpDenyDstPortMode_Object = MibTableColumn
ipDenyDstPortMode = _IpDenyDstPortMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 11),
    _IpDenyDstPortMode_Type()
)
ipDenyDstPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyDstPortMode.setStatus("mandatory")


class _IpDenyDstPort_Type(Integer32):
    """Custom type ipDenyDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpDenyDstPort_Type.__name__ = "Integer32"
_IpDenyDstPort_Object = MibTableColumn
ipDenyDstPort = _IpDenyDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 12),
    _IpDenyDstPort_Type()
)
ipDenyDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyDstPort.setStatus("mandatory")


class _IpDenySrcPortRange_Type(Integer32):
    """Custom type ipDenySrcPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpDenySrcPortRange_Type.__name__ = "Integer32"
_IpDenySrcPortRange_Object = MibTableColumn
ipDenySrcPortRange = _IpDenySrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 13),
    _IpDenySrcPortRange_Type()
)
ipDenySrcPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenySrcPortRange.setStatus("mandatory")


class _IpDenyDstPortRange_Type(Integer32):
    """Custom type ipDenyDstPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpDenyDstPortRange_Type.__name__ = "Integer32"
_IpDenyDstPortRange_Object = MibTableColumn
ipDenyDstPortRange = _IpDenyDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 14),
    _IpDenyDstPortRange_Type()
)
ipDenyDstPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDenyDstPortRange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IP-OLDACCESS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboipold": biboipold,
       "ipAllowTable": ipAllowTable,
       "ipAllowEntry": ipAllowEntry,
       "ipAllowProtocolMode": ipAllowProtocolMode,
       "ipAllowProtocol": ipAllowProtocol,
       "ipAllowSrcIfIndexMode": ipAllowSrcIfIndexMode,
       "ipAllowSrcIfIndex": ipAllowSrcIfIndex,
       "ipAllowSrcAddr": ipAllowSrcAddr,
       "ipAllowSrcMask": ipAllowSrcMask,
       "ipAllowSrcPortMode": ipAllowSrcPortMode,
       "ipAllowSrcPort": ipAllowSrcPort,
       "ipAllowDstAddr": ipAllowDstAddr,
       "ipAllowDstMask": ipAllowDstMask,
       "ipAllowDstPortMode": ipAllowDstPortMode,
       "ipAllowDstPort": ipAllowDstPort,
       "ipAllowSrcPortRange": ipAllowSrcPortRange,
       "ipAllowDstPortRange": ipAllowDstPortRange,
       "ipDenyTable": ipDenyTable,
       "ipDenyEntry": ipDenyEntry,
       "ipDenyProtocolMode": ipDenyProtocolMode,
       "ipDenyProtocol": ipDenyProtocol,
       "ipDenySrcIfIndexMode": ipDenySrcIfIndexMode,
       "ipDenySrcIfIndex": ipDenySrcIfIndex,
       "ipDenySrcAddr": ipDenySrcAddr,
       "ipDenySrcMask": ipDenySrcMask,
       "ipDenySrcPortMode": ipDenySrcPortMode,
       "ipDenySrcPort": ipDenySrcPort,
       "ipDenyDstAddr": ipDenyDstAddr,
       "ipDenyDstMask": ipDenyDstMask,
       "ipDenyDstPortMode": ipDenyDstPortMode,
       "ipDenyDstPort": ipDenyDstPort,
       "ipDenySrcPortRange": ipDenySrcPortRange,
       "ipDenyDstPortRange": ipDenyDstPortRange}
)
