# SNMP MIB module (DIFF-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIFF-SERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:38 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(BurstSize,) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "BurstSize")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

diffServMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 12345)
)
diffServMib.setRevisions(
        ("2000-07-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class SixTupleClfrL4Port(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DiffServObjects_ObjectIdentity = ObjectIdentity
diffServObjects = _DiffServObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 1)
)
_DiffServClassifierNextFree_Type = Unsigned32
_DiffServClassifierNextFree_Object = MibScalar
diffServClassifierNextFree = _DiffServClassifierNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 1),
    _DiffServClassifierNextFree_Type()
)
diffServClassifierNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassifierNextFree.setStatus("current")
_DiffServSixTupleClfrNextFree_Type = Unsigned32
_DiffServSixTupleClfrNextFree_Object = MibScalar
diffServSixTupleClfrNextFree = _DiffServSixTupleClfrNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 2),
    _DiffServSixTupleClfrNextFree_Type()
)
diffServSixTupleClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServSixTupleClfrNextFree.setStatus("current")
_DiffServMeterNextFree_Type = Unsigned32
_DiffServMeterNextFree_Object = MibScalar
diffServMeterNextFree = _DiffServMeterNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 3),
    _DiffServMeterNextFree_Type()
)
diffServMeterNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServMeterNextFree.setStatus("current")
_DiffServActionNextFree_Type = Unsigned32
_DiffServActionNextFree_Object = MibScalar
diffServActionNextFree = _DiffServActionNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 4),
    _DiffServActionNextFree_Type()
)
diffServActionNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionNextFree.setStatus("current")
_DiffServAbsoluteDropAction_ObjectIdentity = ObjectIdentity
diffServAbsoluteDropAction = _DiffServAbsoluteDropAction_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 1, 6)
)
if mibBuilder.loadTexts:
    diffServAbsoluteDropAction.setStatus("current")
_DiffServAlgDropNextFree_Type = Unsigned32
_DiffServAlgDropNextFree_Object = MibScalar
diffServAlgDropNextFree = _DiffServAlgDropNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 7),
    _DiffServAlgDropNextFree_Type()
)
diffServAlgDropNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropNextFree.setStatus("current")
_DiffServQNextFree_Type = Unsigned32
_DiffServQNextFree_Object = MibScalar
diffServQNextFree = _DiffServQNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 8),
    _DiffServQNextFree_Type()
)
diffServQNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServQNextFree.setStatus("current")
_DiffServSchedulerNextFree_Type = Unsigned32
_DiffServSchedulerNextFree_Object = MibScalar
diffServSchedulerNextFree = _DiffServSchedulerNextFree_Object(
    (1, 3, 6, 1, 2, 1, 12345, 1, 9),
    _DiffServSchedulerNextFree_Type()
)
diffServSchedulerNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServSchedulerNextFree.setStatus("current")
_DiffServTables_ObjectIdentity = ObjectIdentity
diffServTables = _DiffServTables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 2)
)
_DiffServClassifierTable_Object = MibTable
diffServClassifierTable = _DiffServClassifierTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1)
)
if mibBuilder.loadTexts:
    diffServClassifierTable.setStatus("current")
_DiffServClassifierEntry_Object = MibTableRow
diffServClassifierEntry = _DiffServClassifierEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1)
)
diffServClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServClassifierIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServClassifierTcb"),
    (0, "DIFF-SERV-MIB", "diffServClassifierId"),
)
if mibBuilder.loadTexts:
    diffServClassifierEntry.setStatus("current")
_DiffServClassifierIfDirection_Type = IfDirection
_DiffServClassifierIfDirection_Object = MibTableColumn
diffServClassifierIfDirection = _DiffServClassifierIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 1),
    _DiffServClassifierIfDirection_Type()
)
diffServClassifierIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassifierIfDirection.setStatus("current")
_DiffServClassifierTcb_Type = Unsigned32
_DiffServClassifierTcb_Object = MibTableColumn
diffServClassifierTcb = _DiffServClassifierTcb_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 2),
    _DiffServClassifierTcb_Type()
)
diffServClassifierTcb.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassifierTcb.setStatus("current")
_DiffServClassifierId_Type = Unsigned32
_DiffServClassifierId_Object = MibTableColumn
diffServClassifierId = _DiffServClassifierId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 3),
    _DiffServClassifierId_Type()
)
diffServClassifierId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassifierId.setStatus("current")


class _DiffServClassifierFilter_Type(RowPointer):
    """Custom type diffServClassifierFilter based on RowPointer"""
    defaultValue = (0, 0)


_DiffServClassifierFilter_Object = MibTableColumn
diffServClassifierFilter = _DiffServClassifierFilter_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 4),
    _DiffServClassifierFilter_Type()
)
diffServClassifierFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierFilter.setStatus("current")
_DiffServClassifierNext_Type = RowPointer
_DiffServClassifierNext_Object = MibTableColumn
diffServClassifierNext = _DiffServClassifierNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 5),
    _DiffServClassifierNext_Type()
)
diffServClassifierNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierNext.setStatus("current")


class _DiffServClassifierPrecedence_Type(Unsigned32):
    """Custom type diffServClassifierPrecedence based on Unsigned32"""
    defaultValue = 0


_DiffServClassifierPrecedence_Object = MibTableColumn
diffServClassifierPrecedence = _DiffServClassifierPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 6),
    _DiffServClassifierPrecedence_Type()
)
diffServClassifierPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierPrecedence.setStatus("current")
_DiffServClassifierStatus_Type = RowStatus
_DiffServClassifierStatus_Object = MibTableColumn
diffServClassifierStatus = _DiffServClassifierStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 1, 1, 7),
    _DiffServClassifierStatus_Type()
)
diffServClassifierStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierStatus.setStatus("current")
_DiffServSixTupleClfrTable_Object = MibTable
diffServSixTupleClfrTable = _DiffServSixTupleClfrTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2)
)
if mibBuilder.loadTexts:
    diffServSixTupleClfrTable.setStatus("current")
_DiffServSixTupleClfrEntry_Object = MibTableRow
diffServSixTupleClfrEntry = _DiffServSixTupleClfrEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1)
)
diffServSixTupleClfrEntry.setIndexNames(
    (0, "DIFF-SERV-MIB", "diffServSixTupleClfrId"),
)
if mibBuilder.loadTexts:
    diffServSixTupleClfrEntry.setStatus("current")
_DiffServSixTupleClfrId_Type = Unsigned32
_DiffServSixTupleClfrId_Object = MibTableColumn
diffServSixTupleClfrId = _DiffServSixTupleClfrId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 1),
    _DiffServSixTupleClfrId_Type()
)
diffServSixTupleClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServSixTupleClfrId.setStatus("current")
_DiffServSixTupleClfrDstAddrType_Type = InetAddressType
_DiffServSixTupleClfrDstAddrType_Object = MibTableColumn
diffServSixTupleClfrDstAddrType = _DiffServSixTupleClfrDstAddrType_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 2),
    _DiffServSixTupleClfrDstAddrType_Type()
)
diffServSixTupleClfrDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstAddrType.setStatus("current")
_DiffServSixTupleClfrDstAddr_Type = InetAddress
_DiffServSixTupleClfrDstAddr_Object = MibTableColumn
diffServSixTupleClfrDstAddr = _DiffServSixTupleClfrDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 3),
    _DiffServSixTupleClfrDstAddr_Type()
)
diffServSixTupleClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstAddr.setStatus("current")


class _DiffServSixTupleClfrDstAddrMask_Type(Unsigned32):
    """Custom type diffServSixTupleClfrDstAddrMask based on Unsigned32"""
    defaultValue = 0


_DiffServSixTupleClfrDstAddrMask_Object = MibTableColumn
diffServSixTupleClfrDstAddrMask = _DiffServSixTupleClfrDstAddrMask_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 4),
    _DiffServSixTupleClfrDstAddrMask_Type()
)
diffServSixTupleClfrDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstAddrMask.setStatus("current")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstAddrMask.setUnits("bits")
_DiffServSixTupleClfrSrcAddrType_Type = InetAddressType
_DiffServSixTupleClfrSrcAddrType_Object = MibTableColumn
diffServSixTupleClfrSrcAddrType = _DiffServSixTupleClfrSrcAddrType_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 5),
    _DiffServSixTupleClfrSrcAddrType_Type()
)
diffServSixTupleClfrSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcAddrType.setStatus("current")
_DiffServSixTupleClfrSrcAddr_Type = InetAddress
_DiffServSixTupleClfrSrcAddr_Object = MibTableColumn
diffServSixTupleClfrSrcAddr = _DiffServSixTupleClfrSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 6),
    _DiffServSixTupleClfrSrcAddr_Type()
)
diffServSixTupleClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcAddr.setStatus("current")


class _DiffServSixTupleClfrSrcAddrMask_Type(Unsigned32):
    """Custom type diffServSixTupleClfrSrcAddrMask based on Unsigned32"""
    defaultValue = 0


_DiffServSixTupleClfrSrcAddrMask_Object = MibTableColumn
diffServSixTupleClfrSrcAddrMask = _DiffServSixTupleClfrSrcAddrMask_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 7),
    _DiffServSixTupleClfrSrcAddrMask_Type()
)
diffServSixTupleClfrSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcAddrMask.setStatus("current")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcAddrMask.setUnits("bits")


class _DiffServSixTupleClfrDscp_Type(Dscp):
    """Custom type diffServSixTupleClfrDscp based on Dscp"""
    defaultValue = -1


_DiffServSixTupleClfrDscp_Object = MibTableColumn
diffServSixTupleClfrDscp = _DiffServSixTupleClfrDscp_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 8),
    _DiffServSixTupleClfrDscp_Type()
)
diffServSixTupleClfrDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDscp.setStatus("current")


class _DiffServSixTupleClfrProtocol_Type(Integer32):
    """Custom type diffServSixTupleClfrProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffServSixTupleClfrProtocol_Type.__name__ = "Integer32"
_DiffServSixTupleClfrProtocol_Object = MibTableColumn
diffServSixTupleClfrProtocol = _DiffServSixTupleClfrProtocol_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 9),
    _DiffServSixTupleClfrProtocol_Type()
)
diffServSixTupleClfrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrProtocol.setStatus("current")


class _DiffServSixTupleClfrDstL4PortMin_Type(SixTupleClfrL4Port):
    """Custom type diffServSixTupleClfrDstL4PortMin based on SixTupleClfrL4Port"""
    defaultValue = 0


_DiffServSixTupleClfrDstL4PortMin_Object = MibTableColumn
diffServSixTupleClfrDstL4PortMin = _DiffServSixTupleClfrDstL4PortMin_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 10),
    _DiffServSixTupleClfrDstL4PortMin_Type()
)
diffServSixTupleClfrDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstL4PortMin.setStatus("current")


class _DiffServSixTupleClfrDstL4PortMax_Type(SixTupleClfrL4Port):
    """Custom type diffServSixTupleClfrDstL4PortMax based on SixTupleClfrL4Port"""
    defaultValue = 65535


_DiffServSixTupleClfrDstL4PortMax_Object = MibTableColumn
diffServSixTupleClfrDstL4PortMax = _DiffServSixTupleClfrDstL4PortMax_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 11),
    _DiffServSixTupleClfrDstL4PortMax_Type()
)
diffServSixTupleClfrDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrDstL4PortMax.setStatus("current")


class _DiffServSixTupleClfrSrcL4PortMin_Type(SixTupleClfrL4Port):
    """Custom type diffServSixTupleClfrSrcL4PortMin based on SixTupleClfrL4Port"""
    defaultValue = 0


_DiffServSixTupleClfrSrcL4PortMin_Object = MibTableColumn
diffServSixTupleClfrSrcL4PortMin = _DiffServSixTupleClfrSrcL4PortMin_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 12),
    _DiffServSixTupleClfrSrcL4PortMin_Type()
)
diffServSixTupleClfrSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcL4PortMin.setStatus("current")


class _DiffServSixTupleClfrSrcL4PortMax_Type(SixTupleClfrL4Port):
    """Custom type diffServSixTupleClfrSrcL4PortMax based on SixTupleClfrL4Port"""
    defaultValue = 65535


_DiffServSixTupleClfrSrcL4PortMax_Object = MibTableColumn
diffServSixTupleClfrSrcL4PortMax = _DiffServSixTupleClfrSrcL4PortMax_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 13),
    _DiffServSixTupleClfrSrcL4PortMax_Type()
)
diffServSixTupleClfrSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrSrcL4PortMax.setStatus("current")
_DiffServSixTupleClfrStatus_Type = RowStatus
_DiffServSixTupleClfrStatus_Object = MibTableColumn
diffServSixTupleClfrStatus = _DiffServSixTupleClfrStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 2, 1, 14),
    _DiffServSixTupleClfrStatus_Type()
)
diffServSixTupleClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSixTupleClfrStatus.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServMeterIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServMeterId"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterIfDirection_Type = IfDirection
_DiffServMeterIfDirection_Object = MibTableColumn
diffServMeterIfDirection = _DiffServMeterIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 1),
    _DiffServMeterIfDirection_Type()
)
diffServMeterIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterIfDirection.setStatus("current")
_DiffServMeterId_Type = Unsigned32
_DiffServMeterId_Object = MibTableColumn
diffServMeterId = _DiffServMeterId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 2),
    _DiffServMeterId_Type()
)
diffServMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterId.setStatus("current")


class _DiffServMeterSucceedNext_Type(RowPointer):
    """Custom type diffServMeterSucceedNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServMeterSucceedNext_Object = MibTableColumn
diffServMeterSucceedNext = _DiffServMeterSucceedNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 3),
    _DiffServMeterSucceedNext_Type()
)
diffServMeterSucceedNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterSucceedNext.setStatus("current")


class _DiffServMeterFailNext_Type(RowPointer):
    """Custom type diffServMeterFailNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServMeterFailNext_Object = MibTableColumn
diffServMeterFailNext = _DiffServMeterFailNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 4),
    _DiffServMeterFailNext_Type()
)
diffServMeterFailNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterFailNext.setStatus("current")
_DiffServMeterSpecific_Type = ObjectIdentifier
_DiffServMeterSpecific_Object = MibTableColumn
diffServMeterSpecific = _DiffServMeterSpecific_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 5),
    _DiffServMeterSpecific_Type()
)
diffServMeterSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterSpecific.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 3, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_DiffServTBMeterTable_Object = MibTable
diffServTBMeterTable = _DiffServTBMeterTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 4)
)
if mibBuilder.loadTexts:
    diffServTBMeterTable.setStatus("current")
_DiffServTBMeterEntry_Object = MibTableRow
diffServTBMeterEntry = _DiffServTBMeterEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 4, 1)
)
diffServTBMeterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServMeterIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServMeterId"),
)
if mibBuilder.loadTexts:
    diffServTBMeterEntry.setStatus("current")
_DiffServTBMeterRate_Type = Unsigned32
_DiffServTBMeterRate_Object = MibTableColumn
diffServTBMeterRate = _DiffServTBMeterRate_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 4, 1, 1),
    _DiffServTBMeterRate_Type()
)
diffServTBMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterRate.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBMeterRate.setUnits("kilobits per second")
_DiffServTBMeterBurstSize_Type = BurstSize
_DiffServTBMeterBurstSize_Object = MibTableColumn
diffServTBMeterBurstSize = _DiffServTBMeterBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 4, 1, 2),
    _DiffServTBMeterBurstSize_Type()
)
diffServTBMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBMeterBurstSize.setUnits("Bytes")
_DiffServTBMeterStatus_Type = RowStatus
_DiffServTBMeterStatus_Object = MibTableColumn
diffServTBMeterStatus = _DiffServTBMeterStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 4, 1, 3),
    _DiffServTBMeterStatus_Type()
)
diffServTBMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterStatus.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1)
)
diffServActionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServActionIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServActionId"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")
_DiffServActionIfDirection_Type = IfDirection
_DiffServActionIfDirection_Object = MibTableColumn
diffServActionIfDirection = _DiffServActionIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1, 1),
    _DiffServActionIfDirection_Type()
)
diffServActionIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionIfDirection.setStatus("current")
_DiffServActionId_Type = Unsigned32
_DiffServActionId_Object = MibTableColumn
diffServActionId = _DiffServActionId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1, 2),
    _DiffServActionId_Type()
)
diffServActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionId.setStatus("current")


class _DiffServActionNext_Type(RowPointer):
    """Custom type diffServActionNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServActionNext_Object = MibTableColumn
diffServActionNext = _DiffServActionNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1, 3),
    _DiffServActionNext_Type()
)
diffServActionNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionNext.setStatus("current")
_DiffServActionSpecific_Type = ObjectIdentifier
_DiffServActionSpecific_Object = MibTableColumn
diffServActionSpecific = _DiffServActionSpecific_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1, 4),
    _DiffServActionSpecific_Type()
)
diffServActionSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionSpecific.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 5, 1, 5),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServDscpMarkActTable_Object = MibTable
diffServDscpMarkActTable = _DiffServDscpMarkActTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 6)
)
if mibBuilder.loadTexts:
    diffServDscpMarkActTable.setStatus("current")
_DiffServDscpMarkActEntry_Object = MibTableRow
diffServDscpMarkActEntry = _DiffServDscpMarkActEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 6, 1)
)
diffServDscpMarkActEntry.setIndexNames(
    (0, "DIFF-SERV-MIB", "diffServDscpMarkActDscp"),
)
if mibBuilder.loadTexts:
    diffServDscpMarkActEntry.setStatus("current")
_DiffServDscpMarkActDscp_Type = Dscp
_DiffServDscpMarkActDscp_Object = MibTableColumn
diffServDscpMarkActDscp = _DiffServDscpMarkActDscp_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 6, 1, 1),
    _DiffServDscpMarkActDscp_Type()
)
diffServDscpMarkActDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServDscpMarkActDscp.setStatus("current")
_DiffServCountActTable_Object = MibTable
diffServCountActTable = _DiffServCountActTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7)
)
if mibBuilder.loadTexts:
    diffServCountActTable.setStatus("current")
_DiffServCountActEntry_Object = MibTableRow
diffServCountActEntry = _DiffServCountActEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1)
)
diffServCountActEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServActionIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServActionId"),
)
if mibBuilder.loadTexts:
    diffServCountActEntry.setStatus("current")
_DiffServCountActOctets_Type = Counter32
_DiffServCountActOctets_Object = MibTableColumn
diffServCountActOctets = _DiffServCountActOctets_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 1),
    _DiffServCountActOctets_Type()
)
diffServCountActOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActOctets.setStatus("current")
_DiffServCountActHCOctets_Type = Counter64
_DiffServCountActHCOctets_Object = MibTableColumn
diffServCountActHCOctets = _DiffServCountActHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 2),
    _DiffServCountActHCOctets_Type()
)
diffServCountActHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActHCOctets.setStatus("current")
_DiffServCountActPkts_Type = Counter32
_DiffServCountActPkts_Object = MibTableColumn
diffServCountActPkts = _DiffServCountActPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 3),
    _DiffServCountActPkts_Type()
)
diffServCountActPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActPkts.setStatus("current")
_DiffServCountActHCPkts_Type = Counter64
_DiffServCountActHCPkts_Object = MibTableColumn
diffServCountActHCPkts = _DiffServCountActHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 4),
    _DiffServCountActHCPkts_Type()
)
diffServCountActHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActHCPkts.setStatus("current")
_DiffServCountActDiscontTime_Type = TimeStamp
_DiffServCountActDiscontTime_Object = MibTableColumn
diffServCountActDiscontTime = _DiffServCountActDiscontTime_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 5),
    _DiffServCountActDiscontTime_Type()
)
diffServCountActDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServCountActDiscontTime.setStatus("current")
_DiffServCountActStatus_Type = RowStatus
_DiffServCountActStatus_Object = MibTableColumn
diffServCountActStatus = _DiffServCountActStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 7, 1, 6),
    _DiffServCountActStatus_Type()
)
diffServCountActStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServCountActStatus.setStatus("current")
_DiffServAlgDropTable_Object = MibTable
diffServAlgDropTable = _DiffServAlgDropTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8)
)
if mibBuilder.loadTexts:
    diffServAlgDropTable.setStatus("current")
_DiffServAlgDropEntry_Object = MibTableRow
diffServAlgDropEntry = _DiffServAlgDropEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1)
)
diffServAlgDropEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServAlgDropIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServAlgDropId"),
)
if mibBuilder.loadTexts:
    diffServAlgDropEntry.setStatus("current")
_DiffServAlgDropIfDirection_Type = IfDirection
_DiffServAlgDropIfDirection_Object = MibTableColumn
diffServAlgDropIfDirection = _DiffServAlgDropIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 1),
    _DiffServAlgDropIfDirection_Type()
)
diffServAlgDropIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAlgDropIfDirection.setStatus("current")
_DiffServAlgDropId_Type = Unsigned32
_DiffServAlgDropId_Object = MibTableColumn
diffServAlgDropId = _DiffServAlgDropId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 2),
    _DiffServAlgDropId_Type()
)
diffServAlgDropId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAlgDropId.setStatus("current")


class _DiffServAlgDropType_Type(Integer32):
    """Custom type diffServAlgDropType based on Integer32"""
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
        *(("headDrop", 3),
          ("other", 1),
          ("randomDrop", 4),
          ("tailDrop", 2))
    )


_DiffServAlgDropType_Type.__name__ = "Integer32"
_DiffServAlgDropType_Object = MibTableColumn
diffServAlgDropType = _DiffServAlgDropType_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 3),
    _DiffServAlgDropType_Type()
)
diffServAlgDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropType.setStatus("current")
_DiffServAlgDropNext_Type = RowPointer
_DiffServAlgDropNext_Object = MibTableColumn
diffServAlgDropNext = _DiffServAlgDropNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 4),
    _DiffServAlgDropNext_Type()
)
diffServAlgDropNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropNext.setStatus("current")
_DiffServAlgDropQMeasure_Type = RowPointer
_DiffServAlgDropQMeasure_Object = MibTableColumn
diffServAlgDropQMeasure = _DiffServAlgDropQMeasure_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 5),
    _DiffServAlgDropQMeasure_Type()
)
diffServAlgDropQMeasure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropQMeasure.setStatus("current")
_DiffServAlgDropQThreshold_Type = Unsigned32
_DiffServAlgDropQThreshold_Object = MibTableColumn
diffServAlgDropQThreshold = _DiffServAlgDropQThreshold_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 6),
    _DiffServAlgDropQThreshold_Type()
)
diffServAlgDropQThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropQThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diffServAlgDropQThreshold.setUnits("Bytes")
_DiffServAlgDropSpecific_Type = ObjectIdentifier
_DiffServAlgDropSpecific_Object = MibTableColumn
diffServAlgDropSpecific = _DiffServAlgDropSpecific_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 7),
    _DiffServAlgDropSpecific_Type()
)
diffServAlgDropSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropSpecific.setStatus("current")
_DiffServAlgDropOctets_Type = Counter32
_DiffServAlgDropOctets_Object = MibTableColumn
diffServAlgDropOctets = _DiffServAlgDropOctets_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 8),
    _DiffServAlgDropOctets_Type()
)
diffServAlgDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropOctets.setStatus("current")
_DiffServAlgDropHCOctets_Type = Counter64
_DiffServAlgDropHCOctets_Object = MibTableColumn
diffServAlgDropHCOctets = _DiffServAlgDropHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 9),
    _DiffServAlgDropHCOctets_Type()
)
diffServAlgDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropHCOctets.setStatus("current")
_DiffServAlgDropPkts_Type = Counter32
_DiffServAlgDropPkts_Object = MibTableColumn
diffServAlgDropPkts = _DiffServAlgDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 10),
    _DiffServAlgDropPkts_Type()
)
diffServAlgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropPkts.setStatus("current")
_DiffServAlgDropHCPkts_Type = Counter64
_DiffServAlgDropHCPkts_Object = MibTableColumn
diffServAlgDropHCPkts = _DiffServAlgDropHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 11),
    _DiffServAlgDropHCPkts_Type()
)
diffServAlgDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAlgDropHCPkts.setStatus("current")
_DiffServAlgDropStatus_Type = RowStatus
_DiffServAlgDropStatus_Object = MibTableColumn
diffServAlgDropStatus = _DiffServAlgDropStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 8, 1, 12),
    _DiffServAlgDropStatus_Type()
)
diffServAlgDropStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAlgDropStatus.setStatus("current")
_DiffServRandomDropTable_Object = MibTable
diffServRandomDropTable = _DiffServRandomDropTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9)
)
if mibBuilder.loadTexts:
    diffServRandomDropTable.setStatus("current")
_DiffServRandomDropEntry_Object = MibTableRow
diffServRandomDropEntry = _DiffServRandomDropEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1)
)
diffServRandomDropEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServAlgDropIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServAlgDropId"),
)
if mibBuilder.loadTexts:
    diffServRandomDropEntry.setStatus("current")
_DiffServRandomDropMinThreshBytes_Type = Unsigned32
_DiffServRandomDropMinThreshBytes_Object = MibTableColumn
diffServRandomDropMinThreshBytes = _DiffServRandomDropMinThreshBytes_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 1),
    _DiffServRandomDropMinThreshBytes_Type()
)
diffServRandomDropMinThreshBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshBytes.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshBytes.setUnits("bytes")
_DiffServRandomDropMinThreshPkts_Type = Unsigned32
_DiffServRandomDropMinThreshPkts_Object = MibTableColumn
diffServRandomDropMinThreshPkts = _DiffServRandomDropMinThreshPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 2),
    _DiffServRandomDropMinThreshPkts_Type()
)
diffServRandomDropMinThreshPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshPkts.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMinThreshPkts.setUnits("packets")
_DiffServRandomDropMaxThreshBytes_Type = Unsigned32
_DiffServRandomDropMaxThreshBytes_Object = MibTableColumn
diffServRandomDropMaxThreshBytes = _DiffServRandomDropMaxThreshBytes_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 3),
    _DiffServRandomDropMaxThreshBytes_Type()
)
diffServRandomDropMaxThreshBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshBytes.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshBytes.setUnits("bytes")
_DiffServRandomDropMaxThreshPkts_Type = Unsigned32
_DiffServRandomDropMaxThreshPkts_Object = MibTableColumn
diffServRandomDropMaxThreshPkts = _DiffServRandomDropMaxThreshPkts_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 4),
    _DiffServRandomDropMaxThreshPkts_Type()
)
diffServRandomDropMaxThreshPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshPkts.setStatus("current")
if mibBuilder.loadTexts:
    diffServRandomDropMaxThreshPkts.setUnits("packets")
_DiffServRandomDropInvWeight_Type = Unsigned32
_DiffServRandomDropInvWeight_Object = MibTableColumn
diffServRandomDropInvWeight = _DiffServRandomDropInvWeight_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 5),
    _DiffServRandomDropInvWeight_Type()
)
diffServRandomDropInvWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropInvWeight.setStatus("current")
_DiffServRandomDropProbMax_Type = Unsigned32
_DiffServRandomDropProbMax_Object = MibTableColumn
diffServRandomDropProbMax = _DiffServRandomDropProbMax_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 6),
    _DiffServRandomDropProbMax_Type()
)
diffServRandomDropProbMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropProbMax.setStatus("current")
_DiffServRandomDropStatus_Type = RowStatus
_DiffServRandomDropStatus_Object = MibTableColumn
diffServRandomDropStatus = _DiffServRandomDropStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 9, 1, 7),
    _DiffServRandomDropStatus_Type()
)
diffServRandomDropStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServRandomDropStatus.setStatus("current")
_DiffServQTable_Object = MibTable
diffServQTable = _DiffServQTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10)
)
if mibBuilder.loadTexts:
    diffServQTable.setStatus("current")
_DiffServQEntry_Object = MibTableRow
diffServQEntry = _DiffServQEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1)
)
diffServQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServQIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServQId"),
)
if mibBuilder.loadTexts:
    diffServQEntry.setStatus("current")
_DiffServQIfDirection_Type = IfDirection
_DiffServQIfDirection_Object = MibTableColumn
diffServQIfDirection = _DiffServQIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 1),
    _DiffServQIfDirection_Type()
)
diffServQIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServQIfDirection.setStatus("current")
_DiffServQId_Type = Unsigned32
_DiffServQId_Object = MibTableColumn
diffServQId = _DiffServQId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 2),
    _DiffServQId_Type()
)
diffServQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServQId.setStatus("current")
_DiffServQNext_Type = RowPointer
_DiffServQNext_Object = MibTableColumn
diffServQNext = _DiffServQNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 3),
    _DiffServQNext_Type()
)
diffServQNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQNext.setStatus("current")
_DiffServQPriority_Type = Unsigned32
_DiffServQPriority_Object = MibTableColumn
diffServQPriority = _DiffServQPriority_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 4),
    _DiffServQPriority_Type()
)
diffServQPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQPriority.setStatus("current")
_DiffServQMinRateAbs_Type = Unsigned32
_DiffServQMinRateAbs_Object = MibTableColumn
diffServQMinRateAbs = _DiffServQMinRateAbs_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 5),
    _DiffServQMinRateAbs_Type()
)
diffServQMinRateAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMinRateAbs.setStatus("current")
if mibBuilder.loadTexts:
    diffServQMinRateAbs.setUnits("kilobits per second")
_DiffServQMinRateRel_Type = Unsigned32
_DiffServQMinRateRel_Object = MibTableColumn
diffServQMinRateRel = _DiffServQMinRateRel_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 6),
    _DiffServQMinRateRel_Type()
)
diffServQMinRateRel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMinRateRel.setStatus("current")
_DiffServQMaxRateAbs_Type = Unsigned32
_DiffServQMaxRateAbs_Object = MibTableColumn
diffServQMaxRateAbs = _DiffServQMaxRateAbs_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 7),
    _DiffServQMaxRateAbs_Type()
)
diffServQMaxRateAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMaxRateAbs.setStatus("current")
if mibBuilder.loadTexts:
    diffServQMaxRateAbs.setUnits("kilobits per second")
_DiffServQMaxRateRel_Type = Unsigned32
_DiffServQMaxRateRel_Object = MibTableColumn
diffServQMaxRateRel = _DiffServQMaxRateRel_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 8),
    _DiffServQMaxRateRel_Type()
)
diffServQMaxRateRel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQMaxRateRel.setStatus("current")
_DiffServQStatus_Type = RowStatus
_DiffServQStatus_Object = MibTableColumn
diffServQStatus = _DiffServQStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 10, 1, 9),
    _DiffServQStatus_Type()
)
diffServQStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQStatus.setStatus("current")
_DiffServSchedulerTable_Object = MibTable
diffServSchedulerTable = _DiffServSchedulerTable_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11)
)
if mibBuilder.loadTexts:
    diffServSchedulerTable.setStatus("current")
_DiffServSchedulerEntry_Object = MibTableRow
diffServSchedulerEntry = _DiffServSchedulerEntry_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1)
)
diffServSchedulerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServSchedulerIfDirection"),
    (0, "DIFF-SERV-MIB", "diffServSchedulerId"),
)
if mibBuilder.loadTexts:
    diffServSchedulerEntry.setStatus("current")
_DiffServSchedulerIfDirection_Type = IfDirection
_DiffServSchedulerIfDirection_Object = MibTableColumn
diffServSchedulerIfDirection = _DiffServSchedulerIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1, 1),
    _DiffServSchedulerIfDirection_Type()
)
diffServSchedulerIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServSchedulerIfDirection.setStatus("current")
_DiffServSchedulerId_Type = Unsigned32
_DiffServSchedulerId_Object = MibTableColumn
diffServSchedulerId = _DiffServSchedulerId_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1, 2),
    _DiffServSchedulerId_Type()
)
diffServSchedulerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServSchedulerId.setStatus("current")


class _DiffServSchedulerMethod_Type(Integer32):
    """Custom type diffServSchedulerMethod based on Integer32"""
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
          ("priorityq", 2),
          ("wrr", 3))
    )


_DiffServSchedulerMethod_Type.__name__ = "Integer32"
_DiffServSchedulerMethod_Object = MibTableColumn
diffServSchedulerMethod = _DiffServSchedulerMethod_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1, 3),
    _DiffServSchedulerMethod_Type()
)
diffServSchedulerMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerMethod.setStatus("current")


class _DiffServSchedulerNext_Type(RowPointer):
    """Custom type diffServSchedulerNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServSchedulerNext_Object = MibTableColumn
diffServSchedulerNext = _DiffServSchedulerNext_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1, 4),
    _DiffServSchedulerNext_Type()
)
diffServSchedulerNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerNext.setStatus("current")
_DiffServSchedulerStatus_Type = RowStatus
_DiffServSchedulerStatus_Object = MibTableColumn
diffServSchedulerStatus = _DiffServSchedulerStatus_Object(
    (1, 3, 6, 1, 2, 1, 12345, 2, 11, 1, 5),
    _DiffServSchedulerStatus_Type()
)
diffServSchedulerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServSchedulerStatus.setStatus("current")
_DiffServMIBConformance_ObjectIdentity = ObjectIdentity
diffServMIBConformance = _DiffServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 3)
)
_DiffServMIBCompliances_ObjectIdentity = ObjectIdentity
diffServMIBCompliances = _DiffServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 3, 1)
)
_DiffServMIBGroups_ObjectIdentity = ObjectIdentity
diffServMIBGroups = _DiffServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2)
)

# Managed Objects groups

diffServMIBClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 1)
)
diffServMIBClassifierGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServClassifierFilter"),
        ("DIFF-SERV-MIB", "diffServClassifierNext"),
        ("DIFF-SERV-MIB", "diffServClassifierPrecedence"),
        ("DIFF-SERV-MIB", "diffServClassifierStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBClassifierGroup.setStatus("current")

diffServMIBSixTupleClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 2)
)
diffServMIBSixTupleClfrGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServSixTupleClfrDstAddrType"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDstAddr"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDstAddrMask"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDstAddrType"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrSrcAddrType"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrSrcAddrMask"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDscp"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrProtocol"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDstL4PortMin"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrDstL4PortMax"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrSrcL4PortMin"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrSrcL4PortMax"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBSixTupleClfrGroup.setStatus("current")

diffServMIBMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 3)
)
diffServMIBMeterGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServMeterSucceedNext"),
        ("DIFF-SERV-MIB", "diffServMeterFailNext"),
        ("DIFF-SERV-MIB", "diffServMeterSpecific"),
        ("DIFF-SERV-MIB", "diffServMeterStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBMeterGroup.setStatus("current")

diffServMIBTokenBucketMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 4)
)
diffServMIBTokenBucketMeterGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServTBMeterRate"),
        ("DIFF-SERV-MIB", "diffServTBMeterBurstSize"),
        ("DIFF-SERV-MIB", "diffServTBMeterStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBTokenBucketMeterGroup.setStatus("current")

diffServMIBActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 5)
)
diffServMIBActionGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServActionNext"),
        ("DIFF-SERV-MIB", "diffServActionSpecific"),
        ("DIFF-SERV-MIB", "diffServActionStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBActionGroup.setStatus("current")

diffServMIBDscpMarkActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 6)
)
diffServMIBDscpMarkActionGroup.setObjects(
    ("DIFF-SERV-MIB", "diffServDscpMarkActDscp")
)
if mibBuilder.loadTexts:
    diffServMIBDscpMarkActionGroup.setStatus("current")

diffServMIBCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 7)
)
diffServMIBCounterGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServCountActOctets"),
        ("DIFF-SERV-MIB", "diffServCountActPkts"),
        ("DIFF-SERV-MIB", "diffServCountActStatus"),
        ("DIFF-SERV-MIB", "diffServAlgDropOctets"),
        ("DIFF-SERV-MIB", "diffServAlgDropPkts"))
)
if mibBuilder.loadTexts:
    diffServMIBCounterGroup.setStatus("current")

diffServMIBHCCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 8)
)
diffServMIBHCCounterGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServCountActOctets"),
        ("DIFF-SERV-MIB", "diffServCountActHCOctets"),
        ("DIFF-SERV-MIB", "diffServCountActPkts"),
        ("DIFF-SERV-MIB", "diffServCountActStatus"),
        ("DIFF-SERV-MIB", "diffServAlgDropOctets"),
        ("DIFF-SERV-MIB", "diffServAlgDropHCOctets"),
        ("DIFF-SERV-MIB", "diffServAlgDropPkts"))
)
if mibBuilder.loadTexts:
    diffServMIBHCCounterGroup.setStatus("current")

diffServMIBVHCCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 9)
)
diffServMIBVHCCounterGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServCountActOctets"),
        ("DIFF-SERV-MIB", "diffServCountActHCOctets"),
        ("DIFF-SERV-MIB", "diffServCountActPkts"),
        ("DIFF-SERV-MIB", "diffServCountActHCPkts"),
        ("DIFF-SERV-MIB", "diffServCountActStatus"),
        ("DIFF-SERV-MIB", "diffServAlgDropOctets"),
        ("DIFF-SERV-MIB", "diffServAlgDropHCOctets"),
        ("DIFF-SERV-MIB", "diffServAlgDropPkts"),
        ("DIFF-SERV-MIB", "diffServAlgDropHCPkts"))
)
if mibBuilder.loadTexts:
    diffServMIBVHCCounterGroup.setStatus("current")

diffServMIBAlgDropGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 10)
)
diffServMIBAlgDropGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServAlgDropType"),
        ("DIFF-SERV-MIB", "diffServAlgDropNext"),
        ("DIFF-SERV-MIB", "diffServAlgDropQMeasure"),
        ("DIFF-SERV-MIB", "diffServAlgDropQThreshold"),
        ("DIFF-SERV-MIB", "diffServAlgDropSpecific"),
        ("DIFF-SERV-MIB", "diffServAlgDropStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBAlgDropGroup.setStatus("current")

diffServMIBRandomDropGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 11)
)
diffServMIBRandomDropGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServRandomDropMinThreshBytes"),
        ("DIFF-SERV-MIB", "diffServRandomDropMinThreshPkts"),
        ("DIFF-SERV-MIB", "diffServRandomDropMaxThreshBytes"),
        ("DIFF-SERV-MIB", "diffServRandomDropMaxThreshPkts"),
        ("DIFF-SERV-MIB", "diffServRandomDropInvWeight"),
        ("DIFF-SERV-MIB", "diffServRandomDropProbMax"),
        ("DIFF-SERV-MIB", "diffServRandomDropStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBRandomDropGroup.setStatus("current")

diffServMIBQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 12)
)
diffServMIBQueueGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServQPriority"),
        ("DIFF-SERV-MIB", "diffServQNext"),
        ("DIFF-SERV-MIB", "diffServQMinRateAbs"),
        ("DIFF-SERV-MIB", "diffServQMinRateRel"),
        ("DIFF-SERV-MIB", "diffServQMaxRateAbs"),
        ("DIFF-SERV-MIB", "diffServQMaxRateRel"),
        ("DIFF-SERV-MIB", "diffServQStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBQueueGroup.setStatus("current")

diffServMIBSchedulerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 13)
)
diffServMIBSchedulerGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServSchedulerMethod"),
        ("DIFF-SERV-MIB", "diffServSchedulerNext"),
        ("DIFF-SERV-MIB", "diffServSchedulerStatus"))
)
if mibBuilder.loadTexts:
    diffServMIBSchedulerGroup.setStatus("current")

diffServMIBStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12345, 3, 2, 14)
)
diffServMIBStaticGroup.setObjects(
      *(("DIFF-SERV-MIB", "diffServClassifierNextFree"),
        ("DIFF-SERV-MIB", "diffServSixTupleClfrNextFree"),
        ("DIFF-SERV-MIB", "diffServMeterNextFree"),
        ("DIFF-SERV-MIB", "diffServActionNextFree"),
        ("DIFF-SERV-MIB", "diffServAlgDropNextFree"),
        ("DIFF-SERV-MIB", "diffServQNextFree"),
        ("DIFF-SERV-MIB", "diffServSchedulerNextFree"))
)
if mibBuilder.loadTexts:
    diffServMIBStaticGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diffServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 12345, 3, 1, 1)
)
if mibBuilder.loadTexts:
    diffServMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIFF-SERV-MIB",
    **{"Dscp": Dscp,
       "SixTupleClfrL4Port": SixTupleClfrL4Port,
       "IfDirection": IfDirection,
       "diffServMib": diffServMib,
       "diffServObjects": diffServObjects,
       "diffServClassifierNextFree": diffServClassifierNextFree,
       "diffServSixTupleClfrNextFree": diffServSixTupleClfrNextFree,
       "diffServMeterNextFree": diffServMeterNextFree,
       "diffServActionNextFree": diffServActionNextFree,
       "diffServAbsoluteDropAction": diffServAbsoluteDropAction,
       "diffServAlgDropNextFree": diffServAlgDropNextFree,
       "diffServQNextFree": diffServQNextFree,
       "diffServSchedulerNextFree": diffServSchedulerNextFree,
       "diffServTables": diffServTables,
       "diffServClassifierTable": diffServClassifierTable,
       "diffServClassifierEntry": diffServClassifierEntry,
       "diffServClassifierIfDirection": diffServClassifierIfDirection,
       "diffServClassifierTcb": diffServClassifierTcb,
       "diffServClassifierId": diffServClassifierId,
       "diffServClassifierFilter": diffServClassifierFilter,
       "diffServClassifierNext": diffServClassifierNext,
       "diffServClassifierPrecedence": diffServClassifierPrecedence,
       "diffServClassifierStatus": diffServClassifierStatus,
       "diffServSixTupleClfrTable": diffServSixTupleClfrTable,
       "diffServSixTupleClfrEntry": diffServSixTupleClfrEntry,
       "diffServSixTupleClfrId": diffServSixTupleClfrId,
       "diffServSixTupleClfrDstAddrType": diffServSixTupleClfrDstAddrType,
       "diffServSixTupleClfrDstAddr": diffServSixTupleClfrDstAddr,
       "diffServSixTupleClfrDstAddrMask": diffServSixTupleClfrDstAddrMask,
       "diffServSixTupleClfrSrcAddrType": diffServSixTupleClfrSrcAddrType,
       "diffServSixTupleClfrSrcAddr": diffServSixTupleClfrSrcAddr,
       "diffServSixTupleClfrSrcAddrMask": diffServSixTupleClfrSrcAddrMask,
       "diffServSixTupleClfrDscp": diffServSixTupleClfrDscp,
       "diffServSixTupleClfrProtocol": diffServSixTupleClfrProtocol,
       "diffServSixTupleClfrDstL4PortMin": diffServSixTupleClfrDstL4PortMin,
       "diffServSixTupleClfrDstL4PortMax": diffServSixTupleClfrDstL4PortMax,
       "diffServSixTupleClfrSrcL4PortMin": diffServSixTupleClfrSrcL4PortMin,
       "diffServSixTupleClfrSrcL4PortMax": diffServSixTupleClfrSrcL4PortMax,
       "diffServSixTupleClfrStatus": diffServSixTupleClfrStatus,
       "diffServMeterTable": diffServMeterTable,
       "diffServMeterEntry": diffServMeterEntry,
       "diffServMeterIfDirection": diffServMeterIfDirection,
       "diffServMeterId": diffServMeterId,
       "diffServMeterSucceedNext": diffServMeterSucceedNext,
       "diffServMeterFailNext": diffServMeterFailNext,
       "diffServMeterSpecific": diffServMeterSpecific,
       "diffServMeterStatus": diffServMeterStatus,
       "diffServTBMeterTable": diffServTBMeterTable,
       "diffServTBMeterEntry": diffServTBMeterEntry,
       "diffServTBMeterRate": diffServTBMeterRate,
       "diffServTBMeterBurstSize": diffServTBMeterBurstSize,
       "diffServTBMeterStatus": diffServTBMeterStatus,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionIfDirection": diffServActionIfDirection,
       "diffServActionId": diffServActionId,
       "diffServActionNext": diffServActionNext,
       "diffServActionSpecific": diffServActionSpecific,
       "diffServActionStatus": diffServActionStatus,
       "diffServDscpMarkActTable": diffServDscpMarkActTable,
       "diffServDscpMarkActEntry": diffServDscpMarkActEntry,
       "diffServDscpMarkActDscp": diffServDscpMarkActDscp,
       "diffServCountActTable": diffServCountActTable,
       "diffServCountActEntry": diffServCountActEntry,
       "diffServCountActOctets": diffServCountActOctets,
       "diffServCountActHCOctets": diffServCountActHCOctets,
       "diffServCountActPkts": diffServCountActPkts,
       "diffServCountActHCPkts": diffServCountActHCPkts,
       "diffServCountActDiscontTime": diffServCountActDiscontTime,
       "diffServCountActStatus": diffServCountActStatus,
       "diffServAlgDropTable": diffServAlgDropTable,
       "diffServAlgDropEntry": diffServAlgDropEntry,
       "diffServAlgDropIfDirection": diffServAlgDropIfDirection,
       "diffServAlgDropId": diffServAlgDropId,
       "diffServAlgDropType": diffServAlgDropType,
       "diffServAlgDropNext": diffServAlgDropNext,
       "diffServAlgDropQMeasure": diffServAlgDropQMeasure,
       "diffServAlgDropQThreshold": diffServAlgDropQThreshold,
       "diffServAlgDropSpecific": diffServAlgDropSpecific,
       "diffServAlgDropOctets": diffServAlgDropOctets,
       "diffServAlgDropHCOctets": diffServAlgDropHCOctets,
       "diffServAlgDropPkts": diffServAlgDropPkts,
       "diffServAlgDropHCPkts": diffServAlgDropHCPkts,
       "diffServAlgDropStatus": diffServAlgDropStatus,
       "diffServRandomDropTable": diffServRandomDropTable,
       "diffServRandomDropEntry": diffServRandomDropEntry,
       "diffServRandomDropMinThreshBytes": diffServRandomDropMinThreshBytes,
       "diffServRandomDropMinThreshPkts": diffServRandomDropMinThreshPkts,
       "diffServRandomDropMaxThreshBytes": diffServRandomDropMaxThreshBytes,
       "diffServRandomDropMaxThreshPkts": diffServRandomDropMaxThreshPkts,
       "diffServRandomDropInvWeight": diffServRandomDropInvWeight,
       "diffServRandomDropProbMax": diffServRandomDropProbMax,
       "diffServRandomDropStatus": diffServRandomDropStatus,
       "diffServQTable": diffServQTable,
       "diffServQEntry": diffServQEntry,
       "diffServQIfDirection": diffServQIfDirection,
       "diffServQId": diffServQId,
       "diffServQNext": diffServQNext,
       "diffServQPriority": diffServQPriority,
       "diffServQMinRateAbs": diffServQMinRateAbs,
       "diffServQMinRateRel": diffServQMinRateRel,
       "diffServQMaxRateAbs": diffServQMaxRateAbs,
       "diffServQMaxRateRel": diffServQMaxRateRel,
       "diffServQStatus": diffServQStatus,
       "diffServSchedulerTable": diffServSchedulerTable,
       "diffServSchedulerEntry": diffServSchedulerEntry,
       "diffServSchedulerIfDirection": diffServSchedulerIfDirection,
       "diffServSchedulerId": diffServSchedulerId,
       "diffServSchedulerMethod": diffServSchedulerMethod,
       "diffServSchedulerNext": diffServSchedulerNext,
       "diffServSchedulerStatus": diffServSchedulerStatus,
       "diffServMIBConformance": diffServMIBConformance,
       "diffServMIBCompliances": diffServMIBCompliances,
       "diffServMIBCompliance": diffServMIBCompliance,
       "diffServMIBGroups": diffServMIBGroups,
       "diffServMIBClassifierGroup": diffServMIBClassifierGroup,
       "diffServMIBSixTupleClfrGroup": diffServMIBSixTupleClfrGroup,
       "diffServMIBMeterGroup": diffServMIBMeterGroup,
       "diffServMIBTokenBucketMeterGroup": diffServMIBTokenBucketMeterGroup,
       "diffServMIBActionGroup": diffServMIBActionGroup,
       "diffServMIBDscpMarkActionGroup": diffServMIBDscpMarkActionGroup,
       "diffServMIBCounterGroup": diffServMIBCounterGroup,
       "diffServMIBHCCounterGroup": diffServMIBHCCounterGroup,
       "diffServMIBVHCCounterGroup": diffServMIBVHCCounterGroup,
       "diffServMIBAlgDropGroup": diffServMIBAlgDropGroup,
       "diffServMIBRandomDropGroup": diffServMIBRandomDropGroup,
       "diffServMIBQueueGroup": diffServMIBQueueGroup,
       "diffServMIBSchedulerGroup": diffServMIBSchedulerGroup,
       "diffServMIBStaticGroup": diffServMIBStaticGroup}
)
