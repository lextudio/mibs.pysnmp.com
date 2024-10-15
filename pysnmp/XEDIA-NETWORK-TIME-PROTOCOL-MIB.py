# SNMP MIB module (XEDIA-NETWORK-TIME-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-NETWORK-TIME-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:59 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaNetworkTimeProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XntpIpAddress(IpAddress, TextualConvention):
    status = "current"


class XntpPort(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class XntpDateAndTime(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )



class XntpSeconds(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )



class XntpAssociationMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("client", 3),
          ("server", 4),
          ("symActive", 1),
          ("symPassive", 2),
          ("unspecifed", 0))
    )



class XntpLeapIndication(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("deleteSecond", 2),
          ("insertSecond", 1),
          ("noWarning", 0),
          ("unsyncronized", 3))
    )



class XntpCounter(Counter32, TextualConvention):
    status = "current"
    displayHint = "d"


class XntpAssociationCondition(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("distSysPeer", 5),
          ("eliminated", 1),
          ("falseticker", 2),
          ("outlyer", 3),
          ("rejected", 0),
          ("syncCandidate", 4),
          ("sysPeer", 6))
    )



class XntpReachability(Integer32, TextualConvention):
    status = "current"
    displayHint = "o"


# MIB Managed Objects in the order of their OIDs

_XntpObjects_ObjectIdentity = ObjectIdentity
xntpObjects = _XntpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1)
)
_XntpSystem_ObjectIdentity = ObjectIdentity
xntpSystem = _XntpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1)
)


class _XntpAdminStatus_Type(Integer32):
    """Custom type xntpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XntpAdminStatus_Type.__name__ = "Integer32"
_XntpAdminStatus_Object = MibScalar
xntpAdminStatus = _XntpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 1),
    _XntpAdminStatus_Type()
)
xntpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xntpAdminStatus.setStatus("current")


class _XntpSrcAddressStatus_Type(Integer32):
    """Custom type xntpSrcAddressStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XntpSrcAddressStatus_Type.__name__ = "Integer32"
_XntpSrcAddressStatus_Object = MibScalar
xntpSrcAddressStatus = _XntpSrcAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 2),
    _XntpSrcAddressStatus_Type()
)
xntpSrcAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xntpSrcAddressStatus.setStatus("current")
_XntpStratum_Type = Integer32
_XntpStratum_Object = MibScalar
xntpStratum = _XntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 3),
    _XntpStratum_Type()
)
xntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpStratum.setStatus("current")
_XntpMode_Type = XntpAssociationMode
_XntpMode_Object = MibScalar
xntpMode = _XntpMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 4),
    _XntpMode_Type()
)
xntpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpMode.setStatus("current")
_XntpPrecision_Type = Integer32
_XntpPrecision_Object = MibScalar
xntpPrecision = _XntpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 5),
    _XntpPrecision_Type()
)
xntpPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpPrecision.setStatus("current")
_XntpClockSource_Type = XntpIpAddress
_XntpClockSource_Object = MibScalar
xntpClockSource = _XntpClockSource_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 6),
    _XntpClockSource_Type()
)
xntpClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpClockSource.setStatus("current")
_XntpPollInterval_Type = Integer32
_XntpPollInterval_Object = MibScalar
xntpPollInterval = _XntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 7),
    _XntpPollInterval_Type()
)
xntpPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpPollInterval.setStatus("current")
_XntpLeapIndicator_Type = XntpLeapIndication
_XntpLeapIndicator_Object = MibScalar
xntpLeapIndicator = _XntpLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 8),
    _XntpLeapIndicator_Type()
)
xntpLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpLeapIndicator.setStatus("current")
_XntpRootDelay_Type = XntpSeconds
_XntpRootDelay_Object = MibScalar
xntpRootDelay = _XntpRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 9),
    _XntpRootDelay_Type()
)
xntpRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpRootDelay.setStatus("current")
_XntpRootDispersion_Type = XntpSeconds
_XntpRootDispersion_Object = MibScalar
xntpRootDispersion = _XntpRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 10),
    _XntpRootDispersion_Type()
)
xntpRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpRootDispersion.setStatus("current")
_XntpReferenceTimestamp_Type = XntpDateAndTime
_XntpReferenceTimestamp_Object = MibScalar
xntpReferenceTimestamp = _XntpReferenceTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 11),
    _XntpReferenceTimestamp_Type()
)
xntpReferenceTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpReferenceTimestamp.setStatus("current")
_XntpLocalTime_Type = XntpDateAndTime
_XntpLocalTime_Object = MibScalar
xntpLocalTime = _XntpLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 12),
    _XntpLocalTime_Type()
)
xntpLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpLocalTime.setStatus("current")
_XntpCounters_ObjectIdentity = ObjectIdentity
xntpCounters = _XntpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2)
)
_XntpPacketsIn_Type = XntpCounter
_XntpPacketsIn_Object = MibScalar
xntpPacketsIn = _XntpPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 1),
    _XntpPacketsIn_Type()
)
xntpPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpPacketsIn.setStatus("current")
_XntpBadVersion_Type = XntpCounter
_XntpBadVersion_Object = MibScalar
xntpBadVersion = _XntpBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 2),
    _XntpBadVersion_Type()
)
xntpBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadVersion.setStatus("current")
_XntpBadStratum_Type = XntpCounter
_XntpBadStratum_Object = MibScalar
xntpBadStratum = _XntpBadStratum_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 3),
    _XntpBadStratum_Type()
)
xntpBadStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadStratum.setStatus("current")
_XntpBadLength_Type = XntpCounter
_XntpBadLength_Object = MibScalar
xntpBadLength = _XntpBadLength_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 4),
    _XntpBadLength_Type()
)
xntpBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadLength.setStatus("current")
_XntpBadMode_Type = XntpCounter
_XntpBadMode_Object = MibScalar
xntpBadMode = _XntpBadMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 5),
    _XntpBadMode_Type()
)
xntpBadMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadMode.setStatus("current")
_XntpBadHeader_Type = XntpCounter
_XntpBadHeader_Object = MibScalar
xntpBadHeader = _XntpBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 6),
    _XntpBadHeader_Type()
)
xntpBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadHeader.setStatus("current")
_XntpBadData_Type = XntpCounter
_XntpBadData_Object = MibScalar
xntpBadData = _XntpBadData_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 7),
    _XntpBadData_Type()
)
xntpBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpBadData.setStatus("current")
_XntpPacketsOut_Type = XntpCounter
_XntpPacketsOut_Object = MibScalar
xntpPacketsOut = _XntpPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 8),
    _XntpPacketsOut_Type()
)
xntpPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpPacketsOut.setStatus("current")
_XntpPhaseAdjustments_Type = XntpCounter
_XntpPhaseAdjustments_Object = MibScalar
xntpPhaseAdjustments = _XntpPhaseAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 9),
    _XntpPhaseAdjustments_Type()
)
xntpPhaseAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpPhaseAdjustments.setStatus("current")
_XntpStepAdjustments_Type = XntpCounter
_XntpStepAdjustments_Object = MibScalar
xntpStepAdjustments = _XntpStepAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 10),
    _XntpStepAdjustments_Type()
)
xntpStepAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpStepAdjustments.setStatus("current")
_XntpServerTable_Object = MibTable
xntpServerTable = _XntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3)
)
if mibBuilder.loadTexts:
    xntpServerTable.setStatus("current")
_XntpServerEntry_Object = MibTableRow
xntpServerEntry = _XntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1)
)
xntpServerEntry.setIndexNames(
    (0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServer"),
)
if mibBuilder.loadTexts:
    xntpServerEntry.setStatus("current")
_XntpServer_Type = XntpIpAddress
_XntpServer_Object = MibTableColumn
xntpServer = _XntpServer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 1),
    _XntpServer_Type()
)
xntpServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xntpServer.setStatus("current")


class _XntpServerVersion_Type(Integer32):
    """Custom type xntpServerVersion based on Integer32"""
    defaultValue = 3


_XntpServerVersion_Object = MibTableColumn
xntpServerVersion = _XntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 2),
    _XntpServerVersion_Type()
)
xntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpServerVersion.setStatus("current")


class _XntpServerMinPoll_Type(Integer32):
    """Custom type xntpServerMinPoll based on Integer32"""
    defaultValue = 6


_XntpServerMinPoll_Object = MibTableColumn
xntpServerMinPoll = _XntpServerMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 3),
    _XntpServerMinPoll_Type()
)
xntpServerMinPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpServerMinPoll.setStatus("current")


class _XntpServerMaxPoll_Type(Integer32):
    """Custom type xntpServerMaxPoll based on Integer32"""
    defaultValue = 10


_XntpServerMaxPoll_Object = MibTableColumn
xntpServerMaxPoll = _XntpServerMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 4),
    _XntpServerMaxPoll_Type()
)
xntpServerMaxPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpServerMaxPoll.setStatus("current")
_XntpServerRowStatus_Type = RowStatus
_XntpServerRowStatus_Object = MibTableColumn
xntpServerRowStatus = _XntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 5),
    _XntpServerRowStatus_Type()
)
xntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpServerRowStatus.setStatus("current")
_XntpSAPeerTable_Object = MibTable
xntpSAPeerTable = _XntpSAPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4)
)
if mibBuilder.loadTexts:
    xntpSAPeerTable.setStatus("current")
_XntpSAPeerEntry_Object = MibTableRow
xntpSAPeerEntry = _XntpSAPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1)
)
xntpSAPeerEntry.setIndexNames(
    (0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeer"),
)
if mibBuilder.loadTexts:
    xntpSAPeerEntry.setStatus("current")
_XntpSAPeer_Type = XntpIpAddress
_XntpSAPeer_Object = MibTableColumn
xntpSAPeer = _XntpSAPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 1),
    _XntpSAPeer_Type()
)
xntpSAPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xntpSAPeer.setStatus("current")


class _XntpSAPeerVersion_Type(Integer32):
    """Custom type xntpSAPeerVersion based on Integer32"""
    defaultValue = 3


_XntpSAPeerVersion_Object = MibTableColumn
xntpSAPeerVersion = _XntpSAPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 2),
    _XntpSAPeerVersion_Type()
)
xntpSAPeerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpSAPeerVersion.setStatus("current")


class _XntpSAPeerMinPoll_Type(Integer32):
    """Custom type xntpSAPeerMinPoll based on Integer32"""
    defaultValue = 6


_XntpSAPeerMinPoll_Object = MibTableColumn
xntpSAPeerMinPoll = _XntpSAPeerMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 3),
    _XntpSAPeerMinPoll_Type()
)
xntpSAPeerMinPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpSAPeerMinPoll.setStatus("current")


class _XntpSAPeerMaxPoll_Type(Integer32):
    """Custom type xntpSAPeerMaxPoll based on Integer32"""
    defaultValue = 10


_XntpSAPeerMaxPoll_Object = MibTableColumn
xntpSAPeerMaxPoll = _XntpSAPeerMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 4),
    _XntpSAPeerMaxPoll_Type()
)
xntpSAPeerMaxPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpSAPeerMaxPoll.setStatus("current")
_XntpSAPeerRowStatus_Type = RowStatus
_XntpSAPeerRowStatus_Object = MibTableColumn
xntpSAPeerRowStatus = _XntpSAPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 5),
    _XntpSAPeerRowStatus_Type()
)
xntpSAPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xntpSAPeerRowStatus.setStatus("current")
_XntpAssocTable_Object = MibTable
xntpAssocTable = _XntpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5)
)
if mibBuilder.loadTexts:
    xntpAssocTable.setStatus("current")
_XntpAssocEntry_Object = MibTableRow
xntpAssocEntry = _XntpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1)
)
xntpAssocEntry.setIndexNames(
    (0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerAddr"),
)
if mibBuilder.loadTexts:
    xntpAssocEntry.setStatus("current")
_XntpAssocPeerAddr_Type = XntpIpAddress
_XntpAssocPeerAddr_Object = MibTableColumn
xntpAssocPeerAddr = _XntpAssocPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 1),
    _XntpAssocPeerAddr_Type()
)
xntpAssocPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xntpAssocPeerAddr.setStatus("current")
_XntpAssocPeerPort_Type = XntpPort
_XntpAssocPeerPort_Object = MibTableColumn
xntpAssocPeerPort = _XntpAssocPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 2),
    _XntpAssocPeerPort_Type()
)
xntpAssocPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerPort.setStatus("current")
_XntpAssocPeerPoll_Type = Integer32
_XntpAssocPeerPoll_Object = MibTableColumn
xntpAssocPeerPoll = _XntpAssocPeerPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 3),
    _XntpAssocPeerPoll_Type()
)
xntpAssocPeerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerPoll.setStatus("current")
_XntpAssocHostAddr_Type = XntpIpAddress
_XntpAssocHostAddr_Object = MibTableColumn
xntpAssocHostAddr = _XntpAssocHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 4),
    _XntpAssocHostAddr_Type()
)
xntpAssocHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocHostAddr.setStatus("current")
_XntpAssocHostPort_Type = XntpPort
_XntpAssocHostPort_Object = MibTableColumn
xntpAssocHostPort = _XntpAssocHostPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 5),
    _XntpAssocHostPort_Type()
)
xntpAssocHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocHostPort.setStatus("current")
_XntpAssocHostPoll_Type = Integer32
_XntpAssocHostPoll_Object = MibTableColumn
xntpAssocHostPoll = _XntpAssocHostPoll_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 6),
    _XntpAssocHostPoll_Type()
)
xntpAssocHostPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocHostPoll.setStatus("current")
_XntpAssocHostMode_Type = XntpAssociationMode
_XntpAssocHostMode_Object = MibTableColumn
xntpAssocHostMode = _XntpAssocHostMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 7),
    _XntpAssocHostMode_Type()
)
xntpAssocHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocHostMode.setStatus("current")
_XntpAssocPeerMode_Type = XntpAssociationMode
_XntpAssocPeerMode_Object = MibTableColumn
xntpAssocPeerMode = _XntpAssocPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 8),
    _XntpAssocPeerMode_Type()
)
xntpAssocPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerMode.setStatus("current")
_XntpAssocPeerStratum_Type = Integer32
_XntpAssocPeerStratum_Object = MibTableColumn
xntpAssocPeerStratum = _XntpAssocPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 9),
    _XntpAssocPeerStratum_Type()
)
xntpAssocPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerStratum.setStatus("current")
_XntpAssocPeerPrecision_Type = Integer32
_XntpAssocPeerPrecision_Object = MibTableColumn
xntpAssocPeerPrecision = _XntpAssocPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 10),
    _XntpAssocPeerPrecision_Type()
)
xntpAssocPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerPrecision.setStatus("current")
_XntpAssocPeerLeap_Type = XntpLeapIndication
_XntpAssocPeerLeap_Object = MibTableColumn
xntpAssocPeerLeap = _XntpAssocPeerLeap_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 11),
    _XntpAssocPeerLeap_Type()
)
xntpAssocPeerLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerLeap.setStatus("current")
_XntpAssocPeerCondition_Type = XntpAssociationCondition
_XntpAssocPeerCondition_Object = MibTableColumn
xntpAssocPeerCondition = _XntpAssocPeerCondition_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 12),
    _XntpAssocPeerCondition_Type()
)
xntpAssocPeerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerCondition.setStatus("current")


class _XntpAssocPeerConfig_Type(Integer32):
    """Custom type xntpAssocPeerConfig based on Integer32"""
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


_XntpAssocPeerConfig_Type.__name__ = "Integer32"
_XntpAssocPeerConfig_Object = MibTableColumn
xntpAssocPeerConfig = _XntpAssocPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 13),
    _XntpAssocPeerConfig_Type()
)
xntpAssocPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerConfig.setStatus("current")
_XntpAssocPeerRootDelay_Type = XntpSeconds
_XntpAssocPeerRootDelay_Object = MibTableColumn
xntpAssocPeerRootDelay = _XntpAssocPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 14),
    _XntpAssocPeerRootDelay_Type()
)
xntpAssocPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerRootDelay.setStatus("current")
_XntpAssocPeerRootDispersion_Type = XntpSeconds
_XntpAssocPeerRootDispersion_Object = MibTableColumn
xntpAssocPeerRootDispersion = _XntpAssocPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 15),
    _XntpAssocPeerRootDispersion_Type()
)
xntpAssocPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerRootDispersion.setStatus("current")
_XntpAssocPeerOffset_Type = XntpSeconds
_XntpAssocPeerOffset_Object = MibTableColumn
xntpAssocPeerOffset = _XntpAssocPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 16),
    _XntpAssocPeerOffset_Type()
)
xntpAssocPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerOffset.setStatus("current")
_XntpAssocPeerDelay_Type = XntpSeconds
_XntpAssocPeerDelay_Object = MibTableColumn
xntpAssocPeerDelay = _XntpAssocPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 17),
    _XntpAssocPeerDelay_Type()
)
xntpAssocPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerDelay.setStatus("current")
_XntpAssocPeerDispersion_Type = XntpSeconds
_XntpAssocPeerDispersion_Object = MibTableColumn
xntpAssocPeerDispersion = _XntpAssocPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 18),
    _XntpAssocPeerDispersion_Type()
)
xntpAssocPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerDispersion.setStatus("current")
_XntpAssocPeerReachability_Type = XntpReachability
_XntpAssocPeerReachability_Object = MibTableColumn
xntpAssocPeerReachability = _XntpAssocPeerReachability_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 19),
    _XntpAssocPeerReachability_Type()
)
xntpAssocPeerReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerReachability.setStatus("current")
_XntpAssocPeerRefrTimestamp_Type = XntpDateAndTime
_XntpAssocPeerRefrTimestamp_Object = MibTableColumn
xntpAssocPeerRefrTimestamp = _XntpAssocPeerRefrTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 20),
    _XntpAssocPeerRefrTimestamp_Type()
)
xntpAssocPeerRefrTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerRefrTimestamp.setStatus("current")
_XntpAssocPeerXmitTimestamp_Type = XntpDateAndTime
_XntpAssocPeerXmitTimestamp_Object = MibTableColumn
xntpAssocPeerXmitTimestamp = _XntpAssocPeerXmitTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 21),
    _XntpAssocPeerXmitTimestamp_Type()
)
xntpAssocPeerXmitTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerXmitTimestamp.setStatus("current")
_XntpAssocPeerOrigTimestamp_Type = XntpDateAndTime
_XntpAssocPeerOrigTimestamp_Object = MibTableColumn
xntpAssocPeerOrigTimestamp = _XntpAssocPeerOrigTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 22),
    _XntpAssocPeerOrigTimestamp_Type()
)
xntpAssocPeerOrigTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerOrigTimestamp.setStatus("current")
_XntpAssocPeerRecvTimestamp_Type = XntpDateAndTime
_XntpAssocPeerRecvTimestamp_Object = MibTableColumn
xntpAssocPeerRecvTimestamp = _XntpAssocPeerRecvTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 23),
    _XntpAssocPeerRecvTimestamp_Type()
)
xntpAssocPeerRecvTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xntpAssocPeerRecvTimestamp.setStatus("current")
_XntpConformance_ObjectIdentity = ObjectIdentity
xntpConformance = _XntpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2)
)
_XntpCompliances_ObjectIdentity = ObjectIdentity
xntpCompliances = _XntpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 1)
)
_XntpGroups_ObjectIdentity = ObjectIdentity
xntpGroups = _XntpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2)
)

# Managed Objects groups

xntpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 1)
)
xntpSystemGroup.setObjects(
      *(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAdminStatus"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSrcAddressStatus"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpStratum"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpMode"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPrecision"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpClockSource"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPollInterval"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpLeapIndicator"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpRootDelay"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpRootDispersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpReferenceTimestamp"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpLocalTime"))
)
if mibBuilder.loadTexts:
    xntpSystemGroup.setStatus("current")

xntpCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 2)
)
xntpCountersGroup.setObjects(
      *(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPacketsIn"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadVersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadStratum"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadLength"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadMode"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadHeader"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadData"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPacketsOut"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPhaseAdjustments"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpStepAdjustments"))
)
if mibBuilder.loadTexts:
    xntpCountersGroup.setStatus("current")

xntpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 3)
)
xntpServerGroup.setObjects(
      *(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerVersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerMinPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerMaxPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerRowStatus"))
)
if mibBuilder.loadTexts:
    xntpServerGroup.setStatus("current")

xntpSAPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 4)
)
xntpSAPeerGroup.setObjects(
      *(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerVersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerMinPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerMaxPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerRowStatus"))
)
if mibBuilder.loadTexts:
    xntpSAPeerGroup.setStatus("current")

xntpAssocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 5)
)
xntpAssocGroup.setObjects(
      *(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPort"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostAddr"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostPort"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostPoll"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostMode"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerMode"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerStratum"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPrecision"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerLeap"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerCondition"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerConfig"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRootDelay"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRootDispersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerOffset"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerDelay"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerDispersion"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerReachability"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRefrTimestamp"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerXmitTimestamp"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerOrigTimestamp"),
        ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRecvTimestamp"))
)
if mibBuilder.loadTexts:
    xntpAssocGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xntpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xntpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-NETWORK-TIME-PROTOCOL-MIB",
    **{"XntpIpAddress": XntpIpAddress,
       "XntpPort": XntpPort,
       "XntpDateAndTime": XntpDateAndTime,
       "XntpSeconds": XntpSeconds,
       "XntpAssociationMode": XntpAssociationMode,
       "XntpLeapIndication": XntpLeapIndication,
       "XntpCounter": XntpCounter,
       "XntpAssociationCondition": XntpAssociationCondition,
       "XntpReachability": XntpReachability,
       "xediaNetworkTimeProtocolMIB": xediaNetworkTimeProtocolMIB,
       "xntpObjects": xntpObjects,
       "xntpSystem": xntpSystem,
       "xntpAdminStatus": xntpAdminStatus,
       "xntpSrcAddressStatus": xntpSrcAddressStatus,
       "xntpStratum": xntpStratum,
       "xntpMode": xntpMode,
       "xntpPrecision": xntpPrecision,
       "xntpClockSource": xntpClockSource,
       "xntpPollInterval": xntpPollInterval,
       "xntpLeapIndicator": xntpLeapIndicator,
       "xntpRootDelay": xntpRootDelay,
       "xntpRootDispersion": xntpRootDispersion,
       "xntpReferenceTimestamp": xntpReferenceTimestamp,
       "xntpLocalTime": xntpLocalTime,
       "xntpCounters": xntpCounters,
       "xntpPacketsIn": xntpPacketsIn,
       "xntpBadVersion": xntpBadVersion,
       "xntpBadStratum": xntpBadStratum,
       "xntpBadLength": xntpBadLength,
       "xntpBadMode": xntpBadMode,
       "xntpBadHeader": xntpBadHeader,
       "xntpBadData": xntpBadData,
       "xntpPacketsOut": xntpPacketsOut,
       "xntpPhaseAdjustments": xntpPhaseAdjustments,
       "xntpStepAdjustments": xntpStepAdjustments,
       "xntpServerTable": xntpServerTable,
       "xntpServerEntry": xntpServerEntry,
       "xntpServer": xntpServer,
       "xntpServerVersion": xntpServerVersion,
       "xntpServerMinPoll": xntpServerMinPoll,
       "xntpServerMaxPoll": xntpServerMaxPoll,
       "xntpServerRowStatus": xntpServerRowStatus,
       "xntpSAPeerTable": xntpSAPeerTable,
       "xntpSAPeerEntry": xntpSAPeerEntry,
       "xntpSAPeer": xntpSAPeer,
       "xntpSAPeerVersion": xntpSAPeerVersion,
       "xntpSAPeerMinPoll": xntpSAPeerMinPoll,
       "xntpSAPeerMaxPoll": xntpSAPeerMaxPoll,
       "xntpSAPeerRowStatus": xntpSAPeerRowStatus,
       "xntpAssocTable": xntpAssocTable,
       "xntpAssocEntry": xntpAssocEntry,
       "xntpAssocPeerAddr": xntpAssocPeerAddr,
       "xntpAssocPeerPort": xntpAssocPeerPort,
       "xntpAssocPeerPoll": xntpAssocPeerPoll,
       "xntpAssocHostAddr": xntpAssocHostAddr,
       "xntpAssocHostPort": xntpAssocHostPort,
       "xntpAssocHostPoll": xntpAssocHostPoll,
       "xntpAssocHostMode": xntpAssocHostMode,
       "xntpAssocPeerMode": xntpAssocPeerMode,
       "xntpAssocPeerStratum": xntpAssocPeerStratum,
       "xntpAssocPeerPrecision": xntpAssocPeerPrecision,
       "xntpAssocPeerLeap": xntpAssocPeerLeap,
       "xntpAssocPeerCondition": xntpAssocPeerCondition,
       "xntpAssocPeerConfig": xntpAssocPeerConfig,
       "xntpAssocPeerRootDelay": xntpAssocPeerRootDelay,
       "xntpAssocPeerRootDispersion": xntpAssocPeerRootDispersion,
       "xntpAssocPeerOffset": xntpAssocPeerOffset,
       "xntpAssocPeerDelay": xntpAssocPeerDelay,
       "xntpAssocPeerDispersion": xntpAssocPeerDispersion,
       "xntpAssocPeerReachability": xntpAssocPeerReachability,
       "xntpAssocPeerRefrTimestamp": xntpAssocPeerRefrTimestamp,
       "xntpAssocPeerXmitTimestamp": xntpAssocPeerXmitTimestamp,
       "xntpAssocPeerOrigTimestamp": xntpAssocPeerOrigTimestamp,
       "xntpAssocPeerRecvTimestamp": xntpAssocPeerRecvTimestamp,
       "xntpConformance": xntpConformance,
       "xntpCompliances": xntpCompliances,
       "xntpCompliance": xntpCompliance,
       "xntpGroups": xntpGroups,
       "xntpSystemGroup": xntpSystemGroup,
       "xntpCountersGroup": xntpCountersGroup,
       "xntpServerGroup": xntpServerGroup,
       "xntpSAPeerGroup": xntpSAPeerGroup,
       "xntpAssocGroup": xntpAssocGroup}
)
