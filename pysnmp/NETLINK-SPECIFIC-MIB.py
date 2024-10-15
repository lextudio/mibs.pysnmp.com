# SNMP MIB module (NETLINK-SPECIFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETLINK-SPECIFIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:37 2024
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
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY


# Types definitions



class NlSubscriberAddress(OctetString):
    """Custom type NlSubscriberAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnaDLC_ObjectIdentity = ObjectIdentity
snaDLC = _SnaDLC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41)
)
_Sdlc_ObjectIdentity = ObjectIdentity
sdlc = _Sdlc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1)
)
_SdlcLSGroup_ObjectIdentity = ObjectIdentity
sdlcLSGroup = _SdlcLSGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 2)
)
_SdlcLSAdminTable_ObjectIdentity = ObjectIdentity
sdlcLSAdminTable = _SdlcLSAdminTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1)
)
_SdlcLSAdminEntry_ObjectIdentity = ObjectIdentity
sdlcLSAdminEntry = _SdlcLSAdminEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1)
)


class _SdlcLSAddress_Type(Integer32):
    """Custom type sdlcLSAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdlcLSAddress_Type.__name__ = "Integer32"
_SdlcLSAddress_Object = MibScalar
sdlcLSAddress = _SdlcLSAddress_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 1),
    _SdlcLSAddress_Type()
)
sdlcLSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAddress.setStatus("mandatory")
_Netlink_ObjectIdentity = ObjectIdentity
netlink = _Netlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 6)
)
_Netstat_ObjectIdentity = ObjectIdentity
netstat = _Netstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 6, 1)
)
_NsMaxNeigh_Type = Integer32
_NsMaxNeigh_Object = MibScalar
nsMaxNeigh = _NsMaxNeigh_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 1),
    _NsMaxNeigh_Type()
)
nsMaxNeigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsMaxNeigh.setStatus("mandatory")
_NsThisNode_Type = Integer32
_NsThisNode_Object = MibScalar
nsThisNode = _NsThisNode_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 2),
    _NsThisNode_Type()
)
nsThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsThisNode.setStatus("mandatory")
_NsNodTable_Object = MibTable
nsNodTable = _NsNodTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 3)
)
if mibBuilder.loadTexts:
    nsNodTable.setStatus("mandatory")
_NsEntry_Object = MibTableRow
nsEntry = _NsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 3, 1)
)
nsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nsNodNum"),
)
if mibBuilder.loadTexts:
    nsEntry.setStatus("mandatory")
_NsNodNum_Type = Integer32
_NsNodNum_Object = MibTableColumn
nsNodNum = _NsNodNum_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 3, 1, 1),
    _NsNodNum_Type()
)
nsNodNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNodNum.setStatus("mandatory")
_NsStatus_Type = Integer32
_NsStatus_Object = MibTableColumn
nsStatus = _NsStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 3, 1, 2),
    _NsStatus_Type()
)
nsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsStatus.setStatus("mandatory")
_NsNumNeigh_Type = Integer32
_NsNumNeigh_Object = MibTableColumn
nsNumNeigh = _NsNumNeigh_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 3, 1, 3),
    _NsNumNeigh_Type()
)
nsNumNeigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumNeigh.setStatus("mandatory")
_NsNeighTable_Object = MibTable
nsNeighTable = _NsNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 4)
)
if mibBuilder.loadTexts:
    nsNeighTable.setStatus("mandatory")
_NsNeighEntry_Object = MibTableRow
nsNeighEntry = _NsNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 4, 1)
)
nsNeighEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nsNTNode"),
    (0, "NETLINK-SPECIFIC-MIB", "nsNTNeigh"),
)
if mibBuilder.loadTexts:
    nsNeighEntry.setStatus("mandatory")
_NsNTNode_Type = Integer32
_NsNTNode_Object = MibTableColumn
nsNTNode = _NsNTNode_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 4, 1, 1),
    _NsNTNode_Type()
)
nsNTNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNTNode.setStatus("mandatory")
_NsNTNeigh_Type = Integer32
_NsNTNeigh_Object = MibTableColumn
nsNTNeigh = _NsNTNeigh_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 4, 1, 2),
    _NsNTNeigh_Type()
)
nsNTNeigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNTNeigh.setStatus("mandatory")


class _NsNTNeighStat_Type(Integer32):
    """Custom type nsNTNeighStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("notConnected", 1))
    )


_NsNTNeighStat_Type.__name__ = "Integer32"
_NsNTNeighStat_Object = MibTableColumn
nsNTNeighStat = _NsNTNeighStat_Object(
    (1, 3, 6, 1, 4, 1, 173, 6, 1, 4, 1, 3),
    _NsNTNeighStat_Type()
)
nsNTNeighStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNTNeighStat.setStatus("mandatory")
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7)
)
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 1)
)
_NodeCfgTable_ObjectIdentity = ObjectIdentity
nodeCfgTable = _NodeCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 1)
)
_NodeAlmTable_ObjectIdentity = ObjectIdentity
nodeAlmTable = _NodeAlmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 2)
)
_NodeSNMPGroup_ObjectIdentity = ObjectIdentity
nodeSNMPGroup = _NodeSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3)
)


class _NodeModel_Type(Integer32):
    """Custom type nodeModel based on Integer32"""
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
        *(("frx4000", 6),
          ("highavail", 4),
          ("model1", 1),
          ("model2", 2),
          ("netfrad", 5),
          ("rackmount", 3),
          ("ss1800", 7))
    )


_NodeModel_Type.__name__ = "Integer32"
_NodeModel_Object = MibScalar
nodeModel = _NodeModel_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 1),
    _NodeModel_Type()
)
nodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeModel.setStatus("mandatory")
_NodeTrapText_Type = DisplayString
_NodeTrapText_Object = MibScalar
nodeTrapText = _NodeTrapText_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 2),
    _NodeTrapText_Type()
)
nodeTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTrapText.setStatus("mandatory")
_NodeTrapAdrTable_Object = MibTable
nodeTrapAdrTable = _NodeTrapAdrTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nodeTrapAdrTable.setStatus("mandatory")
_TpAdrEntry_Object = MibTableRow
tpAdrEntry = _TpAdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3, 1)
)
tpAdrEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "tpAdrIdx"),
)
if mibBuilder.loadTexts:
    tpAdrEntry.setStatus("mandatory")
_TpAdrIdx_Type = Integer32
_TpAdrIdx_Object = MibTableColumn
tpAdrIdx = _TpAdrIdx_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3, 1, 1),
    _TpAdrIdx_Type()
)
tpAdrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAdrIdx.setStatus("mandatory")
_TpAddress_Type = IpAddress
_TpAddress_Object = MibTableColumn
tpAddress = _TpAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3, 1, 2),
    _TpAddress_Type()
)
tpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpAddress.setStatus("mandatory")


class _TpAdrFlag_Type(Integer32):
    """Custom type tpAdrFlag based on Integer32"""
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
          ("disableTraps", 1),
          ("enableTraps", 2))
    )


_TpAdrFlag_Type.__name__ = "Integer32"
_TpAdrFlag_Object = MibTableColumn
tpAdrFlag = _TpAdrFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3, 1, 3),
    _TpAdrFlag_Type()
)
tpAdrFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpAdrFlag.setStatus("mandatory")


class _TpAdrSLev_Type(Integer32):
    """Custom type tpAdrSLev based on Integer32"""
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
        *(("critical", 1),
          ("informational", 4),
          ("major", 2),
          ("minor", 3))
    )


_TpAdrSLev_Type.__name__ = "Integer32"
_TpAdrSLev_Object = MibTableColumn
tpAdrSLev = _TpAdrSLev_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 3, 3, 1, 4),
    _TpAdrSLev_Type()
)
tpAdrSLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpAdrSLev.setStatus("mandatory")
_NodeBagTable_ObjectIdentity = ObjectIdentity
nodeBagTable = _NodeBagTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 1, 4)
)
_Hwcard_ObjectIdentity = ObjectIdentity
hwcard = _Hwcard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 2)
)
_RlpMaxProtos_Type = Integer32
_RlpMaxProtos_Object = MibScalar
rlpMaxProtos = _RlpMaxProtos_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 1),
    _RlpMaxProtos_Type()
)
rlpMaxProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpMaxProtos.setStatus("mandatory")
_RlpConfigTable_Object = MibTable
rlpConfigTable = _RlpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2)
)
if mibBuilder.loadTexts:
    rlpConfigTable.setStatus("mandatory")
_RlpEntry_Object = MibTableRow
rlpEntry = _RlpEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1)
)
rlpEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "rlpIndex"),
)
if mibBuilder.loadTexts:
    rlpEntry.setStatus("mandatory")
_RlpIndex_Type = Integer32
_RlpIndex_Object = MibTableColumn
rlpIndex = _RlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 1),
    _RlpIndex_Type()
)
rlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpIndex.setStatus("mandatory")


class _RlpStatus_Type(Integer32):
    """Custom type rlpStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("failed", 7),
          ("installed", 1),
          ("ipl-failed", 5),
          ("ipl-in-progress", 6),
          ("load-failed", 3),
          ("loading", 4),
          ("operational", 8),
          ("power-off", 9),
          ("power-on", 10))
    )


_RlpStatus_Type.__name__ = "Integer32"
_RlpStatus_Object = MibTableColumn
rlpStatus = _RlpStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 2),
    _RlpStatus_Type()
)
rlpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatus.setStatus("mandatory")
_RlpMemorySize_Type = Integer32
_RlpMemorySize_Object = MibTableColumn
rlpMemorySize = _RlpMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 3),
    _RlpMemorySize_Type()
)
rlpMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpMemorySize.setStatus("mandatory")


class _RlpLIC1Type_Type(Integer32):
    """Custom type rlpLIC1Type based on Integer32"""
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
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("e1", 11),
          ("hs-rs232", 5),
          ("none", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs449", 7),
          ("t1", 10),
          ("universal", 8),
          ("v35", 4),
          ("voice", 13),
          ("x21", 6))
    )


_RlpLIC1Type_Type.__name__ = "Integer32"
_RlpLIC1Type_Object = MibTableColumn
rlpLIC1Type = _RlpLIC1Type_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 4),
    _RlpLIC1Type_Type()
)
rlpLIC1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpLIC1Type.setStatus("mandatory")


class _RlpLIC2Type_Type(Integer32):
    """Custom type rlpLIC2Type based on Integer32"""
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
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("e1", 11),
          ("hs-rs232", 5),
          ("none", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs449", 7),
          ("t1", 10),
          ("universal", 8),
          ("v35", 4),
          ("voice", 13),
          ("x21", 6))
    )


_RlpLIC2Type_Type.__name__ = "Integer32"
_RlpLIC2Type_Object = MibTableColumn
rlpLIC2Type = _RlpLIC2Type_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 5),
    _RlpLIC2Type_Type()
)
rlpLIC2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpLIC2Type.setStatus("mandatory")
_RlpProtocol_Type = OctetString
_RlpProtocol_Object = MibTableColumn
rlpProtocol = _RlpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 6),
    _RlpProtocol_Type()
)
rlpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlpProtocol.setStatus("mandatory")


class _RlpGroupNumber_Type(Integer32):
    """Custom type rlpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RlpGroupNumber_Type.__name__ = "Integer32"
_RlpGroupNumber_Object = MibTableColumn
rlpGroupNumber = _RlpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 7),
    _RlpGroupNumber_Type()
)
rlpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpGroupNumber.setStatus("mandatory")


class _RlpGroupResponsibility_Type(Integer32):
    """Custom type rlpGroupResponsibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_RlpGroupResponsibility_Type.__name__ = "Integer32"
_RlpGroupResponsibility_Object = MibTableColumn
rlpGroupResponsibility = _RlpGroupResponsibility_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 2, 2, 1, 8),
    _RlpGroupResponsibility_Type()
)
rlpGroupResponsibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpGroupResponsibility.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3)
)
_PortX25Group_ObjectIdentity = ObjectIdentity
portX25Group = _PortX25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1)
)
_PortPhyX25AdminTable_Object = MibTable
portPhyX25AdminTable = _PortPhyX25AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    portPhyX25AdminTable.setStatus("mandatory")
_PortPhyX25AdminEntry_Object = MibTableRow
portPhyX25AdminEntry = _PortPhyX25AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1)
)
portPhyX25AdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portPhyX25AdminEntry.setStatus("mandatory")


class _PortPhyX25AdminConnector_Type(Integer32):
    """Custom type portPhyX25AdminConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("e1", 11),
          ("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortPhyX25AdminConnector_Type.__name__ = "Integer32"
_PortPhyX25AdminConnector_Object = MibTableColumn
portPhyX25AdminConnector = _PortPhyX25AdminConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 1),
    _PortPhyX25AdminConnector_Type()
)
portPhyX25AdminConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminConnector.setStatus("mandatory")


class _PortPhyX25AdminSpeed_Type(Integer32):
    """Custom type portPhyX25AdminSpeed based on Integer32"""
    defaultValue = 64000


_PortPhyX25AdminSpeed_Object = MibTableColumn
portPhyX25AdminSpeed = _PortPhyX25AdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 2),
    _PortPhyX25AdminSpeed_Type()
)
portPhyX25AdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminSpeed.setStatus("mandatory")


class _PortPhyX25AdminGenerateClock_Type(Integer32):
    """Custom type portPhyX25AdminGenerateClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25AdminGenerateClock_Type.__name__ = "Integer32"
_PortPhyX25AdminGenerateClock_Object = MibTableColumn
portPhyX25AdminGenerateClock = _PortPhyX25AdminGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 3),
    _PortPhyX25AdminGenerateClock_Type()
)
portPhyX25AdminGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminGenerateClock.setStatus("mandatory")


class _PortPhyX25AdminRcvClockFromDTE_Type(Integer32):
    """Custom type portPhyX25AdminRcvClockFromDTE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25AdminRcvClockFromDTE_Type.__name__ = "Integer32"
_PortPhyX25AdminRcvClockFromDTE_Object = MibTableColumn
portPhyX25AdminRcvClockFromDTE = _PortPhyX25AdminRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 4),
    _PortPhyX25AdminRcvClockFromDTE_Type()
)
portPhyX25AdminRcvClockFromDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminRcvClockFromDTE.setStatus("mandatory")


class _PortPhyX25AdminDialOut_Type(Integer32):
    """Custom type portPhyX25AdminDialOut based on Integer32"""
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
        *(("dialIn", 2),
          ("dialOut", 3),
          ("none", 1))
    )


_PortPhyX25AdminDialOut_Type.__name__ = "Integer32"
_PortPhyX25AdminDialOut_Object = MibTableColumn
portPhyX25AdminDialOut = _PortPhyX25AdminDialOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 5),
    _PortPhyX25AdminDialOut_Type()
)
portPhyX25AdminDialOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminDialOut.setStatus("mandatory")


class _PortPhyX25AdminInactivityTimer_Type(Integer32):
    """Custom type portPhyX25AdminInactivityTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PortPhyX25AdminInactivityTimer_Type.__name__ = "Integer32"
_PortPhyX25AdminInactivityTimer_Object = MibTableColumn
portPhyX25AdminInactivityTimer = _PortPhyX25AdminInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 6),
    _PortPhyX25AdminInactivityTimer_Type()
)
portPhyX25AdminInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminInactivityTimer.setStatus("mandatory")


class _PortPhyX25AdminDisconnectTimer_Type(Integer32):
    """Custom type portPhyX25AdminDisconnectTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortPhyX25AdminDisconnectTimer_Type.__name__ = "Integer32"
_PortPhyX25AdminDisconnectTimer_Object = MibTableColumn
portPhyX25AdminDisconnectTimer = _PortPhyX25AdminDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 7),
    _PortPhyX25AdminDisconnectTimer_Type()
)
portPhyX25AdminDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminDisconnectTimer.setStatus("mandatory")


class _PortPhyX25AdminSetupTimer_Type(Integer32):
    """Custom type portPhyX25AdminSetupTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortPhyX25AdminSetupTimer_Type.__name__ = "Integer32"
_PortPhyX25AdminSetupTimer_Object = MibTableColumn
portPhyX25AdminSetupTimer = _PortPhyX25AdminSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 8),
    _PortPhyX25AdminSetupTimer_Type()
)
portPhyX25AdminSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminSetupTimer.setStatus("mandatory")


class _PortPhyX25AdminTrunkFlag_Type(Integer32):
    """Custom type portPhyX25AdminTrunkFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25AdminTrunkFlag_Type.__name__ = "Integer32"
_PortPhyX25AdminTrunkFlag_Object = MibTableColumn
portPhyX25AdminTrunkFlag = _PortPhyX25AdminTrunkFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 9),
    _PortPhyX25AdminTrunkFlag_Type()
)
portPhyX25AdminTrunkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminTrunkFlag.setStatus("mandatory")
_PortPhyX25AdminTrunkGroup_Type = OctetString
_PortPhyX25AdminTrunkGroup_Object = MibTableColumn
portPhyX25AdminTrunkGroup = _PortPhyX25AdminTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 10),
    _PortPhyX25AdminTrunkGroup_Type()
)
portPhyX25AdminTrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminTrunkGroup.setStatus("mandatory")
_PortPhyX25AdminRowStatus_Type = RowStatus
_PortPhyX25AdminRowStatus_Object = MibTableColumn
portPhyX25AdminRowStatus = _PortPhyX25AdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 1, 1, 11),
    _PortPhyX25AdminRowStatus_Type()
)
portPhyX25AdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhyX25AdminRowStatus.setStatus("mandatory")
_PortPhyX25OperTable_Object = MibTable
portPhyX25OperTable = _PortPhyX25OperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    portPhyX25OperTable.setStatus("mandatory")
_PortPhyX25OperEntry_Object = MibTableRow
portPhyX25OperEntry = _PortPhyX25OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1)
)
portPhyX25OperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portPhyX25OperEntry.setStatus("mandatory")


class _PortPhyX25OperConnector_Type(Integer32):
    """Custom type portPhyX25OperConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("e1", 11),
          ("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortPhyX25OperConnector_Type.__name__ = "Integer32"
_PortPhyX25OperConnector_Object = MibTableColumn
portPhyX25OperConnector = _PortPhyX25OperConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 1),
    _PortPhyX25OperConnector_Type()
)
portPhyX25OperConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperConnector.setStatus("mandatory")
_PortPhyX25OperSpeed_Type = Integer32
_PortPhyX25OperSpeed_Object = MibTableColumn
portPhyX25OperSpeed = _PortPhyX25OperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 2),
    _PortPhyX25OperSpeed_Type()
)
portPhyX25OperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperSpeed.setStatus("mandatory")


class _PortPhyX25OperGenerateClock_Type(Integer32):
    """Custom type portPhyX25OperGenerateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25OperGenerateClock_Type.__name__ = "Integer32"
_PortPhyX25OperGenerateClock_Object = MibTableColumn
portPhyX25OperGenerateClock = _PortPhyX25OperGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 3),
    _PortPhyX25OperGenerateClock_Type()
)
portPhyX25OperGenerateClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperGenerateClock.setStatus("mandatory")


class _PortPhyX25OperRcvClockFromDTE_Type(Integer32):
    """Custom type portPhyX25OperRcvClockFromDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25OperRcvClockFromDTE_Type.__name__ = "Integer32"
_PortPhyX25OperRcvClockFromDTE_Object = MibTableColumn
portPhyX25OperRcvClockFromDTE = _PortPhyX25OperRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 4),
    _PortPhyX25OperRcvClockFromDTE_Type()
)
portPhyX25OperRcvClockFromDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperRcvClockFromDTE.setStatus("mandatory")


class _PortPhyX25OperDialOut_Type(Integer32):
    """Custom type portPhyX25OperDialOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialIn", 2),
          ("dialOut", 3),
          ("none", 1))
    )


_PortPhyX25OperDialOut_Type.__name__ = "Integer32"
_PortPhyX25OperDialOut_Object = MibTableColumn
portPhyX25OperDialOut = _PortPhyX25OperDialOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 5),
    _PortPhyX25OperDialOut_Type()
)
portPhyX25OperDialOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperDialOut.setStatus("mandatory")


class _PortPhyX25OperInactivityTimer_Type(Integer32):
    """Custom type portPhyX25OperInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PortPhyX25OperInactivityTimer_Type.__name__ = "Integer32"
_PortPhyX25OperInactivityTimer_Object = MibTableColumn
portPhyX25OperInactivityTimer = _PortPhyX25OperInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 6),
    _PortPhyX25OperInactivityTimer_Type()
)
portPhyX25OperInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperInactivityTimer.setStatus("mandatory")


class _PortPhyX25OperDisconnectTimer_Type(Integer32):
    """Custom type portPhyX25OperDisconnectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortPhyX25OperDisconnectTimer_Type.__name__ = "Integer32"
_PortPhyX25OperDisconnectTimer_Object = MibTableColumn
portPhyX25OperDisconnectTimer = _PortPhyX25OperDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 7),
    _PortPhyX25OperDisconnectTimer_Type()
)
portPhyX25OperDisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperDisconnectTimer.setStatus("mandatory")


class _PortPhyX25OperSetupTimer_Type(Integer32):
    """Custom type portPhyX25OperSetupTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortPhyX25OperSetupTimer_Type.__name__ = "Integer32"
_PortPhyX25OperSetupTimer_Object = MibTableColumn
portPhyX25OperSetupTimer = _PortPhyX25OperSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 8),
    _PortPhyX25OperSetupTimer_Type()
)
portPhyX25OperSetupTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperSetupTimer.setStatus("mandatory")


class _PortPhyX25OperTrunkFlag_Type(Integer32):
    """Custom type portPhyX25OperTrunkFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPhyX25OperTrunkFlag_Type.__name__ = "Integer32"
_PortPhyX25OperTrunkFlag_Object = MibTableColumn
portPhyX25OperTrunkFlag = _PortPhyX25OperTrunkFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 9),
    _PortPhyX25OperTrunkFlag_Type()
)
portPhyX25OperTrunkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperTrunkFlag.setStatus("mandatory")
_PortPhyX25OperTrunkGroup_Type = OctetString
_PortPhyX25OperTrunkGroup_Object = MibTableColumn
portPhyX25OperTrunkGroup = _PortPhyX25OperTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 2, 1, 10),
    _PortPhyX25OperTrunkGroup_Type()
)
portPhyX25OperTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhyX25OperTrunkGroup.setStatus("mandatory")
_PortLogicalX25AdminTable_Object = MibTable
portLogicalX25AdminTable = _PortLogicalX25AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3)
)
if mibBuilder.loadTexts:
    portLogicalX25AdminTable.setStatus("mandatory")
_PortLogicalX25AdminEntry_Object = MibTableRow
portLogicalX25AdminEntry = _PortLogicalX25AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1)
)
portLogicalX25AdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPhyPort"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portLogicalX25AdminEntry.setStatus("mandatory")


class _PortLogicalX25AdminFrDlci_Type(Integer32):
    """Custom type portLogicalX25AdminFrDlci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PortLogicalX25AdminFrDlci_Type.__name__ = "Integer32"
_PortLogicalX25AdminFrDlci_Object = MibTableColumn
portLogicalX25AdminFrDlci = _PortLogicalX25AdminFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1, 1),
    _PortLogicalX25AdminFrDlci_Type()
)
portLogicalX25AdminFrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLogicalX25AdminFrDlci.setStatus("mandatory")


class _PortLogicalX25AdminCxnPriority_Type(Integer32):
    """Custom type portLogicalX25AdminCxnPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PortLogicalX25AdminCxnPriority_Type.__name__ = "Integer32"
_PortLogicalX25AdminCxnPriority_Object = MibTableColumn
portLogicalX25AdminCxnPriority = _PortLogicalX25AdminCxnPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1, 2),
    _PortLogicalX25AdminCxnPriority_Type()
)
portLogicalX25AdminCxnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLogicalX25AdminCxnPriority.setStatus("mandatory")


class _PortLogicalX25AdminRfc1490_Type(Integer32):
    """Custom type portLogicalX25AdminRfc1490 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexG", 1),
          ("rfc1490", 2))
    )


_PortLogicalX25AdminRfc1490_Type.__name__ = "Integer32"
_PortLogicalX25AdminRfc1490_Object = MibTableColumn
portLogicalX25AdminRfc1490 = _PortLogicalX25AdminRfc1490_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1, 3),
    _PortLogicalX25AdminRfc1490_Type()
)
portLogicalX25AdminRfc1490.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLogicalX25AdminRfc1490.setStatus("mandatory")


class _PortLogicalX25AdminBAG_Type(Integer32):
    """Custom type portLogicalX25AdminBAG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PortLogicalX25AdminBAG_Type.__name__ = "Integer32"
_PortLogicalX25AdminBAG_Object = MibTableColumn
portLogicalX25AdminBAG = _PortLogicalX25AdminBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1, 4),
    _PortLogicalX25AdminBAG_Type()
)
portLogicalX25AdminBAG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLogicalX25AdminBAG.setStatus("mandatory")
_PortLogicalX25AdminRowStatus_Type = RowStatus
_PortLogicalX25AdminRowStatus_Object = MibTableColumn
portLogicalX25AdminRowStatus = _PortLogicalX25AdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 3, 1, 5),
    _PortLogicalX25AdminRowStatus_Type()
)
portLogicalX25AdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLogicalX25AdminRowStatus.setStatus("mandatory")
_PortLogicalX25OperTable_Object = MibTable
portLogicalX25OperTable = _PortLogicalX25OperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4)
)
if mibBuilder.loadTexts:
    portLogicalX25OperTable.setStatus("mandatory")
_PortLogicalX25OperEntry_Object = MibTableRow
portLogicalX25OperEntry = _PortLogicalX25OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4, 1)
)
portLogicalX25OperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPhyPort"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portLogicalX25OperEntry.setStatus("mandatory")


class _PortLogicalX25OperFrDlci_Type(Integer32):
    """Custom type portLogicalX25OperFrDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortLogicalX25OperFrDlci_Type.__name__ = "Integer32"
_PortLogicalX25OperFrDlci_Object = MibTableColumn
portLogicalX25OperFrDlci = _PortLogicalX25OperFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4, 1, 1),
    _PortLogicalX25OperFrDlci_Type()
)
portLogicalX25OperFrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLogicalX25OperFrDlci.setStatus("mandatory")


class _PortLogicalX25OperCxnPriority_Type(Integer32):
    """Custom type portLogicalX25OperCxnPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PortLogicalX25OperCxnPriority_Type.__name__ = "Integer32"
_PortLogicalX25OperCxnPriority_Object = MibTableColumn
portLogicalX25OperCxnPriority = _PortLogicalX25OperCxnPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4, 1, 2),
    _PortLogicalX25OperCxnPriority_Type()
)
portLogicalX25OperCxnPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLogicalX25OperCxnPriority.setStatus("mandatory")


class _PortLogicalX25OperRfc1490_Type(Integer32):
    """Custom type portLogicalX25OperRfc1490 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexG", 1),
          ("rfc1490", 2))
    )


_PortLogicalX25OperRfc1490_Type.__name__ = "Integer32"
_PortLogicalX25OperRfc1490_Object = MibTableColumn
portLogicalX25OperRfc1490 = _PortLogicalX25OperRfc1490_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4, 1, 3),
    _PortLogicalX25OperRfc1490_Type()
)
portLogicalX25OperRfc1490.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLogicalX25OperRfc1490.setStatus("mandatory")


class _PortLogicalX25OperBAG_Type(Integer32):
    """Custom type portLogicalX25OperBAG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortLogicalX25OperBAG_Type.__name__ = "Integer32"
_PortLogicalX25OperBAG_Object = MibTableColumn
portLogicalX25OperBAG = _PortLogicalX25OperBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 4, 1, 4),
    _PortLogicalX25OperBAG_Type()
)
portLogicalX25OperBAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLogicalX25OperBAG.setStatus("mandatory")
_PortX25AdminTable_Object = MibTable
portX25AdminTable = _PortX25AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5)
)
if mibBuilder.loadTexts:
    portX25AdminTable.setStatus("mandatory")
_PortX25AdminEntry_Object = MibTableRow
portX25AdminEntry = _PortX25AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1)
)
portX25AdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portX25AdminEntry.setStatus("mandatory")


class _PortX25AdminBlockedFlag_Type(Integer32):
    """Custom type portX25AdminBlockedFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminBlockedFlag_Type.__name__ = "Integer32"
_PortX25AdminBlockedFlag_Object = MibTableColumn
portX25AdminBlockedFlag = _PortX25AdminBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 1),
    _PortX25AdminBlockedFlag_Type()
)
portX25AdminBlockedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminBlockedFlag.setStatus("mandatory")


class _PortX25AdminFlowCtrlNeg_Type(Integer32):
    """Custom type portX25AdminFlowCtrlNeg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminFlowCtrlNeg_Type.__name__ = "Integer32"
_PortX25AdminFlowCtrlNeg_Object = MibTableColumn
portX25AdminFlowCtrlNeg = _PortX25AdminFlowCtrlNeg_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 2),
    _PortX25AdminFlowCtrlNeg_Type()
)
portX25AdminFlowCtrlNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminFlowCtrlNeg.setStatus("mandatory")


class _PortX25AdminThruptClassNeg_Type(Integer32):
    """Custom type portX25AdminThruptClassNeg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminThruptClassNeg_Type.__name__ = "Integer32"
_PortX25AdminThruptClassNeg_Object = MibTableColumn
portX25AdminThruptClassNeg = _PortX25AdminThruptClassNeg_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 3),
    _PortX25AdminThruptClassNeg_Type()
)
portX25AdminThruptClassNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminThruptClassNeg.setStatus("mandatory")


class _PortX25AdminLocChgPrev_Type(Integer32):
    """Custom type portX25AdminLocChgPrev based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminLocChgPrev_Type.__name__ = "Integer32"
_PortX25AdminLocChgPrev_Object = MibTableColumn
portX25AdminLocChgPrev = _PortX25AdminLocChgPrev_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 4),
    _PortX25AdminLocChgPrev_Type()
)
portX25AdminLocChgPrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminLocChgPrev.setStatus("mandatory")


class _PortX25AdminRevChgAccpt_Type(Integer32):
    """Custom type portX25AdminRevChgAccpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminRevChgAccpt_Type.__name__ = "Integer32"
_PortX25AdminRevChgAccpt_Object = MibTableColumn
portX25AdminRevChgAccpt = _PortX25AdminRevChgAccpt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 5),
    _PortX25AdminRevChgAccpt_Type()
)
portX25AdminRevChgAccpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminRevChgAccpt.setStatus("mandatory")


class _PortX25AdminFastSelAccpt_Type(Integer32):
    """Custom type portX25AdminFastSelAccpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminFastSelAccpt_Type.__name__ = "Integer32"
_PortX25AdminFastSelAccpt_Object = MibTableColumn
portX25AdminFastSelAccpt = _PortX25AdminFastSelAccpt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 6),
    _PortX25AdminFastSelAccpt_Type()
)
portX25AdminFastSelAccpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminFastSelAccpt.setStatus("mandatory")


class _PortX25AdminInCallBar_Type(Integer32):
    """Custom type portX25AdminInCallBar based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminInCallBar_Type.__name__ = "Integer32"
_PortX25AdminInCallBar_Object = MibTableColumn
portX25AdminInCallBar = _PortX25AdminInCallBar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 7),
    _PortX25AdminInCallBar_Type()
)
portX25AdminInCallBar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminInCallBar.setStatus("mandatory")


class _PortX25AdminOutCallBar_Type(Integer32):
    """Custom type portX25AdminOutCallBar based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminOutCallBar_Type.__name__ = "Integer32"
_PortX25AdminOutCallBar_Object = MibTableColumn
portX25AdminOutCallBar = _PortX25AdminOutCallBar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 8),
    _PortX25AdminOutCallBar_Type()
)
portX25AdminOutCallBar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminOutCallBar.setStatus("mandatory")


class _PortX25AdminMaxPktSize_Type(Integer32):
    """Custom type portX25AdminMaxPktSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 4096),
    )


_PortX25AdminMaxPktSize_Type.__name__ = "Integer32"
_PortX25AdminMaxPktSize_Object = MibTableColumn
portX25AdminMaxPktSize = _PortX25AdminMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 9),
    _PortX25AdminMaxPktSize_Type()
)
portX25AdminMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminMaxPktSize.setStatus("mandatory")


class _PortX25AdminDefPktSize_Type(Integer32):
    """Custom type portX25AdminDefPktSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_PortX25AdminDefPktSize_Type.__name__ = "Integer32"
_PortX25AdminDefPktSize_Object = MibTableColumn
portX25AdminDefPktSize = _PortX25AdminDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 10),
    _PortX25AdminDefPktSize_Type()
)
portX25AdminDefPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminDefPktSize.setStatus("mandatory")


class _PortX25AdminMaxWinSize_Type(Integer32):
    """Custom type portX25AdminMaxWinSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_PortX25AdminMaxWinSize_Type.__name__ = "Integer32"
_PortX25AdminMaxWinSize_Object = MibTableColumn
portX25AdminMaxWinSize = _PortX25AdminMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 11),
    _PortX25AdminMaxWinSize_Type()
)
portX25AdminMaxWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminMaxWinSize.setStatus("mandatory")


class _PortX25AdminDefWinSize_Type(Integer32):
    """Custom type portX25AdminDefWinSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PortX25AdminDefWinSize_Type.__name__ = "Integer32"
_PortX25AdminDefWinSize_Object = MibTableColumn
portX25AdminDefWinSize = _PortX25AdminDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 12),
    _PortX25AdminDefWinSize_Type()
)
portX25AdminDefWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminDefWinSize.setStatus("mandatory")


class _PortX25AdminMaxThruptClass_Type(Integer32):
    """Custom type portX25AdminMaxThruptClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 13),
    )


_PortX25AdminMaxThruptClass_Type.__name__ = "Integer32"
_PortX25AdminMaxThruptClass_Object = MibTableColumn
portX25AdminMaxThruptClass = _PortX25AdminMaxThruptClass_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 13),
    _PortX25AdminMaxThruptClass_Type()
)
portX25AdminMaxThruptClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminMaxThruptClass.setStatus("mandatory")


class _PortX25AdminCUGPref_Type(Integer32):
    """Custom type portX25AdminCUGPref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminCUGPref_Type.__name__ = "Integer32"
_PortX25AdminCUGPref_Object = MibTableColumn
portX25AdminCUGPref = _PortX25AdminCUGPref_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 14),
    _PortX25AdminCUGPref_Type()
)
portX25AdminCUGPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminCUGPref.setStatus("mandatory")


class _PortX25AdminCUGIndex_Type(Integer32):
    """Custom type portX25AdminCUGIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PortX25AdminCUGIndex_Type.__name__ = "Integer32"
_PortX25AdminCUGIndex_Object = MibTableColumn
portX25AdminCUGIndex = _PortX25AdminCUGIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 15),
    _PortX25AdminCUGIndex_Type()
)
portX25AdminCUGIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminCUGIndex.setStatus("mandatory")


class _PortX25AdminCUGIncAccess_Type(Integer32):
    """Custom type portX25AdminCUGIncAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminCUGIncAccess_Type.__name__ = "Integer32"
_PortX25AdminCUGIncAccess_Object = MibTableColumn
portX25AdminCUGIncAccess = _PortX25AdminCUGIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 16),
    _PortX25AdminCUGIncAccess_Type()
)
portX25AdminCUGIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminCUGIncAccess.setStatus("mandatory")


class _PortX25AdminCUGOutAccess_Type(Integer32):
    """Custom type portX25AdminCUGOutAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25AdminCUGOutAccess_Type.__name__ = "Integer32"
_PortX25AdminCUGOutAccess_Object = MibTableColumn
portX25AdminCUGOutAccess = _PortX25AdminCUGOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 5, 1, 17),
    _PortX25AdminCUGOutAccess_Type()
)
portX25AdminCUGOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portX25AdminCUGOutAccess.setStatus("mandatory")
_PortX25OperTable_Object = MibTable
portX25OperTable = _PortX25OperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6)
)
if mibBuilder.loadTexts:
    portX25OperTable.setStatus("mandatory")
_PortX25OperEntry_Object = MibTableRow
portX25OperEntry = _PortX25OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1)
)
portX25OperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portX25OperEntry.setStatus("mandatory")


class _PortX25OperBlockedFlag_Type(Integer32):
    """Custom type portX25OperBlockedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperBlockedFlag_Type.__name__ = "Integer32"
_PortX25OperBlockedFlag_Object = MibTableColumn
portX25OperBlockedFlag = _PortX25OperBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 1),
    _PortX25OperBlockedFlag_Type()
)
portX25OperBlockedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperBlockedFlag.setStatus("mandatory")


class _PortX25OperFlowCtrlNeg_Type(Integer32):
    """Custom type portX25OperFlowCtrlNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperFlowCtrlNeg_Type.__name__ = "Integer32"
_PortX25OperFlowCtrlNeg_Object = MibTableColumn
portX25OperFlowCtrlNeg = _PortX25OperFlowCtrlNeg_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 2),
    _PortX25OperFlowCtrlNeg_Type()
)
portX25OperFlowCtrlNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperFlowCtrlNeg.setStatus("mandatory")


class _PortX25OperThruptClassNeg_Type(Integer32):
    """Custom type portX25OperThruptClassNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperThruptClassNeg_Type.__name__ = "Integer32"
_PortX25OperThruptClassNeg_Object = MibTableColumn
portX25OperThruptClassNeg = _PortX25OperThruptClassNeg_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 3),
    _PortX25OperThruptClassNeg_Type()
)
portX25OperThruptClassNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperThruptClassNeg.setStatus("mandatory")


class _PortX25OperLocChgPrev_Type(Integer32):
    """Custom type portX25OperLocChgPrev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperLocChgPrev_Type.__name__ = "Integer32"
_PortX25OperLocChgPrev_Object = MibTableColumn
portX25OperLocChgPrev = _PortX25OperLocChgPrev_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 4),
    _PortX25OperLocChgPrev_Type()
)
portX25OperLocChgPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperLocChgPrev.setStatus("mandatory")


class _PortX25OperRevChgAccpt_Type(Integer32):
    """Custom type portX25OperRevChgAccpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperRevChgAccpt_Type.__name__ = "Integer32"
_PortX25OperRevChgAccpt_Object = MibTableColumn
portX25OperRevChgAccpt = _PortX25OperRevChgAccpt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 5),
    _PortX25OperRevChgAccpt_Type()
)
portX25OperRevChgAccpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperRevChgAccpt.setStatus("mandatory")


class _PortX25OperFastSelAccpt_Type(Integer32):
    """Custom type portX25OperFastSelAccpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperFastSelAccpt_Type.__name__ = "Integer32"
_PortX25OperFastSelAccpt_Object = MibTableColumn
portX25OperFastSelAccpt = _PortX25OperFastSelAccpt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 6),
    _PortX25OperFastSelAccpt_Type()
)
portX25OperFastSelAccpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperFastSelAccpt.setStatus("mandatory")


class _PortX25OperInCallBar_Type(Integer32):
    """Custom type portX25OperInCallBar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperInCallBar_Type.__name__ = "Integer32"
_PortX25OperInCallBar_Object = MibTableColumn
portX25OperInCallBar = _PortX25OperInCallBar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 7),
    _PortX25OperInCallBar_Type()
)
portX25OperInCallBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperInCallBar.setStatus("mandatory")


class _PortX25OperOutCallBar_Type(Integer32):
    """Custom type portX25OperOutCallBar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperOutCallBar_Type.__name__ = "Integer32"
_PortX25OperOutCallBar_Object = MibTableColumn
portX25OperOutCallBar = _PortX25OperOutCallBar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 8),
    _PortX25OperOutCallBar_Type()
)
portX25OperOutCallBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperOutCallBar.setStatus("mandatory")


class _PortX25OperMaxPktSize_Type(Integer32):
    """Custom type portX25OperMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 4096),
    )


_PortX25OperMaxPktSize_Type.__name__ = "Integer32"
_PortX25OperMaxPktSize_Object = MibTableColumn
portX25OperMaxPktSize = _PortX25OperMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 9),
    _PortX25OperMaxPktSize_Type()
)
portX25OperMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperMaxPktSize.setStatus("mandatory")


class _PortX25OperDefPktSize_Type(Integer32):
    """Custom type portX25OperDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_PortX25OperDefPktSize_Type.__name__ = "Integer32"
_PortX25OperDefPktSize_Object = MibTableColumn
portX25OperDefPktSize = _PortX25OperDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 10),
    _PortX25OperDefPktSize_Type()
)
portX25OperDefPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperDefPktSize.setStatus("mandatory")


class _PortX25OperMaxWinSize_Type(Integer32):
    """Custom type portX25OperMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_PortX25OperMaxWinSize_Type.__name__ = "Integer32"
_PortX25OperMaxWinSize_Object = MibTableColumn
portX25OperMaxWinSize = _PortX25OperMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 11),
    _PortX25OperMaxWinSize_Type()
)
portX25OperMaxWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperMaxWinSize.setStatus("mandatory")


class _PortX25OperDefWinSize_Type(Integer32):
    """Custom type portX25OperDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PortX25OperDefWinSize_Type.__name__ = "Integer32"
_PortX25OperDefWinSize_Object = MibTableColumn
portX25OperDefWinSize = _PortX25OperDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 12),
    _PortX25OperDefWinSize_Type()
)
portX25OperDefWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperDefWinSize.setStatus("mandatory")


class _PortX25OperMaxThruptClass_Type(Integer32):
    """Custom type portX25OperMaxThruptClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 13),
    )


_PortX25OperMaxThruptClass_Type.__name__ = "Integer32"
_PortX25OperMaxThruptClass_Object = MibTableColumn
portX25OperMaxThruptClass = _PortX25OperMaxThruptClass_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 13),
    _PortX25OperMaxThruptClass_Type()
)
portX25OperMaxThruptClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperMaxThruptClass.setStatus("mandatory")


class _PortX25OperCUGPref_Type(Integer32):
    """Custom type portX25OperCUGPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperCUGPref_Type.__name__ = "Integer32"
_PortX25OperCUGPref_Object = MibTableColumn
portX25OperCUGPref = _PortX25OperCUGPref_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 14),
    _PortX25OperCUGPref_Type()
)
portX25OperCUGPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperCUGPref.setStatus("mandatory")


class _PortX25OperCUGIndex_Type(Integer32):
    """Custom type portX25OperCUGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PortX25OperCUGIndex_Type.__name__ = "Integer32"
_PortX25OperCUGIndex_Object = MibTableColumn
portX25OperCUGIndex = _PortX25OperCUGIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 15),
    _PortX25OperCUGIndex_Type()
)
portX25OperCUGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperCUGIndex.setStatus("mandatory")


class _PortX25OperCUGIncAccess_Type(Integer32):
    """Custom type portX25OperCUGIncAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperCUGIncAccess_Type.__name__ = "Integer32"
_PortX25OperCUGIncAccess_Object = MibTableColumn
portX25OperCUGIncAccess = _PortX25OperCUGIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 16),
    _PortX25OperCUGIncAccess_Type()
)
portX25OperCUGIncAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperCUGIncAccess.setStatus("mandatory")


class _PortX25OperCUGOutAccess_Type(Integer32):
    """Custom type portX25OperCUGOutAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortX25OperCUGOutAccess_Type.__name__ = "Integer32"
_PortX25OperCUGOutAccess_Object = MibTableColumn
portX25OperCUGOutAccess = _PortX25OperCUGOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 1, 6, 1, 17),
    _PortX25OperCUGOutAccess_Type()
)
portX25OperCUGOutAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portX25OperCUGOutAccess.setStatus("mandatory")
_PortFrGroup_ObjectIdentity = ObjectIdentity
portFrGroup = _PortFrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2)
)
_PortFrConfigTable_Object = MibTable
portFrConfigTable = _PortFrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    portFrConfigTable.setStatus("mandatory")
_PortFrEntry_Object = MibTableRow
portFrEntry = _PortFrEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1)
)
portFrEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portFrRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portFrPortIndex"),
)
if mibBuilder.loadTexts:
    portFrEntry.setStatus("mandatory")
_PortFrRlpIndex_Type = Integer32
_PortFrRlpIndex_Object = MibTableColumn
portFrRlpIndex = _PortFrRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 1),
    _PortFrRlpIndex_Type()
)
portFrRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrRlpIndex.setStatus("mandatory")
_PortFrPortIndex_Type = Integer32
_PortFrPortIndex_Object = MibTableColumn
portFrPortIndex = _PortFrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 2),
    _PortFrPortIndex_Type()
)
portFrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrPortIndex.setStatus("mandatory")


class _PortFrBlockedFlag_Type(Integer32):
    """Custom type portFrBlockedFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrBlockedFlag_Type.__name__ = "Integer32"
_PortFrBlockedFlag_Object = MibTableColumn
portFrBlockedFlag = _PortFrBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 3),
    _PortFrBlockedFlag_Type()
)
portFrBlockedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBlockedFlag.setStatus("mandatory")


class _PortFrMaxBytesPerFrame_Type(Integer32):
    """Custom type portFrMaxBytesPerFrame based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_PortFrMaxBytesPerFrame_Type.__name__ = "Integer32"
_PortFrMaxBytesPerFrame_Object = MibTableColumn
portFrMaxBytesPerFrame = _PortFrMaxBytesPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 4),
    _PortFrMaxBytesPerFrame_Type()
)
portFrMaxBytesPerFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrMaxBytesPerFrame.setStatus("mandatory")


class _PortFrT392Timer_Type(Integer32):
    """Custom type portFrT392Timer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_PortFrT392Timer_Type.__name__ = "Integer32"
_PortFrT392Timer_Object = MibTableColumn
portFrT392Timer = _PortFrT392Timer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 5),
    _PortFrT392Timer_Type()
)
portFrT392Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrT392Timer.setStatus("mandatory")


class _PortFrOutgoingRateControl_Type(Integer32):
    """Custom type portFrOutgoingRateControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrOutgoingRateControl_Type.__name__ = "Integer32"
_PortFrOutgoingRateControl_Object = MibTableColumn
portFrOutgoingRateControl = _PortFrOutgoingRateControl_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 6),
    _PortFrOutgoingRateControl_Type()
)
portFrOutgoingRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrOutgoingRateControl.setStatus("mandatory")


class _PortFrBandwidthAllocation_Type(Integer32):
    """Custom type portFrBandwidthAllocation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrBandwidthAllocation_Type.__name__ = "Integer32"
_PortFrBandwidthAllocation_Object = MibTableColumn
portFrBandwidthAllocation = _PortFrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 7),
    _PortFrBandwidthAllocation_Type()
)
portFrBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBandwidthAllocation.setStatus("mandatory")


class _PortFrConnector_Type(Integer32):
    """Custom type portFrConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("e1", 11),
          ("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortFrConnector_Type.__name__ = "Integer32"
_PortFrConnector_Object = MibTableColumn
portFrConnector = _PortFrConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 8),
    _PortFrConnector_Type()
)
portFrConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrConnector.setStatus("mandatory")


class _PortFrLogicalDCE_Type(Integer32):
    """Custom type portFrLogicalDCE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrLogicalDCE_Type.__name__ = "Integer32"
_PortFrLogicalDCE_Object = MibTableColumn
portFrLogicalDCE = _PortFrLogicalDCE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 9),
    _PortFrLogicalDCE_Type()
)
portFrLogicalDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrLogicalDCE.setStatus("mandatory")


class _PortFrGenClock_Type(Integer32):
    """Custom type portFrGenClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrGenClock_Type.__name__ = "Integer32"
_PortFrGenClock_Object = MibTableColumn
portFrGenClock = _PortFrGenClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 10),
    _PortFrGenClock_Type()
)
portFrGenClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrGenClock.setStatus("mandatory")


class _PortFrRcvClkFrmDTE_Type(Integer32):
    """Custom type portFrRcvClkFrmDTE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrRcvClkFrmDTE_Type.__name__ = "Integer32"
_PortFrRcvClkFrmDTE_Object = MibTableColumn
portFrRcvClkFrmDTE = _PortFrRcvClkFrmDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 11),
    _PortFrRcvClkFrmDTE_Type()
)
portFrRcvClkFrmDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrRcvClkFrmDTE.setStatus("mandatory")


class _PortFrLLM_Type(Integer32):
    """Custom type portFrLLM based on Integer32"""
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
        *(("annexd", 3),
          ("lmi", 2),
          ("none", 1))
    )


_PortFrLLM_Type.__name__ = "Integer32"
_PortFrLLM_Object = MibTableColumn
portFrLLM = _PortFrLLM_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 12),
    _PortFrLLM_Type()
)
portFrLLM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrLLM.setStatus("mandatory")
_PortFrRowStatus_Type = RowStatus
_PortFrRowStatus_Object = MibTableColumn
portFrRowStatus = _PortFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 13),
    _PortFrRowStatus_Type()
)
portFrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrRowStatus.setStatus("mandatory")


class _PortFrSpeed_Type(Integer32):
    """Custom type portFrSpeed based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 2048000),
    )


_PortFrSpeed_Type.__name__ = "Integer32"
_PortFrSpeed_Object = MibTableColumn
portFrSpeed = _PortFrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 14),
    _PortFrSpeed_Type()
)
portFrSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrSpeed.setStatus("mandatory")


class _PortFrBackupUseOnly_Type(Integer32):
    """Custom type portFrBackupUseOnly based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrBackupUseOnly_Type.__name__ = "Integer32"
_PortFrBackupUseOnly_Object = MibTableColumn
portFrBackupUseOnly = _PortFrBackupUseOnly_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 1, 1, 15),
    _PortFrBackupUseOnly_Type()
)
portFrBackupUseOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBackupUseOnly.setStatus("mandatory")
_PortDLCIConfigTable_Object = MibTable
portDLCIConfigTable = _PortDLCIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    portDLCIConfigTable.setStatus("mandatory")
_PortDLCIEntry_Object = MibTableRow
portDLCIEntry = _PortDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1)
)
portDLCIEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portDLCIRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portDLCIPortIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portDLCIIndex"),
)
if mibBuilder.loadTexts:
    portDLCIEntry.setStatus("mandatory")
_PortDLCIRlpIndex_Type = Integer32
_PortDLCIRlpIndex_Object = MibTableColumn
portDLCIRlpIndex = _PortDLCIRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 1),
    _PortDLCIRlpIndex_Type()
)
portDLCIRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDLCIRlpIndex.setStatus("mandatory")
_PortDLCIPortIndex_Type = Integer32
_PortDLCIPortIndex_Object = MibTableColumn
portDLCIPortIndex = _PortDLCIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 2),
    _PortDLCIPortIndex_Type()
)
portDLCIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDLCIPortIndex.setStatus("mandatory")
_PortDLCIIndex_Type = Integer32
_PortDLCIIndex_Object = MibTableColumn
portDLCIIndex = _PortDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 3),
    _PortDLCIIndex_Type()
)
portDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDLCIIndex.setStatus("mandatory")


class _PortDLCIIncomingCIR_Type(Integer32):
    """Custom type portDLCIIncomingCIR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_PortDLCIIncomingCIR_Type.__name__ = "Integer32"
_PortDLCIIncomingCIR_Object = MibTableColumn
portDLCIIncomingCIR = _PortDLCIIncomingCIR_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 4),
    _PortDLCIIncomingCIR_Type()
)
portDLCIIncomingCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIIncomingCIR.setStatus("mandatory")


class _PortDLCIOutgoingCIR_Type(Integer32):
    """Custom type portDLCIOutgoingCIR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_PortDLCIOutgoingCIR_Type.__name__ = "Integer32"
_PortDLCIOutgoingCIR_Object = MibTableColumn
portDLCIOutgoingCIR = _PortDLCIOutgoingCIR_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 5),
    _PortDLCIOutgoingCIR_Type()
)
portDLCIOutgoingCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIOutgoingCIR.setStatus("mandatory")


class _PortDLCIIncomingBc_Type(Integer32):
    """Custom type portDLCIIncomingBc based on Integer32"""
    defaultValue = 0


_PortDLCIIncomingBc_Object = MibTableColumn
portDLCIIncomingBc = _PortDLCIIncomingBc_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 6),
    _PortDLCIIncomingBc_Type()
)
portDLCIIncomingBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIIncomingBc.setStatus("mandatory")


class _PortDLCIOutgoingBc_Type(Integer32):
    """Custom type portDLCIOutgoingBc based on Integer32"""
    defaultValue = 0


_PortDLCIOutgoingBc_Object = MibTableColumn
portDLCIOutgoingBc = _PortDLCIOutgoingBc_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 7),
    _PortDLCIOutgoingBc_Type()
)
portDLCIOutgoingBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIOutgoingBc.setStatus("mandatory")


class _PortDLCIIncomingBe_Type(Integer32):
    """Custom type portDLCIIncomingBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PortDLCIIncomingBe_Type.__name__ = "Integer32"
_PortDLCIIncomingBe_Object = MibTableColumn
portDLCIIncomingBe = _PortDLCIIncomingBe_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 8),
    _PortDLCIIncomingBe_Type()
)
portDLCIIncomingBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIIncomingBe.setStatus("mandatory")


class _PortDLCIOutgoingBe_Type(Integer32):
    """Custom type portDLCIOutgoingBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PortDLCIOutgoingBe_Type.__name__ = "Integer32"
_PortDLCIOutgoingBe_Object = MibTableColumn
portDLCIOutgoingBe = _PortDLCIOutgoingBe_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 9),
    _PortDLCIOutgoingBe_Type()
)
portDLCIOutgoingBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIOutgoingBe.setStatus("mandatory")


class _PortDLCIBecnRecoveryCnt_Type(Integer32):
    """Custom type portDLCIBecnRecoveryCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortDLCIBecnRecoveryCnt_Type.__name__ = "Integer32"
_PortDLCIBecnRecoveryCnt_Object = MibTableColumn
portDLCIBecnRecoveryCnt = _PortDLCIBecnRecoveryCnt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 10),
    _PortDLCIBecnRecoveryCnt_Type()
)
portDLCIBecnRecoveryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIBecnRecoveryCnt.setStatus("mandatory")


class _PortDLCIPriority_Type(Integer32):
    """Custom type portDLCIPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PortDLCIPriority_Type.__name__ = "Integer32"
_PortDLCIPriority_Object = MibTableColumn
portDLCIPriority = _PortDLCIPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 11),
    _PortDLCIPriority_Type()
)
portDLCIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIPriority.setStatus("mandatory")
_PortDLCIRowStatus_Type = RowStatus
_PortDLCIRowStatus_Object = MibTableColumn
portDLCIRowStatus = _PortDLCIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 12),
    _PortDLCIRowStatus_Type()
)
portDLCIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIRowStatus.setStatus("mandatory")


class _PortDLCIBackupGroup_Type(Integer32):
    """Custom type portDLCIBackupGroup based on Integer32"""
    defaultValue = 0


_PortDLCIBackupGroup_Object = MibTableColumn
portDLCIBackupGroup = _PortDLCIBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 13),
    _PortDLCIBackupGroup_Type()
)
portDLCIBackupGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIBackupGroup.setStatus("mandatory")


class _PortDLCIBackupProtEnb_Type(Integer32):
    """Custom type portDLCIBackupProtEnb based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortDLCIBackupProtEnb_Type.__name__ = "Integer32"
_PortDLCIBackupProtEnb_Object = MibTableColumn
portDLCIBackupProtEnb = _PortDLCIBackupProtEnb_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 2, 1, 14),
    _PortDLCIBackupProtEnb_Type()
)
portDLCIBackupProtEnb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDLCIBackupProtEnb.setStatus("mandatory")
_PortFrBackupGroupTable_Object = MibTable
portFrBackupGroupTable = _PortFrBackupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3)
)
if mibBuilder.loadTexts:
    portFrBackupGroupTable.setStatus("mandatory")
_PortFrBackupEntry_Object = MibTableRow
portFrBackupEntry = _PortFrBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1)
)
portFrBackupEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portFrBackupRLP"),
    (0, "NETLINK-SPECIFIC-MIB", "portFrBackupPort"),
    (0, "NETLINK-SPECIFIC-MIB", "portFrBackupDLCI"),
    (0, "NETLINK-SPECIFIC-MIB", "portFrBackupGroup"),
)
if mibBuilder.loadTexts:
    portFrBackupEntry.setStatus("mandatory")


class _PortFrBackupRLP_Type(Integer32):
    """Custom type portFrBackupRLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortFrBackupRLP_Type.__name__ = "Integer32"
_PortFrBackupRLP_Object = MibTableColumn
portFrBackupRLP = _PortFrBackupRLP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 1),
    _PortFrBackupRLP_Type()
)
portFrBackupRLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrBackupRLP.setStatus("mandatory")


class _PortFrBackupPort_Type(Integer32):
    """Custom type portFrBackupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortFrBackupPort_Type.__name__ = "Integer32"
_PortFrBackupPort_Object = MibTableColumn
portFrBackupPort = _PortFrBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 2),
    _PortFrBackupPort_Type()
)
portFrBackupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrBackupPort.setStatus("mandatory")


class _PortFrBackupDLCI_Type(Integer32):
    """Custom type portFrBackupDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PortFrBackupDLCI_Type.__name__ = "Integer32"
_PortFrBackupDLCI_Object = MibTableColumn
portFrBackupDLCI = _PortFrBackupDLCI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 3),
    _PortFrBackupDLCI_Type()
)
portFrBackupDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrBackupDLCI.setStatus("mandatory")


class _PortFrBackupGroup_Type(Integer32):
    """Custom type portFrBackupGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortFrBackupGroup_Type.__name__ = "Integer32"
_PortFrBackupGroup_Object = MibTableColumn
portFrBackupGroup = _PortFrBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 4),
    _PortFrBackupGroup_Type()
)
portFrBackupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrBackupGroup.setStatus("mandatory")


class _PortFrBackupWaitTimer_Type(Integer32):
    """Custom type portFrBackupWaitTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortFrBackupWaitTimer_Type.__name__ = "Integer32"
_PortFrBackupWaitTimer_Object = MibTableColumn
portFrBackupWaitTimer = _PortFrBackupWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 5),
    _PortFrBackupWaitTimer_Type()
)
portFrBackupWaitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBackupWaitTimer.setStatus("mandatory")


class _PortFrBackupProtEnab_Type(Integer32):
    """Custom type portFrBackupProtEnab based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortFrBackupProtEnab_Type.__name__ = "Integer32"
_PortFrBackupProtEnab_Object = MibTableColumn
portFrBackupProtEnab = _PortFrBackupProtEnab_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 6),
    _PortFrBackupProtEnab_Type()
)
portFrBackupProtEnab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBackupProtEnab.setStatus("mandatory")
_PortFrBackupRowStatus_Type = RowStatus
_PortFrBackupRowStatus_Object = MibTableColumn
portFrBackupRowStatus = _PortFrBackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 2, 3, 1, 7),
    _PortFrBackupRowStatus_Type()
)
portFrBackupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrBackupRowStatus.setStatus("mandatory")
_PortBsciGroup_ObjectIdentity = ObjectIdentity
portBsciGroup = _PortBsciGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4)
)
_PortBsciAdminTable_Object = MibTable
portBsciAdminTable = _PortBsciAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1)
)
if mibBuilder.loadTexts:
    portBsciAdminTable.setStatus("mandatory")
_PortBsciAdminEntry_Object = MibTableRow
portBsciAdminEntry = _PortBsciAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1)
)
portBsciAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portBsciAdminEntry.setStatus("mandatory")


class _PortBsciAdminBlockedFlag_Type(Integer32):
    """Custom type portBsciAdminBlockedFlag based on Integer32"""
    defaultValue = 1

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


_PortBsciAdminBlockedFlag_Type.__name__ = "Integer32"
_PortBsciAdminBlockedFlag_Object = MibTableColumn
portBsciAdminBlockedFlag = _PortBsciAdminBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 1),
    _PortBsciAdminBlockedFlag_Type()
)
portBsciAdminBlockedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminBlockedFlag.setStatus("mandatory")


class _PortBsciAdminConnector_Type(Integer32):
    """Custom type portBsciAdminConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortBsciAdminConnector_Type.__name__ = "Integer32"
_PortBsciAdminConnector_Object = MibTableColumn
portBsciAdminConnector = _PortBsciAdminConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 2),
    _PortBsciAdminConnector_Type()
)
portBsciAdminConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminConnector.setStatus("mandatory")


class _PortBsciAdminSpeed_Type(Integer32):
    """Custom type portBsciAdminSpeed based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 19200),
    )


_PortBsciAdminSpeed_Type.__name__ = "Integer32"
_PortBsciAdminSpeed_Object = MibTableColumn
portBsciAdminSpeed = _PortBsciAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 3),
    _PortBsciAdminSpeed_Type()
)
portBsciAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminSpeed.setStatus("mandatory")


class _PortBsciAdminRetransmitInterval_Type(Integer32):
    """Custom type portBsciAdminRetransmitInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_PortBsciAdminRetransmitInterval_Type.__name__ = "Integer32"
_PortBsciAdminRetransmitInterval_Object = MibTableColumn
portBsciAdminRetransmitInterval = _PortBsciAdminRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 4),
    _PortBsciAdminRetransmitInterval_Type()
)
portBsciAdminRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminRetransmitInterval.setStatus("mandatory")


class _PortBsciAdminMAXRetransmits_Type(Integer32):
    """Custom type portBsciAdminMAXRetransmits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PortBsciAdminMAXRetransmits_Type.__name__ = "Integer32"
_PortBsciAdminMAXRetransmits_Object = MibTableColumn
portBsciAdminMAXRetransmits = _PortBsciAdminMAXRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 5),
    _PortBsciAdminMAXRetransmits_Type()
)
portBsciAdminMAXRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminMAXRetransmits.setStatus("mandatory")


class _PortBsciAdminMaxBytesPerFrame_Type(Integer32):
    """Custom type portBsciAdminMaxBytesPerFrame based on Integer32"""
    defaultValue = 4105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 4105),
    )


_PortBsciAdminMaxBytesPerFrame_Type.__name__ = "Integer32"
_PortBsciAdminMaxBytesPerFrame_Object = MibTableColumn
portBsciAdminMaxBytesPerFrame = _PortBsciAdminMaxBytesPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 6),
    _PortBsciAdminMaxBytesPerFrame_Type()
)
portBsciAdminMaxBytesPerFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminMaxBytesPerFrame.setStatus("mandatory")


class _PortBsciAdminGenerateClock_Type(Integer32):
    """Custom type portBsciAdminGenerateClock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminGenerateClock_Type.__name__ = "Integer32"
_PortBsciAdminGenerateClock_Object = MibTableColumn
portBsciAdminGenerateClock = _PortBsciAdminGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 7),
    _PortBsciAdminGenerateClock_Type()
)
portBsciAdminGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminGenerateClock.setStatus("mandatory")


class _PortBsciAdminRcvClockFromDTE_Type(Integer32):
    """Custom type portBsciAdminRcvClockFromDTE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminRcvClockFromDTE_Type.__name__ = "Integer32"
_PortBsciAdminRcvClockFromDTE_Object = MibTableColumn
portBsciAdminRcvClockFromDTE = _PortBsciAdminRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 8),
    _PortBsciAdminRcvClockFromDTE_Type()
)
portBsciAdminRcvClockFromDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminRcvClockFromDTE.setStatus("mandatory")


class _PortBsciAdminPadType_Type(Integer32):
    """Custom type portBsciAdminPadType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 2),
          ("tpad", 1))
    )


_PortBsciAdminPadType_Type.__name__ = "Integer32"
_PortBsciAdminPadType_Object = MibTableColumn
portBsciAdminPadType = _PortBsciAdminPadType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 9),
    _PortBsciAdminPadType_Type()
)
portBsciAdminPadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminPadType.setStatus("mandatory")


class _PortBsciAdminUseEBCDIC_Type(Integer32):
    """Custom type portBsciAdminUseEBCDIC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminUseEBCDIC_Type.__name__ = "Integer32"
_PortBsciAdminUseEBCDIC_Object = MibTableColumn
portBsciAdminUseEBCDIC = _PortBsciAdminUseEBCDIC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 10),
    _PortBsciAdminUseEBCDIC_Type()
)
portBsciAdminUseEBCDIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminUseEBCDIC.setStatus("mandatory")


class _PortBsciAdminCallInfoInRequestPacket_Type(Integer32):
    """Custom type portBsciAdminCallInfoInRequestPacket based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminCallInfoInRequestPacket_Type.__name__ = "Integer32"
_PortBsciAdminCallInfoInRequestPacket_Object = MibTableColumn
portBsciAdminCallInfoInRequestPacket = _PortBsciAdminCallInfoInRequestPacket_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 11),
    _PortBsciAdminCallInfoInRequestPacket_Type()
)
portBsciAdminCallInfoInRequestPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminCallInfoInRequestPacket.setStatus("mandatory")


class _PortBsciAdminClearVCOnLastDeviceDown_Type(Integer32):
    """Custom type portBsciAdminClearVCOnLastDeviceDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminClearVCOnLastDeviceDown_Type.__name__ = "Integer32"
_PortBsciAdminClearVCOnLastDeviceDown_Object = MibTableColumn
portBsciAdminClearVCOnLastDeviceDown = _PortBsciAdminClearVCOnLastDeviceDown_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 12),
    _PortBsciAdminClearVCOnLastDeviceDown_Type()
)
portBsciAdminClearVCOnLastDeviceDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminClearVCOnLastDeviceDown.setStatus("mandatory")


class _PortBsciAdminTransTextSupported_Type(Integer32):
    """Custom type portBsciAdminTransTextSupported based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminTransTextSupported_Type.__name__ = "Integer32"
_PortBsciAdminTransTextSupported_Object = MibTableColumn
portBsciAdminTransTextSupported = _PortBsciAdminTransTextSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 13),
    _PortBsciAdminTransTextSupported_Type()
)
portBsciAdminTransTextSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminTransTextSupported.setStatus("mandatory")


class _PortBsciAdminEndToEndAck_Type(Integer32):
    """Custom type portBsciAdminEndToEndAck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminEndToEndAck_Type.__name__ = "Integer32"
_PortBsciAdminEndToEndAck_Object = MibTableColumn
portBsciAdminEndToEndAck = _PortBsciAdminEndToEndAck_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 14),
    _PortBsciAdminEndToEndAck_Type()
)
portBsciAdminEndToEndAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminEndToEndAck.setStatus("mandatory")


class _PortBsciAdminFullDuplex_Type(Integer32):
    """Custom type portBsciAdminFullDuplex based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminFullDuplex_Type.__name__ = "Integer32"
_PortBsciAdminFullDuplex_Object = MibTableColumn
portBsciAdminFullDuplex = _PortBsciAdminFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 15),
    _PortBsciAdminFullDuplex_Type()
)
portBsciAdminFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminFullDuplex.setStatus("mandatory")


class _PortBsciAdminMultidrop_Type(Integer32):
    """Custom type portBsciAdminMultidrop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminMultidrop_Type.__name__ = "Integer32"
_PortBsciAdminMultidrop_Object = MibTableColumn
portBsciAdminMultidrop = _PortBsciAdminMultidrop_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 16),
    _PortBsciAdminMultidrop_Type()
)
portBsciAdminMultidrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminMultidrop.setStatus("mandatory")


class _PortBsciAdminSlowPollRetryCount_Type(Integer32):
    """Custom type portBsciAdminSlowPollRetryCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_PortBsciAdminSlowPollRetryCount_Type.__name__ = "Integer32"
_PortBsciAdminSlowPollRetryCount_Object = MibTableColumn
portBsciAdminSlowPollRetryCount = _PortBsciAdminSlowPollRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 17),
    _PortBsciAdminSlowPollRetryCount_Type()
)
portBsciAdminSlowPollRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminSlowPollRetryCount.setStatus("mandatory")


class _PortBsciAdminSlowPollRetryFreq_Type(Integer32):
    """Custom type portBsciAdminSlowPollRetryFreq based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PortBsciAdminSlowPollRetryFreq_Type.__name__ = "Integer32"
_PortBsciAdminSlowPollRetryFreq_Object = MibTableColumn
portBsciAdminSlowPollRetryFreq = _PortBsciAdminSlowPollRetryFreq_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 18),
    _PortBsciAdminSlowPollRetryFreq_Type()
)
portBsciAdminSlowPollRetryFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminSlowPollRetryFreq.setStatus("mandatory")


class _PortBsciAdminStartSynchChars_Type(Integer32):
    """Custom type portBsciAdminStartSynchChars based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PortBsciAdminStartSynchChars_Type.__name__ = "Integer32"
_PortBsciAdminStartSynchChars_Object = MibTableColumn
portBsciAdminStartSynchChars = _PortBsciAdminStartSynchChars_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 19),
    _PortBsciAdminStartSynchChars_Type()
)
portBsciAdminStartSynchChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminStartSynchChars.setStatus("mandatory")


class _PortBsciAdminEndPadChars_Type(Integer32):
    """Custom type portBsciAdminEndPadChars based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PortBsciAdminEndPadChars_Type.__name__ = "Integer32"
_PortBsciAdminEndPadChars_Object = MibTableColumn
portBsciAdminEndPadChars = _PortBsciAdminEndPadChars_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 20),
    _PortBsciAdminEndPadChars_Type()
)
portBsciAdminEndPadChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminEndPadChars.setStatus("mandatory")


class _PortBsciAdminPollInterval_Type(Integer32):
    """Custom type portBsciAdminPollInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PortBsciAdminPollInterval_Type.__name__ = "Integer32"
_PortBsciAdminPollInterval_Object = MibTableColumn
portBsciAdminPollInterval = _PortBsciAdminPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 21),
    _PortBsciAdminPollInterval_Type()
)
portBsciAdminPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminPollInterval.setStatus("mandatory")


class _PortBsciAdminNoResponseTimer_Type(Integer32):
    """Custom type portBsciAdminNoResponseTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PortBsciAdminNoResponseTimer_Type.__name__ = "Integer32"
_PortBsciAdminNoResponseTimer_Object = MibTableColumn
portBsciAdminNoResponseTimer = _PortBsciAdminNoResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 22),
    _PortBsciAdminNoResponseTimer_Type()
)
portBsciAdminNoResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminNoResponseTimer.setStatus("mandatory")


class _PortBsciAdminNoResponseRetryCount_Type(Integer32):
    """Custom type portBsciAdminNoResponseRetryCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciAdminNoResponseRetryCount_Type.__name__ = "Integer32"
_PortBsciAdminNoResponseRetryCount_Object = MibTableColumn
portBsciAdminNoResponseRetryCount = _PortBsciAdminNoResponseRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 23),
    _PortBsciAdminNoResponseRetryCount_Type()
)
portBsciAdminNoResponseRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminNoResponseRetryCount.setStatus("mandatory")


class _PortBsciAdminErrorRetransmitCount_Type(Integer32):
    """Custom type portBsciAdminErrorRetransmitCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciAdminErrorRetransmitCount_Type.__name__ = "Integer32"
_PortBsciAdminErrorRetransmitCount_Object = MibTableColumn
portBsciAdminErrorRetransmitCount = _PortBsciAdminErrorRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 24),
    _PortBsciAdminErrorRetransmitCount_Type()
)
portBsciAdminErrorRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminErrorRetransmitCount.setStatus("mandatory")


class _PortBsciAdminNAKRetryCount_Type(Integer32):
    """Custom type portBsciAdminNAKRetryCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciAdminNAKRetryCount_Type.__name__ = "Integer32"
_PortBsciAdminNAKRetryCount_Object = MibTableColumn
portBsciAdminNAKRetryCount = _PortBsciAdminNAKRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 25),
    _PortBsciAdminNAKRetryCount_Type()
)
portBsciAdminNAKRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminNAKRetryCount.setStatus("mandatory")


class _PortBsciAdminBlockCheck_Type(Integer32):
    """Custom type portBsciAdminBlockCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("even-lrc", 2),
          ("odd-lrc", 3))
    )


_PortBsciAdminBlockCheck_Type.__name__ = "Integer32"
_PortBsciAdminBlockCheck_Object = MibTableColumn
portBsciAdminBlockCheck = _PortBsciAdminBlockCheck_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 26),
    _PortBsciAdminBlockCheck_Type()
)
portBsciAdminBlockCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminBlockCheck.setStatus("mandatory")


class _PortBsciAdminDataMode_Type(Integer32):
    """Custom type portBsciAdminDataMode based on Integer32"""
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
        *(("even-7bit", 2),
          ("none-8bit", 3),
          ("odd-7bit", 1))
    )


_PortBsciAdminDataMode_Type.__name__ = "Integer32"
_PortBsciAdminDataMode_Object = MibTableColumn
portBsciAdminDataMode = _PortBsciAdminDataMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 27),
    _PortBsciAdminDataMode_Type()
)
portBsciAdminDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminDataMode.setStatus("mandatory")
_PortBsciAdminRowStatus_Type = RowStatus
_PortBsciAdminRowStatus_Object = MibTableColumn
portBsciAdminRowStatus = _PortBsciAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 28),
    _PortBsciAdminRowStatus_Type()
)
portBsciAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminRowStatus.setStatus("mandatory")


class _PortBsciAdminAnswerNonConfigured_Type(Integer32):
    """Custom type portBsciAdminAnswerNonConfigured based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminAnswerNonConfigured_Type.__name__ = "Integer32"
_PortBsciAdminAnswerNonConfigured_Object = MibTableColumn
portBsciAdminAnswerNonConfigured = _PortBsciAdminAnswerNonConfigured_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 29),
    _PortBsciAdminAnswerNonConfigured_Type()
)
portBsciAdminAnswerNonConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminAnswerNonConfigured.setStatus("mandatory")


class _PortBsciAdminActivateConnectionWithoutPoll_Type(Integer32):
    """Custom type portBsciAdminActivateConnectionWithoutPoll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciAdminActivateConnectionWithoutPoll_Type.__name__ = "Integer32"
_PortBsciAdminActivateConnectionWithoutPoll_Object = MibTableColumn
portBsciAdminActivateConnectionWithoutPoll = _PortBsciAdminActivateConnectionWithoutPoll_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 1, 1, 30),
    _PortBsciAdminActivateConnectionWithoutPoll_Type()
)
portBsciAdminActivateConnectionWithoutPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBsciAdminActivateConnectionWithoutPoll.setStatus("mandatory")
_PortBsciOperTable_Object = MibTable
portBsciOperTable = _PortBsciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2)
)
if mibBuilder.loadTexts:
    portBsciOperTable.setStatus("mandatory")
_PortBsciOperEntry_Object = MibTableRow
portBsciOperEntry = _PortBsciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1)
)
portBsciOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portBsciOperEntry.setStatus("mandatory")


class _PortBsciOperBlockedFlag_Type(Integer32):
    """Custom type portBsciOperBlockedFlag based on Integer32"""
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


_PortBsciOperBlockedFlag_Type.__name__ = "Integer32"
_PortBsciOperBlockedFlag_Object = MibTableColumn
portBsciOperBlockedFlag = _PortBsciOperBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 1),
    _PortBsciOperBlockedFlag_Type()
)
portBsciOperBlockedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperBlockedFlag.setStatus("mandatory")


class _PortBsciOperConnector_Type(Integer32):
    """Custom type portBsciOperConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortBsciOperConnector_Type.__name__ = "Integer32"
_PortBsciOperConnector_Object = MibTableColumn
portBsciOperConnector = _PortBsciOperConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 2),
    _PortBsciOperConnector_Type()
)
portBsciOperConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperConnector.setStatus("mandatory")
_PortBsciOperSpeed_Type = Integer32
_PortBsciOperSpeed_Object = MibTableColumn
portBsciOperSpeed = _PortBsciOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 3),
    _PortBsciOperSpeed_Type()
)
portBsciOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperSpeed.setStatus("mandatory")


class _PortBsciOperRetransmitInterval_Type(Integer32):
    """Custom type portBsciOperRetransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_PortBsciOperRetransmitInterval_Type.__name__ = "Integer32"
_PortBsciOperRetransmitInterval_Object = MibTableColumn
portBsciOperRetransmitInterval = _PortBsciOperRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 4),
    _PortBsciOperRetransmitInterval_Type()
)
portBsciOperRetransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperRetransmitInterval.setStatus("mandatory")


class _PortBsciOperMAXRetransmits_Type(Integer32):
    """Custom type portBsciOperMAXRetransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PortBsciOperMAXRetransmits_Type.__name__ = "Integer32"
_PortBsciOperMAXRetransmits_Object = MibTableColumn
portBsciOperMAXRetransmits = _PortBsciOperMAXRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 5),
    _PortBsciOperMAXRetransmits_Type()
)
portBsciOperMAXRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperMAXRetransmits.setStatus("mandatory")


class _PortBsciOperMaxBytesPerFrame_Type(Integer32):
    """Custom type portBsciOperMaxBytesPerFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 4105),
    )


_PortBsciOperMaxBytesPerFrame_Type.__name__ = "Integer32"
_PortBsciOperMaxBytesPerFrame_Object = MibTableColumn
portBsciOperMaxBytesPerFrame = _PortBsciOperMaxBytesPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 6),
    _PortBsciOperMaxBytesPerFrame_Type()
)
portBsciOperMaxBytesPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperMaxBytesPerFrame.setStatus("mandatory")


class _PortBsciOperGenerateClock_Type(Integer32):
    """Custom type portBsciOperGenerateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperGenerateClock_Type.__name__ = "Integer32"
_PortBsciOperGenerateClock_Object = MibTableColumn
portBsciOperGenerateClock = _PortBsciOperGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 7),
    _PortBsciOperGenerateClock_Type()
)
portBsciOperGenerateClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperGenerateClock.setStatus("mandatory")


class _PortBsciOperRcvClockFromDTE_Type(Integer32):
    """Custom type portBsciOperRcvClockFromDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperRcvClockFromDTE_Type.__name__ = "Integer32"
_PortBsciOperRcvClockFromDTE_Object = MibTableColumn
portBsciOperRcvClockFromDTE = _PortBsciOperRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 8),
    _PortBsciOperRcvClockFromDTE_Type()
)
portBsciOperRcvClockFromDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperRcvClockFromDTE.setStatus("mandatory")


class _PortBsciOperPadType_Type(Integer32):
    """Custom type portBsciOperPadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 2),
          ("tpad", 1))
    )


_PortBsciOperPadType_Type.__name__ = "Integer32"
_PortBsciOperPadType_Object = MibTableColumn
portBsciOperPadType = _PortBsciOperPadType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 9),
    _PortBsciOperPadType_Type()
)
portBsciOperPadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperPadType.setStatus("mandatory")


class _PortBsciOperUseEBCDIC_Type(Integer32):
    """Custom type portBsciOperUseEBCDIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperUseEBCDIC_Type.__name__ = "Integer32"
_PortBsciOperUseEBCDIC_Object = MibTableColumn
portBsciOperUseEBCDIC = _PortBsciOperUseEBCDIC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 10),
    _PortBsciOperUseEBCDIC_Type()
)
portBsciOperUseEBCDIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperUseEBCDIC.setStatus("mandatory")


class _PortBsciOperCallInfoInRequestPacket_Type(Integer32):
    """Custom type portBsciOperCallInfoInRequestPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperCallInfoInRequestPacket_Type.__name__ = "Integer32"
_PortBsciOperCallInfoInRequestPacket_Object = MibTableColumn
portBsciOperCallInfoInRequestPacket = _PortBsciOperCallInfoInRequestPacket_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 11),
    _PortBsciOperCallInfoInRequestPacket_Type()
)
portBsciOperCallInfoInRequestPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperCallInfoInRequestPacket.setStatus("mandatory")


class _PortBsciOperClearVCOnLastDeviceDown_Type(Integer32):
    """Custom type portBsciOperClearVCOnLastDeviceDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperClearVCOnLastDeviceDown_Type.__name__ = "Integer32"
_PortBsciOperClearVCOnLastDeviceDown_Object = MibTableColumn
portBsciOperClearVCOnLastDeviceDown = _PortBsciOperClearVCOnLastDeviceDown_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 12),
    _PortBsciOperClearVCOnLastDeviceDown_Type()
)
portBsciOperClearVCOnLastDeviceDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperClearVCOnLastDeviceDown.setStatus("mandatory")


class _PortBsciOperTransTextSupported_Type(Integer32):
    """Custom type portBsciOperTransTextSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperTransTextSupported_Type.__name__ = "Integer32"
_PortBsciOperTransTextSupported_Object = MibTableColumn
portBsciOperTransTextSupported = _PortBsciOperTransTextSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 13),
    _PortBsciOperTransTextSupported_Type()
)
portBsciOperTransTextSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperTransTextSupported.setStatus("mandatory")


class _PortBsciOperEndToEndAck_Type(Integer32):
    """Custom type portBsciOperEndToEndAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperEndToEndAck_Type.__name__ = "Integer32"
_PortBsciOperEndToEndAck_Object = MibTableColumn
portBsciOperEndToEndAck = _PortBsciOperEndToEndAck_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 14),
    _PortBsciOperEndToEndAck_Type()
)
portBsciOperEndToEndAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperEndToEndAck.setStatus("mandatory")


class _PortBsciOperFullDuplex_Type(Integer32):
    """Custom type portBsciOperFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperFullDuplex_Type.__name__ = "Integer32"
_PortBsciOperFullDuplex_Object = MibTableColumn
portBsciOperFullDuplex = _PortBsciOperFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 15),
    _PortBsciOperFullDuplex_Type()
)
portBsciOperFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperFullDuplex.setStatus("mandatory")


class _PortBsciOperMultidrop_Type(Integer32):
    """Custom type portBsciOperMultidrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperMultidrop_Type.__name__ = "Integer32"
_PortBsciOperMultidrop_Object = MibTableColumn
portBsciOperMultidrop = _PortBsciOperMultidrop_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 16),
    _PortBsciOperMultidrop_Type()
)
portBsciOperMultidrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperMultidrop.setStatus("mandatory")


class _PortBsciOperSlowPollRetryCount_Type(Integer32):
    """Custom type portBsciOperSlowPollRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_PortBsciOperSlowPollRetryCount_Type.__name__ = "Integer32"
_PortBsciOperSlowPollRetryCount_Object = MibTableColumn
portBsciOperSlowPollRetryCount = _PortBsciOperSlowPollRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 17),
    _PortBsciOperSlowPollRetryCount_Type()
)
portBsciOperSlowPollRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperSlowPollRetryCount.setStatus("mandatory")


class _PortBsciOperSlowPollRetryFreq_Type(Integer32):
    """Custom type portBsciOperSlowPollRetryFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PortBsciOperSlowPollRetryFreq_Type.__name__ = "Integer32"
_PortBsciOperSlowPollRetryFreq_Object = MibTableColumn
portBsciOperSlowPollRetryFreq = _PortBsciOperSlowPollRetryFreq_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 18),
    _PortBsciOperSlowPollRetryFreq_Type()
)
portBsciOperSlowPollRetryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperSlowPollRetryFreq.setStatus("mandatory")


class _PortBsciOperStartSynchChars_Type(Integer32):
    """Custom type portBsciOperStartSynchChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PortBsciOperStartSynchChars_Type.__name__ = "Integer32"
_PortBsciOperStartSynchChars_Object = MibTableColumn
portBsciOperStartSynchChars = _PortBsciOperStartSynchChars_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 19),
    _PortBsciOperStartSynchChars_Type()
)
portBsciOperStartSynchChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperStartSynchChars.setStatus("mandatory")


class _PortBsciOperEndPadChars_Type(Integer32):
    """Custom type portBsciOperEndPadChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PortBsciOperEndPadChars_Type.__name__ = "Integer32"
_PortBsciOperEndPadChars_Object = MibTableColumn
portBsciOperEndPadChars = _PortBsciOperEndPadChars_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 20),
    _PortBsciOperEndPadChars_Type()
)
portBsciOperEndPadChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperEndPadChars.setStatus("mandatory")


class _PortBsciOperPollInterval_Type(Integer32):
    """Custom type portBsciOperPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PortBsciOperPollInterval_Type.__name__ = "Integer32"
_PortBsciOperPollInterval_Object = MibTableColumn
portBsciOperPollInterval = _PortBsciOperPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 21),
    _PortBsciOperPollInterval_Type()
)
portBsciOperPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperPollInterval.setStatus("mandatory")


class _PortBsciOperNoResponseTimer_Type(Integer32):
    """Custom type portBsciOperNoResponseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PortBsciOperNoResponseTimer_Type.__name__ = "Integer32"
_PortBsciOperNoResponseTimer_Object = MibTableColumn
portBsciOperNoResponseTimer = _PortBsciOperNoResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 22),
    _PortBsciOperNoResponseTimer_Type()
)
portBsciOperNoResponseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperNoResponseTimer.setStatus("mandatory")


class _PortBsciOperNoResponseRetryCount_Type(Integer32):
    """Custom type portBsciOperNoResponseRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciOperNoResponseRetryCount_Type.__name__ = "Integer32"
_PortBsciOperNoResponseRetryCount_Object = MibTableColumn
portBsciOperNoResponseRetryCount = _PortBsciOperNoResponseRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 23),
    _PortBsciOperNoResponseRetryCount_Type()
)
portBsciOperNoResponseRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperNoResponseRetryCount.setStatus("mandatory")


class _PortBsciOperErrorRetransmitCount_Type(Integer32):
    """Custom type portBsciOperErrorRetransmitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciOperErrorRetransmitCount_Type.__name__ = "Integer32"
_PortBsciOperErrorRetransmitCount_Object = MibTableColumn
portBsciOperErrorRetransmitCount = _PortBsciOperErrorRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 24),
    _PortBsciOperErrorRetransmitCount_Type()
)
portBsciOperErrorRetransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperErrorRetransmitCount.setStatus("mandatory")


class _PortBsciOperNAKRetryCount_Type(Integer32):
    """Custom type portBsciOperNAKRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBsciOperNAKRetryCount_Type.__name__ = "Integer32"
_PortBsciOperNAKRetryCount_Object = MibTableColumn
portBsciOperNAKRetryCount = _PortBsciOperNAKRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 25),
    _PortBsciOperNAKRetryCount_Type()
)
portBsciOperNAKRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperNAKRetryCount.setStatus("mandatory")


class _PortBsciOperBlockCheck_Type(Integer32):
    """Custom type portBsciOperBlockCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("even-lrc", 2),
          ("odd-lrc", 3))
    )


_PortBsciOperBlockCheck_Type.__name__ = "Integer32"
_PortBsciOperBlockCheck_Object = MibTableColumn
portBsciOperBlockCheck = _PortBsciOperBlockCheck_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 26),
    _PortBsciOperBlockCheck_Type()
)
portBsciOperBlockCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperBlockCheck.setStatus("mandatory")


class _PortBsciOperDataMode_Type(Integer32):
    """Custom type portBsciOperDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even-7bit", 2),
          ("none-8bit", 3),
          ("odd-7bit", 1))
    )


_PortBsciOperDataMode_Type.__name__ = "Integer32"
_PortBsciOperDataMode_Object = MibTableColumn
portBsciOperDataMode = _PortBsciOperDataMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 27),
    _PortBsciOperDataMode_Type()
)
portBsciOperDataMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperDataMode.setStatus("mandatory")


class _PortBsciOperAnswerNonConfigured_Type(Integer32):
    """Custom type portBsciOperAnswerNonConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperAnswerNonConfigured_Type.__name__ = "Integer32"
_PortBsciOperAnswerNonConfigured_Object = MibTableColumn
portBsciOperAnswerNonConfigured = _PortBsciOperAnswerNonConfigured_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 28),
    _PortBsciOperAnswerNonConfigured_Type()
)
portBsciOperAnswerNonConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperAnswerNonConfigured.setStatus("mandatory")


class _PortBsciOperActivateConnectionWithoutPoll_Type(Integer32):
    """Custom type portBsciOperActivateConnectionWithoutPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortBsciOperActivateConnectionWithoutPoll_Type.__name__ = "Integer32"
_PortBsciOperActivateConnectionWithoutPoll_Object = MibTableColumn
portBsciOperActivateConnectionWithoutPoll = _PortBsciOperActivateConnectionWithoutPoll_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 2, 1, 29),
    _PortBsciOperActivateConnectionWithoutPoll_Type()
)
portBsciOperActivateConnectionWithoutPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBsciOperActivateConnectionWithoutPoll.setStatus("mandatory")
_BsciSubscrAdminTable_Object = MibTable
bsciSubscrAdminTable = _BsciSubscrAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3)
)
if mibBuilder.loadTexts:
    bsciSubscrAdminTable.setStatus("mandatory")
_BsciSubscrAdminEntry_Object = MibTableRow
bsciSubscrAdminEntry = _BsciSubscrAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1)
)
bsciSubscrAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciSubscrAdminSequence"),
)
if mibBuilder.loadTexts:
    bsciSubscrAdminEntry.setStatus("mandatory")


class _BsciSubscrAdminSequence_Type(Integer32):
    """Custom type bsciSubscrAdminSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BsciSubscrAdminSequence_Type.__name__ = "Integer32"
_BsciSubscrAdminSequence_Object = MibTableColumn
bsciSubscrAdminSequence = _BsciSubscrAdminSequence_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 1),
    _BsciSubscrAdminSequence_Type()
)
bsciSubscrAdminSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrAdminSequence.setStatus("mandatory")
_BsciSubscrAdminLocalID_Type = NlSubscriberAddress
_BsciSubscrAdminLocalID_Object = MibTableColumn
bsciSubscrAdminLocalID = _BsciSubscrAdminLocalID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 2),
    _BsciSubscrAdminLocalID_Type()
)
bsciSubscrAdminLocalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminLocalID.setStatus("mandatory")
_BsciSubscrAdminRemoteID_Type = NlSubscriberAddress
_BsciSubscrAdminRemoteID_Object = MibTableColumn
bsciSubscrAdminRemoteID = _BsciSubscrAdminRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 3),
    _BsciSubscrAdminRemoteID_Type()
)
bsciSubscrAdminRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminRemoteID.setStatus("mandatory")


class _BsciSubscrAdminAutocall_Type(Integer32):
    """Custom type bsciSubscrAdminAutocall based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciSubscrAdminAutocall_Type.__name__ = "Integer32"
_BsciSubscrAdminAutocall_Object = MibTableColumn
bsciSubscrAdminAutocall = _BsciSubscrAdminAutocall_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 4),
    _BsciSubscrAdminAutocall_Type()
)
bsciSubscrAdminAutocall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminAutocall.setStatus("mandatory")


class _BsciSubscrAdminAutocallRtyTimer_Type(Integer32):
    """Custom type bsciSubscrAdminAutocallRtyTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 255),
    )


_BsciSubscrAdminAutocallRtyTimer_Type.__name__ = "Integer32"
_BsciSubscrAdminAutocallRtyTimer_Object = MibTableColumn
bsciSubscrAdminAutocallRtyTimer = _BsciSubscrAdminAutocallRtyTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 5),
    _BsciSubscrAdminAutocallRtyTimer_Type()
)
bsciSubscrAdminAutocallRtyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminAutocallRtyTimer.setStatus("mandatory")


class _BsciSubscrAdminAutocallMaxRtry_Type(Integer32):
    """Custom type bsciSubscrAdminAutocallMaxRtry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciSubscrAdminAutocallMaxRtry_Type.__name__ = "Integer32"
_BsciSubscrAdminAutocallMaxRtry_Object = MibTableColumn
bsciSubscrAdminAutocallMaxRtry = _BsciSubscrAdminAutocallMaxRtry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 6),
    _BsciSubscrAdminAutocallMaxRtry_Type()
)
bsciSubscrAdminAutocallMaxRtry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminAutocallMaxRtry.setStatus("mandatory")


class _BsciSubscrAdminConnectionID_Type(Integer32):
    """Custom type bsciSubscrAdminConnectionID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciSubscrAdminConnectionID_Type.__name__ = "Integer32"
_BsciSubscrAdminConnectionID_Object = MibTableColumn
bsciSubscrAdminConnectionID = _BsciSubscrAdminConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 7),
    _BsciSubscrAdminConnectionID_Type()
)
bsciSubscrAdminConnectionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminConnectionID.setStatus("mandatory")
_BsciSubscrAdminRowStatus_Type = RowStatus
_BsciSubscrAdminRowStatus_Object = MibTableColumn
bsciSubscrAdminRowStatus = _BsciSubscrAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 3, 1, 8),
    _BsciSubscrAdminRowStatus_Type()
)
bsciSubscrAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciSubscrAdminRowStatus.setStatus("mandatory")
_BsciSubscrOperTable_Object = MibTable
bsciSubscrOperTable = _BsciSubscrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4)
)
if mibBuilder.loadTexts:
    bsciSubscrOperTable.setStatus("mandatory")
_BsciSubscrOperEntry_Object = MibTableRow
bsciSubscrOperEntry = _BsciSubscrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1)
)
bsciSubscrOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciSubscrOperSequence"),
)
if mibBuilder.loadTexts:
    bsciSubscrOperEntry.setStatus("mandatory")


class _BsciSubscrOperSequence_Type(Integer32):
    """Custom type bsciSubscrOperSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BsciSubscrOperSequence_Type.__name__ = "Integer32"
_BsciSubscrOperSequence_Object = MibTableColumn
bsciSubscrOperSequence = _BsciSubscrOperSequence_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 1),
    _BsciSubscrOperSequence_Type()
)
bsciSubscrOperSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperSequence.setStatus("mandatory")
_BsciSubscrOperLocalID_Type = NlSubscriberAddress
_BsciSubscrOperLocalID_Object = MibTableColumn
bsciSubscrOperLocalID = _BsciSubscrOperLocalID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 2),
    _BsciSubscrOperLocalID_Type()
)
bsciSubscrOperLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperLocalID.setStatus("mandatory")
_BsciSubscrOperRemoteID_Type = NlSubscriberAddress
_BsciSubscrOperRemoteID_Object = MibTableColumn
bsciSubscrOperRemoteID = _BsciSubscrOperRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 3),
    _BsciSubscrOperRemoteID_Type()
)
bsciSubscrOperRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperRemoteID.setStatus("mandatory")


class _BsciSubscrOperAutocall_Type(Integer32):
    """Custom type bsciSubscrOperAutocall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciSubscrOperAutocall_Type.__name__ = "Integer32"
_BsciSubscrOperAutocall_Object = MibTableColumn
bsciSubscrOperAutocall = _BsciSubscrOperAutocall_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 4),
    _BsciSubscrOperAutocall_Type()
)
bsciSubscrOperAutocall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperAutocall.setStatus("mandatory")


class _BsciSubscrOperAutocallRtyTimer_Type(Integer32):
    """Custom type bsciSubscrOperAutocallRtyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 255),
    )


_BsciSubscrOperAutocallRtyTimer_Type.__name__ = "Integer32"
_BsciSubscrOperAutocallRtyTimer_Object = MibTableColumn
bsciSubscrOperAutocallRtyTimer = _BsciSubscrOperAutocallRtyTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 5),
    _BsciSubscrOperAutocallRtyTimer_Type()
)
bsciSubscrOperAutocallRtyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperAutocallRtyTimer.setStatus("mandatory")


class _BsciSubscrOperAutocallMaxRtry_Type(Integer32):
    """Custom type bsciSubscrOperAutocallMaxRtry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciSubscrOperAutocallMaxRtry_Type.__name__ = "Integer32"
_BsciSubscrOperAutocallMaxRtry_Object = MibTableColumn
bsciSubscrOperAutocallMaxRtry = _BsciSubscrOperAutocallMaxRtry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 6),
    _BsciSubscrOperAutocallMaxRtry_Type()
)
bsciSubscrOperAutocallMaxRtry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperAutocallMaxRtry.setStatus("mandatory")


class _BsciSubscrOperConnectionID_Type(Integer32):
    """Custom type bsciSubscrOperConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciSubscrOperConnectionID_Type.__name__ = "Integer32"
_BsciSubscrOperConnectionID_Object = MibTableColumn
bsciSubscrOperConnectionID = _BsciSubscrOperConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 4, 1, 7),
    _BsciSubscrOperConnectionID_Type()
)
bsciSubscrOperConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciSubscrOperConnectionID.setStatus("mandatory")
_BsciDevAdminTable_Object = MibTable
bsciDevAdminTable = _BsciDevAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5)
)
if mibBuilder.loadTexts:
    bsciDevAdminTable.setStatus("mandatory")
_BsciDevAdminEntry_Object = MibTableRow
bsciDevAdminEntry = _BsciDevAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1)
)
bsciDevAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciDevAdminControlUnitID"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciDevAdminDeviceUnitID"),
)
if mibBuilder.loadTexts:
    bsciDevAdminEntry.setStatus("mandatory")


class _BsciDevAdminControlUnitID_Type(Integer32):
    """Custom type bsciDevAdminControlUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BsciDevAdminControlUnitID_Type.__name__ = "Integer32"
_BsciDevAdminControlUnitID_Object = MibTableColumn
bsciDevAdminControlUnitID = _BsciDevAdminControlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 1),
    _BsciDevAdminControlUnitID_Type()
)
bsciDevAdminControlUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevAdminControlUnitID.setStatus("mandatory")


class _BsciDevAdminDeviceUnitID_Type(Integer32):
    """Custom type bsciDevAdminDeviceUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BsciDevAdminDeviceUnitID_Type.__name__ = "Integer32"
_BsciDevAdminDeviceUnitID_Object = MibTableColumn
bsciDevAdminDeviceUnitID = _BsciDevAdminDeviceUnitID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 2),
    _BsciDevAdminDeviceUnitID_Type()
)
bsciDevAdminDeviceUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevAdminDeviceUnitID.setStatus("mandatory")


class _BsciDevAdminConnectionID_Type(Integer32):
    """Custom type bsciDevAdminConnectionID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciDevAdminConnectionID_Type.__name__ = "Integer32"
_BsciDevAdminConnectionID_Object = MibTableColumn
bsciDevAdminConnectionID = _BsciDevAdminConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 3),
    _BsciDevAdminConnectionID_Type()
)
bsciDevAdminConnectionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminConnectionID.setStatus("mandatory")


class _BsciDevAdminSingleUserVC_Type(Integer32):
    """Custom type bsciDevAdminSingleUserVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevAdminSingleUserVC_Type.__name__ = "Integer32"
_BsciDevAdminSingleUserVC_Object = MibTableColumn
bsciDevAdminSingleUserVC = _BsciDevAdminSingleUserVC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 4),
    _BsciDevAdminSingleUserVC_Type()
)
bsciDevAdminSingleUserVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminSingleUserVC.setStatus("mandatory")


class _BsciDevAdminTransTextSupported_Type(Integer32):
    """Custom type bsciDevAdminTransTextSupported based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevAdminTransTextSupported_Type.__name__ = "Integer32"
_BsciDevAdminTransTextSupported_Object = MibTableColumn
bsciDevAdminTransTextSupported = _BsciDevAdminTransTextSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 5),
    _BsciDevAdminTransTextSupported_Type()
)
bsciDevAdminTransTextSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminTransTextSupported.setStatus("mandatory")


class _BsciDevAdminPrinterAttached_Type(Integer32):
    """Custom type bsciDevAdminPrinterAttached based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevAdminPrinterAttached_Type.__name__ = "Integer32"
_BsciDevAdminPrinterAttached_Object = MibTableColumn
bsciDevAdminPrinterAttached = _BsciDevAdminPrinterAttached_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 6),
    _BsciDevAdminPrinterAttached_Type()
)
bsciDevAdminPrinterAttached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminPrinterAttached.setStatus("mandatory")
_BsciDevAdminRowStatus_Type = RowStatus
_BsciDevAdminRowStatus_Object = MibTableColumn
bsciDevAdminRowStatus = _BsciDevAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 7),
    _BsciDevAdminRowStatus_Type()
)
bsciDevAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminRowStatus.setStatus("mandatory")


class _BsciDevAdminDisableStatusRequest_Type(Integer32):
    """Custom type bsciDevAdminDisableStatusRequest based on Integer32"""
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
        *(("always-active", 3),
          ("none", 2),
          ("normal", 1))
    )


_BsciDevAdminDisableStatusRequest_Type.__name__ = "Integer32"
_BsciDevAdminDisableStatusRequest_Object = MibTableColumn
bsciDevAdminDisableStatusRequest = _BsciDevAdminDisableStatusRequest_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 5, 1, 8),
    _BsciDevAdminDisableStatusRequest_Type()
)
bsciDevAdminDisableStatusRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsciDevAdminDisableStatusRequest.setStatus("mandatory")
_BsciDevOperTable_Object = MibTable
bsciDevOperTable = _BsciDevOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6)
)
if mibBuilder.loadTexts:
    bsciDevOperTable.setStatus("mandatory")
_BsciDevOperEntry_Object = MibTableRow
bsciDevOperEntry = _BsciDevOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1)
)
bsciDevOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciDevOperControlUnitID"),
    (0, "NETLINK-SPECIFIC-MIB", "bsciDevOperDeviceUnitID"),
)
if mibBuilder.loadTexts:
    bsciDevOperEntry.setStatus("mandatory")


class _BsciDevOperControlUnitID_Type(Integer32):
    """Custom type bsciDevOperControlUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BsciDevOperControlUnitID_Type.__name__ = "Integer32"
_BsciDevOperControlUnitID_Object = MibTableColumn
bsciDevOperControlUnitID = _BsciDevOperControlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 1),
    _BsciDevOperControlUnitID_Type()
)
bsciDevOperControlUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperControlUnitID.setStatus("mandatory")


class _BsciDevOperDeviceUnitID_Type(Integer32):
    """Custom type bsciDevOperDeviceUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BsciDevOperDeviceUnitID_Type.__name__ = "Integer32"
_BsciDevOperDeviceUnitID_Object = MibTableColumn
bsciDevOperDeviceUnitID = _BsciDevOperDeviceUnitID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 2),
    _BsciDevOperDeviceUnitID_Type()
)
bsciDevOperDeviceUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperDeviceUnitID.setStatus("mandatory")


class _BsciDevOperConnectionID_Type(Integer32):
    """Custom type bsciDevOperConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsciDevOperConnectionID_Type.__name__ = "Integer32"
_BsciDevOperConnectionID_Object = MibTableColumn
bsciDevOperConnectionID = _BsciDevOperConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 3),
    _BsciDevOperConnectionID_Type()
)
bsciDevOperConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperConnectionID.setStatus("mandatory")


class _BsciDevOperSingleUserVC_Type(Integer32):
    """Custom type bsciDevOperSingleUserVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevOperSingleUserVC_Type.__name__ = "Integer32"
_BsciDevOperSingleUserVC_Object = MibTableColumn
bsciDevOperSingleUserVC = _BsciDevOperSingleUserVC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 4),
    _BsciDevOperSingleUserVC_Type()
)
bsciDevOperSingleUserVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperSingleUserVC.setStatus("mandatory")


class _BsciDevOperTransTextSupported_Type(Integer32):
    """Custom type bsciDevOperTransTextSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevOperTransTextSupported_Type.__name__ = "Integer32"
_BsciDevOperTransTextSupported_Object = MibTableColumn
bsciDevOperTransTextSupported = _BsciDevOperTransTextSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 5),
    _BsciDevOperTransTextSupported_Type()
)
bsciDevOperTransTextSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperTransTextSupported.setStatus("mandatory")


class _BsciDevOperPrinterAttached_Type(Integer32):
    """Custom type bsciDevOperPrinterAttached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BsciDevOperPrinterAttached_Type.__name__ = "Integer32"
_BsciDevOperPrinterAttached_Object = MibTableColumn
bsciDevOperPrinterAttached = _BsciDevOperPrinterAttached_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 6),
    _BsciDevOperPrinterAttached_Type()
)
bsciDevOperPrinterAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperPrinterAttached.setStatus("mandatory")


class _BsciDevOperDisableStatusRequest_Type(Integer32):
    """Custom type bsciDevOperDisableStatusRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always-active", 3),
          ("none", 2),
          ("normal", 1))
    )


_BsciDevOperDisableStatusRequest_Type.__name__ = "Integer32"
_BsciDevOperDisableStatusRequest_Object = MibTableColumn
bsciDevOperDisableStatusRequest = _BsciDevOperDisableStatusRequest_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 4, 6, 1, 7),
    _BsciDevOperDisableStatusRequest_Type()
)
bsciDevOperDisableStatusRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsciDevOperDisableStatusRequest.setStatus("mandatory")
_PortSdlcGroup_ObjectIdentity = ObjectIdentity
portSdlcGroup = _PortSdlcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5)
)
_PortSdlcAdminTable_Object = MibTable
portSdlcAdminTable = _PortSdlcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1)
)
if mibBuilder.loadTexts:
    portSdlcAdminTable.setStatus("mandatory")
_PortSdlcAdminEntry_Object = MibTableRow
portSdlcAdminEntry = _PortSdlcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1)
)
portSdlcAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portSdlcAdminEntry.setStatus("mandatory")


class _PortSdlcAdminCommit_Type(Integer32):
    """Custom type portSdlcAdminCommit based on Integer32"""
    defaultValue = 0


_PortSdlcAdminCommit_Object = MibTableColumn
portSdlcAdminCommit = _PortSdlcAdminCommit_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 1),
    _PortSdlcAdminCommit_Type()
)
portSdlcAdminCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminCommit.setStatus("obsolete")


class _PortSdlcAdminMAXRetries_Type(Integer32):
    """Custom type portSdlcAdminMAXRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PortSdlcAdminMAXRetries_Type.__name__ = "Integer32"
_PortSdlcAdminMAXRetries_Object = MibTableColumn
portSdlcAdminMAXRetries = _PortSdlcAdminMAXRetries_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 2),
    _PortSdlcAdminMAXRetries_Type()
)
portSdlcAdminMAXRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminMAXRetries.setStatus("mandatory")


class _PortSdlcAdminMAXOut_Type(Integer32):
    """Custom type portSdlcAdminMAXOut based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PortSdlcAdminMAXOut_Type.__name__ = "Integer32"
_PortSdlcAdminMAXOut_Object = MibTableColumn
portSdlcAdminMAXOut = _PortSdlcAdminMAXOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 3),
    _PortSdlcAdminMAXOut_Type()
)
portSdlcAdminMAXOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminMAXOut.setStatus("mandatory")


class _PortSdlcAdminPadType_Type(Integer32):
    """Custom type portSdlcAdminPadType based on Integer32"""
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
        *(("hpad", 3),
          ("npad", 4),
          ("tpad", 2),
          ("xpad", 1))
    )


_PortSdlcAdminPadType_Type.__name__ = "Integer32"
_PortSdlcAdminPadType_Object = MibTableColumn
portSdlcAdminPadType = _PortSdlcAdminPadType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 4),
    _PortSdlcAdminPadType_Type()
)
portSdlcAdminPadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminPadType.setStatus("mandatory")


class _PortSdlcAdminGenerateClock_Type(Integer32):
    """Custom type portSdlcAdminGenerateClock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcAdminGenerateClock_Type.__name__ = "Integer32"
_PortSdlcAdminGenerateClock_Object = MibTableColumn
portSdlcAdminGenerateClock = _PortSdlcAdminGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 5),
    _PortSdlcAdminGenerateClock_Type()
)
portSdlcAdminGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminGenerateClock.setStatus("mandatory")


class _PortSdlcAdminRcvClockFromDTE_Type(Integer32):
    """Custom type portSdlcAdminRcvClockFromDTE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcAdminRcvClockFromDTE_Type.__name__ = "Integer32"
_PortSdlcAdminRcvClockFromDTE_Object = MibTableColumn
portSdlcAdminRcvClockFromDTE = _PortSdlcAdminRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 6),
    _PortSdlcAdminRcvClockFromDTE_Type()
)
portSdlcAdminRcvClockFromDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminRcvClockFromDTE.setStatus("mandatory")


class _PortSdlcAdminNrz_Type(Integer32):
    """Custom type portSdlcAdminNrz based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcAdminNrz_Type.__name__ = "Integer32"
_PortSdlcAdminNrz_Object = MibTableColumn
portSdlcAdminNrz = _PortSdlcAdminNrz_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 7),
    _PortSdlcAdminNrz_Type()
)
portSdlcAdminNrz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminNrz.setStatus("mandatory")


class _PortSdlcAdminPacketSize_Type(Integer32):
    """Custom type portSdlcAdminPacketSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_PortSdlcAdminPacketSize_Type.__name__ = "Integer32"
_PortSdlcAdminPacketSize_Object = MibTableColumn
portSdlcAdminPacketSize = _PortSdlcAdminPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 8),
    _PortSdlcAdminPacketSize_Type()
)
portSdlcAdminPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminPacketSize.setStatus("mandatory")


class _PortSdlcAdminDisableRequestDisconnect_Type(Integer32):
    """Custom type portSdlcAdminDisableRequestDisconnect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcAdminDisableRequestDisconnect_Type.__name__ = "Integer32"
_PortSdlcAdminDisableRequestDisconnect_Object = MibTableColumn
portSdlcAdminDisableRequestDisconnect = _PortSdlcAdminDisableRequestDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 9),
    _PortSdlcAdminDisableRequestDisconnect_Type()
)
portSdlcAdminDisableRequestDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminDisableRequestDisconnect.setStatus("mandatory")


class _PortSdlcAdminLPDASupport_Type(Integer32):
    """Custom type portSdlcAdminLPDASupport based on Integer32"""
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
        *(("lpda-1", 2),
          ("lpda-2", 3),
          ("none", 1))
    )


_PortSdlcAdminLPDASupport_Type.__name__ = "Integer32"
_PortSdlcAdminLPDASupport_Object = MibTableColumn
portSdlcAdminLPDASupport = _PortSdlcAdminLPDASupport_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 10),
    _PortSdlcAdminLPDASupport_Type()
)
portSdlcAdminLPDASupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminLPDASupport.setStatus("mandatory")


class _PortSdlcAdminConnector_Type(Integer32):
    """Custom type portSdlcAdminConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortSdlcAdminConnector_Type.__name__ = "Integer32"
_PortSdlcAdminConnector_Object = MibTableColumn
portSdlcAdminConnector = _PortSdlcAdminConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 11),
    _PortSdlcAdminConnector_Type()
)
portSdlcAdminConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminConnector.setStatus("mandatory")


class _PortSdlcAdminSpeed_Type(Integer32):
    """Custom type portSdlcAdminSpeed based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 2048000),
    )


_PortSdlcAdminSpeed_Type.__name__ = "Integer32"
_PortSdlcAdminSpeed_Object = MibTableColumn
portSdlcAdminSpeed = _PortSdlcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 12),
    _PortSdlcAdminSpeed_Type()
)
portSdlcAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminSpeed.setStatus("mandatory")
_PortSdlcAdminRowStatus_Type = RowStatus
_PortSdlcAdminRowStatus_Object = MibTableColumn
portSdlcAdminRowStatus = _PortSdlcAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 13),
    _PortSdlcAdminRowStatus_Type()
)
portSdlcAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminRowStatus.setStatus("mandatory")


class _PortSdlcAdminIdleFillChar_Type(Integer32):
    """Custom type portSdlcAdminIdleFillChar based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex-7e", 2),
          ("hex-ff", 1))
    )


_PortSdlcAdminIdleFillChar_Type.__name__ = "Integer32"
_PortSdlcAdminIdleFillChar_Object = MibTableColumn
portSdlcAdminIdleFillChar = _PortSdlcAdminIdleFillChar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 14),
    _PortSdlcAdminIdleFillChar_Type()
)
portSdlcAdminIdleFillChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminIdleFillChar.setStatus("mandatory")


class _PortSdlcAdminInactivityTimer_Type(Integer32):
    """Custom type portSdlcAdminInactivityTimer based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 250),
    )


_PortSdlcAdminInactivityTimer_Type.__name__ = "Integer32"
_PortSdlcAdminInactivityTimer_Object = MibTableColumn
portSdlcAdminInactivityTimer = _PortSdlcAdminInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 15),
    _PortSdlcAdminInactivityTimer_Type()
)
portSdlcAdminInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminInactivityTimer.setStatus("mandatory")


class _PortSdlcAdminL1Duplex_Type(Integer32):
    """Custom type portSdlcAdminL1Duplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_PortSdlcAdminL1Duplex_Type.__name__ = "Integer32"
_PortSdlcAdminL1Duplex_Object = MibTableColumn
portSdlcAdminL1Duplex = _PortSdlcAdminL1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 1, 1, 16),
    _PortSdlcAdminL1Duplex_Type()
)
portSdlcAdminL1Duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSdlcAdminL1Duplex.setStatus("mandatory")
_PortSdlcOperTable_Object = MibTable
portSdlcOperTable = _PortSdlcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2)
)
if mibBuilder.loadTexts:
    portSdlcOperTable.setStatus("mandatory")
_PortSdlcOperEntry_Object = MibTableRow
portSdlcOperEntry = _PortSdlcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1)
)
portSdlcOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portSdlcOperEntry.setStatus("mandatory")
_PortSdlcOperCommit_Type = Integer32
_PortSdlcOperCommit_Object = MibTableColumn
portSdlcOperCommit = _PortSdlcOperCommit_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 1),
    _PortSdlcOperCommit_Type()
)
portSdlcOperCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperCommit.setStatus("obsolete")


class _PortSdlcOperMAXRetries_Type(Integer32):
    """Custom type portSdlcOperMAXRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PortSdlcOperMAXRetries_Type.__name__ = "Integer32"
_PortSdlcOperMAXRetries_Object = MibTableColumn
portSdlcOperMAXRetries = _PortSdlcOperMAXRetries_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 2),
    _PortSdlcOperMAXRetries_Type()
)
portSdlcOperMAXRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperMAXRetries.setStatus("mandatory")


class _PortSdlcOperMAXOut_Type(Integer32):
    """Custom type portSdlcOperMAXOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PortSdlcOperMAXOut_Type.__name__ = "Integer32"
_PortSdlcOperMAXOut_Object = MibTableColumn
portSdlcOperMAXOut = _PortSdlcOperMAXOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 3),
    _PortSdlcOperMAXOut_Type()
)
portSdlcOperMAXOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperMAXOut.setStatus("mandatory")


class _PortSdlcOperPadType_Type(Integer32):
    """Custom type portSdlcOperPadType based on Integer32"""
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
        *(("hpad", 3),
          ("npad", 4),
          ("tpad", 2),
          ("xpad", 1))
    )


_PortSdlcOperPadType_Type.__name__ = "Integer32"
_PortSdlcOperPadType_Object = MibTableColumn
portSdlcOperPadType = _PortSdlcOperPadType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 4),
    _PortSdlcOperPadType_Type()
)
portSdlcOperPadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperPadType.setStatus("mandatory")


class _PortSdlcOperGenerateClock_Type(Integer32):
    """Custom type portSdlcOperGenerateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcOperGenerateClock_Type.__name__ = "Integer32"
_PortSdlcOperGenerateClock_Object = MibTableColumn
portSdlcOperGenerateClock = _PortSdlcOperGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 5),
    _PortSdlcOperGenerateClock_Type()
)
portSdlcOperGenerateClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperGenerateClock.setStatus("mandatory")


class _PortSdlcOperRcvClockFromDTE_Type(Integer32):
    """Custom type portSdlcOperRcvClockFromDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcOperRcvClockFromDTE_Type.__name__ = "Integer32"
_PortSdlcOperRcvClockFromDTE_Object = MibTableColumn
portSdlcOperRcvClockFromDTE = _PortSdlcOperRcvClockFromDTE_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 6),
    _PortSdlcOperRcvClockFromDTE_Type()
)
portSdlcOperRcvClockFromDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperRcvClockFromDTE.setStatus("mandatory")


class _PortSdlcOperNrz_Type(Integer32):
    """Custom type portSdlcOperNrz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcOperNrz_Type.__name__ = "Integer32"
_PortSdlcOperNrz_Object = MibTableColumn
portSdlcOperNrz = _PortSdlcOperNrz_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 7),
    _PortSdlcOperNrz_Type()
)
portSdlcOperNrz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperNrz.setStatus("mandatory")


class _PortSdlcOperPacketSize_Type(Integer32):
    """Custom type portSdlcOperPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_PortSdlcOperPacketSize_Type.__name__ = "Integer32"
_PortSdlcOperPacketSize_Object = MibTableColumn
portSdlcOperPacketSize = _PortSdlcOperPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 8),
    _PortSdlcOperPacketSize_Type()
)
portSdlcOperPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperPacketSize.setStatus("mandatory")


class _PortSdlcOperDisableRequestDisconnect_Type(Integer32):
    """Custom type portSdlcOperDisableRequestDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortSdlcOperDisableRequestDisconnect_Type.__name__ = "Integer32"
_PortSdlcOperDisableRequestDisconnect_Object = MibTableColumn
portSdlcOperDisableRequestDisconnect = _PortSdlcOperDisableRequestDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 9),
    _PortSdlcOperDisableRequestDisconnect_Type()
)
portSdlcOperDisableRequestDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperDisableRequestDisconnect.setStatus("mandatory")


class _PortSdlcOperLPDASupport_Type(Integer32):
    """Custom type portSdlcOperLPDASupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpda-1", 2),
          ("lpda-2", 3),
          ("none", 1))
    )


_PortSdlcOperLPDASupport_Type.__name__ = "Integer32"
_PortSdlcOperLPDASupport_Object = MibTableColumn
portSdlcOperLPDASupport = _PortSdlcOperLPDASupport_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 10),
    _PortSdlcOperLPDASupport_Type()
)
portSdlcOperLPDASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperLPDASupport.setStatus("mandatory")


class _PortSdlcOperConnector_Type(Integer32):
    """Custom type portSdlcOperConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v35", 5),
          ("x21", 8))
    )


_PortSdlcOperConnector_Type.__name__ = "Integer32"
_PortSdlcOperConnector_Object = MibTableColumn
portSdlcOperConnector = _PortSdlcOperConnector_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 11),
    _PortSdlcOperConnector_Type()
)
portSdlcOperConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperConnector.setStatus("mandatory")
_PortSdlcOperSpeed_Type = Integer32
_PortSdlcOperSpeed_Object = MibTableColumn
portSdlcOperSpeed = _PortSdlcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 12),
    _PortSdlcOperSpeed_Type()
)
portSdlcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperSpeed.setStatus("mandatory")


class _PortSdlcOperIdleFillChar_Type(Integer32):
    """Custom type portSdlcOperIdleFillChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex-7e", 2),
          ("hex-ff", 1))
    )


_PortSdlcOperIdleFillChar_Type.__name__ = "Integer32"
_PortSdlcOperIdleFillChar_Object = MibTableColumn
portSdlcOperIdleFillChar = _PortSdlcOperIdleFillChar_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 13),
    _PortSdlcOperIdleFillChar_Type()
)
portSdlcOperIdleFillChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperIdleFillChar.setStatus("mandatory")


class _PortSdlcOperInactivityTimer_Type(Integer32):
    """Custom type portSdlcOperInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 250),
    )


_PortSdlcOperInactivityTimer_Type.__name__ = "Integer32"
_PortSdlcOperInactivityTimer_Object = MibTableColumn
portSdlcOperInactivityTimer = _PortSdlcOperInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 14),
    _PortSdlcOperInactivityTimer_Type()
)
portSdlcOperInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperInactivityTimer.setStatus("mandatory")


class _PortSdlcOperL1Duplex_Type(Integer32):
    """Custom type portSdlcOperL1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_PortSdlcOperL1Duplex_Type.__name__ = "Integer32"
_PortSdlcOperL1Duplex_Object = MibTableColumn
portSdlcOperL1Duplex = _PortSdlcOperL1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 2, 1, 15),
    _PortSdlcOperL1Duplex_Type()
)
portSdlcOperL1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSdlcOperL1Duplex.setStatus("mandatory")
_LSSdlcAdminTable_Object = MibTable
lSSdlcAdminTable = _LSSdlcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3)
)
if mibBuilder.loadTexts:
    lSSdlcAdminTable.setStatus("mandatory")
_LSSdlcAdminEntry_Object = MibTableRow
lSSdlcAdminEntry = _LSSdlcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1)
)
lSSdlcAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    lSSdlcAdminEntry.setStatus("mandatory")
_LSSdlcAdminLocalSub_Type = NlSubscriberAddress
_LSSdlcAdminLocalSub_Object = MibTableColumn
lSSdlcAdminLocalSub = _LSSdlcAdminLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 1),
    _LSSdlcAdminLocalSub_Type()
)
lSSdlcAdminLocalSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminLocalSub.setStatus("mandatory")
_LSSdlcAdminRemoteSub_Type = NlSubscriberAddress
_LSSdlcAdminRemoteSub_Object = MibTableColumn
lSSdlcAdminRemoteSub = _LSSdlcAdminRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 2),
    _LSSdlcAdminRemoteSub_Type()
)
lSSdlcAdminRemoteSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminRemoteSub.setStatus("mandatory")


class _LSSdlcAdminAutoCall_Type(Integer32):
    """Custom type lSSdlcAdminAutoCall based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcAdminAutoCall_Type.__name__ = "Integer32"
_LSSdlcAdminAutoCall_Object = MibTableColumn
lSSdlcAdminAutoCall = _LSSdlcAdminAutoCall_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 3),
    _LSSdlcAdminAutoCall_Type()
)
lSSdlcAdminAutoCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminAutoCall.setStatus("mandatory")


class _LSSdlcAdminRetryTime_Type(Integer32):
    """Custom type lSSdlcAdminRetryTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 225),
    )


_LSSdlcAdminRetryTime_Type.__name__ = "Integer32"
_LSSdlcAdminRetryTime_Object = MibTableColumn
lSSdlcAdminRetryTime = _LSSdlcAdminRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 4),
    _LSSdlcAdminRetryTime_Type()
)
lSSdlcAdminRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminRetryTime.setStatus("mandatory")


class _LSSdlcAdminRetryCount_Type(Integer32):
    """Custom type lSSdlcAdminRetryCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcAdminRetryCount_Type.__name__ = "Integer32"
_LSSdlcAdminRetryCount_Object = MibTableColumn
lSSdlcAdminRetryCount = _LSSdlcAdminRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 5),
    _LSSdlcAdminRetryCount_Type()
)
lSSdlcAdminRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminRetryCount.setStatus("mandatory")


class _LSSdlcAdminLlc2Conversion_Type(Integer32):
    """Custom type lSSdlcAdminLlc2Conversion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcAdminLlc2Conversion_Type.__name__ = "Integer32"
_LSSdlcAdminLlc2Conversion_Object = MibTableColumn
lSSdlcAdminLlc2Conversion = _LSSdlcAdminLlc2Conversion_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 6),
    _LSSdlcAdminLlc2Conversion_Type()
)
lSSdlcAdminLlc2Conversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminLlc2Conversion.setStatus("mandatory")


class _LSSdlcAdminLPDAResourceID_Type(Integer32):
    """Custom type lSSdlcAdminLPDAResourceID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcAdminLPDAResourceID_Type.__name__ = "Integer32"
_LSSdlcAdminLPDAResourceID_Object = MibTableColumn
lSSdlcAdminLPDAResourceID = _LSSdlcAdminLPDAResourceID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 7),
    _LSSdlcAdminLPDAResourceID_Type()
)
lSSdlcAdminLPDAResourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminLPDAResourceID.setStatus("mandatory")
_LSSdlcAdminRowStatus_Type = RowStatus
_LSSdlcAdminRowStatus_Object = MibTableColumn
lSSdlcAdminRowStatus = _LSSdlcAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 8),
    _LSSdlcAdminRowStatus_Type()
)
lSSdlcAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminRowStatus.setStatus("mandatory")


class _LSSdlcAdminL2DatMode_Type(Integer32):
    """Custom type lSSdlcAdminL2DatMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("two-way-alternate", 1),
          ("two-way-simultaneous", 2))
    )


_LSSdlcAdminL2DatMode_Type.__name__ = "Integer32"
_LSSdlcAdminL2DatMode_Object = MibTableColumn
lSSdlcAdminL2DatMode = _LSSdlcAdminL2DatMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 3, 1, 9),
    _LSSdlcAdminL2DatMode_Type()
)
lSSdlcAdminL2DatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcAdminL2DatMode.setStatus("mandatory")
_LSSdlcOperTable_Object = MibTable
lSSdlcOperTable = _LSSdlcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4)
)
if mibBuilder.loadTexts:
    lSSdlcOperTable.setStatus("mandatory")
_LSSdlcOperEntry_Object = MibTableRow
lSSdlcOperEntry = _LSSdlcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1)
)
lSSdlcOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    lSSdlcOperEntry.setStatus("mandatory")
_LSSdlcOperLocalSub_Type = NlSubscriberAddress
_LSSdlcOperLocalSub_Object = MibTableColumn
lSSdlcOperLocalSub = _LSSdlcOperLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 1),
    _LSSdlcOperLocalSub_Type()
)
lSSdlcOperLocalSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperLocalSub.setStatus("mandatory")
_LSSdlcOperRemoteSub_Type = NlSubscriberAddress
_LSSdlcOperRemoteSub_Object = MibTableColumn
lSSdlcOperRemoteSub = _LSSdlcOperRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 2),
    _LSSdlcOperRemoteSub_Type()
)
lSSdlcOperRemoteSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperRemoteSub.setStatus("mandatory")


class _LSSdlcOperAutoCall_Type(Integer32):
    """Custom type lSSdlcOperAutoCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcOperAutoCall_Type.__name__ = "Integer32"
_LSSdlcOperAutoCall_Object = MibTableColumn
lSSdlcOperAutoCall = _LSSdlcOperAutoCall_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 3),
    _LSSdlcOperAutoCall_Type()
)
lSSdlcOperAutoCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperAutoCall.setStatus("mandatory")


class _LSSdlcOperRetryTime_Type(Integer32):
    """Custom type lSSdlcOperRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 225),
    )


_LSSdlcOperRetryTime_Type.__name__ = "Integer32"
_LSSdlcOperRetryTime_Object = MibTableColumn
lSSdlcOperRetryTime = _LSSdlcOperRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 4),
    _LSSdlcOperRetryTime_Type()
)
lSSdlcOperRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperRetryTime.setStatus("mandatory")


class _LSSdlcOperRetryCount_Type(Integer32):
    """Custom type lSSdlcOperRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcOperRetryCount_Type.__name__ = "Integer32"
_LSSdlcOperRetryCount_Object = MibTableColumn
lSSdlcOperRetryCount = _LSSdlcOperRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 5),
    _LSSdlcOperRetryCount_Type()
)
lSSdlcOperRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperRetryCount.setStatus("mandatory")


class _LSSdlcOperLlc2Conversion_Type(Integer32):
    """Custom type lSSdlcOperLlc2Conversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcOperLlc2Conversion_Type.__name__ = "Integer32"
_LSSdlcOperLlc2Conversion_Object = MibTableColumn
lSSdlcOperLlc2Conversion = _LSSdlcOperLlc2Conversion_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 6),
    _LSSdlcOperLlc2Conversion_Type()
)
lSSdlcOperLlc2Conversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperLlc2Conversion.setStatus("mandatory")


class _LSSdlcOperLPDAResourceID_Type(Integer32):
    """Custom type lSSdlcOperLPDAResourceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcOperLPDAResourceID_Type.__name__ = "Integer32"
_LSSdlcOperLPDAResourceID_Object = MibTableColumn
lSSdlcOperLPDAResourceID = _LSSdlcOperLPDAResourceID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 7),
    _LSSdlcOperLPDAResourceID_Type()
)
lSSdlcOperLPDAResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperLPDAResourceID.setStatus("mandatory")


class _LSSdlcOperL2DatMode_Type(Integer32):
    """Custom type lSSdlcOperL2DatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("two-way-alternate", 1),
          ("two-way-simultaneous", 2))
    )


_LSSdlcOperL2DatMode_Type.__name__ = "Integer32"
_LSSdlcOperL2DatMode_Object = MibTableColumn
lSSdlcOperL2DatMode = _LSSdlcOperL2DatMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 4, 1, 8),
    _LSSdlcOperL2DatMode_Type()
)
lSSdlcOperL2DatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcOperL2DatMode.setStatus("mandatory")
_LSSdlcLlc2AdminTable_Object = MibTable
lSSdlcLlc2AdminTable = _LSSdlcLlc2AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5)
)
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminTable.setStatus("mandatory")
_LSSdlcLlc2AdminEntry_Object = MibTableRow
lSSdlcLlc2AdminEntry = _LSSdlcLlc2AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1)
)
lSSdlcLlc2AdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminEntry.setStatus("mandatory")


class _LSSdlcLlc2AdminLocalSap_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLocalSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_LSSdlcLlc2AdminLocalSap_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLocalSap_Object = MibTableColumn
lSSdlcLlc2AdminLocalSap = _LSSdlcLlc2AdminLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 1),
    _LSSdlcLlc2AdminLocalSap_Type()
)
lSSdlcLlc2AdminLocalSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLocalSap.setStatus("mandatory")


class _LSSdlcLlc2AdminLocalMac_Type(PhysAddress):
    """Custom type lSSdlcLlc2AdminLocalMac based on PhysAddress"""
    defaultHexValue = "000000000000"


_LSSdlcLlc2AdminLocalMac_Object = MibTableColumn
lSSdlcLlc2AdminLocalMac = _LSSdlcLlc2AdminLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 2),
    _LSSdlcLlc2AdminLocalMac_Type()
)
lSSdlcLlc2AdminLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLocalMac.setStatus("mandatory")


class _LSSdlcLlc2AdminIdblk_Type(Integer32):
    """Custom type lSSdlcLlc2AdminIdblk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LSSdlcLlc2AdminIdblk_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminIdblk_Object = MibTableColumn
lSSdlcLlc2AdminIdblk = _LSSdlcLlc2AdminIdblk_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 3),
    _LSSdlcLlc2AdminIdblk_Type()
)
lSSdlcLlc2AdminIdblk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminIdblk.setStatus("mandatory")


class _LSSdlcLlc2AdminIdnum_Type(Integer32):
    """Custom type lSSdlcLlc2AdminIdnum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_LSSdlcLlc2AdminIdnum_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminIdnum_Object = MibTableColumn
lSSdlcLlc2AdminIdnum = _LSSdlcLlc2AdminIdnum_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 4),
    _LSSdlcLlc2AdminIdnum_Type()
)
lSSdlcLlc2AdminIdnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminIdnum.setStatus("mandatory")


class _LSSdlcLlc2AdminLanTi_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanTi based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_LSSdlcLlc2AdminLanTi_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanTi_Object = MibTableColumn
lSSdlcLlc2AdminLanTi = _LSSdlcLlc2AdminLanTi_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 5),
    _LSSdlcLlc2AdminLanTi_Type()
)
lSSdlcLlc2AdminLanTi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanTi.setStatus("mandatory")


class _LSSdlcLlc2AdminLanT1_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanT1 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_LSSdlcLlc2AdminLanT1_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanT1_Object = MibTableColumn
lSSdlcLlc2AdminLanT1 = _LSSdlcLlc2AdminLanT1_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 6),
    _LSSdlcLlc2AdminLanT1_Type()
)
lSSdlcLlc2AdminLanT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanT1.setStatus("mandatory")


class _LSSdlcLlc2AdminLanT2_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanT2 based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_LSSdlcLlc2AdminLanT2_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanT2_Object = MibTableColumn
lSSdlcLlc2AdminLanT2 = _LSSdlcLlc2AdminLanT2_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 7),
    _LSSdlcLlc2AdminLanT2_Type()
)
lSSdlcLlc2AdminLanT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanT2.setStatus("mandatory")


class _LSSdlcLlc2AdminLanN2_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanN2 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcLlc2AdminLanN2_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanN2_Object = MibTableColumn
lSSdlcLlc2AdminLanN2 = _LSSdlcLlc2AdminLanN2_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 8),
    _LSSdlcLlc2AdminLanN2_Type()
)
lSSdlcLlc2AdminLanN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanN2.setStatus("mandatory")


class _LSSdlcLlc2AdminLanN3_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanN3 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LSSdlcLlc2AdminLanN3_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanN3_Object = MibTableColumn
lSSdlcLlc2AdminLanN3 = _LSSdlcLlc2AdminLanN3_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 9),
    _LSSdlcLlc2AdminLanN3_Type()
)
lSSdlcLlc2AdminLanN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanN3.setStatus("mandatory")


class _LSSdlcLlc2AdminLanTw_Type(Integer32):
    """Custom type lSSdlcLlc2AdminLanTw based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LSSdlcLlc2AdminLanTw_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminLanTw_Object = MibTableColumn
lSSdlcLlc2AdminLanTw = _LSSdlcLlc2AdminLanTw_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 10),
    _LSSdlcLlc2AdminLanTw_Type()
)
lSSdlcLlc2AdminLanTw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminLanTw.setStatus("mandatory")


class _LSSdlcLlc2AdminBAG_Type(Integer32):
    """Custom type lSSdlcLlc2AdminBAG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LSSdlcLlc2AdminBAG_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminBAG_Object = MibTableColumn
lSSdlcLlc2AdminBAG = _LSSdlcLlc2AdminBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 11),
    _LSSdlcLlc2AdminBAG_Type()
)
lSSdlcLlc2AdminBAG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminBAG.setStatus("mandatory")


class _LSSdlcLlc2AdminPriority_Type(Integer32):
    """Custom type lSSdlcLlc2AdminPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_LSSdlcLlc2AdminPriority_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminPriority_Object = MibTableColumn
lSSdlcLlc2AdminPriority = _LSSdlcLlc2AdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 12),
    _LSSdlcLlc2AdminPriority_Type()
)
lSSdlcLlc2AdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminPriority.setStatus("mandatory")
_LSSdlcLlc2AdminRowStatus_Type = RowStatus
_LSSdlcLlc2AdminRowStatus_Object = MibTableColumn
lSSdlcLlc2AdminRowStatus = _LSSdlcLlc2AdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 13),
    _LSSdlcLlc2AdminRowStatus_Type()
)
lSSdlcLlc2AdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminRowStatus.setStatus("mandatory")


class _LSSdlcLlc2AdminSuppressXID_Type(Integer32):
    """Custom type lSSdlcLlc2AdminSuppressXID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcLlc2AdminSuppressXID_Type.__name__ = "Integer32"
_LSSdlcLlc2AdminSuppressXID_Object = MibTableColumn
lSSdlcLlc2AdminSuppressXID = _LSSdlcLlc2AdminSuppressXID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 5, 1, 14),
    _LSSdlcLlc2AdminSuppressXID_Type()
)
lSSdlcLlc2AdminSuppressXID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSSdlcLlc2AdminSuppressXID.setStatus("mandatory")
_LSSdlcLlc2OperTable_Object = MibTable
lSSdlcLlc2OperTable = _LSSdlcLlc2OperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6)
)
if mibBuilder.loadTexts:
    lSSdlcLlc2OperTable.setStatus("mandatory")
_LSSdlcLlc2OperEntry_Object = MibTableRow
lSSdlcLlc2OperEntry = _LSSdlcLlc2OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1)
)
lSSdlcLlc2OperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
    (0, "NETLINK-SPECIFIC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    lSSdlcLlc2OperEntry.setStatus("mandatory")


class _LSSdlcLlc2OperLocalSap_Type(Integer32):
    """Custom type lSSdlcLlc2OperLocalSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_LSSdlcLlc2OperLocalSap_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLocalSap_Object = MibTableColumn
lSSdlcLlc2OperLocalSap = _LSSdlcLlc2OperLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 1),
    _LSSdlcLlc2OperLocalSap_Type()
)
lSSdlcLlc2OperLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLocalSap.setStatus("mandatory")
_LSSdlcLlc2OperLocalMac_Type = PhysAddress
_LSSdlcLlc2OperLocalMac_Object = MibTableColumn
lSSdlcLlc2OperLocalMac = _LSSdlcLlc2OperLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 2),
    _LSSdlcLlc2OperLocalMac_Type()
)
lSSdlcLlc2OperLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLocalMac.setStatus("mandatory")


class _LSSdlcLlc2OperIdblk_Type(Integer32):
    """Custom type lSSdlcLlc2OperIdblk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LSSdlcLlc2OperIdblk_Type.__name__ = "Integer32"
_LSSdlcLlc2OperIdblk_Object = MibTableColumn
lSSdlcLlc2OperIdblk = _LSSdlcLlc2OperIdblk_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 3),
    _LSSdlcLlc2OperIdblk_Type()
)
lSSdlcLlc2OperIdblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperIdblk.setStatus("mandatory")


class _LSSdlcLlc2OperIdnum_Type(Integer32):
    """Custom type lSSdlcLlc2OperIdnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_LSSdlcLlc2OperIdnum_Type.__name__ = "Integer32"
_LSSdlcLlc2OperIdnum_Object = MibTableColumn
lSSdlcLlc2OperIdnum = _LSSdlcLlc2OperIdnum_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 4),
    _LSSdlcLlc2OperIdnum_Type()
)
lSSdlcLlc2OperIdnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperIdnum.setStatus("mandatory")


class _LSSdlcLlc2OperLanTi_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanTi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_LSSdlcLlc2OperLanTi_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanTi_Object = MibTableColumn
lSSdlcLlc2OperLanTi = _LSSdlcLlc2OperLanTi_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 5),
    _LSSdlcLlc2OperLanTi_Type()
)
lSSdlcLlc2OperLanTi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanTi.setStatus("mandatory")


class _LSSdlcLlc2OperLanT1_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_LSSdlcLlc2OperLanT1_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanT1_Object = MibTableColumn
lSSdlcLlc2OperLanT1 = _LSSdlcLlc2OperLanT1_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 6),
    _LSSdlcLlc2OperLanT1_Type()
)
lSSdlcLlc2OperLanT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanT1.setStatus("mandatory")


class _LSSdlcLlc2OperLanT2_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_LSSdlcLlc2OperLanT2_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanT2_Object = MibTableColumn
lSSdlcLlc2OperLanT2 = _LSSdlcLlc2OperLanT2_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 7),
    _LSSdlcLlc2OperLanT2_Type()
)
lSSdlcLlc2OperLanT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanT2.setStatus("mandatory")


class _LSSdlcLlc2OperLanN2_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LSSdlcLlc2OperLanN2_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanN2_Object = MibTableColumn
lSSdlcLlc2OperLanN2 = _LSSdlcLlc2OperLanN2_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 8),
    _LSSdlcLlc2OperLanN2_Type()
)
lSSdlcLlc2OperLanN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanN2.setStatus("mandatory")


class _LSSdlcLlc2OperLanN3_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanN3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LSSdlcLlc2OperLanN3_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanN3_Object = MibTableColumn
lSSdlcLlc2OperLanN3 = _LSSdlcLlc2OperLanN3_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 9),
    _LSSdlcLlc2OperLanN3_Type()
)
lSSdlcLlc2OperLanN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanN3.setStatus("mandatory")


class _LSSdlcLlc2OperLanTw_Type(Integer32):
    """Custom type lSSdlcLlc2OperLanTw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LSSdlcLlc2OperLanTw_Type.__name__ = "Integer32"
_LSSdlcLlc2OperLanTw_Object = MibTableColumn
lSSdlcLlc2OperLanTw = _LSSdlcLlc2OperLanTw_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 10),
    _LSSdlcLlc2OperLanTw_Type()
)
lSSdlcLlc2OperLanTw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperLanTw.setStatus("mandatory")


class _LSSdlcLlc2OperBAG_Type(Integer32):
    """Custom type lSSdlcLlc2OperBAG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LSSdlcLlc2OperBAG_Type.__name__ = "Integer32"
_LSSdlcLlc2OperBAG_Object = MibTableColumn
lSSdlcLlc2OperBAG = _LSSdlcLlc2OperBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 11),
    _LSSdlcLlc2OperBAG_Type()
)
lSSdlcLlc2OperBAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperBAG.setStatus("mandatory")


class _LSSdlcLlc2OperPriority_Type(Integer32):
    """Custom type lSSdlcLlc2OperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_LSSdlcLlc2OperPriority_Type.__name__ = "Integer32"
_LSSdlcLlc2OperPriority_Object = MibTableColumn
lSSdlcLlc2OperPriority = _LSSdlcLlc2OperPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 12),
    _LSSdlcLlc2OperPriority_Type()
)
lSSdlcLlc2OperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperPriority.setStatus("mandatory")


class _LSSdlcLlc2OperSuppressXID_Type(Integer32):
    """Custom type lSSdlcLlc2OperSuppressXID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LSSdlcLlc2OperSuppressXID_Type.__name__ = "Integer32"
_LSSdlcLlc2OperSuppressXID_Object = MibTableColumn
lSSdlcLlc2OperSuppressXID = _LSSdlcLlc2OperSuppressXID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 5, 6, 1, 13),
    _LSSdlcLlc2OperSuppressXID_Type()
)
lSSdlcLlc2OperSuppressXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSSdlcLlc2OperSuppressXID.setStatus("mandatory")
_PortT1Group_ObjectIdentity = ObjectIdentity
portT1Group = _PortT1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7)
)
_PortT1AdminTable_Object = MibTable
portT1AdminTable = _PortT1AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1)
)
if mibBuilder.loadTexts:
    portT1AdminTable.setStatus("mandatory")
_PortT1AdminEntry_Object = MibTableRow
portT1AdminEntry = _PortT1AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1)
)
portT1AdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portT1AdminEntry.setStatus("mandatory")


class _PortT1AdminBlockedPortFlag_Type(Integer32):
    """Custom type portT1AdminBlockedPortFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1AdminBlockedPortFlag_Type.__name__ = "Integer32"
_PortT1AdminBlockedPortFlag_Object = MibTableColumn
portT1AdminBlockedPortFlag = _PortT1AdminBlockedPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 1),
    _PortT1AdminBlockedPortFlag_Type()
)
portT1AdminBlockedPortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminBlockedPortFlag.setStatus("mandatory")


class _PortT1AdminGenerateClock_Type(Integer32):
    """Custom type portT1AdminGenerateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1AdminGenerateClock_Type.__name__ = "Integer32"
_PortT1AdminGenerateClock_Object = MibTableColumn
portT1AdminGenerateClock = _PortT1AdminGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 2),
    _PortT1AdminGenerateClock_Type()
)
portT1AdminGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminGenerateClock.setStatus("mandatory")


class _PortT1AdminFramingMode_Type(Integer32):
    """Custom type portT1AdminFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0aT1", 2),
          ("fullT1", 1))
    )


_PortT1AdminFramingMode_Type.__name__ = "Integer32"
_PortT1AdminFramingMode_Object = MibTableColumn
portT1AdminFramingMode = _PortT1AdminFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 3),
    _PortT1AdminFramingMode_Type()
)
portT1AdminFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminFramingMode.setStatus("mandatory")


class _PortT1AdminFrameModelSelect_Type(Integer32):
    """Custom type portT1AdminFrameModelSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_PortT1AdminFrameModelSelect_Type.__name__ = "Integer32"
_PortT1AdminFrameModelSelect_Object = MibTableColumn
portT1AdminFrameModelSelect = _PortT1AdminFrameModelSelect_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 4),
    _PortT1AdminFrameModelSelect_Type()
)
portT1AdminFrameModelSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminFrameModelSelect.setStatus("mandatory")


class _PortT1AdminLineEncoding_Type(Integer32):
    """Custom type portT1AdminLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_PortT1AdminLineEncoding_Type.__name__ = "Integer32"
_PortT1AdminLineEncoding_Object = MibTableColumn
portT1AdminLineEncoding = _PortT1AdminLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 5),
    _PortT1AdminLineEncoding_Type()
)
portT1AdminLineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminLineEncoding.setStatus("mandatory")


class _PortT1AdminLineBuildOut_Type(Integer32):
    """Custom type portT1AdminLineBuildOut based on Integer32"""
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
        *(("minus15db", 7),
          ("minus22p5db", 8),
          ("minus7p5db", 6),
          ("x133-266ft", 2),
          ("x266-399ft", 3),
          ("x399-533ft", 4),
          ("x533-655ft", 5),
          ("zerodb", 1))
    )


_PortT1AdminLineBuildOut_Type.__name__ = "Integer32"
_PortT1AdminLineBuildOut_Object = MibTableColumn
portT1AdminLineBuildOut = _PortT1AdminLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 6),
    _PortT1AdminLineBuildOut_Type()
)
portT1AdminLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminLineBuildOut.setStatus("mandatory")
_PortT1AdminRowStatus_Type = RowStatus
_PortT1AdminRowStatus_Object = MibTableColumn
portT1AdminRowStatus = _PortT1AdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 7),
    _PortT1AdminRowStatus_Type()
)
portT1AdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminRowStatus.setStatus("mandatory")


class _PortT1AdminProtocolFraming_Type(Integer32):
    """Custom type portT1AdminProtocolFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bisync", 2),
          ("sync", 1))
    )


_PortT1AdminProtocolFraming_Type.__name__ = "Integer32"
_PortT1AdminProtocolFraming_Object = MibTableColumn
portT1AdminProtocolFraming = _PortT1AdminProtocolFraming_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 8),
    _PortT1AdminProtocolFraming_Type()
)
portT1AdminProtocolFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminProtocolFraming.setStatus("mandatory")


class _PortT1AdminNRZI_Type(Integer32):
    """Custom type portT1AdminNRZI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1AdminNRZI_Type.__name__ = "Integer32"
_PortT1AdminNRZI_Object = MibTableColumn
portT1AdminNRZI = _PortT1AdminNRZI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 1, 1, 9),
    _PortT1AdminNRZI_Type()
)
portT1AdminNRZI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portT1AdminNRZI.setStatus("mandatory")
_PortT1OperTable_Object = MibTable
portT1OperTable = _PortT1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2)
)
if mibBuilder.loadTexts:
    portT1OperTable.setStatus("mandatory")
_PortT1OperEntry_Object = MibTableRow
portT1OperEntry = _PortT1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1)
)
portT1OperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    portT1OperEntry.setStatus("mandatory")


class _PortT1OperBlockedPortFlag_Type(Integer32):
    """Custom type portT1OperBlockedPortFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1OperBlockedPortFlag_Type.__name__ = "Integer32"
_PortT1OperBlockedPortFlag_Object = MibTableColumn
portT1OperBlockedPortFlag = _PortT1OperBlockedPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 1),
    _PortT1OperBlockedPortFlag_Type()
)
portT1OperBlockedPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperBlockedPortFlag.setStatus("mandatory")


class _PortT1OperGenerateClock_Type(Integer32):
    """Custom type portT1OperGenerateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1OperGenerateClock_Type.__name__ = "Integer32"
_PortT1OperGenerateClock_Object = MibTableColumn
portT1OperGenerateClock = _PortT1OperGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 2),
    _PortT1OperGenerateClock_Type()
)
portT1OperGenerateClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperGenerateClock.setStatus("mandatory")


class _PortT1OperFramingMode_Type(Integer32):
    """Custom type portT1OperFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0aT1", 2),
          ("fullT1", 1))
    )


_PortT1OperFramingMode_Type.__name__ = "Integer32"
_PortT1OperFramingMode_Object = MibTableColumn
portT1OperFramingMode = _PortT1OperFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 3),
    _PortT1OperFramingMode_Type()
)
portT1OperFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperFramingMode.setStatus("mandatory")


class _PortT1OperFrameModelSelect_Type(Integer32):
    """Custom type portT1OperFrameModelSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_PortT1OperFrameModelSelect_Type.__name__ = "Integer32"
_PortT1OperFrameModelSelect_Object = MibTableColumn
portT1OperFrameModelSelect = _PortT1OperFrameModelSelect_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 4),
    _PortT1OperFrameModelSelect_Type()
)
portT1OperFrameModelSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperFrameModelSelect.setStatus("mandatory")


class _PortT1OperLineEncoding_Type(Integer32):
    """Custom type portT1OperLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_PortT1OperLineEncoding_Type.__name__ = "Integer32"
_PortT1OperLineEncoding_Object = MibTableColumn
portT1OperLineEncoding = _PortT1OperLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 5),
    _PortT1OperLineEncoding_Type()
)
portT1OperLineEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperLineEncoding.setStatus("mandatory")


class _PortT1OperLineBuildOut_Type(Integer32):
    """Custom type portT1OperLineBuildOut based on Integer32"""
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
        *(("minus15db", 7),
          ("minus22p5db", 8),
          ("minus7p5db", 6),
          ("x133-266ft", 2),
          ("x266-399ft", 3),
          ("x399-533ft", 4),
          ("x533-655ft", 5),
          ("zerodb", 1))
    )


_PortT1OperLineBuildOut_Type.__name__ = "Integer32"
_PortT1OperLineBuildOut_Object = MibTableColumn
portT1OperLineBuildOut = _PortT1OperLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 6),
    _PortT1OperLineBuildOut_Type()
)
portT1OperLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperLineBuildOut.setStatus("mandatory")


class _PortT1OperProtocolFraming_Type(Integer32):
    """Custom type portT1OperProtocolFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bisync", 2),
          ("sync", 1))
    )


_PortT1OperProtocolFraming_Type.__name__ = "Integer32"
_PortT1OperProtocolFraming_Object = MibTableColumn
portT1OperProtocolFraming = _PortT1OperProtocolFraming_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 7),
    _PortT1OperProtocolFraming_Type()
)
portT1OperProtocolFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperProtocolFraming.setStatus("mandatory")


class _PortT1OperNRZI_Type(Integer32):
    """Custom type portT1OperNRZI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortT1OperNRZI_Type.__name__ = "Integer32"
_PortT1OperNRZI_Object = MibTableColumn
portT1OperNRZI = _PortT1OperNRZI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 7, 2, 1, 8),
    _PortT1OperNRZI_Type()
)
portT1OperNRZI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portT1OperNRZI.setStatus("mandatory")
_PortVoiceGroup_ObjectIdentity = ObjectIdentity
portVoiceGroup = _PortVoiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8)
)
_PortVoiceAdminTable_Object = MibTable
portVoiceAdminTable = _PortVoiceAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1)
)
if mibBuilder.loadTexts:
    portVoiceAdminTable.setStatus("mandatory")
_PortVoiceAdminEntry_Object = MibTableRow
portVoiceAdminEntry = _PortVoiceAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1)
)
portVoiceAdminEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portVoiceAdminRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portVoiceAdminPortIndex"),
)
if mibBuilder.loadTexts:
    portVoiceAdminEntry.setStatus("mandatory")
_PortVoiceAdminRlpIndex_Type = Integer32
_PortVoiceAdminRlpIndex_Object = MibTableColumn
portVoiceAdminRlpIndex = _PortVoiceAdminRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 1),
    _PortVoiceAdminRlpIndex_Type()
)
portVoiceAdminRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceAdminRlpIndex.setStatus("mandatory")
_PortVoiceAdminPortIndex_Type = Integer32
_PortVoiceAdminPortIndex_Object = MibTableColumn
portVoiceAdminPortIndex = _PortVoiceAdminPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 2),
    _PortVoiceAdminPortIndex_Type()
)
portVoiceAdminPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceAdminPortIndex.setStatus("mandatory")


class _PortVoiceAdminBlockedFlag_Type(Integer32):
    """Custom type portVoiceAdminBlockedFlag based on Integer32"""
    defaultValue = 1

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


_PortVoiceAdminBlockedFlag_Type.__name__ = "Integer32"
_PortVoiceAdminBlockedFlag_Object = MibTableColumn
portVoiceAdminBlockedFlag = _PortVoiceAdminBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 3),
    _PortVoiceAdminBlockedFlag_Type()
)
portVoiceAdminBlockedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminBlockedFlag.setStatus("mandatory")


class _PortVoiceAdminSpeed_Type(Integer32):
    """Custom type portVoiceAdminSpeed based on Integer32"""
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
        *(("bps-32000", 3),
          ("bps-4800", 1),
          ("bps-64000", 4),
          ("bps-8000", 2))
    )


_PortVoiceAdminSpeed_Type.__name__ = "Integer32"
_PortVoiceAdminSpeed_Object = MibTableColumn
portVoiceAdminSpeed = _PortVoiceAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 4),
    _PortVoiceAdminSpeed_Type()
)
portVoiceAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminSpeed.setStatus("mandatory")


class _PortVoiceAdminDTMF_Type(Integer32):
    """Custom type portVoiceAdminDTMF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceAdminDTMF_Type.__name__ = "Integer32"
_PortVoiceAdminDTMF_Object = MibTableColumn
portVoiceAdminDTMF = _PortVoiceAdminDTMF_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 5),
    _PortVoiceAdminDTMF_Type()
)
portVoiceAdminDTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminDTMF.setStatus("mandatory")


class _PortVoiceAdminInterface_Type(Integer32):
    """Custom type portVoiceAdminInterface based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ac15-a", 4),
          ("ac15-b", 6),
          ("em-2w", 2),
          ("em-2w-te", 11),
          ("em-4w", 1),
          ("em-4w-te", 10),
          ("loop-start", 3))
    )


_PortVoiceAdminInterface_Type.__name__ = "Integer32"
_PortVoiceAdminInterface_Object = MibTableColumn
portVoiceAdminInterface = _PortVoiceAdminInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 6),
    _PortVoiceAdminInterface_Type()
)
portVoiceAdminInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminInterface.setStatus("mandatory")


class _PortVoiceAdminTETimer_Type(Integer32):
    """Custom type portVoiceAdminTETimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceAdminTETimer_Type.__name__ = "Integer32"
_PortVoiceAdminTETimer_Object = MibTableColumn
portVoiceAdminTETimer = _PortVoiceAdminTETimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 7),
    _PortVoiceAdminTETimer_Type()
)
portVoiceAdminTETimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminTETimer.setStatus("mandatory")


class _PortVoiceAdminLevelIn_Type(Integer32):
    """Custom type portVoiceAdminLevelIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-22, 7),
    )


_PortVoiceAdminLevelIn_Type.__name__ = "Integer32"
_PortVoiceAdminLevelIn_Object = MibTableColumn
portVoiceAdminLevelIn = _PortVoiceAdminLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 8),
    _PortVoiceAdminLevelIn_Type()
)
portVoiceAdminLevelIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminLevelIn.setStatus("mandatory")


class _PortVoiceAdminLevelOut_Type(Integer32):
    """Custom type portVoiceAdminLevelOut based on Integer32"""
    defaultValue = -4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-22, 7),
    )


_PortVoiceAdminLevelOut_Type.__name__ = "Integer32"
_PortVoiceAdminLevelOut_Object = MibTableColumn
portVoiceAdminLevelOut = _PortVoiceAdminLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 9),
    _PortVoiceAdminLevelOut_Type()
)
portVoiceAdminLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminLevelOut.setStatus("mandatory")


class _PortVoiceAdminCallTimer_Type(Integer32):
    """Custom type portVoiceAdminCallTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PortVoiceAdminCallTimer_Type.__name__ = "Integer32"
_PortVoiceAdminCallTimer_Object = MibTableColumn
portVoiceAdminCallTimer = _PortVoiceAdminCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 10),
    _PortVoiceAdminCallTimer_Type()
)
portVoiceAdminCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminCallTimer.setStatus("mandatory")


class _PortVoiceAdminHuntGroup_Type(Integer32):
    """Custom type portVoiceAdminHuntGroup based on Integer32"""
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
        *(("a", 2),
          ("b", 3),
          ("none", 1))
    )


_PortVoiceAdminHuntGroup_Type.__name__ = "Integer32"
_PortVoiceAdminHuntGroup_Object = MibTableColumn
portVoiceAdminHuntGroup = _PortVoiceAdminHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 11),
    _PortVoiceAdminHuntGroup_Type()
)
portVoiceAdminHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminHuntGroup.setStatus("mandatory")


class _PortVoiceAdminLongDialPrefix_Type(OctetString):
    """Custom type portVoiceAdminLongDialPrefix based on OctetString"""
    defaultHexValue = "2A"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PortVoiceAdminLongDialPrefix_Type.__name__ = "OctetString"
_PortVoiceAdminLongDialPrefix_Object = MibTableColumn
portVoiceAdminLongDialPrefix = _PortVoiceAdminLongDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 12),
    _PortVoiceAdminLongDialPrefix_Type()
)
portVoiceAdminLongDialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminLongDialPrefix.setStatus("mandatory")


class _PortVoiceAdminSLTTimeout_Type(Integer32):
    """Custom type portVoiceAdminSLTTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PortVoiceAdminSLTTimeout_Type.__name__ = "Integer32"
_PortVoiceAdminSLTTimeout_Object = MibTableColumn
portVoiceAdminSLTTimeout = _PortVoiceAdminSLTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 13),
    _PortVoiceAdminSLTTimeout_Type()
)
portVoiceAdminSLTTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminSLTTimeout.setStatus("mandatory")


class _PortVoiceAdminLinkDownBusy_Type(Integer32):
    """Custom type portVoiceAdminLinkDownBusy based on Integer32"""
    defaultValue = 2

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


_PortVoiceAdminLinkDownBusy_Type.__name__ = "Integer32"
_PortVoiceAdminLinkDownBusy_Object = MibTableColumn
portVoiceAdminLinkDownBusy = _PortVoiceAdminLinkDownBusy_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 14),
    _PortVoiceAdminLinkDownBusy_Type()
)
portVoiceAdminLinkDownBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminLinkDownBusy.setStatus("mandatory")


class _PortVoiceAdminFaxSupported_Type(Integer32):
    """Custom type portVoiceAdminFaxSupported based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortVoiceAdminFaxSupported_Type.__name__ = "Integer32"
_PortVoiceAdminFaxSupported_Object = MibTableColumn
portVoiceAdminFaxSupported = _PortVoiceAdminFaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 15),
    _PortVoiceAdminFaxSupported_Type()
)
portVoiceAdminFaxSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminFaxSupported.setStatus("mandatory")


class _PortVoiceAdminTelephonyType_Type(Integer32):
    """Custom type portVoiceAdminTelephonyType based on Integer32"""
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
        *(("ac15", 4),
          ("em", 3),
          ("opx", 1),
          ("slt", 2))
    )


_PortVoiceAdminTelephonyType_Type.__name__ = "Integer32"
_PortVoiceAdminTelephonyType_Object = MibTableColumn
portVoiceAdminTelephonyType = _PortVoiceAdminTelephonyType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 16),
    _PortVoiceAdminTelephonyType_Type()
)
portVoiceAdminTelephonyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminTelephonyType.setStatus("mandatory")


class _PortVoiceAdminJitter_Type(Integer32):
    """Custom type portVoiceAdminJitter based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_PortVoiceAdminJitter_Type.__name__ = "Integer32"
_PortVoiceAdminJitter_Object = MibTableColumn
portVoiceAdminJitter = _PortVoiceAdminJitter_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 17),
    _PortVoiceAdminJitter_Type()
)
portVoiceAdminJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminJitter.setStatus("mandatory")


class _PortVoiceAdminSampleDelay_Type(Integer32):
    """Custom type portVoiceAdminSampleDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceAdminSampleDelay_Type.__name__ = "Integer32"
_PortVoiceAdminSampleDelay_Object = MibTableColumn
portVoiceAdminSampleDelay = _PortVoiceAdminSampleDelay_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 18),
    _PortVoiceAdminSampleDelay_Type()
)
portVoiceAdminSampleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminSampleDelay.setStatus("mandatory")


class _PortVoiceAdminDialTimer_Type(Integer32):
    """Custom type portVoiceAdminDialTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PortVoiceAdminDialTimer_Type.__name__ = "Integer32"
_PortVoiceAdminDialTimer_Object = MibTableColumn
portVoiceAdminDialTimer = _PortVoiceAdminDialTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 19),
    _PortVoiceAdminDialTimer_Type()
)
portVoiceAdminDialTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminDialTimer.setStatus("mandatory")


class _PortVoiceAdminAutoDial_Type(Integer32):
    """Custom type portVoiceAdminAutoDial based on Integer32"""
    defaultValue = 1

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


_PortVoiceAdminAutoDial_Type.__name__ = "Integer32"
_PortVoiceAdminAutoDial_Object = MibTableColumn
portVoiceAdminAutoDial = _PortVoiceAdminAutoDial_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 20),
    _PortVoiceAdminAutoDial_Type()
)
portVoiceAdminAutoDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminAutoDial.setStatus("mandatory")


class _PortVoiceAdminSuppression_Type(Integer32):
    """Custom type portVoiceAdminSuppression based on Integer32"""
    defaultValue = 2

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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("very-high", 5),
          ("very-low", 1))
    )


_PortVoiceAdminSuppression_Type.__name__ = "Integer32"
_PortVoiceAdminSuppression_Object = MibTableColumn
portVoiceAdminSuppression = _PortVoiceAdminSuppression_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 21),
    _PortVoiceAdminSuppression_Type()
)
portVoiceAdminSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminSuppression.setStatus("mandatory")


class _PortVoiceAdminAutoDialNumber_Type(OctetString):
    """Custom type portVoiceAdminAutoDialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PortVoiceAdminAutoDialNumber_Type.__name__ = "OctetString"
_PortVoiceAdminAutoDialNumber_Object = MibTableColumn
portVoiceAdminAutoDialNumber = _PortVoiceAdminAutoDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 22),
    _PortVoiceAdminAutoDialNumber_Type()
)
portVoiceAdminAutoDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminAutoDialNumber.setStatus("mandatory")


class _PortVoiceAdminAutoPoll_Type(Integer32):
    """Custom type portVoiceAdminAutoPoll based on Integer32"""
    defaultValue = 1

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


_PortVoiceAdminAutoPoll_Type.__name__ = "Integer32"
_PortVoiceAdminAutoPoll_Object = MibTableColumn
portVoiceAdminAutoPoll = _PortVoiceAdminAutoPoll_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 23),
    _PortVoiceAdminAutoPoll_Type()
)
portVoiceAdminAutoPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminAutoPoll.setStatus("mandatory")


class _PortVoiceAdminAutoPollTimer_Type(Integer32):
    """Custom type portVoiceAdminAutoPollTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_PortVoiceAdminAutoPollTimer_Type.__name__ = "Integer32"
_PortVoiceAdminAutoPollTimer_Object = MibTableColumn
portVoiceAdminAutoPollTimer = _PortVoiceAdminAutoPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 24),
    _PortVoiceAdminAutoPollTimer_Type()
)
portVoiceAdminAutoPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminAutoPollTimer.setStatus("mandatory")


class _PortVoiceAdminExtDigitsSource_Type(Integer32):
    """Custom type portVoiceAdminExtDigitsSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("user", 2))
    )


_PortVoiceAdminExtDigitsSource_Type.__name__ = "Integer32"
_PortVoiceAdminExtDigitsSource_Object = MibTableColumn
portVoiceAdminExtDigitsSource = _PortVoiceAdminExtDigitsSource_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 25),
    _PortVoiceAdminExtDigitsSource_Type()
)
portVoiceAdminExtDigitsSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminExtDigitsSource.setStatus("mandatory")


class _PortVoiceAdminNumDigitsDelete_Type(Integer32):
    """Custom type portVoiceAdminNumDigitsDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PortVoiceAdminNumDigitsDelete_Type.__name__ = "Integer32"
_PortVoiceAdminNumDigitsDelete_Object = MibTableColumn
portVoiceAdminNumDigitsDelete = _PortVoiceAdminNumDigitsDelete_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 26),
    _PortVoiceAdminNumDigitsDelete_Type()
)
portVoiceAdminNumDigitsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminNumDigitsDelete.setStatus("mandatory")


class _PortVoiceAdminForwardDelay_Type(Integer32):
    """Custom type portVoiceAdminForwardDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_PortVoiceAdminForwardDelay_Type.__name__ = "Integer32"
_PortVoiceAdminForwardDelay_Object = MibTableColumn
portVoiceAdminForwardDelay = _PortVoiceAdminForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 27),
    _PortVoiceAdminForwardDelay_Type()
)
portVoiceAdminForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminForwardDelay.setStatus("mandatory")


class _PortVoiceAdminForwardedType_Type(Integer32):
    """Custom type portVoiceAdminForwardedType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_PortVoiceAdminForwardedType_Type.__name__ = "Integer32"
_PortVoiceAdminForwardedType_Object = MibTableColumn
portVoiceAdminForwardedType = _PortVoiceAdminForwardedType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 28),
    _PortVoiceAdminForwardedType_Type()
)
portVoiceAdminForwardedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminForwardedType.setStatus("mandatory")


class _PortVoiceAdminForwardedDigits_Type(Integer32):
    """Custom type portVoiceAdminForwardedDigits based on Integer32"""
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
        *(("all", 2),
          ("extended", 3),
          ("none", 1))
    )


_PortVoiceAdminForwardedDigits_Type.__name__ = "Integer32"
_PortVoiceAdminForwardedDigits_Object = MibTableColumn
portVoiceAdminForwardedDigits = _PortVoiceAdminForwardedDigits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 29),
    _PortVoiceAdminForwardedDigits_Type()
)
portVoiceAdminForwardedDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminForwardedDigits.setStatus("mandatory")


class _PortVoiceAdminMakeRatio_Type(Integer32):
    """Custom type portVoiceAdminMakeRatio based on Integer32"""
    defaultValue = 34

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 80),
    )


_PortVoiceAdminMakeRatio_Type.__name__ = "Integer32"
_PortVoiceAdminMakeRatio_Object = MibTableColumn
portVoiceAdminMakeRatio = _PortVoiceAdminMakeRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 30),
    _PortVoiceAdminMakeRatio_Type()
)
portVoiceAdminMakeRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminMakeRatio.setStatus("mandatory")


class _PortVoiceAdminBreakRatio_Type(Integer32):
    """Custom type portVoiceAdminBreakRatio based on Integer32"""
    defaultValue = 66

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 80),
    )


_PortVoiceAdminBreakRatio_Type.__name__ = "Integer32"
_PortVoiceAdminBreakRatio_Object = MibTableColumn
portVoiceAdminBreakRatio = _PortVoiceAdminBreakRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 31),
    _PortVoiceAdminBreakRatio_Type()
)
portVoiceAdminBreakRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminBreakRatio.setStatus("mandatory")


class _PortVoiceAdminDTMFOnDuration_Type(Integer32):
    """Custom type portVoiceAdminDTMFOnDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_PortVoiceAdminDTMFOnDuration_Type.__name__ = "Integer32"
_PortVoiceAdminDTMFOnDuration_Object = MibTableColumn
portVoiceAdminDTMFOnDuration = _PortVoiceAdminDTMFOnDuration_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 32),
    _PortVoiceAdminDTMFOnDuration_Type()
)
portVoiceAdminDTMFOnDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminDTMFOnDuration.setStatus("mandatory")


class _PortVoiceAdminDTMFOffDuration_Type(Integer32):
    """Custom type portVoiceAdminDTMFOffDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_PortVoiceAdminDTMFOffDuration_Type.__name__ = "Integer32"
_PortVoiceAdminDTMFOffDuration_Object = MibTableColumn
portVoiceAdminDTMFOffDuration = _PortVoiceAdminDTMFOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 33),
    _PortVoiceAdminDTMFOffDuration_Type()
)
portVoiceAdminDTMFOffDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminDTMFOffDuration.setStatus("mandatory")


class _PortVoiceAdminToneType_Type(Integer32):
    """Custom type portVoiceAdminToneType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("mf", 2))
    )


_PortVoiceAdminToneType_Type.__name__ = "Integer32"
_PortVoiceAdminToneType_Object = MibTableColumn
portVoiceAdminToneType = _PortVoiceAdminToneType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 34),
    _PortVoiceAdminToneType_Type()
)
portVoiceAdminToneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminToneType.setStatus("mandatory")
_PortVoiceAdminRowStatus_Type = RowStatus
_PortVoiceAdminRowStatus_Object = MibTableColumn
portVoiceAdminRowStatus = _PortVoiceAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 1, 1, 35),
    _PortVoiceAdminRowStatus_Type()
)
portVoiceAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceAdminRowStatus.setStatus("mandatory")
_PortVoiceOperTable_Object = MibTable
portVoiceOperTable = _PortVoiceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2)
)
if mibBuilder.loadTexts:
    portVoiceOperTable.setStatus("mandatory")
_PortVoiceOperEntry_Object = MibTableRow
portVoiceOperEntry = _PortVoiceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1)
)
portVoiceOperEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portVoiceOperRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portVoiceOperPortIndex"),
)
if mibBuilder.loadTexts:
    portVoiceOperEntry.setStatus("mandatory")
_PortVoiceOperRlpIndex_Type = Integer32
_PortVoiceOperRlpIndex_Object = MibTableColumn
portVoiceOperRlpIndex = _PortVoiceOperRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 1),
    _PortVoiceOperRlpIndex_Type()
)
portVoiceOperRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperRlpIndex.setStatus("mandatory")
_PortVoiceOperPortIndex_Type = Integer32
_PortVoiceOperPortIndex_Object = MibTableColumn
portVoiceOperPortIndex = _PortVoiceOperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 2),
    _PortVoiceOperPortIndex_Type()
)
portVoiceOperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperPortIndex.setStatus("mandatory")


class _PortVoiceOperBlockedFlag_Type(Integer32):
    """Custom type portVoiceOperBlockedFlag based on Integer32"""
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


_PortVoiceOperBlockedFlag_Type.__name__ = "Integer32"
_PortVoiceOperBlockedFlag_Object = MibTableColumn
portVoiceOperBlockedFlag = _PortVoiceOperBlockedFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 3),
    _PortVoiceOperBlockedFlag_Type()
)
portVoiceOperBlockedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperBlockedFlag.setStatus("mandatory")


class _PortVoiceOperSpeed_Type(Integer32):
    """Custom type portVoiceOperSpeed based on Integer32"""
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
        *(("bps-32000", 3),
          ("bps-4800", 1),
          ("bps-64000", 4),
          ("bps-8000", 2))
    )


_PortVoiceOperSpeed_Type.__name__ = "Integer32"
_PortVoiceOperSpeed_Object = MibTableColumn
portVoiceOperSpeed = _PortVoiceOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 4),
    _PortVoiceOperSpeed_Type()
)
portVoiceOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperSpeed.setStatus("mandatory")


class _PortVoiceOperDTMF_Type(Integer32):
    """Custom type portVoiceOperDTMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceOperDTMF_Type.__name__ = "Integer32"
_PortVoiceOperDTMF_Object = MibTableColumn
portVoiceOperDTMF = _PortVoiceOperDTMF_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 5),
    _PortVoiceOperDTMF_Type()
)
portVoiceOperDTMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperDTMF.setStatus("mandatory")


class _PortVoiceOperInterface_Type(Integer32):
    """Custom type portVoiceOperInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ac15-a", 4),
          ("ac15-b", 6),
          ("em-2w", 2),
          ("em-2w-te", 11),
          ("em-4w", 1),
          ("em-4w-te", 10),
          ("loop-start", 3))
    )


_PortVoiceOperInterface_Type.__name__ = "Integer32"
_PortVoiceOperInterface_Object = MibTableColumn
portVoiceOperInterface = _PortVoiceOperInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 6),
    _PortVoiceOperInterface_Type()
)
portVoiceOperInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperInterface.setStatus("mandatory")


class _PortVoiceOperTETimer_Type(Integer32):
    """Custom type portVoiceOperTETimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceOperTETimer_Type.__name__ = "Integer32"
_PortVoiceOperTETimer_Object = MibTableColumn
portVoiceOperTETimer = _PortVoiceOperTETimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 7),
    _PortVoiceOperTETimer_Type()
)
portVoiceOperTETimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperTETimer.setStatus("mandatory")


class _PortVoiceOperLevelIn_Type(Integer32):
    """Custom type portVoiceOperLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-22, 7),
    )


_PortVoiceOperLevelIn_Type.__name__ = "Integer32"
_PortVoiceOperLevelIn_Object = MibTableColumn
portVoiceOperLevelIn = _PortVoiceOperLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 8),
    _PortVoiceOperLevelIn_Type()
)
portVoiceOperLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperLevelIn.setStatus("mandatory")


class _PortVoiceOperLevelOut_Type(Integer32):
    """Custom type portVoiceOperLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-22, 7),
    )


_PortVoiceOperLevelOut_Type.__name__ = "Integer32"
_PortVoiceOperLevelOut_Object = MibTableColumn
portVoiceOperLevelOut = _PortVoiceOperLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 9),
    _PortVoiceOperLevelOut_Type()
)
portVoiceOperLevelOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperLevelOut.setStatus("mandatory")


class _PortVoiceOperCallTimer_Type(Integer32):
    """Custom type portVoiceOperCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PortVoiceOperCallTimer_Type.__name__ = "Integer32"
_PortVoiceOperCallTimer_Object = MibTableColumn
portVoiceOperCallTimer = _PortVoiceOperCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 10),
    _PortVoiceOperCallTimer_Type()
)
portVoiceOperCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperCallTimer.setStatus("mandatory")


class _PortVoiceOperHuntGroup_Type(Integer32):
    """Custom type portVoiceOperHuntGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("none", 1))
    )


_PortVoiceOperHuntGroup_Type.__name__ = "Integer32"
_PortVoiceOperHuntGroup_Object = MibTableColumn
portVoiceOperHuntGroup = _PortVoiceOperHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 11),
    _PortVoiceOperHuntGroup_Type()
)
portVoiceOperHuntGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperHuntGroup.setStatus("mandatory")


class _PortVoiceOperLongDialPrefix_Type(OctetString):
    """Custom type portVoiceOperLongDialPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PortVoiceOperLongDialPrefix_Type.__name__ = "OctetString"
_PortVoiceOperLongDialPrefix_Object = MibTableColumn
portVoiceOperLongDialPrefix = _PortVoiceOperLongDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 12),
    _PortVoiceOperLongDialPrefix_Type()
)
portVoiceOperLongDialPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperLongDialPrefix.setStatus("mandatory")


class _PortVoiceOperSLTTimeout_Type(Integer32):
    """Custom type portVoiceOperSLTTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PortVoiceOperSLTTimeout_Type.__name__ = "Integer32"
_PortVoiceOperSLTTimeout_Object = MibTableColumn
portVoiceOperSLTTimeout = _PortVoiceOperSLTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 13),
    _PortVoiceOperSLTTimeout_Type()
)
portVoiceOperSLTTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperSLTTimeout.setStatus("mandatory")


class _PortVoiceOperLinkDownBusy_Type(Integer32):
    """Custom type portVoiceOperLinkDownBusy based on Integer32"""
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


_PortVoiceOperLinkDownBusy_Type.__name__ = "Integer32"
_PortVoiceOperLinkDownBusy_Object = MibTableColumn
portVoiceOperLinkDownBusy = _PortVoiceOperLinkDownBusy_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 14),
    _PortVoiceOperLinkDownBusy_Type()
)
portVoiceOperLinkDownBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperLinkDownBusy.setStatus("mandatory")


class _PortVoiceOperFaxSupported_Type(Integer32):
    """Custom type portVoiceOperFaxSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortVoiceOperFaxSupported_Type.__name__ = "Integer32"
_PortVoiceOperFaxSupported_Object = MibTableColumn
portVoiceOperFaxSupported = _PortVoiceOperFaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 15),
    _PortVoiceOperFaxSupported_Type()
)
portVoiceOperFaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperFaxSupported.setStatus("mandatory")


class _PortVoiceOperTelephonyType_Type(Integer32):
    """Custom type portVoiceOperTelephonyType based on Integer32"""
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
        *(("ac15", 4),
          ("em", 3),
          ("opx", 1),
          ("slt", 2))
    )


_PortVoiceOperTelephonyType_Type.__name__ = "Integer32"
_PortVoiceOperTelephonyType_Object = MibTableColumn
portVoiceOperTelephonyType = _PortVoiceOperTelephonyType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 16),
    _PortVoiceOperTelephonyType_Type()
)
portVoiceOperTelephonyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperTelephonyType.setStatus("mandatory")


class _PortVoiceOperJitter_Type(Integer32):
    """Custom type portVoiceOperJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_PortVoiceOperJitter_Type.__name__ = "Integer32"
_PortVoiceOperJitter_Object = MibTableColumn
portVoiceOperJitter = _PortVoiceOperJitter_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 17),
    _PortVoiceOperJitter_Type()
)
portVoiceOperJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperJitter.setStatus("mandatory")


class _PortVoiceOperSampleDelay_Type(Integer32):
    """Custom type portVoiceOperSampleDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortVoiceOperSampleDelay_Type.__name__ = "Integer32"
_PortVoiceOperSampleDelay_Object = MibTableColumn
portVoiceOperSampleDelay = _PortVoiceOperSampleDelay_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 18),
    _PortVoiceOperSampleDelay_Type()
)
portVoiceOperSampleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperSampleDelay.setStatus("mandatory")


class _PortVoiceOperDialTimer_Type(Integer32):
    """Custom type portVoiceOperDialTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PortVoiceOperDialTimer_Type.__name__ = "Integer32"
_PortVoiceOperDialTimer_Object = MibTableColumn
portVoiceOperDialTimer = _PortVoiceOperDialTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 19),
    _PortVoiceOperDialTimer_Type()
)
portVoiceOperDialTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperDialTimer.setStatus("mandatory")


class _PortVoiceOperAutoDial_Type(Integer32):
    """Custom type portVoiceOperAutoDial based on Integer32"""
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


_PortVoiceOperAutoDial_Type.__name__ = "Integer32"
_PortVoiceOperAutoDial_Object = MibTableColumn
portVoiceOperAutoDial = _PortVoiceOperAutoDial_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 20),
    _PortVoiceOperAutoDial_Type()
)
portVoiceOperAutoDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperAutoDial.setStatus("mandatory")


class _PortVoiceOperSuppression_Type(Integer32):
    """Custom type portVoiceOperSuppression based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("very-high", 5),
          ("very-low", 1))
    )


_PortVoiceOperSuppression_Type.__name__ = "Integer32"
_PortVoiceOperSuppression_Object = MibTableColumn
portVoiceOperSuppression = _PortVoiceOperSuppression_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 21),
    _PortVoiceOperSuppression_Type()
)
portVoiceOperSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperSuppression.setStatus("mandatory")


class _PortVoiceOperAutoDialNumber_Type(OctetString):
    """Custom type portVoiceOperAutoDialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PortVoiceOperAutoDialNumber_Type.__name__ = "OctetString"
_PortVoiceOperAutoDialNumber_Object = MibTableColumn
portVoiceOperAutoDialNumber = _PortVoiceOperAutoDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 22),
    _PortVoiceOperAutoDialNumber_Type()
)
portVoiceOperAutoDialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperAutoDialNumber.setStatus("mandatory")


class _PortVoiceOperAutoPoll_Type(Integer32):
    """Custom type portVoiceOperAutoPoll based on Integer32"""
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


_PortVoiceOperAutoPoll_Type.__name__ = "Integer32"
_PortVoiceOperAutoPoll_Object = MibTableColumn
portVoiceOperAutoPoll = _PortVoiceOperAutoPoll_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 23),
    _PortVoiceOperAutoPoll_Type()
)
portVoiceOperAutoPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperAutoPoll.setStatus("mandatory")


class _PortVoiceOperAutoPollTimer_Type(Integer32):
    """Custom type portVoiceOperAutoPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_PortVoiceOperAutoPollTimer_Type.__name__ = "Integer32"
_PortVoiceOperAutoPollTimer_Object = MibTableColumn
portVoiceOperAutoPollTimer = _PortVoiceOperAutoPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 24),
    _PortVoiceOperAutoPollTimer_Type()
)
portVoiceOperAutoPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperAutoPollTimer.setStatus("mandatory")


class _PortVoiceOperExtDigitsSource_Type(Integer32):
    """Custom type portVoiceOperExtDigitsSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("user", 2))
    )


_PortVoiceOperExtDigitsSource_Type.__name__ = "Integer32"
_PortVoiceOperExtDigitsSource_Object = MibTableColumn
portVoiceOperExtDigitsSource = _PortVoiceOperExtDigitsSource_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 25),
    _PortVoiceOperExtDigitsSource_Type()
)
portVoiceOperExtDigitsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperExtDigitsSource.setStatus("mandatory")


class _PortVoiceOperNumDigitsDelete_Type(Integer32):
    """Custom type portVoiceOperNumDigitsDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PortVoiceOperNumDigitsDelete_Type.__name__ = "Integer32"
_PortVoiceOperNumDigitsDelete_Object = MibTableColumn
portVoiceOperNumDigitsDelete = _PortVoiceOperNumDigitsDelete_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 26),
    _PortVoiceOperNumDigitsDelete_Type()
)
portVoiceOperNumDigitsDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperNumDigitsDelete.setStatus("mandatory")


class _PortVoiceOperForwardDelay_Type(Integer32):
    """Custom type portVoiceOperForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_PortVoiceOperForwardDelay_Type.__name__ = "Integer32"
_PortVoiceOperForwardDelay_Object = MibTableColumn
portVoiceOperForwardDelay = _PortVoiceOperForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 27),
    _PortVoiceOperForwardDelay_Type()
)
portVoiceOperForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperForwardDelay.setStatus("mandatory")


class _PortVoiceOperForwardedType_Type(Integer32):
    """Custom type portVoiceOperForwardedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_PortVoiceOperForwardedType_Type.__name__ = "Integer32"
_PortVoiceOperForwardedType_Object = MibTableColumn
portVoiceOperForwardedType = _PortVoiceOperForwardedType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 28),
    _PortVoiceOperForwardedType_Type()
)
portVoiceOperForwardedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperForwardedType.setStatus("mandatory")


class _PortVoiceOperForwardedDigits_Type(Integer32):
    """Custom type portVoiceOperForwardedDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("extended", 3),
          ("none", 1))
    )


_PortVoiceOperForwardedDigits_Type.__name__ = "Integer32"
_PortVoiceOperForwardedDigits_Object = MibTableColumn
portVoiceOperForwardedDigits = _PortVoiceOperForwardedDigits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 29),
    _PortVoiceOperForwardedDigits_Type()
)
portVoiceOperForwardedDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperForwardedDigits.setStatus("mandatory")


class _PortVoiceOperMakeRatio_Type(Integer32):
    """Custom type portVoiceOperMakeRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 80),
    )


_PortVoiceOperMakeRatio_Type.__name__ = "Integer32"
_PortVoiceOperMakeRatio_Object = MibTableColumn
portVoiceOperMakeRatio = _PortVoiceOperMakeRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 30),
    _PortVoiceOperMakeRatio_Type()
)
portVoiceOperMakeRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperMakeRatio.setStatus("mandatory")


class _PortVoiceOperBreakRatio_Type(Integer32):
    """Custom type portVoiceOperBreakRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 80),
    )


_PortVoiceOperBreakRatio_Type.__name__ = "Integer32"
_PortVoiceOperBreakRatio_Object = MibTableColumn
portVoiceOperBreakRatio = _PortVoiceOperBreakRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 31),
    _PortVoiceOperBreakRatio_Type()
)
portVoiceOperBreakRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperBreakRatio.setStatus("mandatory")


class _PortVoiceOperDTMFOnDuration_Type(Integer32):
    """Custom type portVoiceOperDTMFOnDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_PortVoiceOperDTMFOnDuration_Type.__name__ = "Integer32"
_PortVoiceOperDTMFOnDuration_Object = MibTableColumn
portVoiceOperDTMFOnDuration = _PortVoiceOperDTMFOnDuration_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 32),
    _PortVoiceOperDTMFOnDuration_Type()
)
portVoiceOperDTMFOnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperDTMFOnDuration.setStatus("mandatory")


class _PortVoiceOperDTMFOffDuration_Type(Integer32):
    """Custom type portVoiceOperDTMFOffDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_PortVoiceOperDTMFOffDuration_Type.__name__ = "Integer32"
_PortVoiceOperDTMFOffDuration_Object = MibTableColumn
portVoiceOperDTMFOffDuration = _PortVoiceOperDTMFOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 33),
    _PortVoiceOperDTMFOffDuration_Type()
)
portVoiceOperDTMFOffDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperDTMFOffDuration.setStatus("mandatory")


class _PortVoiceOperToneType_Type(Integer32):
    """Custom type portVoiceOperToneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("mf", 2))
    )


_PortVoiceOperToneType_Type.__name__ = "Integer32"
_PortVoiceOperToneType_Object = MibTableColumn
portVoiceOperToneType = _PortVoiceOperToneType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 3, 8, 2, 1, 34),
    _PortVoiceOperToneType_Type()
)
portVoiceOperToneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoiceOperToneType.setStatus("mandatory")
_NlInterfaces_ObjectIdentity = ObjectIdentity
nlInterfaces = _NlInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4)
)
_NlIfTable_Object = MibTable
nlIfTable = _NlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1)
)
if mibBuilder.loadTexts:
    nlIfTable.setStatus("mandatory")
_NlIfEntry_Object = MibTableRow
nlIfEntry = _NlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1)
)
nlIfEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfPort"),
)
if mibBuilder.loadTexts:
    nlIfEntry.setStatus("mandatory")
_NlIfRlp_Type = Integer32
_NlIfRlp_Object = MibTableColumn
nlIfRlp = _NlIfRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 1),
    _NlIfRlp_Type()
)
nlIfRlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfRlp.setStatus("mandatory")
_NlIfPort_Type = Integer32
_NlIfPort_Object = MibTableColumn
nlIfPort = _NlIfPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 2),
    _NlIfPort_Type()
)
nlIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfPort.setStatus("mandatory")


class _NlIfType_Type(Integer32):
    """Custom type nlIfType based on Integer32"""
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
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("async", 201),
          ("atm", 37),
          ("basicISDN", 20),
          ("bsci", 202),
          ("ddnX25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("ip", 205),
          ("ipx", 206),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("llc2", 207),
          ("localTalk", 42),
          ("logicalPort", 203),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("t1", 204),
          ("trunk", 200),
          ("ultra", 29),
          ("v35", 45),
          ("voice", 208),
          ("x25ple", 40))
    )


_NlIfType_Type.__name__ = "Integer32"
_NlIfType_Object = MibTableColumn
nlIfType = _NlIfType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 3),
    _NlIfType_Type()
)
nlIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfType.setStatus("mandatory")
_NlIfIndex_Type = Integer32
_NlIfIndex_Object = MibTableColumn
nlIfIndex = _NlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 4),
    _NlIfIndex_Type()
)
nlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfIndex.setStatus("mandatory")
_NlIfTableIndex_Type = Integer32
_NlIfTableIndex_Object = MibTableColumn
nlIfTableIndex = _NlIfTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 5),
    _NlIfTableIndex_Type()
)
nlIfTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfTableIndex.setStatus("mandatory")
_NlIfTableOid_Type = ObjectIdentifier
_NlIfTableOid_Object = MibTableColumn
nlIfTableOid = _NlIfTableOid_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 6),
    _NlIfTableOid_Type()
)
nlIfTableOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfTableOid.setStatus("mandatory")


class _NlIfConnectorType_Type(Integer32):
    """Custom type nlIfConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("csudsu", 9),
          ("e1", 11),
          ("none", 2),
          ("rs232", 3),
          ("rs449", 6),
          ("rs530", 7),
          ("t1", 10),
          ("v25bis-dial", 4),
          ("v35", 5),
          ("voice", 13),
          ("x21", 8))
    )


_NlIfConnectorType_Type.__name__ = "Integer32"
_NlIfConnectorType_Object = MibTableColumn
nlIfConnectorType = _NlIfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 7),
    _NlIfConnectorType_Type()
)
nlIfConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfConnectorType.setStatus("mandatory")


class _NlIfPortStatus_Type(Integer32):
    """Custom type nlIfPortStatus based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("activeVoiceCall", 21),
          ("blueAlarm", 15),
          ("configured", 6),
          ("dialReady", 7),
          ("dialing", 20),
          ("disabled", 4),
          ("disconnect", 5),
          ("failed", 9),
          ("hardwareFault", 10),
          ("ipl", 12),
          ("linkUp", 1),
          ("na", 13),
          ("offHook", 19),
          ("onHook", 18),
          ("onHookPending", 22),
          ("operational", 3),
          ("other", 11),
          ("quiesced", 8),
          ("redAlarm", 17),
          ("remoteLoopback", 14),
          ("restarting", 2),
          ("yellowAlarm", 16))
    )


_NlIfPortStatus_Type.__name__ = "Integer32"
_NlIfPortStatus_Object = MibTableColumn
nlIfPortStatus = _NlIfPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 8),
    _NlIfPortStatus_Type()
)
nlIfPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfPortStatus.setStatus("mandatory")
_NlIfPhyPort_Type = Integer32
_NlIfPhyPort_Object = MibTableColumn
nlIfPhyPort = _NlIfPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 1, 1, 9),
    _NlIfPhyPort_Type()
)
nlIfPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfPhyPort.setStatus("mandatory")
_NlIfLlc2Interfaces_ObjectIdentity = ObjectIdentity
nlIfLlc2Interfaces = _NlIfLlc2Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2)
)
_NlIfLlc2LANTable_Object = MibTable
nlIfLlc2LANTable = _NlIfLlc2LANTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nlIfLlc2LANTable.setStatus("mandatory")
_NlIfLlc2LANEntry_Object = MibTableRow
nlIfLlc2LANEntry = _NlIfLlc2LANEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1)
)
nlIfLlc2LANEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2LANRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2LANPort"),
)
if mibBuilder.loadTexts:
    nlIfLlc2LANEntry.setStatus("mandatory")
_NlIfLlc2LANRlp_Type = Integer32
_NlIfLlc2LANRlp_Object = MibTableColumn
nlIfLlc2LANRlp = _NlIfLlc2LANRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 1),
    _NlIfLlc2LANRlp_Type()
)
nlIfLlc2LANRlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2LANRlp.setStatus("mandatory")
_NlIfLlc2LANPort_Type = Integer32
_NlIfLlc2LANPort_Object = MibTableColumn
nlIfLlc2LANPort = _NlIfLlc2LANPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 2),
    _NlIfLlc2LANPort_Type()
)
nlIfLlc2LANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2LANPort.setStatus("mandatory")


class _NlIfLlc2LANType_Type(Integer32):
    """Custom type nlIfLlc2LANType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("token-ring", 2))
    )


_NlIfLlc2LANType_Type.__name__ = "Integer32"
_NlIfLlc2LANType_Object = MibTableColumn
nlIfLlc2LANType = _NlIfLlc2LANType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 3),
    _NlIfLlc2LANType_Type()
)
nlIfLlc2LANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2LANType.setStatus("mandatory")


class _NlIfLlc2LANCard_Type(Integer32):
    """Custom type nlIfLlc2LANCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NlIfLlc2LANCard_Type.__name__ = "Integer32"
_NlIfLlc2LANCard_Object = MibTableColumn
nlIfLlc2LANCard = _NlIfLlc2LANCard_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 4),
    _NlIfLlc2LANCard_Type()
)
nlIfLlc2LANCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2LANCard.setStatus("mandatory")


class _NlIfLlc2LANID_Type(Integer32):
    """Custom type nlIfLlc2LANID based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NlIfLlc2LANID_Type.__name__ = "Integer32"
_NlIfLlc2LANID_Object = MibTableColumn
nlIfLlc2LANID = _NlIfLlc2LANID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 5),
    _NlIfLlc2LANID_Type()
)
nlIfLlc2LANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2LANID.setStatus("mandatory")


class _NlIfLlc2LANInterface_Type(Integer32):
    """Custom type nlIfLlc2LANInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NlIfLlc2LANInterface_Type.__name__ = "Integer32"
_NlIfLlc2LANInterface_Object = MibTableColumn
nlIfLlc2LANInterface = _NlIfLlc2LANInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 6),
    _NlIfLlc2LANInterface_Type()
)
nlIfLlc2LANInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2LANInterface.setStatus("mandatory")
_NlIfLlc2LANRowStatus_Type = RowStatus
_NlIfLlc2LANRowStatus_Object = MibTableColumn
nlIfLlc2LANRowStatus = _NlIfLlc2LANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 7),
    _NlIfLlc2LANRowStatus_Type()
)
nlIfLlc2LANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2LANRowStatus.setStatus("mandatory")


class _NlIfLlc2LANPriority_Type(Integer32):
    """Custom type nlIfLlc2LANPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NlIfLlc2LANPriority_Type.__name__ = "Integer32"
_NlIfLlc2LANPriority_Object = MibTableColumn
nlIfLlc2LANPriority = _NlIfLlc2LANPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 8),
    _NlIfLlc2LANPriority_Type()
)
nlIfLlc2LANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2LANPriority.setStatus("mandatory")


class _NlIfLlc2LANBlockedPortFlag_Type(Integer32):
    """Custom type nlIfLlc2LANBlockedPortFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfLlc2LANBlockedPortFlag_Type.__name__ = "Integer32"
_NlIfLlc2LANBlockedPortFlag_Object = MibTableColumn
nlIfLlc2LANBlockedPortFlag = _NlIfLlc2LANBlockedPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 1, 1, 9),
    _NlIfLlc2LANBlockedPortFlag_Type()
)
nlIfLlc2LANBlockedPortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2LANBlockedPortFlag.setStatus("mandatory")
_NlIfLlc2FrTable_Object = MibTable
nlIfLlc2FrTable = _NlIfLlc2FrTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    nlIfLlc2FrTable.setStatus("mandatory")
_NlIfLlc2FrEntry_Object = MibTableRow
nlIfLlc2FrEntry = _NlIfLlc2FrEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1)
)
nlIfLlc2FrEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2FrRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2FrPort"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2FrDLCI"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfLlc2FrFormat"),
)
if mibBuilder.loadTexts:
    nlIfLlc2FrEntry.setStatus("mandatory")


class _NlIfLlc2FrRlp_Type(Integer32):
    """Custom type nlIfLlc2FrRlp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfLlc2FrRlp_Type.__name__ = "Integer32"
_NlIfLlc2FrRlp_Object = MibTableColumn
nlIfLlc2FrRlp = _NlIfLlc2FrRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 1),
    _NlIfLlc2FrRlp_Type()
)
nlIfLlc2FrRlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2FrRlp.setStatus("mandatory")


class _NlIfLlc2FrPort_Type(Integer32):
    """Custom type nlIfLlc2FrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NlIfLlc2FrPort_Type.__name__ = "Integer32"
_NlIfLlc2FrPort_Object = MibTableColumn
nlIfLlc2FrPort = _NlIfLlc2FrPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 2),
    _NlIfLlc2FrPort_Type()
)
nlIfLlc2FrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2FrPort.setStatus("mandatory")


class _NlIfLlc2FrDLCI_Type(Integer32):
    """Custom type nlIfLlc2FrDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NlIfLlc2FrDLCI_Type.__name__ = "Integer32"
_NlIfLlc2FrDLCI_Object = MibTableColumn
nlIfLlc2FrDLCI = _NlIfLlc2FrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 3),
    _NlIfLlc2FrDLCI_Type()
)
nlIfLlc2FrDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2FrDLCI.setStatus("mandatory")


class _NlIfLlc2FrFormat_Type(Integer32):
    """Custom type nlIfLlc2FrFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("native-llc2", 1),
          ("srb-8025", 3),
          ("tb-8023", 2))
    )


_NlIfLlc2FrFormat_Type.__name__ = "Integer32"
_NlIfLlc2FrFormat_Object = MibTableColumn
nlIfLlc2FrFormat = _NlIfLlc2FrFormat_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 4),
    _NlIfLlc2FrFormat_Type()
)
nlIfLlc2FrFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2FrFormat.setStatus("mandatory")


class _NlIfLlc2FrPriority_Type(Integer32):
    """Custom type nlIfLlc2FrPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NlIfLlc2FrPriority_Type.__name__ = "Integer32"
_NlIfLlc2FrPriority_Object = MibTableColumn
nlIfLlc2FrPriority = _NlIfLlc2FrPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 5),
    _NlIfLlc2FrPriority_Type()
)
nlIfLlc2FrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrPriority.setStatus("mandatory")


class _NlIfLlc2FrBAG_Type(Integer32):
    """Custom type nlIfLlc2FrBAG based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NlIfLlc2FrBAG_Type.__name__ = "Integer32"
_NlIfLlc2FrBAG_Object = MibTableColumn
nlIfLlc2FrBAG = _NlIfLlc2FrBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 6),
    _NlIfLlc2FrBAG_Type()
)
nlIfLlc2FrBAG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrBAG.setStatus("mandatory")


class _NlIfLlc2FrHostMACAddress_Type(MacAddress):
    """Custom type nlIfLlc2FrHostMACAddress based on MacAddress"""
    defaultHexValue = "400000000001"


_NlIfLlc2FrHostMACAddress_Object = MibTableColumn
nlIfLlc2FrHostMACAddress = _NlIfLlc2FrHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 7),
    _NlIfLlc2FrHostMACAddress_Type()
)
nlIfLlc2FrHostMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrHostMACAddress.setStatus("mandatory")


class _NlIfLlc2FrSessionType_Type(Integer32):
    """Custom type nlIfLlc2FrSessionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("originated", 2),
          ("terminated", 1))
    )


_NlIfLlc2FrSessionType_Type.__name__ = "Integer32"
_NlIfLlc2FrSessionType_Object = MibTableColumn
nlIfLlc2FrSessionType = _NlIfLlc2FrSessionType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 8),
    _NlIfLlc2FrSessionType_Type()
)
nlIfLlc2FrSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrSessionType.setStatus("mandatory")


class _NlIfLlc2FrLANID_Type(Integer32):
    """Custom type nlIfLlc2FrLANID based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NlIfLlc2FrLANID_Type.__name__ = "Integer32"
_NlIfLlc2FrLANID_Object = MibTableColumn
nlIfLlc2FrLANID = _NlIfLlc2FrLANID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 9),
    _NlIfLlc2FrLANID_Type()
)
nlIfLlc2FrLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrLANID.setStatus("mandatory")
_NlIfLlc2FrInterface_Type = Integer32
_NlIfLlc2FrInterface_Object = MibTableColumn
nlIfLlc2FrInterface = _NlIfLlc2FrInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 10),
    _NlIfLlc2FrInterface_Type()
)
nlIfLlc2FrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfLlc2FrInterface.setStatus("mandatory")
_NlIfLlc2FrRowStatus_Type = RowStatus
_NlIfLlc2FrRowStatus_Object = MibTableColumn
nlIfLlc2FrRowStatus = _NlIfLlc2FrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 11),
    _NlIfLlc2FrRowStatus_Type()
)
nlIfLlc2FrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrRowStatus.setStatus("mandatory")


class _NlIfLlc2FrBlockedPortFlag_Type(Integer32):
    """Custom type nlIfLlc2FrBlockedPortFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfLlc2FrBlockedPortFlag_Type.__name__ = "Integer32"
_NlIfLlc2FrBlockedPortFlag_Object = MibTableColumn
nlIfLlc2FrBlockedPortFlag = _NlIfLlc2FrBlockedPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 2, 2, 1, 12),
    _NlIfLlc2FrBlockedPortFlag_Type()
)
nlIfLlc2FrBlockedPortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfLlc2FrBlockedPortFlag.setStatus("mandatory")
_IpxConfig_ObjectIdentity = ObjectIdentity
ipxConfig = _IpxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3)
)
_IpxConfigRouting_ObjectIdentity = ObjectIdentity
ipxConfigRouting = _IpxConfigRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1)
)
_IpxStaticRouteConfigTable_Object = MibTable
ipxStaticRouteConfigTable = _IpxStaticRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipxStaticRouteConfigTable.setStatus("mandatory")
_IpxStaticRouteConfigEntry_Object = MibTableRow
ipxStaticRouteConfigEntry = _IpxStaticRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1, 1)
)
ipxStaticRouteConfigEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "ipxStaticRouteConfigCircIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "ipxStaticRouteConfigNetNum"),
)
if mibBuilder.loadTexts:
    ipxStaticRouteConfigEntry.setStatus("mandatory")


class _IpxStaticRouteConfigCircIndex_Type(Integer32):
    """Custom type ipxStaticRouteConfigCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxStaticRouteConfigCircIndex_Type.__name__ = "Integer32"
_IpxStaticRouteConfigCircIndex_Object = MibTableColumn
ipxStaticRouteConfigCircIndex = _IpxStaticRouteConfigCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1, 1, 1),
    _IpxStaticRouteConfigCircIndex_Type()
)
ipxStaticRouteConfigCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticRouteConfigCircIndex.setStatus("mandatory")


class _IpxStaticRouteConfigNetNum_Type(OctetString):
    """Custom type ipxStaticRouteConfigNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxStaticRouteConfigNetNum_Type.__name__ = "OctetString"
_IpxStaticRouteConfigNetNum_Object = MibTableColumn
ipxStaticRouteConfigNetNum = _IpxStaticRouteConfigNetNum_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1, 1, 2),
    _IpxStaticRouteConfigNetNum_Type()
)
ipxStaticRouteConfigNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStaticRouteConfigNetNum.setStatus("mandatory")


class _IpxStaticRouteConfigRouter_Type(OctetString):
    """Custom type ipxStaticRouteConfigRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxStaticRouteConfigRouter_Type.__name__ = "OctetString"
_IpxStaticRouteConfigRouter_Object = MibTableColumn
ipxStaticRouteConfigRouter = _IpxStaticRouteConfigRouter_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1, 1, 3),
    _IpxStaticRouteConfigRouter_Type()
)
ipxStaticRouteConfigRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteConfigRouter.setStatus("mandatory")
_IpxStaticRouteConfigRowStatus_Type = RowStatus
_IpxStaticRouteConfigRowStatus_Object = MibTableColumn
ipxStaticRouteConfigRowStatus = _IpxStaticRouteConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 1, 1, 4),
    _IpxStaticRouteConfigRowStatus_Type()
)
ipxStaticRouteConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteConfigRowStatus.setStatus("mandatory")
_IpxServConfigTable_Object = MibTable
ipxServConfigTable = _IpxServConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipxServConfigTable.setStatus("mandatory")
_IpxServConfigEntry_Object = MibTableRow
ipxServConfigEntry = _IpxServConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1)
)
ipxServConfigEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "ipxServConfigServiceType"),
    (0, "NETLINK-SPECIFIC-MIB", "ipxServConfigServName"),
)
if mibBuilder.loadTexts:
    ipxServConfigEntry.setStatus("mandatory")


class _IpxServConfigServiceType_Type(Integer32):
    """Custom type ipxServConfigServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxServConfigServiceType_Type.__name__ = "Integer32"
_IpxServConfigServiceType_Object = MibTableColumn
ipxServConfigServiceType = _IpxServConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 1),
    _IpxServConfigServiceType_Type()
)
ipxServConfigServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServConfigServiceType.setStatus("mandatory")


class _IpxServConfigServName_Type(OctetString):
    """Custom type ipxServConfigServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServConfigServName_Type.__name__ = "OctetString"
_IpxServConfigServName_Object = MibTableColumn
ipxServConfigServName = _IpxServConfigServName_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 2),
    _IpxServConfigServName_Type()
)
ipxServConfigServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServConfigServName.setStatus("mandatory")


class _IpxServConfigServNetworkAddress_Type(Integer32):
    """Custom type ipxServConfigServNetworkAddress based on Integer32"""
    defaultValue = 1


_IpxServConfigServNetworkAddress_Object = MibTableColumn
ipxServConfigServNetworkAddress = _IpxServConfigServNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 3),
    _IpxServConfigServNetworkAddress_Type()
)
ipxServConfigServNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigServNetworkAddress.setStatus("mandatory")


class _IpxServConfigServNodeAddress_Type(OctetString):
    """Custom type ipxServConfigServNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServConfigServNodeAddress_Type.__name__ = "OctetString"
_IpxServConfigServNodeAddress_Object = MibTableColumn
ipxServConfigServNodeAddress = _IpxServConfigServNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 4),
    _IpxServConfigServNodeAddress_Type()
)
ipxServConfigServNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigServNodeAddress.setStatus("mandatory")


class _IpxServConfigServSocketNumber_Type(Integer32):
    """Custom type ipxServConfigServSocketNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxServConfigServSocketNumber_Type.__name__ = "Integer32"
_IpxServConfigServSocketNumber_Object = MibTableColumn
ipxServConfigServSocketNumber = _IpxServConfigServSocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 5),
    _IpxServConfigServSocketNumber_Type()
)
ipxServConfigServSocketNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigServSocketNumber.setStatus("mandatory")


class _IpxServConfigInterveningNetworks_Type(Integer32):
    """Custom type ipxServConfigInterveningNetworks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxServConfigInterveningNetworks_Type.__name__ = "Integer32"
_IpxServConfigInterveningNetworks_Object = MibTableColumn
ipxServConfigInterveningNetworks = _IpxServConfigInterveningNetworks_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 6),
    _IpxServConfigInterveningNetworks_Type()
)
ipxServConfigInterveningNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigInterveningNetworks.setStatus("mandatory")


class _IpxServConfigGatewayAddress_Type(OctetString):
    """Custom type ipxServConfigGatewayAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServConfigGatewayAddress_Type.__name__ = "OctetString"
_IpxServConfigGatewayAddress_Object = MibTableColumn
ipxServConfigGatewayAddress = _IpxServConfigGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 7),
    _IpxServConfigGatewayAddress_Type()
)
ipxServConfigGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigGatewayAddress.setStatus("mandatory")


class _IpxServConfigInterface_Type(Integer32):
    """Custom type ipxServConfigInterface based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxServConfigInterface_Type.__name__ = "Integer32"
_IpxServConfigInterface_Object = MibTableColumn
ipxServConfigInterface = _IpxServConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 8),
    _IpxServConfigInterface_Type()
)
ipxServConfigInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigInterface.setStatus("mandatory")
_IpxServConfigRowStatus_Type = RowStatus
_IpxServConfigRowStatus_Object = MibTableColumn
ipxServConfigRowStatus = _IpxServConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 1, 2, 1, 9),
    _IpxServConfigRowStatus_Type()
)
ipxServConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServConfigRowStatus.setStatus("mandatory")
_IpxConfigInterface_ObjectIdentity = ObjectIdentity
ipxConfigInterface = _IpxConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2)
)
_IpxInterfaceTable_Object = MibTable
ipxInterfaceTable = _IpxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6)
)
if mibBuilder.loadTexts:
    ipxInterfaceTable.setStatus("mandatory")
_IpxInterfaceEntry_Object = MibTableRow
ipxInterfaceEntry = _IpxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1)
)
ipxInterfaceEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "ipxInterfaceNumber"),
)
if mibBuilder.loadTexts:
    ipxInterfaceEntry.setStatus("mandatory")


class _IpxInterfaceNumber_Type(Integer32):
    """Custom type ipxInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpxInterfaceNumber_Type.__name__ = "Integer32"
_IpxInterfaceNumber_Object = MibTableColumn
ipxInterfaceNumber = _IpxInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 1),
    _IpxInterfaceNumber_Type()
)
ipxInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceNumber.setStatus("mandatory")


class _IpxInterfaceBlockedPortFlag_Type(Integer32):
    """Custom type ipxInterfaceBlockedPortFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceBlockedPortFlag_Type.__name__ = "Integer32"
_IpxInterfaceBlockedPortFlag_Object = MibTableColumn
ipxInterfaceBlockedPortFlag = _IpxInterfaceBlockedPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 2),
    _IpxInterfaceBlockedPortFlag_Type()
)
ipxInterfaceBlockedPortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceBlockedPortFlag.setStatus("mandatory")


class _IpxInterfaceType_Type(Integer32):
    """Custom type ipxInterfaceType based on Integer32"""
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
        *(("eight025", 2),
          ("ethernet", 1),
          ("frl", 4),
          ("x25", 3))
    )


_IpxInterfaceType_Type.__name__ = "Integer32"
_IpxInterfaceType_Object = MibTableColumn
ipxInterfaceType = _IpxInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 3),
    _IpxInterfaceType_Type()
)
ipxInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceType.setStatus("mandatory")


class _IpxInterfaceFrameType_Type(Integer32):
    """Custom type ipxInterfaceFrameType based on Integer32"""
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
        *(("llc", 3),
          ("raw", 2),
          ("snap", 4),
          ("typeII", 1))
    )


_IpxInterfaceFrameType_Type.__name__ = "Integer32"
_IpxInterfaceFrameType_Object = MibTableColumn
ipxInterfaceFrameType = _IpxInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 4),
    _IpxInterfaceFrameType_Type()
)
ipxInterfaceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceFrameType.setStatus("mandatory")


class _IpxInterfaceMaxTransUnit_Type(Integer32):
    """Custom type ipxInterfaceMaxTransUnit based on Integer32"""
    defaultValue = 4096


_IpxInterfaceMaxTransUnit_Object = MibTableColumn
ipxInterfaceMaxTransUnit = _IpxInterfaceMaxTransUnit_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 5),
    _IpxInterfaceMaxTransUnit_Type()
)
ipxInterfaceMaxTransUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceMaxTransUnit.setStatus("mandatory")


class _IpxInterfaceNetworkAddress_Type(Integer32):
    """Custom type ipxInterfaceNetworkAddress based on Integer32"""
    defaultValue = 0


_IpxInterfaceNetworkAddress_Object = MibTableColumn
ipxInterfaceNetworkAddress = _IpxInterfaceNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 6),
    _IpxInterfaceNetworkAddress_Type()
)
ipxInterfaceNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceNetworkAddress.setStatus("mandatory")


class _IpxInterfaceBandwidthAllocGroup_Type(Integer32):
    """Custom type ipxInterfaceBandwidthAllocGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpxInterfaceBandwidthAllocGroup_Type.__name__ = "Integer32"
_IpxInterfaceBandwidthAllocGroup_Object = MibTableColumn
ipxInterfaceBandwidthAllocGroup = _IpxInterfaceBandwidthAllocGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 7),
    _IpxInterfaceBandwidthAllocGroup_Type()
)
ipxInterfaceBandwidthAllocGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceBandwidthAllocGroup.setStatus("mandatory")


class _IpxInterfacePortDiagEnabled_Type(Integer32):
    """Custom type ipxInterfacePortDiagEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfacePortDiagEnabled_Type.__name__ = "Integer32"
_IpxInterfacePortDiagEnabled_Object = MibTableColumn
ipxInterfacePortDiagEnabled = _IpxInterfacePortDiagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 8),
    _IpxInterfacePortDiagEnabled_Type()
)
ipxInterfacePortDiagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePortDiagEnabled.setStatus("mandatory")


class _IpxInterfaceNetBIOSEnabled_Type(Integer32):
    """Custom type ipxInterfaceNetBIOSEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceNetBIOSEnabled_Type.__name__ = "Integer32"
_IpxInterfaceNetBIOSEnabled_Object = MibTableColumn
ipxInterfaceNetBIOSEnabled = _IpxInterfaceNetBIOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 9),
    _IpxInterfaceNetBIOSEnabled_Type()
)
ipxInterfaceNetBIOSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceNetBIOSEnabled.setStatus("mandatory")


class _IpxInterfaceNetBIOSHops_Type(Integer32):
    """Custom type ipxInterfaceNetBIOSHops based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpxInterfaceNetBIOSHops_Type.__name__ = "Integer32"
_IpxInterfaceNetBIOSHops_Object = MibTableColumn
ipxInterfaceNetBIOSHops = _IpxInterfaceNetBIOSHops_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 10),
    _IpxInterfaceNetBIOSHops_Type()
)
ipxInterfaceNetBIOSHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceNetBIOSHops.setStatus("mandatory")


class _IpxInterfacePeriodicRIPEnabled_Type(Integer32):
    """Custom type ipxInterfacePeriodicRIPEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfacePeriodicRIPEnabled_Type.__name__ = "Integer32"
_IpxInterfacePeriodicRIPEnabled_Object = MibTableColumn
ipxInterfacePeriodicRIPEnabled = _IpxInterfacePeriodicRIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 11),
    _IpxInterfacePeriodicRIPEnabled_Type()
)
ipxInterfacePeriodicRIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePeriodicRIPEnabled.setStatus("mandatory")


class _IpxInterfacePeriodicRIPTimer_Type(Integer32):
    """Custom type ipxInterfacePeriodicRIPTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxInterfacePeriodicRIPTimer_Type.__name__ = "Integer32"
_IpxInterfacePeriodicRIPTimer_Object = MibTableColumn
ipxInterfacePeriodicRIPTimer = _IpxInterfacePeriodicRIPTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 12),
    _IpxInterfacePeriodicRIPTimer_Type()
)
ipxInterfacePeriodicRIPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePeriodicRIPTimer.setStatus("mandatory")


class _IpxInterfacePeriodicSAPEnabled_Type(Integer32):
    """Custom type ipxInterfacePeriodicSAPEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfacePeriodicSAPEnabled_Type.__name__ = "Integer32"
_IpxInterfacePeriodicSAPEnabled_Object = MibTableColumn
ipxInterfacePeriodicSAPEnabled = _IpxInterfacePeriodicSAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 13),
    _IpxInterfacePeriodicSAPEnabled_Type()
)
ipxInterfacePeriodicSAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePeriodicSAPEnabled.setStatus("mandatory")


class _IpxInterfacePeriodicSAPTimer_Type(Integer32):
    """Custom type ipxInterfacePeriodicSAPTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxInterfacePeriodicSAPTimer_Type.__name__ = "Integer32"
_IpxInterfacePeriodicSAPTimer_Object = MibTableColumn
ipxInterfacePeriodicSAPTimer = _IpxInterfacePeriodicSAPTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 14),
    _IpxInterfacePeriodicSAPTimer_Type()
)
ipxInterfacePeriodicSAPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePeriodicSAPTimer.setStatus("mandatory")


class _IpxInterfaceRIPEnabled_Type(Integer32):
    """Custom type ipxInterfaceRIPEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceRIPEnabled_Type.__name__ = "Integer32"
_IpxInterfaceRIPEnabled_Object = MibTableColumn
ipxInterfaceRIPEnabled = _IpxInterfaceRIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 15),
    _IpxInterfaceRIPEnabled_Type()
)
ipxInterfaceRIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceRIPEnabled.setStatus("mandatory")


class _IpxInterfaceRIPAgeTimer_Type(Integer32):
    """Custom type ipxInterfaceRIPAgeTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxInterfaceRIPAgeTimer_Type.__name__ = "Integer32"
_IpxInterfaceRIPAgeTimer_Object = MibTableColumn
ipxInterfaceRIPAgeTimer = _IpxInterfaceRIPAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 16),
    _IpxInterfaceRIPAgeTimer_Type()
)
ipxInterfaceRIPAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceRIPAgeTimer.setStatus("mandatory")


class _IpxInterfaceRIPMaxSize_Type(Integer32):
    """Custom type ipxInterfaceRIPMaxSize based on Integer32"""
    defaultValue = 446

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(54, 446),
    )


_IpxInterfaceRIPMaxSize_Type.__name__ = "Integer32"
_IpxInterfaceRIPMaxSize_Object = MibTableColumn
ipxInterfaceRIPMaxSize = _IpxInterfaceRIPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 17),
    _IpxInterfaceRIPMaxSize_Type()
)
ipxInterfaceRIPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceRIPMaxSize.setStatus("mandatory")


class _IpxInterfaceSAPEnabled_Type(Integer32):
    """Custom type ipxInterfaceSAPEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceSAPEnabled_Type.__name__ = "Integer32"
_IpxInterfaceSAPEnabled_Object = MibTableColumn
ipxInterfaceSAPEnabled = _IpxInterfaceSAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 18),
    _IpxInterfaceSAPEnabled_Type()
)
ipxInterfaceSAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSAPEnabled.setStatus("mandatory")


class _IpxInterfaceSAPAgeTimer_Type(Integer32):
    """Custom type ipxInterfaceSAPAgeTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxInterfaceSAPAgeTimer_Type.__name__ = "Integer32"
_IpxInterfaceSAPAgeTimer_Object = MibTableColumn
ipxInterfaceSAPAgeTimer = _IpxInterfaceSAPAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 19),
    _IpxInterfaceSAPAgeTimer_Type()
)
ipxInterfaceSAPAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSAPAgeTimer.setStatus("mandatory")


class _IpxInterfaceTransportTime_Type(Integer32):
    """Custom type ipxInterfaceTransportTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpxInterfaceTransportTime_Type.__name__ = "Integer32"
_IpxInterfaceTransportTime_Object = MibTableColumn
ipxInterfaceTransportTime = _IpxInterfaceTransportTime_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 20),
    _IpxInterfaceTransportTime_Type()
)
ipxInterfaceTransportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceTransportTime.setStatus("mandatory")


class _IpxInterfaceSerializationEnabled_Type(Integer32):
    """Custom type ipxInterfaceSerializationEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceSerializationEnabled_Type.__name__ = "Integer32"
_IpxInterfaceSerializationEnabled_Object = MibTableColumn
ipxInterfaceSerializationEnabled = _IpxInterfaceSerializationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 21),
    _IpxInterfaceSerializationEnabled_Type()
)
ipxInterfaceSerializationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSerializationEnabled.setStatus("mandatory")


class _IpxInterfaceWatchdogSpoofingEnabled_Type(Integer32):
    """Custom type ipxInterfaceWatchdogSpoofingEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxInterfaceWatchdogSpoofingEnabled_Type.__name__ = "Integer32"
_IpxInterfaceWatchdogSpoofingEnabled_Object = MibTableColumn
ipxInterfaceWatchdogSpoofingEnabled = _IpxInterfaceWatchdogSpoofingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 22),
    _IpxInterfaceWatchdogSpoofingEnabled_Type()
)
ipxInterfaceWatchdogSpoofingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceWatchdogSpoofingEnabled.setStatus("mandatory")


class _IpxInterfaceLanCardNumber_Type(Integer32):
    """Custom type ipxInterfaceLanCardNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpxInterfaceLanCardNumber_Type.__name__ = "Integer32"
_IpxInterfaceLanCardNumber_Object = MibTableColumn
ipxInterfaceLanCardNumber = _IpxInterfaceLanCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 23),
    _IpxInterfaceLanCardNumber_Type()
)
ipxInterfaceLanCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceLanCardNumber.setStatus("mandatory")


class _IpxInterfaceWanEnabled_Type(Integer32):
    """Custom type ipxInterfaceWanEnabled based on Integer32"""
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
        *(("no", 1),
          ("not-applicable", 3),
          ("yes", 2))
    )


_IpxInterfaceWanEnabled_Type.__name__ = "Integer32"
_IpxInterfaceWanEnabled_Object = MibTableColumn
ipxInterfaceWanEnabled = _IpxInterfaceWanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 24),
    _IpxInterfaceWanEnabled_Type()
)
ipxInterfaceWanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceWanEnabled.setStatus("mandatory")


class _IpxInterfaceSourceSubscriber_Type(OctetString):
    """Custom type ipxInterfaceSourceSubscriber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IpxInterfaceSourceSubscriber_Type.__name__ = "OctetString"
_IpxInterfaceSourceSubscriber_Object = MibTableColumn
ipxInterfaceSourceSubscriber = _IpxInterfaceSourceSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 25),
    _IpxInterfaceSourceSubscriber_Type()
)
ipxInterfaceSourceSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSourceSubscriber.setStatus("mandatory")


class _IpxInterfaceDestinationSubscriber_Type(OctetString):
    """Custom type ipxInterfaceDestinationSubscriber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IpxInterfaceDestinationSubscriber_Type.__name__ = "OctetString"
_IpxInterfaceDestinationSubscriber_Object = MibTableColumn
ipxInterfaceDestinationSubscriber = _IpxInterfaceDestinationSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 26),
    _IpxInterfaceDestinationSubscriber_Type()
)
ipxInterfaceDestinationSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceDestinationSubscriber.setStatus("mandatory")


class _IpxInterfaceSVCRetryTimer_Type(Integer32):
    """Custom type ipxInterfaceSVCRetryTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_IpxInterfaceSVCRetryTimer_Type.__name__ = "Integer32"
_IpxInterfaceSVCRetryTimer_Object = MibTableColumn
ipxInterfaceSVCRetryTimer = _IpxInterfaceSVCRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 27),
    _IpxInterfaceSVCRetryTimer_Type()
)
ipxInterfaceSVCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSVCRetryTimer.setStatus("mandatory")


class _IpxInterfaceSVCIdleTimer_Type(Integer32):
    """Custom type ipxInterfaceSVCIdleTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_IpxInterfaceSVCIdleTimer_Type.__name__ = "Integer32"
_IpxInterfaceSVCIdleTimer_Object = MibTableColumn
ipxInterfaceSVCIdleTimer = _IpxInterfaceSVCIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 28),
    _IpxInterfaceSVCIdleTimer_Type()
)
ipxInterfaceSVCIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSVCIdleTimer.setStatus("mandatory")


class _IpxInterfaceMaxVC_Type(Integer32):
    """Custom type ipxInterfaceMaxVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpxInterfaceMaxVC_Type.__name__ = "Integer32"
_IpxInterfaceMaxVC_Object = MibTableColumn
ipxInterfaceMaxVC = _IpxInterfaceMaxVC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 29),
    _IpxInterfaceMaxVC_Type()
)
ipxInterfaceMaxVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceMaxVC.setStatus("mandatory")


class _IpxInterfacePVCConnection_Type(Integer32):
    """Custom type ipxInterfacePVCConnection based on Integer32"""
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
        *(("no", 1),
          ("not-applicable", 3),
          ("yes", 2))
    )


_IpxInterfacePVCConnection_Type.__name__ = "Integer32"
_IpxInterfacePVCConnection_Object = MibTableColumn
ipxInterfacePVCConnection = _IpxInterfacePVCConnection_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 30),
    _IpxInterfacePVCConnection_Type()
)
ipxInterfacePVCConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfacePVCConnection.setStatus("mandatory")


class _IpxInterfaceSourceCard_Type(Integer32):
    """Custom type ipxInterfaceSourceCard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpxInterfaceSourceCard_Type.__name__ = "Integer32"
_IpxInterfaceSourceCard_Object = MibTableColumn
ipxInterfaceSourceCard = _IpxInterfaceSourceCard_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 31),
    _IpxInterfaceSourceCard_Type()
)
ipxInterfaceSourceCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSourceCard.setStatus("mandatory")


class _IpxInterfaceSourcePort_Type(Integer32):
    """Custom type ipxInterfaceSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpxInterfaceSourcePort_Type.__name__ = "Integer32"
_IpxInterfaceSourcePort_Object = MibTableColumn
ipxInterfaceSourcePort = _IpxInterfaceSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 32),
    _IpxInterfaceSourcePort_Type()
)
ipxInterfaceSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSourcePort.setStatus("mandatory")


class _IpxInterfaceSourceDLCI_Type(Integer32):
    """Custom type ipxInterfaceSourceDLCI based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_IpxInterfaceSourceDLCI_Type.__name__ = "Integer32"
_IpxInterfaceSourceDLCI_Object = MibTableColumn
ipxInterfaceSourceDLCI = _IpxInterfaceSourceDLCI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 33),
    _IpxInterfaceSourceDLCI_Type()
)
ipxInterfaceSourceDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceSourceDLCI.setStatus("mandatory")
_IpxInterfaceRowStatus_Type = RowStatus
_IpxInterfaceRowStatus_Object = MibTableColumn
ipxInterfaceRowStatus = _IpxInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 2, 6, 1, 34),
    _IpxInterfaceRowStatus_Type()
)
ipxInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceRowStatus.setStatus("mandatory")
_IpxConfigNodeDefault_ObjectIdentity = ObjectIdentity
ipxConfigNodeDefault = _IpxConfigNodeDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 3)
)
_IpxNodeDefaultConfigNetworkAddress_Type = Integer32
_IpxNodeDefaultConfigNetworkAddress_Object = MibScalar
ipxNodeDefaultConfigNetworkAddress = _IpxNodeDefaultConfigNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 3, 1),
    _IpxNodeDefaultConfigNetworkAddress_Type()
)
ipxNodeDefaultConfigNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNodeDefaultConfigNetworkAddress.setStatus("mandatory")


class _IpxNodeDefaultConfigRIPSAPGap_Type(Integer32):
    """Custom type ipxNodeDefaultConfigRIPSAPGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpxNodeDefaultConfigRIPSAPGap_Type.__name__ = "Integer32"
_IpxNodeDefaultConfigRIPSAPGap_Object = MibScalar
ipxNodeDefaultConfigRIPSAPGap = _IpxNodeDefaultConfigRIPSAPGap_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 3, 2),
    _IpxNodeDefaultConfigRIPSAPGap_Type()
)
ipxNodeDefaultConfigRIPSAPGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNodeDefaultConfigRIPSAPGap.setStatus("mandatory")


class _IpxNodeDefaultConfigRouterName_Type(OctetString):
    """Custom type ipxNodeDefaultConfigRouterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxNodeDefaultConfigRouterName_Type.__name__ = "OctetString"
_IpxNodeDefaultConfigRouterName_Object = MibScalar
ipxNodeDefaultConfigRouterName = _IpxNodeDefaultConfigRouterName_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 3, 3, 3),
    _IpxNodeDefaultConfigRouterName_Type()
)
ipxNodeDefaultConfigRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNodeDefaultConfigRouterName.setStatus("mandatory")
_NlIfIpInterfaces_ObjectIdentity = ObjectIdentity
nlIfIpInterfaces = _NlIfIpInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4)
)
_NlIfIpTable_Object = MibTable
nlIfIpTable = _NlIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1)
)
if mibBuilder.loadTexts:
    nlIfIpTable.setStatus("mandatory")
_NlIfIpEntry_Object = MibTableRow
nlIfIpEntry = _NlIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1)
)
nlIfIpEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfIpInterface"),
)
if mibBuilder.loadTexts:
    nlIfIpEntry.setStatus("mandatory")


class _NlIfIpInterface_Type(Integer32):
    """Custom type nlIfIpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 257),
    )


_NlIfIpInterface_Type.__name__ = "Integer32"
_NlIfIpInterface_Object = MibTableColumn
nlIfIpInterface = _NlIfIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 1),
    _NlIfIpInterface_Type()
)
nlIfIpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfIpInterface.setStatus("mandatory")


class _NlIfIpMtu_Type(Integer32):
    """Custom type nlIfIpMtu based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NlIfIpMtu_Type.__name__ = "Integer32"
_NlIfIpMtu_Object = MibTableColumn
nlIfIpMtu = _NlIfIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 2),
    _NlIfIpMtu_Type()
)
nlIfIpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpMtu.setStatus("mandatory")


class _NlIfIpNetworkMask_Type(IpAddress):
    """Custom type nlIfIpNetworkMask based on IpAddress"""
    defaultHexValue = "FF000000"


_NlIfIpNetworkMask_Object = MibTableColumn
nlIfIpNetworkMask = _NlIfIpNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 3),
    _NlIfIpNetworkMask_Type()
)
nlIfIpNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpNetworkMask.setStatus("mandatory")


class _NlIfIpRouteMetric_Type(Integer32):
    """Custom type nlIfIpRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlIfIpRouteMetric_Type.__name__ = "Integer32"
_NlIfIpRouteMetric_Object = MibTableColumn
nlIfIpRouteMetric = _NlIfIpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 4),
    _NlIfIpRouteMetric_Type()
)
nlIfIpRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpRouteMetric.setStatus("mandatory")


class _NlIfIpICMPAddRoutes_Type(Integer32):
    """Custom type nlIfIpICMPAddRoutes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfIpICMPAddRoutes_Type.__name__ = "Integer32"
_NlIfIpICMPAddRoutes_Object = MibTableColumn
nlIfIpICMPAddRoutes = _NlIfIpICMPAddRoutes_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 5),
    _NlIfIpICMPAddRoutes_Type()
)
nlIfIpICMPAddRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpICMPAddRoutes.setStatus("mandatory")


class _NlIfIpRIPDeltaUpdates_Type(Integer32):
    """Custom type nlIfIpRIPDeltaUpdates based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_NlIfIpRIPDeltaUpdates_Type.__name__ = "Integer32"
_NlIfIpRIPDeltaUpdates_Object = MibTableColumn
nlIfIpRIPDeltaUpdates = _NlIfIpRIPDeltaUpdates_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 6),
    _NlIfIpRIPDeltaUpdates_Type()
)
nlIfIpRIPDeltaUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpRIPDeltaUpdates.setStatus("mandatory")


class _NlIfIpRIPFullUpdates_Type(Integer32):
    """Custom type nlIfIpRIPFullUpdates based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_NlIfIpRIPFullUpdates_Type.__name__ = "Integer32"
_NlIfIpRIPFullUpdates_Object = MibTableColumn
nlIfIpRIPFullUpdates = _NlIfIpRIPFullUpdates_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 7),
    _NlIfIpRIPFullUpdates_Type()
)
nlIfIpRIPFullUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpRIPFullUpdates.setStatus("mandatory")


class _NlIfIpPriority_Type(Integer32):
    """Custom type nlIfIpPriority based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NlIfIpPriority_Type.__name__ = "Integer32"
_NlIfIpPriority_Object = MibTableColumn
nlIfIpPriority = _NlIfIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 8),
    _NlIfIpPriority_Type()
)
nlIfIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpPriority.setStatus("mandatory")


class _NlIfIpBAG_Type(Integer32):
    """Custom type nlIfIpBAG based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NlIfIpBAG_Type.__name__ = "Integer32"
_NlIfIpBAG_Object = MibTableColumn
nlIfIpBAG = _NlIfIpBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 9),
    _NlIfIpBAG_Type()
)
nlIfIpBAG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpBAG.setStatus("mandatory")


class _NlIfIpType_Type(Integer32):
    """Custom type nlIfIpType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              9,
              32,
              53)
        )
    )
    namedValues = NamedValues(
        *(("ethernetCsmacd", 6),
          ("frameRelay", 32),
          ("iso88023Csmacd", 7),
          ("iso88025TokenRing", 9),
          ("other", 1),
          ("propVirtual", 53),
          ("rfc877x25", 5))
    )


_NlIfIpType_Type.__name__ = "Integer32"
_NlIfIpType_Object = MibTableColumn
nlIfIpType = _NlIfIpType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 10),
    _NlIfIpType_Type()
)
nlIfIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpType.setStatus("mandatory")


class _NlIfIpSourceAddress_Type(IpAddress):
    """Custom type nlIfIpSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpSourceAddress_Object = MibTableColumn
nlIfIpSourceAddress = _NlIfIpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 11),
    _NlIfIpSourceAddress_Type()
)
nlIfIpSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSourceAddress.setStatus("mandatory")


class _NlIfIpDestAddress_Type(IpAddress):
    """Custom type nlIfIpDestAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpDestAddress_Object = MibTableColumn
nlIfIpDestAddress = _NlIfIpDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 12),
    _NlIfIpDestAddress_Type()
)
nlIfIpDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpDestAddress.setStatus("mandatory")


class _NlIfIpBroadcastAddress_Type(IpAddress):
    """Custom type nlIfIpBroadcastAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpBroadcastAddress_Object = MibTableColumn
nlIfIpBroadcastAddress = _NlIfIpBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 13),
    _NlIfIpBroadcastAddress_Type()
)
nlIfIpBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpBroadcastAddress.setStatus("mandatory")


class _NlIfIpLANCard_Type(Integer32):
    """Custom type nlIfIpLANCard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NlIfIpLANCard_Type.__name__ = "Integer32"
_NlIfIpLANCard_Object = MibTableColumn
nlIfIpLANCard = _NlIfIpLANCard_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 14),
    _NlIfIpLANCard_Type()
)
nlIfIpLANCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpLANCard.setStatus("mandatory")
_NlIfIpSourceSub_Type = NlSubscriberAddress
_NlIfIpSourceSub_Object = MibTableColumn
nlIfIpSourceSub = _NlIfIpSourceSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 15),
    _NlIfIpSourceSub_Type()
)
nlIfIpSourceSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSourceSub.setStatus("mandatory")
_NlIfIpDestSub_Type = NlSubscriberAddress
_NlIfIpDestSub_Object = MibTableColumn
nlIfIpDestSub = _NlIfIpDestSub_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 16),
    _NlIfIpDestSub_Type()
)
nlIfIpDestSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpDestSub.setStatus("mandatory")


class _NlIfIpSVCRetryTimer_Type(Integer32):
    """Custom type nlIfIpSVCRetryTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_NlIfIpSVCRetryTimer_Type.__name__ = "Integer32"
_NlIfIpSVCRetryTimer_Object = MibTableColumn
nlIfIpSVCRetryTimer = _NlIfIpSVCRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 17),
    _NlIfIpSVCRetryTimer_Type()
)
nlIfIpSVCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSVCRetryTimer.setStatus("mandatory")


class _NlIfIpSVCIdleTimer_Type(Integer32):
    """Custom type nlIfIpSVCIdleTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_NlIfIpSVCIdleTimer_Type.__name__ = "Integer32"
_NlIfIpSVCIdleTimer_Object = MibTableColumn
nlIfIpSVCIdleTimer = _NlIfIpSVCIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 18),
    _NlIfIpSVCIdleTimer_Type()
)
nlIfIpSVCIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSVCIdleTimer.setStatus("mandatory")


class _NlIfIpMaxSVC_Type(Integer32):
    """Custom type nlIfIpMaxSVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfIpMaxSVC_Type.__name__ = "Integer32"
_NlIfIpMaxSVC_Object = MibTableColumn
nlIfIpMaxSVC = _NlIfIpMaxSVC_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 19),
    _NlIfIpMaxSVC_Type()
)
nlIfIpMaxSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpMaxSVC.setStatus("mandatory")


class _NlIfIpPVCConnection_Type(Integer32):
    """Custom type nlIfIpPVCConnection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfIpPVCConnection_Type.__name__ = "Integer32"
_NlIfIpPVCConnection_Object = MibTableColumn
nlIfIpPVCConnection = _NlIfIpPVCConnection_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 20),
    _NlIfIpPVCConnection_Type()
)
nlIfIpPVCConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpPVCConnection.setStatus("mandatory")


class _NlIfIpSourceRlp_Type(Integer32):
    """Custom type nlIfIpSourceRlp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfIpSourceRlp_Type.__name__ = "Integer32"
_NlIfIpSourceRlp_Object = MibTableColumn
nlIfIpSourceRlp = _NlIfIpSourceRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 21),
    _NlIfIpSourceRlp_Type()
)
nlIfIpSourceRlp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSourceRlp.setStatus("mandatory")


class _NlIfIpSourcePort_Type(Integer32):
    """Custom type nlIfIpSourcePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfIpSourcePort_Type.__name__ = "Integer32"
_NlIfIpSourcePort_Object = MibTableColumn
nlIfIpSourcePort = _NlIfIpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 22),
    _NlIfIpSourcePort_Type()
)
nlIfIpSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSourcePort.setStatus("mandatory")


class _NlIfIpSourceDLCI_Type(Integer32):
    """Custom type nlIfIpSourceDLCI based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NlIfIpSourceDLCI_Type.__name__ = "Integer32"
_NlIfIpSourceDLCI_Object = MibTableColumn
nlIfIpSourceDLCI = _NlIfIpSourceDLCI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 23),
    _NlIfIpSourceDLCI_Type()
)
nlIfIpSourceDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSourceDLCI.setStatus("mandatory")


class _NlIfIpRIPSupport_Type(Integer32):
    """Custom type nlIfIpRIPSupport based on Integer32"""
    defaultValue = 2

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
          ("enabled", 2),
          ("receive-only", 3))
    )


_NlIfIpRIPSupport_Type.__name__ = "Integer32"
_NlIfIpRIPSupport_Object = MibTableColumn
nlIfIpRIPSupport = _NlIfIpRIPSupport_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 24),
    _NlIfIpRIPSupport_Type()
)
nlIfIpRIPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpRIPSupport.setStatus("mandatory")


class _NlIfIpInverseARP_Type(Integer32):
    """Custom type nlIfIpInverseARP based on Integer32"""
    defaultValue = 1

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


_NlIfIpInverseARP_Type.__name__ = "Integer32"
_NlIfIpInverseARP_Object = MibTableColumn
nlIfIpInverseARP = _NlIfIpInverseARP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 25),
    _NlIfIpInverseARP_Type()
)
nlIfIpInverseARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpInverseARP.setStatus("mandatory")


class _NlIfIpProxyARP_Type(Integer32):
    """Custom type nlIfIpProxyARP based on Integer32"""
    defaultValue = 1

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


_NlIfIpProxyARP_Type.__name__ = "Integer32"
_NlIfIpProxyARP_Object = MibTableColumn
nlIfIpProxyARP = _NlIfIpProxyARP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 26),
    _NlIfIpProxyARP_Type()
)
nlIfIpProxyARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpProxyARP.setStatus("mandatory")


class _NlIfIpUnnumberedIf_Type(Integer32):
    """Custom type nlIfIpUnnumberedIf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfIpUnnumberedIf_Type.__name__ = "Integer32"
_NlIfIpUnnumberedIf_Object = MibTableColumn
nlIfIpUnnumberedIf = _NlIfIpUnnumberedIf_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 27),
    _NlIfIpUnnumberedIf_Type()
)
nlIfIpUnnumberedIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpUnnumberedIf.setStatus("mandatory")
_NlIfIpRowStatus_Type = RowStatus
_NlIfIpRowStatus_Object = MibTableColumn
nlIfIpRowStatus = _NlIfIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 1, 1, 28),
    _NlIfIpRowStatus_Type()
)
nlIfIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpRowStatus.setStatus("mandatory")
_NlIfIpSecondaryAddrTable_Object = MibTable
nlIfIpSecondaryAddrTable = _NlIfIpSecondaryAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2)
)
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrTable.setStatus("mandatory")
_NlIfIpSecondaryAddrEntry_Object = MibTableRow
nlIfIpSecondaryAddrEntry = _NlIfIpSecondaryAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1)
)
nlIfIpSecondaryAddrEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfIpInterface"),
    (0, "NETLINK-SPECIFIC-MIB", "nlIfIpSecondaryAddrSequence"),
)
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrEntry.setStatus("mandatory")


class _NlIfIpSecondaryAddrSequence_Type(Integer32):
    """Custom type nlIfIpSecondaryAddrSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NlIfIpSecondaryAddrSequence_Type.__name__ = "Integer32"
_NlIfIpSecondaryAddrSequence_Object = MibTableColumn
nlIfIpSecondaryAddrSequence = _NlIfIpSecondaryAddrSequence_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 1),
    _NlIfIpSecondaryAddrSequence_Type()
)
nlIfIpSecondaryAddrSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrSequence.setStatus("mandatory")


class _NlIfIpSecondaryAddrNetworkMask_Type(IpAddress):
    """Custom type nlIfIpSecondaryAddrNetworkMask based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpSecondaryAddrNetworkMask_Object = MibTableColumn
nlIfIpSecondaryAddrNetworkMask = _NlIfIpSecondaryAddrNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 2),
    _NlIfIpSecondaryAddrNetworkMask_Type()
)
nlIfIpSecondaryAddrNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrNetworkMask.setStatus("mandatory")


class _NlIfIpSecondaryAddrRouteMetric_Type(Integer32):
    """Custom type nlIfIpSecondaryAddrRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlIfIpSecondaryAddrRouteMetric_Type.__name__ = "Integer32"
_NlIfIpSecondaryAddrRouteMetric_Object = MibTableColumn
nlIfIpSecondaryAddrRouteMetric = _NlIfIpSecondaryAddrRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 3),
    _NlIfIpSecondaryAddrRouteMetric_Type()
)
nlIfIpSecondaryAddrRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrRouteMetric.setStatus("mandatory")


class _NlIfIpSecondaryAddrSourceAddress_Type(IpAddress):
    """Custom type nlIfIpSecondaryAddrSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpSecondaryAddrSourceAddress_Object = MibTableColumn
nlIfIpSecondaryAddrSourceAddress = _NlIfIpSecondaryAddrSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 4),
    _NlIfIpSecondaryAddrSourceAddress_Type()
)
nlIfIpSecondaryAddrSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrSourceAddress.setStatus("mandatory")


class _NlIfIpSecondaryAddrBroadcastAddress_Type(IpAddress):
    """Custom type nlIfIpSecondaryAddrBroadcastAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NlIfIpSecondaryAddrBroadcastAddress_Object = MibTableColumn
nlIfIpSecondaryAddrBroadcastAddress = _NlIfIpSecondaryAddrBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 5),
    _NlIfIpSecondaryAddrBroadcastAddress_Type()
)
nlIfIpSecondaryAddrBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrBroadcastAddress.setStatus("mandatory")


class _NlIfIpSecondaryAddrRIPSupport_Type(Integer32):
    """Custom type nlIfIpSecondaryAddrRIPSupport based on Integer32"""
    defaultValue = 2

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
          ("enabled", 2),
          ("receive-only", 3))
    )


_NlIfIpSecondaryAddrRIPSupport_Type.__name__ = "Integer32"
_NlIfIpSecondaryAddrRIPSupport_Object = MibTableColumn
nlIfIpSecondaryAddrRIPSupport = _NlIfIpSecondaryAddrRIPSupport_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 6),
    _NlIfIpSecondaryAddrRIPSupport_Type()
)
nlIfIpSecondaryAddrRIPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrRIPSupport.setStatus("mandatory")
_NlIfIpSecondaryAddrRowStatus_Type = RowStatus
_NlIfIpSecondaryAddrRowStatus_Object = MibTableColumn
nlIfIpSecondaryAddrRowStatus = _NlIfIpSecondaryAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 4, 2, 1, 7),
    _NlIfIpSecondaryAddrRowStatus_Type()
)
nlIfIpSecondaryAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfIpSecondaryAddrRowStatus.setStatus("mandatory")
_NlIfVoiceInterfaces_ObjectIdentity = ObjectIdentity
nlIfVoiceInterfaces = _NlIfVoiceInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5)
)
_NlIfVoiceTable_Object = MibTable
nlIfVoiceTable = _NlIfVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1)
)
if mibBuilder.loadTexts:
    nlIfVoiceTable.setStatus("mandatory")
_NlIfVoiceEntry_Object = MibTableRow
nlIfVoiceEntry = _NlIfVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1)
)
nlIfVoiceEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlIfVoiceInterface"),
)
if mibBuilder.loadTexts:
    nlIfVoiceEntry.setStatus("mandatory")


class _NlIfVoiceInterface_Type(Integer32):
    """Custom type nlIfVoiceInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 129),
    )


_NlIfVoiceInterface_Type.__name__ = "Integer32"
_NlIfVoiceInterface_Object = MibTableColumn
nlIfVoiceInterface = _NlIfVoiceInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 1),
    _NlIfVoiceInterface_Type()
)
nlIfVoiceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlIfVoiceInterface.setStatus("mandatory")


class _NlIfVoicePeerNodeType_Type(Integer32):
    """Custom type nlIfVoicePeerNodeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("act", 2),
          ("netlink", 1))
    )


_NlIfVoicePeerNodeType_Type.__name__ = "Integer32"
_NlIfVoicePeerNodeType_Object = MibTableColumn
nlIfVoicePeerNodeType = _NlIfVoicePeerNodeType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 2),
    _NlIfVoicePeerNodeType_Type()
)
nlIfVoicePeerNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoicePeerNodeType.setStatus("mandatory")


class _NlIfVoicePeerNodeNumber_Type(Integer32):
    """Custom type nlIfVoicePeerNodeNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 61),
    )


_NlIfVoicePeerNodeNumber_Type.__name__ = "Integer32"
_NlIfVoicePeerNodeNumber_Object = MibTableColumn
nlIfVoicePeerNodeNumber = _NlIfVoicePeerNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 3),
    _NlIfVoicePeerNodeNumber_Type()
)
nlIfVoicePeerNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoicePeerNodeNumber.setStatus("mandatory")


class _NlIfVoicePeerNodePort_Type(Integer32):
    """Custom type nlIfVoicePeerNodePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_NlIfVoicePeerNodePort_Type.__name__ = "Integer32"
_NlIfVoicePeerNodePort_Object = MibTableColumn
nlIfVoicePeerNodePort = _NlIfVoicePeerNodePort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 4),
    _NlIfVoicePeerNodePort_Type()
)
nlIfVoicePeerNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoicePeerNodePort.setStatus("mandatory")


class _NlIfVoiceLocalNodeNumber_Type(Integer32):
    """Custom type nlIfVoiceLocalNodeNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 61),
    )


_NlIfVoiceLocalNodeNumber_Type.__name__ = "Integer32"
_NlIfVoiceLocalNodeNumber_Object = MibTableColumn
nlIfVoiceLocalNodeNumber = _NlIfVoiceLocalNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 5),
    _NlIfVoiceLocalNodeNumber_Type()
)
nlIfVoiceLocalNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceLocalNodeNumber.setStatus("mandatory")


class _NlIfVoiceLocalNodePort_Type(Integer32):
    """Custom type nlIfVoiceLocalNodePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_NlIfVoiceLocalNodePort_Type.__name__ = "Integer32"
_NlIfVoiceLocalNodePort_Object = MibTableColumn
nlIfVoiceLocalNodePort = _NlIfVoiceLocalNodePort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 6),
    _NlIfVoiceLocalNodePort_Type()
)
nlIfVoiceLocalNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceLocalNodePort.setStatus("mandatory")


class _NlIfVoiceFrameRelayRlp_Type(Integer32):
    """Custom type nlIfVoiceFrameRelayRlp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfVoiceFrameRelayRlp_Type.__name__ = "Integer32"
_NlIfVoiceFrameRelayRlp_Object = MibTableColumn
nlIfVoiceFrameRelayRlp = _NlIfVoiceFrameRelayRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 7),
    _NlIfVoiceFrameRelayRlp_Type()
)
nlIfVoiceFrameRelayRlp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceFrameRelayRlp.setStatus("mandatory")


class _NlIfVoiceFrameRelayPort_Type(Integer32):
    """Custom type nlIfVoiceFrameRelayPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlIfVoiceFrameRelayPort_Type.__name__ = "Integer32"
_NlIfVoiceFrameRelayPort_Object = MibTableColumn
nlIfVoiceFrameRelayPort = _NlIfVoiceFrameRelayPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 8),
    _NlIfVoiceFrameRelayPort_Type()
)
nlIfVoiceFrameRelayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceFrameRelayPort.setStatus("mandatory")


class _NlIfVoiceFrameRelayDLCI_Type(Integer32):
    """Custom type nlIfVoiceFrameRelayDLCI based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NlIfVoiceFrameRelayDLCI_Type.__name__ = "Integer32"
_NlIfVoiceFrameRelayDLCI_Object = MibTableColumn
nlIfVoiceFrameRelayDLCI = _NlIfVoiceFrameRelayDLCI_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 9),
    _NlIfVoiceFrameRelayDLCI_Type()
)
nlIfVoiceFrameRelayDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceFrameRelayDLCI.setStatus("mandatory")


class _NlIfVoiceEnableFragment_Type(Integer32):
    """Custom type nlIfVoiceEnableFragment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlIfVoiceEnableFragment_Type.__name__ = "Integer32"
_NlIfVoiceEnableFragment_Object = MibTableColumn
nlIfVoiceEnableFragment = _NlIfVoiceEnableFragment_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 10),
    _NlIfVoiceEnableFragment_Type()
)
nlIfVoiceEnableFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceEnableFragment.setStatus("mandatory")
_NlIfVoiceRowStatus_Type = RowStatus
_NlIfVoiceRowStatus_Object = MibTableColumn
nlIfVoiceRowStatus = _NlIfVoiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 4, 5, 1, 1, 11),
    _NlIfVoiceRowStatus_Type()
)
nlIfVoiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIfVoiceRowStatus.setStatus("mandatory")
_Subscriber_ObjectIdentity = ObjectIdentity
subscriber = _Subscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 5)
)
_NlLocalSubscriberTable_Object = MibTable
nlLocalSubscriberTable = _NlLocalSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1)
)
if mibBuilder.loadTexts:
    nlLocalSubscriberTable.setStatus("mandatory")
_NlLocalSubscriberEntry_Object = MibTableRow
nlLocalSubscriberEntry = _NlLocalSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1)
)
nlLocalSubscriberEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLocalSubscriberId"),
)
if mibBuilder.loadTexts:
    nlLocalSubscriberEntry.setStatus("mandatory")
_NlLocalSubscriberId_Type = NlSubscriberAddress
_NlLocalSubscriberId_Object = MibTableColumn
nlLocalSubscriberId = _NlLocalSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 1),
    _NlLocalSubscriberId_Type()
)
nlLocalSubscriberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLocalSubscriberId.setStatus("mandatory")


class _NlLocalSubscriberName_Type(DisplayString):
    """Custom type nlLocalSubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NlLocalSubscriberName_Type.__name__ = "DisplayString"
_NlLocalSubscriberName_Object = MibTableColumn
nlLocalSubscriberName = _NlLocalSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 2),
    _NlLocalSubscriberName_Type()
)
nlLocalSubscriberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLocalSubscriberName.setStatus("mandatory")


class _NlLocalSubscriberAlgorithm_Type(Integer32):
    """Custom type nlLocalSubscriberAlgorithm based on Integer32"""
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
        *(("least-lcn", 4),
          ("line-busy", 3),
          ("line-failed", 2),
          ("round-robin", 1))
    )


_NlLocalSubscriberAlgorithm_Type.__name__ = "Integer32"
_NlLocalSubscriberAlgorithm_Object = MibTableColumn
nlLocalSubscriberAlgorithm = _NlLocalSubscriberAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 3),
    _NlLocalSubscriberAlgorithm_Type()
)
nlLocalSubscriberAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberAlgorithm.setStatus("mandatory")


class _NlLocalSubscriberSystematicRedirect_Type(Integer32):
    """Custom type nlLocalSubscriberSystematicRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlLocalSubscriberSystematicRedirect_Type.__name__ = "Integer32"
_NlLocalSubscriberSystematicRedirect_Object = MibTableColumn
nlLocalSubscriberSystematicRedirect = _NlLocalSubscriberSystematicRedirect_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 4),
    _NlLocalSubscriberSystematicRedirect_Type()
)
nlLocalSubscriberSystematicRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberSystematicRedirect.setStatus("mandatory")


class _NlLocalSubscriberRedirectBusy_Type(Integer32):
    """Custom type nlLocalSubscriberRedirectBusy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlLocalSubscriberRedirectBusy_Type.__name__ = "Integer32"
_NlLocalSubscriberRedirectBusy_Object = MibTableColumn
nlLocalSubscriberRedirectBusy = _NlLocalSubscriberRedirectBusy_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 5),
    _NlLocalSubscriberRedirectBusy_Type()
)
nlLocalSubscriberRedirectBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirectBusy.setStatus("mandatory")


class _NlLocalSubscriberRedirectOO_Type(Integer32):
    """Custom type nlLocalSubscriberRedirectOO based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlLocalSubscriberRedirectOO_Type.__name__ = "Integer32"
_NlLocalSubscriberRedirectOO_Object = MibTableColumn
nlLocalSubscriberRedirectOO = _NlLocalSubscriberRedirectOO_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 6),
    _NlLocalSubscriberRedirectOO_Type()
)
nlLocalSubscriberRedirectOO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirectOO.setStatus("mandatory")


class _NlLocalSubscriberPriority_Type(Integer32):
    """Custom type nlLocalSubscriberPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NlLocalSubscriberPriority_Type.__name__ = "Integer32"
_NlLocalSubscriberPriority_Object = MibTableColumn
nlLocalSubscriberPriority = _NlLocalSubscriberPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 7),
    _NlLocalSubscriberPriority_Type()
)
nlLocalSubscriberPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberPriority.setStatus("mandatory")
_NlLocalSubscriberRowStatus_Type = RowStatus
_NlLocalSubscriberRowStatus_Object = MibTableColumn
nlLocalSubscriberRowStatus = _NlLocalSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 1, 1, 8),
    _NlLocalSubscriberRowStatus_Type()
)
nlLocalSubscriberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRowStatus.setStatus("mandatory")
_NlLocalSubscriberRouteTable_Object = MibTable
nlLocalSubscriberRouteTable = _NlLocalSubscriberRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2)
)
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteTable.setStatus("mandatory")
_NlLocalSubscriberRouteEntry_Object = MibTableRow
nlLocalSubscriberRouteEntry = _NlLocalSubscriberRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1)
)
nlLocalSubscriberRouteEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLocalSubscriberId"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLocalSubscriberRouteIndex"),
)
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteEntry.setStatus("mandatory")


class _NlLocalSubscriberRouteIndex_Type(Integer32):
    """Custom type nlLocalSubscriberRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NlLocalSubscriberRouteIndex_Type.__name__ = "Integer32"
_NlLocalSubscriberRouteIndex_Object = MibTableColumn
nlLocalSubscriberRouteIndex = _NlLocalSubscriberRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1, 1),
    _NlLocalSubscriberRouteIndex_Type()
)
nlLocalSubscriberRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteIndex.setStatus("mandatory")


class _NlLocalSubscriberRouteConf_Type(Integer32):
    """Custom type nlLocalSubscriberRouteConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlLocalSubscriberRouteConf_Type.__name__ = "Integer32"
_NlLocalSubscriberRouteConf_Object = MibTableColumn
nlLocalSubscriberRouteConf = _NlLocalSubscriberRouteConf_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1, 2),
    _NlLocalSubscriberRouteConf_Type()
)
nlLocalSubscriberRouteConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteConf.setStatus("mandatory")
_NlLocalSubscriberRouteLP_Type = Integer32
_NlLocalSubscriberRouteLP_Object = MibTableColumn
nlLocalSubscriberRouteLP = _NlLocalSubscriberRouteLP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1, 3),
    _NlLocalSubscriberRouteLP_Type()
)
nlLocalSubscriberRouteLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteLP.setStatus("mandatory")
_NlLocalSubscriberRoutePort_Type = Integer32
_NlLocalSubscriberRoutePort_Object = MibTableColumn
nlLocalSubscriberRoutePort = _NlLocalSubscriberRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1, 4),
    _NlLocalSubscriberRoutePort_Type()
)
nlLocalSubscriberRoutePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRoutePort.setStatus("mandatory")
_NlLocalSubscriberRouteRowStatus_Type = RowStatus
_NlLocalSubscriberRouteRowStatus_Object = MibTableColumn
nlLocalSubscriberRouteRowStatus = _NlLocalSubscriberRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 2, 1, 5),
    _NlLocalSubscriberRouteRowStatus_Type()
)
nlLocalSubscriberRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRouteRowStatus.setStatus("mandatory")
_NlLocalSubscriberRedirTable_Object = MibTable
nlLocalSubscriberRedirTable = _NlLocalSubscriberRedirTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 3)
)
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirTable.setStatus("mandatory")
_NlLocalSubscriberRedirEntry_Object = MibTableRow
nlLocalSubscriberRedirEntry = _NlLocalSubscriberRedirEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 3, 1)
)
nlLocalSubscriberRedirEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLocalSubscriberId"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLocalSubscriberRedirIndex"),
)
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirEntry.setStatus("mandatory")


class _NlLocalSubscriberRedirIndex_Type(Integer32):
    """Custom type nlLocalSubscriberRedirIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NlLocalSubscriberRedirIndex_Type.__name__ = "Integer32"
_NlLocalSubscriberRedirIndex_Object = MibTableColumn
nlLocalSubscriberRedirIndex = _NlLocalSubscriberRedirIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 3, 1, 1),
    _NlLocalSubscriberRedirIndex_Type()
)
nlLocalSubscriberRedirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirIndex.setStatus("mandatory")
_NlLocalSubscriberRedirAddr_Type = NlSubscriberAddress
_NlLocalSubscriberRedirAddr_Object = MibTableColumn
nlLocalSubscriberRedirAddr = _NlLocalSubscriberRedirAddr_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 3, 1, 2),
    _NlLocalSubscriberRedirAddr_Type()
)
nlLocalSubscriberRedirAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirAddr.setStatus("mandatory")
_NlLocalSubscriberRedirRowStatus_Type = RowStatus
_NlLocalSubscriberRedirRowStatus_Object = MibTableColumn
nlLocalSubscriberRedirRowStatus = _NlLocalSubscriberRedirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 5, 3, 1, 3),
    _NlLocalSubscriberRedirRowStatus_Type()
)
nlLocalSubscriberRedirRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLocalSubscriberRedirRowStatus.setStatus("mandatory")
_Llc2_ObjectIdentity = ObjectIdentity
llc2 = _Llc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 6)
)
_NlLlc2HostTable_Object = MibTable
nlLlc2HostTable = _NlLlc2HostTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1)
)
if mibBuilder.loadTexts:
    nlLlc2HostTable.setStatus("mandatory")
_NlLlc2HostEntry_Object = MibTableRow
nlLlc2HostEntry = _NlLlc2HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1)
)
nlLlc2HostEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostGroup"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostIndex"),
)
if mibBuilder.loadTexts:
    nlLlc2HostEntry.setStatus("mandatory")


class _NlLlc2HostIndex_Type(Integer32):
    """Custom type nlLlc2HostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 251),
    )


_NlLlc2HostIndex_Type.__name__ = "Integer32"
_NlLlc2HostIndex_Object = MibTableColumn
nlLlc2HostIndex = _NlLlc2HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 1),
    _NlLlc2HostIndex_Type()
)
nlLlc2HostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2HostIndex.setStatus("mandatory")


class _NlLlc2HostMACAddress_Type(MacAddress):
    """Custom type nlLlc2HostMACAddress based on MacAddress"""
    defaultHexValue = "400000000001"


_NlLlc2HostMACAddress_Object = MibTableColumn
nlLlc2HostMACAddress = _NlLlc2HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 2),
    _NlLlc2HostMACAddress_Type()
)
nlLlc2HostMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostMACAddress.setStatus("mandatory")


class _NlLlc2HostSessionType_Type(Integer32):
    """Custom type nlLlc2HostSessionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("originated", 1),
          ("terminated", 2))
    )


_NlLlc2HostSessionType_Type.__name__ = "Integer32"
_NlLlc2HostSessionType_Object = MibTableColumn
nlLlc2HostSessionType = _NlLlc2HostSessionType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 3),
    _NlLlc2HostSessionType_Type()
)
nlLlc2HostSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostSessionType.setStatus("mandatory")


class _NlLlc2HostT1ReplyTimer_Type(TimeInterval):
    """Custom type nlLlc2HostT1ReplyTimer based on TimeInterval"""
    defaultValue = 10

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_NlLlc2HostT1ReplyTimer_Type.__name__ = "TimeInterval"
_NlLlc2HostT1ReplyTimer_Object = MibTableColumn
nlLlc2HostT1ReplyTimer = _NlLlc2HostT1ReplyTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 4),
    _NlLlc2HostT1ReplyTimer_Type()
)
nlLlc2HostT1ReplyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostT1ReplyTimer.setStatus("mandatory")


class _NlLlc2HostT2RecvAckTimer_Type(TimeInterval):
    """Custom type nlLlc2HostT2RecvAckTimer based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_NlLlc2HostT2RecvAckTimer_Type.__name__ = "TimeInterval"
_NlLlc2HostT2RecvAckTimer_Object = MibTableColumn
nlLlc2HostT2RecvAckTimer = _NlLlc2HostT2RecvAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 5),
    _NlLlc2HostT2RecvAckTimer_Type()
)
nlLlc2HostT2RecvAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostT2RecvAckTimer.setStatus("mandatory")


class _NlLlc2HostTiInactivityTimer_Type(TimeInterval):
    """Custom type nlLlc2HostTiInactivityTimer based on TimeInterval"""
    defaultValue = 30

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_NlLlc2HostTiInactivityTimer_Type.__name__ = "TimeInterval"
_NlLlc2HostTiInactivityTimer_Object = MibTableColumn
nlLlc2HostTiInactivityTimer = _NlLlc2HostTiInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 6),
    _NlLlc2HostTiInactivityTimer_Type()
)
nlLlc2HostTiInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostTiInactivityTimer.setStatus("mandatory")


class _NlLlc2HostN3NumberLPDUs_Type(Integer32):
    """Custom type nlLlc2HostN3NumberLPDUs based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_NlLlc2HostN3NumberLPDUs_Type.__name__ = "Integer32"
_NlLlc2HostN3NumberLPDUs_Object = MibTableColumn
nlLlc2HostN3NumberLPDUs = _NlLlc2HostN3NumberLPDUs_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 7),
    _NlLlc2HostN3NumberLPDUs_Type()
)
nlLlc2HostN3NumberLPDUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostN3NumberLPDUs.setStatus("mandatory")


class _NlLlc2HostTwNumberOutstanding_Type(Integer32):
    """Custom type nlLlc2HostTwNumberOutstanding based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_NlLlc2HostTwNumberOutstanding_Type.__name__ = "Integer32"
_NlLlc2HostTwNumberOutstanding_Object = MibTableColumn
nlLlc2HostTwNumberOutstanding = _NlLlc2HostTwNumberOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 8),
    _NlLlc2HostTwNumberOutstanding_Type()
)
nlLlc2HostTwNumberOutstanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostTwNumberOutstanding.setStatus("mandatory")


class _NlLlc2HostN2ExpiredT1LPDUCount_Type(Integer32):
    """Custom type nlLlc2HostN2ExpiredT1LPDUCount based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlLlc2HostN2ExpiredT1LPDUCount_Type.__name__ = "Integer32"
_NlLlc2HostN2ExpiredT1LPDUCount_Object = MibTableColumn
nlLlc2HostN2ExpiredT1LPDUCount = _NlLlc2HostN2ExpiredT1LPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 9),
    _NlLlc2HostN2ExpiredT1LPDUCount_Type()
)
nlLlc2HostN2ExpiredT1LPDUCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostN2ExpiredT1LPDUCount.setStatus("mandatory")


class _NlLlc2HostPriority_Type(Integer32):
    """Custom type nlLlc2HostPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NlLlc2HostPriority_Type.__name__ = "Integer32"
_NlLlc2HostPriority_Object = MibTableColumn
nlLlc2HostPriority = _NlLlc2HostPriority_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 10),
    _NlLlc2HostPriority_Type()
)
nlLlc2HostPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostPriority.setStatus("mandatory")


class _NlLlc2HostBAG_Type(Integer32):
    """Custom type nlLlc2HostBAG based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NlLlc2HostBAG_Type.__name__ = "Integer32"
_NlLlc2HostBAG_Object = MibTableColumn
nlLlc2HostBAG = _NlLlc2HostBAG_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 11),
    _NlLlc2HostBAG_Type()
)
nlLlc2HostBAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2HostBAG.setStatus("mandatory")
_NlLlc2HostRoutingSubscriberId_Type = NlSubscriberAddress
_NlLlc2HostRoutingSubscriberId_Object = MibTableColumn
nlLlc2HostRoutingSubscriberId = _NlLlc2HostRoutingSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 12),
    _NlLlc2HostRoutingSubscriberId_Type()
)
nlLlc2HostRoutingSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostRoutingSubscriberId.setStatus("mandatory")


class _NlLlc2HostSrcMACAddressMask_Type(MacAddress):
    """Custom type nlLlc2HostSrcMACAddressMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NlLlc2HostSrcMACAddressMask_Object = MibTableColumn
nlLlc2HostSrcMACAddressMask = _NlLlc2HostSrcMACAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 13),
    _NlLlc2HostSrcMACAddressMask_Type()
)
nlLlc2HostSrcMACAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostSrcMACAddressMask.setStatus("mandatory")


class _NlLlc2HostAccess_Type(Integer32):
    """Custom type nlLlc2HostAccess based on Integer32"""
    defaultValue = 6

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
        *(("all", 5),
          ("ethernet", 4),
          ("frameRelay", 2),
          ("lan", 1),
          ("not-applicable", 6),
          ("tokenRing", 3))
    )


_NlLlc2HostAccess_Type.__name__ = "Integer32"
_NlLlc2HostAccess_Object = MibTableColumn
nlLlc2HostAccess = _NlLlc2HostAccess_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 14),
    _NlLlc2HostAccess_Type()
)
nlLlc2HostAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2HostAccess.setStatus("mandatory")
_NlLlc2HostRowStatus_Type = RowStatus
_NlLlc2HostRowStatus_Object = MibTableColumn
nlLlc2HostRowStatus = _NlLlc2HostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 15),
    _NlLlc2HostRowStatus_Type()
)
nlLlc2HostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2HostRowStatus.setStatus("mandatory")


class _NlLlc2HostInterface_Type(Integer32):
    """Custom type nlLlc2HostInterface based on Integer32"""
    defaultValue = 300


_NlLlc2HostInterface_Object = MibTableColumn
nlLlc2HostInterface = _NlLlc2HostInterface_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 16),
    _NlLlc2HostInterface_Type()
)
nlLlc2HostInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2HostInterface.setStatus("mandatory")


class _NlLlc2HostGroup_Type(Integer32):
    """Custom type nlLlc2HostGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NlLlc2HostGroup_Type.__name__ = "Integer32"
_NlLlc2HostGroup_Object = MibTableColumn
nlLlc2HostGroup = _NlLlc2HostGroup_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 1, 1, 17),
    _NlLlc2HostGroup_Type()
)
nlLlc2HostGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2HostGroup.setStatus("mandatory")
_NlLlc2TermConnectionTable_Object = MibTable
nlLlc2TermConnectionTable = _NlLlc2TermConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2)
)
if mibBuilder.loadTexts:
    nlLlc2TermConnectionTable.setStatus("mandatory")
_NlLlc2TermConnectionEntry_Object = MibTableRow
nlLlc2TermConnectionEntry = _NlLlc2TermConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1)
)
nlLlc2TermConnectionEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostGroup"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2TermConnectionSequence"),
)
if mibBuilder.loadTexts:
    nlLlc2TermConnectionEntry.setStatus("mandatory")


class _NlLlc2TermConnectionSequence_Type(Integer32):
    """Custom type nlLlc2TermConnectionSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NlLlc2TermConnectionSequence_Type.__name__ = "Integer32"
_NlLlc2TermConnectionSequence_Object = MibTableColumn
nlLlc2TermConnectionSequence = _NlLlc2TermConnectionSequence_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1, 1),
    _NlLlc2TermConnectionSequence_Type()
)
nlLlc2TermConnectionSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2TermConnectionSequence.setStatus("mandatory")


class _NlLlc2TermConnectionHSAP_Type(Integer32):
    """Custom type nlLlc2TermConnectionHSAP based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 254),
    )


_NlLlc2TermConnectionHSAP_Type.__name__ = "Integer32"
_NlLlc2TermConnectionHSAP_Object = MibTableColumn
nlLlc2TermConnectionHSAP = _NlLlc2TermConnectionHSAP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1, 2),
    _NlLlc2TermConnectionHSAP_Type()
)
nlLlc2TermConnectionHSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2TermConnectionHSAP.setStatus("mandatory")
_NlLlc2TermConnectionLocalSubscriberId_Type = NlSubscriberAddress
_NlLlc2TermConnectionLocalSubscriberId_Object = MibTableColumn
nlLlc2TermConnectionLocalSubscriberId = _NlLlc2TermConnectionLocalSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1, 3),
    _NlLlc2TermConnectionLocalSubscriberId_Type()
)
nlLlc2TermConnectionLocalSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2TermConnectionLocalSubscriberId.setStatus("mandatory")
_NlLlc2TermConnectionRemoteSubscriberId_Type = NlSubscriberAddress
_NlLlc2TermConnectionRemoteSubscriberId_Object = MibTableColumn
nlLlc2TermConnectionRemoteSubscriberId = _NlLlc2TermConnectionRemoteSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1, 4),
    _NlLlc2TermConnectionRemoteSubscriberId_Type()
)
nlLlc2TermConnectionRemoteSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2TermConnectionRemoteSubscriberId.setStatus("mandatory")
_NlLlc2TermConnectionRowStatus_Type = RowStatus
_NlLlc2TermConnectionRowStatus_Object = MibTableColumn
nlLlc2TermConnectionRowStatus = _NlLlc2TermConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 2, 1, 5),
    _NlLlc2TermConnectionRowStatus_Type()
)
nlLlc2TermConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2TermConnectionRowStatus.setStatus("mandatory")
_NlLlc2OrigConnectionTable_Object = MibTable
nlLlc2OrigConnectionTable = _NlLlc2OrigConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3)
)
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionTable.setStatus("mandatory")
_NlLlc2OrigConnectionEntry_Object = MibTableRow
nlLlc2OrigConnectionEntry = _NlLlc2OrigConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1)
)
nlLlc2OrigConnectionEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostGroup"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2HostIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "nlLlc2OrigConnectionSequence"),
)
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionEntry.setStatus("mandatory")


class _NlLlc2OrigConnectionSequence_Type(Integer32):
    """Custom type nlLlc2OrigConnectionSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NlLlc2OrigConnectionSequence_Type.__name__ = "Integer32"
_NlLlc2OrigConnectionSequence_Object = MibTableColumn
nlLlc2OrigConnectionSequence = _NlLlc2OrigConnectionSequence_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 1),
    _NlLlc2OrigConnectionSequence_Type()
)
nlLlc2OrigConnectionSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionSequence.setStatus("mandatory")


class _NlLlc2OrigConnectionHSAP_Type(Integer32):
    """Custom type nlLlc2OrigConnectionHSAP based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 254),
    )


_NlLlc2OrigConnectionHSAP_Type.__name__ = "Integer32"
_NlLlc2OrigConnectionHSAP_Object = MibTableColumn
nlLlc2OrigConnectionHSAP = _NlLlc2OrigConnectionHSAP_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 2),
    _NlLlc2OrigConnectionHSAP_Type()
)
nlLlc2OrigConnectionHSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionHSAP.setStatus("mandatory")


class _NlLlc2OrigConnectionType_Type(Integer32):
    """Custom type nlLlc2OrigConnectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc2", 2),
          ("sdlc", 1))
    )


_NlLlc2OrigConnectionType_Type.__name__ = "Integer32"
_NlLlc2OrigConnectionType_Object = MibTableColumn
nlLlc2OrigConnectionType = _NlLlc2OrigConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 3),
    _NlLlc2OrigConnectionType_Type()
)
nlLlc2OrigConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionType.setStatus("mandatory")
_NlLlc2OrigConnectionLocalSubscriberId_Type = NlSubscriberAddress
_NlLlc2OrigConnectionLocalSubscriberId_Object = MibTableColumn
nlLlc2OrigConnectionLocalSubscriberId = _NlLlc2OrigConnectionLocalSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 4),
    _NlLlc2OrigConnectionLocalSubscriberId_Type()
)
nlLlc2OrigConnectionLocalSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionLocalSubscriberId.setStatus("mandatory")
_NlLlc2OrigConnectionRemoteSubscriberId_Type = NlSubscriberAddress
_NlLlc2OrigConnectionRemoteSubscriberId_Object = MibTableColumn
nlLlc2OrigConnectionRemoteSubscriberId = _NlLlc2OrigConnectionRemoteSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 5),
    _NlLlc2OrigConnectionRemoteSubscriberId_Type()
)
nlLlc2OrigConnectionRemoteSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionRemoteSubscriberId.setStatus("mandatory")


class _NlLlc2OrigConnectionIDBLK_Type(Integer32):
    """Custom type nlLlc2OrigConnectionIDBLK based on Integer32"""
    defaultValue = 0


_NlLlc2OrigConnectionIDBLK_Object = MibTableColumn
nlLlc2OrigConnectionIDBLK = _NlLlc2OrigConnectionIDBLK_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 6),
    _NlLlc2OrigConnectionIDBLK_Type()
)
nlLlc2OrigConnectionIDBLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionIDBLK.setStatus("mandatory")


class _NlLlc2OrigConnectionIDNUM_Type(Integer32):
    """Custom type nlLlc2OrigConnectionIDNUM based on Integer32"""
    defaultValue = 0


_NlLlc2OrigConnectionIDNUM_Object = MibTableColumn
nlLlc2OrigConnectionIDNUM = _NlLlc2OrigConnectionIDNUM_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 7),
    _NlLlc2OrigConnectionIDNUM_Type()
)
nlLlc2OrigConnectionIDNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionIDNUM.setStatus("mandatory")


class _NlLlc2OrigConnectionMAXDATA_Type(Integer32):
    """Custom type nlLlc2OrigConnectionMAXDATA based on Integer32"""
    defaultValue = 0


_NlLlc2OrigConnectionMAXDATA_Object = MibTableColumn
nlLlc2OrigConnectionMAXDATA = _NlLlc2OrigConnectionMAXDATA_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 8),
    _NlLlc2OrigConnectionMAXDATA_Type()
)
nlLlc2OrigConnectionMAXDATA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionMAXDATA.setStatus("mandatory")


class _NlLlc2OrigConnectionMAXIN_Type(Integer32):
    """Custom type nlLlc2OrigConnectionMAXIN based on Integer32"""
    defaultValue = 0


_NlLlc2OrigConnectionMAXIN_Object = MibTableColumn
nlLlc2OrigConnectionMAXIN = _NlLlc2OrigConnectionMAXIN_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 9),
    _NlLlc2OrigConnectionMAXIN_Type()
)
nlLlc2OrigConnectionMAXIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionMAXIN.setStatus("mandatory")
_NlLlc2OrigConnectionRowStatus_Type = RowStatus
_NlLlc2OrigConnectionRowStatus_Object = MibTableColumn
nlLlc2OrigConnectionRowStatus = _NlLlc2OrigConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 3, 1, 10),
    _NlLlc2OrigConnectionRowStatus_Type()
)
nlLlc2OrigConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlLlc2OrigConnectionRowStatus.setStatus("mandatory")


class _NlLlc2NextHostNumber_Type(Integer32):
    """Custom type nlLlc2NextHostNumber based on Integer32"""
    defaultValue = 1


_NlLlc2NextHostNumber_Object = MibScalar
nlLlc2NextHostNumber = _NlLlc2NextHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 6, 4),
    _NlLlc2NextHostNumber_Type()
)
nlLlc2NextHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlLlc2NextHostNumber.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 7)
)
_PinStatusTable_Object = MibTable
pinStatusTable = _PinStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 7, 4)
)
if mibBuilder.loadTexts:
    pinStatusTable.setStatus("mandatory")
_PortPinEntry_Object = MibTableRow
portPinEntry = _PortPinEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 7, 4, 1)
)
portPinEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portPinRlp"),
    (0, "NETLINK-SPECIFIC-MIB", "portPinPort"),
)
if mibBuilder.loadTexts:
    portPinEntry.setStatus("mandatory")
_PortPinRlp_Type = Integer32
_PortPinRlp_Object = MibTableColumn
portPinRlp = _PortPinRlp_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 7, 4, 1, 1),
    _PortPinRlp_Type()
)
portPinRlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPinRlp.setStatus("mandatory")
_PortPinPort_Type = Integer32
_PortPinPort_Object = MibTableColumn
portPinPort = _PortPinPort_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 7, 4, 1, 2),
    _PortPinPort_Type()
)
portPinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPinPort.setStatus("mandatory")
_PortPinStatus_Type = OctetString
_PortPinStatus_Object = MibTableColumn
portPinStatus = _PortPinStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 7, 4, 1, 3),
    _PortPinStatus_Type()
)
portPinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPinStatus.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8)
)
_StatGroup_ObjectIdentity = ObjectIdentity
statGroup = _StatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1)
)
_RlpStatsTable_Object = MibTable
rlpStatsTable = _RlpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2)
)
if mibBuilder.loadTexts:
    rlpStatsTable.setStatus("mandatory")
_RlpStatsEntry_Object = MibTableRow
rlpStatsEntry = _RlpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1)
)
rlpStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "rlpStatsIndex"),
)
if mibBuilder.loadTexts:
    rlpStatsEntry.setStatus("mandatory")
_RlpStatsIndex_Type = Integer32
_RlpStatsIndex_Object = MibTableColumn
rlpStatsIndex = _RlpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 1),
    _RlpStatsIndex_Type()
)
rlpStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsIndex.setStatus("mandatory")
_RlpStatsQMessages_Type = Counter32
_RlpStatsQMessages_Object = MibTableColumn
rlpStatsQMessages = _RlpStatsQMessages_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 2),
    _RlpStatsQMessages_Type()
)
rlpStatsQMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsQMessages.setStatus("mandatory")
_RlpStatsUsedBuffers_Type = Counter32
_RlpStatsUsedBuffers_Object = MibTableColumn
rlpStatsUsedBuffers = _RlpStatsUsedBuffers_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 3),
    _RlpStatsUsedBuffers_Type()
)
rlpStatsUsedBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsUsedBuffers.setStatus("mandatory")
_RlpStatsInFrames_Type = Counter32
_RlpStatsInFrames_Object = MibTableColumn
rlpStatsInFrames = _RlpStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 4),
    _RlpStatsInFrames_Type()
)
rlpStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsInFrames.setStatus("mandatory")
_RlpStatsOutFrames_Type = Counter32
_RlpStatsOutFrames_Object = MibTableColumn
rlpStatsOutFrames = _RlpStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 5),
    _RlpStatsOutFrames_Type()
)
rlpStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsOutFrames.setStatus("mandatory")
_RlpStatsFrameRejects_Type = Counter32
_RlpStatsFrameRejects_Object = MibTableColumn
rlpStatsFrameRejects = _RlpStatsFrameRejects_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 6),
    _RlpStatsFrameRejects_Type()
)
rlpStatsFrameRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsFrameRejects.setStatus("mandatory")
_RlpStatsFrameRetransmits_Type = Counter32
_RlpStatsFrameRetransmits_Object = MibTableColumn
rlpStatsFrameRetransmits = _RlpStatsFrameRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 2, 1, 7),
    _RlpStatsFrameRetransmits_Type()
)
rlpStatsFrameRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpStatsFrameRetransmits.setStatus("mandatory")
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("mandatory")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1)
)
portStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portStatsRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portStatsIndex"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("mandatory")
_PortStatsRlpIndex_Type = Integer32
_PortStatsRlpIndex_Object = MibTableColumn
portStatsRlpIndex = _PortStatsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 1),
    _PortStatsRlpIndex_Type()
)
portStatsRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsRlpIndex.setStatus("mandatory")
_PortStatsIndex_Type = Integer32
_PortStatsIndex_Object = MibTableColumn
portStatsIndex = _PortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 2),
    _PortStatsIndex_Type()
)
portStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsIndex.setStatus("mandatory")
_PortStatsInFrames_Type = Counter32
_PortStatsInFrames_Object = MibTableColumn
portStatsInFrames = _PortStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 3),
    _PortStatsInFrames_Type()
)
portStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsInFrames.setStatus("mandatory")
_PortStatsOutFrames_Type = Counter32
_PortStatsOutFrames_Object = MibTableColumn
portStatsOutFrames = _PortStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 4),
    _PortStatsOutFrames_Type()
)
portStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOutFrames.setStatus("mandatory")
_PortStatsFrameRetrans_Type = Counter32
_PortStatsFrameRetrans_Object = MibTableColumn
portStatsFrameRetrans = _PortStatsFrameRetrans_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 5),
    _PortStatsFrameRetrans_Type()
)
portStatsFrameRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsFrameRetrans.setStatus("mandatory")
_PortStatsFCSErrors_Type = Counter32
_PortStatsFCSErrors_Object = MibTableColumn
portStatsFCSErrors = _PortStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 6),
    _PortStatsFCSErrors_Type()
)
portStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsFCSErrors.setStatus("mandatory")
_PortStatsLogicalRejects_Type = Counter32
_PortStatsLogicalRejects_Object = MibTableColumn
portStatsLogicalRejects = _PortStatsLogicalRejects_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 7),
    _PortStatsLogicalRejects_Type()
)
portStatsLogicalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsLogicalRejects.setStatus("mandatory")
_PortStatsInPercentUtils_Type = Counter32
_PortStatsInPercentUtils_Object = MibTableColumn
portStatsInPercentUtils = _PortStatsInPercentUtils_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 8),
    _PortStatsInPercentUtils_Type()
)
portStatsInPercentUtils.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsInPercentUtils.setStatus("mandatory")
_PortStatsOutPercentUtils_Type = Counter32
_PortStatsOutPercentUtils_Object = MibTableColumn
portStatsOutPercentUtils = _PortStatsOutPercentUtils_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 3, 1, 9),
    _PortStatsOutPercentUtils_Type()
)
portStatsOutPercentUtils.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOutPercentUtils.setStatus("mandatory")
_StatFrame_ObjectIdentity = ObjectIdentity
statFrame = _StatFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4)
)
_FrStatsTable_Object = MibTable
frStatsTable = _FrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    frStatsTable.setStatus("mandatory")
_FrStatsEntry_Object = MibTableRow
frStatsEntry = _FrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1)
)
frStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "frStatsRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "frStatsPortIndex"),
)
if mibBuilder.loadTexts:
    frStatsEntry.setStatus("mandatory")
_FrStatsRlpIndex_Type = Integer32
_FrStatsRlpIndex_Object = MibTableColumn
frStatsRlpIndex = _FrStatsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 1),
    _FrStatsRlpIndex_Type()
)
frStatsRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRlpIndex.setStatus("mandatory")
_FrStatsPortIndex_Type = Integer32
_FrStatsPortIndex_Object = MibTableColumn
frStatsPortIndex = _FrStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 2),
    _FrStatsPortIndex_Type()
)
frStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsPortIndex.setStatus("mandatory")
_FrStatsTxDEFrames_Type = Counter32
_FrStatsTxDEFrames_Object = MibTableColumn
frStatsTxDEFrames = _FrStatsTxDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 3),
    _FrStatsTxDEFrames_Type()
)
frStatsTxDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTxDEFrames.setStatus("mandatory")
_FrStatsRxDEFrames_Type = Counter32
_FrStatsRxDEFrames_Object = MibTableColumn
frStatsRxDEFrames = _FrStatsRxDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 4),
    _FrStatsRxDEFrames_Type()
)
frStatsRxDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRxDEFrames.setStatus("mandatory")
_FrStatsTxFECNFrames_Type = Counter32
_FrStatsTxFECNFrames_Object = MibTableColumn
frStatsTxFECNFrames = _FrStatsTxFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 5),
    _FrStatsTxFECNFrames_Type()
)
frStatsTxFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTxFECNFrames.setStatus("mandatory")
_FrStatsRxFECNFrames_Type = Counter32
_FrStatsRxFECNFrames_Object = MibTableColumn
frStatsRxFECNFrames = _FrStatsRxFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 6),
    _FrStatsRxFECNFrames_Type()
)
frStatsRxFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRxFECNFrames.setStatus("mandatory")
_FrStatsTxBECNFrames_Type = Counter32
_FrStatsTxBECNFrames_Object = MibTableColumn
frStatsTxBECNFrames = _FrStatsTxBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 7),
    _FrStatsTxBECNFrames_Type()
)
frStatsTxBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTxBECNFrames.setStatus("mandatory")
_FrStatsRxBECNFrames_Type = Counter32
_FrStatsRxBECNFrames_Object = MibTableColumn
frStatsRxBECNFrames = _FrStatsRxBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 8),
    _FrStatsRxBECNFrames_Type()
)
frStatsRxBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRxBECNFrames.setStatus("mandatory")
_FrStatsTxLMIFrames_Type = Counter32
_FrStatsTxLMIFrames_Object = MibTableColumn
frStatsTxLMIFrames = _FrStatsTxLMIFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 9),
    _FrStatsTxLMIFrames_Type()
)
frStatsTxLMIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTxLMIFrames.setStatus("mandatory")
_FrStatsRxLMIFrames_Type = Counter32
_FrStatsRxLMIFrames_Object = MibTableColumn
frStatsRxLMIFrames = _FrStatsRxLMIFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 10),
    _FrStatsRxLMIFrames_Type()
)
frStatsRxLMIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRxLMIFrames.setStatus("mandatory")
_FrStatsTxANXDFrames_Type = Counter32
_FrStatsTxANXDFrames_Object = MibTableColumn
frStatsTxANXDFrames = _FrStatsTxANXDFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 11),
    _FrStatsTxANXDFrames_Type()
)
frStatsTxANXDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTxANXDFrames.setStatus("mandatory")
_FrStatsRxANXDFrames_Type = Counter32
_FrStatsRxANXDFrames_Object = MibTableColumn
frStatsRxANXDFrames = _FrStatsRxANXDFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 12),
    _FrStatsRxANXDFrames_Type()
)
frStatsRxANXDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsRxANXDFrames.setStatus("mandatory")
_FrStatsTotDiscFrames_Type = Counter32
_FrStatsTotDiscFrames_Object = MibTableColumn
frStatsTotDiscFrames = _FrStatsTotDiscFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 1, 1, 13),
    _FrStatsTotDiscFrames_Type()
)
frStatsTotDiscFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsTotDiscFrames.setStatus("mandatory")
_X25TxStatsTable_Object = MibTable
x25TxStatsTable = _X25TxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    x25TxStatsTable.setStatus("mandatory")
_X25TxStatsEntry_Object = MibTableRow
x25TxStatsEntry = _X25TxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1)
)
x25TxStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "x25TxRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "x25TxPortIndex"),
)
if mibBuilder.loadTexts:
    x25TxStatsEntry.setStatus("mandatory")
_X25TxRlpIndex_Type = Integer32
_X25TxRlpIndex_Object = MibTableColumn
x25TxRlpIndex = _X25TxRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 1),
    _X25TxRlpIndex_Type()
)
x25TxRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxRlpIndex.setStatus("mandatory")
_X25TxPortIndex_Type = Integer32
_X25TxPortIndex_Object = MibTableColumn
x25TxPortIndex = _X25TxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 2),
    _X25TxPortIndex_Type()
)
x25TxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxPortIndex.setStatus("mandatory")
_X25TxSABMFrames_Type = Counter32
_X25TxSABMFrames_Object = MibTableColumn
x25TxSABMFrames = _X25TxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 3),
    _X25TxSABMFrames_Type()
)
x25TxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxSABMFrames.setStatus("mandatory")
_X25TxUAFrames_Type = Counter32
_X25TxUAFrames_Object = MibTableColumn
x25TxUAFrames = _X25TxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 4),
    _X25TxUAFrames_Type()
)
x25TxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxUAFrames.setStatus("mandatory")
_X25TxDISCFrames_Type = Counter32
_X25TxDISCFrames_Object = MibTableColumn
x25TxDISCFrames = _X25TxDISCFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 5),
    _X25TxDISCFrames_Type()
)
x25TxDISCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxDISCFrames.setStatus("mandatory")
_X25TxDMFrames_Type = Counter32
_X25TxDMFrames_Object = MibTableColumn
x25TxDMFrames = _X25TxDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 6),
    _X25TxDMFrames_Type()
)
x25TxDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxDMFrames.setStatus("mandatory")
_X25TxFRMRFrames_Type = Counter32
_X25TxFRMRFrames_Object = MibTableColumn
x25TxFRMRFrames = _X25TxFRMRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 7),
    _X25TxFRMRFrames_Type()
)
x25TxFRMRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxFRMRFrames.setStatus("mandatory")
_X25TxREJFrames_Type = Counter32
_X25TxREJFrames_Object = MibTableColumn
x25TxREJFrames = _X25TxREJFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 8),
    _X25TxREJFrames_Type()
)
x25TxREJFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxREJFrames.setStatus("mandatory")
_X25TxRRFrames_Type = Counter32
_X25TxRRFrames_Object = MibTableColumn
x25TxRRFrames = _X25TxRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 9),
    _X25TxRRFrames_Type()
)
x25TxRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxRRFrames.setStatus("mandatory")
_X25TxRNRFrames_Type = Counter32
_X25TxRNRFrames_Object = MibTableColumn
x25TxRNRFrames = _X25TxRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 10),
    _X25TxRNRFrames_Type()
)
x25TxRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxRNRFrames.setStatus("mandatory")
_X25TxINFOFrames_Type = Counter32
_X25TxINFOFrames_Object = MibTableColumn
x25TxINFOFrames = _X25TxINFOFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 2, 1, 11),
    _X25TxINFOFrames_Type()
)
x25TxINFOFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TxINFOFrames.setStatus("mandatory")
_X25RxStatsTable_Object = MibTable
x25RxStatsTable = _X25RxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3)
)
if mibBuilder.loadTexts:
    x25RxStatsTable.setStatus("mandatory")
_X25RxStatsEntry_Object = MibTableRow
x25RxStatsEntry = _X25RxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1)
)
x25RxStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "x25RxRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "x25RxPortIndex"),
)
if mibBuilder.loadTexts:
    x25RxStatsEntry.setStatus("mandatory")
_X25RxRlpIndex_Type = Integer32
_X25RxRlpIndex_Object = MibTableColumn
x25RxRlpIndex = _X25RxRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 1),
    _X25RxRlpIndex_Type()
)
x25RxRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxRlpIndex.setStatus("mandatory")
_X25RxPortIndex_Type = Integer32
_X25RxPortIndex_Object = MibTableColumn
x25RxPortIndex = _X25RxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 2),
    _X25RxPortIndex_Type()
)
x25RxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxPortIndex.setStatus("mandatory")
_X25RxSABMFrames_Type = Counter32
_X25RxSABMFrames_Object = MibTableColumn
x25RxSABMFrames = _X25RxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 3),
    _X25RxSABMFrames_Type()
)
x25RxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxSABMFrames.setStatus("mandatory")
_X25RxUAFrames_Type = Counter32
_X25RxUAFrames_Object = MibTableColumn
x25RxUAFrames = _X25RxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 4),
    _X25RxUAFrames_Type()
)
x25RxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxUAFrames.setStatus("mandatory")
_X25RxDISCFrames_Type = Counter32
_X25RxDISCFrames_Object = MibTableColumn
x25RxDISCFrames = _X25RxDISCFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 5),
    _X25RxDISCFrames_Type()
)
x25RxDISCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxDISCFrames.setStatus("mandatory")
_X25RxDMFrames_Type = Counter32
_X25RxDMFrames_Object = MibTableColumn
x25RxDMFrames = _X25RxDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 6),
    _X25RxDMFrames_Type()
)
x25RxDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxDMFrames.setStatus("mandatory")
_X25RxFRMRFrames_Type = Counter32
_X25RxFRMRFrames_Object = MibTableColumn
x25RxFRMRFrames = _X25RxFRMRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 7),
    _X25RxFRMRFrames_Type()
)
x25RxFRMRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxFRMRFrames.setStatus("mandatory")
_X25RxREJFrames_Type = Counter32
_X25RxREJFrames_Object = MibTableColumn
x25RxREJFrames = _X25RxREJFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 8),
    _X25RxREJFrames_Type()
)
x25RxREJFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxREJFrames.setStatus("mandatory")
_X25RxRRFrames_Type = Counter32
_X25RxRRFrames_Object = MibTableColumn
x25RxRRFrames = _X25RxRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 9),
    _X25RxRRFrames_Type()
)
x25RxRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxRRFrames.setStatus("mandatory")
_X25RxRNRFrames_Type = Counter32
_X25RxRNRFrames_Object = MibTableColumn
x25RxRNRFrames = _X25RxRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 10),
    _X25RxRNRFrames_Type()
)
x25RxRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxRNRFrames.setStatus("mandatory")
_X25RxINFOFrames_Type = Counter32
_X25RxINFOFrames_Object = MibTableColumn
x25RxINFOFrames = _X25RxINFOFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 4, 3, 1, 11),
    _X25RxINFOFrames_Type()
)
x25RxINFOFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RxINFOFrames.setStatus("mandatory")
_StatBag_ObjectIdentity = ObjectIdentity
statBag = _StatBag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 5)
)
_StatIp_ObjectIdentity = ObjectIdentity
statIp = _StatIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 6)
)
_StatT1_ObjectIdentity = ObjectIdentity
statT1 = _StatT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7)
)
_T1StatsTable_Object = MibTable
t1StatsTable = _T1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    t1StatsTable.setStatus("mandatory")
_T1StatsEntry_Object = MibTableRow
t1StatsEntry = _T1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1)
)
t1StatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "t1StatsRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "t1StatsPortIndex"),
)
if mibBuilder.loadTexts:
    t1StatsEntry.setStatus("mandatory")
_T1StatsRlpIndex_Type = Integer32
_T1StatsRlpIndex_Object = MibTableColumn
t1StatsRlpIndex = _T1StatsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 1),
    _T1StatsRlpIndex_Type()
)
t1StatsRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRlpIndex.setStatus("mandatory")
_T1StatsPortIndex_Type = Integer32
_T1StatsPortIndex_Object = MibTableColumn
t1StatsPortIndex = _T1StatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 2),
    _T1StatsPortIndex_Type()
)
t1StatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsPortIndex.setStatus("mandatory")
_T1StatsRcvFrames_Type = Counter32
_T1StatsRcvFrames_Object = MibTableColumn
t1StatsRcvFrames = _T1StatsRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 3),
    _T1StatsRcvFrames_Type()
)
t1StatsRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvFrames.setStatus("mandatory")
_T1StatsXmitFrames_Type = Counter32
_T1StatsXmitFrames_Object = MibTableColumn
t1StatsXmitFrames = _T1StatsXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 4),
    _T1StatsXmitFrames_Type()
)
t1StatsXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsXmitFrames.setStatus("mandatory")
_T1StatsLCVCnt_Type = Counter32
_T1StatsLCVCnt_Object = MibTableColumn
t1StatsLCVCnt = _T1StatsLCVCnt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 5),
    _T1StatsLCVCnt_Type()
)
t1StatsLCVCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsLCVCnt.setStatus("mandatory")
_T1StatsPCVRErrs_Type = Counter32
_T1StatsPCVRErrs_Object = MibTableColumn
t1StatsPCVRErrs = _T1StatsPCVRErrs_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 6),
    _T1StatsPCVRErrs_Type()
)
t1StatsPCVRErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsPCVRErrs.setStatus("mandatory")
_T1StatsOOSCnt_Type = Counter32
_T1StatsOOSCnt_Object = MibTableColumn
t1StatsOOSCnt = _T1StatsOOSCnt_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 7),
    _T1StatsOOSCnt_Type()
)
t1StatsOOSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsOOSCnt.setStatus("mandatory")
_T1StatsBlueAlarms_Type = Counter32
_T1StatsBlueAlarms_Object = MibTableColumn
t1StatsBlueAlarms = _T1StatsBlueAlarms_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 8),
    _T1StatsBlueAlarms_Type()
)
t1StatsBlueAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsBlueAlarms.setStatus("mandatory")
_T1StatsYellowAlarms_Type = Counter32
_T1StatsYellowAlarms_Object = MibTableColumn
t1StatsYellowAlarms = _T1StatsYellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 9),
    _T1StatsYellowAlarms_Type()
)
t1StatsYellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsYellowAlarms.setStatus("mandatory")
_T1StatsRedAlarms_Type = Counter32
_T1StatsRedAlarms_Object = MibTableColumn
t1StatsRedAlarms = _T1StatsRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 10),
    _T1StatsRedAlarms_Type()
)
t1StatsRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRedAlarms.setStatus("mandatory")
_T1StatsRcvUsage_Type = Counter32
_T1StatsRcvUsage_Object = MibTableColumn
t1StatsRcvUsage = _T1StatsRcvUsage_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 11),
    _T1StatsRcvUsage_Type()
)
t1StatsRcvUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvUsage.setStatus("mandatory")
_T1StatsXmitUsage_Type = Counter32
_T1StatsXmitUsage_Object = MibTableColumn
t1StatsXmitUsage = _T1StatsXmitUsage_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 12),
    _T1StatsXmitUsage_Type()
)
t1StatsXmitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsXmitUsage.setStatus("mandatory")
_T1StatsXmitAbortFrames_Type = Counter32
_T1StatsXmitAbortFrames_Object = MibTableColumn
t1StatsXmitAbortFrames = _T1StatsXmitAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 13),
    _T1StatsXmitAbortFrames_Type()
)
t1StatsXmitAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsXmitAbortFrames.setStatus("mandatory")
_T1StatsRcvAbortFrames_Type = Counter32
_T1StatsRcvAbortFrames_Object = MibTableColumn
t1StatsRcvAbortFrames = _T1StatsRcvAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 14),
    _T1StatsRcvAbortFrames_Type()
)
t1StatsRcvAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvAbortFrames.setStatus("mandatory")
_T1StatsRcvOverruns_Type = Counter32
_T1StatsRcvOverruns_Object = MibTableColumn
t1StatsRcvOverruns = _T1StatsRcvOverruns_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 15),
    _T1StatsRcvOverruns_Type()
)
t1StatsRcvOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvOverruns.setStatus("mandatory")
_T1StatsRcvErrors_Type = Counter32
_T1StatsRcvErrors_Object = MibTableColumn
t1StatsRcvErrors = _T1StatsRcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 16),
    _T1StatsRcvErrors_Type()
)
t1StatsRcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvErrors.setStatus("mandatory")
_T1StatsRcvChannelErrors_Type = Counter32
_T1StatsRcvChannelErrors_Object = MibTableColumn
t1StatsRcvChannelErrors = _T1StatsRcvChannelErrors_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 7, 1, 1, 17),
    _T1StatsRcvChannelErrors_Type()
)
t1StatsRcvChannelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsRcvChannelErrors.setStatus("mandatory")
_StatDS0A_ObjectIdentity = ObjectIdentity
statDS0A = _StatDS0A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8)
)
_Ds0aStatsTable_Object = MibTable
ds0aStatsTable = _Ds0aStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ds0aStatsTable.setStatus("mandatory")
_Ds0aStatsEntry_Object = MibTableRow
ds0aStatsEntry = _Ds0aStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1)
)
ds0aStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "ds0aStatsRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "ds0aStatsPortIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "ds0aStatsChannelIndex"),
)
if mibBuilder.loadTexts:
    ds0aStatsEntry.setStatus("mandatory")
_Ds0aStatsRlpIndex_Type = Integer32
_Ds0aStatsRlpIndex_Object = MibTableColumn
ds0aStatsRlpIndex = _Ds0aStatsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 1),
    _Ds0aStatsRlpIndex_Type()
)
ds0aStatsRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsRlpIndex.setStatus("mandatory")
_Ds0aStatsPortIndex_Type = Integer32
_Ds0aStatsPortIndex_Object = MibTableColumn
ds0aStatsPortIndex = _Ds0aStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 2),
    _Ds0aStatsPortIndex_Type()
)
ds0aStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsPortIndex.setStatus("mandatory")
_Ds0aStatsChannelIndex_Type = Integer32
_Ds0aStatsChannelIndex_Object = MibTableColumn
ds0aStatsChannelIndex = _Ds0aStatsChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 3),
    _Ds0aStatsChannelIndex_Type()
)
ds0aStatsChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsChannelIndex.setStatus("mandatory")
_Ds0aStatsXmitFrames_Type = Counter32
_Ds0aStatsXmitFrames_Object = MibTableColumn
ds0aStatsXmitFrames = _Ds0aStatsXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 4),
    _Ds0aStatsXmitFrames_Type()
)
ds0aStatsXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsXmitFrames.setStatus("mandatory")
_Ds0aStatsRcvFrames_Type = Counter32
_Ds0aStatsRcvFrames_Object = MibTableColumn
ds0aStatsRcvFrames = _Ds0aStatsRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 5),
    _Ds0aStatsRcvFrames_Type()
)
ds0aStatsRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsRcvFrames.setStatus("mandatory")
_Ds0aStatsRcvAbortFrames_Type = Counter32
_Ds0aStatsRcvAbortFrames_Object = MibTableColumn
ds0aStatsRcvAbortFrames = _Ds0aStatsRcvAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 6),
    _Ds0aStatsRcvAbortFrames_Type()
)
ds0aStatsRcvAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsRcvAbortFrames.setStatus("mandatory")
_Ds0aStatsRcvOverruns_Type = Counter32
_Ds0aStatsRcvOverruns_Object = MibTableColumn
ds0aStatsRcvOverruns = _Ds0aStatsRcvOverruns_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 7),
    _Ds0aStatsRcvOverruns_Type()
)
ds0aStatsRcvOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsRcvOverruns.setStatus("mandatory")
_Ds0aStatsRcvErrors_Type = Counter32
_Ds0aStatsRcvErrors_Object = MibTableColumn
ds0aStatsRcvErrors = _Ds0aStatsRcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 8, 1, 1, 8),
    _Ds0aStatsRcvErrors_Type()
)
ds0aStatsRcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0aStatsRcvErrors.setStatus("mandatory")
_StatVoice_ObjectIdentity = ObjectIdentity
statVoice = _StatVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9)
)
_VoiceStatsTable_Object = MibTable
voiceStatsTable = _VoiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1)
)
if mibBuilder.loadTexts:
    voiceStatsTable.setStatus("mandatory")
_VoiceStatsEntry_Object = MibTableRow
voiceStatsEntry = _VoiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1)
)
voiceStatsEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "voiceStatsRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "voiceStatsPortIndex"),
)
if mibBuilder.loadTexts:
    voiceStatsEntry.setStatus("mandatory")
_VoiceStatsRlpIndex_Type = Integer32
_VoiceStatsRlpIndex_Object = MibTableColumn
voiceStatsRlpIndex = _VoiceStatsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 1),
    _VoiceStatsRlpIndex_Type()
)
voiceStatsRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsRlpIndex.setStatus("mandatory")
_VoiceStatsPortIndex_Type = Integer32
_VoiceStatsPortIndex_Object = MibTableColumn
voiceStatsPortIndex = _VoiceStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 2),
    _VoiceStatsPortIndex_Type()
)
voiceStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsPortIndex.setStatus("mandatory")
_VoiceStatsRxCalls_Type = Counter32
_VoiceStatsRxCalls_Object = MibTableColumn
voiceStatsRxCalls = _VoiceStatsRxCalls_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 3),
    _VoiceStatsRxCalls_Type()
)
voiceStatsRxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsRxCalls.setStatus("mandatory")
_VoiceStatsTxCalls_Type = Counter32
_VoiceStatsTxCalls_Object = MibTableColumn
voiceStatsTxCalls = _VoiceStatsTxCalls_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 4),
    _VoiceStatsTxCalls_Type()
)
voiceStatsTxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsTxCalls.setStatus("mandatory")
_VoiceStatsRxCallsAccepts_Type = Counter32
_VoiceStatsRxCallsAccepts_Object = MibTableColumn
voiceStatsRxCallsAccepts = _VoiceStatsRxCallsAccepts_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 5),
    _VoiceStatsRxCallsAccepts_Type()
)
voiceStatsRxCallsAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsRxCallsAccepts.setStatus("mandatory")
_VoiceStatsTxCallsAccepts_Type = Counter32
_VoiceStatsTxCallsAccepts_Object = MibTableColumn
voiceStatsTxCallsAccepts = _VoiceStatsTxCallsAccepts_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 6),
    _VoiceStatsTxCallsAccepts_Type()
)
voiceStatsTxCallsAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsTxCallsAccepts.setStatus("mandatory")
_VoiceStatsRxClears_Type = Counter32
_VoiceStatsRxClears_Object = MibTableColumn
voiceStatsRxClears = _VoiceStatsRxClears_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 7),
    _VoiceStatsRxClears_Type()
)
voiceStatsRxClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsRxClears.setStatus("mandatory")
_VoiceStatsTxClears_Type = Counter32
_VoiceStatsTxClears_Object = MibTableColumn
voiceStatsTxClears = _VoiceStatsTxClears_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 8),
    _VoiceStatsTxClears_Type()
)
voiceStatsTxClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsTxClears.setStatus("mandatory")
_VoiceStatsBusyCalls_Type = Counter32
_VoiceStatsBusyCalls_Object = MibTableColumn
voiceStatsBusyCalls = _VoiceStatsBusyCalls_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 9),
    _VoiceStatsBusyCalls_Type()
)
voiceStatsBusyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsBusyCalls.setStatus("mandatory")
_VoiceStatsCallTimeouts_Type = Counter32
_VoiceStatsCallTimeouts_Object = MibTableColumn
voiceStatsCallTimeouts = _VoiceStatsCallTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 10),
    _VoiceStatsCallTimeouts_Type()
)
voiceStatsCallTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsCallTimeouts.setStatus("mandatory")
_VoiceStatsRxCongestions_Type = Counter32
_VoiceStatsRxCongestions_Object = MibTableColumn
voiceStatsRxCongestions = _VoiceStatsRxCongestions_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 11),
    _VoiceStatsRxCongestions_Type()
)
voiceStatsRxCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsRxCongestions.setStatus("mandatory")
_VoiceStatsTxCongestions_Type = Counter32
_VoiceStatsTxCongestions_Object = MibTableColumn
voiceStatsTxCongestions = _VoiceStatsTxCongestions_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 1, 9, 1, 1, 12),
    _VoiceStatsTxCongestions_Type()
)
voiceStatsTxCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatsTxCongestions.setStatus("mandatory")
_StatThresh_ObjectIdentity = ObjectIdentity
statThresh = _StatThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2)
)
_RlpThreshTable_Object = MibTable
rlpThreshTable = _RlpThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rlpThreshTable.setStatus("mandatory")
_RlpThreshEntry_Object = MibTableRow
rlpThreshEntry = _RlpThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1)
)
rlpThreshEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "rlpThreshRlpIndex"),
)
if mibBuilder.loadTexts:
    rlpThreshEntry.setStatus("mandatory")
_RlpThreshRlpIndex_Type = Integer32
_RlpThreshRlpIndex_Object = MibTableColumn
rlpThreshRlpIndex = _RlpThreshRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 1),
    _RlpThreshRlpIndex_Type()
)
rlpThreshRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshRlpIndex.setStatus("mandatory")
_RlpThreshPercntBufInUse_Type = Integer32
_RlpThreshPercntBufInUse_Object = MibTableColumn
rlpThreshPercntBufInUse = _RlpThreshPercntBufInUse_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 2),
    _RlpThreshPercntBufInUse_Type()
)
rlpThreshPercntBufInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshPercntBufInUse.setStatus("mandatory")
_RlpThreshMsgQueueLen_Type = Integer32
_RlpThreshMsgQueueLen_Object = MibTableColumn
rlpThreshMsgQueueLen = _RlpThreshMsgQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 3),
    _RlpThreshMsgQueueLen_Type()
)
rlpThreshMsgQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshMsgQueueLen.setStatus("mandatory")
_RlpThreshRxFramesPerSec_Type = Integer32
_RlpThreshRxFramesPerSec_Object = MibTableColumn
rlpThreshRxFramesPerSec = _RlpThreshRxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 4),
    _RlpThreshRxFramesPerSec_Type()
)
rlpThreshRxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshRxFramesPerSec.setStatus("mandatory")
_RlpThreshTxFramesPerSec_Type = Integer32
_RlpThreshTxFramesPerSec_Object = MibTableColumn
rlpThreshTxFramesPerSec = _RlpThreshTxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 5),
    _RlpThreshTxFramesPerSec_Type()
)
rlpThreshTxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshTxFramesPerSec.setStatus("mandatory")
_RlpThreshRejFramesPerSec_Type = Integer32
_RlpThreshRejFramesPerSec_Object = MibTableColumn
rlpThreshRejFramesPerSec = _RlpThreshRejFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 6),
    _RlpThreshRejFramesPerSec_Type()
)
rlpThreshRejFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshRejFramesPerSec.setStatus("mandatory")
_RlpThreshRtxFramesPerSec_Type = Integer32
_RlpThreshRtxFramesPerSec_Object = MibTableColumn
rlpThreshRtxFramesPerSec = _RlpThreshRtxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 1, 1, 7),
    _RlpThreshRtxFramesPerSec_Type()
)
rlpThreshRtxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlpThreshRtxFramesPerSec.setStatus("mandatory")
_PortThreshTable_Object = MibTable
portThreshTable = _PortThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2)
)
if mibBuilder.loadTexts:
    portThreshTable.setStatus("mandatory")
_PortThreshEntry_Object = MibTableRow
portThreshEntry = _PortThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1)
)
portThreshEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "portThreshRlpIndex"),
    (0, "NETLINK-SPECIFIC-MIB", "portThreshIndex"),
)
if mibBuilder.loadTexts:
    portThreshEntry.setStatus("mandatory")
_PortThreshRlpIndex_Type = Integer32
_PortThreshRlpIndex_Object = MibTableColumn
portThreshRlpIndex = _PortThreshRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 1),
    _PortThreshRlpIndex_Type()
)
portThreshRlpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshRlpIndex.setStatus("mandatory")
_PortThreshIndex_Type = Integer32
_PortThreshIndex_Object = MibTableColumn
portThreshIndex = _PortThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 2),
    _PortThreshIndex_Type()
)
portThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshIndex.setStatus("mandatory")
_PortThreshRxFramesPerSec_Type = Integer32
_PortThreshRxFramesPerSec_Object = MibTableColumn
portThreshRxFramesPerSec = _PortThreshRxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 3),
    _PortThreshRxFramesPerSec_Type()
)
portThreshRxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshRxFramesPerSec.setStatus("mandatory")
_PortThreshTxFramesPerSec_Type = Integer32
_PortThreshTxFramesPerSec_Object = MibTableColumn
portThreshTxFramesPerSec = _PortThreshTxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 4),
    _PortThreshTxFramesPerSec_Type()
)
portThreshTxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshTxFramesPerSec.setStatus("mandatory")
_PortThreshRtxFramesPerSec_Type = Integer32
_PortThreshRtxFramesPerSec_Object = MibTableColumn
portThreshRtxFramesPerSec = _PortThreshRtxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 5),
    _PortThreshRtxFramesPerSec_Type()
)
portThreshRtxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshRtxFramesPerSec.setStatus("mandatory")
_PortThreshFCSErrPerSec_Type = Integer32
_PortThreshFCSErrPerSec_Object = MibTableColumn
portThreshFCSErrPerSec = _PortThreshFCSErrPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 6),
    _PortThreshFCSErrPerSec_Type()
)
portThreshFCSErrPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshFCSErrPerSec.setStatus("mandatory")
_PortThreshLogRejPerSec_Type = Integer32
_PortThreshLogRejPerSec_Object = MibTableColumn
portThreshLogRejPerSec = _PortThreshLogRejPerSec_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 7),
    _PortThreshLogRejPerSec_Type()
)
portThreshLogRejPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshLogRejPerSec.setStatus("mandatory")
_PortThreshTxErrorRatio_Type = Integer32
_PortThreshTxErrorRatio_Object = MibTableColumn
portThreshTxErrorRatio = _PortThreshTxErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 8),
    _PortThreshTxErrorRatio_Type()
)
portThreshTxErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshTxErrorRatio.setStatus("mandatory")
_PortThreshRxErrorRatio_Type = Integer32
_PortThreshRxErrorRatio_Object = MibTableColumn
portThreshRxErrorRatio = _PortThreshRxErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 9),
    _PortThreshRxErrorRatio_Type()
)
portThreshRxErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshRxErrorRatio.setStatus("mandatory")
_PortThreshTxPercentUtl_Type = Integer32
_PortThreshTxPercentUtl_Object = MibTableColumn
portThreshTxPercentUtl = _PortThreshTxPercentUtl_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 10),
    _PortThreshTxPercentUtl_Type()
)
portThreshTxPercentUtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshTxPercentUtl.setStatus("mandatory")
_PortThreshRxPercentUtl_Type = Integer32
_PortThreshRxPercentUtl_Object = MibTableColumn
portThreshRxPercentUtl = _PortThreshRxPercentUtl_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 8, 2, 2, 1, 11),
    _PortThreshRxPercentUtl_Type()
)
portThreshRxPercentUtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portThreshRxPercentUtl.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 9)
)


class _BridgeAdminVirtualLANID_Type(Integer32):
    """Custom type bridgeAdminVirtualLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeAdminVirtualLANID_Type.__name__ = "Integer32"
_BridgeAdminVirtualLANID_Object = MibScalar
bridgeAdminVirtualLANID = _BridgeAdminVirtualLANID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 1),
    _BridgeAdminVirtualLANID_Type()
)
bridgeAdminVirtualLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAdminVirtualLANID.setStatus("mandatory")


class _BridgeOperVirtualLANID_Type(Integer32):
    """Custom type bridgeOperVirtualLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeOperVirtualLANID_Type.__name__ = "Integer32"
_BridgeOperVirtualLANID_Object = MibScalar
bridgeOperVirtualLANID = _BridgeOperVirtualLANID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 2),
    _BridgeOperVirtualLANID_Type()
)
bridgeOperVirtualLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeOperVirtualLANID.setStatus("mandatory")


class _BridgeEnabled_Type(Integer32):
    """Custom type bridgeEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BridgeEnabled_Type.__name__ = "Integer32"
_BridgeEnabled_Object = MibScalar
bridgeEnabled = _BridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 3),
    _BridgeEnabled_Type()
)
bridgeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEnabled.setStatus("mandatory")


class _BridgeMaxSizeForwardingTable_Type(Integer32):
    """Custom type bridgeMaxSizeForwardingTable based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 65535),
    )


_BridgeMaxSizeForwardingTable_Type.__name__ = "Integer32"
_BridgeMaxSizeForwardingTable_Object = MibScalar
bridgeMaxSizeForwardingTable = _BridgeMaxSizeForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 4),
    _BridgeMaxSizeForwardingTable_Type()
)
bridgeMaxSizeForwardingTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMaxSizeForwardingTable.setStatus("mandatory")


class _BridgeIPEnabled_Type(Integer32):
    """Custom type bridgeIPEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BridgeIPEnabled_Type.__name__ = "Integer32"
_BridgeIPEnabled_Object = MibScalar
bridgeIPEnabled = _BridgeIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 5),
    _BridgeIPEnabled_Type()
)
bridgeIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIPEnabled.setStatus("mandatory")


class _BridgeIPXEnabled_Type(Integer32):
    """Custom type bridgeIPXEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BridgeIPXEnabled_Type.__name__ = "Integer32"
_BridgeIPXEnabled_Object = MibScalar
bridgeIPXEnabled = _BridgeIPXEnabled_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 6),
    _BridgeIPXEnabled_Type()
)
bridgeIPXEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIPXEnabled.setStatus("mandatory")


class _BridgeAdminSRBID_Type(Integer32):
    """Custom type bridgeAdminSRBID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BridgeAdminSRBID_Type.__name__ = "Integer32"
_BridgeAdminSRBID_Object = MibScalar
bridgeAdminSRBID = _BridgeAdminSRBID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 7),
    _BridgeAdminSRBID_Type()
)
bridgeAdminSRBID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAdminSRBID.setStatus("mandatory")


class _BridgeOperSRBID_Type(Integer32):
    """Custom type bridgeOperSRBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BridgeOperSRBID_Type.__name__ = "Integer32"
_BridgeOperSRBID_Object = MibScalar
bridgeOperSRBID = _BridgeOperSRBID_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 8),
    _BridgeOperSRBID_Type()
)
bridgeOperSRBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeOperSRBID.setStatus("mandatory")


class _BridgeDefaultEthernetFrameType_Type(Integer32):
    """Custom type bridgeDefaultEthernetFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023", 2),
          ("type-II", 1))
    )


_BridgeDefaultEthernetFrameType_Type.__name__ = "Integer32"
_BridgeDefaultEthernetFrameType_Object = MibScalar
bridgeDefaultEthernetFrameType = _BridgeDefaultEthernetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 9, 9),
    _BridgeDefaultEthernetFrameType_Type()
)
bridgeDefaultEthernetFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeDefaultEthernetFrameType.setStatus("mandatory")
_IpNl_ObjectIdentity = ObjectIdentity
ipNl = _IpNl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 11)
)


class _NlIpDefaultRIPVersion_Type(Integer32):
    """Custom type nlIpDefaultRIPVersion based on Integer32"""
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
        *(("rip1Compatible", 2),
          ("ripVersion1", 1),
          ("ripVersion2", 3))
    )


_NlIpDefaultRIPVersion_Type.__name__ = "Integer32"
_NlIpDefaultRIPVersion_Object = MibScalar
nlIpDefaultRIPVersion = _NlIpDefaultRIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 11, 1),
    _NlIpDefaultRIPVersion_Type()
)
nlIpDefaultRIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlIpDefaultRIPVersion.setStatus("mandatory")
_Voice_ObjectIdentity = ObjectIdentity
voice = _Voice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 173, 7, 12)
)


class _VoiceSystemVoiceNodeNum_Type(Integer32):
    """Custom type voiceSystemVoiceNodeNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_VoiceSystemVoiceNodeNum_Type.__name__ = "Integer32"
_VoiceSystemVoiceNodeNum_Object = MibScalar
voiceSystemVoiceNodeNum = _VoiceSystemVoiceNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 1),
    _VoiceSystemVoiceNodeNum_Type()
)
voiceSystemVoiceNodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemVoiceNodeNum.setStatus("mandatory")


class _VoiceSystemRingVolFreq_Type(Integer32):
    """Custom type voiceSystemRingVolFreq based on Integer32"""
    defaultValue = 2

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
        *(("v60-hz-50-00", 4),
          ("v75-hz-16-66", 1),
          ("v75-hz-25-00", 3),
          ("v75-hz-50-00", 5),
          ("v80-hz-20-00", 2))
    )


_VoiceSystemRingVolFreq_Type.__name__ = "Integer32"
_VoiceSystemRingVolFreq_Object = MibScalar
voiceSystemRingVolFreq = _VoiceSystemRingVolFreq_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 2),
    _VoiceSystemRingVolFreq_Type()
)
voiceSystemRingVolFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemRingVolFreq.setStatus("mandatory")


class _VoiceSystemCountryCode_Type(Integer32):
    """Custom type voiceSystemCountryCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_VoiceSystemCountryCode_Type.__name__ = "Integer32"
_VoiceSystemCountryCode_Object = MibScalar
voiceSystemCountryCode = _VoiceSystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 3),
    _VoiceSystemCountryCode_Type()
)
voiceSystemCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemCountryCode.setStatus("mandatory")


class _VoiceSystemDialDigits_Type(Integer32):
    """Custom type voiceSystemDialDigits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_VoiceSystemDialDigits_Type.__name__ = "Integer32"
_VoiceSystemDialDigits_Object = MibScalar
voiceSystemDialDigits = _VoiceSystemDialDigits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 4),
    _VoiceSystemDialDigits_Type()
)
voiceSystemDialDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemDialDigits.setStatus("mandatory")


class _VoiceSystemVoiceRatesMin_Type(Integer32):
    """Custom type voiceSystemVoiceRatesMin based on Integer32"""
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
        *(("bps-32000", 3),
          ("bps-4800", 1),
          ("bps-64000", 4),
          ("bps-8000", 2))
    )


_VoiceSystemVoiceRatesMin_Type.__name__ = "Integer32"
_VoiceSystemVoiceRatesMin_Object = MibScalar
voiceSystemVoiceRatesMin = _VoiceSystemVoiceRatesMin_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 5),
    _VoiceSystemVoiceRatesMin_Type()
)
voiceSystemVoiceRatesMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemVoiceRatesMin.setStatus("mandatory")


class _VoiceSystemVoiceRatesMax_Type(Integer32):
    """Custom type voiceSystemVoiceRatesMax based on Integer32"""
    defaultValue = 4

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
        *(("bps-32000", 3),
          ("bps-4800", 1),
          ("bps-64000", 4),
          ("bps-8000", 2))
    )


_VoiceSystemVoiceRatesMax_Type.__name__ = "Integer32"
_VoiceSystemVoiceRatesMax_Object = MibScalar
voiceSystemVoiceRatesMax = _VoiceSystemVoiceRatesMax_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 6),
    _VoiceSystemVoiceRatesMax_Type()
)
voiceSystemVoiceRatesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemVoiceRatesMax.setStatus("mandatory")


class _VoiceSystemExtDialDigits_Type(Integer32):
    """Custom type voiceSystemExtDialDigits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VoiceSystemExtDialDigits_Type.__name__ = "Integer32"
_VoiceSystemExtDialDigits_Object = MibScalar
voiceSystemExtDialDigits = _VoiceSystemExtDialDigits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 7),
    _VoiceSystemExtDialDigits_Type()
)
voiceSystemExtDialDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSystemExtDialDigits.setStatus("mandatory")
_VoiceSpeedDialTable_Object = MibTable
voiceSpeedDialTable = _VoiceSpeedDialTable_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8)
)
if mibBuilder.loadTexts:
    voiceSpeedDialTable.setStatus("mandatory")
_VoiceSpeedDialEntry_Object = MibTableRow
voiceSpeedDialEntry = _VoiceSpeedDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8, 1)
)
voiceSpeedDialEntry.setIndexNames(
    (0, "NETLINK-SPECIFIC-MIB", "voiceSpeedDialDigits"),
)
if mibBuilder.loadTexts:
    voiceSpeedDialEntry.setStatus("mandatory")


class _VoiceSpeedDialDigits_Type(OctetString):
    """Custom type voiceSpeedDialDigits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VoiceSpeedDialDigits_Type.__name__ = "OctetString"
_VoiceSpeedDialDigits_Object = MibTableColumn
voiceSpeedDialDigits = _VoiceSpeedDialDigits_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8, 1, 1),
    _VoiceSpeedDialDigits_Type()
)
voiceSpeedDialDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceSpeedDialDigits.setStatus("mandatory")


class _VoiceSpeedDialLongDialMap_Type(OctetString):
    """Custom type voiceSpeedDialLongDialMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VoiceSpeedDialLongDialMap_Type.__name__ = "OctetString"
_VoiceSpeedDialLongDialMap_Object = MibTableColumn
voiceSpeedDialLongDialMap = _VoiceSpeedDialLongDialMap_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8, 1, 2),
    _VoiceSpeedDialLongDialMap_Type()
)
voiceSpeedDialLongDialMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSpeedDialLongDialMap.setStatus("mandatory")


class _VoiceSpeedDialExtDialStr_Type(OctetString):
    """Custom type voiceSpeedDialExtDialStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VoiceSpeedDialExtDialStr_Type.__name__ = "OctetString"
_VoiceSpeedDialExtDialStr_Object = MibTableColumn
voiceSpeedDialExtDialStr = _VoiceSpeedDialExtDialStr_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8, 1, 3),
    _VoiceSpeedDialExtDialStr_Type()
)
voiceSpeedDialExtDialStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSpeedDialExtDialStr.setStatus("mandatory")
_VoiceSpeedDialRowStatus_Type = RowStatus
_VoiceSpeedDialRowStatus_Object = MibTableColumn
voiceSpeedDialRowStatus = _VoiceSpeedDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 173, 7, 12, 8, 1, 4),
    _VoiceSpeedDialRowStatus_Type()
)
voiceSpeedDialRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceSpeedDialRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETLINK-SPECIFIC-MIB",
    **{"NlSubscriberAddress": NlSubscriberAddress,
       "snaDLC": snaDLC,
       "sdlc": sdlc,
       "sdlcLSGroup": sdlcLSGroup,
       "sdlcLSAdminTable": sdlcLSAdminTable,
       "sdlcLSAdminEntry": sdlcLSAdminEntry,
       "sdlcLSAddress": sdlcLSAddress,
       "netlink": netlink,
       "network": network,
       "netstat": netstat,
       "nsMaxNeigh": nsMaxNeigh,
       "nsThisNode": nsThisNode,
       "nsNodTable": nsNodTable,
       "nsEntry": nsEntry,
       "nsNodNum": nsNodNum,
       "nsStatus": nsStatus,
       "nsNumNeigh": nsNumNeigh,
       "nsNeighTable": nsNeighTable,
       "nsNeighEntry": nsNeighEntry,
       "nsNTNode": nsNTNode,
       "nsNTNeigh": nsNTNeigh,
       "nsNTNeighStat": nsNTNeighStat,
       "local": local,
       "node": node,
       "nodeCfgTable": nodeCfgTable,
       "nodeAlmTable": nodeAlmTable,
       "nodeSNMPGroup": nodeSNMPGroup,
       "nodeModel": nodeModel,
       "nodeTrapText": nodeTrapText,
       "nodeTrapAdrTable": nodeTrapAdrTable,
       "tpAdrEntry": tpAdrEntry,
       "tpAdrIdx": tpAdrIdx,
       "tpAddress": tpAddress,
       "tpAdrFlag": tpAdrFlag,
       "tpAdrSLev": tpAdrSLev,
       "nodeBagTable": nodeBagTable,
       "hwcard": hwcard,
       "rlpMaxProtos": rlpMaxProtos,
       "rlpConfigTable": rlpConfigTable,
       "rlpEntry": rlpEntry,
       "rlpIndex": rlpIndex,
       "rlpStatus": rlpStatus,
       "rlpMemorySize": rlpMemorySize,
       "rlpLIC1Type": rlpLIC1Type,
       "rlpLIC2Type": rlpLIC2Type,
       "rlpProtocol": rlpProtocol,
       "rlpGroupNumber": rlpGroupNumber,
       "rlpGroupResponsibility": rlpGroupResponsibility,
       "port": port,
       "portX25Group": portX25Group,
       "portPhyX25AdminTable": portPhyX25AdminTable,
       "portPhyX25AdminEntry": portPhyX25AdminEntry,
       "portPhyX25AdminConnector": portPhyX25AdminConnector,
       "portPhyX25AdminSpeed": portPhyX25AdminSpeed,
       "portPhyX25AdminGenerateClock": portPhyX25AdminGenerateClock,
       "portPhyX25AdminRcvClockFromDTE": portPhyX25AdminRcvClockFromDTE,
       "portPhyX25AdminDialOut": portPhyX25AdminDialOut,
       "portPhyX25AdminInactivityTimer": portPhyX25AdminInactivityTimer,
       "portPhyX25AdminDisconnectTimer": portPhyX25AdminDisconnectTimer,
       "portPhyX25AdminSetupTimer": portPhyX25AdminSetupTimer,
       "portPhyX25AdminTrunkFlag": portPhyX25AdminTrunkFlag,
       "portPhyX25AdminTrunkGroup": portPhyX25AdminTrunkGroup,
       "portPhyX25AdminRowStatus": portPhyX25AdminRowStatus,
       "portPhyX25OperTable": portPhyX25OperTable,
       "portPhyX25OperEntry": portPhyX25OperEntry,
       "portPhyX25OperConnector": portPhyX25OperConnector,
       "portPhyX25OperSpeed": portPhyX25OperSpeed,
       "portPhyX25OperGenerateClock": portPhyX25OperGenerateClock,
       "portPhyX25OperRcvClockFromDTE": portPhyX25OperRcvClockFromDTE,
       "portPhyX25OperDialOut": portPhyX25OperDialOut,
       "portPhyX25OperInactivityTimer": portPhyX25OperInactivityTimer,
       "portPhyX25OperDisconnectTimer": portPhyX25OperDisconnectTimer,
       "portPhyX25OperSetupTimer": portPhyX25OperSetupTimer,
       "portPhyX25OperTrunkFlag": portPhyX25OperTrunkFlag,
       "portPhyX25OperTrunkGroup": portPhyX25OperTrunkGroup,
       "portLogicalX25AdminTable": portLogicalX25AdminTable,
       "portLogicalX25AdminEntry": portLogicalX25AdminEntry,
       "portLogicalX25AdminFrDlci": portLogicalX25AdminFrDlci,
       "portLogicalX25AdminCxnPriority": portLogicalX25AdminCxnPriority,
       "portLogicalX25AdminRfc1490": portLogicalX25AdminRfc1490,
       "portLogicalX25AdminBAG": portLogicalX25AdminBAG,
       "portLogicalX25AdminRowStatus": portLogicalX25AdminRowStatus,
       "portLogicalX25OperTable": portLogicalX25OperTable,
       "portLogicalX25OperEntry": portLogicalX25OperEntry,
       "portLogicalX25OperFrDlci": portLogicalX25OperFrDlci,
       "portLogicalX25OperCxnPriority": portLogicalX25OperCxnPriority,
       "portLogicalX25OperRfc1490": portLogicalX25OperRfc1490,
       "portLogicalX25OperBAG": portLogicalX25OperBAG,
       "portX25AdminTable": portX25AdminTable,
       "portX25AdminEntry": portX25AdminEntry,
       "portX25AdminBlockedFlag": portX25AdminBlockedFlag,
       "portX25AdminFlowCtrlNeg": portX25AdminFlowCtrlNeg,
       "portX25AdminThruptClassNeg": portX25AdminThruptClassNeg,
       "portX25AdminLocChgPrev": portX25AdminLocChgPrev,
       "portX25AdminRevChgAccpt": portX25AdminRevChgAccpt,
       "portX25AdminFastSelAccpt": portX25AdminFastSelAccpt,
       "portX25AdminInCallBar": portX25AdminInCallBar,
       "portX25AdminOutCallBar": portX25AdminOutCallBar,
       "portX25AdminMaxPktSize": portX25AdminMaxPktSize,
       "portX25AdminDefPktSize": portX25AdminDefPktSize,
       "portX25AdminMaxWinSize": portX25AdminMaxWinSize,
       "portX25AdminDefWinSize": portX25AdminDefWinSize,
       "portX25AdminMaxThruptClass": portX25AdminMaxThruptClass,
       "portX25AdminCUGPref": portX25AdminCUGPref,
       "portX25AdminCUGIndex": portX25AdminCUGIndex,
       "portX25AdminCUGIncAccess": portX25AdminCUGIncAccess,
       "portX25AdminCUGOutAccess": portX25AdminCUGOutAccess,
       "portX25OperTable": portX25OperTable,
       "portX25OperEntry": portX25OperEntry,
       "portX25OperBlockedFlag": portX25OperBlockedFlag,
       "portX25OperFlowCtrlNeg": portX25OperFlowCtrlNeg,
       "portX25OperThruptClassNeg": portX25OperThruptClassNeg,
       "portX25OperLocChgPrev": portX25OperLocChgPrev,
       "portX25OperRevChgAccpt": portX25OperRevChgAccpt,
       "portX25OperFastSelAccpt": portX25OperFastSelAccpt,
       "portX25OperInCallBar": portX25OperInCallBar,
       "portX25OperOutCallBar": portX25OperOutCallBar,
       "portX25OperMaxPktSize": portX25OperMaxPktSize,
       "portX25OperDefPktSize": portX25OperDefPktSize,
       "portX25OperMaxWinSize": portX25OperMaxWinSize,
       "portX25OperDefWinSize": portX25OperDefWinSize,
       "portX25OperMaxThruptClass": portX25OperMaxThruptClass,
       "portX25OperCUGPref": portX25OperCUGPref,
       "portX25OperCUGIndex": portX25OperCUGIndex,
       "portX25OperCUGIncAccess": portX25OperCUGIncAccess,
       "portX25OperCUGOutAccess": portX25OperCUGOutAccess,
       "portFrGroup": portFrGroup,
       "portFrConfigTable": portFrConfigTable,
       "portFrEntry": portFrEntry,
       "portFrRlpIndex": portFrRlpIndex,
       "portFrPortIndex": portFrPortIndex,
       "portFrBlockedFlag": portFrBlockedFlag,
       "portFrMaxBytesPerFrame": portFrMaxBytesPerFrame,
       "portFrT392Timer": portFrT392Timer,
       "portFrOutgoingRateControl": portFrOutgoingRateControl,
       "portFrBandwidthAllocation": portFrBandwidthAllocation,
       "portFrConnector": portFrConnector,
       "portFrLogicalDCE": portFrLogicalDCE,
       "portFrGenClock": portFrGenClock,
       "portFrRcvClkFrmDTE": portFrRcvClkFrmDTE,
       "portFrLLM": portFrLLM,
       "portFrRowStatus": portFrRowStatus,
       "portFrSpeed": portFrSpeed,
       "portFrBackupUseOnly": portFrBackupUseOnly,
       "portDLCIConfigTable": portDLCIConfigTable,
       "portDLCIEntry": portDLCIEntry,
       "portDLCIRlpIndex": portDLCIRlpIndex,
       "portDLCIPortIndex": portDLCIPortIndex,
       "portDLCIIndex": portDLCIIndex,
       "portDLCIIncomingCIR": portDLCIIncomingCIR,
       "portDLCIOutgoingCIR": portDLCIOutgoingCIR,
       "portDLCIIncomingBc": portDLCIIncomingBc,
       "portDLCIOutgoingBc": portDLCIOutgoingBc,
       "portDLCIIncomingBe": portDLCIIncomingBe,
       "portDLCIOutgoingBe": portDLCIOutgoingBe,
       "portDLCIBecnRecoveryCnt": portDLCIBecnRecoveryCnt,
       "portDLCIPriority": portDLCIPriority,
       "portDLCIRowStatus": portDLCIRowStatus,
       "portDLCIBackupGroup": portDLCIBackupGroup,
       "portDLCIBackupProtEnb": portDLCIBackupProtEnb,
       "portFrBackupGroupTable": portFrBackupGroupTable,
       "portFrBackupEntry": portFrBackupEntry,
       "portFrBackupRLP": portFrBackupRLP,
       "portFrBackupPort": portFrBackupPort,
       "portFrBackupDLCI": portFrBackupDLCI,
       "portFrBackupGroup": portFrBackupGroup,
       "portFrBackupWaitTimer": portFrBackupWaitTimer,
       "portFrBackupProtEnab": portFrBackupProtEnab,
       "portFrBackupRowStatus": portFrBackupRowStatus,
       "portBsciGroup": portBsciGroup,
       "portBsciAdminTable": portBsciAdminTable,
       "portBsciAdminEntry": portBsciAdminEntry,
       "portBsciAdminBlockedFlag": portBsciAdminBlockedFlag,
       "portBsciAdminConnector": portBsciAdminConnector,
       "portBsciAdminSpeed": portBsciAdminSpeed,
       "portBsciAdminRetransmitInterval": portBsciAdminRetransmitInterval,
       "portBsciAdminMAXRetransmits": portBsciAdminMAXRetransmits,
       "portBsciAdminMaxBytesPerFrame": portBsciAdminMaxBytesPerFrame,
       "portBsciAdminGenerateClock": portBsciAdminGenerateClock,
       "portBsciAdminRcvClockFromDTE": portBsciAdminRcvClockFromDTE,
       "portBsciAdminPadType": portBsciAdminPadType,
       "portBsciAdminUseEBCDIC": portBsciAdminUseEBCDIC,
       "portBsciAdminCallInfoInRequestPacket": portBsciAdminCallInfoInRequestPacket,
       "portBsciAdminClearVCOnLastDeviceDown": portBsciAdminClearVCOnLastDeviceDown,
       "portBsciAdminTransTextSupported": portBsciAdminTransTextSupported,
       "portBsciAdminEndToEndAck": portBsciAdminEndToEndAck,
       "portBsciAdminFullDuplex": portBsciAdminFullDuplex,
       "portBsciAdminMultidrop": portBsciAdminMultidrop,
       "portBsciAdminSlowPollRetryCount": portBsciAdminSlowPollRetryCount,
       "portBsciAdminSlowPollRetryFreq": portBsciAdminSlowPollRetryFreq,
       "portBsciAdminStartSynchChars": portBsciAdminStartSynchChars,
       "portBsciAdminEndPadChars": portBsciAdminEndPadChars,
       "portBsciAdminPollInterval": portBsciAdminPollInterval,
       "portBsciAdminNoResponseTimer": portBsciAdminNoResponseTimer,
       "portBsciAdminNoResponseRetryCount": portBsciAdminNoResponseRetryCount,
       "portBsciAdminErrorRetransmitCount": portBsciAdminErrorRetransmitCount,
       "portBsciAdminNAKRetryCount": portBsciAdminNAKRetryCount,
       "portBsciAdminBlockCheck": portBsciAdminBlockCheck,
       "portBsciAdminDataMode": portBsciAdminDataMode,
       "portBsciAdminRowStatus": portBsciAdminRowStatus,
       "portBsciAdminAnswerNonConfigured": portBsciAdminAnswerNonConfigured,
       "portBsciAdminActivateConnectionWithoutPoll": portBsciAdminActivateConnectionWithoutPoll,
       "portBsciOperTable": portBsciOperTable,
       "portBsciOperEntry": portBsciOperEntry,
       "portBsciOperBlockedFlag": portBsciOperBlockedFlag,
       "portBsciOperConnector": portBsciOperConnector,
       "portBsciOperSpeed": portBsciOperSpeed,
       "portBsciOperRetransmitInterval": portBsciOperRetransmitInterval,
       "portBsciOperMAXRetransmits": portBsciOperMAXRetransmits,
       "portBsciOperMaxBytesPerFrame": portBsciOperMaxBytesPerFrame,
       "portBsciOperGenerateClock": portBsciOperGenerateClock,
       "portBsciOperRcvClockFromDTE": portBsciOperRcvClockFromDTE,
       "portBsciOperPadType": portBsciOperPadType,
       "portBsciOperUseEBCDIC": portBsciOperUseEBCDIC,
       "portBsciOperCallInfoInRequestPacket": portBsciOperCallInfoInRequestPacket,
       "portBsciOperClearVCOnLastDeviceDown": portBsciOperClearVCOnLastDeviceDown,
       "portBsciOperTransTextSupported": portBsciOperTransTextSupported,
       "portBsciOperEndToEndAck": portBsciOperEndToEndAck,
       "portBsciOperFullDuplex": portBsciOperFullDuplex,
       "portBsciOperMultidrop": portBsciOperMultidrop,
       "portBsciOperSlowPollRetryCount": portBsciOperSlowPollRetryCount,
       "portBsciOperSlowPollRetryFreq": portBsciOperSlowPollRetryFreq,
       "portBsciOperStartSynchChars": portBsciOperStartSynchChars,
       "portBsciOperEndPadChars": portBsciOperEndPadChars,
       "portBsciOperPollInterval": portBsciOperPollInterval,
       "portBsciOperNoResponseTimer": portBsciOperNoResponseTimer,
       "portBsciOperNoResponseRetryCount": portBsciOperNoResponseRetryCount,
       "portBsciOperErrorRetransmitCount": portBsciOperErrorRetransmitCount,
       "portBsciOperNAKRetryCount": portBsciOperNAKRetryCount,
       "portBsciOperBlockCheck": portBsciOperBlockCheck,
       "portBsciOperDataMode": portBsciOperDataMode,
       "portBsciOperAnswerNonConfigured": portBsciOperAnswerNonConfigured,
       "portBsciOperActivateConnectionWithoutPoll": portBsciOperActivateConnectionWithoutPoll,
       "bsciSubscrAdminTable": bsciSubscrAdminTable,
       "bsciSubscrAdminEntry": bsciSubscrAdminEntry,
       "bsciSubscrAdminSequence": bsciSubscrAdminSequence,
       "bsciSubscrAdminLocalID": bsciSubscrAdminLocalID,
       "bsciSubscrAdminRemoteID": bsciSubscrAdminRemoteID,
       "bsciSubscrAdminAutocall": bsciSubscrAdminAutocall,
       "bsciSubscrAdminAutocallRtyTimer": bsciSubscrAdminAutocallRtyTimer,
       "bsciSubscrAdminAutocallMaxRtry": bsciSubscrAdminAutocallMaxRtry,
       "bsciSubscrAdminConnectionID": bsciSubscrAdminConnectionID,
       "bsciSubscrAdminRowStatus": bsciSubscrAdminRowStatus,
       "bsciSubscrOperTable": bsciSubscrOperTable,
       "bsciSubscrOperEntry": bsciSubscrOperEntry,
       "bsciSubscrOperSequence": bsciSubscrOperSequence,
       "bsciSubscrOperLocalID": bsciSubscrOperLocalID,
       "bsciSubscrOperRemoteID": bsciSubscrOperRemoteID,
       "bsciSubscrOperAutocall": bsciSubscrOperAutocall,
       "bsciSubscrOperAutocallRtyTimer": bsciSubscrOperAutocallRtyTimer,
       "bsciSubscrOperAutocallMaxRtry": bsciSubscrOperAutocallMaxRtry,
       "bsciSubscrOperConnectionID": bsciSubscrOperConnectionID,
       "bsciDevAdminTable": bsciDevAdminTable,
       "bsciDevAdminEntry": bsciDevAdminEntry,
       "bsciDevAdminControlUnitID": bsciDevAdminControlUnitID,
       "bsciDevAdminDeviceUnitID": bsciDevAdminDeviceUnitID,
       "bsciDevAdminConnectionID": bsciDevAdminConnectionID,
       "bsciDevAdminSingleUserVC": bsciDevAdminSingleUserVC,
       "bsciDevAdminTransTextSupported": bsciDevAdminTransTextSupported,
       "bsciDevAdminPrinterAttached": bsciDevAdminPrinterAttached,
       "bsciDevAdminRowStatus": bsciDevAdminRowStatus,
       "bsciDevAdminDisableStatusRequest": bsciDevAdminDisableStatusRequest,
       "bsciDevOperTable": bsciDevOperTable,
       "bsciDevOperEntry": bsciDevOperEntry,
       "bsciDevOperControlUnitID": bsciDevOperControlUnitID,
       "bsciDevOperDeviceUnitID": bsciDevOperDeviceUnitID,
       "bsciDevOperConnectionID": bsciDevOperConnectionID,
       "bsciDevOperSingleUserVC": bsciDevOperSingleUserVC,
       "bsciDevOperTransTextSupported": bsciDevOperTransTextSupported,
       "bsciDevOperPrinterAttached": bsciDevOperPrinterAttached,
       "bsciDevOperDisableStatusRequest": bsciDevOperDisableStatusRequest,
       "portSdlcGroup": portSdlcGroup,
       "portSdlcAdminTable": portSdlcAdminTable,
       "portSdlcAdminEntry": portSdlcAdminEntry,
       "portSdlcAdminCommit": portSdlcAdminCommit,
       "portSdlcAdminMAXRetries": portSdlcAdminMAXRetries,
       "portSdlcAdminMAXOut": portSdlcAdminMAXOut,
       "portSdlcAdminPadType": portSdlcAdminPadType,
       "portSdlcAdminGenerateClock": portSdlcAdminGenerateClock,
       "portSdlcAdminRcvClockFromDTE": portSdlcAdminRcvClockFromDTE,
       "portSdlcAdminNrz": portSdlcAdminNrz,
       "portSdlcAdminPacketSize": portSdlcAdminPacketSize,
       "portSdlcAdminDisableRequestDisconnect": portSdlcAdminDisableRequestDisconnect,
       "portSdlcAdminLPDASupport": portSdlcAdminLPDASupport,
       "portSdlcAdminConnector": portSdlcAdminConnector,
       "portSdlcAdminSpeed": portSdlcAdminSpeed,
       "portSdlcAdminRowStatus": portSdlcAdminRowStatus,
       "portSdlcAdminIdleFillChar": portSdlcAdminIdleFillChar,
       "portSdlcAdminInactivityTimer": portSdlcAdminInactivityTimer,
       "portSdlcAdminL1Duplex": portSdlcAdminL1Duplex,
       "portSdlcOperTable": portSdlcOperTable,
       "portSdlcOperEntry": portSdlcOperEntry,
       "portSdlcOperCommit": portSdlcOperCommit,
       "portSdlcOperMAXRetries": portSdlcOperMAXRetries,
       "portSdlcOperMAXOut": portSdlcOperMAXOut,
       "portSdlcOperPadType": portSdlcOperPadType,
       "portSdlcOperGenerateClock": portSdlcOperGenerateClock,
       "portSdlcOperRcvClockFromDTE": portSdlcOperRcvClockFromDTE,
       "portSdlcOperNrz": portSdlcOperNrz,
       "portSdlcOperPacketSize": portSdlcOperPacketSize,
       "portSdlcOperDisableRequestDisconnect": portSdlcOperDisableRequestDisconnect,
       "portSdlcOperLPDASupport": portSdlcOperLPDASupport,
       "portSdlcOperConnector": portSdlcOperConnector,
       "portSdlcOperSpeed": portSdlcOperSpeed,
       "portSdlcOperIdleFillChar": portSdlcOperIdleFillChar,
       "portSdlcOperInactivityTimer": portSdlcOperInactivityTimer,
       "portSdlcOperL1Duplex": portSdlcOperL1Duplex,
       "lSSdlcAdminTable": lSSdlcAdminTable,
       "lSSdlcAdminEntry": lSSdlcAdminEntry,
       "lSSdlcAdminLocalSub": lSSdlcAdminLocalSub,
       "lSSdlcAdminRemoteSub": lSSdlcAdminRemoteSub,
       "lSSdlcAdminAutoCall": lSSdlcAdminAutoCall,
       "lSSdlcAdminRetryTime": lSSdlcAdminRetryTime,
       "lSSdlcAdminRetryCount": lSSdlcAdminRetryCount,
       "lSSdlcAdminLlc2Conversion": lSSdlcAdminLlc2Conversion,
       "lSSdlcAdminLPDAResourceID": lSSdlcAdminLPDAResourceID,
       "lSSdlcAdminRowStatus": lSSdlcAdminRowStatus,
       "lSSdlcAdminL2DatMode": lSSdlcAdminL2DatMode,
       "lSSdlcOperTable": lSSdlcOperTable,
       "lSSdlcOperEntry": lSSdlcOperEntry,
       "lSSdlcOperLocalSub": lSSdlcOperLocalSub,
       "lSSdlcOperRemoteSub": lSSdlcOperRemoteSub,
       "lSSdlcOperAutoCall": lSSdlcOperAutoCall,
       "lSSdlcOperRetryTime": lSSdlcOperRetryTime,
       "lSSdlcOperRetryCount": lSSdlcOperRetryCount,
       "lSSdlcOperLlc2Conversion": lSSdlcOperLlc2Conversion,
       "lSSdlcOperLPDAResourceID": lSSdlcOperLPDAResourceID,
       "lSSdlcOperL2DatMode": lSSdlcOperL2DatMode,
       "lSSdlcLlc2AdminTable": lSSdlcLlc2AdminTable,
       "lSSdlcLlc2AdminEntry": lSSdlcLlc2AdminEntry,
       "lSSdlcLlc2AdminLocalSap": lSSdlcLlc2AdminLocalSap,
       "lSSdlcLlc2AdminLocalMac": lSSdlcLlc2AdminLocalMac,
       "lSSdlcLlc2AdminIdblk": lSSdlcLlc2AdminIdblk,
       "lSSdlcLlc2AdminIdnum": lSSdlcLlc2AdminIdnum,
       "lSSdlcLlc2AdminLanTi": lSSdlcLlc2AdminLanTi,
       "lSSdlcLlc2AdminLanT1": lSSdlcLlc2AdminLanT1,
       "lSSdlcLlc2AdminLanT2": lSSdlcLlc2AdminLanT2,
       "lSSdlcLlc2AdminLanN2": lSSdlcLlc2AdminLanN2,
       "lSSdlcLlc2AdminLanN3": lSSdlcLlc2AdminLanN3,
       "lSSdlcLlc2AdminLanTw": lSSdlcLlc2AdminLanTw,
       "lSSdlcLlc2AdminBAG": lSSdlcLlc2AdminBAG,
       "lSSdlcLlc2AdminPriority": lSSdlcLlc2AdminPriority,
       "lSSdlcLlc2AdminRowStatus": lSSdlcLlc2AdminRowStatus,
       "lSSdlcLlc2AdminSuppressXID": lSSdlcLlc2AdminSuppressXID,
       "lSSdlcLlc2OperTable": lSSdlcLlc2OperTable,
       "lSSdlcLlc2OperEntry": lSSdlcLlc2OperEntry,
       "lSSdlcLlc2OperLocalSap": lSSdlcLlc2OperLocalSap,
       "lSSdlcLlc2OperLocalMac": lSSdlcLlc2OperLocalMac,
       "lSSdlcLlc2OperIdblk": lSSdlcLlc2OperIdblk,
       "lSSdlcLlc2OperIdnum": lSSdlcLlc2OperIdnum,
       "lSSdlcLlc2OperLanTi": lSSdlcLlc2OperLanTi,
       "lSSdlcLlc2OperLanT1": lSSdlcLlc2OperLanT1,
       "lSSdlcLlc2OperLanT2": lSSdlcLlc2OperLanT2,
       "lSSdlcLlc2OperLanN2": lSSdlcLlc2OperLanN2,
       "lSSdlcLlc2OperLanN3": lSSdlcLlc2OperLanN3,
       "lSSdlcLlc2OperLanTw": lSSdlcLlc2OperLanTw,
       "lSSdlcLlc2OperBAG": lSSdlcLlc2OperBAG,
       "lSSdlcLlc2OperPriority": lSSdlcLlc2OperPriority,
       "lSSdlcLlc2OperSuppressXID": lSSdlcLlc2OperSuppressXID,
       "portT1Group": portT1Group,
       "portT1AdminTable": portT1AdminTable,
       "portT1AdminEntry": portT1AdminEntry,
       "portT1AdminBlockedPortFlag": portT1AdminBlockedPortFlag,
       "portT1AdminGenerateClock": portT1AdminGenerateClock,
       "portT1AdminFramingMode": portT1AdminFramingMode,
       "portT1AdminFrameModelSelect": portT1AdminFrameModelSelect,
       "portT1AdminLineEncoding": portT1AdminLineEncoding,
       "portT1AdminLineBuildOut": portT1AdminLineBuildOut,
       "portT1AdminRowStatus": portT1AdminRowStatus,
       "portT1AdminProtocolFraming": portT1AdminProtocolFraming,
       "portT1AdminNRZI": portT1AdminNRZI,
       "portT1OperTable": portT1OperTable,
       "portT1OperEntry": portT1OperEntry,
       "portT1OperBlockedPortFlag": portT1OperBlockedPortFlag,
       "portT1OperGenerateClock": portT1OperGenerateClock,
       "portT1OperFramingMode": portT1OperFramingMode,
       "portT1OperFrameModelSelect": portT1OperFrameModelSelect,
       "portT1OperLineEncoding": portT1OperLineEncoding,
       "portT1OperLineBuildOut": portT1OperLineBuildOut,
       "portT1OperProtocolFraming": portT1OperProtocolFraming,
       "portT1OperNRZI": portT1OperNRZI,
       "portVoiceGroup": portVoiceGroup,
       "portVoiceAdminTable": portVoiceAdminTable,
       "portVoiceAdminEntry": portVoiceAdminEntry,
       "portVoiceAdminRlpIndex": portVoiceAdminRlpIndex,
       "portVoiceAdminPortIndex": portVoiceAdminPortIndex,
       "portVoiceAdminBlockedFlag": portVoiceAdminBlockedFlag,
       "portVoiceAdminSpeed": portVoiceAdminSpeed,
       "portVoiceAdminDTMF": portVoiceAdminDTMF,
       "portVoiceAdminInterface": portVoiceAdminInterface,
       "portVoiceAdminTETimer": portVoiceAdminTETimer,
       "portVoiceAdminLevelIn": portVoiceAdminLevelIn,
       "portVoiceAdminLevelOut": portVoiceAdminLevelOut,
       "portVoiceAdminCallTimer": portVoiceAdminCallTimer,
       "portVoiceAdminHuntGroup": portVoiceAdminHuntGroup,
       "portVoiceAdminLongDialPrefix": portVoiceAdminLongDialPrefix,
       "portVoiceAdminSLTTimeout": portVoiceAdminSLTTimeout,
       "portVoiceAdminLinkDownBusy": portVoiceAdminLinkDownBusy,
       "portVoiceAdminFaxSupported": portVoiceAdminFaxSupported,
       "portVoiceAdminTelephonyType": portVoiceAdminTelephonyType,
       "portVoiceAdminJitter": portVoiceAdminJitter,
       "portVoiceAdminSampleDelay": portVoiceAdminSampleDelay,
       "portVoiceAdminDialTimer": portVoiceAdminDialTimer,
       "portVoiceAdminAutoDial": portVoiceAdminAutoDial,
       "portVoiceAdminSuppression": portVoiceAdminSuppression,
       "portVoiceAdminAutoDialNumber": portVoiceAdminAutoDialNumber,
       "portVoiceAdminAutoPoll": portVoiceAdminAutoPoll,
       "portVoiceAdminAutoPollTimer": portVoiceAdminAutoPollTimer,
       "portVoiceAdminExtDigitsSource": portVoiceAdminExtDigitsSource,
       "portVoiceAdminNumDigitsDelete": portVoiceAdminNumDigitsDelete,
       "portVoiceAdminForwardDelay": portVoiceAdminForwardDelay,
       "portVoiceAdminForwardedType": portVoiceAdminForwardedType,
       "portVoiceAdminForwardedDigits": portVoiceAdminForwardedDigits,
       "portVoiceAdminMakeRatio": portVoiceAdminMakeRatio,
       "portVoiceAdminBreakRatio": portVoiceAdminBreakRatio,
       "portVoiceAdminDTMFOnDuration": portVoiceAdminDTMFOnDuration,
       "portVoiceAdminDTMFOffDuration": portVoiceAdminDTMFOffDuration,
       "portVoiceAdminToneType": portVoiceAdminToneType,
       "portVoiceAdminRowStatus": portVoiceAdminRowStatus,
       "portVoiceOperTable": portVoiceOperTable,
       "portVoiceOperEntry": portVoiceOperEntry,
       "portVoiceOperRlpIndex": portVoiceOperRlpIndex,
       "portVoiceOperPortIndex": portVoiceOperPortIndex,
       "portVoiceOperBlockedFlag": portVoiceOperBlockedFlag,
       "portVoiceOperSpeed": portVoiceOperSpeed,
       "portVoiceOperDTMF": portVoiceOperDTMF,
       "portVoiceOperInterface": portVoiceOperInterface,
       "portVoiceOperTETimer": portVoiceOperTETimer,
       "portVoiceOperLevelIn": portVoiceOperLevelIn,
       "portVoiceOperLevelOut": portVoiceOperLevelOut,
       "portVoiceOperCallTimer": portVoiceOperCallTimer,
       "portVoiceOperHuntGroup": portVoiceOperHuntGroup,
       "portVoiceOperLongDialPrefix": portVoiceOperLongDialPrefix,
       "portVoiceOperSLTTimeout": portVoiceOperSLTTimeout,
       "portVoiceOperLinkDownBusy": portVoiceOperLinkDownBusy,
       "portVoiceOperFaxSupported": portVoiceOperFaxSupported,
       "portVoiceOperTelephonyType": portVoiceOperTelephonyType,
       "portVoiceOperJitter": portVoiceOperJitter,
       "portVoiceOperSampleDelay": portVoiceOperSampleDelay,
       "portVoiceOperDialTimer": portVoiceOperDialTimer,
       "portVoiceOperAutoDial": portVoiceOperAutoDial,
       "portVoiceOperSuppression": portVoiceOperSuppression,
       "portVoiceOperAutoDialNumber": portVoiceOperAutoDialNumber,
       "portVoiceOperAutoPoll": portVoiceOperAutoPoll,
       "portVoiceOperAutoPollTimer": portVoiceOperAutoPollTimer,
       "portVoiceOperExtDigitsSource": portVoiceOperExtDigitsSource,
       "portVoiceOperNumDigitsDelete": portVoiceOperNumDigitsDelete,
       "portVoiceOperForwardDelay": portVoiceOperForwardDelay,
       "portVoiceOperForwardedType": portVoiceOperForwardedType,
       "portVoiceOperForwardedDigits": portVoiceOperForwardedDigits,
       "portVoiceOperMakeRatio": portVoiceOperMakeRatio,
       "portVoiceOperBreakRatio": portVoiceOperBreakRatio,
       "portVoiceOperDTMFOnDuration": portVoiceOperDTMFOnDuration,
       "portVoiceOperDTMFOffDuration": portVoiceOperDTMFOffDuration,
       "portVoiceOperToneType": portVoiceOperToneType,
       "nlInterfaces": nlInterfaces,
       "nlIfTable": nlIfTable,
       "nlIfEntry": nlIfEntry,
       "nlIfRlp": nlIfRlp,
       "nlIfPort": nlIfPort,
       "nlIfType": nlIfType,
       "nlIfIndex": nlIfIndex,
       "nlIfTableIndex": nlIfTableIndex,
       "nlIfTableOid": nlIfTableOid,
       "nlIfConnectorType": nlIfConnectorType,
       "nlIfPortStatus": nlIfPortStatus,
       "nlIfPhyPort": nlIfPhyPort,
       "nlIfLlc2Interfaces": nlIfLlc2Interfaces,
       "nlIfLlc2LANTable": nlIfLlc2LANTable,
       "nlIfLlc2LANEntry": nlIfLlc2LANEntry,
       "nlIfLlc2LANRlp": nlIfLlc2LANRlp,
       "nlIfLlc2LANPort": nlIfLlc2LANPort,
       "nlIfLlc2LANType": nlIfLlc2LANType,
       "nlIfLlc2LANCard": nlIfLlc2LANCard,
       "nlIfLlc2LANID": nlIfLlc2LANID,
       "nlIfLlc2LANInterface": nlIfLlc2LANInterface,
       "nlIfLlc2LANRowStatus": nlIfLlc2LANRowStatus,
       "nlIfLlc2LANPriority": nlIfLlc2LANPriority,
       "nlIfLlc2LANBlockedPortFlag": nlIfLlc2LANBlockedPortFlag,
       "nlIfLlc2FrTable": nlIfLlc2FrTable,
       "nlIfLlc2FrEntry": nlIfLlc2FrEntry,
       "nlIfLlc2FrRlp": nlIfLlc2FrRlp,
       "nlIfLlc2FrPort": nlIfLlc2FrPort,
       "nlIfLlc2FrDLCI": nlIfLlc2FrDLCI,
       "nlIfLlc2FrFormat": nlIfLlc2FrFormat,
       "nlIfLlc2FrPriority": nlIfLlc2FrPriority,
       "nlIfLlc2FrBAG": nlIfLlc2FrBAG,
       "nlIfLlc2FrHostMACAddress": nlIfLlc2FrHostMACAddress,
       "nlIfLlc2FrSessionType": nlIfLlc2FrSessionType,
       "nlIfLlc2FrLANID": nlIfLlc2FrLANID,
       "nlIfLlc2FrInterface": nlIfLlc2FrInterface,
       "nlIfLlc2FrRowStatus": nlIfLlc2FrRowStatus,
       "nlIfLlc2FrBlockedPortFlag": nlIfLlc2FrBlockedPortFlag,
       "ipxConfig": ipxConfig,
       "ipxConfigRouting": ipxConfigRouting,
       "ipxStaticRouteConfigTable": ipxStaticRouteConfigTable,
       "ipxStaticRouteConfigEntry": ipxStaticRouteConfigEntry,
       "ipxStaticRouteConfigCircIndex": ipxStaticRouteConfigCircIndex,
       "ipxStaticRouteConfigNetNum": ipxStaticRouteConfigNetNum,
       "ipxStaticRouteConfigRouter": ipxStaticRouteConfigRouter,
       "ipxStaticRouteConfigRowStatus": ipxStaticRouteConfigRowStatus,
       "ipxServConfigTable": ipxServConfigTable,
       "ipxServConfigEntry": ipxServConfigEntry,
       "ipxServConfigServiceType": ipxServConfigServiceType,
       "ipxServConfigServName": ipxServConfigServName,
       "ipxServConfigServNetworkAddress": ipxServConfigServNetworkAddress,
       "ipxServConfigServNodeAddress": ipxServConfigServNodeAddress,
       "ipxServConfigServSocketNumber": ipxServConfigServSocketNumber,
       "ipxServConfigInterveningNetworks": ipxServConfigInterveningNetworks,
       "ipxServConfigGatewayAddress": ipxServConfigGatewayAddress,
       "ipxServConfigInterface": ipxServConfigInterface,
       "ipxServConfigRowStatus": ipxServConfigRowStatus,
       "ipxConfigInterface": ipxConfigInterface,
       "ipxInterfaceTable": ipxInterfaceTable,
       "ipxInterfaceEntry": ipxInterfaceEntry,
       "ipxInterfaceNumber": ipxInterfaceNumber,
       "ipxInterfaceBlockedPortFlag": ipxInterfaceBlockedPortFlag,
       "ipxInterfaceType": ipxInterfaceType,
       "ipxInterfaceFrameType": ipxInterfaceFrameType,
       "ipxInterfaceMaxTransUnit": ipxInterfaceMaxTransUnit,
       "ipxInterfaceNetworkAddress": ipxInterfaceNetworkAddress,
       "ipxInterfaceBandwidthAllocGroup": ipxInterfaceBandwidthAllocGroup,
       "ipxInterfacePortDiagEnabled": ipxInterfacePortDiagEnabled,
       "ipxInterfaceNetBIOSEnabled": ipxInterfaceNetBIOSEnabled,
       "ipxInterfaceNetBIOSHops": ipxInterfaceNetBIOSHops,
       "ipxInterfacePeriodicRIPEnabled": ipxInterfacePeriodicRIPEnabled,
       "ipxInterfacePeriodicRIPTimer": ipxInterfacePeriodicRIPTimer,
       "ipxInterfacePeriodicSAPEnabled": ipxInterfacePeriodicSAPEnabled,
       "ipxInterfacePeriodicSAPTimer": ipxInterfacePeriodicSAPTimer,
       "ipxInterfaceRIPEnabled": ipxInterfaceRIPEnabled,
       "ipxInterfaceRIPAgeTimer": ipxInterfaceRIPAgeTimer,
       "ipxInterfaceRIPMaxSize": ipxInterfaceRIPMaxSize,
       "ipxInterfaceSAPEnabled": ipxInterfaceSAPEnabled,
       "ipxInterfaceSAPAgeTimer": ipxInterfaceSAPAgeTimer,
       "ipxInterfaceTransportTime": ipxInterfaceTransportTime,
       "ipxInterfaceSerializationEnabled": ipxInterfaceSerializationEnabled,
       "ipxInterfaceWatchdogSpoofingEnabled": ipxInterfaceWatchdogSpoofingEnabled,
       "ipxInterfaceLanCardNumber": ipxInterfaceLanCardNumber,
       "ipxInterfaceWanEnabled": ipxInterfaceWanEnabled,
       "ipxInterfaceSourceSubscriber": ipxInterfaceSourceSubscriber,
       "ipxInterfaceDestinationSubscriber": ipxInterfaceDestinationSubscriber,
       "ipxInterfaceSVCRetryTimer": ipxInterfaceSVCRetryTimer,
       "ipxInterfaceSVCIdleTimer": ipxInterfaceSVCIdleTimer,
       "ipxInterfaceMaxVC": ipxInterfaceMaxVC,
       "ipxInterfacePVCConnection": ipxInterfacePVCConnection,
       "ipxInterfaceSourceCard": ipxInterfaceSourceCard,
       "ipxInterfaceSourcePort": ipxInterfaceSourcePort,
       "ipxInterfaceSourceDLCI": ipxInterfaceSourceDLCI,
       "ipxInterfaceRowStatus": ipxInterfaceRowStatus,
       "ipxConfigNodeDefault": ipxConfigNodeDefault,
       "ipxNodeDefaultConfigNetworkAddress": ipxNodeDefaultConfigNetworkAddress,
       "ipxNodeDefaultConfigRIPSAPGap": ipxNodeDefaultConfigRIPSAPGap,
       "ipxNodeDefaultConfigRouterName": ipxNodeDefaultConfigRouterName,
       "nlIfIpInterfaces": nlIfIpInterfaces,
       "nlIfIpTable": nlIfIpTable,
       "nlIfIpEntry": nlIfIpEntry,
       "nlIfIpInterface": nlIfIpInterface,
       "nlIfIpMtu": nlIfIpMtu,
       "nlIfIpNetworkMask": nlIfIpNetworkMask,
       "nlIfIpRouteMetric": nlIfIpRouteMetric,
       "nlIfIpICMPAddRoutes": nlIfIpICMPAddRoutes,
       "nlIfIpRIPDeltaUpdates": nlIfIpRIPDeltaUpdates,
       "nlIfIpRIPFullUpdates": nlIfIpRIPFullUpdates,
       "nlIfIpPriority": nlIfIpPriority,
       "nlIfIpBAG": nlIfIpBAG,
       "nlIfIpType": nlIfIpType,
       "nlIfIpSourceAddress": nlIfIpSourceAddress,
       "nlIfIpDestAddress": nlIfIpDestAddress,
       "nlIfIpBroadcastAddress": nlIfIpBroadcastAddress,
       "nlIfIpLANCard": nlIfIpLANCard,
       "nlIfIpSourceSub": nlIfIpSourceSub,
       "nlIfIpDestSub": nlIfIpDestSub,
       "nlIfIpSVCRetryTimer": nlIfIpSVCRetryTimer,
       "nlIfIpSVCIdleTimer": nlIfIpSVCIdleTimer,
       "nlIfIpMaxSVC": nlIfIpMaxSVC,
       "nlIfIpPVCConnection": nlIfIpPVCConnection,
       "nlIfIpSourceRlp": nlIfIpSourceRlp,
       "nlIfIpSourcePort": nlIfIpSourcePort,
       "nlIfIpSourceDLCI": nlIfIpSourceDLCI,
       "nlIfIpRIPSupport": nlIfIpRIPSupport,
       "nlIfIpInverseARP": nlIfIpInverseARP,
       "nlIfIpProxyARP": nlIfIpProxyARP,
       "nlIfIpUnnumberedIf": nlIfIpUnnumberedIf,
       "nlIfIpRowStatus": nlIfIpRowStatus,
       "nlIfIpSecondaryAddrTable": nlIfIpSecondaryAddrTable,
       "nlIfIpSecondaryAddrEntry": nlIfIpSecondaryAddrEntry,
       "nlIfIpSecondaryAddrSequence": nlIfIpSecondaryAddrSequence,
       "nlIfIpSecondaryAddrNetworkMask": nlIfIpSecondaryAddrNetworkMask,
       "nlIfIpSecondaryAddrRouteMetric": nlIfIpSecondaryAddrRouteMetric,
       "nlIfIpSecondaryAddrSourceAddress": nlIfIpSecondaryAddrSourceAddress,
       "nlIfIpSecondaryAddrBroadcastAddress": nlIfIpSecondaryAddrBroadcastAddress,
       "nlIfIpSecondaryAddrRIPSupport": nlIfIpSecondaryAddrRIPSupport,
       "nlIfIpSecondaryAddrRowStatus": nlIfIpSecondaryAddrRowStatus,
       "nlIfVoiceInterfaces": nlIfVoiceInterfaces,
       "nlIfVoiceTable": nlIfVoiceTable,
       "nlIfVoiceEntry": nlIfVoiceEntry,
       "nlIfVoiceInterface": nlIfVoiceInterface,
       "nlIfVoicePeerNodeType": nlIfVoicePeerNodeType,
       "nlIfVoicePeerNodeNumber": nlIfVoicePeerNodeNumber,
       "nlIfVoicePeerNodePort": nlIfVoicePeerNodePort,
       "nlIfVoiceLocalNodeNumber": nlIfVoiceLocalNodeNumber,
       "nlIfVoiceLocalNodePort": nlIfVoiceLocalNodePort,
       "nlIfVoiceFrameRelayRlp": nlIfVoiceFrameRelayRlp,
       "nlIfVoiceFrameRelayPort": nlIfVoiceFrameRelayPort,
       "nlIfVoiceFrameRelayDLCI": nlIfVoiceFrameRelayDLCI,
       "nlIfVoiceEnableFragment": nlIfVoiceEnableFragment,
       "nlIfVoiceRowStatus": nlIfVoiceRowStatus,
       "subscriber": subscriber,
       "nlLocalSubscriberTable": nlLocalSubscriberTable,
       "nlLocalSubscriberEntry": nlLocalSubscriberEntry,
       "nlLocalSubscriberId": nlLocalSubscriberId,
       "nlLocalSubscriberName": nlLocalSubscriberName,
       "nlLocalSubscriberAlgorithm": nlLocalSubscriberAlgorithm,
       "nlLocalSubscriberSystematicRedirect": nlLocalSubscriberSystematicRedirect,
       "nlLocalSubscriberRedirectBusy": nlLocalSubscriberRedirectBusy,
       "nlLocalSubscriberRedirectOO": nlLocalSubscriberRedirectOO,
       "nlLocalSubscriberPriority": nlLocalSubscriberPriority,
       "nlLocalSubscriberRowStatus": nlLocalSubscriberRowStatus,
       "nlLocalSubscriberRouteTable": nlLocalSubscriberRouteTable,
       "nlLocalSubscriberRouteEntry": nlLocalSubscriberRouteEntry,
       "nlLocalSubscriberRouteIndex": nlLocalSubscriberRouteIndex,
       "nlLocalSubscriberRouteConf": nlLocalSubscriberRouteConf,
       "nlLocalSubscriberRouteLP": nlLocalSubscriberRouteLP,
       "nlLocalSubscriberRoutePort": nlLocalSubscriberRoutePort,
       "nlLocalSubscriberRouteRowStatus": nlLocalSubscriberRouteRowStatus,
       "nlLocalSubscriberRedirTable": nlLocalSubscriberRedirTable,
       "nlLocalSubscriberRedirEntry": nlLocalSubscriberRedirEntry,
       "nlLocalSubscriberRedirIndex": nlLocalSubscriberRedirIndex,
       "nlLocalSubscriberRedirAddr": nlLocalSubscriberRedirAddr,
       "nlLocalSubscriberRedirRowStatus": nlLocalSubscriberRedirRowStatus,
       "llc2": llc2,
       "nlLlc2HostTable": nlLlc2HostTable,
       "nlLlc2HostEntry": nlLlc2HostEntry,
       "nlLlc2HostIndex": nlLlc2HostIndex,
       "nlLlc2HostMACAddress": nlLlc2HostMACAddress,
       "nlLlc2HostSessionType": nlLlc2HostSessionType,
       "nlLlc2HostT1ReplyTimer": nlLlc2HostT1ReplyTimer,
       "nlLlc2HostT2RecvAckTimer": nlLlc2HostT2RecvAckTimer,
       "nlLlc2HostTiInactivityTimer": nlLlc2HostTiInactivityTimer,
       "nlLlc2HostN3NumberLPDUs": nlLlc2HostN3NumberLPDUs,
       "nlLlc2HostTwNumberOutstanding": nlLlc2HostTwNumberOutstanding,
       "nlLlc2HostN2ExpiredT1LPDUCount": nlLlc2HostN2ExpiredT1LPDUCount,
       "nlLlc2HostPriority": nlLlc2HostPriority,
       "nlLlc2HostBAG": nlLlc2HostBAG,
       "nlLlc2HostRoutingSubscriberId": nlLlc2HostRoutingSubscriberId,
       "nlLlc2HostSrcMACAddressMask": nlLlc2HostSrcMACAddressMask,
       "nlLlc2HostAccess": nlLlc2HostAccess,
       "nlLlc2HostRowStatus": nlLlc2HostRowStatus,
       "nlLlc2HostInterface": nlLlc2HostInterface,
       "nlLlc2HostGroup": nlLlc2HostGroup,
       "nlLlc2TermConnectionTable": nlLlc2TermConnectionTable,
       "nlLlc2TermConnectionEntry": nlLlc2TermConnectionEntry,
       "nlLlc2TermConnectionSequence": nlLlc2TermConnectionSequence,
       "nlLlc2TermConnectionHSAP": nlLlc2TermConnectionHSAP,
       "nlLlc2TermConnectionLocalSubscriberId": nlLlc2TermConnectionLocalSubscriberId,
       "nlLlc2TermConnectionRemoteSubscriberId": nlLlc2TermConnectionRemoteSubscriberId,
       "nlLlc2TermConnectionRowStatus": nlLlc2TermConnectionRowStatus,
       "nlLlc2OrigConnectionTable": nlLlc2OrigConnectionTable,
       "nlLlc2OrigConnectionEntry": nlLlc2OrigConnectionEntry,
       "nlLlc2OrigConnectionSequence": nlLlc2OrigConnectionSequence,
       "nlLlc2OrigConnectionHSAP": nlLlc2OrigConnectionHSAP,
       "nlLlc2OrigConnectionType": nlLlc2OrigConnectionType,
       "nlLlc2OrigConnectionLocalSubscriberId": nlLlc2OrigConnectionLocalSubscriberId,
       "nlLlc2OrigConnectionRemoteSubscriberId": nlLlc2OrigConnectionRemoteSubscriberId,
       "nlLlc2OrigConnectionIDBLK": nlLlc2OrigConnectionIDBLK,
       "nlLlc2OrigConnectionIDNUM": nlLlc2OrigConnectionIDNUM,
       "nlLlc2OrigConnectionMAXDATA": nlLlc2OrigConnectionMAXDATA,
       "nlLlc2OrigConnectionMAXIN": nlLlc2OrigConnectionMAXIN,
       "nlLlc2OrigConnectionRowStatus": nlLlc2OrigConnectionRowStatus,
       "nlLlc2NextHostNumber": nlLlc2NextHostNumber,
       "status": status,
       "pinStatusTable": pinStatusTable,
       "portPinEntry": portPinEntry,
       "portPinRlp": portPinRlp,
       "portPinPort": portPinPort,
       "portPinStatus": portPinStatus,
       "statistics": statistics,
       "statGroup": statGroup,
       "rlpStatsTable": rlpStatsTable,
       "rlpStatsEntry": rlpStatsEntry,
       "rlpStatsIndex": rlpStatsIndex,
       "rlpStatsQMessages": rlpStatsQMessages,
       "rlpStatsUsedBuffers": rlpStatsUsedBuffers,
       "rlpStatsInFrames": rlpStatsInFrames,
       "rlpStatsOutFrames": rlpStatsOutFrames,
       "rlpStatsFrameRejects": rlpStatsFrameRejects,
       "rlpStatsFrameRetransmits": rlpStatsFrameRetransmits,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "portStatsRlpIndex": portStatsRlpIndex,
       "portStatsIndex": portStatsIndex,
       "portStatsInFrames": portStatsInFrames,
       "portStatsOutFrames": portStatsOutFrames,
       "portStatsFrameRetrans": portStatsFrameRetrans,
       "portStatsFCSErrors": portStatsFCSErrors,
       "portStatsLogicalRejects": portStatsLogicalRejects,
       "portStatsInPercentUtils": portStatsInPercentUtils,
       "portStatsOutPercentUtils": portStatsOutPercentUtils,
       "statFrame": statFrame,
       "frStatsTable": frStatsTable,
       "frStatsEntry": frStatsEntry,
       "frStatsRlpIndex": frStatsRlpIndex,
       "frStatsPortIndex": frStatsPortIndex,
       "frStatsTxDEFrames": frStatsTxDEFrames,
       "frStatsRxDEFrames": frStatsRxDEFrames,
       "frStatsTxFECNFrames": frStatsTxFECNFrames,
       "frStatsRxFECNFrames": frStatsRxFECNFrames,
       "frStatsTxBECNFrames": frStatsTxBECNFrames,
       "frStatsRxBECNFrames": frStatsRxBECNFrames,
       "frStatsTxLMIFrames": frStatsTxLMIFrames,
       "frStatsRxLMIFrames": frStatsRxLMIFrames,
       "frStatsTxANXDFrames": frStatsTxANXDFrames,
       "frStatsRxANXDFrames": frStatsRxANXDFrames,
       "frStatsTotDiscFrames": frStatsTotDiscFrames,
       "x25TxStatsTable": x25TxStatsTable,
       "x25TxStatsEntry": x25TxStatsEntry,
       "x25TxRlpIndex": x25TxRlpIndex,
       "x25TxPortIndex": x25TxPortIndex,
       "x25TxSABMFrames": x25TxSABMFrames,
       "x25TxUAFrames": x25TxUAFrames,
       "x25TxDISCFrames": x25TxDISCFrames,
       "x25TxDMFrames": x25TxDMFrames,
       "x25TxFRMRFrames": x25TxFRMRFrames,
       "x25TxREJFrames": x25TxREJFrames,
       "x25TxRRFrames": x25TxRRFrames,
       "x25TxRNRFrames": x25TxRNRFrames,
       "x25TxINFOFrames": x25TxINFOFrames,
       "x25RxStatsTable": x25RxStatsTable,
       "x25RxStatsEntry": x25RxStatsEntry,
       "x25RxRlpIndex": x25RxRlpIndex,
       "x25RxPortIndex": x25RxPortIndex,
       "x25RxSABMFrames": x25RxSABMFrames,
       "x25RxUAFrames": x25RxUAFrames,
       "x25RxDISCFrames": x25RxDISCFrames,
       "x25RxDMFrames": x25RxDMFrames,
       "x25RxFRMRFrames": x25RxFRMRFrames,
       "x25RxREJFrames": x25RxREJFrames,
       "x25RxRRFrames": x25RxRRFrames,
       "x25RxRNRFrames": x25RxRNRFrames,
       "x25RxINFOFrames": x25RxINFOFrames,
       "statBag": statBag,
       "statIp": statIp,
       "statT1": statT1,
       "t1StatsTable": t1StatsTable,
       "t1StatsEntry": t1StatsEntry,
       "t1StatsRlpIndex": t1StatsRlpIndex,
       "t1StatsPortIndex": t1StatsPortIndex,
       "t1StatsRcvFrames": t1StatsRcvFrames,
       "t1StatsXmitFrames": t1StatsXmitFrames,
       "t1StatsLCVCnt": t1StatsLCVCnt,
       "t1StatsPCVRErrs": t1StatsPCVRErrs,
       "t1StatsOOSCnt": t1StatsOOSCnt,
       "t1StatsBlueAlarms": t1StatsBlueAlarms,
       "t1StatsYellowAlarms": t1StatsYellowAlarms,
       "t1StatsRedAlarms": t1StatsRedAlarms,
       "t1StatsRcvUsage": t1StatsRcvUsage,
       "t1StatsXmitUsage": t1StatsXmitUsage,
       "t1StatsXmitAbortFrames": t1StatsXmitAbortFrames,
       "t1StatsRcvAbortFrames": t1StatsRcvAbortFrames,
       "t1StatsRcvOverruns": t1StatsRcvOverruns,
       "t1StatsRcvErrors": t1StatsRcvErrors,
       "t1StatsRcvChannelErrors": t1StatsRcvChannelErrors,
       "statDS0A": statDS0A,
       "ds0aStatsTable": ds0aStatsTable,
       "ds0aStatsEntry": ds0aStatsEntry,
       "ds0aStatsRlpIndex": ds0aStatsRlpIndex,
       "ds0aStatsPortIndex": ds0aStatsPortIndex,
       "ds0aStatsChannelIndex": ds0aStatsChannelIndex,
       "ds0aStatsXmitFrames": ds0aStatsXmitFrames,
       "ds0aStatsRcvFrames": ds0aStatsRcvFrames,
       "ds0aStatsRcvAbortFrames": ds0aStatsRcvAbortFrames,
       "ds0aStatsRcvOverruns": ds0aStatsRcvOverruns,
       "ds0aStatsRcvErrors": ds0aStatsRcvErrors,
       "statVoice": statVoice,
       "voiceStatsTable": voiceStatsTable,
       "voiceStatsEntry": voiceStatsEntry,
       "voiceStatsRlpIndex": voiceStatsRlpIndex,
       "voiceStatsPortIndex": voiceStatsPortIndex,
       "voiceStatsRxCalls": voiceStatsRxCalls,
       "voiceStatsTxCalls": voiceStatsTxCalls,
       "voiceStatsRxCallsAccepts": voiceStatsRxCallsAccepts,
       "voiceStatsTxCallsAccepts": voiceStatsTxCallsAccepts,
       "voiceStatsRxClears": voiceStatsRxClears,
       "voiceStatsTxClears": voiceStatsTxClears,
       "voiceStatsBusyCalls": voiceStatsBusyCalls,
       "voiceStatsCallTimeouts": voiceStatsCallTimeouts,
       "voiceStatsRxCongestions": voiceStatsRxCongestions,
       "voiceStatsTxCongestions": voiceStatsTxCongestions,
       "statThresh": statThresh,
       "rlpThreshTable": rlpThreshTable,
       "rlpThreshEntry": rlpThreshEntry,
       "rlpThreshRlpIndex": rlpThreshRlpIndex,
       "rlpThreshPercntBufInUse": rlpThreshPercntBufInUse,
       "rlpThreshMsgQueueLen": rlpThreshMsgQueueLen,
       "rlpThreshRxFramesPerSec": rlpThreshRxFramesPerSec,
       "rlpThreshTxFramesPerSec": rlpThreshTxFramesPerSec,
       "rlpThreshRejFramesPerSec": rlpThreshRejFramesPerSec,
       "rlpThreshRtxFramesPerSec": rlpThreshRtxFramesPerSec,
       "portThreshTable": portThreshTable,
       "portThreshEntry": portThreshEntry,
       "portThreshRlpIndex": portThreshRlpIndex,
       "portThreshIndex": portThreshIndex,
       "portThreshRxFramesPerSec": portThreshRxFramesPerSec,
       "portThreshTxFramesPerSec": portThreshTxFramesPerSec,
       "portThreshRtxFramesPerSec": portThreshRtxFramesPerSec,
       "portThreshFCSErrPerSec": portThreshFCSErrPerSec,
       "portThreshLogRejPerSec": portThreshLogRejPerSec,
       "portThreshTxErrorRatio": portThreshTxErrorRatio,
       "portThreshRxErrorRatio": portThreshRxErrorRatio,
       "portThreshTxPercentUtl": portThreshTxPercentUtl,
       "portThreshRxPercentUtl": portThreshRxPercentUtl,
       "bridge": bridge,
       "bridgeAdminVirtualLANID": bridgeAdminVirtualLANID,
       "bridgeOperVirtualLANID": bridgeOperVirtualLANID,
       "bridgeEnabled": bridgeEnabled,
       "bridgeMaxSizeForwardingTable": bridgeMaxSizeForwardingTable,
       "bridgeIPEnabled": bridgeIPEnabled,
       "bridgeIPXEnabled": bridgeIPXEnabled,
       "bridgeAdminSRBID": bridgeAdminSRBID,
       "bridgeOperSRBID": bridgeOperSRBID,
       "bridgeDefaultEthernetFrameType": bridgeDefaultEthernetFrameType,
       "ipNl": ipNl,
       "nlIpDefaultRIPVersion": nlIpDefaultRIPVersion,
       "voice": voice,
       "voiceSystemVoiceNodeNum": voiceSystemVoiceNodeNum,
       "voiceSystemRingVolFreq": voiceSystemRingVolFreq,
       "voiceSystemCountryCode": voiceSystemCountryCode,
       "voiceSystemDialDigits": voiceSystemDialDigits,
       "voiceSystemVoiceRatesMin": voiceSystemVoiceRatesMin,
       "voiceSystemVoiceRatesMax": voiceSystemVoiceRatesMax,
       "voiceSystemExtDialDigits": voiceSystemExtDialDigits,
       "voiceSpeedDialTable": voiceSpeedDialTable,
       "voiceSpeedDialEntry": voiceSpeedDialEntry,
       "voiceSpeedDialDigits": voiceSpeedDialDigits,
       "voiceSpeedDialLongDialMap": voiceSpeedDialLongDialMap,
       "voiceSpeedDialExtDialStr": voiceSpeedDialExtDialStr,
       "voiceSpeedDialRowStatus": voiceSpeedDialRowStatus}
)
