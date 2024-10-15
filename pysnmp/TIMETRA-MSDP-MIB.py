# SNMP MIB module (TIMETRA-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-MSDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:03:29 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState")


# MODULE-IDENTITY

timetraMsdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 43)
)
timetraMsdpMIBModule.setRevisions(
        ("2011-08-01 00:00",
         "1909-02-28 00:00",
         "2006-08-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMsdpConformance_ObjectIdentity = ObjectIdentity
tmnxMsdpConformance = _TmnxMsdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43)
)
_TmnxMsdpCompliances_ObjectIdentity = ObjectIdentity
tmnxMsdpCompliances = _TmnxMsdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 1)
)
_TmnxMsdpGroups_ObjectIdentity = ObjectIdentity
tmnxMsdpGroups = _TmnxMsdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2)
)
_TmnxMsdpObjects_ObjectIdentity = ObjectIdentity
tmnxMsdpObjects = _TmnxMsdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43)
)
_TmnxMsdpGlobals_ObjectIdentity = ObjectIdentity
tmnxMsdpGlobals = _TmnxMsdpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1)
)


class _TmnxMsdpMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpMaxActiveSources_Object = MibScalar
tmnxMsdpMaxActiveSources = _TmnxMsdpMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 1),
    _TmnxMsdpMaxActiveSources_Type()
)
tmnxMsdpMaxActiveSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpMaxActiveSources.setStatus("current")


class _TmnxMsdpMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpMsgRcvRate_Object = MibScalar
tmnxMsdpMsgRcvRate = _TmnxMsdpMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 2),
    _TmnxMsdpMsgRcvRate_Type()
)
tmnxMsdpMsgRcvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpMsgRcvRate.setStatus("current")


class _TmnxMsdpMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpMsgRcvRateTime_Object = MibScalar
tmnxMsdpMsgRcvRateTime = _TmnxMsdpMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 3),
    _TmnxMsdpMsgRcvRateTime_Type()
)
tmnxMsdpMsgRcvRateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpMsgRcvRateThd_Object = MibScalar
tmnxMsdpMsgRcvRateThd = _TmnxMsdpMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 4),
    _TmnxMsdpMsgRcvRateThd_Type()
)
tmnxMsdpMsgRcvRateThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpMsgRcvRateThd.setStatus("current")


class _TmnxMsdpDataEncapsulation_Type(TruthValue):
    """Custom type tmnxMsdpDataEncapsulation based on TruthValue"""


_TmnxMsdpDataEncapsulation_Object = MibScalar
tmnxMsdpDataEncapsulation = _TmnxMsdpDataEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 5),
    _TmnxMsdpDataEncapsulation_Type()
)
tmnxMsdpDataEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpDataEncapsulation.setStatus("current")


class _TmnxMsdpAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpAdminState based on TmnxAdminState"""


_TmnxMsdpAdminState_Object = MibScalar
tmnxMsdpAdminState = _TmnxMsdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 6),
    _TmnxMsdpAdminState_Type()
)
tmnxMsdpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpAdminState.setStatus("current")


class _TmnxMsdpExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpExportPolicy1_Object = MibScalar
tmnxMsdpExportPolicy1 = _TmnxMsdpExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 7),
    _TmnxMsdpExportPolicy1_Type()
)
tmnxMsdpExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpExportPolicy1.setStatus("current")


class _TmnxMsdpExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpExportPolicy2_Object = MibScalar
tmnxMsdpExportPolicy2 = _TmnxMsdpExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 8),
    _TmnxMsdpExportPolicy2_Type()
)
tmnxMsdpExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpExportPolicy2.setStatus("current")


class _TmnxMsdpExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpExportPolicy3_Object = MibScalar
tmnxMsdpExportPolicy3 = _TmnxMsdpExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 9),
    _TmnxMsdpExportPolicy3_Type()
)
tmnxMsdpExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpExportPolicy3.setStatus("current")


class _TmnxMsdpExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpExportPolicy4_Object = MibScalar
tmnxMsdpExportPolicy4 = _TmnxMsdpExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 10),
    _TmnxMsdpExportPolicy4_Type()
)
tmnxMsdpExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpExportPolicy4.setStatus("current")


class _TmnxMsdpExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpExportPolicy5_Object = MibScalar
tmnxMsdpExportPolicy5 = _TmnxMsdpExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 11),
    _TmnxMsdpExportPolicy5_Type()
)
tmnxMsdpExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpExportPolicy5.setStatus("current")


class _TmnxMsdpImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpImportPolicy1_Object = MibScalar
tmnxMsdpImportPolicy1 = _TmnxMsdpImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 12),
    _TmnxMsdpImportPolicy1_Type()
)
tmnxMsdpImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpImportPolicy1.setStatus("current")


class _TmnxMsdpImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpImportPolicy2_Object = MibScalar
tmnxMsdpImportPolicy2 = _TmnxMsdpImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 13),
    _TmnxMsdpImportPolicy2_Type()
)
tmnxMsdpImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpImportPolicy2.setStatus("current")


class _TmnxMsdpImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpImportPolicy3_Object = MibScalar
tmnxMsdpImportPolicy3 = _TmnxMsdpImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 14),
    _TmnxMsdpImportPolicy3_Type()
)
tmnxMsdpImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpImportPolicy3.setStatus("current")


class _TmnxMsdpImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpImportPolicy4_Object = MibScalar
tmnxMsdpImportPolicy4 = _TmnxMsdpImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 15),
    _TmnxMsdpImportPolicy4_Type()
)
tmnxMsdpImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpImportPolicy4.setStatus("current")


class _TmnxMsdpImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpImportPolicy5_Object = MibScalar
tmnxMsdpImportPolicy5 = _TmnxMsdpImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 16),
    _TmnxMsdpImportPolicy5_Type()
)
tmnxMsdpImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpImportPolicy5.setStatus("current")


class _TmnxMsdpLocalAddressType_Type(InetAddressType):
    """Custom type tmnxMsdpLocalAddressType based on InetAddressType"""


_TmnxMsdpLocalAddressType_Object = MibScalar
tmnxMsdpLocalAddressType = _TmnxMsdpLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 17),
    _TmnxMsdpLocalAddressType_Type()
)
tmnxMsdpLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpLocalAddressType.setStatus("current")


class _TmnxMsdpLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpLocalAddress_Object = MibScalar
tmnxMsdpLocalAddress = _TmnxMsdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 18),
    _TmnxMsdpLocalAddress_Type()
)
tmnxMsdpLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpLocalAddress.setStatus("current")
_TmnxMsdpStatusPeerCount_Type = Gauge32
_TmnxMsdpStatusPeerCount_Object = MibScalar
tmnxMsdpStatusPeerCount = _TmnxMsdpStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 19),
    _TmnxMsdpStatusPeerCount_Type()
)
tmnxMsdpStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpStatusPeerCount.setStatus("current")
_TmnxMsdpStatusPeersEstablished_Type = Gauge32
_TmnxMsdpStatusPeersEstablished_Object = MibScalar
tmnxMsdpStatusPeersEstablished = _TmnxMsdpStatusPeersEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 20),
    _TmnxMsdpStatusPeersEstablished_Type()
)
tmnxMsdpStatusPeersEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpStatusPeersEstablished.setStatus("current")
_TmnxMsdpStatusSACount_Type = Gauge32
_TmnxMsdpStatusSACount_Object = MibScalar
tmnxMsdpStatusSACount = _TmnxMsdpStatusSACount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 21),
    _TmnxMsdpStatusSACount_Type()
)
tmnxMsdpStatusSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpStatusSACount.setStatus("current")
_TmnxMsdpStatusLastTimeUp_Type = TimeStamp
_TmnxMsdpStatusLastTimeUp_Object = MibScalar
tmnxMsdpStatusLastTimeUp = _TmnxMsdpStatusLastTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 22),
    _TmnxMsdpStatusLastTimeUp_Type()
)
tmnxMsdpStatusLastTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpStatusLastTimeUp.setStatus("current")
_TmnxMsdpStatusActSrcLimExceeded_Type = Counter32
_TmnxMsdpStatusActSrcLimExceeded_Object = MibScalar
tmnxMsdpStatusActSrcLimExceeded = _TmnxMsdpStatusActSrcLimExceeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 23),
    _TmnxMsdpStatusActSrcLimExceeded_Type()
)
tmnxMsdpStatusActSrcLimExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpStatusActSrcLimExceeded.setStatus("current")


class _TmnxMsdpRpfLookupSequence_Type(Integer32):
    """Custom type tmnxMsdpRpfLookupSequence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("mucastRouteTable", 0),
          ("ucastRouteTable", 1))
    )


_TmnxMsdpRpfLookupSequence_Type.__name__ = "Integer32"
_TmnxMsdpRpfLookupSequence_Object = MibScalar
tmnxMsdpRpfLookupSequence = _TmnxMsdpRpfLookupSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 24),
    _TmnxMsdpRpfLookupSequence_Type()
)
tmnxMsdpRpfLookupSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpRpfLookupSequence.setStatus("current")


class _TmnxMsdpSACacheLifetime_Type(Unsigned32):
    """Custom type tmnxMsdpSACacheLifetime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 600),
    )


_TmnxMsdpSACacheLifetime_Type.__name__ = "Unsigned32"
_TmnxMsdpSACacheLifetime_Object = MibScalar
tmnxMsdpSACacheLifetime = _TmnxMsdpSACacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 25),
    _TmnxMsdpSACacheLifetime_Type()
)
tmnxMsdpSACacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpSACacheLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpSACacheLifetime.setUnits("seconds")
_TmnxMsdpSARejectExportPolicy_Type = Counter32
_TmnxMsdpSARejectExportPolicy_Object = MibScalar
tmnxMsdpSARejectExportPolicy = _TmnxMsdpSARejectExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 26),
    _TmnxMsdpSARejectExportPolicy_Type()
)
tmnxMsdpSARejectExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSARejectExportPolicy.setStatus("current")
_TmnxMsdpSARejectImportPolicy_Type = Counter32
_TmnxMsdpSARejectImportPolicy_Object = MibScalar
tmnxMsdpSARejectImportPolicy = _TmnxMsdpSARejectImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 1, 27),
    _TmnxMsdpSARejectImportPolicy_Type()
)
tmnxMsdpSARejectImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSARejectImportPolicy.setStatus("current")
_TmnxMsdpPeerTable_Object = MibTable
tmnxMsdpPeerTable = _TmnxMsdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2)
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerTable.setStatus("current")
_TmnxMsdpPeerEntry_Object = MibTableRow
tmnxMsdpPeerEntry = _TmnxMsdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1)
)
tmnxMsdpPeerEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerAddressType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerEntry.setStatus("current")
_TmnxMsdpPeerAddressType_Type = InetAddressType
_TmnxMsdpPeerAddressType_Object = MibTableColumn
tmnxMsdpPeerAddressType = _TmnxMsdpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 1),
    _TmnxMsdpPeerAddressType_Type()
)
tmnxMsdpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpPeerAddressType.setStatus("current")


class _TmnxMsdpPeerAddress_Type(InetAddress):
    """Custom type tmnxMsdpPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpPeerAddress_Type.__name__ = "InetAddress"
_TmnxMsdpPeerAddress_Object = MibTableColumn
tmnxMsdpPeerAddress = _TmnxMsdpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 2),
    _TmnxMsdpPeerAddress_Type()
)
tmnxMsdpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpPeerAddress.setStatus("current")
_TmnxMsdpPeerRowStatus_Type = RowStatus
_TmnxMsdpPeerRowStatus_Object = MibTableColumn
tmnxMsdpPeerRowStatus = _TmnxMsdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 3),
    _TmnxMsdpPeerRowStatus_Type()
)
tmnxMsdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerRowStatus.setStatus("current")


class _TmnxMsdpPeerMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpPeerMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpPeerMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpPeerMaxActiveSources_Object = MibTableColumn
tmnxMsdpPeerMaxActiveSources = _TmnxMsdpPeerMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 4),
    _TmnxMsdpPeerMaxActiveSources_Type()
)
tmnxMsdpPeerMaxActiveSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerMaxActiveSources.setStatus("current")


class _TmnxMsdpPeerMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpPeerMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpPeerMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerMsgRcvRate_Object = MibTableColumn
tmnxMsdpPeerMsgRcvRate = _TmnxMsdpPeerMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 5),
    _TmnxMsdpPeerMsgRcvRate_Type()
)
tmnxMsdpPeerMsgRcvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerMsgRcvRate.setStatus("current")


class _TmnxMsdpPeerMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpPeerMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpPeerMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerMsgRcvRateTime_Object = MibTableColumn
tmnxMsdpPeerMsgRcvRateTime = _TmnxMsdpPeerMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 6),
    _TmnxMsdpPeerMsgRcvRateTime_Type()
)
tmnxMsdpPeerMsgRcvRateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpPeerMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpPeerMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpPeerMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpPeerMsgRcvRateThd_Object = MibTableColumn
tmnxMsdpPeerMsgRcvRateThd = _TmnxMsdpPeerMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 7),
    _TmnxMsdpPeerMsgRcvRateThd_Type()
)
tmnxMsdpPeerMsgRcvRateThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerMsgRcvRateThd.setStatus("current")


class _TmnxMsdpPeerAuthKey_Type(OctetString):
    """Custom type tmnxMsdpPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxMsdpPeerAuthKey_Type.__name__ = "OctetString"
_TmnxMsdpPeerAuthKey_Object = MibTableColumn
tmnxMsdpPeerAuthKey = _TmnxMsdpPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 8),
    _TmnxMsdpPeerAuthKey_Type()
)
tmnxMsdpPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerAuthKey.setStatus("current")


class _TmnxMsdpPeerAuthKeyEncrypted_Type(TruthValue):
    """Custom type tmnxMsdpPeerAuthKeyEncrypted based on TruthValue"""


_TmnxMsdpPeerAuthKeyEncrypted_Object = MibTableColumn
tmnxMsdpPeerAuthKeyEncrypted = _TmnxMsdpPeerAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 9),
    _TmnxMsdpPeerAuthKeyEncrypted_Type()
)
tmnxMsdpPeerAuthKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerAuthKeyEncrypted.setStatus("current")


class _TmnxMsdpPeerDefaultPeer_Type(TruthValue):
    """Custom type tmnxMsdpPeerDefaultPeer based on TruthValue"""


_TmnxMsdpPeerDefaultPeer_Object = MibTableColumn
tmnxMsdpPeerDefaultPeer = _TmnxMsdpPeerDefaultPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 10),
    _TmnxMsdpPeerDefaultPeer_Type()
)
tmnxMsdpPeerDefaultPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerDefaultPeer.setStatus("current")


class _TmnxMsdpPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpPeerAdminState based on TmnxAdminState"""


_TmnxMsdpPeerAdminState_Object = MibTableColumn
tmnxMsdpPeerAdminState = _TmnxMsdpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 11),
    _TmnxMsdpPeerAdminState_Type()
)
tmnxMsdpPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerAdminState.setStatus("current")


class _TmnxMsdpPeerExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerExportPolicy1_Object = MibTableColumn
tmnxMsdpPeerExportPolicy1 = _TmnxMsdpPeerExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 12),
    _TmnxMsdpPeerExportPolicy1_Type()
)
tmnxMsdpPeerExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerExportPolicy1.setStatus("current")


class _TmnxMsdpPeerExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerExportPolicy2_Object = MibTableColumn
tmnxMsdpPeerExportPolicy2 = _TmnxMsdpPeerExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 13),
    _TmnxMsdpPeerExportPolicy2_Type()
)
tmnxMsdpPeerExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerExportPolicy2.setStatus("current")


class _TmnxMsdpPeerExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerExportPolicy3_Object = MibTableColumn
tmnxMsdpPeerExportPolicy3 = _TmnxMsdpPeerExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 14),
    _TmnxMsdpPeerExportPolicy3_Type()
)
tmnxMsdpPeerExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerExportPolicy3.setStatus("current")


class _TmnxMsdpPeerExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerExportPolicy4_Object = MibTableColumn
tmnxMsdpPeerExportPolicy4 = _TmnxMsdpPeerExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 15),
    _TmnxMsdpPeerExportPolicy4_Type()
)
tmnxMsdpPeerExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerExportPolicy4.setStatus("current")


class _TmnxMsdpPeerExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerExportPolicy5_Object = MibTableColumn
tmnxMsdpPeerExportPolicy5 = _TmnxMsdpPeerExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 16),
    _TmnxMsdpPeerExportPolicy5_Type()
)
tmnxMsdpPeerExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerExportPolicy5.setStatus("current")


class _TmnxMsdpPeerImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerImportPolicy1_Object = MibTableColumn
tmnxMsdpPeerImportPolicy1 = _TmnxMsdpPeerImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 17),
    _TmnxMsdpPeerImportPolicy1_Type()
)
tmnxMsdpPeerImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerImportPolicy1.setStatus("current")


class _TmnxMsdpPeerImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerImportPolicy2_Object = MibTableColumn
tmnxMsdpPeerImportPolicy2 = _TmnxMsdpPeerImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 18),
    _TmnxMsdpPeerImportPolicy2_Type()
)
tmnxMsdpPeerImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerImportPolicy2.setStatus("current")


class _TmnxMsdpPeerImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerImportPolicy3_Object = MibTableColumn
tmnxMsdpPeerImportPolicy3 = _TmnxMsdpPeerImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 19),
    _TmnxMsdpPeerImportPolicy3_Type()
)
tmnxMsdpPeerImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerImportPolicy3.setStatus("current")


class _TmnxMsdpPeerImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerImportPolicy4_Object = MibTableColumn
tmnxMsdpPeerImportPolicy4 = _TmnxMsdpPeerImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 20),
    _TmnxMsdpPeerImportPolicy4_Type()
)
tmnxMsdpPeerImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerImportPolicy4.setStatus("current")


class _TmnxMsdpPeerImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerImportPolicy5_Object = MibTableColumn
tmnxMsdpPeerImportPolicy5 = _TmnxMsdpPeerImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 21),
    _TmnxMsdpPeerImportPolicy5_Type()
)
tmnxMsdpPeerImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerImportPolicy5.setStatus("current")


class _TmnxMsdpPeerLocalAddressType_Type(InetAddressType):
    """Custom type tmnxMsdpPeerLocalAddressType based on InetAddressType"""


_TmnxMsdpPeerLocalAddressType_Object = MibTableColumn
tmnxMsdpPeerLocalAddressType = _TmnxMsdpPeerLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 22),
    _TmnxMsdpPeerLocalAddressType_Type()
)
tmnxMsdpPeerLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerLocalAddressType.setStatus("current")


class _TmnxMsdpPeerLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpPeerLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpPeerLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpPeerLocalAddress_Object = MibTableColumn
tmnxMsdpPeerLocalAddress = _TmnxMsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 23),
    _TmnxMsdpPeerLocalAddress_Type()
)
tmnxMsdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerLocalAddress.setStatus("current")


class _TmnxMsdpPeerState_Type(Integer32):
    """Custom type tmnxMsdpPeerState based on Integer32"""
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
        *(("connecting", 4),
          ("disabled", 3),
          ("established", 1),
          ("inactive", 2),
          ("listen", 0))
    )


_TmnxMsdpPeerState_Type.__name__ = "Integer32"
_TmnxMsdpPeerState_Object = MibTableColumn
tmnxMsdpPeerState = _TmnxMsdpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 24),
    _TmnxMsdpPeerState_Type()
)
tmnxMsdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerState.setStatus("current")
_TmnxMsdpPeerLastUpOrDown_Type = TimeStamp
_TmnxMsdpPeerLastUpOrDown_Object = MibTableColumn
tmnxMsdpPeerLastUpOrDown = _TmnxMsdpPeerLastUpOrDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 25),
    _TmnxMsdpPeerLastUpOrDown_Type()
)
tmnxMsdpPeerLastUpOrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerLastUpOrDown.setStatus("current")
_TmnxMsdpPeerConRetry_Type = Counter32
_TmnxMsdpPeerConRetry_Object = MibTableColumn
tmnxMsdpPeerConRetry = _TmnxMsdpPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 26),
    _TmnxMsdpPeerConRetry_Type()
)
tmnxMsdpPeerConRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerConRetry.setStatus("current")
_TmnxMsdpPeerStateTimer_Type = Unsigned32
_TmnxMsdpPeerStateTimer_Object = MibTableColumn
tmnxMsdpPeerStateTimer = _TmnxMsdpPeerStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 27),
    _TmnxMsdpPeerStateTimer_Type()
)
tmnxMsdpPeerStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStateTimer.setUnits("seconds")
_TmnxMsdpPeerTimeout_Type = Unsigned32
_TmnxMsdpPeerTimeout_Object = MibTableColumn
tmnxMsdpPeerTimeout = _TmnxMsdpPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 28),
    _TmnxMsdpPeerTimeout_Type()
)
tmnxMsdpPeerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerTimeout.setUnits("seconds")
_TmnxMsdpPeerSAAccepted_Type = Gauge32
_TmnxMsdpPeerSAAccepted_Object = MibTableColumn
tmnxMsdpPeerSAAccepted = _TmnxMsdpPeerSAAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 29),
    _TmnxMsdpPeerSAAccepted_Type()
)
tmnxMsdpPeerSAAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerSAAccepted.setStatus("current")
_TmnxMsdpPeerSARecvd_Type = Gauge32
_TmnxMsdpPeerSARecvd_Object = MibTableColumn
tmnxMsdpPeerSARecvd = _TmnxMsdpPeerSARecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 30),
    _TmnxMsdpPeerSARecvd_Type()
)
tmnxMsdpPeerSARecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerSARecvd.setStatus("current")
_TmnxMsdpPeerLastASLimit_Type = TimeStamp
_TmnxMsdpPeerLastASLimit_Object = MibTableColumn
tmnxMsdpPeerLastASLimit = _TmnxMsdpPeerLastASLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 2, 1, 31),
    _TmnxMsdpPeerLastASLimit_Type()
)
tmnxMsdpPeerLastASLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerLastASLimit.setStatus("current")
_TmnxMsdpPeerGroupTable_Object = MibTable
tmnxMsdpPeerGroupTable = _TmnxMsdpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3)
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupTable.setStatus("current")
_TmnxMsdpPeerGroupEntry_Object = MibTableRow
tmnxMsdpPeerGroupEntry = _TmnxMsdpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1)
)
tmnxMsdpPeerGroupEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupName"),
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupEntry.setStatus("current")
_TmnxMsdpPeerGroupName_Type = TNamedItem
_TmnxMsdpPeerGroupName_Object = MibTableColumn
tmnxMsdpPeerGroupName = _TmnxMsdpPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 1),
    _TmnxMsdpPeerGroupName_Type()
)
tmnxMsdpPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupName.setStatus("current")
_TmnxMsdpPeerGroupRowStatus_Type = RowStatus
_TmnxMsdpPeerGroupRowStatus_Object = MibTableColumn
tmnxMsdpPeerGroupRowStatus = _TmnxMsdpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 2),
    _TmnxMsdpPeerGroupRowStatus_Type()
)
tmnxMsdpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupRowStatus.setStatus("current")


class _TmnxMsdpPeerGroupMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpPeerGroupMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpPeerGroupMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerGroupMsgRcvRate_Object = MibTableColumn
tmnxMsdpPeerGroupMsgRcvRate = _TmnxMsdpPeerGroupMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 3),
    _TmnxMsdpPeerGroupMsgRcvRate_Type()
)
tmnxMsdpPeerGroupMsgRcvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMsgRcvRate.setStatus("current")


class _TmnxMsdpPeerGroupMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpPeerGroupMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpPeerGroupMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerGroupMsgRcvRateTime_Object = MibTableColumn
tmnxMsdpPeerGroupMsgRcvRateTime = _TmnxMsdpPeerGroupMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 4),
    _TmnxMsdpPeerGroupMsgRcvRateTime_Type()
)
tmnxMsdpPeerGroupMsgRcvRateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpPeerGroupMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpPeerGroupMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpPeerGroupMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpPeerGroupMsgRcvRateThd_Object = MibTableColumn
tmnxMsdpPeerGroupMsgRcvRateThd = _TmnxMsdpPeerGroupMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 5),
    _TmnxMsdpPeerGroupMsgRcvRateThd_Type()
)
tmnxMsdpPeerGroupMsgRcvRateThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMsgRcvRateThd.setStatus("current")


class _TmnxMsdpPeerGroupAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpPeerGroupAdminState based on TmnxAdminState"""


_TmnxMsdpPeerGroupAdminState_Object = MibTableColumn
tmnxMsdpPeerGroupAdminState = _TmnxMsdpPeerGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 6),
    _TmnxMsdpPeerGroupAdminState_Type()
)
tmnxMsdpPeerGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupAdminState.setStatus("current")


class _TmnxMsdpPeerGroupExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupExportPolicy1_Object = MibTableColumn
tmnxMsdpPeerGroupExportPolicy1 = _TmnxMsdpPeerGroupExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 7),
    _TmnxMsdpPeerGroupExportPolicy1_Type()
)
tmnxMsdpPeerGroupExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupExportPolicy1.setStatus("current")


class _TmnxMsdpPeerGroupExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupExportPolicy2_Object = MibTableColumn
tmnxMsdpPeerGroupExportPolicy2 = _TmnxMsdpPeerGroupExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 8),
    _TmnxMsdpPeerGroupExportPolicy2_Type()
)
tmnxMsdpPeerGroupExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupExportPolicy2.setStatus("current")


class _TmnxMsdpPeerGroupExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupExportPolicy3_Object = MibTableColumn
tmnxMsdpPeerGroupExportPolicy3 = _TmnxMsdpPeerGroupExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 9),
    _TmnxMsdpPeerGroupExportPolicy3_Type()
)
tmnxMsdpPeerGroupExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupExportPolicy3.setStatus("current")


class _TmnxMsdpPeerGroupExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupExportPolicy4_Object = MibTableColumn
tmnxMsdpPeerGroupExportPolicy4 = _TmnxMsdpPeerGroupExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 10),
    _TmnxMsdpPeerGroupExportPolicy4_Type()
)
tmnxMsdpPeerGroupExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupExportPolicy4.setStatus("current")


class _TmnxMsdpPeerGroupExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupExportPolicy5_Object = MibTableColumn
tmnxMsdpPeerGroupExportPolicy5 = _TmnxMsdpPeerGroupExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 11),
    _TmnxMsdpPeerGroupExportPolicy5_Type()
)
tmnxMsdpPeerGroupExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupExportPolicy5.setStatus("current")


class _TmnxMsdpPeerGroupImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupImportPolicy1_Object = MibTableColumn
tmnxMsdpPeerGroupImportPolicy1 = _TmnxMsdpPeerGroupImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 12),
    _TmnxMsdpPeerGroupImportPolicy1_Type()
)
tmnxMsdpPeerGroupImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupImportPolicy1.setStatus("current")


class _TmnxMsdpPeerGroupImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupImportPolicy2_Object = MibTableColumn
tmnxMsdpPeerGroupImportPolicy2 = _TmnxMsdpPeerGroupImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 13),
    _TmnxMsdpPeerGroupImportPolicy2_Type()
)
tmnxMsdpPeerGroupImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupImportPolicy2.setStatus("current")


class _TmnxMsdpPeerGroupImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupImportPolicy3_Object = MibTableColumn
tmnxMsdpPeerGroupImportPolicy3 = _TmnxMsdpPeerGroupImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 14),
    _TmnxMsdpPeerGroupImportPolicy3_Type()
)
tmnxMsdpPeerGroupImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupImportPolicy3.setStatus("current")


class _TmnxMsdpPeerGroupImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupImportPolicy4_Object = MibTableColumn
tmnxMsdpPeerGroupImportPolicy4 = _TmnxMsdpPeerGroupImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 15),
    _TmnxMsdpPeerGroupImportPolicy4_Type()
)
tmnxMsdpPeerGroupImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupImportPolicy4.setStatus("current")


class _TmnxMsdpPeerGroupImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGroupImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGroupImportPolicy5_Object = MibTableColumn
tmnxMsdpPeerGroupImportPolicy5 = _TmnxMsdpPeerGroupImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 16),
    _TmnxMsdpPeerGroupImportPolicy5_Type()
)
tmnxMsdpPeerGroupImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupImportPolicy5.setStatus("current")


class _TmnxMsdpPeerGroupLocalAddrType_Type(InetAddressType):
    """Custom type tmnxMsdpPeerGroupLocalAddrType based on InetAddressType"""


_TmnxMsdpPeerGroupLocalAddrType_Object = MibTableColumn
tmnxMsdpPeerGroupLocalAddrType = _TmnxMsdpPeerGroupLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 17),
    _TmnxMsdpPeerGroupLocalAddrType_Type()
)
tmnxMsdpPeerGroupLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupLocalAddrType.setStatus("current")


class _TmnxMsdpPeerGroupLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpPeerGroupLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpPeerGroupLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpPeerGroupLocalAddress_Object = MibTableColumn
tmnxMsdpPeerGroupLocalAddress = _TmnxMsdpPeerGroupLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 18),
    _TmnxMsdpPeerGroupLocalAddress_Type()
)
tmnxMsdpPeerGroupLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupLocalAddress.setStatus("current")


class _TmnxMsdpPeerGroupMode_Type(Integer32):
    """Custom type tmnxMsdpPeerGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh-group", 2),
          ("standard", 1))
    )


_TmnxMsdpPeerGroupMode_Type.__name__ = "Integer32"
_TmnxMsdpPeerGroupMode_Object = MibTableColumn
tmnxMsdpPeerGroupMode = _TmnxMsdpPeerGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 19),
    _TmnxMsdpPeerGroupMode_Type()
)
tmnxMsdpPeerGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMode.setStatus("current")


class _TmnxMsdpPeerGroupMaxActSources_Type(Integer32):
    """Custom type tmnxMsdpPeerGroupMaxActSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpPeerGroupMaxActSources_Type.__name__ = "Integer32"
_TmnxMsdpPeerGroupMaxActSources_Object = MibTableColumn
tmnxMsdpPeerGroupMaxActSources = _TmnxMsdpPeerGroupMaxActSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 20),
    _TmnxMsdpPeerGroupMaxActSources_Type()
)
tmnxMsdpPeerGroupMaxActSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupMaxActSources.setStatus("current")
_TmnxMsdpPeerGroupActMsgsExMax_Type = Counter32
_TmnxMsdpPeerGroupActMsgsExMax_Object = MibTableColumn
tmnxMsdpPeerGroupActMsgsExMax = _TmnxMsdpPeerGroupActMsgsExMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 21),
    _TmnxMsdpPeerGroupActMsgsExMax_Type()
)
tmnxMsdpPeerGroupActMsgsExMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupActMsgsExMax.setStatus("current")
_TmnxMsdpPeerGrpSARejExpPolicy_Type = Counter32
_TmnxMsdpPeerGrpSARejExpPolicy_Object = MibTableColumn
tmnxMsdpPeerGrpSARejExpPolicy = _TmnxMsdpPeerGrpSARejExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 22),
    _TmnxMsdpPeerGrpSARejExpPolicy_Type()
)
tmnxMsdpPeerGrpSARejExpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpSARejExpPolicy.setStatus("current")
_TmnxMsdpPeerGrpSARejImpPolicy_Type = Counter32
_TmnxMsdpPeerGrpSARejImpPolicy_Object = MibTableColumn
tmnxMsdpPeerGrpSARejImpPolicy = _TmnxMsdpPeerGrpSARejImpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 3, 1, 23),
    _TmnxMsdpPeerGrpSARejImpPolicy_Type()
)
tmnxMsdpPeerGrpSARejImpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpSARejImpPolicy.setStatus("current")
_TmnxMsdpPeerGrpPeerTable_Object = MibTable
tmnxMsdpPeerGrpPeerTable = _TmnxMsdpPeerGrpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4)
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerTable.setStatus("current")
_TmnxMsdpPeerGrpPeerEntry_Object = MibTableRow
tmnxMsdpPeerGrpPeerEntry = _TmnxMsdpPeerGrpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1)
)
tmnxMsdpPeerGrpPeerEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupName"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerAddressType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerEntry.setStatus("current")
_TmnxMsdpPeerGrpPeerAddressType_Type = InetAddressType
_TmnxMsdpPeerGrpPeerAddressType_Object = MibTableColumn
tmnxMsdpPeerGrpPeerAddressType = _TmnxMsdpPeerGrpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 1),
    _TmnxMsdpPeerGrpPeerAddressType_Type()
)
tmnxMsdpPeerGrpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerAddressType.setStatus("current")


class _TmnxMsdpPeerGrpPeerAddress_Type(InetAddress):
    """Custom type tmnxMsdpPeerGrpPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpPeerGrpPeerAddress_Type.__name__ = "InetAddress"
_TmnxMsdpPeerGrpPeerAddress_Object = MibTableColumn
tmnxMsdpPeerGrpPeerAddress = _TmnxMsdpPeerGrpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 2),
    _TmnxMsdpPeerGrpPeerAddress_Type()
)
tmnxMsdpPeerGrpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerAddress.setStatus("current")
_TmnxMsdpPeerGrpPeerRowStatus_Type = RowStatus
_TmnxMsdpPeerGrpPeerRowStatus_Object = MibTableColumn
tmnxMsdpPeerGrpPeerRowStatus = _TmnxMsdpPeerGrpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 3),
    _TmnxMsdpPeerGrpPeerRowStatus_Type()
)
tmnxMsdpPeerGrpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerRowStatus.setStatus("current")


class _TmnxMsdpPeerGrpPeerMaxActSrcs_Type(Integer32):
    """Custom type tmnxMsdpPeerGrpPeerMaxActSrcs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpPeerGrpPeerMaxActSrcs_Type.__name__ = "Integer32"
_TmnxMsdpPeerGrpPeerMaxActSrcs_Object = MibTableColumn
tmnxMsdpPeerGrpPeerMaxActSrcs = _TmnxMsdpPeerGrpPeerMaxActSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 4),
    _TmnxMsdpPeerGrpPeerMaxActSrcs_Type()
)
tmnxMsdpPeerGrpPeerMaxActSrcs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerMaxActSrcs.setStatus("current")


class _TmnxMsdpPeerGrpPeerMsgRcvRt_Type(Unsigned32):
    """Custom type tmnxMsdpPeerGrpPeerMsgRcvRt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpPeerGrpPeerMsgRcvRt_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerGrpPeerMsgRcvRt_Object = MibTableColumn
tmnxMsdpPeerGrpPeerMsgRcvRt = _TmnxMsdpPeerGrpPeerMsgRcvRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 5),
    _TmnxMsdpPeerGrpPeerMsgRcvRt_Type()
)
tmnxMsdpPeerGrpPeerMsgRcvRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerMsgRcvRt.setStatus("current")


class _TmnxMsdpPeerGrpPeerMsgRcvRtTime_Type(Unsigned32):
    """Custom type tmnxMsdpPeerGrpPeerMsgRcvRtTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpPeerGrpPeerMsgRcvRtTime_Type.__name__ = "Unsigned32"
_TmnxMsdpPeerGrpPeerMsgRcvRtTime_Object = MibTableColumn
tmnxMsdpPeerGrpPeerMsgRcvRtTime = _TmnxMsdpPeerGrpPeerMsgRcvRtTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 6),
    _TmnxMsdpPeerGrpPeerMsgRcvRtTime_Type()
)
tmnxMsdpPeerGrpPeerMsgRcvRtTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerMsgRcvRtTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerMsgRcvRtTime.setUnits("seconds")


class _TmnxMsdpPeerGrpPeerMsgRcvRtThd_Type(Gauge32):
    """Custom type tmnxMsdpPeerGrpPeerMsgRcvRtThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpPeerGrpPeerMsgRcvRtThd_Type.__name__ = "Gauge32"
_TmnxMsdpPeerGrpPeerMsgRcvRtThd_Object = MibTableColumn
tmnxMsdpPeerGrpPeerMsgRcvRtThd = _TmnxMsdpPeerGrpPeerMsgRcvRtThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 7),
    _TmnxMsdpPeerGrpPeerMsgRcvRtThd_Type()
)
tmnxMsdpPeerGrpPeerMsgRcvRtThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerMsgRcvRtThd.setStatus("current")


class _TmnxMsdpPeerGrpPeerAuthKey_Type(OctetString):
    """Custom type tmnxMsdpPeerGrpPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxMsdpPeerGrpPeerAuthKey_Type.__name__ = "OctetString"
_TmnxMsdpPeerGrpPeerAuthKey_Object = MibTableColumn
tmnxMsdpPeerGrpPeerAuthKey = _TmnxMsdpPeerGrpPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 8),
    _TmnxMsdpPeerGrpPeerAuthKey_Type()
)
tmnxMsdpPeerGrpPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerAuthKey.setStatus("current")


class _TmnxMsdpPeerGrpPeerAKeyEncrypt_Type(TruthValue):
    """Custom type tmnxMsdpPeerGrpPeerAKeyEncrypt based on TruthValue"""


_TmnxMsdpPeerGrpPeerAKeyEncrypt_Object = MibTableColumn
tmnxMsdpPeerGrpPeerAKeyEncrypt = _TmnxMsdpPeerGrpPeerAKeyEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 9),
    _TmnxMsdpPeerGrpPeerAKeyEncrypt_Type()
)
tmnxMsdpPeerGrpPeerAKeyEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerAKeyEncrypt.setStatus("current")


class _TmnxMsdpPeerGrpPeerDefaultPeer_Type(TruthValue):
    """Custom type tmnxMsdpPeerGrpPeerDefaultPeer based on TruthValue"""


_TmnxMsdpPeerGrpPeerDefaultPeer_Object = MibTableColumn
tmnxMsdpPeerGrpPeerDefaultPeer = _TmnxMsdpPeerGrpPeerDefaultPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 10),
    _TmnxMsdpPeerGrpPeerDefaultPeer_Type()
)
tmnxMsdpPeerGrpPeerDefaultPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerDefaultPeer.setStatus("current")


class _TmnxMsdpPeerGrpPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpPeerGrpPeerAdminState based on TmnxAdminState"""


_TmnxMsdpPeerGrpPeerAdminState_Object = MibTableColumn
tmnxMsdpPeerGrpPeerAdminState = _TmnxMsdpPeerGrpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 11),
    _TmnxMsdpPeerGrpPeerAdminState_Type()
)
tmnxMsdpPeerGrpPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerAdminState.setStatus("current")


class _TmnxMsdpPeerGrpPeerExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerExportPolicy1_Object = MibTableColumn
tmnxMsdpPeerGrpPeerExportPolicy1 = _TmnxMsdpPeerGrpPeerExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 12),
    _TmnxMsdpPeerGrpPeerExportPolicy1_Type()
)
tmnxMsdpPeerGrpPeerExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerExportPolicy1.setStatus("current")


class _TmnxMsdpPeerGrpPeerExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerExportPolicy2_Object = MibTableColumn
tmnxMsdpPeerGrpPeerExportPolicy2 = _TmnxMsdpPeerGrpPeerExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 13),
    _TmnxMsdpPeerGrpPeerExportPolicy2_Type()
)
tmnxMsdpPeerGrpPeerExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerExportPolicy2.setStatus("current")


class _TmnxMsdpPeerGrpPeerExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerExportPolicy3_Object = MibTableColumn
tmnxMsdpPeerGrpPeerExportPolicy3 = _TmnxMsdpPeerGrpPeerExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 14),
    _TmnxMsdpPeerGrpPeerExportPolicy3_Type()
)
tmnxMsdpPeerGrpPeerExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerExportPolicy3.setStatus("current")


class _TmnxMsdpPeerGrpPeerExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerExportPolicy4_Object = MibTableColumn
tmnxMsdpPeerGrpPeerExportPolicy4 = _TmnxMsdpPeerGrpPeerExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 15),
    _TmnxMsdpPeerGrpPeerExportPolicy4_Type()
)
tmnxMsdpPeerGrpPeerExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerExportPolicy4.setStatus("current")


class _TmnxMsdpPeerGrpPeerExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerExportPolicy5_Object = MibTableColumn
tmnxMsdpPeerGrpPeerExportPolicy5 = _TmnxMsdpPeerGrpPeerExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 16),
    _TmnxMsdpPeerGrpPeerExportPolicy5_Type()
)
tmnxMsdpPeerGrpPeerExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerExportPolicy5.setStatus("current")


class _TmnxMsdpPeerGrpPeerImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerImportPolicy1_Object = MibTableColumn
tmnxMsdpPeerGrpPeerImportPolicy1 = _TmnxMsdpPeerGrpPeerImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 17),
    _TmnxMsdpPeerGrpPeerImportPolicy1_Type()
)
tmnxMsdpPeerGrpPeerImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerImportPolicy1.setStatus("current")


class _TmnxMsdpPeerGrpPeerImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerImportPolicy2_Object = MibTableColumn
tmnxMsdpPeerGrpPeerImportPolicy2 = _TmnxMsdpPeerGrpPeerImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 18),
    _TmnxMsdpPeerGrpPeerImportPolicy2_Type()
)
tmnxMsdpPeerGrpPeerImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerImportPolicy2.setStatus("current")


class _TmnxMsdpPeerGrpPeerImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerImportPolicy3_Object = MibTableColumn
tmnxMsdpPeerGrpPeerImportPolicy3 = _TmnxMsdpPeerGrpPeerImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 19),
    _TmnxMsdpPeerGrpPeerImportPolicy3_Type()
)
tmnxMsdpPeerGrpPeerImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerImportPolicy3.setStatus("current")


class _TmnxMsdpPeerGrpPeerImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerImportPolicy4_Object = MibTableColumn
tmnxMsdpPeerGrpPeerImportPolicy4 = _TmnxMsdpPeerGrpPeerImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 20),
    _TmnxMsdpPeerGrpPeerImportPolicy4_Type()
)
tmnxMsdpPeerGrpPeerImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerImportPolicy4.setStatus("current")


class _TmnxMsdpPeerGrpPeerImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpPeerGrpPeerImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpPeerGrpPeerImportPolicy5_Object = MibTableColumn
tmnxMsdpPeerGrpPeerImportPolicy5 = _TmnxMsdpPeerGrpPeerImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 21),
    _TmnxMsdpPeerGrpPeerImportPolicy5_Type()
)
tmnxMsdpPeerGrpPeerImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerImportPolicy5.setStatus("current")


class _TmnxMsdpPeerGrpPeerLocAddrType_Type(InetAddressType):
    """Custom type tmnxMsdpPeerGrpPeerLocAddrType based on InetAddressType"""


_TmnxMsdpPeerGrpPeerLocAddrType_Object = MibTableColumn
tmnxMsdpPeerGrpPeerLocAddrType = _TmnxMsdpPeerGrpPeerLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 22),
    _TmnxMsdpPeerGrpPeerLocAddrType_Type()
)
tmnxMsdpPeerGrpPeerLocAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerLocAddrType.setStatus("current")


class _TmnxMsdpPeerGrpPeerLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpPeerGrpPeerLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpPeerGrpPeerLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpPeerGrpPeerLocalAddress_Object = MibTableColumn
tmnxMsdpPeerGrpPeerLocalAddress = _TmnxMsdpPeerGrpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 23),
    _TmnxMsdpPeerGrpPeerLocalAddress_Type()
)
tmnxMsdpPeerGrpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerLocalAddress.setStatus("current")


class _TmnxMsdpPeerGrpPeerState_Type(Integer32):
    """Custom type tmnxMsdpPeerGrpPeerState based on Integer32"""
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
        *(("connecting", 4),
          ("disabled", 3),
          ("established", 1),
          ("inactive", 2),
          ("listen", 0))
    )


_TmnxMsdpPeerGrpPeerState_Type.__name__ = "Integer32"
_TmnxMsdpPeerGrpPeerState_Object = MibTableColumn
tmnxMsdpPeerGrpPeerState = _TmnxMsdpPeerGrpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 24),
    _TmnxMsdpPeerGrpPeerState_Type()
)
tmnxMsdpPeerGrpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerState.setStatus("current")
_TmnxMsdpPeerGrpPeerLastUpOrDown_Type = TimeStamp
_TmnxMsdpPeerGrpPeerLastUpOrDown_Object = MibTableColumn
tmnxMsdpPeerGrpPeerLastUpOrDown = _TmnxMsdpPeerGrpPeerLastUpOrDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 25),
    _TmnxMsdpPeerGrpPeerLastUpOrDown_Type()
)
tmnxMsdpPeerGrpPeerLastUpOrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerLastUpOrDown.setStatus("current")
_TmnxMsdpPeerGrpPeerConRetry_Type = Counter32
_TmnxMsdpPeerGrpPeerConRetry_Object = MibTableColumn
tmnxMsdpPeerGrpPeerConRetry = _TmnxMsdpPeerGrpPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 26),
    _TmnxMsdpPeerGrpPeerConRetry_Type()
)
tmnxMsdpPeerGrpPeerConRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerConRetry.setStatus("current")
_TmnxMsdpPeerGrpPeerStateTimer_Type = Unsigned32
_TmnxMsdpPeerGrpPeerStateTimer_Object = MibTableColumn
tmnxMsdpPeerGrpPeerStateTimer = _TmnxMsdpPeerGrpPeerStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 27),
    _TmnxMsdpPeerGrpPeerStateTimer_Type()
)
tmnxMsdpPeerGrpPeerStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerStateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerStateTimer.setUnits("seconds")
_TmnxMsdpPeerGrpPeerTimeout_Type = Unsigned32
_TmnxMsdpPeerGrpPeerTimeout_Object = MibTableColumn
tmnxMsdpPeerGrpPeerTimeout = _TmnxMsdpPeerGrpPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 28),
    _TmnxMsdpPeerGrpPeerTimeout_Type()
)
tmnxMsdpPeerGrpPeerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerTimeout.setUnits("seconds")
_TmnxMsdpPeerGrpPeerSAAccepted_Type = Gauge32
_TmnxMsdpPeerGrpPeerSAAccepted_Object = MibTableColumn
tmnxMsdpPeerGrpPeerSAAccepted = _TmnxMsdpPeerGrpPeerSAAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 29),
    _TmnxMsdpPeerGrpPeerSAAccepted_Type()
)
tmnxMsdpPeerGrpPeerSAAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerSAAccepted.setStatus("current")
_TmnxMsdpPeerGrpPeerSARecvd_Type = Gauge32
_TmnxMsdpPeerGrpPeerSARecvd_Object = MibTableColumn
tmnxMsdpPeerGrpPeerSARecvd = _TmnxMsdpPeerGrpPeerSARecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 30),
    _TmnxMsdpPeerGrpPeerSARecvd_Type()
)
tmnxMsdpPeerGrpPeerSARecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerSARecvd.setStatus("current")
_TmnxMsdpPeerGrpPeerLastASLimit_Type = TimeStamp
_TmnxMsdpPeerGrpPeerLastASLimit_Object = MibTableColumn
tmnxMsdpPeerGrpPeerLastASLimit = _TmnxMsdpPeerGrpPeerLastASLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 4, 1, 31),
    _TmnxMsdpPeerGrpPeerLastASLimit_Type()
)
tmnxMsdpPeerGrpPeerLastASLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerGrpPeerLastASLimit.setStatus("current")
_TmnxMsdpSourceTable_Object = MibTable
tmnxMsdpSourceTable = _TmnxMsdpSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5)
)
if mibBuilder.loadTexts:
    tmnxMsdpSourceTable.setStatus("current")
_TmnxMsdpSourceEntry_Object = MibTableRow
tmnxMsdpSourceEntry = _TmnxMsdpSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1)
)
tmnxMsdpSourceEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSourcePrefixType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSourcePrefix"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSourceMask"),
)
if mibBuilder.loadTexts:
    tmnxMsdpSourceEntry.setStatus("current")
_TmnxMsdpSourcePrefixType_Type = InetAddressType
_TmnxMsdpSourcePrefixType_Object = MibTableColumn
tmnxMsdpSourcePrefixType = _TmnxMsdpSourcePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 1),
    _TmnxMsdpSourcePrefixType_Type()
)
tmnxMsdpSourcePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSourcePrefixType.setStatus("current")


class _TmnxMsdpSourcePrefix_Type(InetAddress):
    """Custom type tmnxMsdpSourcePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSourcePrefix_Type.__name__ = "InetAddress"
_TmnxMsdpSourcePrefix_Object = MibTableColumn
tmnxMsdpSourcePrefix = _TmnxMsdpSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 2),
    _TmnxMsdpSourcePrefix_Type()
)
tmnxMsdpSourcePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSourcePrefix.setStatus("current")
_TmnxMsdpSourceMask_Type = InetAddressPrefixLength
_TmnxMsdpSourceMask_Object = MibTableColumn
tmnxMsdpSourceMask = _TmnxMsdpSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 3),
    _TmnxMsdpSourceMask_Type()
)
tmnxMsdpSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSourceMask.setStatus("current")
_TmnxMsdpSourceRowStatus_Type = RowStatus
_TmnxMsdpSourceRowStatus_Object = MibTableColumn
tmnxMsdpSourceRowStatus = _TmnxMsdpSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 4),
    _TmnxMsdpSourceRowStatus_Type()
)
tmnxMsdpSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpSourceRowStatus.setStatus("current")


class _TmnxMsdpSourceMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpSourceMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpSourceMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpSourceMaxActiveSources_Object = MibTableColumn
tmnxMsdpSourceMaxActiveSources = _TmnxMsdpSourceMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 5),
    _TmnxMsdpSourceMaxActiveSources_Type()
)
tmnxMsdpSourceMaxActiveSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpSourceMaxActiveSources.setStatus("current")


class _TmnxMsdpSourceDiscMethod_Type(Integer32):
    """Custom type tmnxMsdpSourceDiscMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("dynamic", 0))
    )


_TmnxMsdpSourceDiscMethod_Type.__name__ = "Integer32"
_TmnxMsdpSourceDiscMethod_Object = MibTableColumn
tmnxMsdpSourceDiscMethod = _TmnxMsdpSourceDiscMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 6),
    _TmnxMsdpSourceDiscMethod_Type()
)
tmnxMsdpSourceDiscMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSourceDiscMethod.setStatus("current")
_TmnxMsdpSourceSrcActMsgsExMax_Type = Counter32
_TmnxMsdpSourceSrcActMsgsExMax_Object = MibTableColumn
tmnxMsdpSourceSrcActMsgsExMax = _TmnxMsdpSourceSrcActMsgsExMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 7),
    _TmnxMsdpSourceSrcActMsgsExMax_Type()
)
tmnxMsdpSourceSrcActMsgsExMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSourceSrcActMsgsExMax.setStatus("current")
_TmnxMsdpSourceLastExEventTime_Type = TimeStamp
_TmnxMsdpSourceLastExEventTime_Object = MibTableColumn
tmnxMsdpSourceLastExEventTime = _TmnxMsdpSourceLastExEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 5, 1, 8),
    _TmnxMsdpSourceLastExEventTime_Type()
)
tmnxMsdpSourceLastExEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSourceLastExEventTime.setStatus("current")
_TmnxMsdpSrcActiveTable_Object = MibTable
tmnxMsdpSrcActiveTable = _TmnxMsdpSrcActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6)
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveTable.setStatus("current")
_TmnxMsdpSrcActiveEntry_Object = MibTableRow
tmnxMsdpSrcActiveEntry = _TmnxMsdpSrcActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1)
)
tmnxMsdpSrcActiveEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveGroupAddrType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveGroupAddr"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveSourceAddrType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveSourceAddr"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveOriginRPType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveOriginRP"),
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveEntry.setStatus("current")
_TmnxMsdpSrcActiveGroupAddrType_Type = InetAddressType
_TmnxMsdpSrcActiveGroupAddrType_Object = MibTableColumn
tmnxMsdpSrcActiveGroupAddrType = _TmnxMsdpSrcActiveGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 1),
    _TmnxMsdpSrcActiveGroupAddrType_Type()
)
tmnxMsdpSrcActiveGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveGroupAddrType.setStatus("current")


class _TmnxMsdpSrcActiveGroupAddr_Type(InetAddress):
    """Custom type tmnxMsdpSrcActiveGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActiveGroupAddr_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActiveGroupAddr_Object = MibTableColumn
tmnxMsdpSrcActiveGroupAddr = _TmnxMsdpSrcActiveGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 2),
    _TmnxMsdpSrcActiveGroupAddr_Type()
)
tmnxMsdpSrcActiveGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveGroupAddr.setStatus("current")
_TmnxMsdpSrcActiveSourceAddrType_Type = InetAddressType
_TmnxMsdpSrcActiveSourceAddrType_Object = MibTableColumn
tmnxMsdpSrcActiveSourceAddrType = _TmnxMsdpSrcActiveSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 3),
    _TmnxMsdpSrcActiveSourceAddrType_Type()
)
tmnxMsdpSrcActiveSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveSourceAddrType.setStatus("current")


class _TmnxMsdpSrcActiveSourceAddr_Type(InetAddress):
    """Custom type tmnxMsdpSrcActiveSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActiveSourceAddr_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActiveSourceAddr_Object = MibTableColumn
tmnxMsdpSrcActiveSourceAddr = _TmnxMsdpSrcActiveSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 4),
    _TmnxMsdpSrcActiveSourceAddr_Type()
)
tmnxMsdpSrcActiveSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveSourceAddr.setStatus("current")
_TmnxMsdpSrcActiveOriginRPType_Type = InetAddressType
_TmnxMsdpSrcActiveOriginRPType_Object = MibTableColumn
tmnxMsdpSrcActiveOriginRPType = _TmnxMsdpSrcActiveOriginRPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 5),
    _TmnxMsdpSrcActiveOriginRPType_Type()
)
tmnxMsdpSrcActiveOriginRPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveOriginRPType.setStatus("current")


class _TmnxMsdpSrcActiveOriginRP_Type(InetAddress):
    """Custom type tmnxMsdpSrcActiveOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActiveOriginRP_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActiveOriginRP_Object = MibTableColumn
tmnxMsdpSrcActiveOriginRP = _TmnxMsdpSrcActiveOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 6),
    _TmnxMsdpSrcActiveOriginRP_Type()
)
tmnxMsdpSrcActiveOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveOriginRP.setStatus("current")
_TmnxMsdpSrcActivePrLearnFrType_Type = InetAddressType
_TmnxMsdpSrcActivePrLearnFrType_Object = MibTableColumn
tmnxMsdpSrcActivePrLearnFrType = _TmnxMsdpSrcActivePrLearnFrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 7),
    _TmnxMsdpSrcActivePrLearnFrType_Type()
)
tmnxMsdpSrcActivePrLearnFrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActivePrLearnFrType.setStatus("current")


class _TmnxMsdpSrcActivePeerLearntFrom_Type(InetAddress):
    """Custom type tmnxMsdpSrcActivePeerLearntFrom based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActivePeerLearntFrom_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActivePeerLearntFrom_Object = MibTableColumn
tmnxMsdpSrcActivePeerLearntFrom = _TmnxMsdpSrcActivePeerLearntFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 8),
    _TmnxMsdpSrcActivePeerLearntFrom_Type()
)
tmnxMsdpSrcActivePeerLearntFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActivePeerLearntFrom.setStatus("current")
_TmnxMsdpSrcActiveRPFPeerType_Type = InetAddressType
_TmnxMsdpSrcActiveRPFPeerType_Object = MibTableColumn
tmnxMsdpSrcActiveRPFPeerType = _TmnxMsdpSrcActiveRPFPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 9),
    _TmnxMsdpSrcActiveRPFPeerType_Type()
)
tmnxMsdpSrcActiveRPFPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveRPFPeerType.setStatus("current")


class _TmnxMsdpSrcActiveRPFPeer_Type(InetAddress):
    """Custom type tmnxMsdpSrcActiveRPFPeer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActiveRPFPeer_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActiveRPFPeer_Object = MibTableColumn
tmnxMsdpSrcActiveRPFPeer = _TmnxMsdpSrcActiveRPFPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 10),
    _TmnxMsdpSrcActiveRPFPeer_Type()
)
tmnxMsdpSrcActiveRPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveRPFPeer.setStatus("current")
_TmnxMsdpSrcActiveUpTime_Type = TimeInterval
_TmnxMsdpSrcActiveUpTime_Object = MibTableColumn
tmnxMsdpSrcActiveUpTime = _TmnxMsdpSrcActiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 11),
    _TmnxMsdpSrcActiveUpTime_Type()
)
tmnxMsdpSrcActiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveUpTime.setStatus("current")
_TmnxMsdpSrcActiveExpiryTime_Type = TimeInterval
_TmnxMsdpSrcActiveExpiryTime_Object = MibTableColumn
tmnxMsdpSrcActiveExpiryTime = _TmnxMsdpSrcActiveExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 6, 1, 12),
    _TmnxMsdpSrcActiveExpiryTime_Type()
)
tmnxMsdpSrcActiveExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveExpiryTime.setStatus("current")
_TmnxMsdpPeerStatsTable_Object = MibTable
tmnxMsdpPeerStatsTable = _TmnxMsdpPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7)
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsTable.setStatus("current")
_TmnxMsdpPeerStatsEntry_Object = MibTableRow
tmnxMsdpPeerStatsEntry = _TmnxMsdpPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsEntry.setStatus("current")
_TmnxMsdpPeerStatsActSrcLimExcd_Type = Counter32
_TmnxMsdpPeerStatsActSrcLimExcd_Object = MibTableColumn
tmnxMsdpPeerStatsActSrcLimExcd = _TmnxMsdpPeerStatsActSrcLimExcd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 1),
    _TmnxMsdpPeerStatsActSrcLimExcd_Type()
)
tmnxMsdpPeerStatsActSrcLimExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsActSrcLimExcd.setStatus("current")
_TmnxMsdpPeerStatsLastStChange_Type = TimeInterval
_TmnxMsdpPeerStatsLastStChange_Object = MibTableColumn
tmnxMsdpPeerStatsLastStChange = _TmnxMsdpPeerStatsLastStChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 2),
    _TmnxMsdpPeerStatsLastStChange_Type()
)
tmnxMsdpPeerStatsLastStChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsLastStChange.setStatus("current")
_TmnxMsdpPeerStatsLastMsgPeer_Type = TimeInterval
_TmnxMsdpPeerStatsLastMsgPeer_Object = MibTableColumn
tmnxMsdpPeerStatsLastMsgPeer = _TmnxMsdpPeerStatsLastMsgPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 3),
    _TmnxMsdpPeerStatsLastMsgPeer_Type()
)
tmnxMsdpPeerStatsLastMsgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsLastMsgPeer.setStatus("current")
_TmnxMsdpPeerStatsRPFFailures_Type = Counter32
_TmnxMsdpPeerStatsRPFFailures_Object = MibTableColumn
tmnxMsdpPeerStatsRPFFailures = _TmnxMsdpPeerStatsRPFFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 4),
    _TmnxMsdpPeerStatsRPFFailures_Type()
)
tmnxMsdpPeerStatsRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsRPFFailures.setStatus("current")
_TmnxMsdpPeerStatsRemoteCloses_Type = Counter32
_TmnxMsdpPeerStatsRemoteCloses_Object = MibTableColumn
tmnxMsdpPeerStatsRemoteCloses = _TmnxMsdpPeerStatsRemoteCloses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 5),
    _TmnxMsdpPeerStatsRemoteCloses_Type()
)
tmnxMsdpPeerStatsRemoteCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsRemoteCloses.setStatus("current")
_TmnxMsdpPeerStatsPeerTimeouts_Type = Counter32
_TmnxMsdpPeerStatsPeerTimeouts_Object = MibTableColumn
tmnxMsdpPeerStatsPeerTimeouts = _TmnxMsdpPeerStatsPeerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 6),
    _TmnxMsdpPeerStatsPeerTimeouts_Type()
)
tmnxMsdpPeerStatsPeerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsPeerTimeouts.setStatus("current")
_TmnxMsdpPeerStatsSAMsgsSent_Type = Counter32
_TmnxMsdpPeerStatsSAMsgsSent_Object = MibTableColumn
tmnxMsdpPeerStatsSAMsgsSent = _TmnxMsdpPeerStatsSAMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 7),
    _TmnxMsdpPeerStatsSAMsgsSent_Type()
)
tmnxMsdpPeerStatsSAMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAMsgsSent.setStatus("current")
_TmnxMsdpPeerStatsSAMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsSAMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsSAMsgsRecvd = _TmnxMsdpPeerStatsSAMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 8),
    _TmnxMsdpPeerStatsSAMsgsRecvd_Type()
)
tmnxMsdpPeerStatsSAMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsSAReqMsgsSent_Type = Counter32
_TmnxMsdpPeerStatsSAReqMsgsSent_Object = MibTableColumn
tmnxMsdpPeerStatsSAReqMsgsSent = _TmnxMsdpPeerStatsSAReqMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 9),
    _TmnxMsdpPeerStatsSAReqMsgsSent_Type()
)
tmnxMsdpPeerStatsSAReqMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAReqMsgsSent.setStatus("current")
_TmnxMsdpPeerStatsSAReqMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsSAReqMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsSAReqMsgsRecvd = _TmnxMsdpPeerStatsSAReqMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 10),
    _TmnxMsdpPeerStatsSAReqMsgsRecvd_Type()
)
tmnxMsdpPeerStatsSAReqMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAReqMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsSAResMsgsSent_Type = Counter32
_TmnxMsdpPeerStatsSAResMsgsSent_Object = MibTableColumn
tmnxMsdpPeerStatsSAResMsgsSent = _TmnxMsdpPeerStatsSAResMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 11),
    _TmnxMsdpPeerStatsSAResMsgsSent_Type()
)
tmnxMsdpPeerStatsSAResMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAResMsgsSent.setStatus("current")
_TmnxMsdpPeerStatsSAResMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsSAResMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsSAResMsgsRecvd = _TmnxMsdpPeerStatsSAResMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 12),
    _TmnxMsdpPeerStatsSAResMsgsRecvd_Type()
)
tmnxMsdpPeerStatsSAResMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSAResMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsKAMsgsSent_Type = Counter32
_TmnxMsdpPeerStatsKAMsgsSent_Object = MibTableColumn
tmnxMsdpPeerStatsKAMsgsSent = _TmnxMsdpPeerStatsKAMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 13),
    _TmnxMsdpPeerStatsKAMsgsSent_Type()
)
tmnxMsdpPeerStatsKAMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsKAMsgsSent.setStatus("current")
_TmnxMsdpPeerStatsKAMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsKAMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsKAMsgsRecvd = _TmnxMsdpPeerStatsKAMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 14),
    _TmnxMsdpPeerStatsKAMsgsRecvd_Type()
)
tmnxMsdpPeerStatsKAMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsKAMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsUnknMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsUnknMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsUnknMsgsRecvd = _TmnxMsdpPeerStatsUnknMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 15),
    _TmnxMsdpPeerStatsUnknMsgsRecvd_Type()
)
tmnxMsdpPeerStatsUnknMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsUnknMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsErrorMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsErrorMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsErrorMsgsRecvd = _TmnxMsdpPeerStatsErrorMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 16),
    _TmnxMsdpPeerStatsErrorMsgsRecvd_Type()
)
tmnxMsdpPeerStatsErrorMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsErrorMsgsRecvd.setStatus("current")
_TmnxMsdpPeerStatsSALearnt_Type = Gauge32
_TmnxMsdpPeerStatsSALearnt_Object = MibTableColumn
tmnxMsdpPeerStatsSALearnt = _TmnxMsdpPeerStatsSALearnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 17),
    _TmnxMsdpPeerStatsSALearnt_Type()
)
tmnxMsdpPeerStatsSALearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSALearnt.setStatus("current")
_TmnxMsdpPeerStatsSARejExpPolicy_Type = Counter32
_TmnxMsdpPeerStatsSARejExpPolicy_Object = MibTableColumn
tmnxMsdpPeerStatsSARejExpPolicy = _TmnxMsdpPeerStatsSARejExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 18),
    _TmnxMsdpPeerStatsSARejExpPolicy_Type()
)
tmnxMsdpPeerStatsSARejExpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSARejExpPolicy.setStatus("current")
_TmnxMsdpPeerStatsSARejImpPolicy_Type = Counter32
_TmnxMsdpPeerStatsSARejImpPolicy_Object = MibTableColumn
tmnxMsdpPeerStatsSARejImpPolicy = _TmnxMsdpPeerStatsSARejImpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 19),
    _TmnxMsdpPeerStatsSARejImpPolicy_Type()
)
tmnxMsdpPeerStatsSARejImpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsSARejImpPolicy.setStatus("current")
_TmnxMsdpPeerStatsResvMsgsRecvd_Type = Counter32
_TmnxMsdpPeerStatsResvMsgsRecvd_Object = MibTableColumn
tmnxMsdpPeerStatsResvMsgsRecvd = _TmnxMsdpPeerStatsResvMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 7, 1, 20),
    _TmnxMsdpPeerStatsResvMsgsRecvd_Type()
)
tmnxMsdpPeerStatsResvMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpPeerStatsResvMsgsRecvd.setStatus("current")
_TmnxMsdpSrcActRejTable_Object = MibTable
tmnxMsdpSrcActRejTable = _TmnxMsdpSrcActRejTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8)
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejTable.setStatus("current")
_TmnxMsdpSrcActRejEntry_Object = MibTableRow
tmnxMsdpSrcActRejEntry = _TmnxMsdpSrcActRejEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1)
)
tmnxMsdpSrcActRejEntry.setIndexNames(
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejPeerGroupName"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejGroupAddrType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejGroupAddr"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejSourceAddrType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejSourceAddr"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejOriginRPType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejOriginRP"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejPeerAddrType"),
    (0, "TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejPeerAddr"),
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejEntry.setStatus("current")
_TmnxMsdpSrcActRejPeerGroupName_Type = TNamedItemOrEmpty
_TmnxMsdpSrcActRejPeerGroupName_Object = MibTableColumn
tmnxMsdpSrcActRejPeerGroupName = _TmnxMsdpSrcActRejPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 1),
    _TmnxMsdpSrcActRejPeerGroupName_Type()
)
tmnxMsdpSrcActRejPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejPeerGroupName.setStatus("current")
_TmnxMsdpSrcActRejGroupAddrType_Type = InetAddressType
_TmnxMsdpSrcActRejGroupAddrType_Object = MibTableColumn
tmnxMsdpSrcActRejGroupAddrType = _TmnxMsdpSrcActRejGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 2),
    _TmnxMsdpSrcActRejGroupAddrType_Type()
)
tmnxMsdpSrcActRejGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejGroupAddrType.setStatus("current")


class _TmnxMsdpSrcActRejGroupAddr_Type(InetAddress):
    """Custom type tmnxMsdpSrcActRejGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActRejGroupAddr_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActRejGroupAddr_Object = MibTableColumn
tmnxMsdpSrcActRejGroupAddr = _TmnxMsdpSrcActRejGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 3),
    _TmnxMsdpSrcActRejGroupAddr_Type()
)
tmnxMsdpSrcActRejGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejGroupAddr.setStatus("current")
_TmnxMsdpSrcActRejSourceAddrType_Type = InetAddressType
_TmnxMsdpSrcActRejSourceAddrType_Object = MibTableColumn
tmnxMsdpSrcActRejSourceAddrType = _TmnxMsdpSrcActRejSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 4),
    _TmnxMsdpSrcActRejSourceAddrType_Type()
)
tmnxMsdpSrcActRejSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejSourceAddrType.setStatus("current")


class _TmnxMsdpSrcActRejSourceAddr_Type(InetAddress):
    """Custom type tmnxMsdpSrcActRejSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActRejSourceAddr_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActRejSourceAddr_Object = MibTableColumn
tmnxMsdpSrcActRejSourceAddr = _TmnxMsdpSrcActRejSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 5),
    _TmnxMsdpSrcActRejSourceAddr_Type()
)
tmnxMsdpSrcActRejSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejSourceAddr.setStatus("current")
_TmnxMsdpSrcActRejOriginRPType_Type = InetAddressType
_TmnxMsdpSrcActRejOriginRPType_Object = MibTableColumn
tmnxMsdpSrcActRejOriginRPType = _TmnxMsdpSrcActRejOriginRPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 6),
    _TmnxMsdpSrcActRejOriginRPType_Type()
)
tmnxMsdpSrcActRejOriginRPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejOriginRPType.setStatus("current")


class _TmnxMsdpSrcActRejOriginRP_Type(InetAddress):
    """Custom type tmnxMsdpSrcActRejOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActRejOriginRP_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActRejOriginRP_Object = MibTableColumn
tmnxMsdpSrcActRejOriginRP = _TmnxMsdpSrcActRejOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 7),
    _TmnxMsdpSrcActRejOriginRP_Type()
)
tmnxMsdpSrcActRejOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejOriginRP.setStatus("current")
_TmnxMsdpSrcActRejPeerAddrType_Type = InetAddressType
_TmnxMsdpSrcActRejPeerAddrType_Object = MibTableColumn
tmnxMsdpSrcActRejPeerAddrType = _TmnxMsdpSrcActRejPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 8),
    _TmnxMsdpSrcActRejPeerAddrType_Type()
)
tmnxMsdpSrcActRejPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejPeerAddrType.setStatus("current")


class _TmnxMsdpSrcActRejPeerAddr_Type(InetAddress):
    """Custom type tmnxMsdpSrcActRejPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpSrcActRejPeerAddr_Type.__name__ = "InetAddress"
_TmnxMsdpSrcActRejPeerAddr_Object = MibTableColumn
tmnxMsdpSrcActRejPeerAddr = _TmnxMsdpSrcActRejPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 9),
    _TmnxMsdpSrcActRejPeerAddr_Type()
)
tmnxMsdpSrcActRejPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejPeerAddr.setStatus("current")


class _TmnxMsdpSrcActRejFailureReason_Type(Integer32):
    """Custom type tmnxMsdpSrcActRejFailureReason based on Integer32"""
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
        *(("actSrcLimitExceeded", 4),
          ("exportPolicyFailure", 2),
          ("groupActSrcLimitExceeded", 7),
          ("groupPeerActSrcLimitExceeded", 8),
          ("importPolicyFailure", 1),
          ("peerActSrcLimitExceeded", 6),
          ("rpfFailure", 3),
          ("srcActSrcLimitExceeded", 5))
    )


_TmnxMsdpSrcActRejFailureReason_Type.__name__ = "Integer32"
_TmnxMsdpSrcActRejFailureReason_Object = MibTableColumn
tmnxMsdpSrcActRejFailureReason = _TmnxMsdpSrcActRejFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 43, 8, 1, 10),
    _TmnxMsdpSrcActRejFailureReason_Type()
)
tmnxMsdpSrcActRejFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpSrcActRejFailureReason.setStatus("current")
_TmnxMsdpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMsdpNotifyPrefix = _TmnxMsdpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43)
)
_TmnxMsdpNotifications_ObjectIdentity = ObjectIdentity
tmnxMsdpNotifications = _TmnxMsdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0)
)
tmnxMsdpPeerEntry.registerAugmentions(
    ("TIMETRA-MSDP-MIB",
     "tmnxMsdpPeerStatsEntry")
)
tmnxMsdpPeerStatsEntry.setIndexNames(*tmnxMsdpPeerEntry.getIndexNames())

# Managed Objects groups

tmnxMsdpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 1)
)
tmnxMsdpGlobalGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpMaxActiveSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpMsgRcvRate"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpMsgRcvRateTime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpMsgRcvRateThd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpDataEncapsulation"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpAdminState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpExportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpExportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpExportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpExportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpExportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpImportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpImportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpImportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpImportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpImportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpLocalAddress"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpLocalAddressType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusPeerCount"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusPeersEstablished"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusSACount"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusLastTimeUp"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusActSrcLimExceeded"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpRpfLookupSequence"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSACacheLifetime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSARejectExportPolicy"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSARejectImportPolicy"))
)
if mibBuilder.loadTexts:
    tmnxMsdpGlobalGroup.setStatus("current")

tmnxMsdpPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 2)
)
tmnxMsdpPeerGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpPeerRowStatus"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerMaxActiveSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerMsgRcvRate"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerMsgRcvRateTime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerMsgRcvRateThd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerAuthKey"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerAuthKeyEncrypted"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerDefaultPeer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerAdminState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerExportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerExportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerExportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerExportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerExportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerImportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerImportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerImportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerImportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerImportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerLocalAddressType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerLocalAddress"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerRowStatus"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerMaxActSrcs"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerMsgRcvRt"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerMsgRcvRtTime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerMsgRcvRtThd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerAuthKey"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerAKeyEncrypt"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerDefaultPeer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerAdminState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerExportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerExportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerExportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerExportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerExportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerImportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerImportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerImportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerImportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerImportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerLocAddrType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerLocalAddress"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsActSrcLimExcd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsLastStChange"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsLastMsgPeer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsRPFFailures"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsRemoteCloses"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsPeerTimeouts"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAMsgsSent"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAReqMsgsSent"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAReqMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAResMsgsSent"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSAResMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsKAMsgsSent"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsKAMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsUnknMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsErrorMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSALearnt"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSARejExpPolicy"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsSARejImpPolicy"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsResvMsgsRecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerLastUpOrDown"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerConRetry"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStateTimer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerTimeout"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerSAAccepted"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerSARecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerLastASLimit"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerLastUpOrDown"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerConRetry"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerStateTimer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerTimeout"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerSAAccepted"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerSARecvd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpPeerLastASLimit"))
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroup.setStatus("current")

tmnxMsdpPeerGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 3)
)
tmnxMsdpPeerGroupGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupRowStatus"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMsgRcvRate"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMsgRcvRateTime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMsgRcvRateThd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupAdminState"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupExportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupExportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupExportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupExportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupExportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupImportPolicy1"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupImportPolicy2"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupImportPolicy3"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupImportPolicy4"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupImportPolicy5"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupLocalAddrType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupLocalAddress"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMode"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMaxActSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupActMsgsExMax"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpSARejExpPolicy"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGrpSARejImpPolicy"))
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerGroupGroup.setStatus("current")

tmnxMsdpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 4)
)
tmnxMsdpSourceGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpSourceRowStatus"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceMaxActiveSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceDiscMethod"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceSrcActMsgsExMax"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceLastExEventTime"))
)
if mibBuilder.loadTexts:
    tmnxMsdpSourceGroup.setStatus("current")

tmnxMsdpSrcActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 5)
)
tmnxMsdpSrcActiveGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActivePrLearnFrType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActivePeerLearntFrom"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveRPFPeerType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveRPFPeer"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveUpTime"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveGroup.setStatus("current")

tmnxMsdpSrcActiveRejGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 7)
)
tmnxMsdpSrcActiveRejGroup.setObjects(
    ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActRejFailureReason")
)
if mibBuilder.loadTexts:
    tmnxMsdpSrcActiveRejGroup.setStatus("current")


# Notification objects

tmnxMsdpActSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0, 1)
)
tmnxMsdpActSrcLimExcd.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpMaxActiveSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpStatusActSrcLimExceeded"))
)
if mibBuilder.loadTexts:
    tmnxMsdpActSrcLimExcd.setStatus(
        "current"
    )

tmnxMsdpPeerActSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0, 2)
)
tmnxMsdpPeerActSrcLimExcd.setObjects(
    ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerStatsActSrcLimExcd")
)
if mibBuilder.loadTexts:
    tmnxMsdpPeerActSrcLimExcd.setStatus(
        "current"
    )

tmnxMsdpRPFFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0, 3)
)
tmnxMsdpRPFFailure.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveRPFPeerType"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSrcActiveRPFPeer"))
)
if mibBuilder.loadTexts:
    tmnxMsdpRPFFailure.setStatus(
        "current"
    )

tmnxMsdpSourceSrcActMsgsExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0, 4)
)
tmnxMsdpSourceSrcActMsgsExcd.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpSourceMaxActiveSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceSrcActMsgsExMax"))
)
if mibBuilder.loadTexts:
    tmnxMsdpSourceSrcActMsgsExcd.setStatus(
        "current"
    )

tmnxMsdpGroupSrcActMsgsExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 43, 0, 5)
)
tmnxMsdpGroupSrcActMsgsExcd.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupMaxActSources"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerGroupActMsgsExMax"))
)
if mibBuilder.loadTexts:
    tmnxMsdpGroupSrcActMsgsExcd.setStatus(
        "current"
    )


# Notifications groups

tmnxMsdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 2, 6)
)
tmnxMsdpNotificationGroup.setObjects(
      *(("TIMETRA-MSDP-MIB", "tmnxMsdpActSrcLimExcd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpPeerActSrcLimExcd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpRPFFailure"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpSourceSrcActMsgsExcd"),
        ("TIMETRA-MSDP-MIB", "tmnxMsdpGroupSrcActMsgsExcd"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMsdpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMsdpCompliance.setStatus(
        "obsolete"
    )

tmnxMsdpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 43, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMsdpV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MSDP-MIB",
    **{"timetraMsdpMIBModule": timetraMsdpMIBModule,
       "tmnxMsdpConformance": tmnxMsdpConformance,
       "tmnxMsdpCompliances": tmnxMsdpCompliances,
       "tmnxMsdpCompliance": tmnxMsdpCompliance,
       "tmnxMsdpV10v0Compliance": tmnxMsdpV10v0Compliance,
       "tmnxMsdpGroups": tmnxMsdpGroups,
       "tmnxMsdpGlobalGroup": tmnxMsdpGlobalGroup,
       "tmnxMsdpPeerGroup": tmnxMsdpPeerGroup,
       "tmnxMsdpPeerGroupGroup": tmnxMsdpPeerGroupGroup,
       "tmnxMsdpSourceGroup": tmnxMsdpSourceGroup,
       "tmnxMsdpSrcActiveGroup": tmnxMsdpSrcActiveGroup,
       "tmnxMsdpNotificationGroup": tmnxMsdpNotificationGroup,
       "tmnxMsdpSrcActiveRejGroup": tmnxMsdpSrcActiveRejGroup,
       "tmnxMsdpObjects": tmnxMsdpObjects,
       "tmnxMsdpGlobals": tmnxMsdpGlobals,
       "tmnxMsdpMaxActiveSources": tmnxMsdpMaxActiveSources,
       "tmnxMsdpMsgRcvRate": tmnxMsdpMsgRcvRate,
       "tmnxMsdpMsgRcvRateTime": tmnxMsdpMsgRcvRateTime,
       "tmnxMsdpMsgRcvRateThd": tmnxMsdpMsgRcvRateThd,
       "tmnxMsdpDataEncapsulation": tmnxMsdpDataEncapsulation,
       "tmnxMsdpAdminState": tmnxMsdpAdminState,
       "tmnxMsdpExportPolicy1": tmnxMsdpExportPolicy1,
       "tmnxMsdpExportPolicy2": tmnxMsdpExportPolicy2,
       "tmnxMsdpExportPolicy3": tmnxMsdpExportPolicy3,
       "tmnxMsdpExportPolicy4": tmnxMsdpExportPolicy4,
       "tmnxMsdpExportPolicy5": tmnxMsdpExportPolicy5,
       "tmnxMsdpImportPolicy1": tmnxMsdpImportPolicy1,
       "tmnxMsdpImportPolicy2": tmnxMsdpImportPolicy2,
       "tmnxMsdpImportPolicy3": tmnxMsdpImportPolicy3,
       "tmnxMsdpImportPolicy4": tmnxMsdpImportPolicy4,
       "tmnxMsdpImportPolicy5": tmnxMsdpImportPolicy5,
       "tmnxMsdpLocalAddressType": tmnxMsdpLocalAddressType,
       "tmnxMsdpLocalAddress": tmnxMsdpLocalAddress,
       "tmnxMsdpStatusPeerCount": tmnxMsdpStatusPeerCount,
       "tmnxMsdpStatusPeersEstablished": tmnxMsdpStatusPeersEstablished,
       "tmnxMsdpStatusSACount": tmnxMsdpStatusSACount,
       "tmnxMsdpStatusLastTimeUp": tmnxMsdpStatusLastTimeUp,
       "tmnxMsdpStatusActSrcLimExceeded": tmnxMsdpStatusActSrcLimExceeded,
       "tmnxMsdpRpfLookupSequence": tmnxMsdpRpfLookupSequence,
       "tmnxMsdpSACacheLifetime": tmnxMsdpSACacheLifetime,
       "tmnxMsdpSARejectExportPolicy": tmnxMsdpSARejectExportPolicy,
       "tmnxMsdpSARejectImportPolicy": tmnxMsdpSARejectImportPolicy,
       "tmnxMsdpPeerTable": tmnxMsdpPeerTable,
       "tmnxMsdpPeerEntry": tmnxMsdpPeerEntry,
       "tmnxMsdpPeerAddressType": tmnxMsdpPeerAddressType,
       "tmnxMsdpPeerAddress": tmnxMsdpPeerAddress,
       "tmnxMsdpPeerRowStatus": tmnxMsdpPeerRowStatus,
       "tmnxMsdpPeerMaxActiveSources": tmnxMsdpPeerMaxActiveSources,
       "tmnxMsdpPeerMsgRcvRate": tmnxMsdpPeerMsgRcvRate,
       "tmnxMsdpPeerMsgRcvRateTime": tmnxMsdpPeerMsgRcvRateTime,
       "tmnxMsdpPeerMsgRcvRateThd": tmnxMsdpPeerMsgRcvRateThd,
       "tmnxMsdpPeerAuthKey": tmnxMsdpPeerAuthKey,
       "tmnxMsdpPeerAuthKeyEncrypted": tmnxMsdpPeerAuthKeyEncrypted,
       "tmnxMsdpPeerDefaultPeer": tmnxMsdpPeerDefaultPeer,
       "tmnxMsdpPeerAdminState": tmnxMsdpPeerAdminState,
       "tmnxMsdpPeerExportPolicy1": tmnxMsdpPeerExportPolicy1,
       "tmnxMsdpPeerExportPolicy2": tmnxMsdpPeerExportPolicy2,
       "tmnxMsdpPeerExportPolicy3": tmnxMsdpPeerExportPolicy3,
       "tmnxMsdpPeerExportPolicy4": tmnxMsdpPeerExportPolicy4,
       "tmnxMsdpPeerExportPolicy5": tmnxMsdpPeerExportPolicy5,
       "tmnxMsdpPeerImportPolicy1": tmnxMsdpPeerImportPolicy1,
       "tmnxMsdpPeerImportPolicy2": tmnxMsdpPeerImportPolicy2,
       "tmnxMsdpPeerImportPolicy3": tmnxMsdpPeerImportPolicy3,
       "tmnxMsdpPeerImportPolicy4": tmnxMsdpPeerImportPolicy4,
       "tmnxMsdpPeerImportPolicy5": tmnxMsdpPeerImportPolicy5,
       "tmnxMsdpPeerLocalAddressType": tmnxMsdpPeerLocalAddressType,
       "tmnxMsdpPeerLocalAddress": tmnxMsdpPeerLocalAddress,
       "tmnxMsdpPeerState": tmnxMsdpPeerState,
       "tmnxMsdpPeerLastUpOrDown": tmnxMsdpPeerLastUpOrDown,
       "tmnxMsdpPeerConRetry": tmnxMsdpPeerConRetry,
       "tmnxMsdpPeerStateTimer": tmnxMsdpPeerStateTimer,
       "tmnxMsdpPeerTimeout": tmnxMsdpPeerTimeout,
       "tmnxMsdpPeerSAAccepted": tmnxMsdpPeerSAAccepted,
       "tmnxMsdpPeerSARecvd": tmnxMsdpPeerSARecvd,
       "tmnxMsdpPeerLastASLimit": tmnxMsdpPeerLastASLimit,
       "tmnxMsdpPeerGroupTable": tmnxMsdpPeerGroupTable,
       "tmnxMsdpPeerGroupEntry": tmnxMsdpPeerGroupEntry,
       "tmnxMsdpPeerGroupName": tmnxMsdpPeerGroupName,
       "tmnxMsdpPeerGroupRowStatus": tmnxMsdpPeerGroupRowStatus,
       "tmnxMsdpPeerGroupMsgRcvRate": tmnxMsdpPeerGroupMsgRcvRate,
       "tmnxMsdpPeerGroupMsgRcvRateTime": tmnxMsdpPeerGroupMsgRcvRateTime,
       "tmnxMsdpPeerGroupMsgRcvRateThd": tmnxMsdpPeerGroupMsgRcvRateThd,
       "tmnxMsdpPeerGroupAdminState": tmnxMsdpPeerGroupAdminState,
       "tmnxMsdpPeerGroupExportPolicy1": tmnxMsdpPeerGroupExportPolicy1,
       "tmnxMsdpPeerGroupExportPolicy2": tmnxMsdpPeerGroupExportPolicy2,
       "tmnxMsdpPeerGroupExportPolicy3": tmnxMsdpPeerGroupExportPolicy3,
       "tmnxMsdpPeerGroupExportPolicy4": tmnxMsdpPeerGroupExportPolicy4,
       "tmnxMsdpPeerGroupExportPolicy5": tmnxMsdpPeerGroupExportPolicy5,
       "tmnxMsdpPeerGroupImportPolicy1": tmnxMsdpPeerGroupImportPolicy1,
       "tmnxMsdpPeerGroupImportPolicy2": tmnxMsdpPeerGroupImportPolicy2,
       "tmnxMsdpPeerGroupImportPolicy3": tmnxMsdpPeerGroupImportPolicy3,
       "tmnxMsdpPeerGroupImportPolicy4": tmnxMsdpPeerGroupImportPolicy4,
       "tmnxMsdpPeerGroupImportPolicy5": tmnxMsdpPeerGroupImportPolicy5,
       "tmnxMsdpPeerGroupLocalAddrType": tmnxMsdpPeerGroupLocalAddrType,
       "tmnxMsdpPeerGroupLocalAddress": tmnxMsdpPeerGroupLocalAddress,
       "tmnxMsdpPeerGroupMode": tmnxMsdpPeerGroupMode,
       "tmnxMsdpPeerGroupMaxActSources": tmnxMsdpPeerGroupMaxActSources,
       "tmnxMsdpPeerGroupActMsgsExMax": tmnxMsdpPeerGroupActMsgsExMax,
       "tmnxMsdpPeerGrpSARejExpPolicy": tmnxMsdpPeerGrpSARejExpPolicy,
       "tmnxMsdpPeerGrpSARejImpPolicy": tmnxMsdpPeerGrpSARejImpPolicy,
       "tmnxMsdpPeerGrpPeerTable": tmnxMsdpPeerGrpPeerTable,
       "tmnxMsdpPeerGrpPeerEntry": tmnxMsdpPeerGrpPeerEntry,
       "tmnxMsdpPeerGrpPeerAddressType": tmnxMsdpPeerGrpPeerAddressType,
       "tmnxMsdpPeerGrpPeerAddress": tmnxMsdpPeerGrpPeerAddress,
       "tmnxMsdpPeerGrpPeerRowStatus": tmnxMsdpPeerGrpPeerRowStatus,
       "tmnxMsdpPeerGrpPeerMaxActSrcs": tmnxMsdpPeerGrpPeerMaxActSrcs,
       "tmnxMsdpPeerGrpPeerMsgRcvRt": tmnxMsdpPeerGrpPeerMsgRcvRt,
       "tmnxMsdpPeerGrpPeerMsgRcvRtTime": tmnxMsdpPeerGrpPeerMsgRcvRtTime,
       "tmnxMsdpPeerGrpPeerMsgRcvRtThd": tmnxMsdpPeerGrpPeerMsgRcvRtThd,
       "tmnxMsdpPeerGrpPeerAuthKey": tmnxMsdpPeerGrpPeerAuthKey,
       "tmnxMsdpPeerGrpPeerAKeyEncrypt": tmnxMsdpPeerGrpPeerAKeyEncrypt,
       "tmnxMsdpPeerGrpPeerDefaultPeer": tmnxMsdpPeerGrpPeerDefaultPeer,
       "tmnxMsdpPeerGrpPeerAdminState": tmnxMsdpPeerGrpPeerAdminState,
       "tmnxMsdpPeerGrpPeerExportPolicy1": tmnxMsdpPeerGrpPeerExportPolicy1,
       "tmnxMsdpPeerGrpPeerExportPolicy2": tmnxMsdpPeerGrpPeerExportPolicy2,
       "tmnxMsdpPeerGrpPeerExportPolicy3": tmnxMsdpPeerGrpPeerExportPolicy3,
       "tmnxMsdpPeerGrpPeerExportPolicy4": tmnxMsdpPeerGrpPeerExportPolicy4,
       "tmnxMsdpPeerGrpPeerExportPolicy5": tmnxMsdpPeerGrpPeerExportPolicy5,
       "tmnxMsdpPeerGrpPeerImportPolicy1": tmnxMsdpPeerGrpPeerImportPolicy1,
       "tmnxMsdpPeerGrpPeerImportPolicy2": tmnxMsdpPeerGrpPeerImportPolicy2,
       "tmnxMsdpPeerGrpPeerImportPolicy3": tmnxMsdpPeerGrpPeerImportPolicy3,
       "tmnxMsdpPeerGrpPeerImportPolicy4": tmnxMsdpPeerGrpPeerImportPolicy4,
       "tmnxMsdpPeerGrpPeerImportPolicy5": tmnxMsdpPeerGrpPeerImportPolicy5,
       "tmnxMsdpPeerGrpPeerLocAddrType": tmnxMsdpPeerGrpPeerLocAddrType,
       "tmnxMsdpPeerGrpPeerLocalAddress": tmnxMsdpPeerGrpPeerLocalAddress,
       "tmnxMsdpPeerGrpPeerState": tmnxMsdpPeerGrpPeerState,
       "tmnxMsdpPeerGrpPeerLastUpOrDown": tmnxMsdpPeerGrpPeerLastUpOrDown,
       "tmnxMsdpPeerGrpPeerConRetry": tmnxMsdpPeerGrpPeerConRetry,
       "tmnxMsdpPeerGrpPeerStateTimer": tmnxMsdpPeerGrpPeerStateTimer,
       "tmnxMsdpPeerGrpPeerTimeout": tmnxMsdpPeerGrpPeerTimeout,
       "tmnxMsdpPeerGrpPeerSAAccepted": tmnxMsdpPeerGrpPeerSAAccepted,
       "tmnxMsdpPeerGrpPeerSARecvd": tmnxMsdpPeerGrpPeerSARecvd,
       "tmnxMsdpPeerGrpPeerLastASLimit": tmnxMsdpPeerGrpPeerLastASLimit,
       "tmnxMsdpSourceTable": tmnxMsdpSourceTable,
       "tmnxMsdpSourceEntry": tmnxMsdpSourceEntry,
       "tmnxMsdpSourcePrefixType": tmnxMsdpSourcePrefixType,
       "tmnxMsdpSourcePrefix": tmnxMsdpSourcePrefix,
       "tmnxMsdpSourceMask": tmnxMsdpSourceMask,
       "tmnxMsdpSourceRowStatus": tmnxMsdpSourceRowStatus,
       "tmnxMsdpSourceMaxActiveSources": tmnxMsdpSourceMaxActiveSources,
       "tmnxMsdpSourceDiscMethod": tmnxMsdpSourceDiscMethod,
       "tmnxMsdpSourceSrcActMsgsExMax": tmnxMsdpSourceSrcActMsgsExMax,
       "tmnxMsdpSourceLastExEventTime": tmnxMsdpSourceLastExEventTime,
       "tmnxMsdpSrcActiveTable": tmnxMsdpSrcActiveTable,
       "tmnxMsdpSrcActiveEntry": tmnxMsdpSrcActiveEntry,
       "tmnxMsdpSrcActiveGroupAddrType": tmnxMsdpSrcActiveGroupAddrType,
       "tmnxMsdpSrcActiveGroupAddr": tmnxMsdpSrcActiveGroupAddr,
       "tmnxMsdpSrcActiveSourceAddrType": tmnxMsdpSrcActiveSourceAddrType,
       "tmnxMsdpSrcActiveSourceAddr": tmnxMsdpSrcActiveSourceAddr,
       "tmnxMsdpSrcActiveOriginRPType": tmnxMsdpSrcActiveOriginRPType,
       "tmnxMsdpSrcActiveOriginRP": tmnxMsdpSrcActiveOriginRP,
       "tmnxMsdpSrcActivePrLearnFrType": tmnxMsdpSrcActivePrLearnFrType,
       "tmnxMsdpSrcActivePeerLearntFrom": tmnxMsdpSrcActivePeerLearntFrom,
       "tmnxMsdpSrcActiveRPFPeerType": tmnxMsdpSrcActiveRPFPeerType,
       "tmnxMsdpSrcActiveRPFPeer": tmnxMsdpSrcActiveRPFPeer,
       "tmnxMsdpSrcActiveUpTime": tmnxMsdpSrcActiveUpTime,
       "tmnxMsdpSrcActiveExpiryTime": tmnxMsdpSrcActiveExpiryTime,
       "tmnxMsdpPeerStatsTable": tmnxMsdpPeerStatsTable,
       "tmnxMsdpPeerStatsEntry": tmnxMsdpPeerStatsEntry,
       "tmnxMsdpPeerStatsActSrcLimExcd": tmnxMsdpPeerStatsActSrcLimExcd,
       "tmnxMsdpPeerStatsLastStChange": tmnxMsdpPeerStatsLastStChange,
       "tmnxMsdpPeerStatsLastMsgPeer": tmnxMsdpPeerStatsLastMsgPeer,
       "tmnxMsdpPeerStatsRPFFailures": tmnxMsdpPeerStatsRPFFailures,
       "tmnxMsdpPeerStatsRemoteCloses": tmnxMsdpPeerStatsRemoteCloses,
       "tmnxMsdpPeerStatsPeerTimeouts": tmnxMsdpPeerStatsPeerTimeouts,
       "tmnxMsdpPeerStatsSAMsgsSent": tmnxMsdpPeerStatsSAMsgsSent,
       "tmnxMsdpPeerStatsSAMsgsRecvd": tmnxMsdpPeerStatsSAMsgsRecvd,
       "tmnxMsdpPeerStatsSAReqMsgsSent": tmnxMsdpPeerStatsSAReqMsgsSent,
       "tmnxMsdpPeerStatsSAReqMsgsRecvd": tmnxMsdpPeerStatsSAReqMsgsRecvd,
       "tmnxMsdpPeerStatsSAResMsgsSent": tmnxMsdpPeerStatsSAResMsgsSent,
       "tmnxMsdpPeerStatsSAResMsgsRecvd": tmnxMsdpPeerStatsSAResMsgsRecvd,
       "tmnxMsdpPeerStatsKAMsgsSent": tmnxMsdpPeerStatsKAMsgsSent,
       "tmnxMsdpPeerStatsKAMsgsRecvd": tmnxMsdpPeerStatsKAMsgsRecvd,
       "tmnxMsdpPeerStatsUnknMsgsRecvd": tmnxMsdpPeerStatsUnknMsgsRecvd,
       "tmnxMsdpPeerStatsErrorMsgsRecvd": tmnxMsdpPeerStatsErrorMsgsRecvd,
       "tmnxMsdpPeerStatsSALearnt": tmnxMsdpPeerStatsSALearnt,
       "tmnxMsdpPeerStatsSARejExpPolicy": tmnxMsdpPeerStatsSARejExpPolicy,
       "tmnxMsdpPeerStatsSARejImpPolicy": tmnxMsdpPeerStatsSARejImpPolicy,
       "tmnxMsdpPeerStatsResvMsgsRecvd": tmnxMsdpPeerStatsResvMsgsRecvd,
       "tmnxMsdpSrcActRejTable": tmnxMsdpSrcActRejTable,
       "tmnxMsdpSrcActRejEntry": tmnxMsdpSrcActRejEntry,
       "tmnxMsdpSrcActRejPeerGroupName": tmnxMsdpSrcActRejPeerGroupName,
       "tmnxMsdpSrcActRejGroupAddrType": tmnxMsdpSrcActRejGroupAddrType,
       "tmnxMsdpSrcActRejGroupAddr": tmnxMsdpSrcActRejGroupAddr,
       "tmnxMsdpSrcActRejSourceAddrType": tmnxMsdpSrcActRejSourceAddrType,
       "tmnxMsdpSrcActRejSourceAddr": tmnxMsdpSrcActRejSourceAddr,
       "tmnxMsdpSrcActRejOriginRPType": tmnxMsdpSrcActRejOriginRPType,
       "tmnxMsdpSrcActRejOriginRP": tmnxMsdpSrcActRejOriginRP,
       "tmnxMsdpSrcActRejPeerAddrType": tmnxMsdpSrcActRejPeerAddrType,
       "tmnxMsdpSrcActRejPeerAddr": tmnxMsdpSrcActRejPeerAddr,
       "tmnxMsdpSrcActRejFailureReason": tmnxMsdpSrcActRejFailureReason,
       "tmnxMsdpNotifyPrefix": tmnxMsdpNotifyPrefix,
       "tmnxMsdpNotifications": tmnxMsdpNotifications,
       "tmnxMsdpActSrcLimExcd": tmnxMsdpActSrcLimExcd,
       "tmnxMsdpPeerActSrcLimExcd": tmnxMsdpPeerActSrcLimExcd,
       "tmnxMsdpRPFFailure": tmnxMsdpRPFFailure,
       "tmnxMsdpSourceSrcActMsgsExcd": tmnxMsdpSourceSrcActMsgsExcd,
       "tmnxMsdpGroupSrcActMsgsExcd": tmnxMsdpGroupSrcActMsgsExcd}
)
