# SNMP MIB module (HUAWEI-VPLS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VPLS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:18 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(VrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId")


# MODULE-IDENTITY

hwL2VpnVplsExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWL2VpnVcEncapsType(Integer32, TextualConvention):
    status = "current"
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
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5PduVccTransport", 14),
          ("atmAal5SduVccTransport", 2),
          ("atmN2OneVccCellTransport", 9),
          ("atmN2OneVpcCellTransport", 10),
          ("atmOne2OneVccCellMode", 12),
          ("atmOne2OneVpcCellMode", 13),
          ("atmTransparentCellTransport", 3),
          ("cESoPsnBasicMode", 21),
          ("cem", 8),
          ("cep", 16),
          ("ethernet", 5),
          ("frameRelayDlci", 25),
          ("frameRelayDlciMartini", 1),
          ("frameRelayPortMode", 15),
          ("hdlc", 6),
          ("ipInterworking", 64),
          ("ipLayer2Transport", 11),
          ("l2VpnCESoPSNTDMwithCAS", 23),
          ("l2VpnTDMoIPTDMwithCAS", 24),
          ("ppp", 7),
          ("saE1oP", 17),
          ("saE3oP", 19),
          ("saT1oP", 18),
          ("saT3oP", 20),
          ("tDMoIPbasicMode", 22),
          ("unknown", 255),
          ("vlan", 4))
    )



class HWEnableValue(Integer32, TextualConvention):
    status = "current"
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



class HWL2VpnStateChangeReason(Integer32, TextualConvention):
    status = "current"
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
              61,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("acOamFaultDetectDisable", 34),
          ("bfdForPwDisable", 46),
          ("bfdForPwStateChangeToAdminDown", 45),
          ("bfdForPwStateChangeToDown", 43),
          ("bfdForPwStateChangeToUp", 44),
          ("delayTimeOut", 49),
          ("deletedRlb", 26),
          ("downloadAgain", 22),
          ("downloadFtnAndIlmForEthTrunk", 33),
          ("interfaceDown", 19),
          ("interfaceEncapChanged", 20),
          ("interfaceUp", 18),
          ("invalidReason", 1),
          ("ldpGrEndProcessing", 16),
          ("ldpNotifiForward", 30),
          ("ldpNotifiNotForward", 31),
          ("ldpSessionDown", 4),
          ("ldpSessionUp", 5),
          ("localAcFault", 37),
          ("localAcFaultResume", 38),
          ("localPsnFault", 41),
          ("localPsnFaultResume", 42),
          ("lspPingTimeOut", 57),
          ("manualSetDisable", 48),
          ("manualSetEnable", 47),
          ("mtuMatched", 59),
          ("mtuUnmatched", 60),
          ("outInterInInvalidState", 28),
          ("outInterInValidNow", 29),
          ("pwRestart", 32),
          ("receivedDifLabelOrMtu", 6),
          ("receivedIntfParaMatching", 7),
          ("receivedIntfParaUnMatched", 8),
          ("receivedLdpRelease", 14),
          ("receivedLdpRequest", 15),
          ("receivedNewMapping", 11),
          ("receivedNewMappingButRemoteVcDown", 12),
          ("receivedNewRlb", 25),
          ("receivedRsvpMessage", 17),
          ("receivedUnPassCbitCheck", 9),
          ("receivedUnPassPwLoopCheck", 10),
          ("receivedWithdrawn", 13),
          ("refresh", 21),
          ("remoteAcFault", 35),
          ("remoteAcFaultResume", 36),
          ("remotePsnFault", 39),
          ("remotePsnFaultResume", 40),
          ("resumeTimeOut", 50),
          ("setAdminVSI", 63),
          ("tunnelDown", 24),
          ("tunnelUp", 23),
          ("undoVrrpTrack", 56),
          ("undosetAdminVSI", 64),
          ("vcCreated", 2),
          ("vcCreatedOrTurnedToAnother", 27),
          ("vcDeleted", 3),
          ("vcDownWhenReceivedNewRLB", 58),
          ("vrrpBackup", 52),
          ("vrrpDelete", 54),
          ("vrrpInit", 53),
          ("vrrpMaster", 51),
          ("vrrpTrack", 55),
          ("vsiResume", 62),
          ("vsiShut", 61))
    )



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwVplsMIBObjects_ObjectIdentity = ObjectIdentity
hwVplsMIBObjects = _HwVplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1)
)
_HwVplsTable_Object = MibTable
hwVplsTable = _HwVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsTable.setStatus("current")
_HwVplsEntry_Object = MibTableRow
hwVplsEntry = _HwVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1)
)
hwVplsEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
)
if mibBuilder.loadTexts:
    hwVplsEntry.setStatus("current")


class _HwVplsVsiName_Type(DisplayString):
    """Custom type hwVplsVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVplsVsiName_Type.__name__ = "DisplayString"
_HwVplsVsiName_Object = MibTableColumn
hwVplsVsiName = _HwVplsVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 1),
    _HwVplsVsiName_Type()
)
hwVplsVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsVsiName.setStatus("current")


class _HwVplsSignal_Type(Integer32):
    """Custom type hwVplsSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("ldp", 1),
          ("unknown", 255))
    )


_HwVplsSignal_Type.__name__ = "Integer32"
_HwVplsSignal_Object = MibTableColumn
hwVplsSignal = _HwVplsSignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 2),
    _HwVplsSignal_Type()
)
hwVplsSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsSignal.setStatus("current")


class _HwVplsRD_Type(DisplayString):
    """Custom type hwVplsRD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 21),
    )


_HwVplsRD_Type.__name__ = "DisplayString"
_HwVplsRD_Object = MibTableColumn
hwVplsRD = _HwVplsRD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 3),
    _HwVplsRD_Type()
)
hwVplsRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsRD.setStatus("current")
_HwVplsVsiID_Type = Unsigned32
_HwVplsVsiID_Object = MibTableColumn
hwVplsVsiID = _HwVplsVsiID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 4),
    _HwVplsVsiID_Type()
)
hwVplsVsiID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVsiID.setStatus("current")
_HwVplsVcType_Type = HWL2VpnVcEncapsType
_HwVplsVcType_Object = MibTableColumn
hwVplsVcType = _HwVplsVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 5),
    _HwVplsVcType_Type()
)
hwVplsVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVcType.setStatus("current")


class _HwVplsStatus_Type(Integer32):
    """Custom type hwVplsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 3),
          ("down", 2),
          ("up", 1))
    )


_HwVplsStatus_Type.__name__ = "Integer32"
_HwVplsStatus_Object = MibTableColumn
hwVplsStatus = _HwVplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 6),
    _HwVplsStatus_Type()
)
hwVplsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatus.setStatus("current")


class _HwVplsMtu_Type(Unsigned32):
    """Custom type hwVplsMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(328, 65535),
    )


_HwVplsMtu_Type.__name__ = "Unsigned32"
_HwVplsMtu_Object = MibTableColumn
hwVplsMtu = _HwVplsMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 7),
    _HwVplsMtu_Type()
)
hwVplsMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsMtu.setStatus("current")


class _HwVplsTunnelPolicy_Type(DisplayString):
    """Custom type hwVplsTunnelPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwVplsTunnelPolicy_Type.__name__ = "DisplayString"
_HwVplsTunnelPolicy_Object = MibTableColumn
hwVplsTunnelPolicy = _HwVplsTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 8),
    _HwVplsTunnelPolicy_Type()
)
hwVplsTunnelPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsTunnelPolicy.setStatus("current")


class _HwVplsDescription_Type(DisplayString):
    """Custom type hwVplsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwVplsDescription_Type.__name__ = "DisplayString"
_HwVplsDescription_Object = MibTableColumn
hwVplsDescription = _HwVplsDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 9),
    _HwVplsDescription_Type()
)
hwVplsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDescription.setStatus("current")


class _HwVplsLearnStyle_Type(Integer32):
    """Custom type hwVplsLearnStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qualify", 1),
          ("unqualify", 2))
    )


_HwVplsLearnStyle_Type.__name__ = "Integer32"
_HwVplsLearnStyle_Object = MibTableColumn
hwVplsLearnStyle = _HwVplsLearnStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 10),
    _HwVplsLearnStyle_Type()
)
hwVplsLearnStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLearnStyle.setStatus("current")
_HwVplsMacLearnEnable_Type = HWEnableValue
_HwVplsMacLearnEnable_Object = MibTableColumn
hwVplsMacLearnEnable = _HwVplsMacLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 11),
    _HwVplsMacLearnEnable_Type()
)
hwVplsMacLearnEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsMacLearnEnable.setStatus("current")
_HwVplsMacLimitEnable_Type = HWEnableValue
_HwVplsMacLimitEnable_Object = MibTableColumn
hwVplsMacLimitEnable = _HwVplsMacLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 12),
    _HwVplsMacLimitEnable_Type()
)
hwVplsMacLimitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsMacLimitEnable.setStatus("current")
_HwVplsStatisticsEnable_Type = HWEnableValue
_HwVplsStatisticsEnable_Object = MibTableColumn
hwVplsStatisticsEnable = _HwVplsStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 13),
    _HwVplsStatisticsEnable_Type()
)
hwVplsStatisticsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsStatisticsEnable.setStatus("current")


class _HwVplsUnknowMulticast_Type(Integer32):
    """Custom type hwVplsUnknowMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("drop", 2),
          ("localHandle", 3))
    )


_HwVplsUnknowMulticast_Type.__name__ = "Integer32"
_HwVplsUnknowMulticast_Object = MibTableColumn
hwVplsUnknowMulticast = _HwVplsUnknowMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 14),
    _HwVplsUnknowMulticast_Type()
)
hwVplsUnknowMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsUnknowMulticast.setStatus("current")


class _HwVplsUnknowUnicast_Type(Integer32):
    """Custom type hwVplsUnknowUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("drop", 2),
          ("localHandle", 3))
    )


_HwVplsUnknowUnicast_Type.__name__ = "Integer32"
_HwVplsUnknowUnicast_Object = MibTableColumn
hwVplsUnknowUnicast = _HwVplsUnknowUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 15),
    _HwVplsUnknowUnicast_Type()
)
hwVplsUnknowUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsUnknowUnicast.setStatus("current")


class _HwVplsPreference_Type(Unsigned32):
    """Custom type hwVplsPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwVplsPreference_Type.__name__ = "Unsigned32"
_HwVplsPreference_Object = MibTableColumn
hwVplsPreference = _HwVplsPreference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 16),
    _HwVplsPreference_Type()
)
hwVplsPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPreference.setStatus("current")


class _HwVplsVsiType_Type(Integer32):
    """Custom type hwVplsVsiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminVsi", 2),
          ("operationVsi", 1))
    )


_HwVplsVsiType_Type.__name__ = "Integer32"
_HwVplsVsiType_Object = MibTableColumn
hwVplsVsiType = _HwVplsVsiType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 17),
    _HwVplsVsiType_Type()
)
hwVplsVsiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVsiType.setStatus("current")
_HwVplsAdminVsiName_Type = DisplayString
_HwVplsAdminVsiName_Object = MibTableColumn
hwVplsAdminVsiName = _HwVplsAdminVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 18),
    _HwVplsAdminVsiName_Type()
)
hwVplsAdminVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsAdminVsiName.setStatus("current")
_HwVplsAcIsolateFlag_Type = HWEnableValue
_HwVplsAcIsolateFlag_Object = MibTableColumn
hwVplsAcIsolateFlag = _HwVplsAcIsolateFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 19),
    _HwVplsAcIsolateFlag_Type()
)
hwVplsAcIsolateFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsAcIsolateFlag.setStatus("current")


class _HwVplsDiffServMode_Type(Integer32):
    """Custom type hwVplsDiffServMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("shortpipe", 2),
          ("uniform", 3))
    )


_HwVplsDiffServMode_Type.__name__ = "Integer32"
_HwVplsDiffServMode_Object = MibTableColumn
hwVplsDiffServMode = _HwVplsDiffServMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 20),
    _HwVplsDiffServMode_Type()
)
hwVplsDiffServMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDiffServMode.setStatus("current")


class _HwVplsDiffServServiceClass_Type(Integer32):
    """Custom type hwVplsDiffServServiceClass based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("invalidClass", 255))
    )


_HwVplsDiffServServiceClass_Type.__name__ = "Integer32"
_HwVplsDiffServServiceClass_Object = MibTableColumn
hwVplsDiffServServiceClass = _HwVplsDiffServServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 21),
    _HwVplsDiffServServiceClass_Type()
)
hwVplsDiffServServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDiffServServiceClass.setStatus("current")


class _HwVplsDiffServColor_Type(Integer32):
    """Custom type hwVplsDiffServColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("invalidColor", 255),
          ("red", 3),
          ("yellow", 2))
    )


_HwVplsDiffServColor_Type.__name__ = "Integer32"
_HwVplsDiffServColor_Object = MibTableColumn
hwVplsDiffServColor = _HwVplsDiffServColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 22),
    _HwVplsDiffServColor_Type()
)
hwVplsDiffServColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDiffServColor.setStatus("current")


class _HwVplsDiffServDSName_Type(OctetString):
    """Custom type hwVplsDiffServDSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwVplsDiffServDSName_Type.__name__ = "OctetString"
_HwVplsDiffServDSName_Object = MibTableColumn
hwVplsDiffServDSName = _HwVplsDiffServDSName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 23),
    _HwVplsDiffServDSName_Type()
)
hwVplsDiffServDSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDiffServDSName.setStatus("current")
_HwVplsInterfaceWithdraw_Type = HWEnableValue
_HwVplsInterfaceWithdraw_Object = MibTableColumn
hwVplsInterfaceWithdraw = _HwVplsInterfaceWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 24),
    _HwVplsInterfaceWithdraw_Type()
)
hwVplsInterfaceWithdraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsInterfaceWithdraw.setStatus("current")
_HwVplsUpe2NpeWithdraw_Type = HWEnableValue
_HwVplsUpe2NpeWithdraw_Object = MibTableColumn
hwVplsUpe2NpeWithdraw = _HwVplsUpe2NpeWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 25),
    _HwVplsUpe2NpeWithdraw_Type()
)
hwVplsUpe2NpeWithdraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsUpe2NpeWithdraw.setStatus("current")
_HwVplsUpe2UpeWithdraw_Type = HWEnableValue
_HwVplsUpe2UpeWithdraw_Object = MibTableColumn
hwVplsUpe2UpeWithdraw = _HwVplsUpe2UpeWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 26),
    _HwVplsUpe2UpeWithdraw_Type()
)
hwVplsUpe2UpeWithdraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsUpe2UpeWithdraw.setStatus("current")
_HwVplsNpe2UpeWithdraw_Type = HWEnableValue
_HwVplsNpe2UpeWithdraw_Object = MibTableColumn
hwVplsNpe2UpeWithdraw = _HwVplsNpe2UpeWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 27),
    _HwVplsNpe2UpeWithdraw_Type()
)
hwVplsNpe2UpeWithdraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsNpe2UpeWithdraw.setStatus("current")


class _HwVplsDiscovery_Type(Integer32):
    """Custom type hwVplsDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("static", 1))
    )


_HwVplsDiscovery_Type.__name__ = "Integer32"
_HwVplsDiscovery_Object = MibTableColumn
hwVplsDiscovery = _HwVplsDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 28),
    _HwVplsDiscovery_Type()
)
hwVplsDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsDiscovery.setStatus("current")
_HwVplsMacWithdrawEnable_Type = EnabledStatus
_HwVplsMacWithdrawEnable_Object = MibTableColumn
hwVplsMacWithdrawEnable = _HwVplsMacWithdrawEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 29),
    _HwVplsMacWithdrawEnable_Type()
)
hwVplsMacWithdrawEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsMacWithdrawEnable.setStatus("current")
_HwVplsVsiCir_Type = Unsigned32
_HwVplsVsiCir_Object = MibTableColumn
hwVplsVsiCir = _HwVplsVsiCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 30),
    _HwVplsVsiCir_Type()
)
hwVplsVsiCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVsiCir.setStatus("current")
_HwVplsVsiPir_Type = Unsigned32
_HwVplsVsiPir_Object = MibTableColumn
hwVplsVsiPir = _HwVplsVsiPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 31),
    _HwVplsVsiPir_Type()
)
hwVplsVsiPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVsiPir.setStatus("current")


class _HwVplsVsiQosProfileName_Type(DisplayString):
    """Custom type hwVplsVsiQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVplsVsiQosProfileName_Type.__name__ = "DisplayString"
_HwVplsVsiQosProfileName_Object = MibTableColumn
hwVplsVsiQosProfileName = _HwVplsVsiQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 32),
    _HwVplsVsiQosProfileName_Type()
)
hwVplsVsiQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsVsiQosProfileName.setStatus("current")


class _HwVplsAdminStatus_Type(Integer32):
    """Custom type hwVplsAdminStatus based on Integer32"""
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


_HwVplsAdminStatus_Type.__name__ = "Integer32"
_HwVplsAdminStatus_Object = MibTableColumn
hwVplsAdminStatus = _HwVplsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 33),
    _HwVplsAdminStatus_Type()
)
hwVplsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsAdminStatus.setStatus("current")
_HwVplsIgnoreAcState_Type = EnabledStatus
_HwVplsIgnoreAcState_Object = MibTableColumn
hwVplsIgnoreAcState = _HwVplsIgnoreAcState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 34),
    _HwVplsIgnoreAcState_Type()
)
hwVplsIgnoreAcState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsIgnoreAcState.setStatus("current")
_HwVplsEnableStatistic_Type = EnabledStatus
_HwVplsEnableStatistic_Object = MibTableColumn
hwVplsEnableStatistic = _HwVplsEnableStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 35),
    _HwVplsEnableStatistic_Type()
)
hwVplsEnableStatistic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsEnableStatistic.setStatus("current")


class _HwVplsResetStatistic_Type(Integer32):
    """Custom type hwVplsResetStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetStatistic", 1),
          ("unknownStatus", 2))
    )


_HwVplsResetStatistic_Type.__name__ = "Integer32"
_HwVplsResetStatistic_Object = MibTableColumn
hwVplsResetStatistic = _HwVplsResetStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 36),
    _HwVplsResetStatistic_Type()
)
hwVplsResetStatistic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsResetStatistic.setStatus("current")
_HwVplsResetStatisticTime_Type = DateAndTime
_HwVplsResetStatisticTime_Object = MibTableColumn
hwVplsResetStatisticTime = _HwVplsResetStatisticTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 37),
    _HwVplsResetStatisticTime_Type()
)
hwVplsResetStatisticTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsResetStatisticTime.setStatus("current")


class _HwVplsAgingTime_Type(Unsigned32):
    """Custom type hwVplsAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwVplsAgingTime_Type.__name__ = "Unsigned32"
_HwVplsAgingTime_Object = MibTableColumn
hwVplsAgingTime = _HwVplsAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 38),
    _HwVplsAgingTime_Type()
)
hwVplsAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsAgingTime.setStatus("current")
_HwVplsUnknowUnicastMacLearning_Type = EnabledStatus
_HwVplsUnknowUnicastMacLearning_Object = MibTableColumn
hwVplsUnknowUnicastMacLearning = _HwVplsUnknowUnicastMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 39),
    _HwVplsUnknowUnicastMacLearning_Type()
)
hwVplsUnknowUnicastMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsUnknowUnicastMacLearning.setStatus("current")
_HwVplsFlowLabel_Type = EnabledStatus
_HwVplsFlowLabel_Object = MibTableColumn
hwVplsFlowLabel = _HwVplsFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 40),
    _HwVplsFlowLabel_Type()
)
hwVplsFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsFlowLabel.setStatus("current")


class _HwVplsServiceName_Type(OctetString):
    """Custom type hwVplsServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HwVplsServiceName_Type.__name__ = "OctetString"
_HwVplsServiceName_Object = MibTableColumn
hwVplsServiceName = _HwVplsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 41),
    _HwVplsServiceName_Type()
)
hwVplsServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsServiceName.setStatus("current")
_HwVplsRowStatus_Type = RowStatus
_HwVplsRowStatus_Object = MibTableColumn
hwVplsRowStatus = _HwVplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 1, 1, 51),
    _HwVplsRowStatus_Type()
)
hwVplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsRowStatus.setStatus("current")
_HwVplsRtTable_Object = MibTable
hwVplsRtTable = _HwVplsRtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwVplsRtTable.setStatus("current")
_HwVplsRtEntry_Object = MibTableRow
hwVplsRtEntry = _HwVplsRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 2, 1)
)
hwVplsRtEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsRtType"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsRtName"),
)
if mibBuilder.loadTexts:
    hwVplsRtEntry.setStatus("current")


class _HwVplsRtType_Type(Integer32):
    """Custom type hwVplsRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_HwVplsRtType_Type.__name__ = "Integer32"
_HwVplsRtType_Object = MibTableColumn
hwVplsRtType = _HwVplsRtType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 2, 1, 1),
    _HwVplsRtType_Type()
)
hwVplsRtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsRtType.setStatus("current")


class _HwVplsRtName_Type(DisplayString):
    """Custom type hwVplsRtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_HwVplsRtName_Type.__name__ = "DisplayString"
_HwVplsRtName_Object = MibTableColumn
hwVplsRtName = _HwVplsRtName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 2, 1, 2),
    _HwVplsRtName_Type()
)
hwVplsRtName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsRtName.setStatus("current")
_HwVplsRtRowStatus_Type = RowStatus
_HwVplsRtRowStatus_Object = MibTableColumn
hwVplsRtRowStatus = _HwVplsRtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 2, 1, 51),
    _HwVplsRtRowStatus_Type()
)
hwVplsRtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsRtRowStatus.setStatus("current")
_HwVplsAcTable_Object = MibTable
hwVplsAcTable = _HwVplsAcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwVplsAcTable.setStatus("current")
_HwVplsAcEntry_Object = MibTableRow
hwVplsAcEntry = _HwVplsAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1)
)
hwVplsAcEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsAcIfIndex"),
)
if mibBuilder.loadTexts:
    hwVplsAcEntry.setStatus("current")
_HwVplsAcIfIndex_Type = InterfaceIndex
_HwVplsAcIfIndex_Object = MibTableColumn
hwVplsAcIfIndex = _HwVplsAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1, 1),
    _HwVplsAcIfIndex_Type()
)
hwVplsAcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsAcIfIndex.setStatus("current")


class _HwVplsAcStatus_Type(Integer32):
    """Custom type hwVplsAcStatus based on Integer32"""
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


_HwVplsAcStatus_Type.__name__ = "Integer32"
_HwVplsAcStatus_Object = MibTableColumn
hwVplsAcStatus = _HwVplsAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1, 2),
    _HwVplsAcStatus_Type()
)
hwVplsAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsAcStatus.setStatus("current")


class _HwVplsAcUpStartTime_Type(DisplayString):
    """Custom type hwVplsAcUpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwVplsAcUpStartTime_Type.__name__ = "DisplayString"
_HwVplsAcUpStartTime_Object = MibTableColumn
hwVplsAcUpStartTime = _HwVplsAcUpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1, 3),
    _HwVplsAcUpStartTime_Type()
)
hwVplsAcUpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsAcUpStartTime.setStatus("current")
_HwVplsAcUpSumTime_Type = Unsigned32
_HwVplsAcUpSumTime_Object = MibTableColumn
hwVplsAcUpSumTime = _HwVplsAcUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1, 4),
    _HwVplsAcUpSumTime_Type()
)
hwVplsAcUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsAcUpSumTime.setStatus("current")
_HwVplsAcRowStatus_Type = RowStatus
_HwVplsAcRowStatus_Object = MibTableColumn
hwVplsAcRowStatus = _HwVplsAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 3, 1, 51),
    _HwVplsAcRowStatus_Type()
)
hwVplsAcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsAcRowStatus.setStatus("current")
_HwVplsBgpInfoTable_Object = MibTable
hwVplsBgpInfoTable = _HwVplsBgpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwVplsBgpInfoTable.setStatus("current")
_HwVplsBgpInfoEntry_Object = MibTableRow
hwVplsBgpInfoEntry = _HwVplsBgpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4, 1)
)
hwVplsBgpInfoEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsBgpInfoSiteID"),
)
if mibBuilder.loadTexts:
    hwVplsBgpInfoEntry.setStatus("current")


class _HwVplsBgpInfoSiteID_Type(Unsigned32):
    """Custom type hwVplsBgpInfoSiteID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwVplsBgpInfoSiteID_Type.__name__ = "Unsigned32"
_HwVplsBgpInfoSiteID_Object = MibTableColumn
hwVplsBgpInfoSiteID = _HwVplsBgpInfoSiteID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4, 1, 1),
    _HwVplsBgpInfoSiteID_Type()
)
hwVplsBgpInfoSiteID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsBgpInfoSiteID.setStatus("current")


class _HwVplsBgpInfoRange_Type(Unsigned32):
    """Custom type hwVplsBgpInfoRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HwVplsBgpInfoRange_Type.__name__ = "Unsigned32"
_HwVplsBgpInfoRange_Object = MibTableColumn
hwVplsBgpInfoRange = _HwVplsBgpInfoRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4, 1, 2),
    _HwVplsBgpInfoRange_Type()
)
hwVplsBgpInfoRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsBgpInfoRange.setStatus("current")


class _HwVplsBgpInfoOffset_Type(Unsigned32):
    """Custom type hwVplsBgpInfoOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwVplsBgpInfoOffset_Type.__name__ = "Unsigned32"
_HwVplsBgpInfoOffset_Object = MibTableColumn
hwVplsBgpInfoOffset = _HwVplsBgpInfoOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4, 1, 3),
    _HwVplsBgpInfoOffset_Type()
)
hwVplsBgpInfoOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsBgpInfoOffset.setStatus("current")
_HwVplsBgpInfoRowStatus_Type = RowStatus
_HwVplsBgpInfoRowStatus_Object = MibTableColumn
hwVplsBgpInfoRowStatus = _HwVplsBgpInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 4, 1, 51),
    _HwVplsBgpInfoRowStatus_Type()
)
hwVplsBgpInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsBgpInfoRowStatus.setStatus("current")
_HwVplsPwTable_Object = MibTable
hwVplsPwTable = _HwVplsPwTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwVplsPwTable.setStatus("current")
_HwVplsPwEntry_Object = MibTableRow
hwVplsPwEntry = _HwVplsPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1)
)
hwVplsPwEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsPwID"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsPwRemoteIp"),
)
if mibBuilder.loadTexts:
    hwVplsPwEntry.setStatus("current")
_HwVplsPwID_Type = Unsigned32
_HwVplsPwID_Object = MibTableColumn
hwVplsPwID = _HwVplsPwID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 1),
    _HwVplsPwID_Type()
)
hwVplsPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsPwID.setStatus("current")
_HwVplsPwRemoteIp_Type = IpAddress
_HwVplsPwRemoteIp_Object = MibTableColumn
hwVplsPwRemoteIp = _HwVplsPwRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 2),
    _HwVplsPwRemoteIp_Type()
)
hwVplsPwRemoteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsPwRemoteIp.setStatus("current")


class _HwVplsPwTnlPolicy_Type(DisplayString):
    """Custom type hwVplsPwTnlPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwVplsPwTnlPolicy_Type.__name__ = "DisplayString"
_HwVplsPwTnlPolicy_Object = MibTableColumn
hwVplsPwTnlPolicy = _HwVplsPwTnlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 3),
    _HwVplsPwTnlPolicy_Type()
)
hwVplsPwTnlPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwTnlPolicy.setStatus("current")


class _HwVplsPwType_Type(Integer32):
    """Custom type hwVplsPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("other", 2))
    )


_HwVplsPwType_Type.__name__ = "Integer32"
_HwVplsPwType_Object = MibTableColumn
hwVplsPwType = _HwVplsPwType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 4),
    _HwVplsPwType_Type()
)
hwVplsPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwType.setStatus("current")
_HwVplsPwIsUpe_Type = TruthValue
_HwVplsPwIsUpe_Object = MibTableColumn
hwVplsPwIsUpe = _HwVplsPwIsUpe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 5),
    _HwVplsPwIsUpe_Type()
)
hwVplsPwIsUpe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwIsUpe.setStatus("current")
_HwVplsPwInboundLabel_Type = Unsigned32
_HwVplsPwInboundLabel_Object = MibTableColumn
hwVplsPwInboundLabel = _HwVplsPwInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 6),
    _HwVplsPwInboundLabel_Type()
)
hwVplsPwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwInboundLabel.setStatus("current")
_HwVplsPwOutboundLabel_Type = Unsigned32
_HwVplsPwOutboundLabel_Object = MibTableColumn
hwVplsPwOutboundLabel = _HwVplsPwOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 7),
    _HwVplsPwOutboundLabel_Type()
)
hwVplsPwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwOutboundLabel.setStatus("current")


class _HwVplsPwStatus_Type(Integer32):
    """Custom type hwVplsPwStatus based on Integer32"""
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
        *(("backup", 4),
          ("down", 1),
          ("plugout", 3),
          ("up", 2))
    )


_HwVplsPwStatus_Type.__name__ = "Integer32"
_HwVplsPwStatus_Object = MibTableColumn
hwVplsPwStatus = _HwVplsPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 8),
    _HwVplsPwStatus_Type()
)
hwVplsPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPwStatus.setStatus("current")
_HwVplsPwVrIfIndex_Type = InterfaceIndexOrZero
_HwVplsPwVrIfIndex_Object = MibTableColumn
hwVplsPwVrIfIndex = _HwVplsPwVrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 9),
    _HwVplsPwVrIfIndex_Type()
)
hwVplsPwVrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPwVrIfIndex.setStatus("current")


class _HwVplsPwVrID_Type(Unsigned32):
    """Custom type hwVplsPwVrID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVplsPwVrID_Type.__name__ = "Unsigned32"
_HwVplsPwVrID_Object = MibTableColumn
hwVplsPwVrID = _HwVplsPwVrID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 10),
    _HwVplsPwVrID_Type()
)
hwVplsPwVrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPwVrID.setStatus("current")


class _HwVplsPwUpStartTime_Type(DisplayString):
    """Custom type hwVplsPwUpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwVplsPwUpStartTime_Type.__name__ = "DisplayString"
_HwVplsPwUpStartTime_Object = MibTableColumn
hwVplsPwUpStartTime = _HwVplsPwUpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 11),
    _HwVplsPwUpStartTime_Type()
)
hwVplsPwUpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPwUpStartTime.setStatus("current")
_HwVplsPwUpSumTime_Type = Unsigned32
_HwVplsPwUpSumTime_Object = MibTableColumn
hwVplsPwUpSumTime = _HwVplsPwUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 12),
    _HwVplsPwUpSumTime_Type()
)
hwVplsPwUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPwUpSumTime.setStatus("current")
_HwVplsPwRowStatus_Type = RowStatus
_HwVplsPwRowStatus_Object = MibTableColumn
hwVplsPwRowStatus = _HwVplsPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 5, 1, 51),
    _HwVplsPwRowStatus_Type()
)
hwVplsPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsPwRowStatus.setStatus("current")
_HwVplsStatisticsTable_Object = MibTable
hwVplsStatisticsTable = _HwVplsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwVplsStatisticsTable.setStatus("current")
_HwVplsStatisticsEntry_Object = MibTableRow
hwVplsStatisticsEntry = _HwVplsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1)
)
hwVplsStatisticsEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
)
if mibBuilder.loadTexts:
    hwVplsStatisticsEntry.setStatus("current")
_HwVplsOutFrames_Type = Counter64
_HwVplsOutFrames_Object = MibTableColumn
hwVplsOutFrames = _HwVplsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1, 1),
    _HwVplsOutFrames_Type()
)
hwVplsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsOutFrames.setStatus("current")
_HwVplsInFrames_Type = Counter64
_HwVplsInFrames_Object = MibTableColumn
hwVplsInFrames = _HwVplsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1, 2),
    _HwVplsInFrames_Type()
)
hwVplsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsInFrames.setStatus("current")
_HwVplsOutBytes_Type = Counter64
_HwVplsOutBytes_Object = MibTableColumn
hwVplsOutBytes = _HwVplsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1, 3),
    _HwVplsOutBytes_Type()
)
hwVplsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsOutBytes.setStatus("current")
_HwVplsInBytes_Type = Counter64
_HwVplsInBytes_Object = MibTableColumn
hwVplsInBytes = _HwVplsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1, 4),
    _HwVplsInBytes_Type()
)
hwVplsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsInBytes.setStatus("current")
_HwVplsInDiscardFrames_Type = Counter64
_HwVplsInDiscardFrames_Object = MibTableColumn
hwVplsInDiscardFrames = _HwVplsInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 6, 1, 5),
    _HwVplsInDiscardFrames_Type()
)
hwVplsInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsInDiscardFrames.setStatus("current")
_HwVplsUpDownNotifEnable_Type = HWEnableValue
_HwVplsUpDownNotifEnable_Object = MibScalar
hwVplsUpDownNotifEnable = _HwVplsUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 7),
    _HwVplsUpDownNotifEnable_Type()
)
hwVplsUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsUpDownNotifEnable.setStatus("obsolete")
_HwVplsStateChangeReason_Type = HWL2VpnStateChangeReason
_HwVplsStateChangeReason_Object = MibScalar
hwVplsStateChangeReason = _HwVplsStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 8),
    _HwVplsStateChangeReason_Type()
)
hwVplsStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVplsStateChangeReason.setStatus("current")
_HwVplsLdpStatisticsTable_Object = MibTable
hwVplsLdpStatisticsTable = _HwVplsLdpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwVplsLdpStatisticsTable.setStatus("current")
_HwVplsLdpStatisticsEntry_Object = MibTableRow
hwVplsLdpStatisticsEntry = _HwVplsLdpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1)
)
hwVplsLdpStatisticsEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatPwID"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    hwVplsLdpStatisticsEntry.setStatus("current")
_HwVplsLdpStatPwID_Type = Unsigned32
_HwVplsLdpStatPwID_Object = MibTableColumn
hwVplsLdpStatPwID = _HwVplsLdpStatPwID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 1),
    _HwVplsLdpStatPwID_Type()
)
hwVplsLdpStatPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpStatPwID.setStatus("current")
_HwVplsLdpStatRemoteIpAddr_Type = IpAddress
_HwVplsLdpStatRemoteIpAddr_Object = MibTableColumn
hwVplsLdpStatRemoteIpAddr = _HwVplsLdpStatRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 2),
    _HwVplsLdpStatRemoteIpAddr_Type()
)
hwVplsLdpStatRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpStatRemoteIpAddr.setStatus("current")
_HwVplsLdpStatEnable_Type = HWEnableValue
_HwVplsLdpStatEnable_Object = MibTableColumn
hwVplsLdpStatEnable = _HwVplsLdpStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 3),
    _HwVplsLdpStatEnable_Type()
)
hwVplsLdpStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsLdpStatEnable.setStatus("current")
_HwVplsLdpStatInTrafficRate_Type = Counter64
_HwVplsLdpStatInTrafficRate_Object = MibTableColumn
hwVplsLdpStatInTrafficRate = _HwVplsLdpStatInTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 4),
    _HwVplsLdpStatInTrafficRate_Type()
)
hwVplsLdpStatInTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInTrafficRate.setStatus("current")
_HwVplsLdpStatOutTrafficRate_Type = Counter64
_HwVplsLdpStatOutTrafficRate_Object = MibTableColumn
hwVplsLdpStatOutTrafficRate = _HwVplsLdpStatOutTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 5),
    _HwVplsLdpStatOutTrafficRate_Type()
)
hwVplsLdpStatOutTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutTrafficRate.setStatus("current")
_HwVplsLdpStatInFrameRate_Type = Counter64
_HwVplsLdpStatInFrameRate_Object = MibTableColumn
hwVplsLdpStatInFrameRate = _HwVplsLdpStatInFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 6),
    _HwVplsLdpStatInFrameRate_Type()
)
hwVplsLdpStatInFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInFrameRate.setStatus("current")
_HwVplsLdpStatOutFrameRate_Type = Counter64
_HwVplsLdpStatOutFrameRate_Object = MibTableColumn
hwVplsLdpStatOutFrameRate = _HwVplsLdpStatOutFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 7),
    _HwVplsLdpStatOutFrameRate_Type()
)
hwVplsLdpStatOutFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutFrameRate.setStatus("current")
_HwVplsLdpStatInBytes_Type = Counter64
_HwVplsLdpStatInBytes_Object = MibTableColumn
hwVplsLdpStatInBytes = _HwVplsLdpStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 8),
    _HwVplsLdpStatInBytes_Type()
)
hwVplsLdpStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInBytes.setStatus("current")
_HwVplsLdpStatOutBytes_Type = Counter64
_HwVplsLdpStatOutBytes_Object = MibTableColumn
hwVplsLdpStatOutBytes = _HwVplsLdpStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 9),
    _HwVplsLdpStatOutBytes_Type()
)
hwVplsLdpStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutBytes.setStatus("current")
_HwVplsLdpStatInFrames_Type = Counter64
_HwVplsLdpStatInFrames_Object = MibTableColumn
hwVplsLdpStatInFrames = _HwVplsLdpStatInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 10),
    _HwVplsLdpStatInFrames_Type()
)
hwVplsLdpStatInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInFrames.setStatus("current")
_HwVplsLdpStatOutFrames_Type = Counter64
_HwVplsLdpStatOutFrames_Object = MibTableColumn
hwVplsLdpStatOutFrames = _HwVplsLdpStatOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 11),
    _HwVplsLdpStatOutFrames_Type()
)
hwVplsLdpStatOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutFrames.setStatus("current")
_HwVplsLdpStatInUnicastFrames_Type = Counter64
_HwVplsLdpStatInUnicastFrames_Object = MibTableColumn
hwVplsLdpStatInUnicastFrames = _HwVplsLdpStatInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 12),
    _HwVplsLdpStatInUnicastFrames_Type()
)
hwVplsLdpStatInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInUnicastFrames.setStatus("current")
_HwVplsLdpStatOutUnicastFrames_Type = Counter64
_HwVplsLdpStatOutUnicastFrames_Object = MibTableColumn
hwVplsLdpStatOutUnicastFrames = _HwVplsLdpStatOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 13),
    _HwVplsLdpStatOutUnicastFrames_Type()
)
hwVplsLdpStatOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutUnicastFrames.setStatus("current")
_HwVplsLdpStatInMulticastFrames_Type = Counter64
_HwVplsLdpStatInMulticastFrames_Object = MibTableColumn
hwVplsLdpStatInMulticastFrames = _HwVplsLdpStatInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 14),
    _HwVplsLdpStatInMulticastFrames_Type()
)
hwVplsLdpStatInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInMulticastFrames.setStatus("current")
_HwVplsLdpStatOutMulticastFrames_Type = Counter64
_HwVplsLdpStatOutMulticastFrames_Object = MibTableColumn
hwVplsLdpStatOutMulticastFrames = _HwVplsLdpStatOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 15),
    _HwVplsLdpStatOutMulticastFrames_Type()
)
hwVplsLdpStatOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutMulticastFrames.setStatus("current")
_HwVplsLdpStatInBroadcastFrames_Type = Counter64
_HwVplsLdpStatInBroadcastFrames_Object = MibTableColumn
hwVplsLdpStatInBroadcastFrames = _HwVplsLdpStatInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 16),
    _HwVplsLdpStatInBroadcastFrames_Type()
)
hwVplsLdpStatInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInBroadcastFrames.setStatus("current")
_HwVplsLdpStatOutBroadcastFrames_Type = Counter64
_HwVplsLdpStatOutBroadcastFrames_Object = MibTableColumn
hwVplsLdpStatOutBroadcastFrames = _HwVplsLdpStatOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 17),
    _HwVplsLdpStatOutBroadcastFrames_Type()
)
hwVplsLdpStatOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutBroadcastFrames.setStatus("current")
_HwVplsLdpStatInDiscardFrames_Type = Counter64
_HwVplsLdpStatInDiscardFrames_Object = MibTableColumn
hwVplsLdpStatInDiscardFrames = _HwVplsLdpStatInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 18),
    _HwVplsLdpStatInDiscardFrames_Type()
)
hwVplsLdpStatInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInDiscardFrames.setStatus("current")
_HwVplsLdpStatOutDiscardFrames_Type = Counter64
_HwVplsLdpStatOutDiscardFrames_Object = MibTableColumn
hwVplsLdpStatOutDiscardFrames = _HwVplsLdpStatOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 19),
    _HwVplsLdpStatOutDiscardFrames_Type()
)
hwVplsLdpStatOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutDiscardFrames.setStatus("current")
_HwVplsLdpStatInErrorFrames_Type = Counter64
_HwVplsLdpStatInErrorFrames_Object = MibTableColumn
hwVplsLdpStatInErrorFrames = _HwVplsLdpStatInErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 20),
    _HwVplsLdpStatInErrorFrames_Type()
)
hwVplsLdpStatInErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInErrorFrames.setStatus("current")
_HwVplsLdpStatOutErrorFrames_Type = Counter64
_HwVplsLdpStatOutErrorFrames_Object = MibTableColumn
hwVplsLdpStatOutErrorFrames = _HwVplsLdpStatOutErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 21),
    _HwVplsLdpStatOutErrorFrames_Type()
)
hwVplsLdpStatOutErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatOutErrorFrames.setStatus("current")
_HwVplsLdpStatInUnknowFrames_Type = Counter64
_HwVplsLdpStatInUnknowFrames_Object = MibTableColumn
hwVplsLdpStatInUnknowFrames = _HwVplsLdpStatInUnknowFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 22),
    _HwVplsLdpStatInUnknowFrames_Type()
)
hwVplsLdpStatInUnknowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatInUnknowFrames.setStatus("current")
_HwVplsLdpStatResetTime_Type = DateAndTime
_HwVplsLdpStatResetTime_Object = MibTableColumn
hwVplsLdpStatResetTime = _HwVplsLdpStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 23),
    _HwVplsLdpStatResetTime_Type()
)
hwVplsLdpStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpStatResetTime.setStatus("current")


class _HwVplsLdpStatResetStatistic_Type(Integer32):
    """Custom type hwVplsLdpStatResetStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistic", 1)
    )


_HwVplsLdpStatResetStatistic_Type.__name__ = "Integer32"
_HwVplsLdpStatResetStatistic_Object = MibTableColumn
hwVplsLdpStatResetStatistic = _HwVplsLdpStatResetStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 9, 1, 24),
    _HwVplsLdpStatResetStatistic_Type()
)
hwVplsLdpStatResetStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsLdpStatResetStatistic.setStatus("current")
_HwVplsBgpStatisticsTable_Object = MibTable
hwVplsBgpStatisticsTable = _HwVplsBgpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwVplsBgpStatisticsTable.setStatus("current")
_HwVplsBgpStatisticsEntry_Object = MibTableRow
hwVplsBgpStatisticsEntry = _HwVplsBgpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1)
)
hwVplsBgpStatisticsEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatSiteID"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    hwVplsBgpStatisticsEntry.setStatus("current")
_HwVplsBgpStatSiteID_Type = Unsigned32
_HwVplsBgpStatSiteID_Object = MibTableColumn
hwVplsBgpStatSiteID = _HwVplsBgpStatSiteID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 1),
    _HwVplsBgpStatSiteID_Type()
)
hwVplsBgpStatSiteID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsBgpStatSiteID.setStatus("current")
_HwVplsBgpStatRemoteIpAddr_Type = IpAddress
_HwVplsBgpStatRemoteIpAddr_Object = MibTableColumn
hwVplsBgpStatRemoteIpAddr = _HwVplsBgpStatRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 2),
    _HwVplsBgpStatRemoteIpAddr_Type()
)
hwVplsBgpStatRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsBgpStatRemoteIpAddr.setStatus("current")
_HwVplsBgpStatEnable_Type = HWEnableValue
_HwVplsBgpStatEnable_Object = MibTableColumn
hwVplsBgpStatEnable = _HwVplsBgpStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 3),
    _HwVplsBgpStatEnable_Type()
)
hwVplsBgpStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsBgpStatEnable.setStatus("current")
_HwVplsBgpStatInTrafficRate_Type = Counter64
_HwVplsBgpStatInTrafficRate_Object = MibTableColumn
hwVplsBgpStatInTrafficRate = _HwVplsBgpStatInTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 4),
    _HwVplsBgpStatInTrafficRate_Type()
)
hwVplsBgpStatInTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInTrafficRate.setStatus("current")
_HwVplsBgpStatOutTrafficRate_Type = Counter64
_HwVplsBgpStatOutTrafficRate_Object = MibTableColumn
hwVplsBgpStatOutTrafficRate = _HwVplsBgpStatOutTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 5),
    _HwVplsBgpStatOutTrafficRate_Type()
)
hwVplsBgpStatOutTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutTrafficRate.setStatus("current")
_HwVplsBgpStatInFrameRate_Type = Counter64
_HwVplsBgpStatInFrameRate_Object = MibTableColumn
hwVplsBgpStatInFrameRate = _HwVplsBgpStatInFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 6),
    _HwVplsBgpStatInFrameRate_Type()
)
hwVplsBgpStatInFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInFrameRate.setStatus("current")
_HwVplsBgpStatOutFrameRate_Type = Counter64
_HwVplsBgpStatOutFrameRate_Object = MibTableColumn
hwVplsBgpStatOutFrameRate = _HwVplsBgpStatOutFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 7),
    _HwVplsBgpStatOutFrameRate_Type()
)
hwVplsBgpStatOutFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutFrameRate.setStatus("current")
_HwVplsBgpStatInBytes_Type = Counter64
_HwVplsBgpStatInBytes_Object = MibTableColumn
hwVplsBgpStatInBytes = _HwVplsBgpStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 8),
    _HwVplsBgpStatInBytes_Type()
)
hwVplsBgpStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInBytes.setStatus("current")
_HwVplsBgpStatOutBytes_Type = Counter64
_HwVplsBgpStatOutBytes_Object = MibTableColumn
hwVplsBgpStatOutBytes = _HwVplsBgpStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 9),
    _HwVplsBgpStatOutBytes_Type()
)
hwVplsBgpStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutBytes.setStatus("current")
_HwVplsBgpStatInFrames_Type = Counter64
_HwVplsBgpStatInFrames_Object = MibTableColumn
hwVplsBgpStatInFrames = _HwVplsBgpStatInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 10),
    _HwVplsBgpStatInFrames_Type()
)
hwVplsBgpStatInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInFrames.setStatus("current")
_HwVplsBgpStatOutFrames_Type = Counter64
_HwVplsBgpStatOutFrames_Object = MibTableColumn
hwVplsBgpStatOutFrames = _HwVplsBgpStatOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 11),
    _HwVplsBgpStatOutFrames_Type()
)
hwVplsBgpStatOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutFrames.setStatus("current")
_HwVplsBgpStatInUnicastFrames_Type = Counter64
_HwVplsBgpStatInUnicastFrames_Object = MibTableColumn
hwVplsBgpStatInUnicastFrames = _HwVplsBgpStatInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 12),
    _HwVplsBgpStatInUnicastFrames_Type()
)
hwVplsBgpStatInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInUnicastFrames.setStatus("current")
_HwVplsBgpStatOutUnicastFrames_Type = Counter64
_HwVplsBgpStatOutUnicastFrames_Object = MibTableColumn
hwVplsBgpStatOutUnicastFrames = _HwVplsBgpStatOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 13),
    _HwVplsBgpStatOutUnicastFrames_Type()
)
hwVplsBgpStatOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutUnicastFrames.setStatus("current")
_HwVplsBgpStatInMulticastFrames_Type = Counter64
_HwVplsBgpStatInMulticastFrames_Object = MibTableColumn
hwVplsBgpStatInMulticastFrames = _HwVplsBgpStatInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 14),
    _HwVplsBgpStatInMulticastFrames_Type()
)
hwVplsBgpStatInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInMulticastFrames.setStatus("current")
_HwVplsBgpStatOutMulticastFrames_Type = Counter64
_HwVplsBgpStatOutMulticastFrames_Object = MibTableColumn
hwVplsBgpStatOutMulticastFrames = _HwVplsBgpStatOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 15),
    _HwVplsBgpStatOutMulticastFrames_Type()
)
hwVplsBgpStatOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutMulticastFrames.setStatus("current")
_HwVplsBgpStatInBroadcastFrames_Type = Counter64
_HwVplsBgpStatInBroadcastFrames_Object = MibTableColumn
hwVplsBgpStatInBroadcastFrames = _HwVplsBgpStatInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 16),
    _HwVplsBgpStatInBroadcastFrames_Type()
)
hwVplsBgpStatInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInBroadcastFrames.setStatus("current")
_HwVplsBgpStatOutBroadcastFrames_Type = Counter64
_HwVplsBgpStatOutBroadcastFrames_Object = MibTableColumn
hwVplsBgpStatOutBroadcastFrames = _HwVplsBgpStatOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 17),
    _HwVplsBgpStatOutBroadcastFrames_Type()
)
hwVplsBgpStatOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutBroadcastFrames.setStatus("current")
_HwVplsBgpStatInDiscardFrames_Type = Counter64
_HwVplsBgpStatInDiscardFrames_Object = MibTableColumn
hwVplsBgpStatInDiscardFrames = _HwVplsBgpStatInDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 18),
    _HwVplsBgpStatInDiscardFrames_Type()
)
hwVplsBgpStatInDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInDiscardFrames.setStatus("current")
_HwVplsBgpStatOutDiscardFrames_Type = Counter64
_HwVplsBgpStatOutDiscardFrames_Object = MibTableColumn
hwVplsBgpStatOutDiscardFrames = _HwVplsBgpStatOutDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 19),
    _HwVplsBgpStatOutDiscardFrames_Type()
)
hwVplsBgpStatOutDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutDiscardFrames.setStatus("current")
_HwVplsBgpStatInErrorFrames_Type = Counter64
_HwVplsBgpStatInErrorFrames_Object = MibTableColumn
hwVplsBgpStatInErrorFrames = _HwVplsBgpStatInErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 20),
    _HwVplsBgpStatInErrorFrames_Type()
)
hwVplsBgpStatInErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInErrorFrames.setStatus("current")
_HwVplsBgpStatOutErrorFrames_Type = Counter64
_HwVplsBgpStatOutErrorFrames_Object = MibTableColumn
hwVplsBgpStatOutErrorFrames = _HwVplsBgpStatOutErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 21),
    _HwVplsBgpStatOutErrorFrames_Type()
)
hwVplsBgpStatOutErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatOutErrorFrames.setStatus("current")
_HwVplsBgpStatInUnknowFrames_Type = Counter64
_HwVplsBgpStatInUnknowFrames_Object = MibTableColumn
hwVplsBgpStatInUnknowFrames = _HwVplsBgpStatInUnknowFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 22),
    _HwVplsBgpStatInUnknowFrames_Type()
)
hwVplsBgpStatInUnknowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatInUnknowFrames.setStatus("current")
_HwVplsBgpStatResetTime_Type = DateAndTime
_HwVplsBgpStatResetTime_Object = MibTableColumn
hwVplsBgpStatResetTime = _HwVplsBgpStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 10, 1, 23),
    _HwVplsBgpStatResetTime_Type()
)
hwVplsBgpStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsBgpStatResetTime.setStatus("current")
_HwVplsLdpPeerTable_Object = MibTable
hwVplsLdpPeerTable = _HwVplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwVplsLdpPeerTable.setStatus("current")
_HwVplsLdpPeerEntry_Object = MibTableRow
hwVplsLdpPeerEntry = _HwVplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1)
)
hwVplsLdpPeerEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerRouterID"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerPwId"),
)
if mibBuilder.loadTexts:
    hwVplsLdpPeerEntry.setStatus("current")
_HwVplsLdpPeerRouterID_Type = IpAddress
_HwVplsLdpPeerRouterID_Object = MibTableColumn
hwVplsLdpPeerRouterID = _HwVplsLdpPeerRouterID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 1),
    _HwVplsLdpPeerRouterID_Type()
)
hwVplsLdpPeerRouterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpPeerRouterID.setStatus("current")
_HwVplsLdpPeerPwId_Type = Unsigned32
_HwVplsLdpPeerPwId_Object = MibTableColumn
hwVplsLdpPeerPwId = _HwVplsLdpPeerPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 2),
    _HwVplsLdpPeerPwId_Type()
)
hwVplsLdpPeerPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpPeerPwId.setStatus("current")


class _HwVplsLdpPeerTnlPolicyName_Type(DisplayString):
    """Custom type hwVplsLdpPeerTnlPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwVplsLdpPeerTnlPolicyName_Type.__name__ = "DisplayString"
_HwVplsLdpPeerTnlPolicyName_Object = MibTableColumn
hwVplsLdpPeerTnlPolicyName = _HwVplsLdpPeerTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 3),
    _HwVplsLdpPeerTnlPolicyName_Type()
)
hwVplsLdpPeerTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerTnlPolicyName.setStatus("current")


class _HwVplsLdpPeerUpeType_Type(Integer32):
    """Custom type hwVplsLdpPeerUpeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("staticupe", 2),
          ("unknown", 3),
          ("upe", 1))
    )


_HwVplsLdpPeerUpeType_Type.__name__ = "Integer32"
_HwVplsLdpPeerUpeType_Object = MibTableColumn
hwVplsLdpPeerUpeType = _HwVplsLdpPeerUpeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 4),
    _HwVplsLdpPeerUpeType_Type()
)
hwVplsLdpPeerUpeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerUpeType.setStatus("current")
_HwVplsLdpPeerTransLable_Type = Unsigned32
_HwVplsLdpPeerTransLable_Object = MibTableColumn
hwVplsLdpPeerTransLable = _HwVplsLdpPeerTransLable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 5),
    _HwVplsLdpPeerTransLable_Type()
)
hwVplsLdpPeerTransLable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerTransLable.setStatus("current")
_HwVplsLdpPeerRecvLable_Type = Unsigned32
_HwVplsLdpPeerRecvLable_Object = MibTableColumn
hwVplsLdpPeerRecvLable = _HwVplsLdpPeerRecvLable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 6),
    _HwVplsLdpPeerRecvLable_Type()
)
hwVplsLdpPeerRecvLable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerRecvLable.setStatus("current")
_HwVplsLdpPeerVrrpIfIndex_Type = InterfaceIndexOrZero
_HwVplsLdpPeerVrrpIfIndex_Object = MibTableColumn
hwVplsLdpPeerVrrpIfIndex = _HwVplsLdpPeerVrrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 7),
    _HwVplsLdpPeerVrrpIfIndex_Type()
)
hwVplsLdpPeerVrrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerVrrpIfIndex.setStatus("current")


class _HwVplsLdpPeerVirtualRouterId_Type(Unsigned32):
    """Custom type hwVplsLdpPeerVirtualRouterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVplsLdpPeerVirtualRouterId_Type.__name__ = "Unsigned32"
_HwVplsLdpPeerVirtualRouterId_Object = MibTableColumn
hwVplsLdpPeerVirtualRouterId = _HwVplsLdpPeerVirtualRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 8),
    _HwVplsLdpPeerVirtualRouterId_Type()
)
hwVplsLdpPeerVirtualRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerVirtualRouterId.setStatus("current")
_HwVplsLdpPeerCir_Type = Unsigned32
_HwVplsLdpPeerCir_Object = MibTableColumn
hwVplsLdpPeerCir = _HwVplsLdpPeerCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 9),
    _HwVplsLdpPeerCir_Type()
)
hwVplsLdpPeerCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerCir.setStatus("current")
_HwVplsLdpPeerPir_Type = Unsigned32
_HwVplsLdpPeerPir_Object = MibTableColumn
hwVplsLdpPeerPir = _HwVplsLdpPeerPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 10),
    _HwVplsLdpPeerPir_Type()
)
hwVplsLdpPeerPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerPir.setStatus("current")


class _HwVplsLdpPeerQosProfileName_Type(DisplayString):
    """Custom type hwVplsLdpPeerQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVplsLdpPeerQosProfileName_Type.__name__ = "DisplayString"
_HwVplsLdpPeerQosProfileName_Object = MibTableColumn
hwVplsLdpPeerQosProfileName = _HwVplsLdpPeerQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 11),
    _HwVplsLdpPeerQosProfileName_Type()
)
hwVplsLdpPeerQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerQosProfileName.setStatus("current")


class _HwVplsLdpPeerStatus_Type(Integer32):
    """Custom type hwVplsLdpPeerStatus based on Integer32"""
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
        *(("backup", 4),
          ("down", 1),
          ("plugout", 3),
          ("up", 2))
    )


_HwVplsLdpPeerStatus_Type.__name__ = "Integer32"
_HwVplsLdpPeerStatus_Object = MibTableColumn
hwVplsLdpPeerStatus = _HwVplsLdpPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 12),
    _HwVplsLdpPeerStatus_Type()
)
hwVplsLdpPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpPeerStatus.setStatus("current")


class _HwVplsLdpPeerPwName_Type(DisplayString):
    """Custom type hwVplsLdpPeerPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwVplsLdpPeerPwName_Type.__name__ = "DisplayString"
_HwVplsLdpPeerPwName_Object = MibTableColumn
hwVplsLdpPeerPwName = _HwVplsLdpPeerPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 13),
    _HwVplsLdpPeerPwName_Type()
)
hwVplsLdpPeerPwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerPwName.setStatus("current")
_HwVplsLdpPeerIgnoreStpLoopCheck_Type = EnabledStatus
_HwVplsLdpPeerIgnoreStpLoopCheck_Object = MibTableColumn
hwVplsLdpPeerIgnoreStpLoopCheck = _HwVplsLdpPeerIgnoreStpLoopCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 14),
    _HwVplsLdpPeerIgnoreStpLoopCheck_Type()
)
hwVplsLdpPeerIgnoreStpLoopCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerIgnoreStpLoopCheck.setStatus("current")
_HwVplsLdpPeerRowStatus_Type = RowStatus
_HwVplsLdpPeerRowStatus_Object = MibTableColumn
hwVplsLdpPeerRowStatus = _HwVplsLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 11, 1, 51),
    _HwVplsLdpPeerRowStatus_Type()
)
hwVplsLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsLdpPeerRowStatus.setStatus("current")
_HwVplsLdpQosStatisticTable_Object = MibTable
hwVplsLdpQosStatisticTable = _HwVplsLdpQosStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwVplsLdpQosStatisticTable.setStatus("current")
_HwVplsLdpQosStatisticEntry_Object = MibTableRow
hwVplsLdpQosStatisticEntry = _HwVplsLdpQosStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1)
)
hwVplsLdpQosStatisticEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatPwId"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatRemoteIpAddr"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatQueueId"),
)
if mibBuilder.loadTexts:
    hwVplsLdpQosStatisticEntry.setStatus("current")
_HwVplsLdpQosStatPwId_Type = Unsigned32
_HwVplsLdpQosStatPwId_Object = MibTableColumn
hwVplsLdpQosStatPwId = _HwVplsLdpQosStatPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 1),
    _HwVplsLdpQosStatPwId_Type()
)
hwVplsLdpQosStatPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatPwId.setStatus("current")
_HwVplsLdpQosStatRemoteIpAddr_Type = IpAddress
_HwVplsLdpQosStatRemoteIpAddr_Object = MibTableColumn
hwVplsLdpQosStatRemoteIpAddr = _HwVplsLdpQosStatRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 2),
    _HwVplsLdpQosStatRemoteIpAddr_Type()
)
hwVplsLdpQosStatRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatRemoteIpAddr.setStatus("current")


class _HwVplsLdpQosStatQueueId_Type(Integer32):
    """Custom type hwVplsLdpQosStatQueueId based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwVplsLdpQosStatQueueId_Type.__name__ = "Integer32"
_HwVplsLdpQosStatQueueId_Object = MibTableColumn
hwVplsLdpQosStatQueueId = _HwVplsLdpQosStatQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 3),
    _HwVplsLdpQosStatQueueId_Type()
)
hwVplsLdpQosStatQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatQueueId.setStatus("current")
_HwVplsLdpQosStatTotalPassPacket_Type = Counter64
_HwVplsLdpQosStatTotalPassPacket_Object = MibTableColumn
hwVplsLdpQosStatTotalPassPacket = _HwVplsLdpQosStatTotalPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 4),
    _HwVplsLdpQosStatTotalPassPacket_Type()
)
hwVplsLdpQosStatTotalPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatTotalPassPacket.setStatus("current")
_HwVplsLdpQosStatTotalPassByte_Type = Counter64
_HwVplsLdpQosStatTotalPassByte_Object = MibTableColumn
hwVplsLdpQosStatTotalPassByte = _HwVplsLdpQosStatTotalPassByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 5),
    _HwVplsLdpQosStatTotalPassByte_Type()
)
hwVplsLdpQosStatTotalPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatTotalPassByte.setStatus("current")
_HwVplsLdpQosStatTotalDiscardPacket_Type = Counter64
_HwVplsLdpQosStatTotalDiscardPacket_Object = MibTableColumn
hwVplsLdpQosStatTotalDiscardPacket = _HwVplsLdpQosStatTotalDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 6),
    _HwVplsLdpQosStatTotalDiscardPacket_Type()
)
hwVplsLdpQosStatTotalDiscardPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatTotalDiscardPacket.setStatus("current")
_HwVplsLdpQosStatTotalDiscardByte_Type = Counter64
_HwVplsLdpQosStatTotalDiscardByte_Object = MibTableColumn
hwVplsLdpQosStatTotalDiscardByte = _HwVplsLdpQosStatTotalDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 7),
    _HwVplsLdpQosStatTotalDiscardByte_Type()
)
hwVplsLdpQosStatTotalDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatTotalDiscardByte.setStatus("current")
_HwVplsLdpQosStatPassPacketRate_Type = Counter64
_HwVplsLdpQosStatPassPacketRate_Object = MibTableColumn
hwVplsLdpQosStatPassPacketRate = _HwVplsLdpQosStatPassPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 8),
    _HwVplsLdpQosStatPassPacketRate_Type()
)
hwVplsLdpQosStatPassPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatPassPacketRate.setStatus("current")
_HwVplsLdpQosStatPassByteRate_Type = Counter64
_HwVplsLdpQosStatPassByteRate_Object = MibTableColumn
hwVplsLdpQosStatPassByteRate = _HwVplsLdpQosStatPassByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 9),
    _HwVplsLdpQosStatPassByteRate_Type()
)
hwVplsLdpQosStatPassByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatPassByteRate.setStatus("current")
_HwVplsLdpQosStatDiscardPacketRate_Type = Counter64
_HwVplsLdpQosStatDiscardPacketRate_Object = MibTableColumn
hwVplsLdpQosStatDiscardPacketRate = _HwVplsLdpQosStatDiscardPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 10),
    _HwVplsLdpQosStatDiscardPacketRate_Type()
)
hwVplsLdpQosStatDiscardPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatDiscardPacketRate.setStatus("current")
_HwVplsLdpQosStatDiscardByteRate_Type = Counter64
_HwVplsLdpQosStatDiscardByteRate_Object = MibTableColumn
hwVplsLdpQosStatDiscardByteRate = _HwVplsLdpQosStatDiscardByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 12, 1, 11),
    _HwVplsLdpQosStatDiscardByteRate_Type()
)
hwVplsLdpQosStatDiscardByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLdpQosStatDiscardByteRate.setStatus("current")
_HwVplsStatisticTable_Object = MibTable
hwVplsStatisticTable = _HwVplsStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hwVplsStatisticTable.setStatus("current")
_HwVplsStatisticEntry_Object = MibTableRow
hwVplsStatisticEntry = _HwVplsStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1)
)
hwVplsStatisticEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
)
if mibBuilder.loadTexts:
    hwVplsStatisticEntry.setStatus("current")
_HwVplsStatEnable_Type = EnabledStatus
_HwVplsStatEnable_Object = MibTableColumn
hwVplsStatEnable = _HwVplsStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 1),
    _HwVplsStatEnable_Type()
)
hwVplsStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsStatEnable.setStatus("current")


class _HwVplsStatResetStatistic_Type(Integer32):
    """Custom type hwVplsStatResetStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistic", 1)
    )


_HwVplsStatResetStatistic_Type.__name__ = "Integer32"
_HwVplsStatResetStatistic_Object = MibTableColumn
hwVplsStatResetStatistic = _HwVplsStatResetStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 2),
    _HwVplsStatResetStatistic_Type()
)
hwVplsStatResetStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVplsStatResetStatistic.setStatus("current")
_HwVplsStatResetTime_Type = DateAndTime
_HwVplsStatResetTime_Object = MibTableColumn
hwVplsStatResetTime = _HwVplsStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 3),
    _HwVplsStatResetTime_Type()
)
hwVplsStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatResetTime.setStatus("current")
_HwVplsStatQosPacketRate_Type = Counter64
_HwVplsStatQosPacketRate_Object = MibTableColumn
hwVplsStatQosPacketRate = _HwVplsStatQosPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 4),
    _HwVplsStatQosPacketRate_Type()
)
hwVplsStatQosPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatQosPacketRate.setStatus("current")
_HwVplsStatQosByteRate_Type = Counter64
_HwVplsStatQosByteRate_Object = MibTableColumn
hwVplsStatQosByteRate = _HwVplsStatQosByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 5),
    _HwVplsStatQosByteRate_Type()
)
hwVplsStatQosByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatQosByteRate.setStatus("current")
_HwVplsStatQosPacket_Type = Counter64
_HwVplsStatQosPacket_Object = MibTableColumn
hwVplsStatQosPacket = _HwVplsStatQosPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 6),
    _HwVplsStatQosPacket_Type()
)
hwVplsStatQosPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatQosPacket.setStatus("current")
_HwVplsStatQosByte_Type = Counter64
_HwVplsStatQosByte_Object = MibTableColumn
hwVplsStatQosByte = _HwVplsStatQosByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 13, 1, 7),
    _HwVplsStatQosByte_Type()
)
hwVplsStatQosByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsStatQosByte.setStatus("current")
_HwVplsQosStatisticTable_Object = MibTable
hwVplsQosStatisticTable = _HwVplsQosStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hwVplsQosStatisticTable.setStatus("current")
_HwVplsQosStatisticEntry_Object = MibTableRow
hwVplsQosStatisticEntry = _HwVplsQosStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1)
)
hwVplsQosStatisticEntry.setIndexNames(
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatQueueId"),
)
if mibBuilder.loadTexts:
    hwVplsQosStatisticEntry.setStatus("current")


class _HwVplsQosStatQueueId_Type(Integer32):
    """Custom type hwVplsQosStatQueueId based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwVplsQosStatQueueId_Type.__name__ = "Integer32"
_HwVplsQosStatQueueId_Object = MibTableColumn
hwVplsQosStatQueueId = _HwVplsQosStatQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 1),
    _HwVplsQosStatQueueId_Type()
)
hwVplsQosStatQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsQosStatQueueId.setStatus("current")
_HwVplsQosStatTotalPassPacket_Type = Counter64
_HwVplsQosStatTotalPassPacket_Object = MibTableColumn
hwVplsQosStatTotalPassPacket = _HwVplsQosStatTotalPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 2),
    _HwVplsQosStatTotalPassPacket_Type()
)
hwVplsQosStatTotalPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatTotalPassPacket.setStatus("current")
_HwVplsQosStatTotalPassByte_Type = Counter64
_HwVplsQosStatTotalPassByte_Object = MibTableColumn
hwVplsQosStatTotalPassByte = _HwVplsQosStatTotalPassByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 3),
    _HwVplsQosStatTotalPassByte_Type()
)
hwVplsQosStatTotalPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatTotalPassByte.setStatus("current")
_HwVplsQosStatTotalDiscardPacket_Type = Counter64
_HwVplsQosStatTotalDiscardPacket_Object = MibTableColumn
hwVplsQosStatTotalDiscardPacket = _HwVplsQosStatTotalDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 4),
    _HwVplsQosStatTotalDiscardPacket_Type()
)
hwVplsQosStatTotalDiscardPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatTotalDiscardPacket.setStatus("current")
_HwVplsQosStatTotalDiscardByte_Type = Counter64
_HwVplsQosStatTotalDiscardByte_Object = MibTableColumn
hwVplsQosStatTotalDiscardByte = _HwVplsQosStatTotalDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 5),
    _HwVplsQosStatTotalDiscardByte_Type()
)
hwVplsQosStatTotalDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatTotalDiscardByte.setStatus("current")
_HwVplsQosStatPassPacketRate_Type = Counter64
_HwVplsQosStatPassPacketRate_Object = MibTableColumn
hwVplsQosStatPassPacketRate = _HwVplsQosStatPassPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 6),
    _HwVplsQosStatPassPacketRate_Type()
)
hwVplsQosStatPassPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatPassPacketRate.setStatus("current")
_HwVplsQosStatPassByteRate_Type = Counter64
_HwVplsQosStatPassByteRate_Object = MibTableColumn
hwVplsQosStatPassByteRate = _HwVplsQosStatPassByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 7),
    _HwVplsQosStatPassByteRate_Type()
)
hwVplsQosStatPassByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatPassByteRate.setStatus("current")
_HwVplsQosStatDiscardPacketRate_Type = Counter64
_HwVplsQosStatDiscardPacketRate_Object = MibTableColumn
hwVplsQosStatDiscardPacketRate = _HwVplsQosStatDiscardPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 8),
    _HwVplsQosStatDiscardPacketRate_Type()
)
hwVplsQosStatDiscardPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatDiscardPacketRate.setStatus("current")
_HwVplsQosStatDiscardByteRate_Type = Counter64
_HwVplsQosStatDiscardByteRate_Object = MibTableColumn
hwVplsQosStatDiscardByteRate = _HwVplsQosStatDiscardByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 1, 14, 1, 9),
    _HwVplsQosStatDiscardByteRate_Type()
)
hwVplsQosStatDiscardByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsQosStatDiscardByteRate.setStatus("current")
_HwVplsMIBTraps_ObjectIdentity = ObjectIdentity
hwVplsMIBTraps = _HwVplsMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2)
)
_HwVplsMIBConformance_ObjectIdentity = ObjectIdentity
hwVplsMIBConformance = _HwVplsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3)
)
_HwVplsMIBCompliances_ObjectIdentity = ObjectIdentity
hwVplsMIBCompliances = _HwVplsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 1)
)
_HwVplsMIBGroups_ObjectIdentity = ObjectIdentity
hwVplsMIBGroups = _HwVplsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2)
)

# Managed Objects groups

hwVplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 1)
)
hwVplsGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsSignal"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsRD"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiID"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVcType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatus"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsMtu"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsTunnelPolicy"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDescription"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLearnStyle"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsMacLearnEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsMacLimitEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatisticsEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsUnknowMulticast"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsUnknowUnicast"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPreference"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAdminVsiName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAcIsolateFlag"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDiffServMode"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDiffServServiceClass"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDiffServColor"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDiffServDSName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsInterfaceWithdraw"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsUpe2NpeWithdraw"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsUpe2UpeWithdraw"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsNpe2UpeWithdraw"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsDiscovery"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsMacWithdrawEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiCir"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiPir"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiQosProfileName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAdminStatus"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsIgnoreAcState"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsEnableStatistic"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsResetStatistic"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsResetStatisticTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAgingTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsUnknowUnicastMacLearning"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsFlowLabel"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsServiceName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsGroup.setStatus("current")

hwVplsRtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 2)
)
hwVplsRtGroup.setObjects(
    ("HUAWEI-VPLS-EXT-MIB", "hwVplsRtRowStatus")
)
if mibBuilder.loadTexts:
    hwVplsRtGroup.setStatus("current")

hwVplsAcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 3)
)
hwVplsAcGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsAcStatus"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAcUpStartTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAcUpSumTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsAcRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsAcGroup.setStatus("current")

hwVplsBgpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 4)
)
hwVplsBgpInfoGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpInfoRange"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpInfoOffset"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpInfoRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsBgpInfoGroup.setStatus("current")

hwVplsPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 5)
)
hwVplsPwGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsPwTnlPolicy"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwIsUpe"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwInboundLabel"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwOutboundLabel"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwStatus"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwVrIfIndex"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwVrID"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwUpStartTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwUpSumTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsPwGroup.setStatus("current")

hwVplsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 6)
)
hwVplsStatisticsGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsOutFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsInFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsOutBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsInBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsInDiscardFrames"))
)
if mibBuilder.loadTexts:
    hwVplsStatisticsGroup.setStatus("current")

hwVplsNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 7)
)
hwVplsNotificationControlGroup.setObjects(
    ("HUAWEI-VPLS-EXT-MIB", "hwVplsUpDownNotifEnable")
)
if mibBuilder.loadTexts:
    hwVplsNotificationControlGroup.setStatus("current")

hwVplsStateReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 8)
)
hwVplsStateReasonGroup.setObjects(
    ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason")
)
if mibBuilder.loadTexts:
    hwVplsStateReasonGroup.setStatus("current")

hwVplsLdpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 10)
)
hwVplsLdpStatisticsGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInTrafficRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutTrafficRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInFrameRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutFrameRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInUnicastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutUnicastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInMulticastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutMulticastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInBroadcastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutBroadcastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInDiscardFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutDiscardFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInErrorFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatOutErrorFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatInUnknowFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatResetTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpStatResetStatistic"))
)
if mibBuilder.loadTexts:
    hwVplsLdpStatisticsGroup.setStatus("current")

hwVplsBgpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 11)
)
hwVplsBgpStatisticsGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInTrafficRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutTrafficRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInFrameRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutFrameRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutBytes"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInUnicastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutUnicastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInMulticastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutMulticastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInBroadcastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutBroadcastFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInDiscardFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutDiscardFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInErrorFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatOutErrorFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatInUnknowFrames"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsBgpStatResetTime"))
)
if mibBuilder.loadTexts:
    hwVplsBgpStatisticsGroup.setStatus("current")

hwVplsLdpPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 12)
)
hwVplsLdpPeerGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerTnlPolicyName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerUpeType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerTransLable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerRecvLable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerVrrpIfIndex"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerVirtualRouterId"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerCir"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerPir"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerQosProfileName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerStatus"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerPwName"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerIgnoreStpLoopCheck"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsLdpPeerGroup.setStatus("current")

hwVplsLdpQosStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 13)
)
hwVplsLdpQosStatisticGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatTotalPassPacket"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatTotalPassByte"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatTotalDiscardPacket"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatTotalDiscardByte"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatPassPacketRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatPassByteRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatDiscardPacketRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsLdpQosStatDiscardByteRate"))
)
if mibBuilder.loadTexts:
    hwVplsLdpQosStatisticGroup.setStatus("current")

hwVplsStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 14)
)
hwVplsStatisticGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsStatEnable"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatResetStatistic"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatResetTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatQosPacketRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatQosByteRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatQosPacket"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatQosByte"))
)
if mibBuilder.loadTexts:
    hwVplsStatisticGroup.setStatus("current")

hwVplsQosStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 15)
)
hwVplsQosStatisticGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatTotalPassPacket"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatTotalPassByte"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatTotalDiscardPacket"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatTotalDiscardByte"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatPassPacketRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatPassByteRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatDiscardPacketRate"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsQosStatDiscardByteRate"))
)
if mibBuilder.loadTexts:
    hwVplsQosStatisticGroup.setStatus("current")


# Notification objects

hwVplsVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 1)
)
hwVplsVcDown.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsPwType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwTnlPolicy"))
)
if mibBuilder.loadTexts:
    hwVplsVcDown.setStatus(
        "current"
    )

hwVplsVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 2)
)
hwVplsVcUp.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsPwType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwTnlPolicy"))
)
if mibBuilder.loadTexts:
    hwVplsVcUp.setStatus(
        "current"
    )

hwVplsVsiDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 3)
)
hwVplsVsiDown.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiID"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVplsVsiDown.setStatus(
        "current"
    )

hwVplsVsiUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 4)
)
hwVplsVsiUp.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiID"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVplsVsiUp.setStatus(
        "current"
    )

hwVplsVcBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 5)
)
hwVplsVcBackup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsPwType"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"))
)
if mibBuilder.loadTexts:
    hwVplsVcBackup.setStatus(
        "current"
    )

hwVplsVsiDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 6)
)
hwVplsVsiDeleted.setObjects(
    ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiID")
)
if mibBuilder.loadTexts:
    hwVplsVsiDeleted.setStatus(
        "current"
    )

hwVplsVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 2, 7)
)
hwVplsVcDeleted.setObjects(
    ("HUAWEI-VPLS-EXT-MIB", "hwVplsPwType")
)
if mibBuilder.loadTexts:
    hwVplsVcDeleted.setStatus(
        "current"
    )


# Notifications groups

hwVplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 2, 9)
)
hwVplsNotificationGroup.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsVcDown"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVcUp"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiDown"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiUp"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVcBackup"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiDeleted"),
        ("HUAWEI-VPLS-EXT-MIB", "hwVplsVcDeleted"))
)
if mibBuilder.loadTexts:
    hwVplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwVplsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    **{"HWL2VpnVcEncapsType": HWL2VpnVcEncapsType,
       "HWEnableValue": HWEnableValue,
       "HWL2VpnStateChangeReason": HWL2VpnStateChangeReason,
       "hwL2Vpn": hwL2Vpn,
       "hwL2VpnVplsExt": hwL2VpnVplsExt,
       "hwVplsMIBObjects": hwVplsMIBObjects,
       "hwVplsTable": hwVplsTable,
       "hwVplsEntry": hwVplsEntry,
       "hwVplsVsiName": hwVplsVsiName,
       "hwVplsSignal": hwVplsSignal,
       "hwVplsRD": hwVplsRD,
       "hwVplsVsiID": hwVplsVsiID,
       "hwVplsVcType": hwVplsVcType,
       "hwVplsStatus": hwVplsStatus,
       "hwVplsMtu": hwVplsMtu,
       "hwVplsTunnelPolicy": hwVplsTunnelPolicy,
       "hwVplsDescription": hwVplsDescription,
       "hwVplsLearnStyle": hwVplsLearnStyle,
       "hwVplsMacLearnEnable": hwVplsMacLearnEnable,
       "hwVplsMacLimitEnable": hwVplsMacLimitEnable,
       "hwVplsStatisticsEnable": hwVplsStatisticsEnable,
       "hwVplsUnknowMulticast": hwVplsUnknowMulticast,
       "hwVplsUnknowUnicast": hwVplsUnknowUnicast,
       "hwVplsPreference": hwVplsPreference,
       "hwVplsVsiType": hwVplsVsiType,
       "hwVplsAdminVsiName": hwVplsAdminVsiName,
       "hwVplsAcIsolateFlag": hwVplsAcIsolateFlag,
       "hwVplsDiffServMode": hwVplsDiffServMode,
       "hwVplsDiffServServiceClass": hwVplsDiffServServiceClass,
       "hwVplsDiffServColor": hwVplsDiffServColor,
       "hwVplsDiffServDSName": hwVplsDiffServDSName,
       "hwVplsInterfaceWithdraw": hwVplsInterfaceWithdraw,
       "hwVplsUpe2NpeWithdraw": hwVplsUpe2NpeWithdraw,
       "hwVplsUpe2UpeWithdraw": hwVplsUpe2UpeWithdraw,
       "hwVplsNpe2UpeWithdraw": hwVplsNpe2UpeWithdraw,
       "hwVplsDiscovery": hwVplsDiscovery,
       "hwVplsMacWithdrawEnable": hwVplsMacWithdrawEnable,
       "hwVplsVsiCir": hwVplsVsiCir,
       "hwVplsVsiPir": hwVplsVsiPir,
       "hwVplsVsiQosProfileName": hwVplsVsiQosProfileName,
       "hwVplsAdminStatus": hwVplsAdminStatus,
       "hwVplsIgnoreAcState": hwVplsIgnoreAcState,
       "hwVplsEnableStatistic": hwVplsEnableStatistic,
       "hwVplsResetStatistic": hwVplsResetStatistic,
       "hwVplsResetStatisticTime": hwVplsResetStatisticTime,
       "hwVplsAgingTime": hwVplsAgingTime,
       "hwVplsUnknowUnicastMacLearning": hwVplsUnknowUnicastMacLearning,
       "hwVplsFlowLabel": hwVplsFlowLabel,
       "hwVplsServiceName": hwVplsServiceName,
       "hwVplsRowStatus": hwVplsRowStatus,
       "hwVplsRtTable": hwVplsRtTable,
       "hwVplsRtEntry": hwVplsRtEntry,
       "hwVplsRtType": hwVplsRtType,
       "hwVplsRtName": hwVplsRtName,
       "hwVplsRtRowStatus": hwVplsRtRowStatus,
       "hwVplsAcTable": hwVplsAcTable,
       "hwVplsAcEntry": hwVplsAcEntry,
       "hwVplsAcIfIndex": hwVplsAcIfIndex,
       "hwVplsAcStatus": hwVplsAcStatus,
       "hwVplsAcUpStartTime": hwVplsAcUpStartTime,
       "hwVplsAcUpSumTime": hwVplsAcUpSumTime,
       "hwVplsAcRowStatus": hwVplsAcRowStatus,
       "hwVplsBgpInfoTable": hwVplsBgpInfoTable,
       "hwVplsBgpInfoEntry": hwVplsBgpInfoEntry,
       "hwVplsBgpInfoSiteID": hwVplsBgpInfoSiteID,
       "hwVplsBgpInfoRange": hwVplsBgpInfoRange,
       "hwVplsBgpInfoOffset": hwVplsBgpInfoOffset,
       "hwVplsBgpInfoRowStatus": hwVplsBgpInfoRowStatus,
       "hwVplsPwTable": hwVplsPwTable,
       "hwVplsPwEntry": hwVplsPwEntry,
       "hwVplsPwID": hwVplsPwID,
       "hwVplsPwRemoteIp": hwVplsPwRemoteIp,
       "hwVplsPwTnlPolicy": hwVplsPwTnlPolicy,
       "hwVplsPwType": hwVplsPwType,
       "hwVplsPwIsUpe": hwVplsPwIsUpe,
       "hwVplsPwInboundLabel": hwVplsPwInboundLabel,
       "hwVplsPwOutboundLabel": hwVplsPwOutboundLabel,
       "hwVplsPwStatus": hwVplsPwStatus,
       "hwVplsPwVrIfIndex": hwVplsPwVrIfIndex,
       "hwVplsPwVrID": hwVplsPwVrID,
       "hwVplsPwUpStartTime": hwVplsPwUpStartTime,
       "hwVplsPwUpSumTime": hwVplsPwUpSumTime,
       "hwVplsPwRowStatus": hwVplsPwRowStatus,
       "hwVplsStatisticsTable": hwVplsStatisticsTable,
       "hwVplsStatisticsEntry": hwVplsStatisticsEntry,
       "hwVplsOutFrames": hwVplsOutFrames,
       "hwVplsInFrames": hwVplsInFrames,
       "hwVplsOutBytes": hwVplsOutBytes,
       "hwVplsInBytes": hwVplsInBytes,
       "hwVplsInDiscardFrames": hwVplsInDiscardFrames,
       "hwVplsUpDownNotifEnable": hwVplsUpDownNotifEnable,
       "hwVplsStateChangeReason": hwVplsStateChangeReason,
       "hwVplsLdpStatisticsTable": hwVplsLdpStatisticsTable,
       "hwVplsLdpStatisticsEntry": hwVplsLdpStatisticsEntry,
       "hwVplsLdpStatPwID": hwVplsLdpStatPwID,
       "hwVplsLdpStatRemoteIpAddr": hwVplsLdpStatRemoteIpAddr,
       "hwVplsLdpStatEnable": hwVplsLdpStatEnable,
       "hwVplsLdpStatInTrafficRate": hwVplsLdpStatInTrafficRate,
       "hwVplsLdpStatOutTrafficRate": hwVplsLdpStatOutTrafficRate,
       "hwVplsLdpStatInFrameRate": hwVplsLdpStatInFrameRate,
       "hwVplsLdpStatOutFrameRate": hwVplsLdpStatOutFrameRate,
       "hwVplsLdpStatInBytes": hwVplsLdpStatInBytes,
       "hwVplsLdpStatOutBytes": hwVplsLdpStatOutBytes,
       "hwVplsLdpStatInFrames": hwVplsLdpStatInFrames,
       "hwVplsLdpStatOutFrames": hwVplsLdpStatOutFrames,
       "hwVplsLdpStatInUnicastFrames": hwVplsLdpStatInUnicastFrames,
       "hwVplsLdpStatOutUnicastFrames": hwVplsLdpStatOutUnicastFrames,
       "hwVplsLdpStatInMulticastFrames": hwVplsLdpStatInMulticastFrames,
       "hwVplsLdpStatOutMulticastFrames": hwVplsLdpStatOutMulticastFrames,
       "hwVplsLdpStatInBroadcastFrames": hwVplsLdpStatInBroadcastFrames,
       "hwVplsLdpStatOutBroadcastFrames": hwVplsLdpStatOutBroadcastFrames,
       "hwVplsLdpStatInDiscardFrames": hwVplsLdpStatInDiscardFrames,
       "hwVplsLdpStatOutDiscardFrames": hwVplsLdpStatOutDiscardFrames,
       "hwVplsLdpStatInErrorFrames": hwVplsLdpStatInErrorFrames,
       "hwVplsLdpStatOutErrorFrames": hwVplsLdpStatOutErrorFrames,
       "hwVplsLdpStatInUnknowFrames": hwVplsLdpStatInUnknowFrames,
       "hwVplsLdpStatResetTime": hwVplsLdpStatResetTime,
       "hwVplsLdpStatResetStatistic": hwVplsLdpStatResetStatistic,
       "hwVplsBgpStatisticsTable": hwVplsBgpStatisticsTable,
       "hwVplsBgpStatisticsEntry": hwVplsBgpStatisticsEntry,
       "hwVplsBgpStatSiteID": hwVplsBgpStatSiteID,
       "hwVplsBgpStatRemoteIpAddr": hwVplsBgpStatRemoteIpAddr,
       "hwVplsBgpStatEnable": hwVplsBgpStatEnable,
       "hwVplsBgpStatInTrafficRate": hwVplsBgpStatInTrafficRate,
       "hwVplsBgpStatOutTrafficRate": hwVplsBgpStatOutTrafficRate,
       "hwVplsBgpStatInFrameRate": hwVplsBgpStatInFrameRate,
       "hwVplsBgpStatOutFrameRate": hwVplsBgpStatOutFrameRate,
       "hwVplsBgpStatInBytes": hwVplsBgpStatInBytes,
       "hwVplsBgpStatOutBytes": hwVplsBgpStatOutBytes,
       "hwVplsBgpStatInFrames": hwVplsBgpStatInFrames,
       "hwVplsBgpStatOutFrames": hwVplsBgpStatOutFrames,
       "hwVplsBgpStatInUnicastFrames": hwVplsBgpStatInUnicastFrames,
       "hwVplsBgpStatOutUnicastFrames": hwVplsBgpStatOutUnicastFrames,
       "hwVplsBgpStatInMulticastFrames": hwVplsBgpStatInMulticastFrames,
       "hwVplsBgpStatOutMulticastFrames": hwVplsBgpStatOutMulticastFrames,
       "hwVplsBgpStatInBroadcastFrames": hwVplsBgpStatInBroadcastFrames,
       "hwVplsBgpStatOutBroadcastFrames": hwVplsBgpStatOutBroadcastFrames,
       "hwVplsBgpStatInDiscardFrames": hwVplsBgpStatInDiscardFrames,
       "hwVplsBgpStatOutDiscardFrames": hwVplsBgpStatOutDiscardFrames,
       "hwVplsBgpStatInErrorFrames": hwVplsBgpStatInErrorFrames,
       "hwVplsBgpStatOutErrorFrames": hwVplsBgpStatOutErrorFrames,
       "hwVplsBgpStatInUnknowFrames": hwVplsBgpStatInUnknowFrames,
       "hwVplsBgpStatResetTime": hwVplsBgpStatResetTime,
       "hwVplsLdpPeerTable": hwVplsLdpPeerTable,
       "hwVplsLdpPeerEntry": hwVplsLdpPeerEntry,
       "hwVplsLdpPeerRouterID": hwVplsLdpPeerRouterID,
       "hwVplsLdpPeerPwId": hwVplsLdpPeerPwId,
       "hwVplsLdpPeerTnlPolicyName": hwVplsLdpPeerTnlPolicyName,
       "hwVplsLdpPeerUpeType": hwVplsLdpPeerUpeType,
       "hwVplsLdpPeerTransLable": hwVplsLdpPeerTransLable,
       "hwVplsLdpPeerRecvLable": hwVplsLdpPeerRecvLable,
       "hwVplsLdpPeerVrrpIfIndex": hwVplsLdpPeerVrrpIfIndex,
       "hwVplsLdpPeerVirtualRouterId": hwVplsLdpPeerVirtualRouterId,
       "hwVplsLdpPeerCir": hwVplsLdpPeerCir,
       "hwVplsLdpPeerPir": hwVplsLdpPeerPir,
       "hwVplsLdpPeerQosProfileName": hwVplsLdpPeerQosProfileName,
       "hwVplsLdpPeerStatus": hwVplsLdpPeerStatus,
       "hwVplsLdpPeerPwName": hwVplsLdpPeerPwName,
       "hwVplsLdpPeerIgnoreStpLoopCheck": hwVplsLdpPeerIgnoreStpLoopCheck,
       "hwVplsLdpPeerRowStatus": hwVplsLdpPeerRowStatus,
       "hwVplsLdpQosStatisticTable": hwVplsLdpQosStatisticTable,
       "hwVplsLdpQosStatisticEntry": hwVplsLdpQosStatisticEntry,
       "hwVplsLdpQosStatPwId": hwVplsLdpQosStatPwId,
       "hwVplsLdpQosStatRemoteIpAddr": hwVplsLdpQosStatRemoteIpAddr,
       "hwVplsLdpQosStatQueueId": hwVplsLdpQosStatQueueId,
       "hwVplsLdpQosStatTotalPassPacket": hwVplsLdpQosStatTotalPassPacket,
       "hwVplsLdpQosStatTotalPassByte": hwVplsLdpQosStatTotalPassByte,
       "hwVplsLdpQosStatTotalDiscardPacket": hwVplsLdpQosStatTotalDiscardPacket,
       "hwVplsLdpQosStatTotalDiscardByte": hwVplsLdpQosStatTotalDiscardByte,
       "hwVplsLdpQosStatPassPacketRate": hwVplsLdpQosStatPassPacketRate,
       "hwVplsLdpQosStatPassByteRate": hwVplsLdpQosStatPassByteRate,
       "hwVplsLdpQosStatDiscardPacketRate": hwVplsLdpQosStatDiscardPacketRate,
       "hwVplsLdpQosStatDiscardByteRate": hwVplsLdpQosStatDiscardByteRate,
       "hwVplsStatisticTable": hwVplsStatisticTable,
       "hwVplsStatisticEntry": hwVplsStatisticEntry,
       "hwVplsStatEnable": hwVplsStatEnable,
       "hwVplsStatResetStatistic": hwVplsStatResetStatistic,
       "hwVplsStatResetTime": hwVplsStatResetTime,
       "hwVplsStatQosPacketRate": hwVplsStatQosPacketRate,
       "hwVplsStatQosByteRate": hwVplsStatQosByteRate,
       "hwVplsStatQosPacket": hwVplsStatQosPacket,
       "hwVplsStatQosByte": hwVplsStatQosByte,
       "hwVplsQosStatisticTable": hwVplsQosStatisticTable,
       "hwVplsQosStatisticEntry": hwVplsQosStatisticEntry,
       "hwVplsQosStatQueueId": hwVplsQosStatQueueId,
       "hwVplsQosStatTotalPassPacket": hwVplsQosStatTotalPassPacket,
       "hwVplsQosStatTotalPassByte": hwVplsQosStatTotalPassByte,
       "hwVplsQosStatTotalDiscardPacket": hwVplsQosStatTotalDiscardPacket,
       "hwVplsQosStatTotalDiscardByte": hwVplsQosStatTotalDiscardByte,
       "hwVplsQosStatPassPacketRate": hwVplsQosStatPassPacketRate,
       "hwVplsQosStatPassByteRate": hwVplsQosStatPassByteRate,
       "hwVplsQosStatDiscardPacketRate": hwVplsQosStatDiscardPacketRate,
       "hwVplsQosStatDiscardByteRate": hwVplsQosStatDiscardByteRate,
       "hwVplsMIBTraps": hwVplsMIBTraps,
       "hwVplsVcDown": hwVplsVcDown,
       "hwVplsVcUp": hwVplsVcUp,
       "hwVplsVsiDown": hwVplsVsiDown,
       "hwVplsVsiUp": hwVplsVsiUp,
       "hwVplsVcBackup": hwVplsVcBackup,
       "hwVplsVsiDeleted": hwVplsVsiDeleted,
       "hwVplsVcDeleted": hwVplsVcDeleted,
       "hwVplsMIBConformance": hwVplsMIBConformance,
       "hwVplsMIBCompliances": hwVplsMIBCompliances,
       "hwVplsMIBCompliance": hwVplsMIBCompliance,
       "hwVplsMIBGroups": hwVplsMIBGroups,
       "hwVplsGroup": hwVplsGroup,
       "hwVplsRtGroup": hwVplsRtGroup,
       "hwVplsAcGroup": hwVplsAcGroup,
       "hwVplsBgpInfoGroup": hwVplsBgpInfoGroup,
       "hwVplsPwGroup": hwVplsPwGroup,
       "hwVplsStatisticsGroup": hwVplsStatisticsGroup,
       "hwVplsNotificationControlGroup": hwVplsNotificationControlGroup,
       "hwVplsStateReasonGroup": hwVplsStateReasonGroup,
       "hwVplsNotificationGroup": hwVplsNotificationGroup,
       "hwVplsLdpStatisticsGroup": hwVplsLdpStatisticsGroup,
       "hwVplsBgpStatisticsGroup": hwVplsBgpStatisticsGroup,
       "hwVplsLdpPeerGroup": hwVplsLdpPeerGroup,
       "hwVplsLdpQosStatisticGroup": hwVplsLdpQosStatisticGroup,
       "hwVplsStatisticGroup": hwVplsStatisticGroup,
       "hwVplsQosStatisticGroup": hwVplsQosStatisticGroup}
)
