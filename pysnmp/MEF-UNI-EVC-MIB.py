# SNMP MIB module (MEF-UNI-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MEF-UNI-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:50 2024
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

(EntityAdminState,
 EntityOperState) = mibBuilder.importSymbols(
    "ENTITY-STATE-TC-MIB",
    "EntityAdminState",
    "EntityOperState")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mefUniEvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2)
)
mefUniEvcMib.setRevisions(
        ("2013-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MefServicePreservationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPreserve", 2),
          ("preserve", 1))
    )



class MefServiceDeliveryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conditional", 3),
          ("discard", 1),
          ("unconditional", 2))
    )



class MefServiceInterfaceType(Bits, TextualConvention):
    status = "current"


class MefServiceListType(OctetString, TextualConvention):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_MefServiceNotifications_ObjectIdentity = ObjectIdentity
mefServiceNotifications = _MefServiceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 0)
)
_MefServiceObjects_ObjectIdentity = ObjectIdentity
mefServiceObjects = _MefServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1)
)
_MefServiceInterfaceAttributes_ObjectIdentity = ObjectIdentity
mefServiceInterfaceAttributes = _MefServiceInterfaceAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1)
)
_MefServiceInterfaceCfgTable_Object = MibTable
mefServiceInterfaceCfgTable = _MefServiceInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgTable.setStatus("current")
_MefServiceInterfaceCfgEntry_Object = MibTableRow
mefServiceInterfaceCfgEntry = _MefServiceInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1)
)
mefServiceInterfaceCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgEntry.setStatus("current")


class _MefServiceInterfaceCfgType_Type(MefServiceInterfaceType):
    """Custom type mefServiceInterfaceCfgType based on MefServiceInterfaceType"""
    defaultBinValue = "1"


_MefServiceInterfaceCfgType_Object = MibTableColumn
mefServiceInterfaceCfgType = _MefServiceInterfaceCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 1),
    _MefServiceInterfaceCfgType_Type()
)
mefServiceInterfaceCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgType.setStatus("current")
_MefServiceInterfaceCfgIdentifier_Type = DisplayString
_MefServiceInterfaceCfgIdentifier_Object = MibTableColumn
mefServiceInterfaceCfgIdentifier = _MefServiceInterfaceCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 2),
    _MefServiceInterfaceCfgIdentifier_Type()
)
mefServiceInterfaceCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgIdentifier.setStatus("current")


class _MefServiceInterfaceCfgFrameFormat_Type(Integer32):
    """Custom type mefServiceInterfaceCfgFrameFormat based on Integer32"""
    defaultValue = 1

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
        *(("ctag", 2),
          ("noTag", 1),
          ("stag", 3),
          ("stagCtag", 4))
    )


_MefServiceInterfaceCfgFrameFormat_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgFrameFormat_Object = MibTableColumn
mefServiceInterfaceCfgFrameFormat = _MefServiceInterfaceCfgFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 3),
    _MefServiceInterfaceCfgFrameFormat_Type()
)
mefServiceInterfaceCfgFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgFrameFormat.setStatus("current")


class _MefServiceInterfaceCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceInterfaceCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceInterfaceCfgIngressBwpGrpIndex = _MefServiceInterfaceCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 4),
    _MefServiceInterfaceCfgIngressBwpGrpIndex_Type()
)
mefServiceInterfaceCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceInterfaceCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceInterfaceCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceInterfaceCfgEgressBwpGrpIndex = _MefServiceInterfaceCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 5),
    _MefServiceInterfaceCfgEgressBwpGrpIndex_Type()
)
mefServiceInterfaceCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgEgressBwpGrpIndex.setStatus("current")


class _MefServiceInterfaceCfgL2cpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgL2cpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceInterfaceCfgL2cpGrpIndex_Object = MibTableColumn
mefServiceInterfaceCfgL2cpGrpIndex = _MefServiceInterfaceCfgL2cpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 9),
    _MefServiceInterfaceCfgL2cpGrpIndex_Type()
)
mefServiceInterfaceCfgL2cpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgL2cpGrpIndex.setStatus("current")
_MefServiceInterfaceStatusTable_Object = MibTable
mefServiceInterfaceStatusTable = _MefServiceInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusTable.setStatus("current")
_MefServiceInterfaceStatusEntry_Object = MibTableRow
mefServiceInterfaceStatusEntry = _MefServiceInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1)
)
mefServiceInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusEntry.setStatus("current")
_MefServiceInterfaceStatusType_Type = MefServiceInterfaceType
_MefServiceInterfaceStatusType_Object = MibTableColumn
mefServiceInterfaceStatusType = _MefServiceInterfaceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 1),
    _MefServiceInterfaceStatusType_Type()
)
mefServiceInterfaceStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusType.setStatus("current")


class _MefServiceInterfaceStatusMaxVc_Type(Unsigned32):
    """Custom type mefServiceInterfaceStatusMaxVc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MefServiceInterfaceStatusMaxVc_Type.__name__ = "Unsigned32"
_MefServiceInterfaceStatusMaxVc_Object = MibTableColumn
mefServiceInterfaceStatusMaxVc = _MefServiceInterfaceStatusMaxVc_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 2),
    _MefServiceInterfaceStatusMaxVc_Type()
)
mefServiceInterfaceStatusMaxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMaxVc.setStatus("current")


class _MefServiceInterfaceStatusMaxEndPointPerVc_Type(Unsigned32):
    """Custom type mefServiceInterfaceStatusMaxEndPointPerVc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MefServiceInterfaceStatusMaxEndPointPerVc_Type.__name__ = "Unsigned32"
_MefServiceInterfaceStatusMaxEndPointPerVc_Object = MibTableColumn
mefServiceInterfaceStatusMaxEndPointPerVc = _MefServiceInterfaceStatusMaxEndPointPerVc_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 3),
    _MefServiceInterfaceStatusMaxEndPointPerVc_Type()
)
mefServiceInterfaceStatusMaxEndPointPerVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMaxEndPointPerVc.setStatus("current")
_MefServiceInterfaceStatisticsTable_Object = MibTable
mefServiceInterfaceStatisticsTable = _MefServiceInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsTable.setStatus("current")
_MefServiceInterfaceStatisticsEntry_Object = MibTableRow
mefServiceInterfaceStatisticsEntry = _MefServiceInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1)
)
mefServiceInterfaceStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEntry.setStatus("current")
_MefServiceInterfaceStatisticsIngressUndersized_Type = Counter32
_MefServiceInterfaceStatisticsIngressUndersized_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressUndersized = _MefServiceInterfaceStatisticsIngressUndersized_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 1),
    _MefServiceInterfaceStatisticsIngressUndersized_Type()
)
mefServiceInterfaceStatisticsIngressUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressUndersized.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressUndersized.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressOversized_Type = Counter32
_MefServiceInterfaceStatisticsIngressOversized_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressOversized = _MefServiceInterfaceStatisticsIngressOversized_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 2),
    _MefServiceInterfaceStatisticsIngressOversized_Type()
)
mefServiceInterfaceStatisticsIngressOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressOversized.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressOversized.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressFragments_Type = Counter32
_MefServiceInterfaceStatisticsIngressFragments_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressFragments = _MefServiceInterfaceStatisticsIngressFragments_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 3),
    _MefServiceInterfaceStatisticsIngressFragments_Type()
)
mefServiceInterfaceStatisticsIngressFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressFragments.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressFragments.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressCrcAlignment_Type = Counter32
_MefServiceInterfaceStatisticsIngressCrcAlignment_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressCrcAlignment = _MefServiceInterfaceStatisticsIngressCrcAlignment_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 4),
    _MefServiceInterfaceStatisticsIngressCrcAlignment_Type()
)
mefServiceInterfaceStatisticsIngressCrcAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressCrcAlignment.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressCrcAlignment.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressInvalidVid_Type = Counter32
_MefServiceInterfaceStatisticsIngressInvalidVid_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressInvalidVid = _MefServiceInterfaceStatisticsIngressInvalidVid_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 5),
    _MefServiceInterfaceStatisticsIngressInvalidVid_Type()
)
mefServiceInterfaceStatisticsIngressInvalidVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressInvalidVid.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressInvalidVid.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressOctets_Type = Counter64
_MefServiceInterfaceStatisticsIngressOctets_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressOctets = _MefServiceInterfaceStatisticsIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 6),
    _MefServiceInterfaceStatisticsIngressOctets_Type()
)
mefServiceInterfaceStatisticsIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressOctets.setUnits("octets")
_MefServiceInterfaceStatisticsIngressUnicast_Type = Counter64
_MefServiceInterfaceStatisticsIngressUnicast_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressUnicast = _MefServiceInterfaceStatisticsIngressUnicast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 7),
    _MefServiceInterfaceStatisticsIngressUnicast_Type()
)
mefServiceInterfaceStatisticsIngressUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressUnicast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressUnicast.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressMulticast_Type = Counter64
_MefServiceInterfaceStatisticsIngressMulticast_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressMulticast = _MefServiceInterfaceStatisticsIngressMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 8),
    _MefServiceInterfaceStatisticsIngressMulticast_Type()
)
mefServiceInterfaceStatisticsIngressMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressMulticast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressMulticast.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsIngressBroadcast_Type = Counter64
_MefServiceInterfaceStatisticsIngressBroadcast_Object = MibTableColumn
mefServiceInterfaceStatisticsIngressBroadcast = _MefServiceInterfaceStatisticsIngressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 9),
    _MefServiceInterfaceStatisticsIngressBroadcast_Type()
)
mefServiceInterfaceStatisticsIngressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsIngressBroadcast.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsEgressOctets_Type = Counter64
_MefServiceInterfaceStatisticsEgressOctets_Object = MibTableColumn
mefServiceInterfaceStatisticsEgressOctets = _MefServiceInterfaceStatisticsEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 10),
    _MefServiceInterfaceStatisticsEgressOctets_Type()
)
mefServiceInterfaceStatisticsEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressOctets.setUnits("octets")
_MefServiceInterfaceStatisticsEgressUnicast_Type = Counter64
_MefServiceInterfaceStatisticsEgressUnicast_Object = MibTableColumn
mefServiceInterfaceStatisticsEgressUnicast = _MefServiceInterfaceStatisticsEgressUnicast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 11),
    _MefServiceInterfaceStatisticsEgressUnicast_Type()
)
mefServiceInterfaceStatisticsEgressUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressUnicast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressUnicast.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsEgressMulticast_Type = Counter64
_MefServiceInterfaceStatisticsEgressMulticast_Object = MibTableColumn
mefServiceInterfaceStatisticsEgressMulticast = _MefServiceInterfaceStatisticsEgressMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 12),
    _MefServiceInterfaceStatisticsEgressMulticast_Type()
)
mefServiceInterfaceStatisticsEgressMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressMulticast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressMulticast.setUnits("Ethernet frames")
_MefServiceInterfaceStatisticsEgressBroadcast_Type = Counter64
_MefServiceInterfaceStatisticsEgressBroadcast_Object = MibTableColumn
mefServiceInterfaceStatisticsEgressBroadcast = _MefServiceInterfaceStatisticsEgressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 3, 1, 13),
    _MefServiceInterfaceStatisticsEgressBroadcast_Type()
)
mefServiceInterfaceStatisticsEgressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatisticsEgressBroadcast.setUnits("Ethernet frames")
_MefServiceUniAttributes_ObjectIdentity = ObjectIdentity
mefServiceUniAttributes = _MefServiceUniAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2)
)
_MefServiceUniCfgTable_Object = MibTable
mefServiceUniCfgTable = _MefServiceUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefServiceUniCfgTable.setStatus("current")
_MefServiceUniCfgEntry_Object = MibTableRow
mefServiceUniCfgEntry = _MefServiceUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1)
)
mefServiceUniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceUniCfgEntry.setStatus("current")
_MefServiceUniCfgIdentifier_Type = DisplayString
_MefServiceUniCfgIdentifier_Object = MibTableColumn
mefServiceUniCfgIdentifier = _MefServiceUniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 1),
    _MefServiceUniCfgIdentifier_Type()
)
mefServiceUniCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceUniCfgIdentifier.setStatus("current")


class _MefServiceUniCfgBundlingMultiplex_Type(Integer32):
    """Custom type mefServiceUniCfgBundlingMultiplex based on Integer32"""
    defaultValue = 1

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
        *(("allToOne", 1),
          ("bundling", 2),
          ("bundlingMultiplex", 4),
          ("multiplex", 3))
    )


_MefServiceUniCfgBundlingMultiplex_Type.__name__ = "Integer32"
_MefServiceUniCfgBundlingMultiplex_Object = MibTableColumn
mefServiceUniCfgBundlingMultiplex = _MefServiceUniCfgBundlingMultiplex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 2),
    _MefServiceUniCfgBundlingMultiplex_Type()
)
mefServiceUniCfgBundlingMultiplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceUniCfgBundlingMultiplex.setStatus("current")


class _MefServiceUniCfgCeVidUntagged_Type(VlanId):
    """Custom type mefServiceUniCfgCeVidUntagged based on VlanId"""
    defaultValue = 1


_MefServiceUniCfgCeVidUntagged_Object = MibTableColumn
mefServiceUniCfgCeVidUntagged = _MefServiceUniCfgCeVidUntagged_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 3),
    _MefServiceUniCfgCeVidUntagged_Type()
)
mefServiceUniCfgCeVidUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceUniCfgCeVidUntagged.setStatus("current")


class _MefServiceUniCfgCePriorityUntagged_Type(IEEE8021PriorityValue):
    """Custom type mefServiceUniCfgCePriorityUntagged based on IEEE8021PriorityValue"""
    defaultValue = 0


_MefServiceUniCfgCePriorityUntagged_Object = MibTableColumn
mefServiceUniCfgCePriorityUntagged = _MefServiceUniCfgCePriorityUntagged_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 4),
    _MefServiceUniCfgCePriorityUntagged_Type()
)
mefServiceUniCfgCePriorityUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceUniCfgCePriorityUntagged.setStatus("current")
_MefServiceEvcPerUniCfgTable_Object = MibTable
mefServiceEvcPerUniCfgTable = _MefServiceEvcPerUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgTable.setStatus("current")
_MefServiceEvcPerUniCfgEntry_Object = MibTableRow
mefServiceEvcPerUniCfgEntry = _MefServiceEvcPerUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1)
)
mefServiceEvcPerUniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-UNI-EVC-MIB", "mefServiceEvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgEntry.setStatus("current")


class _MefServiceEvcPerUniCfgServiceType_Type(Integer32):
    """Custom type mefServiceEvcPerUniCfgServiceType based on Integer32"""
    defaultValue = 1

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
        *(("epl", 1),
          ("eplan", 3),
          ("eptree", 5),
          ("evpl", 2),
          ("evplan", 4),
          ("evptree", 6))
    )


_MefServiceEvcPerUniCfgServiceType_Type.__name__ = "Integer32"
_MefServiceEvcPerUniCfgServiceType_Object = MibTableColumn
mefServiceEvcPerUniCfgServiceType = _MefServiceEvcPerUniCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1, 1),
    _MefServiceEvcPerUniCfgServiceType_Type()
)
mefServiceEvcPerUniCfgServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgServiceType.setStatus("current")


class _MefServiceEvcPerUniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceEvcPerUniCfgIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_MefServiceEvcPerUniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceEvcPerUniCfgIdentifier_Object = MibTableColumn
mefServiceEvcPerUniCfgIdentifier = _MefServiceEvcPerUniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1, 2),
    _MefServiceEvcPerUniCfgIdentifier_Type()
)
mefServiceEvcPerUniCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgIdentifier.setStatus("current")


class _MefServiceEvcPerUniCfgCeVlanMap_Type(MefServiceListType):
    """Custom type mefServiceEvcPerUniCfgCeVlanMap based on MefServiceListType"""
    defaultValue = OctetString("1:4095")


_MefServiceEvcPerUniCfgCeVlanMap_Object = MibTableColumn
mefServiceEvcPerUniCfgCeVlanMap = _MefServiceEvcPerUniCfgCeVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1, 3),
    _MefServiceEvcPerUniCfgCeVlanMap_Type()
)
mefServiceEvcPerUniCfgCeVlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgCeVlanMap.setStatus("current")


class _MefServiceEvcPerUniCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceEvcPerUniCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgIngressBwpGrpIndex = _MefServiceEvcPerUniCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1, 4),
    _MefServiceEvcPerUniCfgIngressBwpGrpIndex_Type()
)
mefServiceEvcPerUniCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceEvcPerUniCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceEvcPerUniCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgEgressBwpGrpIndex = _MefServiceEvcPerUniCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 2, 1, 5),
    _MefServiceEvcPerUniCfgEgressBwpGrpIndex_Type()
)
mefServiceEvcPerUniCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgEgressBwpGrpIndex.setStatus("current")
_MefServiceEvcAttributes_ObjectIdentity = ObjectIdentity
mefServiceEvcAttributes = _MefServiceEvcAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3)
)


class _MefServiceEvcNextIndex_Type(Unsigned32):
    """Custom type mefServiceEvcNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceEvcNextIndex_Object = MibScalar
mefServiceEvcNextIndex = _MefServiceEvcNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1),
    _MefServiceEvcNextIndex_Type()
)
mefServiceEvcNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcNextIndex.setStatus("current")
_MefServiceEvcCfgTable_Object = MibTable
mefServiceEvcCfgTable = _MefServiceEvcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefServiceEvcCfgTable.setStatus("current")
_MefServiceEvcCfgEntry_Object = MibTableRow
mefServiceEvcCfgEntry = _MefServiceEvcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1)
)
mefServiceEvcCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceEvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceEvcCfgEntry.setStatus("current")
_MefServiceEvcCfgIndex_Type = Unsigned32
_MefServiceEvcCfgIndex_Object = MibTableColumn
mefServiceEvcCfgIndex = _MefServiceEvcCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 1),
    _MefServiceEvcCfgIndex_Type()
)
mefServiceEvcCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceEvcCfgIndex.setStatus("current")
_MefServiceEvcCfgIdentifier_Type = DisplayString
_MefServiceEvcCfgIdentifier_Object = MibTableColumn
mefServiceEvcCfgIdentifier = _MefServiceEvcCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 2),
    _MefServiceEvcCfgIdentifier_Type()
)
mefServiceEvcCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgIdentifier.setStatus("current")


class _MefServiceEvcCfgServiceType_Type(Integer32):
    """Custom type mefServiceEvcCfgServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multipointToMultipoint", 2),
          ("pointToPoint", 1),
          ("rootedMultipoint", 3))
    )


_MefServiceEvcCfgServiceType_Type.__name__ = "Integer32"
_MefServiceEvcCfgServiceType_Object = MibTableColumn
mefServiceEvcCfgServiceType = _MefServiceEvcCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 3),
    _MefServiceEvcCfgServiceType_Type()
)
mefServiceEvcCfgServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgServiceType.setStatus("current")


class _MefServiceEvcCfgMtuSize_Type(Unsigned32):
    """Custom type mefServiceEvcCfgMtuSize based on Unsigned32"""
    defaultValue = 1522

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16384),
    )


_MefServiceEvcCfgMtuSize_Type.__name__ = "Unsigned32"
_MefServiceEvcCfgMtuSize_Object = MibTableColumn
mefServiceEvcCfgMtuSize = _MefServiceEvcCfgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 4),
    _MefServiceEvcCfgMtuSize_Type()
)
mefServiceEvcCfgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcCfgMtuSize.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceEvcCfgMtuSize.setUnits("octets")


class _MefServiceEvcCfgCevlanIdPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceEvcCfgCevlanIdPreservation based on MefServicePreservationType"""


_MefServiceEvcCfgCevlanIdPreservation_Object = MibTableColumn
mefServiceEvcCfgCevlanIdPreservation = _MefServiceEvcCfgCevlanIdPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 5),
    _MefServiceEvcCfgCevlanIdPreservation_Type()
)
mefServiceEvcCfgCevlanIdPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgCevlanIdPreservation.setStatus("current")


class _MefServiceEvcCfgCevlanCosPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceEvcCfgCevlanCosPreservation based on MefServicePreservationType"""


_MefServiceEvcCfgCevlanCosPreservation_Object = MibTableColumn
mefServiceEvcCfgCevlanCosPreservation = _MefServiceEvcCfgCevlanCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 6),
    _MefServiceEvcCfgCevlanCosPreservation_Type()
)
mefServiceEvcCfgCevlanCosPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgCevlanCosPreservation.setStatus("current")


class _MefServiceEvcCfgUnicastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceEvcCfgUnicastDelivery based on MefServiceDeliveryType"""


_MefServiceEvcCfgUnicastDelivery_Object = MibTableColumn
mefServiceEvcCfgUnicastDelivery = _MefServiceEvcCfgUnicastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 7),
    _MefServiceEvcCfgUnicastDelivery_Type()
)
mefServiceEvcCfgUnicastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgUnicastDelivery.setStatus("current")


class _MefServiceEvcCfgMulticastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceEvcCfgMulticastDelivery based on MefServiceDeliveryType"""


_MefServiceEvcCfgMulticastDelivery_Object = MibTableColumn
mefServiceEvcCfgMulticastDelivery = _MefServiceEvcCfgMulticastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 8),
    _MefServiceEvcCfgMulticastDelivery_Type()
)
mefServiceEvcCfgMulticastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgMulticastDelivery.setStatus("current")


class _MefServiceEvcCfgBroadcastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceEvcCfgBroadcastDelivery based on MefServiceDeliveryType"""


_MefServiceEvcCfgBroadcastDelivery_Object = MibTableColumn
mefServiceEvcCfgBroadcastDelivery = _MefServiceEvcCfgBroadcastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 9),
    _MefServiceEvcCfgBroadcastDelivery_Type()
)
mefServiceEvcCfgBroadcastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgBroadcastDelivery.setStatus("current")


class _MefServiceEvcCfgL2cpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceEvcCfgL2cpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceEvcCfgL2cpGrpIndex_Object = MibTableColumn
mefServiceEvcCfgL2cpGrpIndex = _MefServiceEvcCfgL2cpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 10),
    _MefServiceEvcCfgL2cpGrpIndex_Type()
)
mefServiceEvcCfgL2cpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcCfgL2cpGrpIndex.setStatus("current")


class _MefServiceEvcCfgAdminState_Type(EntityAdminState):
    """Custom type mefServiceEvcCfgAdminState based on EntityAdminState"""


_MefServiceEvcCfgAdminState_Object = MibTableColumn
mefServiceEvcCfgAdminState = _MefServiceEvcCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 11),
    _MefServiceEvcCfgAdminState_Type()
)
mefServiceEvcCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgAdminState.setStatus("current")
_MefServiceEvcCfgRowStatus_Type = RowStatus
_MefServiceEvcCfgRowStatus_Object = MibTableColumn
mefServiceEvcCfgRowStatus = _MefServiceEvcCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 12),
    _MefServiceEvcCfgRowStatus_Type()
)
mefServiceEvcCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcCfgRowStatus.setStatus("current")
_MefServiceEvcUniCfgTable_Object = MibTable
mefServiceEvcUniCfgTable = _MefServiceEvcUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mefServiceEvcUniCfgTable.setStatus("current")
_MefServiceEvcUniCfgEntry_Object = MibTableRow
mefServiceEvcUniCfgEntry = _MefServiceEvcUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 3, 1)
)
mefServiceEvcUniCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceEvcCfgIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceEvcUniCfgEntry.setStatus("current")


class _MefServiceEvcUniCfgType_Type(Integer32):
    """Custom type mefServiceEvcUniCfgType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 2),
          ("root", 1),
          ("unknown", 3))
    )


_MefServiceEvcUniCfgType_Type.__name__ = "Integer32"
_MefServiceEvcUniCfgType_Object = MibTableColumn
mefServiceEvcUniCfgType = _MefServiceEvcUniCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 3, 1, 1),
    _MefServiceEvcUniCfgType_Type()
)
mefServiceEvcUniCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcUniCfgType.setStatus("current")
_MefServiceEvcUniCfgRowStatus_Type = RowStatus
_MefServiceEvcUniCfgRowStatus_Object = MibTableColumn
mefServiceEvcUniCfgRowStatus = _MefServiceEvcUniCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 3, 1, 2),
    _MefServiceEvcUniCfgRowStatus_Type()
)
mefServiceEvcUniCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceEvcUniCfgRowStatus.setStatus("current")
_MefServiceEvcStatusTable_Object = MibTable
mefServiceEvcStatusTable = _MefServiceEvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mefServiceEvcStatusTable.setStatus("current")
_MefServiceEvcStatusEntry_Object = MibTableRow
mefServiceEvcStatusEntry = _MefServiceEvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 4, 1)
)
mefServiceEvcStatusEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceEvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceEvcStatusEntry.setStatus("current")


class _MefServiceEvcStatusMaxMtuSize_Type(Unsigned32):
    """Custom type mefServiceEvcStatusMaxMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16384),
    )


_MefServiceEvcStatusMaxMtuSize_Type.__name__ = "Unsigned32"
_MefServiceEvcStatusMaxMtuSize_Object = MibTableColumn
mefServiceEvcStatusMaxMtuSize = _MefServiceEvcStatusMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 4, 1, 1),
    _MefServiceEvcStatusMaxMtuSize_Type()
)
mefServiceEvcStatusMaxMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcStatusMaxMtuSize.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceEvcStatusMaxMtuSize.setUnits("octets")


class _MefServiceEvcStatusMaxNumUni_Type(Unsigned32):
    """Custom type mefServiceEvcStatusMaxNumUni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16384),
    )


_MefServiceEvcStatusMaxNumUni_Type.__name__ = "Unsigned32"
_MefServiceEvcStatusMaxNumUni_Object = MibTableColumn
mefServiceEvcStatusMaxNumUni = _MefServiceEvcStatusMaxNumUni_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 4, 1, 2),
    _MefServiceEvcStatusMaxNumUni_Type()
)
mefServiceEvcStatusMaxNumUni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcStatusMaxNumUni.setStatus("current")
_MefServiceEvcStatusOperationalState_Type = EntityOperState
_MefServiceEvcStatusOperationalState_Object = MibTableColumn
mefServiceEvcStatusOperationalState = _MefServiceEvcStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 4, 1, 3),
    _MefServiceEvcStatusOperationalState_Type()
)
mefServiceEvcStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcStatusOperationalState.setStatus("current")
_MefServiceBwpAttributes_ObjectIdentity = ObjectIdentity
mefServiceBwpAttributes = _MefServiceBwpAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4)
)


class _MefServiceBwpGrpNextIndex_Type(Unsigned32):
    """Custom type mefServiceBwpGrpNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceBwpGrpNextIndex_Object = MibScalar
mefServiceBwpGrpNextIndex = _MefServiceBwpGrpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 1),
    _MefServiceBwpGrpNextIndex_Type()
)
mefServiceBwpGrpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceBwpGrpNextIndex.setStatus("current")
_MefServiceBwpGrpCfgTable_Object = MibTable
mefServiceBwpGrpCfgTable = _MefServiceBwpGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mefServiceBwpGrpCfgTable.setStatus("current")
_MefServiceBwpGrpCfgEntry_Object = MibTableRow
mefServiceBwpGrpCfgEntry = _MefServiceBwpGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1)
)
mefServiceBwpGrpCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceBwpGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceBwpGrpCfgEntry.setStatus("current")
_MefServiceBwpGrpCfgIndex_Type = Unsigned32
_MefServiceBwpGrpCfgIndex_Object = MibTableColumn
mefServiceBwpGrpCfgIndex = _MefServiceBwpGrpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 1),
    _MefServiceBwpGrpCfgIndex_Type()
)
mefServiceBwpGrpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceBwpGrpCfgIndex.setStatus("current")


class _MefServiceBwpCfgNextIndex_Type(Unsigned32):
    """Custom type mefServiceBwpCfgNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceBwpCfgNextIndex_Object = MibTableColumn
mefServiceBwpCfgNextIndex = _MefServiceBwpCfgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 2),
    _MefServiceBwpCfgNextIndex_Type()
)
mefServiceBwpCfgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceBwpCfgNextIndex.setStatus("current")
_MefServiceBwpGrpCfgRowStatus_Type = RowStatus
_MefServiceBwpGrpCfgRowStatus_Object = MibTableColumn
mefServiceBwpGrpCfgRowStatus = _MefServiceBwpGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 3),
    _MefServiceBwpGrpCfgRowStatus_Type()
)
mefServiceBwpGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpGrpCfgRowStatus.setStatus("current")
_MefServiceBwpCfgTable_Object = MibTable
mefServiceBwpCfgTable = _MefServiceBwpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mefServiceBwpCfgTable.setStatus("current")
_MefServiceBwpCfgEntry_Object = MibTableRow
mefServiceBwpCfgEntry = _MefServiceBwpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1)
)
mefServiceBwpCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceBwpGrpCfgIndex"),
    (0, "MEF-UNI-EVC-MIB", "mefServiceBwpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceBwpCfgEntry.setStatus("current")
_MefServiceBwpCfgIndex_Type = Unsigned32
_MefServiceBwpCfgIndex_Object = MibTableColumn
mefServiceBwpCfgIndex = _MefServiceBwpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 1),
    _MefServiceBwpCfgIndex_Type()
)
mefServiceBwpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceBwpCfgIndex.setStatus("current")
_MefServiceBwpCfgIdentifier_Type = DisplayString
_MefServiceBwpCfgIdentifier_Object = MibTableColumn
mefServiceBwpCfgIdentifier = _MefServiceBwpCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 2),
    _MefServiceBwpCfgIdentifier_Type()
)
mefServiceBwpCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgIdentifier.setStatus("current")


class _MefServiceBwpCfgCir_Type(Unsigned32):
    """Custom type mefServiceBwpCfgCir based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_MefServiceBwpCfgCir_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgCir_Object = MibTableColumn
mefServiceBwpCfgCir = _MefServiceBwpCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 3),
    _MefServiceBwpCfgCir_Type()
)
mefServiceBwpCfgCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCir.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCir.setUnits("kbits/s")


class _MefServiceBwpCfgCbs_Type(Unsigned32):
    """Custom type mefServiceBwpCfgCbs based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_MefServiceBwpCfgCbs_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgCbs_Object = MibTableColumn
mefServiceBwpCfgCbs = _MefServiceBwpCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 4),
    _MefServiceBwpCfgCbs_Type()
)
mefServiceBwpCfgCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCbs.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCbs.setUnits("bytes")


class _MefServiceBwpCfgEir_Type(Unsigned32):
    """Custom type mefServiceBwpCfgEir based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_MefServiceBwpCfgEir_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgEir_Object = MibTableColumn
mefServiceBwpCfgEir = _MefServiceBwpCfgEir_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 5),
    _MefServiceBwpCfgEir_Type()
)
mefServiceBwpCfgEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEir.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEir.setUnits("kbits/s")


class _MefServiceBwpCfgEbs_Type(Unsigned32):
    """Custom type mefServiceBwpCfgEbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_MefServiceBwpCfgEbs_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgEbs_Object = MibTableColumn
mefServiceBwpCfgEbs = _MefServiceBwpCfgEbs_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 6),
    _MefServiceBwpCfgEbs_Type()
)
mefServiceBwpCfgEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEbs.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEbs.setUnits("bytes")


class _MefServiceBwpCfgCm_Type(Integer32):
    """Custom type mefServiceBwpCfgCm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 2),
          ("colorBlind", 1))
    )


_MefServiceBwpCfgCm_Type.__name__ = "Integer32"
_MefServiceBwpCfgCm_Object = MibTableColumn
mefServiceBwpCfgCm = _MefServiceBwpCfgCm_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 7),
    _MefServiceBwpCfgCm_Type()
)
mefServiceBwpCfgCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCm.setStatus("current")


class _MefServiceBwpCfgCf_Type(Integer32):
    """Custom type mefServiceBwpCfgCf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("couplingYellowEirOnly", 0),
          ("couplingYellowEirPlusCir", 1))
    )


_MefServiceBwpCfgCf_Type.__name__ = "Integer32"
_MefServiceBwpCfgCf_Object = MibTableColumn
mefServiceBwpCfgCf = _MefServiceBwpCfgCf_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 8),
    _MefServiceBwpCfgCf_Type()
)
mefServiceBwpCfgCf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCf.setStatus("current")


class _MefServiceBwpCfgCosIndex_Type(Unsigned32):
    """Custom type mefServiceBwpCfgCosIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceBwpCfgCosIndex_Object = MibTableColumn
mefServiceBwpCfgCosIndex = _MefServiceBwpCfgCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 9),
    _MefServiceBwpCfgCosIndex_Type()
)
mefServiceBwpCfgCosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCosIndex.setStatus("current")


class _MefServiceBwpCfgPerformanceEnable_Type(Integer32):
    """Custom type mefServiceBwpCfgPerformanceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablePerformanceDataSet", 1),
          ("enablePerformanceDataSet", 2))
    )


_MefServiceBwpCfgPerformanceEnable_Type.__name__ = "Integer32"
_MefServiceBwpCfgPerformanceEnable_Object = MibTableColumn
mefServiceBwpCfgPerformanceEnable = _MefServiceBwpCfgPerformanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 10),
    _MefServiceBwpCfgPerformanceEnable_Type()
)
mefServiceBwpCfgPerformanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceBwpCfgPerformanceEnable.setStatus("current")
_MefServiceBwpCfgRowStatus_Type = RowStatus
_MefServiceBwpCfgRowStatus_Object = MibTableColumn
mefServiceBwpCfgRowStatus = _MefServiceBwpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 3, 1, 11),
    _MefServiceBwpCfgRowStatus_Type()
)
mefServiceBwpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgRowStatus.setStatus("current")
_MefServicePerformanceTable_Object = MibTable
mefServicePerformanceTable = _MefServicePerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    mefServicePerformanceTable.setStatus("current")
_MefServicePerformanceEntry_Object = MibTableRow
mefServicePerformanceEntry = _MefServicePerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1)
)
mefServicePerformanceEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceBwpGrpCfgIndex"),
    (0, "MEF-UNI-EVC-MIB", "mefServiceBwpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServicePerformanceEntry.setStatus("current")
_MefServicePerformanceIngressGreenFrameCount_Type = Counter64
_MefServicePerformanceIngressGreenFrameCount_Object = MibTableColumn
mefServicePerformanceIngressGreenFrameCount = _MefServicePerformanceIngressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 1),
    _MefServicePerformanceIngressGreenFrameCount_Type()
)
mefServicePerformanceIngressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenFrameCount.setUnits("Ethernet frames")
_MefServicePerformanceIngressYellowFrameCount_Type = Counter64
_MefServicePerformanceIngressYellowFrameCount_Object = MibTableColumn
mefServicePerformanceIngressYellowFrameCount = _MefServicePerformanceIngressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 2),
    _MefServicePerformanceIngressYellowFrameCount_Type()
)
mefServicePerformanceIngressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowFrameCount.setUnits("Ethernet frames")
_MefServicePerformanceIngressRedFrameCount_Type = Counter64
_MefServicePerformanceIngressRedFrameCount_Object = MibTableColumn
mefServicePerformanceIngressRedFrameCount = _MefServicePerformanceIngressRedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 3),
    _MefServicePerformanceIngressRedFrameCount_Type()
)
mefServicePerformanceIngressRedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressRedFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressRedFrameCount.setUnits("Ethernet frames")
_MefServicePerformanceIngressGreenOctets_Type = Counter64
_MefServicePerformanceIngressGreenOctets_Object = MibTableColumn
mefServicePerformanceIngressGreenOctets = _MefServicePerformanceIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 4),
    _MefServicePerformanceIngressGreenOctets_Type()
)
mefServicePerformanceIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenOctets.setUnits("octets")
_MefServicePerformanceIngressYellowOctets_Type = Counter64
_MefServicePerformanceIngressYellowOctets_Object = MibTableColumn
mefServicePerformanceIngressYellowOctets = _MefServicePerformanceIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 5),
    _MefServicePerformanceIngressYellowOctets_Type()
)
mefServicePerformanceIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowOctets.setUnits("octets")
_MefServicePerformanceIngressRedOctets_Type = Counter64
_MefServicePerformanceIngressRedOctets_Object = MibTableColumn
mefServicePerformanceIngressRedOctets = _MefServicePerformanceIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 6),
    _MefServicePerformanceIngressRedOctets_Type()
)
mefServicePerformanceIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressRedOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressRedOctets.setUnits("octets")
_MefServicePerformanceIngressGreenFrameDiscards_Type = Counter64
_MefServicePerformanceIngressGreenFrameDiscards_Object = MibTableColumn
mefServicePerformanceIngressGreenFrameDiscards = _MefServicePerformanceIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 7),
    _MefServicePerformanceIngressGreenFrameDiscards_Type()
)
mefServicePerformanceIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenFrameDiscards.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenFrameDiscards.setUnits("Ethernet frames")
_MefServicePerformanceIngressYellowFrameDiscards_Type = Counter64
_MefServicePerformanceIngressYellowFrameDiscards_Object = MibTableColumn
mefServicePerformanceIngressYellowFrameDiscards = _MefServicePerformanceIngressYellowFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 8),
    _MefServicePerformanceIngressYellowFrameDiscards_Type()
)
mefServicePerformanceIngressYellowFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowFrameDiscards.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowFrameDiscards.setUnits("Ethernet frames")
_MefServicePerformanceIngressGreenOctetsDiscards_Type = Counter64
_MefServicePerformanceIngressGreenOctetsDiscards_Object = MibTableColumn
mefServicePerformanceIngressGreenOctetsDiscards = _MefServicePerformanceIngressGreenOctetsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 9),
    _MefServicePerformanceIngressGreenOctetsDiscards_Type()
)
mefServicePerformanceIngressGreenOctetsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenOctetsDiscards.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressGreenOctetsDiscards.setUnits("octets")
_MefServicePerformanceIngressYellowOctetsDiscards_Type = Counter64
_MefServicePerformanceIngressYellowOctetsDiscards_Object = MibTableColumn
mefServicePerformanceIngressYellowOctetsDiscards = _MefServicePerformanceIngressYellowOctetsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 10),
    _MefServicePerformanceIngressYellowOctetsDiscards_Type()
)
mefServicePerformanceIngressYellowOctetsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowOctetsDiscards.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceIngressYellowOctetsDiscards.setUnits("octets")
_MefServicePerformanceEgressGreenFrameCount_Type = Counter64
_MefServicePerformanceEgressGreenFrameCount_Object = MibTableColumn
mefServicePerformanceEgressGreenFrameCount = _MefServicePerformanceEgressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 11),
    _MefServicePerformanceEgressGreenFrameCount_Type()
)
mefServicePerformanceEgressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressGreenFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressGreenFrameCount.setUnits("Ethernet frames")
_MefServicePerformanceEgressYellowFrameCount_Type = Counter64
_MefServicePerformanceEgressYellowFrameCount_Object = MibTableColumn
mefServicePerformanceEgressYellowFrameCount = _MefServicePerformanceEgressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 12),
    _MefServicePerformanceEgressYellowFrameCount_Type()
)
mefServicePerformanceEgressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressYellowFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressYellowFrameCount.setUnits("Ethernet frames")
_MefServicePerformanceEgressGreenOctets_Type = Counter64
_MefServicePerformanceEgressGreenOctets_Object = MibTableColumn
mefServicePerformanceEgressGreenOctets = _MefServicePerformanceEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 13),
    _MefServicePerformanceEgressGreenOctets_Type()
)
mefServicePerformanceEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressGreenOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressGreenOctets.setUnits("octets")
_MefServicePerformanceEgressYellowOctets_Type = Counter64
_MefServicePerformanceEgressYellowOctets_Object = MibTableColumn
mefServicePerformanceEgressYellowOctets = _MefServicePerformanceEgressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 4, 1, 14),
    _MefServicePerformanceEgressYellowOctets_Type()
)
mefServicePerformanceEgressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressYellowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mefServicePerformanceEgressYellowOctets.setUnits("octets")
_MefServiceCosAttributes_ObjectIdentity = ObjectIdentity
mefServiceCosAttributes = _MefServiceCosAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5)
)


class _MefServiceCosNextIndex_Type(Unsigned32):
    """Custom type mefServiceCosNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceCosNextIndex_Object = MibScalar
mefServiceCosNextIndex = _MefServiceCosNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 1),
    _MefServiceCosNextIndex_Type()
)
mefServiceCosNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceCosNextIndex.setStatus("current")
_MefServiceCosCfgTable_Object = MibTable
mefServiceCosCfgTable = _MefServiceCosCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mefServiceCosCfgTable.setStatus("current")
_MefServiceCosCfgEntry_Object = MibTableRow
mefServiceCosCfgEntry = _MefServiceCosCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1)
)
mefServiceCosCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceCosCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceCosCfgEntry.setStatus("current")
_MefServiceCosCfgIndex_Type = Unsigned32
_MefServiceCosCfgIndex_Object = MibTableColumn
mefServiceCosCfgIndex = _MefServiceCosCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 1),
    _MefServiceCosCfgIndex_Type()
)
mefServiceCosCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceCosCfgIndex.setStatus("current")
_MefServiceCosCfgIdentifier_Type = DisplayString
_MefServiceCosCfgIdentifier_Object = MibTableColumn
mefServiceCosCfgIdentifier = _MefServiceCosCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 2),
    _MefServiceCosCfgIdentifier_Type()
)
mefServiceCosCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgIdentifier.setStatus("current")


class _MefServiceCosCfgType_Type(Integer32):
    """Custom type mefServiceCosCfgType based on Integer32"""
    defaultValue = 3

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
        *(("dscp", 4),
          ("evc", 2),
          ("interface", 1),
          ("l2cp", 5),
          ("pcp", 3))
    )


_MefServiceCosCfgType_Type.__name__ = "Integer32"
_MefServiceCosCfgType_Object = MibTableColumn
mefServiceCosCfgType = _MefServiceCosCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 3),
    _MefServiceCosCfgType_Type()
)
mefServiceCosCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgType.setStatus("current")


class _MefServiceCosCfgIdentifierList_Type(MefServiceListType):
    """Custom type mefServiceCosCfgIdentifierList based on MefServiceListType"""
    defaultValue = OctetString("0:7")


_MefServiceCosCfgIdentifierList_Object = MibTableColumn
mefServiceCosCfgIdentifierList = _MefServiceCosCfgIdentifierList_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 4),
    _MefServiceCosCfgIdentifierList_Type()
)
mefServiceCosCfgIdentifierList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceCosCfgIdentifierList.setStatus("current")


class _MefServiceCosCfgMacAddress_Type(MacAddress):
    """Custom type mefServiceCosCfgMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_MefServiceCosCfgMacAddress_Object = MibTableColumn
mefServiceCosCfgMacAddress = _MefServiceCosCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 5),
    _MefServiceCosCfgMacAddress_Type()
)
mefServiceCosCfgMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgMacAddress.setStatus("current")


class _MefServiceCosCfgProtocol_Type(Unsigned32):
    """Custom type mefServiceCosCfgProtocol based on Unsigned32"""
    defaultValue = 0


_MefServiceCosCfgProtocol_Object = MibTableColumn
mefServiceCosCfgProtocol = _MefServiceCosCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 6),
    _MefServiceCosCfgProtocol_Type()
)
mefServiceCosCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgProtocol.setStatus("current")


class _MefServiceCosCfgSubType_Type(Unsigned32):
    """Custom type mefServiceCosCfgSubType based on Unsigned32"""
    defaultValue = 0


_MefServiceCosCfgSubType_Object = MibTableColumn
mefServiceCosCfgSubType = _MefServiceCosCfgSubType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 7),
    _MefServiceCosCfgSubType_Type()
)
mefServiceCosCfgSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgSubType.setStatus("current")
_MefServiceCosCfgRowStatus_Type = RowStatus
_MefServiceCosCfgRowStatus_Object = MibTableColumn
mefServiceCosCfgRowStatus = _MefServiceCosCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 8),
    _MefServiceCosCfgRowStatus_Type()
)
mefServiceCosCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgRowStatus.setStatus("current")
_MefServiceL2cpAttributes_ObjectIdentity = ObjectIdentity
mefServiceL2cpAttributes = _MefServiceL2cpAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6)
)


class _MefServiceL2cpGrpNextIndex_Type(Unsigned32):
    """Custom type mefServiceL2cpGrpNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceL2cpGrpNextIndex_Object = MibScalar
mefServiceL2cpGrpNextIndex = _MefServiceL2cpGrpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 1),
    _MefServiceL2cpGrpNextIndex_Type()
)
mefServiceL2cpGrpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceL2cpGrpNextIndex.setStatus("current")
_MefServiceL2cpGrpCfgTable_Object = MibTable
mefServiceL2cpGrpCfgTable = _MefServiceL2cpGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mefServiceL2cpGrpCfgTable.setStatus("current")
_MefServiceL2cpGrpCfgEntry_Object = MibTableRow
mefServiceL2cpGrpCfgEntry = _MefServiceL2cpGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 2, 1)
)
mefServiceL2cpGrpCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceL2cpGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceL2cpGrpCfgEntry.setStatus("current")
_MefServiceL2cpGrpCfgIndex_Type = Unsigned32
_MefServiceL2cpGrpCfgIndex_Object = MibTableColumn
mefServiceL2cpGrpCfgIndex = _MefServiceL2cpGrpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 2, 1, 1),
    _MefServiceL2cpGrpCfgIndex_Type()
)
mefServiceL2cpGrpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceL2cpGrpCfgIndex.setStatus("current")


class _MefServiceL2cpCfgNextIndex_Type(Unsigned32):
    """Custom type mefServiceL2cpCfgNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceL2cpCfgNextIndex_Object = MibTableColumn
mefServiceL2cpCfgNextIndex = _MefServiceL2cpCfgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 2, 1, 2),
    _MefServiceL2cpCfgNextIndex_Type()
)
mefServiceL2cpCfgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgNextIndex.setStatus("current")
_MefServiceL2cpGrpCfgRowStatus_Type = RowStatus
_MefServiceL2cpGrpCfgRowStatus_Object = MibTableColumn
mefServiceL2cpGrpCfgRowStatus = _MefServiceL2cpGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 2, 1, 3),
    _MefServiceL2cpGrpCfgRowStatus_Type()
)
mefServiceL2cpGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpGrpCfgRowStatus.setStatus("current")
_MefServiceL2cpCfgTable_Object = MibTable
mefServiceL2cpCfgTable = _MefServiceL2cpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    mefServiceL2cpCfgTable.setStatus("current")
_MefServiceL2cpCfgEntry_Object = MibTableRow
mefServiceL2cpCfgEntry = _MefServiceL2cpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1)
)
mefServiceL2cpCfgEntry.setIndexNames(
    (0, "MEF-UNI-EVC-MIB", "mefServiceL2cpGrpCfgIndex"),
    (0, "MEF-UNI-EVC-MIB", "mefServiceL2cpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceL2cpCfgEntry.setStatus("current")
_MefServiceL2cpCfgIndex_Type = Unsigned32
_MefServiceL2cpCfgIndex_Object = MibTableColumn
mefServiceL2cpCfgIndex = _MefServiceL2cpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 1),
    _MefServiceL2cpCfgIndex_Type()
)
mefServiceL2cpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgIndex.setStatus("current")


class _MefServiceL2cpCfgType_Type(Integer32):
    """Custom type mefServiceL2cpCfgType based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("passToEvc", 4),
          ("peer", 3),
          ("tunnel", 2))
    )


_MefServiceL2cpCfgType_Type.__name__ = "Integer32"
_MefServiceL2cpCfgType_Object = MibTableColumn
mefServiceL2cpCfgType = _MefServiceL2cpCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 2),
    _MefServiceL2cpCfgType_Type()
)
mefServiceL2cpCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgType.setStatus("current")


class _MefServiceL2cpCfgMatchScope_Type(Integer32):
    """Custom type mefServiceL2cpCfgMatchScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daPlusProtocol", 2),
          ("daPlusProtocolPlusSubtype", 3),
          ("destinationAddressOnly", 1))
    )


_MefServiceL2cpCfgMatchScope_Type.__name__ = "Integer32"
_MefServiceL2cpCfgMatchScope_Object = MibTableColumn
mefServiceL2cpCfgMatchScope = _MefServiceL2cpCfgMatchScope_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 3),
    _MefServiceL2cpCfgMatchScope_Type()
)
mefServiceL2cpCfgMatchScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgMatchScope.setStatus("current")


class _MefServiceL2cpCfgMacAddress_Type(MacAddress):
    """Custom type mefServiceL2cpCfgMacAddress based on MacAddress"""
    defaultHexValue = "0180C2000000"


_MefServiceL2cpCfgMacAddress_Object = MibTableColumn
mefServiceL2cpCfgMacAddress = _MefServiceL2cpCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 4),
    _MefServiceL2cpCfgMacAddress_Type()
)
mefServiceL2cpCfgMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgMacAddress.setStatus("current")


class _MefServiceL2cpCfgProtocol_Type(Unsigned32):
    """Custom type mefServiceL2cpCfgProtocol based on Unsigned32"""
    defaultValue = 0


_MefServiceL2cpCfgProtocol_Object = MibTableColumn
mefServiceL2cpCfgProtocol = _MefServiceL2cpCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 5),
    _MefServiceL2cpCfgProtocol_Type()
)
mefServiceL2cpCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgProtocol.setStatus("current")


class _MefServiceL2cpCfgSubType_Type(Unsigned32):
    """Custom type mefServiceL2cpCfgSubType based on Unsigned32"""
    defaultValue = 0


_MefServiceL2cpCfgSubType_Object = MibTableColumn
mefServiceL2cpCfgSubType = _MefServiceL2cpCfgSubType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 6),
    _MefServiceL2cpCfgSubType_Type()
)
mefServiceL2cpCfgSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgSubType.setStatus("current")
_MefServiceL2cpCfgRowStatus_Type = RowStatus
_MefServiceL2cpCfgRowStatus_Object = MibTableColumn
mefServiceL2cpCfgRowStatus = _MefServiceL2cpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6, 3, 1, 7),
    _MefServiceL2cpCfgRowStatus_Type()
)
mefServiceL2cpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgRowStatus.setStatus("current")
_MefServiceNotificationCfg_ObjectIdentity = ObjectIdentity
mefServiceNotificationCfg = _MefServiceNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 7)
)


class _MefServiceNotificationCfgAlarmEnable_Type(Bits):
    """Custom type mefServiceNotificationCfgAlarmEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("bServiceConfigurationAlarm", 0)
    )

_MefServiceNotificationCfgAlarmEnable_Type.__name__ = "Bits"
_MefServiceNotificationCfgAlarmEnable_Object = MibScalar
mefServiceNotificationCfgAlarmEnable = _MefServiceNotificationCfgAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 7, 1),
    _MefServiceNotificationCfgAlarmEnable_Type()
)
mefServiceNotificationCfgAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceNotificationCfgAlarmEnable.setStatus("current")
_MefServiceNotificationObj_ObjectIdentity = ObjectIdentity
mefServiceNotificationObj = _MefServiceNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 8)
)
_MefServiceNotificationObjDateAndTime_Type = DateAndTime
_MefServiceNotificationObjDateAndTime_Object = MibScalar
mefServiceNotificationObjDateAndTime = _MefServiceNotificationObjDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 8, 1),
    _MefServiceNotificationObjDateAndTime_Type()
)
mefServiceNotificationObjDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefServiceNotificationObjDateAndTime.setStatus("current")


class _MefServiceNotificationConfigurationChangeType_Type(Integer32):
    """Custom type mefServiceNotificationConfigurationChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("entryAdded", 1),
          ("entryDeleted", 2),
          ("entryModified", 3))
    )


_MefServiceNotificationConfigurationChangeType_Type.__name__ = "Integer32"
_MefServiceNotificationConfigurationChangeType_Object = MibScalar
mefServiceNotificationConfigurationChangeType = _MefServiceNotificationConfigurationChangeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 8, 2),
    _MefServiceNotificationConfigurationChangeType_Type()
)
mefServiceNotificationConfigurationChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefServiceNotificationConfigurationChangeType.setStatus("current")
_MefServiceMibConformance_ObjectIdentity = ObjectIdentity
mefServiceMibConformance = _MefServiceMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2)
)
_MefServiceUniEvcMibCompliances_ObjectIdentity = ObjectIdentity
mefServiceUniEvcMibCompliances = _MefServiceUniEvcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 1)
)
_MefServiceUniEvcMibGroups_ObjectIdentity = ObjectIdentity
mefServiceUniEvcMibGroups = _MefServiceUniEvcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2)
)

# Managed Objects groups

mefServiceInterfaceMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 1)
)
mefServiceInterfaceMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgType"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgFrameFormat"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgIngressBwpGrpIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgEgressBwpGrpIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceCfgL2cpGrpIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatusType"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatusMaxVc"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatusMaxEndPointPerVc"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressUndersized"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressOversized"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressFragments"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressCrcAlignment"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressInvalidVid"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressOctets"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressUnicast"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressMulticast"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsIngressBroadcast"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsEgressOctets"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsEgressUnicast"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsEgressMulticast"),
        ("MEF-UNI-EVC-MIB", "mefServiceInterfaceStatisticsEgressBroadcast"))
)
if mibBuilder.loadTexts:
    mefServiceInterfaceMandatoryGroup.setStatus("current")

mefServiceUniMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 2)
)
mefServiceUniMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceUniCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceUniCfgBundlingMultiplex"),
        ("MEF-UNI-EVC-MIB", "mefServiceUniCfgCeVidUntagged"),
        ("MEF-UNI-EVC-MIB", "mefServiceUniCfgCePriorityUntagged"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcPerUniCfgServiceType"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcPerUniCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcPerUniCfgCeVlanMap"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcPerUniCfgIngressBwpGrpIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcPerUniCfgEgressBwpGrpIndex"))
)
if mibBuilder.loadTexts:
    mefServiceUniMandatoryGroup.setStatus("current")

mefServiceEvcMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 3)
)
mefServiceEvcMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceEvcNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgServiceType"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgMtuSize"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgCevlanIdPreservation"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgCevlanCosPreservation"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgL2cpGrpIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgAdminState"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgRowStatus"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcUniCfgType"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcUniCfgRowStatus"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcStatusMaxMtuSize"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcStatusMaxNumUni"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcStatusOperationalState"))
)
if mibBuilder.loadTexts:
    mefServiceEvcMandatoryGroup.setStatus("current")

mefServiceEvcOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 4)
)
mefServiceEvcOptionalGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceEvcCfgUnicastDelivery"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgMulticastDelivery"),
        ("MEF-UNI-EVC-MIB", "mefServiceEvcCfgBroadcastDelivery"))
)
if mibBuilder.loadTexts:
    mefServiceEvcOptionalGroup.setStatus("current")

mefServiceBwpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 5)
)
mefServiceBwpMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceBwpGrpNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpGrpCfgRowStatus"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgCir"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgCbs"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgEir"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgEbs"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgCm"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgCf"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgCosIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgPerformanceEnable"),
        ("MEF-UNI-EVC-MIB", "mefServiceBwpCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceBwpMandatoryGroup.setStatus("current")

mefServiceCosMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 6)
)
mefServiceCosMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceCosNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgIdentifier"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgType"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgIdentifierList"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgMacAddress"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgProtocol"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgSubType"),
        ("MEF-UNI-EVC-MIB", "mefServiceCosCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceCosMandatoryGroup.setStatus("current")

mefServiceL2cpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 7)
)
mefServiceL2cpMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceL2cpGrpNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgNextIndex"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpGrpCfgRowStatus"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgType"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgMatchScope"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgMacAddress"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgProtocol"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgSubType"),
        ("MEF-UNI-EVC-MIB", "mefServiceL2cpCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceL2cpMandatoryGroup.setStatus("current")

mefServicePerformanceMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 8)
)
mefServicePerformanceMandatoryGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressGreenFrameCount"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressGreenOctets"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceEgressGreenFrameCount"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceEgressGreenOctets"))
)
if mibBuilder.loadTexts:
    mefServicePerformanceMandatoryGroup.setStatus("current")

mefServicePerformanceOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 9)
)
mefServicePerformanceOptionalGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressYellowFrameCount"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressRedFrameCount"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressYellowOctets"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressRedOctets"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceEgressYellowFrameCount"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceEgressYellowOctets"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressGreenFrameDiscards"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressYellowFrameDiscards"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressGreenOctetsDiscards"),
        ("MEF-UNI-EVC-MIB", "mefServicePerformanceIngressYellowOctetsDiscards"))
)
if mibBuilder.loadTexts:
    mefServicePerformanceOptionalGroup.setStatus("current")

mefServiceNotificationObjOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 10)
)
mefServiceNotificationObjOptionalGroup.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceNotificationCfgAlarmEnable"),
        ("MEF-UNI-EVC-MIB", "mefServiceNotificationObjDateAndTime"),
        ("MEF-UNI-EVC-MIB", "mefServiceNotificationConfigurationChangeType"))
)
if mibBuilder.loadTexts:
    mefServiceNotificationObjOptionalGroup.setStatus("current")


# Notification objects

mefServiceConfigurationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 0, 1)
)
mefServiceConfigurationAlarm.setObjects(
      *(("MEF-UNI-EVC-MIB", "mefServiceNotificationObjDateAndTime"),
        ("MEF-UNI-EVC-MIB", "mefServiceNotificationConfigurationChangeType"))
)
if mibBuilder.loadTexts:
    mefServiceConfigurationAlarm.setStatus(
        "current"
    )


# Notifications groups

mefServiceNotificationsOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 11)
)
mefServiceNotificationsOptionalGroup.setObjects(
    ("MEF-UNI-EVC-MIB", "mefServiceConfigurationAlarm")
)
if mibBuilder.loadTexts:
    mefServiceNotificationsOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mefServiceUniMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mefServiceUniMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-UNI-EVC-MIB",
    **{"MefServicePreservationType": MefServicePreservationType,
       "MefServiceDeliveryType": MefServiceDeliveryType,
       "MefServiceInterfaceType": MefServiceInterfaceType,
       "MefServiceListType": MefServiceListType,
       "mefUniEvcMib": mefUniEvcMib,
       "mefServiceNotifications": mefServiceNotifications,
       "mefServiceConfigurationAlarm": mefServiceConfigurationAlarm,
       "mefServiceObjects": mefServiceObjects,
       "mefServiceInterfaceAttributes": mefServiceInterfaceAttributes,
       "mefServiceInterfaceCfgTable": mefServiceInterfaceCfgTable,
       "mefServiceInterfaceCfgEntry": mefServiceInterfaceCfgEntry,
       "mefServiceInterfaceCfgType": mefServiceInterfaceCfgType,
       "mefServiceInterfaceCfgIdentifier": mefServiceInterfaceCfgIdentifier,
       "mefServiceInterfaceCfgFrameFormat": mefServiceInterfaceCfgFrameFormat,
       "mefServiceInterfaceCfgIngressBwpGrpIndex": mefServiceInterfaceCfgIngressBwpGrpIndex,
       "mefServiceInterfaceCfgEgressBwpGrpIndex": mefServiceInterfaceCfgEgressBwpGrpIndex,
       "mefServiceInterfaceCfgL2cpGrpIndex": mefServiceInterfaceCfgL2cpGrpIndex,
       "mefServiceInterfaceStatusTable": mefServiceInterfaceStatusTable,
       "mefServiceInterfaceStatusEntry": mefServiceInterfaceStatusEntry,
       "mefServiceInterfaceStatusType": mefServiceInterfaceStatusType,
       "mefServiceInterfaceStatusMaxVc": mefServiceInterfaceStatusMaxVc,
       "mefServiceInterfaceStatusMaxEndPointPerVc": mefServiceInterfaceStatusMaxEndPointPerVc,
       "mefServiceInterfaceStatisticsTable": mefServiceInterfaceStatisticsTable,
       "mefServiceInterfaceStatisticsEntry": mefServiceInterfaceStatisticsEntry,
       "mefServiceInterfaceStatisticsIngressUndersized": mefServiceInterfaceStatisticsIngressUndersized,
       "mefServiceInterfaceStatisticsIngressOversized": mefServiceInterfaceStatisticsIngressOversized,
       "mefServiceInterfaceStatisticsIngressFragments": mefServiceInterfaceStatisticsIngressFragments,
       "mefServiceInterfaceStatisticsIngressCrcAlignment": mefServiceInterfaceStatisticsIngressCrcAlignment,
       "mefServiceInterfaceStatisticsIngressInvalidVid": mefServiceInterfaceStatisticsIngressInvalidVid,
       "mefServiceInterfaceStatisticsIngressOctets": mefServiceInterfaceStatisticsIngressOctets,
       "mefServiceInterfaceStatisticsIngressUnicast": mefServiceInterfaceStatisticsIngressUnicast,
       "mefServiceInterfaceStatisticsIngressMulticast": mefServiceInterfaceStatisticsIngressMulticast,
       "mefServiceInterfaceStatisticsIngressBroadcast": mefServiceInterfaceStatisticsIngressBroadcast,
       "mefServiceInterfaceStatisticsEgressOctets": mefServiceInterfaceStatisticsEgressOctets,
       "mefServiceInterfaceStatisticsEgressUnicast": mefServiceInterfaceStatisticsEgressUnicast,
       "mefServiceInterfaceStatisticsEgressMulticast": mefServiceInterfaceStatisticsEgressMulticast,
       "mefServiceInterfaceStatisticsEgressBroadcast": mefServiceInterfaceStatisticsEgressBroadcast,
       "mefServiceUniAttributes": mefServiceUniAttributes,
       "mefServiceUniCfgTable": mefServiceUniCfgTable,
       "mefServiceUniCfgEntry": mefServiceUniCfgEntry,
       "mefServiceUniCfgIdentifier": mefServiceUniCfgIdentifier,
       "mefServiceUniCfgBundlingMultiplex": mefServiceUniCfgBundlingMultiplex,
       "mefServiceUniCfgCeVidUntagged": mefServiceUniCfgCeVidUntagged,
       "mefServiceUniCfgCePriorityUntagged": mefServiceUniCfgCePriorityUntagged,
       "mefServiceEvcPerUniCfgTable": mefServiceEvcPerUniCfgTable,
       "mefServiceEvcPerUniCfgEntry": mefServiceEvcPerUniCfgEntry,
       "mefServiceEvcPerUniCfgServiceType": mefServiceEvcPerUniCfgServiceType,
       "mefServiceEvcPerUniCfgIdentifier": mefServiceEvcPerUniCfgIdentifier,
       "mefServiceEvcPerUniCfgCeVlanMap": mefServiceEvcPerUniCfgCeVlanMap,
       "mefServiceEvcPerUniCfgIngressBwpGrpIndex": mefServiceEvcPerUniCfgIngressBwpGrpIndex,
       "mefServiceEvcPerUniCfgEgressBwpGrpIndex": mefServiceEvcPerUniCfgEgressBwpGrpIndex,
       "mefServiceEvcAttributes": mefServiceEvcAttributes,
       "mefServiceEvcNextIndex": mefServiceEvcNextIndex,
       "mefServiceEvcCfgTable": mefServiceEvcCfgTable,
       "mefServiceEvcCfgEntry": mefServiceEvcCfgEntry,
       "mefServiceEvcCfgIndex": mefServiceEvcCfgIndex,
       "mefServiceEvcCfgIdentifier": mefServiceEvcCfgIdentifier,
       "mefServiceEvcCfgServiceType": mefServiceEvcCfgServiceType,
       "mefServiceEvcCfgMtuSize": mefServiceEvcCfgMtuSize,
       "mefServiceEvcCfgCevlanIdPreservation": mefServiceEvcCfgCevlanIdPreservation,
       "mefServiceEvcCfgCevlanCosPreservation": mefServiceEvcCfgCevlanCosPreservation,
       "mefServiceEvcCfgUnicastDelivery": mefServiceEvcCfgUnicastDelivery,
       "mefServiceEvcCfgMulticastDelivery": mefServiceEvcCfgMulticastDelivery,
       "mefServiceEvcCfgBroadcastDelivery": mefServiceEvcCfgBroadcastDelivery,
       "mefServiceEvcCfgL2cpGrpIndex": mefServiceEvcCfgL2cpGrpIndex,
       "mefServiceEvcCfgAdminState": mefServiceEvcCfgAdminState,
       "mefServiceEvcCfgRowStatus": mefServiceEvcCfgRowStatus,
       "mefServiceEvcUniCfgTable": mefServiceEvcUniCfgTable,
       "mefServiceEvcUniCfgEntry": mefServiceEvcUniCfgEntry,
       "mefServiceEvcUniCfgType": mefServiceEvcUniCfgType,
       "mefServiceEvcUniCfgRowStatus": mefServiceEvcUniCfgRowStatus,
       "mefServiceEvcStatusTable": mefServiceEvcStatusTable,
       "mefServiceEvcStatusEntry": mefServiceEvcStatusEntry,
       "mefServiceEvcStatusMaxMtuSize": mefServiceEvcStatusMaxMtuSize,
       "mefServiceEvcStatusMaxNumUni": mefServiceEvcStatusMaxNumUni,
       "mefServiceEvcStatusOperationalState": mefServiceEvcStatusOperationalState,
       "mefServiceBwpAttributes": mefServiceBwpAttributes,
       "mefServiceBwpGrpNextIndex": mefServiceBwpGrpNextIndex,
       "mefServiceBwpGrpCfgTable": mefServiceBwpGrpCfgTable,
       "mefServiceBwpGrpCfgEntry": mefServiceBwpGrpCfgEntry,
       "mefServiceBwpGrpCfgIndex": mefServiceBwpGrpCfgIndex,
       "mefServiceBwpCfgNextIndex": mefServiceBwpCfgNextIndex,
       "mefServiceBwpGrpCfgRowStatus": mefServiceBwpGrpCfgRowStatus,
       "mefServiceBwpCfgTable": mefServiceBwpCfgTable,
       "mefServiceBwpCfgEntry": mefServiceBwpCfgEntry,
       "mefServiceBwpCfgIndex": mefServiceBwpCfgIndex,
       "mefServiceBwpCfgIdentifier": mefServiceBwpCfgIdentifier,
       "mefServiceBwpCfgCir": mefServiceBwpCfgCir,
       "mefServiceBwpCfgCbs": mefServiceBwpCfgCbs,
       "mefServiceBwpCfgEir": mefServiceBwpCfgEir,
       "mefServiceBwpCfgEbs": mefServiceBwpCfgEbs,
       "mefServiceBwpCfgCm": mefServiceBwpCfgCm,
       "mefServiceBwpCfgCf": mefServiceBwpCfgCf,
       "mefServiceBwpCfgCosIndex": mefServiceBwpCfgCosIndex,
       "mefServiceBwpCfgPerformanceEnable": mefServiceBwpCfgPerformanceEnable,
       "mefServiceBwpCfgRowStatus": mefServiceBwpCfgRowStatus,
       "mefServicePerformanceTable": mefServicePerformanceTable,
       "mefServicePerformanceEntry": mefServicePerformanceEntry,
       "mefServicePerformanceIngressGreenFrameCount": mefServicePerformanceIngressGreenFrameCount,
       "mefServicePerformanceIngressYellowFrameCount": mefServicePerformanceIngressYellowFrameCount,
       "mefServicePerformanceIngressRedFrameCount": mefServicePerformanceIngressRedFrameCount,
       "mefServicePerformanceIngressGreenOctets": mefServicePerformanceIngressGreenOctets,
       "mefServicePerformanceIngressYellowOctets": mefServicePerformanceIngressYellowOctets,
       "mefServicePerformanceIngressRedOctets": mefServicePerformanceIngressRedOctets,
       "mefServicePerformanceIngressGreenFrameDiscards": mefServicePerformanceIngressGreenFrameDiscards,
       "mefServicePerformanceIngressYellowFrameDiscards": mefServicePerformanceIngressYellowFrameDiscards,
       "mefServicePerformanceIngressGreenOctetsDiscards": mefServicePerformanceIngressGreenOctetsDiscards,
       "mefServicePerformanceIngressYellowOctetsDiscards": mefServicePerformanceIngressYellowOctetsDiscards,
       "mefServicePerformanceEgressGreenFrameCount": mefServicePerformanceEgressGreenFrameCount,
       "mefServicePerformanceEgressYellowFrameCount": mefServicePerformanceEgressYellowFrameCount,
       "mefServicePerformanceEgressGreenOctets": mefServicePerformanceEgressGreenOctets,
       "mefServicePerformanceEgressYellowOctets": mefServicePerformanceEgressYellowOctets,
       "mefServiceCosAttributes": mefServiceCosAttributes,
       "mefServiceCosNextIndex": mefServiceCosNextIndex,
       "mefServiceCosCfgTable": mefServiceCosCfgTable,
       "mefServiceCosCfgEntry": mefServiceCosCfgEntry,
       "mefServiceCosCfgIndex": mefServiceCosCfgIndex,
       "mefServiceCosCfgIdentifier": mefServiceCosCfgIdentifier,
       "mefServiceCosCfgType": mefServiceCosCfgType,
       "mefServiceCosCfgIdentifierList": mefServiceCosCfgIdentifierList,
       "mefServiceCosCfgMacAddress": mefServiceCosCfgMacAddress,
       "mefServiceCosCfgProtocol": mefServiceCosCfgProtocol,
       "mefServiceCosCfgSubType": mefServiceCosCfgSubType,
       "mefServiceCosCfgRowStatus": mefServiceCosCfgRowStatus,
       "mefServiceL2cpAttributes": mefServiceL2cpAttributes,
       "mefServiceL2cpGrpNextIndex": mefServiceL2cpGrpNextIndex,
       "mefServiceL2cpGrpCfgTable": mefServiceL2cpGrpCfgTable,
       "mefServiceL2cpGrpCfgEntry": mefServiceL2cpGrpCfgEntry,
       "mefServiceL2cpGrpCfgIndex": mefServiceL2cpGrpCfgIndex,
       "mefServiceL2cpCfgNextIndex": mefServiceL2cpCfgNextIndex,
       "mefServiceL2cpGrpCfgRowStatus": mefServiceL2cpGrpCfgRowStatus,
       "mefServiceL2cpCfgTable": mefServiceL2cpCfgTable,
       "mefServiceL2cpCfgEntry": mefServiceL2cpCfgEntry,
       "mefServiceL2cpCfgIndex": mefServiceL2cpCfgIndex,
       "mefServiceL2cpCfgType": mefServiceL2cpCfgType,
       "mefServiceL2cpCfgMatchScope": mefServiceL2cpCfgMatchScope,
       "mefServiceL2cpCfgMacAddress": mefServiceL2cpCfgMacAddress,
       "mefServiceL2cpCfgProtocol": mefServiceL2cpCfgProtocol,
       "mefServiceL2cpCfgSubType": mefServiceL2cpCfgSubType,
       "mefServiceL2cpCfgRowStatus": mefServiceL2cpCfgRowStatus,
       "mefServiceNotificationCfg": mefServiceNotificationCfg,
       "mefServiceNotificationCfgAlarmEnable": mefServiceNotificationCfgAlarmEnable,
       "mefServiceNotificationObj": mefServiceNotificationObj,
       "mefServiceNotificationObjDateAndTime": mefServiceNotificationObjDateAndTime,
       "mefServiceNotificationConfigurationChangeType": mefServiceNotificationConfigurationChangeType,
       "mefServiceMibConformance": mefServiceMibConformance,
       "mefServiceUniEvcMibCompliances": mefServiceUniEvcMibCompliances,
       "mefServiceUniMibCompliance": mefServiceUniMibCompliance,
       "mefServiceUniEvcMibGroups": mefServiceUniEvcMibGroups,
       "mefServiceInterfaceMandatoryGroup": mefServiceInterfaceMandatoryGroup,
       "mefServiceUniMandatoryGroup": mefServiceUniMandatoryGroup,
       "mefServiceEvcMandatoryGroup": mefServiceEvcMandatoryGroup,
       "mefServiceEvcOptionalGroup": mefServiceEvcOptionalGroup,
       "mefServiceBwpMandatoryGroup": mefServiceBwpMandatoryGroup,
       "mefServiceCosMandatoryGroup": mefServiceCosMandatoryGroup,
       "mefServiceL2cpMandatoryGroup": mefServiceL2cpMandatoryGroup,
       "mefServicePerformanceMandatoryGroup": mefServicePerformanceMandatoryGroup,
       "mefServicePerformanceOptionalGroup": mefServicePerformanceOptionalGroup,
       "mefServiceNotificationObjOptionalGroup": mefServiceNotificationObjOptionalGroup,
       "mefServiceNotificationsOptionalGroup": mefServiceNotificationsOptionalGroup}
)
