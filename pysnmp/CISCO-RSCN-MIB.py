# SNMP MIB module (CISCO-RSCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RSCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:42 2024
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

(FcGs3RejectReasonCode,) = mibBuilder.importSymbols(
    "CISCO-NS-MIB",
    "FcGs3RejectReasonCode")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddressId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoRscnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292)
)
ciscoRscnMIB.setRevisions(
        ("2008-09-01 00:00",
         "2006-08-17 00:00",
         "2005-05-06 00:00",
         "2003-10-16 00:00",
         "2002-09-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRscnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRscnMIBObjects = _CiscoRscnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1)
)
_RscnConfiguration_ObjectIdentity = ObjectIdentity
rscnConfiguration = _RscnConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1)
)


class _RscnScrNumber_Type(Integer32):
    """Custom type rscnScrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RscnScrNumber_Type.__name__ = "Integer32"
_RscnScrNumber_Object = MibScalar
rscnScrNumber = _RscnScrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 1),
    _RscnScrNumber_Type()
)
rscnScrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnScrNumber.setStatus("current")
_RscnScrTable_Object = MibTable
rscnScrTable = _RscnScrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rscnScrTable.setStatus("current")
_RscnScrEntry_Object = MibTableRow
rscnScrEntry = _RscnScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1)
)
rscnScrEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-RSCN-MIB", "rscnScrFcId"),
)
if mibBuilder.loadTexts:
    rscnScrEntry.setStatus("current")
_RscnScrFcId_Type = FcAddressId
_RscnScrFcId_Object = MibTableColumn
rscnScrFcId = _RscnScrFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1, 1),
    _RscnScrFcId_Type()
)
rscnScrFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rscnScrFcId.setStatus("current")


class _RscnScrRegType_Type(Integer32):
    """Custom type rscnScrRegType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromBoth", 3),
          ("fromFabricCtrlr", 1),
          ("fromNxPort", 2))
    )


_RscnScrRegType_Type.__name__ = "Integer32"
_RscnScrRegType_Object = MibTableColumn
rscnScrRegType = _RscnScrRegType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1, 2),
    _RscnScrRegType_Type()
)
rscnScrRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnScrRegType.setStatus("current")


class _RscnIlsRejectReqNotifyEnable_Type(TruthValue):
    """Custom type rscnIlsRejectReqNotifyEnable based on TruthValue"""


_RscnIlsRejectReqNotifyEnable_Object = MibScalar
rscnIlsRejectReqNotifyEnable = _RscnIlsRejectReqNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 3),
    _RscnIlsRejectReqNotifyEnable_Type()
)
rscnIlsRejectReqNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnIlsRejectReqNotifyEnable.setStatus("current")


class _RscnElsRejectReqNotifyEnable_Type(TruthValue):
    """Custom type rscnElsRejectReqNotifyEnable based on TruthValue"""


_RscnElsRejectReqNotifyEnable_Object = MibScalar
rscnElsRejectReqNotifyEnable = _RscnElsRejectReqNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 4),
    _RscnElsRejectReqNotifyEnable_Type()
)
rscnElsRejectReqNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnElsRejectReqNotifyEnable.setStatus("current")
_RscnNotifyFcId_Type = FcAddressId
_RscnNotifyFcId_Object = MibScalar
rscnNotifyFcId = _RscnNotifyFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 5),
    _RscnNotifyFcId_Type()
)
rscnNotifyFcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rscnNotifyFcId.setStatus("current")
_RscnMultiPidTable_Object = MibTable
rscnMultiPidTable = _RscnMultiPidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rscnMultiPidTable.setStatus("current")
_RscnMultiPidEntry_Object = MibTableRow
rscnMultiPidEntry = _RscnMultiPidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6, 1)
)
rscnMultiPidEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    rscnMultiPidEntry.setStatus("current")


class _RscnMultiPidEnable_Type(TruthValue):
    """Custom type rscnMultiPidEnable based on TruthValue"""


_RscnMultiPidEnable_Object = MibTableColumn
rscnMultiPidEnable = _RscnMultiPidEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6, 1, 1),
    _RscnMultiPidEnable_Type()
)
rscnMultiPidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnMultiPidEnable.setStatus("current")
_RscnEventTovTable_Object = MibTable
rscnEventTovTable = _RscnEventTovTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rscnEventTovTable.setStatus("current")
_RscnEventTovEntry_Object = MibTableRow
rscnEventTovEntry = _RscnEventTovEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7, 1)
)
rscnEventTovEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    rscnEventTovEntry.setStatus("current")


class _RscnEventTov_Type(Unsigned32):
    """Custom type rscnEventTov based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RscnEventTov_Type.__name__ = "Unsigned32"
_RscnEventTov_Object = MibTableColumn
rscnEventTov = _RscnEventTov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7, 1, 1),
    _RscnEventTov_Type()
)
rscnEventTov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnEventTov.setStatus("current")
if mibBuilder.loadTexts:
    rscnEventTov.setUnits("milli-secs")


class _RscnIlsRxRejectReqNotifyEnable_Type(TruthValue):
    """Custom type rscnIlsRxRejectReqNotifyEnable based on TruthValue"""


_RscnIlsRxRejectReqNotifyEnable_Object = MibScalar
rscnIlsRxRejectReqNotifyEnable = _RscnIlsRxRejectReqNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 8),
    _RscnIlsRxRejectReqNotifyEnable_Type()
)
rscnIlsRxRejectReqNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnIlsRxRejectReqNotifyEnable.setStatus("current")


class _RscnElsRxRejectReqNotifyEnable_Type(TruthValue):
    """Custom type rscnElsRxRejectReqNotifyEnable based on TruthValue"""


_RscnElsRxRejectReqNotifyEnable_Object = MibScalar
rscnElsRxRejectReqNotifyEnable = _RscnElsRxRejectReqNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 9),
    _RscnElsRxRejectReqNotifyEnable_Type()
)
rscnElsRxRejectReqNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscnElsRxRejectReqNotifyEnable.setStatus("current")
_RscnStats_ObjectIdentity = ObjectIdentity
rscnStats = _RscnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2)
)
_RscnScrTotalRejects_Type = Counter32
_RscnScrTotalRejects_Object = MibScalar
rscnScrTotalRejects = _RscnScrTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 1),
    _RscnScrTotalRejects_Type()
)
rscnScrTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnScrTotalRejects.setStatus("current")
_RscnRscnReqTotalRejects_Type = Counter32
_RscnRscnReqTotalRejects_Object = MibScalar
rscnRscnReqTotalRejects = _RscnRscnReqTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 2),
    _RscnRscnReqTotalRejects_Type()
)
rscnRscnReqTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnRscnReqTotalRejects.setStatus("current")
_RscnSwRscnReqTotalRejects_Type = Counter32
_RscnSwRscnReqTotalRejects_Object = MibScalar
rscnSwRscnReqTotalRejects = _RscnSwRscnReqTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 3),
    _RscnSwRscnReqTotalRejects_Type()
)
rscnSwRscnReqTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnSwRscnReqTotalRejects.setStatus("current")
_RscnStatsTable_Object = MibTable
rscnStatsTable = _RscnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rscnStatsTable.setStatus("current")
_RscnStatsEntry_Object = MibTableRow
rscnStatsEntry = _RscnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1)
)
rscnStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    rscnStatsEntry.setStatus("current")
_RscnRxScrs_Type = Counter32
_RscnRxScrs_Object = MibTableColumn
rscnRxScrs = _RscnRxScrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 1),
    _RscnRxScrs_Type()
)
rscnRxScrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnRxScrs.setStatus("current")
_RscnRxRscns_Type = Counter32
_RscnRxRscns_Object = MibTableColumn
rscnRxRscns = _RscnRxRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 2),
    _RscnRxRscns_Type()
)
rscnRxRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnRxRscns.setStatus("current")
_RscnTxRscns_Type = Counter32
_RscnTxRscns_Object = MibTableColumn
rscnTxRscns = _RscnTxRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 3),
    _RscnTxRscns_Type()
)
rscnTxRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnTxRscns.setStatus("current")
_RscnRxSwRscns_Type = Counter32
_RscnRxSwRscns_Object = MibTableColumn
rscnRxSwRscns = _RscnRxSwRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 4),
    _RscnRxSwRscns_Type()
)
rscnRxSwRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnRxSwRscns.setStatus("current")
_RscnTxSwRscns_Type = Counter32
_RscnTxSwRscns_Object = MibTableColumn
rscnTxSwRscns = _RscnTxSwRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 5),
    _RscnTxSwRscns_Type()
)
rscnTxSwRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnTxSwRscns.setStatus("current")
_RscnScrRej_Type = Counter32
_RscnScrRej_Object = MibTableColumn
rscnScrRej = _RscnScrRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 6),
    _RscnScrRej_Type()
)
rscnScrRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnScrRej.setStatus("current")
_RscnRscnReqRej_Type = Counter32
_RscnRscnReqRej_Object = MibTableColumn
rscnRscnReqRej = _RscnRscnReqRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 7),
    _RscnRscnReqRej_Type()
)
rscnRscnReqRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnRscnReqRej.setStatus("current")
_RscnSwRscnReqRej_Type = Counter32
_RscnSwRscnReqRej_Object = MibTableColumn
rscnSwRscnReqRej = _RscnSwRscnReqRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 8),
    _RscnSwRscnReqRej_Type()
)
rscnSwRscnReqRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnSwRscnReqRej.setStatus("current")
_RscnInformation_ObjectIdentity = ObjectIdentity
rscnInformation = _RscnInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3)
)
_RscnIlsRejReasonCode_Type = FcGs3RejectReasonCode
_RscnIlsRejReasonCode_Object = MibScalar
rscnIlsRejReasonCode = _RscnIlsRejReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3, 1),
    _RscnIlsRejReasonCode_Type()
)
rscnIlsRejReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnIlsRejReasonCode.setStatus("current")
_RscnElsRejReasonCode_Type = FcGs3RejectReasonCode
_RscnElsRejReasonCode_Object = MibScalar
rscnElsRejReasonCode = _RscnElsRejReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3, 2),
    _RscnElsRejReasonCode_Type()
)
rscnElsRejReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscnElsRejReasonCode.setStatus("current")
_RscnNotification_ObjectIdentity = ObjectIdentity
rscnNotification = _RscnNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4)
)
_RscnNotifications_ObjectIdentity = ObjectIdentity
rscnNotifications = _RscnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0)
)
_RscnMIBConformance_ObjectIdentity = ObjectIdentity
rscnMIBConformance = _RscnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2)
)
_RscnMIBCompliances_ObjectIdentity = ObjectIdentity
rscnMIBCompliances = _RscnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1)
)
_RscnMIBGroups_ObjectIdentity = ObjectIdentity
rscnMIBGroups = _RscnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2)
)

# Managed Objects groups

rscnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 1)
)
rscnConfigGroup.setObjects(
      *(("CISCO-RSCN-MIB", "rscnScrNumber"),
        ("CISCO-RSCN-MIB", "rscnScrRegType"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
)
if mibBuilder.loadTexts:
    rscnConfigGroup.setStatus("deprecated")

rscnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 2)
)
rscnStatsGroup.setObjects(
      *(("CISCO-RSCN-MIB", "rscnScrTotalRejects"),
        ("CISCO-RSCN-MIB", "rscnRscnReqTotalRejects"),
        ("CISCO-RSCN-MIB", "rscnSwRscnReqTotalRejects"),
        ("CISCO-RSCN-MIB", "rscnRxScrs"),
        ("CISCO-RSCN-MIB", "rscnRxRscns"),
        ("CISCO-RSCN-MIB", "rscnTxRscns"),
        ("CISCO-RSCN-MIB", "rscnRxSwRscns"),
        ("CISCO-RSCN-MIB", "rscnTxSwRscns"),
        ("CISCO-RSCN-MIB", "rscnScrRej"),
        ("CISCO-RSCN-MIB", "rscnRscnReqRej"),
        ("CISCO-RSCN-MIB", "rscnSwRscnReqRej"))
)
if mibBuilder.loadTexts:
    rscnStatsGroup.setStatus("current")

rscnNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 3)
)
rscnNotifyControlGroup.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnElsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnIlsRejectReqNotifyEnable"),
        ("CISCO-RSCN-MIB", "rscnElsRejectReqNotifyEnable"))
)
if mibBuilder.loadTexts:
    rscnNotifyControlGroup.setStatus("current")

rscnConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 5)
)
rscnConfigGroupRev1.setObjects(
      *(("CISCO-RSCN-MIB", "rscnScrNumber"),
        ("CISCO-RSCN-MIB", "rscnScrRegType"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"),
        ("CISCO-RSCN-MIB", "rscnMultiPidEnable"))
)
if mibBuilder.loadTexts:
    rscnConfigGroupRev1.setStatus("current")

rscnConfigGroupRev1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 6)
)
rscnConfigGroupRev1Sup1.setObjects(
    ("CISCO-RSCN-MIB", "rscnEventTov")
)
if mibBuilder.loadTexts:
    rscnConfigGroupRev1Sup1.setStatus("current")

rscnNotifyControlGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 8)
)
rscnNotifyControlGroupSup1.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRxRejectReqNotifyEnable"),
        ("CISCO-RSCN-MIB", "rscnElsRxRejectReqNotifyEnable"))
)
if mibBuilder.loadTexts:
    rscnNotifyControlGroupSup1.setStatus("current")


# Notification objects

rscnElsRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 1)
)
rscnElsRejectReqNotify.setObjects(
      *(("CISCO-RSCN-MIB", "rscnElsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
)
if mibBuilder.loadTexts:
    rscnElsRejectReqNotify.setStatus(
        "current"
    )

rscnIlsRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 2)
)
rscnIlsRejectReqNotify.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
)
if mibBuilder.loadTexts:
    rscnIlsRejectReqNotify.setStatus(
        "current"
    )

rscnElsRxRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 3)
)
rscnElsRxRejectReqNotify.setObjects(
      *(("CISCO-RSCN-MIB", "rscnElsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
)
if mibBuilder.loadTexts:
    rscnElsRxRejectReqNotify.setStatus(
        "current"
    )

rscnIlsRxRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 4)
)
rscnIlsRxRejectReqNotify.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"),
        ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
)
if mibBuilder.loadTexts:
    rscnIlsRxRejectReqNotify.setStatus(
        "current"
    )


# Notifications groups

rscnNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 4)
)
rscnNotifyGroup.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRejectReqNotify"),
        ("CISCO-RSCN-MIB", "rscnElsRejectReqNotify"))
)
if mibBuilder.loadTexts:
    rscnNotifyGroup.setStatus(
        "current"
    )

rscnRejectNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 7)
)
rscnRejectNotifyGroup.setObjects(
      *(("CISCO-RSCN-MIB", "rscnIlsRxRejectReqNotify"),
        ("CISCO-RSCN-MIB", "rscnElsRxRejectReqNotify"))
)
if mibBuilder.loadTexts:
    rscnRejectNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rscnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rscnMIBCompliance.setStatus(
        "deprecated"
    )

rscnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rscnMIBComplianceRev1.setStatus(
        "deprecated"
    )

rscnMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rscnMIBComplianceRev2.setStatus(
        "deprecated"
    )

rscnMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rscnMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RSCN-MIB",
    **{"ciscoRscnMIB": ciscoRscnMIB,
       "ciscoRscnMIBObjects": ciscoRscnMIBObjects,
       "rscnConfiguration": rscnConfiguration,
       "rscnScrNumber": rscnScrNumber,
       "rscnScrTable": rscnScrTable,
       "rscnScrEntry": rscnScrEntry,
       "rscnScrFcId": rscnScrFcId,
       "rscnScrRegType": rscnScrRegType,
       "rscnIlsRejectReqNotifyEnable": rscnIlsRejectReqNotifyEnable,
       "rscnElsRejectReqNotifyEnable": rscnElsRejectReqNotifyEnable,
       "rscnNotifyFcId": rscnNotifyFcId,
       "rscnMultiPidTable": rscnMultiPidTable,
       "rscnMultiPidEntry": rscnMultiPidEntry,
       "rscnMultiPidEnable": rscnMultiPidEnable,
       "rscnEventTovTable": rscnEventTovTable,
       "rscnEventTovEntry": rscnEventTovEntry,
       "rscnEventTov": rscnEventTov,
       "rscnIlsRxRejectReqNotifyEnable": rscnIlsRxRejectReqNotifyEnable,
       "rscnElsRxRejectReqNotifyEnable": rscnElsRxRejectReqNotifyEnable,
       "rscnStats": rscnStats,
       "rscnScrTotalRejects": rscnScrTotalRejects,
       "rscnRscnReqTotalRejects": rscnRscnReqTotalRejects,
       "rscnSwRscnReqTotalRejects": rscnSwRscnReqTotalRejects,
       "rscnStatsTable": rscnStatsTable,
       "rscnStatsEntry": rscnStatsEntry,
       "rscnRxScrs": rscnRxScrs,
       "rscnRxRscns": rscnRxRscns,
       "rscnTxRscns": rscnTxRscns,
       "rscnRxSwRscns": rscnRxSwRscns,
       "rscnTxSwRscns": rscnTxSwRscns,
       "rscnScrRej": rscnScrRej,
       "rscnRscnReqRej": rscnRscnReqRej,
       "rscnSwRscnReqRej": rscnSwRscnReqRej,
       "rscnInformation": rscnInformation,
       "rscnIlsRejReasonCode": rscnIlsRejReasonCode,
       "rscnElsRejReasonCode": rscnElsRejReasonCode,
       "rscnNotification": rscnNotification,
       "rscnNotifications": rscnNotifications,
       "rscnElsRejectReqNotify": rscnElsRejectReqNotify,
       "rscnIlsRejectReqNotify": rscnIlsRejectReqNotify,
       "rscnElsRxRejectReqNotify": rscnElsRxRejectReqNotify,
       "rscnIlsRxRejectReqNotify": rscnIlsRxRejectReqNotify,
       "rscnMIBConformance": rscnMIBConformance,
       "rscnMIBCompliances": rscnMIBCompliances,
       "rscnMIBCompliance": rscnMIBCompliance,
       "rscnMIBComplianceRev1": rscnMIBComplianceRev1,
       "rscnMIBComplianceRev2": rscnMIBComplianceRev2,
       "rscnMIBComplianceRev3": rscnMIBComplianceRev3,
       "rscnMIBGroups": rscnMIBGroups,
       "rscnConfigGroup": rscnConfigGroup,
       "rscnStatsGroup": rscnStatsGroup,
       "rscnNotifyControlGroup": rscnNotifyControlGroup,
       "rscnNotifyGroup": rscnNotifyGroup,
       "rscnConfigGroupRev1": rscnConfigGroupRev1,
       "rscnConfigGroupRev1Sup1": rscnConfigGroupRev1Sup1,
       "rscnRejectNotifyGroup": rscnRejectNotifyGroup,
       "rscnNotifyControlGroupSup1": rscnNotifyControlGroupSup1}
)
