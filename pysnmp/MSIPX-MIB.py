# SNMP MIB module (MSIPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSIPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:59 2024
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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
    "NotificationType",
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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8)
)
_IpxBase_ObjectIdentity = ObjectIdentity
ipxBase = _IpxBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1)
)


class _IpxBaseOperState_Type(Integer32):
    """Custom type ipxBaseOperState based on Integer32"""
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


_IpxBaseOperState_Type.__name__ = "Integer32"
_IpxBaseOperState_Object = MibScalar
ipxBaseOperState = _IpxBaseOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 1),
    _IpxBaseOperState_Type()
)
ipxBaseOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseOperState.setStatus("mandatory")
_IpxBasePrimaryNetNumber_Type = NetNumber
_IpxBasePrimaryNetNumber_Object = MibScalar
ipxBasePrimaryNetNumber = _IpxBasePrimaryNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 2),
    _IpxBasePrimaryNetNumber_Type()
)
ipxBasePrimaryNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasePrimaryNetNumber.setStatus("mandatory")
_IpxBaseNode_Type = PhysAddress
_IpxBaseNode_Object = MibScalar
ipxBaseNode = _IpxBaseNode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 3),
    _IpxBaseNode_Type()
)
ipxBaseNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseNode.setStatus("mandatory")


class _IpxBaseSysName_Type(OctetString):
    """Custom type ipxBaseSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxBaseSysName_Type.__name__ = "OctetString"
_IpxBaseSysName_Object = MibScalar
ipxBaseSysName = _IpxBaseSysName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 4),
    _IpxBaseSysName_Type()
)
ipxBaseSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseSysName.setStatus("mandatory")


class _IpxBaseMaxPathSplits_Type(Integer32):
    """Custom type ipxBaseMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpxBaseMaxPathSplits_Type.__name__ = "Integer32"
_IpxBaseMaxPathSplits_Object = MibScalar
ipxBaseMaxPathSplits = _IpxBaseMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 5),
    _IpxBaseMaxPathSplits_Type()
)
ipxBaseMaxPathSplits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseMaxPathSplits.setStatus("mandatory")
_IpxBaseIfCount_Type = Integer32
_IpxBaseIfCount_Object = MibScalar
ipxBaseIfCount = _IpxBaseIfCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 6),
    _IpxBaseIfCount_Type()
)
ipxBaseIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseIfCount.setStatus("mandatory")
_IpxBaseDestCount_Type = Integer32
_IpxBaseDestCount_Object = MibScalar
ipxBaseDestCount = _IpxBaseDestCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 7),
    _IpxBaseDestCount_Type()
)
ipxBaseDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseDestCount.setStatus("mandatory")
_IpxBaseServCount_Type = Integer32
_IpxBaseServCount_Object = MibScalar
ipxBaseServCount = _IpxBaseServCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 8),
    _IpxBaseServCount_Type()
)
ipxBaseServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBaseServCount.setStatus("mandatory")
_IpxInterface_ObjectIdentity = ObjectIdentity
ipxInterface = _IpxInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2)
)
_IpxIfTable_Object = MibTable
ipxIfTable = _IpxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    ipxIfTable.setStatus("mandatory")
_IpxIfEntry_Object = MibTableRow
ipxIfEntry = _IpxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1)
)
ipxIfEntry.setIndexNames(
    (0, "MSIPX-MIB", "ipxIfIndex"),
)
if mibBuilder.loadTexts:
    ipxIfEntry.setStatus("mandatory")
_IpxIfIndex_Type = Integer32
_IpxIfIndex_Object = MibTableColumn
ipxIfIndex = _IpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 1),
    _IpxIfIndex_Type()
)
ipxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfIndex.setStatus("mandatory")


class _IpxIfAdminState_Type(Integer32):
    """Custom type ipxIfAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfAdminState_Type.__name__ = "Integer32"
_IpxIfAdminState_Object = MibTableColumn
ipxIfAdminState = _IpxIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 2),
    _IpxIfAdminState_Type()
)
ipxIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfAdminState.setStatus("mandatory")


class _IpxIfOperState_Type(Integer32):
    """Custom type ipxIfOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("sleeping", 3),
          ("up", 2))
    )


_IpxIfOperState_Type.__name__ = "Integer32"
_IpxIfOperState_Object = MibTableColumn
ipxIfOperState = _IpxIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 3),
    _IpxIfOperState_Type()
)
ipxIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfOperState.setStatus("mandatory")
_IpxIfAdapterIndex_Type = Integer32
_IpxIfAdapterIndex_Object = MibTableColumn
ipxIfAdapterIndex = _IpxIfAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 4),
    _IpxIfAdapterIndex_Type()
)
ipxIfAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfAdapterIndex.setStatus("mandatory")


class _IpxIfName_Type(OctetString):
    """Custom type ipxIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxIfName_Type.__name__ = "OctetString"
_IpxIfName_Object = MibTableColumn
ipxIfName = _IpxIfName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 5),
    _IpxIfName_Type()
)
ipxIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfName.setStatus("mandatory")


class _IpxIfType_Type(Integer32):
    """Custom type ipxIfType based on Integer32"""
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
        *(("internal", 5),
          ("lan", 2),
          ("other", 1),
          ("personalWanRouter", 6),
          ("routerWorkstationDialout", 7),
          ("standaloneWorkstationDialout", 8),
          ("wanRouter", 3),
          ("wanWorkstation", 4))
    )


_IpxIfType_Type.__name__ = "Integer32"
_IpxIfType_Object = MibTableColumn
ipxIfType = _IpxIfType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 6),
    _IpxIfType_Type()
)
ipxIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfType.setStatus("mandatory")
_IpxIfLocalMaxPacketSize_Type = Integer32
_IpxIfLocalMaxPacketSize_Object = MibTableColumn
ipxIfLocalMaxPacketSize = _IpxIfLocalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 7),
    _IpxIfLocalMaxPacketSize_Type()
)
ipxIfLocalMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfLocalMaxPacketSize.setStatus("mandatory")
_IpxIfMediaType_Type = Integer32
_IpxIfMediaType_Object = MibTableColumn
ipxIfMediaType = _IpxIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 8),
    _IpxIfMediaType_Type()
)
ipxIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfMediaType.setStatus("mandatory")
_IpxIfNetNumber_Type = NetNumber
_IpxIfNetNumber_Object = MibTableColumn
ipxIfNetNumber = _IpxIfNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 9),
    _IpxIfNetNumber_Type()
)
ipxIfNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfNetNumber.setStatus("mandatory")
_IpxIfMacAddress_Type = PhysAddress
_IpxIfMacAddress_Object = MibTableColumn
ipxIfMacAddress = _IpxIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 10),
    _IpxIfMacAddress_Type()
)
ipxIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfMacAddress.setStatus("mandatory")
_IpxIfDelay_Type = Integer32
_IpxIfDelay_Object = MibTableColumn
ipxIfDelay = _IpxIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 11),
    _IpxIfDelay_Type()
)
ipxIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfDelay.setStatus("mandatory")
_IpxIfThroughput_Type = Integer32
_IpxIfThroughput_Object = MibTableColumn
ipxIfThroughput = _IpxIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 12),
    _IpxIfThroughput_Type()
)
ipxIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfThroughput.setStatus("mandatory")


class _IpxIfIpxWanEnable_Type(Integer32):
    """Custom type ipxIfIpxWanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfIpxWanEnable_Type.__name__ = "Integer32"
_IpxIfIpxWanEnable_Object = MibTableColumn
ipxIfIpxWanEnable = _IpxIfIpxWanEnable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 13),
    _IpxIfIpxWanEnable_Type()
)
ipxIfIpxWanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfIpxWanEnable.setStatus("mandatory")


class _IpxIfNetbiosAccept_Type(Integer32):
    """Custom type ipxIfNetbiosAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfNetbiosAccept_Type.__name__ = "Integer32"
_IpxIfNetbiosAccept_Object = MibTableColumn
ipxIfNetbiosAccept = _IpxIfNetbiosAccept_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 14),
    _IpxIfNetbiosAccept_Type()
)
ipxIfNetbiosAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfNetbiosAccept.setStatus("mandatory")


class _IpxIfNetbiosDeliver_Type(Integer32):
    """Custom type ipxIfNetbiosDeliver based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledForStaticlySeededNames", 3),
          ("enabledWhenOperStateUp", 4))
    )


_IpxIfNetbiosDeliver_Type.__name__ = "Integer32"
_IpxIfNetbiosDeliver_Object = MibTableColumn
ipxIfNetbiosDeliver = _IpxIfNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 15),
    _IpxIfNetbiosDeliver_Type()
)
ipxIfNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfNetbiosDeliver.setStatus("mandatory")
_IpxIfInHdrErrors_Type = Counter32
_IpxIfInHdrErrors_Object = MibTableColumn
ipxIfInHdrErrors = _IpxIfInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 16),
    _IpxIfInHdrErrors_Type()
)
ipxIfInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInHdrErrors.setStatus("mandatory")
_IpxIfInFilterDrops_Type = Counter32
_IpxIfInFilterDrops_Object = MibTableColumn
ipxIfInFilterDrops = _IpxIfInFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 17),
    _IpxIfInFilterDrops_Type()
)
ipxIfInFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInFilterDrops.setStatus("mandatory")
_IpxIfInNoRoutes_Type = Counter32
_IpxIfInNoRoutes_Object = MibTableColumn
ipxIfInNoRoutes = _IpxIfInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 18),
    _IpxIfInNoRoutes_Type()
)
ipxIfInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInNoRoutes.setStatus("mandatory")
_IpxIfInDiscards_Type = Counter32
_IpxIfInDiscards_Object = MibTableColumn
ipxIfInDiscards = _IpxIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 19),
    _IpxIfInDiscards_Type()
)
ipxIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInDiscards.setStatus("mandatory")
_IpxIfInDelivers_Type = Counter32
_IpxIfInDelivers_Object = MibTableColumn
ipxIfInDelivers = _IpxIfInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 20),
    _IpxIfInDelivers_Type()
)
ipxIfInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInDelivers.setStatus("mandatory")
_IpxIfOutFilterDrops_Type = Counter32
_IpxIfOutFilterDrops_Object = MibTableColumn
ipxIfOutFilterDrops = _IpxIfOutFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 21),
    _IpxIfOutFilterDrops_Type()
)
ipxIfOutFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfOutFilterDrops.setStatus("mandatory")
_IpxIfOutDiscards_Type = Counter32
_IpxIfOutDiscards_Object = MibTableColumn
ipxIfOutDiscards = _IpxIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 22),
    _IpxIfOutDiscards_Type()
)
ipxIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfOutDiscards.setStatus("mandatory")
_IpxIfOutDelivers_Type = Counter32
_IpxIfOutDelivers_Object = MibTableColumn
ipxIfOutDelivers = _IpxIfOutDelivers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 23),
    _IpxIfOutDelivers_Type()
)
ipxIfOutDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfOutDelivers.setStatus("mandatory")
_IpxIfInNetbiosPackets_Type = Counter32
_IpxIfInNetbiosPackets_Object = MibTableColumn
ipxIfInNetbiosPackets = _IpxIfInNetbiosPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 24),
    _IpxIfInNetbiosPackets_Type()
)
ipxIfInNetbiosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfInNetbiosPackets.setStatus("mandatory")
_IpxIfOutNetbiosPackets_Type = Counter32
_IpxIfOutNetbiosPackets_Object = MibTableColumn
ipxIfOutNetbiosPackets = _IpxIfOutNetbiosPackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 25),
    _IpxIfOutNetbiosPackets_Type()
)
ipxIfOutNetbiosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfOutNetbiosPackets.setStatus("mandatory")
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3)
)
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1)
)
ipxDestEntry.setIndexNames(
    (0, "MSIPX-MIB", "ipxDestNetNum"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestNetNum_Type = NetNumber
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 1),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 2),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 3),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 4),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")
_IpxDestNextHopIfIndex_Type = Integer32
_IpxDestNextHopIfIndex_Object = MibTableColumn
ipxDestNextHopIfIndex = _IpxDestNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 5),
    _IpxDestNextHopIfIndex_Type()
)
ipxDestNextHopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNextHopIfIndex.setStatus("mandatory")
_IpxDestNextHopMacAddress_Type = PhysAddress
_IpxDestNextHopMacAddress_Object = MibTableColumn
ipxDestNextHopMacAddress = _IpxDestNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 6),
    _IpxDestNextHopMacAddress_Type()
)
ipxDestNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNextHopMacAddress.setStatus("mandatory")


class _IpxDestFlags_Type(Integer32):
    """Custom type ipxDestFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IpxDestFlags_Type.__name__ = "Integer32"
_IpxDestFlags_Object = MibTableColumn
ipxDestFlags = _IpxDestFlags_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 7),
    _IpxDestFlags_Type()
)
ipxDestFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestFlags.setStatus("mandatory")
_IpxStaticRouteTable_Object = MibTable
ipxStaticRouteTable = _IpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    ipxStaticRouteTable.setStatus("mandatory")
_IpxStaticRouteEntry_Object = MibTableRow
ipxStaticRouteEntry = _IpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1)
)
ipxStaticRouteEntry.setIndexNames(
    (0, "MSIPX-MIB", "ipxStaticRouteIfIndex"),
    (0, "MSIPX-MIB", "ipxStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    ipxStaticRouteEntry.setStatus("mandatory")
_IpxStaticRouteIfIndex_Type = Integer32
_IpxStaticRouteIfIndex_Object = MibTableColumn
ipxStaticRouteIfIndex = _IpxStaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 1),
    _IpxStaticRouteIfIndex_Type()
)
ipxStaticRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticRouteIfIndex.setStatus("mandatory")
_IpxStaticRouteNetNum_Type = NetNumber
_IpxStaticRouteNetNum_Object = MibTableColumn
ipxStaticRouteNetNum = _IpxStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 2),
    _IpxStaticRouteNetNum_Type()
)
ipxStaticRouteNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticRouteNetNum.setStatus("mandatory")


class _IpxStaticRouteEntryStatus_Type(Integer32):
    """Custom type ipxStaticRouteEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("deleted", 1))
    )


_IpxStaticRouteEntryStatus_Type.__name__ = "Integer32"
_IpxStaticRouteEntryStatus_Object = MibTableColumn
ipxStaticRouteEntryStatus = _IpxStaticRouteEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 3),
    _IpxStaticRouteEntryStatus_Type()
)
ipxStaticRouteEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteEntryStatus.setStatus("mandatory")
_IpxStaticRouteTicks_Type = Integer32
_IpxStaticRouteTicks_Object = MibTableColumn
ipxStaticRouteTicks = _IpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 4),
    _IpxStaticRouteTicks_Type()
)
ipxStaticRouteTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteTicks.setStatus("mandatory")
_IpxStaticRouteHopCount_Type = Integer32
_IpxStaticRouteHopCount_Object = MibTableColumn
ipxStaticRouteHopCount = _IpxStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 5),
    _IpxStaticRouteHopCount_Type()
)
ipxStaticRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteHopCount.setStatus("mandatory")
_IpxStaticRouteNextHopMacAddress_Type = PhysAddress
_IpxStaticRouteNextHopMacAddress_Object = MibTableColumn
ipxStaticRouteNextHopMacAddress = _IpxStaticRouteNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 6),
    _IpxStaticRouteNextHopMacAddress_Type()
)
ipxStaticRouteNextHopMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteNextHopMacAddress.setStatus("mandatory")
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4)
)
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1)
)
ipxServEntry.setIndexNames(
    (0, "MSIPX-MIB", "ipxServType"),
    (0, "MSIPX-MIB", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")


class _IpxServType_Type(OctetString):
    """Custom type ipxServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServType_Type.__name__ = "OctetString"
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 1),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServName_Type(OctetString):
    """Custom type ipxServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "OctetString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 2),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 3),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNumber
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 4),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 5),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")


class _IpxServSocket_Type(OctetString):
    """Custom type ipxServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServSocket_Type.__name__ = "OctetString"
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 6),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 7),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("mandatory")
_IpxStaticServTable_Object = MibTable
ipxStaticServTable = _IpxStaticServTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    ipxStaticServTable.setStatus("mandatory")
_IpxStaticServEntry_Object = MibTableRow
ipxStaticServEntry = _IpxStaticServEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1)
)
ipxStaticServEntry.setIndexNames(
    (0, "MSIPX-MIB", "ipxStaticServIfIndex"),
    (0, "MSIPX-MIB", "ipxStaticServType"),
    (0, "MSIPX-MIB", "ipxStaticServName"),
)
if mibBuilder.loadTexts:
    ipxStaticServEntry.setStatus("mandatory")
_IpxStaticServIfIndex_Type = Integer32
_IpxStaticServIfIndex_Object = MibTableColumn
ipxStaticServIfIndex = _IpxStaticServIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 1),
    _IpxStaticServIfIndex_Type()
)
ipxStaticServIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticServIfIndex.setStatus("mandatory")


class _IpxStaticServType_Type(OctetString):
    """Custom type ipxStaticServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxStaticServType_Type.__name__ = "OctetString"
_IpxStaticServType_Object = MibTableColumn
ipxStaticServType = _IpxStaticServType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 2),
    _IpxStaticServType_Type()
)
ipxStaticServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticServType.setStatus("mandatory")


class _IpxStaticServName_Type(OctetString):
    """Custom type ipxStaticServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxStaticServName_Type.__name__ = "OctetString"
_IpxStaticServName_Object = MibTableColumn
ipxStaticServName = _IpxStaticServName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 3),
    _IpxStaticServName_Type()
)
ipxStaticServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticServName.setStatus("mandatory")


class _IpxStaticServEntryStatus_Type(Integer32):
    """Custom type ipxStaticServEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("deleted", 1))
    )


_IpxStaticServEntryStatus_Type.__name__ = "Integer32"
_IpxStaticServEntryStatus_Object = MibTableColumn
ipxStaticServEntryStatus = _IpxStaticServEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 4),
    _IpxStaticServEntryStatus_Type()
)
ipxStaticServEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServEntryStatus.setStatus("mandatory")
_IpxStaticServNetNum_Type = NetNumber
_IpxStaticServNetNum_Object = MibTableColumn
ipxStaticServNetNum = _IpxStaticServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 5),
    _IpxStaticServNetNum_Type()
)
ipxStaticServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServNetNum.setStatus("mandatory")
_IpxStaticServNode_Type = PhysAddress
_IpxStaticServNode_Object = MibTableColumn
ipxStaticServNode = _IpxStaticServNode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 6),
    _IpxStaticServNode_Type()
)
ipxStaticServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServNode.setStatus("mandatory")


class _IpxStaticServSocket_Type(OctetString):
    """Custom type ipxStaticServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxStaticServSocket_Type.__name__ = "OctetString"
_IpxStaticServSocket_Object = MibTableColumn
ipxStaticServSocket = _IpxStaticServSocket_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 7),
    _IpxStaticServSocket_Type()
)
ipxStaticServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServSocket.setStatus("mandatory")
_IpxStaticServHopCount_Type = Integer32
_IpxStaticServHopCount_Object = MibTableColumn
ipxStaticServHopCount = _IpxStaticServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 8),
    _IpxStaticServHopCount_Type()
)
ipxStaticServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServHopCount.setStatus("mandatory")
_IpxTraps_ObjectIdentity = ObjectIdentity
ipxTraps = _IpxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 8, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSIPX-MIB",
    **{"NetNumber": NetNumber,
       "PhysAddress": PhysAddress,
       "ipx": ipx,
       "ipxBase": ipxBase,
       "ipxBaseOperState": ipxBaseOperState,
       "ipxBasePrimaryNetNumber": ipxBasePrimaryNetNumber,
       "ipxBaseNode": ipxBaseNode,
       "ipxBaseSysName": ipxBaseSysName,
       "ipxBaseMaxPathSplits": ipxBaseMaxPathSplits,
       "ipxBaseIfCount": ipxBaseIfCount,
       "ipxBaseDestCount": ipxBaseDestCount,
       "ipxBaseServCount": ipxBaseServCount,
       "ipxInterface": ipxInterface,
       "ipxIfTable": ipxIfTable,
       "ipxIfEntry": ipxIfEntry,
       "ipxIfIndex": ipxIfIndex,
       "ipxIfAdminState": ipxIfAdminState,
       "ipxIfOperState": ipxIfOperState,
       "ipxIfAdapterIndex": ipxIfAdapterIndex,
       "ipxIfName": ipxIfName,
       "ipxIfType": ipxIfType,
       "ipxIfLocalMaxPacketSize": ipxIfLocalMaxPacketSize,
       "ipxIfMediaType": ipxIfMediaType,
       "ipxIfNetNumber": ipxIfNetNumber,
       "ipxIfMacAddress": ipxIfMacAddress,
       "ipxIfDelay": ipxIfDelay,
       "ipxIfThroughput": ipxIfThroughput,
       "ipxIfIpxWanEnable": ipxIfIpxWanEnable,
       "ipxIfNetbiosAccept": ipxIfNetbiosAccept,
       "ipxIfNetbiosDeliver": ipxIfNetbiosDeliver,
       "ipxIfInHdrErrors": ipxIfInHdrErrors,
       "ipxIfInFilterDrops": ipxIfInFilterDrops,
       "ipxIfInNoRoutes": ipxIfInNoRoutes,
       "ipxIfInDiscards": ipxIfInDiscards,
       "ipxIfInDelivers": ipxIfInDelivers,
       "ipxIfOutFilterDrops": ipxIfOutFilterDrops,
       "ipxIfOutDiscards": ipxIfOutDiscards,
       "ipxIfOutDelivers": ipxIfOutDelivers,
       "ipxIfInNetbiosPackets": ipxIfInNetbiosPackets,
       "ipxIfOutNetbiosPackets": ipxIfOutNetbiosPackets,
       "ipxForwarding": ipxForwarding,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopIfIndex": ipxDestNextHopIfIndex,
       "ipxDestNextHopMacAddress": ipxDestNextHopMacAddress,
       "ipxDestFlags": ipxDestFlags,
       "ipxStaticRouteTable": ipxStaticRouteTable,
       "ipxStaticRouteEntry": ipxStaticRouteEntry,
       "ipxStaticRouteIfIndex": ipxStaticRouteIfIndex,
       "ipxStaticRouteNetNum": ipxStaticRouteNetNum,
       "ipxStaticRouteEntryStatus": ipxStaticRouteEntryStatus,
       "ipxStaticRouteTicks": ipxStaticRouteTicks,
       "ipxStaticRouteHopCount": ipxStaticRouteHopCount,
       "ipxStaticRouteNextHopMacAddress": ipxStaticRouteNextHopMacAddress,
       "ipxServices": ipxServices,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxStaticServTable": ipxStaticServTable,
       "ipxStaticServEntry": ipxStaticServEntry,
       "ipxStaticServIfIndex": ipxStaticServIfIndex,
       "ipxStaticServType": ipxStaticServType,
       "ipxStaticServName": ipxStaticServName,
       "ipxStaticServEntryStatus": ipxStaticServEntryStatus,
       "ipxStaticServNetNum": ipxStaticServNetNum,
       "ipxStaticServNode": ipxStaticServNode,
       "ipxStaticServSocket": ipxStaticServSocket,
       "ipxStaticServHopCount": ipxStaticServHopCount,
       "ipxTraps": ipxTraps}
)
