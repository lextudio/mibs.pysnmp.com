# SNMP MIB module (TIMETRA-SAS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:45 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxLEDState,
 TmnxSlotNumOrZero,
 tmnxCardEntry,
 tmnxChassisEntry,
 tmnxChassisFanEntry,
 tmnxChassisIndex,
 tmnxChassisNotifyHwIndex,
 tmnxChassisPowerSupplyEntry,
 tmnxChassisPowerSupplyInputStatus,
 tmnxChassisPowerSupplyOutputStatus,
 tmnxCpmCardEntry,
 tmnxHwClass,
 tmnxHwEntry,
 tmnxHwID,
 tmnxHwName,
 tmnxHwOperState,
 tmnxHwTemperature) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxLEDState",
    "TmnxSlotNumOrZero",
    "tmnxCardEntry",
    "tmnxChassisEntry",
    "tmnxChassisFanEntry",
    "tmnxChassisIndex",
    "tmnxChassisNotifyHwIndex",
    "tmnxChassisPowerSupplyEntry",
    "tmnxChassisPowerSupplyInputStatus",
    "tmnxChassisPowerSupplyOutputStatus",
    "tmnxCpmCardEntry",
    "tmnxHwClass",
    "tmnxHwEntry",
    "tmnxHwID",
    "tmnxHwName",
    "tmnxHwOperState",
    "tmnxHwTemperature")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(IpAddressPrefixLength,
 ServiceOperStatus,
 TBurstSize,
 TCIRRate,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPolicyID,
 TSysResource,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperGrpHoldDownTime,
 TmnxOperGrpHoldUpTime,
 TmnxOperState,
 TmnxPortID,
 TmnxVwmCardType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "ServiceOperStatus",
    "TBurstSize",
    "TCIRRate",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPolicyID",
    "TSysResource",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperGrpHoldDownTime",
    "TmnxOperGrpHoldUpTime",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxVwmCardType")


# MODULE-IDENTITY

timetraSASysMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 7)
)
timetraSASysMIBModule.setRevisions(
        ("1908-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxFanCfgMode(Integer32, TextualConvention):
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
        *(("auto", 3),
          ("off", 2),
          ("on", 1))
    )



class TmnxPtpTime(Integer32, TextualConvention):
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
        *(("noPtpTime", 0),
          ("oam", 2),
          ("system", 1))
    )



class TmnxSysOperGrpCreationOrigin(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("mvrp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSASSysConformance_ObjectIdentity = ObjectIdentity
tmnxSASSysConformance = _TmnxSASSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3)
)
_TmnxSASSysCompliances_ObjectIdentity = ObjectIdentity
tmnxSASSysCompliances = _TmnxSASSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 1)
)
_TmnxSASSysGroups_ObjectIdentity = ObjectIdentity
tmnxSASSysGroups = _TmnxSASSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2)
)
_TmnxSASSysSecConformance_ObjectIdentity = ObjectIdentity
tmnxSASSysSecConformance = _TmnxSASSysSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 4)
)
_TmnxSASSysSecGroups_ObjectIdentity = ObjectIdentity
tmnxSASSysSecGroups = _TmnxSASSysSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 4, 1)
)
_TmnxSASChassisGroups_ObjectIdentity = ObjectIdentity
tmnxSASChassisGroups = _TmnxSASChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 10)
)
_TmnxSASSysObjs_ObjectIdentity = ObjectIdentity
tmnxSASSysObjs = _TmnxSASSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5)
)
_SysSASBofInfo_ObjectIdentity = ObjectIdentity
sysSASBofInfo = _SysSASBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11)
)
_SbiUplinkAPort_Type = InterfaceIndexOrZero
_SbiUplinkAPort_Object = MibScalar
sbiUplinkAPort = _SbiUplinkAPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 1),
    _SbiUplinkAPort_Type()
)
sbiUplinkAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAPort.setStatus("current")
_SbiUplinkAIpAddr_Type = IpAddress
_SbiUplinkAIpAddr_Object = MibScalar
sbiUplinkAIpAddr = _SbiUplinkAIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 2),
    _SbiUplinkAIpAddr_Type()
)
sbiUplinkAIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAIpAddr.setStatus("current")


class _SbiUplinkAMask_Type(IpAddressPrefixLength):
    """Custom type sbiUplinkAMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiUplinkAMask_Object = MibScalar
sbiUplinkAMask = _SbiUplinkAMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 3),
    _SbiUplinkAMask_Type()
)
sbiUplinkAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAMask.setStatus("current")


class _SbiUplinkAVlan_Type(Integer32):
    """Custom type sbiUplinkAVlan based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_SbiUplinkAVlan_Type.__name__ = "Integer32"
_SbiUplinkAVlan_Object = MibScalar
sbiUplinkAVlan = _SbiUplinkAVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 5),
    _SbiUplinkAVlan_Type()
)
sbiUplinkAVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAVlan.setStatus("current")
_SbiUplinkBPort_Type = InterfaceIndexOrZero
_SbiUplinkBPort_Object = MibScalar
sbiUplinkBPort = _SbiUplinkBPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 6),
    _SbiUplinkBPort_Type()
)
sbiUplinkBPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBPort.setStatus("current")
_SbiUplinkBIpAddr_Type = IpAddress
_SbiUplinkBIpAddr_Object = MibScalar
sbiUplinkBIpAddr = _SbiUplinkBIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 7),
    _SbiUplinkBIpAddr_Type()
)
sbiUplinkBIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBIpAddr.setStatus("current")


class _SbiUplinkBMask_Type(IpAddressPrefixLength):
    """Custom type sbiUplinkBMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiUplinkBMask_Object = MibScalar
sbiUplinkBMask = _SbiUplinkBMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 8),
    _SbiUplinkBMask_Type()
)
sbiUplinkBMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBMask.setStatus("current")


class _SbiUplinkBVlan_Type(Integer32):
    """Custom type sbiUplinkBVlan based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_SbiUplinkBVlan_Type.__name__ = "Integer32"
_SbiUplinkBVlan_Object = MibScalar
sbiUplinkBVlan = _SbiUplinkBVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 10),
    _SbiUplinkBVlan_Type()
)
sbiUplinkBVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBVlan.setStatus("current")
_SbiPingAddress_Type = IpAddress
_SbiPingAddress_Object = MibScalar
sbiPingAddress = _SbiPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 11),
    _SbiPingAddress_Type()
)
sbiPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPingAddress.setStatus("current")
_SbiUplinkRouteTable_Object = MibTable
sbiUplinkRouteTable = _SbiUplinkRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12)
)
if mibBuilder.loadTexts:
    sbiUplinkRouteTable.setStatus("current")
_SbiUplinkRouteEntry_Object = MibTableRow
sbiUplinkRouteEntry = _SbiUplinkRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1)
)
sbiUplinkRouteEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAorB"),
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteDest"),
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteMask"),
)
if mibBuilder.loadTexts:
    sbiUplinkRouteEntry.setStatus("current")


class _SbiUplinkAorB_Type(Unsigned32):
    """Custom type sbiUplinkAorB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SbiUplinkAorB_Type.__name__ = "Unsigned32"
_SbiUplinkAorB_Object = MibTableColumn
sbiUplinkAorB = _SbiUplinkAorB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1, 1),
    _SbiUplinkAorB_Type()
)
sbiUplinkAorB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiUplinkAorB.setStatus("current")
_SbiUplinkRouteDest_Type = IpAddress
_SbiUplinkRouteDest_Object = MibTableColumn
sbiUplinkRouteDest = _SbiUplinkRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1, 2),
    _SbiUplinkRouteDest_Type()
)
sbiUplinkRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiUplinkRouteDest.setStatus("current")
_SbiUplinkRouteMask_Type = IpAddressPrefixLength
_SbiUplinkRouteMask_Object = MibTableColumn
sbiUplinkRouteMask = _SbiUplinkRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1, 3),
    _SbiUplinkRouteMask_Type()
)
sbiUplinkRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiUplinkRouteMask.setStatus("current")
_SbiUplinkRouteNextHop_Type = IpAddress
_SbiUplinkRouteNextHop_Object = MibTableColumn
sbiUplinkRouteNextHop = _SbiUplinkRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1, 4),
    _SbiUplinkRouteNextHop_Type()
)
sbiUplinkRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiUplinkRouteNextHop.setStatus("current")
_SbiUplinkRouteRowStatus_Type = RowStatus
_SbiUplinkRouteRowStatus_Object = MibTableColumn
sbiUplinkRouteRowStatus = _SbiUplinkRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 12, 1, 5),
    _SbiUplinkRouteRowStatus_Type()
)
sbiUplinkRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiUplinkRouteRowStatus.setStatus("current")


class _SbiNoServicePortOne_Type(InterfaceIndexOrZero):
    """Custom type sbiNoServicePortOne based on InterfaceIndexOrZero"""
    defaultValue = 0


_SbiNoServicePortOne_Object = MibScalar
sbiNoServicePortOne = _SbiNoServicePortOne_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 13),
    _SbiNoServicePortOne_Type()
)
sbiNoServicePortOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiNoServicePortOne.setStatus("current")


class _SbiNoServicePortTwo_Type(InterfaceIndexOrZero):
    """Custom type sbiNoServicePortTwo based on InterfaceIndexOrZero"""
    defaultValue = 0


_SbiNoServicePortTwo_Object = MibScalar
sbiNoServicePortTwo = _SbiNoServicePortTwo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 14),
    _SbiNoServicePortTwo_Type()
)
sbiNoServicePortTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiNoServicePortTwo.setStatus("current")


class _SbiUplinkAdminMode_Type(Integer32):
    """Custom type sbiUplinkAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access-uplink", 2),
          ("network", 1))
    )


_SbiUplinkAdminMode_Type.__name__ = "Integer32"
_SbiUplinkAdminMode_Object = MibScalar
sbiUplinkAdminMode = _SbiUplinkAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 15),
    _SbiUplinkAdminMode_Type()
)
sbiUplinkAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAdminMode.setStatus("current")


class _SbiUplinkOperMode_Type(Integer32):
    """Custom type sbiUplinkOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access-uplink", 2),
          ("network", 1))
    )


_SbiUplinkOperMode_Type.__name__ = "Integer32"
_SbiUplinkOperMode_Object = MibScalar
sbiUplinkOperMode = _SbiUplinkOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 16),
    _SbiUplinkOperMode_Type()
)
sbiUplinkOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiUplinkOperMode.setStatus("current")


class _SbiExpansionCardType_Type(Integer32):
    """Custom type sbiExpansionCardType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("m2-xfp", 2),
          ("m4-ds1-ces", 1))
    )


_SbiExpansionCardType_Type.__name__ = "Integer32"
_SbiExpansionCardType_Object = MibScalar
sbiExpansionCardType = _SbiExpansionCardType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 17),
    _SbiExpansionCardType_Type()
)
sbiExpansionCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiExpansionCardType.setStatus("current")


class _SbiConsoleDisabled_Type(TruthValue):
    """Custom type sbiConsoleDisabled based on TruthValue"""


_SbiConsoleDisabled_Object = MibScalar
sbiConsoleDisabled = _SbiConsoleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 18),
    _SbiConsoleDisabled_Type()
)
sbiConsoleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiConsoleDisabled.setStatus("current")


class _SbiPassword_Type(OctetString):
    """Custom type sbiPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SbiPassword_Type.__name__ = "OctetString"
_SbiPassword_Object = MibScalar
sbiPassword = _SbiPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 19),
    _SbiPassword_Type()
)
sbiPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPassword.setStatus("current")


class _SbiUplinkAAutoNegotiate_Type(TruthValue):
    """Custom type sbiUplinkAAutoNegotiate based on TruthValue"""


_SbiUplinkAAutoNegotiate_Object = MibScalar
sbiUplinkAAutoNegotiate = _SbiUplinkAAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 20),
    _SbiUplinkAAutoNegotiate_Type()
)
sbiUplinkAAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkAAutoNegotiate.setStatus("current")


class _SbiUplinkASpeed_Type(Unsigned32):
    """Custom type sbiUplinkASpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_SbiUplinkASpeed_Type.__name__ = "Unsigned32"
_SbiUplinkASpeed_Object = MibScalar
sbiUplinkASpeed = _SbiUplinkASpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 21),
    _SbiUplinkASpeed_Type()
)
sbiUplinkASpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkASpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiUplinkASpeed.setUnits("Mbps")


class _SbiUplinkADuplex_Type(Integer32):
    """Custom type sbiUplinkADuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SbiUplinkADuplex_Type.__name__ = "Integer32"
_SbiUplinkADuplex_Object = MibScalar
sbiUplinkADuplex = _SbiUplinkADuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 22),
    _SbiUplinkADuplex_Type()
)
sbiUplinkADuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkADuplex.setStatus("current")


class _SbiUplinkBAutoNegotiate_Type(TruthValue):
    """Custom type sbiUplinkBAutoNegotiate based on TruthValue"""


_SbiUplinkBAutoNegotiate_Object = MibScalar
sbiUplinkBAutoNegotiate = _SbiUplinkBAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 23),
    _SbiUplinkBAutoNegotiate_Type()
)
sbiUplinkBAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBAutoNegotiate.setStatus("current")


class _SbiUplinkBSpeed_Type(Unsigned32):
    """Custom type sbiUplinkBSpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_SbiUplinkBSpeed_Type.__name__ = "Unsigned32"
_SbiUplinkBSpeed_Object = MibScalar
sbiUplinkBSpeed = _SbiUplinkBSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 24),
    _SbiUplinkBSpeed_Type()
)
sbiUplinkBSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiUplinkBSpeed.setUnits("Mbps")


class _SbiUplinkBDuplex_Type(Integer32):
    """Custom type sbiUplinkBDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SbiUplinkBDuplex_Type.__name__ = "Integer32"
_SbiUplinkBDuplex_Object = MibScalar
sbiUplinkBDuplex = _SbiUplinkBDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 11, 25),
    _SbiUplinkBDuplex_Type()
)
sbiUplinkBDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiUplinkBDuplex.setStatus("current")
_SysEthMgmtBofInfo_ObjectIdentity = ObjectIdentity
sysEthMgmtBofInfo = _SysEthMgmtBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12)
)


class _SbiEthMgmtDisabled_Type(TruthValue):
    """Custom type sbiEthMgmtDisabled based on TruthValue"""


_SbiEthMgmtDisabled_Object = MibScalar
sbiEthMgmtDisabled = _SbiEthMgmtDisabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 1),
    _SbiEthMgmtDisabled_Type()
)
sbiEthMgmtDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtDisabled.setStatus("current")


class _SbiEthMgmtActiveIpAddr_Type(IpAddress):
    """Custom type sbiEthMgmtActiveIpAddr based on IpAddress"""
    defaultValue = 0


_SbiEthMgmtActiveIpAddr_Object = MibScalar
sbiEthMgmtActiveIpAddr = _SbiEthMgmtActiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 2),
    _SbiEthMgmtActiveIpAddr_Type()
)
sbiEthMgmtActiveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtActiveIpAddr.setStatus("current")


class _SbiEthMgmtActiveIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiEthMgmtActiveIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiEthMgmtActiveIpMask_Object = MibScalar
sbiEthMgmtActiveIpMask = _SbiEthMgmtActiveIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 3),
    _SbiEthMgmtActiveIpMask_Type()
)
sbiEthMgmtActiveIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtActiveIpMask.setStatus("current")


class _SbiEthMgmtAutoNegotiate_Type(TruthValue):
    """Custom type sbiEthMgmtAutoNegotiate based on TruthValue"""


_SbiEthMgmtAutoNegotiate_Object = MibScalar
sbiEthMgmtAutoNegotiate = _SbiEthMgmtAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 4),
    _SbiEthMgmtAutoNegotiate_Type()
)
sbiEthMgmtAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtAutoNegotiate.setStatus("current")


class _SbiEthMgmtSpeed_Type(Unsigned32):
    """Custom type sbiEthMgmtSpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_SbiEthMgmtSpeed_Type.__name__ = "Unsigned32"
_SbiEthMgmtSpeed_Object = MibScalar
sbiEthMgmtSpeed = _SbiEthMgmtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 5),
    _SbiEthMgmtSpeed_Type()
)
sbiEthMgmtSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiEthMgmtSpeed.setUnits("Mbps")


class _SbiEthMgmtDuplex_Type(Integer32):
    """Custom type sbiEthMgmtDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SbiEthMgmtDuplex_Type.__name__ = "Integer32"
_SbiEthMgmtDuplex_Object = MibScalar
sbiEthMgmtDuplex = _SbiEthMgmtDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 6),
    _SbiEthMgmtDuplex_Type()
)
sbiEthMgmtDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEthMgmtDuplex.setStatus("current")
_SbiEthMgmtStaticRouteTable_Object = MibTable
sbiEthMgmtStaticRouteTable = _SbiEthMgmtStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7)
)
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteTable.setStatus("current")
_SbiEthMgmtStaticRouteEntry_Object = MibTableRow
sbiEthMgmtStaticRouteEntry = _SbiEthMgmtStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7, 1)
)
sbiEthMgmtStaticRouteEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtStaticRouteDest"),
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtStaticRouteMask"),
)
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteEntry.setStatus("current")
_SbiEthMgmtStaticRouteDest_Type = IpAddress
_SbiEthMgmtStaticRouteDest_Object = MibTableColumn
sbiEthMgmtStaticRouteDest = _SbiEthMgmtStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7, 1, 1),
    _SbiEthMgmtStaticRouteDest_Type()
)
sbiEthMgmtStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteDest.setStatus("current")
_SbiEthMgmtStaticRouteMask_Type = IpAddressPrefixLength
_SbiEthMgmtStaticRouteMask_Object = MibTableColumn
sbiEthMgmtStaticRouteMask = _SbiEthMgmtStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7, 1, 2),
    _SbiEthMgmtStaticRouteMask_Type()
)
sbiEthMgmtStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteMask.setStatus("current")
_SbiEthMgmtStaticRouteNextHop_Type = IpAddress
_SbiEthMgmtStaticRouteNextHop_Object = MibTableColumn
sbiEthMgmtStaticRouteNextHop = _SbiEthMgmtStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7, 1, 3),
    _SbiEthMgmtStaticRouteNextHop_Type()
)
sbiEthMgmtStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteNextHop.setStatus("current")
_SbiEthMgmtStaticRouteRowStatus_Type = RowStatus
_SbiEthMgmtStaticRouteRowStatus_Object = MibTableColumn
sbiEthMgmtStaticRouteRowStatus = _SbiEthMgmtStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 12, 7, 1, 4),
    _SbiEthMgmtStaticRouteRowStatus_Type()
)
sbiEthMgmtStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiEthMgmtStaticRouteRowStatus.setStatus("current")
_SysMpointMgmtInfo_ObjectIdentity = ObjectIdentity
sysMpointMgmtInfo = _SysMpointMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 15)
)


class _TSASMpointBwPlcy_Type(TNamedItem):
    """Custom type tSASMpointBwPlcy based on TNamedItem"""
    defaultHexValue = ""


_TSASMpointBwPlcy_Object = MibScalar
tSASMpointBwPlcy = _TSASMpointBwPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 15, 1),
    _TSASMpointBwPlcy_Type()
)
tSASMpointBwPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASMpointBwPlcy.setStatus("current")
_SysLoopBackInfo_ObjectIdentity = ObjectIdentity
sysLoopBackInfo = _SysLoopBackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 16)
)
_SysLoopbackNoServPort_Type = TmnxPortID
_SysLoopbackNoServPort_Object = MibScalar
sysLoopbackNoServPort = _SysLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 16, 1),
    _SysLoopbackNoServPort_Type()
)
sysLoopbackNoServPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoopbackNoServPort.setStatus("current")
_SysMirrorLoopbackNoServPort_Type = TmnxPortID
_SysMirrorLoopbackNoServPort_Object = MibScalar
sysMirrorLoopbackNoServPort = _SysMirrorLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 16, 2),
    _SysMirrorLoopbackNoServPort_Type()
)
sysMirrorLoopbackNoServPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorLoopbackNoServPort.setStatus("current")
_SysTestHdNoServPort_Type = TmnxPortID
_SysTestHdNoServPort_Object = MibScalar
sysTestHdNoServPort = _SysTestHdNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 16, 3),
    _SysTestHdNoServPort_Type()
)
sysTestHdNoServPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTestHdNoServPort.setStatus("current")
_SysResourceProfInfo_ObjectIdentity = ObjectIdentity
sysResourceProfInfo = _SysResourceProfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17)
)


class _SysG8032FastFloodEnable_Type(TruthValue):
    """Custom type sysG8032FastFloodEnable based on TruthValue"""


_SysG8032FastFloodEnable_Object = MibScalar
sysG8032FastFloodEnable = _SysG8032FastFloodEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 1),
    _SysG8032FastFloodEnable_Type()
)
sysG8032FastFloodEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysG8032FastFloodEnable.setStatus("current")


class _SysResIngTcamSapIngAcl_Type(TSysResource):
    """Custom type sysResIngTcamSapIngAcl based on TSysResource"""
    defaultValue = -1


_SysResIngTcamSapIngAcl_Object = MibScalar
sysResIngTcamSapIngAcl = _SysResIngTcamSapIngAcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 2),
    _SysResIngTcamSapIngAcl_Type()
)
sysResIngTcamSapIngAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamSapIngAcl.setStatus("current")


class _SysResIngTcamIngAclMac_Type(TSysResource):
    """Custom type sysResIngTcamIngAclMac based on TSysResource"""
    defaultValue = -1


_SysResIngTcamIngAclMac_Object = MibScalar
sysResIngTcamIngAclMac = _SysResIngTcamIngAclMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 3),
    _SysResIngTcamIngAclMac_Type()
)
sysResIngTcamIngAclMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamIngAclMac.setStatus("current")


class _SysResIngTcamIngAclIpv4_Type(TSysResource):
    """Custom type sysResIngTcamIngAclIpv4 based on TSysResource"""
    defaultValue = -1


_SysResIngTcamIngAclIpv4_Object = MibScalar
sysResIngTcamIngAclIpv4 = _SysResIngTcamIngAclIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 4),
    _SysResIngTcamIngAclIpv4_Type()
)
sysResIngTcamIngAclIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamIngAclIpv4.setStatus("current")


class _SysResIngTcamIngAcl64bitIpv4Ipv6_Type(TSysResource):
    """Custom type sysResIngTcamIngAcl64bitIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResIngTcamIngAcl64bitIpv4Ipv6_Object = MibScalar
sysResIngTcamIngAcl64bitIpv4Ipv6 = _SysResIngTcamIngAcl64bitIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 5),
    _SysResIngTcamIngAcl64bitIpv4Ipv6_Type()
)
sysResIngTcamIngAcl64bitIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamIngAcl64bitIpv4Ipv6.setStatus("current")


class _SysResIngTcamIngAcl128bitIpv4Ipv6_Type(TSysResource):
    """Custom type sysResIngTcamIngAcl128bitIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResIngTcamIngAcl128bitIpv4Ipv6_Object = MibScalar
sysResIngTcamIngAcl128bitIpv4Ipv6 = _SysResIngTcamIngAcl128bitIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 6),
    _SysResIngTcamIngAcl128bitIpv4Ipv6_Type()
)
sysResIngTcamIngAcl128bitIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamIngAcl128bitIpv4Ipv6.setStatus("current")


class _SysResIngTcamIngAcl64bitIpv6Only_Type(TSysResource):
    """Custom type sysResIngTcamIngAcl64bitIpv6Only based on TSysResource"""
    defaultValue = -1


_SysResIngTcamIngAcl64bitIpv6Only_Object = MibScalar
sysResIngTcamIngAcl64bitIpv6Only = _SysResIngTcamIngAcl64bitIpv6Only_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 7),
    _SysResIngTcamIngAcl64bitIpv6Only_Type()
)
sysResIngTcamIngAcl64bitIpv6Only.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamIngAcl64bitIpv6Only.setStatus("current")


class _SysResIngSapIngClass_Type(TSysResource):
    """Custom type sysResIngSapIngClass based on TSysResource"""
    defaultValue = -1


_SysResIngSapIngClass_Object = MibScalar
sysResIngSapIngClass = _SysResIngSapIngClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 8),
    _SysResIngSapIngClass_Type()
)
sysResIngSapIngClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngSapIngClass.setStatus("current")


class _SysResIngSapIngClassMac_Type(TSysResource):
    """Custom type sysResIngSapIngClassMac based on TSysResource"""
    defaultValue = -1


_SysResIngSapIngClassMac_Object = MibScalar
sysResIngSapIngClassMac = _SysResIngSapIngClassMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 9),
    _SysResIngSapIngClassMac_Type()
)
sysResIngSapIngClassMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngSapIngClassMac.setStatus("current")


class _SysResIngSapIngClassIpv4_Type(TSysResource):
    """Custom type sysResIngSapIngClassIpv4 based on TSysResource"""
    defaultValue = -1


_SysResIngSapIngClassIpv4_Object = MibScalar
sysResIngSapIngClassIpv4 = _SysResIngSapIngClassIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 10),
    _SysResIngSapIngClassIpv4_Type()
)
sysResIngSapIngClassIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngSapIngClassIpv4.setStatus("current")


class _SysResIngSapIngClassIpv4Ipv6_Type(TSysResource):
    """Custom type sysResIngSapIngClassIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResIngSapIngClassIpv4Ipv6_Object = MibScalar
sysResIngSapIngClassIpv4Ipv6 = _SysResIngSapIngClassIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 11),
    _SysResIngSapIngClassIpv4Ipv6_Type()
)
sysResIngSapIngClassIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngSapIngClassIpv4Ipv6.setStatus("current")


class _SysResFabricPathBandwidth_Type(Integer32):
    """Custom type sysResFabricPathBandwidth based on Integer32"""
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
        *(("lb1-11-lb2-25", 1),
          ("lb1-18-lb2-18", 4),
          ("lb1-24-lb2-12", 2),
          ("lb1-25-lb2-11", 3))
    )


_SysResFabricPathBandwidth_Type.__name__ = "Integer32"
_SysResFabricPathBandwidth_Object = MibScalar
sysResFabricPathBandwidth = _SysResFabricPathBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 12),
    _SysResFabricPathBandwidth_Type()
)
sysResFabricPathBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResFabricPathBandwidth.setStatus("obsolete")


class _SysResMaxIPv6Routes_Type(Integer32):
    """Custom type sysResMaxIPv6Routes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16000),
    )


_SysResMaxIPv6Routes_Type.__name__ = "Integer32"
_SysResMaxIPv6Routes_Object = MibScalar
sysResMaxIPv6Routes = _SysResMaxIPv6Routes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 13),
    _SysResMaxIPv6Routes_Type()
)
sysResMaxIPv6Routes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysResMaxIPv6Routes.setStatus("current")
_SysResIngTcamEthCfm_Type = TSysResource
_SysResIngTcamEthCfm_Object = MibScalar
sysResIngTcamEthCfm = _SysResIngTcamEthCfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 14),
    _SysResIngTcamEthCfm_Type()
)
sysResIngTcamEthCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamEthCfm.setStatus("current")


class _SysResIngTcamEthCfmUpMep_Type(TSysResource):
    """Custom type sysResIngTcamEthCfmUpMep based on TSysResource"""
    defaultValue = 1


_SysResIngTcamEthCfmUpMep_Object = MibScalar
sysResIngTcamEthCfmUpMep = _SysResIngTcamEthCfmUpMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 15),
    _SysResIngTcamEthCfmUpMep_Type()
)
sysResIngTcamEthCfmUpMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamEthCfmUpMep.setStatus("current")


class _SysG8032FastFloodEnableOperVal_Type(TruthValue):
    """Custom type sysG8032FastFloodEnableOperVal based on TruthValue"""


_SysG8032FastFloodEnableOperVal_Object = MibScalar
sysG8032FastFloodEnableOperVal = _SysG8032FastFloodEnableOperVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 16),
    _SysG8032FastFloodEnableOperVal_Type()
)
sysG8032FastFloodEnableOperVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysG8032FastFloodEnableOperVal.setStatus("current")


class _SysResEgrTcamSapEgrAcl_Type(TSysResource):
    """Custom type sysResEgrTcamSapEgrAcl based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamSapEgrAcl_Object = MibScalar
sysResEgrTcamSapEgrAcl = _SysResEgrTcamSapEgrAcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 17),
    _SysResEgrTcamSapEgrAcl_Type()
)
sysResEgrTcamSapEgrAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamSapEgrAcl.setStatus("current")


class _SysResEgrTcamEgrAclMac_Type(TSysResource):
    """Custom type sysResEgrTcamEgrAclMac based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamEgrAclMac_Object = MibScalar
sysResEgrTcamEgrAclMac = _SysResEgrTcamEgrAclMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 18),
    _SysResEgrTcamEgrAclMac_Type()
)
sysResEgrTcamEgrAclMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamEgrAclMac.setStatus("current")


class _SysResEgrTcamEgrAclIpv4_Type(TSysResource):
    """Custom type sysResEgrTcamEgrAclIpv4 based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamEgrAclIpv4_Object = MibScalar
sysResEgrTcamEgrAclIpv4 = _SysResEgrTcamEgrAclIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 19),
    _SysResEgrTcamEgrAclIpv4_Type()
)
sysResEgrTcamEgrAclIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamEgrAclIpv4.setStatus("current")


class _SysResEgrTcamEgrAcl64bitIpv4Ipv6_Type(TSysResource):
    """Custom type sysResEgrTcamEgrAcl64bitIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamEgrAcl64bitIpv4Ipv6_Object = MibScalar
sysResEgrTcamEgrAcl64bitIpv4Ipv6 = _SysResEgrTcamEgrAcl64bitIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 20),
    _SysResEgrTcamEgrAcl64bitIpv4Ipv6_Type()
)
sysResEgrTcamEgrAcl64bitIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamEgrAcl64bitIpv4Ipv6.setStatus("current")


class _SysResEgrTcamEgrAcl128bitIpv4Ipv6_Type(TSysResource):
    """Custom type sysResEgrTcamEgrAcl128bitIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamEgrAcl128bitIpv4Ipv6_Object = MibScalar
sysResEgrTcamEgrAcl128bitIpv4Ipv6 = _SysResEgrTcamEgrAcl128bitIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 21),
    _SysResEgrTcamEgrAcl128bitIpv4Ipv6_Type()
)
sysResEgrTcamEgrAcl128bitIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamEgrAcl128bitIpv4Ipv6.setStatus("current")


class _SysResEgrTcamEgrAcl64bitIpv6Only_Type(TSysResource):
    """Custom type sysResEgrTcamEgrAcl64bitIpv6Only based on TSysResource"""
    defaultValue = -1


_SysResEgrTcamEgrAcl64bitIpv6Only_Object = MibScalar
sysResEgrTcamEgrAcl64bitIpv6Only = _SysResEgrTcamEgrAcl64bitIpv6Only_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 22),
    _SysResEgrTcamEgrAcl64bitIpv6Only_Type()
)
sysResEgrTcamEgrAcl64bitIpv6Only.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrTcamEgrAcl64bitIpv6Only.setStatus("current")


class _SysResEgrSapEgrClass_Type(TSysResource):
    """Custom type sysResEgrSapEgrClass based on TSysResource"""
    defaultValue = -1


_SysResEgrSapEgrClass_Object = MibScalar
sysResEgrSapEgrClass = _SysResEgrSapEgrClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 23),
    _SysResEgrSapEgrClass_Type()
)
sysResEgrSapEgrClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrSapEgrClass.setStatus("current")


class _SysResEgrSapEgrClassMac_Type(TSysResource):
    """Custom type sysResEgrSapEgrClassMac based on TSysResource"""
    defaultValue = -1


_SysResEgrSapEgrClassMac_Object = MibScalar
sysResEgrSapEgrClassMac = _SysResEgrSapEgrClassMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 24),
    _SysResEgrSapEgrClassMac_Type()
)
sysResEgrSapEgrClassMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrSapEgrClassMac.setStatus("current")


class _SysResEgrSapEgrClassIpv4_Type(TSysResource):
    """Custom type sysResEgrSapEgrClassIpv4 based on TSysResource"""
    defaultValue = -1


_SysResEgrSapEgrClassIpv4_Object = MibScalar
sysResEgrSapEgrClassIpv4 = _SysResEgrSapEgrClassIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 25),
    _SysResEgrSapEgrClassIpv4_Type()
)
sysResEgrSapEgrClassIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrSapEgrClassIpv4.setStatus("current")


class _SysResEgrSapEgrClassIpv4Ipv6_Type(TSysResource):
    """Custom type sysResEgrSapEgrClassIpv4Ipv6 based on TSysResource"""
    defaultValue = -1


_SysResEgrSapEgrClassIpv4Ipv6_Object = MibScalar
sysResEgrSapEgrClassIpv4Ipv6 = _SysResEgrSapEgrClassIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 26),
    _SysResEgrSapEgrClassIpv4Ipv6_Type()
)
sysResEgrSapEgrClassIpv4Ipv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResEgrSapEgrClassIpv4Ipv6.setStatus("current")


class _SysResIngTcamSapAggMeter_Type(TSysResource):
    """Custom type sysResIngTcamSapAggMeter based on TSysResource"""
    defaultValue = -1


_SysResIngTcamSapAggMeter_Object = MibScalar
sysResIngTcamSapAggMeter = _SysResIngTcamSapAggMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 27),
    _SysResIngTcamSapAggMeter_Type()
)
sysResIngTcamSapAggMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamSapAggMeter.setStatus("current")


class _SysResIngTcamSapAggMeterOperVal_Type(TSysResource):
    """Custom type sysResIngTcamSapAggMeterOperVal based on TSysResource"""
    defaultValue = -1


_SysResIngTcamSapAggMeterOperVal_Object = MibScalar
sysResIngTcamSapAggMeterOperVal = _SysResIngTcamSapAggMeterOperVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 28),
    _SysResIngTcamSapAggMeterOperVal_Type()
)
sysResIngTcamSapAggMeterOperVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResIngTcamSapAggMeterOperVal.setStatus("current")


class _SysResQosSapIngQMode_Type(TruthValue):
    """Custom type sysResQosSapIngQMode based on TruthValue"""


_SysResQosSapIngQMode_Object = MibScalar
sysResQosSapIngQMode = _SysResQosSapIngQMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 29),
    _SysResQosSapIngQMode_Type()
)
sysResQosSapIngQMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResQosSapIngQMode.setStatus("current")


class _SysResQosSapIngQOperMode_Type(TruthValue):
    """Custom type sysResQosSapIngQOperMode based on TruthValue"""


_SysResQosSapIngQOperMode_Object = MibScalar
sysResQosSapIngQOperMode = _SysResQosSapIngQOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 30),
    _SysResQosSapIngQOperMode_Type()
)
sysResQosSapIngQOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResQosSapIngQOperMode.setStatus("current")


class _SysResRouterEcmpMaxRoutesDst_Type(Integer32):
    """Custom type sysResRouterEcmpMaxRoutesDst based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SysResRouterEcmpMaxRoutesDst_Type.__name__ = "Integer32"
_SysResRouterEcmpMaxRoutesDst_Object = MibScalar
sysResRouterEcmpMaxRoutesDst = _SysResRouterEcmpMaxRoutesDst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 31),
    _SysResRouterEcmpMaxRoutesDst_Type()
)
sysResRouterEcmpMaxRoutesDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysResRouterEcmpMaxRoutesDst.setStatus("current")


class _SysDhcpSnoopingSdpEnable_Type(TruthValue):
    """Custom type sysDhcpSnoopingSdpEnable based on TruthValue"""


_SysDhcpSnoopingSdpEnable_Object = MibScalar
sysDhcpSnoopingSdpEnable = _SysDhcpSnoopingSdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 32),
    _SysDhcpSnoopingSdpEnable_Type()
)
sysDhcpSnoopingSdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpSnoopingSdpEnable.setStatus("current")


class _SysDhcpSnoopingEnable_Type(TruthValue):
    """Custom type sysDhcpSnoopingEnable based on TruthValue"""


_SysDhcpSnoopingEnable_Object = MibScalar
sysDhcpSnoopingEnable = _SysDhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 33),
    _SysDhcpSnoopingEnable_Type()
)
sysDhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpSnoopingEnable.setStatus("current")


class _SysResRouterEcmpMaxRoutesDstOperVal_Type(Integer32):
    """Custom type sysResRouterEcmpMaxRoutesDstOperVal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SysResRouterEcmpMaxRoutesDstOperVal_Type.__name__ = "Integer32"
_SysResRouterEcmpMaxRoutesDstOperVal_Object = MibScalar
sysResRouterEcmpMaxRoutesDstOperVal = _SysResRouterEcmpMaxRoutesDstOperVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 34),
    _SysResRouterEcmpMaxRoutesDstOperVal_Type()
)
sysResRouterEcmpMaxRoutesDstOperVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResRouterEcmpMaxRoutesDstOperVal.setStatus("obsolete")


class _SysResIpMacMatchEnable_Type(Integer32):
    """Custom type sysResIpMacMatchEnable based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10),
    )


_SysResIpMacMatchEnable_Type.__name__ = "Integer32"
_SysResIpMacMatchEnable_Object = MibScalar
sysResIpMacMatchEnable = _SysResIpMacMatchEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 35),
    _SysResIpMacMatchEnable_Type()
)
sysResIpMacMatchEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysResIpMacMatchEnable.setStatus("current")


class _SysG8032FastFlood_Type(Integer32):
    """Custom type sysG8032FastFlood based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SysG8032FastFlood_Type.__name__ = "Integer32"
_SysG8032FastFlood_Object = MibScalar
sysG8032FastFlood = _SysG8032FastFlood_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 40),
    _SysG8032FastFlood_Type()
)
sysG8032FastFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysG8032FastFlood.setStatus("current")


class _SysResIngTcamEthCfmDownMep_Type(TSysResource):
    """Custom type sysResIngTcamEthCfmDownMep based on TSysResource"""
    defaultValue = 1


_SysResIngTcamEthCfmDownMep_Object = MibScalar
sysResIngTcamEthCfmDownMep = _SysResIngTcamEthCfmDownMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 51),
    _SysResIngTcamEthCfmDownMep_Type()
)
sysResIngTcamEthCfmDownMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamEthCfmDownMep.setStatus("current")


class _SysResQosMbsPool_Type(Integer32):
    """Custom type sysResQosMbsPool based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 1),
          ("port", 2))
    )


_SysResQosMbsPool_Type.__name__ = "Integer32"
_SysResQosMbsPool_Object = MibScalar
sysResQosMbsPool = _SysResQosMbsPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 53),
    _SysResQosMbsPool_Type()
)
sysResQosMbsPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResQosMbsPool.setStatus("current")


class _SysResIngTcamEthCfmUpMepPrimaryVlan_Type(Integer32):
    """Custom type sysResIngTcamEthCfmUpMepPrimaryVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SysResIngTcamEthCfmUpMepPrimaryVlan_Type.__name__ = "Integer32"
_SysResIngTcamEthCfmUpMepPrimaryVlan_Object = MibScalar
sysResIngTcamEthCfmUpMepPrimaryVlan = _SysResIngTcamEthCfmUpMepPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 54),
    _SysResIngTcamEthCfmUpMepPrimaryVlan_Type()
)
sysResIngTcamEthCfmUpMepPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamEthCfmUpMepPrimaryVlan.setStatus("current")


class _SysResIngTcamEthCfmDownMepPrimaryVlan_Type(Integer32):
    """Custom type sysResIngTcamEthCfmDownMepPrimaryVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SysResIngTcamEthCfmDownMepPrimaryVlan_Type.__name__ = "Integer32"
_SysResIngTcamEthCfmDownMepPrimaryVlan_Object = MibScalar
sysResIngTcamEthCfmDownMepPrimaryVlan = _SysResIngTcamEthCfmDownMepPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 55),
    _SysResIngTcamEthCfmDownMepPrimaryVlan_Type()
)
sysResIngTcamEthCfmDownMepPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResIngTcamEthCfmDownMepPrimaryVlan.setStatus("current")


class _SysResRouterMaxIPSubnets_Type(Integer32):
    """Custom type sysResRouterMaxIPSubnets based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_SysResRouterMaxIPSubnets_Type.__name__ = "Integer32"
_SysResRouterMaxIPSubnets_Object = MibScalar
sysResRouterMaxIPSubnets = _SysResRouterMaxIPSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 56),
    _SysResRouterMaxIPSubnets_Type()
)
sysResRouterMaxIPSubnets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysResRouterMaxIPSubnets.setStatus("current")


class _SysQosPortSchedModeEnable_Type(TruthValue):
    """Custom type sysQosPortSchedModeEnable based on TruthValue"""


_SysQosPortSchedModeEnable_Object = MibScalar
sysQosPortSchedModeEnable = _SysQosPortSchedModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 57),
    _SysQosPortSchedModeEnable_Type()
)
sysQosPortSchedModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysQosPortSchedModeEnable.setStatus("current")


class _SysResMaxIPv6RoutesOperVal_Type(Integer32):
    """Custom type sysResMaxIPv6RoutesOperVal based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16000),
    )


_SysResMaxIPv6RoutesOperVal_Type.__name__ = "Integer32"
_SysResMaxIPv6RoutesOperVal_Object = MibScalar
sysResMaxIPv6RoutesOperVal = _SysResMaxIPv6RoutesOperVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 17, 58),
    _SysResMaxIPv6RoutesOperVal_Type()
)
sysResMaxIPv6RoutesOperVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResMaxIPv6RoutesOperVal.setStatus("current")
_SysSASObjs_ObjectIdentity = ObjectIdentity
sysSASObjs = _SysSASObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 18)
)


class _TmnxSysConsoleAlarmInput_Type(TruthValue):
    """Custom type tmnxSysConsoleAlarmInput based on TruthValue"""


_TmnxSysConsoleAlarmInput_Object = MibScalar
tmnxSysConsoleAlarmInput = _TmnxSysConsoleAlarmInput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 18, 2),
    _TmnxSysConsoleAlarmInput_Type()
)
tmnxSysConsoleAlarmInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysConsoleAlarmInput.setStatus("current")
_SysSASVwmObjs_ObjectIdentity = ObjectIdentity
sysSASVwmObjs = _SysSASVwmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19)
)
_TmnxVwmShelfTable_Object = MibTable
tmnxVwmShelfTable = _TmnxVwmShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1)
)
if mibBuilder.loadTexts:
    tmnxVwmShelfTable.setStatus("current")
_TmnxVwmShelfEntry_Object = MibTableRow
tmnxVwmShelfEntry = _TmnxVwmShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1)
)
tmnxVwmShelfEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfId"),
)
if mibBuilder.loadTexts:
    tmnxVwmShelfEntry.setStatus("current")


class _TmnxVwmShelfId_Type(Integer32):
    """Custom type tmnxVwmShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxVwmShelfId_Type.__name__ = "Integer32"
_TmnxVwmShelfId_Object = MibTableColumn
tmnxVwmShelfId = _TmnxVwmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 1),
    _TmnxVwmShelfId_Type()
)
tmnxVwmShelfId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVwmShelfId.setStatus("current")
_TmnxVwmShelfRowStatus_Type = RowStatus
_TmnxVwmShelfRowStatus_Object = MibTableColumn
tmnxVwmShelfRowStatus = _TmnxVwmShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 2),
    _TmnxVwmShelfRowStatus_Type()
)
tmnxVwmShelfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVwmShelfRowStatus.setStatus("current")


class _TmnxVwmShelfAdminState_Type(TmnxAdminState):
    """Custom type tmnxVwmShelfAdminState based on TmnxAdminState"""


_TmnxVwmShelfAdminState_Object = MibTableColumn
tmnxVwmShelfAdminState = _TmnxVwmShelfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 3),
    _TmnxVwmShelfAdminState_Type()
)
tmnxVwmShelfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVwmShelfAdminState.setStatus("current")


class _TmnxVwmShelfOperState_Type(TmnxAdminState):
    """Custom type tmnxVwmShelfOperState based on TmnxAdminState"""


_TmnxVwmShelfOperState_Object = MibTableColumn
tmnxVwmShelfOperState = _TmnxVwmShelfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 4),
    _TmnxVwmShelfOperState_Type()
)
tmnxVwmShelfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVwmShelfOperState.setStatus("current")


class _TmnxVwmShelfVwmType_Type(Integer32):
    """Custom type tmnxVwmShelfVwmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ec-cw", 1),
          ("ec-dw", 2))
    )


_TmnxVwmShelfVwmType_Type.__name__ = "Integer32"
_TmnxVwmShelfVwmType_Object = MibTableColumn
tmnxVwmShelfVwmType = _TmnxVwmShelfVwmType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 5),
    _TmnxVwmShelfVwmType_Type()
)
tmnxVwmShelfVwmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVwmShelfVwmType.setStatus("current")


class _TmnxVwmShelfEquippedType_Type(Integer32):
    """Custom type tmnxVwmShelfEquippedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cwdm", 2),
          ("dwdm", 4),
          ("not-equipped", 0),
          ("unknown", 1))
    )


_TmnxVwmShelfEquippedType_Type.__name__ = "Integer32"
_TmnxVwmShelfEquippedType_Object = MibTableColumn
tmnxVwmShelfEquippedType = _TmnxVwmShelfEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 6),
    _TmnxVwmShelfEquippedType_Type()
)
tmnxVwmShelfEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVwmShelfEquippedType.setStatus("current")


class _TmnxVwmshelfTypeConnected_Type(Integer32):
    """Custom type tmnxVwmshelfTypeConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("i2c", 2),
          ("usb", 1))
    )


_TmnxVwmshelfTypeConnected_Type.__name__ = "Integer32"
_TmnxVwmshelfTypeConnected_Object = MibTableColumn
tmnxVwmshelfTypeConnected = _TmnxVwmshelfTypeConnected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 1, 1, 7),
    _TmnxVwmshelfTypeConnected_Type()
)
tmnxVwmshelfTypeConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVwmshelfTypeConnected.setStatus("current")
_TmnxVwmShelfCardTable_Object = MibTable
tmnxVwmShelfCardTable = _TmnxVwmShelfCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2)
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardTable.setStatus("current")
_TmnxVwmShelfCardEntry_Object = MibTableRow
tmnxVwmShelfCardEntry = _TmnxVwmShelfCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1)
)
tmnxVwmShelfCardEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfId"),
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"),
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardEntry.setStatus("current")


class _TmnxVwmShelfCardId_Type(Integer32):
    """Custom type tmnxVwmShelfCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TmnxVwmShelfCardId_Type.__name__ = "Integer32"
_TmnxVwmShelfCardId_Object = MibTableColumn
tmnxVwmShelfCardId = _TmnxVwmShelfCardId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1, 1),
    _TmnxVwmShelfCardId_Type()
)
tmnxVwmShelfCardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVwmShelfCardId.setStatus("current")
_TmnxVwmShelfCardType_Type = TmnxVwmCardType
_TmnxVwmShelfCardType_Object = MibTableColumn
tmnxVwmShelfCardType = _TmnxVwmShelfCardType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1, 2),
    _TmnxVwmShelfCardType_Type()
)
tmnxVwmShelfCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxVwmShelfCardType.setStatus("current")
_TmnxVwmShelfCardEqType_Type = TmnxVwmCardType
_TmnxVwmShelfCardEqType_Object = MibTableColumn
tmnxVwmShelfCardEqType = _TmnxVwmShelfCardEqType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1, 3),
    _TmnxVwmShelfCardEqType_Type()
)
tmnxVwmShelfCardEqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVwmShelfCardEqType.setStatus("current")


class _TmnxVwmShelfCardAdminState_Type(TmnxAdminState):
    """Custom type tmnxVwmShelfCardAdminState based on TmnxAdminState"""


_TmnxVwmShelfCardAdminState_Object = MibTableColumn
tmnxVwmShelfCardAdminState = _TmnxVwmShelfCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1, 4),
    _TmnxVwmShelfCardAdminState_Type()
)
tmnxVwmShelfCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxVwmShelfCardAdminState.setStatus("current")


class _TmnxVwmShelfCardOperState_Type(TmnxAdminState):
    """Custom type tmnxVwmShelfCardOperState based on TmnxAdminState"""


_TmnxVwmShelfCardOperState_Object = MibTableColumn
tmnxVwmShelfCardOperState = _TmnxVwmShelfCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 19, 2, 1, 5),
    _TmnxVwmShelfCardOperState_Type()
)
tmnxVwmShelfCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVwmShelfCardOperState.setStatus("current")
_SysQosObjs_ObjectIdentity = ObjectIdentity
sysQosObjs = _SysQosObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 20)
)


class _SysQosWredSlopes_Type(Integer32):
    """Custom type sysQosWredSlopes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-low", 1),
          ("tcp-non-tcp", 2))
    )


_SysQosWredSlopes_Type.__name__ = "Integer32"
_SysQosWredSlopes_Object = MibScalar
sysQosWredSlopes = _SysQosWredSlopes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 20, 1),
    _SysQosWredSlopes_Type()
)
sysQosWredSlopes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysQosWredSlopes.setStatus("current")
_SysClockInfo_ObjectIdentity = ObjectIdentity
sysClockInfo = _SysClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 21)
)


class _TmnxPtpTimeUsePtp_Type(TmnxPtpTime):
    """Custom type tmnxPtpTimeUsePtp based on TmnxPtpTime"""


_TmnxPtpTimeUsePtp_Object = MibScalar
tmnxPtpTimeUsePtp = _TmnxPtpTimeUsePtp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 21, 1),
    _TmnxPtpTimeUsePtp_Type()
)
tmnxPtpTimeUsePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpTimeUsePtp.setStatus("current")
_SysResProfPlcyObjs_ObjectIdentity = ObjectIdentity
sysResProfPlcyObjs = _SysResProfPlcyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22)
)
_TResPlcyTable_Object = MibTable
tResPlcyTable = _TResPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1)
)
if mibBuilder.loadTexts:
    tResPlcyTable.setStatus("current")
_TResPlcyEntry_Object = MibTableRow
tResPlcyEntry = _TResPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1)
)
tResPlcyEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tResPlcyId"),
)
if mibBuilder.loadTexts:
    tResPlcyEntry.setStatus("current")


class _TResPlcyId_Type(Integer32):
    """Custom type tResPlcyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TResPlcyId_Type.__name__ = "Integer32"
_TResPlcyId_Object = MibTableColumn
tResPlcyId = _TResPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 1),
    _TResPlcyId_Type()
)
tResPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tResPlcyId.setStatus("current")
_TResPlcyRowStatus_Type = RowStatus
_TResPlcyRowStatus_Object = MibTableColumn
tResPlcyRowStatus = _TResPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 2),
    _TResPlcyRowStatus_Type()
)
tResPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyRowStatus.setStatus("current")


class _TResPlcyIngTcamSapAggMeter_Type(Integer32):
    """Custom type tResPlcyIngTcamSapAggMeter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TResPlcyIngTcamSapAggMeter_Type.__name__ = "Integer32"
_TResPlcyIngTcamSapAggMeter_Object = MibTableColumn
tResPlcyIngTcamSapAggMeter = _TResPlcyIngTcamSapAggMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 3),
    _TResPlcyIngTcamSapAggMeter_Type()
)
tResPlcyIngTcamSapAggMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamSapAggMeter.setStatus("current")


class _TResPlcyIngTcamQosSapIng_Type(Integer32):
    """Custom type tResPlcyIngTcamQosSapIng based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TResPlcyIngTcamQosSapIng_Type.__name__ = "Integer32"
_TResPlcyIngTcamQosSapIng_Object = MibTableColumn
tResPlcyIngTcamQosSapIng = _TResPlcyIngTcamQosSapIng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 4),
    _TResPlcyIngTcamQosSapIng_Type()
)
tResPlcyIngTcamQosSapIng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamQosSapIng.setStatus("current")


class _TResPlcyIngTcamQosSapIngIpv4_Type(Integer32):
    """Custom type tResPlcyIngTcamQosSapIngIpv4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamQosSapIngIpv4_Type.__name__ = "Integer32"
_TResPlcyIngTcamQosSapIngIpv4_Object = MibTableColumn
tResPlcyIngTcamQosSapIngIpv4 = _TResPlcyIngTcamQosSapIngIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 5),
    _TResPlcyIngTcamQosSapIngIpv4_Type()
)
tResPlcyIngTcamQosSapIngIpv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamQosSapIngIpv4.setStatus("current")


class _TResPlcyIngTcamQosSapIngIpv4Ipv6_Type(Integer32):
    """Custom type tResPlcyIngTcamQosSapIngIpv4Ipv6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamQosSapIngIpv4Ipv6_Type.__name__ = "Integer32"
_TResPlcyIngTcamQosSapIngIpv4Ipv6_Object = MibTableColumn
tResPlcyIngTcamQosSapIngIpv4Ipv6 = _TResPlcyIngTcamQosSapIngIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 6),
    _TResPlcyIngTcamQosSapIngIpv4Ipv6_Type()
)
tResPlcyIngTcamQosSapIngIpv4Ipv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamQosSapIngIpv4Ipv6.setStatus("current")


class _TResPlcyIngTcamQosSapIngMac_Type(Integer32):
    """Custom type tResPlcyIngTcamQosSapIngMac based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamQosSapIngMac_Type.__name__ = "Integer32"
_TResPlcyIngTcamQosSapIngMac_Object = MibTableColumn
tResPlcyIngTcamQosSapIngMac = _TResPlcyIngTcamQosSapIngMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 7),
    _TResPlcyIngTcamQosSapIngMac_Type()
)
tResPlcyIngTcamQosSapIngMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamQosSapIngMac.setStatus("current")


class _TResPlcyIngTcamAclSapIng_Type(Integer32):
    """Custom type tResPlcyIngTcamAclSapIng based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TResPlcyIngTcamAclSapIng_Type.__name__ = "Integer32"
_TResPlcyIngTcamAclSapIng_Object = MibTableColumn
tResPlcyIngTcamAclSapIng = _TResPlcyIngTcamAclSapIng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 8),
    _TResPlcyIngTcamAclSapIng_Type()
)
tResPlcyIngTcamAclSapIng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamAclSapIng.setStatus("current")


class _TResPlcyIngTcamAclSapIngIpv4_Type(Integer32):
    """Custom type tResPlcyIngTcamAclSapIngIpv4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamAclSapIngIpv4_Type.__name__ = "Integer32"
_TResPlcyIngTcamAclSapIngIpv4_Object = MibTableColumn
tResPlcyIngTcamAclSapIngIpv4 = _TResPlcyIngTcamAclSapIngIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 9),
    _TResPlcyIngTcamAclSapIngIpv4_Type()
)
tResPlcyIngTcamAclSapIngIpv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamAclSapIngIpv4.setStatus("current")


class _TResPlcyIngTcamAclSapIng64Ipv6_Type(Integer32):
    """Custom type tResPlcyIngTcamAclSapIng64Ipv6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamAclSapIng64Ipv6_Type.__name__ = "Integer32"
_TResPlcyIngTcamAclSapIng64Ipv6_Object = MibTableColumn
tResPlcyIngTcamAclSapIng64Ipv6 = _TResPlcyIngTcamAclSapIng64Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 10),
    _TResPlcyIngTcamAclSapIng64Ipv6_Type()
)
tResPlcyIngTcamAclSapIng64Ipv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamAclSapIng64Ipv6.setStatus("current")


class _TResPlcyIngTcamAclSapIng128Ipv4Ipv6_Type(Integer32):
    """Custom type tResPlcyIngTcamAclSapIng128Ipv4Ipv6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamAclSapIng128Ipv4Ipv6_Type.__name__ = "Integer32"
_TResPlcyIngTcamAclSapIng128Ipv4Ipv6_Object = MibTableColumn
tResPlcyIngTcamAclSapIng128Ipv4Ipv6 = _TResPlcyIngTcamAclSapIng128Ipv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 11),
    _TResPlcyIngTcamAclSapIng128Ipv4Ipv6_Type()
)
tResPlcyIngTcamAclSapIng128Ipv4Ipv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamAclSapIng128Ipv4Ipv6.setStatus("current")


class _TResPlcyIngTcamAclSapIngMac_Type(Integer32):
    """Custom type tResPlcyIngTcamAclSapIngMac based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TResPlcyIngTcamAclSapIngMac_Type.__name__ = "Integer32"
_TResPlcyIngTcamAclSapIngMac_Object = MibTableColumn
tResPlcyIngTcamAclSapIngMac = _TResPlcyIngTcamAclSapIngMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 12),
    _TResPlcyIngTcamAclSapIngMac_Type()
)
tResPlcyIngTcamAclSapIngMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamAclSapIngMac.setStatus("current")


class _TResPlcyEgrTcamAclSapEgr_Type(Integer32):
    """Custom type tResPlcyEgrTcamAclSapEgr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TResPlcyEgrTcamAclSapEgr_Type.__name__ = "Integer32"
_TResPlcyEgrTcamAclSapEgr_Object = MibTableColumn
tResPlcyEgrTcamAclSapEgr = _TResPlcyEgrTcamAclSapEgr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 13),
    _TResPlcyEgrTcamAclSapEgr_Type()
)
tResPlcyEgrTcamAclSapEgr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyEgrTcamAclSapEgr.setStatus("current")


class _TResPlcyEgrTcamAclSapEgrMacIpv4_Type(Integer32):
    """Custom type tResPlcyEgrTcamAclSapEgrMacIpv4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TResPlcyEgrTcamAclSapEgrMacIpv4_Type.__name__ = "Integer32"
_TResPlcyEgrTcamAclSapEgrMacIpv4_Object = MibTableColumn
tResPlcyEgrTcamAclSapEgrMacIpv4 = _TResPlcyEgrTcamAclSapEgrMacIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 14),
    _TResPlcyEgrTcamAclSapEgrMacIpv4_Type()
)
tResPlcyEgrTcamAclSapEgrMacIpv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyEgrTcamAclSapEgrMacIpv4.setStatus("current")


class _TResPlcyEgrTcamAclSapEgr128Ipv6_Type(Integer32):
    """Custom type tResPlcyEgrTcamAclSapEgr128Ipv6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TResPlcyEgrTcamAclSapEgr128Ipv6_Type.__name__ = "Integer32"
_TResPlcyEgrTcamAclSapEgr128Ipv6_Object = MibTableColumn
tResPlcyEgrTcamAclSapEgr128Ipv6 = _TResPlcyEgrTcamAclSapEgr128Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 15),
    _TResPlcyEgrTcamAclSapEgr128Ipv6_Type()
)
tResPlcyEgrTcamAclSapEgr128Ipv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyEgrTcamAclSapEgr128Ipv6.setStatus("current")


class _TResPlcyEgrTcamAclSapEgr64MacIpv6_Type(Integer32):
    """Custom type tResPlcyEgrTcamAclSapEgr64MacIpv6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TResPlcyEgrTcamAclSapEgr64MacIpv6_Type.__name__ = "Integer32"
_TResPlcyEgrTcamAclSapEgr64MacIpv6_Object = MibTableColumn
tResPlcyEgrTcamAclSapEgr64MacIpv6 = _TResPlcyEgrTcamAclSapEgr64MacIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 16),
    _TResPlcyEgrTcamAclSapEgr64MacIpv6_Type()
)
tResPlcyEgrTcamAclSapEgr64MacIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyEgrTcamAclSapEgr64MacIpv6.setStatus("current")


class _TResPlcyEgrTcamAclSapEgrMac_Type(Integer32):
    """Custom type tResPlcyEgrTcamAclSapEgrMac based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TResPlcyEgrTcamAclSapEgrMac_Type.__name__ = "Integer32"
_TResPlcyEgrTcamAclSapEgrMac_Object = MibTableColumn
tResPlcyEgrTcamAclSapEgrMac = _TResPlcyEgrTcamAclSapEgrMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 17),
    _TResPlcyEgrTcamAclSapEgrMac_Type()
)
tResPlcyEgrTcamAclSapEgrMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyEgrTcamAclSapEgrMac.setStatus("current")


class _TResPlcyDescription_Type(TItemDescription):
    """Custom type tResPlcyDescription based on TItemDescription"""
    defaultHexValue = ""


_TResPlcyDescription_Object = MibTableColumn
tResPlcyDescription = _TResPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 18),
    _TResPlcyDescription_Type()
)
tResPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyDescription.setStatus("current")
_TResPlcyLastChanged_Type = TimeStamp
_TResPlcyLastChanged_Object = MibTableColumn
tResPlcyLastChanged = _TResPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 19),
    _TResPlcyLastChanged_Type()
)
tResPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tResPlcyLastChanged.setStatus("current")


class _TResPlcyIngTcamEthCfm_Type(Integer32):
    """Custom type tResPlcyIngTcamEthCfm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TResPlcyIngTcamEthCfm_Type.__name__ = "Integer32"
_TResPlcyIngTcamEthCfm_Object = MibTableColumn
tResPlcyIngTcamEthCfm = _TResPlcyIngTcamEthCfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 20),
    _TResPlcyIngTcamEthCfm_Type()
)
tResPlcyIngTcamEthCfm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamEthCfm.setStatus("current")


class _TResPlcyIngTcamEthCfmUpMep_Type(Integer32):
    """Custom type tResPlcyIngTcamEthCfmUpMep based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TResPlcyIngTcamEthCfmUpMep_Type.__name__ = "Integer32"
_TResPlcyIngTcamEthCfmUpMep_Object = MibTableColumn
tResPlcyIngTcamEthCfmUpMep = _TResPlcyIngTcamEthCfmUpMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 21),
    _TResPlcyIngTcamEthCfmUpMep_Type()
)
tResPlcyIngTcamEthCfmUpMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamEthCfmUpMep.setStatus("current")


class _TResPlcyG8032CtrlSapStartVlan_Type(Unsigned32):
    """Custom type tResPlcyG8032CtrlSapStartVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3512),
    )


_TResPlcyG8032CtrlSapStartVlan_Type.__name__ = "Unsigned32"
_TResPlcyG8032CtrlSapStartVlan_Object = MibTableColumn
tResPlcyG8032CtrlSapStartVlan = _TResPlcyG8032CtrlSapStartVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 22),
    _TResPlcyG8032CtrlSapStartVlan_Type()
)
tResPlcyG8032CtrlSapStartVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyG8032CtrlSapStartVlan.setStatus("current")


class _TResPlcyG8032CtrlSapEndVlan_Type(Unsigned32):
    """Custom type tResPlcyG8032CtrlSapEndVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3512),
    )


_TResPlcyG8032CtrlSapEndVlan_Type.__name__ = "Unsigned32"
_TResPlcyG8032CtrlSapEndVlan_Object = MibTableColumn
tResPlcyG8032CtrlSapEndVlan = _TResPlcyG8032CtrlSapEndVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 23),
    _TResPlcyG8032CtrlSapEndVlan_Type()
)
tResPlcyG8032CtrlSapEndVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyG8032CtrlSapEndVlan.setStatus("current")


class _TResPlcyResIpMacMatchEnable_Type(Integer32):
    """Custom type tResPlcyResIpMacMatchEnable based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10),
    )


_TResPlcyResIpMacMatchEnable_Type.__name__ = "Integer32"
_TResPlcyResIpMacMatchEnable_Object = MibTableColumn
tResPlcyResIpMacMatchEnable = _TResPlcyResIpMacMatchEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 24),
    _TResPlcyResIpMacMatchEnable_Type()
)
tResPlcyResIpMacMatchEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyResIpMacMatchEnable.setStatus("current")


class _TResPlcyIngTcamEthCfmDownMep_Type(Integer32):
    """Custom type tResPlcyIngTcamEthCfmDownMep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TResPlcyIngTcamEthCfmDownMep_Type.__name__ = "Integer32"
_TResPlcyIngTcamEthCfmDownMep_Object = MibTableColumn
tResPlcyIngTcamEthCfmDownMep = _TResPlcyIngTcamEthCfmDownMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 25),
    _TResPlcyIngTcamEthCfmDownMep_Type()
)
tResPlcyIngTcamEthCfmDownMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResPlcyIngTcamEthCfmDownMep.setStatus("current")


class _TResPlcyIngTcamEthCfmUpMepEnable_Type(TruthValue):
    """Custom type tResPlcyIngTcamEthCfmUpMepEnable based on TruthValue"""


_TResPlcyIngTcamEthCfmUpMepEnable_Object = MibTableColumn
tResPlcyIngTcamEthCfmUpMepEnable = _TResPlcyIngTcamEthCfmUpMepEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 27),
    _TResPlcyIngTcamEthCfmUpMepEnable_Type()
)
tResPlcyIngTcamEthCfmUpMepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tResPlcyIngTcamEthCfmUpMepEnable.setStatus("current")


class _TResPlcyIngTcamEthCfmDownMepEnable_Type(TruthValue):
    """Custom type tResPlcyIngTcamEthCfmDownMepEnable based on TruthValue"""


_TResPlcyIngTcamEthCfmDownMepEnable_Object = MibTableColumn
tResPlcyIngTcamEthCfmDownMepEnable = _TResPlcyIngTcamEthCfmDownMepEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 22, 1, 1, 28),
    _TResPlcyIngTcamEthCfmDownMepEnable_Type()
)
tResPlcyIngTcamEthCfmDownMepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tResPlcyIngTcamEthCfmDownMepEnable.setStatus("current")
_SysResProfDecommObjs_ObjectIdentity = ObjectIdentity
sysResProfDecommObjs = _SysResProfDecommObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23)
)
_TResDecommTable_Object = MibTable
tResDecommTable = _TResDecommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1)
)
if mibBuilder.loadTexts:
    tResDecommTable.setStatus("current")
_TResDecommEntry_Object = MibTableRow
tResDecommEntry = _TResDecommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1, 1)
)
tResDecommEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tResDecommId"),
)
if mibBuilder.loadTexts:
    tResDecommEntry.setStatus("current")


class _TResDecommId_Type(Integer32):
    """Custom type tResDecommId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TResDecommId_Type.__name__ = "Integer32"
_TResDecommId_Object = MibTableColumn
tResDecommId = _TResDecommId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1, 1, 1),
    _TResDecommId_Type()
)
tResDecommId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tResDecommId.setStatus("current")
_TResDecommRowStatus_Type = RowStatus
_TResDecommRowStatus_Object = MibTableColumn
tResDecommRowStatus = _TResDecommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1, 1, 2),
    _TResDecommRowStatus_Type()
)
tResDecommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResDecommRowStatus.setStatus("current")
_TResDecommFromPortMap_Type = Unsigned32
_TResDecommFromPortMap_Object = MibTableColumn
tResDecommFromPortMap = _TResDecommFromPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1, 1, 3),
    _TResDecommFromPortMap_Type()
)
tResDecommFromPortMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResDecommFromPortMap.setStatus("current")
_TResDecommToPortMap_Type = Unsigned32
_TResDecommToPortMap_Object = MibTableColumn
tResDecommToPortMap = _TResDecommToPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 1, 1, 4),
    _TResDecommToPortMap_Type()
)
tResDecommToPortMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tResDecommToPortMap.setStatus("current")
_TResDecommOperTable_Object = MibTable
tResDecommOperTable = _TResDecommOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 2)
)
if mibBuilder.loadTexts:
    tResDecommOperTable.setStatus("current")
_TResDecommOperEntry_Object = MibTableRow
tResDecommOperEntry = _TResDecommOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 2, 1)
)
tResDecommOperEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tResDecommOperId"),
)
if mibBuilder.loadTexts:
    tResDecommOperEntry.setStatus("current")


class _TResDecommOperId_Type(Integer32):
    """Custom type tResDecommOperId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TResDecommOperId_Type.__name__ = "Integer32"
_TResDecommOperId_Object = MibTableColumn
tResDecommOperId = _TResDecommOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 2, 1, 1),
    _TResDecommOperId_Type()
)
tResDecommOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tResDecommOperId.setStatus("current")
_TResDecommOperFromPortMap_Type = Unsigned32
_TResDecommOperFromPortMap_Object = MibTableColumn
tResDecommOperFromPortMap = _TResDecommOperFromPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 2, 1, 2),
    _TResDecommOperFromPortMap_Type()
)
tResDecommOperFromPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tResDecommOperFromPortMap.setStatus("current")
_TResDecommOperToPortMap_Type = Unsigned32
_TResDecommOperToPortMap_Object = MibTableColumn
tResDecommOperToPortMap = _TResDecommOperToPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 23, 2, 1, 3),
    _TResDecommOperToPortMap_Type()
)
tResDecommOperToPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tResDecommOperToPortMap.setStatus("current")
_SysOperGrpObjs_ObjectIdentity = ObjectIdentity
sysOperGrpObjs = _SysOperGrpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24)
)
_SysOperGrpTblLastChanged_Type = TimeStamp
_SysOperGrpTblLastChanged_Object = MibScalar
sysOperGrpTblLastChanged = _SysOperGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 1),
    _SysOperGrpTblLastChanged_Type()
)
sysOperGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpTblLastChanged.setStatus("current")
_SysOperGrpTable_Object = MibTable
sysOperGrpTable = _SysOperGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2)
)
if mibBuilder.loadTexts:
    sysOperGrpTable.setStatus("current")
_SysOperGrpEntry_Object = MibTableRow
sysOperGrpEntry = _SysOperGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1)
)
sysOperGrpEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "sysOperGrpName"),
)
if mibBuilder.loadTexts:
    sysOperGrpEntry.setStatus("current")
_SysOperGrpName_Type = TNamedItem
_SysOperGrpName_Object = MibTableColumn
sysOperGrpName = _SysOperGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 1),
    _SysOperGrpName_Type()
)
sysOperGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysOperGrpName.setStatus("current")
_SysOperGrpRowStatus_Type = RowStatus
_SysOperGrpRowStatus_Object = MibTableColumn
sysOperGrpRowStatus = _SysOperGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 2),
    _SysOperGrpRowStatus_Type()
)
sysOperGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysOperGrpRowStatus.setStatus("current")
_SysOperGrpLastChange_Type = TimeStamp
_SysOperGrpLastChange_Object = MibTableColumn
sysOperGrpLastChange = _SysOperGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 3),
    _SysOperGrpLastChange_Type()
)
sysOperGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpLastChange.setStatus("current")
_SysOperGrpOperStatus_Type = ServiceOperStatus
_SysOperGrpOperStatus_Object = MibTableColumn
sysOperGrpOperStatus = _SysOperGrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 4),
    _SysOperGrpOperStatus_Type()
)
sysOperGrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpOperStatus.setStatus("current")


class _SysOperGrpHoldDownTime_Type(TmnxOperGrpHoldDownTime):
    """Custom type sysOperGrpHoldDownTime based on TmnxOperGrpHoldDownTime"""
    defaultValue = 0


_SysOperGrpHoldDownTime_Object = MibTableColumn
sysOperGrpHoldDownTime = _SysOperGrpHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 5),
    _SysOperGrpHoldDownTime_Type()
)
sysOperGrpHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysOperGrpHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    sysOperGrpHoldDownTime.setUnits("seconds")
_SysOperGrpCreationOrigin_Type = TmnxSysOperGrpCreationOrigin
_SysOperGrpCreationOrigin_Object = MibTableColumn
sysOperGrpCreationOrigin = _SysOperGrpCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 6),
    _SysOperGrpCreationOrigin_Type()
)
sysOperGrpCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpCreationOrigin.setStatus("current")


class _SysOperGrpHoldUpTime_Type(TmnxOperGrpHoldUpTime):
    """Custom type sysOperGrpHoldUpTime based on TmnxOperGrpHoldUpTime"""
    defaultValue = 4


_SysOperGrpHoldUpTime_Object = MibTableColumn
sysOperGrpHoldUpTime = _SysOperGrpHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 7),
    _SysOperGrpHoldUpTime_Type()
)
sysOperGrpHoldUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysOperGrpHoldUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sysOperGrpHoldUpTime.setUnits("seconds")
_SysOperGrpHoldUpTimeRemain_Type = TmnxOperGrpHoldUpTime
_SysOperGrpHoldUpTimeRemain_Object = MibTableColumn
sysOperGrpHoldUpTimeRemain = _SysOperGrpHoldUpTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 8),
    _SysOperGrpHoldUpTimeRemain_Type()
)
sysOperGrpHoldUpTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpHoldUpTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    sysOperGrpHoldUpTimeRemain.setUnits("seconds")
_SysOperGrpHoldDownTimeRemain_Type = TmnxOperGrpHoldDownTime
_SysOperGrpHoldDownTimeRemain_Object = MibTableColumn
sysOperGrpHoldDownTimeRemain = _SysOperGrpHoldDownTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 9),
    _SysOperGrpHoldDownTimeRemain_Type()
)
sysOperGrpHoldDownTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpHoldDownTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    sysOperGrpHoldDownTimeRemain.setUnits("seconds")
_SysOperGrpNumMembers_Type = Gauge32
_SysOperGrpNumMembers_Object = MibTableColumn
sysOperGrpNumMembers = _SysOperGrpNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 10),
    _SysOperGrpNumMembers_Type()
)
sysOperGrpNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpNumMembers.setStatus("current")
_SysOperGrpNumMonitoring_Type = Gauge32
_SysOperGrpNumMonitoring_Object = MibTableColumn
sysOperGrpNumMonitoring = _SysOperGrpNumMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 5, 24, 2, 1, 11),
    _SysOperGrpNumMonitoring_Type()
)
sysOperGrpNumMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperGrpNumMonitoring.setStatus("current")
_TmnxSASChassisObjs_ObjectIdentity = ObjectIdentity
tmnxSASChassisObjs = _TmnxSASChassisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6)
)
_TmnxSASChassisNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxSASChassisNotificationObjs = _TmnxSASChassisNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 1)
)
_TmnxSASChassisNotification_ObjectIdentity = ObjectIdentity
tmnxSASChassisNotification = _TmnxSASChassisNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2)
)
_TmnxChassisExtnTable_Object = MibTable
tmnxChassisExtnTable = _TmnxChassisExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxChassisExtnTable.setStatus("current")
_TmnxChassisExtnEntry_Object = MibTableRow
tmnxChassisExtnEntry = _TmnxChassisExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxChassisExtnEntry.setStatus("current")


class _TmnxChassisUpdateGoldenBootstrapImage_Type(TmnxActionType):
    """Custom type tmnxChassisUpdateGoldenBootstrapImage based on TmnxActionType"""


_TmnxChassisUpdateGoldenBootstrapImage_Object = MibTableColumn
tmnxChassisUpdateGoldenBootstrapImage = _TmnxChassisUpdateGoldenBootstrapImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 1),
    _TmnxChassisUpdateGoldenBootstrapImage_Type()
)
tmnxChassisUpdateGoldenBootstrapImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisUpdateGoldenBootstrapImage.setStatus("current")
_TmnxChassisGoldenBootstrapImageSrc_Type = DisplayString
_TmnxChassisGoldenBootstrapImageSrc_Object = MibTableColumn
tmnxChassisGoldenBootstrapImageSrc = _TmnxChassisGoldenBootstrapImageSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 2),
    _TmnxChassisGoldenBootstrapImageSrc_Type()
)
tmnxChassisGoldenBootstrapImageSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisGoldenBootstrapImageSrc.setStatus("current")


class _TmnxChassisValidateGoldenBootstrapImage_Type(TmnxActionType):
    """Custom type tmnxChassisValidateGoldenBootstrapImage based on TmnxActionType"""


_TmnxChassisValidateGoldenBootstrapImage_Object = MibTableColumn
tmnxChassisValidateGoldenBootstrapImage = _TmnxChassisValidateGoldenBootstrapImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 3),
    _TmnxChassisValidateGoldenBootstrapImage_Type()
)
tmnxChassisValidateGoldenBootstrapImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisValidateGoldenBootstrapImage.setStatus("current")


class _TmnxChassisGoldenBootstrapImageVersion_Type(DisplayString):
    """Custom type tmnxChassisGoldenBootstrapImageVersion based on DisplayString"""
    defaultValue = OctetString("not-validated")


_TmnxChassisGoldenBootstrapImageVersion_Object = MibTableColumn
tmnxChassisGoldenBootstrapImageVersion = _TmnxChassisGoldenBootstrapImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 4),
    _TmnxChassisGoldenBootstrapImageVersion_Type()
)
tmnxChassisGoldenBootstrapImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisGoldenBootstrapImageVersion.setStatus("current")
_TmnxChassisRebootAutoInit_Type = TmnxActionType
_TmnxChassisRebootAutoInit_Object = MibTableColumn
tmnxChassisRebootAutoInit = _TmnxChassisRebootAutoInit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 5),
    _TmnxChassisRebootAutoInit_Type()
)
tmnxChassisRebootAutoInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisRebootAutoInit.setStatus("current")


class _TmnxChassisLowTempState_Type(Integer32):
    """Custom type tmnxChassisLowTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateLowTemp", 2),
          ("stateOk", 1))
    )


_TmnxChassisLowTempState_Type.__name__ = "Integer32"
_TmnxChassisLowTempState_Object = MibTableColumn
tmnxChassisLowTempState = _TmnxChassisLowTempState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 6),
    _TmnxChassisLowTempState_Type()
)
tmnxChassisLowTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisLowTempState.setStatus("current")
_TmnxChassisSystemLEDState_Type = TmnxLEDState
_TmnxChassisSystemLEDState_Object = MibTableColumn
tmnxChassisSystemLEDState = _TmnxChassisSystemLEDState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 3, 1, 7),
    _TmnxChassisSystemLEDState_Type()
)
tmnxChassisSystemLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisSystemLEDState.setStatus("current")
_TmnxHwExtnTable_Object = MibTable
tmnxHwExtnTable = _TmnxHwExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxHwExtnTable.setStatus("current")
_TmnxHwExtnEntry_Object = MibTableRow
tmnxHwExtnEntry = _TmnxHwExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxHwExtnEntry.setStatus("current")
_TmnxHwLowTempThreshold_Type = Integer32
_TmnxHwLowTempThreshold_Object = MibTableColumn
tmnxHwLowTempThreshold = _TmnxHwLowTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 4, 1, 1),
    _TmnxHwLowTempThreshold_Type()
)
tmnxHwLowTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwLowTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHwLowTempThreshold.setUnits("degrees celsius")
_TmnxFabricPolicyTable_Object = MibTable
tmnxFabricPolicyTable = _TmnxFabricPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxFabricPolicyTable.setStatus("current")
_TmnxFabricPolicyEntry_Object = MibTableRow
tmnxFabricPolicyEntry = _TmnxFabricPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1)
)
tmnxFabricPolicyEntry.setIndexNames(
    (0, "TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyIndex"),
)
if mibBuilder.loadTexts:
    tmnxFabricPolicyEntry.setStatus("current")


class _TmnxFabricPolicyIndex_Type(TPolicyID):
    """Custom type tmnxFabricPolicyIndex based on TPolicyID"""
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxFabricPolicyIndex_Type.__name__ = "TPolicyID"
_TmnxFabricPolicyIndex_Object = MibTableColumn
tmnxFabricPolicyIndex = _TmnxFabricPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 1),
    _TmnxFabricPolicyIndex_Type()
)
tmnxFabricPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFabricPolicyIndex.setStatus("current")
_TmnxFabricPolicyRowStatus_Type = RowStatus
_TmnxFabricPolicyRowStatus_Object = MibTableColumn
tmnxFabricPolicyRowStatus = _TmnxFabricPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 2),
    _TmnxFabricPolicyRowStatus_Type()
)
tmnxFabricPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyRowStatus.setStatus("current")


class _TmnxFabricPolicyCIR_Type(TCIRRate):
    """Custom type tmnxFabricPolicyCIR based on TCIRRate"""
    defaultValue = 0


_TmnxFabricPolicyCIR_Object = MibTableColumn
tmnxFabricPolicyCIR = _TmnxFabricPolicyCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 3),
    _TmnxFabricPolicyCIR_Type()
)
tmnxFabricPolicyCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyCIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFabricPolicyCIR.setUnits("kbps")


class _TmnxFabricPolicyPIR_Type(TPIRRate):
    """Custom type tmnxFabricPolicyPIR based on TPIRRate"""
    defaultValue = 8000000


_TmnxFabricPolicyPIR_Object = MibTableColumn
tmnxFabricPolicyPIR = _TmnxFabricPolicyPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 4),
    _TmnxFabricPolicyPIR_Type()
)
tmnxFabricPolicyPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyPIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFabricPolicyPIR.setUnits("kbps")


class _TmnxFabricPolicyCBS_Type(TBurstSize):
    """Custom type tmnxFabricPolicyCBS based on TBurstSize"""
    defaultValue = 4


_TmnxFabricPolicyCBS_Object = MibTableColumn
tmnxFabricPolicyCBS = _TmnxFabricPolicyCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 5),
    _TmnxFabricPolicyCBS_Type()
)
tmnxFabricPolicyCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyCBS.setStatus("current")


class _TmnxFabricPolicyMBS_Type(TBurstSize):
    """Custom type tmnxFabricPolicyMBS based on TBurstSize"""
    defaultValue = -1


_TmnxFabricPolicyMBS_Object = MibTableColumn
tmnxFabricPolicyMBS = _TmnxFabricPolicyMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 6),
    _TmnxFabricPolicyMBS_Type()
)
tmnxFabricPolicyMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyMBS.setStatus("current")


class _TmnxFabricPolicyMpointFabricPort_Type(Integer32):
    """Custom type tmnxFabricPolicyMpointFabricPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TmnxFabricPolicyMpointFabricPort_Type.__name__ = "Integer32"
_TmnxFabricPolicyMpointFabricPort_Object = MibTableColumn
tmnxFabricPolicyMpointFabricPort = _TmnxFabricPolicyMpointFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 5, 1, 7),
    _TmnxFabricPolicyMpointFabricPort_Type()
)
tmnxFabricPolicyMpointFabricPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFabricPolicyMpointFabricPort.setStatus("current")
_TmnxChassisPowerSupplyExtnTable_Object = MibTable
tmnxChassisPowerSupplyExtnTable = _TmnxChassisPowerSupplyExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyExtnTable.setStatus("current")
_TmnxChassisPowerSupplyExtnEntry_Object = MibTableRow
tmnxChassisPowerSupplyExtnEntry = _TmnxChassisPowerSupplyExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyExtnEntry.setStatus("current")


class _TmnxChassisPowerSupplyAssignedDCType_Type(Integer32):
    """Custom type tmnxChassisPowerSupplyAssignedDCType based on Integer32"""
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
        *(("m48-dc", 1),
          ("not-applicable", 0),
          ("p24-dc", 2),
          ("unknown", 3))
    )


_TmnxChassisPowerSupplyAssignedDCType_Type.__name__ = "Integer32"
_TmnxChassisPowerSupplyAssignedDCType_Object = MibTableColumn
tmnxChassisPowerSupplyAssignedDCType = _TmnxChassisPowerSupplyAssignedDCType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 6, 1, 1),
    _TmnxChassisPowerSupplyAssignedDCType_Type()
)
tmnxChassisPowerSupplyAssignedDCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyAssignedDCType.setStatus("current")
_TmnxChassisFanExtnTable_Object = MibTable
tmnxChassisFanExtnTable = _TmnxChassisFanExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 7)
)
if mibBuilder.loadTexts:
    tmnxChassisFanExtnTable.setStatus("current")
_TmnxChassisFanExtnEntry_Object = MibTableRow
tmnxChassisFanExtnEntry = _TmnxChassisFanExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxChassisFanExtnEntry.setStatus("current")


class _TmnxChassisFanCfgMode_Type(TmnxFanCfgMode):
    """Custom type tmnxChassisFanCfgMode based on TmnxFanCfgMode"""


_TmnxChassisFanCfgMode_Object = MibTableColumn
tmnxChassisFanCfgMode = _TmnxChassisFanCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 7, 1, 1),
    _TmnxChassisFanCfgMode_Type()
)
tmnxChassisFanCfgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisFanCfgMode.setStatus("current")


class _TmnxChassisFanOperMode_Type(Integer32):
    """Custom type tmnxChassisFanOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TmnxChassisFanOperMode_Type.__name__ = "Integer32"
_TmnxChassisFanOperMode_Object = MibTableColumn
tmnxChassisFanOperMode = _TmnxChassisFanOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 7, 1, 2),
    _TmnxChassisFanOperMode_Type()
)
tmnxChassisFanOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisFanOperMode.setStatus("current")
_TmnxSASCardObjs_ObjectIdentity = ObjectIdentity
tmnxSASCardObjs = _TmnxSASCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8)
)
_TmnxCardExtnTable_Object = MibTable
tmnxCardExtnTable = _TmnxCardExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxCardExtnTable.setStatus("current")
_TmnxCardExtnEntry_Object = MibTableRow
tmnxCardExtnEntry = _TmnxCardExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxCardExtnEntry.setStatus("current")


class _TmnxCardSysResPlcyId_Type(Integer32):
    """Custom type tmnxCardSysResPlcyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxCardSysResPlcyId_Type.__name__ = "Integer32"
_TmnxCardSysResPlcyId_Object = MibTableColumn
tmnxCardSysResPlcyId = _TmnxCardSysResPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 1, 1, 1),
    _TmnxCardSysResPlcyId_Type()
)
tmnxCardSysResPlcyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardSysResPlcyId.setStatus("current")
_TmnxCpmCardExtnTable_Object = MibTable
tmnxCpmCardExtnTable = _TmnxCpmCardExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxCpmCardExtnTable.setStatus("current")
_TmnxCpmCardExtnEntry_Object = MibTableRow
tmnxCpmCardExtnEntry = _TmnxCpmCardExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxCpmCardExtnEntry.setStatus("current")
_TmnxCpmCardBootImageSource_Type = DisplayString
_TmnxCpmCardBootImageSource_Object = MibTableColumn
tmnxCpmCardBootImageSource = _TmnxCpmCardBootImageSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 8, 2, 1, 1),
    _TmnxCpmCardBootImageSource_Type()
)
tmnxCpmCardBootImageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardBootImageSource.setStatus("current")
_AluExtTmnxChassisTable_Object = MibTable
aluExtTmnxChassisTable = _AluExtTmnxChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 9)
)
if mibBuilder.loadTexts:
    aluExtTmnxChassisTable.setStatus("current")
_AluExtTmnxChassisEntry_Object = MibTableRow
aluExtTmnxChassisEntry = _AluExtTmnxChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 9, 1)
)
aluExtTmnxChassisEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    aluExtTmnxChassisEntry.setStatus("current")


class _AluExtPoePowerMode_Type(Integer32):
    """Custom type aluExtPoePowerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("none", 0))
    )


_AluExtPoePowerMode_Type.__name__ = "Integer32"
_AluExtPoePowerMode_Object = MibTableColumn
aluExtPoePowerMode = _AluExtPoePowerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 9, 1, 3),
    _AluExtPoePowerMode_Type()
)
aluExtPoePowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPoePowerMode.setStatus("current")


class _AluExtPoePowerSupplyStatus_Type(Integer32):
    """Custom type aluExtPoePowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("good", 2),
          ("none", 0))
    )


_AluExtPoePowerSupplyStatus_Type.__name__ = "Integer32"
_AluExtPoePowerSupplyStatus_Object = MibTableColumn
aluExtPoePowerSupplyStatus = _AluExtPoePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 9, 1, 4),
    _AluExtPoePowerSupplyStatus_Type()
)
aluExtPoePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPoePowerSupplyStatus.setStatus("current")


class _AluExtPoeExternalPowerSupplyStatus_Type(Integer32):
    """Custom type aluExtPoeExternalPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_AluExtPoeExternalPowerSupplyStatus_Type.__name__ = "Integer32"
_AluExtPoeExternalPowerSupplyStatus_Object = MibTableColumn
aluExtPoeExternalPowerSupplyStatus = _AluExtPoeExternalPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 9, 1, 5),
    _AluExtPoeExternalPowerSupplyStatus_Type()
)
aluExtPoeExternalPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPoeExternalPowerSupplyStatus.setStatus("current")
_TCardResOperTable_Object = MibTable
tCardResOperTable = _TCardResOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10)
)
if mibBuilder.loadTexts:
    tCardResOperTable.setStatus("current")
_TCardResOperEntry_Object = MibTableRow
tCardResOperEntry = _TCardResOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    tCardResOperEntry.setStatus("current")


class _TCardResOperIngTcamSapAggMeter_Type(Integer32):
    """Custom type tCardResOperIngTcamSapAggMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TCardResOperIngTcamSapAggMeter_Type.__name__ = "Integer32"
_TCardResOperIngTcamSapAggMeter_Object = MibTableColumn
tCardResOperIngTcamSapAggMeter = _TCardResOperIngTcamSapAggMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 1),
    _TCardResOperIngTcamSapAggMeter_Type()
)
tCardResOperIngTcamSapAggMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamSapAggMeter.setStatus("current")


class _TCardResOperIngTcamQosSapIng_Type(Integer32):
    """Custom type tCardResOperIngTcamQosSapIng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TCardResOperIngTcamQosSapIng_Type.__name__ = "Integer32"
_TCardResOperIngTcamQosSapIng_Object = MibTableColumn
tCardResOperIngTcamQosSapIng = _TCardResOperIngTcamQosSapIng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 2),
    _TCardResOperIngTcamQosSapIng_Type()
)
tCardResOperIngTcamQosSapIng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamQosSapIng.setStatus("current")


class _TCardResOperIngTcamQosSapIngIpv4_Type(Integer32):
    """Custom type tCardResOperIngTcamQosSapIngIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamQosSapIngIpv4_Type.__name__ = "Integer32"
_TCardResOperIngTcamQosSapIngIpv4_Object = MibTableColumn
tCardResOperIngTcamQosSapIngIpv4 = _TCardResOperIngTcamQosSapIngIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 3),
    _TCardResOperIngTcamQosSapIngIpv4_Type()
)
tCardResOperIngTcamQosSapIngIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamQosSapIngIpv4.setStatus("current")


class _TCardResOperIngTcamQosSapIngIpv4Ipv6_Type(Integer32):
    """Custom type tCardResOperIngTcamQosSapIngIpv4Ipv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TCardResOperIngTcamQosSapIngIpv4Ipv6_Type.__name__ = "Integer32"
_TCardResOperIngTcamQosSapIngIpv4Ipv6_Object = MibTableColumn
tCardResOperIngTcamQosSapIngIpv4Ipv6 = _TCardResOperIngTcamQosSapIngIpv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 4),
    _TCardResOperIngTcamQosSapIngIpv4Ipv6_Type()
)
tCardResOperIngTcamQosSapIngIpv4Ipv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamQosSapIngIpv4Ipv6.setStatus("current")


class _TCardResOperIngTcamQosSapIngMac_Type(Integer32):
    """Custom type tCardResOperIngTcamQosSapIngMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamQosSapIngMac_Type.__name__ = "Integer32"
_TCardResOperIngTcamQosSapIngMac_Object = MibTableColumn
tCardResOperIngTcamQosSapIngMac = _TCardResOperIngTcamQosSapIngMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 5),
    _TCardResOperIngTcamQosSapIngMac_Type()
)
tCardResOperIngTcamQosSapIngMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamQosSapIngMac.setStatus("current")


class _TCardResOperIngTcamAclSapIng_Type(Integer32):
    """Custom type tCardResOperIngTcamAclSapIng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TCardResOperIngTcamAclSapIng_Type.__name__ = "Integer32"
_TCardResOperIngTcamAclSapIng_Object = MibTableColumn
tCardResOperIngTcamAclSapIng = _TCardResOperIngTcamAclSapIng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 6),
    _TCardResOperIngTcamAclSapIng_Type()
)
tCardResOperIngTcamAclSapIng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamAclSapIng.setStatus("current")


class _TCardResOperIngTcamAclSapIngIpv4_Type(Integer32):
    """Custom type tCardResOperIngTcamAclSapIngIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamAclSapIngIpv4_Type.__name__ = "Integer32"
_TCardResOperIngTcamAclSapIngIpv4_Object = MibTableColumn
tCardResOperIngTcamAclSapIngIpv4 = _TCardResOperIngTcamAclSapIngIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 7),
    _TCardResOperIngTcamAclSapIngIpv4_Type()
)
tCardResOperIngTcamAclSapIngIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamAclSapIngIpv4.setStatus("current")


class _TCardResOperIngTcamAclSapIng64Ipv6_Type(Integer32):
    """Custom type tCardResOperIngTcamAclSapIng64Ipv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamAclSapIng64Ipv6_Type.__name__ = "Integer32"
_TCardResOperIngTcamAclSapIng64Ipv6_Object = MibTableColumn
tCardResOperIngTcamAclSapIng64Ipv6 = _TCardResOperIngTcamAclSapIng64Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 8),
    _TCardResOperIngTcamAclSapIng64Ipv6_Type()
)
tCardResOperIngTcamAclSapIng64Ipv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamAclSapIng64Ipv6.setStatus("current")


class _TCardResOperIngTcamAclSapIng128Ipv4Ipv6_Type(Integer32):
    """Custom type tCardResOperIngTcamAclSapIng128Ipv4Ipv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamAclSapIng128Ipv4Ipv6_Type.__name__ = "Integer32"
_TCardResOperIngTcamAclSapIng128Ipv4Ipv6_Object = MibTableColumn
tCardResOperIngTcamAclSapIng128Ipv4Ipv6 = _TCardResOperIngTcamAclSapIng128Ipv4Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 9),
    _TCardResOperIngTcamAclSapIng128Ipv4Ipv6_Type()
)
tCardResOperIngTcamAclSapIng128Ipv4Ipv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamAclSapIng128Ipv4Ipv6.setStatus("current")


class _TCardResOperIngTcamAclSapIngMac_Type(Integer32):
    """Custom type tCardResOperIngTcamAclSapIngMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_TCardResOperIngTcamAclSapIngMac_Type.__name__ = "Integer32"
_TCardResOperIngTcamAclSapIngMac_Object = MibTableColumn
tCardResOperIngTcamAclSapIngMac = _TCardResOperIngTcamAclSapIngMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 10),
    _TCardResOperIngTcamAclSapIngMac_Type()
)
tCardResOperIngTcamAclSapIngMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamAclSapIngMac.setStatus("current")


class _TCardResOperEgrTcamAclSapEgr_Type(Integer32):
    """Custom type tCardResOperEgrTcamAclSapEgr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TCardResOperEgrTcamAclSapEgr_Type.__name__ = "Integer32"
_TCardResOperEgrTcamAclSapEgr_Object = MibTableColumn
tCardResOperEgrTcamAclSapEgr = _TCardResOperEgrTcamAclSapEgr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 11),
    _TCardResOperEgrTcamAclSapEgr_Type()
)
tCardResOperEgrTcamAclSapEgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperEgrTcamAclSapEgr.setStatus("current")


class _TCardResOperEgrTcamAclSapEgrMacIpv4_Type(Integer32):
    """Custom type tCardResOperEgrTcamAclSapEgrMacIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TCardResOperEgrTcamAclSapEgrMacIpv4_Type.__name__ = "Integer32"
_TCardResOperEgrTcamAclSapEgrMacIpv4_Object = MibTableColumn
tCardResOperEgrTcamAclSapEgrMacIpv4 = _TCardResOperEgrTcamAclSapEgrMacIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 12),
    _TCardResOperEgrTcamAclSapEgrMacIpv4_Type()
)
tCardResOperEgrTcamAclSapEgrMacIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperEgrTcamAclSapEgrMacIpv4.setStatus("current")


class _TCardResOperEgrTcamAclSapEgr128Ipv6_Type(Integer32):
    """Custom type tCardResOperEgrTcamAclSapEgr128Ipv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TCardResOperEgrTcamAclSapEgr128Ipv6_Type.__name__ = "Integer32"
_TCardResOperEgrTcamAclSapEgr128Ipv6_Object = MibTableColumn
tCardResOperEgrTcamAclSapEgr128Ipv6 = _TCardResOperEgrTcamAclSapEgr128Ipv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 13),
    _TCardResOperEgrTcamAclSapEgr128Ipv6_Type()
)
tCardResOperEgrTcamAclSapEgr128Ipv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperEgrTcamAclSapEgr128Ipv6.setStatus("current")


class _TCardResOperEgrTcamAclSapEgr64MacIpv6_Type(Integer32):
    """Custom type tCardResOperEgrTcamAclSapEgr64MacIpv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TCardResOperEgrTcamAclSapEgr64MacIpv6_Type.__name__ = "Integer32"
_TCardResOperEgrTcamAclSapEgr64MacIpv6_Object = MibTableColumn
tCardResOperEgrTcamAclSapEgr64MacIpv6 = _TCardResOperEgrTcamAclSapEgr64MacIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 14),
    _TCardResOperEgrTcamAclSapEgr64MacIpv6_Type()
)
tCardResOperEgrTcamAclSapEgr64MacIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperEgrTcamAclSapEgr64MacIpv6.setStatus("current")


class _TCardResOperEgrTcamAclSapEgrMac_Type(Integer32):
    """Custom type tCardResOperEgrTcamAclSapEgrMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_TCardResOperEgrTcamAclSapEgrMac_Type.__name__ = "Integer32"
_TCardResOperEgrTcamAclSapEgrMac_Object = MibTableColumn
tCardResOperEgrTcamAclSapEgrMac = _TCardResOperEgrTcamAclSapEgrMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 15),
    _TCardResOperEgrTcamAclSapEgrMac_Type()
)
tCardResOperEgrTcamAclSapEgrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperEgrTcamAclSapEgrMac.setStatus("current")


class _TCardResOperIngTcamEthCfm_Type(Integer32):
    """Custom type tCardResOperIngTcamEthCfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TCardResOperIngTcamEthCfm_Type.__name__ = "Integer32"
_TCardResOperIngTcamEthCfm_Object = MibTableColumn
tCardResOperIngTcamEthCfm = _TCardResOperIngTcamEthCfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 18),
    _TCardResOperIngTcamEthCfm_Type()
)
tCardResOperIngTcamEthCfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamEthCfm.setStatus("current")


class _TCardResOperIngTcamEthCfmUpMep_Type(Integer32):
    """Custom type tCardResOperIngTcamEthCfmUpMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TCardResOperIngTcamEthCfmUpMep_Type.__name__ = "Integer32"
_TCardResOperIngTcamEthCfmUpMep_Object = MibTableColumn
tCardResOperIngTcamEthCfmUpMep = _TCardResOperIngTcamEthCfmUpMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 19),
    _TCardResOperIngTcamEthCfmUpMep_Type()
)
tCardResOperIngTcamEthCfmUpMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamEthCfmUpMep.setStatus("current")


class _TCardResOperG8032CtrlSapStartVlan_Type(Unsigned32):
    """Custom type tCardResOperG8032CtrlSapStartVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TCardResOperG8032CtrlSapStartVlan_Type.__name__ = "Unsigned32"
_TCardResOperG8032CtrlSapStartVlan_Object = MibTableColumn
tCardResOperG8032CtrlSapStartVlan = _TCardResOperG8032CtrlSapStartVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 20),
    _TCardResOperG8032CtrlSapStartVlan_Type()
)
tCardResOperG8032CtrlSapStartVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperG8032CtrlSapStartVlan.setStatus("current")


class _TCardResOperG8032CtrlSapEndVlan_Type(Unsigned32):
    """Custom type tCardResOperG8032CtrlSapEndVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TCardResOperG8032CtrlSapEndVlan_Type.__name__ = "Unsigned32"
_TCardResOperG8032CtrlSapEndVlan_Object = MibTableColumn
tCardResOperG8032CtrlSapEndVlan = _TCardResOperG8032CtrlSapEndVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 21),
    _TCardResOperG8032CtrlSapEndVlan_Type()
)
tCardResOperG8032CtrlSapEndVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperG8032CtrlSapEndVlan.setStatus("current")


class _TCardResOperResIpMacMatchEnable_Type(Integer32):
    """Custom type tCardResOperResIpMacMatchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10),
    )


_TCardResOperResIpMacMatchEnable_Type.__name__ = "Integer32"
_TCardResOperResIpMacMatchEnable_Object = MibTableColumn
tCardResOperResIpMacMatchEnable = _TCardResOperResIpMacMatchEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 22),
    _TCardResOperResIpMacMatchEnable_Type()
)
tCardResOperResIpMacMatchEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperResIpMacMatchEnable.setStatus("current")


class _TCardResOperIngTcamEthCfmDownMep_Type(Integer32):
    """Custom type tCardResOperIngTcamEthCfmDownMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TCardResOperIngTcamEthCfmDownMep_Type.__name__ = "Integer32"
_TCardResOperIngTcamEthCfmDownMep_Object = MibTableColumn
tCardResOperIngTcamEthCfmDownMep = _TCardResOperIngTcamEthCfmDownMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 23),
    _TCardResOperIngTcamEthCfmDownMep_Type()
)
tCardResOperIngTcamEthCfmDownMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamEthCfmDownMep.setStatus("current")


class _TCardResOperIngTcamIpMulticast_Type(Integer32):
    """Custom type tCardResOperIngTcamIpMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TCardResOperIngTcamIpMulticast_Type.__name__ = "Integer32"
_TCardResOperIngTcamIpMulticast_Object = MibTableColumn
tCardResOperIngTcamIpMulticast = _TCardResOperIngTcamIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 10, 1, 24),
    _TCardResOperIngTcamIpMulticast_Type()
)
tCardResOperIngTcamIpMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCardResOperIngTcamIpMulticast.setStatus("current")
_TmnxSASSecurityObjects_ObjectIdentity = ObjectIdentity
tmnxSASSecurityObjects = _TmnxSASSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15)
)
_TmnxSASSecurityNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxSASSecurityNotificationObjs = _TmnxSASSecurityNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15, 5)
)


class _TmnxLoginUserName_Type(TNamedItem):
    """Custom type tmnxLoginUserName based on TNamedItem"""
    subtypeSpec = TNamedItem.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TmnxLoginUserName_Type.__name__ = "TNamedItem"
_TmnxLoginUserName_Object = MibScalar
tmnxLoginUserName = _TmnxLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15, 5, 1),
    _TmnxLoginUserName_Type()
)
tmnxLoginUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLoginUserName.setStatus("current")


class _TmnxLoginUserSrcIPAddress_Type(InetAddress):
    """Custom type tmnxLoginUserSrcIPAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLoginUserSrcIPAddress_Type.__name__ = "InetAddress"
_TmnxLoginUserSrcIPAddress_Object = MibScalar
tmnxLoginUserSrcIPAddress = _TmnxLoginUserSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15, 5, 2),
    _TmnxLoginUserSrcIPAddress_Type()
)
tmnxLoginUserSrcIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLoginUserSrcIPAddress.setStatus("current")
_TmnxLoginMaxAttempts_Type = Integer32
_TmnxLoginMaxAttempts_Object = MibScalar
tmnxLoginMaxAttempts = _TmnxLoginMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15, 5, 3),
    _TmnxLoginMaxAttempts_Type()
)
tmnxLoginMaxAttempts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLoginMaxAttempts.setStatus("current")
_TmnxChassisNotifyMDACfgFailReason_Type = DisplayString
_TmnxChassisNotifyMDACfgFailReason_Object = MibScalar
tmnxChassisNotifyMDACfgFailReason = _TmnxChassisNotifyMDACfgFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 15, 5, 4),
    _TmnxChassisNotifyMDACfgFailReason_Type()
)
tmnxChassisNotifyMDACfgFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyMDACfgFailReason.setStatus("current")
_TmnxSASSysMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSASSysMIBNotifyPrefix = _TmnxSASSysMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 1)
)
_TmnxSASSysNotifications_ObjectIdentity = ObjectIdentity
tmnxSASSysNotifications = _TmnxSASSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 1, 3)
)
_TmnxSASSecurityNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSASSecurityNotifyPrefix = _TmnxSASSecurityNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 2)
)
_TmnxSASSecurityNotifications_ObjectIdentity = ObjectIdentity
tmnxSASSecurityNotifications = _TmnxSASSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 2, 0)
)
tmnxChassisEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxChassisExtnEntry")
)
tmnxChassisExtnEntry.setIndexNames(*tmnxChassisEntry.getIndexNames())
tmnxHwEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxHwExtnEntry")
)
tmnxHwExtnEntry.setIndexNames(*tmnxHwEntry.getIndexNames())
tmnxChassisPowerSupplyEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxChassisPowerSupplyExtnEntry")
)
tmnxChassisPowerSupplyExtnEntry.setIndexNames(*tmnxChassisPowerSupplyEntry.getIndexNames())
tmnxChassisFanEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxChassisFanExtnEntry")
)
tmnxChassisFanExtnEntry.setIndexNames(*tmnxChassisFanEntry.getIndexNames())
tmnxCardEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxCardExtnEntry")
)
tmnxCardExtnEntry.setIndexNames(*tmnxCardEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tmnxCpmCardExtnEntry")
)
tmnxCpmCardExtnEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("TIMETRA-SAS-SYSTEM-MIB",
     "tCardResOperEntry")
)
tCardResOperEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())

# Managed Objects groups

tmnxSASSysV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 1)
)
tmnxSASSysV1v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAIpAddr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAMask"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBIpAddr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBMask"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiPingAddress"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteNextHop"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteRowStatus"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisUpdateGoldenBootstrapImage"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisGoldenBootstrapImageSrc"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisValidateGoldenBootstrapImage"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisGoldenBootstrapImageVersion"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisRebootAutoInit"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV1v0Group.setStatus("obsolete")

tmnxSASSysV2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 2)
)
tmnxSASSysV2v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tSASMpointBwPlcy"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAIpAddr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAMask"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkAVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBIpAddr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBMask"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkBVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiPingAddress"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteNextHop"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiUplinkRouteRowStatus"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisUpdateGoldenBootstrapImage"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisGoldenBootstrapImageSrc"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisValidateGoldenBootstrapImage"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisGoldenBootstrapImageVersion"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisRebootAutoInit"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtDisabled"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtActiveIpAddr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtActiveIpMask"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtAutoNegotiate"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtSpeed"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtDuplex"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtStaticRouteNextHop"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sbiEthMgmtStaticRouteRowStatus"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisLowTempState"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV2v0Group.setStatus("current")

tmnxSASSysV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 3)
)
tmnxSASSysV3v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "sbiExpansionCardType"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyRowStatus"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyCIR"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyPIR"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyCBS"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyMBS"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxFabricPolicyMpointFabricPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisPowerSupplyAssignedDCType"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV3v0Group.setStatus("current")

tmnxSASSysV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 4)
)
tmnxSASSysV4v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "sbiConsoleDisabled"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysLoopbackNoServPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysG8032FastFloodEnable"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysMirrorLoopbackNoServPort"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResFabricPathBandwidth"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResMaxIPv6Routes"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamEthCfm"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamEthCfmUpMep"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysG8032FastFloodEnableOperVal"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV4v0Group.setStatus("current")

tmnxSASSysV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 5)
)
tmnxSASSysV5v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamIngAclMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamSapEgrAcl"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamEgrAclMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamEgrAclIpv4"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamEgrAcl64bitIpv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamEgrAcl128bitIpv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrTcamEgrAcl64bitIpv6Only"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrSapEgrClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrSapEgrClassMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrSapEgrClassIpv4"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResEgrSapEgrClassIpv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamSapAggMeter"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamSapAggMeterOperVal"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisFanCfgMode"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisFanOperMode"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResIngTcamIngAcl64bitIpv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxPtpTimeUsePtp"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResQosSapIngQMode"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResQosSapIngQOperMode"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResRouterEcmpMaxRoutesDst"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysResRouterEcmpMaxRoutesDstOperVal"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysTestHdNoServPort"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV5v0Group.setStatus("current")

tmnxSASSysObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 6)
)
tmnxSASSysObjsV6v0Group.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxSysConsoleAlarmInput")
)
if mibBuilder.loadTexts:
    tmnxSASSysObjsV6v0Group.setStatus("current")

tmnxSASSysQosV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 7)
)
tmnxSASSysQosV5v0Group.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "sysQosWredSlopes")
)
if mibBuilder.loadTexts:
    tmnxSASSysQosV5v0Group.setStatus("current")

tmnxSASSysV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 8)
)
tmnxSASSysV6v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "sysDhcpSnoopingSdpEnable"),
        ("TIMETRA-SAS-SYSTEM-MIB", "sysDhcpSnoopingEnable"))
)
if mibBuilder.loadTexts:
    tmnxSASSysV6v0Group.setStatus("current")

tmnxSASSysConsoleV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 9)
)
tmnxSASSysConsoleV6v0Group.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxSysConsoleAlarmInput")
)
if mibBuilder.loadTexts:
    tmnxSASSysConsoleV6v0Group.setStatus("current")

tmnxSASSysResPlcyV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 2, 10)
)
tmnxSASSysResPlcyV6v1Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyRowStatus"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamSapAggMeter"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamQosSapIng"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamQosSapIngIpv4"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamQosSapIngIpv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamQosSapIngMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamAclSapIng"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamAclSapIngIpv4"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamAclSapIng64Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamAclSapIng128Ipv4Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamAclSapIngMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyEgrTcamAclSapEgr"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyEgrTcamAclSapEgrMacIpv4"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyEgrTcamAclSapEgr128Ipv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyEgrTcamAclSapEgr64MacIpv6"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyEgrTcamAclSapEgrMac"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyDescription"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyLastChanged"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamEthCfm"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamEthCfmUpMep"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyG8032CtrlSapStartVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyG8032CtrlSapEndVlan"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyResIpMacMatchEnable"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamEthCfmDownMep"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamEthCfmUpMepEnable"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tResPlcyIngTcamEthCfmDownMepEnable"))
)
if mibBuilder.loadTexts:
    tmnxSASSysResPlcyV6v1Group.setStatus("current")

tmnxSASSysSecV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 4, 1, 1)
)
tmnxSASSysSecV4v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserName"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserSrcIPAddress"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginMaxAttempts"))
)
if mibBuilder.loadTexts:
    tmnxSASSysSecV4v0Group.setStatus("current")

tmnxSASChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 10, 2)
)
tmnxSASChassisGroup.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisSystemLEDState")
)
if mibBuilder.loadTexts:
    tmnxSASChassisGroup.setStatus("current")

tmnxSASChassisV61Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 10, 3)
)
tmnxSASChassisV61Group.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxCpmCardBootImageSource")
)
if mibBuilder.loadTexts:
    tmnxSASChassisV61Group.setStatus("current")


# Notification objects

tmnxEnvTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 1)
)
tmnxEnvTempTooLow.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxHwLowTempThreshold"))
)
if mibBuilder.loadTexts:
    tmnxEnvTempTooLow.setStatus(
        "current"
    )

tmnxRootDirFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 2)
)
tmnxRootDirFull.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwName"))
)
if mibBuilder.loadTexts:
    tmnxRootDirFull.setStatus(
        "current"
    )

tmnxEqPowerInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 3)
)
tmnxEqPowerInputFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyInputStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerInputFailure.setStatus(
        "current"
    )

tmnxEqPowerOutputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 4)
)
tmnxEqPowerOutputFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerOutputFailure.setStatus(
        "current"
    )

tmnxEqMDACfgMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 5)
)
tmnxEqMDACfgMissing.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxChassisNotifyMDACfgFailReason"))
)
if mibBuilder.loadTexts:
    tmnxEqMDACfgMissing.setStatus(
        "current"
    )

tmnxVwmShelfInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 6)
)
tmnxVwmShelfInserted.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfId")
)
if mibBuilder.loadTexts:
    tmnxVwmShelfInserted.setStatus(
        "current"
    )

tmnxVwmShelfIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 7)
)
tmnxVwmShelfIdMismatch.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfId")
)
if mibBuilder.loadTexts:
    tmnxVwmShelfIdMismatch.setStatus(
        "current"
    )

tmnxVwmShelfRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 8)
)
tmnxVwmShelfRemoved.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfId")
)
if mibBuilder.loadTexts:
    tmnxVwmShelfRemoved.setStatus(
        "current"
    )

tmnxUsbUnknownDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxUsbUnknownDev.setStatus(
        "current"
    )

tmnxAlarmInputVoltageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 10)
)
tmnxAlarmInputVoltageFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxAlarmInputVoltageFailure.setStatus(
        "current"
    )

tmnxVwmShelfCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 11)
)
tmnxVwmShelfCardInserted.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardInserted.setStatus(
        "current"
    )

tmnxVwmShelfCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 12)
)
tmnxVwmShelfCardRemoved.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardRemoved.setStatus(
        "current"
    )

tmnxVwmShelfCardIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 13)
)
tmnxVwmShelfCardIdMismatch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardIdMismatch.setStatus(
        "current"
    )

tmnxVwmShelfPSInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 14)
)
tmnxVwmShelfPSInputFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfPSInputFailure.setStatus(
        "current"
    )

tmnxVwmShelfPSOutputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 15)
)
tmnxVwmShelfPSOutputFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfPSOutputFailure.setStatus(
        "current"
    )

tmnxVwmShelfInputLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 16)
)
tmnxVwmShelfInputLoss.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfInputLoss.setStatus(
        "current"
    )

tmnxVwmShelfOutputLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 17)
)
tmnxVwmShelfOutputLoss.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfOutputLoss.setStatus(
        "current"
    )

tmnxVwmShelfCardCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 18)
)
tmnxVwmShelfCardCfgError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxVwmShelfCardId"))
)
if mibBuilder.loadTexts:
    tmnxVwmShelfCardCfgError.setStatus(
        "current"
    )

sysOperGrpOperStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 6, 2, 25)
)
sysOperGrpOperStatusChanged.setObjects(
    ("TIMETRA-SAS-SYSTEM-MIB", "sysOperGrpOperStatus")
)
if mibBuilder.loadTexts:
    sysOperGrpOperStatusChanged.setStatus(
        "current"
    )

tmnxDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxDyingGasp.setStatus(
        "current"
    )

tmnxUserLoginMaxAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 2, 0, 1)
)
tmnxUserLoginMaxAttempts.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserName"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserSrcIPAddress"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginMaxAttempts"))
)
if mibBuilder.loadTexts:
    tmnxUserLoginMaxAttempts.setStatus(
        "current"
    )

tmnxSSHUserLoginMaxAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 2, 0, 3)
)
tmnxSSHUserLoginMaxAttempts.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserName"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginUserSrcIPAddress"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxLoginMaxAttempts"))
)
if mibBuilder.loadTexts:
    tmnxSSHUserLoginMaxAttempts.setStatus(
        "current"
    )


# Notifications groups

tmnxSASSysSecNotifyV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 3, 4, 1, 2)
)
tmnxSASSysSecNotifyV4v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tmnxUserLoginMaxAttempts"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxSSHUserLoginMaxAttempts"))
)
if mibBuilder.loadTexts:
    tmnxSASSysSecNotifyV4v0Group.setStatus(
        "current"
    )

tmnxSASChassisNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 10, 1)
)
tmnxSASChassisNotificationV3v0Group.setObjects(
      *(("TIMETRA-SAS-SYSTEM-MIB", "tmnxEnvTempTooLow"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxRootDirFull"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxEqPowerInputFailure"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxEqPowerOutputFailure"),
        ("TIMETRA-SAS-SYSTEM-MIB", "tmnxEqMDACfgMissing"))
)
if mibBuilder.loadTexts:
    tmnxSASChassisNotificationV3v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-SYSTEM-MIB",
    **{"TmnxFanCfgMode": TmnxFanCfgMode,
       "TmnxPtpTime": TmnxPtpTime,
       "TmnxSysOperGrpCreationOrigin": TmnxSysOperGrpCreationOrigin,
       "timetraSASysMIBModule": timetraSASysMIBModule,
       "tmnxSASSysConformance": tmnxSASSysConformance,
       "tmnxSASSysCompliances": tmnxSASSysCompliances,
       "tmnxSASSysGroups": tmnxSASSysGroups,
       "tmnxSASSysV1v0Group": tmnxSASSysV1v0Group,
       "tmnxSASSysV2v0Group": tmnxSASSysV2v0Group,
       "tmnxSASSysV3v0Group": tmnxSASSysV3v0Group,
       "tmnxSASSysV4v0Group": tmnxSASSysV4v0Group,
       "tmnxSASSysV5v0Group": tmnxSASSysV5v0Group,
       "tmnxSASSysObjsV6v0Group": tmnxSASSysObjsV6v0Group,
       "tmnxSASSysQosV5v0Group": tmnxSASSysQosV5v0Group,
       "tmnxSASSysV6v0Group": tmnxSASSysV6v0Group,
       "tmnxSASSysConsoleV6v0Group": tmnxSASSysConsoleV6v0Group,
       "tmnxSASSysResPlcyV6v1Group": tmnxSASSysResPlcyV6v1Group,
       "tmnxSASSysSecConformance": tmnxSASSysSecConformance,
       "tmnxSASSysSecGroups": tmnxSASSysSecGroups,
       "tmnxSASSysSecV4v0Group": tmnxSASSysSecV4v0Group,
       "tmnxSASSysSecNotifyV4v0Group": tmnxSASSysSecNotifyV4v0Group,
       "tmnxSASChassisGroups": tmnxSASChassisGroups,
       "tmnxSASChassisNotificationV3v0Group": tmnxSASChassisNotificationV3v0Group,
       "tmnxSASChassisGroup": tmnxSASChassisGroup,
       "tmnxSASChassisV61Group": tmnxSASChassisV61Group,
       "tmnxSASSysObjs": tmnxSASSysObjs,
       "sysSASBofInfo": sysSASBofInfo,
       "sbiUplinkAPort": sbiUplinkAPort,
       "sbiUplinkAIpAddr": sbiUplinkAIpAddr,
       "sbiUplinkAMask": sbiUplinkAMask,
       "sbiUplinkAVlan": sbiUplinkAVlan,
       "sbiUplinkBPort": sbiUplinkBPort,
       "sbiUplinkBIpAddr": sbiUplinkBIpAddr,
       "sbiUplinkBMask": sbiUplinkBMask,
       "sbiUplinkBVlan": sbiUplinkBVlan,
       "sbiPingAddress": sbiPingAddress,
       "sbiUplinkRouteTable": sbiUplinkRouteTable,
       "sbiUplinkRouteEntry": sbiUplinkRouteEntry,
       "sbiUplinkAorB": sbiUplinkAorB,
       "sbiUplinkRouteDest": sbiUplinkRouteDest,
       "sbiUplinkRouteMask": sbiUplinkRouteMask,
       "sbiUplinkRouteNextHop": sbiUplinkRouteNextHop,
       "sbiUplinkRouteRowStatus": sbiUplinkRouteRowStatus,
       "sbiNoServicePortOne": sbiNoServicePortOne,
       "sbiNoServicePortTwo": sbiNoServicePortTwo,
       "sbiUplinkAdminMode": sbiUplinkAdminMode,
       "sbiUplinkOperMode": sbiUplinkOperMode,
       "sbiExpansionCardType": sbiExpansionCardType,
       "sbiConsoleDisabled": sbiConsoleDisabled,
       "sbiPassword": sbiPassword,
       "sbiUplinkAAutoNegotiate": sbiUplinkAAutoNegotiate,
       "sbiUplinkASpeed": sbiUplinkASpeed,
       "sbiUplinkADuplex": sbiUplinkADuplex,
       "sbiUplinkBAutoNegotiate": sbiUplinkBAutoNegotiate,
       "sbiUplinkBSpeed": sbiUplinkBSpeed,
       "sbiUplinkBDuplex": sbiUplinkBDuplex,
       "sysEthMgmtBofInfo": sysEthMgmtBofInfo,
       "sbiEthMgmtDisabled": sbiEthMgmtDisabled,
       "sbiEthMgmtActiveIpAddr": sbiEthMgmtActiveIpAddr,
       "sbiEthMgmtActiveIpMask": sbiEthMgmtActiveIpMask,
       "sbiEthMgmtAutoNegotiate": sbiEthMgmtAutoNegotiate,
       "sbiEthMgmtSpeed": sbiEthMgmtSpeed,
       "sbiEthMgmtDuplex": sbiEthMgmtDuplex,
       "sbiEthMgmtStaticRouteTable": sbiEthMgmtStaticRouteTable,
       "sbiEthMgmtStaticRouteEntry": sbiEthMgmtStaticRouteEntry,
       "sbiEthMgmtStaticRouteDest": sbiEthMgmtStaticRouteDest,
       "sbiEthMgmtStaticRouteMask": sbiEthMgmtStaticRouteMask,
       "sbiEthMgmtStaticRouteNextHop": sbiEthMgmtStaticRouteNextHop,
       "sbiEthMgmtStaticRouteRowStatus": sbiEthMgmtStaticRouteRowStatus,
       "sysMpointMgmtInfo": sysMpointMgmtInfo,
       "tSASMpointBwPlcy": tSASMpointBwPlcy,
       "sysLoopBackInfo": sysLoopBackInfo,
       "sysLoopbackNoServPort": sysLoopbackNoServPort,
       "sysMirrorLoopbackNoServPort": sysMirrorLoopbackNoServPort,
       "sysTestHdNoServPort": sysTestHdNoServPort,
       "sysResourceProfInfo": sysResourceProfInfo,
       "sysG8032FastFloodEnable": sysG8032FastFloodEnable,
       "sysResIngTcamSapIngAcl": sysResIngTcamSapIngAcl,
       "sysResIngTcamIngAclMac": sysResIngTcamIngAclMac,
       "sysResIngTcamIngAclIpv4": sysResIngTcamIngAclIpv4,
       "sysResIngTcamIngAcl64bitIpv4Ipv6": sysResIngTcamIngAcl64bitIpv4Ipv6,
       "sysResIngTcamIngAcl128bitIpv4Ipv6": sysResIngTcamIngAcl128bitIpv4Ipv6,
       "sysResIngTcamIngAcl64bitIpv6Only": sysResIngTcamIngAcl64bitIpv6Only,
       "sysResIngSapIngClass": sysResIngSapIngClass,
       "sysResIngSapIngClassMac": sysResIngSapIngClassMac,
       "sysResIngSapIngClassIpv4": sysResIngSapIngClassIpv4,
       "sysResIngSapIngClassIpv4Ipv6": sysResIngSapIngClassIpv4Ipv6,
       "sysResFabricPathBandwidth": sysResFabricPathBandwidth,
       "sysResMaxIPv6Routes": sysResMaxIPv6Routes,
       "sysResIngTcamEthCfm": sysResIngTcamEthCfm,
       "sysResIngTcamEthCfmUpMep": sysResIngTcamEthCfmUpMep,
       "sysG8032FastFloodEnableOperVal": sysG8032FastFloodEnableOperVal,
       "sysResEgrTcamSapEgrAcl": sysResEgrTcamSapEgrAcl,
       "sysResEgrTcamEgrAclMac": sysResEgrTcamEgrAclMac,
       "sysResEgrTcamEgrAclIpv4": sysResEgrTcamEgrAclIpv4,
       "sysResEgrTcamEgrAcl64bitIpv4Ipv6": sysResEgrTcamEgrAcl64bitIpv4Ipv6,
       "sysResEgrTcamEgrAcl128bitIpv4Ipv6": sysResEgrTcamEgrAcl128bitIpv4Ipv6,
       "sysResEgrTcamEgrAcl64bitIpv6Only": sysResEgrTcamEgrAcl64bitIpv6Only,
       "sysResEgrSapEgrClass": sysResEgrSapEgrClass,
       "sysResEgrSapEgrClassMac": sysResEgrSapEgrClassMac,
       "sysResEgrSapEgrClassIpv4": sysResEgrSapEgrClassIpv4,
       "sysResEgrSapEgrClassIpv4Ipv6": sysResEgrSapEgrClassIpv4Ipv6,
       "sysResIngTcamSapAggMeter": sysResIngTcamSapAggMeter,
       "sysResIngTcamSapAggMeterOperVal": sysResIngTcamSapAggMeterOperVal,
       "sysResQosSapIngQMode": sysResQosSapIngQMode,
       "sysResQosSapIngQOperMode": sysResQosSapIngQOperMode,
       "sysResRouterEcmpMaxRoutesDst": sysResRouterEcmpMaxRoutesDst,
       "sysDhcpSnoopingSdpEnable": sysDhcpSnoopingSdpEnable,
       "sysDhcpSnoopingEnable": sysDhcpSnoopingEnable,
       "sysResRouterEcmpMaxRoutesDstOperVal": sysResRouterEcmpMaxRoutesDstOperVal,
       "sysResIpMacMatchEnable": sysResIpMacMatchEnable,
       "sysG8032FastFlood": sysG8032FastFlood,
       "sysResIngTcamEthCfmDownMep": sysResIngTcamEthCfmDownMep,
       "sysResQosMbsPool": sysResQosMbsPool,
       "sysResIngTcamEthCfmUpMepPrimaryVlan": sysResIngTcamEthCfmUpMepPrimaryVlan,
       "sysResIngTcamEthCfmDownMepPrimaryVlan": sysResIngTcamEthCfmDownMepPrimaryVlan,
       "sysResRouterMaxIPSubnets": sysResRouterMaxIPSubnets,
       "sysQosPortSchedModeEnable": sysQosPortSchedModeEnable,
       "sysResMaxIPv6RoutesOperVal": sysResMaxIPv6RoutesOperVal,
       "sysSASObjs": sysSASObjs,
       "tmnxSysConsoleAlarmInput": tmnxSysConsoleAlarmInput,
       "sysSASVwmObjs": sysSASVwmObjs,
       "tmnxVwmShelfTable": tmnxVwmShelfTable,
       "tmnxVwmShelfEntry": tmnxVwmShelfEntry,
       "tmnxVwmShelfId": tmnxVwmShelfId,
       "tmnxVwmShelfRowStatus": tmnxVwmShelfRowStatus,
       "tmnxVwmShelfAdminState": tmnxVwmShelfAdminState,
       "tmnxVwmShelfOperState": tmnxVwmShelfOperState,
       "tmnxVwmShelfVwmType": tmnxVwmShelfVwmType,
       "tmnxVwmShelfEquippedType": tmnxVwmShelfEquippedType,
       "tmnxVwmshelfTypeConnected": tmnxVwmshelfTypeConnected,
       "tmnxVwmShelfCardTable": tmnxVwmShelfCardTable,
       "tmnxVwmShelfCardEntry": tmnxVwmShelfCardEntry,
       "tmnxVwmShelfCardId": tmnxVwmShelfCardId,
       "tmnxVwmShelfCardType": tmnxVwmShelfCardType,
       "tmnxVwmShelfCardEqType": tmnxVwmShelfCardEqType,
       "tmnxVwmShelfCardAdminState": tmnxVwmShelfCardAdminState,
       "tmnxVwmShelfCardOperState": tmnxVwmShelfCardOperState,
       "sysQosObjs": sysQosObjs,
       "sysQosWredSlopes": sysQosWredSlopes,
       "sysClockInfo": sysClockInfo,
       "tmnxPtpTimeUsePtp": tmnxPtpTimeUsePtp,
       "sysResProfPlcyObjs": sysResProfPlcyObjs,
       "tResPlcyTable": tResPlcyTable,
       "tResPlcyEntry": tResPlcyEntry,
       "tResPlcyId": tResPlcyId,
       "tResPlcyRowStatus": tResPlcyRowStatus,
       "tResPlcyIngTcamSapAggMeter": tResPlcyIngTcamSapAggMeter,
       "tResPlcyIngTcamQosSapIng": tResPlcyIngTcamQosSapIng,
       "tResPlcyIngTcamQosSapIngIpv4": tResPlcyIngTcamQosSapIngIpv4,
       "tResPlcyIngTcamQosSapIngIpv4Ipv6": tResPlcyIngTcamQosSapIngIpv4Ipv6,
       "tResPlcyIngTcamQosSapIngMac": tResPlcyIngTcamQosSapIngMac,
       "tResPlcyIngTcamAclSapIng": tResPlcyIngTcamAclSapIng,
       "tResPlcyIngTcamAclSapIngIpv4": tResPlcyIngTcamAclSapIngIpv4,
       "tResPlcyIngTcamAclSapIng64Ipv6": tResPlcyIngTcamAclSapIng64Ipv6,
       "tResPlcyIngTcamAclSapIng128Ipv4Ipv6": tResPlcyIngTcamAclSapIng128Ipv4Ipv6,
       "tResPlcyIngTcamAclSapIngMac": tResPlcyIngTcamAclSapIngMac,
       "tResPlcyEgrTcamAclSapEgr": tResPlcyEgrTcamAclSapEgr,
       "tResPlcyEgrTcamAclSapEgrMacIpv4": tResPlcyEgrTcamAclSapEgrMacIpv4,
       "tResPlcyEgrTcamAclSapEgr128Ipv6": tResPlcyEgrTcamAclSapEgr128Ipv6,
       "tResPlcyEgrTcamAclSapEgr64MacIpv6": tResPlcyEgrTcamAclSapEgr64MacIpv6,
       "tResPlcyEgrTcamAclSapEgrMac": tResPlcyEgrTcamAclSapEgrMac,
       "tResPlcyDescription": tResPlcyDescription,
       "tResPlcyLastChanged": tResPlcyLastChanged,
       "tResPlcyIngTcamEthCfm": tResPlcyIngTcamEthCfm,
       "tResPlcyIngTcamEthCfmUpMep": tResPlcyIngTcamEthCfmUpMep,
       "tResPlcyG8032CtrlSapStartVlan": tResPlcyG8032CtrlSapStartVlan,
       "tResPlcyG8032CtrlSapEndVlan": tResPlcyG8032CtrlSapEndVlan,
       "tResPlcyResIpMacMatchEnable": tResPlcyResIpMacMatchEnable,
       "tResPlcyIngTcamEthCfmDownMep": tResPlcyIngTcamEthCfmDownMep,
       "tResPlcyIngTcamEthCfmUpMepEnable": tResPlcyIngTcamEthCfmUpMepEnable,
       "tResPlcyIngTcamEthCfmDownMepEnable": tResPlcyIngTcamEthCfmDownMepEnable,
       "sysResProfDecommObjs": sysResProfDecommObjs,
       "tResDecommTable": tResDecommTable,
       "tResDecommEntry": tResDecommEntry,
       "tResDecommId": tResDecommId,
       "tResDecommRowStatus": tResDecommRowStatus,
       "tResDecommFromPortMap": tResDecommFromPortMap,
       "tResDecommToPortMap": tResDecommToPortMap,
       "tResDecommOperTable": tResDecommOperTable,
       "tResDecommOperEntry": tResDecommOperEntry,
       "tResDecommOperId": tResDecommOperId,
       "tResDecommOperFromPortMap": tResDecommOperFromPortMap,
       "tResDecommOperToPortMap": tResDecommOperToPortMap,
       "sysOperGrpObjs": sysOperGrpObjs,
       "sysOperGrpTblLastChanged": sysOperGrpTblLastChanged,
       "sysOperGrpTable": sysOperGrpTable,
       "sysOperGrpEntry": sysOperGrpEntry,
       "sysOperGrpName": sysOperGrpName,
       "sysOperGrpRowStatus": sysOperGrpRowStatus,
       "sysOperGrpLastChange": sysOperGrpLastChange,
       "sysOperGrpOperStatus": sysOperGrpOperStatus,
       "sysOperGrpHoldDownTime": sysOperGrpHoldDownTime,
       "sysOperGrpCreationOrigin": sysOperGrpCreationOrigin,
       "sysOperGrpHoldUpTime": sysOperGrpHoldUpTime,
       "sysOperGrpHoldUpTimeRemain": sysOperGrpHoldUpTimeRemain,
       "sysOperGrpHoldDownTimeRemain": sysOperGrpHoldDownTimeRemain,
       "sysOperGrpNumMembers": sysOperGrpNumMembers,
       "sysOperGrpNumMonitoring": sysOperGrpNumMonitoring,
       "tmnxSASChassisObjs": tmnxSASChassisObjs,
       "tmnxSASChassisNotificationObjs": tmnxSASChassisNotificationObjs,
       "tmnxSASChassisNotification": tmnxSASChassisNotification,
       "tmnxEnvTempTooLow": tmnxEnvTempTooLow,
       "tmnxRootDirFull": tmnxRootDirFull,
       "tmnxEqPowerInputFailure": tmnxEqPowerInputFailure,
       "tmnxEqPowerOutputFailure": tmnxEqPowerOutputFailure,
       "tmnxEqMDACfgMissing": tmnxEqMDACfgMissing,
       "tmnxVwmShelfInserted": tmnxVwmShelfInserted,
       "tmnxVwmShelfIdMismatch": tmnxVwmShelfIdMismatch,
       "tmnxVwmShelfRemoved": tmnxVwmShelfRemoved,
       "tmnxUsbUnknownDev": tmnxUsbUnknownDev,
       "tmnxAlarmInputVoltageFailure": tmnxAlarmInputVoltageFailure,
       "tmnxVwmShelfCardInserted": tmnxVwmShelfCardInserted,
       "tmnxVwmShelfCardRemoved": tmnxVwmShelfCardRemoved,
       "tmnxVwmShelfCardIdMismatch": tmnxVwmShelfCardIdMismatch,
       "tmnxVwmShelfPSInputFailure": tmnxVwmShelfPSInputFailure,
       "tmnxVwmShelfPSOutputFailure": tmnxVwmShelfPSOutputFailure,
       "tmnxVwmShelfInputLoss": tmnxVwmShelfInputLoss,
       "tmnxVwmShelfOutputLoss": tmnxVwmShelfOutputLoss,
       "tmnxVwmShelfCardCfgError": tmnxVwmShelfCardCfgError,
       "sysOperGrpOperStatusChanged": sysOperGrpOperStatusChanged,
       "tmnxChassisExtnTable": tmnxChassisExtnTable,
       "tmnxChassisExtnEntry": tmnxChassisExtnEntry,
       "tmnxChassisUpdateGoldenBootstrapImage": tmnxChassisUpdateGoldenBootstrapImage,
       "tmnxChassisGoldenBootstrapImageSrc": tmnxChassisGoldenBootstrapImageSrc,
       "tmnxChassisValidateGoldenBootstrapImage": tmnxChassisValidateGoldenBootstrapImage,
       "tmnxChassisGoldenBootstrapImageVersion": tmnxChassisGoldenBootstrapImageVersion,
       "tmnxChassisRebootAutoInit": tmnxChassisRebootAutoInit,
       "tmnxChassisLowTempState": tmnxChassisLowTempState,
       "tmnxChassisSystemLEDState": tmnxChassisSystemLEDState,
       "tmnxHwExtnTable": tmnxHwExtnTable,
       "tmnxHwExtnEntry": tmnxHwExtnEntry,
       "tmnxHwLowTempThreshold": tmnxHwLowTempThreshold,
       "tmnxFabricPolicyTable": tmnxFabricPolicyTable,
       "tmnxFabricPolicyEntry": tmnxFabricPolicyEntry,
       "tmnxFabricPolicyIndex": tmnxFabricPolicyIndex,
       "tmnxFabricPolicyRowStatus": tmnxFabricPolicyRowStatus,
       "tmnxFabricPolicyCIR": tmnxFabricPolicyCIR,
       "tmnxFabricPolicyPIR": tmnxFabricPolicyPIR,
       "tmnxFabricPolicyCBS": tmnxFabricPolicyCBS,
       "tmnxFabricPolicyMBS": tmnxFabricPolicyMBS,
       "tmnxFabricPolicyMpointFabricPort": tmnxFabricPolicyMpointFabricPort,
       "tmnxChassisPowerSupplyExtnTable": tmnxChassisPowerSupplyExtnTable,
       "tmnxChassisPowerSupplyExtnEntry": tmnxChassisPowerSupplyExtnEntry,
       "tmnxChassisPowerSupplyAssignedDCType": tmnxChassisPowerSupplyAssignedDCType,
       "tmnxChassisFanExtnTable": tmnxChassisFanExtnTable,
       "tmnxChassisFanExtnEntry": tmnxChassisFanExtnEntry,
       "tmnxChassisFanCfgMode": tmnxChassisFanCfgMode,
       "tmnxChassisFanOperMode": tmnxChassisFanOperMode,
       "tmnxSASCardObjs": tmnxSASCardObjs,
       "tmnxCardExtnTable": tmnxCardExtnTable,
       "tmnxCardExtnEntry": tmnxCardExtnEntry,
       "tmnxCardSysResPlcyId": tmnxCardSysResPlcyId,
       "tmnxCpmCardExtnTable": tmnxCpmCardExtnTable,
       "tmnxCpmCardExtnEntry": tmnxCpmCardExtnEntry,
       "tmnxCpmCardBootImageSource": tmnxCpmCardBootImageSource,
       "aluExtTmnxChassisTable": aluExtTmnxChassisTable,
       "aluExtTmnxChassisEntry": aluExtTmnxChassisEntry,
       "aluExtPoePowerMode": aluExtPoePowerMode,
       "aluExtPoePowerSupplyStatus": aluExtPoePowerSupplyStatus,
       "aluExtPoeExternalPowerSupplyStatus": aluExtPoeExternalPowerSupplyStatus,
       "tCardResOperTable": tCardResOperTable,
       "tCardResOperEntry": tCardResOperEntry,
       "tCardResOperIngTcamSapAggMeter": tCardResOperIngTcamSapAggMeter,
       "tCardResOperIngTcamQosSapIng": tCardResOperIngTcamQosSapIng,
       "tCardResOperIngTcamQosSapIngIpv4": tCardResOperIngTcamQosSapIngIpv4,
       "tCardResOperIngTcamQosSapIngIpv4Ipv6": tCardResOperIngTcamQosSapIngIpv4Ipv6,
       "tCardResOperIngTcamQosSapIngMac": tCardResOperIngTcamQosSapIngMac,
       "tCardResOperIngTcamAclSapIng": tCardResOperIngTcamAclSapIng,
       "tCardResOperIngTcamAclSapIngIpv4": tCardResOperIngTcamAclSapIngIpv4,
       "tCardResOperIngTcamAclSapIng64Ipv6": tCardResOperIngTcamAclSapIng64Ipv6,
       "tCardResOperIngTcamAclSapIng128Ipv4Ipv6": tCardResOperIngTcamAclSapIng128Ipv4Ipv6,
       "tCardResOperIngTcamAclSapIngMac": tCardResOperIngTcamAclSapIngMac,
       "tCardResOperEgrTcamAclSapEgr": tCardResOperEgrTcamAclSapEgr,
       "tCardResOperEgrTcamAclSapEgrMacIpv4": tCardResOperEgrTcamAclSapEgrMacIpv4,
       "tCardResOperEgrTcamAclSapEgr128Ipv6": tCardResOperEgrTcamAclSapEgr128Ipv6,
       "tCardResOperEgrTcamAclSapEgr64MacIpv6": tCardResOperEgrTcamAclSapEgr64MacIpv6,
       "tCardResOperEgrTcamAclSapEgrMac": tCardResOperEgrTcamAclSapEgrMac,
       "tCardResOperIngTcamEthCfm": tCardResOperIngTcamEthCfm,
       "tCardResOperIngTcamEthCfmUpMep": tCardResOperIngTcamEthCfmUpMep,
       "tCardResOperG8032CtrlSapStartVlan": tCardResOperG8032CtrlSapStartVlan,
       "tCardResOperG8032CtrlSapEndVlan": tCardResOperG8032CtrlSapEndVlan,
       "tCardResOperResIpMacMatchEnable": tCardResOperResIpMacMatchEnable,
       "tCardResOperIngTcamEthCfmDownMep": tCardResOperIngTcamEthCfmDownMep,
       "tCardResOperIngTcamIpMulticast": tCardResOperIngTcamIpMulticast,
       "tmnxSASSecurityObjects": tmnxSASSecurityObjects,
       "tmnxSASSecurityNotificationObjs": tmnxSASSecurityNotificationObjs,
       "tmnxLoginUserName": tmnxLoginUserName,
       "tmnxLoginUserSrcIPAddress": tmnxLoginUserSrcIPAddress,
       "tmnxLoginMaxAttempts": tmnxLoginMaxAttempts,
       "tmnxChassisNotifyMDACfgFailReason": tmnxChassisNotifyMDACfgFailReason,
       "tmnxSASSysMIBNotifyPrefix": tmnxSASSysMIBNotifyPrefix,
       "tmnxSASSysNotifications": tmnxSASSysNotifications,
       "tmnxDyingGasp": tmnxDyingGasp,
       "tmnxSASSecurityNotifyPrefix": tmnxSASSecurityNotifyPrefix,
       "tmnxSASSecurityNotifications": tmnxSASSecurityNotifications,
       "tmnxUserLoginMaxAttempts": tmnxUserLoginMaxAttempts,
       "tmnxSSHUserLoginMaxAttempts": tmnxSSHUserLoginMaxAttempts}
)
