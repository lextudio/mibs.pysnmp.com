# SNMP MIB module (RBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:30 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
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
 iso,
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 214)
)
rbridgeMIB.setRevisions(
        ("2013-01-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbridgeAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class RbridgeNickname(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )



# MIB Managed Objects in the order of their OIDs

_RbridgeNotifications_ObjectIdentity = ObjectIdentity
rbridgeNotifications = _RbridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 0)
)
_RbridgeObjects_ObjectIdentity = ObjectIdentity
rbridgeObjects = _RbridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1)
)
_RbridgeBase_ObjectIdentity = ObjectIdentity
rbridgeBase = _RbridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 1)
)
_RbridgeBaseTrillVersion_Type = Unsigned32
_RbridgeBaseTrillVersion_Object = MibScalar
rbridgeBaseTrillVersion = _RbridgeBaseTrillVersion_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 1),
    _RbridgeBaseTrillVersion_Type()
)
rbridgeBaseTrillVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBaseTrillVersion.setStatus("current")
_RbridgeBaseNumPorts_Type = Unsigned32
_RbridgeBaseNumPorts_Object = MibScalar
rbridgeBaseNumPorts = _RbridgeBaseNumPorts_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 2),
    _RbridgeBaseNumPorts_Type()
)
rbridgeBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBaseNumPorts.setStatus("current")
if mibBuilder.loadTexts:
    rbridgeBaseNumPorts.setUnits("ports")


class _RbridgeBaseForwardDelay_Type(Unsigned32):
    """Custom type rbridgeBaseForwardDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_RbridgeBaseForwardDelay_Type.__name__ = "Unsigned32"
_RbridgeBaseForwardDelay_Object = MibScalar
rbridgeBaseForwardDelay = _RbridgeBaseForwardDelay_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 3),
    _RbridgeBaseForwardDelay_Type()
)
rbridgeBaseForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBaseForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    rbridgeBaseForwardDelay.setUnits("seconds")
_RbridgeBaseUniMultipathEnable_Type = TruthValue
_RbridgeBaseUniMultipathEnable_Object = MibScalar
rbridgeBaseUniMultipathEnable = _RbridgeBaseUniMultipathEnable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 4),
    _RbridgeBaseUniMultipathEnable_Type()
)
rbridgeBaseUniMultipathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBaseUniMultipathEnable.setStatus("current")
_RbridgeBaseMultiMultipathEnable_Type = TruthValue
_RbridgeBaseMultiMultipathEnable_Object = MibScalar
rbridgeBaseMultiMultipathEnable = _RbridgeBaseMultiMultipathEnable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 5),
    _RbridgeBaseMultiMultipathEnable_Type()
)
rbridgeBaseMultiMultipathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBaseMultiMultipathEnable.setStatus("current")
_RbridgeBaseAcceptEncapNonadj_Type = TruthValue
_RbridgeBaseAcceptEncapNonadj_Object = MibScalar
rbridgeBaseAcceptEncapNonadj = _RbridgeBaseAcceptEncapNonadj_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 6),
    _RbridgeBaseAcceptEncapNonadj_Type()
)
rbridgeBaseAcceptEncapNonadj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBaseAcceptEncapNonadj.setStatus("current")


class _RbridgeBaseNicknameNumber_Type(Unsigned32):
    """Custom type rbridgeBaseNicknameNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RbridgeBaseNicknameNumber_Type.__name__ = "Unsigned32"
_RbridgeBaseNicknameNumber_Object = MibScalar
rbridgeBaseNicknameNumber = _RbridgeBaseNicknameNumber_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 7),
    _RbridgeBaseNicknameNumber_Type()
)
rbridgeBaseNicknameNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBaseNicknameNumber.setStatus("current")
_RbridgeBaseNicknameTable_Object = MibTable
rbridgeBaseNicknameTable = _RbridgeBaseNicknameTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rbridgeBaseNicknameTable.setStatus("current")
_RbridgeBaseNicknameEntry_Object = MibTableRow
rbridgeBaseNicknameEntry = _RbridgeBaseNicknameEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1)
)
rbridgeBaseNicknameEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeBaseNicknameName"),
)
if mibBuilder.loadTexts:
    rbridgeBaseNicknameEntry.setStatus("current")
_RbridgeBaseNicknameName_Type = RbridgeNickname
_RbridgeBaseNicknameName_Object = MibTableColumn
rbridgeBaseNicknameName = _RbridgeBaseNicknameName_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1, 1),
    _RbridgeBaseNicknameName_Type()
)
rbridgeBaseNicknameName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeBaseNicknameName.setStatus("current")


class _RbridgeBaseNicknamePriority_Type(Unsigned32):
    """Custom type rbridgeBaseNicknamePriority based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeBaseNicknamePriority_Type.__name__ = "Unsigned32"
_RbridgeBaseNicknamePriority_Object = MibTableColumn
rbridgeBaseNicknamePriority = _RbridgeBaseNicknamePriority_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1, 2),
    _RbridgeBaseNicknamePriority_Type()
)
rbridgeBaseNicknamePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeBaseNicknamePriority.setStatus("current")


class _RbridgeBaseNicknameDtrPriority_Type(Unsigned32):
    """Custom type rbridgeBaseNicknameDtrPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbridgeBaseNicknameDtrPriority_Type.__name__ = "Unsigned32"
_RbridgeBaseNicknameDtrPriority_Object = MibTableColumn
rbridgeBaseNicknameDtrPriority = _RbridgeBaseNicknameDtrPriority_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1, 3),
    _RbridgeBaseNicknameDtrPriority_Type()
)
rbridgeBaseNicknameDtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeBaseNicknameDtrPriority.setStatus("current")


class _RbridgeBaseNicknameType_Type(Integer32):
    """Custom type rbridgeBaseNicknameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RbridgeBaseNicknameType_Type.__name__ = "Integer32"
_RbridgeBaseNicknameType_Object = MibTableColumn
rbridgeBaseNicknameType = _RbridgeBaseNicknameType_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1, 4),
    _RbridgeBaseNicknameType_Type()
)
rbridgeBaseNicknameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBaseNicknameType.setStatus("current")
_RbridgeBaseNicknameRowStatus_Type = RowStatus
_RbridgeBaseNicknameRowStatus_Object = MibTableColumn
rbridgeBaseNicknameRowStatus = _RbridgeBaseNicknameRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 8, 1, 5),
    _RbridgeBaseNicknameRowStatus_Type()
)
rbridgeBaseNicknameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeBaseNicknameRowStatus.setStatus("current")
_RbridgeBasePortTable_Object = MibTable
rbridgeBasePortTable = _RbridgeBasePortTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rbridgeBasePortTable.setStatus("current")
_RbridgeBasePortEntry_Object = MibTableRow
rbridgeBasePortEntry = _RbridgeBasePortEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1)
)
rbridgeBasePortEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeBasePort"),
)
if mibBuilder.loadTexts:
    rbridgeBasePortEntry.setStatus("current")


class _RbridgeBasePort_Type(Unsigned32):
    """Custom type rbridgeBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbridgeBasePort_Type.__name__ = "Unsigned32"
_RbridgeBasePort_Object = MibTableColumn
rbridgeBasePort = _RbridgeBasePort_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 1),
    _RbridgeBasePort_Type()
)
rbridgeBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeBasePort.setStatus("current")
_RbridgeBasePortIfIndex_Type = InterfaceIndex
_RbridgeBasePortIfIndex_Object = MibTableColumn
rbridgeBasePortIfIndex = _RbridgeBasePortIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 2),
    _RbridgeBasePortIfIndex_Type()
)
rbridgeBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBasePortIfIndex.setStatus("current")


class _RbridgeBasePortDisable_Type(TruthValue):
    """Custom type rbridgeBasePortDisable based on TruthValue"""


_RbridgeBasePortDisable_Object = MibTableColumn
rbridgeBasePortDisable = _RbridgeBasePortDisable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 3),
    _RbridgeBasePortDisable_Type()
)
rbridgeBasePortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortDisable.setStatus("current")


class _RbridgeBasePortTrunkPort_Type(TruthValue):
    """Custom type rbridgeBasePortTrunkPort based on TruthValue"""


_RbridgeBasePortTrunkPort_Object = MibTableColumn
rbridgeBasePortTrunkPort = _RbridgeBasePortTrunkPort_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 4),
    _RbridgeBasePortTrunkPort_Type()
)
rbridgeBasePortTrunkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortTrunkPort.setStatus("current")


class _RbridgeBasePortAccessPort_Type(TruthValue):
    """Custom type rbridgeBasePortAccessPort based on TruthValue"""


_RbridgeBasePortAccessPort_Object = MibTableColumn
rbridgeBasePortAccessPort = _RbridgeBasePortAccessPort_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 5),
    _RbridgeBasePortAccessPort_Type()
)
rbridgeBasePortAccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortAccessPort.setStatus("current")


class _RbridgeBasePortP2pHellos_Type(TruthValue):
    """Custom type rbridgeBasePortP2pHellos based on TruthValue"""


_RbridgeBasePortP2pHellos_Object = MibTableColumn
rbridgeBasePortP2pHellos = _RbridgeBasePortP2pHellos_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 6),
    _RbridgeBasePortP2pHellos_Type()
)
rbridgeBasePortP2pHellos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortP2pHellos.setStatus("current")


class _RbridgeBasePortState_Type(Integer32):
    """Custom type rbridgeBasePortState based on Integer32"""
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
        *(("broken", 5),
          ("disabled", 4),
          ("portInhibited", 2),
          ("uninhibited", 1),
          ("vlanInhibited", 3))
    )


_RbridgeBasePortState_Type.__name__ = "Integer32"
_RbridgeBasePortState_Object = MibTableColumn
rbridgeBasePortState = _RbridgeBasePortState_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 7),
    _RbridgeBasePortState_Type()
)
rbridgeBasePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBasePortState.setStatus("current")


class _RbridgeBasePortInhibitionTime_Type(Unsigned32):
    """Custom type rbridgeBasePortInhibitionTime based on Unsigned32"""
    defaultValue = 30


_RbridgeBasePortInhibitionTime_Object = MibTableColumn
rbridgeBasePortInhibitionTime = _RbridgeBasePortInhibitionTime_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 8),
    _RbridgeBasePortInhibitionTime_Type()
)
rbridgeBasePortInhibitionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortInhibitionTime.setStatus("current")
if mibBuilder.loadTexts:
    rbridgeBasePortInhibitionTime.setUnits("seconds")


class _RbridgeBasePortDisableLearning_Type(TruthValue):
    """Custom type rbridgeBasePortDisableLearning based on TruthValue"""


_RbridgeBasePortDisableLearning_Object = MibTableColumn
rbridgeBasePortDisableLearning = _RbridgeBasePortDisableLearning_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 9),
    _RbridgeBasePortDisableLearning_Type()
)
rbridgeBasePortDisableLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortDisableLearning.setStatus("current")
_RbridgeBasePortDesiredDesigVlan_Type = VlanId
_RbridgeBasePortDesiredDesigVlan_Object = MibTableColumn
rbridgeBasePortDesiredDesigVlan = _RbridgeBasePortDesiredDesigVlan_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 10),
    _RbridgeBasePortDesiredDesigVlan_Type()
)
rbridgeBasePortDesiredDesigVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortDesiredDesigVlan.setStatus("current")
_RbridgeBasePortDesigVlan_Type = VlanId
_RbridgeBasePortDesigVlan_Object = MibTableColumn
rbridgeBasePortDesigVlan = _RbridgeBasePortDesigVlan_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 11),
    _RbridgeBasePortDesigVlan_Type()
)
rbridgeBasePortDesigVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBasePortDesigVlan.setStatus("current")
_RbridgeBasePortStpRoot_Type = BridgeId
_RbridgeBasePortStpRoot_Object = MibTableColumn
rbridgeBasePortStpRoot = _RbridgeBasePortStpRoot_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 12),
    _RbridgeBasePortStpRoot_Type()
)
rbridgeBasePortStpRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBasePortStpRoot.setStatus("current")
_RbridgeBasePortStpRootChanges_Type = Counter32
_RbridgeBasePortStpRootChanges_Object = MibTableColumn
rbridgeBasePortStpRootChanges = _RbridgeBasePortStpRootChanges_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 13),
    _RbridgeBasePortStpRootChanges_Type()
)
rbridgeBasePortStpRootChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeBasePortStpRootChanges.setStatus("current")
if mibBuilder.loadTexts:
    rbridgeBasePortStpRootChanges.setUnits("changes")
_RbridgeBasePortStpWiringCloset_Type = BridgeId
_RbridgeBasePortStpWiringCloset_Object = MibTableColumn
rbridgeBasePortStpWiringCloset = _RbridgeBasePortStpWiringCloset_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 1, 9, 1, 14),
    _RbridgeBasePortStpWiringCloset_Type()
)
rbridgeBasePortStpWiringCloset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeBasePortStpWiringCloset.setStatus("current")
_RbridgeFdb_ObjectIdentity = ObjectIdentity
rbridgeFdb = _RbridgeFdb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 2)
)


class _RbridgeConfidenceNative_Type(Unsigned32):
    """Custom type rbridgeConfidenceNative based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeConfidenceNative_Type.__name__ = "Unsigned32"
_RbridgeConfidenceNative_Object = MibScalar
rbridgeConfidenceNative = _RbridgeConfidenceNative_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 1),
    _RbridgeConfidenceNative_Type()
)
rbridgeConfidenceNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeConfidenceNative.setStatus("current")


class _RbridgeConfidenceDecap_Type(Unsigned32):
    """Custom type rbridgeConfidenceDecap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeConfidenceDecap_Type.__name__ = "Unsigned32"
_RbridgeConfidenceDecap_Object = MibScalar
rbridgeConfidenceDecap = _RbridgeConfidenceDecap_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 2),
    _RbridgeConfidenceDecap_Type()
)
rbridgeConfidenceDecap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeConfidenceDecap.setStatus("current")


class _RbridgeConfidenceStatic_Type(Unsigned32):
    """Custom type rbridgeConfidenceStatic based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeConfidenceStatic_Type.__name__ = "Unsigned32"
_RbridgeConfidenceStatic_Object = MibScalar
rbridgeConfidenceStatic = _RbridgeConfidenceStatic_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 3),
    _RbridgeConfidenceStatic_Type()
)
rbridgeConfidenceStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeConfidenceStatic.setStatus("current")
_RbridgeUniFdbTable_Object = MibTable
rbridgeUniFdbTable = _RbridgeUniFdbTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rbridgeUniFdbTable.setStatus("current")
_RbridgeUniFdbEntry_Object = MibTableRow
rbridgeUniFdbEntry = _RbridgeUniFdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1)
)
rbridgeUniFdbEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeFdbId"),
    (0, "RBRIDGE-MIB", "rbridgeUniFdbAddr"),
)
if mibBuilder.loadTexts:
    rbridgeUniFdbEntry.setStatus("current")


class _RbridgeFdbId_Type(Unsigned32):
    """Custom type rbridgeFdbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbridgeFdbId_Type.__name__ = "Unsigned32"
_RbridgeFdbId_Object = MibTableColumn
rbridgeFdbId = _RbridgeFdbId_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 1),
    _RbridgeFdbId_Type()
)
rbridgeFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeFdbId.setStatus("current")
_RbridgeUniFdbAddr_Type = MacAddress
_RbridgeUniFdbAddr_Object = MibTableColumn
rbridgeUniFdbAddr = _RbridgeUniFdbAddr_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 2),
    _RbridgeUniFdbAddr_Type()
)
rbridgeUniFdbAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeUniFdbAddr.setStatus("current")


class _RbridgeUniFdbPort_Type(Unsigned32):
    """Custom type rbridgeUniFdbPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbridgeUniFdbPort_Type.__name__ = "Unsigned32"
_RbridgeUniFdbPort_Object = MibTableColumn
rbridgeUniFdbPort = _RbridgeUniFdbPort_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 3),
    _RbridgeUniFdbPort_Type()
)
rbridgeUniFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeUniFdbPort.setStatus("current")
_RbridgeUniFdbNickname_Type = RbridgeNickname
_RbridgeUniFdbNickname_Object = MibTableColumn
rbridgeUniFdbNickname = _RbridgeUniFdbNickname_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 4),
    _RbridgeUniFdbNickname_Type()
)
rbridgeUniFdbNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeUniFdbNickname.setStatus("current")


class _RbridgeUniFdbConfidence_Type(Unsigned32):
    """Custom type rbridgeUniFdbConfidence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeUniFdbConfidence_Type.__name__ = "Unsigned32"
_RbridgeUniFdbConfidence_Object = MibTableColumn
rbridgeUniFdbConfidence = _RbridgeUniFdbConfidence_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 5),
    _RbridgeUniFdbConfidence_Type()
)
rbridgeUniFdbConfidence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeUniFdbConfidence.setStatus("current")


class _RbridgeUniFdbStatus_Type(Integer32):
    """Custom type rbridgeUniFdbStatus based on Integer32"""
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
        *(("esadi", 6),
          ("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_RbridgeUniFdbStatus_Type.__name__ = "Integer32"
_RbridgeUniFdbStatus_Object = MibTableColumn
rbridgeUniFdbStatus = _RbridgeUniFdbStatus_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 4, 1, 6),
    _RbridgeUniFdbStatus_Type()
)
rbridgeUniFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeUniFdbStatus.setStatus("current")
_RbridgeUniFibTable_Object = MibTable
rbridgeUniFibTable = _RbridgeUniFibTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rbridgeUniFibTable.setStatus("current")
_RbridgeUniFibEntry_Object = MibTableRow
rbridgeUniFibEntry = _RbridgeUniFibEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5, 1)
)
rbridgeUniFibEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeUniFibNickname"),
    (0, "RBRIDGE-MIB", "rbridgeUniFibPort"),
    (0, "RBRIDGE-MIB", "rbridgeUniFibNextHop"),
)
if mibBuilder.loadTexts:
    rbridgeUniFibEntry.setStatus("current")
_RbridgeUniFibNickname_Type = RbridgeNickname
_RbridgeUniFibNickname_Object = MibTableColumn
rbridgeUniFibNickname = _RbridgeUniFibNickname_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5, 1, 1),
    _RbridgeUniFibNickname_Type()
)
rbridgeUniFibNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeUniFibNickname.setStatus("current")


class _RbridgeUniFibPort_Type(Unsigned32):
    """Custom type rbridgeUniFibPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbridgeUniFibPort_Type.__name__ = "Unsigned32"
_RbridgeUniFibPort_Object = MibTableColumn
rbridgeUniFibPort = _RbridgeUniFibPort_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5, 1, 2),
    _RbridgeUniFibPort_Type()
)
rbridgeUniFibPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeUniFibPort.setStatus("current")
_RbridgeUniFibNextHop_Type = RbridgeNickname
_RbridgeUniFibNextHop_Object = MibTableColumn
rbridgeUniFibNextHop = _RbridgeUniFibNextHop_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5, 1, 3),
    _RbridgeUniFibNextHop_Type()
)
rbridgeUniFibNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeUniFibNextHop.setStatus("current")
_RbridgeUniFibHopCount_Type = Unsigned32
_RbridgeUniFibHopCount_Object = MibTableColumn
rbridgeUniFibHopCount = _RbridgeUniFibHopCount_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 5, 1, 4),
    _RbridgeUniFibHopCount_Type()
)
rbridgeUniFibHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeUniFibHopCount.setStatus("current")
_RbridgeMultiFibTable_Object = MibTable
rbridgeMultiFibTable = _RbridgeMultiFibTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rbridgeMultiFibTable.setStatus("current")
_RbridgeMultiFibEntry_Object = MibTableRow
rbridgeMultiFibEntry = _RbridgeMultiFibEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 6, 1)
)
rbridgeMultiFibEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeMultiFibNickname"),
)
if mibBuilder.loadTexts:
    rbridgeMultiFibEntry.setStatus("current")
_RbridgeMultiFibNickname_Type = RbridgeNickname
_RbridgeMultiFibNickname_Object = MibTableColumn
rbridgeMultiFibNickname = _RbridgeMultiFibNickname_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 6, 1, 1),
    _RbridgeMultiFibNickname_Type()
)
rbridgeMultiFibNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeMultiFibNickname.setStatus("current")
_RbridgeMultiFibPorts_Type = PortList
_RbridgeMultiFibPorts_Object = MibTableColumn
rbridgeMultiFibPorts = _RbridgeMultiFibPorts_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 2, 6, 1, 2),
    _RbridgeMultiFibPorts_Type()
)
rbridgeMultiFibPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeMultiFibPorts.setStatus("current")
_RbridgeVlan_ObjectIdentity = ObjectIdentity
rbridgeVlan = _RbridgeVlan_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 3)
)
_RbridgeVlanTable_Object = MibTable
rbridgeVlanTable = _RbridgeVlanTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbridgeVlanTable.setStatus("current")
_RbridgeVlanEntry_Object = MibTableRow
rbridgeVlanEntry = _RbridgeVlanEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1, 1)
)
rbridgeVlanEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    rbridgeVlanEntry.setStatus("current")


class _RbridgeVlanIndex_Type(Unsigned32):
    """Custom type rbridgeVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4096, 4294967295),
    )


_RbridgeVlanIndex_Type.__name__ = "Unsigned32"
_RbridgeVlanIndex_Object = MibTableColumn
rbridgeVlanIndex = _RbridgeVlanIndex_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1, 1, 1),
    _RbridgeVlanIndex_Type()
)
rbridgeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeVlanIndex.setStatus("current")
_RbridgeVlanForwarderLosts_Type = Counter32
_RbridgeVlanForwarderLosts_Object = MibTableColumn
rbridgeVlanForwarderLosts = _RbridgeVlanForwarderLosts_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1, 1, 2),
    _RbridgeVlanForwarderLosts_Type()
)
rbridgeVlanForwarderLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeVlanForwarderLosts.setStatus("current")
if mibBuilder.loadTexts:
    rbridgeVlanForwarderLosts.setUnits("times")


class _RbridgeVlanDisableLearning_Type(TruthValue):
    """Custom type rbridgeVlanDisableLearning based on TruthValue"""


_RbridgeVlanDisableLearning_Object = MibTableColumn
rbridgeVlanDisableLearning = _RbridgeVlanDisableLearning_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1, 1, 3),
    _RbridgeVlanDisableLearning_Type()
)
rbridgeVlanDisableLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeVlanDisableLearning.setStatus("current")


class _RbridgeVlanSnooping_Type(Integer32):
    """Custom type rbridgeVlanSnooping based on Integer32"""
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
        *(("ipv4", 2),
          ("ipv4v6", 4),
          ("ipv6", 3),
          ("notSupported", 1))
    )


_RbridgeVlanSnooping_Type.__name__ = "Integer32"
_RbridgeVlanSnooping_Object = MibTableColumn
rbridgeVlanSnooping = _RbridgeVlanSnooping_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 1, 1, 4),
    _RbridgeVlanSnooping_Type()
)
rbridgeVlanSnooping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeVlanSnooping.setStatus("current")
_RbridgeVlanPortTable_Object = MibTable
rbridgeVlanPortTable = _RbridgeVlanPortTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rbridgeVlanPortTable.setStatus("current")
_RbridgeVlanPortEntry_Object = MibTableRow
rbridgeVlanPortEntry = _RbridgeVlanPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2, 1)
)
rbridgeVlanPortEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeBasePort"),
    (0, "RBRIDGE-MIB", "rbridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    rbridgeVlanPortEntry.setStatus("current")
_RbridgeVlanPortInhibited_Type = TruthValue
_RbridgeVlanPortInhibited_Object = MibTableColumn
rbridgeVlanPortInhibited = _RbridgeVlanPortInhibited_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2, 1, 1),
    _RbridgeVlanPortInhibited_Type()
)
rbridgeVlanPortInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeVlanPortInhibited.setStatus("current")
_RbridgeVlanPortForwarder_Type = TruthValue
_RbridgeVlanPortForwarder_Object = MibTableColumn
rbridgeVlanPortForwarder = _RbridgeVlanPortForwarder_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2, 1, 2),
    _RbridgeVlanPortForwarder_Type()
)
rbridgeVlanPortForwarder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeVlanPortForwarder.setStatus("current")


class _RbridgeVlanPortAnnouncing_Type(TruthValue):
    """Custom type rbridgeVlanPortAnnouncing based on TruthValue"""


_RbridgeVlanPortAnnouncing_Object = MibTableColumn
rbridgeVlanPortAnnouncing = _RbridgeVlanPortAnnouncing_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2, 1, 3),
    _RbridgeVlanPortAnnouncing_Type()
)
rbridgeVlanPortAnnouncing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeVlanPortAnnouncing.setStatus("current")
_RbridgeVlanPortDetectedVlanMapping_Type = TruthValue
_RbridgeVlanPortDetectedVlanMapping_Object = MibTableColumn
rbridgeVlanPortDetectedVlanMapping = _RbridgeVlanPortDetectedVlanMapping_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 3, 2, 1, 4),
    _RbridgeVlanPortDetectedVlanMapping_Type()
)
rbridgeVlanPortDetectedVlanMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeVlanPortDetectedVlanMapping.setStatus("current")
_RbridgeEsadi_ObjectIdentity = ObjectIdentity
rbridgeEsadi = _RbridgeEsadi_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 4)
)
_RbridgeEsadiTable_Object = MibTable
rbridgeEsadiTable = _RbridgeEsadiTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rbridgeEsadiTable.setStatus("current")
_RbridgeEsadiEntry_Object = MibTableRow
rbridgeEsadiEntry = _RbridgeEsadiEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1)
)
rbridgeEsadiEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    rbridgeEsadiEntry.setStatus("current")


class _RbridgeEsadiEnable_Type(TruthValue):
    """Custom type rbridgeEsadiEnable based on TruthValue"""


_RbridgeEsadiEnable_Object = MibTableColumn
rbridgeEsadiEnable = _RbridgeEsadiEnable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 1),
    _RbridgeEsadiEnable_Type()
)
rbridgeEsadiEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeEsadiEnable.setStatus("current")


class _RbridgeEsadiConfidence_Type(Unsigned32):
    """Custom type rbridgeEsadiConfidence based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbridgeEsadiConfidence_Type.__name__ = "Unsigned32"
_RbridgeEsadiConfidence_Object = MibTableColumn
rbridgeEsadiConfidence = _RbridgeEsadiConfidence_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 2),
    _RbridgeEsadiConfidence_Type()
)
rbridgeEsadiConfidence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeEsadiConfidence.setStatus("current")


class _RbridgeEsadiDrbPriority_Type(Unsigned32):
    """Custom type rbridgeEsadiDrbPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RbridgeEsadiDrbPriority_Type.__name__ = "Unsigned32"
_RbridgeEsadiDrbPriority_Object = MibTableColumn
rbridgeEsadiDrbPriority = _RbridgeEsadiDrbPriority_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 3),
    _RbridgeEsadiDrbPriority_Type()
)
rbridgeEsadiDrbPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeEsadiDrbPriority.setStatus("current")
_RbridgeEsadiDrb_Type = RbridgeAddress
_RbridgeEsadiDrb_Object = MibTableColumn
rbridgeEsadiDrb = _RbridgeEsadiDrb_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 4),
    _RbridgeEsadiDrb_Type()
)
rbridgeEsadiDrb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeEsadiDrb.setStatus("current")


class _RbridgeEsadiDrbHoldingTime_Type(Unsigned32):
    """Custom type rbridgeEsadiDrbHoldingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RbridgeEsadiDrbHoldingTime_Type.__name__ = "Unsigned32"
_RbridgeEsadiDrbHoldingTime_Object = MibTableColumn
rbridgeEsadiDrbHoldingTime = _RbridgeEsadiDrbHoldingTime_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 5),
    _RbridgeEsadiDrbHoldingTime_Type()
)
rbridgeEsadiDrbHoldingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeEsadiDrbHoldingTime.setStatus("current")
_RbridgeEsadiRowStatus_Type = RowStatus
_RbridgeEsadiRowStatus_Object = MibTableColumn
rbridgeEsadiRowStatus = _RbridgeEsadiRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 4, 1, 1, 6),
    _RbridgeEsadiRowStatus_Type()
)
rbridgeEsadiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbridgeEsadiRowStatus.setStatus("current")
_RbridgeCounter_ObjectIdentity = ObjectIdentity
rbridgeCounter = _RbridgeCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 5)
)
_RbridgePortCounterTable_Object = MibTable
rbridgePortCounterTable = _RbridgePortCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rbridgePortCounterTable.setStatus("current")
_RbridgePortCounterEntry_Object = MibTableRow
rbridgePortCounterEntry = _RbridgePortCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1)
)
rbridgePortCounterEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeBasePort"),
)
if mibBuilder.loadTexts:
    rbridgePortCounterEntry.setStatus("current")
_RbridgePortRpfCheckFails_Type = Counter32
_RbridgePortRpfCheckFails_Object = MibTableColumn
rbridgePortRpfCheckFails = _RbridgePortRpfCheckFails_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1, 1),
    _RbridgePortRpfCheckFails_Type()
)
rbridgePortRpfCheckFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgePortRpfCheckFails.setStatus("current")
if mibBuilder.loadTexts:
    rbridgePortRpfCheckFails.setUnits("frames")
_RbridgePortHopCountExceeds_Type = Counter32
_RbridgePortHopCountExceeds_Object = MibTableColumn
rbridgePortHopCountExceeds = _RbridgePortHopCountExceeds_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1, 2),
    _RbridgePortHopCountExceeds_Type()
)
rbridgePortHopCountExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgePortHopCountExceeds.setStatus("current")
if mibBuilder.loadTexts:
    rbridgePortHopCountExceeds.setUnits("frames")
_RbridgePortOptionDrops_Type = Counter32
_RbridgePortOptionDrops_Object = MibTableColumn
rbridgePortOptionDrops = _RbridgePortOptionDrops_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1, 3),
    _RbridgePortOptionDrops_Type()
)
rbridgePortOptionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgePortOptionDrops.setStatus("current")
if mibBuilder.loadTexts:
    rbridgePortOptionDrops.setUnits("frames")
_RbridgePortTrillInFrames_Type = Counter64
_RbridgePortTrillInFrames_Object = MibTableColumn
rbridgePortTrillInFrames = _RbridgePortTrillInFrames_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1, 4),
    _RbridgePortTrillInFrames_Type()
)
rbridgePortTrillInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgePortTrillInFrames.setStatus("current")
if mibBuilder.loadTexts:
    rbridgePortTrillInFrames.setUnits("frames")
_RbridgePortTrillOutFrames_Type = Counter64
_RbridgePortTrillOutFrames_Object = MibTableColumn
rbridgePortTrillOutFrames = _RbridgePortTrillOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 5, 1, 1, 5),
    _RbridgePortTrillOutFrames_Type()
)
rbridgePortTrillOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgePortTrillOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    rbridgePortTrillOutFrames.setUnits("frames")
_RbridgeSnooping_ObjectIdentity = ObjectIdentity
rbridgeSnooping = _RbridgeSnooping_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 6)
)
_RbridgeSnoopingPortTable_Object = MibTable
rbridgeSnoopingPortTable = _RbridgeSnoopingPortTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rbridgeSnoopingPortTable.setStatus("current")
_RbridgeSnoopingPortEntry_Object = MibTableRow
rbridgeSnoopingPortEntry = _RbridgeSnoopingPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 1, 1)
)
rbridgeSnoopingPortEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeBasePort"),
    (0, "RBRIDGE-MIB", "rbridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    rbridgeSnoopingPortEntry.setStatus("current")


class _RbridgeSnoopingPortAddrType_Type(Integer32):
    """Custom type rbridgeSnoopingPortAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4v6", 3),
          ("ipv6", 2))
    )


_RbridgeSnoopingPortAddrType_Type.__name__ = "Integer32"
_RbridgeSnoopingPortAddrType_Object = MibTableColumn
rbridgeSnoopingPortAddrType = _RbridgeSnoopingPortAddrType_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 1, 1, 1),
    _RbridgeSnoopingPortAddrType_Type()
)
rbridgeSnoopingPortAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeSnoopingPortAddrType.setStatus("current")
_RbridgeSnoopingAddrTable_Object = MibTable
rbridgeSnoopingAddrTable = _RbridgeSnoopingAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 2)
)
if mibBuilder.loadTexts:
    rbridgeSnoopingAddrTable.setStatus("current")
_RbridgeSnoopingAddrEntry_Object = MibTableRow
rbridgeSnoopingAddrEntry = _RbridgeSnoopingAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 2, 1)
)
rbridgeSnoopingAddrEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeVlanIndex"),
    (0, "RBRIDGE-MIB", "rbridgeSnoopingAddrType"),
    (0, "RBRIDGE-MIB", "rbridgeSnoopingAddr"),
)
if mibBuilder.loadTexts:
    rbridgeSnoopingAddrEntry.setStatus("current")
_RbridgeSnoopingAddrType_Type = InetAddressType
_RbridgeSnoopingAddrType_Object = MibTableColumn
rbridgeSnoopingAddrType = _RbridgeSnoopingAddrType_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 2, 1, 1),
    _RbridgeSnoopingAddrType_Type()
)
rbridgeSnoopingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeSnoopingAddrType.setStatus("current")
_RbridgeSnoopingAddr_Type = InetAddress
_RbridgeSnoopingAddr_Object = MibTableColumn
rbridgeSnoopingAddr = _RbridgeSnoopingAddr_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 2, 1, 2),
    _RbridgeSnoopingAddr_Type()
)
rbridgeSnoopingAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeSnoopingAddr.setStatus("current")
_RbridgeSnoopingAddrPorts_Type = PortList
_RbridgeSnoopingAddrPorts_Object = MibTableColumn
rbridgeSnoopingAddrPorts = _RbridgeSnoopingAddrPorts_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 6, 2, 1, 3),
    _RbridgeSnoopingAddrPorts_Type()
)
rbridgeSnoopingAddrPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeSnoopingAddrPorts.setStatus("current")
_RbridgeDtree_ObjectIdentity = ObjectIdentity
rbridgeDtree = _RbridgeDtree_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 7)
)


class _RbridgeDtreePriority_Type(Unsigned32):
    """Custom type rbridgeDtreePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbridgeDtreePriority_Type.__name__ = "Unsigned32"
_RbridgeDtreePriority_Object = MibScalar
rbridgeDtreePriority = _RbridgeDtreePriority_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 1),
    _RbridgeDtreePriority_Type()
)
rbridgeDtreePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeDtreePriority.setStatus("current")
_RbridgeDtreeActiveTrees_Type = Unsigned32
_RbridgeDtreeActiveTrees_Object = MibScalar
rbridgeDtreeActiveTrees = _RbridgeDtreeActiveTrees_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 2),
    _RbridgeDtreeActiveTrees_Type()
)
rbridgeDtreeActiveTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeDtreeActiveTrees.setStatus("current")
_RbridgeDtreeMaxTrees_Type = Unsigned32
_RbridgeDtreeMaxTrees_Object = MibScalar
rbridgeDtreeMaxTrees = _RbridgeDtreeMaxTrees_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 3),
    _RbridgeDtreeMaxTrees_Type()
)
rbridgeDtreeMaxTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeDtreeMaxTrees.setStatus("current")
_RbridgeDtreeDesiredUseTrees_Type = Unsigned32
_RbridgeDtreeDesiredUseTrees_Object = MibScalar
rbridgeDtreeDesiredUseTrees = _RbridgeDtreeDesiredUseTrees_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 4),
    _RbridgeDtreeDesiredUseTrees_Type()
)
rbridgeDtreeDesiredUseTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeDtreeDesiredUseTrees.setStatus("current")
_RbridgeDtreeTable_Object = MibTable
rbridgeDtreeTable = _RbridgeDtreeTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 5)
)
if mibBuilder.loadTexts:
    rbridgeDtreeTable.setStatus("current")
_RbridgeDtreeEntry_Object = MibTableRow
rbridgeDtreeEntry = _RbridgeDtreeEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 5, 1)
)
rbridgeDtreeEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeDtreeNumber"),
)
if mibBuilder.loadTexts:
    rbridgeDtreeEntry.setStatus("current")


class _RbridgeDtreeNumber_Type(Unsigned32):
    """Custom type rbridgeDtreeNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbridgeDtreeNumber_Type.__name__ = "Unsigned32"
_RbridgeDtreeNumber_Object = MibTableColumn
rbridgeDtreeNumber = _RbridgeDtreeNumber_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 5, 1, 1),
    _RbridgeDtreeNumber_Type()
)
rbridgeDtreeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeDtreeNumber.setStatus("current")
_RbridgeDtreeNickname_Type = RbridgeNickname
_RbridgeDtreeNickname_Object = MibTableColumn
rbridgeDtreeNickname = _RbridgeDtreeNickname_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 5, 1, 2),
    _RbridgeDtreeNickname_Type()
)
rbridgeDtreeNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeDtreeNickname.setStatus("current")
_RbridgeDtreeIngress_Type = TruthValue
_RbridgeDtreeIngress_Object = MibTableColumn
rbridgeDtreeIngress = _RbridgeDtreeIngress_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 7, 5, 1, 3),
    _RbridgeDtreeIngress_Type()
)
rbridgeDtreeIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeDtreeIngress.setStatus("current")
_RbridgeTrill_ObjectIdentity = ObjectIdentity
rbridgeTrill = _RbridgeTrill_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 1, 8)
)
_RbridgeTrillMinMtuDesired_Type = Unsigned32
_RbridgeTrillMinMtuDesired_Object = MibScalar
rbridgeTrillMinMtuDesired = _RbridgeTrillMinMtuDesired_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 1),
    _RbridgeTrillMinMtuDesired_Type()
)
rbridgeTrillMinMtuDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeTrillMinMtuDesired.setStatus("current")
_RbridgeTrillSz_Type = Unsigned32
_RbridgeTrillSz_Object = MibScalar
rbridgeTrillSz = _RbridgeTrillSz_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 2),
    _RbridgeTrillSz_Type()
)
rbridgeTrillSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeTrillSz.setStatus("current")


class _RbridgeTrillMaxMtuProbes_Type(Unsigned32):
    """Custom type rbridgeTrillMaxMtuProbes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbridgeTrillMaxMtuProbes_Type.__name__ = "Unsigned32"
_RbridgeTrillMaxMtuProbes_Object = MibScalar
rbridgeTrillMaxMtuProbes = _RbridgeTrillMaxMtuProbes_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 3),
    _RbridgeTrillMaxMtuProbes_Type()
)
rbridgeTrillMaxMtuProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbridgeTrillMaxMtuProbes.setStatus("current")
_RbridgeTrillNbrTable_Object = MibTable
rbridgeTrillNbrTable = _RbridgeTrillNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 4)
)
if mibBuilder.loadTexts:
    rbridgeTrillNbrTable.setStatus("current")
_RbridgeTrillNbrEntry_Object = MibTableRow
rbridgeTrillNbrEntry = _RbridgeTrillNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 4, 1)
)
rbridgeTrillNbrEntry.setIndexNames(
    (0, "RBRIDGE-MIB", "rbridgeTrillNbrMacAddr"),
)
if mibBuilder.loadTexts:
    rbridgeTrillNbrEntry.setStatus("current")
_RbridgeTrillNbrMacAddr_Type = MacAddress
_RbridgeTrillNbrMacAddr_Object = MibTableColumn
rbridgeTrillNbrMacAddr = _RbridgeTrillNbrMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 4, 1, 1),
    _RbridgeTrillNbrMacAddr_Type()
)
rbridgeTrillNbrMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbridgeTrillNbrMacAddr.setStatus("current")
_RbridgeTrillNbrMtu_Type = Unsigned32
_RbridgeTrillNbrMtu_Object = MibTableColumn
rbridgeTrillNbrMtu = _RbridgeTrillNbrMtu_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 4, 1, 2),
    _RbridgeTrillNbrMtu_Type()
)
rbridgeTrillNbrMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeTrillNbrMtu.setStatus("current")
_RbridgeTrillNbrFailedMtuTest_Type = TruthValue
_RbridgeTrillNbrFailedMtuTest_Object = MibTableColumn
rbridgeTrillNbrFailedMtuTest = _RbridgeTrillNbrFailedMtuTest_Object(
    (1, 3, 6, 1, 2, 1, 214, 1, 8, 4, 1, 3),
    _RbridgeTrillNbrFailedMtuTest_Type()
)
rbridgeTrillNbrFailedMtuTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbridgeTrillNbrFailedMtuTest.setStatus("current")
_RbridgeConformance_ObjectIdentity = ObjectIdentity
rbridgeConformance = _RbridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 2)
)
_RbridgeCompliances_ObjectIdentity = ObjectIdentity
rbridgeCompliances = _RbridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 2, 1)
)
_RbridgeGroup_ObjectIdentity = ObjectIdentity
rbridgeGroup = _RbridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 214, 2, 2)
)

# Managed Objects groups

rbridgeBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 1)
)
rbridgeBaseGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeBaseTrillVersion"),
        ("RBRIDGE-MIB", "rbridgeBaseNumPorts"),
        ("RBRIDGE-MIB", "rbridgeBaseForwardDelay"),
        ("RBRIDGE-MIB", "rbridgeBaseUniMultipathEnable"),
        ("RBRIDGE-MIB", "rbridgeBaseMultiMultipathEnable"),
        ("RBRIDGE-MIB", "rbridgeBaseAcceptEncapNonadj"),
        ("RBRIDGE-MIB", "rbridgeBaseNicknameNumber"))
)
if mibBuilder.loadTexts:
    rbridgeBaseGroup.setStatus("current")

rbridgeBaseNicknameGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 2)
)
rbridgeBaseNicknameGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeBaseNicknamePriority"),
        ("RBRIDGE-MIB", "rbridgeBaseNicknameDtrPriority"),
        ("RBRIDGE-MIB", "rbridgeBaseNicknameType"),
        ("RBRIDGE-MIB", "rbridgeBaseNicknameRowStatus"))
)
if mibBuilder.loadTexts:
    rbridgeBaseNicknameGroup.setStatus("current")

rbridgeBasePortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 3)
)
rbridgeBasePortGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeBasePortIfIndex"),
        ("RBRIDGE-MIB", "rbridgeBasePortDisable"),
        ("RBRIDGE-MIB", "rbridgeBasePortTrunkPort"),
        ("RBRIDGE-MIB", "rbridgeBasePortAccessPort"),
        ("RBRIDGE-MIB", "rbridgeBasePortP2pHellos"),
        ("RBRIDGE-MIB", "rbridgeBasePortState"),
        ("RBRIDGE-MIB", "rbridgeBasePortDesiredDesigVlan"),
        ("RBRIDGE-MIB", "rbridgeBasePortDesigVlan"),
        ("RBRIDGE-MIB", "rbridgeBasePortInhibitionTime"),
        ("RBRIDGE-MIB", "rbridgeBasePortDisableLearning"),
        ("RBRIDGE-MIB", "rbridgeBasePortStpRoot"),
        ("RBRIDGE-MIB", "rbridgeBasePortStpRootChanges"),
        ("RBRIDGE-MIB", "rbridgeBasePortStpWiringCloset"))
)
if mibBuilder.loadTexts:
    rbridgeBasePortGroup.setStatus("current")

rbridgeFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 4)
)
rbridgeFdbGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeConfidenceNative"),
        ("RBRIDGE-MIB", "rbridgeConfidenceDecap"),
        ("RBRIDGE-MIB", "rbridgeConfidenceStatic"),
        ("RBRIDGE-MIB", "rbridgeUniFdbPort"),
        ("RBRIDGE-MIB", "rbridgeUniFdbNickname"),
        ("RBRIDGE-MIB", "rbridgeUniFdbConfidence"),
        ("RBRIDGE-MIB", "rbridgeUniFdbStatus"))
)
if mibBuilder.loadTexts:
    rbridgeFdbGroup.setStatus("current")

rbridgeFibGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 5)
)
rbridgeFibGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeUniFibHopCount"),
        ("RBRIDGE-MIB", "rbridgeMultiFibPorts"))
)
if mibBuilder.loadTexts:
    rbridgeFibGroup.setStatus("current")

rbridgeVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 6)
)
rbridgeVlanGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeVlanForwarderLosts"),
        ("RBRIDGE-MIB", "rbridgeVlanDisableLearning"),
        ("RBRIDGE-MIB", "rbridgeVlanSnooping"),
        ("RBRIDGE-MIB", "rbridgeVlanPortInhibited"),
        ("RBRIDGE-MIB", "rbridgeVlanPortForwarder"),
        ("RBRIDGE-MIB", "rbridgeVlanPortAnnouncing"),
        ("RBRIDGE-MIB", "rbridgeVlanPortDetectedVlanMapping"))
)
if mibBuilder.loadTexts:
    rbridgeVlanGroup.setStatus("current")

rbridgePortCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 7)
)
rbridgePortCounterGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgePortRpfCheckFails"),
        ("RBRIDGE-MIB", "rbridgePortHopCountExceeds"),
        ("RBRIDGE-MIB", "rbridgePortOptionDrops"),
        ("RBRIDGE-MIB", "rbridgePortTrillInFrames"),
        ("RBRIDGE-MIB", "rbridgePortTrillOutFrames"))
)
if mibBuilder.loadTexts:
    rbridgePortCounterGroup.setStatus("current")

rbridgeEsadiGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 8)
)
rbridgeEsadiGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeEsadiEnable"),
        ("RBRIDGE-MIB", "rbridgeEsadiConfidence"),
        ("RBRIDGE-MIB", "rbridgeEsadiDrbPriority"),
        ("RBRIDGE-MIB", "rbridgeEsadiDrb"),
        ("RBRIDGE-MIB", "rbridgeEsadiDrbHoldingTime"),
        ("RBRIDGE-MIB", "rbridgeEsadiRowStatus"))
)
if mibBuilder.loadTexts:
    rbridgeEsadiGroup.setStatus("current")

rbridgeSnoopingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 9)
)
rbridgeSnoopingGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeSnoopingPortAddrType"),
        ("RBRIDGE-MIB", "rbridgeSnoopingAddrPorts"))
)
if mibBuilder.loadTexts:
    rbridgeSnoopingGroup.setStatus("current")

rbridgeDtreeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 10)
)
rbridgeDtreeGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeDtreePriority"),
        ("RBRIDGE-MIB", "rbridgeDtreeActiveTrees"),
        ("RBRIDGE-MIB", "rbridgeDtreeMaxTrees"),
        ("RBRIDGE-MIB", "rbridgeDtreeDesiredUseTrees"),
        ("RBRIDGE-MIB", "rbridgeDtreeNickname"),
        ("RBRIDGE-MIB", "rbridgeDtreeIngress"))
)
if mibBuilder.loadTexts:
    rbridgeDtreeGroup.setStatus("current")

rbridgeTrillGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 11)
)
rbridgeTrillGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeTrillMinMtuDesired"),
        ("RBRIDGE-MIB", "rbridgeTrillSz"),
        ("RBRIDGE-MIB", "rbridgeTrillMaxMtuProbes"),
        ("RBRIDGE-MIB", "rbridgeTrillNbrMtu"),
        ("RBRIDGE-MIB", "rbridgeTrillNbrFailedMtuTest"))
)
if mibBuilder.loadTexts:
    rbridgeTrillGroup.setStatus("current")


# Notification objects

rbridgeBaseNewDrb = NotificationType(
    (1, 3, 6, 1, 2, 1, 214, 0, 1)
)
if mibBuilder.loadTexts:
    rbridgeBaseNewDrb.setStatus(
        "current"
    )

rbridgeBaseTopologyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 214, 0, 2)
)
if mibBuilder.loadTexts:
    rbridgeBaseTopologyChange.setStatus(
        "current"
    )


# Notifications groups

rbridgeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 214, 2, 2, 12)
)
rbridgeNotificationGroup.setObjects(
      *(("RBRIDGE-MIB", "rbridgeBaseNewDrb"),
        ("RBRIDGE-MIB", "rbridgeBaseTopologyChange"))
)
if mibBuilder.loadTexts:
    rbridgeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 214, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbridgeCompliance.setStatus(
        "current"
    )

rbridgeReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 214, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbridgeReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBRIDGE-MIB",
    **{"RbridgeAddress": RbridgeAddress,
       "RbridgeNickname": RbridgeNickname,
       "rbridgeMIB": rbridgeMIB,
       "rbridgeNotifications": rbridgeNotifications,
       "rbridgeBaseNewDrb": rbridgeBaseNewDrb,
       "rbridgeBaseTopologyChange": rbridgeBaseTopologyChange,
       "rbridgeObjects": rbridgeObjects,
       "rbridgeBase": rbridgeBase,
       "rbridgeBaseTrillVersion": rbridgeBaseTrillVersion,
       "rbridgeBaseNumPorts": rbridgeBaseNumPorts,
       "rbridgeBaseForwardDelay": rbridgeBaseForwardDelay,
       "rbridgeBaseUniMultipathEnable": rbridgeBaseUniMultipathEnable,
       "rbridgeBaseMultiMultipathEnable": rbridgeBaseMultiMultipathEnable,
       "rbridgeBaseAcceptEncapNonadj": rbridgeBaseAcceptEncapNonadj,
       "rbridgeBaseNicknameNumber": rbridgeBaseNicknameNumber,
       "rbridgeBaseNicknameTable": rbridgeBaseNicknameTable,
       "rbridgeBaseNicknameEntry": rbridgeBaseNicknameEntry,
       "rbridgeBaseNicknameName": rbridgeBaseNicknameName,
       "rbridgeBaseNicknamePriority": rbridgeBaseNicknamePriority,
       "rbridgeBaseNicknameDtrPriority": rbridgeBaseNicknameDtrPriority,
       "rbridgeBaseNicknameType": rbridgeBaseNicknameType,
       "rbridgeBaseNicknameRowStatus": rbridgeBaseNicknameRowStatus,
       "rbridgeBasePortTable": rbridgeBasePortTable,
       "rbridgeBasePortEntry": rbridgeBasePortEntry,
       "rbridgeBasePort": rbridgeBasePort,
       "rbridgeBasePortIfIndex": rbridgeBasePortIfIndex,
       "rbridgeBasePortDisable": rbridgeBasePortDisable,
       "rbridgeBasePortTrunkPort": rbridgeBasePortTrunkPort,
       "rbridgeBasePortAccessPort": rbridgeBasePortAccessPort,
       "rbridgeBasePortP2pHellos": rbridgeBasePortP2pHellos,
       "rbridgeBasePortState": rbridgeBasePortState,
       "rbridgeBasePortInhibitionTime": rbridgeBasePortInhibitionTime,
       "rbridgeBasePortDisableLearning": rbridgeBasePortDisableLearning,
       "rbridgeBasePortDesiredDesigVlan": rbridgeBasePortDesiredDesigVlan,
       "rbridgeBasePortDesigVlan": rbridgeBasePortDesigVlan,
       "rbridgeBasePortStpRoot": rbridgeBasePortStpRoot,
       "rbridgeBasePortStpRootChanges": rbridgeBasePortStpRootChanges,
       "rbridgeBasePortStpWiringCloset": rbridgeBasePortStpWiringCloset,
       "rbridgeFdb": rbridgeFdb,
       "rbridgeConfidenceNative": rbridgeConfidenceNative,
       "rbridgeConfidenceDecap": rbridgeConfidenceDecap,
       "rbridgeConfidenceStatic": rbridgeConfidenceStatic,
       "rbridgeUniFdbTable": rbridgeUniFdbTable,
       "rbridgeUniFdbEntry": rbridgeUniFdbEntry,
       "rbridgeFdbId": rbridgeFdbId,
       "rbridgeUniFdbAddr": rbridgeUniFdbAddr,
       "rbridgeUniFdbPort": rbridgeUniFdbPort,
       "rbridgeUniFdbNickname": rbridgeUniFdbNickname,
       "rbridgeUniFdbConfidence": rbridgeUniFdbConfidence,
       "rbridgeUniFdbStatus": rbridgeUniFdbStatus,
       "rbridgeUniFibTable": rbridgeUniFibTable,
       "rbridgeUniFibEntry": rbridgeUniFibEntry,
       "rbridgeUniFibNickname": rbridgeUniFibNickname,
       "rbridgeUniFibPort": rbridgeUniFibPort,
       "rbridgeUniFibNextHop": rbridgeUniFibNextHop,
       "rbridgeUniFibHopCount": rbridgeUniFibHopCount,
       "rbridgeMultiFibTable": rbridgeMultiFibTable,
       "rbridgeMultiFibEntry": rbridgeMultiFibEntry,
       "rbridgeMultiFibNickname": rbridgeMultiFibNickname,
       "rbridgeMultiFibPorts": rbridgeMultiFibPorts,
       "rbridgeVlan": rbridgeVlan,
       "rbridgeVlanTable": rbridgeVlanTable,
       "rbridgeVlanEntry": rbridgeVlanEntry,
       "rbridgeVlanIndex": rbridgeVlanIndex,
       "rbridgeVlanForwarderLosts": rbridgeVlanForwarderLosts,
       "rbridgeVlanDisableLearning": rbridgeVlanDisableLearning,
       "rbridgeVlanSnooping": rbridgeVlanSnooping,
       "rbridgeVlanPortTable": rbridgeVlanPortTable,
       "rbridgeVlanPortEntry": rbridgeVlanPortEntry,
       "rbridgeVlanPortInhibited": rbridgeVlanPortInhibited,
       "rbridgeVlanPortForwarder": rbridgeVlanPortForwarder,
       "rbridgeVlanPortAnnouncing": rbridgeVlanPortAnnouncing,
       "rbridgeVlanPortDetectedVlanMapping": rbridgeVlanPortDetectedVlanMapping,
       "rbridgeEsadi": rbridgeEsadi,
       "rbridgeEsadiTable": rbridgeEsadiTable,
       "rbridgeEsadiEntry": rbridgeEsadiEntry,
       "rbridgeEsadiEnable": rbridgeEsadiEnable,
       "rbridgeEsadiConfidence": rbridgeEsadiConfidence,
       "rbridgeEsadiDrbPriority": rbridgeEsadiDrbPriority,
       "rbridgeEsadiDrb": rbridgeEsadiDrb,
       "rbridgeEsadiDrbHoldingTime": rbridgeEsadiDrbHoldingTime,
       "rbridgeEsadiRowStatus": rbridgeEsadiRowStatus,
       "rbridgeCounter": rbridgeCounter,
       "rbridgePortCounterTable": rbridgePortCounterTable,
       "rbridgePortCounterEntry": rbridgePortCounterEntry,
       "rbridgePortRpfCheckFails": rbridgePortRpfCheckFails,
       "rbridgePortHopCountExceeds": rbridgePortHopCountExceeds,
       "rbridgePortOptionDrops": rbridgePortOptionDrops,
       "rbridgePortTrillInFrames": rbridgePortTrillInFrames,
       "rbridgePortTrillOutFrames": rbridgePortTrillOutFrames,
       "rbridgeSnooping": rbridgeSnooping,
       "rbridgeSnoopingPortTable": rbridgeSnoopingPortTable,
       "rbridgeSnoopingPortEntry": rbridgeSnoopingPortEntry,
       "rbridgeSnoopingPortAddrType": rbridgeSnoopingPortAddrType,
       "rbridgeSnoopingAddrTable": rbridgeSnoopingAddrTable,
       "rbridgeSnoopingAddrEntry": rbridgeSnoopingAddrEntry,
       "rbridgeSnoopingAddrType": rbridgeSnoopingAddrType,
       "rbridgeSnoopingAddr": rbridgeSnoopingAddr,
       "rbridgeSnoopingAddrPorts": rbridgeSnoopingAddrPorts,
       "rbridgeDtree": rbridgeDtree,
       "rbridgeDtreePriority": rbridgeDtreePriority,
       "rbridgeDtreeActiveTrees": rbridgeDtreeActiveTrees,
       "rbridgeDtreeMaxTrees": rbridgeDtreeMaxTrees,
       "rbridgeDtreeDesiredUseTrees": rbridgeDtreeDesiredUseTrees,
       "rbridgeDtreeTable": rbridgeDtreeTable,
       "rbridgeDtreeEntry": rbridgeDtreeEntry,
       "rbridgeDtreeNumber": rbridgeDtreeNumber,
       "rbridgeDtreeNickname": rbridgeDtreeNickname,
       "rbridgeDtreeIngress": rbridgeDtreeIngress,
       "rbridgeTrill": rbridgeTrill,
       "rbridgeTrillMinMtuDesired": rbridgeTrillMinMtuDesired,
       "rbridgeTrillSz": rbridgeTrillSz,
       "rbridgeTrillMaxMtuProbes": rbridgeTrillMaxMtuProbes,
       "rbridgeTrillNbrTable": rbridgeTrillNbrTable,
       "rbridgeTrillNbrEntry": rbridgeTrillNbrEntry,
       "rbridgeTrillNbrMacAddr": rbridgeTrillNbrMacAddr,
       "rbridgeTrillNbrMtu": rbridgeTrillNbrMtu,
       "rbridgeTrillNbrFailedMtuTest": rbridgeTrillNbrFailedMtuTest,
       "rbridgeConformance": rbridgeConformance,
       "rbridgeCompliances": rbridgeCompliances,
       "rbridgeCompliance": rbridgeCompliance,
       "rbridgeReadOnlyCompliance": rbridgeReadOnlyCompliance,
       "rbridgeGroup": rbridgeGroup,
       "rbridgeBaseGroup": rbridgeBaseGroup,
       "rbridgeBaseNicknameGroup": rbridgeBaseNicknameGroup,
       "rbridgeBasePortGroup": rbridgeBasePortGroup,
       "rbridgeFdbGroup": rbridgeFdbGroup,
       "rbridgeFibGroup": rbridgeFibGroup,
       "rbridgeVlanGroup": rbridgeVlanGroup,
       "rbridgePortCounterGroup": rbridgePortCounterGroup,
       "rbridgeEsadiGroup": rbridgeEsadiGroup,
       "rbridgeSnoopingGroup": rbridgeSnoopingGroup,
       "rbridgeDtreeGroup": rbridgeDtreeGroup,
       "rbridgeTrillGroup": rbridgeTrillGroup,
       "rbridgeNotificationGroup": rbridgeNotificationGroup}
)
