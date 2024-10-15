# SNMP MIB module (HUAWEI-MINM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MINM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:01 2024
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

(VlanList,) = mibBuilder.importSymbols(
    "HUAWEI-L2IF-MIB",
    "VlanList")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TransportAddress,
 TransportDomain) = mibBuilder.importSymbols(
    "TRANSPORT-ADDRESS-MIB",
    "TransportAddress",
    "TransportDomain")


# MODULE-IDENTITY

hwMinMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class HWOperStatus(Integer32, TextualConvention):
    status = "current"
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



class HwDot1agCfmCcmInterval(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 4),
          ("interval10min", 8),
          ("interval10ms", 3),
          ("interval10s", 6),
          ("interval1min", 7),
          ("interval1s", 5),
          ("interval20ms", 9),
          ("interval300Hz", 2),
          ("interval30ms", 10),
          ("interval50ms", 11),
          ("intervalInvalid", 1))
    )



class HwDot1agCfmRelayActionFieldValue(Integer32, TextualConvention):
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
        *(("rlyFdb", 2),
          ("rlyHit", 1),
          ("rlyMpdb", 3))
    )



class HwLldpChassisIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portComponent", 3))
    )



class HwLldpChassisId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class HwLldpPortIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class HwLldpPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class HwLldpManAddrIfSubtype(Integer32, TextualConvention):
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
        *(("ifIndex", 2),
          ("systemPortNumber", 3),
          ("unknown", 1))
    )



class HwLldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class HwDot1agCfmIngressActionFieldValue(Integer32, TextualConvention):
    status = "current"
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
        *(("ingBlocked", 3),
          ("ingDown", 2),
          ("ingOk", 1),
          ("ingVid", 4))
    )



class HwDot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
    status = "current"
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
        *(("egrBlocked", 3),
          ("egrDown", 2),
          ("egrOK", 1),
          ("egrVid", 4))
    )



class HWApsInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("apsInterval10ms", 3),
          ("apsInterval15ms", 4),
          ("apsInterval20ms", 5),
          ("apsInterval30ms", 6),
          ("apsInterval3dot3ms", 1),
          ("apsInterval5ms", 2))
    )



class HWProtectMode(Integer32, TextualConvention):
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
        *(("onePlusOneBidirectional", 1),
          ("onePlusOneUnidirectional", 2),
          ("oneToOne", 3))
    )



class HWSwitchOperation(Integer32, TextualConvention):
    status = "current"
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
        *(("clear", 1),
          ("force", 3),
          ("lock", 2),
          ("manual", 4),
          ("null", 5))
    )



class HWProtectProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protocolAps", 1),
          ("protocolOam", 2))
    )



class HWServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mp2mp", 2),
          ("p2p", 1))
    )



class HWInterfaceType(Integer32, TextualConvention):
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
        *(("bundling", 3),
          ("oneToOne", 2),
          ("transparent", 1))
    )



class HWProcessBehavior(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )



class HWStaticMacFwdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 2),
          ("static", 1))
    )



class HwDot1agCfmMepIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )



# MIB Managed Objects in the order of their OIDs

_HwMINM_ObjectIdentity = ObjectIdentity
hwMINM = _HwMINM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133)
)
_HwMinMObjects_ObjectIdentity = ObjectIdentity
hwMinMObjects = _HwMinMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1)
)
_HwMinMSystemObjects_ObjectIdentity = ObjectIdentity
hwMinMSystemObjects = _HwMinMSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 1)
)
_HwMinMVirtualMac_Type = MacAddress
_HwMinMVirtualMac_Object = MibScalar
hwMinMVirtualMac = _HwMinMVirtualMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 1, 1),
    _HwMinMVirtualMac_Type()
)
hwMinMVirtualMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMinMVirtualMac.setStatus("current")


class _HwMinMMacTnlBVlanListLow_Type(VlanList):
    """Custom type hwMinMMacTnlBVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwMinMMacTnlBVlanListLow_Type.__name__ = "VlanList"
_HwMinMMacTnlBVlanListLow_Object = MibScalar
hwMinMMacTnlBVlanListLow = _HwMinMMacTnlBVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 1, 2),
    _HwMinMMacTnlBVlanListLow_Type()
)
hwMinMMacTnlBVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMinMMacTnlBVlanListLow.setStatus("current")


class _HwMinMMacTnlBVlanListHigh_Type(VlanList):
    """Custom type hwMinMMacTnlBVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwMinMMacTnlBVlanListHigh_Type.__name__ = "VlanList"
_HwMinMMacTnlBVlanListHigh_Object = MibScalar
hwMinMMacTnlBVlanListHigh = _HwMinMMacTnlBVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 1, 3),
    _HwMinMMacTnlBVlanListHigh_Type()
)
hwMinMMacTnlBVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMinMMacTnlBVlanListHigh.setStatus("current")


class _HwMinMTrapEnable_Type(EnabledStatus):
    """Custom type hwMinMTrapEnable based on EnabledStatus"""
    defaultValue = 2


_HwMinMTrapEnable_Object = MibScalar
hwMinMTrapEnable = _HwMinMTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 1, 4),
    _HwMinMTrapEnable_Type()
)
hwMinMTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMinMTrapEnable.setStatus("current")
_HwMinMMacTnlObjects_ObjectIdentity = ObjectIdentity
hwMinMMacTnlObjects = _HwMinMMacTnlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2)
)
_HwMinMMacTnlCfgObjects_ObjectIdentity = ObjectIdentity
hwMinMMacTnlCfgObjects = _HwMinMMacTnlCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1)
)
_HwMinMMacTnlIndexNext_Type = Unsigned32
_HwMinMMacTnlIndexNext_Object = MibScalar
hwMinMMacTnlIndexNext = _HwMinMMacTnlIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 1),
    _HwMinMMacTnlIndexNext_Type()
)
hwMinMMacTnlIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlIndexNext.setStatus("current")
_HwMinMMacTnlCfgTable_Object = MibTable
hwMinMMacTnlCfgTable = _HwMinMMacTnlCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCfgTable.setStatus("current")
_HwMinMMacTnlCfgEntry_Object = MibTableRow
hwMinMMacTnlCfgEntry = _HwMinMMacTnlCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1)
)
hwMinMMacTnlCfgEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCfgEntry.setStatus("current")
_HwMinMMacTnlIndex_Type = Unsigned32
_HwMinMMacTnlIndex_Object = MibTableColumn
hwMinMMacTnlIndex = _HwMinMMacTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 1),
    _HwMinMMacTnlIndex_Type()
)
hwMinMMacTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMMacTnlIndex.setStatus("current")


class _HwMinMMacTnlName_Type(OctetString):
    """Custom type hwMinMMacTnlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMinMMacTnlName_Type.__name__ = "OctetString"
_HwMinMMacTnlName_Object = MibTableColumn
hwMinMMacTnlName = _HwMinMMacTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 11),
    _HwMinMMacTnlName_Type()
)
hwMinMMacTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlName.setStatus("current")
_HwMinMMacTnlDMac_Type = MacAddress
_HwMinMMacTnlDMac_Object = MibTableColumn
hwMinMMacTnlDMac = _HwMinMMacTnlDMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 12),
    _HwMinMMacTnlDMac_Type()
)
hwMinMMacTnlDMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlDMac.setStatus("current")
_HwMinMMacTnlBVlanID_Type = VlanIdOrNone
_HwMinMMacTnlBVlanID_Object = MibTableColumn
hwMinMMacTnlBVlanID = _HwMinMMacTnlBVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 13),
    _HwMinMMacTnlBVlanID_Type()
)
hwMinMMacTnlBVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlBVlanID.setStatus("current")


class _HwMinMMacTnlBVlanType_Type(OctetString):
    """Custom type hwMinMMacTnlBVlanType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwMinMMacTnlBVlanType_Type.__name__ = "OctetString"
_HwMinMMacTnlBVlanType_Object = MibTableColumn
hwMinMMacTnlBVlanType = _HwMinMMacTnlBVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 14),
    _HwMinMMacTnlBVlanType_Type()
)
hwMinMMacTnlBVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlBVlanType.setStatus("current")


class _HwMinMMacTnlPriorityValue_Type(Integer32):
    """Custom type hwMinMMacTnlPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwMinMMacTnlPriorityValue_Type.__name__ = "Integer32"
_HwMinMMacTnlPriorityValue_Object = MibTableColumn
hwMinMMacTnlPriorityValue = _HwMinMMacTnlPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 15),
    _HwMinMMacTnlPriorityValue_Type()
)
hwMinMMacTnlPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlPriorityValue.setStatus("current")
_HwMinMMacTnlOutgoingIfIndex_Type = InterfaceIndexOrZero
_HwMinMMacTnlOutgoingIfIndex_Object = MibTableColumn
hwMinMMacTnlOutgoingIfIndex = _HwMinMMacTnlOutgoingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 16),
    _HwMinMMacTnlOutgoingIfIndex_Type()
)
hwMinMMacTnlOutgoingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlOutgoingIfIndex.setStatus("current")
_HwMinMMacTnlSplitHorizonEnable_Type = EnabledStatus
_HwMinMMacTnlSplitHorizonEnable_Object = MibTableColumn
hwMinMMacTnlSplitHorizonEnable = _HwMinMMacTnlSplitHorizonEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 17),
    _HwMinMMacTnlSplitHorizonEnable_Type()
)
hwMinMMacTnlSplitHorizonEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlSplitHorizonEnable.setStatus("current")
_HwMinMMacTnlAdminStatus_Type = HWAdminStatus
_HwMinMMacTnlAdminStatus_Object = MibTableColumn
hwMinMMacTnlAdminStatus = _HwMinMMacTnlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 18),
    _HwMinMMacTnlAdminStatus_Type()
)
hwMinMMacTnlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlAdminStatus.setStatus("current")
_HwMinMMacTnlOperStatus_Type = HWOperStatus
_HwMinMMacTnlOperStatus_Object = MibTableColumn
hwMinMMacTnlOperStatus = _HwMinMMacTnlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 19),
    _HwMinMMacTnlOperStatus_Type()
)
hwMinMMacTnlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlOperStatus.setStatus("current")


class _HwMinMMacTnlDescription_Type(OctetString):
    """Custom type hwMinMMacTnlDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HwMinMMacTnlDescription_Type.__name__ = "OctetString"
_HwMinMMacTnlDescription_Object = MibTableColumn
hwMinMMacTnlDescription = _HwMinMMacTnlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 20),
    _HwMinMMacTnlDescription_Type()
)
hwMinMMacTnlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlDescription.setStatus("current")
_HwMinMMacTnlStatisticsReset_Type = EnabledStatus
_HwMinMMacTnlStatisticsReset_Object = MibTableColumn
hwMinMMacTnlStatisticsReset = _HwMinMMacTnlStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 21),
    _HwMinMMacTnlStatisticsReset_Type()
)
hwMinMMacTnlStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlStatisticsReset.setStatus("current")


class _HwMinMMacTnlPriorityTrustITag_Type(TruthValue):
    """Custom type hwMinMMacTnlPriorityTrustITag based on TruthValue"""
    defaultValue = 2


_HwMinMMacTnlPriorityTrustITag_Object = MibTableColumn
hwMinMMacTnlPriorityTrustITag = _HwMinMMacTnlPriorityTrustITag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 22),
    _HwMinMMacTnlPriorityTrustITag_Type()
)
hwMinMMacTnlPriorityTrustITag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlPriorityTrustITag.setStatus("current")


class _HwMinMMacTnlDeiTrustIDei_Type(TruthValue):
    """Custom type hwMinMMacTnlDeiTrustIDei based on TruthValue"""
    defaultValue = 2


_HwMinMMacTnlDeiTrustIDei_Object = MibTableColumn
hwMinMMacTnlDeiTrustIDei = _HwMinMMacTnlDeiTrustIDei_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 23),
    _HwMinMMacTnlDeiTrustIDei_Type()
)
hwMinMMacTnlDeiTrustIDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlDeiTrustIDei.setStatus("current")


class _HwMinMMacTnlDeiValue_Type(Integer32):
    """Custom type hwMinMMacTnlDeiValue based on Integer32"""
    defaultValue = 0


_HwMinMMacTnlDeiValue_Object = MibTableColumn
hwMinMMacTnlDeiValue = _HwMinMMacTnlDeiValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 24),
    _HwMinMMacTnlDeiValue_Type()
)
hwMinMMacTnlDeiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlDeiValue.setStatus("current")
_HwMinMMacTnlRowStatus_Type = RowStatus
_HwMinMMacTnlRowStatus_Object = MibTableColumn
hwMinMMacTnlRowStatus = _HwMinMMacTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 2, 1, 51),
    _HwMinMMacTnlRowStatus_Type()
)
hwMinMMacTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlRowStatus.setStatus("current")
_HwMinMMacTnlStatisticsTable_Object = MibTable
hwMinMMacTnlStatisticsTable = _HwMinMMacTnlStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlStatisticsTable.setStatus("current")
_HwMinMMacTnlStatisticsEntry_Object = MibTableRow
hwMinMMacTnlStatisticsEntry = _HwMinMMacTnlStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3, 1)
)
hwMinMMacTnlStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlStatisticsEntry.setStatus("current")
_HwMinMMacTnlInPackets_Type = Counter64
_HwMinMMacTnlInPackets_Object = MibTableColumn
hwMinMMacTnlInPackets = _HwMinMMacTnlInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3, 1, 11),
    _HwMinMMacTnlInPackets_Type()
)
hwMinMMacTnlInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlInPackets.setStatus("current")
_HwMinMMacTnlInBytes_Type = Counter64
_HwMinMMacTnlInBytes_Object = MibTableColumn
hwMinMMacTnlInBytes = _HwMinMMacTnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3, 1, 12),
    _HwMinMMacTnlInBytes_Type()
)
hwMinMMacTnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlInBytes.setStatus("current")
_HwMinMMacTnlOutPackets_Type = Counter64
_HwMinMMacTnlOutPackets_Object = MibTableColumn
hwMinMMacTnlOutPackets = _HwMinMMacTnlOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3, 1, 13),
    _HwMinMMacTnlOutPackets_Type()
)
hwMinMMacTnlOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlOutPackets.setStatus("current")
_HwMinMMacTnlOutBytes_Type = Counter64
_HwMinMMacTnlOutBytes_Object = MibTableColumn
hwMinMMacTnlOutBytes = _HwMinMMacTnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 3, 1, 14),
    _HwMinMMacTnlOutBytes_Type()
)
hwMinMMacTnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlOutBytes.setStatus("current")
_HwMacTnlNameToIndexMappingTable_Object = MibTable
hwMacTnlNameToIndexMappingTable = _HwMacTnlNameToIndexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwMacTnlNameToIndexMappingTable.setStatus("current")
_HwMacTnlNameToIndexMappingEntry_Object = MibTableRow
hwMacTnlNameToIndexMappingEntry = _HwMacTnlNameToIndexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 4, 1)
)
hwMacTnlNameToIndexMappingEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMacTnlName"),
)
if mibBuilder.loadTexts:
    hwMacTnlNameToIndexMappingEntry.setStatus("current")


class _HwMacTnlName_Type(OctetString):
    """Custom type hwMacTnlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacTnlName_Type.__name__ = "OctetString"
_HwMacTnlName_Object = MibTableColumn
hwMacTnlName = _HwMacTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 4, 1, 1),
    _HwMacTnlName_Type()
)
hwMacTnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacTnlName.setStatus("current")
_HwMacTnlIndex_Type = Unsigned32
_HwMacTnlIndex_Object = MibTableColumn
hwMacTnlIndex = _HwMacTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 1, 4, 1, 11),
    _HwMacTnlIndex_Type()
)
hwMacTnlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacTnlIndex.setStatus("current")
_HwMinMMacTnlOamObjects_ObjectIdentity = ObjectIdentity
hwMinMMacTnlOamObjects = _HwMinMMacTnlOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2)
)
_HwMinMMacTnlCCTable_Object = MibTable
hwMinMMacTnlCCTable = _HwMinMMacTnlCCTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCCTable.setStatus("current")
_HwMinMMacTnlCCEntry_Object = MibTableRow
hwMinMMacTnlCCEntry = _HwMinMMacTnlCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1)
)
hwMinMMacTnlCCEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCCEntry.setStatus("current")
_HwMinMMacTnlCfmEnable_Type = EnabledStatus
_HwMinMMacTnlCfmEnable_Object = MibTableColumn
hwMinMMacTnlCfmEnable = _HwMinMMacTnlCfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 11),
    _HwMinMMacTnlCfmEnable_Type()
)
hwMinMMacTnlCfmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlCfmEnable.setStatus("current")


class _HwMinMMacTnlCCInterval_Type(HwDot1agCfmCcmInterval):
    """Custom type hwMinMMacTnlCCInterval based on HwDot1agCfmCcmInterval"""
    defaultValue = 3


_HwMinMMacTnlCCInterval_Object = MibTableColumn
hwMinMMacTnlCCInterval = _HwMinMMacTnlCCInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 12),
    _HwMinMMacTnlCCInterval_Type()
)
hwMinMMacTnlCCInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlCCInterval.setStatus("current")
_HwMinMMacTnlSomeRMepCcmDefect_Type = TruthValue
_HwMinMMacTnlSomeRMepCcmDefect_Object = MibTableColumn
hwMinMMacTnlSomeRMepCcmDefect = _HwMinMMacTnlSomeRMepCcmDefect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 13),
    _HwMinMMacTnlSomeRMepCcmDefect_Type()
)
hwMinMMacTnlSomeRMepCcmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlSomeRMepCcmDefect.setStatus("current")
_HwMinMMacTnlSomeRdiDefect_Type = TruthValue
_HwMinMMacTnlSomeRdiDefect_Object = MibTableColumn
hwMinMMacTnlSomeRdiDefect = _HwMinMMacTnlSomeRdiDefect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 14),
    _HwMinMMacTnlSomeRdiDefect_Type()
)
hwMinMMacTnlSomeRdiDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlSomeRdiDefect.setStatus("current")
_HwMinMMacTnlCcReceiveEnabled_Type = TruthValue
_HwMinMMacTnlCcReceiveEnabled_Object = MibTableColumn
hwMinMMacTnlCcReceiveEnabled = _HwMinMMacTnlCcReceiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 15),
    _HwMinMMacTnlCcReceiveEnabled_Type()
)
hwMinMMacTnlCcReceiveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlCcReceiveEnabled.setStatus("current")
_HwMinMMacTnlCCRowStatus_Type = RowStatus
_HwMinMMacTnlCCRowStatus_Object = MibTableColumn
hwMinMMacTnlCCRowStatus = _HwMinMMacTnlCCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 1, 1, 51),
    _HwMinMMacTnlCCRowStatus_Type()
)
hwMinMMacTnlCCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlCCRowStatus.setStatus("current")
_HwMinMMacTnlLbTable_Object = MibTable
hwMinMMacTnlLbTable = _HwMinMMacTnlLbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLbTable.setStatus("current")
_HwMinMMacTnlLbEntry_Object = MibTableRow
hwMinMMacTnlLbEntry = _HwMinMMacTnlLbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1)
)
hwMinMMacTnlLbEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLbEntry.setStatus("current")
_HwMinMMacTnlLbmEnable_Type = EnabledStatus
_HwMinMMacTnlLbmEnable_Object = MibTableColumn
hwMinMMacTnlLbmEnable = _HwMinMMacTnlLbmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 11),
    _HwMinMMacTnlLbmEnable_Type()
)
hwMinMMacTnlLbmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmEnable.setStatus("current")
_HwMinMMacTnlLbmTimeStamp_Type = TimeStamp
_HwMinMMacTnlLbmTimeStamp_Object = MibTableColumn
hwMinMMacTnlLbmTimeStamp = _HwMinMMacTnlLbmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 12),
    _HwMinMMacTnlLbmTimeStamp_Type()
)
hwMinMMacTnlLbmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmTimeStamp.setStatus("current")


class _HwMinMMacTnlLbmTimeOut_Type(Integer32):
    """Custom type hwMinMMacTnlLbmTimeOut based on Integer32"""
    defaultValue = 2000


_HwMinMMacTnlLbmTimeOut_Object = MibTableColumn
hwMinMMacTnlLbmTimeOut = _HwMinMMacTnlLbmTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 13),
    _HwMinMMacTnlLbmTimeOut_Type()
)
hwMinMMacTnlLbmTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmTimeOut.setStatus("current")
_HwMinMMacTnlLbmTimes_Type = Integer32
_HwMinMMacTnlLbmTimes_Object = MibTableColumn
hwMinMMacTnlLbmTimes = _HwMinMMacTnlLbmTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 14),
    _HwMinMMacTnlLbmTimes_Type()
)
hwMinMMacTnlLbmTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmTimes.setStatus("current")


class _HwMinMMacTnlLbmSize_Type(Integer32):
    """Custom type hwMinMMacTnlLbmSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1480),
    )


_HwMinMMacTnlLbmSize_Type.__name__ = "Integer32"
_HwMinMMacTnlLbmSize_Object = MibTableColumn
hwMinMMacTnlLbmSize = _HwMinMMacTnlLbmSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 15),
    _HwMinMMacTnlLbmSize_Type()
)
hwMinMMacTnlLbmSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmSize.setStatus("current")
_HwMinMMacTnlLbrIn_Type = Counter32
_HwMinMMacTnlLbrIn_Object = MibTableColumn
hwMinMMacTnlLbrIn = _HwMinMMacTnlLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 16),
    _HwMinMMacTnlLbrIn_Type()
)
hwMinMMacTnlLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbrIn.setStatus("current")
_HwMinMMacTnlLbmResult_Type = TruthValue
_HwMinMMacTnlLbmResult_Object = MibTableColumn
hwMinMMacTnlLbmResult = _HwMinMMacTnlLbmResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 17),
    _HwMinMMacTnlLbmResult_Type()
)
hwMinMMacTnlLbmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbmResult.setStatus("current")
_HwMinMMacTnlLbRowStatus_Type = RowStatus
_HwMinMMacTnlLbRowStatus_Object = MibTableColumn
hwMinMMacTnlLbRowStatus = _HwMinMMacTnlLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 2, 1, 51),
    _HwMinMMacTnlLbRowStatus_Type()
)
hwMinMMacTnlLbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLbRowStatus.setStatus("current")
_HwMinMMacTnlLbResultTable_Object = MibTable
hwMinMMacTnlLbResultTable = _HwMinMMacTnlLbResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLbResultTable.setStatus("current")
_HwMinMMacTnlLbResultEntry_Object = MibTableRow
hwMinMMacTnlLbResultEntry = _HwMinMMacTnlLbResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3, 1)
)
hwMinMMacTnlLbResultEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLbResultEntry.setStatus("current")
_HwMinMMacTnlMacPingRTTMin_Type = Gauge32
_HwMinMMacTnlMacPingRTTMin_Object = MibTableColumn
hwMinMMacTnlMacPingRTTMin = _HwMinMMacTnlMacPingRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3, 1, 11),
    _HwMinMMacTnlMacPingRTTMin_Type()
)
hwMinMMacTnlMacPingRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlMacPingRTTMin.setStatus("current")
_HwMinMMacTnlMacPingRTTMax_Type = Gauge32
_HwMinMMacTnlMacPingRTTMax_Object = MibTableColumn
hwMinMMacTnlMacPingRTTMax = _HwMinMMacTnlMacPingRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3, 1, 12),
    _HwMinMMacTnlMacPingRTTMax_Type()
)
hwMinMMacTnlMacPingRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlMacPingRTTMax.setStatus("current")
_HwMinMMacTnlMacPingRTTAvg_Type = Gauge32
_HwMinMMacTnlMacPingRTTAvg_Object = MibTableColumn
hwMinMMacTnlMacPingRTTAvg = _HwMinMMacTnlMacPingRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3, 1, 13),
    _HwMinMMacTnlMacPingRTTAvg_Type()
)
hwMinMMacTnlMacPingRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlMacPingRTTAvg.setStatus("current")
_HwMinMMacTnlMacPingPacketLossRatio_Type = Gauge32
_HwMinMMacTnlMacPingPacketLossRatio_Object = MibTableColumn
hwMinMMacTnlMacPingPacketLossRatio = _HwMinMMacTnlMacPingPacketLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 3, 1, 14),
    _HwMinMMacTnlMacPingPacketLossRatio_Type()
)
hwMinMMacTnlMacPingPacketLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlMacPingPacketLossRatio.setStatus("current")
_HwMinMMacTnlLtmTable_Object = MibTable
hwMinMMacTnlLtmTable = _HwMinMMacTnlLtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmTable.setStatus("current")
_HwMinMMacTnlLtmEntry_Object = MibTableRow
hwMinMMacTnlLtmEntry = _HwMinMMacTnlLtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1)
)
hwMinMMacTnlLtmEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmEntry.setStatus("current")
_HwMinMMacTnlLtmEnable_Type = EnabledStatus
_HwMinMMacTnlLtmEnable_Object = MibTableColumn
hwMinMMacTnlLtmEnable = _HwMinMMacTnlLtmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 11),
    _HwMinMMacTnlLtmEnable_Type()
)
hwMinMMacTnlLtmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmEnable.setStatus("current")
_HwMinMMacTnlLtmTimeStamp_Type = TimeStamp
_HwMinMMacTnlLtmTimeStamp_Object = MibTableColumn
hwMinMMacTnlLtmTimeStamp = _HwMinMMacTnlLtmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 12),
    _HwMinMMacTnlLtmTimeStamp_Type()
)
hwMinMMacTnlLtmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmTimeStamp.setStatus("current")


class _HwMinMMacTnlLtmTimeOut_Type(Integer32):
    """Custom type hwMinMMacTnlLtmTimeOut based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMinMMacTnlLtmTimeOut_Type.__name__ = "Integer32"
_HwMinMMacTnlLtmTimeOut_Object = MibTableColumn
hwMinMMacTnlLtmTimeOut = _HwMinMMacTnlLtmTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 13),
    _HwMinMMacTnlLtmTimeOut_Type()
)
hwMinMMacTnlLtmTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmTimeOut.setStatus("current")


class _HwMinMMacTnlLtmTtl_Type(Unsigned32):
    """Custom type hwMinMMacTnlLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMinMMacTnlLtmTtl_Type.__name__ = "Unsigned32"
_HwMinMMacTnlLtmTtl_Object = MibTableColumn
hwMinMMacTnlLtmTtl = _HwMinMMacTnlLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 14),
    _HwMinMMacTnlLtmTtl_Type()
)
hwMinMMacTnlLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmTtl.setStatus("current")


class _HwMinMMacTnlLtmFlags_Type(Bits):
    """Custom type hwMinMMacTnlLtmFlags based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_HwMinMMacTnlLtmFlags_Type.__name__ = "Bits"
_HwMinMMacTnlLtmFlags_Object = MibTableColumn
hwMinMMacTnlLtmFlags = _HwMinMMacTnlLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 15),
    _HwMinMMacTnlLtmFlags_Type()
)
hwMinMMacTnlLtmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmFlags.setStatus("current")
_HwMinMMacTnlLtmSeqNumber_Type = Unsigned32
_HwMinMMacTnlLtmSeqNumber_Object = MibTableColumn
hwMinMMacTnlLtmSeqNumber = _HwMinMMacTnlLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 16),
    _HwMinMMacTnlLtmSeqNumber_Type()
)
hwMinMMacTnlLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmSeqNumber.setStatus("current")
_HwMinMMacTnlLtmEgressIdentifier_Type = Unsigned32
_HwMinMMacTnlLtmEgressIdentifier_Object = MibTableColumn
hwMinMMacTnlLtmEgressIdentifier = _HwMinMMacTnlLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 17),
    _HwMinMMacTnlLtmEgressIdentifier_Type()
)
hwMinMMacTnlLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmEgressIdentifier.setStatus("current")
_HwMinMMacTnlLtmResult_Type = TruthValue
_HwMinMMacTnlLtmResult_Object = MibTableColumn
hwMinMMacTnlLtmResult = _HwMinMMacTnlLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 18),
    _HwMinMMacTnlLtmResult_Type()
)
hwMinMMacTnlLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmResult.setStatus("current")
_HwMinMMacTnlLtmRowStatus_Type = RowStatus
_HwMinMMacTnlLtmRowStatus_Object = MibTableColumn
hwMinMMacTnlLtmRowStatus = _HwMinMMacTnlLtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 4, 1, 51),
    _HwMinMMacTnlLtmRowStatus_Type()
)
hwMinMMacTnlLtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtmRowStatus.setStatus("current")
_HwMinMMacTnlLtrTable_Object = MibTable
hwMinMMacTnlLtrTable = _HwMinMMacTnlLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrTable.setStatus("current")
_HwMinMMacTnlLtrEntry_Object = MibTableRow
hwMinMMacTnlLtrEntry = _HwMinMMacTnlLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1)
)
hwMinMMacTnlLtrEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlLtrSeqNumber"),
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrEntry.setStatus("current")
_HwMinMMacTnlLtrSeqNumber_Type = Unsigned32
_HwMinMMacTnlLtrSeqNumber_Object = MibTableColumn
hwMinMMacTnlLtrSeqNumber = _HwMinMMacTnlLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 1),
    _HwMinMMacTnlLtrSeqNumber_Type()
)
hwMinMMacTnlLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrSeqNumber.setStatus("current")
_HwMinMMacTnlLtrReceiveOrder_Type = Unsigned32
_HwMinMMacTnlLtrReceiveOrder_Object = MibTableColumn
hwMinMMacTnlLtrReceiveOrder = _HwMinMMacTnlLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 2),
    _HwMinMMacTnlLtrReceiveOrder_Type()
)
hwMinMMacTnlLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrReceiveOrder.setStatus("current")


class _HwMinMMacTnlLtrTtl_Type(Unsigned32):
    """Custom type hwMinMMacTnlLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMinMMacTnlLtrTtl_Type.__name__ = "Unsigned32"
_HwMinMMacTnlLtrTtl_Object = MibTableColumn
hwMinMMacTnlLtrTtl = _HwMinMMacTnlLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 11),
    _HwMinMMacTnlLtrTtl_Type()
)
hwMinMMacTnlLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrTtl.setStatus("current")
_HwMinMMacTnlLtrForwarded_Type = TruthValue
_HwMinMMacTnlLtrForwarded_Object = MibTableColumn
hwMinMMacTnlLtrForwarded = _HwMinMMacTnlLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 12),
    _HwMinMMacTnlLtrForwarded_Type()
)
hwMinMMacTnlLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrForwarded.setStatus("current")


class _HwMinMMacTnlLtrLastEgressIdentifier_Type(OctetString):
    """Custom type hwMinMMacTnlLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMinMMacTnlLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_HwMinMMacTnlLtrLastEgressIdentifier_Object = MibTableColumn
hwMinMMacTnlLtrLastEgressIdentifier = _HwMinMMacTnlLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 13),
    _HwMinMMacTnlLtrLastEgressIdentifier_Type()
)
hwMinMMacTnlLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrLastEgressIdentifier.setStatus("current")


class _HwMinMMacTnlLtrNextEgressIdentifier_Type(OctetString):
    """Custom type hwMinMMacTnlLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMinMMacTnlLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_HwMinMMacTnlLtrNextEgressIdentifier_Object = MibTableColumn
hwMinMMacTnlLtrNextEgressIdentifier = _HwMinMMacTnlLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 14),
    _HwMinMMacTnlLtrNextEgressIdentifier_Type()
)
hwMinMMacTnlLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrNextEgressIdentifier.setStatus("current")
_HwMinMMacTnlLtrRelay_Type = HwDot1agCfmRelayActionFieldValue
_HwMinMMacTnlLtrRelay_Object = MibTableColumn
hwMinMMacTnlLtrRelay = _HwMinMMacTnlLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 15),
    _HwMinMMacTnlLtrRelay_Type()
)
hwMinMMacTnlLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrRelay.setStatus("current")
_HwMinMMacTnlLtrIngress_Type = HwDot1agCfmIngressActionFieldValue
_HwMinMMacTnlLtrIngress_Object = MibTableColumn
hwMinMMacTnlLtrIngress = _HwMinMMacTnlLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 16),
    _HwMinMMacTnlLtrIngress_Type()
)
hwMinMMacTnlLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrIngress.setStatus("current")
_HwMinMMacTnlLtrIngressMac_Type = MacAddress
_HwMinMMacTnlLtrIngressMac_Object = MibTableColumn
hwMinMMacTnlLtrIngressMac = _HwMinMMacTnlLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 17),
    _HwMinMMacTnlLtrIngressMac_Type()
)
hwMinMMacTnlLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrIngressMac.setStatus("current")
_HwMinMMacTnlLtrIngressPortIdSubtype_Type = HwLldpPortIdSubtype
_HwMinMMacTnlLtrIngressPortIdSubtype_Object = MibTableColumn
hwMinMMacTnlLtrIngressPortIdSubtype = _HwMinMMacTnlLtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 18),
    _HwMinMMacTnlLtrIngressPortIdSubtype_Type()
)
hwMinMMacTnlLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrIngressPortIdSubtype.setStatus("current")
_HwMinMMacTnlLtrIngressPortId_Type = HwLldpPortId
_HwMinMMacTnlLtrIngressPortId_Object = MibTableColumn
hwMinMMacTnlLtrIngressPortId = _HwMinMMacTnlLtrIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 19),
    _HwMinMMacTnlLtrIngressPortId_Type()
)
hwMinMMacTnlLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrIngressPortId.setStatus("current")
_HwMinMMacTnlLtrEgress_Type = HwDot1agCfmEgressActionFieldValue
_HwMinMMacTnlLtrEgress_Object = MibTableColumn
hwMinMMacTnlLtrEgress = _HwMinMMacTnlLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 20),
    _HwMinMMacTnlLtrEgress_Type()
)
hwMinMMacTnlLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrEgress.setStatus("current")
_HwMinMMacTnlLtrEgressMac_Type = MacAddress
_HwMinMMacTnlLtrEgressMac_Object = MibTableColumn
hwMinMMacTnlLtrEgressMac = _HwMinMMacTnlLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 21),
    _HwMinMMacTnlLtrEgressMac_Type()
)
hwMinMMacTnlLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrEgressMac.setStatus("current")
_HwMinMMacTnlLtrEgressPortIdSubtype_Type = HwLldpPortIdSubtype
_HwMinMMacTnlLtrEgressPortIdSubtype_Object = MibTableColumn
hwMinMMacTnlLtrEgressPortIdSubtype = _HwMinMMacTnlLtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 22),
    _HwMinMMacTnlLtrEgressPortIdSubtype_Type()
)
hwMinMMacTnlLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrEgressPortIdSubtype.setStatus("current")
_HwMinMMacTnlLtrEgressPortId_Type = HwLldpPortId
_HwMinMMacTnlLtrEgressPortId_Object = MibTableColumn
hwMinMMacTnlLtrEgressPortId = _HwMinMMacTnlLtrEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 2, 5, 1, 23),
    _HwMinMMacTnlLtrEgressPortId_Type()
)
hwMinMMacTnlLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMMacTnlLtrEgressPortId.setStatus("current")
_HwMinMMacTnlApsObjects_ObjectIdentity = ObjectIdentity
hwMinMMacTnlApsObjects = _HwMinMMacTnlApsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3)
)
_HwMinMMacTnlApsCfgTable_Object = MibTable
hwMinMMacTnlApsCfgTable = _HwMinMMacTnlApsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hwMinMMacTnlApsCfgTable.setStatus("current")
_HwMinMMacTnlApsCfgEntry_Object = MibTableRow
hwMinMMacTnlApsCfgEntry = _HwMinMMacTnlApsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1)
)
hwMinMMacTnlApsCfgEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMMacTnlApsCfgEntry.setStatus("current")
_HwMinMProtectMacTnlIndex_Type = Unsigned32
_HwMinMProtectMacTnlIndex_Object = MibTableColumn
hwMinMProtectMacTnlIndex = _HwMinMProtectMacTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 11),
    _HwMinMProtectMacTnlIndex_Type()
)
hwMinMProtectMacTnlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMProtectMacTnlIndex.setStatus("current")


class _HwMinMProtectMacTnlName_Type(OctetString):
    """Custom type hwMinMProtectMacTnlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMinMProtectMacTnlName_Type.__name__ = "OctetString"
_HwMinMProtectMacTnlName_Object = MibTableColumn
hwMinMProtectMacTnlName = _HwMinMProtectMacTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 12),
    _HwMinMProtectMacTnlName_Type()
)
hwMinMProtectMacTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectMacTnlName.setStatus("current")
_HwMinMProtectMacTnlDMac_Type = MacAddress
_HwMinMProtectMacTnlDMac_Object = MibTableColumn
hwMinMProtectMacTnlDMac = _HwMinMProtectMacTnlDMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 13),
    _HwMinMProtectMacTnlDMac_Type()
)
hwMinMProtectMacTnlDMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMProtectMacTnlDMac.setStatus("current")
_HwMinMProtectMacTnlBVlanID_Type = VlanId
_HwMinMProtectMacTnlBVlanID_Object = MibTableColumn
hwMinMProtectMacTnlBVlanID = _HwMinMProtectMacTnlBVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 14),
    _HwMinMProtectMacTnlBVlanID_Type()
)
hwMinMProtectMacTnlBVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMProtectMacTnlBVlanID.setStatus("current")


class _HwMinMProtectApsSwitchMode_Type(HWProtectMode):
    """Custom type hwMinMProtectApsSwitchMode based on HWProtectMode"""
    defaultValue = 3


_HwMinMProtectApsSwitchMode_Object = MibTableColumn
hwMinMProtectApsSwitchMode = _HwMinMProtectApsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 15),
    _HwMinMProtectApsSwitchMode_Type()
)
hwMinMProtectApsSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectApsSwitchMode.setStatus("current")


class _HwMinMProtectProtocolApsEnable_Type(EnabledStatus):
    """Custom type hwMinMProtectProtocolApsEnable based on EnabledStatus"""
    defaultValue = 2


_HwMinMProtectProtocolApsEnable_Object = MibTableColumn
hwMinMProtectProtocolApsEnable = _HwMinMProtectProtocolApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 16),
    _HwMinMProtectProtocolApsEnable_Type()
)
hwMinMProtectProtocolApsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectProtocolApsEnable.setStatus("current")


class _HwMinMProtectApsFastInterval_Type(HWApsInterval):
    """Custom type hwMinMProtectApsFastInterval based on HWApsInterval"""
    defaultValue = 1


_HwMinMProtectApsFastInterval_Object = MibTableColumn
hwMinMProtectApsFastInterval = _HwMinMProtectApsFastInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 17),
    _HwMinMProtectApsFastInterval_Type()
)
hwMinMProtectApsFastInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectApsFastInterval.setStatus("current")


class _HwMinMProtectHoldoffTime_Type(Integer32):
    """Custom type hwMinMProtectHoldoffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMinMProtectHoldoffTime_Type.__name__ = "Integer32"
_HwMinMProtectHoldoffTime_Object = MibTableColumn
hwMinMProtectHoldoffTime = _HwMinMProtectHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 18),
    _HwMinMProtectHoldoffTime_Type()
)
hwMinMProtectHoldoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectHoldoffTime.setStatus("current")
_HwMinMProtectRevMode_Type = EnabledStatus
_HwMinMProtectRevMode_Object = MibTableColumn
hwMinMProtectRevMode = _HwMinMProtectRevMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 19),
    _HwMinMProtectRevMode_Type()
)
hwMinMProtectRevMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectRevMode.setStatus("current")


class _HwMinMProtectRevWtrTime_Type(Integer32):
    """Custom type hwMinMProtectRevWtrTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwMinMProtectRevWtrTime_Type.__name__ = "Integer32"
_HwMinMProtectRevWtrTime_Object = MibTableColumn
hwMinMProtectRevWtrTime = _HwMinMProtectRevWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 20),
    _HwMinMProtectRevWtrTime_Type()
)
hwMinMProtectRevWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectRevWtrTime.setStatus("current")
_HwMinMProtectSwitchOperation_Type = HWSwitchOperation
_HwMinMProtectSwitchOperation_Object = MibTableColumn
hwMinMProtectSwitchOperation = _HwMinMProtectSwitchOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 21),
    _HwMinMProtectSwitchOperation_Type()
)
hwMinMProtectSwitchOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectSwitchOperation.setStatus("current")
_HwMinMProtectProtocol_Type = HWProtectProtocol
_HwMinMProtectProtocol_Object = MibTableColumn
hwMinMProtectProtocol = _HwMinMProtectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 22),
    _HwMinMProtectProtocol_Type()
)
hwMinMProtectProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectProtocol.setStatus("current")
_HwMinMProtectRowStatus_Type = RowStatus
_HwMinMProtectRowStatus_Object = MibTableColumn
hwMinMProtectRowStatus = _HwMinMProtectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 2, 3, 1, 1, 51),
    _HwMinMProtectRowStatus_Type()
)
hwMinMProtectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMProtectRowStatus.setStatus("current")
_HwMinMSIObjects_ObjectIdentity = ObjectIdentity
hwMinMSIObjects = _HwMinMSIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3)
)
_HwMinMSIIndexNext_Type = Unsigned32
_HwMinMSIIndexNext_Object = MibScalar
hwMinMSIIndexNext = _HwMinMSIIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 1),
    _HwMinMSIIndexNext_Type()
)
hwMinMSIIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIIndexNext.setStatus("current")
_HwMinMSICfgTable_Object = MibTable
hwMinMSICfgTable = _HwMinMSICfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwMinMSICfgTable.setStatus("current")
_HwMinMSICfgEntry_Object = MibTableRow
hwMinMSICfgEntry = _HwMinMSICfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1)
)
hwMinMSICfgEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMSIIndex"),
)
if mibBuilder.loadTexts:
    hwMinMSICfgEntry.setStatus("current")
_HwMinMSIIndex_Type = Unsigned32
_HwMinMSIIndex_Object = MibTableColumn
hwMinMSIIndex = _HwMinMSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 1),
    _HwMinMSIIndex_Type()
)
hwMinMSIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIIndex.setStatus("current")


class _HwMinMSIID_Type(Integer32):
    """Custom type hwMinMSIID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_HwMinMSIID_Type.__name__ = "Integer32"
_HwMinMSIID_Object = MibTableColumn
hwMinMSIID = _HwMinMSIID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 11),
    _HwMinMSIID_Type()
)
hwMinMSIID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIID.setStatus("current")


class _HwMinMSIName_Type(OctetString):
    """Custom type hwMinMSIName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMinMSIName_Type.__name__ = "OctetString"
_HwMinMSIName_Object = MibTableColumn
hwMinMSIName = _HwMinMSIName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 12),
    _HwMinMSIName_Type()
)
hwMinMSIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIName.setStatus("current")


class _HwMinMSIServiceType_Type(HWServiceType):
    """Custom type hwMinMSIServiceType based on HWServiceType"""
    defaultValue = 2


_HwMinMSIServiceType_Object = MibTableColumn
hwMinMSIServiceType = _HwMinMSIServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 13),
    _HwMinMSIServiceType_Type()
)
hwMinMSIServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIServiceType.setStatus("current")


class _HwMinMSIPriorityTrust8021p_Type(TruthValue):
    """Custom type hwMinMSIPriorityTrust8021p based on TruthValue"""
    defaultValue = 2


_HwMinMSIPriorityTrust8021p_Object = MibTableColumn
hwMinMSIPriorityTrust8021p = _HwMinMSIPriorityTrust8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 14),
    _HwMinMSIPriorityTrust8021p_Type()
)
hwMinMSIPriorityTrust8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIPriorityTrust8021p.setStatus("current")


class _HwMinMSIPriorityValue_Type(Integer32):
    """Custom type hwMinMSIPriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwMinMSIPriorityValue_Type.__name__ = "Integer32"
_HwMinMSIPriorityValue_Object = MibTableColumn
hwMinMSIPriorityValue = _HwMinMSIPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 15),
    _HwMinMSIPriorityValue_Type()
)
hwMinMSIPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIPriorityValue.setStatus("current")


class _HwMinMSIInterfaceType_Type(HWInterfaceType):
    """Custom type hwMinMSIInterfaceType based on HWInterfaceType"""
    defaultValue = 3


_HwMinMSIInterfaceType_Object = MibTableColumn
hwMinMSIInterfaceType = _HwMinMSIInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 16),
    _HwMinMSIInterfaceType_Type()
)
hwMinMSIInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIInterfaceType.setStatus("current")
_HwMinMSIAdminStatus_Type = HWAdminStatus
_HwMinMSIAdminStatus_Object = MibTableColumn
hwMinMSIAdminStatus = _HwMinMSIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 17),
    _HwMinMSIAdminStatus_Type()
)
hwMinMSIAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIAdminStatus.setStatus("current")
_HwMinMSIOperStatus_Type = HWOperStatus
_HwMinMSIOperStatus_Object = MibTableColumn
hwMinMSIOperStatus = _HwMinMSIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 18),
    _HwMinMSIOperStatus_Type()
)
hwMinMSIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIOperStatus.setStatus("current")


class _HwMinMSIMacLearningEnable_Type(EnabledStatus):
    """Custom type hwMinMSIMacLearningEnable based on EnabledStatus"""
    defaultValue = 1


_HwMinMSIMacLearningEnable_Object = MibTableColumn
hwMinMSIMacLearningEnable = _HwMinMSIMacLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 19),
    _HwMinMSIMacLearningEnable_Type()
)
hwMinMSIMacLearningEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMacLearningEnable.setStatus("current")
_HwMinMSIMacLimitAction_Type = HWProcessBehavior
_HwMinMSIMacLimitAction_Object = MibTableColumn
hwMinMSIMacLimitAction = _HwMinMSIMacLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 20),
    _HwMinMSIMacLimitAction_Type()
)
hwMinMSIMacLimitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMacLimitAction.setStatus("current")
_HwMinMSIMacLimitAlarm_Type = EnabledStatus
_HwMinMSIMacLimitAlarm_Object = MibTableColumn
hwMinMSIMacLimitAlarm = _HwMinMSIMacLimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 21),
    _HwMinMSIMacLimitAlarm_Type()
)
hwMinMSIMacLimitAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMacLimitAlarm.setStatus("current")


class _HwMinMSIMacLimitMaxinum_Type(Integer32):
    """Custom type hwMinMSIMacLimitMaxinum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMinMSIMacLimitMaxinum_Type.__name__ = "Integer32"
_HwMinMSIMacLimitMaxinum_Object = MibTableColumn
hwMinMSIMacLimitMaxinum = _HwMinMSIMacLimitMaxinum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 22),
    _HwMinMSIMacLimitMaxinum_Type()
)
hwMinMSIMacLimitMaxinum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMacLimitMaxinum.setStatus("current")


class _HwMinMSIL2CtrlProProcess_Type(Bits):
    """Custom type hwMinMSIL2CtrlProProcess based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("all", 0),
          ("dot1ag", 5),
          ("dot3ah", 4),
          ("lacp", 3),
          ("lldp", 2),
          ("stp", 1))
    )

_HwMinMSIL2CtrlProProcess_Type.__name__ = "Bits"
_HwMinMSIL2CtrlProProcess_Object = MibTableColumn
hwMinMSIL2CtrlProProcess = _HwMinMSIL2CtrlProProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 23),
    _HwMinMSIL2CtrlProProcess_Type()
)
hwMinMSIL2CtrlProProcess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIL2CtrlProProcess.setStatus("current")


class _HwMinMSIUnknownUnicastEnbale_Type(EnabledStatus):
    """Custom type hwMinMSIUnknownUnicastEnbale based on EnabledStatus"""
    defaultValue = 1


_HwMinMSIUnknownUnicastEnbale_Object = MibTableColumn
hwMinMSIUnknownUnicastEnbale = _HwMinMSIUnknownUnicastEnbale_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 24),
    _HwMinMSIUnknownUnicastEnbale_Type()
)
hwMinMSIUnknownUnicastEnbale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIUnknownUnicastEnbale.setStatus("current")


class _HwMinMSIMulticastEnable_Type(EnabledStatus):
    """Custom type hwMinMSIMulticastEnable based on EnabledStatus"""
    defaultValue = 1


_HwMinMSIMulticastEnable_Object = MibTableColumn
hwMinMSIMulticastEnable = _HwMinMSIMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 25),
    _HwMinMSIMulticastEnable_Type()
)
hwMinMSIMulticastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMulticastEnable.setStatus("current")


class _HwMinMSIBroadcastEnable_Type(EnabledStatus):
    """Custom type hwMinMSIBroadcastEnable based on EnabledStatus"""
    defaultValue = 1


_HwMinMSIBroadcastEnable_Object = MibTableColumn
hwMinMSIBroadcastEnable = _HwMinMSIBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 26),
    _HwMinMSIBroadcastEnable_Type()
)
hwMinMSIBroadcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIBroadcastEnable.setStatus("current")


class _HwMinMSIDescription_Type(OctetString):
    """Custom type hwMinMSIDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HwMinMSIDescription_Type.__name__ = "OctetString"
_HwMinMSIDescription_Object = MibTableColumn
hwMinMSIDescription = _HwMinMSIDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 27),
    _HwMinMSIDescription_Type()
)
hwMinMSIDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIDescription.setStatus("current")


class _HwMinMSIStatisticsEnable_Type(EnabledStatus):
    """Custom type hwMinMSIStatisticsEnable based on EnabledStatus"""
    defaultValue = 2


_HwMinMSIStatisticsEnable_Object = MibTableColumn
hwMinMSIStatisticsEnable = _HwMinMSIStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 28),
    _HwMinMSIStatisticsEnable_Type()
)
hwMinMSIStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMinMSIStatisticsEnable.setStatus("current")
_HwMinMSIStatisticsReset_Type = EnabledStatus
_HwMinMSIStatisticsReset_Object = MibTableColumn
hwMinMSIStatisticsReset = _HwMinMSIStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 29),
    _HwMinMSIStatisticsReset_Type()
)
hwMinMSIStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStatisticsReset.setStatus("current")


class _HwMinMSIFcsTransparentEnable_Type(EnabledStatus):
    """Custom type hwMinMSIFcsTransparentEnable based on EnabledStatus"""
    defaultValue = 2


_HwMinMSIFcsTransparentEnable_Object = MibTableColumn
hwMinMSIFcsTransparentEnable = _HwMinMSIFcsTransparentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 30),
    _HwMinMSIFcsTransparentEnable_Type()
)
hwMinMSIFcsTransparentEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIFcsTransparentEnable.setStatus("current")
_HwMinMSIIngressPriorityValue_Type = Integer32
_HwMinMSIIngressPriorityValue_Object = MibTableColumn
hwMinMSIIngressPriorityValue = _HwMinMSIIngressPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 31),
    _HwMinMSIIngressPriorityValue_Type()
)
hwMinMSIIngressPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIIngressPriorityValue.setStatus("current")


class _HwMinMSIEgressPriorityTrustBTag_Type(TruthValue):
    """Custom type hwMinMSIEgressPriorityTrustBTag based on TruthValue"""
    defaultValue = 2


_HwMinMSIEgressPriorityTrustBTag_Object = MibTableColumn
hwMinMSIEgressPriorityTrustBTag = _HwMinMSIEgressPriorityTrustBTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 32),
    _HwMinMSIEgressPriorityTrustBTag_Type()
)
hwMinMSIEgressPriorityTrustBTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIEgressPriorityTrustBTag.setStatus("current")


class _HwMinMSIIngressDeiValue_Type(Integer32):
    """Custom type hwMinMSIIngressDeiValue based on Integer32"""
    defaultValue = 1


_HwMinMSIIngressDeiValue_Object = MibTableColumn
hwMinMSIIngressDeiValue = _HwMinMSIIngressDeiValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 33),
    _HwMinMSIIngressDeiValue_Type()
)
hwMinMSIIngressDeiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIIngressDeiValue.setStatus("current")


class _HwMinMSIEgressDeiTrustBDei_Type(TruthValue):
    """Custom type hwMinMSIEgressDeiTrustBDei based on TruthValue"""
    defaultValue = 2


_HwMinMSIEgressDeiTrustBDei_Object = MibTableColumn
hwMinMSIEgressDeiTrustBDei = _HwMinMSIEgressDeiTrustBDei_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 34),
    _HwMinMSIEgressDeiTrustBDei_Type()
)
hwMinMSIEgressDeiTrustBDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIEgressDeiTrustBDei.setStatus("current")


class _HwMinMSIIsolateAll_Type(EnabledStatus):
    """Custom type hwMinMSIIsolateAll based on EnabledStatus"""
    defaultValue = 2


_HwMinMSIIsolateAll_Object = MibTableColumn
hwMinMSIIsolateAll = _HwMinMSIIsolateAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 35),
    _HwMinMSIIsolateAll_Type()
)
hwMinMSIIsolateAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIIsolateAll.setStatus("current")
_HwMinMSIRowStatus_Type = RowStatus
_HwMinMSIRowStatus_Object = MibTableColumn
hwMinMSIRowStatus = _HwMinMSIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 2, 1, 51),
    _HwMinMSIRowStatus_Type()
)
hwMinMSIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIRowStatus.setStatus("current")
_HwMinMSIMappingTable_Object = MibTable
hwMinMSIMappingTable = _HwMinMSIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwMinMSIMappingTable.setStatus("current")
_HwMinMSIMappingEntry_Object = MibTableRow
hwMinMSIMappingEntry = _HwMinMSIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1)
)
hwMinMSIMappingEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMSIIndex"),
    (0, "HUAWEI-MINM-MIB", "hwMinMSIMappingIfIndex"),
    (0, "HUAWEI-MINM-MIB", "hwMinMSIMappingVlanPriority"),
    (0, "HUAWEI-MINM-MIB", "hwMinMSIMappingGlobalVlanID"),
)
if mibBuilder.loadTexts:
    hwMinMSIMappingEntry.setStatus("current")
_HwMinMSIMappingIfIndex_Type = InterfaceIndexOrZero
_HwMinMSIMappingIfIndex_Object = MibTableColumn
hwMinMSIMappingIfIndex = _HwMinMSIMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 1),
    _HwMinMSIMappingIfIndex_Type()
)
hwMinMSIMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIMappingIfIndex.setStatus("current")


class _HwMinMSIMappingVlanPriority_Type(Integer32):
    """Custom type hwMinMSIMappingVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwMinMSIMappingVlanPriority_Type.__name__ = "Integer32"
_HwMinMSIMappingVlanPriority_Object = MibTableColumn
hwMinMSIMappingVlanPriority = _HwMinMSIMappingVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 2),
    _HwMinMSIMappingVlanPriority_Type()
)
hwMinMSIMappingVlanPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIMappingVlanPriority.setStatus("current")
_HwMinMSIMappingGlobalVlanID_Type = VlanIdOrNone
_HwMinMSIMappingGlobalVlanID_Object = MibTableColumn
hwMinMSIMappingGlobalVlanID = _HwMinMSIMappingGlobalVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 3),
    _HwMinMSIMappingGlobalVlanID_Type()
)
hwMinMSIMappingGlobalVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIMappingGlobalVlanID.setStatus("current")


class _HwMinMSIMappingVlanListLow_Type(VlanList):
    """Custom type hwMinMSIMappingVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwMinMSIMappingVlanListLow_Type.__name__ = "VlanList"
_HwMinMSIMappingVlanListLow_Object = MibTableColumn
hwMinMSIMappingVlanListLow = _HwMinMSIMappingVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 11),
    _HwMinMSIMappingVlanListLow_Type()
)
hwMinMSIMappingVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMappingVlanListLow.setStatus("current")


class _HwMinMSIMappingVlanListHigh_Type(VlanList):
    """Custom type hwMinMSIMappingVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwMinMSIMappingVlanListHigh_Type.__name__ = "VlanList"
_HwMinMSIMappingVlanListHigh_Object = MibTableColumn
hwMinMSIMappingVlanListHigh = _HwMinMSIMappingVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 12),
    _HwMinMSIMappingVlanListHigh_Type()
)
hwMinMSIMappingVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMappingVlanListHigh.setStatus("current")


class _HwMinMSIMappingUserIsolate_Type(EnabledStatus):
    """Custom type hwMinMSIMappingUserIsolate based on EnabledStatus"""
    defaultValue = 2


_HwMinMSIMappingUserIsolate_Object = MibTableColumn
hwMinMSIMappingUserIsolate = _HwMinMSIMappingUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 13),
    _HwMinMSIMappingUserIsolate_Type()
)
hwMinMSIMappingUserIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMappingUserIsolate.setStatus("current")
_HwMinMSIMappingRowStatus_Type = RowStatus
_HwMinMSIMappingRowStatus_Object = MibTableColumn
hwMinMSIMappingRowStatus = _HwMinMSIMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 3, 1, 51),
    _HwMinMSIMappingRowStatus_Type()
)
hwMinMSIMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIMappingRowStatus.setStatus("current")
_HwMinMSIBindMacTnlTable_Object = MibTable
hwMinMSIBindMacTnlTable = _HwMinMSIBindMacTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwMinMSIBindMacTnlTable.setStatus("current")
_HwMinMSIBindMacTnlEntry_Object = MibTableRow
hwMinMSIBindMacTnlEntry = _HwMinMSIBindMacTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 4, 1)
)
hwMinMSIBindMacTnlEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMSIIndex"),
    (0, "HUAWEI-MINM-MIB", "hwMinMSIBindMacTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMinMSIBindMacTnlEntry.setStatus("current")
_HwMinMSIBindMacTnlIndex_Type = Unsigned32
_HwMinMSIBindMacTnlIndex_Object = MibTableColumn
hwMinMSIBindMacTnlIndex = _HwMinMSIBindMacTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 4, 1, 1),
    _HwMinMSIBindMacTnlIndex_Type()
)
hwMinMSIBindMacTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIBindMacTnlIndex.setStatus("current")
_HwMinMSIBindMacTnlRowStatus_Type = RowStatus
_HwMinMSIBindMacTnlRowStatus_Object = MibTableColumn
hwMinMSIBindMacTnlRowStatus = _HwMinMSIBindMacTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 4, 1, 51),
    _HwMinMSIBindMacTnlRowStatus_Type()
)
hwMinMSIBindMacTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIBindMacTnlRowStatus.setStatus("current")
_HwMinMSIStatisticsTable_Object = MibTable
hwMinMSIStatisticsTable = _HwMinMSIStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hwMinMSIStatisticsTable.setStatus("current")
_HwMinMSIStatisticsEntry_Object = MibTableRow
hwMinMSIStatisticsEntry = _HwMinMSIStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5, 1)
)
hwMinMSIStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMSIIndex"),
)
if mibBuilder.loadTexts:
    hwMinMSIStatisticsEntry.setStatus("current")
_HwMinMSIInPackets_Type = Counter64
_HwMinMSIInPackets_Object = MibTableColumn
hwMinMSIInPackets = _HwMinMSIInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5, 1, 11),
    _HwMinMSIInPackets_Type()
)
hwMinMSIInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIInPackets.setStatus("current")
_HwMinMSIInBytes_Type = Counter64
_HwMinMSIInBytes_Object = MibTableColumn
hwMinMSIInBytes = _HwMinMSIInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5, 1, 12),
    _HwMinMSIInBytes_Type()
)
hwMinMSIInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIInBytes.setStatus("current")
_HwMinMSIOutPackets_Type = Counter64
_HwMinMSIOutPackets_Object = MibTableColumn
hwMinMSIOutPackets = _HwMinMSIOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5, 1, 13),
    _HwMinMSIOutPackets_Type()
)
hwMinMSIOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIOutPackets.setStatus("current")
_HwMinMSIOutBytes_Type = Counter64
_HwMinMSIOutBytes_Object = MibTableColumn
hwMinMSIOutBytes = _HwMinMSIOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 5, 1, 14),
    _HwMinMSIOutBytes_Type()
)
hwMinMSIOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinMSIOutBytes.setStatus("current")
_HwMinMSIStaticMacFwdTable_Object = MibTable
hwMinMSIStaticMacFwdTable = _HwMinMSIStaticMacFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdTable.setStatus("current")
_HwMinMSIStaticMacFwdEntry_Object = MibTableRow
hwMinMSIStaticMacFwdEntry = _HwMinMSIStaticMacFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1)
)
hwMinMSIStaticMacFwdEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwMinMSIIndex"),
    (0, "HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdCDMac"),
)
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdEntry.setStatus("current")
_HwMinMSIStaticMacFwdCDMac_Type = MacAddress
_HwMinMSIStaticMacFwdCDMac_Object = MibTableColumn
hwMinMSIStaticMacFwdCDMac = _HwMinMSIStaticMacFwdCDMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 1),
    _HwMinMSIStaticMacFwdCDMac_Type()
)
hwMinMSIStaticMacFwdCDMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdCDMac.setStatus("current")


class _HwMinMSIStaticMacFwdMacTnlName_Type(OctetString):
    """Custom type hwMinMSIStaticMacFwdMacTnlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMinMSIStaticMacFwdMacTnlName_Type.__name__ = "OctetString"
_HwMinMSIStaticMacFwdMacTnlName_Object = MibTableColumn
hwMinMSIStaticMacFwdMacTnlName = _HwMinMSIStaticMacFwdMacTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 11),
    _HwMinMSIStaticMacFwdMacTnlName_Type()
)
hwMinMSIStaticMacFwdMacTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdMacTnlName.setStatus("current")
_HwMinMSIStaticMacFwdOutgoingIfIndex_Type = InterfaceIndexOrZero
_HwMinMSIStaticMacFwdOutgoingIfIndex_Object = MibTableColumn
hwMinMSIStaticMacFwdOutgoingIfIndex = _HwMinMSIStaticMacFwdOutgoingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 12),
    _HwMinMSIStaticMacFwdOutgoingIfIndex_Type()
)
hwMinMSIStaticMacFwdOutgoingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdOutgoingIfIndex.setStatus("current")
_HwMinMSIStaticMacFwdVlanID_Type = VlanIdOrNone
_HwMinMSIStaticMacFwdVlanID_Object = MibTableColumn
hwMinMSIStaticMacFwdVlanID = _HwMinMSIStaticMacFwdVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 13),
    _HwMinMSIStaticMacFwdVlanID_Type()
)
hwMinMSIStaticMacFwdVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdVlanID.setStatus("current")
_HwMinMSIStaticMacFwdType_Type = HWStaticMacFwdType
_HwMinMSIStaticMacFwdType_Object = MibTableColumn
hwMinMSIStaticMacFwdType = _HwMinMSIStaticMacFwdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 14),
    _HwMinMSIStaticMacFwdType_Type()
)
hwMinMSIStaticMacFwdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdType.setStatus("current")
_HwMinMSIStaticMacFwdRowStatus_Type = RowStatus
_HwMinMSIStaticMacFwdRowStatus_Object = MibTableColumn
hwMinMSIStaticMacFwdRowStatus = _HwMinMSIStaticMacFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 6, 1, 51),
    _HwMinMSIStaticMacFwdRowStatus_Type()
)
hwMinMSIStaticMacFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMinMSIStaticMacFwdRowStatus.setStatus("current")
_HwSINameToIndexMappingTable_Object = MibTable
hwSINameToIndexMappingTable = _HwSINameToIndexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hwSINameToIndexMappingTable.setStatus("current")
_HwSINameToIndexMappingEntry_Object = MibTableRow
hwSINameToIndexMappingEntry = _HwSINameToIndexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 7, 1)
)
hwSINameToIndexMappingEntry.setIndexNames(
    (0, "HUAWEI-MINM-MIB", "hwSIName"),
)
if mibBuilder.loadTexts:
    hwSINameToIndexMappingEntry.setStatus("current")


class _HwSIName_Type(OctetString):
    """Custom type hwSIName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwSIName_Type.__name__ = "OctetString"
_HwSIName_Object = MibTableColumn
hwSIName = _HwSIName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 7, 1, 1),
    _HwSIName_Type()
)
hwSIName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSIName.setStatus("current")
_HwSIIndex_Type = Unsigned32
_HwSIIndex_Object = MibTableColumn
hwSIIndex = _HwSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 1, 3, 7, 1, 11),
    _HwSIIndex_Type()
)
hwSIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIIndex.setStatus("current")
_HwMinMNotifications_ObjectIdentity = ObjectIdentity
hwMinMNotifications = _HwMinMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2)
)
_HwMinMConformance_ObjectIdentity = ObjectIdentity
hwMinMConformance = _HwMinMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3)
)
_HwMinMGroups_ObjectIdentity = ObjectIdentity
hwMinMGroups = _HwMinMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1)
)

# Managed Objects groups

hwMinMSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 1)
)
hwMinMSystemGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMVirtualMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanListLow"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanListHigh"),
        ("HUAWEI-MINM-MIB", "hwMinMTrapEnable"))
)
if mibBuilder.loadTexts:
    hwMinMSystemGroup.setStatus("current")

hwMinMMacTnlCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 2)
)
hwMinMMacTnlCfgGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMVirtualMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanListLow"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanListHigh"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlIndexNext"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanType"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlPriorityValue"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOutgoingIfIndex"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSplitHorizonEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOperStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDescription"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMacTnlIndex"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlStatisticsReset"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlPriorityTrustITag"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDeiTrustIDei"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDeiValue"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCfgGroup.setStatus("current")

hwMinMMacTnlStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 3)
)
hwMinMMacTnlStatisticsGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlInPackets"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlInBytes"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOutPackets"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOutBytes"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlStatisticsGroup.setStatus("current")

hwMinMMacTnlOAMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 4)
)
hwMinMMacTnlOAMGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlCfmEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlCCInterval"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSomeRMepCcmDefect"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSomeRdiDefect"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlCcReceiveEnabled"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlCCRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmTimeStamp"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmTimeOut"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmTimes"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmSize"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbrIn"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlMacPingRTTMin"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlMacPingRTTMax"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlMacPingRTTAvg"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlMacPingPacketLossRatio"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbmResult"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLbRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmTimeStamp"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmTimeOut"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmTtl"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmFlags"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmSeqNumber"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmEgressIdentifier"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmResult"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtmRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrTtl"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrForwarded"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrLastEgressIdentifier"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrNextEgressIdentifier"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrRelay"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrIngress"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrIngressMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrIngressPortIdSubtype"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrIngressPortId"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrEgress"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrEgressMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrEgressPortIdSubtype"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlLtrEgressPortId"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlOAMGroup.setStatus("current")

hwMinMMacTnlApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 5)
)
hwMinMMacTnlApsGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectApsSwitchMode"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectProtocolApsEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectApsFastInterval"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectHoldoffTime"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectRevMode"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectRevWtrTime"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectSwitchOperation"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectProtocol"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlIndex"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlApsGroup.setStatus("current")

hwMinMSICfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 6)
)
hwMinMSICfgGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMSIIndexNext"),
        ("HUAWEI-MINM-MIB", "hwMinMSIID"),
        ("HUAWEI-MINM-MIB", "hwMinMSIName"),
        ("HUAWEI-MINM-MIB", "hwMinMSIServiceType"),
        ("HUAWEI-MINM-MIB", "hwMinMSIPriorityTrust8021p"),
        ("HUAWEI-MINM-MIB", "hwMinMSIPriorityValue"),
        ("HUAWEI-MINM-MIB", "hwMinMSIInterfaceType"),
        ("HUAWEI-MINM-MIB", "hwMinMSIAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIOperStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLearningEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLimitAction"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLimitAlarm"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLimitMaxinum"),
        ("HUAWEI-MINM-MIB", "hwMinMSIL2CtrlProProcess"),
        ("HUAWEI-MINM-MIB", "hwMinMSIUnknownUnicastEnbale"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMulticastEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMSIBroadcastEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMSIDescription"),
        ("HUAWEI-MINM-MIB", "hwMinMSIRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdOutgoingIfIndex"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdType"),
        ("HUAWEI-MINM-MIB", "hwMinMSIFcsTransparentEnable"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdRowStatus"),
        ("HUAWEI-MINM-MIB", "hwSIIndex"),
        ("HUAWEI-MINM-MIB", "hwMinMSIBindMacTnlRowStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStaticMacFwdMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMappingVlanListLow"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMappingVlanListHigh"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMappingUserIsolate"),
        ("HUAWEI-MINM-MIB", "hwMinMSIIngressPriorityValue"),
        ("HUAWEI-MINM-MIB", "hwMinMSIEgressPriorityTrustBTag"),
        ("HUAWEI-MINM-MIB", "hwMinMSIIngressDeiValue"),
        ("HUAWEI-MINM-MIB", "hwMinMSIEgressDeiTrustBDei"),
        ("HUAWEI-MINM-MIB", "hwMinMSIIsolateAll"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwMinMSICfgGroup.setStatus("current")

hwMinMSIStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 7)
)
hwMinMSIStatisticsGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMSIInPackets"),
        ("HUAWEI-MINM-MIB", "hwMinMSIInBytes"),
        ("HUAWEI-MINM-MIB", "hwMinMSIOutPackets"),
        ("HUAWEI-MINM-MIB", "hwMinMSIOutBytes"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStatisticsReset"),
        ("HUAWEI-MINM-MIB", "hwMinMSIStatisticsEnable"))
)
if mibBuilder.loadTexts:
    hwMinMSIStatisticsGroup.setStatus("current")


# Notification objects

hwMinMMacTnlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 1)
)
hwMinMMacTnlUp.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOperStatus"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlUp.setStatus(
        "current"
    )

hwMinMMacTnlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 2)
)
hwMinMMacTnlDown.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlOperStatus"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlDown.setStatus(
        "current"
    )

hwMinMSIUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 3)
)
hwMinMSIUp.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMSIID"),
        ("HUAWEI-MINM-MIB", "hwMinMSIName"),
        ("HUAWEI-MINM-MIB", "hwMinMSIAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIOperStatus"))
)
if mibBuilder.loadTexts:
    hwMinMSIUp.setStatus(
        "current"
    )

hwMinMSIDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 4)
)
hwMinMSIDown.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMSIID"),
        ("HUAWEI-MINM-MIB", "hwMinMSIName"),
        ("HUAWEI-MINM-MIB", "hwMinMSIAdminStatus"),
        ("HUAWEI-MINM-MIB", "hwMinMSIOperStatus"))
)
if mibBuilder.loadTexts:
    hwMinMSIDown.setStatus(
        "current"
    )

hwMinMMacTnlCCFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 5)
)
hwMinMMacTnlCCFaultAlarm.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSomeRMepCcmDefect"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSomeRdiDefect"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlCCFaultAlarm.setStatus(
        "current"
    )

hwMinMMacTnlSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 6)
)
hwMinMMacTnlSwitch.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectSwitchOperation"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlSwitch.setStatus(
        "current"
    )

hwMinMMacTnlRevertive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 7)
)
hwMinMMacTnlRevertive.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlName"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlDMac"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectMacTnlBVlanID"),
        ("HUAWEI-MINM-MIB", "hwMinMProtectSwitchOperation"))
)
if mibBuilder.loadTexts:
    hwMinMMacTnlRevertive.setStatus(
        "current"
    )

hwMinMSIMacLimitNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 2, 8)
)
hwMinMSIMacLimitNumRaisingThreshold.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMSIName"),
        ("HUAWEI-MINM-MIB", "hwMinMSIID"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLimitMaxinum"))
)
if mibBuilder.loadTexts:
    hwMinMSIMacLimitNumRaisingThreshold.setStatus(
        "current"
    )


# Notifications groups

hwMinMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 1, 8)
)
hwMinMNotificationGroup.setObjects(
      *(("HUAWEI-MINM-MIB", "hwMinMMacTnlUp"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlDown"),
        ("HUAWEI-MINM-MIB", "hwMinMSIUp"),
        ("HUAWEI-MINM-MIB", "hwMinMSIDown"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlCCFaultAlarm"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlSwitch"),
        ("HUAWEI-MINM-MIB", "hwMinMMacTnlRevertive"),
        ("HUAWEI-MINM-MIB", "hwMinMSIMacLimitNumRaisingThreshold"))
)
if mibBuilder.loadTexts:
    hwMinMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMinMCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 133, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwMinMCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MINM-MIB",
    **{"HWAdminStatus": HWAdminStatus,
       "HWOperStatus": HWOperStatus,
       "HwDot1agCfmCcmInterval": HwDot1agCfmCcmInterval,
       "HwDot1agCfmRelayActionFieldValue": HwDot1agCfmRelayActionFieldValue,
       "HwLldpChassisIdSubtype": HwLldpChassisIdSubtype,
       "HwLldpChassisId": HwLldpChassisId,
       "HwLldpPortIdSubtype": HwLldpPortIdSubtype,
       "HwLldpPortId": HwLldpPortId,
       "HwLldpManAddrIfSubtype": HwLldpManAddrIfSubtype,
       "HwLldpManAddress": HwLldpManAddress,
       "HwDot1agCfmIngressActionFieldValue": HwDot1agCfmIngressActionFieldValue,
       "HwDot1agCfmEgressActionFieldValue": HwDot1agCfmEgressActionFieldValue,
       "HWApsInterval": HWApsInterval,
       "HWProtectMode": HWProtectMode,
       "HWSwitchOperation": HWSwitchOperation,
       "HWProtectProtocol": HWProtectProtocol,
       "HWServiceType": HWServiceType,
       "HWInterfaceType": HWInterfaceType,
       "HWProcessBehavior": HWProcessBehavior,
       "HWStaticMacFwdType": HWStaticMacFwdType,
       "HwDot1agCfmMepIdOrZero": HwDot1agCfmMepIdOrZero,
       "hwMINM": hwMINM,
       "hwMinMMIB": hwMinMMIB,
       "hwMinMObjects": hwMinMObjects,
       "hwMinMSystemObjects": hwMinMSystemObjects,
       "hwMinMVirtualMac": hwMinMVirtualMac,
       "hwMinMMacTnlBVlanListLow": hwMinMMacTnlBVlanListLow,
       "hwMinMMacTnlBVlanListHigh": hwMinMMacTnlBVlanListHigh,
       "hwMinMTrapEnable": hwMinMTrapEnable,
       "hwMinMMacTnlObjects": hwMinMMacTnlObjects,
       "hwMinMMacTnlCfgObjects": hwMinMMacTnlCfgObjects,
       "hwMinMMacTnlIndexNext": hwMinMMacTnlIndexNext,
       "hwMinMMacTnlCfgTable": hwMinMMacTnlCfgTable,
       "hwMinMMacTnlCfgEntry": hwMinMMacTnlCfgEntry,
       "hwMinMMacTnlIndex": hwMinMMacTnlIndex,
       "hwMinMMacTnlName": hwMinMMacTnlName,
       "hwMinMMacTnlDMac": hwMinMMacTnlDMac,
       "hwMinMMacTnlBVlanID": hwMinMMacTnlBVlanID,
       "hwMinMMacTnlBVlanType": hwMinMMacTnlBVlanType,
       "hwMinMMacTnlPriorityValue": hwMinMMacTnlPriorityValue,
       "hwMinMMacTnlOutgoingIfIndex": hwMinMMacTnlOutgoingIfIndex,
       "hwMinMMacTnlSplitHorizonEnable": hwMinMMacTnlSplitHorizonEnable,
       "hwMinMMacTnlAdminStatus": hwMinMMacTnlAdminStatus,
       "hwMinMMacTnlOperStatus": hwMinMMacTnlOperStatus,
       "hwMinMMacTnlDescription": hwMinMMacTnlDescription,
       "hwMinMMacTnlStatisticsReset": hwMinMMacTnlStatisticsReset,
       "hwMinMMacTnlPriorityTrustITag": hwMinMMacTnlPriorityTrustITag,
       "hwMinMMacTnlDeiTrustIDei": hwMinMMacTnlDeiTrustIDei,
       "hwMinMMacTnlDeiValue": hwMinMMacTnlDeiValue,
       "hwMinMMacTnlRowStatus": hwMinMMacTnlRowStatus,
       "hwMinMMacTnlStatisticsTable": hwMinMMacTnlStatisticsTable,
       "hwMinMMacTnlStatisticsEntry": hwMinMMacTnlStatisticsEntry,
       "hwMinMMacTnlInPackets": hwMinMMacTnlInPackets,
       "hwMinMMacTnlInBytes": hwMinMMacTnlInBytes,
       "hwMinMMacTnlOutPackets": hwMinMMacTnlOutPackets,
       "hwMinMMacTnlOutBytes": hwMinMMacTnlOutBytes,
       "hwMacTnlNameToIndexMappingTable": hwMacTnlNameToIndexMappingTable,
       "hwMacTnlNameToIndexMappingEntry": hwMacTnlNameToIndexMappingEntry,
       "hwMacTnlName": hwMacTnlName,
       "hwMacTnlIndex": hwMacTnlIndex,
       "hwMinMMacTnlOamObjects": hwMinMMacTnlOamObjects,
       "hwMinMMacTnlCCTable": hwMinMMacTnlCCTable,
       "hwMinMMacTnlCCEntry": hwMinMMacTnlCCEntry,
       "hwMinMMacTnlCfmEnable": hwMinMMacTnlCfmEnable,
       "hwMinMMacTnlCCInterval": hwMinMMacTnlCCInterval,
       "hwMinMMacTnlSomeRMepCcmDefect": hwMinMMacTnlSomeRMepCcmDefect,
       "hwMinMMacTnlSomeRdiDefect": hwMinMMacTnlSomeRdiDefect,
       "hwMinMMacTnlCcReceiveEnabled": hwMinMMacTnlCcReceiveEnabled,
       "hwMinMMacTnlCCRowStatus": hwMinMMacTnlCCRowStatus,
       "hwMinMMacTnlLbTable": hwMinMMacTnlLbTable,
       "hwMinMMacTnlLbEntry": hwMinMMacTnlLbEntry,
       "hwMinMMacTnlLbmEnable": hwMinMMacTnlLbmEnable,
       "hwMinMMacTnlLbmTimeStamp": hwMinMMacTnlLbmTimeStamp,
       "hwMinMMacTnlLbmTimeOut": hwMinMMacTnlLbmTimeOut,
       "hwMinMMacTnlLbmTimes": hwMinMMacTnlLbmTimes,
       "hwMinMMacTnlLbmSize": hwMinMMacTnlLbmSize,
       "hwMinMMacTnlLbrIn": hwMinMMacTnlLbrIn,
       "hwMinMMacTnlLbmResult": hwMinMMacTnlLbmResult,
       "hwMinMMacTnlLbRowStatus": hwMinMMacTnlLbRowStatus,
       "hwMinMMacTnlLbResultTable": hwMinMMacTnlLbResultTable,
       "hwMinMMacTnlLbResultEntry": hwMinMMacTnlLbResultEntry,
       "hwMinMMacTnlMacPingRTTMin": hwMinMMacTnlMacPingRTTMin,
       "hwMinMMacTnlMacPingRTTMax": hwMinMMacTnlMacPingRTTMax,
       "hwMinMMacTnlMacPingRTTAvg": hwMinMMacTnlMacPingRTTAvg,
       "hwMinMMacTnlMacPingPacketLossRatio": hwMinMMacTnlMacPingPacketLossRatio,
       "hwMinMMacTnlLtmTable": hwMinMMacTnlLtmTable,
       "hwMinMMacTnlLtmEntry": hwMinMMacTnlLtmEntry,
       "hwMinMMacTnlLtmEnable": hwMinMMacTnlLtmEnable,
       "hwMinMMacTnlLtmTimeStamp": hwMinMMacTnlLtmTimeStamp,
       "hwMinMMacTnlLtmTimeOut": hwMinMMacTnlLtmTimeOut,
       "hwMinMMacTnlLtmTtl": hwMinMMacTnlLtmTtl,
       "hwMinMMacTnlLtmFlags": hwMinMMacTnlLtmFlags,
       "hwMinMMacTnlLtmSeqNumber": hwMinMMacTnlLtmSeqNumber,
       "hwMinMMacTnlLtmEgressIdentifier": hwMinMMacTnlLtmEgressIdentifier,
       "hwMinMMacTnlLtmResult": hwMinMMacTnlLtmResult,
       "hwMinMMacTnlLtmRowStatus": hwMinMMacTnlLtmRowStatus,
       "hwMinMMacTnlLtrTable": hwMinMMacTnlLtrTable,
       "hwMinMMacTnlLtrEntry": hwMinMMacTnlLtrEntry,
       "hwMinMMacTnlLtrSeqNumber": hwMinMMacTnlLtrSeqNumber,
       "hwMinMMacTnlLtrReceiveOrder": hwMinMMacTnlLtrReceiveOrder,
       "hwMinMMacTnlLtrTtl": hwMinMMacTnlLtrTtl,
       "hwMinMMacTnlLtrForwarded": hwMinMMacTnlLtrForwarded,
       "hwMinMMacTnlLtrLastEgressIdentifier": hwMinMMacTnlLtrLastEgressIdentifier,
       "hwMinMMacTnlLtrNextEgressIdentifier": hwMinMMacTnlLtrNextEgressIdentifier,
       "hwMinMMacTnlLtrRelay": hwMinMMacTnlLtrRelay,
       "hwMinMMacTnlLtrIngress": hwMinMMacTnlLtrIngress,
       "hwMinMMacTnlLtrIngressMac": hwMinMMacTnlLtrIngressMac,
       "hwMinMMacTnlLtrIngressPortIdSubtype": hwMinMMacTnlLtrIngressPortIdSubtype,
       "hwMinMMacTnlLtrIngressPortId": hwMinMMacTnlLtrIngressPortId,
       "hwMinMMacTnlLtrEgress": hwMinMMacTnlLtrEgress,
       "hwMinMMacTnlLtrEgressMac": hwMinMMacTnlLtrEgressMac,
       "hwMinMMacTnlLtrEgressPortIdSubtype": hwMinMMacTnlLtrEgressPortIdSubtype,
       "hwMinMMacTnlLtrEgressPortId": hwMinMMacTnlLtrEgressPortId,
       "hwMinMMacTnlApsObjects": hwMinMMacTnlApsObjects,
       "hwMinMMacTnlApsCfgTable": hwMinMMacTnlApsCfgTable,
       "hwMinMMacTnlApsCfgEntry": hwMinMMacTnlApsCfgEntry,
       "hwMinMProtectMacTnlIndex": hwMinMProtectMacTnlIndex,
       "hwMinMProtectMacTnlName": hwMinMProtectMacTnlName,
       "hwMinMProtectMacTnlDMac": hwMinMProtectMacTnlDMac,
       "hwMinMProtectMacTnlBVlanID": hwMinMProtectMacTnlBVlanID,
       "hwMinMProtectApsSwitchMode": hwMinMProtectApsSwitchMode,
       "hwMinMProtectProtocolApsEnable": hwMinMProtectProtocolApsEnable,
       "hwMinMProtectApsFastInterval": hwMinMProtectApsFastInterval,
       "hwMinMProtectHoldoffTime": hwMinMProtectHoldoffTime,
       "hwMinMProtectRevMode": hwMinMProtectRevMode,
       "hwMinMProtectRevWtrTime": hwMinMProtectRevWtrTime,
       "hwMinMProtectSwitchOperation": hwMinMProtectSwitchOperation,
       "hwMinMProtectProtocol": hwMinMProtectProtocol,
       "hwMinMProtectRowStatus": hwMinMProtectRowStatus,
       "hwMinMSIObjects": hwMinMSIObjects,
       "hwMinMSIIndexNext": hwMinMSIIndexNext,
       "hwMinMSICfgTable": hwMinMSICfgTable,
       "hwMinMSICfgEntry": hwMinMSICfgEntry,
       "hwMinMSIIndex": hwMinMSIIndex,
       "hwMinMSIID": hwMinMSIID,
       "hwMinMSIName": hwMinMSIName,
       "hwMinMSIServiceType": hwMinMSIServiceType,
       "hwMinMSIPriorityTrust8021p": hwMinMSIPriorityTrust8021p,
       "hwMinMSIPriorityValue": hwMinMSIPriorityValue,
       "hwMinMSIInterfaceType": hwMinMSIInterfaceType,
       "hwMinMSIAdminStatus": hwMinMSIAdminStatus,
       "hwMinMSIOperStatus": hwMinMSIOperStatus,
       "hwMinMSIMacLearningEnable": hwMinMSIMacLearningEnable,
       "hwMinMSIMacLimitAction": hwMinMSIMacLimitAction,
       "hwMinMSIMacLimitAlarm": hwMinMSIMacLimitAlarm,
       "hwMinMSIMacLimitMaxinum": hwMinMSIMacLimitMaxinum,
       "hwMinMSIL2CtrlProProcess": hwMinMSIL2CtrlProProcess,
       "hwMinMSIUnknownUnicastEnbale": hwMinMSIUnknownUnicastEnbale,
       "hwMinMSIMulticastEnable": hwMinMSIMulticastEnable,
       "hwMinMSIBroadcastEnable": hwMinMSIBroadcastEnable,
       "hwMinMSIDescription": hwMinMSIDescription,
       "hwMinMSIStatisticsEnable": hwMinMSIStatisticsEnable,
       "hwMinMSIStatisticsReset": hwMinMSIStatisticsReset,
       "hwMinMSIFcsTransparentEnable": hwMinMSIFcsTransparentEnable,
       "hwMinMSIIngressPriorityValue": hwMinMSIIngressPriorityValue,
       "hwMinMSIEgressPriorityTrustBTag": hwMinMSIEgressPriorityTrustBTag,
       "hwMinMSIIngressDeiValue": hwMinMSIIngressDeiValue,
       "hwMinMSIEgressDeiTrustBDei": hwMinMSIEgressDeiTrustBDei,
       "hwMinMSIIsolateAll": hwMinMSIIsolateAll,
       "hwMinMSIRowStatus": hwMinMSIRowStatus,
       "hwMinMSIMappingTable": hwMinMSIMappingTable,
       "hwMinMSIMappingEntry": hwMinMSIMappingEntry,
       "hwMinMSIMappingIfIndex": hwMinMSIMappingIfIndex,
       "hwMinMSIMappingVlanPriority": hwMinMSIMappingVlanPriority,
       "hwMinMSIMappingGlobalVlanID": hwMinMSIMappingGlobalVlanID,
       "hwMinMSIMappingVlanListLow": hwMinMSIMappingVlanListLow,
       "hwMinMSIMappingVlanListHigh": hwMinMSIMappingVlanListHigh,
       "hwMinMSIMappingUserIsolate": hwMinMSIMappingUserIsolate,
       "hwMinMSIMappingRowStatus": hwMinMSIMappingRowStatus,
       "hwMinMSIBindMacTnlTable": hwMinMSIBindMacTnlTable,
       "hwMinMSIBindMacTnlEntry": hwMinMSIBindMacTnlEntry,
       "hwMinMSIBindMacTnlIndex": hwMinMSIBindMacTnlIndex,
       "hwMinMSIBindMacTnlRowStatus": hwMinMSIBindMacTnlRowStatus,
       "hwMinMSIStatisticsTable": hwMinMSIStatisticsTable,
       "hwMinMSIStatisticsEntry": hwMinMSIStatisticsEntry,
       "hwMinMSIInPackets": hwMinMSIInPackets,
       "hwMinMSIInBytes": hwMinMSIInBytes,
       "hwMinMSIOutPackets": hwMinMSIOutPackets,
       "hwMinMSIOutBytes": hwMinMSIOutBytes,
       "hwMinMSIStaticMacFwdTable": hwMinMSIStaticMacFwdTable,
       "hwMinMSIStaticMacFwdEntry": hwMinMSIStaticMacFwdEntry,
       "hwMinMSIStaticMacFwdCDMac": hwMinMSIStaticMacFwdCDMac,
       "hwMinMSIStaticMacFwdMacTnlName": hwMinMSIStaticMacFwdMacTnlName,
       "hwMinMSIStaticMacFwdOutgoingIfIndex": hwMinMSIStaticMacFwdOutgoingIfIndex,
       "hwMinMSIStaticMacFwdVlanID": hwMinMSIStaticMacFwdVlanID,
       "hwMinMSIStaticMacFwdType": hwMinMSIStaticMacFwdType,
       "hwMinMSIStaticMacFwdRowStatus": hwMinMSIStaticMacFwdRowStatus,
       "hwSINameToIndexMappingTable": hwSINameToIndexMappingTable,
       "hwSINameToIndexMappingEntry": hwSINameToIndexMappingEntry,
       "hwSIName": hwSIName,
       "hwSIIndex": hwSIIndex,
       "hwMinMNotifications": hwMinMNotifications,
       "hwMinMMacTnlUp": hwMinMMacTnlUp,
       "hwMinMMacTnlDown": hwMinMMacTnlDown,
       "hwMinMSIUp": hwMinMSIUp,
       "hwMinMSIDown": hwMinMSIDown,
       "hwMinMMacTnlCCFaultAlarm": hwMinMMacTnlCCFaultAlarm,
       "hwMinMMacTnlSwitch": hwMinMMacTnlSwitch,
       "hwMinMMacTnlRevertive": hwMinMMacTnlRevertive,
       "hwMinMSIMacLimitNumRaisingThreshold": hwMinMSIMacLimitNumRaisingThreshold,
       "hwMinMConformance": hwMinMConformance,
       "hwMinMGroups": hwMinMGroups,
       "hwMinMSystemGroup": hwMinMSystemGroup,
       "hwMinMMacTnlCfgGroup": hwMinMMacTnlCfgGroup,
       "hwMinMMacTnlStatisticsGroup": hwMinMMacTnlStatisticsGroup,
       "hwMinMMacTnlOAMGroup": hwMinMMacTnlOAMGroup,
       "hwMinMMacTnlApsGroup": hwMinMMacTnlApsGroup,
       "hwMinMSICfgGroup": hwMinMSICfgGroup,
       "hwMinMSIStatisticsGroup": hwMinMSIStatisticsGroup,
       "hwMinMNotificationGroup": hwMinMNotificationGroup,
       "hwMinMCompliances": hwMinMCompliances}
)
