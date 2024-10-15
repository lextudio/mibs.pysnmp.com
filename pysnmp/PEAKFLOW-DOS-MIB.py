# SNMP MIB module (PEAKFLOW-DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEAKFLOW-DOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:19 2024
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

(arbornetworksProducts,) = mibBuilder.importSymbols(
    "ARBOR-SMI",
    "arbornetworksProducts")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

peakflowDosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1)
)
peakflowDosMIB.setRevisions(
        ("2013-08-19 00:00",
         "2010-05-20 00:00",
         "2009-03-30 00:00",
         "2008-11-13 00:00",
         "2008-05-08 00:00",
         "2008-04-24 00:00",
         "2008-01-08 00:00",
         "2007-12-14 00:00",
         "2005-11-23 00:00",
         "2005-09-12 00:00",
         "2005-08-26 00:00",
         "2005-05-09 00:00",
         "2005-02-11 00:00",
         "2004-11-10 00:00",
         "2004-10-26 00:00",
         "2001-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PeakflowDosCMI_ObjectIdentity = ObjectIdentity
peakflowDosCMI = _PeakflowDosCMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1)
)


class _PdosUrl_Type(DisplayString):
    """Custom type pdosUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PdosUrl_Type.__name__ = "DisplayString"
_PdosUrl_Object = MibScalar
pdosUrl = _PdosUrl_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 1),
    _PdosUrl_Type()
)
pdosUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosUrl.setStatus("current")
_PdosAnomalyId_Type = Integer32
_PdosAnomalyId_Object = MibScalar
pdosAnomalyId = _PdosAnomalyId_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 2),
    _PdosAnomalyId_Type()
)
pdosAnomalyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyId.setStatus("current")


class _PdosAnomalyDirection_Type(DisplayString):
    """Custom type pdosAnomalyDirection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PdosAnomalyDirection_Type.__name__ = "DisplayString"
_PdosAnomalyDirection_Object = MibScalar
pdosAnomalyDirection = _PdosAnomalyDirection_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 3),
    _PdosAnomalyDirection_Type()
)
pdosAnomalyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyDirection.setStatus("current")


class _PdosAnomalyResource_Type(DisplayString):
    """Custom type pdosAnomalyResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PdosAnomalyResource_Type.__name__ = "DisplayString"
_PdosAnomalyResource_Object = MibScalar
pdosAnomalyResource = _PdosAnomalyResource_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 4),
    _PdosAnomalyResource_Type()
)
pdosAnomalyResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyResource.setStatus("current")


class _PdosHeartbeatSource_Type(DisplayString):
    """Custom type pdosHeartbeatSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PdosHeartbeatSource_Type.__name__ = "DisplayString"
_PdosHeartbeatSource_Object = MibScalar
pdosHeartbeatSource = _PdosHeartbeatSource_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 5),
    _PdosHeartbeatSource_Type()
)
pdosHeartbeatSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosHeartbeatSource.setStatus("obsolete")


class _InternalErrorLocation_Type(DisplayString):
    """Custom type internalErrorLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_InternalErrorLocation_Type.__name__ = "DisplayString"
_InternalErrorLocation_Object = MibScalar
internalErrorLocation = _InternalErrorLocation_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 6),
    _InternalErrorLocation_Type()
)
internalErrorLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    internalErrorLocation.setStatus("obsolete")


class _InternalErrorReason_Type(DisplayString):
    """Custom type internalErrorReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_InternalErrorReason_Type.__name__ = "DisplayString"
_InternalErrorReason_Object = MibScalar
internalErrorReason = _InternalErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 7),
    _InternalErrorReason_Type()
)
internalErrorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    internalErrorReason.setStatus("obsolete")


class _PdosAnomalyProto_Type(DisplayString):
    """Custom type pdosAnomalyProto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PdosAnomalyProto_Type.__name__ = "DisplayString"
_PdosAnomalyProto_Object = MibScalar
pdosAnomalyProto = _PdosAnomalyProto_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 8),
    _PdosAnomalyProto_Type()
)
pdosAnomalyProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyProto.setStatus("current")
_PdosAnomalyLinkPercent_Type = Unsigned32
_PdosAnomalyLinkPercent_Object = MibScalar
pdosAnomalyLinkPercent = _PdosAnomalyLinkPercent_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 9),
    _PdosAnomalyLinkPercent_Type()
)
pdosAnomalyLinkPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyLinkPercent.setStatus("current")
_PdosAnomalyAlertCnt_Type = Integer32
_PdosAnomalyAlertCnt_Object = MibScalar
pdosAnomalyAlertCnt = _PdosAnomalyAlertCnt_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 10),
    _PdosAnomalyAlertCnt_Type()
)
pdosAnomalyAlertCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyAlertCnt.setStatus("obsolete")


class _PdosAnomalyStart_Type(DisplayString):
    """Custom type pdosAnomalyStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PdosAnomalyStart_Type.__name__ = "DisplayString"
_PdosAnomalyStart_Object = MibScalar
pdosAnomalyStart = _PdosAnomalyStart_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 11),
    _PdosAnomalyStart_Type()
)
pdosAnomalyStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyStart.setStatus("current")
_PdosAnomalyDuration_Type = TimeTicks
_PdosAnomalyDuration_Object = MibScalar
pdosAnomalyDuration = _PdosAnomalyDuration_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 12),
    _PdosAnomalyDuration_Type()
)
pdosAnomalyDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyDuration.setStatus("current")


class _PdosAnomalyTcpFlags_Type(DisplayString):
    """Custom type pdosAnomalyTcpFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PdosAnomalyTcpFlags_Type.__name__ = "DisplayString"
_PdosAnomalyTcpFlags_Object = MibScalar
pdosAnomalyTcpFlags = _PdosAnomalyTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 13),
    _PdosAnomalyTcpFlags_Type()
)
pdosAnomalyTcpFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyTcpFlags.setStatus("current")
_PdosAnomalyRouter_Type = IpAddress
_PdosAnomalyRouter_Object = MibScalar
pdosAnomalyRouter = _PdosAnomalyRouter_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 14),
    _PdosAnomalyRouter_Type()
)
pdosAnomalyRouter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyRouter.setStatus("current")


class _PdosAnomalyRouterInterfaces_Type(DisplayString):
    """Custom type pdosAnomalyRouterInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PdosAnomalyRouterInterfaces_Type.__name__ = "DisplayString"
_PdosAnomalyRouterInterfaces_Object = MibScalar
pdosAnomalyRouterInterfaces = _PdosAnomalyRouterInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 15),
    _PdosAnomalyRouterInterfaces_Type()
)
pdosAnomalyRouterInterfaces.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyRouterInterfaces.setStatus("current")


class _PdosAnomalyClassification_Type(DisplayString):
    """Custom type pdosAnomalyClassification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PdosAnomalyClassification_Type.__name__ = "DisplayString"
_PdosAnomalyClassification_Object = MibScalar
pdosAnomalyClassification = _PdosAnomalyClassification_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 16),
    _PdosAnomalyClassification_Type()
)
pdosAnomalyClassification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pdosAnomalyClassification.setStatus("current")
_PeakflowDosMgr_ObjectIdentity = ObjectIdentity
peakflowDosMgr = _PeakflowDosMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 2)
)
_PeakflowDosTraps_ObjectIdentity = ObjectIdentity
peakflowDosTraps = _PeakflowDosTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3)
)
_PeakflowDosTrapsEnumerate_ObjectIdentity = ObjectIdentity
peakflowDosTrapsEnumerate = _PeakflowDosTrapsEnumerate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

bandwidthAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 1)
)
bandwidthAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    bandwidthAnomaly.setStatus(
        "current"
    )

tcpflagsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 2)
)
tcpflagsAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
)
if mibBuilder.loadTexts:
    tcpflagsAnomaly.setStatus(
        "obsolete"
    )

protocolAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 3)
)
protocolAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
)
if mibBuilder.loadTexts:
    protocolAnomaly.setStatus(
        "current"
    )

heartbeatLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 4)
)
heartbeatLoss.setObjects(
    ("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource")
)
if mibBuilder.loadTexts:
    heartbeatLoss.setStatus(
        "obsolete"
    )

internalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 5)
)
internalError.setObjects(
      *(("PEAKFLOW-DOS-MIB", "internalErrorLocation"),
        ("PEAKFLOW-DOS-MIB", "internalErrorReason"))
)
if mibBuilder.loadTexts:
    internalError.setStatus(
        "obsolete"
    )

anomalyDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 6)
)
anomalyDone.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    anomalyDone.setStatus(
        "current"
    )

netflowMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 7)
)
netflowMissing.setObjects(
    ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter")
)
if mibBuilder.loadTexts:
    netflowMissing.setStatus(
        "obsolete"
    )

netflowMissingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 8)
)
netflowMissingDone.setObjects(
    ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter")
)
if mibBuilder.loadTexts:
    netflowMissingDone.setStatus(
        "obsolete"
    )

icmpMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 9)
)
icmpMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
)
if mibBuilder.loadTexts:
    icmpMisuseAnomaly.setStatus(
        "current"
    )

tcpNullMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 10)
)
tcpNullMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
)
if mibBuilder.loadTexts:
    tcpNullMisuseAnomaly.setStatus(
        "current"
    )

tcpSynMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 11)
)
tcpSynMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
)
if mibBuilder.loadTexts:
    tcpSynMisuseAnomaly.setStatus(
        "current"
    )

ipNullMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 12)
)
ipNullMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    ipNullMisuseAnomaly.setStatus(
        "current"
    )

ipFragMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 13)
)
ipFragMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
)
if mibBuilder.loadTexts:
    ipFragMisuseAnomaly.setStatus(
        "current"
    )

ipPrivateMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 14)
)
ipPrivateMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    ipPrivateMisuseAnomaly.setStatus(
        "current"
    )

heartbeatLossDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 15)
)
heartbeatLossDone.setObjects(
    ("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource")
)
if mibBuilder.loadTexts:
    heartbeatLossDone.setStatus(
        "obsolete"
    )

tcpRstMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 16)
)
tcpRstMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
)
if mibBuilder.loadTexts:
    tcpRstMisuseAnomaly.setStatus(
        "current"
    )

totalTrafficMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 17)
)
totalTrafficMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    totalTrafficMisuseAnomaly.setStatus(
        "current"
    )

fingerprintAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 18)
)
fingerprintAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"))
)
if mibBuilder.loadTexts:
    fingerprintAnomaly.setStatus(
        "current"
    )

dnsMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 19)
)
dnsMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
)
if mibBuilder.loadTexts:
    dnsMisuseAnomaly.setStatus(
        "current"
    )

udpMisuseAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 20)
)
udpMisuseAnomaly.setObjects(
      *(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
)
if mibBuilder.loadTexts:
    udpMisuseAnomaly.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKFLOW-DOS-MIB",
    **{"peakflowDosMIB": peakflowDosMIB,
       "peakflowDosCMI": peakflowDosCMI,
       "pdosUrl": pdosUrl,
       "pdosAnomalyId": pdosAnomalyId,
       "pdosAnomalyDirection": pdosAnomalyDirection,
       "pdosAnomalyResource": pdosAnomalyResource,
       "pdosHeartbeatSource": pdosHeartbeatSource,
       "internalErrorLocation": internalErrorLocation,
       "internalErrorReason": internalErrorReason,
       "pdosAnomalyProto": pdosAnomalyProto,
       "pdosAnomalyLinkPercent": pdosAnomalyLinkPercent,
       "pdosAnomalyAlertCnt": pdosAnomalyAlertCnt,
       "pdosAnomalyStart": pdosAnomalyStart,
       "pdosAnomalyDuration": pdosAnomalyDuration,
       "pdosAnomalyTcpFlags": pdosAnomalyTcpFlags,
       "pdosAnomalyRouter": pdosAnomalyRouter,
       "pdosAnomalyRouterInterfaces": pdosAnomalyRouterInterfaces,
       "pdosAnomalyClassification": pdosAnomalyClassification,
       "peakflowDosMgr": peakflowDosMgr,
       "peakflowDosTraps": peakflowDosTraps,
       "peakflowDosTrapsEnumerate": peakflowDosTrapsEnumerate,
       "bandwidthAnomaly": bandwidthAnomaly,
       "tcpflagsAnomaly": tcpflagsAnomaly,
       "protocolAnomaly": protocolAnomaly,
       "heartbeatLoss": heartbeatLoss,
       "internalError": internalError,
       "anomalyDone": anomalyDone,
       "netflowMissing": netflowMissing,
       "netflowMissingDone": netflowMissingDone,
       "icmpMisuseAnomaly": icmpMisuseAnomaly,
       "tcpNullMisuseAnomaly": tcpNullMisuseAnomaly,
       "tcpSynMisuseAnomaly": tcpSynMisuseAnomaly,
       "ipNullMisuseAnomaly": ipNullMisuseAnomaly,
       "ipFragMisuseAnomaly": ipFragMisuseAnomaly,
       "ipPrivateMisuseAnomaly": ipPrivateMisuseAnomaly,
       "heartbeatLossDone": heartbeatLossDone,
       "tcpRstMisuseAnomaly": tcpRstMisuseAnomaly,
       "totalTrafficMisuseAnomaly": totalTrafficMisuseAnomaly,
       "fingerprintAnomaly": fingerprintAnomaly,
       "dnsMisuseAnomaly": dnsMisuseAnomaly,
       "udpMisuseAnomaly": udpMisuseAnomaly}
)
