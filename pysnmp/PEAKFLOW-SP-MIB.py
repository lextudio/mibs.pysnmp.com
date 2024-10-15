# SNMP MIB module (PEAKFLOW-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEAKFLOW-SP-MIB
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(pdosAnomalyClassification,
 pdosAnomalyDirection,
 pdosAnomalyDuration,
 pdosAnomalyStart,
 pdosUrl) = mibBuilder.importSymbols(
    "PEAKFLOW-DOS-MIB",
    "pdosAnomalyClassification",
    "pdosAnomalyDirection",
    "pdosAnomalyDuration",
    "pdosAnomalyStart",
    "pdosUrl")

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

peakflowSPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4)
)
peakflowSPMIB.setRevisions(
        ("2013-08-19 00:00",
         "2013-01-15 00:00",
         "2012-07-30 00:00",
         "2012-05-13 00:00",
         "2011-06-03 00:00",
         "2010-06-08 00:00",
         "2010-05-20 00:00",
         "2009-09-24 00:00",
         "2009-04-01 00:00",
         "2009-03-30 00:00",
         "2009-02-02 00:00",
         "2008-12-16 00:00",
         "2008-11-13 00:00",
         "2008-05-19 00:00",
         "2008-02-19 00:00",
         "2008-02-11 00:00",
         "2007-08-07 00:00",
         "2006-04-26 00:00",
         "2006-03-23 00:00",
         "2005-11-14 00:00",
         "2005-10-19 00:00",
         "2005-09-12 00:00",
         "2005-08-23 00:00",
         "2005-05-17 01:00",
         "2005-05-17 00:00",
         "2005-02-11 00:00",
         "2004-12-10 00:00",
         "2004-03-30 00:00",
         "2002-08-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PeakflowSPCMI_ObjectIdentity = ObjectIdentity
peakflowSPCMI = _PeakflowSPCMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1)
)


class _SpCollector_Type(DisplayString):
    """Custom type spCollector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpCollector_Type.__name__ = "DisplayString"
_SpCollector_Object = MibScalar
spCollector = _SpCollector_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 1),
    _SpCollector_Type()
)
spCollector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spCollector.setStatus("current")


class _SpRouter_Type(DisplayString):
    """Custom type spRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpRouter_Type.__name__ = "DisplayString"
_SpRouter_Object = MibScalar
spRouter = _SpRouter_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 2),
    _SpRouter_Type()
)
spRouter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spRouter.setStatus("current")


class _SpInterface_Type(DisplayString):
    """Custom type spInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpInterface_Type.__name__ = "DisplayString"
_SpInterface_Object = MibScalar
spInterface = _SpInterface_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 3),
    _SpInterface_Type()
)
spInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInterface.setStatus("current")
_SpInterfaceIndex_Type = Unsigned32
_SpInterfaceIndex_Object = MibScalar
spInterfaceIndex = _SpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 4),
    _SpInterfaceIndex_Type()
)
spInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInterfaceIndex.setStatus("current")
_SpDuration_Type = TimeTicks
_SpDuration_Object = MibScalar
spDuration = _SpDuration_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 5),
    _SpDuration_Type()
)
spDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDuration.setStatus("current")


class _SpBGPEvent_Type(DisplayString):
    """Custom type spBGPEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpBGPEvent_Type.__name__ = "DisplayString"
_SpBGPEvent_Object = MibScalar
spBGPEvent = _SpBGPEvent_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 6),
    _SpBGPEvent_Type()
)
spBGPEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPEvent.setStatus("current")
_SpBGPInstability_Type = Unsigned32
_SpBGPInstability_Object = MibScalar
spBGPInstability = _SpBGPInstability_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 7),
    _SpBGPInstability_Type()
)
spBGPInstability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPInstability.setStatus("current")


class _SpBGPTrapName_Type(DisplayString):
    """Custom type spBGPTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpBGPTrapName_Type.__name__ = "DisplayString"
_SpBGPTrapName_Object = MibScalar
spBGPTrapName = _SpBGPTrapName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 8),
    _SpBGPTrapName_Type()
)
spBGPTrapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPTrapName.setStatus("current")


class _SpBGPTrapEvent_Type(DisplayString):
    """Custom type spBGPTrapEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpBGPTrapEvent_Type.__name__ = "DisplayString"
_SpBGPTrapEvent_Object = MibScalar
spBGPTrapEvent = _SpBGPTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 9),
    _SpBGPTrapEvent_Type()
)
spBGPTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPTrapEvent.setStatus("current")


class _SpBGPTrapPrefix_Type(DisplayString):
    """Custom type spBGPTrapPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpBGPTrapPrefix_Type.__name__ = "DisplayString"
_SpBGPTrapPrefix_Object = MibScalar
spBGPTrapPrefix = _SpBGPTrapPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 10),
    _SpBGPTrapPrefix_Type()
)
spBGPTrapPrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPTrapPrefix.setStatus("current")
_SpBGPTrapOldAttributes_Type = DisplayString
_SpBGPTrapOldAttributes_Object = MibScalar
spBGPTrapOldAttributes = _SpBGPTrapOldAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 11),
    _SpBGPTrapOldAttributes_Type()
)
spBGPTrapOldAttributes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPTrapOldAttributes.setStatus("current")
_SpBGPTrapNewAttributes_Type = DisplayString
_SpBGPTrapNewAttributes_Object = MibScalar
spBGPTrapNewAttributes = _SpBGPTrapNewAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 12),
    _SpBGPTrapNewAttributes_Type()
)
spBGPTrapNewAttributes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBGPTrapNewAttributes.setStatus("current")
_SpInterfaceSpeed_Type = Unsigned32
_SpInterfaceSpeed_Object = MibScalar
spInterfaceSpeed = _SpInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 13),
    _SpInterfaceSpeed_Type()
)
spInterfaceSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInterfaceSpeed.setStatus("current")
_SpInterfaceUsage_Type = Unsigned32
_SpInterfaceUsage_Object = MibScalar
spInterfaceUsage = _SpInterfaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 14),
    _SpInterfaceUsage_Type()
)
spInterfaceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInterfaceUsage.setStatus("current")
_SpReportURL_Type = DisplayString
_SpReportURL_Object = MibScalar
spReportURL = _SpReportURL_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 15),
    _SpReportURL_Type()
)
spReportURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spReportURL.setStatus("current")


class _SpReportName_Type(DisplayString):
    """Custom type spReportName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpReportName_Type.__name__ = "DisplayString"
_SpReportName_Object = MibScalar
spReportName = _SpReportName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 16),
    _SpReportName_Type()
)
spReportName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spReportName.setStatus("current")


class _SpReportID_Type(DisplayString):
    """Custom type spReportID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpReportID_Type.__name__ = "DisplayString"
_SpReportID_Object = MibScalar
spReportID = _SpReportID_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 17),
    _SpReportID_Type()
)
spReportID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spReportID.setStatus("current")
_SpAlertID_Type = Unsigned32
_SpAlertID_Object = MibScalar
spAlertID = _SpAlertID_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 18),
    _SpAlertID_Type()
)
spAlertID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spAlertID.setStatus("current")


class _SpHijackRoute_Type(DisplayString):
    """Custom type spHijackRoute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpHijackRoute_Type.__name__ = "DisplayString"
_SpHijackRoute_Object = MibScalar
spHijackRoute = _SpHijackRoute_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 19),
    _SpHijackRoute_Type()
)
spHijackRoute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spHijackRoute.setStatus("current")


class _SpHijackAttr_Type(DisplayString):
    """Custom type spHijackAttr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SpHijackAttr_Type.__name__ = "DisplayString"
_SpHijackAttr_Object = MibScalar
spHijackAttr = _SpHijackAttr_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 20),
    _SpHijackAttr_Type()
)
spHijackAttr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spHijackAttr.setStatus("current")


class _SpHijackLocal_Type(DisplayString):
    """Custom type spHijackLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpHijackLocal_Type.__name__ = "DisplayString"
_SpHijackLocal_Object = MibScalar
spHijackLocal = _SpHijackLocal_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 21),
    _SpHijackLocal_Type()
)
spHijackLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spHijackLocal.setStatus("current")


class _SpUsername_Type(DisplayString):
    """Custom type spUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpUsername_Type.__name__ = "DisplayString"
_SpUsername_Object = MibScalar
spUsername = _SpUsername_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 22),
    _SpUsername_Type()
)
spUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spUsername.setStatus("current")


class _SpVersion_Type(DisplayString):
    """Custom type spVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpVersion_Type.__name__ = "DisplayString"
_SpVersion_Object = MibScalar
spVersion = _SpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 23),
    _SpVersion_Type()
)
spVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spVersion.setStatus("current")


class _SpUsageType_Type(DisplayString):
    """Custom type spUsageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpUsageType_Type.__name__ = "DisplayString"
_SpUsageType_Object = MibScalar
spUsageType = _SpUsageType_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 24),
    _SpUsageType_Type()
)
spUsageType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spUsageType.setStatus("current")


class _SpManagedObject_Type(DisplayString):
    """Custom type spManagedObject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpManagedObject_Type.__name__ = "DisplayString"
_SpManagedObject_Object = MibScalar
spManagedObject = _SpManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 25),
    _SpManagedObject_Type()
)
spManagedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spManagedObject.setStatus("current")


class _SpManagedObjectFamily_Type(DisplayString):
    """Custom type spManagedObjectFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SpManagedObjectFamily_Type.__name__ = "DisplayString"
_SpManagedObjectFamily_Object = MibScalar
spManagedObjectFamily = _SpManagedObjectFamily_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 26),
    _SpManagedObjectFamily_Type()
)
spManagedObjectFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spManagedObjectFamily.setStatus("current")
_SpThreshold_Type = Unsigned32
_SpThreshold_Object = MibScalar
spThreshold = _SpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 27),
    _SpThreshold_Type()
)
spThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spThreshold.setStatus("current")
_SpUsage_Type = Unsigned32
_SpUsage_Object = MibScalar
spUsage = _SpUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 28),
    _SpUsage_Type()
)
spUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spUsage.setStatus("current")


class _SpUnit_Type(DisplayString):
    """Custom type spUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SpUnit_Type.__name__ = "DisplayString"
_SpUnit_Object = MibScalar
spUnit = _SpUnit_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 29),
    _SpUnit_Type()
)
spUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spUnit.setStatus("current")


class _SpHardwareFailureDescription_Type(DisplayString):
    """Custom type spHardwareFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpHardwareFailureDescription_Type.__name__ = "DisplayString"
_SpHardwareFailureDescription_Object = MibScalar
spHardwareFailureDescription = _SpHardwareFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 30),
    _SpHardwareFailureDescription_Type()
)
spHardwareFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spHardwareFailureDescription.setStatus("current")


class _SpFingerprintName_Type(DisplayString):
    """Custom type spFingerprintName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpFingerprintName_Type.__name__ = "DisplayString"
_SpFingerprintName_Object = MibScalar
spFingerprintName = _SpFingerprintName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 31),
    _SpFingerprintName_Type()
)
spFingerprintName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFingerprintName.setStatus("current")


class _SpFingerprintFeedback_Type(DisplayString):
    """Custom type spFingerprintFeedback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpFingerprintFeedback_Type.__name__ = "DisplayString"
_SpFingerprintFeedback_Object = MibScalar
spFingerprintFeedback = _SpFingerprintFeedback_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 32),
    _SpFingerprintFeedback_Type()
)
spFingerprintFeedback.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFingerprintFeedback.setStatus("current")


class _SpFingerprintSender_Type(DisplayString):
    """Custom type spFingerprintSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpFingerprintSender_Type.__name__ = "DisplayString"
_SpFingerprintSender_Object = MibScalar
spFingerprintSender = _SpFingerprintSender_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 33),
    _SpFingerprintSender_Type()
)
spFingerprintSender.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFingerprintSender.setStatus("current")


class _SpFingerprintMessage_Type(DisplayString):
    """Custom type spFingerprintMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpFingerprintMessage_Type.__name__ = "DisplayString"
_SpFingerprintMessage_Object = MibScalar
spFingerprintMessage = _SpFingerprintMessage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 34),
    _SpFingerprintMessage_Type()
)
spFingerprintMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFingerprintMessage.setStatus("current")
_SpMitigationID_Type = Unsigned32
_SpMitigationID_Object = MibScalar
spMitigationID = _SpMitigationID_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 35),
    _SpMitigationID_Type()
)
spMitigationID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spMitigationID.setStatus("current")


class _SpDNSName_Type(DisplayString):
    """Custom type spDNSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpDNSName_Type.__name__ = "DisplayString"
_SpDNSName_Object = MibScalar
spDNSName = _SpDNSName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 36),
    _SpDNSName_Type()
)
spDNSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDNSName.setStatus("current")
_SpDNSExpected_Type = Unsigned32
_SpDNSExpected_Object = MibScalar
spDNSExpected = _SpDNSExpected_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 37),
    _SpDNSExpected_Type()
)
spDNSExpected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDNSExpected.setStatus("current")
_SpDNSObserved_Type = Unsigned32
_SpDNSObserved_Object = MibScalar
spDNSObserved = _SpDNSObserved_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 38),
    _SpDNSObserved_Type()
)
spDNSObserved.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDNSObserved.setStatus("current")
_SpDNSObservedMean_Type = Unsigned32
_SpDNSObservedMean_Object = MibScalar
spDNSObservedMean = _SpDNSObservedMean_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 39),
    _SpDNSObservedMean_Type()
)
spDNSObservedMean.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDNSObservedMean.setStatus("current")
_SpDNSObservedMax_Type = Unsigned32
_SpDNSObservedMax_Object = MibScalar
spDNSObservedMax = _SpDNSObservedMax_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 40),
    _SpDNSObservedMax_Type()
)
spDNSObservedMax.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDNSObservedMax.setStatus("current")


class _SpMitigationName_Type(DisplayString):
    """Custom type spMitigationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpMitigationName_Type.__name__ = "DisplayString"
_SpMitigationName_Object = MibScalar
spMitigationName = _SpMitigationName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 41),
    _SpMitigationName_Type()
)
spMitigationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spMitigationName.setStatus("current")


class _SpScriptCommand_Type(DisplayString):
    """Custom type spScriptCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpScriptCommand_Type.__name__ = "DisplayString"
_SpScriptCommand_Object = MibScalar
spScriptCommand = _SpScriptCommand_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 42),
    _SpScriptCommand_Type()
)
spScriptCommand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spScriptCommand.setStatus("current")


class _SpScriptHost_Type(DisplayString):
    """Custom type spScriptHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpScriptHost_Type.__name__ = "DisplayString"
_SpScriptHost_Object = MibScalar
spScriptHost = _SpScriptHost_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 43),
    _SpScriptHost_Type()
)
spScriptHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spScriptHost.setStatus("current")


class _SpScriptPort_Type(DisplayString):
    """Custom type spScriptPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_SpScriptPort_Type.__name__ = "DisplayString"
_SpScriptPort_Object = MibScalar
spScriptPort = _SpScriptPort_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 44),
    _SpScriptPort_Type()
)
spScriptPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spScriptPort.setStatus("current")


class _SpScriptStart_Type(DisplayString):
    """Custom type spScriptStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpScriptStart_Type.__name__ = "DisplayString"
_SpScriptStart_Object = MibScalar
spScriptStart = _SpScriptStart_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 45),
    _SpScriptStart_Type()
)
spScriptStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spScriptStart.setStatus("current")


class _SpTMSPrefix_Type(DisplayString):
    """Custom type spTMSPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpTMSPrefix_Type.__name__ = "DisplayString"
_SpTMSPrefix_Object = MibScalar
spTMSPrefix = _SpTMSPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 46),
    _SpTMSPrefix_Type()
)
spTMSPrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spTMSPrefix.setStatus("current")


class _SpTMSCommunity_Type(DisplayString):
    """Custom type spTMSCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpTMSCommunity_Type.__name__ = "DisplayString"
_SpTMSCommunity_Object = MibScalar
spTMSCommunity = _SpTMSCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 47),
    _SpTMSCommunity_Type()
)
spTMSCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spTMSCommunity.setStatus("current")


class _SpTMSTimeout_Type(DisplayString):
    """Custom type spTMSTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpTMSTimeout_Type.__name__ = "DisplayString"
_SpTMSTimeout_Object = MibScalar
spTMSTimeout = _SpTMSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 48),
    _SpTMSTimeout_Type()
)
spTMSTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spTMSTimeout.setStatus("current")


class _SpThirdPartyZone_Type(DisplayString):
    """Custom type spThirdPartyZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpThirdPartyZone_Type.__name__ = "DisplayString"
_SpThirdPartyZone_Object = MibScalar
spThirdPartyZone = _SpThirdPartyZone_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 49),
    _SpThirdPartyZone_Type()
)
spThirdPartyZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spThirdPartyZone.setStatus("current")


class _SpThirdPartyAddr_Type(DisplayString):
    """Custom type spThirdPartyAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpThirdPartyAddr_Type.__name__ = "DisplayString"
_SpThirdPartyAddr_Object = MibScalar
spThirdPartyAddr = _SpThirdPartyAddr_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 50),
    _SpThirdPartyAddr_Type()
)
spThirdPartyAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spThirdPartyAddr.setStatus("current")


class _SpMitigationStart_Type(DisplayString):
    """Custom type spMitigationStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpMitigationStart_Type.__name__ = "DisplayString"
_SpMitigationStart_Object = MibScalar
spMitigationStart = _SpMitigationStart_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 51),
    _SpMitigationStart_Type()
)
spMitigationStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spMitigationStart.setStatus("current")


class _SpBlackholeCommunity_Type(DisplayString):
    """Custom type spBlackholeCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpBlackholeCommunity_Type.__name__ = "DisplayString"
_SpBlackholeCommunity_Object = MibScalar
spBlackholeCommunity = _SpBlackholeCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 52),
    _SpBlackholeCommunity_Type()
)
spBlackholeCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBlackholeCommunity.setStatus("current")


class _SpBlackholeTimeout_Type(DisplayString):
    """Custom type spBlackholeTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpBlackholeTimeout_Type.__name__ = "DisplayString"
_SpBlackholeTimeout_Object = MibScalar
spBlackholeTimeout = _SpBlackholeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 53),
    _SpBlackholeTimeout_Type()
)
spBlackholeTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBlackholeTimeout.setStatus("current")


class _SpBlackholePrefix_Type(DisplayString):
    """Custom type spBlackholePrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpBlackholePrefix_Type.__name__ = "DisplayString"
_SpBlackholePrefix_Object = MibScalar
spBlackholePrefix = _SpBlackholePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 54),
    _SpBlackholePrefix_Type()
)
spBlackholePrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBlackholePrefix.setStatus("current")


class _SpBlackholeNexthop_Type(DisplayString):
    """Custom type spBlackholeNexthop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpBlackholeNexthop_Type.__name__ = "DisplayString"
_SpBlackholeNexthop_Object = MibScalar
spBlackholeNexthop = _SpBlackholeNexthop_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 55),
    _SpBlackholeNexthop_Type()
)
spBlackholeNexthop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spBlackholeNexthop.setStatus("current")


class _SpFlowspecCommunity_Type(DisplayString):
    """Custom type spFlowspecCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpFlowspecCommunity_Type.__name__ = "DisplayString"
_SpFlowspecCommunity_Object = MibScalar
spFlowspecCommunity = _SpFlowspecCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 56),
    _SpFlowspecCommunity_Type()
)
spFlowspecCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFlowspecCommunity.setStatus("current")


class _SpFlowspecTimeout_Type(DisplayString):
    """Custom type spFlowspecTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SpFlowspecTimeout_Type.__name__ = "DisplayString"
_SpFlowspecTimeout_Object = MibScalar
spFlowspecTimeout = _SpFlowspecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 57),
    _SpFlowspecTimeout_Type()
)
spFlowspecTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spFlowspecTimeout.setStatus("current")


class _SpCommFailureDestination_Type(DisplayString):
    """Custom type spCommFailureDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpCommFailureDestination_Type.__name__ = "DisplayString"
_SpCommFailureDestination_Object = MibScalar
spCommFailureDestination = _SpCommFailureDestination_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 58),
    _SpCommFailureDestination_Type()
)
spCommFailureDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spCommFailureDestination.setStatus("current")


class _SpCommFailureDescription_Type(DisplayString):
    """Custom type spCommFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpCommFailureDescription_Type.__name__ = "DisplayString"
_SpCommFailureDescription_Object = MibScalar
spCommFailureDescription = _SpCommFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 59),
    _SpCommFailureDescription_Type()
)
spCommFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spCommFailureDescription.setStatus("current")
_SpGreTunnelDestination_Type = IpAddress
_SpGreTunnelDestination_Object = MibScalar
spGreTunnelDestination = _SpGreTunnelDestination_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 60),
    _SpGreTunnelDestination_Type()
)
spGreTunnelDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spGreTunnelDestination.setStatus("current")


class _SpSystemErrorType_Type(DisplayString):
    """Custom type spSystemErrorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpSystemErrorType_Type.__name__ = "DisplayString"
_SpSystemErrorType_Object = MibScalar
spSystemErrorType = _SpSystemErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 61),
    _SpSystemErrorType_Type()
)
spSystemErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spSystemErrorType.setStatus("current")


class _SpSystemErrorDescription_Type(DisplayString):
    """Custom type spSystemErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpSystemErrorDescription_Type.__name__ = "DisplayString"
_SpSystemErrorDescription_Object = MibScalar
spSystemErrorDescription = _SpSystemErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 62),
    _SpSystemErrorDescription_Type()
)
spSystemErrorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spSystemErrorDescription.setStatus("current")


class _SpServiceName_Type(DisplayString):
    """Custom type spServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpServiceName_Type.__name__ = "DisplayString"
_SpServiceName_Object = MibScalar
spServiceName = _SpServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 63),
    _SpServiceName_Type()
)
spServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spServiceName.setStatus("current")


class _SpServiceElement_Type(DisplayString):
    """Custom type spServiceElement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpServiceElement_Type.__name__ = "DisplayString"
_SpServiceElement_Object = MibScalar
spServiceElement = _SpServiceElement_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 64),
    _SpServiceElement_Type()
)
spServiceElement.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spServiceElement.setStatus("current")


class _SpApplicationName_Type(DisplayString):
    """Custom type spApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpApplicationName_Type.__name__ = "DisplayString"
_SpApplicationName_Object = MibScalar
spApplicationName = _SpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 65),
    _SpApplicationName_Type()
)
spApplicationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spApplicationName.setStatus("current")


class _SpAlertDetectionSignatures_Type(DisplayString):
    """Custom type spAlertDetectionSignatures based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SpAlertDetectionSignatures_Type.__name__ = "DisplayString"
_SpAlertDetectionSignatures_Object = MibScalar
spAlertDetectionSignatures = _SpAlertDetectionSignatures_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 66),
    _SpAlertDetectionSignatures_Type()
)
spAlertDetectionSignatures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spAlertDetectionSignatures.setStatus("current")


class _SpManagedObjects_Type(DisplayString):
    """Custom type spManagedObjects based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_SpManagedObjects_Type.__name__ = "DisplayString"
_SpManagedObjects_Object = MibScalar
spManagedObjects = _SpManagedObjects_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 67),
    _SpManagedObjects_Type()
)
spManagedObjects.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spManagedObjects.setStatus("current")
_SpInetAddressType_Type = InetAddressType
_SpInetAddressType_Object = MibScalar
spInetAddressType = _SpInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 68),
    _SpInetAddressType_Type()
)
spInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInetAddressType.setStatus("current")
_SpInetAddress_Type = InetAddress
_SpInetAddress_Object = MibScalar
spInetAddress = _SpInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 69),
    _SpInetAddress_Type()
)
spInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spInetAddress.setStatus("current")
_SpImpactBps_Type = Unsigned32
_SpImpactBps_Object = MibScalar
spImpactBps = _SpImpactBps_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 70),
    _SpImpactBps_Type()
)
spImpactBps.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spImpactBps.setStatus("current")
_SpImpactPps_Type = Unsigned32
_SpImpactPps_Object = MibScalar
spImpactPps = _SpImpactPps_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 71),
    _SpImpactPps_Type()
)
spImpactPps.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spImpactPps.setStatus("current")


class _SpDetectedCountries_Type(DisplayString):
    """Custom type spDetectedCountries based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 152),
    )


_SpDetectedCountries_Type.__name__ = "DisplayString"
_SpDetectedCountries_Object = MibScalar
spDetectedCountries = _SpDetectedCountries_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 72),
    _SpDetectedCountries_Type()
)
spDetectedCountries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDetectedCountries.setStatus("current")
_SpRoutingFailoverInterfaces_Type = DisplayString
_SpRoutingFailoverInterfaces_Object = MibScalar
spRoutingFailoverInterfaces = _SpRoutingFailoverInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 73),
    _SpRoutingFailoverInterfaces_Type()
)
spRoutingFailoverInterfaces.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spRoutingFailoverInterfaces.setStatus("current")


class _SpPravail_Type(DisplayString):
    """Custom type spPravail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpPravail_Type.__name__ = "DisplayString"
_SpPravail_Object = MibScalar
spPravail = _SpPravail_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 74),
    _SpPravail_Type()
)
spPravail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spPravail.setStatus("current")


class _SpDetector_Type(DisplayString):
    """Custom type spDetector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpDetector_Type.__name__ = "DisplayString"
_SpDetector_Object = MibScalar
spDetector = _SpDetector_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 75),
    _SpDetector_Type()
)
spDetector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spDetector.setStatus("current")


class _SpTMSMultiPrefix_Type(DisplayString):
    """Custom type spTMSMultiPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpTMSMultiPrefix_Type.__name__ = "DisplayString"
_SpTMSMultiPrefix_Object = MibScalar
spTMSMultiPrefix = _SpTMSMultiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 76),
    _SpTMSMultiPrefix_Type()
)
spTMSMultiPrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spTMSMultiPrefix.setStatus("current")


class _SpLicenseErrType_Type(DisplayString):
    """Custom type spLicenseErrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SpLicenseErrType_Type.__name__ = "DisplayString"
_SpLicenseErrType_Object = MibScalar
spLicenseErrType = _SpLicenseErrType_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 77),
    _SpLicenseErrType_Type()
)
spLicenseErrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spLicenseErrType.setStatus("current")
_SpLicenseErrCount_Type = Unsigned32
_SpLicenseErrCount_Object = MibScalar
spLicenseErrCount = _SpLicenseErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 78),
    _SpLicenseErrCount_Type()
)
spLicenseErrCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spLicenseErrCount.setStatus("current")
_SpLicenseErrLimit_Type = Unsigned32
_SpLicenseErrLimit_Object = MibScalar
spLicenseErrLimit = _SpLicenseErrLimit_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 79),
    _SpLicenseErrLimit_Type()
)
spLicenseErrLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spLicenseErrLimit.setStatus("current")


class _SpLicenseErrDescription_Type(DisplayString):
    """Custom type spLicenseErrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpLicenseErrDescription_Type.__name__ = "DisplayString"
_SpLicenseErrDescription_Object = MibScalar
spLicenseErrDescription = _SpLicenseErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 1, 80),
    _SpLicenseErrDescription_Type()
)
spLicenseErrDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    spLicenseErrDescription.setStatus("current")
_PeakflowSPMgr_ObjectIdentity = ObjectIdentity
peakflowSPMgr = _PeakflowSPMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2)
)
_DeviceHealth_ObjectIdentity = ObjectIdentity
deviceHealth = _DeviceHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1)
)
_DeviceCpuLoadAvg1min_Type = Integer32
_DeviceCpuLoadAvg1min_Object = MibScalar
deviceCpuLoadAvg1min = _DeviceCpuLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 1),
    _DeviceCpuLoadAvg1min_Type()
)
deviceCpuLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg1min.setStatus("current")
_DeviceCpuLoadAvg5min_Type = Integer32
_DeviceCpuLoadAvg5min_Object = MibScalar
deviceCpuLoadAvg5min = _DeviceCpuLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 2),
    _DeviceCpuLoadAvg5min_Type()
)
deviceCpuLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg5min.setStatus("current")
_DeviceCpuLoadAvg15min_Type = Integer32
_DeviceCpuLoadAvg15min_Object = MibScalar
deviceCpuLoadAvg15min = _DeviceCpuLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 3),
    _DeviceCpuLoadAvg15min_Type()
)
deviceCpuLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg15min.setStatus("current")


class _DeviceDiskUsage_Type(Integer32):
    """Custom type deviceDiskUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceDiskUsage_Type.__name__ = "Integer32"
_DeviceDiskUsage_Object = MibScalar
deviceDiskUsage = _DeviceDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 4),
    _DeviceDiskUsage_Type()
)
deviceDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskUsage.setStatus("current")
_DevicePhysicalMemory_Type = Integer32
_DevicePhysicalMemory_Object = MibScalar
devicePhysicalMemory = _DevicePhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 5),
    _DevicePhysicalMemory_Type()
)
devicePhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePhysicalMemory.setStatus("current")
_DevicePhysicalMemoryInUse_Type = Integer32
_DevicePhysicalMemoryInUse_Object = MibScalar
devicePhysicalMemoryInUse = _DevicePhysicalMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 6),
    _DevicePhysicalMemoryInUse_Type()
)
devicePhysicalMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePhysicalMemoryInUse.setStatus("current")


class _DevicePhysicalMemoryUsage_Type(Integer32):
    """Custom type devicePhysicalMemoryUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevicePhysicalMemoryUsage_Type.__name__ = "Integer32"
_DevicePhysicalMemoryUsage_Object = MibScalar
devicePhysicalMemoryUsage = _DevicePhysicalMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 7),
    _DevicePhysicalMemoryUsage_Type()
)
devicePhysicalMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePhysicalMemoryUsage.setStatus("current")
_DeviceSwapSpace_Type = Integer32
_DeviceSwapSpace_Object = MibScalar
deviceSwapSpace = _DeviceSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 8),
    _DeviceSwapSpace_Type()
)
deviceSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSwapSpace.setStatus("current")
_DeviceSwapSpaceInUse_Type = Integer32
_DeviceSwapSpaceInUse_Object = MibScalar
deviceSwapSpaceInUse = _DeviceSwapSpaceInUse_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 9),
    _DeviceSwapSpaceInUse_Type()
)
deviceSwapSpaceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSwapSpaceInUse.setStatus("current")


class _DeviceSwapSpaceUsage_Type(Integer32):
    """Custom type deviceSwapSpaceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceSwapSpaceUsage_Type.__name__ = "Integer32"
_DeviceSwapSpaceUsage_Object = MibScalar
deviceSwapSpaceUsage = _DeviceSwapSpaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 10),
    _DeviceSwapSpaceUsage_Type()
)
deviceSwapSpaceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSwapSpaceUsage.setStatus("current")
_DeviceTotalFlows_Type = Counter32
_DeviceTotalFlows_Object = MibScalar
deviceTotalFlows = _DeviceTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 2, 1, 11),
    _DeviceTotalFlows_Type()
)
deviceTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalFlows.setStatus("current")
_PeakflowSPTraps_ObjectIdentity = ObjectIdentity
peakflowSPTraps = _PeakflowSPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3)
)
_PeakflowSPTrapsEnumerate_ObjectIdentity = ObjectIdentity
peakflowSPTrapsEnumerate = _PeakflowSPTrapsEnumerate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0)
)

# Managed Objects groups


# Notification objects

flowDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 1)
)
flowDown.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    flowDown.setStatus(
        "current"
    )

flowUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 2)
)
flowUp.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    flowUp.setStatus(
        "current"
    )

snmpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 3)
)
snmpDown.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    snmpDown.setStatus(
        "current"
    )

snmpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 4)
)
snmpUp.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    snmpUp.setStatus(
        "current"
    )

bgpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 5)
)
bgpDown.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    bgpDown.setStatus(
        "current"
    )

bgpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 6)
)
bgpUp.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    bgpUp.setStatus(
        "current"
    )

collectorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 7)
)
collectorDown.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spDetector"))
)
if mibBuilder.loadTexts:
    collectorDown.setStatus(
        "current"
    )

collectorUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 8)
)
collectorUp.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    collectorUp.setStatus(
        "current"
    )

collectorStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 9)
)
collectorStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    collectorStart.setStatus(
        "obsolete"
    )

bgpInstability = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 10)
)
bgpInstability.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"),
        ("PEAKFLOW-SP-MIB", "spBGPInstability"))
)
if mibBuilder.loadTexts:
    bgpInstability.setStatus(
        "current"
    )

bgpInstabilityDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 11)
)
bgpInstabilityDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"))
)
if mibBuilder.loadTexts:
    bgpInstabilityDone.setStatus(
        "current"
    )

bgpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 12)
)
bgpTrap.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spBGPTrapName"),
        ("PEAKFLOW-SP-MIB", "spBGPTrapEvent"),
        ("PEAKFLOW-SP-MIB", "spBGPTrapPrefix"),
        ("PEAKFLOW-SP-MIB", "spBGPTrapOldAttributes"),
        ("PEAKFLOW-SP-MIB", "spBGPTrapNewAttributes"))
)
if mibBuilder.loadTexts:
    bgpTrap.setStatus(
        "current"
    )

interfaceUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 13)
)
interfaceUsage.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"),
        ("PEAKFLOW-SP-MIB", "spInterface"),
        ("PEAKFLOW-SP-MIB", "spInterfaceIndex"),
        ("PEAKFLOW-SP-MIB", "spInterfaceSpeed"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spInterfaceUsage"))
)
if mibBuilder.loadTexts:
    interfaceUsage.setStatus(
        "current"
    )

interfaceUsageDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 14)
)
interfaceUsageDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"),
        ("PEAKFLOW-SP-MIB", "spInterface"),
        ("PEAKFLOW-SP-MIB", "spInterfaceIndex"),
        ("PEAKFLOW-SP-MIB", "spUsageType"))
)
if mibBuilder.loadTexts:
    interfaceUsageDone.setStatus(
        "current"
    )

autoclassifyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 15)
)
autoclassifyStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spUsername"))
)
if mibBuilder.loadTexts:
    autoclassifyStart.setStatus(
        "obsolete"
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 16)
)
configChange.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spUsername"),
        ("PEAKFLOW-SP-MIB", "spVersion"))
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        "current"
    )

notificationLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 17)
)
notificationLimit.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    notificationLimit.setStatus(
        "obsolete"
    )

reportDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 18)
)
reportDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spReportName"),
        ("PEAKFLOW-SP-MIB", "spReportID"),
        ("PEAKFLOW-SP-MIB", "spReportURL"))
)
if mibBuilder.loadTexts:
    reportDone.setStatus(
        "obsolete"
    )

bgpHijack = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 19)
)
bgpHijack.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spRouter"),
        ("PEAKFLOW-SP-MIB", "spHijackRoute"),
        ("PEAKFLOW-SP-MIB", "spHijackAttr"),
        ("PEAKFLOW-SP-MIB", "spHijackLocal"))
)
if mibBuilder.loadTexts:
    bgpHijack.setStatus(
        "current"
    )

managedObjectUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 20)
)
managedObjectUsage.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spManagedObjectFamily"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spUsage"),
        ("PEAKFLOW-SP-MIB", "spUnit"))
)
if mibBuilder.loadTexts:
    managedObjectUsage.setStatus(
        "current"
    )

managedObjectUsageDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 21)
)
managedObjectUsageDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spManagedObjectFamily"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spUnit"))
)
if mibBuilder.loadTexts:
    managedObjectUsageDone.setStatus(
        "current"
    )

hardwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 22)
)
hardwareFailure.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spHardwareFailureDescription"))
)
if mibBuilder.loadTexts:
    hardwareFailure.setStatus(
        "current"
    )

hardwareFailureDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 23)
)
hardwareFailureDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spHardwareFailureDescription"))
)
if mibBuilder.loadTexts:
    hardwareFailureDone.setStatus(
        "current"
    )

fingerprintFeedback = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 24)
)
fingerprintFeedback.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spFingerprintName"),
        ("PEAKFLOW-SP-MIB", "spFingerprintFeedback"))
)
if mibBuilder.loadTexts:
    fingerprintFeedback.setStatus(
        "current"
    )

fingerprintReceive = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 25)
)
fingerprintReceive.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spFingerprintName"),
        ("PEAKFLOW-SP-MIB", "spFingerprintSender"),
        ("PEAKFLOW-SP-MIB", "spFingerprintMessage"))
)
if mibBuilder.loadTexts:
    fingerprintReceive.setStatus(
        "current"
    )

dnsBaseline = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 26)
)
dnsBaseline.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spDNSName"),
        ("PEAKFLOW-SP-MIB", "spDNSExpected"),
        ("PEAKFLOW-SP-MIB", "spDNSObserved"))
)
if mibBuilder.loadTexts:
    dnsBaseline.setStatus(
        "current"
    )

dnsBaselineDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 27)
)
dnsBaselineDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spDNSName"),
        ("PEAKFLOW-SP-MIB", "spDNSExpected"),
        ("PEAKFLOW-SP-MIB", "spDNSObservedMean"),
        ("PEAKFLOW-SP-MIB", "spDNSObservedMax"))
)
if mibBuilder.loadTexts:
    dnsBaselineDone.setStatus(
        "current"
    )

alertScript = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 28)
)
alertScript.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spMitigationName"),
        ("PEAKFLOW-SP-MIB", "spScriptCommand"),
        ("PEAKFLOW-SP-MIB", "spScriptHost"),
        ("PEAKFLOW-SP-MIB", "spScriptPort"),
        ("PEAKFLOW-SP-MIB", "spScriptStart"))
)
if mibBuilder.loadTexts:
    alertScript.setStatus(
        "current"
    )

mitigationDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 29)
)
mitigationDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    mitigationDone.setStatus(
        "current"
    )

mitigationTMSStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 30)
)
mitigationTMSStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spMitigationName"),
        ("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spTMSPrefix"),
        ("PEAKFLOW-SP-MIB", "spTMSCommunity"),
        ("PEAKFLOW-SP-MIB", "spTMSTimeout"),
        ("PEAKFLOW-SP-MIB", "spMitigationStart"),
        ("PEAKFLOW-SP-MIB", "spTMSMultiPrefix"))
)
if mibBuilder.loadTexts:
    mitigationTMSStart.setStatus(
        "current"
    )

mitigationThirdPartyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 31)
)
mitigationThirdPartyStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spMitigationName"),
        ("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spThirdPartyZone"),
        ("PEAKFLOW-SP-MIB", "spThirdPartyAddr"),
        ("PEAKFLOW-SP-MIB", "spMitigationStart"))
)
if mibBuilder.loadTexts:
    mitigationThirdPartyStart.setStatus(
        "current"
    )

mitigationBlackholeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 32)
)
mitigationBlackholeStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spMitigationName"),
        ("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spBlackholeCommunity"),
        ("PEAKFLOW-SP-MIB", "spBlackholeTimeout"),
        ("PEAKFLOW-SP-MIB", "spBlackholePrefix"),
        ("PEAKFLOW-SP-MIB", "spBlackholeNexthop"),
        ("PEAKFLOW-SP-MIB", "spMitigationStart"))
)
if mibBuilder.loadTexts:
    mitigationBlackholeStart.setStatus(
        "current"
    )

mitigationFlowspecStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 33)
)
mitigationFlowspecStart.setObjects(
      *(("PEAKFLOW-SP-MIB", "spMitigationID"),
        ("PEAKFLOW-SP-MIB", "spMitigationName"),
        ("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spFlowspecCommunity"),
        ("PEAKFLOW-SP-MIB", "spFlowspecTimeout"),
        ("PEAKFLOW-SP-MIB", "spMitigationStart"))
)
if mibBuilder.loadTexts:
    mitigationFlowspecStart.setStatus(
        "current"
    )

spcommFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 34)
)
spcommFailure.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spCommFailureDestination"),
        ("PEAKFLOW-SP-MIB", "spCommFailureDescription"))
)
if mibBuilder.loadTexts:
    spcommFailure.setStatus(
        "current"
    )

spcommFailureDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 35)
)
spcommFailureDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spCommFailureDestination"),
        ("PEAKFLOW-SP-MIB", "spCommFailureDescription"))
)
if mibBuilder.loadTexts:
    spcommFailureDone.setStatus(
        "current"
    )

greDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 36)
)
greDown.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spGreTunnelDestination"))
)
if mibBuilder.loadTexts:
    greDown.setStatus(
        "current"
    )

greDownDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 37)
)
greDownDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spGreTunnelDestination"))
)
if mibBuilder.loadTexts:
    greDownDone.setStatus(
        "current"
    )

deviceSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 38)
)
deviceSystemError.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spSystemErrorType"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spSystemErrorDescription"))
)
if mibBuilder.loadTexts:
    deviceSystemError.setStatus(
        "current"
    )

deviceSystemErrorDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 39)
)
deviceSystemErrorDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spSystemErrorType"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spSystemErrorDescription"))
)
if mibBuilder.loadTexts:
    deviceSystemErrorDone.setStatus(
        "current"
    )

fingerprintUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 40)
)
fingerprintUsage.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spFingerprintName"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spUsage"),
        ("PEAKFLOW-SP-MIB", "spUnit"))
)
if mibBuilder.loadTexts:
    fingerprintUsage.setStatus(
        "current"
    )

fingerprintUsageDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 41)
)
fingerprintUsageDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spFingerprintName"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spUnit"))
)
if mibBuilder.loadTexts:
    fingerprintUsageDone.setStatus(
        "current"
    )

serviceUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 42)
)
serviceUsage.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spServiceName"),
        ("PEAKFLOW-SP-MIB", "spUsageType"),
        ("PEAKFLOW-SP-MIB", "spApplicationName"),
        ("PEAKFLOW-SP-MIB", "spServiceElement"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spUsage"))
)
if mibBuilder.loadTexts:
    serviceUsage.setStatus(
        "current"
    )

serviceUsageDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 43)
)
serviceUsageDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spServiceName"))
)
if mibBuilder.loadTexts:
    serviceUsageDone.setStatus(
        "current"
    )

dosNetworkProfiledAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 44)
)
dosNetworkProfiledAlert.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spImpactBps"),
        ("PEAKFLOW-SP-MIB", "spImpactPps"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spDetectedCountries"))
)
if mibBuilder.loadTexts:
    dosNetworkProfiledAlert.setStatus(
        "current"
    )

dosNetworkProfiledAlertDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 45)
)
dosNetworkProfiledAlertDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spImpactBps"),
        ("PEAKFLOW-SP-MIB", "spImpactPps"),
        ("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spDetectedCountries"))
)
if mibBuilder.loadTexts:
    dosNetworkProfiledAlertDone.setStatus(
        "current"
    )

dosHostDetectionAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 46)
)
dosHostDetectionAlert.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spAlertDetectionSignatures"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spInetAddress"),
        ("PEAKFLOW-SP-MIB", "spInetAddressType"),
        ("PEAKFLOW-SP-MIB", "spImpactBps"),
        ("PEAKFLOW-SP-MIB", "spImpactPps"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-SP-MIB", "spManagedObjects"))
)
if mibBuilder.loadTexts:
    dosHostDetectionAlert.setStatus(
        "current"
    )

dosHostDetectionAlertDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 47)
)
dosHostDetectionAlertDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spAlertDetectionSignatures"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spInetAddress"),
        ("PEAKFLOW-SP-MIB", "spInetAddressType"),
        ("PEAKFLOW-SP-MIB", "spImpactBps"),
        ("PEAKFLOW-SP-MIB", "spImpactPps"),
        ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"),
        ("PEAKFLOW-SP-MIB", "spManagedObjects"))
)
if mibBuilder.loadTexts:
    dosHostDetectionAlertDone.setStatus(
        "current"
    )

routingFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 48)
)
routingFailover.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    routingFailover.setStatus(
        "current"
    )

routingFailoverInterfaceDownAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 49)
)
routingFailoverInterfaceDownAlert.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spCollector"),
        ("PEAKFLOW-SP-MIB", "spRoutingFailoverInterfaces"))
)
if mibBuilder.loadTexts:
    routingFailoverInterfaceDownAlert.setStatus(
        "current"
    )

routingFailoverInterfaceDownAlertDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 50)
)
routingFailoverInterfaceDownAlertDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-DOS-MIB", "pdosUrl"),
        ("PEAKFLOW-SP-MIB", "spCollector"))
)
if mibBuilder.loadTexts:
    routingFailoverInterfaceDownAlertDone.setStatus(
        "current"
    )

trafficAutoMitigation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 51)
)
trafficAutoMitigation.setObjects(
    ("PEAKFLOW-SP-MIB", "spManagedObject")
)
if mibBuilder.loadTexts:
    trafficAutoMitigation.setStatus(
        "current"
    )

cloudSignalingMitigationRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 52)
)
cloudSignalingMitigationRequest.setObjects(
      *(("PEAKFLOW-SP-MIB", "spManagedObject"),
        ("PEAKFLOW-SP-MIB", "spPravail"))
)
if mibBuilder.loadTexts:
    cloudSignalingMitigationRequest.setStatus(
        "current"
    )

licenseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 53)
)
licenseError.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrType"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrCount"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrDescription"))
)
if mibBuilder.loadTexts:
    licenseError.setStatus(
        "current"
    )

licenseErrorDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 4, 3, 0, 54)
)
licenseErrorDone.setObjects(
      *(("PEAKFLOW-SP-MIB", "spAlertID"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrType"),
        ("PEAKFLOW-SP-MIB", "spThreshold"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrLimit"),
        ("PEAKFLOW-SP-MIB", "spLicenseErrDescription"))
)
if mibBuilder.loadTexts:
    licenseErrorDone.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKFLOW-SP-MIB",
    **{"peakflowSPMIB": peakflowSPMIB,
       "peakflowSPCMI": peakflowSPCMI,
       "spCollector": spCollector,
       "spRouter": spRouter,
       "spInterface": spInterface,
       "spInterfaceIndex": spInterfaceIndex,
       "spDuration": spDuration,
       "spBGPEvent": spBGPEvent,
       "spBGPInstability": spBGPInstability,
       "spBGPTrapName": spBGPTrapName,
       "spBGPTrapEvent": spBGPTrapEvent,
       "spBGPTrapPrefix": spBGPTrapPrefix,
       "spBGPTrapOldAttributes": spBGPTrapOldAttributes,
       "spBGPTrapNewAttributes": spBGPTrapNewAttributes,
       "spInterfaceSpeed": spInterfaceSpeed,
       "spInterfaceUsage": spInterfaceUsage,
       "spReportURL": spReportURL,
       "spReportName": spReportName,
       "spReportID": spReportID,
       "spAlertID": spAlertID,
       "spHijackRoute": spHijackRoute,
       "spHijackAttr": spHijackAttr,
       "spHijackLocal": spHijackLocal,
       "spUsername": spUsername,
       "spVersion": spVersion,
       "spUsageType": spUsageType,
       "spManagedObject": spManagedObject,
       "spManagedObjectFamily": spManagedObjectFamily,
       "spThreshold": spThreshold,
       "spUsage": spUsage,
       "spUnit": spUnit,
       "spHardwareFailureDescription": spHardwareFailureDescription,
       "spFingerprintName": spFingerprintName,
       "spFingerprintFeedback": spFingerprintFeedback,
       "spFingerprintSender": spFingerprintSender,
       "spFingerprintMessage": spFingerprintMessage,
       "spMitigationID": spMitigationID,
       "spDNSName": spDNSName,
       "spDNSExpected": spDNSExpected,
       "spDNSObserved": spDNSObserved,
       "spDNSObservedMean": spDNSObservedMean,
       "spDNSObservedMax": spDNSObservedMax,
       "spMitigationName": spMitigationName,
       "spScriptCommand": spScriptCommand,
       "spScriptHost": spScriptHost,
       "spScriptPort": spScriptPort,
       "spScriptStart": spScriptStart,
       "spTMSPrefix": spTMSPrefix,
       "spTMSCommunity": spTMSCommunity,
       "spTMSTimeout": spTMSTimeout,
       "spThirdPartyZone": spThirdPartyZone,
       "spThirdPartyAddr": spThirdPartyAddr,
       "spMitigationStart": spMitigationStart,
       "spBlackholeCommunity": spBlackholeCommunity,
       "spBlackholeTimeout": spBlackholeTimeout,
       "spBlackholePrefix": spBlackholePrefix,
       "spBlackholeNexthop": spBlackholeNexthop,
       "spFlowspecCommunity": spFlowspecCommunity,
       "spFlowspecTimeout": spFlowspecTimeout,
       "spCommFailureDestination": spCommFailureDestination,
       "spCommFailureDescription": spCommFailureDescription,
       "spGreTunnelDestination": spGreTunnelDestination,
       "spSystemErrorType": spSystemErrorType,
       "spSystemErrorDescription": spSystemErrorDescription,
       "spServiceName": spServiceName,
       "spServiceElement": spServiceElement,
       "spApplicationName": spApplicationName,
       "spAlertDetectionSignatures": spAlertDetectionSignatures,
       "spManagedObjects": spManagedObjects,
       "spInetAddressType": spInetAddressType,
       "spInetAddress": spInetAddress,
       "spImpactBps": spImpactBps,
       "spImpactPps": spImpactPps,
       "spDetectedCountries": spDetectedCountries,
       "spRoutingFailoverInterfaces": spRoutingFailoverInterfaces,
       "spPravail": spPravail,
       "spDetector": spDetector,
       "spTMSMultiPrefix": spTMSMultiPrefix,
       "spLicenseErrType": spLicenseErrType,
       "spLicenseErrCount": spLicenseErrCount,
       "spLicenseErrLimit": spLicenseErrLimit,
       "spLicenseErrDescription": spLicenseErrDescription,
       "peakflowSPMgr": peakflowSPMgr,
       "deviceHealth": deviceHealth,
       "deviceCpuLoadAvg1min": deviceCpuLoadAvg1min,
       "deviceCpuLoadAvg5min": deviceCpuLoadAvg5min,
       "deviceCpuLoadAvg15min": deviceCpuLoadAvg15min,
       "deviceDiskUsage": deviceDiskUsage,
       "devicePhysicalMemory": devicePhysicalMemory,
       "devicePhysicalMemoryInUse": devicePhysicalMemoryInUse,
       "devicePhysicalMemoryUsage": devicePhysicalMemoryUsage,
       "deviceSwapSpace": deviceSwapSpace,
       "deviceSwapSpaceInUse": deviceSwapSpaceInUse,
       "deviceSwapSpaceUsage": deviceSwapSpaceUsage,
       "deviceTotalFlows": deviceTotalFlows,
       "peakflowSPTraps": peakflowSPTraps,
       "peakflowSPTrapsEnumerate": peakflowSPTrapsEnumerate,
       "flowDown": flowDown,
       "flowUp": flowUp,
       "snmpDown": snmpDown,
       "snmpUp": snmpUp,
       "bgpDown": bgpDown,
       "bgpUp": bgpUp,
       "collectorDown": collectorDown,
       "collectorUp": collectorUp,
       "collectorStart": collectorStart,
       "bgpInstability": bgpInstability,
       "bgpInstabilityDone": bgpInstabilityDone,
       "bgpTrap": bgpTrap,
       "interfaceUsage": interfaceUsage,
       "interfaceUsageDone": interfaceUsageDone,
       "autoclassifyStart": autoclassifyStart,
       "configChange": configChange,
       "notificationLimit": notificationLimit,
       "reportDone": reportDone,
       "bgpHijack": bgpHijack,
       "managedObjectUsage": managedObjectUsage,
       "managedObjectUsageDone": managedObjectUsageDone,
       "hardwareFailure": hardwareFailure,
       "hardwareFailureDone": hardwareFailureDone,
       "fingerprintFeedback": fingerprintFeedback,
       "fingerprintReceive": fingerprintReceive,
       "dnsBaseline": dnsBaseline,
       "dnsBaselineDone": dnsBaselineDone,
       "alertScript": alertScript,
       "mitigationDone": mitigationDone,
       "mitigationTMSStart": mitigationTMSStart,
       "mitigationThirdPartyStart": mitigationThirdPartyStart,
       "mitigationBlackholeStart": mitigationBlackholeStart,
       "mitigationFlowspecStart": mitigationFlowspecStart,
       "spcommFailure": spcommFailure,
       "spcommFailureDone": spcommFailureDone,
       "greDown": greDown,
       "greDownDone": greDownDone,
       "deviceSystemError": deviceSystemError,
       "deviceSystemErrorDone": deviceSystemErrorDone,
       "fingerprintUsage": fingerprintUsage,
       "fingerprintUsageDone": fingerprintUsageDone,
       "serviceUsage": serviceUsage,
       "serviceUsageDone": serviceUsageDone,
       "dosNetworkProfiledAlert": dosNetworkProfiledAlert,
       "dosNetworkProfiledAlertDone": dosNetworkProfiledAlertDone,
       "dosHostDetectionAlert": dosHostDetectionAlert,
       "dosHostDetectionAlertDone": dosHostDetectionAlertDone,
       "routingFailover": routingFailover,
       "routingFailoverInterfaceDownAlert": routingFailoverInterfaceDownAlert,
       "routingFailoverInterfaceDownAlertDone": routingFailoverInterfaceDownAlertDone,
       "trafficAutoMitigation": trafficAutoMitigation,
       "cloudSignalingMitigationRequest": cloudSignalingMitigationRequest,
       "licenseError": licenseError,
       "licenseErrorDone": licenseErrorDone}
)
