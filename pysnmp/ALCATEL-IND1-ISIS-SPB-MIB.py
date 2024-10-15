# SNMP MIB module (ALCATEL-IND1-ISIS-SPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-ISIS-SPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:22 2024
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

(routingIND1IsisSpb,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1IsisSpb")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanIdOrNone")

(IEEE8021BridgePortNumber,
 IEEE8021PbbIngressEgress,
 IEEE8021PbbServiceIdentifierOrUnassigned) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbIngressEgress",
    "IEEE8021PbbServiceIdentifierOrUnassigned")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

alcatelIND1IsisSpbMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1)
)
alcatelIND1IsisSpbMib.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlcatelIND1IsisSpbAreaAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class AlcatelIND1IsisSpbSystemName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AlcatelIND1IsisSpbEctAlgorithm(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class AlcatelIND1IsisSpbMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )



class AlcatelIND1IsisSpbDigestConvention(Integer32, TextualConvention):
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
        *(("loopFreeBoth", 2),
          ("loopFreeMcastOnly", 3),
          ("off", 1))
    )



class AlcatelIND1IsisSpbLinkMetric(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class AlcatelIND1IsisSpbAdjState(Integer32, TextualConvention):
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )



class AlcatelIND1IsisSpbmSPsourceId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class AlcatelIND1IsisSpbBridgePriority(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class AlcatelIND1IsisSpbMTID(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class AlcatelIND1IsisSpbmMulticastMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gmode", 1),
          ("sgmode", 0))
    )



class AlcatelIND1IsisSpbIfOperState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("unknown", 1))
    )



class AlcatelSpbServiceIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 16777215),
    )



class AlcatelIND1IsisSpbmIsidFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 0),
          ("rx", 2),
          ("tx", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IsisSpbMibObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbMibObjects = _AlcatelIND1IsisSpbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1)
)
_AlcatelIND1IsisSpbSys_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbSys = _AlcatelIND1IsisSpbSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1)
)
_AlcatelIND1IsisSpbSysControlBvlan_Type = VlanId
_AlcatelIND1IsisSpbSysControlBvlan_Object = MibScalar
alcatelIND1IsisSpbSysControlBvlan = _AlcatelIND1IsisSpbSysControlBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 1),
    _AlcatelIND1IsisSpbSysControlBvlan_Type()
)
alcatelIND1IsisSpbSysControlBvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysControlBvlan.setStatus("current")


class _AlcatelIND1IsisSpbSysAdminState_Type(Integer32):
    """Custom type alcatelIND1IsisSpbSysAdminState based on Integer32"""
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


_AlcatelIND1IsisSpbSysAdminState_Type.__name__ = "Integer32"
_AlcatelIND1IsisSpbSysAdminState_Object = MibScalar
alcatelIND1IsisSpbSysAdminState = _AlcatelIND1IsisSpbSysAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 2),
    _AlcatelIND1IsisSpbSysAdminState_Type()
)
alcatelIND1IsisSpbSysAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysAdminState.setStatus("current")
_AlcatelIND1IsisSpbSysAreaAddress_Type = AlcatelIND1IsisSpbAreaAddress
_AlcatelIND1IsisSpbSysAreaAddress_Object = MibScalar
alcatelIND1IsisSpbSysAreaAddress = _AlcatelIND1IsisSpbSysAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 3),
    _AlcatelIND1IsisSpbSysAreaAddress_Type()
)
alcatelIND1IsisSpbSysAreaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysAreaAddress.setStatus("current")
_AlcatelIND1IsisSpbSysId_Type = MacAddress
_AlcatelIND1IsisSpbSysId_Object = MibScalar
alcatelIND1IsisSpbSysId = _AlcatelIND1IsisSpbSysId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 4),
    _AlcatelIND1IsisSpbSysId_Type()
)
alcatelIND1IsisSpbSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysId.setStatus("current")
_AlcatelIND1IsisSpbSysControlAddr_Type = MacAddress
_AlcatelIND1IsisSpbSysControlAddr_Object = MibScalar
alcatelIND1IsisSpbSysControlAddr = _AlcatelIND1IsisSpbSysControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 5),
    _AlcatelIND1IsisSpbSysControlAddr_Type()
)
alcatelIND1IsisSpbSysControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysControlAddr.setStatus("current")
_AlcatelIND1IsisSpbSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbSysName_Object = MibScalar
alcatelIND1IsisSpbSysName = _AlcatelIND1IsisSpbSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 6),
    _AlcatelIND1IsisSpbSysName_Type()
)
alcatelIND1IsisSpbSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysName.setStatus("current")
_AlcatelIND1IsisSpbSysBridgePriority_Type = AlcatelIND1IsisSpbBridgePriority
_AlcatelIND1IsisSpbSysBridgePriority_Object = MibScalar
alcatelIND1IsisSpbSysBridgePriority = _AlcatelIND1IsisSpbSysBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 7),
    _AlcatelIND1IsisSpbSysBridgePriority_Type()
)
alcatelIND1IsisSpbSysBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysBridgePriority.setStatus("current")
_AlcatelIND1IsisSpbmSysSPSourceId_Type = AlcatelIND1IsisSpbmSPsourceId
_AlcatelIND1IsisSpbmSysSPSourceId_Object = MibScalar
alcatelIND1IsisSpbmSysSPSourceId = _AlcatelIND1IsisSpbmSysSPSourceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 8),
    _AlcatelIND1IsisSpbmSysSPSourceId_Type()
)
alcatelIND1IsisSpbmSysSPSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbmSysSPSourceId.setStatus("current")
_AlcatelIND1IsisSpbvSysMode_Type = AlcatelIND1IsisSpbMode
_AlcatelIND1IsisSpbvSysMode_Object = MibScalar
alcatelIND1IsisSpbvSysMode = _AlcatelIND1IsisSpbvSysMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 9),
    _AlcatelIND1IsisSpbvSysMode_Type()
)
alcatelIND1IsisSpbvSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbvSysMode.setStatus("current")
_AlcatelIND1IsisSpbmSysMode_Type = AlcatelIND1IsisSpbMode
_AlcatelIND1IsisSpbmSysMode_Object = MibScalar
alcatelIND1IsisSpbmSysMode = _AlcatelIND1IsisSpbmSysMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 10),
    _AlcatelIND1IsisSpbmSysMode_Type()
)
alcatelIND1IsisSpbmSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbmSysMode.setStatus("current")
_AlcatelIND1IsisSpbSysDigestConvention_Type = AlcatelIND1IsisSpbDigestConvention
_AlcatelIND1IsisSpbSysDigestConvention_Object = MibScalar
alcatelIND1IsisSpbSysDigestConvention = _AlcatelIND1IsisSpbSysDigestConvention_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 11),
    _AlcatelIND1IsisSpbSysDigestConvention_Type()
)
alcatelIND1IsisSpbSysDigestConvention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysDigestConvention.setStatus("current")


class _AlcatelIND1IsisSpbSysSetOverload_Type(TruthValue):
    """Custom type alcatelIND1IsisSpbSysSetOverload based on TruthValue"""


_AlcatelIND1IsisSpbSysSetOverload_Object = MibScalar
alcatelIND1IsisSpbSysSetOverload = _AlcatelIND1IsisSpbSysSetOverload_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 12),
    _AlcatelIND1IsisSpbSysSetOverload_Type()
)
alcatelIND1IsisSpbSysSetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysSetOverload.setStatus("current")


class _AlcatelIND1IsisSpbSysOverloadTimeout_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbSysOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_AlcatelIND1IsisSpbSysOverloadTimeout_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbSysOverloadTimeout_Object = MibScalar
alcatelIND1IsisSpbSysOverloadTimeout = _AlcatelIND1IsisSpbSysOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 13),
    _AlcatelIND1IsisSpbSysOverloadTimeout_Type()
)
alcatelIND1IsisSpbSysOverloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadTimeout.setUnits("seconds")


class _AlcatelIND1IsisSpbSysOverloadOnBoot_Type(TruthValue):
    """Custom type alcatelIND1IsisSpbSysOverloadOnBoot based on TruthValue"""


_AlcatelIND1IsisSpbSysOverloadOnBoot_Object = MibScalar
alcatelIND1IsisSpbSysOverloadOnBoot = _AlcatelIND1IsisSpbSysOverloadOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 14),
    _AlcatelIND1IsisSpbSysOverloadOnBoot_Type()
)
alcatelIND1IsisSpbSysOverloadOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadOnBoot.setStatus("current")


class _AlcatelIND1IsisSpbSysOverloadOnBootTimeout_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbSysOverloadOnBootTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_AlcatelIND1IsisSpbSysOverloadOnBootTimeout_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbSysOverloadOnBootTimeout_Object = MibScalar
alcatelIND1IsisSpbSysOverloadOnBootTimeout = _AlcatelIND1IsisSpbSysOverloadOnBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 15),
    _AlcatelIND1IsisSpbSysOverloadOnBootTimeout_Type()
)
alcatelIND1IsisSpbSysOverloadOnBootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadOnBootTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadOnBootTimeout.setUnits("seconds")


class _AlcatelIND1IsisSpbSysOverloadStatus_Type(Integer32):
    """Custom type alcatelIND1IsisSpbSysOverloadStatus based on Integer32"""
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
        *(("dynamic", 2),
          ("manual", 3),
          ("manualOnBoot", 4),
          ("notInOverload", 1))
    )


_AlcatelIND1IsisSpbSysOverloadStatus_Type.__name__ = "Integer32"
_AlcatelIND1IsisSpbSysOverloadStatus_Object = MibScalar
alcatelIND1IsisSpbSysOverloadStatus = _AlcatelIND1IsisSpbSysOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 16),
    _AlcatelIND1IsisSpbSysOverloadStatus_Type()
)
alcatelIND1IsisSpbSysOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysOverloadStatus.setStatus("current")


class _AlcatelIND1IsisSpbSysLastEnabledTime_Type(DisplayString):
    """Custom type alcatelIND1IsisSpbSysLastEnabledTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AlcatelIND1IsisSpbSysLastEnabledTime_Type.__name__ = "DisplayString"
_AlcatelIND1IsisSpbSysLastEnabledTime_Object = MibScalar
alcatelIND1IsisSpbSysLastEnabledTime = _AlcatelIND1IsisSpbSysLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 17),
    _AlcatelIND1IsisSpbSysLastEnabledTime_Type()
)
alcatelIND1IsisSpbSysLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysLastEnabledTime.setStatus("current")


class _AlcatelIND1isisSpbSysLastSpfRun_Type(DisplayString):
    """Custom type alcatelIND1isisSpbSysLastSpfRun based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AlcatelIND1isisSpbSysLastSpfRun_Type.__name__ = "DisplayString"
_AlcatelIND1isisSpbSysLastSpfRun_Object = MibScalar
alcatelIND1isisSpbSysLastSpfRun = _AlcatelIND1isisSpbSysLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 18),
    _AlcatelIND1isisSpbSysLastSpfRun_Type()
)
alcatelIND1isisSpbSysLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1isisSpbSysLastSpfRun.setStatus("current")
_AlcatelIND1IsisSpbSysNumLSPs_Type = Unsigned32
_AlcatelIND1IsisSpbSysNumLSPs_Object = MibScalar
alcatelIND1IsisSpbSysNumLSPs = _AlcatelIND1IsisSpbSysNumLSPs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 19),
    _AlcatelIND1IsisSpbSysNumLSPs_Type()
)
alcatelIND1IsisSpbSysNumLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysNumLSPs.setStatus("current")
_AlcatelIND1IsisSpbSysLastEnabledTimeStamp_Type = TimeStamp
_AlcatelIND1IsisSpbSysLastEnabledTimeStamp_Object = MibScalar
alcatelIND1IsisSpbSysLastEnabledTimeStamp = _AlcatelIND1IsisSpbSysLastEnabledTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 20),
    _AlcatelIND1IsisSpbSysLastEnabledTimeStamp_Type()
)
alcatelIND1IsisSpbSysLastEnabledTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysLastEnabledTimeStamp.setStatus("current")
_AlcatelIND1isisSpbSysLastSpfRunTimeStamp_Type = TimeStamp
_AlcatelIND1isisSpbSysLastSpfRunTimeStamp_Object = MibScalar
alcatelIND1isisSpbSysLastSpfRunTimeStamp = _AlcatelIND1isisSpbSysLastSpfRunTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 1, 21),
    _AlcatelIND1isisSpbSysLastSpfRunTimeStamp_Type()
)
alcatelIND1isisSpbSysLastSpfRunTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1isisSpbSysLastSpfRunTimeStamp.setStatus("current")
_AlcatelIND1IsisSpbProtocolConfig_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbProtocolConfig = _AlcatelIND1IsisSpbProtocolConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2)
)


class _AlcatelIND1IsisSpbProtocolSpfMaxWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolSpfMaxWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )


_AlcatelIND1IsisSpbProtocolSpfMaxWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolSpfMaxWait_Object = MibScalar
alcatelIND1IsisSpbProtocolSpfMaxWait = _AlcatelIND1IsisSpbProtocolSpfMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 1),
    _AlcatelIND1IsisSpbProtocolSpfMaxWait_Type()
)
alcatelIND1IsisSpbProtocolSpfMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfMaxWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolSpfInitialWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolSpfInitialWait based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_AlcatelIND1IsisSpbProtocolSpfInitialWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolSpfInitialWait_Object = MibScalar
alcatelIND1IsisSpbProtocolSpfInitialWait = _AlcatelIND1IsisSpbProtocolSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 2),
    _AlcatelIND1IsisSpbProtocolSpfInitialWait_Type()
)
alcatelIND1IsisSpbProtocolSpfInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfInitialWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolSpfSecondWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolSpfSecondWait based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_AlcatelIND1IsisSpbProtocolSpfSecondWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolSpfSecondWait_Object = MibScalar
alcatelIND1IsisSpbProtocolSpfSecondWait = _AlcatelIND1IsisSpbProtocolSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 3),
    _AlcatelIND1IsisSpbProtocolSpfSecondWait_Type()
)
alcatelIND1IsisSpbProtocolSpfSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolSpfSecondWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolLspMaxWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolLspMaxWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )


_AlcatelIND1IsisSpbProtocolLspMaxWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolLspMaxWait_Object = MibScalar
alcatelIND1IsisSpbProtocolLspMaxWait = _AlcatelIND1IsisSpbProtocolLspMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 4),
    _AlcatelIND1IsisSpbProtocolLspMaxWait_Type()
)
alcatelIND1IsisSpbProtocolLspMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspMaxWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolLspInitialWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolLspInitialWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AlcatelIND1IsisSpbProtocolLspInitialWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolLspInitialWait_Object = MibScalar
alcatelIND1IsisSpbProtocolLspInitialWait = _AlcatelIND1IsisSpbProtocolLspInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 5),
    _AlcatelIND1IsisSpbProtocolLspInitialWait_Type()
)
alcatelIND1IsisSpbProtocolLspInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspInitialWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolLspSecondWait_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbProtocolLspSecondWait based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_AlcatelIND1IsisSpbProtocolLspSecondWait_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbProtocolLspSecondWait_Object = MibScalar
alcatelIND1IsisSpbProtocolLspSecondWait = _AlcatelIND1IsisSpbProtocolLspSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 6),
    _AlcatelIND1IsisSpbProtocolLspSecondWait_Type()
)
alcatelIND1IsisSpbProtocolLspSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolLspSecondWait.setUnits("milliseconds")


class _AlcatelIND1IsisSpbProtocolGracefulRestart_Type(TruthValue):
    """Custom type alcatelIND1IsisSpbProtocolGracefulRestart based on TruthValue"""


_AlcatelIND1IsisSpbProtocolGracefulRestart_Object = MibScalar
alcatelIND1IsisSpbProtocolGracefulRestart = _AlcatelIND1IsisSpbProtocolGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 7),
    _AlcatelIND1IsisSpbProtocolGracefulRestart_Type()
)
alcatelIND1IsisSpbProtocolGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolGracefulRestart.setStatus("current")


class _AlcatelIND1IsisSpbProtocolGRHelperMode_Type(TruthValue):
    """Custom type alcatelIND1IsisSpbProtocolGRHelperMode based on TruthValue"""


_AlcatelIND1IsisSpbProtocolGRHelperMode_Object = MibScalar
alcatelIND1IsisSpbProtocolGRHelperMode = _AlcatelIND1IsisSpbProtocolGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 2, 8),
    _AlcatelIND1IsisSpbProtocolGRHelperMode_Type()
)
alcatelIND1IsisSpbProtocolGRHelperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolGRHelperMode.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticTable_Object = MibTable
alcatelIND1IsisSpbAdjStaticTable = _AlcatelIND1IsisSpbAdjStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticTable.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticTableEntry_Object = MibTableRow
alcatelIND1IsisSpbAdjStaticTableEntry = _AlcatelIND1IsisSpbAdjStaticTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1)
)
alcatelIND1IsisSpbAdjStaticTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryIfIndex"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticTableEntry.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbAdjStaticEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryTopIx = _AlcatelIND1IsisSpbAdjStaticEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 1),
    _AlcatelIND1IsisSpbAdjStaticEntryTopIx_Type()
)
alcatelIND1IsisSpbAdjStaticEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbAdjStaticEntryIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryIfIndex = _AlcatelIND1IsisSpbAdjStaticEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 2),
    _AlcatelIND1IsisSpbAdjStaticEntryIfIndex_Type()
)
alcatelIND1IsisSpbAdjStaticEntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryIfIndex.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryMetric_Type = AlcatelIND1IsisSpbLinkMetric
_AlcatelIND1IsisSpbAdjStaticEntryMetric_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryMetric = _AlcatelIND1IsisSpbAdjStaticEntryMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 3),
    _AlcatelIND1IsisSpbAdjStaticEntryMetric_Type()
)
alcatelIND1IsisSpbAdjStaticEntryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryMetric.setStatus("current")


class _AlcatelIND1IsisSpbAdjStaticEntryHelloInterval_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbAdjStaticEntryHelloInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_AlcatelIND1IsisSpbAdjStaticEntryHelloInterval_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbAdjStaticEntryHelloInterval_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryHelloInterval = _AlcatelIND1IsisSpbAdjStaticEntryHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 4),
    _AlcatelIND1IsisSpbAdjStaticEntryHelloInterval_Type()
)
alcatelIND1IsisSpbAdjStaticEntryHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryHelloInterval.setStatus("current")


class _AlcatelIND1IsisSpbAdjStaticEntryHelloMultiplier_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_AlcatelIND1IsisSpbAdjStaticEntryHelloMultiplier_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbAdjStaticEntryHelloMultiplier_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier = _AlcatelIND1IsisSpbAdjStaticEntryHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 5),
    _AlcatelIND1IsisSpbAdjStaticEntryHelloMultiplier_Type()
)
alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryIfAdminState_Type = AlcatelIND1IsisSpbAdjState
_AlcatelIND1IsisSpbAdjStaticEntryIfAdminState_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryIfAdminState = _AlcatelIND1IsisSpbAdjStaticEntryIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 6),
    _AlcatelIND1IsisSpbAdjStaticEntryIfAdminState_Type()
)
alcatelIND1IsisSpbAdjStaticEntryIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryIfAdminState.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryRowStatus_Type = RowStatus
_AlcatelIND1IsisSpbAdjStaticEntryRowStatus_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryRowStatus = _AlcatelIND1IsisSpbAdjStaticEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 7),
    _AlcatelIND1IsisSpbAdjStaticEntryRowStatus_Type()
)
alcatelIND1IsisSpbAdjStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryRowStatus.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryCircuitId_Type = Unsigned32
_AlcatelIND1IsisSpbAdjStaticEntryCircuitId_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryCircuitId = _AlcatelIND1IsisSpbAdjStaticEntryCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 8),
    _AlcatelIND1IsisSpbAdjStaticEntryCircuitId_Type()
)
alcatelIND1IsisSpbAdjStaticEntryCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryCircuitId.setStatus("current")
_AlcatelIND1IsisSpbAdjStaticEntryIfOperState_Type = AlcatelIND1IsisSpbIfOperState
_AlcatelIND1IsisSpbAdjStaticEntryIfOperState_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryIfOperState = _AlcatelIND1IsisSpbAdjStaticEntryIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 9),
    _AlcatelIND1IsisSpbAdjStaticEntryIfOperState_Type()
)
alcatelIND1IsisSpbAdjStaticEntryIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryIfOperState.setStatus("current")


class _AlcatelIND1IsisSpbAdjStaticEntryAFDConfig_Type(Unsigned32):
    """Custom type alcatelIND1IsisSpbAdjStaticEntryAFDConfig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlcatelIND1IsisSpbAdjStaticEntryAFDConfig_Type.__name__ = "Unsigned32"
_AlcatelIND1IsisSpbAdjStaticEntryAFDConfig_Object = MibTableColumn
alcatelIND1IsisSpbAdjStaticEntryAFDConfig = _AlcatelIND1IsisSpbAdjStaticEntryAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 3, 1, 10),
    _AlcatelIND1IsisSpbAdjStaticEntryAFDConfig_Type()
)
alcatelIND1IsisSpbAdjStaticEntryAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryAFDConfig.setStatus("current")
_AlcatelIND1IsisSpbEctStaticTable_Object = MibTable
alcatelIND1IsisSpbEctStaticTable = _AlcatelIND1IsisSpbEctStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticTable.setStatus("current")
_AlcatelIND1IsisSpbEctStaticTableEntry_Object = MibTableRow
alcatelIND1IsisSpbEctStaticTableEntry = _AlcatelIND1IsisSpbEctStaticTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1)
)
alcatelIND1IsisSpbEctStaticTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryBaseVid"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticTableEntry.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbEctStaticEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryTopIx = _AlcatelIND1IsisSpbEctStaticEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 1),
    _AlcatelIND1IsisSpbEctStaticEntryTopIx_Type()
)
alcatelIND1IsisSpbEctStaticEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryBaseVid_Type = VlanId
_AlcatelIND1IsisSpbEctStaticEntryBaseVid_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryBaseVid = _AlcatelIND1IsisSpbEctStaticEntryBaseVid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 2),
    _AlcatelIND1IsisSpbEctStaticEntryBaseVid_Type()
)
alcatelIND1IsisSpbEctStaticEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryBaseVid.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryEctAlgorithm_Type = AlcatelIND1IsisSpbEctAlgorithm
_AlcatelIND1IsisSpbEctStaticEntryEctAlgorithm_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryEctAlgorithm = _AlcatelIND1IsisSpbEctStaticEntryEctAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 3),
    _AlcatelIND1IsisSpbEctStaticEntryEctAlgorithm_Type()
)
alcatelIND1IsisSpbEctStaticEntryEctAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryEctAlgorithm.setStatus("current")
_AlcatelIND1IsisSpbvEctStaticEntrySpvid_Type = VlanIdOrNone
_AlcatelIND1IsisSpbvEctStaticEntrySpvid_Object = MibTableColumn
alcatelIND1IsisSpbvEctStaticEntrySpvid = _AlcatelIND1IsisSpbvEctStaticEntrySpvid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 4),
    _AlcatelIND1IsisSpbvEctStaticEntrySpvid_Type()
)
alcatelIND1IsisSpbvEctStaticEntrySpvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbvEctStaticEntrySpvid.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryRowStatus_Type = RowStatus
_AlcatelIND1IsisSpbEctStaticEntryRowStatus_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryRowStatus = _AlcatelIND1IsisSpbEctStaticEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 5),
    _AlcatelIND1IsisSpbEctStaticEntryRowStatus_Type()
)
alcatelIND1IsisSpbEctStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryRowStatus.setStatus("current")


class _AlcatelIND1IsisSpbEctStaticEntryMulticastMode_Type(AlcatelIND1IsisSpbmMulticastMode):
    """Custom type alcatelIND1IsisSpbEctStaticEntryMulticastMode based on AlcatelIND1IsisSpbmMulticastMode"""


_AlcatelIND1IsisSpbEctStaticEntryMulticastMode_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryMulticastMode = _AlcatelIND1IsisSpbEctStaticEntryMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 6),
    _AlcatelIND1IsisSpbEctStaticEntryMulticastMode_Type()
)
alcatelIND1IsisSpbEctStaticEntryMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryMulticastMode.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysName_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName = _AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 7),
    _AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysName_Type()
)
alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName.setStatus("current")
_AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac_Type = MacAddress
_AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac_Object = MibTableColumn
alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac = _AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 4, 1, 8),
    _AlcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac_Type()
)
alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicTable_Object = MibTable
alcatelIND1IsisSpbAdjDynamicTable = _AlcatelIND1IsisSpbAdjDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicTable.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntry_Object = MibTableRow
alcatelIND1IsisSpbAdjDynamicEntry = _AlcatelIND1IsisSpbAdjDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1)
)
alcatelIND1IsisSpbAdjDynamicEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryIfIndex"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryPeerSysId"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntry.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbAdjDynamicEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryTopIx = _AlcatelIND1IsisSpbAdjDynamicEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 1),
    _AlcatelIND1IsisSpbAdjDynamicEntryTopIx_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbAdjDynamicEntryIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryIfIndex = _AlcatelIND1IsisSpbAdjDynamicEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 2),
    _AlcatelIND1IsisSpbAdjDynamicEntryIfIndex_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryIfIndex.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryPeerSysId_Type = MacAddress
_AlcatelIND1IsisSpbAdjDynamicEntryPeerSysId_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryPeerSysId = _AlcatelIND1IsisSpbAdjDynamicEntryPeerSysId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 3),
    _AlcatelIND1IsisSpbAdjDynamicEntryPeerSysId_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryPeerSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryPeerSysId.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryAdjState_Type = AlcatelIND1IsisSpbAdjState
_AlcatelIND1IsisSpbAdjDynamicEntryAdjState_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryAdjState = _AlcatelIND1IsisSpbAdjDynamicEntryAdjState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 4),
    _AlcatelIND1IsisSpbAdjDynamicEntryAdjState_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryAdjState.setStatus("current")


class _AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTime_Type(OctetString):
    """Custom type alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTime_Type.__name__ = "OctetString"
_AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTime_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime = _AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 5),
    _AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTime_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryHoldRemaining_Type = Integer32
_AlcatelIND1IsisSpbAdjDynamicEntryHoldRemaining_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining = _AlcatelIND1IsisSpbAdjDynamicEntryHoldRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 6),
    _AlcatelIND1IsisSpbAdjDynamicEntryHoldRemaining_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining.setStatus("current")


class _AlcatelIND1IsisSpbAdjDynamicEntryHoldTimer_Type(Integer32):
    """Custom type alcatelIND1IsisSpbAdjDynamicEntryHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlcatelIND1IsisSpbAdjDynamicEntryHoldTimer_Type.__name__ = "Integer32"
_AlcatelIND1IsisSpbAdjDynamicEntryHoldTimer_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryHoldTimer = _AlcatelIND1IsisSpbAdjDynamicEntryHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 7),
    _AlcatelIND1IsisSpbAdjDynamicEntryHoldTimer_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryHoldTimer.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId_Type = Unsigned32
_AlcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId = _AlcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 8),
    _AlcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryNeighPriority_Type = Unsigned32
_AlcatelIND1IsisSpbAdjDynamicEntryNeighPriority_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryNeighPriority = _AlcatelIND1IsisSpbAdjDynamicEntryNeighPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 9),
    _AlcatelIND1IsisSpbAdjDynamicEntryNeighPriority_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryNeighPriority.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryPeerSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbAdjDynamicEntryPeerSysName_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryPeerSysName = _AlcatelIND1IsisSpbAdjDynamicEntryPeerSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 10),
    _AlcatelIND1IsisSpbAdjDynamicEntryPeerSysName_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryPeerSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryPeerSysName.setStatus("current")


class _AlcatelIND1IsisSpbAdjDynamicEntryRestartStatus_Type(Integer32):
    """Custom type alcatelIND1IsisSpbAdjDynamicEntryRestartStatus based on Integer32"""
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
        *(("helping", 4),
          ("notHelping", 1),
          ("restartComplete", 3),
          ("restarting", 2))
    )


_AlcatelIND1IsisSpbAdjDynamicEntryRestartStatus_Type.__name__ = "Integer32"
_AlcatelIND1IsisSpbAdjDynamicEntryRestartStatus_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryRestartStatus = _AlcatelIND1IsisSpbAdjDynamicEntryRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 11),
    _AlcatelIND1IsisSpbAdjDynamicEntryRestartStatus_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryRestartStatus.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryRestartSupport_Type = TruthValue
_AlcatelIND1IsisSpbAdjDynamicEntryRestartSupport_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryRestartSupport = _AlcatelIND1IsisSpbAdjDynamicEntryRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 12),
    _AlcatelIND1IsisSpbAdjDynamicEntryRestartSupport_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryRestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryRestartSupport.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed_Type = TruthValue
_AlcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed = _AlcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 13),
    _AlcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed.setStatus("current")
_AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp_Type = TimeStamp
_AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp_Object = MibTableColumn
alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp = _AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 5, 1, 14),
    _AlcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp_Type()
)
alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp.setStatus("current")
_AlcatelIND1IsisSpbNodeTable_Object = MibTable
alcatelIND1IsisSpbNodeTable = _AlcatelIND1IsisSpbNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeTable.setStatus("current")
_AlcatelIND1IsisSpbNodeTableEntry_Object = MibTableRow
alcatelIND1IsisSpbNodeTableEntry = _AlcatelIND1IsisSpbNodeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1)
)
alcatelIND1IsisSpbNodeTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbNodeTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbNodeSysId"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeTableEntry.setStatus("current")
_AlcatelIND1IsisSpbNodeTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbNodeTopIx_Object = MibTableColumn
alcatelIND1IsisSpbNodeTopIx = _AlcatelIND1IsisSpbNodeTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1, 1),
    _AlcatelIND1IsisSpbNodeTopIx_Type()
)
alcatelIND1IsisSpbNodeTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeTopIx.setStatus("current")
_AlcatelIND1IsisSpbNodeSysId_Type = MacAddress
_AlcatelIND1IsisSpbNodeSysId_Object = MibTableColumn
alcatelIND1IsisSpbNodeSysId = _AlcatelIND1IsisSpbNodeSysId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1, 2),
    _AlcatelIND1IsisSpbNodeSysId_Type()
)
alcatelIND1IsisSpbNodeSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeSysId.setStatus("current")
_AlcatelIND1IsisSpbNodeSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbNodeSysName_Object = MibTableColumn
alcatelIND1IsisSpbNodeSysName = _AlcatelIND1IsisSpbNodeSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1, 3),
    _AlcatelIND1IsisSpbNodeSysName_Type()
)
alcatelIND1IsisSpbNodeSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeSysName.setStatus("current")
_AlcatelIND1IsisSpbNodeSPSourceId_Type = AlcatelIND1IsisSpbmSPsourceId
_AlcatelIND1IsisSpbNodeSPSourceId_Object = MibTableColumn
alcatelIND1IsisSpbNodeSPSourceId = _AlcatelIND1IsisSpbNodeSPSourceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1, 4),
    _AlcatelIND1IsisSpbNodeSPSourceId_Type()
)
alcatelIND1IsisSpbNodeSPSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeSPSourceId.setStatus("current")
_AlcatelIND1IsisSpbNodeBridgePriority_Type = AlcatelIND1IsisSpbBridgePriority
_AlcatelIND1IsisSpbNodeBridgePriority_Object = MibTableColumn
alcatelIND1IsisSpbNodeBridgePriority = _AlcatelIND1IsisSpbNodeBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 6, 1, 5),
    _AlcatelIND1IsisSpbNodeBridgePriority_Type()
)
alcatelIND1IsisSpbNodeBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeBridgePriority.setStatus("current")
_AlcatelIND1IsisSpbUnicastTable_Object = MibTable
alcatelIND1IsisSpbUnicastTable = _AlcatelIND1IsisSpbUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastTable.setStatus("current")
_AlcatelIND1IsisSpbUnicastTableEntry_Object = MibTableRow
alcatelIND1IsisSpbUnicastTableEntry = _AlcatelIND1IsisSpbUnicastTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1)
)
alcatelIND1IsisSpbUnicastTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbUnicastTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbUnicastBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbUnicastSysMac"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastTableEntry.setStatus("current")
_AlcatelIND1IsisSpbUnicastTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbUnicastTopIx_Object = MibTableColumn
alcatelIND1IsisSpbUnicastTopIx = _AlcatelIND1IsisSpbUnicastTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1, 1),
    _AlcatelIND1IsisSpbUnicastTopIx_Type()
)
alcatelIND1IsisSpbUnicastTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastTopIx.setStatus("current")
_AlcatelIND1IsisSpbUnicastBvlan_Type = VlanId
_AlcatelIND1IsisSpbUnicastBvlan_Object = MibTableColumn
alcatelIND1IsisSpbUnicastBvlan = _AlcatelIND1IsisSpbUnicastBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1, 2),
    _AlcatelIND1IsisSpbUnicastBvlan_Type()
)
alcatelIND1IsisSpbUnicastBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastBvlan.setStatus("current")
_AlcatelIND1IsisSpbUnicastSysMac_Type = MacAddress
_AlcatelIND1IsisSpbUnicastSysMac_Object = MibTableColumn
alcatelIND1IsisSpbUnicastSysMac = _AlcatelIND1IsisSpbUnicastSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1, 3),
    _AlcatelIND1IsisSpbUnicastSysMac_Type()
)
alcatelIND1IsisSpbUnicastSysMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastSysMac.setStatus("current")
_AlcatelIND1IsisSpbUnicastSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbUnicastSysName_Object = MibTableColumn
alcatelIND1IsisSpbUnicastSysName = _AlcatelIND1IsisSpbUnicastSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1, 4),
    _AlcatelIND1IsisSpbUnicastSysName_Type()
)
alcatelIND1IsisSpbUnicastSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastSysName.setStatus("current")
_AlcatelIND1IsisSpbUnicastOutboundIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbUnicastOutboundIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbUnicastOutboundIfIndex = _AlcatelIND1IsisSpbUnicastOutboundIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 7, 1, 5),
    _AlcatelIND1IsisSpbUnicastOutboundIfIndex_Type()
)
alcatelIND1IsisSpbUnicastOutboundIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastOutboundIfIndex.setStatus("current")
_AlcatelIND1IsisSpbMulticastTable_Object = MibTable
alcatelIND1IsisSpbMulticastTable = _AlcatelIND1IsisSpbMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTable.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntry_Object = MibTableRow
alcatelIND1IsisSpbMulticastTableEntry = _AlcatelIND1IsisSpbMulticastTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1)
)
alcatelIND1IsisSpbMulticastTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryMulticastMac"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntry.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbMulticastTableEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryTopIx = _AlcatelIND1IsisSpbMulticastTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 1),
    _AlcatelIND1IsisSpbMulticastTableEntryTopIx_Type()
)
alcatelIND1IsisSpbMulticastTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryBvlan_Type = VlanId
_AlcatelIND1IsisSpbMulticastTableEntryBvlan_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryBvlan = _AlcatelIND1IsisSpbMulticastTableEntryBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 2),
    _AlcatelIND1IsisSpbMulticastTableEntryBvlan_Type()
)
alcatelIND1IsisSpbMulticastTableEntryBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryBvlan.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryMulticastMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastTableEntryMulticastMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryMulticastMac = _AlcatelIND1IsisSpbMulticastTableEntryMulticastMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 3),
    _AlcatelIND1IsisSpbMulticastTableEntryMulticastMac_Type()
)
alcatelIND1IsisSpbMulticastTableEntryMulticastMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryMulticastMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound = _AlcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 4),
    _AlcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound_Type()
)
alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntrySrcMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastTableEntrySrcMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntrySrcMac = _AlcatelIND1IsisSpbMulticastTableEntrySrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 5),
    _AlcatelIND1IsisSpbMulticastTableEntrySrcMac_Type()
)
alcatelIND1IsisSpbMulticastTableEntrySrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntrySrcMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryIfIndexInbound_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbMulticastTableEntryIfIndexInbound_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound = _AlcatelIND1IsisSpbMulticastTableEntryIfIndexInbound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 6),
    _AlcatelIND1IsisSpbMulticastTableEntryIfIndexInbound_Type()
)
alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntrySysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbMulticastTableEntrySysName_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntrySysName = _AlcatelIND1IsisSpbMulticastTableEntrySysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 7),
    _AlcatelIND1IsisSpbMulticastTableEntrySysName_Type()
)
alcatelIND1IsisSpbMulticastTableEntrySysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntrySysName.setStatus("current")
_AlcatelIND1IsisSpbMulticastTableEntryIsid_Type = AlcatelSpbServiceIdentifier
_AlcatelIND1IsisSpbMulticastTableEntryIsid_Object = MibTableColumn
alcatelIND1IsisSpbMulticastTableEntryIsid = _AlcatelIND1IsisSpbMulticastTableEntryIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 8, 1, 8),
    _AlcatelIND1IsisSpbMulticastTableEntryIsid_Type()
)
alcatelIND1IsisSpbMulticastTableEntryIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryIsid.setStatus("current")
_AlcatelIND1IsisSpbLSPTable_Object = MibTable
alcatelIND1IsisSpbLSPTable = _AlcatelIND1IsisSpbLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPTable.setStatus("current")
_AlcatelIND1IsisSpbLSPEntry_Object = MibTableRow
alcatelIND1IsisSpbLSPEntry = _AlcatelIND1IsisSpbLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1)
)
alcatelIND1IsisSpbLSPEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPId"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPEntry.setStatus("current")
_AlcatelIND1IsisSpbLSPTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbLSPTopIx_Object = MibTableColumn
alcatelIND1IsisSpbLSPTopIx = _AlcatelIND1IsisSpbLSPTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 1),
    _AlcatelIND1IsisSpbLSPTopIx_Type()
)
alcatelIND1IsisSpbLSPTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPTopIx.setStatus("current")
_AlcatelIND1IsisSpbLSPId_Type = OctetString
_AlcatelIND1IsisSpbLSPId_Object = MibTableColumn
alcatelIND1IsisSpbLSPId = _AlcatelIND1IsisSpbLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 2),
    _AlcatelIND1IsisSpbLSPId_Type()
)
alcatelIND1IsisSpbLSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPId.setStatus("current")
_AlcatelIND1IsisSpbLSPSeq_Type = Counter32
_AlcatelIND1IsisSpbLSPSeq_Object = MibTableColumn
alcatelIND1IsisSpbLSPSeq = _AlcatelIND1IsisSpbLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 3),
    _AlcatelIND1IsisSpbLSPSeq_Type()
)
alcatelIND1IsisSpbLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPSeq.setStatus("current")
_AlcatelIND1IsisSpbLSPChecksum_Type = Integer32
_AlcatelIND1IsisSpbLSPChecksum_Object = MibTableColumn
alcatelIND1IsisSpbLSPChecksum = _AlcatelIND1IsisSpbLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 4),
    _AlcatelIND1IsisSpbLSPChecksum_Type()
)
alcatelIND1IsisSpbLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPChecksum.setStatus("current")
_AlcatelIND1IsisSpbLSPLifetimeRemain_Type = Integer32
_AlcatelIND1IsisSpbLSPLifetimeRemain_Object = MibTableColumn
alcatelIND1IsisSpbLSPLifetimeRemain = _AlcatelIND1IsisSpbLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 5),
    _AlcatelIND1IsisSpbLSPLifetimeRemain_Type()
)
alcatelIND1IsisSpbLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPLifetimeRemain.setStatus("current")
_AlcatelIND1IsisSpbLSPVersion_Type = Integer32
_AlcatelIND1IsisSpbLSPVersion_Object = MibTableColumn
alcatelIND1IsisSpbLSPVersion = _AlcatelIND1IsisSpbLSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 6),
    _AlcatelIND1IsisSpbLSPVersion_Type()
)
alcatelIND1IsisSpbLSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPVersion.setStatus("current")
_AlcatelIND1IsisSpbLSPPktType_Type = Integer32
_AlcatelIND1IsisSpbLSPPktType_Object = MibTableColumn
alcatelIND1IsisSpbLSPPktType = _AlcatelIND1IsisSpbLSPPktType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 7),
    _AlcatelIND1IsisSpbLSPPktType_Type()
)
alcatelIND1IsisSpbLSPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPPktType.setStatus("current")
_AlcatelIND1IsisSpbLSPPktVersion_Type = Integer32
_AlcatelIND1IsisSpbLSPPktVersion_Object = MibTableColumn
alcatelIND1IsisSpbLSPPktVersion = _AlcatelIND1IsisSpbLSPPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 8),
    _AlcatelIND1IsisSpbLSPPktVersion_Type()
)
alcatelIND1IsisSpbLSPPktVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPPktVersion.setStatus("current")
_AlcatelIND1IsisSpbLSPMaxArea_Type = Integer32
_AlcatelIND1IsisSpbLSPMaxArea_Object = MibTableColumn
alcatelIND1IsisSpbLSPMaxArea = _AlcatelIND1IsisSpbLSPMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 9),
    _AlcatelIND1IsisSpbLSPMaxArea_Type()
)
alcatelIND1IsisSpbLSPMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPMaxArea.setStatus("current")
_AlcatelIND1IsisSpbLSPSysIdLen_Type = Integer32
_AlcatelIND1IsisSpbLSPSysIdLen_Object = MibTableColumn
alcatelIND1IsisSpbLSPSysIdLen = _AlcatelIND1IsisSpbLSPSysIdLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 10),
    _AlcatelIND1IsisSpbLSPSysIdLen_Type()
)
alcatelIND1IsisSpbLSPSysIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPSysIdLen.setStatus("current")
_AlcatelIND1IsisSpbLSPAttributes_Type = Integer32
_AlcatelIND1IsisSpbLSPAttributes_Object = MibTableColumn
alcatelIND1IsisSpbLSPAttributes = _AlcatelIND1IsisSpbLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 11),
    _AlcatelIND1IsisSpbLSPAttributes_Type()
)
alcatelIND1IsisSpbLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPAttributes.setStatus("current")
_AlcatelIND1IsisSpbLSPUsedLen_Type = Integer32
_AlcatelIND1IsisSpbLSPUsedLen_Object = MibTableColumn
alcatelIND1IsisSpbLSPUsedLen = _AlcatelIND1IsisSpbLSPUsedLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 12),
    _AlcatelIND1IsisSpbLSPUsedLen_Type()
)
alcatelIND1IsisSpbLSPUsedLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPUsedLen.setStatus("current")
_AlcatelIND1IsisSpbLSPAllocLen_Type = Integer32
_AlcatelIND1IsisSpbLSPAllocLen_Object = MibTableColumn
alcatelIND1IsisSpbLSPAllocLen = _AlcatelIND1IsisSpbLSPAllocLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 13),
    _AlcatelIND1IsisSpbLSPAllocLen_Type()
)
alcatelIND1IsisSpbLSPAllocLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPAllocLen.setStatus("current")
_AlcatelIND1IsisSpbLSPBuff_Type = OctetString
_AlcatelIND1IsisSpbLSPBuff_Object = MibTableColumn
alcatelIND1IsisSpbLSPBuff = _AlcatelIND1IsisSpbLSPBuff_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 9, 1, 14),
    _AlcatelIND1IsisSpbLSPBuff_Type()
)
alcatelIND1IsisSpbLSPBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPBuff.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceTable_Object = MibTable
alcatelIND1IsisSpbMulticastSourceTable = _AlcatelIND1IsisSpbMulticastSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceTable.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceEntry_Object = MibTableRow
alcatelIND1IsisSpbMulticastSourceEntry = _AlcatelIND1IsisSpbMulticastSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1)
)
alcatelIND1IsisSpbMulticastSourceEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSysMac"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceBvlan"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceEntry.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbMulticastSourceTopIx_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceTopIx = _AlcatelIND1IsisSpbMulticastSourceTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1, 1),
    _AlcatelIND1IsisSpbMulticastSourceTopIx_Type()
)
alcatelIND1IsisSpbMulticastSourceTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceTopIx.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSysMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastSourceSysMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSysMac = _AlcatelIND1IsisSpbMulticastSourceSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1, 2),
    _AlcatelIND1IsisSpbMulticastSourceSysMac_Type()
)
alcatelIND1IsisSpbMulticastSourceSysMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSysMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceBvlan_Type = VlanId
_AlcatelIND1IsisSpbMulticastSourceBvlan_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceBvlan = _AlcatelIND1IsisSpbMulticastSourceBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1, 3),
    _AlcatelIND1IsisSpbMulticastSourceBvlan_Type()
)
alcatelIND1IsisSpbMulticastSourceBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceBvlan.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbMulticastSourceSysName_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSysName = _AlcatelIND1IsisSpbMulticastSourceSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1, 4),
    _AlcatelIND1IsisSpbMulticastSourceSysName_Type()
)
alcatelIND1IsisSpbMulticastSourceSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSysName.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceReachable_Type = TruthValue
_AlcatelIND1IsisSpbMulticastSourceReachable_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceReachable = _AlcatelIND1IsisSpbMulticastSourceReachable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 10, 1, 5),
    _AlcatelIND1IsisSpbMulticastSourceReachable_Type()
)
alcatelIND1IsisSpbMulticastSourceReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceReachable.setStatus("current")
_AlcatelIND1IsisSpbSpfTable_Object = MibTable
alcatelIND1IsisSpbSpfTable = _AlcatelIND1IsisSpbSpfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfTable.setStatus("current")
_AlcatelIND1IsisSpbSpfTableEntry_Object = MibTableRow
alcatelIND1IsisSpbSpfTableEntry = _AlcatelIND1IsisSpbSpfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1)
)
alcatelIND1IsisSpbSpfTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfSysMac"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfTableEntry.setStatus("current")
_AlcatelIND1IsisSpbSpfBvlan_Type = VlanId
_AlcatelIND1IsisSpbSpfBvlan_Object = MibTableColumn
alcatelIND1IsisSpbSpfBvlan = _AlcatelIND1IsisSpbSpfBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 1),
    _AlcatelIND1IsisSpbSpfBvlan_Type()
)
alcatelIND1IsisSpbSpfBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfBvlan.setStatus("current")
_AlcatelIND1IsisSpbSpfSysMac_Type = MacAddress
_AlcatelIND1IsisSpbSpfSysMac_Object = MibTableColumn
alcatelIND1IsisSpbSpfSysMac = _AlcatelIND1IsisSpbSpfSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 2),
    _AlcatelIND1IsisSpbSpfSysMac_Type()
)
alcatelIND1IsisSpbSpfSysMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfSysMac.setStatus("current")
_AlcatelIND1IsisSpbSpfSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbSpfSysName_Object = MibTableColumn
alcatelIND1IsisSpbSpfSysName = _AlcatelIND1IsisSpbSpfSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 3),
    _AlcatelIND1IsisSpbSpfSysName_Type()
)
alcatelIND1IsisSpbSpfSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfSysName.setStatus("current")
_AlcatelIND1IsisSpbSpfIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbSpfIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbSpfIfIndex = _AlcatelIND1IsisSpbSpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 4),
    _AlcatelIND1IsisSpbSpfIfIndex_Type()
)
alcatelIND1IsisSpbSpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfIfIndex.setStatus("current")
_AlcatelIND1IsisSpbSpfNextHopSysMac_Type = MacAddress
_AlcatelIND1IsisSpbSpfNextHopSysMac_Object = MibTableColumn
alcatelIND1IsisSpbSpfNextHopSysMac = _AlcatelIND1IsisSpbSpfNextHopSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 5),
    _AlcatelIND1IsisSpbSpfNextHopSysMac_Type()
)
alcatelIND1IsisSpbSpfNextHopSysMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfNextHopSysMac.setStatus("current")
_AlcatelIND1IsisSpbSpfNextHopSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbSpfNextHopSysName_Object = MibTableColumn
alcatelIND1IsisSpbSpfNextHopSysName = _AlcatelIND1IsisSpbSpfNextHopSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 6),
    _AlcatelIND1IsisSpbSpfNextHopSysName_Type()
)
alcatelIND1IsisSpbSpfNextHopSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfNextHopSysName.setStatus("current")
_AlcatelIND1IsisSpbSpfMetric_Type = AlcatelIND1IsisSpbLinkMetric
_AlcatelIND1IsisSpbSpfMetric_Object = MibTableColumn
alcatelIND1IsisSpbSpfMetric = _AlcatelIND1IsisSpbSpfMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 7),
    _AlcatelIND1IsisSpbSpfMetric_Type()
)
alcatelIND1IsisSpbSpfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfMetric.setStatus("current")
_AlcatelIND1IsisSpbSpfHopCount_Type = Integer32
_AlcatelIND1IsisSpbSpfHopCount_Object = MibTableColumn
alcatelIND1IsisSpbSpfHopCount = _AlcatelIND1IsisSpbSpfHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 11, 1, 8),
    _AlcatelIND1IsisSpbSpfHopCount_Type()
)
alcatelIND1IsisSpbSpfHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfHopCount.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTable_Object = MibTable
alcatelIND1IsisSpbMulticastSourceSpfTable = _AlcatelIND1IsisSpbMulticastSourceSpfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTable.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntry_Object = MibTableRow
alcatelIND1IsisSpbMulticastSourceSpfTableEntry = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1)
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntry.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 1),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 2),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan_Type = VlanId
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 3),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 4),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 5),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 6),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac_Type = MacAddress
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 7),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric_Type = AlcatelIND1IsisSpbLinkMetric
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 8),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric.setStatus("current")
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount_Type = Unsigned32
_AlcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount_Object = MibTableColumn
alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount = _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 12, 1, 9),
    _AlcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount_Type()
)
alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount.setStatus("current")
_AlcatelIND1IsisSpbIngressMacFilterTable_Object = MibTable
alcatelIND1IsisSpbIngressMacFilterTable = _AlcatelIND1IsisSpbIngressMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacFilterTable.setStatus("current")
_AlcatelIND1IsisSpbIngressMacFilterEntry_Object = MibTableRow
alcatelIND1IsisSpbIngressMacFilterEntry = _AlcatelIND1IsisSpbIngressMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13, 1)
)
alcatelIND1IsisSpbIngressMacFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbIngressMacBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbIngressMacSysMac"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacFilterEntry.setStatus("current")
_AlcatelIND1IsisSpbIngressMacBvlan_Type = VlanId
_AlcatelIND1IsisSpbIngressMacBvlan_Object = MibTableColumn
alcatelIND1IsisSpbIngressMacBvlan = _AlcatelIND1IsisSpbIngressMacBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13, 1, 1),
    _AlcatelIND1IsisSpbIngressMacBvlan_Type()
)
alcatelIND1IsisSpbIngressMacBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacBvlan.setStatus("current")
_AlcatelIND1IsisSpbIngressMacSysMac_Type = MacAddress
_AlcatelIND1IsisSpbIngressMacSysMac_Object = MibTableColumn
alcatelIND1IsisSpbIngressMacSysMac = _AlcatelIND1IsisSpbIngressMacSysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13, 1, 2),
    _AlcatelIND1IsisSpbIngressMacSysMac_Type()
)
alcatelIND1IsisSpbIngressMacSysMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacSysMac.setStatus("current")
_AlcatelIND1IsisSpbIngressMacSysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbIngressMacSysName_Object = MibTableColumn
alcatelIND1IsisSpbIngressMacSysName = _AlcatelIND1IsisSpbIngressMacSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13, 1, 3),
    _AlcatelIND1IsisSpbIngressMacSysName_Type()
)
alcatelIND1IsisSpbIngressMacSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacSysName.setStatus("current")
_AlcatelIND1IsisSpbIngressMacIfIndex_Type = InterfaceIndexOrZero
_AlcatelIND1IsisSpbIngressMacIfIndex_Object = MibTableColumn
alcatelIND1IsisSpbIngressMacIfIndex = _AlcatelIND1IsisSpbIngressMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 13, 1, 4),
    _AlcatelIND1IsisSpbIngressMacIfIndex_Type()
)
alcatelIND1IsisSpbIngressMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacIfIndex.setStatus("current")
_AlcatelIND1IsisSpbServiceTable_Object = MibTable
alcatelIND1IsisSpbServiceTable = _AlcatelIND1IsisSpbServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTable.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntry_Object = MibTableRow
alcatelIND1IsisSpbServiceTableEntry = _AlcatelIND1IsisSpbServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1)
)
alcatelIND1IsisSpbServiceTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntryBvlan"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntryIsid"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntrySysMac"),
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntry.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1IsisSpbServiceTableEntryTopIx_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntryTopIx = _AlcatelIND1IsisSpbServiceTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 1),
    _AlcatelIND1IsisSpbServiceTableEntryTopIx_Type()
)
alcatelIND1IsisSpbServiceTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntryTopIx.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntryBvlan_Type = VlanId
_AlcatelIND1IsisSpbServiceTableEntryBvlan_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntryBvlan = _AlcatelIND1IsisSpbServiceTableEntryBvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 2),
    _AlcatelIND1IsisSpbServiceTableEntryBvlan_Type()
)
alcatelIND1IsisSpbServiceTableEntryBvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntryBvlan.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntryIsid_Type = AlcatelSpbServiceIdentifier
_AlcatelIND1IsisSpbServiceTableEntryIsid_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntryIsid = _AlcatelIND1IsisSpbServiceTableEntryIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 3),
    _AlcatelIND1IsisSpbServiceTableEntryIsid_Type()
)
alcatelIND1IsisSpbServiceTableEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntryIsid.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntrySysMac_Type = MacAddress
_AlcatelIND1IsisSpbServiceTableEntrySysMac_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntrySysMac = _AlcatelIND1IsisSpbServiceTableEntrySysMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 4),
    _AlcatelIND1IsisSpbServiceTableEntrySysMac_Type()
)
alcatelIND1IsisSpbServiceTableEntrySysMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntrySysMac.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntrySysName_Type = AlcatelIND1IsisSpbSystemName
_AlcatelIND1IsisSpbServiceTableEntrySysName_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntrySysName = _AlcatelIND1IsisSpbServiceTableEntrySysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 5),
    _AlcatelIND1IsisSpbServiceTableEntrySysName_Type()
)
alcatelIND1IsisSpbServiceTableEntrySysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntrySysName.setStatus("current")
_AlcatelIND1IsisSpbServiceTableEntryIsidFlags_Type = AlcatelIND1IsisSpbmIsidFlags
_AlcatelIND1IsisSpbServiceTableEntryIsidFlags_Object = MibTableColumn
alcatelIND1IsisSpbServiceTableEntryIsidFlags = _AlcatelIND1IsisSpbServiceTableEntryIsidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 14, 1, 6),
    _AlcatelIND1IsisSpbServiceTableEntryIsidFlags_Type()
)
alcatelIND1IsisSpbServiceTableEntryIsidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntryIsidFlags.setStatus("current")
_AlcatelIND1SpbIPVPNBindTable_Object = MibTable
alcatelIND1SpbIPVPNBindTable = _AlcatelIND1SpbIPVPNBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindTable.setStatus("current")
_AlcatelIND1SpbIPVPNBindTableEntry_Object = MibTableRow
alcatelIND1SpbIPVPNBindTableEntry = _AlcatelIND1SpbIPVPNBindTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1)
)
alcatelIND1SpbIPVPNBindTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindVrfName"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindIsid"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindGateway"),
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindTableEntry.setStatus("current")
_AlcatelIND1SpbIPVPNBindTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1SpbIPVPNBindTableEntryTopIx_Object = MibTableColumn
alcatelIND1SpbIPVPNBindTableEntryTopIx = _AlcatelIND1SpbIPVPNBindTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 1),
    _AlcatelIND1SpbIPVPNBindTableEntryTopIx_Type()
)
alcatelIND1SpbIPVPNBindTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindTableEntryTopIx.setStatus("current")


class _AlcatelIND1SpbIPVPNBindVrfName_Type(SnmpAdminString):
    """Custom type alcatelIND1SpbIPVPNBindVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlcatelIND1SpbIPVPNBindVrfName_Type.__name__ = "SnmpAdminString"
_AlcatelIND1SpbIPVPNBindVrfName_Object = MibTableColumn
alcatelIND1SpbIPVPNBindVrfName = _AlcatelIND1SpbIPVPNBindVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 2),
    _AlcatelIND1SpbIPVPNBindVrfName_Type()
)
alcatelIND1SpbIPVPNBindVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindVrfName.setStatus("current")
_AlcatelIND1SpbIPVPNBindIsid_Type = Unsigned32
_AlcatelIND1SpbIPVPNBindIsid_Object = MibTableColumn
alcatelIND1SpbIPVPNBindIsid = _AlcatelIND1SpbIPVPNBindIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 3),
    _AlcatelIND1SpbIPVPNBindIsid_Type()
)
alcatelIND1SpbIPVPNBindIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindIsid.setStatus("current")
_AlcatelIND1SpbIPVPNBindGateway_Type = IpAddress
_AlcatelIND1SpbIPVPNBindGateway_Object = MibTableColumn
alcatelIND1SpbIPVPNBindGateway = _AlcatelIND1SpbIPVPNBindGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 4),
    _AlcatelIND1SpbIPVPNBindGateway_Type()
)
alcatelIND1SpbIPVPNBindGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindGateway.setStatus("current")


class _AlcatelIND1SpbIPVPNBindImportRouteMap_Type(SnmpAdminString):
    """Custom type alcatelIND1SpbIPVPNBindImportRouteMap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlcatelIND1SpbIPVPNBindImportRouteMap_Type.__name__ = "SnmpAdminString"
_AlcatelIND1SpbIPVPNBindImportRouteMap_Object = MibTableColumn
alcatelIND1SpbIPVPNBindImportRouteMap = _AlcatelIND1SpbIPVPNBindImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 5),
    _AlcatelIND1SpbIPVPNBindImportRouteMap_Type()
)
alcatelIND1SpbIPVPNBindImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindImportRouteMap.setStatus("current")
_AlcatelIND1SpbIPVPNBindRowStatus_Type = RowStatus
_AlcatelIND1SpbIPVPNBindRowStatus_Object = MibTableColumn
alcatelIND1SpbIPVPNBindRowStatus = _AlcatelIND1SpbIPVPNBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 15, 1, 6),
    _AlcatelIND1SpbIPVPNBindRowStatus_Type()
)
alcatelIND1SpbIPVPNBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNBindRowStatus.setStatus("current")
_AlcatelIND1SpbIPVPNRouteTable_Object = MibTable
alcatelIND1SpbIPVPNRouteTable = _AlcatelIND1SpbIPVPNRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteTable.setStatus("current")
_AlcatelIND1SpbIPVPNRouteTableEntry_Object = MibTableRow
alcatelIND1SpbIPVPNRouteTableEntry = _AlcatelIND1SpbIPVPNRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1)
)
alcatelIND1SpbIPVPNRouteTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRouteTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRouteIsid"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRoutePrefix"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRoutePrefixLen"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRouteGateway"),
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteTableEntry.setStatus("current")
_AlcatelIND1SpbIPVPNRouteTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1SpbIPVPNRouteTableEntryTopIx_Object = MibTableColumn
alcatelIND1SpbIPVPNRouteTableEntryTopIx = _AlcatelIND1SpbIPVPNRouteTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 1),
    _AlcatelIND1SpbIPVPNRouteTableEntryTopIx_Type()
)
alcatelIND1SpbIPVPNRouteTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteTableEntryTopIx.setStatus("current")
_AlcatelIND1SpbIPVPNRouteIsid_Type = Unsigned32
_AlcatelIND1SpbIPVPNRouteIsid_Object = MibTableColumn
alcatelIND1SpbIPVPNRouteIsid = _AlcatelIND1SpbIPVPNRouteIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 2),
    _AlcatelIND1SpbIPVPNRouteIsid_Type()
)
alcatelIND1SpbIPVPNRouteIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteIsid.setStatus("current")
_AlcatelIND1SpbIPVPNRoutePrefix_Type = IpAddress
_AlcatelIND1SpbIPVPNRoutePrefix_Object = MibTableColumn
alcatelIND1SpbIPVPNRoutePrefix = _AlcatelIND1SpbIPVPNRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 3),
    _AlcatelIND1SpbIPVPNRoutePrefix_Type()
)
alcatelIND1SpbIPVPNRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRoutePrefix.setStatus("current")
_AlcatelIND1SpbIPVPNRoutePrefixLen_Type = Unsigned32
_AlcatelIND1SpbIPVPNRoutePrefixLen_Object = MibTableColumn
alcatelIND1SpbIPVPNRoutePrefixLen = _AlcatelIND1SpbIPVPNRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 4),
    _AlcatelIND1SpbIPVPNRoutePrefixLen_Type()
)
alcatelIND1SpbIPVPNRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRoutePrefixLen.setStatus("current")
_AlcatelIND1SpbIPVPNRouteGateway_Type = IpAddress
_AlcatelIND1SpbIPVPNRouteGateway_Object = MibTableColumn
alcatelIND1SpbIPVPNRouteGateway = _AlcatelIND1SpbIPVPNRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 5),
    _AlcatelIND1SpbIPVPNRouteGateway_Type()
)
alcatelIND1SpbIPVPNRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteGateway.setStatus("current")
_AlcatelIND1SpbIPVPNRouteNodeName_Type = OctetString
_AlcatelIND1SpbIPVPNRouteNodeName_Object = MibTableColumn
alcatelIND1SpbIPVPNRouteNodeName = _AlcatelIND1SpbIPVPNRouteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 6),
    _AlcatelIND1SpbIPVPNRouteNodeName_Type()
)
alcatelIND1SpbIPVPNRouteNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteNodeName.setStatus("current")
_AlcatelIND1SpbIPVPNRouteMetric_Type = Unsigned32
_AlcatelIND1SpbIPVPNRouteMetric_Object = MibTableColumn
alcatelIND1SpbIPVPNRouteMetric = _AlcatelIND1SpbIPVPNRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 16, 1, 7),
    _AlcatelIND1SpbIPVPNRouteMetric_Type()
)
alcatelIND1SpbIPVPNRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRouteMetric.setStatus("current")
_AlcatelIND1SpbIPVPNRedistVrfTable_Object = MibTable
alcatelIND1SpbIPVPNRedistVrfTable = _AlcatelIND1SpbIPVPNRedistVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfTable.setStatus("current")
_AlcatelIND1SpbIPVPNRedistVrfTableEntry_Object = MibTableRow
alcatelIND1SpbIPVPNRedistVrfTableEntry = _AlcatelIND1SpbIPVPNRedistVrfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1)
)
alcatelIND1SpbIPVPNRedistVrfTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistVrfSourceVrf"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistVrfDestIsid"),
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfTableEntry.setStatus("current")
_AlcatelIND1SpbIPVPNRedistVrfTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1SpbIPVPNRedistVrfTableEntryTopIx_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx = _AlcatelIND1SpbIPVPNRedistVrfTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1, 1),
    _AlcatelIND1SpbIPVPNRedistVrfTableEntryTopIx_Type()
)
alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx.setStatus("current")


class _AlcatelIND1SpbIPVPNRedistVrfSourceVrf_Type(SnmpAdminString):
    """Custom type alcatelIND1SpbIPVPNRedistVrfSourceVrf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlcatelIND1SpbIPVPNRedistVrfSourceVrf_Type.__name__ = "SnmpAdminString"
_AlcatelIND1SpbIPVPNRedistVrfSourceVrf_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistVrfSourceVrf = _AlcatelIND1SpbIPVPNRedistVrfSourceVrf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1, 2),
    _AlcatelIND1SpbIPVPNRedistVrfSourceVrf_Type()
)
alcatelIND1SpbIPVPNRedistVrfSourceVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfSourceVrf.setStatus("current")
_AlcatelIND1SpbIPVPNRedistVrfDestIsid_Type = Unsigned32
_AlcatelIND1SpbIPVPNRedistVrfDestIsid_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistVrfDestIsid = _AlcatelIND1SpbIPVPNRedistVrfDestIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1, 3),
    _AlcatelIND1SpbIPVPNRedistVrfDestIsid_Type()
)
alcatelIND1SpbIPVPNRedistVrfDestIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfDestIsid.setStatus("current")


class _AlcatelIND1SpbIPVPNRedistVrfRouteMap_Type(SnmpAdminString):
    """Custom type alcatelIND1SpbIPVPNRedistVrfRouteMap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlcatelIND1SpbIPVPNRedistVrfRouteMap_Type.__name__ = "SnmpAdminString"
_AlcatelIND1SpbIPVPNRedistVrfRouteMap_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistVrfRouteMap = _AlcatelIND1SpbIPVPNRedistVrfRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1, 4),
    _AlcatelIND1SpbIPVPNRedistVrfRouteMap_Type()
)
alcatelIND1SpbIPVPNRedistVrfRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfRouteMap.setStatus("current")
_AlcatelIND1SpbIPVPNRedistVrfRowStatus_Type = RowStatus
_AlcatelIND1SpbIPVPNRedistVrfRowStatus_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistVrfRowStatus = _AlcatelIND1SpbIPVPNRedistVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 17, 1, 5),
    _AlcatelIND1SpbIPVPNRedistVrfRowStatus_Type()
)
alcatelIND1SpbIPVPNRedistVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistVrfRowStatus.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidTable_Object = MibTable
alcatelIND1SpbIPVPNRedistIsidTable = _AlcatelIND1SpbIPVPNRedistIsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidTable.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidTableEntry_Object = MibTableRow
alcatelIND1SpbIPVPNRedistIsidTableEntry = _AlcatelIND1SpbIPVPNRedistIsidTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1)
)
alcatelIND1SpbIPVPNRedistIsidTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistIsidSourceIsid"),
    (0, "ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistIsidDestIsid"),
)
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidTableEntry.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidTableEntryTopIx_Type = AlcatelIND1IsisSpbMTID
_AlcatelIND1SpbIPVPNRedistIsidTableEntryTopIx_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx = _AlcatelIND1SpbIPVPNRedistIsidTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1, 1),
    _AlcatelIND1SpbIPVPNRedistIsidTableEntryTopIx_Type()
)
alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidSourceIsid_Type = Unsigned32
_AlcatelIND1SpbIPVPNRedistIsidSourceIsid_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistIsidSourceIsid = _AlcatelIND1SpbIPVPNRedistIsidSourceIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1, 2),
    _AlcatelIND1SpbIPVPNRedistIsidSourceIsid_Type()
)
alcatelIND1SpbIPVPNRedistIsidSourceIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidSourceIsid.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidDestIsid_Type = Unsigned32
_AlcatelIND1SpbIPVPNRedistIsidDestIsid_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistIsidDestIsid = _AlcatelIND1SpbIPVPNRedistIsidDestIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1, 3),
    _AlcatelIND1SpbIPVPNRedistIsidDestIsid_Type()
)
alcatelIND1SpbIPVPNRedistIsidDestIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidDestIsid.setStatus("current")


class _AlcatelIND1SpbIPVPNRedistIsidRouteMap_Type(SnmpAdminString):
    """Custom type alcatelIND1SpbIPVPNRedistIsidRouteMap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlcatelIND1SpbIPVPNRedistIsidRouteMap_Type.__name__ = "SnmpAdminString"
_AlcatelIND1SpbIPVPNRedistIsidRouteMap_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistIsidRouteMap = _AlcatelIND1SpbIPVPNRedistIsidRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1, 4),
    _AlcatelIND1SpbIPVPNRedistIsidRouteMap_Type()
)
alcatelIND1SpbIPVPNRedistIsidRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidRouteMap.setStatus("current")
_AlcatelIND1SpbIPVPNRedistIsidRowStatus_Type = RowStatus
_AlcatelIND1SpbIPVPNRedistIsidRowStatus_Object = MibTableColumn
alcatelIND1SpbIPVPNRedistIsidRowStatus = _AlcatelIND1SpbIPVPNRedistIsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 1, 18, 1, 5),
    _AlcatelIND1SpbIPVPNRedistIsidRowStatus_Type()
)
alcatelIND1SpbIPVPNRedistIsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alcatelIND1SpbIPVPNRedistIsidRowStatus.setStatus("current")
_AlcatelIND1IsisSpbConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbConformance = _AlcatelIND1IsisSpbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2)
)
_AlcatelIND1IsisSpbGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbGroups = _AlcatelIND1IsisSpbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1)
)
_AlcatelIND1IsisSpbCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IsisSpbCompliances = _AlcatelIND1IsisSpbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 2)
)

# Managed Objects groups

alcatelIND1IsisSpbSysGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 1)
)
alcatelIND1IsisSpbSysGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysControlBvlan"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysAdminState"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysNumLSPs"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1isisSpbSysLastSpfRun"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysLastEnabledTime"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysOverloadStatus"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysOverloadOnBootTimeout"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysOverloadOnBoot"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysOverloadTimeout"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysSetOverload"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1isisSpbSysLastSpfRunTimeStamp"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysLastEnabledTimeStamp"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysGroupSPBM.setStatus("current")

alcatelIND1IsisSpbProtocolConfigGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 2)
)
alcatelIND1IsisSpbProtocolConfigGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolSpfMaxWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolSpfInitialWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolSpfSecondWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolLspMaxWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolLspInitialWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolLspSecondWait"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolGracefulRestart"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbProtocolGRHelperMode"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbProtocolConfigGroupSPBM.setStatus("current")

alcatelIND1IsisSpbAdjStaticEntryConfigGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 3)
)
alcatelIND1IsisSpbAdjStaticEntryConfigGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryHelloInterval"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryIfAdminState"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryMetric"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryRowStatus"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryEctAlgorithm"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryRowStatus"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbvEctStaticEntrySpvid"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjStaticEntryConfigGroupSPBM.setStatus("current")

alcatelIND1IsisSpbSysConfigGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 4)
)
alcatelIND1IsisSpbSysConfigGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysAreaAddress"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysBridgePriority"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysControlAddr"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysDigestConvention"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysId"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbmSysMode"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbmSysSPSourceId"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbvSysMode"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSysConfigGroupSPBM.setStatus("current")

alcatelIND1IsisSpbAdjGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 5)
)
alcatelIND1IsisSpbAdjGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryAdjState"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryHoldTimer"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryNeighPriority"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryPeerSysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryRestartStatus"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryRestartSupport"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryCircuitId"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryIfOperState"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryMulticastMode"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjStaticEntryAFDConfig"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbAdjGroupSPBM.setStatus("current")

alcatelIND1IsisSpbIngressMacGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 6)
)
alcatelIND1IsisSpbIngressMacGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbIngressMacSysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbIngressMacIfIndex"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbIngressMacGroupSPBM.setStatus("current")

alcatelIND1IsisSpbLSPGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 7)
)
alcatelIND1IsisSpbLSPGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPAllocLen"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPAttributes"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPBuff"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPChecksum"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPLifetimeRemain"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPMaxArea"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPPktType"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPPktVersion"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPSeq"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPSysIdLen"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPUsedLen"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbLSPVersion"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbLSPGroupSPBM.setStatus("current")

alcatelIND1IsisSpbMulticastSourceGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 8)
)
alcatelIND1IsisSpbMulticastSourceGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceReachable"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastSourceSysName"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastSourceGroupSPBM.setStatus("current")

alcatelIND1IsisSpbMulticastTableEntryGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 9)
)
alcatelIND1IsisSpbMulticastTableEntryGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntryIsid"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntrySysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbMulticastTableEntrySrcMac"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbMulticastTableEntryGroupSPBM.setStatus("current")

alcatelIND1IsisSpbServiceTableEntryGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 10)
)
alcatelIND1IsisSpbServiceTableEntryGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntryIsidFlags"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbServiceTableEntrySysName"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbServiceTableEntryGroupSPBM.setStatus("current")

alcatelIND1IsisSpbSpfGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 11)
)
alcatelIND1IsisSpbSpfGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfHopCount"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfMetric"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfNextHopSysName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfNextHopSysMac"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfIfIndex"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbSpfSysName"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbSpfGroupSPBM.setStatus("current")

alcatelIND1IsisSpbUnicastGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 12)
)
alcatelIND1IsisSpbUnicastGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbUnicastOutboundIfIndex"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbUnicastSysName"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbUnicastGroupSPBM.setStatus("current")

alcatelIND1IsisSpbNodeGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 13)
)
alcatelIND1IsisSpbNodeGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbNodeBridgePriority"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbNodeSPSourceId"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1IsisSpbNodeSysName"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbNodeGroupSPBM.setStatus("current")

alcatelIND1IsisSpbVPNBindTableGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 14)
)
alcatelIND1IsisSpbVPNBindTableGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindImportRouteMap"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNBindRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbVPNBindTableGroupSPBM.setStatus("current")

alcatelIND1IsisSpbVPNRouteTableGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 15)
)
alcatelIND1IsisSpbVPNRouteTableGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRouteNodeName"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRouteMetric"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbVPNRouteTableGroupSPBM.setStatus("current")

alcatelIND1IsisSpbVPNRedistVrfTableGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 16)
)
alcatelIND1IsisSpbVPNRedistVrfTableGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistVrfRouteMap"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistVrfRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbVPNRedistVrfTableGroupSPBM.setStatus("current")

alcatelIND1IsisSpbVPNRedistIsidTableGroupSPBM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 1, 17)
)
alcatelIND1IsisSpbVPNRedistIsidTableGroupSPBM.setObjects(
      *(("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistIsidRouteMap"),
        ("ALCATEL-IND1-ISIS-SPB-MIB", "alcatelIND1SpbIPVPNRedistIsidRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbVPNRedistIsidTableGroupSPBM.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1IsisSpbComplianceSPBM = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IsisSpbComplianceSPBM.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-ISIS-SPB-MIB",
    **{"AlcatelIND1IsisSpbAreaAddress": AlcatelIND1IsisSpbAreaAddress,
       "AlcatelIND1IsisSpbSystemName": AlcatelIND1IsisSpbSystemName,
       "AlcatelIND1IsisSpbEctAlgorithm": AlcatelIND1IsisSpbEctAlgorithm,
       "AlcatelIND1IsisSpbMode": AlcatelIND1IsisSpbMode,
       "AlcatelIND1IsisSpbDigestConvention": AlcatelIND1IsisSpbDigestConvention,
       "AlcatelIND1IsisSpbLinkMetric": AlcatelIND1IsisSpbLinkMetric,
       "AlcatelIND1IsisSpbAdjState": AlcatelIND1IsisSpbAdjState,
       "AlcatelIND1IsisSpbmSPsourceId": AlcatelIND1IsisSpbmSPsourceId,
       "AlcatelIND1IsisSpbBridgePriority": AlcatelIND1IsisSpbBridgePriority,
       "AlcatelIND1IsisSpbMTID": AlcatelIND1IsisSpbMTID,
       "AlcatelIND1IsisSpbmMulticastMode": AlcatelIND1IsisSpbmMulticastMode,
       "AlcatelIND1IsisSpbIfOperState": AlcatelIND1IsisSpbIfOperState,
       "AlcatelSpbServiceIdentifier": AlcatelSpbServiceIdentifier,
       "AlcatelIND1IsisSpbmIsidFlags": AlcatelIND1IsisSpbmIsidFlags,
       "alcatelIND1IsisSpbMib": alcatelIND1IsisSpbMib,
       "alcatelIND1IsisSpbMibObjects": alcatelIND1IsisSpbMibObjects,
       "alcatelIND1IsisSpbSys": alcatelIND1IsisSpbSys,
       "alcatelIND1IsisSpbSysControlBvlan": alcatelIND1IsisSpbSysControlBvlan,
       "alcatelIND1IsisSpbSysAdminState": alcatelIND1IsisSpbSysAdminState,
       "alcatelIND1IsisSpbSysAreaAddress": alcatelIND1IsisSpbSysAreaAddress,
       "alcatelIND1IsisSpbSysId": alcatelIND1IsisSpbSysId,
       "alcatelIND1IsisSpbSysControlAddr": alcatelIND1IsisSpbSysControlAddr,
       "alcatelIND1IsisSpbSysName": alcatelIND1IsisSpbSysName,
       "alcatelIND1IsisSpbSysBridgePriority": alcatelIND1IsisSpbSysBridgePriority,
       "alcatelIND1IsisSpbmSysSPSourceId": alcatelIND1IsisSpbmSysSPSourceId,
       "alcatelIND1IsisSpbvSysMode": alcatelIND1IsisSpbvSysMode,
       "alcatelIND1IsisSpbmSysMode": alcatelIND1IsisSpbmSysMode,
       "alcatelIND1IsisSpbSysDigestConvention": alcatelIND1IsisSpbSysDigestConvention,
       "alcatelIND1IsisSpbSysSetOverload": alcatelIND1IsisSpbSysSetOverload,
       "alcatelIND1IsisSpbSysOverloadTimeout": alcatelIND1IsisSpbSysOverloadTimeout,
       "alcatelIND1IsisSpbSysOverloadOnBoot": alcatelIND1IsisSpbSysOverloadOnBoot,
       "alcatelIND1IsisSpbSysOverloadOnBootTimeout": alcatelIND1IsisSpbSysOverloadOnBootTimeout,
       "alcatelIND1IsisSpbSysOverloadStatus": alcatelIND1IsisSpbSysOverloadStatus,
       "alcatelIND1IsisSpbSysLastEnabledTime": alcatelIND1IsisSpbSysLastEnabledTime,
       "alcatelIND1isisSpbSysLastSpfRun": alcatelIND1isisSpbSysLastSpfRun,
       "alcatelIND1IsisSpbSysNumLSPs": alcatelIND1IsisSpbSysNumLSPs,
       "alcatelIND1IsisSpbSysLastEnabledTimeStamp": alcatelIND1IsisSpbSysLastEnabledTimeStamp,
       "alcatelIND1isisSpbSysLastSpfRunTimeStamp": alcatelIND1isisSpbSysLastSpfRunTimeStamp,
       "alcatelIND1IsisSpbProtocolConfig": alcatelIND1IsisSpbProtocolConfig,
       "alcatelIND1IsisSpbProtocolSpfMaxWait": alcatelIND1IsisSpbProtocolSpfMaxWait,
       "alcatelIND1IsisSpbProtocolSpfInitialWait": alcatelIND1IsisSpbProtocolSpfInitialWait,
       "alcatelIND1IsisSpbProtocolSpfSecondWait": alcatelIND1IsisSpbProtocolSpfSecondWait,
       "alcatelIND1IsisSpbProtocolLspMaxWait": alcatelIND1IsisSpbProtocolLspMaxWait,
       "alcatelIND1IsisSpbProtocolLspInitialWait": alcatelIND1IsisSpbProtocolLspInitialWait,
       "alcatelIND1IsisSpbProtocolLspSecondWait": alcatelIND1IsisSpbProtocolLspSecondWait,
       "alcatelIND1IsisSpbProtocolGracefulRestart": alcatelIND1IsisSpbProtocolGracefulRestart,
       "alcatelIND1IsisSpbProtocolGRHelperMode": alcatelIND1IsisSpbProtocolGRHelperMode,
       "alcatelIND1IsisSpbAdjStaticTable": alcatelIND1IsisSpbAdjStaticTable,
       "alcatelIND1IsisSpbAdjStaticTableEntry": alcatelIND1IsisSpbAdjStaticTableEntry,
       "alcatelIND1IsisSpbAdjStaticEntryTopIx": alcatelIND1IsisSpbAdjStaticEntryTopIx,
       "alcatelIND1IsisSpbAdjStaticEntryIfIndex": alcatelIND1IsisSpbAdjStaticEntryIfIndex,
       "alcatelIND1IsisSpbAdjStaticEntryMetric": alcatelIND1IsisSpbAdjStaticEntryMetric,
       "alcatelIND1IsisSpbAdjStaticEntryHelloInterval": alcatelIND1IsisSpbAdjStaticEntryHelloInterval,
       "alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier": alcatelIND1IsisSpbAdjStaticEntryHelloMultiplier,
       "alcatelIND1IsisSpbAdjStaticEntryIfAdminState": alcatelIND1IsisSpbAdjStaticEntryIfAdminState,
       "alcatelIND1IsisSpbAdjStaticEntryRowStatus": alcatelIND1IsisSpbAdjStaticEntryRowStatus,
       "alcatelIND1IsisSpbAdjStaticEntryCircuitId": alcatelIND1IsisSpbAdjStaticEntryCircuitId,
       "alcatelIND1IsisSpbAdjStaticEntryIfOperState": alcatelIND1IsisSpbAdjStaticEntryIfOperState,
       "alcatelIND1IsisSpbAdjStaticEntryAFDConfig": alcatelIND1IsisSpbAdjStaticEntryAFDConfig,
       "alcatelIND1IsisSpbEctStaticTable": alcatelIND1IsisSpbEctStaticTable,
       "alcatelIND1IsisSpbEctStaticTableEntry": alcatelIND1IsisSpbEctStaticTableEntry,
       "alcatelIND1IsisSpbEctStaticEntryTopIx": alcatelIND1IsisSpbEctStaticEntryTopIx,
       "alcatelIND1IsisSpbEctStaticEntryBaseVid": alcatelIND1IsisSpbEctStaticEntryBaseVid,
       "alcatelIND1IsisSpbEctStaticEntryEctAlgorithm": alcatelIND1IsisSpbEctStaticEntryEctAlgorithm,
       "alcatelIND1IsisSpbvEctStaticEntrySpvid": alcatelIND1IsisSpbvEctStaticEntrySpvid,
       "alcatelIND1IsisSpbEctStaticEntryRowStatus": alcatelIND1IsisSpbEctStaticEntryRowStatus,
       "alcatelIND1IsisSpbEctStaticEntryMulticastMode": alcatelIND1IsisSpbEctStaticEntryMulticastMode,
       "alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName": alcatelIND1IsisSpbEctStaticEntryRootBridgeSysName,
       "alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac": alcatelIND1IsisSpbEctStaticEntryRootBridgeSysMac,
       "alcatelIND1IsisSpbAdjDynamicTable": alcatelIND1IsisSpbAdjDynamicTable,
       "alcatelIND1IsisSpbAdjDynamicEntry": alcatelIND1IsisSpbAdjDynamicEntry,
       "alcatelIND1IsisSpbAdjDynamicEntryTopIx": alcatelIND1IsisSpbAdjDynamicEntryTopIx,
       "alcatelIND1IsisSpbAdjDynamicEntryIfIndex": alcatelIND1IsisSpbAdjDynamicEntryIfIndex,
       "alcatelIND1IsisSpbAdjDynamicEntryPeerSysId": alcatelIND1IsisSpbAdjDynamicEntryPeerSysId,
       "alcatelIND1IsisSpbAdjDynamicEntryAdjState": alcatelIND1IsisSpbAdjDynamicEntryAdjState,
       "alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime": alcatelIND1IsisSpbAdjDynamicEntryAdjUpTime,
       "alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining": alcatelIND1IsisSpbAdjDynamicEntryHoldRemaining,
       "alcatelIND1IsisSpbAdjDynamicEntryHoldTimer": alcatelIND1IsisSpbAdjDynamicEntryHoldTimer,
       "alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId": alcatelIND1IsisSpbAdjDynamicEntryNbrExtLocalCircuitId,
       "alcatelIND1IsisSpbAdjDynamicEntryNeighPriority": alcatelIND1IsisSpbAdjDynamicEntryNeighPriority,
       "alcatelIND1IsisSpbAdjDynamicEntryPeerSysName": alcatelIND1IsisSpbAdjDynamicEntryPeerSysName,
       "alcatelIND1IsisSpbAdjDynamicEntryRestartStatus": alcatelIND1IsisSpbAdjDynamicEntryRestartStatus,
       "alcatelIND1IsisSpbAdjDynamicEntryRestartSupport": alcatelIND1IsisSpbAdjDynamicEntryRestartSupport,
       "alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed": alcatelIND1IsisSpbAdjDynamicEntryRestartSuppressed,
       "alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp": alcatelIND1IsisSpbAdjDynamicEntryAdjUpTimeStamp,
       "alcatelIND1IsisSpbNodeTable": alcatelIND1IsisSpbNodeTable,
       "alcatelIND1IsisSpbNodeTableEntry": alcatelIND1IsisSpbNodeTableEntry,
       "alcatelIND1IsisSpbNodeTopIx": alcatelIND1IsisSpbNodeTopIx,
       "alcatelIND1IsisSpbNodeSysId": alcatelIND1IsisSpbNodeSysId,
       "alcatelIND1IsisSpbNodeSysName": alcatelIND1IsisSpbNodeSysName,
       "alcatelIND1IsisSpbNodeSPSourceId": alcatelIND1IsisSpbNodeSPSourceId,
       "alcatelIND1IsisSpbNodeBridgePriority": alcatelIND1IsisSpbNodeBridgePriority,
       "alcatelIND1IsisSpbUnicastTable": alcatelIND1IsisSpbUnicastTable,
       "alcatelIND1IsisSpbUnicastTableEntry": alcatelIND1IsisSpbUnicastTableEntry,
       "alcatelIND1IsisSpbUnicastTopIx": alcatelIND1IsisSpbUnicastTopIx,
       "alcatelIND1IsisSpbUnicastBvlan": alcatelIND1IsisSpbUnicastBvlan,
       "alcatelIND1IsisSpbUnicastSysMac": alcatelIND1IsisSpbUnicastSysMac,
       "alcatelIND1IsisSpbUnicastSysName": alcatelIND1IsisSpbUnicastSysName,
       "alcatelIND1IsisSpbUnicastOutboundIfIndex": alcatelIND1IsisSpbUnicastOutboundIfIndex,
       "alcatelIND1IsisSpbMulticastTable": alcatelIND1IsisSpbMulticastTable,
       "alcatelIND1IsisSpbMulticastTableEntry": alcatelIND1IsisSpbMulticastTableEntry,
       "alcatelIND1IsisSpbMulticastTableEntryTopIx": alcatelIND1IsisSpbMulticastTableEntryTopIx,
       "alcatelIND1IsisSpbMulticastTableEntryBvlan": alcatelIND1IsisSpbMulticastTableEntryBvlan,
       "alcatelIND1IsisSpbMulticastTableEntryMulticastMac": alcatelIND1IsisSpbMulticastTableEntryMulticastMac,
       "alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound": alcatelIND1IsisSpbMulticastTableEntryIfIndexOutbound,
       "alcatelIND1IsisSpbMulticastTableEntrySrcMac": alcatelIND1IsisSpbMulticastTableEntrySrcMac,
       "alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound": alcatelIND1IsisSpbMulticastTableEntryIfIndexInbound,
       "alcatelIND1IsisSpbMulticastTableEntrySysName": alcatelIND1IsisSpbMulticastTableEntrySysName,
       "alcatelIND1IsisSpbMulticastTableEntryIsid": alcatelIND1IsisSpbMulticastTableEntryIsid,
       "alcatelIND1IsisSpbLSPTable": alcatelIND1IsisSpbLSPTable,
       "alcatelIND1IsisSpbLSPEntry": alcatelIND1IsisSpbLSPEntry,
       "alcatelIND1IsisSpbLSPTopIx": alcatelIND1IsisSpbLSPTopIx,
       "alcatelIND1IsisSpbLSPId": alcatelIND1IsisSpbLSPId,
       "alcatelIND1IsisSpbLSPSeq": alcatelIND1IsisSpbLSPSeq,
       "alcatelIND1IsisSpbLSPChecksum": alcatelIND1IsisSpbLSPChecksum,
       "alcatelIND1IsisSpbLSPLifetimeRemain": alcatelIND1IsisSpbLSPLifetimeRemain,
       "alcatelIND1IsisSpbLSPVersion": alcatelIND1IsisSpbLSPVersion,
       "alcatelIND1IsisSpbLSPPktType": alcatelIND1IsisSpbLSPPktType,
       "alcatelIND1IsisSpbLSPPktVersion": alcatelIND1IsisSpbLSPPktVersion,
       "alcatelIND1IsisSpbLSPMaxArea": alcatelIND1IsisSpbLSPMaxArea,
       "alcatelIND1IsisSpbLSPSysIdLen": alcatelIND1IsisSpbLSPSysIdLen,
       "alcatelIND1IsisSpbLSPAttributes": alcatelIND1IsisSpbLSPAttributes,
       "alcatelIND1IsisSpbLSPUsedLen": alcatelIND1IsisSpbLSPUsedLen,
       "alcatelIND1IsisSpbLSPAllocLen": alcatelIND1IsisSpbLSPAllocLen,
       "alcatelIND1IsisSpbLSPBuff": alcatelIND1IsisSpbLSPBuff,
       "alcatelIND1IsisSpbMulticastSourceTable": alcatelIND1IsisSpbMulticastSourceTable,
       "alcatelIND1IsisSpbMulticastSourceEntry": alcatelIND1IsisSpbMulticastSourceEntry,
       "alcatelIND1IsisSpbMulticastSourceTopIx": alcatelIND1IsisSpbMulticastSourceTopIx,
       "alcatelIND1IsisSpbMulticastSourceSysMac": alcatelIND1IsisSpbMulticastSourceSysMac,
       "alcatelIND1IsisSpbMulticastSourceBvlan": alcatelIND1IsisSpbMulticastSourceBvlan,
       "alcatelIND1IsisSpbMulticastSourceSysName": alcatelIND1IsisSpbMulticastSourceSysName,
       "alcatelIND1IsisSpbMulticastSourceReachable": alcatelIND1IsisSpbMulticastSourceReachable,
       "alcatelIND1IsisSpbSpfTable": alcatelIND1IsisSpbSpfTable,
       "alcatelIND1IsisSpbSpfTableEntry": alcatelIND1IsisSpbSpfTableEntry,
       "alcatelIND1IsisSpbSpfBvlan": alcatelIND1IsisSpbSpfBvlan,
       "alcatelIND1IsisSpbSpfSysMac": alcatelIND1IsisSpbSpfSysMac,
       "alcatelIND1IsisSpbSpfSysName": alcatelIND1IsisSpbSpfSysName,
       "alcatelIND1IsisSpbSpfIfIndex": alcatelIND1IsisSpbSpfIfIndex,
       "alcatelIND1IsisSpbSpfNextHopSysMac": alcatelIND1IsisSpbSpfNextHopSysMac,
       "alcatelIND1IsisSpbSpfNextHopSysName": alcatelIND1IsisSpbSpfNextHopSysName,
       "alcatelIND1IsisSpbSpfMetric": alcatelIND1IsisSpbSpfMetric,
       "alcatelIND1IsisSpbSpfHopCount": alcatelIND1IsisSpbSpfHopCount,
       "alcatelIND1IsisSpbMulticastSourceSpfTable": alcatelIND1IsisSpbMulticastSourceSpfTable,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntry": alcatelIND1IsisSpbMulticastSourceSpfTableEntry,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx": alcatelIND1IsisSpbMulticastSourceSpfTableEntryTopIx,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac": alcatelIND1IsisSpbMulticastSourceSpfTableEntryBMac,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan": alcatelIND1IsisSpbMulticastSourceSpfTableEntryBvlan,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac": alcatelIND1IsisSpbMulticastSourceSpfTableEntryDestMac,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex": alcatelIND1IsisSpbMulticastSourceSpfTableEntryIfIndex,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName": alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopName,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac": alcatelIND1IsisSpbMulticastSourceSpfTableEntryNHopMac,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric": alcatelIND1IsisSpbMulticastSourceSpfTableEntryMetric,
       "alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount": alcatelIND1IsisSpbMulticastSourceSpfTableEntryHopCount,
       "alcatelIND1IsisSpbIngressMacFilterTable": alcatelIND1IsisSpbIngressMacFilterTable,
       "alcatelIND1IsisSpbIngressMacFilterEntry": alcatelIND1IsisSpbIngressMacFilterEntry,
       "alcatelIND1IsisSpbIngressMacBvlan": alcatelIND1IsisSpbIngressMacBvlan,
       "alcatelIND1IsisSpbIngressMacSysMac": alcatelIND1IsisSpbIngressMacSysMac,
       "alcatelIND1IsisSpbIngressMacSysName": alcatelIND1IsisSpbIngressMacSysName,
       "alcatelIND1IsisSpbIngressMacIfIndex": alcatelIND1IsisSpbIngressMacIfIndex,
       "alcatelIND1IsisSpbServiceTable": alcatelIND1IsisSpbServiceTable,
       "alcatelIND1IsisSpbServiceTableEntry": alcatelIND1IsisSpbServiceTableEntry,
       "alcatelIND1IsisSpbServiceTableEntryTopIx": alcatelIND1IsisSpbServiceTableEntryTopIx,
       "alcatelIND1IsisSpbServiceTableEntryBvlan": alcatelIND1IsisSpbServiceTableEntryBvlan,
       "alcatelIND1IsisSpbServiceTableEntryIsid": alcatelIND1IsisSpbServiceTableEntryIsid,
       "alcatelIND1IsisSpbServiceTableEntrySysMac": alcatelIND1IsisSpbServiceTableEntrySysMac,
       "alcatelIND1IsisSpbServiceTableEntrySysName": alcatelIND1IsisSpbServiceTableEntrySysName,
       "alcatelIND1IsisSpbServiceTableEntryIsidFlags": alcatelIND1IsisSpbServiceTableEntryIsidFlags,
       "alcatelIND1SpbIPVPNBindTable": alcatelIND1SpbIPVPNBindTable,
       "alcatelIND1SpbIPVPNBindTableEntry": alcatelIND1SpbIPVPNBindTableEntry,
       "alcatelIND1SpbIPVPNBindTableEntryTopIx": alcatelIND1SpbIPVPNBindTableEntryTopIx,
       "alcatelIND1SpbIPVPNBindVrfName": alcatelIND1SpbIPVPNBindVrfName,
       "alcatelIND1SpbIPVPNBindIsid": alcatelIND1SpbIPVPNBindIsid,
       "alcatelIND1SpbIPVPNBindGateway": alcatelIND1SpbIPVPNBindGateway,
       "alcatelIND1SpbIPVPNBindImportRouteMap": alcatelIND1SpbIPVPNBindImportRouteMap,
       "alcatelIND1SpbIPVPNBindRowStatus": alcatelIND1SpbIPVPNBindRowStatus,
       "alcatelIND1SpbIPVPNRouteTable": alcatelIND1SpbIPVPNRouteTable,
       "alcatelIND1SpbIPVPNRouteTableEntry": alcatelIND1SpbIPVPNRouteTableEntry,
       "alcatelIND1SpbIPVPNRouteTableEntryTopIx": alcatelIND1SpbIPVPNRouteTableEntryTopIx,
       "alcatelIND1SpbIPVPNRouteIsid": alcatelIND1SpbIPVPNRouteIsid,
       "alcatelIND1SpbIPVPNRoutePrefix": alcatelIND1SpbIPVPNRoutePrefix,
       "alcatelIND1SpbIPVPNRoutePrefixLen": alcatelIND1SpbIPVPNRoutePrefixLen,
       "alcatelIND1SpbIPVPNRouteGateway": alcatelIND1SpbIPVPNRouteGateway,
       "alcatelIND1SpbIPVPNRouteNodeName": alcatelIND1SpbIPVPNRouteNodeName,
       "alcatelIND1SpbIPVPNRouteMetric": alcatelIND1SpbIPVPNRouteMetric,
       "alcatelIND1SpbIPVPNRedistVrfTable": alcatelIND1SpbIPVPNRedistVrfTable,
       "alcatelIND1SpbIPVPNRedistVrfTableEntry": alcatelIND1SpbIPVPNRedistVrfTableEntry,
       "alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx": alcatelIND1SpbIPVPNRedistVrfTableEntryTopIx,
       "alcatelIND1SpbIPVPNRedistVrfSourceVrf": alcatelIND1SpbIPVPNRedistVrfSourceVrf,
       "alcatelIND1SpbIPVPNRedistVrfDestIsid": alcatelIND1SpbIPVPNRedistVrfDestIsid,
       "alcatelIND1SpbIPVPNRedistVrfRouteMap": alcatelIND1SpbIPVPNRedistVrfRouteMap,
       "alcatelIND1SpbIPVPNRedistVrfRowStatus": alcatelIND1SpbIPVPNRedistVrfRowStatus,
       "alcatelIND1SpbIPVPNRedistIsidTable": alcatelIND1SpbIPVPNRedistIsidTable,
       "alcatelIND1SpbIPVPNRedistIsidTableEntry": alcatelIND1SpbIPVPNRedistIsidTableEntry,
       "alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx": alcatelIND1SpbIPVPNRedistIsidTableEntryTopIx,
       "alcatelIND1SpbIPVPNRedistIsidSourceIsid": alcatelIND1SpbIPVPNRedistIsidSourceIsid,
       "alcatelIND1SpbIPVPNRedistIsidDestIsid": alcatelIND1SpbIPVPNRedistIsidDestIsid,
       "alcatelIND1SpbIPVPNRedistIsidRouteMap": alcatelIND1SpbIPVPNRedistIsidRouteMap,
       "alcatelIND1SpbIPVPNRedistIsidRowStatus": alcatelIND1SpbIPVPNRedistIsidRowStatus,
       "alcatelIND1IsisSpbConformance": alcatelIND1IsisSpbConformance,
       "alcatelIND1IsisSpbGroups": alcatelIND1IsisSpbGroups,
       "alcatelIND1IsisSpbSysGroupSPBM": alcatelIND1IsisSpbSysGroupSPBM,
       "alcatelIND1IsisSpbProtocolConfigGroupSPBM": alcatelIND1IsisSpbProtocolConfigGroupSPBM,
       "alcatelIND1IsisSpbAdjStaticEntryConfigGroupSPBM": alcatelIND1IsisSpbAdjStaticEntryConfigGroupSPBM,
       "alcatelIND1IsisSpbSysConfigGroupSPBM": alcatelIND1IsisSpbSysConfigGroupSPBM,
       "alcatelIND1IsisSpbAdjGroupSPBM": alcatelIND1IsisSpbAdjGroupSPBM,
       "alcatelIND1IsisSpbIngressMacGroupSPBM": alcatelIND1IsisSpbIngressMacGroupSPBM,
       "alcatelIND1IsisSpbLSPGroupSPBM": alcatelIND1IsisSpbLSPGroupSPBM,
       "alcatelIND1IsisSpbMulticastSourceGroupSPBM": alcatelIND1IsisSpbMulticastSourceGroupSPBM,
       "alcatelIND1IsisSpbMulticastTableEntryGroupSPBM": alcatelIND1IsisSpbMulticastTableEntryGroupSPBM,
       "alcatelIND1IsisSpbServiceTableEntryGroupSPBM": alcatelIND1IsisSpbServiceTableEntryGroupSPBM,
       "alcatelIND1IsisSpbSpfGroupSPBM": alcatelIND1IsisSpbSpfGroupSPBM,
       "alcatelIND1IsisSpbUnicastGroupSPBM": alcatelIND1IsisSpbUnicastGroupSPBM,
       "alcatelIND1IsisSpbNodeGroupSPBM": alcatelIND1IsisSpbNodeGroupSPBM,
       "alcatelIND1IsisSpbVPNBindTableGroupSPBM": alcatelIND1IsisSpbVPNBindTableGroupSPBM,
       "alcatelIND1IsisSpbVPNRouteTableGroupSPBM": alcatelIND1IsisSpbVPNRouteTableGroupSPBM,
       "alcatelIND1IsisSpbVPNRedistVrfTableGroupSPBM": alcatelIND1IsisSpbVPNRedistVrfTableGroupSPBM,
       "alcatelIND1IsisSpbVPNRedistIsidTableGroupSPBM": alcatelIND1IsisSpbVPNRedistIsidTableGroupSPBM,
       "alcatelIND1IsisSpbCompliances": alcatelIND1IsisSpbCompliances,
       "alcatelIND1IsisSpbComplianceSPBM": alcatelIND1IsisSpbComplianceSPBM}
)
