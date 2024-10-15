# SNMP MIB module (MICOMIPRIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOMIPRIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:56 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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

_McmIp_ObjectIdentity = ObjectIdentity
mcmIp = _McmIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5)
)


class _McmIpRipEnable_Type(Integer32):
    """Custom type mcmIpRipEnable based on Integer32"""
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


_McmIpRipEnable_Type.__name__ = "Integer32"
_McmIpRipEnable_Object = MibScalar
mcmIpRipEnable = _McmIpRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 1),
    _McmIpRipEnable_Type()
)
mcmIpRipEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipEnable.setStatus("mandatory")


class _McmIpRipDfltRtEnable_Type(Integer32):
    """Custom type mcmIpRipDfltRtEnable based on Integer32"""
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


_McmIpRipDfltRtEnable_Type.__name__ = "Integer32"
_McmIpRipDfltRtEnable_Object = MibScalar
mcmIpRipDfltRtEnable = _McmIpRipDfltRtEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 2),
    _McmIpRipDfltRtEnable_Type()
)
mcmIpRipDfltRtEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipDfltRtEnable.setStatus("mandatory")
_McmIpAddrTable_Object = MibTable
mcmIpAddrTable = _McmIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    mcmIpAddrTable.setStatus("deprecated")
_McmIpAddrEntry_Object = MibTableRow
mcmIpAddrEntry = _McmIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1)
)
mcmIpAddrEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "mcmipIfIndex"),
)
if mibBuilder.loadTexts:
    mcmIpAddrEntry.setStatus("deprecated")
_McmipIfIndex_Type = Integer32
_McmipIfIndex_Object = MibTableColumn
mcmipIfIndex = _McmipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 1),
    _McmipIfIndex_Type()
)
mcmipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipIfIndex.setStatus("deprecated")
_McmipAddr_Type = IpAddress
_McmipAddr_Object = MibTableColumn
mcmipAddr = _McmipAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 2),
    _McmipAddr_Type()
)
mcmipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddr.setStatus("deprecated")
_McmipMtu_Type = Integer32
_McmipMtu_Object = MibTableColumn
mcmipMtu = _McmipMtu_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 3),
    _McmipMtu_Type()
)
mcmipMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipMtu.setStatus("deprecated")


class _McmipDlType_Type(Integer32):
    """Custom type mcmipDlType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("char", 7),
          ("csmacd", 1),
          ("ctca", 8),
          ("ether", 5),
          ("fddi", 9),
          ("frIpOpt", 11),
          ("frameRelay", 10),
          ("hdlc", 6),
          ("invalid", 13),
          ("metro", 4),
          ("other", 12),
          ("tpb", 2),
          ("tpr", 3))
    )


_McmipDlType_Type.__name__ = "Integer32"
_McmipDlType_Object = MibTableColumn
mcmipDlType = _McmipDlType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 4),
    _McmipDlType_Type()
)
mcmipDlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipDlType.setStatus("deprecated")


class _McmipKeepAlive_Type(Integer32):
    """Custom type mcmipKeepAlive based on Integer32"""
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


_McmipKeepAlive_Type.__name__ = "Integer32"
_McmipKeepAlive_Object = MibTableColumn
mcmipKeepAlive = _McmipKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 5),
    _McmipKeepAlive_Type()
)
mcmipKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipKeepAlive.setStatus("deprecated")


class _McmipForwardBcast_Type(Integer32):
    """Custom type mcmipForwardBcast based on Integer32"""
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


_McmipForwardBcast_Type.__name__ = "Integer32"
_McmipForwardBcast_Object = MibTableColumn
mcmipForwardBcast = _McmipForwardBcast_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 6),
    _McmipForwardBcast_Type()
)
mcmipForwardBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipForwardBcast.setStatus("deprecated")


class _McmipUnumIf_Type(Integer32):
    """Custom type mcmipUnumIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numbered", 2),
          ("unnumbered", 1))
    )


_McmipUnumIf_Type.__name__ = "Integer32"
_McmipUnumIf_Object = MibTableColumn
mcmipUnumIf = _McmipUnumIf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 7),
    _McmipUnumIf_Type()
)
mcmipUnumIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipUnumIf.setStatus("deprecated")


class _McmipRoutProtType_Type(Integer32):
    """Custom type mcmipRoutProtType based on Integer32"""
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
        *(("disable", 4),
          ("ospf", 2),
          ("passiveRip", 3),
          ("rip", 1))
    )


_McmipRoutProtType_Type.__name__ = "Integer32"
_McmipRoutProtType_Object = MibTableColumn
mcmipRoutProtType = _McmipRoutProtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 3, 1, 8),
    _McmipRoutProtType_Type()
)
mcmipRoutProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipRoutProtType.setStatus("deprecated")


class _NvmIpRipEnable_Type(Integer32):
    """Custom type nvmIpRipEnable based on Integer32"""
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


_NvmIpRipEnable_Type.__name__ = "Integer32"
_NvmIpRipEnable_Object = MibScalar
nvmIpRipEnable = _NvmIpRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 4),
    _NvmIpRipEnable_Type()
)
nvmIpRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipEnable.setStatus("mandatory")


class _NvmIpRipDfltRtEnable_Type(Integer32):
    """Custom type nvmIpRipDfltRtEnable based on Integer32"""
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


_NvmIpRipDfltRtEnable_Type.__name__ = "Integer32"
_NvmIpRipDfltRtEnable_Object = MibScalar
nvmIpRipDfltRtEnable = _NvmIpRipDfltRtEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 5),
    _NvmIpRipDfltRtEnable_Type()
)
nvmIpRipDfltRtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipDfltRtEnable.setStatus("mandatory")
_NvmIpAddrTable_Object = MibTable
nvmIpAddrTable = _NvmIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6)
)
if mibBuilder.loadTexts:
    nvmIpAddrTable.setStatus("deprecated")
_NvmIpAddrEntry_Object = MibTableRow
nvmIpAddrEntry = _NvmIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1)
)
nvmIpAddrEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "nvmipIfIndex"),
)
if mibBuilder.loadTexts:
    nvmIpAddrEntry.setStatus("deprecated")


class _NvmipIfIndex_Type(Integer32):
    """Custom type nvmipIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmipIfIndex_Type.__name__ = "Integer32"
_NvmipIfIndex_Object = MibTableColumn
nvmipIfIndex = _NvmipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 1),
    _NvmipIfIndex_Type()
)
nvmipIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipIfIndex.setStatus("deprecated")
_NvmipAddr_Type = IpAddress
_NvmipAddr_Object = MibTableColumn
nvmipAddr = _NvmipAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 2),
    _NvmipAddr_Type()
)
nvmipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddr.setStatus("deprecated")
_NvmipMtu_Type = Integer32
_NvmipMtu_Object = MibTableColumn
nvmipMtu = _NvmipMtu_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 3),
    _NvmipMtu_Type()
)
nvmipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipMtu.setStatus("deprecated")


class _NvmipDlType_Type(Integer32):
    """Custom type nvmipDlType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("char", 7),
          ("csmacd", 1),
          ("ctca", 8),
          ("ether", 5),
          ("fddi", 9),
          ("frIpOpt", 11),
          ("frameRelay", 10),
          ("hdlc", 6),
          ("invalid", 13),
          ("metro", 4),
          ("other", 12),
          ("tpb", 2),
          ("tpr", 3))
    )


_NvmipDlType_Type.__name__ = "Integer32"
_NvmipDlType_Object = MibTableColumn
nvmipDlType = _NvmipDlType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 4),
    _NvmipDlType_Type()
)
nvmipDlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipDlType.setStatus("deprecated")


class _NvmipKeepAlive_Type(Integer32):
    """Custom type nvmipKeepAlive based on Integer32"""
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


_NvmipKeepAlive_Type.__name__ = "Integer32"
_NvmipKeepAlive_Object = MibTableColumn
nvmipKeepAlive = _NvmipKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 5),
    _NvmipKeepAlive_Type()
)
nvmipKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipKeepAlive.setStatus("deprecated")


class _NvmipForwardBcast_Type(Integer32):
    """Custom type nvmipForwardBcast based on Integer32"""
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


_NvmipForwardBcast_Type.__name__ = "Integer32"
_NvmipForwardBcast_Object = MibTableColumn
nvmipForwardBcast = _NvmipForwardBcast_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 6),
    _NvmipForwardBcast_Type()
)
nvmipForwardBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipForwardBcast.setStatus("deprecated")


class _NvmipUnumIf_Type(Integer32):
    """Custom type nvmipUnumIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numbered", 2),
          ("unnumbered", 1))
    )


_NvmipUnumIf_Type.__name__ = "Integer32"
_NvmipUnumIf_Object = MibTableColumn
nvmipUnumIf = _NvmipUnumIf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 7),
    _NvmipUnumIf_Type()
)
nvmipUnumIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipUnumIf.setStatus("deprecated")


class _NvmipRoutProtType_Type(Integer32):
    """Custom type nvmipRoutProtType based on Integer32"""
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
        *(("disable", 4),
          ("ospf", 2),
          ("passiveRip", 3),
          ("rip", 1))
    )


_NvmipRoutProtType_Type.__name__ = "Integer32"
_NvmipRoutProtType_Object = MibTableColumn
nvmipRoutProtType = _NvmipRoutProtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 8),
    _NvmipRoutProtType_Type()
)
nvmipRoutProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipRoutProtType.setStatus("deprecated")
_NvmipNetMask_Type = IpAddress
_NvmipNetMask_Object = MibTableColumn
nvmipNetMask = _NvmipNetMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 9),
    _NvmipNetMask_Type()
)
nvmipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipNetMask.setStatus("deprecated")
_NvmipBcastAddr_Type = IpAddress
_NvmipBcastAddr_Object = MibTableColumn
nvmipBcastAddr = _NvmipBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 6, 1, 10),
    _NvmipBcastAddr_Type()
)
nvmipBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipBcastAddr.setStatus("deprecated")
_McmIpCntr_ObjectIdentity = ObjectIdentity
mcmIpCntr = _McmIpCntr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7)
)
_McmIpIfCntrZeroTable_Object = MibTable
mcmIpIfCntrZeroTable = _McmIpIfCntrZeroTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mcmIpIfCntrZeroTable.setStatus("obsolete")
_McmIpIfCntrZeroEntry_Object = MibTableRow
mcmIpIfCntrZeroEntry = _McmIpIfCntrZeroEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 1, 1)
)
mcmIpIfCntrZeroEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "mcmIpIfCntrZeroIndex"),
)
if mibBuilder.loadTexts:
    mcmIpIfCntrZeroEntry.setStatus("obsolete")
_McmIpIfCntrZeroIndex_Type = Integer32
_McmIpIfCntrZeroIndex_Object = MibTableColumn
mcmIpIfCntrZeroIndex = _McmIpIfCntrZeroIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 1, 1, 1),
    _McmIpIfCntrZeroIndex_Type()
)
mcmIpIfCntrZeroIndex.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIpIfCntrZeroIndex.setStatus("obsolete")


class _McmIpIfGrpCounterZero_Type(Integer32):
    """Custom type mcmIpIfGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmIpIfGrpCounterZero_Type.__name__ = "Integer32"
_McmIpIfGrpCounterZero_Object = MibTableColumn
mcmIpIfGrpCounterZero = _McmIpIfGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 1, 1, 2),
    _McmIpIfGrpCounterZero_Type()
)
mcmIpIfGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIpIfGrpCounterZero.setStatus("obsolete")
_McmIpCntrGrp_ObjectIdentity = ObjectIdentity
mcmIpCntrGrp = _McmIpCntrGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2)
)


class _McmIpGrpCounterZero_Type(Integer32):
    """Custom type mcmIpGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmIpGrpCounterZero_Type.__name__ = "Integer32"
_McmIpGrpCounterZero_Object = MibScalar
mcmIpGrpCounterZero = _McmIpGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2, 1),
    _McmIpGrpCounterZero_Type()
)
mcmIpGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIpGrpCounterZero.setStatus("obsolete")


class _McmIcmpGrpCounterZero_Type(Integer32):
    """Custom type mcmIcmpGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmIcmpGrpCounterZero_Type.__name__ = "Integer32"
_McmIcmpGrpCounterZero_Object = MibScalar
mcmIcmpGrpCounterZero = _McmIcmpGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2, 2),
    _McmIcmpGrpCounterZero_Type()
)
mcmIcmpGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIcmpGrpCounterZero.setStatus("obsolete")


class _McmTcpGrpCounterZero_Type(Integer32):
    """Custom type mcmTcpGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmTcpGrpCounterZero_Type.__name__ = "Integer32"
_McmTcpGrpCounterZero_Object = MibScalar
mcmTcpGrpCounterZero = _McmTcpGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2, 3),
    _McmTcpGrpCounterZero_Type()
)
mcmTcpGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmTcpGrpCounterZero.setStatus("obsolete")


class _McmUdpGrpCounterZero_Type(Integer32):
    """Custom type mcmUdpGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmUdpGrpCounterZero_Type.__name__ = "Integer32"
_McmUdpGrpCounterZero_Object = MibScalar
mcmUdpGrpCounterZero = _McmUdpGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2, 4),
    _McmUdpGrpCounterZero_Type()
)
mcmUdpGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmUdpGrpCounterZero.setStatus("obsolete")


class _McmSnmpGrpCounterZero_Type(Integer32):
    """Custom type mcmSnmpGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmSnmpGrpCounterZero_Type.__name__ = "Integer32"
_McmSnmpGrpCounterZero_Object = MibScalar
mcmSnmpGrpCounterZero = _McmSnmpGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 7, 2, 5),
    _McmSnmpGrpCounterZero_Type()
)
mcmSnmpGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmSnmpGrpCounterZero.setStatus("obsolete")
_McmInverseArpTable_Object = MibTable
mcmInverseArpTable = _McmInverseArpTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 8)
)
if mibBuilder.loadTexts:
    mcmInverseArpTable.setStatus("mandatory")
_McmInverseArpEntry_Object = MibTableRow
mcmInverseArpEntry = _McmInverseArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 8, 1)
)
mcmInverseArpEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "mcmInverseArpIfIndex"),
    (0, "MICOMIPRIP-MIB", "mcmInverseArpProtocol"),
)
if mibBuilder.loadTexts:
    mcmInverseArpEntry.setStatus("mandatory")


class _McmInverseArpIfIndex_Type(Integer32):
    """Custom type mcmInverseArpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmInverseArpIfIndex_Type.__name__ = "Integer32"
_McmInverseArpIfIndex_Object = MibTableColumn
mcmInverseArpIfIndex = _McmInverseArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 8, 1, 1),
    _McmInverseArpIfIndex_Type()
)
mcmInverseArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmInverseArpIfIndex.setStatus("mandatory")


class _McmInverseArpProtocol_Type(Integer32):
    """Custom type mcmInverseArpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_McmInverseArpProtocol_Type.__name__ = "Integer32"
_McmInverseArpProtocol_Object = MibTableColumn
mcmInverseArpProtocol = _McmInverseArpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 8, 1, 2),
    _McmInverseArpProtocol_Type()
)
mcmInverseArpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmInverseArpProtocol.setStatus("mandatory")


class _McmInverseArpStatus_Type(Integer32):
    """Custom type mcmInverseArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_McmInverseArpStatus_Type.__name__ = "Integer32"
_McmInverseArpStatus_Object = MibTableColumn
mcmInverseArpStatus = _McmInverseArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 8, 1, 3),
    _McmInverseArpStatus_Type()
)
mcmInverseArpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmInverseArpStatus.setStatus("mandatory")
_NvmInverseArpTable_Object = MibTable
nvmInverseArpTable = _NvmInverseArpTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 9)
)
if mibBuilder.loadTexts:
    nvmInverseArpTable.setStatus("mandatory")
_NvmInverseArpEntry_Object = MibTableRow
nvmInverseArpEntry = _NvmInverseArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 9, 1)
)
nvmInverseArpEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "nvmInverseArpIfIndex"),
    (0, "MICOMIPRIP-MIB", "nvmInverseArpProtocol"),
)
if mibBuilder.loadTexts:
    nvmInverseArpEntry.setStatus("mandatory")


class _NvmInverseArpIfIndex_Type(Integer32):
    """Custom type nvmInverseArpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmInverseArpIfIndex_Type.__name__ = "Integer32"
_NvmInverseArpIfIndex_Object = MibTableColumn
nvmInverseArpIfIndex = _NvmInverseArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 9, 1, 1),
    _NvmInverseArpIfIndex_Type()
)
nvmInverseArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmInverseArpIfIndex.setStatus("mandatory")


class _NvmInverseArpProtocol_Type(Integer32):
    """Custom type nvmInverseArpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_NvmInverseArpProtocol_Type.__name__ = "Integer32"
_NvmInverseArpProtocol_Object = MibTableColumn
nvmInverseArpProtocol = _NvmInverseArpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 9, 1, 2),
    _NvmInverseArpProtocol_Type()
)
nvmInverseArpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmInverseArpProtocol.setStatus("mandatory")


class _NvmInverseArpStatus_Type(Integer32):
    """Custom type nvmInverseArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NvmInverseArpStatus_Type.__name__ = "Integer32"
_NvmInverseArpStatus_Object = MibTableColumn
nvmInverseArpStatus = _NvmInverseArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 9, 1, 3),
    _NvmInverseArpStatus_Type()
)
nvmInverseArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmInverseArpStatus.setStatus("mandatory")


class _McmIpRipCompatibility_Type(Integer32):
    """Custom type mcmIpRipCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip1Compatible", 2),
          ("rip2", 3))
    )


_McmIpRipCompatibility_Type.__name__ = "Integer32"
_McmIpRipCompatibility_Object = MibScalar
mcmIpRipCompatibility = _McmIpRipCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 10),
    _McmIpRipCompatibility_Type()
)
mcmIpRipCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipCompatibility.setStatus("mandatory")


class _NvmIpAddressRipCompatibility_Type(Integer32):
    """Custom type nvmIpAddressRipCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip1Compatible", 2),
          ("rip2", 3))
    )


_NvmIpAddressRipCompatibility_Type.__name__ = "Integer32"
_NvmIpAddressRipCompatibility_Object = MibScalar
nvmIpAddressRipCompatibility = _NvmIpAddressRipCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 11),
    _NvmIpAddressRipCompatibility_Type()
)
nvmIpAddressRipCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpAddressRipCompatibility.setStatus("mandatory")
_McmIpAddressTable_Object = MibTable
mcmIpAddressTable = _McmIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12)
)
if mibBuilder.loadTexts:
    mcmIpAddressTable.setStatus("mandatory")
_McmIpAddressEntry_Object = MibTableRow
mcmIpAddressEntry = _McmIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1)
)
mcmIpAddressEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "mcmipAddressIfIndex"),
    (0, "MICOMIPRIP-MIB", "mcmipAddress"),
)
if mibBuilder.loadTexts:
    mcmIpAddressEntry.setStatus("mandatory")
_McmipAddressIfIndex_Type = Integer32
_McmipAddressIfIndex_Object = MibTableColumn
mcmipAddressIfIndex = _McmipAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 1),
    _McmipAddressIfIndex_Type()
)
mcmipAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressIfIndex.setStatus("mandatory")
_McmipAddress_Type = IpAddress
_McmipAddress_Object = MibTableColumn
mcmipAddress = _McmipAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 2),
    _McmipAddress_Type()
)
mcmipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddress.setStatus("mandatory")
_McmipAddressMtu_Type = Integer32
_McmipAddressMtu_Object = MibTableColumn
mcmipAddressMtu = _McmipAddressMtu_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 3),
    _McmipAddressMtu_Type()
)
mcmipAddressMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressMtu.setStatus("mandatory")


class _McmipAddressDlType_Type(Integer32):
    """Custom type mcmipAddressDlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ether", 5),
          ("frameRelay", 10),
          ("invalid", 13))
    )


_McmipAddressDlType_Type.__name__ = "Integer32"
_McmipAddressDlType_Object = MibTableColumn
mcmipAddressDlType = _McmipAddressDlType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 4),
    _McmipAddressDlType_Type()
)
mcmipAddressDlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressDlType.setStatus("mandatory")


class _McmipAddressKeepAlive_Type(Integer32):
    """Custom type mcmipAddressKeepAlive based on Integer32"""
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


_McmipAddressKeepAlive_Type.__name__ = "Integer32"
_McmipAddressKeepAlive_Object = MibTableColumn
mcmipAddressKeepAlive = _McmipAddressKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 5),
    _McmipAddressKeepAlive_Type()
)
mcmipAddressKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressKeepAlive.setStatus("mandatory")


class _McmipAddressForwardBcast_Type(Integer32):
    """Custom type mcmipAddressForwardBcast based on Integer32"""
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


_McmipAddressForwardBcast_Type.__name__ = "Integer32"
_McmipAddressForwardBcast_Object = MibTableColumn
mcmipAddressForwardBcast = _McmipAddressForwardBcast_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 6),
    _McmipAddressForwardBcast_Type()
)
mcmipAddressForwardBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressForwardBcast.setStatus("mandatory")


class _McmipAddressUnumIf_Type(Integer32):
    """Custom type mcmipAddressUnumIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numbered", 2),
          ("unnumbered", 1))
    )


_McmipAddressUnumIf_Type.__name__ = "Integer32"
_McmipAddressUnumIf_Object = MibTableColumn
mcmipAddressUnumIf = _McmipAddressUnumIf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 7),
    _McmipAddressUnumIf_Type()
)
mcmipAddressUnumIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressUnumIf.setStatus("mandatory")


class _McmipAddressRoutProtType_Type(Integer32):
    """Custom type mcmipAddressRoutProtType based on Integer32"""
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
        *(("disable", 4),
          ("ospf", 2),
          ("passiveRip", 3),
          ("rip", 1))
    )


_McmipAddressRoutProtType_Type.__name__ = "Integer32"
_McmipAddressRoutProtType_Object = MibTableColumn
mcmipAddressRoutProtType = _McmipAddressRoutProtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 12, 1, 8),
    _McmipAddressRoutProtType_Type()
)
mcmipAddressRoutProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipAddressRoutProtType.setStatus("mandatory")
_NvmIpAddressTable_Object = MibTable
nvmIpAddressTable = _NvmIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13)
)
if mibBuilder.loadTexts:
    nvmIpAddressTable.setStatus("mandatory")
_NvmIpAddressEntry_Object = MibTableRow
nvmIpAddressEntry = _NvmIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1)
)
nvmIpAddressEntry.setIndexNames(
    (0, "MICOMIPRIP-MIB", "nvmipAddressIfIndex"),
    (0, "MICOMIPRIP-MIB", "nvmipAddress"),
)
if mibBuilder.loadTexts:
    nvmIpAddressEntry.setStatus("mandatory")


class _NvmipAddressIfIndex_Type(Integer32):
    """Custom type nvmipAddressIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmipAddressIfIndex_Type.__name__ = "Integer32"
_NvmipAddressIfIndex_Object = MibTableColumn
nvmipAddressIfIndex = _NvmipAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 1),
    _NvmipAddressIfIndex_Type()
)
nvmipAddressIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressIfIndex.setStatus("mandatory")
_NvmipAddress_Type = IpAddress
_NvmipAddress_Object = MibTableColumn
nvmipAddress = _NvmipAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 2),
    _NvmipAddress_Type()
)
nvmipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddress.setStatus("mandatory")


class _NvmipAddressMtu_Type(Integer32):
    """Custom type nvmipAddressMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_NvmipAddressMtu_Type.__name__ = "Integer32"
_NvmipAddressMtu_Object = MibTableColumn
nvmipAddressMtu = _NvmipAddressMtu_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 3),
    _NvmipAddressMtu_Type()
)
nvmipAddressMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressMtu.setStatus("mandatory")


class _NvmipAddressDlType_Type(Integer32):
    """Custom type nvmipAddressDlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ether", 5),
          ("frameRelay", 10),
          ("invalid", 13))
    )


_NvmipAddressDlType_Type.__name__ = "Integer32"
_NvmipAddressDlType_Object = MibTableColumn
nvmipAddressDlType = _NvmipAddressDlType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 4),
    _NvmipAddressDlType_Type()
)
nvmipAddressDlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressDlType.setStatus("mandatory")


class _NvmipAddressKeepAlive_Type(Integer32):
    """Custom type nvmipAddressKeepAlive based on Integer32"""
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


_NvmipAddressKeepAlive_Type.__name__ = "Integer32"
_NvmipAddressKeepAlive_Object = MibTableColumn
nvmipAddressKeepAlive = _NvmipAddressKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 5),
    _NvmipAddressKeepAlive_Type()
)
nvmipAddressKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressKeepAlive.setStatus("mandatory")


class _NvmipAddressForwardBcast_Type(Integer32):
    """Custom type nvmipAddressForwardBcast based on Integer32"""
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


_NvmipAddressForwardBcast_Type.__name__ = "Integer32"
_NvmipAddressForwardBcast_Object = MibTableColumn
nvmipAddressForwardBcast = _NvmipAddressForwardBcast_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 6),
    _NvmipAddressForwardBcast_Type()
)
nvmipAddressForwardBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressForwardBcast.setStatus("mandatory")


class _NvmipAddressUnumIf_Type(Integer32):
    """Custom type nvmipAddressUnumIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numbered", 2),
          ("unnumbered", 1))
    )


_NvmipAddressUnumIf_Type.__name__ = "Integer32"
_NvmipAddressUnumIf_Object = MibTableColumn
nvmipAddressUnumIf = _NvmipAddressUnumIf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 7),
    _NvmipAddressUnumIf_Type()
)
nvmipAddressUnumIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressUnumIf.setStatus("mandatory")


class _NvmipAddressRoutProtType_Type(Integer32):
    """Custom type nvmipAddressRoutProtType based on Integer32"""
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
        *(("disable", 4),
          ("ospf", 2),
          ("passiveRip", 3),
          ("rip", 1))
    )


_NvmipAddressRoutProtType_Type.__name__ = "Integer32"
_NvmipAddressRoutProtType_Object = MibTableColumn
nvmipAddressRoutProtType = _NvmipAddressRoutProtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 8),
    _NvmipAddressRoutProtType_Type()
)
nvmipAddressRoutProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressRoutProtType.setStatus("mandatory")
_NvmipAddressNetMask_Type = IpAddress
_NvmipAddressNetMask_Object = MibTableColumn
nvmipAddressNetMask = _NvmipAddressNetMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 9),
    _NvmipAddressNetMask_Type()
)
nvmipAddressNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressNetMask.setStatus("mandatory")
_NvmipAddressBcastAddr_Type = IpAddress
_NvmipAddressBcastAddr_Object = MibTableColumn
nvmipAddressBcastAddr = _NvmipAddressBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 10),
    _NvmipAddressBcastAddr_Type()
)
nvmipAddressBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressBcastAddr.setStatus("mandatory")


class _NvmipAddressRowStatus_Type(Integer32):
    """Custom type nvmipAddressRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("destroy", 2))
    )


_NvmipAddressRowStatus_Type.__name__ = "Integer32"
_NvmipAddressRowStatus_Object = MibTableColumn
nvmipAddressRowStatus = _NvmipAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 13, 1, 11),
    _NvmipAddressRowStatus_Type()
)
nvmipAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipAddressRowStatus.setStatus("mandatory")
_McmIPBootpRelayGroup_ObjectIdentity = ObjectIdentity
mcmIPBootpRelayGroup = _McmIPBootpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 14)
)


class _McmIPBootpRelay_Type(Integer32):
    """Custom type mcmIPBootpRelay based on Integer32"""
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


_McmIPBootpRelay_Type.__name__ = "Integer32"
_McmIPBootpRelay_Object = MibScalar
mcmIPBootpRelay = _McmIPBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 14, 1),
    _McmIPBootpRelay_Type()
)
mcmIPBootpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIPBootpRelay.setStatus("mandatory")
_McmIPBootpRelayServerAddr_Type = IpAddress
_McmIPBootpRelayServerAddr_Object = MibScalar
mcmIPBootpRelayServerAddr = _McmIPBootpRelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 14, 2),
    _McmIPBootpRelayServerAddr_Type()
)
mcmIPBootpRelayServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIPBootpRelayServerAddr.setStatus("mandatory")


class _McmIPBootpRelayHops_Type(Integer32):
    """Custom type mcmIPBootpRelayHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmIPBootpRelayHops_Type.__name__ = "Integer32"
_McmIPBootpRelayHops_Object = MibScalar
mcmIPBootpRelayHops = _McmIPBootpRelayHops_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 14, 3),
    _McmIPBootpRelayHops_Type()
)
mcmIPBootpRelayHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIPBootpRelayHops.setStatus("mandatory")
_NvmIPBootpRelayGroup_ObjectIdentity = ObjectIdentity
nvmIPBootpRelayGroup = _NvmIPBootpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 15)
)


class _NvmIPBootpRelay_Type(Integer32):
    """Custom type nvmIPBootpRelay based on Integer32"""
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


_NvmIPBootpRelay_Type.__name__ = "Integer32"
_NvmIPBootpRelay_Object = MibScalar
nvmIPBootpRelay = _NvmIPBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 15, 1),
    _NvmIPBootpRelay_Type()
)
nvmIPBootpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIPBootpRelay.setStatus("mandatory")
_NvmIPBootpRelayServerAddr_Type = IpAddress
_NvmIPBootpRelayServerAddr_Object = MibScalar
nvmIPBootpRelayServerAddr = _NvmIPBootpRelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 15, 2),
    _NvmIPBootpRelayServerAddr_Type()
)
nvmIPBootpRelayServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIPBootpRelayServerAddr.setStatus("mandatory")


class _NvmIPBootpRelayHops_Type(Integer32):
    """Custom type nvmIPBootpRelayHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmIPBootpRelayHops_Type.__name__ = "Integer32"
_NvmIPBootpRelayHops_Object = MibScalar
nvmIPBootpRelayHops = _NvmIPBootpRelayHops_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 15, 3),
    _NvmIPBootpRelayHops_Type()
)
nvmIPBootpRelayHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIPBootpRelayHops.setStatus("mandatory")
_Ip_control_ObjectIdentity = ObjectIdentity
ip_control = _Ip_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 16)
)
_McmIpPingGroup_ObjectIdentity = ObjectIdentity
mcmIpPingGroup = _McmIpPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 16, 1)
)


class _McmIpPingAction_Type(Integer32):
    """Custom type mcmIpPingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ping", 1)
    )


_McmIpPingAction_Type.__name__ = "Integer32"
_McmIpPingAction_Object = MibScalar
mcmIpPingAction = _McmIpPingAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 16, 1, 1),
    _McmIpPingAction_Type()
)
mcmIpPingAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIpPingAction.setStatus("mandatory")
_McmIpPingAddress_Type = IpAddress
_McmIpPingAddress_Object = MibScalar
mcmIpPingAddress = _McmIpPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 16, 1, 2),
    _McmIpPingAddress_Type()
)
mcmIpPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmIpPingAddress.setStatus("mandatory")


class _McmIpPingStatus_Type(Integer32):
    """Custom type mcmIpPingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("destinationUnreachable", 2),
          ("timeExceeded", 3))
    )


_McmIpPingStatus_Type.__name__ = "Integer32"
_McmIpPingStatus_Object = MibScalar
mcmIpPingStatus = _McmIpPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 5, 16, 1, 3),
    _McmIpPingStatus_Type()
)
mcmIpPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpPingStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOMIPRIP-MIB",
    **{"mcmIp": mcmIp,
       "mcmIpRipEnable": mcmIpRipEnable,
       "mcmIpRipDfltRtEnable": mcmIpRipDfltRtEnable,
       "mcmIpAddrTable": mcmIpAddrTable,
       "mcmIpAddrEntry": mcmIpAddrEntry,
       "mcmipIfIndex": mcmipIfIndex,
       "mcmipAddr": mcmipAddr,
       "mcmipMtu": mcmipMtu,
       "mcmipDlType": mcmipDlType,
       "mcmipKeepAlive": mcmipKeepAlive,
       "mcmipForwardBcast": mcmipForwardBcast,
       "mcmipUnumIf": mcmipUnumIf,
       "mcmipRoutProtType": mcmipRoutProtType,
       "nvmIpRipEnable": nvmIpRipEnable,
       "nvmIpRipDfltRtEnable": nvmIpRipDfltRtEnable,
       "nvmIpAddrTable": nvmIpAddrTable,
       "nvmIpAddrEntry": nvmIpAddrEntry,
       "nvmipIfIndex": nvmipIfIndex,
       "nvmipAddr": nvmipAddr,
       "nvmipMtu": nvmipMtu,
       "nvmipDlType": nvmipDlType,
       "nvmipKeepAlive": nvmipKeepAlive,
       "nvmipForwardBcast": nvmipForwardBcast,
       "nvmipUnumIf": nvmipUnumIf,
       "nvmipRoutProtType": nvmipRoutProtType,
       "nvmipNetMask": nvmipNetMask,
       "nvmipBcastAddr": nvmipBcastAddr,
       "mcmIpCntr": mcmIpCntr,
       "mcmIpIfCntrZeroTable": mcmIpIfCntrZeroTable,
       "mcmIpIfCntrZeroEntry": mcmIpIfCntrZeroEntry,
       "mcmIpIfCntrZeroIndex": mcmIpIfCntrZeroIndex,
       "mcmIpIfGrpCounterZero": mcmIpIfGrpCounterZero,
       "mcmIpCntrGrp": mcmIpCntrGrp,
       "mcmIpGrpCounterZero": mcmIpGrpCounterZero,
       "mcmIcmpGrpCounterZero": mcmIcmpGrpCounterZero,
       "mcmTcpGrpCounterZero": mcmTcpGrpCounterZero,
       "mcmUdpGrpCounterZero": mcmUdpGrpCounterZero,
       "mcmSnmpGrpCounterZero": mcmSnmpGrpCounterZero,
       "mcmInverseArpTable": mcmInverseArpTable,
       "mcmInverseArpEntry": mcmInverseArpEntry,
       "mcmInverseArpIfIndex": mcmInverseArpIfIndex,
       "mcmInverseArpProtocol": mcmInverseArpProtocol,
       "mcmInverseArpStatus": mcmInverseArpStatus,
       "nvmInverseArpTable": nvmInverseArpTable,
       "nvmInverseArpEntry": nvmInverseArpEntry,
       "nvmInverseArpIfIndex": nvmInverseArpIfIndex,
       "nvmInverseArpProtocol": nvmInverseArpProtocol,
       "nvmInverseArpStatus": nvmInverseArpStatus,
       "mcmIpRipCompatibility": mcmIpRipCompatibility,
       "nvmIpAddressRipCompatibility": nvmIpAddressRipCompatibility,
       "mcmIpAddressTable": mcmIpAddressTable,
       "mcmIpAddressEntry": mcmIpAddressEntry,
       "mcmipAddressIfIndex": mcmipAddressIfIndex,
       "mcmipAddress": mcmipAddress,
       "mcmipAddressMtu": mcmipAddressMtu,
       "mcmipAddressDlType": mcmipAddressDlType,
       "mcmipAddressKeepAlive": mcmipAddressKeepAlive,
       "mcmipAddressForwardBcast": mcmipAddressForwardBcast,
       "mcmipAddressUnumIf": mcmipAddressUnumIf,
       "mcmipAddressRoutProtType": mcmipAddressRoutProtType,
       "nvmIpAddressTable": nvmIpAddressTable,
       "nvmIpAddressEntry": nvmIpAddressEntry,
       "nvmipAddressIfIndex": nvmipAddressIfIndex,
       "nvmipAddress": nvmipAddress,
       "nvmipAddressMtu": nvmipAddressMtu,
       "nvmipAddressDlType": nvmipAddressDlType,
       "nvmipAddressKeepAlive": nvmipAddressKeepAlive,
       "nvmipAddressForwardBcast": nvmipAddressForwardBcast,
       "nvmipAddressUnumIf": nvmipAddressUnumIf,
       "nvmipAddressRoutProtType": nvmipAddressRoutProtType,
       "nvmipAddressNetMask": nvmipAddressNetMask,
       "nvmipAddressBcastAddr": nvmipAddressBcastAddr,
       "nvmipAddressRowStatus": nvmipAddressRowStatus,
       "mcmIPBootpRelayGroup": mcmIPBootpRelayGroup,
       "mcmIPBootpRelay": mcmIPBootpRelay,
       "mcmIPBootpRelayServerAddr": mcmIPBootpRelayServerAddr,
       "mcmIPBootpRelayHops": mcmIPBootpRelayHops,
       "nvmIPBootpRelayGroup": nvmIPBootpRelayGroup,
       "nvmIPBootpRelay": nvmIPBootpRelay,
       "nvmIPBootpRelayServerAddr": nvmIPBootpRelayServerAddr,
       "nvmIPBootpRelayHops": nvmIPBootpRelayHops,
       "ip-control": ip_control,
       "mcmIpPingGroup": mcmIpPingGroup,
       "mcmIpPingAction": mcmIpPingAction,
       "mcmIpPingAddress": mcmIpPingAddress,
       "mcmIpPingStatus": mcmIpPingStatus}
)
