# SNMP MIB module (CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMobilePolicyChargingControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690)
)
ciscoMobilePolicyChargingControlMIB.setRevisions(
        ("2009-07-10 00:00",
         "2009-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMobilePolicyChargingControlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMobilePolicyChargingControlMIBNotifs = _CiscoMobilePolicyChargingControlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 0)
)
_CiscoMobilePolicyChargingControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMobilePolicyChargingControlMIBObjects = _CiscoMobilePolicyChargingControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1)
)
_CmpccConfig_ObjectIdentity = ObjectIdentity
cmpccConfig = _CmpccConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1)
)
_CmpccProfileConfigTable_Object = MibTable
cmpccProfileConfigTable = _CmpccProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmpccProfileConfigTable.setStatus("current")
_CmpccProfileConfigTableEntry_Object = MibTableRow
cmpccProfileConfigTableEntry = _CmpccProfileConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1, 1)
)
cmpccProfileConfigTableEntry.setIndexNames(
    (0, "CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpcProfileName"),
    (0, "CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpcMethodList"),
)
if mibBuilder.loadTexts:
    cmpccProfileConfigTableEntry.setStatus("current")


class _CmpccpcProfileName_Type(SnmpAdminString):
    """Custom type cmpccpcProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CmpccpcProfileName_Type.__name__ = "SnmpAdminString"
_CmpccpcProfileName_Object = MibTableColumn
cmpccpcProfileName = _CmpccpcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1, 1, 1),
    _CmpccpcProfileName_Type()
)
cmpccpcProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmpccpcProfileName.setStatus("current")


class _CmpccpcMethodList_Type(SnmpAdminString):
    """Custom type cmpccpcMethodList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmpccpcMethodList_Type.__name__ = "SnmpAdminString"
_CmpccpcMethodList_Object = MibTableColumn
cmpccpcMethodList = _CmpccpcMethodList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1, 1, 2),
    _CmpccpcMethodList_Type()
)
cmpccpcMethodList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmpccpcMethodList.setStatus("current")


class _CmpccpcDestinationRealm_Type(SnmpAdminString):
    """Custom type cmpccpcDestinationRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmpccpcDestinationRealm_Type.__name__ = "SnmpAdminString"
_CmpccpcDestinationRealm_Object = MibTableColumn
cmpccpcDestinationRealm = _CmpccpcDestinationRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1, 1, 3),
    _CmpccpcDestinationRealm_Type()
)
cmpccpcDestinationRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmpccpcDestinationRealm.setStatus("current")
_CmpccpcRowStatus_Type = RowStatus
_CmpccpcRowStatus_Object = MibTableColumn
cmpccpcRowStatus = _CmpccpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 1, 1, 4),
    _CmpccpcRowStatus_Type()
)
cmpccpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmpccpcRowStatus.setStatus("current")
_CmpccPreloadEnable_Type = TruthValue
_CmpccPreloadEnable_Object = MibScalar
cmpccPreloadEnable = _CmpccPreloadEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 2),
    _CmpccPreloadEnable_Type()
)
cmpccPreloadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccPreloadEnable.setStatus("current")


class _CmpccProfileDefault_Type(SnmpAdminString):
    """Custom type cmpccProfileDefault based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CmpccProfileDefault_Type.__name__ = "SnmpAdminString"
_CmpccProfileDefault_Object = MibScalar
cmpccProfileDefault = _CmpccProfileDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 3),
    _CmpccProfileDefault_Type()
)
cmpccProfileDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccProfileDefault.setStatus("current")


class _CmpccMethodListPreload_Type(SnmpAdminString):
    """Custom type cmpccMethodListPreload based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmpccMethodListPreload_Type.__name__ = "SnmpAdminString"
_CmpccMethodListPreload_Object = MibScalar
cmpccMethodListPreload = _CmpccMethodListPreload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 4),
    _CmpccMethodListPreload_Type()
)
cmpccMethodListPreload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccMethodListPreload.setStatus("current")


class _CmpccDestinationRealmString_Type(SnmpAdminString):
    """Custom type cmpccDestinationRealmString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmpccDestinationRealmString_Type.__name__ = "SnmpAdminString"
_CmpccDestinationRealmString_Object = MibScalar
cmpccDestinationRealmString = _CmpccDestinationRealmString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 5),
    _CmpccDestinationRealmString_Type()
)
cmpccDestinationRealmString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccDestinationRealmString.setStatus("current")


class _CmpccPreloadTimeout_Type(TimeIntervalSec):
    """Custom type cmpccPreloadTimeout based on TimeIntervalSec"""
    defaultValue = 1800

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 7200),
    )


_CmpccPreloadTimeout_Type.__name__ = "TimeIntervalSec"
_CmpccPreloadTimeout_Object = MibScalar
cmpccPreloadTimeout = _CmpccPreloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 1, 6),
    _CmpccPreloadTimeout_Type()
)
cmpccPreloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccPreloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cmpccPreloadTimeout.setUnits("Seconds")
_CmpccStats_ObjectIdentity = ObjectIdentity
cmpccStats = _CmpccStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2)
)
_CmpccGlobalStatsTable_Object = MibTable
cmpccGlobalStatsTable = _CmpccGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmpccGlobalStatsTable.setStatus("current")
_CmpccGlobalStatsTableEntry_Object = MibTableRow
cmpccGlobalStatsTableEntry = _CmpccGlobalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1)
)
cmpccGlobalStatsTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmpccGlobalStatsTableEntry.setStatus("current")
_CmpccgsTotalSessions_Type = CounterBasedGauge64
_CmpccgsTotalSessions_Object = MibTableColumn
cmpccgsTotalSessions = _CmpccgsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 1),
    _CmpccgsTotalSessions_Type()
)
cmpccgsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsTotalSessions.setStatus("current")
_CmpccgsCCRInitialSent_Type = Counter64
_CmpccgsCCRInitialSent_Object = MibTableColumn
cmpccgsCCRInitialSent = _CmpccgsCCRInitialSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 2),
    _CmpccgsCCRInitialSent_Type()
)
cmpccgsCCRInitialSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCRInitialSent.setStatus("current")
_CmpccgsCCRUpdateSent_Type = Counter64
_CmpccgsCCRUpdateSent_Object = MibTableColumn
cmpccgsCCRUpdateSent = _CmpccgsCCRUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 3),
    _CmpccgsCCRUpdateSent_Type()
)
cmpccgsCCRUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCRUpdateSent.setStatus("current")
_CmpccgsCCRFinalSent_Type = Counter64
_CmpccgsCCRFinalSent_Object = MibTableColumn
cmpccgsCCRFinalSent = _CmpccgsCCRFinalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 4),
    _CmpccgsCCRFinalSent_Type()
)
cmpccgsCCRFinalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCRFinalSent.setStatus("current")
_CmpccgsCCARecd_Type = Counter64
_CmpccgsCCARecd_Object = MibTableColumn
cmpccgsCCARecd = _CmpccgsCCARecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 5),
    _CmpccgsCCARecd_Type()
)
cmpccgsCCARecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCARecd.setStatus("current")
_CmpccgsRARRecd_Type = Counter64
_CmpccgsRARRecd_Object = MibTableColumn
cmpccgsRARRecd = _CmpccgsRARRecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 6),
    _CmpccgsRARRecd_Type()
)
cmpccgsRARRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsRARRecd.setStatus("current")
_CmpccgsRAASent_Type = Counter64
_CmpccgsRAASent_Object = MibTableColumn
cmpccgsRAASent = _CmpccgsRAASent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 7),
    _CmpccgsRAASent_Type()
)
cmpccgsRAASent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsRAASent.setStatus("current")
_CmpccgsCCRFailures_Type = Counter64
_CmpccgsCCRFailures_Object = MibTableColumn
cmpccgsCCRFailures = _CmpccgsCCRFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 8),
    _CmpccgsCCRFailures_Type()
)
cmpccgsCCRFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCRFailures.setStatus("current")
_CmpccgsMessageTypeInvalid_Type = Counter64
_CmpccgsMessageTypeInvalid_Object = MibTableColumn
cmpccgsMessageTypeInvalid = _CmpccgsMessageTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 9),
    _CmpccgsMessageTypeInvalid_Type()
)
cmpccgsMessageTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsMessageTypeInvalid.setStatus("current")
_CmpccgsDuplicateRequests_Type = Counter64
_CmpccgsDuplicateRequests_Object = MibTableColumn
cmpccgsDuplicateRequests = _CmpccgsDuplicateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 10),
    _CmpccgsDuplicateRequests_Type()
)
cmpccgsDuplicateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsDuplicateRequests.setStatus("current")
_CmpccgsCCAErrors_Type = Counter64
_CmpccgsCCAErrors_Object = MibTableColumn
cmpccgsCCAErrors = _CmpccgsCCAErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 11),
    _CmpccgsCCAErrors_Type()
)
cmpccgsCCAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsCCAErrors.setStatus("current")
_CmpccgsRAAFailures_Type = Counter64
_CmpccgsRAAFailures_Object = MibTableColumn
cmpccgsRAAFailures = _CmpccgsRAAFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 12),
    _CmpccgsRAAFailures_Type()
)
cmpccgsRAAFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsRAAFailures.setStatus("current")
_CmpccgsRARErrors_Type = Counter64
_CmpccgsRARErrors_Object = MibTableColumn
cmpccgsRARErrors = _CmpccgsRARErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 13),
    _CmpccgsRARErrors_Type()
)
cmpccgsRARErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsRARErrors.setStatus("current")
_CmpccgsReqTypeInvalid_Type = Counter64
_CmpccgsReqTypeInvalid_Object = MibTableColumn
cmpccgsReqTypeInvalid = _CmpccgsReqTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 14),
    _CmpccgsReqTypeInvalid_Type()
)
cmpccgsReqTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsReqTypeInvalid.setStatus("current")
_CmpccgsReqNumInvalid_Type = Counter64
_CmpccgsReqNumInvalid_Object = MibTableColumn
cmpccgsReqNumInvalid = _CmpccgsReqNumInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 15),
    _CmpccgsReqNumInvalid_Type()
)
cmpccgsReqNumInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsReqNumInvalid.setStatus("current")
_CmpccgsReqStatusInvalid_Type = Counter64
_CmpccgsReqStatusInvalid_Object = MibTableColumn
cmpccgsReqStatusInvalid = _CmpccgsReqStatusInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 16),
    _CmpccgsReqStatusInvalid_Type()
)
cmpccgsReqStatusInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsReqStatusInvalid.setStatus("current")
_CmpccgsSessionIDInvalid_Type = Counter64
_CmpccgsSessionIDInvalid_Object = MibTableColumn
cmpccgsSessionIDInvalid = _CmpccgsSessionIDInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 1, 1, 17),
    _CmpccgsSessionIDInvalid_Type()
)
cmpccgsSessionIDInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccgsSessionIDInvalid.setStatus("current")
_CmpccPCRFMethodListStatsTable_Object = MibTable
cmpccPCRFMethodListStatsTable = _CmpccPCRFMethodListStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmpccPCRFMethodListStatsTable.setStatus("current")
_CmpccPCRFMethodListStatsTableEntry_Object = MibTableRow
cmpccPCRFMethodListStatsTableEntry = _CmpccPCRFMethodListStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1)
)
cmpccPCRFMethodListStatsTableEntry.setIndexNames(
    (0, "CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsMethodList"),
)
if mibBuilder.loadTexts:
    cmpccPCRFMethodListStatsTableEntry.setStatus("current")


class _CmpccpmlsMethodList_Type(SnmpAdminString):
    """Custom type cmpccpmlsMethodList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmpccpmlsMethodList_Type.__name__ = "SnmpAdminString"
_CmpccpmlsMethodList_Object = MibTableColumn
cmpccpmlsMethodList = _CmpccpmlsMethodList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 1),
    _CmpccpmlsMethodList_Type()
)
cmpccpmlsMethodList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmpccpmlsMethodList.setStatus("current")
_CmpccpmlsCCRInitialSent_Type = Counter64
_CmpccpmlsCCRInitialSent_Object = MibTableColumn
cmpccpmlsCCRInitialSent = _CmpccpmlsCCRInitialSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 2),
    _CmpccpmlsCCRInitialSent_Type()
)
cmpccpmlsCCRInitialSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCRInitialSent.setStatus("current")
_CmpccpmlsCCRUpdateSent_Type = Counter64
_CmpccpmlsCCRUpdateSent_Object = MibTableColumn
cmpccpmlsCCRUpdateSent = _CmpccpmlsCCRUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 3),
    _CmpccpmlsCCRUpdateSent_Type()
)
cmpccpmlsCCRUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCRUpdateSent.setStatus("current")
_CmpccpmlsCCRFinalSent_Type = Counter64
_CmpccpmlsCCRFinalSent_Object = MibTableColumn
cmpccpmlsCCRFinalSent = _CmpccpmlsCCRFinalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 4),
    _CmpccpmlsCCRFinalSent_Type()
)
cmpccpmlsCCRFinalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCRFinalSent.setStatus("current")
_CmpccpmlsCCARecd_Type = Counter64
_CmpccpmlsCCARecd_Object = MibTableColumn
cmpccpmlsCCARecd = _CmpccpmlsCCARecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 5),
    _CmpccpmlsCCARecd_Type()
)
cmpccpmlsCCARecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCARecd.setStatus("current")
_CmpccpmlsRARRecd_Type = Counter64
_CmpccpmlsRARRecd_Object = MibTableColumn
cmpccpmlsRARRecd = _CmpccpmlsRARRecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 6),
    _CmpccpmlsRARRecd_Type()
)
cmpccpmlsRARRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsRARRecd.setStatus("current")
_CmpccpmlsRAASent_Type = Counter64
_CmpccpmlsRAASent_Object = MibTableColumn
cmpccpmlsRAASent = _CmpccpmlsRAASent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 7),
    _CmpccpmlsRAASent_Type()
)
cmpccpmlsRAASent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsRAASent.setStatus("current")
_CmpccpmlsPCRFReboots_Type = Counter64
_CmpccpmlsPCRFReboots_Object = MibTableColumn
cmpccpmlsPCRFReboots = _CmpccpmlsPCRFReboots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 8),
    _CmpccpmlsPCRFReboots_Type()
)
cmpccpmlsPCRFReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsPCRFReboots.setStatus("current")
_CmpccpmlsCCRFailures_Type = Counter64
_CmpccpmlsCCRFailures_Object = MibTableColumn
cmpccpmlsCCRFailures = _CmpccpmlsCCRFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 9),
    _CmpccpmlsCCRFailures_Type()
)
cmpccpmlsCCRFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCRFailures.setStatus("current")
_CmpccpmlsMessageTypeInvalid_Type = Counter64
_CmpccpmlsMessageTypeInvalid_Object = MibTableColumn
cmpccpmlsMessageTypeInvalid = _CmpccpmlsMessageTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 10),
    _CmpccpmlsMessageTypeInvalid_Type()
)
cmpccpmlsMessageTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsMessageTypeInvalid.setStatus("current")
_CmpccpmlsDuplicateRequests_Type = Counter64
_CmpccpmlsDuplicateRequests_Object = MibTableColumn
cmpccpmlsDuplicateRequests = _CmpccpmlsDuplicateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 11),
    _CmpccpmlsDuplicateRequests_Type()
)
cmpccpmlsDuplicateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsDuplicateRequests.setStatus("current")
_CmpccpmlsCCAErrors_Type = Counter64
_CmpccpmlsCCAErrors_Object = MibTableColumn
cmpccpmlsCCAErrors = _CmpccpmlsCCAErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 12),
    _CmpccpmlsCCAErrors_Type()
)
cmpccpmlsCCAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsCCAErrors.setStatus("current")
_CmpccpmlsRAAFailures_Type = Counter64
_CmpccpmlsRAAFailures_Object = MibTableColumn
cmpccpmlsRAAFailures = _CmpccpmlsRAAFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 13),
    _CmpccpmlsRAAFailures_Type()
)
cmpccpmlsRAAFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsRAAFailures.setStatus("current")
_CmpccpmlsRARErrors_Type = Counter64
_CmpccpmlsRARErrors_Object = MibTableColumn
cmpccpmlsRARErrors = _CmpccpmlsRARErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 14),
    _CmpccpmlsRARErrors_Type()
)
cmpccpmlsRARErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsRARErrors.setStatus("current")
_CmpccpmlsReqTypeInvalid_Type = Counter64
_CmpccpmlsReqTypeInvalid_Object = MibTableColumn
cmpccpmlsReqTypeInvalid = _CmpccpmlsReqTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 15),
    _CmpccpmlsReqTypeInvalid_Type()
)
cmpccpmlsReqTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsReqTypeInvalid.setStatus("current")
_CmpccpmlsReqNumInvalid_Type = Counter64
_CmpccpmlsReqNumInvalid_Object = MibTableColumn
cmpccpmlsReqNumInvalid = _CmpccpmlsReqNumInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 16),
    _CmpccpmlsReqNumInvalid_Type()
)
cmpccpmlsReqNumInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsReqNumInvalid.setStatus("current")
_CmpccpmlsReqStatusInvalid_Type = Counter64
_CmpccpmlsReqStatusInvalid_Object = MibTableColumn
cmpccpmlsReqStatusInvalid = _CmpccpmlsReqStatusInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 17),
    _CmpccpmlsReqStatusInvalid_Type()
)
cmpccpmlsReqStatusInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsReqStatusInvalid.setStatus("current")
_CmpccpmlsSessionIDInvalid_Type = Counter64
_CmpccpmlsSessionIDInvalid_Object = MibTableColumn
cmpccpmlsSessionIDInvalid = _CmpccpmlsSessionIDInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 2, 1, 18),
    _CmpccpmlsSessionIDInvalid_Type()
)
cmpccpmlsSessionIDInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccpmlsSessionIDInvalid.setStatus("current")
_CmpccPolicyPreloadStatsTable_Object = MibTable
cmpccPolicyPreloadStatsTable = _CmpccPolicyPreloadStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cmpccPolicyPreloadStatsTable.setStatus("current")
_CmpccPolicyPreloadStatsTableEntry_Object = MibTableRow
cmpccPolicyPreloadStatsTableEntry = _CmpccPolicyPreloadStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1)
)
cmpccPolicyPreloadStatsTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmpccPolicyPreloadStatsTableEntry.setStatus("current")


class _CmpccppsPolicyPreloadStatus_Type(Integer32):
    """Custom type cmpccppsPolicyPreloadStatus based on Integer32"""
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
        *(("preloadComplete", 5),
          ("preloadFailed", 3),
          ("preloadInProgress", 2),
          ("preloadNotInitiated", 1),
          ("preloadTimeout", 4))
    )


_CmpccppsPolicyPreloadStatus_Type.__name__ = "Integer32"
_CmpccppsPolicyPreloadStatus_Object = MibTableColumn
cmpccppsPolicyPreloadStatus = _CmpccppsPolicyPreloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 1),
    _CmpccppsPolicyPreloadStatus_Type()
)
cmpccppsPolicyPreloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsPolicyPreloadStatus.setStatus("current")
_CmpccppsPCEFInit_Type = Counter32
_CmpccppsPCEFInit_Object = MibTableColumn
cmpccppsPCEFInit = _CmpccppsPCEFInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 2),
    _CmpccppsPCEFInit_Type()
)
cmpccppsPCEFInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsPCEFInit.setStatus("current")
_CmpccppsPCRFInit_Type = Counter32
_CmpccppsPCRFInit_Object = MibTableColumn
cmpccppsPCRFInit = _CmpccppsPCRFInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 3),
    _CmpccppsPCRFInit_Type()
)
cmpccppsPCRFInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsPCRFInit.setStatus("current")
_CmpccppsReq_Type = Counter32
_CmpccppsReq_Object = MibTableColumn
cmpccppsReq = _CmpccppsReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 4),
    _CmpccppsReq_Type()
)
cmpccppsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsReq.setStatus("current")
_CmpccppsRes_Type = Counter32
_CmpccppsRes_Object = MibTableColumn
cmpccppsRes = _CmpccppsRes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 5),
    _CmpccppsRes_Type()
)
cmpccppsRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsRes.setStatus("current")
_CmpccppsGlobalPolicyPush_Type = Counter32
_CmpccppsGlobalPolicyPush_Object = MibTableColumn
cmpccppsGlobalPolicyPush = _CmpccppsGlobalPolicyPush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 6),
    _CmpccppsGlobalPolicyPush_Type()
)
cmpccppsGlobalPolicyPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsGlobalPolicyPush.setStatus("current")
_CmpccppsGlobalPolicyPushAck_Type = Counter32
_CmpccppsGlobalPolicyPushAck_Object = MibTableColumn
cmpccppsGlobalPolicyPushAck = _CmpccppsGlobalPolicyPushAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 7),
    _CmpccppsGlobalPolicyPushAck_Type()
)
cmpccppsGlobalPolicyPushAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsGlobalPolicyPushAck.setStatus("current")


class _CmpccppsErrorState_Type(Integer32):
    """Custom type cmpccppsErrorState based on Integer32"""
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
        *(("preloadAVPMissing", 2),
          ("preloadEnforceFailure", 3),
          ("preloadInconsistentData", 1),
          ("preloadNoError", 6),
          ("preloadStaticConfigConflict", 5),
          ("preloadWrongOrderFailure", 4))
    )


_CmpccppsErrorState_Type.__name__ = "Integer32"
_CmpccppsErrorState_Object = MibTableColumn
cmpccppsErrorState = _CmpccppsErrorState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 8),
    _CmpccppsErrorState_Type()
)
cmpccppsErrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsErrorState.setStatus("current")
_CmpccppsPreloadDataInconsistent_Type = Counter32
_CmpccppsPreloadDataInconsistent_Object = MibTableColumn
cmpccppsPreloadDataInconsistent = _CmpccppsPreloadDataInconsistent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 9),
    _CmpccppsPreloadDataInconsistent_Type()
)
cmpccppsPreloadDataInconsistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsPreloadDataInconsistent.setStatus("current")
_CmpccppsAVPMissing_Type = Counter32
_CmpccppsAVPMissing_Object = MibTableColumn
cmpccppsAVPMissing = _CmpccppsAVPMissing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 10),
    _CmpccppsAVPMissing_Type()
)
cmpccppsAVPMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAVPMissing.setStatus("current")
_CmpccppsWrongOrderFailures_Type = Counter32
_CmpccppsWrongOrderFailures_Object = MibTableColumn
cmpccppsWrongOrderFailures = _CmpccppsWrongOrderFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 11),
    _CmpccppsWrongOrderFailures_Type()
)
cmpccppsWrongOrderFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsWrongOrderFailures.setStatus("current")
_CmpccppsEnforceFailures_Type = Counter32
_CmpccppsEnforceFailures_Object = MibTableColumn
cmpccppsEnforceFailures = _CmpccppsEnforceFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 12),
    _CmpccppsEnforceFailures_Type()
)
cmpccppsEnforceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsEnforceFailures.setStatus("current")
_CmpccppsStaticConfigConflicts_Type = Counter32
_CmpccppsStaticConfigConflicts_Object = MibTableColumn
cmpccppsStaticConfigConflicts = _CmpccppsStaticConfigConflicts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 13),
    _CmpccppsStaticConfigConflicts_Type()
)
cmpccppsStaticConfigConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsStaticConfigConflicts.setStatus("current")
_CmpccppsCCRFailures_Type = Counter32
_CmpccppsCCRFailures_Object = MibTableColumn
cmpccppsCCRFailures = _CmpccppsCCRFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 14),
    _CmpccppsCCRFailures_Type()
)
cmpccppsCCRFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsCCRFailures.setStatus("current")
_CmpccppsMessageTypeInvalid_Type = Counter32
_CmpccppsMessageTypeInvalid_Object = MibTableColumn
cmpccppsMessageTypeInvalid = _CmpccppsMessageTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 15),
    _CmpccppsMessageTypeInvalid_Type()
)
cmpccppsMessageTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsMessageTypeInvalid.setStatus("current")
_CmpccppsCCAErrors_Type = Counter32
_CmpccppsCCAErrors_Object = MibTableColumn
cmpccppsCCAErrors = _CmpccppsCCAErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 16),
    _CmpccppsCCAErrors_Type()
)
cmpccppsCCAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsCCAErrors.setStatus("current")
_CmpccppsRAAFailed_Type = Counter32
_CmpccppsRAAFailed_Object = MibTableColumn
cmpccppsRAAFailed = _CmpccppsRAAFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 17),
    _CmpccppsRAAFailed_Type()
)
cmpccppsRAAFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsRAAFailed.setStatus("current")
_CmpccppsRARErrors_Type = Counter32
_CmpccppsRARErrors_Object = MibTableColumn
cmpccppsRARErrors = _CmpccppsRARErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 18),
    _CmpccppsRARErrors_Type()
)
cmpccppsRARErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsRARErrors.setStatus("current")
_CmpccppsReqTypeInvalid_Type = Counter32
_CmpccppsReqTypeInvalid_Object = MibTableColumn
cmpccppsReqTypeInvalid = _CmpccppsReqTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 19),
    _CmpccppsReqTypeInvalid_Type()
)
cmpccppsReqTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsReqTypeInvalid.setStatus("current")
_CmpccppsReqNumInvalid_Type = Counter32
_CmpccppsReqNumInvalid_Object = MibTableColumn
cmpccppsReqNumInvalid = _CmpccppsReqNumInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 20),
    _CmpccppsReqNumInvalid_Type()
)
cmpccppsReqNumInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsReqNumInvalid.setStatus("current")
_CmpccppsReqStatusInvalid_Type = Counter32
_CmpccppsReqStatusInvalid_Object = MibTableColumn
cmpccppsReqStatusInvalid = _CmpccppsReqStatusInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 21),
    _CmpccppsReqStatusInvalid_Type()
)
cmpccppsReqStatusInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsReqStatusInvalid.setStatus("current")
_CmpccppsSessionIDInvalid_Type = Counter32
_CmpccppsSessionIDInvalid_Object = MibTableColumn
cmpccppsSessionIDInvalid = _CmpccppsSessionIDInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 22),
    _CmpccppsSessionIDInvalid_Type()
)
cmpccppsSessionIDInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsSessionIDInvalid.setStatus("current")
_CmpccppsTimeoutErrors_Type = Counter32
_CmpccppsTimeoutErrors_Object = MibTableColumn
cmpccppsTimeoutErrors = _CmpccppsTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 3, 1, 23),
    _CmpccppsTimeoutErrors_Type()
)
cmpccppsTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsTimeoutErrors.setStatus("current")
_CmpccPolicyPreloadExtStatsTable_Object = MibTable
cmpccPolicyPreloadExtStatsTable = _CmpccPolicyPreloadExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cmpccPolicyPreloadExtStatsTable.setStatus("current")
_CmpccPolicyPreloadExtStatsTableEntry_Object = MibTableRow
cmpccPolicyPreloadExtStatsTableEntry = _CmpccPolicyPreloadExtStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1)
)
cmpccPolicyPreloadExtStatsTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmpccPolicyPreloadExtStatsTableEntry.setStatus("current")
_CmpccppsServiceContentsInserted_Type = Counter32
_CmpccppsServiceContentsInserted_Object = MibTableColumn
cmpccppsServiceContentsInserted = _CmpccppsServiceContentsInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 1),
    _CmpccppsServiceContentsInserted_Type()
)
cmpccppsServiceContentsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsInserted.setStatus("current")
_CmpccppsServiceContentsDeleted_Type = Counter32
_CmpccppsServiceContentsDeleted_Object = MibTableColumn
cmpccppsServiceContentsDeleted = _CmpccppsServiceContentsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 2),
    _CmpccppsServiceContentsDeleted_Type()
)
cmpccppsServiceContentsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsDeleted.setStatus("current")
_CmpccppsServiceContentsRolledback_Type = Counter32
_CmpccppsServiceContentsRolledback_Object = MibTableColumn
cmpccppsServiceContentsRolledback = _CmpccppsServiceContentsRolledback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 3),
    _CmpccppsServiceContentsRolledback_Type()
)
cmpccppsServiceContentsRolledback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsRolledback.setStatus("current")
_CmpccppsServiceContentsInsertFailed_Type = Counter32
_CmpccppsServiceContentsInsertFailed_Object = MibTableColumn
cmpccppsServiceContentsInsertFailed = _CmpccppsServiceContentsInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 4),
    _CmpccppsServiceContentsInsertFailed_Type()
)
cmpccppsServiceContentsInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsInsertFailed.setStatus("current")
_CmpccppsServiceContentsDeleteFailed_Type = Counter32
_CmpccppsServiceContentsDeleteFailed_Object = MibTableColumn
cmpccppsServiceContentsDeleteFailed = _CmpccppsServiceContentsDeleteFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 5),
    _CmpccppsServiceContentsDeleteFailed_Type()
)
cmpccppsServiceContentsDeleteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsDeleteFailed.setStatus("current")
_CmpccppsServiceContentsRollbackFailed_Type = Counter32
_CmpccppsServiceContentsRollbackFailed_Object = MibTableColumn
cmpccppsServiceContentsRollbackFailed = _CmpccppsServiceContentsRollbackFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 6),
    _CmpccppsServiceContentsRollbackFailed_Type()
)
cmpccppsServiceContentsRollbackFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsServiceContentsRollbackFailed.setStatus("current")
_CmpccppsAcctPolicyMapsInserted_Type = Counter32
_CmpccppsAcctPolicyMapsInserted_Object = MibTableColumn
cmpccppsAcctPolicyMapsInserted = _CmpccppsAcctPolicyMapsInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 7),
    _CmpccppsAcctPolicyMapsInserted_Type()
)
cmpccppsAcctPolicyMapsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsInserted.setStatus("current")
_CmpccppsAcctPolicyMapsDeleted_Type = Counter32
_CmpccppsAcctPolicyMapsDeleted_Object = MibTableColumn
cmpccppsAcctPolicyMapsDeleted = _CmpccppsAcctPolicyMapsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 8),
    _CmpccppsAcctPolicyMapsDeleted_Type()
)
cmpccppsAcctPolicyMapsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsDeleted.setStatus("current")
_CmpccppsAcctPolicyMapsRolledback_Type = Counter32
_CmpccppsAcctPolicyMapsRolledback_Object = MibTableColumn
cmpccppsAcctPolicyMapsRolledback = _CmpccppsAcctPolicyMapsRolledback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 9),
    _CmpccppsAcctPolicyMapsRolledback_Type()
)
cmpccppsAcctPolicyMapsRolledback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsRolledback.setStatus("current")
_CmpccppsAcctPolicyMapsInsertFailed_Type = Counter32
_CmpccppsAcctPolicyMapsInsertFailed_Object = MibTableColumn
cmpccppsAcctPolicyMapsInsertFailed = _CmpccppsAcctPolicyMapsInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 10),
    _CmpccppsAcctPolicyMapsInsertFailed_Type()
)
cmpccppsAcctPolicyMapsInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsInsertFailed.setStatus("current")
_CmpccppsAcctPolicyMapsDeleteFailed_Type = Counter32
_CmpccppsAcctPolicyMapsDeleteFailed_Object = MibTableColumn
cmpccppsAcctPolicyMapsDeleteFailed = _CmpccppsAcctPolicyMapsDeleteFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 11),
    _CmpccppsAcctPolicyMapsDeleteFailed_Type()
)
cmpccppsAcctPolicyMapsDeleteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsDeleteFailed.setStatus("current")
_CmpccppsAcctPolicyMapsRollbackFailed_Type = Counter32
_CmpccppsAcctPolicyMapsRollbackFailed_Object = MibTableColumn
cmpccppsAcctPolicyMapsRollbackFailed = _CmpccppsAcctPolicyMapsRollbackFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 12),
    _CmpccppsAcctPolicyMapsRollbackFailed_Type()
)
cmpccppsAcctPolicyMapsRollbackFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsAcctPolicyMapsRollbackFailed.setStatus("current")
_CmpccppsBillingServicesInserted_Type = Counter32
_CmpccppsBillingServicesInserted_Object = MibTableColumn
cmpccppsBillingServicesInserted = _CmpccppsBillingServicesInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 13),
    _CmpccppsBillingServicesInserted_Type()
)
cmpccppsBillingServicesInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesInserted.setStatus("current")
_CmpccppsBillingServicesDeleted_Type = Counter32
_CmpccppsBillingServicesDeleted_Object = MibTableColumn
cmpccppsBillingServicesDeleted = _CmpccppsBillingServicesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 14),
    _CmpccppsBillingServicesDeleted_Type()
)
cmpccppsBillingServicesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesDeleted.setStatus("current")
_CmpccppsBillingServicesRolledback_Type = Counter32
_CmpccppsBillingServicesRolledback_Object = MibTableColumn
cmpccppsBillingServicesRolledback = _CmpccppsBillingServicesRolledback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 15),
    _CmpccppsBillingServicesRolledback_Type()
)
cmpccppsBillingServicesRolledback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesRolledback.setStatus("current")
_CmpccppsBillingServicesInsertFailed_Type = Counter32
_CmpccppsBillingServicesInsertFailed_Object = MibTableColumn
cmpccppsBillingServicesInsertFailed = _CmpccppsBillingServicesInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 16),
    _CmpccppsBillingServicesInsertFailed_Type()
)
cmpccppsBillingServicesInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesInsertFailed.setStatus("current")
_CmpccppsBillingServicesDeleteFailed_Type = Counter32
_CmpccppsBillingServicesDeleteFailed_Object = MibTableColumn
cmpccppsBillingServicesDeleteFailed = _CmpccppsBillingServicesDeleteFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 17),
    _CmpccppsBillingServicesDeleteFailed_Type()
)
cmpccppsBillingServicesDeleteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesDeleteFailed.setStatus("current")
_CmpccppsBillingServicesRollbackFailed_Type = Counter32
_CmpccppsBillingServicesRollbackFailed_Object = MibTableColumn
cmpccppsBillingServicesRollbackFailed = _CmpccppsBillingServicesRollbackFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 18),
    _CmpccppsBillingServicesRollbackFailed_Type()
)
cmpccppsBillingServicesRollbackFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingServicesRollbackFailed.setStatus("current")
_CmpccppsContentPoliciesInserted_Type = Counter32
_CmpccppsContentPoliciesInserted_Object = MibTableColumn
cmpccppsContentPoliciesInserted = _CmpccppsContentPoliciesInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 19),
    _CmpccppsContentPoliciesInserted_Type()
)
cmpccppsContentPoliciesInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesInserted.setStatus("current")
_CmpccppsContentPoliciesDeleted_Type = Counter32
_CmpccppsContentPoliciesDeleted_Object = MibTableColumn
cmpccppsContentPoliciesDeleted = _CmpccppsContentPoliciesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 20),
    _CmpccppsContentPoliciesDeleted_Type()
)
cmpccppsContentPoliciesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesDeleted.setStatus("current")
_CmpccppsContentPoliciesRolledback_Type = Counter32
_CmpccppsContentPoliciesRolledback_Object = MibTableColumn
cmpccppsContentPoliciesRolledback = _CmpccppsContentPoliciesRolledback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 21),
    _CmpccppsContentPoliciesRolledback_Type()
)
cmpccppsContentPoliciesRolledback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesRolledback.setStatus("current")
_CmpccppsContentPoliciesInsertFailed_Type = Counter32
_CmpccppsContentPoliciesInsertFailed_Object = MibTableColumn
cmpccppsContentPoliciesInsertFailed = _CmpccppsContentPoliciesInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 22),
    _CmpccppsContentPoliciesInsertFailed_Type()
)
cmpccppsContentPoliciesInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesInsertFailed.setStatus("current")
_CmpccppsContentPoliciesDeleteFailed_Type = Counter32
_CmpccppsContentPoliciesDeleteFailed_Object = MibTableColumn
cmpccppsContentPoliciesDeleteFailed = _CmpccppsContentPoliciesDeleteFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 23),
    _CmpccppsContentPoliciesDeleteFailed_Type()
)
cmpccppsContentPoliciesDeleteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesDeleteFailed.setStatus("current")
_CmpccppsContentPoliciesRollbackFailed_Type = Counter32
_CmpccppsContentPoliciesRollbackFailed_Object = MibTableColumn
cmpccppsContentPoliciesRollbackFailed = _CmpccppsContentPoliciesRollbackFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 24),
    _CmpccppsContentPoliciesRollbackFailed_Type()
)
cmpccppsContentPoliciesRollbackFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsContentPoliciesRollbackFailed.setStatus("current")
_CmpccppsBillingPlansInserted_Type = Counter32
_CmpccppsBillingPlansInserted_Object = MibTableColumn
cmpccppsBillingPlansInserted = _CmpccppsBillingPlansInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 25),
    _CmpccppsBillingPlansInserted_Type()
)
cmpccppsBillingPlansInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansInserted.setStatus("current")
_CmpccppsBillingPlansDeleted_Type = Counter32
_CmpccppsBillingPlansDeleted_Object = MibTableColumn
cmpccppsBillingPlansDeleted = _CmpccppsBillingPlansDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 26),
    _CmpccppsBillingPlansDeleted_Type()
)
cmpccppsBillingPlansDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansDeleted.setStatus("current")
_CmpccppsBillingPlansRolledback_Type = Counter32
_CmpccppsBillingPlansRolledback_Object = MibTableColumn
cmpccppsBillingPlansRolledback = _CmpccppsBillingPlansRolledback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 27),
    _CmpccppsBillingPlansRolledback_Type()
)
cmpccppsBillingPlansRolledback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansRolledback.setStatus("current")
_CmpccppsBillingPlansInsertFailed_Type = Counter32
_CmpccppsBillingPlansInsertFailed_Object = MibTableColumn
cmpccppsBillingPlansInsertFailed = _CmpccppsBillingPlansInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 28),
    _CmpccppsBillingPlansInsertFailed_Type()
)
cmpccppsBillingPlansInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansInsertFailed.setStatus("current")
_CmpccppsBillingPlansDeleteFailed_Type = Counter32
_CmpccppsBillingPlansDeleteFailed_Object = MibTableColumn
cmpccppsBillingPlansDeleteFailed = _CmpccppsBillingPlansDeleteFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 29),
    _CmpccppsBillingPlansDeleteFailed_Type()
)
cmpccppsBillingPlansDeleteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansDeleteFailed.setStatus("current")
_CmpccppsBillingPlansRollbackFailed_Type = Counter32
_CmpccppsBillingPlansRollbackFailed_Object = MibTableColumn
cmpccppsBillingPlansRollbackFailed = _CmpccppsBillingPlansRollbackFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 4, 1, 30),
    _CmpccppsBillingPlansRollbackFailed_Type()
)
cmpccppsBillingPlansRollbackFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccppsBillingPlansRollbackFailed.setStatus("current")
_CmpccPolicyMismatch_Type = Counter64
_CmpccPolicyMismatch_Object = MibScalar
cmpccPolicyMismatch = _CmpccPolicyMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 5),
    _CmpccPolicyMismatch_Type()
)
cmpccPolicyMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccPolicyMismatch.setStatus("current")


class _CmpccRollbackFailedReason_Type(Integer32):
    """Custom type cmpccRollbackFailedReason based on Integer32"""
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
        *(("acctPolicyMap", 2),
          ("billingPlan", 6),
          ("billingService", 5),
          ("contentPolicy", 3),
          ("none", 1),
          ("serviceContent", 4))
    )


_CmpccRollbackFailedReason_Type.__name__ = "Integer32"
_CmpccRollbackFailedReason_Object = MibScalar
cmpccRollbackFailedReason = _CmpccRollbackFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 2, 6),
    _CmpccRollbackFailedReason_Type()
)
cmpccRollbackFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpccRollbackFailedReason.setStatus("current")
_CmpccNotifConfig_ObjectIdentity = ObjectIdentity
cmpccNotifConfig = _CmpccNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 3)
)


class _CmpccPreloadErrorNotifEnabled_Type(TruthValue):
    """Custom type cmpccPreloadErrorNotifEnabled based on TruthValue"""


_CmpccPreloadErrorNotifEnabled_Object = MibScalar
cmpccPreloadErrorNotifEnabled = _CmpccPreloadErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 3, 1),
    _CmpccPreloadErrorNotifEnabled_Type()
)
cmpccPreloadErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccPreloadErrorNotifEnabled.setStatus("current")
_CmpccPreloadRollbackFailedNotifEnabled_Type = TruthValue
_CmpccPreloadRollbackFailedNotifEnabled_Object = MibScalar
cmpccPreloadRollbackFailedNotifEnabled = _CmpccPreloadRollbackFailedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 1, 3, 2),
    _CmpccPreloadRollbackFailedNotifEnabled_Type()
)
cmpccPreloadRollbackFailedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpccPreloadRollbackFailedNotifEnabled.setStatus("current")
_CMobilePolicyChargingControlMIBConform_ObjectIdentity = ObjectIdentity
cMobilePolicyChargingControlMIBConform = _CMobilePolicyChargingControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2)
)
_CMobilePolicyChargingControlMIBCompliances_ObjectIdentity = ObjectIdentity
cMobilePolicyChargingControlMIBCompliances = _CMobilePolicyChargingControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 1)
)
_CMobilePolicyChargingControlMIBGroups_ObjectIdentity = ObjectIdentity
cMobilePolicyChargingControlMIBGroups = _CMobilePolicyChargingControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2)
)

# Managed Objects groups

cMobilePolicyChargingControlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 1)
)
cMobilePolicyChargingControlConfigGroup.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPreloadEnable"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccProfileDefault"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccMethodListPreload"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPreloadTimeout"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpcRowStatus"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccDestinationRealmString"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpcDestinationRealm"))
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlConfigGroup.setStatus("current")

cMobilePolicyChargingControlGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 2)
)
cMobilePolicyChargingControlGlobalStatsGroup.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsTotalSessions"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCRInitialSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCRUpdateSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCRFinalSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCARecd"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsRARRecd"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsRAASent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCRFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsRAAFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsReqTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsReqNumInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsReqStatusInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsMessageTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsDuplicateRequests"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsCCAErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsRARErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccgsSessionIDInvalid"))
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlGlobalStatsGroup.setStatus("current")

cMobilePolicyChargingControlPCRFMethodListStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 3)
)
cMobilePolicyChargingControlPCRFMethodListStatsGroup.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCRInitialSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCRUpdateSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCRFinalSent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCARecd"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsRARRecd"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsRAASent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCRFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsRAAFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsReqTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsReqNumInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsReqStatusInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsPCRFReboots"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsMessageTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsDuplicateRequests"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsCCAErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsRARErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccpmlsSessionIDInvalid"))
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlPCRFMethodListStatsGroup.setStatus("current")

cMobilePolicyChargingControlPolicyPreloadStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 4)
)
cMobilePolicyChargingControlPolicyPreloadStatsGroup.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsPCEFInit"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsPCRFInit"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsReq"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsRes"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsGlobalPolicyPush"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsGlobalPolicyPushAck"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsPreloadDataInconsistent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAVPMissing"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsWrongOrderFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsEnforceFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsStaticConfigConflicts"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsCCRFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsRAAFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsReqTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsReqNumInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsReqStatusInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsErrorState"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsPolicyPreloadStatus"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsMessageTypeInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsCCAErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsRARErrors"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsSessionIDInvalid"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsTimeoutErrors"))
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlPolicyPreloadStatsGroup.setStatus("current")

cMobilePolicyChargingControlNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 6)
)
cMobilePolicyChargingControlNotifEnableGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPreloadErrorNotifEnabled")
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlNotifEnableGroup.setStatus("current")

cmpccStatisticsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 7)
)
cmpccStatisticsExtGroup.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesInserted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesDeleted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesRolledback"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesInsertFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesDeleteFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingServicesRollbackFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesInserted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesDeleted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesRolledback"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesInsertFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesDeleteFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsContentPoliciesRollbackFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansInserted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansDeleted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansRolledback"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansInsertFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansDeleteFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsBillingPlansRollbackFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsInserted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsDeleted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsRolledback"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsInsertFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsDeleteFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsServiceContentsRollbackFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsInserted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsDeleted"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsRolledback"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsInsertFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsDeleteFailed"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAcctPolicyMapsRollbackFailed"))
)
if mibBuilder.loadTexts:
    cmpccStatisticsExtGroup.setStatus("current")

cmpccPreloadNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 9)
)
cmpccPreloadNotifControlGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPreloadRollbackFailedNotifEnabled")
)
if mibBuilder.loadTexts:
    cmpccPreloadNotifControlGroup.setStatus("current")

cmpccPolicyMismatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 10)
)
cmpccPolicyMismatchGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPolicyMismatch")
)
if mibBuilder.loadTexts:
    cmpccPolicyMismatchGroup.setStatus("current")

cmpccRollbackFailedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 11)
)
cmpccRollbackFailedGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccRollbackFailedReason")
)
if mibBuilder.loadTexts:
    cmpccRollbackFailedGroup.setStatus("current")


# Notification objects

ciscoMobilePolicyChargingControlPreloadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 0, 1)
)
ciscoMobilePolicyChargingControlPreloadError.setObjects(
      *(("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsErrorState"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsPreloadDataInconsistent"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsAVPMissing"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsEnforceFailures"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsStaticConfigConflicts"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccppsWrongOrderFailures"))
)
if mibBuilder.loadTexts:
    ciscoMobilePolicyChargingControlPreloadError.setStatus(
        "current"
    )

cmpccPreloadRollbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 0, 2)
)
cmpccPreloadRollbackFailed.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccRollbackFailedReason"))
)
if mibBuilder.loadTexts:
    cmpccPreloadRollbackFailed.setStatus(
        "current"
    )


# Notifications groups

cMobilePolicyChargingControlNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 5)
)
cMobilePolicyChargingControlNotifGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "ciscoMobilePolicyChargingControlPreloadError")
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlNotifGroup.setStatus(
        "current"
    )

cmpccPolicyPreloadNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 2, 8)
)
cmpccPolicyPreloadNotifGroup.setObjects(
    ("CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB", "cmpccPreloadRollbackFailed")
)
if mibBuilder.loadTexts:
    cmpccPolicyPreloadNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cMobilePolicyChargingControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlMIBCompliance.setStatus(
        "deprecated"
    )

cMobilePolicyChargingControlMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 690, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cMobilePolicyChargingControlMIBCompliancesRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MOBILE-POLICY-CHARGING-CONTROL-MIB",
    **{"ciscoMobilePolicyChargingControlMIB": ciscoMobilePolicyChargingControlMIB,
       "ciscoMobilePolicyChargingControlMIBNotifs": ciscoMobilePolicyChargingControlMIBNotifs,
       "ciscoMobilePolicyChargingControlPreloadError": ciscoMobilePolicyChargingControlPreloadError,
       "cmpccPreloadRollbackFailed": cmpccPreloadRollbackFailed,
       "ciscoMobilePolicyChargingControlMIBObjects": ciscoMobilePolicyChargingControlMIBObjects,
       "cmpccConfig": cmpccConfig,
       "cmpccProfileConfigTable": cmpccProfileConfigTable,
       "cmpccProfileConfigTableEntry": cmpccProfileConfigTableEntry,
       "cmpccpcProfileName": cmpccpcProfileName,
       "cmpccpcMethodList": cmpccpcMethodList,
       "cmpccpcDestinationRealm": cmpccpcDestinationRealm,
       "cmpccpcRowStatus": cmpccpcRowStatus,
       "cmpccPreloadEnable": cmpccPreloadEnable,
       "cmpccProfileDefault": cmpccProfileDefault,
       "cmpccMethodListPreload": cmpccMethodListPreload,
       "cmpccDestinationRealmString": cmpccDestinationRealmString,
       "cmpccPreloadTimeout": cmpccPreloadTimeout,
       "cmpccStats": cmpccStats,
       "cmpccGlobalStatsTable": cmpccGlobalStatsTable,
       "cmpccGlobalStatsTableEntry": cmpccGlobalStatsTableEntry,
       "cmpccgsTotalSessions": cmpccgsTotalSessions,
       "cmpccgsCCRInitialSent": cmpccgsCCRInitialSent,
       "cmpccgsCCRUpdateSent": cmpccgsCCRUpdateSent,
       "cmpccgsCCRFinalSent": cmpccgsCCRFinalSent,
       "cmpccgsCCARecd": cmpccgsCCARecd,
       "cmpccgsRARRecd": cmpccgsRARRecd,
       "cmpccgsRAASent": cmpccgsRAASent,
       "cmpccgsCCRFailures": cmpccgsCCRFailures,
       "cmpccgsMessageTypeInvalid": cmpccgsMessageTypeInvalid,
       "cmpccgsDuplicateRequests": cmpccgsDuplicateRequests,
       "cmpccgsCCAErrors": cmpccgsCCAErrors,
       "cmpccgsRAAFailures": cmpccgsRAAFailures,
       "cmpccgsRARErrors": cmpccgsRARErrors,
       "cmpccgsReqTypeInvalid": cmpccgsReqTypeInvalid,
       "cmpccgsReqNumInvalid": cmpccgsReqNumInvalid,
       "cmpccgsReqStatusInvalid": cmpccgsReqStatusInvalid,
       "cmpccgsSessionIDInvalid": cmpccgsSessionIDInvalid,
       "cmpccPCRFMethodListStatsTable": cmpccPCRFMethodListStatsTable,
       "cmpccPCRFMethodListStatsTableEntry": cmpccPCRFMethodListStatsTableEntry,
       "cmpccpmlsMethodList": cmpccpmlsMethodList,
       "cmpccpmlsCCRInitialSent": cmpccpmlsCCRInitialSent,
       "cmpccpmlsCCRUpdateSent": cmpccpmlsCCRUpdateSent,
       "cmpccpmlsCCRFinalSent": cmpccpmlsCCRFinalSent,
       "cmpccpmlsCCARecd": cmpccpmlsCCARecd,
       "cmpccpmlsRARRecd": cmpccpmlsRARRecd,
       "cmpccpmlsRAASent": cmpccpmlsRAASent,
       "cmpccpmlsPCRFReboots": cmpccpmlsPCRFReboots,
       "cmpccpmlsCCRFailures": cmpccpmlsCCRFailures,
       "cmpccpmlsMessageTypeInvalid": cmpccpmlsMessageTypeInvalid,
       "cmpccpmlsDuplicateRequests": cmpccpmlsDuplicateRequests,
       "cmpccpmlsCCAErrors": cmpccpmlsCCAErrors,
       "cmpccpmlsRAAFailures": cmpccpmlsRAAFailures,
       "cmpccpmlsRARErrors": cmpccpmlsRARErrors,
       "cmpccpmlsReqTypeInvalid": cmpccpmlsReqTypeInvalid,
       "cmpccpmlsReqNumInvalid": cmpccpmlsReqNumInvalid,
       "cmpccpmlsReqStatusInvalid": cmpccpmlsReqStatusInvalid,
       "cmpccpmlsSessionIDInvalid": cmpccpmlsSessionIDInvalid,
       "cmpccPolicyPreloadStatsTable": cmpccPolicyPreloadStatsTable,
       "cmpccPolicyPreloadStatsTableEntry": cmpccPolicyPreloadStatsTableEntry,
       "cmpccppsPolicyPreloadStatus": cmpccppsPolicyPreloadStatus,
       "cmpccppsPCEFInit": cmpccppsPCEFInit,
       "cmpccppsPCRFInit": cmpccppsPCRFInit,
       "cmpccppsReq": cmpccppsReq,
       "cmpccppsRes": cmpccppsRes,
       "cmpccppsGlobalPolicyPush": cmpccppsGlobalPolicyPush,
       "cmpccppsGlobalPolicyPushAck": cmpccppsGlobalPolicyPushAck,
       "cmpccppsErrorState": cmpccppsErrorState,
       "cmpccppsPreloadDataInconsistent": cmpccppsPreloadDataInconsistent,
       "cmpccppsAVPMissing": cmpccppsAVPMissing,
       "cmpccppsWrongOrderFailures": cmpccppsWrongOrderFailures,
       "cmpccppsEnforceFailures": cmpccppsEnforceFailures,
       "cmpccppsStaticConfigConflicts": cmpccppsStaticConfigConflicts,
       "cmpccppsCCRFailures": cmpccppsCCRFailures,
       "cmpccppsMessageTypeInvalid": cmpccppsMessageTypeInvalid,
       "cmpccppsCCAErrors": cmpccppsCCAErrors,
       "cmpccppsRAAFailed": cmpccppsRAAFailed,
       "cmpccppsRARErrors": cmpccppsRARErrors,
       "cmpccppsReqTypeInvalid": cmpccppsReqTypeInvalid,
       "cmpccppsReqNumInvalid": cmpccppsReqNumInvalid,
       "cmpccppsReqStatusInvalid": cmpccppsReqStatusInvalid,
       "cmpccppsSessionIDInvalid": cmpccppsSessionIDInvalid,
       "cmpccppsTimeoutErrors": cmpccppsTimeoutErrors,
       "cmpccPolicyPreloadExtStatsTable": cmpccPolicyPreloadExtStatsTable,
       "cmpccPolicyPreloadExtStatsTableEntry": cmpccPolicyPreloadExtStatsTableEntry,
       "cmpccppsServiceContentsInserted": cmpccppsServiceContentsInserted,
       "cmpccppsServiceContentsDeleted": cmpccppsServiceContentsDeleted,
       "cmpccppsServiceContentsRolledback": cmpccppsServiceContentsRolledback,
       "cmpccppsServiceContentsInsertFailed": cmpccppsServiceContentsInsertFailed,
       "cmpccppsServiceContentsDeleteFailed": cmpccppsServiceContentsDeleteFailed,
       "cmpccppsServiceContentsRollbackFailed": cmpccppsServiceContentsRollbackFailed,
       "cmpccppsAcctPolicyMapsInserted": cmpccppsAcctPolicyMapsInserted,
       "cmpccppsAcctPolicyMapsDeleted": cmpccppsAcctPolicyMapsDeleted,
       "cmpccppsAcctPolicyMapsRolledback": cmpccppsAcctPolicyMapsRolledback,
       "cmpccppsAcctPolicyMapsInsertFailed": cmpccppsAcctPolicyMapsInsertFailed,
       "cmpccppsAcctPolicyMapsDeleteFailed": cmpccppsAcctPolicyMapsDeleteFailed,
       "cmpccppsAcctPolicyMapsRollbackFailed": cmpccppsAcctPolicyMapsRollbackFailed,
       "cmpccppsBillingServicesInserted": cmpccppsBillingServicesInserted,
       "cmpccppsBillingServicesDeleted": cmpccppsBillingServicesDeleted,
       "cmpccppsBillingServicesRolledback": cmpccppsBillingServicesRolledback,
       "cmpccppsBillingServicesInsertFailed": cmpccppsBillingServicesInsertFailed,
       "cmpccppsBillingServicesDeleteFailed": cmpccppsBillingServicesDeleteFailed,
       "cmpccppsBillingServicesRollbackFailed": cmpccppsBillingServicesRollbackFailed,
       "cmpccppsContentPoliciesInserted": cmpccppsContentPoliciesInserted,
       "cmpccppsContentPoliciesDeleted": cmpccppsContentPoliciesDeleted,
       "cmpccppsContentPoliciesRolledback": cmpccppsContentPoliciesRolledback,
       "cmpccppsContentPoliciesInsertFailed": cmpccppsContentPoliciesInsertFailed,
       "cmpccppsContentPoliciesDeleteFailed": cmpccppsContentPoliciesDeleteFailed,
       "cmpccppsContentPoliciesRollbackFailed": cmpccppsContentPoliciesRollbackFailed,
       "cmpccppsBillingPlansInserted": cmpccppsBillingPlansInserted,
       "cmpccppsBillingPlansDeleted": cmpccppsBillingPlansDeleted,
       "cmpccppsBillingPlansRolledback": cmpccppsBillingPlansRolledback,
       "cmpccppsBillingPlansInsertFailed": cmpccppsBillingPlansInsertFailed,
       "cmpccppsBillingPlansDeleteFailed": cmpccppsBillingPlansDeleteFailed,
       "cmpccppsBillingPlansRollbackFailed": cmpccppsBillingPlansRollbackFailed,
       "cmpccPolicyMismatch": cmpccPolicyMismatch,
       "cmpccRollbackFailedReason": cmpccRollbackFailedReason,
       "cmpccNotifConfig": cmpccNotifConfig,
       "cmpccPreloadErrorNotifEnabled": cmpccPreloadErrorNotifEnabled,
       "cmpccPreloadRollbackFailedNotifEnabled": cmpccPreloadRollbackFailedNotifEnabled,
       "cMobilePolicyChargingControlMIBConform": cMobilePolicyChargingControlMIBConform,
       "cMobilePolicyChargingControlMIBCompliances": cMobilePolicyChargingControlMIBCompliances,
       "cMobilePolicyChargingControlMIBCompliance": cMobilePolicyChargingControlMIBCompliance,
       "cMobilePolicyChargingControlMIBCompliancesRev1": cMobilePolicyChargingControlMIBCompliancesRev1,
       "cMobilePolicyChargingControlMIBGroups": cMobilePolicyChargingControlMIBGroups,
       "cMobilePolicyChargingControlConfigGroup": cMobilePolicyChargingControlConfigGroup,
       "cMobilePolicyChargingControlGlobalStatsGroup": cMobilePolicyChargingControlGlobalStatsGroup,
       "cMobilePolicyChargingControlPCRFMethodListStatsGroup": cMobilePolicyChargingControlPCRFMethodListStatsGroup,
       "cMobilePolicyChargingControlPolicyPreloadStatsGroup": cMobilePolicyChargingControlPolicyPreloadStatsGroup,
       "cMobilePolicyChargingControlNotifGroup": cMobilePolicyChargingControlNotifGroup,
       "cMobilePolicyChargingControlNotifEnableGroup": cMobilePolicyChargingControlNotifEnableGroup,
       "cmpccStatisticsExtGroup": cmpccStatisticsExtGroup,
       "cmpccPolicyPreloadNotifGroup": cmpccPolicyPreloadNotifGroup,
       "cmpccPreloadNotifControlGroup": cmpccPreloadNotifControlGroup,
       "cmpccPolicyMismatchGroup": cmpccPolicyMismatchGroup,
       "cmpccRollbackFailedGroup": cmpccRollbackFailedGroup}
)
