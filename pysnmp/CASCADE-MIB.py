# SNMP MIB module (CASCADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASCADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:41 2024
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

(ifInErrors,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors")

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



class Index(Integer32):
    """Custom type Index based on Integer32"""




class CardTypes(Integer32):
    """Custom type CardTypes based on Integer32"""
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
              55,
              56,
              57,
              58,
              59,
              60,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("ads1-e1", 41),
          ("ads1-j2", 42),
          ("ads1-t1", 40),
          ("ads3-e3", 27),
          ("ads3-t3", 26),
          ("atmcs-1", 37),
          ("atmcs-e3-1", 60),
          ("atmds3-1", 17),
          ("atme3-1", 18),
          ("atmiwu-1", 32),
          ("bds3-1-0", 64),
          ("be1-atm-12", 62),
          ("bio1-4-16", 44),
          ("bio1-oc12-1", 46),
          ("bio1-oc12x4", 47),
          ("bio1-oc3-4", 45),
          ("bio1-oc48-1", 48),
          ("bt1-atm-12", 63),
          ("cbr-ds1-s-4", 28),
          ("cbr-ds1-us-4", 29),
          ("cbr-e1-s-4", 30),
          ("cbr-e1-us-4", 31),
          ("cp1", 5),
          ("dsx1-10", 12),
          ("e1-12", 43),
          ("e1-atm", 25),
          ("e1-pri-4", 20),
          ("fast-ether-2", 55),
          ("fe1-1-30", 3),
          ("fe1-4-30", 8),
          ("fe3-1", 10),
          ("ft1-1-24", 2),
          ("ft1-4-24", 7),
          ("ft3-1", 9),
          ("g-server", 69),
          ("gchn-ds3-4", 68),
          ("gfds3-e3-6", 67),
          ("gfds3-t3-6", 66),
          ("gfether-4", 65),
          ("hssi-2", 11),
          ("ls-oc3-1", 56),
          ("np1", 49),
          ("pri-4", 19),
          ("rs232-18", 13),
          ("rs232-8", 14),
          ("sf1", 50),
          ("sft1-4-24", 21),
          ("sp-30", 70),
          ("sp-4", 35),
          ("sp-40", 71),
          ("sp-8", 36),
          ("st1-pri-4", 23),
          ("sut1-4-24", 22),
          ("t1-atm", 24),
          ("tcfds3-e3-6", 58),
          ("tcfds3-t3-6", 57),
          ("tfast-ether-4", 54),
          ("tfds3-e3-6", 53),
          ("tfds3-t3-6", 52),
          ("tm1", 51),
          ("toc12-atm-1", 38),
          ("toc3-atm-4", 33),
          ("toc3-cfc-2", 59),
          ("tstm1-atm-4", 34),
          ("tstm4-atm-1", 39),
          ("ue1-4-30", 16),
          ("uio-6", 4),
          ("uio-8", 6),
          ("ut1-4-24", 15),
          ("v35-6", 1))
    )





class CardStatuses(Integer32):
    """Custom type CardStatuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("maintenance", 6),
          ("overtemp", 7),
          ("testing", 3),
          ("up", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cascade_ObjectIdentity = ObjectIdentity
cascade = _Cascade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277)
)
_Cascfr_ObjectIdentity = ObjectIdentity
cascfr = _Cascfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1)
)
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 1)
)
_NetMask_Type = IpAddress
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 1),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")
_NetNumber_Type = IpAddress
_NetNumber_Object = MibScalar
netNumber = _NetNumber_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 2),
    _NetNumber_Type()
)
netNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netNumber.setStatus("mandatory")


class _NetDlciAddrSig_Type(Integer32):
    """Custom type netDlciAddrSig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalAddr", 1),
          ("localAddr", 2))
    )


_NetDlciAddrSig_Type.__name__ = "Integer32"
_NetDlciAddrSig_Object = MibScalar
netDlciAddrSig = _NetDlciAddrSig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 3),
    _NetDlciAddrSig_Type()
)
netDlciAddrSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDlciAddrSig.setStatus("mandatory")
_NetMaxSegsize_Type = Integer32
_NetMaxSegsize_Object = MibScalar
netMaxSegsize = _NetMaxSegsize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 4),
    _NetMaxSegsize_Type()
)
netMaxSegsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMaxSegsize.setStatus("mandatory")
_NetSmdsAreaMaskStart_Type = Integer32
_NetSmdsAreaMaskStart_Object = MibScalar
netSmdsAreaMaskStart = _NetSmdsAreaMaskStart_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 8),
    _NetSmdsAreaMaskStart_Type()
)
netSmdsAreaMaskStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSmdsAreaMaskStart.setStatus("mandatory")
_NetSmdsAreaMaskDigits_Type = Integer32
_NetSmdsAreaMaskDigits_Object = MibScalar
netSmdsAreaMaskDigits = _NetSmdsAreaMaskDigits_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 1, 9),
    _NetSmdsAreaMaskDigits_Type()
)
netSmdsAreaMaskDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSmdsAreaMaskDigits.setStatus("mandatory")
_Ase_ObjectIdentity = ObjectIdentity
ase = _Ase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 2)
)
_AseTable_Object = MibTable
aseTable = _AseTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aseTable.setStatus("mandatory")
_AseEntry_Object = MibTableRow
aseEntry = _AseEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1)
)
aseEntry.setIndexNames(
    (0, "CASCADE-MIB", "aseAddr"),
)
if mibBuilder.loadTexts:
    aseEntry.setStatus("mandatory")
_AseAddr_Type = IpAddress
_AseAddr_Object = MibTableColumn
aseAddr = _AseAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 1),
    _AseAddr_Type()
)
aseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aseAddr.setStatus("mandatory")
_AseMask_Type = IpAddress
_AseMask_Object = MibTableColumn
aseMask = _AseMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 2),
    _AseMask_Type()
)
aseMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aseMask.setStatus("mandatory")
_AseDefaultGwAddr_Type = IpAddress
_AseDefaultGwAddr_Object = MibTableColumn
aseDefaultGwAddr = _AseDefaultGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 3),
    _AseDefaultGwAddr_Type()
)
aseDefaultGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aseDefaultGwAddr.setStatus("mandatory")
_AseMetricType_Type = Integer32
_AseMetricType_Object = MibTableColumn
aseMetricType = _AseMetricType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 4),
    _AseMetricType_Type()
)
aseMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aseMetricType.setStatus("mandatory")


class _AseAdminStatus_Type(Integer32):
    """Custom type aseAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("valid", 1)
    )


_AseAdminStatus_Type.__name__ = "Integer32"
_AseAdminStatus_Object = MibTableColumn
aseAdminStatus = _AseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 5),
    _AseAdminStatus_Type()
)
aseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aseAdminStatus.setStatus("mandatory")
_AseIfIndex_Type = Index
_AseIfIndex_Object = MibTableColumn
aseIfIndex = _AseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 6),
    _AseIfIndex_Type()
)
aseIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aseIfIndex.setStatus("mandatory")
_AseDlci_Type = Integer32
_AseDlci_Object = MibTableColumn
aseDlci = _AseDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 2, 1, 1, 7),
    _AseDlci_Type()
)
aseDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aseDlci.setStatus("mandatory")
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 3)
)
_NodeIpAddr_Type = IpAddress
_NodeIpAddr_Object = MibScalar
nodeIpAddr = _NodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 1),
    _NodeIpAddr_Type()
)
nodeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeIpAddr.setStatus("mandatory")
_NodeLanIpAddr_Type = IpAddress
_NodeLanIpAddr_Object = MibScalar
nodeLanIpAddr = _NodeLanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 2),
    _NodeLanIpAddr_Type()
)
nodeLanIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeLanIpAddr.setStatus("mandatory")
_NodeNMSTable_Object = MibTable
nodeNMSTable = _NodeNMSTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nodeNMSTable.setStatus("mandatory")
_NodeNMSEntry_Object = MibTableRow
nodeNMSEntry = _NodeNMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 3, 1)
)
nodeNMSEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeNMSIndex"),
)
if mibBuilder.loadTexts:
    nodeNMSEntry.setStatus("mandatory")
_NodeNMSIndex_Type = Index
_NodeNMSIndex_Object = MibTableColumn
nodeNMSIndex = _NodeNMSIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 3, 1, 1),
    _NodeNMSIndex_Type()
)
nodeNMSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNMSIndex.setStatus("mandatory")
_NodeNMSIpAddr_Type = IpAddress
_NodeNMSIpAddr_Object = MibTableColumn
nodeNMSIpAddr = _NodeNMSIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 3, 1, 2),
    _NodeNMSIpAddr_Type()
)
nodeNMSIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeNMSIpAddr.setStatus("mandatory")


class _NodeState_Type(Integer32):
    """Custom type nodeState based on Integer32"""
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
        *(("active", 3),
          ("down", 1),
          ("initializing", 2),
          ("marginal", 4),
          ("testing", 5))
    )


_NodeState_Type.__name__ = "Integer32"
_NodeState_Object = MibScalar
nodeState = _NodeState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 4),
    _NodeState_Type()
)
nodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeState.setStatus("mandatory")
_NodePollStatus_Type = OctetString
_NodePollStatus_Object = MibScalar
nodePollStatus = _NodePollStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 5),
    _NodePollStatus_Type()
)
nodePollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePollStatus.setStatus("mandatory")
_NodeModel_Type = DisplayString
_NodeModel_Object = MibScalar
nodeModel = _NodeModel_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 6),
    _NodeModel_Type()
)
nodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeModel.setStatus("mandatory")
_NodeSerial_Type = OctetString
_NodeSerial_Object = MibScalar
nodeSerial = _NodeSerial_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 7),
    _NodeSerial_Type()
)
nodeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSerial.setStatus("mandatory")
_NodeSwRev_Type = DisplayString
_NodeSwRev_Object = MibScalar
nodeSwRev = _NodeSwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 8),
    _NodeSwRev_Type()
)
nodeSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSwRev.setStatus("mandatory")
_NodeHwRev_Type = DisplayString
_NodeHwRev_Object = MibScalar
nodeHwRev = _NodeHwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 9),
    _NodeHwRev_Type()
)
nodeHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHwRev.setStatus("mandatory")
_NodeEpromRev_Type = DisplayString
_NodeEpromRev_Object = MibScalar
nodeEpromRev = _NodeEpromRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 10),
    _NodeEpromRev_Type()
)
nodeEpromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeEpromRev.setStatus("mandatory")
_NodeCpuUtil_Type = Gauge32
_NodeCpuUtil_Object = MibScalar
nodeCpuUtil = _NodeCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 11),
    _NodeCpuUtil_Type()
)
nodeCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCpuUtil.setStatus("mandatory")


class _NodePsAStatus_Type(Integer32):
    """Custom type nodePsAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("marginal", 4),
          ("up", 1))
    )


_NodePsAStatus_Type.__name__ = "Integer32"
_NodePsAStatus_Object = MibScalar
nodePsAStatus = _NodePsAStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 12),
    _NodePsAStatus_Type()
)
nodePsAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePsAStatus.setStatus("mandatory")


class _NodePsBStatus_Type(Integer32):
    """Custom type nodePsBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("marginal", 4),
          ("up", 1))
    )


_NodePsBStatus_Type.__name__ = "Integer32"
_NodePsBStatus_Object = MibScalar
nodePsBStatus = _NodePsBStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 13),
    _NodePsBStatus_Type()
)
nodePsBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePsBStatus.setStatus("mandatory")
_NodeFanTable_Object = MibTable
nodeFanTable = _NodeFanTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 14)
)
if mibBuilder.loadTexts:
    nodeFanTable.setStatus("mandatory")
_NodeFanEntry_Object = MibTableRow
nodeFanEntry = _NodeFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 14, 1)
)
nodeFanEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeFanIndex"),
)
if mibBuilder.loadTexts:
    nodeFanEntry.setStatus("mandatory")
_NodeFanIndex_Type = Integer32
_NodeFanIndex_Object = MibTableColumn
nodeFanIndex = _NodeFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 14, 1, 1),
    _NodeFanIndex_Type()
)
nodeFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFanIndex.setStatus("mandatory")


class _NodeFanStatus_Type(Integer32):
    """Custom type nodeFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("marginal", 3),
          ("up", 1))
    )


_NodeFanStatus_Type.__name__ = "Integer32"
_NodeFanStatus_Object = MibTableColumn
nodeFanStatus = _NodeFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 14, 1, 2),
    _NodeFanStatus_Type()
)
nodeFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFanStatus.setStatus("mandatory")
_NodeFanSpeed_Type = Gauge32
_NodeFanSpeed_Object = MibTableColumn
nodeFanSpeed = _NodeFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 14, 1, 3),
    _NodeFanSpeed_Type()
)
nodeFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFanSpeed.setStatus("mandatory")
_NodeMemoryUtil_Type = Gauge32
_NodeMemoryUtil_Object = MibScalar
nodeMemoryUtil = _NodeMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 15),
    _NodeMemoryUtil_Type()
)
nodeMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMemoryUtil.setStatus("mandatory")
_NodeMemoryUsage_Type = Gauge32
_NodeMemoryUsage_Object = MibScalar
nodeMemoryUsage = _NodeMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 16),
    _NodeMemoryUsage_Type()
)
nodeMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMemoryUsage.setStatus("mandatory")
_NodeMaxFramesize_Type = Integer32
_NodeMaxFramesize_Object = MibScalar
nodeMaxFramesize = _NodeMaxFramesize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 17),
    _NodeMaxFramesize_Type()
)
nodeMaxFramesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMaxFramesize.setStatus("mandatory")
_NodeQOSPollTimer_Type = Integer32
_NodeQOSPollTimer_Object = MibScalar
nodeQOSPollTimer = _NodeQOSPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 18),
    _NodeQOSPollTimer_Type()
)
nodeQOSPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeQOSPollTimer.setStatus("mandatory")
_NodeActivePvcs_Type = Counter32
_NodeActivePvcs_Object = MibScalar
nodeActivePvcs = _NodeActivePvcs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 19),
    _NodeActivePvcs_Type()
)
nodeActivePvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeActivePvcs.setStatus("mandatory")
_NodeInactivePvcs_Type = Counter32
_NodeInactivePvcs_Object = MibScalar
nodeInactivePvcs = _NodeInactivePvcs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 20),
    _NodeInactivePvcs_Type()
)
nodeInactivePvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInactivePvcs.setStatus("mandatory")
_NodePendingPvcs_Type = Counter32
_NodePendingPvcs_Object = MibScalar
nodePendingPvcs = _NodePendingPvcs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 21),
    _NodePendingPvcs_Type()
)
nodePendingPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePendingPvcs.setStatus("mandatory")
_NodeInOctets_Type = Counter32
_NodeInOctets_Object = MibScalar
nodeInOctets = _NodeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 22),
    _NodeInOctets_Type()
)
nodeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInOctets.setStatus("mandatory")
_NodeInPkts_Type = Counter32
_NodeInPkts_Object = MibScalar
nodeInPkts = _NodeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 23),
    _NodeInPkts_Type()
)
nodeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInPkts.setStatus("mandatory")
_NodeOutOctets_Type = Counter32
_NodeOutOctets_Object = MibScalar
nodeOutOctets = _NodeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 24),
    _NodeOutOctets_Type()
)
nodeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOutOctets.setStatus("mandatory")
_NodeOutPkts_Type = Counter32
_NodeOutPkts_Object = MibScalar
nodeOutPkts = _NodeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 25),
    _NodeOutPkts_Type()
)
nodeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOutPkts.setStatus("mandatory")
_NodeSwFilename_Type = DisplayString
_NodeSwFilename_Object = MibScalar
nodeSwFilename = _NodeSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 26),
    _NodeSwFilename_Type()
)
nodeSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSwFilename.setStatus("mandatory")


class _NodeRebootAfterLoad_Type(Integer32):
    """Custom type nodeRebootAfterLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_NodeRebootAfterLoad_Type.__name__ = "Integer32"
_NodeRebootAfterLoad_Object = MibScalar
nodeRebootAfterLoad = _NodeRebootAfterLoad_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 27),
    _NodeRebootAfterLoad_Type()
)
nodeRebootAfterLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRebootAfterLoad.setStatus("mandatory")
_NodeSwToLoad_Type = TimeTicks
_NodeSwToLoad_Object = MibScalar
nodeSwToLoad = _NodeSwToLoad_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 28),
    _NodeSwToLoad_Type()
)
nodeSwToLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSwToLoad.setStatus("mandatory")


class _NodeSwLoadState_Type(Integer32):
    """Custom type nodeSwLoadState based on Integer32"""
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
        *(("active", 3),
          ("failed", 4),
          ("inactive", 1),
          ("pending", 2))
    )


_NodeSwLoadState_Type.__name__ = "Integer32"
_NodeSwLoadState_Object = MibScalar
nodeSwLoadState = _NodeSwLoadState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 29),
    _NodeSwLoadState_Type()
)
nodeSwLoadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSwLoadState.setStatus("mandatory")
_NodePrFilename_Type = DisplayString
_NodePrFilename_Object = MibScalar
nodePrFilename = _NodePrFilename_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 30),
    _NodePrFilename_Type()
)
nodePrFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodePrFilename.setStatus("mandatory")
_NodePrToLoad_Type = TimeTicks
_NodePrToLoad_Object = MibScalar
nodePrToLoad = _NodePrToLoad_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 31),
    _NodePrToLoad_Type()
)
nodePrToLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodePrToLoad.setStatus("mandatory")


class _NodePrLoadState_Type(Integer32):
    """Custom type nodePrLoadState based on Integer32"""
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
        *(("active", 3),
          ("failed", 4),
          ("inactive", 1),
          ("pending", 2))
    )


_NodePrLoadState_Type.__name__ = "Integer32"
_NodePrLoadState_Object = MibScalar
nodePrLoadState = _NodePrLoadState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 32),
    _NodePrLoadState_Type()
)
nodePrLoadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodePrLoadState.setStatus("mandatory")
_NodeToWarmboot_Type = TimeTicks
_NodeToWarmboot_Object = MibScalar
nodeToWarmboot = _NodeToWarmboot_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 33),
    _NodeToWarmboot_Type()
)
nodeToWarmboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeToWarmboot.setStatus("mandatory")
_NodeToColdboot_Type = TimeTicks
_NodeToColdboot_Object = MibScalar
nodeToColdboot = _NodeToColdboot_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 34),
    _NodeToColdboot_Type()
)
nodeToColdboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeToColdboot.setStatus("mandatory")
_NodeToRedundant_Type = TimeTicks
_NodeToRedundant_Object = MibScalar
nodeToRedundant = _NodeToRedundant_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 35),
    _NodeToRedundant_Type()
)
nodeToRedundant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeToRedundant.setStatus("mandatory")
_NodeInitiateBulkStats_Type = IpAddress
_NodeInitiateBulkStats_Object = MibScalar
nodeInitiateBulkStats = _NodeInitiateBulkStats_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 36),
    _NodeInitiateBulkStats_Type()
)
nodeInitiateBulkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeInitiateBulkStats.setStatus("mandatory")


class _NodeDiagNonFatalSource_Type(Integer32):
    """Custom type nodeDiagNonFatalSource based on Integer32"""
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
        *(("background-diagnostics", 2),
          ("fault", 3),
          ("frame-heap", 4),
          ("power-on-diagnostics", 1))
    )


_NodeDiagNonFatalSource_Type.__name__ = "Integer32"
_NodeDiagNonFatalSource_Object = MibScalar
nodeDiagNonFatalSource = _NodeDiagNonFatalSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 37),
    _NodeDiagNonFatalSource_Type()
)
nodeDiagNonFatalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagNonFatalSource.setStatus("mandatory")
_NodeDiagNonFatalTime_Type = TimeTicks
_NodeDiagNonFatalTime_Object = MibScalar
nodeDiagNonFatalTime = _NodeDiagNonFatalTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 38),
    _NodeDiagNonFatalTime_Type()
)
nodeDiagNonFatalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagNonFatalTime.setStatus("mandatory")
_NodeDiagNonFatalErrMajor_Type = Integer32
_NodeDiagNonFatalErrMajor_Object = MibScalar
nodeDiagNonFatalErrMajor = _NodeDiagNonFatalErrMajor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 39),
    _NodeDiagNonFatalErrMajor_Type()
)
nodeDiagNonFatalErrMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagNonFatalErrMajor.setStatus("mandatory")
_NodeDiagNonFatalErrMinor_Type = Integer32
_NodeDiagNonFatalErrMinor_Object = MibScalar
nodeDiagNonFatalErrMinor = _NodeDiagNonFatalErrMinor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 40),
    _NodeDiagNonFatalErrMinor_Type()
)
nodeDiagNonFatalErrMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagNonFatalErrMinor.setStatus("mandatory")
_NodeDiagNonFatalStr_Type = DisplayString
_NodeDiagNonFatalStr_Object = MibScalar
nodeDiagNonFatalStr = _NodeDiagNonFatalStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 41),
    _NodeDiagNonFatalStr_Type()
)
nodeDiagNonFatalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagNonFatalStr.setStatus("mandatory")


class _NodeDiagFatalSource_Type(Integer32):
    """Custom type nodeDiagFatalSource based on Integer32"""
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
        *(("background-diagnostics", 2),
          ("fault", 3),
          ("frame-heap", 4),
          ("power-on-diagnostics", 1))
    )


_NodeDiagFatalSource_Type.__name__ = "Integer32"
_NodeDiagFatalSource_Object = MibScalar
nodeDiagFatalSource = _NodeDiagFatalSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 42),
    _NodeDiagFatalSource_Type()
)
nodeDiagFatalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalSource.setStatus("mandatory")
_NodeDiagFatalTime_Type = TimeTicks
_NodeDiagFatalTime_Object = MibScalar
nodeDiagFatalTime = _NodeDiagFatalTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 43),
    _NodeDiagFatalTime_Type()
)
nodeDiagFatalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalTime.setStatus("mandatory")
_NodeDiagFatalErrMajor_Type = Integer32
_NodeDiagFatalErrMajor_Object = MibScalar
nodeDiagFatalErrMajor = _NodeDiagFatalErrMajor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 44),
    _NodeDiagFatalErrMajor_Type()
)
nodeDiagFatalErrMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalErrMajor.setStatus("mandatory")
_NodeDiagFatalErrMinor_Type = Integer32
_NodeDiagFatalErrMinor_Object = MibScalar
nodeDiagFatalErrMinor = _NodeDiagFatalErrMinor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 45),
    _NodeDiagFatalErrMinor_Type()
)
nodeDiagFatalErrMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalErrMinor.setStatus("mandatory")
_NodeDiagFatalStr_Type = DisplayString
_NodeDiagFatalStr_Object = MibScalar
nodeDiagFatalStr = _NodeDiagFatalStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 46),
    _NodeDiagFatalStr_Type()
)
nodeDiagFatalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalStr.setStatus("mandatory")
_NodeDiagFatalReboots_Type = Counter32
_NodeDiagFatalReboots_Object = MibScalar
nodeDiagFatalReboots = _NodeDiagFatalReboots_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 47),
    _NodeDiagFatalReboots_Type()
)
nodeDiagFatalReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalReboots.setStatus("mandatory")
_NodeDiagFatalAddress_Type = Integer32
_NodeDiagFatalAddress_Object = MibScalar
nodeDiagFatalAddress = _NodeDiagFatalAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 48),
    _NodeDiagFatalAddress_Type()
)
nodeDiagFatalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagFatalAddress.setStatus("mandatory")
_NodeDiagBackgroundPasses_Type = Counter32
_NodeDiagBackgroundPasses_Object = MibScalar
nodeDiagBackgroundPasses = _NodeDiagBackgroundPasses_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 49),
    _NodeDiagBackgroundPasses_Type()
)
nodeDiagBackgroundPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagBackgroundPasses.setStatus("mandatory")
_NodeDiagBackgroundFailures_Type = Counter32
_NodeDiagBackgroundFailures_Object = MibScalar
nodeDiagBackgroundFailures = _NodeDiagBackgroundFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 50),
    _NodeDiagBackgroundFailures_Type()
)
nodeDiagBackgroundFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagBackgroundFailures.setStatus("mandatory")
_NodeDiagBackgroundSuccesses_Type = Counter32
_NodeDiagBackgroundSuccesses_Object = MibScalar
nodeDiagBackgroundSuccesses = _NodeDiagBackgroundSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 51),
    _NodeDiagBackgroundSuccesses_Type()
)
nodeDiagBackgroundSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeDiagBackgroundSuccesses.setStatus("mandatory")


class _NodeDiagLEDReset_Type(Integer32):
    """Custom type nodeDiagLEDReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("state-to-active", 1)
    )


_NodeDiagLEDReset_Type.__name__ = "Integer32"
_NodeDiagLEDReset_Object = MibScalar
nodeDiagLEDReset = _NodeDiagLEDReset_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 52),
    _NodeDiagLEDReset_Type()
)
nodeDiagLEDReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeDiagLEDReset.setStatus("mandatory")


class _NodeDiagPowerExtensive_Type(Integer32):
    """Custom type nodeDiagPowerExtensive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("extensive-tests", 1)
    )


_NodeDiagPowerExtensive_Type.__name__ = "Integer32"
_NodeDiagPowerExtensive_Object = MibScalar
nodeDiagPowerExtensive = _NodeDiagPowerExtensive_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 53),
    _NodeDiagPowerExtensive_Type()
)
nodeDiagPowerExtensive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeDiagPowerExtensive.setStatus("mandatory")
_NodePortPoll_Type = OctetString
_NodePortPoll_Object = MibScalar
nodePortPoll = _NodePortPoll_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 54),
    _NodePortPoll_Type()
)
nodePortPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePortPoll.setStatus("mandatory")
_NodeMaxTelnetConsole_Type = Integer32
_NodeMaxTelnetConsole_Object = MibScalar
nodeMaxTelnetConsole = _NodeMaxTelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 55),
    _NodeMaxTelnetConsole_Type()
)
nodeMaxTelnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeMaxTelnetConsole.setStatus("mandatory")
_NodeConsoleTimeout_Type = Integer32
_NodeConsoleTimeout_Object = MibScalar
nodeConsoleTimeout = _NodeConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 56),
    _NodeConsoleTimeout_Type()
)
nodeConsoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeConsoleTimeout.setStatus("mandatory")
_NodeConsoleTable_Object = MibTable
nodeConsoleTable = _NodeConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57)
)
if mibBuilder.loadTexts:
    nodeConsoleTable.setStatus("mandatory")
_NodeConsoleEntry_Object = MibTableRow
nodeConsoleEntry = _NodeConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1)
)
nodeConsoleEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeConsoleIndex"),
)
if mibBuilder.loadTexts:
    nodeConsoleEntry.setStatus("mandatory")


class _NodeConsoleIndex_Type(Integer32):
    """Custom type nodeConsoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_NodeConsoleIndex_Type.__name__ = "Integer32"
_NodeConsoleIndex_Object = MibTableColumn
nodeConsoleIndex = _NodeConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1, 1),
    _NodeConsoleIndex_Type()
)
nodeConsoleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeConsoleIndex.setStatus("mandatory")
_NodeUserName_Type = OctetString
_NodeUserName_Object = MibTableColumn
nodeUserName = _NodeUserName_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1, 2),
    _NodeUserName_Type()
)
nodeUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeUserName.setStatus("mandatory")
_NodeUserFrom_Type = IpAddress
_NodeUserFrom_Object = MibTableColumn
nodeUserFrom = _NodeUserFrom_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1, 3),
    _NodeUserFrom_Type()
)
nodeUserFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeUserFrom.setStatus("mandatory")


class _NodeConsoleAccessMode_Type(Integer32):
    """Custom type nodeConsoleAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_NodeConsoleAccessMode_Type.__name__ = "Integer32"
_NodeConsoleAccessMode_Object = MibTableColumn
nodeConsoleAccessMode = _NodeConsoleAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1, 4),
    _NodeConsoleAccessMode_Type()
)
nodeConsoleAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeConsoleAccessMode.setStatus("mandatory")
_NodeConsoleUptime_Type = TimeTicks
_NodeConsoleUptime_Object = MibTableColumn
nodeConsoleUptime = _NodeConsoleUptime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 57, 1, 5),
    _NodeConsoleUptime_Type()
)
nodeConsoleUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeConsoleUptime.setStatus("mandatory")
_NodePsADiagCode_Type = Integer32
_NodePsADiagCode_Object = MibScalar
nodePsADiagCode = _NodePsADiagCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 58),
    _NodePsADiagCode_Type()
)
nodePsADiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePsADiagCode.setStatus("mandatory")
_NodePsBDiagCode_Type = Integer32
_NodePsBDiagCode_Object = MibScalar
nodePsBDiagCode = _NodePsBDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 59),
    _NodePsBDiagCode_Type()
)
nodePsBDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePsBDiagCode.setStatus("mandatory")
_NodeFrameMemoryUtil_Type = Gauge32
_NodeFrameMemoryUtil_Object = MibScalar
nodeFrameMemoryUtil = _NodeFrameMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 60),
    _NodeFrameMemoryUtil_Type()
)
nodeFrameMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFrameMemoryUtil.setStatus("mandatory")
_NodeFrameMemoryUsage_Type = Gauge32
_NodeFrameMemoryUsage_Object = MibScalar
nodeFrameMemoryUsage = _NodeFrameMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 61),
    _NodeFrameMemoryUsage_Type()
)
nodeFrameMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFrameMemoryUsage.setStatus("mandatory")


class _NodeCapability_Type(Integer32):
    """Custom type nodeCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 1),
          ("smds", 2))
    )


_NodeCapability_Type.__name__ = "Integer32"
_NodeCapability_Object = MibScalar
nodeCapability = _NodeCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 62),
    _NodeCapability_Type()
)
nodeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCapability.setStatus("mandatory")
_NodeSvcLastCallFailure_Type = OctetString
_NodeSvcLastCallFailure_Object = MibScalar
nodeSvcLastCallFailure = _NodeSvcLastCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 63),
    _NodeSvcLastCallFailure_Type()
)
nodeSvcLastCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSvcLastCallFailure.setStatus("mandatory")
_NodeRerouteDelay_Type = Integer32
_NodeRerouteDelay_Object = MibScalar
nodeRerouteDelay = _NodeRerouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 64),
    _NodeRerouteDelay_Type()
)
nodeRerouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRerouteDelay.setStatus("mandatory")
_NodeRerouteCount_Type = Integer32
_NodeRerouteCount_Object = MibScalar
nodeRerouteCount = _NodeRerouteCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 65),
    _NodeRerouteCount_Type()
)
nodeRerouteCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRerouteCount.setStatus("mandatory")
_NodeFileTransferRequest_Type = DisplayString
_NodeFileTransferRequest_Object = MibScalar
nodeFileTransferRequest = _NodeFileTransferRequest_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 66),
    _NodeFileTransferRequest_Type()
)
nodeFileTransferRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeFileTransferRequest.setStatus("mandatory")


class _NodeFileTransferStatus_Type(Integer32):
    """Custom type nodeFileTransferStatus based on Integer32"""
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
        *(("active", 2),
          ("canceled", 7),
          ("complete", 1),
          ("failed", 3),
          ("filename", 5),
          ("invalid", 4),
          ("timeout", 6))
    )


_NodeFileTransferStatus_Type.__name__ = "Integer32"
_NodeFileTransferStatus_Object = MibScalar
nodeFileTransferStatus = _NodeFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 67),
    _NodeFileTransferStatus_Type()
)
nodeFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFileTransferStatus.setStatus("mandatory")
_NodeTime_Type = TimeTicks
_NodeTime_Object = MibScalar
nodeTime = _NodeTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 68),
    _NodeTime_Type()
)
nodeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeTime.setStatus("mandatory")
_NodeBillingAPAddress_Type = IpAddress
_NodeBillingAPAddress_Object = MibScalar
nodeBillingAPAddress = _NodeBillingAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 69),
    _NodeBillingAPAddress_Type()
)
nodeBillingAPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingAPAddress.setStatus("mandatory")
_NodeBillingAPUsername_Type = DisplayString
_NodeBillingAPUsername_Object = MibScalar
nodeBillingAPUsername = _NodeBillingAPUsername_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 70),
    _NodeBillingAPUsername_Type()
)
nodeBillingAPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingAPUsername.setStatus("mandatory")
_NodeBillingAPPassword_Type = DisplayString
_NodeBillingAPPassword_Object = MibScalar
nodeBillingAPPassword = _NodeBillingAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 71),
    _NodeBillingAPPassword_Type()
)
nodeBillingAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingAPPassword.setStatus("mandatory")
_NodeBillingSwAPCommsFailures_Type = Counter32
_NodeBillingSwAPCommsFailures_Object = MibScalar
nodeBillingSwAPCommsFailures = _NodeBillingSwAPCommsFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 72),
    _NodeBillingSwAPCommsFailures_Type()
)
nodeBillingSwAPCommsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingSwAPCommsFailures.setStatus("mandatory")
_NodeBillingTable_Object = MibTable
nodeBillingTable = _NodeBillingTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73)
)
if mibBuilder.loadTexts:
    nodeBillingTable.setStatus("mandatory")
_NodeBillingEntry_Object = MibTableRow
nodeBillingEntry = _NodeBillingEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1)
)
nodeBillingEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeBillingService"),
)
if mibBuilder.loadTexts:
    nodeBillingEntry.setStatus("mandatory")


class _NodeBillingService_Type(Integer32):
    """Custom type nodeBillingService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("smds", 1)
    )


_NodeBillingService_Type.__name__ = "Integer32"
_NodeBillingService_Object = MibTableColumn
nodeBillingService = _NodeBillingService_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 1),
    _NodeBillingService_Type()
)
nodeBillingService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingService.setStatus("mandatory")


class _NodeBilling_Type(Integer32):
    """Custom type nodeBilling based on Integer32"""
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


_NodeBilling_Type.__name__ = "Integer32"
_NodeBilling_Object = MibTableColumn
nodeBilling = _NodeBilling_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 2),
    _NodeBilling_Type()
)
nodeBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBilling.setStatus("mandatory")
_NodeBillingAggrPeriod_Type = TimeTicks
_NodeBillingAggrPeriod_Object = MibTableColumn
nodeBillingAggrPeriod = _NodeBillingAggrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 3),
    _NodeBillingAggrPeriod_Type()
)
nodeBillingAggrPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingAggrPeriod.setStatus("mandatory")
_NodeBillingCurAggrPeriodStart_Type = TimeTicks
_NodeBillingCurAggrPeriodStart_Object = MibTableColumn
nodeBillingCurAggrPeriodStart = _NodeBillingCurAggrPeriodStart_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 4),
    _NodeBillingCurAggrPeriodStart_Type()
)
nodeBillingCurAggrPeriodStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingCurAggrPeriodStart.setStatus("mandatory")
_NodeBillingCurAggrPeriodEnd_Type = TimeTicks
_NodeBillingCurAggrPeriodEnd_Object = MibTableColumn
nodeBillingCurAggrPeriodEnd = _NodeBillingCurAggrPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 5),
    _NodeBillingCurAggrPeriodEnd_Type()
)
nodeBillingCurAggrPeriodEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingCurAggrPeriodEnd.setStatus("mandatory")
_NodeBillingCollection_Type = TimeTicks
_NodeBillingCollection_Object = MibTableColumn
nodeBillingCollection = _NodeBillingCollection_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 6),
    _NodeBillingCollection_Type()
)
nodeBillingCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingCollection.setStatus("mandatory")


class _NodeBillingDailyProcessing_Type(Integer32):
    """Custom type nodeBillingDailyProcessing based on Integer32"""
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


_NodeBillingDailyProcessing_Type.__name__ = "Integer32"
_NodeBillingDailyProcessing_Object = MibTableColumn
nodeBillingDailyProcessing = _NodeBillingDailyProcessing_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 7),
    _NodeBillingDailyProcessing_Type()
)
nodeBillingDailyProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingDailyProcessing.setStatus("mandatory")
_NodeBillingDPTime_Type = TimeTicks
_NodeBillingDPTime_Object = MibTableColumn
nodeBillingDPTime = _NodeBillingDPTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 8),
    _NodeBillingDPTime_Type()
)
nodeBillingDPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingDPTime.setStatus("mandatory")
_NodeBillingUsageRecOvflWarnings_Type = Counter32
_NodeBillingUsageRecOvflWarnings_Object = MibTableColumn
nodeBillingUsageRecOvflWarnings = _NodeBillingUsageRecOvflWarnings_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 9),
    _NodeBillingUsageRecOvflWarnings_Type()
)
nodeBillingUsageRecOvflWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingUsageRecOvflWarnings.setStatus("mandatory")
_NodeBillingTotalUsageRecOvflWarnings_Type = Counter32
_NodeBillingTotalUsageRecOvflWarnings_Object = MibTableColumn
nodeBillingTotalUsageRecOvflWarnings = _NodeBillingTotalUsageRecOvflWarnings_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 10),
    _NodeBillingTotalUsageRecOvflWarnings_Type()
)
nodeBillingTotalUsageRecOvflWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingTotalUsageRecOvflWarnings.setStatus("mandatory")
_NodeBillingBillableUsageEvents_Type = Counter32
_NodeBillingBillableUsageEvents_Object = MibTableColumn
nodeBillingBillableUsageEvents = _NodeBillingBillableUsageEvents_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 11),
    _NodeBillingBillableUsageEvents_Type()
)
nodeBillingBillableUsageEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingBillableUsageEvents.setStatus("mandatory")
_NodeBillingNonBillableUsageEvents_Type = Counter32
_NodeBillingNonBillableUsageEvents_Object = MibTableColumn
nodeBillingNonBillableUsageEvents = _NodeBillingNonBillableUsageEvents_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 12),
    _NodeBillingNonBillableUsageEvents_Type()
)
nodeBillingNonBillableUsageEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingNonBillableUsageEvents.setStatus("mandatory")
_NodeBillingUsageRecCreated_Type = Counter32
_NodeBillingUsageRecCreated_Object = MibTableColumn
nodeBillingUsageRecCreated = _NodeBillingUsageRecCreated_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 13),
    _NodeBillingUsageRecCreated_Type()
)
nodeBillingUsageRecCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingUsageRecCreated.setStatus("mandatory")
_NodeBillingTotalUsageRecCreated_Type = Counter32
_NodeBillingTotalUsageRecCreated_Object = MibTableColumn
nodeBillingTotalUsageRecCreated = _NodeBillingTotalUsageRecCreated_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 14),
    _NodeBillingTotalUsageRecCreated_Type()
)
nodeBillingTotalUsageRecCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingTotalUsageRecCreated.setStatus("mandatory")
_NodeBillingUsageRecCrFailures_Type = Counter32
_NodeBillingUsageRecCrFailures_Object = MibTableColumn
nodeBillingUsageRecCrFailures = _NodeBillingUsageRecCrFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 15),
    _NodeBillingUsageRecCrFailures_Type()
)
nodeBillingUsageRecCrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingUsageRecCrFailures.setStatus("mandatory")
_NodeBillingTotalUsageRecCrFailures_Type = Counter32
_NodeBillingTotalUsageRecCrFailures_Object = MibTableColumn
nodeBillingTotalUsageRecCrFailures = _NodeBillingTotalUsageRecCrFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 16),
    _NodeBillingTotalUsageRecCrFailures_Type()
)
nodeBillingTotalUsageRecCrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingTotalUsageRecCrFailures.setStatus("mandatory")
_NodeBillingUsageRecSent_Type = Counter32
_NodeBillingUsageRecSent_Object = MibTableColumn
nodeBillingUsageRecSent = _NodeBillingUsageRecSent_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 17),
    _NodeBillingUsageRecSent_Type()
)
nodeBillingUsageRecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingUsageRecSent.setStatus("mandatory")
_NodeBillingTotalUsageRecSent_Type = Counter32
_NodeBillingTotalUsageRecSent_Object = MibTableColumn
nodeBillingTotalUsageRecSent = _NodeBillingTotalUsageRecSent_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 18),
    _NodeBillingTotalUsageRecSent_Type()
)
nodeBillingTotalUsageRecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingTotalUsageRecSent.setStatus("mandatory")
_NodeBillingUsageDataStoreFull_Type = Counter32
_NodeBillingUsageDataStoreFull_Object = MibTableColumn
nodeBillingUsageDataStoreFull = _NodeBillingUsageDataStoreFull_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 19),
    _NodeBillingUsageDataStoreFull_Type()
)
nodeBillingUsageDataStoreFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingUsageDataStoreFull.setStatus("mandatory")
_NodeBillingTotalUsageDataStoreFull_Type = Counter32
_NodeBillingTotalUsageDataStoreFull_Object = MibTableColumn
nodeBillingTotalUsageDataStoreFull = _NodeBillingTotalUsageDataStoreFull_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 20),
    _NodeBillingTotalUsageDataStoreFull_Type()
)
nodeBillingTotalUsageDataStoreFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBillingTotalUsageDataStoreFull.setStatus("mandatory")


class _NodeBillingAdminAction_Type(Integer32):
    """Custom type nodeBillingAdminAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceUpload", 2),
          ("invalid", 1))
    )


_NodeBillingAdminAction_Type.__name__ = "Integer32"
_NodeBillingAdminAction_Object = MibTableColumn
nodeBillingAdminAction = _NodeBillingAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 73, 1, 21),
    _NodeBillingAdminAction_Type()
)
nodeBillingAdminAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBillingAdminAction.setStatus("mandatory")


class _NodeRerouteAlg_Type(Integer32):
    """Custom type nodeRerouteAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("negneg", 1),
          ("pospos", 2))
    )


_NodeRerouteAlg_Type.__name__ = "Integer32"
_NodeRerouteAlg_Object = MibScalar
nodeRerouteAlg = _NodeRerouteAlg_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 74),
    _NodeRerouteAlg_Type()
)
nodeRerouteAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRerouteAlg.setStatus("mandatory")


class _NodeOamAlarmDisabled_Type(Integer32):
    """Custom type nodeOamAlarmDisabled based on Integer32"""
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


_NodeOamAlarmDisabled_Type.__name__ = "Integer32"
_NodeOamAlarmDisabled_Object = MibScalar
nodeOamAlarmDisabled = _NodeOamAlarmDisabled_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 76),
    _NodeOamAlarmDisabled_Type()
)
nodeOamAlarmDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeOamAlarmDisabled.setStatus("mandatory")
_NodeRefclocksrcTable_Object = MibTable
nodeRefclocksrcTable = _NodeRefclocksrcTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77)
)
if mibBuilder.loadTexts:
    nodeRefclocksrcTable.setStatus("mandatory")
_NodeRefclocksrcEntry_Object = MibTableRow
nodeRefclocksrcEntry = _NodeRefclocksrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1)
)
nodeRefclocksrcEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeRefclocksrcIndex"),
)
if mibBuilder.loadTexts:
    nodeRefclocksrcEntry.setStatus("mandatory")


class _NodeRefclocksrcIndex_Type(Integer32):
    """Custom type nodeRefclocksrcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NodeRefclocksrcIndex_Type.__name__ = "Integer32"
_NodeRefclocksrcIndex_Object = MibTableColumn
nodeRefclocksrcIndex = _NodeRefclocksrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1, 1),
    _NodeRefclocksrcIndex_Type()
)
nodeRefclocksrcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRefclocksrcIndex.setStatus("mandatory")


class _NodeRefclocksrcPriority_Type(Integer32):
    """Custom type nodeRefclocksrcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NodeRefclocksrcPriority_Type.__name__ = "Integer32"
_NodeRefclocksrcPriority_Object = MibTableColumn
nodeRefclocksrcPriority = _NodeRefclocksrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1, 2),
    _NodeRefclocksrcPriority_Type()
)
nodeRefclocksrcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRefclocksrcPriority.setStatus("mandatory")


class _NodeRefclocksrcType_Type(Integer32):
    """Custom type nodeRefclocksrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("pport", 2))
    )


_NodeRefclocksrcType_Type.__name__ = "Integer32"
_NodeRefclocksrcType_Object = MibTableColumn
nodeRefclocksrcType = _NodeRefclocksrcType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1, 3),
    _NodeRefclocksrcType_Type()
)
nodeRefclocksrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRefclocksrcType.setStatus("mandatory")
_NodeRefclocksrcSlotId_Type = Integer32
_NodeRefclocksrcSlotId_Object = MibTableColumn
nodeRefclocksrcSlotId = _NodeRefclocksrcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1, 4),
    _NodeRefclocksrcSlotId_Type()
)
nodeRefclocksrcSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRefclocksrcSlotId.setStatus("mandatory")
_NodeRefclocksrcPportId_Type = Integer32
_NodeRefclocksrcPportId_Object = MibTableColumn
nodeRefclocksrcPportId = _NodeRefclocksrcPportId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 77, 1, 5),
    _NodeRefclocksrcPportId_Type()
)
nodeRefclocksrcPportId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeRefclocksrcPportId.setStatus("mandatory")
_NodeRefclockActiveSrc_Type = Integer32
_NodeRefclockActiveSrc_Object = MibScalar
nodeRefclockActiveSrc = _NodeRefclockActiveSrc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 78),
    _NodeRefclockActiveSrc_Type()
)
nodeRefclockActiveSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRefclockActiveSrc.setStatus("mandatory")
_NodeRefclockActiveCGUSlotId_Type = Integer32
_NodeRefclockActiveCGUSlotId_Object = MibScalar
nodeRefclockActiveCGUSlotId = _NodeRefclockActiveCGUSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 79),
    _NodeRefclockActiveCGUSlotId_Type()
)
nodeRefclockActiveCGUSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRefclockActiveCGUSlotId.setStatus("mandatory")


class _NodeRefclockActiveCGUMode_Type(Integer32):
    """Custom type nodeRefclockActiveCGUMode based on Integer32"""
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
        *(("extended-holdover", 4),
          ("free-running", 1),
          ("holdover", 3),
          ("sync-to-reference-clock", 2))
    )


_NodeRefclockActiveCGUMode_Type.__name__ = "Integer32"
_NodeRefclockActiveCGUMode_Object = MibScalar
nodeRefclockActiveCGUMode = _NodeRefclockActiveCGUMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 80),
    _NodeRefclockActiveCGUMode_Type()
)
nodeRefclockActiveCGUMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRefclockActiveCGUMode.setStatus("mandatory")


class _NodeInitiateImageBackup_Type(Integer32):
    """Custom type nodeInitiateImageBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("proceed", 1)
    )


_NodeInitiateImageBackup_Type.__name__ = "Integer32"
_NodeInitiateImageBackup_Object = MibScalar
nodeInitiateImageBackup = _NodeInitiateImageBackup_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 81),
    _NodeInitiateImageBackup_Type()
)
nodeInitiateImageBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeInitiateImageBackup.setStatus("mandatory")


class _NodeImageBackupState_Type(Integer32):
    """Custom type nodeImageBackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("proceeding", 1))
    )


_NodeImageBackupState_Type.__name__ = "Integer32"
_NodeImageBackupState_Object = MibScalar
nodeImageBackupState = _NodeImageBackupState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 82),
    _NodeImageBackupState_Type()
)
nodeImageBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeImageBackupState.setStatus("mandatory")


class _NodeInitiateImageRestore_Type(Integer32):
    """Custom type nodeInitiateImageRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("proceed", 1)
    )


_NodeInitiateImageRestore_Type.__name__ = "Integer32"
_NodeInitiateImageRestore_Object = MibScalar
nodeInitiateImageRestore = _NodeInitiateImageRestore_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 83),
    _NodeInitiateImageRestore_Type()
)
nodeInitiateImageRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeInitiateImageRestore.setStatus("mandatory")
_NodeApplicationTable_Object = MibTable
nodeApplicationTable = _NodeApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84)
)
if mibBuilder.loadTexts:
    nodeApplicationTable.setStatus("mandatory")
_NodeApplicationEntry_Object = MibTableRow
nodeApplicationEntry = _NodeApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84, 1)
)
nodeApplicationEntry.setIndexNames(
    (0, "CASCADE-MIB", "nodeApplicationIndex"),
)
if mibBuilder.loadTexts:
    nodeApplicationEntry.setStatus("mandatory")
_NodeApplicationIndex_Type = Index
_NodeApplicationIndex_Object = MibTableColumn
nodeApplicationIndex = _NodeApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84, 1, 1),
    _NodeApplicationIndex_Type()
)
nodeApplicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeApplicationIndex.setStatus("mandatory")
_NodeApplicationDescription_Type = DisplayString
_NodeApplicationDescription_Object = MibTableColumn
nodeApplicationDescription = _NodeApplicationDescription_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84, 1, 2),
    _NodeApplicationDescription_Type()
)
nodeApplicationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeApplicationDescription.setStatus("mandatory")
_NodePrimaryVersion_Type = DisplayString
_NodePrimaryVersion_Object = MibTableColumn
nodePrimaryVersion = _NodePrimaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84, 1, 3),
    _NodePrimaryVersion_Type()
)
nodePrimaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePrimaryVersion.setStatus("mandatory")
_NodeSecondaryVersion_Type = DisplayString
_NodeSecondaryVersion_Object = MibTableColumn
nodeSecondaryVersion = _NodeSecondaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 84, 1, 4),
    _NodeSecondaryVersion_Type()
)
nodeSecondaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSecondaryVersion.setStatus("mandatory")


class _NodePrimarySyncRefAdminState_Type(Integer32):
    """Custom type nodePrimarySyncRefAdminState based on Integer32"""
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
        *(("externala", 1),
          ("externalb", 2),
          ("internal", 5),
          ("portrefa", 3),
          ("portrefb", 4))
    )


_NodePrimarySyncRefAdminState_Type.__name__ = "Integer32"
_NodePrimarySyncRefAdminState_Object = MibScalar
nodePrimarySyncRefAdminState = _NodePrimarySyncRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 85),
    _NodePrimarySyncRefAdminState_Type()
)
nodePrimarySyncRefAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodePrimarySyncRefAdminState.setStatus("mandatory")


class _NodePrimarySyncRefOperationalState_Type(Integer32):
    """Custom type nodePrimarySyncRefOperationalState based on Integer32"""
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
        *(("externala", 1),
          ("externalb", 2),
          ("internal", 5),
          ("portrefa", 3),
          ("portrefb", 4))
    )


_NodePrimarySyncRefOperationalState_Type.__name__ = "Integer32"
_NodePrimarySyncRefOperationalState_Object = MibScalar
nodePrimarySyncRefOperationalState = _NodePrimarySyncRefOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 86),
    _NodePrimarySyncRefOperationalState_Type()
)
nodePrimarySyncRefOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePrimarySyncRefOperationalState.setStatus("mandatory")


class _NodeSecondarySyncRefAdminState_Type(Integer32):
    """Custom type nodeSecondarySyncRefAdminState based on Integer32"""
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
        *(("externala", 1),
          ("externalb", 2),
          ("internal", 5),
          ("portrefa", 3),
          ("portrefb", 4))
    )


_NodeSecondarySyncRefAdminState_Type.__name__ = "Integer32"
_NodeSecondarySyncRefAdminState_Object = MibScalar
nodeSecondarySyncRefAdminState = _NodeSecondarySyncRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 87),
    _NodeSecondarySyncRefAdminState_Type()
)
nodeSecondarySyncRefAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSecondarySyncRefAdminState.setStatus("mandatory")


class _NodeSecondarySyncRefOperationalState_Type(Integer32):
    """Custom type nodeSecondarySyncRefOperationalState based on Integer32"""
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
        *(("externala", 1),
          ("externalb", 2),
          ("internal", 5),
          ("portrefa", 3),
          ("portrefb", 4))
    )


_NodeSecondarySyncRefOperationalState_Type.__name__ = "Integer32"
_NodeSecondarySyncRefOperationalState_Object = MibScalar
nodeSecondarySyncRefOperationalState = _NodeSecondarySyncRefOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 88),
    _NodeSecondarySyncRefOperationalState_Type()
)
nodeSecondarySyncRefOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSecondarySyncRefOperationalState.setStatus("mandatory")


class _NodePrimaryPLLOperationalState_Type(Integer32):
    """Custom type nodePrimaryPLLOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_NodePrimaryPLLOperationalState_Type.__name__ = "Integer32"
_NodePrimaryPLLOperationalState_Object = MibScalar
nodePrimaryPLLOperationalState = _NodePrimaryPLLOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 89),
    _NodePrimaryPLLOperationalState_Type()
)
nodePrimaryPLLOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePrimaryPLLOperationalState.setStatus("mandatory")


class _NodeSecondaryPLLOperationalState_Type(Integer32):
    """Custom type nodeSecondaryPLLOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_NodeSecondaryPLLOperationalState_Type.__name__ = "Integer32"
_NodeSecondaryPLLOperationalState_Object = MibScalar
nodeSecondaryPLLOperationalState = _NodeSecondaryPLLOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 90),
    _NodeSecondaryPLLOperationalState_Type()
)
nodeSecondaryPLLOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSecondaryPLLOperationalState.setStatus("mandatory")


class _NodeExternalClockAOperationalState_Type(Integer32):
    """Custom type nodeExternalClockAOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ais", 2),
          ("los", 3))
    )


_NodeExternalClockAOperationalState_Type.__name__ = "Integer32"
_NodeExternalClockAOperationalState_Object = MibScalar
nodeExternalClockAOperationalState = _NodeExternalClockAOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 91),
    _NodeExternalClockAOperationalState_Type()
)
nodeExternalClockAOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeExternalClockAOperationalState.setStatus("mandatory")


class _NodeExternalClockBOperationalState_Type(Integer32):
    """Custom type nodeExternalClockBOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ais", 2),
          ("los", 3))
    )


_NodeExternalClockBOperationalState_Type.__name__ = "Integer32"
_NodeExternalClockBOperationalState_Object = MibScalar
nodeExternalClockBOperationalState = _NodeExternalClockBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 92),
    _NodeExternalClockBOperationalState_Type()
)
nodeExternalClockBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeExternalClockBOperationalState.setStatus("mandatory")


class _NodePortClockAOperationalState_Type(Integer32):
    """Custom type nodePortClockAOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_NodePortClockAOperationalState_Type.__name__ = "Integer32"
_NodePortClockAOperationalState_Object = MibScalar
nodePortClockAOperationalState = _NodePortClockAOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 93),
    _NodePortClockAOperationalState_Type()
)
nodePortClockAOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePortClockAOperationalState.setStatus("mandatory")


class _NodePortClockBOperationalState_Type(Integer32):
    """Custom type nodePortClockBOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_NodePortClockBOperationalState_Type.__name__ = "Integer32"
_NodePortClockBOperationalState_Object = MibScalar
nodePortClockBOperationalState = _NodePortClockBOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 94),
    _NodePortClockBOperationalState_Type()
)
nodePortClockBOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePortClockBOperationalState.setStatus("mandatory")


class _NodeExternalTimingSource_Type(Integer32):
    """Custom type nodeExternalTimingSource based on Integer32"""
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
        *(("externala", 1),
          ("externalb", 2),
          ("internal", 5),
          ("portrefa", 3),
          ("portrefb", 4))
    )


_NodeExternalTimingSource_Type.__name__ = "Integer32"
_NodeExternalTimingSource_Object = MibScalar
nodeExternalTimingSource = _NodeExternalTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 95),
    _NodeExternalTimingSource_Type()
)
nodeExternalTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeExternalTimingSource.setStatus("mandatory")


class _NodeSyncAutoRestore_Type(Integer32):
    """Custom type nodeSyncAutoRestore based on Integer32"""
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


_NodeSyncAutoRestore_Type.__name__ = "Integer32"
_NodeSyncAutoRestore_Object = MibScalar
nodeSyncAutoRestore = _NodeSyncAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 96),
    _NodeSyncAutoRestore_Type()
)
nodeSyncAutoRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSyncAutoRestore.setStatus("mandatory")


class _NodeExternalClockInterfaceType_Type(Integer32):
    """Custom type nodeExternalClockInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1bnc", 2),
          ("e1ww", 3),
          ("t1", 1))
    )


_NodeExternalClockInterfaceType_Type.__name__ = "Integer32"
_NodeExternalClockInterfaceType_Object = MibScalar
nodeExternalClockInterfaceType = _NodeExternalClockInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 3, 97),
    _NodeExternalClockInterfaceType_Type()
)
nodeExternalClockInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeExternalClockInterfaceType.setStatus("mandatory")
_Pport_ObjectIdentity = ObjectIdentity
pport = _Pport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 4)
)
_PportNumber_Type = Integer32
_PportNumber_Object = MibScalar
pportNumber = _PportNumber_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 1),
    _PportNumber_Type()
)
pportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportNumber.setStatus("mandatory")
_PportTable_Object = MibTable
pportTable = _PportTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2)
)
if mibBuilder.loadTexts:
    pportTable.setStatus("mandatory")
_PportEntry_Object = MibTableRow
pportEntry = _PportEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1)
)
pportEntry.setIndexNames(
    (0, "CASCADE-MIB", "pportSlotId"),
    (0, "CASCADE-MIB", "pportId"),
)
if mibBuilder.loadTexts:
    pportEntry.setStatus("mandatory")
_PportSlotId_Type = Integer32
_PportSlotId_Object = MibTableColumn
pportSlotId = _PportSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 1),
    _PportSlotId_Type()
)
pportSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportSlotId.setStatus("mandatory")
_PportId_Type = Integer32
_PportId_Object = MibTableColumn
pportId = _PportId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 2),
    _PportId_Type()
)
pportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportId.setStatus("mandatory")


class _PportAdminType_Type(Integer32):
    """Custom type pportAdminType based on Integer32"""
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("ads3-e3", 27),
          ("ads3-t3", 26),
          ("atmcs-1", 35),
          ("atmds3-1", 17),
          ("atme3-1", 18),
          ("cbr-atmiwu-1", 32),
          ("cbr-ds1-s-4", 28),
          ("cbr-ds1-us-4", 29),
          ("cbr-e1-s-4", 30),
          ("cbr-e1-us-4", 31),
          ("cp1", 5),
          ("dsx1-10", 12),
          ("e1-atm", 25),
          ("e1-pri-4", 20),
          ("fe1-1-30", 3),
          ("fe1-4-30", 8),
          ("fe3-1", 10),
          ("ft1-1-24", 2),
          ("ft1-4-24", 7),
          ("ft3-1", 9),
          ("hssi-1", 11),
          ("pri-4", 19),
          ("rs232-18", 13),
          ("rs232-8", 14),
          ("sft1-4-24", 21),
          ("st1-pri-4", 23),
          ("sut1-4-24", 22),
          ("t1-atm", 24),
          ("toc3-atm-4", 33),
          ("tstm1-atm-4", 34),
          ("ue1-4-30", 16),
          ("uio-6", 4),
          ("uio-8", 6),
          ("ut1-4-24", 15),
          ("v35-6", 1))
    )


_PportAdminType_Type.__name__ = "Integer32"
_PportAdminType_Object = MibTableColumn
pportAdminType = _PportAdminType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 3),
    _PportAdminType_Type()
)
pportAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAdminType.setStatus("mandatory")
_PportNumLport_Type = Integer32
_PportNumLport_Object = MibTableColumn
pportNumLport = _PportNumLport_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 4),
    _PportNumLport_Type()
)
pportNumLport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportNumLport.setStatus("mandatory")
_PportDataRate_Type = Integer32
_PportDataRate_Object = MibTableColumn
pportDataRate = _PportDataRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 5),
    _PportDataRate_Type()
)
pportDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDataRate.setStatus("mandatory")


class _PportType_Type(Integer32):
    """Custom type pportType based on Integer32"""
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("ads3-e3", 27),
          ("ads3-t3", 26),
          ("atm-1", 17),
          ("atmcs-1", 35),
          ("atme3-1", 18),
          ("cbr-atmiwu-1", 32),
          ("cbr-ds1-s-4", 28),
          ("cbr-ds1-us-4", 29),
          ("cbr-e1-s-4", 30),
          ("cbr-e1-us-4", 31),
          ("cp1", 5),
          ("dsx1-10", 12),
          ("e1-atm", 25),
          ("e1-pri-4", 20),
          ("fe1-1-30", 3),
          ("fe1-4-30", 8),
          ("fe3-1", 10),
          ("ft1-1-24", 2),
          ("ft1-4-24", 7),
          ("ft3-1", 9),
          ("hssi-1", 11),
          ("pri-4", 19),
          ("rs232-18", 13),
          ("rs232-8", 14),
          ("sft1-4-24", 21),
          ("st1-pri-4", 23),
          ("sut1-4-24", 22),
          ("t1-atm", 24),
          ("toc3-atm-4", 33),
          ("tstm1-atm-4", 34),
          ("ue1-4-30", 16),
          ("uio-6", 4),
          ("uio-8", 6),
          ("ut1-4-24", 15),
          ("v35-6", 1))
    )


_PportType_Type.__name__ = "Integer32"
_PportType_Object = MibTableColumn
pportType = _PportType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 6),
    _PportType_Type()
)
pportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportType.setStatus("mandatory")
_PportRecvClock_Type = Integer32
_PportRecvClock_Object = MibTableColumn
pportRecvClock = _PportRecvClock_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 7),
    _PportRecvClock_Type()
)
pportRecvClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportRecvClock.setStatus("mandatory")
_PportXmitClock_Type = Integer32
_PportXmitClock_Object = MibTableColumn
pportXmitClock = _PportXmitClock_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 8),
    _PportXmitClock_Type()
)
pportXmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportXmitClock.setStatus("mandatory")


class _PportAdminStatus_Type(Integer32):
    """Custom type pportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_PportAdminStatus_Type.__name__ = "Integer32"
_PportAdminStatus_Object = MibTableColumn
pportAdminStatus = _PportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 9),
    _PportAdminStatus_Type()
)
pportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAdminStatus.setStatus("mandatory")


class _PportOperStatus_Type(Integer32):
    """Custom type pportOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_PportOperStatus_Type.__name__ = "Integer32"
_PportOperStatus_Object = MibTableColumn
pportOperStatus = _PportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 10),
    _PportOperStatus_Type()
)
pportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOperStatus.setStatus("mandatory")


class _PportDs1LineType_Type(Integer32):
    """Custom type pportDs1LineType based on Integer32"""
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
        *(("d4", 1),
          ("e1-cas-crc4", 5),
          ("e1-cas-no-crc4", 6),
          ("e1-no-cas-crc4", 7),
          ("e1-no-cas-no-crc4", 8),
          ("esf-ansi", 2),
          ("esf-att-address-a", 3),
          ("esf-att-address-b", 9),
          ("esf-none", 4))
    )


_PportDs1LineType_Type.__name__ = "Integer32"
_PportDs1LineType_Object = MibTableColumn
pportDs1LineType = _PportDs1LineType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 11),
    _PportDs1LineType_Type()
)
pportDs1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDs1LineType.setStatus("mandatory")


class _PportDs1ZeroCoding_Type(Integer32):
    """Custom type pportDs1ZeroCoding based on Integer32"""
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
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3),
          ("jammed-bit", 4))
    )


_PportDs1ZeroCoding_Type.__name__ = "Integer32"
_PportDs1ZeroCoding_Object = MibTableColumn
pportDs1ZeroCoding = _PportDs1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 12),
    _PportDs1ZeroCoding_Type()
)
pportDs1ZeroCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDs1ZeroCoding.setStatus("mandatory")
_PportDs1LineBuildout_Type = Integer32
_PportDs1LineBuildout_Object = MibTableColumn
pportDs1LineBuildout = _PportDs1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 13),
    _PportDs1LineBuildout_Type()
)
pportDs1LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDs1LineBuildout.setStatus("mandatory")


class _PportDiagTestId_Type(Integer32):
    """Custom type pportDiagTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ds1-framer-local-loopback", 11),
          ("ds1-framer-remote-loopback", 13),
          ("ds1-line-local-loopback", 12),
          ("ds1-line-remote-loopback", 14),
          ("hssi-local-dte-loopback", 5),
          ("hssi-local-line", 6),
          ("hssi-remote-line-loopback", 7),
          ("v35-csu-loopback", 3),
          ("v35-sca-local-loopback", 1),
          ("v35-sca-remote-loopback", 2))
    )


_PportDiagTestId_Type.__name__ = "Integer32"
_PportDiagTestId_Object = MibTableColumn
pportDiagTestId = _PportDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 14),
    _PportDiagTestId_Type()
)
pportDiagTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDiagTestId.setStatus("mandatory")
_PportDiagTestRuns_Type = Integer32
_PportDiagTestRuns_Object = MibTableColumn
pportDiagTestRuns = _PportDiagTestRuns_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 15),
    _PportDiagTestRuns_Type()
)
pportDiagTestRuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDiagTestRuns.setStatus("mandatory")
_PportInOctets_Type = Counter32
_PportInOctets_Object = MibTableColumn
pportInOctets = _PportInOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 16),
    _PportInOctets_Type()
)
pportInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInOctets.setStatus("mandatory")
_PportInFrames_Type = Counter32
_PportInFrames_Object = MibTableColumn
pportInFrames = _PportInFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 17),
    _PportInFrames_Type()
)
pportInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInFrames.setStatus("mandatory")
_PportInDiscards_Type = Counter32
_PportInDiscards_Object = MibTableColumn
pportInDiscards = _PportInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 18),
    _PportInDiscards_Type()
)
pportInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInDiscards.setStatus("mandatory")
_PportInErrors_Type = Counter32
_PportInErrors_Object = MibTableColumn
pportInErrors = _PportInErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 19),
    _PportInErrors_Type()
)
pportInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInErrors.setStatus("mandatory")
_PportOutOctets_Type = Counter32
_PportOutOctets_Object = MibTableColumn
pportOutOctets = _PportOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 20),
    _PportOutOctets_Type()
)
pportOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutOctets.setStatus("mandatory")
_PportOutFrames_Type = Counter32
_PportOutFrames_Object = MibTableColumn
pportOutFrames = _PportOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 21),
    _PportOutFrames_Type()
)
pportOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutFrames.setStatus("mandatory")
_PportOutDiscards_Type = Counter32
_PportOutDiscards_Object = MibTableColumn
pportOutDiscards = _PportOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 22),
    _PportOutDiscards_Type()
)
pportOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutDiscards.setStatus("mandatory")
_PportOutErrors_Type = Counter32
_PportOutErrors_Object = MibTableColumn
pportOutErrors = _PportOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 23),
    _PportOutErrors_Type()
)
pportOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutErrors.setStatus("mandatory")


class _PportDiagState_Type(Integer32):
    """Custom type pportDiagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_PportDiagState_Type.__name__ = "Integer32"
_PportDiagState_Object = MibTableColumn
pportDiagState = _PportDiagState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 24),
    _PportDiagState_Type()
)
pportDiagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDiagState.setStatus("mandatory")
_PportDiagOptionStr_Type = OctetString
_PportDiagOptionStr_Object = MibTableColumn
pportDiagOptionStr = _PportDiagOptionStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 25),
    _PportDiagOptionStr_Type()
)
pportDiagOptionStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDiagOptionStr.setStatus("mandatory")
_PportDiagPassCount_Type = Integer32
_PportDiagPassCount_Object = MibTableColumn
pportDiagPassCount = _PportDiagPassCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 26),
    _PportDiagPassCount_Type()
)
pportDiagPassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDiagPassCount.setStatus("mandatory")
_PportDiagFailCount_Type = Integer32
_PportDiagFailCount_Object = MibTableColumn
pportDiagFailCount = _PportDiagFailCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 27),
    _PportDiagFailCount_Type()
)
pportDiagFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDiagFailCount.setStatus("mandatory")
_PportDiagResultStr_Type = DisplayString
_PportDiagResultStr_Object = MibTableColumn
pportDiagResultStr = _PportDiagResultStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 28),
    _PportDiagResultStr_Type()
)
pportDiagResultStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDiagResultStr.setStatus("mandatory")


class _PportLinkDownReason_Type(Integer32):
    """Custom type pportLinkDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768,
              65536)
        )
    )
    namedValues = NamedValues(
        *(("ber-threshold", 64),
          ("blue-alarm", 4),
          ("carrier-loss", 8),
          ("line-AIS", 2048),
          ("line-RFI", 16384),
          ("looped-back", 16),
          ("loss-of-cell-delination", 1024),
          ("loss-of-frame", 512),
          ("loss-of-pointer", 8192),
          ("loss-of-signal", 256),
          ("path-AIS", 4096),
          ("path-RFI", 32768),
          ("red-alarm", 1),
          ("signal-label-mismatch", 128),
          ("signal-label-undefined", 65536),
          ("yellow-alarm", 2))
    )


_PportLinkDownReason_Type.__name__ = "Integer32"
_PportLinkDownReason_Object = MibTableColumn
pportLinkDownReason = _PportLinkDownReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 29),
    _PportLinkDownReason_Type()
)
pportLinkDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportLinkDownReason.setStatus("mandatory")


class _PportInterface_Type(Integer32):
    """Custom type pportInterface based on Integer32"""
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
        *(("e1-coax", 6),
          ("e1-db", 7),
          ("eia449", 1),
          ("eia530", 3),
          ("eia530A", 4),
          ("multi-mode", 12),
          ("none", 8),
          ("sdh", 11),
          ("single-mode", 13),
          ("sonet", 10),
          ("v24", 9),
          ("v35", 5),
          ("x21", 2))
    )


_PportInterface_Type.__name__ = "Integer32"
_PportInterface_Object = MibTableColumn
pportInterface = _PportInterface_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 30),
    _PportInterface_Type()
)
pportInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInterface.setStatus("mandatory")


class _PportAdminInterface_Type(Integer32):
    """Custom type pportAdminInterface based on Integer32"""
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
        *(("e1-coax", 6),
          ("e1-db", 7),
          ("eia449", 1),
          ("eia530", 3),
          ("eia530A", 4),
          ("multi-mode", 12),
          ("none", 8),
          ("sdh", 11),
          ("single-mode", 13),
          ("sonet", 10),
          ("v24", 9),
          ("v35", 5),
          ("x21", 2))
    )


_PportAdminInterface_Type.__name__ = "Integer32"
_PportAdminInterface_Object = MibTableColumn
pportAdminInterface = _PportAdminInterface_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 31),
    _PportAdminInterface_Type()
)
pportAdminInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAdminInterface.setStatus("mandatory")


class _PportCellScramble_Type(Integer32):
    """Custom type pportCellScramble based on Integer32"""
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


_PportCellScramble_Type.__name__ = "Integer32"
_PportCellScramble_Object = MibTableColumn
pportCellScramble = _PportCellScramble_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 32),
    _PportCellScramble_Type()
)
pportCellScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportCellScramble.setStatus("mandatory")


class _PportCbitParity_Type(Integer32):
    """Custom type pportCbitParity based on Integer32"""
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


_PportCbitParity_Type.__name__ = "Integer32"
_PportCbitParity_Object = MibTableColumn
pportCbitParity = _PportCbitParity_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 33),
    _PportCbitParity_Type()
)
pportCbitParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportCbitParity.setStatus("mandatory")
_PportMaxBufferSize_Type = Integer32
_PportMaxBufferSize_Object = MibTableColumn
pportMaxBufferSize = _PportMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 34),
    _PportMaxBufferSize_Type()
)
pportMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportMaxBufferSize.setStatus("mandatory")
_PportPeakCellRate0_Type = Integer32
_PportPeakCellRate0_Object = MibTableColumn
pportPeakCellRate0 = _PportPeakCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 35),
    _PportPeakCellRate0_Type()
)
pportPeakCellRate0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate0.setStatus("mandatory")
_PportPeakCellRate1_Type = Integer32
_PportPeakCellRate1_Object = MibTableColumn
pportPeakCellRate1 = _PportPeakCellRate1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 36),
    _PportPeakCellRate1_Type()
)
pportPeakCellRate1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate1.setStatus("mandatory")
_PportPeakCellRate2_Type = Integer32
_PportPeakCellRate2_Object = MibTableColumn
pportPeakCellRate2 = _PportPeakCellRate2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 37),
    _PportPeakCellRate2_Type()
)
pportPeakCellRate2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate2.setStatus("mandatory")
_PportPeakCellRate3_Type = Integer32
_PportPeakCellRate3_Object = MibTableColumn
pportPeakCellRate3 = _PportPeakCellRate3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 38),
    _PportPeakCellRate3_Type()
)
pportPeakCellRate3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate3.setStatus("mandatory")
_PportPeakCellRate4_Type = Integer32
_PportPeakCellRate4_Object = MibTableColumn
pportPeakCellRate4 = _PportPeakCellRate4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 39),
    _PportPeakCellRate4_Type()
)
pportPeakCellRate4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate4.setStatus("mandatory")
_PportPeakCellRate5_Type = Integer32
_PportPeakCellRate5_Object = MibTableColumn
pportPeakCellRate5 = _PportPeakCellRate5_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 40),
    _PportPeakCellRate5_Type()
)
pportPeakCellRate5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate5.setStatus("mandatory")
_PportPeakCellRate6_Type = Integer32
_PportPeakCellRate6_Object = MibTableColumn
pportPeakCellRate6 = _PportPeakCellRate6_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 41),
    _PportPeakCellRate6_Type()
)
pportPeakCellRate6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate6.setStatus("mandatory")
_PportPeakCellRate7_Type = Integer32
_PportPeakCellRate7_Object = MibTableColumn
pportPeakCellRate7 = _PportPeakCellRate7_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 42),
    _PportPeakCellRate7_Type()
)
pportPeakCellRate7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPeakCellRate7.setStatus("mandatory")
_PportInCells_Type = Integer32
_PportInCells_Object = MibTableColumn
pportInCells = _PportInCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 43),
    _PportInCells_Type()
)
pportInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInCells.setStatus("mandatory")
_PportInErrorCells_Type = Integer32
_PportInErrorCells_Object = MibTableColumn
pportInErrorCells = _PportInErrorCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 44),
    _PportInErrorCells_Type()
)
pportInErrorCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportInErrorCells.setStatus("mandatory")
_PportOutCells_Type = Integer32
_PportOutCells_Object = MibTableColumn
pportOutCells = _PportOutCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 45),
    _PportOutCells_Type()
)
pportOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutCells.setStatus("mandatory")
_PportDs3LineBuildout_Type = Integer32
_PportDs3LineBuildout_Object = MibTableColumn
pportDs3LineBuildout = _PportDs3LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 46),
    _PportDs3LineBuildout_Type()
)
pportDs3LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDs3LineBuildout.setStatus("mandatory")
_PportSetDS0LoopUp_Type = Integer32
_PportSetDS0LoopUp_Object = MibTableColumn
pportSetDS0LoopUp = _PportSetDS0LoopUp_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 47),
    _PportSetDS0LoopUp_Type()
)
pportSetDS0LoopUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportSetDS0LoopUp.setStatus("mandatory")
_PportSetDS0LoopDown_Type = Integer32
_PportSetDS0LoopDown_Object = MibTableColumn
pportSetDS0LoopDown = _PportSetDS0LoopDown_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 48),
    _PportSetDS0LoopDown_Type()
)
pportSetDS0LoopDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportSetDS0LoopDown.setStatus("mandatory")
_PportDS0LoopUpStatus_Type = Integer32
_PportDS0LoopUpStatus_Object = MibTableColumn
pportDS0LoopUpStatus = _PportDS0LoopUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 49),
    _PportDS0LoopUpStatus_Type()
)
pportDS0LoopUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0LoopUpStatus.setStatus("mandatory")
_PportDS0LoopDownStatus_Type = Integer32
_PportDS0LoopDownStatus_Object = MibTableColumn
pportDS0LoopDownStatus = _PportDS0LoopDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 50),
    _PportDS0LoopDownStatus_Type()
)
pportDS0LoopDownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0LoopDownStatus.setStatus("mandatory")
_PportDS0LoopStatus_Type = Integer32
_PportDS0LoopStatus_Object = MibTableColumn
pportDS0LoopStatus = _PportDS0LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 51),
    _PportDS0LoopStatus_Type()
)
pportDS0LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0LoopStatus.setStatus("mandatory")


class _PportISDN_Type(Integer32):
    """Custom type pportISDN based on Integer32"""
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


_PportISDN_Type.__name__ = "Integer32"
_PportISDN_Object = MibTableColumn
pportISDN = _PportISDN_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 52),
    _PportISDN_Type()
)
pportISDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportISDN.setStatus("mandatory")


class _Pportdsx3LoopbackConfig_Type(Integer32):
    """Custom type pportdsx3LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx3LineLoop", 3),
          ("dsx3NoLoop", 1),
          ("dsx3PayloadLoop", 2))
    )


_Pportdsx3LoopbackConfig_Type.__name__ = "Integer32"
_Pportdsx3LoopbackConfig_Object = MibTableColumn
pportdsx3LoopbackConfig = _Pportdsx3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 53),
    _Pportdsx3LoopbackConfig_Type()
)
pportdsx3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportdsx3LoopbackConfig.setStatus("mandatory")


class _Pportdsx3SendCode_Type(Integer32):
    """Custom type pportdsx3SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dsx3SendLineCode", 2),
          ("dsx3SendNoCode", 1),
          ("dsx3SendResetCode", 4))
    )


_Pportdsx3SendCode_Type.__name__ = "Integer32"
_Pportdsx3SendCode_Object = MibTableColumn
pportdsx3SendCode = _Pportdsx3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 54),
    _Pportdsx3SendCode_Type()
)
pportdsx3SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportdsx3SendCode.setStatus("mandatory")


class _Pportdsx3LoopStatus_Type(Integer32):
    """Custom type pportdsx3LoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("noloop", 1),
          ("payloadloop", 2))
    )


_Pportdsx3LoopStatus_Type.__name__ = "Integer32"
_Pportdsx3LoopStatus_Object = MibTableColumn
pportdsx3LoopStatus = _Pportdsx3LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 55),
    _Pportdsx3LoopStatus_Type()
)
pportdsx3LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportdsx3LoopStatus.setStatus("mandatory")
_Pportdsx3FEACStatus_Type = Integer32
_Pportdsx3FEACStatus_Object = MibTableColumn
pportdsx3FEACStatus = _Pportdsx3FEACStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 56),
    _Pportdsx3FEACStatus_Type()
)
pportdsx3FEACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportdsx3FEACStatus.setStatus("mandatory")


class _Pportds1LoopbackConfig_Type(Integer32):
    """Custom type pportds1LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1LineLoop", 3),
          ("ds1NoLoop", 1),
          ("ds1PayloadLoop", 2))
    )


_Pportds1LoopbackConfig_Type.__name__ = "Integer32"
_Pportds1LoopbackConfig_Object = MibTableColumn
pportds1LoopbackConfig = _Pportds1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 57),
    _Pportds1LoopbackConfig_Type()
)
pportds1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1LoopbackConfig.setStatus("mandatory")


class _Pportds1SendCode_Type(Integer32):
    """Custom type pportds1SendCode based on Integer32"""
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
        *(("ds1SendFdlESFAnsiLineActuateLoop", 6),
          ("ds1SendFdlESFAnsiLineReleaseLoop", 7),
          ("ds1SendFdlESFAnsiPayloadActuateLoop", 8),
          ("ds1SendFdlESFAnsiPayloadReleaseLoop", 9),
          ("ds1SendFramedInbandLineActuateLoop", 2),
          ("ds1SendFramedInbandLineReleaseLoop", 3),
          ("ds1SendNoCode", 1),
          ("ds1SendUnframedInbandLineActuateLoop", 4),
          ("ds1SendUnframedInbandLineReleaseLoop", 5))
    )


_Pportds1SendCode_Type.__name__ = "Integer32"
_Pportds1SendCode_Object = MibTableColumn
pportds1SendCode = _Pportds1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 58),
    _Pportds1SendCode_Type()
)
pportds1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1SendCode.setStatus("mandatory")


class _Pportds1LoopStatus_Type(Integer32):
    """Custom type pportds1LoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("noloop", 1),
          ("payloadloop", 2))
    )


_Pportds1LoopStatus_Type.__name__ = "Integer32"
_Pportds1LoopStatus_Object = MibTableColumn
pportds1LoopStatus = _Pportds1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 59),
    _Pportds1LoopStatus_Type()
)
pportds1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportds1LoopStatus.setStatus("mandatory")


class _PportSetClkBkup_Type(Integer32):
    """Custom type pportSetClkBkup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClkBkup", 1),
          ("looptimedClkBkup", 2))
    )


_PportSetClkBkup_Type.__name__ = "Integer32"
_PportSetClkBkup_Object = MibTableColumn
pportSetClkBkup = _PportSetClkBkup_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 60),
    _PportSetClkBkup_Type()
)
pportSetClkBkup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportSetClkBkup.setStatus("mandatory")
_PportAtmIdleWord_Type = Integer32
_PportAtmIdleWord_Object = MibTableColumn
pportAtmIdleWord = _PportAtmIdleWord_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 61),
    _PportAtmIdleWord_Type()
)
pportAtmIdleWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAtmIdleWord.setStatus("mandatory")


class _PportAtmDisCardMode_Type(Integer32):
    """Custom type pportAtmDisCardMode based on Integer32"""
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
        *(("ansiInval", 1),
          ("ansiUnassignedInval", 2),
          ("atmFInvalid", 3),
          ("atmFUnassignedInval", 4),
          ("ccittIdle", 5),
          ("ccittUnassignedIdle", 6))
    )


_PportAtmDisCardMode_Type.__name__ = "Integer32"
_PportAtmDisCardMode_Object = MibTableColumn
pportAtmDisCardMode = _PportAtmDisCardMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 62),
    _PportAtmDisCardMode_Type()
)
pportAtmDisCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAtmDisCardMode.setStatus("mandatory")
_PportAtmLastUnconfiguredVpi_Type = Integer32
_PportAtmLastUnconfiguredVpi_Object = MibTableColumn
pportAtmLastUnconfiguredVpi = _PportAtmLastUnconfiguredVpi_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 63),
    _PportAtmLastUnconfiguredVpi_Type()
)
pportAtmLastUnconfiguredVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmLastUnconfiguredVpi.setStatus("mandatory")
_PportAtmLastUnconfiguredVci_Type = Integer32
_PportAtmLastUnconfiguredVci_Object = MibTableColumn
pportAtmLastUnconfiguredVci = _PportAtmLastUnconfiguredVci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 64),
    _PportAtmLastUnconfiguredVci_Type()
)
pportAtmLastUnconfiguredVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmLastUnconfiguredVci.setStatus("mandatory")
_PportAtmUnconfiguredCells_Type = Counter32
_PportAtmUnconfiguredCells_Object = MibTableColumn
pportAtmUnconfiguredCells = _PportAtmUnconfiguredCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 65),
    _PportAtmUnconfiguredCells_Type()
)
pportAtmUnconfiguredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmUnconfiguredCells.setStatus("mandatory")
_PportAtmNumBitsVCI_Type = Integer32
_PportAtmNumBitsVCI_Object = MibTableColumn
pportAtmNumBitsVCI = _PportAtmNumBitsVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 66),
    _PportAtmNumBitsVCI_Type()
)
pportAtmNumBitsVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmNumBitsVCI.setStatus("mandatory")
_PportAtmNumBitsVPI_Type = Integer32
_PportAtmNumBitsVPI_Object = MibTableColumn
pportAtmNumBitsVPI = _PportAtmNumBitsVPI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 67),
    _PportAtmNumBitsVPI_Type()
)
pportAtmNumBitsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmNumBitsVPI.setStatus("mandatory")


class _PportAtmInterfaceType_Type(Integer32):
    """Custom type pportAtmInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_PportAtmInterfaceType_Type.__name__ = "Integer32"
_PportAtmInterfaceType_Object = MibTableColumn
pportAtmInterfaceType = _PportAtmInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 68),
    _PportAtmInterfaceType_Type()
)
pportAtmInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAtmInterfaceType.setStatus("mandatory")


class _PportSonetSDHLoopbackConfig_Type(Integer32):
    """Custom type pportSonetSDHLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diagnosticsLoop", 3),
          ("lineLoop", 2),
          ("noLoop", 1))
    )


_PportSonetSDHLoopbackConfig_Type.__name__ = "Integer32"
_PportSonetSDHLoopbackConfig_Object = MibTableColumn
pportSonetSDHLoopbackConfig = _PportSonetSDHLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 69),
    _PportSonetSDHLoopbackConfig_Type()
)
pportSonetSDHLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportSonetSDHLoopbackConfig.setStatus("mandatory")


class _PportSonetSDHLoopStatus_Type(Integer32):
    """Custom type pportSonetSDHLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diagnosticsLoop", 3),
          ("lineLoop", 2),
          ("noLoop", 1))
    )


_PportSonetSDHLoopStatus_Type.__name__ = "Integer32"
_PportSonetSDHLoopStatus_Object = MibTableColumn
pportSonetSDHLoopStatus = _PportSonetSDHLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 70),
    _PportSonetSDHLoopStatus_Type()
)
pportSonetSDHLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportSonetSDHLoopStatus.setStatus("mandatory")
_PportOutDiscardsCell_Type = Counter32
_PportOutDiscardsCell_Object = MibTableColumn
pportOutDiscardsCell = _PportOutDiscardsCell_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 71),
    _PportOutDiscardsCell_Type()
)
pportOutDiscardsCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOutDiscardsCell.setStatus("mandatory")


class _PportAtmPlcp_Type(Integer32):
    """Custom type pportAtmPlcp based on Integer32"""
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


_PportAtmPlcp_Type.__name__ = "Integer32"
_PportAtmPlcp_Object = MibTableColumn
pportAtmPlcp = _PportAtmPlcp_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 72),
    _PportAtmPlcp_Type()
)
pportAtmPlcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAtmPlcp.setStatus("mandatory")
_PportCbrTargetClockMode_Type = Integer32
_PportCbrTargetClockMode_Object = MibTableColumn
pportCbrTargetClockMode = _PportCbrTargetClockMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 73),
    _PportCbrTargetClockMode_Type()
)
pportCbrTargetClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportCbrTargetClockMode.setStatus("mandatory")
_PportCbrCurrentClockMode_Type = Integer32
_PportCbrCurrentClockMode_Object = MibTableColumn
pportCbrCurrentClockMode = _PportCbrCurrentClockMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 74),
    _PportCbrCurrentClockMode_Type()
)
pportCbrCurrentClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportCbrCurrentClockMode.setStatus("mandatory")
_PportClockMasterChannel_Type = Integer32
_PportClockMasterChannel_Object = MibTableColumn
pportClockMasterChannel = _PportClockMasterChannel_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 75),
    _PportClockMasterChannel_Type()
)
pportClockMasterChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportClockMasterChannel.setStatus("mandatory")


class _PportFibreType_Type(Integer32):
    """Custom type pportFibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sonetMultiMode", 4),
          ("sonetShortSingleMode", 2))
    )


_PportFibreType_Type.__name__ = "Integer32"
_PportFibreType_Object = MibTableColumn
pportFibreType = _PportFibreType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 76),
    _PportFibreType_Type()
)
pportFibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportFibreType.setStatus("mandatory")


class _PportLaserStatus_Type(Integer32):
    """Custom type pportLaserStatus based on Integer32"""
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


_PportLaserStatus_Type.__name__ = "Integer32"
_PportLaserStatus_Object = MibTableColumn
pportLaserStatus = _PportLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 77),
    _PportLaserStatus_Type()
)
pportLaserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportLaserStatus.setStatus("mandatory")


class _PportMaxActiveVpiBits_Type(Integer32):
    """Custom type pportMaxActiveVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PportMaxActiveVpiBits_Type.__name__ = "Integer32"
_PportMaxActiveVpiBits_Object = MibTableColumn
pportMaxActiveVpiBits = _PportMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 78),
    _PportMaxActiveVpiBits_Type()
)
pportMaxActiveVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportMaxActiveVpiBits.setStatus("mandatory")
_PportBipErrorsThresh_Type = Integer32
_PportBipErrorsThresh_Object = MibTableColumn
pportBipErrorsThresh = _PportBipErrorsThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 79),
    _PportBipErrorsThresh_Type()
)
pportBipErrorsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBipErrorsThresh.setStatus("mandatory")
_PportBipSectionErrors_Type = Counter32
_PportBipSectionErrors_Object = MibTableColumn
pportBipSectionErrors = _PportBipSectionErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 80),
    _PportBipSectionErrors_Type()
)
pportBipSectionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBipSectionErrors.setStatus("mandatory")
_PportBipLineErrors_Type = Counter32
_PportBipLineErrors_Object = MibTableColumn
pportBipLineErrors = _PportBipLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 81),
    _PportBipLineErrors_Type()
)
pportBipLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBipLineErrors.setStatus("mandatory")
_PportBipPathErrors_Type = Counter32
_PportBipPathErrors_Object = MibTableColumn
pportBipPathErrors = _PportBipPathErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 82),
    _PportBipPathErrors_Type()
)
pportBipPathErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBipPathErrors.setStatus("mandatory")
_PportFebeErrors_Type = Counter32
_PportFebeErrors_Object = MibTableColumn
pportFebeErrors = _PportFebeErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 83),
    _PportFebeErrors_Type()
)
pportFebeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportFebeErrors.setStatus("mandatory")
_PportHcsErrors_Type = Counter32
_PportHcsErrors_Object = MibTableColumn
pportHcsErrors = _PportHcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 84),
    _PportHcsErrors_Type()
)
pportHcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportHcsErrors.setStatus("mandatory")
_PportHcsSevereErrors_Type = Counter32
_PportHcsSevereErrors_Object = MibTableColumn
pportHcsSevereErrors = _PportHcsSevereErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 85),
    _PportHcsSevereErrors_Type()
)
pportHcsSevereErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportHcsSevereErrors.setStatus("mandatory")
_PportCongestedReceivedCells_Type = Counter32
_PportCongestedReceivedCells_Object = MibTableColumn
pportCongestedReceivedCells = _PportCongestedReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 86),
    _PportCongestedReceivedCells_Type()
)
pportCongestedReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportCongestedReceivedCells.setStatus("mandatory")
_PportCongestedTransmittedCells_Type = Counter32
_PportCongestedTransmittedCells_Object = MibTableColumn
pportCongestedTransmittedCells = _PportCongestedTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 87),
    _PportCongestedTransmittedCells_Type()
)
pportCongestedTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportCongestedTransmittedCells.setStatus("mandatory")
_PportAtmLayerErroredReceivedCells_Type = Counter32
_PportAtmLayerErroredReceivedCells_Object = MibTableColumn
pportAtmLayerErroredReceivedCells = _PportAtmLayerErroredReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 88),
    _PportAtmLayerErroredReceivedCells_Type()
)
pportAtmLayerErroredReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmLayerErroredReceivedCells.setStatus("mandatory")
_PportAtmLayerErroredTransmittedCells_Type = Counter32
_PportAtmLayerErroredTransmittedCells_Object = MibTableColumn
pportAtmLayerErroredTransmittedCells = _PportAtmLayerErroredTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 89),
    _PportAtmLayerErroredTransmittedCells_Type()
)
pportAtmLayerErroredTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAtmLayerErroredTransmittedCells.setStatus("mandatory")
_PportDS0BitStuff_Type = Integer32
_PportDS0BitStuff_Object = MibTableColumn
pportDS0BitStuff = _PportDS0BitStuff_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 90),
    _PportDS0BitStuff_Type()
)
pportDS0BitStuff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0BitStuff.setStatus("mandatory")
_PportDS0BitErrorCount_Type = Integer32
_PportDS0BitErrorCount_Object = MibTableColumn
pportDS0BitErrorCount = _PportDS0BitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 91),
    _PportDS0BitErrorCount_Type()
)
pportDS0BitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0BitErrorCount.setStatus("mandatory")
_PportDS0BitErrorFreeSeconds_Type = Integer32
_PportDS0BitErrorFreeSeconds_Object = MibTableColumn
pportDS0BitErrorFreeSeconds = _PportDS0BitErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 92),
    _PportDS0BitErrorFreeSeconds_Type()
)
pportDS0BitErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0BitErrorFreeSeconds.setStatus("mandatory")
_PportDS0BitErroredSeconds_Type = Integer32
_PportDS0BitErroredSeconds_Object = MibTableColumn
pportDS0BitErroredSeconds = _PportDS0BitErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 93),
    _PportDS0BitErroredSeconds_Type()
)
pportDS0BitErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0BitErroredSeconds.setStatus("mandatory")
_PportDS0MidspanRepeaters_Type = Integer32
_PportDS0MidspanRepeaters_Object = MibTableColumn
pportDS0MidspanRepeaters = _PportDS0MidspanRepeaters_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 94),
    _PportDS0MidspanRepeaters_Type()
)
pportDS0MidspanRepeaters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0MidspanRepeaters.setStatus("mandatory")
_PportDS0TestPatternSync_Type = Integer32
_PportDS0TestPatternSync_Object = MibTableColumn
pportDS0TestPatternSync = _PportDS0TestPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 95),
    _PportDS0TestPatternSync_Type()
)
pportDS0TestPatternSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0TestPatternSync.setStatus("mandatory")
_PportDS0InjectBitError_Type = Integer32
_PportDS0InjectBitError_Object = MibTableColumn
pportDS0InjectBitError = _PportDS0InjectBitError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 96),
    _PportDS0InjectBitError_Type()
)
pportDS0InjectBitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0InjectBitError.setStatus("mandatory")
_PportDS0FarendLpbkType_Type = Integer32
_PportDS0FarendLpbkType_Object = MibTableColumn
pportDS0FarendLpbkType = _PportDS0FarendLpbkType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 97),
    _PportDS0FarendLpbkType_Type()
)
pportDS0FarendLpbkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0FarendLpbkType.setStatus("mandatory")
_PportDS0LpbkMode_Type = Integer32
_PportDS0LpbkMode_Object = MibTableColumn
pportDS0LpbkMode = _PportDS0LpbkMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 98),
    _PportDS0LpbkMode_Type()
)
pportDS0LpbkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0LpbkMode.setStatus("mandatory")
_PportDS0SwitchLpbkStart_Type = Integer32
_PportDS0SwitchLpbkStart_Object = MibTableColumn
pportDS0SwitchLpbkStart = _PportDS0SwitchLpbkStart_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 99),
    _PportDS0SwitchLpbkStart_Type()
)
pportDS0SwitchLpbkStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0SwitchLpbkStart.setStatus("mandatory")
_PportDS0SwitchLpbkEnd_Type = Integer32
_PportDS0SwitchLpbkEnd_Object = MibTableColumn
pportDS0SwitchLpbkEnd = _PportDS0SwitchLpbkEnd_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 100),
    _PportDS0SwitchLpbkEnd_Type()
)
pportDS0SwitchLpbkEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0SwitchLpbkEnd.setStatus("mandatory")
_PportDS0FarendDS0InLpbk_Type = Integer32
_PportDS0FarendDS0InLpbk_Object = MibTableColumn
pportDS0FarendDS0InLpbk = _PportDS0FarendDS0InLpbk_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 101),
    _PportDS0FarendDS0InLpbk_Type()
)
pportDS0FarendDS0InLpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportDS0FarendDS0InLpbk.setStatus("mandatory")
_PportDS0SendTestTraffic_Type = Integer32
_PportDS0SendTestTraffic_Object = MibTableColumn
pportDS0SendTestTraffic = _PportDS0SendTestTraffic_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 102),
    _PportDS0SendTestTraffic_Type()
)
pportDS0SendTestTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportDS0SendTestTraffic.setStatus("mandatory")


class _PportOc3LoopConfig_Type(Integer32):
    """Custom type pportOc3LoopConfig based on Integer32"""
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
        *(("oc3AtmLoop", 2),
          ("oc3NoLoop", 1),
          ("oc3ParPhyLoop", 4),
          ("oc3SerPhyLoop", 3))
    )


_PportOc3LoopConfig_Type.__name__ = "Integer32"
_PportOc3LoopConfig_Object = MibTableColumn
pportOc3LoopConfig = _PportOc3LoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 103),
    _PportOc3LoopConfig_Type()
)
pportOc3LoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportOc3LoopConfig.setStatus("mandatory")


class _PportOc3LoopStatus_Type(Integer32):
    """Custom type pportOc3LoopStatus based on Integer32"""
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
        *(("oc3AtmLoop", 2),
          ("oc3NoLoop", 1),
          ("oc3ParPhyLoop", 4),
          ("oc3SerPhyLoop", 3))
    )


_PportOc3LoopStatus_Type.__name__ = "Integer32"
_PportOc3LoopStatus_Object = MibTableColumn
pportOc3LoopStatus = _PportOc3LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 104),
    _PportOc3LoopStatus_Type()
)
pportOc3LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOc3LoopStatus.setStatus("mandatory")
_PportISDNIpBaseAddr_Type = IpAddress
_PportISDNIpBaseAddr_Object = MibTableColumn
pportISDNIpBaseAddr = _PportISDNIpBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 105),
    _PportISDNIpBaseAddr_Type()
)
pportISDNIpBaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportISDNIpBaseAddr.setStatus("mandatory")


class _PportSonetSTM1Scramble_Type(Integer32):
    """Custom type pportSonetSTM1Scramble based on Integer32"""
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


_PportSonetSTM1Scramble_Type.__name__ = "Integer32"
_PportSonetSTM1Scramble_Object = MibTableColumn
pportSonetSTM1Scramble = _PportSonetSTM1Scramble_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 106),
    _PportSonetSTM1Scramble_Type()
)
pportSonetSTM1Scramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportSonetSTM1Scramble.setStatus("mandatory")


class _PportEFCIMarking_Type(Integer32):
    """Custom type pportEFCIMarking based on Integer32"""
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


_PportEFCIMarking_Type.__name__ = "Integer32"
_PportEFCIMarking_Object = MibTableColumn
pportEFCIMarking = _PportEFCIMarking_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 107),
    _PportEFCIMarking_Type()
)
pportEFCIMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportEFCIMarking.setStatus("mandatory")


class _PportAtmQOSTransmitMode_Type(Integer32):
    """Custom type pportAtmQOSTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-priority", 1),
          ("weighted-round-robin", 2))
    )


_PportAtmQOSTransmitMode_Type.__name__ = "Integer32"
_PportAtmQOSTransmitMode_Object = MibTableColumn
pportAtmQOSTransmitMode = _PportAtmQOSTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 108),
    _PportAtmQOSTransmitMode_Type()
)
pportAtmQOSTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAtmQOSTransmitMode.setStatus("mandatory")


class _PportHECMode_Type(Integer32):
    """Custom type pportHECMode based on Integer32"""
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


_PportHECMode_Type.__name__ = "Integer32"
_PportHECMode_Object = MibTableColumn
pportHECMode = _PportHECMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 109),
    _PportHECMode_Type()
)
pportHECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportHECMode.setStatus("mandatory")
_PportISDNChannelStatus_Type = OctetString
_PportISDNChannelStatus_Object = MibTableColumn
pportISDNChannelStatus = _PportISDNChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 110),
    _PportISDNChannelStatus_Type()
)
pportISDNChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportISDNChannelStatus.setStatus("mandatory")


class _Pportds1FarEndLoopStatus_Type(Integer32):
    """Custom type pportds1FarEndLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fe-line-loop", 2),
          ("fe-noloop", 1),
          ("fe-payload-loop", 3))
    )


_Pportds1FarEndLoopStatus_Type.__name__ = "Integer32"
_Pportds1FarEndLoopStatus_Object = MibTableColumn
pportds1FarEndLoopStatus = _Pportds1FarEndLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 111),
    _Pportds1FarEndLoopStatus_Type()
)
pportds1FarEndLoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FarEndLoopStatus.setStatus("mandatory")


class _Pportds1FDLControl_Type(Integer32):
    """Custom type pportds1FDLControl based on Integer32"""
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


_Pportds1FDLControl_Type.__name__ = "Integer32"
_Pportds1FDLControl_Object = MibTableColumn
pportds1FDLControl = _Pportds1FDLControl_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 112),
    _Pportds1FDLControl_Type()
)
pportds1FDLControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FDLControl.setStatus("mandatory")


class _Pportds1FDLPrmXmit_Type(Integer32):
    """Custom type pportds1FDLPrmXmit based on Integer32"""
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


_Pportds1FDLPrmXmit_Type.__name__ = "Integer32"
_Pportds1FDLPrmXmit_Object = MibTableColumn
pportds1FDLPrmXmit = _Pportds1FDLPrmXmit_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 113),
    _Pportds1FDLPrmXmit_Type()
)
pportds1FDLPrmXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FDLPrmXmit.setStatus("mandatory")


class _Pportds1FDLPidXmit_Type(Integer32):
    """Custom type pportds1FDLPidXmit based on Integer32"""
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


_Pportds1FDLPidXmit_Type.__name__ = "Integer32"
_Pportds1FDLPidXmit_Object = MibTableColumn
pportds1FDLPidXmit = _Pportds1FDLPidXmit_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 114),
    _Pportds1FDLPidXmit_Type()
)
pportds1FDLPidXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FDLPidXmit.setStatus("mandatory")
_Pportds1FDLXmitPid_Type = OctetString
_Pportds1FDLXmitPid_Object = MibTableColumn
pportds1FDLXmitPid = _Pportds1FDLXmitPid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 115),
    _Pportds1FDLXmitPid_Type()
)
pportds1FDLXmitPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FDLXmitPid.setStatus("mandatory")
_Pportds1FDLRcvPid_Type = OctetString
_Pportds1FDLRcvPid_Object = MibTableColumn
pportds1FDLRcvPid = _Pportds1FDLRcvPid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 116),
    _Pportds1FDLRcvPid_Type()
)
pportds1FDLRcvPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportds1FDLRcvPid.setStatus("mandatory")
_Pportds1FDLRcvTsid_Type = OctetString
_Pportds1FDLRcvTsid_Object = MibTableColumn
pportds1FDLRcvTsid = _Pportds1FDLRcvTsid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 117),
    _Pportds1FDLRcvTsid_Type()
)
pportds1FDLRcvTsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FDLRcvTsid.setStatus("mandatory")


class _PportSonetSDHFramingMode_Type(Integer32):
    """Custom type pportSonetSDHFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_PportSonetSDHFramingMode_Type.__name__ = "Integer32"
_PportSonetSDHFramingMode_Object = MibTableColumn
pportSonetSDHFramingMode = _PportSonetSDHFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 118),
    _PportSonetSDHFramingMode_Type()
)
pportSonetSDHFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportSonetSDHFramingMode.setStatus("mandatory")


class _Pportds1InbandLoopType_Type(Integer32):
    """Custom type pportds1InbandLoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1CSU", 1),
          ("ds1NI", 2))
    )


_Pportds1InbandLoopType_Type.__name__ = "Integer32"
_Pportds1InbandLoopType_Object = MibTableColumn
pportds1InbandLoopType = _Pportds1InbandLoopType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 119),
    _Pportds1InbandLoopType_Type()
)
pportds1InbandLoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1InbandLoopType.setStatus("mandatory")


class _PportESFDataLinkStatus_Type(Integer32):
    """Custom type pportESFDataLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_PportESFDataLinkStatus_Type.__name__ = "Integer32"
_PportESFDataLinkStatus_Object = MibTableColumn
pportESFDataLinkStatus = _PportESFDataLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 120),
    _PportESFDataLinkStatus_Type()
)
pportESFDataLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportESFDataLinkStatus.setStatus("mandatory")


class _PportPMTcaId_Type(Integer32):
    """Custom type pportPMTcaId based on Integer32"""
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
              48)
        )
    )
    namedValues = NamedValues(
        *(("currentThresholdCSSP", 9),
          ("currentThresholdCVCPP", 29),
          ("currentThresholdCVCPPFE", 39),
          ("currentThresholdCVL", 1),
          ("currentThresholdCVP", 5),
          ("currentThresholdCVS", 11),
          ("currentThresholdESCPP", 30),
          ("currentThresholdESCPPFE", 40),
          ("currentThresholdESL", 2),
          ("currentThresholdESP", 6),
          ("currentThresholdESS", 12),
          ("currentThresholdESx", 14),
          ("currentThresholdSASCPP", 32),
          ("currentThresholdSASCPPFE", 42),
          ("currentThresholdSASP", 8),
          ("currentThresholdSESCPP", 31),
          ("currentThresholdSESCPPFE", 41),
          ("currentThresholdSESL", 3),
          ("currentThresholdSESP", 7),
          ("currentThresholdSESS", 13),
          ("currentThresholdUASCPP", 33),
          ("currentThresholdUASCPPFE", 43),
          ("currentThresholdUASL", 4),
          ("currentThresholdUASP", 10),
          ("dayThresholdCSSP", 23),
          ("dayThresholdCVCPP", 34),
          ("dayThresholdCVCPPFE", 44),
          ("dayThresholdCVL", 15),
          ("dayThresholdCVP", 19),
          ("dayThresholdCVS", 25),
          ("dayThresholdESCPP", 35),
          ("dayThresholdESCPPFE", 45),
          ("dayThresholdESL", 16),
          ("dayThresholdESP", 20),
          ("dayThresholdESS", 26),
          ("dayThresholdESx", 28),
          ("dayThresholdSASCPP", 37),
          ("dayThresholdSASCPPFE", 47),
          ("dayThresholdSASP", 22),
          ("dayThresholdSESCPP", 36),
          ("dayThresholdSESCPPFE", 46),
          ("dayThresholdSESL", 17),
          ("dayThresholdSESP", 21),
          ("dayThresholdSESS", 27),
          ("dayThresholdUASCPP", 38),
          ("dayThresholdUASCPPFE", 48),
          ("dayThresholdUASL", 18),
          ("dayThresholdUASP", 24))
    )


_PportPMTcaId_Type.__name__ = "Integer32"
_PportPMTcaId_Object = MibTableColumn
pportPMTcaId = _PportPMTcaId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 121),
    _PportPMTcaId_Type()
)
pportPMTcaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportPMTcaId.setStatus("mandatory")
_PportBchanTimerValue_Type = Integer32
_PportBchanTimerValue_Object = MibTableColumn
pportBchanTimerValue = _PportBchanTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 122),
    _PportBchanTimerValue_Type()
)
pportBchanTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBchanTimerValue.setStatus("mandatory")
_PportAAL5CRC32Error_Type = Counter32
_PportAAL5CRC32Error_Object = MibTableColumn
pportAAL5CRC32Error = _PportAAL5CRC32Error_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 123),
    _PportAAL5CRC32Error_Type()
)
pportAAL5CRC32Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAAL5CRC32Error.setStatus("mandatory")
_PportAAL5CPIError_Type = Counter32
_PportAAL5CPIError_Object = MibTableColumn
pportAAL5CPIError = _PportAAL5CPIError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 124),
    _PportAAL5CPIError_Type()
)
pportAAL5CPIError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAAL5CPIError.setStatus("mandatory")
_PportAAL5LengthError_Type = Counter32
_PportAAL5LengthError_Object = MibTableColumn
pportAAL5LengthError = _PportAAL5LengthError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 125),
    _PportAAL5LengthError_Type()
)
pportAAL5LengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAAL5LengthError.setStatus("mandatory")
_PportAAL5ReassemblyTimerError_Type = Counter32
_PportAAL5ReassemblyTimerError_Object = MibTableColumn
pportAAL5ReassemblyTimerError = _PportAAL5ReassemblyTimerError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 126),
    _PportAAL5ReassemblyTimerError_Type()
)
pportAAL5ReassemblyTimerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAAL5ReassemblyTimerError.setStatus("mandatory")
_PportAAL5MaxNrSegError_Type = Counter32
_PportAAL5MaxNrSegError_Object = MibTableColumn
pportAAL5MaxNrSegError = _PportAAL5MaxNrSegError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 127),
    _PportAAL5MaxNrSegError_Type()
)
pportAAL5MaxNrSegError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAAL5MaxNrSegError.setStatus("mandatory")


class _PportRedundancyArch_Type(Integer32):
    """Custom type pportRedundancyArch based on Integer32"""
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
        *(("aps-intracard", 2),
          ("aps-with-resilient-uni", 3),
          ("aps-with-trunk-backup", 4),
          ("disabled", 1))
    )


_PportRedundancyArch_Type.__name__ = "Integer32"
_PportRedundancyArch_Object = MibTableColumn
pportRedundancyArch = _PportRedundancyArch_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 128),
    _PportRedundancyArch_Type()
)
pportRedundancyArch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedundancyArch.setStatus("mandatory")


class _PportAPSadminDir_Type(Integer32):
    """Custom type pportAPSadminDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi-directional", 2),
          ("uni-directional", 1))
    )


_PportAPSadminDir_Type.__name__ = "Integer32"
_PportAPSadminDir_Object = MibTableColumn
pportAPSadminDir = _PportAPSadminDir_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 129),
    _PportAPSadminDir_Type()
)
pportAPSadminDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSadminDir.setStatus("mandatory")


class _PportAPSlineType_Type(Integer32):
    """Custom type pportAPSlineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection-line", 2),
          ("working-line", 1))
    )


_PportAPSlineType_Type.__name__ = "Integer32"
_PportAPSlineType_Object = MibTableColumn
pportAPSlineType = _PportAPSlineType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 130),
    _PportAPSlineType_Type()
)
pportAPSlineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSlineType.setStatus("mandatory")


class _PportAPSrevertiveMode_Type(Integer32):
    """Custom type pportAPSrevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 2),
          ("revertive", 1))
    )


_PportAPSrevertiveMode_Type.__name__ = "Integer32"
_PportAPSrevertiveMode_Object = MibTableColumn
pportAPSrevertiveMode = _PportAPSrevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 131),
    _PportAPSrevertiveMode_Type()
)
pportAPSrevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSrevertiveMode.setStatus("mandatory")


class _PportAPSpairedSlotId_Type(Integer32):
    """Custom type pportAPSpairedSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PportAPSpairedSlotId_Type.__name__ = "Integer32"
_PportAPSpairedSlotId_Object = MibTableColumn
pportAPSpairedSlotId = _PportAPSpairedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 132),
    _PportAPSpairedSlotId_Type()
)
pportAPSpairedSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSpairedSlotId.setStatus("mandatory")
_PportAPSpairedPportId_Type = Integer32
_PportAPSpairedPportId_Object = MibTableColumn
pportAPSpairedPportId = _PportAPSpairedPportId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 133),
    _PportAPSpairedPportId_Type()
)
pportAPSpairedPportId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSpairedPportId.setStatus("mandatory")


class _PportAPSsfBerThresh_Type(Integer32):
    """Custom type pportAPSsfBerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_PportAPSsfBerThresh_Type.__name__ = "Integer32"
_PportAPSsfBerThresh_Object = MibTableColumn
pportAPSsfBerThresh = _PportAPSsfBerThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 134),
    _PportAPSsfBerThresh_Type()
)
pportAPSsfBerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSsfBerThresh.setStatus("mandatory")


class _PportAPSsdBerThresh_Type(Integer32):
    """Custom type pportAPSsdBerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 9),
    )


_PportAPSsdBerThresh_Type.__name__ = "Integer32"
_PportAPSsdBerThresh_Object = MibTableColumn
pportAPSsdBerThresh = _PportAPSsdBerThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 135),
    _PportAPSsdBerThresh_Type()
)
pportAPSsdBerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSsdBerThresh.setStatus("mandatory")


class _PportAPSwtrPeriod_Type(Integer32):
    """Custom type pportAPSwtrPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_PportAPSwtrPeriod_Type.__name__ = "Integer32"
_PportAPSwtrPeriod_Object = MibTableColumn
pportAPSwtrPeriod = _PportAPSwtrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 136),
    _PportAPSwtrPeriod_Type()
)
pportAPSwtrPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSwtrPeriod.setStatus("mandatory")


class _PportAPSprotectionLineState_Type(Integer32):
    """Custom type pportAPSprotectionLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("released", 1),
          ("selected", 2))
    )


_PportAPSprotectionLineState_Type.__name__ = "Integer32"
_PportAPSprotectionLineState_Object = MibTableColumn
pportAPSprotectionLineState = _PportAPSprotectionLineState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 137),
    _PportAPSprotectionLineState_Type()
)
pportAPSprotectionLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAPSprotectionLineState.setStatus("mandatory")


class _PportAPSxCommand_Type(Integer32):
    """Custom type pportAPSxCommand based on Integer32"""
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
        *(("clear", 1),
          ("exercise", 7),
          ("forced-switch-p-to-w", 4),
          ("forced-switch-w-to-p", 3),
          ("lockout-protection", 2),
          ("manual-switch-p-to-w", 6),
          ("manual-switch-w-to-p", 5))
    )


_PportAPSxCommand_Type.__name__ = "Integer32"
_PportAPSxCommand_Object = MibTableColumn
pportAPSxCommand = _PportAPSxCommand_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 138),
    _PportAPSxCommand_Type()
)
pportAPSxCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportAPSxCommand.setStatus("mandatory")


class _PportAPSconfigStatus_Type(Integer32):
    """Custom type pportAPSconfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("not-configured", 1),
          ("valid", 2))
    )


_PportAPSconfigStatus_Type.__name__ = "Integer32"
_PportAPSconfigStatus_Object = MibTableColumn
pportAPSconfigStatus = _PportAPSconfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 139),
    _PportAPSconfigStatus_Type()
)
pportAPSconfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAPSconfigStatus.setStatus("mandatory")


class _PportAPSOperRxStatus_Type(Integer32):
    """Custom type pportAPSOperRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_PportAPSOperRxStatus_Type.__name__ = "Integer32"
_PportAPSOperRxStatus_Object = MibTableColumn
pportAPSOperRxStatus = _PportAPSOperRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 140),
    _PportAPSOperRxStatus_Type()
)
pportAPSOperRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAPSOperRxStatus.setStatus("mandatory")


class _PportBertPattern_Type(Integer32):
    """Custom type pportBertPattern based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 2),
          ("allZeros", 1),
          ("oneOf8", 5),
          ("oneOneZeroZero", 4),
          ("oneZero", 3),
          ("qRSS", 7),
          ("threeOf24", 6),
          ("user1Byte", 8),
          ("user2Byte", 9),
          ("user3Byte", 10),
          ("user4Byte", 11))
    )


_PportBertPattern_Type.__name__ = "Integer32"
_PportBertPattern_Object = MibTableColumn
pportBertPattern = _PportBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 141),
    _PportBertPattern_Type()
)
pportBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBertPattern.setStatus("mandatory")
_PportBertUserBytes_Type = Integer32
_PportBertUserBytes_Object = MibTableColumn
pportBertUserBytes = _PportBertUserBytes_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 142),
    _PportBertUserBytes_Type()
)
pportBertUserBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBertUserBytes.setStatus("mandatory")


class _PportBertErrorRate_Type(Integer32):
    """Custom type pportBertErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tenMinusSix", 3),
          ("tenMinusThree", 2))
    )


_PportBertErrorRate_Type.__name__ = "Integer32"
_PportBertErrorRate_Object = MibTableColumn
pportBertErrorRate = _PportBertErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 143),
    _PportBertErrorRate_Type()
)
pportBertErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBertErrorRate.setStatus("mandatory")


class _PportBertCommand_Type(Integer32):
    """Custom type pportBertCommand based on Integer32"""
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
        *(("clearCounters", 3),
          ("injectError", 4),
          ("start", 1),
          ("stop", 2))
    )


_PportBertCommand_Type.__name__ = "Integer32"
_PportBertCommand_Object = MibTableColumn
pportBertCommand = _PportBertCommand_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 144),
    _PportBertCommand_Type()
)
pportBertCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportBertCommand.setStatus("mandatory")


class _PportBertStatus_Type(Integer32):
    """Custom type pportBertStatus based on Integer32"""
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
        *(("inFrame", 4),
          ("outOfFrame", 3),
          ("unavailable", 2),
          ("unused", 1))
    )


_PportBertStatus_Type.__name__ = "Integer32"
_PportBertStatus_Object = MibTableColumn
pportBertStatus = _PportBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 145),
    _PportBertStatus_Type()
)
pportBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBertStatus.setStatus("mandatory")
_PportBertBitCount_Type = Gauge32
_PportBertBitCount_Object = MibTableColumn
pportBertBitCount = _PportBertBitCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 146),
    _PportBertBitCount_Type()
)
pportBertBitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBertBitCount.setStatus("mandatory")
_PportBertErrorCount_Type = Gauge32
_PportBertErrorCount_Object = MibTableColumn
pportBertErrorCount = _PportBertErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 147),
    _PportBertErrorCount_Type()
)
pportBertErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportBertErrorCount.setStatus("mandatory")


class _Pportds1FELoopbackControl_Type(Integer32):
    """Custom type pportds1FELoopbackControl based on Integer32"""
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


_Pportds1FELoopbackControl_Type.__name__ = "Integer32"
_Pportds1FELoopbackControl_Object = MibTableColumn
pportds1FELoopbackControl = _Pportds1FELoopbackControl_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 148),
    _Pportds1FELoopbackControl_Type()
)
pportds1FELoopbackControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1FELoopbackControl.setStatus("mandatory")
_PportFT1DS0s_Type = DisplayString
_PportFT1DS0s_Object = MibTableColumn
pportFT1DS0s = _PportFT1DS0s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 149),
    _PportFT1DS0s_Type()
)
pportFT1DS0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportFT1DS0s.setStatus("mandatory")
_PportIMUXCnt_Type = Integer32
_PportIMUXCnt_Object = MibTableColumn
pportIMUXCnt = _PportIMUXCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 150),
    _PportIMUXCnt_Type()
)
pportIMUXCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportIMUXCnt.setStatus("mandatory")


class _Pportds1PMConfigThresh_Type(Integer32):
    """Custom type pportds1PMConfigThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itu-g826", 2),
          ("rfc1406", 1))
    )


_Pportds1PMConfigThresh_Type.__name__ = "Integer32"
_Pportds1PMConfigThresh_Object = MibTableColumn
pportds1PMConfigThresh = _Pportds1PMConfigThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 151),
    _Pportds1PMConfigThresh_Type()
)
pportds1PMConfigThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportds1PMConfigThresh.setStatus("mandatory")


class _PportIdleCellType_Type(Integer32):
    """Custom type pportIdleCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmforum", 1),
          ("itu", 2))
    )


_PportIdleCellType_Type.__name__ = "Integer32"
_PportIdleCellType_Object = MibTableColumn
pportIdleCellType = _PportIdleCellType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 152),
    _PportIdleCellType_Type()
)
pportIdleCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportIdleCellType.setStatus("mandatory")


class _PportATMTcaInHECErrorUAlertPeriod_Type(Integer32):
    """Custom type pportATMTcaInHECErrorUAlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaInHECErrorUAlertPeriod_Object = MibTableColumn
pportATMTcaInHECErrorUAlertPeriod = _PportATMTcaInHECErrorUAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 153),
    _PportATMTcaInHECErrorUAlertPeriod_Type()
)
pportATMTcaInHECErrorUAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaInHECErrorUAlertPeriod.setStatus("mandatory")


class _PportATMTcaInHECErrorUThresh_Type(Integer32):
    """Custom type pportATMTcaInHECErrorUThresh based on Integer32"""
    defaultValue = 1


_PportATMTcaInHECErrorUThresh_Object = MibTableColumn
pportATMTcaInHECErrorUThresh = _PportATMTcaInHECErrorUThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 154),
    _PportATMTcaInHECErrorUThresh_Type()
)
pportATMTcaInHECErrorUThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaInHECErrorUThresh.setStatus("mandatory")


class _PportATMTcaEBufOverflowCBRAlertPeriod_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowCBRAlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaEBufOverflowCBRAlertPeriod_Object = MibTableColumn
pportATMTcaEBufOverflowCBRAlertPeriod = _PportATMTcaEBufOverflowCBRAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 155),
    _PportATMTcaEBufOverflowCBRAlertPeriod_Type()
)
pportATMTcaEBufOverflowCBRAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowCBRAlertPeriod.setStatus("mandatory")


class _PportATMTcaEBufOverflowCBRThresh_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowCBRThresh based on Integer32"""
    defaultValue = 1


_PportATMTcaEBufOverflowCBRThresh_Object = MibTableColumn
pportATMTcaEBufOverflowCBRThresh = _PportATMTcaEBufOverflowCBRThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 156),
    _PportATMTcaEBufOverflowCBRThresh_Type()
)
pportATMTcaEBufOverflowCBRThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowCBRThresh.setStatus("mandatory")


class _PportATMTcaEBufOverflowABRAlertPeriod_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowABRAlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaEBufOverflowABRAlertPeriod_Object = MibTableColumn
pportATMTcaEBufOverflowABRAlertPeriod = _PportATMTcaEBufOverflowABRAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 157),
    _PportATMTcaEBufOverflowABRAlertPeriod_Type()
)
pportATMTcaEBufOverflowABRAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowABRAlertPeriod.setStatus("mandatory")


class _PportATMTcaEBufOverflowABRThresh_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowABRThresh based on Integer32"""
    defaultValue = 1


_PportATMTcaEBufOverflowABRThresh_Object = MibTableColumn
pportATMTcaEBufOverflowABRThresh = _PportATMTcaEBufOverflowABRThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 158),
    _PportATMTcaEBufOverflowABRThresh_Type()
)
pportATMTcaEBufOverflowABRThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowABRThresh.setStatus("mandatory")


class _PportATMTcaEBufOverflowVBR1AlertPeriod_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowVBR1AlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaEBufOverflowVBR1AlertPeriod_Object = MibTableColumn
pportATMTcaEBufOverflowVBR1AlertPeriod = _PportATMTcaEBufOverflowVBR1AlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 159),
    _PportATMTcaEBufOverflowVBR1AlertPeriod_Type()
)
pportATMTcaEBufOverflowVBR1AlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowVBR1AlertPeriod.setStatus("mandatory")


class _PportATMTcaEBufOverflowVBR1Thresh_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowVBR1Thresh based on Integer32"""
    defaultValue = 1


_PportATMTcaEBufOverflowVBR1Thresh_Object = MibTableColumn
pportATMTcaEBufOverflowVBR1Thresh = _PportATMTcaEBufOverflowVBR1Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 160),
    _PportATMTcaEBufOverflowVBR1Thresh_Type()
)
pportATMTcaEBufOverflowVBR1Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowVBR1Thresh.setStatus("mandatory")


class _PportATMTcaEBufOverflowVBR2AlertPeriod_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowVBR2AlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaEBufOverflowVBR2AlertPeriod_Object = MibTableColumn
pportATMTcaEBufOverflowVBR2AlertPeriod = _PportATMTcaEBufOverflowVBR2AlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 161),
    _PportATMTcaEBufOverflowVBR2AlertPeriod_Type()
)
pportATMTcaEBufOverflowVBR2AlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowVBR2AlertPeriod.setStatus("mandatory")


class _PportATMTcaEBufOverflowVBR2Thresh_Type(Integer32):
    """Custom type pportATMTcaEBufOverflowVBR2Thresh based on Integer32"""
    defaultValue = 1


_PportATMTcaEBufOverflowVBR2Thresh_Object = MibTableColumn
pportATMTcaEBufOverflowVBR2Thresh = _PportATMTcaEBufOverflowVBR2Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 162),
    _PportATMTcaEBufOverflowVBR2Thresh_Type()
)
pportATMTcaEBufOverflowVBR2Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEBufOverflowVBR2Thresh.setStatus("mandatory")


class _PportATMTcaInFramerFIFOOverflowAlertPeriod_Type(Integer32):
    """Custom type pportATMTcaInFramerFIFOOverflowAlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaInFramerFIFOOverflowAlertPeriod_Object = MibTableColumn
pportATMTcaInFramerFIFOOverflowAlertPeriod = _PportATMTcaInFramerFIFOOverflowAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 163),
    _PportATMTcaInFramerFIFOOverflowAlertPeriod_Type()
)
pportATMTcaInFramerFIFOOverflowAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaInFramerFIFOOverflowAlertPeriod.setStatus("mandatory")


class _PportATMTcaInFramerFIFOOverflowThresh_Type(Integer32):
    """Custom type pportATMTcaInFramerFIFOOverflowThresh based on Integer32"""
    defaultValue = 1


_PportATMTcaInFramerFIFOOverflowThresh_Object = MibTableColumn
pportATMTcaInFramerFIFOOverflowThresh = _PportATMTcaInFramerFIFOOverflowThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 164),
    _PportATMTcaInFramerFIFOOverflowThresh_Type()
)
pportATMTcaInFramerFIFOOverflowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaInFramerFIFOOverflowThresh.setStatus("mandatory")


class _PportATMTcaELookupFailureAlertPeriod_Type(Integer32):
    """Custom type pportATMTcaELookupFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_PportATMTcaELookupFailureAlertPeriod_Object = MibTableColumn
pportATMTcaELookupFailureAlertPeriod = _PportATMTcaELookupFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 165),
    _PportATMTcaELookupFailureAlertPeriod_Type()
)
pportATMTcaELookupFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaELookupFailureAlertPeriod.setStatus("mandatory")


class _PportATMTcaELookupFailureThresh_Type(Integer32):
    """Custom type pportATMTcaELookupFailureThresh based on Integer32"""
    defaultValue = 1


_PportATMTcaELookupFailureThresh_Object = MibTableColumn
pportATMTcaELookupFailureThresh = _PportATMTcaELookupFailureThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 166),
    _PportATMTcaELookupFailureThresh_Type()
)
pportATMTcaELookupFailureThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaELookupFailureThresh.setStatus("mandatory")
_PportATMTcaEnable_Type = Integer32
_PportATMTcaEnable_Object = MibTableColumn
pportATMTcaEnable = _PportATMTcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 167),
    _PportATMTcaEnable_Type()
)
pportATMTcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaEnable.setStatus("mandatory")


class _PportATMTcaId_Type(Integer32):
    """Custom type pportATMTcaId based on Integer32"""
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
        *(("egressABRBufferOverflowC", 3),
          ("egressCBRBufferOverflowC", 2),
          ("egressLookupFailureC", 7),
          ("egressVBR1BufferOverflowC", 4),
          ("egressVBR2BufferOverflowC", 5),
          ("ingressFramerFIFOOverflowC", 6),
          ("ingressHECErrorUThresholdC", 1))
    )


_PportATMTcaId_Type.__name__ = "Integer32"
_PportATMTcaId_Object = MibTableColumn
pportATMTcaId = _PportATMTcaId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 168),
    _PportATMTcaId_Type()
)
pportATMTcaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportATMTcaId.setStatus("mandatory")


class _PportFethAdminMacAddr_Type(OctetString):
    """Custom type pportFethAdminMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PportFethAdminMacAddr_Type.__name__ = "OctetString"
_PportFethAdminMacAddr_Object = MibTableColumn
pportFethAdminMacAddr = _PportFethAdminMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 169),
    _PportFethAdminMacAddr_Type()
)
pportFethAdminMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportFethAdminMacAddr.setStatus("mandatory")


class _PportFethOperMacAddr_Type(OctetString):
    """Custom type pportFethOperMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PportFethOperMacAddr_Type.__name__ = "OctetString"
_PportFethOperMacAddr_Object = MibTableColumn
pportFethOperMacAddr = _PportFethOperMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 170),
    _PportFethOperMacAddr_Type()
)
pportFethOperMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportFethOperMacAddr.setStatus("mandatory")


class _PportConfigAlarmSoakTime_Type(Integer32):
    """Custom type pportConfigAlarmSoakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PportConfigAlarmSoakTime_Type.__name__ = "Integer32"
_PportConfigAlarmSoakTime_Object = MibTableColumn
pportConfigAlarmSoakTime = _PportConfigAlarmSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 171),
    _PportConfigAlarmSoakTime_Type()
)
pportConfigAlarmSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportConfigAlarmSoakTime.setStatus("mandatory")


class _PportConfigAlarmClearTime_Type(Integer32):
    """Custom type pportConfigAlarmClearTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PportConfigAlarmClearTime_Type.__name__ = "Integer32"
_PportConfigAlarmClearTime_Object = MibTableColumn
pportConfigAlarmClearTime = _PportConfigAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 172),
    _PportConfigAlarmClearTime_Type()
)
pportConfigAlarmClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportConfigAlarmClearTime.setStatus("mandatory")


class _PportFethPortCapability_Type(Integer32):
    """Custom type pportFethPortCapability based on Integer32"""
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
        *(("fullDuplex100Mbps", 1),
          ("fullDuplex10Mbps", 3),
          ("halfDuplex100Mbps", 2),
          ("halfDuplex10Mbps", 4))
    )


_PportFethPortCapability_Type.__name__ = "Integer32"
_PportFethPortCapability_Object = MibTableColumn
pportFethPortCapability = _PportFethPortCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 173),
    _PportFethPortCapability_Type()
)
pportFethPortCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportFethPortCapability.setStatus("mandatory")
_PportVpshapingDiscardCellCount_Type = Integer32
_PportVpshapingDiscardCellCount_Object = MibTableColumn
pportVpshapingDiscardCellCount = _PportVpshapingDiscardCellCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 2, 1, 174),
    _PportVpshapingDiscardCellCount_Type()
)
pportVpshapingDiscardCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportVpshapingDiscardCellCount.setStatus("mandatory")
_PportTrafficShaperTable_Object = MibTable
pportTrafficShaperTable = _PportTrafficShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3)
)
if mibBuilder.loadTexts:
    pportTrafficShaperTable.setStatus("mandatory")
_PportTrafficShaperEntry_Object = MibTableRow
pportTrafficShaperEntry = _PportTrafficShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1)
)
pportTrafficShaperEntry.setIndexNames(
    (0, "CASCADE-MIB", "pportSlotId"),
    (0, "CASCADE-MIB", "pportId"),
    (0, "CASCADE-MIB", "pportTrafficShaperIndex"),
)
if mibBuilder.loadTexts:
    pportTrafficShaperEntry.setStatus("mandatory")


class _PportTrafficShaperIndex_Type(Integer32):
    """Custom type pportTrafficShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PportTrafficShaperIndex_Type.__name__ = "Integer32"
_PportTrafficShaperIndex_Object = MibTableColumn
pportTrafficShaperIndex = _PportTrafficShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 1),
    _PportTrafficShaperIndex_Type()
)
pportTrafficShaperIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperIndex.setStatus("mandatory")


class _PportTrafficShaperPriority_Type(Integer32):
    """Custom type pportTrafficShaperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PportTrafficShaperPriority_Type.__name__ = "Integer32"
_PportTrafficShaperPriority_Object = MibTableColumn
pportTrafficShaperPriority = _PportTrafficShaperPriority_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 2),
    _PportTrafficShaperPriority_Type()
)
pportTrafficShaperPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperPriority.setStatus("mandatory")


class _PportTrafficShaperCellRatioDividend_Type(Integer32):
    """Custom type pportTrafficShaperCellRatioDividend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PportTrafficShaperCellRatioDividend_Type.__name__ = "Integer32"
_PportTrafficShaperCellRatioDividend_Object = MibTableColumn
pportTrafficShaperCellRatioDividend = _PportTrafficShaperCellRatioDividend_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 3),
    _PportTrafficShaperCellRatioDividend_Type()
)
pportTrafficShaperCellRatioDividend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperCellRatioDividend.setStatus("mandatory")


class _PportTrafficShaperCellRatioDivisor_Type(Integer32):
    """Custom type pportTrafficShaperCellRatioDivisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PportTrafficShaperCellRatioDivisor_Type.__name__ = "Integer32"
_PportTrafficShaperCellRatioDivisor_Object = MibTableColumn
pportTrafficShaperCellRatioDivisor = _PportTrafficShaperCellRatioDivisor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 4),
    _PportTrafficShaperCellRatioDivisor_Type()
)
pportTrafficShaperCellRatioDivisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperCellRatioDivisor.setStatus("mandatory")


class _PportTrafficShaperPeak_Type(Integer32):
    """Custom type pportTrafficShaperPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PportTrafficShaperPeak_Type.__name__ = "Integer32"
_PportTrafficShaperPeak_Object = MibTableColumn
pportTrafficShaperPeak = _PportTrafficShaperPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 5),
    _PportTrafficShaperPeak_Type()
)
pportTrafficShaperPeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperPeak.setStatus("mandatory")


class _PportTrafficShaperCredit_Type(Integer32):
    """Custom type pportTrafficShaperCredit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PportTrafficShaperCredit_Type.__name__ = "Integer32"
_PportTrafficShaperCredit_Object = MibTableColumn
pportTrafficShaperCredit = _PportTrafficShaperCredit_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 4, 3, 1, 6),
    _PportTrafficShaperCredit_Type()
)
pportTrafficShaperCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportTrafficShaperCredit.setStatus("mandatory")
_Lport_ObjectIdentity = ObjectIdentity
lport = _Lport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 5)
)
_LportTable_Object = MibTable
lportTable = _LportTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lportTable.setStatus("mandatory")
_LportEntry_Object = MibTableRow
lportEntry = _LportEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1)
)
lportEntry.setIndexNames(
    (0, "CASCADE-MIB", "lportIfIndex"),
)
if mibBuilder.loadTexts:
    lportEntry.setStatus("mandatory")
_LportIfIndex_Type = Index
_LportIfIndex_Object = MibTableColumn
lportIfIndex = _LportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 1),
    _LportIfIndex_Type()
)
lportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportIfIndex.setStatus("mandatory")
_LportSlotId_Type = Integer32
_LportSlotId_Object = MibTableColumn
lportSlotId = _LportSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 2),
    _LportSlotId_Type()
)
lportSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSlotId.setStatus("mandatory")
_LportPportId_Type = Integer32
_LportPportId_Object = MibTableColumn
lportPportId = _LportPportId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 3),
    _LportPportId_Type()
)
lportPportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportPportId.setStatus("mandatory")
_LportId_Type = Integer32
_LportId_Object = MibTableColumn
lportId = _LportId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 4),
    _LportId_Type()
)
lportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportId.setStatus("mandatory")


class _LportLink_Type(Integer32):
    """Custom type lportLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("trk", 1))
    )


_LportLink_Type.__name__ = "Integer32"
_LportLink_Object = MibTableColumn
lportLink = _LportLink_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 5),
    _LportLink_Type()
)
lportLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportLink.setStatus("mandatory")


class _LportProtocol_Type(Integer32):
    """Custom type lportProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("atm", 4),
          ("atmAAL1", 10),
          ("dirmgmttrk", 7),
          ("fradPPPto1294", 2),
          ("isdndchan", 5),
          ("nfr", 1),
          ("smds", 3),
          ("smdsoptmgmt", 8))
    )


_LportProtocol_Type.__name__ = "Integer32"
_LportProtocol_Object = MibTableColumn
lportProtocol = _LportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 6),
    _LportProtocol_Type()
)
lportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportProtocol.setStatus("mandatory")


class _LportSignal_Type(Integer32):
    """Custom type lportSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2),
          ("nni", 3))
    )


_LportSignal_Type.__name__ = "Integer32"
_LportSignal_Object = MibTableColumn
lportSignal = _LportSignal_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 7),
    _LportSignal_Type()
)
lportSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSignal.setStatus("mandatory")
_LportFt1Ds0s_Type = OctetString
_LportFt1Ds0s_Object = MibTableColumn
lportFt1Ds0s = _LportFt1Ds0s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 8),
    _LportFt1Ds0s_Type()
)
lportFt1Ds0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportFt1Ds0s.setStatus("mandatory")
_LportGlobalDlci_Type = Integer32
_LportGlobalDlci_Object = MibTableColumn
lportGlobalDlci = _LportGlobalDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 9),
    _LportGlobalDlci_Type()
)
lportGlobalDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportGlobalDlci.setStatus("mandatory")


class _LportDlcmiStd_Type(Integer32):
    """Custom type lportDlcmiStd based on Integer32"""
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
        *(("ansiT1-617-B", 6),
          ("ansiT1-617-D", 3),
          ("autodetect", 5),
          ("ccittQ-933-A", 4),
          ("disabled", 1),
          ("lmiRev1", 2))
    )


_LportDlcmiStd_Type.__name__ = "Integer32"
_LportDlcmiStd_Object = MibTableColumn
lportDlcmiStd = _LportDlcmiStd_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 10),
    _LportDlcmiStd_Type()
)
lportDlcmiStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDlcmiStd.setStatus("mandatory")


class _LportDlciAddrFmt_Type(Integer32):
    """Custom type lportDlciAddrFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("q922", 1)
    )


_LportDlciAddrFmt_Type.__name__ = "Integer32"
_LportDlciAddrFmt_Object = MibTableColumn
lportDlciAddrFmt = _LportDlciAddrFmt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 11),
    _LportDlciAddrFmt_Type()
)
lportDlciAddrFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDlciAddrFmt.setStatus("mandatory")


class _LportDlciAddrLen_Type(Integer32):
    """Custom type lportDlciAddrLen based on Integer32"""
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
        *(("four-octets-17-bits", 4),
          ("four-octets-23-bits", 5),
          ("three-octets-10-bits", 2),
          ("three-octets-16-bits", 3),
          ("two-octets-10-bits", 1))
    )


_LportDlciAddrLen_Type.__name__ = "Integer32"
_LportDlciAddrLen_Object = MibTableColumn
lportDlciAddrLen = _LportDlciAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 12),
    _LportDlciAddrLen_Type()
)
lportDlciAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDlciAddrLen.setStatus("mandatory")
_LportMaxFramesize_Type = Integer32
_LportMaxFramesize_Object = MibTableColumn
lportMaxFramesize = _LportMaxFramesize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 13),
    _LportMaxFramesize_Type()
)
lportMaxFramesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportMaxFramesize.setStatus("mandatory")
_LportDceVerifTimer_Type = Integer32
_LportDceVerifTimer_Object = MibTableColumn
lportDceVerifTimer = _LportDceVerifTimer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 14),
    _LportDceVerifTimer_Type()
)
lportDceVerifTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDceVerifTimer.setStatus("mandatory")
_LportDceErrorThresh_Type = Integer32
_LportDceErrorThresh_Object = MibTableColumn
lportDceErrorThresh = _LportDceErrorThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 15),
    _LportDceErrorThresh_Type()
)
lportDceErrorThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDceErrorThresh.setStatus("mandatory")
_LportDceEventCount_Type = Integer32
_LportDceEventCount_Object = MibTableColumn
lportDceEventCount = _LportDceEventCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 16),
    _LportDceEventCount_Type()
)
lportDceEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDceEventCount.setStatus("mandatory")
_LportDteErrorThresh_Type = Integer32
_LportDteErrorThresh_Object = MibTableColumn
lportDteErrorThresh = _LportDteErrorThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 17),
    _LportDteErrorThresh_Type()
)
lportDteErrorThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDteErrorThresh.setStatus("mandatory")
_LportDteEventCount_Type = Integer32
_LportDteEventCount_Object = MibTableColumn
lportDteEventCount = _LportDteEventCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 18),
    _LportDteEventCount_Type()
)
lportDteEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDteEventCount.setStatus("mandatory")
_LportDtePollTimer_Type = Integer32
_LportDtePollTimer_Object = MibTableColumn
lportDtePollTimer = _LportDtePollTimer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 19),
    _LportDtePollTimer_Type()
)
lportDtePollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDtePollTimer.setStatus("mandatory")
_LportDteFullCounter_Type = Integer32
_LportDteFullCounter_Object = MibTableColumn
lportDteFullCounter = _LportDteFullCounter_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 20),
    _LportDteFullCounter_Type()
)
lportDteFullCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDteFullCounter.setStatus("mandatory")


class _LportDteMulticast_Type(Integer32):
    """Custom type lportDteMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-way", 3),
          ("one-way", 1),
          ("two-way", 2))
    )


_LportDteMulticast_Type.__name__ = "Integer32"
_LportDteMulticast_Object = MibTableColumn
lportDteMulticast = _LportDteMulticast_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 21),
    _LportDteMulticast_Type()
)
lportDteMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDteMulticast.setStatus("mandatory")
_LportTrkRnode_Type = IpAddress
_LportTrkRnode_Object = MibTableColumn
lportTrkRnode = _LportTrkRnode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 22),
    _LportTrkRnode_Type()
)
lportTrkRnode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkRnode.setStatus("mandatory")
_LportTrkRlport_Type = Integer32
_LportTrkRlport_Object = MibTableColumn
lportTrkRlport = _LportTrkRlport_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 23),
    _LportTrkRlport_Type()
)
lportTrkRlport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkRlport.setStatus("mandatory")


class _LportCongestState_Type(Integer32):
    """Custom type lportCongestState based on Integer32"""
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
        *(("critical", 4),
          ("mild", 2),
          ("normal", 1),
          ("severe", 3))
    )


_LportCongestState_Type.__name__ = "Integer32"
_LportCongestState_Object = MibTableColumn
lportCongestState = _LportCongestState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 24),
    _LportCongestState_Type()
)
lportCongestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCongestState.setStatus("mandatory")
_LportQP1Len_Type = Integer32
_LportQP1Len_Object = MibTableColumn
lportQP1Len = _LportQP1Len_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 25),
    _LportQP1Len_Type()
)
lportQP1Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportQP1Len.setStatus("mandatory")
_LportQP2Len_Type = Integer32
_LportQP2Len_Object = MibTableColumn
lportQP2Len = _LportQP2Len_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 26),
    _LportQP2Len_Type()
)
lportQP2Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportQP2Len.setStatus("mandatory")
_LportQP3Len_Type = Integer32
_LportQP3Len_Object = MibTableColumn
lportQP3Len = _LportQP3Len_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 27),
    _LportQP3Len_Type()
)
lportQP3Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportQP3Len.setStatus("mandatory")
_LportQP4Len_Type = Integer32
_LportQP4Len_Object = MibTableColumn
lportQP4Len = _LportQP4Len_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 28),
    _LportQP4Len_Type()
)
lportQP4Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportQP4Len.setStatus("mandatory")
_LportErrTime_Type = TimeTicks
_LportErrTime_Object = MibTableColumn
lportErrTime = _LportErrTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 29),
    _LportErrTime_Type()
)
lportErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportErrTime.setStatus("mandatory")


class _LportErrType_Type(Integer32):
    """Custom type lportErrType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("crc-Error", 4),
          ("discardFW", 16),
          ("discardIllegalLen", 19),
          ("discardPortMismatch", 18),
          ("discardRange", 17),
          ("dlcmiProtoErr", 11),
          ("dlcmiSequenceErr", 13),
          ("dlcmiUnknownIE", 12),
          ("dlcmiUnknownRpt", 14),
          ("hdlc-abort", 2),
          ("illegalDLCI", 9),
          ("rcv-Long", 5),
          ("rcv-overrun", 6),
          ("residual-bit", 3),
          ("short-frame", 1),
          ("tx-underrun", 7),
          ("unknownDLCI", 10),
          ("unknownError", 8),
          ("unknownProt", 15))
    )


_LportErrType_Type.__name__ = "Integer32"
_LportErrType_Object = MibTableColumn
lportErrType = _LportErrType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 30),
    _LportErrType_Type()
)
lportErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportErrType.setStatus("mandatory")
_LportErrData_Type = OctetString
_LportErrData_Object = MibTableColumn
lportErrData = _LportErrData_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 31),
    _LportErrData_Type()
)
lportErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportErrData.setStatus("mandatory")
_LportDiagTestId_Type = Integer32
_LportDiagTestId_Object = MibTableColumn
lportDiagTestId = _LportDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 32),
    _LportDiagTestId_Type()
)
lportDiagTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDiagTestId.setStatus("mandatory")
_LportDiagTestRuns_Type = Integer32
_LportDiagTestRuns_Object = MibTableColumn
lportDiagTestRuns = _LportDiagTestRuns_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 33),
    _LportDiagTestRuns_Type()
)
lportDiagTestRuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDiagTestRuns.setStatus("mandatory")
_LportDataRate_Type = Integer32
_LportDataRate_Object = MibTableColumn
lportDataRate = _LportDataRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 34),
    _LportDataRate_Type()
)
lportDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDataRate.setStatus("mandatory")


class _LportTrkStatus_Type(Integer32):
    """Custom type lportTrkStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("btdefined", 9),
          ("n2way", 3),
          ("nattempt", 1),
          ("nexchange", 5),
          ("nexstart", 4),
          ("nfull", 7),
          ("ninit", 2),
          ("nloading", 6))
    )


_LportTrkStatus_Type.__name__ = "Integer32"
_LportTrkStatus_Object = MibTableColumn
lportTrkStatus = _LportTrkStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 35),
    _LportTrkStatus_Type()
)
lportTrkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportTrkStatus.setStatus("mandatory")
_LportSevCongests_Type = Integer32
_LportSevCongests_Object = MibTableColumn
lportSevCongests = _LportSevCongests_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 36),
    _LportSevCongests_Type()
)
lportSevCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSevCongests.setStatus("mandatory")
_LportAbsCongests_Type = Integer32
_LportAbsCongests_Object = MibTableColumn
lportAbsCongests = _LportAbsCongests_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 37),
    _LportAbsCongests_Type()
)
lportAbsCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportAbsCongests.setStatus("mandatory")
_LportTrkOverhead_Type = Integer32
_LportTrkOverhead_Object = MibTableColumn
lportTrkOverhead = _LportTrkOverhead_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 38),
    _LportTrkOverhead_Type()
)
lportTrkOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkOverhead.setStatus("mandatory")
_LportTrkUtil_Type = Integer32
_LportTrkUtil_Object = MibTableColumn
lportTrkUtil = _LportTrkUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 39),
    _LportTrkUtil_Type()
)
lportTrkUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkUtil.setStatus("mandatory")
_LportVAvailbw_Type = Integer32
_LportVAvailbw_Object = MibTableColumn
lportVAvailbw = _LportVAvailbw_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 40),
    _LportVAvailbw_Type()
)
lportVAvailbw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportVAvailbw.setStatus("mandatory")
_LportTrkLastTimeChange_Type = TimeTicks
_LportTrkLastTimeChange_Object = MibTableColumn
lportTrkLastTimeChange = _LportTrkLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 41),
    _LportTrkLastTimeChange_Type()
)
lportTrkLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportTrkLastTimeChange.setStatus("mandatory")
_LportCongestRate_Type = Integer32
_LportCongestRate_Object = MibTableColumn
lportCongestRate = _LportCongestRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 42),
    _LportCongestRate_Type()
)
lportCongestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCongestRate.setStatus("mandatory")
_LportCongestRateThresh_Type = Integer32
_LportCongestRateThresh_Object = MibTableColumn
lportCongestRateThresh = _LportCongestRateThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 43),
    _LportCongestRateThresh_Type()
)
lportCongestRateThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportCongestRateThresh.setStatus("mandatory")


class _LportDiagState_Type(Integer32):
    """Custom type lportDiagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_LportDiagState_Type.__name__ = "Integer32"
_LportDiagState_Object = MibTableColumn
lportDiagState = _LportDiagState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 44),
    _LportDiagState_Type()
)
lportDiagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDiagState.setStatus("mandatory")
_LportDiagOptionStr_Type = OctetString
_LportDiagOptionStr_Object = MibTableColumn
lportDiagOptionStr = _LportDiagOptionStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 45),
    _LportDiagOptionStr_Type()
)
lportDiagOptionStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDiagOptionStr.setStatus("mandatory")
_LportDiagPassCount_Type = Integer32
_LportDiagPassCount_Object = MibTableColumn
lportDiagPassCount = _LportDiagPassCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 46),
    _LportDiagPassCount_Type()
)
lportDiagPassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDiagPassCount.setStatus("mandatory")
_LportDiagFailCount_Type = Integer32
_LportDiagFailCount_Object = MibTableColumn
lportDiagFailCount = _LportDiagFailCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 47),
    _LportDiagFailCount_Type()
)
lportDiagFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDiagFailCount.setStatus("mandatory")
_LportDiagResultStr_Type = DisplayString
_LportDiagResultStr_Object = MibTableColumn
lportDiagResultStr = _LportDiagResultStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 48),
    _LportDiagResultStr_Type()
)
lportDiagResultStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDiagResultStr.setStatus("mandatory")


class _LportDs0BitStuff_Type(Integer32):
    """Custom type lportDs0BitStuff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bit-stuffing", 1)
    )


_LportDs0BitStuff_Type.__name__ = "Integer32"
_LportDs0BitStuff_Object = MibTableColumn
lportDs0BitStuff = _LportDs0BitStuff_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 49),
    _LportDs0BitStuff_Type()
)
lportDs0BitStuff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDs0BitStuff.setStatus("mandatory")
_LportErrorThreshold_Type = Integer32
_LportErrorThreshold_Object = MibTableColumn
lportErrorThreshold = _LportErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 50),
    _LportErrorThreshold_Type()
)
lportErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportErrorThreshold.setStatus("mandatory")
_LportUnsyncBandwidth_Type = Integer32
_LportUnsyncBandwidth_Object = MibTableColumn
lportUnsyncBandwidth = _LportUnsyncBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 51),
    _LportUnsyncBandwidth_Type()
)
lportUnsyncBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportUnsyncBandwidth.setStatus("mandatory")
_LportDTEInStatusFrames_Type = Counter32
_LportDTEInStatusFrames_Object = MibTableColumn
lportDTEInStatusFrames = _LportDTEInStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 52),
    _LportDTEInStatusFrames_Type()
)
lportDTEInStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEInStatusFrames.setStatus("mandatory")
_LportDTEInFullStatusFrames_Type = Counter32
_LportDTEInFullStatusFrames_Object = MibTableColumn
lportDTEInFullStatusFrames = _LportDTEInFullStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 53),
    _LportDTEInFullStatusFrames_Type()
)
lportDTEInFullStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEInFullStatusFrames.setStatus("mandatory")
_LportDTEInAsyncStatusFrames_Type = Counter32
_LportDTEInAsyncStatusFrames_Object = MibTableColumn
lportDTEInAsyncStatusFrames = _LportDTEInAsyncStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 54),
    _LportDTEInAsyncStatusFrames_Type()
)
lportDTEInAsyncStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEInAsyncStatusFrames.setStatus("mandatory")
_LportDTEInErrorFrames_Type = Counter32
_LportDTEInErrorFrames_Object = MibTableColumn
lportDTEInErrorFrames = _LportDTEInErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 55),
    _LportDTEInErrorFrames_Type()
)
lportDTEInErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEInErrorFrames.setStatus("mandatory")
_LportDTEOutPollFrames_Type = Counter32
_LportDTEOutPollFrames_Object = MibTableColumn
lportDTEOutPollFrames = _LportDTEOutPollFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 56),
    _LportDTEOutPollFrames_Type()
)
lportDTEOutPollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEOutPollFrames.setStatus("mandatory")
_LportDTEPollErrorCounts_Type = Counter32
_LportDTEPollErrorCounts_Object = MibTableColumn
lportDTEPollErrorCounts = _LportDTEPollErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 57),
    _LportDTEPollErrorCounts_Type()
)
lportDTEPollErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEPollErrorCounts.setStatus("mandatory")
_LportDTEFailCounts_Type = Counter32
_LportDTEFailCounts_Object = MibTableColumn
lportDTEFailCounts = _LportDTEFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 58),
    _LportDTEFailCounts_Type()
)
lportDTEFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEFailCounts.setStatus("mandatory")


class _LportDTEFailReason_Type(Integer32):
    """Custom type lportDTEFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte-bad-Nr", 1),
          ("dte-timeout", 2),
          ("prot-error", 3))
    )


_LportDTEFailReason_Type.__name__ = "Integer32"
_LportDTEFailReason_Object = MibTableColumn
lportDTEFailReason = _LportDTEFailReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 59),
    _LportDTEFailReason_Type()
)
lportDTEFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEFailReason.setStatus("mandatory")


class _LportDTEOperStatus_Type(Integer32):
    """Custom type lportDTEOperStatus based on Integer32"""
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


_LportDTEOperStatus_Type.__name__ = "Integer32"
_LportDTEOperStatus_Object = MibTableColumn
lportDTEOperStatus = _LportDTEOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 60),
    _LportDTEOperStatus_Type()
)
lportDTEOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDTEOperStatus.setStatus("mandatory")
_LportDCEInPollFrames_Type = Counter32
_LportDCEInPollFrames_Object = MibTableColumn
lportDCEInPollFrames = _LportDCEInPollFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 61),
    _LportDCEInPollFrames_Type()
)
lportDCEInPollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEInPollFrames.setStatus("mandatory")
_LportDCEInErrorFrames_Type = Counter32
_LportDCEInErrorFrames_Object = MibTableColumn
lportDCEInErrorFrames = _LportDCEInErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 62),
    _LportDCEInErrorFrames_Type()
)
lportDCEInErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEInErrorFrames.setStatus("mandatory")
_LportDCEOutStatusFrames_Type = Counter32
_LportDCEOutStatusFrames_Object = MibTableColumn
lportDCEOutStatusFrames = _LportDCEOutStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 63),
    _LportDCEOutStatusFrames_Type()
)
lportDCEOutStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEOutStatusFrames.setStatus("mandatory")
_LportDCEOutFullStatusFrames_Type = Counter32
_LportDCEOutFullStatusFrames_Object = MibTableColumn
lportDCEOutFullStatusFrames = _LportDCEOutFullStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 64),
    _LportDCEOutFullStatusFrames_Type()
)
lportDCEOutFullStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEOutFullStatusFrames.setStatus("mandatory")
_LportDCEOutAsyncStatusFrames_Type = Counter32
_LportDCEOutAsyncStatusFrames_Object = MibTableColumn
lportDCEOutAsyncStatusFrames = _LportDCEOutAsyncStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 65),
    _LportDCEOutAsyncStatusFrames_Type()
)
lportDCEOutAsyncStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEOutAsyncStatusFrames.setStatus("mandatory")
_LportDCEPollErrorCounts_Type = Counter32
_LportDCEPollErrorCounts_Object = MibTableColumn
lportDCEPollErrorCounts = _LportDCEPollErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 66),
    _LportDCEPollErrorCounts_Type()
)
lportDCEPollErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEPollErrorCounts.setStatus("mandatory")
_LportDCEFailCounts_Type = Counter32
_LportDCEFailCounts_Object = MibTableColumn
lportDCEFailCounts = _LportDCEFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 67),
    _LportDCEFailCounts_Type()
)
lportDCEFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEFailCounts.setStatus("mandatory")


class _LportDCEFailReason_Type(Integer32):
    """Custom type lportDCEFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce-bad-Nr", 1),
          ("dce-timeout", 2),
          ("prot-error", 3))
    )


_LportDCEFailReason_Type.__name__ = "Integer32"
_LportDCEFailReason_Object = MibTableColumn
lportDCEFailReason = _LportDCEFailReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 68),
    _LportDCEFailReason_Type()
)
lportDCEFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEFailReason.setStatus("mandatory")


class _LportDCEOperStatus_Type(Integer32):
    """Custom type lportDCEOperStatus based on Integer32"""
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


_LportDCEOperStatus_Type.__name__ = "Integer32"
_LportDCEOperStatus_Object = MibTableColumn
lportDCEOperStatus = _LportDCEOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 69),
    _LportDCEOperStatus_Type()
)
lportDCEOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEOperStatus.setStatus("mandatory")


class _LportDCEOperDlcmiStd_Type(Integer32):
    """Custom type lportDCEOperDlcmiStd based on Integer32"""
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
        *(("ansiT1-617-B", 6),
          ("ansiT1-617-D", 3),
          ("ccittQ-933-A", 4),
          ("lmiRev1", 2),
          ("reserved", 5),
          ("unknown", 1))
    )


_LportDCEOperDlcmiStd_Type.__name__ = "Integer32"
_LportDCEOperDlcmiStd_Object = MibTableColumn
lportDCEOperDlcmiStd = _LportDCEOperDlcmiStd_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 70),
    _LportDCEOperDlcmiStd_Type()
)
lportDCEOperDlcmiStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDCEOperDlcmiStd.setStatus("mandatory")
_LportLMIInErrorFrames_Type = Counter32
_LportLMIInErrorFrames_Object = MibTableColumn
lportLMIInErrorFrames = _LportLMIInErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 71),
    _LportLMIInErrorFrames_Type()
)
lportLMIInErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportLMIInErrorFrames.setStatus("mandatory")
_LportDCEnN4_Type = Integer32
_LportDCEnN4_Object = MibTableColumn
lportDCEnN4 = _LportDCEnN4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 72),
    _LportDCEnN4_Type()
)
lportDCEnN4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDCEnN4.setStatus("mandatory")
_LportDCEnT3_Type = Integer32
_LportDCEnT3_Object = MibTableColumn
lportDCEnT3 = _LportDCEnT3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 73),
    _LportDCEnT3_Type()
)
lportDCEnT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDCEnT3.setStatus("mandatory")
_LportXmitLatencyThreshold_Type = Integer32
_LportXmitLatencyThreshold_Object = MibTableColumn
lportXmitLatencyThreshold = _LportXmitLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 74),
    _LportXmitLatencyThreshold_Type()
)
lportXmitLatencyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitLatencyThreshold.setStatus("mandatory")
_LportXmitRefillPriority0Percentage_Type = Integer32
_LportXmitRefillPriority0Percentage_Object = MibTableColumn
lportXmitRefillPriority0Percentage = _LportXmitRefillPriority0Percentage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 75),
    _LportXmitRefillPriority0Percentage_Type()
)
lportXmitRefillPriority0Percentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitRefillPriority0Percentage.setStatus("mandatory")
_LportXmitRefillPriority1Percentage_Type = Integer32
_LportXmitRefillPriority1Percentage_Object = MibTableColumn
lportXmitRefillPriority1Percentage = _LportXmitRefillPriority1Percentage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 76),
    _LportXmitRefillPriority1Percentage_Type()
)
lportXmitRefillPriority1Percentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitRefillPriority1Percentage.setStatus("mandatory")
_LportXmitRefillPriority2Percentage_Type = Integer32
_LportXmitRefillPriority2Percentage_Object = MibTableColumn
lportXmitRefillPriority2Percentage = _LportXmitRefillPriority2Percentage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 77),
    _LportXmitRefillPriority2Percentage_Type()
)
lportXmitRefillPriority2Percentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitRefillPriority2Percentage.setStatus("mandatory")
_LportXmitRefillPriority3Percentage_Type = Integer32
_LportXmitRefillPriority3Percentage_Object = MibTableColumn
lportXmitRefillPriority3Percentage = _LportXmitRefillPriority3Percentage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 78),
    _LportXmitRefillPriority3Percentage_Type()
)
lportXmitRefillPriority3Percentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitRefillPriority3Percentage.setStatus("mandatory")
_LportXmitDiscardLow_Type = Integer32
_LportXmitDiscardLow_Object = MibTableColumn
lportXmitDiscardLow = _LportXmitDiscardLow_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 79),
    _LportXmitDiscardLow_Type()
)
lportXmitDiscardLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportXmitDiscardLow.setStatus("mandatory")
_LportSevereThreshold_Type = Integer32
_LportSevereThreshold_Object = MibTableColumn
lportSevereThreshold = _LportSevereThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 80),
    _LportSevereThreshold_Type()
)
lportSevereThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSevereThreshold.setStatus("mandatory")
_LportMildThreshold_Type = Integer32
_LportMildThreshold_Object = MibTableColumn
lportMildThreshold = _LportMildThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 81),
    _LportMildThreshold_Type()
)
lportMildThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportMildThreshold.setStatus("mandatory")
_LportTrkKeepAliveTimer_Type = Integer32
_LportTrkKeepAliveTimer_Object = MibTableColumn
lportTrkKeepAliveTimer = _LportTrkKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 86),
    _LportTrkKeepAliveTimer_Type()
)
lportTrkKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkKeepAliveTimer.setStatus("mandatory")
_LportTrkKeepAliveErrorThreshold_Type = Integer32
_LportTrkKeepAliveErrorThreshold_Object = MibTableColumn
lportTrkKeepAliveErrorThreshold = _LportTrkKeepAliveErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 87),
    _LportTrkKeepAliveErrorThreshold_Type()
)
lportTrkKeepAliveErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkKeepAliveErrorThreshold.setStatus("mandatory")


class _LportIgCutThruStatus_Type(Integer32):
    """Custom type lportIgCutThruStatus based on Integer32"""
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


_LportIgCutThruStatus_Type.__name__ = "Integer32"
_LportIgCutThruStatus_Object = MibTableColumn
lportIgCutThruStatus = _LportIgCutThruStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 88),
    _LportIgCutThruStatus_Type()
)
lportIgCutThruStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportIgCutThruStatus.setStatus("mandatory")


class _LportEgCutThruStatus_Type(Integer32):
    """Custom type lportEgCutThruStatus based on Integer32"""
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


_LportEgCutThruStatus_Type.__name__ = "Integer32"
_LportEgCutThruStatus_Object = MibTableColumn
lportEgCutThruStatus = _LportEgCutThruStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 89),
    _LportEgCutThruStatus_Type()
)
lportEgCutThruStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportEgCutThruStatus.setStatus("mandatory")
_LportEgCutThruThresh_Type = Integer32
_LportEgCutThruThresh_Object = MibTableColumn
lportEgCutThruThresh = _LportEgCutThruThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 90),
    _LportEgCutThruThresh_Type()
)
lportEgCutThruThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportEgCutThruThresh.setStatus("mandatory")


class _LportFrameRelayTrkEnable_Type(Integer32):
    """Custom type lportFrameRelayTrkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("not-allowed", 2))
    )


_LportFrameRelayTrkEnable_Type.__name__ = "Integer32"
_LportFrameRelayTrkEnable_Object = MibTableColumn
lportFrameRelayTrkEnable = _LportFrameRelayTrkEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 91),
    _LportFrameRelayTrkEnable_Type()
)
lportFrameRelayTrkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportFrameRelayTrkEnable.setStatus("mandatory")
_LportSmdsSsiIf_Type = Integer32
_LportSmdsSsiIf_Object = MibTableColumn
lportSmdsSsiIf = _LportSmdsSsiIf_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 92),
    _LportSmdsSsiIf_Type()
)
lportSmdsSsiIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsSsiIf.setStatus("mandatory")
_LportSmdsSsiSlot_Type = Integer32
_LportSmdsSsiSlot_Object = MibTableColumn
lportSmdsSsiSlot = _LportSmdsSsiSlot_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 93),
    _LportSmdsSsiSlot_Type()
)
lportSmdsSsiSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsSsiSlot.setStatus("mandatory")
_LportSmdsScrnId_Type = Integer32
_LportSmdsScrnId_Object = MibTableColumn
lportSmdsScrnId = _LportSmdsScrnId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 94),
    _LportSmdsScrnId_Type()
)
lportSmdsScrnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsScrnId.setStatus("mandatory")


class _LportSmdsIaScrnOp_Type(Integer32):
    """Custom type lportSmdsIaScrnOp based on Integer32"""
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


_LportSmdsIaScrnOp_Type.__name__ = "Integer32"
_LportSmdsIaScrnOp_Object = MibTableColumn
lportSmdsIaScrnOp = _LportSmdsIaScrnOp_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 95),
    _LportSmdsIaScrnOp_Type()
)
lportSmdsIaScrnOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsIaScrnOp.setStatus("mandatory")


class _LportSmdsGaScrnOp_Type(Integer32):
    """Custom type lportSmdsGaScrnOp based on Integer32"""
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


_LportSmdsGaScrnOp_Type.__name__ = "Integer32"
_LportSmdsGaScrnOp_Object = MibTableColumn
lportSmdsGaScrnOp = _LportSmdsGaScrnOp_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 96),
    _LportSmdsGaScrnOp_Type()
)
lportSmdsGaScrnOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsGaScrnOp.setStatus("mandatory")
_LportSmdsIaScrnMap_Type = OctetString
_LportSmdsIaScrnMap_Object = MibTableColumn
lportSmdsIaScrnMap = _LportSmdsIaScrnMap_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 97),
    _LportSmdsIaScrnMap_Type()
)
lportSmdsIaScrnMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsIaScrnMap.setStatus("mandatory")
_LportSmdsGaScrnMap_Type = OctetString
_LportSmdsGaScrnMap_Object = MibTableColumn
lportSmdsGaScrnMap = _LportSmdsGaScrnMap_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 98),
    _LportSmdsGaScrnMap_Type()
)
lportSmdsGaScrnMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsGaScrnMap.setStatus("mandatory")
_LportSmdsTrkAddr_Type = OctetString
_LportSmdsTrkAddr_Object = MibTableColumn
lportSmdsTrkAddr = _LportSmdsTrkAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 99),
    _LportSmdsTrkAddr_Type()
)
lportSmdsTrkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsTrkAddr.setStatus("mandatory")


class _LportSmdsCrc_Type(Integer32):
    """Custom type lportSmdsCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_LportSmdsCrc_Type.__name__ = "Integer32"
_LportSmdsCrc_Object = MibTableColumn
lportSmdsCrc = _LportSmdsCrc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 100),
    _LportSmdsCrc_Type()
)
lportSmdsCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCrc.setStatus("mandatory")


class _LportSmdsCpePoll_Type(Integer32):
    """Custom type lportSmdsCpePoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nopoll", 1),
          ("poll", 2))
    )


_LportSmdsCpePoll_Type.__name__ = "Integer32"
_LportSmdsCpePoll_Object = MibTableColumn
lportSmdsCpePoll = _LportSmdsCpePoll_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 101),
    _LportSmdsCpePoll_Type()
)
lportSmdsCpePoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCpePoll.setStatus("mandatory")


class _LportSmdsPduCheck_Type(Integer32):
    """Custom type lportSmdsPduCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_LportSmdsPduCheck_Type.__name__ = "Integer32"
_LportSmdsPduCheck_Object = MibTableColumn
lportSmdsPduCheck = _LportSmdsPduCheck_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 102),
    _LportSmdsPduCheck_Type()
)
lportSmdsPduCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsPduCheck.setStatus("mandatory")
_LportSmdsCntOutFrDxi2HbPolls_Type = Counter32
_LportSmdsCntOutFrDxi2HbPolls_Object = MibTableColumn
lportSmdsCntOutFrDxi2HbPolls = _LportSmdsCntOutFrDxi2HbPolls_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 103),
    _LportSmdsCntOutFrDxi2HbPolls_Type()
)
lportSmdsCntOutFrDxi2HbPolls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntOutFrDxi2HbPolls.setStatus("mandatory")
_LportSmdsCntOutByteDxi2HbPolls_Type = Counter32
_LportSmdsCntOutByteDxi2HbPolls_Object = MibTableColumn
lportSmdsCntOutByteDxi2HbPolls = _LportSmdsCntOutByteDxi2HbPolls_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 104),
    _LportSmdsCntOutByteDxi2HbPolls_Type()
)
lportSmdsCntOutByteDxi2HbPolls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntOutByteDxi2HbPolls.setStatus("mandatory")
_LportSmdsCntInFrDxi2HbPolls_Type = Counter32
_LportSmdsCntInFrDxi2HbPolls_Object = MibTableColumn
lportSmdsCntInFrDxi2HbPolls = _LportSmdsCntInFrDxi2HbPolls_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 105),
    _LportSmdsCntInFrDxi2HbPolls_Type()
)
lportSmdsCntInFrDxi2HbPolls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntInFrDxi2HbPolls.setStatus("mandatory")
_LportSmdsCntInByteDxi2HbPolls_Type = Counter32
_LportSmdsCntInByteDxi2HbPolls_Object = MibTableColumn
lportSmdsCntInByteDxi2HbPolls = _LportSmdsCntInByteDxi2HbPolls_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 106),
    _LportSmdsCntInByteDxi2HbPolls_Type()
)
lportSmdsCntInByteDxi2HbPolls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntInByteDxi2HbPolls.setStatus("mandatory")
_LportSmdsCntOutFrSip3s_Type = Counter32
_LportSmdsCntOutFrSip3s_Object = MibTableColumn
lportSmdsCntOutFrSip3s = _LportSmdsCntOutFrSip3s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 107),
    _LportSmdsCntOutFrSip3s_Type()
)
lportSmdsCntOutFrSip3s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntOutFrSip3s.setStatus("mandatory")
_LportSmdsCntOutByteSip3s_Type = Counter32
_LportSmdsCntOutByteSip3s_Object = MibTableColumn
lportSmdsCntOutByteSip3s = _LportSmdsCntOutByteSip3s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 108),
    _LportSmdsCntOutByteSip3s_Type()
)
lportSmdsCntOutByteSip3s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntOutByteSip3s.setStatus("mandatory")
_LportSmdsCntInFrSip3s_Type = Counter32
_LportSmdsCntInFrSip3s_Object = MibTableColumn
lportSmdsCntInFrSip3s = _LportSmdsCntInFrSip3s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 109),
    _LportSmdsCntInFrSip3s_Type()
)
lportSmdsCntInFrSip3s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntInFrSip3s.setStatus("mandatory")
_LportSmdsCntInByteSip3s_Type = Counter32
_LportSmdsCntInByteSip3s_Object = MibTableColumn
lportSmdsCntInByteSip3s = _LportSmdsCntInByteSip3s_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 110),
    _LportSmdsCntInByteSip3s_Type()
)
lportSmdsCntInByteSip3s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntInByteSip3s.setStatus("mandatory")
_LportSmdsCntDxi2LinkIdInvalids_Type = Counter32
_LportSmdsCntDxi2LinkIdInvalids_Object = MibTableColumn
lportSmdsCntDxi2LinkIdInvalids = _LportSmdsCntDxi2LinkIdInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 111),
    _LportSmdsCntDxi2LinkIdInvalids_Type()
)
lportSmdsCntDxi2LinkIdInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2LinkIdInvalids.setStatus("mandatory")
_LportSmdsCntDxi2StationIdInvalids_Type = Counter32
_LportSmdsCntDxi2StationIdInvalids_Object = MibTableColumn
lportSmdsCntDxi2StationIdInvalids = _LportSmdsCntDxi2StationIdInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 112),
    _LportSmdsCntDxi2StationIdInvalids_Type()
)
lportSmdsCntDxi2StationIdInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2StationIdInvalids.setStatus("mandatory")
_LportSmdsCntDxi2CrInvalids_Type = Counter32
_LportSmdsCntDxi2CrInvalids_Object = MibTableColumn
lportSmdsCntDxi2CrInvalids = _LportSmdsCntDxi2CrInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 113),
    _LportSmdsCntDxi2CrInvalids_Type()
)
lportSmdsCntDxi2CrInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2CrInvalids.setStatus("mandatory")
_LportSmdsCntDxi2AeInvalids_Type = Counter32
_LportSmdsCntDxi2AeInvalids_Object = MibTableColumn
lportSmdsCntDxi2AeInvalids = _LportSmdsCntDxi2AeInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 114),
    _LportSmdsCntDxi2AeInvalids_Type()
)
lportSmdsCntDxi2AeInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2AeInvalids.setStatus("mandatory")
_LportSmdsCntDxi2CtrlInvalids_Type = Counter32
_LportSmdsCntDxi2CtrlInvalids_Object = MibTableColumn
lportSmdsCntDxi2CtrlInvalids = _LportSmdsCntDxi2CtrlInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 115),
    _LportSmdsCntDxi2CtrlInvalids_Type()
)
lportSmdsCntDxi2CtrlInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2CtrlInvalids.setStatus("mandatory")
_LportSmdsCntDxi2FrameSizeErrors_Type = Counter32
_LportSmdsCntDxi2FrameSizeErrors_Object = MibTableColumn
lportSmdsCntDxi2FrameSizeErrors = _LportSmdsCntDxi2FrameSizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 116),
    _LportSmdsCntDxi2FrameSizeErrors_Type()
)
lportSmdsCntDxi2FrameSizeErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDxi2FrameSizeErrors.setStatus("mandatory")
_LportSmdsCntSip3RsvdInvalids_Type = Counter32
_LportSmdsCntSip3RsvdInvalids_Object = MibTableColumn
lportSmdsCntSip3RsvdInvalids = _LportSmdsCntSip3RsvdInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 117),
    _LportSmdsCntSip3RsvdInvalids_Type()
)
lportSmdsCntSip3RsvdInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3RsvdInvalids.setStatus("mandatory")
_LportSmdsCntSip3BetagMismatchs_Type = Counter32
_LportSmdsCntSip3BetagMismatchs_Object = MibTableColumn
lportSmdsCntSip3BetagMismatchs = _LportSmdsCntSip3BetagMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 118),
    _LportSmdsCntSip3BetagMismatchs_Type()
)
lportSmdsCntSip3BetagMismatchs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3BetagMismatchs.setStatus("mandatory")
_LportSmdsCntSip3BasizeIncorrects_Type = Counter32
_LportSmdsCntSip3BasizeIncorrects_Object = MibTableColumn
lportSmdsCntSip3BasizeIncorrects = _LportSmdsCntSip3BasizeIncorrects_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 119),
    _LportSmdsCntSip3BasizeIncorrects_Type()
)
lportSmdsCntSip3BasizeIncorrects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3BasizeIncorrects.setStatus("mandatory")
_LportSmdsCntSip3BasizeInvalids_Type = Counter32
_LportSmdsCntSip3BasizeInvalids_Object = MibTableColumn
lportSmdsCntSip3BasizeInvalids = _LportSmdsCntSip3BasizeInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 120),
    _LportSmdsCntSip3BasizeInvalids_Type()
)
lportSmdsCntSip3BasizeInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3BasizeInvalids.setStatus("mandatory")
_LportSmdsCntSip3DaTypeInvalids_Type = Counter32
_LportSmdsCntSip3DaTypeInvalids_Object = MibTableColumn
lportSmdsCntSip3DaTypeInvalids = _LportSmdsCntSip3DaTypeInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 121),
    _LportSmdsCntSip3DaTypeInvalids_Type()
)
lportSmdsCntSip3DaTypeInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3DaTypeInvalids.setStatus("mandatory")
_LportSmdsCntSip3DaInvalids_Type = Counter32
_LportSmdsCntSip3DaInvalids_Object = MibTableColumn
lportSmdsCntSip3DaInvalids = _LportSmdsCntSip3DaInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 122),
    _LportSmdsCntSip3DaInvalids_Type()
)
lportSmdsCntSip3DaInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3DaInvalids.setStatus("mandatory")
_LportSmdsCntSip3SaTypeInvalids_Type = Counter32
_LportSmdsCntSip3SaTypeInvalids_Object = MibTableColumn
lportSmdsCntSip3SaTypeInvalids = _LportSmdsCntSip3SaTypeInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 123),
    _LportSmdsCntSip3SaTypeInvalids_Type()
)
lportSmdsCntSip3SaTypeInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3SaTypeInvalids.setStatus("mandatory")
_LportSmdsCntSip3SaInvalids_Type = Counter32
_LportSmdsCntSip3SaInvalids_Object = MibTableColumn
lportSmdsCntSip3SaInvalids = _LportSmdsCntSip3SaInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 124),
    _LportSmdsCntSip3SaInvalids_Type()
)
lportSmdsCntSip3SaInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3SaInvalids.setStatus("mandatory")
_LportSmdsCntSip3BasizeMismatchs_Type = Counter32
_LportSmdsCntSip3BasizeMismatchs_Object = MibTableColumn
lportSmdsCntSip3BasizeMismatchs = _LportSmdsCntSip3BasizeMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 125),
    _LportSmdsCntSip3BasizeMismatchs_Type()
)
lportSmdsCntSip3BasizeMismatchs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3BasizeMismatchs.setStatus("mandatory")
_LportSmdsCntSip3HeLenInvalids_Type = Counter32
_LportSmdsCntSip3HeLenInvalids_Object = MibTableColumn
lportSmdsCntSip3HeLenInvalids = _LportSmdsCntSip3HeLenInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 126),
    _LportSmdsCntSip3HeLenInvalids_Type()
)
lportSmdsCntSip3HeLenInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3HeLenInvalids.setStatus("mandatory")
_LportSmdsCntSip3HeVersionInvalids_Type = Counter32
_LportSmdsCntSip3HeVersionInvalids_Object = MibTableColumn
lportSmdsCntSip3HeVersionInvalids = _LportSmdsCntSip3HeVersionInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 127),
    _LportSmdsCntSip3HeVersionInvalids_Type()
)
lportSmdsCntSip3HeVersionInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3HeVersionInvalids.setStatus("mandatory")
_LportSmdsCntSip3HeCarrierInvalids_Type = Counter32
_LportSmdsCntSip3HeCarrierInvalids_Object = MibTableColumn
lportSmdsCntSip3HeCarrierInvalids = _LportSmdsCntSip3HeCarrierInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 128),
    _LportSmdsCntSip3HeCarrierInvalids_Type()
)
lportSmdsCntSip3HeCarrierInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3HeCarrierInvalids.setStatus("mandatory")
_LportSmdsCntSip3Crc32Errors_Type = Counter32
_LportSmdsCntSip3Crc32Errors_Object = MibTableColumn
lportSmdsCntSip3Crc32Errors = _LportSmdsCntSip3Crc32Errors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 129),
    _LportSmdsCntSip3Crc32Errors_Type()
)
lportSmdsCntSip3Crc32Errors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3Crc32Errors.setStatus("mandatory")
_LportSmdsCntSip3TRsvdInvalids_Type = Counter32
_LportSmdsCntSip3TRsvdInvalids_Object = MibTableColumn
lportSmdsCntSip3TRsvdInvalids = _LportSmdsCntSip3TRsvdInvalids_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 130),
    _LportSmdsCntSip3TRsvdInvalids_Type()
)
lportSmdsCntSip3TRsvdInvalids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSip3TRsvdInvalids.setStatus("mandatory")
_LportSmdsCntSaNotFounds_Type = Counter32
_LportSmdsCntSaNotFounds_Object = MibTableColumn
lportSmdsCntSaNotFounds = _LportSmdsCntSaNotFounds_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 131),
    _LportSmdsCntSaNotFounds_Type()
)
lportSmdsCntSaNotFounds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSaNotFounds.setStatus("mandatory")
_LportSmdsCntSaValidationFails_Type = Counter32
_LportSmdsCntSaValidationFails_Object = MibTableColumn
lportSmdsCntSaValidationFails = _LportSmdsCntSaValidationFails_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 132),
    _LportSmdsCntSaValidationFails_Type()
)
lportSmdsCntSaValidationFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSaValidationFails.setStatus("mandatory")
_LportSmdsCntSaDaOnSamePorts_Type = Counter32
_LportSmdsCntSaDaOnSamePorts_Object = MibTableColumn
lportSmdsCntSaDaOnSamePorts = _LportSmdsCntSaDaOnSamePorts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 133),
    _LportSmdsCntSaDaOnSamePorts_Type()
)
lportSmdsCntSaDaOnSamePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSaDaOnSamePorts.setStatus("mandatory")
_LportSmdsCntDaSsiMismacths_Type = Counter32
_LportSmdsCntDaSsiMismacths_Object = MibTableColumn
lportSmdsCntDaSsiMismacths = _LportSmdsCntDaSsiMismacths_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 134),
    _LportSmdsCntDaSsiMismacths_Type()
)
lportSmdsCntDaSsiMismacths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDaSsiMismacths.setStatus("mandatory")
_LportSmdsCntSsiProvisionErrors_Type = Counter32
_LportSmdsCntSsiProvisionErrors_Object = MibTableColumn
lportSmdsCntSsiProvisionErrors = _LportSmdsCntSsiProvisionErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 135),
    _LportSmdsCntSsiProvisionErrors_Type()
)
lportSmdsCntSsiProvisionErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSsiProvisionErrors.setStatus("mandatory")
_LportSmdsCntDstIaNotFounds_Type = Counter32
_LportSmdsCntDstIaNotFounds_Object = MibTableColumn
lportSmdsCntDstIaNotFounds = _LportSmdsCntDstIaNotFounds_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 136),
    _LportSmdsCntDstIaNotFounds_Type()
)
lportSmdsCntDstIaNotFounds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDstIaNotFounds.setStatus("mandatory")
_LportSmdsCntDstGaNotFounds_Type = Counter32
_LportSmdsCntDstGaNotFounds_Object = MibTableColumn
lportSmdsCntDstGaNotFounds = _LportSmdsCntDstGaNotFounds_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 137),
    _LportSmdsCntDstGaNotFounds_Type()
)
lportSmdsCntDstGaNotFounds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDstGaNotFounds.setStatus("mandatory")
_LportSmdsCntSrcIaScrnFails_Type = Counter32
_LportSmdsCntSrcIaScrnFails_Object = MibTableColumn
lportSmdsCntSrcIaScrnFails = _LportSmdsCntSrcIaScrnFails_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 138),
    _LportSmdsCntSrcIaScrnFails_Type()
)
lportSmdsCntSrcIaScrnFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntSrcIaScrnFails.setStatus("mandatory")
_LportSmdsCntDstIaScrnFails_Type = Counter32
_LportSmdsCntDstIaScrnFails_Object = MibTableColumn
lportSmdsCntDstIaScrnFails = _LportSmdsCntDstIaScrnFails_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 139),
    _LportSmdsCntDstIaScrnFails_Type()
)
lportSmdsCntDstIaScrnFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDstIaScrnFails.setStatus("mandatory")
_LportSmdsCntDstGaScrnFails_Type = Counter32
_LportSmdsCntDstGaScrnFails_Object = MibTableColumn
lportSmdsCntDstGaScrnFails = _LportSmdsCntDstGaScrnFails_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 140),
    _LportSmdsCntDstGaScrnFails_Type()
)
lportSmdsCntDstGaScrnFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsCntDstGaScrnFails.setStatus("mandatory")
_LportSmdsTotalDiscards_Type = Counter32
_LportSmdsTotalDiscards_Object = MibTableColumn
lportSmdsTotalDiscards = _LportSmdsTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 141),
    _LportSmdsTotalDiscards_Type()
)
lportSmdsTotalDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsTotalDiscards.setStatus("mandatory")
_LportSmdsSsiNode_Type = Integer32
_LportSmdsSsiNode_Object = MibTableColumn
lportSmdsSsiNode = _LportSmdsSsiNode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 142),
    _LportSmdsSsiNode_Type()
)
lportSmdsSsiNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsSsiNode.setStatus("mandatory")


class _LportBilling_Type(Integer32):
    """Custom type lportBilling based on Integer32"""
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


_LportBilling_Type.__name__ = "Integer32"
_LportBilling_Object = MibTableColumn
lportBilling = _LportBilling_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 143),
    _LportBilling_Type()
)
lportBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBilling.setStatus("mandatory")
_LportSmdsReserved144_Type = Integer32
_LportSmdsReserved144_Object = MibTableColumn
lportSmdsReserved144 = _LportSmdsReserved144_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 144),
    _LportSmdsReserved144_Type()
)
lportSmdsReserved144.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsReserved144.setStatus("mandatory")


class _LportLinkStatus_Type(Integer32):
    """Custom type lportLinkStatus based on Integer32"""
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


_LportLinkStatus_Type.__name__ = "Integer32"
_LportLinkStatus_Object = MibTableColumn
lportLinkStatus = _LportLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 145),
    _LportLinkStatus_Type()
)
lportLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportLinkStatus.setStatus("mandatory")
_LportLMIDelay_Type = Integer32
_LportLMIDelay_Object = MibTableColumn
lportLMIDelay = _LportLMIDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 146),
    _LportLMIDelay_Type()
)
lportLMIDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportLMIDelay.setStatus("mandatory")
_LportCRC_Type = Integer32
_LportCRC_Object = MibTableColumn
lportCRC = _LportCRC_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 147),
    _LportCRC_Type()
)
lportCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportCRC.setStatus("mandatory")
_LportSmdsMulticastGa_Type = OctetString
_LportSmdsMulticastGa_Object = MibTableColumn
lportSmdsMulticastGa = _LportSmdsMulticastGa_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 148),
    _LportSmdsMulticastGa_Type()
)
lportSmdsMulticastGa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsMulticastGa.setStatus("mandatory")
_LportSmdsMulticastIpAddr_Type = IpAddress
_LportSmdsMulticastIpAddr_Object = MibTableColumn
lportSmdsMulticastIpAddr = _LportSmdsMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 149),
    _LportSmdsMulticastIpAddr_Type()
)
lportSmdsMulticastIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsMulticastIpAddr.setStatus("mandatory")
_LportAtmVPI_Type = Integer32
_LportAtmVPI_Object = MibTableColumn
lportAtmVPI = _LportAtmVPI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 150),
    _LportAtmVPI_Type()
)
lportAtmVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmVPI.setStatus("mandatory")
_LportAtmVCI_Type = Integer32
_LportAtmVCI_Object = MibTableColumn
lportAtmVCI = _LportAtmVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 151),
    _LportAtmVCI_Type()
)
lportAtmVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmVCI.setStatus("mandatory")
_LportPeakCellRateindex_Type = Integer32
_LportPeakCellRateindex_Object = MibTableColumn
lportPeakCellRateindex = _LportPeakCellRateindex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 152),
    _LportPeakCellRateindex_Type()
)
lportPeakCellRateindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportPeakCellRateindex.setStatus("mandatory")
_LportSustCellRate_Type = Integer32
_LportSustCellRate_Object = MibTableColumn
lportSustCellRate = _LportSustCellRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 153),
    _LportSustCellRate_Type()
)
lportSustCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSustCellRate.setStatus("mandatory")
_LportBurstTolerance_Type = Integer32
_LportBurstTolerance_Object = MibTableColumn
lportBurstTolerance = _LportBurstTolerance_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 154),
    _LportBurstTolerance_Type()
)
lportBurstTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBurstTolerance.setStatus("mandatory")


class _LportBuTrkOnFailure_Type(Integer32):
    """Custom type lportBuTrkOnFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_LportBuTrkOnFailure_Type.__name__ = "Integer32"
_LportBuTrkOnFailure_Object = MibTableColumn
lportBuTrkOnFailure = _LportBuTrkOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 155),
    _LportBuTrkOnFailure_Type()
)
lportBuTrkOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBuTrkOnFailure.setStatus("mandatory")
_LportTrkFailureThrsh_Type = Integer32
_LportTrkFailureThrsh_Object = MibTableColumn
lportTrkFailureThrsh = _LportTrkFailureThrsh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 156),
    _LportTrkFailureThrsh_Type()
)
lportTrkFailureThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkFailureThrsh.setStatus("mandatory")
_LportTrkRestThrsh_Type = Integer32
_LportTrkRestThrsh_Object = MibTableColumn
lportTrkRestThrsh = _LportTrkRestThrsh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 157),
    _LportTrkRestThrsh_Type()
)
lportTrkRestThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkRestThrsh.setStatus("mandatory")
_LportBuTrkRetryInt_Type = Integer32
_LportBuTrkRetryInt_Object = MibTableColumn
lportBuTrkRetryInt = _LportBuTrkRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 158),
    _LportBuTrkRetryInt_Type()
)
lportBuTrkRetryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBuTrkRetryInt.setStatus("mandatory")
_LportBuTrkRetryNum_Type = Integer32
_LportBuTrkRetryNum_Object = MibTableColumn
lportBuTrkRetryNum = _LportBuTrkRetryNum_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 159),
    _LportBuTrkRetryNum_Type()
)
lportBuTrkRetryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBuTrkRetryNum.setStatus("mandatory")
_LportBuTrkCycleInt_Type = Integer32
_LportBuTrkCycleInt_Object = MibTableColumn
lportBuTrkCycleInt = _LportBuTrkCycleInt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 160),
    _LportBuTrkCycleInt_Type()
)
lportBuTrkCycleInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportBuTrkCycleInt.setStatus("mandatory")


class _LportTrkManualBu_Type(Integer32):
    """Custom type lportTrkManualBu based on Integer32"""
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
        *(("initCmd", 1),
          ("initSched", 3),
          ("termCmd", 2),
          ("termSched", 4))
    )


_LportTrkManualBu_Type.__name__ = "Integer32"
_LportTrkManualBu_Object = MibTableColumn
lportTrkManualBu = _LportTrkManualBu_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 161),
    _LportTrkManualBu_Type()
)
lportTrkManualBu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkManualBu.setStatus("mandatory")
_LportPrimTrk_Type = Index
_LportPrimTrk_Object = MibTableColumn
lportPrimTrk = _LportPrimTrk_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 162),
    _LportPrimTrk_Type()
)
lportPrimTrk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportPrimTrk.setStatus("mandatory")


class _LportInitCallSetup_Type(Integer32):
    """Custom type lportInitCallSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_LportInitCallSetup_Type.__name__ = "Integer32"
_LportInitCallSetup_Object = MibTableColumn
lportInitCallSetup = _LportInitCallSetup_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 163),
    _LportInitCallSetup_Type()
)
lportInitCallSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportInitCallSetup.setStatus("mandatory")


class _LportBuFailReason_Type(Integer32):
    """Custom type lportBuFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buTrkNotDef", 1),
          ("buTrkNotEstab", 2))
    )


_LportBuFailReason_Type.__name__ = "Integer32"
_LportBuFailReason_Object = MibTableColumn
lportBuFailReason = _LportBuFailReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 164),
    _LportBuFailReason_Type()
)
lportBuFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportBuFailReason.setStatus("mandatory")


class _LportQ922Enable_Type(Integer32):
    """Custom type lportQ922Enable based on Integer32"""
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


_LportQ922Enable_Type.__name__ = "Integer32"
_LportQ922Enable_Object = MibTableColumn
lportQ922Enable = _LportQ922Enable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 165),
    _LportQ922Enable_Type()
)
lportQ922Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportQ922Enable.setStatus("mandatory")


class _LportQ922State_Type(Integer32):
    """Custom type lportQ922State based on Integer32"""
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
        *(("assign-awaiting", 2),
          ("awaiting-establishment", 5),
          ("awaiting-release", 6),
          ("establish-awaiting", 3),
          ("multiple-frame-established", 7),
          ("tei-assigned", 4),
          ("tei-unassigned", 1),
          ("timer-recovery", 8))
    )


_LportQ922State_Type.__name__ = "Integer32"
_LportQ922State_Object = MibTableColumn
lportQ922State = _LportQ922State_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 166),
    _LportQ922State_Type()
)
lportQ922State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportQ922State.setStatus("mandatory")
_LportTrkPduRevision_Type = Integer32
_LportTrkPduRevision_Object = MibTableColumn
lportTrkPduRevision = _LportTrkPduRevision_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 167),
    _LportTrkPduRevision_Type()
)
lportTrkPduRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportTrkPduRevision.setStatus("mandatory")
_LportPVCMgrPduRevision_Type = Integer32
_LportPVCMgrPduRevision_Object = MibTableColumn
lportPVCMgrPduRevision = _LportPVCMgrPduRevision_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 168),
    _LportPVCMgrPduRevision_Type()
)
lportPVCMgrPduRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportPVCMgrPduRevision.setStatus("mandatory")
_LportDS0LoopStatus_Type = Integer32
_LportDS0LoopStatus_Object = MibTableColumn
lportDS0LoopStatus = _LportDS0LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 169),
    _LportDS0LoopStatus_Type()
)
lportDS0LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDS0LoopStatus.setStatus("mandatory")
_LportISDNDuration_Type = Integer32
_LportISDNDuration_Object = MibTableColumn
lportISDNDuration = _LportISDNDuration_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 170),
    _LportISDNDuration_Type()
)
lportISDNDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNDuration.setStatus("mandatory")
_LportISDNSourceAddr_Type = OctetString
_LportISDNSourceAddr_Object = MibTableColumn
lportISDNSourceAddr = _LportISDNSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 171),
    _LportISDNSourceAddr_Type()
)
lportISDNSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNSourceAddr.setStatus("mandatory")
_LportISDNDestAddr_Type = OctetString
_LportISDNDestAddr_Object = MibTableColumn
lportISDNDestAddr = _LportISDNDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 172),
    _LportISDNDestAddr_Type()
)
lportISDNDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNDestAddr.setStatus("mandatory")
_LportISDNIpAddr_Type = IpAddress
_LportISDNIpAddr_Object = MibTableColumn
lportISDNIpAddr = _LportISDNIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 173),
    _LportISDNIpAddr_Type()
)
lportISDNIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNIpAddr.setStatus("mandatory")
_LportISDNCallRejCause_Type = Integer32
_LportISDNCallRejCause_Object = MibTableColumn
lportISDNCallRejCause = _LportISDNCallRejCause_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 174),
    _LportISDNCallRejCause_Type()
)
lportISDNCallRejCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNCallRejCause.setStatus("mandatory")
_LportLastInvalidDLCI_Type = Integer32
_LportLastInvalidDLCI_Object = MibTableColumn
lportLastInvalidDLCI = _LportLastInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 175),
    _LportLastInvalidDLCI_Type()
)
lportLastInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportLastInvalidDLCI.setStatus("mandatory")


class _LportTrkProtState_Type(Integer32):
    """Custom type lportTrkProtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 3))
    )


_LportTrkProtState_Type.__name__ = "Integer32"
_LportTrkProtState_Object = MibTableColumn
lportTrkProtState = _LportTrkProtState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 176),
    _LportTrkProtState_Type()
)
lportTrkProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportTrkProtState.setStatus("mandatory")


class _LportTrkTrafficMix_Type(Integer32):
    """Custom type lportTrkTrafficMix based on Integer32"""
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
        *(("management-and-PVCs", 3),
          ("management-only", 2),
          ("normal", 1),
          ("private", 4))
    )


_LportTrkTrafficMix_Type.__name__ = "Integer32"
_LportTrkTrafficMix_Object = MibTableColumn
lportTrkTrafficMix = _LportTrkTrafficMix_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 177),
    _LportTrkTrafficMix_Type()
)
lportTrkTrafficMix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkTrafficMix.setStatus("mandatory")
_LportNumVC_Type = Integer32
_LportNumVC_Object = MibTableColumn
lportNumVC = _LportNumVC_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 178),
    _LportNumVC_Type()
)
lportNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportNumVC.setStatus("mandatory")
_LportTrkAdminCost_Type = Integer32
_LportTrkAdminCost_Object = MibTableColumn
lportTrkAdminCost = _LportTrkAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 179),
    _LportTrkAdminCost_Type()
)
lportTrkAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkAdminCost.setStatus("mandatory")
_LportPrivateNet_Type = Integer32
_LportPrivateNet_Object = MibTableColumn
lportPrivateNet = _LportPrivateNet_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 180),
    _LportPrivateNet_Type()
)
lportPrivateNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportPrivateNet.setStatus("mandatory")
_LportTrkStaticDelay_Type = Integer32
_LportTrkStaticDelay_Object = MibTableColumn
lportTrkStaticDelay = _LportTrkStaticDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 181),
    _LportTrkStaticDelay_Type()
)
lportTrkStaticDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkStaticDelay.setStatus("mandatory")
_LportTrkDynamicDelay_Type = Integer32
_LportTrkDynamicDelay_Object = MibTableColumn
lportTrkDynamicDelay = _LportTrkDynamicDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 182),
    _LportTrkDynamicDelay_Type()
)
lportTrkDynamicDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkDynamicDelay.setStatus("mandatory")
_LportAtmDataRateQoS1_Type = Integer32
_LportAtmDataRateQoS1_Object = MibTableColumn
lportAtmDataRateQoS1 = _LportAtmDataRateQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 183),
    _LportAtmDataRateQoS1_Type()
)
lportAtmDataRateQoS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmDataRateQoS1.setStatus("mandatory")
_LportAtmDataRateQoS2_Type = Integer32
_LportAtmDataRateQoS2_Object = MibTableColumn
lportAtmDataRateQoS2 = _LportAtmDataRateQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 184),
    _LportAtmDataRateQoS2_Type()
)
lportAtmDataRateQoS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmDataRateQoS2.setStatus("mandatory")
_LportAtmDataRateQoS3_Type = Integer32
_LportAtmDataRateQoS3_Object = MibTableColumn
lportAtmDataRateQoS3 = _LportAtmDataRateQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 185),
    _LportAtmDataRateQoS3_Type()
)
lportAtmDataRateQoS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmDataRateQoS3.setStatus("mandatory")
_LportAtmDataRateQoS4_Type = Integer32
_LportAtmDataRateQoS4_Object = MibTableColumn
lportAtmDataRateQoS4 = _LportAtmDataRateQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 186),
    _LportAtmDataRateQoS4_Type()
)
lportAtmDataRateQoS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmDataRateQoS4.setStatus("mandatory")
_LportOutVAvailbwQoS1_Type = Integer32
_LportOutVAvailbwQoS1_Object = MibTableColumn
lportOutVAvailbwQoS1 = _LportOutVAvailbwQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 187),
    _LportOutVAvailbwQoS1_Type()
)
lportOutVAvailbwQoS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutVAvailbwQoS1.setStatus("mandatory")
_LportOutVAvailbwQoS2_Type = Integer32
_LportOutVAvailbwQoS2_Object = MibTableColumn
lportOutVAvailbwQoS2 = _LportOutVAvailbwQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 188),
    _LportOutVAvailbwQoS2_Type()
)
lportOutVAvailbwQoS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutVAvailbwQoS2.setStatus("mandatory")
_LportOutVAvailbwQoS3_Type = Integer32
_LportOutVAvailbwQoS3_Object = MibTableColumn
lportOutVAvailbwQoS3 = _LportOutVAvailbwQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 189),
    _LportOutVAvailbwQoS3_Type()
)
lportOutVAvailbwQoS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutVAvailbwQoS3.setStatus("mandatory")
_LportOutVAvailbwQoS4_Type = Integer32
_LportOutVAvailbwQoS4_Object = MibTableColumn
lportOutVAvailbwQoS4 = _LportOutVAvailbwQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 190),
    _LportOutVAvailbwQoS4_Type()
)
lportOutVAvailbwQoS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutVAvailbwQoS4.setStatus("mandatory")
_LportInVAvailbwQoS1_Type = Integer32
_LportInVAvailbwQoS1_Object = MibTableColumn
lportInVAvailbwQoS1 = _LportInVAvailbwQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 191),
    _LportInVAvailbwQoS1_Type()
)
lportInVAvailbwQoS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInVAvailbwQoS1.setStatus("mandatory")
_LportInVAvailbwQoS2_Type = Integer32
_LportInVAvailbwQoS2_Object = MibTableColumn
lportInVAvailbwQoS2 = _LportInVAvailbwQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 192),
    _LportInVAvailbwQoS2_Type()
)
lportInVAvailbwQoS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInVAvailbwQoS2.setStatus("mandatory")
_LportInVAvailbwQoS3_Type = Integer32
_LportInVAvailbwQoS3_Object = MibTableColumn
lportInVAvailbwQoS3 = _LportInVAvailbwQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 193),
    _LportInVAvailbwQoS3_Type()
)
lportInVAvailbwQoS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInVAvailbwQoS3.setStatus("mandatory")
_LportInVAvailbwQoS4_Type = Integer32
_LportInVAvailbwQoS4_Object = MibTableColumn
lportInVAvailbwQoS4 = _LportInVAvailbwQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 194),
    _LportInVAvailbwQoS4_Type()
)
lportInVAvailbwQoS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInVAvailbwQoS4.setStatus("mandatory")
_LportOutAllocbwQoS1_Type = Integer32
_LportOutAllocbwQoS1_Object = MibTableColumn
lportOutAllocbwQoS1 = _LportOutAllocbwQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 195),
    _LportOutAllocbwQoS1_Type()
)
lportOutAllocbwQoS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutAllocbwQoS1.setStatus("mandatory")
_LportOutAllocbwQoS2_Type = Integer32
_LportOutAllocbwQoS2_Object = MibTableColumn
lportOutAllocbwQoS2 = _LportOutAllocbwQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 196),
    _LportOutAllocbwQoS2_Type()
)
lportOutAllocbwQoS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutAllocbwQoS2.setStatus("mandatory")
_LportOutAllocbwQoS3_Type = Integer32
_LportOutAllocbwQoS3_Object = MibTableColumn
lportOutAllocbwQoS3 = _LportOutAllocbwQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 197),
    _LportOutAllocbwQoS3_Type()
)
lportOutAllocbwQoS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutAllocbwQoS3.setStatus("mandatory")
_LportOutAllocbwQoS4_Type = Integer32
_LportOutAllocbwQoS4_Object = MibTableColumn
lportOutAllocbwQoS4 = _LportOutAllocbwQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 198),
    _LportOutAllocbwQoS4_Type()
)
lportOutAllocbwQoS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutAllocbwQoS4.setStatus("mandatory")
_LportInAllocbwQoS1_Type = Integer32
_LportInAllocbwQoS1_Object = MibTableColumn
lportInAllocbwQoS1 = _LportInAllocbwQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 199),
    _LportInAllocbwQoS1_Type()
)
lportInAllocbwQoS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInAllocbwQoS1.setStatus("mandatory")
_LportInAllocbwQoS2_Type = Integer32
_LportInAllocbwQoS2_Object = MibTableColumn
lportInAllocbwQoS2 = _LportInAllocbwQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 200),
    _LportInAllocbwQoS2_Type()
)
lportInAllocbwQoS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInAllocbwQoS2.setStatus("mandatory")
_LportInAllocbwQoS3_Type = Integer32
_LportInAllocbwQoS3_Object = MibTableColumn
lportInAllocbwQoS3 = _LportInAllocbwQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 201),
    _LportInAllocbwQoS3_Type()
)
lportInAllocbwQoS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInAllocbwQoS3.setStatus("mandatory")
_LportInAllocbwQoS4_Type = Integer32
_LportInAllocbwQoS4_Object = MibTableColumn
lportInAllocbwQoS4 = _LportInAllocbwQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 202),
    _LportInAllocbwQoS4_Type()
)
lportInAllocbwQoS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInAllocbwQoS4.setStatus("mandatory")


class _LportDynamicQoSbw_Type(Integer32):
    """Custom type lportDynamicQoSbw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qos-class-1", 1),
          ("qos-class-2", 2),
          ("qos-class-3", 4),
          ("qos-class-4", 8))
    )


_LportDynamicQoSbw_Type.__name__ = "Integer32"
_LportDynamicQoSbw_Object = MibTableColumn
lportDynamicQoSbw = _LportDynamicQoSbw_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 203),
    _LportDynamicQoSbw_Type()
)
lportDynamicQoSbw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDynamicQoSbw.setStatus("mandatory")
_LportSVCRetryTimer_Type = Integer32
_LportSVCRetryTimer_Object = MibTableColumn
lportSVCRetryTimer = _LportSVCRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 204),
    _LportSVCRetryTimer_Type()
)
lportSVCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSVCRetryTimer.setStatus("mandatory")


class _LportAtmNetworkType_Type(Integer32):
    """Custom type lportAtmNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("public", 2))
    )


_LportAtmNetworkType_Type.__name__ = "Integer32"
_LportAtmNetworkType_Object = MibTableColumn
lportAtmNetworkType = _LportAtmNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 205),
    _LportAtmNetworkType_Type()
)
lportAtmNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmNetworkType.setStatus("mandatory")


class _LportAtmRouteMetricQoS1_Type(Integer32):
    """Custom type lportAtmRouteMetricQoS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrative-cost", 1),
          ("cell-delay-variation", 3),
          ("end-to-end-delay", 2))
    )


_LportAtmRouteMetricQoS1_Type.__name__ = "Integer32"
_LportAtmRouteMetricQoS1_Object = MibTableColumn
lportAtmRouteMetricQoS1 = _LportAtmRouteMetricQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 206),
    _LportAtmRouteMetricQoS1_Type()
)
lportAtmRouteMetricQoS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmRouteMetricQoS1.setStatus("mandatory")


class _LportAtmRouteMetricQoS2_Type(Integer32):
    """Custom type lportAtmRouteMetricQoS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrative-cost", 1),
          ("cell-delay-variation", 3),
          ("end-to-end-delay", 2))
    )


_LportAtmRouteMetricQoS2_Type.__name__ = "Integer32"
_LportAtmRouteMetricQoS2_Object = MibTableColumn
lportAtmRouteMetricQoS2 = _LportAtmRouteMetricQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 207),
    _LportAtmRouteMetricQoS2_Type()
)
lportAtmRouteMetricQoS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmRouteMetricQoS2.setStatus("mandatory")


class _LportAtmRouteMetricQoS3_Type(Integer32):
    """Custom type lportAtmRouteMetricQoS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrative-cost", 1),
          ("cell-delay-variation", 3),
          ("end-to-end-delay", 2))
    )


_LportAtmRouteMetricQoS3_Type.__name__ = "Integer32"
_LportAtmRouteMetricQoS3_Object = MibTableColumn
lportAtmRouteMetricQoS3 = _LportAtmRouteMetricQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 208),
    _LportAtmRouteMetricQoS3_Type()
)
lportAtmRouteMetricQoS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmRouteMetricQoS3.setStatus("mandatory")


class _LportAtmRouteMetricQoS4_Type(Integer32):
    """Custom type lportAtmRouteMetricQoS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrative-cost", 1),
          ("cell-delay-variation", 3),
          ("end-to-end-delay", 2))
    )


_LportAtmRouteMetricQoS4_Type.__name__ = "Integer32"
_LportAtmRouteMetricQoS4_Object = MibTableColumn
lportAtmRouteMetricQoS4 = _LportAtmRouteMetricQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 209),
    _LportAtmRouteMetricQoS4_Type()
)
lportAtmRouteMetricQoS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmRouteMetricQoS4.setStatus("mandatory")
_LportIlmiPollTimeout_Type = Integer32
_LportIlmiPollTimeout_Object = MibTableColumn
lportIlmiPollTimeout = _LportIlmiPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 210),
    _LportIlmiPollTimeout_Type()
)
lportIlmiPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportIlmiPollTimeout.setStatus("mandatory")


class _LportAtmProtocol_Type(Integer32):
    """Custom type lportAtmProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 3),
          ("uni-30", 1),
          ("uni-31", 2))
    )


_LportAtmProtocol_Type.__name__ = "Integer32"
_LportAtmProtocol_Object = MibTableColumn
lportAtmProtocol = _LportAtmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 211),
    _LportAtmProtocol_Type()
)
lportAtmProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmProtocol.setStatus("mandatory")


class _LportIlmiAdminStatus_Type(Integer32):
    """Custom type lportIlmiAdminStatus based on Integer32"""
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


_LportIlmiAdminStatus_Type.__name__ = "Integer32"
_LportIlmiAdminStatus_Object = MibTableColumn
lportIlmiAdminStatus = _LportIlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 212),
    _LportIlmiAdminStatus_Type()
)
lportIlmiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportIlmiAdminStatus.setStatus("mandatory")


class _LportIlmiOperStatus_Type(Integer32):
    """Custom type lportIlmiOperStatus based on Integer32"""
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
          ("registering", 2),
          ("up", 3))
    )


_LportIlmiOperStatus_Type.__name__ = "Integer32"
_LportIlmiOperStatus_Object = MibTableColumn
lportIlmiOperStatus = _LportIlmiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 213),
    _LportIlmiOperStatus_Type()
)
lportIlmiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportIlmiOperStatus.setStatus("mandatory")
_LportIlmiPollRetry_Type = Counter32
_LportIlmiPollRetry_Object = MibTableColumn
lportIlmiPollRetry = _LportIlmiPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 214),
    _LportIlmiPollRetry_Type()
)
lportIlmiPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportIlmiPollRetry.setStatus("mandatory")
_LportAtmVpiBits_Type = Integer32
_LportAtmVpiBits_Object = MibTableColumn
lportAtmVpiBits = _LportAtmVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 215),
    _LportAtmVpiBits_Type()
)
lportAtmVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmVpiBits.setStatus("mandatory")
_LportAtmVciBits_Type = Integer32
_LportAtmVciBits_Object = MibTableColumn
lportAtmVciBits = _LportAtmVciBits_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 216),
    _LportAtmVciBits_Type()
)
lportAtmVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmVciBits.setStatus("mandatory")


class _LportAtmOamAlarmEnable_Type(Integer32):
    """Custom type lportAtmOamAlarmEnable based on Integer32"""
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


_LportAtmOamAlarmEnable_Type.__name__ = "Integer32"
_LportAtmOamAlarmEnable_Object = MibTableColumn
lportAtmOamAlarmEnable = _LportAtmOamAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 217),
    _LportAtmOamAlarmEnable_Type()
)
lportAtmOamAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportAtmOamAlarmEnable.setStatus("mandatory")
_LportInVAvailbw_Type = Integer32
_LportInVAvailbw_Object = MibTableColumn
lportInVAvailbw = _LportInVAvailbw_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 218),
    _LportInVAvailbw_Type()
)
lportInVAvailbw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInVAvailbw.setStatus("mandatory")


class _LportbwUNIPolicy_Type(Integer32):
    """Custom type lportbwUNIPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-uni-bw-policing", 2),
          ("enable-uni-bw-policing", 1))
    )


_LportbwUNIPolicy_Type.__name__ = "Integer32"
_LportbwUNIPolicy_Object = MibTableColumn
lportbwUNIPolicy = _LportbwUNIPolicy_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 219),
    _LportbwUNIPolicy_Type()
)
lportbwUNIPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportbwUNIPolicy.setStatus("mandatory")


class _LportStarvation_Type(Integer32):
    """Custom type lportStarvation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_LportStarvation_Type.__name__ = "Integer32"
_LportStarvation_Object = MibTableColumn
lportStarvation = _LportStarvation_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 220),
    _LportStarvation_Type()
)
lportStarvation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportStarvation.setStatus("mandatory")


class _LportRecOverflow_Type(Integer32):
    """Custom type lportRecOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_LportRecOverflow_Type.__name__ = "Integer32"
_LportRecOverflow_Object = MibTableColumn
lportRecOverflow = _LportRecOverflow_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 221),
    _LportRecOverflow_Type()
)
lportRecOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportRecOverflow.setStatus("mandatory")


class _LportLossOfCellSequence_Type(Integer32):
    """Custom type lportLossOfCellSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_LportLossOfCellSequence_Type.__name__ = "Integer32"
_LportLossOfCellSequence_Object = MibTableColumn
lportLossOfCellSequence = _LportLossOfCellSequence_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 222),
    _LportLossOfCellSequence_Type()
)
lportLossOfCellSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportLossOfCellSequence.setStatus("mandatory")


class _LportLossOfStructurePointer_Type(Integer32):
    """Custom type lportLossOfStructurePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_LportLossOfStructurePointer_Type.__name__ = "Integer32"
_LportLossOfStructurePointer_Object = MibTableColumn
lportLossOfStructurePointer = _LportLossOfStructurePointer_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 223),
    _LportLossOfStructurePointer_Type()
)
lportLossOfStructurePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportLossOfStructurePointer.setStatus("mandatory")
_LportCbrInsDummyCells_Type = Counter32
_LportCbrInsDummyCells_Object = MibTableColumn
lportCbrInsDummyCells = _LportCbrInsDummyCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 224),
    _LportCbrInsDummyCells_Type()
)
lportCbrInsDummyCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCbrInsDummyCells.setStatus("mandatory")
_LportRecFifoUnderflowCnt_Type = Counter32
_LportRecFifoUnderflowCnt_Object = MibTableColumn
lportRecFifoUnderflowCnt = _LportRecFifoUnderflowCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 225),
    _LportRecFifoUnderflowCnt_Type()
)
lportRecFifoUnderflowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportRecFifoUnderflowCnt.setStatus("mandatory")
_LportRecFifoOverflowCnt_Type = Counter32
_LportRecFifoOverflowCnt_Object = MibTableColumn
lportRecFifoOverflowCnt = _LportRecFifoOverflowCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 226),
    _LportRecFifoOverflowCnt_Type()
)
lportRecFifoOverflowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportRecFifoOverflowCnt.setStatus("mandatory")
_LportCbrLossOfStructurePointerCnt_Type = Counter32
_LportCbrLossOfStructurePointerCnt_Object = MibTableColumn
lportCbrLossOfStructurePointerCnt = _LportCbrLossOfStructurePointerCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 227),
    _LportCbrLossOfStructurePointerCnt_Type()
)
lportCbrLossOfStructurePointerCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCbrLossOfStructurePointerCnt.setStatus("mandatory")
_LportCbrLossOfCellSequenceCnt_Type = Counter32
_LportCbrLossOfCellSequenceCnt_Object = MibTableColumn
lportCbrLossOfCellSequenceCnt = _LportCbrLossOfCellSequenceCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 228),
    _LportCbrLossOfCellSequenceCnt_Type()
)
lportCbrLossOfCellSequenceCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCbrLossOfCellSequenceCnt.setStatus("mandatory")
_LportShaperId_Type = Integer32
_LportShaperId_Object = MibTableColumn
lportShaperId = _LportShaperId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 229),
    _LportShaperId_Type()
)
lportShaperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportShaperId.setStatus("mandatory")


class _LportIlmiPrefixScreenMode_Type(Integer32):
    """Custom type lportIlmiPrefixScreenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accept-all", 255),
          ("node-prefix", 1),
          ("node-prefix-or-port-prefix", 3),
          ("port-prefix", 2),
          ("reject-all", 127))
    )


_LportIlmiPrefixScreenMode_Type.__name__ = "Integer32"
_LportIlmiPrefixScreenMode_Object = MibTableColumn
lportIlmiPrefixScreenMode = _LportIlmiPrefixScreenMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 230),
    _LportIlmiPrefixScreenMode_Type()
)
lportIlmiPrefixScreenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportIlmiPrefixScreenMode.setStatus("mandatory")


class _LportSmdsPduViolTca_Type(Integer32):
    """Custom type lportSmdsPduViolTca based on Integer32"""
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


_LportSmdsPduViolTca_Type.__name__ = "Integer32"
_LportSmdsPduViolTca_Object = MibTableColumn
lportSmdsPduViolTca = _LportSmdsPduViolTca_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 231),
    _LportSmdsPduViolTca_Type()
)
lportSmdsPduViolTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsPduViolTca.setStatus("mandatory")
_LportSmdsPduViolThresh_Type = Integer32
_LportSmdsPduViolThresh_Object = MibTableColumn
lportSmdsPduViolThresh = _LportSmdsPduViolThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 232),
    _LportSmdsPduViolThresh_Type()
)
lportSmdsPduViolThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportSmdsPduViolThresh.setStatus("mandatory")
_LportSmdsPduHdrSip3SaNotFound_Type = OctetString
_LportSmdsPduHdrSip3SaNotFound_Object = MibTableColumn
lportSmdsPduHdrSip3SaNotFound = _LportSmdsPduHdrSip3SaNotFound_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 233),
    _LportSmdsPduHdrSip3SaNotFound_Type()
)
lportSmdsPduHdrSip3SaNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3SaNotFound.setStatus("mandatory")
_LportSmdsPduHdrSip3SaDaOnSamePort_Type = OctetString
_LportSmdsPduHdrSip3SaDaOnSamePort_Object = MibTableColumn
lportSmdsPduHdrSip3SaDaOnSamePort = _LportSmdsPduHdrSip3SaDaOnSamePort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 234),
    _LportSmdsPduHdrSip3SaDaOnSamePort_Type()
)
lportSmdsPduHdrSip3SaDaOnSamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3SaDaOnSamePort.setStatus("mandatory")
_LportSmdsPduHdrSip3DstGaNotFound_Type = OctetString
_LportSmdsPduHdrSip3DstGaNotFound_Object = MibTableColumn
lportSmdsPduHdrSip3DstGaNotFound = _LportSmdsPduHdrSip3DstGaNotFound_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 235),
    _LportSmdsPduHdrSip3DstGaNotFound_Type()
)
lportSmdsPduHdrSip3DstGaNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3DstGaNotFound.setStatus("mandatory")
_LportSmdsPduHdrSip3DstIaScrnFail_Type = OctetString
_LportSmdsPduHdrSip3DstIaScrnFail_Object = MibTableColumn
lportSmdsPduHdrSip3DstIaScrnFail = _LportSmdsPduHdrSip3DstIaScrnFail_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 236),
    _LportSmdsPduHdrSip3DstIaScrnFail_Type()
)
lportSmdsPduHdrSip3DstIaScrnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3DstIaScrnFail.setStatus("mandatory")
_LportSmdsPduHdrSip3SaValFail_Type = OctetString
_LportSmdsPduHdrSip3SaValFail_Object = MibTableColumn
lportSmdsPduHdrSip3SaValFail = _LportSmdsPduHdrSip3SaValFail_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 237),
    _LportSmdsPduHdrSip3SaValFail_Type()
)
lportSmdsPduHdrSip3SaValFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3SaValFail.setStatus("mandatory")
_LportSmdsPduHdrSip3DstIaNotFound_Type = OctetString
_LportSmdsPduHdrSip3DstIaNotFound_Object = MibTableColumn
lportSmdsPduHdrSip3DstIaNotFound = _LportSmdsPduHdrSip3DstIaNotFound_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 238),
    _LportSmdsPduHdrSip3DstIaNotFound_Type()
)
lportSmdsPduHdrSip3DstIaNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3DstIaNotFound.setStatus("mandatory")
_LportSmdsPduHdrSip3SrcIaScrnFail_Type = OctetString
_LportSmdsPduHdrSip3SrcIaScrnFail_Object = MibTableColumn
lportSmdsPduHdrSip3SrcIaScrnFail = _LportSmdsPduHdrSip3SrcIaScrnFail_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 239),
    _LportSmdsPduHdrSip3SrcIaScrnFail_Type()
)
lportSmdsPduHdrSip3SrcIaScrnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3SrcIaScrnFail.setStatus("mandatory")
_LportSmdsPduHdrSip3DstGaScrnFail_Type = OctetString
_LportSmdsPduHdrSip3DstGaScrnFail_Object = MibTableColumn
lportSmdsPduHdrSip3DstGaScrnFail = _LportSmdsPduHdrSip3DstGaScrnFail_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 240),
    _LportSmdsPduHdrSip3DstGaScrnFail_Type()
)
lportSmdsPduHdrSip3DstGaScrnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3DstGaScrnFail.setStatus("mandatory")
_LportSmdsPduHdrSip3SaTypeInvalid_Type = OctetString
_LportSmdsPduHdrSip3SaTypeInvalid_Object = MibTableColumn
lportSmdsPduHdrSip3SaTypeInvalid = _LportSmdsPduHdrSip3SaTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 241),
    _LportSmdsPduHdrSip3SaTypeInvalid_Type()
)
lportSmdsPduHdrSip3SaTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3SaTypeInvalid.setStatus("mandatory")
_LportSmdsPduHdrSip3DaTypeInvalid_Type = OctetString
_LportSmdsPduHdrSip3DaTypeInvalid_Object = MibTableColumn
lportSmdsPduHdrSip3DaTypeInvalid = _LportSmdsPduHdrSip3DaTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 242),
    _LportSmdsPduHdrSip3DaTypeInvalid_Type()
)
lportSmdsPduHdrSip3DaTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrSip3DaTypeInvalid.setStatus("mandatory")
_LportSmdsPduHdrDxi2LinkIdInvalid_Type = OctetString
_LportSmdsPduHdrDxi2LinkIdInvalid_Object = MibTableColumn
lportSmdsPduHdrDxi2LinkIdInvalid = _LportSmdsPduHdrDxi2LinkIdInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 243),
    _LportSmdsPduHdrDxi2LinkIdInvalid_Type()
)
lportSmdsPduHdrDxi2LinkIdInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrDxi2LinkIdInvalid.setStatus("mandatory")
_LportSmdsPduHdrDxi2CrInvalid_Type = OctetString
_LportSmdsPduHdrDxi2CrInvalid_Object = MibTableColumn
lportSmdsPduHdrDxi2CrInvalid = _LportSmdsPduHdrDxi2CrInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 244),
    _LportSmdsPduHdrDxi2CrInvalid_Type()
)
lportSmdsPduHdrDxi2CrInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrDxi2CrInvalid.setStatus("mandatory")
_LportSmdsPduHdrDxi2CtrlInvalid_Type = OctetString
_LportSmdsPduHdrDxi2CtrlInvalid_Object = MibTableColumn
lportSmdsPduHdrDxi2CtrlInvalid = _LportSmdsPduHdrDxi2CtrlInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 245),
    _LportSmdsPduHdrDxi2CtrlInvalid_Type()
)
lportSmdsPduHdrDxi2CtrlInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrDxi2CtrlInvalid.setStatus("mandatory")
_LportSmdsPduHdrDxi2StationIdInvalid_Type = OctetString
_LportSmdsPduHdrDxi2StationIdInvalid_Object = MibTableColumn
lportSmdsPduHdrDxi2StationIdInvalid = _LportSmdsPduHdrDxi2StationIdInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 246),
    _LportSmdsPduHdrDxi2StationIdInvalid_Type()
)
lportSmdsPduHdrDxi2StationIdInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrDxi2StationIdInvalid.setStatus("mandatory")
_LportSmdsPduHdrDxi2AeInvalid_Type = OctetString
_LportSmdsPduHdrDxi2AeInvalid_Object = MibTableColumn
lportSmdsPduHdrDxi2AeInvalid = _LportSmdsPduHdrDxi2AeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 247),
    _LportSmdsPduHdrDxi2AeInvalid_Type()
)
lportSmdsPduHdrDxi2AeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportSmdsPduHdrDxi2AeInvalid.setStatus("mandatory")
_LportDS0FarendLpbkEnabled_Type = Integer32
_LportDS0FarendLpbkEnabled_Object = MibTableColumn
lportDS0FarendLpbkEnabled = _LportDS0FarendLpbkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 248),
    _LportDS0FarendLpbkEnabled_Type()
)
lportDS0FarendLpbkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDS0FarendLpbkEnabled.setStatus("mandatory")
_LportDS0FarendLpbkDisabled_Type = Integer32
_LportDS0FarendLpbkDisabled_Object = MibTableColumn
lportDS0FarendLpbkDisabled = _LportDS0FarendLpbkDisabled_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 249),
    _LportDS0FarendLpbkDisabled_Type()
)
lportDS0FarendLpbkDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportDS0FarendLpbkDisabled.setStatus("mandatory")
_LportTrkProtFailureThreshold_Type = Integer32
_LportTrkProtFailureThreshold_Object = MibTableColumn
lportTrkProtFailureThreshold = _LportTrkProtFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 250),
    _LportTrkProtFailureThreshold_Type()
)
lportTrkProtFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkProtFailureThreshold.setStatus("mandatory")
_LportPtr_Type = OctetString
_LportPtr_Object = MibTableColumn
lportPtr = _LportPtr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 251),
    _LportPtr_Type()
)
lportPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportPtr.setStatus("mandatory")
_LportISDNPoolUtil_Type = Integer32
_LportISDNPoolUtil_Object = MibTableColumn
lportISDNPoolUtil = _LportISDNPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 252),
    _LportISDNPoolUtil_Type()
)
lportISDNPoolUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNPoolUtil.setStatus("mandatory")
_LportISDNIpAddrAssignFail_Type = Integer32
_LportISDNIpAddrAssignFail_Object = MibTableColumn
lportISDNIpAddrAssignFail = _LportISDNIpAddrAssignFail_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 253),
    _LportISDNIpAddrAssignFail_Type()
)
lportISDNIpAddrAssignFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportISDNIpAddrAssignFail.setStatus("mandatory")
_LportTrkUtilQoS1_Type = Integer32
_LportTrkUtilQoS1_Object = MibTableColumn
lportTrkUtilQoS1 = _LportTrkUtilQoS1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 254),
    _LportTrkUtilQoS1_Type()
)
lportTrkUtilQoS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkUtilQoS1.setStatus("mandatory")
_LportTrkUtilQoS2_Type = Integer32
_LportTrkUtilQoS2_Object = MibTableColumn
lportTrkUtilQoS2 = _LportTrkUtilQoS2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 255),
    _LportTrkUtilQoS2_Type()
)
lportTrkUtilQoS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkUtilQoS2.setStatus("mandatory")
_LportTrkUtilQoS3_Type = Integer32
_LportTrkUtilQoS3_Object = MibTableColumn
lportTrkUtilQoS3 = _LportTrkUtilQoS3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 256),
    _LportTrkUtilQoS3_Type()
)
lportTrkUtilQoS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkUtilQoS3.setStatus("mandatory")
_LportTrkUtilQoS4_Type = Integer32
_LportTrkUtilQoS4_Object = MibTableColumn
lportTrkUtilQoS4 = _LportTrkUtilQoS4_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 257),
    _LportTrkUtilQoS4_Type()
)
lportTrkUtilQoS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportTrkUtilQoS4.setStatus("mandatory")
_LportInCells_Type = Counter32
_LportInCells_Object = MibTableColumn
lportInCells = _LportInCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 267),
    _LportInCells_Type()
)
lportInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportInCells.setStatus("mandatory")
_LportOutCells_Type = Counter32
_LportOutCells_Object = MibTableColumn
lportOutCells = _LportOutCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 5, 1, 1, 268),
    _LportOutCells_Type()
)
lportOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportOutCells.setStatus("mandatory")
_Ckt_ObjectIdentity = ObjectIdentity
ckt = _Ckt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 6)
)
_CktTable_Object = MibTable
cktTable = _CktTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cktTable.setStatus("mandatory")
_CktEntry_Object = MibTableRow
cktEntry = _CktEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1)
)
cktEntry.setIndexNames(
    (0, "CASCADE-MIB", "cktSrcIfIndex"),
    (0, "CASCADE-MIB", "cktSrcDlci"),
)
if mibBuilder.loadTexts:
    cktEntry.setStatus("mandatory")
_CktSrcIfIndex_Type = Index
_CktSrcIfIndex_Object = MibTableColumn
cktSrcIfIndex = _CktSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 1),
    _CktSrcIfIndex_Type()
)
cktSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSrcIfIndex.setStatus("mandatory")
_CktSrcDlci_Type = Integer32
_CktSrcDlci_Object = MibTableColumn
cktSrcDlci = _CktSrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 2),
    _CktSrcDlci_Type()
)
cktSrcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSrcDlci.setStatus("mandatory")
_CktPriority_Type = Integer32
_CktPriority_Object = MibTableColumn
cktPriority = _CktPriority_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 3),
    _CktPriority_Type()
)
cktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktPriority.setStatus("mandatory")
_CktCir_Type = Integer32
_CktCir_Object = MibTableColumn
cktCir = _CktCir_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 4),
    _CktCir_Type()
)
cktCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktCir.setStatus("mandatory")
_CktBc_Type = Integer32
_CktBc_Object = MibTableColumn
cktBc = _CktBc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 5),
    _CktBc_Type()
)
cktBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktBc.setStatus("mandatory")
_CktBe_Type = Integer32
_CktBe_Object = MibTableColumn
cktBe = _CktBe_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 6),
    _CktBe_Type()
)
cktBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktBe.setStatus("mandatory")
_CktDestNodeId_Type = Integer32
_CktDestNodeId_Object = MibTableColumn
cktDestNodeId = _CktDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 7),
    _CktDestNodeId_Type()
)
cktDestNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDestNodeId.setStatus("mandatory")
_CktDestIfIndex_Type = Integer32
_CktDestIfIndex_Object = MibTableColumn
cktDestIfIndex = _CktDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 8),
    _CktDestIfIndex_Type()
)
cktDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDestIfIndex.setStatus("mandatory")
_CktDestDlci_Type = Integer32
_CktDestDlci_Object = MibTableColumn
cktDestDlci = _CktDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 9),
    _CktDestDlci_Type()
)
cktDestDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDestDlci.setStatus("mandatory")


class _CktTos_Type(Integer32):
    """Custom type cktTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("committed", 1),
          ("shared", 2))
    )


_CktTos_Type.__name__ = "Integer32"
_CktTos_Object = MibTableColumn
cktTos = _CktTos_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 10),
    _CktTos_Type()
)
cktTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTos.setStatus("mandatory")


class _CktOde_Type(Integer32):
    """Custom type cktOde based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_CktOde_Type.__name__ = "Integer32"
_CktOde_Object = MibTableColumn
cktOde = _CktOde_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 11),
    _CktOde_Type()
)
cktOde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOde.setStatus("mandatory")


class _CktAdminStatus_Type(Integer32):
    """Custom type cktAdminStatus based on Integer32"""
    defaultValue = 2

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


_CktAdminStatus_Type.__name__ = "Integer32"
_CktAdminStatus_Object = MibTableColumn
cktAdminStatus = _CktAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 12),
    _CktAdminStatus_Type()
)
cktAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAdminStatus.setStatus("mandatory")
_CktCreationTime_Type = TimeTicks
_CktCreationTime_Object = MibTableColumn
cktCreationTime = _CktCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 13),
    _CktCreationTime_Type()
)
cktCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktCreationTime.setStatus("mandatory")
_CktLastTimeChange_Type = TimeTicks
_CktLastTimeChange_Object = MibTableColumn
cktLastTimeChange = _CktLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 14),
    _CktLastTimeChange_Type()
)
cktLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLastTimeChange.setStatus("mandatory")


class _CktVcState_Type(Integer32):
    """Custom type cktVcState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("backedup", 9),
          ("calling", 3),
          ("inactive", 1),
          ("retry", 2),
          ("slowretry", 12),
          ("svcall", 7),
          ("svclr", 8),
          ("wcbbkdp", 10),
          ("wcbdeact", 4),
          ("wcbdelete", 5),
          ("wcbreact", 11))
    )


_CktVcState_Type.__name__ = "Integer32"
_CktVcState_Object = MibTableColumn
cktVcState = _CktVcState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 15),
    _CktVcState_Type()
)
cktVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktVcState.setStatus("mandatory")


class _CktDceState_Type(Integer32):
    """Custom type cktDceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktDceState_Type.__name__ = "Integer32"
_CktDceState_Object = MibTableColumn
cktDceState = _CktDceState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 16),
    _CktDceState_Type()
)
cktDceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktDceState.setStatus("mandatory")


class _CktDteStatus_Type(Integer32):
    """Custom type cktDteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktDteStatus_Type.__name__ = "Integer32"
_CktDteStatus_Object = MibTableColumn
cktDteStatus = _CktDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 17),
    _CktDteStatus_Type()
)
cktDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktDteStatus.setStatus("mandatory")


class _CktRnr_Type(Integer32):
    """Custom type cktRnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recvnotready", 1)
    )


_CktRnr_Type.__name__ = "Integer32"
_CktRnr_Object = MibTableColumn
cktRnr = _CktRnr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 18),
    _CktRnr_Type()
)
cktRnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRnr.setStatus("mandatory")


class _CktNiDown_Type(Integer32):
    """Custom type cktNiDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nidown", 1)
    )


_CktNiDown_Type.__name__ = "Integer32"
_CktNiDown_Object = MibTableColumn
cktNiDown = _CktNiDown_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 19),
    _CktNiDown_Type()
)
cktNiDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktNiDown.setStatus("mandatory")


class _CktDteState_Type(Integer32):
    """Custom type cktDteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktDteState_Type.__name__ = "Integer32"
_CktDteState_Object = MibTableColumn
cktDteState = _CktDteState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 20),
    _CktDteState_Type()
)
cktDteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktDteState.setStatus("mandatory")


class _CktOperStatus_Type(Integer32):
    """Custom type cktOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktOperStatus_Type.__name__ = "Integer32"
_CktOperStatus_Object = MibTableColumn
cktOperStatus = _CktOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 21),
    _CktOperStatus_Type()
)
cktOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOperStatus.setStatus("mandatory")


class _CktOutForward_Type(Integer32):
    """Custom type cktOutForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_CktOutForward_Type.__name__ = "Integer32"
_CktOutForward_Object = MibTableColumn
cktOutForward = _CktOutForward_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 22),
    _CktOutForward_Type()
)
cktOutForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutForward.setStatus("mandatory")
_CktRerouteCnt_Type = Integer32
_CktRerouteCnt_Object = MibTableColumn
cktRerouteCnt = _CktRerouteCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 23),
    _CktRerouteCnt_Type()
)
cktRerouteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRerouteCnt.setStatus("mandatory")
_CktVcPtr_Type = OctetString
_CktVcPtr_Object = MibTableColumn
cktVcPtr = _CktVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 24),
    _CktVcPtr_Type()
)
cktVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktVcPtr.setStatus("mandatory")
_CktHopCnt_Type = Integer32
_CktHopCnt_Object = MibTableColumn
cktHopCnt = _CktHopCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 25),
    _CktHopCnt_Type()
)
cktHopCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktHopCnt.setStatus("mandatory")
_CktPath_Type = OctetString
_CktPath_Object = MibTableColumn
cktPath = _CktPath_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 26),
    _CktPath_Type()
)
cktPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktPath.setStatus("mandatory")


class _CktFailReason_Type(Integer32):
    """Custom type cktFailReason based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 1),
          ("balancereroute", 10),
          ("bkpdlcicollision", 25),
          ("bothendptbackup", 29),
          ("dead", 11),
          ("defpathreroute", 12),
          ("dstunknown", 24),
          ("iopdown", 17),
          ("misconfig", 20),
          ("nevercalled", 28),
          ("nidown", 13),
          ("nobw", 3),
          ("nodest", 7),
          ("nomultipointparent", 31),
          ("nopdubuff", 6),
          ("noport", 19),
          ("noroute", 4),
          ("novcbuff", 2),
          ("novpivci", 33),
          ("numsgbuffer", 18),
          ("oldrevinpath", 26),
          ("otherpvcsegdown", 14),
          ("otherpvcsegrnr", 15),
          ("pvcroutefail", 32),
          ("pvcroutemgttrunk", 30),
          ("smdsmgmttrunk", 27),
          ("srcbackedup", 22),
          ("srcunknown", 23),
          ("svcsetupfail", 21),
          ("timeout", 5),
          ("trkdown", 9),
          ("trkrnr", 8),
          ("usingaltpathwarning", 16))
    )


_CktFailReason_Type.__name__ = "Integer32"
_CktFailReason_Object = MibTableColumn
cktFailReason = _CktFailReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 27),
    _CktFailReason_Type()
)
cktFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktFailReason.setStatus("mandatory")
_CktFailNode_Type = Integer32
_CktFailNode_Object = MibTableColumn
cktFailNode = _CktFailNode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 28),
    _CktFailNode_Type()
)
cktFailNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktFailNode.setStatus("mandatory")
_CktFailPort_Type = Integer32
_CktFailPort_Object = MibTableColumn
cktFailPort = _CktFailPort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 29),
    _CktFailPort_Type()
)
cktFailPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktFailPort.setStatus("mandatory")
_CktMcastGroupId_Type = Integer32
_CktMcastGroupId_Object = MibTableColumn
cktMcastGroupId = _CktMcastGroupId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 30),
    _CktMcastGroupId_Type()
)
cktMcastGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMcastGroupId.setStatus("mandatory")
_CktMcastMemberList_Type = OctetString
_CktMcastMemberList_Object = MibTableColumn
cktMcastMemberList = _CktMcastMemberList_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 31),
    _CktMcastMemberList_Type()
)
cktMcastMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMcastMemberList.setStatus("mandatory")
_CktMcastParentGroups_Type = OctetString
_CktMcastParentGroups_Object = MibTableColumn
cktMcastParentGroups = _CktMcastParentGroups_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 32),
    _CktMcastParentGroups_Type()
)
cktMcastParentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktMcastParentGroups.setStatus("mandatory")
_CktInFrames_Type = Counter32
_CktInFrames_Object = MibTableColumn
cktInFrames = _CktInFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 33),
    _CktInFrames_Type()
)
cktInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInFrames.setStatus("mandatory")
_CktInDEFrames_Type = Counter32
_CktInDEFrames_Object = MibTableColumn
cktInDEFrames = _CktInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 34),
    _CktInDEFrames_Type()
)
cktInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInDEFrames.setStatus("mandatory")
_CktInODEFrames_Type = Counter32
_CktInODEFrames_Object = MibTableColumn
cktInODEFrames = _CktInODEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 35),
    _CktInODEFrames_Type()
)
cktInODEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInODEFrames.setStatus("mandatory")
_CktInFECNFrames_Type = Counter32
_CktInFECNFrames_Object = MibTableColumn
cktInFECNFrames = _CktInFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 36),
    _CktInFECNFrames_Type()
)
cktInFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInFECNFrames.setStatus("mandatory")
_CktInBECNFrames_Type = Counter32
_CktInBECNFrames_Object = MibTableColumn
cktInBECNFrames = _CktInBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 37),
    _CktInBECNFrames_Type()
)
cktInBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInBECNFrames.setStatus("mandatory")
_CktInDiscards_Type = Counter32
_CktInDiscards_Object = MibTableColumn
cktInDiscards = _CktInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 38),
    _CktInDiscards_Type()
)
cktInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInDiscards.setStatus("mandatory")
_CktInOctets_Type = Counter32
_CktInOctets_Object = MibTableColumn
cktInOctets = _CktInOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 39),
    _CktInOctets_Type()
)
cktInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInOctets.setStatus("mandatory")
_CktInDEOctets_Type = Counter32
_CktInDEOctets_Object = MibTableColumn
cktInDEOctets = _CktInDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 40),
    _CktInDEOctets_Type()
)
cktInDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInDEOctets.setStatus("mandatory")
_CktInODEOctets_Type = Counter32
_CktInODEOctets_Object = MibTableColumn
cktInODEOctets = _CktInODEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 41),
    _CktInODEOctets_Type()
)
cktInODEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInODEOctets.setStatus("mandatory")
_CktOutFrames_Type = Counter32
_CktOutFrames_Object = MibTableColumn
cktOutFrames = _CktOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 42),
    _CktOutFrames_Type()
)
cktOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutFrames.setStatus("mandatory")
_CktOutDEFrames_Type = Counter32
_CktOutDEFrames_Object = MibTableColumn
cktOutDEFrames = _CktOutDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 43),
    _CktOutDEFrames_Type()
)
cktOutDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutDEFrames.setStatus("mandatory")
_CktOutODEFrames_Type = Counter32
_CktOutODEFrames_Object = MibTableColumn
cktOutODEFrames = _CktOutODEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 44),
    _CktOutODEFrames_Type()
)
cktOutODEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutODEFrames.setStatus("mandatory")
_CktOutFECNFrames_Type = Counter32
_CktOutFECNFrames_Object = MibTableColumn
cktOutFECNFrames = _CktOutFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 45),
    _CktOutFECNFrames_Type()
)
cktOutFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutFECNFrames.setStatus("mandatory")
_CktOutBECNFrames_Type = Counter32
_CktOutBECNFrames_Object = MibTableColumn
cktOutBECNFrames = _CktOutBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 46),
    _CktOutBECNFrames_Type()
)
cktOutBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutBECNFrames.setStatus("mandatory")
_CktOutOctets_Type = Counter32
_CktOutOctets_Object = MibTableColumn
cktOutOctets = _CktOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 47),
    _CktOutOctets_Type()
)
cktOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutOctets.setStatus("mandatory")
_CktOutDEOctets_Type = Counter32
_CktOutDEOctets_Object = MibTableColumn
cktOutDEOctets = _CktOutDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 48),
    _CktOutDEOctets_Type()
)
cktOutDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutDEOctets.setStatus("mandatory")
_CktOutODEOctets_Type = Counter32
_CktOutODEOctets_Object = MibTableColumn
cktOutODEOctets = _CktOutODEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 49),
    _CktOutODEOctets_Type()
)
cktOutODEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutODEOctets.setStatus("mandatory")
_CktOutLostFrames_Type = Counter32
_CktOutLostFrames_Object = MibTableColumn
cktOutLostFrames = _CktOutLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 50),
    _CktOutLostFrames_Type()
)
cktOutLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostFrames.setStatus("mandatory")
_CktOutLostDEFrames_Type = Counter32
_CktOutLostDEFrames_Object = MibTableColumn
cktOutLostDEFrames = _CktOutLostDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 51),
    _CktOutLostDEFrames_Type()
)
cktOutLostDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostDEFrames.setStatus("mandatory")
_CktOutLostODEFrames_Type = Counter32
_CktOutLostODEFrames_Object = MibTableColumn
cktOutLostODEFrames = _CktOutLostODEFrames_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 52),
    _CktOutLostODEFrames_Type()
)
cktOutLostODEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostODEFrames.setStatus("mandatory")
_CktOutLostOctets_Type = Counter32
_CktOutLostOctets_Object = MibTableColumn
cktOutLostOctets = _CktOutLostOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 53),
    _CktOutLostOctets_Type()
)
cktOutLostOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostOctets.setStatus("mandatory")
_CktOutLostDEOctets_Type = Counter32
_CktOutLostDEOctets_Object = MibTableColumn
cktOutLostDEOctets = _CktOutLostDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 54),
    _CktOutLostDEOctets_Type()
)
cktOutLostDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostDEOctets.setStatus("mandatory")
_CktOutLostODEOctets_Type = Counter32
_CktOutLostODEOctets_Object = MibTableColumn
cktOutLostODEOctets = _CktOutLostODEOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 55),
    _CktOutLostODEOctets_Type()
)
cktOutLostODEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutLostODEOctets.setStatus("mandatory")
_CktRtMinDelay_Type = Integer32
_CktRtMinDelay_Object = MibTableColumn
cktRtMinDelay = _CktRtMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 56),
    _CktRtMinDelay_Type()
)
cktRtMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtMinDelay.setStatus("mandatory")
_CktRtMaxDelay_Type = Integer32
_CktRtMaxDelay_Object = MibTableColumn
cktRtMaxDelay = _CktRtMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 57),
    _CktRtMaxDelay_Type()
)
cktRtMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtMaxDelay.setStatus("mandatory")
_CktRtAvgDelay_Type = Integer32
_CktRtAvgDelay_Object = MibTableColumn
cktRtAvgDelay = _CktRtAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 58),
    _CktRtAvgDelay_Type()
)
cktRtAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtAvgDelay.setStatus("mandatory")
_CktDiagTestId_Type = Integer32
_CktDiagTestId_Object = MibTableColumn
cktDiagTestId = _CktDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 59),
    _CktDiagTestId_Type()
)
cktDiagTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDiagTestId.setStatus("mandatory")
_CktDiagTestRuns_Type = Integer32
_CktDiagTestRuns_Object = MibTableColumn
cktDiagTestRuns = _CktDiagTestRuns_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 60),
    _CktDiagTestRuns_Type()
)
cktDiagTestRuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDiagTestRuns.setStatus("mandatory")
_CktHelloCounter_Type = Integer32
_CktHelloCounter_Object = MibTableColumn
cktHelloCounter = _CktHelloCounter_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 61),
    _CktHelloCounter_Type()
)
cktHelloCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktHelloCounter.setStatus("mandatory")
_CktHelloAckCounter_Type = Integer32
_CktHelloAckCounter_Object = MibTableColumn
cktHelloAckCounter = _CktHelloAckCounter_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 62),
    _CktHelloAckCounter_Type()
)
cktHelloAckCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktHelloAckCounter.setStatus("mandatory")
_CktDefinedPath_Type = OctetString
_CktDefinedPath_Object = MibTableColumn
cktDefinedPath = _CktDefinedPath_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 63),
    _CktDefinedPath_Type()
)
cktDefinedPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDefinedPath.setStatus("mandatory")
_CktDefinedPathCount_Type = Integer32
_CktDefinedPathCount_Object = MibTableColumn
cktDefinedPathCount = _CktDefinedPathCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 64),
    _CktDefinedPathCount_Type()
)
cktDefinedPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktDefinedPathCount.setStatus("mandatory")
_CktDefinedPathEnable_Type = Integer32
_CktDefinedPathEnable_Object = MibTableColumn
cktDefinedPathEnable = _CktDefinedPathEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 65),
    _CktDefinedPathEnable_Type()
)
cktDefinedPathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDefinedPathEnable.setStatus("mandatory")
_CktDefinedPathAltOption_Type = Integer32
_CktDefinedPathAltOption_Object = MibTableColumn
cktDefinedPathAltOption = _CktDefinedPathAltOption_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 66),
    _CktDefinedPathAltOption_Type()
)
cktDefinedPathAltOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDefinedPathAltOption.setStatus("mandatory")
_CktUsingDefinedPath_Type = Integer32
_CktUsingDefinedPath_Object = MibTableColumn
cktUsingDefinedPath = _CktUsingDefinedPath_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 67),
    _CktUsingDefinedPath_Type()
)
cktUsingDefinedPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktUsingDefinedPath.setStatus("mandatory")
_CktTryAltPath_Type = Integer32
_CktTryAltPath_Object = MibTableColumn
cktTryAltPath = _CktTryAltPath_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 68),
    _CktTryAltPath_Type()
)
cktTryAltPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTryAltPath.setStatus("mandatory")
_CktNotVirgin_Type = Integer32
_CktNotVirgin_Object = MibTableColumn
cktNotVirgin = _CktNotVirgin_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 69),
    _CktNotVirgin_Type()
)
cktNotVirgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktNotVirgin.setStatus("mandatory")
_CktInForward_Type = Integer32
_CktInForward_Object = MibTableColumn
cktInForward = _CktInForward_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 70),
    _CktInForward_Type()
)
cktInForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInForward.setStatus("mandatory")
_CktBtusSeg_Type = Integer32
_CktBtusSeg_Object = MibTableColumn
cktBtusSeg = _CktBtusSeg_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 71),
    _CktBtusSeg_Type()
)
cktBtusSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktBtusSeg.setStatus("mandatory")
_CktInSegmentsDiscards_Type = Counter32
_CktInSegmentsDiscards_Object = MibTableColumn
cktInSegmentsDiscards = _CktInSegmentsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 72),
    _CktInSegmentsDiscards_Type()
)
cktInSegmentsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInSegmentsDiscards.setStatus("mandatory")
_CktAtmVPI_Type = Integer32
_CktAtmVPI_Object = MibTableColumn
cktAtmVPI = _CktAtmVPI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 73),
    _CktAtmVPI_Type()
)
cktAtmVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmVPI.setStatus("mandatory")
_CktAtmVCI_Type = Integer32
_CktAtmVCI_Object = MibTableColumn
cktAtmVCI = _CktAtmVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 74),
    _CktAtmVCI_Type()
)
cktAtmVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmVCI.setStatus("mandatory")


class _CktType_Type(Integer32):
    """Custom type cktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_CktType_Type.__name__ = "Integer32"
_CktType_Object = MibTableColumn
cktType = _CktType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 75),
    _CktType_Type()
)
cktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktType.setStatus("mandatory")
_CktSvcCallingParty_Type = OctetString
_CktSvcCallingParty_Object = MibTableColumn
cktSvcCallingParty = _CktSvcCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 76),
    _CktSvcCallingParty_Type()
)
cktSvcCallingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcCallingParty.setStatus("mandatory")
_CktSvcCalledParty_Type = OctetString
_CktSvcCalledParty_Object = MibTableColumn
cktSvcCalledParty = _CktSvcCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 77),
    _CktSvcCalledParty_Type()
)
cktSvcCalledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcCalledParty.setStatus("mandatory")
_CktSvcDuration_Type = TimeTicks
_CktSvcDuration_Object = MibTableColumn
cktSvcDuration = _CktSvcDuration_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 78),
    _CktSvcDuration_Type()
)
cktSvcDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcDuration.setStatus("mandatory")
_CktSvcCause_Type = Integer32
_CktSvcCause_Object = MibTableColumn
cktSvcCause = _CktSvcCause_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 79),
    _CktSvcCause_Type()
)
cktSvcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcCause.setStatus("mandatory")


class _CktXlatFlag_Type(Integer32):
    """Custom type cktXlatFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rfc1483", 1)
    )


_CktXlatFlag_Type.__name__ = "Integer32"
_CktXlatFlag_Object = MibTableColumn
cktXlatFlag = _CktXlatFlag_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 80),
    _CktXlatFlag_Type()
)
cktXlatFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktXlatFlag.setStatus("mandatory")
_CktDestLaddr_Type = Integer32
_CktDestLaddr_Object = MibTableColumn
cktDestLaddr = _CktDestLaddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 81),
    _CktDestLaddr_Type()
)
cktDestLaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDestLaddr.setStatus("mandatory")
_CktSrcLaddr_Type = Integer32
_CktSrcLaddr_Object = MibTableColumn
cktSrcLaddr = _CktSrcLaddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 82),
    _CktSrcLaddr_Type()
)
cktSrcLaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktSrcLaddr.setStatus("mandatory")


class _CktLoop_Type(Integer32):
    """Custom type cktLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("local", 1),
          ("remote", 2))
    )


_CktLoop_Type.__name__ = "Integer32"
_CktLoop_Object = MibTableColumn
cktLoop = _CktLoop_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 83),
    _CktLoop_Type()
)
cktLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLoop.setStatus("mandatory")


class _CktRerouteBalance_Type(Integer32):
    """Custom type cktRerouteBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_CktRerouteBalance_Type.__name__ = "Integer32"
_CktRerouteBalance_Object = MibTableColumn
cktRerouteBalance = _CktRerouteBalance_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 84),
    _CktRerouteBalance_Type()
)
cktRerouteBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRerouteBalance.setStatus("mandatory")


class _CktCallingBackup_Type(Integer32):
    """Custom type cktCallingBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_CktCallingBackup_Type.__name__ = "Integer32"
_CktCallingBackup_Object = MibTableColumn
cktCallingBackup = _CktCallingBackup_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 85),
    _CktCallingBackup_Type()
)
cktCallingBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktCallingBackup.setStatus("mandatory")
_CktRCir_Type = Integer32
_CktRCir_Object = MibTableColumn
cktRCir = _CktRCir_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 86),
    _CktRCir_Type()
)
cktRCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRCir.setStatus("mandatory")


class _CktAtmQoS_Type(Integer32):
    """Custom type cktAtmQoS based on Integer32"""
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
        *(("cbr", 1),
          ("vbr1", 2),
          ("vbr2", 3),
          ("vbr3", 4))
    )


_CktAtmQoS_Type.__name__ = "Integer32"
_CktAtmQoS_Object = MibTableColumn
cktAtmQoS = _CktAtmQoS_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 87),
    _CktAtmQoS_Type()
)
cktAtmQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmQoS.setStatus("mandatory")
_CktAtmInCells_Type = Counter32
_CktAtmInCells_Object = MibTableColumn
cktAtmInCells = _CktAtmInCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 88),
    _CktAtmInCells_Type()
)
cktAtmInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInCells.setStatus("mandatory")
_CktAtmOutCells_Type = Counter32
_CktAtmOutCells_Object = MibTableColumn
cktAtmOutCells = _CktAtmOutCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 89),
    _CktAtmOutCells_Type()
)
cktAtmOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmOutCells.setStatus("mandatory")
_CktAtmInDiscardedClp0Cells_Type = Counter32
_CktAtmInDiscardedClp0Cells_Object = MibTableColumn
cktAtmInDiscardedClp0Cells = _CktAtmInDiscardedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 90),
    _CktAtmInDiscardedClp0Cells_Type()
)
cktAtmInDiscardedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInDiscardedClp0Cells.setStatus("mandatory")
_CktAtmInDiscardedClp1Cells_Type = Counter32
_CktAtmInDiscardedClp1Cells_Object = MibTableColumn
cktAtmInDiscardedClp1Cells = _CktAtmInDiscardedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 91),
    _CktAtmInDiscardedClp1Cells_Type()
)
cktAtmInDiscardedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInDiscardedClp1Cells.setStatus("mandatory")


class _CktAtmVcType_Type(Integer32):
    """Custom type cktAtmVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_CktAtmVcType_Type.__name__ = "Integer32"
_CktAtmVcType_Object = MibTableColumn
cktAtmVcType = _CktAtmVcType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 92),
    _CktAtmVcType_Type()
)
cktAtmVcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmVcType.setStatus("mandatory")
_CktAtmPCR_Type = Integer32
_CktAtmPCR_Object = MibTableColumn
cktAtmPCR = _CktAtmPCR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 93),
    _CktAtmPCR_Type()
)
cktAtmPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmPCR.setStatus("mandatory")
_CktAtmSCR_Type = Integer32
_CktAtmSCR_Object = MibTableColumn
cktAtmSCR = _CktAtmSCR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 94),
    _CktAtmSCR_Type()
)
cktAtmSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmSCR.setStatus("mandatory")
_CktAtmMBS_Type = Integer32
_CktAtmMBS_Object = MibTableColumn
cktAtmMBS = _CktAtmMBS_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 95),
    _CktAtmMBS_Type()
)
cktAtmMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmMBS.setStatus("mandatory")
_CktAtmInPassedClp0Cells_Type = Counter32
_CktAtmInPassedClp0Cells_Object = MibTableColumn
cktAtmInPassedClp0Cells = _CktAtmInPassedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 96),
    _CktAtmInPassedClp0Cells_Type()
)
cktAtmInPassedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInPassedClp0Cells.setStatus("mandatory")
_CktAtmInPassedClp1Cells_Type = Counter32
_CktAtmInPassedClp1Cells_Object = MibTableColumn
cktAtmInPassedClp1Cells = _CktAtmInPassedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 97),
    _CktAtmInPassedClp1Cells_Type()
)
cktAtmInPassedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInPassedClp1Cells.setStatus("mandatory")
_CktAtmInTaggedCells_Type = Counter32
_CktAtmInTaggedCells_Object = MibTableColumn
cktAtmInTaggedCells = _CktAtmInTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 98),
    _CktAtmInTaggedCells_Type()
)
cktAtmInTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInTaggedCells.setStatus("mandatory")
_CktAtmOutClp0Cells_Type = Counter32
_CktAtmOutClp0Cells_Object = MibTableColumn
cktAtmOutClp0Cells = _CktAtmOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 99),
    _CktAtmOutClp0Cells_Type()
)
cktAtmOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmOutClp0Cells.setStatus("mandatory")
_CktAtmOutClp1Cells_Type = Counter32
_CktAtmOutClp1Cells_Object = MibTableColumn
cktAtmOutClp1Cells = _CktAtmOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 100),
    _CktAtmOutClp1Cells_Type()
)
cktAtmOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmOutClp1Cells.setStatus("mandatory")


class _CktAtmRQoS_Type(Integer32):
    """Custom type cktAtmRQoS based on Integer32"""
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
        *(("cbr", 1),
          ("vbr1", 2),
          ("vbr2", 3),
          ("vbr3", 4))
    )


_CktAtmRQoS_Type.__name__ = "Integer32"
_CktAtmRQoS_Object = MibTableColumn
cktAtmRQoS = _CktAtmRQoS_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 101),
    _CktAtmRQoS_Type()
)
cktAtmRQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmRQoS.setStatus("mandatory")


class _CktAtmTfdType_Type(Integer32):
    """Custom type cktAtmTfdType based on Integer32"""
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
        *(("pcr-0-01", 1),
          ("pcr-0-01-tag", 2),
          ("pcr-01", 5),
          ("pcr-01-bestEffort", 7),
          ("pcr-01-scr-0-mbs-0", 3),
          ("pcr-01-scr-0-mbs-0-tag", 4),
          ("pcr-01-scr-01-mbs-01", 6))
    )


_CktAtmTfdType_Type.__name__ = "Integer32"
_CktAtmTfdType_Object = MibTableColumn
cktAtmTfdType = _CktAtmTfdType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 102),
    _CktAtmTfdType_Type()
)
cktAtmTfdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmTfdType.setStatus("mandatory")


class _CktAtmRTfdType_Type(Integer32):
    """Custom type cktAtmRTfdType based on Integer32"""
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
        *(("pcr-0-01", 1),
          ("pcr-0-01-tag", 2),
          ("pcr-01", 5),
          ("pcr-01-bestEffort", 7),
          ("pcr-01-scr-0-mbs-0", 3),
          ("pcr-01-scr-0-mbs-0-tag", 4),
          ("pcr-01-scr-01-mbs-01", 6))
    )


_CktAtmRTfdType_Type.__name__ = "Integer32"
_CktAtmRTfdType_Object = MibTableColumn
cktAtmRTfdType = _CktAtmRTfdType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 103),
    _CktAtmRTfdType_Type()
)
cktAtmRTfdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmRTfdType.setStatus("mandatory")
_CktAtmTfdParam1_Type = Integer32
_CktAtmTfdParam1_Object = MibTableColumn
cktAtmTfdParam1 = _CktAtmTfdParam1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 104),
    _CktAtmTfdParam1_Type()
)
cktAtmTfdParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmTfdParam1.setStatus("mandatory")
_CktAtmTfdParam2_Type = Integer32
_CktAtmTfdParam2_Object = MibTableColumn
cktAtmTfdParam2 = _CktAtmTfdParam2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 105),
    _CktAtmTfdParam2_Type()
)
cktAtmTfdParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmTfdParam2.setStatus("mandatory")
_CktAtmTfdParam3_Type = Integer32
_CktAtmTfdParam3_Object = MibTableColumn
cktAtmTfdParam3 = _CktAtmTfdParam3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 106),
    _CktAtmTfdParam3_Type()
)
cktAtmTfdParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmTfdParam3.setStatus("mandatory")
_CktAtmRTfdParam1_Type = Integer32
_CktAtmRTfdParam1_Object = MibTableColumn
cktAtmRTfdParam1 = _CktAtmRTfdParam1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 107),
    _CktAtmRTfdParam1_Type()
)
cktAtmRTfdParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmRTfdParam1.setStatus("mandatory")
_CktAtmRTfdParam2_Type = Integer32
_CktAtmRTfdParam2_Object = MibTableColumn
cktAtmRTfdParam2 = _CktAtmRTfdParam2_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 108),
    _CktAtmRTfdParam2_Type()
)
cktAtmRTfdParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmRTfdParam2.setStatus("mandatory")
_CktAtmRTfdParam3_Type = Integer32
_CktAtmRTfdParam3_Object = MibTableColumn
cktAtmRTfdParam3 = _CktAtmRTfdParam3_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 109),
    _CktAtmRTfdParam3_Type()
)
cktAtmRTfdParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmRTfdParam3.setStatus("mandatory")


class _CktAtmFrameIWF_Type(Integer32):
    """Custom type cktAtmFrameIWF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("iwf", 2))
    )


_CktAtmFrameIWF_Type.__name__ = "Integer32"
_CktAtmFrameIWF_Object = MibTableColumn
cktAtmFrameIWF = _CktAtmFrameIWF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 110),
    _CktAtmFrameIWF_Type()
)
cktAtmFrameIWF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmFrameIWF.setStatus("mandatory")


class _CktAtmUserPlane_Type(Integer32):
    """Custom type cktAtmUserPlane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-multipoint", 2),
          ("point-to-point", 1))
    )


_CktAtmUserPlane_Type.__name__ = "Integer32"
_CktAtmUserPlane_Object = MibTableColumn
cktAtmUserPlane = _CktAtmUserPlane_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 111),
    _CktAtmUserPlane_Type()
)
cktAtmUserPlane.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmUserPlane.setStatus("mandatory")
_CktRBc_Type = Integer32
_CktRBc_Object = MibTableColumn
cktRBc = _CktRBc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 112),
    _CktRBc_Type()
)
cktRBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRBc.setStatus("mandatory")
_CktRBe_Type = Integer32
_CktRBe_Object = MibTableColumn
cktRBe = _CktRBe_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 113),
    _CktRBe_Type()
)
cktRBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRBe.setStatus("mandatory")


class _CktOamLoopbackDirection_Type(Integer32):
    """Custom type cktOamLoopbackDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CktOamLoopbackDirection_Type.__name__ = "Integer32"
_CktOamLoopbackDirection_Object = MibTableColumn
cktOamLoopbackDirection = _CktOamLoopbackDirection_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 114),
    _CktOamLoopbackDirection_Type()
)
cktOamLoopbackDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOamLoopbackDirection.setStatus("mandatory")


class _CktOamLoopbackType_Type(Integer32):
    """Custom type cktOamLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 2),
          ("segment", 1))
    )


_CktOamLoopbackType_Type.__name__ = "Integer32"
_CktOamLoopbackType_Object = MibTableColumn
cktOamLoopbackType = _CktOamLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 115),
    _CktOamLoopbackType_Type()
)
cktOamLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOamLoopbackType.setStatus("mandatory")
_CktOamLoopbackHops_Type = Integer32
_CktOamLoopbackHops_Object = MibTableColumn
cktOamLoopbackHops = _CktOamLoopbackHops_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 116),
    _CktOamLoopbackHops_Type()
)
cktOamLoopbackHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOamLoopbackHops.setStatus("mandatory")
_CktOamLoopbackCount_Type = Integer32
_CktOamLoopbackCount_Object = MibTableColumn
cktOamLoopbackCount = _CktOamLoopbackCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 117),
    _CktOamLoopbackCount_Type()
)
cktOamLoopbackCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOamLoopbackCount.setStatus("mandatory")
_CktOamLoopbackReceived_Type = Counter32
_CktOamLoopbackReceived_Object = MibTableColumn
cktOamLoopbackReceived = _CktOamLoopbackReceived_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 118),
    _CktOamLoopbackReceived_Type()
)
cktOamLoopbackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOamLoopbackReceived.setStatus("mandatory")
_CktOamLoopbackTimeouts_Type = Counter32
_CktOamLoopbackTimeouts_Object = MibTableColumn
cktOamLoopbackTimeouts = _CktOamLoopbackTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 119),
    _CktOamLoopbackTimeouts_Type()
)
cktOamLoopbackTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOamLoopbackTimeouts.setStatus("mandatory")
_CktOamLoopbackReceivedHigh_Type = Integer32
_CktOamLoopbackReceivedHigh_Object = MibTableColumn
cktOamLoopbackReceivedHigh = _CktOamLoopbackReceivedHigh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 120),
    _CktOamLoopbackReceivedHigh_Type()
)
cktOamLoopbackReceivedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOamLoopbackReceivedHigh.setStatus("mandatory")
_CktOamLoopbackReceivedLow_Type = Integer32
_CktOamLoopbackReceivedLow_Object = MibTableColumn
cktOamLoopbackReceivedLow = _CktOamLoopbackReceivedLow_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 121),
    _CktOamLoopbackReceivedLow_Type()
)
cktOamLoopbackReceivedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOamLoopbackReceivedLow.setStatus("mandatory")
_CktOamLoopbackReceivedAvg_Type = Integer32
_CktOamLoopbackReceivedAvg_Object = MibTableColumn
cktOamLoopbackReceivedAvg = _CktOamLoopbackReceivedAvg_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 122),
    _CktOamLoopbackReceivedAvg_Type()
)
cktOamLoopbackReceivedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOamLoopbackReceivedAvg.setStatus("mandatory")


class _CktOamAlarmDisable_Type(Integer32):
    """Custom type cktOamAlarmDisable based on Integer32"""
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


_CktOamAlarmDisable_Type.__name__ = "Integer32"
_CktOamAlarmDisable_Object = MibTableColumn
cktOamAlarmDisable = _CktOamAlarmDisable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 123),
    _CktOamAlarmDisable_Type()
)
cktOamAlarmDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOamAlarmDisable.setStatus("mandatory")
_CktShaperId_Type = Integer32
_CktShaperId_Object = MibTableColumn
cktShaperId = _CktShaperId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 124),
    _CktShaperId_Type()
)
cktShaperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktShaperId.setStatus("mandatory")


class _CktOspfCtd_Type(Integer32):
    """Custom type cktOspfCtd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CktOspfCtd_Type.__name__ = "Integer32"
_CktOspfCtd_Object = MibTableColumn
cktOspfCtd = _CktOspfCtd_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 125),
    _CktOspfCtd_Type()
)
cktOspfCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOspfCtd.setStatus("mandatory")


class _CktOspfCdv_Type(Integer32):
    """Custom type cktOspfCdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CktOspfCdv_Type.__name__ = "Integer32"
_CktOspfCdv_Object = MibTableColumn
cktOspfCdv = _CktOspfCdv_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 126),
    _CktOspfCdv_Type()
)
cktOspfCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktOspfCdv.setStatus("mandatory")
_CktOutPort_Type = Integer32
_CktOutPort_Object = MibTableColumn
cktOutPort = _CktOutPort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 127),
    _CktOutPort_Type()
)
cktOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutPort.setStatus("mandatory")
_CktOutVc_Type = Integer32
_CktOutVc_Object = MibTableColumn
cktOutVc = _CktOutVc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 128),
    _CktOutVc_Type()
)
cktOutVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutVc.setStatus("mandatory")
_CktRVc_Type = Integer32
_CktRVc_Object = MibTableColumn
cktRVc = _CktRVc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 129),
    _CktRVc_Type()
)
cktRVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRVc.setStatus("mandatory")


class _CktEntryType_Type(Integer32):
    """Custom type cktEntryType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("as-trunk", 2),
          ("atm-leaf", 11),
          ("atm-user", 10),
          ("control", 9),
          ("fr-user", 1),
          ("lmi", 4),
          ("mgmt", 6),
          ("multicast", 5),
          ("on-trunk", 3),
          ("smds", 7),
          ("split-multicast", 8))
    )


_CktEntryType_Type.__name__ = "Integer32"
_CktEntryType_Object = MibTableColumn
cktEntryType = _CktEntryType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 130),
    _CktEntryType_Type()
)
cktEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktEntryType.setStatus("mandatory")
_CktDiagStr_Type = OctetString
_CktDiagStr_Object = MibTableColumn
cktDiagStr = _CktDiagStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 131),
    _CktDiagStr_Type()
)
cktDiagStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktDiagStr.setStatus("mandatory")


class _CktSvcAalType_Type(Integer32):
    """Custom type cktSvcAalType based on Integer32"""
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
        *(("aal1", 1),
          ("aal3-4", 3),
          ("aal5", 5),
          ("unspecified", 2),
          ("user-defined", 4))
    )


_CktSvcAalType_Type.__name__ = "Integer32"
_CktSvcAalType_Object = MibTableColumn
cktSvcAalType = _CktSvcAalType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 132),
    _CktSvcAalType_Type()
)
cktSvcAalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcAalType.setStatus("mandatory")


class _CktSvcBBearerClass_Type(Integer32):
    """Custom type cktSvcBBearerClass based on Integer32"""
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
        *(("class-A", 2),
          ("class-C", 3),
          ("class-VP", 5),
          ("class-X", 4),
          ("unspecified", 1))
    )


_CktSvcBBearerClass_Type.__name__ = "Integer32"
_CktSvcBBearerClass_Object = MibTableColumn
cktSvcBBearerClass = _CktSvcBBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 133),
    _CktSvcBBearerClass_Type()
)
cktSvcBBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcBBearerClass.setStatus("mandatory")


class _CktSvcBBearerClippingSusc_Type(Integer32):
    """Custom type cktSvcBBearerClippingSusc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-susceptible", 2),
          ("susceptible", 3),
          ("unspecified", 1))
    )


_CktSvcBBearerClippingSusc_Type.__name__ = "Integer32"
_CktSvcBBearerClippingSusc_Object = MibTableColumn
cktSvcBBearerClippingSusc = _CktSvcBBearerClippingSusc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 134),
    _CktSvcBBearerClippingSusc_Type()
)
cktSvcBBearerClippingSusc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcBBearerClippingSusc.setStatus("mandatory")


class _CktSvcBBearerTmgReq_Type(Integer32):
    """Custom type cktSvcBBearerTmgReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 2),
          ("not-end-to-end", 3),
          ("not-indicated", 1))
    )


_CktSvcBBearerTmgReq_Type.__name__ = "Integer32"
_CktSvcBBearerTmgReq_Object = MibTableColumn
cktSvcBBearerTmgReq = _CktSvcBBearerTmgReq_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 135),
    _CktSvcBBearerTmgReq_Type()
)
cktSvcBBearerTmgReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcBBearerTmgReq.setStatus("mandatory")


class _CktSvcBBearerTfcType_Type(Integer32):
    """Custom type cktSvcBBearerTfcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("not-indicated", 1),
          ("vbr", 3))
    )


_CktSvcBBearerTfcType_Type.__name__ = "Integer32"
_CktSvcBBearerTfcType_Object = MibTableColumn
cktSvcBBearerTfcType = _CktSvcBBearerTfcType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 136),
    _CktSvcBBearerTfcType_Type()
)
cktSvcBBearerTfcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSvcBBearerTfcType.setStatus("mandatory")


class _CktAtmUPCEnable_Type(Integer32):
    """Custom type cktAtmUPCEnable based on Integer32"""
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


_CktAtmUPCEnable_Type.__name__ = "Integer32"
_CktAtmUPCEnable_Object = MibTableColumn
cktAtmUPCEnable = _CktAtmUPCEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 137),
    _CktAtmUPCEnable_Type()
)
cktAtmUPCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmUPCEnable.setStatus("mandatory")
_CktRPriority_Type = Integer32
_CktRPriority_Object = MibTableColumn
cktRPriority = _CktRPriority_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 138),
    _CktRPriority_Type()
)
cktRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRPriority.setStatus("mandatory")
_CktRtPriority_Type = Integer32
_CktRtPriority_Object = MibTableColumn
cktRtPriority = _CktRtPriority_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 139),
    _CktRtPriority_Type()
)
cktRtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRtPriority.setStatus("mandatory")
_CktDeltaBc_Type = Integer32
_CktDeltaBc_Object = MibTableColumn
cktDeltaBc = _CktDeltaBc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 140),
    _CktDeltaBc_Type()
)
cktDeltaBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDeltaBc.setStatus("mandatory")
_CktDeltaBe_Type = Integer32
_CktDeltaBe_Object = MibTableColumn
cktDeltaBe = _CktDeltaBe_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 141),
    _CktDeltaBe_Type()
)
cktDeltaBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDeltaBe.setStatus("mandatory")
_CktDeltaRBc_Type = Integer32
_CktDeltaRBc_Object = MibTableColumn
cktDeltaRBc = _CktDeltaRBc_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 142),
    _CktDeltaRBc_Type()
)
cktDeltaRBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDeltaRBc.setStatus("mandatory")
_CktDeltaRBe_Type = Integer32
_CktDeltaRBe_Object = MibTableColumn
cktDeltaRBe = _CktDeltaRBe_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 143),
    _CktDeltaRBe_Type()
)
cktDeltaRBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDeltaRBe.setStatus("mandatory")
_CktRedFrPcnt_Type = Integer32
_CktRedFrPcnt_Object = MibTableColumn
cktRedFrPcnt = _CktRedFrPcnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 144),
    _CktRedFrPcnt_Type()
)
cktRedFrPcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRedFrPcnt.setStatus("mandatory")
_CktRedFrRPcnt_Type = Integer32
_CktRedFrRPcnt_Object = MibTableColumn
cktRedFrRPcnt = _CktRedFrRPcnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 145),
    _CktRedFrRPcnt_Type()
)
cktRedFrRPcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRedFrRPcnt.setStatus("mandatory")


class _CktRateEnforceSchm_Type(Integer32):
    """Custom type cktRateEnforceSchm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jump", 1),
          ("simple", 2))
    )


_CktRateEnforceSchm_Type.__name__ = "Integer32"
_CktRateEnforceSchm_Object = MibTableColumn
cktRateEnforceSchm = _CktRateEnforceSchm_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 146),
    _CktRateEnforceSchm_Type()
)
cktRateEnforceSchm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRateEnforceSchm.setStatus("mandatory")


class _CktRateEnforceRSchm_Type(Integer32):
    """Custom type cktRateEnforceRSchm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jump", 1),
          ("simple", 2))
    )


_CktRateEnforceRSchm_Type.__name__ = "Integer32"
_CktRateEnforceRSchm_Object = MibTableColumn
cktRateEnforceRSchm = _CktRateEnforceRSchm_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 147),
    _CktRateEnforceRSchm_Type()
)
cktRateEnforceRSchm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRateEnforceRSchm.setStatus("mandatory")


class _CktROde_Type(Integer32):
    """Custom type cktROde based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_CktROde_Type.__name__ = "Integer32"
_CktROde_Object = MibTableColumn
cktROde = _CktROde_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 148),
    _CktROde_Type()
)
cktROde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktROde.setStatus("mandatory")
_CktPrivateNet_Type = Integer32
_CktPrivateNet_Object = MibTableColumn
cktPrivateNet = _CktPrivateNet_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 149),
    _CktPrivateNet_Type()
)
cktPrivateNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktPrivateNet.setStatus("mandatory")


class _CktPrivateNetOverflow_Type(Integer32):
    """Custom type cktPrivateNetOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("use-public", 1)
    )


_CktPrivateNetOverflow_Type.__name__ = "Integer32"
_CktPrivateNetOverflow_Object = MibTableColumn
cktPrivateNetOverflow = _CktPrivateNetOverflow_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 150),
    _CktPrivateNetOverflow_Type()
)
cktPrivateNetOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktPrivateNetOverflow.setStatus("mandatory")
_CktCustomerID_Type = Integer32
_CktCustomerID_Object = MibTableColumn
cktCustomerID = _CktCustomerID_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 151),
    _CktCustomerID_Type()
)
cktCustomerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktCustomerID.setStatus("mandatory")
_CktAtmCDVT_Type = Integer32
_CktAtmCDVT_Object = MibTableColumn
cktAtmCDVT = _CktAtmCDVT_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 152),
    _CktAtmCDVT_Type()
)
cktAtmCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmCDVT.setStatus("mandatory")


class _CktNdcEnable_Type(Integer32):
    """Custom type cktNdcEnable based on Integer32"""
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


_CktNdcEnable_Type.__name__ = "Integer32"
_CktNdcEnable_Object = MibTableColumn
cktNdcEnable = _CktNdcEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 153),
    _CktNdcEnable_Type()
)
cktNdcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktNdcEnable.setStatus("mandatory")


class _CktInterworkingFrToAtmCLP_Type(Integer32):
    """Custom type cktInterworkingFrToAtmCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clp1", 1),
          ("fr-de", 2))
    )


_CktInterworkingFrToAtmCLP_Type.__name__ = "Integer32"
_CktInterworkingFrToAtmCLP_Object = MibTableColumn
cktInterworkingFrToAtmCLP = _CktInterworkingFrToAtmCLP_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 154),
    _CktInterworkingFrToAtmCLP_Type()
)
cktInterworkingFrToAtmCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktInterworkingFrToAtmCLP.setStatus("mandatory")


class _CktInterworkingFrToAtmDe_Type(Integer32):
    """Custom type cktInterworkingFrToAtmDe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm-clp", 2),
          ("de1", 1))
    )


_CktInterworkingFrToAtmDe_Type.__name__ = "Integer32"
_CktInterworkingFrToAtmDe_Object = MibTableColumn
cktInterworkingFrToAtmDe = _CktInterworkingFrToAtmDe_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 155),
    _CktInterworkingFrToAtmDe_Type()
)
cktInterworkingFrToAtmDe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktInterworkingFrToAtmDe.setStatus("mandatory")


class _CktNrtsCLP1_Type(Integer32):
    """Custom type cktNrtsCLP1 based on Integer32"""
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


_CktNrtsCLP1_Type.__name__ = "Integer32"
_CktNrtsCLP1_Object = MibTableColumn
cktNrtsCLP1 = _CktNrtsCLP1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 156),
    _CktNrtsCLP1_Type()
)
cktNrtsCLP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktNrtsCLP1.setStatus("mandatory")
_CktNrtsDiscardClp0_Type = Counter32
_CktNrtsDiscardClp0_Object = MibTableColumn
cktNrtsDiscardClp0 = _CktNrtsDiscardClp0_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 157),
    _CktNrtsDiscardClp0_Type()
)
cktNrtsDiscardClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktNrtsDiscardClp0.setStatus("mandatory")
_CktNrtsDiscardClp1_Type = Counter32
_CktNrtsDiscardClp1_Object = MibTableColumn
cktNrtsDiscardClp1 = _CktNrtsDiscardClp1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 158),
    _CktNrtsDiscardClp1_Type()
)
cktNrtsDiscardClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktNrtsDiscardClp1.setStatus("mandatory")


class _CktMPEnableAMF_Type(Integer32):
    """Custom type cktMPEnableAMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableAMF", 1),
          ("enableAMF", 2))
    )


_CktMPEnableAMF_Type.__name__ = "Integer32"
_CktMPEnableAMF_Object = MibTableColumn
cktMPEnableAMF = _CktMPEnableAMF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 159),
    _CktMPEnableAMF_Type()
)
cktMPEnableAMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMPEnableAMF.setStatus("mandatory")


class _CktMPEligible_Type(Integer32):
    """Custom type cktMPEligible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isMPEligible", 1),
          ("isNotMPEligible", 2))
    )


_CktMPEligible_Type.__name__ = "Integer32"
_CktMPEligible_Object = MibTableColumn
cktMPEligible = _CktMPEligible_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 160),
    _CktMPEligible_Type()
)
cktMPEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMPEligible.setStatus("mandatory")


class _CktMPForcedCaller_Type(Integer32):
    """Custom type cktMPForcedCaller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isMPForcedCaller", 1),
          ("isNotMPForcedCaller", 2))
    )


_CktMPForcedCaller_Type.__name__ = "Integer32"
_CktMPForcedCaller_Object = MibTableColumn
cktMPForcedCaller = _CktMPForcedCaller_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 161),
    _CktMPForcedCaller_Type()
)
cktMPForcedCaller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMPForcedCaller.setStatus("mandatory")


class _CktMPForcedCallee_Type(Integer32):
    """Custom type cktMPForcedCallee based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isMPForcedCallee", 1),
          ("isNotMPForcedCallee", 2))
    )


_CktMPForcedCallee_Type.__name__ = "Integer32"
_CktMPForcedCallee_Object = MibTableColumn
cktMPForcedCallee = _CktMPForcedCallee_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 162),
    _CktMPForcedCallee_Type()
)
cktMPForcedCallee.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktMPForcedCallee.setStatus("mandatory")
_CktFrameSize_Type = Integer32
_CktFrameSize_Object = MibTableColumn
cktFrameSize = _CktFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 163),
    _CktFrameSize_Type()
)
cktFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktFrameSize.setStatus("mandatory")
_CktRFrameSize_Type = Integer32
_CktRFrameSize_Object = MibTableColumn
cktRFrameSize = _CktRFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 164),
    _CktRFrameSize_Type()
)
cktRFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRFrameSize.setStatus("mandatory")


class _CktRNrtsCLP1_Type(Integer32):
    """Custom type cktRNrtsCLP1 based on Integer32"""
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


_CktRNrtsCLP1_Type.__name__ = "Integer32"
_CktRNrtsCLP1_Object = MibTableColumn
cktRNrtsCLP1 = _CktRNrtsCLP1_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 165),
    _CktRNrtsCLP1_Type()
)
cktRNrtsCLP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRNrtsCLP1.setStatus("mandatory")


class _CktBBearerAtmTransferCapability_Type(Integer32):
    """Custom type cktBBearerAtmTransferCapability based on Integer32"""
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
        *(("abr", 8),
          ("cbr", 2),
          ("cbr-with-clr-01", 3),
          ("none", 1),
          ("vbr-nrt", 6),
          ("vbr-nrt-with-clr-01", 7),
          ("vbr-rt", 4),
          ("vbr-rt-with-clr-01", 5))
    )


_CktBBearerAtmTransferCapability_Type.__name__ = "Integer32"
_CktBBearerAtmTransferCapability_Object = MibTableColumn
cktBBearerAtmTransferCapability = _CktBBearerAtmTransferCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 166),
    _CktBBearerAtmTransferCapability_Type()
)
cktBBearerAtmTransferCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktBBearerAtmTransferCapability.setStatus("mandatory")


class _CktAtmFrameDiscard_Type(Integer32):
    """Custom type cktAtmFrameDiscard based on Integer32"""
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


_CktAtmFrameDiscard_Type.__name__ = "Integer32"
_CktAtmFrameDiscard_Object = MibTableColumn
cktAtmFrameDiscard = _CktAtmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 167),
    _CktAtmFrameDiscard_Type()
)
cktAtmFrameDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAtmFrameDiscard.setStatus("mandatory")


class _CktRAtmFrameDiscard_Type(Integer32):
    """Custom type cktRAtmFrameDiscard based on Integer32"""
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


_CktRAtmFrameDiscard_Type.__name__ = "Integer32"
_CktRAtmFrameDiscard_Object = MibTableColumn
cktRAtmFrameDiscard = _CktRAtmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 168),
    _CktRAtmFrameDiscard_Type()
)
cktRAtmFrameDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRAtmFrameDiscard.setStatus("mandatory")
_CktAbrFRMRTT_Type = Integer32
_CktAbrFRMRTT_Object = MibTableColumn
cktAbrFRMRTT = _CktAbrFRMRTT_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 169),
    _CktAbrFRMRTT_Type()
)
cktAbrFRMRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrFRMRTT.setStatus("mandatory")
_CktAbrICR_Type = Integer32
_CktAbrICR_Object = MibTableColumn
cktAbrICR = _CktAbrICR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 170),
    _CktAbrICR_Type()
)
cktAbrICR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrICR.setStatus("mandatory")
_CktRAbrICR_Type = Integer32
_CktRAbrICR_Object = MibTableColumn
cktRAbrICR = _CktRAbrICR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 171),
    _CktRAbrICR_Type()
)
cktRAbrICR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrICR.setStatus("mandatory")
_CktAbrRIF_Type = Integer32
_CktAbrRIF_Object = MibTableColumn
cktAbrRIF = _CktAbrRIF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 172),
    _CktAbrRIF_Type()
)
cktAbrRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrRIF.setStatus("mandatory")
_CktRAbrRIF_Type = Integer32
_CktRAbrRIF_Object = MibTableColumn
cktRAbrRIF = _CktRAbrRIF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 173),
    _CktRAbrRIF_Type()
)
cktRAbrRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrRIF.setStatus("mandatory")
_CktAbrRDF_Type = Integer32
_CktAbrRDF_Object = MibTableColumn
cktAbrRDF = _CktAbrRDF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 174),
    _CktAbrRDF_Type()
)
cktAbrRDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrRDF.setStatus("mandatory")
_CktRAbrRDF_Type = Integer32
_CktRAbrRDF_Object = MibTableColumn
cktRAbrRDF = _CktRAbrRDF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 175),
    _CktRAbrRDF_Type()
)
cktRAbrRDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrRDF.setStatus("mandatory")
_CktAbrTBE_Type = Integer32
_CktAbrTBE_Object = MibTableColumn
cktAbrTBE = _CktAbrTBE_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 176),
    _CktAbrTBE_Type()
)
cktAbrTBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrTBE.setStatus("mandatory")
_CktRAbrTBE_Type = Integer32
_CktRAbrTBE_Object = MibTableColumn
cktRAbrTBE = _CktRAbrTBE_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 177),
    _CktRAbrTBE_Type()
)
cktRAbrTBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrTBE.setStatus("mandatory")
_CktAbrNRM_Type = Integer32
_CktAbrNRM_Object = MibTableColumn
cktAbrNRM = _CktAbrNRM_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 178),
    _CktAbrNRM_Type()
)
cktAbrNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrNRM.setStatus("mandatory")
_CktRAbrNRM_Type = Integer32
_CktRAbrNRM_Object = MibTableColumn
cktRAbrNRM = _CktRAbrNRM_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 179),
    _CktRAbrNRM_Type()
)
cktRAbrNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrNRM.setStatus("mandatory")
_CktAbrTRM_Type = Integer32
_CktAbrTRM_Object = MibTableColumn
cktAbrTRM = _CktAbrTRM_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 180),
    _CktAbrTRM_Type()
)
cktAbrTRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrTRM.setStatus("mandatory")
_CktRAbrTRM_Type = Integer32
_CktRAbrTRM_Object = MibTableColumn
cktRAbrTRM = _CktRAbrTRM_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 181),
    _CktRAbrTRM_Type()
)
cktRAbrTRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrTRM.setStatus("mandatory")
_CktAbrCDF_Type = Integer32
_CktAbrCDF_Object = MibTableColumn
cktAbrCDF = _CktAbrCDF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 182),
    _CktAbrCDF_Type()
)
cktAbrCDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrCDF.setStatus("mandatory")
_CktRAbrCDF_Type = Integer32
_CktRAbrCDF_Object = MibTableColumn
cktRAbrCDF = _CktRAbrCDF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 183),
    _CktRAbrCDF_Type()
)
cktRAbrCDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrCDF.setStatus("mandatory")
_CktAbrADTF_Type = Integer32
_CktAbrADTF_Object = MibTableColumn
cktAbrADTF = _CktAbrADTF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 184),
    _CktAbrADTF_Type()
)
cktAbrADTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAbrADTF.setStatus("mandatory")
_CktRAbrADTF_Type = Integer32
_CktRAbrADTF_Object = MibTableColumn
cktRAbrADTF = _CktRAbrADTF_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 185),
    _CktRAbrADTF_Type()
)
cktRAbrADTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRAbrADTF.setStatus("mandatory")
_CktAccumCTD_Type = Integer32
_CktAccumCTD_Object = MibTableColumn
cktAccumCTD = _CktAccumCTD_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 186),
    _CktAccumCTD_Type()
)
cktAccumCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAccumCTD.setStatus("mandatory")
_CktAccumCDV_Type = Integer32
_CktAccumCDV_Object = MibTableColumn
cktAccumCDV = _CktAccumCDV_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 187),
    _CktAccumCDV_Type()
)
cktAccumCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAccumCDV.setStatus("mandatory")
_CktAccumRCDV_Type = Integer32
_CktAccumRCDV_Object = MibTableColumn
cktAccumRCDV = _CktAccumRCDV_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 188),
    _CktAccumRCDV_Type()
)
cktAccumRCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAccumRCDV.setStatus("mandatory")
_CktCLR_Type = Integer32
_CktCLR_Object = MibTableColumn
cktCLR = _CktCLR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 189),
    _CktCLR_Type()
)
cktCLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktCLR.setStatus("mandatory")
_CktRCLR_Type = Integer32
_CktRCLR_Object = MibTableColumn
cktRCLR = _CktRCLR_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 190),
    _CktRCLR_Type()
)
cktRCLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktRCLR.setStatus("mandatory")
_CktAtmLijId_Type = Integer32
_CktAtmLijId_Object = MibTableColumn
cktAtmLijId = _CktAtmLijId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 191),
    _CktAtmLijId_Type()
)
cktAtmLijId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmLijId.setStatus("mandatory")


class _CktAtmLijType_Type(Integer32):
    """Custom type cktAtmLijType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network-lij", 3),
          ("not-lij", 1),
          ("root-lij", 2))
    )


_CktAtmLijType_Type.__name__ = "Integer32"
_CktAtmLijType_Object = MibTableColumn
cktAtmLijType = _CktAtmLijType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 192),
    _CktAtmLijType_Type()
)
cktAtmLijType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmLijType.setStatus("mandatory")
_CktRtLastDelay_Type = Integer32
_CktRtLastDelay_Object = MibTableColumn
cktRtLastDelay = _CktRtLastDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 193),
    _CktRtLastDelay_Type()
)
cktRtLastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtLastDelay.setStatus("mandatory")
_CktRtAccuMinDelay_Type = Integer32
_CktRtAccuMinDelay_Object = MibTableColumn
cktRtAccuMinDelay = _CktRtAccuMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 194),
    _CktRtAccuMinDelay_Type()
)
cktRtAccuMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtAccuMinDelay.setStatus("mandatory")
_CktRtAccuMaxDelay_Type = Integer32
_CktRtAccuMaxDelay_Object = MibTableColumn
cktRtAccuMaxDelay = _CktRtAccuMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 195),
    _CktRtAccuMaxDelay_Type()
)
cktRtAccuMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtAccuMaxDelay.setStatus("mandatory")
_CktRtAccuAvgDelay_Type = Integer32
_CktRtAccuAvgDelay_Object = MibTableColumn
cktRtAccuAvgDelay = _CktRtAccuAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 196),
    _CktRtAccuAvgDelay_Type()
)
cktRtAccuAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRtAccuAvgDelay.setStatus("mandatory")
_CktQosIntPeriod_Type = Integer32
_CktQosIntPeriod_Object = MibTableColumn
cktQosIntPeriod = _CktQosIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 197),
    _CktQosIntPeriod_Type()
)
cktQosIntPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktQosIntPeriod.setStatus("mandatory")
_CktAtmOutOAMClp0Cells_Type = Counter32
_CktAtmOutOAMClp0Cells_Object = MibTableColumn
cktAtmOutOAMClp0Cells = _CktAtmOutOAMClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 198),
    _CktAtmOutOAMClp0Cells_Type()
)
cktAtmOutOAMClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmOutOAMClp0Cells.setStatus("mandatory")
_CktAtmOutOAMClp1Cells_Type = Counter32
_CktAtmOutOAMClp1Cells_Object = MibTableColumn
cktAtmOutOAMClp1Cells = _CktAtmOutOAMClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 199),
    _CktAtmOutOAMClp1Cells_Type()
)
cktAtmOutOAMClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmOutOAMClp1Cells.setStatus("mandatory")
_CktReqCTD_Type = Integer32
_CktReqCTD_Object = MibTableColumn
cktReqCTD = _CktReqCTD_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 200),
    _CktReqCTD_Type()
)
cktReqCTD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktReqCTD.setStatus("mandatory")
_CktInOctetsPeak_Type = Counter32
_CktInOctetsPeak_Object = MibTableColumn
cktInOctetsPeak = _CktInOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 201),
    _CktInOctetsPeak_Type()
)
cktInOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInOctetsPeak.setStatus("mandatory")
_CktOutOctetsPeak_Type = Counter32
_CktOutOctetsPeak_Object = MibTableColumn
cktOutOctetsPeak = _CktOutOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 202),
    _CktOutOctetsPeak_Type()
)
cktOutOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutOctetsPeak.setStatus("mandatory")
_CktInDEOctetsPeak_Type = Counter32
_CktInDEOctetsPeak_Object = MibTableColumn
cktInDEOctetsPeak = _CktInDEOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 203),
    _CktInDEOctetsPeak_Type()
)
cktInDEOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInDEOctetsPeak.setStatus("mandatory")
_CktOutDEOctetsPeak_Type = Counter32
_CktOutDEOctetsPeak_Object = MibTableColumn
cktOutDEOctetsPeak = _CktOutDEOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 204),
    _CktOutDEOctetsPeak_Type()
)
cktOutDEOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutDEOctetsPeak.setStatus("mandatory")
_CktInODEOctetsPeak_Type = Counter32
_CktInODEOctetsPeak_Object = MibTableColumn
cktInODEOctetsPeak = _CktInODEOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 205),
    _CktInODEOctetsPeak_Type()
)
cktInODEOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktInODEOctetsPeak.setStatus("mandatory")
_CktOutODEOctetsPeak_Type = Counter32
_CktOutODEOctetsPeak_Object = MibTableColumn
cktOutODEOctetsPeak = _CktOutODEOctetsPeak_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 206),
    _CktOutODEOctetsPeak_Type()
)
cktOutODEOctetsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOutODEOctetsPeak.setStatus("mandatory")
_CktAdminCostThreshold_Type = Integer32
_CktAdminCostThreshold_Object = MibTableColumn
cktAdminCostThreshold = _CktAdminCostThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 207),
    _CktAdminCostThreshold_Type()
)
cktAdminCostThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktAdminCostThreshold.setStatus("mandatory")


class _CktAtmSvcServiceCategory_Type(Integer32):
    """Custom type cktAtmSvcServiceCategory based on Integer32"""
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
        *(("cbr", 1),
          ("ubr-abr", 4),
          ("unspecified", 5),
          ("vbr1", 2),
          ("vbr2", 3))
    )


_CktAtmSvcServiceCategory_Type.__name__ = "Integer32"
_CktAtmSvcServiceCategory_Object = MibTableColumn
cktAtmSvcServiceCategory = _CktAtmSvcServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 208),
    _CktAtmSvcServiceCategory_Type()
)
cktAtmSvcServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmSvcServiceCategory.setStatus("mandatory")


class _CktAtmSvcRServiceCategory_Type(Integer32):
    """Custom type cktAtmSvcRServiceCategory based on Integer32"""
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
        *(("cbr", 1),
          ("ubr-abr", 4),
          ("unspecified", 5),
          ("vbr1", 2),
          ("vbr2", 3))
    )


_CktAtmSvcRServiceCategory_Type.__name__ = "Integer32"
_CktAtmSvcRServiceCategory_Object = MibTableColumn
cktAtmSvcRServiceCategory = _CktAtmSvcRServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 209),
    _CktAtmSvcRServiceCategory_Type()
)
cktAtmSvcRServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmSvcRServiceCategory.setStatus("mandatory")


class _CktInterworkingFrToAtmEFCI_Type(Integer32):
    """Custom type cktInterworkingFrToAtmEFCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("efci0", 2),
          ("fr-fecn", 1))
    )


_CktInterworkingFrToAtmEFCI_Type.__name__ = "Integer32"
_CktInterworkingFrToAtmEFCI_Object = MibTableColumn
cktInterworkingFrToAtmEFCI = _CktInterworkingFrToAtmEFCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 210),
    _CktInterworkingFrToAtmEFCI_Type()
)
cktInterworkingFrToAtmEFCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktInterworkingFrToAtmEFCI.setStatus("mandatory")


class _CktDiagSARMon_Type(Integer32):
    """Custom type cktDiagSARMon based on Integer32"""
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
        *(("flowOffInbound", 2),
          ("flowOffInboundOutbound", 6),
          ("flowOffOutbound", 4),
          ("flowOnInbound", 1),
          ("flowOnInboundOutbound", 5),
          ("flowOnOutbound", 3))
    )


_CktDiagSARMon_Type.__name__ = "Integer32"
_CktDiagSARMon_Object = MibTableColumn
cktDiagSARMon = _CktDiagSARMon_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 211),
    _CktDiagSARMon_Type()
)
cktDiagSARMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktDiagSARMon.setStatus("mandatory")
_CktAdminCostReal_Type = Integer32
_CktAdminCostReal_Object = MibTableColumn
cktAdminCostReal = _CktAdminCostReal_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 212),
    _CktAdminCostReal_Type()
)
cktAdminCostReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAdminCostReal.setStatus("mandatory")
_CktAtmInClp0Cells_Type = Counter32
_CktAtmInClp0Cells_Object = MibTableColumn
cktAtmInClp0Cells = _CktAtmInClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 213),
    _CktAtmInClp0Cells_Type()
)
cktAtmInClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInClp0Cells.setStatus("mandatory")
_CktAtmInClp1Cells_Type = Counter32
_CktAtmInClp1Cells_Object = MibTableColumn
cktAtmInClp1Cells = _CktAtmInClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 214),
    _CktAtmInClp1Cells_Type()
)
cktAtmInClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktAtmInClp1Cells.setStatus("mandatory")
_CktATMAAL5CRC32Error_Type = Counter32
_CktATMAAL5CRC32Error_Object = MibTableColumn
cktATMAAL5CRC32Error = _CktATMAAL5CRC32Error_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 215),
    _CktATMAAL5CRC32Error_Type()
)
cktATMAAL5CRC32Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktATMAAL5CRC32Error.setStatus("mandatory")
_CktATMAAL5CPIError_Type = Counter32
_CktATMAAL5CPIError_Object = MibTableColumn
cktATMAAL5CPIError = _CktATMAAL5CPIError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 216),
    _CktATMAAL5CPIError_Type()
)
cktATMAAL5CPIError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktATMAAL5CPIError.setStatus("mandatory")
_CktATMAAL5LengthError_Type = Counter32
_CktATMAAL5LengthError_Object = MibTableColumn
cktATMAAL5LengthError = _CktATMAAL5LengthError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 217),
    _CktATMAAL5LengthError_Type()
)
cktATMAAL5LengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktATMAAL5LengthError.setStatus("mandatory")
_CktATMAAL5ReassemblyTimerError_Type = Counter32
_CktATMAAL5ReassemblyTimerError_Object = MibTableColumn
cktATMAAL5ReassemblyTimerError = _CktATMAAL5ReassemblyTimerError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 218),
    _CktATMAAL5ReassemblyTimerError_Type()
)
cktATMAAL5ReassemblyTimerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktATMAAL5ReassemblyTimerError.setStatus("mandatory")
_CktATMAAL5MaxNrSegError_Type = Counter32
_CktATMAAL5MaxNrSegError_Object = MibTableColumn
cktATMAAL5MaxNrSegError = _CktATMAAL5MaxNrSegError_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 219),
    _CktATMAAL5MaxNrSegError_Type()
)
cktATMAAL5MaxNrSegError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktATMAAL5MaxNrSegError.setStatus("mandatory")
_CktIWF1490to1483Error_Type = Counter32
_CktIWF1490to1483Error_Object = MibTableColumn
cktIWF1490to1483Error = _CktIWF1490to1483Error_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 220),
    _CktIWF1490to1483Error_Type()
)
cktIWF1490to1483Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktIWF1490to1483Error.setStatus("mandatory")
_CktIWF1490to1483LastBadHeader_Type = DisplayString
_CktIWF1490to1483LastBadHeader_Object = MibTableColumn
cktIWF1490to1483LastBadHeader = _CktIWF1490to1483LastBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 221),
    _CktIWF1490to1483LastBadHeader_Type()
)
cktIWF1490to1483LastBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktIWF1490to1483LastBadHeader.setStatus("mandatory")
_CktIWF1483to1490Error_Type = Counter32
_CktIWF1483to1490Error_Object = MibTableColumn
cktIWF1483to1490Error = _CktIWF1483to1490Error_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 222),
    _CktIWF1483to1490Error_Type()
)
cktIWF1483to1490Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktIWF1483to1490Error.setStatus("mandatory")
_CktIWF1483to1490LastBadHeader_Type = DisplayString
_CktIWF1483to1490LastBadHeader_Object = MibTableColumn
cktIWF1483to1490LastBadHeader = _CktIWF1483to1490LastBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 1, 1, 223),
    _CktIWF1483to1490LastBadHeader_Type()
)
cktIWF1483to1490LastBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktIWF1483to1490LastBadHeader.setStatus("mandatory")
_CktLeafTable_Object = MibTable
cktLeafTable = _CktLeafTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cktLeafTable.setStatus("mandatory")
_CktLeafEntry_Object = MibTableRow
cktLeafEntry = _CktLeafEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1)
)
cktLeafEntry.setIndexNames(
    (0, "CASCADE-MIB", "cktLeafSrcIfIndex"),
    (0, "CASCADE-MIB", "cktLeafSrcDlci"),
    (0, "CASCADE-MIB", "cktLeafEndpointIndex"),
)
if mibBuilder.loadTexts:
    cktLeafEntry.setStatus("mandatory")
_CktLeafSrcIfIndex_Type = Index
_CktLeafSrcIfIndex_Object = MibTableColumn
cktLeafSrcIfIndex = _CktLeafSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 1),
    _CktLeafSrcIfIndex_Type()
)
cktLeafSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafSrcIfIndex.setStatus("mandatory")
_CktLeafSrcDlci_Type = Integer32
_CktLeafSrcDlci_Object = MibTableColumn
cktLeafSrcDlci = _CktLeafSrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 2),
    _CktLeafSrcDlci_Type()
)
cktLeafSrcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafSrcDlci.setStatus("mandatory")
_CktLeafEndpointIndex_Type = Integer32
_CktLeafEndpointIndex_Object = MibTableColumn
cktLeafEndpointIndex = _CktLeafEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 3),
    _CktLeafEndpointIndex_Type()
)
cktLeafEndpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafEndpointIndex.setStatus("mandatory")
_CktLeafCreationTime_Type = TimeTicks
_CktLeafCreationTime_Object = MibTableColumn
cktLeafCreationTime = _CktLeafCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 4),
    _CktLeafCreationTime_Type()
)
cktLeafCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafCreationTime.setStatus("mandatory")
_CktLeafEgressIfIndex_Type = Index
_CktLeafEgressIfIndex_Object = MibTableColumn
cktLeafEgressIfIndex = _CktLeafEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 5),
    _CktLeafEgressIfIndex_Type()
)
cktLeafEgressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafEgressIfIndex.setStatus("mandatory")
_CktLeafEgressDlci_Type = Integer32
_CktLeafEgressDlci_Object = MibTableColumn
cktLeafEgressDlci = _CktLeafEgressDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 6),
    _CktLeafEgressDlci_Type()
)
cktLeafEgressDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafEgressDlci.setStatus("mandatory")
_CktLeafDestNodeId_Type = Integer32
_CktLeafDestNodeId_Object = MibTableColumn
cktLeafDestNodeId = _CktLeafDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 7),
    _CktLeafDestNodeId_Type()
)
cktLeafDestNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLeafDestNodeId.setStatus("mandatory")
_CktLeafDestIfIndex_Type = Index
_CktLeafDestIfIndex_Object = MibTableColumn
cktLeafDestIfIndex = _CktLeafDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 8),
    _CktLeafDestIfIndex_Type()
)
cktLeafDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLeafDestIfIndex.setStatus("mandatory")
_CktLeafDestDlci_Type = Integer32
_CktLeafDestDlci_Object = MibTableColumn
cktLeafDestDlci = _CktLeafDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 9),
    _CktLeafDestDlci_Type()
)
cktLeafDestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafDestDlci.setStatus("mandatory")
_CktLeafSvcCallingParty_Type = OctetString
_CktLeafSvcCallingParty_Object = MibTableColumn
cktLeafSvcCallingParty = _CktLeafSvcCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 10),
    _CktLeafSvcCallingParty_Type()
)
cktLeafSvcCallingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafSvcCallingParty.setStatus("mandatory")
_CktLeafSvcCalledParty_Type = OctetString
_CktLeafSvcCalledParty_Object = MibTableColumn
cktLeafSvcCalledParty = _CktLeafSvcCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 11),
    _CktLeafSvcCalledParty_Type()
)
cktLeafSvcCalledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafSvcCalledParty.setStatus("mandatory")


class _CktLeafAdminStatus_Type(Integer32):
    """Custom type cktLeafAdminStatus based on Integer32"""
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


_CktLeafAdminStatus_Type.__name__ = "Integer32"
_CktLeafAdminStatus_Object = MibTableColumn
cktLeafAdminStatus = _CktLeafAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 12),
    _CktLeafAdminStatus_Type()
)
cktLeafAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLeafAdminStatus.setStatus("mandatory")


class _CktLeafVcState_Type(Integer32):
    """Custom type cktLeafVcState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("backedup", 9),
          ("calling", 3),
          ("inactive", 1),
          ("retry", 2),
          ("slowretry", 12),
          ("svcall", 7),
          ("svclr", 8),
          ("wcbbkdp", 10),
          ("wcbdeact", 4),
          ("wcbdelete", 5),
          ("wcbreact", 11))
    )


_CktLeafVcState_Type.__name__ = "Integer32"
_CktLeafVcState_Object = MibTableColumn
cktLeafVcState = _CktLeafVcState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 13),
    _CktLeafVcState_Type()
)
cktLeafVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafVcState.setStatus("mandatory")


class _CktLeafOperStatus_Type(Integer32):
    """Custom type cktLeafOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktLeafOperStatus_Type.__name__ = "Integer32"
_CktLeafOperStatus_Object = MibTableColumn
cktLeafOperStatus = _CktLeafOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 14),
    _CktLeafOperStatus_Type()
)
cktLeafOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafOperStatus.setStatus("mandatory")


class _CktLeafDceState_Type(Integer32):
    """Custom type cktLeafDceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktLeafDceState_Type.__name__ = "Integer32"
_CktLeafDceState_Object = MibTableColumn
cktLeafDceState = _CktLeafDceState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 15),
    _CktLeafDceState_Type()
)
cktLeafDceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafDceState.setStatus("mandatory")


class _CktLeafDteStatus_Type(Integer32):
    """Custom type cktLeafDteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktLeafDteStatus_Type.__name__ = "Integer32"
_CktLeafDteStatus_Object = MibTableColumn
cktLeafDteStatus = _CktLeafDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 16),
    _CktLeafDteStatus_Type()
)
cktLeafDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafDteStatus.setStatus("mandatory")


class _CktLeafDteState_Type(Integer32):
    """Custom type cktLeafDteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CktLeafDteState_Type.__name__ = "Integer32"
_CktLeafDteState_Object = MibTableColumn
cktLeafDteState = _CktLeafDteState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 17),
    _CktLeafDteState_Type()
)
cktLeafDteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafDteState.setStatus("mandatory")
_CktLeafVcPtr_Type = OctetString
_CktLeafVcPtr_Object = MibTableColumn
cktLeafVcPtr = _CktLeafVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 18),
    _CktLeafVcPtr_Type()
)
cktLeafVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafVcPtr.setStatus("mandatory")
_CktLeafHopCnt_Type = Integer32
_CktLeafHopCnt_Object = MibTableColumn
cktLeafHopCnt = _CktLeafHopCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 19),
    _CktLeafHopCnt_Type()
)
cktLeafHopCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafHopCnt.setStatus("mandatory")
_CktLeafPath_Type = OctetString
_CktLeafPath_Object = MibTableColumn
cktLeafPath = _CktLeafPath_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 20),
    _CktLeafPath_Type()
)
cktLeafPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafPath.setStatus("mandatory")


class _CktLeafFailReason_Type(Integer32):
    """Custom type cktLeafFailReason based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 1),
          ("balancereroute", 10),
          ("bkpdlcicollision", 25),
          ("bothendptbackup", 29),
          ("dead", 11),
          ("defpathreroute", 12),
          ("dstunknown", 24),
          ("iopdown", 17),
          ("misconfig", 20),
          ("nevercalled", 28),
          ("nidown", 13),
          ("nobw", 3),
          ("nodest", 7),
          ("nomultipointparent", 31),
          ("nopdubuff", 6),
          ("noport", 19),
          ("noroute", 4),
          ("novcbuff", 2),
          ("novpivci", 33),
          ("numsgbuffer", 18),
          ("oldrevinpath", 26),
          ("otherpvcsegdown", 14),
          ("otherpvcsegrnr", 15),
          ("pvcroutefail", 32),
          ("pvcroutemgttrunk", 30),
          ("smdsmgmttrunk", 27),
          ("srcbackedup", 22),
          ("srcunknown", 23),
          ("svcsetupfail", 21),
          ("timeout", 5),
          ("trkdown", 9),
          ("trkrnr", 8),
          ("usingaltpathwarning", 16))
    )


_CktLeafFailReason_Type.__name__ = "Integer32"
_CktLeafFailReason_Object = MibTableColumn
cktLeafFailReason = _CktLeafFailReason_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 21),
    _CktLeafFailReason_Type()
)
cktLeafFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafFailReason.setStatus("mandatory")
_CktLeafFailNode_Type = Integer32
_CktLeafFailNode_Object = MibTableColumn
cktLeafFailNode = _CktLeafFailNode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 22),
    _CktLeafFailNode_Type()
)
cktLeafFailNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafFailNode.setStatus("mandatory")
_CktLeafFailPort_Type = Integer32
_CktLeafFailPort_Object = MibTableColumn
cktLeafFailPort = _CktLeafFailPort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 23),
    _CktLeafFailPort_Type()
)
cktLeafFailPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafFailPort.setStatus("mandatory")
_CktLeafHelloCounter_Type = Integer32
_CktLeafHelloCounter_Object = MibTableColumn
cktLeafHelloCounter = _CktLeafHelloCounter_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 24),
    _CktLeafHelloCounter_Type()
)
cktLeafHelloCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafHelloCounter.setStatus("mandatory")
_CktLeafHelloAckCounter_Type = Integer32
_CktLeafHelloAckCounter_Object = MibTableColumn
cktLeafHelloAckCounter = _CktLeafHelloAckCounter_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 25),
    _CktLeafHelloAckCounter_Type()
)
cktLeafHelloAckCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafHelloAckCounter.setStatus("mandatory")
_CktLeafAtmVPI_Type = Integer32
_CktLeafAtmVPI_Object = MibTableColumn
cktLeafAtmVPI = _CktLeafAtmVPI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 26),
    _CktLeafAtmVPI_Type()
)
cktLeafAtmVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLeafAtmVPI.setStatus("mandatory")
_CktLeafAtmVCI_Type = Integer32
_CktLeafAtmVCI_Object = MibTableColumn
cktLeafAtmVCI = _CktLeafAtmVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 27),
    _CktLeafAtmVCI_Type()
)
cktLeafAtmVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cktLeafAtmVCI.setStatus("mandatory")


class _CktLeafType_Type(Integer32):
    """Custom type cktLeafType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_CktLeafType_Type.__name__ = "Integer32"
_CktLeafType_Object = MibTableColumn
cktLeafType = _CktLeafType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 28),
    _CktLeafType_Type()
)
cktLeafType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafType.setStatus("mandatory")
_CktLeafAtmInCells_Type = Counter32
_CktLeafAtmInCells_Object = MibTableColumn
cktLeafAtmInCells = _CktLeafAtmInCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 29),
    _CktLeafAtmInCells_Type()
)
cktLeafAtmInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInCells.setStatus("mandatory")
_CktLeafAtmOutCells_Type = Counter32
_CktLeafAtmOutCells_Object = MibTableColumn
cktLeafAtmOutCells = _CktLeafAtmOutCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 30),
    _CktLeafAtmOutCells_Type()
)
cktLeafAtmOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmOutCells.setStatus("mandatory")
_CktLeafAtmInDiscardedClp0Cells_Type = Counter32
_CktLeafAtmInDiscardedClp0Cells_Object = MibTableColumn
cktLeafAtmInDiscardedClp0Cells = _CktLeafAtmInDiscardedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 31),
    _CktLeafAtmInDiscardedClp0Cells_Type()
)
cktLeafAtmInDiscardedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInDiscardedClp0Cells.setStatus("mandatory")
_CktLeafAtmInDiscardedClp1Cells_Type = Counter32
_CktLeafAtmInDiscardedClp1Cells_Object = MibTableColumn
cktLeafAtmInDiscardedClp1Cells = _CktLeafAtmInDiscardedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 32),
    _CktLeafAtmInDiscardedClp1Cells_Type()
)
cktLeafAtmInDiscardedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInDiscardedClp1Cells.setStatus("mandatory")
_CktLeafAtmInPassedClp0Cells_Type = Counter32
_CktLeafAtmInPassedClp0Cells_Object = MibTableColumn
cktLeafAtmInPassedClp0Cells = _CktLeafAtmInPassedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 33),
    _CktLeafAtmInPassedClp0Cells_Type()
)
cktLeafAtmInPassedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInPassedClp0Cells.setStatus("mandatory")
_CktLeafAtmInPassedClp1Cells_Type = Counter32
_CktLeafAtmInPassedClp1Cells_Object = MibTableColumn
cktLeafAtmInPassedClp1Cells = _CktLeafAtmInPassedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 34),
    _CktLeafAtmInPassedClp1Cells_Type()
)
cktLeafAtmInPassedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInPassedClp1Cells.setStatus("mandatory")
_CktLeafAtmInTaggedCells_Type = Counter32
_CktLeafAtmInTaggedCells_Object = MibTableColumn
cktLeafAtmInTaggedCells = _CktLeafAtmInTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 35),
    _CktLeafAtmInTaggedCells_Type()
)
cktLeafAtmInTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmInTaggedCells.setStatus("mandatory")
_CktLeafAtmOutClp0Cells_Type = Counter32
_CktLeafAtmOutClp0Cells_Object = MibTableColumn
cktLeafAtmOutClp0Cells = _CktLeafAtmOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 36),
    _CktLeafAtmOutClp0Cells_Type()
)
cktLeafAtmOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmOutClp0Cells.setStatus("mandatory")
_CktLeafAtmOutClp1Cells_Type = Counter32
_CktLeafAtmOutClp1Cells_Object = MibTableColumn
cktLeafAtmOutClp1Cells = _CktLeafAtmOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 2, 1, 37),
    _CktLeafAtmOutClp1Cells_Type()
)
cktLeafAtmOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktLeafAtmOutClp1Cells.setStatus("mandatory")
_CktSmdsRtTable_Object = MibTable
cktSmdsRtTable = _CktSmdsRtTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cktSmdsRtTable.setStatus("mandatory")
_CktSmdsRtEntry_Object = MibTableRow
cktSmdsRtEntry = _CktSmdsRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1)
)
cktSmdsRtEntry.setIndexNames(
    (0, "CASCADE-MIB", "cktSmdsRemoteNode"),
)
if mibBuilder.loadTexts:
    cktSmdsRtEntry.setStatus("mandatory")
_CktSmdsRemoteNode_Type = Integer32
_CktSmdsRemoteNode_Object = MibTableColumn
cktSmdsRemoteNode = _CktSmdsRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 1),
    _CktSmdsRemoteNode_Type()
)
cktSmdsRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsRemoteNode.setStatus("mandatory")
_CktSmdsHopCnt_Type = Integer32
_CktSmdsHopCnt_Object = MibTableColumn
cktSmdsHopCnt = _CktSmdsHopCnt_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 2),
    _CktSmdsHopCnt_Type()
)
cktSmdsHopCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsHopCnt.setStatus("mandatory")
_CktSmdsRoute_Type = OctetString
_CktSmdsRoute_Object = MibTableColumn
cktSmdsRoute = _CktSmdsRoute_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 3),
    _CktSmdsRoute_Type()
)
cktSmdsRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsRoute.setStatus("mandatory")
_CktSmdsLocalPort_Type = Integer32
_CktSmdsLocalPort_Object = MibTableColumn
cktSmdsLocalPort = _CktSmdsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 4),
    _CktSmdsLocalPort_Type()
)
cktSmdsLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsLocalPort.setStatus("mandatory")
_CktSmdsRemotePort_Type = Integer32
_CktSmdsRemotePort_Object = MibTableColumn
cktSmdsRemotePort = _CktSmdsRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 5),
    _CktSmdsRemotePort_Type()
)
cktSmdsRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsRemotePort.setStatus("mandatory")
_CktSmdsVcState_Type = Integer32
_CktSmdsVcState_Object = MibTableColumn
cktSmdsVcState = _CktSmdsVcState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 6, 3, 1, 6),
    _CktSmdsVcState_Type()
)
cktSmdsVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktSmdsVcState.setStatus("mandatory")
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 7)
)
_CardNumber_Type = Integer32
_CardNumber_Object = MibScalar
cardNumber = _CardNumber_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 1),
    _CardNumber_Type()
)
cardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNumber.setStatus("mandatory")
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1)
)
cardEntry.setIndexNames(
    (0, "CASCADE-MIB", "cardLogicalSlotId"),
    (0, "CASCADE-MIB", "cardRedundState"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("mandatory")
_CardLogicalSlotId_Type = Integer32
_CardLogicalSlotId_Object = MibTableColumn
cardLogicalSlotId = _CardLogicalSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 1),
    _CardLogicalSlotId_Type()
)
cardLogicalSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLogicalSlotId.setStatus("mandatory")
_CardPhysicalSlotId_Type = Integer32
_CardPhysicalSlotId_Object = MibTableColumn
cardPhysicalSlotId = _CardPhysicalSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 2),
    _CardPhysicalSlotId_Type()
)
cardPhysicalSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPhysicalSlotId.setStatus("mandatory")
_CardAdminType_Type = CardTypes
_CardAdminType_Object = MibTableColumn
cardAdminType = _CardAdminType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 3),
    _CardAdminType_Type()
)
cardAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminType.setStatus("mandatory")
_CardOperType_Type = CardTypes
_CardOperType_Object = MibTableColumn
cardOperType = _CardOperType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 4),
    _CardOperType_Type()
)
cardOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperType.setStatus("mandatory")


class _CardState_Type(Integer32):
    """Custom type cardState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("debug", 11),
          ("down", 10),
          ("init", 4),
          ("loading", 2),
          ("offlinediag", 12),
          ("present", 1),
          ("ready", 7),
          ("start", 3),
          ("stopped", 9),
          ("sync", 5),
          ("syncdone", 6))
    )


_CardState_Type.__name__ = "Integer32"
_CardState_Object = MibTableColumn
cardState = _CardState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 5),
    _CardState_Type()
)
cardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardState.setStatus("mandatory")
_CardAdminStatus_Type = CardStatuses
_CardAdminStatus_Object = MibTableColumn
cardAdminStatus = _CardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 6),
    _CardAdminStatus_Type()
)
cardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminStatus.setStatus("mandatory")
_CardOperStatus_Type = CardStatuses
_CardOperStatus_Object = MibTableColumn
cardOperStatus = _CardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 7),
    _CardOperStatus_Type()
)
cardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperStatus.setStatus("mandatory")


class _CardDiagStatus_Type(Integer32):
    """Custom type cardDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("marginal", 2),
          ("ok", 1))
    )


_CardDiagStatus_Type.__name__ = "Integer32"
_CardDiagStatus_Object = MibTableColumn
cardDiagStatus = _CardDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 8),
    _CardDiagStatus_Type()
)
cardDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagStatus.setStatus("mandatory")


class _CardRedundConfig_Type(Integer32):
    """Custom type cardRedundConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("configured", 1)
    )


_CardRedundConfig_Type.__name__ = "Integer32"
_CardRedundConfig_Object = MibTableColumn
cardRedundConfig = _CardRedundConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 9),
    _CardRedundConfig_Type()
)
cardRedundConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRedundConfig.setStatus("mandatory")
_CardRedundSlotMask_Type = Integer32
_CardRedundSlotMask_Object = MibTableColumn
cardRedundSlotMask = _CardRedundSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 10),
    _CardRedundSlotMask_Type()
)
cardRedundSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardRedundSlotMask.setStatus("mandatory")


class _CardRedundActual_Type(Integer32):
    """Custom type cardRedundActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("not-connected", 2))
    )


_CardRedundActual_Type.__name__ = "Integer32"
_CardRedundActual_Object = MibTableColumn
cardRedundActual = _CardRedundActual_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 11),
    _CardRedundActual_Type()
)
cardRedundActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRedundActual.setStatus("mandatory")


class _CardRedundState_Type(Integer32):
    """Custom type cardRedundState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_CardRedundState_Type.__name__ = "Integer32"
_CardRedundState_Object = MibTableColumn
cardRedundState = _CardRedundState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 12),
    _CardRedundState_Type()
)
cardRedundState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRedundState.setStatus("mandatory")
_CardToRedundant_Type = TimeTicks
_CardToRedundant_Object = MibTableColumn
cardToRedundant = _CardToRedundant_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 13),
    _CardToRedundant_Type()
)
cardToRedundant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardToRedundant.setStatus("mandatory")


class _CardDiagNonFatalSource_Type(Integer32):
    """Custom type cardDiagNonFatalSource based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("background-diagnostics", 2),
          ("card-level", 7),
          ("data-alignment", 10),
          ("device-driver-level", 11),
          ("fault", 3),
          ("frame-heap", 4),
          ("general", 9),
          ("i960-data-structures", 8),
          ("power-on-diagnostics", 1),
          ("redundancy", 5),
          ("system-level", 6))
    )


_CardDiagNonFatalSource_Type.__name__ = "Integer32"
_CardDiagNonFatalSource_Object = MibTableColumn
cardDiagNonFatalSource = _CardDiagNonFatalSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 14),
    _CardDiagNonFatalSource_Type()
)
cardDiagNonFatalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagNonFatalSource.setStatus("mandatory")
_CardDiagNonFatalTime_Type = TimeTicks
_CardDiagNonFatalTime_Object = MibTableColumn
cardDiagNonFatalTime = _CardDiagNonFatalTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 15),
    _CardDiagNonFatalTime_Type()
)
cardDiagNonFatalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagNonFatalTime.setStatus("mandatory")
_CardDiagNonFatalErrMajor_Type = Integer32
_CardDiagNonFatalErrMajor_Object = MibTableColumn
cardDiagNonFatalErrMajor = _CardDiagNonFatalErrMajor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 16),
    _CardDiagNonFatalErrMajor_Type()
)
cardDiagNonFatalErrMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagNonFatalErrMajor.setStatus("mandatory")
_CardDiagNonFatalErrMinor_Type = Integer32
_CardDiagNonFatalErrMinor_Object = MibTableColumn
cardDiagNonFatalErrMinor = _CardDiagNonFatalErrMinor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 17),
    _CardDiagNonFatalErrMinor_Type()
)
cardDiagNonFatalErrMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagNonFatalErrMinor.setStatus("mandatory")
_CardDiagNonFatalStr_Type = DisplayString
_CardDiagNonFatalStr_Object = MibTableColumn
cardDiagNonFatalStr = _CardDiagNonFatalStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 18),
    _CardDiagNonFatalStr_Type()
)
cardDiagNonFatalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagNonFatalStr.setStatus("mandatory")


class _CardDiagFatalSource_Type(Integer32):
    """Custom type cardDiagFatalSource based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("background-diagnostics", 2),
          ("card-level", 7),
          ("data-alignment", 10),
          ("device-driver-level", 11),
          ("fault", 3),
          ("frame-heap", 4),
          ("general", 9),
          ("i960-data-structures", 8),
          ("power-on-diagnostics", 1),
          ("redundancy", 5),
          ("system-level", 6))
    )


_CardDiagFatalSource_Type.__name__ = "Integer32"
_CardDiagFatalSource_Object = MibTableColumn
cardDiagFatalSource = _CardDiagFatalSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 19),
    _CardDiagFatalSource_Type()
)
cardDiagFatalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalSource.setStatus("mandatory")
_CardDiagFatalTime_Type = TimeTicks
_CardDiagFatalTime_Object = MibTableColumn
cardDiagFatalTime = _CardDiagFatalTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 20),
    _CardDiagFatalTime_Type()
)
cardDiagFatalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalTime.setStatus("mandatory")
_CardDiagFatalErrMajor_Type = Integer32
_CardDiagFatalErrMajor_Object = MibTableColumn
cardDiagFatalErrMajor = _CardDiagFatalErrMajor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 21),
    _CardDiagFatalErrMajor_Type()
)
cardDiagFatalErrMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalErrMajor.setStatus("mandatory")
_CardDiagFatalErrMinor_Type = Integer32
_CardDiagFatalErrMinor_Object = MibTableColumn
cardDiagFatalErrMinor = _CardDiagFatalErrMinor_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 22),
    _CardDiagFatalErrMinor_Type()
)
cardDiagFatalErrMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalErrMinor.setStatus("mandatory")
_CardDiagFatalStr_Type = DisplayString
_CardDiagFatalStr_Object = MibTableColumn
cardDiagFatalStr = _CardDiagFatalStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 23),
    _CardDiagFatalStr_Type()
)
cardDiagFatalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalStr.setStatus("mandatory")
_CardDiagFatalReboots_Type = Counter32
_CardDiagFatalReboots_Object = MibTableColumn
cardDiagFatalReboots = _CardDiagFatalReboots_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 24),
    _CardDiagFatalReboots_Type()
)
cardDiagFatalReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalReboots.setStatus("mandatory")
_CardDiagFatalAddress_Type = Integer32
_CardDiagFatalAddress_Object = MibTableColumn
cardDiagFatalAddress = _CardDiagFatalAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 25),
    _CardDiagFatalAddress_Type()
)
cardDiagFatalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFatalAddress.setStatus("mandatory")
_CardDiagBackgroundPasses_Type = Counter32
_CardDiagBackgroundPasses_Object = MibTableColumn
cardDiagBackgroundPasses = _CardDiagBackgroundPasses_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 26),
    _CardDiagBackgroundPasses_Type()
)
cardDiagBackgroundPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagBackgroundPasses.setStatus("mandatory")
_CardDiagBackgroundFailures_Type = Counter32
_CardDiagBackgroundFailures_Object = MibTableColumn
cardDiagBackgroundFailures = _CardDiagBackgroundFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 27),
    _CardDiagBackgroundFailures_Type()
)
cardDiagBackgroundFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagBackgroundFailures.setStatus("mandatory")
_CardDiagBackgroundSuccesses_Type = Counter32
_CardDiagBackgroundSuccesses_Object = MibTableColumn
cardDiagBackgroundSuccesses = _CardDiagBackgroundSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 28),
    _CardDiagBackgroundSuccesses_Type()
)
cardDiagBackgroundSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagBackgroundSuccesses.setStatus("mandatory")


class _CardDiagLEDReset_Type(Integer32):
    """Custom type cardDiagLEDReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("state-to-active", 1)
    )


_CardDiagLEDReset_Type.__name__ = "Integer32"
_CardDiagLEDReset_Object = MibTableColumn
cardDiagLEDReset = _CardDiagLEDReset_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 29),
    _CardDiagLEDReset_Type()
)
cardDiagLEDReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagLEDReset.setStatus("mandatory")


class _CardDiagPowerExtensive_Type(Integer32):
    """Custom type cardDiagPowerExtensive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("extensive-tests", 1)
    )


_CardDiagPowerExtensive_Type.__name__ = "Integer32"
_CardDiagPowerExtensive_Object = MibTableColumn
cardDiagPowerExtensive = _CardDiagPowerExtensive_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 30),
    _CardDiagPowerExtensive_Type()
)
cardDiagPowerExtensive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagPowerExtensive.setStatus("mandatory")
_CardCpuUtil_Type = Gauge32
_CardCpuUtil_Object = MibTableColumn
cardCpuUtil = _CardCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 31),
    _CardCpuUtil_Type()
)
cardCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCpuUtil.setStatus("mandatory")
_CardMemoryUsage_Type = Gauge32
_CardMemoryUsage_Object = MibTableColumn
cardMemoryUsage = _CardMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 32),
    _CardMemoryUsage_Type()
)
cardMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMemoryUsage.setStatus("mandatory")
_CardMaxVCs_Type = Gauge32
_CardMaxVCs_Object = MibTableColumn
cardMaxVCs = _CardMaxVCs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 33),
    _CardMaxVCs_Type()
)
cardMaxVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMaxVCs.setStatus("mandatory")
_CardInUseVCs_Type = Gauge32
_CardInUseVCs_Object = MibTableColumn
cardInUseVCs = _CardInUseVCs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 34),
    _CardInUseVCs_Type()
)
cardInUseVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInUseVCs.setStatus("mandatory")
_CardFreeVCs_Type = Gauge32
_CardFreeVCs_Object = MibTableColumn
cardFreeVCs = _CardFreeVCs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 35),
    _CardFreeVCs_Type()
)
cardFreeVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFreeVCs.setStatus("mandatory")
_CardInOctets_Type = Counter32
_CardInOctets_Object = MibTableColumn
cardInOctets = _CardInOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 36),
    _CardInOctets_Type()
)
cardInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInOctets.setStatus("mandatory")
_CardInPkts_Type = Counter32
_CardInPkts_Object = MibTableColumn
cardInPkts = _CardInPkts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 37),
    _CardInPkts_Type()
)
cardInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInPkts.setStatus("mandatory")
_CardOutOctets_Type = Counter32
_CardOutOctets_Object = MibTableColumn
cardOutOctets = _CardOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 38),
    _CardOutOctets_Type()
)
cardOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutOctets.setStatus("mandatory")
_CardOutPkts_Type = Counter32
_CardOutPkts_Object = MibTableColumn
cardOutPkts = _CardOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 39),
    _CardOutPkts_Type()
)
cardOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutPkts.setStatus("mandatory")
_CardToWarmboot_Type = TimeTicks
_CardToWarmboot_Object = MibTableColumn
cardToWarmboot = _CardToWarmboot_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 40),
    _CardToWarmboot_Type()
)
cardToWarmboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardToWarmboot.setStatus("mandatory")
_CardToColdboot_Type = TimeTicks
_CardToColdboot_Object = MibTableColumn
cardToColdboot = _CardToColdboot_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 41),
    _CardToColdboot_Type()
)
cardToColdboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardToColdboot.setStatus("mandatory")
_CardModel_Type = DisplayString
_CardModel_Object = MibTableColumn
cardModel = _CardModel_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 42),
    _CardModel_Type()
)
cardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardModel.setStatus("mandatory")
_CardSerial_Type = DisplayString
_CardSerial_Object = MibTableColumn
cardSerial = _CardSerial_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 43),
    _CardSerial_Type()
)
cardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerial.setStatus("mandatory")
_CardSwRev_Type = DisplayString
_CardSwRev_Object = MibTableColumn
cardSwRev = _CardSwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 44),
    _CardSwRev_Type()
)
cardSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwRev.setStatus("mandatory")
_CardHwRev_Type = DisplayString
_CardHwRev_Object = MibTableColumn
cardHwRev = _CardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 45),
    _CardHwRev_Type()
)
cardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHwRev.setStatus("mandatory")
_CardEpromRev_Type = DisplayString
_CardEpromRev_Object = MibTableColumn
cardEpromRev = _CardEpromRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 46),
    _CardEpromRev_Type()
)
cardEpromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardEpromRev.setStatus("mandatory")
_CardName_Type = DisplayString
_CardName_Object = MibTableColumn
cardName = _CardName_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 47),
    _CardName_Type()
)
cardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardName.setStatus("mandatory")
_CardCktGroupTrap_Type = OctetString
_CardCktGroupTrap_Object = MibTableColumn
cardCktGroupTrap = _CardCktGroupTrap_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 48),
    _CardCktGroupTrap_Type()
)
cardCktGroupTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCktGroupTrap.setStatus("mandatory")
_CardOutBtus_Type = Counter32
_CardOutBtus_Object = MibTableColumn
cardOutBtus = _CardOutBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 49),
    _CardOutBtus_Type()
)
cardOutBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutBtus.setStatus("mandatory")
_CardInGoodBtus_Type = Counter32
_CardInGoodBtus_Object = MibTableColumn
cardInGoodBtus = _CardInGoodBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 50),
    _CardInGoodBtus_Type()
)
cardInGoodBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInGoodBtus.setStatus("mandatory")
_CardInErrorBtus_Type = Counter32
_CardInErrorBtus_Object = MibTableColumn
cardInErrorBtus = _CardInErrorBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 51),
    _CardInErrorBtus_Type()
)
cardInErrorBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInErrorBtus.setStatus("mandatory")
_CardInNoVcBtus_Type = Counter32
_CardInNoVcBtus_Object = MibTableColumn
cardInNoVcBtus = _CardInNoVcBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 52),
    _CardInNoVcBtus_Type()
)
cardInNoVcBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInNoVcBtus.setStatus("mandatory")
_CardInLinkDownBtus_Type = Counter32
_CardInLinkDownBtus_Object = MibTableColumn
cardInLinkDownBtus = _CardInLinkDownBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 53),
    _CardInLinkDownBtus_Type()
)
cardInLinkDownBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInLinkDownBtus.setStatus("mandatory")
_CardInNoBufferBtus_Type = Counter32
_CardInNoBufferBtus_Object = MibTableColumn
cardInNoBufferBtus = _CardInNoBufferBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 54),
    _CardInNoBufferBtus_Type()
)
cardInNoBufferBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInNoBufferBtus.setStatus("mandatory")
_CardInForwardBitBtus_Type = Counter32
_CardInForwardBitBtus_Object = MibTableColumn
cardInForwardBitBtus = _CardInForwardBitBtus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 55),
    _CardInForwardBitBtus_Type()
)
cardInForwardBitBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInForwardBitBtus.setStatus("mandatory")
_CardDiagTestId_Type = Integer32
_CardDiagTestId_Object = MibTableColumn
cardDiagTestId = _CardDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 56),
    _CardDiagTestId_Type()
)
cardDiagTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagTestId.setStatus("mandatory")
_CardDiagTestRuns_Type = Integer32
_CardDiagTestRuns_Object = MibTableColumn
cardDiagTestRuns = _CardDiagTestRuns_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 57),
    _CardDiagTestRuns_Type()
)
cardDiagTestRuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagTestRuns.setStatus("mandatory")


class _CardDiagState_Type(Integer32):
    """Custom type cardDiagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_CardDiagState_Type.__name__ = "Integer32"
_CardDiagState_Object = MibTableColumn
cardDiagState = _CardDiagState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 58),
    _CardDiagState_Type()
)
cardDiagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagState.setStatus("mandatory")
_CardDiagOptionStr_Type = OctetString
_CardDiagOptionStr_Object = MibTableColumn
cardDiagOptionStr = _CardDiagOptionStr_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 59),
    _CardDiagOptionStr_Type()
)
cardDiagOptionStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagOptionStr.setStatus("mandatory")
_CardDiagPasses_Type = Counter32
_CardDiagPasses_Object = MibTableColumn
cardDiagPasses = _CardDiagPasses_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 60),
    _CardDiagPasses_Type()
)
cardDiagPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagPasses.setStatus("mandatory")
_CardDiagFailures_Type = Counter32
_CardDiagFailures_Object = MibTableColumn
cardDiagFailures = _CardDiagFailures_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 61),
    _CardDiagFailures_Type()
)
cardDiagFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagFailures.setStatus("mandatory")
_CardDiagResultString_Type = DisplayString
_CardDiagResultString_Object = MibTableColumn
cardDiagResultString = _CardDiagResultString_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 62),
    _CardDiagResultString_Type()
)
cardDiagResultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDiagResultString.setStatus("mandatory")
_CardFrameMemoryUtil_Type = Gauge32
_CardFrameMemoryUtil_Object = MibTableColumn
cardFrameMemoryUtil = _CardFrameMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 63),
    _CardFrameMemoryUtil_Type()
)
cardFrameMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFrameMemoryUtil.setStatus("mandatory")


class _CardResetPram_Type(Integer32):
    """Custom type cardResetPram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-pram", 1)
    )


_CardResetPram_Type.__name__ = "Integer32"
_CardResetPram_Object = MibTableColumn
cardResetPram = _CardResetPram_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 64),
    _CardResetPram_Type()
)
cardResetPram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardResetPram.setStatus("mandatory")
_CardMemoryUtil_Type = Gauge32
_CardMemoryUtil_Object = MibTableColumn
cardMemoryUtil = _CardMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 65),
    _CardMemoryUtil_Type()
)
cardMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMemoryUtil.setStatus("mandatory")
_CardFrameMemoryUsage_Type = Gauge32
_CardFrameMemoryUsage_Object = MibTableColumn
cardFrameMemoryUsage = _CardFrameMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 66),
    _CardFrameMemoryUsage_Type()
)
cardFrameMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFrameMemoryUsage.setStatus("mandatory")
_CardUpTime_Type = TimeTicks
_CardUpTime_Object = MibTableColumn
cardUpTime = _CardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 67),
    _CardUpTime_Type()
)
cardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardUpTime.setStatus("mandatory")
_CardPramChecksum_Type = Integer32
_CardPramChecksum_Object = MibTableColumn
cardPramChecksum = _CardPramChecksum_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 68),
    _CardPramChecksum_Type()
)
cardPramChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPramChecksum.setStatus("mandatory")
_CardPhysicalIndex_Type = Integer32
_CardPhysicalIndex_Object = MibTableColumn
cardPhysicalIndex = _CardPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 69),
    _CardPhysicalIndex_Type()
)
cardPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPhysicalIndex.setStatus("mandatory")
_CardExternalClockRate_Type = Integer32
_CardExternalClockRate_Object = MibTableColumn
cardExternalClockRate = _CardExternalClockRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 70),
    _CardExternalClockRate_Type()
)
cardExternalClockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardExternalClockRate.setStatus("mandatory")


class _CardShootState_Type(Integer32):
    """Custom type cardShootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shoot-enabled", 1)
    )


_CardShootState_Type.__name__ = "Integer32"
_CardShootState_Object = MibTableColumn
cardShootState = _CardShootState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 71),
    _CardShootState_Type()
)
cardShootState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardShootState.setStatus("mandatory")


class _CardEraseAll_Type(Integer32):
    """Custom type cardEraseAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase-all", 1)
    )


_CardEraseAll_Type.__name__ = "Integer32"
_CardEraseAll_Object = MibTableColumn
cardEraseAll = _CardEraseAll_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 72),
    _CardEraseAll_Type()
)
cardEraseAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardEraseAll.setStatus("mandatory")


class _CardAdminCapability_Type(Integer32):
    """Custom type cardAdminCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cp-30", 5),
          ("cp-40", 9),
          ("cp-50", 10),
          ("cp-basic", 4),
          ("cp-plus", 8),
          ("iom-fcp", 11),
          ("iop-16meg-service", 3),
          ("iop-frame-relay", 1),
          ("iop-multi-service", 2))
    )


_CardAdminCapability_Type.__name__ = "Integer32"
_CardAdminCapability_Object = MibTableColumn
cardAdminCapability = _CardAdminCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 73),
    _CardAdminCapability_Type()
)
cardAdminCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminCapability.setStatus("mandatory")


class _CardOperCapability_Type(Integer32):
    """Custom type cardOperCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cp-30", 5),
          ("cp-40", 9),
          ("cp-50", 10),
          ("cp-basic", 4),
          ("cp-plus", 8),
          ("iom-fcp", 11),
          ("iop-16meg-service", 3),
          ("iop-frame-relay", 1),
          ("iop-multi-service", 2))
    )


_CardOperCapability_Type.__name__ = "Integer32"
_CardOperCapability_Object = MibTableColumn
cardOperCapability = _CardOperCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 74),
    _CardOperCapability_Type()
)
cardOperCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperCapability.setStatus("mandatory")


class _CardISDNswtype_Type(Integer32):
    """Custom type cardISDNswtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("att-4ess", 1),
          ("att-5ess", 2),
          ("dms100", 3))
    )


_CardISDNswtype_Type.__name__ = "Integer32"
_CardISDNswtype_Object = MibTableColumn
cardISDNswtype = _CardISDNswtype_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 75),
    _CardISDNswtype_Type()
)
cardISDNswtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardISDNswtype.setStatus("mandatory")
_CardCpuFgUtil_Type = Gauge32
_CardCpuFgUtil_Object = MibTableColumn
cardCpuFgUtil = _CardCpuFgUtil_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 76),
    _CardCpuFgUtil_Type()
)
cardCpuFgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCpuFgUtil.setStatus("mandatory")


class _CardTrkProtState_Type(Integer32):
    """Custom type cardTrkProtState based on Integer32"""
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


_CardTrkProtState_Type.__name__ = "Integer32"
_CardTrkProtState_Object = MibTableColumn
cardTrkProtState = _CardTrkProtState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 77),
    _CardTrkProtState_Type()
)
cardTrkProtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTrkProtState.setStatus("mandatory")


class _CardISDNSigType_Type(Integer32):
    """Custom type cardISDNSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nfas", 2),
          ("no-nfas", 1))
    )


_CardISDNSigType_Type.__name__ = "Integer32"
_CardISDNSigType_Object = MibTableColumn
cardISDNSigType = _CardISDNSigType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 78),
    _CardISDNSigType_Type()
)
cardISDNSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardISDNSigType.setStatus("mandatory")


class _CardISDNChanId_Type(Integer32):
    """Custom type cardISDNChanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("preferred", 2))
    )


_CardISDNChanId_Type.__name__ = "Integer32"
_CardISDNChanId_Object = MibTableColumn
cardISDNChanId = _CardISDNChanId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 79),
    _CardISDNChanId_Type()
)
cardISDNChanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardISDNChanId.setStatus("mandatory")


class _CardTransmitClockConfig_Type(Integer32):
    """Custom type cardTransmitClockConfig based on Integer32"""
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
        *(("e1-G703sec10-clock", 5),
          ("e1-network-clock", 6),
          ("free-running-clock", 4),
          ("system-primary-clock", 1),
          ("system-primary-secondary-clock", 3),
          ("system-secondary-clock", 2))
    )


_CardTransmitClockConfig_Type.__name__ = "Integer32"
_CardTransmitClockConfig_Object = MibTableColumn
cardTransmitClockConfig = _CardTransmitClockConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 80),
    _CardTransmitClockConfig_Type()
)
cardTransmitClockConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTransmitClockConfig.setStatus("mandatory")


class _CardTransmitClockSwitchOver_Type(Integer32):
    """Custom type cardTransmitClockSwitchOver based on Integer32"""
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


_CardTransmitClockSwitchOver_Type.__name__ = "Integer32"
_CardTransmitClockSwitchOver_Object = MibTableColumn
cardTransmitClockSwitchOver = _CardTransmitClockSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 81),
    _CardTransmitClockSwitchOver_Type()
)
cardTransmitClockSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTransmitClockSwitchOver.setStatus("mandatory")


class _CardTransmitClockStatus_Type(Integer32):
    """Custom type cardTransmitClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-synchronization", 1),
          ("loss-of-synchronization", 2))
    )


_CardTransmitClockStatus_Type.__name__ = "Integer32"
_CardTransmitClockStatus_Object = MibTableColumn
cardTransmitClockStatus = _CardTransmitClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 82),
    _CardTransmitClockStatus_Type()
)
cardTransmitClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTransmitClockStatus.setStatus("mandatory")
_CardSystemPrimaryClockPortConfig_Type = Integer32
_CardSystemPrimaryClockPortConfig_Object = MibTableColumn
cardSystemPrimaryClockPortConfig = _CardSystemPrimaryClockPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 83),
    _CardSystemPrimaryClockPortConfig_Type()
)
cardSystemPrimaryClockPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSystemPrimaryClockPortConfig.setStatus("mandatory")


class _CardSystemPrimaryClockStatus_Type(Integer32):
    """Custom type cardSystemPrimaryClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 1))
    )


_CardSystemPrimaryClockStatus_Type.__name__ = "Integer32"
_CardSystemPrimaryClockStatus_Object = MibTableColumn
cardSystemPrimaryClockStatus = _CardSystemPrimaryClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 84),
    _CardSystemPrimaryClockStatus_Type()
)
cardSystemPrimaryClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSystemPrimaryClockStatus.setStatus("mandatory")
_CardSystemSecondaryClockPortConfig_Type = Integer32
_CardSystemSecondaryClockPortConfig_Object = MibTableColumn
cardSystemSecondaryClockPortConfig = _CardSystemSecondaryClockPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 85),
    _CardSystemSecondaryClockPortConfig_Type()
)
cardSystemSecondaryClockPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSystemSecondaryClockPortConfig.setStatus("mandatory")


class _CardSystemSecondaryClockStatus_Type(Integer32):
    """Custom type cardSystemSecondaryClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 1))
    )


_CardSystemSecondaryClockStatus_Type.__name__ = "Integer32"
_CardSystemSecondaryClockStatus_Object = MibTableColumn
cardSystemSecondaryClockStatus = _CardSystemSecondaryClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 86),
    _CardSystemSecondaryClockStatus_Type()
)
cardSystemSecondaryClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSystemSecondaryClockStatus.setStatus("mandatory")
_CardInCells_Type = Counter32
_CardInCells_Object = MibTableColumn
cardInCells = _CardInCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 87),
    _CardInCells_Type()
)
cardInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInCells.setStatus("mandatory")
_CardInErrorCells_Type = Counter32
_CardInErrorCells_Object = MibTableColumn
cardInErrorCells = _CardInErrorCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 88),
    _CardInErrorCells_Type()
)
cardInErrorCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInErrorCells.setStatus("mandatory")
_CardInErrorVPIVCI_Type = Counter32
_CardInErrorVPIVCI_Object = MibTableColumn
cardInErrorVPIVCI = _CardInErrorVPIVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 89),
    _CardInErrorVPIVCI_Type()
)
cardInErrorVPIVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInErrorVPIVCI.setStatus("mandatory")
_CardOutCells_Type = Counter32
_CardOutCells_Object = MibTableColumn
cardOutCells = _CardOutCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 90),
    _CardOutCells_Type()
)
cardOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutCells.setStatus("mandatory")
_CardOutDiscardCells_Type = Counter32
_CardOutDiscardCells_Object = MibTableColumn
cardOutDiscardCells = _CardOutDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 91),
    _CardOutDiscardCells_Type()
)
cardOutDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutDiscardCells.setStatus("mandatory")


class _CardQOSQueueSize_Type(Integer32):
    """Custom type cardQOSQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cell-24K", 2),
          ("cell-8K", 1))
    )


_CardQOSQueueSize_Type.__name__ = "Integer32"
_CardQOSQueueSize_Object = MibTableColumn
cardQOSQueueSize = _CardQOSQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 92),
    _CardQOSQueueSize_Type()
)
cardQOSQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardQOSQueueSize.setStatus("mandatory")
_CardLastErrorPort_Type = Integer32
_CardLastErrorPort_Object = MibTableColumn
cardLastErrorPort = _CardLastErrorPort_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 93),
    _CardLastErrorPort_Type()
)
cardLastErrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastErrorPort.setStatus("mandatory")
_CardLastErrorVPI_Type = Integer32
_CardLastErrorVPI_Object = MibTableColumn
cardLastErrorVPI = _CardLastErrorVPI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 94),
    _CardLastErrorVPI_Type()
)
cardLastErrorVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastErrorVPI.setStatus("mandatory")
_CardLastErrorVCI_Type = Integer32
_CardLastErrorVCI_Object = MibTableColumn
cardLastErrorVCI = _CardLastErrorVCI_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 95),
    _CardLastErrorVCI_Type()
)
cardLastErrorVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastErrorVCI.setStatus("mandatory")


class _CardSystemPrimaryClockModeConfig_Type(Integer32):
    """Custom type cardSystemPrimaryClockModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line-rate", 1),
          ("plcp-mode", 2))
    )


_CardSystemPrimaryClockModeConfig_Type.__name__ = "Integer32"
_CardSystemPrimaryClockModeConfig_Object = MibTableColumn
cardSystemPrimaryClockModeConfig = _CardSystemPrimaryClockModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 96),
    _CardSystemPrimaryClockModeConfig_Type()
)
cardSystemPrimaryClockModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSystemPrimaryClockModeConfig.setStatus("mandatory")


class _CardSystemSecondaryClockModeConfig_Type(Integer32):
    """Custom type cardSystemSecondaryClockModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line-rate", 1),
          ("plcp-mode", 2))
    )


_CardSystemSecondaryClockModeConfig_Type.__name__ = "Integer32"
_CardSystemSecondaryClockModeConfig_Object = MibTableColumn
cardSystemSecondaryClockModeConfig = _CardSystemSecondaryClockModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 97),
    _CardSystemSecondaryClockModeConfig_Type()
)
cardSystemSecondaryClockModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSystemSecondaryClockModeConfig.setStatus("mandatory")


class _CardNFBDEStatus_Type(Integer32):
    """Custom type cardNFBDEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("not-cleared", 2))
    )


_CardNFBDEStatus_Type.__name__ = "Integer32"
_CardNFBDEStatus_Object = MibTableColumn
cardNFBDEStatus = _CardNFBDEStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 98),
    _CardNFBDEStatus_Type()
)
cardNFBDEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNFBDEStatus.setStatus("mandatory")
_CardProductCode_Type = DisplayString
_CardProductCode_Object = MibTableColumn
cardProductCode = _CardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 99),
    _CardProductCode_Type()
)
cardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProductCode.setStatus("mandatory")
_CardMfgPN_Type = DisplayString
_CardMfgPN_Object = MibTableColumn
cardMfgPN = _CardMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 100),
    _CardMfgPN_Type()
)
cardMfgPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMfgPN.setStatus("mandatory")
_CardTotalUpTime_Type = TimeTicks
_CardTotalUpTime_Object = MibTableColumn
cardTotalUpTime = _CardTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 101),
    _CardTotalUpTime_Type()
)
cardTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTotalUpTime.setStatus("mandatory")


class _CardIOAType_Type(Integer32):
    """Custom type cardIOAType based on Integer32"""
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("bCP-1-m", 56),
          ("bCP-1-o", 57),
          ("bCS-DS3-n-1", 35),
          ("bCS-DS3-r-1", 36),
          ("bCS-E3-n-1", 54),
          ("bCS-E3-r-1", 55),
          ("bIWU-OC3-bumm-1", 44),
          ("bIWU-OC3-bumm-smfir-1", 45),
          ("bIWU-OC3-mm-n-1", 37),
          ("bIWU-OC3-smfir-n-1", 38),
          ("bIWU-OC3-trm-mm-1", 46),
          ("bIWU-OC3-trm-smfir-1", 47),
          ("bds1-e1-bnc-n-12", 50),
          ("bds1-e1-bnc-r-12", 51),
          ("bds1-e1-db15-n-12", 52),
          ("bds1-e1-db15-r-12", 53),
          ("bds1-e1-rj48h-n-12", 64),
          ("bds1-e1-rj48h-r-12", 65),
          ("be1-atm-120-n-12", 60),
          ("be1-atm-120-r-12", 61),
          ("be1-atm-75-n-12", 58),
          ("be1-atm-75-r-12", 59),
          ("bio550-oc12-mmf", 75),
          ("bio550-oc12-smfir", 73),
          ("bio550-oc12-smflr", 74),
          ("bio550-oc3-mmf", 72),
          ("bio550-oc3-smfir", 70),
          ("bio550-oc3-smflr", 71),
          ("bstdx9000-ether-n-2", 69),
          ("bt1-atm-100-n-12", 62),
          ("bt1-atm-100-r-12", 63),
          ("cbx500-ds3-n-6", 68),
          ("cbx500-ether-n-4", 67),
          ("gx550-backplane", 66),
          ("hssi-n", 18),
          ("hssi-r", 19),
          ("npa-universal", 43),
          ("nplus1-chassis", 41),
          ("spa", 1),
          ("spa-universal", 32),
          ("tads1-e1-120-n-8", 26),
          ("tads1-e1-120-r-8", 27),
          ("tads1-e1-75-n-8", 24),
          ("tads1-e1-75-r-8", 25),
          ("tads1-j2-120-n-8", 30),
          ("tads1-j2-120-r-8", 31),
          ("tads1-j2-75-n-8", 28),
          ("tads1-j2-75-r-8", 29),
          ("tads1-t1-n-8", 22),
          ("tads1-t1-r-8", 23),
          ("tds3-8", 4),
          ("tds3-r-8", 16),
          ("te3-8", 5),
          ("te3-r-8", 17),
          ("toc12-smf-n-1", 21),
          ("toc12-smflr-n-1", 42),
          ("toc3-4", 2),
          ("toc3-mm-r-4", 8),
          ("toc3-smfir-n-4", 6),
          ("toc3-smfir-r-4", 7),
          ("toc3-smflr-n-4", 9),
          ("toc3-smflr-r-4", 10),
          ("toc3-stm1copper-n-4", 39),
          ("toc3-stm1copper-r-4", 40),
          ("tstm1-4", 3),
          ("tstm1-mm-r-4", 13),
          ("tstm1-smfir-n-4", 11),
          ("tstm1-smfir-r-4", 12),
          ("tstm1-smflr-n-4", 14),
          ("tstm1-smflr-r-4", 15),
          ("uio-v35", 48),
          ("uio-x21", 49))
    )


_CardIOAType_Type.__name__ = "Integer32"
_CardIOAType_Object = MibTableColumn
cardIOAType = _CardIOAType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 102),
    _CardIOAType_Type()
)
cardIOAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIOAType.setStatus("mandatory")
_CardIOAHwRev_Type = DisplayString
_CardIOAHwRev_Object = MibTableColumn
cardIOAHwRev = _CardIOAHwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 103),
    _CardIOAHwRev_Type()
)
cardIOAHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIOAHwRev.setStatus("mandatory")
_CardIOASerial_Type = DisplayString
_CardIOASerial_Object = MibTableColumn
cardIOASerial = _CardIOASerial_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 104),
    _CardIOASerial_Type()
)
cardIOASerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIOASerial.setStatus("mandatory")
_CardIOAProductCode_Type = DisplayString
_CardIOAProductCode_Object = MibTableColumn
cardIOAProductCode = _CardIOAProductCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 105),
    _CardIOAProductCode_Type()
)
cardIOAProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIOAProductCode.setStatus("mandatory")
_CardIOAMfgPN_Type = DisplayString
_CardIOAMfgPN_Object = MibTableColumn
cardIOAMfgPN = _CardIOAMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 106),
    _CardIOAMfgPN_Type()
)
cardIOAMfgPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIOAMfgPN.setStatus("mandatory")


class _CardDS0Support_Type(Integer32):
    """Custom type cardDS0Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0-lpbk-not-supported", 1),
          ("ds0-lpbk-supported", 2))
    )


_CardDS0Support_Type.__name__ = "Integer32"
_CardDS0Support_Object = MibTableColumn
cardDS0Support = _CardDS0Support_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 107),
    _CardDS0Support_Type()
)
cardDS0Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDS0Support.setStatus("mandatory")
_CardDiagParamId_Type = Integer32
_CardDiagParamId_Object = MibTableColumn
cardDiagParamId = _CardDiagParamId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 108),
    _CardDiagParamId_Type()
)
cardDiagParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagParamId.setStatus("mandatory")
_CardDiagParamValue_Type = Integer32
_CardDiagParamValue_Object = MibTableColumn
cardDiagParamValue = _CardDiagParamValue_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 109),
    _CardDiagParamValue_Type()
)
cardDiagParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDiagParamValue.setStatus("mandatory")


class _CardBulkStatsPeakCapability_Type(Integer32):
    """Custom type cardBulkStatsPeakCapability based on Integer32"""
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


_CardBulkStatsPeakCapability_Type.__name__ = "Integer32"
_CardBulkStatsPeakCapability_Object = MibTableColumn
cardBulkStatsPeakCapability = _CardBulkStatsPeakCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 110),
    _CardBulkStatsPeakCapability_Type()
)
cardBulkStatsPeakCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBulkStatsPeakCapability.setStatus("mandatory")


class _CardBulkStatsTotalCapability_Type(Integer32):
    """Custom type cardBulkStatsTotalCapability based on Integer32"""
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


_CardBulkStatsTotalCapability_Type.__name__ = "Integer32"
_CardBulkStatsTotalCapability_Object = MibTableColumn
cardBulkStatsTotalCapability = _CardBulkStatsTotalCapability_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 111),
    _CardBulkStatsTotalCapability_Type()
)
cardBulkStatsTotalCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBulkStatsTotalCapability.setStatus("mandatory")


class _CardBulkStatsPeakEnable_Type(Integer32):
    """Custom type cardBulkStatsPeakEnable based on Integer32"""
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


_CardBulkStatsPeakEnable_Type.__name__ = "Integer32"
_CardBulkStatsPeakEnable_Object = MibTableColumn
cardBulkStatsPeakEnable = _CardBulkStatsPeakEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 112),
    _CardBulkStatsPeakEnable_Type()
)
cardBulkStatsPeakEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBulkStatsPeakEnable.setStatus("mandatory")


class _CardBulkStatsTotalEnable_Type(Integer32):
    """Custom type cardBulkStatsTotalEnable based on Integer32"""
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


_CardBulkStatsTotalEnable_Type.__name__ = "Integer32"
_CardBulkStatsTotalEnable_Object = MibTableColumn
cardBulkStatsTotalEnable = _CardBulkStatsTotalEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 113),
    _CardBulkStatsTotalEnable_Type()
)
cardBulkStatsTotalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBulkStatsTotalEnable.setStatus("mandatory")


class _CardBulkStatsBaseCollectPeriod_Type(Integer32):
    """Custom type cardBulkStatsBaseCollectPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_CardBulkStatsBaseCollectPeriod_Type.__name__ = "Integer32"
_CardBulkStatsBaseCollectPeriod_Object = MibTableColumn
cardBulkStatsBaseCollectPeriod = _CardBulkStatsBaseCollectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 114),
    _CardBulkStatsBaseCollectPeriod_Type()
)
cardBulkStatsBaseCollectPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBulkStatsBaseCollectPeriod.setStatus("mandatory")
_CardNrtsHwRev_Type = Integer32
_CardNrtsHwRev_Object = MibTableColumn
cardNrtsHwRev = _CardNrtsHwRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 115),
    _CardNrtsHwRev_Type()
)
cardNrtsHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNrtsHwRev.setStatus("mandatory")
_CardNrtsOutCellBufSize_Type = Integer32
_CardNrtsOutCellBufSize_Object = MibTableColumn
cardNrtsOutCellBufSize = _CardNrtsOutCellBufSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 116),
    _CardNrtsOutCellBufSize_Type()
)
cardNrtsOutCellBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNrtsOutCellBufSize.setStatus("mandatory")


class _CardNrtsOperState_Type(Integer32):
    """Custom type cardNrtsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("down", 2),
          ("up", 3))
    )


_CardNrtsOperState_Type.__name__ = "Integer32"
_CardNrtsOperState_Object = MibTableColumn
cardNrtsOperState = _CardNrtsOperState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 117),
    _CardNrtsOperState_Type()
)
cardNrtsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNrtsOperState.setStatus("mandatory")


class _CardNrtsAdminState_Type(Integer32):
    """Custom type cardNrtsAdminState based on Integer32"""
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


_CardNrtsAdminState_Type.__name__ = "Integer32"
_CardNrtsAdminState_Object = MibTableColumn
cardNrtsAdminState = _CardNrtsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 118),
    _CardNrtsAdminState_Type()
)
cardNrtsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsAdminState.setStatus("mandatory")
_CardNrtsCcrmProtocolId_Type = Integer32
_CardNrtsCcrmProtocolId_Object = MibTableColumn
cardNrtsCcrmProtocolId = _CardNrtsCcrmProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 119),
    _CardNrtsCcrmProtocolId_Type()
)
cardNrtsCcrmProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsCcrmProtocolId.setStatus("mandatory")
_CardNrtsBcmProtocolId_Type = Integer32
_CardNrtsBcmProtocolId_Object = MibTableColumn
cardNrtsBcmProtocolId = _CardNrtsBcmProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 120),
    _CardNrtsBcmProtocolId_Type()
)
cardNrtsBcmProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsBcmProtocolId.setStatus("mandatory")
_CardNrtsRmGenInterval_Type = Integer32
_CardNrtsRmGenInterval_Object = MibTableColumn
cardNrtsRmGenInterval = _CardNrtsRmGenInterval_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 121),
    _CardNrtsRmGenInterval_Type()
)
cardNrtsRmGenInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsRmGenInterval.setStatus("mandatory")
_CardNrtsIdleCktThresh_Type = Integer32
_CardNrtsIdleCktThresh_Object = MibTableColumn
cardNrtsIdleCktThresh = _CardNrtsIdleCktThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 122),
    _CardNrtsIdleCktThresh_Type()
)
cardNrtsIdleCktThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsIdleCktThresh.setStatus("mandatory")


class _CardNrtsVbrNrtManage_Type(Integer32):
    """Custom type cardNrtsVbrNrtManage based on Integer32"""
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


_CardNrtsVbrNrtManage_Type.__name__ = "Integer32"
_CardNrtsVbrNrtManage_Object = MibTableColumn
cardNrtsVbrNrtManage = _CardNrtsVbrNrtManage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 123),
    _CardNrtsVbrNrtManage_Type()
)
cardNrtsVbrNrtManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsVbrNrtManage.setStatus("mandatory")
_CardNrtsIcrFact_Type = Integer32
_CardNrtsIcrFact_Object = MibTableColumn
cardNrtsIcrFact = _CardNrtsIcrFact_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 124),
    _CardNrtsIcrFact_Type()
)
cardNrtsIcrFact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsIcrFact.setStatus("mandatory")
_CardNrtsMcastDiscardThresh_Type = Integer32
_CardNrtsMcastDiscardThresh_Object = MibTableColumn
cardNrtsMcastDiscardThresh = _CardNrtsMcastDiscardThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 125),
    _CardNrtsMcastDiscardThresh_Type()
)
cardNrtsMcastDiscardThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsMcastDiscardThresh.setStatus("mandatory")
_CardNrtsMcastDiscardCount_Type = Counter32
_CardNrtsMcastDiscardCount_Object = MibTableColumn
cardNrtsMcastDiscardCount = _CardNrtsMcastDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 126),
    _CardNrtsMcastDiscardCount_Type()
)
cardNrtsMcastDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNrtsMcastDiscardCount.setStatus("mandatory")


class _CardAdminIOAType_Type(Integer32):
    """Custom type cardAdminIOAType based on Integer32"""
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("bCP-1-m", 56),
          ("bCP-1-o", 57),
          ("bCS-DS3-n-1", 35),
          ("bCS-DS3-r-1", 36),
          ("bCS-E3-n-1", 54),
          ("bCS-E3-r-1", 55),
          ("bIWU-OC3-bumm-1", 44),
          ("bIWU-OC3-bumm-smfir-1", 45),
          ("bIWU-OC3-mm-n-1", 37),
          ("bIWU-OC3-smfir-n-1", 38),
          ("bIWU-OC3-trm-mm-1", 46),
          ("bIWU-OC3-trm-smfir-1", 47),
          ("bds1-e1-bnc-n-12", 50),
          ("bds1-e1-bnc-r-12", 51),
          ("bds1-e1-db15-n-12", 52),
          ("bds1-e1-db15-r-12", 53),
          ("bds1-e1-rj48h-n-12", 64),
          ("bds1-e1-rj48h-r-12", 65),
          ("be1-atm-120-n-12", 60),
          ("be1-atm-120-r-12", 61),
          ("be1-atm-75-n-12", 58),
          ("be1-atm-75-r-12", 59),
          ("bio550-oc12-mmf", 75),
          ("bio550-oc12-smfir", 73),
          ("bio550-oc12-smflr", 74),
          ("bio550-oc3-mmf", 72),
          ("bio550-oc3-smfir", 70),
          ("bio550-oc3-smflr", 71),
          ("bstdx9000-ether-n-2", 69),
          ("bt1-atm-100-n-12", 62),
          ("bt1-atm-100-r-12", 63),
          ("cbx500-ds3-n-6", 68),
          ("cbx500-ether-n-4", 67),
          ("hssi-n", 18),
          ("hssi-r", 19),
          ("npa-universal", 43),
          ("nplus1-chassis", 41),
          ("spa", 1),
          ("spa-universal", 32),
          ("tads1-e1-120-n-8", 26),
          ("tads1-e1-120-r-8", 27),
          ("tads1-e1-75-n-8", 24),
          ("tads1-e1-75-r-8", 25),
          ("tads1-j2-120-n-8", 30),
          ("tads1-j2-120-r-8", 31),
          ("tads1-j2-75-n-8", 28),
          ("tads1-j2-75-r-8", 29),
          ("tads1-t1-n-8", 22),
          ("tads1-t1-r-8", 23),
          ("tds3-8", 4),
          ("tds3-r-8", 16),
          ("te3-8", 5),
          ("te3-r-8", 17),
          ("toc12-smf-n-1", 21),
          ("toc12-smflr-n-1", 42),
          ("toc3-4", 2),
          ("toc3-mm-r-4", 8),
          ("toc3-smfir-n-4", 6),
          ("toc3-smfir-r-4", 7),
          ("toc3-smflr-n-4", 9),
          ("toc3-smflr-r-4", 10),
          ("toc3-stm1copper-n-4", 39),
          ("toc3-stm1copper-r-4", 40),
          ("tstm1-4", 3),
          ("tstm1-mm-r-4", 13),
          ("tstm1-smfir-n-4", 11),
          ("tstm1-smfir-r-4", 12),
          ("tstm1-smflr-n-4", 14),
          ("tstm1-smflr-r-4", 15),
          ("uio-v35", 48),
          ("uio-x21", 49))
    )


_CardAdminIOAType_Type.__name__ = "Integer32"
_CardAdminIOAType_Object = MibTableColumn
cardAdminIOAType = _CardAdminIOAType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 127),
    _CardAdminIOAType_Type()
)
cardAdminIOAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminIOAType.setStatus("mandatory")
_CardNrtsMcastRate_Type = Integer32
_CardNrtsMcastRate_Object = MibTableColumn
cardNrtsMcastRate = _CardNrtsMcastRate_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 128),
    _CardNrtsMcastRate_Type()
)
cardNrtsMcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardNrtsMcastRate.setStatus("mandatory")


class _CardMonStatus_Type(Integer32):
    """Custom type cardMonStatus based on Integer32"""
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


_CardMonStatus_Type.__name__ = "Integer32"
_CardMonStatus_Object = MibTableColumn
cardMonStatus = _CardMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 129),
    _CardMonStatus_Type()
)
cardMonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardMonStatus.setStatus("mandatory")
_CardImageSetA_Type = DisplayString
_CardImageSetA_Object = MibTableColumn
cardImageSetA = _CardImageSetA_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 130),
    _CardImageSetA_Type()
)
cardImageSetA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardImageSetA.setStatus("mandatory")
_CardImageSetB_Type = DisplayString
_CardImageSetB_Object = MibTableColumn
cardImageSetB = _CardImageSetB_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 131),
    _CardImageSetB_Type()
)
cardImageSetB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardImageSetB.setStatus("mandatory")
_CardMacAddress_Type = DisplayString
_CardMacAddress_Object = MibTableColumn
cardMacAddress = _CardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 132),
    _CardMacAddress_Type()
)
cardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMacAddress.setStatus("mandatory")
_CardFlashRev_Type = DisplayString
_CardFlashRev_Object = MibTableColumn
cardFlashRev = _CardFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 133),
    _CardFlashRev_Type()
)
cardFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFlashRev.setStatus("mandatory")


class _CardRequiredCapabilityBitmask_Type(Integer32):
    """Custom type cardRequiredCapabilityBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aps-one-plus-one-support", 1),
          ("fe-capability", 8),
          ("holdover-support", 2),
          ("vp-shaping", 4))
    )


_CardRequiredCapabilityBitmask_Type.__name__ = "Integer32"
_CardRequiredCapabilityBitmask_Object = MibTableColumn
cardRequiredCapabilityBitmask = _CardRequiredCapabilityBitmask_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 134),
    _CardRequiredCapabilityBitmask_Type()
)
cardRequiredCapabilityBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRequiredCapabilityBitmask.setStatus("mandatory")


class _CardOperCapabilityBitmask_Type(Integer32):
    """Custom type cardOperCapabilityBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aps-one-plus-one-supported", 1),
          ("fe-capability", 8),
          ("holdover-supported", 2),
          ("vp-shaping", 4))
    )


_CardOperCapabilityBitmask_Type.__name__ = "Integer32"
_CardOperCapabilityBitmask_Object = MibTableColumn
cardOperCapabilityBitmask = _CardOperCapabilityBitmask_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 135),
    _CardOperCapabilityBitmask_Type()
)
cardOperCapabilityBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperCapabilityBitmask.setStatus("mandatory")
_CardDslModule_Type = OctetString
_CardDslModule_Object = MibTableColumn
cardDslModule = _CardDslModule_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 136),
    _CardDslModule_Type()
)
cardDslModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardDslModule.setStatus("mandatory")
_CardIPTableSize_Type = Integer32
_CardIPTableSize_Object = MibTableColumn
cardIPTableSize = _CardIPTableSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 137),
    _CardIPTableSize_Type()
)
cardIPTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardIPTableSize.setStatus("mandatory")


class _CardIPTableState_Type(Integer32):
    """Custom type cardIPTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("marginal", 2),
          ("normal", 1))
    )


_CardIPTableState_Type.__name__ = "Integer32"
_CardIPTableState_Object = MibTableColumn
cardIPTableState = _CardIPTableState_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 138),
    _CardIPTableState_Type()
)
cardIPTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIPTableState.setStatus("mandatory")


class _CardATMTcaInBufOverflowAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaInBufOverflowAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaInBufOverflowAlertPeriod_Object = MibTableColumn
cardATMTcaInBufOverflowAlertPeriod = _CardATMTcaInBufOverflowAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 139),
    _CardATMTcaInBufOverflowAlertPeriod_Type()
)
cardATMTcaInBufOverflowAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInBufOverflowAlertPeriod.setStatus("mandatory")


class _CardATMTcaInBufOverflowThresh_Type(Integer32):
    """Custom type cardATMTcaInBufOverflowThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaInBufOverflowThresh_Object = MibTableColumn
cardATMTcaInBufOverflowThresh = _CardATMTcaInBufOverflowThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 140),
    _CardATMTcaInBufOverflowThresh_Type()
)
cardATMTcaInBufOverflowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInBufOverflowThresh.setStatus("mandatory")


class _CardATMTcaInInvalidVpiVciAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaInInvalidVpiVciAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaInInvalidVpiVciAlertPeriod_Object = MibTableColumn
cardATMTcaInInvalidVpiVciAlertPeriod = _CardATMTcaInInvalidVpiVciAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 141),
    _CardATMTcaInInvalidVpiVciAlertPeriod_Type()
)
cardATMTcaInInvalidVpiVciAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInInvalidVpiVciAlertPeriod.setStatus("mandatory")


class _CardATMTcaInInvalidVpiVciThresh_Type(Integer32):
    """Custom type cardATMTcaInInvalidVpiVciThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaInInvalidVpiVciThresh_Object = MibTableColumn
cardATMTcaInInvalidVpiVciThresh = _CardATMTcaInInvalidVpiVciThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 142),
    _CardATMTcaInInvalidVpiVciThresh_Type()
)
cardATMTcaInInvalidVpiVciThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInInvalidVpiVciThresh.setStatus("mandatory")


class _CardATMTcaInATMDCFullAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaInATMDCFullAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaInATMDCFullAlertPeriod_Object = MibTableColumn
cardATMTcaInATMDCFullAlertPeriod = _CardATMTcaInATMDCFullAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 143),
    _CardATMTcaInATMDCFullAlertPeriod_Type()
)
cardATMTcaInATMDCFullAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInATMDCFullAlertPeriod.setStatus("mandatory")


class _CardATMTcaInATMDCFullThresh_Type(Integer32):
    """Custom type cardATMTcaInATMDCFullThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaInATMDCFullThresh_Object = MibTableColumn
cardATMTcaInATMDCFullThresh = _CardATMTcaInATMDCFullThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 144),
    _CardATMTcaInATMDCFullThresh_Type()
)
cardATMTcaInATMDCFullThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaInATMDCFullThresh.setStatus("mandatory")


class _CardATMTcaEnable_Type(Integer32):
    """Custom type cardATMTcaEnable based on Integer32"""
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


_CardATMTcaEnable_Type.__name__ = "Integer32"
_CardATMTcaEnable_Object = MibTableColumn
cardATMTcaEnable = _CardATMTcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 145),
    _CardATMTcaEnable_Type()
)
cardATMTcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaEnable.setStatus("mandatory")


class _CardATMTcaId_Type(Integer32):
    """Custom type cardATMTcaId based on Integer32"""
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
        *(("egressCidLookupFailureC", 7),
          ("ingressATMDCFullC", 3),
          ("ingressBufferHalfC", 5),
          ("ingressBufferMsbPaeC", 4),
          ("ingressBufferMsbPafC", 6),
          ("ingressBufferOverfloeC", 1),
          ("ingressInvalidVpiVciC", 2))
    )


_CardATMTcaId_Type.__name__ = "Integer32"
_CardATMTcaId_Object = MibTableColumn
cardATMTcaId = _CardATMTcaId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 146),
    _CardATMTcaId_Type()
)
cardATMTcaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardATMTcaId.setStatus("mandatory")


class _CardATMTcaECidLookupFailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaECidLookupFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaECidLookupFailureAlertPeriod_Object = MibTableColumn
cardATMTcaECidLookupFailureAlertPeriod = _CardATMTcaECidLookupFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 147),
    _CardATMTcaECidLookupFailureAlertPeriod_Type()
)
cardATMTcaECidLookupFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaECidLookupFailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaECidLookupThresh_Type(Integer32):
    """Custom type cardATMTcaECidLookupThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaECidLookupThresh_Object = MibTableColumn
cardATMTcaECidLookupThresh = _CardATMTcaECidLookupThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 148),
    _CardATMTcaECidLookupThresh_Type()
)
cardATMTcaECidLookupThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaECidLookupThresh.setStatus("mandatory")


class _CardATMTcaSPPearlOCbrFailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlOCbrFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlOCbrFailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlOCbrFailureAlertPeriod = _CardATMTcaSPPearlOCbrFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 149),
    _CardATMTcaSPPearlOCbrFailureAlertPeriod_Type()
)
cardATMTcaSPPearlOCbrFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOCbrFailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlOCbrThresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlOCbrThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlOCbrThresh_Object = MibTableColumn
cardATMTcaSPPearlOCbrThresh = _CardATMTcaSPPearlOCbrThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 150),
    _CardATMTcaSPPearlOCbrThresh_Type()
)
cardATMTcaSPPearlOCbrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOCbrThresh.setStatus("mandatory")


class _CardATMTcaSPPearlOAbrFailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlOAbrFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlOAbrFailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlOAbrFailureAlertPeriod = _CardATMTcaSPPearlOAbrFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 151),
    _CardATMTcaSPPearlOAbrFailureAlertPeriod_Type()
)
cardATMTcaSPPearlOAbrFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOAbrFailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlOAbrThresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlOAbrThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlOAbrThresh_Object = MibTableColumn
cardATMTcaSPPearlOAbrThresh = _CardATMTcaSPPearlOAbrThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 152),
    _CardATMTcaSPPearlOAbrThresh_Type()
)
cardATMTcaSPPearlOAbrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOAbrThresh.setStatus("mandatory")


class _CardATMTcaSPPearlOVbr1FailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlOVbr1FailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlOVbr1FailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlOVbr1FailureAlertPeriod = _CardATMTcaSPPearlOVbr1FailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 153),
    _CardATMTcaSPPearlOVbr1FailureAlertPeriod_Type()
)
cardATMTcaSPPearlOVbr1FailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOVbr1FailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlOVbr1Thresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlOVbr1Thresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlOVbr1Thresh_Object = MibTableColumn
cardATMTcaSPPearlOVbr1Thresh = _CardATMTcaSPPearlOVbr1Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 154),
    _CardATMTcaSPPearlOVbr1Thresh_Type()
)
cardATMTcaSPPearlOVbr1Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOVbr1Thresh.setStatus("mandatory")


class _CardATMTcaSPPearlOVbr2FailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlOVbr2FailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlOVbr2FailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlOVbr2FailureAlertPeriod = _CardATMTcaSPPearlOVbr2FailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 155),
    _CardATMTcaSPPearlOVbr2FailureAlertPeriod_Type()
)
cardATMTcaSPPearlOVbr2FailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOVbr2FailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlOVbr2Thresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlOVbr2Thresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlOVbr2Thresh_Object = MibTableColumn
cardATMTcaSPPearlOVbr2Thresh = _CardATMTcaSPPearlOVbr2Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 156),
    _CardATMTcaSPPearlOVbr2Thresh_Type()
)
cardATMTcaSPPearlOVbr2Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlOVbr2Thresh.setStatus("mandatory")


class _CardATMTcaSPPearlGCbrFailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlGCbrFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlGCbrFailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlGCbrFailureAlertPeriod = _CardATMTcaSPPearlGCbrFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 157),
    _CardATMTcaSPPearlGCbrFailureAlertPeriod_Type()
)
cardATMTcaSPPearlGCbrFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGCbrFailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlGCbrThresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlGCbrThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlGCbrThresh_Object = MibTableColumn
cardATMTcaSPPearlGCbrThresh = _CardATMTcaSPPearlGCbrThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 158),
    _CardATMTcaSPPearlGCbrThresh_Type()
)
cardATMTcaSPPearlGCbrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGCbrThresh.setStatus("mandatory")


class _CardATMTcaSPPearlGAbrFailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlGAbrFailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlGAbrFailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlGAbrFailureAlertPeriod = _CardATMTcaSPPearlGAbrFailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 159),
    _CardATMTcaSPPearlGAbrFailureAlertPeriod_Type()
)
cardATMTcaSPPearlGAbrFailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGAbrFailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlGAbrThresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlGAbrThresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlGAbrThresh_Object = MibTableColumn
cardATMTcaSPPearlGAbrThresh = _CardATMTcaSPPearlGAbrThresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 160),
    _CardATMTcaSPPearlGAbrThresh_Type()
)
cardATMTcaSPPearlGAbrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGAbrThresh.setStatus("mandatory")


class _CardATMTcaSPPearlGVbr1FailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlGVbr1FailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlGVbr1FailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlGVbr1FailureAlertPeriod = _CardATMTcaSPPearlGVbr1FailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 161),
    _CardATMTcaSPPearlGVbr1FailureAlertPeriod_Type()
)
cardATMTcaSPPearlGVbr1FailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGVbr1FailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlGVbr1Thresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlGVbr1Thresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlGVbr1Thresh_Object = MibTableColumn
cardATMTcaSPPearlGVbr1Thresh = _CardATMTcaSPPearlGVbr1Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 162),
    _CardATMTcaSPPearlGVbr1Thresh_Type()
)
cardATMTcaSPPearlGVbr1Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGVbr1Thresh.setStatus("mandatory")


class _CardATMTcaSPPearlGVbr2FailureAlertPeriod_Type(Integer32):
    """Custom type cardATMTcaSPPearlGVbr2FailureAlertPeriod based on Integer32"""
    defaultValue = 15


_CardATMTcaSPPearlGVbr2FailureAlertPeriod_Object = MibTableColumn
cardATMTcaSPPearlGVbr2FailureAlertPeriod = _CardATMTcaSPPearlGVbr2FailureAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 163),
    _CardATMTcaSPPearlGVbr2FailureAlertPeriod_Type()
)
cardATMTcaSPPearlGVbr2FailureAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGVbr2FailureAlertPeriod.setStatus("mandatory")


class _CardATMTcaSPPearlGVbr2Thresh_Type(Integer32):
    """Custom type cardATMTcaSPPearlGVbr2Thresh based on Integer32"""
    defaultValue = 1


_CardATMTcaSPPearlGVbr2Thresh_Object = MibTableColumn
cardATMTcaSPPearlGVbr2Thresh = _CardATMTcaSPPearlGVbr2Thresh_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 164),
    _CardATMTcaSPPearlGVbr2Thresh_Type()
)
cardATMTcaSPPearlGVbr2Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPPearlGVbr2Thresh.setStatus("mandatory")


class _CardATMTcaSPEnable_Type(Integer32):
    """Custom type cardATMTcaSPEnable based on Integer32"""
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


_CardATMTcaSPEnable_Type.__name__ = "Integer32"
_CardATMTcaSPEnable_Object = MibTableColumn
cardATMTcaSPEnable = _CardATMTcaSPEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 165),
    _CardATMTcaSPEnable_Type()
)
cardATMTcaSPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardATMTcaSPEnable.setStatus("mandatory")


class _CardSPEFCIEnable_Type(Integer32):
    """Custom type cardSPEFCIEnable based on Integer32"""
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


_CardSPEFCIEnable_Type.__name__ = "Integer32"
_CardSPEFCIEnable_Object = MibTableColumn
cardSPEFCIEnable = _CardSPEFCIEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 166),
    _CardSPEFCIEnable_Type()
)
cardSPEFCIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSPEFCIEnable.setStatus("mandatory")


class _CardSPClpEnable_Type(Integer32):
    """Custom type cardSPClpEnable based on Integer32"""
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


_CardSPClpEnable_Type.__name__ = "Integer32"
_CardSPClpEnable_Object = MibTableColumn
cardSPClpEnable = _CardSPClpEnable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 167),
    _CardSPClpEnable_Type()
)
cardSPClpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSPClpEnable.setStatus("mandatory")


class _SpATMTcaId_Type(Integer32):
    """Custom type spATMTcaId based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("spBufferCongestionA1", 11),
          ("spBufferCongestionA2", 12),
          ("spBufferCongestionC1", 9),
          ("spBufferCongestionC2", 10),
          ("spBufferCongestionV11", 13),
          ("spBufferCongestionV12", 14),
          ("spBufferCongestionV21", 15),
          ("spBufferCongestionV22", 16),
          ("spBufferOverflowA1", 3),
          ("spBufferOverflowA2", 4),
          ("spBufferOverflowC1", 1),
          ("spBufferOverflowC2", 2),
          ("spBufferOverflowV11", 5),
          ("spBufferOverflowV12", 6),
          ("spBufferOverflowV21", 7),
          ("spBufferOverflowV22", 8))
    )


_SpATMTcaId_Type.__name__ = "Integer32"
_SpATMTcaId_Object = MibTableColumn
spATMTcaId = _SpATMTcaId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 168),
    _SpATMTcaId_Type()
)
spATMTcaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spATMTcaId.setStatus("mandatory")
_CardSubcardToRedundant_Type = CardTypes
_CardSubcardToRedundant_Object = MibTableColumn
cardSubcardToRedundant = _CardSubcardToRedundant_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 169),
    _CardSubcardToRedundant_Type()
)
cardSubcardToRedundant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSubcardToRedundant.setStatus("mandatory")
_CardMemory5Usage_Type = Gauge32
_CardMemory5Usage_Object = MibTableColumn
cardMemory5Usage = _CardMemory5Usage_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 170),
    _CardMemory5Usage_Type()
)
cardMemory5Usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMemory5Usage.setStatus("mandatory")
_CardSF1OperStatus_Type = CardStatuses
_CardSF1OperStatus_Object = MibTableColumn
cardSF1OperStatus = _CardSF1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 171),
    _CardSF1OperStatus_Type()
)
cardSF1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSF1OperStatus.setStatus("mandatory")
_CardSF2OperStatus_Type = CardStatuses
_CardSF2OperStatus_Object = MibTableColumn
cardSF2OperStatus = _CardSF2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 172),
    _CardSF2OperStatus_Type()
)
cardSF2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSF2OperStatus.setStatus("mandatory")
_CardTM1OperStatus_Type = CardStatuses
_CardTM1OperStatus_Object = MibTableColumn
cardTM1OperStatus = _CardTM1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 173),
    _CardTM1OperStatus_Type()
)
cardTM1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTM1OperStatus.setStatus("mandatory")
_CardTM2OperStatus_Type = CardStatuses
_CardTM2OperStatus_Object = MibTableColumn
cardTM2OperStatus = _CardTM2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 174),
    _CardTM2OperStatus_Type()
)
cardTM2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTM2OperStatus.setStatus("mandatory")


class _CardMemStartLog_Type(Integer32):
    """Custom type cardMemStartLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_CardMemStartLog_Type.__name__ = "Integer32"
_CardMemStartLog_Object = MibTableColumn
cardMemStartLog = _CardMemStartLog_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 175),
    _CardMemStartLog_Type()
)
cardMemStartLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardMemStartLog.setStatus("mandatory")
_CardMemLogLevel_Type = Integer32
_CardMemLogLevel_Object = MibTableColumn
cardMemLogLevel = _CardMemLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 176),
    _CardMemLogLevel_Type()
)
cardMemLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardMemLogLevel.setStatus("mandatory")


class _CardMemClrLog_Type(Integer32):
    """Custom type cardMemClrLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_CardMemClrLog_Type.__name__ = "Integer32"
_CardMemClrLog_Object = MibTableColumn
cardMemClrLog = _CardMemClrLog_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 177),
    _CardMemClrLog_Type()
)
cardMemClrLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardMemClrLog.setStatus("mandatory")
_CardValidSubcards_Type = Integer32
_CardValidSubcards_Object = MibTableColumn
cardValidSubcards = _CardValidSubcards_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 178),
    _CardValidSubcards_Type()
)
cardValidSubcards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardValidSubcards.setStatus("mandatory")
_CardClp0CbrThreshold_Type = Integer32
_CardClp0CbrThreshold_Object = MibTableColumn
cardClp0CbrThreshold = _CardClp0CbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 179),
    _CardClp0CbrThreshold_Type()
)
cardClp0CbrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp0CbrThreshold.setStatus("mandatory")
_CardClp01CbrThreshold_Type = Integer32
_CardClp01CbrThreshold_Object = MibTableColumn
cardClp01CbrThreshold = _CardClp01CbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 180),
    _CardClp01CbrThreshold_Type()
)
cardClp01CbrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp01CbrThreshold.setStatus("mandatory")
_CardClp0VbrRtThreshold_Type = Integer32
_CardClp0VbrRtThreshold_Object = MibTableColumn
cardClp0VbrRtThreshold = _CardClp0VbrRtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 181),
    _CardClp0VbrRtThreshold_Type()
)
cardClp0VbrRtThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp0VbrRtThreshold.setStatus("mandatory")
_CardClp01VbrRtThreshold_Type = Integer32
_CardClp01VbrRtThreshold_Object = MibTableColumn
cardClp01VbrRtThreshold = _CardClp01VbrRtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 182),
    _CardClp01VbrRtThreshold_Type()
)
cardClp01VbrRtThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp01VbrRtThreshold.setStatus("mandatory")
_CardClp0VbrNrtThreshold_Type = Integer32
_CardClp0VbrNrtThreshold_Object = MibTableColumn
cardClp0VbrNrtThreshold = _CardClp0VbrNrtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 183),
    _CardClp0VbrNrtThreshold_Type()
)
cardClp0VbrNrtThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp0VbrNrtThreshold.setStatus("mandatory")
_CardClp01VbrNrtThreshold_Type = Integer32
_CardClp01VbrNrtThreshold_Object = MibTableColumn
cardClp01VbrNrtThreshold = _CardClp01VbrNrtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 184),
    _CardClp01VbrNrtThreshold_Type()
)
cardClp01VbrNrtThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp01VbrNrtThreshold.setStatus("mandatory")
_CardClp0UAbrThreshold_Type = Integer32
_CardClp0UAbrThreshold_Object = MibTableColumn
cardClp0UAbrThreshold = _CardClp0UAbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 185),
    _CardClp0UAbrThreshold_Type()
)
cardClp0UAbrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp0UAbrThreshold.setStatus("mandatory")
_CardClp01UAbrThreshold_Type = Integer32
_CardClp01UAbrThreshold_Object = MibTableColumn
cardClp01UAbrThreshold = _CardClp01UAbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 186),
    _CardClp01UAbrThreshold_Type()
)
cardClp01UAbrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardClp01UAbrThreshold.setStatus("mandatory")
_CardControlMessagesFromBus_Type = Counter32
_CardControlMessagesFromBus_Object = MibTableColumn
cardControlMessagesFromBus = _CardControlMessagesFromBus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 187),
    _CardControlMessagesFromBus_Type()
)
cardControlMessagesFromBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardControlMessagesFromBus.setStatus("mandatory")
_CardControlMessagesToBus_Type = Counter32
_CardControlMessagesToBus_Object = MibTableColumn
cardControlMessagesToBus = _CardControlMessagesToBus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 188),
    _CardControlMessagesToBus_Type()
)
cardControlMessagesToBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardControlMessagesToBus.setStatus("mandatory")
_CardBTUsFromBus_Type = Counter32
_CardBTUsFromBus_Object = MibTableColumn
cardBTUsFromBus = _CardBTUsFromBus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 189),
    _CardBTUsFromBus_Type()
)
cardBTUsFromBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsFromBus.setStatus("mandatory")
_CardBTUsToBus_Type = Counter32
_CardBTUsToBus_Object = MibTableColumn
cardBTUsToBus = _CardBTUsToBus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 190),
    _CardBTUsToBus_Type()
)
cardBTUsToBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsToBus.setStatus("mandatory")
_CardInvalidPvcBTUs_Type = Counter32
_CardInvalidPvcBTUs_Object = MibTableColumn
cardInvalidPvcBTUs = _CardInvalidPvcBTUs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 191),
    _CardInvalidPvcBTUs_Type()
)
cardInvalidPvcBTUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardInvalidPvcBTUs.setStatus("mandatory")
_CardIncompleteFramesFromBus_Type = Counter32
_CardIncompleteFramesFromBus_Object = MibTableColumn
cardIncompleteFramesFromBus = _CardIncompleteFramesFromBus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 192),
    _CardIncompleteFramesFromBus_Type()
)
cardIncompleteFramesFromBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardIncompleteFramesFromBus.setStatus("mandatory")
_CardBTUsBusErrors_Type = Counter32
_CardBTUsBusErrors_Object = MibTableColumn
cardBTUsBusErrors = _CardBTUsBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 193),
    _CardBTUsBusErrors_Type()
)
cardBTUsBusErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsBusErrors.setStatus("mandatory")
_CardBTUsNoResource_Type = Counter32
_CardBTUsNoResource_Object = MibTableColumn
cardBTUsNoResource = _CardBTUsNoResource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 194),
    _CardBTUsNoResource_Type()
)
cardBTUsNoResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsNoResource.setStatus("mandatory")
_CardInvalidPvcBTUsThreshold_Type = Integer32
_CardInvalidPvcBTUsThreshold_Object = MibTableColumn
cardInvalidPvcBTUsThreshold = _CardInvalidPvcBTUsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 195),
    _CardInvalidPvcBTUsThreshold_Type()
)
cardInvalidPvcBTUsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardInvalidPvcBTUsThreshold.setStatus("mandatory")
_CardIncompleteFramesFromBusThreshold_Type = Integer32
_CardIncompleteFramesFromBusThreshold_Object = MibTableColumn
cardIncompleteFramesFromBusThreshold = _CardIncompleteFramesFromBusThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 196),
    _CardIncompleteFramesFromBusThreshold_Type()
)
cardIncompleteFramesFromBusThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardIncompleteFramesFromBusThreshold.setStatus("mandatory")
_CardBTUsBusErrorThreshold_Type = Integer32
_CardBTUsBusErrorThreshold_Object = MibTableColumn
cardBTUsBusErrorThreshold = _CardBTUsBusErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 197),
    _CardBTUsBusErrorThreshold_Type()
)
cardBTUsBusErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsBusErrorThreshold.setStatus("mandatory")
_CardBTUsNoResourceThreshold_Type = Integer32
_CardBTUsNoResourceThreshold_Object = MibTableColumn
cardBTUsNoResourceThreshold = _CardBTUsNoResourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 198),
    _CardBTUsNoResourceThreshold_Type()
)
cardBTUsNoResourceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardBTUsNoResourceThreshold.setStatus("mandatory")
_CardFrameMemoryThreshold_Type = Integer32
_CardFrameMemoryThreshold_Object = MibTableColumn
cardFrameMemoryThreshold = _CardFrameMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 199),
    _CardFrameMemoryThreshold_Type()
)
cardFrameMemoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardFrameMemoryThreshold.setStatus("mandatory")
_CardHoldQFrameMemory_Type = Counter32
_CardHoldQFrameMemory_Object = MibTableColumn
cardHoldQFrameMemory = _CardHoldQFrameMemory_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 200),
    _CardHoldQFrameMemory_Type()
)
cardHoldQFrameMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHoldQFrameMemory.setStatus("mandatory")
_CardTotalAAL5RxErrorCount_Type = Counter32
_CardTotalAAL5RxErrorCount_Object = MibTableColumn
cardTotalAAL5RxErrorCount = _CardTotalAAL5RxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 201),
    _CardTotalAAL5RxErrorCount_Type()
)
cardTotalAAL5RxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTotalAAL5RxErrorCount.setStatus("mandatory")
_CardOperMemSize_Type = Integer32
_CardOperMemSize_Object = MibTableColumn
cardOperMemSize = _CardOperMemSize_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 7, 2, 1, 202),
    _CardOperMemSize_Type()
)
cardOperMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperMemSize.setStatus("mandatory")
_Ds1_ObjectIdentity = ObjectIdentity
ds1 = _Ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 1, 8)
)
_Dsx1ConfigTable_Object = MibTable
dsx1ConfigTable = _Dsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1)
)
if mibBuilder.loadTexts:
    dsx1ConfigTable.setStatus("mandatory")
_Dsx1ConfigEntry_Object = MibTableRow
dsx1ConfigEntry = _Dsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1)
)
dsx1ConfigEntry.setIndexNames(
    (0, "CASCADE-MIB", "dsx1SlotId"),
    (0, "CASCADE-MIB", "dsx1PortId"),
)
if mibBuilder.loadTexts:
    dsx1ConfigEntry.setStatus("mandatory")
_Dsx1SlotId_Type = Integer32
_Dsx1SlotId_Object = MibTableColumn
dsx1SlotId = _Dsx1SlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 1),
    _Dsx1SlotId_Type()
)
dsx1SlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1SlotId.setStatus("mandatory")
_Dsx1PortId_Type = Integer32
_Dsx1PortId_Object = MibTableColumn
dsx1PortId = _Dsx1PortId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 2),
    _Dsx1PortId_Type()
)
dsx1PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1PortId.setStatus("mandatory")


class _Dsx1TimeElapsed_Type(Integer32):
    """Custom type dsx1TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dsx1TimeElapsed_Type.__name__ = "Integer32"
_Dsx1TimeElapsed_Object = MibTableColumn
dsx1TimeElapsed = _Dsx1TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 3),
    _Dsx1TimeElapsed_Type()
)
dsx1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TimeElapsed.setStatus("mandatory")


class _Dsx1ValidIntervals_Type(Integer32):
    """Custom type dsx1ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx1ValidIntervals_Type.__name__ = "Integer32"
_Dsx1ValidIntervals_Object = MibTableColumn
dsx1ValidIntervals = _Dsx1ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 4),
    _Dsx1ValidIntervals_Type()
)
dsx1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ValidIntervals.setStatus("mandatory")


class _Dsx1LineType_Type(Integer32):
    """Custom type dsx1LineType based on Integer32"""
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
        *(("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1-CRC", 5),
          ("dsx1E1-CRC-MF", 7),
          ("dsx1E1-MF", 6),
          ("dsx1ESF", 2),
          ("other", 1))
    )


_Dsx1LineType_Type.__name__ = "Integer32"
_Dsx1LineType_Object = MibTableColumn
dsx1LineType = _Dsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 5),
    _Dsx1LineType_Type()
)
dsx1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineType.setStatus("mandatory")


class _Dsx1LineCoding_Type(Integer32):
    """Custom type dsx1LineCoding based on Integer32"""
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
        *(("dsx1AMI", 5),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("dsx1ZBTSI", 4),
          ("other", 6))
    )


_Dsx1LineCoding_Type.__name__ = "Integer32"
_Dsx1LineCoding_Object = MibTableColumn
dsx1LineCoding = _Dsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 6),
    _Dsx1LineCoding_Type()
)
dsx1LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineCoding.setStatus("mandatory")


class _Dsx1SendCode_Type(Integer32):
    """Custom type dsx1SendCode based on Integer32"""
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
        *(("dsx1Send3in24Pattern", 7),
          ("dsx1Send511Pattern", 6),
          ("dsx1SendLineCode", 2),
          ("dsx1SendNoCode", 1),
          ("dsx1SendOtherTestPattern", 8),
          ("dsx1SendPayloadCode", 3),
          ("dsx1SendQRS", 5),
          ("dsx1SendResetCode", 4))
    )


_Dsx1SendCode_Type.__name__ = "Integer32"
_Dsx1SendCode_Object = MibTableColumn
dsx1SendCode = _Dsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 7),
    _Dsx1SendCode_Type()
)
dsx1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1SendCode.setStatus("mandatory")


class _Dsx1CircuitIdentifier_Type(DisplayString):
    """Custom type dsx1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dsx1CircuitIdentifier_Type.__name__ = "DisplayString"
_Dsx1CircuitIdentifier_Object = MibTableColumn
dsx1CircuitIdentifier = _Dsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 8),
    _Dsx1CircuitIdentifier_Type()
)
dsx1CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CircuitIdentifier.setStatus("mandatory")


class _Dsx1LoopbackConfig_Type(Integer32):
    """Custom type dsx1LoopbackConfig based on Integer32"""
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
        *(("dsx1LineLoop", 3),
          ("dsx1NoLoop", 1),
          ("dsx1OtherLoop", 4),
          ("dsx1PayloadLoop", 2))
    )


_Dsx1LoopbackConfig_Type.__name__ = "Integer32"
_Dsx1LoopbackConfig_Object = MibTableColumn
dsx1LoopbackConfig = _Dsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 9),
    _Dsx1LoopbackConfig_Type()
)
dsx1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LoopbackConfig.setStatus("mandatory")


class _Dsx1LineStatus_Type(Integer32):
    """Custom type dsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_Dsx1LineStatus_Type.__name__ = "Integer32"
_Dsx1LineStatus_Object = MibTableColumn
dsx1LineStatus = _Dsx1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 10),
    _Dsx1LineStatus_Type()
)
dsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineStatus.setStatus("mandatory")


class _Dsx1SignalMode_Type(Integer32):
    """Custom type dsx1SignalMode based on Integer32"""
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
        *(("bitOriented", 3),
          ("messageOriented", 4),
          ("none", 1),
          ("robbedBit", 2))
    )


_Dsx1SignalMode_Type.__name__ = "Integer32"
_Dsx1SignalMode_Object = MibTableColumn
dsx1SignalMode = _Dsx1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 11),
    _Dsx1SignalMode_Type()
)
dsx1SignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1SignalMode.setStatus("mandatory")


class _Dsx1TransmitClockSource_Type(Integer32):
    """Custom type dsx1TransmitClockSource based on Integer32"""
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


_Dsx1TransmitClockSource_Type.__name__ = "Integer32"
_Dsx1TransmitClockSource_Object = MibTableColumn
dsx1TransmitClockSource = _Dsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 12),
    _Dsx1TransmitClockSource_Type()
)
dsx1TransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TransmitClockSource.setStatus("mandatory")


class _Dsx1Fdl_Type(Integer32):
    """Custom type dsx1Fdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dsx1Ansi-T1-403", 2),
          ("dsx1Att-54016", 4),
          ("dsx1Fdl-none", 8),
          ("other", 1))
    )


_Dsx1Fdl_Type.__name__ = "Integer32"
_Dsx1Fdl_Object = MibTableColumn
dsx1Fdl = _Dsx1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 13),
    _Dsx1Fdl_Type()
)
dsx1Fdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Fdl.setStatus("mandatory")
_Dsx1FdlVersion_Type = Integer32
_Dsx1FdlVersion_Object = MibTableColumn
dsx1FdlVersion = _Dsx1FdlVersion_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 1, 1, 14),
    _Dsx1FdlVersion_Type()
)
dsx1FdlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FdlVersion.setStatus("mandatory")
_Dsx1CurrentTable_Object = MibTable
dsx1CurrentTable = _Dsx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2)
)
if mibBuilder.loadTexts:
    dsx1CurrentTable.setStatus("mandatory")
_Dsx1CurrentEntry_Object = MibTableRow
dsx1CurrentEntry = _Dsx1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1)
)
dsx1CurrentEntry.setIndexNames(
    (0, "CASCADE-MIB", "dsx1CurrentSlotId"),
    (0, "CASCADE-MIB", "dsx1CurrentPortId"),
)
if mibBuilder.loadTexts:
    dsx1CurrentEntry.setStatus("mandatory")
_Dsx1CurrentSlotId_Type = Integer32
_Dsx1CurrentSlotId_Object = MibTableColumn
dsx1CurrentSlotId = _Dsx1CurrentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 1),
    _Dsx1CurrentSlotId_Type()
)
dsx1CurrentSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentSlotId.setStatus("mandatory")
_Dsx1CurrentPortId_Type = Integer32
_Dsx1CurrentPortId_Object = MibTableColumn
dsx1CurrentPortId = _Dsx1CurrentPortId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 2),
    _Dsx1CurrentPortId_Type()
)
dsx1CurrentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentPortId.setStatus("mandatory")
_Dsx1CurrentESs_Type = Gauge32
_Dsx1CurrentESs_Object = MibTableColumn
dsx1CurrentESs = _Dsx1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 3),
    _Dsx1CurrentESs_Type()
)
dsx1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentESs.setStatus("mandatory")
_Dsx1CurrentSESs_Type = Gauge32
_Dsx1CurrentSESs_Object = MibTableColumn
dsx1CurrentSESs = _Dsx1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 4),
    _Dsx1CurrentSESs_Type()
)
dsx1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentSESs.setStatus("mandatory")
_Dsx1CurrentSEFSs_Type = Gauge32
_Dsx1CurrentSEFSs_Object = MibTableColumn
dsx1CurrentSEFSs = _Dsx1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 5),
    _Dsx1CurrentSEFSs_Type()
)
dsx1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentSEFSs.setStatus("mandatory")
_Dsx1CurrentUASs_Type = Gauge32
_Dsx1CurrentUASs_Object = MibTableColumn
dsx1CurrentUASs = _Dsx1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 6),
    _Dsx1CurrentUASs_Type()
)
dsx1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentUASs.setStatus("mandatory")
_Dsx1CurrentCSSs_Type = Gauge32
_Dsx1CurrentCSSs_Object = MibTableColumn
dsx1CurrentCSSs = _Dsx1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 7),
    _Dsx1CurrentCSSs_Type()
)
dsx1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentCSSs.setStatus("mandatory")
_Dsx1CurrentBESs_Type = Gauge32
_Dsx1CurrentBESs_Object = MibTableColumn
dsx1CurrentBESs = _Dsx1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 2, 1, 8),
    _Dsx1CurrentBESs_Type()
)
dsx1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentBESs.setStatus("mandatory")
_Dsx1IntervalTable_Object = MibTable
dsx1IntervalTable = _Dsx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3)
)
if mibBuilder.loadTexts:
    dsx1IntervalTable.setStatus("mandatory")
_Dsx1IntervalEntry_Object = MibTableRow
dsx1IntervalEntry = _Dsx1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1)
)
dsx1IntervalEntry.setIndexNames(
    (0, "CASCADE-MIB", "dsx1IntervalSlotId"),
    (0, "CASCADE-MIB", "dsx1IntervalPortId"),
    (0, "CASCADE-MIB", "dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1IntervalEntry.setStatus("mandatory")
_Dsx1IntervalSlotId_Type = Integer32
_Dsx1IntervalSlotId_Object = MibTableColumn
dsx1IntervalSlotId = _Dsx1IntervalSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 1),
    _Dsx1IntervalSlotId_Type()
)
dsx1IntervalSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalSlotId.setStatus("mandatory")
_Dsx1IntervalPortId_Type = Integer32
_Dsx1IntervalPortId_Object = MibTableColumn
dsx1IntervalPortId = _Dsx1IntervalPortId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 2),
    _Dsx1IntervalPortId_Type()
)
dsx1IntervalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalPortId.setStatus("mandatory")


class _Dsx1IntervalNumber_Type(Integer32):
    """Custom type dsx1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx1IntervalNumber_Type.__name__ = "Integer32"
_Dsx1IntervalNumber_Object = MibTableColumn
dsx1IntervalNumber = _Dsx1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 3),
    _Dsx1IntervalNumber_Type()
)
dsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalNumber.setStatus("mandatory")
_Dsx1IntervalESs_Type = Gauge32
_Dsx1IntervalESs_Object = MibTableColumn
dsx1IntervalESs = _Dsx1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 4),
    _Dsx1IntervalESs_Type()
)
dsx1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalESs.setStatus("mandatory")
_Dsx1IntervalSESs_Type = Gauge32
_Dsx1IntervalSESs_Object = MibTableColumn
dsx1IntervalSESs = _Dsx1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 5),
    _Dsx1IntervalSESs_Type()
)
dsx1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalSESs.setStatus("mandatory")
_Dsx1IntervalSEFSs_Type = Gauge32
_Dsx1IntervalSEFSs_Object = MibTableColumn
dsx1IntervalSEFSs = _Dsx1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 6),
    _Dsx1IntervalSEFSs_Type()
)
dsx1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalSEFSs.setStatus("mandatory")
_Dsx1IntervalUASs_Type = Gauge32
_Dsx1IntervalUASs_Object = MibTableColumn
dsx1IntervalUASs = _Dsx1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 7),
    _Dsx1IntervalUASs_Type()
)
dsx1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalUASs.setStatus("mandatory")
_Dsx1IntervalCSSs_Type = Gauge32
_Dsx1IntervalCSSs_Object = MibTableColumn
dsx1IntervalCSSs = _Dsx1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 8),
    _Dsx1IntervalCSSs_Type()
)
dsx1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalCSSs.setStatus("mandatory")
_Dsx1IntervalBESs_Type = Gauge32
_Dsx1IntervalBESs_Object = MibTableColumn
dsx1IntervalBESs = _Dsx1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 3, 1, 9),
    _Dsx1IntervalBESs_Type()
)
dsx1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalBESs.setStatus("mandatory")
_Dsx1TotalTable_Object = MibTable
dsx1TotalTable = _Dsx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4)
)
if mibBuilder.loadTexts:
    dsx1TotalTable.setStatus("mandatory")
_Dsx1TotalEntry_Object = MibTableRow
dsx1TotalEntry = _Dsx1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1)
)
dsx1TotalEntry.setIndexNames(
    (0, "CASCADE-MIB", "dsx1TotalSlotId"),
    (0, "CASCADE-MIB", "dsx1TotalPortId"),
)
if mibBuilder.loadTexts:
    dsx1TotalEntry.setStatus("mandatory")
_Dsx1TotalSlotId_Type = Integer32
_Dsx1TotalSlotId_Object = MibTableColumn
dsx1TotalSlotId = _Dsx1TotalSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 1),
    _Dsx1TotalSlotId_Type()
)
dsx1TotalSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalSlotId.setStatus("mandatory")
_Dsx1TotalPortId_Type = Integer32
_Dsx1TotalPortId_Object = MibTableColumn
dsx1TotalPortId = _Dsx1TotalPortId_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 2),
    _Dsx1TotalPortId_Type()
)
dsx1TotalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalPortId.setStatus("mandatory")
_Dsx1TotalESs_Type = Gauge32
_Dsx1TotalESs_Object = MibTableColumn
dsx1TotalESs = _Dsx1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 3),
    _Dsx1TotalESs_Type()
)
dsx1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalESs.setStatus("mandatory")
_Dsx1TotalSESs_Type = Gauge32
_Dsx1TotalSESs_Object = MibTableColumn
dsx1TotalSESs = _Dsx1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 4),
    _Dsx1TotalSESs_Type()
)
dsx1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalSESs.setStatus("mandatory")
_Dsx1TotalSEFSs_Type = Gauge32
_Dsx1TotalSEFSs_Object = MibTableColumn
dsx1TotalSEFSs = _Dsx1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 5),
    _Dsx1TotalSEFSs_Type()
)
dsx1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalSEFSs.setStatus("mandatory")
_Dsx1TotalUASs_Type = Gauge32
_Dsx1TotalUASs_Object = MibTableColumn
dsx1TotalUASs = _Dsx1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 6),
    _Dsx1TotalUASs_Type()
)
dsx1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalUASs.setStatus("mandatory")
_Dsx1TotalCSSs_Type = Gauge32
_Dsx1TotalCSSs_Object = MibTableColumn
dsx1TotalCSSs = _Dsx1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 7),
    _Dsx1TotalCSSs_Type()
)
dsx1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalCSSs.setStatus("mandatory")
_Dsx1TotalBESs_Type = Gauge32
_Dsx1TotalBESs_Object = MibTableColumn
dsx1TotalBESs = _Dsx1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 277, 1, 8, 4, 1, 8),
    _Dsx1TotalBESs_Type()
)
dsx1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalBESs.setStatus("mandatory")
_Cascsmds_ObjectIdentity = ObjectIdentity
cascsmds = _Cascsmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 2)
)
_Smdsaddr_ObjectIdentity = ObjectIdentity
smdsaddr = _Smdsaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 2, 1)
)
_SmdsaddrTable_Object = MibTable
smdsaddrTable = _SmdsaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1)
)
if mibBuilder.loadTexts:
    smdsaddrTable.setStatus("mandatory")
_SmdsaddrEntry_Object = MibTableRow
smdsaddrEntry = _SmdsaddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1)
)
smdsaddrEntry.setIndexNames(
    (0, "CASCADE-MIB", "smdsaddrAddr"),
)
if mibBuilder.loadTexts:
    smdsaddrEntry.setStatus("mandatory")
_SmdsaddrAddr_Type = OctetString
_SmdsaddrAddr_Object = MibTableColumn
smdsaddrAddr = _SmdsaddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 1),
    _SmdsaddrAddr_Type()
)
smdsaddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrAddr.setStatus("mandatory")


class _SmdsaddrType_Type(Integer32):
    """Custom type smdsaddrType based on Integer32"""
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
        *(("local-group-address", 2),
          ("local-individual-address", 1),
          ("non-local-group-address", 4),
          ("non-local-individual-address", 3))
    )


_SmdsaddrType_Type.__name__ = "Integer32"
_SmdsaddrType_Object = MibTableColumn
smdsaddrType = _SmdsaddrType_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 2),
    _SmdsaddrType_Type()
)
smdsaddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrType.setStatus("mandatory")
_SmdsaddrId_Type = Integer32
_SmdsaddrId_Object = MibTableColumn
smdsaddrId = _SmdsaddrId_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 3),
    _SmdsaddrId_Type()
)
smdsaddrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrId.setStatus("mandatory")
_SmdsaddrIf_Type = Integer32
_SmdsaddrIf_Object = MibTableColumn
smdsaddrIf = _SmdsaddrIf_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 4),
    _SmdsaddrIf_Type()
)
smdsaddrIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrIf.setStatus("mandatory")
_SmdsaddrParentGrpMap_Type = OctetString
_SmdsaddrParentGrpMap_Object = MibTableColumn
smdsaddrParentGrpMap = _SmdsaddrParentGrpMap_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 5),
    _SmdsaddrParentGrpMap_Type()
)
smdsaddrParentGrpMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smdsaddrParentGrpMap.setStatus("mandatory")
_SmdsaddrParentScrnMap_Type = OctetString
_SmdsaddrParentScrnMap_Object = MibTableColumn
smdsaddrParentScrnMap = _SmdsaddrParentScrnMap_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 6),
    _SmdsaddrParentScrnMap_Type()
)
smdsaddrParentScrnMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smdsaddrParentScrnMap.setStatus("mandatory")
_SmdsaddrMemberAddrMap_Type = OctetString
_SmdsaddrMemberAddrMap_Object = MibTableColumn
smdsaddrMemberAddrMap = _SmdsaddrMemberAddrMap_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 7),
    _SmdsaddrMemberAddrMap_Type()
)
smdsaddrMemberAddrMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrMemberAddrMap.setStatus("mandatory")


class _SmdsaddrAdminStatus_Type(Integer32):
    """Custom type smdsaddrAdminStatus based on Integer32"""
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


_SmdsaddrAdminStatus_Type.__name__ = "Integer32"
_SmdsaddrAdminStatus_Object = MibTableColumn
smdsaddrAdminStatus = _SmdsaddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 8),
    _SmdsaddrAdminStatus_Type()
)
smdsaddrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrAdminStatus.setStatus("mandatory")
_SmdsaddrSlot_Type = Integer32
_SmdsaddrSlot_Object = MibTableColumn
smdsaddrSlot = _SmdsaddrSlot_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 9),
    _SmdsaddrSlot_Type()
)
smdsaddrSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrSlot.setStatus("mandatory")
_SmdsaddrSsiIfNum_Type = Integer32
_SmdsaddrSsiIfNum_Object = MibTableColumn
smdsaddrSsiIfNum = _SmdsaddrSsiIfNum_Object(
    (1, 3, 6, 1, 4, 1, 277, 2, 1, 1, 1, 10),
    _SmdsaddrSsiIfNum_Type()
)
smdsaddrSsiIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smdsaddrSsiIfNum.setStatus("mandatory")
_Namebinding_ObjectIdentity = ObjectIdentity
namebinding = _Namebinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 3)
)
_NamebindingTable_Object = MibTable
namebindingTable = _NamebindingTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1)
)
if mibBuilder.loadTexts:
    namebindingTable.setStatus("mandatory")
_NamebindingEntry_Object = MibTableRow
namebindingEntry = _NamebindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1)
)
namebindingEntry.setIndexNames(
    (0, "CASCADE-MIB", "nameType"),
    (0, "CASCADE-MIB", "nameName"),
    (0, "CASCADE-MIB", "namePrimary"),
)
if mibBuilder.loadTexts:
    namebindingEntry.setStatus("mandatory")


class _NameType_Type(Integer32):
    """Custom type nameType based on Integer32"""
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
        *(("e164", 2),
          ("nsap", 3),
          ("sni", 4),
          ("uninniladdr", 1))
    )


_NameType_Type.__name__ = "Integer32"
_NameType_Object = MibTableColumn
nameType = _NameType_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 1),
    _NameType_Type()
)
nameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameType.setStatus("mandatory")
_NameName_Type = OctetString
_NameName_Object = MibTableColumn
nameName = _NameName_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 2),
    _NameName_Type()
)
nameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameName.setStatus("mandatory")


class _NamePrimary_Type(Integer32):
    """Custom type namePrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_NamePrimary_Type.__name__ = "Integer32"
_NamePrimary_Object = MibTableColumn
namePrimary = _NamePrimary_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 3),
    _NamePrimary_Type()
)
namePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namePrimary.setStatus("mandatory")
_NameIfIndex_Type = Integer32
_NameIfIndex_Object = MibTableColumn
nameIfIndex = _NameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 4),
    _NameIfIndex_Type()
)
nameIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameIfIndex.setStatus("mandatory")
_NameNodeId_Type = Integer32
_NameNodeId_Object = MibTableColumn
nameNodeId = _NameNodeId_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 5),
    _NameNodeId_Type()
)
nameNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameNodeId.setStatus("mandatory")


class _NameStatus_Type(Integer32):
    """Custom type nameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("invalid", 2))
    )


_NameStatus_Type.__name__ = "Integer32"
_NameStatus_Object = MibTableColumn
nameStatus = _NameStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 3, 1, 1, 6),
    _NameStatus_Type()
)
nameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameStatus.setStatus("mandatory")
_Isdnaddr_ObjectIdentity = ObjectIdentity
isdnaddr = _Isdnaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 4)
)
_IsdnAddrTable_Object = MibTable
isdnAddrTable = _IsdnAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 1)
)
if mibBuilder.loadTexts:
    isdnAddrTable.setStatus("mandatory")
_IsdnAddrEntry_Object = MibTableRow
isdnAddrEntry = _IsdnAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 1, 1)
)
isdnAddrEntry.setIndexNames(
    (0, "CASCADE-MIB", "isdnAddrIf"),
)
if mibBuilder.loadTexts:
    isdnAddrEntry.setStatus("mandatory")
_IsdnAddrIf_Type = Integer32
_IsdnAddrIf_Object = MibTableColumn
isdnAddrIf = _IsdnAddrIf_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 1, 1, 1),
    _IsdnAddrIf_Type()
)
isdnAddrIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnAddrIf.setStatus("mandatory")
_IsdnAddr_Type = OctetString
_IsdnAddr_Object = MibTableColumn
isdnAddr = _IsdnAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 1, 1, 2),
    _IsdnAddr_Type()
)
isdnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnAddr.setStatus("mandatory")
_IsdnChanType_Type = Integer32
_IsdnChanType_Object = MibTableColumn
isdnChanType = _IsdnChanType_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 1, 1, 3),
    _IsdnChanType_Type()
)
isdnChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnChanType.setStatus("mandatory")
_IsdnCallerIDTable_Object = MibTable
isdnCallerIDTable = _IsdnCallerIDTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 2)
)
if mibBuilder.loadTexts:
    isdnCallerIDTable.setStatus("mandatory")
_IsdnCallerIDEntry_Object = MibTableRow
isdnCallerIDEntry = _IsdnCallerIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 2, 1)
)
isdnCallerIDEntry.setIndexNames(
    (0, "CASCADE-MIB", "isdnCallerIDIf"),
    (0, "CASCADE-MIB", "isdnCallerIDAddr"),
)
if mibBuilder.loadTexts:
    isdnCallerIDEntry.setStatus("mandatory")
_IsdnCallerIDIf_Type = Integer32
_IsdnCallerIDIf_Object = MibTableColumn
isdnCallerIDIf = _IsdnCallerIDIf_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 2, 1, 1),
    _IsdnCallerIDIf_Type()
)
isdnCallerIDIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCallerIDIf.setStatus("mandatory")
_IsdnCallerIDAddr_Type = OctetString
_IsdnCallerIDAddr_Object = MibTableColumn
isdnCallerIDAddr = _IsdnCallerIDAddr_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 2, 1, 2),
    _IsdnCallerIDAddr_Type()
)
isdnCallerIDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCallerIDAddr.setStatus("mandatory")


class _IsdnCallerAdminStatus_Type(Integer32):
    """Custom type isdnCallerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("add", 1)
    )


_IsdnCallerAdminStatus_Type.__name__ = "Integer32"
_IsdnCallerAdminStatus_Object = MibTableColumn
isdnCallerAdminStatus = _IsdnCallerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 4, 2, 1, 3),
    _IsdnCallerAdminStatus_Type()
)
isdnCallerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCallerAdminStatus.setStatus("mandatory")
_Cascsvc_ObjectIdentity = ObjectIdentity
cascsvc = _Cascsvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 5)
)
_Svcaddress_ObjectIdentity = ObjectIdentity
svcaddress = _Svcaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 5, 1)
)
_SvcNodePrefixTable_Object = MibTable
svcNodePrefixTable = _SvcNodePrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1)
)
if mibBuilder.loadTexts:
    svcNodePrefixTable.setStatus("mandatory")
_SvcNodePrefixEntry_Object = MibTableRow
svcNodePrefixEntry = _SvcNodePrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1, 1)
)
svcNodePrefixEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcNodePrefixPrefix"),
)
if mibBuilder.loadTexts:
    svcNodePrefixEntry.setStatus("mandatory")


class _SvcNodePrefixPrefix_Type(OctetString):
    """Custom type svcNodePrefixPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvcNodePrefixPrefix_Type.__name__ = "OctetString"
_SvcNodePrefixPrefix_Object = MibTableColumn
svcNodePrefixPrefix = _SvcNodePrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1, 1, 1),
    _SvcNodePrefixPrefix_Type()
)
svcNodePrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNodePrefixPrefix.setStatus("mandatory")


class _SvcNodePrefixNumBits_Type(Integer32):
    """Custom type svcNodePrefixNumBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_SvcNodePrefixNumBits_Type.__name__ = "Integer32"
_SvcNodePrefixNumBits_Object = MibTableColumn
svcNodePrefixNumBits = _SvcNodePrefixNumBits_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1, 1, 2),
    _SvcNodePrefixNumBits_Type()
)
svcNodePrefixNumBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcNodePrefixNumBits.setStatus("mandatory")


class _SvcNodePrefixNmbPlan_Type(Integer32):
    """Custom type svcNodePrefixNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcNodePrefixNmbPlan_Type.__name__ = "Integer32"
_SvcNodePrefixNmbPlan_Object = MibTableColumn
svcNodePrefixNmbPlan = _SvcNodePrefixNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1, 1, 3),
    _SvcNodePrefixNmbPlan_Type()
)
svcNodePrefixNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcNodePrefixNmbPlan.setStatus("mandatory")


class _SvcNodePrefixAdminStatus_Type(Integer32):
    """Custom type svcNodePrefixAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("invalid", 2))
    )


_SvcNodePrefixAdminStatus_Type.__name__ = "Integer32"
_SvcNodePrefixAdminStatus_Object = MibTableColumn
svcNodePrefixAdminStatus = _SvcNodePrefixAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 1, 1, 4),
    _SvcNodePrefixAdminStatus_Type()
)
svcNodePrefixAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcNodePrefixAdminStatus.setStatus("mandatory")
_SvcPrefixTable_Object = MibTable
svcPrefixTable = _SvcPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2)
)
if mibBuilder.loadTexts:
    svcPrefixTable.setStatus("mandatory")
_SvcPrefixEntry_Object = MibTableRow
svcPrefixEntry = _SvcPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1)
)
svcPrefixEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcPrefixIfIndex"),
    (0, "CASCADE-MIB", "svcPrefixPrefix"),
)
if mibBuilder.loadTexts:
    svcPrefixEntry.setStatus("mandatory")
_SvcPrefixIfIndex_Type = Index
_SvcPrefixIfIndex_Object = MibTableColumn
svcPrefixIfIndex = _SvcPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 1),
    _SvcPrefixIfIndex_Type()
)
svcPrefixIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPrefixIfIndex.setStatus("mandatory")


class _SvcPrefixPrefix_Type(OctetString):
    """Custom type svcPrefixPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvcPrefixPrefix_Type.__name__ = "OctetString"
_SvcPrefixPrefix_Object = MibTableColumn
svcPrefixPrefix = _SvcPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 2),
    _SvcPrefixPrefix_Type()
)
svcPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPrefixPrefix.setStatus("mandatory")


class _SvcPrefixNumBits_Type(Integer32):
    """Custom type svcPrefixNumBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_SvcPrefixNumBits_Type.__name__ = "Integer32"
_SvcPrefixNumBits_Object = MibTableColumn
svcPrefixNumBits = _SvcPrefixNumBits_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 3),
    _SvcPrefixNumBits_Type()
)
svcPrefixNumBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixNumBits.setStatus("mandatory")


class _SvcPrefixNmbPlan_Type(Integer32):
    """Custom type svcPrefixNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcPrefixNmbPlan_Type.__name__ = "Integer32"
_SvcPrefixNmbPlan_Object = MibTableColumn
svcPrefixNmbPlan = _SvcPrefixNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 4),
    _SvcPrefixNmbPlan_Type()
)
svcPrefixNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixNmbPlan.setStatus("mandatory")


class _SvcPrefixAdminCost_Type(Integer32):
    """Custom type svcPrefixAdminCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcPrefixAdminCost_Type.__name__ = "Integer32"
_SvcPrefixAdminCost_Object = MibTableColumn
svcPrefixAdminCost = _SvcPrefixAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 5),
    _SvcPrefixAdminCost_Type()
)
svcPrefixAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixAdminCost.setStatus("mandatory")


class _SvcPrefixLocalGatewayAddress_Type(OctetString):
    """Custom type svcPrefixLocalGatewayAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SvcPrefixLocalGatewayAddress_Type.__name__ = "OctetString"
_SvcPrefixLocalGatewayAddress_Object = MibTableColumn
svcPrefixLocalGatewayAddress = _SvcPrefixLocalGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 6),
    _SvcPrefixLocalGatewayAddress_Type()
)
svcPrefixLocalGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixLocalGatewayAddress.setStatus("mandatory")


class _SvcPrefixLocalGatewayNmbPlan_Type(Integer32):
    """Custom type svcPrefixLocalGatewayNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcPrefixLocalGatewayNmbPlan_Type.__name__ = "Integer32"
_SvcPrefixLocalGatewayNmbPlan_Object = MibTableColumn
svcPrefixLocalGatewayNmbPlan = _SvcPrefixLocalGatewayNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 7),
    _SvcPrefixLocalGatewayNmbPlan_Type()
)
svcPrefixLocalGatewayNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixLocalGatewayNmbPlan.setStatus("mandatory")


class _SvcPrefixRemoteGatewayAddress_Type(OctetString):
    """Custom type svcPrefixRemoteGatewayAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvcPrefixRemoteGatewayAddress_Type.__name__ = "OctetString"
_SvcPrefixRemoteGatewayAddress_Object = MibTableColumn
svcPrefixRemoteGatewayAddress = _SvcPrefixRemoteGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 8),
    _SvcPrefixRemoteGatewayAddress_Type()
)
svcPrefixRemoteGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixRemoteGatewayAddress.setStatus("mandatory")


class _SvcPrefixRemoteGatewayNmbPlan_Type(Integer32):
    """Custom type svcPrefixRemoteGatewayNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcPrefixRemoteGatewayNmbPlan_Type.__name__ = "Integer32"
_SvcPrefixRemoteGatewayNmbPlan_Object = MibTableColumn
svcPrefixRemoteGatewayNmbPlan = _SvcPrefixRemoteGatewayNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 9),
    _SvcPrefixRemoteGatewayNmbPlan_Type()
)
svcPrefixRemoteGatewayNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixRemoteGatewayNmbPlan.setStatus("mandatory")


class _SvcPrefixAdminStatus_Type(Integer32):
    """Custom type svcPrefixAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("dynamic", 3),
          ("invalid", 2))
    )


_SvcPrefixAdminStatus_Type.__name__ = "Integer32"
_SvcPrefixAdminStatus_Object = MibTableColumn
svcPrefixAdminStatus = _SvcPrefixAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 2, 1, 10),
    _SvcPrefixAdminStatus_Type()
)
svcPrefixAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPrefixAdminStatus.setStatus("mandatory")
_SvcAddrTable_Object = MibTable
svcAddrTable = _SvcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3)
)
if mibBuilder.loadTexts:
    svcAddrTable.setStatus("mandatory")
_SvcAddrEntry_Object = MibTableRow
svcAddrEntry = _SvcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3, 1)
)
svcAddrEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcAddrIfIndex"),
    (0, "CASCADE-MIB", "svcAddrAddress"),
)
if mibBuilder.loadTexts:
    svcAddrEntry.setStatus("mandatory")
_SvcAddrIfIndex_Type = Index
_SvcAddrIfIndex_Object = MibTableColumn
svcAddrIfIndex = _SvcAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3, 1, 1),
    _SvcAddrIfIndex_Type()
)
svcAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAddrIfIndex.setStatus("mandatory")


class _SvcAddrAddress_Type(OctetString):
    """Custom type svcAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvcAddrAddress_Type.__name__ = "OctetString"
_SvcAddrAddress_Object = MibTableColumn
svcAddrAddress = _SvcAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3, 1, 2),
    _SvcAddrAddress_Type()
)
svcAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAddrAddress.setStatus("mandatory")


class _SvcAddrNmbPlan_Type(Integer32):
    """Custom type svcAddrNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcAddrNmbPlan_Type.__name__ = "Integer32"
_SvcAddrNmbPlan_Object = MibTableColumn
svcAddrNmbPlan = _SvcAddrNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3, 1, 3),
    _SvcAddrNmbPlan_Type()
)
svcAddrNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAddrNmbPlan.setStatus("mandatory")


class _SvcAddrAdminStatus_Type(Integer32):
    """Custom type svcAddrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("dynamic", 3),
          ("invalid", 2))
    )


_SvcAddrAdminStatus_Type.__name__ = "Integer32"
_SvcAddrAdminStatus_Object = MibTableColumn
svcAddrAdminStatus = _SvcAddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 3, 1, 4),
    _SvcAddrAdminStatus_Type()
)
svcAddrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAddrAdminStatus.setStatus("mandatory")
_SvcAtmUserPartTable_Object = MibTable
svcAtmUserPartTable = _SvcAtmUserPartTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 4)
)
if mibBuilder.loadTexts:
    svcAtmUserPartTable.setStatus("mandatory")
_SvcAtmUserPartEntry_Object = MibTableRow
svcAtmUserPartEntry = _SvcAtmUserPartEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 4, 1)
)
svcAtmUserPartEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcAtmUserPartIfIndex"),
    (0, "CASCADE-MIB", "svcAtmUserPartUserPart"),
)
if mibBuilder.loadTexts:
    svcAtmUserPartEntry.setStatus("mandatory")
_SvcAtmUserPartIfIndex_Type = Index
_SvcAtmUserPartIfIndex_Object = MibTableColumn
svcAtmUserPartIfIndex = _SvcAtmUserPartIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 4, 1, 1),
    _SvcAtmUserPartIfIndex_Type()
)
svcAtmUserPartIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmUserPartIfIndex.setStatus("mandatory")


class _SvcAtmUserPartUserPart_Type(OctetString):
    """Custom type svcAtmUserPartUserPart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SvcAtmUserPartUserPart_Type.__name__ = "OctetString"
_SvcAtmUserPartUserPart_Object = MibTableColumn
svcAtmUserPartUserPart = _SvcAtmUserPartUserPart_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 4, 1, 2),
    _SvcAtmUserPartUserPart_Type()
)
svcAtmUserPartUserPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmUserPartUserPart.setStatus("mandatory")


class _SvcAtmUserPartAdminStatus_Type(Integer32):
    """Custom type svcAtmUserPartAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("invalid", 2))
    )


_SvcAtmUserPartAdminStatus_Type.__name__ = "Integer32"
_SvcAtmUserPartAdminStatus_Object = MibTableColumn
svcAtmUserPartAdminStatus = _SvcAtmUserPartAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 1, 4, 1, 3),
    _SvcAtmUserPartAdminStatus_Type()
)
svcAtmUserPartAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmUserPartAdminStatus.setStatus("mandatory")
_Svcmgt_ObjectIdentity = ObjectIdentity
svcmgt = _Svcmgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 5, 2)
)
_SvcConfigTable_Object = MibTable
svcConfigTable = _SvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1)
)
if mibBuilder.loadTexts:
    svcConfigTable.setStatus("mandatory")
_SvcConfigEntry_Object = MibTableRow
svcConfigEntry = _SvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1)
)
svcConfigEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcConfigIfIndex"),
)
if mibBuilder.loadTexts:
    svcConfigEntry.setStatus("mandatory")
_SvcConfigIfIndex_Type = Index
_SvcConfigIfIndex_Object = MibTableColumn
svcConfigIfIndex = _SvcConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 1),
    _SvcConfigIfIndex_Type()
)
svcConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcConfigIfIndex.setStatus("mandatory")
_SvcConfigInitiateIdentStatsUpload_Type = IpAddress
_SvcConfigInitiateIdentStatsUpload_Object = MibTableColumn
svcConfigInitiateIdentStatsUpload = _SvcConfigInitiateIdentStatsUpload_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 2),
    _SvcConfigInitiateIdentStatsUpload_Type()
)
svcConfigInitiateIdentStatsUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigInitiateIdentStatsUpload.setStatus("mandatory")


class _SvcConfigCgPtyInsertionMode_Type(Integer32):
    """Custom type svcConfigCgPtyInsertionMode based on Integer32"""
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
          ("insert", 2),
          ("replace", 3))
    )


_SvcConfigCgPtyInsertionMode_Type.__name__ = "Integer32"
_SvcConfigCgPtyInsertionMode_Object = MibTableColumn
svcConfigCgPtyInsertionMode = _SvcConfigCgPtyInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 3),
    _SvcConfigCgPtyInsertionMode_Type()
)
svcConfigCgPtyInsertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigCgPtyInsertionMode.setStatus("mandatory")


class _SvcConfigCgPtyInsertionAddress_Type(OctetString):
    """Custom type svcConfigCgPtyInsertionAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 20),
    )


_SvcConfigCgPtyInsertionAddress_Type.__name__ = "OctetString"
_SvcConfigCgPtyInsertionAddress_Object = MibTableColumn
svcConfigCgPtyInsertionAddress = _SvcConfigCgPtyInsertionAddress_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 4),
    _SvcConfigCgPtyInsertionAddress_Type()
)
svcConfigCgPtyInsertionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigCgPtyInsertionAddress.setStatus("mandatory")


class _SvcConfigCgPtyInsertionNmbPlan_Type(Integer32):
    """Custom type svcConfigCgPtyInsertionNmbPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm-endsystem", 2),
          ("e164", 1),
          ("unknown", 4))
    )


_SvcConfigCgPtyInsertionNmbPlan_Type.__name__ = "Integer32"
_SvcConfigCgPtyInsertionNmbPlan_Object = MibTableColumn
svcConfigCgPtyInsertionNmbPlan = _SvcConfigCgPtyInsertionNmbPlan_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 5),
    _SvcConfigCgPtyInsertionNmbPlan_Type()
)
svcConfigCgPtyInsertionNmbPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigCgPtyInsertionNmbPlan.setStatus("mandatory")


class _SvcConfigCgPtyScreenMode_Type(Integer32):
    """Custom type svcConfigCgPtyScreenMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("address", 4),
          ("disabled", 255),
          ("node-prefix", 1),
          ("node-prefix-or-address", 5),
          ("node-prefix-or-port-prefix", 3),
          ("node-prefix-or-port-prefix-or-address", 7),
          ("port-prefix", 2),
          ("port-prefix-or-address", 6))
    )


_SvcConfigCgPtyScreenMode_Type.__name__ = "Integer32"
_SvcConfigCgPtyScreenMode_Object = MibTableColumn
svcConfigCgPtyScreenMode = _SvcConfigCgPtyScreenMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 6),
    _SvcConfigCgPtyScreenMode_Type()
)
svcConfigCgPtyScreenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigCgPtyScreenMode.setStatus("mandatory")


class _SvcConfigEgressAddrXlateMode_Type(Integer32):
    """Custom type svcConfigEgressAddrXlateMode based on Integer32"""
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
        *(("disabled", 1),
          ("replace-when-called-party-matches-prefix", 3),
          ("translate-e164-native-to-nsap", 4),
          ("translate-e164-nsap-to-native", 5),
          ("tunnel-when-called-party-matches-prefix", 2))
    )


_SvcConfigEgressAddrXlateMode_Type.__name__ = "Integer32"
_SvcConfigEgressAddrXlateMode_Object = MibTableColumn
svcConfigEgressAddrXlateMode = _SvcConfigEgressAddrXlateMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 7),
    _SvcConfigEgressAddrXlateMode_Type()
)
svcConfigEgressAddrXlateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigEgressAddrXlateMode.setStatus("mandatory")


class _SvcConfigIngressAddrXlateMode_Type(Integer32):
    """Custom type svcConfigIngressAddrXlateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("translate-e164-native-to-nsap", 4),
          ("translate-e164-nsap-to-native", 5),
          ("tunnel", 2))
    )


_SvcConfigIngressAddrXlateMode_Type.__name__ = "Integer32"
_SvcConfigIngressAddrXlateMode_Object = MibTableColumn
svcConfigIngressAddrXlateMode = _SvcConfigIngressAddrXlateMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 8),
    _SvcConfigIngressAddrXlateMode_Type()
)
svcConfigIngressAddrXlateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigIngressAddrXlateMode.setStatus("mandatory")


class _SvcConfigCgPtyPresentationMode_Type(Integer32):
    """Custom type svcConfigCgPtyPresentationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("never", 2),
          ("user", 1))
    )


_SvcConfigCgPtyPresentationMode_Type.__name__ = "Integer32"
_SvcConfigCgPtyPresentationMode_Object = MibTableColumn
svcConfigCgPtyPresentationMode = _SvcConfigCgPtyPresentationMode_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 1, 1, 9),
    _SvcConfigCgPtyPresentationMode_Type()
)
svcConfigCgPtyPresentationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcConfigCgPtyPresentationMode.setStatus("mandatory")
_SvcAtmConfigTable_Object = MibTable
svcAtmConfigTable = _SvcAtmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2)
)
if mibBuilder.loadTexts:
    svcAtmConfigTable.setStatus("mandatory")
_SvcAtmConfigEntry_Object = MibTableRow
svcAtmConfigEntry = _SvcAtmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1)
)
svcAtmConfigEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcAtmConfigIfIndex"),
)
if mibBuilder.loadTexts:
    svcAtmConfigEntry.setStatus("mandatory")
_SvcAtmConfigIfIndex_Type = Index
_SvcAtmConfigIfIndex_Object = MibTableColumn
svcAtmConfigIfIndex = _SvcAtmConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 1),
    _SvcAtmConfigIfIndex_Type()
)
svcAtmConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigIfIndex.setStatus("mandatory")


class _SvcAtmConfigAdminStatus_Type(Integer32):
    """Custom type svcAtmConfigAdminStatus based on Integer32"""
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


_SvcAtmConfigAdminStatus_Type.__name__ = "Integer32"
_SvcAtmConfigAdminStatus_Object = MibTableColumn
svcAtmConfigAdminStatus = _SvcAtmConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 2),
    _SvcAtmConfigAdminStatus_Type()
)
svcAtmConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigAdminStatus.setStatus("mandatory")


class _SvcAtmConfigOperStatus_Type(Integer32):
    """Custom type svcAtmConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("down", 1),
          ("up", 3))
    )


_SvcAtmConfigOperStatus_Type.__name__ = "Integer32"
_SvcAtmConfigOperStatus_Object = MibTableColumn
svcAtmConfigOperStatus = _SvcAtmConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 3),
    _SvcAtmConfigOperStatus_Type()
)
svcAtmConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigOperStatus.setStatus("mandatory")
_SvcAtmConfigQ93bMaxRestart_Type = Integer32
_SvcAtmConfigQ93bMaxRestart_Object = MibTableColumn
svcAtmConfigQ93bMaxRestart = _SvcAtmConfigQ93bMaxRestart_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 4),
    _SvcAtmConfigQ93bMaxRestart_Type()
)
svcAtmConfigQ93bMaxRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bMaxRestart.setStatus("mandatory")
_SvcAtmConfigQ93bMaxStatEnq_Type = Integer32
_SvcAtmConfigQ93bMaxStatEnq_Object = MibTableColumn
svcAtmConfigQ93bMaxStatEnq = _SvcAtmConfigQ93bMaxStatEnq_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 5),
    _SvcAtmConfigQ93bMaxStatEnq_Type()
)
svcAtmConfigQ93bMaxStatEnq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bMaxStatEnq.setStatus("mandatory")
_SvcAtmConfigQ93bT303_Type = Integer32
_SvcAtmConfigQ93bT303_Object = MibTableColumn
svcAtmConfigQ93bT303 = _SvcAtmConfigQ93bT303_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 6),
    _SvcAtmConfigQ93bT303_Type()
)
svcAtmConfigQ93bT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT303.setStatus("mandatory")
_SvcAtmConfigQ93bT308_Type = Integer32
_SvcAtmConfigQ93bT308_Object = MibTableColumn
svcAtmConfigQ93bT308 = _SvcAtmConfigQ93bT308_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 7),
    _SvcAtmConfigQ93bT308_Type()
)
svcAtmConfigQ93bT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT308.setStatus("mandatory")
_SvcAtmConfigQ93bT309_Type = Integer32
_SvcAtmConfigQ93bT309_Object = MibTableColumn
svcAtmConfigQ93bT309 = _SvcAtmConfigQ93bT309_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 8),
    _SvcAtmConfigQ93bT309_Type()
)
svcAtmConfigQ93bT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT309.setStatus("mandatory")
_SvcAtmConfigQ93bT310_Type = Integer32
_SvcAtmConfigQ93bT310_Object = MibTableColumn
svcAtmConfigQ93bT310 = _SvcAtmConfigQ93bT310_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 9),
    _SvcAtmConfigQ93bT310_Type()
)
svcAtmConfigQ93bT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT310.setStatus("mandatory")
_SvcAtmConfigQ93bT313_Type = Integer32
_SvcAtmConfigQ93bT313_Object = MibTableColumn
svcAtmConfigQ93bT313 = _SvcAtmConfigQ93bT313_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 10),
    _SvcAtmConfigQ93bT313_Type()
)
svcAtmConfigQ93bT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT313.setStatus("mandatory")
_SvcAtmConfigQ93bT316_Type = Integer32
_SvcAtmConfigQ93bT316_Object = MibTableColumn
svcAtmConfigQ93bT316 = _SvcAtmConfigQ93bT316_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 11),
    _SvcAtmConfigQ93bT316_Type()
)
svcAtmConfigQ93bT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT316.setStatus("mandatory")
_SvcAtmConfigQ93bT322_Type = Integer32
_SvcAtmConfigQ93bT322_Object = MibTableColumn
svcAtmConfigQ93bT322 = _SvcAtmConfigQ93bT322_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 12),
    _SvcAtmConfigQ93bT322_Type()
)
svcAtmConfigQ93bT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT322.setStatus("mandatory")
_SvcAtmConfigQ93bT398_Type = Integer32
_SvcAtmConfigQ93bT398_Object = MibTableColumn
svcAtmConfigQ93bT398 = _SvcAtmConfigQ93bT398_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 13),
    _SvcAtmConfigQ93bT398_Type()
)
svcAtmConfigQ93bT398.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT398.setStatus("mandatory")
_SvcAtmConfigQ93bT399_Type = Integer32
_SvcAtmConfigQ93bT399_Object = MibTableColumn
svcAtmConfigQ93bT399 = _SvcAtmConfigQ93bT399_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 14),
    _SvcAtmConfigQ93bT399_Type()
)
svcAtmConfigQ93bT399.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bT399.setStatus("mandatory")
_SvcAtmConfigQ93bTotalConns_Type = Counter32
_SvcAtmConfigQ93bTotalConns_Object = MibTableColumn
svcAtmConfigQ93bTotalConns = _SvcAtmConfigQ93bTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 15),
    _SvcAtmConfigQ93bTotalConns_Type()
)
svcAtmConfigQ93bTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bTotalConns.setStatus("mandatory")
_SvcAtmConfigQ93bActiveConns_Type = Counter32
_SvcAtmConfigQ93bActiveConns_Object = MibTableColumn
svcAtmConfigQ93bActiveConns = _SvcAtmConfigQ93bActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 16),
    _SvcAtmConfigQ93bActiveConns_Type()
)
svcAtmConfigQ93bActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bActiveConns.setStatus("mandatory")


class _SvcAtmConfigQ93bLastCauseTx_Type(Integer32):
    """Custom type svcAtmConfigQ93bLastCauseTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              16,
              17,
              18,
              21,
              22,
              23,
              27,
              28,
              30,
              31,
              35,
              36,
              37,
              38,
              41,
              43,
              45,
              47,
              49,
              51,
              57,
              58,
              63,
              65,
              73,
              78,
              81,
              82,
              88,
              89,
              91,
              92,
              93,
              96,
              97,
              99,
              100,
              101,
              102,
              104,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("aal-params-unsupp-30", 93),
          ("aal-params-unsupp-31", 78),
          ("access-info-discard", 43),
          ("b-cap-not-authorized", 57),
          ("b-cap-not-implemented", 65),
          ("b-cap-unavailable", 58),
          ("call-reject", 21),
          ("call-reject-clir", 23),
          ("combination-unsupported", 73),
          ("dest-incompatible", 88),
          ("dest-out-of-order", 27),
          ("info-element-missing", 96),
          ("info-element-not-imp", 99),
          ("invalid-call-reference", 81),
          ("invalid-endpoint-ref", 89),
          ("invalid-info-element", 100),
          ("invalid-message-len", 104),
          ("invalid-nmb-format", 28),
          ("invalid-transit-net", 91),
          ("message-not-compatible", 101),
          ("msg-type-not-imp", 97),
          ("network-out-of-order", 38),
          ("nmb-changed", 22),
          ("no-channel", 82),
          ("no-route-dest", 3),
          ("no-route-transnet", 2),
          ("no-user-response", 18),
          ("no-vcc-available", 45),
          ("normal-call-clr-31", 16),
          ("normal-unspecified", 31),
          ("optional-element-error", 127),
          ("protocol-error", 111),
          ("qos-unavailable", 49),
          ("rate-unavail-31", 37),
          ("rate-unavailable-30", 51),
          ("req-vcc-unavailable", 35),
          ("resources-unavailable", 47),
          ("response-stat-enq", 30),
          ("service-unavailable", 63),
          ("temp-fail", 41),
          ("timer-recovery", 102),
          ("too-many-add-pty-req", 92),
          ("unalloc-nmb", 1),
          ("user-busy", 17),
          ("vcc-fail-31", 36),
          ("vcc-unacceptable-30", 10))
    )


_SvcAtmConfigQ93bLastCauseTx_Type.__name__ = "Integer32"
_SvcAtmConfigQ93bLastCauseTx_Object = MibTableColumn
svcAtmConfigQ93bLastCauseTx = _SvcAtmConfigQ93bLastCauseTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 17),
    _SvcAtmConfigQ93bLastCauseTx_Type()
)
svcAtmConfigQ93bLastCauseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bLastCauseTx.setStatus("mandatory")


class _SvcAtmConfigQ93bLastCauseRx_Type(Integer32):
    """Custom type svcAtmConfigQ93bLastCauseRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              16,
              17,
              18,
              21,
              22,
              23,
              27,
              28,
              30,
              31,
              35,
              36,
              37,
              38,
              41,
              43,
              45,
              47,
              49,
              51,
              57,
              58,
              63,
              65,
              73,
              78,
              81,
              82,
              88,
              89,
              91,
              92,
              93,
              96,
              97,
              99,
              100,
              101,
              102,
              104,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("aal-params-unsupp-30", 93),
          ("aal-params-unsupp-31", 78),
          ("access-info-discard", 43),
          ("b-cap-not-authorized", 57),
          ("b-cap-not-implemented", 65),
          ("b-cap-unavailable", 58),
          ("call-reject", 21),
          ("call-reject-clir", 23),
          ("combination-unsupported", 73),
          ("dest-incompatible", 88),
          ("dest-out-of-order", 27),
          ("info-element-missing", 96),
          ("info-element-not-imp", 99),
          ("invalid-call-reference", 81),
          ("invalid-endpoint-ref", 89),
          ("invalid-info-element", 100),
          ("invalid-message-len", 104),
          ("invalid-nmb-format", 28),
          ("invalid-transit-net", 91),
          ("message-not-compatible", 101),
          ("msg-type-not-imp", 97),
          ("network-out-of-order", 38),
          ("nmb-changed", 22),
          ("no-channel", 82),
          ("no-route-dest", 3),
          ("no-route-transnet", 2),
          ("no-user-response", 18),
          ("no-vcc-available", 45),
          ("normal-call-clr-31", 16),
          ("normal-unspecified", 31),
          ("optional-element-error", 127),
          ("protocol-error", 111),
          ("qos-unavailable", 49),
          ("rate-unavail-31", 37),
          ("rate-unavailable-30", 51),
          ("req-vcc-unavailable", 35),
          ("resources-unavailable", 47),
          ("response-stat-enq", 30),
          ("service-unavailable", 63),
          ("temp-fail", 41),
          ("timer-recovery", 102),
          ("too-many-add-pty-req", 92),
          ("unalloc-nmb", 1),
          ("user-busy", 17),
          ("vcc-fail-31", 36),
          ("vcc-unacceptable-30", 10))
    )


_SvcAtmConfigQ93bLastCauseRx_Type.__name__ = "Integer32"
_SvcAtmConfigQ93bLastCauseRx_Object = MibTableColumn
svcAtmConfigQ93bLastCauseRx = _SvcAtmConfigQ93bLastCauseRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 18),
    _SvcAtmConfigQ93bLastCauseRx_Type()
)
svcAtmConfigQ93bLastCauseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bLastCauseRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumSetupPduTx_Type = Counter32
_SvcAtmConfigQ93bNumSetupPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumSetupPduTx = _SvcAtmConfigQ93bNumSetupPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 19),
    _SvcAtmConfigQ93bNumSetupPduTx_Type()
)
svcAtmConfigQ93bNumSetupPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumSetupPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumSetupPduRx_Type = Counter32
_SvcAtmConfigQ93bNumSetupPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumSetupPduRx = _SvcAtmConfigQ93bNumSetupPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 20),
    _SvcAtmConfigQ93bNumSetupPduRx_Type()
)
svcAtmConfigQ93bNumSetupPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumSetupPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumCallProcPduTx_Type = Counter32
_SvcAtmConfigQ93bNumCallProcPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumCallProcPduTx = _SvcAtmConfigQ93bNumCallProcPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 21),
    _SvcAtmConfigQ93bNumCallProcPduTx_Type()
)
svcAtmConfigQ93bNumCallProcPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumCallProcPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumCallProcPduRx_Type = Counter32
_SvcAtmConfigQ93bNumCallProcPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumCallProcPduRx = _SvcAtmConfigQ93bNumCallProcPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 22),
    _SvcAtmConfigQ93bNumCallProcPduRx_Type()
)
svcAtmConfigQ93bNumCallProcPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumCallProcPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumConnectPduTx_Type = Counter32
_SvcAtmConfigQ93bNumConnectPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumConnectPduTx = _SvcAtmConfigQ93bNumConnectPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 23),
    _SvcAtmConfigQ93bNumConnectPduTx_Type()
)
svcAtmConfigQ93bNumConnectPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumConnectPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumConnectPduRx_Type = Counter32
_SvcAtmConfigQ93bNumConnectPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumConnectPduRx = _SvcAtmConfigQ93bNumConnectPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 24),
    _SvcAtmConfigQ93bNumConnectPduRx_Type()
)
svcAtmConfigQ93bNumConnectPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumConnectPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumConnectAckPduTx_Type = Counter32
_SvcAtmConfigQ93bNumConnectAckPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumConnectAckPduTx = _SvcAtmConfigQ93bNumConnectAckPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 25),
    _SvcAtmConfigQ93bNumConnectAckPduTx_Type()
)
svcAtmConfigQ93bNumConnectAckPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumConnectAckPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumConnectAckPduRx_Type = Counter32
_SvcAtmConfigQ93bNumConnectAckPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumConnectAckPduRx = _SvcAtmConfigQ93bNumConnectAckPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 26),
    _SvcAtmConfigQ93bNumConnectAckPduRx_Type()
)
svcAtmConfigQ93bNumConnectAckPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumConnectAckPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumReleasePduTx_Type = Counter32
_SvcAtmConfigQ93bNumReleasePduTx_Object = MibTableColumn
svcAtmConfigQ93bNumReleasePduTx = _SvcAtmConfigQ93bNumReleasePduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 27),
    _SvcAtmConfigQ93bNumReleasePduTx_Type()
)
svcAtmConfigQ93bNumReleasePduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumReleasePduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumReleasePduRx_Type = Counter32
_SvcAtmConfigQ93bNumReleasePduRx_Object = MibTableColumn
svcAtmConfigQ93bNumReleasePduRx = _SvcAtmConfigQ93bNumReleasePduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 28),
    _SvcAtmConfigQ93bNumReleasePduRx_Type()
)
svcAtmConfigQ93bNumReleasePduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumReleasePduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumReleaseCmpltPduTx_Type = Counter32
_SvcAtmConfigQ93bNumReleaseCmpltPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumReleaseCmpltPduTx = _SvcAtmConfigQ93bNumReleaseCmpltPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 29),
    _SvcAtmConfigQ93bNumReleaseCmpltPduTx_Type()
)
svcAtmConfigQ93bNumReleaseCmpltPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumReleaseCmpltPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumReleaseCmpltPduRx_Type = Counter32
_SvcAtmConfigQ93bNumReleaseCmpltPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumReleaseCmpltPduRx = _SvcAtmConfigQ93bNumReleaseCmpltPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 30),
    _SvcAtmConfigQ93bNumReleaseCmpltPduRx_Type()
)
svcAtmConfigQ93bNumReleaseCmpltPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumReleaseCmpltPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyPduTx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyPduTx = _SvcAtmConfigQ93bNumAddPtyPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 31),
    _SvcAtmConfigQ93bNumAddPtyPduTx_Type()
)
svcAtmConfigQ93bNumAddPtyPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyPduRx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyPduRx = _SvcAtmConfigQ93bNumAddPtyPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 32),
    _SvcAtmConfigQ93bNumAddPtyPduRx_Type()
)
svcAtmConfigQ93bNumAddPtyPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyAckPduTx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyAckPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyAckPduTx = _SvcAtmConfigQ93bNumAddPtyAckPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 33),
    _SvcAtmConfigQ93bNumAddPtyAckPduTx_Type()
)
svcAtmConfigQ93bNumAddPtyAckPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyAckPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyAckPduRx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyAckPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyAckPduRx = _SvcAtmConfigQ93bNumAddPtyAckPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 34),
    _SvcAtmConfigQ93bNumAddPtyAckPduRx_Type()
)
svcAtmConfigQ93bNumAddPtyAckPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyAckPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyRejPduTx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyRejPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyRejPduTx = _SvcAtmConfigQ93bNumAddPtyRejPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 35),
    _SvcAtmConfigQ93bNumAddPtyRejPduTx_Type()
)
svcAtmConfigQ93bNumAddPtyRejPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyRejPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumAddPtyRejPduRx_Type = Counter32
_SvcAtmConfigQ93bNumAddPtyRejPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumAddPtyRejPduRx = _SvcAtmConfigQ93bNumAddPtyRejPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 36),
    _SvcAtmConfigQ93bNumAddPtyRejPduRx_Type()
)
svcAtmConfigQ93bNumAddPtyRejPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumAddPtyRejPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumDropPtyPduTx_Type = Counter32
_SvcAtmConfigQ93bNumDropPtyPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumDropPtyPduTx = _SvcAtmConfigQ93bNumDropPtyPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 37),
    _SvcAtmConfigQ93bNumDropPtyPduTx_Type()
)
svcAtmConfigQ93bNumDropPtyPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumDropPtyPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumDropPtyPduRx_Type = Counter32
_SvcAtmConfigQ93bNumDropPtyPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumDropPtyPduRx = _SvcAtmConfigQ93bNumDropPtyPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 38),
    _SvcAtmConfigQ93bNumDropPtyPduRx_Type()
)
svcAtmConfigQ93bNumDropPtyPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumDropPtyPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumDropPtyAckPduTx_Type = Counter32
_SvcAtmConfigQ93bNumDropPtyAckPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumDropPtyAckPduTx = _SvcAtmConfigQ93bNumDropPtyAckPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 39),
    _SvcAtmConfigQ93bNumDropPtyAckPduTx_Type()
)
svcAtmConfigQ93bNumDropPtyAckPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumDropPtyAckPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumDropPtyAckPduRx_Type = Counter32
_SvcAtmConfigQ93bNumDropPtyAckPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumDropPtyAckPduRx = _SvcAtmConfigQ93bNumDropPtyAckPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 40),
    _SvcAtmConfigQ93bNumDropPtyAckPduRx_Type()
)
svcAtmConfigQ93bNumDropPtyAckPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumDropPtyAckPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumStatusEnqPduTx_Type = Counter32
_SvcAtmConfigQ93bNumStatusEnqPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumStatusEnqPduTx = _SvcAtmConfigQ93bNumStatusEnqPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 41),
    _SvcAtmConfigQ93bNumStatusEnqPduTx_Type()
)
svcAtmConfigQ93bNumStatusEnqPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumStatusEnqPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumStatusEnqPduRx_Type = Counter32
_SvcAtmConfigQ93bNumStatusEnqPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumStatusEnqPduRx = _SvcAtmConfigQ93bNumStatusEnqPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 42),
    _SvcAtmConfigQ93bNumStatusEnqPduRx_Type()
)
svcAtmConfigQ93bNumStatusEnqPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumStatusEnqPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumStatusPduTx_Type = Counter32
_SvcAtmConfigQ93bNumStatusPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumStatusPduTx = _SvcAtmConfigQ93bNumStatusPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 43),
    _SvcAtmConfigQ93bNumStatusPduTx_Type()
)
svcAtmConfigQ93bNumStatusPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumStatusPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumStatusPduRx_Type = Counter32
_SvcAtmConfigQ93bNumStatusPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumStatusPduRx = _SvcAtmConfigQ93bNumStatusPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 44),
    _SvcAtmConfigQ93bNumStatusPduRx_Type()
)
svcAtmConfigQ93bNumStatusPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumStatusPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumRestartPduTx_Type = Counter32
_SvcAtmConfigQ93bNumRestartPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumRestartPduTx = _SvcAtmConfigQ93bNumRestartPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 45),
    _SvcAtmConfigQ93bNumRestartPduTx_Type()
)
svcAtmConfigQ93bNumRestartPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumRestartPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumRestartPduRx_Type = Counter32
_SvcAtmConfigQ93bNumRestartPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumRestartPduRx = _SvcAtmConfigQ93bNumRestartPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 46),
    _SvcAtmConfigQ93bNumRestartPduRx_Type()
)
svcAtmConfigQ93bNumRestartPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumRestartPduRx.setStatus("mandatory")
_SvcAtmConfigQ93bNumRestartAckPduTx_Type = Counter32
_SvcAtmConfigQ93bNumRestartAckPduTx_Object = MibTableColumn
svcAtmConfigQ93bNumRestartAckPduTx = _SvcAtmConfigQ93bNumRestartAckPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 47),
    _SvcAtmConfigQ93bNumRestartAckPduTx_Type()
)
svcAtmConfigQ93bNumRestartAckPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumRestartAckPduTx.setStatus("mandatory")
_SvcAtmConfigQ93bNumRestartAckPduRx_Type = Counter32
_SvcAtmConfigQ93bNumRestartAckPduRx_Object = MibTableColumn
svcAtmConfigQ93bNumRestartAckPduRx = _SvcAtmConfigQ93bNumRestartAckPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 48),
    _SvcAtmConfigQ93bNumRestartAckPduRx_Type()
)
svcAtmConfigQ93bNumRestartAckPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQ93bNumRestartAckPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalMaxCC_Type = Integer32
_SvcAtmConfigQSaalMaxCC_Object = MibTableColumn
svcAtmConfigQSaalMaxCC = _SvcAtmConfigQSaalMaxCC_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 49),
    _SvcAtmConfigQSaalMaxCC_Type()
)
svcAtmConfigQSaalMaxCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalMaxCC.setStatus("mandatory")
_SvcAtmConfigQSaalMaxPD_Type = Integer32
_SvcAtmConfigQSaalMaxPD_Object = MibTableColumn
svcAtmConfigQSaalMaxPD = _SvcAtmConfigQSaalMaxPD_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 50),
    _SvcAtmConfigQSaalMaxPD_Type()
)
svcAtmConfigQSaalMaxPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalMaxPD.setStatus("mandatory")
_SvcAtmConfigQSaalMaxStat_Type = Integer32
_SvcAtmConfigQSaalMaxStat_Object = MibTableColumn
svcAtmConfigQSaalMaxStat = _SvcAtmConfigQSaalMaxStat_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 51),
    _SvcAtmConfigQSaalMaxStat_Type()
)
svcAtmConfigQSaalMaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalMaxStat.setStatus("mandatory")
_SvcAtmConfigQSaalTPoll_Type = Integer32
_SvcAtmConfigQSaalTPoll_Object = MibTableColumn
svcAtmConfigQSaalTPoll = _SvcAtmConfigQSaalTPoll_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 52),
    _SvcAtmConfigQSaalTPoll_Type()
)
svcAtmConfigQSaalTPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalTPoll.setStatus("mandatory")
_SvcAtmConfigQSaalTKeepalive_Type = Integer32
_SvcAtmConfigQSaalTKeepalive_Object = MibTableColumn
svcAtmConfigQSaalTKeepalive = _SvcAtmConfigQSaalTKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 53),
    _SvcAtmConfigQSaalTKeepalive_Type()
)
svcAtmConfigQSaalTKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalTKeepalive.setStatus("mandatory")
_SvcAtmConfigQSaalTNoResponse_Type = Integer32
_SvcAtmConfigQSaalTNoResponse_Object = MibTableColumn
svcAtmConfigQSaalTNoResponse = _SvcAtmConfigQSaalTNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 54),
    _SvcAtmConfigQSaalTNoResponse_Type()
)
svcAtmConfigQSaalTNoResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalTNoResponse.setStatus("mandatory")
_SvcAtmConfigQSaalTCC_Type = Integer32
_SvcAtmConfigQSaalTCC_Object = MibTableColumn
svcAtmConfigQSaalTCC = _SvcAtmConfigQSaalTCC_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 55),
    _SvcAtmConfigQSaalTCC_Type()
)
svcAtmConfigQSaalTCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalTCC.setStatus("mandatory")
_SvcAtmConfigQSaalTIdle_Type = Integer32
_SvcAtmConfigQSaalTIdle_Object = MibTableColumn
svcAtmConfigQSaalTIdle = _SvcAtmConfigQSaalTIdle_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 56),
    _SvcAtmConfigQSaalTIdle_Type()
)
svcAtmConfigQSaalTIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalTIdle.setStatus("mandatory")
_SvcAtmConfigQSaalNumDiscardTx_Type = Counter32
_SvcAtmConfigQSaalNumDiscardTx_Object = MibTableColumn
svcAtmConfigQSaalNumDiscardTx = _SvcAtmConfigQSaalNumDiscardTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 57),
    _SvcAtmConfigQSaalNumDiscardTx_Type()
)
svcAtmConfigQSaalNumDiscardTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumDiscardTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumDiscardRx_Type = Counter32
_SvcAtmConfigQSaalNumDiscardRx_Object = MibTableColumn
svcAtmConfigQSaalNumDiscardRx = _SvcAtmConfigQSaalNumDiscardRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 58),
    _SvcAtmConfigQSaalNumDiscardRx_Type()
)
svcAtmConfigQSaalNumDiscardRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumDiscardRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErrorTx_Type = Counter32
_SvcAtmConfigQSaalNumErrorTx_Object = MibTableColumn
svcAtmConfigQSaalNumErrorTx = _SvcAtmConfigQSaalNumErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 59),
    _SvcAtmConfigQSaalNumErrorTx_Type()
)
svcAtmConfigQSaalNumErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErrorTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErrorRx_Type = Counter32
_SvcAtmConfigQSaalNumErrorRx_Object = MibTableColumn
svcAtmConfigQSaalNumErrorRx = _SvcAtmConfigQSaalNumErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 60),
    _SvcAtmConfigQSaalNumErrorRx_Type()
)
svcAtmConfigQSaalNumErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErrorRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgnPduTx_Type = Counter32
_SvcAtmConfigQSaalNumBgnPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumBgnPduTx = _SvcAtmConfigQSaalNumBgnPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 61),
    _SvcAtmConfigQSaalNumBgnPduTx_Type()
)
svcAtmConfigQSaalNumBgnPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgnPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgnPduRx_Type = Counter32
_SvcAtmConfigQSaalNumBgnPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumBgnPduRx = _SvcAtmConfigQSaalNumBgnPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 62),
    _SvcAtmConfigQSaalNumBgnPduRx_Type()
)
svcAtmConfigQSaalNumBgnPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgnPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgakPduTx_Type = Counter32
_SvcAtmConfigQSaalNumBgakPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumBgakPduTx = _SvcAtmConfigQSaalNumBgakPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 63),
    _SvcAtmConfigQSaalNumBgakPduTx_Type()
)
svcAtmConfigQSaalNumBgakPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgakPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgakPduRx_Type = Counter32
_SvcAtmConfigQSaalNumBgakPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumBgakPduRx = _SvcAtmConfigQSaalNumBgakPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 64),
    _SvcAtmConfigQSaalNumBgakPduRx_Type()
)
svcAtmConfigQSaalNumBgakPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgakPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgrejPduTx_Type = Counter32
_SvcAtmConfigQSaalNumBgrejPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumBgrejPduTx = _SvcAtmConfigQSaalNumBgrejPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 65),
    _SvcAtmConfigQSaalNumBgrejPduTx_Type()
)
svcAtmConfigQSaalNumBgrejPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgrejPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumBgrejPduRx_Type = Counter32
_SvcAtmConfigQSaalNumBgrejPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumBgrejPduRx = _SvcAtmConfigQSaalNumBgrejPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 66),
    _SvcAtmConfigQSaalNumBgrejPduRx_Type()
)
svcAtmConfigQSaalNumBgrejPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumBgrejPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumEndPduTx_Type = Counter32
_SvcAtmConfigQSaalNumEndPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumEndPduTx = _SvcAtmConfigQSaalNumEndPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 67),
    _SvcAtmConfigQSaalNumEndPduTx_Type()
)
svcAtmConfigQSaalNumEndPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumEndPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumEndPduRx_Type = Counter32
_SvcAtmConfigQSaalNumEndPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumEndPduRx = _SvcAtmConfigQSaalNumEndPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 68),
    _SvcAtmConfigQSaalNumEndPduRx_Type()
)
svcAtmConfigQSaalNumEndPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumEndPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumEndakPduTx_Type = Counter32
_SvcAtmConfigQSaalNumEndakPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumEndakPduTx = _SvcAtmConfigQSaalNumEndakPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 69),
    _SvcAtmConfigQSaalNumEndakPduTx_Type()
)
svcAtmConfigQSaalNumEndakPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumEndakPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumEndakPduRx_Type = Counter32
_SvcAtmConfigQSaalNumEndakPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumEndakPduRx = _SvcAtmConfigQSaalNumEndakPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 70),
    _SvcAtmConfigQSaalNumEndakPduRx_Type()
)
svcAtmConfigQSaalNumEndakPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumEndakPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumRsPduTx_Type = Counter32
_SvcAtmConfigQSaalNumRsPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumRsPduTx = _SvcAtmConfigQSaalNumRsPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 71),
    _SvcAtmConfigQSaalNumRsPduTx_Type()
)
svcAtmConfigQSaalNumRsPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumRsPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumRsPduRx_Type = Counter32
_SvcAtmConfigQSaalNumRsPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumRsPduRx = _SvcAtmConfigQSaalNumRsPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 72),
    _SvcAtmConfigQSaalNumRsPduRx_Type()
)
svcAtmConfigQSaalNumRsPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumRsPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumRsakPduTx_Type = Counter32
_SvcAtmConfigQSaalNumRsakPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumRsakPduTx = _SvcAtmConfigQSaalNumRsakPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 73),
    _SvcAtmConfigQSaalNumRsakPduTx_Type()
)
svcAtmConfigQSaalNumRsakPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumRsakPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumRsakPduRx_Type = Counter32
_SvcAtmConfigQSaalNumRsakPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumRsakPduRx = _SvcAtmConfigQSaalNumRsakPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 74),
    _SvcAtmConfigQSaalNumRsakPduRx_Type()
)
svcAtmConfigQSaalNumRsakPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumRsakPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErPduTx_Type = Counter32
_SvcAtmConfigQSaalNumErPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumErPduTx = _SvcAtmConfigQSaalNumErPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 75),
    _SvcAtmConfigQSaalNumErPduTx_Type()
)
svcAtmConfigQSaalNumErPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErPduRx_Type = Counter32
_SvcAtmConfigQSaalNumErPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumErPduRx = _SvcAtmConfigQSaalNumErPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 76),
    _SvcAtmConfigQSaalNumErPduRx_Type()
)
svcAtmConfigQSaalNumErPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErakPduTx_Type = Counter32
_SvcAtmConfigQSaalNumErakPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumErakPduTx = _SvcAtmConfigQSaalNumErakPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 77),
    _SvcAtmConfigQSaalNumErakPduTx_Type()
)
svcAtmConfigQSaalNumErakPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErakPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumErakPduRx_Type = Counter32
_SvcAtmConfigQSaalNumErakPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumErakPduRx = _SvcAtmConfigQSaalNumErakPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 78),
    _SvcAtmConfigQSaalNumErakPduRx_Type()
)
svcAtmConfigQSaalNumErakPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumErakPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumSdPduTx_Type = Counter32
_SvcAtmConfigQSaalNumSdPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumSdPduTx = _SvcAtmConfigQSaalNumSdPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 79),
    _SvcAtmConfigQSaalNumSdPduTx_Type()
)
svcAtmConfigQSaalNumSdPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumSdPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumSdPduRx_Type = Counter32
_SvcAtmConfigQSaalNumSdPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumSdPduRx = _SvcAtmConfigQSaalNumSdPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 80),
    _SvcAtmConfigQSaalNumSdPduRx_Type()
)
svcAtmConfigQSaalNumSdPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumSdPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumPollPduTx_Type = Counter32
_SvcAtmConfigQSaalNumPollPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumPollPduTx = _SvcAtmConfigQSaalNumPollPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 81),
    _SvcAtmConfigQSaalNumPollPduTx_Type()
)
svcAtmConfigQSaalNumPollPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumPollPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumPollPduRx_Type = Counter32
_SvcAtmConfigQSaalNumPollPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumPollPduRx = _SvcAtmConfigQSaalNumPollPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 82),
    _SvcAtmConfigQSaalNumPollPduRx_Type()
)
svcAtmConfigQSaalNumPollPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumPollPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumStatPduTx_Type = Counter32
_SvcAtmConfigQSaalNumStatPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumStatPduTx = _SvcAtmConfigQSaalNumStatPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 83),
    _SvcAtmConfigQSaalNumStatPduTx_Type()
)
svcAtmConfigQSaalNumStatPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumStatPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumStatPduRx_Type = Counter32
_SvcAtmConfigQSaalNumStatPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumStatPduRx = _SvcAtmConfigQSaalNumStatPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 84),
    _SvcAtmConfigQSaalNumStatPduRx_Type()
)
svcAtmConfigQSaalNumStatPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumStatPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumUstatPduTx_Type = Counter32
_SvcAtmConfigQSaalNumUstatPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumUstatPduTx = _SvcAtmConfigQSaalNumUstatPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 85),
    _SvcAtmConfigQSaalNumUstatPduTx_Type()
)
svcAtmConfigQSaalNumUstatPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumUstatPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumUstatPduRx_Type = Counter32
_SvcAtmConfigQSaalNumUstatPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumUstatPduRx = _SvcAtmConfigQSaalNumUstatPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 86),
    _SvcAtmConfigQSaalNumUstatPduRx_Type()
)
svcAtmConfigQSaalNumUstatPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumUstatPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumUdPduTx_Type = Counter32
_SvcAtmConfigQSaalNumUdPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumUdPduTx = _SvcAtmConfigQSaalNumUdPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 87),
    _SvcAtmConfigQSaalNumUdPduTx_Type()
)
svcAtmConfigQSaalNumUdPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumUdPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumUdPduRx_Type = Counter32
_SvcAtmConfigQSaalNumUdPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumUdPduRx = _SvcAtmConfigQSaalNumUdPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 88),
    _SvcAtmConfigQSaalNumUdPduRx_Type()
)
svcAtmConfigQSaalNumUdPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumUdPduRx.setStatus("mandatory")
_SvcAtmConfigQSaalNumMdPduTx_Type = Counter32
_SvcAtmConfigQSaalNumMdPduTx_Object = MibTableColumn
svcAtmConfigQSaalNumMdPduTx = _SvcAtmConfigQSaalNumMdPduTx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 89),
    _SvcAtmConfigQSaalNumMdPduTx_Type()
)
svcAtmConfigQSaalNumMdPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumMdPduTx.setStatus("mandatory")
_SvcAtmConfigQSaalNumMdPduRx_Type = Counter32
_SvcAtmConfigQSaalNumMdPduRx_Object = MibTableColumn
svcAtmConfigQSaalNumMdPduRx = _SvcAtmConfigQSaalNumMdPduRx_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 2, 1, 90),
    _SvcAtmConfigQSaalNumMdPduRx_Type()
)
svcAtmConfigQSaalNumMdPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmConfigQSaalNumMdPduRx.setStatus("mandatory")
_SvcAtmFailedCallTable_Object = MibTable
svcAtmFailedCallTable = _SvcAtmFailedCallTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3)
)
if mibBuilder.loadTexts:
    svcAtmFailedCallTable.setStatus("mandatory")
_SvcAtmFailedCallEntry_Object = MibTableRow
svcAtmFailedCallEntry = _SvcAtmFailedCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1)
)
svcAtmFailedCallEntry.setIndexNames(
    (0, "CASCADE-MIB", "svcAtmFailedCallIfIndex"),
    (0, "CASCADE-MIB", "svcAtmFailedCallIndex"),
)
if mibBuilder.loadTexts:
    svcAtmFailedCallEntry.setStatus("mandatory")
_SvcAtmFailedCallIfIndex_Type = Index
_SvcAtmFailedCallIfIndex_Object = MibTableColumn
svcAtmFailedCallIfIndex = _SvcAtmFailedCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 1),
    _SvcAtmFailedCallIfIndex_Type()
)
svcAtmFailedCallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallIfIndex.setStatus("mandatory")
_SvcAtmFailedCallIndex_Type = Integer32
_SvcAtmFailedCallIndex_Object = MibTableColumn
svcAtmFailedCallIndex = _SvcAtmFailedCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 2),
    _SvcAtmFailedCallIndex_Type()
)
svcAtmFailedCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallIndex.setStatus("mandatory")


class _SvcAtmFailedCallDirection_Type(Integer32):
    """Custom type svcAtmFailedCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callee", 2),
          ("caller", 1))
    )


_SvcAtmFailedCallDirection_Type.__name__ = "Integer32"
_SvcAtmFailedCallDirection_Object = MibTableColumn
svcAtmFailedCallDirection = _SvcAtmFailedCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 3),
    _SvcAtmFailedCallDirection_Type()
)
svcAtmFailedCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallDirection.setStatus("mandatory")


class _SvcAtmFailedCallPduType_Type(Integer32):
    """Custom type svcAtmFailedCallPduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addPartyReject", 2),
          ("dropParty", 3),
          ("release", 1))
    )


_SvcAtmFailedCallPduType_Type.__name__ = "Integer32"
_SvcAtmFailedCallPduType_Object = MibTableColumn
svcAtmFailedCallPduType = _SvcAtmFailedCallPduType_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 4),
    _SvcAtmFailedCallPduType_Type()
)
svcAtmFailedCallPduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallPduType.setStatus("mandatory")


class _SvcAtmFailedCallPduDirection_Type(Integer32):
    """Custom type svcAtmFailedCallPduDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("received", 2),
          ("transmitted", 1))
    )


_SvcAtmFailedCallPduDirection_Type.__name__ = "Integer32"
_SvcAtmFailedCallPduDirection_Object = MibTableColumn
svcAtmFailedCallPduDirection = _SvcAtmFailedCallPduDirection_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 5),
    _SvcAtmFailedCallPduDirection_Type()
)
svcAtmFailedCallPduDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallPduDirection.setStatus("mandatory")


class _SvcAtmFailedCallCause_Type(Integer32):
    """Custom type svcAtmFailedCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              16,
              17,
              18,
              21,
              22,
              23,
              27,
              28,
              30,
              31,
              35,
              36,
              37,
              38,
              41,
              43,
              45,
              47,
              49,
              51,
              57,
              58,
              63,
              65,
              73,
              78,
              81,
              82,
              88,
              89,
              91,
              92,
              93,
              96,
              97,
              99,
              100,
              101,
              102,
              104,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("aal-params-unsupp-30", 93),
          ("aal-params-unsupp-31", 78),
          ("access-info-discard", 43),
          ("b-cap-not-authorized", 57),
          ("b-cap-not-implemented", 65),
          ("b-cap-unavailable", 58),
          ("call-reject", 21),
          ("call-reject-clir", 23),
          ("combination-unsupported", 73),
          ("dest-incompatible", 88),
          ("dest-out-of-order", 27),
          ("info-element-missing", 96),
          ("info-element-not-imp", 99),
          ("invalid-call-reference", 81),
          ("invalid-endpoint-ref", 89),
          ("invalid-info-element", 100),
          ("invalid-message-len", 104),
          ("invalid-nmb-format", 28),
          ("invalid-transit-net", 91),
          ("message-not-compatible", 101),
          ("msg-type-not-imp", 97),
          ("network-out-of-order", 38),
          ("nmb-changed", 22),
          ("no-channel", 82),
          ("no-route-dest", 3),
          ("no-route-transnet", 2),
          ("no-user-response", 18),
          ("no-vcc-available", 45),
          ("normal-call-clr-31", 16),
          ("normal-unspecified", 31),
          ("optional-element-error", 127),
          ("protocol-error", 111),
          ("qos-unavailable", 49),
          ("rate-unavail-31", 37),
          ("rate-unavailable-30", 51),
          ("req-vcc-unavailable", 35),
          ("resources-unavailable", 47),
          ("response-stat-enq", 30),
          ("service-unavailable", 63),
          ("temp-fail", 41),
          ("timer-recovery", 102),
          ("too-many-add-pty-req", 92),
          ("unalloc-nmb", 1),
          ("user-busy", 17),
          ("vcc-fail-31", 36),
          ("vcc-unacceptable-30", 10))
    )


_SvcAtmFailedCallCause_Type.__name__ = "Integer32"
_SvcAtmFailedCallCause_Object = MibTableColumn
svcAtmFailedCallCause = _SvcAtmFailedCallCause_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 6),
    _SvcAtmFailedCallCause_Type()
)
svcAtmFailedCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallCause.setStatus("mandatory")


class _SvcAtmFailedCallLocation_Type(Integer32):
    """Custom type svcAtmFailedCallLocation based on Integer32"""
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
        *(("intlNet", 7),
          ("netBeyondInterwkPt", 8),
          ("privNetServLocal", 2),
          ("privNetServRemote", 6),
          ("pubNetServLocal", 3),
          ("pubNetServRemote", 5),
          ("transitNet", 4),
          ("user", 1))
    )


_SvcAtmFailedCallLocation_Type.__name__ = "Integer32"
_SvcAtmFailedCallLocation_Object = MibTableColumn
svcAtmFailedCallLocation = _SvcAtmFailedCallLocation_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 7),
    _SvcAtmFailedCallLocation_Type()
)
svcAtmFailedCallLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallLocation.setStatus("mandatory")
_SvcAtmFailedCallDiagnostic_Type = OctetString
_SvcAtmFailedCallDiagnostic_Object = MibTableColumn
svcAtmFailedCallDiagnostic = _SvcAtmFailedCallDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 8),
    _SvcAtmFailedCallDiagnostic_Type()
)
svcAtmFailedCallDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallDiagnostic.setStatus("mandatory")
_SvcAtmFailedCallCreationTime_Type = TimeTicks
_SvcAtmFailedCallCreationTime_Object = MibTableColumn
svcAtmFailedCallCreationTime = _SvcAtmFailedCallCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 9),
    _SvcAtmFailedCallCreationTime_Type()
)
svcAtmFailedCallCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallCreationTime.setStatus("mandatory")
_SvcAtmFailedCallTerminationTime_Type = TimeTicks
_SvcAtmFailedCallTerminationTime_Object = MibTableColumn
svcAtmFailedCallTerminationTime = _SvcAtmFailedCallTerminationTime_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 10),
    _SvcAtmFailedCallTerminationTime_Type()
)
svcAtmFailedCallTerminationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallTerminationTime.setStatus("mandatory")
_SvcAtmFailedCallFailureNodeId_Type = Integer32
_SvcAtmFailedCallFailureNodeId_Object = MibTableColumn
svcAtmFailedCallFailureNodeId = _SvcAtmFailedCallFailureNodeId_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 11),
    _SvcAtmFailedCallFailureNodeId_Type()
)
svcAtmFailedCallFailureNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallFailureNodeId.setStatus("mandatory")
_SvcAtmFailedCallFailureIfIndex_Type = Index
_SvcAtmFailedCallFailureIfIndex_Object = MibTableColumn
svcAtmFailedCallFailureIfIndex = _SvcAtmFailedCallFailureIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 12),
    _SvcAtmFailedCallFailureIfIndex_Type()
)
svcAtmFailedCallFailureIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallFailureIfIndex.setStatus("mandatory")
_SvcAtmFailedCallCallingParty_Type = OctetString
_SvcAtmFailedCallCallingParty_Object = MibTableColumn
svcAtmFailedCallCallingParty = _SvcAtmFailedCallCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 13),
    _SvcAtmFailedCallCallingParty_Type()
)
svcAtmFailedCallCallingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallCallingParty.setStatus("mandatory")
_SvcAtmFailedCallCalledParty_Type = OctetString
_SvcAtmFailedCallCalledParty_Object = MibTableColumn
svcAtmFailedCallCalledParty = _SvcAtmFailedCallCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 14),
    _SvcAtmFailedCallCalledParty_Type()
)
svcAtmFailedCallCalledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallCalledParty.setStatus("mandatory")


class _SvcAtmFailedCallAtmTfdType_Type(Integer32):
    """Custom type svcAtmFailedCallAtmTfdType based on Integer32"""
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
        *(("pcr-0-01", 1),
          ("pcr-0-01-tag", 2),
          ("pcr-01", 5),
          ("pcr-01-bestEffort", 7),
          ("pcr-01-scr-0-mbs-0", 3),
          ("pcr-01-scr-0-mbs-0-tag", 4),
          ("pcr-01-scr-01-mbs-01", 6),
          ("unknown", 8))
    )


_SvcAtmFailedCallAtmTfdType_Type.__name__ = "Integer32"
_SvcAtmFailedCallAtmTfdType_Object = MibTableColumn
svcAtmFailedCallAtmTfdType = _SvcAtmFailedCallAtmTfdType_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 15),
    _SvcAtmFailedCallAtmTfdType_Type()
)
svcAtmFailedCallAtmTfdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmTfdType.setStatus("mandatory")
_SvcAtmFailedCallAtmTfdParam1_Type = Integer32
_SvcAtmFailedCallAtmTfdParam1_Object = MibTableColumn
svcAtmFailedCallAtmTfdParam1 = _SvcAtmFailedCallAtmTfdParam1_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 16),
    _SvcAtmFailedCallAtmTfdParam1_Type()
)
svcAtmFailedCallAtmTfdParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmTfdParam1.setStatus("mandatory")
_SvcAtmFailedCallAtmTfdParam2_Type = Integer32
_SvcAtmFailedCallAtmTfdParam2_Object = MibTableColumn
svcAtmFailedCallAtmTfdParam2 = _SvcAtmFailedCallAtmTfdParam2_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 17),
    _SvcAtmFailedCallAtmTfdParam2_Type()
)
svcAtmFailedCallAtmTfdParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmTfdParam2.setStatus("mandatory")
_SvcAtmFailedCallAtmTfdParam3_Type = Integer32
_SvcAtmFailedCallAtmTfdParam3_Object = MibTableColumn
svcAtmFailedCallAtmTfdParam3 = _SvcAtmFailedCallAtmTfdParam3_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 18),
    _SvcAtmFailedCallAtmTfdParam3_Type()
)
svcAtmFailedCallAtmTfdParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmTfdParam3.setStatus("mandatory")
_SvcAtmFailedCallAtmQosClass_Type = Integer32
_SvcAtmFailedCallAtmQosClass_Object = MibTableColumn
svcAtmFailedCallAtmQosClass = _SvcAtmFailedCallAtmQosClass_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 19),
    _SvcAtmFailedCallAtmQosClass_Type()
)
svcAtmFailedCallAtmQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmQosClass.setStatus("mandatory")


class _SvcAtmFailedCallAtmRTfdType_Type(Integer32):
    """Custom type svcAtmFailedCallAtmRTfdType based on Integer32"""
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
        *(("pcr-0-01", 1),
          ("pcr-0-01-tag", 2),
          ("pcr-01", 5),
          ("pcr-01-bestEffort", 7),
          ("pcr-01-scr-0-mbs-0", 3),
          ("pcr-01-scr-0-mbs-0-tag", 4),
          ("pcr-01-scr-01-mbs-01", 6),
          ("unknown", 8))
    )


_SvcAtmFailedCallAtmRTfdType_Type.__name__ = "Integer32"
_SvcAtmFailedCallAtmRTfdType_Object = MibTableColumn
svcAtmFailedCallAtmRTfdType = _SvcAtmFailedCallAtmRTfdType_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 20),
    _SvcAtmFailedCallAtmRTfdType_Type()
)
svcAtmFailedCallAtmRTfdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmRTfdType.setStatus("mandatory")
_SvcAtmFailedCallAtmRTfdParam1_Type = Integer32
_SvcAtmFailedCallAtmRTfdParam1_Object = MibTableColumn
svcAtmFailedCallAtmRTfdParam1 = _SvcAtmFailedCallAtmRTfdParam1_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 21),
    _SvcAtmFailedCallAtmRTfdParam1_Type()
)
svcAtmFailedCallAtmRTfdParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmRTfdParam1.setStatus("mandatory")
_SvcAtmFailedCallAtmRTfdParam2_Type = Integer32
_SvcAtmFailedCallAtmRTfdParam2_Object = MibTableColumn
svcAtmFailedCallAtmRTfdParam2 = _SvcAtmFailedCallAtmRTfdParam2_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 22),
    _SvcAtmFailedCallAtmRTfdParam2_Type()
)
svcAtmFailedCallAtmRTfdParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmRTfdParam2.setStatus("mandatory")
_SvcAtmFailedCallAtmRTfdParam3_Type = Integer32
_SvcAtmFailedCallAtmRTfdParam3_Object = MibTableColumn
svcAtmFailedCallAtmRTfdParam3 = _SvcAtmFailedCallAtmRTfdParam3_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 23),
    _SvcAtmFailedCallAtmRTfdParam3_Type()
)
svcAtmFailedCallAtmRTfdParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmRTfdParam3.setStatus("mandatory")
_SvcAtmFailedCallAtmRQoSClass_Type = Integer32
_SvcAtmFailedCallAtmRQoSClass_Object = MibTableColumn
svcAtmFailedCallAtmRQoSClass = _SvcAtmFailedCallAtmRQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 24),
    _SvcAtmFailedCallAtmRQoSClass_Type()
)
svcAtmFailedCallAtmRQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAtmRQoSClass.setStatus("mandatory")


class _SvcAtmFailedCallBBearerClass_Type(Integer32):
    """Custom type svcAtmFailedCallBBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              16)
        )
    )
    namedValues = NamedValues(
        *(("class-A", 1),
          ("class-C", 3),
          ("class-X", 16))
    )


_SvcAtmFailedCallBBearerClass_Type.__name__ = "Integer32"
_SvcAtmFailedCallBBearerClass_Object = MibTableColumn
svcAtmFailedCallBBearerClass = _SvcAtmFailedCallBBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 25),
    _SvcAtmFailedCallBBearerClass_Type()
)
svcAtmFailedCallBBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallBBearerClass.setStatus("mandatory")


class _SvcAtmFailedCallBBearerTfcType_Type(Integer32):
    """Custom type svcAtmFailedCallBBearerTfcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("notIndicated", 1),
          ("vbr", 3))
    )


_SvcAtmFailedCallBBearerTfcType_Type.__name__ = "Integer32"
_SvcAtmFailedCallBBearerTfcType_Object = MibTableColumn
svcAtmFailedCallBBearerTfcType = _SvcAtmFailedCallBBearerTfcType_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 26),
    _SvcAtmFailedCallBBearerTfcType_Type()
)
svcAtmFailedCallBBearerTfcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallBBearerTfcType.setStatus("mandatory")


class _SvcAtmFailedCallBBearerTmgRqmt_Type(Integer32):
    """Custom type svcAtmFailedCallBBearerTmgRqmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-required", 3),
          ("notIndicated", 1),
          ("required", 2))
    )


_SvcAtmFailedCallBBearerTmgRqmt_Type.__name__ = "Integer32"
_SvcAtmFailedCallBBearerTmgRqmt_Object = MibTableColumn
svcAtmFailedCallBBearerTmgRqmt = _SvcAtmFailedCallBBearerTmgRqmt_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 27),
    _SvcAtmFailedCallBBearerTmgRqmt_Type()
)
svcAtmFailedCallBBearerTmgRqmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallBBearerTmgRqmt.setStatus("mandatory")


class _SvcAtmFailedCallBBearerUplaneCfg_Type(Integer32):
    """Custom type svcAtmFailedCallBBearerUplaneCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-multipoint", 2),
          ("point-point", 1))
    )


_SvcAtmFailedCallBBearerUplaneCfg_Type.__name__ = "Integer32"
_SvcAtmFailedCallBBearerUplaneCfg_Object = MibTableColumn
svcAtmFailedCallBBearerUplaneCfg = _SvcAtmFailedCallBBearerUplaneCfg_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 28),
    _SvcAtmFailedCallBBearerUplaneCfg_Type()
)
svcAtmFailedCallBBearerUplaneCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallBBearerUplaneCfg.setStatus("mandatory")


class _SvcAtmFailedCallBBearerClippingSusc_Type(Integer32):
    """Custom type svcAtmFailedCallBBearerClippingSusc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-susceptible", 1),
          ("susceptible", 2))
    )


_SvcAtmFailedCallBBearerClippingSusc_Type.__name__ = "Integer32"
_SvcAtmFailedCallBBearerClippingSusc_Object = MibTableColumn
svcAtmFailedCallBBearerClippingSusc = _SvcAtmFailedCallBBearerClippingSusc_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 29),
    _SvcAtmFailedCallBBearerClippingSusc_Type()
)
svcAtmFailedCallBBearerClippingSusc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallBBearerClippingSusc.setStatus("mandatory")


class _SvcAtmFailedCallAdminStatus_Type(Integer32):
    """Custom type svcAtmFailedCallAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SvcAtmFailedCallAdminStatus_Type.__name__ = "Integer32"
_SvcAtmFailedCallAdminStatus_Object = MibTableColumn
svcAtmFailedCallAdminStatus = _SvcAtmFailedCallAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 277, 5, 2, 3, 1, 30),
    _SvcAtmFailedCallAdminStatus_Type()
)
svcAtmFailedCallAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAtmFailedCallAdminStatus.setStatus("mandatory")
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 6)
)
_SwTable_Object = MibTable
swTable = _SwTable_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1)
)
if mibBuilder.loadTexts:
    swTable.setStatus("mandatory")
_SwEntry_Object = MibTableRow
swEntry = _SwEntry_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1)
)
swEntry.setIndexNames(
    (0, "CASCADE-MIB", "swLogicalSlotId"),
    (0, "CASCADE-MIB", "swRedundState"),
)
if mibBuilder.loadTexts:
    swEntry.setStatus("mandatory")
_SwLogicalSlotId_Type = Integer32
_SwLogicalSlotId_Object = MibTableColumn
swLogicalSlotId = _SwLogicalSlotId_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 1),
    _SwLogicalSlotId_Type()
)
swLogicalSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLogicalSlotId.setStatus("mandatory")


class _SwRedundState_Type(Integer32):
    """Custom type swRedundState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SwRedundState_Type.__name__ = "Integer32"
_SwRedundState_Object = MibTableColumn
swRedundState = _SwRedundState_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 2),
    _SwRedundState_Type()
)
swRedundState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRedundState.setStatus("mandatory")
_SwRevision_Type = DisplayString
_SwRevision_Object = MibTableColumn
swRevision = _SwRevision_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 3),
    _SwRevision_Type()
)
swRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRevision.setStatus("mandatory")
_SwBuildID_Type = DisplayString
_SwBuildID_Object = MibTableColumn
swBuildID = _SwBuildID_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 4),
    _SwBuildID_Type()
)
swBuildID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildID.setStatus("mandatory")
_SwBuildDate_Type = DisplayString
_SwBuildDate_Object = MibTableColumn
swBuildDate = _SwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 5),
    _SwBuildDate_Type()
)
swBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildDate.setStatus("mandatory")
_SwBuildDescription_Type = DisplayString
_SwBuildDescription_Object = MibTableColumn
swBuildDescription = _SwBuildDescription_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 6),
    _SwBuildDescription_Type()
)
swBuildDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildDescription.setStatus("mandatory")
_SwCopyrightNotice_Type = DisplayString
_SwCopyrightNotice_Object = MibTableColumn
swCopyrightNotice = _SwCopyrightNotice_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 7),
    _SwCopyrightNotice_Type()
)
swCopyrightNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCopyrightNotice.setStatus("mandatory")
_SwCapabilityMask_Type = Integer32
_SwCapabilityMask_Object = MibTableColumn
swCapabilityMask = _SwCapabilityMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 8),
    _SwCapabilityMask_Type()
)
swCapabilityMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCapabilityMask.setStatus("mandatory")
_SwFeatureMask_Type = Integer32
_SwFeatureMask_Object = MibTableColumn
swFeatureMask = _SwFeatureMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 9),
    _SwFeatureMask_Type()
)
swFeatureMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFeatureMask.setStatus("mandatory")
_SwPatchMask_Type = Integer32
_SwPatchMask_Object = MibTableColumn
swPatchMask = _SwPatchMask_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 10),
    _SwPatchMask_Type()
)
swPatchMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPatchMask.setStatus("mandatory")
_SwBuildUserId_Type = DisplayString
_SwBuildUserId_Object = MibTableColumn
swBuildUserId = _SwBuildUserId_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 11),
    _SwBuildUserId_Type()
)
swBuildUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildUserId.setStatus("mandatory")
_SwBuildView_Type = DisplayString
_SwBuildView_Object = MibTableColumn
swBuildView = _SwBuildView_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 12),
    _SwBuildView_Type()
)
swBuildView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildView.setStatus("mandatory")
_SwBuildConfigSpec_Type = DisplayString
_SwBuildConfigSpec_Object = MibTableColumn
swBuildConfigSpec = _SwBuildConfigSpec_Object(
    (1, 3, 6, 1, 4, 1, 277, 6, 1, 1, 13),
    _SwBuildConfigSpec_Type()
)
swBuildConfigSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuildConfigSpec.setStatus("mandatory")
_Provserver_ObjectIdentity = ObjectIdentity
provserver = _Provserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 277, 9)
)

# Managed Objects groups


# Notification objects

nodeFileTransferReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 0, 49)
)
nodeFileTransferReport.setObjects(
      *(("CASCADE-MIB", "nodeFileTransferRequest"),
        ("CASCADE-MIB", "nodeFileTransferStatus"))
)
if mibBuilder.loadTexts:
    nodeFileTransferReport.setStatus(
        ""
    )

nodeBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 1)
)
nodeBoardInserted.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportType"))
)
if mibBuilder.loadTexts:
    nodeBoardInserted.setStatus(
        ""
    )

nodeBoardPulled = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 2)
)
nodeBoardPulled.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportType"))
)
if mibBuilder.loadTexts:
    nodeBoardPulled.setStatus(
        ""
    )

nodeBoardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 3)
)
nodeBoardMismatch.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportType"))
)
if mibBuilder.loadTexts:
    nodeBoardMismatch.setStatus(
        ""
    )

nodePsAStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 4)
)
nodePsAStatusChange.setObjects(
    ("CASCADE-MIB", "nodePsAStatus")
)
if mibBuilder.loadTexts:
    nodePsAStatusChange.setStatus(
        ""
    )

nodePsBStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 5)
)
nodePsBStatusChange.setObjects(
    ("CASCADE-MIB", "nodePsBStatus")
)
if mibBuilder.loadTexts:
    nodePsBStatusChange.setStatus(
        ""
    )

nodeFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 6)
)
nodeFanStatusChange.setObjects(
      *(("CASCADE-MIB", "nodeFanIndex"),
        ("CASCADE-MIB", "nodeFanStatus"))
)
if mibBuilder.loadTexts:
    nodeFanStatusChange.setStatus(
        ""
    )

nodeSwDownloadComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 7)
)
nodeSwDownloadComplete.setObjects(
    ("CASCADE-MIB", "nodeSwFilename")
)
if mibBuilder.loadTexts:
    nodeSwDownloadComplete.setStatus(
        ""
    )

nodeSwDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 8)
)
nodeSwDownloadFailed.setObjects(
    ("CASCADE-MIB", "nodeSwFilename")
)
if mibBuilder.loadTexts:
    nodeSwDownloadFailed.setStatus(
        ""
    )

nodePrDownloadComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 9)
)
nodePrDownloadComplete.setObjects(
    ("CASCADE-MIB", "nodePrFilename")
)
if mibBuilder.loadTexts:
    nodePrDownloadComplete.setStatus(
        ""
    )

nodePrDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 10)
)
nodePrDownloadFailed.setObjects(
    ("CASCADE-MIB", "nodePrFilename")
)
if mibBuilder.loadTexts:
    nodePrDownloadFailed.setStatus(
        ""
    )

nodeTracefull = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 11)
)
if mibBuilder.loadTexts:
    nodeTracefull.setStatus(
        ""
    )

nodeDiagLogfull = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 12)
)
if mibBuilder.loadTexts:
    nodeDiagLogfull.setStatus(
        ""
    )

nodeFlashMemErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 13)
)
if mibBuilder.loadTexts:
    nodeFlashMemErr.setStatus(
        ""
    )

nodePramErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 14)
)
if mibBuilder.loadTexts:
    nodePramErr.setStatus(
        ""
    )

nodeRamErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 15)
)
if mibBuilder.loadTexts:
    nodeRamErr.setStatus(
        ""
    )

nodeInternalErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 16)
)
if mibBuilder.loadTexts:
    nodeInternalErr.setStatus(
        ""
    )

pportStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 17)
)
pportStatusChange.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportOperStatus"),
        ("CASCADE-MIB", "pportLinkDownReason"))
)
if mibBuilder.loadTexts:
    pportStatusChange.setStatus(
        ""
    )

lportCongests = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 18)
)
lportCongests.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportCongestRate"))
)
if mibBuilder.loadTexts:
    lportCongests.setStatus(
        ""
    )

trkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 19)
)
trkStatusChange.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"),
        ("CASCADE-MIB", "lportTrkStatus"))
)
if mibBuilder.loadTexts:
    trkStatusChange.setStatus(
        ""
    )

cktDlciStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 20)
)
cktDlciStatusChange.setObjects(
      *(("CASCADE-MIB", "cktSrcIfIndex"),
        ("CASCADE-MIB", "cktSrcDlci"),
        ("CASCADE-MIB", "cktOperStatus"),
        ("CASCADE-MIB", "cktFailReason"),
        ("CASCADE-MIB", "cktFailNode"),
        ("CASCADE-MIB", "cktFailPort"))
)
if mibBuilder.loadTexts:
    cktDlciStatusChange.setStatus(
        ""
    )

cktDlciReroute = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 21)
)
cktDlciReroute.setObjects(
      *(("CASCADE-MIB", "cktSrcIfIndex"),
        ("CASCADE-MIB", "cktSrcDlci"))
)
if mibBuilder.loadTexts:
    cktDlciReroute.setStatus(
        ""
    )

pportInterfaceMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 22)
)
pportInterfaceMismatch.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportAdminInterface"),
        ("CASCADE-MIB", "pportInterface"))
)
if mibBuilder.loadTexts:
    pportInterfaceMismatch.setStatus(
        ""
    )

lportErrorExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 23)
)
lportErrorExceedThreshold.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    lportErrorExceedThreshold.setStatus(
        ""
    )

nodeErrorReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 24)
)
nodeErrorReport.setObjects(
      *(("CASCADE-MIB", "nodeDiagNonFatalSource"),
        ("CASCADE-MIB", "nodeDiagNonFatalTime"),
        ("CASCADE-MIB", "nodeDiagNonFatalErrMajor"),
        ("CASCADE-MIB", "nodeDiagNonFatalErrMinor"),
        ("CASCADE-MIB", "nodeDiagNonFatalStr"))
)
if mibBuilder.loadTexts:
    nodeErrorReport.setStatus(
        ""
    )

cktGrpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 25)
)
cktGrpStatusChange.setObjects(
    ("CASCADE-MIB", "cardCktGroupTrap")
)
if mibBuilder.loadTexts:
    cktGrpStatusChange.setStatus(
        ""
    )

nodeUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 26)
)
nodeUserLogin.setObjects(
      *(("CASCADE-MIB", "nodeConsoleIndex"),
        ("CASCADE-MIB", "nodeUserName"),
        ("CASCADE-MIB", "nodeUserFrom"),
        ("CASCADE-MIB", "nodeConsoleUptime"))
)
if mibBuilder.loadTexts:
    nodeUserLogin.setStatus(
        ""
    )

nodeUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 27)
)
nodeUserLogout.setObjects(
      *(("CASCADE-MIB", "nodeConsoleIndex"),
        ("CASCADE-MIB", "nodeUserName"),
        ("CASCADE-MIB", "nodeUserFrom"),
        ("CASCADE-MIB", "nodeConsoleUptime"))
)
if mibBuilder.loadTexts:
    nodeUserLogout.setStatus(
        ""
    )

cardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 28)
)
cardUp.setObjects(
    ("CASCADE-MIB", "cardPhysicalSlotId")
)
if mibBuilder.loadTexts:
    cardUp.setStatus(
        ""
    )

cardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 29)
)
cardDown.setObjects(
    ("CASCADE-MIB", "cardPhysicalSlotId")
)
if mibBuilder.loadTexts:
    cardDown.setStatus(
        ""
    )

lnkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 30)
)
lnkStatusChange.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"),
        ("CASCADE-MIB", "lportLinkStatus"))
)
if mibBuilder.loadTexts:
    lnkStatusChange.setStatus(
        ""
    )

lnkSmdsHbpNaTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 31)
)
lnkSmdsHbpNaTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lnkSmdsHbpNaTca.setStatus(
        ""
    )

lnkSmdsDiscardTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 32)
)
lnkSmdsDiscardTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lnkSmdsDiscardTca.setStatus(
        ""
    )

cardRedundSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 33)
)
cardRedundSwitchOver.setObjects(
    ("CASCADE-MIB", "cardPhysicalSlotId")
)
if mibBuilder.loadTexts:
    cardRedundSwitchOver.setStatus(
        ""
    )

cardErrorReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 34)
)
cardErrorReport.setObjects(
      *(("CASCADE-MIB", "cardDiagNonFatalSource"),
        ("CASCADE-MIB", "cardDiagNonFatalTime"),
        ("CASCADE-MIB", "cardDiagNonFatalErrMajor"),
        ("CASCADE-MIB", "cardDiagNonFatalErrMinor"),
        ("CASCADE-MIB", "cardDiagNonFatalStr"),
        ("CASCADE-MIB", "cardPhysicalSlotId"))
)
if mibBuilder.loadTexts:
    cardErrorReport.setStatus(
        ""
    )

svcSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 35)
)
svcSetup.setObjects(
      *(("CASCADE-MIB", "cktSrcIfIndex"),
        ("CASCADE-MIB", "cktSrcDlci"),
        ("CASCADE-MIB", "cktSvcCallingParty"),
        ("CASCADE-MIB", "cktSvcCalledParty"))
)
if mibBuilder.loadTexts:
    svcSetup.setStatus(
        ""
    )

svcClearing = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 36)
)
if mibBuilder.loadTexts:
    svcClearing.setStatus(
        ""
    )

svcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 37)
)
svcFailure.setObjects(
      *(("CASCADE-MIB", "cktSvcCallingParty"),
        ("CASCADE-MIB", "cktSvcCalledParty"),
        ("CASCADE-MIB", "cktSvcCause"))
)
if mibBuilder.loadTexts:
    svcFailure.setStatus(
        ""
    )

trkBuAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 38)
)
trkBuAttempt.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    trkBuAttempt.setStatus(
        ""
    )

trkBuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 39)
)
trkBuFailure.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"),
        ("CASCADE-MIB", "lportBuFailReason"))
)
if mibBuilder.loadTexts:
    trkBuFailure.setStatus(
        ""
    )

trkBuReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 40)
)
trkBuReleased.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    trkBuReleased.setStatus(
        ""
    )

pportDS0LoopUpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 41)
)
pportDS0LoopUpChange.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportDS0LoopUpStatus"))
)
if mibBuilder.loadTexts:
    pportDS0LoopUpChange.setStatus(
        ""
    )

pportDS0LoopDownChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 42)
)
pportDS0LoopDownChange.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportDS0LoopDownStatus"))
)
if mibBuilder.loadTexts:
    pportDS0LoopDownChange.setStatus(
        ""
    )

lportISDNCallRej = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 43)
)
lportISDNCallRej.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportISDNCallRejCause"))
)
if mibBuilder.loadTexts:
    lportISDNCallRej.setStatus(
        ""
    )

pportdsx3LoopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 44)
)
pportdsx3LoopChange.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportdsx3LoopStatus"))
)
if mibBuilder.loadTexts:
    pportdsx3LoopChange.setStatus(
        ""
    )

pportds1LoopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 45)
)
pportds1LoopChange.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportds1LoopStatus"))
)
if mibBuilder.loadTexts:
    pportds1LoopChange.setStatus(
        ""
    )

pportExtClockBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 46)
)
pportExtClockBackup.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportSetClkBkup"))
)
if mibBuilder.loadTexts:
    pportExtClockBackup.setStatus(
        ""
    )

pportExtClockRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 47)
)
pportExtClockRestore.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"))
)
if mibBuilder.loadTexts:
    pportExtClockRestore.setStatus(
        ""
    )

pportExtClkCapabilityMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 48)
)
pportExtClkCapabilityMismatch.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"))
)
if mibBuilder.loadTexts:
    pportExtClkCapabilityMismatch.setStatus(
        ""
    )

nodeBillingUsageRecOvflWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 50)
)
nodeBillingUsageRecOvflWarning.setObjects(
    ("CASCADE-MIB", "nodeBillingService")
)
if mibBuilder.loadTexts:
    nodeBillingUsageRecOvflWarning.setStatus(
        ""
    )

nodeBillingUsageRecCrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 51)
)
nodeBillingUsageRecCrFailed.setObjects(
    ("CASCADE-MIB", "nodeBillingService")
)
if mibBuilder.loadTexts:
    nodeBillingUsageRecCrFailed.setStatus(
        ""
    )

nodeBillingStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 52)
)
nodeBillingStateChange.setObjects(
      *(("CASCADE-MIB", "nodeBillingService"),
        ("CASCADE-MIB", "nodeBilling"))
)
if mibBuilder.loadTexts:
    nodeBillingStateChange.setStatus(
        ""
    )

lportBillingStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 53)
)
lportBillingStateChange.setObjects(
      *(("CASCADE-MIB", "nodeBillingService"),
        ("CASCADE-MIB", "lportBilling"),
        ("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportBillingStateChange.setStatus(
        ""
    )

nodeBillingSwAPCommsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 54)
)
nodeBillingSwAPCommsFailure.setObjects(
    ("CASCADE-MIB", "nodeBillingAPAddress")
)
if mibBuilder.loadTexts:
    nodeBillingSwAPCommsFailure.setStatus(
        ""
    )

lportCBRLineDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 57)
)
lportCBRLineDataError.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"),
        ("CASCADE-MIB", "lportStarvation"),
        ("CASCADE-MIB", "lportRecOverflow"),
        ("CASCADE-MIB", "lportLossOfCellSequence"),
        ("CASCADE-MIB", "lportLossOfStructurePointer"))
)
if mibBuilder.loadTexts:
    lportCBRLineDataError.setStatus(
        ""
    )

clkSourceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 58)
)
clkSourceSwitch.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportCbrCurrentClockMode"))
)
if mibBuilder.loadTexts:
    clkSourceSwitch.setStatus(
        ""
    )

clkSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 59)
)
clkSourceFailure.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "nodeRefclockActiveSrc"))
)
if mibBuilder.loadTexts:
    clkSourceFailure.setStatus(
        ""
    )

lportSmdsSip3SaNotFoundTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 60)
)
lportSmdsSip3SaNotFoundTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3SaNotFoundTca.setStatus(
        ""
    )

lportSmdsSip3SaDaOnSamePortTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 61)
)
lportSmdsSip3SaDaOnSamePortTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3SaDaOnSamePortTca.setStatus(
        ""
    )

lportSmdsSip3DstGaNotFoundTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 62)
)
lportSmdsSip3DstGaNotFoundTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3DstGaNotFoundTca.setStatus(
        ""
    )

lportSmdsSip3DstIaScrnFailTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 63)
)
lportSmdsSip3DstIaScrnFailTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3DstIaScrnFailTca.setStatus(
        ""
    )

lportSmdsSip3SaValFailTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 64)
)
lportSmdsSip3SaValFailTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3SaValFailTca.setStatus(
        ""
    )

lportSmdsSip3DstIaNotFoundTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 65)
)
lportSmdsSip3DstIaNotFoundTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3DstIaNotFoundTca.setStatus(
        ""
    )

lportSmdsSip3SrcIaScrnFailTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 66)
)
lportSmdsSip3SrcIaScrnFailTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3SrcIaScrnFailTca.setStatus(
        ""
    )

lportSmdsSip3DstGaScrnFailTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 67)
)
lportSmdsSip3DstGaScrnFailTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsSip3DstGaScrnFailTca.setStatus(
        ""
    )

lportSmdsDxi2LinkIdInvalidTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 68)
)
lportSmdsDxi2LinkIdInvalidTca.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportSlotId"),
        ("CASCADE-MIB", "lportPportId"),
        ("CASCADE-MIB", "lportId"))
)
if mibBuilder.loadTexts:
    lportSmdsDxi2LinkIdInvalidTca.setStatus(
        ""
    )

nodePrimarySyncReferenceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 69)
)
nodePrimarySyncReferenceChange.setObjects(
    ("CASCADE-MIB", "nodePrimarySyncRefOperationalState")
)
if mibBuilder.loadTexts:
    nodePrimarySyncReferenceChange.setStatus(
        ""
    )

nodeSecondarySyncReferenceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 70)
)
nodeSecondarySyncReferenceChange.setObjects(
    ("CASCADE-MIB", "nodeSecondarySyncRefOperationalState")
)
if mibBuilder.loadTexts:
    nodeSecondarySyncReferenceChange.setStatus(
        ""
    )

nodeExternalClockAChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 71)
)
nodeExternalClockAChange.setObjects(
    ("CASCADE-MIB", "nodeExternalClockAOperationalState")
)
if mibBuilder.loadTexts:
    nodeExternalClockAChange.setStatus(
        ""
    )

nodeExternalClockBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 72)
)
nodeExternalClockBChange.setObjects(
    ("CASCADE-MIB", "nodeExternalClockBOperationalState")
)
if mibBuilder.loadTexts:
    nodeExternalClockBChange.setStatus(
        ""
    )

nodePortReferenceAChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 73)
)
nodePortReferenceAChange.setObjects(
    ("CASCADE-MIB", "nodePortClockAOperationalState")
)
if mibBuilder.loadTexts:
    nodePortReferenceAChange.setStatus(
        ""
    )

nodePortReferenceBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 74)
)
nodePortReferenceBChange.setObjects(
    ("CASCADE-MIB", "nodePortClockBOperationalState")
)
if mibBuilder.loadTexts:
    nodePortReferenceBChange.setStatus(
        ""
    )

pportDS0InitiateLpbkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 75)
)
pportDS0InitiateLpbkFailure.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportDS0FarendDS0InLpbk"))
)
if mibBuilder.loadTexts:
    pportDS0InitiateLpbkFailure.setStatus(
        ""
    )

pportDS0InitiateLpbkSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 76)
)
pportDS0InitiateLpbkSuccess.setObjects(
      *(("CASCADE-MIB", "pportSlotId"),
        ("CASCADE-MIB", "pportId"),
        ("CASCADE-MIB", "pportDS0FarendDS0InLpbk"))
)
if mibBuilder.loadTexts:
    pportDS0InitiateLpbkSuccess.setStatus(
        ""
    )

lportISDNIpAddrRej = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 77)
)
lportISDNIpAddrRej.setObjects(
      *(("CASCADE-MIB", "lportIfIndex"),
        ("CASCADE-MIB", "lportISDNIpAddrAssignFail"))
)
if mibBuilder.loadTexts:
    lportISDNIpAddrRej.setStatus(
        ""
    )

cktAtmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 78)
)
cktAtmStatusChange.setObjects(
      *(("CASCADE-MIB", "cktSrcIfIndex"),
        ("CASCADE-MIB", "cktAtmVPI"),
        ("CASCADE-MIB", "cktAtmVCI"),
        ("CASCADE-MIB", "cktOperStatus"),
        ("CASCADE-MIB", "cktFailReason"),
        ("CASCADE-MIB", "cktFailNode"),
        ("CASCADE-MIB", "cktFailPort"))
)
if mibBuilder.loadTexts:
    cktAtmStatusChange.setStatus(
        ""
    )

cktAtmReroute = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 79)
)
cktAtmReroute.setObjects(
      *(("CASCADE-MIB", "cktSrcIfIndex"),
        ("CASCADE-MIB", "cktAtmVPI"),
        ("CASCADE-MIB", "cktAtmVCI"))
)
if mibBuilder.loadTexts:
    cktAtmReroute.setStatus(
        ""
    )

cardTransmitClockStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 80)
)
cardTransmitClockStatusChange.setObjects(
      *(("CASCADE-MIB", "cardPhysicalSlotId"),
        ("CASCADE-MIB", "cardTransmitClockStatus"))
)
if mibBuilder.loadTexts:
    cardTransmitClockStatusChange.setStatus(
        ""
    )

cardSystemPrimaryClockStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 81)
)
cardSystemPrimaryClockStatusChange.setObjects(
      *(("CASCADE-MIB", "cardPhysicalSlotId"),
        ("CASCADE-MIB", "cardSystemPrimaryClockStatus"))
)
if mibBuilder.loadTexts:
    cardSystemPrimaryClockStatusChange.setStatus(
        ""
    )

cardSystemSecondaryClockStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 1, 0, 82)
)
cardSystemSecondaryClockStatusChange.setObjects(
      *(("CASCADE-MIB", "cardPhysicalSlotId"),
        ("CASCADE-MIB", "cardSystemSecondaryClockStatus"))
)
if mibBuilder.loadTexts:
    cardSystemSecondaryClockStatusChange.setStatus(
        ""
    )

svcAtmFailedCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 5, 0, 55)
)
svcAtmFailedCall.setObjects(
      *(("CASCADE-MIB", "svcAtmFailedCallIfIndex"),
        ("CASCADE-MIB", "svcAtmFailedCallIndex"))
)
if mibBuilder.loadTexts:
    svcAtmFailedCall.setStatus(
        ""
    )

svcAtmSigStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 277, 5, 0, 56)
)
svcAtmSigStatusChange.setObjects(
      *(("CASCADE-MIB", "svcAtmConfigIfIndex"),
        ("CASCADE-MIB", "svcAtmConfigOperStatus"))
)
if mibBuilder.loadTexts:
    svcAtmSigStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASCADE-MIB",
    **{"Index": Index,
       "CardTypes": CardTypes,
       "CardStatuses": CardStatuses,
       "cascade": cascade,
       "nodeFileTransferReport": nodeFileTransferReport,
       "cascfr": cascfr,
       "nodeBoardInserted": nodeBoardInserted,
       "nodeBoardPulled": nodeBoardPulled,
       "nodeBoardMismatch": nodeBoardMismatch,
       "nodePsAStatusChange": nodePsAStatusChange,
       "nodePsBStatusChange": nodePsBStatusChange,
       "nodeFanStatusChange": nodeFanStatusChange,
       "nodeSwDownloadComplete": nodeSwDownloadComplete,
       "nodeSwDownloadFailed": nodeSwDownloadFailed,
       "nodePrDownloadComplete": nodePrDownloadComplete,
       "nodePrDownloadFailed": nodePrDownloadFailed,
       "nodeTracefull": nodeTracefull,
       "nodeDiagLogfull": nodeDiagLogfull,
       "nodeFlashMemErr": nodeFlashMemErr,
       "nodePramErr": nodePramErr,
       "nodeRamErr": nodeRamErr,
       "nodeInternalErr": nodeInternalErr,
       "pportStatusChange": pportStatusChange,
       "lportCongests": lportCongests,
       "trkStatusChange": trkStatusChange,
       "cktDlciStatusChange": cktDlciStatusChange,
       "cktDlciReroute": cktDlciReroute,
       "pportInterfaceMismatch": pportInterfaceMismatch,
       "lportErrorExceedThreshold": lportErrorExceedThreshold,
       "nodeErrorReport": nodeErrorReport,
       "cktGrpStatusChange": cktGrpStatusChange,
       "nodeUserLogin": nodeUserLogin,
       "nodeUserLogout": nodeUserLogout,
       "cardUp": cardUp,
       "cardDown": cardDown,
       "lnkStatusChange": lnkStatusChange,
       "lnkSmdsHbpNaTca": lnkSmdsHbpNaTca,
       "lnkSmdsDiscardTca": lnkSmdsDiscardTca,
       "cardRedundSwitchOver": cardRedundSwitchOver,
       "cardErrorReport": cardErrorReport,
       "svcSetup": svcSetup,
       "svcClearing": svcClearing,
       "svcFailure": svcFailure,
       "trkBuAttempt": trkBuAttempt,
       "trkBuFailure": trkBuFailure,
       "trkBuReleased": trkBuReleased,
       "pportDS0LoopUpChange": pportDS0LoopUpChange,
       "pportDS0LoopDownChange": pportDS0LoopDownChange,
       "lportISDNCallRej": lportISDNCallRej,
       "pportdsx3LoopChange": pportdsx3LoopChange,
       "pportds1LoopChange": pportds1LoopChange,
       "pportExtClockBackup": pportExtClockBackup,
       "pportExtClockRestore": pportExtClockRestore,
       "pportExtClkCapabilityMismatch": pportExtClkCapabilityMismatch,
       "nodeBillingUsageRecOvflWarning": nodeBillingUsageRecOvflWarning,
       "nodeBillingUsageRecCrFailed": nodeBillingUsageRecCrFailed,
       "nodeBillingStateChange": nodeBillingStateChange,
       "lportBillingStateChange": lportBillingStateChange,
       "nodeBillingSwAPCommsFailure": nodeBillingSwAPCommsFailure,
       "lportCBRLineDataError": lportCBRLineDataError,
       "clkSourceSwitch": clkSourceSwitch,
       "clkSourceFailure": clkSourceFailure,
       "lportSmdsSip3SaNotFoundTca": lportSmdsSip3SaNotFoundTca,
       "lportSmdsSip3SaDaOnSamePortTca": lportSmdsSip3SaDaOnSamePortTca,
       "lportSmdsSip3DstGaNotFoundTca": lportSmdsSip3DstGaNotFoundTca,
       "lportSmdsSip3DstIaScrnFailTca": lportSmdsSip3DstIaScrnFailTca,
       "lportSmdsSip3SaValFailTca": lportSmdsSip3SaValFailTca,
       "lportSmdsSip3DstIaNotFoundTca": lportSmdsSip3DstIaNotFoundTca,
       "lportSmdsSip3SrcIaScrnFailTca": lportSmdsSip3SrcIaScrnFailTca,
       "lportSmdsSip3DstGaScrnFailTca": lportSmdsSip3DstGaScrnFailTca,
       "lportSmdsDxi2LinkIdInvalidTca": lportSmdsDxi2LinkIdInvalidTca,
       "nodePrimarySyncReferenceChange": nodePrimarySyncReferenceChange,
       "nodeSecondarySyncReferenceChange": nodeSecondarySyncReferenceChange,
       "nodeExternalClockAChange": nodeExternalClockAChange,
       "nodeExternalClockBChange": nodeExternalClockBChange,
       "nodePortReferenceAChange": nodePortReferenceAChange,
       "nodePortReferenceBChange": nodePortReferenceBChange,
       "pportDS0InitiateLpbkFailure": pportDS0InitiateLpbkFailure,
       "pportDS0InitiateLpbkSuccess": pportDS0InitiateLpbkSuccess,
       "lportISDNIpAddrRej": lportISDNIpAddrRej,
       "cktAtmStatusChange": cktAtmStatusChange,
       "cktAtmReroute": cktAtmReroute,
       "cardTransmitClockStatusChange": cardTransmitClockStatusChange,
       "cardSystemPrimaryClockStatusChange": cardSystemPrimaryClockStatusChange,
       "cardSystemSecondaryClockStatusChange": cardSystemSecondaryClockStatusChange,
       "net": net,
       "netMask": netMask,
       "netNumber": netNumber,
       "netDlciAddrSig": netDlciAddrSig,
       "netMaxSegsize": netMaxSegsize,
       "netSmdsAreaMaskStart": netSmdsAreaMaskStart,
       "netSmdsAreaMaskDigits": netSmdsAreaMaskDigits,
       "ase": ase,
       "aseTable": aseTable,
       "aseEntry": aseEntry,
       "aseAddr": aseAddr,
       "aseMask": aseMask,
       "aseDefaultGwAddr": aseDefaultGwAddr,
       "aseMetricType": aseMetricType,
       "aseAdminStatus": aseAdminStatus,
       "aseIfIndex": aseIfIndex,
       "aseDlci": aseDlci,
       "node": node,
       "nodeIpAddr": nodeIpAddr,
       "nodeLanIpAddr": nodeLanIpAddr,
       "nodeNMSTable": nodeNMSTable,
       "nodeNMSEntry": nodeNMSEntry,
       "nodeNMSIndex": nodeNMSIndex,
       "nodeNMSIpAddr": nodeNMSIpAddr,
       "nodeState": nodeState,
       "nodePollStatus": nodePollStatus,
       "nodeModel": nodeModel,
       "nodeSerial": nodeSerial,
       "nodeSwRev": nodeSwRev,
       "nodeHwRev": nodeHwRev,
       "nodeEpromRev": nodeEpromRev,
       "nodeCpuUtil": nodeCpuUtil,
       "nodePsAStatus": nodePsAStatus,
       "nodePsBStatus": nodePsBStatus,
       "nodeFanTable": nodeFanTable,
       "nodeFanEntry": nodeFanEntry,
       "nodeFanIndex": nodeFanIndex,
       "nodeFanStatus": nodeFanStatus,
       "nodeFanSpeed": nodeFanSpeed,
       "nodeMemoryUtil": nodeMemoryUtil,
       "nodeMemoryUsage": nodeMemoryUsage,
       "nodeMaxFramesize": nodeMaxFramesize,
       "nodeQOSPollTimer": nodeQOSPollTimer,
       "nodeActivePvcs": nodeActivePvcs,
       "nodeInactivePvcs": nodeInactivePvcs,
       "nodePendingPvcs": nodePendingPvcs,
       "nodeInOctets": nodeInOctets,
       "nodeInPkts": nodeInPkts,
       "nodeOutOctets": nodeOutOctets,
       "nodeOutPkts": nodeOutPkts,
       "nodeSwFilename": nodeSwFilename,
       "nodeRebootAfterLoad": nodeRebootAfterLoad,
       "nodeSwToLoad": nodeSwToLoad,
       "nodeSwLoadState": nodeSwLoadState,
       "nodePrFilename": nodePrFilename,
       "nodePrToLoad": nodePrToLoad,
       "nodePrLoadState": nodePrLoadState,
       "nodeToWarmboot": nodeToWarmboot,
       "nodeToColdboot": nodeToColdboot,
       "nodeToRedundant": nodeToRedundant,
       "nodeInitiateBulkStats": nodeInitiateBulkStats,
       "nodeDiagNonFatalSource": nodeDiagNonFatalSource,
       "nodeDiagNonFatalTime": nodeDiagNonFatalTime,
       "nodeDiagNonFatalErrMajor": nodeDiagNonFatalErrMajor,
       "nodeDiagNonFatalErrMinor": nodeDiagNonFatalErrMinor,
       "nodeDiagNonFatalStr": nodeDiagNonFatalStr,
       "nodeDiagFatalSource": nodeDiagFatalSource,
       "nodeDiagFatalTime": nodeDiagFatalTime,
       "nodeDiagFatalErrMajor": nodeDiagFatalErrMajor,
       "nodeDiagFatalErrMinor": nodeDiagFatalErrMinor,
       "nodeDiagFatalStr": nodeDiagFatalStr,
       "nodeDiagFatalReboots": nodeDiagFatalReboots,
       "nodeDiagFatalAddress": nodeDiagFatalAddress,
       "nodeDiagBackgroundPasses": nodeDiagBackgroundPasses,
       "nodeDiagBackgroundFailures": nodeDiagBackgroundFailures,
       "nodeDiagBackgroundSuccesses": nodeDiagBackgroundSuccesses,
       "nodeDiagLEDReset": nodeDiagLEDReset,
       "nodeDiagPowerExtensive": nodeDiagPowerExtensive,
       "nodePortPoll": nodePortPoll,
       "nodeMaxTelnetConsole": nodeMaxTelnetConsole,
       "nodeConsoleTimeout": nodeConsoleTimeout,
       "nodeConsoleTable": nodeConsoleTable,
       "nodeConsoleEntry": nodeConsoleEntry,
       "nodeConsoleIndex": nodeConsoleIndex,
       "nodeUserName": nodeUserName,
       "nodeUserFrom": nodeUserFrom,
       "nodeConsoleAccessMode": nodeConsoleAccessMode,
       "nodeConsoleUptime": nodeConsoleUptime,
       "nodePsADiagCode": nodePsADiagCode,
       "nodePsBDiagCode": nodePsBDiagCode,
       "nodeFrameMemoryUtil": nodeFrameMemoryUtil,
       "nodeFrameMemoryUsage": nodeFrameMemoryUsage,
       "nodeCapability": nodeCapability,
       "nodeSvcLastCallFailure": nodeSvcLastCallFailure,
       "nodeRerouteDelay": nodeRerouteDelay,
       "nodeRerouteCount": nodeRerouteCount,
       "nodeFileTransferRequest": nodeFileTransferRequest,
       "nodeFileTransferStatus": nodeFileTransferStatus,
       "nodeTime": nodeTime,
       "nodeBillingAPAddress": nodeBillingAPAddress,
       "nodeBillingAPUsername": nodeBillingAPUsername,
       "nodeBillingAPPassword": nodeBillingAPPassword,
       "nodeBillingSwAPCommsFailures": nodeBillingSwAPCommsFailures,
       "nodeBillingTable": nodeBillingTable,
       "nodeBillingEntry": nodeBillingEntry,
       "nodeBillingService": nodeBillingService,
       "nodeBilling": nodeBilling,
       "nodeBillingAggrPeriod": nodeBillingAggrPeriod,
       "nodeBillingCurAggrPeriodStart": nodeBillingCurAggrPeriodStart,
       "nodeBillingCurAggrPeriodEnd": nodeBillingCurAggrPeriodEnd,
       "nodeBillingCollection": nodeBillingCollection,
       "nodeBillingDailyProcessing": nodeBillingDailyProcessing,
       "nodeBillingDPTime": nodeBillingDPTime,
       "nodeBillingUsageRecOvflWarnings": nodeBillingUsageRecOvflWarnings,
       "nodeBillingTotalUsageRecOvflWarnings": nodeBillingTotalUsageRecOvflWarnings,
       "nodeBillingBillableUsageEvents": nodeBillingBillableUsageEvents,
       "nodeBillingNonBillableUsageEvents": nodeBillingNonBillableUsageEvents,
       "nodeBillingUsageRecCreated": nodeBillingUsageRecCreated,
       "nodeBillingTotalUsageRecCreated": nodeBillingTotalUsageRecCreated,
       "nodeBillingUsageRecCrFailures": nodeBillingUsageRecCrFailures,
       "nodeBillingTotalUsageRecCrFailures": nodeBillingTotalUsageRecCrFailures,
       "nodeBillingUsageRecSent": nodeBillingUsageRecSent,
       "nodeBillingTotalUsageRecSent": nodeBillingTotalUsageRecSent,
       "nodeBillingUsageDataStoreFull": nodeBillingUsageDataStoreFull,
       "nodeBillingTotalUsageDataStoreFull": nodeBillingTotalUsageDataStoreFull,
       "nodeBillingAdminAction": nodeBillingAdminAction,
       "nodeRerouteAlg": nodeRerouteAlg,
       "nodeOamAlarmDisabled": nodeOamAlarmDisabled,
       "nodeRefclocksrcTable": nodeRefclocksrcTable,
       "nodeRefclocksrcEntry": nodeRefclocksrcEntry,
       "nodeRefclocksrcIndex": nodeRefclocksrcIndex,
       "nodeRefclocksrcPriority": nodeRefclocksrcPriority,
       "nodeRefclocksrcType": nodeRefclocksrcType,
       "nodeRefclocksrcSlotId": nodeRefclocksrcSlotId,
       "nodeRefclocksrcPportId": nodeRefclocksrcPportId,
       "nodeRefclockActiveSrc": nodeRefclockActiveSrc,
       "nodeRefclockActiveCGUSlotId": nodeRefclockActiveCGUSlotId,
       "nodeRefclockActiveCGUMode": nodeRefclockActiveCGUMode,
       "nodeInitiateImageBackup": nodeInitiateImageBackup,
       "nodeImageBackupState": nodeImageBackupState,
       "nodeInitiateImageRestore": nodeInitiateImageRestore,
       "nodeApplicationTable": nodeApplicationTable,
       "nodeApplicationEntry": nodeApplicationEntry,
       "nodeApplicationIndex": nodeApplicationIndex,
       "nodeApplicationDescription": nodeApplicationDescription,
       "nodePrimaryVersion": nodePrimaryVersion,
       "nodeSecondaryVersion": nodeSecondaryVersion,
       "nodePrimarySyncRefAdminState": nodePrimarySyncRefAdminState,
       "nodePrimarySyncRefOperationalState": nodePrimarySyncRefOperationalState,
       "nodeSecondarySyncRefAdminState": nodeSecondarySyncRefAdminState,
       "nodeSecondarySyncRefOperationalState": nodeSecondarySyncRefOperationalState,
       "nodePrimaryPLLOperationalState": nodePrimaryPLLOperationalState,
       "nodeSecondaryPLLOperationalState": nodeSecondaryPLLOperationalState,
       "nodeExternalClockAOperationalState": nodeExternalClockAOperationalState,
       "nodeExternalClockBOperationalState": nodeExternalClockBOperationalState,
       "nodePortClockAOperationalState": nodePortClockAOperationalState,
       "nodePortClockBOperationalState": nodePortClockBOperationalState,
       "nodeExternalTimingSource": nodeExternalTimingSource,
       "nodeSyncAutoRestore": nodeSyncAutoRestore,
       "nodeExternalClockInterfaceType": nodeExternalClockInterfaceType,
       "pport": pport,
       "pportNumber": pportNumber,
       "pportTable": pportTable,
       "pportEntry": pportEntry,
       "pportSlotId": pportSlotId,
       "pportId": pportId,
       "pportAdminType": pportAdminType,
       "pportNumLport": pportNumLport,
       "pportDataRate": pportDataRate,
       "pportType": pportType,
       "pportRecvClock": pportRecvClock,
       "pportXmitClock": pportXmitClock,
       "pportAdminStatus": pportAdminStatus,
       "pportOperStatus": pportOperStatus,
       "pportDs1LineType": pportDs1LineType,
       "pportDs1ZeroCoding": pportDs1ZeroCoding,
       "pportDs1LineBuildout": pportDs1LineBuildout,
       "pportDiagTestId": pportDiagTestId,
       "pportDiagTestRuns": pportDiagTestRuns,
       "pportInOctets": pportInOctets,
       "pportInFrames": pportInFrames,
       "pportInDiscards": pportInDiscards,
       "pportInErrors": pportInErrors,
       "pportOutOctets": pportOutOctets,
       "pportOutFrames": pportOutFrames,
       "pportOutDiscards": pportOutDiscards,
       "pportOutErrors": pportOutErrors,
       "pportDiagState": pportDiagState,
       "pportDiagOptionStr": pportDiagOptionStr,
       "pportDiagPassCount": pportDiagPassCount,
       "pportDiagFailCount": pportDiagFailCount,
       "pportDiagResultStr": pportDiagResultStr,
       "pportLinkDownReason": pportLinkDownReason,
       "pportInterface": pportInterface,
       "pportAdminInterface": pportAdminInterface,
       "pportCellScramble": pportCellScramble,
       "pportCbitParity": pportCbitParity,
       "pportMaxBufferSize": pportMaxBufferSize,
       "pportPeakCellRate0": pportPeakCellRate0,
       "pportPeakCellRate1": pportPeakCellRate1,
       "pportPeakCellRate2": pportPeakCellRate2,
       "pportPeakCellRate3": pportPeakCellRate3,
       "pportPeakCellRate4": pportPeakCellRate4,
       "pportPeakCellRate5": pportPeakCellRate5,
       "pportPeakCellRate6": pportPeakCellRate6,
       "pportPeakCellRate7": pportPeakCellRate7,
       "pportInCells": pportInCells,
       "pportInErrorCells": pportInErrorCells,
       "pportOutCells": pportOutCells,
       "pportDs3LineBuildout": pportDs3LineBuildout,
       "pportSetDS0LoopUp": pportSetDS0LoopUp,
       "pportSetDS0LoopDown": pportSetDS0LoopDown,
       "pportDS0LoopUpStatus": pportDS0LoopUpStatus,
       "pportDS0LoopDownStatus": pportDS0LoopDownStatus,
       "pportDS0LoopStatus": pportDS0LoopStatus,
       "pportISDN": pportISDN,
       "pportdsx3LoopbackConfig": pportdsx3LoopbackConfig,
       "pportdsx3SendCode": pportdsx3SendCode,
       "pportdsx3LoopStatus": pportdsx3LoopStatus,
       "pportdsx3FEACStatus": pportdsx3FEACStatus,
       "pportds1LoopbackConfig": pportds1LoopbackConfig,
       "pportds1SendCode": pportds1SendCode,
       "pportds1LoopStatus": pportds1LoopStatus,
       "pportSetClkBkup": pportSetClkBkup,
       "pportAtmIdleWord": pportAtmIdleWord,
       "pportAtmDisCardMode": pportAtmDisCardMode,
       "pportAtmLastUnconfiguredVpi": pportAtmLastUnconfiguredVpi,
       "pportAtmLastUnconfiguredVci": pportAtmLastUnconfiguredVci,
       "pportAtmUnconfiguredCells": pportAtmUnconfiguredCells,
       "pportAtmNumBitsVCI": pportAtmNumBitsVCI,
       "pportAtmNumBitsVPI": pportAtmNumBitsVPI,
       "pportAtmInterfaceType": pportAtmInterfaceType,
       "pportSonetSDHLoopbackConfig": pportSonetSDHLoopbackConfig,
       "pportSonetSDHLoopStatus": pportSonetSDHLoopStatus,
       "pportOutDiscardsCell": pportOutDiscardsCell,
       "pportAtmPlcp": pportAtmPlcp,
       "pportCbrTargetClockMode": pportCbrTargetClockMode,
       "pportCbrCurrentClockMode": pportCbrCurrentClockMode,
       "pportClockMasterChannel": pportClockMasterChannel,
       "pportFibreType": pportFibreType,
       "pportLaserStatus": pportLaserStatus,
       "pportMaxActiveVpiBits": pportMaxActiveVpiBits,
       "pportBipErrorsThresh": pportBipErrorsThresh,
       "pportBipSectionErrors": pportBipSectionErrors,
       "pportBipLineErrors": pportBipLineErrors,
       "pportBipPathErrors": pportBipPathErrors,
       "pportFebeErrors": pportFebeErrors,
       "pportHcsErrors": pportHcsErrors,
       "pportHcsSevereErrors": pportHcsSevereErrors,
       "pportCongestedReceivedCells": pportCongestedReceivedCells,
       "pportCongestedTransmittedCells": pportCongestedTransmittedCells,
       "pportAtmLayerErroredReceivedCells": pportAtmLayerErroredReceivedCells,
       "pportAtmLayerErroredTransmittedCells": pportAtmLayerErroredTransmittedCells,
       "pportDS0BitStuff": pportDS0BitStuff,
       "pportDS0BitErrorCount": pportDS0BitErrorCount,
       "pportDS0BitErrorFreeSeconds": pportDS0BitErrorFreeSeconds,
       "pportDS0BitErroredSeconds": pportDS0BitErroredSeconds,
       "pportDS0MidspanRepeaters": pportDS0MidspanRepeaters,
       "pportDS0TestPatternSync": pportDS0TestPatternSync,
       "pportDS0InjectBitError": pportDS0InjectBitError,
       "pportDS0FarendLpbkType": pportDS0FarendLpbkType,
       "pportDS0LpbkMode": pportDS0LpbkMode,
       "pportDS0SwitchLpbkStart": pportDS0SwitchLpbkStart,
       "pportDS0SwitchLpbkEnd": pportDS0SwitchLpbkEnd,
       "pportDS0FarendDS0InLpbk": pportDS0FarendDS0InLpbk,
       "pportDS0SendTestTraffic": pportDS0SendTestTraffic,
       "pportOc3LoopConfig": pportOc3LoopConfig,
       "pportOc3LoopStatus": pportOc3LoopStatus,
       "pportISDNIpBaseAddr": pportISDNIpBaseAddr,
       "pportSonetSTM1Scramble": pportSonetSTM1Scramble,
       "pportEFCIMarking": pportEFCIMarking,
       "pportAtmQOSTransmitMode": pportAtmQOSTransmitMode,
       "pportHECMode": pportHECMode,
       "pportISDNChannelStatus": pportISDNChannelStatus,
       "pportds1FarEndLoopStatus": pportds1FarEndLoopStatus,
       "pportds1FDLControl": pportds1FDLControl,
       "pportds1FDLPrmXmit": pportds1FDLPrmXmit,
       "pportds1FDLPidXmit": pportds1FDLPidXmit,
       "pportds1FDLXmitPid": pportds1FDLXmitPid,
       "pportds1FDLRcvPid": pportds1FDLRcvPid,
       "pportds1FDLRcvTsid": pportds1FDLRcvTsid,
       "pportSonetSDHFramingMode": pportSonetSDHFramingMode,
       "pportds1InbandLoopType": pportds1InbandLoopType,
       "pportESFDataLinkStatus": pportESFDataLinkStatus,
       "pportPMTcaId": pportPMTcaId,
       "pportBchanTimerValue": pportBchanTimerValue,
       "pportAAL5CRC32Error": pportAAL5CRC32Error,
       "pportAAL5CPIError": pportAAL5CPIError,
       "pportAAL5LengthError": pportAAL5LengthError,
       "pportAAL5ReassemblyTimerError": pportAAL5ReassemblyTimerError,
       "pportAAL5MaxNrSegError": pportAAL5MaxNrSegError,
       "pportRedundancyArch": pportRedundancyArch,
       "pportAPSadminDir": pportAPSadminDir,
       "pportAPSlineType": pportAPSlineType,
       "pportAPSrevertiveMode": pportAPSrevertiveMode,
       "pportAPSpairedSlotId": pportAPSpairedSlotId,
       "pportAPSpairedPportId": pportAPSpairedPportId,
       "pportAPSsfBerThresh": pportAPSsfBerThresh,
       "pportAPSsdBerThresh": pportAPSsdBerThresh,
       "pportAPSwtrPeriod": pportAPSwtrPeriod,
       "pportAPSprotectionLineState": pportAPSprotectionLineState,
       "pportAPSxCommand": pportAPSxCommand,
       "pportAPSconfigStatus": pportAPSconfigStatus,
       "pportAPSOperRxStatus": pportAPSOperRxStatus,
       "pportBertPattern": pportBertPattern,
       "pportBertUserBytes": pportBertUserBytes,
       "pportBertErrorRate": pportBertErrorRate,
       "pportBertCommand": pportBertCommand,
       "pportBertStatus": pportBertStatus,
       "pportBertBitCount": pportBertBitCount,
       "pportBertErrorCount": pportBertErrorCount,
       "pportds1FELoopbackControl": pportds1FELoopbackControl,
       "pportFT1DS0s": pportFT1DS0s,
       "pportIMUXCnt": pportIMUXCnt,
       "pportds1PMConfigThresh": pportds1PMConfigThresh,
       "pportIdleCellType": pportIdleCellType,
       "pportATMTcaInHECErrorUAlertPeriod": pportATMTcaInHECErrorUAlertPeriod,
       "pportATMTcaInHECErrorUThresh": pportATMTcaInHECErrorUThresh,
       "pportATMTcaEBufOverflowCBRAlertPeriod": pportATMTcaEBufOverflowCBRAlertPeriod,
       "pportATMTcaEBufOverflowCBRThresh": pportATMTcaEBufOverflowCBRThresh,
       "pportATMTcaEBufOverflowABRAlertPeriod": pportATMTcaEBufOverflowABRAlertPeriod,
       "pportATMTcaEBufOverflowABRThresh": pportATMTcaEBufOverflowABRThresh,
       "pportATMTcaEBufOverflowVBR1AlertPeriod": pportATMTcaEBufOverflowVBR1AlertPeriod,
       "pportATMTcaEBufOverflowVBR1Thresh": pportATMTcaEBufOverflowVBR1Thresh,
       "pportATMTcaEBufOverflowVBR2AlertPeriod": pportATMTcaEBufOverflowVBR2AlertPeriod,
       "pportATMTcaEBufOverflowVBR2Thresh": pportATMTcaEBufOverflowVBR2Thresh,
       "pportATMTcaInFramerFIFOOverflowAlertPeriod": pportATMTcaInFramerFIFOOverflowAlertPeriod,
       "pportATMTcaInFramerFIFOOverflowThresh": pportATMTcaInFramerFIFOOverflowThresh,
       "pportATMTcaELookupFailureAlertPeriod": pportATMTcaELookupFailureAlertPeriod,
       "pportATMTcaELookupFailureThresh": pportATMTcaELookupFailureThresh,
       "pportATMTcaEnable": pportATMTcaEnable,
       "pportATMTcaId": pportATMTcaId,
       "pportFethAdminMacAddr": pportFethAdminMacAddr,
       "pportFethOperMacAddr": pportFethOperMacAddr,
       "pportConfigAlarmSoakTime": pportConfigAlarmSoakTime,
       "pportConfigAlarmClearTime": pportConfigAlarmClearTime,
       "pportFethPortCapability": pportFethPortCapability,
       "pportVpshapingDiscardCellCount": pportVpshapingDiscardCellCount,
       "pportTrafficShaperTable": pportTrafficShaperTable,
       "pportTrafficShaperEntry": pportTrafficShaperEntry,
       "pportTrafficShaperIndex": pportTrafficShaperIndex,
       "pportTrafficShaperPriority": pportTrafficShaperPriority,
       "pportTrafficShaperCellRatioDividend": pportTrafficShaperCellRatioDividend,
       "pportTrafficShaperCellRatioDivisor": pportTrafficShaperCellRatioDivisor,
       "pportTrafficShaperPeak": pportTrafficShaperPeak,
       "pportTrafficShaperCredit": pportTrafficShaperCredit,
       "lport": lport,
       "lportTable": lportTable,
       "lportEntry": lportEntry,
       "lportIfIndex": lportIfIndex,
       "lportSlotId": lportSlotId,
       "lportPportId": lportPportId,
       "lportId": lportId,
       "lportLink": lportLink,
       "lportProtocol": lportProtocol,
       "lportSignal": lportSignal,
       "lportFt1Ds0s": lportFt1Ds0s,
       "lportGlobalDlci": lportGlobalDlci,
       "lportDlcmiStd": lportDlcmiStd,
       "lportDlciAddrFmt": lportDlciAddrFmt,
       "lportDlciAddrLen": lportDlciAddrLen,
       "lportMaxFramesize": lportMaxFramesize,
       "lportDceVerifTimer": lportDceVerifTimer,
       "lportDceErrorThresh": lportDceErrorThresh,
       "lportDceEventCount": lportDceEventCount,
       "lportDteErrorThresh": lportDteErrorThresh,
       "lportDteEventCount": lportDteEventCount,
       "lportDtePollTimer": lportDtePollTimer,
       "lportDteFullCounter": lportDteFullCounter,
       "lportDteMulticast": lportDteMulticast,
       "lportTrkRnode": lportTrkRnode,
       "lportTrkRlport": lportTrkRlport,
       "lportCongestState": lportCongestState,
       "lportQP1Len": lportQP1Len,
       "lportQP2Len": lportQP2Len,
       "lportQP3Len": lportQP3Len,
       "lportQP4Len": lportQP4Len,
       "lportErrTime": lportErrTime,
       "lportErrType": lportErrType,
       "lportErrData": lportErrData,
       "lportDiagTestId": lportDiagTestId,
       "lportDiagTestRuns": lportDiagTestRuns,
       "lportDataRate": lportDataRate,
       "lportTrkStatus": lportTrkStatus,
       "lportSevCongests": lportSevCongests,
       "lportAbsCongests": lportAbsCongests,
       "lportTrkOverhead": lportTrkOverhead,
       "lportTrkUtil": lportTrkUtil,
       "lportVAvailbw": lportVAvailbw,
       "lportTrkLastTimeChange": lportTrkLastTimeChange,
       "lportCongestRate": lportCongestRate,
       "lportCongestRateThresh": lportCongestRateThresh,
       "lportDiagState": lportDiagState,
       "lportDiagOptionStr": lportDiagOptionStr,
       "lportDiagPassCount": lportDiagPassCount,
       "lportDiagFailCount": lportDiagFailCount,
       "lportDiagResultStr": lportDiagResultStr,
       "lportDs0BitStuff": lportDs0BitStuff,
       "lportErrorThreshold": lportErrorThreshold,
       "lportUnsyncBandwidth": lportUnsyncBandwidth,
       "lportDTEInStatusFrames": lportDTEInStatusFrames,
       "lportDTEInFullStatusFrames": lportDTEInFullStatusFrames,
       "lportDTEInAsyncStatusFrames": lportDTEInAsyncStatusFrames,
       "lportDTEInErrorFrames": lportDTEInErrorFrames,
       "lportDTEOutPollFrames": lportDTEOutPollFrames,
       "lportDTEPollErrorCounts": lportDTEPollErrorCounts,
       "lportDTEFailCounts": lportDTEFailCounts,
       "lportDTEFailReason": lportDTEFailReason,
       "lportDTEOperStatus": lportDTEOperStatus,
       "lportDCEInPollFrames": lportDCEInPollFrames,
       "lportDCEInErrorFrames": lportDCEInErrorFrames,
       "lportDCEOutStatusFrames": lportDCEOutStatusFrames,
       "lportDCEOutFullStatusFrames": lportDCEOutFullStatusFrames,
       "lportDCEOutAsyncStatusFrames": lportDCEOutAsyncStatusFrames,
       "lportDCEPollErrorCounts": lportDCEPollErrorCounts,
       "lportDCEFailCounts": lportDCEFailCounts,
       "lportDCEFailReason": lportDCEFailReason,
       "lportDCEOperStatus": lportDCEOperStatus,
       "lportDCEOperDlcmiStd": lportDCEOperDlcmiStd,
       "lportLMIInErrorFrames": lportLMIInErrorFrames,
       "lportDCEnN4": lportDCEnN4,
       "lportDCEnT3": lportDCEnT3,
       "lportXmitLatencyThreshold": lportXmitLatencyThreshold,
       "lportXmitRefillPriority0Percentage": lportXmitRefillPriority0Percentage,
       "lportXmitRefillPriority1Percentage": lportXmitRefillPriority1Percentage,
       "lportXmitRefillPriority2Percentage": lportXmitRefillPriority2Percentage,
       "lportXmitRefillPriority3Percentage": lportXmitRefillPriority3Percentage,
       "lportXmitDiscardLow": lportXmitDiscardLow,
       "lportSevereThreshold": lportSevereThreshold,
       "lportMildThreshold": lportMildThreshold,
       "lportTrkKeepAliveTimer": lportTrkKeepAliveTimer,
       "lportTrkKeepAliveErrorThreshold": lportTrkKeepAliveErrorThreshold,
       "lportIgCutThruStatus": lportIgCutThruStatus,
       "lportEgCutThruStatus": lportEgCutThruStatus,
       "lportEgCutThruThresh": lportEgCutThruThresh,
       "lportFrameRelayTrkEnable": lportFrameRelayTrkEnable,
       "lportSmdsSsiIf": lportSmdsSsiIf,
       "lportSmdsSsiSlot": lportSmdsSsiSlot,
       "lportSmdsScrnId": lportSmdsScrnId,
       "lportSmdsIaScrnOp": lportSmdsIaScrnOp,
       "lportSmdsGaScrnOp": lportSmdsGaScrnOp,
       "lportSmdsIaScrnMap": lportSmdsIaScrnMap,
       "lportSmdsGaScrnMap": lportSmdsGaScrnMap,
       "lportSmdsTrkAddr": lportSmdsTrkAddr,
       "lportSmdsCrc": lportSmdsCrc,
       "lportSmdsCpePoll": lportSmdsCpePoll,
       "lportSmdsPduCheck": lportSmdsPduCheck,
       "lportSmdsCntOutFrDxi2HbPolls": lportSmdsCntOutFrDxi2HbPolls,
       "lportSmdsCntOutByteDxi2HbPolls": lportSmdsCntOutByteDxi2HbPolls,
       "lportSmdsCntInFrDxi2HbPolls": lportSmdsCntInFrDxi2HbPolls,
       "lportSmdsCntInByteDxi2HbPolls": lportSmdsCntInByteDxi2HbPolls,
       "lportSmdsCntOutFrSip3s": lportSmdsCntOutFrSip3s,
       "lportSmdsCntOutByteSip3s": lportSmdsCntOutByteSip3s,
       "lportSmdsCntInFrSip3s": lportSmdsCntInFrSip3s,
       "lportSmdsCntInByteSip3s": lportSmdsCntInByteSip3s,
       "lportSmdsCntDxi2LinkIdInvalids": lportSmdsCntDxi2LinkIdInvalids,
       "lportSmdsCntDxi2StationIdInvalids": lportSmdsCntDxi2StationIdInvalids,
       "lportSmdsCntDxi2CrInvalids": lportSmdsCntDxi2CrInvalids,
       "lportSmdsCntDxi2AeInvalids": lportSmdsCntDxi2AeInvalids,
       "lportSmdsCntDxi2CtrlInvalids": lportSmdsCntDxi2CtrlInvalids,
       "lportSmdsCntDxi2FrameSizeErrors": lportSmdsCntDxi2FrameSizeErrors,
       "lportSmdsCntSip3RsvdInvalids": lportSmdsCntSip3RsvdInvalids,
       "lportSmdsCntSip3BetagMismatchs": lportSmdsCntSip3BetagMismatchs,
       "lportSmdsCntSip3BasizeIncorrects": lportSmdsCntSip3BasizeIncorrects,
       "lportSmdsCntSip3BasizeInvalids": lportSmdsCntSip3BasizeInvalids,
       "lportSmdsCntSip3DaTypeInvalids": lportSmdsCntSip3DaTypeInvalids,
       "lportSmdsCntSip3DaInvalids": lportSmdsCntSip3DaInvalids,
       "lportSmdsCntSip3SaTypeInvalids": lportSmdsCntSip3SaTypeInvalids,
       "lportSmdsCntSip3SaInvalids": lportSmdsCntSip3SaInvalids,
       "lportSmdsCntSip3BasizeMismatchs": lportSmdsCntSip3BasizeMismatchs,
       "lportSmdsCntSip3HeLenInvalids": lportSmdsCntSip3HeLenInvalids,
       "lportSmdsCntSip3HeVersionInvalids": lportSmdsCntSip3HeVersionInvalids,
       "lportSmdsCntSip3HeCarrierInvalids": lportSmdsCntSip3HeCarrierInvalids,
       "lportSmdsCntSip3Crc32Errors": lportSmdsCntSip3Crc32Errors,
       "lportSmdsCntSip3TRsvdInvalids": lportSmdsCntSip3TRsvdInvalids,
       "lportSmdsCntSaNotFounds": lportSmdsCntSaNotFounds,
       "lportSmdsCntSaValidationFails": lportSmdsCntSaValidationFails,
       "lportSmdsCntSaDaOnSamePorts": lportSmdsCntSaDaOnSamePorts,
       "lportSmdsCntDaSsiMismacths": lportSmdsCntDaSsiMismacths,
       "lportSmdsCntSsiProvisionErrors": lportSmdsCntSsiProvisionErrors,
       "lportSmdsCntDstIaNotFounds": lportSmdsCntDstIaNotFounds,
       "lportSmdsCntDstGaNotFounds": lportSmdsCntDstGaNotFounds,
       "lportSmdsCntSrcIaScrnFails": lportSmdsCntSrcIaScrnFails,
       "lportSmdsCntDstIaScrnFails": lportSmdsCntDstIaScrnFails,
       "lportSmdsCntDstGaScrnFails": lportSmdsCntDstGaScrnFails,
       "lportSmdsTotalDiscards": lportSmdsTotalDiscards,
       "lportSmdsSsiNode": lportSmdsSsiNode,
       "lportBilling": lportBilling,
       "lportSmdsReserved144": lportSmdsReserved144,
       "lportLinkStatus": lportLinkStatus,
       "lportLMIDelay": lportLMIDelay,
       "lportCRC": lportCRC,
       "lportSmdsMulticastGa": lportSmdsMulticastGa,
       "lportSmdsMulticastIpAddr": lportSmdsMulticastIpAddr,
       "lportAtmVPI": lportAtmVPI,
       "lportAtmVCI": lportAtmVCI,
       "lportPeakCellRateindex": lportPeakCellRateindex,
       "lportSustCellRate": lportSustCellRate,
       "lportBurstTolerance": lportBurstTolerance,
       "lportBuTrkOnFailure": lportBuTrkOnFailure,
       "lportTrkFailureThrsh": lportTrkFailureThrsh,
       "lportTrkRestThrsh": lportTrkRestThrsh,
       "lportBuTrkRetryInt": lportBuTrkRetryInt,
       "lportBuTrkRetryNum": lportBuTrkRetryNum,
       "lportBuTrkCycleInt": lportBuTrkCycleInt,
       "lportTrkManualBu": lportTrkManualBu,
       "lportPrimTrk": lportPrimTrk,
       "lportInitCallSetup": lportInitCallSetup,
       "lportBuFailReason": lportBuFailReason,
       "lportQ922Enable": lportQ922Enable,
       "lportQ922State": lportQ922State,
       "lportTrkPduRevision": lportTrkPduRevision,
       "lportPVCMgrPduRevision": lportPVCMgrPduRevision,
       "lportDS0LoopStatus": lportDS0LoopStatus,
       "lportISDNDuration": lportISDNDuration,
       "lportISDNSourceAddr": lportISDNSourceAddr,
       "lportISDNDestAddr": lportISDNDestAddr,
       "lportISDNIpAddr": lportISDNIpAddr,
       "lportISDNCallRejCause": lportISDNCallRejCause,
       "lportLastInvalidDLCI": lportLastInvalidDLCI,
       "lportTrkProtState": lportTrkProtState,
       "lportTrkTrafficMix": lportTrkTrafficMix,
       "lportNumVC": lportNumVC,
       "lportTrkAdminCost": lportTrkAdminCost,
       "lportPrivateNet": lportPrivateNet,
       "lportTrkStaticDelay": lportTrkStaticDelay,
       "lportTrkDynamicDelay": lportTrkDynamicDelay,
       "lportAtmDataRateQoS1": lportAtmDataRateQoS1,
       "lportAtmDataRateQoS2": lportAtmDataRateQoS2,
       "lportAtmDataRateQoS3": lportAtmDataRateQoS3,
       "lportAtmDataRateQoS4": lportAtmDataRateQoS4,
       "lportOutVAvailbwQoS1": lportOutVAvailbwQoS1,
       "lportOutVAvailbwQoS2": lportOutVAvailbwQoS2,
       "lportOutVAvailbwQoS3": lportOutVAvailbwQoS3,
       "lportOutVAvailbwQoS4": lportOutVAvailbwQoS4,
       "lportInVAvailbwQoS1": lportInVAvailbwQoS1,
       "lportInVAvailbwQoS2": lportInVAvailbwQoS2,
       "lportInVAvailbwQoS3": lportInVAvailbwQoS3,
       "lportInVAvailbwQoS4": lportInVAvailbwQoS4,
       "lportOutAllocbwQoS1": lportOutAllocbwQoS1,
       "lportOutAllocbwQoS2": lportOutAllocbwQoS2,
       "lportOutAllocbwQoS3": lportOutAllocbwQoS3,
       "lportOutAllocbwQoS4": lportOutAllocbwQoS4,
       "lportInAllocbwQoS1": lportInAllocbwQoS1,
       "lportInAllocbwQoS2": lportInAllocbwQoS2,
       "lportInAllocbwQoS3": lportInAllocbwQoS3,
       "lportInAllocbwQoS4": lportInAllocbwQoS4,
       "lportDynamicQoSbw": lportDynamicQoSbw,
       "lportSVCRetryTimer": lportSVCRetryTimer,
       "lportAtmNetworkType": lportAtmNetworkType,
       "lportAtmRouteMetricQoS1": lportAtmRouteMetricQoS1,
       "lportAtmRouteMetricQoS2": lportAtmRouteMetricQoS2,
       "lportAtmRouteMetricQoS3": lportAtmRouteMetricQoS3,
       "lportAtmRouteMetricQoS4": lportAtmRouteMetricQoS4,
       "lportIlmiPollTimeout": lportIlmiPollTimeout,
       "lportAtmProtocol": lportAtmProtocol,
       "lportIlmiAdminStatus": lportIlmiAdminStatus,
       "lportIlmiOperStatus": lportIlmiOperStatus,
       "lportIlmiPollRetry": lportIlmiPollRetry,
       "lportAtmVpiBits": lportAtmVpiBits,
       "lportAtmVciBits": lportAtmVciBits,
       "lportAtmOamAlarmEnable": lportAtmOamAlarmEnable,
       "lportInVAvailbw": lportInVAvailbw,
       "lportbwUNIPolicy": lportbwUNIPolicy,
       "lportStarvation": lportStarvation,
       "lportRecOverflow": lportRecOverflow,
       "lportLossOfCellSequence": lportLossOfCellSequence,
       "lportLossOfStructurePointer": lportLossOfStructurePointer,
       "lportCbrInsDummyCells": lportCbrInsDummyCells,
       "lportRecFifoUnderflowCnt": lportRecFifoUnderflowCnt,
       "lportRecFifoOverflowCnt": lportRecFifoOverflowCnt,
       "lportCbrLossOfStructurePointerCnt": lportCbrLossOfStructurePointerCnt,
       "lportCbrLossOfCellSequenceCnt": lportCbrLossOfCellSequenceCnt,
       "lportShaperId": lportShaperId,
       "lportIlmiPrefixScreenMode": lportIlmiPrefixScreenMode,
       "lportSmdsPduViolTca": lportSmdsPduViolTca,
       "lportSmdsPduViolThresh": lportSmdsPduViolThresh,
       "lportSmdsPduHdrSip3SaNotFound": lportSmdsPduHdrSip3SaNotFound,
       "lportSmdsPduHdrSip3SaDaOnSamePort": lportSmdsPduHdrSip3SaDaOnSamePort,
       "lportSmdsPduHdrSip3DstGaNotFound": lportSmdsPduHdrSip3DstGaNotFound,
       "lportSmdsPduHdrSip3DstIaScrnFail": lportSmdsPduHdrSip3DstIaScrnFail,
       "lportSmdsPduHdrSip3SaValFail": lportSmdsPduHdrSip3SaValFail,
       "lportSmdsPduHdrSip3DstIaNotFound": lportSmdsPduHdrSip3DstIaNotFound,
       "lportSmdsPduHdrSip3SrcIaScrnFail": lportSmdsPduHdrSip3SrcIaScrnFail,
       "lportSmdsPduHdrSip3DstGaScrnFail": lportSmdsPduHdrSip3DstGaScrnFail,
       "lportSmdsPduHdrSip3SaTypeInvalid": lportSmdsPduHdrSip3SaTypeInvalid,
       "lportSmdsPduHdrSip3DaTypeInvalid": lportSmdsPduHdrSip3DaTypeInvalid,
       "lportSmdsPduHdrDxi2LinkIdInvalid": lportSmdsPduHdrDxi2LinkIdInvalid,
       "lportSmdsPduHdrDxi2CrInvalid": lportSmdsPduHdrDxi2CrInvalid,
       "lportSmdsPduHdrDxi2CtrlInvalid": lportSmdsPduHdrDxi2CtrlInvalid,
       "lportSmdsPduHdrDxi2StationIdInvalid": lportSmdsPduHdrDxi2StationIdInvalid,
       "lportSmdsPduHdrDxi2AeInvalid": lportSmdsPduHdrDxi2AeInvalid,
       "lportDS0FarendLpbkEnabled": lportDS0FarendLpbkEnabled,
       "lportDS0FarendLpbkDisabled": lportDS0FarendLpbkDisabled,
       "lportTrkProtFailureThreshold": lportTrkProtFailureThreshold,
       "lportPtr": lportPtr,
       "lportISDNPoolUtil": lportISDNPoolUtil,
       "lportISDNIpAddrAssignFail": lportISDNIpAddrAssignFail,
       "lportTrkUtilQoS1": lportTrkUtilQoS1,
       "lportTrkUtilQoS2": lportTrkUtilQoS2,
       "lportTrkUtilQoS3": lportTrkUtilQoS3,
       "lportTrkUtilQoS4": lportTrkUtilQoS4,
       "lportInCells": lportInCells,
       "lportOutCells": lportOutCells,
       "ckt": ckt,
       "cktTable": cktTable,
       "cktEntry": cktEntry,
       "cktSrcIfIndex": cktSrcIfIndex,
       "cktSrcDlci": cktSrcDlci,
       "cktPriority": cktPriority,
       "cktCir": cktCir,
       "cktBc": cktBc,
       "cktBe": cktBe,
       "cktDestNodeId": cktDestNodeId,
       "cktDestIfIndex": cktDestIfIndex,
       "cktDestDlci": cktDestDlci,
       "cktTos": cktTos,
       "cktOde": cktOde,
       "cktAdminStatus": cktAdminStatus,
       "cktCreationTime": cktCreationTime,
       "cktLastTimeChange": cktLastTimeChange,
       "cktVcState": cktVcState,
       "cktDceState": cktDceState,
       "cktDteStatus": cktDteStatus,
       "cktRnr": cktRnr,
       "cktNiDown": cktNiDown,
       "cktDteState": cktDteState,
       "cktOperStatus": cktOperStatus,
       "cktOutForward": cktOutForward,
       "cktRerouteCnt": cktRerouteCnt,
       "cktVcPtr": cktVcPtr,
       "cktHopCnt": cktHopCnt,
       "cktPath": cktPath,
       "cktFailReason": cktFailReason,
       "cktFailNode": cktFailNode,
       "cktFailPort": cktFailPort,
       "cktMcastGroupId": cktMcastGroupId,
       "cktMcastMemberList": cktMcastMemberList,
       "cktMcastParentGroups": cktMcastParentGroups,
       "cktInFrames": cktInFrames,
       "cktInDEFrames": cktInDEFrames,
       "cktInODEFrames": cktInODEFrames,
       "cktInFECNFrames": cktInFECNFrames,
       "cktInBECNFrames": cktInBECNFrames,
       "cktInDiscards": cktInDiscards,
       "cktInOctets": cktInOctets,
       "cktInDEOctets": cktInDEOctets,
       "cktInODEOctets": cktInODEOctets,
       "cktOutFrames": cktOutFrames,
       "cktOutDEFrames": cktOutDEFrames,
       "cktOutODEFrames": cktOutODEFrames,
       "cktOutFECNFrames": cktOutFECNFrames,
       "cktOutBECNFrames": cktOutBECNFrames,
       "cktOutOctets": cktOutOctets,
       "cktOutDEOctets": cktOutDEOctets,
       "cktOutODEOctets": cktOutODEOctets,
       "cktOutLostFrames": cktOutLostFrames,
       "cktOutLostDEFrames": cktOutLostDEFrames,
       "cktOutLostODEFrames": cktOutLostODEFrames,
       "cktOutLostOctets": cktOutLostOctets,
       "cktOutLostDEOctets": cktOutLostDEOctets,
       "cktOutLostODEOctets": cktOutLostODEOctets,
       "cktRtMinDelay": cktRtMinDelay,
       "cktRtMaxDelay": cktRtMaxDelay,
       "cktRtAvgDelay": cktRtAvgDelay,
       "cktDiagTestId": cktDiagTestId,
       "cktDiagTestRuns": cktDiagTestRuns,
       "cktHelloCounter": cktHelloCounter,
       "cktHelloAckCounter": cktHelloAckCounter,
       "cktDefinedPath": cktDefinedPath,
       "cktDefinedPathCount": cktDefinedPathCount,
       "cktDefinedPathEnable": cktDefinedPathEnable,
       "cktDefinedPathAltOption": cktDefinedPathAltOption,
       "cktUsingDefinedPath": cktUsingDefinedPath,
       "cktTryAltPath": cktTryAltPath,
       "cktNotVirgin": cktNotVirgin,
       "cktInForward": cktInForward,
       "cktBtusSeg": cktBtusSeg,
       "cktInSegmentsDiscards": cktInSegmentsDiscards,
       "cktAtmVPI": cktAtmVPI,
       "cktAtmVCI": cktAtmVCI,
       "cktType": cktType,
       "cktSvcCallingParty": cktSvcCallingParty,
       "cktSvcCalledParty": cktSvcCalledParty,
       "cktSvcDuration": cktSvcDuration,
       "cktSvcCause": cktSvcCause,
       "cktXlatFlag": cktXlatFlag,
       "cktDestLaddr": cktDestLaddr,
       "cktSrcLaddr": cktSrcLaddr,
       "cktLoop": cktLoop,
       "cktRerouteBalance": cktRerouteBalance,
       "cktCallingBackup": cktCallingBackup,
       "cktRCir": cktRCir,
       "cktAtmQoS": cktAtmQoS,
       "cktAtmInCells": cktAtmInCells,
       "cktAtmOutCells": cktAtmOutCells,
       "cktAtmInDiscardedClp0Cells": cktAtmInDiscardedClp0Cells,
       "cktAtmInDiscardedClp1Cells": cktAtmInDiscardedClp1Cells,
       "cktAtmVcType": cktAtmVcType,
       "cktAtmPCR": cktAtmPCR,
       "cktAtmSCR": cktAtmSCR,
       "cktAtmMBS": cktAtmMBS,
       "cktAtmInPassedClp0Cells": cktAtmInPassedClp0Cells,
       "cktAtmInPassedClp1Cells": cktAtmInPassedClp1Cells,
       "cktAtmInTaggedCells": cktAtmInTaggedCells,
       "cktAtmOutClp0Cells": cktAtmOutClp0Cells,
       "cktAtmOutClp1Cells": cktAtmOutClp1Cells,
       "cktAtmRQoS": cktAtmRQoS,
       "cktAtmTfdType": cktAtmTfdType,
       "cktAtmRTfdType": cktAtmRTfdType,
       "cktAtmTfdParam1": cktAtmTfdParam1,
       "cktAtmTfdParam2": cktAtmTfdParam2,
       "cktAtmTfdParam3": cktAtmTfdParam3,
       "cktAtmRTfdParam1": cktAtmRTfdParam1,
       "cktAtmRTfdParam2": cktAtmRTfdParam2,
       "cktAtmRTfdParam3": cktAtmRTfdParam3,
       "cktAtmFrameIWF": cktAtmFrameIWF,
       "cktAtmUserPlane": cktAtmUserPlane,
       "cktRBc": cktRBc,
       "cktRBe": cktRBe,
       "cktOamLoopbackDirection": cktOamLoopbackDirection,
       "cktOamLoopbackType": cktOamLoopbackType,
       "cktOamLoopbackHops": cktOamLoopbackHops,
       "cktOamLoopbackCount": cktOamLoopbackCount,
       "cktOamLoopbackReceived": cktOamLoopbackReceived,
       "cktOamLoopbackTimeouts": cktOamLoopbackTimeouts,
       "cktOamLoopbackReceivedHigh": cktOamLoopbackReceivedHigh,
       "cktOamLoopbackReceivedLow": cktOamLoopbackReceivedLow,
       "cktOamLoopbackReceivedAvg": cktOamLoopbackReceivedAvg,
       "cktOamAlarmDisable": cktOamAlarmDisable,
       "cktShaperId": cktShaperId,
       "cktOspfCtd": cktOspfCtd,
       "cktOspfCdv": cktOspfCdv,
       "cktOutPort": cktOutPort,
       "cktOutVc": cktOutVc,
       "cktRVc": cktRVc,
       "cktEntryType": cktEntryType,
       "cktDiagStr": cktDiagStr,
       "cktSvcAalType": cktSvcAalType,
       "cktSvcBBearerClass": cktSvcBBearerClass,
       "cktSvcBBearerClippingSusc": cktSvcBBearerClippingSusc,
       "cktSvcBBearerTmgReq": cktSvcBBearerTmgReq,
       "cktSvcBBearerTfcType": cktSvcBBearerTfcType,
       "cktAtmUPCEnable": cktAtmUPCEnable,
       "cktRPriority": cktRPriority,
       "cktRtPriority": cktRtPriority,
       "cktDeltaBc": cktDeltaBc,
       "cktDeltaBe": cktDeltaBe,
       "cktDeltaRBc": cktDeltaRBc,
       "cktDeltaRBe": cktDeltaRBe,
       "cktRedFrPcnt": cktRedFrPcnt,
       "cktRedFrRPcnt": cktRedFrRPcnt,
       "cktRateEnforceSchm": cktRateEnforceSchm,
       "cktRateEnforceRSchm": cktRateEnforceRSchm,
       "cktROde": cktROde,
       "cktPrivateNet": cktPrivateNet,
       "cktPrivateNetOverflow": cktPrivateNetOverflow,
       "cktCustomerID": cktCustomerID,
       "cktAtmCDVT": cktAtmCDVT,
       "cktNdcEnable": cktNdcEnable,
       "cktInterworkingFrToAtmCLP": cktInterworkingFrToAtmCLP,
       "cktInterworkingFrToAtmDe": cktInterworkingFrToAtmDe,
       "cktNrtsCLP1": cktNrtsCLP1,
       "cktNrtsDiscardClp0": cktNrtsDiscardClp0,
       "cktNrtsDiscardClp1": cktNrtsDiscardClp1,
       "cktMPEnableAMF": cktMPEnableAMF,
       "cktMPEligible": cktMPEligible,
       "cktMPForcedCaller": cktMPForcedCaller,
       "cktMPForcedCallee": cktMPForcedCallee,
       "cktFrameSize": cktFrameSize,
       "cktRFrameSize": cktRFrameSize,
       "cktRNrtsCLP1": cktRNrtsCLP1,
       "cktBBearerAtmTransferCapability": cktBBearerAtmTransferCapability,
       "cktAtmFrameDiscard": cktAtmFrameDiscard,
       "cktRAtmFrameDiscard": cktRAtmFrameDiscard,
       "cktAbrFRMRTT": cktAbrFRMRTT,
       "cktAbrICR": cktAbrICR,
       "cktRAbrICR": cktRAbrICR,
       "cktAbrRIF": cktAbrRIF,
       "cktRAbrRIF": cktRAbrRIF,
       "cktAbrRDF": cktAbrRDF,
       "cktRAbrRDF": cktRAbrRDF,
       "cktAbrTBE": cktAbrTBE,
       "cktRAbrTBE": cktRAbrTBE,
       "cktAbrNRM": cktAbrNRM,
       "cktRAbrNRM": cktRAbrNRM,
       "cktAbrTRM": cktAbrTRM,
       "cktRAbrTRM": cktRAbrTRM,
       "cktAbrCDF": cktAbrCDF,
       "cktRAbrCDF": cktRAbrCDF,
       "cktAbrADTF": cktAbrADTF,
       "cktRAbrADTF": cktRAbrADTF,
       "cktAccumCTD": cktAccumCTD,
       "cktAccumCDV": cktAccumCDV,
       "cktAccumRCDV": cktAccumRCDV,
       "cktCLR": cktCLR,
       "cktRCLR": cktRCLR,
       "cktAtmLijId": cktAtmLijId,
       "cktAtmLijType": cktAtmLijType,
       "cktRtLastDelay": cktRtLastDelay,
       "cktRtAccuMinDelay": cktRtAccuMinDelay,
       "cktRtAccuMaxDelay": cktRtAccuMaxDelay,
       "cktRtAccuAvgDelay": cktRtAccuAvgDelay,
       "cktQosIntPeriod": cktQosIntPeriod,
       "cktAtmOutOAMClp0Cells": cktAtmOutOAMClp0Cells,
       "cktAtmOutOAMClp1Cells": cktAtmOutOAMClp1Cells,
       "cktReqCTD": cktReqCTD,
       "cktInOctetsPeak": cktInOctetsPeak,
       "cktOutOctetsPeak": cktOutOctetsPeak,
       "cktInDEOctetsPeak": cktInDEOctetsPeak,
       "cktOutDEOctetsPeak": cktOutDEOctetsPeak,
       "cktInODEOctetsPeak": cktInODEOctetsPeak,
       "cktOutODEOctetsPeak": cktOutODEOctetsPeak,
       "cktAdminCostThreshold": cktAdminCostThreshold,
       "cktAtmSvcServiceCategory": cktAtmSvcServiceCategory,
       "cktAtmSvcRServiceCategory": cktAtmSvcRServiceCategory,
       "cktInterworkingFrToAtmEFCI": cktInterworkingFrToAtmEFCI,
       "cktDiagSARMon": cktDiagSARMon,
       "cktAdminCostReal": cktAdminCostReal,
       "cktAtmInClp0Cells": cktAtmInClp0Cells,
       "cktAtmInClp1Cells": cktAtmInClp1Cells,
       "cktATMAAL5CRC32Error": cktATMAAL5CRC32Error,
       "cktATMAAL5CPIError": cktATMAAL5CPIError,
       "cktATMAAL5LengthError": cktATMAAL5LengthError,
       "cktATMAAL5ReassemblyTimerError": cktATMAAL5ReassemblyTimerError,
       "cktATMAAL5MaxNrSegError": cktATMAAL5MaxNrSegError,
       "cktIWF1490to1483Error": cktIWF1490to1483Error,
       "cktIWF1490to1483LastBadHeader": cktIWF1490to1483LastBadHeader,
       "cktIWF1483to1490Error": cktIWF1483to1490Error,
       "cktIWF1483to1490LastBadHeader": cktIWF1483to1490LastBadHeader,
       "cktLeafTable": cktLeafTable,
       "cktLeafEntry": cktLeafEntry,
       "cktLeafSrcIfIndex": cktLeafSrcIfIndex,
       "cktLeafSrcDlci": cktLeafSrcDlci,
       "cktLeafEndpointIndex": cktLeafEndpointIndex,
       "cktLeafCreationTime": cktLeafCreationTime,
       "cktLeafEgressIfIndex": cktLeafEgressIfIndex,
       "cktLeafEgressDlci": cktLeafEgressDlci,
       "cktLeafDestNodeId": cktLeafDestNodeId,
       "cktLeafDestIfIndex": cktLeafDestIfIndex,
       "cktLeafDestDlci": cktLeafDestDlci,
       "cktLeafSvcCallingParty": cktLeafSvcCallingParty,
       "cktLeafSvcCalledParty": cktLeafSvcCalledParty,
       "cktLeafAdminStatus": cktLeafAdminStatus,
       "cktLeafVcState": cktLeafVcState,
       "cktLeafOperStatus": cktLeafOperStatus,
       "cktLeafDceState": cktLeafDceState,
       "cktLeafDteStatus": cktLeafDteStatus,
       "cktLeafDteState": cktLeafDteState,
       "cktLeafVcPtr": cktLeafVcPtr,
       "cktLeafHopCnt": cktLeafHopCnt,
       "cktLeafPath": cktLeafPath,
       "cktLeafFailReason": cktLeafFailReason,
       "cktLeafFailNode": cktLeafFailNode,
       "cktLeafFailPort": cktLeafFailPort,
       "cktLeafHelloCounter": cktLeafHelloCounter,
       "cktLeafHelloAckCounter": cktLeafHelloAckCounter,
       "cktLeafAtmVPI": cktLeafAtmVPI,
       "cktLeafAtmVCI": cktLeafAtmVCI,
       "cktLeafType": cktLeafType,
       "cktLeafAtmInCells": cktLeafAtmInCells,
       "cktLeafAtmOutCells": cktLeafAtmOutCells,
       "cktLeafAtmInDiscardedClp0Cells": cktLeafAtmInDiscardedClp0Cells,
       "cktLeafAtmInDiscardedClp1Cells": cktLeafAtmInDiscardedClp1Cells,
       "cktLeafAtmInPassedClp0Cells": cktLeafAtmInPassedClp0Cells,
       "cktLeafAtmInPassedClp1Cells": cktLeafAtmInPassedClp1Cells,
       "cktLeafAtmInTaggedCells": cktLeafAtmInTaggedCells,
       "cktLeafAtmOutClp0Cells": cktLeafAtmOutClp0Cells,
       "cktLeafAtmOutClp1Cells": cktLeafAtmOutClp1Cells,
       "cktSmdsRtTable": cktSmdsRtTable,
       "cktSmdsRtEntry": cktSmdsRtEntry,
       "cktSmdsRemoteNode": cktSmdsRemoteNode,
       "cktSmdsHopCnt": cktSmdsHopCnt,
       "cktSmdsRoute": cktSmdsRoute,
       "cktSmdsLocalPort": cktSmdsLocalPort,
       "cktSmdsRemotePort": cktSmdsRemotePort,
       "cktSmdsVcState": cktSmdsVcState,
       "card": card,
       "cardNumber": cardNumber,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardLogicalSlotId": cardLogicalSlotId,
       "cardPhysicalSlotId": cardPhysicalSlotId,
       "cardAdminType": cardAdminType,
       "cardOperType": cardOperType,
       "cardState": cardState,
       "cardAdminStatus": cardAdminStatus,
       "cardOperStatus": cardOperStatus,
       "cardDiagStatus": cardDiagStatus,
       "cardRedundConfig": cardRedundConfig,
       "cardRedundSlotMask": cardRedundSlotMask,
       "cardRedundActual": cardRedundActual,
       "cardRedundState": cardRedundState,
       "cardToRedundant": cardToRedundant,
       "cardDiagNonFatalSource": cardDiagNonFatalSource,
       "cardDiagNonFatalTime": cardDiagNonFatalTime,
       "cardDiagNonFatalErrMajor": cardDiagNonFatalErrMajor,
       "cardDiagNonFatalErrMinor": cardDiagNonFatalErrMinor,
       "cardDiagNonFatalStr": cardDiagNonFatalStr,
       "cardDiagFatalSource": cardDiagFatalSource,
       "cardDiagFatalTime": cardDiagFatalTime,
       "cardDiagFatalErrMajor": cardDiagFatalErrMajor,
       "cardDiagFatalErrMinor": cardDiagFatalErrMinor,
       "cardDiagFatalStr": cardDiagFatalStr,
       "cardDiagFatalReboots": cardDiagFatalReboots,
       "cardDiagFatalAddress": cardDiagFatalAddress,
       "cardDiagBackgroundPasses": cardDiagBackgroundPasses,
       "cardDiagBackgroundFailures": cardDiagBackgroundFailures,
       "cardDiagBackgroundSuccesses": cardDiagBackgroundSuccesses,
       "cardDiagLEDReset": cardDiagLEDReset,
       "cardDiagPowerExtensive": cardDiagPowerExtensive,
       "cardCpuUtil": cardCpuUtil,
       "cardMemoryUsage": cardMemoryUsage,
       "cardMaxVCs": cardMaxVCs,
       "cardInUseVCs": cardInUseVCs,
       "cardFreeVCs": cardFreeVCs,
       "cardInOctets": cardInOctets,
       "cardInPkts": cardInPkts,
       "cardOutOctets": cardOutOctets,
       "cardOutPkts": cardOutPkts,
       "cardToWarmboot": cardToWarmboot,
       "cardToColdboot": cardToColdboot,
       "cardModel": cardModel,
       "cardSerial": cardSerial,
       "cardSwRev": cardSwRev,
       "cardHwRev": cardHwRev,
       "cardEpromRev": cardEpromRev,
       "cardName": cardName,
       "cardCktGroupTrap": cardCktGroupTrap,
       "cardOutBtus": cardOutBtus,
       "cardInGoodBtus": cardInGoodBtus,
       "cardInErrorBtus": cardInErrorBtus,
       "cardInNoVcBtus": cardInNoVcBtus,
       "cardInLinkDownBtus": cardInLinkDownBtus,
       "cardInNoBufferBtus": cardInNoBufferBtus,
       "cardInForwardBitBtus": cardInForwardBitBtus,
       "cardDiagTestId": cardDiagTestId,
       "cardDiagTestRuns": cardDiagTestRuns,
       "cardDiagState": cardDiagState,
       "cardDiagOptionStr": cardDiagOptionStr,
       "cardDiagPasses": cardDiagPasses,
       "cardDiagFailures": cardDiagFailures,
       "cardDiagResultString": cardDiagResultString,
       "cardFrameMemoryUtil": cardFrameMemoryUtil,
       "cardResetPram": cardResetPram,
       "cardMemoryUtil": cardMemoryUtil,
       "cardFrameMemoryUsage": cardFrameMemoryUsage,
       "cardUpTime": cardUpTime,
       "cardPramChecksum": cardPramChecksum,
       "cardPhysicalIndex": cardPhysicalIndex,
       "cardExternalClockRate": cardExternalClockRate,
       "cardShootState": cardShootState,
       "cardEraseAll": cardEraseAll,
       "cardAdminCapability": cardAdminCapability,
       "cardOperCapability": cardOperCapability,
       "cardISDNswtype": cardISDNswtype,
       "cardCpuFgUtil": cardCpuFgUtil,
       "cardTrkProtState": cardTrkProtState,
       "cardISDNSigType": cardISDNSigType,
       "cardISDNChanId": cardISDNChanId,
       "cardTransmitClockConfig": cardTransmitClockConfig,
       "cardTransmitClockSwitchOver": cardTransmitClockSwitchOver,
       "cardTransmitClockStatus": cardTransmitClockStatus,
       "cardSystemPrimaryClockPortConfig": cardSystemPrimaryClockPortConfig,
       "cardSystemPrimaryClockStatus": cardSystemPrimaryClockStatus,
       "cardSystemSecondaryClockPortConfig": cardSystemSecondaryClockPortConfig,
       "cardSystemSecondaryClockStatus": cardSystemSecondaryClockStatus,
       "cardInCells": cardInCells,
       "cardInErrorCells": cardInErrorCells,
       "cardInErrorVPIVCI": cardInErrorVPIVCI,
       "cardOutCells": cardOutCells,
       "cardOutDiscardCells": cardOutDiscardCells,
       "cardQOSQueueSize": cardQOSQueueSize,
       "cardLastErrorPort": cardLastErrorPort,
       "cardLastErrorVPI": cardLastErrorVPI,
       "cardLastErrorVCI": cardLastErrorVCI,
       "cardSystemPrimaryClockModeConfig": cardSystemPrimaryClockModeConfig,
       "cardSystemSecondaryClockModeConfig": cardSystemSecondaryClockModeConfig,
       "cardNFBDEStatus": cardNFBDEStatus,
       "cardProductCode": cardProductCode,
       "cardMfgPN": cardMfgPN,
       "cardTotalUpTime": cardTotalUpTime,
       "cardIOAType": cardIOAType,
       "cardIOAHwRev": cardIOAHwRev,
       "cardIOASerial": cardIOASerial,
       "cardIOAProductCode": cardIOAProductCode,
       "cardIOAMfgPN": cardIOAMfgPN,
       "cardDS0Support": cardDS0Support,
       "cardDiagParamId": cardDiagParamId,
       "cardDiagParamValue": cardDiagParamValue,
       "cardBulkStatsPeakCapability": cardBulkStatsPeakCapability,
       "cardBulkStatsTotalCapability": cardBulkStatsTotalCapability,
       "cardBulkStatsPeakEnable": cardBulkStatsPeakEnable,
       "cardBulkStatsTotalEnable": cardBulkStatsTotalEnable,
       "cardBulkStatsBaseCollectPeriod": cardBulkStatsBaseCollectPeriod,
       "cardNrtsHwRev": cardNrtsHwRev,
       "cardNrtsOutCellBufSize": cardNrtsOutCellBufSize,
       "cardNrtsOperState": cardNrtsOperState,
       "cardNrtsAdminState": cardNrtsAdminState,
       "cardNrtsCcrmProtocolId": cardNrtsCcrmProtocolId,
       "cardNrtsBcmProtocolId": cardNrtsBcmProtocolId,
       "cardNrtsRmGenInterval": cardNrtsRmGenInterval,
       "cardNrtsIdleCktThresh": cardNrtsIdleCktThresh,
       "cardNrtsVbrNrtManage": cardNrtsVbrNrtManage,
       "cardNrtsIcrFact": cardNrtsIcrFact,
       "cardNrtsMcastDiscardThresh": cardNrtsMcastDiscardThresh,
       "cardNrtsMcastDiscardCount": cardNrtsMcastDiscardCount,
       "cardAdminIOAType": cardAdminIOAType,
       "cardNrtsMcastRate": cardNrtsMcastRate,
       "cardMonStatus": cardMonStatus,
       "cardImageSetA": cardImageSetA,
       "cardImageSetB": cardImageSetB,
       "cardMacAddress": cardMacAddress,
       "cardFlashRev": cardFlashRev,
       "cardRequiredCapabilityBitmask": cardRequiredCapabilityBitmask,
       "cardOperCapabilityBitmask": cardOperCapabilityBitmask,
       "cardDslModule": cardDslModule,
       "cardIPTableSize": cardIPTableSize,
       "cardIPTableState": cardIPTableState,
       "cardATMTcaInBufOverflowAlertPeriod": cardATMTcaInBufOverflowAlertPeriod,
       "cardATMTcaInBufOverflowThresh": cardATMTcaInBufOverflowThresh,
       "cardATMTcaInInvalidVpiVciAlertPeriod": cardATMTcaInInvalidVpiVciAlertPeriod,
       "cardATMTcaInInvalidVpiVciThresh": cardATMTcaInInvalidVpiVciThresh,
       "cardATMTcaInATMDCFullAlertPeriod": cardATMTcaInATMDCFullAlertPeriod,
       "cardATMTcaInATMDCFullThresh": cardATMTcaInATMDCFullThresh,
       "cardATMTcaEnable": cardATMTcaEnable,
       "cardATMTcaId": cardATMTcaId,
       "cardATMTcaECidLookupFailureAlertPeriod": cardATMTcaECidLookupFailureAlertPeriod,
       "cardATMTcaECidLookupThresh": cardATMTcaECidLookupThresh,
       "cardATMTcaSPPearlOCbrFailureAlertPeriod": cardATMTcaSPPearlOCbrFailureAlertPeriod,
       "cardATMTcaSPPearlOCbrThresh": cardATMTcaSPPearlOCbrThresh,
       "cardATMTcaSPPearlOAbrFailureAlertPeriod": cardATMTcaSPPearlOAbrFailureAlertPeriod,
       "cardATMTcaSPPearlOAbrThresh": cardATMTcaSPPearlOAbrThresh,
       "cardATMTcaSPPearlOVbr1FailureAlertPeriod": cardATMTcaSPPearlOVbr1FailureAlertPeriod,
       "cardATMTcaSPPearlOVbr1Thresh": cardATMTcaSPPearlOVbr1Thresh,
       "cardATMTcaSPPearlOVbr2FailureAlertPeriod": cardATMTcaSPPearlOVbr2FailureAlertPeriod,
       "cardATMTcaSPPearlOVbr2Thresh": cardATMTcaSPPearlOVbr2Thresh,
       "cardATMTcaSPPearlGCbrFailureAlertPeriod": cardATMTcaSPPearlGCbrFailureAlertPeriod,
       "cardATMTcaSPPearlGCbrThresh": cardATMTcaSPPearlGCbrThresh,
       "cardATMTcaSPPearlGAbrFailureAlertPeriod": cardATMTcaSPPearlGAbrFailureAlertPeriod,
       "cardATMTcaSPPearlGAbrThresh": cardATMTcaSPPearlGAbrThresh,
       "cardATMTcaSPPearlGVbr1FailureAlertPeriod": cardATMTcaSPPearlGVbr1FailureAlertPeriod,
       "cardATMTcaSPPearlGVbr1Thresh": cardATMTcaSPPearlGVbr1Thresh,
       "cardATMTcaSPPearlGVbr2FailureAlertPeriod": cardATMTcaSPPearlGVbr2FailureAlertPeriod,
       "cardATMTcaSPPearlGVbr2Thresh": cardATMTcaSPPearlGVbr2Thresh,
       "cardATMTcaSPEnable": cardATMTcaSPEnable,
       "cardSPEFCIEnable": cardSPEFCIEnable,
       "cardSPClpEnable": cardSPClpEnable,
       "spATMTcaId": spATMTcaId,
       "cardSubcardToRedundant": cardSubcardToRedundant,
       "cardMemory5Usage": cardMemory5Usage,
       "cardSF1OperStatus": cardSF1OperStatus,
       "cardSF2OperStatus": cardSF2OperStatus,
       "cardTM1OperStatus": cardTM1OperStatus,
       "cardTM2OperStatus": cardTM2OperStatus,
       "cardMemStartLog": cardMemStartLog,
       "cardMemLogLevel": cardMemLogLevel,
       "cardMemClrLog": cardMemClrLog,
       "cardValidSubcards": cardValidSubcards,
       "cardClp0CbrThreshold": cardClp0CbrThreshold,
       "cardClp01CbrThreshold": cardClp01CbrThreshold,
       "cardClp0VbrRtThreshold": cardClp0VbrRtThreshold,
       "cardClp01VbrRtThreshold": cardClp01VbrRtThreshold,
       "cardClp0VbrNrtThreshold": cardClp0VbrNrtThreshold,
       "cardClp01VbrNrtThreshold": cardClp01VbrNrtThreshold,
       "cardClp0UAbrThreshold": cardClp0UAbrThreshold,
       "cardClp01UAbrThreshold": cardClp01UAbrThreshold,
       "cardControlMessagesFromBus": cardControlMessagesFromBus,
       "cardControlMessagesToBus": cardControlMessagesToBus,
       "cardBTUsFromBus": cardBTUsFromBus,
       "cardBTUsToBus": cardBTUsToBus,
       "cardInvalidPvcBTUs": cardInvalidPvcBTUs,
       "cardIncompleteFramesFromBus": cardIncompleteFramesFromBus,
       "cardBTUsBusErrors": cardBTUsBusErrors,
       "cardBTUsNoResource": cardBTUsNoResource,
       "cardInvalidPvcBTUsThreshold": cardInvalidPvcBTUsThreshold,
       "cardIncompleteFramesFromBusThreshold": cardIncompleteFramesFromBusThreshold,
       "cardBTUsBusErrorThreshold": cardBTUsBusErrorThreshold,
       "cardBTUsNoResourceThreshold": cardBTUsNoResourceThreshold,
       "cardFrameMemoryThreshold": cardFrameMemoryThreshold,
       "cardHoldQFrameMemory": cardHoldQFrameMemory,
       "cardTotalAAL5RxErrorCount": cardTotalAAL5RxErrorCount,
       "cardOperMemSize": cardOperMemSize,
       "ds1": ds1,
       "dsx1ConfigTable": dsx1ConfigTable,
       "dsx1ConfigEntry": dsx1ConfigEntry,
       "dsx1SlotId": dsx1SlotId,
       "dsx1PortId": dsx1PortId,
       "dsx1TimeElapsed": dsx1TimeElapsed,
       "dsx1ValidIntervals": dsx1ValidIntervals,
       "dsx1LineType": dsx1LineType,
       "dsx1LineCoding": dsx1LineCoding,
       "dsx1SendCode": dsx1SendCode,
       "dsx1CircuitIdentifier": dsx1CircuitIdentifier,
       "dsx1LoopbackConfig": dsx1LoopbackConfig,
       "dsx1LineStatus": dsx1LineStatus,
       "dsx1SignalMode": dsx1SignalMode,
       "dsx1TransmitClockSource": dsx1TransmitClockSource,
       "dsx1Fdl": dsx1Fdl,
       "dsx1FdlVersion": dsx1FdlVersion,
       "dsx1CurrentTable": dsx1CurrentTable,
       "dsx1CurrentEntry": dsx1CurrentEntry,
       "dsx1CurrentSlotId": dsx1CurrentSlotId,
       "dsx1CurrentPortId": dsx1CurrentPortId,
       "dsx1CurrentESs": dsx1CurrentESs,
       "dsx1CurrentSESs": dsx1CurrentSESs,
       "dsx1CurrentSEFSs": dsx1CurrentSEFSs,
       "dsx1CurrentUASs": dsx1CurrentUASs,
       "dsx1CurrentCSSs": dsx1CurrentCSSs,
       "dsx1CurrentBESs": dsx1CurrentBESs,
       "dsx1IntervalTable": dsx1IntervalTable,
       "dsx1IntervalEntry": dsx1IntervalEntry,
       "dsx1IntervalSlotId": dsx1IntervalSlotId,
       "dsx1IntervalPortId": dsx1IntervalPortId,
       "dsx1IntervalNumber": dsx1IntervalNumber,
       "dsx1IntervalESs": dsx1IntervalESs,
       "dsx1IntervalSESs": dsx1IntervalSESs,
       "dsx1IntervalSEFSs": dsx1IntervalSEFSs,
       "dsx1IntervalUASs": dsx1IntervalUASs,
       "dsx1IntervalCSSs": dsx1IntervalCSSs,
       "dsx1IntervalBESs": dsx1IntervalBESs,
       "dsx1TotalTable": dsx1TotalTable,
       "dsx1TotalEntry": dsx1TotalEntry,
       "dsx1TotalSlotId": dsx1TotalSlotId,
       "dsx1TotalPortId": dsx1TotalPortId,
       "dsx1TotalESs": dsx1TotalESs,
       "dsx1TotalSESs": dsx1TotalSESs,
       "dsx1TotalSEFSs": dsx1TotalSEFSs,
       "dsx1TotalUASs": dsx1TotalUASs,
       "dsx1TotalCSSs": dsx1TotalCSSs,
       "dsx1TotalBESs": dsx1TotalBESs,
       "cascsmds": cascsmds,
       "smdsaddr": smdsaddr,
       "smdsaddrTable": smdsaddrTable,
       "smdsaddrEntry": smdsaddrEntry,
       "smdsaddrAddr": smdsaddrAddr,
       "smdsaddrType": smdsaddrType,
       "smdsaddrId": smdsaddrId,
       "smdsaddrIf": smdsaddrIf,
       "smdsaddrParentGrpMap": smdsaddrParentGrpMap,
       "smdsaddrParentScrnMap": smdsaddrParentScrnMap,
       "smdsaddrMemberAddrMap": smdsaddrMemberAddrMap,
       "smdsaddrAdminStatus": smdsaddrAdminStatus,
       "smdsaddrSlot": smdsaddrSlot,
       "smdsaddrSsiIfNum": smdsaddrSsiIfNum,
       "namebinding": namebinding,
       "namebindingTable": namebindingTable,
       "namebindingEntry": namebindingEntry,
       "nameType": nameType,
       "nameName": nameName,
       "namePrimary": namePrimary,
       "nameIfIndex": nameIfIndex,
       "nameNodeId": nameNodeId,
       "nameStatus": nameStatus,
       "isdnaddr": isdnaddr,
       "isdnAddrTable": isdnAddrTable,
       "isdnAddrEntry": isdnAddrEntry,
       "isdnAddrIf": isdnAddrIf,
       "isdnAddr": isdnAddr,
       "isdnChanType": isdnChanType,
       "isdnCallerIDTable": isdnCallerIDTable,
       "isdnCallerIDEntry": isdnCallerIDEntry,
       "isdnCallerIDIf": isdnCallerIDIf,
       "isdnCallerIDAddr": isdnCallerIDAddr,
       "isdnCallerAdminStatus": isdnCallerAdminStatus,
       "cascsvc": cascsvc,
       "svcAtmFailedCall": svcAtmFailedCall,
       "svcAtmSigStatusChange": svcAtmSigStatusChange,
       "svcaddress": svcaddress,
       "svcNodePrefixTable": svcNodePrefixTable,
       "svcNodePrefixEntry": svcNodePrefixEntry,
       "svcNodePrefixPrefix": svcNodePrefixPrefix,
       "svcNodePrefixNumBits": svcNodePrefixNumBits,
       "svcNodePrefixNmbPlan": svcNodePrefixNmbPlan,
       "svcNodePrefixAdminStatus": svcNodePrefixAdminStatus,
       "svcPrefixTable": svcPrefixTable,
       "svcPrefixEntry": svcPrefixEntry,
       "svcPrefixIfIndex": svcPrefixIfIndex,
       "svcPrefixPrefix": svcPrefixPrefix,
       "svcPrefixNumBits": svcPrefixNumBits,
       "svcPrefixNmbPlan": svcPrefixNmbPlan,
       "svcPrefixAdminCost": svcPrefixAdminCost,
       "svcPrefixLocalGatewayAddress": svcPrefixLocalGatewayAddress,
       "svcPrefixLocalGatewayNmbPlan": svcPrefixLocalGatewayNmbPlan,
       "svcPrefixRemoteGatewayAddress": svcPrefixRemoteGatewayAddress,
       "svcPrefixRemoteGatewayNmbPlan": svcPrefixRemoteGatewayNmbPlan,
       "svcPrefixAdminStatus": svcPrefixAdminStatus,
       "svcAddrTable": svcAddrTable,
       "svcAddrEntry": svcAddrEntry,
       "svcAddrIfIndex": svcAddrIfIndex,
       "svcAddrAddress": svcAddrAddress,
       "svcAddrNmbPlan": svcAddrNmbPlan,
       "svcAddrAdminStatus": svcAddrAdminStatus,
       "svcAtmUserPartTable": svcAtmUserPartTable,
       "svcAtmUserPartEntry": svcAtmUserPartEntry,
       "svcAtmUserPartIfIndex": svcAtmUserPartIfIndex,
       "svcAtmUserPartUserPart": svcAtmUserPartUserPart,
       "svcAtmUserPartAdminStatus": svcAtmUserPartAdminStatus,
       "svcmgt": svcmgt,
       "svcConfigTable": svcConfigTable,
       "svcConfigEntry": svcConfigEntry,
       "svcConfigIfIndex": svcConfigIfIndex,
       "svcConfigInitiateIdentStatsUpload": svcConfigInitiateIdentStatsUpload,
       "svcConfigCgPtyInsertionMode": svcConfigCgPtyInsertionMode,
       "svcConfigCgPtyInsertionAddress": svcConfigCgPtyInsertionAddress,
       "svcConfigCgPtyInsertionNmbPlan": svcConfigCgPtyInsertionNmbPlan,
       "svcConfigCgPtyScreenMode": svcConfigCgPtyScreenMode,
       "svcConfigEgressAddrXlateMode": svcConfigEgressAddrXlateMode,
       "svcConfigIngressAddrXlateMode": svcConfigIngressAddrXlateMode,
       "svcConfigCgPtyPresentationMode": svcConfigCgPtyPresentationMode,
       "svcAtmConfigTable": svcAtmConfigTable,
       "svcAtmConfigEntry": svcAtmConfigEntry,
       "svcAtmConfigIfIndex": svcAtmConfigIfIndex,
       "svcAtmConfigAdminStatus": svcAtmConfigAdminStatus,
       "svcAtmConfigOperStatus": svcAtmConfigOperStatus,
       "svcAtmConfigQ93bMaxRestart": svcAtmConfigQ93bMaxRestart,
       "svcAtmConfigQ93bMaxStatEnq": svcAtmConfigQ93bMaxStatEnq,
       "svcAtmConfigQ93bT303": svcAtmConfigQ93bT303,
       "svcAtmConfigQ93bT308": svcAtmConfigQ93bT308,
       "svcAtmConfigQ93bT309": svcAtmConfigQ93bT309,
       "svcAtmConfigQ93bT310": svcAtmConfigQ93bT310,
       "svcAtmConfigQ93bT313": svcAtmConfigQ93bT313,
       "svcAtmConfigQ93bT316": svcAtmConfigQ93bT316,
       "svcAtmConfigQ93bT322": svcAtmConfigQ93bT322,
       "svcAtmConfigQ93bT398": svcAtmConfigQ93bT398,
       "svcAtmConfigQ93bT399": svcAtmConfigQ93bT399,
       "svcAtmConfigQ93bTotalConns": svcAtmConfigQ93bTotalConns,
       "svcAtmConfigQ93bActiveConns": svcAtmConfigQ93bActiveConns,
       "svcAtmConfigQ93bLastCauseTx": svcAtmConfigQ93bLastCauseTx,
       "svcAtmConfigQ93bLastCauseRx": svcAtmConfigQ93bLastCauseRx,
       "svcAtmConfigQ93bNumSetupPduTx": svcAtmConfigQ93bNumSetupPduTx,
       "svcAtmConfigQ93bNumSetupPduRx": svcAtmConfigQ93bNumSetupPduRx,
       "svcAtmConfigQ93bNumCallProcPduTx": svcAtmConfigQ93bNumCallProcPduTx,
       "svcAtmConfigQ93bNumCallProcPduRx": svcAtmConfigQ93bNumCallProcPduRx,
       "svcAtmConfigQ93bNumConnectPduTx": svcAtmConfigQ93bNumConnectPduTx,
       "svcAtmConfigQ93bNumConnectPduRx": svcAtmConfigQ93bNumConnectPduRx,
       "svcAtmConfigQ93bNumConnectAckPduTx": svcAtmConfigQ93bNumConnectAckPduTx,
       "svcAtmConfigQ93bNumConnectAckPduRx": svcAtmConfigQ93bNumConnectAckPduRx,
       "svcAtmConfigQ93bNumReleasePduTx": svcAtmConfigQ93bNumReleasePduTx,
       "svcAtmConfigQ93bNumReleasePduRx": svcAtmConfigQ93bNumReleasePduRx,
       "svcAtmConfigQ93bNumReleaseCmpltPduTx": svcAtmConfigQ93bNumReleaseCmpltPduTx,
       "svcAtmConfigQ93bNumReleaseCmpltPduRx": svcAtmConfigQ93bNumReleaseCmpltPduRx,
       "svcAtmConfigQ93bNumAddPtyPduTx": svcAtmConfigQ93bNumAddPtyPduTx,
       "svcAtmConfigQ93bNumAddPtyPduRx": svcAtmConfigQ93bNumAddPtyPduRx,
       "svcAtmConfigQ93bNumAddPtyAckPduTx": svcAtmConfigQ93bNumAddPtyAckPduTx,
       "svcAtmConfigQ93bNumAddPtyAckPduRx": svcAtmConfigQ93bNumAddPtyAckPduRx,
       "svcAtmConfigQ93bNumAddPtyRejPduTx": svcAtmConfigQ93bNumAddPtyRejPduTx,
       "svcAtmConfigQ93bNumAddPtyRejPduRx": svcAtmConfigQ93bNumAddPtyRejPduRx,
       "svcAtmConfigQ93bNumDropPtyPduTx": svcAtmConfigQ93bNumDropPtyPduTx,
       "svcAtmConfigQ93bNumDropPtyPduRx": svcAtmConfigQ93bNumDropPtyPduRx,
       "svcAtmConfigQ93bNumDropPtyAckPduTx": svcAtmConfigQ93bNumDropPtyAckPduTx,
       "svcAtmConfigQ93bNumDropPtyAckPduRx": svcAtmConfigQ93bNumDropPtyAckPduRx,
       "svcAtmConfigQ93bNumStatusEnqPduTx": svcAtmConfigQ93bNumStatusEnqPduTx,
       "svcAtmConfigQ93bNumStatusEnqPduRx": svcAtmConfigQ93bNumStatusEnqPduRx,
       "svcAtmConfigQ93bNumStatusPduTx": svcAtmConfigQ93bNumStatusPduTx,
       "svcAtmConfigQ93bNumStatusPduRx": svcAtmConfigQ93bNumStatusPduRx,
       "svcAtmConfigQ93bNumRestartPduTx": svcAtmConfigQ93bNumRestartPduTx,
       "svcAtmConfigQ93bNumRestartPduRx": svcAtmConfigQ93bNumRestartPduRx,
       "svcAtmConfigQ93bNumRestartAckPduTx": svcAtmConfigQ93bNumRestartAckPduTx,
       "svcAtmConfigQ93bNumRestartAckPduRx": svcAtmConfigQ93bNumRestartAckPduRx,
       "svcAtmConfigQSaalMaxCC": svcAtmConfigQSaalMaxCC,
       "svcAtmConfigQSaalMaxPD": svcAtmConfigQSaalMaxPD,
       "svcAtmConfigQSaalMaxStat": svcAtmConfigQSaalMaxStat,
       "svcAtmConfigQSaalTPoll": svcAtmConfigQSaalTPoll,
       "svcAtmConfigQSaalTKeepalive": svcAtmConfigQSaalTKeepalive,
       "svcAtmConfigQSaalTNoResponse": svcAtmConfigQSaalTNoResponse,
       "svcAtmConfigQSaalTCC": svcAtmConfigQSaalTCC,
       "svcAtmConfigQSaalTIdle": svcAtmConfigQSaalTIdle,
       "svcAtmConfigQSaalNumDiscardTx": svcAtmConfigQSaalNumDiscardTx,
       "svcAtmConfigQSaalNumDiscardRx": svcAtmConfigQSaalNumDiscardRx,
       "svcAtmConfigQSaalNumErrorTx": svcAtmConfigQSaalNumErrorTx,
       "svcAtmConfigQSaalNumErrorRx": svcAtmConfigQSaalNumErrorRx,
       "svcAtmConfigQSaalNumBgnPduTx": svcAtmConfigQSaalNumBgnPduTx,
       "svcAtmConfigQSaalNumBgnPduRx": svcAtmConfigQSaalNumBgnPduRx,
       "svcAtmConfigQSaalNumBgakPduTx": svcAtmConfigQSaalNumBgakPduTx,
       "svcAtmConfigQSaalNumBgakPduRx": svcAtmConfigQSaalNumBgakPduRx,
       "svcAtmConfigQSaalNumBgrejPduTx": svcAtmConfigQSaalNumBgrejPduTx,
       "svcAtmConfigQSaalNumBgrejPduRx": svcAtmConfigQSaalNumBgrejPduRx,
       "svcAtmConfigQSaalNumEndPduTx": svcAtmConfigQSaalNumEndPduTx,
       "svcAtmConfigQSaalNumEndPduRx": svcAtmConfigQSaalNumEndPduRx,
       "svcAtmConfigQSaalNumEndakPduTx": svcAtmConfigQSaalNumEndakPduTx,
       "svcAtmConfigQSaalNumEndakPduRx": svcAtmConfigQSaalNumEndakPduRx,
       "svcAtmConfigQSaalNumRsPduTx": svcAtmConfigQSaalNumRsPduTx,
       "svcAtmConfigQSaalNumRsPduRx": svcAtmConfigQSaalNumRsPduRx,
       "svcAtmConfigQSaalNumRsakPduTx": svcAtmConfigQSaalNumRsakPduTx,
       "svcAtmConfigQSaalNumRsakPduRx": svcAtmConfigQSaalNumRsakPduRx,
       "svcAtmConfigQSaalNumErPduTx": svcAtmConfigQSaalNumErPduTx,
       "svcAtmConfigQSaalNumErPduRx": svcAtmConfigQSaalNumErPduRx,
       "svcAtmConfigQSaalNumErakPduTx": svcAtmConfigQSaalNumErakPduTx,
       "svcAtmConfigQSaalNumErakPduRx": svcAtmConfigQSaalNumErakPduRx,
       "svcAtmConfigQSaalNumSdPduTx": svcAtmConfigQSaalNumSdPduTx,
       "svcAtmConfigQSaalNumSdPduRx": svcAtmConfigQSaalNumSdPduRx,
       "svcAtmConfigQSaalNumPollPduTx": svcAtmConfigQSaalNumPollPduTx,
       "svcAtmConfigQSaalNumPollPduRx": svcAtmConfigQSaalNumPollPduRx,
       "svcAtmConfigQSaalNumStatPduTx": svcAtmConfigQSaalNumStatPduTx,
       "svcAtmConfigQSaalNumStatPduRx": svcAtmConfigQSaalNumStatPduRx,
       "svcAtmConfigQSaalNumUstatPduTx": svcAtmConfigQSaalNumUstatPduTx,
       "svcAtmConfigQSaalNumUstatPduRx": svcAtmConfigQSaalNumUstatPduRx,
       "svcAtmConfigQSaalNumUdPduTx": svcAtmConfigQSaalNumUdPduTx,
       "svcAtmConfigQSaalNumUdPduRx": svcAtmConfigQSaalNumUdPduRx,
       "svcAtmConfigQSaalNumMdPduTx": svcAtmConfigQSaalNumMdPduTx,
       "svcAtmConfigQSaalNumMdPduRx": svcAtmConfigQSaalNumMdPduRx,
       "svcAtmFailedCallTable": svcAtmFailedCallTable,
       "svcAtmFailedCallEntry": svcAtmFailedCallEntry,
       "svcAtmFailedCallIfIndex": svcAtmFailedCallIfIndex,
       "svcAtmFailedCallIndex": svcAtmFailedCallIndex,
       "svcAtmFailedCallDirection": svcAtmFailedCallDirection,
       "svcAtmFailedCallPduType": svcAtmFailedCallPduType,
       "svcAtmFailedCallPduDirection": svcAtmFailedCallPduDirection,
       "svcAtmFailedCallCause": svcAtmFailedCallCause,
       "svcAtmFailedCallLocation": svcAtmFailedCallLocation,
       "svcAtmFailedCallDiagnostic": svcAtmFailedCallDiagnostic,
       "svcAtmFailedCallCreationTime": svcAtmFailedCallCreationTime,
       "svcAtmFailedCallTerminationTime": svcAtmFailedCallTerminationTime,
       "svcAtmFailedCallFailureNodeId": svcAtmFailedCallFailureNodeId,
       "svcAtmFailedCallFailureIfIndex": svcAtmFailedCallFailureIfIndex,
       "svcAtmFailedCallCallingParty": svcAtmFailedCallCallingParty,
       "svcAtmFailedCallCalledParty": svcAtmFailedCallCalledParty,
       "svcAtmFailedCallAtmTfdType": svcAtmFailedCallAtmTfdType,
       "svcAtmFailedCallAtmTfdParam1": svcAtmFailedCallAtmTfdParam1,
       "svcAtmFailedCallAtmTfdParam2": svcAtmFailedCallAtmTfdParam2,
       "svcAtmFailedCallAtmTfdParam3": svcAtmFailedCallAtmTfdParam3,
       "svcAtmFailedCallAtmQosClass": svcAtmFailedCallAtmQosClass,
       "svcAtmFailedCallAtmRTfdType": svcAtmFailedCallAtmRTfdType,
       "svcAtmFailedCallAtmRTfdParam1": svcAtmFailedCallAtmRTfdParam1,
       "svcAtmFailedCallAtmRTfdParam2": svcAtmFailedCallAtmRTfdParam2,
       "svcAtmFailedCallAtmRTfdParam3": svcAtmFailedCallAtmRTfdParam3,
       "svcAtmFailedCallAtmRQoSClass": svcAtmFailedCallAtmRQoSClass,
       "svcAtmFailedCallBBearerClass": svcAtmFailedCallBBearerClass,
       "svcAtmFailedCallBBearerTfcType": svcAtmFailedCallBBearerTfcType,
       "svcAtmFailedCallBBearerTmgRqmt": svcAtmFailedCallBBearerTmgRqmt,
       "svcAtmFailedCallBBearerUplaneCfg": svcAtmFailedCallBBearerUplaneCfg,
       "svcAtmFailedCallBBearerClippingSusc": svcAtmFailedCallBBearerClippingSusc,
       "svcAtmFailedCallAdminStatus": svcAtmFailedCallAdminStatus,
       "software": software,
       "swTable": swTable,
       "swEntry": swEntry,
       "swLogicalSlotId": swLogicalSlotId,
       "swRedundState": swRedundState,
       "swRevision": swRevision,
       "swBuildID": swBuildID,
       "swBuildDate": swBuildDate,
       "swBuildDescription": swBuildDescription,
       "swCopyrightNotice": swCopyrightNotice,
       "swCapabilityMask": swCapabilityMask,
       "swFeatureMask": swFeatureMask,
       "swPatchMask": swPatchMask,
       "swBuildUserId": swBuildUserId,
       "swBuildView": swBuildView,
       "swBuildConfigSpec": swBuildConfigSpec,
       "provserver": provserver}
)
