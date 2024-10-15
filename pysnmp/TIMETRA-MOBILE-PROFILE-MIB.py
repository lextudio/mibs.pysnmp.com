# SNMP MIB module (TIMETRA-MOBILE-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-MOBILE-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:03:19 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(TDSCPName,
 TDSCPValue,
 TFCName,
 TIpProtocol,
 TItemDescription,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxMobArpValue,
 TmnxMobArpValueOrZero,
 TmnxMobBufferLimit,
 TmnxMobChargingProfile,
 TmnxMobDiaPeerHost,
 TmnxMobDiaTransTimer,
 TmnxMobMcc,
 TmnxMobMccOrEmpty,
 TmnxMobMnc,
 TmnxMobMncOrEmpty,
 TmnxMobProfGbrRate,
 TmnxMobProfIpTtl,
 TmnxMobProfMbrRate,
 TmnxMobProfName,
 TmnxMobProfNameOrEmpty,
 TmnxMobProfPolChargingMethod,
 TmnxMobProfPolMeteringMethod,
 TmnxMobProfPolReportingLevel,
 TmnxMobQciValue,
 TmnxMobQciValueOrZero,
 TmnxMobQueueLimit,
 TmnxMobStaticPolPrecedenceOrZero,
 TmnxTimeInSec,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDSCPName",
    "TDSCPValue",
    "TFCName",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxMobArpValue",
    "TmnxMobArpValueOrZero",
    "TmnxMobBufferLimit",
    "TmnxMobChargingProfile",
    "TmnxMobDiaPeerHost",
    "TmnxMobDiaTransTimer",
    "TmnxMobMcc",
    "TmnxMobMccOrEmpty",
    "TmnxMobMnc",
    "TmnxMobMncOrEmpty",
    "TmnxMobProfGbrRate",
    "TmnxMobProfIpTtl",
    "TmnxMobProfMbrRate",
    "TmnxMobProfName",
    "TmnxMobProfNameOrEmpty",
    "TmnxMobProfPolChargingMethod",
    "TmnxMobProfPolMeteringMethod",
    "TmnxMobProfPolReportingLevel",
    "TmnxMobQciValue",
    "TmnxMobQciValueOrZero",
    "TmnxMobQueueLimit",
    "TmnxMobStaticPolPrecedenceOrZero",
    "TmnxTimeInSec",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraMobProfileMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 67)
)
timetraMobProfileMIBModule.setRevisions(
        ("1909-12-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMobProfThreshold(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TmnxMobProfMsgReTxTimeout(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )



class TmnxMobProfMsgReTxRetryCount(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TmnxMobProfKeepAliveTimeout(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 180),
    )



class TmnxMobProfKeepAliveRetryCount(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class TmnxMobProfKeepAliveResponse(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class TmnxMobProfKeepAliveInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 180),
    )



class TmnxMobProfAllowDiscard(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("discard", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMobProfileConformance_ObjectIdentity = ObjectIdentity
tmnxMobProfileConformance = _TmnxMobProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67)
)
_TmnxMobProfileCompliances_ObjectIdentity = ObjectIdentity
tmnxMobProfileCompliances = _TmnxMobProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 1)
)
_TmnxMobProfileGroups_ObjectIdentity = ObjectIdentity
tmnxMobProfileGroups = _TmnxMobProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2)
)
_TmnxMobProfile_ObjectIdentity = ObjectIdentity
tmnxMobProfile = _TmnxMobProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67)
)
_TmnxMobProfileObjs_ObjectIdentity = ObjectIdentity
tmnxMobProfileObjs = _TmnxMobProfileObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1)
)
_TmnxMobProfSysTable_Object = MibTable
tmnxMobProfSysTable = _TmnxMobProfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMobProfSysTable.setStatus("current")
_TmnxMobProfSysEntry_Object = MibTableRow
tmnxMobProfSysEntry = _TmnxMobProfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1)
)
tmnxMobProfSysEntry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfSysEntry.setStatus("current")
_TmnxMobProfSysName_Type = TmnxMobProfName
_TmnxMobProfSysName_Object = MibTableColumn
tmnxMobProfSysName = _TmnxMobProfSysName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 1),
    _TmnxMobProfSysName_Type()
)
tmnxMobProfSysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfSysName.setStatus("current")
_TmnxMobProfSysRowStatus_Type = RowStatus
_TmnxMobProfSysRowStatus_Object = MibTableColumn
tmnxMobProfSysRowStatus = _TmnxMobProfSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 2),
    _TmnxMobProfSysRowStatus_Type()
)
tmnxMobProfSysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysRowStatus.setStatus("current")
_TmnxMobProfSysLastChanged_Type = TimeStamp
_TmnxMobProfSysLastChanged_Object = MibTableColumn
tmnxMobProfSysLastChanged = _TmnxMobProfSysLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 3),
    _TmnxMobProfSysLastChanged_Type()
)
tmnxMobProfSysLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfSysLastChanged.setStatus("current")


class _TmnxMobProfSysDescription_Type(TItemDescription):
    """Custom type tmnxMobProfSysDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfSysDescription_Object = MibTableColumn
tmnxMobProfSysDescription = _TmnxMobProfSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 4),
    _TmnxMobProfSysDescription_Type()
)
tmnxMobProfSysDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysDescription.setStatus("current")


class _TmnxMobProfSysBCLimit_Type(Unsigned32):
    """Custom type tmnxMobProfSysBCLimit based on Unsigned32"""
    defaultValue = 250000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 250000),
    )


_TmnxMobProfSysBCLimit_Type.__name__ = "Unsigned32"
_TmnxMobProfSysBCLimit_Object = MibTableColumn
tmnxMobProfSysBCLimit = _TmnxMobProfSysBCLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 5),
    _TmnxMobProfSysBCLimit_Type()
)
tmnxMobProfSysBCLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysBCLimit.setStatus("current")


class _TmnxMobProfSysBCActivtyRate_Type(Unsigned32):
    """Custom type tmnxMobProfSysBCActivtyRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_TmnxMobProfSysBCActivtyRate_Type.__name__ = "Unsigned32"
_TmnxMobProfSysBCActivtyRate_Object = MibTableColumn
tmnxMobProfSysBCActivtyRate = _TmnxMobProfSysBCActivtyRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 6),
    _TmnxMobProfSysBCActivtyRate_Type()
)
tmnxMobProfSysBCActivtyRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysBCActivtyRate.setStatus("current")


class _TmnxMobProfSysBCPdnLimit_Type(Unsigned32):
    """Custom type tmnxMobProfSysBCPdnLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_TmnxMobProfSysBCPdnLimit_Type.__name__ = "Unsigned32"
_TmnxMobProfSysBCPdnLimit_Object = MibTableColumn
tmnxMobProfSysBCPdnLimit = _TmnxMobProfSysBCPdnLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 7),
    _TmnxMobProfSysBCPdnLimit_Type()
)
tmnxMobProfSysBCPdnLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysBCPdnLimit.setStatus("current")


class _TmnxMobProfSysBCUeLimit_Type(Unsigned32):
    """Custom type tmnxMobProfSysBCUeLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_TmnxMobProfSysBCUeLimit_Type.__name__ = "Unsigned32"
_TmnxMobProfSysBCUeLimit_Object = MibTableColumn
tmnxMobProfSysBCUeLimit = _TmnxMobProfSysBCUeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 8),
    _TmnxMobProfSysBCUeLimit_Type()
)
tmnxMobProfSysBCUeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysBCUeLimit.setStatus("current")


class _TmnxMobProfSysSDFIpv4Limit_Type(Unsigned32):
    """Custom type tmnxMobProfSysSDFIpv4Limit based on Unsigned32"""
    defaultValue = 390000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500000),
    )


_TmnxMobProfSysSDFIpv4Limit_Type.__name__ = "Unsigned32"
_TmnxMobProfSysSDFIpv4Limit_Object = MibTableColumn
tmnxMobProfSysSDFIpv4Limit = _TmnxMobProfSysSDFIpv4Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 9),
    _TmnxMobProfSysSDFIpv4Limit_Type()
)
tmnxMobProfSysSDFIpv4Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSDFIpv4Limit.setStatus("current")


class _TmnxMobProfSysSDFIpv6Limit_Type(Unsigned32):
    """Custom type tmnxMobProfSysSDFIpv6Limit based on Unsigned32"""
    defaultValue = 190000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512000),
    )


_TmnxMobProfSysSDFIpv6Limit_Type.__name__ = "Unsigned32"
_TmnxMobProfSysSDFIpv6Limit_Object = MibTableColumn
tmnxMobProfSysSDFIpv6Limit = _TmnxMobProfSysSDFIpv6Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 10),
    _TmnxMobProfSysSDFIpv6Limit_Type()
)
tmnxMobProfSysSDFIpv6Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSDFIpv6Limit.setStatus("current")


class _TmnxMobProfSysCpuThreshldCriticl_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysCpuThreshldCriticl based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysCpuThreshldCriticl_Object = MibTableColumn
tmnxMobProfSysCpuThreshldCriticl = _TmnxMobProfSysCpuThreshldCriticl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 11),
    _TmnxMobProfSysCpuThreshldCriticl_Type()
)
tmnxMobProfSysCpuThreshldCriticl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldCriticl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldCriticl.setUnits("percentage")


class _TmnxMobProfSysCpuThreshldMajor_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysCpuThreshldMajor based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysCpuThreshldMajor_Object = MibTableColumn
tmnxMobProfSysCpuThreshldMajor = _TmnxMobProfSysCpuThreshldMajor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 12),
    _TmnxMobProfSysCpuThreshldMajor_Type()
)
tmnxMobProfSysCpuThreshldMajor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldMajor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldMajor.setUnits("percentage")


class _TmnxMobProfSysCpuThreshldMinor_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysCpuThreshldMinor based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysCpuThreshldMinor_Object = MibTableColumn
tmnxMobProfSysCpuThreshldMinor = _TmnxMobProfSysCpuThreshldMinor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 13),
    _TmnxMobProfSysCpuThreshldMinor_Type()
)
tmnxMobProfSysCpuThreshldMinor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldMinor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysCpuThreshldMinor.setUnits("percentage")


class _TmnxMobProfSysMemThreshldCriticl_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysMemThreshldCriticl based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysMemThreshldCriticl_Object = MibTableColumn
tmnxMobProfSysMemThreshldCriticl = _TmnxMobProfSysMemThreshldCriticl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 14),
    _TmnxMobProfSysMemThreshldCriticl_Type()
)
tmnxMobProfSysMemThreshldCriticl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldCriticl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldCriticl.setUnits("percentage")


class _TmnxMobProfSysMemThreshldMajor_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysMemThreshldMajor based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysMemThreshldMajor_Object = MibTableColumn
tmnxMobProfSysMemThreshldMajor = _TmnxMobProfSysMemThreshldMajor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 15),
    _TmnxMobProfSysMemThreshldMajor_Type()
)
tmnxMobProfSysMemThreshldMajor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldMajor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldMajor.setUnits("percentage")


class _TmnxMobProfSysMemThreshldMinor_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysMemThreshldMinor based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysMemThreshldMinor_Object = MibTableColumn
tmnxMobProfSysMemThreshldMinor = _TmnxMobProfSysMemThreshldMinor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 16),
    _TmnxMobProfSysMemThreshldMinor_Type()
)
tmnxMobProfSysMemThreshldMinor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldMinor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysMemThreshldMinor.setUnits("percentage")


class _TmnxMobProfSysSgnlFailThrshldS5_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysSgnlFailThrshldS5 based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysSgnlFailThrshldS5_Object = MibTableColumn
tmnxMobProfSysSgnlFailThrshldS5 = _TmnxMobProfSysSgnlFailThrshldS5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 17),
    _TmnxMobProfSysSgnlFailThrshldS5_Type()
)
tmnxMobProfSysSgnlFailThrshldS5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS5.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS5.setUnits("percentage")


class _TmnxMobProfSysSgnlFailThrshldS8_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysSgnlFailThrshldS8 based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysSgnlFailThrshldS8_Object = MibTableColumn
tmnxMobProfSysSgnlFailThrshldS8 = _TmnxMobProfSysSgnlFailThrshldS8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 18),
    _TmnxMobProfSysSgnlFailThrshldS8_Type()
)
tmnxMobProfSysSgnlFailThrshldS8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS8.setUnits("percentage")


class _TmnxMobProfSysSgnlFailThrshldS11_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysSgnlFailThrshldS11 based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysSgnlFailThrshldS11_Object = MibTableColumn
tmnxMobProfSysSgnlFailThrshldS11 = _TmnxMobProfSysSgnlFailThrshldS11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 19),
    _TmnxMobProfSysSgnlFailThrshldS11_Type()
)
tmnxMobProfSysSgnlFailThrshldS11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS11.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldS11.setUnits("percentage")


class _TmnxMobProfSysSgnlFailThrshldGxc_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysSgnlFailThrshldGxc based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysSgnlFailThrshldGxc_Object = MibTableColumn
tmnxMobProfSysSgnlFailThrshldGxc = _TmnxMobProfSysSgnlFailThrshldGxc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 20),
    _TmnxMobProfSysSgnlFailThrshldGxc_Type()
)
tmnxMobProfSysSgnlFailThrshldGxc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldGxc.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysSgnlFailThrshldGxc.setUnits("percentage")


class _TmnxMobProfSysTrfcDropThrshldS1u_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysTrfcDropThrshldS1u based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysTrfcDropThrshldS1u_Object = MibTableColumn
tmnxMobProfSysTrfcDropThrshldS1u = _TmnxMobProfSysTrfcDropThrshldS1u_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 21),
    _TmnxMobProfSysTrfcDropThrshldS1u_Type()
)
tmnxMobProfSysTrfcDropThrshldS1u.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS1u.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS1u.setUnits("percentage")


class _TmnxMobProfSysTrfcDropThrshldS5_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysTrfcDropThrshldS5 based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysTrfcDropThrshldS5_Object = MibTableColumn
tmnxMobProfSysTrfcDropThrshldS5 = _TmnxMobProfSysTrfcDropThrshldS5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 22),
    _TmnxMobProfSysTrfcDropThrshldS5_Type()
)
tmnxMobProfSysTrfcDropThrshldS5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS5.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS5.setUnits("percentage")


class _TmnxMobProfSysTrfcDropThrshldS8_Type(TmnxMobProfThreshold):
    """Custom type tmnxMobProfSysTrfcDropThrshldS8 based on TmnxMobProfThreshold"""
    defaultValue = 50


_TmnxMobProfSysTrfcDropThrshldS8_Object = MibTableColumn
tmnxMobProfSysTrfcDropThrshldS8 = _TmnxMobProfSysTrfcDropThrshldS8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 23),
    _TmnxMobProfSysTrfcDropThrshldS8_Type()
)
tmnxMobProfSysTrfcDropThrshldS8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysTrfcDropThrshldS8.setUnits("percentage")


class _TmnxMobProfSysPagingBufferLimit_Type(TmnxMobBufferLimit):
    """Custom type tmnxMobProfSysPagingBufferLimit based on TmnxMobBufferLimit"""
    defaultValue = 8000


_TmnxMobProfSysPagingBufferLimit_Object = MibTableColumn
tmnxMobProfSysPagingBufferLimit = _TmnxMobProfSysPagingBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 24),
    _TmnxMobProfSysPagingBufferLimit_Type()
)
tmnxMobProfSysPagingBufferLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysPagingBufferLimit.setStatus("current")


class _TmnxMobProfSysPagingBufferSize_Type(TmnxMobQueueLimit):
    """Custom type tmnxMobProfSysPagingBufferSize based on TmnxMobQueueLimit"""
    defaultValue = 8000


_TmnxMobProfSysPagingBufferSize_Object = MibTableColumn
tmnxMobProfSysPagingBufferSize = _TmnxMobProfSysPagingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 25),
    _TmnxMobProfSysPagingBufferSize_Type()
)
tmnxMobProfSysPagingBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysPagingBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysPagingBufferSize.setUnits("bytes")


class _TmnxMobProfSysPagingTimeout_Type(Unsigned32):
    """Custom type tmnxMobProfSysPagingTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxMobProfSysPagingTimeout_Type.__name__ = "Unsigned32"
_TmnxMobProfSysPagingTimeout_Object = MibTableColumn
tmnxMobProfSysPagingTimeout = _TmnxMobProfSysPagingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 26),
    _TmnxMobProfSysPagingTimeout_Type()
)
tmnxMobProfSysPagingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysPagingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysPagingTimeout.setUnits("seconds")


class _TmnxMobProfSysS1BufferLimit_Type(TmnxMobBufferLimit):
    """Custom type tmnxMobProfSysS1BufferLimit based on TmnxMobBufferLimit"""
    defaultValue = 8000


_TmnxMobProfSysS1BufferLimit_Object = MibTableColumn
tmnxMobProfSysS1BufferLimit = _TmnxMobProfSysS1BufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 27),
    _TmnxMobProfSysS1BufferLimit_Type()
)
tmnxMobProfSysS1BufferLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysS1BufferLimit.setStatus("current")


class _TmnxMobProfSysS1BufferSize_Type(TmnxMobQueueLimit):
    """Custom type tmnxMobProfSysS1BufferSize based on TmnxMobQueueLimit"""
    defaultValue = 8000


_TmnxMobProfSysS1BufferSize_Object = MibTableColumn
tmnxMobProfSysS1BufferSize = _TmnxMobProfSysS1BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 1, 1, 28),
    _TmnxMobProfSysS1BufferSize_Type()
)
tmnxMobProfSysS1BufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSysS1BufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSysS1BufferSize.setUnits("bytes")
_TmnxMobProfDiaTable_Object = MibTable
tmnxMobProfDiaTable = _TmnxMobProfDiaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaTable.setStatus("current")
_TmnxMobProfDiaEntry_Object = MibTableRow
tmnxMobProfDiaEntry = _TmnxMobProfDiaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1)
)
tmnxMobProfDiaEntry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaEntry.setStatus("current")
_TmnxMobProfDiaName_Type = TmnxMobProfName
_TmnxMobProfDiaName_Object = MibTableColumn
tmnxMobProfDiaName = _TmnxMobProfDiaName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 1),
    _TmnxMobProfDiaName_Type()
)
tmnxMobProfDiaName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfDiaName.setStatus("current")
_TmnxMobProfDiaRowStatus_Type = RowStatus
_TmnxMobProfDiaRowStatus_Object = MibTableColumn
tmnxMobProfDiaRowStatus = _TmnxMobProfDiaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 2),
    _TmnxMobProfDiaRowStatus_Type()
)
tmnxMobProfDiaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaRowStatus.setStatus("current")
_TmnxMobProfDiaLastChanged_Type = TimeStamp
_TmnxMobProfDiaLastChanged_Object = MibTableColumn
tmnxMobProfDiaLastChanged = _TmnxMobProfDiaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 3),
    _TmnxMobProfDiaLastChanged_Type()
)
tmnxMobProfDiaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaLastChanged.setStatus("current")


class _TmnxMobProfDiaDescription_Type(TItemDescription):
    """Custom type tmnxMobProfDiaDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfDiaDescription_Object = MibTableColumn
tmnxMobProfDiaDescription = _TmnxMobProfDiaDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 4),
    _TmnxMobProfDiaDescription_Type()
)
tmnxMobProfDiaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaDescription.setStatus("current")


class _TmnxMobProfDiaWatchdgTimer_Type(Unsigned32):
    """Custom type tmnxMobProfDiaWatchdgTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TmnxMobProfDiaWatchdgTimer_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaWatchdgTimer_Object = MibTableColumn
tmnxMobProfDiaWatchdgTimer = _TmnxMobProfDiaWatchdgTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 5),
    _TmnxMobProfDiaWatchdgTimer_Type()
)
tmnxMobProfDiaWatchdgTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaWatchdgTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaWatchdgTimer.setUnits("seconds")


class _TmnxMobProfDiaConnTimer_Type(Unsigned32):
    """Custom type tmnxMobProfDiaConnTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_TmnxMobProfDiaConnTimer_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaConnTimer_Object = MibTableColumn
tmnxMobProfDiaConnTimer = _TmnxMobProfDiaConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 6),
    _TmnxMobProfDiaConnTimer_Type()
)
tmnxMobProfDiaConnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaConnTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaConnTimer.setUnits("seconds")


class _TmnxMobProfDiaTransTimer_Type(TmnxMobDiaTransTimer):
    """Custom type tmnxMobProfDiaTransTimer based on TmnxMobDiaTransTimer"""
    defaultValue = 5


_TmnxMobProfDiaTransTimer_Object = MibTableColumn
tmnxMobProfDiaTransTimer = _TmnxMobProfDiaTransTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 7),
    _TmnxMobProfDiaTransTimer_Type()
)
tmnxMobProfDiaTransTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaTransTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaTransTimer.setUnits("seconds")


class _TmnxMobProfDiaIpTtl_Type(TmnxMobProfIpTtl):
    """Custom type tmnxMobProfDiaIpTtl based on TmnxMobProfIpTtl"""
    defaultValue = 255


_TmnxMobProfDiaIpTtl_Object = MibTableColumn
tmnxMobProfDiaIpTtl = _TmnxMobProfDiaIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 8),
    _TmnxMobProfDiaIpTtl_Type()
)
tmnxMobProfDiaIpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaIpTtl.setStatus("current")


class _TmnxMobProfDiaIpDscp_Type(TDSCPValue):
    """Custom type tmnxMobProfDiaIpDscp based on TDSCPValue"""
    defaultValue = 56


_TmnxMobProfDiaIpDscp_Object = MibTableColumn
tmnxMobProfDiaIpDscp = _TmnxMobProfDiaIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 9),
    _TmnxMobProfDiaIpDscp_Type()
)
tmnxMobProfDiaIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaIpDscp.setStatus("current")


class _TmnxMobProfDiaDprTimeout_Type(Unsigned32):
    """Custom type tmnxMobProfDiaDprTimeout based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxMobProfDiaDprTimeout_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaDprTimeout_Object = MibTableColumn
tmnxMobProfDiaDprTimeout = _TmnxMobProfDiaDprTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 10),
    _TmnxMobProfDiaDprTimeout_Type()
)
tmnxMobProfDiaDprTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaDprTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaDprTimeout.setUnits("seconds")


class _TmnxMobProfDiaPermFailRetryTime_Type(Unsigned32):
    """Custom type tmnxMobProfDiaPermFailRetryTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TmnxMobProfDiaPermFailRetryTime_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaPermFailRetryTime_Object = MibTableColumn
tmnxMobProfDiaPermFailRetryTime = _TmnxMobProfDiaPermFailRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 11),
    _TmnxMobProfDiaPermFailRetryTime_Type()
)
tmnxMobProfDiaPermFailRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPermFailRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPermFailRetryTime.setUnits("minutes")


class _TmnxMobProfDiaDnsRefreshInt_Type(Unsigned32):
    """Custom type tmnxMobProfDiaDnsRefreshInt based on Unsigned32"""
    defaultValue = 21600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxMobProfDiaDnsRefreshInt_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaDnsRefreshInt_Object = MibTableColumn
tmnxMobProfDiaDnsRefreshInt = _TmnxMobProfDiaDnsRefreshInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 2, 1, 12),
    _TmnxMobProfDiaDnsRefreshInt_Type()
)
tmnxMobProfDiaDnsRefreshInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaDnsRefreshInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDiaDnsRefreshInt.setUnits("seconds")
_TmnxMobProfDiaPeerTable_Object = MibTable
tmnxMobProfDiaPeerTable = _TmnxMobProfDiaPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerTable.setStatus("current")
_TmnxMobProfDiaPeerEntry_Object = MibTableRow
tmnxMobProfDiaPeerEntry = _TmnxMobProfDiaPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1)
)
tmnxMobProfDiaPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerEntry.setStatus("current")
_TmnxMobProfDiaPeerName_Type = TmnxMobProfName
_TmnxMobProfDiaPeerName_Object = MibTableColumn
tmnxMobProfDiaPeerName = _TmnxMobProfDiaPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 1),
    _TmnxMobProfDiaPeerName_Type()
)
tmnxMobProfDiaPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerName.setStatus("current")
_TmnxMobProfDiaPeerRowStatus_Type = RowStatus
_TmnxMobProfDiaPeerRowStatus_Object = MibTableColumn
tmnxMobProfDiaPeerRowStatus = _TmnxMobProfDiaPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 2),
    _TmnxMobProfDiaPeerRowStatus_Type()
)
tmnxMobProfDiaPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerRowStatus.setStatus("current")
_TmnxMobProfDiaPeerLastChanged_Type = TimeStamp
_TmnxMobProfDiaPeerLastChanged_Object = MibTableColumn
tmnxMobProfDiaPeerLastChanged = _TmnxMobProfDiaPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 3),
    _TmnxMobProfDiaPeerLastChanged_Type()
)
tmnxMobProfDiaPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerLastChanged.setStatus("current")


class _TmnxMobProfDiaPeerDescription_Type(TItemDescription):
    """Custom type tmnxMobProfDiaPeerDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfDiaPeerDescription_Object = MibTableColumn
tmnxMobProfDiaPeerDescription = _TmnxMobProfDiaPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 4),
    _TmnxMobProfDiaPeerDescription_Type()
)
tmnxMobProfDiaPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerDescription.setStatus("current")


class _TmnxMobProfDiaPeerDiaProfName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfDiaPeerDiaProfName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfDiaPeerDiaProfName_Object = MibTableColumn
tmnxMobProfDiaPeerDiaProfName = _TmnxMobProfDiaPeerDiaProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 5),
    _TmnxMobProfDiaPeerDiaProfName_Type()
)
tmnxMobProfDiaPeerDiaProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerDiaProfName.setStatus("current")


class _TmnxMobProfDiaPeerDestRealm_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobProfDiaPeerDestRealm based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobProfDiaPeerDestRealm_Object = MibTableColumn
tmnxMobProfDiaPeerDestRealm = _TmnxMobProfDiaPeerDestRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 6),
    _TmnxMobProfDiaPeerDestRealm_Type()
)
tmnxMobProfDiaPeerDestRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerDestRealm.setStatus("current")


class _TmnxMobProfDiaPeerTransport_Type(Integer32):
    """Custom type tmnxMobProfDiaPeerTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sctp", 2),
          ("tcp", 1))
    )


_TmnxMobProfDiaPeerTransport_Type.__name__ = "Integer32"
_TmnxMobProfDiaPeerTransport_Object = MibTableColumn
tmnxMobProfDiaPeerTransport = _TmnxMobProfDiaPeerTransport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 7),
    _TmnxMobProfDiaPeerTransport_Type()
)
tmnxMobProfDiaPeerTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerTransport.setStatus("current")


class _TmnxMobProfDiaPeerLoadBalance_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfDiaPeerLoadBalance based on TmnxEnabledDisabled"""


_TmnxMobProfDiaPeerLoadBalance_Object = MibTableColumn
tmnxMobProfDiaPeerLoadBalance = _TmnxMobProfDiaPeerLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 8),
    _TmnxMobProfDiaPeerLoadBalance_Type()
)
tmnxMobProfDiaPeerLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerLoadBalance.setStatus("current")


class _TmnxMobProfDiaPeerIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobProfDiaPeerIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobProfDiaPeerIfVRtrId_Object = MibTableColumn
tmnxMobProfDiaPeerIfVRtrId = _TmnxMobProfDiaPeerIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 9),
    _TmnxMobProfDiaPeerIfVRtrId_Type()
)
tmnxMobProfDiaPeerIfVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerIfVRtrId.setStatus("current")


class _TmnxMobProfDiaPeerIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobProfDiaPeerIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobProfDiaPeerIfIndex_Object = MibTableColumn
tmnxMobProfDiaPeerIfIndex = _TmnxMobProfDiaPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 10),
    _TmnxMobProfDiaPeerIfIndex_Type()
)
tmnxMobProfDiaPeerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerIfIndex.setStatus("current")


class _TmnxMobProfDiaPeerApplication_Type(Integer32):
    """Custom type tmnxMobProfDiaPeerApplication based on Integer32"""
    defaultValue = 0

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
        *(("gx", 1),
          ("gxc", 2),
          ("gy", 4),
          ("none", 0),
          ("rf", 3),
          ("s6b", 5))
    )


_TmnxMobProfDiaPeerApplication_Type.__name__ = "Integer32"
_TmnxMobProfDiaPeerApplication_Object = MibTableColumn
tmnxMobProfDiaPeerApplication = _TmnxMobProfDiaPeerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 3, 1, 11),
    _TmnxMobProfDiaPeerApplication_Type()
)
tmnxMobProfDiaPeerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerApplication.setStatus("current")
_TmnxMobProfDiaPeerListTable_Object = MibTable
tmnxMobProfDiaPeerListTable = _TmnxMobProfDiaPeerListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListTable.setStatus("current")
_TmnxMobProfDiaPeerListEntry_Object = MibTableRow
tmnxMobProfDiaPeerListEntry = _TmnxMobProfDiaPeerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1)
)
tmnxMobProfDiaPeerListEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
)
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListEntry.setStatus("current")


class _TmnxMobProfDiaPeerListIndex_Type(Unsigned32):
    """Custom type tmnxMobProfDiaPeerListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_TmnxMobProfDiaPeerListIndex_Type.__name__ = "Unsigned32"
_TmnxMobProfDiaPeerListIndex_Object = MibTableColumn
tmnxMobProfDiaPeerListIndex = _TmnxMobProfDiaPeerListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 1),
    _TmnxMobProfDiaPeerListIndex_Type()
)
tmnxMobProfDiaPeerListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListIndex.setStatus("current")
_TmnxMobProfDiaPeerListRowStatus_Type = RowStatus
_TmnxMobProfDiaPeerListRowStatus_Object = MibTableColumn
tmnxMobProfDiaPeerListRowStatus = _TmnxMobProfDiaPeerListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 2),
    _TmnxMobProfDiaPeerListRowStatus_Type()
)
tmnxMobProfDiaPeerListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListRowStatus.setStatus("current")
_TmnxMobProfDiaPeerListLastChngd_Type = TimeStamp
_TmnxMobProfDiaPeerListLastChngd_Object = MibTableColumn
tmnxMobProfDiaPeerListLastChngd = _TmnxMobProfDiaPeerListLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 3),
    _TmnxMobProfDiaPeerListLastChngd_Type()
)
tmnxMobProfDiaPeerListLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListLastChngd.setStatus("current")
_TmnxMobProfDiaPeerListAddrType_Type = InetAddressType
_TmnxMobProfDiaPeerListAddrType_Object = MibTableColumn
tmnxMobProfDiaPeerListAddrType = _TmnxMobProfDiaPeerListAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 4),
    _TmnxMobProfDiaPeerListAddrType_Type()
)
tmnxMobProfDiaPeerListAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListAddrType.setStatus("current")


class _TmnxMobProfDiaPeerListAddr_Type(InetAddress):
    """Custom type tmnxMobProfDiaPeerListAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobProfDiaPeerListAddr_Type.__name__ = "InetAddress"
_TmnxMobProfDiaPeerListAddr_Object = MibTableColumn
tmnxMobProfDiaPeerListAddr = _TmnxMobProfDiaPeerListAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 5),
    _TmnxMobProfDiaPeerListAddr_Type()
)
tmnxMobProfDiaPeerListAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListAddr.setStatus("current")


class _TmnxMobProfDiaPeerListPort_Type(InetPortNumber):
    """Custom type tmnxMobProfDiaPeerListPort based on InetPortNumber"""
    defaultValue = 3868

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3868, 3888),
    )


_TmnxMobProfDiaPeerListPort_Type.__name__ = "InetPortNumber"
_TmnxMobProfDiaPeerListPort_Object = MibTableColumn
tmnxMobProfDiaPeerListPort = _TmnxMobProfDiaPeerListPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 6),
    _TmnxMobProfDiaPeerListPort_Type()
)
tmnxMobProfDiaPeerListPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListPort.setStatus("current")


class _TmnxMobProfDiaPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobProfDiaPeerAdminState based on TmnxAdminState"""


_TmnxMobProfDiaPeerAdminState_Object = MibTableColumn
tmnxMobProfDiaPeerAdminState = _TmnxMobProfDiaPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 4, 1, 7),
    _TmnxMobProfDiaPeerAdminState_Type()
)
tmnxMobProfDiaPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerAdminState.setStatus("current")
_TmnxMobProfPmipv6Table_Object = MibTable
tmnxMobProfPmipv6Table = _TmnxMobProfPmipv6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6Table.setStatus("current")
_TmnxMobProfPmipv6Entry_Object = MibTableRow
tmnxMobProfPmipv6Entry = _TmnxMobProfPmipv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1)
)
tmnxMobProfPmipv6Entry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6Name"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6Entry.setStatus("current")
_TmnxMobProfPmipv6Name_Type = TmnxMobProfName
_TmnxMobProfPmipv6Name_Object = MibTableColumn
tmnxMobProfPmipv6Name = _TmnxMobProfPmipv6Name_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 1),
    _TmnxMobProfPmipv6Name_Type()
)
tmnxMobProfPmipv6Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6Name.setStatus("current")
_TmnxMobProfPmipv6RowStatus_Type = RowStatus
_TmnxMobProfPmipv6RowStatus_Object = MibTableColumn
tmnxMobProfPmipv6RowStatus = _TmnxMobProfPmipv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 2),
    _TmnxMobProfPmipv6RowStatus_Type()
)
tmnxMobProfPmipv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6RowStatus.setStatus("current")
_TmnxMobProfPmipv6LastChanged_Type = TimeStamp
_TmnxMobProfPmipv6LastChanged_Object = MibTableColumn
tmnxMobProfPmipv6LastChanged = _TmnxMobProfPmipv6LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 3),
    _TmnxMobProfPmipv6LastChanged_Type()
)
tmnxMobProfPmipv6LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6LastChanged.setStatus("current")


class _TmnxMobProfPmipv6Description_Type(TItemDescription):
    """Custom type tmnxMobProfPmipv6Description based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfPmipv6Description_Object = MibTableColumn
tmnxMobProfPmipv6Description = _TmnxMobProfPmipv6Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 4),
    _TmnxMobProfPmipv6Description_Type()
)
tmnxMobProfPmipv6Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6Description.setStatus("current")


class _TmnxMobProfPmipv6MsgReTxTimeout_Type(TmnxMobProfMsgReTxTimeout):
    """Custom type tmnxMobProfPmipv6MsgReTxTimeout based on TmnxMobProfMsgReTxTimeout"""
    defaultValue = 5


_TmnxMobProfPmipv6MsgReTxTimeout_Object = MibTableColumn
tmnxMobProfPmipv6MsgReTxTimeout = _TmnxMobProfPmipv6MsgReTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 5),
    _TmnxMobProfPmipv6MsgReTxTimeout_Type()
)
tmnxMobProfPmipv6MsgReTxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6MsgReTxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6MsgReTxTimeout.setUnits("seconds")


class _TmnxMobProfPmipv6MsgReTxRetryCnt_Type(TmnxMobProfMsgReTxRetryCount):
    """Custom type tmnxMobProfPmipv6MsgReTxRetryCnt based on TmnxMobProfMsgReTxRetryCount"""
    defaultValue = 3


_TmnxMobProfPmipv6MsgReTxRetryCnt_Object = MibTableColumn
tmnxMobProfPmipv6MsgReTxRetryCnt = _TmnxMobProfPmipv6MsgReTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 6),
    _TmnxMobProfPmipv6MsgReTxRetryCnt_Type()
)
tmnxMobProfPmipv6MsgReTxRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6MsgReTxRetryCnt.setStatus("current")


class _TmnxMobProfPmipv6KeepAlvTimeout_Type(TmnxMobProfKeepAliveResponse):
    """Custom type tmnxMobProfPmipv6KeepAlvTimeout based on TmnxMobProfKeepAliveResponse"""
    defaultValue = 5


_TmnxMobProfPmipv6KeepAlvTimeout_Object = MibTableColumn
tmnxMobProfPmipv6KeepAlvTimeout = _TmnxMobProfPmipv6KeepAlvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 7),
    _TmnxMobProfPmipv6KeepAlvTimeout_Type()
)
tmnxMobProfPmipv6KeepAlvTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6KeepAlvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6KeepAlvTimeout.setUnits("seconds")


class _TmnxMobProfPmipv6KeepAlvRetryCnt_Type(TmnxMobProfKeepAliveRetryCount):
    """Custom type tmnxMobProfPmipv6KeepAlvRetryCnt based on TmnxMobProfKeepAliveRetryCount"""
    defaultValue = 4


_TmnxMobProfPmipv6KeepAlvRetryCnt_Object = MibTableColumn
tmnxMobProfPmipv6KeepAlvRetryCnt = _TmnxMobProfPmipv6KeepAlvRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 8),
    _TmnxMobProfPmipv6KeepAlvRetryCnt_Type()
)
tmnxMobProfPmipv6KeepAlvRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6KeepAlvRetryCnt.setStatus("current")


class _TmnxMobProfPmipv6KeepAlvIntvl_Type(TmnxMobProfKeepAliveInterval):
    """Custom type tmnxMobProfPmipv6KeepAlvIntvl based on TmnxMobProfKeepAliveInterval"""
    defaultValue = 60


_TmnxMobProfPmipv6KeepAlvIntvl_Object = MibTableColumn
tmnxMobProfPmipv6KeepAlvIntvl = _TmnxMobProfPmipv6KeepAlvIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 9),
    _TmnxMobProfPmipv6KeepAlvIntvl_Type()
)
tmnxMobProfPmipv6KeepAlvIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6KeepAlvIntvl.setStatus("current")


class _TmnxMobProfPmipv6IpTtl_Type(TmnxMobProfIpTtl):
    """Custom type tmnxMobProfPmipv6IpTtl based on TmnxMobProfIpTtl"""
    defaultValue = 255


_TmnxMobProfPmipv6IpTtl_Object = MibTableColumn
tmnxMobProfPmipv6IpTtl = _TmnxMobProfPmipv6IpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 10),
    _TmnxMobProfPmipv6IpTtl_Type()
)
tmnxMobProfPmipv6IpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6IpTtl.setStatus("current")


class _TmnxMobProfPmipv6IpDscp_Type(TDSCPValue):
    """Custom type tmnxMobProfPmipv6IpDscp based on TDSCPValue"""
    defaultValue = 56


_TmnxMobProfPmipv6IpDscp_Object = MibTableColumn
tmnxMobProfPmipv6IpDscp = _TmnxMobProfPmipv6IpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 5, 1, 11),
    _TmnxMobProfPmipv6IpDscp_Type()
)
tmnxMobProfPmipv6IpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6IpDscp.setStatus("current")
_TmnxMobProfGtpTable_Object = MibTable
tmnxMobProfGtpTable = _TmnxMobProfGtpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxMobProfGtpTable.setStatus("current")
_TmnxMobProfGtpEntry_Object = MibTableRow
tmnxMobProfGtpEntry = _TmnxMobProfGtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1)
)
tmnxMobProfGtpEntry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfGtpEntry.setStatus("current")
_TmnxMobProfGtpName_Type = TmnxMobProfName
_TmnxMobProfGtpName_Object = MibTableColumn
tmnxMobProfGtpName = _TmnxMobProfGtpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 1),
    _TmnxMobProfGtpName_Type()
)
tmnxMobProfGtpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfGtpName.setStatus("current")
_TmnxMobProfGtpRowStatus_Type = RowStatus
_TmnxMobProfGtpRowStatus_Object = MibTableColumn
tmnxMobProfGtpRowStatus = _TmnxMobProfGtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 2),
    _TmnxMobProfGtpRowStatus_Type()
)
tmnxMobProfGtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpRowStatus.setStatus("current")
_TmnxMobProfGtpLastChanged_Type = TimeStamp
_TmnxMobProfGtpLastChanged_Object = MibTableColumn
tmnxMobProfGtpLastChanged = _TmnxMobProfGtpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 3),
    _TmnxMobProfGtpLastChanged_Type()
)
tmnxMobProfGtpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfGtpLastChanged.setStatus("current")


class _TmnxMobProfGtpDescription_Type(TItemDescription):
    """Custom type tmnxMobProfGtpDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfGtpDescription_Object = MibTableColumn
tmnxMobProfGtpDescription = _TmnxMobProfGtpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 4),
    _TmnxMobProfGtpDescription_Type()
)
tmnxMobProfGtpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpDescription.setStatus("current")


class _TmnxMobProfGtpMsgReTxTimeout_Type(TmnxMobProfMsgReTxTimeout):
    """Custom type tmnxMobProfGtpMsgReTxTimeout based on TmnxMobProfMsgReTxTimeout"""
    defaultValue = 5


_TmnxMobProfGtpMsgReTxTimeout_Object = MibTableColumn
tmnxMobProfGtpMsgReTxTimeout = _TmnxMobProfGtpMsgReTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 5),
    _TmnxMobProfGtpMsgReTxTimeout_Type()
)
tmnxMobProfGtpMsgReTxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpMsgReTxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfGtpMsgReTxTimeout.setUnits("seconds")


class _TmnxMobProfGtpMsgReTxRetryCnt_Type(TmnxMobProfMsgReTxRetryCount):
    """Custom type tmnxMobProfGtpMsgReTxRetryCnt based on TmnxMobProfMsgReTxRetryCount"""
    defaultValue = 3


_TmnxMobProfGtpMsgReTxRetryCnt_Object = MibTableColumn
tmnxMobProfGtpMsgReTxRetryCnt = _TmnxMobProfGtpMsgReTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 6),
    _TmnxMobProfGtpMsgReTxRetryCnt_Type()
)
tmnxMobProfGtpMsgReTxRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpMsgReTxRetryCnt.setStatus("current")


class _TmnxMobProfGtpKeepAlvTimeout_Type(TmnxMobProfKeepAliveTimeout):
    """Custom type tmnxMobProfGtpKeepAlvTimeout based on TmnxMobProfKeepAliveTimeout"""
    defaultValue = 60


_TmnxMobProfGtpKeepAlvTimeout_Object = MibTableColumn
tmnxMobProfGtpKeepAlvTimeout = _TmnxMobProfGtpKeepAlvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 7),
    _TmnxMobProfGtpKeepAlvTimeout_Type()
)
tmnxMobProfGtpKeepAlvTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpKeepAlvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfGtpKeepAlvTimeout.setUnits("seconds")


class _TmnxMobProfGtpKeepAlvRetryCnt_Type(TmnxMobProfKeepAliveRetryCount):
    """Custom type tmnxMobProfGtpKeepAlvRetryCnt based on TmnxMobProfKeepAliveRetryCount"""
    defaultValue = 4


_TmnxMobProfGtpKeepAlvRetryCnt_Object = MibTableColumn
tmnxMobProfGtpKeepAlvRetryCnt = _TmnxMobProfGtpKeepAlvRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 8),
    _TmnxMobProfGtpKeepAlvRetryCnt_Type()
)
tmnxMobProfGtpKeepAlvRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpKeepAlvRetryCnt.setStatus("current")


class _TmnxMobProfGtpKeepAlvResp_Type(TmnxMobProfKeepAliveResponse):
    """Custom type tmnxMobProfGtpKeepAlvResp based on TmnxMobProfKeepAliveResponse"""
    defaultValue = 5


_TmnxMobProfGtpKeepAlvResp_Object = MibTableColumn
tmnxMobProfGtpKeepAlvResp = _TmnxMobProfGtpKeepAlvResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 9),
    _TmnxMobProfGtpKeepAlvResp_Type()
)
tmnxMobProfGtpKeepAlvResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpKeepAlvResp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfGtpKeepAlvResp.setUnits("seconds")


class _TmnxMobProfGtpIpTtl_Type(TmnxMobProfIpTtl):
    """Custom type tmnxMobProfGtpIpTtl based on TmnxMobProfIpTtl"""
    defaultValue = 255


_TmnxMobProfGtpIpTtl_Object = MibTableColumn
tmnxMobProfGtpIpTtl = _TmnxMobProfGtpIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 10),
    _TmnxMobProfGtpIpTtl_Type()
)
tmnxMobProfGtpIpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpIpTtl.setStatus("current")


class _TmnxMobProfGtpIpDscp_Type(TDSCPValue):
    """Custom type tmnxMobProfGtpIpDscp based on TDSCPValue"""
    defaultValue = 56


_TmnxMobProfGtpIpDscp_Object = MibTableColumn
tmnxMobProfGtpIpDscp = _TmnxMobProfGtpIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 6, 1, 11),
    _TmnxMobProfGtpIpDscp_Type()
)
tmnxMobProfGtpIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfGtpIpDscp.setStatus("current")
_TmnxMobProfPlmnListTable_Object = MibTable
tmnxMobProfPlmnListTable = _TmnxMobProfPlmnListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListTable.setStatus("current")
_TmnxMobProfPlmnListEntry_Object = MibTableRow
tmnxMobProfPlmnListEntry = _TmnxMobProfPlmnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7, 1)
)
tmnxMobProfPlmnListEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPlmnListName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPlmnListMcc"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPlmnListMnc"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListEntry.setStatus("current")
_TmnxMobProfPlmnListName_Type = TmnxMobProfName
_TmnxMobProfPlmnListName_Object = MibTableColumn
tmnxMobProfPlmnListName = _TmnxMobProfPlmnListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7, 1, 1),
    _TmnxMobProfPlmnListName_Type()
)
tmnxMobProfPlmnListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListName.setStatus("current")
_TmnxMobProfPlmnListMcc_Type = TmnxMobMcc
_TmnxMobProfPlmnListMcc_Object = MibTableColumn
tmnxMobProfPlmnListMcc = _TmnxMobProfPlmnListMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7, 1, 2),
    _TmnxMobProfPlmnListMcc_Type()
)
tmnxMobProfPlmnListMcc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListMcc.setStatus("current")
_TmnxMobProfPlmnListMnc_Type = TmnxMobMnc
_TmnxMobProfPlmnListMnc_Object = MibTableColumn
tmnxMobProfPlmnListMnc = _TmnxMobProfPlmnListMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7, 1, 3),
    _TmnxMobProfPlmnListMnc_Type()
)
tmnxMobProfPlmnListMnc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListMnc.setStatus("current")
_TmnxMobProfPlmnListRowStatus_Type = RowStatus
_TmnxMobProfPlmnListRowStatus_Object = MibTableColumn
tmnxMobProfPlmnListRowStatus = _TmnxMobProfPlmnListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 7, 1, 4),
    _TmnxMobProfPlmnListRowStatus_Type()
)
tmnxMobProfPlmnListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListRowStatus.setStatus("current")
_TmnxMobProfPolTable_Object = MibTable
tmnxMobProfPolTable = _TmnxMobProfPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxMobProfPolTable.setStatus("current")
_TmnxMobProfPolEntry_Object = MibTableRow
tmnxMobProfPolEntry = _TmnxMobProfPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1)
)
tmnxMobProfPolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPolEntry.setStatus("current")
_TmnxMobProfPolName_Type = TmnxMobProfName
_TmnxMobProfPolName_Object = MibTableColumn
tmnxMobProfPolName = _TmnxMobProfPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 1),
    _TmnxMobProfPolName_Type()
)
tmnxMobProfPolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPolName.setStatus("current")
_TmnxMobProfPolRowStatus_Type = RowStatus
_TmnxMobProfPolRowStatus_Object = MibTableColumn
tmnxMobProfPolRowStatus = _TmnxMobProfPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 2),
    _TmnxMobProfPolRowStatus_Type()
)
tmnxMobProfPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolRowStatus.setStatus("current")
_TmnxMobProfPolLastChanged_Type = TimeStamp
_TmnxMobProfPolLastChanged_Object = MibTableColumn
tmnxMobProfPolLastChanged = _TmnxMobProfPolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 3),
    _TmnxMobProfPolLastChanged_Type()
)
tmnxMobProfPolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolLastChanged.setStatus("current")


class _TmnxMobProfPolRuleUnitName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobProfPolRuleUnitName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPolRuleUnitName_Object = MibTableColumn
tmnxMobProfPolRuleUnitName = _TmnxMobProfPolRuleUnitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 4),
    _TmnxMobProfPolRuleUnitName_Type()
)
tmnxMobProfPolRuleUnitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolRuleUnitName.setStatus("current")


class _TmnxMobProfChgRuleUnitName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobProfChgRuleUnitName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfChgRuleUnitName_Object = MibTableColumn
tmnxMobProfChgRuleUnitName = _TmnxMobProfChgRuleUnitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 5),
    _TmnxMobProfChgRuleUnitName_Type()
)
tmnxMobProfChgRuleUnitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgRuleUnitName.setStatus("current")


class _TmnxMobProfPolQciValue_Type(TmnxMobQciValueOrZero):
    """Custom type tmnxMobProfPolQciValue based on TmnxMobQciValueOrZero"""
    defaultValue = 0


_TmnxMobProfPolQciValue_Object = MibTableColumn
tmnxMobProfPolQciValue = _TmnxMobProfPolQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 6),
    _TmnxMobProfPolQciValue_Type()
)
tmnxMobProfPolQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolQciValue.setStatus("current")


class _TmnxMobProfPolArpValue_Type(TmnxMobArpValueOrZero):
    """Custom type tmnxMobProfPolArpValue based on TmnxMobArpValueOrZero"""
    defaultValue = 0


_TmnxMobProfPolArpValue_Object = MibTableColumn
tmnxMobProfPolArpValue = _TmnxMobProfPolArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 7),
    _TmnxMobProfPolArpValue_Type()
)
tmnxMobProfPolArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolArpValue.setStatus("current")


class _TmnxMobProfPolPrecedence_Type(TmnxMobStaticPolPrecedenceOrZero):
    """Custom type tmnxMobProfPolPrecedence based on TmnxMobStaticPolPrecedenceOrZero"""
    defaultValue = 0


_TmnxMobProfPolPrecedence_Object = MibTableColumn
tmnxMobProfPolPrecedence = _TmnxMobProfPolPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 8),
    _TmnxMobProfPolPrecedence_Type()
)
tmnxMobProfPolPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolPrecedence.setStatus("current")


class _TmnxMobProfPolInUse_Type(TruthValue):
    """Custom type tmnxMobProfPolInUse based on TruthValue"""


_TmnxMobProfPolInUse_Object = MibTableColumn
tmnxMobProfPolInUse = _TmnxMobProfPolInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 9),
    _TmnxMobProfPolInUse_Type()
)
tmnxMobProfPolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolInUse.setStatus("current")
_TmnxMobProfPolRefCount_Type = Counter32
_TmnxMobProfPolRefCount_Object = MibTableColumn
tmnxMobProfPolRefCount = _TmnxMobProfPolRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 10),
    _TmnxMobProfPolRefCount_Type()
)
tmnxMobProfPolRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolRefCount.setStatus("current")
_TmnxMobProfPolConfRefCount_Type = Counter32
_TmnxMobProfPolConfRefCount_Object = MibTableColumn
tmnxMobProfPolConfRefCount = _TmnxMobProfPolConfRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 8, 1, 11),
    _TmnxMobProfPolConfRefCount_Type()
)
tmnxMobProfPolConfRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolConfRefCount.setStatus("current")
_TmnxMobProfPolUntFlwTable_Object = MibTable
tmnxMobProfPolUntFlwTable = _TmnxMobProfPolUntFlwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwTable.setStatus("current")
_TmnxMobProfPolUntFlwEntry_Object = MibTableRow
tmnxMobProfPolUntFlwEntry = _TmnxMobProfPolUntFlwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1)
)
tmnxMobProfPolUntFlwEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwId"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwEntry.setStatus("current")


class _TmnxMobProfPolUntFlwId_Type(Unsigned32):
    """Custom type tmnxMobProfPolUntFlwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxMobProfPolUntFlwId_Type.__name__ = "Unsigned32"
_TmnxMobProfPolUntFlwId_Object = MibTableColumn
tmnxMobProfPolUntFlwId = _TmnxMobProfPolUntFlwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 1),
    _TmnxMobProfPolUntFlwId_Type()
)
tmnxMobProfPolUntFlwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwId.setStatus("current")
_TmnxMobProfPolUntFlwRowStatus_Type = RowStatus
_TmnxMobProfPolUntFlwRowStatus_Object = MibTableColumn
tmnxMobProfPolUntFlwRowStatus = _TmnxMobProfPolUntFlwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 2),
    _TmnxMobProfPolUntFlwRowStatus_Type()
)
tmnxMobProfPolUntFlwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRowStatus.setStatus("current")
_TmnxMobProfPolUntFlwLastChanged_Type = TimeStamp
_TmnxMobProfPolUntFlwLastChanged_Object = MibTableColumn
tmnxMobProfPolUntFlwLastChanged = _TmnxMobProfPolUntFlwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 3),
    _TmnxMobProfPolUntFlwLastChanged_Type()
)
tmnxMobProfPolUntFlwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLastChanged.setStatus("current")


class _TmnxMobProfPolUntFlwDirection_Type(Integer32):
    """Custom type tmnxMobProfPolUntFlwDirection based on Integer32"""
    defaultValue = 3

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
          ("downLink", 1),
          ("upLink", 2))
    )


_TmnxMobProfPolUntFlwDirection_Type.__name__ = "Integer32"
_TmnxMobProfPolUntFlwDirection_Object = MibTableColumn
tmnxMobProfPolUntFlwDirection = _TmnxMobProfPolUntFlwDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 4),
    _TmnxMobProfPolUntFlwDirection_Type()
)
tmnxMobProfPolUntFlwDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwDirection.setStatus("current")


class _TmnxMobProfPolUntFlwMatchPrtcl_Type(TIpProtocol):
    """Custom type tmnxMobProfPolUntFlwMatchPrtcl based on TIpProtocol"""
    defaultValue = -2


_TmnxMobProfPolUntFlwMatchPrtcl_Object = MibTableColumn
tmnxMobProfPolUntFlwMatchPrtcl = _TmnxMobProfPolUntFlwMatchPrtcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 5),
    _TmnxMobProfPolUntFlwMatchPrtcl_Type()
)
tmnxMobProfPolUntFlwMatchPrtcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwMatchPrtcl.setStatus("current")


class _TmnxMobProfPolUntFlwLclAddrType_Type(InetAddressType):
    """Custom type tmnxMobProfPolUntFlwLclAddrType based on InetAddressType"""


_TmnxMobProfPolUntFlwLclAddrType_Object = MibTableColumn
tmnxMobProfPolUntFlwLclAddrType = _TmnxMobProfPolUntFlwLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 6),
    _TmnxMobProfPolUntFlwLclAddrType_Type()
)
tmnxMobProfPolUntFlwLclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclAddrType.setStatus("current")


class _TmnxMobProfPolUntFlwLclAddr_Type(InetAddress):
    """Custom type tmnxMobProfPolUntFlwLclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobProfPolUntFlwLclAddr_Type.__name__ = "InetAddress"
_TmnxMobProfPolUntFlwLclAddr_Object = MibTableColumn
tmnxMobProfPolUntFlwLclAddr = _TmnxMobProfPolUntFlwLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 7),
    _TmnxMobProfPolUntFlwLclAddr_Type()
)
tmnxMobProfPolUntFlwLclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclAddr.setStatus("current")


class _TmnxMobProfPolUntFlwLclPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxMobProfPolUntFlwLclPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxMobProfPolUntFlwLclPrefixLen_Object = MibTableColumn
tmnxMobProfPolUntFlwLclPrefixLen = _TmnxMobProfPolUntFlwLclPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 8),
    _TmnxMobProfPolUntFlwLclPrefixLen_Type()
)
tmnxMobProfPolUntFlwLclPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclPrefixLen.setStatus("current")


class _TmnxMobProfPolUntFlwRmtAddrType_Type(InetAddressType):
    """Custom type tmnxMobProfPolUntFlwRmtAddrType based on InetAddressType"""


_TmnxMobProfPolUntFlwRmtAddrType_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtAddrType = _TmnxMobProfPolUntFlwRmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 9),
    _TmnxMobProfPolUntFlwRmtAddrType_Type()
)
tmnxMobProfPolUntFlwRmtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtAddrType.setStatus("current")


class _TmnxMobProfPolUntFlwRmtAddr_Type(InetAddress):
    """Custom type tmnxMobProfPolUntFlwRmtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobProfPolUntFlwRmtAddr_Type.__name__ = "InetAddress"
_TmnxMobProfPolUntFlwRmtAddr_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtAddr = _TmnxMobProfPolUntFlwRmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 10),
    _TmnxMobProfPolUntFlwRmtAddr_Type()
)
tmnxMobProfPolUntFlwRmtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtAddr.setStatus("current")


class _TmnxMobProfPolUntFlwRmtPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxMobProfPolUntFlwRmtPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxMobProfPolUntFlwRmtPrefixLen_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtPrefixLen = _TmnxMobProfPolUntFlwRmtPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 11),
    _TmnxMobProfPolUntFlwRmtPrefixLen_Type()
)
tmnxMobProfPolUntFlwRmtPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtPrefixLen.setStatus("current")


class _TmnxMobProfPolUntFlwLclPortVal1_Type(TTcpUdpPort):
    """Custom type tmnxMobProfPolUntFlwLclPortVal1 based on TTcpUdpPort"""
    defaultValue = 0


_TmnxMobProfPolUntFlwLclPortVal1_Object = MibTableColumn
tmnxMobProfPolUntFlwLclPortVal1 = _TmnxMobProfPolUntFlwLclPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 12),
    _TmnxMobProfPolUntFlwLclPortVal1_Type()
)
tmnxMobProfPolUntFlwLclPortVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclPortVal1.setStatus("current")


class _TmnxMobProfPolUntFlwLclPortVal2_Type(TTcpUdpPort):
    """Custom type tmnxMobProfPolUntFlwLclPortVal2 based on TTcpUdpPort"""
    defaultValue = 0


_TmnxMobProfPolUntFlwLclPortVal2_Object = MibTableColumn
tmnxMobProfPolUntFlwLclPortVal2 = _TmnxMobProfPolUntFlwLclPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 13),
    _TmnxMobProfPolUntFlwLclPortVal2_Type()
)
tmnxMobProfPolUntFlwLclPortVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclPortVal2.setStatus("current")


class _TmnxMobProfPolUntFlwLclPortOper_Type(TTcpUdpPortOperator):
    """Custom type tmnxMobProfPolUntFlwLclPortOper based on TTcpUdpPortOperator"""


_TmnxMobProfPolUntFlwLclPortOper_Object = MibTableColumn
tmnxMobProfPolUntFlwLclPortOper = _TmnxMobProfPolUntFlwLclPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 14),
    _TmnxMobProfPolUntFlwLclPortOper_Type()
)
tmnxMobProfPolUntFlwLclPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwLclPortOper.setStatus("current")


class _TmnxMobProfPolUntFlwRmtPortVal1_Type(TTcpUdpPort):
    """Custom type tmnxMobProfPolUntFlwRmtPortVal1 based on TTcpUdpPort"""
    defaultValue = 0


_TmnxMobProfPolUntFlwRmtPortVal1_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtPortVal1 = _TmnxMobProfPolUntFlwRmtPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 15),
    _TmnxMobProfPolUntFlwRmtPortVal1_Type()
)
tmnxMobProfPolUntFlwRmtPortVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtPortVal1.setStatus("current")


class _TmnxMobProfPolUntFlwRmtPortVal2_Type(TTcpUdpPort):
    """Custom type tmnxMobProfPolUntFlwRmtPortVal2 based on TTcpUdpPort"""
    defaultValue = 0


_TmnxMobProfPolUntFlwRmtPortVal2_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtPortVal2 = _TmnxMobProfPolUntFlwRmtPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 16),
    _TmnxMobProfPolUntFlwRmtPortVal2_Type()
)
tmnxMobProfPolUntFlwRmtPortVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtPortVal2.setStatus("current")


class _TmnxMobProfPolUntFlwRmtPortOper_Type(TTcpUdpPortOperator):
    """Custom type tmnxMobProfPolUntFlwRmtPortOper based on TTcpUdpPortOperator"""


_TmnxMobProfPolUntFlwRmtPortOper_Object = MibTableColumn
tmnxMobProfPolUntFlwRmtPortOper = _TmnxMobProfPolUntFlwRmtPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 17),
    _TmnxMobProfPolUntFlwRmtPortOper_Type()
)
tmnxMobProfPolUntFlwRmtPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwRmtPortOper.setStatus("current")


class _TmnxMobProfPolUntFlwAaApp_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobProfPolUntFlwAaApp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPolUntFlwAaApp_Object = MibTableColumn
tmnxMobProfPolUntFlwAaApp = _TmnxMobProfPolUntFlwAaApp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 9, 1, 18),
    _TmnxMobProfPolUntFlwAaApp_Type()
)
tmnxMobProfPolUntFlwAaApp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwAaApp.setStatus("current")
_TmnxMobProfPolBaseTable_Object = MibTable
tmnxMobProfPolBaseTable = _TmnxMobProfPolBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseTable.setStatus("current")
_TmnxMobProfPolBaseEntry_Object = MibTableRow
tmnxMobProfPolBaseEntry = _TmnxMobProfPolBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1)
)
tmnxMobProfPolBaseEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseEntry.setStatus("current")
_TmnxMobProfPolBaseName_Type = TmnxMobProfName
_TmnxMobProfPolBaseName_Object = MibTableColumn
tmnxMobProfPolBaseName = _TmnxMobProfPolBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 1),
    _TmnxMobProfPolBaseName_Type()
)
tmnxMobProfPolBaseName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseName.setStatus("current")
_TmnxMobProfPolBaseRowStatus_Type = RowStatus
_TmnxMobProfPolBaseRowStatus_Object = MibTableColumn
tmnxMobProfPolBaseRowStatus = _TmnxMobProfPolBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 2),
    _TmnxMobProfPolBaseRowStatus_Type()
)
tmnxMobProfPolBaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseRowStatus.setStatus("current")
_TmnxMobProfPolBaseLastChanged_Type = TimeStamp
_TmnxMobProfPolBaseLastChanged_Object = MibTableColumn
tmnxMobProfPolBaseLastChanged = _TmnxMobProfPolBaseLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 3),
    _TmnxMobProfPolBaseLastChanged_Type()
)
tmnxMobProfPolBaseLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseLastChanged.setStatus("current")


class _TmnxMobProfPolBasePrecedence_Type(TmnxMobStaticPolPrecedenceOrZero):
    """Custom type tmnxMobProfPolBasePrecedence based on TmnxMobStaticPolPrecedenceOrZero"""
    defaultValue = 0


_TmnxMobProfPolBasePrecedence_Object = MibTableColumn
tmnxMobProfPolBasePrecedence = _TmnxMobProfPolBasePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 4),
    _TmnxMobProfPolBasePrecedence_Type()
)
tmnxMobProfPolBasePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolBasePrecedence.setStatus("current")


class _TmnxMobProfPolBasePreActivate_Type(TruthValue):
    """Custom type tmnxMobProfPolBasePreActivate based on TruthValue"""


_TmnxMobProfPolBasePreActivate_Object = MibTableColumn
tmnxMobProfPolBasePreActivate = _TmnxMobProfPolBasePreActivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 5),
    _TmnxMobProfPolBasePreActivate_Type()
)
tmnxMobProfPolBasePreActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolBasePreActivate.setStatus("current")


class _TmnxMobProfPolBaseInUse_Type(TruthValue):
    """Custom type tmnxMobProfPolBaseInUse based on TruthValue"""


_TmnxMobProfPolBaseInUse_Object = MibTableColumn
tmnxMobProfPolBaseInUse = _TmnxMobProfPolBaseInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 6),
    _TmnxMobProfPolBaseInUse_Type()
)
tmnxMobProfPolBaseInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseInUse.setStatus("current")
_TmnxMobProfPolBaseRefCount_Type = Counter32
_TmnxMobProfPolBaseRefCount_Object = MibTableColumn
tmnxMobProfPolBaseRefCount = _TmnxMobProfPolBaseRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 7),
    _TmnxMobProfPolBaseRefCount_Type()
)
tmnxMobProfPolBaseRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseRefCount.setStatus("current")
_TmnxMobProfPolBaseConfRefCount_Type = Counter32
_TmnxMobProfPolBaseConfRefCount_Object = MibTableColumn
tmnxMobProfPolBaseConfRefCount = _TmnxMobProfPolBaseConfRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 10, 1, 8),
    _TmnxMobProfPolBaseConfRefCount_Type()
)
tmnxMobProfPolBaseConfRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseConfRefCount.setStatus("current")
_TmnxMobProfQciPolTable_Object = MibTable
tmnxMobProfQciPolTable = _TmnxMobProfQciPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxMobProfQciPolTable.setStatus("current")
_TmnxMobProfQciPolEntry_Object = MibTableRow
tmnxMobProfQciPolEntry = _TmnxMobProfQciPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11, 1)
)
tmnxMobProfQciPolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfQciPolEntry.setStatus("current")
_TmnxMobProfQciPolName_Type = TmnxMobProfName
_TmnxMobProfQciPolName_Object = MibTableColumn
tmnxMobProfQciPolName = _TmnxMobProfQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11, 1, 1),
    _TmnxMobProfQciPolName_Type()
)
tmnxMobProfQciPolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolName.setStatus("current")
_TmnxMobProfQciPolRowStatus_Type = RowStatus
_TmnxMobProfQciPolRowStatus_Object = MibTableColumn
tmnxMobProfQciPolRowStatus = _TmnxMobProfQciPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11, 1, 2),
    _TmnxMobProfQciPolRowStatus_Type()
)
tmnxMobProfQciPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolRowStatus.setStatus("current")
_TmnxMobProfQciPolLastChanged_Type = TimeStamp
_TmnxMobProfQciPolLastChanged_Object = MibTableColumn
tmnxMobProfQciPolLastChanged = _TmnxMobProfQciPolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11, 1, 3),
    _TmnxMobProfQciPolLastChanged_Type()
)
tmnxMobProfQciPolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolLastChanged.setStatus("current")


class _TmnxMobProfQciPolDescription_Type(TItemDescription):
    """Custom type tmnxMobProfQciPolDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfQciPolDescription_Object = MibTableColumn
tmnxMobProfQciPolDescription = _TmnxMobProfQciPolDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 11, 1, 4),
    _TmnxMobProfQciPolDescription_Type()
)
tmnxMobProfQciPolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolDescription.setStatus("current")
_TmnxMobProfQciPolQciTable_Object = MibTable
tmnxMobProfQciPolQciTable = _TmnxMobProfQciPolQciTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciTable.setStatus("current")
_TmnxMobProfQciPolQciEntry_Object = MibTableRow
tmnxMobProfQciPolQciEntry = _TmnxMobProfQciPolQciEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1)
)
tmnxMobProfQciPolQciEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciValue"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciArpValue"),
)
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciEntry.setStatus("current")
_TmnxMobProfQciPolQciValue_Type = TmnxMobQciValue
_TmnxMobProfQciPolQciValue_Object = MibTableColumn
tmnxMobProfQciPolQciValue = _TmnxMobProfQciPolQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 1),
    _TmnxMobProfQciPolQciValue_Type()
)
tmnxMobProfQciPolQciValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciValue.setStatus("current")
_TmnxMobProfQciPolQciArpValue_Type = TmnxMobArpValue
_TmnxMobProfQciPolQciArpValue_Object = MibTableColumn
tmnxMobProfQciPolQciArpValue = _TmnxMobProfQciPolQciArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 2),
    _TmnxMobProfQciPolQciArpValue_Type()
)
tmnxMobProfQciPolQciArpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciArpValue.setStatus("current")
_TmnxMobProfQciPolQciLastChanged_Type = TimeStamp
_TmnxMobProfQciPolQciLastChanged_Object = MibTableColumn
tmnxMobProfQciPolQciLastChanged = _TmnxMobProfQciPolQciLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 3),
    _TmnxMobProfQciPolQciLastChanged_Type()
)
tmnxMobProfQciPolQciLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciLastChanged.setStatus("current")


class _TmnxMobProfQciPolQciDscpPreserve_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfQciPolQciDscpPreserve based on TmnxEnabledDisabled"""


_TmnxMobProfQciPolQciDscpPreserve_Object = MibTableColumn
tmnxMobProfQciPolQciDscpPreserve = _TmnxMobProfQciPolQciDscpPreserve_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 4),
    _TmnxMobProfQciPolQciDscpPreserve_Type()
)
tmnxMobProfQciPolQciDscpPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciDscpPreserve.setStatus("current")
_TmnxMobProfQciPolQciDscp_Type = TDSCPName
_TmnxMobProfQciPolQciDscp_Object = MibTableColumn
tmnxMobProfQciPolQciDscp = _TmnxMobProfQciPolQciDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 5),
    _TmnxMobProfQciPolQciDscp_Type()
)
tmnxMobProfQciPolQciDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciDscp.setStatus("current")
_TmnxMobProfQciPolQciDscpOut_Type = TDSCPName
_TmnxMobProfQciPolQciDscpOut_Object = MibTableColumn
tmnxMobProfQciPolQciDscpOut = _TmnxMobProfQciPolQciDscpOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 6),
    _TmnxMobProfQciPolQciDscpOut_Type()
)
tmnxMobProfQciPolQciDscpOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciDscpOut.setStatus("current")
_TmnxMobProfQciPolQciFcName_Type = TFCName
_TmnxMobProfQciPolQciFcName_Object = MibTableColumn
tmnxMobProfQciPolQciFcName = _TmnxMobProfQciPolQciFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 7),
    _TmnxMobProfQciPolQciFcName_Type()
)
tmnxMobProfQciPolQciFcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciFcName.setStatus("current")


class _TmnxMobProfQciPolQciProfile_Type(Integer32):
    """Custom type tmnxMobProfQciPolQciProfile based on Integer32"""
    defaultValue = 0

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
        *(("applyCir", 3),
          ("in", 1),
          ("none", 0),
          ("out", 2))
    )


_TmnxMobProfQciPolQciProfile_Type.__name__ = "Integer32"
_TmnxMobProfQciPolQciProfile_Object = MibTableColumn
tmnxMobProfQciPolQciProfile = _TmnxMobProfQciPolQciProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 12, 1, 8),
    _TmnxMobProfQciPolQciProfile_Type()
)
tmnxMobProfQciPolQciProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciProfile.setStatus("current")
_TmnxMobProfPeerListTable_Object = MibTable
tmnxMobProfPeerListTable = _TmnxMobProfPeerListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxMobProfPeerListTable.setStatus("current")
_TmnxMobProfPeerListEntry_Object = MibTableRow
tmnxMobProfPeerListEntry = _TmnxMobProfPeerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13, 1)
)
tmnxMobProfPeerListEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPeerListEntry.setStatus("current")
_TmnxMobProfPeerListName_Type = TmnxMobProfName
_TmnxMobProfPeerListName_Object = MibTableColumn
tmnxMobProfPeerListName = _TmnxMobProfPeerListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13, 1, 1),
    _TmnxMobProfPeerListName_Type()
)
tmnxMobProfPeerListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListName.setStatus("current")
_TmnxMobProfPeerListRowStatus_Type = RowStatus
_TmnxMobProfPeerListRowStatus_Object = MibTableColumn
tmnxMobProfPeerListRowStatus = _TmnxMobProfPeerListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13, 1, 2),
    _TmnxMobProfPeerListRowStatus_Type()
)
tmnxMobProfPeerListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListRowStatus.setStatus("current")
_TmnxMobProfPeerListLastChanged_Type = TimeStamp
_TmnxMobProfPeerListLastChanged_Object = MibTableColumn
tmnxMobProfPeerListLastChanged = _TmnxMobProfPeerListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13, 1, 3),
    _TmnxMobProfPeerListLastChanged_Type()
)
tmnxMobProfPeerListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListLastChanged.setStatus("current")


class _TmnxMobProfPeerListDescription_Type(TItemDescription):
    """Custom type tmnxMobProfPeerListDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfPeerListDescription_Object = MibTableColumn
tmnxMobProfPeerListDescription = _TmnxMobProfPeerListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 13, 1, 4),
    _TmnxMobProfPeerListDescription_Type()
)
tmnxMobProfPeerListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListDescription.setStatus("current")
_TmnxMobProfPeerListPeerTable_Object = MibTable
tmnxMobProfPeerListPeerTable = _TmnxMobProfPeerListPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerTable.setStatus("current")
_TmnxMobProfPeerListPeerEntry_Object = MibTableRow
tmnxMobProfPeerListPeerEntry = _TmnxMobProfPeerListPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1)
)
tmnxMobProfPeerListPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerAddrType"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerAddr"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerEntry.setStatus("current")
_TmnxMobProfPeerListPeerAddrType_Type = InetAddressType
_TmnxMobProfPeerListPeerAddrType_Object = MibTableColumn
tmnxMobProfPeerListPeerAddrType = _TmnxMobProfPeerListPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 1),
    _TmnxMobProfPeerListPeerAddrType_Type()
)
tmnxMobProfPeerListPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerAddrType.setStatus("current")


class _TmnxMobProfPeerListPeerAddr_Type(InetAddress):
    """Custom type tmnxMobProfPeerListPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobProfPeerListPeerAddr_Type.__name__ = "InetAddress"
_TmnxMobProfPeerListPeerAddr_Object = MibTableColumn
tmnxMobProfPeerListPeerAddr = _TmnxMobProfPeerListPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 2),
    _TmnxMobProfPeerListPeerAddr_Type()
)
tmnxMobProfPeerListPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerAddr.setStatus("current")
_TmnxMobProfPeerListPeerPrefixLen_Type = InetAddressPrefixLength
_TmnxMobProfPeerListPeerPrefixLen_Object = MibTableColumn
tmnxMobProfPeerListPeerPrefixLen = _TmnxMobProfPeerListPeerPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 3),
    _TmnxMobProfPeerListPeerPrefixLen_Type()
)
tmnxMobProfPeerListPeerPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerPrefixLen.setStatus("current")
_TmnxMobProfPeerListPeerRowStatus_Type = RowStatus
_TmnxMobProfPeerListPeerRowStatus_Object = MibTableColumn
tmnxMobProfPeerListPeerRowStatus = _TmnxMobProfPeerListPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 4),
    _TmnxMobProfPeerListPeerRowStatus_Type()
)
tmnxMobProfPeerListPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerRowStatus.setStatus("current")
_TmnxMobProfPeerListPeerLastChgd_Type = TimeStamp
_TmnxMobProfPeerListPeerLastChgd_Object = MibTableColumn
tmnxMobProfPeerListPeerLastChgd = _TmnxMobProfPeerListPeerLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 5),
    _TmnxMobProfPeerListPeerLastChgd_Type()
)
tmnxMobProfPeerListPeerLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerLastChgd.setStatus("current")


class _TmnxMobProfPeerListPeerDesc_Type(TItemDescription):
    """Custom type tmnxMobProfPeerListPeerDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfPeerListPeerDesc_Object = MibTableColumn
tmnxMobProfPeerListPeerDesc = _TmnxMobProfPeerListPeerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 6),
    _TmnxMobProfPeerListPeerDesc_Type()
)
tmnxMobProfPeerListPeerDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerDesc.setStatus("current")


class _TmnxMobProfPeerListPeerKeepAlive_Type(TruthValue):
    """Custom type tmnxMobProfPeerListPeerKeepAlive based on TruthValue"""


_TmnxMobProfPeerListPeerKeepAlive_Object = MibTableColumn
tmnxMobProfPeerListPeerKeepAlive = _TmnxMobProfPeerListPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 7),
    _TmnxMobProfPeerListPeerKeepAlive_Type()
)
tmnxMobProfPeerListPeerKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerKeepAlive.setStatus("current")


class _TmnxMobProfPeerListPeerAdmnState_Type(TmnxAdminState):
    """Custom type tmnxMobProfPeerListPeerAdmnState based on TmnxAdminState"""


_TmnxMobProfPeerListPeerAdmnState_Object = MibTableColumn
tmnxMobProfPeerListPeerAdmnState = _TmnxMobProfPeerListPeerAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 8),
    _TmnxMobProfPeerListPeerAdmnState_Type()
)
tmnxMobProfPeerListPeerAdmnState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerAdmnState.setStatus("current")


class _TmnxMobProfPeerListPeerRatType_Type(Integer32):
    """Custom type tmnxMobProfPeerListPeerRatType based on Integer32"""
    defaultValue = 2

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
        *(("ehrpd", 4),
          ("eutran", 3),
          ("geran", 1),
          ("hrpd", 5),
          ("oneXrtt", 6),
          ("umb", 7),
          ("utran", 2))
    )


_TmnxMobProfPeerListPeerRatType_Type.__name__ = "Integer32"
_TmnxMobProfPeerListPeerRatType_Object = MibTableColumn
tmnxMobProfPeerListPeerRatType = _TmnxMobProfPeerListPeerRatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 9),
    _TmnxMobProfPeerListPeerRatType_Type()
)
tmnxMobProfPeerListPeerRatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerRatType.setStatus("current")


class _TmnxMobProfPeerListPeerForeign_Type(Integer32):
    """Custom type tmnxMobProfPeerListPeerForeign based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("foreign", 2),
          ("home", 1),
          ("none", 3))
    )


_TmnxMobProfPeerListPeerForeign_Type.__name__ = "Integer32"
_TmnxMobProfPeerListPeerForeign_Object = MibTableColumn
tmnxMobProfPeerListPeerForeign = _TmnxMobProfPeerListPeerForeign_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 10),
    _TmnxMobProfPeerListPeerForeign_Type()
)
tmnxMobProfPeerListPeerForeign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerForeign.setStatus("current")


class _TmnxMobProfPeerListPeerPlmnMcc_Type(TmnxMobMccOrEmpty):
    """Custom type tmnxMobProfPeerListPeerPlmnMcc based on TmnxMobMccOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPeerListPeerPlmnMcc_Object = MibTableColumn
tmnxMobProfPeerListPeerPlmnMcc = _TmnxMobProfPeerListPeerPlmnMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 11),
    _TmnxMobProfPeerListPeerPlmnMcc_Type()
)
tmnxMobProfPeerListPeerPlmnMcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerPlmnMcc.setStatus("current")


class _TmnxMobProfPeerListPeerPlmnMnc_Type(TmnxMobMncOrEmpty):
    """Custom type tmnxMobProfPeerListPeerPlmnMnc based on TmnxMobMncOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPeerListPeerPlmnMnc_Object = MibTableColumn
tmnxMobProfPeerListPeerPlmnMnc = _TmnxMobProfPeerListPeerPlmnMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 14, 1, 12),
    _TmnxMobProfPeerListPeerPlmnMnc_Type()
)
tmnxMobProfPeerListPeerPlmnMnc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerPlmnMnc.setStatus("current")
_TmnxMobProfSgwChargingTable_Object = MibTable
tmnxMobProfSgwChargingTable = _TmnxMobProfSgwChargingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxMobProfSgwChargingTable.setStatus("current")
_TmnxMobProfSgwChargingEntry_Object = MibTableRow
tmnxMobProfSgwChargingEntry = _TmnxMobProfSgwChargingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1)
)
tmnxMobProfSgwChargingEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgId"),
)
if mibBuilder.loadTexts:
    tmnxMobProfSgwChargingEntry.setStatus("current")
_TmnxMobProfSgwChrgId_Type = TmnxMobChargingProfile
_TmnxMobProfSgwChrgId_Object = MibTableColumn
tmnxMobProfSgwChrgId = _TmnxMobProfSgwChrgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 1),
    _TmnxMobProfSgwChrgId_Type()
)
tmnxMobProfSgwChrgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgId.setStatus("current")
_TmnxMobProfSgwChrgRowStatus_Type = RowStatus
_TmnxMobProfSgwChrgRowStatus_Object = MibTableColumn
tmnxMobProfSgwChrgRowStatus = _TmnxMobProfSgwChrgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 2),
    _TmnxMobProfSgwChrgRowStatus_Type()
)
tmnxMobProfSgwChrgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgRowStatus.setStatus("current")
_TmnxMobProfSgwChrgLastChanged_Type = TimeStamp
_TmnxMobProfSgwChrgLastChanged_Object = MibTableColumn
tmnxMobProfSgwChrgLastChanged = _TmnxMobProfSgwChrgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 3),
    _TmnxMobProfSgwChrgLastChanged_Type()
)
tmnxMobProfSgwChrgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgLastChanged.setStatus("current")


class _TmnxMobProfSgwChrgDesc_Type(TItemDescription):
    """Custom type tmnxMobProfSgwChrgDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfSgwChrgDesc_Object = MibTableColumn
tmnxMobProfSgwChrgDesc = _TmnxMobProfSgwChrgDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 4),
    _TmnxMobProfSgwChrgDesc_Type()
)
tmnxMobProfSgwChrgDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgDesc.setStatus("current")


class _TmnxMobProfSgwChrgOffLineState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgOffLineState based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgOffLineState_Object = MibTableColumn
tmnxMobProfSgwChrgOffLineState = _TmnxMobProfSgwChrgOffLineState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 5),
    _TmnxMobProfSgwChrgOffLineState_Type()
)
tmnxMobProfSgwChrgOffLineState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgOffLineState.setStatus("current")


class _TmnxMobProfSgwChrgPriCdfDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfSgwChrgPriCdfDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfSgwChrgPriCdfDiaPeer_Object = MibTableColumn
tmnxMobProfSgwChrgPriCdfDiaPeer = _TmnxMobProfSgwChrgPriCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 6),
    _TmnxMobProfSgwChrgPriCdfDiaPeer_Type()
)
tmnxMobProfSgwChrgPriCdfDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPriCdfDiaPeer.setStatus("current")


class _TmnxMobProfSgwChrgSecCdfDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfSgwChrgSecCdfDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfSgwChrgSecCdfDiaPeer_Object = MibTableColumn
tmnxMobProfSgwChrgSecCdfDiaPeer = _TmnxMobProfSgwChrgSecCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 7),
    _TmnxMobProfSgwChrgSecCdfDiaPeer_Type()
)
tmnxMobProfSgwChrgSecCdfDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgSecCdfDiaPeer.setStatus("current")


class _TmnxMobProfSgwChrgCitQosChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgCitQosChange based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgCitQosChange_Object = MibTableColumn
tmnxMobProfSgwChrgCitQosChange = _TmnxMobProfSgwChrgCitQosChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 8),
    _TmnxMobProfSgwChrgCitQosChange_Type()
)
tmnxMobProfSgwChrgCitQosChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitQosChange.setStatus("current")


class _TmnxMobProfSgwChrgCitUsrLocChnge_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgCitUsrLocChnge based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgCitUsrLocChnge_Object = MibTableColumn
tmnxMobProfSgwChrgCitUsrLocChnge = _TmnxMobProfSgwChrgCitUsrLocChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 9),
    _TmnxMobProfSgwChrgCitUsrLocChnge_Type()
)
tmnxMobProfSgwChrgCitUsrLocChnge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitUsrLocChnge.setStatus("current")


class _TmnxMobProfSgwChrgCitTrfTimeChng_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgCitTrfTimeChng based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgCitTrfTimeChng_Object = MibTableColumn
tmnxMobProfSgwChrgCitTrfTimeChng = _TmnxMobProfSgwChrgCitTrfTimeChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 10),
    _TmnxMobProfSgwChrgCitTrfTimeChng_Type()
)
tmnxMobProfSgwChrgCitTrfTimeChng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitTrfTimeChng.setStatus("current")


class _TmnxMobProfSgwChrgCitTrfTmStart_Type(TmnxTimeInSec):
    """Custom type tmnxMobProfSgwChrgCitTrfTmStart based on TmnxTimeInSec"""
    defaultValue = 0


_TmnxMobProfSgwChrgCitTrfTmStart_Object = MibTableColumn
tmnxMobProfSgwChrgCitTrfTmStart = _TmnxMobProfSgwChrgCitTrfTmStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 11),
    _TmnxMobProfSgwChrgCitTrfTmStart_Type()
)
tmnxMobProfSgwChrgCitTrfTmStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitTrfTmStart.setStatus("current")


class _TmnxMobProfSgwChrgCitTrfTmEnd_Type(TmnxTimeInSec):
    """Custom type tmnxMobProfSgwChrgCitTrfTmEnd based on TmnxTimeInSec"""
    defaultValue = 0


_TmnxMobProfSgwChrgCitTrfTmEnd_Object = MibTableColumn
tmnxMobProfSgwChrgCitTrfTmEnd = _TmnxMobProfSgwChrgCitTrfTmEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 12),
    _TmnxMobProfSgwChrgCitTrfTmEnd_Type()
)
tmnxMobProfSgwChrgCitTrfTmEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitTrfTmEnd.setStatus("current")


class _TmnxMobProfSgwChrgPrctTimeLmt_Type(Unsigned32):
    """Custom type tmnxMobProfSgwChrgPrctTimeLmt based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxMobProfSgwChrgPrctTimeLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfSgwChrgPrctTimeLmt_Object = MibTableColumn
tmnxMobProfSgwChrgPrctTimeLmt = _TmnxMobProfSgwChrgPrctTimeLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 13),
    _TmnxMobProfSgwChrgPrctTimeLmt_Type()
)
tmnxMobProfSgwChrgPrctTimeLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctTimeLmt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctTimeLmt.setUnits("seconds")


class _TmnxMobProfSgwChrgPrctVolumeLmt_Type(Unsigned32):
    """Custom type tmnxMobProfSgwChrgPrctVolumeLmt based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMobProfSgwChrgPrctVolumeLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfSgwChrgPrctVolumeLmt_Object = MibTableColumn
tmnxMobProfSgwChrgPrctVolumeLmt = _TmnxMobProfSgwChrgPrctVolumeLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 14),
    _TmnxMobProfSgwChrgPrctVolumeLmt_Type()
)
tmnxMobProfSgwChrgPrctVolumeLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctVolumeLmt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctVolumeLmt.setUnits("kbytes")


class _TmnxMobProfSgwChrgPrctMaxChCond_Type(Unsigned32):
    """Custom type tmnxMobProfSgwChrgPrctMaxChCond based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxMobProfSgwChrgPrctMaxChCond_Type.__name__ = "Unsigned32"
_TmnxMobProfSgwChrgPrctMaxChCond_Object = MibTableColumn
tmnxMobProfSgwChrgPrctMaxChCond = _TmnxMobProfSgwChrgPrctMaxChCond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 15),
    _TmnxMobProfSgwChrgPrctMaxChCond_Type()
)
tmnxMobProfSgwChrgPrctMaxChCond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctMaxChCond.setStatus("current")


class _TmnxMobProfSgwChrgPrctMsTmzChnge_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgPrctMsTmzChnge based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgPrctMsTmzChnge_Object = MibTableColumn
tmnxMobProfSgwChrgPrctMsTmzChnge = _TmnxMobProfSgwChrgPrctMsTmzChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 16),
    _TmnxMobProfSgwChrgPrctMsTmzChnge_Type()
)
tmnxMobProfSgwChrgPrctMsTmzChnge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctMsTmzChnge.setStatus("current")


class _TmnxMobProfSgwChrgPrctPlmnChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgPrctPlmnChange based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgPrctPlmnChange_Object = MibTableColumn
tmnxMobProfSgwChrgPrctPlmnChange = _TmnxMobProfSgwChrgPrctPlmnChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 17),
    _TmnxMobProfSgwChrgPrctPlmnChange_Type()
)
tmnxMobProfSgwChrgPrctPlmnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctPlmnChange.setStatus("current")


class _TmnxMobProfSgwChrgPrctRatChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgPrctRatChange based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgPrctRatChange_Object = MibTableColumn
tmnxMobProfSgwChrgPrctRatChange = _TmnxMobProfSgwChrgPrctRatChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 18),
    _TmnxMobProfSgwChrgPrctRatChange_Type()
)
tmnxMobProfSgwChrgPrctRatChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctRatChange.setStatus("current")


class _TmnxMobProfSgwChrgPrctMgmtInterv_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgPrctMgmtInterv based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgPrctMgmtInterv_Object = MibTableColumn
tmnxMobProfSgwChrgPrctMgmtInterv = _TmnxMobProfSgwChrgPrctMgmtInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 19),
    _TmnxMobProfSgwChrgPrctMgmtInterv_Type()
)
tmnxMobProfSgwChrgPrctMgmtInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctMgmtInterv.setStatus("current")


class _TmnxMobProfSgwChrgCitSgwChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfSgwChrgCitSgwChange based on TmnxEnabledDisabled"""


_TmnxMobProfSgwChrgCitSgwChange_Object = MibTableColumn
tmnxMobProfSgwChrgCitSgwChange = _TmnxMobProfSgwChrgCitSgwChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 20),
    _TmnxMobProfSgwChrgCitSgwChange_Type()
)
tmnxMobProfSgwChrgCitSgwChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgCitSgwChange.setStatus("obsolete")


class _TmnxMobProfSgwChrgPrctSrvNdChLmt_Type(Unsigned32):
    """Custom type tmnxMobProfSgwChrgPrctSrvNdChLmt based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxMobProfSgwChrgPrctSrvNdChLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfSgwChrgPrctSrvNdChLmt_Object = MibTableColumn
tmnxMobProfSgwChrgPrctSrvNdChLmt = _TmnxMobProfSgwChrgPrctSrvNdChLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 15, 1, 21),
    _TmnxMobProfSgwChrgPrctSrvNdChLmt_Type()
)
tmnxMobProfSgwChrgPrctSrvNdChLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChrgPrctSrvNdChLmt.setStatus("current")
_TmnxMobProfPgwChargingTable_Object = MibTable
tmnxMobProfPgwChargingTable = _TmnxMobProfPgwChargingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxMobProfPgwChargingTable.setStatus("current")
_TmnxMobProfPgwChargingEntry_Object = MibTableRow
tmnxMobProfPgwChargingEntry = _TmnxMobProfPgwChargingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1)
)
tmnxMobProfPgwChargingEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgId"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPgwChargingEntry.setStatus("current")
_TmnxMobProfPgwChrgId_Type = TmnxMobChargingProfile
_TmnxMobProfPgwChrgId_Object = MibTableColumn
tmnxMobProfPgwChrgId = _TmnxMobProfPgwChrgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 1),
    _TmnxMobProfPgwChrgId_Type()
)
tmnxMobProfPgwChrgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgId.setStatus("current")
_TmnxMobProfPgwChrgRowStatus_Type = RowStatus
_TmnxMobProfPgwChrgRowStatus_Object = MibTableColumn
tmnxMobProfPgwChrgRowStatus = _TmnxMobProfPgwChrgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 2),
    _TmnxMobProfPgwChrgRowStatus_Type()
)
tmnxMobProfPgwChrgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgRowStatus.setStatus("current")
_TmnxMobProfPgwChrgLastChanged_Type = TimeStamp
_TmnxMobProfPgwChrgLastChanged_Object = MibTableColumn
tmnxMobProfPgwChrgLastChanged = _TmnxMobProfPgwChrgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 3),
    _TmnxMobProfPgwChrgLastChanged_Type()
)
tmnxMobProfPgwChrgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgLastChanged.setStatus("current")


class _TmnxMobProfPgwChrgDesc_Type(TItemDescription):
    """Custom type tmnxMobProfPgwChrgDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfPgwChrgDesc_Object = MibTableColumn
tmnxMobProfPgwChrgDesc = _TmnxMobProfPgwChrgDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 4),
    _TmnxMobProfPgwChrgDesc_Type()
)
tmnxMobProfPgwChrgDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgDesc.setStatus("current")


class _TmnxMobProfPgwChrgOffLineState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgOffLineState based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgOffLineState_Object = MibTableColumn
tmnxMobProfPgwChrgOffLineState = _TmnxMobProfPgwChrgOffLineState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 5),
    _TmnxMobProfPgwChrgOffLineState_Type()
)
tmnxMobProfPgwChrgOffLineState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgOffLineState.setStatus("current")


class _TmnxMobProfPgwChrgPriCdfDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfPgwChrgPriCdfDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPgwChrgPriCdfDiaPeer_Object = MibTableColumn
tmnxMobProfPgwChrgPriCdfDiaPeer = _TmnxMobProfPgwChrgPriCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 6),
    _TmnxMobProfPgwChrgPriCdfDiaPeer_Type()
)
tmnxMobProfPgwChrgPriCdfDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPriCdfDiaPeer.setStatus("current")


class _TmnxMobProfPgwChrgSecCdfDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfPgwChrgSecCdfDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPgwChrgSecCdfDiaPeer_Object = MibTableColumn
tmnxMobProfPgwChrgSecCdfDiaPeer = _TmnxMobProfPgwChrgSecCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 7),
    _TmnxMobProfPgwChrgSecCdfDiaPeer_Type()
)
tmnxMobProfPgwChrgSecCdfDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgSecCdfDiaPeer.setStatus("current")


class _TmnxMobProfPgwChrgCitQosChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgCitQosChange based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgCitQosChange_Object = MibTableColumn
tmnxMobProfPgwChrgCitQosChange = _TmnxMobProfPgwChrgCitQosChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 8),
    _TmnxMobProfPgwChrgCitQosChange_Type()
)
tmnxMobProfPgwChrgCitQosChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitQosChange.setStatus("current")


class _TmnxMobProfPgwChrgCitUsrLocChnge_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgCitUsrLocChnge based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgCitUsrLocChnge_Object = MibTableColumn
tmnxMobProfPgwChrgCitUsrLocChnge = _TmnxMobProfPgwChrgCitUsrLocChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 9),
    _TmnxMobProfPgwChrgCitUsrLocChnge_Type()
)
tmnxMobProfPgwChrgCitUsrLocChnge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitUsrLocChnge.setStatus("current")


class _TmnxMobProfPgwChrgCitTrfTimeChng_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgCitTrfTimeChng based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgCitTrfTimeChng_Object = MibTableColumn
tmnxMobProfPgwChrgCitTrfTimeChng = _TmnxMobProfPgwChrgCitTrfTimeChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 10),
    _TmnxMobProfPgwChrgCitTrfTimeChng_Type()
)
tmnxMobProfPgwChrgCitTrfTimeChng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTrfTimeChng.setStatus("current")


class _TmnxMobProfPgwChrgCitTrfTmStart_Type(TmnxTimeInSec):
    """Custom type tmnxMobProfPgwChrgCitTrfTmStart based on TmnxTimeInSec"""
    defaultValue = 0


_TmnxMobProfPgwChrgCitTrfTmStart_Object = MibTableColumn
tmnxMobProfPgwChrgCitTrfTmStart = _TmnxMobProfPgwChrgCitTrfTmStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 11),
    _TmnxMobProfPgwChrgCitTrfTmStart_Type()
)
tmnxMobProfPgwChrgCitTrfTmStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTrfTmStart.setStatus("current")


class _TmnxMobProfPgwChrgCitTrfTmEnd_Type(TmnxTimeInSec):
    """Custom type tmnxMobProfPgwChrgCitTrfTmEnd based on TmnxTimeInSec"""
    defaultValue = 0


_TmnxMobProfPgwChrgCitTrfTmEnd_Object = MibTableColumn
tmnxMobProfPgwChrgCitTrfTmEnd = _TmnxMobProfPgwChrgCitTrfTmEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 12),
    _TmnxMobProfPgwChrgCitTrfTmEnd_Type()
)
tmnxMobProfPgwChrgCitTrfTmEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTrfTmEnd.setStatus("current")


class _TmnxMobProfPgwChrgCitSgwChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgCitSgwChange based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgCitSgwChange_Object = MibTableColumn
tmnxMobProfPgwChrgCitSgwChange = _TmnxMobProfPgwChrgCitSgwChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 13),
    _TmnxMobProfPgwChrgCitSgwChange_Type()
)
tmnxMobProfPgwChrgCitSgwChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitSgwChange.setStatus("current")


class _TmnxMobProfPgwChrgCitTimeLmtRg_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgCitTimeLmtRg based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxMobProfPgwChrgCitTimeLmtRg_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgCitTimeLmtRg_Object = MibTableColumn
tmnxMobProfPgwChrgCitTimeLmtRg = _TmnxMobProfPgwChrgCitTimeLmtRg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 16),
    _TmnxMobProfPgwChrgCitTimeLmtRg_Type()
)
tmnxMobProfPgwChrgCitTimeLmtRg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTimeLmtRg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTimeLmtRg.setUnits("seconds")


class _TmnxMobProfPgwChrgCitVolumeLmtRg_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgCitVolumeLmtRg based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_TmnxMobProfPgwChrgCitVolumeLmtRg_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgCitVolumeLmtRg_Object = MibTableColumn
tmnxMobProfPgwChrgCitVolumeLmtRg = _TmnxMobProfPgwChrgCitVolumeLmtRg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 17),
    _TmnxMobProfPgwChrgCitVolumeLmtRg_Type()
)
tmnxMobProfPgwChrgCitVolumeLmtRg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitVolumeLmtRg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitVolumeLmtRg.setUnits("kbytes")


class _TmnxMobProfPgwChrgCitTermServDf_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgCitTermServDf based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgCitTermServDf_Object = MibTableColumn
tmnxMobProfPgwChrgCitTermServDf = _TmnxMobProfPgwChrgCitTermServDf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 18),
    _TmnxMobProfPgwChrgCitTermServDf_Type()
)
tmnxMobProfPgwChrgCitTermServDf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgCitTermServDf.setStatus("current")


class _TmnxMobProfPgwChrgPrctTimeLmt_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgPrctTimeLmt based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxMobProfPgwChrgPrctTimeLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgPrctTimeLmt_Object = MibTableColumn
tmnxMobProfPgwChrgPrctTimeLmt = _TmnxMobProfPgwChrgPrctTimeLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 19),
    _TmnxMobProfPgwChrgPrctTimeLmt_Type()
)
tmnxMobProfPgwChrgPrctTimeLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctTimeLmt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctTimeLmt.setUnits("seconds")


class _TmnxMobProfPgwChrgPrctVolumeLmt_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgPrctVolumeLmt based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMobProfPgwChrgPrctVolumeLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgPrctVolumeLmt_Object = MibTableColumn
tmnxMobProfPgwChrgPrctVolumeLmt = _TmnxMobProfPgwChrgPrctVolumeLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 20),
    _TmnxMobProfPgwChrgPrctVolumeLmt_Type()
)
tmnxMobProfPgwChrgPrctVolumeLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctVolumeLmt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctVolumeLmt.setUnits("kbytes")


class _TmnxMobProfPgwChrgPrctMaxChCond_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgPrctMaxChCond based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxMobProfPgwChrgPrctMaxChCond_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgPrctMaxChCond_Object = MibTableColumn
tmnxMobProfPgwChrgPrctMaxChCond = _TmnxMobProfPgwChrgPrctMaxChCond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 21),
    _TmnxMobProfPgwChrgPrctMaxChCond_Type()
)
tmnxMobProfPgwChrgPrctMaxChCond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctMaxChCond.setStatus("current")


class _TmnxMobProfPgwChrgPrctMsTmzChnge_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgPrctMsTmzChnge based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgPrctMsTmzChnge_Object = MibTableColumn
tmnxMobProfPgwChrgPrctMsTmzChnge = _TmnxMobProfPgwChrgPrctMsTmzChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 22),
    _TmnxMobProfPgwChrgPrctMsTmzChnge_Type()
)
tmnxMobProfPgwChrgPrctMsTmzChnge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctMsTmzChnge.setStatus("current")


class _TmnxMobProfPgwChrgPrctPlmnChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgPrctPlmnChange based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgPrctPlmnChange_Object = MibTableColumn
tmnxMobProfPgwChrgPrctPlmnChange = _TmnxMobProfPgwChrgPrctPlmnChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 23),
    _TmnxMobProfPgwChrgPrctPlmnChange_Type()
)
tmnxMobProfPgwChrgPrctPlmnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctPlmnChange.setStatus("current")


class _TmnxMobProfPgwChrgPrctRatChange_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgPrctRatChange based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgPrctRatChange_Object = MibTableColumn
tmnxMobProfPgwChrgPrctRatChange = _TmnxMobProfPgwChrgPrctRatChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 24),
    _TmnxMobProfPgwChrgPrctRatChange_Type()
)
tmnxMobProfPgwChrgPrctRatChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctRatChange.setStatus("current")


class _TmnxMobProfPgwChrgGyState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfPgwChrgGyState based on TmnxEnabledDisabled"""


_TmnxMobProfPgwChrgGyState_Object = MibTableColumn
tmnxMobProfPgwChrgGyState = _TmnxMobProfPgwChrgGyState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 25),
    _TmnxMobProfPgwChrgGyState_Type()
)
tmnxMobProfPgwChrgGyState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgGyState.setStatus("current")


class _TmnxMobProfPgwGyPriOcsDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfPgwGyPriOcsDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPgwGyPriOcsDiaPeer_Object = MibTableColumn
tmnxMobProfPgwGyPriOcsDiaPeer = _TmnxMobProfPgwGyPriOcsDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 26),
    _TmnxMobProfPgwGyPriOcsDiaPeer_Type()
)
tmnxMobProfPgwGyPriOcsDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwGyPriOcsDiaPeer.setStatus("current")


class _TmnxMobProfPgwGySecOcsDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfPgwGySecOcsDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPgwGySecOcsDiaPeer_Object = MibTableColumn
tmnxMobProfPgwGySecOcsDiaPeer = _TmnxMobProfPgwGySecOcsDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 27),
    _TmnxMobProfPgwGySecOcsDiaPeer_Type()
)
tmnxMobProfPgwGySecOcsDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwGySecOcsDiaPeer.setStatus("current")


class _TmnxMobProfPgwGyDccaProf_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfPgwGyDccaProf based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfPgwGyDccaProf_Object = MibTableColumn
tmnxMobProfPgwGyDccaProf = _TmnxMobProfPgwGyDccaProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 28),
    _TmnxMobProfPgwGyDccaProf_Type()
)
tmnxMobProfPgwGyDccaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwGyDccaProf.setStatus("current")


class _TmnxMobProfPgwChrgPrctSrvNdChLmt_Type(Unsigned32):
    """Custom type tmnxMobProfPgwChrgPrctSrvNdChLmt based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxMobProfPgwChrgPrctSrvNdChLmt_Type.__name__ = "Unsigned32"
_TmnxMobProfPgwChrgPrctSrvNdChLmt_Object = MibTableColumn
tmnxMobProfPgwChrgPrctSrvNdChLmt = _TmnxMobProfPgwChrgPrctSrvNdChLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 16, 1, 29),
    _TmnxMobProfPgwChrgPrctSrvNdChLmt_Type()
)
tmnxMobProfPgwChrgPrctSrvNdChLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChrgPrctSrvNdChLmt.setStatus("current")
_TmnxMobGtpPriGrpTable_Object = MibTable
tmnxMobGtpPriGrpTable = _TmnxMobGtpPriGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpTable.setStatus("current")
_TmnxMobGtpPriGrpEntry_Object = MibTableRow
tmnxMobGtpPriGrpEntry = _TmnxMobGtpPriGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1)
)
tmnxMobGtpPriGrpEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
)
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpEntry.setStatus("current")
_TmnxMobGtpPriGrpName_Type = TmnxMobProfName
_TmnxMobGtpPriGrpName_Object = MibTableColumn
tmnxMobGtpPriGrpName = _TmnxMobGtpPriGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 1),
    _TmnxMobGtpPriGrpName_Type()
)
tmnxMobGtpPriGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpName.setStatus("current")
_TmnxMobGtpPriGrpRowStatus_Type = RowStatus
_TmnxMobGtpPriGrpRowStatus_Object = MibTableColumn
tmnxMobGtpPriGrpRowStatus = _TmnxMobGtpPriGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 2),
    _TmnxMobGtpPriGrpRowStatus_Type()
)
tmnxMobGtpPriGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpRowStatus.setStatus("current")
_TmnxMobGtpPriGrpLastChanged_Type = TimeStamp
_TmnxMobGtpPriGrpLastChanged_Object = MibTableColumn
tmnxMobGtpPriGrpLastChanged = _TmnxMobGtpPriGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 3),
    _TmnxMobGtpPriGrpLastChanged_Type()
)
tmnxMobGtpPriGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpLastChanged.setStatus("current")


class _TmnxMobGtpPriGrpDescription_Type(TItemDescription):
    """Custom type tmnxMobGtpPriGrpDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobGtpPriGrpDescription_Object = MibTableColumn
tmnxMobGtpPriGrpDescription = _TmnxMobGtpPriGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 4),
    _TmnxMobGtpPriGrpDescription_Type()
)
tmnxMobGtpPriGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpDescription.setStatus("current")


class _TmnxMobGtpPriGrpMaxCdrsPerPdu_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpMaxCdrsPerPdu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobGtpPriGrpMaxCdrsPerPdu_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpMaxCdrsPerPdu_Object = MibTableColumn
tmnxMobGtpPriGrpMaxCdrsPerPdu = _TmnxMobGtpPriGrpMaxCdrsPerPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 5),
    _TmnxMobGtpPriGrpMaxCdrsPerPdu_Type()
)
tmnxMobGtpPriGrpMaxCdrsPerPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpMaxCdrsPerPdu.setStatus("current")


class _TmnxMobGtpPriGrpDeadtime_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpDeadtime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxMobGtpPriGrpDeadtime_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpDeadtime_Object = MibTableColumn
tmnxMobGtpPriGrpDeadtime = _TmnxMobGtpPriGrpDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 6),
    _TmnxMobGtpPriGrpDeadtime_Type()
)
tmnxMobGtpPriGrpDeadtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpDeadtime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpDeadtime.setUnits("seconds")


class _TmnxMobGtpPriGrpRedirection_Type(TruthValue):
    """Custom type tmnxMobGtpPriGrpRedirection based on TruthValue"""


_TmnxMobGtpPriGrpRedirection_Object = MibTableColumn
tmnxMobGtpPriGrpRedirection = _TmnxMobGtpPriGrpRedirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 7),
    _TmnxMobGtpPriGrpRedirection_Type()
)
tmnxMobGtpPriGrpRedirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpRedirection.setStatus("current")


class _TmnxMobGtpPriGrpIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobGtpPriGrpIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobGtpPriGrpIfVRtrId_Object = MibTableColumn
tmnxMobGtpPriGrpIfVRtrId = _TmnxMobGtpPriGrpIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 8),
    _TmnxMobGtpPriGrpIfVRtrId_Type()
)
tmnxMobGtpPriGrpIfVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpIfVRtrId.setStatus("current")


class _TmnxMobGtpPriGrpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobGtpPriGrpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobGtpPriGrpIfIndex_Object = MibTableColumn
tmnxMobGtpPriGrpIfIndex = _TmnxMobGtpPriGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 9),
    _TmnxMobGtpPriGrpIfIndex_Type()
)
tmnxMobGtpPriGrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpIfIndex.setStatus("current")


class _TmnxMobGtpPriGrpLocalCdrStorage_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobGtpPriGrpLocalCdrStorage based on TmnxEnabledDisabled"""


_TmnxMobGtpPriGrpLocalCdrStorage_Object = MibTableColumn
tmnxMobGtpPriGrpLocalCdrStorage = _TmnxMobGtpPriGrpLocalCdrStorage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 10),
    _TmnxMobGtpPriGrpLocalCdrStorage_Type()
)
tmnxMobGtpPriGrpLocalCdrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpLocalCdrStorage.setStatus("current")


class _TmnxMobGtpPriGrpFilePrivateInfo_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobGtpPriGrpFilePrivateInfo based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobGtpPriGrpFilePrivateInfo_Object = MibTableColumn
tmnxMobGtpPriGrpFilePrivateInfo = _TmnxMobGtpPriGrpFilePrivateInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 11),
    _TmnxMobGtpPriGrpFilePrivateInfo_Type()
)
tmnxMobGtpPriGrpFilePrivateInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFilePrivateInfo.setStatus("current")


class _TmnxMobGtpPriGrpFileExtension_Type(DisplayString):
    """Custom type tmnxMobGtpPriGrpFileExtension based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxMobGtpPriGrpFileExtension_Type.__name__ = "DisplayString"
_TmnxMobGtpPriGrpFileExtension_Object = MibTableColumn
tmnxMobGtpPriGrpFileExtension = _TmnxMobGtpPriGrpFileExtension_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 12),
    _TmnxMobGtpPriGrpFileExtension_Type()
)
tmnxMobGtpPriGrpFileExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileExtension.setStatus("current")


class _TmnxMobGtpPriGrpFileClosureSize_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpFileClosureSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMobGtpPriGrpFileClosureSize_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpFileClosureSize_Object = MibTableColumn
tmnxMobGtpPriGrpFileClosureSize = _TmnxMobGtpPriGrpFileClosureSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 13),
    _TmnxMobGtpPriGrpFileClosureSize_Type()
)
tmnxMobGtpPriGrpFileClosureSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileClosureSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileClosureSize.setUnits("megabytes")


class _TmnxMobGtpPriGrpFileClsLifeTime_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpFileClsLifeTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxMobGtpPriGrpFileClsLifeTime_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpFileClsLifeTime_Object = MibTableColumn
tmnxMobGtpPriGrpFileClsLifeTime = _TmnxMobGtpPriGrpFileClsLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 14),
    _TmnxMobGtpPriGrpFileClsLifeTime_Type()
)
tmnxMobGtpPriGrpFileClsLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileClsLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileClsLifeTime.setUnits("hours")


class _TmnxMobGtpPriGrpFileClsMaxRecs_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpFileClsMaxRecs based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 75000),
    )


_TmnxMobGtpPriGrpFileClsMaxRecs_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpFileClsMaxRecs_Object = MibTableColumn
tmnxMobGtpPriGrpFileClsMaxRecs = _TmnxMobGtpPriGrpFileClsMaxRecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 15),
    _TmnxMobGtpPriGrpFileClsMaxRecs_Type()
)
tmnxMobGtpPriGrpFileClsMaxRecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileClsMaxRecs.setStatus("current")


class _TmnxMobGtpPriGrpFileObsoleteTime_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpFileObsoleteTime based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxMobGtpPriGrpFileObsoleteTime_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpFileObsoleteTime_Object = MibTableColumn
tmnxMobGtpPriGrpFileObsoleteTime = _TmnxMobGtpPriGrpFileObsoleteTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 16),
    _TmnxMobGtpPriGrpFileObsoleteTime_Type()
)
tmnxMobGtpPriGrpFileObsoleteTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileObsoleteTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpFileObsoleteTime.setUnits("days")


class _TmnxMobGtpPriGrpPrimaryCf_Type(Integer32):
    """Custom type tmnxMobGtpPriGrpPrimaryCf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cf1", 1),
          ("cf2", 2))
    )


_TmnxMobGtpPriGrpPrimaryCf_Type.__name__ = "Integer32"
_TmnxMobGtpPriGrpPrimaryCf_Object = MibTableColumn
tmnxMobGtpPriGrpPrimaryCf = _TmnxMobGtpPriGrpPrimaryCf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 17),
    _TmnxMobGtpPriGrpPrimaryCf_Type()
)
tmnxMobGtpPriGrpPrimaryCf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpPrimaryCf.setStatus("current")


class _TmnxMobGtpPriGrpCf1State_Type(TruthValue):
    """Custom type tmnxMobGtpPriGrpCf1State based on TruthValue"""


_TmnxMobGtpPriGrpCf1State_Object = MibTableColumn
tmnxMobGtpPriGrpCf1State = _TmnxMobGtpPriGrpCf1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 18),
    _TmnxMobGtpPriGrpCf1State_Type()
)
tmnxMobGtpPriGrpCf1State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf1State.setStatus("current")


class _TmnxMobGtpPriGrpCf1Limit_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpCf1Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobGtpPriGrpCf1Limit_Object = MibTableColumn
tmnxMobGtpPriGrpCf1Limit = _TmnxMobGtpPriGrpCf1Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 19),
    _TmnxMobGtpPriGrpCf1Limit_Type()
)
tmnxMobGtpPriGrpCf1Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf1Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf1Limit.setUnits("megabytes")


class _TmnxMobGtpPriGrpCf2State_Type(TruthValue):
    """Custom type tmnxMobGtpPriGrpCf2State based on TruthValue"""


_TmnxMobGtpPriGrpCf2State_Object = MibTableColumn
tmnxMobGtpPriGrpCf2State = _TmnxMobGtpPriGrpCf2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 20),
    _TmnxMobGtpPriGrpCf2State_Type()
)
tmnxMobGtpPriGrpCf2State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf2State.setStatus("current")


class _TmnxMobGtpPriGrpCf2Limit_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpCf2Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobGtpPriGrpCf2Limit_Object = MibTableColumn
tmnxMobGtpPriGrpCf2Limit = _TmnxMobGtpPriGrpCf2Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 21),
    _TmnxMobGtpPriGrpCf2Limit_Type()
)
tmnxMobGtpPriGrpCf2Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf2Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCf2Limit.setUnits("megabytes")


class _TmnxMobGtpPriGrpCpmMemoryState_Type(TruthValue):
    """Custom type tmnxMobGtpPriGrpCpmMemoryState based on TruthValue"""


_TmnxMobGtpPriGrpCpmMemoryState_Object = MibTableColumn
tmnxMobGtpPriGrpCpmMemoryState = _TmnxMobGtpPriGrpCpmMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 22),
    _TmnxMobGtpPriGrpCpmMemoryState_Type()
)
tmnxMobGtpPriGrpCpmMemoryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpCpmMemoryState.setStatus("current")


class _TmnxMobGtpPriGrpQueueSize_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpQueueSize based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 500000),
    )


_TmnxMobGtpPriGrpQueueSize_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpQueueSize_Object = MibTableColumn
tmnxMobGtpPriGrpQueueSize = _TmnxMobGtpPriGrpQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 23),
    _TmnxMobGtpPriGrpQueueSize_Type()
)
tmnxMobGtpPriGrpQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpQueueSize.setStatus("current")


class _TmnxMobGtpPriGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobGtpPriGrpAdminState based on TmnxAdminState"""


_TmnxMobGtpPriGrpAdminState_Object = MibTableColumn
tmnxMobGtpPriGrpAdminState = _TmnxMobGtpPriGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 24),
    _TmnxMobGtpPriGrpAdminState_Type()
)
tmnxMobGtpPriGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpAdminState.setStatus("current")


class _TmnxMobGtpPriGrpInactiveTimer_Type(Unsigned32):
    """Custom type tmnxMobGtpPriGrpInactiveTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxMobGtpPriGrpInactiveTimer_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriGrpInactiveTimer_Object = MibTableColumn
tmnxMobGtpPriGrpInactiveTimer = _TmnxMobGtpPriGrpInactiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 17, 1, 25),
    _TmnxMobGtpPriGrpInactiveTimer_Type()
)
tmnxMobGtpPriGrpInactiveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpInactiveTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpInactiveTimer.setUnits("minutes")
_TmnxMobGtpPriServerTable_Object = MibTable
tmnxMobGtpPriServerTable = _TmnxMobGtpPriServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerTable.setStatus("current")
_TmnxMobGtpPriServerEntry_Object = MibTableRow
tmnxMobGtpPriServerEntry = _TmnxMobGtpPriServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1)
)
tmnxMobGtpPriServerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerIndex"),
)
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerEntry.setStatus("current")
_TmnxMobGtpPriServerIndex_Type = Unsigned32
_TmnxMobGtpPriServerIndex_Object = MibTableColumn
tmnxMobGtpPriServerIndex = _TmnxMobGtpPriServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 1),
    _TmnxMobGtpPriServerIndex_Type()
)
tmnxMobGtpPriServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerIndex.setStatus("current")
_TmnxMobGtpPriServerRowStatus_Type = RowStatus
_TmnxMobGtpPriServerRowStatus_Object = MibTableColumn
tmnxMobGtpPriServerRowStatus = _TmnxMobGtpPriServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 2),
    _TmnxMobGtpPriServerRowStatus_Type()
)
tmnxMobGtpPriServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerRowStatus.setStatus("current")
_TmnxMobGtpPriServerLastChngd_Type = TimeStamp
_TmnxMobGtpPriServerLastChngd_Object = MibTableColumn
tmnxMobGtpPriServerLastChngd = _TmnxMobGtpPriServerLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 3),
    _TmnxMobGtpPriServerLastChngd_Type()
)
tmnxMobGtpPriServerLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerLastChngd.setStatus("current")


class _TmnxMobGtpPriServerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobGtpPriServerAdminState based on TmnxAdminState"""


_TmnxMobGtpPriServerAdminState_Object = MibTableColumn
tmnxMobGtpPriServerAdminState = _TmnxMobGtpPriServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 4),
    _TmnxMobGtpPriServerAdminState_Type()
)
tmnxMobGtpPriServerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerAdminState.setStatus("current")
_TmnxMobGtpPriServerAddrType_Type = InetAddressType
_TmnxMobGtpPriServerAddrType_Object = MibTableColumn
tmnxMobGtpPriServerAddrType = _TmnxMobGtpPriServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 5),
    _TmnxMobGtpPriServerAddrType_Type()
)
tmnxMobGtpPriServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerAddrType.setStatus("current")


class _TmnxMobGtpPriServerAddr_Type(InetAddress):
    """Custom type tmnxMobGtpPriServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobGtpPriServerAddr_Type.__name__ = "InetAddress"
_TmnxMobGtpPriServerAddr_Object = MibTableColumn
tmnxMobGtpPriServerAddr = _TmnxMobGtpPriServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 6),
    _TmnxMobGtpPriServerAddr_Type()
)
tmnxMobGtpPriServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerAddr.setStatus("current")


class _TmnxMobGtpPriServerPort_Type(InetPortNumber):
    """Custom type tmnxMobGtpPriServerPort based on InetPortNumber"""
    defaultValue = 3386


_TmnxMobGtpPriServerPort_Object = MibTableColumn
tmnxMobGtpPriServerPort = _TmnxMobGtpPriServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 7),
    _TmnxMobGtpPriServerPort_Type()
)
tmnxMobGtpPriServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerPort.setStatus("current")


class _TmnxMobGtpPriServerRetries_Type(Unsigned32):
    """Custom type tmnxMobGtpPriServerRetries based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobGtpPriServerRetries_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriServerRetries_Object = MibTableColumn
tmnxMobGtpPriServerRetries = _TmnxMobGtpPriServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 8),
    _TmnxMobGtpPriServerRetries_Type()
)
tmnxMobGtpPriServerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerRetries.setStatus("current")


class _TmnxMobGtpPriServerTimeout_Type(Unsigned32):
    """Custom type tmnxMobGtpPriServerTimeout based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TmnxMobGtpPriServerTimeout_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriServerTimeout_Object = MibTableColumn
tmnxMobGtpPriServerTimeout = _TmnxMobGtpPriServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 9),
    _TmnxMobGtpPriServerTimeout_Type()
)
tmnxMobGtpPriServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerTimeout.setUnits("seconds")


class _TmnxMobGtpPriServerEchoInterval_Type(Unsigned32):
    """Custom type tmnxMobGtpPriServerEchoInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxMobGtpPriServerEchoInterval_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriServerEchoInterval_Object = MibTableColumn
tmnxMobGtpPriServerEchoInterval = _TmnxMobGtpPriServerEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 10),
    _TmnxMobGtpPriServerEchoInterval_Type()
)
tmnxMobGtpPriServerEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerEchoInterval.setUnits("seconds")


class _TmnxMobGtpPriServerMaxRequests_Type(Unsigned32):
    """Custom type tmnxMobGtpPriServerMaxRequests based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TmnxMobGtpPriServerMaxRequests_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriServerMaxRequests_Object = MibTableColumn
tmnxMobGtpPriServerMaxRequests = _TmnxMobGtpPriServerMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 11),
    _TmnxMobGtpPriServerMaxRequests_Type()
)
tmnxMobGtpPriServerMaxRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerMaxRequests.setStatus("current")


class _TmnxMobGtpPriServerNodeAlive_Type(TruthValue):
    """Custom type tmnxMobGtpPriServerNodeAlive based on TruthValue"""


_TmnxMobGtpPriServerNodeAlive_Object = MibTableColumn
tmnxMobGtpPriServerNodeAlive = _TmnxMobGtpPriServerNodeAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 12),
    _TmnxMobGtpPriServerNodeAlive_Type()
)
tmnxMobGtpPriServerNodeAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerNodeAlive.setStatus("current")


class _TmnxMobGtpPriServerPriority_Type(Unsigned32):
    """Custom type tmnxMobGtpPriServerPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobGtpPriServerPriority_Type.__name__ = "Unsigned32"
_TmnxMobGtpPriServerPriority_Object = MibTableColumn
tmnxMobGtpPriServerPriority = _TmnxMobGtpPriServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 13),
    _TmnxMobGtpPriServerPriority_Type()
)
tmnxMobGtpPriServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerPriority.setStatus("current")


class _TmnxMobGtpPriServerPathProtocol_Type(Integer32):
    """Custom type tmnxMobGtpPriServerPathProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_TmnxMobGtpPriServerPathProtocol_Type.__name__ = "Integer32"
_TmnxMobGtpPriServerPathProtocol_Object = MibTableColumn
tmnxMobGtpPriServerPathProtocol = _TmnxMobGtpPriServerPathProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 18, 1, 14),
    _TmnxMobGtpPriServerPathProtocol_Type()
)
tmnxMobGtpPriServerPathProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerPathProtocol.setStatus("current")
_TmnxMobUmtsQosPolTable_Object = MibTable
tmnxMobUmtsQosPolTable = _TmnxMobUmtsQosPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolTable.setStatus("current")
_TmnxMobUmtsQosPolEntry_Object = MibTableRow
tmnxMobUmtsQosPolEntry = _TmnxMobUmtsQosPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1)
)
tmnxMobUmtsQosPolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolName"),
)
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolEntry.setStatus("current")
_TmnxMobUmtsQosPolName_Type = TmnxMobProfName
_TmnxMobUmtsQosPolName_Object = MibTableColumn
tmnxMobUmtsQosPolName = _TmnxMobUmtsQosPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 1),
    _TmnxMobUmtsQosPolName_Type()
)
tmnxMobUmtsQosPolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolName.setStatus("current")
_TmnxMobUmtsQosPolRowStatus_Type = RowStatus
_TmnxMobUmtsQosPolRowStatus_Object = MibTableColumn
tmnxMobUmtsQosPolRowStatus = _TmnxMobUmtsQosPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 2),
    _TmnxMobUmtsQosPolRowStatus_Type()
)
tmnxMobUmtsQosPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolRowStatus.setStatus("current")
_TmnxMobUmtsQosPolLastChanged_Type = TimeStamp
_TmnxMobUmtsQosPolLastChanged_Object = MibTableColumn
tmnxMobUmtsQosPolLastChanged = _TmnxMobUmtsQosPolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 3),
    _TmnxMobUmtsQosPolLastChanged_Type()
)
tmnxMobUmtsQosPolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolLastChanged.setStatus("current")


class _TmnxMobUmtsQosPolConvSpeechQci_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolConvSpeechQci based on TmnxMobQciValue"""
    defaultValue = 1


_TmnxMobUmtsQosPolConvSpeechQci_Object = MibTableColumn
tmnxMobUmtsQosPolConvSpeechQci = _TmnxMobUmtsQosPolConvSpeechQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 4),
    _TmnxMobUmtsQosPolConvSpeechQci_Type()
)
tmnxMobUmtsQosPolConvSpeechQci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolConvSpeechQci.setStatus("current")


class _TmnxMobUmtsQosPolConvUnkTdg_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolConvUnkTdg based on TmnxMobQciValue"""
    defaultValue = 2


_TmnxMobUmtsQosPolConvUnkTdg_Object = MibTableColumn
tmnxMobUmtsQosPolConvUnkTdg = _TmnxMobUmtsQosPolConvUnkTdg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 5),
    _TmnxMobUmtsQosPolConvUnkTdg_Type()
)
tmnxMobUmtsQosPolConvUnkTdg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolConvUnkTdg.setStatus("current")


class _TmnxMobUmtsQosPolConvUnkTdl_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolConvUnkTdl based on TmnxMobQciValue"""
    defaultValue = 3


_TmnxMobUmtsQosPolConvUnkTdl_Object = MibTableColumn
tmnxMobUmtsQosPolConvUnkTdl = _TmnxMobUmtsQosPolConvUnkTdl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 6),
    _TmnxMobUmtsQosPolConvUnkTdl_Type()
)
tmnxMobUmtsQosPolConvUnkTdl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolConvUnkTdl.setStatus("current")


class _TmnxMobUmtsQosPolStreamQciValue_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolStreamQciValue based on TmnxMobQciValue"""
    defaultValue = 4


_TmnxMobUmtsQosPolStreamQciValue_Object = MibTableColumn
tmnxMobUmtsQosPolStreamQciValue = _TmnxMobUmtsQosPolStreamQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 7),
    _TmnxMobUmtsQosPolStreamQciValue_Type()
)
tmnxMobUmtsQosPolStreamQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolStreamQciValue.setStatus("current")


class _TmnxMobUmtsQosPolInterSigP1Qci_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolInterSigP1Qci based on TmnxMobQciValue"""
    defaultValue = 5


_TmnxMobUmtsQosPolInterSigP1Qci_Object = MibTableColumn
tmnxMobUmtsQosPolInterSigP1Qci = _TmnxMobUmtsQosPolInterSigP1Qci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 8),
    _TmnxMobUmtsQosPolInterSigP1Qci_Type()
)
tmnxMobUmtsQosPolInterSigP1Qci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolInterSigP1Qci.setStatus("current")


class _TmnxMobUmtsQosPolInterP1Qci_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolInterP1Qci based on TmnxMobQciValue"""
    defaultValue = 6


_TmnxMobUmtsQosPolInterP1Qci_Object = MibTableColumn
tmnxMobUmtsQosPolInterP1Qci = _TmnxMobUmtsQosPolInterP1Qci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 9),
    _TmnxMobUmtsQosPolInterP1Qci_Type()
)
tmnxMobUmtsQosPolInterP1Qci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolInterP1Qci.setStatus("current")


class _TmnxMobUmtsQosPolInterP2Qci_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolInterP2Qci based on TmnxMobQciValue"""
    defaultValue = 7


_TmnxMobUmtsQosPolInterP2Qci_Object = MibTableColumn
tmnxMobUmtsQosPolInterP2Qci = _TmnxMobUmtsQosPolInterP2Qci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 10),
    _TmnxMobUmtsQosPolInterP2Qci_Type()
)
tmnxMobUmtsQosPolInterP2Qci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolInterP2Qci.setStatus("current")


class _TmnxMobUmtsQosPolInterP3Qci_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolInterP3Qci based on TmnxMobQciValue"""
    defaultValue = 8


_TmnxMobUmtsQosPolInterP3Qci_Object = MibTableColumn
tmnxMobUmtsQosPolInterP3Qci = _TmnxMobUmtsQosPolInterP3Qci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 11),
    _TmnxMobUmtsQosPolInterP3Qci_Type()
)
tmnxMobUmtsQosPolInterP3Qci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolInterP3Qci.setStatus("current")


class _TmnxMobUmtsQosPolBackground_Type(TmnxMobQciValue):
    """Custom type tmnxMobUmtsQosPolBackground based on TmnxMobQciValue"""
    defaultValue = 9


_TmnxMobUmtsQosPolBackground_Object = MibTableColumn
tmnxMobUmtsQosPolBackground = _TmnxMobUmtsQosPolBackground_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 19, 1, 12),
    _TmnxMobUmtsQosPolBackground_Type()
)
tmnxMobUmtsQosPolBackground.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolBackground.setStatus("current")
_TmnxMobProfRadTable_Object = MibTable
tmnxMobProfRadTable = _TmnxMobProfRadTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxMobProfRadTable.setStatus("current")
_TmnxMobProfRadEntry_Object = MibTableRow
tmnxMobProfRadEntry = _TmnxMobProfRadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1)
)
tmnxMobProfRadEntry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfRadEntry.setStatus("current")
_TmnxMobProfRadName_Type = TmnxMobProfName
_TmnxMobProfRadName_Object = MibTableColumn
tmnxMobProfRadName = _TmnxMobProfRadName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 1),
    _TmnxMobProfRadName_Type()
)
tmnxMobProfRadName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfRadName.setStatus("current")
_TmnxMobProfRadRowStatus_Type = RowStatus
_TmnxMobProfRadRowStatus_Object = MibTableColumn
tmnxMobProfRadRowStatus = _TmnxMobProfRadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 2),
    _TmnxMobProfRadRowStatus_Type()
)
tmnxMobProfRadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadRowStatus.setStatus("current")
_TmnxMobProfRadLastChanged_Type = TimeStamp
_TmnxMobProfRadLastChanged_Object = MibTableColumn
tmnxMobProfRadLastChanged = _TmnxMobProfRadLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 3),
    _TmnxMobProfRadLastChanged_Type()
)
tmnxMobProfRadLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadLastChanged.setStatus("current")


class _TmnxMobProfRadDescription_Type(TItemDescription):
    """Custom type tmnxMobProfRadDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfRadDescription_Object = MibTableColumn
tmnxMobProfRadDescription = _TmnxMobProfRadDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 4),
    _TmnxMobProfRadDescription_Type()
)
tmnxMobProfRadDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadDescription.setStatus("current")


class _TmnxMobProfRadAuthProbeInt_Type(Unsigned32):
    """Custom type tmnxMobProfRadAuthProbeInt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 600),
    )


_TmnxMobProfRadAuthProbeInt_Type.__name__ = "Unsigned32"
_TmnxMobProfRadAuthProbeInt_Object = MibTableColumn
tmnxMobProfRadAuthProbeInt = _TmnxMobProfRadAuthProbeInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 5),
    _TmnxMobProfRadAuthProbeInt_Type()
)
tmnxMobProfRadAuthProbeInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadAuthProbeInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfRadAuthProbeInt.setUnits("seconds")


class _TmnxMobProfRadServerDeadTime_Type(Unsigned32):
    """Custom type tmnxMobProfRadServerDeadTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_TmnxMobProfRadServerDeadTime_Type.__name__ = "Unsigned32"
_TmnxMobProfRadServerDeadTime_Object = MibTableColumn
tmnxMobProfRadServerDeadTime = _TmnxMobProfRadServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 6),
    _TmnxMobProfRadServerDeadTime_Type()
)
tmnxMobProfRadServerDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadServerDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfRadServerDeadTime.setUnits("seconds")


class _TmnxMobProfRadRetryTimeout_Type(Unsigned32):
    """Custom type tmnxMobProfRadRetryTimeout based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TmnxMobProfRadRetryTimeout_Type.__name__ = "Unsigned32"
_TmnxMobProfRadRetryTimeout_Object = MibTableColumn
tmnxMobProfRadRetryTimeout = _TmnxMobProfRadRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 7),
    _TmnxMobProfRadRetryTimeout_Type()
)
tmnxMobProfRadRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfRadRetryTimeout.setUnits("seconds")


class _TmnxMobProfRadRetryCount_Type(Unsigned32):
    """Custom type tmnxMobProfRadRetryCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobProfRadRetryCount_Type.__name__ = "Unsigned32"
_TmnxMobProfRadRetryCount_Object = MibTableColumn
tmnxMobProfRadRetryCount = _TmnxMobProfRadRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 20, 1, 8),
    _TmnxMobProfRadRetryCount_Type()
)
tmnxMobProfRadRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadRetryCount.setStatus("current")
_TmnxMobProfRadGrpTable_Object = MibTable
tmnxMobProfRadGrpTable = _TmnxMobProfRadGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpTable.setStatus("current")
_TmnxMobProfRadGrpEntry_Object = MibTableRow
tmnxMobProfRadGrpEntry = _TmnxMobProfRadGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1)
)
tmnxMobProfRadGrpEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpEntry.setStatus("current")
_TmnxMobProfRadGrpName_Type = TmnxMobProfName
_TmnxMobProfRadGrpName_Object = MibTableColumn
tmnxMobProfRadGrpName = _TmnxMobProfRadGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 1),
    _TmnxMobProfRadGrpName_Type()
)
tmnxMobProfRadGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpName.setStatus("current")
_TmnxMobProfRadGrpRowStatus_Type = RowStatus
_TmnxMobProfRadGrpRowStatus_Object = MibTableColumn
tmnxMobProfRadGrpRowStatus = _TmnxMobProfRadGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 2),
    _TmnxMobProfRadGrpRowStatus_Type()
)
tmnxMobProfRadGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpRowStatus.setStatus("current")
_TmnxMobProfRadGrpLastChanged_Type = TimeStamp
_TmnxMobProfRadGrpLastChanged_Object = MibTableColumn
tmnxMobProfRadGrpLastChanged = _TmnxMobProfRadGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 3),
    _TmnxMobProfRadGrpLastChanged_Type()
)
tmnxMobProfRadGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpLastChanged.setStatus("current")


class _TmnxMobProfRadGrpDescription_Type(TItemDescription):
    """Custom type tmnxMobProfRadGrpDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfRadGrpDescription_Object = MibTableColumn
tmnxMobProfRadGrpDescription = _TmnxMobProfRadGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 4),
    _TmnxMobProfRadGrpDescription_Type()
)
tmnxMobProfRadGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpDescription.setStatus("current")


class _TmnxMobProfRadGrpIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobProfRadGrpIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobProfRadGrpIfVRtrId_Object = MibTableColumn
tmnxMobProfRadGrpIfVRtrId = _TmnxMobProfRadGrpIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 5),
    _TmnxMobProfRadGrpIfVRtrId_Type()
)
tmnxMobProfRadGrpIfVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpIfVRtrId.setStatus("current")


class _TmnxMobProfRadGrpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobProfRadGrpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobProfRadGrpIfIndex_Object = MibTableColumn
tmnxMobProfRadGrpIfIndex = _TmnxMobProfRadGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 6),
    _TmnxMobProfRadGrpIfIndex_Type()
)
tmnxMobProfRadGrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpIfIndex.setStatus("current")


class _TmnxMobProfRadGrpAuthServerPort_Type(InetPortNumber):
    """Custom type tmnxMobProfRadGrpAuthServerPort based on InetPortNumber"""
    defaultValue = 1812


_TmnxMobProfRadGrpAuthServerPort_Object = MibTableColumn
tmnxMobProfRadGrpAuthServerPort = _TmnxMobProfRadGrpAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 7),
    _TmnxMobProfRadGrpAuthServerPort_Type()
)
tmnxMobProfRadGrpAuthServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpAuthServerPort.setStatus("current")


class _TmnxMobProfRadGrpAcctServerPort_Type(InetPortNumber):
    """Custom type tmnxMobProfRadGrpAcctServerPort based on InetPortNumber"""
    defaultValue = 1813


_TmnxMobProfRadGrpAcctServerPort_Object = MibTableColumn
tmnxMobProfRadGrpAcctServerPort = _TmnxMobProfRadGrpAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 8),
    _TmnxMobProfRadGrpAcctServerPort_Type()
)
tmnxMobProfRadGrpAcctServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpAcctServerPort.setStatus("current")


class _TmnxMobProfRadGrpSecret_Type(OctetString):
    """Custom type tmnxMobProfRadGrpSecret based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobProfRadGrpSecret_Type.__name__ = "OctetString"
_TmnxMobProfRadGrpSecret_Object = MibTableColumn
tmnxMobProfRadGrpSecret = _TmnxMobProfRadGrpSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 9),
    _TmnxMobProfRadGrpSecret_Type()
)
tmnxMobProfRadGrpSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpSecret.setStatus("current")


class _TmnxMobProfRadGrpIntUpdateIntvl_Type(Unsigned32):
    """Custom type tmnxMobProfRadGrpIntUpdateIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 1440),
    )


_TmnxMobProfRadGrpIntUpdateIntvl_Type.__name__ = "Unsigned32"
_TmnxMobProfRadGrpIntUpdateIntvl_Object = MibTableColumn
tmnxMobProfRadGrpIntUpdateIntvl = _TmnxMobProfRadGrpIntUpdateIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 10),
    _TmnxMobProfRadGrpIntUpdateIntvl_Type()
)
tmnxMobProfRadGrpIntUpdateIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpIntUpdateIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpIntUpdateIntvl.setUnits("minutes")


class _TmnxMobProfRadGrpServerType_Type(Integer32):
    """Custom type tmnxMobProfRadGrpServerType based on Integer32"""
    defaultValue = 0

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
        *(("acct", 2),
          ("auth", 1),
          ("both", 3),
          ("none", 0))
    )


_TmnxMobProfRadGrpServerType_Type.__name__ = "Integer32"
_TmnxMobProfRadGrpServerType_Object = MibTableColumn
tmnxMobProfRadGrpServerType = _TmnxMobProfRadGrpServerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 11),
    _TmnxMobProfRadGrpServerType_Type()
)
tmnxMobProfRadGrpServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpServerType.setStatus("current")


class _TmnxMobProfRadGrpRadiusProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfRadGrpRadiusProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfRadGrpRadiusProfile_Object = MibTableColumn
tmnxMobProfRadGrpRadiusProfile = _TmnxMobProfRadGrpRadiusProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 12),
    _TmnxMobProfRadGrpRadiusProfile_Type()
)
tmnxMobProfRadGrpRadiusProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpRadiusProfile.setStatus("current")


class _TmnxMobProfRadGrpIgnAcctResp_Type(TruthValue):
    """Custom type tmnxMobProfRadGrpIgnAcctResp based on TruthValue"""


_TmnxMobProfRadGrpIgnAcctResp_Object = MibTableColumn
tmnxMobProfRadGrpIgnAcctResp = _TmnxMobProfRadGrpIgnAcctResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 21, 1, 13),
    _TmnxMobProfRadGrpIgnAcctResp_Type()
)
tmnxMobProfRadGrpIgnAcctResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpIgnAcctResp.setStatus("current")
_TmnxMobProfRadPeerTable_Object = MibTable
tmnxMobProfRadPeerTable = _TmnxMobProfRadPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22)
)
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerTable.setStatus("current")
_TmnxMobProfRadPeerEntry_Object = MibTableRow
tmnxMobProfRadPeerEntry = _TmnxMobProfRadPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1)
)
tmnxMobProfRadPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerIndex"),
)
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerEntry.setStatus("current")
_TmnxMobProfRadPeerIndex_Type = Unsigned32
_TmnxMobProfRadPeerIndex_Object = MibTableColumn
tmnxMobProfRadPeerIndex = _TmnxMobProfRadPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 1),
    _TmnxMobProfRadPeerIndex_Type()
)
tmnxMobProfRadPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerIndex.setStatus("current")
_TmnxMobProfRadPeerRowStatus_Type = RowStatus
_TmnxMobProfRadPeerRowStatus_Object = MibTableColumn
tmnxMobProfRadPeerRowStatus = _TmnxMobProfRadPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 2),
    _TmnxMobProfRadPeerRowStatus_Type()
)
tmnxMobProfRadPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerRowStatus.setStatus("current")
_TmnxMobProfRadPeerLastChngd_Type = TimeStamp
_TmnxMobProfRadPeerLastChngd_Object = MibTableColumn
tmnxMobProfRadPeerLastChngd = _TmnxMobProfRadPeerLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 3),
    _TmnxMobProfRadPeerLastChngd_Type()
)
tmnxMobProfRadPeerLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerLastChngd.setStatus("current")


class _TmnxMobProfRadPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobProfRadPeerAdminState based on TmnxAdminState"""


_TmnxMobProfRadPeerAdminState_Object = MibTableColumn
tmnxMobProfRadPeerAdminState = _TmnxMobProfRadPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 4),
    _TmnxMobProfRadPeerAdminState_Type()
)
tmnxMobProfRadPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerAdminState.setStatus("current")


class _TmnxMobProfRadPeerAddrType_Type(InetAddressType):
    """Custom type tmnxMobProfRadPeerAddrType based on InetAddressType"""


_TmnxMobProfRadPeerAddrType_Object = MibTableColumn
tmnxMobProfRadPeerAddrType = _TmnxMobProfRadPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 5),
    _TmnxMobProfRadPeerAddrType_Type()
)
tmnxMobProfRadPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerAddrType.setStatus("current")


class _TmnxMobProfRadPeerAddr_Type(InetAddress):
    """Custom type tmnxMobProfRadPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobProfRadPeerAddr_Type.__name__ = "InetAddress"
_TmnxMobProfRadPeerAddr_Object = MibTableColumn
tmnxMobProfRadPeerAddr = _TmnxMobProfRadPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 6),
    _TmnxMobProfRadPeerAddr_Type()
)
tmnxMobProfRadPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerAddr.setStatus("current")


class _TmnxMobProfRadPeerPriority_Type(Unsigned32):
    """Custom type tmnxMobProfRadPeerPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxMobProfRadPeerPriority_Type.__name__ = "Unsigned32"
_TmnxMobProfRadPeerPriority_Object = MibTableColumn
tmnxMobProfRadPeerPriority = _TmnxMobProfRadPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 7),
    _TmnxMobProfRadPeerPriority_Type()
)
tmnxMobProfRadPeerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerPriority.setStatus("current")


class _TmnxMobProfRadPeerAuthSvrPort_Type(InetPortNumber):
    """Custom type tmnxMobProfRadPeerAuthSvrPort based on InetPortNumber"""
    defaultValue = 0


_TmnxMobProfRadPeerAuthSvrPort_Object = MibTableColumn
tmnxMobProfRadPeerAuthSvrPort = _TmnxMobProfRadPeerAuthSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 8),
    _TmnxMobProfRadPeerAuthSvrPort_Type()
)
tmnxMobProfRadPeerAuthSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerAuthSvrPort.setStatus("current")


class _TmnxMobProfRadPeerAcctSvrPort_Type(InetPortNumber):
    """Custom type tmnxMobProfRadPeerAcctSvrPort based on InetPortNumber"""
    defaultValue = 0


_TmnxMobProfRadPeerAcctSvrPort_Object = MibTableColumn
tmnxMobProfRadPeerAcctSvrPort = _TmnxMobProfRadPeerAcctSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 9),
    _TmnxMobProfRadPeerAcctSvrPort_Type()
)
tmnxMobProfRadPeerAcctSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerAcctSvrPort.setStatus("current")


class _TmnxMobProfRadPeerSecret_Type(OctetString):
    """Custom type tmnxMobProfRadPeerSecret based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobProfRadPeerSecret_Type.__name__ = "OctetString"
_TmnxMobProfRadPeerSecret_Object = MibTableColumn
tmnxMobProfRadPeerSecret = _TmnxMobProfRadPeerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 10),
    _TmnxMobProfRadPeerSecret_Type()
)
tmnxMobProfRadPeerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerSecret.setStatus("current")


class _TmnxMobProfRadPeerRadProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobProfRadPeerRadProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobProfRadPeerRadProfile_Object = MibTableColumn
tmnxMobProfRadPeerRadProfile = _TmnxMobProfRadPeerRadProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 22, 1, 11),
    _TmnxMobProfRadPeerRadProfile_Type()
)
tmnxMobProfRadPeerRadProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerRadProfile.setStatus("current")
_TmnxMobProfDccaTable_Object = MibTable
tmnxMobProfDccaTable = _TmnxMobProfDccaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxMobProfDccaTable.setStatus("current")
_TmnxMobProfDccaEntry_Object = MibTableRow
tmnxMobProfDccaEntry = _TmnxMobProfDccaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1)
)
tmnxMobProfDccaEntry.setIndexNames(
    (1, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfDccaEntry.setStatus("current")
_TmnxMobProfDccaName_Type = TmnxMobProfName
_TmnxMobProfDccaName_Object = MibTableColumn
tmnxMobProfDccaName = _TmnxMobProfDccaName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 1),
    _TmnxMobProfDccaName_Type()
)
tmnxMobProfDccaName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfDccaName.setStatus("current")
_TmnxMobProfDccaRowStatus_Type = RowStatus
_TmnxMobProfDccaRowStatus_Object = MibTableColumn
tmnxMobProfDccaRowStatus = _TmnxMobProfDccaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 2),
    _TmnxMobProfDccaRowStatus_Type()
)
tmnxMobProfDccaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaRowStatus.setStatus("current")
_TmnxMobProfDccaLastChanged_Type = TimeStamp
_TmnxMobProfDccaLastChanged_Object = MibTableColumn
tmnxMobProfDccaLastChanged = _TmnxMobProfDccaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 3),
    _TmnxMobProfDccaLastChanged_Type()
)
tmnxMobProfDccaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDccaLastChanged.setStatus("current")


class _TmnxMobProfDccaDescription_Type(TItemDescription):
    """Custom type tmnxMobProfDccaDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobProfDccaDescription_Object = MibTableColumn
tmnxMobProfDccaDescription = _TmnxMobProfDccaDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 4),
    _TmnxMobProfDccaDescription_Type()
)
tmnxMobProfDccaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaDescription.setStatus("current")


class _TmnxMobProfDccaApplTxTimer_Type(Unsigned32):
    """Custom type tmnxMobProfDccaApplTxTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxMobProfDccaApplTxTimer_Type.__name__ = "Unsigned32"
_TmnxMobProfDccaApplTxTimer_Object = MibTableColumn
tmnxMobProfDccaApplTxTimer = _TmnxMobProfDccaApplTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 5),
    _TmnxMobProfDccaApplTxTimer_Type()
)
tmnxMobProfDccaApplTxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaApplTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDccaApplTxTimer.setUnits("seconds")


class _TmnxMobProfDccaRetryCnt_Type(Unsigned32):
    """Custom type tmnxMobProfDccaRetryCnt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxMobProfDccaRetryCnt_Type.__name__ = "Unsigned32"
_TmnxMobProfDccaRetryCnt_Object = MibTableColumn
tmnxMobProfDccaRetryCnt = _TmnxMobProfDccaRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 6),
    _TmnxMobProfDccaRetryCnt_Type()
)
tmnxMobProfDccaRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaRetryCnt.setStatus("current")


class _TmnxMobProfDcca3GppQosNegProf_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfDcca3GppQosNegProf based on TmnxEnabledDisabled"""


_TmnxMobProfDcca3GppQosNegProf_Object = MibTableColumn
tmnxMobProfDcca3GppQosNegProf = _TmnxMobProfDcca3GppQosNegProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 7),
    _TmnxMobProfDcca3GppQosNegProf_Type()
)
tmnxMobProfDcca3GppQosNegProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDcca3GppQosNegProf.setStatus("current")


class _TmnxMobProfDccaQosInformation_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfDccaQosInformation based on TmnxEnabledDisabled"""


_TmnxMobProfDccaQosInformation_Object = MibTableColumn
tmnxMobProfDccaQosInformation = _TmnxMobProfDccaQosInformation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 8),
    _TmnxMobProfDccaQosInformation_Type()
)
tmnxMobProfDccaQosInformation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaQosInformation.setStatus("current")


class _TmnxMobProfDccaCalledStationId_Type(Integer32):
    """Custom type tmnxMobProfDccaCalledStationId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("real", 1),
          ("virtual", 2))
    )


_TmnxMobProfDccaCalledStationId_Type.__name__ = "Integer32"
_TmnxMobProfDccaCalledStationId_Object = MibTableColumn
tmnxMobProfDccaCalledStationId = _TmnxMobProfDccaCalledStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 9),
    _TmnxMobProfDccaCalledStationId_Type()
)
tmnxMobProfDccaCalledStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaCalledStationId.setStatus("current")


class _TmnxMobProfDccaCcSessFailover_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfDccaCcSessFailover based on TmnxEnabledDisabled"""


_TmnxMobProfDccaCcSessFailover_Object = MibTableColumn
tmnxMobProfDccaCcSessFailover = _TmnxMobProfDccaCcSessFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 10),
    _TmnxMobProfDccaCcSessFailover_Type()
)
tmnxMobProfDccaCcSessFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaCcSessFailover.setStatus("current")


class _TmnxMobProfDccaCcSessFlovrHndl_Type(Integer32):
    """Custom type tmnxMobProfDccaCcSessFlovrHndl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("retryAndTerm", 3),
          ("terminate", 1))
    )


_TmnxMobProfDccaCcSessFlovrHndl_Type.__name__ = "Integer32"
_TmnxMobProfDccaCcSessFlovrHndl_Object = MibTableColumn
tmnxMobProfDccaCcSessFlovrHndl = _TmnxMobProfDccaCcSessFlovrHndl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 11),
    _TmnxMobProfDccaCcSessFlovrHndl_Type()
)
tmnxMobProfDccaCcSessFlovrHndl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaCcSessFlovrHndl.setStatus("current")


class _TmnxMobProfDccaForcedReAuth_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaForcedReAuth based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaForcedReAuth_Object = MibTableColumn
tmnxMobProfDccaForcedReAuth = _TmnxMobProfDccaForcedReAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 12),
    _TmnxMobProfDccaForcedReAuth_Type()
)
tmnxMobProfDccaForcedReAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaForcedReAuth.setStatus("current")


class _TmnxMobProfDccaQuotaExNoThrsld_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaQuotaExNoThrsld based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaQuotaExNoThrsld_Object = MibTableColumn
tmnxMobProfDccaQuotaExNoThrsld = _TmnxMobProfDccaQuotaExNoThrsld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 13),
    _TmnxMobProfDccaQuotaExNoThrsld_Type()
)
tmnxMobProfDccaQuotaExNoThrsld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaQuotaExNoThrsld.setStatus("current")


class _TmnxMobProfDccaQuotaExThrsldAct_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaQuotaExThrsldAct based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaQuotaExThrsldAct_Object = MibTableColumn
tmnxMobProfDccaQuotaExThrsldAct = _TmnxMobProfDccaQuotaExThrsldAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 14),
    _TmnxMobProfDccaQuotaExThrsldAct_Type()
)
tmnxMobProfDccaQuotaExThrsldAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaQuotaExThrsldAct.setStatus("current")


class _TmnxMobProfDccaQuotaUnavail_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaQuotaUnavail based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaQuotaUnavail_Object = MibTableColumn
tmnxMobProfDccaQuotaUnavail = _TmnxMobProfDccaQuotaUnavail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 15),
    _TmnxMobProfDccaQuotaUnavail_Type()
)
tmnxMobProfDccaQuotaUnavail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaQuotaUnavail.setStatus("current")


class _TmnxMobProfDccaRatingCondtChng_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaRatingCondtChng based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaRatingCondtChng_Object = MibTableColumn
tmnxMobProfDccaRatingCondtChng = _TmnxMobProfDccaRatingCondtChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 16),
    _TmnxMobProfDccaRatingCondtChng_Type()
)
tmnxMobProfDccaRatingCondtChng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaRatingCondtChng.setStatus("current")


class _TmnxMobProfDccaValidityTimeExp_Type(TmnxMobProfAllowDiscard):
    """Custom type tmnxMobProfDccaValidityTimeExp based on TmnxMobProfAllowDiscard"""


_TmnxMobProfDccaValidityTimeExp_Object = MibTableColumn
tmnxMobProfDccaValidityTimeExp = _TmnxMobProfDccaValidityTimeExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 17),
    _TmnxMobProfDccaValidityTimeExp_Type()
)
tmnxMobProfDccaValidityTimeExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaValidityTimeExp.setStatus("current")


class _TmnxMobProfDccaFhSessContTimer_Type(Unsigned32):
    """Custom type tmnxMobProfDccaFhSessContTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TmnxMobProfDccaFhSessContTimer_Type.__name__ = "Unsigned32"
_TmnxMobProfDccaFhSessContTimer_Object = MibTableColumn
tmnxMobProfDccaFhSessContTimer = _TmnxMobProfDccaFhSessContTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 18),
    _TmnxMobProfDccaFhSessContTimer_Type()
)
tmnxMobProfDccaFhSessContTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaFhSessContTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDccaFhSessContTimer.setUnits("minutes")


class _TmnxMobProfDccaDefaultQht_Type(Unsigned32):
    """Custom type tmnxMobProfDccaDefaultQht based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxMobProfDccaDefaultQht_Type.__name__ = "Unsigned32"
_TmnxMobProfDccaDefaultQht_Object = MibTableColumn
tmnxMobProfDccaDefaultQht = _TmnxMobProfDccaDefaultQht_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 19),
    _TmnxMobProfDccaDefaultQht_Type()
)
tmnxMobProfDccaDefaultQht.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaDefaultQht.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfDccaDefaultQht.setUnits("minutes")


class _TmnxMobProfDccaFirstPktBehavior_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobProfDccaFirstPktBehavior based on TmnxEnabledDisabled"""


_TmnxMobProfDccaFirstPktBehavior_Object = MibTableColumn
tmnxMobProfDccaFirstPktBehavior = _TmnxMobProfDccaFirstPktBehavior_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 23, 1, 20),
    _TmnxMobProfDccaFirstPktBehavior_Type()
)
tmnxMobProfDccaFirstPktBehavior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfDccaFirstPktBehavior.setStatus("current")
_TmnxMobProfPolUnitTable_Object = MibTable
tmnxMobProfPolUnitTable = _TmnxMobProfPolUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitTable.setStatus("current")
_TmnxMobProfPolUnitEntry_Object = MibTableRow
tmnxMobProfPolUnitEntry = _TmnxMobProfPolUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1)
)
tmnxMobProfPolUnitEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitEntry.setStatus("current")
_TmnxMobProfPolUnitName_Type = TmnxMobProfName
_TmnxMobProfPolUnitName_Object = MibTableColumn
tmnxMobProfPolUnitName = _TmnxMobProfPolUnitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 1),
    _TmnxMobProfPolUnitName_Type()
)
tmnxMobProfPolUnitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitName.setStatus("current")
_TmnxMobProfPolUnitRowStatus_Type = RowStatus
_TmnxMobProfPolUnitRowStatus_Object = MibTableColumn
tmnxMobProfPolUnitRowStatus = _TmnxMobProfPolUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 2),
    _TmnxMobProfPolUnitRowStatus_Type()
)
tmnxMobProfPolUnitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitRowStatus.setStatus("current")
_TmnxMobProfPolUnitLastChanged_Type = TimeStamp
_TmnxMobProfPolUnitLastChanged_Object = MibTableColumn
tmnxMobProfPolUnitLastChanged = _TmnxMobProfPolUnitLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 3),
    _TmnxMobProfPolUnitLastChanged_Type()
)
tmnxMobProfPolUnitLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitLastChanged.setStatus("current")


class _TmnxMobProfPolUnitUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxMobProfPolUnitUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxMobProfPolUnitUplinkGbrRate_Object = MibTableColumn
tmnxMobProfPolUnitUplinkGbrRate = _TmnxMobProfPolUnitUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 4),
    _TmnxMobProfPolUnitUplinkGbrRate_Type()
)
tmnxMobProfPolUnitUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitUplinkGbrRate.setUnits("kbps")


class _TmnxMobProfPolUnitUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxMobProfPolUnitUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxMobProfPolUnitUplinkMbrRate_Object = MibTableColumn
tmnxMobProfPolUnitUplinkMbrRate = _TmnxMobProfPolUnitUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 5),
    _TmnxMobProfPolUnitUplinkMbrRate_Type()
)
tmnxMobProfPolUnitUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitUplinkMbrRate.setUnits("kbps")


class _TmnxMobProfPolUnitDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxMobProfPolUnitDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxMobProfPolUnitDwnlinkGbrRate_Object = MibTableColumn
tmnxMobProfPolUnitDwnlinkGbrRate = _TmnxMobProfPolUnitDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 6),
    _TmnxMobProfPolUnitDwnlinkGbrRate_Type()
)
tmnxMobProfPolUnitDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitDwnlinkGbrRate.setUnits("kbps")


class _TmnxMobProfPolUnitDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxMobProfPolUnitDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxMobProfPolUnitDwnlinkMbrRate_Object = MibTableColumn
tmnxMobProfPolUnitDwnlinkMbrRate = _TmnxMobProfPolUnitDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 7),
    _TmnxMobProfPolUnitDwnlinkMbrRate_Type()
)
tmnxMobProfPolUnitDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitDwnlinkMbrRate.setUnits("kbps")


class _TmnxMobProfPolUntFlwGateStatus_Type(Integer32):
    """Custom type tmnxMobProfPolUntFlwGateStatus based on Integer32"""
    defaultValue = 3

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
        *(("allow", 3),
          ("allowDL", 2),
          ("allowUL", 1),
          ("autoRedirect", 5),
          ("drop", 4),
          ("redirect", 6))
    )


_TmnxMobProfPolUntFlwGateStatus_Type.__name__ = "Integer32"
_TmnxMobProfPolUntFlwGateStatus_Object = MibTableColumn
tmnxMobProfPolUntFlwGateStatus = _TmnxMobProfPolUntFlwGateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 8),
    _TmnxMobProfPolUntFlwGateStatus_Type()
)
tmnxMobProfPolUntFlwGateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlwGateStatus.setStatus("current")


class _TmnxMobProfPolUntRedirectAdrType_Type(InetAddressType):
    """Custom type tmnxMobProfPolUntRedirectAdrType based on InetAddressType"""


_TmnxMobProfPolUntRedirectAdrType_Object = MibTableColumn
tmnxMobProfPolUntRedirectAdrType = _TmnxMobProfPolUntRedirectAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 9),
    _TmnxMobProfPolUntRedirectAdrType_Type()
)
tmnxMobProfPolUntRedirectAdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntRedirectAdrType.setStatus("current")


class _TmnxMobProfPolUntRedirectAddr_Type(InetAddress):
    """Custom type tmnxMobProfPolUntRedirectAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxMobProfPolUntRedirectAddr_Type.__name__ = "InetAddress"
_TmnxMobProfPolUntRedirectAddr_Object = MibTableColumn
tmnxMobProfPolUntRedirectAddr = _TmnxMobProfPolUntRedirectAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 10),
    _TmnxMobProfPolUntRedirectAddr_Type()
)
tmnxMobProfPolUntRedirectAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntRedirectAddr.setStatus("current")


class _TmnxMobProfPolUntInUse_Type(TruthValue):
    """Custom type tmnxMobProfPolUntInUse based on TruthValue"""


_TmnxMobProfPolUntInUse_Object = MibTableColumn
tmnxMobProfPolUntInUse = _TmnxMobProfPolUntInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 11),
    _TmnxMobProfPolUntInUse_Type()
)
tmnxMobProfPolUntInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntInUse.setStatus("current")
_TmnxMobProfPolUntRefCount_Type = Counter32
_TmnxMobProfPolUntRefCount_Object = MibTableColumn
tmnxMobProfPolUntRefCount = _TmnxMobProfPolUntRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 24, 1, 12),
    _TmnxMobProfPolUntRefCount_Type()
)
tmnxMobProfPolUntRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntRefCount.setStatus("current")
_TmnxMobProfChgUnitTable_Object = MibTable
tmnxMobProfChgUnitTable = _TmnxMobProfChgUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitTable.setStatus("current")
_TmnxMobProfChgUnitEntry_Object = MibTableRow
tmnxMobProfChgUnitEntry = _TmnxMobProfChgUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1)
)
tmnxMobProfChgUnitEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitEntry.setStatus("current")
_TmnxMobProfChgUnitName_Type = TmnxMobProfName
_TmnxMobProfChgUnitName_Object = MibTableColumn
tmnxMobProfChgUnitName = _TmnxMobProfChgUnitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 1),
    _TmnxMobProfChgUnitName_Type()
)
tmnxMobProfChgUnitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitName.setStatus("current")
_TmnxMobProfChgUnitRowStatus_Type = RowStatus
_TmnxMobProfChgUnitRowStatus_Object = MibTableColumn
tmnxMobProfChgUnitRowStatus = _TmnxMobProfChgUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 2),
    _TmnxMobProfChgUnitRowStatus_Type()
)
tmnxMobProfChgUnitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitRowStatus.setStatus("current")
_TmnxMobProfChgUnitLastChanged_Type = TimeStamp
_TmnxMobProfChgUnitLastChanged_Object = MibTableColumn
tmnxMobProfChgUnitLastChanged = _TmnxMobProfChgUnitLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 3),
    _TmnxMobProfChgUnitLastChanged_Type()
)
tmnxMobProfChgUnitLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitLastChanged.setStatus("current")


class _TmnxMobProfChgUnitRatingGroup_Type(Unsigned32):
    """Custom type tmnxMobProfChgUnitRatingGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxMobProfChgUnitRatingGroup_Type.__name__ = "Unsigned32"
_TmnxMobProfChgUnitRatingGroup_Object = MibTableColumn
tmnxMobProfChgUnitRatingGroup = _TmnxMobProfChgUnitRatingGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 4),
    _TmnxMobProfChgUnitRatingGroup_Type()
)
tmnxMobProfChgUnitRatingGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitRatingGroup.setStatus("current")


class _TmnxMobProfChgUnitServIdentifier_Type(Unsigned32):
    """Custom type tmnxMobProfChgUnitServIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxMobProfChgUnitServIdentifier_Type.__name__ = "Unsigned32"
_TmnxMobProfChgUnitServIdentifier_Object = MibTableColumn
tmnxMobProfChgUnitServIdentifier = _TmnxMobProfChgUnitServIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 5),
    _TmnxMobProfChgUnitServIdentifier_Type()
)
tmnxMobProfChgUnitServIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitServIdentifier.setStatus("current")


class _TmnxMobProfChgUnitReportingLevel_Type(TmnxMobProfPolReportingLevel):
    """Custom type tmnxMobProfChgUnitReportingLevel based on TmnxMobProfPolReportingLevel"""


_TmnxMobProfChgUnitReportingLevel_Object = MibTableColumn
tmnxMobProfChgUnitReportingLevel = _TmnxMobProfChgUnitReportingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 6),
    _TmnxMobProfChgUnitReportingLevel_Type()
)
tmnxMobProfChgUnitReportingLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitReportingLevel.setStatus("current")


class _TmnxMobProfChgUnitChargingMethod_Type(TmnxMobProfPolChargingMethod):
    """Custom type tmnxMobProfChgUnitChargingMethod based on TmnxMobProfPolChargingMethod"""


_TmnxMobProfChgUnitChargingMethod_Object = MibTableColumn
tmnxMobProfChgUnitChargingMethod = _TmnxMobProfChgUnitChargingMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 7),
    _TmnxMobProfChgUnitChargingMethod_Type()
)
tmnxMobProfChgUnitChargingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitChargingMethod.setStatus("current")


class _TmnxMobProfChgUnitMeteringMethod_Type(TmnxMobProfPolMeteringMethod):
    """Custom type tmnxMobProfChgUnitMeteringMethod based on TmnxMobProfPolMeteringMethod"""


_TmnxMobProfChgUnitMeteringMethod_Object = MibTableColumn
tmnxMobProfChgUnitMeteringMethod = _TmnxMobProfChgUnitMeteringMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 8),
    _TmnxMobProfChgUnitMeteringMethod_Type()
)
tmnxMobProfChgUnitMeteringMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitMeteringMethod.setStatus("current")


class _TmnxMobProfChgUnitInUse_Type(TruthValue):
    """Custom type tmnxMobProfChgUnitInUse based on TruthValue"""


_TmnxMobProfChgUnitInUse_Object = MibTableColumn
tmnxMobProfChgUnitInUse = _TmnxMobProfChgUnitInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 9),
    _TmnxMobProfChgUnitInUse_Type()
)
tmnxMobProfChgUnitInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitInUse.setStatus("current")
_TmnxMobProfChgUnitRefCount_Type = Counter32
_TmnxMobProfChgUnitRefCount_Object = MibTableColumn
tmnxMobProfChgUnitRefCount = _TmnxMobProfChgUnitRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 25, 1, 10),
    _TmnxMobProfChgUnitRefCount_Type()
)
tmnxMobProfChgUnitRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitRefCount.setStatus("current")
_TmnxMobProfHTTPRedirectTable_Object = MibTable
tmnxMobProfHTTPRedirectTable = _TmnxMobProfHTTPRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26)
)
if mibBuilder.loadTexts:
    tmnxMobProfHTTPRedirectTable.setStatus("current")
_TmnxMobProfHTTPRedirectEntry_Object = MibTableRow
tmnxMobProfHTTPRedirectEntry = _TmnxMobProfHTTPRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26, 1)
)
tmnxMobProfHTTPRedirectEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfHttpRedirectName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitName"),
)
if mibBuilder.loadTexts:
    tmnxMobProfHTTPRedirectEntry.setStatus("current")
_TmnxMobProfHttpRedirectName_Type = TmnxMobProfName
_TmnxMobProfHttpRedirectName_Object = MibTableColumn
tmnxMobProfHttpRedirectName = _TmnxMobProfHttpRedirectName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26, 1, 1),
    _TmnxMobProfHttpRedirectName_Type()
)
tmnxMobProfHttpRedirectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobProfHttpRedirectName.setStatus("current")
_TmnxMobProfHttpRedirectRowStatus_Type = RowStatus
_TmnxMobProfHttpRedirectRowStatus_Object = MibTableColumn
tmnxMobProfHttpRedirectRowStatus = _TmnxMobProfHttpRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26, 1, 2),
    _TmnxMobProfHttpRedirectRowStatus_Type()
)
tmnxMobProfHttpRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfHttpRedirectRowStatus.setStatus("current")
_TmnxMobProfHttpRedirectLstChgd_Type = TimeStamp
_TmnxMobProfHttpRedirectLstChgd_Object = MibTableColumn
tmnxMobProfHttpRedirectLstChgd = _TmnxMobProfHttpRedirectLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26, 1, 3),
    _TmnxMobProfHttpRedirectLstChgd_Type()
)
tmnxMobProfHttpRedirectLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfHttpRedirectLstChgd.setStatus("current")


class _TmnxMobProfHttpRedirctPrecedence_Type(TmnxMobStaticPolPrecedenceOrZero):
    """Custom type tmnxMobProfHttpRedirctPrecedence based on TmnxMobStaticPolPrecedenceOrZero"""
    defaultValue = 0


_TmnxMobProfHttpRedirctPrecedence_Object = MibTableColumn
tmnxMobProfHttpRedirctPrecedence = _TmnxMobProfHttpRedirctPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 1, 26, 1, 4),
    _TmnxMobProfHttpRedirctPrecedence_Type()
)
tmnxMobProfHttpRedirctPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobProfHttpRedirctPrecedence.setStatus("current")
_TmnxMobProfileGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxMobProfileGlobalObjs = _TmnxMobProfileGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2)
)
_TmnxMobProfSysTblLstChgd_Type = TimeStamp
_TmnxMobProfSysTblLstChgd_Object = MibScalar
tmnxMobProfSysTblLstChgd = _TmnxMobProfSysTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 1),
    _TmnxMobProfSysTblLstChgd_Type()
)
tmnxMobProfSysTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfSysTblLstChgd.setStatus("current")
_TmnxMobProfDiaTblLstChgd_Type = TimeStamp
_TmnxMobProfDiaTblLstChgd_Object = MibScalar
tmnxMobProfDiaTblLstChgd = _TmnxMobProfDiaTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 2),
    _TmnxMobProfDiaTblLstChgd_Type()
)
tmnxMobProfDiaTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaTblLstChgd.setStatus("current")
_TmnxMobProfDiaPeerTblLstChgd_Type = TimeStamp
_TmnxMobProfDiaPeerTblLstChgd_Object = MibScalar
tmnxMobProfDiaPeerTblLstChgd = _TmnxMobProfDiaPeerTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 3),
    _TmnxMobProfDiaPeerTblLstChgd_Type()
)
tmnxMobProfDiaPeerTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerTblLstChgd.setStatus("current")
_TmnxMobProfDiaPeerListTblLstChgd_Type = TimeStamp
_TmnxMobProfDiaPeerListTblLstChgd_Object = MibScalar
tmnxMobProfDiaPeerListTblLstChgd = _TmnxMobProfDiaPeerListTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 4),
    _TmnxMobProfDiaPeerListTblLstChgd_Type()
)
tmnxMobProfDiaPeerListTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDiaPeerListTblLstChgd.setStatus("current")
_TmnxMobProfPmipv6TblLstChgd_Type = TimeStamp
_TmnxMobProfPmipv6TblLstChgd_Object = MibScalar
tmnxMobProfPmipv6TblLstChgd = _TmnxMobProfPmipv6TblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 5),
    _TmnxMobProfPmipv6TblLstChgd_Type()
)
tmnxMobProfPmipv6TblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6TblLstChgd.setStatus("current")
_TmnxMobProfGtpTblLstChgd_Type = TimeStamp
_TmnxMobProfGtpTblLstChgd_Object = MibScalar
tmnxMobProfGtpTblLstChgd = _TmnxMobProfGtpTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 6),
    _TmnxMobProfGtpTblLstChgd_Type()
)
tmnxMobProfGtpTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfGtpTblLstChgd.setStatus("current")
_TmnxMobProfPlmnListTblLstChgd_Type = TimeStamp
_TmnxMobProfPlmnListTblLstChgd_Object = MibScalar
tmnxMobProfPlmnListTblLstChgd = _TmnxMobProfPlmnListTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 7),
    _TmnxMobProfPlmnListTblLstChgd_Type()
)
tmnxMobProfPlmnListTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPlmnListTblLstChgd.setStatus("current")
_TmnxMobProfPolTblLstChgd_Type = TimeStamp
_TmnxMobProfPolTblLstChgd_Object = MibScalar
tmnxMobProfPolTblLstChgd = _TmnxMobProfPolTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 8),
    _TmnxMobProfPolTblLstChgd_Type()
)
tmnxMobProfPolTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolTblLstChgd.setStatus("current")
_TmnxMobProfPolUntFlowTblLstChgd_Type = TimeStamp
_TmnxMobProfPolUntFlowTblLstChgd_Object = MibScalar
tmnxMobProfPolUntFlowTblLstChgd = _TmnxMobProfPolUntFlowTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 9),
    _TmnxMobProfPolUntFlowTblLstChgd_Type()
)
tmnxMobProfPolUntFlowTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUntFlowTblLstChgd.setStatus("current")
_TmnxMobProfPolBaseTblLstChgd_Type = TimeStamp
_TmnxMobProfPolBaseTblLstChgd_Object = MibScalar
tmnxMobProfPolBaseTblLstChgd = _TmnxMobProfPolBaseTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 10),
    _TmnxMobProfPolBaseTblLstChgd_Type()
)
tmnxMobProfPolBaseTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolBaseTblLstChgd.setStatus("current")
_TmnxMobProfQciPolTblLstChgd_Type = TimeStamp
_TmnxMobProfQciPolTblLstChgd_Object = MibScalar
tmnxMobProfQciPolTblLstChgd = _TmnxMobProfQciPolTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 11),
    _TmnxMobProfQciPolTblLstChgd_Type()
)
tmnxMobProfQciPolTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolTblLstChgd.setStatus("current")
_TmnxMobProfQciPolQciTblLstChgd_Type = TimeStamp
_TmnxMobProfQciPolQciTblLstChgd_Object = MibScalar
tmnxMobProfQciPolQciTblLstChgd = _TmnxMobProfQciPolQciTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 12),
    _TmnxMobProfQciPolQciTblLstChgd_Type()
)
tmnxMobProfQciPolQciTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfQciPolQciTblLstChgd.setStatus("current")
_TmnxMobProfPeerListTblLstChgd_Type = TimeStamp
_TmnxMobProfPeerListTblLstChgd_Object = MibScalar
tmnxMobProfPeerListTblLstChgd = _TmnxMobProfPeerListTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 13),
    _TmnxMobProfPeerListTblLstChgd_Type()
)
tmnxMobProfPeerListTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListTblLstChgd.setStatus("current")
_TmnxMobProfPeerListPeerTblLtCgd_Type = TimeStamp
_TmnxMobProfPeerListPeerTblLtCgd_Object = MibScalar
tmnxMobProfPeerListPeerTblLtCgd = _TmnxMobProfPeerListPeerTblLtCgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 14),
    _TmnxMobProfPeerListPeerTblLtCgd_Type()
)
tmnxMobProfPeerListPeerTblLtCgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPeerListPeerTblLtCgd.setStatus("current")
_TmnxMobProfSgwChargingTblLstChgd_Type = TimeStamp
_TmnxMobProfSgwChargingTblLstChgd_Object = MibScalar
tmnxMobProfSgwChargingTblLstChgd = _TmnxMobProfSgwChargingTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 15),
    _TmnxMobProfSgwChargingTblLstChgd_Type()
)
tmnxMobProfSgwChargingTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfSgwChargingTblLstChgd.setStatus("current")
_TmnxMobProfPgwChargingTblLstChgd_Type = TimeStamp
_TmnxMobProfPgwChargingTblLstChgd_Object = MibScalar
tmnxMobProfPgwChargingTblLstChgd = _TmnxMobProfPgwChargingTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 16),
    _TmnxMobProfPgwChargingTblLstChgd_Type()
)
tmnxMobProfPgwChargingTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPgwChargingTblLstChgd.setStatus("current")
_TmnxMobGtpPriGrpTblLstChgd_Type = TimeStamp
_TmnxMobGtpPriGrpTblLstChgd_Object = MibScalar
tmnxMobGtpPriGrpTblLstChgd = _TmnxMobGtpPriGrpTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 17),
    _TmnxMobGtpPriGrpTblLstChgd_Type()
)
tmnxMobGtpPriGrpTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGtpPriGrpTblLstChgd.setStatus("current")
_TmnxMobGtpPriServerTblLstChgd_Type = TimeStamp
_TmnxMobGtpPriServerTblLstChgd_Object = MibScalar
tmnxMobGtpPriServerTblLstChgd = _TmnxMobGtpPriServerTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 18),
    _TmnxMobGtpPriServerTblLstChgd_Type()
)
tmnxMobGtpPriServerTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGtpPriServerTblLstChgd.setStatus("current")
_TmnxMobUmtsQosPolTblLstChgd_Type = TimeStamp
_TmnxMobUmtsQosPolTblLstChgd_Object = MibScalar
tmnxMobUmtsQosPolTblLstChgd = _TmnxMobUmtsQosPolTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 19),
    _TmnxMobUmtsQosPolTblLstChgd_Type()
)
tmnxMobUmtsQosPolTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobUmtsQosPolTblLstChgd.setStatus("current")
_TmnxMobProfRadTblLstChgd_Type = TimeStamp
_TmnxMobProfRadTblLstChgd_Object = MibScalar
tmnxMobProfRadTblLstChgd = _TmnxMobProfRadTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 20),
    _TmnxMobProfRadTblLstChgd_Type()
)
tmnxMobProfRadTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadTblLstChgd.setStatus("current")
_TmnxMobProfRadGrpTblLstChgd_Type = TimeStamp
_TmnxMobProfRadGrpTblLstChgd_Object = MibScalar
tmnxMobProfRadGrpTblLstChgd = _TmnxMobProfRadGrpTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 21),
    _TmnxMobProfRadGrpTblLstChgd_Type()
)
tmnxMobProfRadGrpTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadGrpTblLstChgd.setStatus("current")
_TmnxMobProfRadPeerTblLstChgd_Type = TimeStamp
_TmnxMobProfRadPeerTblLstChgd_Object = MibScalar
tmnxMobProfRadPeerTblLstChgd = _TmnxMobProfRadPeerTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 22),
    _TmnxMobProfRadPeerTblLstChgd_Type()
)
tmnxMobProfRadPeerTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfRadPeerTblLstChgd.setStatus("current")
_TmnxMobProfDccaTblLstChgd_Type = TimeStamp
_TmnxMobProfDccaTblLstChgd_Object = MibScalar
tmnxMobProfDccaTblLstChgd = _TmnxMobProfDccaTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 23),
    _TmnxMobProfDccaTblLstChgd_Type()
)
tmnxMobProfDccaTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfDccaTblLstChgd.setStatus("current")
_TmnxMobProfPolUnitTblLstChgd_Type = TimeStamp
_TmnxMobProfPolUnitTblLstChgd_Object = MibScalar
tmnxMobProfPolUnitTblLstChgd = _TmnxMobProfPolUnitTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 24),
    _TmnxMobProfPolUnitTblLstChgd_Type()
)
tmnxMobProfPolUnitTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfPolUnitTblLstChgd.setStatus("current")
_TmnxMobProfChgUnitTblLstChgd_Type = TimeStamp
_TmnxMobProfChgUnitTblLstChgd_Object = MibScalar
tmnxMobProfChgUnitTblLstChgd = _TmnxMobProfChgUnitTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 25),
    _TmnxMobProfChgUnitTblLstChgd_Type()
)
tmnxMobProfChgUnitTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfChgUnitTblLstChgd.setStatus("current")
_TmnxMobProfHTTPRedirctTblLstChgd_Type = TimeStamp
_TmnxMobProfHTTPRedirctTblLstChgd_Object = MibScalar
tmnxMobProfHTTPRedirctTblLstChgd = _TmnxMobProfHTTPRedirctTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 67, 2, 26),
    _TmnxMobProfHTTPRedirctTblLstChgd_Type()
)
tmnxMobProfHTTPRedirctTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobProfHTTPRedirctTblLstChgd.setStatus("current")

# Managed Objects groups

tmnxMobProfGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 1)
)
tmnxMobProfGlobalGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerTblLtCgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlowTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChargingTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChargingTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6TblLstChgd"))
)
if mibBuilder.loadTexts:
    tmnxMobProfGlobalGroup.setStatus("current")

tmnxMobProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 2)
)
tmnxMobProfGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysBCLimit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysBCActivtyRate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysBCPdnLimit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysBCUeLimit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSDFIpv4Limit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSDFIpv6Limit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysCpuThreshldCriticl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysCpuThreshldMajor"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysCpuThreshldMinor"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysMemThreshldCriticl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysMemThreshldMajor"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysMemThreshldMinor"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSgnlFailThrshldS5"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSgnlFailThrshldS8"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSgnlFailThrshldS11"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysSgnlFailThrshldGxc"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysTrfcDropThrshldS1u"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysTrfcDropThrshldS5"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysTrfcDropThrshldS8"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysPagingBufferLimit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysPagingBufferSize"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysPagingTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysS1BufferLimit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysS1BufferSize"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpMsgReTxTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpMsgReTxRetryCnt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpKeepAlvTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpKeepAlvRetryCnt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpKeepAlvResp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpIpTtl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpIpDscp"))
)
if mibBuilder.loadTexts:
    tmnxMobProfGroup.setStatus("current")

tmnxMobProfQciPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 3)
)
tmnxMobProfQciPolicyGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciDscpPreserve"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciDscp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciDscpOut"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciFcName"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolQciProfile"))
)
if mibBuilder.loadTexts:
    tmnxMobProfQciPolicyGroup.setStatus("current")

tmnxMobProfDiameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 4)
)
tmnxMobProfDiameterGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaWatchdgTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaConnTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaTransTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaIpTtl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaIpDscp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaDprTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPermFailRetryTime"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaDnsRefreshInt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerDiaProfName"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerDestRealm"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerTransport"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerLoadBalance"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerIfVRtrId"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerIfIndex"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerApplication"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListLastChngd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerAdminState"))
)
if mibBuilder.loadTexts:
    tmnxMobProfDiameterGroup.setStatus("current")

tmnxMobProfUnsupportedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 5)
)
tmnxMobProfUnsupportedGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPlmnListTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPlmnListRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSysDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfGtpDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfQciPolDescription"))
)
if mibBuilder.loadTexts:
    tmnxMobProfUnsupportedGroup.setStatus("current")

tmnxMobProfChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 6)
)
tmnxMobProfChargingGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgDesc"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgOffLineState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPriCdfDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgSecCdfDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitQosChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitUsrLocChnge"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitTrfTimeChng"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitTrfTmStart"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitTrfTmEnd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctTimeLmt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctVolumeLmt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctMaxChCond"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctMsTmzChnge"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctPlmnChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctRatChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctMgmtInterv"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgDesc"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgOffLineState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPriCdfDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgSecCdfDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitQosChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitUsrLocChnge"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitTrfTimeChng"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitTrfTmStart"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitTrfTmEnd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitSgwChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitTimeLmtRg"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitVolumeLmtRg"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgCitTermServDf"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctTimeLmt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctVolumeLmt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctMaxChCond"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctMsTmzChnge"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctPlmnChange"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctRatChange"))
)
if mibBuilder.loadTexts:
    tmnxMobProfChargingGroup.setStatus("current")

tmnxMobProfGtpPrimeServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 8)
)
tmnxMobProfGtpPrimeServerGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpMaxCdrsPerPdu"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpDeadtime"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpRedirection"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpIfVRtrId"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpIfIndex"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpLocalCdrStorage"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFilePrivateInfo"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFileExtension"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFileClosureSize"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFileClsLifeTime"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFileClsMaxRecs"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpFileObsoleteTime"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpPrimaryCf"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpCf1State"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpCf1Limit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpCf2State"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpCf2Limit"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpCpmMemoryState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpQueueSize"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpAdminState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpInactiveTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerLastChngd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAdminState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerRetries"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerEchoInterval"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerMaxRequests"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerNodeAlive"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerPriority"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerPathProtocol"))
)
if mibBuilder.loadTexts:
    tmnxMobProfGtpPrimeServerGroup.setStatus("current")

tmnxMobProfUmtsQosPolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 9)
)
tmnxMobProfUmtsQosPolGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolConvSpeechQci"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolConvUnkTdg"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolConvUnkTdl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolStreamQciValue"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolInterSigP1Qci"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolInterP1Qci"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolInterP2Qci"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolInterP3Qci"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobUmtsQosPolBackground"))
)
if mibBuilder.loadTexts:
    tmnxMobProfUmtsQosPolGroup.setStatus("current")

tmnxMobProfRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 10)
)
tmnxMobProfRadiusGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadAuthProbeInt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadServerDeadTime"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadRetryTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadRetryCount"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpIfVRtrId"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpIfIndex"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpAuthServerPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpAcctServerPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpSecret"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpIntUpdateIntvl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpServerType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpRadiusProfile"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpIgnAcctResp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerLastChngd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerAdminState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerPriority"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerAuthSvrPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerAcctSvrPort"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerSecret"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerRadProfile"))
)
if mibBuilder.loadTexts:
    tmnxMobProfRadiusGroup.setStatus("current")

tmnxMobProfChargingV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 11)
)
tmnxMobProfChargingV3Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgGyState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwGyPriOcsDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwGySecOcsDiaPeer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwGyDccaProf"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPgwChrgPrctSrvNdChLmt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgPrctSrvNdChLmt"))
)
if mibBuilder.loadTexts:
    tmnxMobProfChargingV3Group.setStatus("current")

tmnxMobProfDccaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 12)
)
tmnxMobProfDccaGroup.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaApplTxTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaRetryCnt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDcca3GppQosNegProf"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaQosInformation"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaCalledStationId"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaCcSessFailover"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaCcSessFlovrHndl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaForcedReAuth"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaQuotaExNoThrsld"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaQuotaExThrsldAct"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaQuotaUnavail"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaRatingCondtChng"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaValidityTimeExp"))
)
if mibBuilder.loadTexts:
    tmnxMobProfDccaGroup.setStatus("current")

tmnxMobProfGlobalV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 13)
)
tmnxMobProfGlobalV3Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitTblLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfHTTPRedirctTblLstChgd"))
)
if mibBuilder.loadTexts:
    tmnxMobProfGlobalV3Group.setStatus("current")

tmnxMobProfV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 14)
)
tmnxMobProfV3Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListDescription"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerLastChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerDesc"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerKeepAlive"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerAdmnState"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerRatType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerForeign"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerPlmnMcc"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPeerListPeerPlmnMnc"))
)
if mibBuilder.loadTexts:
    tmnxMobProfV3Group.setStatus("current")

tmnxMobProfPolicyRulesV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 15)
)
tmnxMobProfPolicyRulesV3Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolRuleUnitName"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgRuleUnitName"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolQciValue"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolArpValue"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwDirection"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwMatchPrtcl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclPrefixLen"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtPrefixLen"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclPortVal1"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclPortVal2"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwLclPortOper"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtPortVal1"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtPortVal2"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwRmtPortOper"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBasePrecedence"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBasePreActivate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitUplinkGbrRate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitUplinkMbrRate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitDwnlinkGbrRate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUnitDwnlinkMbrRate"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwGateStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitLastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRatingGroup"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitServIdentifier"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitReportingLevel"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitChargingMethod"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitMeteringMethod"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolPrecedence"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfHttpRedirectRowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfHttpRedirectLstChgd"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntRedirectAdrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntRedirectAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntFlwAaApp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfHttpRedirctPrecedence"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntInUse"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolUntRefCount"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolInUse"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolRefCount"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitInUse"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRefCount"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseInUse"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseRefCount"))
)
if mibBuilder.loadTexts:
    tmnxMobProfPolicyRulesV3Group.setStatus("current")

tmnxMobProfPmipv6V3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 16)
)
tmnxMobProfPmipv6V3Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6RowStatus"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6LastChanged"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6Description"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6MsgReTxTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6MsgReTxRetryCnt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6KeepAlvTimeout"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6KeepAlvRetryCnt"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6IpTtl"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6IpDscp"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPmipv6KeepAlvIntvl"))
)
if mibBuilder.loadTexts:
    tmnxMobProfPmipv6V3Group.setStatus("current")

tmnxMobProfileObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 17)
)
tmnxMobProfileObsoletedGroup.setObjects(
    ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfSgwChrgCitSgwChange")
)
if mibBuilder.loadTexts:
    tmnxMobProfileObsoletedGroup.setStatus("current")

tmnxMobProfPolicyRulesV31Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 18)
)
tmnxMobProfPolicyRulesV31Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseConfRefCount"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolConfRefCount"))
)
if mibBuilder.loadTexts:
    tmnxMobProfPolicyRulesV31Group.setStatus("current")

tmnxMobProfDccaV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 2, 19)
)
tmnxMobProfDccaV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaFhSessContTimer"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaDefaultQht"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDccaFirstPktBehavior"))
)
if mibBuilder.loadTexts:
    tmnxMobProfDccaV4v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxMobProfV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMobProfV1v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobProfV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMobProfV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobProf7xxxV10v0Compl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMobProf7xxxV10v0Compl.setStatus(
        "current"
    )

tmnxMobProfV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 67, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMobProfV4v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MOBILE-PROFILE-MIB",
    **{"TmnxMobProfThreshold": TmnxMobProfThreshold,
       "TmnxMobProfMsgReTxTimeout": TmnxMobProfMsgReTxTimeout,
       "TmnxMobProfMsgReTxRetryCount": TmnxMobProfMsgReTxRetryCount,
       "TmnxMobProfKeepAliveTimeout": TmnxMobProfKeepAliveTimeout,
       "TmnxMobProfKeepAliveRetryCount": TmnxMobProfKeepAliveRetryCount,
       "TmnxMobProfKeepAliveResponse": TmnxMobProfKeepAliveResponse,
       "TmnxMobProfKeepAliveInterval": TmnxMobProfKeepAliveInterval,
       "TmnxMobProfAllowDiscard": TmnxMobProfAllowDiscard,
       "timetraMobProfileMIBModule": timetraMobProfileMIBModule,
       "tmnxMobProfileConformance": tmnxMobProfileConformance,
       "tmnxMobProfileCompliances": tmnxMobProfileCompliances,
       "tmnxMobProfV1v0Compliance": tmnxMobProfV1v0Compliance,
       "tmnxMobProfV3v0Compliance": tmnxMobProfV3v0Compliance,
       "tmnxMobProf7xxxV10v0Compl": tmnxMobProf7xxxV10v0Compl,
       "tmnxMobProfV4v0Compliance": tmnxMobProfV4v0Compliance,
       "tmnxMobProfileGroups": tmnxMobProfileGroups,
       "tmnxMobProfGlobalGroup": tmnxMobProfGlobalGroup,
       "tmnxMobProfGroup": tmnxMobProfGroup,
       "tmnxMobProfQciPolicyGroup": tmnxMobProfQciPolicyGroup,
       "tmnxMobProfDiameterGroup": tmnxMobProfDiameterGroup,
       "tmnxMobProfUnsupportedGroup": tmnxMobProfUnsupportedGroup,
       "tmnxMobProfChargingGroup": tmnxMobProfChargingGroup,
       "tmnxMobProfGtpPrimeServerGroup": tmnxMobProfGtpPrimeServerGroup,
       "tmnxMobProfUmtsQosPolGroup": tmnxMobProfUmtsQosPolGroup,
       "tmnxMobProfRadiusGroup": tmnxMobProfRadiusGroup,
       "tmnxMobProfChargingV3Group": tmnxMobProfChargingV3Group,
       "tmnxMobProfDccaGroup": tmnxMobProfDccaGroup,
       "tmnxMobProfGlobalV3Group": tmnxMobProfGlobalV3Group,
       "tmnxMobProfV3Group": tmnxMobProfV3Group,
       "tmnxMobProfPolicyRulesV3Group": tmnxMobProfPolicyRulesV3Group,
       "tmnxMobProfPmipv6V3Group": tmnxMobProfPmipv6V3Group,
       "tmnxMobProfileObsoletedGroup": tmnxMobProfileObsoletedGroup,
       "tmnxMobProfPolicyRulesV31Group": tmnxMobProfPolicyRulesV31Group,
       "tmnxMobProfDccaV4v0Group": tmnxMobProfDccaV4v0Group,
       "tmnxMobProfile": tmnxMobProfile,
       "tmnxMobProfileObjs": tmnxMobProfileObjs,
       "tmnxMobProfSysTable": tmnxMobProfSysTable,
       "tmnxMobProfSysEntry": tmnxMobProfSysEntry,
       "tmnxMobProfSysName": tmnxMobProfSysName,
       "tmnxMobProfSysRowStatus": tmnxMobProfSysRowStatus,
       "tmnxMobProfSysLastChanged": tmnxMobProfSysLastChanged,
       "tmnxMobProfSysDescription": tmnxMobProfSysDescription,
       "tmnxMobProfSysBCLimit": tmnxMobProfSysBCLimit,
       "tmnxMobProfSysBCActivtyRate": tmnxMobProfSysBCActivtyRate,
       "tmnxMobProfSysBCPdnLimit": tmnxMobProfSysBCPdnLimit,
       "tmnxMobProfSysBCUeLimit": tmnxMobProfSysBCUeLimit,
       "tmnxMobProfSysSDFIpv4Limit": tmnxMobProfSysSDFIpv4Limit,
       "tmnxMobProfSysSDFIpv6Limit": tmnxMobProfSysSDFIpv6Limit,
       "tmnxMobProfSysCpuThreshldCriticl": tmnxMobProfSysCpuThreshldCriticl,
       "tmnxMobProfSysCpuThreshldMajor": tmnxMobProfSysCpuThreshldMajor,
       "tmnxMobProfSysCpuThreshldMinor": tmnxMobProfSysCpuThreshldMinor,
       "tmnxMobProfSysMemThreshldCriticl": tmnxMobProfSysMemThreshldCriticl,
       "tmnxMobProfSysMemThreshldMajor": tmnxMobProfSysMemThreshldMajor,
       "tmnxMobProfSysMemThreshldMinor": tmnxMobProfSysMemThreshldMinor,
       "tmnxMobProfSysSgnlFailThrshldS5": tmnxMobProfSysSgnlFailThrshldS5,
       "tmnxMobProfSysSgnlFailThrshldS8": tmnxMobProfSysSgnlFailThrshldS8,
       "tmnxMobProfSysSgnlFailThrshldS11": tmnxMobProfSysSgnlFailThrshldS11,
       "tmnxMobProfSysSgnlFailThrshldGxc": tmnxMobProfSysSgnlFailThrshldGxc,
       "tmnxMobProfSysTrfcDropThrshldS1u": tmnxMobProfSysTrfcDropThrshldS1u,
       "tmnxMobProfSysTrfcDropThrshldS5": tmnxMobProfSysTrfcDropThrshldS5,
       "tmnxMobProfSysTrfcDropThrshldS8": tmnxMobProfSysTrfcDropThrshldS8,
       "tmnxMobProfSysPagingBufferLimit": tmnxMobProfSysPagingBufferLimit,
       "tmnxMobProfSysPagingBufferSize": tmnxMobProfSysPagingBufferSize,
       "tmnxMobProfSysPagingTimeout": tmnxMobProfSysPagingTimeout,
       "tmnxMobProfSysS1BufferLimit": tmnxMobProfSysS1BufferLimit,
       "tmnxMobProfSysS1BufferSize": tmnxMobProfSysS1BufferSize,
       "tmnxMobProfDiaTable": tmnxMobProfDiaTable,
       "tmnxMobProfDiaEntry": tmnxMobProfDiaEntry,
       "tmnxMobProfDiaName": tmnxMobProfDiaName,
       "tmnxMobProfDiaRowStatus": tmnxMobProfDiaRowStatus,
       "tmnxMobProfDiaLastChanged": tmnxMobProfDiaLastChanged,
       "tmnxMobProfDiaDescription": tmnxMobProfDiaDescription,
       "tmnxMobProfDiaWatchdgTimer": tmnxMobProfDiaWatchdgTimer,
       "tmnxMobProfDiaConnTimer": tmnxMobProfDiaConnTimer,
       "tmnxMobProfDiaTransTimer": tmnxMobProfDiaTransTimer,
       "tmnxMobProfDiaIpTtl": tmnxMobProfDiaIpTtl,
       "tmnxMobProfDiaIpDscp": tmnxMobProfDiaIpDscp,
       "tmnxMobProfDiaDprTimeout": tmnxMobProfDiaDprTimeout,
       "tmnxMobProfDiaPermFailRetryTime": tmnxMobProfDiaPermFailRetryTime,
       "tmnxMobProfDiaDnsRefreshInt": tmnxMobProfDiaDnsRefreshInt,
       "tmnxMobProfDiaPeerTable": tmnxMobProfDiaPeerTable,
       "tmnxMobProfDiaPeerEntry": tmnxMobProfDiaPeerEntry,
       "tmnxMobProfDiaPeerName": tmnxMobProfDiaPeerName,
       "tmnxMobProfDiaPeerRowStatus": tmnxMobProfDiaPeerRowStatus,
       "tmnxMobProfDiaPeerLastChanged": tmnxMobProfDiaPeerLastChanged,
       "tmnxMobProfDiaPeerDescription": tmnxMobProfDiaPeerDescription,
       "tmnxMobProfDiaPeerDiaProfName": tmnxMobProfDiaPeerDiaProfName,
       "tmnxMobProfDiaPeerDestRealm": tmnxMobProfDiaPeerDestRealm,
       "tmnxMobProfDiaPeerTransport": tmnxMobProfDiaPeerTransport,
       "tmnxMobProfDiaPeerLoadBalance": tmnxMobProfDiaPeerLoadBalance,
       "tmnxMobProfDiaPeerIfVRtrId": tmnxMobProfDiaPeerIfVRtrId,
       "tmnxMobProfDiaPeerIfIndex": tmnxMobProfDiaPeerIfIndex,
       "tmnxMobProfDiaPeerApplication": tmnxMobProfDiaPeerApplication,
       "tmnxMobProfDiaPeerListTable": tmnxMobProfDiaPeerListTable,
       "tmnxMobProfDiaPeerListEntry": tmnxMobProfDiaPeerListEntry,
       "tmnxMobProfDiaPeerListIndex": tmnxMobProfDiaPeerListIndex,
       "tmnxMobProfDiaPeerListRowStatus": tmnxMobProfDiaPeerListRowStatus,
       "tmnxMobProfDiaPeerListLastChngd": tmnxMobProfDiaPeerListLastChngd,
       "tmnxMobProfDiaPeerListAddrType": tmnxMobProfDiaPeerListAddrType,
       "tmnxMobProfDiaPeerListAddr": tmnxMobProfDiaPeerListAddr,
       "tmnxMobProfDiaPeerListPort": tmnxMobProfDiaPeerListPort,
       "tmnxMobProfDiaPeerAdminState": tmnxMobProfDiaPeerAdminState,
       "tmnxMobProfPmipv6Table": tmnxMobProfPmipv6Table,
       "tmnxMobProfPmipv6Entry": tmnxMobProfPmipv6Entry,
       "tmnxMobProfPmipv6Name": tmnxMobProfPmipv6Name,
       "tmnxMobProfPmipv6RowStatus": tmnxMobProfPmipv6RowStatus,
       "tmnxMobProfPmipv6LastChanged": tmnxMobProfPmipv6LastChanged,
       "tmnxMobProfPmipv6Description": tmnxMobProfPmipv6Description,
       "tmnxMobProfPmipv6MsgReTxTimeout": tmnxMobProfPmipv6MsgReTxTimeout,
       "tmnxMobProfPmipv6MsgReTxRetryCnt": tmnxMobProfPmipv6MsgReTxRetryCnt,
       "tmnxMobProfPmipv6KeepAlvTimeout": tmnxMobProfPmipv6KeepAlvTimeout,
       "tmnxMobProfPmipv6KeepAlvRetryCnt": tmnxMobProfPmipv6KeepAlvRetryCnt,
       "tmnxMobProfPmipv6KeepAlvIntvl": tmnxMobProfPmipv6KeepAlvIntvl,
       "tmnxMobProfPmipv6IpTtl": tmnxMobProfPmipv6IpTtl,
       "tmnxMobProfPmipv6IpDscp": tmnxMobProfPmipv6IpDscp,
       "tmnxMobProfGtpTable": tmnxMobProfGtpTable,
       "tmnxMobProfGtpEntry": tmnxMobProfGtpEntry,
       "tmnxMobProfGtpName": tmnxMobProfGtpName,
       "tmnxMobProfGtpRowStatus": tmnxMobProfGtpRowStatus,
       "tmnxMobProfGtpLastChanged": tmnxMobProfGtpLastChanged,
       "tmnxMobProfGtpDescription": tmnxMobProfGtpDescription,
       "tmnxMobProfGtpMsgReTxTimeout": tmnxMobProfGtpMsgReTxTimeout,
       "tmnxMobProfGtpMsgReTxRetryCnt": tmnxMobProfGtpMsgReTxRetryCnt,
       "tmnxMobProfGtpKeepAlvTimeout": tmnxMobProfGtpKeepAlvTimeout,
       "tmnxMobProfGtpKeepAlvRetryCnt": tmnxMobProfGtpKeepAlvRetryCnt,
       "tmnxMobProfGtpKeepAlvResp": tmnxMobProfGtpKeepAlvResp,
       "tmnxMobProfGtpIpTtl": tmnxMobProfGtpIpTtl,
       "tmnxMobProfGtpIpDscp": tmnxMobProfGtpIpDscp,
       "tmnxMobProfPlmnListTable": tmnxMobProfPlmnListTable,
       "tmnxMobProfPlmnListEntry": tmnxMobProfPlmnListEntry,
       "tmnxMobProfPlmnListName": tmnxMobProfPlmnListName,
       "tmnxMobProfPlmnListMcc": tmnxMobProfPlmnListMcc,
       "tmnxMobProfPlmnListMnc": tmnxMobProfPlmnListMnc,
       "tmnxMobProfPlmnListRowStatus": tmnxMobProfPlmnListRowStatus,
       "tmnxMobProfPolTable": tmnxMobProfPolTable,
       "tmnxMobProfPolEntry": tmnxMobProfPolEntry,
       "tmnxMobProfPolName": tmnxMobProfPolName,
       "tmnxMobProfPolRowStatus": tmnxMobProfPolRowStatus,
       "tmnxMobProfPolLastChanged": tmnxMobProfPolLastChanged,
       "tmnxMobProfPolRuleUnitName": tmnxMobProfPolRuleUnitName,
       "tmnxMobProfChgRuleUnitName": tmnxMobProfChgRuleUnitName,
       "tmnxMobProfPolQciValue": tmnxMobProfPolQciValue,
       "tmnxMobProfPolArpValue": tmnxMobProfPolArpValue,
       "tmnxMobProfPolPrecedence": tmnxMobProfPolPrecedence,
       "tmnxMobProfPolInUse": tmnxMobProfPolInUse,
       "tmnxMobProfPolRefCount": tmnxMobProfPolRefCount,
       "tmnxMobProfPolConfRefCount": tmnxMobProfPolConfRefCount,
       "tmnxMobProfPolUntFlwTable": tmnxMobProfPolUntFlwTable,
       "tmnxMobProfPolUntFlwEntry": tmnxMobProfPolUntFlwEntry,
       "tmnxMobProfPolUntFlwId": tmnxMobProfPolUntFlwId,
       "tmnxMobProfPolUntFlwRowStatus": tmnxMobProfPolUntFlwRowStatus,
       "tmnxMobProfPolUntFlwLastChanged": tmnxMobProfPolUntFlwLastChanged,
       "tmnxMobProfPolUntFlwDirection": tmnxMobProfPolUntFlwDirection,
       "tmnxMobProfPolUntFlwMatchPrtcl": tmnxMobProfPolUntFlwMatchPrtcl,
       "tmnxMobProfPolUntFlwLclAddrType": tmnxMobProfPolUntFlwLclAddrType,
       "tmnxMobProfPolUntFlwLclAddr": tmnxMobProfPolUntFlwLclAddr,
       "tmnxMobProfPolUntFlwLclPrefixLen": tmnxMobProfPolUntFlwLclPrefixLen,
       "tmnxMobProfPolUntFlwRmtAddrType": tmnxMobProfPolUntFlwRmtAddrType,
       "tmnxMobProfPolUntFlwRmtAddr": tmnxMobProfPolUntFlwRmtAddr,
       "tmnxMobProfPolUntFlwRmtPrefixLen": tmnxMobProfPolUntFlwRmtPrefixLen,
       "tmnxMobProfPolUntFlwLclPortVal1": tmnxMobProfPolUntFlwLclPortVal1,
       "tmnxMobProfPolUntFlwLclPortVal2": tmnxMobProfPolUntFlwLclPortVal2,
       "tmnxMobProfPolUntFlwLclPortOper": tmnxMobProfPolUntFlwLclPortOper,
       "tmnxMobProfPolUntFlwRmtPortVal1": tmnxMobProfPolUntFlwRmtPortVal1,
       "tmnxMobProfPolUntFlwRmtPortVal2": tmnxMobProfPolUntFlwRmtPortVal2,
       "tmnxMobProfPolUntFlwRmtPortOper": tmnxMobProfPolUntFlwRmtPortOper,
       "tmnxMobProfPolUntFlwAaApp": tmnxMobProfPolUntFlwAaApp,
       "tmnxMobProfPolBaseTable": tmnxMobProfPolBaseTable,
       "tmnxMobProfPolBaseEntry": tmnxMobProfPolBaseEntry,
       "tmnxMobProfPolBaseName": tmnxMobProfPolBaseName,
       "tmnxMobProfPolBaseRowStatus": tmnxMobProfPolBaseRowStatus,
       "tmnxMobProfPolBaseLastChanged": tmnxMobProfPolBaseLastChanged,
       "tmnxMobProfPolBasePrecedence": tmnxMobProfPolBasePrecedence,
       "tmnxMobProfPolBasePreActivate": tmnxMobProfPolBasePreActivate,
       "tmnxMobProfPolBaseInUse": tmnxMobProfPolBaseInUse,
       "tmnxMobProfPolBaseRefCount": tmnxMobProfPolBaseRefCount,
       "tmnxMobProfPolBaseConfRefCount": tmnxMobProfPolBaseConfRefCount,
       "tmnxMobProfQciPolTable": tmnxMobProfQciPolTable,
       "tmnxMobProfQciPolEntry": tmnxMobProfQciPolEntry,
       "tmnxMobProfQciPolName": tmnxMobProfQciPolName,
       "tmnxMobProfQciPolRowStatus": tmnxMobProfQciPolRowStatus,
       "tmnxMobProfQciPolLastChanged": tmnxMobProfQciPolLastChanged,
       "tmnxMobProfQciPolDescription": tmnxMobProfQciPolDescription,
       "tmnxMobProfQciPolQciTable": tmnxMobProfQciPolQciTable,
       "tmnxMobProfQciPolQciEntry": tmnxMobProfQciPolQciEntry,
       "tmnxMobProfQciPolQciValue": tmnxMobProfQciPolQciValue,
       "tmnxMobProfQciPolQciArpValue": tmnxMobProfQciPolQciArpValue,
       "tmnxMobProfQciPolQciLastChanged": tmnxMobProfQciPolQciLastChanged,
       "tmnxMobProfQciPolQciDscpPreserve": tmnxMobProfQciPolQciDscpPreserve,
       "tmnxMobProfQciPolQciDscp": tmnxMobProfQciPolQciDscp,
       "tmnxMobProfQciPolQciDscpOut": tmnxMobProfQciPolQciDscpOut,
       "tmnxMobProfQciPolQciFcName": tmnxMobProfQciPolQciFcName,
       "tmnxMobProfQciPolQciProfile": tmnxMobProfQciPolQciProfile,
       "tmnxMobProfPeerListTable": tmnxMobProfPeerListTable,
       "tmnxMobProfPeerListEntry": tmnxMobProfPeerListEntry,
       "tmnxMobProfPeerListName": tmnxMobProfPeerListName,
       "tmnxMobProfPeerListRowStatus": tmnxMobProfPeerListRowStatus,
       "tmnxMobProfPeerListLastChanged": tmnxMobProfPeerListLastChanged,
       "tmnxMobProfPeerListDescription": tmnxMobProfPeerListDescription,
       "tmnxMobProfPeerListPeerTable": tmnxMobProfPeerListPeerTable,
       "tmnxMobProfPeerListPeerEntry": tmnxMobProfPeerListPeerEntry,
       "tmnxMobProfPeerListPeerAddrType": tmnxMobProfPeerListPeerAddrType,
       "tmnxMobProfPeerListPeerAddr": tmnxMobProfPeerListPeerAddr,
       "tmnxMobProfPeerListPeerPrefixLen": tmnxMobProfPeerListPeerPrefixLen,
       "tmnxMobProfPeerListPeerRowStatus": tmnxMobProfPeerListPeerRowStatus,
       "tmnxMobProfPeerListPeerLastChgd": tmnxMobProfPeerListPeerLastChgd,
       "tmnxMobProfPeerListPeerDesc": tmnxMobProfPeerListPeerDesc,
       "tmnxMobProfPeerListPeerKeepAlive": tmnxMobProfPeerListPeerKeepAlive,
       "tmnxMobProfPeerListPeerAdmnState": tmnxMobProfPeerListPeerAdmnState,
       "tmnxMobProfPeerListPeerRatType": tmnxMobProfPeerListPeerRatType,
       "tmnxMobProfPeerListPeerForeign": tmnxMobProfPeerListPeerForeign,
       "tmnxMobProfPeerListPeerPlmnMcc": tmnxMobProfPeerListPeerPlmnMcc,
       "tmnxMobProfPeerListPeerPlmnMnc": tmnxMobProfPeerListPeerPlmnMnc,
       "tmnxMobProfSgwChargingTable": tmnxMobProfSgwChargingTable,
       "tmnxMobProfSgwChargingEntry": tmnxMobProfSgwChargingEntry,
       "tmnxMobProfSgwChrgId": tmnxMobProfSgwChrgId,
       "tmnxMobProfSgwChrgRowStatus": tmnxMobProfSgwChrgRowStatus,
       "tmnxMobProfSgwChrgLastChanged": tmnxMobProfSgwChrgLastChanged,
       "tmnxMobProfSgwChrgDesc": tmnxMobProfSgwChrgDesc,
       "tmnxMobProfSgwChrgOffLineState": tmnxMobProfSgwChrgOffLineState,
       "tmnxMobProfSgwChrgPriCdfDiaPeer": tmnxMobProfSgwChrgPriCdfDiaPeer,
       "tmnxMobProfSgwChrgSecCdfDiaPeer": tmnxMobProfSgwChrgSecCdfDiaPeer,
       "tmnxMobProfSgwChrgCitQosChange": tmnxMobProfSgwChrgCitQosChange,
       "tmnxMobProfSgwChrgCitUsrLocChnge": tmnxMobProfSgwChrgCitUsrLocChnge,
       "tmnxMobProfSgwChrgCitTrfTimeChng": tmnxMobProfSgwChrgCitTrfTimeChng,
       "tmnxMobProfSgwChrgCitTrfTmStart": tmnxMobProfSgwChrgCitTrfTmStart,
       "tmnxMobProfSgwChrgCitTrfTmEnd": tmnxMobProfSgwChrgCitTrfTmEnd,
       "tmnxMobProfSgwChrgPrctTimeLmt": tmnxMobProfSgwChrgPrctTimeLmt,
       "tmnxMobProfSgwChrgPrctVolumeLmt": tmnxMobProfSgwChrgPrctVolumeLmt,
       "tmnxMobProfSgwChrgPrctMaxChCond": tmnxMobProfSgwChrgPrctMaxChCond,
       "tmnxMobProfSgwChrgPrctMsTmzChnge": tmnxMobProfSgwChrgPrctMsTmzChnge,
       "tmnxMobProfSgwChrgPrctPlmnChange": tmnxMobProfSgwChrgPrctPlmnChange,
       "tmnxMobProfSgwChrgPrctRatChange": tmnxMobProfSgwChrgPrctRatChange,
       "tmnxMobProfSgwChrgPrctMgmtInterv": tmnxMobProfSgwChrgPrctMgmtInterv,
       "tmnxMobProfSgwChrgCitSgwChange": tmnxMobProfSgwChrgCitSgwChange,
       "tmnxMobProfSgwChrgPrctSrvNdChLmt": tmnxMobProfSgwChrgPrctSrvNdChLmt,
       "tmnxMobProfPgwChargingTable": tmnxMobProfPgwChargingTable,
       "tmnxMobProfPgwChargingEntry": tmnxMobProfPgwChargingEntry,
       "tmnxMobProfPgwChrgId": tmnxMobProfPgwChrgId,
       "tmnxMobProfPgwChrgRowStatus": tmnxMobProfPgwChrgRowStatus,
       "tmnxMobProfPgwChrgLastChanged": tmnxMobProfPgwChrgLastChanged,
       "tmnxMobProfPgwChrgDesc": tmnxMobProfPgwChrgDesc,
       "tmnxMobProfPgwChrgOffLineState": tmnxMobProfPgwChrgOffLineState,
       "tmnxMobProfPgwChrgPriCdfDiaPeer": tmnxMobProfPgwChrgPriCdfDiaPeer,
       "tmnxMobProfPgwChrgSecCdfDiaPeer": tmnxMobProfPgwChrgSecCdfDiaPeer,
       "tmnxMobProfPgwChrgCitQosChange": tmnxMobProfPgwChrgCitQosChange,
       "tmnxMobProfPgwChrgCitUsrLocChnge": tmnxMobProfPgwChrgCitUsrLocChnge,
       "tmnxMobProfPgwChrgCitTrfTimeChng": tmnxMobProfPgwChrgCitTrfTimeChng,
       "tmnxMobProfPgwChrgCitTrfTmStart": tmnxMobProfPgwChrgCitTrfTmStart,
       "tmnxMobProfPgwChrgCitTrfTmEnd": tmnxMobProfPgwChrgCitTrfTmEnd,
       "tmnxMobProfPgwChrgCitSgwChange": tmnxMobProfPgwChrgCitSgwChange,
       "tmnxMobProfPgwChrgCitTimeLmtRg": tmnxMobProfPgwChrgCitTimeLmtRg,
       "tmnxMobProfPgwChrgCitVolumeLmtRg": tmnxMobProfPgwChrgCitVolumeLmtRg,
       "tmnxMobProfPgwChrgCitTermServDf": tmnxMobProfPgwChrgCitTermServDf,
       "tmnxMobProfPgwChrgPrctTimeLmt": tmnxMobProfPgwChrgPrctTimeLmt,
       "tmnxMobProfPgwChrgPrctVolumeLmt": tmnxMobProfPgwChrgPrctVolumeLmt,
       "tmnxMobProfPgwChrgPrctMaxChCond": tmnxMobProfPgwChrgPrctMaxChCond,
       "tmnxMobProfPgwChrgPrctMsTmzChnge": tmnxMobProfPgwChrgPrctMsTmzChnge,
       "tmnxMobProfPgwChrgPrctPlmnChange": tmnxMobProfPgwChrgPrctPlmnChange,
       "tmnxMobProfPgwChrgPrctRatChange": tmnxMobProfPgwChrgPrctRatChange,
       "tmnxMobProfPgwChrgGyState": tmnxMobProfPgwChrgGyState,
       "tmnxMobProfPgwGyPriOcsDiaPeer": tmnxMobProfPgwGyPriOcsDiaPeer,
       "tmnxMobProfPgwGySecOcsDiaPeer": tmnxMobProfPgwGySecOcsDiaPeer,
       "tmnxMobProfPgwGyDccaProf": tmnxMobProfPgwGyDccaProf,
       "tmnxMobProfPgwChrgPrctSrvNdChLmt": tmnxMobProfPgwChrgPrctSrvNdChLmt,
       "tmnxMobGtpPriGrpTable": tmnxMobGtpPriGrpTable,
       "tmnxMobGtpPriGrpEntry": tmnxMobGtpPriGrpEntry,
       "tmnxMobGtpPriGrpName": tmnxMobGtpPriGrpName,
       "tmnxMobGtpPriGrpRowStatus": tmnxMobGtpPriGrpRowStatus,
       "tmnxMobGtpPriGrpLastChanged": tmnxMobGtpPriGrpLastChanged,
       "tmnxMobGtpPriGrpDescription": tmnxMobGtpPriGrpDescription,
       "tmnxMobGtpPriGrpMaxCdrsPerPdu": tmnxMobGtpPriGrpMaxCdrsPerPdu,
       "tmnxMobGtpPriGrpDeadtime": tmnxMobGtpPriGrpDeadtime,
       "tmnxMobGtpPriGrpRedirection": tmnxMobGtpPriGrpRedirection,
       "tmnxMobGtpPriGrpIfVRtrId": tmnxMobGtpPriGrpIfVRtrId,
       "tmnxMobGtpPriGrpIfIndex": tmnxMobGtpPriGrpIfIndex,
       "tmnxMobGtpPriGrpLocalCdrStorage": tmnxMobGtpPriGrpLocalCdrStorage,
       "tmnxMobGtpPriGrpFilePrivateInfo": tmnxMobGtpPriGrpFilePrivateInfo,
       "tmnxMobGtpPriGrpFileExtension": tmnxMobGtpPriGrpFileExtension,
       "tmnxMobGtpPriGrpFileClosureSize": tmnxMobGtpPriGrpFileClosureSize,
       "tmnxMobGtpPriGrpFileClsLifeTime": tmnxMobGtpPriGrpFileClsLifeTime,
       "tmnxMobGtpPriGrpFileClsMaxRecs": tmnxMobGtpPriGrpFileClsMaxRecs,
       "tmnxMobGtpPriGrpFileObsoleteTime": tmnxMobGtpPriGrpFileObsoleteTime,
       "tmnxMobGtpPriGrpPrimaryCf": tmnxMobGtpPriGrpPrimaryCf,
       "tmnxMobGtpPriGrpCf1State": tmnxMobGtpPriGrpCf1State,
       "tmnxMobGtpPriGrpCf1Limit": tmnxMobGtpPriGrpCf1Limit,
       "tmnxMobGtpPriGrpCf2State": tmnxMobGtpPriGrpCf2State,
       "tmnxMobGtpPriGrpCf2Limit": tmnxMobGtpPriGrpCf2Limit,
       "tmnxMobGtpPriGrpCpmMemoryState": tmnxMobGtpPriGrpCpmMemoryState,
       "tmnxMobGtpPriGrpQueueSize": tmnxMobGtpPriGrpQueueSize,
       "tmnxMobGtpPriGrpAdminState": tmnxMobGtpPriGrpAdminState,
       "tmnxMobGtpPriGrpInactiveTimer": tmnxMobGtpPriGrpInactiveTimer,
       "tmnxMobGtpPriServerTable": tmnxMobGtpPriServerTable,
       "tmnxMobGtpPriServerEntry": tmnxMobGtpPriServerEntry,
       "tmnxMobGtpPriServerIndex": tmnxMobGtpPriServerIndex,
       "tmnxMobGtpPriServerRowStatus": tmnxMobGtpPriServerRowStatus,
       "tmnxMobGtpPriServerLastChngd": tmnxMobGtpPriServerLastChngd,
       "tmnxMobGtpPriServerAdminState": tmnxMobGtpPriServerAdminState,
       "tmnxMobGtpPriServerAddrType": tmnxMobGtpPriServerAddrType,
       "tmnxMobGtpPriServerAddr": tmnxMobGtpPriServerAddr,
       "tmnxMobGtpPriServerPort": tmnxMobGtpPriServerPort,
       "tmnxMobGtpPriServerRetries": tmnxMobGtpPriServerRetries,
       "tmnxMobGtpPriServerTimeout": tmnxMobGtpPriServerTimeout,
       "tmnxMobGtpPriServerEchoInterval": tmnxMobGtpPriServerEchoInterval,
       "tmnxMobGtpPriServerMaxRequests": tmnxMobGtpPriServerMaxRequests,
       "tmnxMobGtpPriServerNodeAlive": tmnxMobGtpPriServerNodeAlive,
       "tmnxMobGtpPriServerPriority": tmnxMobGtpPriServerPriority,
       "tmnxMobGtpPriServerPathProtocol": tmnxMobGtpPriServerPathProtocol,
       "tmnxMobUmtsQosPolTable": tmnxMobUmtsQosPolTable,
       "tmnxMobUmtsQosPolEntry": tmnxMobUmtsQosPolEntry,
       "tmnxMobUmtsQosPolName": tmnxMobUmtsQosPolName,
       "tmnxMobUmtsQosPolRowStatus": tmnxMobUmtsQosPolRowStatus,
       "tmnxMobUmtsQosPolLastChanged": tmnxMobUmtsQosPolLastChanged,
       "tmnxMobUmtsQosPolConvSpeechQci": tmnxMobUmtsQosPolConvSpeechQci,
       "tmnxMobUmtsQosPolConvUnkTdg": tmnxMobUmtsQosPolConvUnkTdg,
       "tmnxMobUmtsQosPolConvUnkTdl": tmnxMobUmtsQosPolConvUnkTdl,
       "tmnxMobUmtsQosPolStreamQciValue": tmnxMobUmtsQosPolStreamQciValue,
       "tmnxMobUmtsQosPolInterSigP1Qci": tmnxMobUmtsQosPolInterSigP1Qci,
       "tmnxMobUmtsQosPolInterP1Qci": tmnxMobUmtsQosPolInterP1Qci,
       "tmnxMobUmtsQosPolInterP2Qci": tmnxMobUmtsQosPolInterP2Qci,
       "tmnxMobUmtsQosPolInterP3Qci": tmnxMobUmtsQosPolInterP3Qci,
       "tmnxMobUmtsQosPolBackground": tmnxMobUmtsQosPolBackground,
       "tmnxMobProfRadTable": tmnxMobProfRadTable,
       "tmnxMobProfRadEntry": tmnxMobProfRadEntry,
       "tmnxMobProfRadName": tmnxMobProfRadName,
       "tmnxMobProfRadRowStatus": tmnxMobProfRadRowStatus,
       "tmnxMobProfRadLastChanged": tmnxMobProfRadLastChanged,
       "tmnxMobProfRadDescription": tmnxMobProfRadDescription,
       "tmnxMobProfRadAuthProbeInt": tmnxMobProfRadAuthProbeInt,
       "tmnxMobProfRadServerDeadTime": tmnxMobProfRadServerDeadTime,
       "tmnxMobProfRadRetryTimeout": tmnxMobProfRadRetryTimeout,
       "tmnxMobProfRadRetryCount": tmnxMobProfRadRetryCount,
       "tmnxMobProfRadGrpTable": tmnxMobProfRadGrpTable,
       "tmnxMobProfRadGrpEntry": tmnxMobProfRadGrpEntry,
       "tmnxMobProfRadGrpName": tmnxMobProfRadGrpName,
       "tmnxMobProfRadGrpRowStatus": tmnxMobProfRadGrpRowStatus,
       "tmnxMobProfRadGrpLastChanged": tmnxMobProfRadGrpLastChanged,
       "tmnxMobProfRadGrpDescription": tmnxMobProfRadGrpDescription,
       "tmnxMobProfRadGrpIfVRtrId": tmnxMobProfRadGrpIfVRtrId,
       "tmnxMobProfRadGrpIfIndex": tmnxMobProfRadGrpIfIndex,
       "tmnxMobProfRadGrpAuthServerPort": tmnxMobProfRadGrpAuthServerPort,
       "tmnxMobProfRadGrpAcctServerPort": tmnxMobProfRadGrpAcctServerPort,
       "tmnxMobProfRadGrpSecret": tmnxMobProfRadGrpSecret,
       "tmnxMobProfRadGrpIntUpdateIntvl": tmnxMobProfRadGrpIntUpdateIntvl,
       "tmnxMobProfRadGrpServerType": tmnxMobProfRadGrpServerType,
       "tmnxMobProfRadGrpRadiusProfile": tmnxMobProfRadGrpRadiusProfile,
       "tmnxMobProfRadGrpIgnAcctResp": tmnxMobProfRadGrpIgnAcctResp,
       "tmnxMobProfRadPeerTable": tmnxMobProfRadPeerTable,
       "tmnxMobProfRadPeerEntry": tmnxMobProfRadPeerEntry,
       "tmnxMobProfRadPeerIndex": tmnxMobProfRadPeerIndex,
       "tmnxMobProfRadPeerRowStatus": tmnxMobProfRadPeerRowStatus,
       "tmnxMobProfRadPeerLastChngd": tmnxMobProfRadPeerLastChngd,
       "tmnxMobProfRadPeerAdminState": tmnxMobProfRadPeerAdminState,
       "tmnxMobProfRadPeerAddrType": tmnxMobProfRadPeerAddrType,
       "tmnxMobProfRadPeerAddr": tmnxMobProfRadPeerAddr,
       "tmnxMobProfRadPeerPriority": tmnxMobProfRadPeerPriority,
       "tmnxMobProfRadPeerAuthSvrPort": tmnxMobProfRadPeerAuthSvrPort,
       "tmnxMobProfRadPeerAcctSvrPort": tmnxMobProfRadPeerAcctSvrPort,
       "tmnxMobProfRadPeerSecret": tmnxMobProfRadPeerSecret,
       "tmnxMobProfRadPeerRadProfile": tmnxMobProfRadPeerRadProfile,
       "tmnxMobProfDccaTable": tmnxMobProfDccaTable,
       "tmnxMobProfDccaEntry": tmnxMobProfDccaEntry,
       "tmnxMobProfDccaName": tmnxMobProfDccaName,
       "tmnxMobProfDccaRowStatus": tmnxMobProfDccaRowStatus,
       "tmnxMobProfDccaLastChanged": tmnxMobProfDccaLastChanged,
       "tmnxMobProfDccaDescription": tmnxMobProfDccaDescription,
       "tmnxMobProfDccaApplTxTimer": tmnxMobProfDccaApplTxTimer,
       "tmnxMobProfDccaRetryCnt": tmnxMobProfDccaRetryCnt,
       "tmnxMobProfDcca3GppQosNegProf": tmnxMobProfDcca3GppQosNegProf,
       "tmnxMobProfDccaQosInformation": tmnxMobProfDccaQosInformation,
       "tmnxMobProfDccaCalledStationId": tmnxMobProfDccaCalledStationId,
       "tmnxMobProfDccaCcSessFailover": tmnxMobProfDccaCcSessFailover,
       "tmnxMobProfDccaCcSessFlovrHndl": tmnxMobProfDccaCcSessFlovrHndl,
       "tmnxMobProfDccaForcedReAuth": tmnxMobProfDccaForcedReAuth,
       "tmnxMobProfDccaQuotaExNoThrsld": tmnxMobProfDccaQuotaExNoThrsld,
       "tmnxMobProfDccaQuotaExThrsldAct": tmnxMobProfDccaQuotaExThrsldAct,
       "tmnxMobProfDccaQuotaUnavail": tmnxMobProfDccaQuotaUnavail,
       "tmnxMobProfDccaRatingCondtChng": tmnxMobProfDccaRatingCondtChng,
       "tmnxMobProfDccaValidityTimeExp": tmnxMobProfDccaValidityTimeExp,
       "tmnxMobProfDccaFhSessContTimer": tmnxMobProfDccaFhSessContTimer,
       "tmnxMobProfDccaDefaultQht": tmnxMobProfDccaDefaultQht,
       "tmnxMobProfDccaFirstPktBehavior": tmnxMobProfDccaFirstPktBehavior,
       "tmnxMobProfPolUnitTable": tmnxMobProfPolUnitTable,
       "tmnxMobProfPolUnitEntry": tmnxMobProfPolUnitEntry,
       "tmnxMobProfPolUnitName": tmnxMobProfPolUnitName,
       "tmnxMobProfPolUnitRowStatus": tmnxMobProfPolUnitRowStatus,
       "tmnxMobProfPolUnitLastChanged": tmnxMobProfPolUnitLastChanged,
       "tmnxMobProfPolUnitUplinkGbrRate": tmnxMobProfPolUnitUplinkGbrRate,
       "tmnxMobProfPolUnitUplinkMbrRate": tmnxMobProfPolUnitUplinkMbrRate,
       "tmnxMobProfPolUnitDwnlinkGbrRate": tmnxMobProfPolUnitDwnlinkGbrRate,
       "tmnxMobProfPolUnitDwnlinkMbrRate": tmnxMobProfPolUnitDwnlinkMbrRate,
       "tmnxMobProfPolUntFlwGateStatus": tmnxMobProfPolUntFlwGateStatus,
       "tmnxMobProfPolUntRedirectAdrType": tmnxMobProfPolUntRedirectAdrType,
       "tmnxMobProfPolUntRedirectAddr": tmnxMobProfPolUntRedirectAddr,
       "tmnxMobProfPolUntInUse": tmnxMobProfPolUntInUse,
       "tmnxMobProfPolUntRefCount": tmnxMobProfPolUntRefCount,
       "tmnxMobProfChgUnitTable": tmnxMobProfChgUnitTable,
       "tmnxMobProfChgUnitEntry": tmnxMobProfChgUnitEntry,
       "tmnxMobProfChgUnitName": tmnxMobProfChgUnitName,
       "tmnxMobProfChgUnitRowStatus": tmnxMobProfChgUnitRowStatus,
       "tmnxMobProfChgUnitLastChanged": tmnxMobProfChgUnitLastChanged,
       "tmnxMobProfChgUnitRatingGroup": tmnxMobProfChgUnitRatingGroup,
       "tmnxMobProfChgUnitServIdentifier": tmnxMobProfChgUnitServIdentifier,
       "tmnxMobProfChgUnitReportingLevel": tmnxMobProfChgUnitReportingLevel,
       "tmnxMobProfChgUnitChargingMethod": tmnxMobProfChgUnitChargingMethod,
       "tmnxMobProfChgUnitMeteringMethod": tmnxMobProfChgUnitMeteringMethod,
       "tmnxMobProfChgUnitInUse": tmnxMobProfChgUnitInUse,
       "tmnxMobProfChgUnitRefCount": tmnxMobProfChgUnitRefCount,
       "tmnxMobProfHTTPRedirectTable": tmnxMobProfHTTPRedirectTable,
       "tmnxMobProfHTTPRedirectEntry": tmnxMobProfHTTPRedirectEntry,
       "tmnxMobProfHttpRedirectName": tmnxMobProfHttpRedirectName,
       "tmnxMobProfHttpRedirectRowStatus": tmnxMobProfHttpRedirectRowStatus,
       "tmnxMobProfHttpRedirectLstChgd": tmnxMobProfHttpRedirectLstChgd,
       "tmnxMobProfHttpRedirctPrecedence": tmnxMobProfHttpRedirctPrecedence,
       "tmnxMobProfileGlobalObjs": tmnxMobProfileGlobalObjs,
       "tmnxMobProfSysTblLstChgd": tmnxMobProfSysTblLstChgd,
       "tmnxMobProfDiaTblLstChgd": tmnxMobProfDiaTblLstChgd,
       "tmnxMobProfDiaPeerTblLstChgd": tmnxMobProfDiaPeerTblLstChgd,
       "tmnxMobProfDiaPeerListTblLstChgd": tmnxMobProfDiaPeerListTblLstChgd,
       "tmnxMobProfPmipv6TblLstChgd": tmnxMobProfPmipv6TblLstChgd,
       "tmnxMobProfGtpTblLstChgd": tmnxMobProfGtpTblLstChgd,
       "tmnxMobProfPlmnListTblLstChgd": tmnxMobProfPlmnListTblLstChgd,
       "tmnxMobProfPolTblLstChgd": tmnxMobProfPolTblLstChgd,
       "tmnxMobProfPolUntFlowTblLstChgd": tmnxMobProfPolUntFlowTblLstChgd,
       "tmnxMobProfPolBaseTblLstChgd": tmnxMobProfPolBaseTblLstChgd,
       "tmnxMobProfQciPolTblLstChgd": tmnxMobProfQciPolTblLstChgd,
       "tmnxMobProfQciPolQciTblLstChgd": tmnxMobProfQciPolQciTblLstChgd,
       "tmnxMobProfPeerListTblLstChgd": tmnxMobProfPeerListTblLstChgd,
       "tmnxMobProfPeerListPeerTblLtCgd": tmnxMobProfPeerListPeerTblLtCgd,
       "tmnxMobProfSgwChargingTblLstChgd": tmnxMobProfSgwChargingTblLstChgd,
       "tmnxMobProfPgwChargingTblLstChgd": tmnxMobProfPgwChargingTblLstChgd,
       "tmnxMobGtpPriGrpTblLstChgd": tmnxMobGtpPriGrpTblLstChgd,
       "tmnxMobGtpPriServerTblLstChgd": tmnxMobGtpPriServerTblLstChgd,
       "tmnxMobUmtsQosPolTblLstChgd": tmnxMobUmtsQosPolTblLstChgd,
       "tmnxMobProfRadTblLstChgd": tmnxMobProfRadTblLstChgd,
       "tmnxMobProfRadGrpTblLstChgd": tmnxMobProfRadGrpTblLstChgd,
       "tmnxMobProfRadPeerTblLstChgd": tmnxMobProfRadPeerTblLstChgd,
       "tmnxMobProfDccaTblLstChgd": tmnxMobProfDccaTblLstChgd,
       "tmnxMobProfPolUnitTblLstChgd": tmnxMobProfPolUnitTblLstChgd,
       "tmnxMobProfChgUnitTblLstChgd": tmnxMobProfChgUnitTblLstChgd,
       "tmnxMobProfHTTPRedirctTblLstChgd": tmnxMobProfHTTPRedirctTblLstChgd}
)
