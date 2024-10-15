# SNMP MIB module (CISCO-MEGACO-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEGACO-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:56 2024
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

(Counter32SinceReset,) = mibBuilder.importSymbols(
    "CISCO-ATM-TRUNK-MIB",
    "Counter32SinceReset")

(cmedGatewayConfigEntry,
 cmedGatewayId,
 cmedGatewayLinkId,
 cmedGatewayStatsEntry,
 cmedTerminationsEntry) = mibBuilder.importSymbols(
    "CISCO-IETF-MEGACO-MIB",
    "cmedGatewayConfigEntry",
    "cmedGatewayId",
    "cmedGatewayLinkId",
    "cmedGatewayStatsEntry",
    "cmedTerminationsEntry")

(CCallControlProfileIndex,
 CCallControlProfileIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlProfileIndex",
    "CCallControlProfileIndexOrZero")

(CMgcGroupIndex,) = mibBuilder.importSymbols(
    "CISCO-MGC-MIB",
    "CMgcGroupIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(CvcSpeechCoderRate,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcSpeechCoderRate")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

ciscoMegacoExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104)
)
ciscoMegacoExtMIB.setRevisions(
        ("2006-08-29 12:00",
         "2006-04-21 12:00",
         "2005-11-03 12:00",
         "2005-04-25 12:00",
         "2004-06-03 12:00",
         "2003-10-13 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CH248Packages(Bits, TextualConvention):
    status = "current"


class CMedxCotTones(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co1", 1),
          ("co2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMegacoExtMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoMegacoExtMIBNotifications = _CiscoMegacoExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 0)
)
_CiscoMegacoExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMegacoExtMIBObjects = _CiscoMegacoExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1)
)
_CmedxConfig_ObjectIdentity = ObjectIdentity
cmedxConfig = _CmedxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1)
)
_CmedxGatewayConfigTable_Object = MibTable
cmedxGatewayConfigTable = _CmedxGatewayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmedxGatewayConfigTable.setStatus("current")
_CmedxGatewayConfigEntry_Object = MibTableRow
cmedxGatewayConfigEntry = _CmedxGatewayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmedxGatewayConfigEntry.setStatus("current")
_CmedxGatewayMgcGroupIndex_Type = CMgcGroupIndex
_CmedxGatewayMgcGroupIndex_Object = MibTableColumn
cmedxGatewayMgcGroupIndex = _CmedxGatewayMgcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 1),
    _CmedxGatewayMgcGroupIndex_Type()
)
cmedxGatewayMgcGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgcGroupIndex.setStatus("current")


class _CmedxGatewayIpAddressIndex_Type(Unsigned32):
    """Custom type cmedxGatewayIpAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CmedxGatewayIpAddressIndex_Type.__name__ = "Unsigned32"
_CmedxGatewayIpAddressIndex_Object = MibTableColumn
cmedxGatewayIpAddressIndex = _CmedxGatewayIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 2),
    _CmedxGatewayIpAddressIndex_Type()
)
cmedxGatewayIpAddressIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayIpAddressIndex.setStatus("current")


class _CmedxGatewayAssociationId_Type(Unsigned32):
    """Custom type cmedxGatewayAssociationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmedxGatewayAssociationId_Type.__name__ = "Unsigned32"
_CmedxGatewayAssociationId_Object = MibTableColumn
cmedxGatewayAssociationId = _CmedxGatewayAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 3),
    _CmedxGatewayAssociationId_Type()
)
cmedxGatewayAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayAssociationId.setStatus("current")


class _CmedxGatewayMaxContexts_Type(Unsigned32):
    """Custom type cmedxGatewayMaxContexts based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CmedxGatewayMaxContexts_Type.__name__ = "Unsigned32"
_CmedxGatewayMaxContexts_Object = MibTableColumn
cmedxGatewayMaxContexts = _CmedxGatewayMaxContexts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 4),
    _CmedxGatewayMaxContexts_Type()
)
cmedxGatewayMaxContexts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMaxContexts.setStatus("current")


class _CmedxGatewayMaxTermsInContext_Type(Unsigned32):
    """Custom type cmedxGatewayMaxTermsInContext based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmedxGatewayMaxTermsInContext_Type.__name__ = "Unsigned32"
_CmedxGatewayMaxTermsInContext_Object = MibTableColumn
cmedxGatewayMaxTermsInContext = _CmedxGatewayMaxTermsInContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 5),
    _CmedxGatewayMaxTermsInContext_Type()
)
cmedxGatewayMaxTermsInContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMaxTermsInContext.setStatus("current")


class _CmedxGatewayMgExecTime_Type(Unsigned32):
    """Custom type cmedxGatewayMgExecTime based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgExecTime_Type.__name__ = "Unsigned32"
_CmedxGatewayMgExecTime_Object = MibTableColumn
cmedxGatewayMgExecTime = _CmedxGatewayMgExecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 6),
    _CmedxGatewayMgExecTime_Type()
)
cmedxGatewayMgExecTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgExecTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMgExecTime.setUnits("milliseconds")


class _CmedxGatewayMgcExecTime_Type(Unsigned32):
    """Custom type cmedxGatewayMgcExecTime based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgcExecTime_Type.__name__ = "Unsigned32"
_CmedxGatewayMgcExecTime_Object = MibTableColumn
cmedxGatewayMgcExecTime = _CmedxGatewayMgcExecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 7),
    _CmedxGatewayMgcExecTime_Type()
)
cmedxGatewayMgcExecTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgcExecTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMgcExecTime.setUnits("milliseconds")


class _CmedxGatewayProvisionRespTime_Type(Unsigned32):
    """Custom type cmedxGatewayProvisionRespTime based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayProvisionRespTime_Type.__name__ = "Unsigned32"
_CmedxGatewayProvisionRespTime_Object = MibTableColumn
cmedxGatewayProvisionRespTime = _CmedxGatewayProvisionRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 8),
    _CmedxGatewayProvisionRespTime_Type()
)
cmedxGatewayProvisionRespTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayProvisionRespTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmedxGatewayProvisionRespTime.setUnits("milliseconds")


class _CmedxGatewayNumConnRetries_Type(Unsigned32):
    """Custom type cmedxGatewayNumConnRetries based on Unsigned32"""
    defaultValue = 11

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmedxGatewayNumConnRetries_Type.__name__ = "Unsigned32"
_CmedxGatewayNumConnRetries_Object = MibTableColumn
cmedxGatewayNumConnRetries = _CmedxGatewayNumConnRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 9),
    _CmedxGatewayNumConnRetries_Type()
)
cmedxGatewayNumConnRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayNumConnRetries.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayNumConnRetries.setUnits("times")


class _CmedxGatewayMaxWaitingDelay_Type(Unsigned32):
    """Custom type cmedxGatewayMaxWaitingDelay based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CmedxGatewayMaxWaitingDelay_Type.__name__ = "Unsigned32"
_CmedxGatewayMaxWaitingDelay_Object = MibTableColumn
cmedxGatewayMaxWaitingDelay = _CmedxGatewayMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 10),
    _CmedxGatewayMaxWaitingDelay_Type()
)
cmedxGatewayMaxWaitingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMaxWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMaxWaitingDelay.setUnits("milliseconds")


class _CmedxGatewayRestartDelay_Type(Unsigned32):
    """Custom type cmedxGatewayRestartDelay based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CmedxGatewayRestartDelay_Type.__name__ = "Unsigned32"
_CmedxGatewayRestartDelay_Object = MibTableColumn
cmedxGatewayRestartDelay = _CmedxGatewayRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 11),
    _CmedxGatewayRestartDelay_Type()
)
cmedxGatewayRestartDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayRestartDelay.setUnits("milliseconds")


class _CmedxGatewayRespRetentionTime_Type(Unsigned32):
    """Custom type cmedxGatewayRespRetentionTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayRespRetentionTime_Type.__name__ = "Unsigned32"
_CmedxGatewayRespRetentionTime_Object = MibTableColumn
cmedxGatewayRespRetentionTime = _CmedxGatewayRespRetentionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 12),
    _CmedxGatewayRespRetentionTime_Type()
)
cmedxGatewayRespRetentionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayRespRetentionTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayRespRetentionTime.setUnits("seconds")


class _CmedxGatewayInitialRtt_Type(Unsigned32):
    """Custom type cmedxGatewayInitialRtt based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayInitialRtt_Type.__name__ = "Unsigned32"
_CmedxGatewayInitialRtt_Object = MibTableColumn
cmedxGatewayInitialRtt = _CmedxGatewayInitialRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 13),
    _CmedxGatewayInitialRtt_Type()
)
cmedxGatewayInitialRtt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayInitialRtt.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayInitialRtt.setUnits("milliseconds")


class _CmedxGatewayInactivityTime_Type(Unsigned32):
    """Custom type cmedxGatewayInactivityTime based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayInactivityTime_Type.__name__ = "Unsigned32"
_CmedxGatewayInactivityTime_Object = MibTableColumn
cmedxGatewayInactivityTime = _CmedxGatewayInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 14),
    _CmedxGatewayInactivityTime_Type()
)
cmedxGatewayInactivityTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayInactivityTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayInactivityTime.setUnits("10 milliseconds")


class _CmedxGatewayHeaderAddrType_Type(InetAddressType):
    """Custom type cmedxGatewayHeaderAddrType based on InetAddressType"""


_CmedxGatewayHeaderAddrType_Object = MibTableColumn
cmedxGatewayHeaderAddrType = _CmedxGatewayHeaderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 15),
    _CmedxGatewayHeaderAddrType_Type()
)
cmedxGatewayHeaderAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayHeaderAddrType.setStatus("current")


class _CmedxGatewayDownServiceDelay_Type(Integer32):
    """Custom type cmedxGatewayDownServiceDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CmedxGatewayDownServiceDelay_Type.__name__ = "Integer32"
_CmedxGatewayDownServiceDelay_Object = MibTableColumn
cmedxGatewayDownServiceDelay = _CmedxGatewayDownServiceDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 16),
    _CmedxGatewayDownServiceDelay_Type()
)
cmedxGatewayDownServiceDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayDownServiceDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayDownServiceDelay.setUnits("milliseconds")
_CmedxGatewayActiveMgcAddress_Type = InetAddress
_CmedxGatewayActiveMgcAddress_Object = MibTableColumn
cmedxGatewayActiveMgcAddress = _CmedxGatewayActiveMgcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 17),
    _CmedxGatewayActiveMgcAddress_Type()
)
cmedxGatewayActiveMgcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayActiveMgcAddress.setStatus("current")


class _CmedxGatewayActiveMgcDomain_Type(SnmpAdminString):
    """Custom type cmedxGatewayActiveMgcDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmedxGatewayActiveMgcDomain_Type.__name__ = "SnmpAdminString"
_CmedxGatewayActiveMgcDomain_Object = MibTableColumn
cmedxGatewayActiveMgcDomain = _CmedxGatewayActiveMgcDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 18),
    _CmedxGatewayActiveMgcDomain_Type()
)
cmedxGatewayActiveMgcDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayActiveMgcDomain.setStatus("current")
_CmedxGatewayActiveMgcPortNum_Type = CiscoPort
_CmedxGatewayActiveMgcPortNum_Object = MibTableColumn
cmedxGatewayActiveMgcPortNum = _CmedxGatewayActiveMgcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 19),
    _CmedxGatewayActiveMgcPortNum_Type()
)
cmedxGatewayActiveMgcPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayActiveMgcPortNum.setStatus("current")


class _CmedxGatewayStateChangeReason_Type(Integer32):
    """Custom type cmedxGatewayStateChangeReason based on Integer32"""
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
        *(("mgDirected", 2),
          ("mgcDirected", 1),
          ("mgcNotReachable", 3),
          ("numRetriesExpired", 4))
    )


_CmedxGatewayStateChangeReason_Type.__name__ = "Integer32"
_CmedxGatewayStateChangeReason_Object = MibTableColumn
cmedxGatewayStateChangeReason = _CmedxGatewayStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 20),
    _CmedxGatewayStateChangeReason_Type()
)
cmedxGatewayStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayStateChangeReason.setStatus("current")


class _CmedxGatewayStateChangeMethod_Type(Integer32):
    """Custom type cmedxGatewayStateChangeMethod based on Integer32"""
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
        *(("cancelGraceful", 8),
          ("disconnect", 7),
          ("failover", 5),
          ("forced", 3),
          ("graceful", 2),
          ("handoff", 4),
          ("other", 1),
          ("restart", 6))
    )


_CmedxGatewayStateChangeMethod_Type.__name__ = "Integer32"
_CmedxGatewayStateChangeMethod_Object = MibTableColumn
cmedxGatewayStateChangeMethod = _CmedxGatewayStateChangeMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 21),
    _CmedxGatewayStateChangeMethod_Type()
)
cmedxGatewayStateChangeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayStateChangeMethod.setStatus("current")


class _CmedxGatewayAdminAction_Type(Integer32):
    """Custom type cmedxGatewayAdminAction based on Integer32"""
    defaultValue = 2

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
        *(("cancelGraceful", 4),
          ("downForceful", 2),
          ("downGraceful", 3),
          ("up", 1))
    )


_CmedxGatewayAdminAction_Type.__name__ = "Integer32"
_CmedxGatewayAdminAction_Object = MibTableColumn
cmedxGatewayAdminAction = _CmedxGatewayAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 22),
    _CmedxGatewayAdminAction_Type()
)
cmedxGatewayAdminAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayAdminAction.setStatus("current")


class _CmedxGatewayServiceState_Type(Integer32):
    """Custom type cmedxGatewayServiceState based on Integer32"""
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
        *(("inService", 1),
          ("mgcDirectOos", 6),
          ("outOfService", 3),
          ("pendingFoos", 4),
          ("pendingGoos", 5),
          ("pendingIs", 2))
    )


_CmedxGatewayServiceState_Type.__name__ = "Integer32"
_CmedxGatewayServiceState_Object = MibTableColumn
cmedxGatewayServiceState = _CmedxGatewayServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 23),
    _CmedxGatewayServiceState_Type()
)
cmedxGatewayServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayServiceState.setStatus("current")


class _CmedxGatewayDynamicTpktVersion_Type(TruthValue):
    """Custom type cmedxGatewayDynamicTpktVersion based on TruthValue"""


_CmedxGatewayDynamicTpktVersion_Object = MibTableColumn
cmedxGatewayDynamicTpktVersion = _CmedxGatewayDynamicTpktVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 24),
    _CmedxGatewayDynamicTpktVersion_Type()
)
cmedxGatewayDynamicTpktVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayDynamicTpktVersion.setStatus("current")


class _CmedxGatewayMaxCommandMsgSize_Type(Unsigned32):
    """Custom type cmedxGatewayMaxCommandMsgSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CmedxGatewayMaxCommandMsgSize_Type.__name__ = "Unsigned32"
_CmedxGatewayMaxCommandMsgSize_Object = MibTableColumn
cmedxGatewayMaxCommandMsgSize = _CmedxGatewayMaxCommandMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 25),
    _CmedxGatewayMaxCommandMsgSize_Type()
)
cmedxGatewayMaxCommandMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMaxCommandMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMaxCommandMsgSize.setUnits("Kbyte")


class _CmedxGatewayMaxReplyMsgSize_Type(Unsigned32):
    """Custom type cmedxGatewayMaxReplyMsgSize based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CmedxGatewayMaxReplyMsgSize_Type.__name__ = "Unsigned32"
_CmedxGatewayMaxReplyMsgSize_Object = MibTableColumn
cmedxGatewayMaxReplyMsgSize = _CmedxGatewayMaxReplyMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 26),
    _CmedxGatewayMaxReplyMsgSize_Type()
)
cmedxGatewayMaxReplyMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMaxReplyMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMaxReplyMsgSize.setUnits("Kbyte")


class _CmedxGatewaySctpAssocId_Type(Unsigned32):
    """Custom type cmedxGatewaySctpAssocId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmedxGatewaySctpAssocId_Type.__name__ = "Unsigned32"
_CmedxGatewaySctpAssocId_Object = MibTableColumn
cmedxGatewaySctpAssocId = _CmedxGatewaySctpAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 27),
    _CmedxGatewaySctpAssocId_Type()
)
cmedxGatewaySctpAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewaySctpAssocId.setStatus("current")


class _CmedxGatewaySrvChgProfile_Type(SnmpAdminString):
    """Custom type cmedxGatewaySrvChgProfile based on SnmpAdminString"""
    defaultValue = OctetString("CISCO_TGW")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CmedxGatewaySrvChgProfile_Type.__name__ = "SnmpAdminString"
_CmedxGatewaySrvChgProfile_Object = MibTableColumn
cmedxGatewaySrvChgProfile = _CmedxGatewaySrvChgProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 28),
    _CmedxGatewaySrvChgProfile_Type()
)
cmedxGatewaySrvChgProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewaySrvChgProfile.setStatus("current")


class _CmedxGatewaySrvChgProfileVer_Type(Unsigned32):
    """Custom type cmedxGatewaySrvChgProfileVer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CmedxGatewaySrvChgProfileVer_Type.__name__ = "Unsigned32"
_CmedxGatewaySrvChgProfileVer_Object = MibTableColumn
cmedxGatewaySrvChgProfileVer = _CmedxGatewaySrvChgProfileVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 29),
    _CmedxGatewaySrvChgProfileVer_Type()
)
cmedxGatewaySrvChgProfileVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewaySrvChgProfileVer.setStatus("current")


class _CmedxGatewayMsgTokenType_Type(Integer32):
    """Custom type cmedxGatewayMsgTokenType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longFormat", 2),
          ("shortFormat", 1))
    )


_CmedxGatewayMsgTokenType_Type.__name__ = "Integer32"
_CmedxGatewayMsgTokenType_Object = MibTableColumn
cmedxGatewayMsgTokenType = _CmedxGatewayMsgTokenType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 30),
    _CmedxGatewayMsgTokenType_Type()
)
cmedxGatewayMsgTokenType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMsgTokenType.setStatus("current")


class _CmedxGatewayMgProvisionRspTime_Type(Unsigned32):
    """Custom type cmedxGatewayMgProvisionRspTime based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgProvisionRspTime_Type.__name__ = "Unsigned32"
_CmedxGatewayMgProvisionRspTime_Object = MibTableColumn
cmedxGatewayMgProvisionRspTime = _CmedxGatewayMgProvisionRspTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 31),
    _CmedxGatewayMgProvisionRspTime_Type()
)
cmedxGatewayMgProvisionRspTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgProvisionRspTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMgProvisionRspTime.setUnits("milliseconds")


class _CmedxGatewayMgcProvisionRspTime_Type(Unsigned32):
    """Custom type cmedxGatewayMgcProvisionRspTime based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgcProvisionRspTime_Type.__name__ = "Unsigned32"
_CmedxGatewayMgcProvisionRspTime_Object = MibTableColumn
cmedxGatewayMgcProvisionRspTime = _CmedxGatewayMgcProvisionRspTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 32),
    _CmedxGatewayMgcProvisionRspTime_Type()
)
cmedxGatewayMgcProvisionRspTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgcProvisionRspTime.setStatus("current")
if mibBuilder.loadTexts:
    cmedxGatewayMgcProvisionRspTime.setUnits("milliseconds")


class _CmedxGatewayMgOrigPendLimit_Type(Unsigned32):
    """Custom type cmedxGatewayMgOrigPendLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgOrigPendLimit_Type.__name__ = "Unsigned32"
_CmedxGatewayMgOrigPendLimit_Object = MibTableColumn
cmedxGatewayMgOrigPendLimit = _CmedxGatewayMgOrigPendLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 33),
    _CmedxGatewayMgOrigPendLimit_Type()
)
cmedxGatewayMgOrigPendLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgOrigPendLimit.setStatus("current")


class _CmedxGatewayMgcOrigPendLimit_Type(Unsigned32):
    """Custom type cmedxGatewayMgcOrigPendLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedxGatewayMgcOrigPendLimit_Type.__name__ = "Unsigned32"
_CmedxGatewayMgcOrigPendLimit_Object = MibTableColumn
cmedxGatewayMgcOrigPendLimit = _CmedxGatewayMgcOrigPendLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 34),
    _CmedxGatewayMgcOrigPendLimit_Type()
)
cmedxGatewayMgcOrigPendLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayMgcOrigPendLimit.setStatus("current")


class _CmedxGatewayDomainName_Type(SnmpAdminString):
    """Custom type cmedxGatewayDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmedxGatewayDomainName_Type.__name__ = "SnmpAdminString"
_CmedxGatewayDomainName_Object = MibTableColumn
cmedxGatewayDomainName = _CmedxGatewayDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 35),
    _CmedxGatewayDomainName_Type()
)
cmedxGatewayDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayDomainName.setStatus("current")


class _CmedxGatewayCmbDnAndPortInMID_Type(TruthValue):
    """Custom type cmedxGatewayCmbDnAndPortInMID based on TruthValue"""


_CmedxGatewayCmbDnAndPortInMID_Object = MibTableColumn
cmedxGatewayCmbDnAndPortInMID = _CmedxGatewayCmbDnAndPortInMID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 1, 1, 36),
    _CmedxGatewayCmbDnAndPortInMID_Type()
)
cmedxGatewayCmbDnAndPortInMID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxGatewayCmbDnAndPortInMID.setStatus("current")
_CmedxTerminationTypeTable_Object = MibTable
cmedxTerminationTypeTable = _CmedxTerminationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmedxTerminationTypeTable.setStatus("current")
_CmedxTerminationTypeEntry_Object = MibTableRow
cmedxTerminationTypeEntry = _CmedxTerminationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1)
)
cmedxTerminationTypeEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxTermTypeId"),
)
if mibBuilder.loadTexts:
    cmedxTerminationTypeEntry.setStatus("current")


class _CmedxTermTypeId_Type(Unsigned32):
    """Custom type cmedxTermTypeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmedxTermTypeId_Type.__name__ = "Unsigned32"
_CmedxTermTypeId_Object = MibTableColumn
cmedxTermTypeId = _CmedxTermTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1, 1),
    _CmedxTermTypeId_Type()
)
cmedxTermTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxTermTypeId.setStatus("current")


class _CmedxTermType_Type(Integer32):
    """Custom type cmedxTermType based on Integer32"""
    defaultValue = 3

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
        *(("pdnAtmAal1", 4),
          ("pdnAtmAal2", 5),
          ("pdnRtp", 3),
          ("scn", 2),
          ("unknown", 1))
    )


_CmedxTermType_Type.__name__ = "Integer32"
_CmedxTermType_Object = MibTableColumn
cmedxTermType = _CmedxTermType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1, 2),
    _CmedxTermType_Type()
)
cmedxTermType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxTermType.setStatus("current")


class _CmedxTermTypeProfileId_Type(CCallControlProfileIndexOrZero):
    """Custom type cmedxTermTypeProfileId based on CCallControlProfileIndexOrZero"""
    defaultValue = 0


_CmedxTermTypeProfileId_Object = MibTableColumn
cmedxTermTypeProfileId = _CmedxTermTypeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1, 3),
    _CmedxTermTypeProfileId_Type()
)
cmedxTermTypeProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxTermTypeProfileId.setStatus("current")
_CmedxTermTypePkgIds_Type = CH248Packages
_CmedxTermTypePkgIds_Object = MibTableColumn
cmedxTermTypePkgIds = _CmedxTermTypePkgIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1, 4),
    _CmedxTermTypePkgIds_Type()
)
cmedxTermTypePkgIds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxTermTypePkgIds.setStatus("current")
_CmedxTermTypeRowStatus_Type = RowStatus
_CmedxTermTypeRowStatus_Object = MibTableColumn
cmedxTermTypeRowStatus = _CmedxTermTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 2, 1, 5),
    _CmedxTermTypeRowStatus_Type()
)
cmedxTermTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxTermTypeRowStatus.setStatus("current")
_CmedxProfileTable_Object = MibTable
cmedxProfileTable = _CmedxProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cmedxProfileTable.setStatus("current")
_CmedxProfileEntry_Object = MibTableRow
cmedxProfileEntry = _CmedxProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1)
)
cmedxProfileEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxProfileIndex"),
)
if mibBuilder.loadTexts:
    cmedxProfileEntry.setStatus("current")
_CmedxProfileIndex_Type = CCallControlProfileIndex
_CmedxProfileIndex_Object = MibTableColumn
cmedxProfileIndex = _CmedxProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 1),
    _CmedxProfileIndex_Type()
)
cmedxProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxProfileIndex.setStatus("current")


class _CmedxProfilePlayCpToneInterDur_Type(Unsigned32):
    """Custom type cmedxProfilePlayCpToneInterDur based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfilePlayCpToneInterDur_Type.__name__ = "Unsigned32"
_CmedxProfilePlayCpToneInterDur_Object = MibTableColumn
cmedxProfilePlayCpToneInterDur = _CmedxProfilePlayCpToneInterDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 2),
    _CmedxProfilePlayCpToneInterDur_Type()
)
cmedxProfilePlayCpToneInterDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfilePlayCpToneInterDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfilePlayCpToneInterDur.setUnits("milliseconds")


class _CmedxProfileDtmfDigitOnDur_Type(Unsigned32):
    """Custom type cmedxProfileDtmfDigitOnDur based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 4294967295),
    )


_CmedxProfileDtmfDigitOnDur_Type.__name__ = "Unsigned32"
_CmedxProfileDtmfDigitOnDur_Object = MibTableColumn
cmedxProfileDtmfDigitOnDur = _CmedxProfileDtmfDigitOnDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 3),
    _CmedxProfileDtmfDigitOnDur_Type()
)
cmedxProfileDtmfDigitOnDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileDtmfDigitOnDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileDtmfDigitOnDur.setUnits("milliseconds")


class _CmedxProfileDtmfPauseDur_Type(Unsigned32):
    """Custom type cmedxProfileDtmfPauseDur based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 4294967295),
    )


_CmedxProfileDtmfPauseDur_Type.__name__ = "Unsigned32"
_CmedxProfileDtmfPauseDur_Object = MibTableColumn
cmedxProfileDtmfPauseDur = _CmedxProfileDtmfPauseDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 4),
    _CmedxProfileDtmfPauseDur_Type()
)
cmedxProfileDtmfPauseDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileDtmfPauseDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileDtmfPauseDur.setUnits("milliseconds")


class _CmedxProfileCot1Frequency_Type(Unsigned32):
    """Custom type cmedxProfileCot1Frequency based on Unsigned32"""
    defaultValue = 2010

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CmedxProfileCot1Frequency_Type.__name__ = "Unsigned32"
_CmedxProfileCot1Frequency_Object = MibTableColumn
cmedxProfileCot1Frequency = _CmedxProfileCot1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 5),
    _CmedxProfileCot1Frequency_Type()
)
cmedxProfileCot1Frequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileCot1Frequency.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileCot1Frequency.setUnits("Hz")


class _CmedxProfileCot2Frequency_Type(Unsigned32):
    """Custom type cmedxProfileCot2Frequency based on Unsigned32"""
    defaultValue = 1780

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CmedxProfileCot2Frequency_Type.__name__ = "Unsigned32"
_CmedxProfileCot2Frequency_Object = MibTableColumn
cmedxProfileCot2Frequency = _CmedxProfileCot2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 6),
    _CmedxProfileCot2Frequency_Type()
)
cmedxProfileCot2Frequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileCot2Frequency.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileCot2Frequency.setUnits("Hz")


class _CmedxProfileInitiateCotDur_Type(Unsigned32):
    """Custom type cmedxProfileInitiateCotDur based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfileInitiateCotDur_Type.__name__ = "Unsigned32"
_CmedxProfileInitiateCotDur_Object = MibTableColumn
cmedxProfileInitiateCotDur = _CmedxProfileInitiateCotDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 7),
    _CmedxProfileInitiateCotDur_Type()
)
cmedxProfileInitiateCotDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileInitiateCotDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileInitiateCotDur.setUnits("milliseconds")


class _CmedxProfileRespCotMethod_Type(Integer32):
    """Custom type cmedxProfileRespCotMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("transponder", 2))
    )


_CmedxProfileRespCotMethod_Type.__name__ = "Integer32"
_CmedxProfileRespCotMethod_Object = MibTableColumn
cmedxProfileRespCotMethod = _CmedxProfileRespCotMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 8),
    _CmedxProfileRespCotMethod_Type()
)
cmedxProfileRespCotMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileRespCotMethod.setStatus("current")


class _CmedxProfileDetectLongCpToneDur_Type(Unsigned32):
    """Custom type cmedxProfileDetectLongCpToneDur based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfileDetectLongCpToneDur_Type.__name__ = "Unsigned32"
_CmedxProfileDetectLongCpToneDur_Object = MibTableColumn
cmedxProfileDetectLongCpToneDur = _CmedxProfileDetectLongCpToneDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 9),
    _CmedxProfileDetectLongCpToneDur_Type()
)
cmedxProfileDetectLongCpToneDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileDetectLongCpToneDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileDetectLongCpToneDur.setUnits("milliseconds")


class _CmedxProfileDetectLongDigitDur_Type(Unsigned32):
    """Custom type cmedxProfileDetectLongDigitDur based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfileDetectLongDigitDur_Type.__name__ = "Unsigned32"
_CmedxProfileDetectLongDigitDur_Object = MibTableColumn
cmedxProfileDetectLongDigitDur = _CmedxProfileDetectLongDigitDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 10),
    _CmedxProfileDetectLongDigitDur_Type()
)
cmedxProfileDetectLongDigitDur.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileDetectLongDigitDur.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileDetectLongDigitDur.setUnits("milliseconds")


class _CmedxProfileEchoCancelEnabled_Type(TruthValue):
    """Custom type cmedxProfileEchoCancelEnabled based on TruthValue"""


_CmedxProfileEchoCancelEnabled_Object = MibTableColumn
cmedxProfileEchoCancelEnabled = _CmedxProfileEchoCancelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 11),
    _CmedxProfileEchoCancelEnabled_Type()
)
cmedxProfileEchoCancelEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileEchoCancelEnabled.setStatus("current")


class _CmedxProfileEchoCancelTail_Type(Integer32):
    """Custom type cmedxProfileEchoCancelTail based on Integer32"""
    defaultValue = 1

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
        *(("echoCanceller128ms", 6),
          ("echoCanceller16ms", 2),
          ("echoCanceller24ms", 3),
          ("echoCanceller32ms", 4),
          ("echoCanceller64ms", 5),
          ("echoCanceller8ms", 1))
    )


_CmedxProfileEchoCancelTail_Type.__name__ = "Integer32"
_CmedxProfileEchoCancelTail_Object = MibTableColumn
cmedxProfileEchoCancelTail = _CmedxProfileEchoCancelTail_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 12),
    _CmedxProfileEchoCancelTail_Type()
)
cmedxProfileEchoCancelTail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileEchoCancelTail.setStatus("current")


class _CmedxProfileInGainControl_Type(Integer32):
    """Custom type cmedxProfileInGainControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 14),
    )


_CmedxProfileInGainControl_Type.__name__ = "Integer32"
_CmedxProfileInGainControl_Object = MibTableColumn
cmedxProfileInGainControl = _CmedxProfileInGainControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 13),
    _CmedxProfileInGainControl_Type()
)
cmedxProfileInGainControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileInGainControl.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileInGainControl.setUnits("dB")


class _CmedxProfileOutAttnControl_Type(Unsigned32):
    """Custom type cmedxProfileOutAttnControl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CmedxProfileOutAttnControl_Type.__name__ = "Unsigned32"
_CmedxProfileOutAttnControl_Object = MibTableColumn
cmedxProfileOutAttnControl = _CmedxProfileOutAttnControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 14),
    _CmedxProfileOutAttnControl_Type()
)
cmedxProfileOutAttnControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileOutAttnControl.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileOutAttnControl.setUnits("dB")


class _CmedxProfileVoIpVadEnabled_Type(TruthValue):
    """Custom type cmedxProfileVoIpVadEnabled based on TruthValue"""


_CmedxProfileVoIpVadEnabled_Object = MibTableColumn
cmedxProfileVoIpVadEnabled = _CmedxProfileVoIpVadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 15),
    _CmedxProfileVoIpVadEnabled_Type()
)
cmedxProfileVoIpVadEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileVoIpVadEnabled.setStatus("current")


class _CmedxProfileVoIpVadTimer_Type(Unsigned32):
    """Custom type cmedxProfileVoIpVadTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfileVoIpVadTimer_Type.__name__ = "Unsigned32"
_CmedxProfileVoIpVadTimer_Object = MibTableColumn
cmedxProfileVoIpVadTimer = _CmedxProfileVoIpVadTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 16),
    _CmedxProfileVoIpVadTimer_Type()
)
cmedxProfileVoIpVadTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileVoIpVadTimer.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileVoIpVadTimer.setUnits("milliseconds")


class _CmedxProfileVoAal2VadTimer_Type(Unsigned32):
    """Custom type cmedxProfileVoAal2VadTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmedxProfileVoAal2VadTimer_Type.__name__ = "Unsigned32"
_CmedxProfileVoAal2VadTimer_Object = MibTableColumn
cmedxProfileVoAal2VadTimer = _CmedxProfileVoAal2VadTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 17),
    _CmedxProfileVoAal2VadTimer_Type()
)
cmedxProfileVoAal2VadTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileVoAal2VadTimer.setStatus("current")
if mibBuilder.loadTexts:
    cmedxProfileVoAal2VadTimer.setUnits("milliseconds")


class _CmedxProfileAtmBearerType_Type(Integer32):
    """Custom type cmedxProfileAtmBearerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bearerPvc", 2),
          ("bearerSvc", 1))
    )


_CmedxProfileAtmBearerType_Type.__name__ = "Integer32"
_CmedxProfileAtmBearerType_Object = MibTableColumn
cmedxProfileAtmBearerType = _CmedxProfileAtmBearerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 18),
    _CmedxProfileAtmBearerType_Type()
)
cmedxProfileAtmBearerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileAtmBearerType.setStatus("current")


class _CmedxProfileAtmAalPartialFill_Type(Unsigned32):
    """Custom type cmedxProfileAtmAalPartialFill based on Unsigned32"""
    defaultValue = 47

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CmedxProfileAtmAalPartialFill_Type.__name__ = "Unsigned32"
_CmedxProfileAtmAalPartialFill_Object = MibTableColumn
cmedxProfileAtmAalPartialFill = _CmedxProfileAtmAalPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 19),
    _CmedxProfileAtmAalPartialFill_Type()
)
cmedxProfileAtmAalPartialFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileAtmAalPartialFill.setStatus("current")


class _CmedxProfileAtmAalType_Type(Integer32):
    """Custom type cmedxProfileAtmAalType based on Integer32"""
    defaultValue = 3

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
        *(("aal1", 2),
          ("aal1Sdt", 3),
          ("aal1Udt", 4),
          ("aal2", 5),
          ("other", 1))
    )


_CmedxProfileAtmAalType_Type.__name__ = "Integer32"
_CmedxProfileAtmAalType_Object = MibTableColumn
cmedxProfileAtmAalType = _CmedxProfileAtmAalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 20),
    _CmedxProfileAtmAalType_Type()
)
cmedxProfileAtmAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileAtmAalType.setStatus("current")


class _CmedxProfileSuppressBearerDigit_Type(TruthValue):
    """Custom type cmedxProfileSuppressBearerDigit based on TruthValue"""


_CmedxProfileSuppressBearerDigit_Object = MibTableColumn
cmedxProfileSuppressBearerDigit = _CmedxProfileSuppressBearerDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 21),
    _CmedxProfileSuppressBearerDigit_Type()
)
cmedxProfileSuppressBearerDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileSuppressBearerDigit.setStatus("current")
_CmedxProfileRowStatus_Type = RowStatus
_CmedxProfileRowStatus_Object = MibTableColumn
cmedxProfileRowStatus = _CmedxProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 22),
    _CmedxProfileRowStatus_Type()
)
cmedxProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileRowStatus.setStatus("current")
_CmedxProfileOriginatingCotTx_Type = CMedxCotTones
_CmedxProfileOriginatingCotTx_Object = MibTableColumn
cmedxProfileOriginatingCotTx = _CmedxProfileOriginatingCotTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 23),
    _CmedxProfileOriginatingCotTx_Type()
)
cmedxProfileOriginatingCotTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileOriginatingCotTx.setStatus("current")
_CmedxProfileOriginatingCotRx_Type = CMedxCotTones
_CmedxProfileOriginatingCotRx_Object = MibTableColumn
cmedxProfileOriginatingCotRx = _CmedxProfileOriginatingCotRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 24),
    _CmedxProfileOriginatingCotRx_Type()
)
cmedxProfileOriginatingCotRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileOriginatingCotRx.setStatus("current")
_CmedxProfileTerminatingCotTx_Type = CMedxCotTones
_CmedxProfileTerminatingCotTx_Object = MibTableColumn
cmedxProfileTerminatingCotTx = _CmedxProfileTerminatingCotTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 25),
    _CmedxProfileTerminatingCotTx_Type()
)
cmedxProfileTerminatingCotTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileTerminatingCotTx.setStatus("current")
_CmedxProfileTerminatingCotRx_Type = CMedxCotTones
_CmedxProfileTerminatingCotRx_Object = MibTableColumn
cmedxProfileTerminatingCotRx = _CmedxProfileTerminatingCotRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 26),
    _CmedxProfileTerminatingCotRx_Type()
)
cmedxProfileTerminatingCotRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileTerminatingCotRx.setStatus("current")


class _CmedxProfileComfortNoiseGenerate_Type(Integer32):
    """Custom type cmedxProfileComfortNoiseGenerate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711A2", 3),
          ("none", 1),
          ("simple", 2))
    )


_CmedxProfileComfortNoiseGenerate_Type.__name__ = "Integer32"
_CmedxProfileComfortNoiseGenerate_Object = MibTableColumn
cmedxProfileComfortNoiseGenerate = _CmedxProfileComfortNoiseGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 3, 1, 27),
    _CmedxProfileComfortNoiseGenerate_Type()
)
cmedxProfileComfortNoiseGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedxProfileComfortNoiseGenerate.setStatus("current")
_CmedxCallReduceControlTable_Object = MibTable
cmedxCallReduceControlTable = _CmedxCallReduceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cmedxCallReduceControlTable.setStatus("current")
_CmedxCallReduceControlEntry_Object = MibTableRow
cmedxCallReduceControlEntry = _CmedxCallReduceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1)
)
cmedxCallReduceControlEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
)
if mibBuilder.loadTexts:
    cmedxCallReduceControlEntry.setStatus("current")


class _CmedxCallCongEnabled_Type(TruthValue):
    """Custom type cmedxCallCongEnabled based on TruthValue"""


_CmedxCallCongEnabled_Object = MibTableColumn
cmedxCallCongEnabled = _CmedxCallCongEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 1),
    _CmedxCallCongEnabled_Type()
)
cmedxCallCongEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxCallCongEnabled.setStatus("current")


class _CmedxCallRenotifInterval_Type(Unsigned32):
    """Custom type cmedxCallRenotifInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmedxCallRenotifInterval_Type.__name__ = "Unsigned32"
_CmedxCallRenotifInterval_Object = MibTableColumn
cmedxCallRenotifInterval = _CmedxCallRenotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 2),
    _CmedxCallRenotifInterval_Type()
)
cmedxCallRenotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxCallRenotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCallRenotifInterval.setUnits("seconds")


class _CmedxCRRNumOfLevel_Type(Unsigned32):
    """Custom type cmedxCRRNumOfLevel based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmedxCRRNumOfLevel_Type.__name__ = "Unsigned32"
_CmedxCRRNumOfLevel_Object = MibTableColumn
cmedxCRRNumOfLevel = _CmedxCRRNumOfLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 3),
    _CmedxCRRNumOfLevel_Type()
)
cmedxCRRNumOfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxCRRNumOfLevel.setStatus("current")


class _CmedxCurrentCRR_Type(Unsigned32):
    """Custom type cmedxCurrentCRR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmedxCurrentCRR_Type.__name__ = "Unsigned32"
_CmedxCurrentCRR_Object = MibTableColumn
cmedxCurrentCRR = _CmedxCurrentCRR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 4),
    _CmedxCurrentCRR_Type()
)
cmedxCurrentCRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCurrentCRR.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCurrentCRR.setUnits("percent")
_CmedxCrrNotifyState_Type = TruthValue
_CmedxCrrNotifyState_Object = MibTableColumn
cmedxCrrNotifyState = _CmedxCrrNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 5),
    _CmedxCrrNotifyState_Type()
)
cmedxCrrNotifyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCrrNotifyState.setStatus("current")


class _CmedxCrrNotifyEnabled_Type(OctetString):
    """Custom type cmedxCrrNotifyEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CmedxCrrNotifyEnabled_Type.__name__ = "OctetString"
_CmedxCrrNotifyEnabled_Object = MibTableColumn
cmedxCrrNotifyEnabled = _CmedxCrrNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 6),
    _CmedxCrrNotifyEnabled_Type()
)
cmedxCrrNotifyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCrrNotifyEnabled.setStatus("current")


class _CmedxCurrentCallState_Type(Integer32):
    """Custom type cmedxCurrentCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptCall", 1),
          ("dropCall", 2))
    )


_CmedxCurrentCallState_Type.__name__ = "Integer32"
_CmedxCurrentCallState_Object = MibTableColumn
cmedxCurrentCallState = _CmedxCurrentCallState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 4, 1, 7),
    _CmedxCurrentCallState_Type()
)
cmedxCurrentCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCurrentCallState.setStatus("current")
_CmedxCallReduceLevelTable_Object = MibTable
cmedxCallReduceLevelTable = _CmedxCallReduceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cmedxCallReduceLevelTable.setStatus("current")
_CmedxCallReduceLevelEntry_Object = MibTableRow
cmedxCallReduceLevelEntry = _CmedxCallReduceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 5, 1)
)
cmedxCallReduceLevelEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxCallReduceLevelNum"),
)
if mibBuilder.loadTexts:
    cmedxCallReduceLevelEntry.setStatus("current")


class _CmedxCallReduceLevelNum_Type(Unsigned32):
    """Custom type cmedxCallReduceLevelNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmedxCallReduceLevelNum_Type.__name__ = "Unsigned32"
_CmedxCallReduceLevelNum_Object = MibTableColumn
cmedxCallReduceLevelNum = _CmedxCallReduceLevelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 5, 1, 1),
    _CmedxCallReduceLevelNum_Type()
)
cmedxCallReduceLevelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxCallReduceLevelNum.setStatus("current")


class _CmedxCallReduceRate_Type(Unsigned32):
    """Custom type cmedxCallReduceRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmedxCallReduceRate_Type.__name__ = "Unsigned32"
_CmedxCallReduceRate_Object = MibTableColumn
cmedxCallReduceRate = _CmedxCallReduceRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 5, 1, 2),
    _CmedxCallReduceRate_Type()
)
cmedxCallReduceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxCallReduceRate.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCallReduceRate.setUnits("percent")
_CmedxCodecNegotiationTable_Object = MibTable
cmedxCodecNegotiationTable = _CmedxCodecNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cmedxCodecNegotiationTable.setStatus("current")
_CmedxCodecNegotiationEntry_Object = MibTableRow
cmedxCodecNegotiationEntry = _CmedxCodecNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 6, 1)
)
cmedxCodecNegotiationEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxProfileIndex"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxCodecNegotiationCodec"),
)
if mibBuilder.loadTexts:
    cmedxCodecNegotiationEntry.setStatus("current")
_CmedxCodecNegotiationCodec_Type = CvcSpeechCoderRate
_CmedxCodecNegotiationCodec_Object = MibTableColumn
cmedxCodecNegotiationCodec = _CmedxCodecNegotiationCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 6, 1, 1),
    _CmedxCodecNegotiationCodec_Type()
)
cmedxCodecNegotiationCodec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxCodecNegotiationCodec.setStatus("current")


class _CmedxCodecNegotiationPreference_Type(Unsigned32):
    """Custom type cmedxCodecNegotiationPreference based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmedxCodecNegotiationPreference_Type.__name__ = "Unsigned32"
_CmedxCodecNegotiationPreference_Object = MibTableColumn
cmedxCodecNegotiationPreference = _CmedxCodecNegotiationPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 6, 1, 2),
    _CmedxCodecNegotiationPreference_Type()
)
cmedxCodecNegotiationPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxCodecNegotiationPreference.setStatus("current")
_CmedxOverloadControlTable_Object = MibTable
cmedxOverloadControlTable = _CmedxOverloadControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cmedxOverloadControlTable.setStatus("current")
_CmedxOverloadControlEntry_Object = MibTableRow
cmedxOverloadControlEntry = _CmedxOverloadControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 7, 1)
)
cmedxOverloadControlEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
)
if mibBuilder.loadTexts:
    cmedxOverloadControlEntry.setStatus("current")


class _CmedxOverloadControlEnabled_Type(TruthValue):
    """Custom type cmedxOverloadControlEnabled based on TruthValue"""


_CmedxOverloadControlEnabled_Object = MibTableColumn
cmedxOverloadControlEnabled = _CmedxOverloadControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 7, 1, 1),
    _CmedxOverloadControlEnabled_Type()
)
cmedxOverloadControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxOverloadControlEnabled.setStatus("current")
_CmedxOverloadNotifyState_Type = TruthValue
_CmedxOverloadNotifyState_Object = MibTableColumn
cmedxOverloadNotifyState = _CmedxOverloadNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 7, 1, 2),
    _CmedxOverloadNotifyState_Type()
)
cmedxOverloadNotifyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadNotifyState.setStatus("current")


class _CmedxOverloadNotifyEnabled_Type(OctetString):
    """Custom type cmedxOverloadNotifyEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CmedxOverloadNotifyEnabled_Type.__name__ = "OctetString"
_CmedxOverloadNotifyEnabled_Object = MibTableColumn
cmedxOverloadNotifyEnabled = _CmedxOverloadNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 1, 7, 1, 3),
    _CmedxOverloadNotifyEnabled_Type()
)
cmedxOverloadNotifyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadNotifyEnabled.setStatus("current")
_CmedxStats_ObjectIdentity = ObjectIdentity
cmedxStats = _CmedxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2)
)
_CmedxGatewayStatsTable_Object = MibTable
cmedxGatewayStatsTable = _CmedxGatewayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmedxGatewayStatsTable.setStatus("current")
_CmedxGatewayStatsEntry_Object = MibTableRow
cmedxGatewayStatsEntry = _CmedxGatewayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmedxGatewayStatsEntry.setStatus("current")


class _CmedxGatewayLastEvent_Type(Unsigned32):
    """Custom type cmedxGatewayLastEvent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CmedxGatewayLastEvent_Type.__name__ = "Unsigned32"
_CmedxGatewayLastEvent_Object = MibTableColumn
cmedxGatewayLastEvent = _CmedxGatewayLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 1, 1, 1),
    _CmedxGatewayLastEvent_Type()
)
cmedxGatewayLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxGatewayLastEvent.setStatus("current")
_CmedxCommandStatsTable_Object = MibTable
cmedxCommandStatsTable = _CmedxCommandStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmedxCommandStatsTable.setStatus("current")
_CmedxCommandStatsEntry_Object = MibTableRow
cmedxCommandStatsEntry = _CmedxCommandStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1)
)
cmedxCommandStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
)
if mibBuilder.loadTexts:
    cmedxCommandStatsEntry.setStatus("current")
_CmedxCmdNumAddFails_Type = Counter32
_CmedxCmdNumAddFails_Object = MibTableColumn
cmedxCmdNumAddFails = _CmedxCmdNumAddFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 1),
    _CmedxCmdNumAddFails_Type()
)
cmedxCmdNumAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAddFails.setStatus("current")
_CmedxCmdNumAddSucceeds_Type = Counter32
_CmedxCmdNumAddSucceeds_Object = MibTableColumn
cmedxCmdNumAddSucceeds = _CmedxCmdNumAddSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 2),
    _CmedxCmdNumAddSucceeds_Type()
)
cmedxCmdNumAddSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAddSucceeds.setStatus("current")
_CmedxCmdNumSubtractFails_Type = Counter32
_CmedxCmdNumSubtractFails_Object = MibTableColumn
cmedxCmdNumSubtractFails = _CmedxCmdNumSubtractFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 3),
    _CmedxCmdNumSubtractFails_Type()
)
cmedxCmdNumSubtractFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSubtractFails.setStatus("current")
_CmedxCmdNumSubtractSucceeds_Type = Counter32
_CmedxCmdNumSubtractSucceeds_Object = MibTableColumn
cmedxCmdNumSubtractSucceeds = _CmedxCmdNumSubtractSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 4),
    _CmedxCmdNumSubtractSucceeds_Type()
)
cmedxCmdNumSubtractSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSubtractSucceeds.setStatus("current")
_CmedxCmdNumMoveFails_Type = Counter32
_CmedxCmdNumMoveFails_Object = MibTableColumn
cmedxCmdNumMoveFails = _CmedxCmdNumMoveFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 5),
    _CmedxCmdNumMoveFails_Type()
)
cmedxCmdNumMoveFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumMoveFails.setStatus("current")
_CmedxCmdNumMoveSucceeds_Type = Counter32
_CmedxCmdNumMoveSucceeds_Object = MibTableColumn
cmedxCmdNumMoveSucceeds = _CmedxCmdNumMoveSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 6),
    _CmedxCmdNumMoveSucceeds_Type()
)
cmedxCmdNumMoveSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumMoveSucceeds.setStatus("current")
_CmedxCmdNumModifyFails_Type = Counter32
_CmedxCmdNumModifyFails_Object = MibTableColumn
cmedxCmdNumModifyFails = _CmedxCmdNumModifyFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 7),
    _CmedxCmdNumModifyFails_Type()
)
cmedxCmdNumModifyFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumModifyFails.setStatus("current")
_CmedxCmdNumModifySucceeds_Type = Counter32
_CmedxCmdNumModifySucceeds_Object = MibTableColumn
cmedxCmdNumModifySucceeds = _CmedxCmdNumModifySucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 8),
    _CmedxCmdNumModifySucceeds_Type()
)
cmedxCmdNumModifySucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumModifySucceeds.setStatus("current")
_CmedxCmdNumAuditValFails_Type = Counter32
_CmedxCmdNumAuditValFails_Object = MibTableColumn
cmedxCmdNumAuditValFails = _CmedxCmdNumAuditValFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 9),
    _CmedxCmdNumAuditValFails_Type()
)
cmedxCmdNumAuditValFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditValFails.setStatus("current")
_CmedxCmdNumAuditValSucceeds_Type = Counter32
_CmedxCmdNumAuditValSucceeds_Object = MibTableColumn
cmedxCmdNumAuditValSucceeds = _CmedxCmdNumAuditValSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 10),
    _CmedxCmdNumAuditValSucceeds_Type()
)
cmedxCmdNumAuditValSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditValSucceeds.setStatus("current")
_CmedxCmdNumAuditCapFails_Type = Counter32
_CmedxCmdNumAuditCapFails_Object = MibTableColumn
cmedxCmdNumAuditCapFails = _CmedxCmdNumAuditCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 11),
    _CmedxCmdNumAuditCapFails_Type()
)
cmedxCmdNumAuditCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditCapFails.setStatus("current")
_CmedxCmdNumAuditCapSucceeds_Type = Counter32
_CmedxCmdNumAuditCapSucceeds_Object = MibTableColumn
cmedxCmdNumAuditCapSucceeds = _CmedxCmdNumAuditCapSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 12),
    _CmedxCmdNumAuditCapSucceeds_Type()
)
cmedxCmdNumAuditCapSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditCapSucceeds.setStatus("current")
_CmedxCmdNumNotifyFails_Type = Counter32
_CmedxCmdNumNotifyFails_Object = MibTableColumn
cmedxCmdNumNotifyFails = _CmedxCmdNumNotifyFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 13),
    _CmedxCmdNumNotifyFails_Type()
)
cmedxCmdNumNotifyFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumNotifyFails.setStatus("current")
_CmedxCmdNumNotifySucceeds_Type = Counter32
_CmedxCmdNumNotifySucceeds_Object = MibTableColumn
cmedxCmdNumNotifySucceeds = _CmedxCmdNumNotifySucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 14),
    _CmedxCmdNumNotifySucceeds_Type()
)
cmedxCmdNumNotifySucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumNotifySucceeds.setStatus("current")
_CmedxCmdNumSrvChgFromMgcFails_Type = Counter32
_CmedxCmdNumSrvChgFromMgcFails_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgcFails = _CmedxCmdNumSrvChgFromMgcFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 15),
    _CmedxCmdNumSrvChgFromMgcFails_Type()
)
cmedxCmdNumSrvChgFromMgcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgcFails.setStatus("current")
_CmedxCmdNumSrvChgFromMgcSucceeds_Type = Counter32
_CmedxCmdNumSrvChgFromMgcSucceeds_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgcSucceeds = _CmedxCmdNumSrvChgFromMgcSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 16),
    _CmedxCmdNumSrvChgFromMgcSucceeds_Type()
)
cmedxCmdNumSrvChgFromMgcSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgcSucceeds.setStatus("current")
_CmedxCmdNumSrvChgFromMgFails_Type = Counter32
_CmedxCmdNumSrvChgFromMgFails_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgFails = _CmedxCmdNumSrvChgFromMgFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 17),
    _CmedxCmdNumSrvChgFromMgFails_Type()
)
cmedxCmdNumSrvChgFromMgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgFails.setStatus("current")
_CmedxCmdNumSrvChgFromMgSucceeds_Type = Counter32
_CmedxCmdNumSrvChgFromMgSucceeds_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgSucceeds = _CmedxCmdNumSrvChgFromMgSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 18),
    _CmedxCmdNumSrvChgFromMgSucceeds_Type()
)
cmedxCmdNumSrvChgFromMgSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgSucceeds.setStatus("current")
_CmedxCmdTotalFails_Type = Counter32
_CmedxCmdTotalFails_Object = MibTableColumn
cmedxCmdTotalFails = _CmedxCmdTotalFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 19),
    _CmedxCmdTotalFails_Type()
)
cmedxCmdTotalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdTotalFails.setStatus("current")
_CmedxCmdTotalSucceeds_Type = Counter32
_CmedxCmdTotalSucceeds_Object = MibTableColumn
cmedxCmdTotalSucceeds = _CmedxCmdTotalSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 20),
    _CmedxCmdTotalSucceeds_Type()
)
cmedxCmdTotalSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdTotalSucceeds.setStatus("current")
_CmedxCmdTotal_Type = Counter32
_CmedxCmdTotal_Object = MibTableColumn
cmedxCmdTotal = _CmedxCmdTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 21),
    _CmedxCmdTotal_Type()
)
cmedxCmdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdTotal.setStatus("current")
_CmedxCmdNumAddPendings_Type = Counter32
_CmedxCmdNumAddPendings_Object = MibTableColumn
cmedxCmdNumAddPendings = _CmedxCmdNumAddPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 22),
    _CmedxCmdNumAddPendings_Type()
)
cmedxCmdNumAddPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAddPendings.setStatus("current")
_CmedxCmdNumSubtractPendings_Type = Counter32
_CmedxCmdNumSubtractPendings_Object = MibTableColumn
cmedxCmdNumSubtractPendings = _CmedxCmdNumSubtractPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 23),
    _CmedxCmdNumSubtractPendings_Type()
)
cmedxCmdNumSubtractPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSubtractPendings.setStatus("current")
_CmedxCmdNumMovePendings_Type = Counter32
_CmedxCmdNumMovePendings_Object = MibTableColumn
cmedxCmdNumMovePendings = _CmedxCmdNumMovePendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 24),
    _CmedxCmdNumMovePendings_Type()
)
cmedxCmdNumMovePendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumMovePendings.setStatus("current")
_CmedxCmdNumModifyPendings_Type = Counter32
_CmedxCmdNumModifyPendings_Object = MibTableColumn
cmedxCmdNumModifyPendings = _CmedxCmdNumModifyPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 25),
    _CmedxCmdNumModifyPendings_Type()
)
cmedxCmdNumModifyPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumModifyPendings.setStatus("current")
_CmedxCmdNumAuditValPendings_Type = Counter32
_CmedxCmdNumAuditValPendings_Object = MibTableColumn
cmedxCmdNumAuditValPendings = _CmedxCmdNumAuditValPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 26),
    _CmedxCmdNumAuditValPendings_Type()
)
cmedxCmdNumAuditValPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditValPendings.setStatus("current")
_CmedxCmdNumAuditCapPendings_Type = Counter32
_CmedxCmdNumAuditCapPendings_Object = MibTableColumn
cmedxCmdNumAuditCapPendings = _CmedxCmdNumAuditCapPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 27),
    _CmedxCmdNumAuditCapPendings_Type()
)
cmedxCmdNumAuditCapPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumAuditCapPendings.setStatus("current")
_CmedxCmdNumNotifyPendings_Type = Counter32
_CmedxCmdNumNotifyPendings_Object = MibTableColumn
cmedxCmdNumNotifyPendings = _CmedxCmdNumNotifyPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 28),
    _CmedxCmdNumNotifyPendings_Type()
)
cmedxCmdNumNotifyPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumNotifyPendings.setStatus("current")
_CmedxCmdNumSrvChgFromMgcPendings_Type = Counter32
_CmedxCmdNumSrvChgFromMgcPendings_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgcPendings = _CmedxCmdNumSrvChgFromMgcPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 29),
    _CmedxCmdNumSrvChgFromMgcPendings_Type()
)
cmedxCmdNumSrvChgFromMgcPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgcPendings.setStatus("current")
_CmedxCmdNumSrvChgFromMgPendings_Type = Counter32
_CmedxCmdNumSrvChgFromMgPendings_Object = MibTableColumn
cmedxCmdNumSrvChgFromMgPendings = _CmedxCmdNumSrvChgFromMgPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 30),
    _CmedxCmdNumSrvChgFromMgPendings_Type()
)
cmedxCmdNumSrvChgFromMgPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumSrvChgFromMgPendings.setStatus("current")
_CmedxCmdTotalPendings_Type = Counter32
_CmedxCmdTotalPendings_Object = MibTableColumn
cmedxCmdTotalPendings = _CmedxCmdTotalPendings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 2, 1, 31),
    _CmedxCmdTotalPendings_Type()
)
cmedxCmdTotalPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdTotalPendings.setStatus("current")
_CmedxContextStatsTable_Object = MibTable
cmedxContextStatsTable = _CmedxContextStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cmedxContextStatsTable.setStatus("current")
_CmedxContextStatsEntry_Object = MibTableRow
cmedxContextStatsEntry = _CmedxContextStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1)
)
cmedxContextStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
)
if mibBuilder.loadTexts:
    cmedxContextStatsEntry.setStatus("current")
_CmedxCntxNumActiveContexts_Type = Gauge32
_CmedxCntxNumActiveContexts_Object = MibTableColumn
cmedxCntxNumActiveContexts = _CmedxCntxNumActiveContexts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 1),
    _CmedxCntxNumActiveContexts_Type()
)
cmedxCntxNumActiveContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxNumActiveContexts.setStatus("current")
_CmedxCntxPeakNumActiveContexts_Type = Gauge32
_CmedxCntxPeakNumActiveContexts_Object = MibTableColumn
cmedxCntxPeakNumActiveContexts = _CmedxCntxPeakNumActiveContexts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 2),
    _CmedxCntxPeakNumActiveContexts_Type()
)
cmedxCntxPeakNumActiveContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxPeakNumActiveContexts.setStatus("current")
_CmedxCntxNumContextAllocated_Type = Counter32
_CmedxCntxNumContextAllocated_Object = MibTableColumn
cmedxCntxNumContextAllocated = _CmedxCntxNumContextAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 3),
    _CmedxCntxNumContextAllocated_Type()
)
cmedxCntxNumContextAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxNumContextAllocated.setStatus("current")
_CmedxCntxNumContextFreed_Type = Counter32
_CmedxCntxNumContextFreed_Object = MibTableColumn
cmedxCntxNumContextFreed = _CmedxCntxNumContextFreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 4),
    _CmedxCntxNumContextFreed_Type()
)
cmedxCntxNumContextFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxNumContextFreed.setStatus("current")
_CmedxCntxShortestContextLife_Type = TimeTicks
_CmedxCntxShortestContextLife_Object = MibTableColumn
cmedxCntxShortestContextLife = _CmedxCntxShortestContextLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 5),
    _CmedxCntxShortestContextLife_Type()
)
cmedxCntxShortestContextLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxShortestContextLife.setStatus("current")
_CmedxCntxAverageContextLife_Type = TimeTicks
_CmedxCntxAverageContextLife_Object = MibTableColumn
cmedxCntxAverageContextLife = _CmedxCntxAverageContextLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 6),
    _CmedxCntxAverageContextLife_Type()
)
cmedxCntxAverageContextLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxAverageContextLife.setStatus("current")
_CmedxCntxLongestContextLife_Type = TimeTicks
_CmedxCntxLongestContextLife_Object = MibTableColumn
cmedxCntxLongestContextLife = _CmedxCntxLongestContextLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 7),
    _CmedxCntxLongestContextLife_Type()
)
cmedxCntxLongestContextLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxLongestContextLife.setStatus("current")
_CmedxCntxNumCntxMoreThan2Terms_Type = Gauge32
_CmedxCntxNumCntxMoreThan2Terms_Object = MibTableColumn
cmedxCntxNumCntxMoreThan2Terms = _CmedxCntxNumCntxMoreThan2Terms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 3, 1, 8),
    _CmedxCntxNumCntxMoreThan2Terms_Type()
)
cmedxCntxNumCntxMoreThan2Terms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCntxNumCntxMoreThan2Terms.setStatus("current")
_CmedxPhysicalTermStatsTable_Object = MibTable
cmedxPhysicalTermStatsTable = _CmedxPhysicalTermStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cmedxPhysicalTermStatsTable.setStatus("current")
_CmedxPhysicalTermStatsEntry_Object = MibTableRow
cmedxPhysicalTermStatsEntry = _CmedxPhysicalTermStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cmedxPhysicalTermStatsEntry.setStatus("current")
_CmedxPhyTermStatsNumAdds_Type = Counter32
_CmedxPhyTermStatsNumAdds_Object = MibTableColumn
cmedxPhyTermStatsNumAdds = _CmedxPhyTermStatsNumAdds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4, 1, 1),
    _CmedxPhyTermStatsNumAdds_Type()
)
cmedxPhyTermStatsNumAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxPhyTermStatsNumAdds.setStatus("current")
_CmedxPhyTermStatsNumFailures_Type = Counter32
_CmedxPhyTermStatsNumFailures_Object = MibTableColumn
cmedxPhyTermStatsNumFailures = _CmedxPhyTermStatsNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4, 1, 2),
    _CmedxPhyTermStatsNumFailures_Type()
)
cmedxPhyTermStatsNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxPhyTermStatsNumFailures.setStatus("current")
_CmedxPhyTermStatsOosFromMgcs_Type = Counter32
_CmedxPhyTermStatsOosFromMgcs_Object = MibTableColumn
cmedxPhyTermStatsOosFromMgcs = _CmedxPhyTermStatsOosFromMgcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4, 1, 3),
    _CmedxPhyTermStatsOosFromMgcs_Type()
)
cmedxPhyTermStatsOosFromMgcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxPhyTermStatsOosFromMgcs.setStatus("current")
_CmedxPhyTermStatsOosFromOams_Type = Counter32
_CmedxPhyTermStatsOosFromOams_Object = MibTableColumn
cmedxPhyTermStatsOosFromOams = _CmedxPhyTermStatsOosFromOams_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 4, 1, 4),
    _CmedxPhyTermStatsOosFromOams_Type()
)
cmedxPhyTermStatsOosFromOams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxPhyTermStatsOosFromOams.setStatus("current")
_CmedxEphemeralTermStatsTable_Object = MibTable
cmedxEphemeralTermStatsTable = _CmedxEphemeralTermStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cmedxEphemeralTermStatsTable.setStatus("current")
_CmedxEphemeralTermStatsEntry_Object = MibTableRow
cmedxEphemeralTermStatsEntry = _CmedxEphemeralTermStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 5, 1)
)
cmedxEphemeralTermStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxEphTermStatsType"),
)
if mibBuilder.loadTexts:
    cmedxEphemeralTermStatsEntry.setStatus("current")


class _CmedxEphTermStatsType_Type(Integer32):
    """Custom type cmedxEphTermStatsType based on Integer32"""
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
        *(("all", 1),
          ("pdnAtmAal1", 4),
          ("pdnAtmAal2", 5),
          ("pdnRtp", 3),
          ("scn", 2))
    )


_CmedxEphTermStatsType_Type.__name__ = "Integer32"
_CmedxEphTermStatsType_Object = MibTableColumn
cmedxEphTermStatsType = _CmedxEphTermStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 5, 1, 1),
    _CmedxEphTermStatsType_Type()
)
cmedxEphTermStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxEphTermStatsType.setStatus("current")
_CmedxEphTermStatsNumAdds_Type = Counter32
_CmedxEphTermStatsNumAdds_Object = MibTableColumn
cmedxEphTermStatsNumAdds = _CmedxEphTermStatsNumAdds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 5, 1, 2),
    _CmedxEphTermStatsNumAdds_Type()
)
cmedxEphTermStatsNumAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermStatsNumAdds.setStatus("current")
_CmedxEphTermStatsNumFailures_Type = Counter32
_CmedxEphTermStatsNumFailures_Object = MibTableColumn
cmedxEphTermStatsNumFailures = _CmedxEphTermStatsNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 5, 1, 3),
    _CmedxEphTermStatsNumFailures_Type()
)
cmedxEphTermStatsNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermStatsNumFailures.setStatus("current")
_CmedxCommandProcStatsTable_Object = MibTable
cmedxCommandProcStatsTable = _CmedxCommandProcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cmedxCommandProcStatsTable.setStatus("current")
_CmedxCommandProcStatsEntry_Object = MibTableRow
cmedxCommandProcStatsEntry = _CmedxCommandProcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1)
)
cmedxCommandProcStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
)
if mibBuilder.loadTexts:
    cmedxCommandProcStatsEntry.setStatus("current")
_CmedxCmdPhyTermAddRespTimeMin_Type = Gauge32
_CmedxCmdPhyTermAddRespTimeMin_Object = MibTableColumn
cmedxCmdPhyTermAddRespTimeMin = _CmedxCmdPhyTermAddRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 1),
    _CmedxCmdPhyTermAddRespTimeMin_Type()
)
cmedxCmdPhyTermAddRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeMin.setUnits("ms")
_CmedxCmdPhyTermAddRespTimeMax_Type = Gauge32
_CmedxCmdPhyTermAddRespTimeMax_Object = MibTableColumn
cmedxCmdPhyTermAddRespTimeMax = _CmedxCmdPhyTermAddRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 2),
    _CmedxCmdPhyTermAddRespTimeMax_Type()
)
cmedxCmdPhyTermAddRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeMax.setUnits("ms")
_CmedxCmdPhyTermAddRespTimeAvg_Type = Gauge32
_CmedxCmdPhyTermAddRespTimeAvg_Object = MibTableColumn
cmedxCmdPhyTermAddRespTimeAvg = _CmedxCmdPhyTermAddRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 3),
    _CmedxCmdPhyTermAddRespTimeAvg_Type()
)
cmedxCmdPhyTermAddRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeAvg.setUnits("ms")
_CmedxCmdPhyTermAddRespTimeCount_Type = Gauge32
_CmedxCmdPhyTermAddRespTimeCount_Object = MibTableColumn
cmedxCmdPhyTermAddRespTimeCount = _CmedxCmdPhyTermAddRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 4),
    _CmedxCmdPhyTermAddRespTimeCount_Type()
)
cmedxCmdPhyTermAddRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermAddRespTimeCount.setStatus("current")
_CmedxCmdPhyTermModRespTimeMin_Type = Gauge32
_CmedxCmdPhyTermModRespTimeMin_Object = MibTableColumn
cmedxCmdPhyTermModRespTimeMin = _CmedxCmdPhyTermModRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 5),
    _CmedxCmdPhyTermModRespTimeMin_Type()
)
cmedxCmdPhyTermModRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeMin.setUnits("ms")
_CmedxCmdPhyTermModRespTimeMax_Type = Gauge32
_CmedxCmdPhyTermModRespTimeMax_Object = MibTableColumn
cmedxCmdPhyTermModRespTimeMax = _CmedxCmdPhyTermModRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 6),
    _CmedxCmdPhyTermModRespTimeMax_Type()
)
cmedxCmdPhyTermModRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeMax.setUnits("ms")
_CmedxCmdPhyTermModRespTimeAvg_Type = Gauge32
_CmedxCmdPhyTermModRespTimeAvg_Object = MibTableColumn
cmedxCmdPhyTermModRespTimeAvg = _CmedxCmdPhyTermModRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 7),
    _CmedxCmdPhyTermModRespTimeAvg_Type()
)
cmedxCmdPhyTermModRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeAvg.setUnits("ms")
_CmedxCmdPhyTermModRespTimeCount_Type = Gauge32
_CmedxCmdPhyTermModRespTimeCount_Object = MibTableColumn
cmedxCmdPhyTermModRespTimeCount = _CmedxCmdPhyTermModRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 8),
    _CmedxCmdPhyTermModRespTimeCount_Type()
)
cmedxCmdPhyTermModRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermModRespTimeCount.setStatus("current")
_CmedxCmdPhyTermSubRespTimeMin_Type = Gauge32
_CmedxCmdPhyTermSubRespTimeMin_Object = MibTableColumn
cmedxCmdPhyTermSubRespTimeMin = _CmedxCmdPhyTermSubRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 9),
    _CmedxCmdPhyTermSubRespTimeMin_Type()
)
cmedxCmdPhyTermSubRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeMin.setUnits("ms")
_CmedxCmdPhyTermSubRespTimeMax_Type = Gauge32
_CmedxCmdPhyTermSubRespTimeMax_Object = MibTableColumn
cmedxCmdPhyTermSubRespTimeMax = _CmedxCmdPhyTermSubRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 10),
    _CmedxCmdPhyTermSubRespTimeMax_Type()
)
cmedxCmdPhyTermSubRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeMax.setUnits("ms")
_CmedxCmdPhyTermSubRespTimeAvg_Type = Gauge32
_CmedxCmdPhyTermSubRespTimeAvg_Object = MibTableColumn
cmedxCmdPhyTermSubRespTimeAvg = _CmedxCmdPhyTermSubRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 11),
    _CmedxCmdPhyTermSubRespTimeAvg_Type()
)
cmedxCmdPhyTermSubRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeAvg.setUnits("ms")
_CmedxCmdPhyTermSubRespTimeCount_Type = Gauge32
_CmedxCmdPhyTermSubRespTimeCount_Object = MibTableColumn
cmedxCmdPhyTermSubRespTimeCount = _CmedxCmdPhyTermSubRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 12),
    _CmedxCmdPhyTermSubRespTimeCount_Type()
)
cmedxCmdPhyTermSubRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdPhyTermSubRespTimeCount.setStatus("current")
_CmedxCmdEphTermAddRespTimeMin_Type = Gauge32
_CmedxCmdEphTermAddRespTimeMin_Object = MibTableColumn
cmedxCmdEphTermAddRespTimeMin = _CmedxCmdEphTermAddRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 13),
    _CmedxCmdEphTermAddRespTimeMin_Type()
)
cmedxCmdEphTermAddRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeMin.setUnits("ms")
_CmedxCmdEphTermAddRespTimeMax_Type = Gauge32
_CmedxCmdEphTermAddRespTimeMax_Object = MibTableColumn
cmedxCmdEphTermAddRespTimeMax = _CmedxCmdEphTermAddRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 14),
    _CmedxCmdEphTermAddRespTimeMax_Type()
)
cmedxCmdEphTermAddRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeMax.setUnits("ms")
_CmedxCmdEphTermAddRespTimeAvg_Type = Gauge32
_CmedxCmdEphTermAddRespTimeAvg_Object = MibTableColumn
cmedxCmdEphTermAddRespTimeAvg = _CmedxCmdEphTermAddRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 15),
    _CmedxCmdEphTermAddRespTimeAvg_Type()
)
cmedxCmdEphTermAddRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeAvg.setUnits("ms")
_CmedxCmdEphTermAddRespTimeCount_Type = Gauge32
_CmedxCmdEphTermAddRespTimeCount_Object = MibTableColumn
cmedxCmdEphTermAddRespTimeCount = _CmedxCmdEphTermAddRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 16),
    _CmedxCmdEphTermAddRespTimeCount_Type()
)
cmedxCmdEphTermAddRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermAddRespTimeCount.setStatus("current")
_CmedxCmdEphTermModRespTimeMin_Type = Gauge32
_CmedxCmdEphTermModRespTimeMin_Object = MibTableColumn
cmedxCmdEphTermModRespTimeMin = _CmedxCmdEphTermModRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 17),
    _CmedxCmdEphTermModRespTimeMin_Type()
)
cmedxCmdEphTermModRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeMin.setUnits("ms")
_CmedxCmdEphTermModRespTimeMax_Type = Gauge32
_CmedxCmdEphTermModRespTimeMax_Object = MibTableColumn
cmedxCmdEphTermModRespTimeMax = _CmedxCmdEphTermModRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 18),
    _CmedxCmdEphTermModRespTimeMax_Type()
)
cmedxCmdEphTermModRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeMax.setUnits("ms")
_CmedxCmdEphTermModRespTimeAvg_Type = Gauge32
_CmedxCmdEphTermModRespTimeAvg_Object = MibTableColumn
cmedxCmdEphTermModRespTimeAvg = _CmedxCmdEphTermModRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 19),
    _CmedxCmdEphTermModRespTimeAvg_Type()
)
cmedxCmdEphTermModRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeAvg.setUnits("ms")
_CmedxCmdEphTermModRespTimeCount_Type = Gauge32
_CmedxCmdEphTermModRespTimeCount_Object = MibTableColumn
cmedxCmdEphTermModRespTimeCount = _CmedxCmdEphTermModRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 20),
    _CmedxCmdEphTermModRespTimeCount_Type()
)
cmedxCmdEphTermModRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermModRespTimeCount.setStatus("current")
_CmedxCmdEphTermSubRespTimeMin_Type = Gauge32
_CmedxCmdEphTermSubRespTimeMin_Object = MibTableColumn
cmedxCmdEphTermSubRespTimeMin = _CmedxCmdEphTermSubRespTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 21),
    _CmedxCmdEphTermSubRespTimeMin_Type()
)
cmedxCmdEphTermSubRespTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeMin.setUnits("ms")
_CmedxCmdEphTermSubRespTimeMax_Type = Gauge32
_CmedxCmdEphTermSubRespTimeMax_Object = MibTableColumn
cmedxCmdEphTermSubRespTimeMax = _CmedxCmdEphTermSubRespTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 22),
    _CmedxCmdEphTermSubRespTimeMax_Type()
)
cmedxCmdEphTermSubRespTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeMax.setUnits("ms")
_CmedxCmdEphTermSubRespTimeAvg_Type = Gauge32
_CmedxCmdEphTermSubRespTimeAvg_Object = MibTableColumn
cmedxCmdEphTermSubRespTimeAvg = _CmedxCmdEphTermSubRespTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 23),
    _CmedxCmdEphTermSubRespTimeAvg_Type()
)
cmedxCmdEphTermSubRespTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeAvg.setUnits("ms")
_CmedxCmdEphTermSubRespTimeCount_Type = Gauge32
_CmedxCmdEphTermSubRespTimeCount_Object = MibTableColumn
cmedxCmdEphTermSubRespTimeCount = _CmedxCmdEphTermSubRespTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 24),
    _CmedxCmdEphTermSubRespTimeCount_Type()
)
cmedxCmdEphTermSubRespTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdEphTermSubRespTimeCount.setStatus("current")
_CmedxCmdNumInProgCmds_Type = Gauge32
_CmedxCmdNumInProgCmds_Object = MibTableColumn
cmedxCmdNumInProgCmds = _CmedxCmdNumInProgCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 25),
    _CmedxCmdNumInProgCmds_Type()
)
cmedxCmdNumInProgCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdNumInProgCmds.setStatus("current")
_CmedxCmdMaxInProgCmds_Type = Gauge32
_CmedxCmdMaxInProgCmds_Object = MibTableColumn
cmedxCmdMaxInProgCmds = _CmedxCmdMaxInProgCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 26),
    _CmedxCmdMaxInProgCmds_Type()
)
cmedxCmdMaxInProgCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdMaxInProgCmds.setStatus("current")
_CmedxCmdSinceLastReset_Type = Unsigned32
_CmedxCmdSinceLastReset_Object = MibTableColumn
cmedxCmdSinceLastReset = _CmedxCmdSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 6, 1, 27),
    _CmedxCmdSinceLastReset_Type()
)
cmedxCmdSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxCmdSinceLastReset.setStatus("current")
if mibBuilder.loadTexts:
    cmedxCmdSinceLastReset.setUnits("seconds")
_CmedxOverloadStatsTable_Object = MibTable
cmedxOverloadStatsTable = _CmedxOverloadStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cmedxOverloadStatsTable.setStatus("current")
_CmedxOverloadStatsEntry_Object = MibTableRow
cmedxOverloadStatsEntry = _CmedxOverloadStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1)
)
cmedxOverloadStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
)
if mibBuilder.loadTexts:
    cmedxOverloadStatsEntry.setStatus("current")
_CmedxOverloadEnterCounts_Type = Counter32SinceReset
_CmedxOverloadEnterCounts_Object = MibTableColumn
cmedxOverloadEnterCounts = _CmedxOverloadEnterCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1, 1),
    _CmedxOverloadEnterCounts_Type()
)
cmedxOverloadEnterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadEnterCounts.setStatus("current")
_CmedxOverloadExitCounts_Type = Counter32SinceReset
_CmedxOverloadExitCounts_Object = MibTableColumn
cmedxOverloadExitCounts = _CmedxOverloadExitCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1, 2),
    _CmedxOverloadExitCounts_Type()
)
cmedxOverloadExitCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadExitCounts.setStatus("current")


class _CmedxOverloadCurrentState_Type(Integer32):
    """Custom type cmedxOverloadCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overload", 2))
    )


_CmedxOverloadCurrentState_Type.__name__ = "Integer32"
_CmedxOverloadCurrentState_Object = MibTableColumn
cmedxOverloadCurrentState = _CmedxOverloadCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1, 3),
    _CmedxOverloadCurrentState_Type()
)
cmedxOverloadCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadCurrentState.setStatus("current")
_CmedxOverloadLastResetTime_Type = TimeStamp
_CmedxOverloadLastResetTime_Object = MibTableColumn
cmedxOverloadLastResetTime = _CmedxOverloadLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1, 4),
    _CmedxOverloadLastResetTime_Type()
)
cmedxOverloadLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadLastResetTime.setStatus("current")
_CmedxOverloadCountersClear_Type = TruthValue
_CmedxOverloadCountersClear_Object = MibTableColumn
cmedxOverloadCountersClear = _CmedxOverloadCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 7, 1, 5),
    _CmedxOverloadCountersClear_Type()
)
cmedxOverloadCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxOverloadCountersClear.setStatus("current")
_CmedxOverloadResourceStatsTable_Object = MibTable
cmedxOverloadResourceStatsTable = _CmedxOverloadResourceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cmedxOverloadResourceStatsTable.setStatus("current")
_CmedxOverloadResourceStatsEntry_Object = MibTableRow
cmedxOverloadResourceStatsEntry = _CmedxOverloadResourceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1)
)
cmedxOverloadResourceStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsResourceIndex"),
)
if mibBuilder.loadTexts:
    cmedxOverloadResourceStatsEntry.setStatus("current")


class _CmedxOverloadRsResourceIndex_Type(Unsigned32):
    """Custom type cmedxOverloadRsResourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CmedxOverloadRsResourceIndex_Type.__name__ = "Unsigned32"
_CmedxOverloadRsResourceIndex_Object = MibTableColumn
cmedxOverloadRsResourceIndex = _CmedxOverloadRsResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 1),
    _CmedxOverloadRsResourceIndex_Type()
)
cmedxOverloadRsResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxOverloadRsResourceIndex.setStatus("current")
_CmedxOverloadRsHighCounts_Type = Counter32SinceReset
_CmedxOverloadRsHighCounts_Object = MibTableColumn
cmedxOverloadRsHighCounts = _CmedxOverloadRsHighCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 2),
    _CmedxOverloadRsHighCounts_Type()
)
cmedxOverloadRsHighCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadRsHighCounts.setStatus("current")
_CmedxOverloadRsMedCounts_Type = Counter32SinceReset
_CmedxOverloadRsMedCounts_Object = MibTableColumn
cmedxOverloadRsMedCounts = _CmedxOverloadRsMedCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 3),
    _CmedxOverloadRsMedCounts_Type()
)
cmedxOverloadRsMedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadRsMedCounts.setStatus("current")
_CmedxOverloadRsLowCounts_Type = Counter32SinceReset
_CmedxOverloadRsLowCounts_Object = MibTableColumn
cmedxOverloadRsLowCounts = _CmedxOverloadRsLowCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 4),
    _CmedxOverloadRsLowCounts_Type()
)
cmedxOverloadRsLowCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadRsLowCounts.setStatus("current")
_CmedxOverloadContributorCounts_Type = Counter32SinceReset
_CmedxOverloadContributorCounts_Object = MibTableColumn
cmedxOverloadContributorCounts = _CmedxOverloadContributorCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 5),
    _CmedxOverloadContributorCounts_Type()
)
cmedxOverloadContributorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadContributorCounts.setStatus("current")
_CmedxOverloadRsLastResetTime_Type = TimeStamp
_CmedxOverloadRsLastResetTime_Object = MibTableColumn
cmedxOverloadRsLastResetTime = _CmedxOverloadRsLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 6),
    _CmedxOverloadRsLastResetTime_Type()
)
cmedxOverloadRsLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxOverloadRsLastResetTime.setStatus("current")
_CmedxOverloadRsCountersClear_Type = TruthValue
_CmedxOverloadRsCountersClear_Object = MibTableColumn
cmedxOverloadRsCountersClear = _CmedxOverloadRsCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 8, 1, 7),
    _CmedxOverloadRsCountersClear_Type()
)
cmedxOverloadRsCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxOverloadRsCountersClear.setStatus("current")
_CmedxEphemeralTermStatsInfoTable_Object = MibTable
cmedxEphemeralTermStatsInfoTable = _CmedxEphemeralTermStatsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cmedxEphemeralTermStatsInfoTable.setStatus("current")
_CmedxEphemeralTermStatsInfoEntry_Object = MibTableRow
cmedxEphemeralTermStatsInfoEntry = _CmedxEphemeralTermStatsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1)
)
cmedxEphemeralTermStatsInfoEntry.setIndexNames(
    (0, "CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoStatsIndex"),
)
if mibBuilder.loadTexts:
    cmedxEphemeralTermStatsInfoEntry.setStatus("current")


class _CmedxEphTermInfoStatsIndex_Type(Unsigned32):
    """Custom type cmedxEphTermInfoStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmedxEphTermInfoStatsIndex_Type.__name__ = "Unsigned32"
_CmedxEphTermInfoStatsIndex_Object = MibTableColumn
cmedxEphTermInfoStatsIndex = _CmedxEphTermInfoStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 1),
    _CmedxEphTermInfoStatsIndex_Type()
)
cmedxEphTermInfoStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedxEphTermInfoStatsIndex.setStatus("current")


class _CmedxEphTermInfoStatsIndexType_Type(Integer32):
    """Custom type cmedxEphTermInfoStatsIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bpvc", 1),
          ("gw", 2),
          ("vgw", 3))
    )


_CmedxEphTermInfoStatsIndexType_Type.__name__ = "Integer32"
_CmedxEphTermInfoStatsIndexType_Object = MibTableColumn
cmedxEphTermInfoStatsIndexType = _CmedxEphTermInfoStatsIndexType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 2),
    _CmedxEphTermInfoStatsIndexType_Type()
)
cmedxEphTermInfoStatsIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoStatsIndexType.setStatus("current")
_CmedxEphTermInfoNumTerm_Type = Counter32SinceReset
_CmedxEphTermInfoNumTerm_Object = MibTableColumn
cmedxEphTermInfoNumTerm = _CmedxEphTermInfoNumTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 3),
    _CmedxEphTermInfoNumTerm_Type()
)
cmedxEphTermInfoNumTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoNumTerm.setStatus("current")
_CmedxEphTermInfoNumInUsed_Type = Gauge32
_CmedxEphTermInfoNumInUsed_Object = MibTableColumn
cmedxEphTermInfoNumInUsed = _CmedxEphTermInfoNumInUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 4),
    _CmedxEphTermInfoNumInUsed_Type()
)
cmedxEphTermInfoNumInUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoNumInUsed.setStatus("current")
_CmedxEphTermInfoMaxNumInUsed_Type = Gauge32
_CmedxEphTermInfoMaxNumInUsed_Object = MibTableColumn
cmedxEphTermInfoMaxNumInUsed = _CmedxEphTermInfoMaxNumInUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 5),
    _CmedxEphTermInfoMaxNumInUsed_Type()
)
cmedxEphTermInfoMaxNumInUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoMaxNumInUsed.setStatus("current")
_CmedxEphTermInfoMinDuration_Type = Gauge32
_CmedxEphTermInfoMinDuration_Object = MibTableColumn
cmedxEphTermInfoMinDuration = _CmedxEphTermInfoMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 6),
    _CmedxEphTermInfoMinDuration_Type()
)
cmedxEphTermInfoMinDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    cmedxEphTermInfoMinDuration.setUnits("ms")
_CmedxEphTermInfoMaxDuration_Type = Gauge32
_CmedxEphTermInfoMaxDuration_Object = MibTableColumn
cmedxEphTermInfoMaxDuration = _CmedxEphTermInfoMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 7),
    _CmedxEphTermInfoMaxDuration_Type()
)
cmedxEphTermInfoMaxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cmedxEphTermInfoMaxDuration.setUnits("ms")
_CmedxEphTermInfoAvgDuration_Type = Gauge32
_CmedxEphTermInfoAvgDuration_Object = MibTableColumn
cmedxEphTermInfoAvgDuration = _CmedxEphTermInfoAvgDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 8),
    _CmedxEphTermInfoAvgDuration_Type()
)
cmedxEphTermInfoAvgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoAvgDuration.setStatus("current")
if mibBuilder.loadTexts:
    cmedxEphTermInfoAvgDuration.setUnits("ms")
_CmedxEphTermInfoCounterClear_Type = TruthValue
_CmedxEphTermInfoCounterClear_Object = MibTableColumn
cmedxEphTermInfoCounterClear = _CmedxEphTermInfoCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 9),
    _CmedxEphTermInfoCounterClear_Type()
)
cmedxEphTermInfoCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedxEphTermInfoCounterClear.setStatus("current")
_CmedxEphTermInfoSinceLastClear_Type = Unsigned32
_CmedxEphTermInfoSinceLastClear_Object = MibTableColumn
cmedxEphTermInfoSinceLastClear = _CmedxEphTermInfoSinceLastClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 10),
    _CmedxEphTermInfoSinceLastClear_Type()
)
cmedxEphTermInfoSinceLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoSinceLastClear.setStatus("current")
if mibBuilder.loadTexts:
    cmedxEphTermInfoSinceLastClear.setUnits("minutes")
_CmedxEphTermInfoSinceLastReset_Type = Unsigned32
_CmedxEphTermInfoSinceLastReset_Object = MibTableColumn
cmedxEphTermInfoSinceLastReset = _CmedxEphTermInfoSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 11),
    _CmedxEphTermInfoSinceLastReset_Type()
)
cmedxEphTermInfoSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoSinceLastReset.setStatus("current")
if mibBuilder.loadTexts:
    cmedxEphTermInfoSinceLastReset.setUnits("seconds")


class _CmedxEphTermIndexInfo_Type(Unsigned32):
    """Custom type cmedxEphTermIndexInfo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmedxEphTermIndexInfo_Type.__name__ = "Unsigned32"
_CmedxEphTermIndexInfo_Object = MibTableColumn
cmedxEphTermIndexInfo = _CmedxEphTermIndexInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 12),
    _CmedxEphTermIndexInfo_Type()
)
cmedxEphTermIndexInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermIndexInfo.setStatus("current")
_CmedxEphTermInfoNumFreed_Type = Unsigned32
_CmedxEphTermInfoNumFreed_Object = MibTableColumn
cmedxEphTermInfoNumFreed = _CmedxEphTermInfoNumFreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 1, 2, 9, 1, 13),
    _CmedxEphTermInfoNumFreed_Type()
)
cmedxEphTermInfoNumFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedxEphTermInfoNumFreed.setStatus("current")
_CiscoMegacoExtConformance_ObjectIdentity = ObjectIdentity
ciscoMegacoExtConformance = _CiscoMegacoExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2)
)
_CmedxCompliances_ObjectIdentity = ObjectIdentity
cmedxCompliances = _CmedxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1)
)
_CmedxGroups_ObjectIdentity = ObjectIdentity
cmedxGroups = _CmedxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2)
)
cmedGatewayConfigEntry.registerAugmentions(
    ("CISCO-MEGACO-EXT-MIB",
     "cmedxGatewayConfigEntry")
)
cmedxGatewayConfigEntry.setIndexNames(*cmedGatewayConfigEntry.getIndexNames())
cmedGatewayStatsEntry.registerAugmentions(
    ("CISCO-MEGACO-EXT-MIB",
     "cmedxGatewayStatsEntry")
)
cmedxGatewayStatsEntry.setIndexNames(*cmedGatewayStatsEntry.getIndexNames())
cmedTerminationsEntry.registerAugmentions(
    ("CISCO-MEGACO-EXT-MIB",
     "cmedxPhysicalTermStatsEntry")
)
cmedxPhysicalTermStatsEntry.setIndexNames(*cmedTerminationsEntry.getIndexNames())

# Managed Objects groups

cmedxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 1)
)
cmedxConfigGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcGroupIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayIpAddressIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayAssociationId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxTermsInContext"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayProvisionRespTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayNumConnRetries"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxWaitingDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRestartDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRespRetentionTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInitialRtt"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInactivityTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayHeaderAddrType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayDownServiceDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcAddress"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcDomain"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcPortNum"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeReason"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeProfileId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypePkgIds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeRowStatus"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfilePlayCpToneInterDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfDigitOnDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfPauseDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot1Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot2Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInitiateCotDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRespCotMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongCpToneDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongDigitDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelTail"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInGainControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileOutAttnControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoAal2VadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmBearerType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalPartialFill"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileSuppressBearerDigit"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cmedxConfigGroup.setStatus("deprecated")

cmedxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 2)
)
cmedxStatsGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayLastEvent"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAddFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAddSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSubtractFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSubtractSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumMoveFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumMoveSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumModifyFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumModifySucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditValFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditValSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditCapFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditCapSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumNotifyFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumNotifySucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgcFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgcSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumActiveContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxPeakNumActiveContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumContextAllocated"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumContextFreed"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxShortestContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxAverageContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxLongestContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumCntxMoreThan2Terms"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsNumAdds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsNumFailures"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsOosFromMgcs"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsOosFromOams"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermStatsNumAdds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermStatsNumFailures"))
)
if mibBuilder.loadTexts:
    cmedxStatsGroup.setStatus("deprecated")

cmedxCallReduceRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 3)
)
cmedxCallReduceRateGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxCallCongEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCallRenotifInterval"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCRRNumOfLevel"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCurrentCRR"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCallReduceRate"))
)
if mibBuilder.loadTexts:
    cmedxCallReduceRateGroup.setStatus("current")

cmedxCodecNegotiationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 4)
)
cmedxCodecNegotiationGroup.setObjects(
    ("CISCO-MEGACO-EXT-MIB", "cmedxCodecNegotiationPreference")
)
if mibBuilder.loadTexts:
    cmedxCodecNegotiationGroup.setStatus("current")

cmedxConfigExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 5)
)
cmedxConfigExtGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayDynamicTpktVersion"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxCommandMsgSize"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxReplyMsgSize"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileOriginatingCotTx"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileOriginatingCotRx"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileTerminatingCotTx"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileTerminatingCotRx"))
)
if mibBuilder.loadTexts:
    cmedxConfigExtGroup.setStatus("current")

cmedxServiceStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 6)
)
cmedxServiceStateGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayAdminAction"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayServiceState"))
)
if mibBuilder.loadTexts:
    cmedxServiceStateGroup.setStatus("current")

cmedxConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 7)
)
cmedxConfigGroupRev1.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcGroupIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayIpAddressIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayAssociationId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxTermsInContext"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayProvisionRespTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayNumConnRetries"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxWaitingDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRestartDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRespRetentionTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInitialRtt"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInactivityTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayHeaderAddrType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayDownServiceDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcAddress"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcDomain"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcPortNum"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeReason"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeProfileId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypePkgIds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeRowStatus"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfilePlayCpToneInterDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfDigitOnDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfPauseDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot1Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot2Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInitiateCotDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRespCotMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongCpToneDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongDigitDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelTail"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInGainControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileOutAttnControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoAal2VadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmBearerType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalPartialFill"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileSuppressBearerDigit"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRowStatus"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileComfortNoiseGenerate"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySctpAssocId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySrvChgProfile"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySrvChgProfileVer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMsgTokenType"))
)
if mibBuilder.loadTexts:
    cmedxConfigGroupRev1.setStatus("deprecated")

cmedxCallReduceRateNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 8)
)
cmedxCallReduceRateNotifyGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxCrrNotifyState"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCrrNotifyEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCurrentCallState"))
)
if mibBuilder.loadTexts:
    cmedxCallReduceRateNotifyGroup.setStatus("current")

cmedxOverloadControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 9)
)
cmedxOverloadControlGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxOverloadControlEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadNotifyState"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadNotifyEnabled"))
)
if mibBuilder.loadTexts:
    cmedxOverloadControlGroup.setStatus("current")

cmedxOverloadStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 10)
)
cmedxOverloadStatsGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxOverloadEnterCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadExitCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadCurrentState"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadLastResetTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadCountersClear"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsHighCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsMedCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsLowCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadContributorCounts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsLastResetTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxOverloadRsCountersClear"))
)
if mibBuilder.loadTexts:
    cmedxOverloadStatsGroup.setStatus("current")

cmedxStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 11)
)
cmedxStatsExtGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxCmdTotalFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdTotalSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdTotal"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdTotalPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermAddRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermAddRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermAddRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermAddRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermModRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermModRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermModRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermModRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermSubRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermSubRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermSubRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdPhyTermSubRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermAddRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermAddRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermAddRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermAddRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermModRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermModRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermModRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermModRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermSubRespTimeMin"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermSubRespTimeMax"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermSubRespTimeAvg"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdEphTermSubRespTimeCount"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumInProgCmds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdMaxInProgCmds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdSinceLastReset"))
)
if mibBuilder.loadTexts:
    cmedxStatsExtGroup.setStatus("current")

cmedxEphemeralTermStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 12)
)
cmedxEphemeralTermStatsGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoStatsIndexType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoNumTerm"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoNumInUsed"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoMaxNumInUsed"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoMinDuration"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoMaxDuration"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoAvgDuration"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoCounterClear"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoSinceLastClear"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoSinceLastReset"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermIndexInfo"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermInfoNumFreed"))
)
if mibBuilder.loadTexts:
    cmedxEphemeralTermStatsGroup.setStatus("current")

cmedxConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 13)
)
cmedxConfigGroupRev2.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcGroupIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayIpAddressIndex"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayAssociationId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxTermsInContext"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcExecTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayNumConnRetries"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMaxWaitingDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRestartDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayRespRetentionTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInitialRtt"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayInactivityTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayHeaderAddrType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayDownServiceDelay"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcAddress"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcDomain"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayActiveMgcPortNum"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeReason"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayStateChangeMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeProfileId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypePkgIds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxTermTypeRowStatus"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfilePlayCpToneInterDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfDigitOnDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDtmfPauseDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot1Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileCot2Frequency"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInitiateCotDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRespCotMethod"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongCpToneDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileDetectLongDigitDur"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileEchoCancelTail"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileInGainControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileOutAttnControl"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadEnabled"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoIpVadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileVoAal2VadTimer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmBearerType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalPartialFill"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileAtmAalType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileSuppressBearerDigit"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileRowStatus"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxProfileComfortNoiseGenerate"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySctpAssocId"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySrvChgProfile"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewaySrvChgProfileVer"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMsgTokenType"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgProvisionRspTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcProvisionRspTime"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgOrigPendLimit"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayMgcOrigPendLimit"))
)
if mibBuilder.loadTexts:
    cmedxConfigGroupRev2.setStatus("current")

cmedxStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 14)
)
cmedxStatsGroupRev1.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayLastEvent"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAddFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAddSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSubtractFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSubtractSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumMoveFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumMoveSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumModifyFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumModifySucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditValFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditValSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditCapFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditCapSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumNotifyFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumNotifySucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgcFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgcSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgFails"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgSucceeds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumActiveContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxPeakNumActiveContexts"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumContextAllocated"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumContextFreed"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxShortestContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxAverageContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxLongestContextLife"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCntxNumCntxMoreThan2Terms"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsNumAdds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsNumFailures"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsOosFromMgcs"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxPhyTermStatsOosFromOams"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermStatsNumAdds"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxEphTermStatsNumFailures"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAddPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSubtractPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumMovePendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumModifyPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditValPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumAuditCapPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumNotifyPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgcPendings"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxCmdNumSrvChgFromMgPendings"))
)
if mibBuilder.loadTexts:
    cmedxStatsGroupRev1.setStatus("current")

cmedxConfigDomainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 2, 15)
)
cmedxConfigDomainInfoGroup.setObjects(
      *(("CISCO-MEGACO-EXT-MIB", "cmedxGatewayDomainName"),
        ("CISCO-MEGACO-EXT-MIB", "cmedxGatewayCmbDnAndPortInMID"))
)
if mibBuilder.loadTexts:
    cmedxConfigDomainInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmedxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmedxCompliance.setStatus(
        "deprecated"
    )

cmedxComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmedxComplianceRev1.setStatus(
        "deprecated"
    )

cmedxComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cmedxComplianceRev2.setStatus(
        "deprecated"
    )

cmedxComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cmedxComplianceRev3.setStatus(
        "deprecated"
    )

cmedxComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 104, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cmedxComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEGACO-EXT-MIB",
    **{"CH248Packages": CH248Packages,
       "CMedxCotTones": CMedxCotTones,
       "ciscoMegacoExtMIB": ciscoMegacoExtMIB,
       "ciscoMegacoExtMIBNotifications": ciscoMegacoExtMIBNotifications,
       "ciscoMegacoExtMIBObjects": ciscoMegacoExtMIBObjects,
       "cmedxConfig": cmedxConfig,
       "cmedxGatewayConfigTable": cmedxGatewayConfigTable,
       "cmedxGatewayConfigEntry": cmedxGatewayConfigEntry,
       "cmedxGatewayMgcGroupIndex": cmedxGatewayMgcGroupIndex,
       "cmedxGatewayIpAddressIndex": cmedxGatewayIpAddressIndex,
       "cmedxGatewayAssociationId": cmedxGatewayAssociationId,
       "cmedxGatewayMaxContexts": cmedxGatewayMaxContexts,
       "cmedxGatewayMaxTermsInContext": cmedxGatewayMaxTermsInContext,
       "cmedxGatewayMgExecTime": cmedxGatewayMgExecTime,
       "cmedxGatewayMgcExecTime": cmedxGatewayMgcExecTime,
       "cmedxGatewayProvisionRespTime": cmedxGatewayProvisionRespTime,
       "cmedxGatewayNumConnRetries": cmedxGatewayNumConnRetries,
       "cmedxGatewayMaxWaitingDelay": cmedxGatewayMaxWaitingDelay,
       "cmedxGatewayRestartDelay": cmedxGatewayRestartDelay,
       "cmedxGatewayRespRetentionTime": cmedxGatewayRespRetentionTime,
       "cmedxGatewayInitialRtt": cmedxGatewayInitialRtt,
       "cmedxGatewayInactivityTime": cmedxGatewayInactivityTime,
       "cmedxGatewayHeaderAddrType": cmedxGatewayHeaderAddrType,
       "cmedxGatewayDownServiceDelay": cmedxGatewayDownServiceDelay,
       "cmedxGatewayActiveMgcAddress": cmedxGatewayActiveMgcAddress,
       "cmedxGatewayActiveMgcDomain": cmedxGatewayActiveMgcDomain,
       "cmedxGatewayActiveMgcPortNum": cmedxGatewayActiveMgcPortNum,
       "cmedxGatewayStateChangeReason": cmedxGatewayStateChangeReason,
       "cmedxGatewayStateChangeMethod": cmedxGatewayStateChangeMethod,
       "cmedxGatewayAdminAction": cmedxGatewayAdminAction,
       "cmedxGatewayServiceState": cmedxGatewayServiceState,
       "cmedxGatewayDynamicTpktVersion": cmedxGatewayDynamicTpktVersion,
       "cmedxGatewayMaxCommandMsgSize": cmedxGatewayMaxCommandMsgSize,
       "cmedxGatewayMaxReplyMsgSize": cmedxGatewayMaxReplyMsgSize,
       "cmedxGatewaySctpAssocId": cmedxGatewaySctpAssocId,
       "cmedxGatewaySrvChgProfile": cmedxGatewaySrvChgProfile,
       "cmedxGatewaySrvChgProfileVer": cmedxGatewaySrvChgProfileVer,
       "cmedxGatewayMsgTokenType": cmedxGatewayMsgTokenType,
       "cmedxGatewayMgProvisionRspTime": cmedxGatewayMgProvisionRspTime,
       "cmedxGatewayMgcProvisionRspTime": cmedxGatewayMgcProvisionRspTime,
       "cmedxGatewayMgOrigPendLimit": cmedxGatewayMgOrigPendLimit,
       "cmedxGatewayMgcOrigPendLimit": cmedxGatewayMgcOrigPendLimit,
       "cmedxGatewayDomainName": cmedxGatewayDomainName,
       "cmedxGatewayCmbDnAndPortInMID": cmedxGatewayCmbDnAndPortInMID,
       "cmedxTerminationTypeTable": cmedxTerminationTypeTable,
       "cmedxTerminationTypeEntry": cmedxTerminationTypeEntry,
       "cmedxTermTypeId": cmedxTermTypeId,
       "cmedxTermType": cmedxTermType,
       "cmedxTermTypeProfileId": cmedxTermTypeProfileId,
       "cmedxTermTypePkgIds": cmedxTermTypePkgIds,
       "cmedxTermTypeRowStatus": cmedxTermTypeRowStatus,
       "cmedxProfileTable": cmedxProfileTable,
       "cmedxProfileEntry": cmedxProfileEntry,
       "cmedxProfileIndex": cmedxProfileIndex,
       "cmedxProfilePlayCpToneInterDur": cmedxProfilePlayCpToneInterDur,
       "cmedxProfileDtmfDigitOnDur": cmedxProfileDtmfDigitOnDur,
       "cmedxProfileDtmfPauseDur": cmedxProfileDtmfPauseDur,
       "cmedxProfileCot1Frequency": cmedxProfileCot1Frequency,
       "cmedxProfileCot2Frequency": cmedxProfileCot2Frequency,
       "cmedxProfileInitiateCotDur": cmedxProfileInitiateCotDur,
       "cmedxProfileRespCotMethod": cmedxProfileRespCotMethod,
       "cmedxProfileDetectLongCpToneDur": cmedxProfileDetectLongCpToneDur,
       "cmedxProfileDetectLongDigitDur": cmedxProfileDetectLongDigitDur,
       "cmedxProfileEchoCancelEnabled": cmedxProfileEchoCancelEnabled,
       "cmedxProfileEchoCancelTail": cmedxProfileEchoCancelTail,
       "cmedxProfileInGainControl": cmedxProfileInGainControl,
       "cmedxProfileOutAttnControl": cmedxProfileOutAttnControl,
       "cmedxProfileVoIpVadEnabled": cmedxProfileVoIpVadEnabled,
       "cmedxProfileVoIpVadTimer": cmedxProfileVoIpVadTimer,
       "cmedxProfileVoAal2VadTimer": cmedxProfileVoAal2VadTimer,
       "cmedxProfileAtmBearerType": cmedxProfileAtmBearerType,
       "cmedxProfileAtmAalPartialFill": cmedxProfileAtmAalPartialFill,
       "cmedxProfileAtmAalType": cmedxProfileAtmAalType,
       "cmedxProfileSuppressBearerDigit": cmedxProfileSuppressBearerDigit,
       "cmedxProfileRowStatus": cmedxProfileRowStatus,
       "cmedxProfileOriginatingCotTx": cmedxProfileOriginatingCotTx,
       "cmedxProfileOriginatingCotRx": cmedxProfileOriginatingCotRx,
       "cmedxProfileTerminatingCotTx": cmedxProfileTerminatingCotTx,
       "cmedxProfileTerminatingCotRx": cmedxProfileTerminatingCotRx,
       "cmedxProfileComfortNoiseGenerate": cmedxProfileComfortNoiseGenerate,
       "cmedxCallReduceControlTable": cmedxCallReduceControlTable,
       "cmedxCallReduceControlEntry": cmedxCallReduceControlEntry,
       "cmedxCallCongEnabled": cmedxCallCongEnabled,
       "cmedxCallRenotifInterval": cmedxCallRenotifInterval,
       "cmedxCRRNumOfLevel": cmedxCRRNumOfLevel,
       "cmedxCurrentCRR": cmedxCurrentCRR,
       "cmedxCrrNotifyState": cmedxCrrNotifyState,
       "cmedxCrrNotifyEnabled": cmedxCrrNotifyEnabled,
       "cmedxCurrentCallState": cmedxCurrentCallState,
       "cmedxCallReduceLevelTable": cmedxCallReduceLevelTable,
       "cmedxCallReduceLevelEntry": cmedxCallReduceLevelEntry,
       "cmedxCallReduceLevelNum": cmedxCallReduceLevelNum,
       "cmedxCallReduceRate": cmedxCallReduceRate,
       "cmedxCodecNegotiationTable": cmedxCodecNegotiationTable,
       "cmedxCodecNegotiationEntry": cmedxCodecNegotiationEntry,
       "cmedxCodecNegotiationCodec": cmedxCodecNegotiationCodec,
       "cmedxCodecNegotiationPreference": cmedxCodecNegotiationPreference,
       "cmedxOverloadControlTable": cmedxOverloadControlTable,
       "cmedxOverloadControlEntry": cmedxOverloadControlEntry,
       "cmedxOverloadControlEnabled": cmedxOverloadControlEnabled,
       "cmedxOverloadNotifyState": cmedxOverloadNotifyState,
       "cmedxOverloadNotifyEnabled": cmedxOverloadNotifyEnabled,
       "cmedxStats": cmedxStats,
       "cmedxGatewayStatsTable": cmedxGatewayStatsTable,
       "cmedxGatewayStatsEntry": cmedxGatewayStatsEntry,
       "cmedxGatewayLastEvent": cmedxGatewayLastEvent,
       "cmedxCommandStatsTable": cmedxCommandStatsTable,
       "cmedxCommandStatsEntry": cmedxCommandStatsEntry,
       "cmedxCmdNumAddFails": cmedxCmdNumAddFails,
       "cmedxCmdNumAddSucceeds": cmedxCmdNumAddSucceeds,
       "cmedxCmdNumSubtractFails": cmedxCmdNumSubtractFails,
       "cmedxCmdNumSubtractSucceeds": cmedxCmdNumSubtractSucceeds,
       "cmedxCmdNumMoveFails": cmedxCmdNumMoveFails,
       "cmedxCmdNumMoveSucceeds": cmedxCmdNumMoveSucceeds,
       "cmedxCmdNumModifyFails": cmedxCmdNumModifyFails,
       "cmedxCmdNumModifySucceeds": cmedxCmdNumModifySucceeds,
       "cmedxCmdNumAuditValFails": cmedxCmdNumAuditValFails,
       "cmedxCmdNumAuditValSucceeds": cmedxCmdNumAuditValSucceeds,
       "cmedxCmdNumAuditCapFails": cmedxCmdNumAuditCapFails,
       "cmedxCmdNumAuditCapSucceeds": cmedxCmdNumAuditCapSucceeds,
       "cmedxCmdNumNotifyFails": cmedxCmdNumNotifyFails,
       "cmedxCmdNumNotifySucceeds": cmedxCmdNumNotifySucceeds,
       "cmedxCmdNumSrvChgFromMgcFails": cmedxCmdNumSrvChgFromMgcFails,
       "cmedxCmdNumSrvChgFromMgcSucceeds": cmedxCmdNumSrvChgFromMgcSucceeds,
       "cmedxCmdNumSrvChgFromMgFails": cmedxCmdNumSrvChgFromMgFails,
       "cmedxCmdNumSrvChgFromMgSucceeds": cmedxCmdNumSrvChgFromMgSucceeds,
       "cmedxCmdTotalFails": cmedxCmdTotalFails,
       "cmedxCmdTotalSucceeds": cmedxCmdTotalSucceeds,
       "cmedxCmdTotal": cmedxCmdTotal,
       "cmedxCmdNumAddPendings": cmedxCmdNumAddPendings,
       "cmedxCmdNumSubtractPendings": cmedxCmdNumSubtractPendings,
       "cmedxCmdNumMovePendings": cmedxCmdNumMovePendings,
       "cmedxCmdNumModifyPendings": cmedxCmdNumModifyPendings,
       "cmedxCmdNumAuditValPendings": cmedxCmdNumAuditValPendings,
       "cmedxCmdNumAuditCapPendings": cmedxCmdNumAuditCapPendings,
       "cmedxCmdNumNotifyPendings": cmedxCmdNumNotifyPendings,
       "cmedxCmdNumSrvChgFromMgcPendings": cmedxCmdNumSrvChgFromMgcPendings,
       "cmedxCmdNumSrvChgFromMgPendings": cmedxCmdNumSrvChgFromMgPendings,
       "cmedxCmdTotalPendings": cmedxCmdTotalPendings,
       "cmedxContextStatsTable": cmedxContextStatsTable,
       "cmedxContextStatsEntry": cmedxContextStatsEntry,
       "cmedxCntxNumActiveContexts": cmedxCntxNumActiveContexts,
       "cmedxCntxPeakNumActiveContexts": cmedxCntxPeakNumActiveContexts,
       "cmedxCntxNumContextAllocated": cmedxCntxNumContextAllocated,
       "cmedxCntxNumContextFreed": cmedxCntxNumContextFreed,
       "cmedxCntxShortestContextLife": cmedxCntxShortestContextLife,
       "cmedxCntxAverageContextLife": cmedxCntxAverageContextLife,
       "cmedxCntxLongestContextLife": cmedxCntxLongestContextLife,
       "cmedxCntxNumCntxMoreThan2Terms": cmedxCntxNumCntxMoreThan2Terms,
       "cmedxPhysicalTermStatsTable": cmedxPhysicalTermStatsTable,
       "cmedxPhysicalTermStatsEntry": cmedxPhysicalTermStatsEntry,
       "cmedxPhyTermStatsNumAdds": cmedxPhyTermStatsNumAdds,
       "cmedxPhyTermStatsNumFailures": cmedxPhyTermStatsNumFailures,
       "cmedxPhyTermStatsOosFromMgcs": cmedxPhyTermStatsOosFromMgcs,
       "cmedxPhyTermStatsOosFromOams": cmedxPhyTermStatsOosFromOams,
       "cmedxEphemeralTermStatsTable": cmedxEphemeralTermStatsTable,
       "cmedxEphemeralTermStatsEntry": cmedxEphemeralTermStatsEntry,
       "cmedxEphTermStatsType": cmedxEphTermStatsType,
       "cmedxEphTermStatsNumAdds": cmedxEphTermStatsNumAdds,
       "cmedxEphTermStatsNumFailures": cmedxEphTermStatsNumFailures,
       "cmedxCommandProcStatsTable": cmedxCommandProcStatsTable,
       "cmedxCommandProcStatsEntry": cmedxCommandProcStatsEntry,
       "cmedxCmdPhyTermAddRespTimeMin": cmedxCmdPhyTermAddRespTimeMin,
       "cmedxCmdPhyTermAddRespTimeMax": cmedxCmdPhyTermAddRespTimeMax,
       "cmedxCmdPhyTermAddRespTimeAvg": cmedxCmdPhyTermAddRespTimeAvg,
       "cmedxCmdPhyTermAddRespTimeCount": cmedxCmdPhyTermAddRespTimeCount,
       "cmedxCmdPhyTermModRespTimeMin": cmedxCmdPhyTermModRespTimeMin,
       "cmedxCmdPhyTermModRespTimeMax": cmedxCmdPhyTermModRespTimeMax,
       "cmedxCmdPhyTermModRespTimeAvg": cmedxCmdPhyTermModRespTimeAvg,
       "cmedxCmdPhyTermModRespTimeCount": cmedxCmdPhyTermModRespTimeCount,
       "cmedxCmdPhyTermSubRespTimeMin": cmedxCmdPhyTermSubRespTimeMin,
       "cmedxCmdPhyTermSubRespTimeMax": cmedxCmdPhyTermSubRespTimeMax,
       "cmedxCmdPhyTermSubRespTimeAvg": cmedxCmdPhyTermSubRespTimeAvg,
       "cmedxCmdPhyTermSubRespTimeCount": cmedxCmdPhyTermSubRespTimeCount,
       "cmedxCmdEphTermAddRespTimeMin": cmedxCmdEphTermAddRespTimeMin,
       "cmedxCmdEphTermAddRespTimeMax": cmedxCmdEphTermAddRespTimeMax,
       "cmedxCmdEphTermAddRespTimeAvg": cmedxCmdEphTermAddRespTimeAvg,
       "cmedxCmdEphTermAddRespTimeCount": cmedxCmdEphTermAddRespTimeCount,
       "cmedxCmdEphTermModRespTimeMin": cmedxCmdEphTermModRespTimeMin,
       "cmedxCmdEphTermModRespTimeMax": cmedxCmdEphTermModRespTimeMax,
       "cmedxCmdEphTermModRespTimeAvg": cmedxCmdEphTermModRespTimeAvg,
       "cmedxCmdEphTermModRespTimeCount": cmedxCmdEphTermModRespTimeCount,
       "cmedxCmdEphTermSubRespTimeMin": cmedxCmdEphTermSubRespTimeMin,
       "cmedxCmdEphTermSubRespTimeMax": cmedxCmdEphTermSubRespTimeMax,
       "cmedxCmdEphTermSubRespTimeAvg": cmedxCmdEphTermSubRespTimeAvg,
       "cmedxCmdEphTermSubRespTimeCount": cmedxCmdEphTermSubRespTimeCount,
       "cmedxCmdNumInProgCmds": cmedxCmdNumInProgCmds,
       "cmedxCmdMaxInProgCmds": cmedxCmdMaxInProgCmds,
       "cmedxCmdSinceLastReset": cmedxCmdSinceLastReset,
       "cmedxOverloadStatsTable": cmedxOverloadStatsTable,
       "cmedxOverloadStatsEntry": cmedxOverloadStatsEntry,
       "cmedxOverloadEnterCounts": cmedxOverloadEnterCounts,
       "cmedxOverloadExitCounts": cmedxOverloadExitCounts,
       "cmedxOverloadCurrentState": cmedxOverloadCurrentState,
       "cmedxOverloadLastResetTime": cmedxOverloadLastResetTime,
       "cmedxOverloadCountersClear": cmedxOverloadCountersClear,
       "cmedxOverloadResourceStatsTable": cmedxOverloadResourceStatsTable,
       "cmedxOverloadResourceStatsEntry": cmedxOverloadResourceStatsEntry,
       "cmedxOverloadRsResourceIndex": cmedxOverloadRsResourceIndex,
       "cmedxOverloadRsHighCounts": cmedxOverloadRsHighCounts,
       "cmedxOverloadRsMedCounts": cmedxOverloadRsMedCounts,
       "cmedxOverloadRsLowCounts": cmedxOverloadRsLowCounts,
       "cmedxOverloadContributorCounts": cmedxOverloadContributorCounts,
       "cmedxOverloadRsLastResetTime": cmedxOverloadRsLastResetTime,
       "cmedxOverloadRsCountersClear": cmedxOverloadRsCountersClear,
       "cmedxEphemeralTermStatsInfoTable": cmedxEphemeralTermStatsInfoTable,
       "cmedxEphemeralTermStatsInfoEntry": cmedxEphemeralTermStatsInfoEntry,
       "cmedxEphTermInfoStatsIndex": cmedxEphTermInfoStatsIndex,
       "cmedxEphTermInfoStatsIndexType": cmedxEphTermInfoStatsIndexType,
       "cmedxEphTermInfoNumTerm": cmedxEphTermInfoNumTerm,
       "cmedxEphTermInfoNumInUsed": cmedxEphTermInfoNumInUsed,
       "cmedxEphTermInfoMaxNumInUsed": cmedxEphTermInfoMaxNumInUsed,
       "cmedxEphTermInfoMinDuration": cmedxEphTermInfoMinDuration,
       "cmedxEphTermInfoMaxDuration": cmedxEphTermInfoMaxDuration,
       "cmedxEphTermInfoAvgDuration": cmedxEphTermInfoAvgDuration,
       "cmedxEphTermInfoCounterClear": cmedxEphTermInfoCounterClear,
       "cmedxEphTermInfoSinceLastClear": cmedxEphTermInfoSinceLastClear,
       "cmedxEphTermInfoSinceLastReset": cmedxEphTermInfoSinceLastReset,
       "cmedxEphTermIndexInfo": cmedxEphTermIndexInfo,
       "cmedxEphTermInfoNumFreed": cmedxEphTermInfoNumFreed,
       "ciscoMegacoExtConformance": ciscoMegacoExtConformance,
       "cmedxCompliances": cmedxCompliances,
       "cmedxCompliance": cmedxCompliance,
       "cmedxComplianceRev1": cmedxComplianceRev1,
       "cmedxComplianceRev2": cmedxComplianceRev2,
       "cmedxComplianceRev3": cmedxComplianceRev3,
       "cmedxComplianceRev4": cmedxComplianceRev4,
       "cmedxGroups": cmedxGroups,
       "cmedxConfigGroup": cmedxConfigGroup,
       "cmedxStatsGroup": cmedxStatsGroup,
       "cmedxCallReduceRateGroup": cmedxCallReduceRateGroup,
       "cmedxCodecNegotiationGroup": cmedxCodecNegotiationGroup,
       "cmedxConfigExtGroup": cmedxConfigExtGroup,
       "cmedxServiceStateGroup": cmedxServiceStateGroup,
       "cmedxConfigGroupRev1": cmedxConfigGroupRev1,
       "cmedxCallReduceRateNotifyGroup": cmedxCallReduceRateNotifyGroup,
       "cmedxOverloadControlGroup": cmedxOverloadControlGroup,
       "cmedxOverloadStatsGroup": cmedxOverloadStatsGroup,
       "cmedxStatsExtGroup": cmedxStatsExtGroup,
       "cmedxEphemeralTermStatsGroup": cmedxEphemeralTermStatsGroup,
       "cmedxConfigGroupRev2": cmedxConfigGroupRev2,
       "cmedxStatsGroupRev1": cmedxStatsGroupRev1,
       "cmedxConfigDomainInfoGroup": cmedxConfigDomainInfoGroup}
)
