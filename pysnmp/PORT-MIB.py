# SNMP MIB module (PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:15 2024
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

(slotNo,) = mibBuilder.importSymbols(
    "CARD-MIB",
    "slotNo")

(coriolisMibs,
 port) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "coriolisMibs",
    "port")

(dot3StatsDuplexStatus,) = mibBuilder.importSymbols(
    "EtherLike-MIB",
    "dot3StatsDuplexStatus")

(InterfaceIndex,
 ifAdminStatus,
 ifOperStatus,
 ifSpeed) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAdminStatus",
    "ifOperStatus",
    "ifSpeed")

(ifMauAutoNegConfig,) = mibBuilder.importSymbols(
    "MAU-MIB",
    "ifMauAutoNegConfig")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(sonetLineCurrentStatus,
 sonetPathCurrentStatus,
 sonetSectionCurrentStatus,
 sonetVTCurrentStatus) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetLineCurrentStatus",
    "sonetPathCurrentStatus",
    "sonetSectionCurrentStatus",
    "sonetVTCurrentStatus")


# MODULE-IDENTITY

portMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 2, 1)
)
portEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortNo_Type(Integer32):
    """Custom type portNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortNo_Type.__name__ = "Integer32"
_PortNo_Object = MibTableColumn
portNo = _PortNo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 2, 1, 1),
    _PortNo_Type()
)
portNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portNo.setStatus("current")
_Mib2IfIndex_Type = InterfaceIndex
_Mib2IfIndex_Object = MibTableColumn
mib2IfIndex = _Mib2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 2, 1, 2),
    _Mib2IfIndex_Type()
)
mib2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mib2IfIndex.setStatus("current")
_EtherPortTable_Object = MibTable
etherPortTable = _EtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3)
)
if mibBuilder.loadTexts:
    etherPortTable.setStatus("current")
_EtherPortEntry_Object = MibTableRow
etherPortEntry = _EtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1)
)
etherPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    etherPortEntry.setStatus("current")


class _EtherPortSpeedCfg_Type(Integer32):
    """Custom type etherPortSpeedCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3))
    )


_EtherPortSpeedCfg_Type.__name__ = "Integer32"
_EtherPortSpeedCfg_Object = MibTableColumn
etherPortSpeedCfg = _EtherPortSpeedCfg_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 1),
    _EtherPortSpeedCfg_Type()
)
etherPortSpeedCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortSpeedCfg.setStatus("current")


class _EtherPortSpeedStatus_Type(Integer32):
    """Custom type etherPortSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3))
    )


_EtherPortSpeedStatus_Type.__name__ = "Integer32"
_EtherPortSpeedStatus_Object = MibTableColumn
etherPortSpeedStatus = _EtherPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 2),
    _EtherPortSpeedStatus_Type()
)
etherPortSpeedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortSpeedStatus.setStatus("current")


class _EtherPortDuplexCfg_Type(Integer32):
    """Custom type etherPortDuplexCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("unknown", 1))
    )


_EtherPortDuplexCfg_Type.__name__ = "Integer32"
_EtherPortDuplexCfg_Object = MibTableColumn
etherPortDuplexCfg = _EtherPortDuplexCfg_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 3),
    _EtherPortDuplexCfg_Type()
)
etherPortDuplexCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortDuplexCfg.setStatus("current")


class _EtherPortLoopback_Type(Integer32):
    """Custom type etherPortLoopback based on Integer32"""
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


_EtherPortLoopback_Type.__name__ = "Integer32"
_EtherPortLoopback_Object = MibTableColumn
etherPortLoopback = _EtherPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 4),
    _EtherPortLoopback_Type()
)
etherPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortLoopback.setStatus("current")


class _EtherPortPhyReset_Type(Integer32):
    """Custom type etherPortPhyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inReset", 1),
          ("outOfReset", 2))
    )


_EtherPortPhyReset_Type.__name__ = "Integer32"
_EtherPortPhyReset_Object = MibTableColumn
etherPortPhyReset = _EtherPortPhyReset_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 5),
    _EtherPortPhyReset_Type()
)
etherPortPhyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortPhyReset.setStatus("current")
_EtherPortStatsTxPkts64Octets_Type = Counter32
_EtherPortStatsTxPkts64Octets_Object = MibTableColumn
etherPortStatsTxPkts64Octets = _EtherPortStatsTxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 6),
    _EtherPortStatsTxPkts64Octets_Type()
)
etherPortStatsTxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts64Octets.setStatus("current")
_EtherPortStatsTxPkts65to127Octets_Type = Counter32
_EtherPortStatsTxPkts65to127Octets_Object = MibTableColumn
etherPortStatsTxPkts65to127Octets = _EtherPortStatsTxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 7),
    _EtherPortStatsTxPkts65to127Octets_Type()
)
etherPortStatsTxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts65to127Octets.setStatus("current")
_EtherPortStatsTxPkts128to255Octets_Type = Counter32
_EtherPortStatsTxPkts128to255Octets_Object = MibTableColumn
etherPortStatsTxPkts128to255Octets = _EtherPortStatsTxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 8),
    _EtherPortStatsTxPkts128to255Octets_Type()
)
etherPortStatsTxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts128to255Octets.setStatus("current")
_EtherPortStatsTxPkts256to511Octets_Type = Counter32
_EtherPortStatsTxPkts256to511Octets_Object = MibTableColumn
etherPortStatsTxPkts256to511Octets = _EtherPortStatsTxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 9),
    _EtherPortStatsTxPkts256to511Octets_Type()
)
etherPortStatsTxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts256to511Octets.setStatus("current")
_EtherPortStatsTxPkts512to1023Octets_Type = Counter32
_EtherPortStatsTxPkts512to1023Octets_Object = MibTableColumn
etherPortStatsTxPkts512to1023Octets = _EtherPortStatsTxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 10),
    _EtherPortStatsTxPkts512to1023Octets_Type()
)
etherPortStatsTxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts512to1023Octets.setStatus("current")
_EtherPortStatsTxPkts1024to1518Octets_Type = Counter32
_EtherPortStatsTxPkts1024to1518Octets_Object = MibTableColumn
etherPortStatsTxPkts1024to1518Octets = _EtherPortStatsTxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 11),
    _EtherPortStatsTxPkts1024to1518Octets_Type()
)
etherPortStatsTxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts1024to1518Octets.setStatus("current")
_EtherPortStatsTxPkts1519to1530Octets_Type = Counter32
_EtherPortStatsTxPkts1519to1530Octets_Object = MibTableColumn
etherPortStatsTxPkts1519to1530Octets = _EtherPortStatsTxPkts1519to1530Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 12),
    _EtherPortStatsTxPkts1519to1530Octets_Type()
)
etherPortStatsTxPkts1519to1530Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxPkts1519to1530Octets.setStatus("current")
_EtherPortStatsTxFCSErrors_Type = Counter32
_EtherPortStatsTxFCSErrors_Object = MibTableColumn
etherPortStatsTxFCSErrors = _EtherPortStatsTxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 13),
    _EtherPortStatsTxFCSErrors_Type()
)
etherPortStatsTxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxFCSErrors.setStatus("current")
_EtherPortStatsTxOversize_Type = Counter32
_EtherPortStatsTxOversize_Object = MibTableColumn
etherPortStatsTxOversize = _EtherPortStatsTxOversize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 14),
    _EtherPortStatsTxOversize_Type()
)
etherPortStatsTxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxOversize.setStatus("current")
_EtherPortStatsTxUndersize_Type = Counter32
_EtherPortStatsTxUndersize_Object = MibTableColumn
etherPortStatsTxUndersize = _EtherPortStatsTxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 15),
    _EtherPortStatsTxUndersize_Type()
)
etherPortStatsTxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxUndersize.setStatus("current")
_EtherPortStatsTxControlFrames_Type = Counter32
_EtherPortStatsTxControlFrames_Object = MibTableColumn
etherPortStatsTxControlFrames = _EtherPortStatsTxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 16),
    _EtherPortStatsTxControlFrames_Type()
)
etherPortStatsTxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxControlFrames.setStatus("current")
_EtherPortStatsTxBadFifoUnderrun_Type = Counter32
_EtherPortStatsTxBadFifoUnderrun_Object = MibTableColumn
etherPortStatsTxBadFifoUnderrun = _EtherPortStatsTxBadFifoUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 17),
    _EtherPortStatsTxBadFifoUnderrun_Type()
)
etherPortStatsTxBadFifoUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxBadFifoUnderrun.setStatus("current")
_EtherPortStatsTxBadFifoOverrun_Type = Counter32
_EtherPortStatsTxBadFifoOverrun_Object = MibTableColumn
etherPortStatsTxBadFifoOverrun = _EtherPortStatsTxBadFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 18),
    _EtherPortStatsTxBadFifoOverrun_Type()
)
etherPortStatsTxBadFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxBadFifoOverrun.setStatus("current")
_EtherPortStatsTxDropFifoOverrun_Type = Counter32
_EtherPortStatsTxDropFifoOverrun_Object = MibTableColumn
etherPortStatsTxDropFifoOverrun = _EtherPortStatsTxDropFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 19),
    _EtherPortStatsTxDropFifoOverrun_Type()
)
etherPortStatsTxDropFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxDropFifoOverrun.setStatus("current")
_EtherPortStatsTxBadParityError_Type = Counter32
_EtherPortStatsTxBadParityError_Object = MibTableColumn
etherPortStatsTxBadParityError = _EtherPortStatsTxBadParityError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 20),
    _EtherPortStatsTxBadParityError_Type()
)
etherPortStatsTxBadParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxBadParityError.setStatus("current")
_EtherPortStatsTxDropParityError_Type = Counter32
_EtherPortStatsTxDropParityError_Object = MibTableColumn
etherPortStatsTxDropParityError = _EtherPortStatsTxDropParityError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 21),
    _EtherPortStatsTxDropParityError_Type()
)
etherPortStatsTxDropParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxDropParityError.setStatus("current")
_EtherPortStatsTxBadSequenceError_Type = Counter32
_EtherPortStatsTxBadSequenceError_Object = MibTableColumn
etherPortStatsTxBadSequenceError = _EtherPortStatsTxBadSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 22),
    _EtherPortStatsTxBadSequenceError_Type()
)
etherPortStatsTxBadSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxBadSequenceError.setStatus("current")
_EtherPortStatsTxDropSequenceError_Type = Counter32
_EtherPortStatsTxDropSequenceError_Object = MibTableColumn
etherPortStatsTxDropSequenceError = _EtherPortStatsTxDropSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 23),
    _EtherPortStatsTxDropSequenceError_Type()
)
etherPortStatsTxDropSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxDropSequenceError.setStatus("current")
_EtherPortStatsTxBadJamError_Type = Counter32
_EtherPortStatsTxBadJamError_Object = MibTableColumn
etherPortStatsTxBadJamError = _EtherPortStatsTxBadJamError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 24),
    _EtherPortStatsTxBadJamError_Type()
)
etherPortStatsTxBadJamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxBadJamError.setStatus("current")
_EtherPortStatsTxDropJamError_Type = Counter32
_EtherPortStatsTxDropJamError_Object = MibTableColumn
etherPortStatsTxDropJamError = _EtherPortStatsTxDropJamError_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 25),
    _EtherPortStatsTxDropJamError_Type()
)
etherPortStatsTxDropJamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsTxDropJamError.setStatus("current")


class _EtherPortSpeedTrapEnable_Type(Integer32):
    """Custom type etherPortSpeedTrapEnable based on Integer32"""
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


_EtherPortSpeedTrapEnable_Type.__name__ = "Integer32"
_EtherPortSpeedTrapEnable_Object = MibTableColumn
etherPortSpeedTrapEnable = _EtherPortSpeedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 26),
    _EtherPortSpeedTrapEnable_Type()
)
etherPortSpeedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortSpeedTrapEnable.setStatus("current")


class _EtherPortDuplexTrapEnable_Type(Integer32):
    """Custom type etherPortDuplexTrapEnable based on Integer32"""
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


_EtherPortDuplexTrapEnable_Type.__name__ = "Integer32"
_EtherPortDuplexTrapEnable_Object = MibTableColumn
etherPortDuplexTrapEnable = _EtherPortDuplexTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 27),
    _EtherPortDuplexTrapEnable_Type()
)
etherPortDuplexTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortDuplexTrapEnable.setStatus("current")


class _EtherPortAutonegTrapEnable_Type(Integer32):
    """Custom type etherPortAutonegTrapEnable based on Integer32"""
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


_EtherPortAutonegTrapEnable_Type.__name__ = "Integer32"
_EtherPortAutonegTrapEnable_Object = MibTableColumn
etherPortAutonegTrapEnable = _EtherPortAutonegTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 28),
    _EtherPortAutonegTrapEnable_Type()
)
etherPortAutonegTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortAutonegTrapEnable.setStatus("current")


class _EtherPortRowStatus_Type(Integer32):
    """Custom type etherPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2))
    )


_EtherPortRowStatus_Type.__name__ = "Integer32"
_EtherPortRowStatus_Object = MibTableColumn
etherPortRowStatus = _EtherPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 29),
    _EtherPortRowStatus_Type()
)
etherPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortRowStatus.setStatus("current")


class _EtherPortAutonegAdvSpeed_Type(Integer32):
    """Custom type etherPortAutonegAdvSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3))
    )


_EtherPortAutonegAdvSpeed_Type.__name__ = "Integer32"
_EtherPortAutonegAdvSpeed_Object = MibTableColumn
etherPortAutonegAdvSpeed = _EtherPortAutonegAdvSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 30),
    _EtherPortAutonegAdvSpeed_Type()
)
etherPortAutonegAdvSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortAutonegAdvSpeed.setStatus("current")


class _EtherPortAutonegAdvDuplex_Type(Integer32):
    """Custom type etherPortAutonegAdvDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("unknown", 1))
    )


_EtherPortAutonegAdvDuplex_Type.__name__ = "Integer32"
_EtherPortAutonegAdvDuplex_Object = MibTableColumn
etherPortAutonegAdvDuplex = _EtherPortAutonegAdvDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 31),
    _EtherPortAutonegAdvDuplex_Type()
)
etherPortAutonegAdvDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortAutonegAdvDuplex.setStatus("current")


class _EtherPortPauseStateReceived_Type(Integer32):
    """Custom type etherPortPauseStateReceived based on Integer32"""
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
        *(("enableRx", 3),
          ("enableTx", 2),
          ("enableTxRx", 4),
          ("noPause", 1),
          ("undefined", 5))
    )


_EtherPortPauseStateReceived_Type.__name__ = "Integer32"
_EtherPortPauseStateReceived_Object = MibTableColumn
etherPortPauseStateReceived = _EtherPortPauseStateReceived_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 32),
    _EtherPortPauseStateReceived_Type()
)
etherPortPauseStateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortPauseStateReceived.setStatus("current")


class _EtherPortVlanMode_Type(Integer32):
    """Custom type etherPortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("stripVID", 2),
          ("transparent", 3))
    )


_EtherPortVlanMode_Type.__name__ = "Integer32"
_EtherPortVlanMode_Object = MibTableColumn
etherPortVlanMode = _EtherPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 33),
    _EtherPortVlanMode_Type()
)
etherPortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortVlanMode.setStatus("current")
_EtherPortDefaultVlanId_Type = Integer32
_EtherPortDefaultVlanId_Object = MibTableColumn
etherPortDefaultVlanId = _EtherPortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 34),
    _EtherPortDefaultVlanId_Type()
)
etherPortDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortDefaultVlanId.setStatus("current")
_EtherPortRxOverrun_Type = Counter32
_EtherPortRxOverrun_Object = MibTableColumn
etherPortRxOverrun = _EtherPortRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 35),
    _EtherPortRxOverrun_Type()
)
etherPortRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxOverrun.setStatus("current")
_EtherPortRxSyncErrors_Type = Counter32
_EtherPortRxSyncErrors_Object = MibTableColumn
etherPortRxSyncErrors = _EtherPortRxSyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 36),
    _EtherPortRxSyncErrors_Type()
)
etherPortRxSyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxSyncErrors.setStatus("current")
_EtherPortRxDelSeqErrors_Type = Counter32
_EtherPortRxDelSeqErrors_Object = MibTableColumn
etherPortRxDelSeqErrors = _EtherPortRxDelSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 37),
    _EtherPortRxDelSeqErrors_Type()
)
etherPortRxDelSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxDelSeqErrors.setStatus("current")
_EtherPortRxFifoOverrunErrors_Type = Counter32
_EtherPortRxFifoOverrunErrors_Object = MibTableColumn
etherPortRxFifoOverrunErrors = _EtherPortRxFifoOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 38),
    _EtherPortRxFifoOverrunErrors_Type()
)
etherPortRxFifoOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxFifoOverrunErrors.setStatus("current")
_EtherPortRxControlFrames_Type = Counter32
_EtherPortRxControlFrames_Object = MibTableColumn
etherPortRxControlFrames = _EtherPortRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 39),
    _EtherPortRxControlFrames_Type()
)
etherPortRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxControlFrames.setStatus("current")
_EtherPortRxThreshOvrszFrames_Type = Counter32
_EtherPortRxThreshOvrszFrames_Object = MibTableColumn
etherPortRxThreshOvrszFrames = _EtherPortRxThreshOvrszFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 40),
    _EtherPortRxThreshOvrszFrames_Type()
)
etherPortRxThreshOvrszFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortRxThreshOvrszFrames.setStatus("current")
_EtherPortStatsRxPkts1519to1530Octets_Type = Counter32
_EtherPortStatsRxPkts1519to1530Octets_Object = MibTableColumn
etherPortStatsRxPkts1519to1530Octets = _EtherPortStatsRxPkts1519to1530Octets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 3, 1, 41),
    _EtherPortStatsRxPkts1519to1530Octets_Type()
)
etherPortStatsRxPkts1519to1530Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortStatsRxPkts1519to1530Octets.setStatus("current")
_TdmIoDS1PortTable_Object = MibTable
tdmIoDS1PortTable = _TdmIoDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4)
)
if mibBuilder.loadTexts:
    tdmIoDS1PortTable.setStatus("current")
_TdmIoDS1PortEntry_Object = MibTableRow
tdmIoDS1PortEntry = _TdmIoDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1)
)
tdmIoDS1PortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    tdmIoDS1PortEntry.setStatus("current")


class _TdmIoDS1PortType_Type(Integer32):
    """Custom type tdmIoDS1PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ds1", 1)
    )


_TdmIoDS1PortType_Type.__name__ = "Integer32"
_TdmIoDS1PortType_Object = MibTableColumn
tdmIoDS1PortType = _TdmIoDS1PortType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 1),
    _TdmIoDS1PortType_Type()
)
tdmIoDS1PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortType.setStatus("current")


class _TdmIoDS1PortTiming_Type(Integer32):
    """Custom type tdmIoDS1PortTiming based on Integer32"""
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


_TdmIoDS1PortTiming_Type.__name__ = "Integer32"
_TdmIoDS1PortTiming_Object = MibTableColumn
tdmIoDS1PortTiming = _TdmIoDS1PortTiming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 2),
    _TdmIoDS1PortTiming_Type()
)
tdmIoDS1PortTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortTiming.setStatus("current")


class _TdmIoDS1PortBuildOut_Type(Integer32):
    """Custom type tdmIoDS1PortBuildOut based on Integer32"""
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
        *(("longHaulOneFiveDB", 8),
          ("longHaulSevenFiveDB", 7),
          ("longHaulTwentyTwoDB", 9),
          ("longHaulZeroDB", 6),
          ("shortHaulMax133Feet", 1),
          ("shortHaulMax266Feet", 2),
          ("shortHaulMax399Feet", 3),
          ("shortHaulMax533Feet", 4),
          ("shortHaulMax655Feet", 5))
    )


_TdmIoDS1PortBuildOut_Type.__name__ = "Integer32"
_TdmIoDS1PortBuildOut_Object = MibTableColumn
tdmIoDS1PortBuildOut = _TdmIoDS1PortBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 5),
    _TdmIoDS1PortBuildOut_Type()
)
tdmIoDS1PortBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortBuildOut.setStatus("current")


class _TdmIoDS1PortFraming_Type(Integer32):
    """Custom type tdmIoDS1PortFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ds1unframed", 1)
    )


_TdmIoDS1PortFraming_Type.__name__ = "Integer32"
_TdmIoDS1PortFraming_Object = MibTableColumn
tdmIoDS1PortFraming = _TdmIoDS1PortFraming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 6),
    _TdmIoDS1PortFraming_Type()
)
tdmIoDS1PortFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortFraming.setStatus("current")


class _TdmIoDS1PortCoding_Type(Integer32):
    """Custom type tdmIoDS1PortCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2))
    )


_TdmIoDS1PortCoding_Type.__name__ = "Integer32"
_TdmIoDS1PortCoding_Object = MibTableColumn
tdmIoDS1PortCoding = _TdmIoDS1PortCoding_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 7),
    _TdmIoDS1PortCoding_Type()
)
tdmIoDS1PortCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortCoding.setStatus("current")


class _TdmIoDS1PortLoopbackState_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )


_TdmIoDS1PortLoopbackState_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackState_Object = MibTableColumn
tdmIoDS1PortLoopbackState = _TdmIoDS1PortLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 8),
    _TdmIoDS1PortLoopbackState_Type()
)
tdmIoDS1PortLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackState.setStatus("current")


class _TdmIoDS1PortLoopbackType_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("digitalOn", 9),
          ("localOn", 8),
          ("noLoop", 1),
          ("remoteOn", 10))
    )


_TdmIoDS1PortLoopbackType_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackType_Object = MibTableColumn
tdmIoDS1PortLoopbackType = _TdmIoDS1PortLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 9),
    _TdmIoDS1PortLoopbackType_Type()
)
tdmIoDS1PortLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackType.setStatus("current")


class _TdmIoDS1PortLoopbackResults_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 2))
    )


_TdmIoDS1PortLoopbackResults_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackResults_Object = MibTableColumn
tdmIoDS1PortLoopbackResults = _TdmIoDS1PortLoopbackResults_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 10),
    _TdmIoDS1PortLoopbackResults_Type()
)
tdmIoDS1PortLoopbackResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackResults.setStatus("current")
_TdmIoDS1PortLoopbackLLbActCode_Type = Integer32
_TdmIoDS1PortLoopbackLLbActCode_Object = MibTableColumn
tdmIoDS1PortLoopbackLLbActCode = _TdmIoDS1PortLoopbackLLbActCode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 11),
    _TdmIoDS1PortLoopbackLLbActCode_Type()
)
tdmIoDS1PortLoopbackLLbActCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLLbActCode.setStatus("current")
_TdmIoDS1PortLoopbackLLbDeactCode_Type = Integer32
_TdmIoDS1PortLoopbackLLbDeactCode_Object = MibTableColumn
tdmIoDS1PortLoopbackLLbDeactCode = _TdmIoDS1PortLoopbackLLbDeactCode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 12),
    _TdmIoDS1PortLoopbackLLbDeactCode_Type()
)
tdmIoDS1PortLoopbackLLbDeactCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLLbDeactCode.setStatus("current")


class _TdmIoDS1PortLoopbackLlbActCodeLen_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackLlbActCodeLen based on Integer32"""
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
        *(("up5Bit", 1),
          ("up6Bit", 2),
          ("up7Bit", 3),
          ("up8Bit", 4))
    )


_TdmIoDS1PortLoopbackLlbActCodeLen_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackLlbActCodeLen_Object = MibTableColumn
tdmIoDS1PortLoopbackLlbActCodeLen = _TdmIoDS1PortLoopbackLlbActCodeLen_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 13),
    _TdmIoDS1PortLoopbackLlbActCodeLen_Type()
)
tdmIoDS1PortLoopbackLlbActCodeLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLlbActCodeLen.setStatus("current")


class _TdmIoDS1PortLoopbackLlbDeactCodeLen_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackLlbDeactCodeLen based on Integer32"""
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
        *(("down5Bit", 1),
          ("down6Bit", 2),
          ("down7Bit", 3),
          ("down8Bit", 4))
    )


_TdmIoDS1PortLoopbackLlbDeactCodeLen_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackLlbDeactCodeLen_Object = MibTableColumn
tdmIoDS1PortLoopbackLlbDeactCodeLen = _TdmIoDS1PortLoopbackLlbDeactCodeLen_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 14),
    _TdmIoDS1PortLoopbackLlbDeactCodeLen_Type()
)
tdmIoDS1PortLoopbackLlbDeactCodeLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLlbDeactCodeLen.setStatus("current")


class _TdmIoDS1PortLoopbackLlbControl_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackLlbControl based on Integer32"""
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
        *(("genActOn", 2),
          ("genDeActOn", 3),
          ("genOff", 1),
          ("monOff", 4),
          ("monOn", 5))
    )


_TdmIoDS1PortLoopbackLlbControl_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackLlbControl_Object = MibTableColumn
tdmIoDS1PortLoopbackLlbControl = _TdmIoDS1PortLoopbackLlbControl_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 15),
    _TdmIoDS1PortLoopbackLlbControl_Type()
)
tdmIoDS1PortLoopbackLlbControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLlbControl.setStatus("current")


class _TdmIoDS1PortLoopbackLlbGenPath_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackLlbGenPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genRcv", 1),
          ("genXmit", 2))
    )


_TdmIoDS1PortLoopbackLlbGenPath_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackLlbGenPath_Object = MibTableColumn
tdmIoDS1PortLoopbackLlbGenPath = _TdmIoDS1PortLoopbackLlbGenPath_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 16),
    _TdmIoDS1PortLoopbackLlbGenPath_Type()
)
tdmIoDS1PortLoopbackLlbGenPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLlbGenPath.setStatus("current")


class _TdmIoDS1PortLoopbackLlbMonPath_Type(Integer32):
    """Custom type tdmIoDS1PortLoopbackLlbMonPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monRcv", 1),
          ("monXmit", 2))
    )


_TdmIoDS1PortLoopbackLlbMonPath_Type.__name__ = "Integer32"
_TdmIoDS1PortLoopbackLlbMonPath_Object = MibTableColumn
tdmIoDS1PortLoopbackLlbMonPath = _TdmIoDS1PortLoopbackLlbMonPath_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 17),
    _TdmIoDS1PortLoopbackLlbMonPath_Type()
)
tdmIoDS1PortLoopbackLlbMonPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLoopbackLlbMonPath.setStatus("current")


class _TdmIoDS1PortPrbsAlgorithm_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("algo215", 1),
          ("algo220", 2))
    )


_TdmIoDS1PortPrbsAlgorithm_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsAlgorithm_Object = MibTableColumn
tdmIoDS1PortPrbsAlgorithm = _TdmIoDS1PortPrbsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 18),
    _TdmIoDS1PortPrbsAlgorithm_Type()
)
tdmIoDS1PortPrbsAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsAlgorithm.setStatus("current")


class _TdmIoDS1PortPrbsInversion_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TdmIoDS1PortPrbsInversion_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsInversion_Object = MibTableColumn
tdmIoDS1PortPrbsInversion = _TdmIoDS1PortPrbsInversion_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 19),
    _TdmIoDS1PortPrbsInversion_Type()
)
tdmIoDS1PortPrbsInversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsInversion.setStatus("current")


class _TdmIoDS1PortPrbsGenPath_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsGenPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genRcv", 1),
          ("genXmit", 2))
    )


_TdmIoDS1PortPrbsGenPath_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsGenPath_Object = MibTableColumn
tdmIoDS1PortPrbsGenPath = _TdmIoDS1PortPrbsGenPath_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 20),
    _TdmIoDS1PortPrbsGenPath_Type()
)
tdmIoDS1PortPrbsGenPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsGenPath.setStatus("current")


class _TdmIoDS1PortPrbsMonPath_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsMonPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monRcv", 1),
          ("monXmit", 2))
    )


_TdmIoDS1PortPrbsMonPath_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsMonPath_Object = MibTableColumn
tdmIoDS1PortPrbsMonPath = _TdmIoDS1PortPrbsMonPath_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 21),
    _TdmIoDS1PortPrbsMonPath_Type()
)
tdmIoDS1PortPrbsMonPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsMonPath.setStatus("current")


class _TdmIoDS1PortPrbsMonitor_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TdmIoDS1PortPrbsMonitor_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsMonitor_Object = MibTableColumn
tdmIoDS1PortPrbsMonitor = _TdmIoDS1PortPrbsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 22),
    _TdmIoDS1PortPrbsMonitor_Type()
)
tdmIoDS1PortPrbsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsMonitor.setStatus("current")


class _TdmIoDS1PortPrbsTransmit_Type(Integer32):
    """Custom type tdmIoDS1PortPrbsTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TdmIoDS1PortPrbsTransmit_Type.__name__ = "Integer32"
_TdmIoDS1PortPrbsTransmit_Object = MibTableColumn
tdmIoDS1PortPrbsTransmit = _TdmIoDS1PortPrbsTransmit_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 23),
    _TdmIoDS1PortPrbsTransmit_Type()
)
tdmIoDS1PortPrbsTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsTransmit.setStatus("current")
_TdmIoDS1PortPrbsBec_Type = Counter32
_TdmIoDS1PortPrbsBec_Object = MibTableColumn
tdmIoDS1PortPrbsBec = _TdmIoDS1PortPrbsBec_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 24),
    _TdmIoDS1PortPrbsBec_Type()
)
tdmIoDS1PortPrbsBec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortPrbsBec.setStatus("current")


class _TdmIoDS1PortBertState_Type(Integer32):
    """Custom type tdmIoDS1PortBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("other", 3),
          ("running", 2))
    )


_TdmIoDS1PortBertState_Type.__name__ = "Integer32"
_TdmIoDS1PortBertState_Object = MibTableColumn
tdmIoDS1PortBertState = _TdmIoDS1PortBertState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 25),
    _TdmIoDS1PortBertState_Type()
)
tdmIoDS1PortBertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortBertState.setStatus("current")


class _TdmIoDS1PortBertPattern_Type(Integer32):
    """Custom type tdmIoDS1PortBertPattern based on Integer32"""
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
        *(("pattern211", 5),
          ("pattern215", 4),
          ("pattern220", 2),
          ("pattern223", 1),
          ("patternAllOnes", 7),
          ("patternAllZeros", 6),
          ("patternAlternate", 8),
          ("patternQrss", 3))
    )


_TdmIoDS1PortBertPattern_Type.__name__ = "Integer32"
_TdmIoDS1PortBertPattern_Object = MibTableColumn
tdmIoDS1PortBertPattern = _TdmIoDS1PortBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 26),
    _TdmIoDS1PortBertPattern_Type()
)
tdmIoDS1PortBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortBertPattern.setStatus("current")


class _TdmIoDS1PortBertDuration_Type(Integer32):
    """Custom type tdmIoDS1PortBertDuration based on Integer32"""
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
        *(("fiveMin", 2),
          ("oneHour", 4),
          ("oneMin", 1),
          ("thirtyMin", 3),
          ("twelveHour", 5),
          ("twentyfourHour", 6))
    )


_TdmIoDS1PortBertDuration_Type.__name__ = "Integer32"
_TdmIoDS1PortBertDuration_Object = MibTableColumn
tdmIoDS1PortBertDuration = _TdmIoDS1PortBertDuration_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 27),
    _TdmIoDS1PortBertDuration_Type()
)
tdmIoDS1PortBertDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortBertDuration.setStatus("current")


class _TdmIoDS1PortBertResults_Type(Integer32):
    """Custom type tdmIoDS1PortBertResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timeLeft", 1),
          ("totalBitErrs", 2),
          ("totalBits", 3))
    )


_TdmIoDS1PortBertResults_Type.__name__ = "Integer32"
_TdmIoDS1PortBertResults_Object = MibTableColumn
tdmIoDS1PortBertResults = _TdmIoDS1PortBertResults_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 28),
    _TdmIoDS1PortBertResults_Type()
)
tdmIoDS1PortBertResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortBertResults.setStatus("current")


class _TdmIoDS1PortLineESS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortLineESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortLineESS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortLineESS15Min_Object = MibTableColumn
tdmIoDS1PortLineESS15Min = _TdmIoDS1PortLineESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 29),
    _TdmIoDS1PortLineESS15Min_Type()
)
tdmIoDS1PortLineESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLineESS15Min.setStatus("current")


class _TdmIoDS1PortPathESS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortPathESS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathESS15Min_Object = MibTableColumn
tdmIoDS1PortPathESS15Min = _TdmIoDS1PortPathESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 30),
    _TdmIoDS1PortPathESS15Min_Type()
)
tdmIoDS1PortPathESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathESS15Min.setStatus("current")


class _TdmIoDS1PortLineESS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortLineESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS1PortLineESS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortLineESS1Day_Object = MibTableColumn
tdmIoDS1PortLineESS1Day = _TdmIoDS1PortLineESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 31),
    _TdmIoDS1PortLineESS1Day_Type()
)
tdmIoDS1PortLineESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortLineESS1Day.setStatus("current")


class _TdmIoDS1PortPathESS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortPathESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS1PortPathESS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortPathESS1Day_Object = MibTableColumn
tdmIoDS1PortPathESS1Day = _TdmIoDS1PortPathESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 32),
    _TdmIoDS1PortPathESS1Day_Type()
)
tdmIoDS1PortPathESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathESS1Day.setStatus("current")


class _TdmIoDS1PortPathCVS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_TdmIoDS1PortPathCVS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathCVS15Min_Object = MibTableColumn
tdmIoDS1PortPathCVS15Min = _TdmIoDS1PortPathCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 33),
    _TdmIoDS1PortPathCVS15Min_Type()
)
tdmIoDS1PortPathCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathCVS15Min.setStatus("current")


class _TdmIoDS1PortPathCVS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortPathCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_TdmIoDS1PortPathCVS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortPathCVS1Day_Object = MibTableColumn
tdmIoDS1PortPathCVS1Day = _TdmIoDS1PortPathCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 34),
    _TdmIoDS1PortPathCVS1Day_Type()
)
tdmIoDS1PortPathCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathCVS1Day.setStatus("current")


class _TdmIoDS1PortPathSESS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortPathSESS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathSESS15Min_Object = MibTableColumn
tdmIoDS1PortPathSESS15Min = _TdmIoDS1PortPathSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 35),
    _TdmIoDS1PortPathSESS15Min_Type()
)
tdmIoDS1PortPathSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathSESS15Min.setStatus("current")


class _TdmIoDS1PortPathSESS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortPathSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS1PortPathSESS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortPathSESS1Day_Object = MibTableColumn
tdmIoDS1PortPathSESS1Day = _TdmIoDS1PortPathSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 36),
    _TdmIoDS1PortPathSESS1Day_Type()
)
tdmIoDS1PortPathSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathSESS1Day.setStatus("current")


class _TdmIoDS1PortPathSASS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathSASS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortPathSASS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathSASS15Min_Object = MibTableColumn
tdmIoDS1PortPathSASS15Min = _TdmIoDS1PortPathSASS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 37),
    _TdmIoDS1PortPathSASS15Min_Type()
)
tdmIoDS1PortPathSASS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathSASS15Min.setStatus("current")


class _TdmIoDS1PortPathSASS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortPathSASS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS1PortPathSASS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortPathSASS1Day_Object = MibTableColumn
tdmIoDS1PortPathSASS1Day = _TdmIoDS1PortPathSASS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 38),
    _TdmIoDS1PortPathSASS1Day_Type()
)
tdmIoDS1PortPathSASS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathSASS1Day.setStatus("current")


class _TdmIoDS1PortPathCSS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathCSS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortPathCSS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathCSS15Min_Object = MibTableColumn
tdmIoDS1PortPathCSS15Min = _TdmIoDS1PortPathCSS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 39),
    _TdmIoDS1PortPathCSS15Min_Type()
)
tdmIoDS1PortPathCSS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathCSS15Min.setStatus("current")


class _TdmIoDS1PortPathCSS1Day_Type(Integer32):
    """Custom type tdmIoDS1PortPathCSS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS1PortPathCSS1Day_Type.__name__ = "Integer32"
_TdmIoDS1PortPathCSS1Day_Object = MibTableColumn
tdmIoDS1PortPathCSS1Day = _TdmIoDS1PortPathCSS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 40),
    _TdmIoDS1PortPathCSS1Day_Type()
)
tdmIoDS1PortPathCSS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathCSS1Day.setStatus("current")


class _TdmIoDS1PortPathUASS15Min_Type(Integer32):
    """Custom type tdmIoDS1PortPathUASS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS1PortPathUASS15Min_Type.__name__ = "Integer32"
_TdmIoDS1PortPathUASS15Min_Object = MibTableColumn
tdmIoDS1PortPathUASS15Min = _TdmIoDS1PortPathUASS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 41),
    _TdmIoDS1PortPathUASS15Min_Type()
)
tdmIoDS1PortPathUASS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortPathUASS15Min.setStatus("current")


class _TdmIoDS1PortRowStatus_Type(Integer32):
    """Custom type tdmIoDS1PortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2))
    )


_TdmIoDS1PortRowStatus_Type.__name__ = "Integer32"
_TdmIoDS1PortRowStatus_Object = MibTableColumn
tdmIoDS1PortRowStatus = _TdmIoDS1PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 42),
    _TdmIoDS1PortRowStatus_Type()
)
tdmIoDS1PortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS1PortRowStatus.setStatus("current")


class _DsxStatus_Type(Integer32):
    """Custom type dsxStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dsx-exz-failure-cleared", 18),
          ("dsx-exz-failure-declared", 17),
          ("dsx-lof-failure-cleared", 12),
          ("dsx-lof-failure-declared", 11),
          ("dsx-los-failure-cleared", 10),
          ("dsx-los-failure-declared", 9),
          ("dsx-other-failure-cleared", 14),
          ("dsx-other-failure-declared", 13),
          ("dsx-pden-failure-cleared", 20),
          ("dsx-pden-failure-declared", 19),
          ("dsx-rcvais-failure-cleared", 6),
          ("dsx-rcvais-failure-declared", 5),
          ("dsx-rcvrai-failure-cleared", 2),
          ("dsx-rcvrai-failure-declared", 1),
          ("dsx-uas-failure-cleared", 16),
          ("dsx-uas-failure-declared", 15),
          ("dsx-xmitais-failure-cleared", 8),
          ("dsx-xmitais-failure-declared", 7),
          ("dsx-xmitrai-failure-cleared", 4),
          ("dsx-xmitrai-failure-declared", 3))
    )


_DsxStatus_Type.__name__ = "Integer32"
_DsxStatus_Object = MibTableColumn
dsxStatus = _DsxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 43),
    _DsxStatus_Type()
)
dsxStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsxStatus.setStatus("current")
_TdmIoDS1PortLCVCount_Type = Integer32
_TdmIoDS1PortLCVCount_Object = MibTableColumn
tdmIoDS1PortLCVCount = _TdmIoDS1PortLCVCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 4, 1, 44),
    _TdmIoDS1PortLCVCount_Type()
)
tdmIoDS1PortLCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoDS1PortLCVCount.setStatus("current")
_SonetPortTable_Object = MibTable
sonetPortTable = _SonetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5)
)
if mibBuilder.loadTexts:
    sonetPortTable.setStatus("current")
_SonetPortEntry_Object = MibTableRow
sonetPortEntry = _SonetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1)
)
sonetPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    sonetPortEntry.setStatus("current")


class _SonetPortType_Type(Integer32):
    """Custom type sonetPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oc12c", 1),
          ("oc12sts1", 2))
    )


_SonetPortType_Type.__name__ = "Integer32"
_SonetPortType_Object = MibTableColumn
sonetPortType = _SonetPortType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 1),
    _SonetPortType_Type()
)
sonetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortType.setStatus("current")
_SonetPortIdString_Type = OctetString
_SonetPortIdString_Object = MibTableColumn
sonetPortIdString = _SonetPortIdString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 2),
    _SonetPortIdString_Type()
)
sonetPortIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortIdString.setStatus("current")


class _SonetPortTiming_Type(Integer32):
    """Custom type sonetPortTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_SonetPortTiming_Type.__name__ = "Integer32"
_SonetPortTiming_Object = MibTableColumn
sonetPortTiming = _SonetPortTiming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 3),
    _SonetPortTiming_Type()
)
sonetPortTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortTiming.setStatus("current")


class _SonetPortLoopback_Type(Integer32):
    """Custom type sonetPortLoopback based on Integer32"""
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
        *(("none", 5),
          ("pdle", 3),
          ("sdle", 2),
          ("sllben", 4),
          ("slle", 1))
    )


_SonetPortLoopback_Type.__name__ = "Integer32"
_SonetPortLoopback_Object = MibTableColumn
sonetPortLoopback = _SonetPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 4),
    _SonetPortLoopback_Type()
)
sonetPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLoopback.setStatus("current")


class _SonetPortScrambling_Type(Integer32):
    """Custom type sonetPortScrambling based on Integer32"""
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


_SonetPortScrambling_Type.__name__ = "Integer32"
_SonetPortScrambling_Object = MibTableColumn
sonetPortScrambling = _SonetPortScrambling_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 5),
    _SonetPortScrambling_Type()
)
sonetPortScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortScrambling.setStatus("current")


class _SonetPortChannelization_Type(Integer32):
    """Custom type sonetPortChannelization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concatenated", 1),
          ("nonConcatenated", 2))
    )


_SonetPortChannelization_Type.__name__ = "Integer32"
_SonetPortChannelization_Object = MibTableColumn
sonetPortChannelization = _SonetPortChannelization_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 6),
    _SonetPortChannelization_Type()
)
sonetPortChannelization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortChannelization.setStatus("current")
_SonetPortConfigedChans_Type = Unsigned32
_SonetPortConfigedChans_Object = MibTableColumn
sonetPortConfigedChans = _SonetPortConfigedChans_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 7),
    _SonetPortConfigedChans_Type()
)
sonetPortConfigedChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPortConfigedChans.setStatus("current")


class _SonetPortSectESS15Min_Type(Integer32):
    """Custom type sonetPortSectESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortSectESS15Min_Type.__name__ = "Integer32"
_SonetPortSectESS15Min_Object = MibTableColumn
sonetPortSectESS15Min = _SonetPortSectESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 8),
    _SonetPortSectESS15Min_Type()
)
sonetPortSectESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectESS15Min.setStatus("current")


class _SonetPortLineESS15Min_Type(Integer32):
    """Custom type sonetPortLineESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortLineESS15Min_Type.__name__ = "Integer32"
_SonetPortLineESS15Min_Object = MibTableColumn
sonetPortLineESS15Min = _SonetPortLineESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 9),
    _SonetPortLineESS15Min_Type()
)
sonetPortLineESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineESS15Min.setStatus("current")


class _SonetPortPathESS15Min_Type(Integer32):
    """Custom type sonetPortPathESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortPathESS15Min_Type.__name__ = "Integer32"
_SonetPortPathESS15Min_Object = MibTableColumn
sonetPortPathESS15Min = _SonetPortPathESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 10),
    _SonetPortPathESS15Min_Type()
)
sonetPortPathESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathESS15Min.setStatus("current")


class _SonetPortSectESS1Day_Type(Integer32):
    """Custom type sonetPortSectESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortSectESS1Day_Type.__name__ = "Integer32"
_SonetPortSectESS1Day_Object = MibTableColumn
sonetPortSectESS1Day = _SonetPortSectESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 11),
    _SonetPortSectESS1Day_Type()
)
sonetPortSectESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectESS1Day.setStatus("current")


class _SonetPortLineESS1Day_Type(Integer32):
    """Custom type sonetPortLineESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortLineESS1Day_Type.__name__ = "Integer32"
_SonetPortLineESS1Day_Object = MibTableColumn
sonetPortLineESS1Day = _SonetPortLineESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 12),
    _SonetPortLineESS1Day_Type()
)
sonetPortLineESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineESS1Day.setStatus("current")


class _SonetPortPathESS1Day_Type(Integer32):
    """Custom type sonetPortPathESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortPathESS1Day_Type.__name__ = "Integer32"
_SonetPortPathESS1Day_Object = MibTableColumn
sonetPortPathESS1Day = _SonetPortPathESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 13),
    _SonetPortPathESS1Day_Type()
)
sonetPortPathESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathESS1Day.setStatus("current")


class _SonetPortSectCVS15Min_Type(Integer32):
    """Custom type sonetPortSectCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonetPortSectCVS15Min_Type.__name__ = "Integer32"
_SonetPortSectCVS15Min_Object = MibTableColumn
sonetPortSectCVS15Min = _SonetPortSectCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 14),
    _SonetPortSectCVS15Min_Type()
)
sonetPortSectCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectCVS15Min.setStatus("current")


class _SonetPortLineCVS15Min_Type(Integer32):
    """Custom type sonetPortLineCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonetPortLineCVS15Min_Type.__name__ = "Integer32"
_SonetPortLineCVS15Min_Object = MibTableColumn
sonetPortLineCVS15Min = _SonetPortLineCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 15),
    _SonetPortLineCVS15Min_Type()
)
sonetPortLineCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineCVS15Min.setStatus("current")


class _SonetPortPathCVS15Min_Type(Integer32):
    """Custom type sonetPortPathCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonetPortPathCVS15Min_Type.__name__ = "Integer32"
_SonetPortPathCVS15Min_Object = MibTableColumn
sonetPortPathCVS15Min = _SonetPortPathCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 16),
    _SonetPortPathCVS15Min_Type()
)
sonetPortPathCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathCVS15Min.setStatus("current")


class _SonetPortSectCVS1Day_Type(Integer32):
    """Custom type sonetPortSectCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonetPortSectCVS1Day_Type.__name__ = "Integer32"
_SonetPortSectCVS1Day_Object = MibTableColumn
sonetPortSectCVS1Day = _SonetPortSectCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 17),
    _SonetPortSectCVS1Day_Type()
)
sonetPortSectCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectCVS1Day.setStatus("current")


class _SonetPortLineCVS1Day_Type(Integer32):
    """Custom type sonetPortLineCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonetPortLineCVS1Day_Type.__name__ = "Integer32"
_SonetPortLineCVS1Day_Object = MibTableColumn
sonetPortLineCVS1Day = _SonetPortLineCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 18),
    _SonetPortLineCVS1Day_Type()
)
sonetPortLineCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineCVS1Day.setStatus("current")


class _SonetPortPathCVS1Day_Type(Integer32):
    """Custom type sonetPortPathCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonetPortPathCVS1Day_Type.__name__ = "Integer32"
_SonetPortPathCVS1Day_Object = MibTableColumn
sonetPortPathCVS1Day = _SonetPortPathCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 19),
    _SonetPortPathCVS1Day_Type()
)
sonetPortPathCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathCVS1Day.setStatus("current")


class _SonetPortSectSESS15Min_Type(Integer32):
    """Custom type sonetPortSectSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortSectSESS15Min_Type.__name__ = "Integer32"
_SonetPortSectSESS15Min_Object = MibTableColumn
sonetPortSectSESS15Min = _SonetPortSectSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 20),
    _SonetPortSectSESS15Min_Type()
)
sonetPortSectSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectSESS15Min.setStatus("current")


class _SonetPortLineSESS15Min_Type(Integer32):
    """Custom type sonetPortLineSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortLineSESS15Min_Type.__name__ = "Integer32"
_SonetPortLineSESS15Min_Object = MibTableColumn
sonetPortLineSESS15Min = _SonetPortLineSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 21),
    _SonetPortLineSESS15Min_Type()
)
sonetPortLineSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineSESS15Min.setStatus("current")


class _SonetPortPathSESS15Min_Type(Integer32):
    """Custom type sonetPortPathSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortPathSESS15Min_Type.__name__ = "Integer32"
_SonetPortPathSESS15Min_Object = MibTableColumn
sonetPortPathSESS15Min = _SonetPortPathSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 22),
    _SonetPortPathSESS15Min_Type()
)
sonetPortPathSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathSESS15Min.setStatus("current")


class _SonetPortSectSESS1Day_Type(Integer32):
    """Custom type sonetPortSectSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortSectSESS1Day_Type.__name__ = "Integer32"
_SonetPortSectSESS1Day_Object = MibTableColumn
sonetPortSectSESS1Day = _SonetPortSectSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 23),
    _SonetPortSectSESS1Day_Type()
)
sonetPortSectSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortSectSESS1Day.setStatus("current")


class _SonetPortLineSESS1Day_Type(Integer32):
    """Custom type sonetPortLineSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortLineSESS1Day_Type.__name__ = "Integer32"
_SonetPortLineSESS1Day_Object = MibTableColumn
sonetPortLineSESS1Day = _SonetPortLineSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 24),
    _SonetPortLineSESS1Day_Type()
)
sonetPortLineSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineSESS1Day.setStatus("current")


class _SonetPortPathSESS1Day_Type(Integer32):
    """Custom type sonetPortPathSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortPathSESS1Day_Type.__name__ = "Integer32"
_SonetPortPathSESS1Day_Object = MibTableColumn
sonetPortPathSESS1Day = _SonetPortPathSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 25),
    _SonetPortPathSESS1Day_Type()
)
sonetPortPathSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathSESS1Day.setStatus("current")


class _SonetPortLineUASS15Min_Type(Integer32):
    """Custom type sonetPortLineUASS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortLineUASS15Min_Type.__name__ = "Integer32"
_SonetPortLineUASS15Min_Object = MibTableColumn
sonetPortLineUASS15Min = _SonetPortLineUASS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 26),
    _SonetPortLineUASS15Min_Type()
)
sonetPortLineUASS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineUASS15Min.setStatus("current")


class _SonetPortPathUASS15Min_Type(Integer32):
    """Custom type sonetPortPathUASS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetPortPathUASS15Min_Type.__name__ = "Integer32"
_SonetPortPathUASS15Min_Object = MibTableColumn
sonetPortPathUASS15Min = _SonetPortPathUASS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 27),
    _SonetPortPathUASS15Min_Type()
)
sonetPortPathUASS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathUASS15Min.setStatus("current")


class _SonetPortLineUASS1Day_Type(Integer32):
    """Custom type sonetPortLineUASS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortLineUASS1Day_Type.__name__ = "Integer32"
_SonetPortLineUASS1Day_Object = MibTableColumn
sonetPortLineUASS1Day = _SonetPortLineUASS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 28),
    _SonetPortLineUASS1Day_Type()
)
sonetPortLineUASS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLineUASS1Day.setStatus("current")


class _SonetPortPathUASS1Day_Type(Integer32):
    """Custom type sonetPortPathUASS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetPortPathUASS1Day_Type.__name__ = "Integer32"
_SonetPortPathUASS1Day_Object = MibTableColumn
sonetPortPathUASS1Day = _SonetPortPathUASS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 29),
    _SonetPortPathUASS1Day_Type()
)
sonetPortPathUASS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPathUASS1Day.setStatus("current")


class _SonetPortRowStatus_Type(Integer32):
    """Custom type sonetPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2))
    )


_SonetPortRowStatus_Type.__name__ = "Integer32"
_SonetPortRowStatus_Object = MibTableColumn
sonetPortRowStatus = _SonetPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 30),
    _SonetPortRowStatus_Type()
)
sonetPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortRowStatus.setStatus("current")


class _SonetTCAStatus_Type(Integer32):
    """Custom type sonetTCAStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("sonet-line-cv-tca-declared", 4),
          ("sonet-line-es-tca-declared", 6),
          ("sonet-line-farend-cv-tca-declared", 8),
          ("sonet-line-farend-es-tca-declared", 10),
          ("sonet-line-farend-ses-tca-declared", 9),
          ("sonet-line-farend-uas-tca-declared", 11),
          ("sonet-line-ses-tca-declared", 5),
          ("sonet-line-uas-tca-declared", 7),
          ("sonet-path-cv-tca-declared", 12),
          ("sonet-path-es-tca-declared", 14),
          ("sonet-path-farend-cv-tca-declared", 16),
          ("sonet-path-farend-es-tca-declared", 18),
          ("sonet-path-farend-ses-tca-declared", 17),
          ("sonet-path-farend-uas-tca-declared", 19),
          ("sonet-path-ses-tca-declared", 13),
          ("sonet-path-uas-tca-declared", 15),
          ("sonet-section-cv-tca-declared", 1),
          ("sonet-section-es-tca-declared", 3),
          ("sonet-section-ses-tca-declared", 2),
          ("sonet-vt-cv-tca-declared", 20),
          ("sonet-vt-es-tca-declared", 22),
          ("sonet-vt-farend-cv-tca-declared", 24),
          ("sonet-vt-farend-es-tca-declared", 26),
          ("sonet-vt-farend-ses-tca-declared", 25),
          ("sonet-vt-farend-uas-tca-declared", 27),
          ("sonet-vt-ses-tca-declared", 21),
          ("sonet-vt-uas-tca-declared", 23))
    )


_SonetTCAStatus_Type.__name__ = "Integer32"
_SonetTCAStatus_Object = MibTableColumn
sonetTCAStatus = _SonetTCAStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 5, 1, 31),
    _SonetTCAStatus_Type()
)
sonetTCAStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sonetTCAStatus.setStatus("current")
_AtmPortTable_Object = MibTable
atmPortTable = _AtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6)
)
if mibBuilder.loadTexts:
    atmPortTable.setStatus("current")
_AtmPortEntry_Object = MibTableRow
atmPortEntry = _AtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1)
)
atmPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    atmPortEntry.setStatus("current")
_AtmPortVPTunnel_Type = TruthValue
_AtmPortVPTunnel_Object = MibTableColumn
atmPortVPTunnel = _AtmPortVPTunnel_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 1),
    _AtmPortVPTunnel_Type()
)
atmPortVPTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortVPTunnel.setStatus("current")
_AtmPortMaxTotalBits_Type = Integer32
_AtmPortMaxTotalBits_Object = MibTableColumn
atmPortMaxTotalBits = _AtmPortMaxTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 2),
    _AtmPortMaxTotalBits_Type()
)
atmPortMaxTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortMaxTotalBits.setStatus("current")


class _AtmPortTiming_Type(Integer32):
    """Custom type atmPortTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("loop", 2))
    )


_AtmPortTiming_Type.__name__ = "Integer32"
_AtmPortTiming_Object = MibTableColumn
atmPortTiming = _AtmPortTiming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 3),
    _AtmPortTiming_Type()
)
atmPortTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortTiming.setStatus("current")
_AtmPortInCells_Type = Counter32
_AtmPortInCells_Object = MibTableColumn
atmPortInCells = _AtmPortInCells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 4),
    _AtmPortInCells_Type()
)
atmPortInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortInCells.setStatus("current")
_AtmPortOutCells_Type = Counter32
_AtmPortOutCells_Object = MibTableColumn
atmPortOutCells = _AtmPortOutCells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 5),
    _AtmPortOutCells_Type()
)
atmPortOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortOutCells.setStatus("current")


class _AtmPortCDVT_Type(Integer32):
    """Custom type atmPortCDVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 100000),
    )


_AtmPortCDVT_Type.__name__ = "Integer32"
_AtmPortCDVT_Object = MibTableColumn
atmPortCDVT = _AtmPortCDVT_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 6),
    _AtmPortCDVT_Type()
)
atmPortCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortCDVT.setStatus("current")
_AtmPortMaxActvBits_Type = OctetString
_AtmPortMaxActvBits_Object = MibTableColumn
atmPortMaxActvBits = _AtmPortMaxActvBits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 7),
    _AtmPortMaxActvBits_Type()
)
atmPortMaxActvBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortMaxActvBits.setStatus("current")
_AtmPortHCInCells_Type = Counter64
_AtmPortHCInCells_Object = MibTableColumn
atmPortHCInCells = _AtmPortHCInCells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 8),
    _AtmPortHCInCells_Type()
)
atmPortHCInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortHCInCells.setStatus("current")
_AtmPortHCOutCells_Type = Counter64
_AtmPortHCOutCells_Object = MibTableColumn
atmPortHCOutCells = _AtmPortHCOutCells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 9),
    _AtmPortHCOutCells_Type()
)
atmPortHCOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortHCOutCells.setStatus("current")


class _AtmPortRowStatus_Type(Integer32):
    """Custom type atmPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2))
    )


_AtmPortRowStatus_Type.__name__ = "Integer32"
_AtmPortRowStatus_Object = MibTableColumn
atmPortRowStatus = _AtmPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 6, 1, 10),
    _AtmPortRowStatus_Type()
)
atmPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortRowStatus.setStatus("current")
_OpticalPortTable_Object = MibTable
opticalPortTable = _OpticalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7)
)
if mibBuilder.loadTexts:
    opticalPortTable.setStatus("current")
_OpticalPortEntry_Object = MibTableRow
opticalPortEntry = _OpticalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1)
)
opticalPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
    (0, "PORT-MIB", "lambda"),
)
if mibBuilder.loadTexts:
    opticalPortEntry.setStatus("current")
__pysmi_lambda_Type = Integer32
__pysmi_lambda_Object = MibScalar
_pysmi_lambda = __pysmi_lambda_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 1),
    __pysmi_lambda_Type()
)
_pysmi_lambda.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    _pysmi_lambda.setStatus("current")


class _OpticalPortMode_Type(Integer32):
    """Custom type opticalPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("protected", 3),
          ("working", 2))
    )


_OpticalPortMode_Type.__name__ = "Integer32"
_OpticalPortMode_Object = MibTableColumn
opticalPortMode = _OpticalPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 2),
    _OpticalPortMode_Type()
)
opticalPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalPortMode.setStatus("current")


class _OpticalPortRxSMselect_Type(Integer32):
    """Custom type opticalPortRxSMselect based on Integer32"""
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
        *(("both", 3),
          ("none", 4),
          ("primary", 1),
          ("reserve", 2))
    )


_OpticalPortRxSMselect_Type.__name__ = "Integer32"
_OpticalPortRxSMselect_Object = MibTableColumn
opticalPortRxSMselect = _OpticalPortRxSMselect_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 3),
    _OpticalPortRxSMselect_Type()
)
opticalPortRxSMselect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opticalPortRxSMselect.setStatus("current")


class _OpticalPortTxSMselect_Type(Integer32):
    """Custom type opticalPortTxSMselect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("reserve", 2))
    )


_OpticalPortTxSMselect_Type.__name__ = "Integer32"
_OpticalPortTxSMselect_Object = MibTableColumn
opticalPortTxSMselect = _OpticalPortTxSMselect_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 4),
    _OpticalPortTxSMselect_Type()
)
opticalPortTxSMselect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalPortTxSMselect.setStatus("current")


class _OpticalPortRxSignalState_Type(Integer32):
    """Custom type opticalPortRxSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("lossOfSignal", 2))
    )


_OpticalPortRxSignalState_Type.__name__ = "Integer32"
_OpticalPortRxSignalState_Object = MibTableColumn
opticalPortRxSignalState = _OpticalPortRxSignalState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 5),
    _OpticalPortRxSignalState_Type()
)
opticalPortRxSignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPortRxSignalState.setStatus("current")


class _OpticalPortRxFrameState_Type(Integer32):
    """Custom type opticalPortRxFrameState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 2),
          ("lossOfFrame", 1))
    )


_OpticalPortRxFrameState_Type.__name__ = "Integer32"
_OpticalPortRxFrameState_Object = MibTableColumn
opticalPortRxFrameState = _OpticalPortRxFrameState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 6),
    _OpticalPortRxFrameState_Type()
)
opticalPortRxFrameState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPortRxFrameState.setStatus("current")


class _OpticalPortTxStatus_Type(Integer32):
    """Custom type opticalPortTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_OpticalPortTxStatus_Type.__name__ = "Integer32"
_OpticalPortTxStatus_Object = MibTableColumn
opticalPortTxStatus = _OpticalPortTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 7),
    _OpticalPortTxStatus_Type()
)
opticalPortTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPortTxStatus.setStatus("current")


class _OpticalPortTxEnable_Type(Integer32):
    """Custom type opticalPortTxEnable based on Integer32"""
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


_OpticalPortTxEnable_Type.__name__ = "Integer32"
_OpticalPortTxEnable_Object = MibTableColumn
opticalPortTxEnable = _OpticalPortTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 8),
    _OpticalPortTxEnable_Type()
)
opticalPortTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalPortTxEnable.setStatus("current")


class _OpticalPortLaserPowerLevel_Type(Integer32):
    """Custom type opticalPortLaserPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_OpticalPortLaserPowerLevel_Type.__name__ = "Integer32"
_OpticalPortLaserPowerLevel_Object = MibTableColumn
opticalPortLaserPowerLevel = _OpticalPortLaserPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 9),
    _OpticalPortLaserPowerLevel_Type()
)
opticalPortLaserPowerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opticalPortLaserPowerLevel.setStatus("current")


class _OpticalPortLaserWavelength_Type(Integer32):
    """Custom type opticalPortLaserWavelength based on Integer32"""
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
        *(("fifteenFifty", 3),
          ("fifteenXX", 1),
          ("thirteenTen", 2),
          ("thirteenTenFifteenFifty", 4))
    )


_OpticalPortLaserWavelength_Type.__name__ = "Integer32"
_OpticalPortLaserWavelength_Object = MibTableColumn
opticalPortLaserWavelength = _OpticalPortLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 10),
    _OpticalPortLaserWavelength_Type()
)
opticalPortLaserWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalPortLaserWavelength.setStatus("current")


class _OpticalPortRowStatus_Type(Integer32):
    """Custom type opticalPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )


_OpticalPortRowStatus_Type.__name__ = "Integer32"
_OpticalPortRowStatus_Object = MibTableColumn
opticalPortRowStatus = _OpticalPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 7, 1, 11),
    _OpticalPortRowStatus_Type()
)
opticalPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalPortRowStatus.setStatus("current")
_RingPortTable_Object = MibTable
ringPortTable = _RingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8)
)
if mibBuilder.loadTexts:
    ringPortTable.setStatus("current")
_RingPortEntry_Object = MibTableRow
ringPortEntry = _RingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1)
)
ringPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    ringPortEntry.setStatus("current")
_RingPortArbiterEnabled_Type = TruthValue
_RingPortArbiterEnabled_Object = MibTableColumn
ringPortArbiterEnabled = _RingPortArbiterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 1),
    _RingPortArbiterEnabled_Type()
)
ringPortArbiterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortArbiterEnabled.setStatus("current")


class _RingPortFrameMode_Type(Integer32):
    """Custom type ringPortFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("axson", 1),
          ("pos", 2))
    )


_RingPortFrameMode_Type.__name__ = "Integer32"
_RingPortFrameMode_Object = MibTableColumn
ringPortFrameMode = _RingPortFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 2),
    _RingPortFrameMode_Type()
)
ringPortFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortFrameMode.setStatus("current")


class _RingPortMaxChannels_Type(Integer32):
    """Custom type ringPortMaxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RingPortMaxChannels_Type.__name__ = "Integer32"
_RingPortMaxChannels_Object = MibTableColumn
ringPortMaxChannels = _RingPortMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 3),
    _RingPortMaxChannels_Type()
)
ringPortMaxChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortMaxChannels.setStatus("current")


class _RingPortMaxSubChannels_Type(Integer32):
    """Custom type ringPortMaxSubChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RingPortMaxSubChannels_Type.__name__ = "Integer32"
_RingPortMaxSubChannels_Object = MibTableColumn
ringPortMaxSubChannels = _RingPortMaxSubChannels_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 4),
    _RingPortMaxSubChannels_Type()
)
ringPortMaxSubChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortMaxSubChannels.setStatus("current")
_RingPortAutoQueueSizing_Type = TruthValue
_RingPortAutoQueueSizing_Object = MibTableColumn
ringPortAutoQueueSizing = _RingPortAutoQueueSizing_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 5),
    _RingPortAutoQueueSizing_Type()
)
ringPortAutoQueueSizing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortAutoQueueSizing.setStatus("current")


class _RingPortRingMode_Type(Integer32):
    """Custom type ringPortRingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 2),
          ("working", 1))
    )


_RingPortRingMode_Type.__name__ = "Integer32"
_RingPortRingMode_Object = MibTableColumn
ringPortRingMode = _RingPortRingMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 6),
    _RingPortRingMode_Type()
)
ringPortRingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortRingMode.setStatus("current")


class _RingPortNodeId_Type(Integer32):
    """Custom type ringPortNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RingPortNodeId_Type.__name__ = "Integer32"
_RingPortNodeId_Object = MibTableColumn
ringPortNodeId = _RingPortNodeId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 7),
    _RingPortNodeId_Type()
)
ringPortNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortNodeId.setStatus("current")


class _RingPortAdminStatus_Type(Integer32):
    """Custom type ringPortAdminStatus based on Integer32"""
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
        *(("diagnostic", 4),
          ("down", 2),
          ("redundant", 3),
          ("up", 1))
    )


_RingPortAdminStatus_Type.__name__ = "Integer32"
_RingPortAdminStatus_Object = MibTableColumn
ringPortAdminStatus = _RingPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 8),
    _RingPortAdminStatus_Type()
)
ringPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortAdminStatus.setStatus("current")


class _RingPortOperStatus_Type(Integer32):
    """Custom type ringPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RingPortOperStatus_Type.__name__ = "Integer32"
_RingPortOperStatus_Object = MibTableColumn
ringPortOperStatus = _RingPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 9),
    _RingPortOperStatus_Type()
)
ringPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringPortOperStatus.setStatus("current")
_RingPortRxFrames_Type = Counter32
_RingPortRxFrames_Object = MibTableColumn
ringPortRxFrames = _RingPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 10),
    _RingPortRxFrames_Type()
)
ringPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringPortRxFrames.setStatus("current")
_RingPortRxFrameErrors_Type = Counter32
_RingPortRxFrameErrors_Object = MibTableColumn
ringPortRxFrameErrors = _RingPortRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 11),
    _RingPortRxFrameErrors_Type()
)
ringPortRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringPortRxFrameErrors.setStatus("current")
_RingPortTxFrames_Type = Counter32
_RingPortTxFrames_Object = MibTableColumn
ringPortTxFrames = _RingPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 12),
    _RingPortTxFrames_Type()
)
ringPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringPortTxFrames.setStatus("current")


class _RingPortMaxTDMChannels_Type(Integer32):
    """Custom type ringPortMaxTDMChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_RingPortMaxTDMChannels_Type.__name__ = "Integer32"
_RingPortMaxTDMChannels_Object = MibTableColumn
ringPortMaxTDMChannels = _RingPortMaxTDMChannels_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 13),
    _RingPortMaxTDMChannels_Type()
)
ringPortMaxTDMChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortMaxTDMChannels.setStatus("current")


class _RingPortK1K2Status_Type(Integer32):
    """Custom type ringPortK1K2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_RingPortK1K2Status_Type.__name__ = "Integer32"
_RingPortK1K2Status_Object = MibTableColumn
ringPortK1K2Status = _RingPortK1K2Status_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 14),
    _RingPortK1K2Status_Type()
)
ringPortK1K2Status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ringPortK1K2Status.setStatus("current")


class _RingPortAISStatus_Type(Integer32):
    """Custom type ringPortAISStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_RingPortAISStatus_Type.__name__ = "Integer32"
_RingPortAISStatus_Object = MibTableColumn
ringPortAISStatus = _RingPortAISStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 15),
    _RingPortAISStatus_Type()
)
ringPortAISStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ringPortAISStatus.setStatus("current")


class _RingPortPHYStatus_Type(Integer32):
    """Custom type ringPortPHYStatus based on Integer32"""
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
        *(("down", 2),
          ("lower-layer-down", 3),
          ("unknown", 4),
          ("up", 1))
    )


_RingPortPHYStatus_Type.__name__ = "Integer32"
_RingPortPHYStatus_Object = MibTableColumn
ringPortPHYStatus = _RingPortPHYStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 8, 1, 16),
    _RingPortPHYStatus_Type()
)
ringPortPHYStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ringPortPHYStatus.setStatus("current")
_TdmIoDS3PortTable_Object = MibTable
tdmIoDS3PortTable = _TdmIoDS3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9)
)
if mibBuilder.loadTexts:
    tdmIoDS3PortTable.setStatus("current")
_TdmIoDS3PortEntry_Object = MibTableRow
tdmIoDS3PortEntry = _TdmIoDS3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1)
)
tdmIoDS3PortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    tdmIoDS3PortEntry.setStatus("current")


class _TdmIoDS3PortPBitESS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortPBitESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortPBitESS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitESS15Min_Object = MibTableColumn
tdmIoDS3PortPBitESS15Min = _TdmIoDS3PortPBitESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 1),
    _TdmIoDS3PortPBitESS15Min_Type()
)
tdmIoDS3PortPBitESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitESS15Min.setStatus("current")


class _TdmIoDS3PortPBitESS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortPBitESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortPBitESS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitESS1Day_Object = MibTableColumn
tdmIoDS3PortPBitESS1Day = _TdmIoDS3PortPBitESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 2),
    _TdmIoDS3PortPBitESS1Day_Type()
)
tdmIoDS3PortPBitESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitESS1Day.setStatus("current")


class _TdmIoDS3PortPBitSESS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortPBitSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortPBitSESS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitSESS15Min_Object = MibTableColumn
tdmIoDS3PortPBitSESS15Min = _TdmIoDS3PortPBitSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 3),
    _TdmIoDS3PortPBitSESS15Min_Type()
)
tdmIoDS3PortPBitSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitSESS15Min.setStatus("current")


class _TdmIoDS3PortPBitSESS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortPBitSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortPBitSESS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitSESS1Day_Object = MibTableColumn
tdmIoDS3PortPBitSESS1Day = _TdmIoDS3PortPBitSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 4),
    _TdmIoDS3PortPBitSESS1Day_Type()
)
tdmIoDS3PortPBitSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitSESS1Day.setStatus("current")


class _TdmIoDS3PortSEFSS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortSEFSS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortSEFSS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortSEFSS15Min_Object = MibTableColumn
tdmIoDS3PortSEFSS15Min = _TdmIoDS3PortSEFSS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 5),
    _TdmIoDS3PortSEFSS15Min_Type()
)
tdmIoDS3PortSEFSS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortSEFSS15Min.setStatus("current")


class _TdmIoDS3PortSEFSS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortSEFSS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortSEFSS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortSEFSS1Day_Object = MibTableColumn
tdmIoDS3PortSEFSS1Day = _TdmIoDS3PortSEFSS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 6),
    _TdmIoDS3PortSEFSS1Day_Type()
)
tdmIoDS3PortSEFSS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortSEFSS1Day.setStatus("current")


class _TdmIoDS3PortUASS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortUASS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortUASS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortUASS15Min_Object = MibTableColumn
tdmIoDS3PortUASS15Min = _TdmIoDS3PortUASS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 7),
    _TdmIoDS3PortUASS15Min_Type()
)
tdmIoDS3PortUASS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortUASS15Min.setStatus("current")


class _TdmIoDS3PortUASS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortUASS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortUASS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortUASS1Day_Object = MibTableColumn
tdmIoDS3PortUASS1Day = _TdmIoDS3PortUASS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 8),
    _TdmIoDS3PortUASS1Day_Type()
)
tdmIoDS3PortUASS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortUASS1Day.setStatus("current")


class _TdmIoDS3PortLineCVS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortLineCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_TdmIoDS3PortLineCVS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortLineCVS15Min_Object = MibTableColumn
tdmIoDS3PortLineCVS15Min = _TdmIoDS3PortLineCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 9),
    _TdmIoDS3PortLineCVS15Min_Type()
)
tdmIoDS3PortLineCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortLineCVS15Min.setStatus("current")


class _TdmIoDS3PortLineCVS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortLineCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_TdmIoDS3PortLineCVS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortLineCVS1Day_Object = MibTableColumn
tdmIoDS3PortLineCVS1Day = _TdmIoDS3PortLineCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 10),
    _TdmIoDS3PortLineCVS1Day_Type()
)
tdmIoDS3PortLineCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortLineCVS1Day.setStatus("current")


class _TdmIoDS3PortPBitCVS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortPBitCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_TdmIoDS3PortPBitCVS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitCVS15Min_Object = MibTableColumn
tdmIoDS3PortPBitCVS15Min = _TdmIoDS3PortPBitCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 11),
    _TdmIoDS3PortPBitCVS15Min_Type()
)
tdmIoDS3PortPBitCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitCVS15Min.setStatus("current")


class _TdmIoDS3PortPBitCVS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortPBitCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_TdmIoDS3PortPBitCVS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortPBitCVS1Day_Object = MibTableColumn
tdmIoDS3PortPBitCVS1Day = _TdmIoDS3PortPBitCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 12),
    _TdmIoDS3PortPBitCVS1Day_Type()
)
tdmIoDS3PortPBitCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortPBitCVS1Day.setStatus("current")


class _TdmIoDS3PortLineESS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortLineESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortLineESS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortLineESS15Min_Object = MibTableColumn
tdmIoDS3PortLineESS15Min = _TdmIoDS3PortLineESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 13),
    _TdmIoDS3PortLineESS15Min_Type()
)
tdmIoDS3PortLineESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortLineESS15Min.setStatus("current")


class _TdmIoDS3PortLineESS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortLineESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortLineESS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortLineESS1Day_Object = MibTableColumn
tdmIoDS3PortLineESS1Day = _TdmIoDS3PortLineESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 14),
    _TdmIoDS3PortLineESS1Day_Type()
)
tdmIoDS3PortLineESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortLineESS1Day.setStatus("current")


class _TdmIoDS3PortCBitCVS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortCBitCVS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_TdmIoDS3PortCBitCVS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitCVS15Min_Object = MibTableColumn
tdmIoDS3PortCBitCVS15Min = _TdmIoDS3PortCBitCVS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 15),
    _TdmIoDS3PortCBitCVS15Min_Type()
)
tdmIoDS3PortCBitCVS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitCVS15Min.setStatus("current")


class _TdmIoDS3PortCBitCVS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortCBitCVS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_TdmIoDS3PortCBitCVS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitCVS1Day_Object = MibTableColumn
tdmIoDS3PortCBitCVS1Day = _TdmIoDS3PortCBitCVS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 16),
    _TdmIoDS3PortCBitCVS1Day_Type()
)
tdmIoDS3PortCBitCVS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitCVS1Day.setStatus("current")


class _TdmIoDS3PortCBitESS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortCBitESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortCBitESS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitESS15Min_Object = MibTableColumn
tdmIoDS3PortCBitESS15Min = _TdmIoDS3PortCBitESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 17),
    _TdmIoDS3PortCBitESS15Min_Type()
)
tdmIoDS3PortCBitESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitESS15Min.setStatus("current")


class _TdmIoDS3PortCBitESS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortCBitESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortCBitESS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitESS1Day_Object = MibTableColumn
tdmIoDS3PortCBitESS1Day = _TdmIoDS3PortCBitESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 18),
    _TdmIoDS3PortCBitESS1Day_Type()
)
tdmIoDS3PortCBitESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitESS1Day.setStatus("current")


class _TdmIoDS3PortCBitSESS15Min_Type(Integer32):
    """Custom type tdmIoDS3PortCBitSESS15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TdmIoDS3PortCBitSESS15Min_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitSESS15Min_Object = MibTableColumn
tdmIoDS3PortCBitSESS15Min = _TdmIoDS3PortCBitSESS15Min_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 19),
    _TdmIoDS3PortCBitSESS15Min_Type()
)
tdmIoDS3PortCBitSESS15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitSESS15Min.setStatus("current")


class _TdmIoDS3PortCBitSESS1Day_Type(Integer32):
    """Custom type tdmIoDS3PortCBitSESS1Day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TdmIoDS3PortCBitSESS1Day_Type.__name__ = "Integer32"
_TdmIoDS3PortCBitSESS1Day_Object = MibTableColumn
tdmIoDS3PortCBitSESS1Day = _TdmIoDS3PortCBitSESS1Day_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 20),
    _TdmIoDS3PortCBitSESS1Day_Type()
)
tdmIoDS3PortCBitSESS1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortCBitSESS1Day.setStatus("current")


class _TdmIoDS3PortRowStatus_Type(Integer32):
    """Custom type tdmIoDS3PortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2))
    )


_TdmIoDS3PortRowStatus_Type.__name__ = "Integer32"
_TdmIoDS3PortRowStatus_Object = MibTableColumn
tdmIoDS3PortRowStatus = _TdmIoDS3PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 9, 1, 21),
    _TdmIoDS3PortRowStatus_Type()
)
tdmIoDS3PortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoDS3PortRowStatus.setStatus("current")
_PosPortTable_Object = MibTable
posPortTable = _PosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10)
)
if mibBuilder.loadTexts:
    posPortTable.setStatus("current")
_PosPortEntry_Object = MibTableRow
posPortEntry = _PosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1)
)
posPortEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
    (0, "PORT-MIB", "portNo"),
)
if mibBuilder.loadTexts:
    posPortEntry.setStatus("current")
_PosPortTransportSegmentCount_Type = Counter32
_PosPortTransportSegmentCount_Object = MibTableColumn
posPortTransportSegmentCount = _PosPortTransportSegmentCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 1),
    _PosPortTransportSegmentCount_Type()
)
posPortTransportSegmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPortTransportSegmentCount.setStatus("current")


class _PosPortMode_Type(Integer32):
    """Custom type posPortMode based on Integer32"""
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
        *(("bridgedDataMode", 2),
          ("ipAddr", 5),
          ("macAddr", 4),
          ("mapOS", 7),
          ("mpls", 6),
          ("transparent", 1),
          ("vlan", 3))
    )


_PosPortMode_Type.__name__ = "Integer32"
_PosPortMode_Object = MibTableColumn
posPortMode = _PosPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 2),
    _PosPortMode_Type()
)
posPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPortMode.setStatus("current")
_PosPortDefaultVID_Type = Unsigned32
_PosPortDefaultVID_Object = MibTableColumn
posPortDefaultVID = _PosPortDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 3),
    _PosPortDefaultVID_Type()
)
posPortDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPortDefaultVID.setStatus("current")


class _PosPortMinPktSize_Type(Integer32):
    """Custom type posPortMinPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_PosPortMinPktSize_Type.__name__ = "Integer32"
_PosPortMinPktSize_Object = MibTableColumn
posPortMinPktSize = _PosPortMinPktSize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 4),
    _PosPortMinPktSize_Type()
)
posPortMinPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPortMinPktSize.setStatus("current")


class _PosPortMaxPktSize_Type(Integer32):
    """Custom type posPortMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_PosPortMaxPktSize_Type.__name__ = "Integer32"
_PosPortMaxPktSize_Object = MibTableColumn
posPortMaxPktSize = _PosPortMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 5),
    _PosPortMaxPktSize_Type()
)
posPortMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPortMaxPktSize.setStatus("current")
_PosPortMinPktViolations_Type = Counter32
_PosPortMinPktViolations_Object = MibTableColumn
posPortMinPktViolations = _PosPortMinPktViolations_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 6),
    _PosPortMinPktViolations_Type()
)
posPortMinPktViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPortMinPktViolations.setStatus("current")
_PosPortMaxPktViolations_Type = Counter32
_PosPortMaxPktViolations_Object = MibTableColumn
posPortMaxPktViolations = _PosPortMaxPktViolations_Object(
    (1, 3, 6, 1, 4, 1, 5812, 3, 10, 1, 7),
    _PosPortMaxPktViolations_Type()
)
posPortMaxPktViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPortMaxPktViolations.setStatus("current")

# Managed Objects groups


# Notification objects

portPhyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 0)
)
portPhyStatusChange.setObjects(
    ("IF-MIB", "ifOperStatus")
)
if mibBuilder.loadTexts:
    portPhyStatusChange.setStatus(
        ""
    )

portAdminStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 1)
)
portAdminStatusChange.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    portAdminStatusChange.setStatus(
        ""
    )

portSpeedStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 20)
)
portSpeedStatusTrap.setObjects(
    ("IF-MIB", "ifSpeed")
)
if mibBuilder.loadTexts:
    portSpeedStatusTrap.setStatus(
        ""
    )

etherPortDuplexStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 21)
)
etherPortDuplexStatusTrap.setObjects(
    ("EtherLike-MIB", "dot3StatsDuplexStatus")
)
if mibBuilder.loadTexts:
    etherPortDuplexStatusTrap.setStatus(
        ""
    )

etherPortAutonegStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 22)
)
etherPortAutonegStatusTrap.setObjects(
    ("MAU-MIB", "ifMauAutoNegConfig")
)
if mibBuilder.loadTexts:
    etherPortAutonegStatusTrap.setStatus(
        ""
    )

sonetSectionLOSChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 27)
)
sonetSectionLOSChange.setObjects(
    ("SONET-MIB", "sonetSectionCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetSectionLOSChange.setStatus(
        ""
    )

sonetSectionLOFChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 28)
)
sonetSectionLOFChange.setObjects(
    ("SONET-MIB", "sonetSectionCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetSectionLOFChange.setStatus(
        ""
    )

sonetLineAISChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 29)
)
sonetLineAISChange.setObjects(
    ("SONET-MIB", "sonetLineCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetLineAISChange.setStatus(
        ""
    )

sonetLineRDIChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 30)
)
sonetLineRDIChange.setObjects(
    ("SONET-MIB", "sonetLineCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetLineRDIChange.setStatus(
        ""
    )

sonetPathLOPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 31)
)
sonetPathLOPChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathLOPChange.setStatus(
        ""
    )

sonetPathAISChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 32)
)
sonetPathAISChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathAISChange.setStatus(
        ""
    )

sonetPathRDIChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 33)
)
sonetPathRDIChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathRDIChange.setStatus(
        ""
    )

sonetPathUNEQPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 34)
)
sonetPathUNEQPChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathUNEQPChange.setStatus(
        ""
    )

sonetPathPSLMChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 35)
)
sonetPathPSLMChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathPSLMChange.setStatus(
        ""
    )

sonetVTLOPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 36)
)
sonetVTLOPChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTLOPChange.setStatus(
        ""
    )

sonetVTAISChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 37)
)
sonetVTAISChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTAISChange.setStatus(
        ""
    )

sonetVTRDIChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 38)
)
sonetVTRDIChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTRDIChange.setStatus(
        ""
    )

sonetVTRFIChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 39)
)
sonetVTRFIChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTRFIChange.setStatus(
        ""
    )

sonetVTUNEQPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 40)
)
sonetVTUNEQPChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTUNEQPChange.setStatus(
        ""
    )

sonetVTPSLMChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 41)
)
sonetVTPSLMChange.setObjects(
    ("SONET-MIB", "sonetVTCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetVTPSLMChange.setStatus(
        ""
    )

ringPortK1K2Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 47)
)
ringPortK1K2Change.setObjects(
    ("PORT-MIB", "ringPortK1K2Status")
)
if mibBuilder.loadTexts:
    ringPortK1K2Change.setStatus(
        ""
    )

ringPortAISChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 48)
)
ringPortAISChange.setObjects(
    ("PORT-MIB", "ringPortAISStatus")
)
if mibBuilder.loadTexts:
    ringPortAISChange.setStatus(
        ""
    )

ringPortPHYChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 49)
)
ringPortPHYChange.setObjects(
    ("PORT-MIB", "ringPortPHYStatus")
)
if mibBuilder.loadTexts:
    ringPortPHYChange.setStatus(
        ""
    )

sonetPortTCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 50)
)
sonetPortTCAlarm.setObjects(
    ("PORT-MIB", "sonetTCAStatus")
)
if mibBuilder.loadTexts:
    sonetPortTCAlarm.setStatus(
        ""
    )

dsxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 55)
)
dsxAlarm.setObjects(
    ("PORT-MIB", "dsxStatus")
)
if mibBuilder.loadTexts:
    dsxAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PORT-MIB",
    **{"portPhyStatusChange": portPhyStatusChange,
       "portAdminStatusChange": portAdminStatusChange,
       "portSpeedStatusTrap": portSpeedStatusTrap,
       "etherPortDuplexStatusTrap": etherPortDuplexStatusTrap,
       "etherPortAutonegStatusTrap": etherPortAutonegStatusTrap,
       "sonetSectionLOSChange": sonetSectionLOSChange,
       "sonetSectionLOFChange": sonetSectionLOFChange,
       "sonetLineAISChange": sonetLineAISChange,
       "sonetLineRDIChange": sonetLineRDIChange,
       "sonetPathLOPChange": sonetPathLOPChange,
       "sonetPathAISChange": sonetPathAISChange,
       "sonetPathRDIChange": sonetPathRDIChange,
       "sonetPathUNEQPChange": sonetPathUNEQPChange,
       "sonetPathPSLMChange": sonetPathPSLMChange,
       "sonetVTLOPChange": sonetVTLOPChange,
       "sonetVTAISChange": sonetVTAISChange,
       "sonetVTRDIChange": sonetVTRDIChange,
       "sonetVTRFIChange": sonetVTRFIChange,
       "sonetVTUNEQPChange": sonetVTUNEQPChange,
       "sonetVTPSLMChange": sonetVTPSLMChange,
       "ringPortK1K2Change": ringPortK1K2Change,
       "ringPortAISChange": ringPortAISChange,
       "ringPortPHYChange": ringPortPHYChange,
       "sonetPortTCAlarm": sonetPortTCAlarm,
       "dsxAlarm": dsxAlarm,
       "portMIB": portMIB,
       "portTable": portTable,
       "portEntry": portEntry,
       "portNo": portNo,
       "mib2IfIndex": mib2IfIndex,
       "etherPortTable": etherPortTable,
       "etherPortEntry": etherPortEntry,
       "etherPortSpeedCfg": etherPortSpeedCfg,
       "etherPortSpeedStatus": etherPortSpeedStatus,
       "etherPortDuplexCfg": etherPortDuplexCfg,
       "etherPortLoopback": etherPortLoopback,
       "etherPortPhyReset": etherPortPhyReset,
       "etherPortStatsTxPkts64Octets": etherPortStatsTxPkts64Octets,
       "etherPortStatsTxPkts65to127Octets": etherPortStatsTxPkts65to127Octets,
       "etherPortStatsTxPkts128to255Octets": etherPortStatsTxPkts128to255Octets,
       "etherPortStatsTxPkts256to511Octets": etherPortStatsTxPkts256to511Octets,
       "etherPortStatsTxPkts512to1023Octets": etherPortStatsTxPkts512to1023Octets,
       "etherPortStatsTxPkts1024to1518Octets": etherPortStatsTxPkts1024to1518Octets,
       "etherPortStatsTxPkts1519to1530Octets": etherPortStatsTxPkts1519to1530Octets,
       "etherPortStatsTxFCSErrors": etherPortStatsTxFCSErrors,
       "etherPortStatsTxOversize": etherPortStatsTxOversize,
       "etherPortStatsTxUndersize": etherPortStatsTxUndersize,
       "etherPortStatsTxControlFrames": etherPortStatsTxControlFrames,
       "etherPortStatsTxBadFifoUnderrun": etherPortStatsTxBadFifoUnderrun,
       "etherPortStatsTxBadFifoOverrun": etherPortStatsTxBadFifoOverrun,
       "etherPortStatsTxDropFifoOverrun": etherPortStatsTxDropFifoOverrun,
       "etherPortStatsTxBadParityError": etherPortStatsTxBadParityError,
       "etherPortStatsTxDropParityError": etherPortStatsTxDropParityError,
       "etherPortStatsTxBadSequenceError": etherPortStatsTxBadSequenceError,
       "etherPortStatsTxDropSequenceError": etherPortStatsTxDropSequenceError,
       "etherPortStatsTxBadJamError": etherPortStatsTxBadJamError,
       "etherPortStatsTxDropJamError": etherPortStatsTxDropJamError,
       "etherPortSpeedTrapEnable": etherPortSpeedTrapEnable,
       "etherPortDuplexTrapEnable": etherPortDuplexTrapEnable,
       "etherPortAutonegTrapEnable": etherPortAutonegTrapEnable,
       "etherPortRowStatus": etherPortRowStatus,
       "etherPortAutonegAdvSpeed": etherPortAutonegAdvSpeed,
       "etherPortAutonegAdvDuplex": etherPortAutonegAdvDuplex,
       "etherPortPauseStateReceived": etherPortPauseStateReceived,
       "etherPortVlanMode": etherPortVlanMode,
       "etherPortDefaultVlanId": etherPortDefaultVlanId,
       "etherPortRxOverrun": etherPortRxOverrun,
       "etherPortRxSyncErrors": etherPortRxSyncErrors,
       "etherPortRxDelSeqErrors": etherPortRxDelSeqErrors,
       "etherPortRxFifoOverrunErrors": etherPortRxFifoOverrunErrors,
       "etherPortRxControlFrames": etherPortRxControlFrames,
       "etherPortRxThreshOvrszFrames": etherPortRxThreshOvrszFrames,
       "etherPortStatsRxPkts1519to1530Octets": etherPortStatsRxPkts1519to1530Octets,
       "tdmIoDS1PortTable": tdmIoDS1PortTable,
       "tdmIoDS1PortEntry": tdmIoDS1PortEntry,
       "tdmIoDS1PortType": tdmIoDS1PortType,
       "tdmIoDS1PortTiming": tdmIoDS1PortTiming,
       "tdmIoDS1PortBuildOut": tdmIoDS1PortBuildOut,
       "tdmIoDS1PortFraming": tdmIoDS1PortFraming,
       "tdmIoDS1PortCoding": tdmIoDS1PortCoding,
       "tdmIoDS1PortLoopbackState": tdmIoDS1PortLoopbackState,
       "tdmIoDS1PortLoopbackType": tdmIoDS1PortLoopbackType,
       "tdmIoDS1PortLoopbackResults": tdmIoDS1PortLoopbackResults,
       "tdmIoDS1PortLoopbackLLbActCode": tdmIoDS1PortLoopbackLLbActCode,
       "tdmIoDS1PortLoopbackLLbDeactCode": tdmIoDS1PortLoopbackLLbDeactCode,
       "tdmIoDS1PortLoopbackLlbActCodeLen": tdmIoDS1PortLoopbackLlbActCodeLen,
       "tdmIoDS1PortLoopbackLlbDeactCodeLen": tdmIoDS1PortLoopbackLlbDeactCodeLen,
       "tdmIoDS1PortLoopbackLlbControl": tdmIoDS1PortLoopbackLlbControl,
       "tdmIoDS1PortLoopbackLlbGenPath": tdmIoDS1PortLoopbackLlbGenPath,
       "tdmIoDS1PortLoopbackLlbMonPath": tdmIoDS1PortLoopbackLlbMonPath,
       "tdmIoDS1PortPrbsAlgorithm": tdmIoDS1PortPrbsAlgorithm,
       "tdmIoDS1PortPrbsInversion": tdmIoDS1PortPrbsInversion,
       "tdmIoDS1PortPrbsGenPath": tdmIoDS1PortPrbsGenPath,
       "tdmIoDS1PortPrbsMonPath": tdmIoDS1PortPrbsMonPath,
       "tdmIoDS1PortPrbsMonitor": tdmIoDS1PortPrbsMonitor,
       "tdmIoDS1PortPrbsTransmit": tdmIoDS1PortPrbsTransmit,
       "tdmIoDS1PortPrbsBec": tdmIoDS1PortPrbsBec,
       "tdmIoDS1PortBertState": tdmIoDS1PortBertState,
       "tdmIoDS1PortBertPattern": tdmIoDS1PortBertPattern,
       "tdmIoDS1PortBertDuration": tdmIoDS1PortBertDuration,
       "tdmIoDS1PortBertResults": tdmIoDS1PortBertResults,
       "tdmIoDS1PortLineESS15Min": tdmIoDS1PortLineESS15Min,
       "tdmIoDS1PortPathESS15Min": tdmIoDS1PortPathESS15Min,
       "tdmIoDS1PortLineESS1Day": tdmIoDS1PortLineESS1Day,
       "tdmIoDS1PortPathESS1Day": tdmIoDS1PortPathESS1Day,
       "tdmIoDS1PortPathCVS15Min": tdmIoDS1PortPathCVS15Min,
       "tdmIoDS1PortPathCVS1Day": tdmIoDS1PortPathCVS1Day,
       "tdmIoDS1PortPathSESS15Min": tdmIoDS1PortPathSESS15Min,
       "tdmIoDS1PortPathSESS1Day": tdmIoDS1PortPathSESS1Day,
       "tdmIoDS1PortPathSASS15Min": tdmIoDS1PortPathSASS15Min,
       "tdmIoDS1PortPathSASS1Day": tdmIoDS1PortPathSASS1Day,
       "tdmIoDS1PortPathCSS15Min": tdmIoDS1PortPathCSS15Min,
       "tdmIoDS1PortPathCSS1Day": tdmIoDS1PortPathCSS1Day,
       "tdmIoDS1PortPathUASS15Min": tdmIoDS1PortPathUASS15Min,
       "tdmIoDS1PortRowStatus": tdmIoDS1PortRowStatus,
       "dsxStatus": dsxStatus,
       "tdmIoDS1PortLCVCount": tdmIoDS1PortLCVCount,
       "sonetPortTable": sonetPortTable,
       "sonetPortEntry": sonetPortEntry,
       "sonetPortType": sonetPortType,
       "sonetPortIdString": sonetPortIdString,
       "sonetPortTiming": sonetPortTiming,
       "sonetPortLoopback": sonetPortLoopback,
       "sonetPortScrambling": sonetPortScrambling,
       "sonetPortChannelization": sonetPortChannelization,
       "sonetPortConfigedChans": sonetPortConfigedChans,
       "sonetPortSectESS15Min": sonetPortSectESS15Min,
       "sonetPortLineESS15Min": sonetPortLineESS15Min,
       "sonetPortPathESS15Min": sonetPortPathESS15Min,
       "sonetPortSectESS1Day": sonetPortSectESS1Day,
       "sonetPortLineESS1Day": sonetPortLineESS1Day,
       "sonetPortPathESS1Day": sonetPortPathESS1Day,
       "sonetPortSectCVS15Min": sonetPortSectCVS15Min,
       "sonetPortLineCVS15Min": sonetPortLineCVS15Min,
       "sonetPortPathCVS15Min": sonetPortPathCVS15Min,
       "sonetPortSectCVS1Day": sonetPortSectCVS1Day,
       "sonetPortLineCVS1Day": sonetPortLineCVS1Day,
       "sonetPortPathCVS1Day": sonetPortPathCVS1Day,
       "sonetPortSectSESS15Min": sonetPortSectSESS15Min,
       "sonetPortLineSESS15Min": sonetPortLineSESS15Min,
       "sonetPortPathSESS15Min": sonetPortPathSESS15Min,
       "sonetPortSectSESS1Day": sonetPortSectSESS1Day,
       "sonetPortLineSESS1Day": sonetPortLineSESS1Day,
       "sonetPortPathSESS1Day": sonetPortPathSESS1Day,
       "sonetPortLineUASS15Min": sonetPortLineUASS15Min,
       "sonetPortPathUASS15Min": sonetPortPathUASS15Min,
       "sonetPortLineUASS1Day": sonetPortLineUASS1Day,
       "sonetPortPathUASS1Day": sonetPortPathUASS1Day,
       "sonetPortRowStatus": sonetPortRowStatus,
       "sonetTCAStatus": sonetTCAStatus,
       "atmPortTable": atmPortTable,
       "atmPortEntry": atmPortEntry,
       "atmPortVPTunnel": atmPortVPTunnel,
       "atmPortMaxTotalBits": atmPortMaxTotalBits,
       "atmPortTiming": atmPortTiming,
       "atmPortInCells": atmPortInCells,
       "atmPortOutCells": atmPortOutCells,
       "atmPortCDVT": atmPortCDVT,
       "atmPortMaxActvBits": atmPortMaxActvBits,
       "atmPortHCInCells": atmPortHCInCells,
       "atmPortHCOutCells": atmPortHCOutCells,
       "atmPortRowStatus": atmPortRowStatus,
       "opticalPortTable": opticalPortTable,
       "opticalPortEntry": opticalPortEntry,
       "lambda": _pysmi_lambda,
       "opticalPortMode": opticalPortMode,
       "opticalPortRxSMselect": opticalPortRxSMselect,
       "opticalPortTxSMselect": opticalPortTxSMselect,
       "opticalPortRxSignalState": opticalPortRxSignalState,
       "opticalPortRxFrameState": opticalPortRxFrameState,
       "opticalPortTxStatus": opticalPortTxStatus,
       "opticalPortTxEnable": opticalPortTxEnable,
       "opticalPortLaserPowerLevel": opticalPortLaserPowerLevel,
       "opticalPortLaserWavelength": opticalPortLaserWavelength,
       "opticalPortRowStatus": opticalPortRowStatus,
       "ringPortTable": ringPortTable,
       "ringPortEntry": ringPortEntry,
       "ringPortArbiterEnabled": ringPortArbiterEnabled,
       "ringPortFrameMode": ringPortFrameMode,
       "ringPortMaxChannels": ringPortMaxChannels,
       "ringPortMaxSubChannels": ringPortMaxSubChannels,
       "ringPortAutoQueueSizing": ringPortAutoQueueSizing,
       "ringPortRingMode": ringPortRingMode,
       "ringPortNodeId": ringPortNodeId,
       "ringPortAdminStatus": ringPortAdminStatus,
       "ringPortOperStatus": ringPortOperStatus,
       "ringPortRxFrames": ringPortRxFrames,
       "ringPortRxFrameErrors": ringPortRxFrameErrors,
       "ringPortTxFrames": ringPortTxFrames,
       "ringPortMaxTDMChannels": ringPortMaxTDMChannels,
       "ringPortK1K2Status": ringPortK1K2Status,
       "ringPortAISStatus": ringPortAISStatus,
       "ringPortPHYStatus": ringPortPHYStatus,
       "tdmIoDS3PortTable": tdmIoDS3PortTable,
       "tdmIoDS3PortEntry": tdmIoDS3PortEntry,
       "tdmIoDS3PortPBitESS15Min": tdmIoDS3PortPBitESS15Min,
       "tdmIoDS3PortPBitESS1Day": tdmIoDS3PortPBitESS1Day,
       "tdmIoDS3PortPBitSESS15Min": tdmIoDS3PortPBitSESS15Min,
       "tdmIoDS3PortPBitSESS1Day": tdmIoDS3PortPBitSESS1Day,
       "tdmIoDS3PortSEFSS15Min": tdmIoDS3PortSEFSS15Min,
       "tdmIoDS3PortSEFSS1Day": tdmIoDS3PortSEFSS1Day,
       "tdmIoDS3PortUASS15Min": tdmIoDS3PortUASS15Min,
       "tdmIoDS3PortUASS1Day": tdmIoDS3PortUASS1Day,
       "tdmIoDS3PortLineCVS15Min": tdmIoDS3PortLineCVS15Min,
       "tdmIoDS3PortLineCVS1Day": tdmIoDS3PortLineCVS1Day,
       "tdmIoDS3PortPBitCVS15Min": tdmIoDS3PortPBitCVS15Min,
       "tdmIoDS3PortPBitCVS1Day": tdmIoDS3PortPBitCVS1Day,
       "tdmIoDS3PortLineESS15Min": tdmIoDS3PortLineESS15Min,
       "tdmIoDS3PortLineESS1Day": tdmIoDS3PortLineESS1Day,
       "tdmIoDS3PortCBitCVS15Min": tdmIoDS3PortCBitCVS15Min,
       "tdmIoDS3PortCBitCVS1Day": tdmIoDS3PortCBitCVS1Day,
       "tdmIoDS3PortCBitESS15Min": tdmIoDS3PortCBitESS15Min,
       "tdmIoDS3PortCBitESS1Day": tdmIoDS3PortCBitESS1Day,
       "tdmIoDS3PortCBitSESS15Min": tdmIoDS3PortCBitSESS15Min,
       "tdmIoDS3PortCBitSESS1Day": tdmIoDS3PortCBitSESS1Day,
       "tdmIoDS3PortRowStatus": tdmIoDS3PortRowStatus,
       "posPortTable": posPortTable,
       "posPortEntry": posPortEntry,
       "posPortTransportSegmentCount": posPortTransportSegmentCount,
       "posPortMode": posPortMode,
       "posPortDefaultVID": posPortDefaultVID,
       "posPortMinPktSize": posPortMinPktSize,
       "posPortMaxPktSize": posPortMaxPktSize,
       "posPortMinPktViolations": posPortMinPktViolations,
       "posPortMaxPktViolations": posPortMaxPktViolations}
)
