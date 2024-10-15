# SNMP MIB module (CISCO-CLASS-BASED-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CLASS-BASED-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:31 2024
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

(DlciNumber,) = mibBuilder.importSymbols(
    "CISCO-FRAME-RELAY-MIB",
    "DlciNumber")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero",
    "Unsigned64")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 dod,
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
    "dod",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCBQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166)
)
ciscoCBQosMIB.setRevisions(
        ("2014-01-24 00:00",
         "2013-10-10 00:00",
         "2013-06-20 00:00",
         "2013-02-15 00:00",
         "2012-07-24 00:00",
         "2012-03-22 00:00",
         "2009-11-25 00:00",
         "2009-09-16 00:00",
         "2009-04-24 00:00",
         "2009-01-26 00:00",
         "2008-11-20 00:00",
         "2008-06-17 00:00",
         "2007-10-09 00:00",
         "2007-08-30 00:00",
         "2007-07-10 00:00",
         "2004-09-20 00:00",
         "2004-04-12 00:00",
         "2003-07-24 00:00",
         "2003-06-09 00:00",
         "2003-01-21 00:00",
         "2002-12-03 00:00",
         "2002-07-24 00:00",
         "2001-03-14 00:00",
         "2000-12-08 00:00",
         "2000-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QueueMechanism(Integer32, TextualConvention):
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
        *(("atmClp", 5),
          ("discardClass", 3),
          ("dscp", 2),
          ("mplsExp", 6),
          ("precedence", 1),
          ("qosGroup", 4))
    )



class QosObjectType(Integer32, TextualConvention):
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
        *(("account", 11),
          ("classmap", 2),
          ("compression", 9),
          ("ipslaMeasure", 10),
          ("matchStatement", 3),
          ("police", 7),
          ("policymap", 1),
          ("queueing", 4),
          ("randomDetect", 5),
          ("set", 8),
          ("trafficShaping", 6))
    )



class TrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class QosClassInfo(Integer32, TextualConvention):
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
        *(("matchAll", 2),
          ("matchAny", 3),
          ("none", 1))
    )



class QosMatchInfo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchNot", 2),
          ("none", 1))
    )



class InterfaceType(Integer32, TextualConvention):
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
        *(("atmPVC", 4),
          ("controlPlane", 5),
          ("evc", 7),
          ("frDLCI", 3),
          ("mainInterface", 1),
          ("subInterface", 2),
          ("vlanPort", 6))
    )



class QueueingBandwidthUnits(Integer32, TextualConvention):
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
        *(("kbps", 1),
          ("perMillion", 6),
          ("perThousand", 5),
          ("percentage", 2),
          ("percentageRemaining", 3),
          ("ratioRemaining", 4))
    )



class TrafficShapingLimit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("peak", 2))
    )



class PoliceAction(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("drop", 5),
          ("setAtmClp", 7),
          ("setDei", 16),
          ("setDeiImposition", 17),
          ("setDiscardClass", 10),
          ("setFrDe", 8),
          ("setIpDSCP", 2),
          ("setIpDscpTunnel", 12),
          ("setIpPrecedence", 3),
          ("setIpPrecedenceTunnel", 13),
          ("setL2Cos", 9),
          ("setL2CosInner", 14),
          ("setMplsExp", 6),
          ("setMplsExpTopMost", 11),
          ("setQosGroup", 4),
          ("setSrpPriority", 18),
          ("transmit", 1),
          ("unconfigured", 15))
    )



class SetFeatureType(Bits, TextualConvention):
    status = "current"


class REDMechanism(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmClp", 5),
          ("dei", 9),
          ("discardClass", 3),
          ("dscp", 2),
          ("l2Cos", 4),
          ("mplsExp", 6),
          ("precedence", 1),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )



class CbQosQueueUnitType(Integer32, TextualConvention):
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
        *(("bytes", 3),
          ("cells", 2),
          ("ms", 4),
          ("packets", 1),
          ("percentage", 6),
          ("us", 5))
    )



class CbQosQueueDepth(Unsigned32, TextualConvention):
    status = "current"


class CbQosRateType(Integer32, TextualConvention):
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
        *(("bps", 1),
          ("cps", 3),
          ("perMillion", 5),
          ("perThousand", 4),
          ("percentage", 2))
    )



class IPHCOption(Integer32, TextualConvention):
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
        *(("bothRtpTcp", 3),
          ("rtp", 1),
          ("tcp", 2))
    )



class CbQosTMSetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipDscp", 1),
          ("ipPrecedence", 2),
          ("l2Cos", 4),
          ("mplsExpImp", 5),
          ("mplsExpTop", 6),
          ("none", 0),
          ("qosGroup", 3))
    )



class CbQosEBType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("typeCorvil", 1),
          ("typeNone", 0))
    )



class CbQosEBCtd(OctetString, TextualConvention):
    status = "current"


class SetC3plAccountFeatureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("police", 2),
          ("queueing", 0),
          ("wred", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCBQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCBQosMIBObjects = _CiscoCBQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1)
)
_CbQosServicePolicy_ObjectIdentity = ObjectIdentity
cbQosServicePolicy = _CbQosServicePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1)
)
_CbQosServicePolicyTable_Object = MibTable
cbQosServicePolicyTable = _CbQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cbQosServicePolicyTable.setStatus("current")
_CbQosServicePolicyEntry_Object = MibTableRow
cbQosServicePolicyEntry = _CbQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1)
)
cbQosServicePolicyEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
)
if mibBuilder.loadTexts:
    cbQosServicePolicyEntry.setStatus("current")
_CbQosPolicyIndex_Type = Unsigned32
_CbQosPolicyIndex_Object = MibTableColumn
cbQosPolicyIndex = _CbQosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 1),
    _CbQosPolicyIndex_Type()
)
cbQosPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosPolicyIndex.setStatus("current")
_CbQosIfType_Type = InterfaceType
_CbQosIfType_Object = MibTableColumn
cbQosIfType = _CbQosIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 2),
    _CbQosIfType_Type()
)
cbQosIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIfType.setStatus("current")
_CbQosPolicyDirection_Type = TrafficDirection
_CbQosPolicyDirection_Object = MibTableColumn
cbQosPolicyDirection = _CbQosPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 3),
    _CbQosPolicyDirection_Type()
)
cbQosPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPolicyDirection.setStatus("current")
_CbQosIfIndex_Type = InterfaceIndex
_CbQosIfIndex_Object = MibTableColumn
cbQosIfIndex = _CbQosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 4),
    _CbQosIfIndex_Type()
)
cbQosIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIfIndex.setStatus("current")
_CbQosFrDLCI_Type = DlciNumber
_CbQosFrDLCI_Object = MibTableColumn
cbQosFrDLCI = _CbQosFrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 5),
    _CbQosFrDLCI_Type()
)
cbQosFrDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosFrDLCI.setStatus("current")


class _CbQosAtmVPI_Type(Unsigned32):
    """Custom type cbQosAtmVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CbQosAtmVPI_Type.__name__ = "Unsigned32"
_CbQosAtmVPI_Object = MibTableColumn
cbQosAtmVPI = _CbQosAtmVPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 6),
    _CbQosAtmVPI_Type()
)
cbQosAtmVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosAtmVPI.setStatus("current")


class _CbQosAtmVCI_Type(Unsigned32):
    """Custom type cbQosAtmVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbQosAtmVCI_Type.__name__ = "Unsigned32"
_CbQosAtmVCI_Object = MibTableColumn
cbQosAtmVCI = _CbQosAtmVCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 7),
    _CbQosAtmVCI_Type()
)
cbQosAtmVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosAtmVCI.setStatus("current")
_CbQosEntityIndex_Type = EntPhysicalIndexOrZero
_CbQosEntityIndex_Object = MibTableColumn
cbQosEntityIndex = _CbQosEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 8),
    _CbQosEntityIndex_Type()
)
cbQosEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEntityIndex.setStatus("current")
_CbQosVlanIndex_Type = VlanIndex
_CbQosVlanIndex_Object = MibTableColumn
cbQosVlanIndex = _CbQosVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 9),
    _CbQosVlanIndex_Type()
)
cbQosVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosVlanIndex.setStatus("current")
_CbQosEVC_Type = Unsigned32
_CbQosEVC_Object = MibTableColumn
cbQosEVC = _CbQosEVC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 10),
    _CbQosEVC_Type()
)
cbQosEVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEVC.setStatus("current")
_CbQosPolicyDiscontinuityTime_Type = TimeStamp
_CbQosPolicyDiscontinuityTime_Object = MibTableColumn
cbQosPolicyDiscontinuityTime = _CbQosPolicyDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 11),
    _CbQosPolicyDiscontinuityTime_Type()
)
cbQosPolicyDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPolicyDiscontinuityTime.setStatus("current")
_CbQosParentPolicyIndex_Type = Unsigned32
_CbQosParentPolicyIndex_Object = MibTableColumn
cbQosParentPolicyIndex = _CbQosParentPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 1, 1, 1, 12),
    _CbQosParentPolicyIndex_Type()
)
cbQosParentPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosParentPolicyIndex.setStatus("current")
_CbQosInterfacePolicy_ObjectIdentity = ObjectIdentity
cbQosInterfacePolicy = _CbQosInterfacePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 2)
)
_CbQosInterfacePolicyTable_Object = MibTable
cbQosInterfacePolicyTable = _CbQosInterfacePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbQosInterfacePolicyTable.setStatus("current")
_CbQosInterfacePolicyEntry_Object = MibTableRow
cbQosInterfacePolicyEntry = _CbQosInterfacePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 2, 1, 1)
)
cbQosInterfacePolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    cbQosInterfacePolicyEntry.setStatus("current")
_CbQosIFPolicyIndex_Type = Unsigned32
_CbQosIFPolicyIndex_Object = MibTableColumn
cbQosIFPolicyIndex = _CbQosIFPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 2, 1, 1, 1),
    _CbQosIFPolicyIndex_Type()
)
cbQosIFPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIFPolicyIndex.setStatus("current")
_CbQosFrameRelayVCPolicy_ObjectIdentity = ObjectIdentity
cbQosFrameRelayVCPolicy = _CbQosFrameRelayVCPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 3)
)
_CbQosFrameRelayPolicyTable_Object = MibTable
cbQosFrameRelayPolicyTable = _CbQosFrameRelayPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cbQosFrameRelayPolicyTable.setStatus("current")
_CbQosFrameRelayPolicyEntry_Object = MibTableRow
cbQosFrameRelayPolicyEntry = _CbQosFrameRelayPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 3, 1, 1)
)
cbQosFrameRelayPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosFrDLCI"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    cbQosFrameRelayPolicyEntry.setStatus("current")
_CbQosFRPolicyIndex_Type = Unsigned32
_CbQosFRPolicyIndex_Object = MibTableColumn
cbQosFRPolicyIndex = _CbQosFRPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 3, 1, 1, 1),
    _CbQosFRPolicyIndex_Type()
)
cbQosFRPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosFRPolicyIndex.setStatus("current")
_CbQosATMPVCPolicy_ObjectIdentity = ObjectIdentity
cbQosATMPVCPolicy = _CbQosATMPVCPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 4)
)
_CbQosATMPVCPolicyTable_Object = MibTable
cbQosATMPVCPolicyTable = _CbQosATMPVCPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cbQosATMPVCPolicyTable.setStatus("current")
_CbQosATMPVCPolicyEntry_Object = MibTableRow
cbQosATMPVCPolicyEntry = _CbQosATMPVCPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 4, 1, 1)
)
cbQosATMPVCPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVPI"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVCI"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    cbQosATMPVCPolicyEntry.setStatus("current")
_CbQosATMPolicyIndex_Type = Unsigned32
_CbQosATMPolicyIndex_Object = MibTableColumn
cbQosATMPolicyIndex = _CbQosATMPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 4, 1, 1, 1),
    _CbQosATMPolicyIndex_Type()
)
cbQosATMPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosATMPolicyIndex.setStatus("current")
_CbQosObjects_ObjectIdentity = ObjectIdentity
cbQosObjects = _CbQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5)
)
_CbQosObjectsTable_Object = MibTable
cbQosObjectsTable = _CbQosObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cbQosObjectsTable.setStatus("current")
_CbQosObjectsEntry_Object = MibTableRow
cbQosObjectsEntry = _CbQosObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1, 1)
)
cbQosObjectsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosObjectsEntry.setStatus("current")
_CbQosObjectsIndex_Type = Unsigned32
_CbQosObjectsIndex_Object = MibTableColumn
cbQosObjectsIndex = _CbQosObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1, 1, 1),
    _CbQosObjectsIndex_Type()
)
cbQosObjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosObjectsIndex.setStatus("current")
_CbQosConfigIndex_Type = Unsigned32
_CbQosConfigIndex_Object = MibTableColumn
cbQosConfigIndex = _CbQosConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1, 1, 2),
    _CbQosConfigIndex_Type()
)
cbQosConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosConfigIndex.setStatus("current")
_CbQosObjectsType_Type = QosObjectType
_CbQosObjectsType_Object = MibTableColumn
cbQosObjectsType = _CbQosObjectsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1, 1, 3),
    _CbQosObjectsType_Type()
)
cbQosObjectsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosObjectsType.setStatus("current")
_CbQosParentObjectsIndex_Type = Unsigned32
_CbQosParentObjectsIndex_Object = MibTableColumn
cbQosParentObjectsIndex = _CbQosParentObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 5, 1, 1, 4),
    _CbQosParentObjectsIndex_Type()
)
cbQosParentObjectsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosParentObjectsIndex.setStatus("current")
_CbQosPolicyMapCfg_ObjectIdentity = ObjectIdentity
cbQosPolicyMapCfg = _CbQosPolicyMapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 6)
)
_CbQosPolicyMapCfgTable_Object = MibTable
cbQosPolicyMapCfgTable = _CbQosPolicyMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cbQosPolicyMapCfgTable.setStatus("current")
_CbQosPolicyMapCfgEntry_Object = MibTableRow
cbQosPolicyMapCfgEntry = _CbQosPolicyMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 6, 1, 1)
)
cbQosPolicyMapCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosPolicyMapCfgEntry.setStatus("current")


class _CbQosPolicyMapName_Type(DisplayString):
    """Custom type cbQosPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbQosPolicyMapName_Type.__name__ = "DisplayString"
_CbQosPolicyMapName_Object = MibTableColumn
cbQosPolicyMapName = _CbQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 6, 1, 1, 1),
    _CbQosPolicyMapName_Type()
)
cbQosPolicyMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPolicyMapName.setStatus("current")


class _CbQosPolicyMapDesc_Type(DisplayString):
    """Custom type cbQosPolicyMapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbQosPolicyMapDesc_Type.__name__ = "DisplayString"
_CbQosPolicyMapDesc_Object = MibTableColumn
cbQosPolicyMapDesc = _CbQosPolicyMapDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 6, 1, 1, 2),
    _CbQosPolicyMapDesc_Type()
)
cbQosPolicyMapDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPolicyMapDesc.setStatus("current")
_CbQosClassMapCfg_ObjectIdentity = ObjectIdentity
cbQosClassMapCfg = _CbQosClassMapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7)
)
_CbQosCMCfgTable_Object = MibTable
cbQosCMCfgTable = _CbQosCMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cbQosCMCfgTable.setStatus("current")
_CbQosCMCfgEntry_Object = MibTableRow
cbQosCMCfgEntry = _CbQosCMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7, 1, 1)
)
cbQosCMCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosCMCfgEntry.setStatus("current")


class _CbQosCMName_Type(DisplayString):
    """Custom type cbQosCMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbQosCMName_Type.__name__ = "DisplayString"
_CbQosCMName_Object = MibTableColumn
cbQosCMName = _CbQosCMName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7, 1, 1, 1),
    _CbQosCMName_Type()
)
cbQosCMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMName.setStatus("current")


class _CbQosCMDesc_Type(DisplayString):
    """Custom type cbQosCMDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbQosCMDesc_Type.__name__ = "DisplayString"
_CbQosCMDesc_Object = MibTableColumn
cbQosCMDesc = _CbQosCMDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7, 1, 1, 2),
    _CbQosCMDesc_Type()
)
cbQosCMDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDesc.setStatus("current")
_CbQosCMInfo_Type = QosClassInfo
_CbQosCMInfo_Object = MibTableColumn
cbQosCMInfo = _CbQosCMInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 7, 1, 1, 3),
    _CbQosCMInfo_Type()
)
cbQosCMInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMInfo.setStatus("current")
_CbQosMatchStmtCfg_ObjectIdentity = ObjectIdentity
cbQosMatchStmtCfg = _CbQosMatchStmtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 8)
)
_CbQosMatchStmtCfgTable_Object = MibTable
cbQosMatchStmtCfgTable = _CbQosMatchStmtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cbQosMatchStmtCfgTable.setStatus("current")
_CbQosMatchStmtCfgEntry_Object = MibTableRow
cbQosMatchStmtCfgEntry = _CbQosMatchStmtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 8, 1, 1)
)
cbQosMatchStmtCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosMatchStmtCfgEntry.setStatus("current")


class _CbQosMatchStmtName_Type(DisplayString):
    """Custom type cbQosMatchStmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbQosMatchStmtName_Type.__name__ = "DisplayString"
_CbQosMatchStmtName_Object = MibTableColumn
cbQosMatchStmtName = _CbQosMatchStmtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 8, 1, 1, 1),
    _CbQosMatchStmtName_Type()
)
cbQosMatchStmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchStmtName.setStatus("current")
_CbQosMatchStmtInfo_Type = QosMatchInfo
_CbQosMatchStmtInfo_Object = MibTableColumn
cbQosMatchStmtInfo = _CbQosMatchStmtInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 8, 1, 1, 2),
    _CbQosMatchStmtInfo_Type()
)
cbQosMatchStmtInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchStmtInfo.setStatus("current")
_CbQosQueueingCfg_ObjectIdentity = ObjectIdentity
cbQosQueueingCfg = _CbQosQueueingCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9)
)
_CbQosQueueingCfgTable_Object = MibTable
cbQosQueueingCfgTable = _CbQosQueueingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgTable.setStatus("current")
_CbQosQueueingCfgEntry_Object = MibTableRow
cbQosQueueingCfgEntry = _CbQosQueueingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1)
)
cbQosQueueingCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgEntry.setStatus("current")


class _CbQosQueueingCfgBandwidth_Type(Integer32):
    """Custom type cbQosQueueingCfgBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_CbQosQueueingCfgBandwidth_Type.__name__ = "Integer32"
_CbQosQueueingCfgBandwidth_Object = MibTableColumn
cbQosQueueingCfgBandwidth = _CbQosQueueingCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 1),
    _CbQosQueueingCfgBandwidth_Type()
)
cbQosQueueingCfgBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgBandwidth.setStatus("deprecated")
_CbQosQueueingCfgBandwidthUnits_Type = QueueingBandwidthUnits
_CbQosQueueingCfgBandwidthUnits_Object = MibTableColumn
cbQosQueueingCfgBandwidthUnits = _CbQosQueueingCfgBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 2),
    _CbQosQueueingCfgBandwidthUnits_Type()
)
cbQosQueueingCfgBandwidthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgBandwidthUnits.setStatus("current")
_CbQosQueueingCfgFlowEnabled_Type = TruthValue
_CbQosQueueingCfgFlowEnabled_Object = MibTableColumn
cbQosQueueingCfgFlowEnabled = _CbQosQueueingCfgFlowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 3),
    _CbQosQueueingCfgFlowEnabled_Type()
)
cbQosQueueingCfgFlowEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgFlowEnabled.setStatus("current")
_CbQosQueueingCfgPriorityEnabled_Type = TruthValue
_CbQosQueueingCfgPriorityEnabled_Object = MibTableColumn
cbQosQueueingCfgPriorityEnabled = _CbQosQueueingCfgPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 4),
    _CbQosQueueingCfgPriorityEnabled_Type()
)
cbQosQueueingCfgPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgPriorityEnabled.setStatus("current")


class _CbQosQueueingCfgAggregateQSize_Type(Integer32):
    """Custom type cbQosQueueingCfgAggregateQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbQosQueueingCfgAggregateQSize_Type.__name__ = "Integer32"
_CbQosQueueingCfgAggregateQSize_Object = MibTableColumn
cbQosQueueingCfgAggregateQSize = _CbQosQueueingCfgAggregateQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 5),
    _CbQosQueueingCfgAggregateQSize_Type()
)
cbQosQueueingCfgAggregateQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgAggregateQSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosQueueingCfgAggregateQSize.setUnits("Packets")


class _CbQosQueueingCfgIndividualQSize_Type(Integer32):
    """Custom type cbQosQueueingCfgIndividualQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_CbQosQueueingCfgIndividualQSize_Type.__name__ = "Integer32"
_CbQosQueueingCfgIndividualQSize_Object = MibTableColumn
cbQosQueueingCfgIndividualQSize = _CbQosQueueingCfgIndividualQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 6),
    _CbQosQueueingCfgIndividualQSize_Type()
)
cbQosQueueingCfgIndividualQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgIndividualQSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosQueueingCfgIndividualQSize.setUnits("Packets")


class _CbQosQueueingCfgDynamicQNumber_Type(Integer32):
    """Custom type cbQosQueueingCfgDynamicQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_CbQosQueueingCfgDynamicQNumber_Type.__name__ = "Integer32"
_CbQosQueueingCfgDynamicQNumber_Object = MibTableColumn
cbQosQueueingCfgDynamicQNumber = _CbQosQueueingCfgDynamicQNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 7),
    _CbQosQueueingCfgDynamicQNumber_Type()
)
cbQosQueueingCfgDynamicQNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgDynamicQNumber.setStatus("current")


class _CbQosQueueingCfgPrioBurstSize_Type(Unsigned32):
    """Custom type cbQosQueueingCfgPrioBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64000000),
    )


_CbQosQueueingCfgPrioBurstSize_Type.__name__ = "Unsigned32"
_CbQosQueueingCfgPrioBurstSize_Object = MibTableColumn
cbQosQueueingCfgPrioBurstSize = _CbQosQueueingCfgPrioBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 8),
    _CbQosQueueingCfgPrioBurstSize_Type()
)
cbQosQueueingCfgPrioBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgPrioBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingCfgPrioBurstSize.setUnits("Bytes")
_CbQosQueueingCfgQLimitUnits_Type = CbQosQueueUnitType
_CbQosQueueingCfgQLimitUnits_Object = MibTableColumn
cbQosQueueingCfgQLimitUnits = _CbQosQueueingCfgQLimitUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 9),
    _CbQosQueueingCfgQLimitUnits_Type()
)
cbQosQueueingCfgQLimitUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgQLimitUnits.setStatus("current")
_CbQosQueueingCfgAggregateQLimit_Type = CbQosQueueDepth
_CbQosQueueingCfgAggregateQLimit_Object = MibTableColumn
cbQosQueueingCfgAggregateQLimit = _CbQosQueueingCfgAggregateQLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 10),
    _CbQosQueueingCfgAggregateQLimit_Type()
)
cbQosQueueingCfgAggregateQLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgAggregateQLimit.setStatus("current")
_CbQosQueueingCfgAggrQLimitTime_Type = Unsigned32
_CbQosQueueingCfgAggrQLimitTime_Object = MibTableColumn
cbQosQueueingCfgAggrQLimitTime = _CbQosQueueingCfgAggrQLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 11),
    _CbQosQueueingCfgAggrQLimitTime_Type()
)
cbQosQueueingCfgAggrQLimitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgAggrQLimitTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingCfgAggrQLimitTime.setUnits("milli-seconds")
_CbQosQueueingCfgPriorityLevel_Type = Unsigned32
_CbQosQueueingCfgPriorityLevel_Object = MibTableColumn
cbQosQueueingCfgPriorityLevel = _CbQosQueueingCfgPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 12),
    _CbQosQueueingCfgPriorityLevel_Type()
)
cbQosQueueingCfgPriorityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgPriorityLevel.setStatus("current")
_CbQosQueueingCfgBandwidth64_Type = Unsigned64
_CbQosQueueingCfgBandwidth64_Object = MibTableColumn
cbQosQueueingCfgBandwidth64 = _CbQosQueueingCfgBandwidth64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 13),
    _CbQosQueueingCfgBandwidth64_Type()
)
cbQosQueueingCfgBandwidth64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgBandwidth64.setStatus("current")
_CbQosQueueingCfgIndividualQSize64_Type = Unsigned64
_CbQosQueueingCfgIndividualQSize64_Object = MibTableColumn
cbQosQueueingCfgIndividualQSize64 = _CbQosQueueingCfgIndividualQSize64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 9, 1, 1, 14),
    _CbQosQueueingCfgIndividualQSize64_Type()
)
cbQosQueueingCfgIndividualQSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCfgIndividualQSize64.setStatus("current")
_CbQosREDCfg_ObjectIdentity = ObjectIdentity
cbQosREDCfg = _CbQosREDCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10)
)
_CbQosREDCfgTable_Object = MibTable
cbQosREDCfgTable = _CbQosREDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cbQosREDCfgTable.setStatus("current")
_CbQosREDCfgEntry_Object = MibTableRow
cbQosREDCfgEntry = _CbQosREDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1, 1)
)
cbQosREDCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosREDCfgEntry.setStatus("current")


class _CbQosREDCfgExponWeight_Type(Integer32):
    """Custom type cbQosREDCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CbQosREDCfgExponWeight_Type.__name__ = "Integer32"
_CbQosREDCfgExponWeight_Object = MibTableColumn
cbQosREDCfgExponWeight = _CbQosREDCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1, 1, 1),
    _CbQosREDCfgExponWeight_Type()
)
cbQosREDCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgExponWeight.setStatus("current")


class _CbQosREDCfgMeanQsize_Type(Integer32):
    """Custom type cbQosREDCfgMeanQsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbQosREDCfgMeanQsize_Type.__name__ = "Integer32"
_CbQosREDCfgMeanQsize_Object = MibTableColumn
cbQosREDCfgMeanQsize = _CbQosREDCfgMeanQsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1, 1, 2),
    _CbQosREDCfgMeanQsize_Type()
)
cbQosREDCfgMeanQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgMeanQsize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosREDCfgMeanQsize.setUnits("Packets")
_CbQosREDCfgDscpPrec_Type = REDMechanism
_CbQosREDCfgDscpPrec_Object = MibTableColumn
cbQosREDCfgDscpPrec = _CbQosREDCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1, 1, 3),
    _CbQosREDCfgDscpPrec_Type()
)
cbQosREDCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgDscpPrec.setStatus("current")
_CbQosREDCfgECNEnabled_Type = TruthValue
_CbQosREDCfgECNEnabled_Object = MibTableColumn
cbQosREDCfgECNEnabled = _CbQosREDCfgECNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 10, 1, 1, 4),
    _CbQosREDCfgECNEnabled_Type()
)
cbQosREDCfgECNEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgECNEnabled.setStatus("current")
_CbQosREDClassCfg_ObjectIdentity = ObjectIdentity
cbQosREDClassCfg = _CbQosREDClassCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11)
)
_CbQosREDClassCfgTable_Object = MibTable
cbQosREDClassCfgTable = _CbQosREDClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cbQosREDClassCfgTable.setStatus("current")
_CbQosREDClassCfgEntry_Object = MibTableRow
cbQosREDClassCfgEntry = _CbQosREDClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1)
)
cbQosREDClassCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosREDValue"),
)
if mibBuilder.loadTexts:
    cbQosREDClassCfgEntry.setStatus("current")


class _CbQosREDValue_Type(Integer32):
    """Custom type cbQosREDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CbQosREDValue_Type.__name__ = "Integer32"
_CbQosREDValue_Object = MibTableColumn
cbQosREDValue = _CbQosREDValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 1),
    _CbQosREDValue_Type()
)
cbQosREDValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosREDValue.setStatus("current")


class _CbQosREDCfgMinThreshold_Type(Integer32):
    """Custom type cbQosREDCfgMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_CbQosREDCfgMinThreshold_Type.__name__ = "Integer32"
_CbQosREDCfgMinThreshold_Object = MibTableColumn
cbQosREDCfgMinThreshold = _CbQosREDCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 2),
    _CbQosREDCfgMinThreshold_Type()
)
cbQosREDCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgMinThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosREDCfgMinThreshold.setUnits("Packets")


class _CbQosREDCfgMaxThreshold_Type(Integer32):
    """Custom type cbQosREDCfgMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_CbQosREDCfgMaxThreshold_Type.__name__ = "Integer32"
_CbQosREDCfgMaxThreshold_Object = MibTableColumn
cbQosREDCfgMaxThreshold = _CbQosREDCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 3),
    _CbQosREDCfgMaxThreshold_Type()
)
cbQosREDCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgMaxThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosREDCfgMaxThreshold.setUnits("Packets")


class _CbQosREDCfgPktDropProb_Type(Integer32):
    """Custom type cbQosREDCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CbQosREDCfgPktDropProb_Type.__name__ = "Integer32"
_CbQosREDCfgPktDropProb_Object = MibTableColumn
cbQosREDCfgPktDropProb = _CbQosREDCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 4),
    _CbQosREDCfgPktDropProb_Type()
)
cbQosREDCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDCfgPktDropProb.setStatus("current")
_CbQosREDClassCfgThresholdUnit_Type = CbQosQueueUnitType
_CbQosREDClassCfgThresholdUnit_Object = MibTableColumn
cbQosREDClassCfgThresholdUnit = _CbQosREDClassCfgThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 5),
    _CbQosREDClassCfgThresholdUnit_Type()
)
cbQosREDClassCfgThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgThresholdUnit.setStatus("deprecated")
_CbQosREDClassCfgMinThreshold_Type = CbQosQueueDepth
_CbQosREDClassCfgMinThreshold_Object = MibTableColumn
cbQosREDClassCfgMinThreshold = _CbQosREDClassCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 6),
    _CbQosREDClassCfgMinThreshold_Type()
)
cbQosREDClassCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMinThreshold.setStatus("current")
_CbQosREDClassCfgMaxThreshold_Type = CbQosQueueDepth
_CbQosREDClassCfgMaxThreshold_Object = MibTableColumn
cbQosREDClassCfgMaxThreshold = _CbQosREDClassCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 7),
    _CbQosREDClassCfgMaxThreshold_Type()
)
cbQosREDClassCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMaxThreshold.setStatus("current")
_CbQosREDClassCfgMinThresholdTime_Type = Unsigned32
_CbQosREDClassCfgMinThresholdTime_Object = MibTableColumn
cbQosREDClassCfgMinThresholdTime = _CbQosREDClassCfgMinThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 8),
    _CbQosREDClassCfgMinThresholdTime_Type()
)
cbQosREDClassCfgMinThresholdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMinThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMinThresholdTime.setUnits("milli-seconds")
_CbQosREDClassCfgMaxThresholdTime_Type = Unsigned32
_CbQosREDClassCfgMaxThresholdTime_Object = MibTableColumn
cbQosREDClassCfgMaxThresholdTime = _CbQosREDClassCfgMaxThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 9),
    _CbQosREDClassCfgMaxThresholdTime_Type()
)
cbQosREDClassCfgMaxThresholdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMaxThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMaxThresholdTime.setUnits("milli-seconds")
_CbQosREDClassCfgMaxThresholdUnit_Type = CbQosQueueUnitType
_CbQosREDClassCfgMaxThresholdUnit_Object = MibTableColumn
cbQosREDClassCfgMaxThresholdUnit = _CbQosREDClassCfgMaxThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 10),
    _CbQosREDClassCfgMaxThresholdUnit_Type()
)
cbQosREDClassCfgMaxThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMaxThresholdUnit.setStatus("current")
_CbQosREDClassCfgMinThresholdUnit_Type = CbQosQueueUnitType
_CbQosREDClassCfgMinThresholdUnit_Object = MibTableColumn
cbQosREDClassCfgMinThresholdUnit = _CbQosREDClassCfgMinThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 11, 1, 1, 11),
    _CbQosREDClassCfgMinThresholdUnit_Type()
)
cbQosREDClassCfgMinThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDClassCfgMinThresholdUnit.setStatus("current")
_CbQosPoliceCfg_ObjectIdentity = ObjectIdentity
cbQosPoliceCfg = _CbQosPoliceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12)
)
_CbQosPoliceCfgTable_Object = MibTable
cbQosPoliceCfgTable = _CbQosPoliceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgTable.setStatus("current")
_CbQosPoliceCfgEntry_Object = MibTableRow
cbQosPoliceCfgEntry = _CbQosPoliceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1)
)
cbQosPoliceCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgEntry.setStatus("current")


class _CbQosPoliceCfgRate_Type(Unsigned32):
    """Custom type cbQosPoliceCfgRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgRate_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgRate_Object = MibTableColumn
cbQosPoliceCfgRate = _CbQosPoliceCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 1),
    _CbQosPoliceCfgRate_Type()
)
cbQosPoliceCfgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgRate.setUnits("bits/second")


class _CbQosPoliceCfgBurstSize_Type(Unsigned32):
    """Custom type cbQosPoliceCfgBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 512000000),
    )


_CbQosPoliceCfgBurstSize_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgBurstSize_Object = MibTableColumn
cbQosPoliceCfgBurstSize = _CbQosPoliceCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 2),
    _CbQosPoliceCfgBurstSize_Type()
)
cbQosPoliceCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstSize.setUnits("Octets")


class _CbQosPoliceCfgExtBurstSize_Type(Unsigned32):
    """Custom type cbQosPoliceCfgExtBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 512000000),
    )


_CbQosPoliceCfgExtBurstSize_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgExtBurstSize_Object = MibTableColumn
cbQosPoliceCfgExtBurstSize = _CbQosPoliceCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 3),
    _CbQosPoliceCfgExtBurstSize_Type()
)
cbQosPoliceCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstSize.setUnits("Octets")
_CbQosPoliceCfgConformAction_Type = PoliceAction
_CbQosPoliceCfgConformAction_Object = MibTableColumn
cbQosPoliceCfgConformAction = _CbQosPoliceCfgConformAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 4),
    _CbQosPoliceCfgConformAction_Type()
)
cbQosPoliceCfgConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgConformAction.setStatus("deprecated")


class _CbQosPoliceCfgConformSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceCfgConformSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CbQosPoliceCfgConformSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgConformSetValue_Object = MibTableColumn
cbQosPoliceCfgConformSetValue = _CbQosPoliceCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 5),
    _CbQosPoliceCfgConformSetValue_Type()
)
cbQosPoliceCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgConformSetValue.setStatus("deprecated")
_CbQosPoliceCfgExceedAction_Type = PoliceAction
_CbQosPoliceCfgExceedAction_Object = MibTableColumn
cbQosPoliceCfgExceedAction = _CbQosPoliceCfgExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 6),
    _CbQosPoliceCfgExceedAction_Type()
)
cbQosPoliceCfgExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExceedAction.setStatus("deprecated")


class _CbQosPoliceCfgExceedSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceCfgExceedSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CbQosPoliceCfgExceedSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgExceedSetValue_Object = MibTableColumn
cbQosPoliceCfgExceedSetValue = _CbQosPoliceCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 7),
    _CbQosPoliceCfgExceedSetValue_Type()
)
cbQosPoliceCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExceedSetValue.setStatus("deprecated")
_CbQosPoliceCfgViolateAction_Type = PoliceAction
_CbQosPoliceCfgViolateAction_Object = MibTableColumn
cbQosPoliceCfgViolateAction = _CbQosPoliceCfgViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 8),
    _CbQosPoliceCfgViolateAction_Type()
)
cbQosPoliceCfgViolateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgViolateAction.setStatus("deprecated")


class _CbQosPoliceCfgViolateSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceCfgViolateSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CbQosPoliceCfgViolateSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgViolateSetValue_Object = MibTableColumn
cbQosPoliceCfgViolateSetValue = _CbQosPoliceCfgViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 9),
    _CbQosPoliceCfgViolateSetValue_Type()
)
cbQosPoliceCfgViolateSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgViolateSetValue.setStatus("deprecated")


class _CbQosPoliceCfgPir_Type(Unsigned32):
    """Custom type cbQosPoliceCfgPir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2000000000),
    )


_CbQosPoliceCfgPir_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgPir_Object = MibTableColumn
cbQosPoliceCfgPir = _CbQosPoliceCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 10),
    _CbQosPoliceCfgPir_Type()
)
cbQosPoliceCfgPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPir.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPir.setUnits("bits/second")
_CbQosPoliceCfgRate64_Type = Unsigned64
_CbQosPoliceCfgRate64_Object = MibTableColumn
cbQosPoliceCfgRate64 = _CbQosPoliceCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 11),
    _CbQosPoliceCfgRate64_Type()
)
cbQosPoliceCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgRate64.setUnits("bits/second")
_CbQosPoliceCfgRateType_Type = CbQosRateType
_CbQosPoliceCfgRateType_Object = MibTableColumn
cbQosPoliceCfgRateType = _CbQosPoliceCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 12),
    _CbQosPoliceCfgRateType_Type()
)
cbQosPoliceCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgRateType.setStatus("current")


class _CbQosPoliceCfgPercentRateValue_Type(Unsigned32):
    """Custom type cbQosPoliceCfgPercentRateValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbQosPoliceCfgPercentRateValue_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgPercentRateValue_Object = MibTableColumn
cbQosPoliceCfgPercentRateValue = _CbQosPoliceCfgPercentRateValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 13),
    _CbQosPoliceCfgPercentRateValue_Type()
)
cbQosPoliceCfgPercentRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPercentRateValue.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPercentRateValue.setUnits("% of Interface Bandwidth")


class _CbQosPoliceCfgPercentPirValue_Type(Unsigned32):
    """Custom type cbQosPoliceCfgPercentPirValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbQosPoliceCfgPercentPirValue_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgPercentPirValue_Object = MibTableColumn
cbQosPoliceCfgPercentPirValue = _CbQosPoliceCfgPercentPirValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 14),
    _CbQosPoliceCfgPercentPirValue_Type()
)
cbQosPoliceCfgPercentPirValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPercentPirValue.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPercentPirValue.setUnits("% of Interface Bandwidth")
_CbQosPoliceCfgCellRate_Type = Unsigned32
_CbQosPoliceCfgCellRate_Object = MibTableColumn
cbQosPoliceCfgCellRate = _CbQosPoliceCfgCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 15),
    _CbQosPoliceCfgCellRate_Type()
)
cbQosPoliceCfgCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCellRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCellRate.setUnits("cells/second")
_CbQosPoliceCfgCellPir_Type = Unsigned32
_CbQosPoliceCfgCellPir_Object = MibTableColumn
cbQosPoliceCfgCellPir = _CbQosPoliceCfgCellPir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 16),
    _CbQosPoliceCfgCellPir_Type()
)
cbQosPoliceCfgCellPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCellPir.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCellPir.setUnits("cells/second")


class _CbQosPoliceCfgBurstCell_Type(Unsigned32):
    """Custom type cbQosPoliceCfgBurstCell based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgBurstCell_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgBurstCell_Object = MibTableColumn
cbQosPoliceCfgBurstCell = _CbQosPoliceCfgBurstCell_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 17),
    _CbQosPoliceCfgBurstCell_Type()
)
cbQosPoliceCfgBurstCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstCell.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstCell.setUnits("Cells")


class _CbQosPoliceCfgExtBurstCell_Type(Unsigned32):
    """Custom type cbQosPoliceCfgExtBurstCell based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgExtBurstCell_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgExtBurstCell_Object = MibTableColumn
cbQosPoliceCfgExtBurstCell = _CbQosPoliceCfgExtBurstCell_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 18),
    _CbQosPoliceCfgExtBurstCell_Type()
)
cbQosPoliceCfgExtBurstCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstCell.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstCell.setUnits("Cells")


class _CbQosPoliceCfgBurstTime_Type(Unsigned32):
    """Custom type cbQosPoliceCfgBurstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgBurstTime_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgBurstTime_Object = MibTableColumn
cbQosPoliceCfgBurstTime = _CbQosPoliceCfgBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 19),
    _CbQosPoliceCfgBurstTime_Type()
)
cbQosPoliceCfgBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstTime.setUnits("milli-seconds")


class _CbQosPoliceCfgExtBurstTime_Type(Unsigned32):
    """Custom type cbQosPoliceCfgExtBurstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgExtBurstTime_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgExtBurstTime_Object = MibTableColumn
cbQosPoliceCfgExtBurstTime = _CbQosPoliceCfgExtBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 20),
    _CbQosPoliceCfgExtBurstTime_Type()
)
cbQosPoliceCfgExtBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstTime.setUnits("milli-seconds")


class _CbQosPoliceCfgCdvt_Type(Unsigned32):
    """Custom type cbQosPoliceCfgCdvt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosPoliceCfgCdvt_Type.__name__ = "Unsigned32"
_CbQosPoliceCfgCdvt_Object = MibTableColumn
cbQosPoliceCfgCdvt = _CbQosPoliceCfgCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 21),
    _CbQosPoliceCfgCdvt_Type()
)
cbQosPoliceCfgCdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCdvt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgCdvt.setUnits("micro-second")
_CbQosPoliceCfgConformColor_Type = DisplayString
_CbQosPoliceCfgConformColor_Object = MibTableColumn
cbQosPoliceCfgConformColor = _CbQosPoliceCfgConformColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 22),
    _CbQosPoliceCfgConformColor_Type()
)
cbQosPoliceCfgConformColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgConformColor.setStatus("current")
_CbQosPoliceCfgExceedColor_Type = DisplayString
_CbQosPoliceCfgExceedColor_Object = MibTableColumn
cbQosPoliceCfgExceedColor = _CbQosPoliceCfgExceedColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 23),
    _CbQosPoliceCfgExceedColor_Type()
)
cbQosPoliceCfgExceedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExceedColor.setStatus("current")
_CbQosPoliceCfgConditional_Type = TruthValue
_CbQosPoliceCfgConditional_Object = MibTableColumn
cbQosPoliceCfgConditional = _CbQosPoliceCfgConditional_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 24),
    _CbQosPoliceCfgConditional_Type()
)
cbQosPoliceCfgConditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgConditional.setStatus("current")
_CbQosPoliceCfgBurstSize64_Type = Unsigned64
_CbQosPoliceCfgBurstSize64_Object = MibTableColumn
cbQosPoliceCfgBurstSize64 = _CbQosPoliceCfgBurstSize64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 25),
    _CbQosPoliceCfgBurstSize64_Type()
)
cbQosPoliceCfgBurstSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstSize64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgBurstSize64.setUnits("Octets")
_CbQosPoliceCfgExtBurstSize64_Type = Unsigned64
_CbQosPoliceCfgExtBurstSize64_Object = MibTableColumn
cbQosPoliceCfgExtBurstSize64 = _CbQosPoliceCfgExtBurstSize64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 26),
    _CbQosPoliceCfgExtBurstSize64_Type()
)
cbQosPoliceCfgExtBurstSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstSize64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtBurstSize64.setUnits("Octets")
_CbQosPoliceCfgPir64_Type = Unsigned64
_CbQosPoliceCfgPir64_Object = MibTableColumn
cbQosPoliceCfgPir64 = _CbQosPoliceCfgPir64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 12, 1, 1, 27),
    _CbQosPoliceCfgPir64_Type()
)
cbQosPoliceCfgPir64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPir64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfgPir64.setUnits("Octets")
_CbQosTSCfg_ObjectIdentity = ObjectIdentity
cbQosTSCfg = _CbQosTSCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13)
)
_CbQosTSCfgTable_Object = MibTable
cbQosTSCfgTable = _CbQosTSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cbQosTSCfgTable.setStatus("current")
_CbQosTSCfgEntry_Object = MibTableRow
cbQosTSCfgEntry = _CbQosTSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1)
)
cbQosTSCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosTSCfgEntry.setStatus("current")


class _CbQosTSCfgRate_Type(Integer32):
    """Custom type cbQosTSCfgRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CbQosTSCfgRate_Type.__name__ = "Integer32"
_CbQosTSCfgRate_Object = MibTableColumn
cbQosTSCfgRate = _CbQosTSCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 1),
    _CbQosTSCfgRate_Type()
)
cbQosTSCfgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgRate.setUnits("bits/second")


class _CbQosTSCfgBurstSize_Type(Integer32):
    """Custom type cbQosTSCfgBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 154400000),
    )


_CbQosTSCfgBurstSize_Type.__name__ = "Integer32"
_CbQosTSCfgBurstSize_Object = MibTableColumn
cbQosTSCfgBurstSize = _CbQosTSCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 2),
    _CbQosTSCfgBurstSize_Type()
)
cbQosTSCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstSize.setUnits("bits")


class _CbQosTSCfgExtBurstSize_Type(Integer32):
    """Custom type cbQosTSCfgExtBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 154400000),
    )


_CbQosTSCfgExtBurstSize_Type.__name__ = "Integer32"
_CbQosTSCfgExtBurstSize_Object = MibTableColumn
cbQosTSCfgExtBurstSize = _CbQosTSCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 3),
    _CbQosTSCfgExtBurstSize_Type()
)
cbQosTSCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstSize.setUnits("bits")
_CbQosTSCfgAdaptiveEnabled_Type = TruthValue
_CbQosTSCfgAdaptiveEnabled_Object = MibTableColumn
cbQosTSCfgAdaptiveEnabled = _CbQosTSCfgAdaptiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 4),
    _CbQosTSCfgAdaptiveEnabled_Type()
)
cbQosTSCfgAdaptiveEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgAdaptiveEnabled.setStatus("current")


class _CbQosTSCfgAdaptiveRate_Type(Integer32):
    """Custom type cbQosTSCfgAdaptiveRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 154400000),
    )


_CbQosTSCfgAdaptiveRate_Type.__name__ = "Integer32"
_CbQosTSCfgAdaptiveRate_Object = MibTableColumn
cbQosTSCfgAdaptiveRate = _CbQosTSCfgAdaptiveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 5),
    _CbQosTSCfgAdaptiveRate_Type()
)
cbQosTSCfgAdaptiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgAdaptiveRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgAdaptiveRate.setUnits("bits/second")
_CbQosTSCfgLimitType_Type = TrafficShapingLimit
_CbQosTSCfgLimitType_Object = MibTableColumn
cbQosTSCfgLimitType = _CbQosTSCfgLimitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 6),
    _CbQosTSCfgLimitType_Type()
)
cbQosTSCfgLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgLimitType.setStatus("current")
_CbQosTSCfgRateType_Type = CbQosRateType
_CbQosTSCfgRateType_Object = MibTableColumn
cbQosTSCfgRateType = _CbQosTSCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 7),
    _CbQosTSCfgRateType_Type()
)
cbQosTSCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgRateType.setStatus("current")


class _CbQosTSCfgPercentRateValue_Type(Unsigned32):
    """Custom type cbQosTSCfgPercentRateValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbQosTSCfgPercentRateValue_Type.__name__ = "Unsigned32"
_CbQosTSCfgPercentRateValue_Object = MibTableColumn
cbQosTSCfgPercentRateValue = _CbQosTSCfgPercentRateValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 8),
    _CbQosTSCfgPercentRateValue_Type()
)
cbQosTSCfgPercentRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgPercentRateValue.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgPercentRateValue.setUnits("% of Interface Bandwidth")


class _CbQosTSCfgBurstTime_Type(Unsigned32):
    """Custom type cbQosTSCfgBurstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosTSCfgBurstTime_Type.__name__ = "Unsigned32"
_CbQosTSCfgBurstTime_Object = MibTableColumn
cbQosTSCfgBurstTime = _CbQosTSCfgBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 9),
    _CbQosTSCfgBurstTime_Type()
)
cbQosTSCfgBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstTime.setUnits("milli-seconds")


class _CbQosTSCfgExtBurstTime_Type(Unsigned32):
    """Custom type cbQosTSCfgExtBurstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbQosTSCfgExtBurstTime_Type.__name__ = "Unsigned32"
_CbQosTSCfgExtBurstTime_Object = MibTableColumn
cbQosTSCfgExtBurstTime = _CbQosTSCfgExtBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 10),
    _CbQosTSCfgExtBurstTime_Type()
)
cbQosTSCfgExtBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstTime.setUnits("milli-seconds")
_CbQosTSCfgRate64_Type = Unsigned64
_CbQosTSCfgRate64_Object = MibTableColumn
cbQosTSCfgRate64 = _CbQosTSCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 11),
    _CbQosTSCfgRate64_Type()
)
cbQosTSCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgRate64.setUnits("bits/second")
_CbQosTSCfgBurstSize64_Type = Unsigned64
_CbQosTSCfgBurstSize64_Object = MibTableColumn
cbQosTSCfgBurstSize64 = _CbQosTSCfgBurstSize64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 12),
    _CbQosTSCfgBurstSize64_Type()
)
cbQosTSCfgBurstSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstSize64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgBurstSize64.setUnits("bits")
_CbQosTSCfgExtBurstSize64_Type = Unsigned64
_CbQosTSCfgExtBurstSize64_Object = MibTableColumn
cbQosTSCfgExtBurstSize64 = _CbQosTSCfgExtBurstSize64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 13, 1, 1, 13),
    _CbQosTSCfgExtBurstSize64_Type()
)
cbQosTSCfgExtBurstSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstSize64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSCfgExtBurstSize64.setUnits("bits")
_CbQosSetCfg_ObjectIdentity = ObjectIdentity
cbQosSetCfg = _CbQosSetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14)
)
_CbQosSetCfgTable_Object = MibTable
cbQosSetCfgTable = _CbQosSetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cbQosSetCfgTable.setStatus("current")
_CbQosSetCfgEntry_Object = MibTableRow
cbQosSetCfgEntry = _CbQosSetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1)
)
cbQosSetCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosSetCfgEntry.setStatus("current")
_CbQosSetCfgFeature_Type = SetFeatureType
_CbQosSetCfgFeature_Object = MibTableColumn
cbQosSetCfgFeature = _CbQosSetCfgFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 1),
    _CbQosSetCfgFeature_Type()
)
cbQosSetCfgFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgFeature.setStatus("current")


class _CbQosSetCfgIpDSCPValue_Type(Integer32):
    """Custom type cbQosSetCfgIpDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CbQosSetCfgIpDSCPValue_Type.__name__ = "Integer32"
_CbQosSetCfgIpDSCPValue_Object = MibTableColumn
cbQosSetCfgIpDSCPValue = _CbQosSetCfgIpDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 2),
    _CbQosSetCfgIpDSCPValue_Type()
)
cbQosSetCfgIpDSCPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgIpDSCPValue.setStatus("current")


class _CbQosSetCfgIpPrecedenceValue_Type(Integer32):
    """Custom type cbQosSetCfgIpPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgIpPrecedenceValue_Type.__name__ = "Integer32"
_CbQosSetCfgIpPrecedenceValue_Object = MibTableColumn
cbQosSetCfgIpPrecedenceValue = _CbQosSetCfgIpPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 3),
    _CbQosSetCfgIpPrecedenceValue_Type()
)
cbQosSetCfgIpPrecedenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgIpPrecedenceValue.setStatus("current")


class _CbQosSetCfgQosGroupValue_Type(Integer32):
    """Custom type cbQosSetCfgQosGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosSetCfgQosGroupValue_Type.__name__ = "Integer32"
_CbQosSetCfgQosGroupValue_Object = MibTableColumn
cbQosSetCfgQosGroupValue = _CbQosSetCfgQosGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 4),
    _CbQosSetCfgQosGroupValue_Type()
)
cbQosSetCfgQosGroupValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgQosGroupValue.setStatus("current")


class _CbQosSetCfgL2CosValue_Type(Integer32):
    """Custom type cbQosSetCfgL2CosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgL2CosValue_Type.__name__ = "Integer32"
_CbQosSetCfgL2CosValue_Object = MibTableColumn
cbQosSetCfgL2CosValue = _CbQosSetCfgL2CosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 5),
    _CbQosSetCfgL2CosValue_Type()
)
cbQosSetCfgL2CosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgL2CosValue.setStatus("current")


class _CbQosSetCfgMplsExpValue_Type(Unsigned32):
    """Custom type cbQosSetCfgMplsExpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgMplsExpValue_Type.__name__ = "Unsigned32"
_CbQosSetCfgMplsExpValue_Object = MibTableColumn
cbQosSetCfgMplsExpValue = _CbQosSetCfgMplsExpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 6),
    _CbQosSetCfgMplsExpValue_Type()
)
cbQosSetCfgMplsExpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgMplsExpValue.setStatus("current")


class _CbQosSetCfgDiscardClassValue_Type(Unsigned32):
    """Custom type cbQosSetCfgDiscardClassValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgDiscardClassValue_Type.__name__ = "Unsigned32"
_CbQosSetCfgDiscardClassValue_Object = MibTableColumn
cbQosSetCfgDiscardClassValue = _CbQosSetCfgDiscardClassValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 7),
    _CbQosSetCfgDiscardClassValue_Type()
)
cbQosSetCfgDiscardClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgDiscardClassValue.setStatus("current")


class _CbQosSetCfgMplsExpTopMostValue_Type(Unsigned32):
    """Custom type cbQosSetCfgMplsExpTopMostValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgMplsExpTopMostValue_Type.__name__ = "Unsigned32"
_CbQosSetCfgMplsExpTopMostValue_Object = MibTableColumn
cbQosSetCfgMplsExpTopMostValue = _CbQosSetCfgMplsExpTopMostValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 8),
    _CbQosSetCfgMplsExpTopMostValue_Type()
)
cbQosSetCfgMplsExpTopMostValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgMplsExpTopMostValue.setStatus("current")


class _CbQosSetCfgSrpPriority_Type(Unsigned32):
    """Custom type cbQosSetCfgSrpPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgSrpPriority_Type.__name__ = "Unsigned32"
_CbQosSetCfgSrpPriority_Object = MibTableColumn
cbQosSetCfgSrpPriority = _CbQosSetCfgSrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 9),
    _CbQosSetCfgSrpPriority_Type()
)
cbQosSetCfgSrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgSrpPriority.setStatus("current")


class _CbQosSetCfgFrFecnBecn_Type(Unsigned32):
    """Custom type cbQosSetCfgFrFecnBecn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosSetCfgFrFecnBecn_Type.__name__ = "Unsigned32"
_CbQosSetCfgFrFecnBecn_Object = MibTableColumn
cbQosSetCfgFrFecnBecn = _CbQosSetCfgFrFecnBecn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 10),
    _CbQosSetCfgFrFecnBecn_Type()
)
cbQosSetCfgFrFecnBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgFrFecnBecn.setStatus("current")


class _CbQosSetCfgL2CosInnerValue_Type(Integer32):
    """Custom type cbQosSetCfgL2CosInnerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgL2CosInnerValue_Type.__name__ = "Integer32"
_CbQosSetCfgL2CosInnerValue_Object = MibTableColumn
cbQosSetCfgL2CosInnerValue = _CbQosSetCfgL2CosInnerValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 11),
    _CbQosSetCfgL2CosInnerValue_Type()
)
cbQosSetCfgL2CosInnerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgL2CosInnerValue.setStatus("current")


class _CbQosSetCfgFrDe_Type(TruthValue):
    """Custom type cbQosSetCfgFrDe based on TruthValue"""


_CbQosSetCfgFrDe_Object = MibTableColumn
cbQosSetCfgFrDe = _CbQosSetCfgFrDe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 12),
    _CbQosSetCfgFrDe_Type()
)
cbQosSetCfgFrDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgFrDe.setStatus("current")


class _CbQosSetCfgIpPrecedenceTunnelValue_Type(Unsigned32):
    """Custom type cbQosSetCfgIpPrecedenceTunnelValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CbQosSetCfgIpPrecedenceTunnelValue_Type.__name__ = "Unsigned32"
_CbQosSetCfgIpPrecedenceTunnelValue_Object = MibTableColumn
cbQosSetCfgIpPrecedenceTunnelValue = _CbQosSetCfgIpPrecedenceTunnelValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 13),
    _CbQosSetCfgIpPrecedenceTunnelValue_Type()
)
cbQosSetCfgIpPrecedenceTunnelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgIpPrecedenceTunnelValue.setStatus("current")


class _CbQosSetCfgIpDSCPTunnelValue_Type(Unsigned32):
    """Custom type cbQosSetCfgIpDSCPTunnelValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CbQosSetCfgIpDSCPTunnelValue_Type.__name__ = "Unsigned32"
_CbQosSetCfgIpDSCPTunnelValue_Object = MibTableColumn
cbQosSetCfgIpDSCPTunnelValue = _CbQosSetCfgIpDSCPTunnelValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 14),
    _CbQosSetCfgIpDSCPTunnelValue_Type()
)
cbQosSetCfgIpDSCPTunnelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgIpDSCPTunnelValue.setStatus("current")
_CbQosSetCfgDei_Type = TruthValue
_CbQosSetCfgDei_Object = MibTableColumn
cbQosSetCfgDei = _CbQosSetCfgDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 15),
    _CbQosSetCfgDei_Type()
)
cbQosSetCfgDei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgDei.setStatus("current")
_CbQosSetCfgDeiImposition_Type = TruthValue
_CbQosSetCfgDeiImposition_Object = MibTableColumn
cbQosSetCfgDeiImposition = _CbQosSetCfgDeiImposition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 14, 1, 1, 16),
    _CbQosSetCfgDeiImposition_Type()
)
cbQosSetCfgDeiImposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetCfgDeiImposition.setStatus("current")
_CbQosClassMapStats_ObjectIdentity = ObjectIdentity
cbQosClassMapStats = _CbQosClassMapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15)
)
_CbQosCMStatsTable_Object = MibTable
cbQosCMStatsTable = _CbQosCMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cbQosCMStatsTable.setStatus("current")
_CbQosCMStatsEntry_Object = MibTableRow
cbQosCMStatsEntry = _CbQosCMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1)
)
cbQosCMStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosCMStatsEntry.setStatus("current")
_CbQosCMPrePolicyPktOverflow_Type = Counter32
_CbQosCMPrePolicyPktOverflow_Object = MibTableColumn
cbQosCMPrePolicyPktOverflow = _CbQosCMPrePolicyPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 1),
    _CbQosCMPrePolicyPktOverflow_Type()
)
cbQosCMPrePolicyPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyPktOverflow.setStatus("current")
_CbQosCMPrePolicyPkt_Type = Counter32
_CbQosCMPrePolicyPkt_Object = MibTableColumn
cbQosCMPrePolicyPkt = _CbQosCMPrePolicyPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 2),
    _CbQosCMPrePolicyPkt_Type()
)
cbQosCMPrePolicyPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyPkt.setStatus("current")
_CbQosCMPrePolicyPkt64_Type = Counter64
_CbQosCMPrePolicyPkt64_Object = MibTableColumn
cbQosCMPrePolicyPkt64 = _CbQosCMPrePolicyPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 3),
    _CbQosCMPrePolicyPkt64_Type()
)
cbQosCMPrePolicyPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyPkt64.setStatus("current")
_CbQosCMPrePolicyByteOverflow_Type = Counter32
_CbQosCMPrePolicyByteOverflow_Object = MibTableColumn
cbQosCMPrePolicyByteOverflow = _CbQosCMPrePolicyByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 4),
    _CbQosCMPrePolicyByteOverflow_Type()
)
cbQosCMPrePolicyByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyByteOverflow.setStatus("current")
_CbQosCMPrePolicyByte_Type = Counter32
_CbQosCMPrePolicyByte_Object = MibTableColumn
cbQosCMPrePolicyByte = _CbQosCMPrePolicyByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 5),
    _CbQosCMPrePolicyByte_Type()
)
cbQosCMPrePolicyByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyByte.setStatus("current")
_CbQosCMPrePolicyByte64_Type = Counter64
_CbQosCMPrePolicyByte64_Object = MibTableColumn
cbQosCMPrePolicyByte64 = _CbQosCMPrePolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 6),
    _CbQosCMPrePolicyByte64_Type()
)
cbQosCMPrePolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyByte64.setStatus("current")
_CbQosCMPrePolicyBitRate_Type = Gauge32
_CbQosCMPrePolicyBitRate_Object = MibTableColumn
cbQosCMPrePolicyBitRate = _CbQosCMPrePolicyBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 7),
    _CbQosCMPrePolicyBitRate_Type()
)
cbQosCMPrePolicyBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyBitRate.setUnits("bits per second")
_CbQosCMPostPolicyByteOverflow_Type = Counter32
_CbQosCMPostPolicyByteOverflow_Object = MibTableColumn
cbQosCMPostPolicyByteOverflow = _CbQosCMPostPolicyByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 8),
    _CbQosCMPostPolicyByteOverflow_Type()
)
cbQosCMPostPolicyByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyByteOverflow.setStatus("current")
_CbQosCMPostPolicyByte_Type = Counter32
_CbQosCMPostPolicyByte_Object = MibTableColumn
cbQosCMPostPolicyByte = _CbQosCMPostPolicyByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 9),
    _CbQosCMPostPolicyByte_Type()
)
cbQosCMPostPolicyByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyByte.setStatus("current")
_CbQosCMPostPolicyByte64_Type = Counter64
_CbQosCMPostPolicyByte64_Object = MibTableColumn
cbQosCMPostPolicyByte64 = _CbQosCMPostPolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 10),
    _CbQosCMPostPolicyByte64_Type()
)
cbQosCMPostPolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyByte64.setStatus("current")
_CbQosCMPostPolicyBitRate_Type = Gauge32
_CbQosCMPostPolicyBitRate_Object = MibTableColumn
cbQosCMPostPolicyBitRate = _CbQosCMPostPolicyBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 11),
    _CbQosCMPostPolicyBitRate_Type()
)
cbQosCMPostPolicyBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyBitRate.setUnits("bits per second")
_CbQosCMDropPktOverflow_Type = Counter32
_CbQosCMDropPktOverflow_Object = MibTableColumn
cbQosCMDropPktOverflow = _CbQosCMDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 12),
    _CbQosCMDropPktOverflow_Type()
)
cbQosCMDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropPktOverflow.setStatus("current")
_CbQosCMDropPkt_Type = Counter32
_CbQosCMDropPkt_Object = MibTableColumn
cbQosCMDropPkt = _CbQosCMDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 13),
    _CbQosCMDropPkt_Type()
)
cbQosCMDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropPkt.setStatus("current")
_CbQosCMDropPkt64_Type = Counter64
_CbQosCMDropPkt64_Object = MibTableColumn
cbQosCMDropPkt64 = _CbQosCMDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 14),
    _CbQosCMDropPkt64_Type()
)
cbQosCMDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropPkt64.setStatus("current")
_CbQosCMDropByteOverflow_Type = Counter32
_CbQosCMDropByteOverflow_Object = MibTableColumn
cbQosCMDropByteOverflow = _CbQosCMDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 15),
    _CbQosCMDropByteOverflow_Type()
)
cbQosCMDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropByteOverflow.setStatus("current")
_CbQosCMDropByte_Type = Counter32
_CbQosCMDropByte_Object = MibTableColumn
cbQosCMDropByte = _CbQosCMDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 16),
    _CbQosCMDropByte_Type()
)
cbQosCMDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropByte.setStatus("current")
_CbQosCMDropByte64_Type = Counter64
_CbQosCMDropByte64_Object = MibTableColumn
cbQosCMDropByte64 = _CbQosCMDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 17),
    _CbQosCMDropByte64_Type()
)
cbQosCMDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropByte64.setStatus("current")
_CbQosCMDropBitRate_Type = Gauge32
_CbQosCMDropBitRate_Object = MibTableColumn
cbQosCMDropBitRate = _CbQosCMDropBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 18),
    _CbQosCMDropBitRate_Type()
)
cbQosCMDropBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMDropBitRate.setUnits("bits per second")
_CbQosCMNoBufDropPktOverflow_Type = Counter32
_CbQosCMNoBufDropPktOverflow_Object = MibTableColumn
cbQosCMNoBufDropPktOverflow = _CbQosCMNoBufDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 19),
    _CbQosCMNoBufDropPktOverflow_Type()
)
cbQosCMNoBufDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMNoBufDropPktOverflow.setStatus("current")
_CbQosCMNoBufDropPkt_Type = Counter32
_CbQosCMNoBufDropPkt_Object = MibTableColumn
cbQosCMNoBufDropPkt = _CbQosCMNoBufDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 20),
    _CbQosCMNoBufDropPkt_Type()
)
cbQosCMNoBufDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMNoBufDropPkt.setStatus("current")
_CbQosCMNoBufDropPkt64_Type = Counter64
_CbQosCMNoBufDropPkt64_Object = MibTableColumn
cbQosCMNoBufDropPkt64 = _CbQosCMNoBufDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 21),
    _CbQosCMNoBufDropPkt64_Type()
)
cbQosCMNoBufDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMNoBufDropPkt64.setStatus("current")
_CbQosCMFragmentPktOverflow_Type = Counter32
_CbQosCMFragmentPktOverflow_Object = MibTableColumn
cbQosCMFragmentPktOverflow = _CbQosCMFragmentPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 22),
    _CbQosCMFragmentPktOverflow_Type()
)
cbQosCMFragmentPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentPktOverflow.setStatus("current")
_CbQosCMFragmentPkt_Type = Counter32
_CbQosCMFragmentPkt_Object = MibTableColumn
cbQosCMFragmentPkt = _CbQosCMFragmentPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 23),
    _CbQosCMFragmentPkt_Type()
)
cbQosCMFragmentPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentPkt.setStatus("current")
_CbQosCMFragmentPkt64_Type = Counter64
_CbQosCMFragmentPkt64_Object = MibTableColumn
cbQosCMFragmentPkt64 = _CbQosCMFragmentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 24),
    _CbQosCMFragmentPkt64_Type()
)
cbQosCMFragmentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentPkt64.setStatus("current")
_CbQosCMFragmentByteOverflow_Type = Counter32
_CbQosCMFragmentByteOverflow_Object = MibTableColumn
cbQosCMFragmentByteOverflow = _CbQosCMFragmentByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 25),
    _CbQosCMFragmentByteOverflow_Type()
)
cbQosCMFragmentByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentByteOverflow.setStatus("current")
_CbQosCMFragmentByte_Type = Counter32
_CbQosCMFragmentByte_Object = MibTableColumn
cbQosCMFragmentByte = _CbQosCMFragmentByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 26),
    _CbQosCMFragmentByte_Type()
)
cbQosCMFragmentByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentByte.setStatus("current")
_CbQosCMFragmentByte64_Type = Counter64
_CbQosCMFragmentByte64_Object = MibTableColumn
cbQosCMFragmentByte64 = _CbQosCMFragmentByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 27),
    _CbQosCMFragmentByte64_Type()
)
cbQosCMFragmentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMFragmentByte64.setStatus("current")
_CbQosCMPrePolicyBitRate64_Type = CounterBasedGauge64
_CbQosCMPrePolicyBitRate64_Object = MibTableColumn
cbQosCMPrePolicyBitRate64 = _CbQosCMPrePolicyBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 28),
    _CbQosCMPrePolicyBitRate64_Type()
)
cbQosCMPrePolicyBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMPrePolicyBitRate64.setUnits("bits per second")
_CbQosCMPostPolicyBitRate64_Type = CounterBasedGauge64
_CbQosCMPostPolicyBitRate64_Object = MibTableColumn
cbQosCMPostPolicyBitRate64 = _CbQosCMPostPolicyBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 29),
    _CbQosCMPostPolicyBitRate64_Type()
)
cbQosCMPostPolicyBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMPostPolicyBitRate64.setUnits("bits per second")
_CbQosCMDropBitRate64_Type = CounterBasedGauge64
_CbQosCMDropBitRate64_Object = MibTableColumn
cbQosCMDropBitRate64 = _CbQosCMDropBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 15, 1, 1, 30),
    _CbQosCMDropBitRate64_Type()
)
cbQosCMDropBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosCMDropBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosCMDropBitRate64.setUnits("bits per second")
_CbQosMatchStmtStats_ObjectIdentity = ObjectIdentity
cbQosMatchStmtStats = _CbQosMatchStmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16)
)
_CbQosMatchStmtStatsTable_Object = MibTable
cbQosMatchStmtStatsTable = _CbQosMatchStmtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cbQosMatchStmtStatsTable.setStatus("current")
_CbQosMatchStmtStatsEntry_Object = MibTableRow
cbQosMatchStmtStatsEntry = _CbQosMatchStmtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1)
)
cbQosMatchStmtStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosMatchStmtStatsEntry.setStatus("current")
_CbQosMatchPrePolicyPktOverflow_Type = Counter32
_CbQosMatchPrePolicyPktOverflow_Object = MibTableColumn
cbQosMatchPrePolicyPktOverflow = _CbQosMatchPrePolicyPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 1),
    _CbQosMatchPrePolicyPktOverflow_Type()
)
cbQosMatchPrePolicyPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyPktOverflow.setStatus("current")
_CbQosMatchPrePolicyPkt_Type = Counter32
_CbQosMatchPrePolicyPkt_Object = MibTableColumn
cbQosMatchPrePolicyPkt = _CbQosMatchPrePolicyPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 2),
    _CbQosMatchPrePolicyPkt_Type()
)
cbQosMatchPrePolicyPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyPkt.setStatus("current")
_CbQosMatchPrePolicyPkt64_Type = Counter64
_CbQosMatchPrePolicyPkt64_Object = MibTableColumn
cbQosMatchPrePolicyPkt64 = _CbQosMatchPrePolicyPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 3),
    _CbQosMatchPrePolicyPkt64_Type()
)
cbQosMatchPrePolicyPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyPkt64.setStatus("current")
_CbQosMatchPrePolicyByteOverflow_Type = Counter32
_CbQosMatchPrePolicyByteOverflow_Object = MibTableColumn
cbQosMatchPrePolicyByteOverflow = _CbQosMatchPrePolicyByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 4),
    _CbQosMatchPrePolicyByteOverflow_Type()
)
cbQosMatchPrePolicyByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyByteOverflow.setStatus("current")
_CbQosMatchPrePolicyByte_Type = Counter32
_CbQosMatchPrePolicyByte_Object = MibTableColumn
cbQosMatchPrePolicyByte = _CbQosMatchPrePolicyByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 5),
    _CbQosMatchPrePolicyByte_Type()
)
cbQosMatchPrePolicyByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyByte.setStatus("current")
_CbQosMatchPrePolicyByte64_Type = Counter64
_CbQosMatchPrePolicyByte64_Object = MibTableColumn
cbQosMatchPrePolicyByte64 = _CbQosMatchPrePolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 6),
    _CbQosMatchPrePolicyByte64_Type()
)
cbQosMatchPrePolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyByte64.setStatus("current")
_CbQosMatchPrePolicyBitRate_Type = Gauge32
_CbQosMatchPrePolicyBitRate_Object = MibTableColumn
cbQosMatchPrePolicyBitRate = _CbQosMatchPrePolicyBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 16, 1, 1, 7),
    _CbQosMatchPrePolicyBitRate_Type()
)
cbQosMatchPrePolicyBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosMatchPrePolicyBitRate.setUnits("bits per second")
_CbQosPoliceStats_ObjectIdentity = ObjectIdentity
cbQosPoliceStats = _CbQosPoliceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17)
)
_CbQosPoliceStatsTable_Object = MibTable
cbQosPoliceStatsTable = _CbQosPoliceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cbQosPoliceStatsTable.setStatus("current")
_CbQosPoliceStatsEntry_Object = MibTableRow
cbQosPoliceStatsEntry = _CbQosPoliceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1)
)
cbQosPoliceStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosPoliceStatsEntry.setStatus("current")
_CbQosPoliceConformedPktOverflow_Type = Counter32
_CbQosPoliceConformedPktOverflow_Object = MibTableColumn
cbQosPoliceConformedPktOverflow = _CbQosPoliceConformedPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 1),
    _CbQosPoliceConformedPktOverflow_Type()
)
cbQosPoliceConformedPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPktOverflow.setUnits("Packets")
_CbQosPoliceConformedPkt_Type = Counter32
_CbQosPoliceConformedPkt_Object = MibTableColumn
cbQosPoliceConformedPkt = _CbQosPoliceConformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 2),
    _CbQosPoliceConformedPkt_Type()
)
cbQosPoliceConformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPkt.setUnits("Packets")
_CbQosPoliceConformedPkt64_Type = Counter64
_CbQosPoliceConformedPkt64_Object = MibTableColumn
cbQosPoliceConformedPkt64 = _CbQosPoliceConformedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 3),
    _CbQosPoliceConformedPkt64_Type()
)
cbQosPoliceConformedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedPkt64.setUnits("Packets")
_CbQosPoliceConformedByteOverflow_Type = Counter32
_CbQosPoliceConformedByteOverflow_Object = MibTableColumn
cbQosPoliceConformedByteOverflow = _CbQosPoliceConformedByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 4),
    _CbQosPoliceConformedByteOverflow_Type()
)
cbQosPoliceConformedByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByteOverflow.setUnits("Octets")
_CbQosPoliceConformedByte_Type = Counter32
_CbQosPoliceConformedByte_Object = MibTableColumn
cbQosPoliceConformedByte = _CbQosPoliceConformedByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 5),
    _CbQosPoliceConformedByte_Type()
)
cbQosPoliceConformedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByte.setUnits("Octets")
_CbQosPoliceConformedByte64_Type = Counter64
_CbQosPoliceConformedByte64_Object = MibTableColumn
cbQosPoliceConformedByte64 = _CbQosPoliceConformedByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 6),
    _CbQosPoliceConformedByte64_Type()
)
cbQosPoliceConformedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedByte64.setUnits("Octets")
_CbQosPoliceConformedBitRate_Type = Gauge32
_CbQosPoliceConformedBitRate_Object = MibTableColumn
cbQosPoliceConformedBitRate = _CbQosPoliceConformedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 7),
    _CbQosPoliceConformedBitRate_Type()
)
cbQosPoliceConformedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedBitRate.setUnits("bits per second")
_CbQosPoliceExceededPktOverflow_Type = Counter32
_CbQosPoliceExceededPktOverflow_Object = MibTableColumn
cbQosPoliceExceededPktOverflow = _CbQosPoliceExceededPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 8),
    _CbQosPoliceExceededPktOverflow_Type()
)
cbQosPoliceExceededPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPktOverflow.setUnits("Packets")
_CbQosPoliceExceededPkt_Type = Counter32
_CbQosPoliceExceededPkt_Object = MibTableColumn
cbQosPoliceExceededPkt = _CbQosPoliceExceededPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 9),
    _CbQosPoliceExceededPkt_Type()
)
cbQosPoliceExceededPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPkt.setUnits("Packets")
_CbQosPoliceExceededPkt64_Type = Counter64
_CbQosPoliceExceededPkt64_Object = MibTableColumn
cbQosPoliceExceededPkt64 = _CbQosPoliceExceededPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 10),
    _CbQosPoliceExceededPkt64_Type()
)
cbQosPoliceExceededPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededPkt64.setUnits("Packets")
_CbQosPoliceExceededByteOverflow_Type = Counter32
_CbQosPoliceExceededByteOverflow_Object = MibTableColumn
cbQosPoliceExceededByteOverflow = _CbQosPoliceExceededByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 11),
    _CbQosPoliceExceededByteOverflow_Type()
)
cbQosPoliceExceededByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByteOverflow.setUnits("Octets")
_CbQosPoliceExceededByte_Type = Counter32
_CbQosPoliceExceededByte_Object = MibTableColumn
cbQosPoliceExceededByte = _CbQosPoliceExceededByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 12),
    _CbQosPoliceExceededByte_Type()
)
cbQosPoliceExceededByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByte.setUnits("Octets")
_CbQosPoliceExceededByte64_Type = Counter64
_CbQosPoliceExceededByte64_Object = MibTableColumn
cbQosPoliceExceededByte64 = _CbQosPoliceExceededByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 13),
    _CbQosPoliceExceededByte64_Type()
)
cbQosPoliceExceededByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededByte64.setUnits("Octets")
_CbQosPoliceExceededBitRate_Type = Gauge32
_CbQosPoliceExceededBitRate_Object = MibTableColumn
cbQosPoliceExceededBitRate = _CbQosPoliceExceededBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 14),
    _CbQosPoliceExceededBitRate_Type()
)
cbQosPoliceExceededBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededBitRate.setUnits("bits per second")
_CbQosPoliceViolatedPktOverflow_Type = Counter32
_CbQosPoliceViolatedPktOverflow_Object = MibTableColumn
cbQosPoliceViolatedPktOverflow = _CbQosPoliceViolatedPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 15),
    _CbQosPoliceViolatedPktOverflow_Type()
)
cbQosPoliceViolatedPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPktOverflow.setUnits("Packets")
_CbQosPoliceViolatedPkt_Type = Counter32
_CbQosPoliceViolatedPkt_Object = MibTableColumn
cbQosPoliceViolatedPkt = _CbQosPoliceViolatedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 16),
    _CbQosPoliceViolatedPkt_Type()
)
cbQosPoliceViolatedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPkt.setUnits("Packets")
_CbQosPoliceViolatedPkt64_Type = Counter64
_CbQosPoliceViolatedPkt64_Object = MibTableColumn
cbQosPoliceViolatedPkt64 = _CbQosPoliceViolatedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 17),
    _CbQosPoliceViolatedPkt64_Type()
)
cbQosPoliceViolatedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedPkt64.setUnits("Packets")
_CbQosPoliceViolatedByteOverflow_Type = Counter32
_CbQosPoliceViolatedByteOverflow_Object = MibTableColumn
cbQosPoliceViolatedByteOverflow = _CbQosPoliceViolatedByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 18),
    _CbQosPoliceViolatedByteOverflow_Type()
)
cbQosPoliceViolatedByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByteOverflow.setUnits("Octets")
_CbQosPoliceViolatedByte_Type = Counter32
_CbQosPoliceViolatedByte_Object = MibTableColumn
cbQosPoliceViolatedByte = _CbQosPoliceViolatedByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 19),
    _CbQosPoliceViolatedByte_Type()
)
cbQosPoliceViolatedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByte.setUnits("Octets")
_CbQosPoliceViolatedByte64_Type = Counter64
_CbQosPoliceViolatedByte64_Object = MibTableColumn
cbQosPoliceViolatedByte64 = _CbQosPoliceViolatedByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 20),
    _CbQosPoliceViolatedByte64_Type()
)
cbQosPoliceViolatedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedByte64.setUnits("Octets")
_CbQosPoliceViolatedBitRate_Type = Gauge32
_CbQosPoliceViolatedBitRate_Object = MibTableColumn
cbQosPoliceViolatedBitRate = _CbQosPoliceViolatedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 21),
    _CbQosPoliceViolatedBitRate_Type()
)
cbQosPoliceViolatedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedBitRate.setUnits("bits per second")
_CbQosPoliceConformedBitRate64_Type = CounterBasedGauge64
_CbQosPoliceConformedBitRate64_Object = MibTableColumn
cbQosPoliceConformedBitRate64 = _CbQosPoliceConformedBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 22),
    _CbQosPoliceConformedBitRate64_Type()
)
cbQosPoliceConformedBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceConformedBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceConformedBitRate64.setUnits("bits per second")
_CbQosPoliceExceededBitRate64_Type = CounterBasedGauge64
_CbQosPoliceExceededBitRate64_Object = MibTableColumn
cbQosPoliceExceededBitRate64 = _CbQosPoliceExceededBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 23),
    _CbQosPoliceExceededBitRate64_Type()
)
cbQosPoliceExceededBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExceededBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExceededBitRate64.setUnits("bits per second")
_CbQosPoliceViolatedBitRate64_Type = CounterBasedGauge64
_CbQosPoliceViolatedBitRate64_Object = MibTableColumn
cbQosPoliceViolatedBitRate64 = _CbQosPoliceViolatedBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 17, 1, 1, 24),
    _CbQosPoliceViolatedBitRate64_Type()
)
cbQosPoliceViolatedBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceViolatedBitRate64.setUnits("bits per second")
_CbQosQueueingStats_ObjectIdentity = ObjectIdentity
cbQosQueueingStats = _CbQosQueueingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18)
)
_CbQosQueueingStatsTable_Object = MibTable
cbQosQueueingStatsTable = _CbQosQueueingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cbQosQueueingStatsTable.setStatus("current")
_CbQosQueueingStatsEntry_Object = MibTableRow
cbQosQueueingStatsEntry = _CbQosQueueingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1)
)
cbQosQueueingStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosQueueingStatsEntry.setStatus("current")
_CbQosQueueingCurrentQDepth_Type = Gauge32
_CbQosQueueingCurrentQDepth_Object = MibTableColumn
cbQosQueueingCurrentQDepth = _CbQosQueueingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 1),
    _CbQosQueueingCurrentQDepth_Type()
)
cbQosQueueingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCurrentQDepth.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingCurrentQDepth.setUnits("Octets")
_CbQosQueueingMaxQDepth_Type = Gauge32
_CbQosQueueingMaxQDepth_Object = MibTableColumn
cbQosQueueingMaxQDepth = _CbQosQueueingMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 2),
    _CbQosQueueingMaxQDepth_Type()
)
cbQosQueueingMaxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingMaxQDepth.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingMaxQDepth.setUnits("Octets")
_CbQosQueueingDiscardByteOverflow_Type = Counter32
_CbQosQueueingDiscardByteOverflow_Object = MibTableColumn
cbQosQueueingDiscardByteOverflow = _CbQosQueueingDiscardByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 3),
    _CbQosQueueingDiscardByteOverflow_Type()
)
cbQosQueueingDiscardByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByteOverflow.setUnits("Octets")
_CbQosQueueingDiscardByte_Type = Counter32
_CbQosQueueingDiscardByte_Object = MibTableColumn
cbQosQueueingDiscardByte = _CbQosQueueingDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 4),
    _CbQosQueueingDiscardByte_Type()
)
cbQosQueueingDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByte.setUnits("Octets")
_CbQosQueueingDiscardByte64_Type = Counter64
_CbQosQueueingDiscardByte64_Object = MibTableColumn
cbQosQueueingDiscardByte64 = _CbQosQueueingDiscardByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 5),
    _CbQosQueueingDiscardByte64_Type()
)
cbQosQueueingDiscardByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardByte64.setUnits("Octets")
_CbQosQueueingDiscardPktOverflow_Type = Counter32
_CbQosQueueingDiscardPktOverflow_Object = MibTableColumn
cbQosQueueingDiscardPktOverflow = _CbQosQueueingDiscardPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 6),
    _CbQosQueueingDiscardPktOverflow_Type()
)
cbQosQueueingDiscardPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPktOverflow.setUnits("Packets")
_CbQosQueueingDiscardPkt_Type = Counter32
_CbQosQueueingDiscardPkt_Object = MibTableColumn
cbQosQueueingDiscardPkt = _CbQosQueueingDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 7),
    _CbQosQueueingDiscardPkt_Type()
)
cbQosQueueingDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPkt.setUnits("Packets")
_CbQosQueueingDiscardPkt64_Type = Counter64
_CbQosQueueingDiscardPkt64_Object = MibTableColumn
cbQosQueueingDiscardPkt64 = _CbQosQueueingDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 8),
    _CbQosQueueingDiscardPkt64_Type()
)
cbQosQueueingDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingDiscardPkt64.setUnits("Packets")
_CbQosQueueingCurrentQDepthPkt_Type = Gauge32
_CbQosQueueingCurrentQDepthPkt_Object = MibTableColumn
cbQosQueueingCurrentQDepthPkt = _CbQosQueueingCurrentQDepthPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 9),
    _CbQosQueueingCurrentQDepthPkt_Type()
)
cbQosQueueingCurrentQDepthPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingCurrentQDepthPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingCurrentQDepthPkt.setUnits("Packets")
_CbQosQueueingMaxQDepthPkt_Type = Gauge32
_CbQosQueueingMaxQDepthPkt_Object = MibTableColumn
cbQosQueueingMaxQDepthPkt = _CbQosQueueingMaxQDepthPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 10),
    _CbQosQueueingMaxQDepthPkt_Type()
)
cbQosQueueingMaxQDepthPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingMaxQDepthPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingMaxQDepthPkt.setUnits("Packets")
_CbQosQueueingTransmitByte64_Type = Counter64
_CbQosQueueingTransmitByte64_Object = MibTableColumn
cbQosQueueingTransmitByte64 = _CbQosQueueingTransmitByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 11),
    _CbQosQueueingTransmitByte64_Type()
)
cbQosQueueingTransmitByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingTransmitByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingTransmitByte64.setUnits("Octets")
_CbQosQueueingTransmitPkt64_Type = Counter64
_CbQosQueueingTransmitPkt64_Object = MibTableColumn
cbQosQueueingTransmitPkt64 = _CbQosQueueingTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 18, 1, 1, 12),
    _CbQosQueueingTransmitPkt64_Type()
)
cbQosQueueingTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosQueueingTransmitPkt64.setUnits("Packets")
_CbQosTSStats_ObjectIdentity = ObjectIdentity
cbQosTSStats = _CbQosTSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19)
)
_CbQosTSStatsTable_Object = MibTable
cbQosTSStatsTable = _CbQosTSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cbQosTSStatsTable.setStatus("current")
_CbQosTSStatsEntry_Object = MibTableRow
cbQosTSStatsEntry = _CbQosTSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1)
)
cbQosTSStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosTSStatsEntry.setStatus("current")
_CbQosTSStatsDelayedByteOverflow_Type = Counter32
_CbQosTSStatsDelayedByteOverflow_Object = MibTableColumn
cbQosTSStatsDelayedByteOverflow = _CbQosTSStatsDelayedByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 1),
    _CbQosTSStatsDelayedByteOverflow_Type()
)
cbQosTSStatsDelayedByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByteOverflow.setUnits("octets")
_CbQosTSStatsDelayedByte_Type = Counter32
_CbQosTSStatsDelayedByte_Object = MibTableColumn
cbQosTSStatsDelayedByte = _CbQosTSStatsDelayedByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 2),
    _CbQosTSStatsDelayedByte_Type()
)
cbQosTSStatsDelayedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByte.setUnits("octets")
_CbQosTSStatsDelayedByte64_Type = Counter64
_CbQosTSStatsDelayedByte64_Object = MibTableColumn
cbQosTSStatsDelayedByte64 = _CbQosTSStatsDelayedByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 3),
    _CbQosTSStatsDelayedByte64_Type()
)
cbQosTSStatsDelayedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedByte64.setUnits("octets")
_CbQosTSStatsDelayedPktOverflow_Type = Counter32
_CbQosTSStatsDelayedPktOverflow_Object = MibTableColumn
cbQosTSStatsDelayedPktOverflow = _CbQosTSStatsDelayedPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 4),
    _CbQosTSStatsDelayedPktOverflow_Type()
)
cbQosTSStatsDelayedPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPktOverflow.setUnits("packets")
_CbQosTSStatsDelayedPkt_Type = Counter32
_CbQosTSStatsDelayedPkt_Object = MibTableColumn
cbQosTSStatsDelayedPkt = _CbQosTSStatsDelayedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 5),
    _CbQosTSStatsDelayedPkt_Type()
)
cbQosTSStatsDelayedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPkt.setUnits("packets")
_CbQosTSStatsDelayedPkt64_Type = Counter64
_CbQosTSStatsDelayedPkt64_Object = MibTableColumn
cbQosTSStatsDelayedPkt64 = _CbQosTSStatsDelayedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 6),
    _CbQosTSStatsDelayedPkt64_Type()
)
cbQosTSStatsDelayedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDelayedPkt64.setUnits("packets")
_CbQosTSStatsDropByteOverflow_Type = Counter32
_CbQosTSStatsDropByteOverflow_Object = MibTableColumn
cbQosTSStatsDropByteOverflow = _CbQosTSStatsDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 7),
    _CbQosTSStatsDropByteOverflow_Type()
)
cbQosTSStatsDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByteOverflow.setUnits("octets")
_CbQosTSStatsDropByte_Type = Counter32
_CbQosTSStatsDropByte_Object = MibTableColumn
cbQosTSStatsDropByte = _CbQosTSStatsDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 8),
    _CbQosTSStatsDropByte_Type()
)
cbQosTSStatsDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByte.setUnits("octets")
_CbQosTSStatsDropByte64_Type = Counter64
_CbQosTSStatsDropByte64_Object = MibTableColumn
cbQosTSStatsDropByte64 = _CbQosTSStatsDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 9),
    _CbQosTSStatsDropByte64_Type()
)
cbQosTSStatsDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropByte64.setUnits("octets")
_CbQosTSStatsDropPktOverflow_Type = Counter32
_CbQosTSStatsDropPktOverflow_Object = MibTableColumn
cbQosTSStatsDropPktOverflow = _CbQosTSStatsDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 10),
    _CbQosTSStatsDropPktOverflow_Type()
)
cbQosTSStatsDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPktOverflow.setUnits("packets")
_CbQosTSStatsDropPkt_Type = Counter32
_CbQosTSStatsDropPkt_Object = MibTableColumn
cbQosTSStatsDropPkt = _CbQosTSStatsDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 11),
    _CbQosTSStatsDropPkt_Type()
)
cbQosTSStatsDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPkt.setUnits("packets")
_CbQosTSStatsDropPkt64_Type = Counter64
_CbQosTSStatsDropPkt64_Object = MibTableColumn
cbQosTSStatsDropPkt64 = _CbQosTSStatsDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 12),
    _CbQosTSStatsDropPkt64_Type()
)
cbQosTSStatsDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsDropPkt64.setUnits("packets")
_CbQosTSStatsActive_Type = TruthValue
_CbQosTSStatsActive_Object = MibTableColumn
cbQosTSStatsActive = _CbQosTSStatsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 13),
    _CbQosTSStatsActive_Type()
)
cbQosTSStatsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsActive.setStatus("current")
_CbQosTSStatsCurrentQSize_Type = Gauge32
_CbQosTSStatsCurrentQSize_Object = MibTableColumn
cbQosTSStatsCurrentQSize = _CbQosTSStatsCurrentQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 19, 1, 1, 14),
    _CbQosTSStatsCurrentQSize_Type()
)
cbQosTSStatsCurrentQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTSStatsCurrentQSize.setStatus("current")
if mibBuilder.loadTexts:
    cbQosTSStatsCurrentQSize.setUnits("packets")
_CbQosREDClassStats_ObjectIdentity = ObjectIdentity
cbQosREDClassStats = _CbQosREDClassStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20)
)
_CbQosREDClassStatsTable_Object = MibTable
cbQosREDClassStatsTable = _CbQosREDClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1)
)
if mibBuilder.loadTexts:
    cbQosREDClassStatsTable.setStatus("current")
_CbQosREDClassStatsEntry_Object = MibTableRow
cbQosREDClassStatsEntry = _CbQosREDClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1)
)
cbQosREDClassStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosREDValue"),
)
if mibBuilder.loadTexts:
    cbQosREDClassStatsEntry.setStatus("current")
_CbQosREDRandomDropPktOverflow_Type = Counter32
_CbQosREDRandomDropPktOverflow_Object = MibTableColumn
cbQosREDRandomDropPktOverflow = _CbQosREDRandomDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 1),
    _CbQosREDRandomDropPktOverflow_Type()
)
cbQosREDRandomDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPktOverflow.setUnits("Packets")
_CbQosREDRandomDropPkt_Type = Counter32
_CbQosREDRandomDropPkt_Object = MibTableColumn
cbQosREDRandomDropPkt = _CbQosREDRandomDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 2),
    _CbQosREDRandomDropPkt_Type()
)
cbQosREDRandomDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPkt.setUnits("Packets")
_CbQosREDRandomDropPkt64_Type = Counter64
_CbQosREDRandomDropPkt64_Object = MibTableColumn
cbQosREDRandomDropPkt64 = _CbQosREDRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 3),
    _CbQosREDRandomDropPkt64_Type()
)
cbQosREDRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropPkt64.setUnits("Packets")
_CbQosREDRandomDropByteOverflow_Type = Counter32
_CbQosREDRandomDropByteOverflow_Object = MibTableColumn
cbQosREDRandomDropByteOverflow = _CbQosREDRandomDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 4),
    _CbQosREDRandomDropByteOverflow_Type()
)
cbQosREDRandomDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByteOverflow.setUnits("Octets")
_CbQosREDRandomDropByte_Type = Counter32
_CbQosREDRandomDropByte_Object = MibTableColumn
cbQosREDRandomDropByte = _CbQosREDRandomDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 5),
    _CbQosREDRandomDropByte_Type()
)
cbQosREDRandomDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByte.setUnits("Octets")
_CbQosREDRandomDropByte64_Type = Counter64
_CbQosREDRandomDropByte64_Object = MibTableColumn
cbQosREDRandomDropByte64 = _CbQosREDRandomDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 6),
    _CbQosREDRandomDropByte64_Type()
)
cbQosREDRandomDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDRandomDropByte64.setUnits("Octets")
_CbQosREDTailDropPktOverflow_Type = Counter32
_CbQosREDTailDropPktOverflow_Object = MibTableColumn
cbQosREDTailDropPktOverflow = _CbQosREDTailDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 7),
    _CbQosREDTailDropPktOverflow_Type()
)
cbQosREDTailDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropPktOverflow.setUnits("Packets")
_CbQosREDTailDropPkt_Type = Counter32
_CbQosREDTailDropPkt_Object = MibTableColumn
cbQosREDTailDropPkt = _CbQosREDTailDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 8),
    _CbQosREDTailDropPkt_Type()
)
cbQosREDTailDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropPkt.setUnits("Packets")
_CbQosREDTailDropPkt64_Type = Counter64
_CbQosREDTailDropPkt64_Object = MibTableColumn
cbQosREDTailDropPkt64 = _CbQosREDTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 9),
    _CbQosREDTailDropPkt64_Type()
)
cbQosREDTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropPkt64.setUnits("Packets")
_CbQosREDTailDropByteOverflow_Type = Counter32
_CbQosREDTailDropByteOverflow_Object = MibTableColumn
cbQosREDTailDropByteOverflow = _CbQosREDTailDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 10),
    _CbQosREDTailDropByteOverflow_Type()
)
cbQosREDTailDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropByteOverflow.setUnits("Octets")
_CbQosREDTailDropByte_Type = Counter32
_CbQosREDTailDropByte_Object = MibTableColumn
cbQosREDTailDropByte = _CbQosREDTailDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 11),
    _CbQosREDTailDropByte_Type()
)
cbQosREDTailDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropByte.setUnits("Octets")
_CbQosREDTailDropByte64_Type = Counter64
_CbQosREDTailDropByte64_Object = MibTableColumn
cbQosREDTailDropByte64 = _CbQosREDTailDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 12),
    _CbQosREDTailDropByte64_Type()
)
cbQosREDTailDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTailDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTailDropByte64.setUnits("Octets")
_CbQosREDTransmitPktOverflow_Type = Counter32
_CbQosREDTransmitPktOverflow_Object = MibTableColumn
cbQosREDTransmitPktOverflow = _CbQosREDTransmitPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 13),
    _CbQosREDTransmitPktOverflow_Type()
)
cbQosREDTransmitPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitPktOverflow.setUnits("Packets")
_CbQosREDTransmitPkt_Type = Counter32
_CbQosREDTransmitPkt_Object = MibTableColumn
cbQosREDTransmitPkt = _CbQosREDTransmitPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 14),
    _CbQosREDTransmitPkt_Type()
)
cbQosREDTransmitPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitPkt.setUnits("Packets")
_CbQosREDTransmitPkt64_Type = Counter64
_CbQosREDTransmitPkt64_Object = MibTableColumn
cbQosREDTransmitPkt64 = _CbQosREDTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 15),
    _CbQosREDTransmitPkt64_Type()
)
cbQosREDTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitPkt64.setUnits("Packets")
_CbQosREDTransmitByteOverflow_Type = Counter32
_CbQosREDTransmitByteOverflow_Object = MibTableColumn
cbQosREDTransmitByteOverflow = _CbQosREDTransmitByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 16),
    _CbQosREDTransmitByteOverflow_Type()
)
cbQosREDTransmitByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitByteOverflow.setUnits("Octets")
_CbQosREDTransmitByte_Type = Counter32
_CbQosREDTransmitByte_Object = MibTableColumn
cbQosREDTransmitByte = _CbQosREDTransmitByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 17),
    _CbQosREDTransmitByte_Type()
)
cbQosREDTransmitByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitByte.setUnits("Octets")
_CbQosREDTransmitByte64_Type = Counter64
_CbQosREDTransmitByte64_Object = MibTableColumn
cbQosREDTransmitByte64 = _CbQosREDTransmitByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 18),
    _CbQosREDTransmitByte64_Type()
)
cbQosREDTransmitByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDTransmitByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDTransmitByte64.setUnits("Octets")
_CbQosREDECNMarkPktOverflow_Type = Counter32
_CbQosREDECNMarkPktOverflow_Object = MibTableColumn
cbQosREDECNMarkPktOverflow = _CbQosREDECNMarkPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 19),
    _CbQosREDECNMarkPktOverflow_Type()
)
cbQosREDECNMarkPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPktOverflow.setUnits("Packets")
_CbQosREDECNMarkPkt_Type = Counter32
_CbQosREDECNMarkPkt_Object = MibTableColumn
cbQosREDECNMarkPkt = _CbQosREDECNMarkPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 20),
    _CbQosREDECNMarkPkt_Type()
)
cbQosREDECNMarkPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPkt.setUnits("Packets")
_CbQosREDECNMarkPkt64_Type = Counter64
_CbQosREDECNMarkPkt64_Object = MibTableColumn
cbQosREDECNMarkPkt64 = _CbQosREDECNMarkPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 21),
    _CbQosREDECNMarkPkt64_Type()
)
cbQosREDECNMarkPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkPkt64.setUnits("Packets")
_CbQosREDECNMarkByteOverflow_Type = Counter32
_CbQosREDECNMarkByteOverflow_Object = MibTableColumn
cbQosREDECNMarkByteOverflow = _CbQosREDECNMarkByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 22),
    _CbQosREDECNMarkByteOverflow_Type()
)
cbQosREDECNMarkByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByteOverflow.setUnits("Octets")
_CbQosREDECNMarkByte_Type = Counter32
_CbQosREDECNMarkByte_Object = MibTableColumn
cbQosREDECNMarkByte = _CbQosREDECNMarkByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 23),
    _CbQosREDECNMarkByte_Type()
)
cbQosREDECNMarkByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByte.setUnits("Octets")
_CbQosREDECNMarkByte64_Type = Counter64
_CbQosREDECNMarkByte64_Object = MibTableColumn
cbQosREDECNMarkByte64 = _CbQosREDECNMarkByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 24),
    _CbQosREDECNMarkByte64_Type()
)
cbQosREDECNMarkByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosREDECNMarkByte64.setUnits("Octets")
_CbQosREDMeanQSizeUnits_Type = CbQosQueueUnitType
_CbQosREDMeanQSizeUnits_Object = MibTableColumn
cbQosREDMeanQSizeUnits = _CbQosREDMeanQSizeUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 25),
    _CbQosREDMeanQSizeUnits_Type()
)
cbQosREDMeanQSizeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDMeanQSizeUnits.setStatus("current")
_CbQosREDMeanQSize_Type = CbQosQueueDepth
_CbQosREDMeanQSize_Object = MibTableColumn
cbQosREDMeanQSize = _CbQosREDMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 20, 1, 1, 26),
    _CbQosREDMeanQSize_Type()
)
cbQosREDMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosREDMeanQSize.setStatus("current")
_CbQosPoliceActionCfg_ObjectIdentity = ObjectIdentity
cbQosPoliceActionCfg = _CbQosPoliceActionCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21)
)
_CbQosPoliceActionCfgTable_Object = MibTable
cbQosPoliceActionCfgTable = _CbQosPoliceActionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1)
)
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgTable.setStatus("current")
_CbQosPoliceActionCfgEntry_Object = MibTableRow
cbQosPoliceActionCfgEntry = _CbQosPoliceActionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1)
)
cbQosPoliceActionCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgIndex"),
)
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgEntry.setStatus("current")
_CbQosPoliceActionCfgIndex_Type = Unsigned32
_CbQosPoliceActionCfgIndex_Object = MibTableColumn
cbQosPoliceActionCfgIndex = _CbQosPoliceActionCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 1),
    _CbQosPoliceActionCfgIndex_Type()
)
cbQosPoliceActionCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgIndex.setStatus("current")
_CbQosPoliceActionCfgConform_Type = PoliceAction
_CbQosPoliceActionCfgConform_Object = MibTableColumn
cbQosPoliceActionCfgConform = _CbQosPoliceActionCfgConform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 2),
    _CbQosPoliceActionCfgConform_Type()
)
cbQosPoliceActionCfgConform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgConform.setStatus("current")


class _CbQosPoliceActionCfgConformSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceActionCfgConformSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosPoliceActionCfgConformSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceActionCfgConformSetValue_Object = MibTableColumn
cbQosPoliceActionCfgConformSetValue = _CbQosPoliceActionCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 3),
    _CbQosPoliceActionCfgConformSetValue_Type()
)
cbQosPoliceActionCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgConformSetValue.setStatus("current")
_CbQosPoliceActionCfgExceed_Type = PoliceAction
_CbQosPoliceActionCfgExceed_Object = MibTableColumn
cbQosPoliceActionCfgExceed = _CbQosPoliceActionCfgExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 4),
    _CbQosPoliceActionCfgExceed_Type()
)
cbQosPoliceActionCfgExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgExceed.setStatus("current")


class _CbQosPoliceActionCfgExceedSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceActionCfgExceedSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosPoliceActionCfgExceedSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceActionCfgExceedSetValue_Object = MibTableColumn
cbQosPoliceActionCfgExceedSetValue = _CbQosPoliceActionCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 5),
    _CbQosPoliceActionCfgExceedSetValue_Type()
)
cbQosPoliceActionCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgExceedSetValue.setStatus("current")
_CbQosPoliceActionCfgViolate_Type = PoliceAction
_CbQosPoliceActionCfgViolate_Object = MibTableColumn
cbQosPoliceActionCfgViolate = _CbQosPoliceActionCfgViolate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 6),
    _CbQosPoliceActionCfgViolate_Type()
)
cbQosPoliceActionCfgViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgViolate.setStatus("current")


class _CbQosPoliceActionCfgViolateSetValue_Type(Unsigned32):
    """Custom type cbQosPoliceActionCfgViolateSetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosPoliceActionCfgViolateSetValue_Type.__name__ = "Unsigned32"
_CbQosPoliceActionCfgViolateSetValue_Object = MibTableColumn
cbQosPoliceActionCfgViolateSetValue = _CbQosPoliceActionCfgViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 21, 1, 1, 7),
    _CbQosPoliceActionCfgViolateSetValue_Type()
)
cbQosPoliceActionCfgViolateSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgViolateSetValue.setStatus("current")
_CbQosIPHCCfg_ObjectIdentity = ObjectIdentity
cbQosIPHCCfg = _CbQosIPHCCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 22)
)
_CbQosIPHCCfgTable_Object = MibTable
cbQosIPHCCfgTable = _CbQosIPHCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cbQosIPHCCfgTable.setStatus("current")
_CbQosIPHCCfgEntry_Object = MibTableRow
cbQosIPHCCfgEntry = _CbQosIPHCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 22, 1, 1)
)
cbQosIPHCCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosIPHCCfgEntry.setStatus("current")
_CbQosIPHCCfgOption_Type = IPHCOption
_CbQosIPHCCfgOption_Object = MibTableColumn
cbQosIPHCCfgOption = _CbQosIPHCCfgOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 22, 1, 1, 1),
    _CbQosIPHCCfgOption_Type()
)
cbQosIPHCCfgOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCCfgOption.setStatus("current")
_CbQosIPHCCfgEnabled_Type = TruthValue
_CbQosIPHCCfgEnabled_Object = MibTableColumn
cbQosIPHCCfgEnabled = _CbQosIPHCCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 22, 1, 1, 2),
    _CbQosIPHCCfgEnabled_Type()
)
cbQosIPHCCfgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCCfgEnabled.setStatus("current")
_CbQosIPHCStats_ObjectIdentity = ObjectIdentity
cbQosIPHCStats = _CbQosIPHCStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23)
)
_CbQosIPHCStatsTable_Object = MibTable
cbQosIPHCStatsTable = _CbQosIPHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1)
)
if mibBuilder.loadTexts:
    cbQosIPHCStatsTable.setStatus("current")
_CbQosIPHCStatsEntry_Object = MibTableRow
cbQosIPHCStatsEntry = _CbQosIPHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1)
)
cbQosIPHCStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosIPHCStatsEntry.setStatus("current")
_CbQosIPHCRtpSentPktOverflow_Type = Counter32
_CbQosIPHCRtpSentPktOverflow_Object = MibTableColumn
cbQosIPHCRtpSentPktOverflow = _CbQosIPHCRtpSentPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 1),
    _CbQosIPHCRtpSentPktOverflow_Type()
)
cbQosIPHCRtpSentPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPktOverflow.setUnits("Packets")
_CbQosIPHCRtpSentPkt_Type = Counter32
_CbQosIPHCRtpSentPkt_Object = MibTableColumn
cbQosIPHCRtpSentPkt = _CbQosIPHCRtpSentPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 2),
    _CbQosIPHCRtpSentPkt_Type()
)
cbQosIPHCRtpSentPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPkt.setUnits("Packets")
_CbQosIPHCRtpSentPkt64_Type = Counter64
_CbQosIPHCRtpSentPkt64_Object = MibTableColumn
cbQosIPHCRtpSentPkt64 = _CbQosIPHCRtpSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 3),
    _CbQosIPHCRtpSentPkt64_Type()
)
cbQosIPHCRtpSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentPkt64.setUnits("Packets")
_CbQosIPHCRtpCmprsOutPktOverflow_Type = Counter32
_CbQosIPHCRtpCmprsOutPktOverflow_Object = MibTableColumn
cbQosIPHCRtpCmprsOutPktOverflow = _CbQosIPHCRtpCmprsOutPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 4),
    _CbQosIPHCRtpCmprsOutPktOverflow_Type()
)
cbQosIPHCRtpCmprsOutPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPktOverflow.setUnits("Packets")
_CbQosIPHCRtpCmprsOutPkt_Type = Counter32
_CbQosIPHCRtpCmprsOutPkt_Object = MibTableColumn
cbQosIPHCRtpCmprsOutPkt = _CbQosIPHCRtpCmprsOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 5),
    _CbQosIPHCRtpCmprsOutPkt_Type()
)
cbQosIPHCRtpCmprsOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPkt.setUnits("Packets")
_CbQosIPHCRtpCmprsOutPkt64_Type = Counter64
_CbQosIPHCRtpCmprsOutPkt64_Object = MibTableColumn
cbQosIPHCRtpCmprsOutPkt64 = _CbQosIPHCRtpCmprsOutPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 6),
    _CbQosIPHCRtpCmprsOutPkt64_Type()
)
cbQosIPHCRtpCmprsOutPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpCmprsOutPkt64.setUnits("Packets")
_CbQosIPHCRtpSavedByteOverflow_Type = Counter32
_CbQosIPHCRtpSavedByteOverflow_Object = MibTableColumn
cbQosIPHCRtpSavedByteOverflow = _CbQosIPHCRtpSavedByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 7),
    _CbQosIPHCRtpSavedByteOverflow_Type()
)
cbQosIPHCRtpSavedByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByteOverflow.setUnits("Octets")
_CbQosIPHCRtpSavedByte_Type = Counter32
_CbQosIPHCRtpSavedByte_Object = MibTableColumn
cbQosIPHCRtpSavedByte = _CbQosIPHCRtpSavedByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 8),
    _CbQosIPHCRtpSavedByte_Type()
)
cbQosIPHCRtpSavedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByte.setUnits("Octets")
_CbQosIPHCRtpSavedByte64_Type = Counter64
_CbQosIPHCRtpSavedByte64_Object = MibTableColumn
cbQosIPHCRtpSavedByte64 = _CbQosIPHCRtpSavedByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 9),
    _CbQosIPHCRtpSavedByte64_Type()
)
cbQosIPHCRtpSavedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSavedByte64.setUnits("Octets")
_CbQosIPHCRtpSentByteOverflow_Type = Counter32
_CbQosIPHCRtpSentByteOverflow_Object = MibTableColumn
cbQosIPHCRtpSentByteOverflow = _CbQosIPHCRtpSentByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 10),
    _CbQosIPHCRtpSentByteOverflow_Type()
)
cbQosIPHCRtpSentByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByteOverflow.setUnits("Octets")
_CbQosIPHCRtpSentByte_Type = Counter32
_CbQosIPHCRtpSentByte_Object = MibTableColumn
cbQosIPHCRtpSentByte = _CbQosIPHCRtpSentByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 11),
    _CbQosIPHCRtpSentByte_Type()
)
cbQosIPHCRtpSentByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByte.setUnits("Octets")
_CbQosIPHCRtpSentByte64_Type = Counter64
_CbQosIPHCRtpSentByte64_Object = MibTableColumn
cbQosIPHCRtpSentByte64 = _CbQosIPHCRtpSentByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 12),
    _CbQosIPHCRtpSentByte64_Type()
)
cbQosIPHCRtpSentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByte64.setUnits("Octets")
_CbQosIPHCRtpSentByteRate_Type = Gauge32
_CbQosIPHCRtpSentByteRate_Object = MibTableColumn
cbQosIPHCRtpSentByteRate = _CbQosIPHCRtpSentByteRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 13),
    _CbQosIPHCRtpSentByteRate_Type()
)
cbQosIPHCRtpSentByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByteRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpSentByteRate.setUnits("Octets per second")
_CbQosIPHCTcpSentPktOverflow_Type = Counter32
_CbQosIPHCTcpSentPktOverflow_Object = MibTableColumn
cbQosIPHCTcpSentPktOverflow = _CbQosIPHCTcpSentPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 14),
    _CbQosIPHCTcpSentPktOverflow_Type()
)
cbQosIPHCTcpSentPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPktOverflow.setUnits("Packets")
_CbQosIPHCTcpSentPkt_Type = Counter32
_CbQosIPHCTcpSentPkt_Object = MibTableColumn
cbQosIPHCTcpSentPkt = _CbQosIPHCTcpSentPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 15),
    _CbQosIPHCTcpSentPkt_Type()
)
cbQosIPHCTcpSentPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPkt.setUnits("Packets")
_CbQosIPHCTcpSentPkt64_Type = Counter64
_CbQosIPHCTcpSentPkt64_Object = MibTableColumn
cbQosIPHCTcpSentPkt64 = _CbQosIPHCTcpSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 16),
    _CbQosIPHCTcpSentPkt64_Type()
)
cbQosIPHCTcpSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentPkt64.setUnits("Packets")
_CbQosIPHCTcpCmprsOutPktOverflow_Type = Counter32
_CbQosIPHCTcpCmprsOutPktOverflow_Object = MibTableColumn
cbQosIPHCTcpCmprsOutPktOverflow = _CbQosIPHCTcpCmprsOutPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 17),
    _CbQosIPHCTcpCmprsOutPktOverflow_Type()
)
cbQosIPHCTcpCmprsOutPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPktOverflow.setUnits("Packets")
_CbQosIPHCTcpCmprsOutPkt_Type = Counter32
_CbQosIPHCTcpCmprsOutPkt_Object = MibTableColumn
cbQosIPHCTcpCmprsOutPkt = _CbQosIPHCTcpCmprsOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 18),
    _CbQosIPHCTcpCmprsOutPkt_Type()
)
cbQosIPHCTcpCmprsOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPkt.setUnits("Packets")
_CbQosIPHCTcpCmprsOutPkt64_Type = Counter64
_CbQosIPHCTcpCmprsOutPkt64_Object = MibTableColumn
cbQosIPHCTcpCmprsOutPkt64 = _CbQosIPHCTcpCmprsOutPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 19),
    _CbQosIPHCTcpCmprsOutPkt64_Type()
)
cbQosIPHCTcpCmprsOutPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpCmprsOutPkt64.setUnits("Packets")
_CbQosIPHCTcpSavedByteOverflow_Type = Counter32
_CbQosIPHCTcpSavedByteOverflow_Object = MibTableColumn
cbQosIPHCTcpSavedByteOverflow = _CbQosIPHCTcpSavedByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 20),
    _CbQosIPHCTcpSavedByteOverflow_Type()
)
cbQosIPHCTcpSavedByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByteOverflow.setUnits("Octets")
_CbQosIPHCTcpSavedByte_Type = Counter32
_CbQosIPHCTcpSavedByte_Object = MibTableColumn
cbQosIPHCTcpSavedByte = _CbQosIPHCTcpSavedByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 21),
    _CbQosIPHCTcpSavedByte_Type()
)
cbQosIPHCTcpSavedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByte.setUnits("Octets")
_CbQosIPHCTcpSavedByte64_Type = Counter64
_CbQosIPHCTcpSavedByte64_Object = MibTableColumn
cbQosIPHCTcpSavedByte64 = _CbQosIPHCTcpSavedByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 22),
    _CbQosIPHCTcpSavedByte64_Type()
)
cbQosIPHCTcpSavedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSavedByte64.setUnits("Octets")
_CbQosIPHCTcpSentByteOverflow_Type = Counter32
_CbQosIPHCTcpSentByteOverflow_Object = MibTableColumn
cbQosIPHCTcpSentByteOverflow = _CbQosIPHCTcpSentByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 23),
    _CbQosIPHCTcpSentByteOverflow_Type()
)
cbQosIPHCTcpSentByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByteOverflow.setUnits("Octets")
_CbQosIPHCTcpSentByte_Type = Counter32
_CbQosIPHCTcpSentByte_Object = MibTableColumn
cbQosIPHCTcpSentByte = _CbQosIPHCTcpSentByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 24),
    _CbQosIPHCTcpSentByte_Type()
)
cbQosIPHCTcpSentByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByte.setUnits("Octets")
_CbQosIPHCTcpSentByte64_Type = Counter64
_CbQosIPHCTcpSentByte64_Object = MibTableColumn
cbQosIPHCTcpSentByte64 = _CbQosIPHCTcpSentByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 25),
    _CbQosIPHCTcpSentByte64_Type()
)
cbQosIPHCTcpSentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByte64.setUnits("Octets")
_CbQosIPHCTcpSentByteRate_Type = Gauge32
_CbQosIPHCTcpSentByteRate_Object = MibTableColumn
cbQosIPHCTcpSentByteRate = _CbQosIPHCTcpSentByteRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 26),
    _CbQosIPHCTcpSentByteRate_Type()
)
cbQosIPHCTcpSentByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByteRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpSentByteRate.setUnits("Octets per second")
_CbQosIPHCRtpFullHdrSentPktOverflow_Type = Counter64
_CbQosIPHCRtpFullHdrSentPktOverflow_Object = MibTableColumn
cbQosIPHCRtpFullHdrSentPktOverflow = _CbQosIPHCRtpFullHdrSentPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 27),
    _CbQosIPHCRtpFullHdrSentPktOverflow_Type()
)
cbQosIPHCRtpFullHdrSentPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPktOverflow.setUnits("Packets")
_CbQosIPHCRtpFullHdrSentPkt_Type = Counter64
_CbQosIPHCRtpFullHdrSentPkt_Object = MibTableColumn
cbQosIPHCRtpFullHdrSentPkt = _CbQosIPHCRtpFullHdrSentPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 28),
    _CbQosIPHCRtpFullHdrSentPkt_Type()
)
cbQosIPHCRtpFullHdrSentPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPkt.setUnits("Packets")
_CbQosIPHCRtpFullHdrSentPkt64_Type = Counter64
_CbQosIPHCRtpFullHdrSentPkt64_Object = MibTableColumn
cbQosIPHCRtpFullHdrSentPkt64 = _CbQosIPHCRtpFullHdrSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 29),
    _CbQosIPHCRtpFullHdrSentPkt64_Type()
)
cbQosIPHCRtpFullHdrSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCRtpFullHdrSentPkt64.setUnits("Packets")
_CbQosIPHCTcpFullHdrSentPktOverflow_Type = Counter64
_CbQosIPHCTcpFullHdrSentPktOverflow_Object = MibTableColumn
cbQosIPHCTcpFullHdrSentPktOverflow = _CbQosIPHCTcpFullHdrSentPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 30),
    _CbQosIPHCTcpFullHdrSentPktOverflow_Type()
)
cbQosIPHCTcpFullHdrSentPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPktOverflow.setUnits("Packets")
_CbQosIPHCTcpFullHdrSentPkt_Type = Counter64
_CbQosIPHCTcpFullHdrSentPkt_Object = MibTableColumn
cbQosIPHCTcpFullHdrSentPkt = _CbQosIPHCTcpFullHdrSentPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 31),
    _CbQosIPHCTcpFullHdrSentPkt_Type()
)
cbQosIPHCTcpFullHdrSentPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPkt.setUnits("Packets")
_CbQosIPHCTcpFullHdrSentPkt64_Type = Counter64
_CbQosIPHCTcpFullHdrSentPkt64_Object = MibTableColumn
cbQosIPHCTcpFullHdrSentPkt64 = _CbQosIPHCTcpFullHdrSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 23, 1, 1, 32),
    _CbQosIPHCTcpFullHdrSentPkt64_Type()
)
cbQosIPHCTcpFullHdrSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosIPHCTcpFullHdrSentPkt64.setUnits("Packets")
_CbQosSetStats_ObjectIdentity = ObjectIdentity
cbQosSetStats = _CbQosSetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24)
)
_CbQosSetStatsTable_Object = MibTable
cbQosSetStatsTable = _CbQosSetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1)
)
if mibBuilder.loadTexts:
    cbQosSetStatsTable.setStatus("current")
_CbQosSetStatsEntry_Object = MibTableRow
cbQosSetStatsEntry = _CbQosSetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1)
)
cbQosSetStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosSetStatsEntry.setStatus("current")
_CbQosSetDscpPkt64_Type = Counter64
_CbQosSetDscpPkt64_Object = MibTableColumn
cbQosSetDscpPkt64 = _CbQosSetDscpPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 1),
    _CbQosSetDscpPkt64_Type()
)
cbQosSetDscpPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetDscpPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetDscpPkt64.setUnits("Packets")
_CbQosSetPrecedencePkt64_Type = Counter64
_CbQosSetPrecedencePkt64_Object = MibTableColumn
cbQosSetPrecedencePkt64 = _CbQosSetPrecedencePkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 2),
    _CbQosSetPrecedencePkt64_Type()
)
cbQosSetPrecedencePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetPrecedencePkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetPrecedencePkt64.setUnits("Packets")
_CbQosSetQosGroupPkt64_Type = Counter64
_CbQosSetQosGroupPkt64_Object = MibTableColumn
cbQosSetQosGroupPkt64 = _CbQosSetQosGroupPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 3),
    _CbQosSetQosGroupPkt64_Type()
)
cbQosSetQosGroupPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetQosGroupPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetQosGroupPkt64.setUnits("Packets")
_CbQosSetFrDePkt64_Type = Counter64
_CbQosSetFrDePkt64_Object = MibTableColumn
cbQosSetFrDePkt64 = _CbQosSetFrDePkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 4),
    _CbQosSetFrDePkt64_Type()
)
cbQosSetFrDePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetFrDePkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetFrDePkt64.setUnits("Packets")
_CbQosSetAtmClpPkt64_Type = Counter64
_CbQosSetAtmClpPkt64_Object = MibTableColumn
cbQosSetAtmClpPkt64 = _CbQosSetAtmClpPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 5),
    _CbQosSetAtmClpPkt64_Type()
)
cbQosSetAtmClpPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetAtmClpPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetAtmClpPkt64.setUnits("Packets")
_CbQosSetL2CosPkt64_Type = Counter64
_CbQosSetL2CosPkt64_Object = MibTableColumn
cbQosSetL2CosPkt64 = _CbQosSetL2CosPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 6),
    _CbQosSetL2CosPkt64_Type()
)
cbQosSetL2CosPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetL2CosPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetL2CosPkt64.setUnits("Packets")
_CbQosSetMplsExpImpositionPkt64_Type = Counter64
_CbQosSetMplsExpImpositionPkt64_Object = MibTableColumn
cbQosSetMplsExpImpositionPkt64 = _CbQosSetMplsExpImpositionPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 7),
    _CbQosSetMplsExpImpositionPkt64_Type()
)
cbQosSetMplsExpImpositionPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetMplsExpImpositionPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetMplsExpImpositionPkt64.setUnits("Packets")
_CbQosSetDiscardClassPkt64_Type = Counter64
_CbQosSetDiscardClassPkt64_Object = MibTableColumn
cbQosSetDiscardClassPkt64 = _CbQosSetDiscardClassPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 8),
    _CbQosSetDiscardClassPkt64_Type()
)
cbQosSetDiscardClassPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetDiscardClassPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetDiscardClassPkt64.setUnits("Packets")
_CbQosSetMplsExpTopMostPkt64_Type = Counter64
_CbQosSetMplsExpTopMostPkt64_Object = MibTableColumn
cbQosSetMplsExpTopMostPkt64 = _CbQosSetMplsExpTopMostPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 9),
    _CbQosSetMplsExpTopMostPkt64_Type()
)
cbQosSetMplsExpTopMostPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetMplsExpTopMostPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetMplsExpTopMostPkt64.setUnits("Packets")
_CbQosSetSrpPriorityPkt64_Type = Counter64
_CbQosSetSrpPriorityPkt64_Object = MibTableColumn
cbQosSetSrpPriorityPkt64 = _CbQosSetSrpPriorityPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 10),
    _CbQosSetSrpPriorityPkt64_Type()
)
cbQosSetSrpPriorityPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetSrpPriorityPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetSrpPriorityPkt64.setUnits("Packets")
_CbQosSetFrFecnBecnPkt64_Type = Counter64
_CbQosSetFrFecnBecnPkt64_Object = MibTableColumn
cbQosSetFrFecnBecnPkt64 = _CbQosSetFrFecnBecnPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 11),
    _CbQosSetFrFecnBecnPkt64_Type()
)
cbQosSetFrFecnBecnPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetFrFecnBecnPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetFrFecnBecnPkt64.setUnits("Packets")
_CbQosSetDscpTunnelPkt64_Type = Counter64
_CbQosSetDscpTunnelPkt64_Object = MibTableColumn
cbQosSetDscpTunnelPkt64 = _CbQosSetDscpTunnelPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 12),
    _CbQosSetDscpTunnelPkt64_Type()
)
cbQosSetDscpTunnelPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetDscpTunnelPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetDscpTunnelPkt64.setUnits("Packets")
_CbQosSetPrecedenceTunnelPkt64_Type = Counter64
_CbQosSetPrecedenceTunnelPkt64_Object = MibTableColumn
cbQosSetPrecedenceTunnelPkt64 = _CbQosSetPrecedenceTunnelPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 24, 1, 1, 13),
    _CbQosSetPrecedenceTunnelPkt64_Type()
)
cbQosSetPrecedenceTunnelPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosSetPrecedenceTunnelPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosSetPrecedenceTunnelPkt64.setUnits("Packets")
_CbQosPoliceColorStats_ObjectIdentity = ObjectIdentity
cbQosPoliceColorStats = _CbQosPoliceColorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25)
)
_CbQosPoliceColorStatsTable_Object = MibTable
cbQosPoliceColorStatsTable = _CbQosPoliceColorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cbQosPoliceColorStatsTable.setStatus("current")
_CbQosPoliceColorStatsEntry_Object = MibTableRow
cbQosPoliceColorStatsEntry = _CbQosPoliceColorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1)
)
cbQosPoliceColorStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosPoliceColorStatsEntry.setStatus("current")
_CbQosPoliceCfmColorCfmPkt64_Type = Counter64
_CbQosPoliceCfmColorCfmPkt64_Object = MibTableColumn
cbQosPoliceCfmColorCfmPkt64 = _CbQosPoliceCfmColorCfmPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 1),
    _CbQosPoliceCfmColorCfmPkt64_Type()
)
cbQosPoliceCfmColorCfmPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmPkt64.setUnits("Packets")
_CbQosPoliceCfmColorCfmByte64_Type = Counter64
_CbQosPoliceCfmColorCfmByte64_Object = MibTableColumn
cbQosPoliceCfmColorCfmByte64 = _CbQosPoliceCfmColorCfmByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 2),
    _CbQosPoliceCfmColorCfmByte64_Type()
)
cbQosPoliceCfmColorCfmByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmByte64.setUnits("Octets")
_CbQosPoliceCfmColorExdPkt64_Type = Counter64
_CbQosPoliceCfmColorExdPkt64_Object = MibTableColumn
cbQosPoliceCfmColorExdPkt64 = _CbQosPoliceCfmColorExdPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 3),
    _CbQosPoliceCfmColorExdPkt64_Type()
)
cbQosPoliceCfmColorExdPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdPkt64.setUnits("Packets")
_CbQosPoliceCfmColorExdByte64_Type = Counter64
_CbQosPoliceCfmColorExdByte64_Object = MibTableColumn
cbQosPoliceCfmColorExdByte64 = _CbQosPoliceCfmColorExdByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 4),
    _CbQosPoliceCfmColorExdByte64_Type()
)
cbQosPoliceCfmColorExdByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdByte64.setUnits("Octets")
_CbQosPoliceCfmColorVltPkt64_Type = Counter64
_CbQosPoliceCfmColorVltPkt64_Object = MibTableColumn
cbQosPoliceCfmColorVltPkt64 = _CbQosPoliceCfmColorVltPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 5),
    _CbQosPoliceCfmColorVltPkt64_Type()
)
cbQosPoliceCfmColorVltPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltPkt64.setUnits("Packets")
_CbQosPoliceCfmColorVltByte64_Type = Counter64
_CbQosPoliceCfmColorVltByte64_Object = MibTableColumn
cbQosPoliceCfmColorVltByte64 = _CbQosPoliceCfmColorVltByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 6),
    _CbQosPoliceCfmColorVltByte64_Type()
)
cbQosPoliceCfmColorVltByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltByte64.setUnits("Octets")
_CbQosPoliceExdColorExdPkt64_Type = Counter64
_CbQosPoliceExdColorExdPkt64_Object = MibTableColumn
cbQosPoliceExdColorExdPkt64 = _CbQosPoliceExdColorExdPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 7),
    _CbQosPoliceExdColorExdPkt64_Type()
)
cbQosPoliceExdColorExdPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdPkt64.setUnits("Packets")
_CbQosPoliceExdColorExdByte64_Type = Counter64
_CbQosPoliceExdColorExdByte64_Object = MibTableColumn
cbQosPoliceExdColorExdByte64 = _CbQosPoliceExdColorExdByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 8),
    _CbQosPoliceExdColorExdByte64_Type()
)
cbQosPoliceExdColorExdByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdByte64.setUnits("Octets")
_CbQosPoliceExdColorVltPkt64_Type = Counter64
_CbQosPoliceExdColorVltPkt64_Object = MibTableColumn
cbQosPoliceExdColorVltPkt64 = _CbQosPoliceExdColorVltPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 9),
    _CbQosPoliceExdColorVltPkt64_Type()
)
cbQosPoliceExdColorVltPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltPkt64.setUnits("Packets")
_CbQosPoliceExdColorVltByte64_Type = Counter64
_CbQosPoliceExdColorVltByte64_Object = MibTableColumn
cbQosPoliceExdColorVltByte64 = _CbQosPoliceExdColorVltByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 10),
    _CbQosPoliceExdColorVltByte64_Type()
)
cbQosPoliceExdColorVltByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltByte64.setUnits("Octets")
_CbQosPoliceVltColorVltPkt64_Type = Counter64
_CbQosPoliceVltColorVltPkt64_Object = MibTableColumn
cbQosPoliceVltColorVltPkt64 = _CbQosPoliceVltColorVltPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 11),
    _CbQosPoliceVltColorVltPkt64_Type()
)
cbQosPoliceVltColorVltPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltPkt64.setUnits("Packets")
_CbQosPoliceVltColorVltByte64_Type = Counter64
_CbQosPoliceVltColorVltByte64_Object = MibTableColumn
cbQosPoliceVltColorVltByte64 = _CbQosPoliceVltColorVltByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 12),
    _CbQosPoliceVltColorVltByte64_Type()
)
cbQosPoliceVltColorVltByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltByte64.setUnits("Octets")
_CbQosPoliceCfmColorCfmBitRate_Type = CounterBasedGauge64
_CbQosPoliceCfmColorCfmBitRate_Object = MibTableColumn
cbQosPoliceCfmColorCfmBitRate = _CbQosPoliceCfmColorCfmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 13),
    _CbQosPoliceCfmColorCfmBitRate_Type()
)
cbQosPoliceCfmColorCfmBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorCfmBitRate.setUnits("bits per second")
_CbQosPoliceCfmColorExdBitRate_Type = CounterBasedGauge64
_CbQosPoliceCfmColorExdBitRate_Object = MibTableColumn
cbQosPoliceCfmColorExdBitRate = _CbQosPoliceCfmColorExdBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 14),
    _CbQosPoliceCfmColorExdBitRate_Type()
)
cbQosPoliceCfmColorExdBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorExdBitRate.setUnits("bits per second")
_CbQosPoliceCfmColorVltBitRate_Type = CounterBasedGauge64
_CbQosPoliceCfmColorVltBitRate_Object = MibTableColumn
cbQosPoliceCfmColorVltBitRate = _CbQosPoliceCfmColorVltBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 15),
    _CbQosPoliceCfmColorVltBitRate_Type()
)
cbQosPoliceCfmColorVltBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceCfmColorVltBitRate.setUnits("bits per second")
_CbQosPoliceExdColorExdBitRate_Type = CounterBasedGauge64
_CbQosPoliceExdColorExdBitRate_Object = MibTableColumn
cbQosPoliceExdColorExdBitRate = _CbQosPoliceExdColorExdBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 16),
    _CbQosPoliceExdColorExdBitRate_Type()
)
cbQosPoliceExdColorExdBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorExdBitRate.setUnits("bits per second")
_CbQosPoliceExdColorVltBitRate_Type = CounterBasedGauge64
_CbQosPoliceExdColorVltBitRate_Object = MibTableColumn
cbQosPoliceExdColorVltBitRate = _CbQosPoliceExdColorVltBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 17),
    _CbQosPoliceExdColorVltBitRate_Type()
)
cbQosPoliceExdColorVltBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceExdColorVltBitRate.setUnits("bits per second")
_CbQosPoliceVltColorVltBitRate_Type = CounterBasedGauge64
_CbQosPoliceVltColorVltBitRate_Object = MibTableColumn
cbQosPoliceVltColorVltBitRate = _CbQosPoliceVltColorVltBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 25, 1, 1, 18),
    _CbQosPoliceVltColorVltBitRate_Type()
)
cbQosPoliceVltColorVltBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cbQosPoliceVltColorVltBitRate.setUnits("bits per second")
_CbQosTableMapCfg_ObjectIdentity = ObjectIdentity
cbQosTableMapCfg = _CbQosTableMapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26)
)
_CbQosTableMapCfgTable_Object = MibTable
cbQosTableMapCfgTable = _CbQosTableMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cbQosTableMapCfgTable.setStatus("current")
_CbQosTableMapCfgEntry_Object = MibTableRow
cbQosTableMapCfgEntry = _CbQosTableMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1, 1)
)
cbQosTableMapCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapCfgIndex"),
)
if mibBuilder.loadTexts:
    cbQosTableMapCfgEntry.setStatus("current")
_CbQosTableMapCfgIndex_Type = Unsigned32
_CbQosTableMapCfgIndex_Object = MibTableColumn
cbQosTableMapCfgIndex = _CbQosTableMapCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1, 1, 1),
    _CbQosTableMapCfgIndex_Type()
)
cbQosTableMapCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosTableMapCfgIndex.setStatus("current")
_CbQosTableMapCfgName_Type = DisplayString
_CbQosTableMapCfgName_Object = MibTableColumn
cbQosTableMapCfgName = _CbQosTableMapCfgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1, 1, 2),
    _CbQosTableMapCfgName_Type()
)
cbQosTableMapCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTableMapCfgName.setStatus("current")


class _CbQosTableMapCfgBehavior_Type(Integer32):
    """Custom type cbQosTableMapCfgBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("ignore", 3),
          ("value", 1))
    )


_CbQosTableMapCfgBehavior_Type.__name__ = "Integer32"
_CbQosTableMapCfgBehavior_Object = MibTableColumn
cbQosTableMapCfgBehavior = _CbQosTableMapCfgBehavior_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1, 1, 3),
    _CbQosTableMapCfgBehavior_Type()
)
cbQosTableMapCfgBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTableMapCfgBehavior.setStatus("current")


class _CbQosTableMapCfgDftValue_Type(Unsigned32):
    """Custom type cbQosTableMapCfgDftValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CbQosTableMapCfgDftValue_Type.__name__ = "Unsigned32"
_CbQosTableMapCfgDftValue_Object = MibTableColumn
cbQosTableMapCfgDftValue = _CbQosTableMapCfgDftValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 26, 1, 1, 4),
    _CbQosTableMapCfgDftValue_Type()
)
cbQosTableMapCfgDftValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTableMapCfgDftValue.setStatus("current")
_CbQosTableMapValueCfg_ObjectIdentity = ObjectIdentity
cbQosTableMapValueCfg = _CbQosTableMapValueCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 27)
)
_CbQosTableMapValueCfgTable_Object = MibTable
cbQosTableMapValueCfgTable = _CbQosTableMapValueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 27, 1)
)
if mibBuilder.loadTexts:
    cbQosTableMapValueCfgTable.setStatus("current")
_CbQosTableMapValueCfgEntry_Object = MibTableRow
cbQosTableMapValueCfgEntry = _CbQosTableMapValueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 27, 1, 1)
)
cbQosTableMapValueCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapCfgIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapValueCfgFrom"),
)
if mibBuilder.loadTexts:
    cbQosTableMapValueCfgEntry.setStatus("current")
_CbQosTableMapValueCfgFrom_Type = Unsigned32
_CbQosTableMapValueCfgFrom_Object = MibTableColumn
cbQosTableMapValueCfgFrom = _CbQosTableMapValueCfgFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 27, 1, 1, 1),
    _CbQosTableMapValueCfgFrom_Type()
)
cbQosTableMapValueCfgFrom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosTableMapValueCfgFrom.setStatus("current")
_CbQosTableMapValueCfgTo_Type = Unsigned32
_CbQosTableMapValueCfgTo_Object = MibTableColumn
cbQosTableMapValueCfgTo = _CbQosTableMapValueCfgTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 27, 1, 1, 2),
    _CbQosTableMapValueCfgTo_Type()
)
cbQosTableMapValueCfgTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTableMapValueCfgTo.setStatus("current")
_CbQosTableMapSetCfg_ObjectIdentity = ObjectIdentity
cbQosTableMapSetCfg = _CbQosTableMapSetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28)
)
_CbQosTableMapSetCfgTable_Object = MibTable
cbQosTableMapSetCfgTable = _CbQosTableMapSetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1)
)
if mibBuilder.loadTexts:
    cbQosTableMapSetCfgTable.setStatus("current")
_CbQosTableMapSetCfgEntry_Object = MibTableRow
cbQosTableMapSetCfgEntry = _CbQosTableMapSetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1)
)
cbQosTableMapSetCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosTableMapSetCfgEntry.setStatus("current")
_CbQosTMSetIpDscpFromType_Type = CbQosTMSetType
_CbQosTMSetIpDscpFromType_Object = MibTableColumn
cbQosTMSetIpDscpFromType = _CbQosTMSetIpDscpFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 1),
    _CbQosTMSetIpDscpFromType_Type()
)
cbQosTMSetIpDscpFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetIpDscpFromType.setStatus("current")
_CbQosTMSetIpDscpMapName_Type = DisplayString
_CbQosTMSetIpDscpMapName_Object = MibTableColumn
cbQosTMSetIpDscpMapName = _CbQosTMSetIpDscpMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 2),
    _CbQosTMSetIpDscpMapName_Type()
)
cbQosTMSetIpDscpMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetIpDscpMapName.setStatus("current")
_CbQosTMSetIpPrecedenceFromType_Type = CbQosTMSetType
_CbQosTMSetIpPrecedenceFromType_Object = MibTableColumn
cbQosTMSetIpPrecedenceFromType = _CbQosTMSetIpPrecedenceFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 3),
    _CbQosTMSetIpPrecedenceFromType_Type()
)
cbQosTMSetIpPrecedenceFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetIpPrecedenceFromType.setStatus("current")
_CbQosTMSetIpPrecedenceMapName_Type = DisplayString
_CbQosTMSetIpPrecedenceMapName_Object = MibTableColumn
cbQosTMSetIpPrecedenceMapName = _CbQosTMSetIpPrecedenceMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 4),
    _CbQosTMSetIpPrecedenceMapName_Type()
)
cbQosTMSetIpPrecedenceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetIpPrecedenceMapName.setStatus("current")
_CbQosTMSetQosGroupFromType_Type = CbQosTMSetType
_CbQosTMSetQosGroupFromType_Object = MibTableColumn
cbQosTMSetQosGroupFromType = _CbQosTMSetQosGroupFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 5),
    _CbQosTMSetQosGroupFromType_Type()
)
cbQosTMSetQosGroupFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetQosGroupFromType.setStatus("current")
_CbQosTMSetQosGroupMapName_Type = DisplayString
_CbQosTMSetQosGroupMapName_Object = MibTableColumn
cbQosTMSetQosGroupMapName = _CbQosTMSetQosGroupMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 6),
    _CbQosTMSetQosGroupMapName_Type()
)
cbQosTMSetQosGroupMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetQosGroupMapName.setStatus("current")
_CbQosTMSetL2CosFromType_Type = CbQosTMSetType
_CbQosTMSetL2CosFromType_Object = MibTableColumn
cbQosTMSetL2CosFromType = _CbQosTMSetL2CosFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 7),
    _CbQosTMSetL2CosFromType_Type()
)
cbQosTMSetL2CosFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetL2CosFromType.setStatus("current")
_CbQosTMSetL2CosMapName_Type = DisplayString
_CbQosTMSetL2CosMapName_Object = MibTableColumn
cbQosTMSetL2CosMapName = _CbQosTMSetL2CosMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 8),
    _CbQosTMSetL2CosMapName_Type()
)
cbQosTMSetL2CosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetL2CosMapName.setStatus("current")
_CbQosTMSetMplsExpImpFromType_Type = CbQosTMSetType
_CbQosTMSetMplsExpImpFromType_Object = MibTableColumn
cbQosTMSetMplsExpImpFromType = _CbQosTMSetMplsExpImpFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 9),
    _CbQosTMSetMplsExpImpFromType_Type()
)
cbQosTMSetMplsExpImpFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetMplsExpImpFromType.setStatus("current")
_CbQosTMSetMplsExpImpMapName_Type = DisplayString
_CbQosTMSetMplsExpImpMapName_Object = MibTableColumn
cbQosTMSetMplsExpImpMapName = _CbQosTMSetMplsExpImpMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 10),
    _CbQosTMSetMplsExpImpMapName_Type()
)
cbQosTMSetMplsExpImpMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetMplsExpImpMapName.setStatus("current")
_CbQosTMSetMplsExpTopFromType_Type = CbQosTMSetType
_CbQosTMSetMplsExpTopFromType_Object = MibTableColumn
cbQosTMSetMplsExpTopFromType = _CbQosTMSetMplsExpTopFromType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 11),
    _CbQosTMSetMplsExpTopFromType_Type()
)
cbQosTMSetMplsExpTopFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetMplsExpTopFromType.setStatus("current")
_CbQosTMSetMplsExpTopMapName_Type = DisplayString
_CbQosTMSetMplsExpTopMapName_Object = MibTableColumn
cbQosTMSetMplsExpTopMapName = _CbQosTMSetMplsExpTopMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 28, 1, 1, 12),
    _CbQosTMSetMplsExpTopMapName_Type()
)
cbQosTMSetMplsExpTopMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosTMSetMplsExpTopMapName.setStatus("current")
_CbQosEBCfg_ObjectIdentity = ObjectIdentity
cbQosEBCfg = _CbQosEBCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29)
)
_CbQosEBCfgTable_Object = MibTable
cbQosEBCfgTable = _CbQosEBCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1)
)
if mibBuilder.loadTexts:
    cbQosEBCfgTable.setStatus("current")
_CbQosEBCfgEntry_Object = MibTableRow
cbQosEBCfgEntry = _CbQosEBCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1, 1)
)
cbQosEBCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosEBCfgEntry.setStatus("current")
_CbQosEBCfgMechanism_Type = CbQosEBType
_CbQosEBCfgMechanism_Object = MibTableColumn
cbQosEBCfgMechanism = _CbQosEBCfgMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1, 1, 1),
    _CbQosEBCfgMechanism_Type()
)
cbQosEBCfgMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBCfgMechanism.setStatus("current")


class _CbQosEBCfgDropTarget_Type(Unsigned32):
    """Custom type cbQosEBCfgDropTarget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000000),
    )


_CbQosEBCfgDropTarget_Type.__name__ = "Unsigned32"
_CbQosEBCfgDropTarget_Object = MibTableColumn
cbQosEBCfgDropTarget = _CbQosEBCfgDropTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1, 1, 2),
    _CbQosEBCfgDropTarget_Type()
)
cbQosEBCfgDropTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBCfgDropTarget.setStatus("current")
if mibBuilder.loadTexts:
    cbQosEBCfgDropTarget.setUnits("packets")


class _CbQosEBCfgDelayTarget_Type(Unsigned32):
    """Custom type cbQosEBCfgDelayTarget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000000),
    )


_CbQosEBCfgDelayTarget_Type.__name__ = "Unsigned32"
_CbQosEBCfgDelayTarget_Object = MibTableColumn
cbQosEBCfgDelayTarget = _CbQosEBCfgDelayTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1, 1, 3),
    _CbQosEBCfgDelayTarget_Type()
)
cbQosEBCfgDelayTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBCfgDelayTarget.setStatus("current")
if mibBuilder.loadTexts:
    cbQosEBCfgDelayTarget.setUnits("packets")


class _CbQosEBCfgDelayThreshold_Type(Unsigned32):
    """Custom type cbQosEBCfgDelayThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000),
    )


_CbQosEBCfgDelayThreshold_Type.__name__ = "Unsigned32"
_CbQosEBCfgDelayThreshold_Object = MibTableColumn
cbQosEBCfgDelayThreshold = _CbQosEBCfgDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 29, 1, 1, 4),
    _CbQosEBCfgDelayThreshold_Type()
)
cbQosEBCfgDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBCfgDelayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cbQosEBCfgDelayThreshold.setUnits("millisecond")
_CbQosEBStats_ObjectIdentity = ObjectIdentity
cbQosEBStats = _CbQosEBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30)
)
_CbQosEBStatsTable_Object = MibTable
cbQosEBStatsTable = _CbQosEBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cbQosEBStatsTable.setStatus("current")
_CbQosEBStatsEntry_Object = MibTableRow
cbQosEBStatsEntry = _CbQosEBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30, 1, 1)
)
cbQosEBStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    cbQosEBStatsEntry.setStatus("current")
_CbQosEBStatsCorvilEBValue_Type = Gauge32
_CbQosEBStatsCorvilEBValue_Object = MibTableColumn
cbQosEBStatsCorvilEBValue = _CbQosEBStatsCorvilEBValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30, 1, 1, 1),
    _CbQosEBStatsCorvilEBValue_Type()
)
cbQosEBStatsCorvilEBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBStatsCorvilEBValue.setStatus("current")
if mibBuilder.loadTexts:
    cbQosEBStatsCorvilEBValue.setUnits("kbps")
_CbQosEBStatsCorvilEBStatus_Type = TruthValue
_CbQosEBStatsCorvilEBStatus_Object = MibTableColumn
cbQosEBStatsCorvilEBStatus = _CbQosEBStatsCorvilEBStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30, 1, 1, 2),
    _CbQosEBStatsCorvilEBStatus_Type()
)
cbQosEBStatsCorvilEBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBStatsCorvilEBStatus.setStatus("current")
_CbQosEBStatsCorvilCTD_Type = CbQosEBCtd
_CbQosEBStatsCorvilCTD_Object = MibTableColumn
cbQosEBStatsCorvilCTD = _CbQosEBStatsCorvilCTD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 30, 1, 1, 3),
    _CbQosEBStatsCorvilCTD_Type()
)
cbQosEBStatsCorvilCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosEBStatsCorvilCTD.setStatus("current")
_CbQosMeasureIPSLACfg_ObjectIdentity = ObjectIdentity
cbQosMeasureIPSLACfg = _CbQosMeasureIPSLACfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 31)
)
_CbQosMeasureIPSLACfgTable_Object = MibTable
cbQosMeasureIPSLACfgTable = _CbQosMeasureIPSLACfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 31, 1)
)
if mibBuilder.loadTexts:
    cbQosMeasureIPSLACfgTable.setStatus("current")
_CbQosMeasureIPSLACfgEntry_Object = MibTableRow
cbQosMeasureIPSLACfgEntry = _CbQosMeasureIPSLACfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 31, 1, 1)
)
cbQosMeasureIPSLACfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosMeasureIPSLACfgGroupIndex"),
)
if mibBuilder.loadTexts:
    cbQosMeasureIPSLACfgEntry.setStatus("current")
_CbQosMeasureIPSLACfgGroupIndex_Type = Unsigned32
_CbQosMeasureIPSLACfgGroupIndex_Object = MibTableColumn
cbQosMeasureIPSLACfgGroupIndex = _CbQosMeasureIPSLACfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 31, 1, 1, 1),
    _CbQosMeasureIPSLACfgGroupIndex_Type()
)
cbQosMeasureIPSLACfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMeasureIPSLACfgGroupIndex.setStatus("current")


class _CbQosMeasureIPSLACfgGroupName_Type(DisplayString):
    """Custom type cbQosMeasureIPSLACfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CbQosMeasureIPSLACfgGroupName_Type.__name__ = "DisplayString"
_CbQosMeasureIPSLACfgGroupName_Object = MibTableColumn
cbQosMeasureIPSLACfgGroupName = _CbQosMeasureIPSLACfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 31, 1, 1, 2),
    _CbQosMeasureIPSLACfgGroupName_Type()
)
cbQosMeasureIPSLACfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosMeasureIPSLACfgGroupName.setStatus("current")
_CbQosQueueingClassCfg_ObjectIdentity = ObjectIdentity
cbQosQueueingClassCfg = _CbQosQueueingClassCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32)
)
_CbQosQueueingClassCfgTable_Object = MibTable
cbQosQueueingClassCfgTable = _CbQosQueueingClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1)
)
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgTable.setStatus("current")
_CbQosQueueingClassCfgEntry_Object = MibTableRow
cbQosQueueingClassCfgEntry = _CbQosQueueingClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1)
)
cbQosQueueingClassCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingClassConfigIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosQlimitWeightValue"),
)
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgEntry.setStatus("current")


class _CbQosQueueingClassConfigIndex_Type(Integer32):
    """Custom type cbQosQueueingClassConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbQosQueueingClassConfigIndex_Type.__name__ = "Integer32"
_CbQosQueueingClassConfigIndex_Object = MibTableColumn
cbQosQueueingClassConfigIndex = _CbQosQueueingClassConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1, 1),
    _CbQosQueueingClassConfigIndex_Type()
)
cbQosQueueingClassConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosQueueingClassConfigIndex.setStatus("current")


class _CbQosQlimitWeightValue_Type(Integer32):
    """Custom type cbQosQlimitWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CbQosQlimitWeightValue_Type.__name__ = "Integer32"
_CbQosQlimitWeightValue_Object = MibTableColumn
cbQosQlimitWeightValue = _CbQosQlimitWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1, 2),
    _CbQosQlimitWeightValue_Type()
)
cbQosQlimitWeightValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbQosQlimitWeightValue.setStatus("current")
_CbQosQueueingClassCfgThreshold_Type = CbQosQueueDepth
_CbQosQueueingClassCfgThreshold_Object = MibTableColumn
cbQosQueueingClassCfgThreshold = _CbQosQueueingClassCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1, 3),
    _CbQosQueueingClassCfgThreshold_Type()
)
cbQosQueueingClassCfgThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgThreshold.setStatus("current")
_CbQosQueueingClassCfgThresholdUnit_Type = CbQosQueueUnitType
_CbQosQueueingClassCfgThresholdUnit_Object = MibTableColumn
cbQosQueueingClassCfgThresholdUnit = _CbQosQueueingClassCfgThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1, 4),
    _CbQosQueueingClassCfgThresholdUnit_Type()
)
cbQosQueueingClassCfgThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgThresholdUnit.setStatus("current")
_CbQosQueueingClassCfgQLimitWeight_Type = QueueMechanism
_CbQosQueueingClassCfgQLimitWeight_Object = MibTableColumn
cbQosQueueingClassCfgQLimitWeight = _CbQosQueueingClassCfgQLimitWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 32, 1, 1, 5),
    _CbQosQueueingClassCfgQLimitWeight_Type()
)
cbQosQueueingClassCfgQLimitWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgQLimitWeight.setStatus("current")
_CbQosC3plAccountCfg_ObjectIdentity = ObjectIdentity
cbQosC3plAccountCfg = _CbQosC3plAccountCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 33)
)
_CbQosC3plAccountCfgTable_Object = MibTable
cbQosC3plAccountCfgTable = _CbQosC3plAccountCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 33, 1)
)
if mibBuilder.loadTexts:
    cbQosC3plAccountCfgTable.setStatus("current")
_CbQosC3plAccountCfgEntry_Object = MibTableRow
cbQosC3plAccountCfgEntry = _CbQosC3plAccountCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 33, 1, 1)
)
cbQosC3plAccountCfgEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    cbQosC3plAccountCfgEntry.setStatus("current")
_CbQosC3plAccountFeatureType_Type = SetC3plAccountFeatureType
_CbQosC3plAccountFeatureType_Object = MibTableColumn
cbQosC3plAccountFeatureType = _CbQosC3plAccountFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 33, 1, 1, 1),
    _CbQosC3plAccountFeatureType_Type()
)
cbQosC3plAccountFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountFeatureType.setStatus("current")
_CbQosC3plAccountStats_ObjectIdentity = ObjectIdentity
cbQosC3plAccountStats = _CbQosC3plAccountStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34)
)
_CbQosC3plAccountStatsTable_Object = MibTable
cbQosC3plAccountStatsTable = _CbQosC3plAccountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1)
)
if mibBuilder.loadTexts:
    cbQosC3plAccountStatsTable.setStatus("current")
_CbQosC3plAccountStatsEntry_Object = MibTableRow
cbQosC3plAccountStatsEntry = _CbQosC3plAccountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1)
)
cbQosC3plAccountStatsEntry.setIndexNames(
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsIndex"),
    (0, "CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountFeatureType"),
)
if mibBuilder.loadTexts:
    cbQosC3plAccountStatsEntry.setStatus("current")
_CbQosC3plAccountDropPktOverflow_Type = Counter32
_CbQosC3plAccountDropPktOverflow_Object = MibTableColumn
cbQosC3plAccountDropPktOverflow = _CbQosC3plAccountDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 1),
    _CbQosC3plAccountDropPktOverflow_Type()
)
cbQosC3plAccountDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPktOverflow.setUnits("Packets")
_CbQosC3plAccountDropPkt_Type = Counter32
_CbQosC3plAccountDropPkt_Object = MibTableColumn
cbQosC3plAccountDropPkt = _CbQosC3plAccountDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 2),
    _CbQosC3plAccountDropPkt_Type()
)
cbQosC3plAccountDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPkt.setUnits("Packets")
_CbQosC3plAccountDropPkt64_Type = Counter64
_CbQosC3plAccountDropPkt64_Object = MibTableColumn
cbQosC3plAccountDropPkt64 = _CbQosC3plAccountDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 3),
    _CbQosC3plAccountDropPkt64_Type()
)
cbQosC3plAccountDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropPkt64.setUnits("Packets")
_CbQosC3plAccountDropByteOverflow_Type = Counter32
_CbQosC3plAccountDropByteOverflow_Object = MibTableColumn
cbQosC3plAccountDropByteOverflow = _CbQosC3plAccountDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 4),
    _CbQosC3plAccountDropByteOverflow_Type()
)
cbQosC3plAccountDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByteOverflow.setUnits("Octets")
_CbQosC3plAccountDropByte_Type = Counter32
_CbQosC3plAccountDropByte_Object = MibTableColumn
cbQosC3plAccountDropByte = _CbQosC3plAccountDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 5),
    _CbQosC3plAccountDropByte_Type()
)
cbQosC3plAccountDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByte.setUnits("Octets")
_CbQosC3plAccountDropByte64_Type = Counter64
_CbQosC3plAccountDropByte64_Object = MibTableColumn
cbQosC3plAccountDropByte64 = _CbQosC3plAccountDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 6),
    _CbQosC3plAccountDropByte64_Type()
)
cbQosC3plAccountDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountDropByte64.setUnits("Octets")
_CbQosC3plAccountTailDropPktOverflow_Type = Counter32
_CbQosC3plAccountTailDropPktOverflow_Object = MibTableColumn
cbQosC3plAccountTailDropPktOverflow = _CbQosC3plAccountTailDropPktOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 7),
    _CbQosC3plAccountTailDropPktOverflow_Type()
)
cbQosC3plAccountTailDropPktOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPktOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPktOverflow.setUnits("Packets")
_CbQosC3plAccountTailDropPkt_Type = Counter32
_CbQosC3plAccountTailDropPkt_Object = MibTableColumn
cbQosC3plAccountTailDropPkt = _CbQosC3plAccountTailDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 8),
    _CbQosC3plAccountTailDropPkt_Type()
)
cbQosC3plAccountTailDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPkt.setUnits("Packets")
_CbQosC3plAccountTailDropPkt64_Type = Counter64
_CbQosC3plAccountTailDropPkt64_Object = MibTableColumn
cbQosC3plAccountTailDropPkt64 = _CbQosC3plAccountTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 9),
    _CbQosC3plAccountTailDropPkt64_Type()
)
cbQosC3plAccountTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropPkt64.setUnits("Packets")
_CbQosC3plAccountTailDropByteOverflow_Type = Counter32
_CbQosC3plAccountTailDropByteOverflow_Object = MibTableColumn
cbQosC3plAccountTailDropByteOverflow = _CbQosC3plAccountTailDropByteOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 10),
    _CbQosC3plAccountTailDropByteOverflow_Type()
)
cbQosC3plAccountTailDropByteOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByteOverflow.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByteOverflow.setUnits("Octets")
_CbQosC3plAccountTailDropByte_Type = Counter32
_CbQosC3plAccountTailDropByte_Object = MibTableColumn
cbQosC3plAccountTailDropByte = _CbQosC3plAccountTailDropByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 11),
    _CbQosC3plAccountTailDropByte_Type()
)
cbQosC3plAccountTailDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByte.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByte.setUnits("Octets")
_CbQosC3plAccountTailDropByte64_Type = Counter64
_CbQosC3plAccountTailDropByte64_Object = MibTableColumn
cbQosC3plAccountTailDropByte64 = _CbQosC3plAccountTailDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 1, 34, 1, 1, 12),
    _CbQosC3plAccountTailDropByte64_Type()
)
cbQosC3plAccountTailDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    cbQosC3plAccountTailDropByte64.setUnits("Octets")
_CiscocbQosMIBConformance_ObjectIdentity = ObjectIdentity
ciscocbQosMIBConformance = _CiscocbQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2)
)
_CiscocbQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscocbQosMIBCompliances = _CiscocbQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1)
)
_CiscocbQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscocbQosMIBGroups = _CiscocbQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2)
)

# Managed Objects groups

cbQosServicePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 1)
)
cbQosServicePolicyGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosIfType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDirection"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIfIndex"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosFrDLCI"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVPI"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVCI"))
)
if mibBuilder.loadTexts:
    cbQosServicePolicyGroup.setStatus("deprecated")

cbQosInterfacePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 2)
)
cbQosInterfacePolicyGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIFPolicyIndex")
)
if mibBuilder.loadTexts:
    cbQosInterfacePolicyGroup.setStatus("current")

cbQosFrameRelayVCPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 3)
)
cbQosFrameRelayVCPolicyGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosFRPolicyIndex")
)
if mibBuilder.loadTexts:
    cbQosFrameRelayVCPolicyGroup.setStatus("current")

cbQosATMPVCPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 4)
)
cbQosATMPVCPolicyGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosATMPolicyIndex")
)
if mibBuilder.loadTexts:
    cbQosATMPVCPolicyGroup.setStatus("current")

cbQosObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 5)
)
cbQosObjectsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosConfigIndex"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosObjectsType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosParentObjectsIndex"))
)
if mibBuilder.loadTexts:
    cbQosObjectsGroup.setStatus("current")

cbQosPolicyMapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 6)
)
cbQosPolicyMapCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyMapDesc"))
)
if mibBuilder.loadTexts:
    cbQosPolicyMapCfgGroup.setStatus("current")

cbQosClassMapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 7)
)
cbQosClassMapCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDesc"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMInfo"))
)
if mibBuilder.loadTexts:
    cbQosClassMapCfgGroup.setStatus("current")

cbQosMatchStmtCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 8)
)
cbQosMatchStmtCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchStmtName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchStmtInfo"))
)
if mibBuilder.loadTexts:
    cbQosMatchStmtCfgGroup.setStatus("current")

cbQosQueueingCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 9)
)
cbQosQueueingCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidth"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidthUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgFlowEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPriorityEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgAggregateQSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgIndividualQSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPrioBurstSize"))
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgGroup.setStatus("deprecated")

cbQosREDCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 10)
)
cbQosREDCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgExponWeight"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgMeanQsize"))
)
if mibBuilder.loadTexts:
    cbQosREDCfgGroup.setStatus("deprecated")

cbQosREDClassCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 11)
)
cbQosREDClassCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgMinThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgMaxThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgPktDropProb"))
)
if mibBuilder.loadTexts:
    cbQosREDClassCfgGroup.setStatus("deprecated")

cbQosPoliceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 12)
)
cbQosPoliceCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgConformAction"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgConformSetValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExceedAction"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExceedSetValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPir"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgGroup.setStatus("deprecated")

cbQosTSCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 13)
)
cbQosTSCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgExtBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgAdaptiveEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgAdaptiveRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgLimitType"))
)
if mibBuilder.loadTexts:
    cbQosTSCfgGroup.setStatus("current")

cbQosSetCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 14)
)
cbQosSetCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgFeature"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpDSCPValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpPrecedenceValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgQosGroupValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgL2CosValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgMplsExpValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgDiscardClassValue"))
)
if mibBuilder.loadTexts:
    cbQosSetCfgGroup.setStatus("deprecated")

cbQosClassMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 15)
)
cbQosClassMapStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPostPolicyByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPostPolicyByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPostPolicyByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPostPolicyBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropBitRate"))
)
if mibBuilder.loadTexts:
    cbQosClassMapStatsGroup.setStatus("current")

cbQosNoBufferDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 16)
)
cbQosNoBufferDropGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMNoBufDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMNoBufDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMNoBufDropPkt64"))
)
if mibBuilder.loadTexts:
    cbQosNoBufferDropGroup.setStatus("current")

cbQosQueueingDynamicQNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 17)
)
cbQosQueueingDynamicQNumberGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgDynamicQNumber")
)
if mibBuilder.loadTexts:
    cbQosQueueingDynamicQNumberGroup.setStatus("current")

cbQosTrafficShapingDelayCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 18)
)
cbQosTrafficShapingDelayCountersGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDelayedPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsActive"))
)
if mibBuilder.loadTexts:
    cbQosTrafficShapingDelayCountersGroup.setStatus("current")

cbQosMatchStmtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 19)
)
cbQosMatchStmtStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMatchPrePolicyBitRate"))
)
if mibBuilder.loadTexts:
    cbQosMatchStmtStatsGroup.setStatus("current")

cbQosPoliceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 20)
)
cbQosPoliceStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededBitRate"))
)
if mibBuilder.loadTexts:
    cbQosPoliceStatsGroup.setStatus("current")

cbQosQueueingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 21)
)
cbQosQueueingStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCurrentQDepth"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingMaxQDepth"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingDiscardPkt64"))
)
if mibBuilder.loadTexts:
    cbQosQueueingStatsGroup.setStatus("current")

cbQosTSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 22)
)
cbQosTSStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSStatsCurrentQSize"))
)
if mibBuilder.loadTexts:
    cbQosTSStatsGroup.setStatus("current")

cbQosREDClassStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 23)
)
cbQosREDClassStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDRandomDropByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTailDropByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDMeanQSizeUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDMeanQSize"))
)
if mibBuilder.loadTexts:
    cbQosREDClassStatsGroup.setStatus("current")

cbQosREDClassXmitCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 24)
)
cbQosREDClassXmitCountersGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDTransmitByte64"))
)
if mibBuilder.loadTexts:
    cbQosREDClassXmitCountersGroup.setStatus("current")

cbQosAFPoliceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 25)
)
cbQosAFPoliceStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedBitRate"))
)
if mibBuilder.loadTexts:
    cbQosAFPoliceStatsGroup.setStatus("current")

cbQosAFPoliceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 26)
)
cbQosAFPoliceCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgViolateAction"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgViolateSetValue"))
)
if mibBuilder.loadTexts:
    cbQosAFPoliceCfgGroup.setStatus("deprecated")

cbQosREDDscpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 27)
)
cbQosREDDscpCfgGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgDscpPrec")
)
if mibBuilder.loadTexts:
    cbQosREDDscpCfgGroup.setStatus("current")

cbQosNewSetCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 28)
)
cbQosNewSetCfgGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgL2CosValue")
)
if mibBuilder.loadTexts:
    cbQosNewSetCfgGroup.setStatus("deprecated")

cbQosQueueingCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 29)
)
cbQosQueueingCfgGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidth"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidthUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgFlowEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPriorityEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgIndividualQSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPrioBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgQLimitUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgAggregateQLimit"))
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgGroupRev1.setStatus("deprecated")

cbQosREDCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 30)
)
cbQosREDCfgGroupRev1.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgExponWeight")
)
if mibBuilder.loadTexts:
    cbQosREDCfgGroupRev1.setStatus("current")

cbQosREDClassCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 31)
)
cbQosREDClassCfgGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgPktDropProb"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgThresholdUnit"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMinThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMaxThreshold"))
)
if mibBuilder.loadTexts:
    cbQosREDClassCfgGroupRev1.setStatus("deprecated")

cbQosPoliceCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 32)
)
cbQosPoliceCfgGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPir"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgGroupRev1.setStatus("deprecated")

cbQosPoliceActionCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 33)
)
cbQosPoliceActionCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgConform"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgConformSetValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgExceed"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgExceedSetValue"))
)
if mibBuilder.loadTexts:
    cbQosPoliceActionCfgGroup.setStatus("current")

cbQosAFPoliceViolateCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 34)
)
cbQosAFPoliceViolateCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgViolate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceActionCfgViolateSetValue"))
)
if mibBuilder.loadTexts:
    cbQosAFPoliceViolateCfgGroup.setStatus("current")

cbQosREDECNCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 35)
)
cbQosREDECNCfgGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgECNEnabled")
)
if mibBuilder.loadTexts:
    cbQosREDECNCfgGroup.setStatus("current")

cbQosREDClassECNMarkCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 36)
)
cbQosREDClassECNMarkCountersGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDECNMarkByte64"))
)
if mibBuilder.loadTexts:
    cbQosREDClassECNMarkCountersGroup.setStatus("current")

cbQosPoliceCfgExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 37)
)
cbQosPoliceCfgExtGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRate64")
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgExtGroup.setStatus("current")

cbQosSetCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 38)
)
cbQosSetCfgGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgFeature"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpDSCPValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpPrecedenceValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgQosGroupValue"))
)
if mibBuilder.loadTexts:
    cbQosSetCfgGroupRev1.setStatus("current")

cbQosSetCfgMplsImpositionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 39)
)
cbQosSetCfgMplsImpositionGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgMplsExpValue")
)
if mibBuilder.loadTexts:
    cbQosSetCfgMplsImpositionGroup.setStatus("current")

cbQosSetCfgDiscardClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 40)
)
cbQosSetCfgDiscardClassGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgDiscardClassValue")
)
if mibBuilder.loadTexts:
    cbQosSetCfgDiscardClassGroup.setStatus("current")

cbQosSetCfgMPLSTopMostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 41)
)
cbQosSetCfgMPLSTopMostGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgMplsExpTopMostValue")
)
if mibBuilder.loadTexts:
    cbQosSetCfgMPLSTopMostGroup.setStatus("current")

cbQosPoliceCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 42)
)
cbQosPoliceCfgGroupRev2.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstSize"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgGroupRev2.setStatus("current")

cbQosPoliceCfgPirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 43)
)
cbQosPoliceCfgPirGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPir")
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgPirGroup.setStatus("current")

cbQosPoliceCfgPercentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 44)
)
cbQosPoliceCfgPercentGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRateType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPercentRateValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPercentPirValue"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgPercentGroup.setStatus("current")

cbQosTSCfgPercentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 45)
)
cbQosTSCfgPercentGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgRateType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgPercentRateValue"))
)
if mibBuilder.loadTexts:
    cbQosTSCfgPercentGroup.setStatus("current")

cbQosIPHCCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 46)
)
cbQosIPHCCfgGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCCfgOption")
)
if mibBuilder.loadTexts:
    cbQosIPHCCfgGroup.setStatus("current")

cbQosIPHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 47)
)
cbQosIPHCStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpCmprsOutPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpCmprsOutPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpCmprsOutPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSavedByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSavedByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSavedByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpSentByteRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpCmprsOutPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpCmprsOutPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpCmprsOutPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSavedByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSavedByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSavedByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpSentByteRate"))
)
if mibBuilder.loadTexts:
    cbQosIPHCStatsGroup.setStatus("current")

cbQosServicePolicyGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 48)
)
cbQosServicePolicyGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosIfType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDirection"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIfIndex"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosFrDLCI"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVPI"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosAtmVCI"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEntityIndex"))
)
if mibBuilder.loadTexts:
    cbQosServicePolicyGroupRev1.setStatus("current")

cbQosQueueingCfgQLimitTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 49)
)
cbQosQueueingCfgQLimitTimeGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgAggrQLimitTime")
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgQLimitTimeGroup.setStatus("current")

cbQosREDCfgThresholdTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 50)
)
cbQosREDCfgThresholdTimeGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMinThresholdTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMaxThresholdTime"))
)
if mibBuilder.loadTexts:
    cbQosREDCfgThresholdTimeGroup.setStatus("current")

cbQosPoliceCfgCellGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 51)
)
cbQosPoliceCfgCellGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgCellRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgCellPir"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstCell"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstCell"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgCellGroup.setStatus("current")

cbQosPoliceCfgTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 52)
)
cbQosPoliceCfgTimeGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstTime"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgTimeGroup.setStatus("current")

cbQosPoliceCfgCdvtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 53)
)
cbQosPoliceCfgCdvtGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgCdvt")
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgCdvtGroup.setStatus("current")

cbQosPoliceCfgColorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 54)
)
cbQosPoliceCfgColorGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgConformColor"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExceedColor"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgColorGroup.setStatus("current")

cbQosTSCfgTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 55)
)
cbQosTSCfgTimeGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgBurstTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgExtBurstTime"))
)
if mibBuilder.loadTexts:
    cbQosTSCfgTimeGroup.setStatus("current")

cbQosSetCfgSrpPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 56)
)
cbQosSetCfgSrpPriorityGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgSrpPriority")
)
if mibBuilder.loadTexts:
    cbQosSetCfgSrpPriorityGroup.setStatus("current")

cbQosSetCfgFrFecnBecnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 57)
)
cbQosSetCfgFrFecnBecnGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgFrFecnBecn")
)
if mibBuilder.loadTexts:
    cbQosSetCfgFrFecnBecnGroup.setStatus("current")

cbQosSetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 58)
)
cbQosSetStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetDscpPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetPrecedencePkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetQosGroupPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetFrDePkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetAtmClpPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetL2CosPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetMplsExpImpositionPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetDiscardClassPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetMplsExpTopMostPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetSrpPriorityPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetFrFecnBecnPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetDscpTunnelPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetPrecedenceTunnelPkt64"))
)
if mibBuilder.loadTexts:
    cbQosSetStatsGroup.setStatus("current")

cbQosPoliceColorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 59)
)
cbQosPoliceColorStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorCfmPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorCfmByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorExdPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorExdByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorVltPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorVltByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorExdPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorExdByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorVltPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorVltByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceVltColorVltPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceVltColorVltByte64"))
)
if mibBuilder.loadTexts:
    cbQosPoliceColorStatsGroup.setStatus("current")

cbQosTableMapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 60)
)
cbQosTableMapCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapCfgName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapCfgBehavior"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapCfgDftValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTableMapValueCfgTo"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetIpDscpFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetIpDscpMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetIpPrecedenceFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetIpPrecedenceMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetQosGroupFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetQosGroupMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetL2CosFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetL2CosMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetMplsExpImpFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetMplsExpImpMapName"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetMplsExpTopFromType"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTMSetMplsExpTopMapName"))
)
if mibBuilder.loadTexts:
    cbQosTableMapCfgGroup.setStatus("current")

cbQosEBCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 61)
)
cbQosEBCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBCfgMechanism"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBCfgDropTarget"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBCfgDelayTarget"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBCfgDelayThreshold"))
)
if mibBuilder.loadTexts:
    cbQosEBCfgGroup.setStatus("current")

cbQosEBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 62)
)
cbQosEBStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBStatsCorvilEBValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBStatsCorvilEBStatus"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEBStatsCorvilCTD"))
)
if mibBuilder.loadTexts:
    cbQosEBStatsGroup.setStatus("current")

cbQosServicePolicyExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 63)
)
cbQosServicePolicyExtGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosVlanIndex")
)
if mibBuilder.loadTexts:
    cbQosServicePolicyExtGroup.setStatus("current")

cbQosMeasureIPSLACfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 64)
)
cbQosMeasureIPSLACfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosMeasureIPSLACfgGroupIndex"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosMeasureIPSLACfgGroupName"))
)
if mibBuilder.loadTexts:
    cbQosMeasureIPSLACfgGroup.setStatus("current")

cbQosTSCfgExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 65)
)
cbQosTSCfgExtGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgRate64")
)
if mibBuilder.loadTexts:
    cbQosTSCfgExtGroup.setStatus("current")

cbQosQueueingCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 66)
)
cbQosQueueingCfgGroupRev2.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidth"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidthUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgFlowEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPriorityEnabled"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgIndividualQSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPrioBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgQLimitUnits"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgAggregateQLimit"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgPriorityLevel"))
)
if mibBuilder.loadTexts:
    cbQosQueueingCfgGroupRev2.setStatus("current")

cbQosSetCfgL2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 67)
)
cbQosSetCfgL2Group.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgL2CosValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgL2CosInnerValue"))
)
if mibBuilder.loadTexts:
    cbQosSetCfgL2Group.setStatus("current")

cbQosREDClassCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 68)
)
cbQosREDClassCfgGroupRev2.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDCfgPktDropProb"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMinThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMaxThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMinThresholdTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMaxThresholdTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMaxThresholdUnit"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosREDClassCfgMinThresholdUnit"))
)
if mibBuilder.loadTexts:
    cbQosREDClassCfgGroupRev2.setStatus("current")

cbQosQueueingClassCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 69)
)
cbQosQueueingClassCfgGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingClassCfgThreshold"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingClassCfgThresholdUnit"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingClassCfgQLimitWeight"))
)
if mibBuilder.loadTexts:
    cbQosQueueingClassCfgGroup.setStatus("current")

cbQosPoliceCfgGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 70)
)
cbQosPoliceCfgGroupRev3.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstSize"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgConditional"))
)
if mibBuilder.loadTexts:
    cbQosPoliceCfgGroupRev3.setStatus("current")

cbQosC3plAccountCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 71)
)
cbQosC3plAccountCfgGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountFeatureType")
)
if mibBuilder.loadTexts:
    cbQosC3plAccountCfgGroup.setStatus("current")

cbQosC3plAccountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 72)
)
cbQosC3plAccountStatsGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountDropByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosC3plAccountTailDropByte64"))
)
if mibBuilder.loadTexts:
    cbQosC3plAccountStatsGroup.setStatus("current")

cbQosSetCfgFrDeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 73)
)
cbQosSetCfgFrDeGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgFrDe")
)
if mibBuilder.loadTexts:
    cbQosSetCfgFrDeGroup.setStatus("current")

cbQosEVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 74)
)
cbQosEVCGroup.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosEVC")
)
if mibBuilder.loadTexts:
    cbQosEVCGroup.setStatus("current")

cbQosFragmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 75)
)
cbQosFragmentGroup.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentByteOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentByte"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMFragmentByte64"))
)
if mibBuilder.loadTexts:
    cbQosFragmentGroup.setStatus("current")

cbQosSetCfgExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 76)
)
cbQosSetCfgExt.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpPrecedenceTunnelValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgIpDSCPTunnelValue"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgDei"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosSetCfgDeiImposition"))
)
if mibBuilder.loadTexts:
    cbQosSetCfgExt.setStatus("current")

cbQosPoliceColorStatsExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 77)
)
cbQosPoliceColorStatsExt.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorExdBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorCfmBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorExdBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfmColorVltBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExdColorVltBitRate"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceVltColorVltBitRate"))
)
if mibBuilder.loadTexts:
    cbQosPoliceColorStatsExt.setStatus("current")

cbQosIPHCCfgExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 78)
)
cbQosIPHCCfgExt.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCCfgEnabled")
)
if mibBuilder.loadTexts:
    cbQosIPHCCfgExt.setStatus("current")

cbQosIPHCStatsExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 79)
)
cbQosIPHCStatsExt.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpFullHdrSentPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpFullHdrSentPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCRtpFullHdrSentPkt64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpFullHdrSentPktOverflow"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpFullHdrSentPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosIPHCTcpFullHdrSentPkt64"))
)
if mibBuilder.loadTexts:
    cbQosIPHCStatsExt.setStatus("current")

cbQos421XRCfgExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 80)
)
cbQos421XRCfgExt.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosPolicyDiscontinuityTime"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgBandwidth64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCfgIndividualQSize64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgBurstSize64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgExtBurstSize64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceCfgPir64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgBurstSize64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosTSCfgExtBurstSize64"))
)
if mibBuilder.loadTexts:
    cbQos421XRCfgExt.setStatus("current")

cbQosBitRateExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 81)
)
cbQosBitRateExt.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPrePolicyBitRate64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMPostPolicyBitRate64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosCMDropBitRate64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceConformedBitRate64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceExceededBitRate64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosPoliceViolatedBitRate64"))
)
if mibBuilder.loadTexts:
    cbQosBitRateExt.setStatus("current")

cbQosQueueingStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 82)
)
cbQosQueueingStatsGroupRev1.setObjects(
      *(("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingCurrentQDepthPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingMaxQDepthPkt"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingTransmitByte64"),
        ("CISCO-CLASS-BASED-QOS-MIB", "cbQosQueueingTransmitPkt64"))
)
if mibBuilder.loadTexts:
    cbQosQueueingStatsGroupRev1.setStatus("current")

cbQosServicePolicyExtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 2, 83)
)
cbQosServicePolicyExtGroupRev2.setObjects(
    ("CISCO-CLASS-BASED-QOS-MIB", "cbQosParentPolicyIndex")
)
if mibBuilder.loadTexts:
    cbQosServicePolicyExtGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscocbQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBCompliance.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev8.setStatus(
        "current"
    )

ciscocbQosMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev9.setStatus(
        "current"
    )

ciscocbQosMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev10.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev11.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev12.setStatus(
        "deprecated"
    )

ciscocbQosMIBComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 166, 2, 1, 14)
)
if mibBuilder.loadTexts:
    ciscocbQosMIBComplianceRev13.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CLASS-BASED-QOS-MIB",
    **{"QueueMechanism": QueueMechanism,
       "QosObjectType": QosObjectType,
       "TrafficDirection": TrafficDirection,
       "QosClassInfo": QosClassInfo,
       "QosMatchInfo": QosMatchInfo,
       "InterfaceType": InterfaceType,
       "QueueingBandwidthUnits": QueueingBandwidthUnits,
       "TrafficShapingLimit": TrafficShapingLimit,
       "PoliceAction": PoliceAction,
       "SetFeatureType": SetFeatureType,
       "REDMechanism": REDMechanism,
       "CbQosQueueUnitType": CbQosQueueUnitType,
       "CbQosQueueDepth": CbQosQueueDepth,
       "CbQosRateType": CbQosRateType,
       "IPHCOption": IPHCOption,
       "CbQosTMSetType": CbQosTMSetType,
       "CbQosEBType": CbQosEBType,
       "CbQosEBCtd": CbQosEBCtd,
       "SetC3plAccountFeatureType": SetC3plAccountFeatureType,
       "ciscoCBQosMIB": ciscoCBQosMIB,
       "ciscoCBQosMIBObjects": ciscoCBQosMIBObjects,
       "cbQosServicePolicy": cbQosServicePolicy,
       "cbQosServicePolicyTable": cbQosServicePolicyTable,
       "cbQosServicePolicyEntry": cbQosServicePolicyEntry,
       "cbQosPolicyIndex": cbQosPolicyIndex,
       "cbQosIfType": cbQosIfType,
       "cbQosPolicyDirection": cbQosPolicyDirection,
       "cbQosIfIndex": cbQosIfIndex,
       "cbQosFrDLCI": cbQosFrDLCI,
       "cbQosAtmVPI": cbQosAtmVPI,
       "cbQosAtmVCI": cbQosAtmVCI,
       "cbQosEntityIndex": cbQosEntityIndex,
       "cbQosVlanIndex": cbQosVlanIndex,
       "cbQosEVC": cbQosEVC,
       "cbQosPolicyDiscontinuityTime": cbQosPolicyDiscontinuityTime,
       "cbQosParentPolicyIndex": cbQosParentPolicyIndex,
       "cbQosInterfacePolicy": cbQosInterfacePolicy,
       "cbQosInterfacePolicyTable": cbQosInterfacePolicyTable,
       "cbQosInterfacePolicyEntry": cbQosInterfacePolicyEntry,
       "cbQosIFPolicyIndex": cbQosIFPolicyIndex,
       "cbQosFrameRelayVCPolicy": cbQosFrameRelayVCPolicy,
       "cbQosFrameRelayPolicyTable": cbQosFrameRelayPolicyTable,
       "cbQosFrameRelayPolicyEntry": cbQosFrameRelayPolicyEntry,
       "cbQosFRPolicyIndex": cbQosFRPolicyIndex,
       "cbQosATMPVCPolicy": cbQosATMPVCPolicy,
       "cbQosATMPVCPolicyTable": cbQosATMPVCPolicyTable,
       "cbQosATMPVCPolicyEntry": cbQosATMPVCPolicyEntry,
       "cbQosATMPolicyIndex": cbQosATMPolicyIndex,
       "cbQosObjects": cbQosObjects,
       "cbQosObjectsTable": cbQosObjectsTable,
       "cbQosObjectsEntry": cbQosObjectsEntry,
       "cbQosObjectsIndex": cbQosObjectsIndex,
       "cbQosConfigIndex": cbQosConfigIndex,
       "cbQosObjectsType": cbQosObjectsType,
       "cbQosParentObjectsIndex": cbQosParentObjectsIndex,
       "cbQosPolicyMapCfg": cbQosPolicyMapCfg,
       "cbQosPolicyMapCfgTable": cbQosPolicyMapCfgTable,
       "cbQosPolicyMapCfgEntry": cbQosPolicyMapCfgEntry,
       "cbQosPolicyMapName": cbQosPolicyMapName,
       "cbQosPolicyMapDesc": cbQosPolicyMapDesc,
       "cbQosClassMapCfg": cbQosClassMapCfg,
       "cbQosCMCfgTable": cbQosCMCfgTable,
       "cbQosCMCfgEntry": cbQosCMCfgEntry,
       "cbQosCMName": cbQosCMName,
       "cbQosCMDesc": cbQosCMDesc,
       "cbQosCMInfo": cbQosCMInfo,
       "cbQosMatchStmtCfg": cbQosMatchStmtCfg,
       "cbQosMatchStmtCfgTable": cbQosMatchStmtCfgTable,
       "cbQosMatchStmtCfgEntry": cbQosMatchStmtCfgEntry,
       "cbQosMatchStmtName": cbQosMatchStmtName,
       "cbQosMatchStmtInfo": cbQosMatchStmtInfo,
       "cbQosQueueingCfg": cbQosQueueingCfg,
       "cbQosQueueingCfgTable": cbQosQueueingCfgTable,
       "cbQosQueueingCfgEntry": cbQosQueueingCfgEntry,
       "cbQosQueueingCfgBandwidth": cbQosQueueingCfgBandwidth,
       "cbQosQueueingCfgBandwidthUnits": cbQosQueueingCfgBandwidthUnits,
       "cbQosQueueingCfgFlowEnabled": cbQosQueueingCfgFlowEnabled,
       "cbQosQueueingCfgPriorityEnabled": cbQosQueueingCfgPriorityEnabled,
       "cbQosQueueingCfgAggregateQSize": cbQosQueueingCfgAggregateQSize,
       "cbQosQueueingCfgIndividualQSize": cbQosQueueingCfgIndividualQSize,
       "cbQosQueueingCfgDynamicQNumber": cbQosQueueingCfgDynamicQNumber,
       "cbQosQueueingCfgPrioBurstSize": cbQosQueueingCfgPrioBurstSize,
       "cbQosQueueingCfgQLimitUnits": cbQosQueueingCfgQLimitUnits,
       "cbQosQueueingCfgAggregateQLimit": cbQosQueueingCfgAggregateQLimit,
       "cbQosQueueingCfgAggrQLimitTime": cbQosQueueingCfgAggrQLimitTime,
       "cbQosQueueingCfgPriorityLevel": cbQosQueueingCfgPriorityLevel,
       "cbQosQueueingCfgBandwidth64": cbQosQueueingCfgBandwidth64,
       "cbQosQueueingCfgIndividualQSize64": cbQosQueueingCfgIndividualQSize64,
       "cbQosREDCfg": cbQosREDCfg,
       "cbQosREDCfgTable": cbQosREDCfgTable,
       "cbQosREDCfgEntry": cbQosREDCfgEntry,
       "cbQosREDCfgExponWeight": cbQosREDCfgExponWeight,
       "cbQosREDCfgMeanQsize": cbQosREDCfgMeanQsize,
       "cbQosREDCfgDscpPrec": cbQosREDCfgDscpPrec,
       "cbQosREDCfgECNEnabled": cbQosREDCfgECNEnabled,
       "cbQosREDClassCfg": cbQosREDClassCfg,
       "cbQosREDClassCfgTable": cbQosREDClassCfgTable,
       "cbQosREDClassCfgEntry": cbQosREDClassCfgEntry,
       "cbQosREDValue": cbQosREDValue,
       "cbQosREDCfgMinThreshold": cbQosREDCfgMinThreshold,
       "cbQosREDCfgMaxThreshold": cbQosREDCfgMaxThreshold,
       "cbQosREDCfgPktDropProb": cbQosREDCfgPktDropProb,
       "cbQosREDClassCfgThresholdUnit": cbQosREDClassCfgThresholdUnit,
       "cbQosREDClassCfgMinThreshold": cbQosREDClassCfgMinThreshold,
       "cbQosREDClassCfgMaxThreshold": cbQosREDClassCfgMaxThreshold,
       "cbQosREDClassCfgMinThresholdTime": cbQosREDClassCfgMinThresholdTime,
       "cbQosREDClassCfgMaxThresholdTime": cbQosREDClassCfgMaxThresholdTime,
       "cbQosREDClassCfgMaxThresholdUnit": cbQosREDClassCfgMaxThresholdUnit,
       "cbQosREDClassCfgMinThresholdUnit": cbQosREDClassCfgMinThresholdUnit,
       "cbQosPoliceCfg": cbQosPoliceCfg,
       "cbQosPoliceCfgTable": cbQosPoliceCfgTable,
       "cbQosPoliceCfgEntry": cbQosPoliceCfgEntry,
       "cbQosPoliceCfgRate": cbQosPoliceCfgRate,
       "cbQosPoliceCfgBurstSize": cbQosPoliceCfgBurstSize,
       "cbQosPoliceCfgExtBurstSize": cbQosPoliceCfgExtBurstSize,
       "cbQosPoliceCfgConformAction": cbQosPoliceCfgConformAction,
       "cbQosPoliceCfgConformSetValue": cbQosPoliceCfgConformSetValue,
       "cbQosPoliceCfgExceedAction": cbQosPoliceCfgExceedAction,
       "cbQosPoliceCfgExceedSetValue": cbQosPoliceCfgExceedSetValue,
       "cbQosPoliceCfgViolateAction": cbQosPoliceCfgViolateAction,
       "cbQosPoliceCfgViolateSetValue": cbQosPoliceCfgViolateSetValue,
       "cbQosPoliceCfgPir": cbQosPoliceCfgPir,
       "cbQosPoliceCfgRate64": cbQosPoliceCfgRate64,
       "cbQosPoliceCfgRateType": cbQosPoliceCfgRateType,
       "cbQosPoliceCfgPercentRateValue": cbQosPoliceCfgPercentRateValue,
       "cbQosPoliceCfgPercentPirValue": cbQosPoliceCfgPercentPirValue,
       "cbQosPoliceCfgCellRate": cbQosPoliceCfgCellRate,
       "cbQosPoliceCfgCellPir": cbQosPoliceCfgCellPir,
       "cbQosPoliceCfgBurstCell": cbQosPoliceCfgBurstCell,
       "cbQosPoliceCfgExtBurstCell": cbQosPoliceCfgExtBurstCell,
       "cbQosPoliceCfgBurstTime": cbQosPoliceCfgBurstTime,
       "cbQosPoliceCfgExtBurstTime": cbQosPoliceCfgExtBurstTime,
       "cbQosPoliceCfgCdvt": cbQosPoliceCfgCdvt,
       "cbQosPoliceCfgConformColor": cbQosPoliceCfgConformColor,
       "cbQosPoliceCfgExceedColor": cbQosPoliceCfgExceedColor,
       "cbQosPoliceCfgConditional": cbQosPoliceCfgConditional,
       "cbQosPoliceCfgBurstSize64": cbQosPoliceCfgBurstSize64,
       "cbQosPoliceCfgExtBurstSize64": cbQosPoliceCfgExtBurstSize64,
       "cbQosPoliceCfgPir64": cbQosPoliceCfgPir64,
       "cbQosTSCfg": cbQosTSCfg,
       "cbQosTSCfgTable": cbQosTSCfgTable,
       "cbQosTSCfgEntry": cbQosTSCfgEntry,
       "cbQosTSCfgRate": cbQosTSCfgRate,
       "cbQosTSCfgBurstSize": cbQosTSCfgBurstSize,
       "cbQosTSCfgExtBurstSize": cbQosTSCfgExtBurstSize,
       "cbQosTSCfgAdaptiveEnabled": cbQosTSCfgAdaptiveEnabled,
       "cbQosTSCfgAdaptiveRate": cbQosTSCfgAdaptiveRate,
       "cbQosTSCfgLimitType": cbQosTSCfgLimitType,
       "cbQosTSCfgRateType": cbQosTSCfgRateType,
       "cbQosTSCfgPercentRateValue": cbQosTSCfgPercentRateValue,
       "cbQosTSCfgBurstTime": cbQosTSCfgBurstTime,
       "cbQosTSCfgExtBurstTime": cbQosTSCfgExtBurstTime,
       "cbQosTSCfgRate64": cbQosTSCfgRate64,
       "cbQosTSCfgBurstSize64": cbQosTSCfgBurstSize64,
       "cbQosTSCfgExtBurstSize64": cbQosTSCfgExtBurstSize64,
       "cbQosSetCfg": cbQosSetCfg,
       "cbQosSetCfgTable": cbQosSetCfgTable,
       "cbQosSetCfgEntry": cbQosSetCfgEntry,
       "cbQosSetCfgFeature": cbQosSetCfgFeature,
       "cbQosSetCfgIpDSCPValue": cbQosSetCfgIpDSCPValue,
       "cbQosSetCfgIpPrecedenceValue": cbQosSetCfgIpPrecedenceValue,
       "cbQosSetCfgQosGroupValue": cbQosSetCfgQosGroupValue,
       "cbQosSetCfgL2CosValue": cbQosSetCfgL2CosValue,
       "cbQosSetCfgMplsExpValue": cbQosSetCfgMplsExpValue,
       "cbQosSetCfgDiscardClassValue": cbQosSetCfgDiscardClassValue,
       "cbQosSetCfgMplsExpTopMostValue": cbQosSetCfgMplsExpTopMostValue,
       "cbQosSetCfgSrpPriority": cbQosSetCfgSrpPriority,
       "cbQosSetCfgFrFecnBecn": cbQosSetCfgFrFecnBecn,
       "cbQosSetCfgL2CosInnerValue": cbQosSetCfgL2CosInnerValue,
       "cbQosSetCfgFrDe": cbQosSetCfgFrDe,
       "cbQosSetCfgIpPrecedenceTunnelValue": cbQosSetCfgIpPrecedenceTunnelValue,
       "cbQosSetCfgIpDSCPTunnelValue": cbQosSetCfgIpDSCPTunnelValue,
       "cbQosSetCfgDei": cbQosSetCfgDei,
       "cbQosSetCfgDeiImposition": cbQosSetCfgDeiImposition,
       "cbQosClassMapStats": cbQosClassMapStats,
       "cbQosCMStatsTable": cbQosCMStatsTable,
       "cbQosCMStatsEntry": cbQosCMStatsEntry,
       "cbQosCMPrePolicyPktOverflow": cbQosCMPrePolicyPktOverflow,
       "cbQosCMPrePolicyPkt": cbQosCMPrePolicyPkt,
       "cbQosCMPrePolicyPkt64": cbQosCMPrePolicyPkt64,
       "cbQosCMPrePolicyByteOverflow": cbQosCMPrePolicyByteOverflow,
       "cbQosCMPrePolicyByte": cbQosCMPrePolicyByte,
       "cbQosCMPrePolicyByte64": cbQosCMPrePolicyByte64,
       "cbQosCMPrePolicyBitRate": cbQosCMPrePolicyBitRate,
       "cbQosCMPostPolicyByteOverflow": cbQosCMPostPolicyByteOverflow,
       "cbQosCMPostPolicyByte": cbQosCMPostPolicyByte,
       "cbQosCMPostPolicyByte64": cbQosCMPostPolicyByte64,
       "cbQosCMPostPolicyBitRate": cbQosCMPostPolicyBitRate,
       "cbQosCMDropPktOverflow": cbQosCMDropPktOverflow,
       "cbQosCMDropPkt": cbQosCMDropPkt,
       "cbQosCMDropPkt64": cbQosCMDropPkt64,
       "cbQosCMDropByteOverflow": cbQosCMDropByteOverflow,
       "cbQosCMDropByte": cbQosCMDropByte,
       "cbQosCMDropByte64": cbQosCMDropByte64,
       "cbQosCMDropBitRate": cbQosCMDropBitRate,
       "cbQosCMNoBufDropPktOverflow": cbQosCMNoBufDropPktOverflow,
       "cbQosCMNoBufDropPkt": cbQosCMNoBufDropPkt,
       "cbQosCMNoBufDropPkt64": cbQosCMNoBufDropPkt64,
       "cbQosCMFragmentPktOverflow": cbQosCMFragmentPktOverflow,
       "cbQosCMFragmentPkt": cbQosCMFragmentPkt,
       "cbQosCMFragmentPkt64": cbQosCMFragmentPkt64,
       "cbQosCMFragmentByteOverflow": cbQosCMFragmentByteOverflow,
       "cbQosCMFragmentByte": cbQosCMFragmentByte,
       "cbQosCMFragmentByte64": cbQosCMFragmentByte64,
       "cbQosCMPrePolicyBitRate64": cbQosCMPrePolicyBitRate64,
       "cbQosCMPostPolicyBitRate64": cbQosCMPostPolicyBitRate64,
       "cbQosCMDropBitRate64": cbQosCMDropBitRate64,
       "cbQosMatchStmtStats": cbQosMatchStmtStats,
       "cbQosMatchStmtStatsTable": cbQosMatchStmtStatsTable,
       "cbQosMatchStmtStatsEntry": cbQosMatchStmtStatsEntry,
       "cbQosMatchPrePolicyPktOverflow": cbQosMatchPrePolicyPktOverflow,
       "cbQosMatchPrePolicyPkt": cbQosMatchPrePolicyPkt,
       "cbQosMatchPrePolicyPkt64": cbQosMatchPrePolicyPkt64,
       "cbQosMatchPrePolicyByteOverflow": cbQosMatchPrePolicyByteOverflow,
       "cbQosMatchPrePolicyByte": cbQosMatchPrePolicyByte,
       "cbQosMatchPrePolicyByte64": cbQosMatchPrePolicyByte64,
       "cbQosMatchPrePolicyBitRate": cbQosMatchPrePolicyBitRate,
       "cbQosPoliceStats": cbQosPoliceStats,
       "cbQosPoliceStatsTable": cbQosPoliceStatsTable,
       "cbQosPoliceStatsEntry": cbQosPoliceStatsEntry,
       "cbQosPoliceConformedPktOverflow": cbQosPoliceConformedPktOverflow,
       "cbQosPoliceConformedPkt": cbQosPoliceConformedPkt,
       "cbQosPoliceConformedPkt64": cbQosPoliceConformedPkt64,
       "cbQosPoliceConformedByteOverflow": cbQosPoliceConformedByteOverflow,
       "cbQosPoliceConformedByte": cbQosPoliceConformedByte,
       "cbQosPoliceConformedByte64": cbQosPoliceConformedByte64,
       "cbQosPoliceConformedBitRate": cbQosPoliceConformedBitRate,
       "cbQosPoliceExceededPktOverflow": cbQosPoliceExceededPktOverflow,
       "cbQosPoliceExceededPkt": cbQosPoliceExceededPkt,
       "cbQosPoliceExceededPkt64": cbQosPoliceExceededPkt64,
       "cbQosPoliceExceededByteOverflow": cbQosPoliceExceededByteOverflow,
       "cbQosPoliceExceededByte": cbQosPoliceExceededByte,
       "cbQosPoliceExceededByte64": cbQosPoliceExceededByte64,
       "cbQosPoliceExceededBitRate": cbQosPoliceExceededBitRate,
       "cbQosPoliceViolatedPktOverflow": cbQosPoliceViolatedPktOverflow,
       "cbQosPoliceViolatedPkt": cbQosPoliceViolatedPkt,
       "cbQosPoliceViolatedPkt64": cbQosPoliceViolatedPkt64,
       "cbQosPoliceViolatedByteOverflow": cbQosPoliceViolatedByteOverflow,
       "cbQosPoliceViolatedByte": cbQosPoliceViolatedByte,
       "cbQosPoliceViolatedByte64": cbQosPoliceViolatedByte64,
       "cbQosPoliceViolatedBitRate": cbQosPoliceViolatedBitRate,
       "cbQosPoliceConformedBitRate64": cbQosPoliceConformedBitRate64,
       "cbQosPoliceExceededBitRate64": cbQosPoliceExceededBitRate64,
       "cbQosPoliceViolatedBitRate64": cbQosPoliceViolatedBitRate64,
       "cbQosQueueingStats": cbQosQueueingStats,
       "cbQosQueueingStatsTable": cbQosQueueingStatsTable,
       "cbQosQueueingStatsEntry": cbQosQueueingStatsEntry,
       "cbQosQueueingCurrentQDepth": cbQosQueueingCurrentQDepth,
       "cbQosQueueingMaxQDepth": cbQosQueueingMaxQDepth,
       "cbQosQueueingDiscardByteOverflow": cbQosQueueingDiscardByteOverflow,
       "cbQosQueueingDiscardByte": cbQosQueueingDiscardByte,
       "cbQosQueueingDiscardByte64": cbQosQueueingDiscardByte64,
       "cbQosQueueingDiscardPktOverflow": cbQosQueueingDiscardPktOverflow,
       "cbQosQueueingDiscardPkt": cbQosQueueingDiscardPkt,
       "cbQosQueueingDiscardPkt64": cbQosQueueingDiscardPkt64,
       "cbQosQueueingCurrentQDepthPkt": cbQosQueueingCurrentQDepthPkt,
       "cbQosQueueingMaxQDepthPkt": cbQosQueueingMaxQDepthPkt,
       "cbQosQueueingTransmitByte64": cbQosQueueingTransmitByte64,
       "cbQosQueueingTransmitPkt64": cbQosQueueingTransmitPkt64,
       "cbQosTSStats": cbQosTSStats,
       "cbQosTSStatsTable": cbQosTSStatsTable,
       "cbQosTSStatsEntry": cbQosTSStatsEntry,
       "cbQosTSStatsDelayedByteOverflow": cbQosTSStatsDelayedByteOverflow,
       "cbQosTSStatsDelayedByte": cbQosTSStatsDelayedByte,
       "cbQosTSStatsDelayedByte64": cbQosTSStatsDelayedByte64,
       "cbQosTSStatsDelayedPktOverflow": cbQosTSStatsDelayedPktOverflow,
       "cbQosTSStatsDelayedPkt": cbQosTSStatsDelayedPkt,
       "cbQosTSStatsDelayedPkt64": cbQosTSStatsDelayedPkt64,
       "cbQosTSStatsDropByteOverflow": cbQosTSStatsDropByteOverflow,
       "cbQosTSStatsDropByte": cbQosTSStatsDropByte,
       "cbQosTSStatsDropByte64": cbQosTSStatsDropByte64,
       "cbQosTSStatsDropPktOverflow": cbQosTSStatsDropPktOverflow,
       "cbQosTSStatsDropPkt": cbQosTSStatsDropPkt,
       "cbQosTSStatsDropPkt64": cbQosTSStatsDropPkt64,
       "cbQosTSStatsActive": cbQosTSStatsActive,
       "cbQosTSStatsCurrentQSize": cbQosTSStatsCurrentQSize,
       "cbQosREDClassStats": cbQosREDClassStats,
       "cbQosREDClassStatsTable": cbQosREDClassStatsTable,
       "cbQosREDClassStatsEntry": cbQosREDClassStatsEntry,
       "cbQosREDRandomDropPktOverflow": cbQosREDRandomDropPktOverflow,
       "cbQosREDRandomDropPkt": cbQosREDRandomDropPkt,
       "cbQosREDRandomDropPkt64": cbQosREDRandomDropPkt64,
       "cbQosREDRandomDropByteOverflow": cbQosREDRandomDropByteOverflow,
       "cbQosREDRandomDropByte": cbQosREDRandomDropByte,
       "cbQosREDRandomDropByte64": cbQosREDRandomDropByte64,
       "cbQosREDTailDropPktOverflow": cbQosREDTailDropPktOverflow,
       "cbQosREDTailDropPkt": cbQosREDTailDropPkt,
       "cbQosREDTailDropPkt64": cbQosREDTailDropPkt64,
       "cbQosREDTailDropByteOverflow": cbQosREDTailDropByteOverflow,
       "cbQosREDTailDropByte": cbQosREDTailDropByte,
       "cbQosREDTailDropByte64": cbQosREDTailDropByte64,
       "cbQosREDTransmitPktOverflow": cbQosREDTransmitPktOverflow,
       "cbQosREDTransmitPkt": cbQosREDTransmitPkt,
       "cbQosREDTransmitPkt64": cbQosREDTransmitPkt64,
       "cbQosREDTransmitByteOverflow": cbQosREDTransmitByteOverflow,
       "cbQosREDTransmitByte": cbQosREDTransmitByte,
       "cbQosREDTransmitByte64": cbQosREDTransmitByte64,
       "cbQosREDECNMarkPktOverflow": cbQosREDECNMarkPktOverflow,
       "cbQosREDECNMarkPkt": cbQosREDECNMarkPkt,
       "cbQosREDECNMarkPkt64": cbQosREDECNMarkPkt64,
       "cbQosREDECNMarkByteOverflow": cbQosREDECNMarkByteOverflow,
       "cbQosREDECNMarkByte": cbQosREDECNMarkByte,
       "cbQosREDECNMarkByte64": cbQosREDECNMarkByte64,
       "cbQosREDMeanQSizeUnits": cbQosREDMeanQSizeUnits,
       "cbQosREDMeanQSize": cbQosREDMeanQSize,
       "cbQosPoliceActionCfg": cbQosPoliceActionCfg,
       "cbQosPoliceActionCfgTable": cbQosPoliceActionCfgTable,
       "cbQosPoliceActionCfgEntry": cbQosPoliceActionCfgEntry,
       "cbQosPoliceActionCfgIndex": cbQosPoliceActionCfgIndex,
       "cbQosPoliceActionCfgConform": cbQosPoliceActionCfgConform,
       "cbQosPoliceActionCfgConformSetValue": cbQosPoliceActionCfgConformSetValue,
       "cbQosPoliceActionCfgExceed": cbQosPoliceActionCfgExceed,
       "cbQosPoliceActionCfgExceedSetValue": cbQosPoliceActionCfgExceedSetValue,
       "cbQosPoliceActionCfgViolate": cbQosPoliceActionCfgViolate,
       "cbQosPoliceActionCfgViolateSetValue": cbQosPoliceActionCfgViolateSetValue,
       "cbQosIPHCCfg": cbQosIPHCCfg,
       "cbQosIPHCCfgTable": cbQosIPHCCfgTable,
       "cbQosIPHCCfgEntry": cbQosIPHCCfgEntry,
       "cbQosIPHCCfgOption": cbQosIPHCCfgOption,
       "cbQosIPHCCfgEnabled": cbQosIPHCCfgEnabled,
       "cbQosIPHCStats": cbQosIPHCStats,
       "cbQosIPHCStatsTable": cbQosIPHCStatsTable,
       "cbQosIPHCStatsEntry": cbQosIPHCStatsEntry,
       "cbQosIPHCRtpSentPktOverflow": cbQosIPHCRtpSentPktOverflow,
       "cbQosIPHCRtpSentPkt": cbQosIPHCRtpSentPkt,
       "cbQosIPHCRtpSentPkt64": cbQosIPHCRtpSentPkt64,
       "cbQosIPHCRtpCmprsOutPktOverflow": cbQosIPHCRtpCmprsOutPktOverflow,
       "cbQosIPHCRtpCmprsOutPkt": cbQosIPHCRtpCmprsOutPkt,
       "cbQosIPHCRtpCmprsOutPkt64": cbQosIPHCRtpCmprsOutPkt64,
       "cbQosIPHCRtpSavedByteOverflow": cbQosIPHCRtpSavedByteOverflow,
       "cbQosIPHCRtpSavedByte": cbQosIPHCRtpSavedByte,
       "cbQosIPHCRtpSavedByte64": cbQosIPHCRtpSavedByte64,
       "cbQosIPHCRtpSentByteOverflow": cbQosIPHCRtpSentByteOverflow,
       "cbQosIPHCRtpSentByte": cbQosIPHCRtpSentByte,
       "cbQosIPHCRtpSentByte64": cbQosIPHCRtpSentByte64,
       "cbQosIPHCRtpSentByteRate": cbQosIPHCRtpSentByteRate,
       "cbQosIPHCTcpSentPktOverflow": cbQosIPHCTcpSentPktOverflow,
       "cbQosIPHCTcpSentPkt": cbQosIPHCTcpSentPkt,
       "cbQosIPHCTcpSentPkt64": cbQosIPHCTcpSentPkt64,
       "cbQosIPHCTcpCmprsOutPktOverflow": cbQosIPHCTcpCmprsOutPktOverflow,
       "cbQosIPHCTcpCmprsOutPkt": cbQosIPHCTcpCmprsOutPkt,
       "cbQosIPHCTcpCmprsOutPkt64": cbQosIPHCTcpCmprsOutPkt64,
       "cbQosIPHCTcpSavedByteOverflow": cbQosIPHCTcpSavedByteOverflow,
       "cbQosIPHCTcpSavedByte": cbQosIPHCTcpSavedByte,
       "cbQosIPHCTcpSavedByte64": cbQosIPHCTcpSavedByte64,
       "cbQosIPHCTcpSentByteOverflow": cbQosIPHCTcpSentByteOverflow,
       "cbQosIPHCTcpSentByte": cbQosIPHCTcpSentByte,
       "cbQosIPHCTcpSentByte64": cbQosIPHCTcpSentByte64,
       "cbQosIPHCTcpSentByteRate": cbQosIPHCTcpSentByteRate,
       "cbQosIPHCRtpFullHdrSentPktOverflow": cbQosIPHCRtpFullHdrSentPktOverflow,
       "cbQosIPHCRtpFullHdrSentPkt": cbQosIPHCRtpFullHdrSentPkt,
       "cbQosIPHCRtpFullHdrSentPkt64": cbQosIPHCRtpFullHdrSentPkt64,
       "cbQosIPHCTcpFullHdrSentPktOverflow": cbQosIPHCTcpFullHdrSentPktOverflow,
       "cbQosIPHCTcpFullHdrSentPkt": cbQosIPHCTcpFullHdrSentPkt,
       "cbQosIPHCTcpFullHdrSentPkt64": cbQosIPHCTcpFullHdrSentPkt64,
       "cbQosSetStats": cbQosSetStats,
       "cbQosSetStatsTable": cbQosSetStatsTable,
       "cbQosSetStatsEntry": cbQosSetStatsEntry,
       "cbQosSetDscpPkt64": cbQosSetDscpPkt64,
       "cbQosSetPrecedencePkt64": cbQosSetPrecedencePkt64,
       "cbQosSetQosGroupPkt64": cbQosSetQosGroupPkt64,
       "cbQosSetFrDePkt64": cbQosSetFrDePkt64,
       "cbQosSetAtmClpPkt64": cbQosSetAtmClpPkt64,
       "cbQosSetL2CosPkt64": cbQosSetL2CosPkt64,
       "cbQosSetMplsExpImpositionPkt64": cbQosSetMplsExpImpositionPkt64,
       "cbQosSetDiscardClassPkt64": cbQosSetDiscardClassPkt64,
       "cbQosSetMplsExpTopMostPkt64": cbQosSetMplsExpTopMostPkt64,
       "cbQosSetSrpPriorityPkt64": cbQosSetSrpPriorityPkt64,
       "cbQosSetFrFecnBecnPkt64": cbQosSetFrFecnBecnPkt64,
       "cbQosSetDscpTunnelPkt64": cbQosSetDscpTunnelPkt64,
       "cbQosSetPrecedenceTunnelPkt64": cbQosSetPrecedenceTunnelPkt64,
       "cbQosPoliceColorStats": cbQosPoliceColorStats,
       "cbQosPoliceColorStatsTable": cbQosPoliceColorStatsTable,
       "cbQosPoliceColorStatsEntry": cbQosPoliceColorStatsEntry,
       "cbQosPoliceCfmColorCfmPkt64": cbQosPoliceCfmColorCfmPkt64,
       "cbQosPoliceCfmColorCfmByte64": cbQosPoliceCfmColorCfmByte64,
       "cbQosPoliceCfmColorExdPkt64": cbQosPoliceCfmColorExdPkt64,
       "cbQosPoliceCfmColorExdByte64": cbQosPoliceCfmColorExdByte64,
       "cbQosPoliceCfmColorVltPkt64": cbQosPoliceCfmColorVltPkt64,
       "cbQosPoliceCfmColorVltByte64": cbQosPoliceCfmColorVltByte64,
       "cbQosPoliceExdColorExdPkt64": cbQosPoliceExdColorExdPkt64,
       "cbQosPoliceExdColorExdByte64": cbQosPoliceExdColorExdByte64,
       "cbQosPoliceExdColorVltPkt64": cbQosPoliceExdColorVltPkt64,
       "cbQosPoliceExdColorVltByte64": cbQosPoliceExdColorVltByte64,
       "cbQosPoliceVltColorVltPkt64": cbQosPoliceVltColorVltPkt64,
       "cbQosPoliceVltColorVltByte64": cbQosPoliceVltColorVltByte64,
       "cbQosPoliceCfmColorCfmBitRate": cbQosPoliceCfmColorCfmBitRate,
       "cbQosPoliceCfmColorExdBitRate": cbQosPoliceCfmColorExdBitRate,
       "cbQosPoliceCfmColorVltBitRate": cbQosPoliceCfmColorVltBitRate,
       "cbQosPoliceExdColorExdBitRate": cbQosPoliceExdColorExdBitRate,
       "cbQosPoliceExdColorVltBitRate": cbQosPoliceExdColorVltBitRate,
       "cbQosPoliceVltColorVltBitRate": cbQosPoliceVltColorVltBitRate,
       "cbQosTableMapCfg": cbQosTableMapCfg,
       "cbQosTableMapCfgTable": cbQosTableMapCfgTable,
       "cbQosTableMapCfgEntry": cbQosTableMapCfgEntry,
       "cbQosTableMapCfgIndex": cbQosTableMapCfgIndex,
       "cbQosTableMapCfgName": cbQosTableMapCfgName,
       "cbQosTableMapCfgBehavior": cbQosTableMapCfgBehavior,
       "cbQosTableMapCfgDftValue": cbQosTableMapCfgDftValue,
       "cbQosTableMapValueCfg": cbQosTableMapValueCfg,
       "cbQosTableMapValueCfgTable": cbQosTableMapValueCfgTable,
       "cbQosTableMapValueCfgEntry": cbQosTableMapValueCfgEntry,
       "cbQosTableMapValueCfgFrom": cbQosTableMapValueCfgFrom,
       "cbQosTableMapValueCfgTo": cbQosTableMapValueCfgTo,
       "cbQosTableMapSetCfg": cbQosTableMapSetCfg,
       "cbQosTableMapSetCfgTable": cbQosTableMapSetCfgTable,
       "cbQosTableMapSetCfgEntry": cbQosTableMapSetCfgEntry,
       "cbQosTMSetIpDscpFromType": cbQosTMSetIpDscpFromType,
       "cbQosTMSetIpDscpMapName": cbQosTMSetIpDscpMapName,
       "cbQosTMSetIpPrecedenceFromType": cbQosTMSetIpPrecedenceFromType,
       "cbQosTMSetIpPrecedenceMapName": cbQosTMSetIpPrecedenceMapName,
       "cbQosTMSetQosGroupFromType": cbQosTMSetQosGroupFromType,
       "cbQosTMSetQosGroupMapName": cbQosTMSetQosGroupMapName,
       "cbQosTMSetL2CosFromType": cbQosTMSetL2CosFromType,
       "cbQosTMSetL2CosMapName": cbQosTMSetL2CosMapName,
       "cbQosTMSetMplsExpImpFromType": cbQosTMSetMplsExpImpFromType,
       "cbQosTMSetMplsExpImpMapName": cbQosTMSetMplsExpImpMapName,
       "cbQosTMSetMplsExpTopFromType": cbQosTMSetMplsExpTopFromType,
       "cbQosTMSetMplsExpTopMapName": cbQosTMSetMplsExpTopMapName,
       "cbQosEBCfg": cbQosEBCfg,
       "cbQosEBCfgTable": cbQosEBCfgTable,
       "cbQosEBCfgEntry": cbQosEBCfgEntry,
       "cbQosEBCfgMechanism": cbQosEBCfgMechanism,
       "cbQosEBCfgDropTarget": cbQosEBCfgDropTarget,
       "cbQosEBCfgDelayTarget": cbQosEBCfgDelayTarget,
       "cbQosEBCfgDelayThreshold": cbQosEBCfgDelayThreshold,
       "cbQosEBStats": cbQosEBStats,
       "cbQosEBStatsTable": cbQosEBStatsTable,
       "cbQosEBStatsEntry": cbQosEBStatsEntry,
       "cbQosEBStatsCorvilEBValue": cbQosEBStatsCorvilEBValue,
       "cbQosEBStatsCorvilEBStatus": cbQosEBStatsCorvilEBStatus,
       "cbQosEBStatsCorvilCTD": cbQosEBStatsCorvilCTD,
       "cbQosMeasureIPSLACfg": cbQosMeasureIPSLACfg,
       "cbQosMeasureIPSLACfgTable": cbQosMeasureIPSLACfgTable,
       "cbQosMeasureIPSLACfgEntry": cbQosMeasureIPSLACfgEntry,
       "cbQosMeasureIPSLACfgGroupIndex": cbQosMeasureIPSLACfgGroupIndex,
       "cbQosMeasureIPSLACfgGroupName": cbQosMeasureIPSLACfgGroupName,
       "cbQosQueueingClassCfg": cbQosQueueingClassCfg,
       "cbQosQueueingClassCfgTable": cbQosQueueingClassCfgTable,
       "cbQosQueueingClassCfgEntry": cbQosQueueingClassCfgEntry,
       "cbQosQueueingClassConfigIndex": cbQosQueueingClassConfigIndex,
       "cbQosQlimitWeightValue": cbQosQlimitWeightValue,
       "cbQosQueueingClassCfgThreshold": cbQosQueueingClassCfgThreshold,
       "cbQosQueueingClassCfgThresholdUnit": cbQosQueueingClassCfgThresholdUnit,
       "cbQosQueueingClassCfgQLimitWeight": cbQosQueueingClassCfgQLimitWeight,
       "cbQosC3plAccountCfg": cbQosC3plAccountCfg,
       "cbQosC3plAccountCfgTable": cbQosC3plAccountCfgTable,
       "cbQosC3plAccountCfgEntry": cbQosC3plAccountCfgEntry,
       "cbQosC3plAccountFeatureType": cbQosC3plAccountFeatureType,
       "cbQosC3plAccountStats": cbQosC3plAccountStats,
       "cbQosC3plAccountStatsTable": cbQosC3plAccountStatsTable,
       "cbQosC3plAccountStatsEntry": cbQosC3plAccountStatsEntry,
       "cbQosC3plAccountDropPktOverflow": cbQosC3plAccountDropPktOverflow,
       "cbQosC3plAccountDropPkt": cbQosC3plAccountDropPkt,
       "cbQosC3plAccountDropPkt64": cbQosC3plAccountDropPkt64,
       "cbQosC3plAccountDropByteOverflow": cbQosC3plAccountDropByteOverflow,
       "cbQosC3plAccountDropByte": cbQosC3plAccountDropByte,
       "cbQosC3plAccountDropByte64": cbQosC3plAccountDropByte64,
       "cbQosC3plAccountTailDropPktOverflow": cbQosC3plAccountTailDropPktOverflow,
       "cbQosC3plAccountTailDropPkt": cbQosC3plAccountTailDropPkt,
       "cbQosC3plAccountTailDropPkt64": cbQosC3plAccountTailDropPkt64,
       "cbQosC3plAccountTailDropByteOverflow": cbQosC3plAccountTailDropByteOverflow,
       "cbQosC3plAccountTailDropByte": cbQosC3plAccountTailDropByte,
       "cbQosC3plAccountTailDropByte64": cbQosC3plAccountTailDropByte64,
       "ciscocbQosMIBConformance": ciscocbQosMIBConformance,
       "ciscocbQosMIBCompliances": ciscocbQosMIBCompliances,
       "ciscocbQosMIBCompliance": ciscocbQosMIBCompliance,
       "ciscocbQosMIBComplianceRev1": ciscocbQosMIBComplianceRev1,
       "ciscocbQosMIBComplianceRev2": ciscocbQosMIBComplianceRev2,
       "ciscocbQosMIBComplianceRev3": ciscocbQosMIBComplianceRev3,
       "ciscocbQosMIBComplianceRev4": ciscocbQosMIBComplianceRev4,
       "ciscocbQosMIBComplianceRev5": ciscocbQosMIBComplianceRev5,
       "ciscocbQosMIBComplianceRev6": ciscocbQosMIBComplianceRev6,
       "ciscocbQosMIBComplianceRev7": ciscocbQosMIBComplianceRev7,
       "ciscocbQosMIBComplianceRev8": ciscocbQosMIBComplianceRev8,
       "ciscocbQosMIBComplianceRev9": ciscocbQosMIBComplianceRev9,
       "ciscocbQosMIBComplianceRev10": ciscocbQosMIBComplianceRev10,
       "ciscocbQosMIBComplianceRev11": ciscocbQosMIBComplianceRev11,
       "ciscocbQosMIBComplianceRev12": ciscocbQosMIBComplianceRev12,
       "ciscocbQosMIBComplianceRev13": ciscocbQosMIBComplianceRev13,
       "ciscocbQosMIBGroups": ciscocbQosMIBGroups,
       "cbQosServicePolicyGroup": cbQosServicePolicyGroup,
       "cbQosInterfacePolicyGroup": cbQosInterfacePolicyGroup,
       "cbQosFrameRelayVCPolicyGroup": cbQosFrameRelayVCPolicyGroup,
       "cbQosATMPVCPolicyGroup": cbQosATMPVCPolicyGroup,
       "cbQosObjectsGroup": cbQosObjectsGroup,
       "cbQosPolicyMapCfgGroup": cbQosPolicyMapCfgGroup,
       "cbQosClassMapCfgGroup": cbQosClassMapCfgGroup,
       "cbQosMatchStmtCfgGroup": cbQosMatchStmtCfgGroup,
       "cbQosQueueingCfgGroup": cbQosQueueingCfgGroup,
       "cbQosREDCfgGroup": cbQosREDCfgGroup,
       "cbQosREDClassCfgGroup": cbQosREDClassCfgGroup,
       "cbQosPoliceCfgGroup": cbQosPoliceCfgGroup,
       "cbQosTSCfgGroup": cbQosTSCfgGroup,
       "cbQosSetCfgGroup": cbQosSetCfgGroup,
       "cbQosClassMapStatsGroup": cbQosClassMapStatsGroup,
       "cbQosNoBufferDropGroup": cbQosNoBufferDropGroup,
       "cbQosQueueingDynamicQNumberGroup": cbQosQueueingDynamicQNumberGroup,
       "cbQosTrafficShapingDelayCountersGroup": cbQosTrafficShapingDelayCountersGroup,
       "cbQosMatchStmtStatsGroup": cbQosMatchStmtStatsGroup,
       "cbQosPoliceStatsGroup": cbQosPoliceStatsGroup,
       "cbQosQueueingStatsGroup": cbQosQueueingStatsGroup,
       "cbQosTSStatsGroup": cbQosTSStatsGroup,
       "cbQosREDClassStatsGroup": cbQosREDClassStatsGroup,
       "cbQosREDClassXmitCountersGroup": cbQosREDClassXmitCountersGroup,
       "cbQosAFPoliceStatsGroup": cbQosAFPoliceStatsGroup,
       "cbQosAFPoliceCfgGroup": cbQosAFPoliceCfgGroup,
       "cbQosREDDscpCfgGroup": cbQosREDDscpCfgGroup,
       "cbQosNewSetCfgGroup": cbQosNewSetCfgGroup,
       "cbQosQueueingCfgGroupRev1": cbQosQueueingCfgGroupRev1,
       "cbQosREDCfgGroupRev1": cbQosREDCfgGroupRev1,
       "cbQosREDClassCfgGroupRev1": cbQosREDClassCfgGroupRev1,
       "cbQosPoliceCfgGroupRev1": cbQosPoliceCfgGroupRev1,
       "cbQosPoliceActionCfgGroup": cbQosPoliceActionCfgGroup,
       "cbQosAFPoliceViolateCfgGroup": cbQosAFPoliceViolateCfgGroup,
       "cbQosREDECNCfgGroup": cbQosREDECNCfgGroup,
       "cbQosREDClassECNMarkCountersGroup": cbQosREDClassECNMarkCountersGroup,
       "cbQosPoliceCfgExtGroup": cbQosPoliceCfgExtGroup,
       "cbQosSetCfgGroupRev1": cbQosSetCfgGroupRev1,
       "cbQosSetCfgMplsImpositionGroup": cbQosSetCfgMplsImpositionGroup,
       "cbQosSetCfgDiscardClassGroup": cbQosSetCfgDiscardClassGroup,
       "cbQosSetCfgMPLSTopMostGroup": cbQosSetCfgMPLSTopMostGroup,
       "cbQosPoliceCfgGroupRev2": cbQosPoliceCfgGroupRev2,
       "cbQosPoliceCfgPirGroup": cbQosPoliceCfgPirGroup,
       "cbQosPoliceCfgPercentGroup": cbQosPoliceCfgPercentGroup,
       "cbQosTSCfgPercentGroup": cbQosTSCfgPercentGroup,
       "cbQosIPHCCfgGroup": cbQosIPHCCfgGroup,
       "cbQosIPHCStatsGroup": cbQosIPHCStatsGroup,
       "cbQosServicePolicyGroupRev1": cbQosServicePolicyGroupRev1,
       "cbQosQueueingCfgQLimitTimeGroup": cbQosQueueingCfgQLimitTimeGroup,
       "cbQosREDCfgThresholdTimeGroup": cbQosREDCfgThresholdTimeGroup,
       "cbQosPoliceCfgCellGroup": cbQosPoliceCfgCellGroup,
       "cbQosPoliceCfgTimeGroup": cbQosPoliceCfgTimeGroup,
       "cbQosPoliceCfgCdvtGroup": cbQosPoliceCfgCdvtGroup,
       "cbQosPoliceCfgColorGroup": cbQosPoliceCfgColorGroup,
       "cbQosTSCfgTimeGroup": cbQosTSCfgTimeGroup,
       "cbQosSetCfgSrpPriorityGroup": cbQosSetCfgSrpPriorityGroup,
       "cbQosSetCfgFrFecnBecnGroup": cbQosSetCfgFrFecnBecnGroup,
       "cbQosSetStatsGroup": cbQosSetStatsGroup,
       "cbQosPoliceColorStatsGroup": cbQosPoliceColorStatsGroup,
       "cbQosTableMapCfgGroup": cbQosTableMapCfgGroup,
       "cbQosEBCfgGroup": cbQosEBCfgGroup,
       "cbQosEBStatsGroup": cbQosEBStatsGroup,
       "cbQosServicePolicyExtGroup": cbQosServicePolicyExtGroup,
       "cbQosMeasureIPSLACfgGroup": cbQosMeasureIPSLACfgGroup,
       "cbQosTSCfgExtGroup": cbQosTSCfgExtGroup,
       "cbQosQueueingCfgGroupRev2": cbQosQueueingCfgGroupRev2,
       "cbQosSetCfgL2Group": cbQosSetCfgL2Group,
       "cbQosREDClassCfgGroupRev2": cbQosREDClassCfgGroupRev2,
       "cbQosQueueingClassCfgGroup": cbQosQueueingClassCfgGroup,
       "cbQosPoliceCfgGroupRev3": cbQosPoliceCfgGroupRev3,
       "cbQosC3plAccountCfgGroup": cbQosC3plAccountCfgGroup,
       "cbQosC3plAccountStatsGroup": cbQosC3plAccountStatsGroup,
       "cbQosSetCfgFrDeGroup": cbQosSetCfgFrDeGroup,
       "cbQosEVCGroup": cbQosEVCGroup,
       "cbQosFragmentGroup": cbQosFragmentGroup,
       "cbQosSetCfgExt": cbQosSetCfgExt,
       "cbQosPoliceColorStatsExt": cbQosPoliceColorStatsExt,
       "cbQosIPHCCfgExt": cbQosIPHCCfgExt,
       "cbQosIPHCStatsExt": cbQosIPHCStatsExt,
       "cbQos421XRCfgExt": cbQos421XRCfgExt,
       "cbQosBitRateExt": cbQosBitRateExt,
       "cbQosQueueingStatsGroupRev1": cbQosQueueingStatsGroupRev1,
       "cbQosServicePolicyExtGroupRev2": cbQosServicePolicyExtGroupRev2}
)
