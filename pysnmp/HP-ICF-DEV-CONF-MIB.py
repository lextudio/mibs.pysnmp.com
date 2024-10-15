# SNMP MIB module (HP-ICF-DEV-CONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DEV-CONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:56 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpicfDevConf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126)
)
hpicfDevConf.setRevisions(
        ("2017-05-02 00:00",
         "2016-11-02 00:00",
         "2016-06-07 00:00",
         "2016-02-01 00:00",
         "2016-01-28 00:00",
         "2015-12-18 00:00",
         "2015-12-04 00:00",
         "2015-09-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpPartnerDeviceType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("arubaAccessPoint", 2),
          ("arubaBridgeRouter", 3),
          ("ciscoBridgeRouter", 5),
          ("ciscoPhone", 6),
          ("deviceIdentity", 8),
          ("hpBridgeRouter", 4),
          ("none", 1),
          ("scsWanCpe", 7))
    )



class HpPartnerDeviceTypeList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HpSwitchDevNotifications_ObjectIdentity = ObjectIdentity
hpSwitchDevNotifications = _HpSwitchDevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 0)
)
_HpSwitchDevScalar_ObjectIdentity = ObjectIdentity
hpSwitchDevScalar = _HpSwitchDevScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 1)
)
_HpSwitchDevGlobals_ObjectIdentity = ObjectIdentity
hpSwitchDevGlobals = _HpSwitchDevGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 2)
)
_HpSwitchDevConformance_ObjectIdentity = ObjectIdentity
hpSwitchDevConformance = _HpSwitchDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3)
)
_HpSwitchDevCompliances_ObjectIdentity = ObjectIdentity
hpSwitchDevCompliances = _HpSwitchDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1)
)
_HpSwitchDevConfigGroups_ObjectIdentity = ObjectIdentity
hpSwitchDevConfigGroups = _HpSwitchDevConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2)
)
_HpSwitchDevConfig_ObjectIdentity = ObjectIdentity
hpSwitchDevConfig = _HpSwitchDevConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4)
)
_HpSwitchDevProfTable_Object = MibTable
hpSwitchDevProfTable = _HpSwitchDevProfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1)
)
if mibBuilder.loadTexts:
    hpSwitchDevProfTable.setStatus("current")
_HpSwitchDevProfEntry_Object = MibTableRow
hpSwitchDevProfEntry = _HpSwitchDevProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1)
)
hpSwitchDevProfEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchProfIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchDevProfEntry.setStatus("current")


class _HpSwitchProfIndex_Type(Unsigned32):
    """Custom type hpSwitchProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchProfIndex_Type.__name__ = "Unsigned32"
_HpSwitchProfIndex_Object = MibTableColumn
hpSwitchProfIndex = _HpSwitchProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 1),
    _HpSwitchProfIndex_Type()
)
hpSwitchProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchProfIndex.setStatus("current")
_HpSwitchProfRowStatus_Type = RowStatus
_HpSwitchProfRowStatus_Object = MibTableColumn
hpSwitchProfRowStatus = _HpSwitchProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 2),
    _HpSwitchProfRowStatus_Type()
)
hpSwitchProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfRowStatus.setStatus("current")


class _HpSwitchProfName_Type(OctetString):
    """Custom type hpSwitchProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpSwitchProfName_Type.__name__ = "OctetString"
_HpSwitchProfName_Object = MibTableColumn
hpSwitchProfName = _HpSwitchProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 3),
    _HpSwitchProfName_Type()
)
hpSwitchProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfName.setStatus("current")


class _HpSwitchProfUntaggedVlanID_Type(Unsigned32):
    """Custom type hpSwitchProfUntaggedVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpSwitchProfUntaggedVlanID_Type.__name__ = "Unsigned32"
_HpSwitchProfUntaggedVlanID_Object = MibTableColumn
hpSwitchProfUntaggedVlanID = _HpSwitchProfUntaggedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 4),
    _HpSwitchProfUntaggedVlanID_Type()
)
hpSwitchProfUntaggedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfUntaggedVlanID.setStatus("current")
_HpSwitchProfTaggedVlanList_Type = VidList
_HpSwitchProfTaggedVlanList_Object = MibTableColumn
hpSwitchProfTaggedVlanList = _HpSwitchProfTaggedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 5),
    _HpSwitchProfTaggedVlanList_Type()
)
hpSwitchProfTaggedVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfTaggedVlanList.setStatus("current")


class _HpSwitchProfIngressBandwidth_Type(Unsigned32):
    """Custom type hpSwitchProfIngressBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchProfIngressBandwidth_Type.__name__ = "Unsigned32"
_HpSwitchProfIngressBandwidth_Object = MibTableColumn
hpSwitchProfIngressBandwidth = _HpSwitchProfIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 6),
    _HpSwitchProfIngressBandwidth_Type()
)
hpSwitchProfIngressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfIngressBandwidth.setStatus("current")


class _HpSwitchProfEgressBandwidth_Type(Unsigned32):
    """Custom type hpSwitchProfEgressBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchProfEgressBandwidth_Type.__name__ = "Unsigned32"
_HpSwitchProfEgressBandwidth_Object = MibTableColumn
hpSwitchProfEgressBandwidth = _HpSwitchProfEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 7),
    _HpSwitchProfEgressBandwidth_Type()
)
hpSwitchProfEgressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfEgressBandwidth.setStatus("current")


class _HpSwitchProfCosPriority_Type(Unsigned32):
    """Custom type hpSwitchProfCosPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchProfCosPriority_Type.__name__ = "Unsigned32"
_HpSwitchProfCosPriority_Object = MibTableColumn
hpSwitchProfCosPriority = _HpSwitchProfCosPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 8),
    _HpSwitchProfCosPriority_Type()
)
hpSwitchProfCosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfCosPriority.setStatus("current")


class _HpSwitchProfPortSpeed_Type(Integer32):
    """Custom type hpSwitchProfPortSpeed based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("auto1000Mbits", 9),
          ("auto1000or2500Mbits", 16),
          ("auto1000or2500or5000Mbits", 17),
          ("auto100Mbits", 8),
          ("auto10Gbits", 10),
          ("auto10Mbits", 7),
          ("auto10or100Mbits", 11),
          ("auto2500Mbits", 13),
          ("auto2500or5000Mbits", 15),
          ("auto40Gbits", 12),
          ("auto5000Mbits", 14),
          ("autoNeg", 5),
          ("fullDuplex1000Mbits", 6),
          ("fullDuplex100Mbits", 4),
          ("fullDuplex10Mbits", 3),
          ("halfDuplex100Mbits", 2),
          ("halfDuplex10Mbits", 1))
    )


_HpSwitchProfPortSpeed_Type.__name__ = "Integer32"
_HpSwitchProfPortSpeed_Object = MibTableColumn
hpSwitchProfPortSpeed = _HpSwitchProfPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 9),
    _HpSwitchProfPortSpeed_Type()
)
hpSwitchProfPortSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfPortSpeed.setStatus("current")
_HpSwitchProfPoeMaxPower_Type = Unsigned32
_HpSwitchProfPoeMaxPower_Object = MibTableColumn
hpSwitchProfPoeMaxPower = _HpSwitchProfPoeMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 10),
    _HpSwitchProfPoeMaxPower_Type()
)
hpSwitchProfPoeMaxPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfPoeMaxPower.setStatus("current")


class _HpSwitchProfPoePriority_Type(Integer32):
    """Custom type hpSwitchProfPoePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_HpSwitchProfPoePriority_Type.__name__ = "Integer32"
_HpSwitchProfPoePriority_Object = MibTableColumn
hpSwitchProfPoePriority = _HpSwitchProfPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 11),
    _HpSwitchProfPoePriority_Type()
)
hpSwitchProfPoePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfPoePriority.setStatus("current")


class _HpSwitchProfJumboFrameSupport_Type(Integer32):
    """Custom type hpSwitchProfJumboFrameSupport based on Integer32"""
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


_HpSwitchProfJumboFrameSupport_Type.__name__ = "Integer32"
_HpSwitchProfJumboFrameSupport_Object = MibTableColumn
hpSwitchProfJumboFrameSupport = _HpSwitchProfJumboFrameSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 12),
    _HpSwitchProfJumboFrameSupport_Type()
)
hpSwitchProfJumboFrameSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfJumboFrameSupport.setStatus("current")


class _HpSwitchProfTunneledNodeSupport_Type(TruthValue):
    """Custom type hpSwitchProfTunneledNodeSupport based on TruthValue"""


_HpSwitchProfTunneledNodeSupport_Object = MibTableColumn
hpSwitchProfTunneledNodeSupport = _HpSwitchProfTunneledNodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 13),
    _HpSwitchProfTunneledNodeSupport_Type()
)
hpSwitchProfTunneledNodeSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchProfTunneledNodeSupport.setStatus("current")
_HpSwitchDevAssociationTable_Object = MibTable
hpSwitchDevAssociationTable = _HpSwitchDevAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2)
)
if mibBuilder.loadTexts:
    hpSwitchDevAssociationTable.setStatus("deprecated")
_HpSwitchDevAssociationEntry_Object = MibTableRow
hpSwitchDevAssociationEntry = _HpSwitchDevAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1)
)
hpSwitchDevAssociationEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationType"),
)
if mibBuilder.loadTexts:
    hpSwitchDevAssociationEntry.setStatus("deprecated")
_HpSwitchDevAssociationType_Type = HpPartnerDeviceType
_HpSwitchDevAssociationType_Object = MibTableColumn
hpSwitchDevAssociationType = _HpSwitchDevAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 1),
    _HpSwitchDevAssociationType_Type()
)
hpSwitchDevAssociationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchDevAssociationType.setStatus("deprecated")


class _HpSwitchDevAssociationProfName_Type(OctetString):
    """Custom type hpSwitchDevAssociationProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpSwitchDevAssociationProfName_Type.__name__ = "OctetString"
_HpSwitchDevAssociationProfName_Object = MibTableColumn
hpSwitchDevAssociationProfName = _HpSwitchDevAssociationProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 2),
    _HpSwitchDevAssociationProfName_Type()
)
hpSwitchDevAssociationProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevAssociationProfName.setStatus("deprecated")


class _HpSwitchDevAssociationProfID_Type(Unsigned32):
    """Custom type hpSwitchDevAssociationProfID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchDevAssociationProfID_Type.__name__ = "Unsigned32"
_HpSwitchDevAssociationProfID_Object = MibTableColumn
hpSwitchDevAssociationProfID = _HpSwitchDevAssociationProfID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 3),
    _HpSwitchDevAssociationProfID_Type()
)
hpSwitchDevAssociationProfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevAssociationProfID.setStatus("deprecated")


class _HpSwitchDevAssociationStatus_Type(Integer32):
    """Custom type hpSwitchDevAssociationStatus based on Integer32"""
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


_HpSwitchDevAssociationStatus_Type.__name__ = "Integer32"
_HpSwitchDevAssociationStatus_Object = MibTableColumn
hpSwitchDevAssociationStatus = _HpSwitchDevAssociationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 4),
    _HpSwitchDevAssociationStatus_Type()
)
hpSwitchDevAssociationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevAssociationStatus.setStatus("deprecated")
_HpSwitchRogueDevice_ObjectIdentity = ObjectIdentity
hpSwitchRogueDevice = _HpSwitchRogueDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3)
)


class _HpSwitchRogueDevStatus_Type(Integer32):
    """Custom type hpSwitchRogueDevStatus based on Integer32"""
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


_HpSwitchRogueDevStatus_Type.__name__ = "Integer32"
_HpSwitchRogueDevStatus_Object = MibScalar
hpSwitchRogueDevStatus = _HpSwitchRogueDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 1),
    _HpSwitchRogueDevStatus_Type()
)
hpSwitchRogueDevStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRogueDevStatus.setStatus("current")


class _HpSwitchRogueDevAction_Type(Integer32):
    """Custom type hpSwitchRogueDevAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("log", 2))
    )


_HpSwitchRogueDevAction_Type.__name__ = "Integer32"
_HpSwitchRogueDevAction_Object = MibScalar
hpSwitchRogueDevAction = _HpSwitchRogueDevAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 2),
    _HpSwitchRogueDevAction_Type()
)
hpSwitchRogueDevAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRogueDevAction.setStatus("current")
_HpSwitchRogueDevMacTable_Object = MibTable
hpSwitchRogueDevMacTable = _HpSwitchRogueDevMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hpSwitchRogueDevMacTable.setStatus("current")
_HpSwitchRogueDevMacEntry_Object = MibTableRow
hpSwitchRogueDevMacEntry = _HpSwitchRogueDevMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1)
)
hpSwitchRogueDevMacEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevMacAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchRogueDevMacEntry.setStatus("current")
_HpSwitchRogueDevMacAddress_Type = MacAddress
_HpSwitchRogueDevMacAddress_Object = MibTableColumn
hpSwitchRogueDevMacAddress = _HpSwitchRogueDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1, 1),
    _HpSwitchRogueDevMacAddress_Type()
)
hpSwitchRogueDevMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchRogueDevMacAddress.setStatus("current")
_HpSwitchNeighborDevMacAddress_Type = MacAddress
_HpSwitchNeighborDevMacAddress_Object = MibTableColumn
hpSwitchNeighborDevMacAddress = _HpSwitchNeighborDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1, 2),
    _HpSwitchNeighborDevMacAddress_Type()
)
hpSwitchNeighborDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchNeighborDevMacAddress.setStatus("current")
_HpSwitchWhitelistMacTable_Object = MibTable
hpSwitchWhitelistMacTable = _HpSwitchWhitelistMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4)
)
if mibBuilder.loadTexts:
    hpSwitchWhitelistMacTable.setStatus("current")
_HpSwitchWhitelistMacEntry_Object = MibTableRow
hpSwitchWhitelistMacEntry = _HpSwitchWhitelistMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1)
)
hpSwitchWhitelistMacEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistMacAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchWhitelistMacEntry.setStatus("current")
_HpSwitchWhitelistMacAddress_Type = MacAddress
_HpSwitchWhitelistMacAddress_Object = MibTableColumn
hpSwitchWhitelistMacAddress = _HpSwitchWhitelistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1, 1),
    _HpSwitchWhitelistMacAddress_Type()
)
hpSwitchWhitelistMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchWhitelistMacAddress.setStatus("current")
_HpSwitchWhitelistRowStatus_Type = RowStatus
_HpSwitchWhitelistRowStatus_Object = MibTableColumn
hpSwitchWhitelistRowStatus = _HpSwitchWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1, 2),
    _HpSwitchWhitelistRowStatus_Type()
)
hpSwitchWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchWhitelistRowStatus.setStatus("current")
_HpSwitchDevPortTable_Object = MibTable
hpSwitchDevPortTable = _HpSwitchDevPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5)
)
if mibBuilder.loadTexts:
    hpSwitchDevPortTable.setStatus("current")
_HpSwitchDevPortEntry_Object = MibTableRow
hpSwitchDevPortEntry = _HpSwitchDevPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1)
)
hpSwitchDevPortEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchDevPortEntry.setStatus("current")
_HpSwitchDevPortIndex_Type = InterfaceIndex
_HpSwitchDevPortIndex_Object = MibTableColumn
hpSwitchDevPortIndex = _HpSwitchDevPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 1),
    _HpSwitchDevPortIndex_Type()
)
hpSwitchDevPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchDevPortIndex.setStatus("current")
_HpSwitchDevPortType_Type = HpPartnerDeviceType
_HpSwitchDevPortType_Object = MibTableColumn
hpSwitchDevPortType = _HpSwitchDevPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 2),
    _HpSwitchDevPortType_Type()
)
hpSwitchDevPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDevPortType.setStatus("current")


class _HpSwitchDevPortProfName_Type(OctetString):
    """Custom type hpSwitchDevPortProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchDevPortProfName_Type.__name__ = "OctetString"
_HpSwitchDevPortProfName_Object = MibTableColumn
hpSwitchDevPortProfName = _HpSwitchDevPortProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 3),
    _HpSwitchDevPortProfName_Type()
)
hpSwitchDevPortProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDevPortProfName.setStatus("current")


class _HpSwitchDevPortDeviceName_Type(OctetString):
    """Custom type hpSwitchDevPortDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchDevPortDeviceName_Type.__name__ = "OctetString"
_HpSwitchDevPortDeviceName_Object = MibTableColumn
hpSwitchDevPortDeviceName = _HpSwitchDevPortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 4),
    _HpSwitchDevPortDeviceName_Type()
)
hpSwitchDevPortDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDevPortDeviceName.setStatus("current")
_HpSwitchDevIdentAssociationTable_Object = MibTable
hpSwitchDevIdentAssociationTable = _HpSwitchDevIdentAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6)
)
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationTable.setStatus("current")
_HpSwitchDevIdentAssociationEntry_Object = MibTableRow
hpSwitchDevIdentAssociationEntry = _HpSwitchDevIdentAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1)
)
hpSwitchDevIdentAssociationEntry.setIndexNames(
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationType"),
    (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationSubType"),
)
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationEntry.setStatus("current")
_HpSwitchDevIdentAssociationType_Type = HpPartnerDeviceType
_HpSwitchDevIdentAssociationType_Object = MibTableColumn
hpSwitchDevIdentAssociationType = _HpSwitchDevIdentAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 1),
    _HpSwitchDevIdentAssociationType_Type()
)
hpSwitchDevIdentAssociationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationType.setStatus("current")


class _HpSwitchDevIdentAssociationSubType_Type(Unsigned32):
    """Custom type hpSwitchDevIdentAssociationSubType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpSwitchDevIdentAssociationSubType_Type.__name__ = "Unsigned32"
_HpSwitchDevIdentAssociationSubType_Object = MibTableColumn
hpSwitchDevIdentAssociationSubType = _HpSwitchDevIdentAssociationSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 2),
    _HpSwitchDevIdentAssociationSubType_Type()
)
hpSwitchDevIdentAssociationSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationSubType.setStatus("current")
_HpSwitchDevIdentAssociationRowStatus_Type = RowStatus
_HpSwitchDevIdentAssociationRowStatus_Object = MibTableColumn
hpSwitchDevIdentAssociationRowStatus = _HpSwitchDevIdentAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 3),
    _HpSwitchDevIdentAssociationRowStatus_Type()
)
hpSwitchDevIdentAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationRowStatus.setStatus("current")


class _HpSwitchDevIdentAssociationProfName_Type(OctetString):
    """Custom type hpSwitchDevIdentAssociationProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpSwitchDevIdentAssociationProfName_Type.__name__ = "OctetString"
_HpSwitchDevIdentAssociationProfName_Object = MibTableColumn
hpSwitchDevIdentAssociationProfName = _HpSwitchDevIdentAssociationProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 4),
    _HpSwitchDevIdentAssociationProfName_Type()
)
hpSwitchDevIdentAssociationProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationProfName.setStatus("current")


class _HpSwitchDevIdentAssociationProfID_Type(Unsigned32):
    """Custom type hpSwitchDevIdentAssociationProfID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchDevIdentAssociationProfID_Type.__name__ = "Unsigned32"
_HpSwitchDevIdentAssociationProfID_Object = MibTableColumn
hpSwitchDevIdentAssociationProfID = _HpSwitchDevIdentAssociationProfID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 5),
    _HpSwitchDevIdentAssociationProfID_Type()
)
hpSwitchDevIdentAssociationProfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationProfID.setStatus("current")


class _HpSwitchDevIdentAssociationStatus_Type(Integer32):
    """Custom type hpSwitchDevIdentAssociationStatus based on Integer32"""
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


_HpSwitchDevIdentAssociationStatus_Type.__name__ = "Integer32"
_HpSwitchDevIdentAssociationStatus_Object = MibTableColumn
hpSwitchDevIdentAssociationStatus = _HpSwitchDevIdentAssociationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 6),
    _HpSwitchDevIdentAssociationStatus_Type()
)
hpSwitchDevIdentAssociationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationStatus.setStatus("current")


class _HpSwitchDevIdentAssociationDeviceType_Type(Unsigned32):
    """Custom type hpSwitchDevIdentAssociationDeviceType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchDevIdentAssociationDeviceType_Type.__name__ = "Unsigned32"
_HpSwitchDevIdentAssociationDeviceType_Object = MibTableColumn
hpSwitchDevIdentAssociationDeviceType = _HpSwitchDevIdentAssociationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 7),
    _HpSwitchDevIdentAssociationDeviceType_Type()
)
hpSwitchDevIdentAssociationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationDeviceType.setStatus("current")

# Managed Objects groups

hpSwitchDevProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 1)
)
hpSwitchDevProfileGroup.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchProfName"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfRowStatus"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfUntaggedVlanID"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTaggedVlanList"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfIngressBandwidth"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfEgressBandwidth"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfCosPriority"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPortSpeed"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoeMaxPower"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoePriority"))
)
if mibBuilder.loadTexts:
    hpSwitchDevProfileGroup.setStatus("deprecated")

hpSwitchDevAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 2)
)
hpSwitchDevAssociationGroup.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationProfName"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationProfID"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchDevAssociationGroup.setStatus("deprecated")

hpSwitchRogueDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 3)
)
hpSwitchRogueDevGroup.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevStatus"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevAction"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchNeighborDevMacAddress"))
)
if mibBuilder.loadTexts:
    hpSwitchRogueDevGroup.setStatus("current")

hpSwitchWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 4)
)
hpSwitchWhitelistGroup.setObjects(
    ("HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistRowStatus")
)
if mibBuilder.loadTexts:
    hpSwitchWhitelistGroup.setStatus("current")

hpSwitchDevPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 5)
)
hpSwitchDevPortGroup.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortType"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortProfName"))
)
if mibBuilder.loadTexts:
    hpSwitchDevPortGroup.setStatus("deprecated")

hpSwitchDevProfileGroupNew = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 6)
)
hpSwitchDevProfileGroupNew.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchProfName"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfRowStatus"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfUntaggedVlanID"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTaggedVlanList"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfIngressBandwidth"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfEgressBandwidth"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfCosPriority"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPortSpeed"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoeMaxPower"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoePriority"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfJumboFrameSupport"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTunneledNodeSupport"))
)
if mibBuilder.loadTexts:
    hpSwitchDevProfileGroupNew.setStatus("current")

hpSwitchDevIdentAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 7)
)
hpSwitchDevIdentAssociationGroup.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationRowStatus"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationProfName"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationProfID"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationStatus"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationDeviceType"))
)
if mibBuilder.loadTexts:
    hpSwitchDevIdentAssociationGroup.setStatus("current")

hpSwitchDevPortGroupNew = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 8)
)
hpSwitchDevPortGroupNew.setObjects(
      *(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortType"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortProfName"),
        ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortDeviceName"))
)
if mibBuilder.loadTexts:
    hpSwitchDevPortGroupNew.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchDevCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchDevCompliance.setStatus(
        "deprecated"
    )

hpSwitchDevCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchDevCompliance1.setStatus(
        "deprecated"
    )

hpSwitchDevCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpSwitchDevCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DEV-CONF-MIB",
    **{"HpPartnerDeviceType": HpPartnerDeviceType,
       "HpPartnerDeviceTypeList": HpPartnerDeviceTypeList,
       "hpicfDevConf": hpicfDevConf,
       "hpSwitchDevNotifications": hpSwitchDevNotifications,
       "hpSwitchDevScalar": hpSwitchDevScalar,
       "hpSwitchDevGlobals": hpSwitchDevGlobals,
       "hpSwitchDevConformance": hpSwitchDevConformance,
       "hpSwitchDevCompliances": hpSwitchDevCompliances,
       "hpSwitchDevCompliance": hpSwitchDevCompliance,
       "hpSwitchDevCompliance1": hpSwitchDevCompliance1,
       "hpSwitchDevCompliance2": hpSwitchDevCompliance2,
       "hpSwitchDevConfigGroups": hpSwitchDevConfigGroups,
       "hpSwitchDevProfileGroup": hpSwitchDevProfileGroup,
       "hpSwitchDevAssociationGroup": hpSwitchDevAssociationGroup,
       "hpSwitchRogueDevGroup": hpSwitchRogueDevGroup,
       "hpSwitchWhitelistGroup": hpSwitchWhitelistGroup,
       "hpSwitchDevPortGroup": hpSwitchDevPortGroup,
       "hpSwitchDevProfileGroupNew": hpSwitchDevProfileGroupNew,
       "hpSwitchDevIdentAssociationGroup": hpSwitchDevIdentAssociationGroup,
       "hpSwitchDevPortGroupNew": hpSwitchDevPortGroupNew,
       "hpSwitchDevConfig": hpSwitchDevConfig,
       "hpSwitchDevProfTable": hpSwitchDevProfTable,
       "hpSwitchDevProfEntry": hpSwitchDevProfEntry,
       "hpSwitchProfIndex": hpSwitchProfIndex,
       "hpSwitchProfRowStatus": hpSwitchProfRowStatus,
       "hpSwitchProfName": hpSwitchProfName,
       "hpSwitchProfUntaggedVlanID": hpSwitchProfUntaggedVlanID,
       "hpSwitchProfTaggedVlanList": hpSwitchProfTaggedVlanList,
       "hpSwitchProfIngressBandwidth": hpSwitchProfIngressBandwidth,
       "hpSwitchProfEgressBandwidth": hpSwitchProfEgressBandwidth,
       "hpSwitchProfCosPriority": hpSwitchProfCosPriority,
       "hpSwitchProfPortSpeed": hpSwitchProfPortSpeed,
       "hpSwitchProfPoeMaxPower": hpSwitchProfPoeMaxPower,
       "hpSwitchProfPoePriority": hpSwitchProfPoePriority,
       "hpSwitchProfJumboFrameSupport": hpSwitchProfJumboFrameSupport,
       "hpSwitchProfTunneledNodeSupport": hpSwitchProfTunneledNodeSupport,
       "hpSwitchDevAssociationTable": hpSwitchDevAssociationTable,
       "hpSwitchDevAssociationEntry": hpSwitchDevAssociationEntry,
       "hpSwitchDevAssociationType": hpSwitchDevAssociationType,
       "hpSwitchDevAssociationProfName": hpSwitchDevAssociationProfName,
       "hpSwitchDevAssociationProfID": hpSwitchDevAssociationProfID,
       "hpSwitchDevAssociationStatus": hpSwitchDevAssociationStatus,
       "hpSwitchRogueDevice": hpSwitchRogueDevice,
       "hpSwitchRogueDevStatus": hpSwitchRogueDevStatus,
       "hpSwitchRogueDevAction": hpSwitchRogueDevAction,
       "hpSwitchRogueDevMacTable": hpSwitchRogueDevMacTable,
       "hpSwitchRogueDevMacEntry": hpSwitchRogueDevMacEntry,
       "hpSwitchRogueDevMacAddress": hpSwitchRogueDevMacAddress,
       "hpSwitchNeighborDevMacAddress": hpSwitchNeighborDevMacAddress,
       "hpSwitchWhitelistMacTable": hpSwitchWhitelistMacTable,
       "hpSwitchWhitelistMacEntry": hpSwitchWhitelistMacEntry,
       "hpSwitchWhitelistMacAddress": hpSwitchWhitelistMacAddress,
       "hpSwitchWhitelistRowStatus": hpSwitchWhitelistRowStatus,
       "hpSwitchDevPortTable": hpSwitchDevPortTable,
       "hpSwitchDevPortEntry": hpSwitchDevPortEntry,
       "hpSwitchDevPortIndex": hpSwitchDevPortIndex,
       "hpSwitchDevPortType": hpSwitchDevPortType,
       "hpSwitchDevPortProfName": hpSwitchDevPortProfName,
       "hpSwitchDevPortDeviceName": hpSwitchDevPortDeviceName,
       "hpSwitchDevIdentAssociationTable": hpSwitchDevIdentAssociationTable,
       "hpSwitchDevIdentAssociationEntry": hpSwitchDevIdentAssociationEntry,
       "hpSwitchDevIdentAssociationType": hpSwitchDevIdentAssociationType,
       "hpSwitchDevIdentAssociationSubType": hpSwitchDevIdentAssociationSubType,
       "hpSwitchDevIdentAssociationRowStatus": hpSwitchDevIdentAssociationRowStatus,
       "hpSwitchDevIdentAssociationProfName": hpSwitchDevIdentAssociationProfName,
       "hpSwitchDevIdentAssociationProfID": hpSwitchDevIdentAssociationProfID,
       "hpSwitchDevIdentAssociationStatus": hpSwitchDevIdentAssociationStatus,
       "hpSwitchDevIdentAssociationDeviceType": hpSwitchDevIdentAssociationDeviceType}
)
