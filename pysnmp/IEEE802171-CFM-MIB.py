# SNMP MIB module (IEEE802171-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE802171-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:20 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpManAddress,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpManAddress",
    "LldpPortId",
    "LldpPortIdSubtype")

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
 iso,
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
    "zeroDotZero")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TransportAddress,
 TransportDomain) = mibBuilder.importSymbols(
    "TRANSPORT-ADDRESS-MIB",
    "TransportAddress",
    "TransportDomain")


# MODULE-IDENTITY

ieee8021cfmMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 3)
)
ieee8021cfmMIB.setRevisions(
        ("2006-11-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1agCfmMaintDomainNameType(Integer32, TextualConvention):
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
        *(("charString", 4),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("none", 1))
    )



class Dot1agCfmMaintDomainName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )



class Dot1agCfmMaintAssocNameType(Integer32, TextualConvention):
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
        *(("charString", 2),
          ("primaryVid", 1),
          ("rfc2865VpnId", 4),
          ("unsignedInt16", 3))
    )



class Dot1agCfmMaintAssocName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class Dot1agCfmMaintenanceDomainLevel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMpDirection(Integer32, TextualConvention):
    status = "current"
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



class Dot1agCfmPortStatus(Integer32, TextualConvention):
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
        *(("psBlocked", 1),
          ("psNoPortStateTLV", 0),
          ("psUp", 2))
    )



class Dot1agCfmInterfaceStatus(Integer32, TextualConvention):
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("isDormant", 5),
          ("isDown", 2),
          ("isLowerLayerDown", 7),
          ("isNoInterfaceSatatusTLV", 0),
          ("isNotPresent", 6),
          ("isTesting", 3),
          ("isUnknown", 4),
          ("isUp", 1))
    )



class Dot1agCfmHighestDefectPri(Integer32, TextualConvention):
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
        *(("defErrorCCM", 5),
          ("defMACstatus", 3),
          ("defRDICCM", 2),
          ("defRemoteCCM", 4),
          ("defXconCCM", 6),
          ("none", 1))
    )



class Dot1agCfmLowestAlarmPri(Integer32, TextualConvention):
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
        *(("allDef", 1),
          ("errXcon", 4),
          ("macRemErrXcon", 2),
          ("noDef", 6),
          ("remErrXcon", 3),
          ("xcon", 5))
    )



class Dot1agCfmMepId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class Dot1agCfmMepIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )



class Dot1agCfmMhfCreation(Integer32, TextualConvention):
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
        *(("defMHFdefault", 2),
          ("defMHFexplicit", 3),
          ("defMHFnone", 1))
    )



class Dot1agCfmCcmInterval(Integer32, TextualConvention):
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 3),
          ("interval10min", 7),
          ("interval10ms", 2),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval1s", 4),
          ("interval300Hz", 1),
          ("intervalInvalid", 0))
    )



class Dot1agCfmFngState(Integer32, TextualConvention):
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
        *(("fngDefect", 2),
          ("fngDefectClearing", 5),
          ("fngDefectReported", 4),
          ("fngReportDefect", 3),
          ("fngReset", 1))
    )



class Dot1agCfmRelayActionFieldValue(Integer32, TextualConvention):
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



class Dot1agCfmIngressActionFieldValue(Integer32, TextualConvention):
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



class Dot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
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



class Dot1agCfmRemoteMepState(Integer32, TextualConvention):
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
        *(("rMepFailed", 3),
          ("rMepIdle", 1),
          ("rMepOk", 4),
          ("rMepStart", 2))
    )



class Dot1afCfmIndexIntegerNextFree(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Dot1agCfmConfigErrors(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Dot1agNotifications_ObjectIdentity = ObjectIdentity
dot1agNotifications = _Dot1agNotifications_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 0)
)
_Dot1agMIBObjects_ObjectIdentity = ObjectIdentity
dot1agMIBObjects = _Dot1agMIBObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1)
)
_Dot1agCfmStack_ObjectIdentity = ObjectIdentity
dot1agCfmStack = _Dot1agCfmStack_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 1)
)
_Dot1agCfmStackTable_Object = MibTable
dot1agCfmStackTable = _Dot1agCfmStackTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmStackTable.setStatus("current")
_Dot1agCfmStackEntry_Object = MibTableRow
dot1agCfmStackEntry = _Dot1agCfmStackEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1)
)
dot1agCfmStackEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmStackifIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmStackDirection"),
)
if mibBuilder.loadTexts:
    dot1agCfmStackEntry.setStatus("current")
_Dot1agCfmStackifIndex_Type = InterfaceIndex
_Dot1agCfmStackifIndex_Object = MibTableColumn
dot1agCfmStackifIndex = _Dot1agCfmStackifIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 1),
    _Dot1agCfmStackifIndex_Type()
)
dot1agCfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackifIndex.setStatus("current")
_Dot1agCfmStackDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmStackDirection_Object = MibTableColumn
dot1agCfmStackDirection = _Dot1agCfmStackDirection_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 2),
    _Dot1agCfmStackDirection_Type()
)
dot1agCfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackDirection.setStatus("current")
_Dot1agCfmStackMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmStackMepId_Object = MibTableColumn
dot1agCfmStackMepId = _Dot1agCfmStackMepId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 3),
    _Dot1agCfmStackMepId_Type()
)
dot1agCfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMepId.setStatus("current")
_Dot1agCfmStackMacAddress_Type = MacAddress
_Dot1agCfmStackMacAddress_Object = MibTableColumn
dot1agCfmStackMacAddress = _Dot1agCfmStackMacAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 4),
    _Dot1agCfmStackMacAddress_Type()
)
dot1agCfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMacAddress.setStatus("current")
_Dot1agCfmDefaultMdLevel_ObjectIdentity = ObjectIdentity
dot1agCfmDefaultMdLevel = _Dot1agCfmDefaultMdLevel_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 2)
)
_Dot1agCfmDefaultMdLevelTable_Object = MibTable
dot1agCfmDefaultMdLevelTable = _Dot1agCfmDefaultMdLevelTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelTable.setStatus("current")
_Dot1agCfmDefaultMdLevelEntry_Object = MibTableRow
dot1agCfmDefaultMdLevelEntry = _Dot1agCfmDefaultMdLevelEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1)
)
dot1agCfmDefaultMdLevelEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelEntry.setStatus("current")


class _Dot1agCfmDefaultMdLevelIndex_Type(Unsigned32):
    """Custom type dot1agCfmDefaultMdLevelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmDefaultMdLevelIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmDefaultMdLevelIndex_Object = MibTableColumn
dot1agCfmDefaultMdLevelIndex = _Dot1agCfmDefaultMdLevelIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 1),
    _Dot1agCfmDefaultMdLevelIndex_Type()
)
dot1agCfmDefaultMdLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelIndex.setStatus("current")
_Dot1agCfmDefaultMdLevelVid_Type = VlanIdOrNone
_Dot1agCfmDefaultMdLevelVid_Object = MibTableColumn
dot1agCfmDefaultMdLevelVid = _Dot1agCfmDefaultMdLevelVid_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 2),
    _Dot1agCfmDefaultMdLevelVid_Type()
)
dot1agCfmDefaultMdLevelVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelVid.setStatus("current")


class _Dot1agCfmDefaultMdLevelMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmDefaultMdLevelMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmDefaultMdLevelMhfCreation_Object = MibTableColumn
dot1agCfmDefaultMdLevelMhfCreation = _Dot1agCfmDefaultMdLevelMhfCreation_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 3),
    _Dot1agCfmDefaultMdLevelMhfCreation_Type()
)
dot1agCfmDefaultMdLevelMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelMhfCreation.setStatus("current")


class _Dot1agCfmDefaultMdLevelLevel_Type(Dot1agCfmMaintenanceDomainLevel):
    """Custom type dot1agCfmDefaultMdLevelLevel based on Dot1agCfmMaintenanceDomainLevel"""
    defaultValue = -1


_Dot1agCfmDefaultMdLevelLevel_Object = MibTableColumn
dot1agCfmDefaultMdLevelLevel = _Dot1agCfmDefaultMdLevelLevel_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 4),
    _Dot1agCfmDefaultMdLevelLevel_Type()
)
dot1agCfmDefaultMdLevelLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelLevel.setStatus("current")
_Dot1agCfmConfigErrorList_ObjectIdentity = ObjectIdentity
dot1agCfmConfigErrorList = _Dot1agCfmConfigErrorList_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 3)
)
_Dot1agCfmConfigErrorListTable_Object = MibTable
dot1agCfmConfigErrorListTable = _Dot1agCfmConfigErrorListTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListTable.setStatus("current")
_Dot1agCfmConfigErrorListEntry_Object = MibTableRow
dot1agCfmConfigErrorListEntry = _Dot1agCfmConfigErrorListEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 3, 1, 1)
)
dot1agCfmConfigErrorListEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListVid"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListEntry.setStatus("current")
_Dot1agCfmConfigErrorListVid_Type = VlanId
_Dot1agCfmConfigErrorListVid_Object = MibTableColumn
dot1agCfmConfigErrorListVid = _Dot1agCfmConfigErrorListVid_Object(
    (1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 1),
    _Dot1agCfmConfigErrorListVid_Type()
)
dot1agCfmConfigErrorListVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListVid.setStatus("current")
_Dot1agCfmConfigErrorListIfIndex_Type = InterfaceIndex
_Dot1agCfmConfigErrorListIfIndex_Object = MibTableColumn
dot1agCfmConfigErrorListIfIndex = _Dot1agCfmConfigErrorListIfIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 2),
    _Dot1agCfmConfigErrorListIfIndex_Type()
)
dot1agCfmConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListIfIndex.setStatus("current")
_Dot1agCfmConfigErrorListErrorType_Type = Dot1agCfmConfigErrors
_Dot1agCfmConfigErrorListErrorType_Object = MibTableColumn
dot1agCfmConfigErrorListErrorType = _Dot1agCfmConfigErrorListErrorType_Object(
    (1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 3),
    _Dot1agCfmConfigErrorListErrorType_Type()
)
dot1agCfmConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListErrorType.setStatus("current")
_Dot1agCfmMd_ObjectIdentity = ObjectIdentity
dot1agCfmMd = _Dot1agCfmMd_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 4)
)
_Dot1agCfmMdTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdTableNextIndex_Object = MibScalar
dot1agCfmMdTableNextIndex = _Dot1agCfmMdTableNextIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 1),
    _Dot1agCfmMdTableNextIndex_Type()
)
dot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdTableNextIndex.setStatus("current")
_Dot1agCfmMdTable_Object = MibTable
dot1agCfmMdTable = _Dot1agCfmMdTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMdTable.setStatus("current")
_Dot1agCfmMdEntry_Object = MibTableRow
dot1agCfmMdEntry = _Dot1agCfmMdEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1)
)
dot1agCfmMdEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMdEntry.setStatus("current")


class _Dot1agCfmMdIndex_Type(Unsigned32):
    """Custom type dot1agCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmMdIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMdIndex_Object = MibTableColumn
dot1agCfmMdIndex = _Dot1agCfmMdIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 1),
    _Dot1agCfmMdIndex_Type()
)
dot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMdIndex.setStatus("current")


class _Dot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type dot1agCfmMdFormat based on Dot1agCfmMaintDomainNameType"""


_Dot1agCfmMdFormat_Object = MibTableColumn
dot1agCfmMdFormat = _Dot1agCfmMdFormat_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 2),
    _Dot1agCfmMdFormat_Type()
)
dot1agCfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdFormat.setStatus("current")


class _Dot1agCfmMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type dot1agCfmMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_Dot1agCfmMdName_Object = MibTableColumn
dot1agCfmMdName = _Dot1agCfmMdName_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 3),
    _Dot1agCfmMdName_Type()
)
dot1agCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdName.setStatus("current")


class _Dot1agCfmMdLevel_Type(Dot1agCfmMaintenanceDomainLevel):
    """Custom type dot1agCfmMdLevel based on Dot1agCfmMaintenanceDomainLevel"""
    defaultValue = 0


_Dot1agCfmMdLevel_Object = MibTableColumn
dot1agCfmMdLevel = _Dot1agCfmMdLevel_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 4),
    _Dot1agCfmMdLevel_Type()
)
dot1agCfmMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdLevel.setStatus("current")


class _Dot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMdMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmMdMhfCreation_Object = MibTableColumn
dot1agCfmMdMhfCreation = _Dot1agCfmMdMhfCreation_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 5),
    _Dot1agCfmMdMhfCreation_Type()
)
dot1agCfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfCreation.setStatus("current")


class _Dot1agCfmMdFaultAlarmDestDomain_Type(TransportDomain):
    """Custom type dot1agCfmMdFaultAlarmDestDomain based on TransportDomain"""
    defaultValue = (0, 0)


_Dot1agCfmMdFaultAlarmDestDomain_Object = MibTableColumn
dot1agCfmMdFaultAlarmDestDomain = _Dot1agCfmMdFaultAlarmDestDomain_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 6),
    _Dot1agCfmMdFaultAlarmDestDomain_Type()
)
dot1agCfmMdFaultAlarmDestDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdFaultAlarmDestDomain.setStatus("current")
_Dot1agCfmMdFaulAlarmDestAddress_Type = TransportAddress
_Dot1agCfmMdFaulAlarmDestAddress_Object = MibTableColumn
dot1agCfmMdFaulAlarmDestAddress = _Dot1agCfmMdFaulAlarmDestAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 7),
    _Dot1agCfmMdFaulAlarmDestAddress_Type()
)
dot1agCfmMdFaulAlarmDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdFaulAlarmDestAddress.setStatus("current")
_Dot1agCfmMdRowStatus_Type = RowStatus
_Dot1agCfmMdRowStatus_Object = MibTableColumn
dot1agCfmMdRowStatus = _Dot1agCfmMdRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 8),
    _Dot1agCfmMdRowStatus_Type()
)
dot1agCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdRowStatus.setStatus("current")
_Dot1agCfmMa_ObjectIdentity = ObjectIdentity
dot1agCfmMa = _Dot1agCfmMa_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 5)
)
_Dot1agCfmMaTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMaTableNextIndex_Object = MibScalar
dot1agCfmMaTableNextIndex = _Dot1agCfmMaTableNextIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 1),
    _Dot1agCfmMaTableNextIndex_Type()
)
dot1agCfmMaTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaTableNextIndex.setStatus("current")
_Dot1agCfmMaTable_Object = MibTable
dot1agCfmMaTable = _Dot1agCfmMaTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMaTable.setStatus("current")
_Dot1agCfmMaEntry_Object = MibTableRow
dot1agCfmMaEntry = _Dot1agCfmMaEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1)
)
dot1agCfmMaEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaEntry.setStatus("current")


class _Dot1agCfmMaIndex_Type(Unsigned32):
    """Custom type dot1agCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(16777217, 4294967295),
    )


_Dot1agCfmMaIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMaIndex_Object = MibTableColumn
dot1agCfmMaIndex = _Dot1agCfmMaIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 1),
    _Dot1agCfmMaIndex_Type()
)
dot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaIndex.setStatus("current")
_Dot1agCfmMaFormat_Type = Dot1agCfmMaintAssocNameType
_Dot1agCfmMaFormat_Object = MibTableColumn
dot1agCfmMaFormat = _Dot1agCfmMaFormat_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 2),
    _Dot1agCfmMaFormat_Type()
)
dot1agCfmMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaFormat.setStatus("current")
_Dot1agCfmMaName_Type = Dot1agCfmMaintAssocName
_Dot1agCfmMaName_Object = MibTableColumn
dot1agCfmMaName = _Dot1agCfmMaName_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 3),
    _Dot1agCfmMaName_Type()
)
dot1agCfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaName.setStatus("current")


class _Dot1agCfmMaMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMaMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmMaMhfCreation_Object = MibTableColumn
dot1agCfmMaMhfCreation = _Dot1agCfmMaMhfCreation_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 4),
    _Dot1agCfmMaMhfCreation_Type()
)
dot1agCfmMaMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMhfCreation.setStatus("current")


class _Dot1agCfmMaCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type dot1agCfmMaCcmInterval based on Dot1agCfmCcmInterval"""


_Dot1agCfmMaCcmInterval_Object = MibTableColumn
dot1agCfmMaCcmInterval = _Dot1agCfmMaCcmInterval_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 5),
    _Dot1agCfmMaCcmInterval_Type()
)
dot1agCfmMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCcmInterval.setStatus("current")


class _Dot1agCfmMaFaultAlarmDestDomain_Type(TransportDomain):
    """Custom type dot1agCfmMaFaultAlarmDestDomain based on TransportDomain"""
    defaultValue = (0, 0)


_Dot1agCfmMaFaultAlarmDestDomain_Object = MibTableColumn
dot1agCfmMaFaultAlarmDestDomain = _Dot1agCfmMaFaultAlarmDestDomain_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 6),
    _Dot1agCfmMaFaultAlarmDestDomain_Type()
)
dot1agCfmMaFaultAlarmDestDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaFaultAlarmDestDomain.setStatus("current")
_Dot1agCfmMaFaulAlarmDestAddress_Type = TransportAddress
_Dot1agCfmMaFaulAlarmDestAddress_Object = MibTableColumn
dot1agCfmMaFaulAlarmDestAddress = _Dot1agCfmMaFaulAlarmDestAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 7),
    _Dot1agCfmMaFaulAlarmDestAddress_Type()
)
dot1agCfmMaFaulAlarmDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaFaulAlarmDestAddress.setStatus("current")
_Dot1agCfmMaMoreThanOneVid_Type = TruthValue
_Dot1agCfmMaMoreThanOneVid_Object = MibTableColumn
dot1agCfmMaMoreThanOneVid = _Dot1agCfmMaMoreThanOneVid_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 8),
    _Dot1agCfmMaMoreThanOneVid_Type()
)
dot1agCfmMaMoreThanOneVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMoreThanOneVid.setStatus("current")
_Dot1agCfmMaRowStatus_Type = RowStatus
_Dot1agCfmMaRowStatus_Object = MibTableColumn
dot1agCfmMaRowStatus = _Dot1agCfmMaRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 9),
    _Dot1agCfmMaRowStatus_Type()
)
dot1agCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaRowStatus.setStatus("current")
_Dot1agCfmMaVlanTable_Object = MibTable
dot1agCfmMaVlanTable = _Dot1agCfmMaVlanTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanTable.setStatus("current")
_Dot1agCfmMaVlanEntry_Object = MibTableRow
dot1agCfmMaVlanEntry = _Dot1agCfmMaVlanEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 4, 1)
)
dot1agCfmMaVlanEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaVlanVid"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanEntry.setStatus("current")
_Dot1agCfmMaVlanVid_Type = VlanId
_Dot1agCfmMaVlanVid_Object = MibTableColumn
dot1agCfmMaVlanVid = _Dot1agCfmMaVlanVid_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 4, 1, 1),
    _Dot1agCfmMaVlanVid_Type()
)
dot1agCfmMaVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanVid.setStatus("current")
_Dot1agCfmMaVlanRowStatus_Type = RowStatus
_Dot1agCfmMaVlanRowStatus_Object = MibTableColumn
dot1agCfmMaVlanRowStatus = _Dot1agCfmMaVlanRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 4, 1, 2),
    _Dot1agCfmMaVlanRowStatus_Type()
)
dot1agCfmMaVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanRowStatus.setStatus("current")
_Dot1agCfmMaMepListTable_Object = MibTable
dot1agCfmMaMepListTable = _Dot1agCfmMaMepListTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 8)
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListTable.setStatus("current")
_Dot1agCfmMaMepListEntry_Object = MibTableRow
dot1agCfmMaMepListEntry = _Dot1agCfmMaMepListEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 8, 1)
)
dot1agCfmMaMepListEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListEntry.setStatus("current")
_Dot1agCfmMaMepListIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMaMepListIdentifier_Object = MibTableColumn
dot1agCfmMaMepListIdentifier = _Dot1agCfmMaMepListIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 8, 1, 1),
    _Dot1agCfmMaMepListIdentifier_Type()
)
dot1agCfmMaMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListIdentifier.setStatus("current")
_Dot1agCfmMaMepListRowStatus_Type = RowStatus
_Dot1agCfmMaMepListRowStatus_Object = MibTableColumn
dot1agCfmMaMepListRowStatus = _Dot1agCfmMaMepListRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 5, 8, 1, 2),
    _Dot1agCfmMaMepListRowStatus_Type()
)
dot1agCfmMaMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListRowStatus.setStatus("current")
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 6)
)
_Dot1agCfmMepTable_Object = MibTable
dot1agCfmMepTable = _Dot1agCfmMepTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMepTable.setStatus("current")
_Dot1agCfmMepEntry_Object = MibTableRow
dot1agCfmMepEntry = _Dot1agCfmMepEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1)
)
dot1agCfmMepEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepEntry.setStatus("current")
_Dot1agCfmMepIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMepIdentifier_Object = MibTableColumn
dot1agCfmMepIdentifier = _Dot1agCfmMepIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 1),
    _Dot1agCfmMepIdentifier_Type()
)
dot1agCfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepIdentifier.setStatus("current")
_Dot1agCfmMepIfIndex_Type = InterfaceIndex
_Dot1agCfmMepIfIndex_Object = MibTableColumn
dot1agCfmMepIfIndex = _Dot1agCfmMepIfIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 2),
    _Dot1agCfmMepIfIndex_Type()
)
dot1agCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepIfIndex.setStatus("current")
_Dot1agCfmMepDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmMepDirection_Object = MibTableColumn
dot1agCfmMepDirection = _Dot1agCfmMepDirection_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 3),
    _Dot1agCfmMepDirection_Type()
)
dot1agCfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDirection.setStatus("current")


class _Dot1agCfmMepPrimaryVid_Type(Unsigned32):
    """Custom type dot1agCfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_Dot1agCfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_Dot1agCfmMepPrimaryVid_Object = MibTableColumn
dot1agCfmMepPrimaryVid = _Dot1agCfmMepPrimaryVid_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 4),
    _Dot1agCfmMepPrimaryVid_Type()
)
dot1agCfmMepPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPrimaryVid.setStatus("current")


class _Dot1agCfmMepActive_Type(TruthValue):
    """Custom type dot1agCfmMepActive based on TruthValue"""


_Dot1agCfmMepActive_Object = MibTableColumn
dot1agCfmMepActive = _Dot1agCfmMepActive_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 5),
    _Dot1agCfmMepActive_Type()
)
dot1agCfmMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepActive.setStatus("current")


class _Dot1agCfmMepFngState_Type(Dot1agCfmFngState):
    """Custom type dot1agCfmMepFngState based on Dot1agCfmFngState"""


_Dot1agCfmMepFngState_Object = MibTableColumn
dot1agCfmMepFngState = _Dot1agCfmMepFngState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 6),
    _Dot1agCfmMepFngState_Type()
)
dot1agCfmMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepFngState.setStatus("current")


class _Dot1agCfmMepCciEnabled_Type(TruthValue):
    """Custom type dot1agCfmMepCciEnabled based on TruthValue"""


_Dot1agCfmMepCciEnabled_Object = MibTableColumn
dot1agCfmMepCciEnabled = _Dot1agCfmMepCciEnabled_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 7),
    _Dot1agCfmMepCciEnabled_Type()
)
dot1agCfmMepCciEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCciEnabled.setStatus("current")


class _Dot1agCfmMepCcmLtmPriority_Type(Unsigned32):
    """Custom type dot1agCfmMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agCfmMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_Dot1agCfmMepCcmLtmPriority_Object = MibTableColumn
dot1agCfmMepCcmLtmPriority = _Dot1agCfmMepCcmLtmPriority_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 8),
    _Dot1agCfmMepCcmLtmPriority_Type()
)
dot1agCfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCcmLtmPriority.setStatus("current")
_Dot1agCfmMepMacAddress_Type = MacAddress
_Dot1agCfmMepMacAddress_Object = MibTableColumn
dot1agCfmMepMacAddress = _Dot1agCfmMepMacAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 9),
    _Dot1agCfmMepMacAddress_Type()
)
dot1agCfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepMacAddress.setStatus("current")


class _Dot1agCfmMepFaultAlarmDestDomain_Type(TransportDomain):
    """Custom type dot1agCfmMepFaultAlarmDestDomain based on TransportDomain"""
    defaultValue = (0, 0)


_Dot1agCfmMepFaultAlarmDestDomain_Object = MibTableColumn
dot1agCfmMepFaultAlarmDestDomain = _Dot1agCfmMepFaultAlarmDestDomain_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 10),
    _Dot1agCfmMepFaultAlarmDestDomain_Type()
)
dot1agCfmMepFaultAlarmDestDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFaultAlarmDestDomain.setStatus("current")
_Dot1agCfmMepFaulAlarmDestAddress_Type = TransportAddress
_Dot1agCfmMepFaulAlarmDestAddress_Object = MibTableColumn
dot1agCfmMepFaulAlarmDestAddress = _Dot1agCfmMepFaulAlarmDestAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 11),
    _Dot1agCfmMepFaulAlarmDestAddress_Type()
)
dot1agCfmMepFaulAlarmDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFaulAlarmDestAddress.setStatus("current")


class _Dot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type dot1agCfmMepLowPrDef based on Dot1agCfmLowestAlarmPri"""


_Dot1agCfmMepLowPrDef_Object = MibTableColumn
dot1agCfmMepLowPrDef = _Dot1agCfmMepLowPrDef_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 12),
    _Dot1agCfmMepLowPrDef_Type()
)
dot1agCfmMepLowPrDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepLowPrDef.setStatus("current")


class _Dot1agCfmMepFngAlarmTime_Type(TimeInterval):
    """Custom type dot1agCfmMepFngAlarmTime based on TimeInterval"""
    defaultValue = 250

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_Dot1agCfmMepFngAlarmTime_Type.__name__ = "TimeInterval"
_Dot1agCfmMepFngAlarmTime_Object = MibTableColumn
dot1agCfmMepFngAlarmTime = _Dot1agCfmMepFngAlarmTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 13),
    _Dot1agCfmMepFngAlarmTime_Type()
)
dot1agCfmMepFngAlarmTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFngAlarmTime.setStatus("current")


class _Dot1agCfmMepFngResetTime_Type(TimeInterval):
    """Custom type dot1agCfmMepFngResetTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_Dot1agCfmMepFngResetTime_Type.__name__ = "TimeInterval"
_Dot1agCfmMepFngResetTime_Object = MibTableColumn
dot1agCfmMepFngResetTime = _Dot1agCfmMepFngResetTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 14),
    _Dot1agCfmMepFngResetTime_Type()
)
dot1agCfmMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFngResetTime.setStatus("current")
_Dot1agCfmMepHighestPrDefect_Type = Dot1agCfmHighestDefectPri
_Dot1agCfmMepHighestPrDefect_Object = MibTableColumn
dot1agCfmMepHighestPrDefect = _Dot1agCfmMepHighestPrDefect_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 15),
    _Dot1agCfmMepHighestPrDefect_Type()
)
dot1agCfmMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepHighestPrDefect.setStatus("current")
_Dot1agCfmMepSomeRdiDefect_Type = TruthValue
_Dot1agCfmMepSomeRdiDefect_Object = MibTableColumn
dot1agCfmMepSomeRdiDefect = _Dot1agCfmMepSomeRdiDefect_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 16),
    _Dot1agCfmMepSomeRdiDefect_Type()
)
dot1agCfmMepSomeRdiDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepSomeRdiDefect.setStatus("current")
_Dot1agCfmMepErrMacStatus_Type = TruthValue
_Dot1agCfmMepErrMacStatus_Object = MibTableColumn
dot1agCfmMepErrMacStatus = _Dot1agCfmMepErrMacStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 17),
    _Dot1agCfmMepErrMacStatus_Type()
)
dot1agCfmMepErrMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepErrMacStatus.setStatus("current")
_Dot1agCfmMepSomeRMepCcmDefect_Type = TruthValue
_Dot1agCfmMepSomeRMepCcmDefect_Object = MibTableColumn
dot1agCfmMepSomeRMepCcmDefect = _Dot1agCfmMepSomeRMepCcmDefect_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 18),
    _Dot1agCfmMepSomeRMepCcmDefect_Type()
)
dot1agCfmMepSomeRMepCcmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepSomeRMepCcmDefect.setStatus("current")
_Dot1agCfmMepErrorCcmDefect_Type = TruthValue
_Dot1agCfmMepErrorCcmDefect_Object = MibTableColumn
dot1agCfmMepErrorCcmDefect = _Dot1agCfmMepErrorCcmDefect_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 19),
    _Dot1agCfmMepErrorCcmDefect_Type()
)
dot1agCfmMepErrorCcmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepErrorCcmDefect.setStatus("current")
_Dot1agCfmMepXconCcmDefect_Type = TruthValue
_Dot1agCfmMepXconCcmDefect_Object = MibTableColumn
dot1agCfmMepXconCcmDefect = _Dot1agCfmMepXconCcmDefect_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 20),
    _Dot1agCfmMepXconCcmDefect_Type()
)
dot1agCfmMepXconCcmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepXconCcmDefect.setStatus("current")


class _Dot1agCfmMepErrorCcmLastFailure_Type(OctetString):
    """Custom type dot1agCfmMepErrorCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_Dot1agCfmMepErrorCcmLastFailure_Type.__name__ = "OctetString"
_Dot1agCfmMepErrorCcmLastFailure_Object = MibTableColumn
dot1agCfmMepErrorCcmLastFailure = _Dot1agCfmMepErrorCcmLastFailure_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 21),
    _Dot1agCfmMepErrorCcmLastFailure_Type()
)
dot1agCfmMepErrorCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepErrorCcmLastFailure.setStatus("current")


class _Dot1agCfmMepXconCcmLastFailure_Type(OctetString):
    """Custom type dot1agCfmMepXconCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_Dot1agCfmMepXconCcmLastFailure_Type.__name__ = "OctetString"
_Dot1agCfmMepXconCcmLastFailure_Object = MibTableColumn
dot1agCfmMepXconCcmLastFailure = _Dot1agCfmMepXconCcmLastFailure_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 22),
    _Dot1agCfmMepXconCcmLastFailure_Type()
)
dot1agCfmMepXconCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepXconCcmLastFailure.setStatus("current")
_Dot1agCfmMepRCcmSequenceErrors_Type = Counter32
_Dot1agCfmMepRCcmSequenceErrors_Object = MibTableColumn
dot1agCfmMepRCcmSequenceErrors = _Dot1agCfmMepRCcmSequenceErrors_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 23),
    _Dot1agCfmMepRCcmSequenceErrors_Type()
)
dot1agCfmMepRCcmSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepRCcmSequenceErrors.setStatus("current")
_Dot1agCfmMepCciSentCcms_Type = Counter32
_Dot1agCfmMepCciSentCcms_Object = MibTableColumn
dot1agCfmMepCciSentCcms = _Dot1agCfmMepCciSentCcms_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 24),
    _Dot1agCfmMepCciSentCcms_Type()
)
dot1agCfmMepCciSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCciSentCcms.setStatus("current")
_Dot1agCfmMepNextLbmTransId_Type = Unsigned32
_Dot1agCfmMepNextLbmTransId_Object = MibTableColumn
dot1agCfmMepNextLbmTransId = _Dot1agCfmMepNextLbmTransId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 25),
    _Dot1agCfmMepNextLbmTransId_Type()
)
dot1agCfmMepNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepNextLbmTransId.setStatus("current")
_Dot1agCfmMepLbrIn_Type = Counter32
_Dot1agCfmMepLbrIn_Object = MibTableColumn
dot1agCfmMepLbrIn = _Dot1agCfmMepLbrIn_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 26),
    _Dot1agCfmMepLbrIn_Type()
)
dot1agCfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrIn.setStatus("current")
_Dot1agCfmMepLbrInOutOfOrder_Type = Counter32
_Dot1agCfmMepLbrInOutOfOrder_Object = MibTableColumn
dot1agCfmMepLbrInOutOfOrder = _Dot1agCfmMepLbrInOutOfOrder_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 27),
    _Dot1agCfmMepLbrInOutOfOrder_Type()
)
dot1agCfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrInOutOfOrder.setStatus("current")
_Dot1agCfmMepLbrBadMsdu_Type = Counter32
_Dot1agCfmMepLbrBadMsdu_Object = MibTableColumn
dot1agCfmMepLbrBadMsdu = _Dot1agCfmMepLbrBadMsdu_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 28),
    _Dot1agCfmMepLbrBadMsdu_Type()
)
dot1agCfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrBadMsdu.setStatus("current")
_Dot1agCfmMepLtmNextSeqNumber_Type = Unsigned32
_Dot1agCfmMepLtmNextSeqNumber_Object = MibTableColumn
dot1agCfmMepLtmNextSeqNumber = _Dot1agCfmMepLtmNextSeqNumber_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 29),
    _Dot1agCfmMepLtmNextSeqNumber_Type()
)
dot1agCfmMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLtmNextSeqNumber.setStatus("current")
_Dot1agCfmMepUnexpLtrIn_Type = Counter32
_Dot1agCfmMepUnexpLtrIn_Object = MibTableColumn
dot1agCfmMepUnexpLtrIn = _Dot1agCfmMepUnexpLtrIn_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 30),
    _Dot1agCfmMepUnexpLtrIn_Type()
)
dot1agCfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepUnexpLtrIn.setStatus("current")
_Dot1agCfmMepLbrOut_Type = Counter32
_Dot1agCfmMepLbrOut_Object = MibTableColumn
dot1agCfmMepLbrOut = _Dot1agCfmMepLbrOut_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 31),
    _Dot1agCfmMepLbrOut_Type()
)
dot1agCfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrOut.setStatus("current")


class _Dot1agCfmMepTransmitLbmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmStatus based on TruthValue"""


_Dot1agCfmMepTransmitLbmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLbmStatus = _Dot1agCfmMepTransmitLbmStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 32),
    _Dot1agCfmMepTransmitLbmStatus_Type()
)
dot1agCfmMepTransmitLbmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmStatus.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLbmDestMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMacAddress = _Dot1agCfmMepTransmitLbmDestMacAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 33),
    _Dot1agCfmMepTransmitLbmDestMacAddress_Type()
)
dot1agCfmMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmMepTransmitLbmDestMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMepId = _Dot1agCfmMepTransmitLbmDestMepId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 34),
    _Dot1agCfmMepTransmitLbmDestMepId_Type()
)
dot1agCfmMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMepId.setStatus("current")
_Dot1agCfmMepTransmitLbmDestIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLbmDestIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestIsMepId = _Dot1agCfmMepTransmitLbmDestIsMepId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 35),
    _Dot1agCfmMepTransmitLbmDestIsMepId_Type()
)
dot1agCfmMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestIsMepId.setStatus("current")


class _Dot1agCfmMepTransmitLbmMessages_Type(Integer32):
    """Custom type dot1agCfmMepTransmitLbmMessages based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Dot1agCfmMepTransmitLbmMessages_Type.__name__ = "Integer32"
_Dot1agCfmMepTransmitLbmMessages_Object = MibTableColumn
dot1agCfmMepTransmitLbmMessages = _Dot1agCfmMepTransmitLbmMessages_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 36),
    _Dot1agCfmMepTransmitLbmMessages_Type()
)
dot1agCfmMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmMessages.setStatus("current")


class _Dot1agCfmMepTransmitLbmDataTlv_Type(OctetString):
    """Custom type dot1agCfmMepTransmitLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_Dot1agCfmMepTransmitLbmDataTlv_Type.__name__ = "OctetString"
_Dot1agCfmMepTransmitLbmDataTlv_Object = MibTableColumn
dot1agCfmMepTransmitLbmDataTlv = _Dot1agCfmMepTransmitLbmDataTlv_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 37),
    _Dot1agCfmMepTransmitLbmDataTlv_Type()
)
dot1agCfmMepTransmitLbmDataTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDataTlv.setStatus("current")


class _Dot1agCfmMepTransmitLbmVlanPriority_Type(Integer32):
    """Custom type dot1agCfmMepTransmitLbmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agCfmMepTransmitLbmVlanPriority_Type.__name__ = "Integer32"
_Dot1agCfmMepTransmitLbmVlanPriority_Object = MibTableColumn
dot1agCfmMepTransmitLbmVlanPriority = _Dot1agCfmMepTransmitLbmVlanPriority_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 38),
    _Dot1agCfmMepTransmitLbmVlanPriority_Type()
)
dot1agCfmMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanPriority.setStatus("current")


class _Dot1agCfmMepTransmitLbmVlanDropEnable_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmVlanDropEnable based on TruthValue"""


_Dot1agCfmMepTransmitLbmVlanDropEnable_Object = MibTableColumn
dot1agCfmMepTransmitLbmVlanDropEnable = _Dot1agCfmMepTransmitLbmVlanDropEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 39),
    _Dot1agCfmMepTransmitLbmVlanDropEnable_Type()
)
dot1agCfmMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanDropEnable.setStatus("current")


class _Dot1agCfmMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmResultOK based on TruthValue"""


_Dot1agCfmMepTransmitLbmResultOK_Object = MibTableColumn
dot1agCfmMepTransmitLbmResultOK = _Dot1agCfmMepTransmitLbmResultOK_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 40),
    _Dot1agCfmMepTransmitLbmResultOK_Type()
)
dot1agCfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmResultOK.setStatus("current")
_Dot1agCfmMepTransmitLbmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLbmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLbmSeqNumber = _Dot1agCfmMepTransmitLbmSeqNumber_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 41),
    _Dot1agCfmMepTransmitLbmSeqNumber_Type()
)
dot1agCfmMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmSeqNumber.setStatus("current")


class _Dot1agCfmMepTransmitLtmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmStatus based on TruthValue"""


_Dot1agCfmMepTransmitLtmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLtmStatus = _Dot1agCfmMepTransmitLtmStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 42),
    _Dot1agCfmMepTransmitLtmStatus_Type()
)
dot1agCfmMepTransmitLtmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmStatus.setStatus("current")


class _Dot1agCfmMepTransmitLtmFlags_Type(Bits):
    """Custom type dot1agCfmMepTransmitLtmFlags based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_Dot1agCfmMepTransmitLtmFlags_Type.__name__ = "Bits"
_Dot1agCfmMepTransmitLtmFlags_Object = MibTableColumn
dot1agCfmMepTransmitLtmFlags = _Dot1agCfmMepTransmitLtmFlags_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 43),
    _Dot1agCfmMepTransmitLtmFlags_Type()
)
dot1agCfmMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmFlags.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLtmTargetMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMacAddress = _Dot1agCfmMepTransmitLtmTargetMacAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 44),
    _Dot1agCfmMepTransmitLtmTargetMacAddress_Type()
)
dot1agCfmMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmMepTransmitLtmTargetMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMepId = _Dot1agCfmMepTransmitLtmTargetMepId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 45),
    _Dot1agCfmMepTransmitLtmTargetMepId_Type()
)
dot1agCfmMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMepId.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLtmTargetIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetIsMepId = _Dot1agCfmMepTransmitLtmTargetIsMepId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 46),
    _Dot1agCfmMepTransmitLtmTargetIsMepId_Type()
)
dot1agCfmMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetIsMepId.setStatus("current")


class _Dot1agCfmMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type dot1agCfmMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1agCfmMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_Dot1agCfmMepTransmitLtmTtl_Object = MibTableColumn
dot1agCfmMepTransmitLtmTtl = _Dot1agCfmMepTransmitLtmTtl_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 47),
    _Dot1agCfmMepTransmitLtmTtl_Type()
)
dot1agCfmMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTtl.setStatus("current")


class _Dot1agCfmMepTransmitLtmResult_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmResult based on TruthValue"""


_Dot1agCfmMepTransmitLtmResult_Object = MibTableColumn
dot1agCfmMepTransmitLtmResult = _Dot1agCfmMepTransmitLtmResult_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 48),
    _Dot1agCfmMepTransmitLtmResult_Type()
)
dot1agCfmMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmResult.setStatus("current")
_Dot1agCfmMepTransmitLtmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLtmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLtmSeqNumber = _Dot1agCfmMepTransmitLtmSeqNumber_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 49),
    _Dot1agCfmMepTransmitLtmSeqNumber_Type()
)
dot1agCfmMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmSeqNumber.setStatus("current")


class _Dot1agCfmMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dot1agCfmMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmMepTransmitLtmEgressIdentifier_Object = MibTableColumn
dot1agCfmMepTransmitLtmEgressIdentifier = _Dot1agCfmMepTransmitLtmEgressIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 50),
    _Dot1agCfmMepTransmitLtmEgressIdentifier_Type()
)
dot1agCfmMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmEgressIdentifier.setStatus("current")
_Dot1agCfmMepRowStatus_Type = RowStatus
_Dot1agCfmMepRowStatus_Object = MibTableColumn
dot1agCfmMepRowStatus = _Dot1agCfmMepRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 51),
    _Dot1agCfmMepRowStatus_Type()
)
dot1agCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepRowStatus.setStatus("current")
_Dot1agCfmLtrTable_Object = MibTable
dot1agCfmLtrTable = _Dot1agCfmLtrTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmLtrTable.setStatus("current")
_Dot1agCfmLtrEntry_Object = MibTableRow
dot1agCfmLtrEntry = _Dot1agCfmLtrEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1)
)
dot1agCfmLtrEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmLtrSeqNumber"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    dot1agCfmLtrEntry.setStatus("current")


class _Dot1agCfmLtrSeqNumber_Type(Unsigned32):
    """Custom type dot1agCfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot1agCfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrSeqNumber_Object = MibTableColumn
dot1agCfmLtrSeqNumber = _Dot1agCfmLtrSeqNumber_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 1),
    _Dot1agCfmLtrSeqNumber_Type()
)
dot1agCfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrSeqNumber.setStatus("current")


class _Dot1agCfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type dot1agCfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrReceiveOrder_Object = MibTableColumn
dot1agCfmLtrReceiveOrder = _Dot1agCfmLtrReceiveOrder_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 2),
    _Dot1agCfmLtrReceiveOrder_Type()
)
dot1agCfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrReceiveOrder.setStatus("current")


class _Dot1agCfmLtrTtl_Type(Unsigned32):
    """Custom type dot1agCfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1agCfmLtrTtl_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrTtl_Object = MibTableColumn
dot1agCfmLtrTtl = _Dot1agCfmLtrTtl_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 3),
    _Dot1agCfmLtrTtl_Type()
)
dot1agCfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTtl.setStatus("current")
_Dot1agCfmLtrForwarded_Type = TruthValue
_Dot1agCfmLtrForwarded_Object = MibTableColumn
dot1agCfmLtrForwarded = _Dot1agCfmLtrForwarded_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 4),
    _Dot1agCfmLtrForwarded_Type()
)
dot1agCfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrForwarded.setStatus("current")
_Dot1agCfmLtrTerminalMep_Type = TruthValue
_Dot1agCfmLtrTerminalMep_Object = MibTableColumn
dot1agCfmLtrTerminalMep = _Dot1agCfmLtrTerminalMep_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 5),
    _Dot1agCfmLtrTerminalMep_Type()
)
dot1agCfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTerminalMep.setStatus("current")


class _Dot1agCfmLtrLastEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dot1agCfmLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrLastEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrLastEgressIdentifier = _Dot1agCfmLtrLastEgressIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 6),
    _Dot1agCfmLtrLastEgressIdentifier_Type()
)
dot1agCfmLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrLastEgressIdentifier.setStatus("current")


class _Dot1agCfmLtrNextEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dot1agCfmLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrNextEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrNextEgressIdentifier = _Dot1agCfmLtrNextEgressIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 7),
    _Dot1agCfmLtrNextEgressIdentifier_Type()
)
dot1agCfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrNextEgressIdentifier.setStatus("current")
_Dot1agCfmLtrRelay_Type = Dot1agCfmRelayActionFieldValue
_Dot1agCfmLtrRelay_Object = MibTableColumn
dot1agCfmLtrRelay = _Dot1agCfmLtrRelay_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 8),
    _Dot1agCfmLtrRelay_Type()
)
dot1agCfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrRelay.setStatus("current")
_Dot1agCfmLtrChassisIdSubtype_Type = LldpChassisIdSubtype
_Dot1agCfmLtrChassisIdSubtype_Object = MibTableColumn
dot1agCfmLtrChassisIdSubtype = _Dot1agCfmLtrChassisIdSubtype_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 9),
    _Dot1agCfmLtrChassisIdSubtype_Type()
)
dot1agCfmLtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrChassisIdSubtype.setStatus("current")
_Dot1agCfmLtrChassisId_Type = LldpChassisId
_Dot1agCfmLtrChassisId_Object = MibTableColumn
dot1agCfmLtrChassisId = _Dot1agCfmLtrChassisId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 10),
    _Dot1agCfmLtrChassisId_Type()
)
dot1agCfmLtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrChassisId.setStatus("current")
_Dot1agCfmLtrManAddressType_Type = AddressFamilyNumbers
_Dot1agCfmLtrManAddressType_Object = MibTableColumn
dot1agCfmLtrManAddressType = _Dot1agCfmLtrManAddressType_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 11),
    _Dot1agCfmLtrManAddressType_Type()
)
dot1agCfmLtrManAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrManAddressType.setStatus("current")
_Dot1agCfmLtrManAddress_Type = LldpManAddress
_Dot1agCfmLtrManAddress_Object = MibTableColumn
dot1agCfmLtrManAddress = _Dot1agCfmLtrManAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 12),
    _Dot1agCfmLtrManAddress_Type()
)
dot1agCfmLtrManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrManAddress.setStatus("current")
_Dot1agCfmLtrIngress_Type = Dot1agCfmIngressActionFieldValue
_Dot1agCfmLtrIngress_Object = MibTableColumn
dot1agCfmLtrIngress = _Dot1agCfmLtrIngress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 13),
    _Dot1agCfmLtrIngress_Type()
)
dot1agCfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngress.setStatus("current")
_Dot1agCfmLtrIngressMac_Type = MacAddress
_Dot1agCfmLtrIngressMac_Object = MibTableColumn
dot1agCfmLtrIngressMac = _Dot1agCfmLtrIngressMac_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 14),
    _Dot1agCfmLtrIngressMac_Type()
)
dot1agCfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressMac.setStatus("current")
_Dot1agCfmLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_Dot1agCfmLtrIngressPortIdSubtype_Object = MibTableColumn
dot1agCfmLtrIngressPortIdSubtype = _Dot1agCfmLtrIngressPortIdSubtype_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 15),
    _Dot1agCfmLtrIngressPortIdSubtype_Type()
)
dot1agCfmLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressPortIdSubtype.setStatus("current")
_Dot1agCfmLtrIngressPortId_Type = LldpPortId
_Dot1agCfmLtrIngressPortId_Object = MibTableColumn
dot1agCfmLtrIngressPortId = _Dot1agCfmLtrIngressPortId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 16),
    _Dot1agCfmLtrIngressPortId_Type()
)
dot1agCfmLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressPortId.setStatus("current")
_Dot1agCfmLtrEgress_Type = Dot1agCfmEgressActionFieldValue
_Dot1agCfmLtrEgress_Object = MibTableColumn
dot1agCfmLtrEgress = _Dot1agCfmLtrEgress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 17),
    _Dot1agCfmLtrEgress_Type()
)
dot1agCfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgress.setStatus("current")
_Dot1agCfmLtrEgressMac_Type = MacAddress
_Dot1agCfmLtrEgressMac_Object = MibTableColumn
dot1agCfmLtrEgressMac = _Dot1agCfmLtrEgressMac_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 18),
    _Dot1agCfmLtrEgressMac_Type()
)
dot1agCfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressMac.setStatus("current")
_Dot1agCfmLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_Dot1agCfmLtrEgressPortIdSubtype_Object = MibTableColumn
dot1agCfmLtrEgressPortIdSubtype = _Dot1agCfmLtrEgressPortIdSubtype_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 19),
    _Dot1agCfmLtrEgressPortIdSubtype_Type()
)
dot1agCfmLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressPortIdSubtype.setStatus("current")
_Dot1agCfmLtrEgressPortId_Type = LldpPortId
_Dot1agCfmLtrEgressPortId_Object = MibTableColumn
dot1agCfmLtrEgressPortId = _Dot1agCfmLtrEgressPortId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 20),
    _Dot1agCfmLtrEgressPortId_Type()
)
dot1agCfmLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressPortId.setStatus("current")


class _Dot1agCfmLtrOrganizationSpecificTlv_Type(OctetString):
    """Custom type dot1agCfmLtrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_Dot1agCfmLtrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_Dot1agCfmLtrOrganizationSpecificTlv_Object = MibTableColumn
dot1agCfmLtrOrganizationSpecificTlv = _Dot1agCfmLtrOrganizationSpecificTlv_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 21),
    _Dot1agCfmLtrOrganizationSpecificTlv_Type()
)
dot1agCfmLtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrOrganizationSpecificTlv.setStatus("current")
_Dot1agCfmMepDbTable_Object = MibTable
dot1agCfmMepDbTable = _Dot1agCfmMepDbTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbTable.setStatus("current")
_Dot1agCfmMepDbEntry_Object = MibTableRow
dot1agCfmMepDbEntry = _Dot1agCfmMepDbEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1)
)
dot1agCfmMepDbEntry.setIndexNames(
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbEntry.setStatus("current")
_Dot1agCfmMepDbRMepIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMepDbRMepIdentifier_Object = MibTableColumn
dot1agCfmMepDbRMepIdentifier = _Dot1agCfmMepDbRMepIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 1),
    _Dot1agCfmMepDbRMepIdentifier_Type()
)
dot1agCfmMepDbRMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepIdentifier.setStatus("current")
_Dot1agCfmMepDbRMepState_Type = Dot1agCfmRemoteMepState
_Dot1agCfmMepDbRMepState_Object = MibTableColumn
dot1agCfmMepDbRMepState = _Dot1agCfmMepDbRMepState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 2),
    _Dot1agCfmMepDbRMepState_Type()
)
dot1agCfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepState.setStatus("current")
_Dot1agCfmMepDbRMepFailedOkTime_Type = TimeStamp
_Dot1agCfmMepDbRMepFailedOkTime_Object = MibTableColumn
dot1agCfmMepDbRMepFailedOkTime = _Dot1agCfmMepDbRMepFailedOkTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 3),
    _Dot1agCfmMepDbRMepFailedOkTime_Type()
)
dot1agCfmMepDbRMepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepFailedOkTime.setStatus("current")
_Dot1agCfmMepDbMacAddress_Type = MacAddress
_Dot1agCfmMepDbMacAddress_Object = MibTableColumn
dot1agCfmMepDbMacAddress = _Dot1agCfmMepDbMacAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 4),
    _Dot1agCfmMepDbMacAddress_Type()
)
dot1agCfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbMacAddress.setStatus("current")
_Dot1agCfmMepDbRdi_Type = TruthValue
_Dot1agCfmMepDbRdi_Object = MibTableColumn
dot1agCfmMepDbRdi = _Dot1agCfmMepDbRdi_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 5),
    _Dot1agCfmMepDbRdi_Type()
)
dot1agCfmMepDbRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRdi.setStatus("current")


class _Dot1agCfmMepDbPortStatusTlv_Type(Dot1agCfmPortStatus):
    """Custom type dot1agCfmMepDbPortStatusTlv based on Dot1agCfmPortStatus"""


_Dot1agCfmMepDbPortStatusTlv_Object = MibTableColumn
dot1agCfmMepDbPortStatusTlv = _Dot1agCfmMepDbPortStatusTlv_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 6),
    _Dot1agCfmMepDbPortStatusTlv_Type()
)
dot1agCfmMepDbPortStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbPortStatusTlv.setStatus("current")


class _Dot1agCfmMepDbInterfaceStatusTlv_Type(Dot1agCfmInterfaceStatus):
    """Custom type dot1agCfmMepDbInterfaceStatusTlv based on Dot1agCfmInterfaceStatus"""


_Dot1agCfmMepDbInterfaceStatusTlv_Object = MibTableColumn
dot1agCfmMepDbInterfaceStatusTlv = _Dot1agCfmMepDbInterfaceStatusTlv_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 7),
    _Dot1agCfmMepDbInterfaceStatusTlv_Type()
)
dot1agCfmMepDbInterfaceStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbInterfaceStatusTlv.setStatus("current")
_Dot1agCfmMepDbChassisIdSubtype_Type = LldpChassisIdSubtype
_Dot1agCfmMepDbChassisIdSubtype_Object = MibTableColumn
dot1agCfmMepDbChassisIdSubtype = _Dot1agCfmMepDbChassisIdSubtype_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 8),
    _Dot1agCfmMepDbChassisIdSubtype_Type()
)
dot1agCfmMepDbChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbChassisIdSubtype.setStatus("current")
_Dot1agCfmMepDbChassisId_Type = LldpChassisId
_Dot1agCfmMepDbChassisId_Object = MibTableColumn
dot1agCfmMepDbChassisId = _Dot1agCfmMepDbChassisId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 9),
    _Dot1agCfmMepDbChassisId_Type()
)
dot1agCfmMepDbChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbChassisId.setStatus("current")
_Dot1agCfmMepDbManAddressType_Type = AddressFamilyNumbers
_Dot1agCfmMepDbManAddressType_Object = MibTableColumn
dot1agCfmMepDbManAddressType = _Dot1agCfmMepDbManAddressType_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 10),
    _Dot1agCfmMepDbManAddressType_Type()
)
dot1agCfmMepDbManAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbManAddressType.setStatus("current")
_Dot1agCfmMepDbManAddress_Type = LldpManAddress
_Dot1agCfmMepDbManAddress_Object = MibTableColumn
dot1agCfmMepDbManAddress = _Dot1agCfmMepDbManAddress_Object(
    (1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 11),
    _Dot1agCfmMepDbManAddress_Type()
)
dot1agCfmMepDbManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbManAddress.setStatus("current")
_Dot1agCfmConformance_ObjectIdentity = ObjectIdentity
dot1agCfmConformance = _Dot1agCfmConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2)
)
_Dot1agCfmCompliances_ObjectIdentity = ObjectIdentity
dot1agCfmCompliances = _Dot1agCfmCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2, 1)
)
_Dot1agCfmGroups_ObjectIdentity = ObjectIdentity
dot1agCfmGroups = _Dot1agCfmGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2, 2)
)

# Managed Objects groups

dot1agCfmStackGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 1)
)
dot1agCfmStackGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmStackMepId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmStackMacAddress"))
)
if mibBuilder.loadTexts:
    dot1agCfmStackGroup.setStatus("current")

dot1agCfmDefaultMdLevelGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 2)
)
dot1agCfmDefaultMdLevelGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelMhfCreation"),
        ("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelLevel"),
        ("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelVid"))
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevelGroup.setStatus("current")

dot1agCfmConfigErrorListGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 3)
)
dot1agCfmConfigErrorListGroup.setObjects(
    ("IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListGroup.setStatus("current")

dot1agCfmMdGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 4)
)
dot1agCfmMdGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmMdTableNextIndex"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdLevel"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdMhfCreation"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdFaultAlarmDestDomain"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdFaulAlarmDestAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMdRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmMdGroup.setStatus("current")

dot1agCfmMaGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 5)
)
dot1agCfmMaGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmMaTableNextIndex"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaName"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaFormat"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaMhfCreation"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaCcmInterval"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaRowStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaVlanRowStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaFaultAlarmDestDomain"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaFaulAlarmDestAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaMoreThanOneVid"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmMaGroup.setStatus("current")

dot1agCfmMepGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 6)
)
dot1agCfmMepGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepPrimaryVid"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepActive"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepFngState"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepCciEnabled"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepCcmLtmPriority"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepMacAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepFaultAlarmDestDomain"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepFaulAlarmDestAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLowPrDef"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepFngAlarmTime"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepFngResetTime"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepHighestPrDefect"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepSomeRdiDefect"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepErrMacStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepSomeRMepCcmDefect"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepErrorCcmDefect"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepXconCcmDefect"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepErrorCcmLastFailure"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepXconCcmLastFailure"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepRCcmSequenceErrors"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepCciSentCcms"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepNextLbmTransId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrIn"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrInOutOfOrder"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrBadMsdu"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLtmNextSeqNumber"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepUnexpLtrIn"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrOut"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestMepId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestIsMepId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmMessages"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDataTlv"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmVlanPriority"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmVlanDropEnable"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmResultOK"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmSeqNumber"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmFlags"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMacAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMepId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetIsMepId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTtl"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmResult"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmEgressIdentifier"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepRowStatus"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrForwarded"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrRelay"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrChassisIdSubtype"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrChassisId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrManAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrManAddressType"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressMac"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressPortIdSubtype"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressPortId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressMac"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressPortIdSubtype"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressPortId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrTerminalMep"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrLastEgressIdentifier"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrNextEgressIdentifier"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrTtl"),
        ("IEEE802171-CFM-MIB", "dot1agCfmLtrOrganizationSpecificTlv"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepGroup.setStatus("current")

dot1agCfmMepDbGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 7)
)
dot1agCfmMepDbGroup.setObjects(
      *(("IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepState"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepFailedOkTime"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbMacAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbRdi"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbPortStatusTlv"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbInterfaceStatusTlv"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbChassisIdSubtype"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbChassisId"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbManAddress"),
        ("IEEE802171-CFM-MIB", "dot1agCfmMepDbManAddressType"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbGroup.setStatus("current")


# Notification objects

dot1agCfmFaultAlarm = NotificationType(
    (1, 0, 8802, 1, 1, 3, 0, 1)
)
dot1agCfmFaultAlarm.setObjects(
    ("IEEE802171-CFM-MIB", "dot1agCfmMepHighestPrDefect")
)
if mibBuilder.loadTexts:
    dot1agCfmFaultAlarm.setStatus(
        "current"
    )


# Notifications groups

dot1agCfmNotificationsGroup = NotificationGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 8)
)
dot1agCfmNotificationsGroup.setObjects(
    ("IEEE802171-CFM-MIB", "dot1agCfmFaultAlarm")
)
if mibBuilder.loadTexts:
    dot1agCfmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot1agCfmCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE802171-CFM-MIB",
    **{"Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMaintenanceDomainLevel": Dot1agCfmMaintenanceDomainLevel,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmPortStatus": Dot1agCfmPortStatus,
       "Dot1agCfmInterfaceStatus": Dot1agCfmInterfaceStatus,
       "Dot1agCfmHighestDefectPri": Dot1agCfmHighestDefectPri,
       "Dot1agCfmLowestAlarmPri": Dot1agCfmLowestAlarmPri,
       "Dot1agCfmMepId": Dot1agCfmMepId,
       "Dot1agCfmMepIdOrZero": Dot1agCfmMepIdOrZero,
       "Dot1agCfmMhfCreation": Dot1agCfmMhfCreation,
       "Dot1agCfmCcmInterval": Dot1agCfmCcmInterval,
       "Dot1agCfmFngState": Dot1agCfmFngState,
       "Dot1agCfmRelayActionFieldValue": Dot1agCfmRelayActionFieldValue,
       "Dot1agCfmIngressActionFieldValue": Dot1agCfmIngressActionFieldValue,
       "Dot1agCfmEgressActionFieldValue": Dot1agCfmEgressActionFieldValue,
       "Dot1agCfmRemoteMepState": Dot1agCfmRemoteMepState,
       "Dot1afCfmIndexIntegerNextFree": Dot1afCfmIndexIntegerNextFree,
       "Dot1agCfmConfigErrors": Dot1agCfmConfigErrors,
       "ieee8021cfmMIB": ieee8021cfmMIB,
       "dot1agNotifications": dot1agNotifications,
       "dot1agCfmFaultAlarm": dot1agCfmFaultAlarm,
       "dot1agMIBObjects": dot1agMIBObjects,
       "dot1agCfmStack": dot1agCfmStack,
       "dot1agCfmStackTable": dot1agCfmStackTable,
       "dot1agCfmStackEntry": dot1agCfmStackEntry,
       "dot1agCfmStackifIndex": dot1agCfmStackifIndex,
       "dot1agCfmStackDirection": dot1agCfmStackDirection,
       "dot1agCfmStackMepId": dot1agCfmStackMepId,
       "dot1agCfmStackMacAddress": dot1agCfmStackMacAddress,
       "dot1agCfmDefaultMdLevel": dot1agCfmDefaultMdLevel,
       "dot1agCfmDefaultMdLevelTable": dot1agCfmDefaultMdLevelTable,
       "dot1agCfmDefaultMdLevelEntry": dot1agCfmDefaultMdLevelEntry,
       "dot1agCfmDefaultMdLevelIndex": dot1agCfmDefaultMdLevelIndex,
       "dot1agCfmDefaultMdLevelVid": dot1agCfmDefaultMdLevelVid,
       "dot1agCfmDefaultMdLevelMhfCreation": dot1agCfmDefaultMdLevelMhfCreation,
       "dot1agCfmDefaultMdLevelLevel": dot1agCfmDefaultMdLevelLevel,
       "dot1agCfmConfigErrorList": dot1agCfmConfigErrorList,
       "dot1agCfmConfigErrorListTable": dot1agCfmConfigErrorListTable,
       "dot1agCfmConfigErrorListEntry": dot1agCfmConfigErrorListEntry,
       "dot1agCfmConfigErrorListVid": dot1agCfmConfigErrorListVid,
       "dot1agCfmConfigErrorListIfIndex": dot1agCfmConfigErrorListIfIndex,
       "dot1agCfmConfigErrorListErrorType": dot1agCfmConfigErrorListErrorType,
       "dot1agCfmMd": dot1agCfmMd,
       "dot1agCfmMdTableNextIndex": dot1agCfmMdTableNextIndex,
       "dot1agCfmMdTable": dot1agCfmMdTable,
       "dot1agCfmMdEntry": dot1agCfmMdEntry,
       "dot1agCfmMdIndex": dot1agCfmMdIndex,
       "dot1agCfmMdFormat": dot1agCfmMdFormat,
       "dot1agCfmMdName": dot1agCfmMdName,
       "dot1agCfmMdLevel": dot1agCfmMdLevel,
       "dot1agCfmMdMhfCreation": dot1agCfmMdMhfCreation,
       "dot1agCfmMdFaultAlarmDestDomain": dot1agCfmMdFaultAlarmDestDomain,
       "dot1agCfmMdFaulAlarmDestAddress": dot1agCfmMdFaulAlarmDestAddress,
       "dot1agCfmMdRowStatus": dot1agCfmMdRowStatus,
       "dot1agCfmMa": dot1agCfmMa,
       "dot1agCfmMaTableNextIndex": dot1agCfmMaTableNextIndex,
       "dot1agCfmMaTable": dot1agCfmMaTable,
       "dot1agCfmMaEntry": dot1agCfmMaEntry,
       "dot1agCfmMaIndex": dot1agCfmMaIndex,
       "dot1agCfmMaFormat": dot1agCfmMaFormat,
       "dot1agCfmMaName": dot1agCfmMaName,
       "dot1agCfmMaMhfCreation": dot1agCfmMaMhfCreation,
       "dot1agCfmMaCcmInterval": dot1agCfmMaCcmInterval,
       "dot1agCfmMaFaultAlarmDestDomain": dot1agCfmMaFaultAlarmDestDomain,
       "dot1agCfmMaFaulAlarmDestAddress": dot1agCfmMaFaulAlarmDestAddress,
       "dot1agCfmMaMoreThanOneVid": dot1agCfmMaMoreThanOneVid,
       "dot1agCfmMaRowStatus": dot1agCfmMaRowStatus,
       "dot1agCfmMaVlanTable": dot1agCfmMaVlanTable,
       "dot1agCfmMaVlanEntry": dot1agCfmMaVlanEntry,
       "dot1agCfmMaVlanVid": dot1agCfmMaVlanVid,
       "dot1agCfmMaVlanRowStatus": dot1agCfmMaVlanRowStatus,
       "dot1agCfmMaMepListTable": dot1agCfmMaMepListTable,
       "dot1agCfmMaMepListEntry": dot1agCfmMaMepListEntry,
       "dot1agCfmMaMepListIdentifier": dot1agCfmMaMepListIdentifier,
       "dot1agCfmMaMepListRowStatus": dot1agCfmMaMepListRowStatus,
       "dot1agCfmMep": dot1agCfmMep,
       "dot1agCfmMepTable": dot1agCfmMepTable,
       "dot1agCfmMepEntry": dot1agCfmMepEntry,
       "dot1agCfmMepIdentifier": dot1agCfmMepIdentifier,
       "dot1agCfmMepIfIndex": dot1agCfmMepIfIndex,
       "dot1agCfmMepDirection": dot1agCfmMepDirection,
       "dot1agCfmMepPrimaryVid": dot1agCfmMepPrimaryVid,
       "dot1agCfmMepActive": dot1agCfmMepActive,
       "dot1agCfmMepFngState": dot1agCfmMepFngState,
       "dot1agCfmMepCciEnabled": dot1agCfmMepCciEnabled,
       "dot1agCfmMepCcmLtmPriority": dot1agCfmMepCcmLtmPriority,
       "dot1agCfmMepMacAddress": dot1agCfmMepMacAddress,
       "dot1agCfmMepFaultAlarmDestDomain": dot1agCfmMepFaultAlarmDestDomain,
       "dot1agCfmMepFaulAlarmDestAddress": dot1agCfmMepFaulAlarmDestAddress,
       "dot1agCfmMepLowPrDef": dot1agCfmMepLowPrDef,
       "dot1agCfmMepFngAlarmTime": dot1agCfmMepFngAlarmTime,
       "dot1agCfmMepFngResetTime": dot1agCfmMepFngResetTime,
       "dot1agCfmMepHighestPrDefect": dot1agCfmMepHighestPrDefect,
       "dot1agCfmMepSomeRdiDefect": dot1agCfmMepSomeRdiDefect,
       "dot1agCfmMepErrMacStatus": dot1agCfmMepErrMacStatus,
       "dot1agCfmMepSomeRMepCcmDefect": dot1agCfmMepSomeRMepCcmDefect,
       "dot1agCfmMepErrorCcmDefect": dot1agCfmMepErrorCcmDefect,
       "dot1agCfmMepXconCcmDefect": dot1agCfmMepXconCcmDefect,
       "dot1agCfmMepErrorCcmLastFailure": dot1agCfmMepErrorCcmLastFailure,
       "dot1agCfmMepXconCcmLastFailure": dot1agCfmMepXconCcmLastFailure,
       "dot1agCfmMepRCcmSequenceErrors": dot1agCfmMepRCcmSequenceErrors,
       "dot1agCfmMepCciSentCcms": dot1agCfmMepCciSentCcms,
       "dot1agCfmMepNextLbmTransId": dot1agCfmMepNextLbmTransId,
       "dot1agCfmMepLbrIn": dot1agCfmMepLbrIn,
       "dot1agCfmMepLbrInOutOfOrder": dot1agCfmMepLbrInOutOfOrder,
       "dot1agCfmMepLbrBadMsdu": dot1agCfmMepLbrBadMsdu,
       "dot1agCfmMepLtmNextSeqNumber": dot1agCfmMepLtmNextSeqNumber,
       "dot1agCfmMepUnexpLtrIn": dot1agCfmMepUnexpLtrIn,
       "dot1agCfmMepLbrOut": dot1agCfmMepLbrOut,
       "dot1agCfmMepTransmitLbmStatus": dot1agCfmMepTransmitLbmStatus,
       "dot1agCfmMepTransmitLbmDestMacAddress": dot1agCfmMepTransmitLbmDestMacAddress,
       "dot1agCfmMepTransmitLbmDestMepId": dot1agCfmMepTransmitLbmDestMepId,
       "dot1agCfmMepTransmitLbmDestIsMepId": dot1agCfmMepTransmitLbmDestIsMepId,
       "dot1agCfmMepTransmitLbmMessages": dot1agCfmMepTransmitLbmMessages,
       "dot1agCfmMepTransmitLbmDataTlv": dot1agCfmMepTransmitLbmDataTlv,
       "dot1agCfmMepTransmitLbmVlanPriority": dot1agCfmMepTransmitLbmVlanPriority,
       "dot1agCfmMepTransmitLbmVlanDropEnable": dot1agCfmMepTransmitLbmVlanDropEnable,
       "dot1agCfmMepTransmitLbmResultOK": dot1agCfmMepTransmitLbmResultOK,
       "dot1agCfmMepTransmitLbmSeqNumber": dot1agCfmMepTransmitLbmSeqNumber,
       "dot1agCfmMepTransmitLtmStatus": dot1agCfmMepTransmitLtmStatus,
       "dot1agCfmMepTransmitLtmFlags": dot1agCfmMepTransmitLtmFlags,
       "dot1agCfmMepTransmitLtmTargetMacAddress": dot1agCfmMepTransmitLtmTargetMacAddress,
       "dot1agCfmMepTransmitLtmTargetMepId": dot1agCfmMepTransmitLtmTargetMepId,
       "dot1agCfmMepTransmitLtmTargetIsMepId": dot1agCfmMepTransmitLtmTargetIsMepId,
       "dot1agCfmMepTransmitLtmTtl": dot1agCfmMepTransmitLtmTtl,
       "dot1agCfmMepTransmitLtmResult": dot1agCfmMepTransmitLtmResult,
       "dot1agCfmMepTransmitLtmSeqNumber": dot1agCfmMepTransmitLtmSeqNumber,
       "dot1agCfmMepTransmitLtmEgressIdentifier": dot1agCfmMepTransmitLtmEgressIdentifier,
       "dot1agCfmMepRowStatus": dot1agCfmMepRowStatus,
       "dot1agCfmLtrTable": dot1agCfmLtrTable,
       "dot1agCfmLtrEntry": dot1agCfmLtrEntry,
       "dot1agCfmLtrSeqNumber": dot1agCfmLtrSeqNumber,
       "dot1agCfmLtrReceiveOrder": dot1agCfmLtrReceiveOrder,
       "dot1agCfmLtrTtl": dot1agCfmLtrTtl,
       "dot1agCfmLtrForwarded": dot1agCfmLtrForwarded,
       "dot1agCfmLtrTerminalMep": dot1agCfmLtrTerminalMep,
       "dot1agCfmLtrLastEgressIdentifier": dot1agCfmLtrLastEgressIdentifier,
       "dot1agCfmLtrNextEgressIdentifier": dot1agCfmLtrNextEgressIdentifier,
       "dot1agCfmLtrRelay": dot1agCfmLtrRelay,
       "dot1agCfmLtrChassisIdSubtype": dot1agCfmLtrChassisIdSubtype,
       "dot1agCfmLtrChassisId": dot1agCfmLtrChassisId,
       "dot1agCfmLtrManAddressType": dot1agCfmLtrManAddressType,
       "dot1agCfmLtrManAddress": dot1agCfmLtrManAddress,
       "dot1agCfmLtrIngress": dot1agCfmLtrIngress,
       "dot1agCfmLtrIngressMac": dot1agCfmLtrIngressMac,
       "dot1agCfmLtrIngressPortIdSubtype": dot1agCfmLtrIngressPortIdSubtype,
       "dot1agCfmLtrIngressPortId": dot1agCfmLtrIngressPortId,
       "dot1agCfmLtrEgress": dot1agCfmLtrEgress,
       "dot1agCfmLtrEgressMac": dot1agCfmLtrEgressMac,
       "dot1agCfmLtrEgressPortIdSubtype": dot1agCfmLtrEgressPortIdSubtype,
       "dot1agCfmLtrEgressPortId": dot1agCfmLtrEgressPortId,
       "dot1agCfmLtrOrganizationSpecificTlv": dot1agCfmLtrOrganizationSpecificTlv,
       "dot1agCfmMepDbTable": dot1agCfmMepDbTable,
       "dot1agCfmMepDbEntry": dot1agCfmMepDbEntry,
       "dot1agCfmMepDbRMepIdentifier": dot1agCfmMepDbRMepIdentifier,
       "dot1agCfmMepDbRMepState": dot1agCfmMepDbRMepState,
       "dot1agCfmMepDbRMepFailedOkTime": dot1agCfmMepDbRMepFailedOkTime,
       "dot1agCfmMepDbMacAddress": dot1agCfmMepDbMacAddress,
       "dot1agCfmMepDbRdi": dot1agCfmMepDbRdi,
       "dot1agCfmMepDbPortStatusTlv": dot1agCfmMepDbPortStatusTlv,
       "dot1agCfmMepDbInterfaceStatusTlv": dot1agCfmMepDbInterfaceStatusTlv,
       "dot1agCfmMepDbChassisIdSubtype": dot1agCfmMepDbChassisIdSubtype,
       "dot1agCfmMepDbChassisId": dot1agCfmMepDbChassisId,
       "dot1agCfmMepDbManAddressType": dot1agCfmMepDbManAddressType,
       "dot1agCfmMepDbManAddress": dot1agCfmMepDbManAddress,
       "dot1agCfmConformance": dot1agCfmConformance,
       "dot1agCfmCompliances": dot1agCfmCompliances,
       "dot1agCfmCompliance": dot1agCfmCompliance,
       "dot1agCfmGroups": dot1agCfmGroups,
       "dot1agCfmStackGroup": dot1agCfmStackGroup,
       "dot1agCfmDefaultMdLevelGroup": dot1agCfmDefaultMdLevelGroup,
       "dot1agCfmConfigErrorListGroup": dot1agCfmConfigErrorListGroup,
       "dot1agCfmMdGroup": dot1agCfmMdGroup,
       "dot1agCfmMaGroup": dot1agCfmMaGroup,
       "dot1agCfmMepGroup": dot1agCfmMepGroup,
       "dot1agCfmMepDbGroup": dot1agCfmMepDbGroup,
       "dot1agCfmNotificationsGroup": dot1agCfmNotificationsGroup}
)
