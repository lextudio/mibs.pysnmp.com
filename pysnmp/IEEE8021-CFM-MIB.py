# SNMP MIB module (IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:29 2024
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

(IEEE8021VlanIndex,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021VlanIndex",
    "ieee802dot1mibs")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
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
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021CfmMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8)
)
ieee8021CfmMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00",
         "2008-10-15 00:00",
         "2007-06-10 00:00")
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
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("charString", 2),
          ("iccFormat", 32),
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



class Dot1agCfmMDLevel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMDLevelOrNone(Integer32, TextualConvention):
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
          ("isNoInterfaceStatusTLV", 0),
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
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("defErrorCCM", 4),
          ("defMACstatus", 2),
          ("defRDICCM", 1),
          ("defRemoteCCM", 3),
          ("defXconCCM", 5),
          ("none", 0))
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
          ("noXcon", 6),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("defMHFdefault", 2),
          ("defMHFdefer", 4),
          ("defMHFexplicit", 3),
          ("defMHFnone", 1))
    )



class Dot1agCfmIdPermission(Integer32, TextualConvention):
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
        *(("sendIdChassis", 2),
          ("sendIdChassisManage", 4),
          ("sendIdDefer", 5),
          ("sendIdManage", 3),
          ("sendIdNone", 1))
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
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ingBlocked", 3),
          ("ingDown", 2),
          ("ingNoTlv", 0),
          ("ingOk", 1),
          ("ingVid", 4))
    )



class Dot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("egrBlocked", 3),
          ("egrDown", 2),
          ("egrNoTlv", 0),
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



class Dot1agCfmMepDefects(Bits, TextualConvention):
    status = "current"


class Dot1agCfmConfigErrors(Bits, TextualConvention):
    status = "current"


class Dot1agCfmPbbComponentIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_Dot1agNotifications_ObjectIdentity = ObjectIdentity
dot1agNotifications = _Dot1agNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 0)
)
_Dot1agMIBObjects_ObjectIdentity = ObjectIdentity
dot1agMIBObjects = _Dot1agMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1)
)
_Dot1agCfmStack_ObjectIdentity = ObjectIdentity
dot1agCfmStack = _Dot1agCfmStack_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1)
)
_Dot1agCfmStackTable_Object = MibTable
dot1agCfmStackTable = _Dot1agCfmStackTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmStackTable.setStatus("deprecated")
_Dot1agCfmStackEntry_Object = MibTableRow
dot1agCfmStackEntry = _Dot1agCfmStackEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1)
)
dot1agCfmStackEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmStackifIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmStackVlanIdOrNone"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmStackMdLevel"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmStackDirection"),
)
if mibBuilder.loadTexts:
    dot1agCfmStackEntry.setStatus("deprecated")
_Dot1agCfmStackifIndex_Type = InterfaceIndex
_Dot1agCfmStackifIndex_Object = MibTableColumn
dot1agCfmStackifIndex = _Dot1agCfmStackifIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 1),
    _Dot1agCfmStackifIndex_Type()
)
dot1agCfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackifIndex.setStatus("deprecated")
_Dot1agCfmStackVlanIdOrNone_Type = VlanIdOrNone
_Dot1agCfmStackVlanIdOrNone_Object = MibTableColumn
dot1agCfmStackVlanIdOrNone = _Dot1agCfmStackVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 2),
    _Dot1agCfmStackVlanIdOrNone_Type()
)
dot1agCfmStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackVlanIdOrNone.setStatus("deprecated")
_Dot1agCfmStackMdLevel_Type = Dot1agCfmMDLevel
_Dot1agCfmStackMdLevel_Object = MibTableColumn
dot1agCfmStackMdLevel = _Dot1agCfmStackMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 3),
    _Dot1agCfmStackMdLevel_Type()
)
dot1agCfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackMdLevel.setStatus("deprecated")
_Dot1agCfmStackDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmStackDirection_Object = MibTableColumn
dot1agCfmStackDirection = _Dot1agCfmStackDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 4),
    _Dot1agCfmStackDirection_Type()
)
dot1agCfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmStackDirection.setStatus("deprecated")
_Dot1agCfmStackMdIndex_Type = Unsigned32
_Dot1agCfmStackMdIndex_Object = MibTableColumn
dot1agCfmStackMdIndex = _Dot1agCfmStackMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 5),
    _Dot1agCfmStackMdIndex_Type()
)
dot1agCfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMdIndex.setStatus("deprecated")
_Dot1agCfmStackMaIndex_Type = Unsigned32
_Dot1agCfmStackMaIndex_Object = MibTableColumn
dot1agCfmStackMaIndex = _Dot1agCfmStackMaIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 6),
    _Dot1agCfmStackMaIndex_Type()
)
dot1agCfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMaIndex.setStatus("deprecated")
_Dot1agCfmStackMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmStackMepId_Object = MibTableColumn
dot1agCfmStackMepId = _Dot1agCfmStackMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 7),
    _Dot1agCfmStackMepId_Type()
)
dot1agCfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMepId.setStatus("deprecated")
_Dot1agCfmStackMacAddress_Type = MacAddress
_Dot1agCfmStackMacAddress_Object = MibTableColumn
dot1agCfmStackMacAddress = _Dot1agCfmStackMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 8),
    _Dot1agCfmStackMacAddress_Type()
)
dot1agCfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmStackMacAddress.setStatus("deprecated")
_Dot1agCfmDefaultMd_ObjectIdentity = ObjectIdentity
dot1agCfmDefaultMd = _Dot1agCfmDefaultMd_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2)
)


class _Dot1agCfmDefaultMdDefLevel_Type(Dot1agCfmMDLevel):
    """Custom type dot1agCfmDefaultMdDefLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_Dot1agCfmDefaultMdDefLevel_Object = MibScalar
dot1agCfmDefaultMdDefLevel = _Dot1agCfmDefaultMdDefLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 1),
    _Dot1agCfmDefaultMdDefLevel_Type()
)
dot1agCfmDefaultMdDefLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdDefLevel.setStatus("current")


class _Dot1agCfmDefaultMdDefMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmDefaultMdDefMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 1

    subtypeSpec = Dot1agCfmMhfCreation.subtypeSpec
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


_Dot1agCfmDefaultMdDefMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_Dot1agCfmDefaultMdDefMhfCreation_Object = MibScalar
dot1agCfmDefaultMdDefMhfCreation = _Dot1agCfmDefaultMdDefMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 2),
    _Dot1agCfmDefaultMdDefMhfCreation_Type()
)
dot1agCfmDefaultMdDefMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdDefMhfCreation.setStatus("current")


class _Dot1agCfmDefaultMdDefIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmDefaultMdDefIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1

    subtypeSpec = Dot1agCfmIdPermission.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sendIdChassis", 2),
          ("sendIdChassisManage", 4),
          ("sendIdManage", 3),
          ("sendIdNone", 1))
    )


_Dot1agCfmDefaultMdDefIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_Dot1agCfmDefaultMdDefIdPermission_Object = MibScalar
dot1agCfmDefaultMdDefIdPermission = _Dot1agCfmDefaultMdDefIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 3),
    _Dot1agCfmDefaultMdDefIdPermission_Type()
)
dot1agCfmDefaultMdDefIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdDefIdPermission.setStatus("current")
_Dot1agCfmDefaultMdTable_Object = MibTable
dot1agCfmDefaultMdTable = _Dot1agCfmDefaultMdTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdTable.setStatus("deprecated")
_Dot1agCfmDefaultMdEntry_Object = MibTableRow
dot1agCfmDefaultMdEntry = _Dot1agCfmDefaultMdEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1)
)
dot1agCfmDefaultMdEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdComponentId"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdPrimaryVid"),
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdEntry.setStatus("deprecated")
_Dot1agCfmDefaultMdComponentId_Type = Dot1agCfmPbbComponentIdentifier
_Dot1agCfmDefaultMdComponentId_Object = MibTableColumn
dot1agCfmDefaultMdComponentId = _Dot1agCfmDefaultMdComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 1),
    _Dot1agCfmDefaultMdComponentId_Type()
)
dot1agCfmDefaultMdComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdComponentId.setStatus("deprecated")
_Dot1agCfmDefaultMdPrimaryVid_Type = VlanId
_Dot1agCfmDefaultMdPrimaryVid_Object = MibTableColumn
dot1agCfmDefaultMdPrimaryVid = _Dot1agCfmDefaultMdPrimaryVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 2),
    _Dot1agCfmDefaultMdPrimaryVid_Type()
)
dot1agCfmDefaultMdPrimaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdPrimaryVid.setStatus("deprecated")
_Dot1agCfmDefaultMdStatus_Type = TruthValue
_Dot1agCfmDefaultMdStatus_Object = MibTableColumn
dot1agCfmDefaultMdStatus = _Dot1agCfmDefaultMdStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 3),
    _Dot1agCfmDefaultMdStatus_Type()
)
dot1agCfmDefaultMdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdStatus.setStatus("deprecated")


class _Dot1agCfmDefaultMdLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type dot1agCfmDefaultMdLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_Dot1agCfmDefaultMdLevel_Object = MibTableColumn
dot1agCfmDefaultMdLevel = _Dot1agCfmDefaultMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 4),
    _Dot1agCfmDefaultMdLevel_Type()
)
dot1agCfmDefaultMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdLevel.setStatus("deprecated")


class _Dot1agCfmDefaultMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmDefaultMdMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmDefaultMdMhfCreation_Object = MibTableColumn
dot1agCfmDefaultMdMhfCreation = _Dot1agCfmDefaultMdMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 5),
    _Dot1agCfmDefaultMdMhfCreation_Type()
)
dot1agCfmDefaultMdMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdMhfCreation.setStatus("deprecated")


class _Dot1agCfmDefaultMdIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmDefaultMdIdPermission based on Dot1agCfmIdPermission"""


_Dot1agCfmDefaultMdIdPermission_Object = MibTableColumn
dot1agCfmDefaultMdIdPermission = _Dot1agCfmDefaultMdIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 6),
    _Dot1agCfmDefaultMdIdPermission_Type()
)
dot1agCfmDefaultMdIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdIdPermission.setStatus("deprecated")
_Dot1agCfmVlan_ObjectIdentity = ObjectIdentity
dot1agCfmVlan = _Dot1agCfmVlan_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3)
)
_Dot1agCfmVlanTable_Object = MibTable
dot1agCfmVlanTable = _Dot1agCfmVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmVlanTable.setStatus("deprecated")
_Dot1agCfmVlanEntry_Object = MibTableRow
dot1agCfmVlanEntry = _Dot1agCfmVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1)
)
dot1agCfmVlanEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmVlanComponentId"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmVlanVid"),
)
if mibBuilder.loadTexts:
    dot1agCfmVlanEntry.setStatus("deprecated")
_Dot1agCfmVlanComponentId_Type = Dot1agCfmPbbComponentIdentifier
_Dot1agCfmVlanComponentId_Object = MibTableColumn
dot1agCfmVlanComponentId = _Dot1agCfmVlanComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 1),
    _Dot1agCfmVlanComponentId_Type()
)
dot1agCfmVlanComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmVlanComponentId.setStatus("deprecated")
_Dot1agCfmVlanVid_Type = VlanId
_Dot1agCfmVlanVid_Object = MibTableColumn
dot1agCfmVlanVid = _Dot1agCfmVlanVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 2),
    _Dot1agCfmVlanVid_Type()
)
dot1agCfmVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmVlanVid.setStatus("deprecated")
_Dot1agCfmVlanPrimaryVid_Type = VlanId
_Dot1agCfmVlanPrimaryVid_Object = MibTableColumn
dot1agCfmVlanPrimaryVid = _Dot1agCfmVlanPrimaryVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 3),
    _Dot1agCfmVlanPrimaryVid_Type()
)
dot1agCfmVlanPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmVlanPrimaryVid.setStatus("deprecated")
_Dot1agCfmVlanRowStatus_Type = RowStatus
_Dot1agCfmVlanRowStatus_Object = MibTableColumn
dot1agCfmVlanRowStatus = _Dot1agCfmVlanRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 4),
    _Dot1agCfmVlanRowStatus_Type()
)
dot1agCfmVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmVlanRowStatus.setStatus("deprecated")
_Dot1agCfmConfigErrorList_ObjectIdentity = ObjectIdentity
dot1agCfmConfigErrorList = _Dot1agCfmConfigErrorList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4)
)
_Dot1agCfmConfigErrorListTable_Object = MibTable
dot1agCfmConfigErrorListTable = _Dot1agCfmConfigErrorListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListTable.setStatus("deprecated")
_Dot1agCfmConfigErrorListEntry_Object = MibTableRow
dot1agCfmConfigErrorListEntry = _Dot1agCfmConfigErrorListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1)
)
dot1agCfmConfigErrorListEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListVid"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListEntry.setStatus("deprecated")
_Dot1agCfmConfigErrorListVid_Type = VlanId
_Dot1agCfmConfigErrorListVid_Object = MibTableColumn
dot1agCfmConfigErrorListVid = _Dot1agCfmConfigErrorListVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 1),
    _Dot1agCfmConfigErrorListVid_Type()
)
dot1agCfmConfigErrorListVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListVid.setStatus("deprecated")
_Dot1agCfmConfigErrorListIfIndex_Type = InterfaceIndex
_Dot1agCfmConfigErrorListIfIndex_Object = MibTableColumn
dot1agCfmConfigErrorListIfIndex = _Dot1agCfmConfigErrorListIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 2),
    _Dot1agCfmConfigErrorListIfIndex_Type()
)
dot1agCfmConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListIfIndex.setStatus("deprecated")
_Dot1agCfmConfigErrorListErrorType_Type = Dot1agCfmConfigErrors
_Dot1agCfmConfigErrorListErrorType_Object = MibTableColumn
dot1agCfmConfigErrorListErrorType = _Dot1agCfmConfigErrorListErrorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 3),
    _Dot1agCfmConfigErrorListErrorType_Type()
)
dot1agCfmConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListErrorType.setStatus("deprecated")
_Dot1agCfmMd_ObjectIdentity = ObjectIdentity
dot1agCfmMd = _Dot1agCfmMd_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5)
)
_Dot1agCfmMdTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdTableNextIndex_Object = MibScalar
dot1agCfmMdTableNextIndex = _Dot1agCfmMdTableNextIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 1),
    _Dot1agCfmMdTableNextIndex_Type()
)
dot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdTableNextIndex.setStatus("current")
_Dot1agCfmMdTable_Object = MibTable
dot1agCfmMdTable = _Dot1agCfmMdTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMdTable.setStatus("current")
_Dot1agCfmMdEntry_Object = MibTableRow
dot1agCfmMdEntry = _Dot1agCfmMdEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1)
)
dot1agCfmMdEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 1),
    _Dot1agCfmMdIndex_Type()
)
dot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMdIndex.setStatus("current")


class _Dot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type dot1agCfmMdFormat based on Dot1agCfmMaintDomainNameType"""


_Dot1agCfmMdFormat_Object = MibTableColumn
dot1agCfmMdFormat = _Dot1agCfmMdFormat_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 2),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 3),
    _Dot1agCfmMdName_Type()
)
dot1agCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdName.setStatus("current")


class _Dot1agCfmMdMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type dot1agCfmMdMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_Dot1agCfmMdMdLevel_Object = MibTableColumn
dot1agCfmMdMdLevel = _Dot1agCfmMdMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 4),
    _Dot1agCfmMdMdLevel_Type()
)
dot1agCfmMdMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMdLevel.setStatus("current")


class _Dot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMdMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 1

    subtypeSpec = Dot1agCfmMhfCreation.subtypeSpec
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


_Dot1agCfmMdMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_Dot1agCfmMdMhfCreation_Object = MibTableColumn
dot1agCfmMdMhfCreation = _Dot1agCfmMdMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 5),
    _Dot1agCfmMdMhfCreation_Type()
)
dot1agCfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfCreation.setStatus("current")


class _Dot1agCfmMdMhfIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMdMhfIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1

    subtypeSpec = Dot1agCfmIdPermission.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sendIdChassis", 2),
          ("sendIdChassisManage", 4),
          ("sendIdManage", 3),
          ("sendIdNone", 1))
    )


_Dot1agCfmMdMhfIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_Dot1agCfmMdMhfIdPermission_Object = MibTableColumn
dot1agCfmMdMhfIdPermission = _Dot1agCfmMdMhfIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 6),
    _Dot1agCfmMdMhfIdPermission_Type()
)
dot1agCfmMdMhfIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfIdPermission.setStatus("current")
_Dot1agCfmMdMaNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdMaNextIndex_Object = MibTableColumn
dot1agCfmMdMaNextIndex = _Dot1agCfmMdMaNextIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 7),
    _Dot1agCfmMdMaNextIndex_Type()
)
dot1agCfmMdMaNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdMaNextIndex.setStatus("current")
_Dot1agCfmMdRowStatus_Type = RowStatus
_Dot1agCfmMdRowStatus_Object = MibTableColumn
dot1agCfmMdRowStatus = _Dot1agCfmMdRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 8),
    _Dot1agCfmMdRowStatus_Type()
)
dot1agCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdRowStatus.setStatus("current")
_Dot1agCfmMa_ObjectIdentity = ObjectIdentity
dot1agCfmMa = _Dot1agCfmMa_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6)
)
_Dot1agCfmMaNetTable_Object = MibTable
dot1agCfmMaNetTable = _Dot1agCfmMaNetTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMaNetTable.setStatus("current")
_Dot1agCfmMaNetEntry_Object = MibTableRow
dot1agCfmMaNetEntry = _Dot1agCfmMaNetEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1)
)
dot1agCfmMaNetEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaNetEntry.setStatus("current")


class _Dot1agCfmMaIndex_Type(Unsigned32):
    """Custom type dot1agCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmMaIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMaIndex_Object = MibTableColumn
dot1agCfmMaIndex = _Dot1agCfmMaIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 1),
    _Dot1agCfmMaIndex_Type()
)
dot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaIndex.setStatus("current")
_Dot1agCfmMaNetFormat_Type = Dot1agCfmMaintAssocNameType
_Dot1agCfmMaNetFormat_Object = MibTableColumn
dot1agCfmMaNetFormat = _Dot1agCfmMaNetFormat_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 2),
    _Dot1agCfmMaNetFormat_Type()
)
dot1agCfmMaNetFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaNetFormat.setStatus("current")
_Dot1agCfmMaNetName_Type = Dot1agCfmMaintAssocName
_Dot1agCfmMaNetName_Object = MibTableColumn
dot1agCfmMaNetName = _Dot1agCfmMaNetName_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 3),
    _Dot1agCfmMaNetName_Type()
)
dot1agCfmMaNetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaNetName.setStatus("current")


class _Dot1agCfmMaNetCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type dot1agCfmMaNetCcmInterval based on Dot1agCfmCcmInterval"""


_Dot1agCfmMaNetCcmInterval_Object = MibTableColumn
dot1agCfmMaNetCcmInterval = _Dot1agCfmMaNetCcmInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 4),
    _Dot1agCfmMaNetCcmInterval_Type()
)
dot1agCfmMaNetCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaNetCcmInterval.setStatus("current")
_Dot1agCfmMaNetRowStatus_Type = RowStatus
_Dot1agCfmMaNetRowStatus_Object = MibTableColumn
dot1agCfmMaNetRowStatus = _Dot1agCfmMaNetRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 5),
    _Dot1agCfmMaNetRowStatus_Type()
)
dot1agCfmMaNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaNetRowStatus.setStatus("current")
_Dot1agCfmMaCompTable_Object = MibTable
dot1agCfmMaCompTable = _Dot1agCfmMaCompTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMaCompTable.setStatus("deprecated")
_Dot1agCfmMaCompEntry_Object = MibTableRow
dot1agCfmMaCompEntry = _Dot1agCfmMaCompEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1)
)
dot1agCfmMaCompEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaComponentId"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaCompEntry.setStatus("deprecated")
_Dot1agCfmMaComponentId_Type = Dot1agCfmPbbComponentIdentifier
_Dot1agCfmMaComponentId_Object = MibTableColumn
dot1agCfmMaComponentId = _Dot1agCfmMaComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 1),
    _Dot1agCfmMaComponentId_Type()
)
dot1agCfmMaComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaComponentId.setStatus("deprecated")
_Dot1agCfmMaCompPrimaryVlanId_Type = VlanIdOrNone
_Dot1agCfmMaCompPrimaryVlanId_Object = MibTableColumn
dot1agCfmMaCompPrimaryVlanId = _Dot1agCfmMaCompPrimaryVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 2),
    _Dot1agCfmMaCompPrimaryVlanId_Type()
)
dot1agCfmMaCompPrimaryVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCompPrimaryVlanId.setStatus("deprecated")


class _Dot1agCfmMaCompMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMaCompMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmMaCompMhfCreation_Object = MibTableColumn
dot1agCfmMaCompMhfCreation = _Dot1agCfmMaCompMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 3),
    _Dot1agCfmMaCompMhfCreation_Type()
)
dot1agCfmMaCompMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCompMhfCreation.setStatus("deprecated")


class _Dot1agCfmMaCompIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMaCompIdPermission based on Dot1agCfmIdPermission"""


_Dot1agCfmMaCompIdPermission_Object = MibTableColumn
dot1agCfmMaCompIdPermission = _Dot1agCfmMaCompIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 4),
    _Dot1agCfmMaCompIdPermission_Type()
)
dot1agCfmMaCompIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCompIdPermission.setStatus("deprecated")
_Dot1agCfmMaCompNumberOfVids_Type = Unsigned32
_Dot1agCfmMaCompNumberOfVids_Object = MibTableColumn
dot1agCfmMaCompNumberOfVids = _Dot1agCfmMaCompNumberOfVids_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 5),
    _Dot1agCfmMaCompNumberOfVids_Type()
)
dot1agCfmMaCompNumberOfVids.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCompNumberOfVids.setStatus("deprecated")
_Dot1agCfmMaCompRowStatus_Type = RowStatus
_Dot1agCfmMaCompRowStatus_Object = MibTableColumn
dot1agCfmMaCompRowStatus = _Dot1agCfmMaCompRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 6),
    _Dot1agCfmMaCompRowStatus_Type()
)
dot1agCfmMaCompRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCompRowStatus.setStatus("deprecated")
_Dot1agCfmMaMepListTable_Object = MibTable
dot1agCfmMaMepListTable = _Dot1agCfmMaMepListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListTable.setStatus("current")
_Dot1agCfmMaMepListEntry_Object = MibTableRow
dot1agCfmMaMepListEntry = _Dot1agCfmMaMepListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1)
)
dot1agCfmMaMepListEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListEntry.setStatus("current")
_Dot1agCfmMaMepListIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMaMepListIdentifier_Object = MibTableColumn
dot1agCfmMaMepListIdentifier = _Dot1agCfmMaMepListIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 1),
    _Dot1agCfmMaMepListIdentifier_Type()
)
dot1agCfmMaMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListIdentifier.setStatus("current")
_Dot1agCfmMaMepListRowStatus_Type = RowStatus
_Dot1agCfmMaMepListRowStatus_Object = MibTableColumn
dot1agCfmMaMepListRowStatus = _Dot1agCfmMaMepListRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 2),
    _Dot1agCfmMaMepListRowStatus_Type()
)
dot1agCfmMaMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListRowStatus.setStatus("current")
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7)
)
_Dot1agCfmMepTable_Object = MibTable
dot1agCfmMepTable = _Dot1agCfmMepTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMepTable.setStatus("current")
_Dot1agCfmMepEntry_Object = MibTableRow
dot1agCfmMepEntry = _Dot1agCfmMepEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1)
)
dot1agCfmMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepEntry.setStatus("current")
_Dot1agCfmMepIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMepIdentifier_Object = MibTableColumn
dot1agCfmMepIdentifier = _Dot1agCfmMepIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 1),
    _Dot1agCfmMepIdentifier_Type()
)
dot1agCfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepIdentifier.setStatus("current")
_Dot1agCfmMepIfIndex_Type = InterfaceIndexOrZero
_Dot1agCfmMepIfIndex_Object = MibTableColumn
dot1agCfmMepIfIndex = _Dot1agCfmMepIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 2),
    _Dot1agCfmMepIfIndex_Type()
)
dot1agCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepIfIndex.setStatus("current")
_Dot1agCfmMepDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmMepDirection_Object = MibTableColumn
dot1agCfmMepDirection = _Dot1agCfmMepDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 3),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 4),
    _Dot1agCfmMepPrimaryVid_Type()
)
dot1agCfmMepPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPrimaryVid.setStatus("current")


class _Dot1agCfmMepActive_Type(TruthValue):
    """Custom type dot1agCfmMepActive based on TruthValue"""


_Dot1agCfmMepActive_Object = MibTableColumn
dot1agCfmMepActive = _Dot1agCfmMepActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 5),
    _Dot1agCfmMepActive_Type()
)
dot1agCfmMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepActive.setStatus("current")


class _Dot1agCfmMepFngState_Type(Dot1agCfmFngState):
    """Custom type dot1agCfmMepFngState based on Dot1agCfmFngState"""


_Dot1agCfmMepFngState_Object = MibTableColumn
dot1agCfmMepFngState = _Dot1agCfmMepFngState_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 6),
    _Dot1agCfmMepFngState_Type()
)
dot1agCfmMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepFngState.setStatus("current")


class _Dot1agCfmMepCciEnabled_Type(TruthValue):
    """Custom type dot1agCfmMepCciEnabled based on TruthValue"""


_Dot1agCfmMepCciEnabled_Object = MibTableColumn
dot1agCfmMepCciEnabled = _Dot1agCfmMepCciEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 7),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 8),
    _Dot1agCfmMepCcmLtmPriority_Type()
)
dot1agCfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCcmLtmPriority.setStatus("current")
_Dot1agCfmMepMacAddress_Type = MacAddress
_Dot1agCfmMepMacAddress_Object = MibTableColumn
dot1agCfmMepMacAddress = _Dot1agCfmMepMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 9),
    _Dot1agCfmMepMacAddress_Type()
)
dot1agCfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepMacAddress.setStatus("current")


class _Dot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type dot1agCfmMepLowPrDef based on Dot1agCfmLowestAlarmPri"""


_Dot1agCfmMepLowPrDef_Object = MibTableColumn
dot1agCfmMepLowPrDef = _Dot1agCfmMepLowPrDef_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 10),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 11),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 12),
    _Dot1agCfmMepFngResetTime_Type()
)
dot1agCfmMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFngResetTime.setStatus("current")
_Dot1agCfmMepHighestPrDefect_Type = Dot1agCfmHighestDefectPri
_Dot1agCfmMepHighestPrDefect_Object = MibTableColumn
dot1agCfmMepHighestPrDefect = _Dot1agCfmMepHighestPrDefect_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 13),
    _Dot1agCfmMepHighestPrDefect_Type()
)
dot1agCfmMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepHighestPrDefect.setStatus("current")
_Dot1agCfmMepDefects_Type = Dot1agCfmMepDefects
_Dot1agCfmMepDefects_Object = MibTableColumn
dot1agCfmMepDefects = _Dot1agCfmMepDefects_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 14),
    _Dot1agCfmMepDefects_Type()
)
dot1agCfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDefects.setStatus("current")


class _Dot1agCfmMepErrorCcmLastFailure_Type(OctetString):
    """Custom type dot1agCfmMepErrorCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_Dot1agCfmMepErrorCcmLastFailure_Type.__name__ = "OctetString"
_Dot1agCfmMepErrorCcmLastFailure_Object = MibTableColumn
dot1agCfmMepErrorCcmLastFailure = _Dot1agCfmMepErrorCcmLastFailure_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 15),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 16),
    _Dot1agCfmMepXconCcmLastFailure_Type()
)
dot1agCfmMepXconCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepXconCcmLastFailure.setStatus("current")
_Dot1agCfmMepCcmSequenceErrors_Type = Counter32
_Dot1agCfmMepCcmSequenceErrors_Object = MibTableColumn
dot1agCfmMepCcmSequenceErrors = _Dot1agCfmMepCcmSequenceErrors_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 17),
    _Dot1agCfmMepCcmSequenceErrors_Type()
)
dot1agCfmMepCcmSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCcmSequenceErrors.setStatus("current")
_Dot1agCfmMepCciSentCcms_Type = Counter32
_Dot1agCfmMepCciSentCcms_Object = MibTableColumn
dot1agCfmMepCciSentCcms = _Dot1agCfmMepCciSentCcms_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 18),
    _Dot1agCfmMepCciSentCcms_Type()
)
dot1agCfmMepCciSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCciSentCcms.setStatus("current")
_Dot1agCfmMepNextLbmTransId_Type = Unsigned32
_Dot1agCfmMepNextLbmTransId_Object = MibTableColumn
dot1agCfmMepNextLbmTransId = _Dot1agCfmMepNextLbmTransId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 19),
    _Dot1agCfmMepNextLbmTransId_Type()
)
dot1agCfmMepNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepNextLbmTransId.setStatus("current")
_Dot1agCfmMepLbrIn_Type = Counter32
_Dot1agCfmMepLbrIn_Object = MibTableColumn
dot1agCfmMepLbrIn = _Dot1agCfmMepLbrIn_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 20),
    _Dot1agCfmMepLbrIn_Type()
)
dot1agCfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrIn.setStatus("current")
_Dot1agCfmMepLbrInOutOfOrder_Type = Counter32
_Dot1agCfmMepLbrInOutOfOrder_Object = MibTableColumn
dot1agCfmMepLbrInOutOfOrder = _Dot1agCfmMepLbrInOutOfOrder_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 21),
    _Dot1agCfmMepLbrInOutOfOrder_Type()
)
dot1agCfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrInOutOfOrder.setStatus("current")
_Dot1agCfmMepLbrBadMsdu_Type = Counter32
_Dot1agCfmMepLbrBadMsdu_Object = MibTableColumn
dot1agCfmMepLbrBadMsdu = _Dot1agCfmMepLbrBadMsdu_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 22),
    _Dot1agCfmMepLbrBadMsdu_Type()
)
dot1agCfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrBadMsdu.setStatus("current")
_Dot1agCfmMepLtmNextSeqNumber_Type = Unsigned32
_Dot1agCfmMepLtmNextSeqNumber_Object = MibTableColumn
dot1agCfmMepLtmNextSeqNumber = _Dot1agCfmMepLtmNextSeqNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 23),
    _Dot1agCfmMepLtmNextSeqNumber_Type()
)
dot1agCfmMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLtmNextSeqNumber.setStatus("current")
_Dot1agCfmMepUnexpLtrIn_Type = Counter32
_Dot1agCfmMepUnexpLtrIn_Object = MibTableColumn
dot1agCfmMepUnexpLtrIn = _Dot1agCfmMepUnexpLtrIn_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 24),
    _Dot1agCfmMepUnexpLtrIn_Type()
)
dot1agCfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepUnexpLtrIn.setStatus("current")
_Dot1agCfmMepLbrOut_Type = Counter32
_Dot1agCfmMepLbrOut_Object = MibTableColumn
dot1agCfmMepLbrOut = _Dot1agCfmMepLbrOut_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 25),
    _Dot1agCfmMepLbrOut_Type()
)
dot1agCfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrOut.setStatus("current")


class _Dot1agCfmMepTransmitLbmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmStatus based on TruthValue"""


_Dot1agCfmMepTransmitLbmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLbmStatus = _Dot1agCfmMepTransmitLbmStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 26),
    _Dot1agCfmMepTransmitLbmStatus_Type()
)
dot1agCfmMepTransmitLbmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmStatus.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLbmDestMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMacAddress = _Dot1agCfmMepTransmitLbmDestMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 27),
    _Dot1agCfmMepTransmitLbmDestMacAddress_Type()
)
dot1agCfmMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmMepTransmitLbmDestMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMepId = _Dot1agCfmMepTransmitLbmDestMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 28),
    _Dot1agCfmMepTransmitLbmDestMepId_Type()
)
dot1agCfmMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMepId.setStatus("current")
_Dot1agCfmMepTransmitLbmDestIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLbmDestIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestIsMepId = _Dot1agCfmMepTransmitLbmDestIsMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 29),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 30),
    _Dot1agCfmMepTransmitLbmMessages_Type()
)
dot1agCfmMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmMessages.setStatus("current")
_Dot1agCfmMepTransmitLbmDataTlv_Type = OctetString
_Dot1agCfmMepTransmitLbmDataTlv_Object = MibTableColumn
dot1agCfmMepTransmitLbmDataTlv = _Dot1agCfmMepTransmitLbmDataTlv_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 31),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 32),
    _Dot1agCfmMepTransmitLbmVlanPriority_Type()
)
dot1agCfmMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanPriority.setStatus("current")


class _Dot1agCfmMepTransmitLbmVlanDropEnable_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmVlanDropEnable based on TruthValue"""


_Dot1agCfmMepTransmitLbmVlanDropEnable_Object = MibTableColumn
dot1agCfmMepTransmitLbmVlanDropEnable = _Dot1agCfmMepTransmitLbmVlanDropEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 33),
    _Dot1agCfmMepTransmitLbmVlanDropEnable_Type()
)
dot1agCfmMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanDropEnable.setStatus("current")


class _Dot1agCfmMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmResultOK based on TruthValue"""


_Dot1agCfmMepTransmitLbmResultOK_Object = MibTableColumn
dot1agCfmMepTransmitLbmResultOK = _Dot1agCfmMepTransmitLbmResultOK_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 34),
    _Dot1agCfmMepTransmitLbmResultOK_Type()
)
dot1agCfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmResultOK.setStatus("current")
_Dot1agCfmMepTransmitLbmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLbmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLbmSeqNumber = _Dot1agCfmMepTransmitLbmSeqNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 35),
    _Dot1agCfmMepTransmitLbmSeqNumber_Type()
)
dot1agCfmMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmSeqNumber.setStatus("current")


class _Dot1agCfmMepTransmitLtmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmStatus based on TruthValue"""


_Dot1agCfmMepTransmitLtmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLtmStatus = _Dot1agCfmMepTransmitLtmStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 36),
    _Dot1agCfmMepTransmitLtmStatus_Type()
)
dot1agCfmMepTransmitLtmStatus.setMaxAccess("read-create")
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 37),
    _Dot1agCfmMepTransmitLtmFlags_Type()
)
dot1agCfmMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmFlags.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLtmTargetMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMacAddress = _Dot1agCfmMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 38),
    _Dot1agCfmMepTransmitLtmTargetMacAddress_Type()
)
dot1agCfmMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMepId_Type = Dot1agCfmMepIdOrZero
_Dot1agCfmMepTransmitLtmTargetMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMepId = _Dot1agCfmMepTransmitLtmTargetMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 39),
    _Dot1agCfmMepTransmitLtmTargetMepId_Type()
)
dot1agCfmMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMepId.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLtmTargetIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetIsMepId = _Dot1agCfmMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 40),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 41),
    _Dot1agCfmMepTransmitLtmTtl_Type()
)
dot1agCfmMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTtl.setStatus("current")


class _Dot1agCfmMepTransmitLtmResult_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmResult based on TruthValue"""


_Dot1agCfmMepTransmitLtmResult_Object = MibTableColumn
dot1agCfmMepTransmitLtmResult = _Dot1agCfmMepTransmitLtmResult_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 42),
    _Dot1agCfmMepTransmitLtmResult_Type()
)
dot1agCfmMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmResult.setStatus("current")
_Dot1agCfmMepTransmitLtmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLtmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLtmSeqNumber = _Dot1agCfmMepTransmitLtmSeqNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 43),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 44),
    _Dot1agCfmMepTransmitLtmEgressIdentifier_Type()
)
dot1agCfmMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmEgressIdentifier.setStatus("current")
_Dot1agCfmMepRowStatus_Type = RowStatus
_Dot1agCfmMepRowStatus_Object = MibTableColumn
dot1agCfmMepRowStatus = _Dot1agCfmMepRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 45),
    _Dot1agCfmMepRowStatus_Type()
)
dot1agCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepRowStatus.setStatus("current")


class _Dot1agCfmMepPbbTeCanReportPbbTePresence_Type(TruthValue):
    """Custom type dot1agCfmMepPbbTeCanReportPbbTePresence based on TruthValue"""


_Dot1agCfmMepPbbTeCanReportPbbTePresence_Object = MibTableColumn
dot1agCfmMepPbbTeCanReportPbbTePresence = _Dot1agCfmMepPbbTeCanReportPbbTePresence_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 46),
    _Dot1agCfmMepPbbTeCanReportPbbTePresence_Type()
)
dot1agCfmMepPbbTeCanReportPbbTePresence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTeCanReportPbbTePresence.setStatus("current")
_Dot1agCfmMepPbbTeTrafficMismatchDefect_Type = TruthValue
_Dot1agCfmMepPbbTeTrafficMismatchDefect_Object = MibTableColumn
dot1agCfmMepPbbTeTrafficMismatchDefect = _Dot1agCfmMepPbbTeTrafficMismatchDefect_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 47),
    _Dot1agCfmMepPbbTeTrafficMismatchDefect_Type()
)
dot1agCfmMepPbbTeTrafficMismatchDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTeTrafficMismatchDefect.setStatus("current")
_Dot1agCfmMepPbbTransmitLbmLtmReverseVid_Type = IEEE8021VlanIndex
_Dot1agCfmMepPbbTransmitLbmLtmReverseVid_Object = MibTableColumn
dot1agCfmMepPbbTransmitLbmLtmReverseVid = _Dot1agCfmMepPbbTransmitLbmLtmReverseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 48),
    _Dot1agCfmMepPbbTransmitLbmLtmReverseVid_Type()
)
dot1agCfmMepPbbTransmitLbmLtmReverseVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTransmitLbmLtmReverseVid.setStatus("current")


class _Dot1agCfmMepPbbTeMismatchAlarm_Type(TruthValue):
    """Custom type dot1agCfmMepPbbTeMismatchAlarm based on TruthValue"""


_Dot1agCfmMepPbbTeMismatchAlarm_Object = MibTableColumn
dot1agCfmMepPbbTeMismatchAlarm = _Dot1agCfmMepPbbTeMismatchAlarm_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 49),
    _Dot1agCfmMepPbbTeMismatchAlarm_Type()
)
dot1agCfmMepPbbTeMismatchAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTeMismatchAlarm.setStatus("current")
_Dot1agCfmMepPbbTeLocalMismatchDefect_Type = TruthValue
_Dot1agCfmMepPbbTeLocalMismatchDefect_Object = MibTableColumn
dot1agCfmMepPbbTeLocalMismatchDefect = _Dot1agCfmMepPbbTeLocalMismatchDefect_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 50),
    _Dot1agCfmMepPbbTeLocalMismatchDefect_Type()
)
dot1agCfmMepPbbTeLocalMismatchDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTeLocalMismatchDefect.setStatus("current")
_Dot1agCfmMepPbbTeMismatchSinceReset_Type = TruthValue
_Dot1agCfmMepPbbTeMismatchSinceReset_Object = MibTableColumn
dot1agCfmMepPbbTeMismatchSinceReset = _Dot1agCfmMepPbbTeMismatchSinceReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 51),
    _Dot1agCfmMepPbbTeMismatchSinceReset_Type()
)
dot1agCfmMepPbbTeMismatchSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepPbbTeMismatchSinceReset.setStatus("current")
_Dot1agCfmLtrTable_Object = MibTable
dot1agCfmLtrTable = _Dot1agCfmLtrTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmLtrTable.setStatus("current")
_Dot1agCfmLtrEntry_Object = MibTableRow
dot1agCfmLtrEntry = _Dot1agCfmLtrEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1)
)
dot1agCfmLtrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrSeqNumber"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrReceiveOrder"),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 1),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 2),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 3),
    _Dot1agCfmLtrTtl_Type()
)
dot1agCfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTtl.setStatus("current")
_Dot1agCfmLtrForwarded_Type = TruthValue
_Dot1agCfmLtrForwarded_Object = MibTableColumn
dot1agCfmLtrForwarded = _Dot1agCfmLtrForwarded_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 4),
    _Dot1agCfmLtrForwarded_Type()
)
dot1agCfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrForwarded.setStatus("current")
_Dot1agCfmLtrTerminalMep_Type = TruthValue
_Dot1agCfmLtrTerminalMep_Object = MibTableColumn
dot1agCfmLtrTerminalMep = _Dot1agCfmLtrTerminalMep_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 5),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 6),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 7),
    _Dot1agCfmLtrNextEgressIdentifier_Type()
)
dot1agCfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrNextEgressIdentifier.setStatus("current")
_Dot1agCfmLtrRelay_Type = Dot1agCfmRelayActionFieldValue
_Dot1agCfmLtrRelay_Object = MibTableColumn
dot1agCfmLtrRelay = _Dot1agCfmLtrRelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 8),
    _Dot1agCfmLtrRelay_Type()
)
dot1agCfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrRelay.setStatus("current")
_Dot1agCfmLtrChassisIdSubtype_Type = LldpChassisIdSubtype
_Dot1agCfmLtrChassisIdSubtype_Object = MibTableColumn
dot1agCfmLtrChassisIdSubtype = _Dot1agCfmLtrChassisIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 9),
    _Dot1agCfmLtrChassisIdSubtype_Type()
)
dot1agCfmLtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrChassisIdSubtype.setStatus("current")
_Dot1agCfmLtrChassisId_Type = LldpChassisId
_Dot1agCfmLtrChassisId_Object = MibTableColumn
dot1agCfmLtrChassisId = _Dot1agCfmLtrChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 10),
    _Dot1agCfmLtrChassisId_Type()
)
dot1agCfmLtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrChassisId.setStatus("current")
_Dot1agCfmLtrManAddressDomain_Type = TDomain
_Dot1agCfmLtrManAddressDomain_Object = MibTableColumn
dot1agCfmLtrManAddressDomain = _Dot1agCfmLtrManAddressDomain_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 11),
    _Dot1agCfmLtrManAddressDomain_Type()
)
dot1agCfmLtrManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrManAddressDomain.setStatus("current")
_Dot1agCfmLtrManAddress_Type = TAddress
_Dot1agCfmLtrManAddress_Object = MibTableColumn
dot1agCfmLtrManAddress = _Dot1agCfmLtrManAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 12),
    _Dot1agCfmLtrManAddress_Type()
)
dot1agCfmLtrManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrManAddress.setStatus("current")
_Dot1agCfmLtrIngress_Type = Dot1agCfmIngressActionFieldValue
_Dot1agCfmLtrIngress_Object = MibTableColumn
dot1agCfmLtrIngress = _Dot1agCfmLtrIngress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 13),
    _Dot1agCfmLtrIngress_Type()
)
dot1agCfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngress.setStatus("current")
_Dot1agCfmLtrIngressMac_Type = MacAddress
_Dot1agCfmLtrIngressMac_Object = MibTableColumn
dot1agCfmLtrIngressMac = _Dot1agCfmLtrIngressMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 14),
    _Dot1agCfmLtrIngressMac_Type()
)
dot1agCfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressMac.setStatus("current")
_Dot1agCfmLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_Dot1agCfmLtrIngressPortIdSubtype_Object = MibTableColumn
dot1agCfmLtrIngressPortIdSubtype = _Dot1agCfmLtrIngressPortIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 15),
    _Dot1agCfmLtrIngressPortIdSubtype_Type()
)
dot1agCfmLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressPortIdSubtype.setStatus("current")
_Dot1agCfmLtrIngressPortId_Type = LldpPortId
_Dot1agCfmLtrIngressPortId_Object = MibTableColumn
dot1agCfmLtrIngressPortId = _Dot1agCfmLtrIngressPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 16),
    _Dot1agCfmLtrIngressPortId_Type()
)
dot1agCfmLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressPortId.setStatus("current")
_Dot1agCfmLtrEgress_Type = Dot1agCfmEgressActionFieldValue
_Dot1agCfmLtrEgress_Object = MibTableColumn
dot1agCfmLtrEgress = _Dot1agCfmLtrEgress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 17),
    _Dot1agCfmLtrEgress_Type()
)
dot1agCfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgress.setStatus("current")
_Dot1agCfmLtrEgressMac_Type = MacAddress
_Dot1agCfmLtrEgressMac_Object = MibTableColumn
dot1agCfmLtrEgressMac = _Dot1agCfmLtrEgressMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 18),
    _Dot1agCfmLtrEgressMac_Type()
)
dot1agCfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressMac.setStatus("current")
_Dot1agCfmLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_Dot1agCfmLtrEgressPortIdSubtype_Object = MibTableColumn
dot1agCfmLtrEgressPortIdSubtype = _Dot1agCfmLtrEgressPortIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 19),
    _Dot1agCfmLtrEgressPortIdSubtype_Type()
)
dot1agCfmLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressPortIdSubtype.setStatus("current")
_Dot1agCfmLtrEgressPortId_Type = LldpPortId
_Dot1agCfmLtrEgressPortId_Object = MibTableColumn
dot1agCfmLtrEgressPortId = _Dot1agCfmLtrEgressPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 20),
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
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 21),
    _Dot1agCfmLtrOrganizationSpecificTlv_Type()
)
dot1agCfmLtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrOrganizationSpecificTlv.setStatus("current")
_Dot1agCfmMepDbTable_Object = MibTable
dot1agCfmMepDbTable = _Dot1agCfmMepDbTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbTable.setStatus("current")
_Dot1agCfmMepDbEntry_Object = MibTableRow
dot1agCfmMepDbEntry = _Dot1agCfmMepDbEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1)
)
dot1agCfmMepDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbEntry.setStatus("current")
_Dot1agCfmMepDbRMepIdentifier_Type = Dot1agCfmMepId
_Dot1agCfmMepDbRMepIdentifier_Object = MibTableColumn
dot1agCfmMepDbRMepIdentifier = _Dot1agCfmMepDbRMepIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 1),
    _Dot1agCfmMepDbRMepIdentifier_Type()
)
dot1agCfmMepDbRMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepIdentifier.setStatus("current")
_Dot1agCfmMepDbRMepState_Type = Dot1agCfmRemoteMepState
_Dot1agCfmMepDbRMepState_Object = MibTableColumn
dot1agCfmMepDbRMepState = _Dot1agCfmMepDbRMepState_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 2),
    _Dot1agCfmMepDbRMepState_Type()
)
dot1agCfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepState.setStatus("current")
_Dot1agCfmMepDbRMepFailedOkTime_Type = TimeStamp
_Dot1agCfmMepDbRMepFailedOkTime_Object = MibTableColumn
dot1agCfmMepDbRMepFailedOkTime = _Dot1agCfmMepDbRMepFailedOkTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 3),
    _Dot1agCfmMepDbRMepFailedOkTime_Type()
)
dot1agCfmMepDbRMepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepFailedOkTime.setStatus("current")
_Dot1agCfmMepDbMacAddress_Type = MacAddress
_Dot1agCfmMepDbMacAddress_Object = MibTableColumn
dot1agCfmMepDbMacAddress = _Dot1agCfmMepDbMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 4),
    _Dot1agCfmMepDbMacAddress_Type()
)
dot1agCfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbMacAddress.setStatus("current")
_Dot1agCfmMepDbRdi_Type = TruthValue
_Dot1agCfmMepDbRdi_Object = MibTableColumn
dot1agCfmMepDbRdi = _Dot1agCfmMepDbRdi_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 5),
    _Dot1agCfmMepDbRdi_Type()
)
dot1agCfmMepDbRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRdi.setStatus("current")


class _Dot1agCfmMepDbPortStatusTlv_Type(Dot1agCfmPortStatus):
    """Custom type dot1agCfmMepDbPortStatusTlv based on Dot1agCfmPortStatus"""


_Dot1agCfmMepDbPortStatusTlv_Object = MibTableColumn
dot1agCfmMepDbPortStatusTlv = _Dot1agCfmMepDbPortStatusTlv_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 6),
    _Dot1agCfmMepDbPortStatusTlv_Type()
)
dot1agCfmMepDbPortStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbPortStatusTlv.setStatus("current")


class _Dot1agCfmMepDbInterfaceStatusTlv_Type(Dot1agCfmInterfaceStatus):
    """Custom type dot1agCfmMepDbInterfaceStatusTlv based on Dot1agCfmInterfaceStatus"""


_Dot1agCfmMepDbInterfaceStatusTlv_Object = MibTableColumn
dot1agCfmMepDbInterfaceStatusTlv = _Dot1agCfmMepDbInterfaceStatusTlv_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 7),
    _Dot1agCfmMepDbInterfaceStatusTlv_Type()
)
dot1agCfmMepDbInterfaceStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbInterfaceStatusTlv.setStatus("current")
_Dot1agCfmMepDbChassisIdSubtype_Type = LldpChassisIdSubtype
_Dot1agCfmMepDbChassisIdSubtype_Object = MibTableColumn
dot1agCfmMepDbChassisIdSubtype = _Dot1agCfmMepDbChassisIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 8),
    _Dot1agCfmMepDbChassisIdSubtype_Type()
)
dot1agCfmMepDbChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbChassisIdSubtype.setStatus("current")
_Dot1agCfmMepDbChassisId_Type = LldpChassisId
_Dot1agCfmMepDbChassisId_Object = MibTableColumn
dot1agCfmMepDbChassisId = _Dot1agCfmMepDbChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 9),
    _Dot1agCfmMepDbChassisId_Type()
)
dot1agCfmMepDbChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbChassisId.setStatus("current")
_Dot1agCfmMepDbManAddressDomain_Type = TDomain
_Dot1agCfmMepDbManAddressDomain_Object = MibTableColumn
dot1agCfmMepDbManAddressDomain = _Dot1agCfmMepDbManAddressDomain_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 10),
    _Dot1agCfmMepDbManAddressDomain_Type()
)
dot1agCfmMepDbManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbManAddressDomain.setStatus("current")
_Dot1agCfmMepDbManAddress_Type = TAddress
_Dot1agCfmMepDbManAddress_Object = MibTableColumn
dot1agCfmMepDbManAddress = _Dot1agCfmMepDbManAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 11),
    _Dot1agCfmMepDbManAddress_Type()
)
dot1agCfmMepDbManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbManAddress.setStatus("current")
_Dot1agCfmMepDbRMepIsActive_Type = TruthValue
_Dot1agCfmMepDbRMepIsActive_Object = MibTableColumn
dot1agCfmMepDbRMepIsActive = _Dot1agCfmMepDbRMepIsActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 12),
    _Dot1agCfmMepDbRMepIsActive_Type()
)
dot1agCfmMepDbRMepIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRMepIsActive.setStatus("current")
_Dot1agCfmConformance_ObjectIdentity = ObjectIdentity
dot1agCfmConformance = _Dot1agCfmConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 2)
)
_Dot1agCfmCompliances_ObjectIdentity = ObjectIdentity
dot1agCfmCompliances = _Dot1agCfmCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 1)
)
_Dot1agCfmGroups_ObjectIdentity = ObjectIdentity
dot1agCfmGroups = _Dot1agCfmGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2)
)

# Managed Objects groups

dot1agCfmStackGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 1)
)
dot1agCfmStackGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmStackMdIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmStackMaIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmStackMepId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmStackMacAddress"))
)
if mibBuilder.loadTexts:
    dot1agCfmStackGroup.setStatus("deprecated")

dot1agCfmDefaultMdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 2)
)
dot1agCfmDefaultMdGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdMhfCreation"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdIdPermission"))
)
if mibBuilder.loadTexts:
    dot1agCfmDefaultMdGroup.setStatus("deprecated")

dot1agCfmVlanIdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 3)
)
dot1agCfmVlanIdGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmVlanPrimaryVid"),
        ("IEEE8021-CFM-MIB", "dot1agCfmVlanRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmVlanIdGroup.setStatus("deprecated")

dot1agCfmConfigErrorListGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 4)
)
dot1agCfmConfigErrorListGroup.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    dot1agCfmConfigErrorListGroup.setStatus("deprecated")

dot1agCfmMdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 5)
)
dot1agCfmMdGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdTableNextIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfCreation"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfIdPermission"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMaNextIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmMdGroup.setStatus("current")

dot1agCfmMaGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 6)
)
dot1agCfmMaGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompMhfCreation"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompIdPermission"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompRowStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompNumberOfVids"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmMaGroup.setStatus("deprecated")

dot1agCfmMepGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 7)
)
dot1agCfmMepGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepActive"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepFngState"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepCciEnabled"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmLtmPriority"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepMacAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLowPrDef"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepFngAlarmTime"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepFngResetTime"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDefects"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepErrorCcmLastFailure"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepXconCcmLastFailure"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmSequenceErrors"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepCciSentCcms"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepNextLbmTransId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrIn"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrInOutOfOrder"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrBadMsdu"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLtmNextSeqNumber"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepUnexpLtrIn"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrOut"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMepId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestIsMepId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmMessages"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDataTlv"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanPriority"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanDropEnable"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmResultOK"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmSeqNumber"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmFlags"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMacAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMepId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetIsMepId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTtl"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmResult"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmEgressIdentifier"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepRowStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrForwarded"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrRelay"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisIdSubtype"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddressDomain"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressMac"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortIdSubtype"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressMac"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortIdSubtype"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrTerminalMep"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrLastEgressIdentifier"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrNextEgressIdentifier"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrTtl"),
        ("IEEE8021-CFM-MIB", "dot1agCfmLtrOrganizationSpecificTlv"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepGroup.setStatus("current")

dot1agCfmMepDbGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 8)
)
dot1agCfmMepDbGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepFailedOkTime"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbMacAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRdi"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbPortStatusTlv"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbInterfaceStatusTlv"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisIdSubtype"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddressDomain"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddress"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbGroup.setStatus("current")

ieee8021CfmMaNetGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 10)
)
ieee8021CfmMaNetGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021CfmMaNetGroup.setStatus("current")

ieee8021CfmDefaultMdDefGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 11)
)
ieee8021CfmDefaultMdDefGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"),
        ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"))
)
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdDefGroup.setStatus("current")

ieee8021CfmPbbTeExtensionGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 12)
)
ieee8021CfmPbbTeExtensionGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIsActive"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTransmitLbmLtmReverseVid"))
)
if mibBuilder.loadTexts:
    ieee8021CfmPbbTeExtensionGroup.setStatus("current")

ieee8021CfmPbbTeTrafficBitGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 13)
)
ieee8021CfmPbbTeTrafficBitGroup.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddress"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeCanReportPbbTePresence"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeMismatchAlarm"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeTrafficMismatchDefect"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeLocalMismatchDefect"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeMismatchSinceReset"))
)
if mibBuilder.loadTexts:
    ieee8021CfmPbbTeTrafficBitGroup.setStatus("current")


# Notification objects

dot1agCfmFaultAlarm = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 8, 0, 1)
)
dot1agCfmFaultAlarm.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect")
)
if mibBuilder.loadTexts:
    dot1agCfmFaultAlarm.setStatus(
        "current"
    )


# Notifications groups

dot1agCfmNotificationsGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 9)
)
dot1agCfmNotificationsGroup.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmFaultAlarm")
)
if mibBuilder.loadTexts:
    dot1agCfmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot1agCfmCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-CFM-MIB",
    **{"Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMDLevel": Dot1agCfmMDLevel,
       "Dot1agCfmMDLevelOrNone": Dot1agCfmMDLevelOrNone,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmPortStatus": Dot1agCfmPortStatus,
       "Dot1agCfmInterfaceStatus": Dot1agCfmInterfaceStatus,
       "Dot1agCfmHighestDefectPri": Dot1agCfmHighestDefectPri,
       "Dot1agCfmLowestAlarmPri": Dot1agCfmLowestAlarmPri,
       "Dot1agCfmMepId": Dot1agCfmMepId,
       "Dot1agCfmMepIdOrZero": Dot1agCfmMepIdOrZero,
       "Dot1agCfmMhfCreation": Dot1agCfmMhfCreation,
       "Dot1agCfmIdPermission": Dot1agCfmIdPermission,
       "Dot1agCfmCcmInterval": Dot1agCfmCcmInterval,
       "Dot1agCfmFngState": Dot1agCfmFngState,
       "Dot1agCfmRelayActionFieldValue": Dot1agCfmRelayActionFieldValue,
       "Dot1agCfmIngressActionFieldValue": Dot1agCfmIngressActionFieldValue,
       "Dot1agCfmEgressActionFieldValue": Dot1agCfmEgressActionFieldValue,
       "Dot1agCfmRemoteMepState": Dot1agCfmRemoteMepState,
       "Dot1afCfmIndexIntegerNextFree": Dot1afCfmIndexIntegerNextFree,
       "Dot1agCfmMepDefects": Dot1agCfmMepDefects,
       "Dot1agCfmConfigErrors": Dot1agCfmConfigErrors,
       "Dot1agCfmPbbComponentIdentifier": Dot1agCfmPbbComponentIdentifier,
       "ieee8021CfmMib": ieee8021CfmMib,
       "dot1agNotifications": dot1agNotifications,
       "dot1agCfmFaultAlarm": dot1agCfmFaultAlarm,
       "dot1agMIBObjects": dot1agMIBObjects,
       "dot1agCfmStack": dot1agCfmStack,
       "dot1agCfmStackTable": dot1agCfmStackTable,
       "dot1agCfmStackEntry": dot1agCfmStackEntry,
       "dot1agCfmStackifIndex": dot1agCfmStackifIndex,
       "dot1agCfmStackVlanIdOrNone": dot1agCfmStackVlanIdOrNone,
       "dot1agCfmStackMdLevel": dot1agCfmStackMdLevel,
       "dot1agCfmStackDirection": dot1agCfmStackDirection,
       "dot1agCfmStackMdIndex": dot1agCfmStackMdIndex,
       "dot1agCfmStackMaIndex": dot1agCfmStackMaIndex,
       "dot1agCfmStackMepId": dot1agCfmStackMepId,
       "dot1agCfmStackMacAddress": dot1agCfmStackMacAddress,
       "dot1agCfmDefaultMd": dot1agCfmDefaultMd,
       "dot1agCfmDefaultMdDefLevel": dot1agCfmDefaultMdDefLevel,
       "dot1agCfmDefaultMdDefMhfCreation": dot1agCfmDefaultMdDefMhfCreation,
       "dot1agCfmDefaultMdDefIdPermission": dot1agCfmDefaultMdDefIdPermission,
       "dot1agCfmDefaultMdTable": dot1agCfmDefaultMdTable,
       "dot1agCfmDefaultMdEntry": dot1agCfmDefaultMdEntry,
       "dot1agCfmDefaultMdComponentId": dot1agCfmDefaultMdComponentId,
       "dot1agCfmDefaultMdPrimaryVid": dot1agCfmDefaultMdPrimaryVid,
       "dot1agCfmDefaultMdStatus": dot1agCfmDefaultMdStatus,
       "dot1agCfmDefaultMdLevel": dot1agCfmDefaultMdLevel,
       "dot1agCfmDefaultMdMhfCreation": dot1agCfmDefaultMdMhfCreation,
       "dot1agCfmDefaultMdIdPermission": dot1agCfmDefaultMdIdPermission,
       "dot1agCfmVlan": dot1agCfmVlan,
       "dot1agCfmVlanTable": dot1agCfmVlanTable,
       "dot1agCfmVlanEntry": dot1agCfmVlanEntry,
       "dot1agCfmVlanComponentId": dot1agCfmVlanComponentId,
       "dot1agCfmVlanVid": dot1agCfmVlanVid,
       "dot1agCfmVlanPrimaryVid": dot1agCfmVlanPrimaryVid,
       "dot1agCfmVlanRowStatus": dot1agCfmVlanRowStatus,
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
       "dot1agCfmMdMdLevel": dot1agCfmMdMdLevel,
       "dot1agCfmMdMhfCreation": dot1agCfmMdMhfCreation,
       "dot1agCfmMdMhfIdPermission": dot1agCfmMdMhfIdPermission,
       "dot1agCfmMdMaNextIndex": dot1agCfmMdMaNextIndex,
       "dot1agCfmMdRowStatus": dot1agCfmMdRowStatus,
       "dot1agCfmMa": dot1agCfmMa,
       "dot1agCfmMaNetTable": dot1agCfmMaNetTable,
       "dot1agCfmMaNetEntry": dot1agCfmMaNetEntry,
       "dot1agCfmMaIndex": dot1agCfmMaIndex,
       "dot1agCfmMaNetFormat": dot1agCfmMaNetFormat,
       "dot1agCfmMaNetName": dot1agCfmMaNetName,
       "dot1agCfmMaNetCcmInterval": dot1agCfmMaNetCcmInterval,
       "dot1agCfmMaNetRowStatus": dot1agCfmMaNetRowStatus,
       "dot1agCfmMaCompTable": dot1agCfmMaCompTable,
       "dot1agCfmMaCompEntry": dot1agCfmMaCompEntry,
       "dot1agCfmMaComponentId": dot1agCfmMaComponentId,
       "dot1agCfmMaCompPrimaryVlanId": dot1agCfmMaCompPrimaryVlanId,
       "dot1agCfmMaCompMhfCreation": dot1agCfmMaCompMhfCreation,
       "dot1agCfmMaCompIdPermission": dot1agCfmMaCompIdPermission,
       "dot1agCfmMaCompNumberOfVids": dot1agCfmMaCompNumberOfVids,
       "dot1agCfmMaCompRowStatus": dot1agCfmMaCompRowStatus,
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
       "dot1agCfmMepLowPrDef": dot1agCfmMepLowPrDef,
       "dot1agCfmMepFngAlarmTime": dot1agCfmMepFngAlarmTime,
       "dot1agCfmMepFngResetTime": dot1agCfmMepFngResetTime,
       "dot1agCfmMepHighestPrDefect": dot1agCfmMepHighestPrDefect,
       "dot1agCfmMepDefects": dot1agCfmMepDefects,
       "dot1agCfmMepErrorCcmLastFailure": dot1agCfmMepErrorCcmLastFailure,
       "dot1agCfmMepXconCcmLastFailure": dot1agCfmMepXconCcmLastFailure,
       "dot1agCfmMepCcmSequenceErrors": dot1agCfmMepCcmSequenceErrors,
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
       "dot1agCfmMepPbbTeCanReportPbbTePresence": dot1agCfmMepPbbTeCanReportPbbTePresence,
       "dot1agCfmMepPbbTeTrafficMismatchDefect": dot1agCfmMepPbbTeTrafficMismatchDefect,
       "dot1agCfmMepPbbTransmitLbmLtmReverseVid": dot1agCfmMepPbbTransmitLbmLtmReverseVid,
       "dot1agCfmMepPbbTeMismatchAlarm": dot1agCfmMepPbbTeMismatchAlarm,
       "dot1agCfmMepPbbTeLocalMismatchDefect": dot1agCfmMepPbbTeLocalMismatchDefect,
       "dot1agCfmMepPbbTeMismatchSinceReset": dot1agCfmMepPbbTeMismatchSinceReset,
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
       "dot1agCfmLtrManAddressDomain": dot1agCfmLtrManAddressDomain,
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
       "dot1agCfmMepDbManAddressDomain": dot1agCfmMepDbManAddressDomain,
       "dot1agCfmMepDbManAddress": dot1agCfmMepDbManAddress,
       "dot1agCfmMepDbRMepIsActive": dot1agCfmMepDbRMepIsActive,
       "dot1agCfmConformance": dot1agCfmConformance,
       "dot1agCfmCompliances": dot1agCfmCompliances,
       "dot1agCfmCompliance": dot1agCfmCompliance,
       "dot1agCfmGroups": dot1agCfmGroups,
       "dot1agCfmStackGroup": dot1agCfmStackGroup,
       "dot1agCfmDefaultMdGroup": dot1agCfmDefaultMdGroup,
       "dot1agCfmVlanIdGroup": dot1agCfmVlanIdGroup,
       "dot1agCfmConfigErrorListGroup": dot1agCfmConfigErrorListGroup,
       "dot1agCfmMdGroup": dot1agCfmMdGroup,
       "dot1agCfmMaGroup": dot1agCfmMaGroup,
       "dot1agCfmMepGroup": dot1agCfmMepGroup,
       "dot1agCfmMepDbGroup": dot1agCfmMepDbGroup,
       "dot1agCfmNotificationsGroup": dot1agCfmNotificationsGroup,
       "ieee8021CfmMaNetGroup": ieee8021CfmMaNetGroup,
       "ieee8021CfmDefaultMdDefGroup": ieee8021CfmDefaultMdDefGroup,
       "ieee8021CfmPbbTeExtensionGroup": ieee8021CfmPbbTeExtensionGroup,
       "ieee8021CfmPbbTeTrafficBitGroup": ieee8021CfmPbbTeTrafficBitGroup}
)
